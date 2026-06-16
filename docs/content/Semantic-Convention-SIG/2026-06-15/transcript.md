SIG: Semantic Convention SIG
Date: 2026-06-15
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

Liudmila Molkova 00:02:28 Hello, hi everyone.
Trask Stalnaker 00:02:37 Happy Monday.
Sven Cowart 00:02:39 Hello.
Liudmila Molkova 00:02:39 Happy Monday!
I'm not sure whose turn is it to run the… call?
Trask Stalnaker 00:02:58 I think you and Josh did it most recently?
Liudmila Molkova 00:03:02 I…
Trask Stalnaker 00:03:06 So, really.
Keep track.
I can drive today.
Alright, we will start with… Triage, and if you've got any topics you want to discuss, go ahead and throw them On the agenda.
So, I've seen… I think there's active… Engagement here from the… System… SumCon sig… I assume… why does it say… O.
Blocked is not automatic, okay.
blocked.
GitHub moved this to blocked. Oh, okay, look at that. The project automation moved it to blocked when it got blocked.
But I'm assuming… it got done?
Blocked? Or not? Oh, no, there is. Okay.
I was just, for some reason, expecting The block sample up here.
Alright, so that is… Still blocked.
Promote… Oh, looks like Adria… So what are we… just… Sure… Promotions… that's exciting.
Oh, one rename, okay, yeah.
Looks like, Alright.
And… haha, there, now it shows… I understand the logic here, GitHub's UI logic of when it displays The blocked there, or not.
Needs more approvals… Ready to be merged.
Remote process… to RC…
Liudmila Molkova 00:07:26 Oh, this… unfortunately got hit by a recent check I added to… not allow… Garop… To have a lower… Stability done.
Attributes.
And I'm… I'm glad we caught it.
It's unfortunate that This PR got hit by it.
Trask Stalnaker 00:08:26 What is stability…
Liudmila Molkova 00:08:30 Yeah, let me find the bug number.
But I think it's mentioned somewhere. Stability level on the group, must be… The same or higher than, attributes, or opt-in attributes can have.
Lower level.
Trask Stalnaker 00:09:13 Alright.
Avoiding code owners… Got a couple of… HTTP ones… This is probably the… Most interesting…
Liudmila Molkova 00:09:47 I think it's… just waiting for the review, and I was going to give it another… round, but I didn't have a chance, so I'll try my best.
Trask Stalnaker 00:10:19 And so, any… we're good with any here. Do we have any… precedence for… capturing… body… Content.
We're doing that, kind of, more or less in… Gen AI… I guess.
Anywhere else?
Liudmila Molkova 00:10:43 Okay, we have some other… any… precedence… This is a special linea here, though, because it's… A union of binary and the ring.
If you feature a flag result.
Trask Stalnaker 00:11:05 Oh, that's why… because of binary, okay.
Yeah… That makes sense, thank you.
Liudmila Molkova 00:11:20 Oh, this one, I think I raised a comment But… It seems, here we are… Suggesting to have another configuration option.
To limit the body.
I don't know how to think about it.
Trask Stalnaker 00:11:55 I see, in addition to the standard… configuration… Yeah, I think, We had brought up, I think in the… one of the discussions, there was a mention of the database query… Which I think we did…
Liudmila Molkova 00:12:36 I think we're limiting the query summary, and we're limiting it to something very short, to 55, because of its suspend name.
I don't remember, us limiting the text, yeah, but worth checking.
Trask Stalnaker 00:12:52 Maybe that's something we only did in Java.
Liudmila Molkova 00:12:57 Oh, you did it in Java, huh? Do you have an option for it?
Trask Stalnaker 00:13:02 No, I think we just… Probably hard-coded it, at something absurdly large, just because.
Some people had, like, 20 megabyte query texts, and it was causing memory, System to go out of memory.
Something like that. What is it?
Yeah.
I won't find it.
Yeah, the problem is that the default for SDK is to not limit.
is no limit.
But the difference here is this is an opt-in attribute versus, like, db query text, which is not… Which is recommended.
Liudmila Molkova 00:14:13 Well, the opt-in mechanism could be by specifying the limit size.
And by default, it's 0, so nothing can't capture.
Trask Stalnaker 00:14:21 Right.
Liudmila Molkova 00:14:23 So I, I… Think what we discussed last time.
with Josh is that maybe we should have a generic way to handle it, maybe the limit should be for all.
Attributes that are expected to be large.
Michele Mancioppi 00:14:53 This is really interesting.
Liudmila Molkova 00:14:54 So.
Michele Mancioppi 00:14:56 I, I've… there were several OTEPs around this, right, in the past?
I remember I've seen OTEPs for introducing annotations to collect HTTP payloads from At least two serverless vendors.
The names I no longer remember. I think Epsagoon did it at least once.
Maybe Tandra did as well. Are we going to do this in, in, instrumentations.
Liudmila Molkova 00:15:28 So here, the annotations are in some kind.
And, Tresky, if you scroll down a little bit, there is an example.
I think…
Trask Stalnaker 00:15:36 Kelly is asking more just generally about the body capturing the ACV body.
So Sylvain has been prototyping this in the Java instrumentation repo.
So, I suspect we would… accept that, like, it is something we've heard in the Java instrumentation repo for… Probably at least 5 years old.
Michele Mancioppi 00:16:04 Oh, yeah.
Trask Stalnaker 00:16:05 So it's a common request, we've just kind of… Pushed it, because… It's also very complicated to-do Well…
Michele Mancioppi 00:16:19 So, is it… it was my understanding that in the TC, at least early on, the idea was We will never collect payloads.
This is changing now.
Which I think is a good change.
But I was not aware that the policy changed.
Liudmila Molkova 00:16:37 There is no policy on this.
an existing one. But yeah, I think there is… there is a… there was a consensus that the payloads should not be collected, but… Given they use overwhelming asks around it.
And that did something, and that we already do this for GenAI. I think Gen AI changed a lot of mental models.
I think we are at the point that I would be… I'm supportive of this, to start collecting the payloads.
as often.
Michele Mancioppi 00:17:13 I can tell you, for example, all the serverless tools have collected payloads in Lambda since the beginning of time, because it was the only way to debug stuff.
So, I'm in favor as well, I'm positively surprised.
Trask Stalnaker 00:17:27 Good.
Michele Mancioppi 00:17:28 It also creates a huge gap, because now we have yet another semantic invention that is implemented virtually nowhere, except Java.
But it shouldn't stop us from opening the floodgates.
Trask Stalnaker 00:17:56 odds…
Michele Mancioppi 00:17:56 I just joined at the right moment. So, something on screen that really piqued my interest.
Trask Stalnaker 00:18:06 Yeah, I… I recall, I think that, we could probably find that OTEP, and yeah, I think, 5 years ago, things… people also felt there were a lot of, Yeah, that we didn't need to do that. It's been a long time.
So as far as annotating…
Liudmila Molkova 00:18:36 So we would introduce the sanitation value size, let's say, and now should it be t-shirt or some other form, this is, Not that important.
And then… We could also introduce the configuration property that limits the… It allows to configure The common limit for large attributes?
But then, why would it be a limit for a large attribute? It can be a limit for any… attribute. Like, how is it different then?
I could get in back to the PR. I think the… The key question, whether this limit should be… Required. Currently, it's required.
I think it shouldn't be required, but it's totally fine to have a configuration option that That's it.
Michele Mancioppi 00:19:50 Don't we have a red-in option?
in some SDKs and in the collector to truncate attribute values.
Trask Stalnaker 00:20:00 Yeah, that's this guy here.
So this is currently proposing to have an additional like, limit.
Since this one applies broadly, it's one limit that applies to all the attributes.
Yordis Prieto 00:20:22 Would that be below that global one?
Oh, the collector one?
Because that's where the trickiness starts happening.
Liudmila Molkova 00:20:34 This one would be preventing the… it would be at the… the moment attribute is populated, and the SDK limit, or whatever you haven't collected, would apply to already recorded span.
Well, not recorded, but in the pipeline.
Yordis Prieto 00:20:56 So, to be clear, something else could still truncate even further, right? As for…
Trask Stalnaker 00:21:03 Right.
Liudmila Molkova 00:21:04 Perhaps this is the… the… Save belt for the memory usage, so you don't even read the stream beyond something.
And this is why it's must.
Yordis Prieto 00:21:24 Yeah, because there are gonna be multiple filter supplies, like, being explicit or clear about, okay, when this actually applies will be important.
Even giving a name to those type of limits as well.
Michele Mancioppi 00:21:56 There is an aspect of truncation for payloads.
Specifically, that is worth pointing out, because I have seen it done right in only one product, which I'm not going to name.
Truncation should be aware.
Auto format.
So, if you take… most of the payloads that we're going to record are some sort of JSON.
Or Yamo.
You truncate it and it becomes invalid.
And all of a sudden, it is worse than before.
I mean, Trask, you're doing this, but in reality, there are smart ways, given a target limit.
to drop, for example, content from a JSON object, or a JSON array, or an array nested into an object.
still keeping it, JSON, valid.
And… What is missing today Is a way to say that that attribute got truncated.
So, if we had a way to say that attribute got truncated, then we make a truncation that is not invalidating the format of the payload, that is a better situation than just truncating in the middle of it.
Trask Stalnaker 00:23:25 Yeah, this one… It was probably too general… to have… Much logic, but, I mean, potentially instrumentation could be aware.
Michele Mancioppi 00:23:44 I would expect the collector to do mostly truncation.
The, truncation is not a cheap… thing to do. You need to introspect the payload. Depending on the format, it gets really funky.
So, if we did a semantically correct truncation of a duty in the collector.
But my point of, we need a way to specify that that attribute got truncated by this much.
Would be valid regardless.
Trask Stalnaker 00:24:17 Yeah, probably that needs to be raised in the spec.
repo… Because already we're doing truncation in the SDK.
And I don't think… so we record dropped attributes?
Michele Mancioppi 00:24:33 Bye.
Trask Stalnaker 00:24:33 I don't think we record the number of truncated attributes.
That would be…
Michele Mancioppi 00:24:40 And there would be a pretty easy way to do it, because in the UTLP, we're anyhow nesting the stream value into value, so that the value thing is an extensible object.
So if we added there, like, truncated characters, and then put a number, That would work.
In a mostly… Backwards compatible way.
Trask Stalnaker 00:25:59 Alright, let's see if we added any… issue any agenda items, and we did, alright.
Sven.
Sven Cowart 00:26:21 So… This is all about, and the, As a result of wanting to Pursue some of these flow-related, semantic conventions.
We need a way to express Attributes on source and destination.
And there is an existing pattern today for… Server and client.
And… That… that's, it's in, I think, the general naming docs, where there's a server client pattern that is described and how to use it, but it's not clear if that can just be extended, the same type of pattern could be extended to source and destination. And… With the key difference being in the docs for source and destination and client server, already clear about the fact that If you can identify client and server, you should use it, but if you can't, you should use source and destination, which is oftentimes the case for almost actually always the case for NetFlow-related and packet-related network telemetry. So… what I've tried to do is… I tried to be really clear, it's kind of hard, because… some… a decent bit to unpack here. But… more or less, there's two options that I see, and I tried to give an example, for example, like, pod name on Kubernetes, if you want to decorate the endpoint with it. If we use the exact same pattern that we have today for client-server, that would be… What do you see there under option 1?
And… I suggested another one option too, because that is typically what you find in the existing implementations, even, like, DIN IP fix official spec that's existed for Over a few decades, and I think… I've been going back and forth on this problem, so I tried to, like, in the questions underneath, I tried to explain the rationale and why I can see both being legitimate options to move forward. But the ask here is more or less to just… Let's extend the client-server naming pattern for source and destination, so that we can utilize that in the other, Network-related telemetry, Efforts that we're… we're… Trying to pursue right now.
Trask Stalnaker 00:29:07 Are there other, places this is affected besides Kubernetes, aspect? Because, like, a lot of the things… the domain modeling is already, sort of, essentially restricted to client-server, so we don't… this doesn't… Come up.
Sven Cowart 00:29:24 Yeah, there is. If you… One second.
So… I don't have any example right now, but I see this coming up in a number of places.
Particularly around all the… Anytime that we interact with packets and anyone would like to add additional attributes to that, regardless of if it's Kubernetes or not.
then, like, I could put… HTP on the end of it, right? Or, like, in an HTTP area, or RPC, or any of those other ones that exist. Even things like… the… Host name information, and… other things.
Would it make sense to pull more examples into this comment or issue and move from there?
Trask Stalnaker 00:30:56 it would help me, like, with the Kubernetes, The… like, what are… what specific… so, source, pod name, or pod name, Are you instrument… is this instrumentation all coming from the network?
Capture… And then you're kind of… figuring out ways to add in… layer in some Kubernetes stuff, versus it's captured from Kubernetes…
Sven Cowart 00:31:34 It's captured, actually, it's looking at actual network packets.
in the eBPF layer, and then from that, saying… and then using the Kubernetes API to say, oh, is there a IP address in the… where I'm running right now that matches the source and destination IPs that are within the network packets, and if it is, we can attribute the… the, the pod and node name, and basically all the Kubernetes attributes that exist and are relevant for that piece of information.
Trask Stalnaker 00:32:09 Why, nest it under… oh, because you need to put 2 on one.
Sven Cowart 00:32:15 Exactly.
Trask Stalnaker 00:32:16 telemetry.
Sven Cowart 00:32:18 Yeah, because it's… it's flow. You always have source and destination.
And there is a theoretical possibility that you could get client server, like, especially if it's in a Kubernetes environment, you could determine Potentially.
who the client and who the server is. But you'd have to do more than look at the packet data.
Right? You'd have to weave in some other… Other pieces of data to do that, and it's possible, but that's not really the direction.
I was thinking about going anyways with this work, because it's not how flow typically works, and so it would be kind of weird for users of flow data to see client server instead of source destination, and it wouldn't work in most other cases that are not Kubernetes, if the deployment environment's just bare metal, or… Or closer to it, anyways.
Liudmila Molkova 00:33:15 I'm curious, do you need to… say it's a Kubernetes pod name, could it be the… Source address and destination address and something else tells it's… what are… oh, you still need to solve the problem of recording two pod names on the same.
So let me try it, I'm right.
Sven Cowart 00:33:35 Yeah. Yep.
And it's… and again, it's all the Kubernetes. What we do at Merman is, I mean, we have basically the entire list of Kubernetes, so we give you the Kubernetes namespace, the node, the… all… everything we know about where that IP is running.
Trask Stalnaker 00:33:57 Just to tie it to a more general problem, like, even on client, we kind of have this… For client-server, you could still, want to… Those on to the, Like, what am I trying to say?
We ran into this problem with service name recently, where we have this idea of peer service name.
And we want to stamp that onto individual telemetry.
And so we tried this. We ended up with, I think.
What did we end up with, Michelle, that we still aren't…
Sven Cowart 00:34:48 This morning, but it looks like… You would be prefixing… Client server onto those attributes.
Michele Mancioppi 00:34:57 Yeah, we actually did, peer. No, service.peer.
name and service appear at the namespace?
And then, I got winged that we are changing that.
to, peer.client.
something. Or maybe client.serve is the name, and server.
That's… I don't remember. I lost track.
Liudmila Molkova 00:35:22 service, server, peer name, or something like this. Trex, you had a PR,
Sven Cowart 00:35:29 Thank you, bro.
Liudmila Molkova 00:35:29 I… I don't.
Michele Mancioppi 00:35:30 Only the ibuprofen.
Sven Cowart 00:35:33 If you go to the… someone commented saying that's the same problem, so it should be linked to the one I have as well.
Trask Stalnaker 00:35:39 Somebody already did.
Sven Cowart 00:35:41 Someone… I saw it this morning, so go… yeah, I think this is what you're.
Trask Stalnaker 00:35:44 Yes, yes, alright.
Oh, let's see what is…
Michele Mancioppi 00:35:52 I appreciate how I tried not to comment.
The topic came up, and then you brought me into it.
Trask Stalnaker 00:36:00 I know, I know.
It's a complicated one.
Or there's no good answer.
Michele Mancioppi 00:36:08 I think we are comple- we're making it a complicated one, yes.
I don't think it's… We like to do that. Yes, I don't know, I think we are over… over-engineering that one to death.
Trask Stalnaker 00:36:30 So… If, with this pattern, would support, I believe, and… is… I don't know if it's relevant.
But this is a… resource attribute. I kind of think it's relevant.
anytime we have re… I think it's a general problem. Anytime we have resource attributes.
That describes something. And then we want to… Attach that, basically, to flows, or… Requests.
To the target, the resource for the targeting side.
So, maybe this will help us… to generalize… This and feel good, like, that, okay, whatever, we're establishing a pattern here for… for it.
But I do think it would… this discussion at least supports the source dot, destination dot, as being the… Prefix.
Sven Cowart 00:37:44 Yeah, I think that makes more sense just when you read it, because if it… if it's under… If we use that existing pattern that exists, it feels like you're describing Kubernetes, not describing network traffic, right? And that's why I lean towards option 2 as well. It does.
Liudmila Molkova 00:38:04 In the existing… Oh, sorry.
Sven Cowart 00:38:06 Oh, go ahead.
RC Robert Cowart 00:38:07 I've just been listening, sorry I joined a bit late in the call, but I've just been listening, and I was leaning toward option 2 sitting here, too, for the same reason, Trask, when you were saying, like, that's a resource identifier already, K8 pod name.
been… source destination is specifying the two sides, so it makes sense that that's nested underneath. I also was leaning option 2 from the discussion.
Liudmila Molkova 00:38:32 Yeah, the thing I wanted to mention, that for… The option 1, the area client server.
This is actually span kinds. They are not the client server.
that… well, they are client-server, but, like, when we say metric HTTP client.
request duration, HTTP server, request duration, they are indeed the HTTP thing that we clarify further.
By the client or server where it happens.
And I think it's… it's even a different use case, or a different pattern.
So I think we are not even, making inconsistent things.
Michele Mancioppi 00:39:16 Also, I should warn about the user's award source and destination.
I had introduced that in Instana, which was not based on OpenTelemetry, but it was literally the same concept, and nobody understood it.
I would advise to stick with using the kinds.
So, server and client.
Sven Cowart 00:39:41 Well, but you don't know that. There's no way to know if it's client or server in what we're instrumenting here.
Michele Mancioppi 00:39:48 Because they're doing full duplex, potentially, right?
RC Robert Cowart 00:39:49 traffic.
Trask Stalnaker 00:39:52 And that, Michelle, that's… Relates to discussions we had when we did go with client-server, as opposed to originally there was, like, net peer and some other choices that, and it does feel like for the majority of things that we model that fit into client-server, that's a nice terminology.
Yordis Prieto 00:40:15 is…
Michele Mancioppi 00:40:15 If you know who's the source and who's the destination, you can call them however you want, right? But this doesn't reconcile with fans' comment.
About the fact that it doesn't know the direction.
Trask Stalnaker 00:40:27 Yeah, yeah, so that's why we, we added source and destination already exist in the semantic conventions, we just haven't used them, Because we haven't run into… I don't think we've used them, because we haven't had the model.
Things at the network layer where we don't know.
Michele Mancioppi 00:40:53 Oh, so the concern is that, for example, for a messaging instrumentation, they mostly do polling?
So the source would not be the client in that case.
And it's not even inclined to be, in that case, produced for a consumer.
Is that the… Or…
Trask Stalnaker 00:41:12 Polling, like, it's whoever initiates the connection is the client, and even though the… in polling, the messages are flowing in the other reverse direction, client is still the one that is doing the polling, and server is the one that's sending the data.
RC Robert Cowart 00:41:30 Jen, I'm gonna share over the top of you real quick, just for clarification. I can add this or send it to you to add to your ticket, but… but this is the thing, like, you know, connection over the network, some… some computer to a web server.
Liudmila Molkova 00:41:44 Or…
RC Robert Cowart 00:41:45 it sees this is the source, this is the destination. But when the web server answers, the web server is the source, and back here is the destination. However, in both cases, this was always the client over on the left, and the web server was always the server.
And that's… that's the dilemma, that the… depending where you're observing from, does source destination.
Michele Mancioppi 00:42:13 What?
RC Robert Cowart 00:42:14 flips, right? And there are things you can look at to make a good guess. For example.
443 is a pretty common port number for servers, so you can maybe try to make an educated guess that's the server, but you're not guaranteed, from this perspective that you're observing from that that is true or not, right?
And so… but it's… but it's this dilemma of the source destination flips depending on the direction that it makes it different than… distinctly different than client-server.
Michele Mancioppi 00:42:45 But this is not even a matter of the protocol, because in the case of the, of TCP that you are depicting here.
The client and the server are always clear, even at the protocol level.
the client opens the socket. It's never the other way around, right?
So, yeah, you're talking about.
RC Robert Cowart 00:43:03 similar.
Michele Mancioppi 00:43:04 level of the HEP response request.
RC Robert Cowart 00:43:07 Sure, but that assumes you're doing deep packet inspection. Let's say you're getting a NetFlow record or a firewall log that is a single record that represents multiple packets in that direction over time, so… I might, for example, see TCP flagged as sin and ACK, but what I don't know, is that because I'm a server that sent a SYN ACK, or does that mean because I'm a client that sent a SIN, and then later sent an ACK? And so both of those flags show up in my record.
I don't know which end just alone from that. Just… this has to do with the way that the industry has instrumented devices over time, right? But if I have… if I… if I have deep packet inspection, sure, I can know this happened first, then this happened, then this happened. Oh, and by the way, that assumes that the same network device saw both directions of traffic. If you have asymmetric routing, a given device might have only seen one direction.
And then it might not know the other side either. So it, you know, it does… There's a number of scenarios where it gets more challenging, but… and in general, like, depending on the use case, you actually want a distinction of source, destination or client server.
You know, there's a number of, of… conditions of interest you might want to detect, where if you only had client-server, you could not accurately determine them, and if you only had source destination, you also could not accurately determine them, because you just don't have the necessary information. I could go into depth about that, but.
Michele Mancioppi 00:44:50 No, I'm buying the argument in particular in streaming full duplex. I buy it.
So the idea is to actually, have both… Client or server, so something like the… actually, the kind.
As well as the network direction.
on those metrics, I want to guess.
RC Robert Cowart 00:45:11 What is the… what do you mean by the kind in that regard?
Michele Mancioppi 00:45:14 Mankind.
Client server is a sprint kind of thing, is tracing. So my argument was, let's try not to use words that exist somewhere else in OpenTelemetry.
for… Different scenarios, so the client should have been… the client? The word client should be used consistently.
RC Robert Cowart 00:45:32 Agreed, yeah.
Sven Cowart 00:45:33 So, actually, as part of… the follow-up work that I didn't want to open a PR up yet, There was one that, oh, what's his name?
someone within the OV group that created a draft based on some of the work that they're doing and the work that I did in Merman, but in Merman, we propose a new kind, which is source and destination, because what we want to do is model flow data as a network, let's say, think of it as a flow trace, flow span, which then would allow us to distinctly tell you this was the network, this is how things traveled across the network, versus this is how things traveled inside the application, or the server in that case. So I'm with you, I don't want to… overload client-server kinds inside of traces, and what we need is source and destination kinds that… or something else that clearly tells you that it's different.
Michele Mancioppi 00:46:29 I would even… I would even beg you, please don't use the word kind, because people are not gonna… are not gonna constrain to the main, so now it's a spam kind, and this is a flow kind. People are gonna use the word kind and get mighty confused.
Sven Cowart 00:46:43 Yeah, yeah, that's fair, yeah.
Michele Mancioppi 00:46:46 So I would call it, I don't know, flow direction, or network flow direction, or something distinct, so that it's… because people are barely keeping the kind straight. I don't find a normal person, ask them what is the kind producer, see what they tell you.
Sven Cowart 00:47:01 Okay.
Unknown.
RC Robert Cowart 00:47:04 This is going to be fun, because in the context of network devices, flow direction means something different than most people on the endpoint think about. It means… it means whether did I meter this flow ingress, or did I meter this flow egress, is what it… it would mean… flow direction would mean. So… But yeah, at some point, I guess you gotta put a stake in the ground and say, this is what we're saying it is, but yeah.
Michele Mancioppi 00:47:28 Met the other one, yes.
Trask Stalnaker 00:47:34 And, how's the… the networking group? I know you all, like, it's… I think this is a good discussion to have here, kind of, about some of this, But really, it's starting to get, you know, like, it's going to quickly get very deep here, and, we'll need… we'll really need to spin up that networking group.
Sven Cowart 00:48:01 Yeah, so… We met last week on the networking SIG,
Trask Stalnaker 00:48:07 Oh, awesome.
Sven Cowart 00:48:08 We have a few decisions I think we want to make out of that, and I don't know if we want to talk about that here, but it basically came down to, do we want to model it after how the systems working group is right now?
and just have a project board with a set of approvers and maintainers within the semantic convention SIG.
Or does it actually need an entire SIG? That was… Braden was recommending we just model it after how the system SIG operates today.
And, and then he questioned if he should be the right one to lead that, because it's at the limits of his expertise.
And, yeah, it's all in the… in the GitHub issue, the discussion points and summarizations of conversations that have been had.
Trask Stalnaker 00:48:59 So, what do you mean by the difference between a SEMCOM SIG and a full SIG?
Braden, hey, Braden's here.
Sven Cowart 00:49:10 I'm not in the system, Sig, but he… he was saying, oh, hey, he's here.
Braydon Kains (Google) 00:49:16 Yeah, sorry, I joined late.
Sven Cowart 00:49:17 You're good.
Braydon Kains (Google) 00:49:19 What I… what I had in mind there was the… the System SEMCOM group Even though we all sort of end up being involved in implementations and stuff, too, the responsibilities of the group are strictly on the semantic inventions.
I think the distinction that Josh wanted to make, I gather this mostly came from Josh, was that if a semantic conventions group probably isn't sufficient if there are grander plans to make lots of new instrumentation out of them, too. In that case, it would make sense for there to be a full SIG with a proper, like, upstream… I'm mostly thinking about, like, the community project proposal, and exactly how this is presented at a project-wide level, because if it was just in… within the SEMCOF group, it probably wouldn't need All of that, necessarily, but if there is going to be a grander scale to it.
which it sounds like there probably is, then probably we would need a broader project proposal. Based on… based on what I'm hearing, it almost might make sense to spin up a federated SEMConf repo around this, kind of like we did with GenAI.
Because it's going to have quite a scale, and we'd be worried about, like, overloading maintainers, with just, like, constant PRs and, like, prodding for approvals, because there aren't any approvers or maintainers in the group at the moment.
So there being a separate repo would probably be… is a separate discussion that probably would need to be had.
But the… that broader… that initial question of, like, should this be just a… SEMCOM working group or a broader project, that was where my brain was at. Like, is this an effort to make, like, network observability better, and semantic conventions just a part of it, or are we just trying to get the semantic conventions? Like, depending… it's what the group feels we should be responsible for.
Trask Stalnaker 00:51:19 So, a couple of thoughts here. One is the Semantic Convention Working Group, SIGS, Do, go through the, community project proposal still. We do consider them SIGs.
They're just, like, sub-sigs of the semantic invention group, so, like, right, we've got CICD, browser, kubernetes.
Okay. Did we do system? Yeah, we did.
Braydon Kains (Google) 00:51:53 Actually, system may have been here, yeah, I think this was made before I joined, but… Yeah.
Trask Stalnaker 00:51:59 the… so I don't think either way gets you out of that requirement.
Braydon Kains (Google) 00:52:05 We're still doing that, then, that's…
Trask Stalnaker 00:52:07 I think it's a really interesting point about whether it is… so the one example we have of, like, GenAI of semantic conventions and instrumentation.
being together, one SIG together. And I… Do you think that, that is… sounds like a good fit for you all?
Because part of landing semantic conventions, part of a requirement for landing semantic conventions is… instrumentation, and ideally in the OpenTelemetry org.
That we can, Used to validate and develop that.
So, yeah, I think that would be maybe just as… now.
Sorry, I haven't read the latest… Or much of the issue here.
I think I had seen something about 3,000 attributes.
RC Robert Cowart 00:53:22 That would… that would have been my comment, yeah.
Trask Stalnaker 00:53:25 So that is… a little scary, from the core repo, so that definitely makes me think, you know, federated repo under the OpenTelemetry org, similar to the GenAI work.
Sven Cowart 00:53:48 It's a federated repo. I'm not quite understanding.
Trask Stalnaker 00:53:51 Aye.
Yeah.
So, let's start with the terminology.
Yeah.
Did we merge it? No. Oh, because I'm on issues.
This is Josh… So let me drop a couple links into… actually, I'll do it into the doc.
Liudmila Molkova 00:54:25 Can you approve this PR task. Door tip.
Trask Stalnaker 00:54:30 Have I not? Oh, dear.
Yes.
Sorry, folks.
I have not managed our time well.
There is also Lynn Milla's merged PR that is… Useful… But most importantly, this is our first internal federated semantic invention repo. It's basically a way for us to split domains out of this monolith.
Sven Cowart 00:55:12 Is there tooling in place to… kind of pull it all in into the same site, still, that gets published? Yeah. Okay, cool.
Trask Stalnaker 00:55:20 Or there's schema, Yeah, the whole Weaver tool is really… they've done a lot of work in the last year to support these federated semantic conventions.
Sven Cowart 00:55:32 I… I think that makes a lot of sense, because it is our plan to… Contribute the instrumentation piece to the semantic conventions that we want, that we're trying to push forward on.
Some of it's gonna be through OBI, and whatever isn't will be through… other vehicles that we'll need to figure out when that time comes.
Trask Stalnaker 00:55:57 So the one tricky thing I would say with network, is we still have… we can't… we can't move all of the networking stuff out of the core repo.
Or I don't think we would want to. So I think there's some amount of networking that should probably be considered core, and still live in this repo.
Server.address, client.address.
Mmm.
RC Robert Cowart 00:56:27 We also think there are some things that, like… I think we have a good idea what we would recommend here to split, but, like, there are some things that would still be, like, system.
and some things that are clearly, like, on their own network. Like, a routing protocol like VGP is under network, but… TCP metrics for the TCP stack on a server is probably still system, you know, as an example.
Braydon Kains (Google) 00:56:53 And we'd still, like, co-own… the system group would co-own anything that was related to, like, actual host monitoring, which there are a number of network metrics and attributes right now.
And that is… that is okay with us.
Trask Stalnaker 00:57:10 Cool. When are you all, do you all have a weekly meeting set up already?
That you all are chatting about these things, or are you just chatting on the issue at this point?
Sven Cowart 00:57:21 mostly chatting on the issue. We need to find a new time. We were gonna take over that Network SIG meeting.
And meet there, but it doesn't work for Braden, so I think we need to find a new time that works.
Braydon Kains (Google) 00:57:33 But I am also okay with, if you guys need to keep that meeting. I think my… the extent of my involvement will probably be I can help you guys open up a project, and then hopefully hand it off to you, and then in that case, you don't need to move… move that meeting.
RC Robert Cowart 00:57:49 volunteered to do what's necessary, if so, delete it, but, you know, I'll just need some coaching along the way at some point, because, you know, I'm still a bit of a noob at all this, so…
Braydon Kains (Google) 00:58:00 I'm happy to help you guys get the project proposal up. I think modeling after what the GenAI proposal was makes a lot of sense.
So maybe I can… help guide with what that proposal should look like. And we'll also need to get, TC and GC Approval, and, well, specific liaisons for the group.
Trask Stalnaker 00:58:22 Yeah.
Braydon Kains (Google) 00:58:23 Sponsors, so… I can help navigate that, since I know many TC and GC members personally, so I can hopefully help find proper ownership for that.
So yeah, we can chat either in the hotel network Slack channel, or you can DM me. We can figure it out.
Liudmila Molkova 00:58:43 And I think one of the important things are to have somebody familiar with semantic conventions and the process consistently joining those discussions. So, Braden, it would be nice if you could actually make it and be.
Braydon Kains (Google) 00:58:59 engineer.
Liudmila Molkova 00:59:00 Otherwise, getting approvals from semantic conventions maintainers might be tricky.
Braydon Kains (Google) 00:59:06 Right, well then maybe we should reschedule, unless someone else wanted to take my place, either way, but… Yeah, unfortunately, at Eastern Time, that time slot is no good for me, so…
Trask Stalnaker 00:59:20 And… I ran us out of time.
Thank you all. Yeah, Thanks for the update on the networking stuff, that's very helpful.
And Serbia and Lytmila, sorry, Cool, awesome, look forward to it.
Liudmila Molkova 00:59:43 I'll probably create a tracking issue.
But we can't talk about it, it's not urgent.
Sven Cowart 00:59:50 Hey, Lude and Mela, if you just have one more minute, did you mean, like, bringing back what we discussed in the networking group into this SIG?
Liudmila Molkova 00:59:59 I meant that when you, have your discussions in the networking group, it would be nice to have somebody I think it's important, it's essential to have somebody who is working on semantic conventions, not just in networking, but has experience with it.
So that, it's just, we would produce something coherent with the rest of open telemetry.
Sven Cowart 01:00:22 Yeah, yeah, yeah, that makes sense.
Trask Stalnaker 01:00:23 There's just… there's so much history baked into the semantic conventions that, you know, we try to document stuff, but a lot of it's not, and so yeah, having people who've been through the process and been involved Before is critical.
Liudmila Molkova 01:00:40 Yeah, thank you all.
Sven Cowart 01:00:42 Bye.
Trask Stalnaker 01:00:43 Right?
Braydon Kains (Google) 01:00:43 Thanks, everyone.
Armin (Dynatrace) 01:00:44 Popeye?
