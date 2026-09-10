SIG: OpenTelemetry on Mainframes Weekly Sync
Date: 2026-09-09
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Rüdiger Schulze (International Business Machines Corporation)** 00:25 Hey, Jim.
**Jim Porell (Rocket Software, Inc.)** 00:32 Guess I gotta come off mute to say hello.
**Rüdiger Schulze (International Business Machines Corporation)** 00:35 Right.
My bad, I don't have anything new for the semantic conventions yet, but I want to talk about… a Leano project today, so let's wait for Azos to join.
**Jim Porell (Rocket Software, Inc.)** 00:50 Okay, I was gonna ask about that anyway, since, what is it?
TAC meeting is tomorrow or something.
**Rüdiger Schulze (International Business Machines Corporation)** 00:56 Right, yeah, so… Let's just update the notes.
Time is passing quickly.
Reminds us at Delaware.
**Jim Porell (Rocket Software, Inc.)** 01:16 You say so, I don't know about that, but… I had the longest summer ever, it felt like.
now that I'm active again, it's like… I would agree that Time is going faster than I'd like, but…
**Matt Hogstrom** 01:42 It speeds up as you get closer to the end.
**Jim Porell (Rocket Software, Inc.)** 01:48 I don't know about that.
**Rüdiger Schulze (International Business Machines Corporation)** 01:52 And that… My bad, don't have anything new yet for semantic conventions, but we will discuss the… a bloano project today.
**Matt Hogstrom** 02:04 Okay.
**Rüdiger Schulze (International Business Machines Corporation)** 02:06 So…
**Jim Porell (Rocket Software, Inc.)** 02:13 So during my morning break, I went out and got… $270 worth of fuel, diesel, high test gasoline, gasoline, ready for the apocalypse.
No.
**Matt Hogstrom** 02:27 Oh, that's good.
How much was diesel where you guys are at, or where you're at?
**Jim Porell (Rocket Software, Inc.)** 02:31 5… I got it for $5.89 a gallon.
**Matt Hogstrom** 02:37 Yeah, it's about the same here down in North Carolina.
**Jim Porell (Rocket Software, Inc.)** 02:39 But I saw $5.99, that was the cheapest I found, and then I have to get this high test for all my mowers and wheels.
**Matt Hogstrom** 02:46 Wow.
**Jim Porell (Rocket Software, Inc.)** 02:46 offers and stuff, and that.
**Matt Hogstrom** 02:47 You get the, ethanol free?
**Jim Porell (Rocket Software, Inc.)** 02:50 Yes, that's the key. Yep.
So that's $5.17 a gallon, and then regular gas was $4.17 a gallon.
**Matt Hogstrom** 02:59 Wow.
Crazy.
**Jim Porell (Rocket Software, Inc.)** 03:01 That's probably cheap compared to what you're paying in euros for a liter, so…
**Rüdiger Schulze (International Business Machines Corporation)** 03:05 The little is now, like, 220, 230 euro, so…
**Jim Porell (Rocket Software, Inc.)** 03:09 Yeah, so you, like, ate something.
Almost 9, probably, yeah.
**Rüdiger Schulze (International Business Machines Corporation)** 03:16 Not fun anymore to…
**Jim Porell (Rocket Software, Inc.)** 03:19 No.
**Rüdiger Schulze (International Business Machines Corporation)** 03:19 to go across the country, which I every now and then do.
Alright, good. So, I think you have seen the email from John, so we got a project name, it's Opleano.
Essentially, it's the, you know, following the proposal that was made by Richard BMC earlier.
To come up with, Let's say a service within COS, to provide OpenTelemetry Conform APIs.
I especially say conform, because obviously, you know.
having these native languages, mainframe native languages, we would have a slightly different programming model, like you would have it in Java or any of the other languages.
And, there was, from the OMP, they sent a template for the presentation tomorrow, so I tried to fill this out. I added two additional slides.
Essentially, kind of, like, calling out what we discussed earlier.
And that's also what is on the… it's a copy of what we put into the Chitub project proposal, some time back. I think it summarizes what we… what I just said, except of… I think what I didn't mention is the… the ZOE cross-memory service for consideration. Jim.
it's interesting, I did a little bit of research. When we get there, by, you know.
by some time in future. That might have actually a performance consideration there, so in terms of… You know, time for injection that might add… Might be something for users to opt in, but at the same time then accept that there is maybe a… Slight overhead in injection time.
**Matt Hogstrom** 05:23 You're gonna have overhead no matter what you do, though, right? You're either gonna cross-memory, you're gonna do a TCP IP socket or something.
**Rüdiger Schulze (International Business Machines Corporation)** 05:31 Right, right.
**Jim Porell (Rocket Software, Inc.)** 05:32 The cool thing about the cross-memory service is it allows, like, an unauthorized program, in this case, maybe this, you know, emitter, to work with privileged storage areas, you know, without having to go through all kinds of programming, because all the… all the… all the staff-type stuff and APF stuff is handled as part of the Zoe Cross Memory Service. And we use it in Omegamon, and it's pretty cheap. It's relatively cheap.
**Rüdiger Schulze (International Business Machines Corporation)** 06:03 Okay.
Okay, so, and then… from a design perspective, I think we will see this later on, but we, I mean, one of the reasons why this project, I think, was proposed in the form When we look at what is currently out there, the SMF, in-memory SMF, SMF-based approach. Obviously, some sort of static, clunky in the way of how Windows customers can use this. So, Obviously, we try to do a better job here in, bringing this to life.
On a very high level, what we talk about, obviously, we would have instrumented applications, and we can talk about how the instrumented applications would, you know, work with this ingestion layer, but one way, obviously, would be that We have a way of memory mapping to… similar to what the OpenTelemetry APIs would do.
That would, from a COS point of view, and also from the programming model that we have with, these, these languages that we are looking at here, obviously the most straightforward approach.
And then we need to have something similar, like we had within memory, some sort of circular ring buffer, which allows us to, store this data, and then pick up this data for other Kronos processing.
And obviously, we would want to make use of the OpenTelemetry APIs. I think we don't even want to do… sorry, I said APIs, I meant the SDKs. Obviously, I think we don't even want to be too prescriptive in a way which SDK, so… Might be actually… we may leave it open to have a choice as a… somebody who is using this, to either go with Java, Go, or eventually see C++ SDK.
And then obviously the backend collector that's… out of scope from… from the project perspective that's… that's done already. What would be used, From a customer perspective.
That's on the high level, and then there are a couple of slides which, the way they read, they are very busy, but that was the template.
the way they read is actually the interesting information that we need to fill out is on the… on the right side of the slide, and I would briefly run you through, and please commend if you have, you know, inputs or suggestions of how to… to… Change that to make this, you know, different wording.
Open for… for suggestions here. So, the industry problem, obviously, we want to, wanna provide a… real-time, near-real-time telemetry data emission from COS applications written in those mainframe native languages, while obviously, you know, providing performance, security, and I say here low barrier of adoption, but that refers to what I said earlier on the SMF discussion.
Then, question for existing efforts, alternatives, obviously, there's this SMF-based approach.
When you look broader into the ecosystems, there are different types of technologies, agents, but, you know, when you look at this.
what comes from the distributed world, obviously, given the architecture and ZRA side, will not necessarily work. And then, specifically to the… to the emitter again, mentioned what I just said.
So, where we want to get to is, and this is probably kind of like the mission statement, emit telemetry from CS applications through OpenTelemetry, conform APIs, and then unprivileged asynchronous, and above.
the bar, processing pipeline.
**Matt Hogstrom** 10:13 Would it be fair to characterize that Ibm has instrumented their application runtimes, right? KICS, IMS, DB2, MQ, etc.
To emit, traces, And I think IBM's at least stated direction was they were going to continue to emit those through the data gatherer. So that's kind of one signal, but the other signals, like metrics, events, etc, they were going to leave to the monitors.
So, are… you mentioned traces in here. Is that really kind of a scope, since that's already being handled by the data gatherer for a mission?
**Jim Porell (Rocket Software, Inc.)** 10:53 Let me jump on that one, Matt, because I think part of the reason that, And I was gonna change the word applications to applications in middleware.
Because not all, you know, what we have is a view of what IBM's doing, but what is Broadcom doing for IDMS, for, you know, their proprietary middleware? What is BMC doing for their proprietary middleware? So, those actually factor into that weirdo environment, you know, operational environment that's not necessarily Java.
And CBASE. So, if we changed it to applications and middleware, then it applies to metrics, traces, and logs as well.
**Matt Hogstrom** 11:35 Okay, I think that's a good expansion.
**Rüdiger Schulze (International Business Machines Corporation)** 11:38 Yeah, and I concur that this is really intended to cover at least the three signal types.
Profiling, obviously, is a little bit of a different beast in this context, but, Definitely tracers would be included.
**Matt Hogstrom** 11:55 Okay.
**Rüdiger Schulze (International Business Machines Corporation)** 11:56 Yeah, so, that is this one. Then market adoption, now obviously, OpenTelemetry is there, you know.
enterprises are using it, financial institutions have it running in production in their distributed environment. When I expand into the mainfrain environment, there's various examples out there of customers who do that already. From a vendor and ecosystem perspective.
I put a very generic statement here, we can export this into the mainframe.
ecosystem.
Obviously, there's support, by the observability vendors, hyperscalers, let me put the mainframe vendors here as well, and startups, obviously, as well.
**Matt Hogstrom** 12:54 You know, I don't know if it's worthwhile to say that, because I think OpenTelemetry is clearly being adopted. The one thing that is a real problem is that every vendor is omitting it in their own way.
Which complicates the management of the ecosystem on the platform.
It's worse than that.
Well, I… okay, fair.
**Jim Porell (Rocket Software, Inc.)** 13:19 I mean, I'm seeing customers that think.
everything that you get, like, say, from AMIOps, as few, omegamon.
should be in OpenTelemetry format. And my question to them is, what problem are you trying to solve? You know, you know, it's OpenTelem's answer, what's the question? And it's really… what's the curated list of stuff that's necessary to do, you know, application stuff? Because again, the other conversation I have to coach them on is, are you looking for applications or infrastructure, you know, information?
And the majority of people that I see are, you know, what they really want is application stuff.
**Rüdiger Schulze (International Business Machines Corporation)** 14:06 So let me ask you in this round, I mean, obviously, this is somehow about this COS service, but, you know, we talk about this list of curated, sickness or metrics, right? Would you… would you see value if… Maybe as an adjacent project to this, or a separate project.
Actually, you start to… Publish a list of… the curated list of signals of C, which actually every vendor in this space can review, can comment on, can provide input on.
this is something that… I mean, we work on semantic conventions, but this is slightly different, right? The semantic conventions lead us to this… Curated list of, you know, telemetry that we wanna, wanna, wanna expose, and maybe, you know, across the ecosystem, agree on.
**Jim Porell (Rocket Software, Inc.)** 15:05 Me personally, I kind of think that we oughta, as we work on the standard naming conventions.
We use that as we start with the curated list, a curated list, and focus our attention toward that, and then it… It becomes more natural, Because then you can coach the vendors. You know, you can coach the analytics vendors, like, these are the ones that are going to be popular to have pre-built dashboards for. But then, same with the customers, is you don't want to expose every metric in the world, because these SREs don't know anything about mainframes. You want them to come back to… The monitors, if you'd like, for the subject matter You do want to detect stuff earlier.
I mean, again, we can send everything, but it's… I just don't see it happening, and I also see the MIPS being…
**Rüdiger Schulze (International Business Machines Corporation)** 16:01 Okay, spinach.
**Jim Porell (Rocket Software, Inc.)** 16:02 Down to a halt.
**Rüdiger Schulze (International Business Machines Corporation)** 16:03 Sounds like the answer is, let's focus the semantic conventions to what we would consider the correlated listers.
Damn.
By doing so, we arrive at the curated list, and the… You know, common naming scheme that we want to have, right?
**Jim Porell (Rocket Software, Inc.)** 16:18 Yeah, I think that's right.
**Rüdiger Schulze (International Business Machines Corporation)** 16:20 Okay, good.
**Jim Porell (Rocket Software, Inc.)** 16:23 That'll reduce the… by the way, that should reduce our effort, because you can say, yeah, that's not in scope, you know, let's focus on something else.
**Rüdiger Schulze (International Business Machines Corporation)** 16:33 Right. I mean, on the, on the particular issue that, that was mentioned on, the real challenge is that every vendor is kind of, like, sending in their own format, OpenTelemetry format.
Probably not on this slide. It's actually also… I suppose this is actually not really… it's… Not something that we can address directly with this project here. It's more than actually where the semantic conventions come in, supposedly, and being prescriptive from that perspective.
**Jim Porell (Rocket Software, Inc.)** 17:17 Well, I think one of the problems Otlp is very verbose.
In terms of… you know, we're doing it with Omegamon today as experimental, but it's like Prometheus. You have to define every single metric, label, all that kind of stuff.
And… there's a lot of technical debt. Now, as a vendor, we eat that, but when a customer starts doing it.
Then it… it gets complicated for them.
The interesting thing to me is that all the analytic vendors, and, you know, and that's… I'll start with IBM, Instana.
But, you know, Splunk, Datadog, Dynatrace, Elaster, Krafana, they'll accept any protocol.
You know, doesn't have to be OTLP. Now, once they get it, they can put it into OTLP format.
And that's, again, another one of the coaching that I give customers is.
The end game is you want to see topologies and that kind of stuff, you know, in an openTelemetry manner that uses this, but how it gets to that end destination, who cares?
You know, And this is where… and that's when, to Matt's point… and by the way, all these vendors.
That's what they're doing today, and then they're creating their own version of OpenTelemetry semantics, because it does not exist on ZOS yet.
**Matt Hogstrom** 18:48 Yeah, I was on a slightly different point, though. I was thinking, operationally, that since everybody's emitting it uniquely in their own product, configuration management is just kind of a nightmare. Like, for instance, oh, I have to go to IDMS and tell it to stop.
Or I have to go to Kicks and tell it to stop. And so, I've… my configuration has just kind of ballooned out across all the players. I don't have any kind of central management. Since ZOS is a densely shared.
infrastructure, that kind of, you know, distributed configuration and emission strategy is really a challenge, especially if you're on a a call in the middle of the night, just don't hit the stop it button, because it's just generating too much noise, right? I don't know if that's ever come up. It's still early days, but I could see that situation arise. So, I was thinking this was more of a way of helping to streamline that operationally.
As opposed to just the format of it being able to emit the data.
**Jim Porell (Rocket Software, Inc.)** 19:53 That's a really good point, yeah.
**Rüdiger Schulze (International Business Machines Corporation)** 19:56 Yeah, so, I mean, at least the project, how it was originally proposed, right? This is more really about giving these APIs to programs, to middleware.
I, I think the… the point that you make, Matt, is more about, The… if you look at the… right, and this is just the analogy, if you look at the… what the community is doing with OPMP, with the agent management protocol.
Have a central management plane where you can actually control what is being collected and also dynamically change this. So… Supposedly, that would be, again, a different flavor of project to… Alright.
**Matt Hogstrom** 20:49 Yeah.
**Jim Porell (Rocket Software, Inc.)** 20:51 Yeah, but I think… This is where… Driving adoption of a common service like this.
would help.
drive common operations.
At least on ZOS, so… There, there is, you know… Because vendors can decide, yeah, I'm just gonna do it my way, and we're back to Matt's problem.
**Matt Hogstrom** 21:20 Well, and it's… it's… if there is not a clear… up-and-comer, everybody's gonna do what they think is right based on their delivery schedule, right?
**Jim Porell (Rocket Software, Inc.)** 21:29 Yeah, I agree with that.
Yeah, it's… it's… we're chasing… We're chasing roadmaps that already exist.
**Matt Hogstrom** 21:37 Yeah, exactly.
**Rüdiger Schulze (International Business Machines Corporation)** 21:48 Yeah, I think this is all valid points. It's just, I think, it's maybe… You know, either in the opening or in the closing for tomorrow, maybe this is worthwhile to mention that there's actually potential for more in… in… related areas, Not specifically for this type of effort here, but, Obviously valid in the same way, right?
Right.
I think…
**Jim Porell (Rocket Software, Inc.)** 22:24 I think what you're saying, another way of saying that, is this is the tip of the iceberg.
It'll be… there's a…
**Matt Hogstrom** 22:31 a lot.
**Jim Porell (Rocket Software, Inc.)** 22:31 A lot of related things that could stem off of this commonality.
**Rüdiger Schulze (International Business Machines Corporation)** 22:40 Right, Then, at least, you know, in this template, obviously, there is also questions around how we, you know, as vendors, would support this project, how we ensure community is growing. There's various these questions as they come now. I assume for the time being that, you know, BMC proposed that The other three vendors, big vendors, are here on the call.
I assume there is buy-in and also willingness to contribute to this project in some shape or form.
**Jim Porell (Rocket Software, Inc.)** 23:17 I think some of that still has to be wrestled with. I know on our side, and I know having listened to, Craig Lothko, he'd probably say the same thing. I don't know, Matt.
**Matt Hogstrom** 23:28 Well, I was gonna say that I think the, I think there's interest, but the commitment is the piece… it's waiting for this to actually be proposed, articulated, scope.
et cetera, not just a, sure, I'll give you 4 people, and I'm not sure what you're doing yet. So, there's still… that still needs to be done. I assume that's the same with Rocket, and even IBM.
**Rüdiger Schulze (International Business Machines Corporation)** 23:52 Yep.
Right, yeah, this is about people, system programmers, application developers, language skills, eventually also somebody from enterprise observability.
then there's a technical charter, which was also sent around, so the project would operate, like, you know, more or less every open source project under CNCF, I suppose.
Then, yeah.
I mean… there are processes around how leadership is being determined for those type of projects. I kept it kind of like, you know, in a soap person way, but I think anybody here from this group, or anybody who would join and start to run this project is in some way involved with OpenTelemetry since a while. Also.
may be involved with the Open Mainframe project, and, obviously.
I think the intent is to bring up this project, Based on conversations that we had so far, and The aim would be to, to, you know, I assume tomorrow there will be an approval given by the TAC, then… you know, formally, we would set up the project trying to get this until the end of September done, and that should then also include that everything is in place to further define, you know, questions like scope, function.
You know, functionality requirements, maybe major architectural decisions, things like this, that may then influence further Activities around this project.
Okay. Then recently…
**Matt Hogstrom** 25:50 I'm sorry, can you… can you go back to the previous one? The, succession planning and continuity, that almost sounds like, you know, planning for the… Switching of people in the project.
But this is talking more about how to bring the project online, is the description. Am I misunderstanding what that means?
We talk about that, like, at Broadcom. What's my succession plan? When so-and-so retires, who's going to come in to replace them? That's more of a project management, once it's up and running, not a bootstrapping.
**Rüdiger Schulze (International Business Machines Corporation)** 26:25 I see what you're saying, right?
Yeah, that's a good question. I mean, in this form, I mean, what would we answer there, right? I mean, we need to bring up the project first.
**Matt Hogstrom** 26:40 Exactly.
**Rüdiger Schulze (International Business Machines Corporation)** 26:41 I, I…
**Matt Hogstrom** 26:42 I think it's, yes, we will, once the project's approved, right?
**Rüdiger Schulze (International Business Machines Corporation)** 26:47 Yeah, and once it's there, and once it's running, and proves to be… Having attraction, then… then I think it will continue, right?
**Matt Hogstrom** 26:56 Yeah, okay.
**Rüdiger Schulze (International Business Machines Corporation)** 26:58 Right.
Critical resource requirements. Obviously, COS system access, Chitub already in place, but, GALASA could be used.
It's a little bit fuzzy here, if you have some recommendations what to put there, contributor attraction, obviously the regular game, OMP blogs, promoting the project, what is not mentioned here, but what we just discussed, right? Also vendors internally agreeing on putting people on this.
And then, retention, foundation leverage.
Would have to look up what exactly was given there on the template, but, Point was essentially about also, you know.
proving and showcasing that the project is alive, right? So, to, actually… you know… Create visibility around the project.
Okay.
then resource coexistence and impact on our users. This is a little tricky, but at least when I look at, from our company's perspective, I mean.
I expect to become people on that, you know, are not necessarily open source or OMP contributors at that time.
And, however, they are familiar with the topic, and to contribute, so there would be not this major issue of overlap.
And, I mean, infrastructure access, obviously, there's a process now through the OMP. I think it will be a mix of OMP resources, but… plus probably, you know, internal resources of the contributing companies.
Interesting, it becomes then when it's really about performance testing. There's probably nothing that you can do with OMP-provided resources. That's probably something that would happen at some point.
internally, But I suppose once we get there, I think then also the maturity of the project would be a different one, to look at this.
And, portfolio migration strategy. I mean, the… I put kind of, like.
statement in here which says, I mean, these OMP projects, they start from sandbox, go to incubating to active.
I mean… Trying to somehow be reasonable in terms of You know, putting this project really to life.
With, you know, maybe a first release in the beginning of 2027.
And… and then… You know, we will see how the further adoption is, and also what feedback there is, and… maybe with a chance to move this to an active state. I mean, this… I mean, we… what we don't want is, like, with all these projects, obviously it may take longer to get to active, but to put a target here, I would say in two years, this is… Two years is in… in this fast living time, it's already a long time, but it's maybe something to… And I still oversee.
Right.
Yeah.
**Matt Hogstrom** 30:42 I… when you talk about resources, I'm thinking right now the ZOE project has a number of resources at Marist.
When you talk about resource coexistence, are you really talking about that kind of thing?
Because ZOS resources are… well, they're hard to come by in the open.
**Jim Porell (Rocket Software, Inc.)** 31:05 Yeah, I was thinking this was… from other OMP projects, not other.
**Matt Hogstrom** 31:11 Okay.
**Jim Porell (Rocket Software, Inc.)** 31:11 Broadcom, Rocket, IBM projects.
**Matt Hogstrom** 31:14 Well, the reason I was saying is because the one resource that you have to have, and it's on the previous slide, is access to ZOS systems. Right. So we would have to go dip into the Marist pool.
And possibly, dilute them as well. So, just something to consider.
**Rüdiger Schulze (International Business Machines Corporation)** 31:33 Is the Marist pool actually the OMP pool that…
**Matt Hogstrom** 31:37 No, the mayorst out of the goodness of their hearts.
**Rüdiger Schulze (International Business Machines Corporation)** 31:41 Yeah.
**Matt Hogstrom** 31:41 Of course, a couple of minis.
For Zoe. So we would be either adding to that burden, because I wouldn't expect Zoe would want to share their minis, right, because they have it for their testing and their processes.
So, we'd have to figure out where to get it.
But… I would suggest strongly that IBM throw a Rock Hopper or a Linux One system somewhere, and we start spinning up ZVDTs to satisfy the need in some hosted environment, but that's just me.
**Rüdiger Schulze (International Business Machines Corporation)** 32:11 Yeah.
There is a lot of this process with the OMP, I think this is… relatively new, where you can request COS access for approved OMP projects, so maybe that's maybe the way to go down here.
**Matt Hogstrom** 32:27 Okay.
**Rüdiger Schulze (International Business Machines Corporation)** 32:28 And, right.
Hey, Yash. We go over a set of slides which will be presented to the Open Mainframe project tomorrow, which is part of the CNCF, and this project here is related, that is being proposed here is related to OpenTelemetry, so we use this meeting to… to discuss the input preparation for this, just FYI.
So, codebase origin, so, My current view is there's no existing codebase. I mean, there's obviously reuse, I think I kind of, like, touched on this. I rather expect people with experience to come to this project, but it would be a newly developed project under the OMP, so there's no… no heritage or, you know, donation of code in this way, but, it's… skills that I expect to… Don't count.
Right, and that's the template. So that would be the DAC for tomorrow.
**Jim Porell (Rocket Software, Inc.)** 33:40 That looks reasonable.
**Rüdiger Schulze (International Business Machines Corporation)** 33:44 Good.
Actually.
**Jim Porell (Rocket Software, Inc.)** 33:46 I think they're quite… Yeah, the question comes back to, like, okay… What's the executive buy-in, you know, now neces… you know, that's necessary to actually start putting people on this, We gotta figure that out.
**Matt Hogstrom** 34:04 I would suggest almost at the very beginning, and maybe it doesn't follow the template, but what's the business value this intends to deliver to customers and vendors?
Just kind of state that, because at some point, when you're talking about releasing.
You really need to focus on something that's going to have an immediate impact, and not the promise of something in the future.
So… is the… you know, if you were going to make this statement, the goal of the project is to enable COBOL and other languages on ZOS to be able to emit Data so that… they would have a complete end-to-end view of the mainframe along with their distributed infrastructure, right? Is that the business value?
Dude.
**Jim Porell (Rocket Software, Inc.)** 34:52 This was just…
**Matt Hogstrom** 34:53 this is all very, kind of, technically oriented, and if somebody looked at it like, well, okay, that's a great technical thing, but what do I get out of it?
**Rüdiger Schulze (International Business Machines Corporation)** 35:01 Right.
No, I think it's… that's actually exactly what you said. I mean, in all honesty, we had people coming to us and saying, we want to have OpenTelemetry SDK for COVID, and we asked, what do you want to do with it?
**Matt Hogstrom** 35:16 Oh, my God.
You know, I want one first and play with it.
**Rüdiger Schulze (International Business Machines Corporation)** 35:22 Yeah, but, yeah, I think it's the broader set of, actually, potential exploiters that would benefit from this to also.
**Matt Hogstrom** 35:32 That was a book.
**Rüdiger Schulze (International Business Machines Corporation)** 35:32 point. I mean, it's… it's… actually, okay, I put a couple… I will put a couple of, bullet points there. So, the COBOL one is one, but obviously, if… if you look at this from the platform perspective, it's really about the ecosystem. I mean, it's the capability to Have a more easy way to support the three signal types at a… at a… Producer side, data producer side.
**Matt Hogstrom** 36:02 And so, is the… as I'm just asking questions that… Because I haven't been involved in the previous discussion, so… It sounds to me like there's really two deliverables that would have to come out of this. Number one would be the SDK for COBOL, if that was the initial priority, which makes sense.
And then you have to have a platform to receive those signals, transform them, and then emit them from the mainframe. So it's kind of two pieces of what you're working on, right? Would be the API and the emission.
**Rüdiger Schulze (International Business Machines Corporation)** 36:34 That's right, right. So there's two layers, what is being reported as two layers, right? The one is the, the, where you do the ingestion could be… you could refer to this as a sort of SDK, right? And then there's the… You know, and another component to it, to export the data.
**Matt Hogstrom** 36:59 I guess my point is you're probably gonna have two different teams working on it, not one team working on everything.
I would think.
**Rüdiger Schulze (International Business Machines Corporation)** 37:08 That's a good one.
So what I realized, looking at this, I mean, it's easy to put a kind of, like, a very, very thin OTELConform API there, right? Think about a couple of attributes, and COBOL, you copy this over.
The real fun comes in when you look at the complexity of, for instance, the metric API, because there is lots of different ways of, How you can actually collect, measurements, or different type of measurements, so you… to be fully compliant. It's some effort, right, to put all the specifications in there.
On the other hand, once, you know, you iterated through this and done this, then it's, you know, it's also… if it really comes down just to, let's say, defined data structures.
Then it's also an overseeable effort.
Central.
The interesting part is probably this circular ring buffer, or similar technology, to make this reliably work and stamp this up. I mean, from reusing the OTEL SDK, there are some… So, so obviously, this is what we did with, with DMITO earlier.
It's technically possible. There are some interesting considerations around these SDKs, how to feed the data.
But, Once this is kind of, like, solved, that's… that's… probably then, you know, rather straightforward. So, I think that there's, you know, once agreeing on this mapping.
approach API, so… I mean, obviously, there's the API spec, but, each, each, let's say, implementation has, then, its own way of interpreting this, this spec and making this, this hotel conform. That's, that's kind of like, the one aspect, and then, obviously.
I think I said this on earlier calls, I'm not a COBOL developer, right? So getting somebody who actually, you know, with the classes of a COBOL developer, with the classes of an assembler developer, who looks at this and kind of, like, judges, this is the format we want to have that, right? Or…
**Matt Hogstrom** 39:33 Right.
**Rüdiger Schulze (International Business Machines Corporation)** 39:34 It's most reasonable. And… I mean, the… yeah, and then the… you know, then it… call it memory service, or whatever, buffering service.
I mean, there were reasons why we chose SMF, like, two years ago, right? So this is really making distance stable, that's kind of, like, the key.
**Matt Hogstrom** 39:58 Well, to be honest with you, when I was at IBM and we did CDP, this is actually the CDP architecture.
There's the data gatherer, there's the SMF parser.
**Rüdiger Schulze (International Business Machines Corporation)** 40:09 Yeah, no.
**Matt Hogstrom** 40:10 And at some point, I would say on the left side is the SDK for the applications, which is one deliverable. Then the second one is, where am I intercepting that data? I think SMF is pretty good, because we use the same approach for IMS logs, right? We wrote them to SMF, records, which we basically intercepted, and then deleted. Said, don't save them, and we just used it as a highway to move the data across, and then… then you're into the, I got the data, let me enrich it, format it, and send it out. So, I actually… I don't know anybody on the CDP team at IBM today, but this would almost seem to be kind of in their wheelhouse, which I would think BMC Data Streamer and even Iron Stream would.
Fit the right side of the equation.
So I guess the question is, are we… the left side's very clear to me, that would be an API, and then you have to send it somewhere, but then you could have several different implementations of the right side.
**Rüdiger Schulze (International Business Machines Corporation)** 41:08 That's correct, actually.
And that's a question that we also have been discussing. I mean, it's actually a good question also about the scoping of the project, right? So, obviously, the left side is something that needs to come online, but the right side actually could be… we could say there is some sort of, again, defined interface. There can be vendor implementations, there can be… I said it already, different SDKs could actually plug in, right? Depending if you're… what's your favorite one, choose it. So, we can actually…
**Jim Porell (Rocket Software, Inc.)** 41:43 Can I share for a second? Because I think I got a slide that covers it, I think.
**Rüdiger Schulze (International Business Machines Corporation)** 41:47 so…
**Jim Porell (Rocket Software, Inc.)** 41:48 what you just said… if I… where's that share button?
Oh, there it is.
No.
So, I think, you know, this is an old diagram, I think, when it first started, but… What you're talking about is this thing here.
You know, this OpenTelemetry emitter. Now, the question is, is the IBM one… open enough that anybody can use it, or is this a price thing? If it's a price thing, then there's some value in having an open source one.
For anybody to use, but if this was… I think we kind of need a view as this… open technology.
You know, or common technology that's going to be there, or is it in some… I don't know how this is being sold or distributed.
**Matt Hogstrom** 42:46 Yeah, I don't know either. I just remember when we had the initial call, I think Rudiger, you were on those, that at the time, IBM said the data gatherer was effectively for emitting spans from the middleware, and they had no intention of opening it up for metrics or other signals.
**Jim Porell (Rocket Software, Inc.)** 43:02 Okay, if that's true, then yeah, I didn't…
**Matt Hogstrom** 43:05 That was a point in time, maybe they changed it.
**Jim Porell (Rocket Software, Inc.)** 43:08 No, I believe.
**Matt Hogstrom** 43:09 That's where I think we were left with, okay, that still needs invention, right? That's part of the equation to really balance this out so it becomes a solution that's usable.
**Rüdiger Schulze (International Business Machines Corporation)** 43:19 So let me ask a question here.
And don't, you know, don't focus too much that this is part of the data gatherer, okay?
By the way, the emitter is part of the base operating system, so it's coming without any license fee.
Okay.
It's also the reason why I want to put this question here. So, I mean, one thing, obviously, with what we discussed, and maybe let me put up the screen here.
Also to… maybe help the project to… to… to move forward. One thing that you could obviously imagine is that at this other Enchronous export layer, this emitter would sit, but not taking the data from SMF, but taking the data from You know, whatever technology, circular ring buffer memory service, we decide for, right?
As I also said, right, there's not necessarily an intention to distribute the code of the emitter, but the emitter is part of the operating system, right? So, from a… From your perspective, would it be an acceptable… approach, when we would say, okay, we scoped this project to focus on the ingestion layer, or what we call the COBOL SDK, right? So these different mappings.
Focus on building the circular ring buffer or similar technology.
The emitter, obviously, adopting this.
And then being built into the operating system.
Providing, kind of, like, natural stream of this formatted, telemetry through OpenTelemetry, to… to any consumer, really.
**Matt Hogstrom** 45:21 When you say the emitter is part of the operating system, what specific component are you talking about?
**Rüdiger Schulze (International Business Machines Corporation)** 45:26 So the… there's… we refer to this to the COSO telemetry emitter, which is packaged with the data gatherer.
But the data gatherer is a… so, just for full completeness, the data gatherer comes in two flavors. There is a… there is a version which is part of the base operating system.
free of charge, no fees apply. I think it's a separate ID that you need to… to deploy. There's also an advanced version, but I'm not talking about the advanced version, right? I'm just talking about what's coming with.
The advanced… sorry, with the data gazr, which is part of the base.
licensing.
And, the emitter itself, that's a component… you could almost think of it like a standalone component. It's packaged with the data gatherer, but it's not having… Lags into the data gazr as such, right?
**Matt Hogstrom** 46:31 Okay.
So you could basically use that and harvest that component out. Is that actually a supported configuration, or just happens to be software that could be used, but there's not… it's not officially supported?
**Rüdiger Schulze (International Business Machines Corporation)** 46:45 Gotcha.
**Matt Hogstrom** 46:46 in the context of the.
**Rüdiger Schulze (International Business Machines Corporation)** 46:47 I mean, this would be future discussion, right? But it could be becoming, you know, if the respective servers would be… that we discuss, or Playano becomes live, right? Could be a supported configuration, obviously, from an operating system point of view.
**Matt Hogstrom** 47:03 Okay.
I… so the reason I'm asking, we have a… we have a component, called the Data Gatherer, or not the data gather… I'm sorry, Data Mover.
Which is part of our common services.
And it uses a, basically we have this idea of… think of it as, kind of like a Kafka bus. It's not Kafka, but we use things called categories.
Where any product on the system can make a PC call in and put something into a category. And then this is… it's kind of a broker, so if there's an interested party in that category, it then forwards the data off to that… that interested party. It also has an SMF component.
That will read SMF data and then forward that to interested parties as well.
So, that's why I'm trying to understand, because I originally thought, well.
That might actually be a compelling base set of capability, if that's something that would get approved internally, I have no idea if it would or not, to donate that, because then that kind of bootstraps this whole intermediate layer.
Because it has.
**Jim Porell (Rocket Software, Inc.)** 48:11 Believe it.
**Matt Hogstrom** 48:12 The ring buffers and everything are already there.
**Jim Porell (Rocket Software, Inc.)** 48:15 And even if it's not, donated… since it is in the system, you know, as a free thing in the system, is it something that you augment with, like I… like you said, if it's only doing traces.
We can leverage that kind of infrastructure for.
metrics and logs, yeah.
You know, or at least emulate that functionality so it's consistently applied.
**Matt Hogstrom** 48:42 Yeah. The only reason I bring this up is, if you get everything instrumented on the left, but you don't have a highway to move it, it's not gonna do you any good.
**Jim Porell (Rocket Software, Inc.)** 48:52 Oh, I think he's…
**Matt Hogstrom** 48:52 These are two completely highly related and dependent pieces as part of El Plano.
**Jim Porell (Rocket Software, Inc.)** 48:59 Right.
Agreed.
**Rüdiger Schulze (International Business Machines Corporation)** 49:03 Yeah, so, I mean, as we said, right, there's obviously different ways in terms of realizing the right side of the slide, the highway functionality. I mean, obviously, as the project evolves, we can discuss if… You know, there are… Once we kind of, like, define what this is and how the data is being obtained.
we can discuss if there are certain fast passes also for adoption, right, using Excel.
**Matt Hogstrom** 49:35 Isn't cool.
**Rüdiger Schulze (International Business Machines Corporation)** 49:35 Who knows?
Sounds like, you know, from your perspective, the data mover could do something similar, like.
What the emitter could do in future, so it's…
**Matt Hogstrom** 49:47 I mean, at the end of the day, we're just ripping data off of SMF, or off these categories, forwarding it and processing it, right?
**Rüdiger Schulze (International Business Machines Corporation)** 49:54 So, from an ecosystem perspective, it sounds like there's different ways of implementing the highway, right?
**Matt Hogstrom** 50:05 Yeah.
**Jim Porell (Rocket Software, Inc.)** 50:06 Yeah.
And that kind of comes back to, you know, do any of the vendors want to contribute something? Because, I mean, we have… Our data provider as well.
Java-based, On the OTLP side, I'm like, I don't think it's the greatest implementation, but… Could be.
**Matt Hogstrom** 50:33 Well, and that's where…
**Jim Porell (Rocket Software, Inc.)** 50:34 too.
**Matt Hogstrom** 50:35 This is, making the project out of stone soup.
**Jim Porell (Rocket Software, Inc.)** 50:39 Yeah, yeah, yeah.
**Matt Hogstrom** 50:39 Everybody's gonna bring something to the party, hopefully.
**Jim Porell (Rocket Software, Inc.)** 50:42 Yeah, right.
Stone soup, oh my god, now I feel.
**Matt Hogstrom** 50:47 Takes you back to elementary school, doesn't it?
**Jim Porell (Rocket Software, Inc.)** 50:48 Exactly, thank you for that one.
**Matt Hogstrom** 50:50 You're welcome.
**Rüdiger Schulze (International Business Machines Corporation)** 50:56 Okay.
**Jim Porell (Rocket Software, Inc.)** 50:57 Because…
**Rüdiger Schulze (International Business Machines Corporation)** 50:57 Good.
**Jim Porell (Rocket Software, Inc.)** 50:57 Yeah.
**Rüdiger Schulze (International Business Machines Corporation)** 50:58 Yeah, go ahead.
**Jim Porell (Rocket Software, Inc.)** 50:59 No, no, I was just gonna go on the side. I got invited today to Grandfather's Day, Grandparents' Day on April 2nd for my granddaughter's first grade class, so… It's like, it was the perfect time to bring up that analogy.
**Rüdiger Schulze (International Business Machines Corporation)** 51:15 Does it come from the Flintstones, or where does Stone.
**Jim Porell (Rocket Software, Inc.)** 51:17 No, it's a parable where villages, everybody's hungry, and this tradesman comes in, and he goes.
Oh, I can make a soup out of stone. And they're like, what? And so he puts a big pot on the water, throws a stone, and then says, hey, you got any carrots? And people slowly start bringing in things, and all of a sudden, it's a soup for everybody.
**Rüdiger Schulze (International Business Machines Corporation)** 51:44 Okay, yeah, I see the point, yeah.
**Jim Porell (Rocket Software, Inc.)** 51:46 Yeah.
**Rüdiger Schulze (International Business Machines Corporation)** 51:47 Yeah, maybe it becomes something like this, yeah. Sounds good.
Okay, I add one slide at the beginning, business value, and then let's have the meeting tomorrow.
I suppose it goes through, let's see what the comments are, and then… And look at, you know, logistics and things like this.
**Matt Hogstrom** 52:10 Okay. Just a heads up, next week I'm gonna be in Plano, so I… I'm gonna try to make the… the meeting, but I don't know if I'll be able to or not, depending on what activities we've got going out there.
**Rüdiger Schulze (International Business Machines Corporation)** 52:21 Yep. Okay, good.
**Jim Porell (Rocket Software, Inc.)** 52:23 Alright.
**Rüdiger Schulze (International Business Machines Corporation)** 52:24 Are they focused on…
**Matt Hogstrom** 52:25 Sorry, did I say Plano? I said… I meant frog.
I see Open in front of me.
**Jim Porell (Rocket Software, Inc.)** 52:31 They can say hi to all our recent, rocket transferees to the…
**Matt Hogstrom** 52:37 You bastard.
Well, that's a… it would be an interesting discussion to have with you.
But…
**Jim Porell (Rocket Software, Inc.)** 52:47 Yeah.
I don't know.
**Rüdiger Schulze (International Business Machines Corporation)** 52:51 Okay, beautiful.
**Matt Hogstrom** 52:52 You're doing good, thank you, Rudiger.
**Jim Porell (Rocket Software, Inc.)** 52:54 Yeah, thanks a lot.
**Rüdiger Schulze (International Business Machines Corporation)** 52:55 Go ahead.
**Jim Porell (Rocket Software, Inc.)** 52:56 Bye.
