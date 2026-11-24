SIG: Networking SIG
Date: 2026-11-23
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

Rob Cowart 00:03:08 Hey, everyone. We are, I'm just reading through quickly the notes before we get started here.
Antonio had marked himself also, and Nesso Giuseppe's on, alright.
Hate.
I'm not sure if Sven will be joining or not.
Antonio Martinez (Cisco Systems, Inc.) 00:03:53 Very well.
Rob Cowart 00:03:54 But… oh, there he is. There's Antonio.
Giuseppe, you had the first talking point, Oh, you want to go ahead and cover that?
Giuseppe Ognibene (Coralogix) 00:04:07 Yeah, so, it's a question from the OB SIG. There are two issues open it.
And, they were just asking if we can add it to our hobby 2026 goals, or if he should go to 2027.
As Ben is not in the role, so…
Antonio Martinez (Cisco Systems, Inc.) 00:04:34 Do you know Rob, is when he's supposed to join today, or should we ping him?
Rob Cowart 00:04:39 If Sven… I'm sorry, did you say if Sven was joining?
Antonio Martinez (Cisco Systems, Inc.) 00:04:43 I'm asking you, do you know if he's joining today?
Rob Cowart 00:04:46 He… should be available. I was, I saw it also on his calendar, but… Not 100% sure.
Antonio Martinez (Cisco Systems, Inc.) 00:04:57 Let me ping him. Yeah, I'm ping him.
Rob Cowart 00:04:59 Dude.
Giuseppe Ognibene (Coralogix) 00:05:11 Yeah, but by the way, it's not urgent, like, if we… you would like to go… On the next point, we can wait Sven or… I can send a message on the Slack channel.
Antonio Martinez (Cisco Systems, Inc.) 00:05:23 Do you… Giuseppe, do you know what's missing from those? Like, do you know the status? Let's call it on a better way. Do you know the status of those issues?
Giuseppe Ognibene (Coralogix) 00:05:34 No, honestly, I didn't check.
Antonio Martinez (Cisco Systems, Inc.) 00:05:36 Okay, good.
Giuseppe Ognibene (Coralogix) 00:05:38 Yeah. Sorry, go on.
Antonio Martinez (Cisco Systems, Inc.) 00:05:40 Do you mind… do you mind, like, investigating a little bit and maybe opening a Slack thread on the OTL network group on the…
Giuseppe Ognibene (Coralogix) 00:05:47 Yeah, yeah, yeah.
Antonio Martinez (Cisco Systems, Inc.) 00:05:48 We can discuss it from there. Like… oh, Spanish here, that's cool. From… from a 2026 perspective, it's only one month, a couple of weeks, and we have, I guess, Christmas, everyone is taking a few days off there, so it's kind of one month. So I would say it's time for… for 2026, but for sure, if you let us know what's actually missing, we can… we can provide to you some sort of estimation, I could say.
Is that from my perspective?
Sven Cowart (ElastiFlow Inc) 00:06:22 I just joined, by the way. I saw these.
Being talked about.
Giuseppe Ognibene (Coralogix) 00:06:27 Nice, man.
Antonio Martinez (Cisco Systems, Inc.) 00:06:27 If you want to make the question again, actually?
Giuseppe Ognibene (Coralogix) 00:06:30 Yeah, no, basically, we had the OB SIG last week, and we were going through all the issues opened for the 2026 goals, and there were these two, and Obi folks asking me to… Let them know if this should go on this year's goals or next year.
So it's not urgent, like, please do something now, but just to… To update the status.
Sven Cowart (ElastiFlow Inc) 00:07:00 So here's my, So, before… the reason I haven't done anything with this particular one is because I think we first need to propose what the actual semantic conventions are, because what I don't want to do is merge this code in, and open a PR, and then with certain semantic conventions, and then change them again after They've been circulated and debated on, which I'm sure will cause some change by the time that they actually get accepted. So with that being said, that's why I haven't done the other one. This one here.
it was kind of the same thing a little bit. I wanted to wait until we're sure that These are… the ones, I'm less… concerned about… the ones that are listed here, but when I actually ended up making these code changes, and I have it ready on my local branch for this, this issue. There's a branch I have ready, and the problem with that is, is that because some of the ones… you can see here, source address, source port, source cider, destination address port, CIDR.
There's other things that use source and destination that are still then abbreviated.
And… I didn't want to open a PR that only changes some of these.
And not all of them. And so I wanted to make sure that when I do that, I also make a recommendation for… the other ones, and I just need to circle back on this.
Giuseppe, how… the… I think what I heard, Antonio, you say, the flow one is probably gonna wait. Like, we don't need to do it this year.
I can try to get this 1092 in, or at least have it a PR ready in the next few days.
And then we could close this one out, because I don't think anything that new is introduced here, for flow.direction.
That probably won't be a thing.
Because… We will likely just use… Network.
Direction.
Antonio Martinez (Cisco Systems, Inc.) 00:09:13 Correct. So, for example, in the source address.
It will have local, where it is, network local address, or the source address. For the port, it will be a network local port, where it is here, it is network local port.
CIG is the one that we were selecting here, that was merge it a few months ago, so it will be network PR or network local address. So, yeah, majority of them, if the only thing missing is that table, majority of them, we have it, yeah.
Sven Cowart (ElastiFlow Inc) 00:09:41 Actually, so, sorry, Antonio, actually, those would still be source. So what they are in OB is Source Abbreviated, and then… we wouldn't use the network.local in Pierce, because those are not the.
Antonio Martinez (Cisco Systems, Inc.) 00:09:53 That's beautiful.
Sven Cowart (ElastiFlow Inc) 00:09:53 Oh.
Antonio Martinez (Cisco Systems, Inc.) 00:09:54 I see, I see your point, I see your point.
Sven Cowart (ElastiFlow Inc) 00:09:57 That was the other thing, thank you, you just jogged my memory there. It's been months since I looked at this. I was waiting on CIDR to be established.
And… now we have CIDR ones for source and network.
So we…
Antonio Martinez (Cisco Systems, Inc.) 00:10:11 You can't look.
Sven Cowart (ElastiFlow Inc) 00:10:12 So, that is now… Something we can do.
Rob Cowart 00:10:16 fix, not cider.
Sven Cowart (ElastiFlow Inc) 00:10:18 Yeah, yeah, but I'm talking about the Obi ones, because the Obi called the Dot Cider, and I wanted to not create a new one without it having an established.
Rob Cowart 00:10:26 Oh, yeah, yeah.
Sven Cowart (ElastiFlow Inc) 00:10:28 developmental, yeah.
Rob Cowart 00:10:28 Throw it here.
Sven Cowart (ElastiFlow Inc) 00:10:29 Actually.
Rob Cowart 00:10:30 those side effects. I think…
Sven Cowart (ElastiFlow Inc) 00:10:31 Yeah, so I actually think now I can update this code, and then create a branch finally, because we have that CIDR one.
Antonio Martinez (Cisco Systems, Inc.) 00:10:39 minute.
Rob Cowart 00:10:40 Well, I had a question about flow direction on this one.
What is this… what is that value indicating on the OB side.
Sven Cowart (ElastiFlow Inc) 00:10:54 It would be the same thing that it does for Mermin, so it is a, like a bi-flow representation.
Rob Cowart 00:11:00 Basically, a send or receive.
Sven Cowart (ElastiFlow Inc) 00:11:02 Yes.
Rob Cowart 00:11:03 Okay.
It's…
Sven Cowart (ElastiFlow Inc) 00:11:06 It…
Rob Cowart 00:11:06 I ask about it because… flow direction in, like, NetFlow IPFix data.
is an indication of where the traffic was sampled. On the ingress interface or on the egress interface.
Yeah.
Sven Cowart (ElastiFlow Inc) 00:11:23 So…
Rob Cowart 00:11:24 And so it's a different thing, so it's… it's, you know, even here where it says, like, standardizing as a flow-specific attribute, we… we still need… to me, this is a… these are two different things. Send, receive, and… Where traffic is observed, by something counting it are… are two different things, and we just have to be clear. Like, if I'm coming from the network world and see flow direction, I'm immediately assuming this is where it was sampled.
Not, not… So, yeah, no.
traffic itself, you know? Yeah.
Sven Cowart (ElastiFlow Inc) 00:12:00 This is not going to be a new attribute.
This is really old.
And, well, this issue. In the timeline of this SIG, this is really old, I should say, because it was created, In… yeah, earlier this year.
Rob Cowart 00:12:18 Yeah, yeah, yeah. Jan… oh, January. Yeah.
Sven Cowart (ElastiFlow Inc) 00:12:20 So, it's existed for a long time. This is just going to be network.direction now, because we already have that, and that's ingress, egress, so it'll be network.direction, ingress, egress, because that's what they mean by that in OB.
Oh, transmit and receive, sorry, not ingress, egress.
Rob Cowart 00:12:36 Yeah, I was gonna say, yeah. Yeah, exactly, yeah.
Antonio Martinez (Cisco Systems, Inc.) 00:12:41 It's perfect for me.
I think we can solve that, actually, that issue, in that sense.
Rob Cowart 00:12:46 But I think that makes this one a whole lot more straightforward, is what it sounds like.
Sven Cowart (ElastiFlow Inc) 00:12:50 Yep.
Rob Cowart 00:12:50 Like, this probably could be done still this year.
Sven Cowart (ElastiFlow Inc) 00:12:54 Yeah, yeah, yep. I already have most of the code, and I've been keeping it… like, once a month, I'll go rebase and keep it up to date, so I could get that in very shortly.
Antonio Martinez (Cisco Systems, Inc.) 00:13:07 So I think it's clear for everyone, and then that was the other one, and that one, the reason is because we didn't define yet the network.flow, right, on the spec?
Sven Cowart (ElastiFlow Inc) 00:13:17 There's just… there's a number of things, actually, here, but yes, that is one of those things.
there's the question around… I would just like to have a formalized flow semantic convention proposal, before we… Before I make all those changes, and then probably have to change them again.
Antonio Martinez (Cisco Systems, Inc.) 00:13:38 So, it's idea. Looking forward to see that thing.
Sven Cowart (ElastiFlow Inc) 00:13:40 Yeah, and… And I do have an update on this, And just a little bit of a… this is what I've been working on, so you guys understand why there's been some, why you haven't seen anything from me in a couple weeks. So… the entities… Well, first of all, just on a very human side.
You guys… well, those that were at KubeCon know that I was rushing to… like a madman to launch a new thing for, Elossa flow called SIGI, so I had no time left, and I needed a couple days to recharge. And then after that, now I've been focusing on the entities piece.
And… that… those things will actually inform some of how the flow semantic conventions should be influenced. For example, like, what is the resource a flow is reporting on?
I wanted to know… that I wanted to have an answer to that question before I create a flow of semantic convention proposal, and getting into the entity's work somewhat opened up Pandora's box for me a little bit, so I need to… I will have something in the next few days that… internally ready, and from that, I can make my best proposal for OpenTelemetry.
Rob Cowart 00:15:01 Yeah, we've actually both been working on that one a little bit, so…
Antonio Martinez (Cisco Systems, Inc.) 00:15:05 Or do you…
Sven Cowart (ElastiFlow Inc) 00:15:06 And then, Antonio, you'll get the, network interface Issue, and all those other things related to that, because it's all kind of in one bucket.
Antonio Martinez (Cisco Systems, Inc.) 00:15:14 That's interesting, because last week, you couldn't make it, but we were talking about creating a ticket for following the ROP initial proposal, and I have something for today, but it's using entities, and it's in a draft request, so all the feedback could go there, that you guys are working.
I will show you. Okay. I will show later on, but yeah.
Also, in the last meeting,
Sven Cowart (ElastiFlow Inc) 00:15:39 Is that pull… Is that the pull… is that the… is that link, is that the one for the pull request, or an issue?
Antonio Martinez (Cisco Systems, Inc.) 00:15:48 I have it both, actually. I will show, show it in a.
Sven Cowart (ElastiFlow Inc) 00:15:51 Oh, okay, sweet.
Antonio Martinez (Cisco Systems, Inc.) 00:15:52 And then, with regard to entities, we were chatting also the other day, and Lyudmila said with me, like, they… they are put… they have some standardization of our relationship.
Maybe they didn't cover all the ones that we have today available, but they have, like, part of rank on, so yeah. And I put the link here in the entity relation from the last meeting that was.
November 16th. Okay. For you to know, in case you want to jump there.
Sven Cowart (ElastiFlow Inc) 00:16:19 Does that actually… Have you dug into the spec? Like, how's the relationship actually communicated over?
Antonio Martinez (Cisco Systems, Inc.) 00:16:29 It's another fill on the model, so you can put how it depends on another entity.
What we were…
Braydon Kains (Google LLC) 00:16:41 signal, there's going to be an entity event. So, like, the two entities will be on a signal, and there will be an event that says this one with this identity is this relationship of this identity in, presumably backends. Recognize that and state.
Sven Cowart (ElastiFlow Inc) 00:16:55 I see.
Braydon Kains (Google LLC) 00:16:56 I think the idea, I don't think it's actually been implemented on the back-end side, so it's more theoretical right now, but… That's the idea.
Sven Cowart (ElastiFlow Inc) 00:17:03 You're saying… let me make sure I heard you right. You're saying that entity events will be used to emit Relationships for those entities.
Braydon Kains (Google LLC) 00:17:13 Yeah, I think it's going to be… so, like, OpenTelemetry events are… logs under the hood and interpreted as such, but with a specific name and specific fields that are, like, recognized as part of the SEMCOM spec.
And… Presumably, the idea is that backends are going to perceive entity events that's, like.
this… this Kates pod ID is part of this Kates replica set ID, and as long as the backend is tracking those entities all separately, it will be able to recognize those relationships over time, so that when you send a signal of a Kate's pod.
with the Kates Pod community, then it's part of it, yeah.
Sven Cowart (ElastiFlow Inc) 00:17:53 Okay, yeah, so then the relationships will not actually be modeled in, like, the resource attributes of a… Of a signal reporting something about that resource, so you're not gonna see that in, like, a trace.
Braydon Kains (Google LLC) 00:18:10 It's not a… it's not a… it's not part of the, like, trace requests payload. It's… there's a separate thing that manages the state of that, and then individual signals come with specific entities that the backend is supposed to maintain knowledge of.
Sven Cowart (ElastiFlow Inc) 00:18:26 Got it. That actually… that's a good direction.
that feels right, I'd have… I'm gonna figure out if that is right as I get through this entity's work.
Braydon Kains (Google LLC) 00:18:35 Yeah, it's… it was becoming… I think the concern was that it was going to be very, very heavy to always have to specify all entities in a relationship in, like, a proto-payload. Like, that would have been pretty excessive, so…
Sven Cowart (ElastiFlow Inc) 00:18:49 Yeah.
Braydon Kains (Google LLC) 00:18:49 Some of them.
Antonio Martinez (Cisco Systems, Inc.) 00:18:51 That's true.
Braydon Kains (Google LLC) 00:18:52 modeled in some way, or inspired by some of the way Google Cloud Monitoring designed this. Well, not… well, Monarch, the metric database.
Sven Cowart (ElastiFlow Inc) 00:19:02 Got it.
Braydon Kains (Google LLC) 00:19:02 It manages the relationships in a similar way.
Antonio Martinez (Cisco Systems, Inc.) 00:19:15 Okay, that's useful to know about it.
Anything else, Sven that you want to mention from your site?
Sven Cowart (ElastiFlow Inc) 00:19:22 No, that's… that's it, thank you.
Antonio Martinez (Cisco Systems, Inc.) 00:19:25 Okay, so a few things from my side. So, that was a comment from last meeting that we have. It's like, we have the proposal from Rob. That proposal is coming from the… interface MIPS.
we discussed it, we went through one study there, and there were some comments, so the idea is, like, I created a document to… to cover it, sorry, that GitHub issue to cover it, and also a couple of pull requests to solve it.
Something else also important to highlight, even the foundational data is coming from the SNMP FMIPS. We should… proposed metrics and attributes which are going to be aligned with whatever next network telemetry is out there, like OpenConfig or Gemini, for you to know. And then there is also, this is my proposal, but it's why I wanted to open the discussion here. Today, there is system.network and hardware.network. Let me actually open so you guys are… see what I'm talking about.
Mmm… here, hardware.
Mmm… Networking.
Here it is, yeah. So, today there is a, how do you call it? A semantic convention for Hardware.network. I think that's kind of the old, network group built together, and it's kind of… not use much, but there are some alignment with what I want to do, so… but the comment that we have, Braydon, if I recall correctly, is, like, we should Create a new namespace for network, right?
Braydon Kains (Google LLC) 00:21:07 Well, we do have… we… so we have a network namespace already.
Antonio Martinez (Cisco Systems, Inc.) 00:21:11 per… Correct.
Braydon Kains (Google LLC) 00:21:12 For hardware, network.
this is… like, the hardware namespace is so old and not up to the rest of the SEMCOM standard, it's just sort of been, like, left alone because no one wants to touch it.
I don't know what here in network I.O. and network packets is not Is not covered, and why it would need to be in a… Hardware namespace, specifically.
So, I don't have a good answer, but my instinct is that we should just cover this all in our existing namespace, because I don't think… I can't see why these need to be semantically different than everything else we have.
Antonio Martinez (Cisco Systems, Inc.) 00:21:54 So, in opinion. And if we go in that direction, what should we put here? Should we deprecate it, that one?
mark it as status deprecated, or… or that should not be us, the one doing it, I guess.
Braydon Kains (Google LLC) 00:22:05 Sugar.
Sven Cowart (ElastiFlow Inc) 00:22:07 I… so, when I… when I brought this up a few months ago, Lou Milla said that, yes, they would be open to deprecate this if we have recommendations on what replacement.
Four of them would look like.
Antonio Martinez (Cisco Systems, Inc.) 00:22:22 Okay, okay, so the step would be, like, create a replacement, agree on that, and then mark it as deprecated. The reason because it's not only the hardware one, but there is also system.network.
that… It's kind of a line, also.
I don't know why I jump in there, sorry.
If I go to system, you will find it quicker.
Braydon Kains (Google LLC) 00:22:46 So the system network ones are… I would also maybe be fine to replace those. I… for reference, we are planning to put them release candidates in, so we would need to make a choice relatively soon.
I can… the case for system network, which I don't know if it applies to hardware or not.
But for system network, it's… based, basically, directly on what ProcFS reports for network information.
Antonio Martinez (Cisco Systems, Inc.) 00:23:18 Is it? Okay.
Okay, here.
Braydon Kains (Google LLC) 00:23:20 And… I don't know if… We can apply all of that to… Stuff in just, like, normal network namespace that would work Both for, like, like, we, like, we could… Come up with, this is how, to take the ProcFS information and map it to the network namespace stuff?
Antonio Martinez (Cisco Systems, Inc.) 00:23:46 Correct. That would be my suggestion here. The saying that we are dropping the hardware, I would be in favor of dropping also the system network.
And then creating, like, the GitHub issue that I created was pretty straightforward. Here, I just defined the interfaces. They were… both of them as draft, because I was doing through today, but I will add the… if I go to models… Here, we already have the interface name, this is nothing new, but we'll have us defining the ROP document, alias, description, ID, index, MTU, and the type, and then it also describes, like, a… entity, and the entity will have as requirement, name, and ID. As I was saying, this is my proposal.
Once it is stable together with State what I mean, agreed among us, together with the other one, which is network I.O, network packets, the description wasn't updated, but drop it is part of the package, and then network interface queue size, those were the ones coming from… From there, from… from raw propulsion. And then network package is gonna have a… network package type that describes unicast, multicast, or broadcast, and also… let me show you the pull request.
Braydon Kains (Google LLC) 00:25:16 So…
Antonio Martinez (Cisco Systems, Inc.) 00:25:16 Racket's gonna have.
The request wasn't updated, but my comment here was, like, we're gonna have, like, an extra drop type, because there are different reasons why it could be dropped, like… unknown protocol and variety of the other ones, so that way, if we focus now on having the namespace network for those, I don't think system plus hardware are really needed. But this is my… from my opinion, that's why we are here.
Sven Cowart (ElastiFlow Inc) 00:25:45 I… Braydon, I have an idea. Maybe this works.
the way I see this is that these are the metrics, and you could have… and maybe this is what breaks down when we get into the entity modeling, But, really, what we're talking about here is… Those metrics can either describe a network interface resource, Or a system resource.
Braydon Kains (Google LLC) 00:26:12 Yeah, that's… that's essentially the only difference now… the only important difference now between what you just showed and what's in System Network is that System Network is meant to be reported against… So it's reported against a host with that stuff, with the network interface details as attributes.
Versus this one, which would be network… reported against network interface resource attributes, and… I guess, somehow, either we go the… like, it's the full 9 yards, and the interface is actually associated to the host in the back end, so we only have to report the interface, or we report the host and interface attributes as resource attributes all at once.
But the problem is, if you're reporting Against a host.
Then, the different… They… So that, that's kind of… In the pre… in the pre-proper entity world, it would be kind of shitty, because every… If you're scraping for multiple interfaces on one system with the host metrics receiver.
Right now, the way it works is it's all under one resource payload, and you detect the host at the top.
And then the interface details are, like.
attributes, dimensions on the metric itself, and so you can have time series for all the different interfaces in In one host resource payload.
But now what you'd have to do to be able to associate The network… metrics to specific interfaces, you need to report a separate A separate resource payload for each network interface.
Antonio Martinez (Cisco Systems, Inc.) 00:28:01 I think that's the direction where we want to go, right?
Sven Cowart (ElastiFlow Inc) 00:28:07 I… I think we want to do… Well… Describing the ideal end state, what we'd want is metrics about individual interfaces?
And… Metrics about a specific host.
and their network data, like, let's take packets. I might ask the question, what is the packet How many packets have dropped on this host total?
And then I want to also be able to say how many packets have dropped By each interface that might be on this host.
what do we… is… does that make sense, Braydon? Or…
Braydon Kains (Google LLC) 00:28:54 I'm… I'm trying to… I'm trying to think of this… In terms of, like, how it would practically get used if we… If we did it the current way, like, without proper entity relations and entity events.
The way it would have to work would be… each… system.network, or, sorry, we would have, like, for each interface, we'd have a network.packets.dropped, but then the resource for each one would have to be the interface name, and the same host ID.
And so you'd have 5… different… resources.
in…
Rob Cowart 00:29:36 Can I ask just a question to help me out here on the… because I'll admit, I'm slightly confused at the moment, but I'm also trying to think about real world.
Are you literally saying, Braydon, that typically you would be reporting today as this system thing exists? You would be reporting the network… metrics, in a payload, With all of the other metrics for system.
Braydon Kains (Google LLC) 00:30:07 It would be… So, if we're talking about specifically the collector implementation of host metrics, each scraper for each category, Makes one resource payload.
And then the expectation is that you shove the host resource detection on it after.
So right now, if you use the network scraper.
It scrapes information for all interfaces.
For each of those networks, so if we take Packets dropped is just one example.
It would be packets dropped with attributes for every interface that it… That it grabbed in that scrape.
And the expectation is that the next step in the pipeline would be the host resource detection that would put the host attributes in the resource. So then, in the end, you have a host resource.
And, like, 5 different, like, if you have 5 interfaces or something, a bunch of different sys… like, system network packet dropped.
With the dimensions of the attribute being, like, what interface it's for.
Rob Cowart 00:31:15 Okay, this might sound like I'm grossly exaggerating, but trust me, I am not.
What if that system has… 800 interfaces.
Braydon Kains (Google LLC) 00:31:28 then you would report… you can tell it not to only collect specific interfaces. There is a filter for that.
Rob Cowart 00:31:36 Yeah, I'm a service provider, and at the end of every one of.
Braydon Kains (Google LLC) 00:31:38 But you need, but you need all of them.
Rob Cowart 00:31:40 And I need them all.
Braydon Kains (Google LLC) 00:31:42 Then, you would collect However many, like, you… it would be… it would be up to you if you… if you need to collect that many, but you can't support a payload big enough to produce it.
Rob Cowart 00:31:55 Okay, that… because that's kind of what I was getting at, is that… It seems to me there it… there are definitely very many real-world environments. Not every network device, right? But, like.
Most likely, every environment will have a handful of devices that definitely Would result in a huge payload if you're trying to send all the interfaces.
Braydon Kains (Google LLC) 00:32:20 The collector can also split that up, so it's not like they would be guaranteed to all be in one big… Like, for example.
Google Cloud can't take more than 200 data points in a single request. So, if you had 800 interfaces and you're just collecting network dropped.
You would set up the batching, and it would split up into like… Five different requests of the same… the same host resource, but with different data points under it, and send them as 5 different requests. So, like, it would get chunked up.
Rob Cowart 00:32:51 So, so, let's just say we chunk that up.
Like, we send the interface stuff separately, and we chunk that up into, say, 100 payloads.
But then, each payload would have to go through that process of, Of, like, the whole host, identity part there, with…
Braydon Kains (Google LLC) 00:33:14 Yes, so I… at the very least, the resource detection processor.
Rob Cowart 00:33:19 What a minute.
Braydon Kains (Google LLC) 00:33:19 doesn't do it every single time. Like, it… it… at startup, it detects the host resource.
And then charitably assumes that nothing changes and just adds…
Rob Cowart 00:33:31 I mean, that's actually good, yeah. Alright, that was more the concern I was trying to get to, so… but if it has some mechanism that we're not… Overwhelming the host resource detection part, yeah.
Braydon Kains (Google LLC) 00:33:45 Yeah, it's still, like, if you're collecting information for that many interfaces, like.
you know, your collector process is still doing lots of allocations and lots of extra CPU work, because it's processing so many data points.
At once, but…
Rob Cowart 00:34:00 Oh, yeah, we… we… for sure, yeah.
Braydon Kains (Google LLC) 00:34:03 Yep.
Rob Cowart 00:34:04 I mean, that's why generally I would always… my intuition would always be, and I think the way most solutions Have historically done it would be… Breaking that up into almost per-interface payloads.
Braydon Kains (Google LLC) 00:34:20 Yeah, which you could… you could… kind of do? It would be kind of difficult in the collector to do it quite that way, but you can definitely chunk it up by data point, and there is support for partitioning. It's very new in the collector, but you can partition based on an attribute. So what… so if you wanted to, you could say, like, make batches of up to 200 data points and partition on the network interface name.
And then that would make it so that interface names go in individual payloads in the collector.
They all get batched separately, and apply their own batching rules separately, so you have to make sure you're, like, flush time out of the batches, and your batch sizing is appropriate for what you want per interface, but it is capable of doing that.
Rob Cowart 00:35:07 Okay, I only bring it up because I, you know, just because of the pure volume of it, and I don't know if there are… other such things in a typical system that could have such high numbers. I mean, I guess you could have, like, you know, a massive storage array with, you know, a couple hundred disk or more in it or something, too, so…
Braydon Kains (Google LLC) 00:35:28 The… the best example is processes, by default, the process scraper.
Rob Cowart 00:35:33 Yeah, yeah.
Braydon Kains (Google LLC) 00:35:33 collects all that information per process, and produces, like, a separate host… sorry, a separate resource payload for every process it scrapes.
And that's by default, and it's… that is also very heavy.
Rob Cowart 00:35:47 Yeah, yeah, I could see that, yup.
also far more ephemeral, too, so… yeah.
Braydon Kains (Google LLC) 00:35:52 Yeah, and it's one of those things where we've talked about, like, oh, what if you could, like.
cache the PID and only get specific information, but, like, between scrapes, you can't guarantee that PID even represents the same process, let alone is still alive or not.
Rob Cowart 00:36:08 Bill.
Antonio Martinez (Cisco Systems, Inc.) 00:36:15 I think we…
Sven Cowart (ElastiFlow Inc) 00:36:15 This is completely unrelated to this SIG, but that is something that can be solved with eBPF, Braydon?
Braydon Kains (Google LLC) 00:36:25 Yeah, we've… we've talked about that sort of thing before.
I think if… if there were eBPF solutions that could Do the same thing and not have to, like, read all of slash proc every minute.
Certainly be better. I'm just… we're gonna maintain this one until EBPF is ready for prime time.
Sven Cowart (ElastiFlow Inc) 00:36:46 Yeah. Yeah, I wonder where OBI is on that.
This would be a good place for that to go.
Antonio Martinez (Cisco Systems, Inc.) 00:36:54 brother.
Sven Cowart (ElastiFlow Inc) 00:36:56 So back to, back on this. Am I understanding this right? The… the tension here is… It didn't drop.
Do we keep… A network, or system network.
These system network met… metrics that… Have a dimension of network interface.
When they're reported.
Or move to a… per… Network interface.
metric.
Braydon Kains (Google LLC) 00:37:34 That is essentially… it's essentially, is the interface the resource, or is it a dimension on the metric? That's… Essentially, the question to answer.
Sven Cowart (ElastiFlow Inc) 00:37:43 Yeah.
Braydon Kains (Google LLC) 00:37:44 which…
Antonio Martinez (Cisco Systems, Inc.) 00:37:45 Goof.
Braydon Kains (Google LLC) 00:37:46 I, like, I can work with either one.
I'm just thinking of, like, how we use these metrics at Google, we're… if we move to the other model, we're just gonna promote… we can just promote the network interface name back to a metric attribute, and that's fine. So, like, if… If it's just… if it's better to… For our conventions, to just stick to Reporting interface as the resource, and then We can properly define its relationship with host.
Then I think we… It's probably okay.
Sven Cowart (ElastiFlow Inc) 00:38:25 I will say, at this point, I don't know if I have a preference until we make it a little further on.
the entity model.
Because I… realistically, without knowing the host, knowing something about a network interface is irrelevant.
So I get it being like this, I just wonder if… the… Like, for some reason, my mind is going towards… Network interface, metric per network interface, and then a systems.network metrics that is an aggregation of all those things, but…
Braydon Kains (Google LLC) 00:39:12 Well, the one thing with just.
Sven Cowart (ElastiFlow Inc) 00:39:13 Feels weird, too.
Braydon Kains (Google LLC) 00:39:14 Doing it like this is… this may not matter when you get to most backends.
But right now, the idea is that under host, you can sum across all network interface names to get that information for your entire host, and that's… Right. Maybe harder to do if they're all separate resources, but… Once it's in a backend, I don't know how much that matters as much, but…
Antonio Martinez (Cisco Systems, Inc.) 00:39:42 I do have also a comment. Remember from the beginning, we said that those are going to be describing the SNMP use case. For the SNMP, correct me, guys, that you are more experienced on that side, we don't have access to the host ID, right?
Sven Cowart (ElastiFlow Inc) 00:39:57 Yep.
Antonio Martinez (Cisco Systems, Inc.) 00:39:59 Do we have, or we don't, sorry.
Sven Cowart (ElastiFlow Inc) 00:40:01 We… yes, we would have access to the host ID, yeah.
Antonio Martinez (Cisco Systems, Inc.) 00:40:04 Okay, okay.
Sven Cowart (ElastiFlow Inc) 00:40:04 Or whatever becomes the host ID, but yes, we know how to… We'd be able to tell what the host is.
Antonio Martinez (Cisco Systems, Inc.) 00:40:12 It will be some sort of the device where we are pulling the data, right?
Sven Cowart (ElastiFlow Inc) 00:40:15 Yep.
Antonio Martinez (Cisco Systems, Inc.) 00:40:16 Okay, clear enough. So, I have a common… I don't think makes sense to keep both because we are gonna… we're gonna have a network.whatever under the… the new network, namespace. So… Does it make sense, had that been done before, Braydon, that you are more experienced in the semantic commission, to move Because those metrics could be moved.
To the network one, with some small changes.
Is it something that we could do, or we should… we would need to still keep that for the… receiver that exists today and is well used, and then maybe start a new one for more focusing on other use cases, like network metadata, not only system, in that case.
Braydon Kains (Google LLC) 00:41:10 I know that the preference for SEMCOM maintainers is generally to deduplicate as much as possible, and… I think if… If the way that we report these metrics, is… Accurate enough for how you want to report them in just gen… in other network cases. Like, if we're defining metrics here and metrics under network that are semantically, basically identical.
Then it would make sense to just pick the network one.
but right now, the system network ones are very… Focused on just, like.
Well, I mean, slash proc really is what they're focused on. We adapt them for other… for other platforms, too, but they're… these are… it's… this is semantically just a mapping of what… when you slash proc slash net, like, it's… it's… Is that what the file's called? I forget, but anyways, it's basically exactly like that.
And so, if we were going to… change… What… how these metrics… work and look in the network namespace, and we had to, like, adapt some of the information we get from slash proc strangely to adapt, then I would think it's no longer worth it. But I feel like the stuff in slash proc slash net is pretty much Just a surface level… Like, same thing as… As any other scenario where you're trying to get this information.
Antonio Martinez (Cisco Systems, Inc.) 00:42:50 Clem feeling.
Rob Cowart 00:42:51 Are these already, stable, conventions here?
Braydon Kains (Google LLC) 00:42:57 air… They are not dissimilar from what's currently in host metrics?
they're going release candidate soon. The attributes… our release candidate, the metrics are not yet.
Rob Cowart 00:43:14 I mean, there is a side of me that says.
You know, an interface is something that Simply cannot exist outside of a system.
And so… there… There is some sense to me to it being nested under system.
There's some nuance to that, though, because I've, you know, like… And again, this comes back to the entity work.
So, I have two network interfaces. They're both putting traffic, you know, send and receive, and I'm getting metrics from them.
But both of those interfaces are part of a lag group, and the lag network interface Has metrics too, which is the sum of these other metrics below. So there's… there's this natural layering effect, or, you know, where you have, sub-interfaces on a lot of network gear, virtual interfaces, if you want to call it that, right? So that all… so there is this natural stacking of interfaces. In fact, there is a table called the if stack table that literally reveals what these interfaces are, and even a status that says.
like, linked down, and the reason is lower level is down. In other words, the thing that I'm built on top of is down, so I'm down too, you know?
And I don't know that the entity… if there's maybe a clear way to express any… that type of relationship, and the way that system is built up right now, or entities are built up, but… that aside for a second, I mean, network interfaces can't exist on their own. Like, they are always going to be part of a system, so I could understand them being under system. Having said that.
My quick review of the list.
I think is a subset of what it needs to be, and what it needs to be is the PR that, that we were talking about to kick this conversation off that Antonio put together. So, So, the reason I ask about its status is, like, can this be modified?
And then it maybe could make sense that it's under system for interfaces, you know?
Braydon Kains (Google LLC) 00:45:44 Yeah, the… The… so it's… it's a… it's… the attributes that we feel are lacking, right? Like, the information about the inter… the attributes about the interface that are… that is lacking here, right? That's what we're talking about.
Or is it the breadth of metrics.
Rob Cowart 00:46:04 So, like… If we… if… could you go back to that list, I'm sorry, Antonio, of the system ones?
So, so I'll just give you an example.
If we took packets dropped and packets, and packet count.
what we would say… like, there's more granularity there on most of the network world. It's like, what you have is… packets. There's unicast, there's multicast, there's broadcast.
Then you have… discards, errors.
and, unknown protocols, all of which are dropped. So, here we just have dropped.
Which, I would say, great, why? Like, because I maybe care that… about that, you know, that it matters a bit. Also, like, the raw packet count, but what types of packets? And so, we actually would just have… packet. And then another attribute that says, is this metric about drops? Is this… or, you know, discards? Is this about, yeah, there you go, drop reason, etc, right? So, so there's some additional nuance that I would think we'd want to put in there. I don't think there's anything that's currently there where I would go, like.
oh, that's… that shouldn't be there, but I feel like, like I said before, it's a subset, it needs to be enriched a little bit.
And then maybe it could just stay under system. That would be my… And again, stay under system because it's always… it's still under network, under system, but because an interface Never… like, an interface can't exist without a system, you know?
So I can see where that makes part. I just feel like it probably needs to be… Further enhanced what's been suggested there.
Antonio Martinez (Cisco Systems, Inc.) 00:48:05 That's your point, Rob, but if we go in that direction, what happens once Sven is proposing the BGP, or he's proposing the flow ones? Are they also gonna go under system.network.x? Because we're gonna break system.network.interface, and network.bep. I mean, both of them are network namespace, or citizens, so we kind of have… that's why I was proposing to have it, both of them, and using… starting with the network namespace.
Rob Cowart 00:48:33 Yeah, I see what you're saying. I mean, I… I really could go either way on interface, but if I was going to make a split, it would be… What could exist because, like, BGP is not… confined to a given system. It is, in fact.
by nature, spread across systems, so you could say the BGP itself is an entity that lives above systems, so it can't be nested under system, right? It would have to be its own thing.
OSPF, all, like, most of the stuff would just be under network, with not some other top-level object above it.
Sven Cowart (ElastiFlow Inc) 00:49:14 Because…
Rob Cowart 00:49:15 they are concepts that aren't constrained to a given system, you know? That was kind of the way I would… if I was going to have stuff that was not only under network as the starting point.
It would be a question to me, does it exist entirely inside that thing containing it, or is it across… other things, you know? So, does that make sense?
I could go either way, quite frankly. Like I said, I'm not… I'm not… I'm just thinking if it's already in system, and it's already that far, and there is a logical argument that it could stay there.
then we should probably change what's already in system with the suggestions that were made for interface, from our side. And, But yeah, so… I guess I wasn't trying to say I recommend one or the other, I was… but I was trying to… share the point that I think you could go either way on it.
Braydon Kains (Google LLC) 00:50:18 The… the only thing I'll… I'll say is that the reason the system network attributes or metrics are, like, low in depth is because it's only based on, like, what the OS APIs give us. So, like, the… When we, when we, like, cat slash proc slash net slash dev, you know, we get.
we get dropped as just a number, and, like, that's all we get. And it's… with Windows, it's slightly more information, you get discards, but it's, like, the same, like… That's the reason that these metrics are so limited in comparison.
And so I don't… like, probably what could work is… The network namespace has… the extra information… so… Sorry, I'm trying to properly formulate my thought here. The network namespace has, like, the really good interface information. Like, the breadth of metrics, like what Antonio's PR had.
I think one thing that could work if this is allowed, we might need to ask SEMCOF maintainers if this is okay, temporarily, for us to say.
Can you have… A metric that is optionally reported against one entity or the other.
And then have an attribute that is, like.
You should include this attribute if you're reporting against the host interface… the host resource.
If… if that could work… Then we could… Keep the way that we recommend Implementing a lot of these, where, like, 4 network packet dropped.
Just to, like… because even if this metric isn't… technically useful, like, a lot of people are using this as semantically described here. The names are slightly different, but it's, like, just a raw Like, dropped number, like, from slash proc.
and we could keep that around.
If it was just network.packet.dropped, And we could optionally report that against the host.
And if you're reporting as the host, we recommend you turn on Network Interface Name.
then that… could work.
It just sounds kind of… complicated, like, we've… I don't know if we've had a scenario quite like this, where we say, against one Entity or another, and depending on that, you should report different attributes on the metric.
I don't know if that… Has quite existed before, but… In terms of, like.
Rob Cowart 00:53:00 I guess my confusion is, in this, to what you're saying there, is… I feel like you're taking the view of… of something that is accessing directly SSH, or whatever command line of the system.
But what if I have the exact same box.
It's just running NetSNMP agent that exposes the metrics, via SNMP, but it's all the same, like, like, it's still the system stuff. I can get disk stuff, I can get… I can get all this information.
also via SNMP, much of what I see in that system table, I can get by SNMP, right?
Shouldn't those two be the exact same set of attributes, you know, metrics and stuff?
Braydon Kains (Google LLC) 00:53:51 Wee… Yes, but there's also, like, if… let's say you were using something that could get way more information about the interface versus another thing.
That can only scrape slash proc.
That would be, like, that's a scenario that we still need to accurately support because of how widespread it is. We… there's lots of scenarios where people are, like.
Mounting host slash proc onto containers, and that's the only way they can get information about the host for that container.
So, I just want to make sure that whatever we do, the metrics still exist in a way Where we can accurately support the scenario where that's all we have.
I think that's all I'm trying to say.
Sven Cowart (ElastiFlow Inc) 00:54:35 can, and I think Braydon suggest… like, I'm sorry, Antonio's PR actually does that. I… Because you can still do represent packets.drop, it just wouldn't… the metric itself would not be called packets.dropped, it would just be packets with… An attribute or a dimension of what that means.
Braydon Kains (Google LLC) 00:54:58 Right, but we can… we could still say that it would still be the same thing, right? Yeah.
Rob Cowart 00:55:02 And…
Sven Cowart (ElastiFlow Inc) 00:55:03 But I… I'm actually with Rob on this, is… And I hadn't thought about it until this call. I thought, oh, everything SNMP-related is just going to land in the network namespace, the top-level parent namespace, but I actually think a lot of the SNMP work is going to… Should probably just land in system.
metrics.
Because, to Rob's point, you get all of the same information.
Rob Cowart 00:55:36 In fact, it looks like S&P gets more.
Sven Cowart (ElastiFlow Inc) 00:55:40 Yeah.
Rob Cowart 00:55:40 It actually makes me wonder, I've been sitting here as y'all are talking, poking around a little bit in the file system, because, you know, it's not like the NetSNMP agent makes the data up on its own. It's pulling it from somewhere, too. It just might be getting it from certain other places and drivers and stuff that the prox file system is not.
You know.
Braydon Kains (Google LLC) 00:56:02 Yeah, ProcFS is only getting what the kernel counters can manage.
So, like, if… an individual device had drivers that you could make, like, a CAPI call to to get more information that isn't exposed, like.
to the general device interface that the kernel uses, then, like, presumably you could get more information than what PROCFS gives you.
Rob Cowart 00:56:26 I have a suspicion the kernel gives more information, but just, it's not… expose the proc interface.
Braydon Kains (Google LLC) 00:56:34 Yeah, that's also possible, yeah.
There probably are syscalls to get more information.
Rob Cowart 00:56:38 Yeah, exactly, yeah, that's the moment.
Antonio Martinez (Cisco Systems, Inc.) 00:56:47 Okay, Edmund, but as my point before, if we… EU system.
what happened with the rest of the method that we envisioned to add, also? Are they also going to drop under the system, or are we gonna do it depending on if it is under pulling data from a host, it's gonna go under the system, or if it is gonna be more representing the network? For example, the one about the session that I did on KubeCon, it was something like network.path.hop. It's gonna be on their system, because in my opinion, it doesn't make much sense, but… The point that I'm trying to see here is, like, I see the use case of getting the data from the system here, or even SNMP at the end of the day is a system, but we are always going to have a split on network metrics. No network namespace, I mean, network metrics, where people are going to look for them, or people are going to use them? I don't know.
We don't have to take it near or another decision.
Rob Cowart 00:57:58 I'm willing to do the following, which is, investigate a bit. Oh, there it is. I was sitting there looking. We kept talking about prox. It is not prox. It's sys class net, and then interface name.
That's where it's all at. I was sitting there going, like, this can't be, I know I found this stuff before.
Braydon Kains (Google LLC) 00:58:21 Yeah, the… so the system.network.packet dropped metric that we were looking at, that is coming from ProcNetDev, but if you go to sys class, like, the actual device, you can get more information.
For individual devices.
Rob Cowart 00:58:35 Okay.
So… what… what I am willing to do is spend a little bit of time Looking at, these… Whether it's sys class or proc or whatever, what those metrics exactly are.
And then… How that maps to what Antonio's written up.
At least so we have the other alternative to look at, which is, hey, you know, one, network can just stay on its own thing.
And there'll be some… relation, but not directly using the same metrics in both, in both places? Or… we… try to get another update to System.network with the… with the work from Antonio there, and we can explain how you're not actually losing anything by doing that.
like, in this scenario, you'd populate it this way, and in this scenario, here's where those same values come from, you know? Like, so that we show compatibility there. Or, I go through that, and I realize there is no compatibility, and then what definitely needs to be separate.
But I'm willing to do that if that makes sense, so…
Antonio Martinez (Cisco Systems, Inc.) 00:59:59 Yeah, I don't think we have to take the decision now. As I said, I'm gonna… also going through the pull request a little bit more, and once I have it ready, I will let you know, guys, to take a look.
In the Slack channel, so we can continue the conversation from there. I think it's easier also to keep it track.
Okay.
Sven Cowart (ElastiFlow Inc) 01:00:16 Antonio.
Rob Cowart 01:00:19 I'm sorry, go ahead, Sven.
Sven Cowart (ElastiFlow Inc) 01:00:21 To your hot point, I actually don't agree with you there, I don't think it would be a system.
Antonio Martinez (Cisco Systems, Inc.) 01:00:26 Correct, it won't.
Sven Cowart (ElastiFlow Inc) 01:00:27 It… because it's more like BGP or Flow, where you're talking about a thing that is the connection, or the thing in between systems that you're observing.
Antonio Martinez (Cisco Systems, Inc.) 01:00:36 Correct, and that's why I have the strong opinion that we should not divide network.
telemetry between system.network on network.
That's my feeling, like, if you find a user… Oh, I agree.
Sven Cowart (ElastiFlow Inc) 01:00:49 I totally agree. I just… convinced that Interfaces are not… interfaces themselves are about a system and not the connection between systems. And that's why I'm willing to, like, go that direction.
But for me, I just… we need to model this, like, actually model the entity relationships to understand where this is going. And until we do that, it's gonna be hard to make a good recommendation.
Rob Cowart 01:01:19 Whoever's sharing, can you quit sharing real quick, so I can share?
Antonio Martinez (Cisco Systems, Inc.) 01:01:23 shareholders.
Rob Cowart 01:01:23 Now we're at time, I just want to show one thing for 30 seconds.
Oh, there we are.
so… Here is, like, one of the interfaces on this Linux box.
And these are the different stats you have.
So, like, the multicast when we were talking about packets, Is there… Now some of these, like CRC, carrier errors, they're actually going to be expressed in a different MIB called the ether-like MIB, and by the way, we probably need to take some of that into consideration when we're defining a subset of things, like, there's… because there are different technology-specific attributes that could come as well, and this is an Ethernet interface, so it's there. But, like, when I see the multicast one here.
And so, my argument would be, it's there, the system folks just ignored it.
So, and that's what I'm saying, like, this is the same data, it's just coming from a different place, and I just think we need to map it, and my intuition already is going to be that taking the current metrics that… that have been defined in Antonio's PR and expanding them into the system is probably right, and then there's probably another part of it, which is… Change the code that's using other methods, like, that's using the file system method to get the metrics, and just expanding that to get all of the metrics.
All right, I, I, I will… yeah.
Antonio Martinez (Cisco Systems, Inc.) 01:03:10 It's for first thought, honestly, yeah. Let's… let's think about it. Let's… Also, I would encourage everyone to… to put a list of project that we want to modulate as part of network, because if majority of a huge percentage are more fully under system or interface, oh, there we have the answer. But it's gonna be, like.
a huge presentation is gonna be more general, that, system thing, which I assume I still have a strong opinion there. But yeah, there is also a quick thing that I want to bring today before we end up. I was talking with John Asley, I don't know if you remember him from Cisco. He was here last week also at QFCOM. He mentioned that he's gonna ask someone from Cloud Native to get the Oracle credit, so we can start modeling some virtual network for start gathering metric generation. That's mainly with regard to the SNMP receiver, so we can test it on how we can modulate them.
he asked me if we can get a list of users by email that need access to the… to those places, so I put here my… my email. Feel free to add your email there, or send me through Slack, or WebEx, or whatever, and I will pass him. So we… We can have access not only in me. Yep, that could be great. For the rest, I will go through in the next one… in the next meeting. It's not a priority.
Alec 01:04:33 Antonio, any reason we're not doing the, DevNet always on sandboxes?
Antonio Martinez (Cisco Systems, Inc.) 01:04:38 Could you repeat, Alec, the proportion?
Alec 01:04:41 Yeah, yeah. Is there any reason we're not using the DevNet always-on sandboxes?
And just work ourselves around the credits.
Antonio Martinez (Cisco Systems, Inc.) 01:04:50 This is a DevNet a fiscal thing, right, only?
Alec 01:04:54 Yeah, yeah.
Antonio Martinez (Cisco Systems, Inc.) 01:04:55 Nope.
Alec 01:04:55 That's.
Antonio Martinez (Cisco Systems, Inc.) 01:04:55 Can people… can people from outside also access? That's the question here. I mean, outside.
Alec 01:04:59 Assuming they can make an email, which I think you can easily, yes.
You don't have to be a customer, is what I'm saying, so you can… anybody can join, but you would need to have a Cisco account.
Antonio Martinez (Cisco Systems, Inc.) 01:05:13 Cisco account, okay. I could prefer, honestly, that Oracle thing is coming from… I mean, they donated some credit to Cloud Native, so if John can get it, I could say it's… It's easier for everyone, so we don't need to… force anyone to create, like, a Cisco account.
Alec 01:05:31 Yeah.
I agree.
Antonio Martinez (Cisco Systems, Inc.) 01:05:33 But if we are having trouble with that, we can use that. And also, for the people that was not in KifCon, Sven proposed that they have, like, some sort of a real lab, not a virtual one, so we can also… Half use cases from… from a hardware lab, actually.
Yeah, those kind of things, like temperature, that we can test it out there.
Alec 01:05:56 Oh, I gotcha. Who's got, Rackspace for us?
Antonio Martinez (Cisco Systems, Inc.) 01:06:01 Sven from SIG. You mentioned that we can, we can use for some testing.
Sven Cowart (ElastiFlow Inc) 01:06:07 We don't have rack space, but we have… Rob's lab that runs in that room, er, I think the room next to them, actually, but… Yeah, that's pretty robust and has real devices. But that's the… that's what I'm afraid of with these Oracle credits, like, is it just gonna be virtual stuff? Because that's not gonna really give us what we need.
Alec 01:06:25 Yeah, yeah, yeah.
It's the same thing the sandbox I was suggesting. They're just, like, containers running somewhere within Cisco, so…
Braydon Kains (Google LLC) 01:06:33 I think Josh's idea around that was that there is still benefit to having, like, hermetic, reproducible virtual environments for some cases, and that's why we wanted the OCI credits. It wasn't to say we could cover everything with it, but that the existence of those was helpful.
Rob Cowart 01:06:50 Sven to be fair, Sven, we actually do have a little bit of rack space in Boston.
Sven Cowart (ElastiFlow Inc) 01:06:55 Oh, true, yeah.
Alec 01:06:59 We got Repo Depot, we can get, cheap gear.
It's the rack space that's the problem, the power.
Rob Cowart 01:07:07 Yeah, I mean, if someone has equipment they want, and we want to build some and, you know, create… because we could make some access to certain people to create some certain environments, so, you know.
We won't have to solve that here, but, you know.
Alec 01:07:22 No, I don't know. It involves dumpster diving, too. I gotta go find free stuff. You know?
Rob Cowart 01:07:30 Sometimes, we're working on some stuff right now that I, like, I literally pulled out every old piece of gear I could get… I could find that hadn't been turned on for, like, 4 or 5 years, just to be like, I know this one has this weird thing it does. So, but it's good to have, sometimes, the, you know.
Something that's not happy path engineering, you know?
Alec 01:07:53 Yeah.
Antonio Martinez (Cisco Systems, Inc.) 01:07:59 Okay, so my proposal would be, like, let's start, see if John can provide us some Oracle, credits, let's see if we can put there some virtual network lab And if we see that we have a lack of hardware, real hardware, we can explore other options.
Or if it doesn't work, we can explore the one that Alex mentioned about the DevNet in Cisco.
And yeah, let's… we can go from there, I guess.
Sven Cowart (ElastiFlow Inc) 01:08:26 Awesome.
Antonio Martinez (Cisco Systems, Inc.) 01:08:29 Okay, unless there is any other comment, the rest I will go through next week, if you guys are okay. I will… once I have more stable those requests, I will let you know, so we can open that conversation in Slack altogether.
Sven Cowart (ElastiFlow Inc) 01:08:43 Sounds good. Thank you.
Antonio Martinez (Cisco Systems, Inc.) 01:08:44 After the rest of the week, Stephen.
Alec 01:08:46 Cool, we'll see.
Giuseppe Ognibene (Coralogix) 01:08:47 Right.
