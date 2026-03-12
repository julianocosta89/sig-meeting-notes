SIG: OpenTelemetry on Mainframes Weekly Meeting
Date: 2025-11-05
Duration: 32 minutes
Zoom Recording URL: https://zoom.us/rec/share/w8BewCcwK26O3ohNuV-yZIiQhXBgnDf06X-MOI7ARtefx2ARmJkWEDZSb_0UBuEV.Cmxfg9Q0QpMxfA_u
============================================================

## Zoom Recording Transcript

**atoulme** 01:17 Hey, everybody.
Hey, Greg.
**Greg Shriver** 01:22 Hey, hello.
Morgan says he has a conflict.
**atoulme** 01:36 But fame.
**Greg Shriver** 01:38 What's that?
**atoulme** 01:39 It's a theme. His life is a long, overdrawn, double-booked calendar.
**Greg Shriver** 01:46 Devilable calendar, right?
**atoulme** 01:52 So… well, I mean, also, like, realistically, like, he's on the same time zone as me, we're on PST, and… Europe… EST, everybody's trying to get time from us, like, from 8 to 11 is a really critical time.
Okay, so I'm trying to find the SIGDA notes…
**Ruediger Schulze (IBM)** 02:13 Hi there, by the way. Greetings from the GS UK, which is a mainframe conference, and we… We… obviously, we talked a lot about OpenTelemetry, yeah.
**atoulme** 02:25 Oh, great. Good fees, I hope.
**Ruediger Schulze (IBM)** 02:28 Yeah, so, continued interest, you know, we talked about native distributed tracing, which obviously is a functionality which we have supporting OTEL.
Also just had the more community presentation about absorbability and OTAL with the Open Mainframe project.
And, yeah, I talked about what we are… what we are currently doing, so, cool.
And, Greg, just FYI, I also announced you as the co-lead.
**Greg Shriver** 03:00 Oh, Wolf.
**Ruediger Schulze (IBM)** 03:01 to the Hope Mainframe project. And I said, next time you need to prove… not need, but next time we want to present together, right?
**Greg Shriver** 03:09 Sounds good, yeah.
**Ruediger Schulze (IBM)** 03:11 Perfect. Okay. Good. So, back to business.
**atoulme** 03:15 On the topic of conferences, I'll be at KubeCon next week, so if anyone is going to KubeCon and wants to have a chat about mainframes, we can… we can discuss.
**Ruediger Schulze (IBM)** 03:25 I think this is the… you know, I think this is now vice versa. You have to also keep the mainframe flag open at KubeCon, because I think none of us kind of, like, get the entry ticket to KubeCon yet.
**atoulme** 03:36 Okay.
**Ruediger Schulze (IBM)** 03:37 But it's on the agenda, as Craig was mentioning earlier, once.
**atoulme** 03:43 Okay.
Yeah, well, me and Morgan will be there, and we can definitely bring it up, because this is important, so…
**Ruediger Schulze (IBM)** 03:53 Oh, okay.
**atoulme** 03:53 Okay.
So, mostly, like, there's been a tactical thing that we've been trying to narrow down for a little while, which is about the GitHub action. I know it's a little… unnerving. I'm trying to understand how to best articulate this. I… I know last week we were trying to get to some time with Trask Retiger. I feel like I'm just, at this point, I don't have any value, I'm just a go-between. I… there's some… there's some mechanics to how things are done in terms of a project infrastructure that is just out of my hands, and Trask has been kind of the shepherd of trying to get every administrative aspect done. I've done it before for ARM machines back when it was a bit more experimental.
We had to go through the same GitHub action, GitHub application thing, and you just need to be good about, like, documenting who is doing what, and who's responsible for what, because those things tend to eventually break. It's just a matter of time.
Right.
**Ruediger Schulze (IBM)** 04:52 Right.
**atoulme** 04:52 So…
**Ruediger Schulze (IBM)** 04:53 In terms of, you know, the… adding, in this case, myself as an admin for the Linux S390 runners.
That PR is already processed, so if you go to Community Assets, that's done.
But I think I was yesterday checking, I think I still miss the authority to actually do something on this.
application to… As an installer modifier, do you think?
The, settings for this app, so that then, on the repository.
And I think the underlying question there is if, you know, and I don't know what the community mechanism for this would be, obviously I would have to have certain, authority on this, on this organization.
In order to do so.
**atoulme** 05:48 So you would need to be… You would need to be at least temporarily an administrator of the organization.
GitHub.
**Ruediger Schulze (IBM)** 05:54 Yeah, I suspect so, and every time, then, obviously, when another repository would have to be added.
Because we wouldn't add this to all repositories at the beginning, right?
**atoulme** 06:06 Yep.
**Ruediger Schulze (IBM)** 06:07 And we say it in the description, on request to the community, as a community issue, so whenever another, let's say, Java SDK wants to support it, right, we would have to somehow do this again.
**atoulme** 06:24 Well, I think that's… I mean, we need to also just be very… I, frankly, I just care about the collector myself, so… Right. If we can do OpenTermity Collector first to get started, get it off the ground, that would be a great way.
**Ruediger Schulze (IBM)** 06:37 Right. Yeah, I mean, if it's temporary, I'm completely fine with this. I'm just saying, you know, what we wrote into the documentation for now, and then we can do it again, kind of like temporary if it comes.
**atoulme** 06:56 Okay, so looks like we're, what are we waiting on the most here at this point? Is that… do we need one more check from this application to select the repositories? That requires a little bit of admin work?
**Ruediger Schulze (IBM)** 07:12 So the way that needs to work is, while the application is installed, it needs to be installed by a GitHub ID, which is associated with an email address. Yes. And this email address needs to be the same than the IBM ID.
So, essentially, this email address needs to be associated with an IBM ID. And I got an IBM ID, obviously, but I'm not authorized to make changes to the application, or… Reinstall or whatever, right?
**atoulme** 07:46 So we're stuck on a technicality around GitHub itself.
**Ruediger Schulze (IBM)** 07:51 Yeah.
**atoulme** 07:51 I need to… Bring it up with Trask, I guess.
I don't know how to solve for this. I, myself, I don't think I actually have access to building anything with an IBM ID, so I'm a bit stuck. I don't think Trask would be able to do that either, he's a Microsoft employee, I don't know… What the relationship there is, and if we want… In a sense, like, you're putting your name down as the community asset maintainer, makes it that it has to be you. So, now we need to organize almost like a Zoom session, where he gives you permission for 15 minutes to be the installer.
**Ruediger Schulze (IBM)** 08:33 And then, ideally, there is somebody from our open source office.
That in the same time, she can check everything is fine, because otherwise we have to do this exercise once again.
**atoulme** 08:43 That's random.
**Ruediger Schulze (IBM)** 08:44 So, we should… best would be if she is on the call and can just do this…
**atoulme** 08:49 Okay, so we'd need to do, like, an off-cycle call just for that. Yeah. That person you're thinking about, is she, based out of Europe, or…
**Ruediger Schulze (IBM)** 08:57 No, she is from the US, it's… I need to get her full name, Elizabeth… Elizabeth Joseph is her name.
**atoulme** 09:07 Okay, so Elizabeth Joseph… So, it would make sense for me to try to get Trask into a meeting with you And Elizabeth Joseph… Right. And we do this in some sort of a ceremony of some sort, where we're all together, just doing this.
**Ruediger Schulze (IBM)** 09:25 So, yeah, sounds like that would be the best.
Cool. Best approach to this.
**atoulme** 09:31 And I just have doubts that once it's installed, if we pull the new admin privileges, maybe that might still affect you, but still affect the integration we need to see. But that's a question I'm gonna ask Trask.
He should know.
Okay.
**Ruediger Schulze (IBM)** 09:49 Okay.
**atoulme** 09:50 Cool, cool, thanks. Hey, that's what I have.
**Ruediger Schulze (IBM)** 09:55 Okay, good.
Let me see… I think we have a couple of things to follow up on as we… there has been, you know, if I look at Craig and myself, and also Rachel, I think we have been a little bit in travels around, you know, the last couple of weeks.
I think we have, Topics where we want to follow up on… Obviously, I want to put out a couple of span… PRs for… I spoke just briefly about native distributed tracing from the COS subsystems. Obviously, there are… there's initial support, there are spans that we want to put forward.
And also get feedback from the community, because this might then drive, you know, in later releases, or PDFs, as we call it, changes to these.
Subsystem. I'm just adding this here.
Systems… subs… systems, bands.
to be added as PRs to semantic conventions.
And, then I think we want to continue the discussion around entities for virtualization.
And, we had, I think, Craig, we discussed this earlier, I think one of the points was actually to understand from the… from the project perspective, so OTEL project perspective, while there is, I think there's a proposal out there for virtualization.
And we have been reviewing this. Antoine, this is FYI, we actually have been looking at this in one of the earlier SIG meetings, actually also independently, we have been working on how mainframe entities would fit into this.
And what needs to be done. But then I think, you know, got stuck, and we need to take on this again. But there's also this question about, you know, how to generally the community is progressing with virtualization, because we would have to Build on that.
True.
**atoulme** 12:11 Sure.
**Ruediger Schulze (IBM)** 12:12 Yeah, and I didn't have a chance, and presumably I will not have it now, May. No, I think I want to have a chance next Monday to go to the six semantic meeting, but this would be questions, maybe. I can ask this on the channel.
**atoulme** 12:26 I mean, just to be clear, next Monday, there might not be too many people, active since KubeCon.
**Ruediger Schulze (IBM)** 12:33 Right, yeah, you're right, yeah, so…
**atoulme** 12:38 I mean, for me, it's just out of curiosity, right? I actually don't know enough about the architecture of a mainframe, and I'm thinking that if you were to go to the semantic conventions discussion.
you would probably see a lot of people who don't know about, like, the domain, the entities, like, the big… the big things that you talk about. And I wonder if, I'm sure there's extensive documentation about this, right? An entity-state diagram of some sort, which is, like, you know, one has many, or this type of things would probably go a long way.
**Ruediger Schulze (IBM)** 13:11 Yeah, and actually, we had things like this in the works.
We had, you know, we also had kind of, like, discussions around, do we understand the semantics of what the community is putting in place in the right way? So, those type of questions.
**atoulme** 13:30 Man.
**Ruediger Schulze (IBM)** 13:30 And, and, Then there's also this aspect, just to say it, right? We actually don't want to have the mainframe look too much different to anything else out there.
**atoulme** 13:43 Presley.
**Ruediger Schulze (IBM)** 13:43 virtualization concepts, they… they are kind of, like, you know, the same on each platform, with the exception, we, of course, have also logical partitions, so you get the box, but essentially you partition the box already into Into a set of hosts, or a set of logical partitions.
And then on top of this, you kind of, again, have, you know, virtualization running. This is a typical deployment model, maybe more common if you run Linux on C compared to CUS, but it's a common deployment, right? Okay. And, One of the starting points for all these metrics is to get kind of, like, the entities right, because then we can associate, you know.
system, CPU utilization, and we have different types of processors also. We started already to discuss on this, but then it really comes down to… and we said, actually, we want to put out, maybe the next thing. Actually, Craig, yeah, we said this. Let's put out some simple PRs to test on how the community would like to have Yep.
you know, we have general purpose processors, we have tips, and we have, you know, whatever, IFS, Linux processor, so different types of processors also, and we would have to understand how to… how to put this into the spec.
**atoulme** 15:07 Understood.
**Greg Shriver** 15:08 We… we actually had… we had invested a fair amount of time and as a group, into documents that we had on Google Docs.
**Ruediger Schulze (IBM)** 15:18 Right.
**Greg Shriver** 15:19 And we had them fairly fleshed out, right? And we did have some of that high-level information that would be, I think, helpful as a gentle introduction to folks who aren't familiar with mainframes to get familiar with mainframes. But we kind of pivoted from that.
And, we… and correct me if I'm wrong here, Rudiga, but we pivoted from that and basically took the approach that everything has to be in GitHub in the repository.
**Ruediger Schulze (IBM)** 15:53 Right, right, right.
**Greg Shriver** 15:54 You know? And, you know, if it's not in the repository, it really hasn't happened, right? So, I guess… maybe… and yes, we did talk about, you know, taking, you know, small PRs, but I thought we talked about taking small PRs from a metrics perspective. I don't know that we ever actually had, you know, plans to To try and articulate something at a higher level in the actual repository, and where we would put that.
**Ruediger Schulze (IBM)** 16:25 Yeah, I think we… you're right about this, so we… And this is an interesting question, right? So, do we need to put content in there to… explain specific concepts. So, there's maybe… there's… I think there's two perspectives on this, right? So, I mean.
Generally, there's a lot of content out there, documentation, that describes what a mainframe is.
But I think the key here is, If you have telemetry data that maps on common concept of semantic conventions and then mainframe-specific concepts.
And also makes use of these common metric names, common entity names, for instance.
**atoulme** 17:10 Would there have to be some documentation that says.
**Ruediger Schulze (IBM)** 17:14 If you have telemetry data coming from the mainframe, this is, you know, how the concepts of the mainframe map to it.
So…
**atoulme** 17:23 I think so. I can see that. That would be a good…
**Ruediger Schulze (IBM)** 17:27 Yeah.
**atoulme** 17:27 Personally.
Even if it's just fluff for use, like, it's not really innovating or creating value, it's not defining things, it's just mapping to existing things, it would be great to just have that as an introductory article for people on OpenTeometry.io.
So, I, if you have any of those Google Docs anywhere, feel free to… open an issue, PDF them out, and send, like, put them on an issue there, and we can just have them as a… Hey, here's a… here's the work that we had.
We don't know yet what to do with it, like, we can just leave it in public so that people can maybe take it and put it to the next. I know that the technical, like, there's a lot of folks working on OpenTeamatory I.O. itself who would be delighted to take some content and push it to help. It could even just be a blog post.
For starters.
Because we… I think we also need to see… to, send intent. It's like, we're serious about this, the mainframe C group is working on this type of things, here is some information about an overview of why a mainframe needs to be in semantic conventions, and what it is that we're doing, how it maps a little bit.
And we can be a bit fluffy about the details, but… You know how when you do a research paper, if you've seen those research papers from academics, where they either have a breakthrough, and they talk about the protocol and all the work they've done, but sometimes the research paper is, I just want to declare intent that I think there's a research area in this particular topic.
Here is the bibliography of 20 things that were published in this area. I have no idea what I'm doing, and I'm here to ask for help, and also I'm here to just point out that this is something that I think is interesting and why.
And then they… Publish that, they go to a conference, they talk about it with their colleagues, and they go from there to, here is a protocol, here is how we're going about it, here is where we implement that.
So more like a collegial approach to including the community. And if I have this type of document, I can go on the KubeCon floor and, you know, pretty much push it on anybody and say, you need to know about mainframes, here is why.
**Ruediger Schulze (IBM)** 19:40 Yeah.
**atoulme** 19:42 It's easier for me, it's easier for you, it's…
**Ruediger Schulze (IBM)** 19:46 Actually, I think this… I think this would nicely fit if you combine this with this native distributed tracing, what I just said.
It's kind of like… it's kind of like a starting point, and then there's also… so, just to say this, native… and there have been technologies before, but native distributed tracing is real, it's there, it's in the products.
**atoulme** 20:12 Nice. And we had, you know.
**Ruediger Schulze (IBM)** 20:15 Different vendors, obviously, Craig, you know about this, had also technology before for this, supporting this.
So, there's already something, and I think there's also an ecosystem of vendors which now has open telemetry protocol for metrics, so it's not artificial in the sense, that's what I'm trying to say, right? There's a need, actually, to While the vendor community on the mainframe has taken steps.
now is the next step to… you know, we always talk about portable data, now… and semantic conventions contribute to portable data, obviously, I don't need to… to tell you, but… you know…
**atoulme** 20:54 Yep. Yeah, definitely. Yeah.
I think this is very inspiring if we can, create some level of, I've pushed on that, and… I personally have customers who would want to see more of that type of support, and I think any statement, even if it's just a blog post or just some documentation, would help, increase the attention. It's kind of a feedback loop, right?
**Ruediger Schulze (IBM)** 21:19 Yeah.
**atoulme** 21:20 you say something nice about mainframes, people are like, oh, OpenTempTree Mainframes actually has something to say about it, right? And then you go. We have a SIG meeting. Okay, cool. And now we're pushing this, okay. And… We don't have to be… I know there's this… the engineering mindset is, like, you need to be good about this. We're specifying something. We're doing a good job. We're putting everything, this is complete. We actually have a versioning on this. We're going to measure that.
But then there's this weird girl marketing of OSS approach to things, which is, put a little bit, put 10 lines, put 20 lines, put 50 lines, get this contribution from the left that you're not expecting. I know, I'm… You know this, but… okay, so… Yeah, if there's anything I can help with on pushing some of that, I'd love to review those Google Docs for myself, and frankly, get more educated on the problem space.
**Ruediger Schulze (IBM)** 22:13 And, if you can send that to me, or in the notes, I would be so thankful.
**atoulme** 22:18 And I can get myself more situated on how to help you most.
**Ruediger Schulze (IBM)** 22:23 Huh.
**atoulme** 22:24 I've been very hung up on the GitHub CI issue, but maybe I don't need to as much. I just want to make sure we move on that so that we can declare platform support for interesting architectures.
And, yeah. Right.
Give you a… Oh, sorry.
**Ruediger Schulze (IBM)** 22:43 Go ahead, go ahead.
**atoulme** 22:44 To give you too much context here, there are two forces at play right now. One is that the open chemistry project as a whole wants to graduate.
**Ruediger Schulze (IBM)** 22:52 And to graduate, it needs to show some maturity, which…
**atoulme** 22:55 it requires us to kind of be focused on what we were doing. So, for example, the GC is working on a blog post right now, around having some refined requirements for adding new initiatives, right? So, we want to make sure we don't disperse ourselves into 20 different things, so there's that.
There's just a lot of… whinging things around, like, stability and stability. I don't think… in a sense, like, the mainframe discussion is almost, like, we just need to keep going. But there are things more around, like, Java JavaScript frameworks, or the collectors, which have been giving grief to people.
So we need to be just acknowledging that, in general, for the OpenTermetry project to succeed, it needs to be seen as production-ready by people. Just put it out there, just for your context, for yourself.
**Ruediger Schulze (IBM)** 23:47 Yeah, true.
**atoulme** 23:47 the collector itself. The collector has limited bandwidth and capacity, and there's multiple ways to look at this type of problems. You can think of this as a tragedy of the commons, you can think of it as you only have so much capacity or so many hours on your day.
Or you can think of, how can I multiply and leverage what we have so we can get 10, 20, 30x what we offer, right? So that's… could be the AI approach. It's like, we find a way to somehow have someone do 10x what they were doing before.
Or we get smart about being very intent and pushing clear guidelines so we reduce waste in communications, and we make it easier for people.
All of this is at play, right? It's just going to require the collector to also come together and stabilize and go for $1.
what I would not want is that, as part of that effort, we start to say no to arbitrary things, like, oh, mainframe support, We're trying to go 1.0, so… no.
**Ruediger Schulze (IBM)** 24:42 Yeah, fair.
**atoulme** 24:43 make sure we keep that door open. I'm going to plead with the collector maintainers that we keep ourselves open to innovation, because otherwise we'll die.
It's very simple to me. Like, this is an open source project, it cannot be mature at the expense of innovating and enabling new domains.
But I need to make that argument with some amount of, like, gusto and pushing some… some ideas. I'm working on that. And I understand that point, too. It's like, they're, you know, those people have been working on stabilization for over a year or two years now. It's been very slow coming, and… Surfing, adding an additional platform to support is not somewhere on their roadmap at this point, right? They're not thinking about this day in, day out.
I just need them to be nimble about it, and just set ourselves up for success by not over-promising anything as well, right? So… Tier 3, just making sure it compiles, somewhat runs, and does not support everything, and we get bug reports specifically for mainframe and IX, but they don't reflect on the maturity of the overall software.
That's fine.
**Ruediger Schulze (IBM)** 25:51 Right. So, I mean, as you know, the situation with a collector is like this. Tier 3, that's already happening for Linux on C. AIX, there's this issue, right? Linux on power is obviously also Tier 3.
**atoulme** 26:08 I mean, once we get the…
**Ruediger Schulze (IBM)** 26:13 once we get the JITAB Action Runner for Linux on C working, we can actually, if we run the unit test, we are in a position, if this works well, to elevate to Tier 2, right? That would be the aim of this.
AIX is a different story. Obviously, this is a requirement also from a client base, as I understand it, but it's probably also, My company obviously needs to do a couple of things in this space before things will move there.
Don't want to say more about that.
Right.
**atoulme** 26:50 Yeah, that makes sense. Yeah, works for me.
**Ruediger Schulze (IBM)** 26:53 Okay, good. No, this is good, good discussion, Antoine. Craig, let's pull out the documents and… and make sure we have them here in the, you know, we add them to the meeting notes, and… and Antoine, I sent you the link, via Slack. Let's open my Slack later on.
And, I can do that.
**Greg Shriver** 27:14 that.
I can go through and take a look at, you know, and find… because I think some of them are already referenced in here, maybe just surface them to the top and say, here's a list of of, documents, like Google documents that we have now. Another thing that we might be able to do… I mean, I know we've probably already have blog posts you know, in conspicuous places that are probably already published. Like, you probably have them from IBM, and I know we have some from, you know, from Broadcom as well, and I'm sure others do, also.
Would there be any value in maybe having, you know, a list of links that contain these types of general fluff type of resources?
Or is that just low-value, busy work that we shouldn't pursue?
**Ruediger Schulze (IBM)** 28:13 So, I mean, generally, I think we had a couple of common… blog posts on… collector support Tier 3. We had open mainframe… Pro. Okay.
Project, some blog posts in the past.
block, hotel I.O. block, in the meantime.
And then there's, yeah, there's surely also content which is… like I said, native distributed tracing. Obviously, you find blocks there. Okay, this is more Windows-specific, it's a question if you want to put this there, but… It's… it's… You know, it's reality, it's out there, right?
And I record it.
There, there isn't… so… Maybe we need to find a way to express this. There is an OTA support happening across the ISV ecosystem.
for the mainframe, which I think is a true statement in the meantime.
**Greg Shriver** 29:14 I agree.
**Ruediger Schulze (IBM)** 29:15 And, and, Maybe there's a way of how we can express this, and this is also the motivation to continue this to, you know, everything that we said before, to make this more mature.
**Greg Shriver** 29:29 Sure.
**Ruediger Schulze (IBM)** 29:34 Yeah, but maybe, Craig, if you could start gathering these things, and I can look for a generic type of Block and communication that has been there before, then maybe we start from there.
**Greg Shriver** 29:46 I'll take an action item to find those… to unearth those documents and get them, you know, consolidated in a curated place.
Here in the notes, and then we can, you know, socialize it any other way.
**Ruediger Schulze (IBM)** 30:00 Right.
Richard, you have to be quiet, but we met 2 or 3 weeks ago, so Richard and I also met. So, Greg and Antoine, you're still on my list to meet.
**Richard Nikula** 30:11 Yep. No, nothing to add today, so I was just hanging out.
**Ruediger Schulze (IBM)** 30:15 Okay, good.
**Richard Nikula** 30:17 help as I can. We…
**Ruediger Schulze (IBM)** 30:23 Okay.
And I think we have an action list. Antoine, let me add the name… I will add the name of the… maybe you wrote this down, but let me see if we… yeah, a little bit, Joseph, you wrote it down, right?
**atoulme** 30:38 I did, and I will, I will work on that. Create. The thing I might do here is, it's… I don't know if I want to directly go to Trask, but I might. Worst case, I'll try to again the slot tomorrow of 11 a.m. PST, which is pretty late for you, with.
**Ruediger Schulze (IBM)** 30:58 That's good.
**atoulme** 30:58 project in Frasig, but I can at least bring it up with them. I want to understand exactly the technicality behind this, so I'll try to be at that meeting that time around, and make sure I talk about it with him and the other maintainers, because Trask is not the only one who can do this.
Austin Barker and others.
So they might be also more amenable, and earlier… In the time zone, so Austin could actually probably help, but yeah, so…
**Ruediger Schulze (IBM)** 31:22 The problem is just, I'm on the plane tomorrow again, it's like last week.
**atoulme** 31:26 Yeah, no worries.
No worries. So, I understand that you won't be able to join tomorrow. I'm just going to make sure we…
**Ruediger Schulze (IBM)** 31:32 Yeah.
**atoulme** 31:33 Line up all those things, and it don't have to happen right away.
**Ruediger Schulze (IBM)** 31:36 with ScoopCon next week, it might be difficult as well, but we'll figure it out.
Okay, thank you.
**atoulme** 31:42 Of course, thank you so much for your consistency.
**Ruediger Schulze (IBM)** 31:44 Yeah.
**atoulme** 31:45 Trying to get this done. That's, been, long, long work, but we'll get there.
**Ruediger Schulze (IBM)** 31:50 Yep. Okay, good. Thank you, everybody.
**Greg Shriver** 31:53 buddy.
**Ruediger Schulze (IBM)** 31:54 But…
**Greg Shriver** 31:55 Bye.
