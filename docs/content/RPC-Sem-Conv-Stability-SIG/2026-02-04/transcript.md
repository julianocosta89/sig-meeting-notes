SIG: RPC Sem Conv Stability SIG
Date: 2026-02-04
Duration: 47 minutes
============================================================

## Zoom Recording Transcript

**Liudmila Molkova** 02:32 Hello.
**Trask Stalnaker** 02:34 Yes, I'm not outnumbered anymore.
**Liudmila Molkova** 02:38 Yeah…
**Trask Stalnaker** 02:50 Hey, Steve.
**Steve Rao** 02:51 Yeah, hi, folks.
**Liudmila Molkova** 02:55 Oh, no.
Okay, what mean?
**Matthew Hensley** 03:03 Hello!
**Trask Stalnaker** 03:04 If… if you're, jet lagging, I can share.
**Liudmila Molkova** 03:10 I mean, go ahead. I'm jet lagging, but I feel okay, but since you volunteered.
**Trask Stalnaker** 03:17 Yeah, I'll drive, I'll drive.
**Matthew Hensley** 03:23 I am, fairly jet-lagged myself, but I did want to come check in since I had to miss last week, and… Let's see where we're at, and if there's anything I can do to help.
**Trask Stalnaker** 03:34 Alright.
Let us see where we're at. We're… where we're at in general is… Very close to… Calling it RC.
I've seen that you and Lydnila doing some proofreading, which is great.
Alright… oh, but Milla has populated the agenda.
**Liudmila Molkova** 04:10 How do you know?
**Trask Stalnaker** 04:17 Are you claiming otherwise?
**Liudmila Molkova** 04:22 Nope.
**Trask Stalnaker** 04:24 Alright, let's… Let's see how our board tracking is… Okay… in other words, okay.
In progress… Let's get me on this… Oh, okay.
Yes, so we've got a couple of simple PRs, Matthew or Steve, if you can look at them… Yes, this is the… Target.
JRPC Target, okay, I saw that's on the agenda.
Double. Okay, that's on the agenda… GRPC mapping… okay, okay.
We've got postability… And… Okay.
Great, let's just… Tackled the agenda Double.
Steve, how are you feeling about this… Oh, I see, you're on it. Awesome. Yeah.
**Steve Rao** 06:00 Yeah.
I think he's okay, yeah. And I update the, the PR.
And, Yeah, I refactored the format of this semantic convention page, and I also removed Network-related attributes.
Yeah.
at first, yeah, I want to, remove them until, Ludomi, remove others, because, related attributes, seem like, the common attribute. If I remove it, it will remove other, such as gRPC or JSNRPC, something like that, so I want to, do it later. So I, I, I finish it, no, yeah.
**Trask Stalnaker** 06:58 Okay, yeah, makes sense. Was there anything… That you were unsure about, that you wanted to discuss?
gear…
**Steve Rao** 07:10 Yeah, here, this point. Yeah, Romero, you think, it's necessary to, to mention or highlight, the scenarios in, double registry address?
**Liudmila Molkova** 07:28 I… I don't… no, I don't have a strong opinion. It's more a question to you, like, if you feel… it… it's necessary. If you feel it's… it's… it's trivial, enough for… Then… okay, go ahead.
**Trask Stalnaker** 07:46 What I would look at, Steve, is look at this PR.
**Steve Rao** 07:51 Yeah.
**Trask Stalnaker** 07:53 This PR is… Server address… Is clarifying server address.
And, yeah.
**Steve Rao** 08:09 Yeah, yeah.
**Trask Stalnaker** 08:11 And so… In the… this is all under server address, and… I think it's… this is useful, this kind of came out of a couple weeks of our discussions, and I think it's not obvious, like… We could make… you could make reasonable choices in different directions.
But I think it would make sense to align double with this behavior.
Which is basically what we're saying here is.
**Liudmila Molkova** 08:57 So, I think DABA is somewhat special, and maybe, Steve, correct me if I'm wrong.
that… In gRPC, they kind of mix two things together.
this case of, okay, I'll give you the… what DABO calls it registry, like, I give you a place from which you would find out the endpoint.
Or I can give you the dead point itself. In case of gRPC, it's one thing, the target string.
In case of DABO, and Steve, correct me, there are two ways you can initialize client.
different APIs, different approach. One, you give it the URL, And then, if I understand correctly, it's the actual URL of the endpoint you're going to talk to.
Or you can give it a registry, and then it's just part of the registry style.
**Steve Rao** 09:55 Hmm… Okay.
**Liudmila Molkova** 09:57 Alright?
**Steve Rao** 09:58 Yeah, Yeah, I think the second point, yeah, it's not right. Yeah, I can… yeah, I can introduce something about this point. I end up a client.
Usually, we will, config a registry address.
And the client, well, query, server instance by the registry address. It will, communicate with the registrar.
a registry.
And get the correct server address.
And, yeah, when the client invokes the servo, it will use the server's address instead of registry, endpoint or registry address. This is, most, common use case. And another common case, without a registry. It will, yeah, maybe we can config a server, address.
And it will invoke the server by this address directly.
This is not… yeah, maybe this is an initial case. It's not a common use case.
I'm not sure I make a sense.
**Liudmila Molkova** 11:26 So you're saying that the registry address is the common case?
**Steve Rao** 11:31 Yeah And, but, for users, they don't, observe the, registry address, because, usually it will… a client.
will, get the server address by registry, address. It will communicate with the registry.
such as it will tell the registry, I want to, get the address for service A, and the registry will, inform the client, related address And so, for kind, Surely, it will use the server address provided by a registry.
To invoke the servo.
**Liudmila Molkova** 12:21 Yeah, so let's say you are right, like, somebody implements the semantic conventions, writes their own instrumentation.
And it's not you.
What… what should they do when… Registry addresses configured.
And I think I'd… like, I… My understanding was that they just wouldn't populate server address report.
Is it the case?
**Trask Stalnaker** 12:52 This is an interesting question that I think, could pertain to this PR also.
Is this when we're, yeah, that should not… Use actual network level connections.
Information… Like, if you… Did have a… if you were doing client-side load balancing, would we not… I guess, because server.address is the logical We've defined that as the logical server, not the… network.
peer.
address, or something, I forgot what we called that.
So, Steven, in your case, when the registry Does the… can the register send back multiple addresses?
**Steve Rao** 14:03 Yeah.
And the client will select one.
By load balance, algorithm.
To communicate with the servo.
**Trask Stalnaker** 14:16 So I think what we're trying to say is if it only returns one address, like, there's only one address that's representing your service, whether it's server-side load balanced.
Then you would put that in server.address, but if it returns multiple.
**Steve Rao** 14:42 Yeah.
In a registry, it will, yeah, return multiple address, but in client, it will, select one. And in Java instrumentation, implementation, we can get the correct one.
To come… to… to invoke, this will.
And, I, I, yeah.
According to my knowledge, there's several, Address means, a logical address.
And… Yeah, but I think in double scenarios, what we get is also the, Logic address, because, that is address, registered by server, by server service.
It's noted, network PR address.
**Trask Stalnaker** 16:08 Is that capturing the question?
**Steve Rao** 16:15 Yeah, I, I think, yeah, it is, individual, a logical address.
It's not, Physical address.
I think in our current, implementation, yeah, if you… yeah, maybe we can, go to our Java instrumentation, we can see how we get the address, yeah.
**Trask Stalnaker** 16:47 Yeah, I understand that we can. I think, what we… just, we have to answer maybe a SEMCOM V… Question… about… server.address.
Versus network.
peer address.
Winnett.
comes to… I mean, I… In general, I'm trying to think in general, server.address, versus network peer address.
This is… Often gonna be the name… this… VIN? Is it defined as… IP…
**Steve Rao** 17:36 IP address.
**Liudmila Molkova** 17:37 Yeah, I think so.
**Trask Stalnaker** 17:42 Oh, where is that nice diagram we had?
**Liudmila Molkova** 17:48 It's… somewhere… In general…
**Trask Stalnaker** 18:10 Okay.
2… Client.address, server.address, network.peer.address, Is the IP, okay.
**Liudmila Molkova** 18:29 And the definition says IP address, or… Unix domain socket name.
**Trask Stalnaker** 18:36 Okay.
And so, when… It's a good question. I don't really know, like, when you're doing client-side load balancing.
**Steve Rao** 18:51 Hmm.
**Trask Stalnaker** 18:53 I mean, I would… I guess you could do either.
Server names, or… Addresses…
**Steve Rao** 19:08 Yeah.
**Trask Stalnaker** 19:11 Yeah, we can get the two…
**Steve Rao** 19:14 information.
**Liudmila Molkova** 19:22 And it's… it's probably the main case that the… Local load balancing returns.
IP addresses.
Or other than… post names.
**Steve Rao** 19:39 Yeah.
**Trask Stalnaker** 19:50 Yeah, I would expect that to be the common case, just since it was kind of part of the point, is just then you don't need to do the DNS.
What is, if we did capture… At… The… so… if… If, on an individual request.
We knew which… Server it was talking to.
like, for HTTP, I guess this is where the difference between the physical modeling of HTTP versus the logical modeling of RPC.
Because with HTTP, we would capture the… IndividualRequests, server.address.
**Liudmila Molkova** 20:51 Yep.
So you're saying… Could we… Let's say we… Know that individual request.
Runs against some server address.
And it's… it's… it's a DNS name.
Well, low cardinality theme, whatever.
Could we record the server address?
I don't think so, and the motivation is… Oh, or… oh, I think we do this for a database, give me a sec.
So, I think we're saying that for retries, in case of retrice, because it's a logical thing, that for retrice, use the latest The latest network peer address.
And for the database separation involved multiple network calls.
The address of the last contacted node should be used.
**Trask Stalnaker** 22:27 Okay, and this is… okay, so this is… and this is specifically for network peer address.
**Liudmila Molkova** 22:37 Should they say the same investment in RPC? Let's see…
**Trask Stalnaker** 22:45 I think… Oh, and that would give a… place to capture that? What… For the client load balancing case, because it kind of sucks not to have any server.address.
Since that's often used as, like, a map, tracing map.
Do we… what do we do for… Do we… we must have network.
Pure address…
**Liudmila Molkova** 23:20 We have it, we just don't specify the retrace.
**Trask Stalnaker** 23:25 Yes.
So I think what we're suggesting, Steve, is that server.address… That you wouldn't capture server.address if the client is load balancing over multiple servers.
But you would… be able… you would capture that data in network peer address. This would be… the individual… specific… IP that you… contacted.
**Steve Rao** 24:16 Yeah, sorry, yeah, can you repeat, it again? I want to follow it.
**Trask Stalnaker** 24:22 Yeah, so in client-side load balancing, if the registry returns a single… Address?
Then you could put that in server.address.
**Steve Rao** 24:42 Hmm.
**Trask Stalnaker** 24:43 If it returns multiple then you wouldn't put anything in server.address But you, would put Each… on each request, you would populate network peer address with the server that was contacted.
**Steve Rao** 25:06 Yeah, I have a question here. Yeah, you mentioned, yeah, we showed, Do a different, Dl wheels, according to the registry's return.
You mean, yeah, maybe we should, do a different process according to the registry return, if it's returned single address.
we should, set it in server.address. And if, Register returned multiple addresses, and the client will, do a load balance to select the final one.
we should, set it in network PR address. You… Is… is correct.
**Trask Stalnaker** 26:04 That's what we're… yeah, pos… I think, yes. The one thing that, I mean, It's a little ambiguous, as maybe that one If it's returning… I guess it's fine if it's only returning one.
Like, it… I could see that, hey, if you're doing client-side load balancing, but you only happen to have one IP address fed to you.
Then, is that really a logical… service.
Maybe not.
**Steve Rao** 26:46 But I think, in another case, the registry returned multiple addresses, and the client selected one address finally.
And it's a, address.
It's… it's also a logical address.
Because it's the address, it will communicate with the servo.
I think, this is no different between the first pace.
**Trask Stalnaker** 27:19 Yeah, so we might want to say, basically, that any form of client load balancing You don't populate server.address?
Because server.address… you don't have a… in that case, you don't really have a logical address for your service.
**Steve Rao** 27:42 Okay, but, yeah.
According to my knowledge, the, the logical address, it also can be an IP address.
And, just the address is not, real network address is okay, because, in some cases, there is, a proxy.
And, a network PR address is, means, a proxy address.
So that, yeah, for example, in client server scenarios, if the, yeah, if we're, in the middle, there is a proxy, and the network PR address is a proxy address.
But, if, Yeah, if, without the, proxy, the, server address, it means the logical address.
So, in the second scenario, if the registry, returned multiple addresses, each, data, server address instead of the proxy address. So, if we get the final address by load balance, it's also the, logical address, I think.
**Liudmila Molkova** 29:13 it's okay for server address to be an AP, because if it was provided as an AP, right, so if I'm saying, okay.
double… Url is… and provide the IP instead of the… DNS name. It's just because there is… there is literally, like, no good means for us to even care about it.
but… For the proxy case, I think what Trask is showing, at least for HTTP, we… we can… We, we know… that… There is a proxy, the forward proxy, right?
**Steve Rao** 29:58 Hmm.
**Liudmila Molkova** 30:00 And… When we call proxy, we actually provide the… boast, like, you send a request to proxy, but you say, actually, it's to the server.
It's part of the request.
What?
in case of… RPC, it's… it's slightly different, right? And your registry Can?
**Trask Stalnaker** 30:37 What would you do… I think the point she was getting at is, what if the RPC client was also going through a forward proxy?
then… And it was… you had a IP address, you had… you were doing client-side load balancing.
Plus a forward proxy.
If you don't put the… What would you put in network.peer.address, then?
You would put the forward proxy… In there, since that's the pier.
But you wouldn't… where would you… you wouldn't really have somewhere to put the… server's IP address.
That you're talking to.
**Liudmila Molkova** 31:40 When you make a connection, you make a connection to one thing, right? You don't make a connection to two different things at once.
well, at least you. You send the request on a specific connection, and this connection… Network peer address should be used, whatever it is.
**Trask Stalnaker** 32:04 Right, so here, let's… let's… So, say we're doing client-led balancing… across… We have… Not a forward… Proxy… We make a request, peer network.
Pure address… is… Dot.
Because that's our immediate peer.
Do we capture… Anything… If we say that for client-side load balancing client-side.
Load balancing, that we don't capture server address, then we leave this blank.
**Liudmila Molkova** 33:26 searching… I… Well… Nicole, the key question, is it a… is it a valid case at all? Like… Do you have a proxy end also?
quiet side-law balancing, you know. Why would you do this to yourself?
**Trask Stalnaker** 33:59 So, maybe we can talk about what are the… what are the harms of capturing a non-logical… server address in server.address.
**Liudmila Molkova** 34:17 Cardinality.
The one and the only.
**Trask Stalnaker** 34:23 I was curious about, I saw your comment, and I mean, you were adding that, so… So we don't include network.peer… Let's see, client… Mmm… Oh, this is experimental, though, so…
**Liudmila Molkova** 34:54 And we have a bug on it to remove it, to make it opt-in.
**Trask Stalnaker** 34:58 Okay, okay, so it isn't… it is a problem.
Yeah, I was surprised that that was a cardinality problem.
Like, how many… I mean, over time.
I guess if you're aggregating over… a good period of time. I guess that's the problem.
Makes sense.
backends want to. It's not maybe a problem, and the SDK is so much.
**Liudmila Molkova** 35:38 We don't… we don't include it on the… Request duration.
The contest, stable metric.
**Trask Stalnaker** 35:48 Yeah, yeah.
**Liudmila Molkova** 35:50 And I think we intentionally put it on open connections, because you kind of want to know how many connections you have per endpoint.
It's, like, a low-level metric.
But even there.
It's… Questionable.
**Trask Stalnaker** 36:16 And so, presumably, when you're doing client-side load balancing, via… a registry service.
you're… getting random IP addresses as… Pods, things spin up and register themselves with The registry service as service… potential service endpoints.
**Liudmila Molkova** 36:49 Yeah.
And also.
We… If we wanted to record… this. We would record it as a network peer address. Yeah, there are maybe some edge cases where we… Wouldn't be able to capture all we have, but… but… It's just a very complex case.
**Trask Stalnaker** 37:37 Yeah, and potentially at that point, you could drop to… physical… So if you were doing physical layer, like, for HTTP, I mean, do we have… I guess we don't really… HTTP… instrumentation could suffer today from that, like, if you're doing client-side load balancing on top of an HTTP instrumentation, we would capture the IP address as server.port.
**Liudmila Molkova** 38:21 We could. We capture whatever was provided in the URL, right, or the header.
**Trask Stalnaker** 38:26 Right.
**Liudmila Molkova** 38:31 I see what you mean, yeah. But this is logical.
I actually wanted to ask, Steve, so, yeah, we will, like, if, in the case of registry.
We most probably… Can't populate server address.
Should we also add something like double registry address?
As an attribute.
And then, if we record this along with Server address. Probably either one of them.
Or maybe there are cases when there are both.
Would it be… would you be… would you care about anything else at all?
**Steve Rao** 39:20 Yeah, you mean, yeah, in registry scenarios.
The idea is to, populate… to add the registry address to the server, dot address.
**Liudmila Molkova** 39:37 No, no, no, to edit as a separate attribute.
**Trask Stalnaker** 39:41 Just like the gRPC.target.
**Liudmila Molkova** 39:44 Pr.
**Trask Stalnaker** 39:45 You could have a double dot registry.
**Steve Rao** 39:49 Hmm. Oh, yeah, I think, I think it's okay, but, Yeah, it can provide additional, information for you, sir.
Yeah, I think we can do it, but… Yeah, I'm open to it.
**Liudmila Molkova** 40:12 Yeah, and then the server address, you just want provided a place to.
Typical case for the registry.
**Steve Rao** 40:25 Yeah, yeah, You may… yeah, I understand your concern, yeah, in… if we, put the… address from registry to the server.address, it will cause a cardinality prevalence in metrics.
is cracked.
**Liudmila Molkova** 40:50 If, if we provide, like, so when, when you, when somebody configures Registry address?
Then, registry address itself is not the right thing.
You put in the server address.
But then… Yeah. The registry would probably return IP addresses.
And we can record the actual address used.
In network PR address.
**Steve Rao** 41:21 Hmm.
**Liudmila Molkova** 41:22 And we will then leave server address without value.
**Steve Rao** 41:28 Okay.
So, okay, I understand. You mean, we shouldn't, use the server address to, to, to set the… IP address.
Returned by a registry.
Mmm… Yeah, I think, yeah, I think, yeah, it's okay, but, yeah.
Yeah, this is a different, between, my 12 hours thinking.
**Trask Stalnaker** 42:07 Yeah, I do think it would be worth, kind of, Trying to get a little bit more visibility on the client-side load balancing.
Question… from… Just almost awareness from, backends.
Who are using server address to draw… Connections… that I think some people would be surprised that we wouldn't… I think some people may be surprised that we don't capture server.address for, like, an RPC call.
**Steve Rao** 42:55 Yeah, yeah.
Yeah, because, Yeah, it's a… A bit different between the other semantic convention.
**Trask Stalnaker** 43:12 So don'.
**Liudmila Molkova** 43:13 Oh, software.
**Trask Stalnaker** 43:15 Go ahead.
**Liudmila Molkova** 43:18 Do you feel the same for GRPC?
**Trask Stalnaker** 43:24 I, I, I mean, I just… I think that some people will be surprised, not saying necessarily it's… a bad… Way to go.
I just think that, So that's where, if we had, kind of a general… and, like, thinking of, backends, like… Do they have to deal with this for… each different… semantic invention, like gRPC, you would fall back from server.address to… gRPC.target.
As your, sort of, map… something, Your distributed flow, map.
For a Dubbo, you would fall back to… Double.registry.
Or is there some.
**Liudmila Molkova** 44:30 Or in Mongol, you would fall back to Delhi stuff.
IP addresses, or the main… names configured.
Yeah.
**Trask Stalnaker** 44:45 Yeah, is there something… Better that we can do.
I think we haven't really run into this.
Yeah, previously… Because database… is… I mean, I guess if we had dug into some of the databases, definitely do client-side load balancing and, like, I mean, Cassandra, that's common, you know, but…
**Liudmila Molkova** 45:22 Yeah, and we didn't stabilize it. We didn't stabilize any of the databases that had this problem.
**Trask Stalnaker** 45:28 the NoSQL.
Yeah.
**Liudmila Molkova** 45:32 Well, at least a bill… no.
Yeah.
Right.
So, I think the way to make progress then would be to maybe come up with some proposals and ask around.
Yeah, I can try.
**Trask Stalnaker** 46:01 Well, yeah, let's at least, we can… Have some… discuss it, Try to float something, discuss… or discuss the general problem, and…
**Liudmila Molkova** 46:15 some columns…
**Trask Stalnaker** 46:17 Meeting, and or spec, and or… next week. Like, I don't want to derail everyth, like, with our, you know, famous last-minute surprises.
But I do think it's worth a week of trying to get some more input.
**Liudmila Molkova** 46:41 Yeah.
But then, let's, let's keep, the gRPC target open then.
And… The mapping is blocked.
Un… Dot.
**Trask Stalnaker** 47:07 Yeah, do you want me to, block it so it doesn't get… Excellent.
**Liudmila Molkova** 47:13 Yeah, go ahead.
**Trask Stalnaker** 47:14 in the…
**Liudmila Molkova** 47:15 Yeah, go ahead, because it's now ready to merge, and somebody can just hit it.
**Trask Stalnaker** 47:24 Alright.
Good discussion.
**Liudmila Molkova** 47:27 Yay! Thank you both.
**Trask Stalnaker** 47:30 So close.
**Steve Rao** 47:31 Thank you. Thank you all.
**Trask Stalnaker** 47:32 Alright.
**Liudmila Molkova** 47:34 Take care, good to have you.
**Trask Stalnaker** 47:35 Have you back. Yep.
**Liudmila Molkova** 47:37 Thanks.
