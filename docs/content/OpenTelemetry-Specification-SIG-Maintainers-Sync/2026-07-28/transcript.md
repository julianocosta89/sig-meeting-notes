SIG: OpenTelemetry Specification SIG + Maintainers Sync
Date: 2026-07-28
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Daniel Dyla (Dynatrace LLC)** 01:07 Should we put the meeting link in the top of the document or something? It's… A little bit annoying to find.
**Tigran Najaryan (Splunk Inc.)** 01:16 Yeah, that's a good point.
Let me do that.
**Daniel Dyla (Dynatrace LLC)** 01:21 Yeah.
**Armin (Dynatrace)** 02:18 Thanks for the hint. For some reason, my Zoom client still has the old Zoom link somewhere.
**Diego Hurtado** 02:25 Yeah, no problem. I also need to update my calendar.
Because I copied the OpenTelemetry calendar event into another one.
And I had to do it again for that.
I copied the one with the right link now.
**Daniel Dyla (Dynatrace LLC)** 02:41 My Outlook is not… or my Outlook Zoom integration does not detect these new LFX links as Zoom meetings, so now they don't show up in my client at all.
And… It's a more frustrating… a minor frustration, but it is a frustration.
Does anyone know if I copy the link?
In the top left of the meeting, there's the little, like, info, and there's a normal Zoom link in there. Does anybody know if that link is stable?
**Diego Hurtado** 03:15 Do I.
**Daniel Dyla (Dynatrace LLC)** 03:15 The meeting ID?
I think…
**Armin (Dynatrace)** 03:18 You know.
**Daniel Dyla (Dynatrace LLC)** 03:19 I can't… can you share your screen? Can you share Zoom, I think Zoom hides itself from itself. I could try. Somebody else.
**Diego Hurtado** 03:29 Oh, yeah, yeah.
I, I'm running this from my browser soon.
**Daniel Dyla (Dynatrace LLC)** 03:34 Yeah, so in the Zoom client.
at the top left of every meeting, there's a little, like, eye and a circle, and if you click that, it gives you various… like, it tells you who the host is, and the meeting ID, and stuff like that, and there's a link there that's just a standard Zoom link.
Does anybody know if that is stable?
**Trask Stalnaker** 03:55 The link on the… if you… I'm not sure which link you're talking about, but the link that's… if you go to the Google Calendar, the OpenTelemetry Google Calendar, there is… we're not updating that each… Each week, so that is… should be status.
**Daniel Dyla (Dynatrace LLC)** 04:11 I know that that link is stable, but that's a ZoomLFXplatformlinuxfoundation.org.
**Trask Stalnaker** 04:19 Oh, it redirected.
**Daniel Dyla (Dynatrace LLC)** 04:19 domain. No, it… yeah, it redirects, which is not a problem. The problem is that the Zoom Outlook integration doesn't detect it as a Zoom meeting.
**Armin (Dynatrace)** 04:33 then you're talking about the link that I posted in the chat, right?
**Daniel Dyla (Dynatrace LLC)** 04:37 Yes. Is that… because that's a pro… like, a normal, standard Zoom link. Does anybody know if that link is stable?
**Trask Stalnaker** 04:53 I'll share my screenshot of what I see, if that helps.
It seems to recognize it, at least it's showing up in the location.
Spot for me.
**Daniel Dyla (Dynatrace LLC)** 05:06 Right, but if you go to your Zoom… I don't know if you use the same… now we're getting into company-specific things.
**Trask Stalnaker** 05:12 Competence.
**Daniel Dyla (Dynatrace LLC)** 05:13 Zoom Workplace, I have a list of today's meetings that I.
**Trask Stalnaker** 05:16 Obviously, I'm at Microsoft. Obviously, we don't use Zoom workplace, sorry, can't help.
**Daniel Dyla (Dynatrace LLC)** 05:23 Yeah.
So I have, like, a list of my Zoom meetings for the day.
And I just click on one and it joins.
And this one is not in that list.
**Armin (Dynatrace)** 05:34 So that's why the two of us are always ending up in the wrong meeting for the first minute until… Some smart person like Igor points it out to us.
**Daniel Dyla (Dynatrace LLC)** 05:47 It looks like the LFX link.
has this… the meeting ID in it?
So I'm gonna go ahead and make an assumption.
That this is a stable link.
And add it to my calendar.
And I will let you all know if it stops working.
**Tigran Najaryan (Splunk Inc.)** 06:13 Hey everyone, am I sharing the right browser window now with the agenda?
**Daniel Dyla (Dynatrace LLC)** 06:19 Yes, I see the agenda.
**Tigran Najaryan (Splunk Inc.)** 06:21 Until… yeah, okay, cool.
All right, if you guys ever… anybody has any topics they would like to talk about today, please add it to the agenda.
And your name?
To a list of attendees.
I think we can go ahead… is Robert here?
**Jack Berg (Raintank, Inc. – Grafana Labs)** 06:41 Robert is not here.
**Tigran Najaryan (Splunk Inc.)** 06:44 Okay, let's, let's see.
I think he… what he wants, is, There's a number of approvals, Jack, you blocked it.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 06:54 Yeah, I blocked it two weeks ago at the spec meeting, and the reason was, that it jumps right to stable for this, because this is being classified as a bug fix. And I was… I was saying, look, this is… even though we might characterize this as a bug fix, it's still pretty consequential, and so we should give it some extra scrutiny. And so it was a block on, like, giving it some extra time and scrutiny, rather than on the content itself.
And since then, I've reviewed it. I've actually built a prototype of this in Java as well, so I went pretty deep into trying to understand this, and it was almost all good. There's just, there's one question that I have here, which I think Robert is the only person that can answer this, but it's about the defaults.
And so, you know, or they… it's a combination of the defaults and the interpretation of, like, a zero or negative value. So, like, you know, what Robert has said here is, like, if you set the depth to be zero, that means unlimited.
So it's like, sort of like, if you set the size of a… the message size of an HTTP client to be negative 1 or something, then the message size is unlimited. It's like that type of function. And so, like, I… my comment is that I think we should avoid doing that.
But I want to hear what Robert has to say about this.
**Tigran Najaryan (Splunk Inc.)** 08:21 Okay, since he's not here, you want to take that offline?
**Jack Berg (Raintank, Inc. – Grafana Labs)** 08:24 Yes.
I think he's got some PTO coming up, and so it might take a bit of time before he gets back to this, but, you know, I'm in the loop now, I prototyped this, and I'll get this resolved as soon as he's available to respond.
**Tigran Najaryan (Splunk Inc.)** 08:41 Okay, sounds good.
**Carlos Alberto Cortez** 08:43 By the way, sorry, just to clarify, Jack, your only concern, if I understood correctly, is the defaults.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 08:51 It's like the default slash the semantics of setting zero.
Yeah, my comments are, you know, state my position, so…
**Carlos Alberto Cortez** 09:02 Okay, yeah, that understood. I think it's, yeah, let's do that, let's wait for him. In the meantime, I think we can, this call's not in the call, like, offline, the rest with the Maintainers.
In case there's anything else while we wait for Robert.
So please, Maintainers, take a look in that regard.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 09:22 Yeah, right, let's not, you know, use Robert's absence as a reason to stop the discussion overall. You know, like, let's get this in a place where once Robert gets back.
you know, we're in a state to move forward, so get all of your thoughts out on this PR, please.
**Tigran Najaryan (Splunk Inc.)** 09:39 The other thing you mentioned, that this is… this goes straight to stable, Is there any… Alternate to doing that.
Because I'm not sure that… I'm not sure I agree, like.
And this is actually Abbott Fitz, right?
It changes the behavior. It's, it's just an omission in the spec, right? We simply forgot to add it.
So, I don't know, like… that I necessarily agree with the idea that this just fixes a bug.
And it's okay to make that change.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 10:15 So, Robert defended it as, like, a bug fix a couple of weeks ago. I won't be able to articulate his position there. He had reasons why he thought it was, but if you have counter reasons, I don't think that there's actually a discussion on this PR yet, saying, like, actually trying to pose that question. Is this a bug fix, or just, like, you know, a normal change that should go through the development to stable?
maturity model. So, please make that comment, and.
**Tigran Najaryan (Splunk Inc.)** 10:42 Yeah, yeah, I'll do that. Yeah, let me do that as a comment, and he can reply.
Okay, let's move to the next one.
It's yours as well, Jack. No, it's, Josh's.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 10:57 Yeah, so… This is a PR that Josh opened back in June, and I'm promoting it on his behalf.
And the reason that I'm promoting it is that we're working on landing a prototype of entities in the Java SDK, and this language is important to us, to feel comfortable landing that prototype.
And, essentially what this does is it… is it changes the conception of a resource detector. There's… there's currently four built-in resource detectors, four named resource detectors. There could be more, but, like, the four were the ones that we could get agreement on, and they're in development. We never stabilize these.
And, you know, traditionally, resource detectors have provided bags of resource attributes.
And this change that, that Josh is proposing is saying, like, hey, resource detectors should, should… not just provide bags of, like, you know, unstructured attributes, but should provide entity-aware resources. And an entity-aware resource is just, like, a resource that has entity information attached to it, and the entity information gives you, like, you know, the structure around that previously unstructured, you know, bag of attributes. And so, yeah, resource detectors go from being like, hey, just bags of attributes to entity-aware.
And there's a new environment variable that allows you to toggle the behavior of resource detectors.
So, the, the, the, it's somewhere in here, I think it's… OTEL Experimental, yeah, this one. OTEL Experimental Entities Enabled, and this defaults to false.
So, by default, your resource detectors will keep emitting, like, you know, entity unaware resources, and if you set this to true, then the resource detectors update and, you know, the behavior of your SDK updates to suddenly become entity aware.
So, this is how we think we do this in, like, a backwards compatible way. By default, like, you know, there are no entities being emitted by your SDKs, but if you opt into this experimental environment variable, then you start getting entity-aware resources.
**Tigran Najaryan (Splunk Inc.)** 13:08 I think to add to that, the important piece is that even when you enable this flag.
The result of detection, yes, you get entities, but when those entities are merged into a resource, with the… With the current implementation, you're most likely going to end up with the exact same set of attributes as you do without the entity enablement.
Was that a fair expectation there?
**Jack Berg (Raintank, Inc. – Grafana Labs)** 13:38 That it's the same as before?
**Tigran Najaryan (Splunk Inc.)** 13:41 is the same as before, the same set of attributes on the resource, on the merge resource. The entities, when they are detected.
After the entity detection, we merge them into the resource attributes, right?
And that set of attributes is naturally going to end up with being the same as it is today, before… before this change is made. Do we want to formally make that a requirement, or we think that It's possible that we deviate from that.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 14:13 I think that, you know, the set of attributes still ends up being equal, is… it falls out of the merge semantics.
Our semantics were done in a way that attempts to be backward… is backwards compatible, and so, like, you know, that's implicit in here, is that, you know…
**Tigran Najaryan (Splunk Inc.)** 14:34 I think that that's implicit also only if you require that the entities, the individual entities, detect the same attributes As the resource detectors do today.
But if you turn… turn the resource detectors into entity detectors, you may accidentally… change the set of attributes those new detectors produce. Do we want to make it explicit that this is what we expect to happen? Don't rewrite your resource detectors to start doing something entirely different, just because it's called entity now.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 15:11 So, the current resource detectors, the descriptions are intentionally open-ended. You know, resource detectors, you know, the concept was created before we had semantic conventions, before we had conventions about things like entities and resource attributes. And so, like, you know, when I initially added this PR a long… a couple years ago now to add this set of resource detectors that are built in, container host process service, I had to keep the descriptions open-ended enough to accommodate just, like, the divergence in the community that had emerged over the course of years.
And so, like, they're nondescript. They say things like, the container resource detector populates container attributes, but it's not… it's not specific about which container attributes. The host one populates host and OS, the process one populates process, and so, like.
you know, I actually don't know the answer to your question, Tigran on whether.
**Tigran Najaryan (Splunk Inc.)** 16:09 Yeah.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 16:10 into this should, like, also constitute a change in which attributes I produce, but, like, it's a good question to ask.
**Tigran Najaryan (Splunk Inc.)** 16:17 So, I know the spec doesn't tell precisely what the detectors, what attributes should be included there. What I'm saying is, is it necessary for us to accompany this change with guidelines to language Maintainers on how exactly to enact this change? And the guidelines should say Take your resource detector logic, And reuse it exactly as is, so that you don't break… Your resource output.
when the… when the… when this flag… when the experimental entities are enabled, at least as a recommendation, because I think that's highly desirable, but it may not be entirely clear to people who are implementing this, right?
What's hold on?
Not as part of spec, as part of recommendations on how to implement the spec change.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 17:06 Yeah, yeah, and I just like… so, someday, we want to get to the state where entities are enabled by default, and the entities that are emitted match the semantic conventions.
So, you know, if… If a resource detector today, like the container resource detector, doesn't perfectly embody the semantic conventions for the container entity, then at some point, there's going to be a breaking change.
**Tigran Najaryan (Splunk Inc.)** 17:33 Yeah.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 17:34 And I think, like, I think it could be a good thing to make the breaking change occur with this OTEL experimental entities enabled environment variable. You're explicitly saying, like, I want to, like, I want to be in an entity's world.
And so you're, like, opting into that. So, if not this environment variable, then there's gonna have to be another one to opt into in the future.
**Tigran Najaryan (Splunk Inc.)** 17:55 Okay, I'm fine with what you're saying, but then, in that case, let's be explicit about that.
that this.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 18:01 Yeah.
**Tigran Najaryan (Splunk Inc.)** 18:02 allows breaking changes. Okay, I'll shut up, then you have your hand up.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 18:07 Sorry.
**Daniel Dyla (Dynatrace LLC)** 18:08 Yeah, a couple things. One, do we want one… Environment variable to enable breaking changes for all of these things, because… Like, the taking container as an example, if the attributes change, When you move to entities.
And that's a breaking change.
Will that happen before… entities is ready, and people start using it. Like, if something down the line, I don't know, some Kubernetes thing then has a breaking change, but there is… there's a reason we don't have a single environment flag for all of the instrumentation semantic conventions breaking changes. We did one for HTTP, we did one for messaging.
I think we may want to do something more similar here, where it's more granular. I want to opt into the breaking change on container, but I'm not ready for host.
The other day…
**Jack Berg (Raintank, Inc. – Grafana Labs)** 19:07 The problem is, it's not always…
**Tigran Najaryan (Splunk Inc.)** 19:08 change, though, then?
**Jack Berg (Raintank, Inc. – Grafana Labs)** 19:10 Exactly.
**Tigran Najaryan (Splunk Inc.)** 19:10 To me, it's not clear. It's like that this is a breaking change.
**Daniel Dyla (Dynatrace LLC)** 19:12 I didn't hear either of you.
**Tigran Najaryan (Splunk Inc.)** 19:14 I think I was expecting that this is not a breaking change from the perspective of the resource shape.
But maybe I'm wrong, so… I think what we need to do is to clarify what exactly happens when you enable this thing.
Does it change the resource shape or no?
**Daniel Dyla (Dynatrace LLC)** 19:30 We talked about this yesterday, and… I wish Josh Surith was here, but, we talked about it yesterday in the entities meeting, and one question that came up is that the reason for this for this flag is so that users can opt into a change that might be viewed as breaking. It had to do with the way that, schema URL is handled in the merge.
If I remember correctly.
The… the question that I brought up is, like, we… Bent way over backwards in the data model and in all of our… in everything so far to make this a backwards-compatible change, such that Both produce… producers and consumers could continue working with resources.
As they always have been.
And we did that so that we wouldn't have to have this type of braking change.
My question is, why… are we… Why… why are we… I'm trying to think of a way to phrase this that doesn't sound… Why are we bending over backwards to not make breaking changes in other places, and then saying, now we have this flag to make breaking changes here? Shouldn't entities either be a break or not?
**Jack Berg (Raintank, Inc. – Grafana Labs)** 20:55 Let me actually… so, let me back.
**Tigran Najaryan (Splunk Inc.)** 20:58 Sorry, Josh. Go ahead. Sorry, can we… since Josh is also not here, and we probably need to timebox this, is it worth maybe moving the discussion offline?
Unless you have something quick to say, because I think we have a few other items to talk about.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 21:12 I, I have something quick to say, so, there might not actually be any breaking changes, because, like, you know, think about what happens when you enable entities for a resource detector, like the container resource detector. Previously, it was reporting all the container attributes.
Now, it's producing them in an entity-aware fashion, and the semantic conventions describe for, you know, the container entity which ones are identifying, which ones are descriptive. So, like, is there any case where a container attribute is no longer produced anymore once you become entity aware?
I think no. I think, like, it's just, like, a categorization exercise, and all the attributes continue to be reported, and now they're just either identifying or descriptive.
**Daniel Dyla (Dynatrace LLC)** 22:01 So why are we stripping entity information? If it's backwards compatible all the way up to pipeline, why would we strip it by default unless you set this flag?
**Jack Berg (Raintank, Inc. – Grafana Labs)** 22:12 So, the reason is, is because it populates experimental fields in OTLP.
And so, like, you know, it's like an opt-in such that your SDK will, like, emit experimental fields in OTLP. And I… but I actually… now that I'm, like, kind of repaging this into my brain, the implementation that Josh has in Java and stuff, I, like, I don't think it's high risk if a user opts into this environment variable.
I don't think there's any risk, actually.
**Tigran Najaryan (Splunk Inc.)** 22:40 So I think we need to be clear about either it's a breaking change for the resource, or it's not, and say that explicitly one way or another. I think that's important, because…
**Daniel Dyla (Dynatrace LLC)** 22:51 I think, I think it should not be.
**Tigran Najaryan (Splunk Inc.)** 22:53 Yeah.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 22:54 And if somebody has evidence that it is a braking change, please clarify in a comment in which way it could be breaking.
**Daniel Dyla (Dynatrace LLC)** 23:00 Yeah, exactly. Because any given detector may have breaking changes to the semantics of what it's emitting, but that's immaterial to whether it's a resource or an entity.
as they stabilize.
**Liudmila Molkova** 23:15 It may be not be breaking for anything existing, but once you have it enabled, you get something that can break.
This is your consent to… Knowing that you cannot depend on the new features you are enabling.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 23:35 Yeah, the entity.
**Daniel Dyla (Dynatrace LLC)** 23:35 Inc.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 23:36 because they're not fully stable. Like, the categorization of description or identifying attributes, that is subject to change still, at least for some of the entities.
**Tigran Najaryan (Splunk Inc.)** 23:47 I don't admit.
**Daniel Dyla (Dynatrace LLC)** 23:47 My confusion just came from… the discussion was a little bit about… started to become about braking changes, and we've gone so far out of our way to make it not breaking that it would be unfortunate to introduce brakes now.
**Tigran Najaryan (Splunk Inc.)** 24:05 Okay.
So I think we need to ask for clarification here. What is the expectation, really? I think what, Ludmila, you're saying is that once the flag is enabled, the resource attributes can't change, but the entity attributes may change, right? So you're opting in.
**Daniel Dyla (Dynatrace LLC)** 24:24 Not the attributes themselves.
It's like the.
**Tigran Najaryan (Splunk Inc.)** 24:27 shape of the…
**Daniel Dyla (Dynatrace LLC)** 24:28 protocol.
**Tigran Najaryan (Splunk Inc.)** 24:29 the attributes may change as well. The entities… this… Or maybe not. Okay, yeah, maybe not.
**Daniel Dyla (Dynatrace LLC)** 24:38 If you say the container entity is stable, then those attributes are going to be the same.
**Tigran Najaryan (Splunk Inc.)** 24:44 Yeah, yes.
**Liudmila Molkova** 24:45 Right.
And…
**Daniel Dyla (Dynatrace LLC)** 24:48 This is opting into, like.
**Liudmila Molkova** 24:50 I've qualified for Upton.
**Tigran Najaryan (Splunk Inc.)** 24:52 Okay.
**Daniel Dyla (Dynatrace LLC)** 24:53 This is opting into, like, protocol level, which may, you know, maybe a field… changes, or some… I don't know. It's unlikely, I think, but… It's still experimental.
**Tigran Najaryan (Splunk Inc.)** 25:10 Okay.
Sounds good.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 25:13 Please do review this, you know, Josh is out on… for… for a week on PTO, maybe a little bit more. I think we can make progress before this. It's not actually that controversial to me, even though there might need to be at least a clarification, but…
**Daniel Dyla (Dynatrace LLC)** 25:31 I also am not entirely sure… That, because it's an entirely new field.
It's a backwards compatible change at the protocol level.
is this attribute necessary? Like, we've added other things to the protocol in the past that haven't had to have specific opt-in configurations.
It's marked as experimental, right?
**Jack Berg (Raintank, Inc. – Grafana Labs)** 25:56 Yeah, I don't know any instances where we have populated experimental attributes in OTLP by default.
**Daniel Dyla (Dynatrace LLC)** 26:05 Even if that's not the case, and we haven't.
I don't think that we necessarily need to specifically opt into it, as long as we're clear that it is experimental, because… As long as consumers understand that it's an experimental field.
I'm not sure that there's any risk to just sending it.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 26:26 Do you want to leave that comment? And also, I'll say that, like, if we start out with an environment variable that opts into it, we could later remove that environment variable and have the behavior of that be, like, the default, right? So, because that's where we want to get to eventually, is that entities are transmitted by default.
**Tigran Najaryan (Splunk Inc.)** 26:47 But again, I'm with Dan on this. What is it? What harm is there if we include this field?
It's… it's on the consumers to deal with that, and the consumers have no idea that you have an environment variable set in some SDK. Doesn't matter, really.
they have to look at the field and the presence of the field on the wire, not some SDK environment variable.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 27:13 It's just, it's just, like, sort of uncharted territory. What does it mean to have an experimental field in OTLP? I actually don't know that we have this.
Anywhere else in logs, metrics.
**Tigran Najaryan (Splunk Inc.)** 27:24 Braydon't, as far as I remember.
**Daniel Dyla (Dynatrace LLC)** 27:26 Well, yeah, because part of the problem is, are we telling consumers, you know, I don't know, I work at Dynatrace, are we telling Dynatrace to… Consume this field.
and build, you know, I don't know, experimental product features based on it to give feedback.
If the answer is no, then how can we ever validate that the entities are… you know, that the use case is valid? And if the answer is yes.
Then, do we need to say, if we make a breaking change to this, we'll change the field number?
Because there's no way to distinguish Like, there's no… there's no protocol version dis… Distinction right now.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 28:13 Yeah, we've already decided in the past that if we were to make a breaking change to the entity ref message type, it does have to go with a new field number.
Like, that's how experimental properties have to work in OTLP. It's like, you know, they're effectively permanent, and if you want to change, you create a new instance and delete the old one.
**Daniel Dyla (Dynatrace LLC)** 28:34 Yeah, so what we're saying is not that this might change, but it might go away in favor of something else in the future. And, to me.
That points towards… It's safe to emit, it's safe to consume.
I don't know why we have the environment variable opt-in in that case.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 28:55 Make the argument.
Will do. The best part is no part. Like, yeah, there's no reason to keep the environment variable, let's delete it.
**Michele Mancioppi (Dash0 Inc.)** 29:03 We have done it already in the past, right? When we started adding, Event name to log records. We just did it.
And nobody broke.
So, yeah, why not?
**Tigran Najaryan (Splunk Inc.)** 29:17 Okay, let's move on. We have a few other things to… to talk about. Please comment on the… on the PR.
offline.
Liila, you have another one which may be essentially a new experimental field in the span?
**Liudmila Molkova** 29:33 Oh, yes, absolutely.
Yeah, can they present?
**Tigran Najaryan (Splunk Inc.)** 29:38 Sure.
**Liudmila Molkova** 29:43 Yeah, so… Okay, so… Let me set the ground, There were a lot of discussions in the past about spend type, and it meant different things. I'm proposing to add it.
And it's exactly what it is in semantic conventions.
So let me show you… This is the new syntax we have, and we had something in the past which was group ID, but essentially, this is a span definition.
And it has a type.
This, is a sticky ID that you can identify the span, in a stream of spans. It's absolutely… Similar to the event name.
It's very similar to metric name, and it's very similar to entity type.
Why do we need it?
So, in the past, we used something like this attribute.
Messaging system to identify a category, like a messaging.
But it's not enough. So, in messaging, we invented another attribute that is called messaging corporation type, that within the messaging system identifies the Type of the operation, and it's effectively a spend type.
And it goes even further, and we have also a distinction between So these two guys are not unique. You need to also take the spend kind into the account.
So there are several different things to look, just in the messaging, to differentiate Quite a few attributes we have there within one convention.
And… guess what? In Gen AI, We are… going to have at least this many spans, these are just the existing ones, and we're merging some of the operations together, just because we are a little bit lazy.
But in some version of the world, each… distinct operation on your, let's say, REST API, or in your product definition, becomes its own span, if you want to precisely describe it.
So, where does it create issues? Well, first of all, it's… We cannot validate it.
So, if I show you what we do to validate spans in Gen AI conventions with Weaver LifeCheck.
This is just, some bunch of regal code that matches knowing some heuristics about GenAI spans and matches them into SPAN definitions, that are also expressed here, hard-coded, What we do for our metrics? Nothing.
Or for events, because we have it matched by Weaver, and everything is validated by Weaver out of the box.
If we were to build these heuristics, they will be… Per semantic convention, like, per domain, and within this domain, there would be multiple properties to look at, and there will be no guarantee that semantic conventions has A unique combination of these properties that match to the spent type.
Users would have the same problem if they want to query something like, give me all, I don't know, messaging receivers.
how would they do this without spend type? They would need to know All the things that identify messaging receivable, and they would need… they wouldn't have, We wouldn't be able, or it will be more… OTLP payload to establish both the vendor-specific naming for this operation, which could be, I don't know, poll, or the generic operation, like receive. So we need to maintain, kind of, both terminologies either way.
But, they are bespoke, depending on semantic conventions, and the moment you receive something that's not defined in hotel semantic conventions, you can no longer, as a consumer, even infer What the spend type would be.
So, what I'm proposing is essentially a product field, for this.
it could be an attribute, but we've just done this exercise with, event name. It used to be an attribute, and eventually we decided that because we want routing, and because we want, effective routing, because we want effective querying.
It would just make sense as the top-level property.
So, this is an addition.
And then I'm proposing to update the API spec to add the new properties and type. It's optional.
Nothing breaks if you don't provide it.
Everything still works in the same way, but instrumentations and applications that want their spans identifiable.
would populate it.
We would retire all the hacks and semantic conventions.
That, Create some spans just for the purpose of the identification.
And it would, actually… Save us some performance and a little bit of, overhead.
Sample… samplers would get this pen type as well.
They would be able to sample based on it. It's immutable, and obviously we would need to have the spend type.
Available to exporters, and… Yes, that's essentially… It… Yeah, Diego?
**Diego Hurtado** 36:02 Yeah… Don't name it span type, name it type, please, to be consistent.
**Liudmila Molkova** 36:10 Oh yes, it's true.
**Diego Hurtado** 36:11 To realize.
**Liudmila Molkova** 36:13 So the spend type, it's funny you say, because the spend type, the Python has built-in type, and it cannot be the property.
**Diego Hurtado** 36:22 No, no, we can… we can use type and underscore, that's fine. My point is that there is, Name, and not span name, right? So it should be typed and not span type, so…
**Liudmila Molkova** 36:37 Okay, yeah.
**Diego Hurtado** 36:39 Thank you.
**Liudmila Molkova** 36:41 Thanks.
Yeah, Tigran, I think you're the next one.
**Tigran Najaryan (Splunk Inc.)** 36:44 Oh, Jake, I think you were.
Before me.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 36:48 Okay, I just want to say that I support this. So I've encountered A lot of the problems that you described personally, I've had to build pipelines that try to detect which versions of semantic conventions and which specific semantic conventions span in bodies, and you have to do this sort of duck typing thing where you look for the presence of certain attributes.
And, it's not fun, and having a clear, unambiguous identifier that this is an HTTP server span would be fantastic. This is an HTTP messaging span would be fantastic.
I think that the fact that span kind is, like, isn't a new was probably a miss, and we would have been better off if we could have nailed these semantics from the beginning, like having span kind be a string, have span kind be, you know, sort of this fully qualified identifier, like, event name is. That would have been nice if we could have got it up front, and, you know, it's good that we're trying to address it now. And similarly with span name, span name has, like, frustrated me as well, because it's just, like, a concatenation of other data that's already on the span and attributes, so why does that exist? But, yeah, like, you know, I'll support you in whatever way I can. I support this concept. So, yeah, thanks for working on it.
**Liudmila Molkova** 38:08 Awesome, thank you.
So it seems Zoom has a problem with ordering now, I'm not sure, Tigran near the end.
**Tigran Najaryan (Splunk Inc.)** 38:15 I'll go next, yeah, yeah. So, I also support the idea. I had a few questions, I left some comments on the PR there.
One… one of the questions I had was the… one of the motivational examples of how the span kind of… or, sorry, spam type can be used was that We can do the response to metrics conversion easier.
I am not sure I entirely understand how would that work. When I look at, For example, the HTTP span, the HTTP client stand.
Depending on… So, actually, you can convert a single HTTP client span to multiple HTTP metrics.
And which metric you convert to.
essentially is based on which attribute of the span you're choosing as the value of that metric. So there's not a one-to-one mapping, there's one-to-many mapping.
If that's the case, I don't understand how… Exactly. The… having the spawn type helps.
For that converter to be implemented.
**Liudmila Molkova** 39:24 Yeah, so…
**Tigran Najaryan (Splunk Inc.)** 39:25 clarify.
**Liudmila Molkova** 39:26 Yeah, and I'll leave a… probably I'll add something to that. I think, yes, you already… that spends the metric conversions can be done in multiple different ways. One of the ways I am most familiar with is when you take all the spends, and you create one spend metric out of it.
A spend client and spend server, maybe producer and consumer.
And these metrics obviously suffer from spam name cardinality.
Even in a good case, it's pretty high, but usually people put some high cardinology stuff in the span name, by mistake.
So this metric suffered, and instead of using spend name, they could use span type as an attribute.
And then it becomes a low cardinality, obviously much lower resolution, but that's the point.
The other way, yes, you can convert span type to a metric, and actually, in semantic conventions, when we define a spend type, we also usually define a corresponding duration metric.
**Tigran Najaryan (Splunk Inc.)** 40:30 Yeah.
Okay.
Okay, the other question I had was about the situation that you are discussing in the OTEP, where actually the SPAN may be describing multiple operations that happen at the same time, the HTTP and the messaging, right? So, messaging over HTTP.
Have you looked at the possibility of allowing actually recording multiple types in a span, instead of a single span field, make it an array?
So that you can explicitly allow that situation to be recorded on a spam.
**Liudmila Molkova** 41:05 I think… I… I don't want this. Why? Because if you combine FAS server and HTTP server in one, you're effectively creating a new span type.
it has one name, right? We need to have a rules on how name is formed once. We need to decide what makes an error for this span type.
It may be different depending on, like, the FAS or, HTTP.
We need to, like, describe things that go into sampling relevant, like, what attributes are… need to be provided at start time.
the attributes… the set of attributes might be slightly different, that you… you might drop some of the HTTP, or… for whatever reason. In a generic case, what I'm saying, that if you really want to be a good semantic conventions author, or just make your response identifiable.
Create the new type for this, because it's in Newspan.
**Tigran Najaryan (Splunk Inc.)** 42:09 So you're saying if I have a situation where I need to record a composite operation, simply mechanically recording the superset of all the attributes from, let's say, both HTTP and messaging.
Sync is not good enough, because the semantics of what really is happening Is different enough.
from… from a simple combination of… of the two. So you would need to have… have to have a unique Syncf defined for that case anyway. That's why it's… Okay. Right. Okay, I think it would be worth, maybe.
Explaining that that alternate is not… is not really a good alternate.
**Liudmila Molkova** 42:53 I'll check if I didn't.
**Tigran Najaryan (Splunk Inc.)** 42:54 Yeah, I had a couple comments like that, but I think, anyway, I support the idea, so…
**Michele Mancioppi** 42:59 I, I actually think that what Tigran said about multiple types is correct, and I know that because, we already did something exactly like this.
And it's called span type in their zero, and for user experience, you do need to be able to annotate multiple types. GenAI and HTTP is a classic example. HTTP and database is another classic example.
GraphQL and HTTP.
another one.
So, it kind of… having multiple types helps. And in my head, the multiple types… are something that makes very much sense, because… Spend type is effectively entity, References, but for sparins.
The same way a resource can carry multiple references, the span could carry multiple types.
**Liudmila Molkova** 43:54 Well, they don't care multiple types, because between database span and HTTP span, even if they are blended, you need to decide what makes the HTTP span name… oh, sorry, the span name.
Right? So the semantics are bigger than attributes.
And, if we… if you want, to… Encode that the, like, this, let's say this identity.
Is a blend of two other identities that you expect, you're under, like, you expect some form of inheritance. We could… have it encoded in semantic conventions here, and when, once you match the span definition to… sorry, OTLP to a span definition, which is easy now, you can tell which, sub-identities it has.
So for this, we don't need to have an array of Types.
It could come through the side channel of semantic convention schema.
Would it work for you, Michele?
**Michele Mancioppi** 45:02 I mean, for me, it could work either way, as I'm just relating the experiences I have from Darcyo. I am not sure about your argument that we should have only one type, because we have only one name, and here I'm oversimplifying things massively.
I think that in terms of… so one of the strategic goals of this OTEP is to make things easy to search and query.
And, I think multiple types aligns better with that statical.
Then, either making a composite type, and then you have to go with contains, or going another way with semantic conventions. Just my two cents.
**Liudmila Molkova** 45:45 somehow we didn't do this for events or metrics, right? Metric has exactly one name, and event has exactly one name, even though you could say that It can blend multiple other things together.
**Michele Mancioppi** 45:59 Yeah, but we did… we did put the type in the all-sematic of Najan matrix.
So in all the semantic convention metrics, they have the type built in as a namespace, effectively.
For events, yes, you have a point.
They, in practice, they, however, tend to be very focused, because 90% of the events I've seen outside of Gen AI is people reporting errors.
**Liudmila Molkova** 46:33 Okay, yeah, I'll think about it. I kind of feel strongly about the parity and one event type, and you can build a… Composite identity with string concatenation as well.
Okay, done? I think you're… oh, Aaron, Aaron is…
**Daniel Dyla (Dynatrace LLC)** 46:53 I think Aaron is ahead of me.
**Liudmila Molkova** 46:55 Yeah.
**Aaron Abbott** 46:56 Yeah, I was just gonna say I also like this proposal, support it, and I think We'd be happy to prototype it in Python as well.
If that's helpful, One other thing I was gonna ask about was, I think it was in the OTEB text, but there's the telemetry… the collector schema transforms, I was wondering if there's already anything… for that in the collector's schema transforming processor. Does it handle spans already? And if so, is it the same heuristic approach this would help with?
**Tigran Najaryan (Splunk Inc.)** 47:31 The schema transform processor, it's on the end user to define how exactly they want to transform it. The processor itself has no knowledge about Synconf, as far as I know.
So the assumption is the user knows… user knows what the semconv is, and they know How to write the transformation from what to what they are mapping.
**Aaron Abbott** 47:56 So, I meant the, like, schema URL-based one, like, we have this changelog of, Differences between schema versions and the… in the semantic conventions repo.
**Tigran Najaryan (Splunk Inc.)** 48:06 the schema processor, you mean? I think that one is incomplete, I don't know if it's… working at the moment. I may be wrong.
**Liudmila Molkova** 48:17 So the… I think what, I take out of it. So, for metric, we can match a metric by the name, and we can change something on this metric specifically in the collector. For span, it's not the case, because we cannot match.
**Aaron Abbott** 48:35 Okay. Yeah, I think that's what I was getting at. Seems like this would be helpful, really helpful for that, too.
**Daniel Dyla (Dynatrace LLC)** 48:44 I wanted to, I guess… support what Michele already said, that spans can have multiple types.
The… the database and HTTP and LLM and HTTP examples, to me are… are fairly convincing examples, but there are others. I just wanted to add that this is also… kind of a problem with, instrumentation, where, we have sometimes, like, two spans, where one wraps the other, that it might be nicer to have it be collapsed down into one span. I think this is just a smaller part of a much larger problem with the way that we… Model some of the spans, in semantic conventions.
But, I guess… We… we talked yesterday in entities about adding a name to Entity… to the entity, and we decided not to.
And what we decided on is that the type and… Attributes already in code like, the name is essentially a product decision for a backend, like, what do I want to call this entity?
And I think… For span name, it's kind of the same, except that we've already provided a name. If I could, I would go back and recommend that we don't have a name, or that we call it, like, a fallback name, or something, and de-emphasize it in favor of… Names derived from the attributes and the type.
But then there are…
**Liudmila Molkova** 50:25 This would work with multiple types, then.
diff…
**Daniel Dyla (Dynatrace LLC)** 50:28 Which would? Well, yeah, so, different types… Would produce… different names. You know, you may have two different products. One is LLM-focused, that… that names it.
a, you know, a prompt, and you might have a different product that is more HTTP-focused that calls it an HTTP call, or even two different views within the same product.
I… I think having one name Has problems the same way that having one type has problems.
We have one name, and we have to live with that now, but we don't necessarily have to live with having only one type.
**Liudmila Molkova** 51:09 Before I let Michele speak, I want to reply to this. So, from semantic conventions.
It's not correct to have DB and HTTP spans merged together.
it might be fine in some cases, like PBPF, where you look at this at the same angle, but from application perspective.
Your DB span is not your HTTP span.
You have authentication and URL flow, you have retries, and HTTP spans are not representative of your DB operations. You have different context on HTTP and for databases. And from semantic conventions perspective, like, from the purity side of view, they are modeled as two different layers.
**Daniel Dyla (Dynatrace LLC)** 51:56 I wasn't, I guess, saying that they are always… that they are modeled as one layer?
I was saying that maybe they should be.
That may be the model of spans, which I'm not suggesting would change. We have to live with what we have now.
But… I don't necessarily agree, like, there are databases where you make an… like, where the transport is HTTP. We don't have a different… spam…
**Liudmila Molkova** 52:26 Even though the Trask.
**Daniel Dyla (Dynatrace LLC)** 52:27 desperate.
**Liudmila Molkova** 52:27 with HTTP, you could have redirects, retries, and authentication inside your flow, so it could.
**Daniel Dyla (Dynatrace LLC)** 52:33 That's true of, like, any, you know, when I connect to MySQL.
Not over HTTP. That's true of that, too.
**Liudmila Molkova** 52:42 Absolutely.
**Daniel Dyla (Dynatrace LLC)** 52:43 as a…
**Liudmila Molkova** 52:44 So, we modeled a logical layer, and somebody can model the transport layer underneath in addition to. They probably don't want to, but they could.
**Tigran Najaryan (Splunk Inc.)** 52:54 Yeah, I think Ludmila is making a good point here. You may be using an authentication token for the transplant layer, and an authentication token Or the database itself.
Those can be two different values, even though the attribute name may be the same. So, how are you then supposed to record those two values as an attribute of a span? You can't anymore.
It's even worse.
**Liudmila Molkova** 53:21 Span definition, yeah, is the… it's the scope, like, what you instrument. It's tied to the spend definition. It's the errors you can catch. If you say sometimes it's something long that includes all the retries and authentication.
And sometimes something short that's on the transport. If you're saying they are the same span, then you're not defining the span well enough, and maybe you don't need span type.
Or maybe you need your own spend type that means either or.
**Daniel Dyla (Dynatrace LLC)** 53:52 Would you say the same is true in the LLM case?
**Liudmila Molkova** 53:55 Absolutely, yeah.
**Daniel Dyla (Dynatrace LLC)** 53:56 Should I… should I modif… should I model a separate prompt span that is a child of my HTTP span that's generated every single time, that has the same duration and timing.
**Liudmila Molkova** 54:08 No, no, no, the HTTP span is a child of your LLM span, and sometimes it includes time to authenticate you because you, have ORs and not API key or something, and sometimes it includes time to retry, and most of the time when you're streaming, the LLM span covers the whole stream, while HTTP covers time to response headers.
**Tigran Najaryan (Splunk Inc.)** 54:35 Okay, shall we move the discussion offline? Because we have a couple others on the agenda.
**Michele Mancioppi** 54:41 I have, one last point to make.
About what, Daniel said about, span names, I agree, they were a mistake, to the extent that in there, we override span names with, an attribute called There's little spam name in our ingestion pipeline, and exactly one customer in several years has asked.
to, to allow them to see the default spend names. So, on average, like, for the overwhelming majority of cases, the experience of building with rules, names based on attributes, works orders a magnitude better than what the instrumentations do out of the box, especially for HTTP and database plans.
**Tigran Najaryan (Splunk Inc.)** 55:33 Thank you all. Please take a look at the PR.
Let's move on, if you don't mind.
Diego, you have the next one.
**Diego Hurtado** 55:45 Right, can you open that,
**Tigran Najaryan (Splunk Inc.)** 55:49 Ludmila, can you please stop sharing, or maybe share the… the other PR, or I can do it up to you.
Oh, God.
**Diego Hurtado** 56:03 Alright, thank you. Great, so… just, an update on this thing. There was a PR… from Ludmila.
that was merged recently about, that PR… That's a GitHub workflow that will close stale issues.
After giving a 14-day warning, Today or sale.
The documentation for that process is being added here in this PR, along with the rest of the… Documentation regarding issues that were closed.
Now, this PR used to be named Ada Friendly when an issue is closed, blah blah. I renamed it at Ada Neutral, because the language has significantly changed now. It is, It's very neutral, equally harmless, and Yeah, I think the controversial part, regarding the… the chosen language have been addressed already, so just, take a look. Thank you, everyone, for the reviews. I guess, Addressing all your comments.
So, yeah.
Thank you If you can take a look at the tools.
**Tigran Najaryan (Splunk Inc.)** 57:34 Thank you, Diego. Any questions, anyone?
Alright.
Next one.
Rob or Braydon, are you in the call?
**Braydon Kains (Google LLC)** 57:51 I am here. I think Rob had to drop, but this should be relatively quick. I think this project proposal has most of the approvals that it needs. The GC Liaison and TC Liaison have both approved, and I believe everyone noted as a project lead has approved, so I don't know if we, leave it open for a few more days for… For comment, or if it's ready to merge, just wanted to… Check in on the status, in case there was anything missing before we merged.
**Trask Stalnaker** 58:23 Does it have… it probably just needs 5… the majority GC approvals to merge.
**Braydon Kains (Google LLC)** 58:31 Okay.
**Trask Stalnaker** 58:32 what do we have here? We've got 1, 2, 3… for… Yeah, just ask, Ted is your liaison?
**Braydon Kains (Google LLC)** 58:43 Yes.
**Trask Stalnaker** 58:44 Just ask him to raise it in the GC meeting tomorrow.
And we'll get… Should be just a formality.
**Braydon Kains (Google LLC)** 58:54 Okay, sounds good. Thank you.
**Trask Stalnaker** 58:57 Yeah.
**Tigran Najaryan (Splunk Inc.)** 59:04 Alright.
We're almost at time.
Thank you, everyone.
**Trask Stalnaker** 59:15 Thanks. Thanks a lot.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 59:16 See you next week.
**Liudmila Molkova** 59:17 Thank you.
**Tigran Najaryan (Splunk Inc.)** 59:18 Bye.
