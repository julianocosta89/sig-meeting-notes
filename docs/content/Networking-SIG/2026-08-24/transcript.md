SIG: Networking SIG
Date: 2026-08-24
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

Giuseppe Ognibene (Coralogix) 00:01:18 Hi, Sven?
Sven Cowart (ElastiFlow Inc) 00:01:21 Hey.
How are you?
Giuseppe Ognibene (Coralogix) 00:01:24 I'm fine. How are you?
Sven Cowart (ElastiFlow Inc) 00:02:06 Giuseppe, what do you do at CoreLogix?
You work on… OpenTelemetry ecosystem for them, or is there other things you work on?
Giuseppe Ognibene (Coralogix) 00:02:17 No, no, mainly Obi.
Sven Cowart (ElastiFlow Inc) 00:02:19 Oh, cool.
Giuseppe Ognibene (Coralogix) 00:02:20 Nope.
Sven Cowart (ElastiFlow Inc) 00:02:22 I'm one of the co-founders of Elastiflow.
But… I work on everything there. We're a small company, so… Definitely in.
Giuseppe Ognibene (Coralogix) 00:02:35 in Australia?
Sven Cowart (ElastiFlow Inc) 00:02:37 Say that again?
Giuseppe Ognibene (Coralogix) 00:02:39 Are you in, Australia?
Sven Cowart (ElastiFlow Inc) 00:02:42 No, California.
Giuseppe Ognibene (Coralogix) 00:02:46 Because I said… Beth, sorry?
Sven Cowart (ElastiFlow Inc) 00:02:48 California.
Giuseppe Ognibene (Coralogix) 00:02:51 Because I saw the surf, the,
Sven Cowart (ElastiFlow Inc) 00:02:55 Yeah.
Giuseppe Ognibene (Coralogix) 00:02:55 table, and I thought it was afraid.
Sven Cowart (ElastiFlow Inc) 00:02:59 No, California and the U.S.
You're muted, Antonio.
Good morning.
Antonio Martinez (Cisco Systems, Inc.) 00:03:13 Hayden, sorry for that, I was… I'm dropping for another call, honestly.
Sven Cowart (ElastiFlow Inc) 00:03:23 Hey, Rob.
Rob Cowart 00:03:33 Oh, there we go, hey, sorry, I wasn't on, First call of the day, didn't have it all turned on yet.
Sven Cowart (ElastiFlow Inc) 00:03:45 I was doing the same thing.
Alright, I'm gonna share my screen to get us started here.
Start by making this smaller.
Okay, Antonio, you probably haven't gotten a chance to see what I've said yet in the latest message, on the, issue regarding network source and our destination that you opened.
I agree with you, I think it's not well clarified at this moment in time. And there's also, I think, for us, coming from a network background.
issues with how network local and network peer is being used and is defined currently in the ecosystem, and both of those kind of, I think, need to be ratified at the same time.
So… what I did is, and this is a lot more just explanation for when I present this to the semantic conventions group.
But I tried to define which of these things For what these things mean.
So, quickly reviewing here, client.server, primarily used L7.
It's very logical who initiated and accepted.
The guidance here.
And I think this is where some of the nuance comes in, and where I think, Rob, when we talked on Friday, I actually changed a little bit of my stance on where we should take this, because the guidance on client and servers is that it's de-proxied, meaning that it's behind Like, you're getting the address behind any intermittinaries?
So… and that's from… that's the language they use in the actual documentation, right? So, if you go down to this example.
On an app's inbound HTTP server, so right here… You'd have your client address of whatever this client here is, your server address, which in this case would just be its… URI, and then a network.
peer.address, which is actually the 10.0.0.9.
address, because that's the closest connected thing, and client would work the same way, right? The server would have this address, the networked up here address would be of the proxy, the load balancer.
So that's how it's being used today.
I think source and destination.
should I pause there? I see you grimacing.
Rob Cowart 00:06:33 So, I think we should make a note that that definition of it's always on the other side of the, Intermediator, proxy, whatever it might be.
Probably should be revisited.
Sven Cowart (ElastiFlow Inc) 00:06:48 Okay.
Rob Cowart 00:06:49 Just because… I guess it depends on what your definition of a server is, but my definition of a server is… you know, essentially a… process listening on a socket, which it is open for inbound connections.
Sven Cowart (ElastiFlow Inc) 00:07:06 It's not always on it. It's not always on it. It's not saying that, it's saying that if it is.
If there is a client-server talking, and there is an intermittent area, that You're not talking about that in the mid-air, you're not talking about the load balancer.
Rob Cowart 00:07:22 But again, I disagree with that definition at a network level.
Sven Cowart (ElastiFlow Inc) 00:07:27 Because you think the load balancer's a server?
Rob Cowart 00:07:29 Generally, what would say… what oftentimes happen is the client makes a connection to the proxy.
It then… the proxy then creates an entirely different connection.
to one of the servers it so chooses to, because, especially if it's load balancing and not proxying. And it's actually two distinct connections.
Sven Cowart (ElastiFlow Inc) 00:07:55 Yes.
Yeah, understood that.
Rob Cowart 00:07:58 Yeah.
Sven Cowart (ElastiFlow Inc) 00:07:59 Client and server are supposed to be logical, not the physical connections.
Rob Cowart 00:08:04 Well, I'm not even talking… I mean, technically no connection is physical.
Sven Cowart (ElastiFlow Inc) 00:08:07 Well, yeah.
Rob Cowart 00:08:08 But… I get what you're saying, like, I just, at a network level, disagree with that definition.
It doesn't… it doesn't speak to the reality.
Antonio Martinez (Cisco Systems, Inc.) 00:08:28 Honestly, I mean, deciding those, it's challenging, but I'm here with Sven in the sense that client service should be, like.
Not that network perspective here, this would be more like, what is your… API or URL that you are hitting, so that is gonna be the server that you're hitting.
You… we don't know what's in the middle.
At least this is how I see also.
Rob Cowart 00:08:56 Actually, I would… again, I'd just disagree with that statement. Like, let's say I'm running something in the cloud, whether it's one or multiple things behind it, and in front of that is, like, you know, load balancer, or whatever your, you know, your cloud provider chooses to call it. When you define that you are… you're hitting the load balancer.
That's all your client knows about. It has no clue what actually The load balancer connects the client to… on the back end, or to which it even creates an entirely separate connection to something on the back end, and Retransmits the request payload to.
It's literally two distinct network connections. And your client truly has no clue about the server on the back end when you have that type of scenario.
Sven Cowart (ElastiFlow Inc) 00:09:54 So no one's saying that that isn't the case by these definitions. Like, if you had a client span being generated.
In this scenario, our network.peer.address would be that load balancer that you just described.
Rob Cowart 00:10:12 Okay.
Sven Cowart (ElastiFlow Inc) 00:10:13 Right? And on that client span being generated out of here, the server.address would be whatever the URL is of that thing that you're hitting.
And you're right, it doesn't have any clue what the actual connection area is, but it knows it's hitting that address.
Rob Cowart 00:10:30 Right, which is the load balancer's address.
Sven Cowart (ElastiFlow Inc) 00:10:37 E… Yes.
Rob Cowart 00:10:39 It is. I mean, we could PCAP this. It is the load balancer's address.
Antonio Martinez (Cisco Systems, Inc.) 00:10:48 Correct, but we also need a way to describe the… the URL at the end, so I think that's the proper representation also.
Rob Cowart 00:11:03 I feel like if I was to view this, like, if I was looking at spans or something and wanted to view this, I'd want to see two separate spans. One from the client to the proxy, and one from the proxy to the backend server.
Which, by the way, most likely the proxy to the back-end server, like, the client in this case, the actual client, would be client, and proxy would be server. And for the second connection, the proxy would be client, and the server would… on the back end would be server.
Antonio Martinez (Cisco Systems, Inc.) 00:11:37 Yeah, I think everybody wants to hear.
Rob Cowart 00:11:39 Now, the question is this, and look, if these terms are already given, client and server, and they're used in this particular way, then I think we need to introduce a second set of terms, like initiator and responder.
That actually, in fact, there are some, Cisco implementations of things that actually use those exact words, initiator and responder.
I tend to think of those as the client and the server, but, you know,
Sven Cowart (ElastiFlow Inc) 00:12:15 What is that?
Rob Cowart 00:12:16 What's that?
Sven Cowart (ElastiFlow Inc) 00:12:17 What additional thing are you trying to solve for that's not being captured here? That's… I think I'm missing something.
Rob Cowart 00:12:27 So, yeah… perhaps I'm trying to be, semantically correct.
So what are you saying? You're saying that they say here the proxy is the pier.
Sven Cowart (ElastiFlow Inc) 00:12:45 Yes. Well, it depends where you look at it from, but yes.
Right. I mean, it… in your situ… what you just… what you said earlier is true, too. You would have two spans generated. A client span would be generated here, and a server span would be generated here.
Rob Cowart 00:13:04 Oh, I… I see what you're saying, but I was not necessarily referring to it in… what you're talking about with the two spans. I was thinking of flow spans.
Sven Cowart (ElastiFlow Inc) 00:13:16 You'd also have that.
I mean, if it works like Mermin, you would have that too. And in both scenarios, the peer address in this situation would be the proxy for both the client span generated here and the server span generated here.
And then it… I think that the point of tension, what it feels like to me, for you, is that server and client is just logical. It's not… like…
Antonio Martinez (Cisco Systems, Inc.) 00:13:53 They represent an HTTP con… not connection, the word, but they represent the HTTP here, request and response.
Rob Cowart 00:14:01 You're…
Antonio Martinez (Cisco Systems, Inc.) 00:14:01 And what housing?
Rob Cowart 00:14:02 So, I think that's the difference, is I'm thinking them… I tend to think of that as a network-level thing.
Sven Cowart (ElastiFlow Inc) 00:14:10 Yeah.
Rob Cowart 00:14:11 And this is referring to an application level thing.
Sven Cowart (ElastiFlow Inc) 00:14:15 That's what I try to call it here, right? So, this is used for L7, like, it's app-level information.
Rob Cowart 00:14:21 Okay, so I guess what's missing, then, is this is where I come back to. Where is the network level initiator and responder?
Looks like there's not one.
Antonio Martinez (Cisco Systems, Inc.) 00:14:35 And lookup and peer is the one thing today for that.
Sven Cowart (ElastiFlow Inc) 00:14:39 that would be it, and that's the second part of this whole comment I left, where it's like, we should.
Rob Cowart 00:14:44 But then… but I'm sorry to be pedantic here, but, like, Those are just terrible names.
Because if I'm looking at it from the… if I'm looking at it from the, like, I'm measuring, like, where am I observing or metering this… this activity on? So let's say I'm doing it on the server.
So, I'm gonna say, if local is client, and peer means the server side.
So I'm gonna say… I'm gonna say, so locals instantiator and peer is responder, is that what we're saying?
Sven Cowart (ElastiFlow Inc) 00:15:16 Wait, hold on a second. Before we go there, let's also, like, we're still gonna use source and destination.
Rob Cowart 00:15:22 No, but which has a completely different meaning. Yes.
Sven Cowart (ElastiFlow Inc) 00:15:25 Right.
Rob Cowart 00:15:26 Traffic is bidirectional.
Yeah.
Sven Cowart (ElastiFlow Inc) 00:15:28 But we could use, like, what BuyFlow does with IPFix, where it calls out the initiator and the responder.
As one of the fields.
Rob Cowart 00:15:38 That might be the other way to do it.
Sven Cowart (ElastiFlow Inc) 00:15:39 Good.
Rob Cowart 00:15:40 That's…
Sven Cowart (ElastiFlow Inc) 00:15:40 I was thinking about taking it, I just didn't want to add that in.
Rob Cowart 00:15:43 Yeah.
Sven Cowart (ElastiFlow Inc) 00:15:44 Because that's gonna make it even more complicated for people to understand.
Rob Cowart 00:15:48 I saw Antonio shaking his head when I was saying, like, if I'm looking at it from the server side, I would just have a real problem of saying.
the initiator is local when the… when… when if I'm metering it or observing it at the server side, it's literally not local. It's on the other side of the wire.
Antonio Martinez (Cisco Systems, Inc.) 00:16:10 And that's… that's where I wrote what I created that ticket, because for me it was also super confusing, and even it is, because now we have source, destination, network, local, and network here. But on the other side.
Networking local network PR from… based on our investigation that we did, it's stable, and it's been used across many instrumentation languages, and used… using other semantic conventions, in the sense, like, database, HTTP, a few others. So.
I think we just need to… Regard a little bit what that is, because it's gonna be really bad for us if we… We just duplicate it and then call it source and destination, or something along those lines.
Rob Cowart 00:16:51 Yeah, okay.
Antonio Martinez (Cisco Systems, Inc.) 00:16:52 That was my dear.
Sven Cowart (ElastiFlow Inc) 00:16:53 in my explanation of all this, so that I can get to the end, because.
Rob Cowart 00:16:58 Yeah, yeah, yeah, okay.
Sven Cowart (ElastiFlow Inc) 00:16:59 more clear then. So, source and destination, right? With the initiator thing, that's coming. I don't want to include that into this.
conversation and PR.
Like, because at that point, we're, like, defining flow… flow-related semantics about initiator and responder, and… I'm just worried that, oh, if we open up that bag, like, we'll open up a whole other bag of worms that we need to detangle in this one thing that we could get closed faster if we just focus on this.
Rob Cowart 00:17:28 So…
Sven Cowart (ElastiFlow Inc) 00:17:29 the… then Network Local Peer, the way it's currently used, right, is just… get the socket name, get peer name. It's actually being used more in conjunction with L7 information to, like, describe some L4 stuff.
That… where they're actually talking about the connections.
So there's two things that we need to do and clarify, and one is, I'm… I would like to just make it really plain and simple in the language and the… and the, the documentation.
Is how to decide which ones to use.
So, I gave my prescription here, but this might change based on what we decide on below.
And then part of that is actually, and this is the… more of the decision that we need to make.
Is that… Four source and destination addresses.
the registry already says to de-proxy it the same way that client and server is, but that's just not possible most of the time where you're doing flow observation, so… we need to make sure that language is… that is in the scenario that you use it for L7 metering.
and you can't figure out who the client server is. But what I'd actually really like to do is say, change this language to discourage the deep proxying of source and destination addresses, so that We can then… And then say, if you're metering things at… at the application layer, you should always be able to figure out who the client server is, and if you don't, then use, port logic.
Highest port is client, lowest port is server on a specific connection. But in most scenarios, you wouldn't even have to default to that. It'd probably be less than a few percent of times where you'd have to do that. So.
I actually want to change some… a little bit of the guidance there around… The fact that source and destination addresses right now are just being treated as a fallback to client and server, and really just being used for L7.
L7 fallback to client and server, and I don't like that at all. I think that's a bad move.
Rob Cowart 00:19:38 Can I ask a question here, Sven? Yep.
Just… just to make sure it's… we're fully covered.
What… I'm already trying to answer my question in my head, so let me just answer it. But… Would it… what would be the issue to say.
Client, server, source, destination, as is.
is a Layer 7 thing.
Network.ClientServer, network.source destination, is basically like a Layer 4 thing.
Sven Cowart (ElastiFlow Inc) 00:20:23 I don't think there's necessarily an issue with it, I just want us to scrutinize if it's necessary.
Like, it just feels like that… This then becomes even more complicated and confusing.
I think people would be like, wait, what, you want me to use network.source.destination versus source destination versus client? I feel like that would get tricky.
I mean, yeah…
Antonio Martinez (Cisco Systems, Inc.) 00:20:49 I like what Robert…
Sven Cowart (ElastiFlow Inc) 00:20:50 Yeah.
Sorry, Antonio.
Antonio Martinez (Cisco Systems, Inc.) 00:20:53 No, no, no, you're completely certain.
Rob Cowart 00:20:57 Okay, I just wanted to throw it out there, as… You know, as… because it is a possibility, right?
Sven Cowart (ElastiFlow Inc) 00:21:03 Yeah, it is. Yeah, we could go that way.
then… And honestly, I don't really think that many people are using Source and Destination. I know Obi is for their flow metrics, but outside of that, I don't really know what else in the ecosystem uses it. So…
Rob Cowart 00:21:24 I don't think it's as relevant for Layer 7, which makes your… Your suggestions, Sven of just dropping that particular requirement on those fields… Yeah. …makes that more viable.
Sven Cowart (ElastiFlow Inc) 00:21:40 So then… So, do we agree that we should push for re… Wording the language around Source destination.
And it's still in development, so that's one where we actually do have Rename it.
Rob Cowart 00:22:00 And is the suggestion, whether it's in this PR or not, that we would then, do a… Where's Chad on here?
For everyone's sake.
if you look at that link I just shared in the chat, that essentially we would add an equivalent to this buy flow director, direction field.
Sven Cowart (ElastiFlow Inc) 00:22:25 Yeah.
Yeah, I wouldn't do it in this PR, but yes.
Rob Cowart 00:22:28 Yeah, yeah, yeah, where basically we're saying… so… so we just stay at source destination… oh, thanks, Sam, for pulling that up, yeah. We just stay at source destination, and we have a… Third field that's related to source destination, which declares which one is the initiator and which one is the responder, basically.
Sven Cowart (ElastiFlow Inc) 00:22:51 Yep.
Rob Cowart 00:22:55 Okay.
Antonio Martinez (Cisco Systems, Inc.) 00:22:56 So what you are saying, just for me to understand, is, like, we are gonna always use a client and server for… L7, which is clear, and we're gonna be using Network PR, Network Local for everything which is Level 4 and below, and then Source and destination is gonna be only for the use case of the bi-directional, and then we are gonna put who started the… a connection?
with,
Rob Cowart 00:23:27 Well, yeah, I don't know quite perfectly.
Antonio Martinez (Cisco Systems, Inc.) 00:23:29 Is that right?
Rob Cowart 00:23:29 a local in the pier yet.
Sven Cowart (ElastiFlow Inc) 00:23:32 Yeah, I think we still need to talk about the local year one, but yes, otherwise, everything else checks out for me.
So that…
Antonio Martinez (Cisco Systems, Inc.) 00:23:42 I think people are gonna get super confused with, source and destination name space. That's only covering that small use case of the bi-directional.
I mean, which we need to support it, for sure, but maybe we can do it through the… Through the network namespace.
Sven Cowart (ElastiFlow Inc) 00:24:00 What… what would be the confusing part?
Antonio Martinez (Cisco Systems, Inc.) 00:24:04 I mean, the confusion part, in my opinion, is, like, people are gonna need to read that source and destination.
namespace is only used for the bidirectional connection, only for that one. The rest use local and peer.
Right?
Sven Cowart (ElastiFlow Inc) 00:24:22 Yeah.
I don't know why that would be confusing, though. Like, that clears it up, because I think it's confusing as is right now.
Antonio Martinez (Cisco Systems, Inc.) 00:24:30 Yeah, yeah, right now it's super confusing.
Rob Cowart 00:24:33 Is local and peer also a Layer 7 thing?
Sven Cowart (ElastiFlow Inc) 00:24:37 Well, it isn't how it's used today.
Rob Cowart 00:24:40 It isn't, or it is.
Sven Cowart (ElastiFlow Inc) 00:24:42 is…
Rob Cowart 00:24:43 It is.
Sven Cowart (ElastiFlow Inc) 00:24:44 Yeah.
Rob Cowart 00:24:45 Yeah.
In my opinion, good, keep it there.
It's just a shame that it says network on it, but…
Sven Cowart (ElastiFlow Inc) 00:24:55 I think… I think the logic is that I know this is not a physical wire connection, but… It's the difference between, at an application level, what is the thing I'm actually connected to versus what is the thing I'm trying to reach. And that's the difference between network.local and And, flying Doug.
Or client, and then server versus networked up here.
And that… I mean, I think it makes sense for it to be called network, because it is actually talking about a network connection.
like, thing I'm connected to, so I do get it.
I think maybe the shameful part is what the names are, but that just came from Linux. Like, we already looked at that.
So… So that brings me to the last one, right? Is that… for L2, L3 things regarding Network routing.
and, routing tables, like, things like PGP, OSPF, LGP, are… Those things, where are we going with that?
And I think there's 3 options. I really don't like this hybrid one. I think it's just more confusion. But there's just reuse.
Where we just say, Networking local can be used for Defining direct connections related to client-server spans, or for neighbors, or we create something new, and I just gave one suggestion here, we can define what the name is, but create, like, neighbor.local.address and neighbor.peer.address.
Rob Cowart 00:26:36 Honestly, I'm not sure in that context what local would… maybe necessarily mean.
No, I can't say that. Actually, I can't think of one scenario where I know that that would… What that would be.
Okay.
Basically, the point I had made to Sven was that you know, the… those… those terms like peering and stuff, peers, neighbors, especially in routing pro… like OSPF, they talk about neighbors. BGP talks about peers. And so they have very… those… those words have very common usage already in network world.
And so the… so… and that was kind of what brought this whole thing up.
Sven Cowart (ElastiFlow Inc) 00:27:27 So, yeah, the ques…
Rob Cowart 00:27:29 Okay.
Sven Cowart (ElastiFlow Inc) 00:27:30 You guys lean one way or the other to reuse and open the…
Rob Cowart 00:27:33 Peter, you and I talked, I actually thought about this a little bit, though.
And… Depending on the protocol, I don't know… the things that talk about neighbors, I don't know of any scenario that talks about neighbors where there's not a direct connection between the neighbors.
There are scenarios where there's peering, where there might be intermediaries that are essentially your… I mean, in a way, the kind of… I don't want to say invisible to, but, You might go through other things before you reach the pier.
Like, you have a route to the pier, you know?
so a neighbor and a peer, they're very similar, and I feel like… I know I told you last week we could just use neighbor for everything, but… There are a few scenarios where there is small nuances that are different.
And… I wouldn't want to confuse somebody, you know?
having said that, we could still use the words, like, if we're gonna have, like, say, network.bgp.peer. Okay, I think that's pretty clear what we're talking about.
You know what I'm saying? Instead of trying to normalize
Sven Cowart (ElastiFlow Inc) 00:29:01 But we think that.
Rob Cowart 00:29:01 It'll have to normalize across all routing protocols, basically.
Sven Cowart (ElastiFlow Inc) 00:29:06 Do you think that's better?
That feels…
Rob Cowart 00:29:10 If you ask me right now, my feeling is probably, but I need to kind of start building out a little bit more and review some of the work I already have on the back end to answer that more.
Specifically.
Sven Cowart (ElastiFlow Inc) 00:29:27 I think from the application of that data, it makes it more complicated.
Wrong.
like, like, if I… we talked about, this is important to be able to… draw a topology, understand it. Now I have to know that I have to look At a bunch of different places.
I get the address out of a bunch of different places instead of just one, and then look at a field like Routing protocol. That could be one of these that we… Support.
Rob Cowart 00:30:12 Yeah, I guess I'm not sure where… I'm not sure what that confusion would be, or that difficulty would be.
Sven Cowart (ElastiFlow Inc) 00:30:20 Just that you have information.
Information that is modeling the same type of value.
in many different fields, but the difference between them is just the protocol being used. That would be, like.
Rob Cowart 00:30:37 Yeah, I hear what you're saying. That's what I'm saying, like, I need to get into it a little bit more before I'm gonna take a 100% stance on that, you know?
Sven Cowart (ElastiFlow Inc) 00:30:46 That would be, like.
the equivalent there would be, for me, would be, like, a network.connection.type doesn't exist, but what instead what you have is a network.tcp.address, network.udp.address, and for every protocol there is.
Like, part of the protocol.
Rob Cowart 00:31:03 But that's a little bit different, because, like, I know the word protocol is in there, but a routing protocol, in a way, the better way to say it is… Essentially, a routing protocol is an application that runs on a network device.
And… and… Exchanges information to determine the routes on the network.
You know, exchanges information with other routers to… Learn about and determine the full set of routes on the network.
So, I was actually even thinking to myself, this morning, our… Are there basically spans for routing protocols? Like, traces, to know… to troubleshoot route… routing issues?
But again, I don't know that I have… that could be total garbage, what I just said, just because I haven't… I gotta get into it a little bit more, right?
just trying to think about what are the best places to express some of that information. I know that doesn't change the need for certain conventions, but… My… here's what I will say to you, Sven. My… Feeling is that if client-server is layer 7, And even network local and network peer are… predominantly talking about Layer 7, things, connections.
Sven Cowart (ElastiFlow Inc) 00:32:48 Could be Layer 4, right, if you're doing, like, metering.
By looking at packets, you could have some Layer 4 applications for it as well.
Today.
Rob Cowart 00:33:00 See, but that's where, in my mind, I'm saying, no, I'm just using source destination and buy flow direction.
Sven Cowart (ElastiFlow Inc) 00:33:11 Yeah, I mean, I get where you're coming from, yeah.
Rob Cowart 00:33:14 Yeah, so…
Sven Cowart (ElastiFlow Inc) 00:33:15 That's Right now, there's probably places where it's not being used like that, but…
Rob Cowart 00:33:21 Oh, I get you, yeah, I understand, yeah.
So my feeling is, if these are defined the way you sit, including client… or source destination not being with this weird Layer 7 limitation that was placed on it, if that was removed.
I feel like my gut right now, and I only say this is… non-specific as I am, because like I said, I need to get into that specific aspect a little deeper.
with the actual data to make sure it fits what we're hypothesizing about at the moment.
But my feeling is we could probably work around what's there.
Based on the definitions you've given.
Sven Cowart (ElastiFlow Inc) 00:34:08 Which one?
Rob Cowart 00:34:10 Client server, as defined right now, is talking about a Layer 7 thing.
Sven Cowart (ElastiFlow Inc) 00:34:14 No, I get that, but on local, I'm talking about the other one. Like, the routing would reuse, or create new?
Rob Cowart 00:34:21 Network local and network peer?
Sven Cowart (ElastiFlow Inc) 00:34:24 Yeah.
Rob Cowart 00:34:27 If it turns out there's a natural fit, it could reuse. If not, we can work around it.
That… you know what I'm saying?
Sven Cowart (ElastiFlow Inc) 00:34:36 No.
Rob Cowart 00:34:40 Network.routing.local.peer. Like, you know, there's always the ability in that, and still have normalization across all routing protocols, just have it under one higher level… Object, if you will.
Sven Cowart (ElastiFlow Inc) 00:34:55 Yeah, yeah, that's what I was trying to suggest to you.
Rob Cowart 00:35:00 I see, yeah, yeah, yeah.
Sven Cowart (ElastiFlow Inc) 00:35:08 Let me ask, It's kind of a dumb question, I just don't know the routing protocols well enough to know, but is there a scenario where this would need to be an array of sorts?
Rob Cowart 00:35:24 Not in the context… I guess it depends on the context, but not typically when we're talking about a neighbor. It's usually one-to-one relationships, right?
Now, a router might have a relationship with multiple other routers. That's super common, but… It's usually over its different interfaces.
You know.
So yeah, I don't… I don't think there's any need for that to be an array. Like, when I think of the different SNMP MIBs for… For those type of relationships, like, you're just not gonna have a… you'll have multiple instances for each pair.
So there's no need to have, like, one instance that has an array of values.
Sven Cowart (ElastiFlow Inc) 00:36:19 Okay.
Alright, I think we covered this.
Is there any other questions?
Rob Cowart 00:36:33 I do ask…
Antonio Martinez (Cisco Systems, Inc.) 00:36:34 Any extra…
Rob Cowart 00:36:35 having the clarity of the Layer 7 thing. I think that's the part that, to me, makes… would otherwise make it confusing. I think we should also, though, like… it's not just how do we want to define our stuff in the network SIG, but those… that recommendation back that they need to be more… and maybe it is more clear, but I don't… but it needs to be more clear that this is referring to an application level not, not a Layer 4 below-level thing.
I'm sorry, I think I might have… Talked at the same time as someone else, someone was saying something.
Antonio Martinez (Cisco Systems, Inc.) 00:37:16 I was mentioning, like.
what are we gonna do now? If we want to add new things for network, do we want to add it as network.local. Let's say, ESNumber?
prefix, or those things that we were discussing, they will be under network.logger, on network.p, right? That's… The way to go now.
Sven Cowart (ElastiFlow Inc) 00:37:40 I think it depends on… I mean, what I've heard is, we don't know yet, unfortunately.
Unless you're talking about… a Layer 7 thing.
I don't think we're gonna have the ability to change or deprecate local NP or under network.
Because it's stable and it's used everywhere. So either it's… we open up the definitions to be used… like, if you're talking, Antoni, about, like, you need to do something that's describing something happening at L2 or L3, then… It seems like we don't know yet, because we don't know if we're going to take the route of doing network.local and network.peer, or network.
Maybe it's routing.local.
Network.routing.p, right? That's… that's what I was trying to understand, what Rob was think… was thinking going there, but… Or if it's… Right.
Antonio Martinez (Cisco Systems, Inc.) 00:38:36 And why don't we reuse the SIG 1 as you have option 1, network.local and PR, also for L2 and 3?
Sven Cowart (ElastiFlow Inc) 00:38:51 I can't answer that question. I don't know why we wouldn't reuse that right now.
Rob Cowart 00:39:06 I have my very opinionated, feelings on it.
I just feel like those names are meaningless to anyone in network ops.
That would be my number one reason for not wanting to use them.
And the only word there that really… like, the only place they would have some use would be… For usages that are not… and mostly it's around routing protocols, for usages that are not the way they're used right now, today.
Look, let me say this. I will next… take a look at routing protocols, and we'll put that together next. So maybe let me show what I have for interfaces, and then for this week, for what I'll do, I can focus on the routing protocol one, because I think that's probably the main one that… Could have an overlap where those names might have made sense.
Sven Cowart (ElastiFlow Inc) 00:40:18 Makes sense. Antonio, do you have a different situation you're trying to solve that isn't.
Rob Cowart 00:40:22 Yeah, that'd be helpful.
Antonio Martinez (Cisco Systems, Inc.) 00:40:29 Is it… The scenario that we had was, like, okay, we have the IP of the… our destination, or our peer, as you know, but we want to provide more info, not only the IP. We have the IPv4, and then the IPv6, we have both of those.
In case the device have both, supported, let's call it. And we also have the prefix that we want to support, and then we also have the ESN number and ESN organization.
those were kind of the scenarios that we wanted to support, and that's why I thought, like, network.peer.whatever, like, prefix or ESM number, makes sense under that scenario, without the routing.
Rob Cowart 00:41:15 So… in… the way I've seen things done, I'm not saying OTEL-specific, just in general, the way I see those type of things. Essentially, additional descriptive metadata relevant to an IP address, like.
What's the name it resolves to? What's the ASN that it's part of? Et cetera, et cetera, et cetera, right?
Antonio Martinez (Cisco Systems, Inc.) 00:41:40 Not in my use case today, yeah.
Rob Cowart 00:41:43 You know, I would argue that those should be allowed to be additional attributes, on any… existing attribute that is an IP address, regardless of where it lives.
You know, what's… what it's under.
So, so just like, there should be… with, you know, client.address, or whatever, and there should be client.as, or ASN, or whatever, right? There should be networklocal.address, and networklocal.asn, and source.address, and source.asn. Like, any… anything that is an IP address.
Arguably should also support having those additional attributes.
Sven Cowart (ElastiFlow Inc) 00:42:32 Hmm.
Rob Cowart 00:42:32 at that place in the nesting, wherever that IP address lives.
Sven Cowart (ElastiFlow Inc) 00:42:39 That…
Antonio Martinez (Cisco Systems, Inc.) 00:42:39 Yeah, that's the same thing for me.
Sven Cowart (ElastiFlow Inc) 00:42:41 I would agree with that.
I don't… think that concept… I'm not saying they'd be against it, but that concept doesn't exist yet.
or concepts similar to… I haven't seen it in any of the hotel semantic conventions, where you… like, they have the concept of a prefix, like, client source, or client server, and I'm trying to… I have an PR open that introduces source and destination.
As a prefix to a bunch of other things.
Sists, but those are, like, Address postfix.
So, wherever there's, like, what you guys just… what you just said, As a post-fix to anything.
I… Like, the question to me would be, do I then… like, do we have to go through and add that to client serv… to client and to server?
spec, and to source, and destination spec, and to network.local.network.addressSpec, or can we just say, these are address post specs? They can be used in client server, da-da-da-da-da-da, right?
Like, that's… I think it's more of a documentation question than it is a…
Antonio Martinez (Cisco Systems, Inc.) 00:43:50 But do we want to add it under clientandserver.adders? I mean, at that level, Thank you very much.
Sven Cowart (ElastiFlow Inc) 00:43:57 Right.
Probably skip that one.
Antonio Martinez (Cisco Systems, Inc.) 00:44:01 But for me, like, in destination.
source and destination, and network, local, and PR, yeah, we should add it to the four of those namespaces, and duplicate them for sure, yeah.
That would be my aim.
Rob Cowart 00:44:15 Here is Antonio, about this particular use case, anyway, because it relates to something. This morning, I was also thinking about, like… to what degree… sometimes I feel like, when I've read through, and I've read through a lot of different issues and things now, and sometimes I feel like there are decisions that are… are suggestions, I should say, because I'm not going to say that I saw the final decisions, but suggestions that are made.
based on… The SYNC system, where the data that's receiving the data.
And to me, conceptually, OTEL is always about the transmission of… the data.
Not what you do with it once you get it.
And… and so I say that to say.
Antonio Martinez (Cisco Systems, Inc.) 00:45:22 Correct.
Rob Cowart 00:45:22 These particular things. I transmit the IP address. It's the job of the system that receives it to add whatever other stuff it wants to around that IP address. Like, I think that's a position that arguably could be taken.
Like, what is the need to transmit, for example, an AS number with every single IP address? Like, it's just gonna be… because let's face it, that doesn't change… it does change, but it doesn't change a lot, you know?
Antonio Martinez (Cisco Systems, Inc.) 00:45:49 No, no, no. Agreed, that's… that's optional metadata. For our use case, we want to provide it, because for sure we know, like, if we send it, let's say, to Dynatrace, or to DataTalk, or Rafano, whatever, they are not going to provide that, unless you provide some sort of scripting that pulls that from a public database, where you have, like, a… through an IP to an AIC number, or hostname. So, we have that data our customer wants, and we are really providing, but we want a way to standardize, so if tomorrow any other vendor there wants to also put that in their OpenTelemetry, they also put it on the same way. That's sort of my goal.
Rob Cowart 00:46:26 I see.
It does sound like, though, like that's essentially a way to try to… Fix the SIG system's deficiencies.
Antonio Martinez (Cisco Systems, Inc.) 00:46:38 Okay.
Rob Cowart 00:46:39 Yeah, yeah.
Okay, I just didn't know, like I said, I'm still learning here enough to know, like, I wasn't sure how… common or acceptable that was, if you will. So…
Sven Cowart (ElastiFlow Inc) 00:46:53 So do we…
Antonio Martinez (Cisco Systems, Inc.) 00:46:53 Truly, hello.
Sven Cowart (ElastiFlow Inc) 00:46:55 I'm gonna… I am gonna ask the duplication question.
Like, is it okay, like, do we just prefer to duplicate across those, or… Is there something we want to say where, hey, these can be prefixed by anything that Also represents an address.
Rob Cowart 00:47:15 I feel like, in particular, on IP addresses, a… like, if you were to ask me if I was creating this from scratch, right? I mean, think, like, JSON schema or something, right? I would define IP address, and the IP address type has all of these additional things that it could have as fields.
And then, when I say source.address is an IP address type, then it just has all that other stuff comes along with it, you know?
And then you don't have to document all over the place.
Because it's… it's automatic. And then later, if we decide, you know, IP address should also have, say, security zone name.
Okay, great, then I can add that to the IP address type, and I don't have to change everything else.
Sven Cowart (ElastiFlow Inc) 00:48:06 Yeah.
Antonio Martinez (Cisco Systems, Inc.) 00:48:08 I mean, it's the same, honestly, my way to see, but we just need to flood that, so we'll have, like, network.peer.address. Prefix, and then for the other one, the same, but… Logically, if you collapse all, is what you're totally saying, but this is just a different representation, making it flat.
Rob Cowart 00:48:28 Spons.
Antonio Martinez (Cisco Systems, Inc.) 00:48:29 But yeah, I think we all see, from the same perspective, as an object, like, where you're sending the data is there.
Is that others?
Sven Cowart (ElastiFlow Inc) 00:48:41 Okay, and I think you're asking that because of some of the other issues you've opened.
So…
Antonio Martinez (Cisco Systems, Inc.) 00:48:45 Correct, correct.
Sven Cowart (ElastiFlow Inc) 00:48:46 also digging.
Antonio Martinez (Cisco Systems, Inc.) 00:48:47 Those are under one.
Sven Cowart (ElastiFlow Inc) 00:48:48 Double-check it, but… I think the duplication question is number one, and then… If that's acceptable, we can… I think those should be easier, and just go, okay, add, add, add, add this to those things, and move on.
Alright.
Cool.
Antonio Martinez (Cisco Systems, Inc.) 00:49:08 Before… before we close here, what are we gonna do here with the… clarification between source and destination, and then network PR, and network others. Are we gonna create, like, a… a pull request where we explain that the source and the finish are focusing on bi-directional scenarios? Yes.
Sven Cowart (ElastiFlow Inc) 00:49:28 Yep, so I'll create a pull request.
that makes all those changes. I do have another question for the SAMCOM group, because they did bring up that they don't… right now, there's this… it's documented here.
The guidance on all this, which is the general attributes, and then there's these things about client, server, source, destination, and other attributes, and that's where… it's like a weird place to document all this, and they feel that too. So, I don't know if I need to change this, but mainly, this stuff is going to change, and then the actual spec for source and destination would change.
And I will… I can create that PR.
that… what I… I wanted to wait to create that PR until… We get clarification on if we're going to reuse.
this for routing or not? Because… that is related to all these changes. And so… Yeah, I just… I need to… I guess I just need, Rob, you to…
Rob Cowart 00:50:30 Yeah, I'll move on to that one next.
Fortunately, most of those from our own internal schema, I already have pretty close to what would be A schema, it just needs to be adjusted a little bit for some hotel-related things.
Sven Cowart (ElastiFlow Inc) 00:50:50 Yeah, okay.
what I would… what I'm gonna take on with that PR is it's gonna be mainly rewriting this whole thing, of making it very… Clear on what gets used by what and when.
So I can start that, and I will create a draft PR until we get the additional routing information, and then I'll present it next week in Semantic Convention SIG.
Yeah.
Alright, Rob.
Rob Cowart 00:51:26 Eat video.
Sven Cowart (ElastiFlow Inc) 00:51:28 We're good on that, right? I can move on.
I think we beat that one.
Antonio Martinez (Cisco Systems, Inc.) 00:51:33 Yep, I think it's clear enough for me.
Rob Cowart 00:51:35 as I'm pulling this up, Oh, I was gonna share my screen. That's fine.
I was gonna ask the question of, were we able to make some progress on, a repo?
Sven Cowart (ElastiFlow Inc) 00:51:53 Not yet.
Until we need it, I don't know… like, as… As long as we're still working in that network namespace.
I don't think we're gonna get a repo.
Antonio Martinez (Cisco Systems, Inc.) 00:52:10 Yeah, name, interface will be there, as it is generic in that sense, so…
Rob Cowart 00:52:16 So, okay, so… I personally just feel like I'd like a place that's a little bit more of a scratch area to work before I move stuff anywhere else, so…
Sven Cowart (ElastiFlow Inc) 00:52:31 Agreed, yeah.
Rob Cowart 00:52:32 So, I have shared… I made this… this is a public repo out of our organization.
And quite… so that… so that the rest of y'all can view, comment, or whatever on.
And we could… Sven… I don't know what GitHub allows us to do, but maybe even be able to add a few folks from here to… to… I guess you could clone and, fork and… do a PR that way, or whatever as well. I'm happy to work here until we figure out where that stuff is landing, that's all I was trying to say. I was trying to come up with something that everyone could participate on.
I can…
Sven Cowart (ElastiFlow Inc) 00:53:12 I can bring it up, I just don't know how they're gonna feel about taking out all the network stuff into a federated repo. I mean, it shouldn't be a problem, but I just haven't…
Rob Cowart 00:53:20 I thought that was what was suggested, though.
That's why I'm a little confused.
Sven Cowart (ElastiFlow Inc) 00:53:24 suggested is that some of the deeper network stuff… the conversation was about what is core and what is…
Rob Cowart 00:53:32 So basically, like, network interface or something might just be in the normal conventions. Yes. In the normal repo, but the, you know… ISIS routing protocol might be in its own.
Sven Cowart (ElastiFlow Inc) 00:53:46 Yeah.
Rob Cowart 00:53:47 Okay.
Sven Cowart (ElastiFlow Inc) 00:53:48 Honestly, that's not great, because that means… Like, we can federate the network namespace, or we can't.
Rob Cowart 00:53:55 Yeah, yeah.
Sven Cowart (ElastiFlow Inc) 00:53:56 So… I'll…
Rob Cowart 00:53:58 And I think it's… well, I don't know. I don't know how much work it is, so I shouldn't say that I think it's okay to pull the network stuff over into a different repo, but that could be a big pain also.
Okay, well, for now, I'm just gonna be working over here, and if necessary, we can add anyone in as we need to, however we need to, but this is public. So, So anyway, I'd appreciate, I didn't make this as a quick pull request, I just wrapped this up a little bit before the call, and there's still a little bit I have to do on it, but this is my first pass at what I would make as a suggestion.
Set of… semantic conventions for just network interface to get started.
And… I did move away from trying to worry about YAML files and stuff at the moment, because, a couple weeks ago, when I joined the entity SIG afterwards and was chatting with them, they were also, like.
don't worry about all that right now, just get them… write it in a Markdown file and submit it, and then can worry… once it's all kind of agreed to and fine, you know, the YAML stuff can come at the end, and I'm like, that's okay, fine.
Although I did borrow a lot of these table formats and stuff out of, the standard templates for things.
so, anyway, please take the time to give me a quick review. I guess, there's actually a PR for that that's here.
my assum… assumptions are that the… single identifying thing would be an interface name. I guess that's not the single identity, because they're also… an interface is going to be on a host of some type, so there's probably, like, a hostname or something, system.hostname or something from the… System SIG that would also be one of the attributes. I guess I probably need to add that later on the metrics as well.
But anyway, please go through this and take a look. The… Outside of the interface name, the other things are, marked as I thought made sense for recommended or opt-in, etc.
what's also here, as I was reading a bit more, I know we had the conversation, like, with bandwidth and things like that, as I was reading a bit more, It seemed that these would still be… they're not metrics, would be considered attributes, but they're not identifying attributes, they're only descriptive attributes, because they can change.
And that includes things like state.
Does that… so, and both here, like, again, I'm trying to figure out naming conventions and all. I think this is proper naming convention.
For that.
But, again, if anyone has any comments or knows better on any of these, feel free to speak up and tell me.
Then… I wanted to ask here a question.
To get started, these are all of the current IANA-defined network interface types. I actually have a handful of ones that are defined by the cable technologies, kind of governing body that I need to add here as well, which, I just… Ran out of time before we were gonna get to this call, but the thing I wanted to ask about was names.
I don't know, like, let's look at one of these down here, where we could use I guess, yeah, let's take this. AL5. Or do we want the thing you have to assign to be… like, these are all kind of more abbreviated?
Forms, and then there's, like, the more verbose form, but someone could argue the more user-friendly form.
Is there any, preferred… official preferred way to do that?
Like, should it stay this is the values that would be assigned and put on the wire, or do we want to use more, I'll call them prettier names?
User-friendly names.
Sven Cowart (ElastiFlow Inc) 00:58:43 What are the values that are used on the wire on the left?
Rob Cowart 00:58:46 Yeah.
Sven Cowart (ElastiFlow Inc) 00:58:47 I would use those.
Rob Cowart 00:58:51 I mean, they are gonna be more.
Antonio Martinez (Cisco Systems, Inc.) 00:58:52 they're.
Rob Cowart 00:58:52 act generally. And that's also the more, I'll say official.
Antonio Martinez (Cisco Systems, Inc.) 00:59:00 Correct, they are compact terms. I mean, the problem of… Putting a name that describes that is, like.
We are gonna be the one.
proposing that name, and we are going to be the one that need to maintain that name, and so on and so forth. So if there is already a standard that have data from a, let's say, from an API, I'm afraid we're not also infusing it.
Sven Cowart (ElastiFlow Inc) 00:59:22 Yeah.
Antonio Martinez (Cisco Systems, Inc.) 00:59:24 For sure, that table that you have here is quite useful. That provides, like, the snapshot of description, but that description is totally… And… Optional.
Rob Cowart 00:59:35 By the way.
Antonio Martinez (Cisco Systems, Inc.) 00:59:36 between them.
Rob Cowart 00:59:36 These are also in real… like, in S&MP, these are gonna be enumerations. You know, S&MP's gonna have the value 66.
And it means it's this kind of interface, and this is the official abbreviations for those enumerations, and then the more verbose descriptions. But… so we're gonna stick this way, then, which is totally fine. It actually… then I don't need to go back and change it all.
We actually do have User-friendly pretty names for these as well.
that, a more complete table of them that we happen to use in our product that I would be happy to add those in here, but I didn't, I just didn't know what was official. So if we want to leave them the way they are, we can leave them the way they are.
Sven Cowart (ElastiFlow Inc) 01:00:23 I've got… I think, Antonio, that's a really good point, is that there's gonna be some vendor who comes around and says, I want that point-to-point over land to be just point-to-point, and then They're gonna ask us to change it, and it's like, no, you can figure out what the display name is in your app.
Rob Cowart 01:00:39 Well, and I think we can also always fall back and go, if you've got a problem with it, go talk to the IANA and get them to change it. Yeah.
Okay, so we'll stick with that then. I… Sven…
Sven Cowart (ElastiFlow Inc) 01:00:57 I real quick touch on, oh, we're at time, at the start.
Wouldn't the state, if that's part of the entity, be a problem because it does change values, which would create a new time series if it goes, like, up, down, and now you have a.
Rob Cowart 01:01:12 No, because it's only descriptive, it's not identity.
If it's an identifying attribute, those are the only ones that specify a time series.
Sven Cowart (ElastiFlow Inc) 01:01:23 Got it, alright, that makes sense.
Rob Cowart 01:01:26 The last thing, real quick before everyone drops, I think I also handled this correctly for, for metrics, where instead of having, like, multicast in and multicast out, or multicast send, multicast receive, we use, and this is the existing network I.O. direction, to basically, essentially have ingress, egress, more or less.
So, again, if there's any comments on any of the text or any of these things, let me know, but I still think there are some things, especially from SNMP World, that could be used to generate events, but for me right now, that's kind of a to-do item. So, But if anything that's there, someone wants to comment on, let me know, and… If I did a decent job, then I'll continue with this style, let's say it that way. If not, then I'll have to fix it, and I'll learn something else about it.
Sven Cowart (ElastiFlow Inc) 01:02:25 Alright, thank you.
Antonio Martinez (Cisco Systems, Inc.) 01:02:26 Great job, by the way, proposing that. One quick comment, for metrics, do we want to add the unit as part of the metric name? I saw that you have some sort of network… Crazy.
Rob Cowart 01:02:38 That was a question.
Antonio Martinez (Cisco Systems, Inc.) 01:02:40 Right.
Rob Cowart 01:02:40 is…
Antonio Martinez (Cisco Systems, Inc.) 01:02:42 Because, bro.
Because already, when you are sending over a metric, you are also sending it the attribute, you are also sending the description, and also the unit. So the unit is already part of the what you are sending through the wire, so I don't think we need to put it as part of the title, so…
Rob Cowart 01:03:02 I totally understand, and I think I did that correctly everywhere else, like, interface unicast, and it's in packets.
multicast in packets, except… but I was like.
I guess I could call it throughput? Or, like, okay, that's a… but that's a good… that's a good thing to open me up a… make a comment on, so I can fix it. But yeah, I did think about that when I was like, that's kind of… It's repeating itself.
Sven Cowart (ElastiFlow Inc) 01:03:29 I think there's guidance on that somewhere, specifically talking about bytes that I've read at some point or another, so… Stevie, maybe… I'll try to find it.
Rob Cowart 01:03:38 Okay.
You mean where that's sometimes valid?
Sven Cowart (ElastiFlow Inc) 01:03:43 I don't remember.
But I remember reading and being like, oh, that's interesting, that's kind of a weird problem, because normally these metrics do end in bytes.
But I think the metric they… yeah, I don't remember, I don't want to misstate it.
Rob Cowart 01:03:56 Yeah, yeah, but I get your point, Antoni. Like I said, I felt like I did it differently here, and I knew that one was wrong, and that was actually a question I wanted to ask if we had more time, was, around that, but yeah.
Sven Cowart (ElastiFlow Inc) 01:04:09 on it, if I find it.
Rob Cowart 01:04:11 Okay, yeah, that'd be good.
Antonio Martinez (Cisco Systems, Inc.) 01:04:14 Awesome, yeah, it will take a deeper look. By the way, do you mind creating, like, a GitHubSuse link dot in the GitHub ESUS under our new board, and then we can add comments there, maybe?
No rush for that. It will… I can… I can access…
Rob Cowart 01:04:30 Do I need to make this… open this somewhere over on the hotel thing? Yep.
Antonio Martinez (Cisco Systems, Inc.) 01:04:35 Just… just put a link in the guitarist with the.
Rob Cowart 01:04:37 Oh, yeah, okay.
Antonio Martinez (Cisco Systems, Inc.) 01:04:38 That will… that will be fine for me.
Rob Cowart 01:04:40 Yep.
Alright.
Sven Cowart (ElastiFlow Inc) 01:04:43 Thank you.
Antonio Martinez (Cisco Systems, Inc.) 01:04:44 Possibly. Staywise.
