SIG: Semantic Convention SIG
Date: 2026-06-01
Duration: 53 minutes
============================================================

## Zoom Recording Transcript

**Christophe Kamphaus** 00:17 Hello?
**Sylvain Juge (Elastic)** 00:20 Alone.
**Trask Stalnaker** 01:46 Good morning, folks.
Give another minute.
See if we get any more people showing up.
Cool. Well… Small group today, not a problem. Let's see what kind of discussions we can have.
Antonio, hey.
**Antonio Jimenez** 03:17 Daniel, how are you doing?
So, I'm interested… I'm interested in adding… proposing some network attributes into the existing one. Those are things that we needed on fiscal Thursdays.
So we are today using the ones… Available, like in network, peer address, port, all of those.
But we would like to suggest some of them. There is already some comments on the request, which means that there are some traction on them, but it could be great that we… if we could Help on the triage.
So the… I'm gonna put it here in the chat. They could fall under the… the network attribute existing one, so let me put it also in the doc, in the world doc.
So, yeah. Today, those network attributes already exist, so it would be extending.
Honestly, it's not adding, like, new logic.
**Trask Stalnaker** 04:28 They're all peer… network peer… What is, have you happened to look at Elastic Common Schema?
To see what… if they have something similar there.
**Antonio Jimenez** 04:44 Andy there.
And then look.
**Trask Stalnaker** 04:47 from, okay, not really for vendor. There… it's a, we… Have been… we kind of… We're… It's an existing standard, that we have, Tried to align, you know, bring in Our goal is to merge the… Long term.
So it'd be… I'm just kind of curious to see… They have… got… because they have a… they… I think they have a lot more of these network…
**Christophe Kamphaus** 05:38 They also have a page, ECS and OpenTelemetry, and I think there, they make some mapping between the ECS and OpenTelemetry schemas.
For some properties, it matches one-to-one, but some have conflicts.
**Trask Stalnaker** 06:00 So, like, let's take DNS. I feel like… is there a… okay, so they have DNS fields… So what is… so I think in our network peer address is an IP address, I think, in OpenTelemetry, if I recall.
**Antonio Jimenez** 06:31 That's right, yeah.
**Trask Stalnaker** 06:33 Okay, and so, like, what… how would you capture DNS name here, or…
**Antonio Jimenez** 06:41 Yeah, so we are using, as you… if you keep reading the title, we are using the reverse DNS, so we are able to get from the IP, the actual host name.
However, any DNS will look… will work differently, so from the host name, or from the URL, you will get the IP. So here's the reverse DNS. And if you go a little bit down into the comments, there was a great comment from, Another mate, who is suggesting to, instead of falling.
DNS. I don't even recall now what they put. They are suggesting host name directly here. This is the one. Network here hostname, because that will be generic, regardless if you are getting it from a… reverse DNS, or if you are getting it from any other approach.
**Trask Stalnaker** 07:31 Hmm.
**Antonio Jimenez** 07:32 And then the host name provider, I don't think it's super… critical now. I mean, we can add it in the future, in case we have several, and that can be confusing for users, but I think for now, with the hostname, it might be more than enough.
So I added a comment at the end saying that I support that.
**Trask Stalnaker** 07:54 How does this relate to, server.address.
**Antonio Jimenez** 08:02 Correct, so server.address is more… the way how we see a list is more for… HTTP… protocol, or, I mean, any other communication protocol. This is, like, more, like, network layer, I could call it. I can see in the description of the server.address that says something like, use hostname.
or IP, if you don't have hostnames, so I know that, and we are using it for other HTTP, communication, but here I think we are in more, like, a low level.
I don't know.
If that makes sense.
**Trask Stalnaker** 08:43 And, where do you capture this? Is this something that you're… like, translating on the back end. I'm just, normally we recommend against doing, reverse DNS lookups, in instrumentation, just because of performance.
**Antonio Jimenez** 09:02 Correct, absolutely. So this is a different use case from the typical of instrumenting microservice. So what we are doing in cost analysis, like, we are monitoring an application.
And by monitoring that application, we are also traversing the whole network using a traceroute.
And then what we are obtaining out of there is all the hubs. Its hubs is gonna have, like, a… IP, a port.
And then, thoughts on us, in order to provide extra information, we are also doing our reverse DNS.
Now we are on the exporting of that telemetry data over OpenTelemetry to our customer.
We consider that the host name that we are obtaining is quite useful for the customer, so we don't want to miss it sending it over.
**Trask Stalnaker** 09:51 And let's see, the other two, correct. What is the address prefix?
**Antonio Jimenez** 09:58 And this is quite aligned with the other, so prefix is nothing else that you have the, the subset, so in mind that you have an IP, but you want to have also the prefix address, so it's giving you the range of IPs that it's, have, in common.
It's also follow RFC, so it's not something disco preparatory.
And this is also quite useful for our customer. The reason is because cardinality gets bigger and bigger when you have a lot of IPs involved, so if you're using the prefix, it's easier to search by ranges of IPs.
**Trask Stalnaker** 10:45 I see… Is that Nora's kind of standard terminology prefix for this? What this is?
**Antonio Jimenez** 10:55 Yep, following the… the FC, yeah.
**Trask Stalnaker** 10:59 Oh, you said this, RFC.
**Antonio Jimenez** 11:02 RFC, sorry, yeah, I know.
**Trask Stalnaker** 11:16 And then as name… Autonomous system name.
**Antonio Jimenez** 11:29 Correct. This is also a little bit low level in networking, but it's quite useful for debugging problems, because that's, honestly, the way how I understand it.
It's… Provide to you which is the owner of an IP.
So, you have big net… network groups at the end, like Google, AWS. It's not cloud, it's, like, big companies have, like, those networks.
So at the end, they are the owners of those IPs, so it's a way to know who is routing through.
**Trask Stalnaker** 12:04 Oh, that's cool. I didn't realize that was, I mean, it makes sense. So there's just, like, a lookup Table somewhere on the internet for these…
**Antonio Jimenez** 12:14 Surely, yeah, that's exactly like that.
Correct. So it's a big, big database with all that information, is there?
And this is also quite useful for at least in physical functionalized customers using mainly for BEP routing protocols.
Because when you are deciding which path you traverse, you are deciding which network you are using, and when The network change, you might go through more hops, which means that you're… its TTP request is gonna take longer, because it's traversing more hops during the network path.
So they are for debugging purposes, which… A S… I mean, autonomous system, are you traversing is quite important.
**Trask Stalnaker** 13:05 Anyone on the call have thoughts?
I know… I mean, just kind of… There's… these things… Don't… Tend to move… Very quickly, like, there's a lot of, you know, kind of… future… requests, I'm not sure what it would, sort of.
Trying to think what it would take to… If you can move it forward.
**Liudmila Molkova** 13:44 Hi, and Daniel, I'm curious, are you planning to define any signals, windows?
Good to see you, babe.
**Antonio Jimenez** 13:54 Would you repeat the question? Sorry, if I am planning to…
**Liudmila Molkova** 13:58 Do you plan to define any signals that would use them? Would you define any metrics, or blogs?
**Antonio Jimenez** 14:06 Yep, so, this is still ongoing.
proposal, but our goal, like, if I search for a sec on my screen, if it is possible… Yeah.
**Trask Stalnaker** 14:18 Let me stop.
**Antonio Jimenez** 14:24 So, 1,000 eyes have… let me see, because I have many room resulting, sorry for that.
Susan has half the… So, tosonize has that network path visualization that is, as I was mentioning, is traversing the whole internet and saying, okay, from that synthetic tokenized agent.
like, let's say London is a synthetic socialized agent, and you… in that case, you go to another agent, but it could go to any endpoint. We are traversing all those networks. So what I am working internally is, like, we are going to switch our mind, and instead of thinking about ops.
sorry, microservices, we're going to start thinking about IPs hubs, so at the end of the day, it's hops to hubs, it's the same as microservices to microservices.
So the signal that we are planning to use here is Apptrace, and then we're gonna have, like, a delay between two hubs. We're gonna have also which protocol are we using, which is already an attribute defined, which is, I think, network connection, network protocol, yeah, network protocol. So, there are already many attributes that we are reducing, but there are some missing, so I would like to start proposing them before we make that public to our customer.
Let me see if I have the glass.
I'm gonna stop stressing, sir.
**Trask Stalnaker** 16:08 Milo is kind of asking, like, are… So, what are you recording these on? I'm assuming events?
Versus compared to spans or metric. You mentioned cardinality, so maybe metrics?
It wouldn't be…
**Antonio Jimenez** 16:25 It will be for… it will be for traces.
**Trask Stalnaker** 16:28 Oh, for traces, for spans.
**Antonio Jimenez** 16:30 Yep. Yeah, it will be, it will be on OpenTelemetry, trace.
With… instead of having microservices talking to microservices, you're gonna be ops talking to HOPs.
That's the end goal.
Here I have an example, I did a proof of concept, let me go through.
**Trask Stalnaker** 16:51 And you're creating, like, synthetic spans on the back end, then?
**Antonio Jimenez** 16:56 Correct, correct. So we are creating internally in our site.
Give me a second, I'm gonna show you an example of how it looks like.
So this is a proof of content, not yet customer-facing.
In that case, I'm just sending it to Splunk.
18 weeks.
So, as I was mentioning, we are… We have a list of hubs calling each other, and the way how we are represented is, like, a thousand agent.
which is the root in that case, it's calling that IP, and then that IP is sending a pro, which is, like, what you use for traceroute.
to the next one, and the next one, to the next one, and so on. And then the cool things, like, if you think for a second about a service map, it's better visualization than a waterfall, because we are not used to seeing that in waterfall.
But we can see perfectly in a transaction.
Let's see if we have some data.
Yeah, so we have our thoughts on SA calling on a hub, calling on another hub, and so traversing the whole network until you reach the destination.
And right now, we have many of those attributes. As I said, this is totally internal. That's what's even used in the old format, but now would be something like network peer address, network peer hostname. That is the one that I am proposing. We are using more internally, this is a proof of concept. And then other things that we are going to have is, like, the… which hub we are, but I'm not proposing that to the community, because this is quite specific for our use case, and which is the percentage of the network loss that we are having. So this is the kind of the use case that we are Orcino, and then in order to have, like, the… ASN number, the prefix, the host name, I think they are quite aligned with the… community, and with the network community, I think that they could be quite useful.
I don't know if that helps you.
**Liudmila Molkova** 19:15 Do you propagate context?
**Antonio Jimenez** 19:19 We don't provide context because we don't have access to those hubs. What we are doing is we are doing a translation, so we have all the information from our trace route, so the one that they were showing before, so we have all that information internally, then we are converting it into a standard, which is the OpenTelemity Trace, and then we are sending it through. But we don't have access to those hubs. Those are network hubs out there, so we cannot traverse… I mean, we only can traverse in that sense, but we cannot, do with eBPF or something like that, context preparation.
**Liudmila Molkova** 19:59 Yeah, I'm… the… where I'm leading to is that if we were to design it in Ottawa, we would probably design those as events.
And you would still be able to see the map.
But the trace view, like, representing those as traces.
Sounds like what we normally represent as traces is operations inside the application, right? And here, the spans are the things between, and it's… the context is artificial.
So, would it… hmm… Makes sense to have those as events instead.
**Antonio Jimenez** 20:41 what could be for you an event? Like, IPX is sending, prof to APY.
**Liudmila Molkova** 20:50 Yeah, kinda.
**Antonio Jimenez** 20:52 But that could be quite unrelated, because our goal is to have everything connected to each other, because we would like to know, like, here we are spending 1 millisecond, here we're spending 20 milliseconds, and so on. And that example is not perfect, in the sense, like, but we also can see that in, traversing a network, we have losses presented in some of them, so this is where all the picture looks perfect together.
As I was mentioning, if you think for a second, this is at the end.
of the day is the same, that microservices stored in microservices. I understand the part that is artificial, but it's not artificial because that connection was actually done. The only thing is, like, we cannot track from the root. We are tracking from the upper layer.
And then we are converting it into a… into a trace, but this is not artificial, I mean, that was actually happening, and we were measuring Let me see if I have…
**Trask Stalnaker** 21:51 Are they aggregate… are they, sorry, still catching up, but are they aggregated, or you're taking each request And then, based on the IP, you're just… you're… on the back end, you're… Determining what all the intermediate hops were.
**Antonio Jimenez** 22:11 For sure, they are aggregated, so when you run traceroute.comm, it's giving you all the IPs that you are traversing until you reach your destination. It's like… So if you just do… world.com… So it's giving you all the fields that it's traversing?
And this is what we are doing, but in, So those are the IPs that it's going from my computer to Google.
And this is what we.
**Trask Stalnaker** 22:47 Are you…
**Antonio Jimenez** 22:48 This is…
**Trask Stalnaker** 22:49 Are you kidding?
**Antonio Jimenez** 22:50 and numbered them.
**Trask Stalnaker** 22:52 Are you doing that on a per, like, for each HTTP request?
You're doing that, or you're kind of at… or, like, the span that you're looking at, that you're building, is that a span for a specific… Like, user request, or that's a… an aggregation, sort of, of…
**Antonio Jimenez** 23:17 You said… It's a synthetic test, so it's not a real user monitoring, it's a synthetic test. In that synthetic.
**Trask Stalnaker** 23:25 Oh, it's not rooted… I see, it's not even rooted into a user role.
**Antonio Jimenez** 23:31 That's right.
**Trask Stalnaker** 23:31 test the service.
**Antonio Jimenez** 23:32 So, so huh?
So here, the use case most common is, like, my application is working on Seattle, but the application is not working in Spain. Why? It is the same code base on the same Docker image, the same… so it might be a network. So now you reach your application from different places on different areas in the world, and then you discover, okay, from Seattle, there is only, I don't know, X number of hops, and all of them are taking a delay lower than 1 millisecond. And the one in Spain is having, I don't know, many hops.
or even losses package, or maybe the delay is quite big, and then there is a timeout. So this is what… Usually, Cisco Thousanda is trying… trying to solve.
Yeah, this is why we have those synthetic tests to proactively know if my application in Spain is not behaving properly in 2H1 network is.
**Liudmila Molkova** 24:24 And this is per… Each packet, or it's per this, synthetic PSOFs. Traffic.
**Antonio Jimenez** 24:33 Persected test, let's call it, yeah. That, round that they was shown is persected test, yeah.
So here you can find a… yeah, for example, here you can see a more realistic sample.
Here you can see, like, we are going from that agent to that endpoint, and then those are all the hubs that we are traversing.
True.
this is what ThousandS is doing, and what I'm trying to… I mean, our customers are asking about that information, and then I realized that the main way to do it is to send it as an up and limited trace.
as it kind of works already here, as you can see, but now in order to support a specific attribute that I can see that they are useful for the community, like the hostname that I was mentioning, like, network here, hostname.
I've seen that it could be a great tool.
Come… try to talk with the community to see if we can also align there.
Now, this is my boy.
**Liudmila Molkova** 25:36 Yeah, so I think… Guy.
We try to avoid defining attributes without also defining a signal that, uses this attribute, because then it's kind of hard to understand what attribute is for, and would it work or not.
The… then this is the first part. Then, the second part is, there… we try to have a few people, several people to work on, especially something… this complicated. Complicated in the sense that it's used… it can be used in multiple ways.
It seems to be pretty generic.
And we have a couple of other folks who were interested in something similar.
I think they work on EBPF, and I thought somebody was the flow proposal.
I, I can dig up, The context, I don't have it right now.
But, where… Ideally, we would want you folks to have a small group.
That would review this proposal, and work on this proposal, from different angles, and would be, like, happy with it being generic.
Enough.
I think there were… there was interest from… folks on this, and I think we should… Try to form this group if your folks have energy.
I'm thinking, and maybe Tras can, Christoph can, Darmin.
can share their thoughts. Do we need, like, a SIG, or do we have a virtual group?
That can meet in scope of this call.
I would be in favor of having a virtual group that shares the meeting space with this group, because it seems everybody who works on it is relatively new to semantic conventions, and it would be nice to have those discussions, in front of people who Oh, no, the drill, sorry.
**Christophe Kamphaus** 28:01 Yeah, I think networking is a pretty central part.
So, I think it makes sense to keep it in the semantic zig.
**Liudmila Molkova** 28:17 Awesome, then maybe the next step would be, Antonio, can… you created a bunch of… oh, thanks, Harman. You created a bunch of, pull requests, right? Or are those issues?
**Antonio Jimenez** 28:29 I only created Asus, really happy to work on the pull request, if you guys consider.
I created.
**Liudmila Molkova** 28:36 Three of them.
**Antonio Jimenez** 28:37 for them only. Like, to see the traction, I can see that they are the main ones, honestly, that the community could They were off.
**Liudmila Molkova** 28:46 Yeah, would you mind creating an issue to track Like, networking, extension and semantic conventions, like, create a networking group.
And I'll make sure… with some scenarios you would be interested in. Just keep it, like, brief, no need to go into the details. And I'll tag… People who were interested in something related.
And, I, I'm not sure if you know them. Do you know Mario? Mario Marcia?
**Antonio Jimenez** 29:21 Gotcha.
**Liudmila Molkova** 29:21 I'm trying to graph on it.
**Antonio Jimenez** 29:22 For sure, yeah. Yeah.
**Liudmila Molkova** 29:23 So, I don't know. Let's start the Slack chat, maybe in the Semantic Conventions channel.
And, you folks can… can decide what is the common And they can comment on the issue, they can share their scenarios, what they're interested in.
And we can.
**Antonio Jimenez** 29:43 Friends.
**Liudmila Molkova** 29:43 the, the intersection.
**Antonio Jimenez** 29:46 Okay, I think there is already a network semantic group, isn't it? Because I saw on the calendar that on Tuesdays, there is, like, that group happening, but during the last weeks, there were not any items on the agenda, so I said, let's go to the generic one better.
That was my version of it.
**Trask Stalnaker** 30:05 I think it's…
**Liudmila Molkova** 30:06 bad, right?
**Antonio Jimenez** 30:08 Yeah, could be that.
**Trask Stalnaker** 30:09 EB… that's not a semantic convention group, that's the network EBPF.
Which, yeah, is, I think, getting folded into the… general EVPF, hopefully.
**Braydon Kains (Google)** 30:30 I think a lot of network stuff has come to the system… system group recently, which is… there's… the… Mixed… mixed results, because… Some network metrics are very related to stuff we do, and some are very… Specific to networking and not… System-level networking, so… I think this… I'm sorry I joined late, but this is about the… the peer name one?
Because I don't think we would necessarily be the right group to… address that.
None of us are really… Networking experts, specifically.
So, we've had some other proposals from the eBPF networking group, which is now being folded, I guess.
To introduce a bunch of new stuff.
Related to… specific TCP protocol behaviors.
that also is something that, like, we haven't had time to address, time or expertise, realistically. And I've tried to socialize it internally with some people who do know networking stuff, but I don't think there's been movement on that.
We might need to… figure out what to do with network, or the network namespace, I think.
**Liudmila Molkova** 31:49 Do you have any interest in it?
**Braydon Kains (Google)** 31:54 interest, time, and expertise are all different… different things. I want to see the… I want to see the namespace improve.
But I don't do the level of deep networking stuff that the namespace requires, so I don't know how much help I can be on the definition. If I can help with maybe organizing a group of people who are interested, that's a way I could probably help.
**Liudmila Molkova** 32:19 That would be awesome.
**Braydon Kains (Google)** 32:26 I don't know how we're proposing new… new SIG groups in semantic conventions these days. I know there's, like, a general… push for the hotel project to accept more, like.
scoped projects than open-ended SIGs like this, but… I can try and… I can try and propose something.
**Liudmila Molkova** 32:49 I was hoping that we can discuss in the issue, which scenarios around networking We want to tackle. We have energy to tackle.
And, It… once we, have a list of scenarios and people who are interested in some of that.
It's the client be more clear.
If it's a small group focused on, you know, just the synthetic tests for a network, or it's something bigger.
**Braydon Kains (Google)** 33:28 Yeah, okay, it makes sense. So I, I know, I know there's the TCP proposal, and there's this peer proposal.
If anybody knows of any other network proposals that are in limbo, I can try and collect them.
**Liudmila Molkova** 33:43 Yeah, I'll comment on the issue, the things that I'll find. I think there is also a flow proposal, which is somewhat… might be somewhat similar.
If it's something, like, the normal process, we create a project in the community, but we need a maintainer, from semantic conventions to sponsor it.
I personally, Braden, if you sponsor it, I would be… happy. I don't know what other maintainers think.
**Braydon Kains (Google)** 34:13 I don't technically have a maintainer title, so whether that would work or not.
Is up in the air.
**Liudmila Molkova** 34:21 I would be happy to delegate to you.
**Braydon Kains (Google)** 34:24 Okay, sure.
**Trask Stalnaker** 34:26 I think the main question for me is whether we go through the community project proposal, or whether we just spin it up as a, kind of, a more, if you will, like, lightweight project within this SIG.
**Antonio Jimenez** 34:47 That might make sense, as it doesn't die again as the network one, the EPPF network one.
**Trask Stalnaker** 34:56 The key… either way, the key is getting the… getting people, identified and scope identified, as Ludmilla says, so I think… starting the issue in the SEMCOM repo.
Makes sense, as Lynn Miller.
Proposed, and then we can kind of see where it goes based on scope and people.
**Braydon Kains (Google)** 35:26 I think there's a… there's a lot of… activity right now, specifically with, like, eBPF collecting golden signals, so if we needed to scope it around something, targeting that would probably be… make sense.
**Trask Stalnaker** 35:44 Cool. That sounded like a good… Path forward, Antonio?
**Antonio Jimenez** 35:52 Okay, that sounds good. So we gather some people internation, and then we discuss the different attributes of possible.
Trace Signal for that use case.
I still do have a quick question. For the genetic attributes, They are not related with a signal, per se. Can we still add the one that they was proposing there, or we still want to have them be discussed on that new group?
**Trask Stalnaker** 36:28 So the… generic signal… Oh, you mean whether it's okay to capture it as a span?
**Antonio Jimenez** 36:38 Correct, I mean, because for my use case, it's gonna be on spam, but I consider them as generic, in the sense, like, it could be also used in metrics or events as they are I mean, the thing, honestly, it's the thing as an address, or as a port, it's as the prefix.
So… quite far, quite January, so… That's the same extent.
**Trask Stalnaker** 37:02 Yeah, I would have that dis… I mean, I think we should have that discussion with… in that group of people, and within this SIG.
I've seen… it reminded me of, In, the Java extensions, we have this, thing called inferred spans.
Which basically takes profile data and turns it into synthetic spans on, trace.
So, kind of this idea of synthetic spans?
doesn't… I mean, it… There's some prior art, There's no… I don't think there's any prior art, though, in the spec or semantic conventions.
So I think it's an interesting discussion topic, though. It's certainly… I can see the advantage for your visualization desire, similar with the kind of inferred spans. There's some advantages to creating synthetic spans sometimes.
**Antonio Jimenez** 38:16 Excellent. Clear for me, thank you.
**Liudmila Molkova** 38:21 Thank you.
**Trask Stalnaker** 38:25 Let's see, we lost Sylvain, goodmilla.
**Liudmila Molkova** 38:32 Oh, my God.
**Trask Stalnaker** 38:35 More network.
**Liudmila Molkova** 38:35 So… Yeah, so… Oh, right, again, network again. So this is a request from CJO. He's asking a great question. So, we have a couple of metrics for connections.
The HTTP client open connections and the HTTP client connection duration.
And these two friends have network peer address.
And it's, especially problematic for open connections, because it's an up-down counter.
And it accumulates… It keeps all the time series active with all the attributes that ever existed, so if your process has a long uptime, then you're just accumulating network peer addresses.
It's also a problem with, histograms, if somebody opts in into cumulative histograms.
Cumulative aggregation, so… And the proposal… What he has currently is to mark network peer address as opt-in on up-down counter.
And I'm thinking we should probably also mark this… it as opt-in on the… Connection duration histogram as well.
Just because… Even if it's not as easy to hit this condition.
On histograms, it's still much easier mental model that you opt in across the board.
**Trask Stalnaker** 40:22 Yeah, and it aligns with what we did in other ACDP metrics.
Like, we intentionally… don't capture network peer address because of cardinality concerns, I think.
**Liudmila Molkova** 40:36 Well, I think for connections, the… the address Is… more interesting.
**Trask Stalnaker** 40:42 Oh, we don't…
**Liudmila Molkova** 40:44 We don't capture it here at all.
the IP.
**Trask Stalnaker** 40:51 I see, for a connection, I see. Oh, no, we do have server address.
So, sorry, I didn't follow what you were saying.
**Liudmila Molkova** 41:01 So for the other HTTP metrics, not connection-related, we don't even capture the network PR address thing.
**Trask Stalnaker** 41:11 Right.
**Liudmila Molkova** 41:11 trade clients.
**Trask Stalnaker** 41:12 it's…
**Liudmila Molkova** 41:14 Huh.
**Trask Stalnaker** 41:15 That's what I was, saying. We don't capture it in.
anywhere.
It makes, I think… I mean, does… is there a reason… I mean, it's kind of implicitly opt-in.
**Liudmila Molkova** 41:30 Oh, I see.
**Trask Stalnaker** 41:33 Is there a difference with connection metrics, why it would be different from… normal… Like, duration metrics?
**Liudmila Molkova** 41:50 my mental model, the… Connections, having addressed, like, what you're connected to.
is part of the semantics, it's not just any random attribute that you can put. You can probably make the same argument for the request.
I…
**Trask Stalnaker** 42:14 Because you might end up with multiple… connections to different IPs for the same server address?
**Liudmila Molkova** 42:24 Right, and maybe you have two short connections with a specific one, specific IP, or specific failure… failures with the specific IP address.
Sorry, I think I interrupted somebody.
**Braydon Kains (Google)** 42:42 I was just gonna say that, like, I was… this is my first time… looking at this metric in depth, and I was kind of surprised that The network peer address.
was… on by default, because of that, because of, like, from one server address, if it's load balancing across a ton of servers. Like, this is very normal for, like, the Google APIs, for example.
You might get, like, 7 IPs when you DNS resolve.
like, a GRPC would get a bunch, and then… try all of them, and then decide, oh, this IP works. But, for example, if any of them work, and you're round-robining across all of them, then this… I know this is HTTP, not gRPC, I'm just giving an example. Like, presumably the… for one server address, you could have, like, 7 or 8 IPs, depending on how you implement the client.
So I would imagine that the cardinality would be a big problem if you keep the peer address on by default. So I support it going Opt in, personally.
**Liudmila Molkova** 43:40 Yeah, and 7 or 8 is not a problem, right? And if it grows unbounded, then it's a problem.
**Braydon Kains (Google)** 43:46 It's, yeah, it's just if it goes a long time, and you connect to different places, or something changes behind the load balancer, or…
**Liudmila Molkova** 43:55 And it's, it's a problem, like, normally you would have a fixed set during specific time range.
**Braydon Kains (Google)** 44:01 Yeah.
**Liudmila Molkova** 44:03 But then, if… yeah, if you… this time series stays active, then that's a problem.
But yeah, it seems to work.
**Trask Stalnaker** 44:12 Any… yeah, I don't think there's any, disagreement that… that should be… not recommended.
I think my only question is whether it should be aligned with Duration with the other ones where it's not present versus… or should we make it opt-in here?
in the others? Like, is there a difference between the request duration and… The connection duration, for example, that would be different, and… You kind of answered that, with the, like, connections… Been… more an ag… like, that you could have multiple connections for… I mean, but yeah, the same argument, I think, could be made for a request.
duration also.
But that's a pretty small… I mean, given that we implicitly say that it's opt-in if it's not present anyway.
**Liudmila Molkova** 45:24 We all always have this argument, On opt-in attributes, should they be… Even listed on any metrics, if all of them opt in.
And I read it as, okay, I'm an instrumentation implementing this metric. If I don't see an attribute mentioned, I probably don't bother.
And if I see it, then I can think, oh, do I want to expose this configuration property? And the code generation, let's say, if we do this, and we do it along with the config, it would take care of the ones mentioned explicitly.
And with this logic, we probably should add… Network peer address, too.
All of them, as of TIN.
But it can always be done later.
**Trask Stalnaker** 46:11 Yeah, I like that reasoning.
Makes sense.
Yeah, I'll give you another… I'll give it another green check, just… But yes, it's… experimental.
Makes sense.
**Liudmila Molkova** 46:27 You wanna hit merge?
**Trask Stalnaker** 46:29 Sure…
**Liudmila Molkova** 46:35 Nice.
I noticed something that we… We have a policy that checks that stable, let's say, metric or stable group cannot reference unstable attribute unless it's opt-in.
And I noticed that we managed to… make some… mark some metrics or entities as RC without marking all the attributes as RC.
And I want to extend the policy that we have.
To require attributes.
Reference than a signal to… Have as the same or higher stability.
And this pure does it. There is an exception I had to add for Oracle, the Oracle DB span is RC, but it references non-RC attributes, development attributes, I created a tracking issue for this one.
So the problem that existed, with some others was in the… somewhere in the process, and somebody else fixed it.
So it, it… Did not become an exception.
There should be a link somewhere in the… in the PR.
**Trask Stalnaker** 48:09 And this is… any… Signal… I thought that… yeah, that's interesting. I thought that for, like… bands, for example, I thought that we had experimental stuff.
**Liudmila Molkova** 48:25 If it's opt-in, then it's fine.
And we have an existing policy that checks for it.
**Trask Stalnaker** 48:32 I'm dating them.
**Liudmila Molkova** 48:33 Policy to, not apply not to stable, but to any other stability.
So everything on RRC should be RC stable, Or opt-in?
**Trask Stalnaker** 48:52 Okay, okay.
And so we were just missing, you said, the RC, like, Okay, any kind of lower stability?
**Liudmila Molkova** 49:04 Yep.
**Trask Stalnaker** 49:09 Nice.
development, experimental.
Do we still have a mix?
**Liudmila Molkova** 49:16 I still formally support a mix on… a schema. And once we switch to V2, it will completely go away.
**Trask Stalnaker** 49:27 Yeah.
**Liudmila Molkova** 49:30 Oh, I can remove experimental.
**Trask Stalnaker** 49:32 Stability tests… How do I read this test?
**Liudmila Molkova** 49:39 Let's compile it.
**Trask Stalnaker** 49:45 Best passage on the Lord.
**Liudmila Molkova** 49:47 Yeah, so this is a test.
Forever stability.
Right from the end.
We'll be around the… GS underscore input.
And, there should be no deny signals from… Any policies with this input?
**Trask Stalnaker** 50:21 Did, let's see, did we get our… Copilot, give it… yes, okay.
**Liudmila Molkova** 50:27 Johnson Machus, I think, if I remember correctly.
**Trask Stalnaker** 50:30 Sure. It's very good at Rigo.
Or relative to humans, at least.
Thank you, Christoph.
**Liudmila Molkova** 50:45 Yeah, thank you.
**Trask Stalnaker** 50:50 Crash event…
**Liudmila Molkova** 50:58 Not sure who added this.
**Trask Stalnaker** 51:01 Probably Jason, he was…
**Christophe Kamphaus** 51:02 I added it.
**Trask Stalnaker** 51:03 Okay.
**Christophe Kamphaus** 51:05 I think it's fine, it's just that, Mila, you reviewed it a few things at the end.
And I think they are all addressed.
**Liudmila Molkova** 51:17 Awesome, thanks. Sorry, I'll take another look today, promise.
**Trask Stalnaker** 51:31 Alright, I think we hit the end of our agenda.
Thank you, everyone.
for joining.
**Liudmila Molkova** 51:39 Thank you.
**Trask Stalnaker** 51:40 Till next time.
**Christophe Kamphaus** 51:41 Thank you.
**Armin (Dynatrace)** 51:42 Hey.
**Christophe Kamphaus** 51:42 Have a good week.
**Armin (Dynatrace)** 51:44 Me too.
**Antonio Jimenez** 51:44 Thank you, Owen, keep in touch.
