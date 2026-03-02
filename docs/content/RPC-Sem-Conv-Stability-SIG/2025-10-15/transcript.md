SIG: RPC Sem Conv Stability SIG
Date: 2025-10-15
Duration: 49 minutes
Zoom Recording URL: https://zoom.us/rec/share/MMivMEFqcxbA8BI2A5hJQ77uJZIr55l4Q75AKLVMao6I-wZNhrTN5J7umLWptaJt.RVx4F2XjIuvvu-Ge
============================================================

## Zoom Recording Transcript

**Trask Stalnaker** 01:51 No, it's Andrew's note-taker again.
Not taking the hint.
Hey, folks.
**Steve Rao** 02:05 Oh.
**Liudmila Molkova** 03:09 Hi, folks!
**Trask Stalnaker** 03:11 Hey, Lamila.
It just got done.
Kicking out our bot friend.
Which consumes 2 minutes of every meeting.
I guess I could leave it, but… annoys me, so…
Alright, let's see what we got here… nothing… alright.
So, clean slate… Odd 7…
Same… True…
Project board.
There was an agenda.
Alright.
So we can take care of those…
So, request hedging…
**Liudmila Molkova** 04:57 So this one…
This is about errors.
And cancellations. And we have a different issue on this, which is on the board.
**James Thompson** 05:21 Yeah, there's effectively two issues talking about cancellation, hedging.
**Trask Stalnaker** 05:27 Oh, do we have… let's see…
**Liudmila Molkova** 05:32 It's, it's linked to that issue, but yeah.
**Trask Stalnaker** 05:38 Oh, this is the general issue for canceled.
**Liudmila Molkova** 05:44 Yeah, I think so.
Maybe we should close one of them as a duplicate?
**Trask Stalnaker** 06:02 I should cancel it.
Yeah… We should… There was some good context here.
Alright, error type 2… Spain's RPC… okay, so we are… In progress…
And… this one… BC…
**Liudmila Molkova** 07:40 Do we… should it be in progress?
**Trask Stalnaker** 07:44 That should be to-do.
Oh, sorry, did I… I thought I was on a PR, my bad.
So… So is it a to-do, or is it a post-stability?
**Liudmila Molkova** 07:59 Yeah, I would rather… Do it… do it as a possibility.
**Trask Stalnaker** 08:07 Yeah, I don't think we were planning… to tackle WCF.
Well, there's a lot of discussion, though.
**James Thompson** 08:22 Yeah, the discussion is about the convention for how to capture the namespace of the header.
**Trask Stalnaker** 08:32 very specific to WCF.
**James Thompson** 08:37 I think so, because you've got the XML namespaces.
Alright, so you can't just use the…
Key of the header, because you might have the same key for different namespaces in the header.
**Matthew Hensley / Grafana Labs** 08:54 Been a while since I've done anything with soap.
I'm pretty sure it also can't apply to Java.
But, like I said, it's been over a decade, but there's Java.NET SOAP interop things, and specifically namespaces.
Big, big issue there.
**Liudmila Molkova** 09:18 Do… how much do we care about something that's decade-old in semantic conventions?
I… I could rather… not have it.
**Matthew Hensley / Grafana Labs** 09:29 I think it's fine to…
leave. I wouldn't… it's not really a concern right now for what we're trying to get done, but…
I mean, I've worked on soap… instrumenting soap stuff with WCF in this year, so… Unfortunately.
**Liudmila Molkova** 09:46 Mmm.
**Trask Stalnaker** 09:48 Yeah, I think we just need to define the scope of the stability effort.
And we had done that for databases. We had an issue where we had basically, like, decided on…
I see Google, Postgres, the ones that we… Yes.
So I think we just need… An issue like this.
Or… RPC…
**Matthew Hensley / Grafana Labs** 10:31 Yeah, I definitely agree, and it'd be great if someone who actually has these issues still
And is aware of, like, the intricacies of them, could weigh in in the future, so…
I'll go try to find that one, might leave a comment on it to that effect.
Comes across it.
**Trask Stalnaker** 10:49 We haven't renamed it yet, but I think we agreed on RPC protocol name?
No, we haven't accrued.
**Liudmila Molkova** 11:02 Okay. Anyway, yeah.
We'll understand, I hope.
**Trask Stalnaker** 11:06 Yeah.
It says for initial RP to see some constability…
Alright, so this is… oh, it was at the top of the list…
Huh? Yes.
Tight.
RPC…
Let's see… to-do… So… initial proposal… GRPC…
Double… But weren't we saying Dubbo wasn't a protocol, though?
I think it's both. Is that correct, Steve?
**Steve Rao** 12:19 Yes.
**James Thompson** 12:21 But the protocol for Dubo is actually not…
Dubbo's… isn't that the old protocol, and there's a new protocol used instead? There's two… Dabo Protocols.
**Steve Rao** 12:36 Yeah, there are two, protocols, one called a double protocol, another called a triple protocol.
**Trask Stalnaker** 12:47 What's the other one called?
**Steve Rao** 12:49 Triple. Triple.
**Trask Stalnaker** 12:52 Like that.
**Steve Rao** 12:52 G-R-I-P-P-L-E.
**Trask Stalnaker** 12:55 Triple, got it.
A PL department.
**Steve Rao** 13:00 Yes. Just, just one, just one P.
**Trask Stalnaker** 13:03 P-I-P-L-E, so, yeah.
Oh, yes, I can spell.
If you had to pick one of these that was a priority for the double… Maintainer, Dubbo community?
Which, of course, as stabilizing semantic conventions, Which one would you pick?
**Steve Rao** 13:28 Yeah, I can discuss with them, maybe they, prefer the later, yeah, because this is a support in, CCO.
Okay.
**Liudmila Molkova** 13:41 Would it be the protocol-level instrumentation, or the framework-level instrumentation? And on the framework level, would
Would it be important?
Like, if I'm a user.
like, if I use Java, double… library. Do… do I…
care? Like, do I see it immediately, if it's the…
triple or double protocol or gRPC underneath.
**Steve Rao** 14:21 Yeah, maybe I want to correct, one point, yeah, in, double,
In double, if a user want to use the gRPC to send a request to a gRPC server.
they must use the triple protocol to support this feature.
So, without a gRPC, protocol.
In, in double client.
**Liudmila Molkova** 14:55 Yeah, I'm… I guess my… my question is.
What instrumentation would apply to? Does it apply to the… API?
Or does it apply to a specific protocol? Is it important distinction for the instrumentation?
**Steve Rao** 15:15 Yeah, sorry, I'm not very clear about your question. Can you explain more?
**Liudmila Molkova** 15:24 So when I'm using Apache Dabo as a framework, like, right as
Does it prevent different APIs for different protocols, or it's the same API?
**Steve Rao** 15:36 same API, but they can set the protocol.
**Liudmila Molkova** 15:42 Yeah, and let's say when I have a span that's an RPC call, Would it describe the…
API call, or the underlying protocol call?
**Steve Rao** 16:03 Yeah, sorry, I'm not very clear about your, concept, API call or protocol call. Yeah, can you…
Give an example.
**Liudmila Molkova** 16:14 Okay, go ahead.
**Trask Stalnaker** 16:16 Would you capture, the method call that the user is making to double, like…
Hey, Dubbo, send this payload to the remote server.
Would… In the instrumentation, do you capture that, sort of, at the…
Double the logical layer, the double… Method that's being called.
**Steve Rao** 16:43 Hmm.
**Trask Stalnaker** 16:44 Or do you capture it?
Lower down in the stack at the wire, more like the wire protocol.
layer.
**Steve Rao** 16:56 Yeah, maybe I, I, I think it's a double method.
Yeah, in Java instrumentation.
**Trask Stalnaker** 17:09 could you, like, for GRPC, there are certain attributes.
like, Well, I guess RPC method, RPC service.
Are the… would you capture these, I guess You're calling a gRPC service.
And you… it would be nice if the RPC method on the client side matches the RPC method on the server side.
Is that the case, or…
Is the GRPC kind of binding could be to some…
different, like, when you're setting up that binding, the config… when you're configuring Dubbo, you're telling it…
This method… when I call this method, it's really this RPC endpoint, and here's the… Service name, etc.
**Steve Rao** 18:37 You, you mean,
Yeah,
Yeah, sorry, I'm not very clear about your question. Yeah, can you, yeah, leave a comment? Yeah, maybe I can…
**Trask Stalnaker** 19:09 Sure, sure, we can come back, to that.
But it does… I mean, Ludmila, I mean, we can discuss kind of separately What?
What is our goal? What do we want to capture?
Do we want to capture it? Because I was… I…
An impression or kind of preference for… capturing…
It at a little bit more the protocol layer.
Since that… matches what we do for our HTTP, it…
Which is maybe not so important.
it allows that correlation, like, you have gRPC call on one side, you have gRPC call on the other.
Would be nice.
Now, feasibility-wise, if… I mean, if that…
That could always be a fallback case if that's not feasible to capture the…
protocol piece, like, say, in Dubbo, maybe they capture… they can't capture that.
At this point.
But that would be okay.
But what would be ideal, I guess, is what we need to decide.
**Liudmila Molkova** 20:37 Yeah, I…
**Steve Rao** 20:40 Yeah.
**Liudmila Molkova** 20:41 I agree, we can.
Talk about it separately, and… Oh, you left a comment, thank you.
**Steve Rao** 20:49 Yeah, yeah.
**Trask Stalnaker** 21:07 Okay, so this is a GRPC client talking to a double…
**Steve Rao** 21:14 law.
**Trask Stalnaker** 21:15 server.
is not a Dubbo client.
**Steve Rao** 21:21 It's them.
Yeah, yeah, I also test, run a double client to, invoke, GRPC server. It's, it's the same. It will create two spans, one called, double, another called, gRPC. Just, just like,
It's just controvers, vice versa, please.
**Trask Stalnaker** 21:48 Okay, it'll create, is the client span always RPC system gRPC?
**Steve Rao** 21:55 you mean, in… Double client.
**Trask Stalnaker** 22:01 Yeah.
**Steve Rao** 22:02 No, it's the Apache Dabo.
**Trask Stalnaker** 22:05 Okay.
Right, right.
**Steve Rao** 22:10 And, yeah, the triple protocol, is, additional, is an extended, protocol based on gRPC.
it used the HTTP2, API to achieve, features.
Similar to GRPC.
**Trask Stalnaker** 22:32 So that gets extra… even more confusing than would the be triple, like…
**Steve Rao** 22:37 Yeah, yeah, maybe… Maybe I should…
**Trask Stalnaker** 22:41 protocol.
**Steve Rao** 22:42 Yeah, maybe I, I, I guess,
Just like you mentioned, maybe we can use the RBC protocol name, and to, to capture the protocol information.
**Trask Stalnaker** 22:59 But it would be…
**Liudmila Molkova** 22:59 It would be… Go ahead. Then it would be gRPC triple… Double.
And it would not be the framework name.
So it would be gRPC on both sides. Oh… Or possibly triple.
**Trask Stalnaker** 23:15 Role-on-one. Yeah. Yeah, yeah.
**Liudmila Molkova** 23:17 Yeah.
**Trask Stalnaker** 23:19 Which I think is okay, given that Triple is an extension of gRPC.
**Steve Rao** 23:25 Yeah.
**Trask Stalnaker** 23:40 Are there certain things that Triple does if both sides are talking triple? That…
aren't in gRPC, or is it really just the gRPC protocol renamed for your use case?
**Steve Rao** 23:59 You, you mean, yeah, if, yeah, both sides are double client, are double, double client, invoke the, double server?
Yeah, in that side, maybe, they just use the gRPC protocol to, to communicate.
Is that a case?
**Trask Stalnaker** 24:24 Sure.
I guess my question is, why… what's different about Triple?
Compared to gRPC.
**Steve Rao** 24:33 Yeah, maybe for this question, maybe we can, go to the documentation. It, supports some, additional feature. Yeah, maybe we can…
Yep.
It's introduce something about that.
**Trask Stalnaker** 25:03 So it's design and implementation of GRPC.
So does that mean at the protocol? So that's kind of what I'm trying to understand is…
Is it really just GRPC protocol, like a wrapper around?
**Steve Rao** 25:18 But it provides some, convenient, use case, for, for users.
**Trask Stalnaker** 25:36 So, it's compatible with the gRPC framework.
This is where we just keep falling down this rabbit hole of framework versus protocol.
**James Thompson** 25:50 And it's also the same for Connect RPC.
Right?
**Trask Stalnaker** 25:59 Connect talks gRPC, I forget.
**James Thompson** 26:03 Yeah, it talks gRPC, ConnectRPC, and HTTP.
**Trask Stalnaker** 26:15 Okay, so… gRPC, is… Okay, candidates.
PRPC, both a framework and a protocol.
Double… Okay, framework… That supports…
The Dubbo, the native, That's, also, the… Let's see… Triple… I'm not sure if…
**Liudmila Molkova** 27:21 It seems, based on the docs, the triple is defined as a prodigal.
And the double is a framework Rounded, that's somewhat protocol.
Agnostic.
This is my understanding, but Steve, can you correct me?
**Steve Rao** 27:43 Yes, I think, yeah, it's okay.
**Trask Stalnaker** 27:52 Can you tell, Ludmila, I guess my question, like, what…
at the protocol layer, what does Ripple…
provide that's not in gRPC? Do we have any examples?
**Steve Rao** 28:05 I, I set a, link in, chat, yeah, you can…
**Trask Stalnaker** 28:14 Nice.
**Liudmila Molkova** 28:28 So it supports content types, like application JSON, that you can…
invoke from, let's say, a browser or URL.
Essentially, right? If, let's say, you have a Triple Server.
then the client can interact with it in more ways than with gRPC server.
**Trask Stalnaker** 28:53 I see. And that is… yes, that makes sense, that that would be defined as a protocol.
Do we have other links for… Double a double 2…
So it's called 002.
**Steve Rao** 29:26 Yeah, yeah, double 2 is also… we equal the double particle, yeah.
**Liudmila Molkova** 29:32 Is it fair to say that the triple replaces W2, so this is a major version bump?
**Steve Rao** 29:39 Yeah, maybe you can, you can sync it like this.
**Liudmila Molkova** 29:46 And does it mean that you folks would be… would consider DAW2 as something legacy, or old, and…
unimportant? How do you think about it?
**Steve Rao** 29:57 yeah, the double protocol support, support in 2.0.
And in CL, they desert a new, protocol called GPO. This is, the background of protocol.
**Trask Stalnaker** 30:14 Oh, okay.
So…
Okay, and then we've got Connect, RPC…
Which can talk GRPC…
Choosing the protocol…
**Liudmila Molkova** 31:12 It also supports gRPC Web.
**Trask Stalnaker** 31:20 the new one.
**James Thompson** 31:24 On the left-hand side, there's a page, multi-protocol Support.
Down at the bottom of the list.
**Trask Stalnaker** 31:38 Connect protocol… okay, I just want to add some links.
Connect…
You said GRPC web?
**Liudmila Molkova** 32:05 Sure, BC Webb, yes.
**Trask Stalnaker** 32:11 Yeah, okay… Oh, it's connect… Is that?
The only one… yeah, so maybe they don't even support regular gRPC, but whatever gRPC web is…
**Liudmila Molkova** 32:26 Oh, no, they do claim they support your peace.
E.
Okay. Safety…
**Trask Stalnaker** 32:37 Go ahead.
**Liudmila Molkova** 32:38 If you come back to the previous page, they mentioned GRPC, GRPC web.
**Trask Stalnaker** 32:52 Okay.
So, gRPC, gRPC Web, Connect.
**James Thompson** 33:00 And HTTP, as well.
**Liudmila Molkova** 33:03 The connect is based on the HTTP.
And your PC web, I would imagine, is also based on HTTP.
The gRPC is based on HTC.
**Trask Stalnaker** 33:25 Okay.
The last one that I think we've talked about has… been JSON RPC?
**Liudmila Molkova** 33:37 Yeah.
And this front is… it's…
It's essentially agnostic to protocol at all.
So, you can… Use it over, let's say, as the dean.
So…
**Trask Stalnaker** 34:06 Yeah, that's where my…
I get… I get stuck on what's a protocol.
**Liudmila Molkova** 34:12 Yeah.
**Trask Stalnaker** 34:13 Yeah, cause, like, I think of this as a protocol.
Because it defines, like, Status code…
But I totally get that it's not a protocol in the wire Protocol sense.
**Liudmila Molkova** 34:37 Yeah.
**Trask Stalnaker** 34:57 Not a wire…
**Liudmila Molkova** 35:05 Wow.
Your PC is not a wire product, alright?
as well.
And it's based on HTTP.
**Trask Stalnaker** 35:15 Yeah… okay, but it's… it's… Okay, so, but it's… it's bound to us one… wire protocol.
**Liudmila Molkova** 35:28 Right, yeah.
**Trask Stalnaker** 35:31 Okay, supports multiple… Ir… Love all.
**Liudmila Molkova** 35:48 It's also not the framework.
**Trask Stalnaker** 35:53 Yes.
Not a framework.
**James Thompson** 36:01 I almost see it as a message specification.
Right? Because it's describing the type of message that's sent.
Alright, it's the bottom of the envelope.
**Trask Stalnaker** 36:14 It has the name RPC in it.
**James Thompson** 36:18 Yeah.
**Trask Stalnaker** 36:27 It's only synchronous, right?
**James Thompson** 36:31 Y-you ha- no, you have notifications?
**Trask Stalnaker** 36:36 locations…
**Liudmila Molkova** 36:40 So you can exchange arbitrary messages.
**Trask Stalnaker** 36:44 Okay, so it can be streaming.
**Liudmila Molkova** 36:47 It can be streaming, yes.
After defeating me!
**Trask Stalnaker** 37:00 Okay.
Do we agree that this is…
Is there anything else we want to add to our candidate list?
Let's see if we mentioned anything else on our… Project.
Proposal…
We did mention… this… We haven't.
odd.
So we could definitely consider that.
Nice.
No, we didn't mention JSON RPC. I think you had mentioned it in your… I think I might have cut that out or something, because I feel like…
That was in one of your early drafts.
**Liudmila Molkova** 38:00 Yeah, but anyway, we… We have an existing convention for it.
**Trask Stalnaker** 38:10 Oh yeah, do we have any other existing… conventions.
**James Thompson** 38:16 There's just the three.
**Trask Stalnaker** 38:19 Okay, so no double, but the other three.
Okay.
So at least… Let me post that, because that… At least helps us.
have a place to keep coming back to.
Do we want to… drill into the… further into this, in terms of what RPC protocol name… would be…
Or was there anything else that we should do first?
**Liudmila Molkova** 39:14 We can drill down into this, I…
Have a PR… oh, we have just a few minutes left.
I… .
**Trask Stalnaker** 39:25 Yeah, let's look at the open PRs.
**Liudmila Molkova** 39:27 Yeah.
**Trask Stalnaker** 39:27 Good.
Network protocol attributes, RPC signals… Okay, so we are good to…
Add in error type to RPC… oh, yes, I saw your ask there.
**Liudmila Molkova** 39:59 We… It would be a bit wider than this PR.
So, because we already used the generic nodes, on RPC metrics?
So… I don't mind if we do this as a follow-up, but we could also… stood here.
**Trask Stalnaker** 40:23 Let's do it in the follow-up.
**Liudmila Molkova** 40:27 Yep.
Oh, no good.
need cops.
Don't just look at me!
**Trask Stalnaker** 40:57 Alright, and we've got, oh, yes, yes, I agree with this.
So… James, I think just remove… let's just remove them.
From here.
Cool.
**Liudmila Molkova** 41:28 Should we close this PR then? Because it…
**Trask Stalnaker** 41:31 only thing?
**Liudmila Molkova** 41:33 I think so.
**Trask Stalnaker** 41:34 Haha.
I miss sad.
Indeed.
Yeah.
Makes sense.
Alright, and… Remove network type from… oh yes, this was…
Okay, oh, needs another rebase, okay…
And… Oh! I used another rebase. Sorry.
Alright.
Cool, but they have, as soon as that one, yeah, then we're good to go there.
**James Thompson** 42:35 Also, in the agenda, there is a question about what to do for one of the issues.
**Trask Stalnaker** 42:41 True.
**James Thompson** 42:42 The last one, hu.
**Trask Stalnaker** 42:43 This one? Okay.
**James Thompson** 42:47 Let's scroll right down to the bottom.
**Trask Stalnaker** 42:50 Yeah.
**Liudmila Molkova** 42:56 I've started looking into this, and I think we should tie the duration Question 2…
It's kind of hairy. So, for non-streaming calls, it's trivial.
But… We cry out.
**Trask Stalnaker** 43:16 Well, we thought it was trivial, I mean, but yes, we can copy-paste the definition from… the non-trivial definition from HTTP.
**Liudmila Molkova** 43:25 Yeah, but for… RPC… streaming.
In theory, we should have the duration of the whole…
thing, more reliable than an HTTP case.
And…
So what we can… what we can do, we can… so I checked what…
gRPC does. The gRPC, the native instrumentation.
As the end-to-end duration, from the start to the end, meaning to the status code.
And the status code is sent when the stream is completed.
**Trask Stalnaker** 44:17 Okay.
**Liudmila Molkova** 44:19 So… if… We… we have a choice. Either we say, okay.
We have one version of span for… and metric, more importantly, for a non-streaming case, and another one for streaming.
Where we need to be… we need to also think about the end-to-end duration.
So, whenever we… like, we also probably should figure out the protocol versus framework question before we proceed with this. What is this?
logical operation.
**Trask Stalnaker** 45:04 Well, the one thing you said that I liked was what, you know, looking at what the gRPC team has chosen to do for the streaming
case, even though it's only metrics that… that… I hadn't thought about that, that we could learn
Kind of from their implementation for metrics, even, like, for the streaming case, what is duration there?
**Liudmila Molkova** 45:30 Yeah, and there is another trick we do in Genie A conventions. We can have a time to the first.
Message.
For this… the reaming… That's the strategy goal. So, but essentially, it's extensible to support… other… more observability.
So I think that the part that's the duration of the corresponding KPI call would be tricky for RPC considering streaming.
**Trask Stalnaker** 46:25 Yeah.
But I like, I mean, I like the initial proposal of… It's until the status code…
Is that, I mean, in the streaming case.
Basically, until this dream has ended.
**Liudmila Molkova** 46:45 Yeah.
**James Thompson** 46:46 But weren't the logic… logical operations…
include a reconnect, so if you've got a status code, that's…
status code, then it could reconnect, so wouldn't that technically be the same logical operation?
**Trask Stalnaker** 47:05 I didn't underst… I didn't follow that example.
**James Thompson** 47:08 So, you create a stream, and you get a status code back, Alright.
Indicating that the connection's closed.
But what if the operation reconnects?
Right? On the error.
Right? Wouldn't that be the same logical operation?
**Trask Stalnaker** 47:36 I don't know.
**Liudmila Molkova** 47:38 Yeah, this is… Another tricky part.
Right, so I… this is the second sentence, right, in this thing… it…
**James Thompson** 47:50 It's probably fine, but the prob- the problem…
**Liudmila Molkova** 47:53 Let's maybe try to solve the problem as the first sentence.
Because there is no single API call representing the streaming case.
**Trask Stalnaker** 48:08 And we are, we did hit our… time boundary…
So, let's bump this, and
We'll… let's put both of these two on… Next week's…
Topics…
Cool.
Well, thank y'all.
**Liudmila Molkova** 48:57 Thank you.
**Trask Stalnaker** 48:58 Welcome back, Lydnilla.
**Liudmila Molkova** 48:59 Thanks!
Thanks for driving it, and see you around!
**Trask Stalnaker** 49:03 See ya.
