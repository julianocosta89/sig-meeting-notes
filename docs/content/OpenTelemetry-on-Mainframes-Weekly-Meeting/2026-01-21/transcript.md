SIG: OpenTelemetry on Mainframes Weekly Meeting
Date: 2026-01-21
Duration: 61 minutes
Zoom Recording URL: https://zoom.us/rec/share/wzG11Aybm9grGiex_fqCY_Eq5jmBDEVGkQhSDbr22En1GdUrfkWOGpEMXO3KQbZh.KgGO0RK9j7qgrc9N
============================================================

## Zoom Recording Transcript

Greg Shriver 00:02:37 Hello, folks.
Jim Porell 00:02:42 Hey, I just saw that, Rudiger can't make it.
Greg Shriver 00:02:45 Yeah, yeah, I saw that too.
Yeah, and I don't… I don't have anything new for today.
I did have a question.
Of the SIG… SIG mainframe maintainers.
Not sure exactly if that's, like, list. I was gonna… I was hoping, if Morgan showed up, maybe I was gonna ask him.
Jim Porell 00:03:16 Maybe Antoine, one of the two.
Greg Shriver 00:03:19 Yeah, yeah, yeah.
Jim Porell 00:03:25 The other thing, I was talking to,
I saw Rudiger last week, and…
Greg Shriver 00:03:32 Oh, okay.
Jim Porell 00:03:33 Something… we were at a joint meeting together, and
I don't know if it's adding a spark, but…
we probably gotta work a little faster. I don't know what to do in terms of… well, there's still a lot to do in terms of naming. I mean, we're really at the base operating system level, but…
And I don't know what the right way to do it, Greg, is, but… We gotta figure…
I gotta figure some of that out.
Greg Shriver 00:04:06 Well, yeah, I, I agree, I agree, but…
So, what… what would you suggest? And, I mean, in terms of… well… I guess… I mean, moving forward.
Jim Porell 00:04:20 We're in some more straw man, you know, maybe, maybe we put together… some…
You know, try and get some more straw men done on…
Like, the process models and stuff.
Greg Shriver 00:04:33 Yeah.
Jim Porell 00:04:34 And going beyond our normal group, maybe adding some other people in.
Greg Shriver 00:04:40 Sure.
Well, I know, I mean, we had… we had kind of similar conversations in the past, and I think the net-net was that
that we were, we… instead of trying to make these giant PRs, maybe have these small PRs.
You know, to eat the elephant… eat the elephant one bite at a time.
And I think we kinda tried that, I mean,
you know, we put a… I put the PR out with the dock stuff, and it's just kind of sitting there.
And that's why I had the question about the SIG maintainers, because that, you know, it seems like that is the… sort of the next step to even get that PR merged.
But I… I agree with you, Jim. You know, even… even if that PR is merged, that doesn't really get… that doesn't really move the ball substantively, in terms of… in terms of the semantic conventions that I think Rudiger
articulated on the last meeting that he was on, that… that he wanted… that he felt we need to focus on in, I guess, calendar 26?
Jim Porell 00:05:53 Good.
Greg Shriver 00:05:54 So…
I know.
Angelika Heinrich 00:06:01 Yeah, I mean…
Greg Shriver 00:06:03 Hi, Angie.
Angelika Heinrich 00:06:04 Yeah, I was just gonna say at the…
I wouldn't stop with trying to put together smaller PRs, because I can't see a big one.
Going our way.
But, you know, it's just making sure we get visibility and maybe even,
you know, attending some of these SIG weekly meetings to help push the approvals faster, so it's not just on Rudiger.
Greg Shriver 00:06:35 Yeah.
Angelika Heinrich 00:06:36 you know, and like Greg says, just understanding the approval process more to see how we can push
For approvals on our pull requests.
So for me, for example, like, we were looking at the database stuff.
And the messaging, so we're just gonna go ahead and do the pull request for what we think is right.
Right, and then see what gets approved.
If there are other resources that you're concerned, like processed, you said, right?
Jim Porell 00:07:08 Well, I think… When you look at the process model, there's…
differences between KICS, IMS, DB2 stored procedures, batch, Unix system services applications, so…
Do we want to get, you know, it's almost like an array.
Greg Shriver 00:07:27 Where they're remarkably similar.
Jim Porell 00:07:30 But… probably different enough that they warrant their own naming conventions, like kicks.something, versus
processed, you know, I don't know.
I'm making it up, but…
They're similar, but different enough that they might warrant
You know, some unique naming across them.
And I know in the document, you know, the Google Doc we had, there was… there was kind of a matrix that we had drawn out at some point to show some of that.
But we want to call out for semantic conventions.
Actually named them differently.
I mean, I'm on the…
maybe take a stab at something, but I can't do… I'm gonna be out next week, but I could probably do it the week after.
Angelika Heinrich 00:08:30 Yeah.
I think that'll probably be the easiest way, right?
If that's something you want to address, then… .
Jim Porell 00:08:40 I'm just trying to… these are all things to move forward.
Another area is… no… The convention has things like clustering.
But Z clustering, because a sysplex, you know, is a shared model versus a message-passing model, so are there unique things that we ought to be naming for
within a sysplex.
Angelika Heinrich 00:09:06 Maybe, yeah.
I know we had some suspec stuff, right, but not a lot.
Jim Porell 00:09:13 Yeah, it's on the following, but that, you know, that's… we gotta think about all these things. I think process model is probably before sysplex, but…
At least that's my personal view, but…
Angelika Heinrich 00:09:27 Alright.
Well, yeah, I mean, it's…
I know with the, you know, what I could find on the entities model.
Kind of, sort of ties into that.
I don't think entities is…
Stable yet, but it does seem to already be pulled in.
To the current,
GA semantic conventions, at least I can see they're calling out that there are roles missing in resource attributes, which can only be determined by entity. So, basically, it's…
I think you're right, but I think the only way we can go forward is if…
At least in my mind, is if we…
Take a stab at putting together a proposal, and…
You know, I'll review it here and see if we can get approval.
Over the board.
Jim Porell 00:10:27 Yeah, I've found where I'm thinking, too, so…
Greg Shriver 00:10:37 So…
Jim Porell 00:10:38 Yeah.
Greg Shriver 00:10:39 Yeah, so, Angie, you had… did you have a PR that you were planning on
On opening up, or did you already open it? I'm sorry.
Angelika Heinrich 00:10:49 I didn't get it opened yet, yeah. Okay.
Greg Shriver 00:10:52 Okay, and no, no, no, I wasn't push myself.
Angelika Heinrich 00:10:54 Yeah, no, so I did… I did start reviewing our doc, and then my main goal was just to figure out if there's anything mainframe-specific that we want to call out.
for mainframe… database systems.
Besides what's already defined. And then on top of that, really good…
called out the entities model, so I needed to go back and then review, you know, go back and see what
The database model may be putting out for Entities for databases.
And then if there's anything, like,
Jim was saying, now you're right, if there is anything specific for mainframe, right, that we would want to have identified.
Right, that could DB2 shared member groups, or… I don't know.
Jim Porell 00:11:44 Yeah, I'm making this up, but, you know, you have SQL, NoSQL, you know, distinguish between a Mongo versus a DB2, as an example.
And then certainly on Z, we have…
you know, from IBM, you have IBM Full Function, IBM… I mean, IMS Full Function, IMS FastPath.
Db2, and then you can get into A database, IDMS, you know, whatever else Broadcom has.
Are those distinctions important?
Yeah.
Angelika Heinrich 00:12:22 And DB2 semantic conventions, yes.
Yeah. Well, sorry, not DB2, but database. So yes, you would have to say what the database type is…
Jim Porell 00:12:33 Yeah, and do they have unique characteristics?
That's why I was trying to go into SQL versus NoSQL, hierarchical, that kind of stuff.
Angelika Heinrich 00:12:42 Yeah.
Yeah, so I'll take a note of what you're saying and see if I can…
represent, or if I can find anything on that specifically.
Greg Shriver 00:13:04 It's cool. And, Jim, you said that you were gonna…
What was… what were you saying you were gonna… maybe not this week, but in the following week, you said you were
process models.
Jim Porell 00:13:17 Yeah, like, if you look at the different operational environments, the process model.
Do we name them separately, or are they types? I mean, that's…
Kind of similar discussion of database, but…
At least I can… I'll try and build a matrix.
To show it, and then… You know, maybe it's typing within…
Existing conventions, or maybe we have to add some new naming.
Because of the unique differences.
I gotta be honest, I'm not smart enough to tell you that within this space, but…
At least I'll bring it up.
Greg Shriver 00:14:03 No, I think we've had… I mean, that's a good point. I think we've had,
Discussions in the past about, you know, specifically on the topic of do we try and shoehorn, you know, mainframe stuff into existing semantic conventions?
Or do we try and make it separate and appropriately namespaced so that it's very clear that it's…
you know, that this is, you know, not necessarily a mainframe thing, but this is something that's, say, IDMS-specific, or IMS FastPass-specific, you know? And I think…
You know, it's… it's always… it seems…
and I think we've gone back and forth on this topic. I think it seems to be tempting to shoehorn mainframe into existing semantic conventions, because…
Because it would be probably more quickly usable by people.
by the SRE community, but… but that temptation, we probably shouldn't give in to it.
You know, on the other hand, we have the semantic convention folks who are saying that if you crush us with a whole bunch of new semantic conventions, it's gonna bog us down, and we really don't want that.
So…
Richard Nikula 00:15:26 But it has to be both, right? I mean, I think.
Jim Porell 00:15:29 Yeah.
Richard Nikula 00:15:29 the reality of the world is some things have to fit because they are things, right? I mean, it's… there's no reason to always invent a new term for something just because
it's different, right? But some things just don't line up. I mean, there are things that…
You know, are different, and…
So they have to… they have to be different. So… so I think, you know, we… we've sort of started on that tack, that there are some things that the systems are systems, and they, you know, they're…
And transaction processors are transaction processors, but… Does it kicks…
Have to match up with… with a…
With a WebLogic server? No. Everything can't be the same.
Jim Porell 00:16:19 Right, Kix and Tomcat, probably similar. MQ, MQ, you know, MQ, Tibco, maybe similar, but if there's unique…
So you want to embrace some, but maybe extend.
Angelika Heinrich 00:16:33 Yeah.
I remember.
Yeah, I agree. I was just gonna say, I do remember from the process conversation, we initially thought we could use that for batch jobs, but then we realized that that
would be… superposing… so we would confuse ourselves, because if it was a Unix process.
Then, you know, we would use the semantic conventions probably correctly, but as a job, we probably want to create our own
Semantic conventions for jobs, because… In theory, they're not a process.
It just would have been easier to use process.
Greg Shriver 00:17:17 Yeah, I agree.
I mean, I agree with all of these points that are raised. I think at the end of the day, it's a judgment call, and it's going to be a judgment call by the people in this group, and hopefully the people that are reviewing
you know, reviewing and hopefully providing comment to the PRs that this group, you know, will hopefully soon, you know, be generating.
Jim Porell 00:17:45 The other thing, too, is I kind of had an epiphany last week.
Rudiger shared… how…
OpenTelemetry is being done by the subsystems and, you know, where they're taking the W3C input into transaction managers and stuff like that, and where they plan to write OpenTelemetry.
After I stopped laughing.
Greg Shriver 00:18:13 And the point is…
Jim Porell 00:18:15 You're talking about… A lot of transactions that are very few instructions.
If we really instrument everything.
you might as well triple, quadruple the number of MIPS you have on your mainframe.
And… Because of the path length associated with
Actually instrumenting every ques… every transaction.
So that led me to say, what do we want to prioritize on?
You know, it's probably… I think what a customer's gonna wanna do is…
Major transaction systems, major databases, and really don't need to go into a Not yet.
Those… but those are their first priorities.
like, kicks DB2… maybe IMSDB2.
I don't know, but I just… I started thinking, you know, Customers really…
You know, we have bleeding-edge customers as…
Morgan would say, you know, they've been working with one particular customer.
The focus ought to be on
What does that customer really want? What are the key items they need?
I don't know if that makes sense, but… versus trying to just do an inventory of the whole damn system.
Greg Shriver 00:19:48 It does. It sounds like you're proposing more of a top-down approach.
As opposed to, you know, trying to instrument all of the minutiae, or the leaves at the bottom of the trees, or the leaves at the end of the branches, you know, kind of start with the trunk.
I know that's… that's more bottom-up. I picked a bad analogy, but…
Jim Porell 00:20:11 But I like that. I mean, it works.
But if I think about the picture that Rudiger showed me,
you know, they… they've chosen certain subsystems and stuff that IBM's exploiting, gonna, you know, be willing to write this stuff to, but I still think the customers are gonna decide what and where they want to turn it on.
And we probably ought to, you know, if we thought about it from a customer perspective.
We'd probably get a lot smaller scope to focus on, and maybe make some faster progress.
Greg Shriver 00:20:50 Yeah, that's fair.
I mean, are… Well, I guess, yeah, are… are they…
Considering making instrumentation of those individual things optional, or…
Jim Porell 00:21:07 Oh, it has to be. It's like tracing. You turn on certain traces, Or you don't, you know?
Greg Shriver 00:21:14 Okay.
Jim Porell 00:21:14 like, kicks traces are invasive.
So, people only turn them on when they're in a diagnostic position.
it's too expensive to run otherwise.
Greg Shriver 00:21:28 I see.
Jim Porell 00:21:30 Well, I don't know if that makes sense to you, but…
Greg Shriver 00:21:32 Well, it does. It does.
Angelika Heinrich 00:21:36 Yeah, I mean, I agree.
The other thing, I think, is there are other data pieces that customers do have active, even at a transaction level.
You know, like this, and if… Right.
Customers often write that.
Even if it's just a, you know, customized version of those SMF records, but they do write those out, typically.
So in my mind, I think, well, there clearly weren't transaction-level data, just…
you know, not the whole world. They don't need to know every single little thing about kicks, but they do want to have some vital
Like, performance indicators, right?
So, yeah. But I understand, I think, for mainframe… communities, it will be a… A decision of what
You know, visibility versus cost.
Because we've… we're coming at this backwards, where I think distributed systems have had this for…
Kind of out of the box.
So we're not used to that overhead, right? It's not something we cater for.
Jim Porell 00:23:04 And the other thing, too, is on the other systems.
It's also a software developer's kit.
For a lot of the applications, and so they're self-instrumenting, if you'd like.
In our environment, you know.
what IBM's doing, and it's like security. Security and resilience, it's the application's responsibility on non-Z platforms to add security, add resilience, cluster, that kind of stuff. On the mainframe, it's the system's responsibility to do that.
So… some of this is, you know, IBM's trying to add it into the subsystem so it's easy.
But I think some of the bleeding-edge customers will use a developer's toolkit just to expeditiously add their critical applications.
Angelika Heinrich 00:23:54 Yeah.
Richard Nikula 00:23:54 I mean, I haven't actually seen that on the distributed side. I mean, there is some uptake.
But over there, it's still a lot of the same thing. It's the… you know, I basically…
say it's the plumbing, right? The plumbing is instrumenting, right? So, you know, the… the things like MQ, the things like the web, you know, the app servers, you know, they're building plumbing
Tracing, not really application tracing, but plumbing tracing, because the application still
have a really hard time justifying, oh, I need to put extra code in to instrument myself, right? I mean, it is what OpenTelemetry was targeted at, but…
upkeep has been, at least where I've been.
I've not seen a lot of the application people saying, oh, wow, I can, you know, I'll throw these tags in, and then magically everything will…
be traceable in everything I do.
But I'm sure there's some.
So that's why… so I said, it's one of the challenges of a lot of this, is it's… what we're tracking is plumbing information, and… and it's better than we had. I mean, that's, you know, that's the good news, right? It's…
Angelika Heinrich 00:25:07 Yeah.
Yeah, from the custom, like, custom attributes, I have seen, like, customers I work with use OTL
Pervasively, they do have requests to, you know, support
Custom tags that they've included in their baggage.
And they want that available.
So I agree with Jim that I think there is, you know, obviously the… on one side, I think auto-instrumentation is probably… you're right, Richard, the way most customers go, but I think the more mature customers get, they realize that there is value in having
Data that reflects your application and your business better than just the standard stuff?
And so I've seen, you know, we've had customers request that.
that support.
Richard Nikula 00:26:34 How did that really shut us up? I'm sorry.
Angelika Heinrich 00:26:37 No, I'm sorry, I didn't mean to.
Greg Shriver 00:26:41 Yeah, that's pretty good.
Angelika Heinrich 00:26:45 Yeah, so, you know, in terms of just customer, like, priorities, right, that's probably a good point. I can go back
at least with the customers I've worked with, and just try and
Summarize what… what they're looking for.
I know that databases are something, you know.
a couple of my customers are looking for, that's why I really want to get those
semantic conventions settled for mainframe.
And then the other stuff that I think I brought up before with MQ as well, that's definitely something…
That's come up a few times already, so it's probably worth just checking that we have that.
I'll see what else there is, but those are two I know for sure.
We'll be in that list.
And I'll… I'll share that just in the stack channel, I guess we don't have to wait till the next meeting.
Probably might be a smaller pool than, than what, ridicah may have, but…
Lisa will be some input.
Greg Shriver 00:28:12 Yeah, that'd be great.
Jim Porell 00:28:19 Yeah, I think that's… again, that's the conversation. I think Rudiger's gonna be happy,
He was just looking for, you know, how do we…
help expedite the whole process, and that was a conversation, that's why I brought it up.
like, I'm gonna be a traveler next week, but maybe if he joins, it's a good conversation with him.
Greg Shriver 00:28:56 Yeah, and… you know, for the PRs that we have out there. I mean, do we still have…
So I know we have…
Angelika Heinrich 00:29:07 Now we have the TPS one, huh?
Greg Shriver 00:29:09 There's the TPS one that's still out there.
And the dock one, I think, that I… that I had, the 8624.
I mean, maybe it would be helpful if,
if we could, for the PRs that are out there, if we could each take a look at the PRs and…
You know, even if it's just a comment that you add, you know, just so there's some activity there, that… so… because I keep seeing these bots that say this PR is stale, and it just closes it.
And then you have to reopen it. Yeah, it's… it's… it's… I mean, I'm not familiar with the… with the mechanisms, but…
you know, apparently, if you… I guess it's necessary if you open a PR and it just sits there and it gets stale, then some bot comes and closes it for you and says it hasn't had any activity. So I think, you know, maybe from that perspective, if we could just try and make sure
that for the people in this group, if we've got, you know, PRs that are open, that we're at least regularly taking a look at them.
And… and providing comment if… if we can. I recognize every… everyone is busy and has a day job.
Angelika Heinrich 00:30:29 I'll try, yeah, I'll take a look.
Greg Shriver 00:30:33 Yeah, and then, of course, we want to make ourselves more work, so we want to get… we want to get more PRs, right? So, we want more small PRs, right? So, yeah, if we can get the, you know, the… the… at least…
something small with the stuff that's really pressing, you know, for the database, and pressing for MQ, whether it's part of the messaging SIG or not.
Maybe we just push forward with, you know.
You know, push forward with the things that we've heard from our customers that they need.
And… and… You know.
I don't know. I'm thinking that maybe that's a way that, you know, that we can at least keep the momentum going, and we can keep the ball rolling.
Jim Porell 00:31:31 Nope.
Greg Shriver 00:31:34 So…
Does, does anybody have anything else that they want to bring up for this week?
Richard Salac 00:31:49 I do, if I may. My name is Richard Salak, I'm from the…
Zoe organization, and also from the… from the Broadcom. So, if I can have a couple of her minutes…
Greg Shriver 00:32:00 Absolutely, welcome.
Richard Salac 00:32:02 Oh, you probably met, my colleague Andre, Andre Mello on some of the previous meetings, and,
I am here with Pabel, who is also my colleague, and we in Zoe, and specifically, I'm from the API Mitigation Layer team.
We started implementing, OpenTelemetry to support observability. We are the first one in the ZOE project.
And we are in the stage that, we…
use the OpenTelemetry SpringBook starter, so we got some basic support, and now we are discovering, you know, the whole universe that you just discussed about the semantics and attributes and, let's say, misalignments between the distributed world and in the mainframe.
Mainframe semantics.
And, basically, we got a couple of the questions, or maybe… maybe just seeking out guidance how to… how to approach some of these.
some of these things, because API Mediation Layer is a Java application, so it's something that's not native ZetOS, and that it's supposed to occasionally run off the platform, for example, in the
in the Kubernetes, so we are kind of caught in between all those universes, and we need to somehow, somehow, let's say, resolve the differences.
Angelika Heinrich 00:33:38 Meg. So…
Richard Salac 00:33:40 Yeah, so, basically my question, is basically how to… how we can approach your group, and how we can raise our questions and findings and maybe seek out some of your experience and guidance.
Greg Shriver 00:34:06 Well, yeah, I mean, that's great, I mean, thank you. I think maybe…
So, there's a couple different ways to engage, right? Of course, you can do it like what you're doing now on the meeting. There's also, you know, the Slack channel. Are you… hopefully you're… you and Andres are also on the Slack channel.
And I think, you know, between meetings, it's certainly fine to, like, you know, to ask those questions. And… but you mentioned that you, you know, during… actually, you know, when you're actually doing this implementation, that you're noticing misalignment, you know, between
Between all of these different universes. If there's a… if there were… what I would suggest is if you could…
You know, when you notice those misalignments, if you could identify them and maybe tag them, or maybe write up a sentence of what it is.
And then, you know, certainly, you know, bring it to… you know, bring it to the group, either via the Slack channel or on a meeting like this. I'm not sure…
I don't know if it elevates to, like, opening an issue or not. I don't really know how… how we use issues, in the OpenTelemetry context. I'm not… I'm not aware of that.
But if we could at least get it to a point where we could… where everyone could understand, like, what the misalignment is.
and then kind of either, you know, have it in a PR, or… I don't know about a PR, but maybe if, you know, specify… maybe it could be packaged up in a PR such that it could get scrutiny, you know, across this group and across the wider OpenTelemetry community.
I mean, that… those are my thoughts. Does anybody else have any… have any, thoughts on… on how to proceed?
Jim Porell 00:36:08 I think all of the above you kind of gave both answers, so… Sounds about right.
Greg Shriver 00:36:16 You know, thanks, Jim, and Richard, I appreciate that. I mean, it would be,
Thank you for bringing it up. I'd be curious and interested to see
the misalignments that you notice, you know? Are they the same misalignments that we've perhaps discussed in the past?
I don't know. I don't know.
Richard Salac 00:36:44 Thank you, Greg. I am not sure how much time do you have. I prepared a short
presentation, just of 5 slides illustrating… illustrating the issues. I can write it now, or if we are running out of time, I can share them in the Slack. It's… it's up to you.
Greg Shriver 00:37:02 I would say both. I mean, hopefully everybody has time. I mean, this meeting, I think, runs until… for another 25 minutes, so if you have 5 slides…
Richard Salac 00:37:12 I would say… I would say roll it, and I would also…
Greg Shriver 00:37:16 If it's something that you can share broadly, I mean, obviously it is, because you're sharing it here, but you may want to also share it on the Slack channel.
Richard Salac 00:37:26 Okay, no problem, I will definitely do. So, if nobody's against it, I'm going to take the screen sharing.
Jim Porell 00:37:35 report.
Richard Salac 00:37:46 So, just please tell me, do you see the… do you see the presentation?
Jim Porell 00:37:50 Yes.
Greg Shriver 00:37:51 Yes.
Richard Salac 00:37:51 Okay, great.
I don't know how much are you familiar with the Open Mainframe project and with Zoe?
Are you, are you not?
Jim Porell 00:38:02 I am, and I'm pretty familiar with the API mediation layer as well.
Richard Salac 00:38:06 Okay, great. So I'm… going to…
Skip the introduction. If you are interested in more details, or want to get familiar, I encourage you to visit zoe.org for
More information, we are specifically, raising these questions, not… I wouldn't call them issues yet, they are generally questions.
When implementing the OpenTelemetry into the API mediation layer, which is a Java-based application running primarily on ZOS, but not exclusively.
And it serves as a gateway to access ZOS applications via REST API.
And one of the main benefits of having the API meditation layer is that it provides a single sign-on experience through the mainframe and distributed world.
We are using the OpenTelemetry Spring Boot Starter, so the one really provided by the OpenTelemetry itself, not by the Spring.
And we were very surprised, positively, that there is already some support for the ZetOS, so we are exploring
What is, what is available there?
These are generally the questions that we have. Basically, we found some differences between what the OpenTelemetry SDK for Java provides and what the semantics for mainframe.
defined, so we found some, some differences. We found that some required fields or recommended fields are not populated, but there are some, some opt-in fields.
provided in…
stat, some fields that are populated by the SDK provides the values in different format than the semantics.
describe.
And then, you know, we have the question whether a Java application, even though it is running on the ZOS, should follow, or how precisely should it follow the ZOS software semantics?
Mainly because of something that was already mentioned in the discussion before, that, on traditionally Unix or distributed system, we have a process, basically, and that's it. But on mainframe, we have jobs, we have starter tasks, and these all can play
Together, we have processes and process IDs, and we have other spaces on ZOS.
So should we prefer one over another, or provide, provide all of them?
These are… these are the questions, and…
Of course, if we find such differences between the semadext and the SDK,
Should we correct the SDK or fix the value so we follow the ZOS semantics? And the question is…
How do you… how this we will be…
understood by the users, because if they follow the SDK, and everybody will follow the SDK, then the…
data provided by the OpenTelemetry framework will be consistent, but not exactly, necessarily by the semantics.
And I… and I have…
three specific examples, just as an illustration. Maybe we will find more in the future, so this is just really for the beginning to introduce the questions we have and to kick off.
this discussion. The ZOS OpenTelemetry semantics, this is a screenshot from, from the OpenTelemetry documentation.
have… has 3…
it is small, but in this case, we have the OS type, OS version, and OS description attribute.
And, the Java SDK, even on the ZOS, can correctly identify the OS type.
Which is nice.
On the other hand, the recommended OS. version is not identified at all, but it provides the OS description, but in different format than it is listed in the, in the documentation.
These are, on one hand, minor discrepancies, But, you know…
I wonder what happens, what, you know, these minor discrepancies will do within the observability stack, when every SDK and every product will provide slightly different values. It can become a mess for the clients and for the users to actually use the telemetry data and analyze the telemetry data.
Jim Porell 00:43:03 This is… this is actually really helpful.
Richard Salac 00:43:06 So…
Jim Porell 00:43:08 what other examples? Because these are areas that we are focused on, you know, there has been discussion about this, so…
Trying to get standards, but…
It's also important, like you say, display IPL info, that the commands return the right stuff, too, so…
something we gotta make sure that Rudeter sees, you know, to bring back to IBM if the commands aren't given the right information.
Richard Salac 00:43:36 Thank you, Jim.
I am going to continue, another question is about the process.
Because these semi-.
Jim Porell 00:43:47 This is kind of what I was talking about here.
Richard Salac 00:43:51 Yeah, exactly, exactly. There is more to it. Well, on one hand.
Jim Porell 00:43:56 True.
Richard Salac 00:43:58 the Java application on ZOS, it's running under the USS, so it has a Unix PID, but it really doesn't follow the semantics that says that it should be in address space.
I believe, and that's my personal, personal opinion, that, that we should provide both, because they are both useful. We, can very well provide the started task name as part of the process, process namespace, because this is also, also, also valuable.
Richard Nikula 00:44:31 almost… that almost seems to be outside… in my view, that should be outside of a scope of a Java process running on ZOS, right? I mean, its job is to report
It… information. There is a… Process running that has… That's overseeing it, but…
it starts to get really messy if… if every sub-process tries to figure out what is its role in the big world, right? So, I don't know, I'd say…
Jim Porell 00:45:02 Well, I'll… I'll… Disagree a little bit.
Richard Nikula 00:45:06 Okay, good.
Jim Porell 00:45:06 Again, this is one of those weirdo ones where…
I was the lead architect for Unix System Services when I was at IBM, and my analogy was.
you know, there were 3 communities we had to focus on. One was, end users, and so if it's a web service on a mainframe, web service on Unix, you can't tell the difference. Okay, we accomplished that. Application developer?
Formats and protocols and APIs are common and consistent, all good. And systems programmers.
The mantra was to boldly go where we've already gone before, so use palm line.
and not slash Etsy.
And…
what I found was developers are also systems programmers and observers, if you'd like, and so what we had was an MVS dog and a Unix dog, and Unix Systems Services was the fire hydrant in the middle.
Which, a crude analogy, but in this case, Somebody managing this They might want to manage
Unix system services in the Unix way, so the process ID, the Unix PID, is really important.
Richard Nikula 00:46:18 But a legacy mainframer wants to manage it in the ZOS way, so the address-based identifier.
Jim Porell 00:46:26 is really important. So, this is one of those ones that's hybrid, that both are required. Now, with KICS, IMS, DB2, nobody cares about the Unix PID ID, you know, unless it's maybe Java running inside Kix sometimes, you know.
Richard Nikula 00:46:43 That's right, because you got now your job on this way? Right, you got…
Greg Shriver 00:46:45 Alright, bye.
Richard Nikula 00:46:46 ZOS kicks, and then Java, right? So it's… that's why I said it gets harder when you're trying to
To represent your parents' environment, at each level, but I mean, I see your point, but it's…
So how many different identifiers do you need to be…
Jim Porell 00:47:05 Yep.
Greg Shriver 00:47:06 In fact, I think when we, you know, using the prior analogy of the trunk, I mean, back when we discussed… we discussed this issue, I think, several months ago.
And I think someone, it may have been me, made the proposal that, you know, instead of a process identifier, we should use the ASID, because that's what it is in ZOS.
But of course, that doesn't… that whole thing breaks down when you have multiple process IDs within an address space.
Jim Porell 00:47:36 So, and then for the, you know, to… for…
Greg Shriver 00:47:40 for the audiences that want… that need the actual Unix process ID, that would break that.
Jim Porell 00:47:49 Right. And then you've got hybrid things like ZCX, which has both a Docker version and an OpenShift version, and so that process ID, that container ID, is really important for managing and observability, where on ZOS,
Yeah, not so much, you know.
So, yeah, we… we gotta think about that, and unfortunately, it's kind of recursive in some respects, because, like, you inherit attributes going down. You know, we had the same conversation around virtualization. You start with an LPAR,
Then you might have ZVM on top of an LPAR, then you might have another ZVM or ZOS, and then you have Docker inside ZOS.
You know, what level do you want to get to?
Greg Shriver 00:48:42 Well, and I think…
Angelika Heinrich 00:48:43 We treat each of those as their own entities?
Jim Porell 00:48:46 In some respects, yeah, I agree with that, Andrew, Angelica.
Angelika Heinrich 00:48:52 And she said.
Jim Porell 00:48:53 Yeah, it's step… it's step 5… it's step… sorry, it's… step five is refinement, you know, to get down to that. Yep.
Angelika Heinrich 00:49:00 Yeah, in my mind, the process PID, because I remember we did debate this a lot, but if…
process PRD has meaning on ZOS to some degree, and I think Yeah.
Jim Porell 00:49:13 For some environments, it does.
Angelika Heinrich 00:49:15 environments, it does.
Richard Salac 00:49:21 Yeah, and they bring us on…
Angelika Heinrich 00:49:22 Address space, or address, you know, address spaces and tasks, or, you know, running under a job entry system, maybe that needs its own.
Jim Porell 00:49:32 Right.
Angelika Heinrich 00:49:33 registry, right? I don't… I think overloading process may become confusing.
Greg Shriver 00:49:41 Agreed.
Angelika Heinrich 00:49:42 I don't know.
Bummer.
Jim Porell 00:49:43 Or we didn't get too far, we got two charts anymore.
Probably just share them, because there's just more stuff we have to do.
Greg Shriver 00:49:52 Yeah.
And I wanted to… Richard made a point, too. It's really difficult for…
Someone who, you know, a process or a program that wakes up in a holodeck.
to understand that he's on the enterprise, right? I mean, there's so much virtualization going on, you have no idea, you know, I mean, it depends, it really depends on the level and who is… who is, you know, grabbing and populating that telemetry.
And I think… I don't remember how you phrased it, Richard, but, you know, you shouldn't… you shouldn't really be trying to get in the business of figuring out who your parent is.
Richard Salac 00:50:41 We are in specific.
Richard Nikula 00:50:43 Now we have two Richards, we have to be careful, but yeah, I agree.
Greg Shriver 00:50:46 Oh, yes, oh my gosh.
Richard Salac 00:50:51 Yeah, we are in a specific situation when we, know the value of the, of the starter task, and we are able to discover the address, address space, so we can provide both, just the question is
for us is how, in which attribute, and whether we, whether we actually shared. And this brings a question, how much should the ZOS or mainframe semantics apply for us when we run Andre Unix?
Jim Porell 00:51:30 I think when we're inside Unix System Services.
We should try and be just like… normal…
Unix slash Windows. I think we should be pretty darn close to that.
But… With the exception is, in some cases, like you said, we might have to…
you know, give out the address space ID in addition to the UNIX PID.
Richard Salac 00:51:58 Yeah, I can imagine a real… use cases.
I was just gonna ask.
Angelika Heinrich 00:52:03 for a use case, Richard.
Jim Porell 00:52:05 Exactly, yes.
Richard Salac 00:52:07 Yes, I hope I have one, because we, or let's say…
On the mainframe of the USS, you can have memory limits defined on the address space level, instead of on the process level.
So, imagine a situation that you are getting an error in production because something in your address space is hitting the memory limit, and you are interested in how the memory consumption is distributed between
The processes running within that address space.
And for this kind of analysis, you need both.
Jim Porell 00:52:51 Yeah, I agree. I don't know how we do that, but we gotta figure it out.
Angelika Heinrich 00:52:55 And what would be the…
What kind of a signal are you thinking of when you think of that use case?
Richard Salac 00:53:06 Miss Signal… JVM memory consumption is a standard metric that is…
that is provided by the SDK out of the box.
So, and the process, pit and possibly the address space, identifier, maybe in some additional attribute, are resource attributes, so, so these are automatically attached to every, basically, signal that is produced.
Angelika Heinrich 00:53:35 Every signal?
Richard Nikula 00:53:39 Right, so again there, you need to be producing ZOS metrics, because there are limits within ZOS, and then there's…
Java-related metrics, because there's metrics within Java, right? So it's…
It is very complicated, no doubt about it.
Richard Salac 00:53:54 Yeah, we just started, and it already got very complicated.
And, in closing, we got into a situation when we are maybe in a need of defining, or not maybe, we are in a need of defining a new attribute.
The specific use case for that, that API ML supports OIDC authentication, and basically the OIDC identity is mapped to a mainframe user.
So, for this scenario, we are asked to implement a log signal that will connect these two identities for audit purposes.
And, the standard OpenTelemetry semantics, I mean, the standard one, not the mainframe one, defines user ID as the identification of the user.
But we are in a need to provide the additional user ID, or let's say we need two user IDs, the one… the mainframe one, and the one that was…
Present in the token used for the authentication.
We can, of course, provide, or let's say we can define custom, customer debut. I just wanted, wanted to ask whether.
Maybe, if you see this as a common scenario, and you, maybe had a similar problem or question.
Jim Porell 00:55:34 Why wouldn't that be common to other platforms? So, again, I know enough about what you're doing here, and OIDC providers, that a lot of them do mappings.
you know,
I don't think RACF or, you know, ACF2 Top Secret, whatever we're doing in ZOS is unique.
Because I think you can, you know, the whole idea is
you might have many-to-one type of mappings, you know, through an LDAP server or something.
Is that true, or am I just crazy, and I only know mainframes?
Richard Salac 00:56:13 Yes, I agree that this is not solely related to the mainframe. Also, other products can do similar mappings.
But it… but, you know, this is something…
That is not available in the semantics as of now.
Jim Porell 00:56:34 Right, so I would agree.
Yeah, but I was thinking maybe instead of user ID and distributed ID, because you're trying to come up with common semantics.
I'm thinking user ID and user.mapped ID to show, or user.alternate ID.
So it's not mainframe versus the world, but it's something that's common, consistent across multiple platforms.
That makes sense?
Richard Salac 00:57:05 It makes sense to me. My question is, does it make sense for such issue to maybe… raise that question to the general open telemetry semantics through some issues or some other…
group.
Jim Porell 00:57:19 I think it is. I think from what you just described as a problem, it's probably worthwhile bringing forward.
Greg Shriver 00:57:25 I would agree.
Jim Porell 00:57:28 And the reason is, again, I might…
be monitoring something on a user ID basis, but I want to pick up all derivations of that user ID, so that would include whatever it's been mapped to as well.
It all depends on how you do a search, as an example.
So yeah, these are good. You got more?
Greg Shriver 00:57:53 And then on the other side of that, I mean, on the other side of that, you're always, you know, free to create custom attributes.
Jim Porell 00:58:01 Right.
Greg Shriver 00:58:02 So, but… but it… and that might even be the easy button, like, you know, if you have… if you have a use case, you know, that a… that a customer needs, like.
And can't wait to have semantics ratified, or at least have it, you know, looked at, but…
It's certainly… I agree, I agree with, with Jim that it's certainly worthwhile bringing that forward.
Richard Nikula 00:58:28 I sort of kind of assumed that that was sort of the way that's going to have to proceed, right? It's like, there's only so much that's going to get done, right? But there's a gazillion attributes out there that we've already… everybody's been collecting for years. They're not all maps, so they all got to be custom. Then somebody, you know, will get to an area and suddenly…
oh, now there's a whole bunch of mapped ones. Okay, well, guess what? All these tools allow you to do that, so we'll map them to the right set at some point.
Now, obviously, the more we get right before everybody does it, the better off we are, but…
Greg Shriver 00:59:01 Sure.
Richard Nikula 00:59:01 I mean, of the stuff we've done, it's probably been about
And again, it's more on the metric side, but it's probably only been, you know.
2% of the metrics are actually defined, right? So we've got Lots of other things.
Greg Shriver 00:59:23 Sure.
Yeah, it sounded like you got cut off there, Richard. It sounded like you were,
You know, your battery and your headset might be dying or something.
Richard Nikula 00:59:33 That's weird. It's actually a webcam.
So it's powered. But in any case, that's fine. The point was simply that, you know, that there's a lot of… a lot of… a lot of attributes, and we've only mapped a very small percentage of them so far.
Jim Porell 00:59:46 Yeah, exactly.
Richard Nikula 00:59:47 Where do the rest come from? They have to be custom
This is what they should be, and get them mapped.
Richard Salac 00:59:57 Yeah, Richard, how many more pages do you have? Because it's probably… we're out of time, probably, like…
Jim Porell 01:00:03 like was suggested, you oughta append this to the Slack channel.
Richard Salac 01:00:06 No, no, no, this is the last slide I had prepared for the beginning.
introduction, I promise you 5, I give you 5. Good stuff.
Greg Shriver 01:00:13 Yeah, cause…
Jim Porell 01:00:14 Very, really good.
Greg Shriver 01:00:16 Yeah, this was really good, and thank you for bringing this, and thank you for presenting it, and fostering, and fostering that conversation, so…
So, so yes, Richard, if you, you know, if you could, you know.
provide this deck, on the Slack channel. I think that would be very helpful.
Richard Salac 01:00:39 Okay, definitely, I can do that.
Greg Shriver 01:00:41 Yeah.
I appreciate it.
Richard Salac 01:00:43 Okay.
Greg Shriver 01:00:45 And, thank you, everybody, for your time today. It was a good discussion.
Richard Salac 01:00:52 Thank you, it was a pleasure meeting you all.
Jim Porell 01:00:55 Alright, see you soon.
Richard Salac 01:00:57 Yo.
Angelika Heinrich 01:00:58 Bye.
