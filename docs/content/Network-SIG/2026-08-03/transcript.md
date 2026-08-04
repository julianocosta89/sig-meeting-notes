SIG: Network SIG
Date: 2026-08-03
Duration: 54 minutes
============================================================

## Zoom Recording Transcript

**RC Robert Cowart** 06:46 Hey, everybody.
**Stephen Lang** 06:51 Hi.
**RC Robert Cowart** 06:52 Sorry, I'm kind of heads down here, I didn't even realize it was already 5 minutes past.
Let me, look over at the sheet to try Let's see, Antonio's not… here today. He had a talking point, but he did not, He said he has a conflict today. I do know that the project PR was merged, which, I guess that makes us official now? So, Good to see that that piece is behind us.
I guess now it's just doing all the work that we had in the project, PR.
Let me bring up… actually, let me share my screen real quick. Probably also be helpful.
Alright.
Oh, this was the… the… Bringing in source destination.
Let me see if Sven is joining this as well. I don't know if he… Oh, that's right, Sven's out today, too. Okay.
I would say we probably need to push that to next week. I think those were the two that were mostly focused on this one, and I don't have any updates on the status of this particular ticket and have not read through it. I don't know if anyone else has read through it and might have a comment or not, but… Alright.
Then let me, Did anyone else have anything in particular they wanted to bring up? I would gladly open the floor before I move on to the talking point that I had.
**Marc Netterfield** 09:24 Nothing specific for me.
**Stephen Lang** 09:27 Not from me, either.
**RC Robert Cowart** 09:33 then… You know, as I've said on some of our other calls, I'm a… I'm a bit new to the hotel stuff, so I've been, you know, trying to just figure out how to do things right in OTEL, as I've also been going through some of the data that we, want to create conventions for over time.
and you know, we talked in the past about wanting to start with just defining entities and things, which I most definitely wanted to do as a starting point, but, you know, just from my experience, the vast majority of or quite a significant number, I shouldn't say the vast majority, but quite a significant number of… you know, metrics or attributes in network tend to be focused around network interfaces, and even in particular, the various specific types of interfaces. You know, so there's, like, generic interface, metrics, but there's also, you know, like, in-and-out bytes, you know, in and out errors, those type of things. But then, if you have an Ethernet interface, that has all types of Ethernet-specific metrics along with it, or if you have a DSL interface, a bunch of DSL-specific, metrics that also could be related to, an interface. So, essentially, it would become, like, You know, optional or, you know, maybe required, but type-specific attributes. I'm not quite sure how we would express that yet, but anyway, so I thought to myself, okay, I'm just gonna go through the… the standard stuff, and get all the interface stuff out of the way, which is, these… these different JSON objects here, you can… again, this is just out of the standard ITF and IEEE MIBs as a foundation.
And you can see this file has somewhere down here, like, 70,000-something lines. So, suffice it to say, there's a lot of them. Having said that, a lot of them, though, are also very… type… Interface type specific.
like, here's some stuff specific to MPLS. By the way, every single thing in here is an attribute that in the SNMP world is indexed by, the interface index. So, essentially, the equivalent of an interface name, description, what have you, but it is They're all identified, instances of them are identified by the same thing. So, And so then I wanted to start down this path of, I guess, you know, mapping them and what they would be like in… in the semantic conventions, and this is where I, as I said, you know, it's… it's doing a bit of… of research to come up with things.
the… First thing I probably wanted to talk about here is just thinking about the network interface entity itself.
I think already in other places, we do see network interface, referred to by the name, which I believe would be the correct way to specify it. Like, in SNMP world, you could argue that the interface index is the, you know, the correct, specific way.
But… you don't always have that for non-SNMP sources, but you tend to always have the interface name.
There are a few questions, though, I would love to have a little bit of feedback or advice on what y'all think.
In addition to these, so hopefully these are fairly, understood and straightforward. I don't know if there's any questions, I'm happy to answer them, but I don't have to talk about necessarily each specific one here.
But I think these were the obvious things, then, that would identify an interface. There may be a few other things that come up when we get into type-specific things.
You know, like, specific types of interface, some other attributes they may have.
Or not, but just now, from the generic ones, that would be the list I had. But, having said that, I do think there are some that… I was kind of on the fence on about, do we call these descriptive? Are they, are they, in fact, a metric?
For example.
That's a different example I want to talk about. When we get into things like the speed of the interface.
or the maximum transmissible unit, the MTU of the interface, or the MAC address of the interface. Now, the MAC address arguably probably should be, one of the descriptive things.
Cause it's… it is more of an identifier.
But, like, take the speed of the interface. I mean, is that a metric? Or… and there's probably two ways to look at this, there is… The maximum speed of an interface, what the hardware supports.
Okay, I would… you could certainly, I think, make the case that that is a descriptive element of the network interface.
But, say, for example, like, you know, probably the easiest way to explain it would be, like, your… your… if your internet connection at home, say you have, like, a… your router has a 1G interface, but you only have a 200 megabit per second circuit connected to it.
Well, technically, the maximum you're gonna get through that is 200 megabit. So, like, if you did, like, utilization metrics based on the fact that it was physically a 1 gigabit interface, when you got to… you know, 200 megabits of traffic, it'd be telling you you only have 20% utilized, which isn't really true. That interface is… is 100% utilized, because the maximum rate it's going to be able to do is 200 megabits. So, you know, and if you get something like a wireless interface, as signal levels and things change.
The maximum rate could change quite dynamically, just based on a variety of conditions, even if the physical capabilities of the interface are higher, you know?
So I kind of feel like if speed is a good example of one where you could have a debate, in my opinion, on whether that's descriptive, or it's actually more like a descriptive attribute of identifying something, or is it a, actually a metric itself, you know what I'm saying?
I don't know if anyone had any thoughts or comments on what I was saying there.
**Marc Netterfield** 16:54 So, I've seen it implemented both ways in, like, different tooling, over the years, and so I agree with you, it's a problem space, for sure.
And yeah, especially when you talk about the ones that are more dynamic, like wireless is a really good example, because Off of the signal strength, it will kind of negotiate bandwidth capabilities. And then you get into cases where people will have a carrier link, but they don't define the bandwidth statement on the configuration, and so they are functionally limited, but Like, their device won't let you know what that… it doesn't know, right?
True.
**RC Robert Cowart** 17:34 My feeling is here, is I would also want to take the speed.
And make it one of these descriptive… attributes over here.
But we have a separate metric, which, in telco world, they call it, like, a SER, like a committed information rate.
As kind of like, what is the actual… maximum bandwidth I'm capable of getting at the moment.
**Marc Netterfield** 18:04 Well, like, by configuration allowed to get, right?
**RC Robert Cowart** 18:08 Oh, sure, yes, yes, correct, yeah, yeah, yeah.
But would that make sense, you think? To do… to kind of split… split them up that way? Interface speed is more of a descriptive attribute?
**Stephen Lang** 18:27 So, the other thing that I'm thinking of, you've got, like, the… The link negotiation rate.
Which is your current active rate, which could change dramatically all the time on wireless.
The maximum theoretical rate of the hardware.
But then, where does bandwidth management come in?
Especially, like, with, I don't know, vSwitches and cloud providers.
Would you be able to dynamically set what the… The theoretical maximum could be, even if it's less than the negotiated rate. I'm thinking, for example, for traffic shaping.
how… how would that be captured? Would that be… Here, or… or elsewhere, because in that case… Would there be 3 different speeds that you're thinking of, which would be… You know, the theoretical maximum of the hardware, then the link negotiation, and then what's actually allowed through whatever traffic shaping profile you have.
And I don't know if that is the same as the link negotiation, or if it's independent.
**RC Robert Cowart** 19:34 So, first off, that does make sense to me. Maybe it actually is 3, Do you have any examples of where that data might come from?
Especially, like, traffic shaping or anything like that.
**Stephen Lang** 19:49 So… I mean, my head is kind of right now going to really about IOPS and disks, because I know with certain disks, you would, you know, potentially spend more to get, you know, faster disks.
And I don't know, because I haven't configured the vSwitches in something like, you know.
in AWS or something, and I don't know what the configuration looks like, but I assume that they have the ability to define links.
with, effectively, you know, different rates.
And if, I mean, if that's not possible now, I would assume that it's possible on some provider.
And I'm just wondering, like, where that would fit in, but probably… you know, maybe it's worth if I go in, try and find a concrete example of where this might be dynamically set.
**RC Robert Cowart** 20:38 So, so in general, and I'm… I'll talk, like, physical networks, which ultimately, at some point, the cloud providers are doing behind the scenes, probably, but, generally on a physical network, if I wanted to limit Bandwidth, in some way.
One, it's very possible you're only limiting it to certain types of traffic, of which class of service queues would be… You know, some type of, class of service mechanism would be how you would probably do that. But then, I would not consider that something I'd be thinking about at the network interface level. That's a whole other set of actual entity types, I think. A class of service queue.
which would be, like, contained by a network interface? Sure, absolutely, but it would be a little bit, Different of an entity type.
But yeah, maybe some more research there on that one. By the way, I only expressed half the debate, because you also got the thing of, even if we're talking physical interfaces.
Yeah, but it's a duplex interface, so it actually has that bandwidth in both directions, so when you say the speed, are you referring to one direction, or are you referring to both directions added together? Or, you know, like, it's… I've had so many debates in my lifetime over this dumb field interface speed.
But, I think what probably makes sense, just based on the comments made, is maybe there's a descriptive thing, which is whatever… The interface reporting… you know, whatever… however… whatever mechanism is used to report the interface, and what bandwidth it is capable of.
Is a descriptive item.
The actual bandwidth that it's currently providing is… Possibly something different, and that could be currently providing because of… that's just what it's configured for?
Or currently providing because the given state of the network has thus limited it to some particular bandwidth, right?
And that's maybe some type of separate metric, then.
**Sven Cowart** 23:02 The thing that comes to mind for me is… As a metric.
Is utilization the number you care about?
**RC Robert Cowart** 23:18 So, I would argue… Not always. In many cases, yes, for sure, utilization is probably, you know, is what people look at often.
I would argue, though, that if I had significantly especially if you're talking about wire, wireless networks, they're the ones that are going to be far more dynamic in the way they change. I mean, you know, a physical, like, say your internet connection, you know, given internet connection might be a 1 gig interface, but you have a 200 megabit per second circuit.
that's generally not gonna change that much, you know? But as soon as you get into anything wireless, that can be… highly dynamic. I mean, even on your laptop, you know, open up the signal, or, like, the Wi-Fi information, and just walk around the room or the office, and you'll probably see it changing pretty dynamically.
And if those are… I would certainly like to be looking at those.
from an observability perspective, to understand where I have poor coverage and dead spots in my environment, where maybe somebody… you know, who knows? In their backpack has something that's emitting signals that's devastating my Wi-Fi connectivity, you know? I mean, there could be a number of reasons why just seeing that number changing could indicate some condition of interest you want to look into.
So, in general, though, Sven, I do agree with you, utilization is the thing I care about the most.
**Sven Cowart** 25:01 Yeah, that makes sense.
I mean, I kind of see it as, the same thing as CPU. Like, CPU utilization has the same Situation.
And…
**Marc Netterfield** 25:17 land of ambiguity.
**RC Robert Cowart** 25:20 Turtle is that, Marc?
**Marc Netterfield** 25:22 Talking about, like, the ambiguity and how you measure it, or, like, what data point actually tells you how utilized you are, yeah.
**RC Robert Cowart** 25:27 Yeah, like, me telling you I had 978 ticks of Google Space doesn't really mean a whole lot.
**Sven Cowart** 25:35 Yeah, and CPU also has, like, right, like, with vCPUs and CPU limits configuration and all that, it has, like, weird dynamic nature to it where it can change on the fly based on the host configuration, and… So I think it's worth, in this particular case, I… I… where I'm going with that thought is I'm wonder… it probably makes sense we need to sync with, Braden, and he's not here today, so maybe when he gets back from his vacation, which is 3 weeks from now, to see what direction they're going with it on the systems and host entity.
Because we probably should have… mirrored representations of the… of… on that, or… or… not mirrored, but similar representation… similar ways to represent those things.
for the network and the CPU, right?
Huh.
**RC Robert Cowart** 26:27 Well, yeah.
**Sven Cowart** 26:29 Like, if they have utilization as a metric, then… and I'm not saying we don't have the other ones, too, but then we probably should also have a utilization metric.
**RC Robert Cowart** 26:37 Oh, yes, I don't… I don't disagree with that.
Yeah.
**Sven Cowart** 26:41 Yeah.
**RC Robert Cowart** 26:41 I mean, I would not… I'm pausing because I'm partially opinionated on both of those, because I generally… those are things that I consider to be highly dynamic metrics. We're, like, almost 0 or 100, and if your time slice is small enough, there's only two values, 0 and 100%.
So what matters actually way more is, in my opinion, in most cases, is some type of time and band, analytics, you know? Like, that my network was 100% utilized doesn't tell me something. That… 35% of the time, it was at greater than 90% utilization. Okay, that means something that I can maybe think about taking some action on, you know?
**Stephen Lang** 27:38 Yeah, so on the CPU utilization, this… Discussion has been going on.
Along, both system and the Kubernetes semantic conventions group as well.
And for Kubernetes, they pretty much just follow what is available from Kubelet.
And there was an ongoing discussion for a few weeks.
Around how to determine CPU utilization as a percentage.
Versus calculating the rate yourself.
And Robert, what you were just saying about the time window is, for me, the most important point, because if you calculate, for CPU at least, utilization is a percentage over time.
But what is that time? Because if you don't provide what the time window is exactly, and what the alignment is, and what the phase is, you can't accurately reproduce that yourself.
So I… my opinion is that I think it's better to provide the raw data and allow the users to calculate the rate.
Over whatever time that they want themselves on the fly.
Because of the whys.
If you provide a utilization percentage over time metric.
I think it's just too open to interpretation.
Because it could be that you decide that it's a 10-second window, or a 30-second window.
But what if you wanted a 15-second window?
then… You know, you're forced to use the raw data anyway.
So I think if you do provide utilization as a percentage over time, I think it's really important that you kind of document And specify what the time window Requirements are, and what kind of alignment you have.
Because unless it's something that's predictable, like you have You know, with the OTP codes.
Are you familiar with the protocol of, you know, when you get the QR code and you scan as, like, a multi-factor authentication?
And those codes refresh every 30 seconds.
But the spec defines that they refresh, effectively at the The 0 second, and the 32nd.
So it's not random… it's not a random point in time. It's based on, you know, the synchronized time. It's going to be the 0th, second, and the 30th second.
So, unless it's aligned to some, like, known universal.
like NCP is.
Then, you're just gonna get weird.
Data, in… just… in my opinion, so… the percentage over time, I think, is a difficult debate, and I would rather allow the users just to calculate it themselves, so you provide them You know, the… whatever raw data.
**Sven Cowart** 30:12 That makes sense to me. Is that the same… is that the same conclusion that the other groups came to?
**Stephen Lang** 30:17 So they, they provide both.
So, they give you the raw usage always, which is the CPU.Time.
But CPU.usage is a… is a percentage.
And they're currently submitting a change because it was badly aligned before.
So effectively, the hotel collector was running at… Whatever scrape interval was defined by the user.
And then Kubelet is hard-coded to run it every 10 seconds or something.
So, with Kubelet producing a new data point every 10 seconds, depending on when your 60-second scrape interval or whatever it was that you had configured, you would get the last known value produced by Kubelet, which could have been up to 10, sort of, 10 seconds ago.
So there was a load of, kind of, data missing, because if you wanted to aggregate over the last minute, you would have 5 data points missing.
So, they've… they are doing a change currently to align the percentage utilization of CPU to what Kubelet produces.
But again, I just think it's messy, because the alternative is you just look at the raw time.
And then you determine what your interval is, and you calculate your rate yourself.
So, that's.
**Marc Netterfield** 31:32 That's essentially how most SNMP-based stuff is working, is because SNMP, they do, like, bandwidth on a counter.
And so it's, you know, ever incrementing, and then you just divide it out by, well, how long since I checked it, you know?
**Stephen Lang** 31:46 And that, to me, makes more sense, because then it's explicit, and maybe people can use, you know, different time windows and intervals. That's up to them.
Whereas if you make a decision to provide a utilization metric, I think you should, at the very minimum, provide also the raw data as well.
But then the utilization metric should provide, sort of, very strict documentation in terms of You know, how the… and which window is used, so that you can understand what that is. And so the argument, Sven in the CA at STEMCOM to provide both was that the raw data, of course, is required, it's always necessary, but the utilization metric, some people found that that was useful just as a quick, at-a-glance check.
You know, is it… or is it 50%? Is it 0%? Is it 100%? I just want to know, like, a rough idea. I don't care about, you know, the specifics right now.
Brett.
**RC Robert Cowart** 32:39 But even at a quick glance, if you don't know the interval.
It's hard to interpret that number.
**Stephen Lang** 32:46 Exactly, yeah.
**RC Robert Cowart** 32:47 Just because it's…
**Sven Cowart** 32:49 What I just heard you say, though, right, is always 10 seconds?
**Stephen Lang** 32:53 In the case of Kubelet, yeah, but I mean, that could… I don't know, that could change in the future.
**Sven Cowart** 32:59 Yeah.
**RC Robert Cowart** 33:02 A lot of network devices, you won't be getting it that granularly anyway.
Because it'll otherwise, you know, they just can't, you know, have smaller compute capabilities and can't handle being, polled or in any other way have, have statistics collected. In fact, some, some network equipment, only even updates its counters at something like every 5 seconds, or every 7 seconds, or, you know, like… like it's not a continually updated number when you pull it, yeah.
**Sven Cowart** 33:36 But I don't think that matters in this case, because the metric here would be produced inside of The collector, anyways.
**RC Robert Cowart** 33:45 Sure, sure, but my point just being, if I look at it, like, and I say, oh.
you know, 20% network utilization. I'm totally fine. That's not the issue that I'm experiencing. Like, if you have users complaining about intermittent issues, you go, I'm only 20% utilized. You go, yeah, if you're polling, though, every 5… minutes, that could mean that you had big chunks at 100, and the rest of the time was almost zero, and it just averaged out to be, like, 20 or 30%, you know?
But it's… and it's the… I mean, we're not going to solve that problem. I guess. If operators don't know how to interpret those things, then that's a whole different issue, but yeah.
Okay,
**Sven Cowart** 34:29 I could just foresee, What, what, what's gonna happen, most likely?
And we can just wait until this happens, but… because I do agree, I mean, utilization is a flawed metric in some ways like this, where… especially where it's defined as a certain interval rate, predefined, not user-defined. I actually think it might have been a mistake to go away from user-defined in the collector, that almost seems more… Appropriate, because it at least allows the user to then configure that.
But, if someone has that on CPU, Usage, that metric.
They're probably gonna then open an issue at some point with the network.
Networking attributes to say, hey, can we just get a basic usage?
So, we don't have to do it now, but I foresee it happening, coming up.
**RC Robert Cowart** 35:21 If that does, though, I would still argue there's another part to that whole problem, which… so let me ask you this.
You have a 1 gigabit per second interface.
you're currently using 1 gigabit per second. What's the utilization of the interface?
**Sven Cowart** 35:41 100.
**RC Robert Cowart** 35:42 Well, it could be 100 in one direction, but a 1 gigabit interface is always duplex. And in the return direction, it's 0%.
Or maybe both directions are at half utilization.
You say, like, okay, we're going to use 2 gigabit per second, because we're going to take both directions, but I can't divide each direction by 2 gigabit. You know what I'm saying? Like, so then you're like, okay, then we need two utilizations, ingress and egress.
Right?
You get what I'm saying? Like, like, there's… either way you look at it, there's… there's sometimes a bit challenges there.
But, point taken. The main thing I wanted to get out of this is that, because I want to start thinking about entities here, which is just, like, which of these are more descriptive versus, you know… For example, like, where did I have it?
MTU, Yeah, you can… you can reconfigure that. It could change over time, but… For… for the most part, it rarely ever does.
You know, it'll get configured at some point in the life cycle, and then it's just gonna be what it is, you know?
you could argue the same applies to MAC addresses, but I think it's, you know, it… like, a MAC could be… probably does need to be also a descriptive attribute, on the entity itself.
all right, let me… let me move on to the other, kind of.
Just more of a question than anything else.
a little bit of an exchange I had with Braden a while ago, he… I think corrected a flaw in my original assumptions going into this.
which was that a lot of things currently in OTEL where you have, like, for example, in-out direction, or what have you, will not… like, I would have done something like this initially. I would have said, we have bytes in, and we have a whole other metric.
That is, bites out.
And my understanding is, no, that's not actually the way it ends up, Happening in most cases is that we would just have interface bytes.
And then that would have this attribute. Currently, what's in use is, like, network I.O. direction.
One of the… one of the Kubernetes things I looked at, for example, had this.
Is that everyone else's understanding? Am I… am I understanding that correct?
**Sven Cowart** 38:25 Yep.
**RC Robert Cowart** 38:26 Okay, which would mean, in a lot of the cases here on network, where we have, you know, like, ingress or egress bytes, it'll end up just being one metric, and we'll be, will have this I.O. direction part that has to be on it.
I was actually trying to think of that I.O. direction, like, should it be network interface I.O. direction?
because I think that I.O. direction is more referring to, like, in and out of an application, or in and out of a pod, or in and… but… I couldn't really come up with anything in my head that I thought direction might be different So it did seem to me like that's probably safe to reuse that concept here. So, so I just left it as it… as it was.
Then the other question that I had on this, that I'd be looking for any guidance There are a lot of things in network world, due to history, where you will have essentially two representations of the same types of information.
In the SNMP world, this has to go back, you know, 40 years ago when it was created, and 10 megabit per second interfaces were the new fast ones.
You know, it made 32 having only a 32-bit counter reserved, you know, or saved or conserved resources.
But as things got faster and faster, you get into the problem that, like, a 1-gig interface at full utilization can flip a 32-bit counter in about I think it's, like, 4.7 or 4.8 seconds or something. Pretty fast, anyway. And so… and now we even have, like, terabit interfaces. So, you know, you have these high-capacity 64-bit, numbers.
So, the first thing is, When there are these conflicting things.
or not, I shouldn't say conflicting, but basically two representations, historically, of the same thing. I would think we would just want to normalize these to the higher, to larger size representation. We have a limited number of data types for, for metrics, anyway.
So, any, any…
**Stephen Lang** 40:57 There was a question a few weeks ago around, the discussion of the OTLP.
And the data types that were supported.
**RC Robert Cowart** 41:07 Another one that I was going to ask also was about the counters flipping, basically. Like, we need to be able to get up to bigger than… the current by size, by floats, anyway. Go ahead, sorry.
**Stephen Lang** 41:21 Yeah, so I just wondered if that… if there was an answer to that, Discussion or investigation if the 64-bit counters were actually supported by the protocol.
Because I think, as far as I remember, we… Determined that, the maximum was… or was it that they were 64-bit, but they were signed?
Not on summer.
**RC Robert Cowart** 41:48 That, that is my understanding, is that they are signed.
**Stephen Lang** 41:53 Is that high enough capacity?
**RC Robert Cowart** 41:57 I'm gonna say no.
Just because, I mean, like I said, I mean, the current fastest Ethernet switches on the market are 1.6 terabit now.
now, that doesn't mean they're at full capacity all the time, but it's certainly possible In a… in a reasonable lifespan of a network switch to have Reached the most significant bit being set to a 1.
And… You know, that should not be represented as a negative number.
**Stephen Lang** 42:35 So, is this still an open question?
**RC Robert Cowart** 42:38 I would call it still an open item at this point.
**Stephen Lang** 42:41 maybe I'll take this as an action for myself, and to try and get to the bottom of this. Oh, I agree, yeah.
the… But when I looked at this briefly last time, I came to the conclusion that maybe the only way that we could represent this data is a 64-bit unsigned value.
was actually not using OTLP, it was using the OTEL Arrow protocol.
Over time.
But that would… Actually limit the usage of Whoever wants to implement these new network conventions.
to OTAP and not OTLP, which sounds a bit extreme.
I don't think I've heard of a case where that would actually happen anywhere else, because I'm not even sure if OTAP is… Defined as stable yet.
I know, like.
**Sven Cowart** 43:32 Yeah, it's not… they're still working on it.
**Stephen Lang** 43:35 Yeah.
**Sven Cowart** 43:36 Did move into the next phase, though, which is good to see.
**Stephen Lang** 43:40 Yeah.
**Sven Cowart** 43:41 I think by the end of this year, they're supposed to be stable.
**Stephen Lang** 43:48 Okay. Well, let me try and get to the bottom of this, and then what would be needed as next steps if we did need to… Add support or change.
OTLP for 64-bit insane.
**RC Robert Cowart** 44:02 Yeah, the only other thing I had thought about was that, you know.
in theory, right? Like, I set the most significant bit, so technically now that's a… that's a negative number.
If you were to interpret it straight away. But if the downstream application knows that in the schema, this is defined as a counter, which, by nature, can never be negative. So, if it encounters a negative number, and the attribute is a counter, then I have to interpret the bits in that as unsigned on the management application side.
Which, in theory, could work. My concern is, is there's a ton of tooling between those two points.
None of which may be aware of that nuance, and could thus mess the number totally up, you know?
**Stephen Lang** 44:56 Yeah.
**RC Robert Cowart** 44:57 So, yeah.
**Stephen Lang** 44:58 Yeah, no, I get that. You could just reinterpret the bytes, which is effectively just a typecast.
**RC Robert Cowart** 45:03 Yeah,
**Stephen Lang** 45:05 But it's kind of risky with it transmitting through different systems, like you said.
**RC Robert Cowart** 45:10 Yep.
Okay, no, that would be great if you would… if you'd take that item, Because we are definitely going to need it at some point. Or need to know what we're going to do. And the answer cannot be… oh, don't worry, just reboot your switches whenever that happens, you know? So, okay, Anyway, so then to further on my progress, I am going… like I said, I have all of the things for all the standard MIBs. I have everything that is… Currently.
indexed or identified by a network interface. Some of which, like, this is, like, wireless stuff, there's… there's a number of different interface Technology interface types that are in here.
And, here, like, you know, link aggregation interfaces, etc.
So…
**Sven Cowart** 46:16 war in the Middle East.
**RC Robert Cowart** 46:18 What's that?
**Sven Cowart** 46:19 Oh, sorry about that, I switched to the wrong tabs and it started playing a YouTube video.
**RC Robert Cowart** 46:23 Oh.
Oh, I didn't hear that on my side. Interesting.
So anyway, I'm gonna, continue to use interface as a bit of my first pass, as well as trying to figure out all the different things that we're gonna need to generate, and then I will go into the rest of the things that… and again, I'm focusing initially on IETF and IEEE-based standard MIBs.
And we'll… we'll move over to vendor-specific stuff afterwards, but I want to get a starting point with the standards.
And… And per… start producing, the entities.
for those as well. And then I will try to get them up ahead of time, so that everyone has a chance to review and give feedback in the future, but, you know, I am… I'm starting to make some progress now on some of these, so that's the main thing I wanted to pass on, and…
**Sven Cowart** 47:27 Where is this code being committed, or going to?
**RC Robert Cowart** 47:30 Nowhere yet, so that probably brings up another point, is… I can create some issues just on the semantic convention repo.
My question was, now that the project itself has been, merged.
are we going to be getting our own semantic convention repo, like the Gen AI stuff and some of the other things? I know that was discussed and…
**Sven Cowart** 48:01 We should… what we… what I want to get clarity on next call in the cement convention's call is, It, a key question is, because, like, something like network would still potentially be just in the semantic conventions repo.
Because what we said is core attributes would be still in the semantic conventions repo, but the specific network repo is all the specialized stuff that isn't considered core, and something like network interface feels like that's.
**RC Robert Cowart** 48:31 Sure, sure, sure. My feeling is, right now, I'm just gonna make… I'm gonna make it under, like, network, and then we can figure out, okay, now that we understand what they are, let's go see where we have overlap.
**Sven Cowart** 48:45 I'm having the same problem with the stuff I'm working on for this, is that I don't quite know where to put this stuff right now.
Can I, can I circle back on that point real quick? Because I want to just bring up something about the network interface.
or network I.O. direction. Right now, that is transmit and receive, not ingress, egress.
**RC Robert Cowart** 49:08 That's still the same, though. Yeah, send, receive…
**Sven Cowart** 49:11 Yeah.
**RC Robert Cowart** 49:11 ingress, egress, I think that has still a pretty clear definition in the context of a network.
**Sven Cowart** 49:18 The only thing I was thinking about is if you're talking about just, like.
Yeah, I mean, I guess it can still work, but it just feels a little weird, because transmit and receive, in the definition of the words, feel like, oh, these are… this is about usage.
Not about capability, but…
**RC Robert Cowart** 49:38 Well, if I'm talking, like, bytes in, bytes out, that is also bytes sent, bytes received.
**Sven Cowart** 49:43 Yeah.
**RC Robert Cowart** 49:44 You know, bites transmitted, bytes, you know…
**Sven Cowart** 49:46 If you're just describing the potential speed of a network.
interface.
if… I mean, I guess it still works, it just feels a little awkward.
**RC Robert Cowart** 49:55 Yeah, that is a little bit… How fast is your interface? Oh, it's 1 gigabit per second sent, and 1 gigabit per second received. Yeah.
**Sven Cowart** 50:05 So… but that… I just wanted to bring that up, because earlier you used ingress, egress, and I just wanted to make sure that we're okay with the fact that the words are transmit and receive. And it comes from Linux back, like, it's just the Linux stats that… where those directions came from.
**RC Robert Cowart** 50:24 Well, there's other… I mean, typically, you'll see in anything wireless, you'll tend to see send and… or transmit and receive as well.
Yeah.
**Sven Cowart** 50:35 Yeah, it's just weird, because ingress and egress, you do see a number of times in other things when it comes to just interfaces.
**Stephen Lang** 50:42 The lines on the board as well, on the PCB, tend to be TX, RX. On the actual PCB.
**RC Robert Cowart** 50:52 Yeah, it'll take me a while, it'll take me years of conditioning to move away from the terms ingress, egress, so… y'all will have to forgive me if that's what I say, so…
**Sven Cowart** 51:04 So the other thing I was just gonna share is what I'm working on right now, and I'm not done with it yet, but… and I had to reboot, so I'm not ready to show it to get on this call. I don't know why my internet just… Nothing was working. Rebooted, I was back, but, The thing I've been struggling with with this group is… a holistic picture of, okay, these are all the attributes we own. Now, let's list them out in a table.
like, in one page, so we can say, these are the things that we need to review and put attention on. And then from there.
**RC Robert Cowart** 51:39 We're saying the existing stuff?
**Sven Cowart** 51:41 Yeah, yeah, because, like, I… we need to start the process of reviewing the existing stuff so that we can start to figure out what goes where, what needs attention, what needs to be reworked, and And so I've started doing that, but I don't know where to put that file, so… I'm just gonna create it as a gist for now.
Or maybe I'll start creating the network. I can do it on my personal GitHub user account, just start creating the equivalent of the GenAI repo.
Where we have some of these things, and we can just all work on that.
For the time being, until the other repo's ready, but,
**RC Robert Cowart** 52:21 Do we know the process yet for the other repo? Is Braden chasing that down, or…
**Sven Cowart** 52:25 I'm working on it with Lyud Miller, but last time I said it should just be as simple as creating it, but it hasn't happened yet, so I don't know yet.
I'm trying to find that out next call, so… but I'm just letting you guys know, I might do it as a gist, depending on what that process looks like.
So, yeah. But we… because I also want to start creating the project board so we can officially track this stuff in a project board, and… I haven't done that yet because I don't have the repo yet, but we need the repo to create the project board, so… There's a number of things that just organizationally still need to happen.
It would be good for you, no matter what.
To create an issue.
**RC Robert Cowart** 53:11 To me, you're saying?
**Sven Cowart** 53:12 Yeah, about the network interface entity, so that we can start tracking it, and once the project board's ready, we can just pull it over.
**RC Robert Cowart** 53:21 Yeah. It's gonna take a while, though, actually, though, write all that. It's gonna be big. That's… This will probably be the biggest one that's… Yeah. Now, I might just start with the basics, the common stuff, and then we can add the interface type specific attributes later, but yeah.
Okay.
**Sven Cowart** 53:49 I think that's it then.
**RC Robert Cowart** 53:50 Yep.
Alright.
**Sven Cowart** 53:53 See you guys around.
**RC Robert Cowart** 53:54 Thanks.
**Marc Netterfield** 53:55 Catch you later.
**RC Robert Cowart** 53:56 Alright, have a good one. Bye.
**Giuseppe Ognibene | Coralogix** 53:57 My light?
