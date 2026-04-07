SIG: Entities SIG
Date: 2026-04-06
Duration: 49 minutes
============================================================

## Zoom Recording Transcript

**Arve Knudsen** 00:21 Hello, hello, Kyle.
**krajo Krajcsovits** 00:25 Hey, Hade. Hi, dude.
**Arve Knudsen** 00:31 How are you doing?
**krajo Krajcsovits** 00:33 I'm good, thank you.
I did 3 days of hiking.
**Arve Knudsen** 00:37 For the four days.
**krajo Krajcsovits** 00:38 Which was nice.
**Arve Knudsen** 00:40 That sounds fantastic.
**krajo Krajcsovits** 00:42 Yeah, yeah, I got the blisters to prove it.
No, it was fine, but it was the first weekend with good weather, and they really took advantage. I really want to go next weekend, but I'm on call, so… It's gonna have to be 2 weeks from now.
**Arve Knudsen** 00:59 Fantastic.
**krajo Krajcsovits** 01:00 How about you? How was your weekend?
**Arve Knudsen** 01:03 But it's been very good. The weather is nice here.
We had a lot of sun today, so we also went on a… I mean, we went on a long stroll by the lake.
**krajo Krajcsovits** 01:15 Nice.
**Arve Knudsen** 01:16 So, nothing as intense as, as your hike.
**krajo Krajcsovits** 01:21 It wasn't that interesting. I mean, we did 18K on Friday, like, 12.
Saturday and 15 today.
**Arve Knudsen** 01:30 Yeah.
**krajo Krajcsovits** 01:31 But, yeah, we're progressing.
I don't actually know, like, this… it's Easter, so I have no idea if other people will show up.
**Arve Knudsen** 01:40 Maybe it's… yeah, I don't see anyone joining, so maybe it's… Oh, wait, there's somebody.
**Josh Suereth** 01:45 Hey, sorry, semantic conventions ran over.
**Arve Knudsen** 01:48 Hello, Josh.
**Josh Suereth** 01:50 How's it going?
**Arve Knudsen** 01:52 Good, how are you doing?
**Josh Suereth** 01:54 Not bad, not bad. Sorry we've been canceling a bit.
QConn, and then, vacations, apparently.
So, I haven't seen if other folks are attending today, but… Yep.
Do you guys have agenda items?
**krajo Krajcsovits** 02:11 Oh, I didn't put in merchandise. I have a bunch of questions, because I'm getting involved more in what ARV is working on, if no?
Okay.
And, it's related to resource attributes and entities, and I got a bunch of questions.
Let me see if I can…
**Josh Suereth** 02:29 Edit.
**krajo Krajcsovits** 02:30 agenda.
**Josh Suereth** 02:31 you know, you should be able to edit it. If you can't, let me know. I'll… Present, and we'll type them up.
**krajo Krajcsovits** 02:39 Oh, God.
**Josh Suereth** 02:39 Let me check and see if anyone else is joining.
Okay.
Let's see… Okay, give me 2 seconds.
**krajo Krajcsovits** 04:03 Sure.
**Josh Suereth** 04:21 Alright.
Haven't heard back, so let's get started.
**krajo Krajcsovits** 04:31 Yeah, so, as I said, I'm… joining ARVA in work on Prometus and Mibir around resource attributes, and by extension, you know, entities.
And I've been to one of these meetings, and I read a little bit of the spec, but, like, it's not like I… I know a lot, so I'm… Coming this… kind of fresh, so I want to just… You know, clarify a few things, and just starting with the most basic questions.
You know, because looking at the spec, Yeah, I think that is the thing that I looked at. Let me see…
**Josh Suereth** 05:11 Have you read the OTEPs? Because there are… I think there's links from the OTEPs.
Like, there's a motivation.
**krajo Krajcsovits** 05:22 Design piece… yeah, okay, I'll… this… okay, I'll read that.
**Josh Suereth** 05:26 Okay.
**krajo Krajcsovits** 05:28 Yeah, we don't have to actually go into that.
**Josh Suereth** 05:30 I can give you the elevator pitch, too. Yeah.
**krajo Krajcsovits** 05:33 That would be awesome.
**Josh Suereth** 05:34 Yeah, the elevator pitch, the way I usually describe it to people is, you know, when you think of interacting with observability.
there is the search pattern API, of, like, tell me what data's in this database, right? But then there's also this issue of having, like, a…
**krajo Krajcsovits** 05:52 Having a… what, sorry? You're cutting out.
**Josh Suereth** 05:55 My USB just disconnected, sorry.
Am I back?
**krajo Krajcsovits** 05:59 You're back, yeah.
**Josh Suereth** 06:01 Okay.
like, the left-hand navigation panel, right? The left-hand navigation panel of, like, cool, I want to see what clusters I have, I want to see what namespaces are in those clusters, I want to see what pods are running, and I want to explore space in that sense. Or I want to know what services I'm running, and how many instances per service, or I want to see, like.
You know, what organizations there are. It's like, it's like a hierarchical view.
But it's kind of the left-hand nav panel, and we need both. Like, OpenTelemetry sends signals, and it also has resource, and resource is that kind of hierarchy of thing, and, and Problem number one is left-hand nav.
And when you take the implications of that, that gives you a set of things, right? Like… I need to aggregate by that. So, I want to know what's the CPU usage for all pods in this namespace? That kind of a thing.
But it… but it all starts from that kind of, like, left-hand nav panel, if that helps. That's my elevator pitch.
there's more that we can do with it, like, all sorts of crazy things. But that's, that's predominantly what it is. Now, where things get fun… This is past the elevator pitch, this is into the real-world problems we have.
Observability databases are one of two Today.
Type 1 is a time series database, like Prometheus.
Where you want to kind of limit cardinality.
And you throw everything into a big old flat, you know, key-value pair thing with a point at the end.
Or you have these columnar databases, like, you know, ClickHouse, or for at Google, it's BigQuery, is our thing, you know, that we have. It's not like a relational database, you know?
And those are optimized where the more columns you have flattened out, the better. I think Honeycomb might be similar.
And so, people are trying to shove All of that data into these… into every single row.
Right?
and so, with entities, we're trying to give you a little bit more flexibility here.
We want the ability for you to quickly group And aggregate data.
with the OpenTelemetry data model, so if you need to, say, group on cluster, you can do that quickly. But we also want to make it so if you want to store those attributes.
that are not identifying, but important for driving a UI, and you want to store them in a separate, you know, row, or a separate table, and do a join, that you can kind of get the best of both worlds, right? So that's why we have this notion of entity identity versus descriptive attributes.
Quickly grouped by the, you know, foundational structure, but you can also do your queries with, like, the actual human readable component that's important to humans.
So we're trying to give you options there, and this is why Entities has two output channels. You can either fully encode them in the signal itself, so every single row has all of that data.
Or, you can have it as a separate relationship channel.
Where I try to keep just the key identifying attributes with the signal, and I have separate tables that I use for the descriptive things, right? So, because they're reported separately, as separate signals.
That's kind of the, Phase 2. So, Phase 1 is… we just make it clear to you that everything's coming out one channel, and you can decide to store it however you want.
Because we'll let you know what's identifying, what's descriptive, and we'll let you do the bundling grouping how you need.
Phase 2 is where you can actually just not send the data to begin with out of the primary metrics logs, you know, span channel.
And you can get it out the separate, you know, event entity relationship event that we're planning to fire and send and have things for. There's prototypes in the collector already that do entity, events, by the way.
I think it's sort of.
**krajo Krajcsovits** 10:14 Does that mean… But you're still sending the identifying attributes with the primary SQL, right?
**Josh Suereth** 10:22 still be sending primary… yeah, yeah, yeah. Like… I mean, the macro thing is we need to send just enough information to signal that you identify where it came from, and that you can do the grouping you need efficiently.
And we send, Things in the other signal to allow you to do higher level flows and control and that kind of stuff.
**krajo Krajcsovits** 10:56 Interesting.
And… Like, do you have a timeline for these phases? I guess we are in phase one, or early phase one.
**Josh Suereth** 11:07 Yeah, we've blown our timelines out of the water, just from lack…
**krajo Krajcsovits** 11:10 Love it, man.
**Josh Suereth** 11:12 Yeah, lack of, like, speed, and, you know.
we have a lot of hard challenges, so we're in Phase 1. The goal was to have Phase 1 out by the end of last year. That did not happen. We got a bunch of sidetracks with, like, trying to solve for RUM, trying to solve for resource mutation. There's a bunch of problems in OpenTelemetry.
that are important, and are, like, somewhat related to this left-hand nav thing, this, this identity thing. So, we kind of chased some, some, Rabbits, if you will, if you know that, Turn a phrase from Alice in Wonderland.
**krajo Krajcsovits** 11:54 Oh, yeah.
**Josh Suereth** 11:55 Yeah.
**krajo Krajcsovits** 12:02 And I see this meeting is recorded because, I will have to listen back, which… you gave me a lot of information in such a short time, my head is spinning. So, anyway.
**Josh Suereth** 12:13 Of course, yeah, and it absolutely is recorded, and if you, I'll find the link so you can find the recordings. It's in…
**krajo Krajcsovits** 12:20 Yeah, that would be a… that was my second question, like, where do I… grab all of them.
**Josh Suereth** 12:25 Yeah, here we go. So… I'll show you this.
There's a meeting recordings tab here.
that goes to a spreadsheet, and then you have… it's a big spreadsheet, because it's just all OpenTelemetry meetings. You scroll to the bottom.
Well, actually, the bottom of where things are. You can see all the meetings that have been recorded, and, like.
how many minutes it was? Wow, it looks like somebody… named in the Python sig for a long time, usually that's a sign that there's, like, an AI bot that doesn't leave when everyone else does.
And so it's literally just a Zoom link of an AI bot listening. It's so funny. Anyway, but you can see, like, how many minutes it was, and what time it was, and then that's the link. These only last for a few weeks.
**krajo Krajcsovits** 13:19 Yeah, I definitely want to save this, so I'm going to try to get this. If you put the link to the… Not too.
**Josh Suereth** 13:25 Yeah, yeah, yeah. I'm gonna put a link to… it's OpenTelemetry Community's README, so I'll put a link to this tab with a link to meeting recordings, that's how I always find it.
So, yeah.
Ordings.
It's right there.
Yep.
**krajo Krajcsovits** 13:44 Cool. Thank you so much.
**Josh Suereth** 13:46 Yeah, no problem.
**krajo Krajcsovits** 13:47 Okay, so, yeah, so I guess… Yeah, I had this idea of the discovery grouping.
You covered that, and identifying… what are the resource attributes, what are the identifying resources, what are the restrictive attributes, because you want to kind of separate them. I didn't realize you wanted to… Separate them so much, That they are eventually actually sent in a separate channel.
**Josh Suereth** 14:15 I mean, so we… that's where things get fun, is OpenTelemetry. We're about flexibility.
So yes, we want to make it possible that you can have them completely separate.
Some users may never do that, and they still have to be successful.
**Arve Knudsen** 14:33 On this, I spoke with Dimitri from this SIG Josh, during KubeCon, and, what he told me was that the, the entity event, signal, should not be necessary for Prometheus to ingest. Like, Prometheus should only do with the OTLP metrics, payloads. Like, all the… all the necessary information should come… should come through.
all TLP requests. Does that make sense to you?
**Josh Suereth** 15:10 Yes, yes. I… the way I'd phrase it, though, is Prometheus Doesn't need to.
If you wanted to, like, if you thought you would have better storage characteristics engaging with it as a separate signal, it will be an option for you when it's there.
**Arve Knudsen** 15:28 Okay.
**Josh Suereth** 15:29 You don't, like, it's supposed to be completely an optional thing.
**Arve Knudsen** 15:33 Yeah, yeah, that's a relief, Josh. I kind of just wanted to make sure that Prometheus will not need to ingest this separate signal, if you see what I mean, for asynchronous ingestion of entity changes.
I kind of wanted to kind of verify that all the necessary information comes through OTLP.
**Josh Suereth** 15:56 Yes.
Yeah, and the other thing, like.
the way we're thinking about… or the way I think about it in Prometheus land, you know cube state metrics, how they come in?
Where it's, like, pod node, a name, that kind of thing, and people kind of look at those and maybe join state information sometimes, but they're kind of independently useful.
If you imagine a world where someone's using our events.
for entities, they would show up like cube state metrics do in Prometheus. We would… we actually plan to have an automatic conversion to metrics, state metrics, or info metrics, or whatever you call them.
So that, If you needed to engage with, like, the state aspect of entities, that's what that would look like in Prometheus, so it would be just like how you do CubeState metrics today.
**Arve Knudsen** 16:54 Yeah, I think that makes sense. I mean, I'm not super familiar with cube state matrix myself. I mean, I know about them.
But I, I think I get your idea.
**Josh Suereth** 17:04 Okay.
Cool.
**krajo Krajcsovits** 17:11 Right. I guess on to my second, like, warm-up dumb question. So… Just from UX point of view.
when I have a metric.
It has its attributes, and then the identifying resource attributes pointed out by entities.
And… Is it unexpected that on the UI, Whatever graphic thing you have.
as long as these are the same, these attributes are the same, you get the same line. So it's the same color, I click on it, it's the same thing. So that… it's… it… Both of them together identify the series.
**Josh Suereth** 17:52 Yes. Yeah. I'll give you examples, like, examples for identifying attributes change.
If a process shuts down and restarts.
There's an opportunity for them to change.
They may, they may not.
So, like, I have… I have a pod that gets killed and rebooted, Okay.
Because we actually use pod ID as our identifying attributes, you will get a pod ID, and that will be different, and so that'll be, like, when the pod crashed, that will be one continuous line, and then there'll be a separate line because, you know, you're actually a different ID at that point, if that's what you're tracking.
**krajo Krajcsovits** 18:38 Yeah, but that doesn't have a… okay, so, new line.
**Josh Suereth** 18:41 But again, since I can choose what entities I can place in, I could actually decide not to identify by pod.
Anyway, that… we… I might be confusing you, so I'll stick to, like, generally what people do. So generally, that would be a new time series.
Right. Because of the crash restart. However, let's talk about, and again, I don't have a better example yet, because I don't remember how other things work, like Nomad, but, Java EE systems. Do you remember old school Java EE, or, like.
possibly, like, Apache Tomcat mod things.
**krajo Krajcsovits** 19:23 I never got into Java, I… Word in it a little bit, and then I said, oh, this is not for me.
**Josh Suereth** 19:29 Okay, so the TLDR is there's a single web server that gets started.
That web server can load in a plugin.
That is a web application, okay? These applications can be loaded and dropped dynamically.
What we plan to do for that kind of capability would be the plugin is given an identity.
And when that plugin is loaded, any metric reported on behalf of that plugin Has an identity and will have a time series.
The overall web server, the global thing, will also have its own time series, and be reported independently of, like, the plugin.
Right? Because you'd report where you have the web server as your only piece of identity in resource 1, and then resource 2 I would say this web server and this plugin.
our report.
So that I can actually track, like, within my process, I have something that has a different lifespan.
**krajo Krajcsovits** 20:28 Oh, I see.
**Josh Suereth** 20:29 And I can, like, port its time series independently, but I don't have to, you know, in terms of instrumentation, every piece of instrumentation doesn't have to add, oh, I'm part of this plugin. They just say, here are my metric attributes, and the resources handling those additional things you need to do to know you're a plugin A.
individually.
**krajo Krajcsovits** 20:49 And you mean, when you say plugin A, it's not the instance of the plugin, it's the plugin?
**Josh Suereth** 20:54 No, it'd be the instance of the plugin, because you're.
**krajo Krajcsovits** 20:56 Oh, yes, that's.
**Josh Suereth** 20:57 Yeah, like, the idea would be, I might have, like, a thing that can call Ruby, right? And I might have 12 different instances of calling Ruby, but they're technically different applications of Ruby, right? But the plugin's the same plugin.
So, I need a way to identify the instance, and that's… that's one thing entities would allow.
**krajo Krajcsovits** 21:17 Okay.
I think we are on the same page, but I, you know, it's one of those things that you always have to ask, is it plugged in, is it, you know, into the wall? Just that we are really on the same page. Next question…
**Josh Suereth** 21:32 By the way, if you have, suggestions for how we can update our docs, or what we've written so far, to make it clear, you're not the only one asking these questions, these are kind of commonly asked, it's just we need, like… we're trying to improve our writing to get these things down so people know and kind of get the concept better. So, any suggestions there?
Keep that in the back of your mind.
Okay. Okay, yeah, I…
**krajo Krajcsovits** 21:59 I'll be, like, one of my… not the main project, my side project is, stabilizing the Prometus Side of things. We are kind of done with the… Receiver, but there's a whole lot of backlog items for the spec.
So, Prometu Sotaspec. I started working on it, I got a bunch of things done, but, like, there's so much more. So I'll be working on docs anyway, so that could be… Something I can, contribute to.
Alright, yeah, I'm not even going to copy this, but, like, Metricatsu boots are… always independently identifying. Like, even if the entity says.
these attributes are identifying, and they didn't change. If the metric attributes change, then that's a different metric. Like, that's very…
**Josh Suereth** 22:57 Yeah.
**krajo Krajcsovits** 22:58 Right, okay, yeah, yeah, I, okay, just, okay, then the… So, this might be a tricky question.
I guess maybe I could already deduce it from what you said.
But… So… We talked about the web server and the plugin, but you can have, you know, many entities.
And then, is it, like, in theory possible that someone still expects the same line if one entity changes. I'm thinking of this weird case, possibly, where you… run on a VM, You have a, like.
It used to happen for us in VMware's, Sphere, or whatever it was called.
where they would hibernate a VM and start it up somewhere else.
**Josh Suereth** 23:48 Oh, vMotion, yeah, yeah, yeah.
**krajo Krajcsovits** 23:49 Yeah, VivoShot, yeah, I didn't remember, but in theory, it is possible to kind of have a discontinuity But… Like, I guess it would be incredibly hard, too.
To keep track of that.
**Josh Suereth** 24:04 You know, it's a good question, so, but this is where, like, the way we would deal with this is with the buy syntax in PromQL. Like, basically, if you wanted to have that be a continuous line, you would use BY to get rid of the entity that doesn't matter.
**krajo Krajcsovits** 24:20 Oh, okay, yeah.
So it's… so, yeah.
I see, so…
**Josh Suereth** 24:26 But, yeah, you get what I'm saying.
**krajo Krajcsovits** 24:29 Yeah, I get what you're saying. So basically, you want to keep this clean. If it changes, it changes, and if it means the same thing for somebody, then you have to, like.
make it so, basically. Use the bike. Okay, okay, that's, that's great.
**Josh Suereth** 24:43 If there's a way to easily, like, group by entities, like, I think users will probably want that, but we can actually wait for them to ask for it as we build this, right?
**krajo Krajcsovits** 24:54 Yeah, the… The group buy thing is, is, is tricky, like, the… So for Prometus, it's always tricky when the data model changes, so when you add an entity or do something, you sometimes have to rewrite your queries, or you will not get the same thing, but… I'm not there yet to think about those cases. Like… Maybe the entities will be actually happening in that case, because they are kind of self-describing, in a sense.
unlike the labels in Prometus Fair, you can… you have some name, and you have no idea what it means, basically. Entity gives you a little bit of structure, at least, so…
**Josh Suereth** 25:45 It does, and the other thing is, you know, if it's an entity-based thing, that you're almost always doing a spatial aggregation of some sort.
**krajo Krajcsovits** 25:53 No.
**Josh Suereth** 25:54 Whereas with labels.
some… we abuse the heck out of labels, even internally, like, we abuse them to mean so much. You have no idea what a grouping by a label really means sometimes. You can assume spatial aggregation, but it's not guaranteed.
**krajo Krajcsovits** 26:09 Right.
Okay, so now to the more tricky questions, maybe. So… Okay, yeah.
Let me copy this.
da-da-da-da… So I… oh, crap, this looks like crap.
So… I was, Where did we get this from? Anyway, somebody said that, you know, there's this merge thing in the SDKs when it comes to multiple entities.
And, there's a passage in there where it says that, When you merge an… when you… not even entities, sorry, this is about resource attributes.
So when you merge resource attributes.
The last one that you merge in wins, if there's a conflict on the name.
Right.
So, what's the, like… I guess the question is, like, how do customers react to this? Like, is it… Is it something that's easily explained away, or…
**Josh Suereth** 27:26 That's one of the reasons we're trying to make entities so we have less issues here, but, like, basically, from my experience with customers and resource issues, is it's still a bit of an R. Kennedy.
Where when it doesn't work, they hate it. When it works well.
you don't hear anything, right? Like, you can only get it wrong.
And, you know, when they complain about usability.
half the time, it's actually, like, resource detection's not set up well, so, like, they… their queries are slow because they don't have enough, you know, things fragmented in the data store, that kind of stuff.
So, yeah, right now I would say it's a little bit of people who know, know, and people who don't, don't. What we're trying to do is keep the rules simple. So that rule that you see there around merging.
the way we phrase this to people, and the way we've talked about this, is just the order you list your resource detectors should be important. Today, in the spec, because its last one wins, it means that the order is in inverse priority order. The bottom one is the most important in resource detection.
and the last thing in the list wins the attribute. So, if you have an order that you care about, in terms of detecting where you are.
Make sure the thing that's important is on the bottom.
In the new entity merge algorithm we have, the big open question is, I changed it so that the top is important.
And we have the resource detection in priority order.
Where you would say, cool, it's more important for me to know what the Amazon AWS detector says than it is the generic host detector, because the generic host detector does a whole bunch of shenanigans I don't care about. I want what Amazon says my VM is, or I want what GCP says it is, right?
And so I can put those above the generic host one, and then I know what attributes get chosen.
I… to me, the important thing for users is just to give them that ability of, like.
hey, I want… I wanna know where I'm running.
I have these resource detectors by name of, you know, host, VM, Kubernetes, cloud, right?
And if it's not Kubernetes, it could be things like, we have, I think there's, like, a Heroku detector somewhere, there's some HashiCore things, you know, like, there's… there's… So there's, like, cloud, there's, like, Kubernetes container-y things, like Docker versus Kubernetes, if you're running in, Docker work… what are they called? Docker container.
**krajo Krajcsovits** 30:09 It's warm, or what? No, not.
**Josh Suereth** 30:11 Yeah, like a Swarm, or, you know, I'm running… I'm running containers inside of, like, Microsoft, because I'm, you know, Microsoft Windows is not necessarily Kubernetes friendly, some people do Windows-y things, sure.
Anyway, you get my point, though. There's, like, those layers, and so you pick those, and you put them in the priority order of which one matters, like, which identity is most important to you.
And then things should work from there. That's kind of like the end state of what we want. And then the way the merge specification is phrased is supposed to make that thing be true.
Right, right.
So, it's hard to connect that dot, or those dots.
If you come into it just from the specification, because… the specification's the specification. Rationale and things are all in PR comments and history, and that's where the OTEP directory is supposed to kind of tell you The goals of why the specification's shaped the way it is.
**krajo Krajcsovits** 31:12 Right, right. And when you talk about putting in them in reverse order, you mean in the collector, you list them in?
**Josh Suereth** 31:18 in the collector resources, or in the SDK.
**krajo Krajcsovits** 31:22 Or it is, okay, okay.
**Josh Suereth** 31:23 Yeah.
**krajo Krajcsovits** 31:26 And then, yeah, I guess when reading the spec for the entities, it says then it's the most specific entity That needs to be… Kept, right?
**Josh Suereth** 31:40 Yes.
Like, again, we're talking about flipping the order for entities.
**krajo Krajcsovits** 31:46 Right.
But in your example, you said that you want to, like, the AWS DNS, or whatever.
That needs to be… but that's not most specific, that's most… more… what do you mean by most specific? Is it…
**Josh Suereth** 32:02 That would be, like, a generic host detector versus a AWS host detector. The AWS one would be more specific.
**krajo Krajcsovits** 32:10 Oh, I see, I see what you mean.
**Josh Suereth** 32:11 Right? Because I know I'm on AWS, whereas the host detector has no idea where the host is.
could be anywhere, and so it just tries to look at really general Linux-y things.
And it might not figure out that it's on a cloud at all, for example.
it might… but you can use it on your laptop, you can use it on, you know, your own internal cloud, like, it's usable everywhere, but it's not as specific as, like, the specific AWS, the specific Microsoft thing, you know.
**krajo Krajcsovits** 32:46 Okay, so… Pacific, as in… In my head, more specific was very different. So, more specific, for example, generic host detector versus AWS.
Yeah, I get what you mean by more specific here, I'm just… Like… as far as I understand.
The naming of things is really… is convention, so there's no strict rules, so it could… it is theoretically possible that two entities that are completely independent, and… but… Different things have the same… Point to the same attribute.
**Josh Suereth** 33:44 Whoa.
**krajo Krajcsovits** 33:44 more…
**Josh Suereth** 33:45 Yeah.
**krajo Krajcsovits** 33:46 Specific.
**Josh Suereth** 33:47 I see what you're saying. Yeah, the, This… this has been one of the things that's kind of bogged us down a little bit, of we're… we're getting to the point now where, with entities, this whole cloud availability zone, we think cloud availability zone is actually just really bad, like, kind of poorly designed.
the reality is, cloud availability zone is kind of tied to an entity and should be namespaced as such, at least on GCP. So one of the things that's true on GCP is, the availability zone is specific to, like, the entity type, and you can have more than one.
So, for example, I can be a VM that's on availability zone in EU, but I could be part of an auto-scaling, like, managed instance group that is in NA.
Right. Do I report my availability zone for both of those at the same time? I can't.
If I needed to.
So… What we've gone with, with entities, There is what we allow users to do, which is more flexible.
Because users will do whatever.
We can't really force them to use naming conventions, but within OpenTelemetry, entities will… the attributes will be namespaced by the entity type, so you kind of know that they don't conflict. So kates.pod will have attributes, kates.pod.x, right?
**krajo Krajcsovits** 35:18 Yeah, yeah.
**Josh Suereth** 35:19 Yeah.
**krajo Krajcsovits** 35:19 I… I think, by the way, in general, I've, you know, looking at coming this to the… coming to this pretty fresh.
I feel like… people in the know writing SDKs, writing, like, Kubernetes, or whatever.
We'll do a good job, because they understand namespacing, and trying to not conflict.
But then, when I'm thinking of application developers, that's going to be, like.
it's usually a mess. Like, just look at logging, what people do for logs in applications, then you know it's going to be a mess.
So… Yeah, we'll see how this pans out, but… I've… Maybe this leads into my next question, actually.
Let me write this down. General… Space… names… Okay, so… I was thinking that… Yeah, I had a question which Arva already answered, but I put it in here as well, that… venue… Yeah, so when you merge attributes and you have entities, then obviously you need to make sure that The entity points to the… Like, the right entity points to the… Resource attribute that got merged.
like… If there's a conflict of resource attributes.
You keep only one of the two that conflicted, and the entity like… If two entities point to it, then only one of them can point to it, because it's… it can be… Otherwise, a conflict.
**Josh Suereth** 37:17 Yes.
**krajo Krajcsovits** 37:18 Like, for example, one attribute is a string, the other is an int, then it doesn't make, you know, much sense to point to an int from something that expects a string.
**Josh Suereth** 37:27 That's true. Yes. Yeah, yeah. The other thing that we're doing, which is kind of, like, weird shenanigans, is we're putting all the attributes in resource to be backwards compatible.
**krajo Krajcsovits** 37:36 Yeah.
**Josh Suereth** 37:37 So, you literally can't… like, you physically can't do that in OTLP.
You can't have one key have both an int and a string.
**krajo Krajcsovits** 37:46 Yeah, yeah, yeah, yeah, yeah, that's… yeah, the, the, the… kind of the… Yeah, we talked about the… Yeah, I guess… I guess our issue is… Again, coming back to this You know, conflict and losing an attribute.
We talked about this, that… We basically have to explain to the user to… Use the right order of things.
But… Would it be too late to either, like, prohibit conflicts, or to make sure that you keep the attribute that you lose in some way?
**Josh Suereth** 38:32 Oh, shit.
**krajo Krajcsovits** 38:33 signal?
**Josh Suereth** 38:34 Yeah, so we… we're kind of doing both. You can see the comments on the PR, but basically, there's a to-do to add to the protocol. We're gonna have a dropped attributes count.
Somewhere.
I need to figure out where, but it'll tell you how often those conflicts happened.
So we can actually record that there was a conflict that occurred, and then you can flag to the user and say, hey, you have an issue with your entities, like, you know, some of them are conflicting.
the plan when the SDK and the collector are implemented, that will be, like, an error log that shows up that says, hey, you have a conflict in your entity definitions, so you can actually see it. It would actually be, like, a kind of a first-class thing. And then we are planning to prevent them from making it into OTLP.
So you as a downstream database, like, won't have a conflict, because we have resolved it ahead of time.
But we will flag to you and let you know that there was a conflict that was resolved, so you can still tell the user, your data might not have what you wanted in it, because you have an issue.
In reality, what we expect to happen is, you know, for the most part, open telemetry instrumentation will do the right thing, and probably work well together, and will fix all those conflicts.
And then, when people customize, like you said, like, it becomes Wild West, this is our way of at least letting you know there's an issue, and preventing the worst defenders from making it through.
It's still possible that some wonkiness gets through, that we're trying to… like, we're trying to do our best to make this be a very flexible, yet very, easy-to-depend-on data model.
And it's really hard to get flexibility and easy to depend on.
at the same time. Like, those are almost completely at odds with each other, you know what I mean?
**krajo Krajcsovits** 40:25 Yep.
Yeah, I think for us, since we are… You know.
Obviously, Promatus and Grafana Mimir has some implementation of resource attributes.
It has been a little bit rocky road, like, there's some issues, obviously, but it's natural, you know, it's a new thing.
We have to, like… Yeah, we have to see… if this is, enough to have this count of the tributes. I mean, I like the fact that we can actually at least tell the customer that something is wrong, and when we get a support ticket, hey, my thing is missing, and we can take a look at the count, we can have an idea of what went wrong. Because without that, we are Blind, completely, like… Or maybe… well, I guess not… Are we buying completely? Like… If the entity… Like, model or description or whatever is public, we can take a look and find the conflict ourselves.
But if it's not public, then what would we see in the OTRP payload? We would see… An entity that points to an attribute.
And the other entity that conflicted, I guess, wouldn't have that attribute, so we would see nothing, right? We would… without this count, we would see nothing from this conflict.
**Josh Suereth** 41:57 Right now, yeah. I mean, sorry, like, with things as they're implemented today, which again, we're not fully implemented, yes, but before we would, like, stabilize and launch, you would… you would have that in there.
I mean, the reality is, though, you… one of them, when you would see the entity, one of them, you wouldn't see the entity.
So, if you have… If you're trying to join two time series.
Right? If someone writes a query that's supposed to hit two separate things, one of them has an entity and one of them doesn't. That is something you would know when you get the query results.
**krajo Krajcsovits** 42:35 Yep.
Or you would get bogus results if they are both string and mean something different, but yeah.
**Josh Suereth** 42:45 Absolutely.
**krajo Krajcsovits** 42:45 It's probably the worst case, but…
**Josh Suereth** 42:47 Yeah, yeah, yeah, yeah, that's true, fair, yeah.
**krajo Krajcsovits** 42:50 ew.
Boom.
**Josh Suereth** 43:03 Okay. I do need to drop in about 2 minutes, apologies.
**krajo Krajcsovits** 43:08 Okay, I think just one thing that I wanted to reiterate, and I'm not taking more than time, is that The event mod… event model, yeah, let me… shit, let me copy-paste it. So… We don't really… believe in that, so I don't really have a… Incentive to… to implant it, really.
Aww.
Because… It… it's an asynchronous, data transfer.
And we have one rule of thumb in all of our databases, which is either we return the correct result or nothing at all.
And which means… and we ran into this so many times, that there was issues with out of order, with deduplication and redundancy, and blah blah blah.
And you wouldn't believe how minute are, like, small things customers notice.
**Josh Suereth** 44:05 No, I…
**krajo Krajcsovits** 44:05 would…
**Josh Suereth** 44:06 Yeah.
**krajo Krajcsovits** 44:07 You know, so they would notice if you… if we change the result of some queries between two times, like, between one minute, because we get the information late. So that's… that's very… I mean…
**Josh Suereth** 44:21 So, so, here's, here's the thing.
I hear what you're saying, but I also think you probably want to… you might want to relax that a little bit, and here's why.
I would not allow… Alerts and, like, auto-scaling control loopy things that have high turnaround interact with anything that comes on a side channel for the reason you mentioned.
If I need to detect something within, like, a millisecond, and something is asynchronous, it's gonna be disjoint, it's gonna be out of state, it's gonna be out of scope. I need that in my main channel, because I can't wait for the join to happen.
that's too late, that's too slow, that's not good, right?
So, if I'm writing an alert.
and I have any kind of, like, fast turnaround that I need for the signal detection to occur.
this is problematic, because data's gonna, like, I'm gonna get metric points that don't have the, you know, name associated with it or something, whatever, whatever's on the entity signal.
So, I should actually not let you do that query, to some extent, if you're on a high-performance alerting thing.
Right. That said.
The use cases where these are important are… might be, like, analytical, or might be on a different timeline or different time horizon, but they still might be important.
You know, being able to, like, navigate through your data.
you can't… there's… it's almost like, if you've dealt with AI, the context window.
You can't shove everything into the time series over time that you need sometimes for some of the joins you want to do.
You know, so… Anything you need for HotPath, absolutely agree, should be right there, ready to use very, very quickly. But not all query use cases are HotPath query use cases. And if you make that clear to people.
you're okay, to some extent, but for context, at Google, we have these things called metadata metrics. If you look at Google Cloud Metrics, you'll see metrics have, like, additional labels that are attached to them that have a different lifespan, a different lifetime, because they come in an asynchronous channel.
And they are awkward as hell at times. So, for context, your VM name can change over time.
When we record a metric on your behalf, we record it with the VMID, and then we attach the name later, because the name can change.
And so when you write queries based on VM name, that name can change.
Over time. And this does, you're right, confuse people, but when… if you get… if you get a system where you're kind of advertising to people when that happens and why.
And, like, how to write high performance?
Alerts and metrics, and how to make sure the right data is in the hot path.
And the data you need for, like, dashboards or visualizations that occur on an analytics basis are in the other path.
I think you can still be successful.
So, I agree with you that it's a huge problem, and it's something people need to be aware of.
And I agree with you that the default should be, for any… for most critical things, that they're in the hot path, and that they're joined, right? Again, the whole idea of entities is this optional path to allow all of these additional use cases that we know people need.
But we're… we are not targeting the use case you just mentioned of, like, a fast alert. That is… that's the optical word. If you need a fast alert that's tagged with some piece of information, you need that join to happen early, and you need to make sure it's on the resource. Because otherwise, it's really hard to get that data to the downstream systems timely.
You know, and fast. Does that… does that help answer?
**krajo Krajcsovits** 48:04 Yeah, it… Again, this was, this is a pretty hard rule for us, so we have to… we have to discuss this. Unfortunately, we actually have an off-site coming up.
Where are there, and… myself will talk about OpenTeametry, what we had in the past, and what we are working on inside the company, and… I guess that would be a nice place to discuss this, because it is… it would be a pretty big… shift in, in, in, in mindset.
**Josh Suereth** 48:40 Yeah, and I hear you that, like, again, it's completely optional. You don't need to engage with this. I think what that means in practice is there'll be a set of data that you never get, and that's probably fine, because you're probably not getting it today, so it doesn't matter if you don't get it, you know what I mean?
**krajo Krajcsovits** 48:56 Yeah, as long as a huge company comes along and puts, you know, a big bag of money, so I think you have to think about it, but it's not super urgent, obviously, but, you know, you have to think about this early enough so you don't get caught with your pants down, basically.
**Josh Suereth** 49:10 Yeah, I hear you, I hear you. Okay. I do need to drop, and this was a great discussion. If you need… if you have any more questions or want to come back and kind of talk through things, happy, happy to do that next week, actually.
**krajo Krajcsovits** 49:20 Yeah, yeah, I plan to be here more, for sure.
**Josh Suereth** 49:23 Okay.
**krajo Krajcsovits** 49:24 Thank you so much.
**Josh Suereth** 49:25 Art… not art… art fell…
**Arve Knudsen** 49:28 Or vet.
**Josh Suereth** 49:29 No, no.
**Arve Knudsen** 49:30 Okay.
**Josh Suereth** 49:30 I always, I always miss… I was trying to fix it, but I accidentally clicked on your name.
**Arve Knudsen** 49:36 Yeah, thank you, Josh.
**Josh Suereth** 49:38 Thank you, everybody.
**Arve Knudsen** 49:40 Thanks for the chat. Have a great day.
**Josh Suereth** 49:42 Me too.
**Arve Knudsen** 49:42 And by the way…
