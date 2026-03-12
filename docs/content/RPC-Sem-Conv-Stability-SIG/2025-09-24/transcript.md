SIG: RPC Sem Conv Stability SIG
Date: 2025-09-24
Duration: 53 minutes
Zoom Recording URL: https://zoom.us/rec/share/OkHRI7MGKFB4JA5YEbnIJIzBfPUdfwocmQLOjeAKRKEEuNnnyHfuKoIVTLAFGPCg.hZkA1KXAVWa-ZY9M
============================================================

## Zoom Recording Transcript

**Liudmila Molkova** 01:56 Hello, hi everybody.
**Steve Rao** 02:14 Okay, let's…
**Liudmila Molkova** 02:16 Hello!
Let's give Trask a minute to join, let me ping him, and we'll get started.
Oh, here he is.
Hello!
Okay.
So, please add your name to the agenda, if you have anything… Let's add your name to the attendees list. If you want to bring anything up, please add it to the agenda.
One thing that we rarely did up on telemetry, and I've heard concerns that we don't Have the place for new people to introduce themselves.
So, maybe we can spend 5 minutes if, anybody wants to say hi.
how you… what… what he brings… what brings you here? It would be wonderful.
Otherwise, let's get going.
Okay.
So, let's… Darth was the project board?
We don't have anything new there. I think we have a bunch of things in progress, and maybe we can spend some time Reviewing things, and… Discussing any open questions?
I think there are a couple of peers… that are… Pretty close.
There is this one from James, which adds… attributes, which adds attributes to metrics. We didn't have any attributes on metrics.
So, if I look here, we now have attribute table everywhere, everywhere.
And the attributes are the same.
I think the notable change that I pushed for it. There is some confusing language.
In the free… there was some confusing language in the free form markdown.
Where we explain the RPC service is not the same as service name.
And I propose to remove it.
**Matthew Hensley / Grafana Labs** 06:02 Yeah, that makes sense to remove me.
**Liudmila Molkova** 06:14 Okay.
So then, James, do you want to call out anything else on this PR?
**James Thompson** 06:22 No. I… I can't think of anything.
**Liudmila Molkova** 06:29 Okay.
So, Dan…
**James Thompson** 06:31 Just check the description, because I can't remember… one of them we did remove an attribute from.
I can't remember if it was this PR or the other one. We moved… removed network.transport.
if you have a look at the description, I mentioned which one I removed it from, as we discussed.
**Liudmila Molkova** 06:58 metric type.
**James Thompson** 06:59 Yep.
Yeah.
So those are the only change… notable changes.
**Liudmila Molkova** 07:09 Right, so we used to have network… hype.
And we… Don't… Yes, we did. We used to have network type.
**James Thompson** 07:22 Yes.
**Liudmila Molkova** 07:22 It does not seem to be super useful, and we don't have network type on HTTP spans.
We have protocol name, protocol version, runs… Word… I think, and that's… Probably enough to… Figure out the network type.
I remember back in the HTTP days, we decided not to add network type because Can be added later.
But it's essentially IPv4 or IPv6.
Okay, so then it sounds like, Do we need to continue reviewing the doff line?
I, So, the other one is… I think we can be merged, the JSON RPC?
I have two approvals… There are no open discussions.
So I'm going to merge it, unless somebody wants to take a final look.
**Trask Stalnaker** 08:58 Urgent.
**Liudmila Molkova** 09:10 Okay.
James, did he edit it?
**James Thompson** 09:20 Yeah, I added those ones. Like, we've previously spoken about them.
Right, but we never got around to moving… updating the status on the board of those issues.
Technically, that shouldn't probably now be done, because PR just got merged.
**Liudmila Molkova** 09:57 would at least our PC method as recommended?
**James Thompson** 10:02 So that was the one we discussed where the generic page for JSON RPC said it was required.
But you… Yeah.
See if you have a look at the changes.
**Liudmila Molkova** 10:23 It's still required.
**James Thompson** 10:25 Yep, alright, but the problem was before, it was just on a general page, so technically it also applied to metrics.
And, yeah, there was an issue with the logic there.
**Liudmila Molkova** 10:36 Essentially, I remember that the resolution for this one is to make it not required.
**James Thompson** 10:43 Hmm… Bye.
I'm just trying… Yeah. Can you scroll down? Because I can't remember Wolv's last comments on that.
Hmm.
**Liudmila Molkova** 11:07 Either way, if it's not always available, it cannot be required on spans or metrics.
**James Thompson** 11:15 Yeah, no, so, so we… yeah.
I'll reread it, but I'm pretty sure that one should be done.
I'll check and comment on it.
**Trask Stalnaker** 11:25 So in the, in the… PR that we just clicked merge on… RPC method… Is listed as…
**Liudmila Molkova** 11:42 required.
**Trask Stalnaker** 11:43 Excuse me.
They're only for JSON RPC, right?
**Liudmila Molkova** 11:48 I got a little messy with this pad.
**Trask Stalnaker** 11:50 And the other… on the general one, it looked.
**Liudmila Molkova** 11:52 I'll make myself look like a number. It's recommended.
**Trask Stalnaker** 12:00 Here, I'll pull up the, the Markdown view, because…
**Liudmila Molkova** 12:05 Like I said last time, that's the only way I connect.
**Trask Stalnaker** 12:08 Sweet.
Confirm… Symmetric.
So, on the metrics, it is… Recommended.
And let's see on the spans…
**James Thompson** 12:32 And the old page said it was…
**Trask Stalnaker** 12:35 Recommended.
So it's only marked required now on… JSON RPC metrics.
**James Thompson** 12:46 Yep.
**Trask Stalnaker** 12:48 Is that… Oh, but this is… this is saying that they don't want it to be required on JSON RPC metric.
JSON or PC.
**Liudmila Molkova** 12:58 Spans or metrics.
So we still need to change the RPC method to be probably conditionally required when available.
for… all metrics, and… Json RPC Span.
**James Thompson** 13:21 I'll re… let's discuss it next week, I need to re-read it then.
**Trask Stalnaker** 13:27 Okay.
Sounds good.
But we should probably unbook it, so it won't close.
Oh, well… I'll try to do that.
You beat me to it.
**Liudmila Molkova** 13:57 Oh, sorry.
Let's see if it closes it.
**Trask Stalnaker** 14:04 Yeah.
I think it shouldn't. I think we… I think… I think we are in time.
Oh!
**Liudmila Molkova** 14:14 I never…
**Trask Stalnaker** 14:15 The merge queue already kicked us out.
Removed it.
Oh, looks like there's some merge conflict-y problems.
Because the merge queue has a bunch of failures.
**Liudmila Molkova** 14:30 Oh, the change.
**Trask Stalnaker** 14:32 No, no, no, scroll down.
Go to View Details on the merge… where it says the merge queue removed this pull request, above… yeah, right there, below your mouse, to the right of your mouse, yeah!
**Liudmila Molkova** 14:48 Well, let me check.
**Trask Stalnaker** 14:49 And a bunch of other things.
**Liudmila Molkova** 14:52 Right.
**Trask Stalnaker** 14:54 Oh, authorization, authentication.
**Liudmila Molkova** 14:57 Oh, Doctor Hub is down!
The world is ending.
**Trask Stalnaker** 15:03 Oh, fantastic.
Alright, so we'll try to merge that later.
**Liudmila Molkova** 15:13 Yeah.
Okay, moving on to the next one… Right, so this one just adds network protocol name version to everything RPC.
And there is a pull request for it?
**James Thompson** 15:37 There is a pull request, and there's a question… Right? About a couple of metrics.
Right?
Is… should we add it there?
Just for completeness, or should we not?
**Liudmila Molkova** 15:52 I think there are two points. First one, we should not merge this PR, because it puts things in the right state. We should only merge it after your other PR.
**James Thompson** 16:03 Correct.
Alright? But we also… Question of, does it go on every single metric?
Alright, so… Right? Because there was a couple of metrics.
Where, yeah, yeah.
We, we touched on it last week.
Right? Does it make… do those metrics even make sense?
**Liudmila Molkova** 16:31 So let's deprecate them, and then we will not need to update them. We can also deprecate them before any changes are made.
**James Thompson** 16:39 Yeah.
Yeah.
So…
**Trask Stalnaker** 16:42 My recommendation, I think last week was to put these two attributes just on the general Not to list them on each one, just to keep them in the common.
And we'll just assume that we have… they apply everywhere. And yeah, those two metrics are a little odd. I agree.
**James Thompson** 17:06 Yeah, but… because the closest equivalent I could find in HTTP did not have them.
So… That's why I was wondering, should we have them on the RPC equivalent or not?
**Trask Stalnaker** 17:19 But that was for a different reason. That was the active… Which I don't think are similar.
the active requests, I don't think, are similar.
**Liudmila Molkova** 17:41 It seems uncontroversial not to add them to this metrics, anyway.
And then we'll deprecate this. Damn.
**James Thompson** 17:49 Nope.
**Trask Stalnaker** 17:50 Oh, did I open this last week? Hey!
**Liudmila Molkova** 17:52 Yay!
Yay!
**James Thompson** 18:23 You just only add it to the duration metric.
**Liudmila Molkova** 18:29 Sorry?
**James Thompson** 18:31 Let's.
**Liudmila Molkova** 18:31 Can you repeat?
**James Thompson** 18:32 So, you just wrote, let's add network protagon to the duration metric. It's already on the duration metrics.
Alright, based on the PR I have.
**Liudmila Molkova** 18:45 So…
**James Thompson** 18:48 Right, so the PR I have adds it to them all, except for those ones that we want to discuss, whether we deprecate them.
**Trask Stalnaker** 18:57 So, like, it's okay to add them, yeah, to the RPC server request size, response size…
**James Thompson** 19:04 Yep.
Yeah, so that's all done as part of the PR, but the question is, do we also add it to those ones that we want to deprecate?
**Trask Stalnaker** 19:14 My point is, add it to the common section.
is what I would… was proposing, as opposed to the way that the PR is laid out right now, which is adding it to each metric individually.
**James Thompson** 19:31 If we need to split them out later, we can.
**Liudmila Molkova** 19:38 Let's do the following. Maybe before we merge the PR that adds attributes to all metrics.
I can send a PR later today to deprecate this too, and we will never touch them again.
**James Thompson** 19:53 Or I can do it later today as well.
If that makes it easier.
**Liudmila Molkova** 19:58 Go for it.
**Trask Stalnaker** 20:00 then Lydmil and I can approve. We have two approvals, and we can merge it.
**James Thompson** 20:05 Yep.
**Liudmila Molkova** 20:22 So it seems I cannot assign you, James.
**James Thompson** 20:24 I have others assigned to me.
Trask was able to sign me the other week.
**Liudmila Molkova** 20:33 Oh, sorry.
**Trask Stalnaker** 20:37 per cake.
**James Thompson** 20:41 No, you're missing a H.
**Liudmila Molkova** 20:46 Anyway, you, you can.
**James Thompson** 20:48 Yep.
**Liudmila Molkova** 20:48 Take it over.
**Trask Stalnaker** 20:49 I'll… I'll find it.
I'll try.
**Liudmila Molkova** 21:01 Okay.
Oh, I've lost our project board… Okay, and this is the… A bigger one.
**James Thompson** 21:27 Yep.
And once the JSON RPC is merged in, the other ones will be undrafted and rebased.
**Liudmila Molkova** 21:41 You mean for the rest of them? Okay.
**James Thompson** 21:43 Yep, yep, for gRPC and ConnectRPC, the document's already done, the markdown's ready, it just needs a rebase to bring in the common group.
**Trask Stalnaker** 21:53 Oh, right. You were waiting for the RPC one to get… I mean, the JSON RPC to get merged for that.
**James Thompson** 21:59 work.
Yep.
**Liudmila Molkova** 22:04 Okay, is there something you want to discuss on any of them, or it's straightforward?
**James Thompson** 22:08 It was straightforward.
Right, because it's using the same groups as what we had for JSON RPC.
Alright, it's using the same common group.
Yeah.
**Liudmila Molkova** 22:22 Okay, sounds good.
**Trask Stalnaker** 22:33 Yeah, I can't assign that issue to James.
either… and it's weird, there's a… I'm trying a couple other people in the org, and… It's, like, hit and miss. People I know who I should be able to assign are not.
I'll… I'll figure it out, and or wait for GitHub to work again.
**Liudmila Molkova** 22:56 Yeah, if Docker is done, then maybe GitHub is done as well.
It's a question of time until everything is done.
Okay, let's take a look at the project board again.
We probably, yeah, want to move some of it.
It's in progress… This is… not in progress.
**Trask Stalnaker** 23:28 Oh, I think you have to comment on it, James. I think it's… Must be only… I think I can only assign people who have right access to the repo, unless they have commented on the issue, and then I can assign you.
Always forget that.
So confusing.
**Liudmila Molkova** 23:58 Yes.
Okay.
So, do we want to discuss something that's intuitive?
**Trask Stalnaker** 24:11 Have we… are all the… did we cover… All the in-progress… Bingo.
PR.
**Liudmila Molkova** 24:21 Right.
**Trask Stalnaker** 24:21 Yes, fantastic.
Yeah, let's.
**Liudmila Molkova** 24:31 Yeah, so this one.
**Trask Stalnaker** 24:37 I was supposed to do that.
**Liudmila Molkova** 24:41 Who were, but, I don't know if… We would have quite a few conflicts, but it's essentially… whatever we do, we'll have quite a few conflicts.
**Trask Stalnaker** 24:55 Yeah, although if we don't do it on the subpages, that will be… better, which… I don't think, We did.
Or… database, at least.
**Liudmila Molkova** 25:11 Alright.
**Trask Stalnaker** 25:12 So I think we can just add it to the… Top-level README…
**Liudmila Molkova** 25:18 Okay, yeah.
**Trask Stalnaker** 25:23 Did we do database spans, Markdown?
Yeah, we did, and probably metrics, so the general… We did it on the general… Right. …on the README.
**Liudmila Molkova** 25:36 Right.
Okay.
So then there will be no conflict. It should be straightforward.
**Trask Stalnaker** 25:46 Yeah…
**Liudmila Molkova** 25:49 Okay.
So this one, I wanted to take it over, so maybe what I'll do… Once the JSON RPC is in, I can update JSON RPC.
And… Or… or I will just wait for the rest of the… System-specific pages to be updated.
**James Thompson** 26:29 I think we… I think the first thing to discuss is what do we… is it a system? Is it a protocol? Is it a framework? What's… These sub-name space we want to go with to describe describe it. I think that's key.
**Liudmila Molkova** 26:47 Yeah, I would vote for protocol.
But we can always bike shed under naming.
**James Thompson** 26:54 Yeah.
Because, for me, I almost… think, framework, because the protocol could be used to more describe the transport, so if you look at something like ConnectRPC, it works over gRPC, HTTP, and ConnectRPC.
Right, so you have the three options there.
**Liudmila Molkova** 27:19 Yeah, I like the framework. It confirms our… thinking of this… on the scope, right? We essentially want to tackle frameworks.
**James Thompson** 27:31 Yeah.
**Trask Stalnaker** 27:35 And is that, significantly indifferent enough from system.
I guess system is, like… We're using system for databases, anything else?
**Liudmila Molkova** 27:50 Message, messaging.
**Trask Stalnaker** 27:52 Okay.
**James Thompson** 27:53 But I think the difference…
**Trask Stalnaker** 27:54 External systems, yeah.
**James Thompson** 27:57 Yeah, those are systems where you usually deploy a product that's running The database service server you need for the system, the messaging server.
Whereas RPC, you look after both ends of the communication.
**Trask Stalnaker** 28:13 Although it gets a little… complicated with, messaging where you have, like, Kafka framework talking to Azure, Service Bus.
System.
Right? So, like, system… ideally, the name system seems to reference that it's the system you're talking to.
almost… kind of wish maybe we had done messaging framework, or I don't know.
It's… confusing. Same for database, I mean, I guess, because… JDBC, although usually we're able to reach into, like.
The connection string and try to pull out what database we're actually talking to.
And maybe we could do that for messaging.
2.
Yeah. There might be ways.
But I… I… I think I agree.
I like framework, also.
**Liudmila Molkova** 29:33 Okay, let's start with framework. If, if… If there are any complaints, we will… Updates on the PR.
I write it here.
Small problem with it.
It's… it's too close to the client vibrating.
It's like, it could be confusing that people would try to put Their… their client library instead of the… technology you're handed.
**Trask Stalnaker** 30:35 Are there multiple frameworks that do connect like, or JSON RPC…
**Liudmila Molkova** 30:44 multiple libraries?
**Trask Stalnaker** 30:48 Yeah, like, is JSON RPC a framework?
**James Thompson** 30:53 You can do JSON RPC… Right, over… standard I.O.
Alright? Because I'm just thinking about how… how do we capture, or even if we look at Dubbo.
Right? You have the double, and then you have all your different protocols it works over.
**Liudmila Molkova** 31:24 Oh, this is a framework.
It's just terminology, right? It doesn't mean… I'm just curious, should your.
**Trask Stalnaker** 31:32 I mean, Double is a… I mean, Double is a library.
It's a framework that you use, and… It could emit, potentially, multiple different RPC protocol, or protocols, like, it could emit gRPC, or maybe JSON RPC.
**Steve Rao** 31:58 Yeah.
**Liudmila Molkova** 32:08 Anyway…
**Matthew Hensley / Grafana Labs** 32:10 This might be one of them where it's good to, you know.
mock up what the different attributes would look like side by side, to see how confusing they are. To your point, Mela, with, like, the client library name being too similar to framework.
It's a concern. Might be a little bit easier if we could actually look at them and see, does it make sense versus speaking theoretically.
Coming up with some common examples for… Some of the popular, options we need to consider.
**Liudmila Molkova** 32:42 We have them, right? We… that's the Edom that we have, or is it?
Apache double, connector PC.NETWCF.
**Trask Stalnaker** 32:56 JRPC.
Steve, should… is Apache Doubo… Is this… does this list make sense, I guess, from the Apache Double perspective, like, You can emit… GRPC… from Apache Devo, is that correct?
Is that one of the options, or is Apache Dubbo Like, have its own sort of wire protocol that's… Different.
**Steve Rao** 33:29 Yeah, yes.
Yeah.
**Trask Stalnaker** 33:35 It has its own wire protocol.
**Steve Rao** 33:37 Yeah.
**Trask Stalnaker** 33:38 Okay, thanks.
**James Thompson** 33:40 But doesn't Apache Dabo have multiple that you can choose from?
**Steve Rao** 33:46 Yes.
**James Thompson** 33:47 Yeah, so you can choose from multiple.
I think it's under concepts and Architecture, from memory.
**Trask Stalnaker** 33:56 So one of… but one of them is, like, a NATA, like, the… a NATA VW… Communication, our protocol, but it can also talk over others.
**James Thompson** 34:12 There's a communication protocol.
Yeah, I think that's…
**Trask Stalnaker** 34:18 Yeah, yeah, yeah. There we go.
**James Thompson** 34:21 Yep.
So, HTTP, REST, gRPC, JSON RPC, Thrift, HSN2, etc.
**Matthew Hensley / Grafana Labs** 34:34 WCF and… Core WCF, or similar.
That can talk over all kinds of… Different mechanisms.
**Liudmila Molkova** 34:44 Json RPC can also work on top of pretty much anything.
**James Thompson** 34:50 Yeah, and so can ConnectRPC.
**Liudmila Molkova** 34:55 But also, they're called protocols.
**James Thompson** 34:58 Yeah.
**Liudmila Molkova** 34:59 and frameworks.
**James Thompson** 35:01 Yeah.
**Trask Stalnaker** 35:05 So what do we want to… I guess the question is, what do we want to capture here?
Do we want… I mean, I… I… I think we want to capture the protocol, If possible?
as opposed to, like, so if Dubbo is talking gRPC, I think we want to capture gRPC as this protocol.
**James Thompson** 35:38 For me, I think we almost want to capture both the framework and the protocol.
**Trask Stalnaker** 35:48 Well, we're capturing the framework via, the library instrumentation scope name.
I mean, not… not in a struct, maybe in a enum… way, which could… be a consideration. But it is… it is captured.
Yeah, the instrumentation scope name.
**James Thompson** 36:21 Meh.
**Liudmila Molkova** 36:25 So I'm thinking that the interesting parts start around streaming.
If, let's say, Dabo… Applies some… something meaningful on top of gRPC stream, then it's interesting to capture Something meaningful and not the message back and forth.
**Trask Stalnaker** 37:02 But it would still be nice to… stick gRPC in there somewhere.
Even if it's streaming, to know that it was done, doubly used the gRPC.
Protocol.
**Liudmila Molkova** 37:21 Oh, I thought…
**Trask Stalnaker** 37:23 No, go ahead.
**Liudmila Molkova** 37:24 I thought… He was thinking about the duplication.
So there is the duplicate… there is the gRPC instrumentation, and there is double instrumentation. If double works on top of gRPC, there is some duplication, or there are different layers.
**Trask Stalnaker** 37:42 No, sorry, I was thinking more about, say, native double instrumentation, but… may or may not be using gRPC, actually, library.
They may just be talking gRPC, kind of like we do in the, OpenTelemetry Java Exporter.
And so… What would we want the double instrumentation to… emit as far as what Frodo, like, do we want to… Is it… Important to… more important… What's the most important bit? Is it that it's gRPC, that it's talking gRPC?
Or that it is the Dubbo framework.
**Liudmila Molkova** 38:43 I see. What if we had some double-specific attributes? Would we report them? And, our PC system would be… gRPC?
I mean, it could be.
**Trask Stalnaker** 39:05 Yeah, I mean, I'm not sure you potentially, like, debo… I mean, you do have the instrumentation scope name, if you… want to know that it's Dubbo.
**Liudmila Molkova** 39:22 But it's language-specific, right?
**Trask Stalnaker** 39:27 Right. But is that… is that important that it's Dubbo?
Or I guess, how important is it that it's devoted? Is that something that… you… want to model…
**Liudmila Molkova** 39:51 It might be important if, let's say, we have a special flavor for Wow.
So normally what we do, right?
The value of the system thing tells what telemetry format should be.
Right. Here, it would not, and it… It's probably not a big problem.
**Trask Stalnaker** 40:26 Maybe, though, like, if it's talking gRPC, wouldn't we expect gRPC status codes?
**James Thompson** 40:35 Actually, I don't know.
**Trask Stalnaker** 40:37 I think… We would… I guess maybe that's a question, Steve, for you, if you… Don't know if you could… Find out, like… the… when Dubbo is talking GRPC, I'm assuming it would expect, because, right, that would be potentially interop, like, you could use Dubbo on the client side to talk gRPC to a service that wasn't Dubbo, but using gRPC, is that…
**Steve Rao** 41:17 Yeah, it's, yeah, I can introduce about this, this, question from Dabo. Yeah, Dabo, yeah, we, We, we defined that is a framework.
And, it supports, multiple, a communication protocol, such as gRPC and something like that, and in double framework, it helps users to, build, RBC application easily.
And, except for, protocol, RBC protocol, is also contained.
consistent some other part. You also need to build a RPC application.
So, yeah, maybe from, double sides, the scope of, this framework is not, owning, means, RPC protocol. Yeah, RPC protocol is just a part of this framework.
**Liudmila Molkova** 42:33 I'm curious, what… what does the layer on top of gRPC does? Is it just convenience API? Does it do something special?
Would you be interested in significantly different telemetry? Do you… Have any thoughts on this?
**Steve Rao** 42:50 Yeah, maybe I need to familiarize about the background later, and yeah, maybe I can leave comments with my colleague from Double Site.
**Liudmila Molkova** 43:03 That would be great, thank you.
Okay.
So we have just 3 more minutes, It would be interesting to unders… and… If we would use the underline verbatical.
**Trask Stalnaker** 43:35 I think my vote has flipped back to RPC protocol.
But… If it's something…
**Liudmila Molkova** 43:46 That, because it's…
**Trask Stalnaker** 43:48 The protocol has to be… communi- like, be the same on both sides of client and server, like, that is the protocol that's being discussed, like, whereas when you start the term framework, start to think of, like, Matt, you were mentioning the .NET, RPC frameworks, which can all, like, Tuck different protocols, and… For correlating client and server telemetry, like, that is… I would kind of… I would expect those to be the same.
**Liudmila Molkova** 44:27 Yeah, that's a great point.
Okay, so then, I can try modeling it with the RPC… protocol.
And removing the constants that are the dump it.
**Trask Stalnaker** 44:53 It looked like there was a… it looked like there might be a double protocol, also.
**Liudmila Molkova** 45:03 Okay.
**Trask Stalnaker** 45:03 the choices.
**James Thompson** 45:06 What would we do for JSON RPC?
In that case.
Because JSON RPC… can be a HTTP, standard I.O, Alright.
**Liudmila Molkova** 45:20 JSON RPC is a protocol. You have to use it on both sides, it's not a framework.
**Trask Stalnaker** 45:36 That makes sense to me. I mean, as a litmus test.
**James Thompson** 45:43 But… but what happens if you then do connect RPC?
Right?
Right. Which can operate over gRPC, HTTP.
**Trask Stalnaker** 45:56 That would be a framework, Ben.
And not one of the protocol.
**James Thompson** 46:08 But it's also a protocol. It could… it has its own protocol, alright?
Yeah.
**Trask Stalnaker** 46:15 So if it has its own native protocol in addition to being able to talk other protocols, then, I mean, we can define, kind of like Dubbo as A native protocol also, in addition to being able to do other protocols, so that… that's okay.
we would just expect the Connect RPC framework instrumentation to Emit the protocol version that it is using.
Does that make sense?
Thanks, James.
**James Thompson** 47:11 Yeah, I'm trying to wrap my head around it.
Alright.
Yeah.
**Trask Stalnaker** 47:20 Might be a good place to stop and… We can all wrap our heads around it.
**Liudmila Molkova** 47:28 Yeah, I'll try to do some research by the next week.
**Trask Stalnaker** 47:33 Cool.
**Liudmila Molkova** 47:34 Cool, thank you all. See you around.
**Trask Stalnaker** 47:37 Thanks.
**Matthew Hensley / Grafana Labs** 47:38 Thank you.
**Trask Stalnaker** 47:39 Bye.
**Steve Rao** 47:40 Bye.
Hmm?
