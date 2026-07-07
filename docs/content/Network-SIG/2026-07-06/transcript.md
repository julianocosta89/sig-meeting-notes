SIG: Network SIG
Date: 2026-07-06
Duration: 42 minutes
============================================================

## Zoom Recording Transcript

**Giuseppe Ognibene | Coralogix** 02:45 Hi, Sven.
Everyone.
**antonjim** 03:11 Everyone.
**Sven Cowart** 03:12 Sorry I was on mute. Hello!
How's everybody?
**antonjim** 03:21 Yeah, I'm good.
Starting the week.
**Sven Cowart** 03:24 Yeah, okay.
Are we there?
**RC Robert Cowart** 04:04 Oh, sorry I had Mike off.
Senator, are you running with this to talk about proposal?
**Sven Cowart** 04:12 Sure. Yep.
Do you have something to talk about, or…
**RC Robert Cowart** 04:19 I have a few things I've been thinking about, but, But you can go and talk about your thing first, and that's fine.
**Sven Cowart** 04:32 All right.
Oh, I'll just share my screen. Has everyone here viewed the… The proposal?
**antonjim** 04:49 Yeah, I took a look I have a comment.
But…
**Sven Cowart** 04:54 Something like.
**antonjim** 04:54 Looks pretty well.
**Sven Cowart** 04:56 Sorry I'm having.
I'm not at home right now, and… Not.
don't use Zoom, but I have an external monitor, and I can the window I'm looking for.
**antonjim** 05:09 Do you want me to, s.
**Sven Cowart** 05:12 Yeah, would you mind?
**antonjim** 05:16 Yeah, let me do that.
**Sven Cowart** 05:17 Oh, yeah, I got it. I got it Let me make this smaller because it's probably really hard to read.
Okay, So, Rob, I had a question for you, actually. Have you gotten a chance to look at this?
**RC Robert Cowart** 05:37 So, I mean, I did see that. I haven't written a response yet.
Yeah, quite frankly, I think that.
Well… So, so the, the, the few little items you have there, like DNS and this, to me, that's.
Okay, that might be, like, attribute items, but it's more… I'm think… the things in my mind are more around, like.
okay, you have the basis, right? You have, so let's say, network interfaces, then you have what would be called bridging or switching in SNMP speak. Then you have, like, spanning tree protocol, which is… and then you can get into routing protocols, and, like, that's where my head is in… when we're talking networky things.
And there's various, you know, entities, attributes.
metrics, what have you. So, Yeah, there probably could be a bit more fleshed out there, I think.
**Sven Cowart** 06:47 I think that's great.
**RC Robert Cowart** 06:50 But… and… and probably even… hold on, let me just step back real quick. I… I… we… there probably needs to be, because there's a good comment there, like, trace route and this and that, like, you know, what are even the different types of things we're talking about, right? There are… I like to think of it this way, there are… There's the things that forward traffic.
They're so like router switches, firewalls, like, you know, take traffic in. Then, based on some criteria, send it out.
There is network out elements of endpoints.
There's… the traffic itself, so this would be, like, NetFlow data, that kind of thing.
And then there is, what are the different ways that those things can be tested? Like… like, a trace route is not actually real traffic, but it is… elements, you know, or testing, doing some type of essentially synthetic test of the end-to-end path that traffic might take, right? So, so there's, like, these handful of buckets of things, and within those, there's going to be entities. This is maybe kind of getting back to then where you asked me at the beginning, you know, if I had anything to talk about, is that I've actually been thinking about some things, and it's mostly That, I feel like there would be some good value in.
Having a call that just focuses on discussing some of those things and getting everyone on the same page.
And it doesn't… and I would expect that list not to be comprehensive of all of networking.
kind of along the lines of what I was suggesting last week, that to start with, we focus on data center networking. So, like, if someone's like.
Okay, they want to do gigabit passive optical network, you know, like fiber to the home, fiber premises, stuff like, nope, not data center networking. We're not doing that in the first pass, you know. I mean, if someone wants to submit something, they can always submit something. But my, but like our strategic focus beyond, say, data center to get started with, you know.
I see Matthew's joined as well. He also had a lot of stuff around the entities, you know.
**Matthieu Noirbusson** 09:05 -H.
**antonjim** 09:06 Mac… And coming here was more in the direction, like.
network is quite broad, and we cannot put the list all the technologies, entities, devices that we want to. I mean, they will come on different priorities, on different customer requests, and so on. But as we are putting here, like, short-term, mid-term, and long-term, from my perspective, in Cisco ThousandEyes, those things we are already doing.
We have some sort of proposal that is some sort of internal, not put in any standardization. That's why I think it would be great that we talk about them in the future. I'm not saying we have to do it at the beginning, but at least in the middle term, we can talk about We have those synthetic trace routes, like it travels hop to hop, and then see where we are spending the highest delay, or if there are timeouts, which IPs, which ASN. So all those data we're already doing, it would be great to create some sort of stabilization.
And the same for BGP. For us, it's one of the key in Cisco, like… how many praxis are being advertised, or withdraw, or routes have been updated. All those things are quite important for our big, big customers, so if we find out some standardization there also, that would be awesome.
That's what I proposed there.
**RC Robert Cowart** 10:19 Well, and that is a fair point. The… when I would say routing protocols, I was kind of counting BGP, but some of these things are not just data center, they're also, like, WAN-type stuff. I guess maybe my perspective would be, or my suggestion would be, and I don't know where you see the need, but, like.
I, when I think about WAN, I think about it from two sides. I think about the customer's side and I think about the provider's side.
And, so, say, for example, you know, like, I'm a service provider providing Layer 2 VPN services over MPLS backbone.
That's important for me to know as the service provider. It's completely irrelevant to the end customer. All they care about is, you know, I have X amount of traffic or X amount of quality over different class of services, et cetera. You know, you know what I mean? Like, like the two perspectives are completely different.
And, and so, I'm just wondering, does… like enterprise WAN, in other words, not provider-side WAN, but enterprise WAN, does that cover most of the use cases?
Because that is a dramatically less complex part of WAN than the provider side, in my opinion.
**antonjim** 11:47 Yep.
**Sven Cowart** 11:52 So, I'm trying to figure out what that means for this proposal specifically.
**RC Robert Cowart** 12:00 If you would like me to add something, I can add something a little bit later today.
**Sven Cowart** 12:05 Okay. Yeah, that's fine.
**RC Robert Cowart** 12:07 In fact.
**Sven Cowart** 12:08 I think, though, there's two different things here. One is about, like, just providing attributes.
And then there's the other one about under figuring out what the entities are.
Or do you guys see those as closely related?
**RC Robert Cowart** 12:26 I, I see them as basically the same thing, like you got to kind of do them in parallel, I think.
**antonjim** 12:32 Most likely, yeah.
**RC Robert Cowart** 12:33 I'm I'm sorry. Go ahead.
I'm differentiating also when I say, like, the attributes are closely related. I'm not talking about, like, the metrics and those… I'm just talking about, like.
Yeah.
you know, you had, like, a VRF, a virtual route forwarder, right? Like, a virtual router.
How do we identify virtual routers? That, like, that part of it, like, what are the identifying mechanisms and stuff? For, for a network interface, what are the identifying things? We need to know that first.
Then we can, you know, then it becomes a little bit easier to say, okay, what metrics does an interface have, what log messages might be, et cetera, et cetera, but just that entity and the attributes that identify those entities.
And then there's relationships that go with that, but, and the entity work, but.
That part of the attributes to me seems very, related work, like, it's hard to do one without the other, I think.
**Sven Cowart** 13:41 Sure.
Okay, so I think then it makes sense, even as a near-term goal, that we need to start banging out that Design.
very soon.
Because if, in your mind, this is blocking other things from happening.
**RC Robert Cowart** 13:59 It's packed.
**Sven Cowart** 14:00 I can understand why you feel that way.
I think some things we can move forward, especially in this near-term list, but… Yeah, and by the way, I'm not the right person to bang out that… that design. So, I know, Matthew, you've had ideas that you've shared some gists. So… I do think your call out.
is good. Can we plan to… One, someone needs to create an issue. Well.
I was gonna… Matthew, I was actually gonna tell you to create an issue, and then I realized, wait, if this project gets accepted, then we're gonna have our own project, and it probably needs to be in that project, and then transferring the issue over is gonna be a mess, so… Maybe not yet, but can we plan for the next week to have that conversation that you want to have, Rob?
**RC Robert Cowart** 14:52 Yeah, I think that's fine. I would not mind, Well, shoot. Yeah, this, this has been a little bit my challenge as well. Like, where, where are we putting stuff for right now?
**Braydon Kains (Google)** 15:05 OpenTelemetry GitHub admins can move issues across repos, so I think it is… if we just start in the semantic conventions repo, I'm pretty sure that they can just transfer it to our new repo when that's ready.
**RC Robert Cowart** 15:21 Okay, then then maybe we should take. Let me go back over to the document here.
**Sven Cowart** 15:26 I think someone just needs to create an issue about network entities then in semantic convention repo.
And who is.
Braden, would you be… are you in the entity SIG?
**Braydon Kains (Google)** 15:44 I am not in the entity's SIG. Okay. It overlaps with two other meetings for me.
But if… It's… do you need me to go to that meeting for something?
**Sven Cowart** 15:58 No, no, no, I think one of, I mean, I really think Rob or Matthew, one of you two, because It seems like you two are… Or even Antonio with it.
It feels like someone needs to start attending the entity SIG regularly.
**Braydon Kains (Google)** 16:18 I might be.
**antonjim** 16:18 It's a goal, because every… What is the goal? Because the entities that we are going to propose are going to need to be approved by then, or is it just to align more?
**Braydon Kains (Google)** 16:30 The way I see it is that, like, we need to be involved with the entity SIG for cases where we feel like the entity model isn't supporting what we actually want.
And this, this is happening in System 2, where we… We're… We're finding some scenarios where what entities has right now properly specified doesn't effectively cover the things that we need to disambiguate. There's some things about process and executables. There's some things about hosts that could be cloud instances or could be Proxmox or something else, like different classifications of the same thing.
So, like, I also need to be in the entity SIG. I think I can find a way to deconflict and make it to that SIG. I also work with the sort of person in charge of that SIG. He's also a Googler.
So…
**Sven Cowart** 17:18 Okay.
**Braydon Kains (Google)** 17:19 But…
**RC Robert Cowart** 17:19 Oh.
**Braydon Kains (Google)** 17:20 If someone else from the SIG can also find a way to attend that meeting, it's at 1230 Eastern, so what is that?
**RC Robert Cowart** 17:29 I've got… I've added it to my calendar now. It's a… Okay. Looks like… looks like Monday is just gonna.
**Matthieu Noirbusson** 17:35 That's.
**Braydon Kains (Google)** 17:36 That's how it's turning out for.
**RC Robert Cowart** 17:38 Okay.
**Sven Cowart** 17:41 Okay, great.
That's helpful, because one of the asks from Ludmilla was also that we list who's representative of the SIGs that we need to collaborate with, so…
**Braydon Kains (Google)** 17:55 Yeah, you can put me down for the system group one.
**Sven Cowart** 17:58 Yep.
**Braydon Kains (Google)** 17:59 Okay.
**Sven Cowart** 17:59 Got it.
Thank you.
Alright. So sounds like the plan, then, is next week we will have some type of entities design discussion.
It's probably best to come with something prepared, not just start from scratch. Yeah.
**RC Robert Cowart** 18:17 I was going to ask Matthew if he maybe has some time this week that he and I could sync a little bit on some things.
**Matthieu Noirbusson** 18:26 I think we have to think about entities.
two topology topics, I think.
But I'm sorry, but I won't be here for two weeks, so… I'll let you work on that.
**RC Robert Cowart** 18:45 Okay, you had a few things you had said that you had already kind of had some work around, though, right?
**Matthieu Noirbusson** 18:52 Yeah, yeah, yeah, I bet it's, It's a tool that we are working on, not really in production.
So, we… we start to think about that, and And we try to share. I'm quite new on this exercise. This is my first participation to a SIG, so… I first listened to you.
And, when…
**RC Robert Cowart** 19:24 I've only been hanging out on different ones for about two months myself, so, I think that's why we have, you know, other folks on here to help guide us as well. So, I mean, my feeling, quite frankly, right now, is I'm just going to start recording information and thoughts and ideas, and then we can… Shape it into the hotel way as, as we learn more. That's kind of what my approach is going to be. So.
**Sven Cowart** 19:51 I'm going to link to this document so it can be easily referenced. Rob, have you had a chance to look at that yet?
**RC Robert Cowart** 20:00 I have not yet, no, but I…
**Sven Cowart** 20:02 Okay.
**RC Robert Cowart** 20:02 I can do it. I can do it this week, so.
**Sven Cowart** 20:08 Okay.
**Matthieu Noirbusson** 20:09 Okay, thank you.
**Braydon Kains (Google)** 20:11 I can try to help with any questions about, like, general entity data model stuff, since we've had to model a few complicated things in system, too.
**RC Robert Cowart** 20:22 Got it. Okay. quite quite frankly what I'm just gonna try to get.
until, get done till Monday, is just try to get, like.
some thoughts around. I think a little bit that me and Matthew have shared. I think we're at least Generally speaking, in the same direction in our thoughts, so… but my feeling is just, I'm just gonna record as much as I can, and then we can… Try to see how it gets shaped from there. So.
**Sven Cowart** 20:53 And the other thing to just call out here is that, request, Ludmilla requested that we also take on the DNS area, which makes a lot of sense.
**RC Robert Cowart** 21:00 Oh, okay, yeah, yeah.
**Sven Cowart** 21:01 There's…
**antonjim** 21:02 Okay.
**Sven Cowart** 21:03 Not much.
**antonjim** 21:03 You need to be a.
**Sven Cowart** 21:04 Right now.
Yeah.
**Braydon Kains (Google)** 21:06 I think those were added inadvertently by groups that weren't necessarily network experts, but needed those specific DNS things.
**RC Robert Cowart** 21:16 Sven, I don't know if you know this, but in our internal Codex repo.
By the way, for those who don't know, but way before XAI, right, Codex was actually, or is that OpenAI that's Codex? I don't remember. Anyway, we had our own Codex before then.
But I actually have, like, I see DNS answers is, like, a top-level thing. Like, I literally… every… already every single DNS structure that can be that's part of the DNS standard we already have broken out. It's… we could… so, essentially, what I'm trying to say is, we could do some of that just for, like, actual DNS traffic itself.
You know, digging into it, we could have a pretty quick starting point there, I think.
And.
Some stuff will rename and things like that, but just, like, the work has already been done to… to break apart all the data structures and all that, as far as DNS traffic goes.
**Sven Cowart** 22:17 I do, I, I do find it interesting that.
That's its own area, not just within the network area.
Brandon, do you know why that happened?
**Braydon Kains (Google)** 22:27 why DNS was given its own spot instead of being under network? Is that the question? Yeah.
I don't know, my guess is that it was… the network area may not have existed yet.
**Sven Cowart** 22:43 Okay.
**RC Robert Cowart** 22:44 What, what I don't see on this list as well, as soon as you say DNS, I think that pretty much means also, you need, we need to take on DHCP.
Umm.
You know, it's just being generally related. Exactly.
Oh, yeah. Like, there's not even one, but like… Yeah.
You know, because if you think about, what do I need for a network to work?
I need an address. Okay, DHCP. I need to be able to resolve names. Okay, DNS. I need… you know, so, like, there's… there's these kind of foundational pieces that… Certainly endpoints will need before they even communicate on the network. Right? So if you're gonna if they're asking for Dns, we might as well include Dhcp to go with it.
So, yeah.
**Sven Cowart** 23:28 Yeah, they.
No, it just it made me wonder about.
And I'm gonna bring this up in the semantic convention's sake, but I'm going to wait a little bit until the project starts off. But for these things that we have, when should they be new areas that the network just owns or top level, meaning they're top level, or when should it be a network dot attribute?
**Braydon Kains (Google)** 23:58 Yeah, that might be up to us to decide, I think.
**Sven Cowart** 24:01 Okay.
**Braydon Kains (Google)** 24:02 Because the network areas is… has always been kind of nebulous, like, as a system group, we've used it.
For things that used to be called system.network, but we sort of… Changed our model and a lot of places, a lot of other areas have changed the model from like, it used to be.
The first name is just, like, the group who owns it.
Yeah. But then it just meant that the system namespace was a dumping ground for a ton of stuff that wasn't necessary, and so we… we sort of remodeled so that the system namespace is for anything that's actually about, like, a… like a box, like a… like a… an OS, if you… so, like, if it… Got it. We have system.network, that's for things that are about, like, an operating system's network statistics, or, like, networking devices on the system or something. I don't remember exactly… we might not be following that rule quite right, but that's, like, the way I'm thinking about it.
**Sven Cowart** 24:56 Okay.
**Braydon Kains (Google)** 24:57 And then network is for things that are generally about networking.
In general. I don't think we're following that rule super well right now, though, because I think we have a work.interface In… in the network… namespace instead of system network interface, and so we have, like, network interface name, but that's just, like, the device name on Linux is how we're using it, so that might not be quite right.
**Sven Cowart** 25:25 Mmh.
**Braydon Kains (Google)** 25:25 It is kind of up to us, though, exactly how we handle this. Like, for DNS, I am… I don't see why network.dns would be wrong.
Hmm, yeah, I don't know I'd have to think about that a little bit, but…
**Sven Cowart** 25:49 Same. I think I can argue myself in two different directions. Yeah.
**antonjim** 25:52 Right, that's.
**Braydon Kains (Google)** 25:53 That's most semant.
**antonjim** 25:54 How do we…
**Braydon Kains (Google)** 25:55 It was like that.
Sorry, intent.
**antonjim** 25:58 Brandon, Brandon, how?
How do we solve the problem of, like, for example, in ThousandEyes Cisco, we have been using DNS questionnaire. I put it in the chat also. There are DNS metrics. We have been using them for, like, kind of 3 years already, and they have been on stability development.
I imagine other companies are also doing that, I mean, using metrics that are in stability, development, and so on.
If we move now, just because we are creating that new network group to network.dns, which I'm not against, I'm saying that.
Is it that the plan that we are gonna start?
deprecating things and then moving to the new, or are we gonna try to stabilize the existing one, like, because I… I have the feeling, like, for the things that we kind of agree, like, for example, the other day, we totally disagree about the year address and local address and those things, which… it's fine, but for those things, if the only thing that we want to do is maybe add network.
I am a little bit… thinking that maybe we should not deprecate and create a new one, because that has been used already for a long time. Yeah. For customers.
**Braydon Kains (Google)** 27:01 Yeah, this is a philosophical hotel question, it's all over the place. It's happening a lot in the collector, of like, this thing is not marked stable, but it's been used for so incredibly long that we're not gonna rock the boat now. It's stable by, Kris "Cowbert" By virtue of it just having existed for so long. There's a word.
**RC Robert Cowart** 27:22 backdoor standards.
**Braydon Kains (Google)** 27:23 De facto, there it is.
**antonjim** 27:26 So maybe.
**Braydon Kains (Google)** 27:26 It's a philosophical question that our group can answer, of, like, how much do we care about something that we feel is de facto standard now? That might influence our decisions, so the fact that DNS… these metrics are still in stability development, but they've been heavily used by people for so long. Like, I think this… these were introduced, like, before the semantic conventions repo even existed. Like, back when it was part of the specification repo. Like, it's been a very… these are pretty old, as far as I know. And we could say that that influences our decision to say.
DNS.
Can remain in namespace, because… these attributes, even though they're stability development, have existed for so long that we feel they are de facto standard, and we can sort of build our decisions around that. I like the sound of that, and I always try and lean that way whenever I'm doing anything related to Semconf, or, like… like, in the really heavily used collector components, but it is… kind of up to us. Once we take ownership of these namespaces, it is also, like.
Our prerogative to say these are marked development, people.
theoretically should have expected that they could be… have the rug pulled up from under them, even though I think that's kind of unfair, but… It would be within our rights to say that, if we decide philosophically it's more important for us to organize it in a way, now that we have proper expertise fully owning the area.
I think that's… we take a vote, or we just sort of decide as a group which direction we want to lean.
**RC Robert Cowart** 28:57 I I mean, I would agree that it makes sense. There's no, there's no need to to change something just for the sake of changing something. Yeah.
But, I am a little surprised that there's not, at least it sounds like there's not.
Some type of established principle of, like.
you know, of where you'd like deprecate, but things really should support both for a period of time, but will quit supporting the old one, say, 24 months after it's been marked deprecated or something.
**Braydon Kains (Google)** 29:29 So that philosophy exists in the collector.
The… the way we handle it for the collector is… We have a bunch of, like.
we came up with tons of metric names before semantic conventions existed. And so when our… when the metrics we produce start to adopt semantic conventions instead, we… have, like, a double write period, where you can write the old and the new schemas at the same time, and then, like, slowly transition your dashboards. But I don't think that sort of principle exists at the semantic conventions level. I think they consider that to be… Up to implementations, like SDKs.
**Sven Cowart** 30:15 Makes sense.
**Braydon Kains (Google)** 30:16 SDK is consuming semantic conventions, but…
**RC Robert Cowart** 30:19 I guess there's versions on the semantic conventions as well, right?
**Braydon Kains (Google)** 30:23 Yeah, that's, that's the other thing, too.
**RC Robert Cowart** 30:26 So if you're if you're developing a product, you're gonna say, like, we support these versions. And that's kind of up to the the person creating the solution at that point, I guess.
**Braydon Kains (Google)** 30:37 There is supposed to be also… I don't know how well it works, but there is supposed to be some, like, auto-migration for, like, if there… for simple changes, like… like, like, renames or attribute renames are supposed to be, like, a migration from one schema to another, but I honestly have no idea how well that works, and whether it's still, like.
**antonjim** 30:55 Okay.
**Braydon Kains (Google)** 30:56 very well maintained or not.
**Sven Cowart** 31:03 Braden, how.
**antonjim** 31:04 Too soon.
**Sven Cowart** 31:04 Does it ever become a problem for you and the system, Sig, that systems just becomes a dumping ground for things? Because in my mind, the way I was kind of just thinking about this problem is that I almost prefer creating more areas instead of just dumping everything into network.
But… Like, for instance, the flow attributes that we wanted to add would probably just be best in In the net flow, or flow… Area instead of network.flow and then dump everything in there.
it…
**Braydon Kains (Google)** 31:35 Yeah, I… I sort of had this… this debate with the maintainers probably two and a half, three years ago, where I… I wanted more areas because I didn't like how cluttered the system namespace was becoming. And this is also… there was, like… a question of, like, we have lots of attributes and metrics that are specific to particular operating systems, so, like, this is a Windows only, this is a Linux only, or Unix.
**Sven Cowart** 32:00 Mmh.
**Braydon Kains (Google)** 32:00 Or whatever. And exactly how we organized those namespaces was, was also… an issue, and I think there was some worry about the… The directory sprawl becoming too much, so… You're talking about, like, we have a system… Directory area, but we can have multiple files within that that, like, have… That, that… Present the information better on the website, so even though system the system namespace ends up being a dumping ground. We could… you can change how the markdown looks that gets rendered to the website, so that.
**Sven Cowart** 32:38 the map.
**Braydon Kains (Google)** 32:39 public documentation, like, looking at it is organized the way you want, but still, like, under the hood, the.
**Sven Cowart** 32:46 There you.
**Braydon Kains (Google)** 32:46 maintains a certain way of working, where the YAML file for a system ends up being gigantic, but we could theoretically present The different subspaces of system dot something.
In a nicer way on the website, which we don't, but we could.
I think it depends on the… whether we think the problem is about information presentation, or just, like, our own maintainability, and that kind of changes how we want to… How we want to tackle it.
And in terms of root namespaces, like, if this was network.dns versus just dns, I think we could still… We could still organize it in a way where the… we have a network folder, and one, like.
Registry.yaml file, but… Not everything in that folder has to be network.something.
So we can still consolidate everything we own into the same area, but.
Make our own choices on the namespaces, and… and how we present.
The information on, like, this generated… Semantic conventions, docs I think there's ways around it. I don't know if there's a general preference on there being more root namespaces or not. My personal preference is more root namespaces in a way that makes… in a way that makes sense. Like, we have process and system and network and memory and things, and so, like.
when would something go in system.memory versus memory? My thinking is that if this is a metric about a RAM stick, or whatever, like, if that's the way you're thinking of it, then it goes in memory, but if it's about the operating system's memory management, it goes into system.memory. And I try to… I try to… think of things in that sort of model. So for network.dns, I like DNS being the root, because network is kind of implied, like, when is DNS ever not going to belong to network? I feel like that's… it's significant enough to be its own root area.
**RC Robert Cowart** 34:53 My, my.
**Braydon Kains (Google)** 34:54 I really could go either way on that. You can always find an argument for one way or the other equally.
**RC Robert Cowart** 35:01 My, my tendency is also to favor more high level as well.
**Sven Cowart** 35:10 So what I, what the way I'm processing all that information is that.
How we decide to group and how we decide to the entities that we.
decide to… Contribute will also inform if there needs to be new namespaces or not.
**Braydon Kains (Google)** 35:33 I think so. I think… I think we're the… the SystemSig is the only one that's really running into this sort of, like.
Hierarchical way of thinking about namespaces right now.
Since a lot of the others, like, at least the other stable SimConf, are, like.
Or, like, just, like, information about an area, and very span-focused.
So it's just, like, HTTP, like, yeah, if it's about HTTP, it goes in the HTTP namespace. Yes. Or databases is the same idea.
But now we're talking about… the system group is probably kind of blazing a trail in terms of, like, we have really, like, almost object-oriented, if you want to think of it that way, like.
we're really centered around, like, metrics about something, or about, like, an area, a sub-area of something. And so we're kind of the first ones thinking of root namespaces in the particular way that we are.
But I think, you know.
I think it works okay, Yeah. It probably could be applied here in a similar way, where the root namespace, the… basically, it… the root namespace is not, like, what group owns this, it's about, like, what significant area of… Absolutely. Something is just about.
**Sven Cowart** 36:51 Yeah, I agree. So the question is, what are the significant areas for us?
And… We can figure that out.
**RC Robert Cowart** 37:00 Initial list.
**Sven Cowart** 37:02 You what?
**RC Robert Cowart** 37:03 I can work on, like I said, from that other question you asked me earlier, I can work on an initial list.
Here within the next few days, yeah.
**Braydon Kains (Google)** 37:13 I think the way we can think of it is… if… if there are… If there are attributes that.
Are sim… are, like, shareable… Across… Different.
significant networking areas.
Then network is a good namespace for those things.
It's almost like a utility namespace, like, if it's going to be used in different sub-areas.
Then network is a good spot that all of them can sort of refer back into.
**Sven Cowart** 37:48 Yep, that makes sense.
But… Alright, and otherwise, it's, some small minor comments, and then about How do we target or what are we need to target stability for?
the things we're working on, which I totally agree with. I think it's a great call out. I didn't think of that as part of the project proposal originally.
I think it's going to be hard to do that until we get a little bit more concrete on what the actual items that we're going to be proposing on.
Yeah. But…
**Braydon Kains (Google)** 38:22 if you want to, like, make it… make it clear what we mean by targeting stability, I think the important thing for stability that sometimes gets sort of swept under the rug is that to mark something stable, you need to prove that it works under an implementation. So if we talk about how we are consistently, like, making changes to our semantic conventions in conjunction with, updating instrumentation that uses it, we can target stability easier because we're constantly proving our own implementation, I think.
**Sven Cowart** 38:53 Yep.
**Braydon Kains (Google)** 38:54 Proving our conventions via implementations.
**antonjim** 38:58 There is something quite important that, Brendan, you just mentioned here, who is.
Instrumenting the network and using… who is gonna use them?
who is going to use those telemetry semantic convention that we are going to propose here, because that is important, because they are not going to be finding some correlation instrumentation language. Maybe OEI is going to do it.
Josep is here, and he has also even proposals for network flows, if I'm not mistaken. But who else is it going to be? Because we might need to work closely with them. I know Elastic Flow or Fiscal Thousand Eyes more as a proprietary thing, we'll try to adapt to them, but we also need some standard groups, like OBI is a really good example, honestly, doing those, right?
Or to work with them.
**Sven Cowart** 39:46 So, that is the plan, is OBI is one of them, one of the vehicles, and the other one is the contributions we want to make in the long term.
Deliverables around… Proper receivers for Flow, SNMP, and Trap.
And.
**antonjim** 40:02 I really understand.
**Sven Cowart** 40:03 Maybe there's more, you know, but we'll control that, those components that we add there. So.
I think that's how we'll get.
**RC Robert Cowart** 40:13 Yeah, we we need to take a look at what's there first.st But if there is a deficit, we're certainly prepared to contribute some stuff there. So.
**Braydon Kains (Google)** 40:25 Those collector receivers, at least, are very sparsely maintained, and I think sparsely used. We don't have proper data, but… Those could be a good spot to adopt the semantic conventions. Probably not, like, a wholesale breakage, but, you know, like, using the migration strategy that other receivers are using, migrating those to… a newer implementation.
**Sven Cowart** 40:54 Okay, I think that's it from So I'm, this PR.
Rob, is there anything else you'd wanted to… Bring up, or was that the entity's…
**RC Robert Cowart** 41:06 No, that was the main thing, is just like trying to get pragmatic, but the but that's okay. I'll just. I think the best thing is, I just need to make an initial draft to spark the conversation, and then we'll focus on that next week.
And, yeah, so… Basically, Sven, it'd be helpful if you kick me in the butt once or twice this week, and make sure that I… with the other things going on. I only have one other high prior… really high priority item this week, but, I should be able to dedicate, you know, a little bit of time, so… Well, say, actually, good couple days, anyway.
**Sven Cowart** 41:48 Sounds good.
All right.
Thank you very much. Good to see everyone.
**Braydon Kains (Google)** 41:52 Nice to meet you.
**Matthieu Noirbusson** 41:54 Thank you. Bye.
**Giuseppe Ognibene | Coralogix** 41:56 Yep. Okay.
