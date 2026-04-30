SIG: OpenTelemetry on Mainframes Weekly Meeting
Date: 2026-04-29
Duration: 17 minutes
Zoom Recording URL: https://zoom.us/rec/share/jvPybtPiGWuzGDbPnLKxhkIZlxNBj2gZS3OQxvhWazpFb30Waw5SIvgwDIzXfdt0.KhlZh74dfMqeT7WL
============================================================

## Zoom Recording Transcript

**Jim Porell** 00:08 -Oh, where is everybody again?
Craig says he can't make it, yeah, and you're on there waiting to join, Antoine, so…
**atoulme** 00:23 -Oh, what is that stuff?
**Jim Porell** 00:27 Oh, I… by the way, Antoine, the… says host has another meeting in progress. I brought that up to, What's that? You are.
That's new.
**atoulme** 00:39 Let me see, we need to nuke this guy out. Oh, he's… Okay, so… FFE… What?
**Jim Porell** 00:54 Yeah, I'd never heard of that before.
**atoulme** 00:56 Oh, this happens a lot. Boom.
**Jim Porell** 00:59 Okay.
**atoulme** 01:00 It's annoying.
It's really, really, really, really bad. Like, people will do this in… Not interested. If you want to show, come… come to our meeting. Don't… don't send your AI. Thank you.
**Jim Porell** 01:13 I've never seen that before, so that was a new one to me, so…
**atoulme** 01:19 Oh my, you live a coveted existence, please tell me. Tell me your ways.
I have dealt with this way too much.
When the collector sigs, this is a daily occurrence, if every time we have a sign meeting that happens.
That's the first 5 minutes of our meeting.
**Jim Porell** 01:37 Okay.
I did see, regarding the host meeting is already being used by somebody else, I brought that up to Morgan in the last call, or two weeks ago, I think.
And he mentioned that it should be set up so that multiple people can use the same Zoom, but there might be a finite limit of simultaneous meetings, so… I don't know, he was gonna look into it.
**atoulme** 02:03 Yeah, it's, probably just… Previous meeting running over.
Wednesdays. I don't know if you've seen the… the calendar for, OpenTeometry meetings, but…
**Jim Porell** 02:17 No, I…
**atoulme** 02:17 A version of it.
Let me shut my screen, I'll show you.
**Jim Porell** 02:23 Genoris, yes, I see your text, you are in the right place.
Oh my goodness, what?
**atoulme** 02:32 That's what the week looks like.
**Jim Porell** 02:33 Okay, well… well, there's a lot of simultaneous meetings, yeah, so…
**atoulme** 02:38 Believe we have up to 4.
maybe 5 different Zoom accounts at the same time, and each of them have to have a different… so… This is event count number 2.
Zoom account number one. So today.
We are here. Zoom account number 4.
The technical committee meets from 8 to 9, is using the same account.
Naturally, if they run over, then we're competing for access to the same Zoom account.
**Jim Porell** 03:07 Okay.
**atoulme** 03:07 So that's what's happening.
**Jim Porell** 03:09 Alright, thank you for sharing that.
**atoulme** 03:11 Yeah, it's available from the, GitHub OpenTeametry community web, README, so I'll just put that in. If you're ever interested, find out more.
**Jim Porell** 03:21 Alright, thanks.
**atoulme** 03:23 Okay, and with that, maybe you should just get going. So, I'm gonna share the meeting notes here. I can also share my screen, make sure we're doing a good job of being good citizens, of Passing things around. So the way it works is that we create a new section on every meeting.
And we have two things in there. One is the attendees.
And you can put your name, affiliation, you don't have to, I'll just put mine to get started.
I encourage you to do the same.
And then agenda items.
Agenda is freeform, you can add stuff during the meeting, or we can capture things that we discuss.
And then as much as possible, we… we document that.
Okay.
**Jim Porell** 04:20 Yeah, so… and the other thing to point out, Yoris, since you're new here, and hopefully… am I pronouncing that properly? .
**Joris Yangsheng Xu** 04:30 Yes, you're… can you hear me?
**Jim Porell** 04:33 Yes, yup.
**Joris Yangsheng Xu** 04:33 Yes, yours is correct.
**Jim Porell** 04:36 Okay, and is Shu his last name?
**Joris Yangsheng Xu** 04:39 Yes, yes.
**Jim Porell** 04:40 Okay, so normally we have a little bit larger quorum than we have today. In particular, Rudiger, Schultz is our spiritual leader, and Greg… Greg Shriver is the, kind of, the backup. And neither of them are here today.
So… you can look at, again, look at prior meetings, where the status of PRs are and stuff like that. I'm gonna suggest it's interesting to… since you've joined, why did you join? What are you looking for? Probably worth capturing here.
**atoulme** 05:18 Yeah.
**Joris Yangsheng Xu** 05:18 Just to learn, I guess, and, I hope to contribute, someday, I think it was, Angelica, who I've met, Heinrich from Broadcom, who gave a talk about, observability Hotel at GSUK, for the first time.
And, yeah, I spoke to her, and… Learned a little bit about it, and… I thought it could be useful to… To experiment, learn a bit, and try to see how it can help at my internship.
**Jim Porell** 06:04 Oh, is that… are you doing an internship at Broadcom?
**Joris Yangsheng Xu** 06:07 No, I am doing an internship at Serabobank in the Netherlands.
**Jim Porell** 06:14 Oh, okay.
**Joris Yangsheng Xu** 06:14 A big bank, yeah.
Yep.
**atoulme** 06:18 That makes sense.
Okay.
Yeah, we can talk about the existing work. My understanding is that… Right now, we have open PRs here. You can take a look.
What else do we have?
So let's give it… TPS, what is TPS thing for?
Transaction Processing System, okay. So in the CMT Conventions repository, we have work that is ongoing, and if you can take a look here… You will see that this is highly… You know, it's just, like, driven definitions of Everything there is to know about the attributes that you would apply To different items that are part of a mainframe, right?
So, for example… Actually, this, all of this, all of those docs, as far as I can tell, are actually derived from a YAML file.
So let's try to go to the source, here.
Okay.
So, CICS, or KICS, we're going to have… Here, some sort of a… Information here about the server.
Whereas the span name should be the system name and space transaction ID.
Spencer.
server, split status… So… We'll have some level of attributes, which are required.
The name of the system, example, IBM Kicks.
The TPS facility type could be IPIC or MRO, and you have references to that. Same goes for entities.
So, entities are a new concept in OpenTemmetry. They define, elements of your infrastructure, like a host, a node in the communities cluster, and in that case.
a transaction processing system with GPS is going to be part of that.
So, it's currently in development, as you can see.
And then you can see how this is being defined as, with a number of attributes.
And the main one's just the region, to identify where it's coming from.
And then so on and so forth, right? So, if you have any questions about this, this is kind of the output of this group.
is…
**Joris Yangsheng Xu** 08:45 Yep.
**atoulme** 08:45 Standardizing how we talk about a, A mainframe, and how we are going to represent this information in a codified way that will allow us to show that to our customers and make sure that they are able to understand the metrics, the traces, the logs that are being stamped with the same attributes, so that they can make sense of what's going on.
So, just for what it's worth, it's… it's a pretty complex topic, and semantic conventions is also bulking under, like, the amount of change in requests coming in.
So, it takes a while to get things in. If you look at the conversation, it's at 80 comments.
Which, unfortunately, Takes a while.
And I think it's, It's ongoing, so if you have any feedback on this, or anything you'd like to understand.
Please, please feel free to go and review that. Is there any way you'd like to be able to define your spans so that you would be able to pinpoint where they're coming from? That would be a great way.
That's one.
The next one, so there's been some work on that.
Looks like as of last week, and I wasn't aware of this, of diggers construing backing off of this PR for now.
And then there's some… Docs PR also pending.
From the mainframe seek.
That's meaningful. So that would mean that the OpenTeometry.io website would start to have a section dedicated to mainframes.
So, here we're having some healthy discussion.
It looks like it's been approved. Some changes that are required, so CI doesn't pass, but this is… Fixable, it's usually about the format, nothing else.
And then if you look at the actual code here, it's new.
It's a new index file for mainframes, so… Feel free to review and produce that, and if you can help us move it forward, that would be very appreciated.
Okay.
No.
Oh.
There's just one open issue for this, duty to the collector.
**Jim Porell** 11:12 I don't think they've made any progress on it.
**atoulme** 11:14 Oh, really?
**Jim Porell** 11:15 They're not sharing any progress, I don't think, because I think it came into IBM as a problem.
**atoulme** 11:21 Oh, good to know.
**Jim Porell** 11:23 But I think the interesting thing here, Antoine, I don't think you've been part of those conversations, is that Z, by its nature, has the ability… if you turn on OpenTelemetry for all applications and stuff, the volume… Of traces that it might send out is humongous.
So… a customer tried out, I think, the IBM implementation of the collector on Linux for Z, and said it was terrible.
My hypothesis is, if it was on x86, it would be equally as bad. That it might be more of a volume issue than it is about performance.
you know, I… so I don't know. I asked them to investigate that, and… I haven't seen anything resulting from that yet.
**atoulme** 12:19 I'm tempted to just close this issue as cannot reproduce.
**Jim Porell** 12:23 Maybe him.
It's been out there… been out there for a while, yeah.
**atoulme** 12:31 Yeah, the thing, we're not in the business of gathering tickets and getting them right. Right, exactly. We can either fix it or get off of this if they cannot help us, understand.
Yeah, they just opened that ticket, and that's why they have a GitHub account, so they… they're not particularly… this is the first and last time they use GitHub was to report this issue.
**Jim Porell** 12:55 Yeah, there you go.
**atoulme** 12:56 Well, unfortunately, that's not gonna get where they want us to go. It's a good signal that there's some usage on S390X of the collector. We do have very limited support for it at this time, we just make sure it compiles for this platform, but we actually never we don't know if it performs for all the use cases that you can think of, right? So, has to be careful.
Okay, so that's where we are. If… Any other questions? Anything else you'd like to talk about, Doris?
**Joris Yangsheng Xu** 13:28 No, I… I mean, my intention was to follow just, observe for some sessions, and then jump in when I learn a bit more about, hotel.
**atoulme** 13:42 Yep, well, you're very welcome, thank you for joining.
**Jim Porell** 13:47 I think the other thing that's important is, at the top is the Slack channel. You might want to join that, because that… well, at least you'll see if there's any changes to meetings, and or if key people aren't going to show up or not.
**atoulme** 14:01 Let me change that.
**Jim Porell** 14:04 Yeah, thank you, that's good news.
**Joris Yangsheng Xu** 14:07 Angelica, mentioned to me that the… OpenTelemetry I.O. training.
is a good way to start. I was wondering if you have any more, like, resources on, where to learn about it?
**atoulme** 14:27 It depends what are you… it depends a little bit on what you're trying to achieve, because… We have a lot of surface in OpenTeometry. We have people who are practitioners from application development who would want to have OpenTeometry in their applications.
We want… we also have operators who use the collector.
So.
**Joris Yangsheng Xu** 14:45 I'm… yeah, I'm working on, infrastructure.
Like, mainframe Sysproach, middleware kicks.
Like, those kinds of things.
**atoulme** 14:57 In that case, you would want to use the collector by default, I think.
is that the collector is going to be well-defined in this OpenTeometry I.O. training.
It also has… Yeah, I think that's the best tutorial. If you'd like to take the… there's a CNCF training as well. Maybe you can ask Angelica to get a seat on the education side of the Linux Foundation and get certified. Yeah, that's a perk for your internship, to make sure that you come out of this thing. I actually went through this.
You know, otherwise… To get started with a collector and understand some of the elements of it, there's, I think a registry that has all the, elements of OpenTemmetry, so if you have a question, like, what can you do for me?
That might be a great way to pull off some ideas.
For example, I want to get host metrics.
**Joris Yangsheng Xu** 16:00 I think maybe also… Good to mention is, the… I am learning, OpenTelemetry, for, like, myself, so it's not for Robo Bank specific.
**atoulme** 16:15 Okay.
Yeah, I think that conflates with the goal anyway. So, OpenTechIO, yes, you can try the demo, maybe that's a good way to get started here, depending also a bit on the language and your interest for running all of this, or part of it.
We can also just run the demo here in Docker and Kubernetes, just to try things out. It can fit on the laptop, but it's… As you can see, it's starting to balloon up, there's a lot of things going on.
From there on, you can read a bit more about, like, architecture and things like this.
**Joris Yangsheng Xu** 16:50 Yep.
**atoulme** 16:52 Yeah, that will get you going.
**Joris Yangsheng Xu** 16:56 Alright, thank you very much.
**atoulme** 16:59 You're welcome.
**Jim Porell** 17:02 Thanks, Antoine.
**atoulme** 17:04 No problems.
If there's, anything else we should talk about?
**Jim Porell** 17:09 I think that's probably about it, you know, if there's… These other folks aren't there, then probably just… Cold stay.
**atoulme** 17:17 Let me check the slide real quick, nobody is pointing… no.
Okay, alright, I'm gonna drop off. Thank you, everybody. Have a great day.
**Jim Porell** 17:25 Alright, bye-bye.
**atoulme** 17:26 Bye.
**Joris Yangsheng Xu** 17:27 Alright, have a great day.
