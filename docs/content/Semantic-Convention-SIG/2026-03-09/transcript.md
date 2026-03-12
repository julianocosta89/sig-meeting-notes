SIG: Semantic Convention SIG
Date: 2026-03-09
Duration: 61 minutes
Zoom Recording URL: https://zoom.us/rec/share/6uewSxY2szc4keQmiOVkwIw8hjDrt8akK9cVMUx_dmufoU54IsWPlhvlwEUmHHQ.5jHGA9XCFMeaysm6
============================================================

## Zoom Recording Transcript

Josh Suereth 00:02:12 Hey, everybody.
Donal O'Sullivan 00:02:19 blow…
Josh Suereth 00:02:44 Hey, Trask.
Liudmila Molkova 00:02:48 Hello.
Josh Suereth 00:02:49 Hey, folks. I was gonna try to eat some breakfast here. Would someone else be willing to run the meeting? Yeah.
Liudmila Molkova 00:02:57 I think it's my turn.
Josh Suereth 00:02:59 Okay.
Trask 00:03:00 Thank you. I'm suffering from, the time change and haven't made it to my office yet.
Liudmila Molkova 00:03:08 I mean, from the upstairs, or…
Trask 00:03:10 Yeah, exactly.
Liudmila Molkova 00:03:19 Okay.
Let's start with… triage, and please add your name to the agendas list. If you want to discuss something, please add it to the agenda.
PR triage board.
I'm sorry, I'm trying to zoom in.
And it's not working.
R… Ready to be merged.
Okay.
Anything… Wee… Last-minute feedback that needs to be resolved.
Sounds good.
Anybody wants to take a look before I hit merge?
I probably want to take colloqua.
I also want to take a look at this one.
I didn't have a chance.
Trask 00:04:36 Oh, good, thank you. I appreciate it.
Liudmila Molkova 00:04:38 Yeah, thanks.
It's March. Zero.
And… moving to… blocked. Is there anything interesting to talk about here? I think this was on Patrice to… Inside… We're waiting for Patrice to review. I, should probably put it in the awaiting Quad Owner's approval, and… In this… Since Patrice is the co-owner.
Great, and this is probably the… Wayne?
Of course.
So I think it's also a beating Cordona approval.
Stabilized deployment environment, I think I blocked it just because there was a… P… oh, it's a different one.
Okay.
So, I think this was broken down into two different pull requests.
And… C… Let's spend a couple more minutes on this.
Right.
someday show… yeah, they are showing up on a project board, but they are… Awaiting co-owner's approval.
So… It's probably that PR is blocked on this, too.
Is it fair?
Trask 00:06:53 Yes, definitely. Okay.
Liudmila Molkova 00:06:55 Okay.
Trask 00:06:57 Yeah, I think I left the comment here that hasn't been replied through, that's true.
Liudmila Molkova 00:07:05 Chris.
Trask 00:07:10 Oh, maybe the mine was with pipe, too.
Liudmila Molkova 00:07:14 Maybe… okay. But… - Arnalf, he works with you in the service seed, right?
Trask 00:07:26 I… yes, yes.
So I… we're meeting this.
weak.
We meet every other week, so… yeah, we'll follow up there.
Liudmila Molkova 00:07:38 Awesome.
So… Then, there are a few things that are untriaged.
I'm going to move… This one, too, needs more approval.
We talked about log type a little bit last time, right, and… We… the discussion is still going. Should we add it to the agenda?
This heel mark here?
Hilmar 00:08:12 Yes, I'm here. Hello.
Yeah, would be great to get some more insights, if it's possible to continue on that one and, or… I mean, I realized from the last time that there is a kind of workaround regarding using resources, and then do routing by a dedicated resource, but, It feels a little bit cumbersome, to be honest, and not the right way.
the PR I created so far for that one is, I don't know, a work in progress, or I'm happy to have suggestions what could be done better. I'm not quite sure if an enum is correct, or if a free text would be better.
Yo.
Liudmila Molkova 00:09:00 Yeah, like, I've added to the agenda, let's talk about it.
Hilmar 00:09:03 Okay.
Liudmila Molkova 00:09:05 Thank you. So this is on… browsers seek to take a look.
Is anybody from the browser sick here?
Okay, I… I have some questions. Why not url.fu? And probably there is some explanation, but… We'll take a look.
And this is… Belling.
Just spelling.
Okay, moving… On… inquire out of the box on the agenda, and we… Trashed almost everything.
Okay, let's move on to the first… Topic. Initial definition of transaction purchasing system.
Do we have somebody from Mainframes seek?
It doesn't seem so… maybe… They will come later, so we'll just push it.
To the end of the list.
Daniel Dyla (Dynatrace) 00:10:45 Rudiger is here.
Liudmila Molkova 00:10:48 Oh.
Ruediger Schulze (IBM) 00:10:49 Yeah, apologies, just, yeah, just was running between rooms.
Liudmila Molkova 00:10:55 Oh, no problem.
Do you want to talk about the PR?
Ruediger Schulze (IBM) 00:11:00 Yes, I just wanted to… maybe, generally, from the mainframe sake, give a little bit of update, and then, as we had this already ongoing for a while, also wanted to, ask what the next step is on this transaction processing system, PR.
So, This is in context to be seen of what has been done for the COS transaction processing systems.
KICS and IMS, in this case, to implement, open telemetry tracing, so there's a native implementation of OpenTelemetry tracing now available.
And we also have been introducing spans.
and a set of attributes, obviously, on these spans, and this is what's being documented here in this PR, and We had a couple of falls on back, obviously, on this, but I think from what is currently on the PR, this is describing the minimum scope of Of attributes that we would want to… introduce on the TPS to the semantic conventions, and Yeah, my question would be, you know, what's the next step on this PR in order to move forward?
Liudmila Molkova 00:12:23 Sorry, I was muted. So the mainframe SIG is happy with the state of the PR.
Ruediger Schulze (IBM) 00:12:29 I think so, yes, yeah.
And it's also approved… sorry. We also had changes, but I think, in the leadership, but it's approved by UCG Shriver. GS, Shriver as one of the approvals from the mainframe.
6, so it's also approved from that perspective.
Liudmila Molkova 00:12:50 Okay, sounds good. And then you also have prototypes for this, or the actual implementations.
Ruediger Schulze (IBM) 00:12:56 So in this case, it's actually an actual implementation that is available in KICS today. It's part of the product. IMS will follow on this. They are using still, proprietary… Attributes, but we would want to change that as soon as… We'll, you know.
Having the semantic conventions in place.
Liudmila Molkova 00:13:20 Okay, and so essentially what you're looking for is for someone from the… the… some confrovers to… approve from more eyes.
Ruediger Schulze (IBM) 00:13:33 I think so. So from, you know, checks on the PR, I think this is all passing currently, so it's more if it's, correct in the way of writing the PR, and so on.
Liudmila Molkova 00:13:49 I… I will take another look. I think I see some… maybe, I have a lot of questions, maybe we can… spent… Now, 10 minutes talking about this.
right now, since our agenda is not… to PACT?
So, we have a guidance on how to define spans.
And if you look there, you would find some patterns.
And, there might be good reasons for this not to follow patterns, but it doesn't.
Aye.
So, for example, here, this thing… Seems to be high cardinality, and we never put high cardinality things into spend names, because people aggregate, they do metrics from spends, or they do, some visualizations that rely on spend name being lower than LG. So this will, break people's assumptions about spend name.
Ruediger Schulze (IBM) 00:15:00 Okay, I see. So, in… in… so per guidance, actually, what you say, it would be just an indication that… This is coming from a specific TPS system, or kick system in this case.
Not the particular transaction.
Name…
Liudmila Molkova 00:15:25 Yeah.
So, here's the naming pattern, and usually it's action target. So, you would… I don't know if there is any form of operation name or some verb.
That can, like, some action that describes what happens?
But usually we put it first. For example, in case of database, it's… Select something. Oh, usually.
for… it's applicable to NoSQL, but essentially it's a verb.
And then target.
Looking here, the operation name, I don't know, maybe… Is it the program name?
Ruediger Schulze (IBM) 00:16:07 The, program name is a representation of a particular action. Yeah, it could be.
But the program name also has a, you know, can have a certain high cardinality, right? This can be many transactions of… was… you know, with different program names. On the other hand, it helps to identify that, you want to look for a specific transaction, within the transaction processing system. You want to have all transactions which, you know, perform a certain operation.
So, this could be either program name, or actually, the transaction ID, as it is being specified here.
It's also an indication, or it's also an acronym which identifies a specific type of work.
Liudmila Molkova 00:17:08 Okay.
than… Maybe, it's a good idea to compare to how it What we do in other conventions, and maybe find If you…
Ruediger Schulze (IBM) 00:17:23 could have a similar pattern. The pattern is a soft…
Liudmila Molkova 00:17:27 recommendation. The low cardinality is a hard requirement.
Ruediger Schulze (IBM) 00:17:35 And then let's, let's, let's take a look at this.
Liudmila Molkova 00:17:40 And we edited just recently, sorry, you didn't have a chance to know what's for you, what's not here.
And… One thing, like, there is this document that was, linked. It would also suggest you to add something like error type.
Because this is the way, we record, Errors, consistently across different signals.
Here, if you look how it's rendered.
It may be worth spending some time on polishing it and explaining, because… This is the span, it's no longer a document.
So you, you have this freeform text here.
But here, it's the span.
And I'm curious, is there, like, more than… more than one implementation for this instrumentation?
Like, would you…
Ruediger Schulze (IBM) 00:19:26 Yeah, so from a mainframe point of view, it's two. It's two different transaction, action processing systems, KICS and IMS, but when we put this initially together, we were also… assuming that other transaction processing systems could support this, like, for instance, from Oracle, however, we, you know.
throughout, you know, this… this issue, and also related PR, obviously, has been… ongoing for a while. We haven't really got any… Any input with respect to other transaction processing systems?
So, as of now, it's very much COS-specific or mainframe-specific.
Liudmila Molkova 00:20:14 Would it make sense, then, to use the prefix that's specific to?
Ibm or mainframes? TPS is very generic.
Ruediger Schulze (IBM) 00:20:24 Yeah, right, and that's a valid question. So, if maybe from a community point of view, no other… Transaction processing systems would be currently considered, then we may think about making this mainframe-specific.
And, we would have to look at if it's CUS TPS, or COS, or mainframe TPS is probably something to consider. We have both namespaces currently being defined, I think.
Yeah.
Liudmila Molkova 00:21:02 I am curious what others think, if from… from my perspective, it seems… since you're in development, and you still want to be… maybe include other vendors to support it, it may make sense to start with TPS, but it would probably be a blocker to stabilization to find the second one, if it, stays in this namespace. I'm curious what other people think.
Michele Mancioppi 00:21:34 I would start with an IBM prefixed.
Thanks, Pace.
Honestly, I've… IBM is the only vendor.
that I know that is, considering A meeting open telemetry from a system 30 years old, which is kudos to you folks.
Thank you. But I will not expect a second one to appear anytime soon on the horizon, so… Something that is… this is pretty specific for kicks.
I would even use the word kicks in the name.
IBM.kickstart.
Something.
Trask 00:22:14 My question, Radier, would be, if there… what is the path to getting a second, like, is that, and… I would… try to… if you want to use the general… oh, I mean, if… yeah.
I would try to front-load that.
in terms of, Adding a second.
Ruediger Schulze (IBM) 00:22:41 Bringing in a second.
Trask 00:22:44 to use, if you want to use the TPS. Otherwise, if it seems unlikely.
In reality, then, yeah, there's nothing wrong with using the, the IBM prefix for it.
Ruediger Schulze (IBM) 00:23:02 Yeah.
I mean, we… There would be an… obviously, Oracle would be one of the vendors. We could fill this in as a vendor.
Name, but it would be important then also to get some feedback or, comments from, you know.
Those type of transaction processing system owners.
Trask 00:23:32 We've got a couple folks from Oracle, involved in semantic inventions, Definitely, you know, seems worth reaching out to them.
Ruediger Schulze (IBM) 00:23:45 Yeah, maybe… would it be something to post on the Semantic Convention's Slack channel, just to ask if there's any… Perspective on that.
Trask 00:23:58 Oh, for sure. I mean, we would probably even support if you wanted to write a blog post to, you know.
Ruediger Schulze (IBM) 00:24:05 about the effort.
Trask 00:24:08 looking for… contributors…
Ruediger Schulze (IBM) 00:24:13 Okay, sounds good.
Liudmila Molkova 00:24:18 If you start with, Slack post, I… I'll tag the people from Oracle that were involved, and maybe they can… Can think about something, but blog posts would be amazing.
Ruediger Schulze (IBM) 00:24:33 Okay.
can do that.
Liudmila Molkova 00:24:38 Nice.
Okay, awesome. Thanks for bringing it up, and maybe there are other spans. You can also apply this, the discussion to them, probably.
Ruediger Schulze (IBM) 00:25:18 Right, right.
Liudmila Molkova 00:25:21 And for the entities, and just wanted to take a look at different things.
This is the… Tps entity, and the only attribute it has is Region ID.
Is it right?
Ruediger Schulze (IBM) 00:25:39 Yes.
So this is the entity, you can imagine this, this is, like, the entity that is running the particular transaction from.
Liudmila Molkova 00:26:00 Yeah, I'm thinking, like, if it's… Aren't there more things that identify the system?
Ruediger Schulze (IBM) 00:26:13 We kept it… to a minimum, there are probably other things that we could add. This potentially goes then also into… considerations, like, if it's a distributed system, it could be the process ID. In the COS world, obviously, this would be the equivalent to a process ID. We talk about address-based IDs.
If this would be… something to… to… to take into consideration. Obviously, the region ID, this is something to… as a… as a minimal identification, Yeah, it's a… it's a little bit a question of how to… To… how far to take the… the identifying attributes here, or… from our perspective, at least, the region ID would be sufficient for a unique identification.
But could be enriched with additional information on… Process and system information, eventually.
Liudmila Molkova 00:27:26 I think Josh… You wanna say something?
Josh Suereth 00:27:29 From an entity stan… oh, I'm… hold on, my camera's still off. Anyway, from an entity standpoint, I think… I think region ID is totally fine. Like, if your entity is simple, and it's just like, hey, we have an ID, What's… what's interesting here is when you start to balance this with metrics that you're gonna create, right? Because the entity is identifying for the metric, it's identifying for the span, so this gets into cardinality. If you start adding too much to your identity.
you can start making your metrics kind of unwieldy or unusable. So, I actually like the fact that you have just a single ID that's, like, unique and identifying here. But when you do your metric design.
Cause you're… I think this is just spans, right?
Ruediger Schulze (IBM) 00:28:14 Right now, it's… yes, correct. It's… right now, it's just spans.
Josh Suereth 00:28:18 Yeah, so if you do your metric design and you're tying your metrics against the same entity that's producing the spans, those metrics will implicitly have this as part of their cardinality, right? And so, that's where things kind of get interesting, which is why I think keeping it minimal is generally better.
You can do as much as you want with descriptive attributes if you wanted to add those, right? But in terms of, identifying, we want to try to keep those minimal so that we can Make sure our metrics are manageable.
Ruediger Schulze (IBM) 00:28:48 Okay.
Liudmila Molkova 00:28:51 I, I… don't mind having one. I think it's… then the name should be precise. It identifies the region. We had this with, like, service instance that was part of the service identity.
Josh Suereth 00:29:07 Oh, yeah, the entity name should be TPS.region.
Liudmila Molkova 00:29:11 Right.
Josh Suereth 00:29:12 And that would be the entity that you tie things to, yeah.
Liudmila Molkova 00:29:31 Okay!
I think we… There's a lot of feedback around this one.
Ruediger Schulze (IBM) 00:29:41 Very good, thanks, appreciate that.
Liudmila Molkova 00:29:44 Thank you! So you have another topic, seek plans for 2026. Thanks for sharing this.
Ruediger Schulze (IBM) 00:29:51 Yeah, and just want to keep it brief, but I have a couple of questions on this, and if you want to click the link on the sick plans, it's leading to the… I think it was an issue that you had opened earlier.
So, obviously, with the open telemetry tracing functionality now in place, we also want to expand our focus to, metrics, and, that obviously drives questions around representing resources or entities, and, but also looking at other aspects of the, tracing capabilities again. So, in terms of So, a couple of questions, just, I think the messaging, semantic convention SICK is currently on hold. I wasn't sure about the database one, but… Obviously, in regard to MQ, we also have span attributes. Also, for DB2, we have span attributes.
Is, you know, should we just move forward with, also.
putting an issue in the PR, representing those… those attributes, and then bringing them forward to this SIG meeting here? Or is there generally, let's say, a hold on activities around messaging, and we should just wait and… Come back once the messaging stick is being re-established.
Liudmila Molkova 00:31:23 Yeah, if you're, like, for DB2, the database are… Stable?
The… when it comes to the SQL databases and DB2, it should be as straightforward.
The question is, do we… Host… DB2 conventions here in this repo, or we would rather consider… ask you to consider hosting them somewhere in the ABM ecosystem, just because they… they didn't exist so far.
In semantic conventions, and they are probably… not entirely the same as mainframe SIG scope?
Ruediger Schulze (IBM) 00:32:06 I mean, the database in this case is specific to the mainframe, but there's obviously an overlap to distributed database functionality as well. But specifically here, and this is also something functioning new from a specification point of view.
On the mainframe side, we are having a server span for the database system.
Where I think the current spec is largely focused on client spend.
Functionality from a database point of view.
So, that's something, I think, to, you know, have a discussion on, or to be looking at.
Liudmila Molkova 00:32:46 Yeah, this is the great point, because there are a bunch of instrumentations in Collector that deal with database servers.
And, they are slightly different because they don't provide native instrumentation. They take what they can take from the database, On the collector's side, and they expose it in… open telemetry look and feel. But I… I think we… and some other people wanted to do server database conventions. If you are interested in this.
It would be great to find… the community, and see how much interest. So far, we've been telling people to build it on the site, not as a.
Ruediger Schulze (IBM) 00:33:39 Potentially.
Liudmila Molkova 00:33:40 Metroid Project.
But if there is a lot of people and you are ready to build a community around it.
It could be an option, I feel.
Ruediger Schulze (IBM) 00:33:50 Okay.
There's maybe a similar topic for a blog, as we discussed before.
Michele Mancioppi 00:33:59 If I can provide some advice on this one, it's… A pretty good idea, in my opinion, to actually Publish a first version.
of the semantic conventions, the way you would do it using Weaver.
It's, it's a pretty smooth experience. With something IBM prefixed.
And then you write about it, and then, People are going to come up with more opinions than otherwise.
You know… Okay.
Man is wrong on the internet effect.
You've done something tangible to disagree with, and… You're gonna find more of them.
Ruediger Schulze (IBM) 00:34:37 Sounds good.
Liudmila Molkova 00:34:46 I love your suggestion, Mikhail.
Michele Mancioppi 00:34:50 Meme on the internet, it always works.
Liudmila Molkova 00:34:53 Yeah, so for messaging, is it also, like, you're interested in the server side?
And the client, or just the server?
Ruediger Schulze (IBM) 00:35:02 It's both, it's both, but it's, I mean, what we produce is obviously server-side.
But it's, Yeah, it's actually a football's, Putting and getting messages, or receiving messages.
Liudmila Molkova 00:35:20 Yeah, that's one that's tricky, and I… I would say… Pick… not more than one, maybe less than one, but not more than one of those efforts at the same time. Like, from the past experience, it's not visible to drive.
Two such big efforts at the same time.
Ruediger Schulze (IBM) 00:35:46 Okay.
Liudmila Molkova 00:35:47 Yeah, and the principle is the same, like, the server side is tricky. The client side, I think, Trask, you were thinking about… doing messaging this year? Do you still think it's… it's a good idea?
Trask 00:36:08 I do think it's a good idea, I… I'm not quite… Yeah.
It's a… tough one, but it's a… it's an important one. I suspect we won't finish it this year, but I would like to try to start it this year.
Liudmila Molkova 00:36:35 I agree.
Trask 00:36:39 And by… I would like to start it this year, I don't mean I would really enjoy it, but it feels very necessary, so I think we will.
Liudmila Molkova 00:36:53 I saw something else in your, list here, very interesting, the job processing?
And…
Ruediger Schulze (IBM) 00:37:02 Trade.
Liudmila Molkova 00:37:05 This is also for the server. Well, internal, background, what kind of job processing?
Ruediger Schulze (IBM) 00:37:12 So, obviously, on… on the mainframe side, specifically on CUS, you have, job execution has been also there since, you know, long history.
And this would be specific job execution from a mainframe perspective, but there might be actually, again, also generic concepts to job execution. That's probably something to discover and discuss as well.
But specifically, COS has a job entry system. JESS has also two of them, JESS2 and JESS3.
There's a specific job, control language, also there, since… Decades. But that's essentially what we would be looking at here from a… From a job processing perspective, to have, representations then… Around this type of job execution.
But, you could generally frame this as batch type of workloads.
And, this is obviously also present on other platforms.
Liudmila Molkova 00:38:23 Yeah, sorry, give… give me one second, Tate. I'll be… Have a kid.
Yeah, I'm sorry, thanks for waiting.
I don't know.
neil yashinsky 00:38:48 Duty calls.
Liudmila Molkova 00:38:51 Thanks.
So I'm… I wonder, from this group, we have a lot of different areas that Need some guidance for job processing.
like, the GenAI conventions, I think, is this… is one of them, but also, just in general, the background job processing. I wonder if we can put together some very basic guidance, like, what span kind do you use, and I don't know, how do you… Record links, because obviously you cannot record batch processing without links, even though it sucks.
Like, would it be something helpful?
Trask Stalnaker 00:39:44 Yeah, we have a… I mean, I know in the… I did a little… digging in the Java instrumentation repo, and… We have, At least 5, Background job instrumentations?
like, kind of scheduled job instrument… I was kind of breaking it out when I was looking through our instrumentation, and there's scheduled jobs, and then there's sort of, like, job processing, Which is… not… which doesn't sort of have that scheduling concept, and maybe, is maybe more focused on the batching or other pieces. We didn't have much, we just had… I think there was, like, spring batch, and maybe one… I think that was actually the only one that was not a… Scheduled job.
But anyway, yeah, A couple of those are reasonably popular.
Java libraries, like Quartz and Spring Scheduling.
It would be nice to have some… Understanding of what we should be emitting there.
it's been raised externally. We chose internal, I mean, even just the span kind, we chose internal.
Way back when.
And… There's been some questioning of whether that's… Correct or not.
Liudmila Molkova 00:41:23 I'm thinking, should we… should this be a pre… Per rec for messaging? Because the messaging could rely on the principles.
Trask Stalnaker 00:41:34 Can we…
Liudmila Molkova 00:41:35 Try to… Do this, and messaging will be easier after.
Trask Stalnaker 00:41:43 I don't remember it coming up in the… when we were doing messaging, though, like it…
Liudmila Molkova 00:41:51 I think we have some principles and messaging that where people apply for, even in process things, like… Spend links, kinds… Q&a.
Things like this.
Trask Stalnaker 00:42:13 Yeah, links is something that comes up, like, that even came up recently in the GenAI… Yeah, like… for a consumer span, and let's kind of apply… yeah, I can see the connection there with the messaging. For a consumer span of one.
Consuming one thing.
Like… Should you just use parent, or… Like, if it's always just one… parent.
Michele Mancioppi 00:42:43 Yeah, the problem is that with messaging, instrumentations, you tend… Not to know.
How many messages you're consuming?
Trask Stalnaker 00:42:56 It's not necessarily… I mean, that's not necessarily… at least in the Java APIs, the majority actually just consume, except one at a time, like, unless you're doing a poll… your own manual pull, but if you're getting… using a higher level API, You're getting fed the single message.
Michele Mancioppi 00:43:20 I have different experiences with Kafka, but sure.
Liudmila Molkova 00:43:24 Yeah, I… I just… sorry, I should have paid more attention to time.
We have two more topics, Maybe we can continue this discussion next time?
Would it be okay, Ridicar?
Ruediger Schulze (IBM) 00:43:40 Yes, that's fine with me. And again, appreciate the time that you're spending on this.
Liudmila Molkova 00:43:46 Oh, man.
Thanks for coming, and so, great discussion, and I think it helps us prioritize better.
Ruediger Schulze (IBM) 00:43:53 Thank you.
Liudmila Molkova 00:43:56 Thanks. Okay, Donald?
Did I pronounce your name correctly?
Donal O'Sullivan 00:44:02 Hey guys, Jorge. Yeah, I'm new here. Nice to meet you.
Yeah, so I just was bringing this to the group's attention. We've got a bunch of approvals from the, from the systems, work group, so I think at the start, Ludmila, you'd said you'd review it, so there's probably not much to talk about here.
Because I know you're… you're talking about time there, so… Yeah.
Liudmila Molkova 00:44:29 Excellent.
Thank you for bringing it up, and yay, I was waiting for this, Pierre.
Donal O'Sullivan 00:44:35 Great. Thank you.
Liudmila Molkova 00:44:37 Thanks.
Okay, and then… let's… Talk about log type.
So, Hilmer, can you, summarize, the discussion, or B&B?
Josh, you want to summarize?
Yeah, Josh, go ahead.
Josh Suereth 00:45:02 Yeah, so basically, I think… We… let's talk a bit about process, because I think this is important for this.
What you're trying to do is design How to handle log.type.
And semantic conventions is not a place for design. Semantic Conventions is for, like, when you actually want to take something and say, now this is a convention everyone uses. So, I actually think that this should not be a PR, and what you need to do is start working on the prototypes, or, like, an OTEP around how we want to handle log things. And this was in our feedback, this was in our discussion before. But effectively, like, from my perspective, there's no way I can approve this right now, because we don't know if it's gonna work.
I agree with you that the thing I said about using resource is my current prototype of what I'm doing to solve this problem, and it's gross as hell, and I don't like it.
But that's… that's, like, what works today. If we merge this PR without knowing if it works, or knowing how this works through the whole system of OpenTelemetry, that's not a semantic convention. That is just, like, a risk.
So I think we, like, I'd love to see a prototype that shows this working end-to-end the way you intend, with the controls that we need to solve the problem at hand.
what might be a little bit better than semantic conventions is to start with an OTEP or a design, where we can actually start fleshing through the problem itself.
And figure out, how do we want to solve this in OpenTelemetry.
Right? And then once you get past that, you get into a prototype, we show this working, then we get to semantic conventions as kind of the last step of, okay, cool, now we can encode, these are the attributes we use to solve this design. But I think you're well before the semantic convention stage, and I think that's a thing that we previously allowed, like, early in semantic conventions, that was a mistake for us to do as well, that we're trying to fix. Of, like, let's give this thing time for design, let's actually let you run free making designs and making this work, but you don't need to put it in semantic conventions to do that.
And actually, semantic conventions would be a very problematic place to have it, because we shouldn't be making lots of changes in semantic conventions. We shouldn't be breaking this. So let's make sure what you're proposing can actually work, which I don't think it can as designed, with OpenTelemetry the way it is today. And we can talk through that if you want.
But foundationally, I think that, like, this is the wrong place to put this right now, because I think you still have fundamental design things to solve. Does that make sense?
Hilmar 00:47:32 Yes, maybe? I don't know. I'm… yeah, I'm open to everything which brings this a little bit step forward, and you're probably right. I mean, when we started investigating in how can we leverage OpenTelemetry for audit logging.
We also were thinking, hmm, we have… Traces, we have spans, metrics, can we maybe have logs?
and audit logs, is this an additional channel, maybe, and treated then differently, or not?
But, yeah, on the end, we decided to… let's give it a kickstart and see how far we come with the… with the regular locks. And then we realized, okay, if a system is under a heavy load, and we have a lot of logs, then we need to distinguish between normal logs and others, and that's why I thought maybe let's have a log-type thing, and then do different processing and separation there.
Would be great if you can give me an idea about how you would like to have such a prototyping, how it should look like, or if there is something similar which I can take as a template or something.
or an example OTAP, which goes maybe into the same direction.
that would help me a lot, then I'm happy to create such things and see if we can continue there then.
Josh Suereth 00:49:01 Yeah, actually, I think, most recently, a good prototype would be some of the stuff the Service and Deployment SIG has been doing.
Around, like, criticality. I'll see if I can find that PR and send it to you. They do, like, a whole investigation into the space and that sort of thing. The other thing is, from OTEPS, you can look in the specification, like, OTEP directory and find the PR that led to the OTEP. You can see in there, in each PR, we list, like, what prototypes we expect. I think if you look in the specification, there's active, design discussions around prototypes and things.
Where you can see, like, the discussion that happens, the things you have to fill out, the expected prototyping that's there. In semantic conventions, we are trying to get more rigid around prototyping, of making sure that the convention actually matches a design and a pattern that works in real life.
Anyway, I'll find some of these PRs and get that in the notes quick.
Hilmar 00:50:02 Thanks.
Great.
Liudmila Molkova 00:50:05 things… one thing about prototyping, for logs specifically, and up until I'm sure we have Two ways to… maybe more than two, but two major ways to emit logs. The first one is through log bridge.
And, like, you use your SLF for J, or whatever, logger, something, some log facade in your language, and then OpenTelemetry maps it to your OpenTelemetry format. The other one is people emitting things explicitly through OpenTelemetry API.
And the… I'm not deep into the discussion, not as deep as Josh, but for me, it would be important to understand who and how is supposed to Populated, and when.
Hilmar 00:50:55 The answer is very clear. So, the log bridges won't help here, because this is very generic, and then nobody knows, actually, who, I don't know, created the underlying logs in the end, and a lot of them are then regular info warning debug logs or something.
And those are normally not audit relevant.
So it's, in the business cases, most of the time, really using the API and saying, okay, this is now something I need to record for, kind of, ever, so 10 years, 20 years, whatever, and then this is happening via the APIs.
Josh Suereth 00:51:37 In my experience, there's a specific API for audit logs. That's why I think that this design… this, like, deserves an OTEP. Like, you know, and there's, like, different kinds of audit logging that you do around either access to data or access to systems. It tends to be tied up with your auth, but generally, at least for us, it's always a dedicated thing that you know you're audit logging and that we can track.
and enforce, and that sort of thing. So, that's why I think audit logging… I know there was an OTEP for audit logging inside of OpenTelemetry that kind of got, hey, we don't have time to work on this right now.
But I do think that you're… I don't want to conflate what you're doing. Like, let's see if we can solve some minimal problems, but, yeah, like, to your point there, Lydmilla, I don't think we want a logging bridge creating audit logs. Okay.
Liudmila Molkova 00:52:31 then what… to your point, Josh, the… There are a lot of audit logging formats out there, and the way to make progress would be to analyze them and find commonalities and see if the goal is to start with log type, then it should be just part of the plan.
Not the… the whole plan, and we should understand how it helps To express these different formats.
Josh Suereth 00:52:59 If I can rephrase that, because I like that. Hilmar, you could start with take existing audit log formats, and try to make a semantic convention for how to represent all of them, and have something that can suck them out of their existing files, and convert them into LTLP in this format.
And that might be, like, that might be a step one.
And that might be a decent demo, if you can show that transformation and say, this convention matches all of these audit signals that we need. That doesn't solve the, like, how does OpenTelemetry generate it inside of its API SDK? That doesn't necessarily solve, like, the protocol of, like, you know, how do we… make sure that these things are a separate stream, and make them efficient on that separate stream, but it is progress, and it is the kind of prototype we would want for a semantic convention. Does that help?
Hilmar 00:53:50 Yeah.
not quite clear if I got your point right, but, I'll see and come up with something, maybe… I hope till next week, maybe till I need a little bit longer, but, yeah, then we can…
Michele Mancioppi 00:54:04 Maybe have a follow-up discussion on that.
Hilmar 00:54:06 Thanks.
Liudmila Molkova 00:54:09 Thank you.
We are at the end, and we still have time. We can… Come back to… Some of the mainframe discussions?
Does anybody want to bring something else?
Okay. Then maybe… We should talk about… There's two things, we didn't have a chance.
Ruediger Schulze (IBM) 00:54:44 Right, so, as I was starting to talk about, so we're also now looking at, you know, turning our attention to metrics, and, obviously, Josh, I've been on a couple of or a few of the entity SIC meetings, but haven't joined recently. So, what I would be interested is to understand, you know, where we are with entities and also the relationship definitions.
And specifically, as we also had been in contact last year.
When we look at concepts like virtualization, then, the, you know, specification of relationships, obviously, is of interest here, and also to express of… And I've, like, for instance, a virtual machine is being hosted on a particular server or host. And, Then, currently in the semantic conventions, also, there's no… I think virtualization is not covered yet, even there was, I think, Josh, you had a proposal at that time. So, I was wondering if there was any work done since… last year, I think it was mid of last year when we looked at this, but obviously, if you look at, from a mainframe point on, you know, providing metric support, and if we take it from the bottom up, from platform to operating system, and then workloads.
We would have to have, you know, some, you know, representation of virtualization concepts being available in these semantic conventions, and just wanted to check on where things are, and maybe then also what type of contributions would have to be made in order to move things forward.
Josh Suereth 00:56:32 Yeah, so, right now, Let me add the OTEP into the chat. Where are we… where are we now in the chat? Did we move up… back up?
I saw notes.
Oh, entity relationships, here we go. So there is a OTEP around entity relationships. It is approved by the SIG, but it is not merged yet. But if you wanted to see, like, how we're thinking about relationships here.
you can… you can take a look at this PR, and this denotes, like, what… what they look like, and how they're, communicated. We are still not planning to put them in, the OTLP resource, we're planning to send them as a separate event that would be sent via OTLP.
Ruediger Schulze (IBM) 00:57:20 So they're still a separate channel.
Josh Suereth 00:57:22 In terms of virtualization, yeah, I had that proposal, and that has been, like, number 3 on my priority queue set for a whole year, because number 1 and number 2 are still not done, which is Semantic Convention, Federation, and Weaver, right? And then, entities itself, like, the core entities work.
So I still, like, until those are done, I can't really pick up more stuff, and… That work is taking me a lot longer than I would like to say publicly, so I will just not tell you how long I've been on it.
That said, we've been making good progress on both, and would be happy to talk more about all of that. The entity thing, that's your… what's going on for relationships. Virtualization modeling is still something that would need to happen, and it might make sense to pull together, like, the folks who are doing container-related stuff, possibly, or just, like, a VM… you know, we're gonna do EC2, we're gonna do overall virtualization, we're gonna do, Azure VMs, we're gonna do Google VMs, we're gonna do, what are they, like, HyperX, and Mox Procs, and all that crap, and we're gonna… make a SEM conv around that, you know?
The virtualization space is fun, I think it's relatively stable, so I'm not really worried about us coming up with a set of conventions, but I do think the conventions we have today are… really heavily, hey, Kubernetes, and might not necessarily serve you that well. So, I think… I think it'd be good to put that group together. I do not have time to put that group together, which is why, like, I've been lacking at that, and I don't know of anyone else who has tried.
Unless someone else is aware of that.
Ruediger Schulze (IBM) 00:59:10 Okay, so specifically for virtualization, I think what you're saying is to putting together a dedicated Semantic convention sick group.
To focus on representation of virtualization concepts.
Josh Suereth 00:59:26 Yeah, just to make sure that we have, that we're accounting for the space, and that we can model things that people do.
Ruediger Schulze (IBM) 00:59:35 And supposedly, this goes through the regular process to… you need to propose a project, and then it needs to be agreed, and then the related SIC would be established, right?
Josh Suereth 00:59:48 Yeah, and if you don't get active interests, what it could mean is not that it's… One thing I always want to say, if you don't get active interest right now, it's not that it's a bad idea, it's that everybody else is working on higher priority things. Like I said, this is, like, number 3 or 4 on my list, it's just, unfortunately, the top 2, I still haven't finished, so…
Ruediger Schulze (IBM) 01:00:13 Is this… just let me ask this, so if there are, you know, the prereqs that you said, is this then something to push forward virtualization right now, or is this something to clearly say there's a dependency?
Josh Suereth 01:00:30 you could say there's a dependency. I, like… I think you could probably make progress without having to fully understand how virtualization for other machines is gonna work out, because I still find mainframes are similar, but different. And so, like, if you're looking for someone to give you a pattern for how to handle virtualization.
I could see that as a dependency, but if you were, like.
you know, we're gonna define the pattern, and the virtualization group can use us as a reference. I'm actually okay with that, I don't expect you to use the exact same semantic conventions. Now, I could be wrong about this, but I just don't see that happening, right?
Ruediger Schulze (IBM) 01:01:15 Okay.
Liudmila Molkova 01:01:20 Yeah, I don't want to interrupt, but we are at time.
It's a great discussion, and let's keep it going.
Ruediger Schulze (IBM) 01:01:30 Okay, yeah… Thanks, thanks, thanks very much.
neil yashinsky 01:01:33 Yeah, thanks, Ludmila, for your leadership. Thanks, everyone, for their contributions. Have a great day.
Liudmila Molkova 01:01:37 Thank you, have a good day, see you around.
