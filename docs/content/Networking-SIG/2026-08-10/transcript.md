SIG: Networking SIG
Date: 2026-08-10
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Marc Netterfield** 01:06 Hey, Matthew, I'm not sure if you know, there's another link that they might be meeting on, so if we don't see a bunch of people join in the next 5 minutes, we'll… I'll share the other link.
**Matthieu Noirbusson (Sensor Factory)** 01:16 Okay.
**Marc Netterfield** 01:21 Maybe. Maybe we're all on the same wind today.
**Sven Cowart (ElastiFlow Inc)** 04:28 Can you guys hear me?
I realized my microphone was muted.
Externally.
**Stephen Lang (Raintank, Inc. – Grafana Labs)** 04:34 I can hear you now.
**Sven Cowart (ElastiFlow Inc)** 04:36 Good morning.
**Antonio Martinez (Cisco Systems, Inc.)** 04:39 Hey everyone, sir, I was just starting with the… the new Zoom meeting.
**Sven Cowart (ElastiFlow Inc)** 04:44 Saw you typing.
I'd share my screen. Well… Let's see… what do we have?
Antonio, do you want to take it, since you put your first few things on the agenda?
**Antonio Martinez (Cisco Systems, Inc.)** 05:17 Absalom, let me read the screen, sorry.
Okay, so from my side, first thing, let's go to that item. Great job on the pull request merch on the group. I don't know if there are any action items, or what's the next step. I was actually just looking into, Let's see, there is already, like, a network group.
**Sven Cowart (ElastiFlow Inc)** 05:49 Yup.
Yeah, so we need… there is an action item to update this.
That I have, and also their… My next steps are to… I have to get myself added as a member to actually OpenTelemetry, organization, and… And then once I do that, I can create the project board to start tracking the work officially.
I was on… I was, on PTO last week, so… didn't get it done then. But that's my… My plan of action for this week to move things forward is to, get the project board up, and then to, organize some of this work in here, but I first have to go through the hoops of actually being added as a member, otherwise I can't do that.
**Antonio Martinez (Cisco Systems, Inc.)** 06:44 Absolutely.
Okay, I wanted to understand, I don't know, guys, if you have context about it, but what's really that OpenTelemnity Network repo?
Alpha Collecto… Yes, sir.
beneath.
**Sven Cowart (ElastiFlow Inc)** 07:08 That's a good question. I don't have too much context about this. This is, far before.
I got involved.
And the effort.
**Antonio Martinez (Cisco Systems, Inc.)** 07:18 Nope.
I think Giuseppe from OVI is here. Do… have you heard anything about that OpenTelemetry BPF?
Focusing on network, most likely.
**Sven Cowart (ElastiFlow Inc)** 07:30 Yeah. This is not Obi. Obi is, an OB.
**Antonio Martinez (Cisco Systems, Inc.)** 07:33 Very rare.
**Sven Cowart (ElastiFlow Inc)** 07:34 People, yeah.
**Antonio Martinez (Cisco Systems, Inc.)** 07:35 Right, right, I understand that.
**Giuseppe Ognibene (Coralogix)** 07:37 I heard of it, I am searching, because there was a question about it on Obi's Slack channel. I think, as far as I remember, it's like a dead project.
**Sven Cowart (ElastiFlow Inc)** 07:48 Yeah.
**Giuseppe Ognibene (Coralogix)** 07:49 There were some, something similar related to Obi, but I'm not sure. Let me, let me search this, this reply.
**Sven Cowart (ElastiFlow Inc)** 08:00 Last I heard from it was that it's been dead for about 2-3 years now.
**Giuseppe Ognibene (Coralogix)** 08:05 Yep.
Okay.
**Sven Cowart (ElastiFlow Inc)** 08:07 more or less OB.
Is intended and designed to replace this.
**Giuseppe Ognibene (Coralogix)** 08:14 Okay, I found it.
Where is Zoom?
This one.
Zero, it was only for network-level metrics.
**Antonio Martinez (Cisco Systems, Inc.)** 08:39 Basically.
Oops, so… We will need to… to take an action, I mean, most likely from our side also, right? We might need to mark it as segregated.
Probably, because if no one is…
**Sven Cowart (ElastiFlow Inc)** 09:05 Yeah.
**Antonio Martinez (Cisco Systems, Inc.)** 09:09 And most likely, I don't know if every… every group have, like, a repository, but maybe our repository can point to the… Oh, to the semantic convention, if that makes sense to you guys.
**Sven Cowart (ElastiFlow Inc)** 09:20 Yeah, so we'll… we'll have a, The plan is to open an open telemetry What is the name of it?
OpenTelemetry Network SEMCOM.
repo?
that looks… or structurally is similar and the same to the GenAI one, because we want to do the, capture all the federated semantic conventions inside of it.
**Antonio Martinez (Cisco Systems, Inc.)** 09:48 Okay, so, but I think Trix other, like, the system, is on the semantic convention from Autel.
Right. So, the main reason why moving it out is anything particular, or… He's… System, for example, is here.
**Sven Cowart (ElastiFlow Inc)** 10:09 Yup.
So we'll still have our network one there.
And the main reason is because once we get into adding semantic conventions for Let me back up and explain the whole breadth of it. So what we'll have is we'll have some ending conventions that live in both this repo, that are considered core, and then some ending conventions that are non-core, that are very networking focus and specific, which could include things like vendor-specific attributes and MIBs and so on and so forth. So, when we get into the… especially, I think, when we get into the SNMP world.
we might have hundreds and thousands of SMANDI conventions, and the Semandi Conventions group asked, we don't really want you to blow up our entire project with that many conventions, so… we'll do a federated semantic convention repo, for that part of work. So part of what we need to do, and I've already started on this, Last week, I just didn't get done, because I only worked Monday.
Is identifying what would be core and what would be in the federated repo, and… And then… and then go from there.
More or less, right now, all the stuff that is there today.
source destination, and everything that's in network namespace and in the DNS namespace will be considered core, right? I'm thinking of core things that are shared and, useful for Many levels of… many different forms of instrumentation, not just Oh, this is for SNMP only.
type of thing, right? So, like, source and destination IPs.
Are useful in a number of different ways for a lot of different folks who want to, instrument various Things.
And so, to that degree, like, we'll have… I know Rob is working on the… In that exact spot that you just showed, adding an entities.yaml.
file for networking that scope for the networking pieces, and Man, so we will be working in there, though, as well.
Does that make sense?
**Antonio Martinez (Cisco Systems, Inc.)** 12:43 Remember, me too, yeah.
Okay, with regard to the project, we are kind of on agreement about the next step. I also put that action item. We had that conversation about using source and destination, but we didn't create a ticket. I know when that you created that ticket, I think I put it here.
And it's one of the ocean.
Yeah, you created here, that source and destination, ticket also, but if I'm not mistaken, this is more like a generic one for… for attribute in… inside of OpenTelematy, right?
**Sven Cowart (ElastiFlow Inc)** 13:29 Yes, more or less. There's some guidance Already for client server, around if you need to use that as a prefix to dictate direction, you can do that. This is basically asking to open that up, that we can also have source and destination.
something, like source and destination, kubernetes.pod name, so that on a flow.
if you have flow metrics or flow traces, you can denote the side, like, which pod is on each side of that… that connection conversation happening. So that's what… that's what I'm… that's what that's about.
**Antonio Martinez (Cisco Systems, Inc.)** 14:12 Okay, so I think my GitHubSpace is more like a follow-up on your ticket for network. We might need to do it for Froometics later, but here today we have, as you're familiar, local, PR Address import, and then the suggestion is, like, we… We create the following new attribute, which is network source address, source port, and the same for our destination, and so in the future, we can extend those for prefix, yes, and number, reverse DNS, and APV4, APV6, they are kind of pending on that.
**Sven Cowart (ElastiFlow Inc)** 14:55 Hmm… Sorry, let me… Can we just use, do we need to say network.source and network.destination?
**Antonio Martinez (Cisco Systems, Inc.)** 15:27 That was also a comment, I mean, thinking that they had, because the source and destination already exists, but they are not that network-focused. They are more like… Or… mmm… how do you call it? For more of, like, a client request HTTP, for example, they are not in that network detail. I think Ted explained here, or Shory Trust.
Network is more for the physical layer, while client servers, source, and destination are more a local layer.
So, we can think about it, as you just said, but… if we want to extend it for adding other things, like ESN number, or… APV4, APV6, or… Yeah, well, prefix, that might don't fall under the logical direction, more like the network one.
**Sven Cowart (ElastiFlow Inc)** 16:26 I would like to take… let's… let's do a follow… we… we can both do it. I'm for sure, attending the Semantic Convention's call, and I will, double-check that with them. That is a rather old comment.
Because it is made, it was made a year ago. So I just want to make sure that's still how they feel, because… Otherwise, I'm confused why we would take over the source and destination namespace.
If it was not intended to be about the physical layer. But I get what he's saying here, it just… I want to make sure that we're consistent. Also, I'm concerned that if we do network.source.endestination and have source and destination, it would become very confusing quickly which one someone should use.
**Antonio Martinez (Cisco Systems, Inc.)** 17:10 fun.
**Sven Cowart (ElastiFlow Inc)** 17:11 It would also make it really hard from the actual People that need to, Store and visualize this data, like the actual downstream, observability platforms, because, like, now there is… numerous places that you could put source and destination IPs.
I don't think that's a good idea. I don't think it's a good idea to say that. There's some guidance somewhere, Let me see if I can find it really quickly.
**Antonio Martinez (Cisco Systems, Inc.)** 17:47 I also find if that source, the source and destination namespace, let's say, it's gonna be for network focus, I'm totally fine, also extending it. I didn't take that action just because I read that comment from Tras.
**Sven Cowart (ElastiFlow Inc)** 18:02 Yeah, I think we need to clarify, no matter what. There… cause there is… I might need to send it after the fact.
Because it is in a weird place. And I have a hard time finding it every time, but there's actual guidance on when to… Use… I think it might be here.
I… I got right here. So, let me… I'll send it, and you can open it.
Nope.
Why did that work?
Right? And just in the definition of this, what is written here, that's why I always assumed, okay, they're talking about Like, to me, when I read this, this reads as, okay, it's… this is describing This, to me, reads as if it is in odds with what Brass said in that other comment.
**Antonio Martinez (Cisco Systems, Inc.)** 19:51 True.
**Sven Cowart (ElastiFlow Inc)** 19:52 So let's just get clarification on that, because that's pretty important for us to know, because if it is, like, intended to Only be used by To, observe applications.
At a higher level than the physical layer, then… That should be called out here, at the very minimum, and then I don't know if we should actually be owning that namespace or not.
We could, but we should bring all these things up, so I can do that in the next call, right after this one.
**Antonio Martinez (Cisco Systems, Inc.)** 20:26 Yeah, makes a decision. Honestly, we need to clarify that.
**Sven Cowart (ElastiFlow Inc)** 20:39 Okay, great. Oh, Steven, sweet.
Did you get anything about the UN64?
**Stephen Lang (Raintank, Inc. – Grafana Labs)** 20:50 Yeah, so this was from, the conversation last week.
Yep. To the support of full-range unsigned 64-bit ints.
And so I spoke to a few different, sort of SIGs and groups and raised the same question in a few different calls to try and get an idea as to, you know, the scope of support for UNT64.
And I think the current situation is that, unanimously, unsigned full-range 64-bit ints are not currently supported anywhere in the stack.
So that means it's not in the spec.
Neither of the… OTLP or OTAP protocols support it.
And the one backend that I investigated, Prometheus, also does not support it.
That being said, nobody said.
That it's an all-out no forever.
There was definitely support for bringing this in, if needed.
the… people wanted some more clarification as to the exact use cases, but interestingly, on the OTEL Arrow SIG, which is mostly Microsoft and F5 NGINX, they said that this isn't the first time that somebody has brought this up.
So I think that, you know, definitely this could be useful to introduce a new type, but… It's a significant undertaking, because it would need to be implemented at every point in the stack by multiple vendors.
**Antonio Martinez (Cisco Systems, Inc.)** 22:21 And today.
**Stephen Lang (Raintank, Inc. – Grafana Labs)** 22:21 projects.
Including, sort of, on the spec, all the way through the protocol.
you know, through the, you know, the SDKs, the clients, and the backends.
So, as far as I could tell, the lowest… common denominator that I could see at the moment.
was that the Prometheus backend Supports, stores all numbers as a float 64.
So, this… It gives us sort of a greater range than a 32-bit unsigned int, but it doesn't give us the full range of a 64-bit unsigned int.
So I think the next steps are gonna be, like, whether It is absolutely imperative that we require the full range of the unsigned 64-bit int.
Because if that's the case, we're looking at Prometheus said.
The last type to be added to the codebase was the native histogram, and that took about 5 years.
It would certainly not take as long for younger projects like Hotel Arrow. I think they would be able to implement this quite quickly.
But then, you know, we have… I know the spec… People who are familiar with the specs said that it would be, you know, definitely a discussion that we could open.
But like I said, I think it would be a significant undertaking, and it would need to be… Maybe a project in its… in its own right.
But there's some alternatives that we could consider, and that is whether we do really need the raw data stored, as an unsigned 64, or if there's other things that we could do, for example.
Is it okay if we reduce You know, the accuracy. Can we… can we chop off some bytes?
Is Float64 enough?
Or maybe we don't store, you know, the raw Counter, maybe we store… Maybe we store a rate instead, with a fixed window.
Or, you know, like a delta or something that would be, like, a fundamentally smaller value.
So it's an open question, it's just that the answer is currently no.
Uin64 is certainly not supported anywhere in the stack. It potentially could be in the future.
It could be a multi-year effort. Everybody's open to it.
Or, you know, the alternatives are… Can we, you know.
Reduce the, the range of the numbers that we're working with.
Or, you know, either by… Just chopping off some bytes.
And just dealing with that, or, you know.
And we present the data in a different way, using a Delta Aurora.
a rates calculation of some kind. So that's, that's where the conversations went.
**Sven Cowart (ElastiFlow Inc)** 25:05 Okay That's useful. Good to hear that people are at least open to it.
I… I know the use cases are going to come up when we get into S&P world. That's where it's going to be the most needed.
However, that being said, I do think it's a good question to… to ask when… We get there.
Is there another way to represent it by doing something like deltas?
But I know, like, I know there's a common example, like, certain counters, for example, that you'd get from SNMP data would flip inside of an hour.
all the time. Actually, there's some that would flip inside of, probably less than a minute if you don't have U64, which makes the… the value pretty much useless.
That being said, if we can do some type of Delta or some type of other representation of it? Do we really need it? Like, it only would be necessary if we're just passing on the raw value. That's where my, expertise around the use case, around SNMP data, we need… that somewhat ends, and we need to lean on Rob to… to kind of guide us around that, and show us what those examples are.
I do find the Prometheus one is, is a little bit interesting.
it always has bothered me that Prometheus doesn't support U64, but I know it's not getting added, so I… I wonder how… in this situation.
when… let's say we do move forward, and it does get accepted, and we're a year or two down the road, and we now have… OpenTelemetry has U64 support, Would Prometheus just… I mean, I don't even know if Prometheus would move forward on adding that support themselves, or how does that work for them, or they would just have to do stuff on their end when exporting to Prometheus to handle certain values a different way.
**Stephen Lang (Raintank, Inc. – Grafana Labs)** 27:21 Well, so Prometheus has an OTLP endpoint at the moment, which has to be sort of compliant with the spec, right? So I would imagine if a new type was introduced into the spec, then, you know, in order for Prometheus to stay relevant.
somebody would have to add in, you know, support for the new type, whether that would just organically happen from, like, the current Prometheus maintainers, or, you know, maybe someone that was interested could, could contribute. But I would imagine that, Prometheus would kind of closely follow the, the hotel spec.
Particularly around OTLP. Not so sure about OTAP, I think that would have to be, sort of, treated independently.
And I think this… this is why, if you did want to kind of approach this and, you know, make sure that UINT64 was available, we'd have to go probably spec first.
And then approach it from, you know, not only the both OTRP and OTAP protocols.
But also to ensure that, you know, the actual implementation, the exporters, the SDKs can support it as well.
And then it's going to be up to the individual backends to, to follow suit.
**Sven Cowart (ElastiFlow Inc)** 28:27 Okay.
I'm not sure that… This might sound weird, but I'm not sure that… I think it would be an incredibly non-trivial change for Prometheus, wire protocol and storage protocols to support that effort.
**Stephen Lang (Raintank, Inc. – Grafana Labs)** 28:43 Yeah, I think that the trouble is in the TSDB with their fundamentally… like, the way that they store the samples, is kind of all built around Float64 right now, so yeah, I think you're right that it would be sort of non-trivial.
And probably, I don't know.
you can imagine the first implementation would just be to cast the number to a float64, right, which is what I think They do with everything else.
But yeah, so to get the full, like, end-to-end implementation.
like I said, the last type that they added, they quoted 5 years.
**Sven Cowart (ElastiFlow Inc)** 29:17 Right.
**Stephen Lang (Raintank, Inc. – Grafana Labs)** 29:19 It's not necessarily a reason not to do it, it's just, you know… If we're going to do it, we need to be absolutely sure, and, you know, it should be justified, and we should look at this from a sort of spec-first point of view.
But then also, you know.
it's… is the raw number really needed? I think is probably the first justification to be had, and that's something maybe we involve Rob a bit more in terms of whether we should actually Sort of open this conversation further or not.
**Sven Cowart (ElastiFlow Inc)** 29:50 Yeah, I… I think, there's an… I'll take an action item to… sync with Rob on it, and catch him up on what you just shared here, and But it seems to me that It's probably worth, no matter what, to… Open an issue with it inside the spec.
repo.
And describing the need for it, highlighting the exact use cases, and to kick that conversation off.
So at least, like, that… No matter the decision that gets made, there's a paper trail.
At some point or another, right, for the community into the future, that… Everyone understands yes or no, this is why we did it and why we didn't do it.
Yep.
So I think that's the best starting point, and let's just have that conversation within the SPEC group.
**Stephen Lang (Raintank, Inc. – Grafana Labs)** 30:42 Yeah, that would be great if you could, sort of, take that, and, like, especially around the specific use cases is what I couldn't really provide. I kind of gave the generic example that we needed, you know, high-range counters that would likely flip with anything less than you went 64, sort of relatively quickly.
But giving, you know, specific and explicit use cases as to when that might be the case, and… I don't know, an order of magnitude of metric values that might be involved. You know, is this just… one value. Is this an edge case?
Or actually, you know, are there… several metric values that we would consider that this would be applicable to, because probably a spec change isn't necessary for a single value, right?
**Sven Cowart (ElastiFlow Inc)** 31:29 Yeah.
**Stephen Lang (Raintank, Inc. – Grafana Labs)** 31:30 There's, like, tens of, I'd say at least tens, and then it's gonna be… Yeah. And then also, if you get an issue created, I can sort of share that with, Hotel Arrow, and then if they want to add in where this might have been mentioned previously, maybe it's the same use case, maybe there's different use cases.
Because I'd imagine adding this type wouldn't be applicable to just network, you know, it's probably applicable elsewhere as well.
**Sven Cowart (ElastiFlow Inc)** 31:57 Makes sense.
**Antonio Martinez (Cisco Systems, Inc.)** 32:00 Can I… can I ask something? You mentioned, Stefan, that Prometheus and the specs support float 64.
Can we use Flat64 for that use case?
**Stephen Lang (Raintank, Inc. – Grafana Labs)** 32:12 So that, that's something that I think, Like, if we can be more explicit with the use cases.
And… answer the question as to whether we need the full range UINT64 in the metric value.
But there's two alternatives. One is to store A, a lower accuracy value, or maybe we don't reach the full range.
Because Float64, I think, gives you… Something like 2 to the 53.
Instead of 2.
**Antonio Martinez (Cisco Systems, Inc.)** 32:40 terrific.
**Stephen Lang (Raintank, Inc. – Grafana Labs)** 32:41 64. So, is 2 to the 53 enough?
Because if it is, then great, there's no problem, we can just use Float64.
But if you need more than 2 to the 53, then.
Again, do we really need the raw number, or could we calculate the rate over a 10-second window, or the rate over a 30-second window?
And instead of storing the raw value, we just store the rate.
Because the rate is… Much likely to be less, even if a counter is flipping.
You know, every hour or every 30 minutes, the rate of change of that number is going to be far less than storing the raw number itself.
So we could, you know, actually build into the conventions And, you know, this metric that we would be creating, we would build in from the start that it would be a rate value.
Not a raw counter value.
Because maybe the use case.
It's… it's okay, as long as we know the rate.
You know, maybe we just don't care about counter resets, or… You know, maybe we don't need the full original value.
**Antonio Martinez (Cisco Systems, Inc.)** 33:50 Filipino, thank you.
**Stephen Lang (Raintank, Inc. – Grafana Labs)** 33:52 Yeah, you're right. It's, It's validating if we do need to go down this route and introduce a new type, it should be intentional, and it should be that, you know, it's required that we need the raw value all the time.
Which I do think is questionable, because if we know that even the 64-bit unsigned-in is eventually going to flip, then that's got to deal with resets.
And… You know, maybe it's okay that we… we just store a rate value.
Yeah, we can discuss it further, maybe, on the issue.
**Antonio Martinez (Cisco Systems, Inc.)** 34:28 Do you take the action right into that?
**Sven Cowart (ElastiFlow Inc)** 34:30 Yeah.
**Antonio Martinez (Cisco Systems, Inc.)** 34:31 Is one of the spec?
Yeah. Oh, yes.
**Sven Cowart (ElastiFlow Inc)** 34:34 I wrote it down.
I'm not gonna own that, because I'm not the right person, but I'll get Rob to be on that.
**Stephen Lang (Raintank, Inc. – Grafana Labs)** 34:41 I'm happy to contribute wherever's necessary as well, it's just the use cases I'm not too familiar with.
**Sven Cowart (ElastiFlow Inc)** 34:48 That makes sense.
Steven, you're, you're in the, you're in the spec… you're actually in the spec, SIG.
Awesome.
**Stephen Lang (Raintank, Inc. – Grafana Labs)** 34:58 No, it's, there's a couple people that work at Grafana. It was an internal call, so I can, I see. I can ping down more, I don't know if there's a spec SIG, we could join it together or something.
**Sven Cowart (ElastiFlow Inc)** 35:10 Yeah. I think somebody is in this group, maybe it was Braden.
That was in that regularly.
**Antonio Martinez (Cisco Systems, Inc.)** 35:17 I'll hurry up.
**Stephen Lang (Raintank, Inc. – Grafana Labs)** 35:19 Yeah, I think it was, Jack Berg that was the person that I spoke to.
**Sven Cowart (ElastiFlow Inc)** 35:23 Okay.
**Stephen Lang (Raintank, Inc. – Grafana Labs)** 35:27 About the spec.
**Sven Cowart (ElastiFlow Inc)** 35:32 Okay, we have one more question.
So, I think the answer for that is… It goes back to the definition and how we need to think about splitting up where things go.
If the entity describes something that is… universally usable.
across various layers of the OSI stack, then I think it goes into the core.
the, the core repo.
I'm actually… so, just so you guys know, I'm in the middle of writing a blog about the network SIG for the OpenTelemetry blog, describing why we wanted to start this up, and in that, I'm going to detail out, like, okay, there's been a big gap inside of the the OSI model for OpenTelemetry, specifically within Layer 3 and Layer 4. This is why we're doing it, and then I'm going to describe some of these things about, this is what we consider core, this is what we consider not core.
and, so it's really clear for everyone to understand and see.
And to just get more eyes and attention onto the SIG, too, so I think that'll be helpful. So… but, for example, like a… like a network interface is one entity that we know we need to create. That's going to be core, because network interfaces can… there's various things that could be instrumenting something about a network interface across various levels of the OSI model.
that… then I'm not… at this time, I'm not too sure exactly what those non-core network entities would look like.
I think we need to just cross that bridge when we get there, but to me, it's… it would be things that could be, Vendor-specific or in the weeds of… The physical networking world.
I'm not… again, I'm not sure what those would be right now.
I think most of the things that we've talked about so far would just be part of CORE.
**Antonio Martinez (Cisco Systems, Inc.)** 37:59 Hi, man.
**Sven Cowart (ElastiFlow Inc)** 38:06 Somebody's saying something? They're cutting in and out, if they are.
**Antonio Martinez (Cisco Systems, Inc.)** 38:10 Matthieu, did that answer your question?
**Sven Cowart (ElastiFlow Inc)** 38:36 I think that was a yes, I'm not sure.
**Stephen Lang (Raintank, Inc. – Grafana Labs)** 38:39 Dealers.
**Antonio Martinez (Cisco Systems, Inc.)** 38:40 There's no…
**Stephen Lang (Raintank, Inc. – Grafana Labs)** 38:40 coming through.
Clearly for me.
**Antonio Martinez (Cisco Systems, Inc.)** 38:45 Any other comments from anyone that wants to bring something?
**Sven Cowart (ElastiFlow Inc)** 38:55 No, I'll be a lot more active this week. Sorry again, I was off last week, just Monday. I actually just showed up for this call, and then I took off. So, I'm hoping to get things moved a lot further, and more organized.
I have, right now, work in progress where I've listed out all the attributes inside of a single document that we would own, that we can work on and iterate together first, and to make sure that we understand okay, this is gonna be core, this is the things that need attention. I kind of needed something to visualize, because everything's all over the place right now, and I needed something to look at to actually organize it and make sense of the information that we need to sort through.
But I'm hoping by the end of this week, we'll be in a much better place from a project management standpoint, because right now it feels… A little bit like spinning wheels.
**Antonio Martinez (Cisco Systems, Inc.)** 39:54 Yeah, looking forward to seeing that.
**Sven Cowart (ElastiFlow Inc)** 39:57 Alright. Awesome. Thanks for everything.
**Antonio Martinez (Cisco Systems, Inc.)** 40:02 What's up next week?
**Sven Cowart (ElastiFlow Inc)** 40:03 Yep.
Have a good day, bye.
**Antonio Martinez (Cisco Systems, Inc.)** 40:06 Dude.
**Stephen Lang (Raintank, Inc. – Grafana Labs)** 40:06 Bye.
