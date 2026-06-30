SIG: Network SIG
Date: 2026-06-29
Duration: 49 minutes
============================================================

## Zoom Recording Transcript

**Giuseppe Ognibene | Coralogix** 00:34 Are there one?
**Sven Cowart** 00:35 Hey, good morning.
**Giuseppe Ognibene | Coralogix** 00:38 Morning.
**Sven Cowart** 00:42 Is it, could one of you… Go to next week in your calendar, and see if this meeting is… 3 hours later.
It is for you, Steven.
**Stephen Lang** 00:54 Yeah, I noticed that only.
**Sven Cowart** 00:56 Okay.
**Stephen Lang** 00:56 Only this meeting today appears to be at this current time. Yeah.
**Sven Cowart** 01:03 Braden to fix that.
**Mario Macias** 01:13 Hello everybody.
**Sven Cowart** 01:15 Hello.
Good to see you, Mario.
Mario.
Where are you coming? Where are you joining from? Spain?
**Mario Macias** 01:26 Yes, Barcelona in concrete.
**Sven Cowart** 01:29 Cool Very nice.
Let's wait a little bit further just to join.
I'm expecting at least Rob.
And hopefully Braden to join as well.
Hey, Rob.
You're muted.
**RC Robert Cowart** 03:26 Yeah, I said, sorry for being a couple minutes late.
**Sven Cowart** 03:37 All right, well.
We'll get started. Hopefully Braden decides to hop in. We did notice that the call is at the wrong time next week, so.
Somebody will have to adjust that who can do that, which I think is just… Either Braden or you, Mario, at this time. Oh, there he is.
**Braydon Kains (Google)** 03:57 Hi, sorry about that. How's it going?
**Sven Cowart** 03:59 Very good.
Good morning.
Or afternoon.
**RC Robert Cowart** 04:04 Is it the wrong time next week? On my calendar, it's the right time.
**Sven Cowart** 04:09 Three hours later for me.
**RC Robert Cowart** 04:11 So, so what was interesting, I don't know what happened, but when I, you know, because usually I bring up the OTEL calendar, and then I, like, duplicate onto my calendar.
**Braydon Kains (Google)** 04:20 Yep.
**RC Robert Cowart** 04:21 And every time I did that, it was creating it like 3 hours later.
**Braydon Kains (Google)** 04:25 I…
**RC Robert Cowart** 04:25 I manually moved mine, I don't know what was happening there.
**Braydon Kains (Google)** 04:29 mine up. When I… when I made… when I tried to move the meeting, I didn't realize… because, like, all my other calendar calendars sync to my local time, but the hotel calendar is always specific, no matter what. So I got confused, and I set it to what I thought was supposed to be in Eastern, and it was screwed up, and then I fixed it for this one, but I clearly forgot to check the weekly on Monday thing. I see. So I'll fix it after this. This is gonna be the right time for the…
**Sven Cowart** 04:59 Okay.
**Braydon Kains (Google)** 04:59 It's just… I'm just terrible at using Calendar, apparently.
**Sven Cowart** 05:03 Yes.
**Mario Macias** 05:04 Okay.
**Sven Cowart** 05:06 Sounds good.
**RC Robert Cowart** 05:07 Then I think you and Braden got a lot in common looking at all that music gear in this background.
**Braydon Kains (Google)** 05:12 I have a few too many things back there, that's for sure.
**Sven Cowart** 05:16 Alright.
Alright, we got 3 things, I think we can get through all 3 of them, so we can just start at the And Rob, I'll let you kick it off.
**RC Robert Cowart** 05:26 I mean, mine's a little bit more digging into details if there were more community things I'll cover first, but, you know.
**Sven Cowart** 05:32 That's… That's fine. So I wanted to just really quickly… Oh.
And I apologize, I really do, that this took me way longer than I wanted it to take.
I was… Very sick last week. And Couldn't do anything all week long. I'm still not 100% today, but I'm getting closer. But I did want to — so this morning, woke up, just quickly jotted down.
my thoughts around the objectives, and for us to at least agree on the objectives, you can ignore 80% of the text around a lot of these things that I want to, point out, because it's still just me jotting down ideas so that I continue to flesh out this project.
template, by the end of the day, and then get that opened.
But the thing I wanted to, yeah, so I just wanted to make sure that we're all on the same page about.
Kind of the objectives that we have, which is, one, to expand and clarify and maintain the semantic conventions within the network.
Area.
Does that sound right?
**Mario Macias** 06:39 Sure.
**Sven Cowart** 06:41 Two, define standard semantic conventions for traditional network telemetry methods. That includes things like define network metrics, trace span, define standard SNMP metrics, define SNMP trap log structures.
And then objective three is to improve the usability of network related OpenTelemetry collector contrib receiver components.
There's, the S&P receiver and the NetFlow receiver.
Neither of them are standardized to.
The semantic conventions, they kind of add their own things in and there's just.
lack of functionality as well inside of them, and then there is no SNMP trap receiver, within that contrib repo, so that's the third objective.
And the last objective is to support and expand OPI's network-related telemetry function.
So that's just Mario supporting what Obi's doing.
within the network flows, and then the thing that I talked about with you before, which is to contribute the flow trace exporting out of OBI.
**Mario Macias** 07:48 Okay, yeah, this fourth objective for me is fine.
**Sven Cowart** 07:52 Okay.
**Mario Macias** 07:53 possibility that when they review it, they will say, no, we don't accept this as an objective. This should be part of the OVC. Okay. For me, we can keep it and just see if they accept it. Okay.
**Sven Cowart** 08:10 That sounds good.
**RC Robert Cowart** 08:12 Is it worth mentioning also, like, support other Sigs with any network relevant things that they that might be nested. I'm thinking, like the system, Sig is going to have network specific things collaborating on that particular side.
**Sven Cowart** 08:32 Yeah, I'm going to write that out inside the.
Like, they expanded.
**Mario Macias** 08:36 Yes.
**Sven Cowart** 08:36 description for objective one, like type collaborate, type collaboration with or semantic convention entities, systems and OBC.
**Mario Macias** 08:45 Yeah, I think we can also mention that instead of support and expand, at least provide the foundations for other SIGs, or keeping close communication and close collaboration, so we align all the SIGs. Yeah, something like that.
**Sven Cowart** 09:08 Okay.
**Stephen Lang** 09:09 So just on that subject as well. I wonder if the Prometheus community could help here, because there's the existing Snmp exporter.
And there's a bit of a effort going on at the moment.
to try and bring the Prometheus and OTEL worlds closer together in terms of sharing maintainers. Because what we have at the moment is, for example, we have a Prometheus SNMP exporter with Prometheus maintainers, and then we have the, you know, hotel SNMP receiver with hotel maintainers, and they're effectively implementing the same thing.
It would make sense, for example, to take the more mature Codebase, and have it work for both worlds, somehow.
Either by, you know, including as a library or making them At least follow the same conventions, But, you know, maybe it's worth at least.
Thinking about, how we can align Both Prometheus and Atel communities.
Not sure if that wants to be considered here as well.
**RC Robert Cowart** 10:10 So, personally, I think that's fine.
I'm trying to think how I want to say what I want to say without coming across as arrogant.
But like, I've done SNMP the vast majority of my career with Elastiflow. People tend to think of us more nowadays for flow data, but like SNMP, I've done way more of. And I can tell you there's so many undocumented details.
Out there, for example, even in LLMs, ask an LLM, pick your favorite one, ask them about PDU packing. It probably knows nothing because it's just one of those things that people in the space know and no one's ever written down anywhere, so it never was trained on anything, you know. And so, I think the first thing I'd love to just… I would personally love to do, a review of those, and if they're written in Go, and they use Go SNMP, they probably already have problems.
because that go Snmp library. We kind of hate it internally. We use it a little bit, too, but I'd love to just rewrite that thing. It has got some bad stuff in it.
And so I'm just being a little skeptical of when I, I've looked at the Prometheus one before and I would not use it. I actually think the best open source SNMP thing at the moment is Telegraph and I usually describe it as the best of all of the sucky open source SNMP pollers.
So, we we would hope to. That's why I think Sven said, improve, because we would hope to bring in a few of those things that are non obvious into it, so that there's like one one… there is one really good one. So I would look at it more as, like, who's done something clever?
Like, who has a good scheduler, for example? Like, that would be good. We could use those pieces, parts. I'm sure there's some good parts in there, but, I guess I want to say, happy to bring all the things together and unify it, but It probably needs a good review as first, though, to make sure that that the stuff is supported that really needs to be supported.
**Sven Cowart** 12:19 Steven, is the ask to pull in the SNMP receiver that is part of Prometheus? Is that what you're saying, or…
**Stephen Lang** 12:26 It's more to keep the communication lines open. So, I mean, if, for example, there was stuff that we could already use in the Prometheus exporter, then let's not rebuild it.
But at the same time… Yeah.
if there's some maintainers over on the SNMP exporter that maybe they could get involved, and it could work both ways, so the communication flows each way, and we could help each other.
Because, like, Rob, if there's problems with that exporter, then… It'd be great if we could share.
You know how to resolve those problems.
Whether it's just a case of, you know, keeping the communication lanes open between the two, and I'm happy to get involved on that side.
I just think there could be a lot of valuable knowledge here within this SIG, and it would be nice to share that to the relevant communities.
And whether that means we can do code reuse, then great, but if otherwise, at least sharing the knowledge.
**Braydon Kains (Google)** 13:22 In… in the… in the receiver, in the collector, I think… Like, we can essentially consider it completely malleable, because I just, out of curiosity, I went and looked through the commit history, and I'm back to 2024, and I'm still not seeing an actual, like, feature work change. I'm only seeing, like.
Across the board, like, dependency update changes and stuff.
**Sven Cowart** 13:46 Mmm.
**Braydon Kains (Google)** 13:47 So that receiver is, in essence, unmaintained, and I think has just kind of flown under the radar, because nobody's reported problems, because nobody's using it.
Yeah. So I think, essentially, we should… I should reach out to the person who's a code owner on it right now, but I think, for all intents and purposes, we can essentially consider the SNMP receiver as it exists completely malleable to whatever we decide to do.
So if that ends up being, the SNMP exporter in Prometheus.
Is able to, like, take out reusable chunks of SNMP, maybe corrected by Rob's knowledge, or whatever we can do, and we could just pull that in to the collector and make a receiver out of it.
that is probably fine, like, it's probably something we're perfectly fine to do. I'm guessing if we wanted to… totally gut the receiver and start it over from scratch. I don't even think anyone would notice if we did it. But I think we can… we can consider the receiver completely flexible, I think.
**RC Robert Cowart** 14:46 And.
**Sven Cowart** 14:47 Makes sense.
**RC Robert Cowart** 14:47 I don't know who's using these things, so we would need to try to have some backward compatibility.
**Braydon Kains (Google)** 14:53 Yeah, there probably is someone somewhere using it, and, like, if we just… I'm not saying we actually should, like, silently disrupt the whole thing. We would do a proper transition. There's a whole document explaining how we handle like, semantic conventions transitions when receivers are going to move from old conventions to new ones. There's a specific combination of feature gates on the collector and stuff. Probably we would just adopt that same That same philosophy, when we update it, but…
**Sven Cowart** 15:24 That makes a lot of sense. All right, so is there any one objective that I've missed?
**Braydon Kains (Google)** 15:36 No, I think this works. I think…
**Mario Macias** 15:37 Fine.
**Braydon Kains (Google)** 15:38 it's… if you wanted to split it up a specific way, you know, Objective 1, the, like, primary target is… this is where we're talking about, like, the semantic conventions repo, like, the core stuff that gets shared across everywhere. Then Objective 2 is kind of where we're gonna… go into the federated SemConf repo, so that the deeper protocol stuff can move quicker than coarse-moving conventions. And then Objective 3 and 4 are both targeted to implementation details. And maybe GC might have a different opinion on this than me. I would say maybe merging objectives three and four into just this idea of support implementation of our semantic conventions that we've.
Aye.
**Sven Cowart** 16:27 Yeah, that makes sense to me. And I can call out the specifics inside of the objective.
**Braydon Kains (Google)** 16:32 Yeah, just because then the… then the objective kind of maps to, like, the… the, like, three distinct work streams, or it's, like, core work.
Federated work.
implementation work.
**Sven Cowart** 16:44 Yep. Within the… You brought up the federated semantic conventions.
in Objective 1, The network area would become a federated semantic convention, is my understanding, right?
**Braydon Kains (Google)** 16:59 I think the way people are envisioning it right now, I don't know if we have a hard plan here yet, but the way I'm thinking of it is, there is, like, a core, like, network namespace, and, like.
those attributes are shared by, like, HTTP, by a system, by a few other places, by messaging, like, some other places within the core repo, and may… may end up being used by, like… because other federated repos can refer into Core.
So basically, anytime there's an attribute that we feel is, like.
gonna be shared across other namespaces, it'll live in core. But for things like NetFlow, or SNMP, or things that are, like… we are defining semantic conventions around an external protocol. It's not about being shared, it's just about being able to effectively instrument, like.
data about a protocol, or something like that. That's the kind of thing that would live in the federated repo, and can refer back to stuff in the core repo.
It's kind of this same way of thinking of, like, You know, shared libraries versus…
**Sven Cowart** 18:03 Yep.
**Braydon Kains (Google)** 18:04 Application.
**Sven Cowart** 18:04 All right, that makes sense.
Alright, and then my last question here was around… project leads.
Braden, I know you brought this up originally, but then you kind of backed out. I didn't know where you were.
**Braydon Kains (Google)** 18:20 Yeah, I keep on going back and forth, because I'm not sure what… the… semantic conventions maintainers want or not. I think… I think they want me to be around because semantic conventions has a lot of history and a lot of, like, moving parts, and because, well, now… now two of the major semantic conventions maintainers are, like, just direct co-workers of mine, so it makes sense for me to be Around for, at the very least, the first, like, the initial setup of the project, and getting things started, and getting the workflow started, so I think you can leave me as a lead here. Maybe list me third.
**Sven Cowart** 18:56 Okay.
**Braydon Kains (Google)** 18:57 Yeah, so I can help with anything semantic conventions related and anything collector related, you know, I can't help with much about, like, actual network expertise, but I can still serve as, like, a project lead here and help get the workflow set up and everything.
**Sven Cowart** 19:13 Is there, that makes a lot of sense and thank you.
And these were not listed by any order, by the way.
**Braydon Kains (Google)** 19:20 Yeah, that's.
**Sven Cowart** 19:21 Yeah.
**Braydon Kains (Google)** 19:23 That's me… the order is just me nitpicking anyway, it's.
**Sven Cowart** 19:27 Is there anyone else that would like to be a lead on this?
**Antonio Jimenez** 19:33 Sorry for jumping late. From the Cisco ThousandEyes perspective, I would like to also contributing on that project, I will.
I would be happy to to be there. Yeah.
**Sven Cowart** 19:43 Okay. And I think the leads here, their responsibility is once the project is created, maintaining the project board and then being the maintainer and then approvers of any of the PRs that come in that would modify or change semantic conventions and making sure that we're working with other.
entities, or sorry, other SICs to, to be collaborative, and… unifying cross-board.
Is that the right expectation?
**Braydon Kains (Google)** 20:13 I think so, yeah.
And there's also, like, I think System Group is the only one that really does this, but the… Idea that, like, if We are… if we're doing something that is different from other semantic conventions groups, or if we feel like core semantic conventions rules aren't addressing what we need to do, it sort of ends up falling on Project Leads to sort of hash that out and maybe write new guidance or, or help fix guidance or whatever.
**Sven Cowart** 20:43 Alright, that makes sense.
Last question is TC sponsors and GC liaison. I'm not sure. I don't.
**Braydon Kains (Google)** 20:53 So.
**Sven Cowart** 20:53 Not long enough to know, but I know Thrask and Ludmilla showed interest at some point.
**Braydon Kains (Google)** 20:58 Yeah, I think, for GC Liaison, Ted Young was the GC Liaison of the previous iteration of the group, and he said he would be willing to be GC Liaison again.
So, we can ask him, I think. For GC liaison.
I think Lyudmila did show interest.
She might be willing to. There are a few other TC members that I'm… directly in contact with that I can ask as well.
**Sven Cowart** 21:28 Okay.
**Braydon Kains (Google)** 21:28 Got it, but
**Sven Cowart** 21:30 Sounds good. I think Josh was interested too at some point.
**Braydon Kains (Google)** 21:33 Yes, he would be interested. I think he's actually stepping down from the TC very shortly.
**Sven Cowart** 21:39 Okay.
**Braydon Kains (Google)** 21:39 Because since Ludmilla is now at Google, now there's too many Google people on the TC, so he has to step down.
**Sven Cowart** 21:46 I see.
**Braydon Kains (Google)** 21:46 So he won't… I don't think he'll be able to sign up for this But I think he will be an important contact for us, because anytime we're talking about Federated Semcom, or, like, just Semcom in general, he's sort of the main guy, so…
**Sven Cowart** 22:00 Got it.
**Braydon Kains (Google)** 22:01 Okay.
**Sven Cowart** 22:03 Awesome. Alright, that's all I had. I'm gonna fill the rest of this template out, and open up a PR.
By the end of the day, and Hopefully that makes it more official, and we can get things rolling.
**Braydon Kains (Google)** 22:16 Yeah, sounds good.
**Sven Cowart** 22:20 I shouldn't have stopped sharing my screen, should I?
Alright, Mario?
**Mario Macias** 22:32 Yes, just to update the status. I I did the I started this semcom semantic convention for what we already have in in Ubi, trying to adapt it to to some comments I got I got a PR some months ago it got automatically closed because it it was using a namespace that was not assigned to any SIG so I recreated it and then under the network but there are still some references that don't have assigned any SIG Related to the source and destination attributes, so it has… closed again. Asking in the… asking in the… in the semantic convention channels, they say that once the new network seek is established.
Those sections, destination and source can be assigned to our SIG. So we can continue. So yeah.
**Sven Cowart** 23:32 Pos.
**Mario Macias** 23:32 so it's it's it's fine just waiting for the new I thought we I could work in parallel but since not so yeah it's fine waiting for the new network network seek to get established and then relaunch it but if in the meanwhile you want to Provide feedback.
Oh, it's… I'm more than happy that keep addressing…
**Sven Cowart** 23:56 Okay.
It's.
**Braydon Kains (Google)** 23:58 We might let you open the PR in draft.
I'm not 100% sure how that part works, but…
**Mario Macias** 24:04 Oh, dear.
**Braydon Kains (Google)** 24:06 If you open a new draft, it might work.
**Mario Macias** 24:08 Yeah, I think I cannot reopen it again. So yeah, maybe I can open it in draft. Yeah, I can try.
Yes.
**Braydon Kains (Google)** 24:16 Yeah, if I had the permissions to reopen it, I would, but…
**Mario Macias** 24:19 Okay.
**Braydon Kains (Google)** 24:20 I don't have those, unfortunately. I can maybe see if one of the maintainers could try and reopen it in a draft, just because we want to be able to at least have people start commenting on it if we want to get started.
**Mario Macias** 24:32 Yes.
**Braydon Kains (Google)** 24:33 Ownership… the ownership thing will be solved once we have The… once the project… that Sven is working on is merged.
then we'll have the repo owners make us a group, and we'll make a PR that assigns the network approvers group to a bunch of areas in the code owners file, and then that will fix this automation so we can open stuff up.
**Mario Macias** 24:57 Okay, okay, thank you.
**Sven Cowart** 25:04 All right.
And lastly, Rob, Yeah, things, questions.
**RC Robert Cowart** 25:09 Yeah. So As I… there's been a number of things I've been thinking about in general, and as I've been… also, I mentioned in one of the original tickets this approach that I've been taking around just so much. There's just so many MIBs out there for so many different things to help inform some of the work being done. Just give you an idea. I'm through about a 5th of what we currently have on unique MIBs. And I just checked. I already have 1 million MIB objects.
So it may end up being as many as close to you know, 5 million. So to be able to just do, you know, I'm putting this in a like vector store, lexical search store, so that I can say Okay, show me all the things that are, have to do with OSPF adjacencies and get all of the, you know, as an example, just to be able to pull stuff.
**Mario Macias** 26:07 Okay.
**RC Robert Cowart** 26:08 By the way, our friends at Cisco are the worst. They got like 3,000 unique MIBs themselves. So, but anyway, and as, so as I've been thinking about things, the, a lot, the, there's.
2 things. One is just more, I think, of a like a near term priority that needs to be thought about, and that is 1st like thinking about entities.
and what I mean by like that is, there's interfaces and interfaces have Vlans, and they have class of service queues, and and an interface may have a physical connection to something else, and across that might be a protocol adjacency. And then there might, you know. So there's there's a number of different things that are all kind of interrelated, and where we probably need to make some decisions and start focusing a little bit of entity work and then say, Okay, now, within those entities, what might the attributes be that is applicable to those different entity types?
that that. So that that's 1 thing I know that. And, by the way, on our side, the way we're thinking about this, we we actually have some network discovery technology that we, you know, weren't been having our roadmap, anyway, to work on. I'm not gonna. There's been maybe a little bit of of idea ideation started, but not a lot of coding yet on it, mostly because Our thought actually is on this is.
we want it all to work with the same entities that are in OTEL. So, I kind of feel like… and maybe I'm misunderstanding the entity effort, someone tell me if I am, but it seems like there's first entities to be defined related to network stuff. And then Whether that becomes official entities immediately, that might be some other point to be decided or discussed at some point with that particular group. But nonetheless, I just feel like identifying those managed objects that we want to focus on first, I think makes a lot of sense.
I have my opinions on that, but I don't know if, You know, anyone else has immediately any thoughts off the top of their heads about what might the immediate priorities be?
**Braydon Kains (Google)** 28:29 Yeah, one thing that they're trying to do in the core SemConf repo generally is basically that entities come first, kind of. There actually is an order of stability when you're trying to mark something as stable. So you have to make attributes stable first.
And then the entity that uses those attributes, and only then can you… can you, stabilize metrics and stuff using the entity. So it's, like, in that order. So entities and attributes kind of end up happening at the same time, because you can't define the entity without first defining what the attributes are. And then… The… the thing about entities that we're kind of running into right now is that sometimes the thing that you're trying to report against is kind of hierarchical in nature. Like, for… for system, it's… it's, like, we have… you have a VM, it's, like, that VM, I guess, is part of a, like, a project, if it's a cloud VM, or it's under some, like, Proxmox instance, or whatever you're talking about. But… Entities is sort of designed to be a flat hierarchy, so… you can kind of… you can define relationships in terms of, like, this is a something else joined on a field, or has a joined on something else, which can make it sort of hierarchical. But the… the actual entity like, reporting thing in the proto is just an array. It's, like, it's flat.
So that might be the first thing that we have to figure out as we decide I want.
metrics… like, what is this metric going to be reported for? Like, it's… It's… if this is a metric, for a VLAN, You know, then we need to say, okay, VLAN is probably an entity.
What are the attributes necessary to uniquely identify?
a VLAN? Like, what is the bare minimum set of attributes that identify it? And then there can be other attributes about it that are descriptive and informational, but that don't necessarily change the identity of it.
I don't have a good, like… I don't know enough about networking to come up with a good networking example, but in… in system, for example, the process entity, the… I… the identifying attributes are just two, just the PID and the creation time.
If those… if either of those attributes change, then we are calling it a new pro- this is a new process. This is not the same process as before.
And then there's like 10 descriptive attributes that are information about like the process command line, the process name or the current executable, all that stuff that can all change in the lifetime of one process and not change the identity of it. Like this is still the same process, but different. These are just informational attributes that go along with it.
and we need to have… Sorry, what was that?
**RC Robert Cowart** 31:28 Then stop sharing.
**Sven Cowart** 31:31 Oh, sorry.
**Antonio Jimenez** 31:31 Yes.
**Mario Macias** 31:32 Hehehehehehehe.
**RC Robert Cowart** 31:36 Okay, sorry, Brayden.
**Braydon Kains (Google)** 31:38 No, no, that's fine. But, so when we, When we come up with a… with an entity.
we… something that we know we need to report against, that… that's… then we decide, okay, what… what uniquely identifies this? What attributes will always be the same throughout the identity of this thing as it lives? And the backend can then keep track of, like.
all the different VLANs it knows based on at least these, like, one to three, just, like, identifying attributes.
**RC Robert Cowart** 32:08 So, by the way, this is not Otel. This was actually some ideation we were talking about internally, but it turned out to be very similar to the entity way of thinking about it.
**Braydon Kains (Google)** 32:20 Yep.
**RC Robert Cowart** 32:23 So I was gonna say that I don't think we personally on our side have an issue with the entity way that it's like hierarchical comes through the relationships more or less.
**Braydon Kains (Google)** 32:34 Yep.
**RC Robert Cowart** 32:34 Not, not necessarily being some nested object oriented type of thing. So that's the way we've thought about it too. Okay.
**Braydon Kains (Google)** 32:44 Makes sense.
**RC Robert Cowart** 32:45 But I already see, like, even the example you gave, like, you mentioned something with, like, processes, right?
**Braydon Kains (Google)** 32:51 Yep.
**RC Robert Cowart** 32:52 And like a process.
Opens up a network port and boom, now you're right in our world, right?
Yeah.
which can have flows that go across it, which can, you know, all kind of things. I mean, there's like tons of touch points. Anyway, I just wanted to say like something like this is what I do think, you know, would be an exercise to go through first on a few items. I do think, though, the the there's a a higher level thing that we could Matthew T. maybe get agreement on, and and I'll just throw my opinion out there I feel like step one is Data center networking.
In other words, not WAN, not MPLS, tunneling, not Layer 2 services over pseudo-wire by… by a Tier 1 telco, not… you know what I mean? And maybe not even campus Wi-Fi, like, you know, like… data center networking as a… as, like, a… that's what we're gonna scope first, just as an example. I think that's probably when I think about all of the rest of OTEL and what it is Currently instrumenting?
It's intermittent instrumenting data center. Infrastructure applications, et cetera, et cetera, right? So I feel like that's probably the most logical place to start.
Umm.
I don't know if there's any other opinion or agreement there.
**Antonio Jimenez** 34:19 Have we considered also start with what is currently there?
Because we have a conversation a couple of 6 meetings ago about the network.pr.address, and we were calling local and peer. And so I mean.
it's important to add new entities and add new things, and I am sure, Robert, that you may have a long list to go through, but I don't think we should tackle All of the… at the beginning, or… I mean, it's good what you said to start with the data centers, but maybe what we should do is revisit what is there already, even if it is in development or in the stable, so we have an agreement about what's currently being used, and then we can maybe go from there. That could be also my suggestion, because there is already doubt About what is there today.
**RC Robert Cowart** 35:08 No, that totally makes sense. Yeah. I was just mostly like, start what's there. I'm, I'm, I wouldn't surprise me if it's data center, you know, but yeah, I'm not, I don't want to reinvent the wheel. I just want to, I'm just trying to think about scope, you know, that we, not that if someone wants to come along and contribute something to a totally different area that I would suggest we say no about it. You know, I'm just trying to think like, okay.
There's so much that could be done. What do we want to, you know, what's the area to focus on initially?
**Braydon Kains (Google)** 35:45 I do think we could… we could essentially do both what Antonio and Robert are saying, because I think what… what is there in… in SimCom already is so… a lot of this entity stuff and a lot of the more newfangled stuff was very nascent when all that stuff was defined and stabilized, mostly because they were trying to stabilize HTTP. That was sort of the… the first initial target. They wanted to stabilize the HTTP… it was really HTTP spans was the main thing they were thinking about. They wanted to get HTTP spans stabilized, and so they came up with the attributes that are there right now. So that, combined with whatever network attributes the system group has added for Which is essentially just, like, network interface metrics that come from ProcFS.
I think it, it's.
we will come to realize very quickly that it's all quite simplistic and probably not up to snuff anyway. So, if we take account of what's there, and then combine it with trying to come up with a model that we think is better and more realistic to to the real networking world, with full networking expertise, like a review of what's there, along with what we think the new model should be. I think I think we'll have a good starting scope with that.
**RC Robert Cowart** 37:03 Okay, yeah, by the way, I turned my camera off, it was freaking out, I don'.
**Braydon Kains (Google)** 37:08 Yeah, that's fine.
**RC Robert Cowart** 37:09 Okay.
**Braydon Kains (Google)** 37:10 I was about to close my eyes, so I didn't have to.
**RC Robert Cowart** 37:14 Basically, I have related to all this MIB work, some long-running jobs going on, and I've really needed to reboot my laptop for the last 4 weeks, but that just means I stopped the jobs, and then, you know, gotta reopen 57 windows, and I'm just not doing that right now, so… Anyway, okay, the other thing that has… and if this is somewhere in… in all of the OTEL documentation and what have you, just… just tell me, Rob, you gotta go read more.
But what has been in my mind is like.
Okay, 1st correct me if I'm wrong, that there are that pretty much all the values are Signed values and floats more or less. Correct.
CLAB, like metrics in particular, right?
**Braydon Kains (Google)** 38:07 I, I thought the, the proto was.
was unsigned? I have to check, That sounds right to me, but I need to remember, the protocol.
**RC Robert Cowart** 38:22 So then you reviewed 2, right? You thought everything was floats, right?
**Sven Cowart** 38:25 Yeah, yeah, there's… Yep.
**RC Robert Cowart** 38:28 Because…
**Sven Cowart** 38:29 And… And signed.
**RC Robert Cowart** 38:32 Yeah, so much… in network.
is you're gonna have a lot of unsigned 64 bit counters.
**Braydon Kains (Google)** 38:42 Yep.
**RC Robert Cowart** 38:43 And, you know, Let's face it, 10 years ago.
like, when are you worried about ever in the lifetime of a network device getting rebooted, hitting that… but, you know, shoot, even a 1G interface can do a 32-bit counter in about, you know, 4.7 seconds.
At full bandwidth, right? And then if you talk about like bike counters or whatever, and then you have, Now you have, though, like, 1.6 terabit switches.
So you know, 64 bit counters going into a range that would be interpreted as a sign value as negative numbers is problematic.
So as I'm starting to think about ahead to some of this stuff and piecing together some things.
I was just curious what everyone's opinion and what's happened elsewhere on how that gets handled. Should… should… should we simply be saying, like, let's say I'm… I'm pulling a network interface, pulling back a 64-bit value.
Should I not even worry about sending the raw value and simply say the metrics are, it's a, you could say a delta of bytes or a rate of bytes.
Between those two poll intervals, right? It's not, you know, between the current and the last time it was polled. In other words, we're only communicating the change.
per record, as opposed to the raw unsigned 64 bit integer.
**Antonio Jimenez** 40:21 But I don't think we have to be the one doing that. The reason why is because the observability backends are already optimized in the same… I don't know what's your goal there, Robert, but I think the observability backend already optimized to only keep the deltas, and so on, so… As it is done in other places, I am… Consider it makes more sense to put the whole number.
Rather than just a change.
**Braydon Kains (Google)** 40:44 It does depend what backend you're talking about, whether… they all decide to do this differently. Like, the GCP one, for example, can accept both, so it… on a metric descriptor. So, the other thing with GCPs is that it's all heavily schematized, which is not, you know, how Prometheus works or anything, but, like, once a metric descriptor is defined, it's defined as either it takes a delta or it takes a cumulative, and if it takes a cumulative, then it's expecting the raw 64-bit counter.
and if it's Delta, then it's expecting you to report the rate of change And we usually… we usually tell customers to report the cumulative, not the delta, in a lot of cases.
I don't know… I actually don't remember how the… Overflow case is handled, though, like, if we actually do go over the assigned 64-bit.
Counter. I… I did check the proto, by the way, and I… I… it is assigned it is assigned 64. I forgot that I… for some reason, I thought I saw a UINT64 somewhere, but I think that's just collector code doing something weird. The proto is… is signed when it's an INT data point.
I don't… I'm realizing that I've never actually checked What happens?
When… if the number… if the number… like, if the counter overflows.
**RC Robert Cowart** 42:10 Yeah, because it… because usually, if that most significant bit goes to 1, then it's a negative number, if it's signed.
**Braydon Kains (Google)** 42:16 Yeah, yeah.
**RC Robert Cowart** 42:17 Which would be… Not very useful, and And so, like, you know, so…
**Braydon Kains (Google)** 42:27 Sure.
**RC Robert Cowart** 42:27 Start to think about these because, you know, we're thinking, we're thinking about.
what is being communicated right? So as soon as if it's only signed values that can be communicated via, you know.
Otlp, right? The the line protocol, then It it almost excludes sending raw values of counters.
As far as at least 64 bit counters.
**Braydon Kains (Google)** 43:00 Yeah, the protocol does support reporting deltas, so, like, that is… It could be… maybe don't take this as a hard answer yet, because I do need to look into what the general recommendation is for this. I realize I've never run into it, but I think it is within reason for us to say.
This counter… goes so excessively large as a cumulative that we recommend reporting it as a delta. I think that's something we're within our rights to say on a… on a given, like, number… like, counter metric.
I should… I should check with SemConf maintainers to see if.
If that's true, but I figure that we are… Usually, we say… like, in our SemConf rules somewhere, there's something about, like, when you should report a cumulative versus when you should report a delta, where the upside of a cumulative reporting, ignoring the overflow problem, the upside of cumulative is that if you're… if you drop out and you miss a data point or something.
Your… your backend can recover.
**RC Robert Cowart** 44:09 Or phone.
**Braydon Kains (Google)** 44:10 the data won't be wrong. But then with Delta, it could be, but the upside with Delta is that For, like, a client application reporting stuff, it's way less memory usage, because it doesn't need to hold the current cumulative value, it's just reporting a difference.
**RC Robert Cowart** 44:25 Queries are typically a lot, more straightforward if it's just if it's not the overall cumulative number.
**Braydon Kains (Google)** 44:34 Yes.
I will… I will look… I'll take this away as an action item. I'll try and get an answer on this. I'm realizing I've never… Checked.
**RC Robert Cowart** 44:47 I'm also happy for you to share. Oh, here's where this has been documented.
**Braydon Kains (Google)** 44:52 Yeah, if I… I'll try and… I'll try and find any previous… we have some writing on this somewhere, but I might be mixing up between, like, GCP's recommendations and what Semcom is recommending, so I need to…
**RC Robert Cowart** 45:06 Yeah, yeah.
**Braydon Kains (Google)** 45:06 Straighten this out.
**RC Robert Cowart** 45:07 Yeah, I'm just as we go through this. I've been trying to, you know, as I mentioned to you on the one slack thread, trying to shift my thought from things I've done in the past, like the the way of showing you know, the actual metric values, and then the attribute says whether it's in or out, as opposed to just having an in metric and an out metric. But, you know, so it's just adjusting to those things, but this is… this is the one I just found any clear… you know, any clear directive, or what have you on. And it will definitely be relevant. Like, this is not a hypothetical thing that will never occur because the number's too big. It'll definitely can occur, so…
**Braydon Kains (Google)** 45:53 Yeah, there actually already are metrics where it definitely can occur, too, so I'm surprised it's never… come up for me before, because, like, CPU time, as soon as you're.
**RC Robert Cowart** 46:02 Not big yet.
**Braydon Kains (Google)** 46:03 as soon as your VMs live long enough, your CPU time is going to be a gigantic number, and so I don't know how this has never come up, but… okay. Yes, I'll…
**Sven Cowart** 46:14 Do you think there.
**Braydon Kains (Google)** 46:15 Right.
**Sven Cowart** 46:15 Opportunity to change.
The types that are allowed?
and to open it up to allow for unsigned values.
In the spec?
**Braydon Kains (Google)** 46:25 be an uphill battle, but not impossible. It would be an uphill battle, but if we do truly have a good reason, then I don't see why not. So maybe, it would help if I send the bit of the proto that I'm looking at.
This is the… the number data point proto, all of the… all of the SDK specs, the collector, and all that stuff, they all work off of this proto. And the way the number data point proto works is the data point is either a double or an int, so… If we were going to implement this in a way where we wanted a number data point that Could be, like, an unsigned 64, or some other way of, like.
growing larger, we'd probably add to the one of here, and I don't think that would be a breaking change, but it would be… it would be a fight in the specification. Any change to specification is always… is always heavy. Right.
So, yeah, we shouldn't consider it impossible. It's… it is definitely possible.
We're… it's… it'd be a lot of work, but it's.
**RC Robert Cowart** 47:40 Yeah, I mean… for for what it's worth. I'm on board with what you were saying, Braden, like to me. I would prefer to keep the raw value just because it's the most flexible on the on the back end. It's mostly like you lose granularity. But you don't lose the actual number over a time.
So.
**Stephen Lang** 48:07 Just a thought, Rob. I wonder if Otap.
Supports.
Unsigned 64-bit integers, the hotel arrow protocol.
**Braydon Kains (Google)** 48:17 Good question, actually, I don't know.
I don't know if they keep their protos here, if they… I think it's in a different repo, so I'm not sure where to check that. That's worth looking into as well.
I'll definitely look into this, and I'll come back to the network Slack channel with the summary once I've had a chance to…
**RC Robert Cowart** 48:53 That would be great.
**Braydon Kains (Google)** 48:55 It'll probably be tomorrow, but I'll try and come back tomorrow.
I can answer that.
**RC Robert Cowart** 49:00 anyway. So yeah, not quite that far yet, but just just trying to to think about that as I work towards some of my own 1st submissions. So.
**Braydon Kains (Google)** 49:14 Cool. I'll bring that on Tuesday, and then… Oh.
Just so everyone knows, I'm taking a 5-day weekend, Canada Day, through the Through the weekend. So, I'll be back next week. I assume the project PR will be ready at some point, and I probably won't be around to review it until next week, but…
**Sven Cowart** 49:36 That's right.
All right.
I think that's it, then Thanks for coming.
**Braydon Kains (Google)** 49:45 Thanks, everyone.
**Sven Cowart** 49:46 See you guys next.
**Mario Macias** 49:46 Thank you, everybody. See you.
**Antonio Jimenez** 49:48 To your point.
**Giuseppe Ognibene | Coralogix** 49:48 Thank you. Yeah, yeah.
