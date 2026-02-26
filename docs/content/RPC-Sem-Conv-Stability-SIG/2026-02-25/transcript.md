SIG: RPC Sem Conv Stability SIG
Date: 2026-02-25
Duration: 31 minutes
============================================================

## Zoom Recording Transcript

**Steve Rao** 02:44 Yeah, hello, folks.
**Trask Stalnaker** 02:51 Ayy.
I know, we've got another note-taker.
**Steve Rao** 03:08 Well, yeah, there are two note-takers.
**Trask Stalnaker** 03:12 Yeah.
We'll give him a minute. Oh, Matt's here, hang on.
**Matthew Hensley / Grafana Labs** 04:08 Hello!
**Trask Stalnaker** 04:20 So, I'm not sure if we've got anything.
to do. We did, we went stable. I mean, we went RC.
I guess next up, we could kind of survey…
the state of… prototypes… I know…
been working… we're working on it in Java,
I've got a couple PRs in, and a couple PRs pending, and… but probably a good bit.
To go still…
**Matthew Hensley / Grafana Labs** 05:07 One thing I think we could do is maybe make a new issue or something for… or even just here in the agenda, the list of prototypes and who's working on them. I got asked a few times, kind of like, oh, who's… wait, who's doing what? Apparently, some of the RPC work has been a surprise to people.
**Trask Stalnaker** 05:30 Oh, the… the fact that we're… went… that we were close to being RC.
**Matthew Hensley / Grafana Labs** 05:36 I think just, like, because of the holidays and such, a lot of people just kind of missed…
any that it was happening, and that were… like, the RSC was like, wait, who's working on that? Like, what prototypes are coming?
**Trask Stalnaker** 05:53 Yeah, yeah, let's make an issue. Stabilize…
Alright, let's make sure there's not already an issue here for RPC State.
**Matthew Hensley / Grafana Labs** 06:05 The other thing with that, if, like, it's an issue, if someone else wishes to join in.
They can always drop a note, and… Share what they're working on.
**Trask Stalnaker** 06:16 Yeah…
Yeah, I think we can create a new issue. Stabilize our PC…
I think we've got an issue in Java, let's see…
Yeah, I think this is it.
**Matthew Hensley / Grafana Labs** 08:50 I need to write one up for the .NET stuff, and I'll do that and make sure.
It's referenced.
**Trask Stalnaker** 08:58 Cool.
It should link up.
more of these PRs to that issue.
Let's see…
Alright, I think… Right.
Actually, I can put… Steve, I can put you down for a demo.
**Steve Rao** 12:41 Sure.
**Trask Stalnaker** 12:55 Alright.
Cool, anything… any other thoughts?
**Matthew Hensley / Grafana Labs** 13:06 The only one that I've had… I'm pretty far along in the implementation.
And the only part I'm hung up on is the span name stuff, slash, like.
RPC method, and then when it's other, like, using the system name, trying to figure out in what scenario, like, first for WCF, it's trying to figure out what is the fully qualified name that makes sense here.
Because there's… like, SOAP namespacey things you can do, and also, obviously, like, a fully qualified Method name?
And so… Been sorting through that, trying to figure out what makes the most sense for instrumentation, and then…
Trying to understand, like, in what cases would we hit the other?
Like, where does that make sense? It's basically, like, how to…
Everything's clear besides that part of it.
is… A little, like, judgment-based.
And it's possible I just don't…
have enough, like, in-depth WCF knowledge.
That's intuitive, but that's one is…
as far as implementing, it's like, ugh, might need to,
Add some sentences when we're done, based on what we learned.
Here, because it's… it's not impossible, but it's, like, it's super subjective.
So far.
**Trask Stalnaker** 14:31 Yeah, I think that is kind of like,
That reminds me of a little bit of…
DB's system name, but worse.
not system name, DB namespace.
Where each… Database sort of has… or a lot of different… there's a lot of variety.
And so that's where those… kind of override…
So, like, GRPC… we should have… Let's see, span,
Dude, we should have RPC method… Pretty well.
Should be clear, but let's verify.
Just put verify.
**Matthew Hensley / Grafana Labs** 15:43 And I think… I'm probably just, like, over-analyzing some of this, but the fact there was…
any ambiguity is probably something someone else will run into. And it was a question of, like, what does fully qualified mean?
And I think it depends on the technology and…
perspective, so I was just thinking through that. I think all I think is we just end up with some more guidance.
Out of this.
**Trask Stalnaker** 16:09 Nope.
**Matthew Hensley / Grafana Labs** 16:10 future attempts.
**Trask Stalnaker** 16:13 Yeah, this is… maybe… I mean, it might be a little too much. Our general definition might be a little too GR… tailored to gRPC.
Fully qualified, logical name of the method, because… gRPC, sort of, Encodes it in that way.
Yeah, if there… I would…
Lean towards something that's in the payload.
That is… used… for routing it… to the appropriate… Endpoint, if that… Helps.
**Matthew Hensley / Grafana Labs** 17:07 Yeah, that's kind of the approach I've taken. It's kind of the…
what, like, the internal routing stuff, because in WCF, much like, I think, Dubbo's another good example, where you can define a service, and it's available over different transports that have
Fairly different semantics, like SOAP versus like…
A name pipe is extremely different, and how you address them ends up fairly different, so it's…
Just trying to figure out that, like, what's…
what would apply here and make sense in this ecosystem? Like, is… I don't… I'm just trying to figure out that one, because, like, WCF has, you know, namespaces and class names, and…
I think it looks like internally, that's how it maps it, and so that's what I'm going for.
Kind of like, what… what you'd see from any transport, so… that's been… Sorry.
Let me restate that, I'm… Got a little tongue-tied there,
I was moving towards the thing that works for all the transports, so regardless of how someone connects to your service, you would get a consistent method name, because that's what it's hitting.
And when I say method, it isn't necessarily, like, the code, it's what the framework uses for the routing.
And how it identifies it internally.
**Trask Stalnaker** 18:33 Yeah.
Makes sense. I mean, I think it's okay that different
Frameworks are gonna define that differently, and… So, like, something with, like, WCF, since it's only .NET.
It's not really gonna matter that much.
That it's a defined…
All that matters is that it's useful to users, as opposed to, like, the consistency.
**Matthew Hensley / Grafana Labs** 19:07 So that's actually… I disagree there, and because WCF is the framework name, but you have train supports that can interop, just like… it's like we talk about Dubbo, but it also supports gRPC.
And so, you would want both sides of that to be…
**Trask Stalnaker** 19:25 OWCF supports gRPC?
**Matthew Hensley / Grafana Labs** 19:28 No, WCF supports SOAP, and it is definitely… it supports SOAP and XML RPC, and while we don't hear about those often.
they are…
**Trask Stalnaker** 19:38 I see.
**Matthew Hensley / Grafana Labs** 19:39 Very much in use.
And don't…
**Trask Stalnaker** 19:42 fair.
**Matthew Hensley / Grafana Labs** 19:42 Yeah, between .NET and Java, like, the interrupt between those two is extremely common.
**Trask Stalnaker** 19:50 So, more or less, like, instead of thinking of, I mean.
for me, thinking about this problem, it's not really so much what would WCF use as what would you use for soap, like.
generic soap.
protocol, or so forth. Yeah, and that's my, conflict here. It's a little bit of both.
**Matthew Hensley / Grafana Labs** 20:14 Because you want it to be something reasonable, that if someone notices, like, hey, these should be aligned and they're not, that it's not completely different philosophies, but also…
What's idiomatic for people that But the more typical, like.NET-only use case.
**Trask Stalnaker** 20:37 Yeah, I haven't looked at… a SOAP request in… A decade or more, let's…
**Matthew Hensley / Grafana Labs** 20:48 I spent many years doing .NET and Java SOAP interrupt.
things, and… I… I guess it's good that it's useful in this case, but…
Man, it's crazy how different they can serialize things.
**Trask Stalnaker** 21:14 Let's see what we've got…
**Matthew Hensley / Grafana Labs** 21:19 And so, SOAP in particular is an easy example of this, where SOAP has your eyes, so you can have something that looks suspiciously like a URL.
It's stable.
You're supposed to, you know, it's whatever your company.
**Trask Stalnaker** 21:34 the endpoint that you target. So it's not in the body, it's… just the endpoint.
**Matthew Hensley / Grafana Labs** 21:41 No, it's in the envelope.
**Trask Stalnaker** 21:42 Might be in the box.
Okay.
**Matthew Hensley / Grafana Labs** 21:44 It's in the envelope, but it looks like a URL, because it's, you know, like, XMO namespacey.
And… But that's only for SOAP, that someone would use the URL-looking namespace stuff.
I'm sorry, if this doesn't make total sense, I'm still trying to sort it out in my head, like, how to satisfy…
These different dimensions.
**Trask Stalnaker** 22:24 Yeah, no, that sounds like, a useful…
snippet, or some comp, or even a… Yeah, how would we do… Dude…
And we can always put it in, like, a non-normative page,
But we could certainly consider a, a RPC… Override, kind of.
Page that describes that, kind of, the way that… Database.
The database vendor pages work.
**Matthew Hensley / Grafana Labs** 23:06 Yeah, I think it'll end up being just some…
When the non-normative pages, or at most, tweaking…
A little bit of the text, like.
Just defining fully qualified better, and… Constraining it down to…
The intention sum, so it's not so open-ended.
**Trask Stalnaker** 23:28 Woo!
Well, good luck.
**Steve Rao** 23:33 Sorry? Yeah, Chaska, I have a small question.
**Trask Stalnaker** 23:37 Yeah.
**Steve Rao** 23:37 Yeah, I put the link on the agenda.
**Trask Stalnaker** 23:42 Yeah.
**Steve Rao** 23:44 Yeah, can you see the… my comment about the client-side load balance?
**Trask Stalnaker** 23:50 Yeah.
**Steve Rao** 23:53 Yeah, it seems you don't, share the… your screen.
**Trask Stalnaker** 23:58 Oh, sorry, yes.
Service part, server…
**Steve Rao** 24:14 Yeah, and that's fine, yeah.
**Trask Stalnaker** 24:20 the service name from the registry. Service name…
Is… there isn't…
Interesting. So is this what you look up in the registry? You actually look up the…
**Steve Rao** 24:43 Yeah, yeah.
Yeah, maybe we can get, get the,
instance addressed by this service name in registry.
Yeah, it looks like a hostern name in HTTP client.
we can get the IP address by DNS.
**Trask Stalnaker** 25:06 Maybe, yeah. Now what does port mean here?
**Steve Rao** 25:11 Yeah, this is, a server-side service port.
Just like, yeah, the client will, well…
Get the server port by registry.
And, invoke the, server-side, service.
This is the port of the service.
**Matthew Hensley / Grafana Labs** 25:37 Okay. So…
**Trask Stalnaker** 25:39 Oh, go ahead.
**Matthew Hensley / Grafana Labs** 25:39 Quartz Concrete, and then the address is something that gets resolved.
Into an actual address.
**Trask Stalnaker** 25:53 Can you have, I mean, is this is the… Is this network peer port?
Or did you want this as server.port?
Like, when you, when you look it up in the registry.
Are you… is this part of the logical name of the service? Are you looking up the combination of these two things?
**Steve Rao** 26:22 Yeah.
**Trask Stalnaker** 26:26 What does this mean?
**Steve Rao** 26:28 Yeah, this is,
Yeah, IP, yeah, in the registry, and there is a map.
The, the key, it looks like, the, service name.
And, the, and, the value, is, is content, several, IP address and IP, port.
Yeah, this is, the, the, the server, port is, it's a service,
Our port is not the, network peer port.
**Trask Stalnaker** 27:18 the service work.
I'm still… a little… last…
**Steve Rao** 27:32 Okay, yeah, maybe I can, add more, example or ex- examination about this point later.
**Trask Stalnaker** 27:41 Yeah, that would be great. Kind of like, maybe an example of…
What does, what does client-side configuration look like?
For…
this, and sort of how these… yeah, that would be great, just some more detail, especially on the port, because I think I understand the other pieces.
**Steve Rao** 28:06 Okay.
**Trask Stalnaker** 28:09 Cool, thanks for following up on that.
**Steve Rao** 28:13 No problem.
**Trask Stalnaker** 28:19 Alright, well… Because we'll probably… we may as well keep this touchpoint, for the next…
Few weeks, see if we can…
Work, just in case there's any questions about, prototypes and getting towards stability.
**Steve Rao** 28:40 Okay.
**Trask Stalnaker** 28:41 But we could keep it short if there's just, just kind of, like, check-ins.
**Matthew Hensley / Grafana Labs** 28:47 Yeah, that sounds good.
We're precariously close to, having actual implementations before KubeCon.
**Trask Stalnaker** 28:55 I know, right?
Yeah, when is QCon?
**Matthew Hensley / Grafana Labs** 28:59 It's the end of March.
**Trask Stalnaker** 29:02 Okay.
**Matthew Hensley / Grafana Labs** 29:02 I think March 22nd? So, like, a month.
**Trask Stalnaker** 29:06 So technically, we will have been in RC for a month by then, so… It's not…
Unreasonable to say that we… could market stay… if we were ready and wanted the market stable before KoopCon?
Something to…
talk about another time. Oh, Linmilla's going to present the RPC SUMCOM RC work in the spec meeting next week.
Okay, cool. So, actually, that'll be good,
I'm curious her thoughts on… Stability timeline, if we have… prototypes.
**Matthew Hensley / Grafana Labs** 29:58 Yeah, next week, is that the, the Monday SimConf one, or the other…
**Trask Stalnaker** 30:04 Tuesday… Okay. Tuesday, general spec, yeah.
**Matthew Hensley / Grafana Labs** 30:09 Bye.
Cool. Just want to make sure I make it there, but it'd be fun if I could have, something…
that actually generates usable telemetry by then, just so we could… I know the Java one's pretty far along, and y'all are just working through
Sudden things.
**Trask Stalnaker** 30:29 Yeah… Yeah, yeah, no, that's a good point. I'll, see if we can have… like,
At least be able to… Advertise our current state there.
**Matthew Hensley / Grafana Labs** 30:44 Well, it's, one of those things where having at least one that's concrete to show off.
And is,
you know, it's like, what's the fastest way to get the answer on the internet? It's to post your question, and then to post a wrong answer.
**Trask Stalnaker** 30:58 Yes, yes.
**Matthew Hensley / Grafana Labs** 31:00 no one's gonna read the spec, but if you put up… if you show them a PR…
**Trask Stalnaker** 31:03 code.
**Matthew Hensley / Grafana Labs** 31:04 Yeah, they'll… they'll have something to…
Say, so I might get some better feedback if we just have
Something for people to go look at, and… Yeah.
**Trask Stalnaker** 31:14 Alright.
Till next week, then.
**Steve Rao** 31:19 Yeah, 6 weeks.
**Matthew Hensley / Grafana Labs** 31:21 Catch y'all later. See ya.
**Trask Stalnaker** 31:22 I…
