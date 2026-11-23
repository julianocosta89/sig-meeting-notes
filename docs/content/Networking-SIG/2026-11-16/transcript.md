SIG: Networking SIG
Date: 2026-11-16
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Josh Halley (Cisco Systems, Inc.)** 02:40 Hey, Antonio.
**Antonio Martinez (Cisco Systems, Inc.)** 02:44 Hey there, how are you doing?
Thank you for joining my buddy.
Thank you for hearing.
**Josh Halley (Cisco Systems, Inc.)** 02:51 I survived Chicago airport over Saturday, so… I was.
**Antonio Martinez (Cisco Systems, Inc.)** 02:55 One of the lucky.
**Josh Halley (Cisco Systems, Inc.)** 02:55 ones that got stranded out there for… for the evening, so…
**Antonio Martinez (Cisco Systems, Inc.)** 03:00 Lucky you indeed, lucky you. I know many people are still flying back.
**Josh Halley (Cisco Systems, Inc.)** 03:04 They're still stuck.
**Antonio Martinez (Cisco Systems, Inc.)** 03:07 Because delay of delay.
Bummer.
Let me clean the spring, and see if the other day.
**Giuseppe Ognibene (Coralogix)** 03:15 Maybe one.
**Antonio Martinez (Cisco Systems, Inc.)** 03:17 Yeah, you should be.
We'll meet you in Chief Co, man.
**Giuseppe Ognibene (Coralogix)** 03:20 Yeah, how's it going? How was the talk?
**Antonio Martinez (Cisco Systems, Inc.)** 03:24 There were many eBPF talks for you to know.
Quite fun. I enjoy it a lot.
Excellent, you'll have to be there.
**Giuseppe Ognibene (Coralogix)** 03:34 Next time, hopefully.
**Antonio Martinez (Cisco Systems, Inc.)** 03:37 Yeah.
I'm paying Spain.
I don't know if he will join.
Show the screen.
Benny is out, so I don't think he will be able to make… I mean, he's not available on Slack, so I don't think he will be able to make it.
Madeja.
Couple of comments from… I don't know neither about Braydon.
from my side, it just… just came back from QFCO, and then there is a couple of pull requests ongoing, so please take a look there. One is for the JONA ID, following with the… There is existing geo name… Let me see if one of those links go there.
Yeah, those are the existing DNA ID. Let me see if I are here… Perfect, those are the existing ones. We describe, like, continent, country.
region, so on and so forth, but we are also using, in our site, the GON ID, which represents allocation, so feel free to take a look at the semantic convention later on, whenever you have time. Also, the one I have a protocol for the host name.
I just created, honestly, a few minutes ago.
based on the talk that they did on the KubeCon, we are… we have an IP, and we want to know the host name of that IP by using a DNS resolver lookup, and we want to store it, that, in our semantic convention, and the proposal is host name, based on the GitHub issue that was created, A few months ago, actually. That was the latest proposal, so here you can also find it.
Hey, Rob, good to see you.
**Rob Cowart** 06:53 Hey.
Sorry, I was… I was on the other bridge. I still had a stale Zoom link in my calendar, sorry.
**Antonio Martinez (Cisco Systems, Inc.)** 07:01 No problem at all.
So, it's really good that you also joined, because Josh is here today. So, Rob is also the co-founder of SIG, the company where Sven was… is working. We were missing you also in the QFCOM, Rob.
Okay, so those are two pull requests up there, so I recommend you. And one of the output from the… Chief Kong, was, like, we can start investigating semantic convention for SNMP, and the way that we consider we should do it is based on standard SNMP MIPS, and I have been reading a little bit about it, and there is… those, like the interface MIP, or the MIP version 2, so those ones are the ones that I would tackle first, and then from there we can continue. I know, Rob, that you started also working on a… an interface.
semantic convection proposal, I don't know where that ends up, if you end up creating a GitHub issue or not, but that would be following the same lines, honestly.
**Rob Cowart** 08:09 It's really just been time to move that over, but, I 100% agree on the standard MIPS. In fact, even some of the naming conversation we had about BGP stuff in the past, that was also based on the standard BGP MIP, so… I mean, I like this approach from a few standpoints, but, one, just there's already a huge body of work. I mean, that's gonna be… the data, the source of the data that we're dealing with is going to be coming from that. And even most… other, whether it's streaming telemetry sources, or even the names of the attributes in Linux, for example, if you get into the… what is it, the net slash whatever, whatever file system, it's also just the same SNMP stuff, so… you know, not only that, a lot of people don't realize this, but oftentimes, the counters and things to count these standard metrics, or these S&MP metrics, are actually baked into silicon and firmware and stuff, so, like, they can't always be changed easily.
So, if we went a totally different direction, you're almost excluding people that have, you know, the last decade of counters built into silicon, for example, so… leaning on those existing standards is just a smart thing to do, I think.
**Antonio Martinez (Cisco Systems, Inc.)** 09:36 Yeah, I think it's a starting point. Eventually, we will also want to… Put some standardization on semantic over vendor, especially, but that for sure will be way far from… from… from initial.
So yeah, that was one of the great output of the notes that we have in QFCO. Like, we should start modeling SNMP data, but that SNMP data should also be modeling from a standpoint of view of not SNMP technology, more from a network.
technology point of view, and the reason is because there are other technologies for getting network data, as GNMI, also. I mind there with other, like, OpenConf, I think is another one. So it's just a matter of Think on a broader… mine here, not just copying and pasting an SNMP… ID into an attributed a matric.
**Rob Cowart** 10:41 Yeah, agreed.
although I would probably argue that most of those other standards, at some point, when you dig down deep into them, they're still just based on the SNMP stuff below, you know? Yeah.
**Antonio Martinez (Cisco Systems, Inc.)** 10:57 Okay. Mixing that to you.
So that… go ahead, yeah.
**Rob Cowart** 11:03 I was just gonna say, on the open config thing, Sven mentioned that to me, we had a conversation, actually, about it.
And… and I've been trying… I spent a little bit of time over the weekend, and Have been trying to dig further and… into that.
as I… first, I will say, like, last time I looked at that's been quite a while ago, so, like, it's come quite a way, I would say.
The… the thing in my mind is I'm trying to think a bit about Entities, as well as, you know, attributes, metrics, etc, you know?
And so I'm, I'm trying to go through there a little bit and see where… In my ideal world.
There would be a clear mapping between what we do and some of these other emerging standards, what they are.
you know.
**Antonio Martinez (Cisco Systems, Inc.)** 12:08 With what we do? You mean SNMP?
**Rob Cowart** 12:10 Well, we're… we're hotel, right? So, like… I have an OTEL semantic invention for… A metric or an specific entity or something.
In an ideal world, we would have… An easy way of also converting to, say.
OpenConfig or something like that, you know?
And then there's also another one that complicates it. I forget the RFC number off the top of my head, it's in the 8000 somewhere. It is the RFC around expressing topology information.
And so, yeah, I'm trying to put my brain a little bit around reconciling those three things together for how that might make sense, you know, to have, kind of.
Three different standards that still have some type of relationship to each other, instead of just living on an island by themselves, you know?
I don't have a concrete thing to say about that, you know, yet. Maybe I will in a week, but, yeah.
**Josh Halley (Cisco Systems, Inc.)** 13:20 So, if I can chime in for a minute. So, Rob, I agree with you fully. I think whatever gets generated, there needs to be a single metric definition for CPU, a single metric definition for interface bytes or packets in and out.
OpenConfig, first time I saw it, it made my head hurt. Looking at all those Yang definitions, it's certainly not something which is, easy on the eyes.
However, it was the industry's attempt to try and standardize between vendors.
it's been… I don't want to say that we're close to being there. I know there's still a lot of entropy out there when it comes to OpenConfig, and it tends to be the service provider space that's adopted it more heavily than in enterprise.
But I think… it probably does make sense to look at, you know, what do we have on the truck with SNMP from vendor A and vendor B, and what's there in OpenConfig, and where's the gaps?
Before settling on final naming conventions.
For semantics. But, yeah, it's certainly… not perfect. OpenConfig, but I think with time, like, what we tend to see is, as more customers push for open standards, more of these OpenConfig, capabilities tend to feed into the platforms.
So with time, we are seeing even the enterprise platforms picking up more open config, capabilities.
Slowly.
**Rob Cowart** 14:55 I mean, I know… I know Junipers had some support for it in their, JTI, their kind of streaming telemetry flavor for a while. That was my first exposure to it, but, I haven't… I haven't… encountered it a lot more off… more recently, but, it was interesting to look at, actually, because I was actually thinking, like I said before, it's… it's come quite a ways, actually.
I think, ultimately, because, like, part of our goal here is also that… they're… Would at some point be a smooth transition, also, between the network world and the things connected to the network world, you know?
And, you know, that's the… that's… so, like, I don't know how it's kind of structured over on the OpenConfig side, if that provides it. Although, generally speaking, I think, Kind of a network interface of some form, virtual or physical, ends up being probably the bridge between those two worlds, but, Anyway, yeah.
Is that a big initiative at Cisco at all?
Do you know?
**Josh Halley (Cisco Systems, Inc.)** 16:09 It sort of… I don't want to say we get dragged. It's a standard that the industry's Built up, and all of the vendors are sort of… like, you'll see, you know, tenders going out which mandate open config for certain things, but this largely in the defense and the, In the service provider industry, they tend to want to work more with harmonious standards for model-driven telemetry and Yang-based configuration, more so than in the enterprise space, which I'd say is a little bit more slow-to-adopt automation-first principles.
**Rob Cowart** 16:55 Yeah, you could say that again.
**Josh Halley (Cisco Systems, Inc.)** 16:58 I was trying to choose the right words.
**Rob Cowart** 17:01 I mean, it just is what it is, you know. I think the difference that, you know, always happens is just how long network gear stays in operation.
You know.
It's rare to see a 10-year-old server in a data center. It's not very rare at all to see a 10-year-old switch, you know.
**Josh Halley (Cisco Systems, Inc.)** 17:19 Hmm.
**Rob Cowart** 17:21 and so, yeah, there tends to be lag in that regard.
**Josh Halley (Cisco Systems, Inc.)** 17:27 I think the difference also is, you know, for service providers, the network is their business, right? It's their core business. For the enterprise, under circumstances, the plumbing, so… You got that angle, Toto.
**Rob Cowart** 17:38 Yep, yep, yep.
So, Josh, is OpenConfig kind of your area?
**Josh Halley (Cisco Systems, Inc.)** 17:47 Mom.
**Rob Cowart** 17:48 OpenSpin, by any chance, at the… and brought up OpenConfig at the event? I don't know.
**Josh Halley (Cisco Systems, Inc.)** 17:54 I'm sorry, say again, real back.
**Rob Cowart** 17:55 Is this a person that spoke with Sven about OpenConfig? He said someone spoke with him about OpenConfig.
**Josh Halley (Cisco Systems, Inc.)** 18:00 I think we all huddled around after Antonio's session to sort of, you know, we all enjoyed his session. It was a great one to watch on video, if you guys have a chance, and we just got to talking about SNMP, and challenges with SNMP, and a little bit about OpenConfix, so… yeah.
**Rob Cowart** 18:17 I see, yeah, okay.
No, it just would be… I'm just trying to… maybe it would be good if I haven't… so I know if I have any questions, maybe you'd be a good source of… of someone to…
**Josh Halley (Cisco Systems, Inc.)** 18:28 You're welcome to ping me, I can't guarantee you that I got all the answers, but yeah, feel free, Rob.
**Rob Cowart** 18:34 Nope.
**Antonio Martinez (Cisco Systems, Inc.)** 18:40 Okay, so I will start by creating those.
GitHub issues, and then we can model it from there, hopefully. Always having into consideration the OpenConfig and Gemini one.
**Rob Cowart** 18:51 Antonio, because I'm actually probably further along on some of that, but just in various forms of my half-done work, and just haven't gotten to issues. If you kick the issues off, it probably gets me easier to start adding some stuff to them.
**Antonio Martinez (Cisco Systems, Inc.)** 19:05 Do you want that I focus by its model on the SNMP standard MIPS, or do you want that we start by the interface semantic convention proposal that you created?
**Rob Cowart** 19:16 Yeah, but that was… if you look at that, that was based on IFMIP. So, like, yeah, it actually is…
**Antonio Martinez (Cisco Systems, Inc.)** 19:22 Let us start with that one, then.
**Rob Cowart** 19:23 Yeah, I mean, the thought was, okay, what are the… thinking of hotel entities, like, what are the network entities? But ultimately, they're based on the MIBs, you know? What is an OSPF neighbor? Well.
It's exactly what's in the OSPF neighbor table in the MIB, you know, as an idea, right? So, like, it's all still was very MIBs-based, you know? In fact, if you… if you were to look at what I created there, you don't see a lot of verbatim MIB stuff in there, so…
**Antonio Martinez (Cisco Systems, Inc.)** 19:55 Okay, sounds good again.
**Rob Cowart** 19:56 I think the biggest challenge we're gonna have is just… because, you know… OTEL, as I've learned now, right, hotel has a very distinct ways that it… communicates information.
that… that's just, you know, that's probably, from someone like myself, who's coming out of the more traditional network observability, SNMP, etc. space.
that's always gonna be a mind shift, you know?
Like, in octets, out octets. It's really just… octets, or I.O, with a direction in and out.
as a separate attribute, you know? And, like, there's little details like that, they're just… they're just mind shift, not saying one's right or wrong, I can actually see some… good reasoning or elegance in the way that OTEL does it, but it's still just unusual for someone that's coming from the traditional network space, you know?
**Antonio Martinez (Cisco Systems, Inc.)** 21:05 Yep.
Sure.
**Rob Cowart** 21:09 Who was it? Last call, This is probably, actually, would be a good idea.
Braydon shared a document around, kind of like, like, best practices type of things for, Oh, there we go.
now that I think about having just said that, you know.
creating a… I think what we need to do is get a couple… of, like… let it be interfaces MIB, maybe entity MIB, host resources MIB, although host resources are largely map to the host stuff in OTEL, probably.
you know, maybe OSPF, BGP, kind of like those basic standard stuff.
And get those done?
That we're really happy with, and then we can create a similar document like this that maybe addresses this mind shift you need to make if you're converting from SNMP to the OTEL semantic convention.
And that way, that way, a multitude of people could start contributing more here, you know.
**Antonio Martinez (Cisco Systems, Inc.)** 22:27 Yeah, with regard to that, what you just said is, like, let's focus on the standard, it will fall under the general class. I imagine you assume, but the specialist class will fall under the vendor specific, like, it will be, like, UniPer, Cisco, whatever. And then with what you just said, we are also, let me find it quicker here.
We are also, what is it called? Code owner of the SNMP receiver in the collector, so if we go to the contrib, we are code owner. So, Sven and I, we were also having a chat there, and our idea is, like.
Once we support, because that was also the recommendation from the maintainer, when we support something on the semantic convention, let's create a profiler that do from… let me go to the receiver, sorry.
And… it shouldn't be… Sure.
**Rob Cowart** 23:20 It's a reference implementation.
**Antonio Martinez (Cisco Systems, Inc.)** 23:22 Correct, we… our proposal is, like, today.
we provide the flexibility, so each person is able to create their own metric name and their own ad seal name as they want, and that works today. So, we don't want to remove that flexibility, because there are tons of vendor-specific, but our idea is, like, once we support something standard, and we know the OID is a standard thing and so on, we create a profile saying, okay, the if MIPS, it are on that profile. So you just run the SNMP receiver with that profile being set.
The main goal is, like, everyone use for those the semantic commands on them, we grow there, gradually. That is our goal, as we have also the… we can manage the roadmap of that receiver. At the same time, there is also another receiver, which is the… here it is. That is… code owners are the… Splanting, so we could… try to… to help there, but… and we can for sure create the GitHub issues and the code, but they are the one deciding if they want to, I mean, supported those profiling logic, but I think there is no doubt that that should be the way to go.
**Rob Cowart** 24:43 Yeah, that sounds… makes sense to me.
**Antonio Martinez (Cisco Systems, Inc.)** 24:48 period.
**Rob Cowart** 24:49 And streaming telemetry, there will be… you know, like I said, Juniper JTI, I think Cisco's model-driven telemetry does GNMI? One of them does, that they have, yeah.
**Josh Halley (Cisco Systems, Inc.)** 25:03 We've got different export formats, yeah. So GNMI is one. The level of which We can export with GNMI, depends on the platform.
But GNMI should be… arguably, GNMI should be the North Star from a, telemetry perspective, because you're building one socket for both your config and your telemetry streams. You're not constantly iterating sockets like you would natively with, with Yang or ResConf.
But with net confidence, yes, continuous concern.
**Antonio Martinez (Cisco Systems, Inc.)** 25:39 Jason, with regard to… to which telemetry? Is it the same here? Like, each vendor is streaming different telemetry, or is there some sort of a standard? Do you know where…
**Josh Halley (Cisco Systems, Inc.)** 25:49 So this is OpenConfig, right? So you should have the ability, when you're subscribing to a stream, you should be able to choose whether it's a vendor-agnostic stream, which is open config, or whether you're pulling the specific Yang… libraries associated with, the vendor-specific stuff. So there tends to be both, at least within Cisco platforms, you tend to have your open config, Your open config hierarchy that you can pull from, and then you've also got your vendor-specific it's not a one-to-one, there will be gaps, and I think this goes for every vendor, but if you're looking under GNMI, it would be that you're tapping, essentially, the open config streams.
And then eventually for things… for obscure stuff, which is, for the larger platforms, so for some of the obscure stuff, that's when you need to, dig into potentially vendor-specific things, where there's, so far, no alignment between vendors.
Okay, that…
**Rob Cowart** 26:53 I think an example, an example.
I'm sorry, go ahead.
**Josh Halley (Cisco Systems, Inc.)** 26:56 Just an example of that would be quality of service, right? Juniper handles quality of service differently to Cisco, and that's where you see things diverge.
Sorry, Ron.
**Rob Cowart** 27:07 There's no standard on quality of service. Everyone handles QoS differently.
has their own MIBs. But in general, you tend to, even on the standard stuff, like, it's… you always have this problem that the vendors have a need to differentiate their offering in the marketplace, so they have, like, this standard plus this little secret sauce. Well, if you bought that platform for the secret sauce.
You sure as heck want to monitor the secret sauce, and so you probably do care about some of those vendor-specific extensions.
**Josh Halley (Cisco Systems, Inc.)** 27:41 And that's where our customers need to tell us to bring them into OpenConfig, so it's standard. So,
**Rob Cowart** 27:48 Some of them… some of them are challenging on standards, just because it's like, there's only one vendor in the world that has that metric, you know? So, or that piece of information, some… I mean, they can often be named different, but conceptually has a given.
**Josh Halley (Cisco Systems, Inc.)** 28:02 Hmm.
**Rob Cowart** 28:03 You know?
So, yeah.
**Josh Halley (Cisco Systems, Inc.)** 28:07 No, I agree, but I think looking at the problem space, there's a huge amount of low-hanging fruit, which this team here can already start working on, right? It's not that we need to look at what's the weird standard from X25 on Cisco platforms, right? We can… I think there's plenty of stuff on the truck already, and I guess the question is, you know, what are the things to tackle first?
**Antonio Martinez (Cisco Systems, Inc.)** 28:33 Couldn't agree more, yeah.
**Rob Cowart** 28:34 There's a good body of work on the core standard MIBs, so, yeah.
**Antonio Martinez (Cisco Systems, Inc.)** 28:43 Looking?
So I think we are on… on track on nonsense. Something else that I would like to highlight also is, like, through the conference, I met with that guy, Alexander… Thiago from Guseuse, Alexander from Intel, Zoomatillo, who is also an OpenTelemetry contributor from Ericsson, and they would be… the three of them would be interesting on modeling the data centers.
Intel for now.
different point of view that only network. They also want to see, Variety of different things about the, how it works their devices, but we have all a common theme, which is modulating the data center, and why this is important is because as part of my work also inside of Fisco, I am helping Meraki and Catalyst also to modulate their telemetry data, and here we fall perfectly under switches and routers, and they are all, at the end of the day, in a data center, so I think I will try to invite them. They said that they would like to join from time to time. They have also some work, because that guy from Alexander from Inter have been working with NVIDIA, some sort of partnership there about standardization. So they have already, like, a… Hmm… predefined or proof of concept there, and he will share with us, he said. So yeah, I will invite them, and hopefully we have more people sharing, and hopefully that doesn't slow down things.
But yeah, more… more people with high knowledge about the domain, so yeah.
I will try to convince them to join and provide their feedback.
Because that was one of your comments, right, Rob, when we started that group to modulate also not only an interface level, but at higher level, right?
**Rob Cowart** 30:37 Oh, I mean, I would say across the board, there's plenty to be done besides just, like, interfaces, yeah.
**Antonio Martinez (Cisco Systems, Inc.)** 30:46 We don't actually picture them.
I just came from Qupcom, but I will pin them.
to join us.
Okay, I know Braydon is also here, I don't know, Braydon, if you want to say something for Kivko, or any of you guys have any other comments?
**Braydon Kains (Google LLC)** 31:03 No, I think you… pretty much covered it. Josh, thank you for joining us. Appreciate it.
I thought KubeCon was good.
And we had some good discussions, but… I don't think we made any, any major changes to, like, our roadmap or what we want to do. I guess the big one is we did talk about, entities, and the fact that, one of the big, major contributors to entities is stepping down from hotel contributions, because he's moving on to a new company. His name's Dimitri.
**Rob Cowart** 31:40 Oh.
**Braydon Kains (Google LLC)** 31:42 So… Entities will be strapped.
for capacity, because Josh Surrett is the other most… popular… most… most prominent contributor, and he's just spreads super thin. I work with him, so I… I know for a fact he spreads super thin. So, there is room for us to… step up and help a bit with entities as a signal where necessary to model things. I suspect that some of the… some of the things we want to model will require some of the more advanced, like, entity relationships stuff that is talked about, but not, like, embedded in the signal yet, that we might Be able to help drive by providing examples where we need it.
**Rob Cowart** 32:25 Yeah, they said that on the calls I had joined, as kind of like, okay, we could probably… they'd like to see our ideas there to… Provide more real-world… Examples of the different relationship types and things like that, so…
**Braydon Kains (Google LLC)** 32:42 Yep.
I… I can probably try to start joining those. I have an overlap with another SIG, so it might be a, like, a… you know, every… every couple weeks, I'll go to the entity SIG, and then I'll go to the other one, whatever.
**Rob Cowart** 32:57 I was pretty regular for a while, but I've just been overwhelmed the last few weeks, so… Yeah.
Probably get back to it soon.
**Antonio Martinez (Cisco Systems, Inc.)** 33:07 what I was doing with Lyudmila during the KivCon also was, like, entities can modulate.
relationships today. I mean, it works.
See what's saying with me?
**Rob Cowart** 33:19 have hardly any types, that's the problem.
**Antonio Martinez (Cisco Systems, Inc.)** 33:23 What do you mean by type here?
**Rob Cowart** 33:25 like, and I'm not saying these are official, but, you know, just to give you an idea, like, an interface can be a member of a link aggregation group.
a, you know, a… network flow can be tunneled through a VPN You know, like a session within a session, or encapsulated, or, you know, that type of stuff, right?
So, so there's, there's lots of layering relationships and things like that that, you know.
Absolutely. What is a VLAN tag? You know, is it a member of relationship, or is it a… has this attribute? Like, like, you know what I mean? Like, relationships, say, of an interface to a VLAN, or, you know, an interface to a lag, or a… or it's connected to something. Like, there could… could be a whole bunch, actually, you know?
**Josh Halley (Cisco Systems, Inc.)** 34:25 You're gonna have those complexities when you start looking at VRFs and protocols also. So if you're gonna start metricing out the protocols, you're gonna have the protocols existing within a given VRF, Potentially over the same physical interface.
Right, so there's challenges to… there in terms of the entity mappings?
So it's certainly a bigger piece of work to look at how all those relationships could look like.
**Antonio Martinez (Cisco Systems, Inc.)** 34:54 Okay, but I still don't get it, if… relationship exists where… what is the problem? Like, we don't have enough… And they were calling it, relationship types for your use case, Rob, or…
**Rob Cowart** 35:08 those types, the specific types have not been defined yet. That's say, like, this is, like.
**Antonio Martinez (Cisco Systems, Inc.)** 35:15 Okay.
**Rob Cowart** 35:15 What does it mean to be a member of?
a group, or, you know, something like that. Like… well, show us an example of a member of, and then we'll know what it means, and can start to define it, and put… you know what I mean? Like, like, it's more like… Needing real-world examples that substantiate or justify Saying this relationship type has a specific purpose, you know, and why you would use it, and that kind of thing, if that makes sense, yeah.
**Braydon Kains (Google LLC)** 35:45 the relationship so far that have been modeled are, like, not complicated enough to substantiate, like, the breadth of relationships that we expect. A lot of them are, like, this VM is a EC2 VM. Like, they're relatively simple, like, part of, or is, things like that. So we're probably gonna… I think that's… We just need to actually give the examples of how we're gonna use them. I don't think entities, like, is trying to specifically restrict the relationships, just there hasn't been enough examples yet. I think that's all.
**Rob Cowart** 36:17 Yeah, yeah, exactly.
**Antonio Martinez (Cisco Systems, Inc.)** 36:22 Braydon, do you… do you want to be the point of contact with the entity, or do you need help there, so we can try to… appointment.
**Braydon Kains (Google LLC)** 36:32 and the entity's SIG Oh, I'm getting… I'm getting mixed up. My time zone hasn't swapped back to normal yet, so my calendar's all weird, but… the… the entity SIG overlaps with another SIG. I don't remember which one, but it overlaps with another SIG I need to attend regularly.
**Antonio Martinez (Cisco Systems, Inc.)** 36:56 Hmm.
**Braydon Kains (Google LLC)** 36:56 So…
**Rob Cowart** 36:57 I've already.
**Braydon Kains (Google LLC)** 36:57 I can probably split my time between them, but…
**Rob Cowart** 37:01 I've already been joining those, so I'm happy if there has to be a point of contact to be a point of contact, so…
**Braydon Kains (Google LLC)** 37:10 I think… I think we could… you could probably put us both down for that, because… I also… I work directly with Josh, He's, like, our… like, higher level technical leads, so I speak with him often, so that we can put it… we can put us both down.
**Rob Cowart** 37:27 My impression was actually they were very interested in having The potential real-world examples that we might provide to kind of… push it forward. So, this is…
**Braydon Kains (Google LLC)** 37:38 Yeah, I think.
**Rob Cowart** 37:38 Very, very receptive to… collaboration there, so… That was my take.
**Antonio Martinez (Cisco Systems, Inc.)** 37:54 Communicate address.
Okay, so as I was mentioning at the beginning, that super requests are up there, feel free to take a look. I will start creating, I sent to myself, I start creating, Democratic convention for this… interface MIP model, and yeah, we should go… and try to connect with those folks in case they want to help us start joining us.
Okay.
**Rob Cowart** 38:21 Yeah, would it be helpful if I just shared with you the stuff I had already pulled together on InterfaceMib?
**Antonio Martinez (Cisco Systems, Inc.)** 38:28 Absolutely, unless this is the,
**Rob Cowart** 38:32 I don't know if I asked W.
or not.
**Antonio Martinez (Cisco Systems, Inc.)** 38:34 Unless this is that one, which I will take into account.
**Rob Cowart** 38:38 Yes, it just hasn't been updated further.
**Antonio Martinez (Cisco Systems, Inc.)** 38:41 Yeah, that…
**Rob Cowart** 38:42 That's it, yes, correct.
And like I said, if you go into there, you're gonna see it's all,
**Antonio Martinez (Cisco Systems, Inc.)** 38:48 On the right?
**Rob Cowart** 38:49 Yeah.
**Antonio Martinez (Cisco Systems, Inc.)** 38:50 Okay, yeah, I will take that into account. I will even link it into the house that is public.
Okay.
**Rob Cowart** 38:59 And some of that stuff at the bottom is just more my, notes and stuff as I was pulling it together, so… Yep.
**Antonio Martinez (Cisco Systems, Inc.)** 39:10 Sound good to me?
See you, see you next.
**Rob Cowart** 39:13 Jodeo, completely selfish question I have for you.
I heard Sven gave you a demo of our announced product at KubeCon. What was your thought?
**Antonio Martinez (Cisco Systems, Inc.)** 39:23 I like it, I like your product, guys. I like how you guys are connecting network, application telemetry data on the same view. I think it's one of the first Observability, what kind of order, doing that?
I think this is what we are trying to… to reaching all together. It's the same, like, Thousand is focusing a lot in network data, or Cisco in general, but we don't have yet the… Or at least it is slow, the capability to merge both things together, so great job there, yeah.
**Rob Cowart** 39:53 Yeah, thanks.
They didn't good work.
Sven especially. I mean, a lot of people don't realize, like, Elastiflow was more my thing, SIGI was more Sven's thing. Like… Building on that foundation. So, yeah.
**Antonio Martinez (Cisco Systems, Inc.)** 40:09 Yeah, and it's good that you guys are donating or helping there.
**Rob Cowart** 40:12 Yep.
**Braydon Kains (Google LLC)** 40:13 Seems like they got decent traffic at the booth, so that's good.
**Rob Cowart** 40:17 It could always be more. Always.
**Braydon Kains (Google LLC)** 40:21 It was just a quiet KubeCon in general, too.
**Rob Cowart** 40:23 Was it really? Interesting.
**Braydon Kains (Google LLC)** 40:24 It was… it was pretty quiet.
**Rob Cowart** 40:28 Do you think that's just broader econ… you know, macroeconomic situation, or,
**Braydon Kains (Google LLC)** 40:35 Yeah, there's a lot of things it could be. It could also be that it's at Salt Lake City again.
And people who go to repeated KubeCons probably aren't super excited by that. I wasn't super excited by that.
Could also be that the Agent Con, MCP con, there's quite an overlap between.
**Rob Cowart** 40:53 the audience.
**Braydon Kains (Google LLC)** 40:54 audiences of those two now.
And it was… it was a relatively quick follow between those two.
And it could just be the, like, travel budgets also.
I think there's… there's starting to be a, like, precedent that, like, KubeCon EU is the super hype one, and then NA is the smaller one, and that then, like, is a compounding problem, because companies don't want to pay people to go to the smaller one. Why not pay to go big at the big one?
**Rob Cowart** 41:20 Oh, interesting. Yeah, I've been in the EU myself, I haven't been to North America, so…
**Braydon Kains (Google LLC)** 41:27 Having been to both the.
**Rob Cowart** 41:28 Pretty impressive one. It was a couple years ago now, but it was still pretty impressive, so, you know.
**Braydon Kains (Google LLC)** 41:34 NA was still good for… for me, because I just… I just wanted to see… Hotel people and talk shop, and that part was good.
So, I was happy, but I think there were a lot of, like, you know, startups looking for sales leads that were not super happy with the conference.
**Antonio Martinez (Cisco Systems, Inc.)** 41:48 This one's fun.
**Rob Cowart** 41:49 I think we were looking for feedback more than anything else, you know, having something new we're pushing out, so… and that was successful for that. People didn't realize it, but, like, we were A-B testing messaging on the booth and all kinds of stuff, so… Cool. Well, maybe next time I'll get to see y'all in person, so…
**Braydon Kains (Google LLC)** 42:11 Yeah, hopefully, I'm gonna try and go to EU.
I'm trying to stack the deck, submitting lots of stuff.
**Rob Cowart** 42:16 It's in Barcelona again, I think.
**Braydon Kains (Google LLC)** 42:18 Barcelona, yeah.
**Rob Cowart** 42:18 Yeah, yeah, that's the one I've been before, was there too, so… Alright.
**Braydon Kains (Google LLC)** 42:27 Thanks, everybody.
**Antonio Martinez (Cisco Systems, Inc.)** 42:29 Hello?
**Matthieu Noirbusson (Sensor Factory)** 42:30 too, right?
**Rob Cowart** 42:31 But…
**Antonio Martinez (Cisco Systems, Inc.)** 42:46 Hello, meaning you.
Premium?
Pelave durino.
Love it?
Let me answer my phone, Caldon.
