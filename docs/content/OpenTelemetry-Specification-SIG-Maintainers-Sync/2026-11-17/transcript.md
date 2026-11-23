SIG: OpenTelemetry Specification SIG + Maintainers Sync
Date: 2026-11-17
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Carlos Alberto Cortez (Dash0)** 02:57 Hey, hey, let's wait 1 minute, maybe two. We have, 10 people now, Yeah, let's hope more people join. We have a few items in the agenda ready. Don't forget to put some perspective Or, yeah, the expected time that you think that your topic will be taken.
Otherwise, just add your names, please.
Okay, let's study one minute.
Okay, I guess we can start, Okay, let's go over the items.
Thank you for joining. Recurring topic, stable by default.
Do we have some new progress on that front? I know that KubeCon Happened last week.
So I'm not sure that there was progress on this one.
**Michele Mancioppi (Dash0 Inc.)** 05:14 It was discussed in the panel.
And, Austin and Ted let me know that it's no longer called Stable by default, but it is a post-graduation roadmap.
**Carlos Alberto Cortez (Dash0)** 05:28 Right.
Do we have Ted here, maybe?
No.
Okay, nevermind.
**David Ashpole (Google LLC)** 05:37 I'll take a second to plug my OTEP that I, raised, I guess, 2 weeks ago now.
But I have an OTEP out for adding stability to the instrumentation APIs, and I think that that will be a concrete way for us to make progress towards having SDKs emit stable telemetry by default.
**Carlos Alberto Cortez (Dash0)** 05:58 Yeah, I agree.
**David Ashpole (Google LLC)** 05:59 Link it if that's helpful.
**Carlos Alberto Cortez (Dash0)** 06:01 Yeah, I remember seeing that, but not sure where it is. I thought it could be here.
He said, oh, that's the one, right?
**David Ashpole (Google LLC)** 06:12 Yep, that's it.
**Carlos Alberto Cortez (Dash0)** 06:23 Yeah, okay, I see some reviews, probably, yeah, because of KubeCon, yeah, we need extra reviews, it would be nice to get people's eyes on this one.
**David Ashpole (Google LLC)** 06:32 It's…
**Carlos Alberto Cortez (Dash0)** 06:37 Okay, I guess we can move on, because, you know, yeah, let's sync on that one, next week.
Trask, do you want to share? I can share for you otherwise.
**Trask Stalnaker (Microsoft Corporation)** 06:49 No, this is just a quick follow-up to a discussion we had, the week before KubeCon.
That there was, a question, or I think someone thought maybe we had language that allowed SDKs to… Change to exponential histograms by default.
in, like, either a major or minor version bump, I don't know, but I didn't find anything. I did go looking in the spec, and I didn't find anything that, allowed this.
So, just wanted to… follow-up there. Not sure if, anybody has any more… Info about that, or if that's something we even want to pursue.
**Josh Suereth (Google LLC)** 07:52 I can jump in, because I think I'm the one who said we could do it. We don't restrict, the bucket boundaries.
So, yeah.
I don't know if the specific… like, the specification disallows things for compatibility, but it doesn't… I don't know if it explicitly allows it.
So, I guess the question would be, how do we… how do we feel about this overall? Like, do we… Is it a breaking change in practice? And it probably is. I think the way downstream systems are implemented is it turned out to be breaking. Is that right?
**Trask Stalnaker (Microsoft Corporation)** 08:29 Let me see, sorry, I'm not remembering, bucket…
**Josh Suereth (Google LLC)** 08:40 It's in the semantic.
**Trask Stalnaker (Microsoft Corporation)** 08:41 with food.
**Josh Suereth (Google LLC)** 08:41 stability, definitions about what you're allowed to change in semantic conventions.
**Trask Stalnaker (Microsoft Corporation)** 08:46 Yeah, so…
**Josh Suereth (Google LLC)** 08:47 That's the last weekend.
**Trask Stalnaker (Microsoft Corporation)** 08:48 Yeah, so this is slightly different. This is… this, so, semantic conventions… Right, we can change the, the explicit bucket boundaries.
We agreed that that's allowed. This is more about the entire, the overall, the SDK itself.
Can we, change? Because that's not a… per… Anything change? That's like a global change to switch everything over to exponential.
So I was looking at the SDK more… the SDK spec.
To see what it said about the… The default But it's not really terribly, I… I don't actually… Want to push this forward for the… Java Agent 3.0, release, Edmor just wanted to kind of… Bring this back, and if anybody else was interested in Pushing that forward.
**Reiley Yang (Microsoft Corporation)** 10:15 Trask, will that work for you if the spec says, like.
Any implementation should use exponential bucket histogram by default.
Unless user explicitly specifies something else.
building should, then we don't have to force the existing SDKs to change the behavior, and the maintainers of the existing SDKs, they can decide what to do.
**Trask Stalnaker (Microsoft Corporation)** 10:43 Yeah, I guess I'm, I'm worried about being the first person to ship something that switches everybody to exponential histograms, since that's a… In practice, going to change some things. Now, what exactly, like, yes, it makes maybe some things better, maybe it will use more space, I don't know,
**Reiley Yang (Microsoft Corporation)** 11:10 someone has to make the first change, right? So, I think for ICKs, if we force an existing ICK to make the change.
I… I guess many users will consider that as a breaking change. Like, imagine if you have a backend system where you use OpenTelemetry, and you… you have been using this explicit bucket histogram, and you know your backend has no idea about exponential.
So everything is working fine. Then someone changes the SDK behavior without bumping the major version. Now, your exporter, like, your company's specific exporter, received exponential bucket of Scrum. You're saying, Jesus Christ, I don't even know how to handle floating points.
So I can imagine many of the scenarios, so… If we want to make the change, we should be prepared that all the AI SDKs will have a major version bump, and I guess many Maintainers would have a lot of things to say about it.
**Carlos Alberto Cortez (Dash0)** 12:02 Yeah, that's a valid point.
Trask do you have something to say, or we just go for.
**Trask Stalnaker (Microsoft Corporation)** 12:09 No, let's go to hands, yeah.
**Carlos Alberto Cortez (Dash0)** 12:11 Yo, Josh.
**Trask Stalnaker (Microsoft Corporation)** 12:13 That's true.
**Joshua MacDonald (Microsoft)** 12:13 I discussed this at KubeCon with some people, because I felt like this conversation was still fresh, and it concerned me, because a lot of vendors do, I think, like the exponential histogram structure, but when asked about it, David reminded me that the Cost of the exponential histogram comes from exemplars, or having many, many exemplars, and so not only are you getting a larger structure, you're getting, like, a ton of exemplars with every exponential histogram. It occurred to me to bring back a conversation about, well.
maybe we… the exponential histogram is too expensive, and maybe we should do something about that. Maybe we're just not done with the exponential histogram if nobody wants to turn it on by default. That's the question I have.
And it causes me to think about whether we should turn down exemplars, and whether we should think about a better encoding for sparse buckets or something closer to Prometheus, or some sort of extension there. And I'll take that offline. Thank you. Josh.
**Josh Suereth (Google LLC)** 13:16 I was gonna say the same thing, but targeting something different. I think the, like, the sizes of the number of buckets by default is a little too much.
I think we can take a little bit of a, A little bit of a hit to the precision… Because we don't need, like, 98 precision. Existing histograms don't have it. The fact that it form-fits to the actual distribution you see in practice is the important part. So I think if we tune down the number of exemplars and tune down the number of buckets, we could turn it on by default.
But I think that's the big thing right now, is the defaults that we have for exponential histograms are great if you really want high precision, but really bad if you had existing Buckets. You end up with, like, hundreds more.
So, I think when you look at exponential, and if it was, like, bucket for bucket, the same number of buckets, we… might be okay. So I'd like to explore changing those defaults before we turn it on by default.
And I will say, the second point I have, I was looking through the spec quick, Trask, Exponential histograms are only a should, not a must. So having them on by default can only be a should.
And, I think… I think we probably need to go through a major version bump of SDKs to… to do that, like, to everyone's point. I think that has to be considered a breaking change. So the two things I would say is, one, I'm with you, Josh, let's look at the performance of these things and figure out how to make them not be so costly. And then second.
we… we have to do a version bump. But I… I'd be… I think this is something we should make sure happens.
**Trask Stalnaker (Microsoft Corporation)** 14:52 And one qualification to that, major version bump to the SDK is that, Potentially, like, there's also distributions.
like the Java agent, that could… that our major version bumped independently, so it can take breaking changes, separate from the SDK.
But yeah, I don't want to be the only one hanging out in that land, and getting all those user complaints if we don't, do it well. Thank you, that helps. I had forgotten the precision argument that we do use all of those buckets in order to force better precision.
**Carlos Alberto Cortez (Dash0)** 15:46 Out of curiosity, Jamek, did you mention that we will take this… well, you will take that as a private conversation. Do we have an issue for this? If not, probably there's value in creating that one.
**Joshua MacDonald (Microsoft)** 15:57 I… Don't know if we do, but I'd be glad to help.
**Trask Stalnaker (Microsoft Corporation)** 16:05 Thank you all.
**Carlos Alberto Cortez (Dash0)** 16:08 Okay, thank you so much for that, Trask. Okay, let's go over, the other items. Robert is not here, I think.
**Reiley Yang (Microsoft Corporation)** 16:15 I'll cover this one, so… this is more for, for us to align what's the right bar. So the… the situation is, you can either treat, like, all the potential like, DDoS attack, all the things, as a security vulnerability. Or you can say, like, if the user is authenticated, there's a DDoS attack, I don't care at all. Or you can find some… something even in the middle, like, try to… try to say, hey, like, if you have multiple users who can authenticate and send data.
But one user might go malicious, and they can just leverage some, like, defect.
to take over all the resources, so other users won't be able to use the service properly. And based on what we were seeing, we don't think this community has enough capacity to treat everything as security issue. But yet, we're saying if authentic user can just take the entire thing down for a multi-tenancy scenario. That… that also seems to be bad. So, we're trying to explore, like, what's a reasonable balance to at least have the Maintainers know that different levels of security vulnerability have different priority, then they can focus on the most important things. I think the gist here is If you have the scenario where you can have DDoS attacked, but this is not due to some code defect or something, it's just, like, lighting of the resource or something, then that's considered okay for the community.
So, you can find all the details. I think each open source product might have a different position here. What we're trying to do is we try to Try to define the rule so in the end, we'll have a reasonable number of security vulnerabilities that the community can really handle, instead of we define a high bar, then we end up with, like, too many things, and then everything is just, like.
like, too noisy. Nobody will handle that. So, I like the direction here, but I want to be careful. This is why we need more feedback.
**Carlos Alberto Cortez (Dash0)** 18:23 Braydon.
**Braydon Kains (Google LLC)** 18:26 I feel like we should… Claire, so the collector, SIG is the main folks, not main folks affected by this, but maybe the main folks speaking up because of the… just the volume of reports that we get on Contrib that fall under this category.
We should clarify that When we say, we do or don't care about this.
We would always prioritize something this urgent if it was reported to us, whether it's reported to us privately, through disclosure, or through a GitHub issue. This is still critical, and we want to fix this. So… From my perspective, the… the… ceremony of private disclosure, private fork, full CVE fix, feels more like We're doing this because… People should be scared about this, and we should… report it properly and make sure it goes through those channels, and I feel like an authenticated DDoS attack doesn't qualify for that. Not that it doesn't qualify for urgency of fix, but that it doesn't qualify for the full, like.
People should be… like, scared of this. Their scanners should pick it up and… and… make people upset.
It's… it's more like… because that's a lot of extra work. That is a… it's, like, a huge amount of extra work, and we want to feel like that work is worth it. And reporting a CVE for every, like, authenticated possible DDoS attack.
doesn't feel worth it in comparison to saving the CVE flow for things that users should be more afraid of, I guess.
**Reiley Yang (Microsoft Corporation)** 20:10 Yeah, I understand what they were saying.
**Carlos Alberto Cortez (Dash0)** 20:15 Josh?
**Josh Suereth (Google LLC)** 20:19 I do want to… I know this meeting's recorded, so I can only say so much, but I will say that we should make sure we have good tenancy isolation, and that I'm… I'm very supportive of us considering authenticated traffic as a possible source of attack. That is all I will say.
But I think we need to take this seriously, and we need to work on this in some fashion. And so if our threat model doesn't cover, authenticated things right now, I think that does need to get updated. And I hear what you're saying, Braydon, but, Yeah, I… I think this is important, I can confirm it's important, and I can't…
**Reiley Yang (Microsoft Corporation)** 21:02 Kashi Armor here?
gosh, you didn't finish your sentence before you went muted.
**Josh Suereth (Google LLC)** 21:11 Oh, I said… my last sentence was, I can't say more.
**Reiley Yang (Microsoft Corporation)** 21:14 Oh, okay.
So, yeah, I agree with Josh, and this is why I'm saying I want to be more careful. You can imagine if people have, something like YouTube, they can authenticate and upload videos, and if one user finds a backdoor, they can just take YouTube down, nobody else have access. That's horrible.
Right? So when you look at the PR from Robert, I think he's… he's trying to cover out a path, saying if… the user can take the service down simply because you don't have the luxury to have enough resource, then that's okay. But if it's due to a defect, like, you… you have some horrible, like, hash algorithm, like, if authentic the user finds a backdoor, they can just cause everything to be, like.
ON or, like, even, like, N square or something, then it's your bug, you should… you should consider a serious fix. And all of these are considered as CVEs.
I guess we probably can move on, so this is more like we need more review and guide perspectives.
And if you ask me, my perspective is I want to define a high bar, but I understand the high bar for openTelemetry probably means the bar is too high, nobody even think about it, they're going to do nothing about it. So, I want to understand that and take feedback, see what's the right balance.
**David Ashpole (Google LLC)** 22:41 I'll just restate what I've… what I think I've posted on this as well, which is, I'm supportive of this as a general bar, but it seems like all the SIGs that are going to be impacted by it are interested in opting out, so, I don't know if that actually helps us very much, if the individual SIGs aren't on board, that this is going to impact.
**Reiley Yang (Microsoft Corporation)** 23:10 Okay, I… I think we come over while. Thank you.
**Carlos Alberto Cortez (Dash0)** 23:17 Okay, in that case, let's move on to the next item.
Wait, what's happening? Give me a second.
There we are.
Okay, thank you so much. Next one, Christophe.
**Christophe Kamphaus** 23:32 Hello.
Yeah, it's about spend lifecycle events. We had some discussion, and I know there was previous work done on it.
To define such events, the feedback we got was, let's… Define CC funds in someconf.
Because back was a bit stalling on it.
I went to SamConf, and there I got the message. If it's in hotel namespace, it's official, and it needs It needs to be in the spec, yes.
So I came back here also with a proposal, so it can be illustrated.
I had AI write up a draft for an OTEP, It's linked at the top, as well as… I implemented, knowing the last comment.
as well as, implement these events in SamConf, so we… Could see how it looks like.
We can still discuss event names, attributes, and so on.
Now, my question to you is, how would you like to proceed? I can open… This as a real OTAP.
I can just, implemented in Samfkunf as a specific event.
for example, CICD, Pipeline events.
So we can try it out.
Yes, Trason?
**Jason Plumb (Splunk Inc.)** 25:13 Sorry, this is the first time I'm seeing this. Is this, is CICD the main use case for this, or are there… is there a place that describes what the use case for these events is? Or are?
**Christophe Kamphaus** 25:22 it's not just CICD, it's an issue in any long-running span.
For pipeline runs, of course, it's a case, but it's also for agent workflows, where it can… Agents can take a long time, so there… it would also… be useful.
**Jason Plumb (Splunk Inc.)** 25:45 Got it, so it's for long-running spans.
**Christophe Kamphaus** 25:47 Yes.
**Jason Plumb (Splunk Inc.)** 25:48 Okay, thank you.
**Carlos Alberto Cortez (Dash0)** 25:53 Josh.
**Josh Suereth (Google LLC)** 25:55 I just want to add some context. The way to think about this is, we have an underlying span event model that is effectively used by the SDK for how you actually, like, update spans and make calls to a span locally.
This is exposing that as kind of an API that people can interact with on the, you know, decomposition stream of deltas about spans.
For long-running operations, so we don't lose things, but also, like, now we have this complication of we'll have two span models, right? We'll have this span event model, and then we'll have the upper-level span model.
So, the feedback in SEMCOMF that Christophe mentioned was that if this becomes official, we think people are going to build an ecosystem around it.
And this will be seen as the default way to do it. So even if we… if this group says we don't think it belongs in an OTEP, if Christophe goes and builds this in Synconf, we've effectively created the default, like, way of interacting with that. So the thing… the thing I really wanted to make sure that we talked about here was whether we're comfortable Having, like, two levels of a span model.
Right? Where there's the raw event, like, delta-based spans, and then there's the full spans that is the current OTLP signal.
And making sure that we resolve all of the pain that might get caused by having both of these for the ecosystem, right? So, Christophe has plans for CICD, for how to address it.
I think the data model itself is completely reasonable. Like, we've prototyped this in various ways. It's more, are we on this journey together, I think is the big question. Because whether or not it's an OTEP, it's something that will cause a lot of… new work in the ecosystem, so… Anyway, let's just to add context, hopefully that helps, Christophe.
**Liudmila Molkova** 27:51 Hey, sorry, I'm curious, do we expect to send this event along with SPENS?
Or it's the alternative channel.
**Christophe Kamphaus** 28:03 I expect that you would make it configurable, so you could configure it in your SDK, Whether to send Events for any long running spans, or both.
And… You could then have either in your backend some processing to show In progress months, or have… A collector, connector.
That would take events and send spans out of it.
**Liudmila Molkova** 28:38 I would… we cannot not sense parents, because events, even though they have context, they don't have parenting… they don't have their own context.
**Christophe Kamphaus** 28:49 You could take the span ID trace ID, But you would be missing some fields, like the parent ID, so that would need to become an attribute on the log record.
**Liudmila Molkova** 29:05 There is no unique… spend it, you would need to fake it. It would be a wrong data model if we send this event without spends, and they are called Pen.
Like, related to spend life cycle.
**Christophe Kamphaus** 29:22 I mean, you could send the log records out without sending spans out.
Even if you just, set the span ID, trace ID, In Zlog context.
**Liudmila Molkova** 29:35 Yeah, and I mean, you would need to create a span.
Anyway.
**Christophe Kamphaus** 29:39 At some point, yes.
**Liudmila Molkova** 29:40 not send it. Okay, sorry, Trask Reiley one more question. Do we want SDKs to send it, or instrumentations?
**Carlos Alberto Cortez (Dash0)** 30:02 I am not Christoph, but, you may remember I had a prototype which I didn't finish, which would be a… it was trying to add this using a… optional spam processor, so that would mean the SDK.
**Liudmila Molkova** 30:17 Yeah, so then we need to introduce the… Dependency between the tracing and logging, which is not… Terrible. It's just something.
That needs maybe a language-specific approach.
**Christophe Kamphaus** 30:31 Early approach that you could use is to emit these manually.
So if you know in your applications that you have a span that might be long-running.
So that you would use these events.
myself as well, or… Instead… But that it would be instrumented manually to start with.
**Liudmila Molkova** 30:55 Yeah, for this, I kind of think that if it's manual, if it's the instrumentation which does it.
It kinda makes sense to send specialized events.
Like, CAICD pipeline start event.
**Christophe Kamphaus** 31:11 Yeah, that was also our thought in CICD6.
That if we emit these events manually anyway, we could define a specialized event for it.
But I just wanted to have this discussion here.
Because if we start having a CICD event.
Later, we have a GenAI event that does the same thing, which is… then we want to have the same structure, ideally.
Then it's just a short hop to have a generic event for it.
**Liudmila Molkova** 31:43 Yeah, probably my stance is that if it's the generic event, it should be emitted by the SDK.
And if it's the instrumented by instrumentation, it's probably… should be specialized, otherwise you emit it manually, then they emit it by the SDK and so on. Anyway, I… I'm… I'm excited about this. I think we need to find a way to make it work. I'm just, poking, in the… open questions. Go ahead, I think Trask was next.
**Trask Stalnaker (Microsoft Corporation)** 32:13 Yeah, one of our questions is similar, About whether it would be for all spans, or specific spans that, like, you know have some… a propensity for running for a long time.
I kind of like the idea of only doing it for those spans, like CICD spans, maybe GenAI spans, where agent spans where you are concerned about them running for a long time.
I also like the… I do actually like the idea of it being a generic event… From the perspective of backends that want to support Inlining these… rendering these events into the trace tree? Because that's… I think one of the reasons why… main reasons why we want to emit these start events is to be able to Show traces early, and also show traces where the the span never ended for some reason.
And the last thought here was, span ended. I'm wondering if this, if this is important, an important event, because again, back to the use case, at least the use case I've heard of, for rendering these trace trees, before they've completed, or if they don't ever complete.
The ended event.
Isn't so much needed, because you have this ban at that point anyways.
And I do think Ludmila… I hadn't thought about that point. Ludmila brought about the, events don't have, events can't have children.
And so we can't really model the whole thing as just events without… I mean, we could introduce a custom attribute called, parent.
event ID, or, you know, we could muck up some stuff, but in general, our model is that events don't have children, and so… I'm not sure about modeling the whole thing as events. Anyway, that's… I think, again, like, as Ludmila said, just, I… I've heard that this has come up a lot of times. Thank you for tackling this, just kind of throwing out a bunch of things to think about.
**Christophe Kamphaus** 35:00 You're welcome. To respond to this, in the render docs page, I did include a parent ID, In the events, so we could have this pan-chart relationship.
And to the other one, why would we have an ended event?
I thought it was important because you could lose any number of events, either at the start or at the end.
And if you include all attributes you know about.
That's the start, and that's the end, at least.
You could have a good chance to have the complete span.
And in the middle, you could trust centiffs.
To keep it, small.
**Trask Stalnaker (Microsoft Corporation)** 35:48 Yeah, so if you were doing diffs on those, like, kind of streaming case is interesting.
I noticed in the model you said that hotel span ended was the complete span.
**Christophe Kamphaus** 36:03 You would still merge it with the all previous attributes. That was my thought.
So, if your controller restarted, and you are resuming a span that started before, You might lose some attributes.
But if you then still merge some in the backend.
You would have a good chance to have a complete span out of it.
**Trask Stalnaker (Microsoft Corporation)** 36:31 Thanks.
**Carlos Alberto Cortez (Dash0)** 36:32 By the way, we have 5 minutes more for this topic, because we have a pair of more items, and I would like to reserve some time, if that's okay.
**Michele Mancioppi (Dash0 Inc.)** 36:39 There is one point about this particular SPAC, and I was the person giving the most feedback about this not having to be something in some comms yesterday. What concerns me the most, and I don't think it's an unsolvable problem, but it's something that I think we need to keep in mind, is that nobody wants to have two ways of representing spans when you're analyzing them. My expectation is that this thing will always have to be translated to actual spans on the wing.
And this, in principle, is not difficult, except that in any reasonable system.
you are not gonna process, at least a reasonable scale, you may not process the start and end events for the same span in the same instance, not unless you go and have the same Two-tiered architecture with load balancing exporter that makes life so interesting, with tail sampling, metrics aggregations, and the like.
Josh characterized it yesterday as exacerbating Some of the problems that we have in the, way that we build observatory pipelines with collectors, and that is precisely why, I think we should be very careful about this.
It's something that most users would not be able to use successfully.
**Carlos Alberto Cortez (Dash0)** 38:07 Reiley?
**Reiley Yang (Microsoft Corporation)** 38:09 Yeah, I have a question. So, it seems to me, like, very similar to the profiling events. Like, I mean, in profiling, you can… you can add events for any function invocation, like, whatever, like, detail.
Thing to do, so… Are we thinking about that? I… I saw the proposal is to add an SDK SPAM processor, and I'm… I'm… I… I'm questioning if that spam processor will introduce some, like, circular reference or something. Like, imagine if some people want to add additional costing. I want to subscribe to those events and do something, then they might trigger additional events and then run into a storm of events.
So in the exporters, we have some explicit wording about if the exporter is triggering HTTP, you have spend, what do you do? So for this one, are we thinking about that?
**Carlos Alberto Cortez (Dash0)** 39:10 Jason.
**Jason Plumb (Splunk Inc.)** 39:12 I know we're almost at time, so I'll try and keep that short. Just kind of two things pop to mind here. One being, if this is mostly targeting long-running spans, long-running operations.
and you turn this on, and the events are generated by the SDK, what do we do for operations that are just normal spans, like, not long-running operations, and does that sort of imply that we have a way to discriminate between the ones we want events for and the ones we don't, and is that not over-complicating things?
So, just food for thought. And then, second thought is that on the client side.
we kind of already have something that mirrors this. We have, session events for a long-running user. I'm using the word user sessions. We don't actually have a session spec yet, but, you know, maybe one day.
But we have these, and they're running in production. They indicate, like, when a session starts and when a session stops, and if it rolls over, we link them to the next session. This… this seems to kind of mirror that pretty closely.
I'm also… there's been… I mean, until we get sessions figured out, and actually do that work.
there's… there's differing opinions on whether or not events are the right signal for that stuff, or whether or not it should be a long-running span, and I think this… this has the opportunity to either shed some light or complicate that. Anyway.
Thanks for bringing this up.
**Christophe Kamphaus** 40:36 Yeah, thank you.
Also, I had these thoughts that in SAMConf, we could annotate some spans that might potentially be long-running.
What we do with that, I don't know yet.
Just a sort.
What about next steps on this?
**Carlos Alberto Cortez (Dash0)** 40:58 I would suggest you go and check, Christophe, what Jason mentioned regarding, the client-side stuff.
And compared that to profiling, because Reiley also mentioned that.
And then probably keep discussing offline, or, you know, discuss this next week. That would be my suggestion.
**Liudmila Molkova** 41:17 I have a tiny suggestion. It sounds like the auto-spun started as… A very non-controversial thing, and annotating some long-running spans.
And, eating this from the instrumentation side.
And what if we start and prototype it in CAICD?
And then we see if we need the rest.
**Christophe Kamphaus** 41:45 Sure, we can do that.
**Reiley Yang (Microsoft Corporation)** 41:49 I'm gonna call myself.
**Liudmila Molkova** 41:50 this…
**Reiley Yang (Microsoft Corporation)** 41:53 I put a comment in the chat. I think when OpenTelemetry started, people have been very clear about splines are not designed for long-running operations. If you have long-running things, you should omit individual events, and since that position has changed, just want to call that out.
**Liudmila Molkova** 42:10 We don't know how long they are, and it's subjective, and we need a context.
**Michele Mancioppi (Dash0 Inc.)** 42:15 And automatic instrument.
We're definitely not going to know in advance.
And users are not going to understand the difference, or be able to adopt without significant tooling. The very refined mental model you need to have to effectively reimplement X-Trace, because this is what we're talking about here.
**Liudmila Molkova** 42:36 Michele, would just the start be concerning? I think it does not introduce a new way to enhance fans. How do you feel about just the start for the backends?
**Michele Mancioppi (Dash0 Inc.)** 42:45 I feel that the users would expect this to be a new way of introducing spans, and I don't think this would translate over as something understandable.
I mean, users have… Enough challenges understanding spans as they are, now we do something that is suspiciously similar and completely different.
I do think we need to have a solution, it's a problem worth tackling. I'm just saying that we need to be careful, because To get a good solution is going to be really complicated.
**Carlos Alberto Cortez (Dash0)** 43:22 By the way, I don't want to start, like, a conversation from scratch, but at LightStep, we have these called meta spans, that basically you use The span model to represent all the response, you know?
But, so technically, you could ingest everything using spans, but of course, you have to handle those special meta spans that would represent starting, etc.
Okay, yeah. Okay, thank you so much, Christophe. Let's keep this question offline.
**Christophe Kamphaus** 43:55 Yep, thank you, everyone.
**Carlos Alberto Cortez (Dash0)** 43:58 Perfect. Okay, Tyler.
**Tyler Helmuth** 44:05 Hello.
This should be pretty quick.
I'm signed up for… the heartbeats.
And a little presentation like we had last time, so I don't know if I can share. There we go.
Okay, this is just a quick heartbeat for the OpenTelemetry home charts.
They're… small?
We don't have a lot going on in the charts compared to other SIGs, but they are pretty active.
We have 7 charts now, which is up from, like, 3 just from 2022, so people are coming and asking to want to install more and more things.
And we're able to support that. The collector chart and the operator chart, by far, are the most used charts, although, the CubeStack chart is definitely getting a lot of activity in the repo when it comes to contributions, and we're pushing that start… that chart a bit more from, like, the OpenTelemetry docs. It's in one of the blueprints, for example, so I expect that one to continue to To grow and grow.
We do have a good number of contributors showing up.
it's a lot of drive-by contributors, which isn't necessarily a bad thing for this particular repo. It's pretty easy for a user to use the chart. If they experience a gap, they show up, they make a PR, we get it merged in. And that's working out for us at the moment.
Like I mentioned, the CubeStack chart, the act… the collector and the operator are the most active. They're doing the most. We have two EVPF charts, and the eBPF instrumentation chart is the newer one. It was what installs OB, the new 1.0. We're working on getting the chart ready for 1.0 as well to pair with the app.
The other chart, I'm not really sure if anyone's using that. If anyone is involved with the other eBPF chart or the other ePPF instrumentation solutions, I would love to talk with you about those things and what this chart… what the future of this chart looks like.
Some of the things that we're doing right now that are actually helping our end users that we're driving are this component rename mapping. So right now, the collector components are renaming a lot of the components in order to be more consistent.
And that affects the way that the chart is used, if we have presets or out-of-the-box config. And so right now, one of the features that we have is to… help users by renaming if they're using the old names, so we are rewriting config at the moment. If they use the old name, we rewrite it to the new name, and everything merges nicely. It's all behind a feature gate, so if they don't want to do this, they can turn it off, but what it allows is if they use the old names.
Then it spits out the new names, and that will work with the presets, and everything merges nicely.
We have 3 Maintainers today, although Dimitri is stepping back, so it's just gonna be me and Jacob at the moment. We do have some new active community members that are coming and doing a lot for us right now, triaging and reviewing a lot of the PRs, so I'm hopeful that we'll have new approvers soon.
I don't think we're overwhelmed when it comes to Maintainers. I don't feel overwhelmed at the moment, at least, but we're always looking to continue to To level up everyone in the community.
Like I was mentioning earlier, most of the work is user-driven. We don't have any big roadmap items. Users just come, submit PRs, we get them merged in, we go forward. Right now, the big thing I do want to work on that I haven't gotten to yet is an exhaustive testing framework.
We use chart testing right now, which proves that the chart renders into a kind cluster, but it doesn't prove that the collector actually, like, is running a config that we want it to run. All that it proves is that the Helm install command worked.
So, I've got some experience now doing some more exhaustive testing on other Helm charts that I work on, and so my goal is to add a framework that actually renders config, and then asserts that the rendered config meets expectations.
So if you know anyone interested in Helm or wants to get involved in OpenTelemetry, this would be, like, a nice project to get started on.
And… that's it.
That's the Helm charts.
That's the heartbeat.
Thanks, everyone.
**Carlos Alberto Cortez (Dash0)** 48:43 Trask.
**Trask Stalnaker (Microsoft Corporation)** 48:46 Yeah, thanks. The eBPF, I'm guessing that is from, this repo, the OpenTelemetry-Network repo?
If so, that, we archived that repo recently, that SIG is not active.
Yeah.
**Tyler Helmuth** 49:07 Yay, that means I get to archive a chart and hopefully… I guess probably just delete it, because the fact that it hasn't been released in forever means that it's archived. So, yes, I will remove that code. Thank you.
**Trask Stalnaker (Microsoft Corporation)** 49:20 Yeah, and then, I had a question about, any overlap or thoughts about… with the packaging, the new packaging SIG? Sort of leveraging things sort of, like, you're doing operator and collector installation, and so there's a lot of things doing installation in the community, and so I was kind of curious what… if there's any opportunity for centralizing those things.
**Tyler Helmuth** 49:53 I haven't gotten to engage with the packaging SIG at all, but if there's overlap, I'd love to talk about it. The Helm charts right now are… like, a way for users to define Kubernetes manifest, right? But they all depend on images that are built elsewhere. We don't build anything inside the Helm chart itself. But if there are… if the packaging SIG is looking for more than, like, packaging up the binaries and stuff, and it wants to go further into, like, install and, like, that whole user experience, then the Helm chart is, like, part of that, for sure.
**Michele Mancioppi (Dash0 Inc.)** 50:27 I, don't know, I can speak for the packaging SIG.
It… we're working on, creating The container images.
I, we take part, we take the installation experience for installing OpenTelemetry and automatic injection Linux.
At the moment, we are way too understaffed to take also Helm charts and… In addition to that.
Cool.
**Trask Stalnaker (Microsoft Corporation)** 50:56 Okay, but that… you see those as sort of parallel, like, installation mechanisms?
**Michele Mancioppi (Dash0 Inc.)** 51:04 For the, for the, packages, yes. For the IPM packages, yes.
In, in Kubernetes, the, for example, the operator owns the activation And, and… The last mile of the delivery, so putting the images inside pods.
And the idea is that the images would come from the packaging stick.
So they are.
**Tyler Helmuth** 51:31 Yeah, the Helm chart could depend on those easily. Again, it's just… it's just an image that we're defining as a default. Many users overwrite the default and use their own things, so the Helm chart's less concerned about the binaries themselves, and more… it is just completely concerned about How does a user get started in Kubernetes? How do they install this particular thing in Kubernetes?
**Michele Mancioppi (Dash0 Inc.)** 51:54 Yeah, it's, I mean, come to SIG, let's have a chat about the images. At the moment, we are on a hovering pattern, because the CNCF at KubeCon has announced that they are creating a CNCF registry.
And we would like to avoid to create something on GCR or Docker Hub, and then 3 weeks later, there is the official Truly Blast, one true and only registry to use, so…
**Tyler Helmuth** 52:22 Yeah, right now, the charts just pull… from whatever authoritative SIG source the other SIGs have defined. So, like, the collector images come from collector resources, the operator, and all the other instrumentation images come from the operator, GHCR, and Bela, or Obi and Obi, and so on and so forth. So, if those authoritative places switch, then we can update the charts.
**Michele Mancioppi (Dash0 Inc.)** 52:45 Yeah, that was, that was the plan, that they would switch, and then the CNCA dropped the bomb, so we're… we're seeing where.
Switch through.
**Tyler Helmuth** 52:53 Cool.
**Carlos Alberto Cortez (Dash0)** 52:56 Okay, thank you so much for that. Okay, we have two more items in the agenda. Probably we can start with yours, Michele, because you wanted us to merge a PR. Jack mentioned that your PR will be merged tomorrow.
**Michele Mancioppi (Dash0 Inc.)** 53:09 So…
**Carlos Alberto Cortez (Dash0)** 53:10 Yeah, let's do that, yeah. In case people want to check, is this about specifying criteria for automatic injection in SDKs.
Yeah, so last-minute feedback is appreciated.
With that, we can now go to Josh, entities of the telescope.
You want to share?
**Josh Suereth (Google LLC)** 53:27 Yeah, I guess I'll… Yeah, yeah, thanks. We don't have a ton of time, and I don't want to take a ton of time, so basically there's a PR. This PR is rather important for us for entities. We think it resolves, like, one of the last things before we go to an alpha state.
This is around the issue where some of the entities that we define, we can't actually make them be, like, universally unique IDs.
So, this gives us a way where we can kind of construct a universal ID from things that don't start out universal by layering entities together. So this is the whole, like, local ID, global ID stuff that you saw in Entities ID.
It's a good proposal, it's approved by the entity SIG. There's a few really good questions on it that I think Dimitri might clean up before he… turns into a pumpkin and goes on to a new startup. But, yeah. I don't know if you're here, Dimitri, I don't think… I don't think he was.
But I did want to make sure that folks have a chance to review this and kind of, look at it, because from the entity SIG, we'd like to get this Git merged, and then start, getting the work to finish this up so we can get to an alpha state quickly.
If you have questions, please ask them on the PR. We… I guess we can… I don't know how much time I have, Carlos, but I don't want to take up too much time.
**Carlos Alberto Cortez (Dash0)** 54:43 That's the last item we have, so you have the la- the… this… the rest of the.
**Josh Suereth (Google LLC)** 54:48 Okay.
Awesome. If anyone has questions about it, I'm happy to answer them here live, but mostly I just wanted to get people to start taking a look at it, since it has SIG approval now.
Okay, I don't think we need to hold anyone if no one has anything they want to ask or has looked at it.
**Carlos Alberto Cortez (Dash0)** 55:39 I think that people need to look at it. I remember checking that, and it was, like, it's in progress at the time, and probably people need to go back and re-read it.
**Josh Suereth (Google LLC)** 55:49 Yeah.
Yeah, and I… I don't think I can do it justice. I think it's worth actually reading the PR.
**Carlos Alberto Cortez (Dash0)** 56:06 Yeah, I don't know if you are well for your consideration, but if you don't receive enough feedback by… during this week, you may consider you or Dimitri to do a presentation.
Like, we consider that for our tabs. It depends how many reviews you get.
**Josh Suereth (Google LLC)** 56:19 Yeah, if I had 10 minutes, I'd walk through all the details, I just don't think I can do it in 5.
So, next time I'll get earlier on the agenda, if, if we don't get enough reviews.
**Carlos Alberto Cortez (Dash0)** 56:29 I'll add him right now, before you forget.
**Michele Mancioppi (Dash0 Inc.)** 56:35 I mean, Christophe came in with such a banger.
Of course you went off track.
**Carlos Alberto Cortez (Dash0)** 56:44 Okay, that's all we have for now.
Yeah.
Anything else?
Like, out-of-bind information, announcements, anything?
In that case, 5 minutes back, maybe a good time to get a coffee.
Thank you so much.
**Christophe Kamphaus** 57:03 Thanks.
Thank you. Bye.
**Trask Stalnaker (Microsoft Corporation)** 57:05 by…
**Aleksandar Hadzibabic** 57:08 Thank you, guys.
