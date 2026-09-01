SIG: Networking SIG
Date: 2026-08-31
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Giuseppe Ognibene (Coralogix)** 02:20 Hi, Sven.
**Sven Cowart (ElastiFlow Inc)** 02:22 Hello.
Good morning.
**Giuseppe Ognibene (Coralogix)** 02:27 Morning.
**Sven Cowart (ElastiFlow Inc)** 02:32 Or is it… is it morning for you?
**Giuseppe Ognibene (Coralogix)** 02:35 No, it's not morning, it's 4PM.
**Sven Cowart (ElastiFlow Inc)** 02:38 Good afternoon.
**RC Rob Cowart** 02:45 Where are you located?
Giuseppe.
**Giuseppe Ognibene (Coralogix)** 02:47 Okay.
You bet.
**RC Rob Cowart** 02:50 Okay. Whereabouts?
**Giuseppe Ognibene (Coralogix)** 02:53 It's, it's Sicily, south part of it.
**RC Rob Cowart** 02:56 Fade away down there.
**Giuseppe Ognibene (Coralogix)** 02:58 Yep.
**Sven Cowart (ElastiFlow Inc)** 03:04 Alright.
This is probably a Hobie getting today.
Seems.
Sorry.
Struggling to find the right thing here.
It's a lot smaller.
Okay… So, just a quick update.
We registered this.
These areas inside of… What is this?
Yes.
these areas inside of semantic conventions, so hopefully we'll be able to open up… we should be able to open up PRs now.
With those areas… with those areas attached.
So what happens is when I… Just FYI, Rob, this is probably relevant to you.
When I created this PR.
It was automatically closed.
Because, because I made changes inside of the YAML registry files.
That are in clients, destination, server, and source.
And there's not code owners for that.
So, what I did is I… Made.
In this PR.
You can see… I've made… the owners for those areas, also a group, a GitHub group called SEMCON Network Approvers, which they still have to create that group?
So that's the next step.
We're… I'm gonna add a few of us on there. To be on there, you need to be an OTEL member.
So, Rob, if you're still not an OTA member, please do that today.
**RC Rob Cowart** 05:12 I don't know that it'll get done today, but maybe tomorrow, yeah.
**Sven Cowart (ElastiFlow Inc)** 05:16 But, we still have the problem that… Client is an unknown area.
So, I have to bring that up in the semantic convention SIG today.
So that just, like, I don't want to reopen this, and then it gets closed again.
But this does address… All the things that… We talked about in the issue that, Antonio brought up, Around store assassination.
And I think that will then… Meaningfully at least unblock us from these other things.
That he also brought up.
Excuse me.
So, that's where we're at right now.
on those things… That's it, I think.
For what I wanted to share really quickly.
Yeah, so, Rob, wanna go next?
**RC Rob Cowart** 06:21 So, the first thing I wanted to talk about is… is related, in a way, to that whole area of source destination, client, server. I know I had made this comment last week.
And I saw the… at least from a few folks that were on video, I saw some nodding heads.
Saying, You know, showing some degree of agreement.
that when it comes to IP addresses, like, in general.
The fields out there, we tend to see this .address suffix.
And the… Which, I mean, could hold things other than an IP address based on, like, what, like, say, network, local address, local peer address, but I think in most cases they would be IP addresses that are put in there.
But, I think from all of our experience, there is a set of attributes that are related to IP addresses.
that really could be, I was gonna say in theory, but I feel like, in practice, are very often applied to almost any other, or, you know, optionally to any IP address. Things like the reverse lookup, DNS, you know, fully qualified domain name. Like… the autonomous system that it belongs to. Like, there's geolocation information, potentially. There, you know, so there could be a number of other attributes that could be related to, really any IP address. And I don't know if OTEL has this concept.
Clearly, there's not… I mean, if I was to think about it, you know, independent of OTEL for a second, I would, you know, I would be thinking something like, I'm writing some JSON schema, and I say.
an IP object type has these potential fields that go with it, and when I create that JSON schema, then anytime I say something is an IP type, then I know that all of these other suffixes that have particular meaning, like, you know.
Subnet mask, and, you know, or, network, address, or even, like, broadcast address, or, like, there could be a number of different fields that go along with any given IP address. And so, whether it's a best practice or general guideline for IP addresses, I feel like… and I'm saying this also, again, because I was about to go through, and you'll see in a second, this BGP stuff as an example, and it's like, huh, an IP address.
well, okay, then I'm gonna need also .asn and dot… I'm, like, thinking, like.
now I gotta go check 27 other different things that have used IP address in the past, and make sure that I'm doing it consistently. And I feel like if there was just, like, an IP address best practice of some type… then it makes it easy in the future, because what I'm worried about is we start down a given path, and then it just gets really hard and confusing for anyone also submitting similar things in the future that we have to remind them, oh no, you can't name that this because that's already in the IP address best practice that would use that name for, you know… and, like, we avoid conflicts, we avoid all kinds of confusion around other potential attributes related to a given IP address. Does that make sense at all?
**Sven Cowart (ElastiFlow Inc)** 10:14 Yep.
That's what I thought, we discussed last week, and we agreed, and…
**RC Rob Cowart** 10:19 I think we, as a team, were kind of like, yeah, that's how I do it.
**Sven Cowart (ElastiFlow Inc)** 10:24 No, I was supposed to…
**RC Rob Cowart** 10:25 That's our plan for, like, what are we gonna see?
**Sven Cowart (ElastiFlow Inc)** 10:27 Oh, no, there… you can see there's a… There was an action item for me to take that to the semantic conventions.
SIG call, which I tried to, but they ran out of time, so it's one of the things I'm gonna bring up again today.
**RC Rob Cowart** 10:42 Okay. Do you need me to support you on that, or do you have…
**Sven Cowart (ElastiFlow Inc)** 10:45 I can take it, but… It's fine, whatever you want to do.
**RC Rob Cowart** 10:50 Okay, yeah, cause I just… this is gonna… this is gonna become an issue, like, just staying consistent over time, if… if we don't just put a stake in the ground and say, nope, this is the… this is how we think of IP addresses, period, you know?
Okay, so that was one thing I wanted to talk about. Then… Let me… Actually, let me open another… another. I was gonna show this in my browser, but I might want to… Kind of live edit here, so… Let me just open this real quick in a… in an IDE.
So, a couple confessions real quick.
I was… working on… some stuff here over the last couple days for our own product, using our own in-house schema we've used now for the last few years, and adding a few things, and was coming up with some, like, that I felt like uncomfortable naming decisions to make.
And… And then I realized that, this way that it's done in OTEL, where, like, this network direction, like, instead of saying messagesTotal.in and messagesTotal.out as two separate attributes, which is, quite frankly the way I've seen it in tons of products I've worked in over the years.
Just having one thing that has another tag, or label, or attribute, whatever you want to call it, you know.
To it to specify the direction that's, you know, a separate thing than that.
it just kind of made me see, like, okay, I see where that's actually a smart decision at some point, because it would have helped me actually avoid some of the conflicts that I was trying to work my way out of, naming conflicts I wanted to work my way out of, and something we have internally.
So I'm actually, although it was weird to me at first, I'm kind of warming to that way of doing it.
The main thing I wanted to get an ask on, because we had talked last week about… we were on the conversation of local and peer.
And one of the things I'd said, well, you know, peers in BGP have a very specific Thing that they mean.
But, having said that, is… there is, though, like, a local side of a pier. An OSPF would be a neighbor, they would call it, but still.
There is a local, and there is a remote Side to the connection.
Or, or what… Right now is network.local.address and network.peer.address.
And I thought this was a good example to give, because we could reuse the existing ones.
But, if we do so, and let me show what that would look like if we did.
If we reuse those, what we'd end up is something like this.
is we just wouldn't worry about the BGP part.
Because we're saying, hey, this is a BGP peer entity. So, We say network peer address, and down… here.
We would do network local address.
And I guess my question is.
And by the way, we do the same on port also, right?
So… So if we're reusing, we end up with these things like this.
So again, that's… that's… well, you see the two… the rows I changed right there.
So that actually would work. We could reuse those attributes.
in these routing protocol peer relationships, it does make their naming inconsistent with the other attributes related to that entity, assuming no one has objections to the attribute names that I picked already, but,
**Sven Cowart (ElastiFlow Inc)** 16:01 Why… why couldn't we just drop the BGP peer from the other attributes?
**RC Rob Cowart** 16:09 Because my worry is, then, at some point.
I'm gonna start to have potential naming conflicts with other things.
For example, network admin state, network.interface. Or, like, do I do network admin state?
Also, drop BGP peer, does that mean on the interface one? I also drop… Interface from that one?
**Sven Cowart (ElastiFlow Inc)** 16:45 Hmm.
**RC Rob Cowart** 16:46 Like, like, to me.
**Sven Cowart (ElastiFlow Inc)** 16:47 Nope.
like, for example, local ASN, That, to me, seems like…
**RC Rob Cowart** 16:54 Because these are, again, this comes back to that normalizing. Yeah. You're… you're correct that… if we do what we said before, then this one… this would probably also be local ASN.
Yeah. Got it.
Peer ASM.
**Sven Cowart (ElastiFlow Inc)** 17:23 I think it makes sense to keep the BGP pure Part of that path, as long as It's only relevant.
**RC Rob Cowart** 17:33 There's maybe an underscore here as well, but that's… yeah.
**Sven Cowart (ElastiFlow Inc)** 17:36 To describe that specific If it's a specific attribute that's only relevant to BGP, then… It makes sense to leave it in there.
**RC Rob Cowart** 17:49 And that's probably the right way to differentiate it, I would say, probably, Sven, if that's what we're saying. Is… so, essentially, if we're referring about Endpoints across two… you know, I think part of the thing that… There's two things we'd be saying.
So, one, if we're talking about endpoints across two related or I should say, you know, the attributes specific to identifying an endpoint, or two related endpoints, that's one way that's categorized, right? Or that's where we reuse these existing ones.
**Sven Cowart (ElastiFlow Inc)** 18:33 Yeah.
**RC Rob Cowart** 18:37 What we're also saying, though, is that, network.local and network.peer.
Are not specific to network traffic.
**Sven Cowart (ElastiFlow Inc)** 18:53 Yep.
**RC Rob Cowart** 18:55 Because this here is not necessarily…
**Sven Cowart (ElastiFlow Inc)** 18:59 Nope.
**RC Rob Cowart** 19:00 I mean, there is going to be traffic that flows between those two piers, yes, but in this case, right, we're just identifying the peer pair.
Not necessarily generating a record, like a flow trace or something that's actually about traffic. So as long as we say it's for identifying pairs of endpoints.
You know, pairs of related endpoints.
then… And it's not specific to the flow of traffic, just related in some way. That's how those are used.
then I think we can actually reuse those existing ones without, creating any concerns. At least so far from what I've gone through. I want to go through some other examples, but…
**Sven Cowart (ElastiFlow Inc)** 19:43 Yeah.
**RC Rob Cowart** 19:44 what I've gone through so far, that would seem to work.
**Sven Cowart (ElastiFlow Inc)** 19:49 And on… on the, the key.
the parts of that key, could we just do… peer.bgp instead of bgp.peer.
**RC Rob Cowart** 19:59 Well, actually, this is… this is an entity. This needs to be an underscore.
the BGP peer is the entity.
You see what I'm saying?
**Sven Cowart (ElastiFlow Inc)** 20:11 Is that… is that how it's done?
**RC Rob Cowart** 20:13 Well, that is the name of it, right? Like… you could nest peer underneath BGP, I guess, or… Yeah, I don't know that it's consistent enough at this moment to say that whether that would be that way or not. You could do it either way. But my point is, in this case, BGP Peer is the entity.
**Sven Cowart (ElastiFlow Inc)** 20:38 Right, but I don't think the attributes have to… Have that in the name.
**RC Rob Cowart** 20:45 So you're saying drop them.
**Sven Cowart (ElastiFlow Inc)** 20:48 No, I'm saying do peer.bgp.
**RC Rob Cowart** 20:52 Oh,
**Sven Cowart (ElastiFlow Inc)** 20:52 XYZ.
**RC Rob Cowart** 20:53 I personally would hate that.
**Sven Cowart (ElastiFlow Inc)** 20:55 Why is that?
**RC Rob Cowart** 20:57 Because it's not clear to me right away at a glance what it is.
What it's related to.
**Sven Cowart (ElastiFlow Inc)** 21:08 I guess I don't… I don't see that, but…
**RC Rob Cowart** 21:10 It's the same way down further in metrics.
messages… like, I went back and forth on this. Is it total messages and update messages? No, that should be messages.
Or is it messages underscore update, messages underscore total?
one reads better, the other is way quick… like, I know right away those are both about messages, and I don't even need to get past the first couple letters of my brain comprehending that.
Nope, that's not what I'm looking for, that's not what I'm looking for. Where if I see total, then I'm like, oh man, is it… no, no, no, like, it… it's more brain power to me.
And that's why, at a glance, oh, that's about BGP, that's not the one I want.
Where if it says peer, then I have to pause and my brain has to think about Is that the peer thing that I'm actually looking for at the moment? Or think about sorting something alphabetically.
Yeah, I… I personally don't like that. I'd rather keep it BGP to start with.
I don't know, do you have a… do you have a different way you process it?
**Sven Cowart (ElastiFlow Inc)** 22:23 I… yeah, I don't… I don't have that cognitive overload from that. For me, it just makes it consistent, and what…
**RC Rob Cowart** 22:29 overwhelming sufficient.
**Sven Cowart (ElastiFlow Inc)** 22:30 The way… the way I read it is network.
pier.bgp. Okay, I'm describing the pier, and I'm describing things that are related to BGP about that pier.
That's…
**RC Rob Cowart** 22:43 No, but that's… see, this gets back to this word, this confusing thing. Network.peer is about an endpoint that I'm related to. A BGP peer is a very specific thing.
You get what I'm saying?
**Sven Cowart (ElastiFlow Inc)** 23:09 Yeah, I just… I don't… I don't… I don't… I don't think anywhere network.peer is defined as the endpoint.
As an endpoint.
**RC Rob Cowart** 23:17 decided it was.
The use of peer and local, right after the word NETERT, already have a given meaning, and we just decided that we will keep that consistency with that current meaning.
**Sven Cowart (ElastiFlow Inc)** 23:38 And let's not keep it.
**RC Rob Cowart** 23:40 Okay, then we go back to changing everything to be peer underscore BGP, then.
**Sven Cowart (ElastiFlow Inc)** 23:46 That's… that… yeah, I mean, I think that's cleaner, but I…
**RC Rob Cowart** 23:52 I don't know, does anyone else have an opinion? I'm just curious, like, you know.
By the way, me and Sven get in more heated topics all the… debates all the time. Ignore us going back and forth, so… Does… Does anyone have any thoughts there?
Mark or Giuseppe?
**Giuseppe Ognibene (Coralogix)** 24:15 Hmm, I was thinking about.
**MARC NETTERFIELD** 24:16 I will admit, I'm one foot out the door, because I'm in an airport right now, so just kind of trying to follow along.
**RC Rob Cowart** 24:23 Got it So to me, Sven, I'm just trying to say, you know, for that entity type, I want to keep things that are specific to that entity type prefixed with the entity type.
**Sven Cowart (ElastiFlow Inc)** 24:40 Yeah.
**RC Rob Cowart** 24:41 and to me, a BGP peer is… is… It's a very specific thing.
**Sven Cowart (ElastiFlow Inc)** 24:49 I just haven't seen that tight coupling anywhere else in the entity definitions that I've looked at.
I could be very wrong.
**RC Rob Cowart** 24:56 I can go back through and check. I thought I was being somewhat consistent there, but, Certainly could be wrong about it.
I always feel like when I look at stuff, if there's anything to look at, it's usually, like, Kubernetes has the wide, you know, K8 has the widest array of things to look at.
What the heck, am I on, like, a wrong version or something?
Oh yeah, it looked like I was.
**Sven Cowart (ElastiFlow Inc)** 26:14 Okay. I think you might be right about this.
**RC Rob Cowart** 26:18 Do you have an example? Because I can't even find K8s right now. Do you have an example that you could put.
**Sven Cowart (ElastiFlow Inc)** 26:22 Yeah, do you want me to share?
**RC Rob Cowart** 26:24 Yeah, please.
**Sven Cowart (ElastiFlow Inc)** 26:35 Oh.
**RC Rob Cowart** 26:36 Yeah, there you go. Cluster. Cluster, cluster, yeah.
**Sven Cowart (ElastiFlow Inc)** 26:39 And it's… it's the same all the way down.
Just curious about some of these other ones.
It's, like, not enough done to really know.
Yeah, alright, so… I think you're right there.
**RC Rob Cowart** 27:26 I mean, at least we can get started with this as, like, an initial draft, and then, you know, there's still… still discussed comments on it.
**Sven Cowart (ElastiFlow Inc)** 27:37 I guess the, well, it could still be accurate, though, the way I described it.
Because… Like, here they're using dot notation inside the entity's name.
K8, stop, cluster.
**RC Rob Cowart** 27:56 Well, but isn't K8s the higher level thing? Just like Network.
**Sven Cowart (ElastiFlow Inc)** 28:04 Well, sure, but that's… Like, for example, OS… no, where was that one I just saw?
Or it was a single level.
Yeah, like, host is just host.
**RC Rob Cowart** 28:19 Well, yeah, I mean, I think that applies correctly to that one.
We're gonna need host network stuff as well, though.
**Sven Cowart (ElastiFlow Inc)** 28:27 All I'm saying is there's already a pattern established where you're using dots. That, I mean, that would be the question that needs to be asked and clarified.
within the entity SIG is, like, what is the naming standards for these things?
Because in this case, it would be… in our case, your way would be K… or network.bgp underscore peer.
And with what I'm saying, it would be… Network.peter.bgp.
That will be the entity's name.
Or the type.
Like, I haven't seen any rule that says you can't have three parts to…
**RC Rob Cowart** 29:06 No one's saying you can't have 3 parts. I'm not making that argument.
The argument I was making is that .peer alone peer.
Not peer BGP. Pier alone already has a meaning. So if you put a dot after the peer, so if you say network.peer, that already has meaning. If you put a dot after the peer, you're basically saying.
Everything after the network.peer.
is subservient to that existing meaning of peer, and I'm saying that's not the case here.
**Sven Cowart (ElastiFlow Inc)** 29:49 what's not the case? That they're not doing this here? Yeah. But… or that…
**RC Rob Cowart** 29:54 No, I'm saying that everything after network.peer.
For those other attributes, Is not necessarily subservient to that existing definition of network.peer.
**Sven Cowart (ElastiFlow Inc)** 30:11 Oh, that's not true.
I mean, there's… There's more labels used on these things than Or there's more attributes that exist outside of just the entity definition.
On a number of these entities.
**RC Rob Cowart** 30:31 I'm not talking about these, I'm talking about the ones that I was… that I have over on my sheet.
**Sven Cowart (ElastiFlow Inc)** 30:36 diet.
**RC Rob Cowart** 30:37 That's what I'm talking about. It's specifically because of that word, peer already has a pre-existing meaning. Networking.peer.al already has a pre-existing purpose and meaning.
If we're changing that a little bit.
**Sven Cowart (ElastiFlow Inc)** 30:51 That's what I'm saying, yeah, we'll change that. I thought we said we could do that if we go that route.
**RC Rob Cowart** 31:03 Yeah, I don't know, that… that wasn't what I was… I was necessarily thinking I was saying, but… I guess maybe I'm just getting confused, then, on my understanding of how some of this stuff is designed to work.
**Sven Cowart (ElastiFlow Inc)** 31:24 I don't think it is defined yet, that's the problem.
**MARC NETTERFIELD** 31:36 Excuse me, jumping in a little bit here. Are we kind of debating if it's gonna be, like, network.bgp.beer, and also network.peer.whatever, or…
**RC Rob Cowart** 31:46 dot BGP, yeah.
**MARC NETTERFIELD** 31:48 Oh, okay.
**RC Rob Cowart** 31:52 So, so my, my feeling was this, that under network.
You would likely want to have, as the next thing after network dot, you would want to have the entity type.
It's kind of be that next level thing down.
And… starting with the whole topic of BGP, there's, like, you know, BGP, basically the process that runs on the network device, or the instance of the process, if you have virtual, like, VRFs.
There are peer relationships, there are paths, there are, you know, there's a few other… there's prefixes, there's a few other… entity types, there'll be about 5 is what I have at the moment, that'll be built out. They have relationships to each other, and then… And so, I was thinking, network dot, entity type dot.
And then all the attributes related to that entity type.
**Sven Cowart (ElastiFlow Inc)** 33:03 Right, but if… if what you're saying is that network.peer.
Has a definition that doesn't fit that BGP peer entity type.
then you can't use peer.address either.
And that's where I'm like, we have to change the definition.
Or… like, we can… I don't think we should mix the two concepts, and right now, what's the way it is in the last way you showed it on screen, the concepts are mixed. And I'm okay saying that, opening up the definition, that something can be more than one thing.
Which I think is actually really useful, because then it avoids the downstream pressure of having an explosion of addresses.
in different attributes. Because for every routing protocol, then, we're going to have to have a new address field.
If we go with the concept of it's .bgp underscore peer dot address, or… You know what I mean.
**RC Rob Cowart** 34:06 Yeah, I mean, the… I guess the question is, where does the specific part come in?
Right? And what I mean by that, where does a specific part come in, is like, If I just give you an IP address, you'll know what that IP address is.
if I tell you… It's my BGP peer's IP address. Now you know exactly what that IP address is. It's an IP address on a router that I have a peering adjacency with.
**Sven Cowart (ElastiFlow Inc)** 34:38 You know?
**RC Rob Cowart** 34:39 And… So, what creates that specificity?
the entity type.
Or something else in the attribute name.
**Sven Cowart (ElastiFlow Inc)** 34:57 I would… Say it's the entity type.
So that we don't have to explode how many address attributes exist.
**RC Rob Cowart** 35:04 And this is probably where the lack of definition comes in, because the entity group is just… I mean.
as I told you from my couple times I've been on calls with them, I almost felt like they were like.
oh, great, someone is gonna actually do some stuff related to entities now. Like, we might be the first big use case, you know, that actually tries to use the whole entities concept, like doing entities first, then going… doing attributes for those entities, you know?
**Sven Cowart (ElastiFlow Inc)** 35:33 Yep.
But… and… and that's… and that's… I mean, this is… Because I want to…
**RC Rob Cowart** 35:40 I'm gonna put both… both versions up, and then we can… we can discuss around it.
**Sven Cowart (ElastiFlow Inc)** 35:47 Yeah, I mean, I think you just need to present it in the semantic conventions group, or…
**RC Rob Cowart** 35:51 That's fine, too.
**Sven Cowart (ElastiFlow Inc)** 35:52 Yeah, or… and the entities group.
Because, I mean, really, this needs to become, like, a heuristic that everyone who writes entities needs to follow. Otherwise, things will become inconsistent.
But my biggest concern is… address attribute explosion. Like, it's gonna… I can… I have to look at an attribute, if it's related to one another, and as an end application developer, in 15 different places.
And that sucks.
**RC Rob Cowart** 36:31 I think the key thing there, if we… let's just stick with this IP thing for a second, though, and this comes back to what you and I were talking about just the other day, Sven, is, like, with source destination. What I care about is really 3 pieces of information.
A source, a destination, And which end initiated the conversation?
**Sven Cowart (ElastiFlow Inc)** 36:51 Yep.
**RC Rob Cowart** 36:51 you know, I don't really need client-server if I have the other three, because I derive whether you want to call it client, server, initiator, responder, whatever, I can derive that from those three pieces of information, of source, destination, and which end initiated the conversation.
Yeah.
the… And in this case, what we're saying then, if you're gonna use Network.peer.address, network.local.address, totally fine.
But you must also have something else that specifies whether it's a field or the entity type itself that specifies what that IP address specifically is, like, the context of why it's even being shared with you, basically.
**Sven Cowart (ElastiFlow Inc)** 37:38 Yep.
**RC Rob Cowart** 37:42 Okay, let me… let's do this, then. Divide and conquer?
I can't do both of them calls.
If you want to discuss attributes, some type of defined best practice, standardized attributes around IP address on the semantic convention SIG, that's fine, and I can then join the entity SIG later today and ask my questions related to this.
**Sven Cowart (ElastiFlow Inc)** 38:07 Okay.
**RC Rob Cowart** 38:07 I just can't do both, I don't have enough time today to do both.
**Sven Cowart (ElastiFlow Inc)** 38:11 Is there some… is there Lude Miller or Thrask on the entity SIG on a regular basis, do you know?
**RC Rob Cowart** 38:16 Hold on, I'll tell you who… Is it Thrasp that's on that?
Might be, actually.
**Sven Cowart (ElastiFlow Inc)** 38:29 Yeah, it's today.
**RC Rob Cowart** 38:31 Yeah, I know it's today, I'm usually… I have it on my calendar.
Josh, that's who's generally running it when I'm on it, yeah.
**Sven Cowart (ElastiFlow Inc)** 38:40 Oh, okay, that should be fine.
**RC Rob Cowart** 38:41 Yep.
**Sven Cowart (ElastiFlow Inc)** 38:44 Just, he used to be part of the entity SIG group, or Semantic Convention SIG.
**RC Rob Cowart** 38:49 Okay.
**Sven Cowart (ElastiFlow Inc)** 38:50 For political reasons, had to move.
**RC Rob Cowart** 38:54 Too many people in one company, right?
**Sven Cowart (ElastiFlow Inc)** 38:56 Yep.
**RC Rob Cowart** 38:58 Okay.
**Sven Cowart (ElastiFlow Inc)** 39:02 Alright, that sounds good.
**RC Rob Cowart** 39:05 But, I think the main thing going away from this is… That we were discussing last week was, Do we completely abandon NetworkLocal.address, networkpeer.address, and I think the answer here, after going through some examples, is there's an opportunity that we don't have to.
**Sven Cowart (ElastiFlow Inc)** 39:26 Yeah.
**RC Rob Cowart** 39:26 Nope.
**Sven Cowart (ElastiFlow Inc)** 39:27 Yep. As long as… and I mean, that is part… that relates, that's the second part to the… the PR that… I've opened that is outstanding.
In this PR, right, where I am… Where I explicitly call that out, that… We have not… Cover these pairs yet.
And there's the open question.
Anyways, somewhere in here, there's the open question of, do we want to reuse or come up with something new?
So… In some ways, I will also be asking that question from a different angle.
Today.
**RC Rob Cowart** 40:25 Yep.
**Sven Cowart (ElastiFlow Inc)** 40:25 But whatever comes out of that conversations and these conversations will… I will update this PR before I make it final.
To include that definition of local and peer.
**RC Rob Cowart** 40:39 Okay.
**Sven Cowart (ElastiFlow Inc)** 40:45 Hey, Braydon.
**Braydon Kains (he/him)** 40:48 Hey y'all, I'm hoping I can… my internet stays alive long enough to hear the rest of the call. Sorry, it's storming over here.
**Sven Cowart (ElastiFlow Inc)** 40:56 No worries.
Where are you?
**Braydon Kains (he/him)** 41:00 I'm in, Ontario.
**Sven Cowart (ElastiFlow Inc)** 41:05 you know, I think I was just watching, there's a YouTube guy I follow, I forget his name, Josh something, but he does really good weather forecast, but the Northeast is about to get bombed.
All week long, with crazy storms.
**Braydon Kains (he/him)** 41:19 Yeah, I've seen that in our forecast, too. I'm not planning on doing much.
**Sven Cowart (ElastiFlow Inc)** 41:26 Alright, well, stay safe. I think we are wrapping up here.
**Braydon Kains (he/him)** 41:31 Yep, sorry I was late.
**Sven Cowart (ElastiFlow Inc)** 41:33 No worries.
Alright, take care, everyone. Bye.
**RC Rob Cowart** 41:37 That's all.
**Giuseppe Ognibene (Coralogix)** 41:41 Bye.
