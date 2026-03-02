SIG: RPC Sem Conv Stability SIG
Date: 2025-10-22
Duration: 47 minutes
Zoom Recording URL: https://zoom.us/rec/share/AXkl8uoqf2ypmhIlN1j80Olr2H2ZdwBOQWna3hcPxSoi181ar7qaW4AQqN4Mh7ZO.AdsuBJIHdpZqMxiC
============================================================

## Zoom Recording Transcript

**Liudmila Molkova** 02:45 Hi, everyone.
**Steve Rao** 02:51 Hello?
**Trask Stalnaker** 03:02 Hey, alright, we've got a crowd!
**Steve Rao** 03:18 Yeah, everyone.
**Trask Stalnaker** 03:21 Nice to you.
Lyudmila, if you're… Talking to us, you're muted.
**Liudmila Molkova** 04:12 Oh, I'm so sorry!
Okay, I've been going.
**Trask Stalnaker** 04:16 And you thought we were being all quiet.
**Liudmila Molkova** 04:20 Yeah.
Absolutely, yes.
**Trask Stalnaker** 04:24 Sorry, I'll… as normal, I'm looking for the, Zoom…
host key, so I can kick out our bot friend.
**Liudmila Molkova** 04:34 Mmm.
Go for it. I'm checking if you have anything, yeah.
**Trask Stalnaker** 04:39 Sometime I'll learn to just live with the bot.
**Liudmila Molkova** 04:48 Yeah, so I'm looking what we have in progress, and if we need to, if we can
Make something happen.
So for this one, I guess we need another one.
somebody from Semantic Conventions to approve, because you trust clocked yourself out of it.
**Trask Stalnaker** 05:07 Oh, yes, yes.
**Liudmila Molkova** 05:12 Why is this one in progress?
**Trask Stalnaker** 05:17 Fine.
**Liudmila Molkova** 05:19 the WCF attributes and spends.
**James Thompson** 05:23 It shouldn't be.
**Liudmila Molkova** 05:26 Should not?
**James Thompson** 05:27 It should not be in progress.
**Liudmila Molkova** 05:29 Okay.
So, I guess I'll put it in the possibility?
Okay.
And then… what do we have in… Oh, okay, quite diff… Your new issues, right?
Okay, so I'm working on this one. We can put it in progress.
**James Thompson** 06:06 Couldn't we do that one at the same time as the rename of the metric?
Because otherwise, we don't have any record of the unit changing.
**Liudmila Molkova** 06:20 I don't know if I should rename this metric.
But, let's put it in the agenda, okay?
Great.
What else do we have?
In no status.
So let's spend… Couple, more minutes.
Triaging what we can in null status, and then…
Let's move on to the agenda.
I thought we rearragged it.
**James Thompson** 07:25 We can come back to that one, that's post-stability anyway.
**Liudmila Molkova** 07:29 Okay. Yeah, I agree.
RPC conventions for GVT.
**Trask Stalnaker** 07:41 post stability.
I think… do we have a… do we have a…
**James Thompson** 07:48 Quidd. Yes.
**Trask Stalnaker** 07:50 Okay.
**James Thompson** 07:54 Alright, it says Java Report.
**Liudmila Molkova** 08:11 Okay.
Let's just do one more. This one, it's probably… Definitely prayer stability.
Which caters for no service being known, and also enables streaming messages to be identified.
Okay, let's talk about it, but it sounds like the pre-stability work item.
**Trask Stalnaker** 08:46 At least the non-streaming aspect.
**Liudmila Molkova** 08:50 Right.
Okay, I closed… Our meeting notes, but let's get back to them.
thing this… Continues the discussion we started last time.
**Trask Stalnaker** 09:16 Right…
**Liudmila Molkova** 09:22 So it sounds… gRPC is the no-brainer. Like, if we don't stabilize gRPC, we cannot stabilize anything else.
The connector PC is pretty much a different flavor of gRPC.
And I'm still trying to understand the Dubo story, but it sounds like it's… okay, so both Connector PC and… and… and…
doable, or… compatible with gRPC plus compatible with more things, so they're…
A little bit like an abstraction on top of the gRPC.
or a protocol.
So, all this to say that this…
Pretty much the same conventions with some minor tweaks.
**Trask Stalnaker** 10:25 Yeah, the…
**James Thompson** 10:26 Are we saying… are we saying Davos is the protocol?
**Liudmila Molkova** 10:31 It is?
It is two protocols.
**James Thompson** 10:34 Yeah.
But, in terms of what we have in our conventions as the protocol name.
**Liudmila Molkova** 10:45 Can you repeat?
**Sean Yang** 10:47 Sorry, can you hear me?
**Liudmila Molkova** 10:49 Yeah.
**Sean Yang** 10:50 Thank you. Yeah, double has the multi version. We have double 2 and double 3. In double 2, we have a protocol both on TCP. That means, the proc vertical means double. But in double 3,
we introduced a new protocol, named Triple. Yeah, that triple protocol is based on the GRPC, but the difference, with the GRPC is that GRPC only supports
photopath, serious ferment.
Yeah, you, you, if you want to use gRPC, first, first you should write a, protocol defense,
IDL, but in double, you can use every Java interface as a, RPC, IDL. So, the triple protocol will warp.
our, internal, series, series, method to, to, gRPC protocol. So, that means, triple were compatible with the gRPC format.
So, that means, in…
in trouble, it's where Core will use the gRPC, HTTP, specialization. So, so, I think it doesn't mean,
that means, Triple is complete with the, GIPLC, but there are some different,
with the gaps that, in…
because the GSPC will have a client and a server, and, in server-side, the triple will support multi, multi-style protocol. For example, it will… it can stop
the IPC, and it can't, provide the rest
access. So, you can access the, triple protocol from the gRPC client, or, or the double triple client.
Or you can direct access the REST endpoint, use the, browser, or… other, REST client.
Yeah.
That's the difference with the Triple and gRPC.
**Trask Stalnaker** 13:33 I had a question, Sean, if you look at the…
wire, like, look at the traffic on the wire. Does it look just like gRPC?
Or I guess.
**Sean Yang** 13:50 Yeah, yeah, that's in why I think it's the same with GRPC.
**Trask Stalnaker** 13:59 if you're using, unless you're using HTTP use, like, for, like, web browsing.
**Sean Yang** 14:08 Yeah, yeah. If you're, you're, you're, you're actually…
REST HTTP, it will, series with the JSN, not, not by the protocol, yeah.
You're right.
**Trask Stalnaker** 14:27 And so one of the dis… Questions we had… Is whether we're… capturing…
like, RPC… right now, we have this rpc.system Attribute, where we put
double or GRPC in those… in that value.
on… We're thinking of changing that Possibly to rpc.protocol.name?
But we're struggling a little bit with RPC because
There's the protocol, and then there's the framework.
so, like, in Dubbo case…
maybe RPC system name makes sense as doo, and protocol name as gRPC…
But we kind of wanted to just… Yeah.
So I'm not sure, like, how… How…
Do you all… how do you all see, like, what's the important thing
Do you think, for your users, to be able to see that it was… like, say you only got to pick one.
Would you want users to know that it was Dubbo sending Dubbo, or that it was…
the protocol, the GRPC protocol.
**Sean Yang** 16:05 Hmm… as… I think for… Photo 2, for double 2, protocol name should be double.
And the network protocol name is based on the TCP, yes.
Yes.
Because we have… in Dabo, we have…
two versions, yeah, yeah, yeah. The, the, the W2, it used TCP.
not HTTP.
Yeah, and the acceleration, is not… it's different with the F3.
So… I prefer the,
Oracle name, you use triple or double?
I, I think… put a PS4.
**Trask Stalnaker** 17:09 Oh, I see, it's not… right, right, my… my… Yeah, yeah, yeah. It's not GRPC, yeah, it's triple.
**Sean Yang** 17:15 Yeah, yeah, yeah.
**Trask Stalnaker** 17:16 Okay.
**Sean Yang** 17:17 A network protocol… Natal work.
**Liudmila Molkova** 17:28 This one, there's… go ahead.
**Sean Yang** 17:30 I think this line you… somewhere.
Yeah, I think he…
**Albumen** 17:37 for it, which is, how can open elementary figure about several, kind of.
protocol on HTTP reaches, which are, like, WebDocket.
server stream and application JSON, or… and so on, yeah. How can we distinguish it? Because they are all HTTP.
And for Triple, we… to be honest, we think Triple is more like the HTT protocol itself.
We support application JSON, we support application drafty.
Yeah, and as a client side, we only support application GRPC, but for the server side, we support JSON,
port, PenGAT, port application draft PC, and so on.
So, I think it is a really big protocol for triple protocol.
Yeah, and for us, we just exposed the name about Triple to our user. They just use the Triple protocol.
And… Which kind of the…
Protocol achieved on the wire is… all depends on the client.
connected to the thorough.
**Liudmila Molkova** 19:15 So, if I understand correctly,
The part that they caught is…
The… there are a lot of variations within
let's say triple server, and you would like.
**Albumen** 19:29 Yeah.
**Liudmila Molkova** 19:30 For the content.
Type that's requested by client.
**Albumen** 19:35 Yeah, yeah, yes, yes. By default, it…
It is, by default, it is application JSON, but if the client requests, like, the WebSocket, we will use the WebSocket way, or if it's application Japanese, we will use the Japanese way.
**Liudmila Molkova** 19:58 So we want to record a flavor of this.
A radical, in some form.
**Albumen** 20:06 Yeah, then… my question is, how can… OpenTelemetry record, like, Tomcat.
yeah, the HTTP server on Tomcat, because Tomcat also support, like, WebSockets.
support, like, JSON, and so on. Yeah, will the… maybe the stop… Cannot have been recorded.
**Liudmila Molkova** 20:37 So for the Tomcat, this would be…
Not the technology thing, but the instrumentation library that applies to the cut.
And then we would…
**Albumen** 20:50 Hmm…
**Liudmila Molkova** 20:50 forward it in the Instrumentation scope name, but… Like, why would it be…
Like, why would you want to record it in some?
structured way. What is that that you want to actually record?
**Albumen** 21:08 Because, for the traffic away, most of the clients are inside the data center.
But if we use the… JSON where most of the users
And they come from, like, the end user.
Which is the north and, north-south traffic, but…
For the job, it's the way we think, most of users only use it in the data center.
So… And… Mmm… another reason for, like, is…
From the traffic… the traffic from the user, we might apply more, like, security tech on them, but…
For those traffic inside the data center, we would be more… make it easy for our users.
then… the policy might be different. So, if there is only one choice, we would…
truth, the protocol name be.
be triple. But if there is another…
attributes for double, we would be like to record the real content type.
Yeah, and that, that can be the, attribute for double only, like, the attributes for GRPC only, yeah, that just only for double, that's okay.
**Liudmila Molkova** 22:51 Yeah, we do have the content type attribute, but it's specific to HTTP request and response headers.
And…
**Albumen** 23:02 Yeah, that's okay, that's enough for us.
**Liudmila Molkova** 23:06 Okay So, it would be the…
There are, the request had their key, so the content type would be here, and the corresponding corresponds.
Content type.
**Trask Stalnaker** 23:35 Yeah, and as you mentioned, also, if there are Dubbo-specific things, we can… have Double-specific attributes as well.
**Albumen** 23:49 Yeah, yeah.
**Trask Stalnaker** 23:50 Same as…
**Albumen** 23:51 that I've earned.
**Trask Stalnaker** 23:52 What we're… we're trying to understand at this point, kind of just very high level, what's the… what's the common pieces between all of the RPC frameworks?
**Albumen** 24:09 Yeah, yeah, yeah. I think you can treat the…
VIPO protocol as a more native HTTP protocol now.
Things double is 3.3.
Yeah, we re-factorily, totally.
And now it's all based on HGT protocol, it…
for not only HTTP2 for GRPC, now it's… it only… it also supports HTTP1 and HTTP3.
Yeah, we… so, under… underlined it, there's a…
several ways to request a triple server, like using HTTP 1.1 with JSON to triple server, using HTTP2 with JRPC,
And even on HTTP3, we also support GRPC and JSON now.
**Liudmila Molkova** 25:16 I'm thinking where the… where is… what is the line between network protocol?
an RPC protocol.
**Albumen** 25:26 I think on… based on the network, it…
50, wow.
Yeah, they are all based on HTTP, and we can use only one HTTP
to figure out on the network. Yeah, and it is friendly for the… getaway.
to distinguish, Traffic inside it.
**Liudmila Molkova** 26:01 Okay, so, like, triple or double, they are… they are not not for protocols.
At least because they, they…
**Albumen** 26:11 Yeah, the HTTP.
**Liudmila Molkova** 26:13 Yeah, their news, yeah.
**Trask Stalnaker** 26:14 I mean, Dubbo is… I guess, technically, right? Because you said Dubbo is straight on TCP.
**Albumen** 26:24 Yeah, we built on NetHeat, and we support…
a totally private TCP protocol, like, for the double protocol. Then, for the triple protocol, we, based on native with the HTTP,
library, then we support all the content type on HTTP.
Yeah, double can be a network protocol. It's only private for double SDK.
**Trask Stalnaker** 27:10 What do you mean by it's private?
**Albumen** 27:13 If you… if you want to decode the content, you should follow the double way, and…
as I knew…
there is only several gateways supported. Yeah, most of the gateway only bypassed it with the raw TCP traffic.
They cannot.
decode the… Power midran inside the request.
Yeah.
The protocol is private, but, there's not a…
**Trask Stalnaker** 27:52 Specification, there's no specification.
**Albumen** 27:56 Yeah, yeah, yeah, HTTP.
**Liudmila Molkova** 28:20 I think that this… we're still… Have this question of… What should we call it?
Like, the protocol or framework.
**Albumen** 28:34 Mmm… I think we can follow… other… Other framework, let's connect RPC.
the Triple protocol itself is…
a little similar to the Connect protocol, I think.
**Liudmila Molkova** 28:58 Yeah, and the connector PC is probably… It's a… Okay, there is a protocol…
So, right, to a certain extent, it's similar to triple, right? It's the…
**Albumen** 29:17 Yeah, we were inspired from the Kinect, two years ago, yeah.
To be honest.
**Trask Stalnaker** 29:27 I like the… Ludmila, the… Separate, like, the… you've added the network transport, Name there.
I mean, network protocol name?
because that fits into, like, the… JSON RPC example well.
Where… JSON RPC is a protocol, but it is not a transport.
And so… JSON RPC fits nicely as a protocol name, But then you can… Still have network protocol name.
**Matthew Hensley** 30:10 So, one thing's part of this, like.
we have… everything has a transport of some type, like TCP, UDP, whatever.
I think on top of it, we actually talk about the protocol.
I think where maybe a good line to draw is, in the case, like, double, it sounds like the wire format is an implementation detail specific to double, double, despite it using
Some common transports.
Versus JSON RPC is something that you expect interopt?
So I think…
that might be a good way to delineate the protocol. So, like, in this… in that case, JSON RPC,
in gRPC that are designed for interrupt would be a great protocol.
But so is double. DOBO, because…
it can only speak to itself. So, it's like, you have to implement this thing.
And it just so happens to be in that case, it's an implementation detail versus, like, JSON RPC.
And we might get… The next layer up in the scope info.
Because it's, like, your actual client or server library that's been instrumented Is obviously super important.
But when I think about protocol, it's like, what do you have to speak?
**Trask Stalnaker** 31:25 Like, it doesn't really matter how.
**Matthew Hensley** 31:27 But it's trying to figure out how to enable interrupt here, and is interrupt even expected?
Don't know if that makes sense, but…
**Trask Stalnaker** 31:38 So what would you say for 002…
Then, where it's just the native Dubo protocol…
Would you put that under network protocol name, or RPC protocol name, or both?
I was wondering, Matt, what you were thinking there.
**Matthew Hensley** 32:11 I'm trying to sort it out to something coherent.
I guess, forgetting these particular labels, I think about, like, they… there's some mechanism, standard I.O, TCP, whatever.
That these protocols use. You have a protocol on top of it.
That you have to implement, and then it's… I think the issue is things like JSON RPC have many libraries with many implementations.
Things like Dubbo are…
a protocol and a framework all wrapped up, like, there's not a distinction in that case, versus…
all these JSON RPC and gRPC implementations, where
different library, they all speak the same thing. In the case of Dubbo, they're…
Hard to separate, because it's an implementation detail within that.
framework.
**Liudmila Molkova** 33:07 And we still want to… Report the RPC spends for double, regardless of the… protocol, because… Everything except…
The value of this attribute is… Describing the same thing that… Procedural.
**Trask Stalnaker** 33:33 Sorry, can you repeat that? I didn't follow.
**Liudmila Molkova** 33:37 So we… if DABO is just a network protocol name, right, DABO2.
We still want an RPC span for whatever happens over this network protocol.
Right. And… We still want some constant.
I… I have a minor concern that there are two constants. I'm not sure if…
It makes sense to have them.
But… Yeah, I also don't see the other way to capture the specific flavor.
**Matthew Hensley** 34:16 Well, I think what we've done in some other spots… I think that's good…
way to make this slightly more concretely, Mela, is that in the case of Dubbo, it's gonna be kind of duplicated. Gonna have these…
two constants that are the same? That's what you're saying?
**Liudmila Molkova** 34:35 I'm saying that, like, let's forget about protocol name, network protocol name for a second. Here.
So the triple and double Or similar constants. W2, yeah.
Here.
They're similar.
But not similar enough that we… Would have one value.
So we…
**Trask Stalnaker** 35:02 Why do you think they're similar?
**Liudmila Molkova** 35:09 I would imagine this is an implementation… oh, it's not an implementation detail, those are different major versions of the…
framework I'm using.
Okay.
**Trask Stalnaker** 35:25 can… 003 oct… over W002 protocol?
**Albumen** 35:33 No.
No, yeah, we… we should fit the…
Apple protocol and a Drupal protocol, totally, yeah.
Double SDK or double framework supports two types of protocols.
One is double protocol, which we used.
Mainly on double 2… double 2.
Then, for the turbo protocol, it's a totally brand new protocol we introduced.
For several years. Yeah, it can only run on double 3, and double 3, supports both double protocol and triple protocol, and the double protocol is only for compatible methods.
Then, if we talk about the double protocol itself, it just only means the double protocol we used on double 2, and it is totally, based on the TCP… built on the TCP.
It doesn't meet the… specification, like the HTTP, is totally different with HTTP.
But if you're using the triple protocol, it's totally based on the HTTV protocol.
then you can, see it like a HTTP, Package on the wire.
Yeah, then… Based on that approval protocol, we have several We support several content hype.
Yeah, several kinds of tab.
Like, one is for application GRPC, which is totally works, follow the specification of gRPC.
And another… Kind of… kind of obvious application JSON, we totally work… follow the specification of React protocol.
And beside it, we also support, like, WebSockets, SovaStream.
And so long. Yeah, that's all, capital protocol on AzureTV protocol.
But double protocol, not.
**Trask Stalnaker** 37:58 Triple protocol is really, like, Multiple…
Oh, no, I guess it… I'm trying to decide if it's multiple protocols or multiple transports for…
**Albumen** 38:16 Like, we can… we can treat their HTTP
with HTTP1, HTTP2, HTTP3, right? But… they… they all…
are… they… they are… they are on… Integrated protocol.
Yeah, we can use attribute protocol for these three… protocol layer.
Although they are totally different on the network.
Back in the car.
**Trask Stalnaker** 38:45 The content type. The content type is just what you use to vary.
**Albumen** 38:50 No response.
Yeah, yeah, yeah, yeah.
So, that… and… and the behavior.
Are the behaviors between these
content hubs are totally different. So that is the reason why we want to record the…
Real content type on one request.
But we think the triple protocol
can cover all the requests on HTT protocol on double.
Yeah.
So, and for… we can now… I think we can start with, maybe the double tool protocol, yeah. It can be… it can follow the, directory
framework, yeah, how Jack is to be recorded in the network name, the protocol name?
**Trask Stalnaker** 40:04 So, on the… double server, if you get a gRPC request…
**Albumen** 40:13 No, not only double server on the track is this server.
And how… we can follow the way, like, the GPC itself.
**Trask Stalnaker** 40:25 So, in the double server framework.
if you get a gRPC request, you could log…
would you want to log RPC protocol name as GRPC in that case?
Of course.
**Albumen** 40:44 We would prefer to record with triple, at least, yeah.
**Trask Stalnaker** 40:50 And the gRPC is a variant of being a variant of the triple.
**Albumen** 40:56 Yeah.
**Liudmila Molkova** 41:03 So there is one thing that I…
I think we… we would need to discuss is which of those layers.
We're actually instrument on.
One relevant discussion is about retries.
So… Let's say we talk about gRPC retrice.
And they would, like, on the library framework, there would be one client call.
On the protocol level, there could be two calls.
There would be two calls on this server.
**Albumen** 41:46 Yeah, that's right. The retry, even in double… not only on double 2 or double 3, the triple protocol, we retries on the library.
Yeah.
**Liudmila Molkova** 42:02 Yeah, and they've.
**Albumen** 42:03 Timeout, or the server error, or the network error.
The protocol itself only throws the exception directly to the library.
Then the library will figure out whether
retry or not. It all depends on the user's preference.
Then, on the network, or on the…
protocol. If the user tries to retries, there's multiple procedure call.
But, for the user side, that's the only one.
**Liudmila Molkova** 42:41 Right.
No, it would be from telemetry's side, it would be really weird if we had one client spend for a PC.
But to… Server expense.
**Albumen** 42:59 I think that that is… depends on our instrumentations, yeah.
You can instruct double with the…
We have the cluster filter, yeah, which is for the user's core.
If even there are any retries on one core, the cluster filter will only run once.
But if you instruct on the filter, yeah, difference with the cluster field, the filter itself.
each… Procedure call will record once.
So, mmm… it depends on our preference.
Yeah, we can record once or record multiple times.
**Trask Stalnaker** 43:45 And that was sort of Lanila aspirational, like, I mean, what we would like is a one-to-one, but I mean, I know in the Java instrumentation, depending on what
But you're able to instrument having one client span, and…
Two service bands is not uncommon, unfortunately.
**Liudmila Molkova** 44:07 Yeah, so maybe we can, think about it similarly to HTTP, where we have a preference, right?
We have a preference for per attempt.
And then… I say, if it's not possible, then okay.
Do what you can.
**Albumen** 44:31 Yeah. Mmm… Yeah, that's all possible, but based on our…
Research and our user's preference, we would prefer to re… to use only one span, even if there is any retract.
Bah.
Yeah, but that's okay to the users. Some wants to record for using several spans, some wants once.
But based on our implementations inside Alibaba, we only use one span.
For the retries. And actually, by default, we would disable the retries.
I default.
Bah.
Yeah, then it would be not really confusing if there is no retries.
**Liudmila Molkova** 45:27 Yeah, I agree. So I think what you're saying matches, what I understand from your PC metrics.
they met… they actually have two metrics. They have the…
Overall duration, and they have the attempt duration.
So this makes me think that they… One at least Like, they target cannibal slayers.
Here.
**Albumen** 45:59 Yeah, that's right, so in our world, that's important.
**Liudmila Molkova** 46:05 And also, if we're talking about gRPC, then there is HTTP instrumentation underneath, which actually tracks retries already.
**Albumen** 46:17 Mmm… Yeah, so… I think we…
If it is, the triple… yeah, that the name likes the triple, then we can… Desire that I…
way might… might a little weird to the SGDP here, or a little weird to Japanese, but that all works for the triple product itself.
**Liudmila Molkova** 46:50 Okay, we are at time. I think we understand the problem better, but I don't think we have a final solution still.
**Albumen** 47:00 Yeah, so that's okay, we… I think we can also…
Discuss next time on the issue.
Yeah, that's a really good start for double… double framework.
**Liudmila Molkova** 47:15 Yeah, thanks a lot for coming. Thank you.
**Steve Rao** 47:18 Yeah, thank you.
**Trask Stalnaker** 47:21 Bye.
**Liudmila Molkova** 47:21 See you around. Bye.
**Steve Rao** 47:23 I forgot to say, Shim and, and, Kevin, yeah, our maintainer from Dubo community, yeah.
**Trask Stalnaker** 47:31 I remember Kevin from before, I don't think I had met Sean before, nice to meet you.
**Albumen** 47:37 Yeah, and SA is also a PMC member in Dabo, yeah.
Awesome. Welcome.
**Liudmila Molkova** 47:46 Yeah.
**Albumen** 47:46 Thanks for coming.
**Trask Stalnaker** 47:47 See ya.
**Albumen** 47:49 Boo.
