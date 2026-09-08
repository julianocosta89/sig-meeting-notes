SIG: Networking SIG
Date: 2026-09-07
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Giuseppe Ognibene (Coralogix)** 03:10 Hi, everyone.
**Matthieu Noirbusson (Sensor Factory)** 03:15 You know.
**Antonio Martinez (Cisco Systems, Inc.)** 03:36 Hey there! Let's see if more people join today.
So, these are what people are already doing today.
happy that we don't have roam around, as they have different topics for… I have follow-up conversation for them today, but it's fine.
But it's here, too. That's where… So, the first thing that I want to mention is from… On that meeting, sorry, from that request.
There was a follow-up.
Let's see if I can find it.
Where… where we needed to add the OpenTelemity teams?
for the approvers, maintainers, and triageers. My question here is, like, does it make sense that we should add ourselves into the… Provers, at least, or maintainers, or triageers.
The people that are on those teams are… Not active anymore.
And if you know the process to do that, that moves under Teams.
Alright, thank you.
initiatives.
**Stephen Lang (Raintank, Inc. – Grafana Labs)** 07:48 Maybe we'd need, Braden? Would he be the one that has access, or,
**Antonio Martinez (Cisco Systems, Inc.)** 07:54 Yep, no, me too.
**Stephen Lang (Raintank, Inc. – Grafana Labs)** 07:55 Because…
**Antonio Martinez (Cisco Systems, Inc.)** 07:57 So, majority of the members here are not active anymore in the domain?
So I don't know if… how we should… be able to… to add it ourselves as maybe as a program, 3 hours, maybe, to start with?
But we need to do that. Antoine, who might be active around.
Could help us here, but… My dear.
Do you have any input on that topic, how we could… Otherwise, Factory?
**Stephen Lang (Raintank, Inc. – Grafana Labs)** 08:34 I guess we can, we can ping Braden, right, on Slack, see if he knows how… To maybe, escalate it, or… Otherwise, we'd need to create new teams, right? Unless we can get in touch with those existing maintainers.
**Antonio Martinez (Cisco Systems, Inc.)** 08:54 Nope, nope.
Or who you suggested, sorry, Christopher?
**Stephen Lang (Raintank, Inc. – Grafana Labs)** 08:58 Braden?
**Antonio Martinez (Cisco Systems, Inc.)** 08:59 Hmm, yeah, yeah, you're right.
Yeah, I will… I will follow up with him. I will take that action, I think.
**Stephen Lang (Raintank, Inc. – Grafana Labs)** 09:06 Okay, thanks.
I guess we're trying… Try and get the existing teams.
Sort of reallocated, if possible.
**Antonio Martinez (Cisco Systems, Inc.)** 09:15 That's the most sense to me.
So here there is a… a pull requests.
And the one that they opened before, that is still on draft, that's true.
please take a look whenever you have time. I applied some feedback, that's why it was great to have ZVA here in the meeting to follow up the feedback, but yeah.
It's about, clarify with regard to network, local network peer, also server address, and… Client address, or one to use one or to use the other.
Here you have the information. Client server, source destination, network local, and peer. It's… there is confusion about when to use which.
Yeah, it's try to clarify for where it's a little bit still, hard to follow.
But yeah, feel free to take a look.
I will be off next one. I don't know if any of you have been on the last meeting where they were talking about the IP address type, enrichment. I think… Giuseppe was here. There was an action item for Sven to go into the semantic commission. Do you know anything, if that was…
**Giuseppe Ognibene (Coralogix)** 10:25 No, I remember the action item, but I don't know if it went there.
**Antonio Martinez (Cisco Systems, Inc.)** 10:33 Yep, okay, I will chug it for next one. Robert from the… Hmm… Elastic Floating suggested some metrics, sorry, attributes and metrics for the interface.
the goal was to review, in home, and later here have proposal. I don't know, guys, if you had a chance to look into. I think, Giuseppe… Stefan, I've seen that document before, in the past?
Emm… with regard to the feed… to the proposal, I have some feedback, like, I know it's… Hard to talk here about it, because you guys might not have a lot of context, but one of the feedbacks from my side is, like, there is an attribute called Network Interface Banguage.
Which, in the proposal is, like, contain the current bandwidth in bytes per second. I have the feeling that that should not be an attribute, it should be more like a metric from the… from the network perspective, with regard to that interface.
I also have the feedback about the following attributes.
Here we have the… code, sorry, mode, to true to false as a boolean. My proposal is, like, instead of calling promiscuit mode, we just call it mode, and then we have a values and a string which contain the mode that have been used, and if there is no value being used, we just don't have any, or we can have, like, a… And… Opt Valley. But the idea is, like, that is quite… Limiting to only promiscuous mode, and in case we have in the future other, that will be not the best approach.
I will leave that feedback for him. And something similar to the connector present, there is another one for how it is connected, if it is connected or not connected. True, if the interface of the half a physical connector, false otherwise. Here, we can do something similar to specify the actual connector being used.
That could be, like, LD45, LC, or any other.
With that being said, we also can say Yeah, the problem might be, like, that data might not be always available, so I can… I can think about it again, but… Yeah, I mean, having a Boolean as an attribute… yeah, go ahead.
**Marc Netterfield** 13:07 I was gonna go ahead and say both of those are inherited from, like, old SNMP spec, so I'm not sure… How we might, get that information without, In SNP, it's just going to be a true-false Boolean.
**Antonio Martinez (Cisco Systems, Inc.)** 13:21 I see your point, I see your point.
Yeah, I mean, for the people that are more familiar with OpenTelemetry than SNMP, I don't usually see attribute as a true-false. I mean, they could exist for sure.
But I don't usually see them. I mean, that information is not possible to access.
Easily, so it might not be possible for that. I might, for the promiss mode, we can for sure have it, but for the connector, it might be not possible, so I'm gonna add here a note.
Bang.
**Stephen Lang (Raintank, Inc. – Grafana Labs)** 13:59 For booleans, would you just have a metric value of 0 or 1?
**Antonio Martinez (Cisco Systems, Inc.)** 14:03 Correct. Not a metric value, remember, this is an attribute, not a metric.
**Stephen Lang (Raintank, Inc. – Grafana Labs)** 14:10 Right.
**Antonio Martinez (Cisco Systems, Inc.)** 14:12 But yeah, it will be zero one or true-false, yeah.
And it doesn't… I don't usually see them, I mean, for sure it's possible, following the spec, but yeah.
Let's discuss the one robber is here, he's the one proposing that.
And now, for the metrics, like, you guys are also quite familiar with regard to eBPF.
Emm… Bite is to not… I mean, the… the unit is not usually put in the… In the metric name, so… and there is already a semantic convention for Network input and output, let's say, or number of bytes transmitted and received.
So, I think we should use it, network.io, that's my proposal. Also, in that meeting, we agreed that we are not gonna follow anymore the system. That was, like, a quite legacy… a namespace that we are not gonna follow anymore, but for that, I would say, like, network.
interface.io could be one option, or network.io could be an even better one, because we could use it for other things that are not Super related with the interface.
like, more generic, but yeah. I don't know, you guys that have been touching similar code path for eBPF?
**Stephen Lang (Raintank, Inc. – Grafana Labs)** 15:41 Mario, you've probably done this most, haven't you, when you've been looking at, like, the, inter-zone bytes?
That kind of thing. I think… trying to think about use cases where we've done measuring of… You know, cheap versus expensive network throughput on, you know, multi-region, multi-zone deployments.
**Mario Macias** 16:01 Oh… yeah, the, the throw food?
And we, we… Yeah, we, we, we measure, we, we measure the… just the total bytes. Of course, you can infer the throughput from that. What was the question or the aspect you incomplete?
**Stephen Lang (Raintank, Inc. – Grafana Labs)** 16:23 Just if there would be anything more generic than an interface that you would be measuring I.O. for.
**Antonio Martinez (Cisco Systems, Inc.)** 16:30 I'm proposing, like, network.io or network.interface.io, but if we remove interface, that might be more generic, and we could use for other things with regard to network, not only network interface.
And there wasn't.
**Mario Macias** 16:42 Yes.
Yes, we… I will mention their interface. What we are… what we are measuring currently is as a generic.
throughput and the interface is an optional attribute, so you can report the attribute in case you want to… To… to differentiate by interface.
**Antonio Martinez (Cisco Systems, Inc.)** 17:06 Okay, so that makes totally random.
**Stephen Lang (Raintank, Inc. – Grafana Labs)** 17:09 But one thing I'm familiar with the bytes is that sometimes you see two separate metrics, one with bytes and one with packets.
So I don't know if, how you'd kind of consider that.
Here.
Because if you take off the units completely from the metric name.
What if, what if you need to represent both packets and bytes, or…
**Antonio Martinez (Cisco Systems, Inc.)** 17:34 And that's… and that's a reality, we need to represent both, because later there is another one called network.
barcades.
Here, I'm trying to follow the same approach, like HTTP server requests, or for messaging, there is also… let me see if I don't find it quickly. Here, we have also something called… send message.
So, here we could also use something like packets, network.packets, that was my proposal.
And then Robert was… proposing, like, unicast, I mean, network.interface unicast, multicast, broadcast.
we could encapsulate the three of them in a single one, like network.packets. That's my proposal list, and then unicast, multicast, and broadcast could be, like, as an attribute, how we are… which approach we are using to a stream, because, I mean, if not, we'll end up with 3 metric, which is not the best approach. And then, we also went from the direction for these cars.
EROS, protocol unknown, which is the same that this car, but based on that.
research, like, the protocol is unknown.
Here, I think we should also use network.packets, but now you guys might be more familiar than me, but here… yeah, use it?
**Giuseppe Ognibene (Coralogix)** 19:01 No, no, sorry, Antonio, continuous question for later.
**Antonio Martinez (Cisco Systems, Inc.)** 19:05 Okay.
**Giuseppe Ognibene (Coralogix)** 19:06 Hello?
**Antonio Martinez (Cisco Systems, Inc.)** 19:07 The comment here was, like, what about if we could use something like error.type attribute, and the error.type attribute, we could say of if that was this car, or if we know the reason of the error, for sure we could put the region of the error.
or if that was discarded because of the protocol unknown, that's the error type. So here, at the end, we could use also network.packets for those 3, like… Protocol, discount an error, the same that for the other.
Or the other one have erodottype, so which means that it will be as successful, and then you will have for sure the direction.
**Mario Macias** 19:42 process.
**Antonio Martinez (Cisco Systems, Inc.)** 19:43 Twice.
And then the last one that he's proposing is here. A queue.
Personally, I need a bit… reticent in the sense, like, is it really used? Like, is it really customer interesting on the queue of elements in an interface?
I don't know…
**Marc Netterfield** 20:05 for Networking.
**Antonio Martinez (Cisco Systems, Inc.)** 20:06 that you're It is, right?
**Marc Netterfield** 20:08 It's, it's like, it's a hardware constraint. You usually buy bigger routers and switches because they have bigger queues. You can be actually backed up.
**Antonio Martinez (Cisco Systems, Inc.)** 20:18 I see your point.
Okay, so here I was talking something like network.q.packets, because… to follow the same approach as packets, and then as it is part of the queue, but yeah, for that one, as you guys are more familiar, we could.
follow-up, but output for me was a little bit necessary. Yeah, go ahead.
**Stephen Lang (Raintank, Inc. – Grafana Labs)** 20:39 Do you need that as well as the errors? Because, like, in the case of network saturation, if you've already got the direction.
Do you need to know.
that the queue is full as well. Or is it more that you want to track?
the exact size of the queue over time. Is that useful?
**Marc Netterfield** 20:59 That's a good question, I'd have to think about it for a little bit, I'm actually trying to find what the OID on SNMP has in the definition so that we can know.
Like, what the existing metric looks like out of other gear.
**Stephen Lang (Raintank, Inc. – Grafana Labs)** 21:17 I'm just wondering if you would admit it, you know, independently as another metric, or if you would just use it as part of the exporter to decide what the, what the reason was for the error, for example. You could use it to differentiate.
You know, between saturation or something else.
**Antonio Martinez (Cisco Systems, Inc.)** 21:39 Share your point, yeah.
I think for that one, we have to see more, like, which one is the goal of that message, because the other is kind of makes sense, like, some sort of throughput at the end of the day.
But for that one, it's a little bit… Confusion for me.
Okay, hold yours in yesterday. Do you want to go ahead and message me?
**Giuseppe Ognibene (Coralogix)** 22:02 Yeah, so the first one is about the promiscuit, promiscuous mod. You were saying that it was, like, a Boolean. Not sure if it's a good, thing to, like, reuse the… our Linux is, You know, you can set the promiscuits mod with on-off, so instead of having true-false, maybe we can reuse it on for, on-off.
That's another idea, or also, you can set more than, one, like, the value can be greater than 1, but, in that case, the, like, the cardinality will, will explode the thing, so maybe on-off, it's, It's a good approach.
This was the, the first, the first note. The second one is about, the…
**Antonio Martinez (Cisco Systems, Inc.)** 22:57 Can we… can… can we… because my comment… my comment here was, like, what about if in the future we have other modes, or maybe today there is already those modes. My goal was something like network interface mode, and if it is promiscu, we add it, and if it is not, we… we could even have, like, not… I mean, we could have something else.
Or not mention.
Not attribute at all.
I don't know if… so we make it more generic for future modes. That was some sort of, like, comment there.
I don't know.
**Giuseppe Ognibene (Coralogix)** 23:28 But in that case, it would be, like, mod, and you can just write promiscuous.
**Antonio Martinez (Cisco Systems, Inc.)** 23:36 That will be on a string, that will be on a string, and then if there are more modes, perfect. If that's the only one, maybe makes sense for today.
**Giuseppe Ognibene (Coralogix)** 23:43 I don't know I mean, if…
**Marc Netterfield** 23:53 I'm trying to see if there are, like, other examples of modes that would exist.
**Antonio Martinez (Cisco Systems, Inc.)** 23:59 anywhere.
**Giuseppe Ognibene (Coralogix)** 24:00 So you want to have just one interface mod, and then add a list of strings for all the mods that exist for an interface.
**Antonio Martinez (Cisco Systems, Inc.)** 24:10 Correct, but as I was saying, I don't know if there are more modes.
**Giuseppe Ognibene (Coralogix)** 24:17 Yeah, there are a lot of more… oh, okay, Marc says later, yeah.
**Marc Netterfield** 24:20 Oh, yeah.
**Giuseppe Ognibene (Coralogix)** 24:26 So it is not a good idea to have, like, a network interface promiscuous, true, false, or on-off, and then one other networkinterface, dot… For another, mod?
Like, having different attributes with their own, various…
**Antonio Martinez (Cisco Systems, Inc.)** 24:49 I could say, like, if promiscuous is on, the mode will be promiscuous.
But, I don't know. First thing, I don't know if there are more modes, but… and if there are other modes, could they be at the same time, or there is only one at the same time? So we need to clarify those questions before we propose.
The mode, or not the mode, or… Okay, but…
**Giuseppe Ognibene (Coralogix)** 25:14 In that case, so if you write promiscuous, it means that it's on. It is… Correct.
**Antonio Martinez (Cisco Systems, Inc.)** 25:20 my proposal.
**Giuseppe Ognibene (Coralogix)** 25:21 Okay, but if you don't write it, it's off, which means, like, the absent of the value means that it's off.
**Antonio Martinez (Cisco Systems, Inc.)** 25:30 Or… or we can put an opt option, like, open up option. But yeah, but the first question is, like, are there more modes apart from promiscuits, or that's the only one?
**Giuseppe Ognibene (Coralogix)** 25:42 okay.
**Antonio Martinez (Cisco Systems, Inc.)** 25:48 Which we need to investigate it, I guess.
And if those modes could be at the same time, or only one could be at the same time, so I think we need to clarify that question. But in case there is only one mode, or they could be at the same time, promiscuous mode with off on makes sense to me, as it is following the… The actual interface approach.
I like idea.
I will take those notes.
**Stephen Lang (Raintank, Inc. – Grafana Labs)** 26:12 I suppose, I don't know, thinking about, Wi-Fi, you could have… An access point node.
or, like, client mode. Does that fall into the same kind of category?
I mean, but even then, you could have… Promiscuous and… Access point mode on at the same time.
I don't know if they both count… I mean, they're both modes, but are they the same kind of mode? I think this is what you're asking, right?
**Antonio Martinez (Cisco Systems, Inc.)** 26:42 Correct.
Okay, I think we need to follow up here, and we'll do some investigation.
What was the other comment you said, about the interface promotion?
**Giuseppe Ognibene (Coralogix)** 26:57 The… there was a metric… that was counting the bytes, and you wanted to remove the interface, I think.
Correct. What is his name?
I think that we can, Here, let me… 17.
Not this one.
So, the ones they run a loss to the issue.
Okay, this one.
I… Long time ago, I created this issue to create some network metrics, like TCP, RTT, and blah blah blah. And, there is a similar one, it's called the System Network I.O.
Which is existing, but, I remember I had some, some thought about it. It depends also on the place where you are counting the bytes. So if it's in the socket, if it's on the TCP send, and… Like, on the last part of the interface.
So… that's all. Just want to point out.
**Antonio Martinez (Cisco Systems, Inc.)** 28:17 Yeah, I think I mentioned that based on other meetings that we have in the network group, we decided that the system.network is a quite legacy namespace, and we will get rid of.
So, yeah.
**Giuseppe Ognibene (Coralogix)** 28:33 about…
**Antonio Martinez (Cisco Systems, Inc.)** 28:33 For me, that part makes totally sense, so now is what Mario was approving. Network.io, or network.interface.io, if we consider that sending or receiving bytes is only focusing on interface, those were the only… those were the two approaches that I was proposing.
But yeah, I agree that… system.network already exists, and I don't know if that's stable, or what did say. I mean, at least it is not as stable. It's in development. But, but yeah, the semantic commission team don't want to support anymore the system.network.
group.
**Giuseppe Ognibene (Coralogix)** 29:13 Okay.
**Antonio Martinez (Cisco Systems, Inc.)** 29:16 Okay.
More suggestion, question for the… Networking interface proposal.
Also, in the last meeting, I think you said that you were there. I couldn't make it. You were talking about network.peer.bep or network.bepppier. It was also a proposal from Robert, which is a bit if he's not here.
Comment there is, like, if… the VEP is not on the PR side, which means on the other side of the connection. It doesn't make any sense to have it on that way.
If it is on the other side always, for sure it makes sense on that way, but if it is not that approach, we should use BEP underscore peer. The reason why underscore is used is because… not here in general, is because when those two words cannot be splitted.
Because if not, they will have different… different meaning. So if you need to keep both together to… to keep the meaning as a single thing at the end of the day, is where it should be used.
So I would say, like, from what I was… I watched the recording from… for Robert B.P. They have a… A specific meaning on the routing network logic.
So I think we should be more into that direction, rather than into peer.bgp.
Because if not, that is gonna be quite… confusing with network.peer that already exists.
It's my take here.
Nice. Beautiful.
**Marc Netterfield** 30:57 I was thinking about that one, too. I felt like if we just wrote out an example both ways, it would be kind of obvious which way would feel more correct.
**Antonio Martinez (Cisco Systems, Inc.)** 31:11 Roop.
So, those were some sort of my comments. I will follow up with Brandon there, and try to follow up on the feedback with Robert.
Yep.
I don't know, guys, if you want to discuss today something else.
**Giuseppe Ognibene (Coralogix)** 31:30 Not too much.
**Marc Netterfield** 31:31 link for this, this document that you're working with?
**Antonio Martinez (Cisco Systems, Inc.)** 31:34 I don't wanna remove.
I'll put it in the chat.
**Marc Netterfield** 31:40 Thank you.
**Antonio Martinez (Cisco Systems, Inc.)** 31:51 Good, so if there are no more, info, I will… continue those two conversations in the GitHub, sorry, on the Slack page from the Networking team, so you can also provide your input there, in case you're interested.
**Stephen Lang (Raintank, Inc. – Grafana Labs)** 32:04 Thanks, Antonio.
**Giuseppe Ognibene (Coralogix)** 32:06 Thank you.
**Antonio Martinez (Cisco Systems, Inc.)** 32:08 Father Will, see your waist.
**Giuseppe Ognibene (Coralogix)** 32:10 See you. Bye-bye.
