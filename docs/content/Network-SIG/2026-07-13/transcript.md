SIG: Network SIG
Date: 2026-07-13
Duration: 77 minutes
============================================================

## Zoom Recording Transcript

Sven Cowart 00:05:36 Check, check. There we go. Sorry. I was having tech difficulties on my end.
Antonio Jimenez 00:05:42 Everyone?
Good morning.
Sven Cowart 00:05:46 All right. Doc.
Unless there's something else, I think this is, Rob, you had more something to discuss.
BLA, that you wanted to show or present, or have a conversation about.
Antonio Jimenez 00:06:09 Yeah. You're muted, Rober.
RC Robert Cowart 00:06:15 Oh, sorry. I said, I said, I need just a minute, Sven. I don't know if, and I'll start in a But if anyone else has anything they need to bring up in the meantime.
Antonio Jimenez 00:06:27 I would like to know, Sven, what's the status on the project proposal, like, for the… the request, and you have to weather?
Sven Cowart 00:06:35 I just need to make a few updates, but I was waiting until this call to clarify some things around what I need to update. So, it's just the same updates we discussed last week, in addition to the stuff we're about to discuss here.
Antonio Jimenez 00:06:54 Great, thank you.
Sven Cowart 00:06:55 Yep.
I'll be right back.
RC Robert Cowart 00:07:13 And.
Okay, the first thing I'd be curious about before I share my screen on some things is, I'm curious… If, Anyone happen to put any thoughts into this particular area in the meantime since we last spoke?
And I'm just asking, like, any random ideas or questions or thoughts that, you know, you might have had.
And I ask that because as I… as I kind of talk through some of my own here, then, you know, I could potentially… Bring up, or reference, or try to tie any of those things in.
Antonio Jimenez 00:07:57 Which area specifically do you mean, Robert?
RC Robert Cowart 00:08:00 And, like, what are the different network entities that, you know, we're thinking about, like, a first pass of entities and the relationships they have, etc.
Antonio Jimenez 00:08:13 Okay, I see.
RC Robert Cowart 00:08:20 Nobody? Okay.
Antonio Jimenez 00:08:23 I mean, we can… we can talk about the, like, different entities, like server, for example, like… a client is talking with a server, I think those are one of the… And… fundamental of network also, which I think we're gonna start one day, and don't have to be today, but we're gonna start maybe with… Those kind.
RC Robert Cowart 00:08:45 Okay, that's a I'll make a little note here.
on that particular item.
Okay, let me.
Let me share my screen here.
All right, First, I'm gonna… I'm gonna… Do a minor rant for a second, and it's more of a begging for any tips if anyone has them. But, you know, I know there's certain work that's happened in this area of entities, and I was.
And I've seen screens and screen shares and stuff, and I was trying to find more stuff that I could tie into here.
but my gosh, sometimes it's, like, really hard to find stuff in the, you know, in any of the documentation, or in particular repositories. I think that's what I'm getting challenged with a bit.
is just the… And I have a suspicion where some of it may be, but like, stuff that's not, like, yet published, because it's not yet done. It's, like, work in progress, so it's gonna be living in GitHub issues and things like that, as opposed to, like, in the proper OTEL documentation.
I'm finding it, like, impossible to find stuff that I know has to exist. I don't know if anyone has any tips on that would be extremely helpful, but, so I'd hoped to bring a little more, of the hotel-ness, for lack of a better word, into a few things to talk about, but I just was struggling to find much, and I know it's network, so some stuff might not exist, but I know, like.
I've heard that the entities group in part of system already has, like, a network interface. Well, I can't find it anywhere, if they… in anything, if they do, so that's, something I'm gonna have to figure out how to better find things, so… But anyway, all right.
So… Last week, when I said we, like, entities, one of the things we said is, like, okay, let's just focus on enterprise networking, or, like, enterprise data center WAN networking.
As a starting point, partially by doing that, we also eliminate in that first pass… well, first, I think we pick up the areas of infrastructure that OTEL currently is most related to.
you know, in systems and applications and all that kind of things, and we eliminate having to worry initially about certain technologies that enterprises typically don't care about. You know, like, a great example would be, like, a global MPLS backbone. You know, that might be something that a service provider has, and some enterprises do. I mean, I know a number of enterprises that, you know.
That buy like literally raw bandwidth, raw fiber and run their own global networks. But they're definitely the the exception rather than the rule, right? So, so just trying to, you know, keep a certain scope of things. And then, so at a high level, then thinking about what some of the entities were, and, and basically these are more like kind of notes to myself, thinking about how do we slice and dice and break things up.
Into, into different groups or groupings of things, just trying to organize how that overall entity model or relationship could look like. And I think essentially the way I'm thinking about this is that there's actually, and a couple of this we've talked about, but there's actually kind of three primary categories that I think Most of the stuff can be grouped into.
Traffic is, you know, the actual traffic traversing the network.
Of which, you know, when you look at any given spot on a network, you're gonna either see, like, raw application traffic.
You're gonna have some type of tunneling or encapsulation or something like that, which usually is containing Application traffic, there's kind of a, a recursive thing here, in that, you know, a tunnel could actually have another tunnel in it, which could actually be, like, an IPv4 and 6 encapsulation, which is actually carrying application traffic. So, you know, there's a… there's a layered approach that could be there.
But you're also, on the network, going to have control plane traffic. So, you know, your typical… Things like, you know, ARP and LLDP and, Routing protocols and things that also are associated with your different networking layers.
So, and the control plane stuff was something that really, when we briefly were talking through a few things last week, we were talking about, like, application traffic, or just, you know, traffic in general, but not really broken it down into different categories of, or groupings of things to think about.
Okay.
And the reason I talk about these higher level groupings is because it kind of matters for some of the entities, you know.
then there's the… I'll call them the systems that are… that traffic is going to and from, and of those, it's pretty much endpoints, or things that forward traffic. So, you know.
routers, switches, etc, they forward traffic, and typically, servers are endpoints. Now, routers and switches actually can, in a certain flow of traffic, be endpoints themselves. Like, if you SSH to a switch.
the switch is the SSH server, right? It's the endpoint of that SSH connection, but that's unrelated to the switch's forwarding function.
You know, so, a system… We'll always be at least an endpoint in one way or another, but when we're talking about network devices, there's also, you know.
forwarders and things. And there's also, arguably, like, if you take a… like, let's take, like, a VMware server, right? And you have the vSwitch and the VMware server. Well, the vSwitch, it's in software, but it's still a forwarder.
And the VMs… Or, like, the endpoints, you know?
So, so whether virtual or physical, and I… and by the way, that kind of applies to a number of things.
here that we would talk about is that, my thoughts were, as I was thinking through a number of things, like physical and virtual, whether it be Physical and virtual network interfaces, or it be, like an Ospf. You have Ospf neighbors, and you have Ospf virtual neighbors and Ospf interfaces and Ospf virtual interfaces that those in general can be differentiated by a type and don't need their own entities. So my assumption in most of this is that We can simplify the entity model a lot if we are going down this path of saying, unless we come up with something where this just doesn't fit, and I haven't yet, and as I've been thinking through it, I think in most cases, both physical and virtual things can be treated with the same set of Identifying attributes, metrics, things of that nature.
Okay, and then… I don't know how this will play exactly into the… the entities thing yet, but, you know, typically in network, a lot of times we're thinking about, You know, you have like forwarding or data plane, if you want to call it that, and control plane where, you know, control plane is like the example of SSHing into the switch and the different commands and some of the low level protocols that are, for example, down here we have like, I have like spanning tree.
As a entity type, but that's more of a control plane type of… You know, communication happening between the switches and things, and less so of a, of, like, real data, you know? So it would be control plane traffic, it wouldn't be, like, application or tunnel traffic or anything like that, right? So these are kind of these broad categories that I've been thinking about as where we would start to… we could start to group for tag or otherwise identify certain entities with.
If I sound a little bit vague when I say that, that is actually a bit intentional, because I just feel like there is a good bit of Like, gray area between things. I'll give you an idea. A network interface?
Most people would say the network interface itself is a layer 2 entity.
But I can assign a network interface an IP address. And that kind of… that assignment kind of makes it… over to the Layer 3 area, because IP is a Layer 3 thing, right? So, you know, the reality is it's probably not even properly placed there. It should be placed somewhere, you know, across the line slightly. It depends on which part of it you're talking about, you know?
So… Okay, so with that said.
Anyone have any thoughts or comments just about this, or, like, where they say, like, oh, Rob, you really missed this one particular category of stuff?
Antonio Jimenez 00:18:53 Not that I can think right now, but you mentioned before, entities, at least the way how I see it, like, entities are… the generator or the receiver of that data. Like, if you go to HTTP, it will be, like, the destination place, or on the… the server, or the application. So, I think… you're doing here a great job in the sense, like, encapsulating IP, sorry, IP subnet, or also interface, or BGP.
For the other, I am not that experienced, so I cannot tell, but session is also a great one, so for sure, I'm more willing, I mean, that's my starting point.
RC Robert Cowart 00:19:32 Yeah, yeah, yeah, I mean, I wish I would have been a bit further actually in this, I just.
Yeah, it was a time issue for me here, you know.
Antonio Jimenez 00:19:41 What's up?
RC Robert Cowart 00:19:45 And by the way, I just tried to focus on identifying or descriptive attributes here, like all metrics and all kinds of stuff like that is… can come later. This was just more like trying to identify, I think I had shown before, jump over here to my Miro works a bit better with the trackpad sometimes.
Whoop, like, this was an example of something we had been playing with internally before. So I also want to get all these relationship, or different relationship type things, in here. This was actually something where I was, when I was saying before about data model.
When I was, trying to find Like, I just cannot find anywhere that has, Any definitive information about the different relationship.
Types.
That have been talked about so far. Like, there's some examples here about, like, part of… And… and occasionally you'll see examples, but I don't really see a particular list at the moment. I'm gonna go on the entities call later today, and I want to ask about that, where that kind of work is at. Because I… I suspect that we will end up with a lot of… You know, we'll add to that relationship thing quite significantly, if you will, you know, so.
Okay. But I just didn't get as far with some of the examples that I wanted to have. But I did want to talk about just a few things, just as an example of where things are going and could go.
And that, okay, network interface, I think, is probably the most well-understood, And we'll have to coordinate with the systems, SIG around this, because I think that's, that is probably is, if we're thinking of like system as, as whether it's virtual or physical, but basically a box, right? And, and the hardware related to that and the, whether again that's physical or virtual, you know, it probably is in the context of system where network interface, should reside. We do, though, probably want to make sure that the different attributes that are, being… Defined for that particular, Type, or for that particular entity, if you will, are… Also gonna meet what our needs are gonna be.
And then, where it starts to get a little more gray, I think, is when we get into… from a network perspective, like, from a systems perspective, there probably is not as much about certain protocols that the inbox cares about.
or information, like IP address, for example. But for networking scenarios, we actually care about more than just an IP address. We also want to think about subnets, which is, you know.
These IP addresses assigned to network interfaces, they all belong to one At least one subnet. And I say at least one, because, you could… There's a I haven't gotten far enough yet, but I've been thinking through a lot whether… we want to… Whether we will want to think of a subnet and a route as the same thing.
And the reason being is that, you know, you could actually… and this is why I said, like, you know, an IP address belongs to a subnet. Well, actually, it could belong to a lot of subnets, because depending on the routing protocols and stuff, you have summary routes and… And other types of things that, like, you know, so subnets that are smaller subnets and a bigger subnet, and technically that IP belongs to multiple subnets, so… and a route could be broader than the subnet that's specified for any given individual interface. So Routes might end up being something separate than just a subnet. I just… before I have a concrete opinion on that, I want to… I have to work through it more in my head. I haven't added that type here yet, but But nonetheless, there could be other attributes. I think there are… the one thing I'm gonna need to do here is also suggest, like, what is the primary identifier? Like, on a subnet, I think the CIDR is probably the primary identifier.
And then the, I don't know, maybe if I do like that, right? And then these other things are, like.
optional identifiers you could have on there, and quite frankly, most of them just arrive out of that cider in one way or another. But.
Antonio Jimenez 00:24:58 or…
RC Robert Cowart 00:25:00 Was someone gonna say something?
Antonio Jimenez 00:25:02 No, I was just saying, like, CIDR could be the cue, I agree, but if you have also the mask and the prefix, that also makes uniqueness there, right?
Sorry, I don't know if we can… we should.
RC Robert Cowart 00:25:15 Yeah, if it is a cider, you could also argue that you don't have mask at all, because… or mask size, because the cider actually has the slash. When I was referring to mask, I was thinking, like, you know, 255.255.0.0, something like that, right?
But mass size probably doesn't need to be there, because if you have a cider, the slash… part is the size. So…
Antonio Jimenez 00:25:41 Question.
RC Robert Cowart 00:25:43 And in the prefix is the first part, minus the slash. So, so again, some of this could be a little bit of duplicate, but I just wanted it there because sometimes you see these things, so…
Antonio Jimenez 00:25:56 For sure.
RC Robert Cowart 00:25:58 Okay, and then for various, and I had two examples here of routing protocols, Now, I know technically, like, BGP or OSPF themselves, and one way of seeing it is they are applications.
That… run on these networking devices, but I… you know, if you wanted to get technical these pieces, parts can be spread around a bit in the… in these different layers, but, I mostly had them there, because, you know, they are basically… control plane functions for Layer 3 route determination, so that's the reason I had them associated at this level.
And this is where I kind of get into this whole area of… Like, for network observability use cases.
We're gonna care a lot about things like, you know, how is BGP and OSPF and other routing protocols behaving?
for… like, for someone who just doesn't care about network side of things, or… or a lot of the existing, you know, OTEL-related observability platforms that don't currently support network.
you know, they're not good. They might not necessarily even care about these attributes per se. They might care about other layer 3 stuff, but not necessarily these here. And that's where I thought like.
in some way, I feel like it makes sense to have certain things grouped, whether it's with some type of tagging or other thing, to basically say, like, yeah, like, these are control plane stuff, and if you really don't… If you're not focused on the network side of it, you might not even care about these attributes, or these entities.
Yeah, so, I'm just not… it's not clear to me yet exactly how, in the OTEL world, we would want to mark, or group, or otherwise, indicate those differences, but this is kind of my example when I say, like, control plane versus forwarding plane. Now, certainly, these particular protocols are doing a lot with IP addresses and subnets as routes, etc, so there's a definite Direct relationship?
And.
You know, between these two worlds?
But there are some distinct things, distinct groupings I think we could make in one way or another.
Okay, And by the way, that also applied down here at this… at the bottom as well. Like, even at the Layer 2 level of switching, you're going to have, you know, the switching fabric or the bridge, you know, that you would have. You have certain protocols to make sure you don't have loops and… and stuff like that, so, like, Spanning Tree and others that would be in here. And then… then there'll be other protocols that are, like, ARP and LLDP and those type of things that are just basic, low-level… You know, control plane type protocols that have Less to do with the actual real application traffic, you know, so again, creating these kind of… there'll always kind of be these two groups.
Yeah.
Okay, so with that said, like, I almost feel like there's a… there's an interesting line to draw down the middle of this that has control plane stuff on one side.
Pure data forwarding type stuff on the other side, which actually will probably be the more simple set of entities and attributes.
And then, It'll also be, like, where network… most of the network traffic stuff lives and what have you.
And so that's kind of one way I want to start breaking these up a little bit.
Okay, then I want to spend a minute talking about.
Traffic, if you will. So… This is… this thing I want to talk about is something I really don't see… existing And it's specifically this form and semantic conventions at the moment.
Even in some of the work that's like Sven that we've done.
with Mermin, or like the OB work that's going on talking about flows or network connections.
I really don't see this concept, but I, I do think is a, is a useful concept, which is this idea of a service access point.
Oh.
Most of the tools on the network side I've worked on in the past, have some concept similar to this.
And, and some of them just call it Service Access Point. And it's essentially a, you know, it's… It's basically where a service is accessible, or think of it as a network socket. That'd be the other word to use for it. So, And in, you know, modern, again, data center type networks, yes, there are other… we're not talking about older protocols or alternative protocols that don't have IP addresses, so staying in the world of IP, right, it's a IP address, a Layer 4 protocol, and a Layer 4 port.
So, if I had, for example, you know, some application over here.
Umm.
Right? When the… when a browser's gonna make a request, it… it is opening on an IP address with a given protocol and a given port.
as that, that client side in this case, but it's opening a service access point, a socket, if you will, to call it that. Then it's gonna, it's gonna talk across the network, be, you know, be forwarded, et cetera, et cetera, but it's gonna talk across the network To like a, you know, some web server.
which is… has a socket of its own, or a service access point of its own, that it then talks to, right? And so… I tend to think of of.
this particular thing as the interface between what is more direct, like, application level, and then what is in the middle network level.
And then what would a flow then actually be? Well, a flow is a source service access point and a destination service access point.
Does that make sense?
Antonio Jimenez 00:33:06 Should we keep the concept of access point here, or do you think that will make people confused about the, like, SAP Like, in the sense, like, we have a server talking with, Sorry, I'll start starting with our destination.
We don't have to include, I mean, that assumes somehow that if you're going to communicate, you can only access to that access point. So is it kind of, I'm saying just because it might be treated as confusing for.
Other people that are not that… Deep in the domain? I don't know. What do you think.
RC Robert Cowart 00:33:40 Well, that's kind of the question I'm asking. I mean, the.
Antonio Jimenez 00:33:43 Right, right.
RC Robert Cowart 00:33:43 This instead of that is just think of it as socket, right? Network socket.
Antonio Jimenez 00:33:54 But when I hear about network socket, I always think, like, a lower layer in the… and you were talking, like, application layer here.
RC Robert Cowart 00:34:02 No, I'm talking about, like, Layer 4, like, you know, so… so applications live up here, so the… everything that's TCP, IP.
Antonio Jimenez 00:34:12 -H.
RC Robert Cowart 00:34:13 Because, like, an application, a web server, when I start it up, it's going to bind to a particular port of a particular protocol on a particular one or more IP addresses, right? It might bind to all the IP addresses on the box, but one or more IP addresses.
And so… so there is a socket, a network socket, that is identified by that.
that the web server is listening on, and traffic that hits that, that's when I… when I hit that spot, when I cross over, now I'm in application territory.
But when I'm… when I then talk back this way, then I'm back in network territory.
Antonio Jimenez 00:34:54 Yep.
RC Robert Cowart 00:34:59 Now, the thing to me is, like, I… I just know right now, like, OTEL Worlds doesn't think this way, like… So, not at the moment. I can't find any, any, any thought like that. And basically what ends up happening then is instead of a, instead of a session.
being something like this, you know, a session becomes a Would then basically just be a.
You know, a source socket and a destination socket.
Good.
And that's it, right?
I think this is very real world. The question is, is that compatible with how things have been done in general?
Antonio Jimenez 00:36:00 Correct, because here, let's think for a second. We are gonna have a metric, let's say, number of packets.
Per second, like, throughput. And then you're gonna have, like, a source and a destination. Would make sense to have there the word socket, or… active point, because here I would think, like, I see this already defined. If I'm not mistaken, it was something like network.remote.address. I think it makes sense on that body, so having remote have destinations, or network.
destination dot address, and in my opinion, we should even have, like, dot IPv4 or IPv6, or… port IAB before on those things. And then, also, we would have protocol, and then we have network IAM, those things, but which I don't think we need to add there to don't make it complex or confusing for people using it is access point or socket, I would keep those as assumptions.
Like, when you're sending data to a place, it's clear that it's using through a circuit, or it's reaching the access point. This is what I'm trying to mention here.
RC Robert Cowart 00:37:10 The yeah, the.
the reason I would… so… so, by the way, I'm… I'm not married to one way or the other, but, you know, I'm just trying to think through,
Antonio Jimenez 00:37:23 Sure, sure.
RC Robert Cowart 00:37:24 All the different scenarios. But, like, there are literally… metrics that can be have, like, on a given server, like running NetStat or whatever, you could get some of that type of stuff, or, Say the TCP MIB, as an example, that literally has per socket metrics.
And so, if people wanted those things… so, in other words, essentially, the… it is the… One side of a session, Metrics provided by the system where that, thing is running.
Independent of… perhaps independent of the overall awareness of the session, just for it… for itself, counting on this IP address, and this port, and this protocol, here's the count of bytes, packets, etc, you know.
The reason I'm not married to it is because, I think we could debate how valuable those metrics are, outside of… outside of understanding it per flow. So, that's just my opinion, you know, people could have a different opinion, so…
Antonio Jimenez 00:38:37 But that's the great thing of OpenTelemetry in If we have different granularity, so let's say that we want to have, like, a system level, so we only want destination and source.
is what we are talking right now, or at least I was talking. And then if you want to have deeper granularity, like per socket or per session, we will for sure define those attributes, so it could be using maybe OBI use case, or it could be using different socket use case, but we should not have it as a primary attribute, or in the naming of the… of the attribute, that's what I'm trying to say, so I'm fine having later something like, I don't know, session ID, I mean, I think that's super useful, but we are not gonna have it available always, so it will be, like, any session ID between those two endpoint.
But if we have it available, for sure, we will use it. That's what I'm trying to say, like, that's the cool thing about OpenTelemetry, so you will define different attributes, and we will be If we have it available or not, and if we have it for sure, they will provide higher granularity, or higher… Detail.
RC Robert Cowart 00:39:49 Got it.
Sven Cowart 00:39:50 Is there…
RC Robert Cowart 00:39:50 So,
Sven Cowart 00:39:53 I haven't looked too much into entities, but is the general idea that… 'cause I see… There's a ton of overlap between the entities that I do see in the talks.
And just the attributes that exist under a namespace.
And more or less, what a one entity is, is an attribute grouping.
in a in an area or namespace of OpenTelemetry.
Is that right?
Antonio Jimenez 00:40:20 As Robert was mentioning before, NTCs, at least the way how we see in OpenTelemetry, they are not mature yet, but… so they don't need to be in a namespace, so if we are, let's say, entity related with address, like, an address would have, like, an IPv4, IPv6, and a port, and so on, so we don't have to be forced to call that entity network.address. Usually, it's gonna… World work. I mean, we're gonna understood well, but it's not like a requirement that we have in the standing.
And then different attributes could be shared between different entities. So what you said is perfect. An entity is grouped in a subset of attributes, but those attributes don't have to share the same namespace, or they could be even in different entities, like IP.
Robert mentioned before, it could be in session, or it…
Sven Cowart 00:41:14 You were awesome.
RC Robert Cowart 00:41:18 Yeah, I mean, they're…
Sven Cowart 00:41:21 All right. Well, I mean, the point I was that the reason I was asking that question is because I think this, like the idea of a socket or SAP makes sense to me.
The only thing is, I don't think we need to introduce any new attributes to do that, right? Like, and that's why I was trying to make sure that we're avoiding, like, I don't want to see a network.sap.ip address or something like that. It's just, like, when these three things are present.
Now you have the SAP.
RC Robert Cowart 00:41:49 I see what you're saying. It's conceptually there.
Sven Cowart 00:41:53 Yes. Okay, okay.
Antonio Jimenez 00:41:54 I follow you now, I follow.
RC Robert Cowart 00:41:55 Specified as an entity.
Antonio Jimenez 00:41:58 For sure, and even we can describe… put that in the description of the attribute, or specify in the entity description, but I agree. I mean, I was on the direction of, it's gonna make people confused if we put socket or sub on the attribute name. That was my comment.
RC Robert Cowart 00:42:14 No, no, that's a good point. It's a, it's almost, it's It's not an entity, it's a concept, if you will.
Sven Cowart 00:42:22 Yeah, and I think then that…
RC Robert Cowart 00:42:25 Okay, then no, that's a good way to think about it. Yeah.
Sven Cowart 00:42:28 I think that also addresses Gocepi's point that I saw you had your hand raised. Was that what you were about to ask.
Giuseppe Ognibene | Coralogix 00:42:33 Yeah, yeah, yeah.
Sven Cowart 00:42:35 Okay. Yeah. So we wouldn't have that duplicate.
Yeah. But I like just looking at some of these entities in the web on the entities page in the docs. It seems like that's what they've done, but we should verify that. And if that is what they've done, then I think doing something like this makes a ton of sense.
RC Robert Cowart 00:42:55 So from what I've gathered also from attending the entities call last week, and by the way, I kind of just introduced myself and, and that we have started this network SIG, effort.
Antonio Jimenez 00:43:08 Let's see.
RC Robert Cowart 00:43:09 And, sorry, just realized I wasn't on video.
But No.
looks like it doesn't want to go on anyway. I And… But one of the things they were talking about there, because there was someone else, there was another thing, and that they were, also talking about how new everything is, but from what I gather, the… The general idea is the way forward in the future would be like, so any, any new domain to have any type of.
You know, semantic conventions, attributes, what have you, defined.
Would start with… Like, what are the entities? Essentially, what is being managed here, or being monitored here? And defining that, and how you identify it. And then all the other semantic conventions then fall under that.
Which to me makes total sense, right? But, but it's also then having to make sure we stay in line with what's already out there. So, like I said, I'm okay, and I actually like the way that you've said that. Is that, and when we start to document a few things, then we can talk about that.
Conceptually, these attributes represent the network socket, or the SAP, if you will, the service access point.
Antonio Jimenez 00:44:39 Sure.
RC Robert Cowart 00:44:40 Yeah, that that makes a lot of sense to me. Okay.
cool. And so what that ends up meaning, basically, is that, you know, like.
When we talk about the traffic side of it, you know, a session is more like like a… a flow of traffic, right? We can call this session, or we can call this, you know… but, you know, a… a flow of traffic then becomes the classic 5-tuple.
here.
The the The one thing that I do think is worth adding on to this classic 5-tuple is, Oh!
there's this concept, actually, Cisco primarily has it in some of their flow records, this concept of a buy flow indicator, where it's basically a value that says, Like, if it's known, so this would have to be optional, because it depends on the perspective You know, like, what was the perspective of the system that produced the flow record?
But it's, it basically is saying, like, which… which end was the… the server, you know? And the way I think it… if I remember correctly on the Cisco one, it's basically saying, it's a value that… an enumeration, where it's like, zero is unknown, one equals source.
I'm sorry, one equals initiator and one equals responder, and it's always relevant to the source field in the flow. So, is the source the initiator, in other words, the client, or is the source the responder, or, in other words, the server?
I think that's a good optional attribute to have in there, but just to provide some indication of client server.
The other option for that is just, you know, you create entirely different additional attributes get attached, which are client and server, fields, but…
Sven Cowart 00:46:52 That's… A session just that. I'm sorry I'm knit knitting the name here, but sessions is a little bit confusing.
For a session, if this.
RC Robert Cowart 00:47:04 Recession is very much a, a net. This is the, the, in the term of network. I mean, layer four is known as the, well, okay, layer four is known as the transport layer, but, it.
It is where you'd refer to a network session.
Sven Cowart 00:47:20 Right, but for sessionless protocols.
But.
it…
RC Robert Cowart 00:47:25 So… So, let's just take TCP UDP as an example, right? Just because it doesn't have a, a, a frame, like a handshake or something else that has all of these, Yeah.
connection-oriented parts to it, so that the real way to… a lot of people say, like, or like, when they refer to TCP UDP, they think of they refer to, like, UDP doesn't have sessions. No, correct way to say it is, TCP is a connection-oriented protocol, and UDP being a connection list, meaning they have no handshake and other attributes exchanged.
to guarantee delivery.
That doesn't mean it's not a session.
So, if I fire off a UDP trap, or, you know, like a SNMP trap over UDP, I still have a source IP and a source port when I do that, and the other, and I'm sending it to an IP and a port, and that's still technically a session. It's not a connection-oriented session. In other words, there's no additional attributes or functionality to ensure You know, guarantee the delivery, retransmits, all that kind of stuff, but it's still a session.
It's just not a connection-oriented session.
Does that make sense?
Sven Cowart 00:48:55 Yeah, it does.
Antonio Jimenez 00:48:57 We even have to define it, because even if it is not used for I mean, it is used for UDP, but not on that much. It's used in other protocols, so just assume we will need it, for sure, yeah.
So…
RC Robert Cowart 00:49:14 The main thing I kind of touched on.
Sven Cowart 00:49:16 It works out because the flow then could be defined as something with, well, it just gets tricky because on the flow side.
You're not always guaranteed to have the protocol identifier.
RC Robert Cowart 00:49:33 That's not correct.
Sven Cowart 00:49:36 No?
RC Robert Cowart 00:49:37 No.
Not not correct.
You, you are always.
That probably wasn't a… the best image.
Oh.
There we go. Let me You're always gonna have this field in the IP header.
Now, it might be zero.
Sven Cowart 00:50:02 Not IP traffic, that's what I'.
RC Robert Cowart 00:50:07 Oh, so what kind of traffic are you referring to, then?
Sven Cowart 00:50:11 Any… anything else?
RC Robert Cowart 00:50:14 I mean, in a modern network, like, are there other things? Sure, over time, there's been other protocols.
like Novell Netware back in the day, IPX was the protocol, right?
Like, there are other protocols, for sure.
Other, but there are also things that are further down the, like, layer 2 stuff, like LLDP, yeah, doesn't have, doesn't, it's not IP traffic, it's lower level things. Because it's not IP traffic, it also can't be routed, so it only functions in the same broadcast domain.
so most of those lower-level protocols like that are non-routable protocols.
anyway, and are not used for application to application traffic. This is this is one of the reasons I was kind of talking about like this control plane versus data plane stuff.
there's gonna be a lot of things that are not IP, That are control plane traffic.
There's going to be almost nothing that is data plane traffic that's not IP.
I'm not saying it's impossible, but, like, there'll be very little in a modern network. In the past, it used to be different.
Now, if you're talking, is everything not TCP or UDP? Oh, definitely, that can be the case. SCTP gets used a lot for, like, streaming type stuff. Icmp obviously is a, is a, you know, for various background functionality in, in the network.
In fact, ICMP is used a ton all the time.
And most people don't even notice it happening in the background, you know.
Sven Cowart 00:52:02 Let me, yeah, so two things.
on the… The lower levels of traffic.
Do network devices not produce flows records for that traffic?
RC Robert Cowart 00:52:16 So it depends a lot on on sflow, because you're just getting raw packet samples like the 1st bytes of a header.
You'll get… just depends on whichever bite you happen to get. So, in general, you could get all the different types of stuff.
Usually on NetFlow and IPFix, you're only getting Layer 3 for those. And it has to… it generally has to do with the way, the… Like the, the maps inside the devices that actually track the flows over time are based around the traditional five tuple. And so, so they don't even have a way to store and map.
non-IP traffic.
Sven Cowart 00:53:04 Oh, yeah, that was… that's what I thought we'd agreed upon before with… around flows, because flows… To me, some of these fields are optional.
Because the possibility of having flows generated that don't actually have these things like even ICMP.
Dominic Johnson, flow records about Icmp traffic wouldn't have ports.
RC Robert Cowart 00:53:25 So this brings up another question, actually, is…
Sven Cowart 00:53:29 And The the heart of my question was like, is a flow and a session 2 different things.
I guess a session assume there's ports or is ICMP traffic in your definition of a session also, or is that also a session?
RC Robert Cowart 00:53:52 So… Yeah, that's a gray area, I would say. I would argue that some types of ICMP messages, you could argue that they are session-related, session-near.
Sven Cowart 00:54:06 Yeah, I noticed that.
RC Robert Cowart 00:54:07 Not at all.
But you do bring up a different point, when you bring some of those up, is, like.
Should that port field… be allowed to be overloaded in any way.
There are a lot of network devices that actually do this today, in particular for ICMP traffic. So in ICMP, you're gonna have a type and a code. So, for example… Yeah.
Sven Cowart 00:54:36 Hey, Mermin.
RC Robert Cowart 00:54:37 What's that?
Sven Cowart 00:54:38 So we do in Mermin.
Oh.
RC Robert Cowart 00:54:42 Yeah, you have, like, an echo response and an echo, reply, for example. In other words, the message is used for a ping. Or, you know, or one is, I try to connect to something, and I get back a port unreachable, or like a destination unreachable, and then I have a code that is address unreachable, port unreachable, like, like, what, in what way was it unreachable, right?
And, a lot of network devices, when they send flow records like IPFix or NetFlow, they will actually overload the source and destination ports to be the ICMP type and ICMP code.
Sven Cowart 00:55:22 So either we need to then modify the source and destination definitions to accommodate for that.
Or we need to, for flow identification, come up with an entirely different concept that can handle both. I'd like to just… Clarify port usage, I think, for that situation.
RC Robert Cowart 00:55:41 So… I personally don't like the overload. I think it's confusing.
Sven Cowart 00:55:47 Mmm.
RC Robert Cowart 00:55:48 I would, I would rather have additional ICMP fields that contain the type and code and be more, more declarative about it.
Sven Cowart 00:55:58 Okay.
Why? Oh, just because it's confusing?
RC Robert Cowart 00:56:02 Because it's confusing. The same reason, like, we're.
Antonio Jimenez 00:56:04 Talking up here, things can be.
RC Robert Cowart 00:56:06 confusing. I just think it confuses people. Like, if you don't know that, if you wouldn't have known what I just told you.
then you wouldn't have known, like, like, literally, you would have thought, I don't know why they got values in source and destination port, this was ICMP traffic, that's dumb, what is the system doing? Like, you know, like, it just, it creates more questions than it, and I feel like in, in the case of IPFIX and NetFlow.
Where they… there's not the flexibility to… Like, there's just not quite as much, like, payload… flexibility there. It makes sense why they did that.
I think we have a lot more flexibility in the OTEL payloads, and it's not necessary to do that. That's my opinion.
Sven Cowart 00:56:57 So do you still think with the things I just brought up, that session and flow is the same thing?
The same entity.
RC Robert Cowart 00:57:04 No, actually, I don't. I put flow there just to make… just to say, like, for example, flows are sessions.
But flows could, in theory, be other things, too, that are not necessarily network sessions.
Antonio Jimenez 00:57:18 Sorry for jumping into the conversation, but can also a flow be part of a session? I mean, they are not the same thing. I mean, a session will have several flows.
RC Robert Cowart 00:57:27 I would say all sessions are flows, not all flows are sessions.
Sven Cowart 00:57:32 Yep.
Antonio Jimenez 00:57:37 Right, right, right.
So… I like the idea that Ben is mentioning about categorizing them separately, even if they kind of share almost the same concepts, but yeah, people are gonna… Get conf… make question about them, for sure. The thing that we are doing.
RC Robert Cowart 00:57:59 Okay, we're we're kind of coming up on the end. I'm I'm gonna continue to work on this and then try to start documenting a few things. I want to come back to a question about documenting here in a second. But What I'm… so a couple things I took away are… we will. We will have this. There. There will be some things that we will talk about conceptually, but not necessarily have separate entities for them.
Like a socket or a service access point, right?
Sven Cowart 00:58:36 Wait, no, no, no. Why do you say that?
RC Robert Cowart 00:58:41 Because we're we're not creating separate Attributes for them, separate entities for them.
Sven Cowart 00:58:49 Well, they're, they, we don't, we're not creating separate attributes, but they're grouping of attributes that makes it an entity.
RC Robert Cowart 00:58:57 Oh, I see what you're saying.
Sven Cowart 00:59:00 Like all three of those attributes on Network Socket already exist today.
RC Robert Cowart 00:59:04 Yes, correct.
Sven Cowart 00:59:05 We're not going to create a network socket area or a dot network socket dot address. We're just going to reuse the existing ones and then say this is a socket when you have these things.
RC Robert Cowart 00:59:15 I see, yeah, okay, alright, no, that makes sense.
Sven Cowart 00:59:18 We need to verify what the entities say that that's what the intention is, but that's what it seems like just reading some of the…
RC Robert Cowart 00:59:24 Got it. Okay, no, that sounds good. All right. I misunderstood. But Okay.
The,
Sven Cowart 00:59:36 I do think, sorry, one thing, this does bring up a problem in the fact that addresses right now always source, or it… There's no just networked out address.
There's always a directionality to a dot address, which… that I don't know if in the entity's definition that somehow… I I don't. We gotta think through that.
RC Robert Cowart 01:00:00 Well, and it does get confusing, right? Because, like.
If you if you think about this a little bit further.
You you start to get to.
you know… where… here we go.
How are you guys?
Giuseppe Ognibene | Coralogix 01:00:24 Can you…
RC Robert Cowart 01:00:25 This here…
Sven Cowart 01:00:26 We can hear you now.
RC Robert Cowart 01:00:28 Set.
Giuseppe Ognibene | Coralogix 01:00:29 I had that question. Sorry, my microphone just stopped it.
Sorry to interrupt you, I had a question regarding the… session flow, because I saw that you deleted the flow name But I think it should be more correct to use Flow.
Because if we agree to use it, the PIN2 also for SMP and UDP, That are not, let's say, session.
Right?
RC Robert Cowart 01:01:03 Well, so, yeah, so we had that conversation a little earlier. That was, like, like, TCP and UDP is still technically a session.
It's not a connection-oriented session, like TCP is, but it's still a session.
Giuseppe Ognibene | Coralogix 01:01:20 Yeah, but with the session, the table that you have on the bottom of the screen.
We will use it also for ICMP, right, or not?
RC Robert Cowart 01:01:31 CLAB, For for support. What.
Sven Cowart 01:01:32 I see MP.
Giuseppe Ognibene | Coralogix 01:01:33 SMP.
RC Robert Cowart 01:01:35 Oh, that's what we were saying, like, no, that's where we would probably not… You know, maybe a flow and a session maybe are two different things.
Giuseppe Ognibene | Coralogix 01:01:47 Yeah,
RC Robert Cowart 01:01:48 I mean, they're very… like, this is where I said, like, every session is a flow, but not every flow is a session.
Giuseppe Ognibene | Coralogix 01:01:56 OK, so we need another table for everything that is not a session.
But the fields are the same.
So we will duplicate them.
RC Robert Cowart 01:02:08 Umm.
Some of them are the same.
like… I think there's 1 we'll have to revisit a little bit in more detail, which is that Because, like, the point was, not all flows have ports.
ICMP doesn't have ports.
Sven Cowart 01:02:34 There needs to be optionality to it.
RC Robert Cowart 01:02:36 Doesn't have ports.
OSPF, hello packets and things back and forth, you know, don't have ports.
Giuseppe Ognibene | Coralogix 01:02:48 Okay, yes, yeah, yeah.
Thank you.
RC Robert Cowart 01:02:52 All right.
And this is why every session is a flow, because it has these, but not every flow is a session, because it doesn't have… the other items.
Giuseppe Ognibene | Coralogix 01:03:05 Yep.
RC Robert Cowart 01:03:07 And look when when it gets down to it. Maybe maybe we do need to think of these as the same, but like ports are optional fields.
Sven Cowart 01:03:17 Yeah, I… Let's just get a little further on defining these things.
RC Robert Cowart 01:03:21 Yeah, yeah, I will go through a few more common protocols and put some examples in for a future one.
what I wanted to just show up here is, like, that IP address one is one that it's, like.
You know, you… You have, like, all over the place.
You know what I'm saying? Like, the IP address… belongs to a cider. It's bound to an interface or assigned to an interface. It is… part of a… of a network socket, you know, like… like, IP just ends up going all over the place, so there is a lot of relationships that it… it can have.
you know.
If we're, we're gonna do DNS, or, and DHCP, we were talking about in the last call, it was assigned by, you know, the IP address. Like, there's, there's tons of different ways you could have relationships to IP address.
And I just think this is where we gotta get a few more mapped out, and then we can pull and drag these around a bit.
Okay.
So, getting back, because we're at the top of the hour, real It sounded like there was no confusion around like this idea of separating what are more of the control plane focused things versus what are more the the forwarding or data plane focus things.
And, and then… we'll get some examples of, like, different types of protocols, and how they, you know, what might be the identifiers for this flow session thing. It sounds like this is probably the more, like, a little bit more high priority, because of, like.
The OBI effort,
Sven Cowart 01:05:09 Yeah.
RC Robert Cowart 01:05:10 etc. Is that true?
Sven Cowart 01:05:12 Yep, I'd say so.
RC Robert Cowart 01:05:16 All right.
Well, thanks for the feedback. That gives me a little bit more thought. The final question I had real quick before ever is, where are we putting stuff right now? If I want to create an issue and start to document, are we going to have our own space, or is it just.
Sven Cowart 01:05:31 We will, right now.
RC Robert Cowart 01:05:33 Create them in the semantic convention one, and and then.
Sven Cowart 01:05:36 Yes, that was the plan that we agreed on last week was it goes in the Semantic Conventions issues. And then once they create that federated repo, it'll be moved. They could be able to move the issues from repo to repo.
RC Robert Cowart 01:05:51 Okay.
Sven Cowart 01:05:54 Can you share this doc with me?
And the next.
like soon, so that I can update some of the reference it, so I can update some of the things in the project proposal.
RC Robert Cowart 01:06:05 Yes.
Sven Cowart 01:06:07 Thank you.
RC Robert Cowart 01:06:08 It's kind of a shame that, We need to figure out if there's a way to have a community Miro thing. I don't know if Miro does anything with open source projects or whatever.
Because I'd love to just share this with the broader team instead of… GitHub issues and drawing things in ASCII are not always the most helpful, so…
Sven Cowart 01:06:30 noise Brad Grimes, Esq: allow public access to the link in Miro.
RC Robert Cowart 01:06:36 Yeah, okay, yeah, we'll look at that and see about sharing it out then.
Sven Cowart 01:06:39 Okay.
RC Robert Cowart 01:06:41 Alright. Thanks, everyone, for the time and listening.
Sven Cowart 01:06:45 Thank you.
Antonio Jimenez 01:06:45 Yep, very good. Thank you. Talk to you guys.
RC Robert Cowart 01:06:48 Sorry, but.
Antonio Jimenez 01:06:49 Esben… Esben, by the way, you mentioned that you have some question about that Jira issue that you have. Do you still have question, or everything was…
Sven Cowart 01:06:56 Sorry, the what?
Antonio Jimenez 01:06:59 You mentioned at the beginning of the call that you have some doubts about the… The Github project that you were, proposing?
Sven Cowart 01:07:07 Oh, oh, no, it was main… more around, this entity's work wasn't there yet. Like, we very loosely defined, we… I think I said one sentence on it, and it wasn't defined yet, and then… I was going to use what Rob proposed here to figure out and list what are the things that we're going to try to aim for around stability.
so… Darcy Kitching, because that was the the main ask Ludmilla asked of us in the project proposal was that we need to identify what things that we're going to drive towards stable attributes.
And…
Antonio Jimenez 01:07:48 That makes sense to me. Mostly with my app.
Sven Cowart 01:07:51 Clarification. Go on.
Oh, sorry, go ahead.
Antonio Jimenez 01:07:56 Oh, I was just mentioning that most likely we will need… we will add more things, but I like the idea of a start with those for the moment.
Sven Cowart 01:08:02 Yeah, yeah, I agree. And I mean, once the project is up and going too, I mean, I think we can make updates to that page anyways, and we will need to make updates as we learn and discover more.
All right. Take care, everybody.
RC Robert Cowart 01:08:23 Alright.
Antonio Jimenez 01:08:24 Right.
RC Robert Cowart 01:10:01 Did I go?
We're back, let' Thank you.
Talk about your husband I grew up in this business, so I have any. I feel.
I don't get into it.
So what's next?
Start over.
I don't do That doesn't work exactly. Well.
Save someone's stuff. Give a new identity. It's not all the stuff.
There are different package options. Sometimes the disappearance isn't enough.
Others want more, so… Anybody's.
The human remains found in the business car after the accident.
the corner on payroll.
trade secret.
Are there others in your network?
Openly coming across.
Maybe.
How did Lucas know where to find you?
When people come to us, they are our choice.
When you're desperate enough, you know where to look.
Never had anybody come back like this.
Yeah, they do this one. Yeah.
He was scared of life or death. He was working with a woman.
Stephanie Hollis died in the robber You disappeared her, too.
Never heard of that.
maybe.
Maybe Lucas found something something he thought.
Other people should know about.
share it with Stephanie, because she has an audience. Stephanie gets silence. Lucas figures.
He's next.
Did he tell you what he was running from?
No, make an appointment to ask.
offer service.
I'm in the rooms.
the risks of resurfacing.
My husband's blinds on Lucas's hands.
I'm gonna help you find out who's responsible for killing Master.
I'm very good at what I do But I need you to trust me.
As long as you understand what I'm gonna do when I'm trying to.
We'll deal with that later.
Right now we have to move quickly.
What was Lucas's role in this?
Isaac Newton.
Are you serious?
There's no way your husband gives a cut name.
No matter what they did today.
What the heck to him.
Give me one second.
Wow.
Bobby, what do you got? Well, looked in Stefan's Youtube account.
Pass somebody over to something.
Let's see, I mean, just double push it to post it.
That's only from some secret source. But she has a little Scott focus.
So maybe, maybe we found something on a laptop that was repaired, shared with us.
that, too. But cross references point involves anybody who bounces on the books. Bring their laptop in and see if there's accumulating evidence on it. It's probably a family member, maybe employee. Okay.
Oh, sorry.
Oh, wow! Call culture. Yeah, I got a credit card receipt here.
Lucas restored the crashed hard drive in the personal assistant of Team Frost.
Who's that?
Big Wave Real Estate Developer.
Boomer has it. He's running for mayor. So sounds like he's the bill does.
Alright. So an assistant brings their boss's crashed hard drive service doesn't know what's on it. Focus finds it just with Stephanie. Stephanie's in politics.
He decides to break it.
or spare.
This is digital trust, pretty easy to follow. So you would have known what's next.
As long as we didn't kill Stephanie, I I think Lucas made a copy of what he found.
Put it on the flash drive back to the repair Kind of barter his way out of Where's the customer?
Do me a favor. Run an alias for me, Anyway, Isaac, no.
