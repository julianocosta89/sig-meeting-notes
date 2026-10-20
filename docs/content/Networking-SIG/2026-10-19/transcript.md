SIG: Networking SIG
Date: 2026-10-19
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Antonio Martinez (Cisco Systems, Inc.)** 01:03 Hey, everyone.
**Serena Kei** 01:10 Hello.
**Marc Netterfield** 01:13 Hello, hello.
**Antonio Martinez (Cisco Systems, Inc.)** 01:15 Sorry if I joined late. I don't know if the rest, Ben and the other, are gonna join, so let me… Pim them quickly, if you don't mind.
**Serena Kei** 01:28 Yeah, not at all.
**Antonio Martinez (Cisco Systems, Inc.)** 02:08 Okay, he said that he's not coming today into the meeting, so we can have a briefly one, no problem.
they are actually saying that we can even cancel it. Okay, but we can go briefly on the topic that we have today.
By the way, Serena, this is your first time joining, do you want to introduce yourself or provide some context?
**Serena Kei** 02:36 Sure, yeah, it's, my first time joining. I'm… I work at Grafana Labs. I currently… I'm working on OpenTelemetry support, for Kubernetes monitoring.
And, yeah, networking is kind of, like, the next area I'm interested in. I'm pretty new to open telemetry, so I'll probably be pretty quiet for the first few calls.
To see how things work, and… To learn a few things. Yeah, nice to meet you all.
**Antonio Martinez (Cisco Systems, Inc.)** 03:08 Awesome.
**Serena Kei** 03:11 I'm based in East Coast Canada, so, Eastern Standard Time Zone, but I usually wake up pretty early, so…
**Antonio Martinez (Cisco Systems, Inc.)** 03:18 Awesome.
And your interns on the network group is for something specific, apart from the OpenTelemetry side, or…
**Serena Kei** 03:27 Yeah, OpenTelemetry support for Kubernetes. I'm pretty new to both Kubernetes and OpenTelemetry, so my knowledge will be more limited.
I'll try and contribute where I can.
**Antonio Martinez (Cisco Systems, Inc.)** 03:41 Awesome, awesome.
Perfect thing… So, for today, I have those topics about the Mac, but it could be great to review that with Sven while he's back, so let's move them for the next one.
And for the collector contribut SNMP receiver, it's great that we have Marc here. Sven and myself are now code owners, which is great, because it means that that group will keep maintaining that SNMP receiver.
And we should start investigating on the current status and roadmap, honestly. I know Marc is quite involved in there, so I love it.
Between the existing issues, I saw that there is, like, the SNMP lock traps.
And there was some discussion about creating, like, a separate, component, or reusing the existing one, so we decided at the end about reusing the existing one.
And here you can find out the two pull requests that we have for LF. Honestly, it's… the main one is that one, which is at the support, and the other one was just some simulation that I needed in order to… to play around and to start using it, so if you also want to take a look at that, great. That purpose is not, like, mandatory to be merited.
Hey, do you want to add something, Marc, there?
**Marc Netterfield** 05:04 No, I hadn't seen that second one, so I'll take a look at that, in a little while.
**Antonio Martinez (Cisco Systems, Inc.)** 05:09 Awesome. And then those two tickets also came through conversation that we have recently. One of them is about, MIPS file, that will be quite useful for once we have the SNMP traps logs. The reason why is because instead of having the OIDs, directly we will have the actual, metric name associated with. I know other places like the SNMP exporter from Prometheus already doing that on your… your… the… sorry, the proposal that you have previously about an extra component was already doing that. I really like the idea, but I consider it's better to have in a separate issue, so pull requests don't get bigger and we don't block. But yeah, I really… very, really interesting about that. Feel free to… to take it if you consider that, Mark.
And the other one was the refactoring, so let me also clarify a little bit over that. When I started working on the SNMP lock traps, I realized that we need to do a separation between traps and pooling, and then I directly started creating that improvement in the config, i.e, you can actually see that it was Let me see if that's loads quickly… Yeah, so I started doing it over on that pull request, but then Marc did the proposal, like, if we are gonna… improve the configuration? Why don't we do it following a new approach, in that a new approach will follow the same one as the promises exporter using the SNMP exporter logic, where I will need to dig a little bit and learn, honestly, but if I understand correctly, you guys have, like, a log, sorry, a file, which contains all the metric associated, so that file will be… will be used in different platform, not only in OpenTelemetry, and we will take advantage of using it here, right? That's kind of level.
**Marc Netterfield** 07:22 Yeah, that's the idea. Tons of people already have this file.
**Antonio Martinez (Cisco Systems, Inc.)** 07:26 I worked…
**Marc Netterfield** 07:27 with, like, 6 or 7 different versions of SNMP configurations in my career, I feel like I just don't want to have to reinvent it again.
**Antonio Martinez (Cisco Systems, Inc.)** 07:36 Honestly, so…
**Marc Netterfield** 07:38 We would have to see if maybe if there's any specific use cases that we would want to address that aren't currently covered, but right now, I don't think that I'm aware of any off the top of my head, so…
**Antonio Martinez (Cisco Systems, Inc.)** 07:47 Awesome. So, if you don't mind providing some more context to that issue, about, like, examples of how that file looked like, so we can start exploring that ticket. So, I really like the idea of having, like, a full configuration under SNMP receiver.
Improving the… Improving the fields, to…
**Marc Netterfield** 08:09 would be more.
**Antonio Martinez (Cisco Systems, Inc.)** 08:09 more, like, using the latest use cases, but we need to understand better before we start taking any action, I would say. But yeah, I like the approach.
Awesome there. And then… in other list of topics, we have also the Splant team is… sorry, I cannot open that? The Splant team is also working on a new receiver, which is the JNM9. I don't know if you have seen that before, it's like a new, Network pulling approach, but instead of being a pulling, it's a push, so the network device is actually pushing the… telemetry data, and here we can receive it. You can see more here, most likely, if that link is right. Yeah, right, your PC Management Interfaces is acronymal. From what I am hearing in Cisco, it seems to be this is quite use nowadays, like, in new hardware, honestly. So it's great that they are, contributing that to open telemetry, the first thing, and the second thing is, like, I consider… I just mentioned here that it would be great for us, for the network group, to keep an eye there, but I think everyone in the room would be more than interested to see what they are doing and keep on the radar. I guess it will be the next Base of network telemetry data in the future.
**Marc Netterfield** 09:36 Yeah. I remember a couple years ago, I met up with the Ken Dick people, and I was discussing, like.
this is 3 years ago. I was like, how many of your customers are, like, actively using, streaming telemetry, or GNMI, or, you know, all the related, protocols? And at that time, they said, they're like, it was, like, 3. Not, like, 3%, just 3, you know? But it feels like a lot of people have been labbing it out, experimenting with it over the last couple years, and so I feel like it's… This is the time for it.
**Antonio Martinez (Cisco Systems, Inc.)** 10:07 friends for… for Splunk, as far as I, unaware of, they are starting supporting it on the pork that they have from the OpenTelemetry Collector Contrip, because there were customers asking for it, and now they are contributing it.
So yeah, most likely there are more customer interests.
But SNMP will never be removed, honestly, because hardware tends to long for many years, so there are many hardware still out there using only SNMP.
Okay.
**Marc Netterfield** 10:39 I don't imagine, like, UPS vendors and things like that that speak SNMP ever switching over to, like, a streaming telemetry.
**Antonio Martinez (Cisco Systems, Inc.)** 10:47 Right, that will be a really slow… Switch.
Okay, so… I guess we will dip into those topics more once when he's also back, and now I saw that Brian… Braydon is here, and are you?
I don't know.
Ryan, are you in the call?
Maybe not. Okay, so I will briefly explain what's going on with that pull request, in case I can get any feedback. We… what we are trying to fix is the support of adding the new… sorry, no, the new… the metric for… sorry, the attributes for MAC address into the community.
Into the semantic convention, and that's the proportion, but there is… another mate from the OpenTelemnity community, I don't know if you know him. He's everywhere.
Right. Okay, nice that you are now here, because I wanted to get your attention here. So, his main concern is not against what we are doing, his main concern is, like, we are against… not against… we are gonna… Create a conflict with the… Let me see where all that conversation started. With the, E… CS from Elastic, Because they are calling it directly Mac instead of Mac.address. So, I don't know if, as you are more familiar with how semantic convention works, and how… we should tackle the alignment between OpenTelemetry Dismantic Convention and ECS Elastic Convention. From what I understood, they donated to the OpenTelemetry, but it doesn't mean that we cannot things that are different, at least from the way that, I understand it.
Dmm…
**Braydon Kains (Google LLC)** 12:46 Yeah, I have… I have no idea where this is… where this is coming from.
we haven't… we haven't needed to stay aligned to the way ECS does things in a long time.
That's… that's my… that's my memory.
So, I don't know why… I'm gonna… I'm gonna stop myself. I'm gonna stop myself from making the comment I wanna make.
Correct. So the reason we were gonna do…
**Antonio Martinez (Cisco Systems, Inc.)** 13:17 Go ahead.
**Braydon Kains (Google LLC)** 13:17 Mac.address.
rather than .mac was so that we don't make Mac a leaf. Is that the idea?
**Antonio Martinez (Cisco Systems, Inc.)** 13:27 Totally, that's the idea, because the… Rob, Sven see the value of having, like, organization, all… I… So, in the future, we can have other things apart from only the address. So… and that guy is honestly happy about the proposal, but what he's not happy is, like, if Elastic donated to OpenTelemetry, we have conflict with the ECS approach, which… I mean, it's not something written that we always have to follow. Things evolve.
And what I suggest is, like, if a customer is sending that data to Elastic.
Unless they don't want to have a config, they can just have an adapter in the middle or something, like a collector that will Adapt to the… to their convention, let's say.
But that's not really… I should block.
a proposal. That's the way, Serena and Robert are also trying to… Combine on that direction, but yeah.
**Braydon Kains (Google LLC)** 14:26 Yeah.
I… I have no idea where this ECS alignment thing is coming from.
like… the… ECS was donated a long time ago.
And so we adapted many of the things from ECS to fit semantic conventions rules. Like, it was the other way around. We weren't trying to stay in line with the way ECS was defined. I don't… I don't think we've ever had that direction. Like, it wasn't… it was never bidirectional.
That's… that's my… that's my recollection. So, this idea that we should be pushing back on something because it doesn't align with the way ECS does it. Has… I've never seen anyone push back on that, and… okay, the… Let's… let's… Let's not worry about this right now.
I'll comment… I'll comment on the PR2, saying we should go with Mac.address.
**Antonio Martinez (Cisco Systems, Inc.)** 15:27 Let's do that, yeah. That's the plan from my side, so once we have your approval, we will ask Lyudmila, most likely, and we will get merged here.
Even when we have that small conflict, that's my suggestion, too.
Okay, I think we are all clear there. And then for the other two, they are already approved by Sven and yourself, and the other guy, I don't remember, his name… yeah, Chris. Oh, yeah.
**Braydon Kains (Google LLC)** 15:56 Crystal.
**Antonio Martinez (Cisco Systems, Inc.)** 15:57 Yeah, he'll also approve it, but how should we proceed now? How can I ask for merch? Should I ask someone in specific, or…
**Braydon Kains (Google LLC)** 16:06 Probably works.
Just post in the Symante Convention Slack channel saying, we're pretty sure this is all the necessary approvals.
**Antonio Martinez (Cisco Systems, Inc.)** 16:14 Okay. So, just put it on.
**Braydon Kains (Google LLC)** 16:16 is a maintainer, too, so…
**Antonio Martinez (Cisco Systems, Inc.)** 16:19 Just mention in there, like, could you guys merge it when you have time?
**Braydon Kains (Google LLC)** 16:23 Basically, saying we're pretty sure this has all the approvals necessary, could it be merged?
**Antonio Martinez (Cisco Systems, Inc.)** 16:30 Okay, I will go in that direction.
Before you joined, we were talking a little bit about the SNMP receiver, that… Okay, you're aware of, perfect, so…
**Braydon Kains (Google LLC)** 16:42 I remember seeing that. That's good.
**Antonio Martinez (Cisco Systems, Inc.)** 16:45 That's my… Far for today's agenda, I don't know, guys, if you have something else.
Okay, so we can most likely follow up on the next one with more topics.
**Braydon Kains (Google LLC)** 17:08 Sounds good.
**Antonio Martinez (Cisco Systems, Inc.)** 17:10 Have a good one, see you all.
**Braydon Kains (Google LLC)** 17:12 Thanks, everyone.
**Marc Netterfield** 17:12 Very good. We'll talk to you later.
