SIG: Network SIG
Date: 2026-06-16
Duration: 46 minutes
============================================================

## Zoom Recording Transcript

**Stephen Lang** 02:54 Oh, it looks like there's a handful of people.
**Sven Cowart** 02:57 Right.
Say it again?
**Stephen Lang** 02:59 I said it looks like there's a handful of people.
**Sven Cowart** 03:01 Yeah.
**Antonio Jimenez** 03:03 Hey, guys.
**Sven Cowart** 03:04 Hello.
**Giuseppe Ognibene | Coralogix** 03:07 Erdogan.
**Sven Cowart** 03:15 So, to kick this off, I think, Probably good to talk about what was covered in yesterday's semantic convention call. Were any of you on there?
By any chance? No. Okay, so we're still trying to figure out exactly, how to approach… this, group, or SIG, and, Where it's landed now is that… there's a GenAI SIG that has its own project in GitHub that's a federated project, so Federated semantic conventions project, and the… Thrask encouraged us to pursue it in that way, which means we still need to start up a… a… create a project proposal, and the project proposal would get added to the community projects inside of that… the community repo, and… and then… we would be a federated semantic conventions group with our own list of maintainers and improvers, inside that repo. And… And then… for… One other key call-out was that, we need somebody like Braden, who's had the experience number of years of experience contributing semantic conventions, making sure that the context around these things don't get lost, so he needs to continue to stay in this. And then, also making sure that We continue to connect with the system SIG.
and the regular SIG, and the OBI SIG, for that matter, I think, too, to make sure that Because the network touches all those parts, and we need to be clear around where to go there.
as a next step, I think the… the… one of the… I think, yeah, the next step is just creating that project proposal, I'd probably say.
And… and then move from there, and start addressing some of these issues that have come up, and wrangle them.
**Antonio Jimenez** 05:26 Hey, I remember Brandon created, a GitHub issue with kind of that goal to create that group. Do we still need a separate ticket for creating the project, or can we… keep that ticket, I think you qualify, huh?
If I have it wrong, let me check it out.
**Sven Cowart** 05:47 I have it, you're talking about… this, I'll share my screen real quick.
**Antonio Jimenez** 05:52 Nice.
**Sven Cowart** 05:56 Hold on, can I share just that one window? I didn't want to share everything.
**Antonio Jimenez** 06:06 Correct, the title was New Working Group Networking.
**Sven Cowart** 06:10 Oh, sorry, wrong one, yeah. Sorry, I have a bunch of… I have a tab that's… All of them.
**Antonio Jimenez** 06:17 I put it in the chat.
So that one is…
**Sven Cowart** 06:23 There we go, this one, right?
**Antonio Jimenez** 06:26 Yeah, exactly. That ticket is getting a little bit crazy in the sense, like, everyone is having a discussion that they want, and people is trying to answer to those discussions, even as a comment, so I don't think that's a procedure for sure, but the goal of that ticket was clear, like, we need a new group For folks that are, kind of, expert on that field, are interested on it.
**Sven Cowart** 06:52 Yep, exactly. So, this is the example that… Crass pointed out the semantic conventions Gen AI, we should have a semantic conventions network.
repo, which acts as a federated semantic conventions group, and… and then… I guess the question, like, I think the problem I have is I could do all this stuff, I just don't have access to doing any of this stuff, right? So who's the person who has access to creating a new repo, a project board.
And… and so on, then, for this, for this work. Because ideally, where I think, like, part of this is getting a little out of hand and crazy.
We need to start taking these issues and putting them on a project board, and then being… creating a cadence on this, on this call, around those issues to… to touch on them, make sure they're all moving forward.
I just don't have access to it, so I think… I think it's what…
**RC Robert Cowart** 07:53 needs to do for us, though, isn't it? As a next step?
Or is there some approval that needs to happen first?
**Sven Cowart** 08:01 I think a next… as a next step, what we need to do is… is create one of these.
Because this is the official request, this is the project proposal, right? This is the official request, then, to have all these things filled out.
And we should just use the… Is the… did they submit one of these for Gen AI?
Yeah.
Like, we can probably use this as a template.
So, use the template, use this as a guide to generate I1, and then do that. That was gonna be my next step to do that, or someone else can do it.
**RC Robert Cowart** 08:50 I mean, I'm happy to collaborate on it, so… Yeah.
if anyone else has input they want to put into it, but I'm happy to spend some time on it too, so…
**Sven Cowart** 09:04 The other thing to call out, I think, is…
**RC Robert Cowart** 09:07 Real quick, are you just gonna make a PR or something, Sven, or a branch for something that…
**Sven Cowart** 09:11 Yep, yep, and then I'll… I'll just link to that other issue, the one.
that has all the brain dump of everyone's thoughts and ideas right now about the new working group linked to that and, in the PR.
And that's the official stake in the ground. I hope, then, that… I don't even know if Braden has access to that, but he has… From my understanding, it seemed like he has influence.
Because he works directly with Thrask and those people, so, company.
You're laughing, Antonio.
**Antonio Jimenez** 09:46 But I think you're right, like, Brandon, I don't think he's needed a maintainer, so we are gonna need much, like, a trans or Blumidla here to… to approve that, and then we can go ahead. But this is… because that was exactly what he mentioned in the ticket, when he created, like, Trask or Luminda.
And… proposed that, so he was on… he did that on their behalf. So, I mean, we will need their approval, for sure, here.
**Sven Cowart** 10:16 No.
**RC Robert Cowart** 10:18 But both me and Sven were on the… the… semantic convention call the SIG call yesterday, and it seemed like it was… the support's there.
**Sven Cowart** 10:29 Yeah.
Yeah, everybody wants it.
**RC Robert Cowart** 10:32 Their main suggestion was just to have a representative kind of of that group, so, you know. So we're probably gonna have to move this call, basically, but.
**Antonio Jimenez** 10:44 Let me explain it.
**Sven Cowart** 10:48 And I think as part of the project plan, the initial one, we just need to, like, We'll need to create milestones and probably group around efforts to focus on first, and then move forward, because There's a lot to be done. Right now, my understanding is we're going to continue to use the OTEL network.
Slack channel to communicate.
And we might start a new Google Doc, or just add on to the existing one that there is, and… Yeah, it just… Hopefully by the end of this week, we'll have all the… This, what feels like paperwork done, and then we can start organizing ourselves in a meaningful way.
That's my goal, anyways.
One call-out that's worth mentioning is, and as we're thinking about these issues, and you guys are all thinking about it, was that there's likely a A core set of network attributes.
That we're gonna have to… get approval through the semantic conventions Group, and this is things like source and destination areas, for example, is two areas where you have Like, we need to… like, one thing that comes to mind, I haven't even opened this issue yet, this is another one I was going to open, but there's an issue in source and destination area that, the .address is… can be anything.
And it can't… meaning it can be an IP address, a hostname, a… all types of different things, and that can be very bad, especially when you need to communicate, actually, an IP address and a hostname is two different fields. Like, whoa, which one… how do you do that, right? And reconcile that. So, I think there's a lot of improvements on some of the basic stuff that is core to all of OpenTelemetry that needs to be added, and then… And then a much more specific, network-specific attributes and semantic conventions that need to be figured out.
Anyways… I don't… Dude, do we have anything that specifically we want to talk about here?
**Antonio Jimenez** 13:01 I have a few issues that I would like to discuss, but I agree that that makes more sense to have, like, have them in a board and review when more people get attraction, not maybe just ask. I'm fine also talking now, but it's gonna be hard to reach an agreement, most likely.
But… Yeah. That should be fair, guys.
**Sven Cowart** 13:24 What are the… Oh, yeah, okay. Yeah, I wouldn't mind just look… Yeah, why don't you show… show what you're…
**Antonio Jimenez** 13:36 Let me know that. Let me share my screen.
Just kidding.
Okay, so I was using, as you… you were mentioning before, are you using the network group.
And then I put here the three options. So those are things that we are already proposing to be done in Thousand Eyes, part of Tisco. One is the AP prefix, so let me go to that ticket. I know some folks from the call already commented out here, which is great. So, we have the existing, network peer address attribute that all of you might be familiar. So, the proposing is network peer address prefix. I know that there was some back and forth on… we went to… to that suggestion at the end, network peer at this prefix. The main reason was because, If we use the other one, that one that I was suggesting initially, that is gonna be, that is going to contain a prefix that is actually an actual attribute, which is not the current approach to follow. That's why it was suggested to go into that direction. It was suggested by Robert, I think Robert is also in the call… Rob, sorry.
So that's the suggestion, and all of you are familiar with what prefix means. There is a FC for that. We describe it well. The goal is, like, it will look like something like that. It will be a string.
For sure, development for, for the time, for the beginning.
Yeah, that's the idea. I don't know if it makes kind of sense for you guys, or you want to change, propose something different.
**Sven Cowart** 15:29 Makes a lot of sense to me.
There was… some chatter…
**RC Robert Cowart** 15:37 I will say… I'm sorry, Sven, to interrupt, sorry, go on.
**Sven Cowart** 15:41 Go ahead. Yeah.
**RC Robert Cowart** 15:42 I was gonna say, by the way, my comments were primarily around the address prefix part.
I know that network peer thing is… pre-existing?
I'm not gonna lie, I have a problem with peer. Like, it's just such a non-specific, overloaded term. I don't see how it makes any… like, for example, is a peer, like, a OSPF neighbor, or like… you know, is it a web server on the other side of an HTTP call? Is it a… you know, is it a Layer 2?
you know, is it like a… you know what I'm saying? Like a direct Layer 2 connection?
I don't know. Like, it's just, like, peer means nothing to me, and everything at the same time, you know what I mean? It's like, it almost makes me wonder if network peer is going to stay as a… as a valid term. It begs to have network.peer.type.
That, that goes along with it.
**Antonio Jimenez** 16:52 I see… I see your point. The way how I understood it, at least, is, like, local means, like, the… some sort of source, and peer means, for me, the destination. This is at least how I understood it, both of them. Like, local is, like, who is doing the request, and peer is, like.
to who you are, Nicole. At least this is the way how we are treating it in socialize. Like, we have our… source, and then we have our destination. But yeah, you… I agree in the sense, like, PR might be too generic. For the use case that I explained, would make way more sense, like, source and destination, but yeah.
**RC Robert Cowart** 17:26 So, so yeah, so, if we're saying, like, peer is always, like, remote.
**Antonio Jimenez** 17:32 That's the way how I use it today.
**RC Robert Cowart** 17:35 I see.
**Sven Cowart** 17:41 Why… why not just use, sourceanddestination.address?
**Antonio Jimenez** 17:47 Yeah, that would be perfect, but I don't know why that decision was taken before.
And I don't think it's… I see change today.
As they are considered as stable, too.
**Sven Cowart** 17:57 Yeah, that… these two have actually always confused me for that… Because they seem at odds with… Source and destination.
And… So…
**RC Robert Cowart** 18:13 For me, it's just always about, like.
And I could agree with this definition.
If we're talking about a message being sent from one place to another, that, to me, is… it's either source destination or client server.
If you're just talking about two related things.
again, BGP peer, OSPF neighbor, that type of thing, right? Like.
I'm not necessarily specifically saying that, you know, I'm not trying to talk about or… or imply a direction of information flow, I'm simply trying to talk about two things that have some type of relationship across the network.
okay, this could make sense, you know? Having said that, though, like… I… I don't know, I guess this is just where my brain is, and if, like, if someone is willing to say, like, oh, no, in OTEL, we have this different approach, I'm more than happy to listen. But I do think about, like, technology-specific terms.
Because in BGP, it's called a peer. In OSPF, it's called a neighbor. So if I had, like, network.ospf.
I'd use the word neighbor, but if I had network.bgp. I'd use the word peer, you know, just because those are the… that's the vernacular of those technologies.
Now, you could argue, though, we're just gonna… we're just gonna say local and peer are referring to, A relationship that's not necessarily implying a flow of traffic.
You know, like, specifically about a flow of traffic. And we're going to use local and pier. Local being near end, pier being far end.
And, and then there's some type of… I just feel like there has to be a type field then, so that you could say, oh, this is… Network.peer.type is… BGPpeer. Network.peer.type is OSPFneighbor. Network.peer.type is… LLDP… You know, whatever port or whatever on the other end, you know?
**Sven Cowart** 20:35 Yeah, it's not too different than… I mean, that's how they did it up there in the connection one, so… Is there some parity there.
**RC Robert Cowart** 20:42 Yeah, no.
**Sven Cowart** 20:43 Where they have connection type.
**RC Robert Cowart** 20:48 Oh, man, that's…
**Stephen Lang** 20:50 There must be some route to address the stability of stable, though. Like, surely it can't be… once it's stable, it's written in stone. There must be some kind of… deprecation process, or, you know, a V2.
Because, I mean, for… From my side.
Is there anything to prevent a peer from being local?
And… because then it's… maybe they're not mutually exclusive with local, so local and peer, they could both be local, right?
**RC Robert Cowart** 21:19 I agree with you. Like, local and remote makes more sense to me, and peer is more of a relationship type.
**Stephen Lang** 21:34 So my point is, maybe if it's listed as stable, we don't have to take that as it will be stable.
Forever, and this is the way that it has to be, especially considering that A number of new conventions that might be coming in as part of this group.
Maybe we need to consider How to adapt to the currently stable attributes.
**RC Robert Cowart** 21:57 The good news is the list isn't very long.
**Stephen Lang** 22:03 Because, I mean, you could do something, surely, like network.v2, and then say everything under that namespace is… Entirely new and up for grabs.
And that doesn't necessarily destroy the current attributes, but it potentially duplicates them, which could be a problem. I'm just thinking, like, what are the approaches for addressing.
**Sven Cowart** 22:23 Yeah.
**Stephen Lang** 22:23 A stable attribute which might not be ideal long-term.
**Antonio Jimenez** 22:28 I think this is where we need those people who have expertise in multi-convention, because I also see other paths where we can call it, like, network.remote or network.destination, and keep peer also stable, and using it at the same time on the other as development, and then if we see people Believe more on that, we will deprecate the other, but both of them could live for a time period.
I mean, this is the big problem of standardization, like, it's never go quick.
For you.
**Sven Cowart** 22:58 I… I… what's probably best is to… As part of the issue you raised.
I would say we need to address this problem, the local and peer, like, Like, the fact that we don't agree with that wording here.
And… and then use that as a common… And I can do it, anyone else can do it too, so if somebody wants to volunteer, bring that up in the semantic conventions call on Monday, and say, like, we have a problem with some of the, like, core structures of the… what is there today in the network area.
And here's one of the ways that we already identified that we want to change that. What would it look like for us to Steven, do what you're saying, deprecate something that is stable in favor of a new idea, and then as part of that new idea, we can also then address this prefix thing that you're bringing up here.
Because I…
**Antonio Jimenez** 23:53 I… I think… both of them could go separated, but yeah, I don't have a problem addressing both together.
**RC Robert Cowart** 24:03 I'm kind of curious on this one. This was the other thing when I looked at this.
The other word that immediately bothered me was address.
just because… It's an IP address. It's… for example, it's not a MAC address.
Or, you know, like, there's multiple addresses that… also in networking, but is that… is that more broadly across the OTEL thing, is just address used to refer to an IP?
**Sven Cowart** 24:34 Well, I… that's actually my earlier point, even if you look at source and destination area, address is defined as, yeah, an IP address or a socket name, and then even to make it worse, in the source and destination, it could also be a host name.
**RC Robert Cowart** 24:51 Oh, okay, so address is just more like a generic catch-all.
**Sven Cowart** 24:55 Yes.
**RC Robert Cowart** 24:57 Okay.
**Stephen Lang** 25:00 So, I believe if an attribute is more broadly defined, it would be within an entity?
I don't know if there's any… I'm not too familiar with these.
network, SEMConf, if there is any existing entities.
I don't know if anybody knows.
**RC Robert Cowart** 25:17 So apparently they're starting to do something, related to systems, some network entities. I haven't looked it up yet, though, but apparently something is starting there.
So, I have it on my to-do list to look it up and review it, just because I'm curious where they're going.
But it does make me wonder, like, I mean, look, every network interface in a modern network actually, I shouldn't say that. Like, a network interface on a switch doesn't necessarily have an IP address, but, like.
Every network interface on a server, for the most part, has a MAC address and an IP address.
So, and especially when I see Socket, it makes me think about, Something more logical as opposed to something more… that's true network layer.
You know.
Anyway, I just think there's a duplicity there that a single address field cannot catch.
You'd have to have multiple attributes, not a single attribute.
**Stephen Lang** 26:28 So this is probably where, if, like, an individual attribute.
is going to be changed, it might be easier, but if it's part of a shared entity that could go across many SIGs, that might be where it's, could be more difficult to track, and it's probably better to get in earlier, especially if the system SIG are thinking about network entities.
I guess this is probably where the overlap is going to be with with this.
**RC Robert Cowart** 26:57 Okay, so it sounds like that's probably a more pertinent next step, then.
**Stephen Lang** 27:06 Yeah, so I think it would make sense for this group to preempt what's going on with the network entities in the system's sake, otherwise… That runs the risk of introducing terms.
Which could spread.
And it could be fragmented with the network CENCOM that we're thinking about here.
So if you wanted consistency between the new SEMCOM that's been introduced as part of this project.
And, you know, the work going on in the other SIGs, it makes sense to try and align the two, especially at the entity level, I suppose is what I'm trying to say.
**RC Robert Cowart** 27:39 I, I'm, I'm happy to, to take, take a to-do on that.
**Stephen Lang** 27:53 And it's.
**RC Robert Cowart** 27:54 Taking some documents there, but…
**Stephen Lang** 27:55 Great, thank you. Yeah, Sven, for this document that you're thinking of creating, I wonder if it's worth highlighting the exact areas that do overlap with other existing SIGs, and maybe part of the project effort is that we even assign, you know…
**Sven Cowart** 28:13 Yes.
**Stephen Lang** 28:14 Have some kind of, like, ongoing thing that we do, which is to stay up to date with the overlapping parts.
**Sven Cowart** 28:21 That's… nope.
**Stephen Lang** 28:22 Yeah.
**Sven Cowart** 28:46 Okay.
So, as far as… Northwest, yep.
that first IP prefix thing, I think.
It makes the most sense, though, to… Instead of adding yet another Attribute to something that we think might change.
Let's get the… Let's get the attribute name.
before even the address prefix, like, is it gonna be .peer, or is it gonna be something else agreed upon first? So that we can then, as a part of that.
Addition or change, also add in address prefix, or things like… Addressing the concern around The… the overuse of .address, and specifically these network attributes.
And make that one holistic, kind of… Add.
So otherwise, it just seems like we're gonna do a bunch of extra work.
**Antonio Jimenez** 29:41 Correct, because it could also be, like, address dot… MAC, or address.ip, or address.prefix. That's what makes sense to me.
**Sven Cowart** 29:50 Yep.
**RC Robert Cowart** 29:51 Yeah, I suspect when that attribute was created, the thought was more of, like.
I'm an application running on an endpoint, and I need to connect to something over the network, so I need to, like… what address am I talking with? Which could be some variety of things, where when we talk about network, we're talking about very specific things, related to various locations on the network stack, so…
**Sven Cowart** 30:15 just seeing how client or server.address is used in the downstream applications, they're often just, like, identifiers to kind of signal, hey, we're talking about this thing, right? And so, I think it came from that perspective. It's like, oh, I need to show in a table in Grafana this is the app that I'm talking about, identified either by hostname or IP address or something of that, and… I think it got overloaded then, and now that we're going to network domain, it doesn't fit anymore.
But it does bring up the question of, like.
if we now reuse ad… or .address.star, I would be concerned that it creates confusion with what is already in client server and source destination.
I don't have a better word to use, so that's a little bit of the problem.
**Stephen Lang** 31:05 I mean, it might be that there's two things. There's the specifics of the network side, but it might be intentionally open-ended, because you know, both an IP address or a hostname would resolve.
For a certain application configuration. So maybe it is address, and it's intentionally vague, because you don't actually know beforehand whether an IP address or a hostname is going to be used. Maybe the application accepts both and will just emit whatever it is configured with.
So, maybe there's a case for you would have some general attributes.
If you don't know what it is exactly that you're going to be dealing with in that attribute.
**Sven Cowart** 31:46 You know?
**Stephen Lang** 31:47 Or it could be, depending on your use case, you know exactly what it's going to be, and you could determine You know, what the type is, what you really mean by address, and in which case there's another attribute that you could use.
Yeah. Because if you have too specific an attribute, then the applications that don't know what that's going to be could misuse that and, you know, put something like an IP address in What's supposed to be in a hostname, and give it just the wrong meaning.
So, something that's probably going to be difficult with overlapping with other less specific Use cases is… might be just this point, that maybe they don't know the specific type that it is that they're dealing with, if that makes sense.
**Sven Cowart** 32:28 Yeah, it totally makes sense, and the specific type's not always available either, if you're talking about, like, from instrumenting something inside the application, or the application layer. And… I… my point was more about… I doubt we're gonna be able to get any buy-in by adding more stuff to address.star, right? Because address already has a specific meaning, so we would probably have more buy-in if it's something like network.local.mac, network.local.ip.
instead of trying to add it onto .address, because it already has that very generic meaning across many things in OpenTelemetry.
**Antonio Jimenez** 33:10 Yep.
**Sven Cowart** 33:16 And that does mean, and this is something I haven't quite figured out, like, if you need the specificity of, like, IP, or .ip.mac.host name.
then do you duplicate one of those values, depending on if it's available inside a .address? And… will it… And I think that's more of a… a actual instrumentation question, what… how people want to go about using those attributes, but it does beg the question of, like, there might be some data duplication there, depending on how someone might implement it, and… Yeah, I haven't figured out how to wrangle that.
Unfortunately, when we built Mermin, I had the same problem, and I now have duplicate data on some of the fields because of the inherent problem of the generic nature of address. But I needed to also communicate host name, and like, I need an IP address and hostname, so I put hostname into address, and then created a .ip for the IP address, and Yeah, there was other things there, but…
**RC Robert Cowart** 34:26 It's just important also to know, like.
I think there are clearly IP addresses and going to be, because When you store them on the back end, right, lots of data stores are gonna support queries by CIDR block and things like that, you know, and… and if… if you can't guarantee the field is an IP, Then, you lose a lot of… You know, observability application optimization and flexibility, you know.
**Antonio Jimenez** 34:59 Yeah, follow the conversation with the host name. The other proposal that they have that you can find out in the list of tickets is, like, the reverse DNS. So, in Thousandize, what we do is, like, we have an IP, and in order to provide to the customer which first name that belong to, we use a reverse DNS.
And then I was… initially, I was proposing something on those lines, network peer DNS name. After some conversation with different experts on the domain, we came with the concussion of network PR hostname, which is kind of what you are saying, in the sense, like, we… our address is quite generic, so we kind of put it on top of address.
address, if you see the documentation, is not for hostname, really, it's more for socket name, as they are calling it here, so it didn't fall neither. That's why we were suggesting, network peer address, but maybe now we want to go more in… in a different direction if… if we… Introduce, like, remote, or if we introduce destination?
Yep.
Sure.
That's also fall under the same circumstances.
**Sven Cowart** 36:11 I think this is the right move.
By the way, I think the… the… let me find it really quickly, the, documentation on… that I was referring to.
So, this is… And this is, oh, I can't.
take over the screen share. You had to kind of have the page open if… oh, there we go, that works too.
Under source.address, right here it says domain name, if available, without reverse DNS lookup.
And… this just adds one layer of… this is not the exact same attribute, but it is the .address, and this is where I mean there almost needs to be a reconciliation across what .address means across the board on all these different areas, because I do think they should mean the same thing if it's in network.
Dotlocal.address should be the same meaning as source.address, just from a different perspective.
And this is where my confusion came to, because, I mean, yeah, to your point, that doesn't address what you're saying, because you said this was… you were using reverse DNS, but there's other ways to get a domain name that… and… So then, this feels like, man, we're really overloading that .address, and it just becomes a visual identifier in a downstream UI. Like, take the most descriptive one when available, but it's not always available, so… what do you… How do you…
**Antonio Jimenez** 38:06 Sure.
**Sven Cowart** 38:07 Yeah.
**Antonio Jimenez** 38:09 The problem is that that also is overused, in the sense, like, this is mainly used for… the host of my URL, so if you're doing, like, an HTTP request that will be having the host.
So, yeah, it's hard now to… to… to move it. It's, I think, development, I think about, yeah.
Mmm.
It will be hard to convince people around that.
**Sven Cowart** 38:36 And…
**RC Robert Cowart** 38:37 I would love to know what the logic was to exclude reverse DNS in that definition.
**Sven Cowart** 38:46 We should ask.
This is… I mean, this on-server has the same… Same call-out, right? And destination and… Client does do as well.
So as a… I think there's a… there's a… Trying to think, sorry. It all feels like these things all touch the same… core problems that we have with how these attributes are being used. So my question… Just now, like, is… do we address them independently in both of those issues, or is there a more holistic… like, these are core networking definitions and attributes that we need to move forward on so that we can build from that, and instead of trying to… Patch what's already there, piece by piece.
**Antonio Jimenez** 39:48 We should bring up that we would like to… give another thing to the prefix of network.peer, I would say, and if the conversation go in that direction, I would say, in a good direction, I mean, we should for sure wait for that.
And if that entering a loop that we know is never gonna solve, we should… keep adding more attributes on top of that, because if not, we're gonna be blocked for a long period of time. That could be my… my tuition here.
**Sven Cowart** 40:17 Okay, Okay, that makes sense.
**Antonio Jimenez** 40:26 So once we create… once we create that group, maybe try to give priority to proposals for our network peer, maybe destination or remote, makes sense, and then later we should decide what we say instead of address. Do we go directly to .ip, or .mac, or .host name?
Yeah.
I think right now.
**RC Robert Cowart** 40:46 What would be helpful is simply to kind of lay out the main blocks, you know, like.
Almost like a… you can even think of it almost as, like, following the OSI layer to a certain degree, but, like… You know, there's… there's things about the physical infrastructure, and what plugs into what, and then there's… things that communicate over the network. And then there's, you know, actually before that, there's the various network protocols that establish even routability, and then, you know, at some point you have the actual traffic. That's where we're getting into source, destination, all that kind of stuff. And just kind of lay out that that hierarchy in the project document, because I think that'll also help reveal, like, here's where we're talking with the system SIG, here's where these other things, these are all network SIG, you know? So I can help a little bit with that diagram, if necessary, so…
**Sven Cowart** 41:43 Sure.
**RC Robert Cowart** 41:44 And then, as you point out, Antonio, like, that would kind of… One of the things we'd be clarifying is, like, there are relationships in networking that are not necessarily referring… like, they're referring to relationships, not… Travel of traffic, necessarily.
You know, so is that what peers are, or is that not, or do we, you know… and so that at least will help us scope the whole conversation.
And then we could… we could get… because I actually think… I agree with you, and I think, Finn, you… I know your work, you'd agree with this, like, those fundamental points have to be cleared up to even then start Scoping where there's entities, and what attributes those entities have, and all that kind of stuff, you know.
**Antonio Jimenez** 42:32 Yep.
Okay, sorry for that, but I have to drop for today, but feel free to keep those conversations with your next… Try to join next Monday… sorry, next Tuesday.
Okay.
**Sven Cowart** 42:44 I guess the last call-out is just be on the lookout for a time, and message what times work for you in hotel telemetry. I'll send a message right after this, so we can figure out a way to reschedule it, and I'll… Figure out who the person is who has access to the calendar invite to get it changed.
**Antonio Jimenez** 43:00 That would be awesome, yeah.
**RC Robert Cowart** 43:02 Alright, I'm gonna put your name on that action item, Sven.
**Sven Cowart** 43:05 Yep. Alright.
Take care.
I don't… I don't think we have anything else to talk about unless someone has something else.
**Giuseppe Ognibene | Coralogix** 43:13 I just want to say, Rob, to Rob, that I updated the proposal. I saw that you will… Gave me a very, very long comment, thank you for that.
I reply to you after one week, if you want to have a discussion, maybe not now.
I saw also that tomorrow you will join the OBC, as you wish.
**RC Robert Cowart** 43:38 Yeah, I thought we were going to talk about it, actually, because they had… they had… you weren't there that one week, and they had said, let's talk about this next week. And then, like, literally got right to me. I would have been next, but we had no more time. So, so yeah, we can… we can just cover it tomorrow.
you know.
But, but…
**Giuseppe Ognibene | Coralogix** 43:56 Maybe… maybe if it will take so much time, we can have also one-on-one, or next time in this network scene, we can have a discussion.
**RC Robert Cowart** 44:09 Yeah, yeah, I'll… I can also try to write up any… any comments back. I did look through your… your reply, and in… and in general, there was one or two items where I thought, okay, let me think about that for a second. But.
**Giuseppe Ognibene | Coralogix** 44:27 Okay.
**RC Robert Cowart** 44:28 Yeah, I think it's going in the right direction.
By the way, we… like, we have our own schema in… internally at Elastiflow that… It's probably, like, the fourth scheme I've ever done. In fact, way back in the original day, we called it Codex, which we were thinking is, like, Community for Data and Event Exchange type of thing. It was more like what OTEL then, you know, has grown up to be in the meantime while we were sitting on our butts, not really trying to do anything publicly, so… But nonetheless, like, we went down this path, and then we… we realized, like, oh my gosh, like, for all those different scenarios, we had different attributes, and like… and we've had it actually as a to-do on our… on our internal schema, and now we're gonna move to OTEL, but the point is, like.
Like, okay, we gotta simplify this to a smaller set of metrics, and then a type field, and a, you know… and that really seems the way to do it, because… And, you know, most of those examples I gave, I mean, there are… there are ways, even, like, in the middle of the network, like, Cisco has application visibility and control, which will give you latency metrics from right in the middle of the path, even, you know? And so, you can get all of that different stuff, and so, It would just be terrible to have, you know.
150 attributes, depending on where you're measuring from, you know? So…
**Giuseppe Ognibene | Coralogix** 45:56 Yeah, yeah, I agree with you. Actually, the proposal to have a more generic way I had a similar proposal, but then we discussed it, and I didn't use it.
Well… Yep, thank you.
**RC Robert Cowart** 46:12 I think we're pretty much on the same page, though, so…
**Sven Cowart** 46:21 Alright, if that's it, then, be on the lookout.
For more information to come.
Alright, thank you. Steven, or is it Stefan or Steven?
**Stephen Lang** 46:32 student.
**Sven Cowart** 46:33 Steven, you work at Grafana, I'm assuming, based on the logos in the background?
**Stephen Lang** 46:38 Bye.
Yeah.
**Sven Cowart** 46:39 Okay, cool. I added… I just… I'm just asking because I added your name to the.
**Stephen Lang** 46:43 Yeah, so, thank you, yeah, appreciate it.
**Sven Cowart** 46:47 Okay, cool.
Take care, everyone. See you next week.
**Stephen Lang** 46:50 Thanks.
**Giuseppe Ognibene | Coralogix** 46:51 My light…
