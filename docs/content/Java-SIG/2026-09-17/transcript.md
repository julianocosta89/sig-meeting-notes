SIG: Java SIG
Date: 2026-09-17
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

BRUNO Baptista 00:01:16 Hello.
Jason Plumb 00:01:19 Hey, BRUNO.
John Watson 00:01:29 Hey, Mr. Plumb…
Jason Plumb 00:01:31 Hey, you missed a pretty sweet CNCF meetup yesterday.
John Watson 00:01:35 How'd that go?
Jason Plumb 00:01:36 It was fun.
That's fine.
John Watson 00:01:41 Pretty low-key.
We need to do a Portland hotel lunch.
Jason Plumb 00:01:46 We do, we talked about it a little bit last night, like, we're due for one, yeah.
Trask Stalnaker (Microsoft Corporation) 00:01:52 For the reins.
Jason Plumb 00:01:55 Yeah.
I was saying, I went to that meet… the CNCF meetup yesterday.
Trask Stalnaker (Microsoft Corporation) 00:01:59 Oh, cool.
Jason Plumb 00:02:00 Yeah, because it was actually in Portland this time, and not in Beaverton or Milwaukee.
Trask Stalnaker (Microsoft Corporation) 00:02:21 Was it, was it Kubern… like, CNCF, a particular project in CNCF, or…
Jason Plumb 00:02:29 No, they're doing… they're doing CNCF meetups, and they rotate through speakers and stuff, so, Reece gave a talk on OTTL, and someone whose name I'm derping on, gave a talk on… like, kind of how to commit to FluentBit using AI?
That's kind of, like, the… those are kind of the topics.
Trask Stalnaker (Microsoft Corporation) 00:02:51 That's cool. I missed… Yeah, I saw the… Slack message, but I think I missed what the context was.
Jason Plumb 00:03:07 Yeah, they're doing them every, kind of, 2 months, because there's not strong organizational leadership right now. They're looking for help, like, every open source thing ever.
Trask Stalnaker (Microsoft Corporation) 00:03:18 Is it put on by, like, the CNCF ambassadors?
Jason Plumb 00:03:22 It is, yeah.
Trask Stalnaker (Microsoft Corporation) 00:03:24 Nice, nice.
Jason Plumb 00:03:28 In this case, I think it's Jonas, I think is the person.
Trask Stalnaker (Microsoft Corporation) 00:03:42 Alright… V3… Death, so… thinking the release will go out, the last 2X release will go out next week, but I know, Lori's… Out, this week.
So, may take us a bit longer to get through some of those PRs, so… Don't hold me to any release date, please.
Other than that, any questions about the V3 stuff? Any, anything anybody wants.
To discuss or highlight?
Alright, well, let's move on.
Gregor Zeitlinger 00:04:55 How are you?
Trask Stalnaker (Microsoft Corporation) 00:04:56 Oh, yeah.
Gregor Zeitlinger 00:04:57 There was one issue, in contrab.
That I'm discussing with, Jack Shirazi, but he's not on the call. It is related to, declarative configuration and the bridge there.
Jack is also on the call, and we also discussed it. Jack, do you think it makes sense to discuss this here?
Jack Berg (Raintank, Inc. – Grafana Labs) 00:05:33 I think we can discuss it at, like, a high level, and we can… we can decide whether, we have the people here to… to… to go deeper into the details.
Gregor Zeitlinger 00:05:46 That's a good idea. Let's do that.
Jack Berg (Raintank, Inc. – Grafana Labs) 00:05:51 Do you want to kick us off?
Gregor Zeitlinger 00:05:52 Yeah, sure, but I'm still, gonna just find, The point request number, because some people probably want to see what number it was.
So just give me a second, Yeah, okay, there it is. I'll just put it…
Trask Stalnaker (Microsoft Corporation) 00:06:22 This one, probably.
Gregor Zeitlinger 00:06:25 I'm not looking at… Yeah, exactly, dynamic control, that's… that's the one.
So, this was triggered, because we, deprecated one, Bridge, Declarative Config Bridge Builder, this one, and it's scheduled for, removal in 3.0. And while I was working on that, I, discovered independently That, declarative config is not used as it should, because, In this use case, you can have a YAML file and also read system properties.
from what I saw, this was not, done to violate declarative configuration, but nevertheless, it does. And so… We, have to decide whether we want to, fix that, Together with the technical thing of changing the bridge, or whether we want to accept this inconsistency.
And, clean it up later. This inconsistency is also, kind of useful here, because if you re… if you get rid of the inconsistency, then you have to specify some things twice, namely the service name. You have to put it inside the YAML file, and you also have to give it to the op amp, because it needs it for identifying itself.
If I understand this correctly.
Jack Berg (Raintank, Inc. – Grafana Labs) 00:08:22 So… Do we… given Sylvain's message about Jack joining the call later, should we… should we just postpone this?
Gregor Zeitlinger 00:08:31 Yeah, if he joins later, then it's probably a good idea to do it later.
Trask Stalnaker (Microsoft Corporation) 00:08:38 Cool, yeah, just throw it at the… on the agenda.
So, moving on… Jason.
Jason Plumb 00:08:51 Yeah, so this, came up in Android, a couple of weeks ago. It was discovered that, We have a couple of HTTP instrumentations that are based on… the upstream Java instrumentation implementations, and… When… when they get created, there's a… there's kind of an understated SPI that happens, that causes the service loader to walk the class path looking for customizers, right? So… You can customize these instrumentations, and…
Trask Stalnaker (Microsoft Corporation) 00:09:26 Can you explain what you mean by walk the class path?
Jason Plumb 00:09:29 Well, service loader.
Yeah, sorry, it's just service letter.
Trask Stalnaker (Microsoft Corporation) 00:09:34 Yeah, like, that's not, like, scanning, that's just, like, look up this resource, get this name, look up this class.
Jason Plumb 00:09:43 It's like, you know, Git implementers, right? It's like the service-letter thing.
Trask Stalnaker (Microsoft Corporation) 00:09:48 Yeah.
Jason Plumb 00:09:49 Yeah, sorry, I'm probably overstating it when I say walk the class path.
You're right to call that out, I'm not… it's not… it's not fair to say it's walking the class path. Okay. But it does enough, looking at.
Trask Stalnaker (Microsoft Corporation) 00:10:01 There's a couple of discrete.
Jason Plumb 00:10:03 It does, and so that makes some people get twitchy on Android when they have this strict mode turned on. We have a policy that we wrote in Android that says we're not super hyper-fixated on strict mode, and that we will always have some amount of violations, but… In this one particular case, they saw, like, an 80 millisecond bump, and, you know, that's not great for startup time, it's, like, not the end of the world, but it's not great, and some application users are sensitive to this kind of stuff, so… The question is, what can we do about it? There's no real API right now to inhibit customization, and I think that's what's ultimately being asked for.
Lori has responded on this issue, and he's not here today, so maybe… maybe there's not a lot of traction to be gained on this right now.
But if anybody else had seen this or thought about this kind of same thing.
It would be a cool thing to…
Trask Stalnaker (Microsoft Corporation) 00:10:57 How is this not a problem for the SDK? I mean, the SDK does SPI…
Jason Plumb 00:11:06 We don't use auto-configure.
Trask Stalnaker (Microsoft Corporation) 00:11:09 Mmm…
Jason Plumb 00:11:10 That's where all the service stuff happens.
I, I would think.
Jack Berg (Raintank, Inc. – Grafana Labs) 00:11:17 Not all of it, not all of it.
Jason Plumb 00:11:20 There's some other stuff.
Jack Berg (Raintank, Inc. – Grafana Labs) 00:11:21 contact storage provider.
Jason Plumb 00:11:23 Yeah, we had a workaround for that. We had to put a workaround in for storage.
Jack Berg (Raintank, Inc. – Grafana Labs) 00:11:28 And the OTLP senders, those use SPI as well?
Jason Plumb 00:11:34 Okay.
I hadn't heard of that one coming up yet, but I believe you.
Jack Berg (Raintank, Inc. – Grafana Labs) 00:11:39 No, it… the… They're there. That's how we determine… we check what's available and some other system properties to resolve which sender to use, but you're right that the majority of them is in auto-configuration.
Trask Stalnaker (Microsoft Corporation) 00:12:00 Do I remember that we had… issue in the core repo before, or maybe in this repo, I forget, and… We did some build time… workaround…
Jason Plumb 00:12:20 That's interesting.
Jack Berg (Raintank, Inc. – Grafana Labs) 00:12:22 Build time workaround to what?
Jog my memory.
Trask Stalnaker (Microsoft Corporation) 00:12:26 the SPI, like… Laurie, I think Lori did it, probably, so, he would remember.
the… I thought we did something… somewhere… We're at build time in the class… we actually generate a class file, that has… the SPI stuff… So that… or this lookup thing, so that… Don't have to… it's just a normal class file, then it's not a resource read.
Maybe? Because that seems to be the problem.
Jack Berg (Raintank, Inc. – Grafana Labs) 00:13:07 I don't remember that specific thing, but we… what you reminded me of is that, we have an abstraction on top of SPI loading called Component Loader, and it's just, like, a very small interface that it has basically the same API as SPI does for, like, loading A particular interface and implementations of it, but… It's our own, it's Component Loader, and you can provide your own implementations of that that, you know, have different mechanisms for loading that thing.
And so everywhere within the core repo, that is how we load SPIs. It's not through… like, the default implementation of this component loader is the SPI thing, but you can bring your own. And the place that brings their own is the Spring Boot starter.
That brings its own component loader that, like, hooks into, Spring's, auto-wired stuff.
Trask Stalnaker (Microsoft Corporation) 00:14:04 And you don't bring your own component loader via SPI?
Jack Berg (Raintank, Inc. – Grafana Labs) 00:14:08 I don't think so. No, no, no. That's, thank you.
Jason Plumb 00:14:12 Boros right there.
Yeah, I think… I mean, my instinct is that there's probably some room to improve the API here, to allow us to turn this off somehow, or something? I just don't have a good sense of what it might look like yet, because I haven't started packing on it.
Jack Berg (Raintank, Inc. – Grafana Labs) 00:14:31 Well, I can tell you what we do for our component loader. So, like, The way that we make this configurable on places like our OTLP exporter, which needs to load SPIs, is all of our OTLP exporter builders have an optional setter for you to set your own component loader.
Jason Plumb 00:14:49 Yeah.
Jack Berg (Raintank, Inc. – Grafana Labs) 00:14:50 And if you don't set one, then the SPI mechanism will be used, but if you do set one, we'll load the sender using whichever component loader you specify. So, Instrumenter Builder could expose a similar setter.
Jason Plumb 00:15:03 Yeah, exactly. Okay, that sounds like a reasonable first approach.
Trask Stalnaker (Microsoft Corporation) 00:15:09 I like that.
Also, like, I would prefer not, like, having a setting to disable as much as either the set the component loader And, or, look at, generating… the… oh, but this is… we actually do want this via SPI, because of… this is for… distro… I think this is for distros to bring… Some… their own stuff.
So that does need to be SPI. But yeah, you wouldn't care about that in, Android.
So, set component loader.
Jason Plumb 00:15:57 Yeah. So, I mean, your point, though, being don't make it specific, make it broader, kind of more gen… like, attack it at the more generic level than making it pinpoint.
Trask Stalnaker (Microsoft Corporation) 00:16:09 Follow the pattern, I guess, in this case.
Jason Plumb 00:16:12 I mean, that component letter's also a very big hammer.
But it's great, I mean, it would allow us to do this.
Trask Stalnaker (Microsoft Corporation) 00:16:20 Yeah.
Jason Plumb 00:16:21 Cool. I don't think we need to belabor that much longer, I think that's a good first start.
Thank you.
Trask Stalnaker (Microsoft Corporation) 00:16:35 Alright, jack.
Jack Berg (Raintank, Inc. – Grafana Labs) 00:16:39 Yeah, so, I opened this PR the other day, and… I think it just warrants a quick explanation, because it seems like a weird thing to do on its surface.
Right now, periodic metric reader.
which is the metric analog to the batch span processor, batch log record processor, it uses a different mechanism to export on a cadence. You know, it exports metrics every 60 seconds, right? And the… what it does is it has a, A scheduled executor, and it, you know, at initialization time, it says, hey, schedule… this task, or this task is, like, exporting, every 60 seconds, or whatever your interval is. And then we just rely on the scheduler to invoke that, that method every 60 seconds.
And, this… This gets really problematic if you want to… if you want your… your… the mechanics of what's happening in that exporter to get more complicated, like is being proposed by adding an export timeout configuration parameter.
And in particular, we have this export timeout parameter, and we also had this new feature that was added a little bit ago, where you can break metric exports into batches. There's now, like, a max batch size, so you can say, like, hey, if you have 10,000 metrics, I want to export them in batches of 100.
And then that'll be, whatever, like 100 batches.
And, you know, now all of a sudden, you… it becomes more important to have a, like, a timeout on each one of those individual batches that compose this, like, broader export.
So…
Trask Stalnaker (Microsoft Corporation) 00:18:27 Can you help me just quickly? Why is set X… why is the timeout on the… The batching, the periodic metric reader, and not on the exporter.
Jack Berg (Raintank, Inc. – Grafana Labs) 00:18:41 there is a timeout on the exporter as well, and so these two things interact, and that's kind of always been the case. Like, batch fan processor and batch log processor similarly have, like.
a max export timeout field, and then the exporter themselves that they're calling has a max timeout as well. And so, like, you actually need to… you need to tune these correctly to not have, like, nonsensical behavior.
Trask Stalnaker (Microsoft Corporation) 00:19:07 What… what does the… the… oh, it is exporter timeout, okay.
Okay, that is confusing. So, it measures it as a… as a collar?
the timeout?
Jack Berg (Raintank, Inc. – Grafana Labs) 00:19:20 Yeah.
Yeah, it's like the max amount of time it's gonna.
Trask Stalnaker (Microsoft Corporation) 00:19:24 Oh, that it awaits for an AC.
Jack Berg (Raintank, Inc. – Grafana Labs) 00:19:25 rates.
Yeah, right. It'll, like, sort of block its next activities for however long you configure it to do.
Trask Stalnaker (Microsoft Corporation) 00:19:33 Okay.
Jack Berg (Raintank, Inc. – Grafana Labs) 00:19:35 Yeah, and the thing that makes it even, like, confusing…
Trask Stalnaker (Microsoft Corporation) 00:19:37 But I don't want on the batch spam processor.
I want it to… I don't want it to block, I want it to move on.
Jack Berg (Raintank, Inc. – Grafana Labs) 00:19:46 Right, right, yeah.
Trask Stalnaker (Microsoft Corporation) 00:19:48 Fair enough.
Jack Berg (Raintank, Inc. – Grafana Labs) 00:19:48 And I still… and I'm, like, in agreement with you on that. I wasn't always, I guess, but… no.
Okay.
Trask Stalnaker (Microsoft Corporation) 00:19:59 Sorry I derailed this.
Jack Berg (Raintank, Inc. – Grafana Labs) 00:20:00 Yeah, so anyways, this is a refactor of the periodic metric reader to match the batch span processor and batch log record sort of structure. And the way that those work is they have a worker thread.
So, a dedicated worker thread, which is going to, like, wait for some activity to happen. In the case of batch span processor, it's like, hey.
Did we… did our queue fill up, or did a certain amount of time pass? And either of those is the signal to export.
And so, the same thing as of this PR is true for metrics. It's like, there's a dedicated worker thread that's waiting for a signal to export.
And, and because you have, like, this dedicated thread, it becomes, like, the code to apply export-level timeouts becomes, like, dramatically simpler.
And I guess it's hard to sort of describe that in words as much as, like, going to observe the code. Like, the code gets really hard to wrap your head around if you try to have Export-level timeouts with the current pattern.
But, Yeah, so, you know, the… what… what provides the signal that this worker thread should… should export? And, you know, there's a… there's a small scheduler that is just, instead of, you know, scheduling a task.
to, you know, do an export on your 60-second cadence. All it's going to do on that 60-second cadence is submit the signal to this worker thread.
And, so it gets much smaller in scope, but, Yeah, there's still a scheduler involved.
And yeah, so I guess that's the explanation for why this exists. I'm not particularly passionate about this, like, I just saw the proposal for how we fix export… how we add export timeout, like, spiraling into something that I refuse to maintain. And so, like, if we want to add export timeout.
And I think we should, because that's what we kind of need to do in order to have this metric batch feature, where, you know, exports are decomposed into batches.
Then we gotta, we gotta restructure.
So,
Trask Stalnaker (Microsoft Corporation) 00:22:19 So, I… Yeah, so why… I'm not quite sure I followed yet why we need the export timeout setting at the periodic metric reader level.
In my head, what I… like, the periodic metric reader would… just… kind of similar to how I would like the batch span processor to work.
It just… Fire, like, every 60 seconds, it… Fires off the exports.
And… Maybe it batches them up first and sends them But I'm not sure why… I'm not clear yet why we need to wait.
Why we need any kind of waiting or blocking at that point.
Jack Berg (Raintank, Inc. – Grafana Labs) 00:23:14 I'm gonna try and type it out in the… in the notes file, because… and just maybe we can, like, kind of come to… Do you want to share?
Trask Stalnaker (Microsoft Corporation) 00:23:21 Do you want to share?
Jack Berg (Raintank, Inc. – Grafana Labs) 00:23:22 No, I mean, you can see my text as I write. So, like, imagine we have… it's the consider bullet point. So, imagine we have 10,000 metrics, and we have a batch configuration of 1,000. So, every time, we have a collection, which is, you know, every 60 seconds.
We have 10 exports.
1,000 metrics each.
And, you know, these 10 exports are, are sequential. That's, like, what the spec says that they're to do.
And, they need to… They… if we have… if we have no timeout today, like, which is what we have today, then… the… Those 10 batches can sort of block the next collect and export, like, in perpetuity.
Trask Stalnaker (Microsoft Corporation) 00:24:29 Why, so yeah, so this is, I think, the crux of my question.
Sequential, in the sense of the batch… say, batch span processor today, it is sequential in that it blocks for, not only the call to the exporter returns an async.
completable future. But then we block on that future until the… it actually comes back from… returns from the server.
Jack Berg (Raintank, Inc. – Grafana Labs) 00:25:03 Yeah, so, so, export, one, blocks, and, Export 2 until, export 1.
A completable future resolves success.
Trask Stalnaker (Microsoft Corporation) 00:25:19 Yeah, so this is my… I have the same objection I have for batch band processor here, which is, why do we block on the completable future?
Jack Berg (Raintank, Inc. – Grafana Labs) 00:25:35 So, why do we block on the completable future? Like, the simple short answer is because the spec says to.
Trask Stalnaker (Microsoft Corporation) 00:25:43 But I thought we decided on that batspan processor case, that… the spec doesn't actually… there was… there was disagreement on what the spec says, but I thought the… Newer consensus was that that's the… Concurrency only applies to the actual function call, not necessarily that it means it has to block on an async future.
Jack Berg (Raintank, Inc. – Grafana Labs) 00:26:11 Right, but, like, I think what we also decided in that new consensus was that we need a sort of back pressure mechanism of some kind.
And we don't have that for spans, or metrics, or logs, so if there's some way for an exporter to communicate that it has capacity for, like, another concurrent call.
then, like, then I… and that's what I'm advocating.
Trask Stalnaker (Microsoft Corporation) 00:26:37 But that could be… I mean, that can be handled today already by the exporter, which, instead of returning a completable future, it can block the return. It can just not even return anything. It can block as long as it wants there.
Jack Berg (Raintank, Inc. – Grafana Labs) 00:26:54 Right, it can, but, like, I don't think that it's expected to.
And so I kind of worry about that, like, if we're adding this new expectation to exporters, like, you know, we just snap our fingers and say, you know, now you need to, you know, signal back to us by synchronously blocking your export call.
Trask Stalnaker (Microsoft Corporation) 00:27:15 Okay, okay, I'm a… I think I'm caught up here. So, this is basically carrying over the… The old world, the… yeah, because we're not quite ready to go to the new world yet, because there's some… Complications still that need to be ironed out there.
John Watson 00:27:35 I mean, in my head.
this… we need… we kind of… I mean, obviously I'm not involved in the spec anymore, but we kind of need both these things because anyone can bring their own processor, and anyone can bring their own exporter, and we need to be able to make sure that, depending on I mean, we're not in control of both of those things. In fact, sometimes we're in control of neither of them. That there is some sort of contract between those two things that will ensure that we won't be stopping things from functioning.
In general. So that's kind of the way I think about it. It's like, yes, it's belt and suspenders, but unfortunately, we can't control the belt or the suspenders, and so we just need to make sure we have a contract so that the belt and suspenders can work together.
Jack Berg (Raintank, Inc. – Grafana Labs) 00:28:19 So that, yeah, like, that's how I rationalize in my head the… this, like, weird… this idiosyncrasy that there's two export timeouts, like, one at the processor, one at the exporter level, but I think it's independent of Trask's point.
Trask Stalnaker (Microsoft Corporation) 00:28:33 But, John, what I'm saying is not… And so this is not what I'm saying by no timeout, right? What I'm saying is don't block.
If we don't block on… the… What do we call it?
completable…
John Watson 00:28:50 By what is we, who is we? What is we…
Trask Stalnaker (Microsoft Corporation) 00:28:53 Am… PMR slash batch fan processor.
John Watson 00:28:59 Okay.
Trask Stalnaker (Microsoft Corporation) 00:29:01 Don't block on the… Completable result, what is it?
Jack Berg (Raintank, Inc. – Grafana Labs) 00:29:06 Code, completable result code.
John Watson 00:29:08 I mean, it's essentially complete with the future, but our own…
Trask Stalnaker (Microsoft Corporation) 00:29:10 Yeah, we'll just say.
John Watson 00:29:13 Yep.
Trask Stalnaker (Microsoft Corporation) 00:29:17 If we don't block on that, then… My take is that then… We're… even if, Even if it's a bad exporter.
Right? We're not blocking. We're not… we're not in that bad state.
John Watson 00:29:38 But we are potentially spawning an infinite number of threads.
To do that, to do that background work.
Trask Stalnaker (Microsoft Corporation) 00:29:47 Yes, yes, without the back pressure situation that…
John Watson 00:29:51 It gets rid of the back pressure if we don't have that.
Trask Stalnaker (Microsoft Corporation) 00:29:54 I… okay, okay, that's fair, so…
John Watson 00:29:57 So, yes, it's very… it's a lot of… and it seems overcomplicated, I totally, 100% agree, but there… I think there are reasons for every piece that's in there, whether they're always needed, maybe not, but… I don't know, I think when the spec was originally built, it was like, we're going to try to be as safe as possible here, and that does mean we need to build back pressure into the contracts.
Jack Berg (Raintank, Inc. – Grafana Labs) 00:30:20 I wonder if we can just do that back pressure mechanism that we talked about, Trask, like, sort of, like, independently of the spec doing anything at this point. Like, extend the exporter interfaces to have some sort of signaling device that, that processors can key off, or that callers… Yeah, max concurrent, or… I don't know exactly what it would look like. Maybe, maybe, maybe it's like an opt-in feature where you tell us if your export method will, in fact, block, when… when it's, like, reached its… its concurrency limit.
Like,
Trask Stalnaker (Microsoft Corporation) 00:30:51 Oh, Hawaii.
Jack Berg (Raintank, Inc. – Grafana Labs) 00:30:51 like that.
Trask Stalnaker (Microsoft Corporation) 00:30:52 Right. I was thinking max concurrent being on the exporter itself.
Jack Berg (Raintank, Inc. – Grafana Labs) 00:30:56 Yeah, no, that could work too, and then the caller has to track how many are in flight, so I don't know what's better.
They're just different.
Trask Stalnaker (Microsoft Corporation) 00:31:05 Oh, no, as if you put the max concurrent on the exporter, then the exporter would then start blocking if it has… it would keep track of how many it has in flight, and it would block then if it has Too many.
Jack Berg (Raintank, Inc. – Grafana Labs) 00:31:21 Yeah, and I guess that the.
Trask Stalnaker (Microsoft Corporation) 00:31:22 have to.
Jack Berg (Raintank, Inc. – Grafana Labs) 00:31:23 The point I'm making, though, is that the caller needs to know if the exporter's smart enough to do that.
Trask Stalnaker (Microsoft Corporation) 00:31:30 Yeah, yeah, yeah.
Jack Berg (Raintank, Inc. – Grafana Labs) 00:31:31 Yeah.
But, like, what do you… just backing up a step, what do you think, like, based on your understanding of, like, the spec at this moment, do you think that, like, we… we could, in Java, just go and build that without any further clarification at the spec? Like, I kind of think yes.
I think there's other languages that are taking the interpretation that you wanted us to take originally, and so there's, like, precedent for it, so, like, what are we waiting for?
Trask Stalnaker (Microsoft Corporation) 00:32:03 I agree.
Jack Berg (Raintank, Inc. – Grafana Labs) 00:32:09 Okay, so, like, wrapping this up, you know, even besides the points you're making, Trask, I think there is some benefit of having metrics logs and spans, they're sort of the main processor that calls exporters having more similarity. You know, and this refactor makes them more structurally similar. Before this, and currently, you know, metrics is sort of like an oddball.
I think maybe you could even extract an abstract class, an abstract parent class of all three, but I'm not gonna do that. But you could.
Trask Stalnaker (Microsoft Corporation) 00:32:57 Makes sense to me.
Jack Berg (Raintank, Inc. – Grafana Labs) 00:33:01 Alright, I cede the floor.
Trask Stalnaker (Microsoft Corporation) 00:33:07 Cool. Then let's move on. Jonathan.
Hey!
Jonathan Halliday (IBM) 00:33:12 Hopefully this is a quick one. Recall that there's, this OTEP for… being able to expose thread context to external observers. So this is great for the BPF profiler, which would quite like to know which trace ID is active on the thread when it samples that thread.
The OTEP requires, an ELF symbol, and the JVM doesn't have this.
So, implementing this, seems to me to require shipping some .so file that defines the L symbol.
I assume, but I want to get it on record as a decision from the maintainers, that this is a non-starter. There just doesn't seem to be the bandwidth to… mess about with doing native builds and shipping .so files as part of the SDK. Is that correct?
Jack Berg (Raintank, Inc. – Grafana Labs) 00:34:09 That's my position, because that propagates to the agent as well, like, anything that is…
Jonathan Halliday (IBM) 00:34:15 Yeah, so… Architecture specific.
Jack Berg (Raintank, Inc. – Grafana Labs) 00:34:16 gas to propagate.
Jonathan Halliday (IBM) 00:34:18 What's… what's the view on contrib, if I was to implement this OTEP?
could something that built a native file live in Contrib, or shall I just put this on my own GitHub and… We'll just say, yeah, there's this third-party thing if you… if you want a starting point for this.
Trask Stalnaker (Microsoft Corporation) 00:34:38 I mean, from the agent perspective, this is something that I really want. The, the profile… this is… this unlocks the profiling,
Jonathan Halliday (IBM) 00:34:50 Yeah, it's a great feature to have.
Trask Stalnaker (Microsoft Corporation) 00:34:52 Yeah.
Jonathan Halliday (IBM) 00:34:53 But yeah…
Trask Stalnaker (Microsoft Corporation) 00:34:54 It's painful to maintain. Honestly, my… my… my… from the agent perspective, I want this, however… whatever is required. Like, obviously, like, I would like to not… really love to not have a native binary, but if that is absolutely the only way we can support this, then… We gotta figure out a way.
Jonathan Halliday (IBM) 00:35:17 Well, I am in discussion with the OpenJDK contributors about potentially having Java itself, the JVM, declare their self-symbol as part of its build, and to add API surface in, probably an unsafe to be able to read and write it.
which would… solve this issue very nicely, at least for people who are on a sufficiently up-to-date version of Java.
But that'll be, you know, next September's LTS, if it happens at all. So… We shall see. Okay, at least I have a roadmap. So…
Trask Stalnaker (Microsoft Corporation) 00:35:54 Yeah, I mean, if you… so if you can land something in Contrib, then, you know, we can pull that into the agent.
Potentially as an experimental feature.
Jonathan Halliday (IBM) 00:36:04 Yep.
Oh, goodness.
Jack Berg (Raintank, Inc. – Grafana Labs) 00:36:05 What does that even… what is… what does this even look like? So…
Jonathan Halliday (IBM) 00:36:08 And what does this look like?
Jack Berg (Raintank, Inc. – Grafana Labs) 00:36:10 No, like, just like, so we have two different jars that, like, are architecture-specific, or end jars that are architecture-specific, because they take native dependencies.
Jonathan Halliday (IBM) 00:36:23 Usually what you do is you build all your SO files and pack them into one jar, and you have a class that looks to see what it's running on and unpacks the right SO and links it.
Jack Berg (Raintank, Inc. – Grafana Labs) 00:36:34 Okay. See, I…
Trask Stalnaker (Microsoft Corporation) 00:36:36 Nettie.
Jack Berg (Raintank, Inc. – Grafana Labs) 00:36:36 We're on board with that.
Trask Stalnaker (Microsoft Corporation) 00:36:38 Yeah, like, Nettie does that, there's sometimes… or maybe it's the TC native, or something like that. I've… I've seen this pattern before, and it's not… it's not horrible. From a consumer perspective, it's pretty nice, from a maintainer perspective. I mean, it kind of sucks, but…
Jack Berg (Raintank, Inc. – Grafana Labs) 00:37:00 The thing I reluctant about is… is… is like having two different agents where you need to choose the right one based on the architecture. Like, that's a really nice pattern that we have in Java that other languages don't have. Like, Python.NET, and others in the future, you need to select the right auto-instrumentation based on your architecture. And it's… it greatly simplifies that we don't have that, so if there's a way around that requirement, I am… I'm… I'm open to it.
Jason Plumb 00:37:33 Seems like Contrib is a decent fit.
Jack Berg (Raintank, Inc. – Grafana Labs) 00:37:37 It doesn't have to be contribib. Like, I think a lot of this work so far has been in Core, because there's specification for this, and, you know, I don't… I don't want to just put something in Contrib just for the sake of it, if it's going to ultimately live in Core someday, so…
Jason Plumb 00:37:53 Cool.
Trask Stalnaker (Microsoft Corporation) 00:37:58 Let's do it, Jonathan.
Jonathan Halliday (IBM) 00:38:00 Okay, so yeah, I have a version of this running locally.
The issue I think we're gonna hit is that neither of these OTEPs specifies API surface, so that's why the one for the process context is still draft.
There is… there is no specified way for the user to, describe… What they want to export.
Even just to turn it on or off.
So I think we're going to have to update the OTEP a bit before we can define the API surface.
And I presume you don't want to merge stuff?
with a… an undefined API.
So… I don't know. It's some way off yet.
Jack Berg (Raintank, Inc. – Grafana Labs) 00:38:51 So, let me actually just… let me get John Watson's opinion on this. So, So, John, I've been going back with Jonathan on this PR, and back and forth with him, and, you know, it's all about thread context sharing, so it's all about writing, like, context to a shared memory location, so an out-of-process profiler can read from that memory location and propagate that thread context onto profiles for correlation.
And, you know, the thing that I've been struggling with is, like, what is the SDK or API extension point that this plugs into such that you can turn it on and off, such that you can configure it. Or do we need a new extension point? Do we not have the right extension point to do this? And so the things that came to mind for me was, like, the context storage.
SPI, like, if you can hook into and wrap context storage, and every time context is stored, and, like, you know, unstored…
Jonathan Halliday (IBM) 00:39:59 Hang on, there's two OTEPs. The PR you're looking at is process context, and it's simpler because…
Trask Stalnaker (Microsoft Corporation) 00:40:06 resource, just the resource.
Jonathan Halliday (IBM) 00:40:07 All you need is a resource. Now, getting the resource turns out to be surprisingly hard.
But it's… it's doable.
All I did there was I wrote, I think it's Auto Configuration Customizer Provider.
was the extension point I used, and I just had something that looked up a resource and called a method to publish it, and great. That gets called relatively early in the life cycle, and it works fine.
For the thread context, yes, I think, context storage is the right way to go. I have… a rapper currently that does it. I think I would… At least like to try replacing FedContact storage instead.
Instead of adding to it.
And the reason is… that… it's basically a stack, right? You're… as… as contexts are nested, for that context storage stores the ancestors to reach one, so it can… pop them as you unwind the stack. And there is additional, information I want to store in the same manner, particularly the off-feet buffer that It's the serialized version of each one, and it's somewhat cleaner to do that.
in… FedContact storage itself, rather than in the wrapper.
I can use the wrapper if I need to, and that similarly works. I have that implemented.
Jack Berg (Raintank, Inc. – Grafana Labs) 00:41:39 So we've got some data we want to write to a shared memory location. Yeah, sure. Some of it's on startup.
Jonathan Halliday (IBM) 00:41:43 We need a resource, yeah.
Jack Berg (Raintank, Inc. – Grafana Labs) 00:41:46 Some of it is context-specific, like, some of it.
Jonathan Halliday (IBM) 00:41:49 Yeah, so my first thought for getting this resource was, well, hang on, we've already got a resource that appears in Trace exports, right? So something is already configuring that. Let's just ask the trace exporter what it is, and we'll just… Take that. Turns out the exporter won't tell you that. There's no way to get a handle on it, there's no API for doing that. But also, worse, the exporter might not exist.
In which case… Help.
I think probably something based on maybe OTEL resource attributes is the way to go. There's already a, you know, a spec for that.
a configuration surface, right? There's a… there's a variable defined, and the syntax for that as key-value pairs is defined, and great.
So perhaps something that reads total resource attributes and turns it into a resource and hands that to the… The publisher is the way to go.
That's fair.
Jack Berg (Raintank, Inc. – Grafana Labs) 00:42:51 That's gonna miss the mark.
Jonathan Halliday (IBM) 00:42:53 Okay.
Jack Berg (Raintank, Inc. – Grafana Labs) 00:42:55 So, you've got this shared memory writer, and it needs, like, two callbacks. One is, like, what is the resource that the SDK was started with? And this writer needs to be called whenever that's established, and it needs to write that to the shared memory location.
The other callback is when thread context changes, and that happens very frequently, all the time. And again, you need to call back to this This year.
writer.
Jonathan Halliday (IBM) 00:43:21 Maybe.
The reason you… you probably need to do that once There's another bit of configuration, and what it does is specify the dictionary keys.
So, what gets published by the thread?
Is key-value pairs, except the keys, are indexes into something that's in the process context.
Because that takes up less space, and what you want on each thread is as few cache lines as possible.
So, you're publishing a… An index, and a value.
And that index is a pointer into the process context.
But the most likely case is that you have a static configuration that says the things I want to publish on a per thread basis are… say the path. The… is it UL.path? I can't remember what the… the key is.
But essentially, you define a handful of these things, some subset of the attributes, which is what you want to expose. And you build the dictionary once.
And at the point where you've built the dictionary, which is probably somewhere during your startup.
Yes, then you do need to call process context publisher to add that dictionary to the process context. But after that, you probably never need to call it again.
Jack Berg (Raintank, Inc. – Grafana Labs) 00:44:39 You still need to write the values every time those val- those.
Jonathan Halliday (IBM) 00:44:42 No, the values are published by a different publisher. That's not process context publisher, that's thread context publisher. That's not in this PR yet.
Jack Berg (Raintank, Inc. – Grafana Labs) 00:44:50 But there's two…
Jonathan Halliday (IBM) 00:44:51 You need to call every time, and that's the one where you use the context storage hook.
Jack Berg (Raintank, Inc. – Grafana Labs) 00:44:57 So, I was speaking…
Trask Stalnaker (Microsoft Corporation) 00:44:58 I'm a little lost.
Jack Berg (Raintank, Inc. – Grafana Labs) 00:44:58 but I…
Trask Stalnaker (Microsoft Corporation) 00:44:59 Middle East last year.
Could… The… this PR is… so there's two different… things that were…
Jonathan Halliday (IBM) 00:45:11 There's two RTAPs, and you've only got a PR for one of them, which is making this conversation a little bit difficult, because you haven't got the whole picture.
But this, this…
Trask Stalnaker (Microsoft Corporation) 00:45:19 This PR is… so, the… this PR is about… the resource attributes, making those available.
Jonathan Halliday (IBM) 00:45:28 things that are global to the JVM. Well, more or less. You can technically have multiple SDKs per JVM, which breaks this horribly, but… Yeah, yeah. Yes, essentially you need a resource from somewhere.
Trask Stalnaker (Microsoft Corporation) 00:45:40 Is there anything related to the context storage needed for this PR? Okay. So it's the other PR, which is the thread correlation.
PR.
Jonathan Halliday (IBM) 00:45:51 Yes.
Trask Stalnaker (Microsoft Corporation) 00:45:52 PR doesn't.
Jonathan Halliday (IBM) 00:45:52 Well, it will be when I create that PR, but…
Trask Stalnaker (Microsoft Corporation) 00:45:54 Yeah.
Jonathan Halliday (IBM) 00:45:55 You know, that Bark one would go to contribute, for example.
Trask Stalnaker (Microsoft Corporation) 00:45:58 Okay, so in this PR is just at startup, It's published in the resource.
Jonathan Halliday (IBM) 00:46:06 Yeah, most, most likely order configuration, customer, customizer provider.
Would somehow magic up a resource, through some mechanism to be defined.
and then call… Published from this publisher.
Trask Stalnaker (Microsoft Corporation) 00:46:21 Okay, thanks, I'm caught up now.
Jonathan Halliday (IBM) 00:46:27 Yeah, so to land this one.
We need to nail down what the configuration surface looks like, and… there's an open question, does that have to be defined in the OTEP, I'll maintain as willing to say, this is how it works in Java for now, and maybe it'll change.
John Watson 00:46:44 We have mutable resources racing down the freeway towards us at a high speed at this point.
Jack Berg (Raintank, Inc. – Grafana Labs) 00:46:52 Yeah, John, there's a couple of projects that are sort of intersecting on, like, they need resource to be more accessible.
And one of them is this process contact sharing, one of them is entities that want resources to have descriptive attributes which change, and one of them is op-amp, which needs the access to the resource, because it communicates with an external server and uses the resource as, like, the identity source for that.
for that, you know, communication. And so… sort of where my head's going on this is, like, our OpenTelemetry SDK object, which exposes the SDK variants of meter provider, tracer provider, logger provider, it needs some accessor for, like, the resource, which may be dynamic.
Associated with those providers.
John Watson 00:47:39 It's gonna make Gregor very happy.
Jack Berg (Raintank, Inc. – Grafana Labs) 00:47:41 Exactly. Like, it's… it's… I think what Gregor is proposing is needed, it just isn't spec'd yet.
John Watson 00:47:47 Right.
Yeah.
Jack Berg (Raintank, Inc. – Grafana Labs) 00:47:51 And so, like, I'm actually thinking of, like, a new component called resource provider. Like, that's how… that's the language that they're talking about in the entities group, and I think it's mostly right. It's the thing that provides your resource. It provides it internally to the meter providers, and it provides it externally to things like op-amp and maybe context Process contact sharing that need to get access to the current state of that.
John Watson 00:48:15 Yeah.
How difficult do you think it would be to have that spec change there ride on the entity stuff?
Jack Berg (Raintank, Inc. – Grafana Labs) 00:48:27 I think it's really close, there's a PR about entities, that has 4 approvals right now that introduces the terminology resource provider.
And so, at that point, I think we have, like, probable cause to go and build something, like, akin to what I'm talking about.
John Watson 00:48:45 Yeah, no, I think it makes sense. I think it's been something that, you know, people have been clamoring for for years.
So, it's probably about time to build it.
Jack Berg (Raintank, Inc. – Grafana Labs) 00:48:58 Yeah, and it's like, what does a resource do? What does the resource provider do? The resource provider is, like, it's accessible from the meter provider, logger provider, tracer provider, so they can read the current state of the resource whenever they're exporting.
And maybe it has callbacks or something, so that, like, things like op-amp or process context sharing can, like, register to whenever that resource changes, and get an invocation to, like, write that new resource to the shared memory location.
That's, like, roughly the shape that's in my head, but, like, Yeah.
John Watson 00:49:33 I think it makes sense.
Jack Berg (Raintank, Inc. – Grafana Labs) 00:49:40 But what do we do until then? Like, it's like, I think, for Jonathan's purposes, this auto-configuration customizer, which gets a hook to the auto-configured SDK, and therefore can do some reflective nonsense to access the resource.
It, like, it works, sort of. And, it's… it's not perfect because it doesn't work when you're not using auto-configure. I'm not sure off the top of my head if it works if you're using declarative config, so, like, but, like, maybe it helps prove the concept and land something that can be iterated on.
Gregor Zeitlinger 00:50:13 Jack, I think, in the context of, The dynamic control thing, it didn't work.
I cannot tell you right now why not.
Jack Berg (Raintank, Inc. – Grafana Labs) 00:50:28 I… you could tell me that it did or didn't, and I would believe you. And, like, I do think resource provider Did… Gregor, let me ask you a question. Did what I described about a resource provider, which is accessible from the OpenTelemetry SDK object, and which allows, like, external callers to access the current state of the resource, or register callbacks.
that get invoked when the resource changes. Does that shape solve the problem of… that you've… that you've seen in op-amp?
Gregor Zeitlinger 00:50:58 Yes, it would, yeah, and I think it's the right shape.
Jack Berg (Raintank, Inc. – Grafana Labs) 00:51:01 Okay.
Jack Shirazi 00:51:01 If… if the service name is a resource, and not… the standalone service name. Like, is the standalone service name still considered to be a resource?
Gregor Zeitlinger 00:51:14 This is folded into resource attributes, and so you don't have to care where it's coming from.
Jack Berg (Raintank, Inc. – Grafana Labs) 00:51:23 What this would give you access to is the fully resolved resource.
Complete with entities in the future when those land, complete with service name and all other attributes that are associated. And I guess, like, it's up to callers to determine what to do with that. Like, maybe OpAmp needs to find an identity in that bundle of attributes that is, like, service name, service instance ID, service namespace, and use that as the identity for the connections.
But, like, all that's unspecified, so, like, I'm happy to let OpAmp do whatever it sees fit for now.
Gregor Zeitlinger 00:51:55 What entities would… Eventually define that, right?
Jack Berg (Raintank, Inc. – Grafana Labs) 00:51:59 Exactly, that's why I think it's maybe short-sighted to key off of service name too… too heavily. Like, in the future, resources will have entities, and entities will be a deterministic identifier for the resource.
Gregor Zeitlinger 00:52:12 Is that part not already specified? What… what, constitutes the service identity, I thought this is something that we had discussed extensively.
Jack Berg (Raintank, Inc. – Grafana Labs) 00:52:23 Yeah, it just hasn't landed yet. Like, there's, there were some, some behaviors in the spec that are too ambiguous, and, like, that basically stalled Josh Surrett's PR to land entities in OpenTelemetry Java. And… Once those get resolved at the spec level, we can, like, you know, we can land the entity's implementation and you know, you can actually start having this identity that I'm talking about.
Gregor Zeitlinger 00:52:53 So what do we do until then? We still have to decide what we do for the dynamic control in the meantime, because it's probably not gonna land until… We want to release 3.0.
Jack Shirazi 00:53:08 The dynamic control's a different situation, because the op-amp doesn't have a… Define node within Declarative config, and that's a different issue.
Gregor Zeitlinger 00:53:21 But it essentially boils down to the same problem, that, you cannot get the resolved YAML file in memory, including all the hooks that may have run.
Jack Shirazi 00:53:37 Although that's true, that's… I would be wor… less… I wouldn't be worried about that. I think that's… that's an improvement.
That, the dynamic control would later on be able to figure out what the, the resolved Service name is, but… I don't think that… that has to be the initial implementation. I don't think you need to worry about that.
Gregor Zeitlinger 00:54:03 If you're fine with restricting what the YAML file can be, then you can also establish the convention that the YAML file ought to have a reference to an environment variable.
and then you can read this environment variable yourself. Then you're just saying that this is a restriction to the YAML file, and It is a best practice anyways.
Does that make sense?
Jack Shirazi 00:54:35 I think we're… we're doing three different things here. So let's… let's go for one thing at a time.
OpAMP doesn't have a declarative config specification.
And consequently, the only way of implementing it is by Finding a property or environment variable.
Even if you're using declarative config.
And that's… I think that's the primary issue you have with the current implementation, Gregor.
Gregor Zeitlinger 00:55:08 The declarative configuration is specified, and it does say that, it is the only source of truth. You're not allowed to also read system properties.
Jack Berg (Raintank, Inc. – Grafana Labs) 00:55:22 Just doesn't have any surface area for op-amp.
Gregor Zeitlinger 00:55:31 You mean I'm confusing something?
Jack Shirazi 00:55:34 Gregor wants the up amp.
the op-amp endpoint and any other items that OPAMP needs to be defined in the declarative config.
Gregor Zeitlinger 00:55:45 No, no, no, no, no, I'm not saying that.
Jack Shirazi 00:55:48 I don't find it.
Gregor Zeitlinger 00:55:49 to increase the surface of declarative configuration. This is about… The service name that is defined in declarative configuration, and that That is… should be used both for the op-amp configuration, for the identity, and also for setting up the SDK. This is what I'm talking about.
Jack Shirazi 00:56:12 Yeah, I mean, I'm fine with an implementation which just uses the service name that's defined in the DeLuity config.
I don't see a problem.
You cannot…
Gregor Zeitlinger 00:56:23 get it out of it. This is, what, what the problem is.
you cannot, you could read the YAML file, but it would be incorrect, because it can be… Modified after loading.
Jack Shirazi 00:56:42 Good luck.
Jack Berg (Raintank, Inc. – Grafana Labs) 00:56:43 Not yet.
Jack Shirazi 00:56:45 Oh.
I… I thought it was using… I thought I was using a, A declarative config provider.
to get the defined service name. Was I not doing that?
Gregor Zeitlinger 00:57:05 Well, I cannot look at the source code right now. This would take too long.
Jack Shirazi 00:57:09 Okay.
Gregor Zeitlinger 00:57:11 I can double-check, but as far as I remember, this was not the case.
Okay, we're running out of time, anyways. Should we discuss it again, next week?
Jack Berg (Raintank, Inc. – Grafana Labs) 00:57:24 I think… I think the takeaway that we should have is that, I don't think we can or should block 3.0 based on this… this issue.
I think that there is a proper solution coming. In the nearerish future, with the spec formalizing what I call, like, a resource provider.
And then, you know, things like Jonathan's context process sharing and Jack's op-amp being able to, you know, key off of that and get resource information in a reliable way.
But it's, like, and I'll build that as soon as, like, the spec lands that even suggests that this is a capability. Like, I want to unblock these situations, but they're not there yet.
And, you know, like, you know, just going on the declarative config, front, Jack, like, as soon as there is a specification on how op-amp intersects with the SDK, we can… we can add that declarative config schema formally for… for op-amp, so… But that's… I don't know what the solution is there. I do not see any open spec PRs that, like, formalize that interaction between the SDK and op-amp, so…
Trask Stalnaker (Microsoft Corporation) 00:58:48 Jason, you comfy there?
Looks hot.
Jason Plumb 00:58:51 It's heating up. It's heating up.
Trask Stalnaker (Microsoft Corporation) 00:58:58 Cool, we've got 2 minutes left. Real quickly, Sylvain, apologies, haven't… Looked over this one yet.
Sylvain Juge (Elastic) 00:59:09 So, it's actually just a ping, so I reworked it to make it only rely on metric names.
So we should… Be more convenient to use, and we can get rid of the Any reference to target system name.
But maybe something that is worth knowing. So, with that, we basically register everything, and then we disable all the metrics that are not being, like, opt-in.
Which means there is some more registration, so we could… Probably further optimize it, because there is some lookup of all the embeds.
But when something is being filtered out, so when the MBIN is not present, it means the lookup will still continue, to be executed.
But if the MBIN is present and is ignored, it will be removed.
Trask Stalnaker (Microsoft Corporation) 01:00:07 Cool, I will, yeah, we need to get this in, so yes, I will… Get to this, probably early next week.
Sylvain Juge (Elastic) 01:00:17 Yeah, thanks.
Trask Stalnaker (Microsoft Corporation) 01:00:18 extra to get it in, yeah. Thank you.
Alright.
Any last word?
Good seeing y'all.
Jack Berg (Raintank, Inc. – Grafana Labs) 01:00:35 Take care. See ya.
Gregor Zeitlinger 01:00:38 Theorem!
