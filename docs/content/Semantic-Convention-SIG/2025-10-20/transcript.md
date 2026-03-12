SIG: Semantic Convention SIG
Date: 2025-10-20
Duration: 62 minutes
============================================================

## Zoom Recording Transcript

Liudmila Molkova 00:00:44 Hello, hi everyone.
Florian Lehner 00:00:50 Hello.
Liudmila Molkova 00:01:55 Let me fix my camera setup.
And while we're waiting, I'm going to turn the camera off for a sec. While we're waiting, feel free to add things to the agenda.
I am going to share my screen.
And… I will go and fix my camera.
Okay, it probably will take some time, I'm… go into… Go ahead without my camera on, otherwise, like, if you want to see me upside down.
If you enjoy it, they can give it on.
Okay. Fine.
So, I have just one topic, I see just one topic on the agenda for now.
And let's start with triage.
Do we also have an issue triage board for the functional?
Okay, let's see…
Josh Suereth 00:03:35 I think… I don't know if Yao's here, but I thought he got most of the.
Liudmila Molkova 00:03:38 Is it new?
Josh Suereth 00:03:39 Yeah, so, like, he's been working on this for a while.
Liudmila Molkova 00:03:42 Oh, Josh, I cannot hear you.
Josh Suereth 00:03:43 Oh, you can't hear me at all?
Armin (Dynatrace) 00:03:45 I can't hear. Oh, I can hear you fine.
Alexandra Konrad @Elastic Security 00:03:47 I… I can hear as well.
Armin (Dynatrace) 00:03:52 Look, Mia? I guess you can't hear us, right?
Daniel Dyla (Dynatrace) 00:04:07 Maybe her microphone…
Josh Suereth 00:04:09 Yeah, to make a Stranger Things reference, I think it was in the…
Liudmila Molkova 00:04:12 hear anybody.
Yeah.
Okay, let me fix my setup.
Josh Suereth 00:04:48 Oh, no one's talking, so I don't know, Lyudmila, if you'll know if it's working yet, if, none of us are talking.
So, I'll keep saying things. If anyone else wants to say things, feel free.
But, Yeah, I'll just mention this triage board. I think Yao's been working on it for a while, and it's, I believe the automation is ready enough for us to take a look at it, at least.
Armin, do you have any more… Is y'all here? No.
Armin (Dynatrace) 00:05:17 Yeah, since you've asked. So, I think he can't do Monday afternoons for a few weeks, so he has a conflict there, that's why he's not here.
But otherwise, he's… he's in and available until 1 hour ago.
Let me read the heroes now.
Liudmila Molkova 00:05:56 Yes, I can hear you! Can you hear me?
Armin (Dynatrace) 00:05:59 Yes.
Liudmila Molkova 00:06:00 Wow, I'm so sorry.
Armin (Dynatrace) 00:06:05 All good. So Josh said that the bot is fairly new, that's all part that you've missed.
Liudmila Molkova 00:06:15 Sorry, can you repeat this?
Armin (Dynatrace) 00:06:16 The board is new, Shard just created that one, and it's hooked up with the automation, but that's all, I think.
Liudmila Molkova 00:06:24 Okay, yeah, so maybe let's take a look together what we have here.
So we have some issues that are accepted, right? And based on the new triage process that are the only issues we should have PRs for.
If we don't have, if issue is not accepted, Meaning, it has this label.
We… may… and there will be an automation that effectively rejects the PRs.
I think everybody who works on the SIG Can add the label.
And… The thing we are asking is to create an issue.
Before you work on something, and then the PRs, will be accepted.
Meaning?
Subject to review.
based on this label on the issue.
there are issues that need SIG, right? So those we… Don't have expertise on, or don't have a group of people who are actively working on it.
So I think this is the… need-seq label, and it's currently up to the manual triage to set this label.
And… Some of the issues need info.
Right, probably this needs info.
I'm not sure what's the processes.
For the needs info. But essentially, I believe that if… if something stays very long in the status, it eventually should be closed.
Unless there is a community interest.
And finally, there are a bunch of issues that need triage.
So maybe, we do the best effort to triage all the issues.
But maybe we should spend some time each call, if we have it, to go through a few of them.
And triage, what do you folks think?
Okay.
So, let's just stop in… a few?
So this belongs to Gen AI.
And… Aye.
Think there should be… what should we do in this case? So this is obviously a SIG issue. We don't want to spend time here.
to triage.
Instead of specific SIG.
So, essentially, we should ask the Jenny I seek, or should we have a column here that's… redirects it to the SIG.
Is Joe here?
Josh Suereth 00:09:56 No, I think you missed that. He's… he has a conflict for, like, the next month or so, so he's… He's online right before this meeting, and then not for the meeting.
Oh, okay. So we… we can talk to him offline about that, but yeah, I think we… He had the flow and the process, and I believe that there's some thing that's supposed to kick it to the SIG at this point, for them to triage and accept or reject.
Liudmila Molkova 00:10:22 Okay.
Josh Suereth 00:10:23 Yeah.
Liudmila Molkova 00:10:24 Let's, write down the questions so I have a chance to ask.
Okay, let's take a look at a couple of other issues and, call the time on it.
Guidance for start and stop point for HTTP server spend duration metric.
Okay, this, I think it's a fair clarification we should make. I would accept this issue.
So I think that the process here is to update the label, and then it should be moved in the board.
to the… Right.
lease.
Okay, let's see if it happens, and support for AWS EKS Fargate identifying attributes.
I think this is an example where we need SIG, or need a group that knows how to work with AWS EKS Fargate.
Or… is…
Michele Mancioppi 00:12:16 I mean… Has expertise in… This makes sense.
But, the, node type… I'm not sold about it. This is not how… how it's… there is no matching in the ECS flavor of Fargate.
So we have, a bunch of ECS resource detectors that are meeting AWS ECS task launch type.
Let me look it up very quickly.
So this may require some, more thinking about it.
Liudmila Molkova 00:12:50 Yeah, and this is essentially the question of, do we have people who understand… who have enough context to judge about this issue? And it seems… We don't have a formal group of these people.
Michele Mancioppi 00:13:03 No, but it's also the kind of stuff that so far has been done for AWS, mostly by the AWS people.
And, I have not seen them very involved in specifications in a bit.
So… There should be idealistic for this.
But I don't know of anybody willing to drive that.
Also, because they will need to implement it also in their AWS history of OpenTelemetry, and it would make zero sense for us.
To upstream something different than, honestly, they would.
Josh Suereth 00:13:41 this is where we try to build maintainers and SIGs, right? So the idea behind the SIG is we get known maintainers who own that area and can drive it. So I agree with you, like, from a concern of, like, you know.
we need to include AWS in this, but to get this… to get this kind of an issue to make progress, or for us to accept it, we need a group of owners, and we need those owners to be active in the spec.
And so, we should reach out to AWS and see if they're going to be involved. If not, we'll have to find a group of people who understand AWS, who can operate it, like, at that level here for us, so that we can make these things… help these things get through.
So, example of why I think this shouldn't go through general SEMCONF approval, and why we should build a SIG, yeah.
Michele Mancioppi 00:14:28 I actually take back what I said about the launch type. This matches the same thing that does… so there's a WSECS launch type, no task is involved.
I would ping Mikher Hausenblast on this and see how he wants to play on AWS side.
Liudmila Molkova 00:14:45 Could you mention him on the issue, or pink him in some other way?
Michele Mancioppi 00:14:49 One second, yeah.
Wonderful.
Liudmila Molkova 00:14:57 So I think if I change the label, it does not update the… status, we can probably look into this, but here I'm going to… For now, I'm going to do it manually.
Another question… Okay, we've spent quite a few… quite… quite a lot of time on the issue triage, and I'm sorry, it's… New to me and everybody else.
Do we want to take a look at the… triage board, or… Our agenda is kind of low, so maybe we will go through the agenda, and then we take a look at the trash board, at the PR trash board.
Okay Don't hear no, I consider it as a yes.
Florian, do you want to talk about.
Florian Lehner 00:16:12 Yeah, hi, yeah, this is a PR that we have open for some time now.
The profiling SIC members and maintainers and approvers approved it, and we wanted to ask If this can be we.
Continued, and maybe merged at some point.
Liudmila Molkova 00:16:38 This is the PPROF compatibility, right?
Florian Lehner 00:16:41 Yep, it's for people of compatibility.
Liudmila Molkova 00:16:46 Do they actually need to mention profile?
Florian Lehner 00:16:49 It's a sub-message, like we have for the other attributes. If you look, just the line above, it's PProf mapping, and, mapping is also just a sub-message in the PProf protocol. So, using the sub-message as part of the attribute, makes it clear where it belongs to, and it just… This is a general comment to PPROF.
Liudmila Molkova 00:17:16 Yeah, makes sense. I think I raised it before, but it would be great to have a document that describes the people of Tuotel mapping overall.
It… it doesn't even have to be normative, but.
Florian Lehner 00:17:28 There is no document, and there will not be a document. We… We just updated OpenTelemetry I.O.
Side with the profiles information, and there we stated in the, compatibility with PPROF, that there's only a loose connection, so there's no one-to-one direct mapping, but more a loose connection, with the idea that you can say, hey, I'm exporting PProf to OTEL profiles, and OTEL profiles back to Pprov, and there should not be a data loss.
But there will be differences. Differences in some PPROF fields, like IDs, orders of, PPROF, elements, and, if you convert, Autel Profiles data to PCROF.
You will have definitely, loss.
Liudmila Molkova 00:18:28 it… I'm not sure I understand. So there is something that needs these attributes, and something that populates them in some way.
Florian Lehner 00:18:37 Yep, this does not exist yet.
Liudmila Molkova 00:18:40 So what I…
Michele Mancioppi 00:18:42 This reminds me a lot of what happened with the log event, with the event name field in logs, where it started as an attribute, and then it migrated into an OTLP field.
Florian Lehner 00:18:55 We are going the other way around. We want to remove the OTLP field and, want to have an attribute.
Michele Mancioppi 00:19:02 Huh.
Why?
Florian Lehner 00:19:05 For convenience and for keeping the protocol simple.
Michele Mancioppi 00:19:10 Okay.
I see.
Liudmila Molkova 00:19:20 Yeah, I don't have a concern with the specific PR, but I think the… The… you're… you're adding this attribute for a reason.
And there… there will be something that does mapping, and it should be documented. It… it… There could be multiple ways to do this, maybe it's not… Too strict, maybe it's loose, but it should be documented.
Florian Lehner 00:19:45 I could just pull… put the documentation in chat, so that's the PR that just started with the content for profiles and the specification.
And… Yeah, One step after the other, but as long as specification and semantic convention takes most of the time, that's the place where you're most active.
We cannot have everything at once, that's unfortunately not possible.
Liudmila Molkova 00:20:14 Yeah, that's okay, but I'm arguing with your statement that it will never be documented. It should be documented as.
Florian Lehner 00:20:23 It will be documented, it's not done yet. It will be documented. Okay, okay.
Liudmila Molkova 00:20:27 Okay.
Florian Lehner 00:20:28 It's.
Liudmila Molkova 00:20:28 Agreed.
Florian Lehner 00:20:29 OpenTelemetry I.O. specification is the place, There are gear gaps, we are aware of that, but we can just close the monitor at whatever time.
Liudmila Molkova 00:20:39 Oh, crap.
Sounds good. So then, I'll take a look at the PR, it doesn't seem controversial at all, and the general feedback is to move towards documentation for the mapping.
Florian Lehner 00:20:54 Cool, thanks.
Michele Mancioppi 00:20:56 Can I ask for, preferential treatment, because I need to leave in 10 minutes. Can I please have, an idea of how the peer.service discussion can evolve from here?
Josh Suereth 00:21:13 Yeah, next time feel free to add it into the general topic agenda ahead of time.
Michele Mancioppi 00:21:18 Forgot about it, sorry.
Josh Suereth 00:21:19 Yeah, no worries, no worries.
Michele Mancioppi 00:21:25 So my understanding was that, The last time there was consensus about… no. The last time Trask said that DPR, so the remodeling dp.service namespace, should not be dependent on the kind of embedding mechanism that you, Josh, were discussing, I think.
two weeks ago, in the SIG.
I'm glad to hear that.
But how do we proceed with the PR itself?
Josh Suereth 00:21:58 Yeah, I think the… so… I still have a lot of concerns around peer, but primarily, we need an implementation that generates peer.
That we can look at, right? That's one of the things we want for these, but specifically with peer, I'm a bit nervous about the scope of that namespace, and you saw, like, the discussion we had here. I think you saw the recording. So, I don't want to repeat everything I said last time, because I talked a lot, so I'd like to hear from you. What do you disagree with from that discussion? What's your thinking around peer? And what would you like to see?
Michele Mancioppi 00:22:36 I do not have a strong opinion about what the solution should look like. I have some concern about breaking open tracing sites that were using pure.service. Pure.service is fundamentally a manual instrumentation thing. I know of no implementation that adds it automatically.
The closest thing I could imagine is a collector processor that would do that, but it would be incredibly critical, because it would assume that Effective client and server, would come in in the same collector in a useful time frame, which is… Just not happening in the collector in a reliable fashion.
So I do not believe that necessarily there is an implementation, we should volunteer. There are, however, implementations out there.
of open tracing-related components that do rely on peer.service being peer.service. I made a cursory search in the OpenTelemetry organization, and there was some Zipkin router thing that actually is looking at the value of peer.service.
I don't know if that counts towards what you were asking.
Josh Suereth 00:23:45 That… that would count, but that would mean it would go in a compatibility letter.
Michele Mancioppi 00:23:49 Okay.
Josh Suereth 00:23:49 Right, so, but our compatibility to layer namespaces is an OHTL namespace.
we don't really have a good place for this. So, I guess my thinking around peer.service, and I think you heard that, I… For context, we have a system that does peer.service mapping, but not peer.service. We call it something completely different.
Because it is, as you suggest, kind of fraught with peril to do at the client side. You have to hardcode that knowledge, it can be wrong, very easily, and it's better done joined later in a downstream system.
We don't have it… so right now, a lot of our conventions are around what the telemetry that's generated looks like.
We don't necessarily have conventions around how to join together data and create new things that everyone agrees what the joined data will look like.
The other thing is, you're talking about conventions from OpenTracing, which I think will have… I don't think we have a great open tracing representation here, so, I'd want to find some folks from the Open Tracing ecosystem to talk to about this, but, you know, If OpenTracing uses peer.Service, that's great, that doesn't mean that OpenTelemetry needs to continue to do that.
we might want to think about some other thing, that works. But generally, what I don't want to do is, and we've blocked these in the past, where you have a namespace that is so generic and problematic that it can get abused. Peer.service, again, the peer namespace, I think, is my main problem.
Right? Of anything could be peer, and we've previously kind of put peer inside of network, right? So there's a network peer that is well-namespaced, it's clear what that means, what the scope of it is, where it fits in. Service.peer.
I think would be acceptable.
I still… this one still actually makes me rather nervous, though, of, like, just putting this… this pen.
Michele Mancioppi 00:25:43 It makes me nervous as well, because we end up with a namespace that is split Between resource attributes and signal attributes.
That is something that users generally do not understand. I see, for example, recently, I found we have, issues in the cubeless.receiver, because Some metric data point attributes, like case volume type, were put by OpenTelemetry maintainers.
into the resource.
So even maintainers do not get it always right.
Spitting it across things sounds…
Josh Suereth 00:26:20 Mighty, like, fraught of…
Michele Mancioppi 00:26:22 Like, pain. Just pain.
Josh Suereth 00:26:25 to some extent, your arguments, like, I understand that it can be confusing for users, and I do think we need to clearly delineate what is resource and what is not. I don't think it's practical for us to enforce generically that you never have conflicts between resource and signal.
We literally don't have that in place in OpenTelemetry today, it's something we can't prevent.
We can…
Michele Mancioppi 00:26:49 I would not… don't get me wrong, I don't think we should enforce against it. I'm just saying that this likely will always come at a cost.
Yeah.
Josh Suereth 00:26:57 That I… that I agree with, yeah. And I think we already have that today in a bunch of places. So… Right? Like, if I report my host address versus the server address of the span I'm talking to, if I put server's address in resource, that's a reasonable thing to do, and now I have confusion, if I try to flatten this and stuff. Agreed, but I think that that, I think we need to find a way to address that head-on.
and make that easier for users. But I don't think we want to propagate, like, okay, throw a random string in front of things to disambiguate. I don't think that necessarily helps.
but, it's possible. Like, anyway, we… In terms of making progress in Service.peer, what is your goal? Like, what do you need from Service.peer? You want the name to be stable so people agree what it means in the open tracing ecosystem? Or do you want people within OpenTelemetry to start using it?
Michele Mancioppi 00:27:58 I want people… I want to have… an official blast way in OpenTelemetry to… to do in the OpenTelemetry fashion what Pierre the service did in OpenTracing.
Josh Suereth 00:28:09 Okay, so sometime after the fact.
you join together data and understand this A is talking to B, and I can annotate the peer service in the span.
Michele Mancioppi 00:28:19 Or, if I'm working with users that are doing manual instrumentation.
Then they have an official way to do it.
Because there are advanced users, like, all the period of service. Like, when you go and talk to lightstep people, I don't believe anybody ever set it automatically. It's all manual.
But it had semantics. Today, we do not have a way in open telemetry to express that semantic.
Or at least we have it, but it's broken, because it doesn't work with service.namespace.
Josh Suereth 00:28:50 Yeah.
Liudmila Molkova 00:28:54 So if I… Yes? If, if I can… just to summarize.
You would like to build.
Let's say, service graph.
Be able to build a service grant.
And, annotate the leaf nodes or outgoing nodes with some extra information about The… what's being called.
Michele Mancioppi 00:29:19 I would not go as far as to say the graph, because it's more like point-to-point.
Josh Suereth 00:29:28 Sure, but for one point, you're trying to… you're trying to… on an edge, you're trying to say, here's my source, and here's my destination.
Michele Mancioppi 00:29:34 Absolutely, yes.
Josh Suereth 00:29:36 Yes. Okay. I mean, for context, We've been going a different way, internally at my company on how we do that, and we actually do use the same attribute in both places.
And then, when we render it to users, we disambiguate.
Michele Mancioppi 00:29:55 Okay.
Josh Suereth 00:29:56 Which is also why that was my proposal, because I know that that works, and that it uses the same semantics, and it actually uses semantics as I think they're intended, right? Like, a client span is the attributes of the client you're talking to. So putting service name in client span means this is the service I'm communicating with.
If we look at the model of OpenTelemetry as it exists today. Now, is that confusing to people who try to flatten? Will that confuse users? Yes. I think that that takes some… like, that's not a… Thing that we just step into and do.
Michele Mancioppi 00:30:27 The, it's gonna be incredibly confusing for, users that are grouping across those spans by the same key.
Josh Suereth 00:30:35 If they're using the OpenTelemetry data model.
And not flattening, it should be fine.
If they're flattening, or if they're not namespacing the OpenTelemetry data model when they flatten.
Right?
Michele Mancioppi 00:30:49 I believe the problem is flattening. I believe the problem is when you make a spans grouped by.
pier.whatever, just… I'm using the peer.service.
Josh Suereth 00:30:59 You're going to see both sides.
Michele Mancioppi 00:31:03 And that is going to be confusing.
They would see both the clients to a service and the downstreams of a service, the same service.
Josh Suereth 00:31:11 Why would you… why would you see that?
Michele Mancioppi 00:31:13 Because you would not be grouping at the same time as mankind.
Josh Suereth 00:31:17 No, no, so, so… If you do group by service name, right?
from a span attribute, you only get the outgoing services. If you group on the resource attribute, you only get the source attributes.
Michele Mancioppi 00:31:34 Oh, okay.
Josh Suereth 00:31:36 Yeah.
So, it should be totally fine. Like, again, if the semantics are, if it's on the span, it's about the thing the span is talking to.
And if it's on the resource, it's about the source.
I think we're in okay shape here, it's just it's confusing that it's the same attribute, but if you namespace appropriately and tell people this is the span attribute and this is the source attribute, then it's more clear, right?
Michele Mancioppi 00:32:01 I, usually don't like to do this. I mean, of course, there is a concern for tools that do not differentiate in terms of the end user experience, at which level the attribute is.
Josh Suereth 00:32:14 Yes, yeah, that, I think, is the biggest argument against what I'm suggesting. From a pure open telemetry perspective.
Right, and again, this is why there's, like, me, theoretical me, and then practical me, okay?
Michele Mancioppi 00:32:26 Okay.
Josh Suereth 00:32:27 Theoretical me is, like, this is a clear way to handle this. That doesn't involve a lot of work that I think will, from semantic conventions, I should say, but is, like, a way that actually addresses some of the problems in OpenTelemetry generally of resource versus span. We need people to understand that difference eventually, because this will just continue. So people who flatten should be namespacing, right? That's theoretical me.
Then there's practical me of, okay, how do we help people who are doing this today not just suddenly break and die?
if this is, like, really needed in the community and, like, a big… a big thing that people leverage, we need a path forward, okay? So, my thinking is, for now.
You don't need a semantic convention to use an attribute in OpenTelemetry. Semantic conventions are about standardizing its meaning and that use case across how we want people to do OpenTelemetry.
So, when we standardize on a semantic convention, it's like, here is what we think everyone should be doing.
I don't think peer.service is how we want things to go going forward right now. And that theoretical me is in disagreement there. So that's why I don't think… like, I think we should continue to say service.peer is fine to use.
Right? And you can use service.peer.namespace, and we won't be adding to peer namespace, or peer.service namespace, or whatever. You can feel free to use that. We won't be adding to that in SEMCOF.
Where we need to figure out what's going on now is if there's, like, an OpenTelemetry piece of instrumentation.
that provides service names, or sorry, peer service, or peer service namespace.
that will have to be semantic invention compatible, right? So that's where… that would cause us to have to make a decision here.
And if that thing already exists, and you're telling me it does, then I think we should start prioritizing to figure out the solution. It does not exist. Okay.
Michele Mancioppi 00:34:21 knowledge. What exists is, exporters in, in OTIL that rely on peer.service work in the way it does.
Josh Suereth 00:34:32 Export… oh, you mean Zipkin.
Michele Mancioppi 00:34:34 Yeah.
Josh Suereth 00:34:35 Yeah, yeah, yeah. But in Zipkin, we actually get peer.service like, we have to have people provide peer.service for Zipkin. So, I do think for Zipkin, we can have peer.service stabilized for Zipkin.
But Zipkin doesn't have a service namespace, does it?
Michele Mancioppi 00:34:53 No, not to my knowledge. It's just the service.
But I'm not, not a ZPN expert.
Alright, so I will, I created an issue with this, and, I'll… I'll try to describe what we just discussed on the issue, and meanwhile, I'll close the PR, because it's not applicable.
And that would be better.
Josh Suereth 00:35:16 Yeah, yeah, I think… I want to talk a bit with the other SEMCOM maintainers to see where they stand on this, because I'm not… it's not my decision, you know, it's our decision, so we'll do a chat off that. Don't close your PR just yet, we'll have a discussion on chat about it, and then we'll come back to you with… if you want.
Michele Mancioppi 00:35:34 we'll let you know if we're not planning to go forward with it. Just let me know how you want to go forward. I believe that there should be a way described in the SAMCOMs for users to do that, because the fact that SAMCOM's seen as the way that instrumentation should work.
Yes, but it's a very project-centric view. It doesn't help the end-user sides, but… I can live with that, if that is the decision.
Josh Suereth 00:35:59 There's also… a compatibility part of the specification, where attributes in SEMConv are defined in the specification. So the semantic convention registry is actually dependent on the spec. The spec gives us license to do what we do.
In the spec, there's attributes that are demanded for compatibility. All of the ones required for Jaeger are in there.
So, it would be reasonable for me to say Zipkin's an important enough use case. We should have the Zipkin compatibility in the spec, yeah.
In fact.
It might already be there? No. That's all the old stuff, I think. Oh, in Zipkin Exporters, yeah.
Michele Mancioppi 00:36:40 Whoa!
Josh Suereth 00:36:41 So it'd be… it declares.
Michele Mancioppi 00:36:42 I believe we say your name, Michaela, and you are here.
Alright, I'll, continue. Sorry for this. Querying metrics, in OpenTelemetry.
Josh Suereth 00:37:00 Alright, so I think a path forward would be… we… we update this for Zipkin, but if I understand correctly, I don't think Zipkin can support peer service namespace.
Liudmila Molkova 00:37:14 It probably will never change.
Josh Suereth 00:37:18 Yeah.
Anyway, sorry.
I'll hand it back to you, Lyudmila, but I think… I think we need a little bit of a discussion offline about this to figure out what we want to do, but my… my recommendation right now is we stabilize peer.service as a compatibility.
metric that is used for Zipkin.
And we do that in the specification.
With a list of, like, compatibility things we have.
And… if you look at some of these attributes in here for the Zipkin mapping, I think we might have changed some of them as well.
Liudmila Molkova 00:37:56 Yeah, and this is a stable document.
Josh Suereth 00:37:59 Yeah.
So… I don't know what we want to do with that, besides, I think we've basically decided to move away from Zipkin.
Support.
Anyway, let's have a discussion. I'll open a chat thread, and we'll have some other talks in other places, because I think this is actually problematic.
Liudmila Molkova 00:38:21 But beyond SEMCOMF.
Yeah, so one thing I wanted to share, there is an effort, To introduce some, it's actually part of the configuration, the development, part.
That there is a formalized component that works, like, it matches IP address.
Or maybe the, the DNS name.
And depending on the IP address or DNS name, sets peer.service. I think it's used for span through metrics conversion and to power things like service map.
So there is a, sorry, general interest in this thing.
whether we like it or not. We can say it's not part of semantic conventions, or it is part of semantic conventions, but yes, I agree, we should make some decisions.
Josh Suereth 00:39:22 Let me be clear, if you… if we wanted to have that thing do… use, like, a service.peer.name and service.peer.namespace?
I'm actually okay with that. It's peer, the namespace that I have problems with. Who owns the peer namespace?
Right? Having the service folks own the service namespace and putting peer underneath it, so you keep the two in sync? Great. But peer, how do you keep peer and service in sync, otherwise?
And how… what if, like, every… every single namespace could show up in Peer?
That's problematic. That's why… so Pierre is the one I don't like.
But service.peer.namespace, I'm actually fine if we go that way, it's just that is… would be a breaking change.
Liudmila Molkova 00:40:07 Oh, now I see how embedding comes here. We would embed service.
Peer on their service.
Okay, thank you all for the discussion. Let's take the next steps among maintainers and figure it out.
Josh, you want to talk about general SIMCON maintenance work?
Josh Suereth 00:40:53 Yeah, so this is just, there was a chat thread in CNCF Slack that, reminded me that, we have a bunch of missing how-to guides. So this is a call to action.
For those of you who have stabilized metrics, or spans, or events, that we are looking for some how-to guides to help people through that process. If you look in… yeah, thank you, Lydmela. So, in Docs, we have how to write conventions. There's a README. This README is a great starting point. It has, a bunch of to-dos, though, around how to do different pieces.
So it starts off with some general notions and, like, how we think about stuff, talks about system-specific, it's, like, our entry point into how to write.
conventions. But we're kind of missing some of our justification for decisions we've made. We're missing, We're actually just missing a whole guide.
So, I think there's a few things that I'd like to call out here. If anyone who has stabilized spans or metrics, or events are interested, there is just a, how do you actually define the stupid thing? Like, let's write up the doc, right? And then, how do I go about thinking about conventions?
there's, again, in that… in that section, there's a whole bunch of good stuff about… we have something about T-shaped signals, we have how to do attributes, how to think about attributes, there's general naming guidance in SEMConv already today that people fleshed out. The entity SIG, we put together an EntitySIG modeling guide for how to do resource and entities.
So there's a bunch of good stuff in there.
But… this is a, I think, somewhat low-hanging fruit for folks who want to at least get started with this. What I would like to do is capture a lot of the expert advice that we have and things we've learned.
in stabilizing, the conventions that we have so far, right? So, we want to make sure that this is, up-to-date with, like, where we're going in practices. For context, the discussion that we had.
Yeah, I think there's a bunch of issues on… on… for each one, I believe, we open one.
We had a discussion about why we are doing, Usage and limit metrics instead of utilization metrics.
And that discussion we've had to have, I think… I don't know how many times I've had that discussion with people, both internal to my company and in open source. It seems like it pops up, every 2 months or so. And, you know, that's an opportunity for us to take that and, like, write it down.
I think if you look in the non-normative guidance as well, there's a lot, like, the System SEMCOM folks have been writing down. I think CICD got some stuff written down there.
Anything we can get to make, like, central repositories for people to get up to speed on the complexity of this domain, and how to get started would be valuable. So, this is a call to action, and just, thank you, Lamila, for walking through here. Under non-normative, I think if you click on that.
We're slowly moving stuff.
There's another how to write conventions here that I think was a merge conflict of why that one's still there.
We moved the directory, but the merge conflict didn't move the new file. So this is a, you know, how to think about state metrics, for example, right?
Anyway, call to action to get more of these things in.
And more of how to think about compatibility, how to think of, How to think of attributes, how to think of metrics in general use cases.
The more of this we can get written down, the better.
Liudmila Molkova 00:44:38 I could not agree more.
So we, it's extremely hard to go through the old issues and pull requests to understand the reasons we made decision, And, even to capture the common practices. So one thing we've… I think we've been doing, is that whenever some part of the guidance evolves.
Were documented in the issue.
And, we doc… I'm trying to remember any of them. I think Trask opened a few, where we just list evolving practices, in the issue, and once we kind of feel there is a consensus, we start Documenting it in the, in semantic conventions.
Or, I think some of the issues, about how to… The capture… Principles.
So, like, if anybody wants to work on any of this, there could be some pointers.
and… and things to cover.
So… If anybody wants to start doing this.
Please, create a draft, ask for… for the details, ask for the feedback, and once, there is an outline, people will be… it will be much easier to contribute.
more details.
Josh Suereth 00:46:21 Yeah, another way to rephrase what Ludmila said, if you want to write semantic conventions and you had a bunch of questions, write the outline of all the questions you had in the order you wanted to read them, and just send it with a bunch of to-dos. And that's a good enough start for us, right?
Liudmila Molkova 00:46:39 Yeah, thank you for rephrasing it.
Oh, how to create migration guides. So, actually, we… we can automate this, pretty much.
Josh Suereth 00:46:55 So we can remove that section of the how-to?
Liudmila Molkova 00:46:59 I think we cannot remove it, I think we should, First, automate it, and then remove it, right? It's manual until we automate it.
Josh Suereth 00:47:08 Okay, got it, got it.
Liudmila Molkova 00:47:22 Okay, we have… 15 minutes left, do we want to go through the PR triage board, or do we want to call it a day?
Josh Suereth 00:47:39 We could let most people drop off, and maybe those of us who, are able to, like.
Approved PRs can continue with a little bit of triage.
Liudmila Molkova 00:47:49 Yeah, sounds good.
Okay, so let's take a look. There is something that's ready to be merged, but I think it's not.
There are some open discussions.
So this is up-down counters to follow non-pluralization rule.
So, it's up-down counters, and for them, we recommend to use .counter something else that's, like.active, or something, that's applicable. But there is an active discussion here.
I don't think we have… is Chris here?
Okay, so, and there is a discussion on renaming.
Okay, apparently… There is an ask for… Help.
Josh Suereth 00:49:08 Yeah, I think the one above was actually the most important, A discussion that was unresolved, that… we should follow up with Chris on was… this is why I didn't merge it when it had enough approvals. The, so basically the question is, instead of having, like, Kate Stamen misscheduled nodes, having .node.misseduled.
So you'd have, like.node.misseduled, and then if we want .count, you would put count on there. But this was a name and proposal that I think is a… Human readability thing.
And it uses less underscores, or none.
in the naming convention here. So, given that we have kind of stopped using underscores in many places.
I don't know if that's important, but that was the one I wanted to see if they'd resolve before we would merge.
Liudmila Molkova 00:49:58 Yeah, I'll leave a comment. I think this, this matches, other things we have defined. So, like, here, you see, like, node becomes a namespace, and then you can have multiple things under the node. It's probably totally subjective what is better, but… and it's still… it's a grouping mechanism, which makes sense. So this… This version looks more semantic conventions to my eyes than that one.
Okay, I'll take a look at this one, and we'll hopefully resolve those discussions. So, there are some, trivial… I think I've seen some trivial, version updates.
PRs that we should just merge.
josh, maybe you can approve this one and merge?
There was another… PR that fixes… pipe our CICD.
This one from Tarosk.
I'm pasting in the chat.
And… the… This one.
So let's take a look what else we have and needs more approvals.
I remember this one, there's knob date.
Consolidate thread details into YAML registry.
Daniel Dyla (Dynatrace) 00:52:12 There's an open comment on… 2929 from Trask that says we should close it after 2931 is merged, and it should get reopened.
Liudmila Molkova 00:52:24 Oh, okay.
Awesome, thank you.
Okay.
We won't be able to merge it anyway, because it has a broken check.
Thank you.
What's going on here?
Okay, there was a part of the markdown.
that's now moved to YAML.
Okay, this makes sense to me.
So I'm going to approve this one.
And it's now ready to be merged.
If anybody wants to take a look.
the peer service, I… let's… let's wait for the outcome of our discussion on the peer service before we take a look.
Hey, there is a bunch of things that add something as a cloud entity. The reason I didn't approve it is because I think what it does, it just adds a constant.
And… I think it's… Not enough, in general.
And we, we have a… best practice that advises against it. So, for example, we would probably want to document how cloud resource ID looks in this cloud, what it's… How it's obtained, and other properties related to the cloud.
I think we don't… have… Good documents that describe it.
So, like, we would ideally have an, I don't know, AWS cloud, Azure Cloud, Similar to specific databases.
So, at the bare minimum, I would ask to update the examples and maybe notes here on how to capture this in the clouds being added.
Oh, right here.
Josh Suereth 00:56:12 Can you go back to the PR? What's the actual proposed change?
Liudmila Molkova 00:56:18 to add… There's two constants.
Josh Suereth 00:56:23 Okay.
Liudmila Molkova 00:57:02 To some extent, I also feel that we don't have a group that works on the cloud.
Josh Suereth 00:57:08 Yeah, actually, this is one I want to kick off, because these have been problematic for GCP. We actually… our resource detectors really struggle with these.
particularly… I think they're designed a little closer to how AWS runs than how GCP does, so, like, availability zone is highly problematic for us. We actually have to duplicate it in a few cases, where we have other attributes that mean availability zone to avoid conflicts, because One resource can have multiple availability zones that are relevant to it.
like, a Kubernetes cluster.
Can have a node that runs in a separate availability zone.
And so, when you have one cloud availability zone.
what does that mean? Which one do you put there? Like, what guidance do we have? So, I do think that we need to get a group together on this. I'd agree. I'm happy to sponsor from a GCP standpoint, but I do think we need to get some other cloud providers, so… Yeah. We should put that on the list of, SIGs we need to create.
Liudmila Molkova 00:58:15 Okay, yeah, that sounds reasonable. So we would effectively put this PRS on holds, unless such a group is… Ormed.
Josh Suereth 00:58:35 Yeah, I mean, is there anything in it that you think is blocking them? The main blocking thing is that they just haven't defined the rest of the cloud attributes, right?
Liudmila Molkova 00:58:44 I haven't updated the rest of the cloud attributes to cover the Akamai. I'm also… Like, if the group is formed, we would actually need to update pretty much everything. So you see here, it's AWS underscore EC2. This needs to be updated to follow our dot guidance everywhere.
And work consistently.
The fact that we put underscore cloud everywhere, not sure if it makes any sense at all.
Josh Suereth 00:59:16 I mean, now? Well, GCP also has underscores, because we predate the dots as well. If you scroll down.
Liudmila Molkova 00:59:22 Right, yes.
Josh Suereth 00:59:23 Yeah, so does, Oracle, and yeah.
Tencent, so…
Liudmila Molkova 00:59:28 So, like, I don't feel we have to block these PRs.
But also, whatever they're writing would be eventually broken.
Josh Suereth 00:59:39 Yeah, I think it's fair then to… I would ask them to put dots, and I would ask them to figure out if they can fill out resource ID, and if not, we… we'll have to think about things. One thing we… Yeah, cloud is not considered stable yet, but people depend on it heavily, so we have to be careful with breaking anyway.
Liudmila Molkova 01:00:35 Okay, I'll add the comments on the PR.
And we are at time. Thank you all.
Armin (Dynatrace) 01:00:46 Thanks, bye-bye.
