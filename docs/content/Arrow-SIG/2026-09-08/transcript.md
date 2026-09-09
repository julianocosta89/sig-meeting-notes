SIG: Arrow SIG
Date: 2026-09-08
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Pierre Mariani** 00:46 Hello, Joshua. Hello, Aaron.
Hey, hello.
**Josh MacDonald** 00:52 Trying to find the right window.
Alright, I told Laurent I would run this meeting, and here I am.
So… please… perhaps consider adding your name to the agenda. I know we have four of us now, so I'm speaking to a small number. But, I've… Added one to describe the work that I'm working on today, or recently, and you might do the same.
I'm gonna wait another minute or two, so… Stay tuned.
Secret is, when you're running the meeting that's on a Tuesday, it's only been 6 days since the last meeting. When you do the Thursday, it's been, like, 10 days, or 8 days, or something like that.
Hello. Alright, well, now we have… five of us, so we could probably move forward. You know secretly I love it when Meetings ends early, so we'll see what we can do.
Here we are, here we are, okay, I'm going to start. First we have issues that need discussion.
And I went through them earlier.
It's probably more than… I had 4 down, but yeah, here we are. So… two of these topics have been sitting around in this list for weeks now, and keep sitting there. The Phase 3 update is one that I'm comfortable with. We keep waiting, or I keep hoping that CJ will join us for a meeting to talk about this next one.
And I probably should have pinged him earlier than recently. So, if he joins us, we can come back to this one.
The… so the first two we've talked about before, the next one is this Kafka receiver I looked through earlier, just calling for some consolidation in the code. It's become a little bit… I guess the word is sloppy these days, at least a little bit, so, Refactoring is a thing you want to do when your code gets to be close to 10,000 lines, I think.
And I think I've seen a draft PR that's open for this one already. Maybe we'll… Maybe I have, maybe I haven't. Okay, I haven't. He's got another one.
**Laurent Quérel** 03:40 Yeah, I know that Shen Li's working on that, I asked him to… Yeah, to improve this part of the code, and also to… to update the Readme file, I'd like to see, a better architecture or documentation around the Kafka receiver, Kafka Exporter.
And alignment between the architecture and the components of those receiver-exporters, and the… That will instruct, basically, the code refactoring, because we need to simplify definitively.
this code in order to any future maintainer to better understand what is happening and how to deal with this code.
**Josh MacDonald** 04:29 Gotcha. All right. Well, I agree, and I look forward to this, improving. I expect that you would like to see a diagram That's… that's become a common request. I think we should.
**Laurent Quérel** 04:44 Yeah, I think it's a good practice to have some high-level overview of the architecture, and… It's missing today.
For the start of the good.
**Josh MacDonald** 04:56 hopefully we won't encounter more of those examples throughout this meeting as we run through open PRs. So these are the issues I opened early, earlier today that are stale. I closed a couple of them before the meeting. The ones that are left open.
I'm glad we have a couple of my team members here. I'm gonna ask about this oldest one here. If you recall, at some point in the past 6 months, we were looking at integrating with a very large C++ codebase that we have.
And we're talking about how we would connect it with the Rust codebase that we're working on here. This request was filed for a C++ interface. I know, Laurent, that you were interested as well. I have a feeling that we've… found a better way to do this by now, and I'm gonna open the floor.
**Laurent Quérel** 05:45 What I remember was… Using the concept of topic as, A way to exchange between… A pipeline instance and the rest of the world.
I think that was the direction we… Would you stop?
Yeah, what we did on our side, but it's… I don't think it's, I mean, addressing all the aspects of, what was mentioned into this, bit of issue, but what we did at some point was to create a C… a CAPI That will, basically, expose, some of the… admin API we expose with the HTTP endpoint. So basically, the ability to start, stop pipelines.
I think what you'd like to see here is something a little bit more, More advanced in terms of unveiling the… or integrating the… decent gene was… yeah.
Yeah, so, I think, topics are, a good, a good approach.
to connect, or to, yeah, to connect this, in-process padata exporter with, with a C++ application, or some other external application.
**Josh MacDonald** 07:22 Okay, Any chance Aaron or Karsh has any recollection of this topic? I know that Samir, I haven't spoken with Samir in a bit.
And you don't have to have an answer.
**Aaron Marten** 07:37 I know what was driving this topic, I don't know if this… this issue is still relevant. I'll need to sync with Summer.
**Josh MacDonald** 07:46 Well, I think we can accept it. It should have been accepted, like, whenever, February, but, here we are, and now we can, hope that something happens, or we'll review it for staleness again.
In a bit.
Let's see, okay, so I know I remember when this was filed that we had a major problem with the build, you know, back in March. I believe we've solved the ARM runner question, but I wanted to run this by the group.
No answer is a good answer.
**Laurent Quérel** 08:26 I think that has been fixed, but, I think, maybe Zhou… is Joe with us today?
**Josh MacDonald** 08:33 Don't see…
**Laurent Quérel** 08:34 No.
Yeah, I'm not sure 100%, but I'm relatively confident that has been fixed.
**Josh MacDonald** 08:48 I think I, will agree, so we're gonna close that one. The next one on the list was, one that I didn't remember very well, asking for something… that's the problem with these issues that refer to PRs, in the pipeline control… Message Manager.
Hey, looks like we… Oh, this was a PR… Looks like we lost, Ukarsh, so that's okay.
**Laurent Quérel** 09:24 improvement suggests… Let's see, great fix, so yeah, yeah, I agree.
I think we… we have some element of… can you assign me the… this, this GitHub issue?
And, I will investigate a little bit more,
**Josh MacDonald** 09:58 E… yes.
**Laurent Quérel** 10:00 because we did… we did a lot of things in this area now, to improve the situation. I will read again the, the suggestion, which was, fairly, fairly big, that I did in this Pierre, and I will check that we did everything. I'm not sure 100%.
**Josh MacDonald** 10:22 Sounds good. There was also one that I closed as stale, and I think we took care of it, but I'm going to mention it since now I realize it's actually connected.
And… So… Those are the open ones.
And I decided that we could close this one, but I believe it's very connected. It was the same period in time.
This is… this is the mechanism, the actual API call, that lets a node signal that it's experiencing back pressure, and it's called receive when, and there's a Boolean, as far as I recall, argument.
**Laurent Quérel** 11:00 Yeah.
**Josh MacDonald** 11:01 I'm gonna leave that this may be connected…
**Laurent Quérel** 11:10 Yeah, thank you for that.
**Josh MacDonald** 11:12 with that one, and we'll leave it open, and it has been assigned. Thank you.
**Laurent Quérel** 11:17 Thank you.
**Josh MacDonald** 11:19 And lastly, Albert.
There's one… -Oh, you closed… nope, it just got updated. There's one open from 6 months ago about… Date and time columns.
**Albert Lockett** 11:34 Yeah, we still want to do this. I haven't worked on it, but it's not stale. The reason I've got it not ready for work is just because I think we have some figuring out to do with the type system. What happens if you subtract two timestamps? What do you get?
Arrow has its own answer. I think the code collector has its own answer. We probably also need to have an answer, so… Anyway, I just didn't want someone to step into it and start doing it without the analysis being done, and so… but yeah, we still want to do it.
**Josh MacDonald** 12:04 Got it.
**Laurent Quérel** 12:07 In this area, just for information, something that Albert, I did recently related to… tile… So there is a now function now available that you can use to basically have a timestamp.
To a signal that, for whatever reason, does not have a timestamp, or to the location that you'd like to see the timestamp. And there is also a way to… To cast… Because we, we had to support testing, Between different data types.
So there is also a way to cast, the result of the narrow function, which is A timestamp into whatever format or data type that you'd like to see.
For an attribute, it could be a string, it could be an int.
Just for… as a reminder, that's something that has been added recently.
**Josh MacDonald** 13:05 Right, here's one, and here's the other, in case you missed it.
So, we're making progress. Very good.
Okay, well, we made it through all the issues. I did take a pass through, the list of PRs earlier this afternoon, and I don't think there was anything majorly important worth talking about, except there are some stuck PRs. If you own a stuck PR, help us by resolving some of the, conflicts, basically.
Including one from Chan-Lee about Kafka, one from… from some… some… I forget who on the Windows performance test, there's a huge document by Lalit that also needs reviews and so on. But I don't think we should discuss those things here.
Anyone, mind if we move on to, agenda items?
Okay, well, I just want to provide a progress report. You know, I merged an RFC number 0004, a while, a week and a half or two ago, and, I have been trying to make, implementation progress, and this one is tricky because it is a… Touching a fairly cross-cutting concern in the codebase that ends up kind of touching a bunch of stuff.
And I will say for… just… I tried to redo this a couple times and end up with a smaller PR, and I'm not… I'm surely I could end up with a smaller PR, but not one that's much smaller that actually does something.
So, I've asked, a team member to give me a thorough review, which is a lot to ask, and it's, I'm giving him some time. I also just wanted to talk about it in this group here briefly.
So, the transport headers feature that we have today is a little bit inefficient in the way it's implemented, and the code has a little bit of, difficult-to-read nature involving when a value has been normalized. So for these transport headers, which are in the configuration, we generally normalize them. One thing I've done here is introduce a data type to make that a little bit safer and easier to handle, and the code look a little bit nicer.
So then, I also was benchmarking this, and I've developed some pretty intense benchmarks to get to all the different variations that we have.
I'm also trying to just apply some general, like, Rust improvement that I'm making for myself. So, for example, switching from a VEC structure to a boxed slice saves you one word of space in some cases, so that's the type of thing that I was making sure that as I'm benchmarking, like, we should be able to make this truck slightly smaller and move performance.
So, then everywhere in the configuration where we refer to a context entry name, like a header in the configuration, what we're going to do is validate it as part of configuration.
and there's a separate conversation about that, actually, that we should have, one of the open. You know, we missed an issue. I'll come back to that. So we validate that the configuration fields are valid, they can't be empty, for example, or have graphic characters in them.
Then, that means that you have lowercased header names.
there are four components that I've touched in this PR that all declare and bind to context, so… so that includes, the… partition processor reads a transport header value. The traffic generator generates them. There is also a couple more. And then, so Kafka is big. Like, the Kafka exporter and the Kafka receiver, and then… through the general engine policies, we have capture policies, which all the receivers can do, and then we have propagator policies, which all the exporters can do. So.
I've gone through and modified four components plus the policies to generate these declarations, which is a global view of your context bindings. So every node that consumes context somehow is expected to declare it through the factory, and that means that the engine can build a complete configuration story and hand it to you through pipeline context. So pipeline context, If you recall, that is the thing that Start receives when a new node fires up.
or when you reconfigure a pipeline, a new pipeline comes up, you start all the nodes. So Pipeline Contacts is handed to you, and what I've done in this PR is add a new compiled context policy object, which is all the engine's… engine-wide configuration of context declarations. And that tells… think of it as a compiler what information is necessary to propagate the context. So, as an example, the only change, the only functional change that I'm optimizing here is that Is that if you are… if none of the bindings across the entire configuration will use the original header name, which has case preservation potential.
If nobody wants case-preserved header names, then it won't be stored in the receiver, and that way we just save an allocation, for example.
A couple of other things were just sort of, like, almost difficult to keep and easier to optimize than not. The capture logic would go through the list of rules one at a time, and this is a pretty good place to apply a hash function, so I've changed it to use a hash lookup.
of the… You… that's indexed by these normalized keys called context entry name, so that means there's a case-insensitive lookup happening.
And I have posted some benchmark numbers. So we're seeing, you know, good improvement on end-to-end propagation.
Thanks to those various, improvements. So, that was all I wanted to share.
I, again, I have a thorough code review on the way, and, that's my proposal for, the first step of the work that I have proposed.
I will offer anyone who wants to speak this moment.
**Laurent Quérel** 20:05 I'm a big fan of the…
**Josh MacDonald** 20:08 I owe you a diagram.
**Laurent Quérel** 20:10 No, what I like is the fact that we… we force… Hello, declaration.
In the config file.
So we can build, highly optimized approach to manipulate those headers and transport them, and blah blah blah. So, for me, that's definitively, any type of security, forcing people to, to express the error and how they propagate, I think, is… It's a good, a good approach.
**Albert Lockett** 20:48 I'm, can I just ask a question? And if this is in the PR, you can tell me to just go read it.
So, as I understand it, based on what you said, the, it's the responsibility of the component to tell the engine, hey, here are all the, the context, context entries, formerly called headers, the keys, basically, that I'm going to, either access or produce. And then, when the node starts, it gets some context key, and then it can then use those to either set or get context values, is that right?
**Josh MacDonald** 21:28 That is the direction. This PR is a very first step in that direction. There's no compiled key identifier, for example, but there is a normalized key now that I'm enforcing some new discipline around. And I know, for example, from looking at some of these components that the… there's a wild card, basically. Like, I propagate all… I propagate all the entries, and that's… that's one of the declarations that's going to be supported.
As far as I know, the wildcard consumes normalized values, so you don't have to… if you have the wildcard, you don't need to preserve the original names, as an example.
So, so… and if we find a new type of policy, we'll just create another enum value, so, like.
Oh, if you decide you want wildcard with original case sensitivity matching, then you can… we can do that later.
**Albert Lockett** 22:18 Okay, okay, cool.
**Josh MacDonald** 22:19 This is my epic that I had, and… Just to, I guess, wish I could see the numbers. 19, 3919 is the one that I'm… kind of focusing on right now. I… The… since… since we mentioned security, like, the… one of the next features would be to get authorization… authorized data fields into this context.
I've… I had also proposed a byte-oriented encoding, but that could be pushed back. It doesn't need to happen. The point is that we need to start getting, strong type information and putting these other types of values into our context, ideally soon. So that's what I'll be working on.
**Albert Lockett** 23:01 Okay, sounds good.
Yeah, the re…
**Laurent Quérel** 23:05 So, Albert, is your question related to the fact that… I try to understand… I think I have an idea of why you are asking that, but I'd like to double-check.
**Albert Lockett** 23:17 The revenge.
**Laurent Quérel** 23:18 The fact that we can have also a good…
**Albert Lockett** 23:20 Oh, I was trying to figure out, like, if and how this would work with, like, let's say that in OPL someday we wanted to be able to do, like, programming with headers, right? Maybe you want to write a program that says if the header value is this, then route it to this destination, or conversely, maybe you want to say something like, hey, every batch that has this field in it, like, set this particular header value, and I think that, like, with what you're… what you're saying here, we can… we can achieve a lot of that. Like, for example.
We should be able to, like, parse the program up front, figure out, here's all the, like, references I have to some… to some header value, and then I… tell the engine to create context entries for that. So, like, it's pretty… it's pretty easy to do, like, especially if the program only defines, like, static header values. If it tries to, like, define them using some kind of, like, dynamic expression, then maybe we have to, maybe, like you said, we have to have some kind of, like, different enum for header value propagation, but I think that'll, like, a lot of our early use cases are, like.
I mean, jeez, I don't want to say, I don't want to say something that I… that I can't, that I can't… but I think a lot of our use cases are probably, like, the header key, at least, is something static. So, I think, yeah, I think we'll probably be okay.
**Laurent Quérel** 24:52 Yeah, I agree.
**Albert Lockett** 24:54 I was just trying to basically say what we're probably gonna try to do with this after.
**Laurent Quérel** 25:02 Yeah, and so… because you are parsing the OPL script or program.
During the first phase, when we basically receive the configuration of the transform processor, for example.
Then you will be in a position to extract from the OPL program.
the header keys… Assuming that there is no dynamic hierarchies.
So there is something like set header.
Header name or error key, blah. And, and then you could… you could basically extract the list of error that will be provided to what Joshua needs, in the questioning framework where the headers will be specified.
And that would be good enough.
**Albert Lockett** 25:58 Yep.
Exactly.
**Laurent Quérel** 26:00 I think it… That sounds…
**Josh MacDonald** 26:03 Sounds right to me.
**Laurent Quérel** 26:04 Yeah, I think that the use case is… I don't think we really have, right now, a use case where the error key by themselves could be dynamic.
I don't know if it's even, a good thing. So, personally, I'm fine with this limit.
**Albert Lockett** 26:27 Yep.
**Josh MacDonald** 26:27 Thank you. So… Yeah, I think that the types of configuration that you might express through OPL will also be configurable in more raw configuration, and so either we'll have some YAML that has references and gets compiled, or you'll have OPL programs that do the same thing. And I don't… also don't know if there are our dynamic Header bags that matter, or so… and so on.
But if we need to, we can do it.
Great, so I've mentioned that we had forgotten an issue, and I see on the list of attendees somebody new. May I put you on the spot, Pierre and invite you to say hello?
**Pierre Mariani** 27:15 Of course.
**Josh MacDonald** 27:16 ink.
you are… contributing… Let's see, I can't remember where.
I believe you have a PR open.
**Pierre Mariani** 27:28 It was merged a few hours ago. It was merged, okay. Yes, yes. Thank you, yeah, thank you for calling me out. Hi, everybody, this is Pierre, I started contributing to the project, last week, and, you know, doing this in my own time, it's not company-sponsored.
Yes, I worked on this configuration issue, mainly because it was one of the first, good first issue for newcomers.
And learning the process, so, I've also contributed, Found an issue related to configuration validation to mostly ask questions more than propose anything. I try to understand.
You know, if we can, validate configuration systematically and kind of at scale across everything. I think at this point, I'll probably keep looking for good first issues, in the codebase to get a better understanding of what needs to happen.
If I don't find anything, I will focus on testing. I kind of want to understand how things work into it.
But yeah, thank you very much, and excited to be here.
**Josh MacDonald** 28:39 Thanks very much.
**Laurent Quérel** 28:39 Thank you.
**Pierre Mariani** 28:40 Monsieur.
**Josh MacDonald** 28:41 Yeah, so I read this issue, and I put, like, I remember, you know, like, we've had issues filed about broader configuration issues starting as early as 1832, but I also realized we were missing some. Oh, you have it, you had it, of course. Well done.
**Pierre Mariani** 28:58 I figured the answer.
**Josh MacDonald** 29:00 There was, just recently, we… we've been looking at the problem of keeping header values secret, like, not accidentally leaking into the logs, and we've re… we've turned away some pull requests.
that were attempting to attack that problem, and I think would end up basically running into the same type of issue that we have here, which is the need for a struct of nested configuration structs, of nested configuration structs, to have some sort of trait that is, like, universal across all the configurations that you can, like, hey, I want to check if this config is valid. I want you to recursively check if this config is valid, and I want you to, when you print this configuration, call my hook in case it's a secret value so that I don't accidentally print this configuration. And every time I see that, I realize I don't have enough rust strength to find a good solution on my own. So, I'm glad you brought this up.
Laurent, you had talked, you had, put a kind of hold on one of our colleagues' PRs here.
**Laurent Quérel** 30:14 Yep.
**Josh MacDonald** 30:14 Realizing that we had not provided enough framework around configuration. Do you have any thoughts?
**Laurent Quérel** 30:19 Yes, that's true.
So there is, I have an ongoing branch where I'm basically refactoring the… The framework we use to manipulate basically, configuration. So the… right now, we… We don't really have a separation between The configuration that, we get, either from a file or from… reliable configuration coming from API. And what we do internally with this configuration that we provide to each pipeline engine, and, and more importantly.
The same configuration structure is also used when we want to expose the… The current, status… Of every running pipelines.
Which… Bring a lot of issues in terms of security, because we, we don't really have an easy way to… say that, especially in the… so, for people that are familiar with the configuration, there is basically an engine-level configuration field… a set of fields, and… and we have… A node-level configuration which is, represented with the config field into each node.
And we delegate the validation of this part of the configuration to each individual node.
And, and basically, the engine does not have any, way to look inside this config node level information. So I'm refactoring the framework to make sure that there is a good, a well-defined protocol between the engine and the nodes.
And… and we end up with… A separation between the external configuration and the internal representation of this configuration in order to make sure that For the internal, that's the responsibility of the node to provide or to identify fields that are Privacy or security sensitive.
And there is a well-defined protocol, so when we expose this configuration back when we, for example, we asked for status for pipeline.
We ensure that we never expose, information that has been identified as secure or privacy sensitive.
So the, I hope that this week I will be able… I'm not sure, I hope that this week I will be able to transform this exploration branch into a Pierre editor for review.
Pierre, I can definitely ping you also when it's available, so you can review that, provide feedback.
And maybe that could be, Also, a nice way to add some additional things that you notified.
**Pierre Mariani** 33:34 So, yeah, that'd be great. Happy to do that.
**Josh MacDonald** 33:39 Very cool. I pulled up the other issue that we had filed recently from Laurent about that one here, 3848, and I'll just remark, I've said this in the past, some of you have heard this already, we… the configuration problem is, like, one of the biggest in this territory that we find ourselves in. The Go Collector, as… I would say struggled with that. Maybe one of its biggest struggles is how hard it is to get to a place where your configuration is… has all those properties that Laurent just mentioned. I'm going to put in a link to the conf map. It's sort of like half the complexity in the Go Collector is just configuration, and I worry that we're heading that direction, but maybe we won't.
Cool alright, well, the next topic is yours, Laurent.
**Laurent Quérel** 34:32 Yeah, so I didn't prepare, an LFC for it, but, what I'd like to do is… Exposed the, the context, the, the… the problem I'm trying to solve, and collect feedback from people present in this meeting.
Because I think it's a concern that we all have.
So, either on the Five side, or a Microsoft side, or whoever is using the system.
So, right now, we have some internal team using the… this, hotel RODF engine, and we have a QA team reporting some bugs sometimes, and I'm always… disappointed by the level of detail that this QA team is providing. So, what I lacked, and that will be true also for future, Use of this scene by… Anyone, or future customer, or future users.
So, what I like is an easy way to collect diagnostic level information.
In a very, I mean, systematic way. So basically, ideally, I'd like to get an archive With different information inside, like the flight recorder or something similar, where we get the… metrics, logs, configuration endpoint, history of the last X configuration without the secure slash privacy sensitive information.
Cpu, PProf, memory PProf, if it's, available.
So… the way I see it is… an HTTP endpoint, or, something that we could trigger with the DFCTL command, the CLI.
And… and then we, yeah, we initiate this, this request.
The system is collecting all the information I just provided, or specified there. Probably some of them are missing, and then we get a zip file.
on this Z file, So first, all the information will be there, so that will be nice for… to… to basically to, To attach the corresponding zip file to a Jira report, or to a GitHub issue, or whatever is used by the corresponding user and the QA team. But ideally.
what I'd like to see is also the… Right now, we have an admin.
UI that is embedded into the DFE engine, which is nice.
What would be really cool is an option in this, admin UI to Load the… the archive.
And put us into a position where we can see The last 5 minutes, the last 15 minutes of what happened, just before the, the creation of this, diagnostic archive.
And then we can look at the logs, we can look at the metric, we can look at the various things, the configuration file, and so on. That would be, in my opinion, really cool to investigate an issue and very quickly, Make some, analysis of it, and… And I also… that could be also very interesting for an agent to look at the provided information and try to reproduce the issue because if we have all the series or the sequence of the configuration file, what I'm observing a lot, those days is During the live reconfiguration, sometimes we… we are stuck.
It's not an easy way… I mean, it's not so easy to overuse the problem, so having all those information all together will, greatly simplify the… The debugging and the fixing of those issues.
**Josh MacDonald** 38:51 Alright, this is a… I'm sure we've seen this before, many of us, I remember the port 8000 diagnostics port from my last company, for sure. Anybody in the audience have thoughts or feelings?
**Pierre Mariani** 39:10 I have a number of questions.
So… There would be some type of, flag that you would turn on, so that the system starts recording this… those details.
And then you generate the traffic that is interesting to you, and then you export it, or… you want the system to automatically be able to record the last 20 seconds, whatever number that is. I'm assuming, in that case, it would have to be something that can be turned off.
So, you're nodding, so it sounds like it's more of the latter.
**Laurent Quérel** 39:45 Yes, yeah, I was, yeah, because most of the time, Oh, bye.
It's too late to enable the fat to, to, yeah, to, to trigger this, this plug, and, Having some kind of ring buffer, recording the last X second, or the last X minute.
I'm talking about only, obviously, internal telemetry, the internal telemetry system, the ITS system that we have into the engine.
Yeah, I think that's… that will be, ideal. Not saying that the first option that you described is not, also another option. Maybe we can support both. My first request is the second, the second description.
**Pierre Mariani** 40:41 And…
**Josh MacDonald** 40:45 And we have this log tap mechanism that receives… events and puts them in a log… a ring buffer, as far as I understand, so that might be, like, a model… The topics that you just mentioned are all very much within the scope of the wider diagnostics like, organization that I sit in, and, like, lots of technology exists for that sort of, like.
buffering. Usually it uses ETW, or Linux user events, or perf, like, kernel support, and so on. So I love the description of a flight recorder. I've been thinking of a flight recorder as something more like a mixed… like a… A real-time mixed signal protocol, that you might use to record the, like, here's the exact state of my application when it crashed, maybe.
For example, or here's a minute of intense data that I wanted to collect, and then I stopped after a minute.
I actually… while I love that, I… what I was hearing was a more simple, or more configuration-specific, like.
Maybe we have, special much like LogTap just gives you a way to have all the logs go to a certain place. These are the critical configuration log messages, and they also produce, like, a trail of, like, replay instructions for the operator who wants to try and reproduce a configuration problem.
Without including any data, which might be a much simpler request.
I like both of them.
**Laurent Quérel** 42:20 And… because we have Aran with us today, I'd like to ask specifically to Aaron a question regarding the… A durable processor in relation with this, Ring buffer approach that we just discussed.
Alan, is it possible to… to use a variation of the, the derailable processor, where we could specify the derivable processor to work and record the last explode on the disk. Basically, Behave like a ring buffer and a pass… in a pass-through mode.
And… and when… And when we trigger a snapshot, we get, basically, the last recorded information.
So it's very close to what the durable processor is doing, but… Without necessarily, VF… I mean, it's not used in the exact same context that it is used right now.
the goal is not to make persistent and making sure that ACNAC are, are, will drive, basically, whatever information is stored on the disk. It's more using it as a ring buffer approach, and then we can trigger a snapshot.
**Aaron Marten** 43:51 Yeah, obviously I'd have to spend a little time thinking about that, but… but I think, you might be able to do something like that. So, the way that the… Not necessarily the durable buffer processor, but thinking about the design of Quiver underneath.
The way it works, right, is that, It writes these segment files to disk, and then on the other side of that, there's subscribers that get notifications that, hey, a segment file is now available.
And then when all the subscribers acknowledge that, that segment file, then Querel will clean it up, because it's been, it's been fully processed. So you could imagine that you've got a subscriber that, behaves like this, where it, you know, it gets these notifications.
And it sits on it, and that notification, it sits on for some fixed amount of time, 20 seconds or something like that.
**Laurent Quérel** 44:43 Right.
**Aaron Marten** 44:44 And then after 20 seconds, it says, yep, we're good. And then, it will… it will automatically clean up. So in that way, it will act like a ring bumper. But if at any point in time, it gets a signal of, hey, we need you to report the snapshot, at that point.
It reads all of the segments that it has received pending notifications for, and, you know, sends them somewhere.
**Laurent Quérel** 45:07 Yo.
But do you think… so I can see how we could emulate The, the ring buffer approach, with the corresponding durable, processor, that, do you have a buffer processor, sorry. But do you think that it will, My feeling is it looks like we could imagine a small variation of this durable buffer processor to That will be optimized for this exact behavioral.
**Aaron Marten** 45:46 Right.
**Laurent Quérel** 45:48 Because, you have to manage, with the first, with the general version of the durable buffer processor.
things can… can happen out of orders. So the… you have a message, it's… it's, ACT or NAC, not necessarily exactly in the same timing.
But for the ring buffer that we are looking for.
we could consider that, everything older than X Based on when we receive the corresponding information, we just consider that it's auto-acc.
So I could imagine a slightly more efficient version of what you did based on those assumptions.
Do you see that as a complex and, and big, change, or is it something that we could add easily as a second behavior of this, Of this specific process at all.
**Aaron Marten** 46:53 I don't… I think it's doable. I don't see that as a major challenge, like, doing something like we had just been talking about here.
**Laurent Quérel** 47:03 Yeah, and another reason or motivation why that could be interesting And it's not in the… diagnostic space or, context.
So… and it's… it's always… it's a mechanism that is used by some observative vendor. I try to remember what the one that is doing that… Especially for, in, in the mobile, mobile observability space. So basically, they have ring buffers on the edge.
Directly, let's say, on the… on your phone.
And they, they divide the territory traffic in two, two sub-traffic.
Critical traffic and, detailed traffic.
The detail will go directly to this ring buffer.
And, let's say, a control… a controller plan.
could trigger… the replay of the ring buffer only when it's required.
So it's a… Not necessarily for the diagnosis purposes. It could be for… Just on demand, for whatever reason.
So… That could be a second reason why having this variation of the durable buffer processor could be interesting.
**Josh MacDonald** 48:35 I dug up a link to the thing you're thinking of called the CAP.
**Laurent Quérel** 48:39 Yeah, be brief. Thank you. That's exactly that. And, yeah, it's a very nice feature.
**Josh MacDonald** 48:49 Complex.
I mean, this is, something that… the ring buffer technology is something that Microsoft has a lot of, I will say.
And I look forward to more on this.
I guess this… in a more conventional Microsoft setting, you might use the ETW to record, and then your flight buffer, your flight recorder is what's in the kernel buffer at the moment when you crashed, essentially.
I put also a link to this OTLP MMAP project. It's, one of the OpenTelemetry contributors that you, probably know, Josh, has this, and it's an MMAP protocol buffer sequence, which I think is very much like what Google wants internally, or has… uses internally, that he was sort of socializing.
Yeah, well… I was also wondering if anyone knows of, like, a standard, like, oh yeah, you just asked about a, like, thing, and that's a standard package that gives you the, like, QA pack.
Download feature that we could just import or use, but… I also see the appeal of making it be, you know, OpenTelemetry specific.
**Laurent Quérel** 50:22 Nope.
Okay, so that's the topic.
Alright.
**Josh MacDonald** 50:26 Thank you. I think we made it to the end. And unless anyone objects, we can have 10 minutes back.
**Laurent Quérel** 50:35 Great.
Thank you. Thank you all.
**Josh MacDonald** 50:37 Cheers.
**Laurent Quérel** 50:38 Bye.
