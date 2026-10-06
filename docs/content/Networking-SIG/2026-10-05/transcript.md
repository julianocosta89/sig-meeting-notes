SIG: Networking SIG
Date: 2026-10-05
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Giuseppe Ognibene (Coralogix)** 01:16 Hi, everyone.
**Marc Netterfield** 01:24 Hello, hello!
**Sven Cowart (ElastiFlow Inc)** 01:28 Hello.
All right, I'd say let's get started, but looking at the, talking points today.
Seems they all belong to Antonio.
So let's wait.
For the time to be here.
**Braydon Kains (Google LLC)** 02:22 I'm not sure if he's, at the EU Observability Summit.
Oh, no.
**Sven Cowart (ElastiFlow Inc)** 02:29 Nice Firebird.
**Braydon Kains (Google LLC)** 02:32 The Studio 2016.
**Sven Cowart (ElastiFlow Inc)** 02:35 Oh, nice.
Hey, Antonio.
You have all the talking points, so I'll let you take it away.
**Antonio Martinez (Cisco Systems, Inc.)** 02:50 Could you repeat, sorry, I mean?
**Sven Cowart (ElastiFlow Inc)** 02:51 Oh, you have all the talking points, so you can take it away.
**Antonio Martinez (Cisco Systems, Inc.)** 02:56 Absolutely, why not, yeah, let me say it.
**Sven Cowart (ElastiFlow Inc)** 03:00 You've been great to see.
**Antonio Martinez (Cisco Systems, Inc.)** 03:03 Indeed, yeah. Okay, so from my perspective, let's open it up. I would like to know if we have any updates from the security Team on that one.
I think we're just waiting for them because Brandon approved from the assistant team.
**Sven Cowart (ElastiFlow Inc)** 03:22 Yeah.
**Antonio Martinez (Cisco Systems, Inc.)** 03:24 Let me know if there is any way how we can post there somehow.
**Sven Cowart (ElastiFlow Inc)** 03:29 I already messaged them on Slack, I can attend their SIG.
this week, and hope for that. I gotta just make sure it doesn't conflict with anything else I have.
going on, but otherwise, Ludmilla did take a look, because I sent it to her specifically to try to… Get…
**Antonio Martinez (Cisco Systems, Inc.)** 03:46 Yep.
**Sven Cowart (ElastiFlow Inc)** 03:48 Get a little… maybe… maybe make that… get progress through… through her.
So… Nonetheless, I have to go through, this just came in yesterday, so I was going to sleep yesterday, so I need to go through and update things here.
**Antonio Martinez (Cisco Systems, Inc.)** 04:05 Awesome. I'm sure it will be soon sorted out.
I think… Yeah, go ahead.
**Sven Cowart (ElastiFlow Inc)** 04:11 I think attending the SIG is the only option.
Blessings.
**Antonio Martinez (Cisco Systems, Inc.)** 04:15 Maybe we can just drop on their SIG on their agenda.
If you cannot make it, or…
**Sven Cowart (ElastiFlow Inc)** 04:21 Oh, yeah, okay, yeah, I can do that too.
**Antonio Martinez (Cisco Systems, Inc.)** 04:26 Okay, so… Okay, that's really cool.
you The eBPF team, it's good that we have here Giuseppe, the BPF team created that ticket about the DNS lookup duration. It's.
metric that we already have in the DNS one, and they are asking if we can move the DNS question name as an opt attribute instead of being required. That is quite a line. I was looking, it is quite a line, the same with the request duration for HTTP, if you think about it.
HTTP. Here, under HTTP, they're saying the user… sorry, the server address is, is optional.
where it is server other is optional. So I think for Dns, if I go quickly under Dns.
metrics… Right now, we are putting as required the DNS question name, so it kind of makes sense. The reason why they are saying it's because they don't have the data is because it's bringing a cardinality issue.
Let me see where they are mentioning… yeah, bondless cardinality, it would be proposed to convert it to optional, is that required? They even created a pull request anymore.
Which, as I was saying.
Makes sense to me, so yeah, prove it. And they have, some small changes requested, but yeah. I don't know your opinion before we also… Progress.
**Sven Cowart (ElastiFlow Inc)** 06:00 Can you go back to metrics?
Can you go back to the metric page?
**Antonio Martinez (Cisco Systems, Inc.)** 06:07 Absolutely.
**Braydon Kains (Google LLC)** 06:14 Is this supposed to be against a resource that would help you know?
What it's attached to? Just without the… the… Question… I mean, even the question name doesn't necessarily identify it, so I assume it's supposed to be against some resource.
So that you can know what… what we're even talking about.
**Sven Cowart (ElastiFlow Inc)** 06:36 Yeah, that was… that's exactly where my head went, Brandon. I don't actually know what this is to provide a good answer.
**Antonio Martinez (Cisco Systems, Inc.)** 06:45 But if you think about it for a second, like, DNS.
lookup duration is what is performing, I don't know if it is described here. Measure the time taken to perform a DNS lookup. For the DNS lookup, the only thing that you have is gonna be, like, the… the IP, and then you're gonna have… in which is gonna be converted the question name.
The name being queried.
Which is kind of similar, as I was mentioning, from my perspective, like an HTTP, you're doing a request to something, and then you… this is the something, like the server, others, and port, and here they are optional. In my mind, they are optional, because they don't want to break cardinality amongst others.
**Sven Cowart (ElastiFlow Inc)** 07:35 I think I have a hard time.
I have a hard time knowing where the community should land on this.
Because for me, the cardinality problem is an issue of what database you're using.
And if your database can't support high cardinality, well then.
That's on… The fault of the system, not on the spec.
**Antonio Martinez (Cisco Systems, Inc.)** 08:06 But that is…
**Braydon Kains (Google LLC)** 08:08 That is true, but we also try to design around the fact that most people are gonna be writing this to Prometheus, which is the… Prime suspect of not handling my criminality.
So that's… I think that's where the opt-in part of this comes in. From that perspective, I understand.
I also think… Something like… duration histogram that would contain any DNS you're looking up would be… Mmm.
potentially not useful? Like, what if there's specific Like…
**Antonio Martinez (Cisco Systems, Inc.)** 08:43 Yeah, that's.
**Braydon Kains (Google LLC)** 08:44 names you're looking up that are way worse, you're going to throw off your whole histogram, but you're not going to know why.
I don't know if that's enough of a reason to say it needs to be required, though.
**Antonio Martinez (Cisco Systems, Inc.)** 09:01 conversation, I don't know if it was here or in the issue, that they somewhat initiate that conversation, so, like, is it already… and useful if we remove that attribute. And the reason… the comment here was, like.
Okay, but if you look into a time period, like, DNS is going up regardless of the… what you are querying, it means that there must be a problem, or your DNS system is misbehaving, or there is a lot of error types being exposed, means that you have an error.
It's also kind of important.
Based on all your DNS, not based on a DNS lookup on a specific direction.
**Braydon Kains (Google LLC)** 09:43 I guess you could figure out that something's wrong with your DNS lookup system and you wouldn't.
Be able to tell.
Why? Also, isn't error.type also boundless if we're talking about boundless cardinality?
**Antonio Martinez (Cisco Systems, Inc.)** 09:57 It's gone.
It's… I mean, I don't think so, because the… There is no a list of values that we support today, it's more like free free form today, I would say. Yeah.
But I don't think that will break any cardinality.
Based on the kind of error that we can have.
**Braydon Kains (Google LLC)** 10:22 Well, I'm more… I'm more talking about, like.
Theoretically, I guess, because if… Yeah, I know what you mean.
**Sven Cowart (ElastiFlow Inc)** 10:31 It is… it is boundless, but the odds of it happening are probably significantly smaller than.
**Braydon Kains (Google LLC)** 10:36 Yeah.
**Sven Cowart (ElastiFlow Inc)** 10:37 And that's where I…
**Braydon Kains (Google LLC)** 10:38 is.
**Sven Cowart (ElastiFlow Inc)** 10:39 Coming to the the previous point, and I I mean, I get that a lot of people use Prometheus.
But I even find, like, in that HTTP semantic convention that you shared.
Without… Server address, that metric.
is basically useless.
**Antonio Martinez (Cisco Systems, Inc.)** 11:01 I don't. I mean for sure, when you're debugging, you need more info. But as far as you have also the the duration, because what you're interested in knowing the duration of your service, the request That are coming to your service, so you want to know the duration, or if there are any kind of error.
Wait, you just want to qualify?
**Sven Cowart (ElastiFlow Inc)** 11:19 You couldn't identify the actual service that it's going to because your server address is nothing.
So that would, like… If you're observing a large system with tons of servers, you'd just be aggregating HTTP server duration across all servers in your…
**Antonio Martinez (Cisco Systems, Inc.)** 11:37 Main.
**Sven Cowart (ElastiFlow Inc)** 11:38 It just feels very strange to make that opt-in because of a cardinality problem.
And, and specifically because that cardinality problem.
Only really exists in certain backends.
I get that it's really popular.
Nonetheless, like, it just… I guess where my mind is, is like, where do we… fall on… I guess it's fine to make it opt-in, because if you don't have that problem, you can just say.
While I'm opting in.
**Antonio Martinez (Cisco Systems, Inc.)** 12:15 Hold on, yeah.
**Braydon Kains (Google LLC)** 12:17 We could, like, there is, there is such thing as recommended.
**Antonio Martinez (Cisco Systems, Inc.)** 12:21 Yeah, they initiated the conversation, so here. But given the metric is an option, is it okay to attribute at recommended level, assuming so much cardinality?
but they don't know where it landed because it was resolved. I don't know. I thought we need to send a second call before.
**Braydon Kains (Google LLC)** 12:46 That's a, I never, I never knew if that was a.
a… important… like, distinction, where, like, if a metric itself is opt-in, then it's okay to mark things as required, because you can opt out of the metric entirely. I don't know if I fully buy into that.
Like, I can see clearly that there is a case where someone wants this… Histogram…
**Antonio Martinez (Cisco Systems, Inc.)** 13:13 I'm going to recommend it, by the way.
**Braydon Kains (Google LLC)** 13:14 Without, yeah.
Yeah, recommended. I think that's probably what I would… what I would say, where, like.
We do recommend it because we, as a SIG, feel that the metric is Dubiously useful without it, but we aren't going to say we literally don't want you to report this without.
Like, if you are in a scenario, Where it doesn't matter.
the individual, like, you just want every DNS lookup, regardless of the name you're looking up, to all fall into the same buckets, like… I guess that's okay? Like, it… As long as… this is kind of similar to, like, how the system semantic conventions provides metrics like utilization.
And within the description, we say, like, we don't think you should use client-side utilization, but here's the metric anyway if you really want to report it.
**Sven Cowart (ElastiFlow Inc)** 14:14 Yep.
**Antonio Martinez (Cisco Systems, Inc.)** 14:19 Okay, so, and just also to let you know, the eBPF team make it by default, they are not adding the DNS, the DNS question name, by default, it's configurable, and the customer can configure it. By default, they are not adding it. They are populating the metric, but not adding the… because certain… since, like, some customers say that it's, like, a denial of this.
Okay, feel free to…
**Braydon Kains (Google LLC)** 14:42 The case for OBI here, I can kind of see it where, like, if you really are trying to control, I mean, so OBI is very Grafana-focused. There are other… there are other backends that care about OBI now, too, but Grafana is one that would crumble under high cardinality, and something like an eBPF solution monitoring the whole system where the user could make DNS requests of, like, any amount on all kinds of question names.
Causing a problem, like, I can… I can see where… where OBI is coming from.
For wanting to make this.
Wanting to make this optional.
Hi.
**Antonio Martinez (Cisco Systems, Inc.)** 15:26 Okay, so please take a look whenever you find time. I always forget what is this, the process, but once a network SIG group approve it, Ludmila or any other with approval, sorry, with maintainer can merge it, I guess.
But yeah, that's it.
And moving on, Monster.
**Braydon Kains (Google LLC)** 15:46 I can leave an approval on it from the network approver group and, like, summarize what we talked about here.
**Antonio Martinez (Cisco Systems, Inc.)** 15:53 Oh, that's really awesome.
Hmm.
**Sven Cowart (ElastiFlow Inc)** 15:56 I think, just kind of speak to that a little bit, Antonio. I think the process is that a PR has to gain significant approvals, and then that gets the attention of the people who have merge rights, is that right, Brittany?
**Braydon Kains (Google LLC)** 16:10 Yeah, generally.
The people who have merch rights will sometimes see it ahead of time as well, but…
**Sven Cowart (ElastiFlow Inc)** 16:16 Yeah.
**Braydon Kains (Google LLC)** 16:16 The general process in SAMCOM is similar to other projects where like the the main owners and maintainers, like, unless they have ownership of that area as well, they wait for the people with ownership to approve conceptually, so that the maintainers can look on a higher level, just like, is this following general SEMCOM rules after?
**Sven Cowart (ElastiFlow Inc)** 16:42 Sounds good.
**Antonio Martinez (Cisco Systems, Inc.)** 16:49 Great, thank you for that. And I have on my to-do list three pull requests. One is the ESN number, ESN, organization name. It's been already approved. I'm waiting for them right now.
Someone else from the… from the team, and then we can ask the maintainers.
peter Here is pretty straightforward is what we agree on. So we'll have Esn number and Esn organization.
It will drop under all the addresses, attributes, which… Will be network local, network peer, but not only those, also the… The client, the destination, and the server and source, all of them.
And then it's quite similar, honestly, for the prefix, also known as CIDR. We are going to have client, server, source and destination, network, local, and peer CIDR, which will be the prefix of that address, honestly.
And that is waiting approval for both of you guys. Whenever you find out time, feel free to do it.
Another one… totally following the same pattern. We have the Mac.
We will be for both client servers, source and destination, then local and peer.
and that will be the Mac address of the That, note, or device.
And so, yeah, whenever you find time. Feel free to take a look, and if you have any comment, I will review it for sure.
So those were…
**Sven Cowart (ElastiFlow Inc)** 18:21 Okay.
I do have one quick call out on the AS.
And I'll… actually, all three of these.
The only thing that came to mind, and I didn't bring it up in the PR, is because I don't want to… delayed this These semantic conventions from being merged is that we This is the exact use case, and maybe it'll make it… more obvious, and why we should need to pick up that work again as a larger community of the embedded attributes or attribute types that can be, expanded on. So, I… Robbie Wyler, Just to call it out that that is related to this, but that would be a much larger effort.
And… and what that is, is Brayden, I don't know if you were on these… those calls, you know what I'm talking about?
**Braydon Kains (Google LLC)** 19:10 I don't think so. I'm wondering if it addresses the main thing I saw there, which is like, we have the same like ASN Yes. attributes in every single namespace. Yeah. Like, is there a way around that? Is that what this is about?
**Sven Cowart (ElastiFlow Inc)** 19:24 Yeah, exactly, yeah. There was some efforts, I believe it was started in 2024, maybe even continued on in 2025, and then kind of got halted and didn't get moved forward, that Ludmilla pointed me to, but it was this idea that… and the suggestion I made to Semantic Convention Group was, what we really want is, like, a.
Like, attribute types that are groupings of attributes that you can add on to and embed into any prefix?
when these other things are present? Because I'm… and so, what we're describing here is the IP type.
Attributes.
Right, and there was some work where that was done, but it just didn't… it didn't get completed and merged in, because she said she doesn't quite remember, she'd have to work through it again, but there was edge cases where it wouldn't make sense, or something along those lines. But I do think that would be valuable, especially for this, and likely other people, too, across the community.
**Braydon Kains (Google LLC)** 20:25 Yeah, because ideally we wouldn't need to have… the same… like, metric definition in every… different place, like, because I imagine that that CIDR definite, like, the semantics around what the CIDR contains itself is probably not dissimilar between network local, network peer, versus client server, versus Yeah. Whatever the third group was. But we… but because of the way that we're setting it up, like, we kind of have to… Repeat the same metric over and over.
I.
And keep the semantics in sync. And so that I can, I could see that being, being frustrating.
to… to maintain… I don't… there's… there's an argument to be made whether it's clear to users or not, if there's, like, one… I.
network.mac that had different, like, groups of attributes instead to just, like, differentiate between them.
But… Well…
**Sven Cowart (ElastiFlow Inc)** 21:31 Oh, the problem is you need to… It comes back to it could be different based on the meeting, since they source client server and network local up here have all different meanings, and so you can't.
**Braydon Kains (Google LLC)** 21:42 Right.
**Sven Cowart (ElastiFlow Inc)** 21:43 Yeah. You could have more than one of those on… And from a different group on a…
**Braydon Kains (Google LLC)** 21:50 Right.
**Sven Cowart (ElastiFlow Inc)** 21:50 Or something, yeah.
**Braydon Kains (Google LLC)** 21:52 Yeah, maybe that is fine.
Just to leave them in their own namespaces, anyway.
We might be able to do something where we, like.
source of root… from, like, some root network docs explaining CIDR number semantics, like, how we think those should be reported, what RFCs, and then just, like, link to them in all… link to that, like, root guidance in all of them, maybe that would be enough.
**Antonio Martinez (Cisco Systems, Inc.)** 22:24 Yeah, that could be an option, but… Honestly, from my perspective, it's like… Here, for example, we have all of those, which is super similar to those.
From my perspective, we have to keep doing that until we have the ticket that Sven was mentioning, like Bilmira had some sort of block or didn't progress, because from my understanding, it would be like we're gonna have a an object that could be, let's call it address, and that address object is going to have a subset of attributes. One is going to be address.
port See Idr Marc.
And we can count, because more will come. Network type, I think? Oh, yeah, this is totally separate.
It's great things with others, but what I'm saying here is, like.
we… once we do that change from one place to another, it will be the same, because all those attributes will keep existing, so we'll not break anything. The only thing will be is, like, instead of having to modify, I don't know, 16 files, 17 files, we are gonna just modify on a single place, and everything will be automatically populated.
That's also the way how it… I anticipate that will work, right?
And you know, you only have to define the… all the attributes of that address object in one place. Maybe we put it most likely under network.
common, I don't know, just thinking loud, but that could be the way how I see that.
Until that doesn't progress, we'll have to duplicate things.
**Sven Cowart (ElastiFlow Inc)** 23:59 Makes sense to me.
I don't… I like it actually being inside the… The model for each, because it makes it not confusing, because if we start adding it somewhere else, like, by being embedded there, I'd be like, so it would just make it hard to find.
**Braydon Kains (Google LLC)** 24:18 Yeah.
**Sven Cowart (ElastiFlow Inc)** 24:21 It's just a less ideal… Situation from a maintenance perspective, and… potential even drift, I would say.
**Braydon Kains (Google LLC)** 24:30 I think that would be the only thing I'm worried about, like, the, you know, the… us having a harder time maintaining them is a fully fine cost to take, as long as we are, like, making clear metrics for users. But the hard part would be, what if the… if… like, we have to keep them in sync. We have to make sure we actually do keep them in sync, and we lack a… A very obvious mechanism with which to do that right now.
**Sven Cowart (ElastiFlow Inc)** 24:58 Yeah.
**Braydon Kains (Google LLC)** 25:02 So… Yeah, I… I still am okay with it, and I, like, because when I think back to Sven's PR, but, like, the general guidance of, like, what those namespaces mean.
I think them… like, being replicated across all those namespaces. There's a good reason that we're doing it that way.
It's… Just a matter of how we're gonna keep it in sync with each other.
**Sven Cowart (ElastiFlow Inc)** 25:26 Maybe, maybe what we do is, It's right, not… too dissimilar from how we're doing the guidance on that guidance doc inside a network, but just write something else.
About… these attributes are all related, and they must be kept in sync.
Ron @rrc-cooper: inside of the network.
Domain.
**Braydon Kains (Google LLC)** 25:53 Yeah.
**Sven Cowart (ElastiFlow Inc)** 25:54 That way it… It's just called out somewhere.
Because that.
**Braydon Kains (Google LLC)** 26:01 That makes sense.
**Sven Cowart (ElastiFlow Inc)** 26:01 That is my biggest concern is Drift, especially because, like, we're not the only ones that can edit this stuff, and we might miss something.
N.
At least if that's documented somewhere else.
Okay, this address type.
Group, that would be useful.
**Braydon Kains (Google LLC)** 26:23 It would be, it would be a good protection against People trying to use agents to edit the stuff, too, because…
**Sven Cowart (ElastiFlow Inc)** 26:29 That's right.
**Braydon Kains (Google LLC)** 26:30 Somewhere, yeah.
**Sven Cowart (ElastiFlow Inc)** 26:32 I didn't know.
**Braydon Kains (Google LLC)** 26:33 Then the agent's reading something that exists that says we have to.
**Sven Cowart (ElastiFlow Inc)** 26:37 Anyone who's using AI agents would see that and then make the edit appropriately. Yeah.
**Braydon Kains (Google LLC)** 26:43 for sure.
**Antonio Martinez (Cisco Systems, Inc.)** 26:44 Maybe after that pull request is merged, things will be kind of more organized for the network documentation, so maybe we can add it.
or after.
and choosing network match attribute. Maybe we're gonna like somewhere around here.
Oh, here, okay…
**Sven Cowart (ElastiFlow Inc)** 27:05 Yeah, we can do that. That makes sense.
**Antonio Martinez (Cisco Systems, Inc.)** 27:06 Yeah, one of… one of those two.
One of those two files could be… Could be a place to add it.
I will put down an action item.
For that.
**Sven Cowart (ElastiFlow Inc)** 27:16 Cool.
We could also just make a new markdown file.
If it makes sense.
**Braydon Kains (Google LLC)** 27:23 Yeah, the markdown, we do have a little bit of freedom in how we… How we write that stuff, like how it gets presented to the Semantic conventions like website, like, You know, if we wanted to really group things together in a different way, we could just write the mark down a different way. We are allowed to do that.
**Antonio Martinez (Cisco Systems, Inc.)** 27:52 I will take the action item to create a GitHub T-shirt for that.
And… Cool. And the other comment that they have was, I don't know Robert, but he didn't attend a few meetings, but do we know anything about the network interface metric and attribute proposal that it was put together a few weeks ago?
Thing was around those lines.
I don't know if… He had the chance to create like a GitHub issue on a proposal.
**Sven Cowart (ElastiFlow Inc)** 28:28 No, not yet. I don't… I don't think Rob has made any progress on this, unfortunately.
**Antonio Martinez (Cisco Systems, Inc.)** 28:35 Do you think we should try to start by creating the GitHub issue, adding the link here, and then we can start adding the feedback there, because we started creating Talking about some feedback in the meeting, but…
**Sven Cowart (ElastiFlow Inc)** 28:47 Oh, yeah.
**Antonio Martinez (Cisco Systems, Inc.)** 28:47 I agree.
**Sven Cowart (ElastiFlow Inc)** 28:49 Yeah, I would say that's a good idea.
**Antonio Martinez (Cisco Systems, Inc.)** 28:53 Oops.
data production tool.
Okay. It would be great to start adding those, because that will be the keys.
And I remember he also put together something for SNMP, if I'm not mistaken, or…
**Sven Cowart (ElastiFlow Inc)** 29:25 Yes, yep. The…
**Antonio Martinez (Cisco Systems, Inc.)** 29:28 That one, I don't have the link where it was.
**Sven Cowart (ElastiFlow Inc)** 29:31 The BGP one and the SNMP one, which I don't know if he's shared the link for the SNMP work yet.
I can ask.
**Antonio Martinez (Cisco Systems, Inc.)** 29:42 We may want to retake those conversation.
**Sven Cowart (ElastiFlow Inc)** 29:46 Yep.
Absolutely.
**Antonio Martinez (Cisco Systems, Inc.)** 29:58 And because one thing that is interesting, like, the other day I was talking with the Meraki team inside of Cisco, they were mentioning that if we have any proposal, how we are gonna name things under OpenTelemetry, and they said, yeah, we are working on that, but we don't have anything yet.
established, or any… anything concrete. But yeah, they are also looking for that.
So once we have something, we'll pass it also the proposal for them… to them, but yeah.
Ruby Ruth.
**Sven Cowart (ElastiFlow Inc)** 30:25 Yep. I I just slacked him.
See? See? See what he has.
**Antonio Martinez (Cisco Systems, Inc.)** 30:33 Okay.
Any other topic, guys, from your side?
**Sven Cowart (ElastiFlow Inc)** 30:42 Not at the moment.
**Giuseppe Ognibene (Coralogix)** 30:46 Perfect.
**Antonio Martinez (Cisco Systems, Inc.)** 30:47 Okay, so…
**Giuseppe Ognibene (Coralogix)** 30:48 I have a question for Sven. I don't know if you had time to see the TCP network matrix.
**Sven Cowart (ElastiFlow Inc)** 30:55 No, I still need to get to that. I'm sorry.
**Giuseppe Ognibene (Coralogix)** 30:58 No, no problem. I mean, I know it's long, so take your time.
**Sven Cowart (ElastiFlow Inc)** 31:02 Yeah, no, no, we're Just so you guys are aware, we're… I got a lot on my plate preparing for KubeCon, so some of this work is taking a backseat, because I need to make sure my team can go to KubeCon, and we're a small company, so sometimes when there's hot priorities like this, I have very little wiggle room to… to… to work on.
**Giuseppe Ognibene (Coralogix)** 31:28 Do you have a book?
**Sven Cowart (ElastiFlow Inc)** 31:29 Just do we have a booth? Yes, we do.
**Giuseppe Ognibene (Coralogix)** 31:32 Oh, cool.
**Sven Cowart (ElastiFlow Inc)** 31:33 Yeah.
**Giuseppe Ognibene (Coralogix)** 31:35 Nice.
**Sven Cowart (ElastiFlow Inc)** 31:36 Right.
I'm assuming that means you're going?
**Giuseppe Ognibene (Coralogix)** 31:41 No.
**Sven Cowart (ElastiFlow Inc)** 31:41 Yep.
**Braydon Kains (Google LLC)** 31:43 I'll.
**Antonio Martinez (Cisco Systems, Inc.)** 31:43 Probably be there this time.
**Sven Cowart (ElastiFlow Inc)** 31:44 Oh, great. Great to meet you in person.
**Antonio Martinez (Cisco Systems, Inc.)** 31:47 Indeed, yeah. I… I have a question. I don't know how those things work, honestly, but there is usually, like, an OpenTelemetry And… observatory, I think they call it, and they have like they're like on a schedule with, or they are going to talk about the operator seek or the collect the collector seek.
Maybe we can also ask for a slot for the Networking. I don't know how busy you guys are gonna be, and if it is that worth it, but maybe that will be also some marketing, in the sense, like, if anyone else wants to join, to see what we are talking there, what we are doing there. We don't have to have, really, an agenda, that will be… Brydon might be more familiar than me, but as far as I know, it's just the same at that meeting, but there, in person.
It could bring people that are not that familiar with network or not that familiar with open telemetry joining there.
**Braydon Kains (Google LLC)** 32:41 Yeah, I can… I don't know what the plan is this year, so at… at the EU conference, they… there was not an observatory, and we just kind of met in the project area, the CNCF project area. I think, at the very least, they'll be doing that again, if there's not an observatory.
**Sven Cowart (ElastiFlow Inc)** 33:00 I didn't see that in… any of the materials I read that they would be.
**Braydon Kains (Google LLC)** 33:06 Okay, so then they probably didn't do it, which is too bad, it was always fun, but I.
**Sven Cowart (ElastiFlow Inc)** 33:10 There was a maintainer summit, but that's…
**Braydon Kains (Google LLC)** 33:13 Oh yeah, the maintainer summit.
**Sven Cowart (ElastiFlow Inc)** 33:15 Yeah.
**Braydon Kains (Google LLC)** 33:16 Yeah, that's a separate event. It's before the CNCF Located Day.
**Sven Cowart (ElastiFlow Inc)** 33:20 Yeah.
**Antonio Martinez (Cisco Systems, Inc.)** 33:24 That's on Sunday, right?
**Braydon Kains (Google LLC)** 33:27 Yes, that's on Sunday, and I think… Both of you would be… Able to go, since as a graduated project, anybody who's an OpenTelemetry org member is… is allowed to.
**Sven Cowart (ElastiFlow Inc)** 33:37 Oh, okay. Oh, that's cool. I didn't know that. I didn't think I would actually be able to go.
**Antonio Martinez (Cisco Systems, Inc.)** 33:42 By the way, you have to ask for permission. I mean, not permission, but when you register, you have to mention at least your GitHub name.
And then they will approve it to you, but it's something like they have to do it some sort of manual, so ask for it. I did it, like, a couple of weeks ago.
**Sven Cowart (ElastiFlow Inc)** 34:01 I see.
**Antonio Martinez (Cisco Systems, Inc.)** 34:03 So it will be there, too.
But do we know if we can ask for a slot on that agenda that they have?
or who is the responsible for that? Maybe we can add. I don't know. Sorry.
Betting, or… Let me level my notes also. I don't know.
**Braydon Kains (Google LLC)** 34:21 It will… for that schedule, it'll probably be Reese, if it is happening recently, as the hotel community manager. I can ask her, if that's…
**Antonio Martinez (Cisco Systems, Inc.)** 34:32 That'd be great.
**Braydon Kains (Google LLC)** 34:33 And yeah, if it is, then I'll ask for a slot for us, if we're interested.
**Antonio Martinez (Cisco Systems, Inc.)** 34:49 Thank you for that. Let us know if you don't find something.
**Braydon Kains (Google LLC)** 34:52 Yep.
**Antonio Martinez (Cisco Systems, Inc.)** 34:55 Alright, so… That was all, I guess, for today.
**Sven Cowart (ElastiFlow Inc)** 35:02 Yep.
**Antonio Martinez (Cisco Systems, Inc.)** 35:03 Please take… Thank you. Take some time to review the progress so we can progress that for the next one.
**Sven Cowart (ElastiFlow Inc)** 35:08 Sounds good.
**Braydon Kains (Google LLC)** 35:09 Sounds good. I didn't realize they were… you were, like, waiting on me for those, so I'll get to those today.
**Antonio Martinez (Cisco Systems, Inc.)** 35:13 How you guys usually like to receive notification? Because, at least from my perspective, I have, like, that typical pull request, like, all the people that ask me for review, it will appear there on the list.
So, I don't usually notify anyone, but it's personal, and it's… its thing is different. So, when my name is here, I get, like.
on that table, like, I just request it on Tongene, and that's the way how it works, but how you guys are doing? Do you prefer, like, I ping you when I never have a pull request for you, or… Do you prefer.
**Braydon Kains (Google LLC)** 35:45 Yeah.
**Antonio Martinez (Cisco Systems, Inc.)** 35:45 point.
**Braydon Kains (Google LLC)** 35:46 If you're ever waiting for me for something like I'm like, it's blocked without my looking at it, then a Slack ping is fine. I try to manage it through GitHub notifications, but once you become a, like an approver or maintainer in like the collector repo, the notifications explode. So like I.
**Antonio Martinez (Cisco Systems, Inc.)** 36:07 Happy birthday.
**Braydon Kains (Google LLC)** 36:08 track of everything.
**Antonio Martinez (Cisco Systems, Inc.)** 36:09 Are you anybody?
**Sven Cowart (ElastiFlow Inc)** 36:11 That's actually good to know, because I also just keep track of it like you, but I guess I haven't reached that level yet where I have so many where I don't know where to look at anymore.
**Braydon Kains (Google LLC)** 36:21 If I… every time I go to my notifications tab, I have the little thing that says 10 plus new notifications, and I refresh it, and the whole thing's a wash.
**Sven Cowart (ElastiFlow Inc)** 36:29 So.
**Antonio Martinez (Cisco Systems, Inc.)** 36:31 I understand you don't read them. Yeah, I.
**Braydon Kains (Google LLC)** 36:34 I try to keep track of it as best I can, but yeah, the direct Slack pings are fine, given the impossibility with which I keep track of everything.
**Antonio Martinez (Cisco Systems, Inc.)** 36:45 Awesome.
Thank you, everyone. Yeah, bye.
**Giuseppe Ognibene (Coralogix)** 36:49 See you.
