SIG: Network SIG
Date: 2026-07-20
Duration: 37 minutes
============================================================

## Zoom Recording Transcript

**Mario Macias** 00:40 I don't know who's been… Oh, sorry, I think I cannot hear you. Maybe it's me?
**Sven Cowart** 00:58 Can you hear me now?
Yeah.
**Mario Macias** 01:01 Yes, I kind of.
**Sven Cowart** 01:02 Or I forget to turn it on in the mornings.
I was saying, I said good morning, and then I realized you're in Europe, so good afternoon to you.
**Mario Macias** 01:12 Yeah, thank you. Good, good moment, any day of the day.
Many reasons.
**Sven Cowart** 01:17 Good moment, there you go.
What are you working on right now?
Over on Grafana.
**Mario Macias** 01:35 I mean, you mean in the department of… or the team in Grafana?
**Sven Cowart** 01:40 Yeah, just in general, yeah.
**Mario Macias** 01:43 Yeah, it's… I'm in the Open Telemetry, in the OV.
**Sven Cowart** 01:47 Oh, okay.
**Mario Macias** 01:47 Yeah, and Baylor. Oh, nice. We've Baylor, EVPF.
**Sven Cowart** 01:54 Hi, Matt. Hello.
**Mario Macias** 01:55 Oh, Antonio.
**Sven Cowart** 01:56 on the alloy team that leads that a while ago at one of the… one of the Grafana conferences. I don't remember his name, but he was a staff engineer over there. It's really…
**Mario Macias** 02:05 But…
**Sven Cowart** 02:06 Really nice guy, helpful guy.
If I could look it up, we've changed numbers, I don't remember his name.
**Mario Macias** 02:13 Maybe?
**Sven Cowart** 02:27 Hey, Antonio.
**antonjim** 02:29 Good to see everyone.
**Sven Cowart** 02:31 Oh, hey, Braydon.
**Mario Macias** 02:32 We'll pursue you.
**Braydon Kains (Google LLC)** 02:36 Hello. Morning.
**Sven Cowart** 02:38 I had to guess, I think this is gonna be it today. Rubbing me's gonna be out.
Today, so, this might be rather short. I have just two things to cover real quick.
The, project PR has been updated, so it's ready for… another review, or a final review, hopefully, where we just get the thumbs up. I'll be… attending… Yeah, right again. I'll be attending conventions, Group today to ask if… what else needs to happen, if anything, at this point? So… Okay.
**Mario Macias** 03:22 Okay.
**Sven Cowart** 03:24 The… and just for you guys that, last time kind of covered this, but the main… ask was to provide stability or clarity around making stability part of the goals of this project. The other ones were to identify who the staff members are that are also in other groups. I've tried to list them.
Out in the staffing section here.
Rob said he'll start to regularly participate in the entities SIG, I'll start to participate in SEMCOM SIG regularly, and Braydon… Do you leave the system safe?
**Braydon Kains (Google LLC)** 04:06 We don't really have one lead, per se, but I probably am the most active at the moment.
**Sven Cowart** 04:12 Okay.
**Braydon Kains (Google LLC)** 04:13 And you can also put me down as affiliation Collector.
**Sven Cowart** 04:17 Oh, sweet. Okay, that's great. I'll do that. I'll add that.
And Ben Giuseppe and Mario, I put you guys on over.
**Mario Macias** 04:26 Great.
**Sven Cowart** 04:28 Anything I missed?
from anyone.
Okay, and then…
**Braydon Kains (Google LLC)** 04:37 I think Steven is on OB, I think, or at least I've…
**Mario Macias** 04:41 Yes, Steven has sentinovi, yeah, yes.
**antonjim** 04:47 And most likely Henrik is also… I'm doing another offer on Open Telemetry.
**Braydon Kains (Google LLC)** 04:57 Enric does do a lot of… a lot of open Telemetry stuff. I don't know what specific SIGs He's most involved with, but, he does a lot of, like, Community education stuff.
**Sven Cowart** 05:07 Which one?
**Braydon Kains (Google LLC)** 05:08 Enrique.
**Sven Cowart** 05:12 Oh, okay.
**antonjim** 05:12 Right.
**Sven Cowart** 05:13 I haven't met him yet.
Which one did you say, Antonio, that he's a part of?
**antonjim** 05:19 Yeah, I was mentioning the same one, Henry.
**Sven Cowart** 05:21 Oh, okay.
**Braydon Kains (Google LLC)** 05:22 I'm not… I'm not sure what specific SIG he's most involved with. I think he's… well, he's a developer relations person at Dynatrace, and so he does a ton of, like, community education and community involvement stuff. I'm not sure which… if any specific SIG he's most involved with.
**Sven Cowart** 05:42 Got it, okay. I'll reach out to him, see if he wants to.
List anything here?
And then the other, bigger item was just around… we covered in entities. We started to talk about entities and what came from that, and all the areas that we're going to dig into, which I've now listed in Let our find a little bit here in the midterm goals, and see… see where we go.
A lot of this is obviously still a work in progress, so we'll need to keep updating this as we make progress and actually defining these things.
Okay, taboo… Okay, the other thing was, I'm gonna start, opening issues and opening PRs for some of the near-term goals.
And so we can start moving on.
At least the… And just… So you see what those are. It's mainly about review all the existing attributes and see where there needs to be improvement and clarifications, and think about, like, moving forward, as well as addressing all the existing issues that are open in the areas that we are calling Terry to take over.
And, and then just some naming and university.
improvements in the documentation, generally. So, some small items, but just things we can get started on here soon, and create a plan around tackling. I'll probably… I will go through these and write issues for them. I'm not exactly sure how I want to do it yet, but we can review those then next week. And then if… if… anyone wants to volunteer, I'll also do it, but if anybody wants to volunteer as well, and look at the issues that are related, that are linked here, and the areas we'll cover, and see if you have ideas on how to address them, then Please feel free and bring that information to the next call.
**antonjim** 07:41 But how do we want to proceed? That's a good comment. Do we want to review existing issues with… related with network, and start commenting about them here, and then proposing on a comment, like, summarizing the agreement here, and in a comment in the ticket, right?
**Sven Cowart** 07:57 Yep, I think so, yeah.
Yeah. There's not… Hope on these again? That's weird.
**antonjim** 08:10 We're gonna try to look for a few of them that could be interesting to start with.
**Sven Cowart** 08:15 Yeah, I know some of them are yours, too, so we should start addressing those. This one has the most, but it's not that many, really. I was expecting it to be way more.
And each of these other ones don't have that many either. So, I mean, it's work, but we'll get through it. I don't think it's an insurmountable task that we have to do to review these, especially if we… I'll, volunteer some of our time here to do that.
And I think that is it that I wanted to talk about.
**Braydon Kains (Google LLC)** 08:53 I had one item.
**antonjim** 08:55 Before…
**Braydon Kains (Google LLC)** 08:56 There you go.
You can go ahead.
**antonjim** 09:00 Thank you, Braydon. The comment is.
what do we want to do first? Because you mentioned that for next meeting, we can start addressing the comment, but if you go to, for example, one of the tickets that I proposed there, we are still on top of network.
address.local or network.local.address.
Does it make sense that we still have agreement about, let's say, the peer, sorry, peer or local, that we add, like, the ESN number, or the prefix, or those things.
Or where we didn't agree yet, if we want to keep the pier, or unlocal, or… remote, or we want to have, like, source and destination. I don't know if you follow me, like, imagine that we agree on having, like, the prefix or the ESN number.
as new attributes. Do we want to still add them on top of local and remote, or do we want to start… I mean, I mean, a development proposal for… Resource and destination.
**Sven Cowart** 10:04 Here's what I want to do. This first one, I'm gonna create an issue where I just list out everything that exists.
And then we can iterate on that, and then see, okay, based on everything that exists, it makes sense to move in this direction, and then hopefully that informs the ones that you've opened.
I don't think without that holistic picture, we're gonna… come to a good solution by just addressing each of the things individually. So I'd like to start there around the ones where there is, confusion or, they're not well thought out enough for us. Does that make sense?
So, I'll actually create that issue.
**antonjim** 10:44 No, no, not…
**Sven Cowart** 10:45 Yeah.
And I'll link… I'll link to all the necessary ones that are most immediately impacted by… by that.
Does that sound good?
**antonjim** 10:59 Ideally, yeah.
**Mario Macias** 11:00 Yes, from Sunday.
**Sven Cowart** 11:04 Good, Braydon.
Let's see, what is this one?
**Braydon Kains (Google LLC)** 11:09 So, something that is happening, you know, in parallel to the network group is that there are lots of requests for new networking features in host metrics, so we're still fielding some requests to the system network namespace.
And so when they come in, I try and look at them as best I can. Like, I've made clear that I'm not a networking expert, but I'm still trying to field these as a member of the system group. So I'm looking at this one, and if people know about network interfaces, check my understanding here, because I sort of… Took a 20-minute look at this, and I… I understand that, like, this is someone who's never contributed to semantic conventions before, so they have no way to know, but… the definition of the metric kind of confused me. It talks about getting the… the… speed of a network interface from that file. That file reports one integer, so that would be for symmetric interfaces, like up and down are the same.
And then when they're not the same.
I think it biases to down, so it'll report the down speed in that, but not the up speed.
But then the network… the metric has… reports it by… direction.
Always by direction, so transmit and receive get their own… limits.
So… if… I'm trying to just… two things I'm trying to figure out. First of all, I don't know if this should be in system. Like, this… the network bandwidth limit is not… a pers… not, like, for the system. The system as a whole doesn't have a network bandwidth limit. It's each… like, interface has one, so I feel like this should be in the network namespace, not the system namespace, because that's sort of the way we're treating the system namespace. It's like things that apply to the system as a whole.
like, the system network I.O, that… is… it's kind of also per interface, so I don't know how well it applies here, but the… The network bandwidth limit is not a system-wide thing, it's just each link has its own… has its own limits. And then whether the direction should always be reported, or if it should be optional. And, like, if the direction attribute isn't reported, then you assume it's a symmetric interface.
I don't know if that's… As someone consuming the metric.
which would you prefer? Would you prefer that the attributes… the lack of presence means that up and down are the same, or if, in most cases, you're reporting both directions with the same number?
As two data points.
**antonjim** 14:09 My point of view on those unclear scenarios is always to have completeness, so send both metrics, with different attributes, even if they have the same value.
So, people don't get… Don't have to make those questions themselves, or read the documentation.
**Braydon Kains (Google LLC)** 14:29 Okay, that makes sense.
**Sven Cowart** 14:31 I would agree with that. I don't like making assumptions in schema.
So, I actually agree with both your points, Braydon. I don't think it should be in the system area.
Because it does relate to network interfaces.
Just feels a little weird.
**Braydon Kains (Google LLC)** 14:59 Yeah, I think… it… Likely this metric, the entity that this metric will be reported against?
would be… Well, actually, our network… our network metrics aren't really designed around interface… around entities right now. Right now, the idea is that this would be reported against a host, and then each network interface name would get its own data point.
It might be better for this to be reported against, like, a network interface entity.
And just have this metric.
With just the direction attribute, and then expect that it's reported against an interface entity, but… We haven't gone that far yet, so I'm not sure.
Whether that's actually what we want to do in the long run or not.
**Sven Cowart** 15:47 Yeah, that's already what we're drafting, that… and you'll see that that Rob puts up, but sometime this week around network entities, but network interfaces will be one of those entities, so I…
**Braydon Kains (Google LLC)** 15:57 Okay, I see.
**Sven Cowart** 15:58 That makes a lot of sense, and I think that's a great call-out to move into that direction.
**Braydon Kains (Google LLC)** 16:03 Okay, I'll… I'll bring this to the… the, Slack channel, so that Rob can get in on the discussion, and we can… we can verify that, that this is probably… Should be a metric reported against an entity, and probably not in the system namespace.
**Sven Cowart** 16:21 Yep, makes sense.
And if it… the in-and-out thing, I… the more I think about that, the more confident I feel that they should just be two separate metrics. There's quite a number of things that are like that, and it just seems… Weird to not make it to…
**Braydon Kains (Google LLC)** 16:41 Well, we had it as two separate metrics, and… A few years ago, made the change to reporting the same metric name with two direction values.
On the… in the attribute.
**Sven Cowart** 16:53 See?
**Braydon Kains (Google LLC)** 16:54 That is becoming very common in the, sort of, hotel metric ecosystem. Less… less names and more, The… the multiplexing of the same thing goes, like, via the attributes.
differentiating time series on the same name. And I think the reason for that is largely around dashboarding.
Where, like, if you want to get lots of information about one type of thing. You just have to query one name, and then you get lots of different like, dimensions of information via attribute values. I think that's the reason that it's designed more in this, like, hierarchical way, where one name has lots of different types of time series under it.
I don't know that for sure, though. I don't think anyone's ever written it down.
**Sven Cowart** 17:45 So, that makes a lot of sense.
I think I wasn't explicit enough what I was saying, but I… the attribute thing makes sense. I don't think what I would disagree with is the ability to opt-in or not.
**Braydon Kains (Google LLC)** 17:58 Oh, okay, yes, yeah.
**Sven Cowart** 17:59 There, right then.
I assume that it means it's for both, it just feels strange.
**Braydon Kains (Google LLC)** 18:05 Yeah.
Yeah, I think I can… I think I can see that then. Just… I'm trying to think of the… something that we try to do in… in… our SIG is… like, because these metrics are targeting so many platforms and so many weird ways to get this information, you know, we try and have very explicit instructions for people implementing instrumentation for the metric, exactly how to get it on different on different systems. So, like, for this metric, for example, you could get it from sys classnet From that file. Or if it's asymmetric, you wanna, like.
go, like, IWDev, or ETH tool, or one of those, like, CLI tools to get this information, or maybe… there's probably syscall equivalents for that.
And then on Windows, there's a specific PowerShell command, I think, to get The link speed for a device, and there's probably some other… syscuddle thing on BSD likes, but, like, we'd have to very clearly lay out, if you're reporting this metric on Linux, we expect you to get it this way or this way. On Windows, this way, or this way, and… So I've…
**Sven Cowart** 19:16 Right.
**Braydon Kains (Google LLC)** 19:17 Like, probably what we're gonna end up saying is for… for… For reporting environments where you're just getting one link speed.
If you're confident that you're on a… that this is a symmetrical interface, and that that's… It's fine to report the same for both, then report that number for both up and down.
the scenario I'm trying to… I'm trying to… disambiguate is that someone… who instrumented this metric only via that file on Linux, or only via the, like, generic link speed attribute on… in Windows, when they report it.
They're assuming it's a symmetrical interface, because there's no way to know just by looking at that file that you don't have an asymmetric.
down.
So it might be… Someone could instrument it badly and report it wrong.
That was why I thought maybe you get rid of the network I.O. direction to say, like, we're not saying this is one or the other, but it would be kind of confusing in the dashboard. I can understand that it would be confusing to consume the metric with the direction as an opt-in, too.
Yeah. So probably we'll just need to be really explicit in the instructions.
In, like, the note around the metric about, like, exactly how this should be… reported.
**Sven Cowart** 20:42 What I'd rather do than make it optional is just to make it explicitly called out that it's both.
So the enum could be 3 and out, or, like… in, or out, or in out, or something, I don't know, but just a random.
**Braydon Kains (Google LLC)** 20:57 I'm like…
**Sven Cowart** 20:57 It'd be a bad idea, but that feels more clear than saying.
If it's not there, make an assumption about what it is.
**Braydon Kains (Google LLC)** 21:07 Yeah, there might be another… Another way we could do this, where instead of… No, never mind, this doesn't make sense, what I was about to say.
The… introducing a third… enum value to network I.O. direction.
One of the annoying things, this has bugged me about semantic conventions for a while, is that, like, if you have a shared attribute that's an enum.
But you're using that attribute in different places, where different values of the enum are or aren't… like, allowed. The big one is CPU mode.
we… there's… we have, like, a shared CPU mo… or CPU state attribute, that when you use it.
in system CPU utilization, or process CPU utilization, or container CPU, like, the enum values that are allowed are different, and we don't really have a way to say that.
In the metric definition. So we say, use this attribute, but then we have a note saying, we only expect this, this, and this value, which is not a very explicit way of saying it. So that's the only reason I'd be worried about introducing a third value for direction, which is, like, for system network I.O, there's no such thing as both directions, but… we're okay with it in this… in one metric to have the third value, but not in another, and we don't have a good way… this is a question I've asked the SimCom, say, a couple times, and I don't think anyone… feels as strongly about it as I do, that we need a solution for that, but…
**antonjim** 22:39 I was just looking, online. It seems like there is already a hardware network bandwidth limit, which is kind of similar to what… That guy is mentioning, isn't it?
**Braydon Kains (Google LLC)** 22:54 Yeah, the hardware namespace has a lot of… a lot of history.
This… this is before semantic conventions SIG really spun up. There was a company called Sentry, not the… not the observability company Sentry, a different Sentry, that had a bunch of, like, hardware… hardware, like.
Definitions for how they… how they measure hardware and stuff.
And they… Basically, bulk contributed all of their hardware.whatever metrics and attributes all at once.
And then… Stopped looking at it.
And so, a lot of the hardware namespace, we don't really recommend using because it hasn't really been given the semantic conventions, like, once over. Or, like, hasn't really been redesigned to work.
With our design rules.
And a lot of it really needs a lot of attention, and I just haven't had time to go back and look at it, but there are people in GPU who really want these metrics to look better, and, like, I'm… I'm guessing… the… this metric… I haven't… I haven't actually looked at this, I didn't know there was one.
It is…
**antonjim** 24:11 what's…
**Braydon Kains (Google LLC)** 24:12 None. Bro… Sorry, go ahead.
**antonjim** 24:17 No, no, my comment was on the direction of, if we end up creating something like network interface bandwidth limit.
do we want to deprecate the stability of those existing ones? Because they are also under the Open Telemetry semantic commission page at the end of the day.
**Braydon Kains (Google LLC)** 24:34 Yeah, there is… That's actually kind of an open question about, like, how we've… how we handle this namespace at all.
Because… there are people who use these metrics now, but, like, the SEMConf SIG generally doesn't like them? I mean, I think a lot of them are designed okay in, like, the pre-entity world, or… and, like, the pre, like, shared attribute world, but even on that… on that network bandwidth limit.
this… the whole, like, the hardware ID, the hardware parent, the hardware model, you know, a lot of these… like… Are things that should be an entity.
and aren't… The hardware… hardware name is not… like, that's the network interface name. It's probably where we want to use that. And, like, the hardware.network probably has its own… Entire world of stuff that we haven't even looked at yet.
that… might need to be… might need to be addressed, too. I… it's probably worth… We could probably say it's time to finally look at the hardware namespace and decide what to do about it. It's kind of been an elephant in the room for a while.
**antonjim** 25:53 at least the hardware.network, we could… I mean, because all of those we are gonna… most likely we are gonna… proposed, in the sense, like, interfaces, or… what else we have here? Packets, most likely will go through the OVI, will be interesting, like, on the number of packets being flowed.
Network app.
Is the network up? Okay, that's odd. Okay, but yeah, we need to most likely investigate what they have there.
**Braydon Kains (Google LLC)** 26:26 Hardware, metric hardware.status, network, like, already, already that probably doesn't… fly in… in modern SEMCOMF, because we would need to call that network status. Anyways, yeah… Yeah.
That is a good question.
About what we do when we find stuff in the hardware namespace like this.
the owners of this namespace will sometimes show up, but not regularly participating.
And I think they don't like a lot of semantic conventions, that's kind of the other sort of tension going on, is that they don't like a lot of what semantic conventions does for their metric design in comparison.
I think that's why we haven't addressed it.
But we keep on getting requests in the host metrics receiver to introduce stuff using these metrics, and I'm not super comfortable introducing new instrumentation using these metrics, because I don't really know anything about them.
I don't have a good… yeah, I don't have a good answer here. We might need to talk about this in the SEMCOM SIG, maybe.
**Sven Cowart** 27:42 I think that's a good call-out. For what it's worth, when I got into Open Telemetry about a year and a half ago, I saw the hardware stuff, and I was very confused by it.
So I was like, well, it's computers, isn't everything hardware? That's not software.
**Braydon Kains (Google LLC)** 27:56 Yeah.
**Sven Cowart** 27:56 I didn't really get it.
**Braydon Kains (Google LLC)** 27:59 And there's a lot of overlap that probably is unnecessary.
Because they, they're… they're… Contribution of these metrics.
predates the System SemComf spinning up. So, when System SemComf spun up and we brought a bunch of stuff from the host metrics receiver, like, existing metrics that, like, super didn't fit the design either, but, like, we brought all the metrics that we had in host metrics, and then started fitting them to the SEMCOMF guidance.
So we kind of did the same thing as hardware. If we didn't look at what stuff overlapped, we just were kind of worried about our own Our own porting, basically.
And then it turns out there's a lot of overlap between what's in hardware and what's in system.
**Sven Cowart** 28:42 And the…
**antonjim** 28:44 City Elementary.
**Sven Cowart** 28:44 When we do the flow.
flow metrics, because network I.O, network packets.
**Braydon Kains (Google LLC)** 28:53 Yeah, like, we don't actually want a hardware version of all of these, like, overlapping…
**Sven Cowart** 28:59 Yeah.
**Braydon Kains (Google LLC)** 29:03 But, of course, if we try and say… like, we might have a different idea for what these packets… or what these different attributes that they're using should look like. And so it's like, do we say, alright, now let's try and retrofit all our newly designed attributes onto this old hardware network I.O, or do we try and deprecate hardware network I.O. and force it to, like.
force people to use our network one instead. There's… Yeah, this… This namespace has stressed me out for a while. I'm still not sure what to do about it, and I don't think the maintainers are super sure either.
**Sven Cowart** 29:43 Okay. Well, that's good to know.
I didn't think we'd get into the politics of Open Telemetry.
Inside of one month, but I guess here we are.
**Braydon Kains (Google LLC)** 29:54 No, that's… that's… that's semantic conventions under the hood. It's… it's… it's being… it's… it's part… partly as being as pedantic as… as possible.
And partly political.
I shouldn't sound so cynical on a brand new group, but it's fine.
Don't worry about it.
**Sven Cowart** 30:13 It's just… it's for humor.
**Braydon Kains (Google LLC)** 30:15 It's the name of the game.
**Sven Cowart** 30:18 Okay, thanks for bringing this up.
**antonjim** 30:24 I have another quick question. Before I created another ticket to have that conversation with my colleagues last week.
We have a custom… we are already sending the network lockout address, sorry, not the PR, the network PR address, and… as you know, there is another one with… if it is APB4, APB6, the network type.
But the customer wanted to have both. They didn't want it to have… and as you know, those are attributes, so it's not what you mentioned, Braydon before, about the metric, that you can say, okay, the metric is, like, the whatever, and then you put the… instead of putting the address on the metric, instead of putting IPv4 and IPv6, you're putting as an attribute. So, it doesn't work here, because both of them are attributes. It's not one is metric and one is attribute.
So the comment is, does it make sense to have something like network. Sorry, not.io, network.peer.address.
IPv4.ipv6, because it's possible that you find out both IPs on the same device, let's say. For our use case, it's a device.
So… Does it make sense that we evaluate those questions, or…
**Sven Cowart** 31:46 Are you… what is it that you're, reporting or instrumenting? Like, is it… Is it… are you exporting a metric, or is this on traces, or…
**antonjim** 31:56 Correct. For us, the metric is, like, how much throughput are you sending over that device, in terms of network, and also latency of that network, and so on. And then, when we describe about the device, we have, like, things like the Mac, the port, the address.
Another one for sure is, like.
we always put the IPv6 if we have it, if not, we put the IPv4. This is the way how we do it today, but there was a customer that they wanted to have both, actually. So it was like, okay, what do we do now?
**Sven Cowart** 32:27 So the metric would be one metric to describe both IPv6 and IPv4 traffic?
**antonjim** 32:33 Actually, I'd like to have, like, two… not metric, two attribute. Ideally, it would be two attribute, like, network or, so under the attrib.
**Braydon Kains (Google LLC)** 32:42 Time series.
**antonjim** 32:43 IP before.
Correct, correct.
**Braydon Kains (Google LLC)** 32:46 One… one time series. So, like, there… this… this… The throughput is being described for… one address that has an IPv4 and an IPv6 at the same time.
**antonjim** 32:59 Correct. For us, it's a device send… correct, that's right. It's a device sending the data through the network.
**Braydon Kains (Google LLC)** 33:07 Yeah.
**antonjim** 33:17 We'll have to reserve it now, but the question is, does it make sense that we created a GitHub issue and evaluate it, or it will go a little bit against unaddressed… I mean, in my opinion, it makes sense, because we need to extend… others is quite generic also. We need to extend it about what others really mean.
**Braydon Kains (Google LLC)** 33:44 Yeah, so the one thing about introducing an address.ipv4 and IPv6 is that I see here that the address can also be a Unix socket So, does that mean… Any possible way… any possible value for address would need to have, like, a subversion of it, so there would need to be an address.unix.
**antonjim** 34:05 Correct. The way how we solve it internally is, like, how we did it for the customer, was instead of having address, we put IPv4.
this is the metric that we are providing to the customer, for sure, also, like, the 6. This is what we leave to the customer. We are not breaking any other customer, because we are still sent the other one to the other, so we are not breaking anyone today, but… we are sending the other two as duplicated for that use case. It's only for that customer use case in our side, but… Aye.
I have my doubt, and we did that for that reason, because if… person is, like others, is kind of, already, stable, so I didn't want it to go against.
Macias.
Because it's half its own namespace already.
**Braydon Kains (Google LLC)** 34:57 Right.
I forgot that that was stable. Like, we might actually be able to introduce, like, keep address, but introduce… introduce, like.
more attributes, like network.local.address remains, but network.local.address.ipv4, and .ipv6, and whatever… whatever else we might want, and make those… make those opt-in, and… And say that, like, if you know… if you want to report multiple addresses for the same time series, then you go into these deeper, drilled-down attributes, and we say we expect that you would report if you report network localaddress.ipv4 and .ipv6, you wouldn't also report address, like, just the, just address 1.
I think that's… I think that's reasonable.
We aren't… we wouldn't break anyone by introducing that. It would just be, like, a new option on those metrics that… if you need to report… I think it's a perfectly reasonable use case to say there are multiple addresses for the same Entity, and we need to be able to report multiple on the same time series. So here are some more specific versions of this attribute that are opt-in.
**antonjim** 36:22 For voting.
Okay, so I will clear that this one, we will discuss it. It's the same problem as we said before. If we want to do it later, source and destination, or… We… we might don't want to… commit those yet until we have an agreement about what we do about local and remote or destination source. But yeah, that will be kind of the direction that we take there.
I will create that ticket, so we can discuss in more detail later.
**Sven Cowart** 37:00 Sounds good, thank you.
Okay, I think that's it then. Anything… anyone have anything else?
**Braydon Kains (Google LLC)** 37:10 I don't think so.
I'll try and join the SEMCOM SIG today. It overlaps with another meeting, so I can… if it cuts out short, I can join the SEMCOM SIG, but… We'll see what happens.
**Sven Cowart** 37:20 Sounds good. Thank you.
**Braydon Kains (Google LLC)** 37:23 Thanks, everyone.
**antonjim** 37:24 But…
