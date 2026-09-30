SIG: OpenTelemetry Specification SIG + Maintainers Sync
Date: 2026-09-29
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Jack Berg (Raintank, Inc. – Grafana Labs)** 03:29 Hello, everyone.
As folks trickle in, please add your names to the list of attendees. If you have any topics, please add them.
I noticed Ted and Alex threw on a big chunk to the agenda, talking about C… C++ bindings, so… I think what we'll do is we'll have the shorter topics come before that, and we'll use the tail end of the meeting to just, like, have that take us to the finish line.
And we'll get started in just one minute.
because we seem to have… Prompt attendance today.
Which is good.
**Mario Román Dono** 04:50 Hello, I have a question. This is my first meeting.
Well, the first time I joined this meeting, and I would like to discuss one of the issues someone pointed me to this meeting, but I don't know how much time is going to take the discussion.
And… I don't know if we should add it here and see it.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 05:14 You're probably in the right place, depending on what issue you're referring to.
**Mario Román Dono** 05:19 Yeah, it's this one. Let me, let me put it here.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 05:21 Would you add it to the agenda, and give an estimate for how much time you think, it warrants discussion, and… We can go from there.
**Mario Román Dono** 05:31 Okay.
Thank you.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 05:33 Thanks, Mario.
And, let's get started now. So, Riley, you have the first topic.
**Reiley Yang (Microsoft Corporation)** 05:40 Yeah, so I shared this PR in an earlier meeting, and I got a lot of feedback, so thanks, everyone. And.
For people who haven't heard about this, this is, like, we're trying to define the level of security commitments.
The current issue is, from the user perspective, when they use OpenTelemetry components, they might run into security vulnerabilities. Either it's as simple as you have a dependency on some other component, and they already have published the CVE, they already fixed that, you just need to bump the version of your dependency and release a new one. Or it could be As complex as a security advisory, that's very debatable, and people want to see whether it is a real security threat, or it's like security in depth or something.
So, the challenge is, for the Maintainers, they want to understand what level of commitment they're expected to do, and there hasn't been, good guidance across the the entire project. And for the users, it's very confusing for them, because they might have different expectations, and they don't know what they can expect here.
So I'm trying to, like, find some balance by giving people this, like, different levels to guide them to, like, to understand what are the things they need to consider, and what are the things we consider as, like, something we expect most of the seeks to be able to achieve. Then we also try to define a high-level commitment, trying to be aspirational.
So, if you look at the PR, I think the medium level is what we want most of the SIGs to be able to achieve. The high one, I guess we don't want that to be that easy, so, like, 5 or 10% of the SIGs, if they work really hard, they might be able to achieve that.
And I think this will help both the maintainers to have a clarity on what they need to do, and the user to see, like, what they can expect from OpenTelemetry. And over time, I expect the bar might change based on what we learn.
So this is, like, a starting point, and there… there are two major things I want to cause that I want to get more feedback in a synchronous discussion here. The first one is.
I would say it's a minor thing, like, a lot of people, they come with opinions saying, I don't want you to say, like, number of days, because I don't have any commitment, to work during, like, holidays or weekends, so why do… like, why don't we say business days? And I saw the examples from other CNCF projects, some of them, they mentioned business days.
My argument here is business days is very vague, like for different users from different places.
What does business day mean? So instead of trying to fight on that.
My suggestion is we stick with days, but we give people more days, instead of, like, doing businesses and confuse everyone.
So, I want to get feedback on that.
And the second one is, I kind of, like, hinted earlier, there are two types of.
things that we're handling. One is, you know, you have a dependency on some other packages, and they have a published CVE. They already have a fix, or they don't have the fix, but they just need to bump the version for their underlying dependency. So it's more like a dependency management. You need to bump the versions.
And for those things, even if you, you're struggling.
you don't want to disclose that. Anyone with adequate tools, they can just download your artifact, or, like, whatever thing you ship, and run the scanner, they will be able to find all the CVEs you have, then they can form a tag if they want. So, I feel, in that case, the… there's actually an urgency.
And I want us to be very sensitive about the time.
The other type is the security advisory. So these are what people discover, normally from security researchers or from some users. They discovered and they report you secretly, so nobody else is supposed to know until you agreed with them on the severity level.
And.
Sometimes, you can even work with them to secretly patch the system and release the fix, and have the fix applied everywhere before you disclose that to the public. So that's why I feel, we have more time.
I didn't try to clearly distinguish them in this PR, because I don't want this document to be, like, too long, don't read. So, those are the two things I'm debating with myself.
With that, I'll stop and get feedback. Robert.
**Robert Pająk (Splunk Inc.)** 10:29 Hello.
First of all, thanks for raising this. I know we raised it before, and there was one reason I… there were two reasons why I have not published any comments here so far. One was just lack of time to… to put it, but second, I also prefer to discuss it. So, my… My concerns are on a more high-level basis than just talking about days, business days, the amount. I'm more concerned about saying that we are committed to anything.
that you are committing, what does it mean from the legal perspective? Will someone sue us, for instance? Or who would sue, like, Linux Foundation, or who, if we do not make the commitments? Like, if there's a commitment, then it means that it's a responsibility that someone… yeah, so… In my opinion, I tried… I looked at the Kubernetes security response. I do not… do not say anything about the commitment at all. They just say that they will do it within 3 days or something, but they do not sell, and, you know, there are no… I… I have missed too far. Maybe I'm wrong, but I'm not sure if they give any, you know, hard guarantees.
They just said that, you know.
And these are my main concerns, just to make sure that… is it… and also, if we want to commit something, then it means that someone, in my opinion, would… Should be, you know.
should be accountable for this, and I'm not sure how we want to achieve this. And yeah, these are… so these are, like, more high… High level questions and feedback.
**Reiley Yang (Microsoft Corporation)** 11:57 Yeah, so I think in general, in CNCF and OpenClimb, we see the level of commitment or something.
that doesn't have a legal binding. So the worst case is if you don't meet the commitment, you should remove the commitment, or maybe you need to step down from your current role. Like, you're no longer an approver, maintainer, or TC member, or governance committee member, or something.
But there's no additional punishment beyond that. So I believe that's the commitment, and that word has been used in other places, I can see.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 12:29 Yeah, I'm typing a message right now to the chat that is related to this, and you know, I think about some of the commitments we make in the Java SIG. We commit to a certain release cadence.
We… and a schedule around that, we release the Friday after the first Monday of each month.
We commit to certain backwards compatibility guarantees, and and more. But these aren't… these aren't legally binding. I don't think, you know, if we… if we violated these, that we'd be subject to any sort of legal scrutiny. But, you know, declaring them publicly, you know, forms a sort of contract that people can build off of.
And it's useful to declare them publicly for that reason, because, you know, even if they're not legally binding, you know, having it written down on paper gives something for people taking that dependency to… it gives them criteria to make decisions off of.
You know, I guess to Robert's point, though.
John Fischer, security does maybe come with certain connotations, and if we can… if we can clarify, or just, you know, reiterate what we mean by a commitment to this, to sort of give ourselves, legal cover, and just not.
not have people making assumptions that can't hold up. That would be useful.
**Robert Pająk (Splunk Inc.)** 14:09 Like…
**Reiley Yang (Microsoft Corporation)** 14:10 I do not.
**Robert Pająk (Splunk Inc.)** 14:11 And I just think that, you know, the way it's working right now, that Maintainers will be You know, we'll probably try to do the best effort, but we'll not prefer to, you know.
Say that they commit to anything.
I think that Java is very special. I'm not sure if other languages are that mature regarding the release cadence, things like that, but probably DTC, you have… I guess others have, you know.
I'm new in DTC, but I'm not sure if other languages are that mature regarding release cadence, responding to security incidents, etc.
Yep.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 14:49 I think public commitments about these types of things, your security posture, your release cadence, your backwards compatibility, they, like, being public about them helps, project that your project is a serious project.
And it's good for the ecosystem. Like, if you never commit to anything, then, you know, at some point, you're not a serious project, and serious projects won't take a dependency on you.
**Robert Pająk (Splunk Inc.)** 15:17 Fair.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 15:28 Riley, I did leave a comment in here about the naming of these things. We've talked about this in, in back channels as well, about whether low, medium, and high.
conveys what we want to convey about these things. Specifically, like, we want the criteria in medium to be the target, and we don't want to convey to external readers that medium is insufficient in some way. It's perfectly sufficient. It is the target, and so I love some suggestions about alternative names. I encourage other people looking at this to to think about alternatives as well through that perspective. Like, you know, we want to convey that medium, or the criteria in medium, is what we expect most projects to achieve, and that's a very reasonable and good set of criteria. So, high really is above and beyond, but it still is achievable for projects that want to go the extra step.
**Reiley Yang (Microsoft Corporation)** 16:29 Yeah, so I made some changes, but for that particular, like, award, I didn't make the change, because so far, I got your feedback, Jack, only, and I want to collect more feedback. So I feel like these things, we might debate on this. It's a tricky position.
Okay, so… I… like, my ask is please give more comments, and be explicit about which one do you think is a blocking concern, which one is more like an optional suggestion.
And if you support, also give support. Otherwise, I think it's very hard to move.
the needles here. Thanks a lot.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 17:17 Thanks, Riley.
I have the next topic. It's a quick one.
There's a PR open in the spec.
chris patterson: And it's about the interaction between declarative config and resource detectors, and what to do when a declarative config file references a resource detector that does not exist.
And basically what this PR does is it relaxes it. Currently the spec phrasing says that the declarative config should return an error and you know.
Resource detectors are not consistently named across all the language ecosystems, and so I want a more graceful degradation path.
So, and basically I want to warn if we encounter a resource detector which is not available in that language ecosystem for more cross-language portability.
You know, this is heavily approved. If folks have final comments on this, please, please leave them or else I'm going to merge this probably tomorrow.
Thanks.
Moving on, Mario. Welcome, Mario. You have the next topic, and it's about this issue, 5178.
**Mario Román Dono** 18:39 Yeah, okay, this was an issue that I stumbled upon a few days ago. It's about adding a new attribute to both Batch Local Record Processor and Batch Span Processor.
For enabling some kind of block mode, so that instead of dropping logs, the thread Blocks, if they're useful.
And in our case, in my team's case, it's interesting because we have an application that which purpose is precisely to process logs as setters to an hotel, collector. And therefore we need, this to be the… to be blocked, if the… if the queue's full. And I just wanted to know, what's the status of this? I saw another comment saying that, it would be… Interesting to add indeed, but I don't know, if we need more, discussion of this, and also I would like to be involved, if possible. I don't know if either by writing something on the specification, or by creating specific implementations on the SDKs, but anyway, I just wanted to bring this topic here and discuss it.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 20:03 From a process standpoint, this is in this triage deciding community feedback stage, and basically we're trying to… the spec Maintainers are trying to decide if there's enough interest in the community to move forward on this idea, at which point we would adjust the label from, you know, community feedback to one of these accepted, labels, so accepted and ready, or accepted ready with sponsor, or accepted needs sponsor, at which point, you know, we're basically saying, like, hey, this concept, you know, this is noted, and, you know, it has enough merit that we want to move forward with it, and somebody can pick it up and work on it.
I can say from my standpoint, this seems like a reasonable addition. You know, if I'm thinking about this, I'm so… I am surprised we've made it this far without this type of capability. Dropping when the queue is full is certainly a reasonable default behavior, but it's not… it's not necessarily desirable in all cases, so this makes sense to me.
Wondering what the other spec sponsors, spec Maintainers have to have to say about this.
**Liudmila Molkova** 21:17 I'm curious, the simple processor would be blocking.
What's the reason not to use a simple processor here, especially since it talks to the collector and the network bandwidth probably is not a huge concern?
Because, like, obviously the blocking has… aware the fact that random operations would start to take a long time, and somebody would pay for this specific, unblocking time… the operation unrelated to this blocking would be problematic. It will be hard to… A diagnosis and everything.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 21:57 The reason not to use a simple processor is because it exports one record at a time.
But the other things you said are true, Ludmil.
**Liudmila Molkova** 22:07 Yeah, and I wonder if Simple is a good alternative, because you pay the price on our operations.
For this. And if it… the… the… Desires talk to local collector.
Then every export in every operation is less problematic.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 22:31 They're all problematic, uniformly. Yeah.
**Liudmila Molkova** 22:34 Okay.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 22:36 Yeah, appointment.
Tristan, you have your hand up. You want to jump in?
**Tristan Sloughter (mydecisive.ai)** 22:41 Yeah, I was just gonna say essentially the same thing that… but the pro… Problem with the simple processor is that it exports it, so you're waiting… you're blocking not both on when the batch processor can accept it, but on when it can be exported. So, it's kind of like you want to switch between being able to throw it over the wall to the processor versus waiting for the processor, but you don't want to necessarily block on saying, well, the export has to happen as well. That's just, It's taking more time than it needs to be, if you're able to run the batch processor.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 23:17 And Tristan, we were talking a few weeks ago about this, this really subtle thing, which is like, should an exporter block until it's.
Its export is complete.
Or, and should, batch span processor, batch log record processor be able to, call, export multiple times?
while waiting for individual exports to resolve, you know, concurrently, asynchronously. And, you know, you were mentioning how Erlang does do that. Erlang allows its batch band processor to call export multiple times, as long as, you know, the exporter sort of still has capacity.
or something along those lines, and Java does not. But I imagine that this type of blocking capability at the processor level couples really well with Erlang's behavior, because, you know, most of the time.
If you take Erlang's stance on this, you know, the queue, it'll fill up, and it will block for just, like, a moment until, you know, the export request is sort of composed and sent off to the exporter. But we won't necessarily have this, this behavior very often that Liudmila was talking about, where, you know, one span ends up having terrible performance.
Terrible blocking before performance because of the exporter.
**Tristan Sloughter (mydecisive.ai)** 24:44 Right. Yeah, it's a common strategy in Erlang for this, is you switch between a synchronous and asynchronous call if it becomes too, clogged up, and you just block When it's too clogged up, and switch back to the asynchronous call when it's, When it's got space again.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 25:05 Yep.
Aaron?
Wanna jump in?
**Aaron Abbott (Google LLC)** 25:12 Yep.
I was gonna mention, I know this is true of, like, Node.js, and in Python we have, like, async functions.
Like, shouldn't this be pushed all the way back to the API so that the caller can decide whether or not they want to block, like, instrumentation?
On the queue export, for example.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 25:36 It's giving the instrumentation a lot of power.
And I guess the question that I always have is, like, what would the decision-making criteria be for that instrumentation? Like, when would an instrumentation decide to block or not block?
**Trask Stalnaker (Microsoft Corporation)** 25:54 I think that's related to the audit.
Proposal in the community that's been open for a long time.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 26:02 Oh, I see.
**Trask Stalnaker (Microsoft Corporation)** 26:04 Where you want guaranteed delivery.
**Aaron Abbott (Google LLC)** 26:10 Yeah, I also think in some languages, it's not possible to block the caller necessarily unless you use these things. So like in node with the simple processor right now. It just runs like a fire and forget doesn't actually block the caller.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 26:30 Well, we should try to decouple these things. I know there is conversation going on around auditing, but that's been unfolding for quite a long time. And so, you know, ideally in my head, if there's, like, a general functionality that can exist just at the SDK level that, you know, allows some SDK users to, you know, influence which of their… influence the configuration so that spans aren't dropped, so that, you know, the caller is blocked instead of dropping the spans. That seems like a good thing.
**Liudmila Molkova** 27:07 Maybe… on passing control to the caller. Sorry for jumping in.
It should be possible to write batch processor in the way that you can build blocking on top of it.
Rather than… Add this feature to existing one. Because it seems like a rare ask.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 27:28 Reiley just made a similar comment in the chat, which is like, you know, maybe there should just be a parallel processor, a blocking batch processor, so.
Yeah.
**Joshua MacDonald (Microsoft)** 27:39 In the collector, we call that the QBatch processor has all the functionality wrapped up in, like, one single piece of code, but you have to set a Boolean that says, I'm going to wait for the result of this call, and it affects all the callers, but it sounds like this would be something you might want to configure on a per… per export basis, or per tracer, or something like that, you know, like, deciding when you want to block or not. There's actually two Booleans in there. One is to block and wait for the request to respond, and one is to block when the queue is full.
Those are separate. So the block when waiting for the result is like what Tristan has described, and it gives you the ability to to have all these things at once. But.
what I would point out here is we really want to have a concurrency option before we go to blocking exports. Right now, this restriction on having a single export is most of the problem that we're having, and there is actually a specification, like, statement saying you shall have a non-blocking API, and that's because, like, it's pretty troublesome to be blocking your instrumentation, which could actually happen inside of an RPC system, for example, and block your RPC export. So, we really definitely need concurrency, and then I could imagine extending the existing batch processor to give you that support, but as people have called out, it's like, maybe you need to switch to an async interface, and so on.
I I've I've I've offered to present the collector's ongoing work with Batch this meeting. Haven't made it to do so yet, but I can come back with some more information on that. Maybe, Mario, you'd like to know more. Braden responded on the issue. He's also been, working in a small group with us to consolidate and unify the SDK and the collector batching configuration, which is sort of a mess.
Because Collector has moved quite ahead of where the SDKs are right now, and I can present that. Thank you, I think we should probably move on.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 29:38 Josh, this sounds like a great topic for, like, a project update, like, a deep dive. Do you want to add yourself to the schedule in one of the upcoming weeks?
**Joshua MacDonald (Microsoft)** 29:47 Yes.
I believe I'm on call for this meeting next week, so maybe that's the time.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 29:54 SDK Maintainers need to know what is happening in the collector.
**Joshua MacDonald (Microsoft)** 29:58 Yeah, I'd like to bring in Braden as well, but yes, we should do that.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 30:02 Sounds great.
I'll just note that, like, as we're sort of, like, wrapping this up, that, what folks were talking about are different solutions for this overall problem, which is like, hey, I don't want my spans or logs to be dropped, because they're more mission critical.
And so I'd rather block the application than have them dropped. And so, yes, we can and should talk about the different solutions, but I actually was sort of hearing some consensus that, you know, in some shape or form, we do want this capability.
Okay, let's wrap up that. Please engage on this issue, upvote it if it's important to you.
And let's move on to Alex Boten. You have the next issue.
**Alex Boten** 30:47 Yeah, this one's pretty quick. I just wanted to make, inform people on this call. Maybe they can go inform other people within the organization that care about the collector. This RFC was published this week. We're gonna talk more about it in a couple of weeks, when we talk about, kind of, the V1 of the collector and the state of that.
But I just wanted to inform people to go have a look at it. We're trying to get as much input as we can from the community, from end users, before we make our decisions here.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 31:22 Yeah, so please go read and engage on that, the long time V1 of the collector.
Well, it finally happened.
**Alex Boten** 31:30 Attempt number three. We'll get there.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 31:31 my fingers.
**Alex Boten** 31:34 Aren't we all?
**Jack Berg (Raintank, Inc. – Grafana Labs)** 31:38 Thanks, Alex.
**Alex Boten** 31:40 Yep.
Do you want to talk about the next… next topic?
**Jack Berg (Raintank, Inc. – Grafana Labs)** 31:44 Yeah, Ted and Alex have the next 30 minutes to talk about ABI, C and C++.
**Alex Boten** 31:51 I I don't know what Ted had in mind, but I I don't think my part of this is gonna take thirty minutes.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 31:57 Do one of you want to take over the screen share? If it's 30 minutes worth of conversation, there might be things you want to navigate around to.
**Ted Young (Raintank, Inc. – Grafana Labs)** 32:07 I think.
**Alex Boten** 32:07 I.
**Ted Young (Raintank, Inc. – Grafana Labs)** 32:08 Just put on as like a generic placeholder for, you know, giving one of these report backs.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 32:13 Oh, this is one of the project updates. Okay, I got it. Yeah.
Still, feel free to take over the screen share.
**Alex Boten** 32:22 I guess I can start. I don't really have anything to screen share, so you can just open up that donation proposal and we can kind of stare at it. Or you can stop screen sharing, whatever.
Okay, so I just want to give everybody a little bit of context on where this came from originally, and where I think this should be going. Ted, you can feel free to jump in and interrupt me at any point in time.
So, okay, so this donation. The original goal was to find ways to cut down resource consumption and prevent SDKs, this was specifically in Python, from causing applications to incur latency.
So my original starting point with this project was I wanted to look at ways to improve the performance of the Python SDK and through like a series of small improvements that were reviewed and merged thanks to the fantastic Python Maintainers. We did make some improvements, but there were still problems where like some amount of overhead from loading the SDK and some issues with the global interpreter log just couldn't be solved through the SDK alone.
So at that point, I started looking at this, you know, alternative, or monstrosity, depending on how you feel about it, which was to wrap a C++ SDK in a library called PyBind in Python.
Awesomeness. Thank you, Michele.
This eventually led to the donation proposal that's right in front of us here.
Something that should be mentioned as more functionality was implemented, things like including, so this was originally the prototype that I was working on was specifically for tracing, but the customer I was working with at the time was interested in better performance with tracing.
But, that's not where I stopped. As more functionality was implemented, you know, adding other signals, adding support for config parsing, additional exporters.
You know, the resource profile of embedding the C++ SDK in Python changed. For example, when I tried to bring in a gRPC exporter, the compiled library size went up.
When config parsing was implemented using the YAML library, the memory overhead went up because of how the memory was being consumed by the struct that was being loaded. You know, so I guess one of the benefits of adding more functionality was to provide parity across languages. That came at the cost of performance in different places.
So, I've talked to many folks across the community who wanted to participate in something like this, and so it sounds like there's at least a desire to have this, to support something like this for other languages than Python. So Python was just the thing that I was interested in, but, you know, folks have talked to me about, hey, is it possible to support this in Ruby, or Node, or whatever.
So, one of the suggestions in the proposal was also to bring in, like, an ABI, or maybe publish, like, a LibFFI-compliant library. I've done some testing around this, and specifically around LibFFI since, so this was, like, a few weeks ago. And I wanted to test out, like, a LibFFI approach in Python, Ruby, and Node. So far, my findings have been that, like, a LibFFI approach was.
would still provide us a better performance in Python, but the results from using it in Node and in Ruby were a bit mixed. Some places, either the performance was comparable, if not worse. I will caveat this statement with, I'm not an expert on LibFFI, so I have not spent a lot of time optimizing what that would look like, and I'm also not a Node or Ruby SDK expert. Diego, I'm… I will get to your point in just one second, I just want to finish.
The.
overall thing that I'm trying to say here.
So I guess… You know, at this point, what I would like to propose is that we kick off this project To bring all the people that want to collaborate on something like this together, and further investigate what paths are available to us.
questions that should be answered by this project are, you know, whether an SDK wrapper is the right approach, or an ABI, or something like LibFFI is the right approach, whether the back end of this should be using C++, Rust, you know, I'm not making a judgment here. And… It would also provide, I think the project would also have to provide.
like, the benchmarks that are used to make decisions for this moving forward. And ideally, this would also, you know, tie in nicely with the benchmark repository project.
And kind of like what I did here, I would love to find ways that we can improve the performance of existing SDKs along the way.
One question that I keep getting from folks when I talk to them about this is, you know, would this replace all the existing SDKs, all the native SDKs? And I think my honest perspective on this is that I don't think it will.
I think there's always going to be different use cases for different users. You know, our reference implementations are intentionally flexible because we want to support everything that OTel supports.
I would suggest that whatever this project ends up.
outputting is a little bit more specific and a little bit more targeted to support, like, the performance… the high performance, use case, rather than supporting the flexibility that reference implementations have to support.
Diego.
**Diego Hurtado (Dash0)** 37:40 Right, thank you. Thank you, Alexa. You guys can hear me?
**Alex Boten** 37:44 Yep.
**Diego Hurtado (Dash0)** 37:46 Alright, great.
Finally.
It's the first one. Okay, right, so I already… Agreed to, collaborate.
This project, and From the conversation we had… I had with Alex, I… I noticed that this, idea Of implementing part of… one language into another language is, I believe, very powerful. It can, have many positive outcomes.
And I think, Many people We'll probably be interested.
In… something.
using this approach.
refeeding a language into… With another one, right?
Now, I say this because this could have, applications, not only by… Making performance better, but also by solving problems with.
dependencies that some languages may have, right? So, I… I just wanted to… Tell you all this.
Because… All these, possible, Applications that this refitting may have.
may not necessarily be the ones that we investigate, right? So.
These, some people may get an idea that, we will be investigating refitting.
languages, with the intention of achieving X goal.
And that may not be the case. So, just, I will… Encourage people to get in touch.
Alex, I'll also be happy to help. If you have any idea, any application, so that we can discuss this and.
You know, evaluated among the many possibilities this, approaches.
Thank you.
**Ted Young (Raintank, Inc. – Grafana Labs)** 40:13 Yeah, I can chime in and because there's some discussion going on in the chat and yeah, just to emphasize the goal isn't to replace everything with C++. I think the goal is, we have, some reports that, you can look out, Korut put out stuff and, you know, benchmarks.
I think, was it Jirasi that said, I only trust the benchmarks that I've faked myself?
But nevertheless, you do get some languages at least where you can see that there's a lot of latency added to.
Latency added to applications when you add OpenTelemetry and a lot of resource consumption. Python's kind of at the top of the list.
And the question is, for people who really care about performance and resource consumption.
Can we provide them an option short of completely redoing the SDK architectures?
It would be cool to, at some point, revisit, you know, have, like, an SDK 2.0 discussion around all the things we've learned in production over the years, and, like, how we might want to redo the architecture for the SDKs, but that's, like, a really big lift.
And the question is, in the meantime, is it possible to provide people with an alternative implementation so you don't have to mess with the existing SDKs, but give them something else that requires much less effort in terms of getting to a high-performance solution?
And in exchange for that, maybe not giving them any options for this high-performance solution. We have one option that we're already giving people that's a very flexible framework. The other option doesn't need to give people all of these options. It could just be the, quote, you know.
Right way to do performant open telemetry in our minds.
And it can be the approach that, for that particular language, takes the least amount of resources. And that's what made binding to C++ attractive, because the C++ SDK is robust, it's been in production for a long time.
It has all of the signals, it's very complete, and it's pretty normal to do foreign function bindings to C++ in a lot of these scripting languages in particular, which are the languages that we're most interested in targeting.
But like Alex said, it doesn't… it's not like a magical unicorn. It doesn't automatically Solve all of your problems.
And it could potentially come with some problems.
But it seems to me that it's certainly worth investigating.
But I think it's, again, it's important to stress that maybe the point here with this SIG and this investigation is not to… try to use C++ as a hammer to turn everything into a nail, but just to go language by language and be like, for this particular language, are we seeing, like, significant performance degradation when you use OpenTelemetry, and if so, is there some quick fix that we could do in this language, some lower effort.
You know, approach that we could take that doesn't create some long-term maintenance burden to give people an option.
It might be improving things in the SDK in that language that don't turn into a big maintenance burden, but are just a one-time effort. It might be, binding to C++ or binding to Rust.
But I think it should be emphasized that the goal is just to give people a A fast path that doesn't necessarily have a bunch of options.
I'm curious what people think about that as a goal.
As opposed to C++ all the things as the goal.
Hey, Kelly.
**Michele Mancioppi (Dash0 Inc.)** 44:16 I think it's a good place to start.
The, My expectation is the moment that you have some success stories with the languages that are the most challenged in terms of performance.
Then others may follow suit. I also think that in the long run, having fewer SDKs to to support.
is… A small part of the biggest question we have as a project as a whole, that is the maintainership, the lack of maintainership.
Which Jack, for example, mentioned in the comments.
I'm very supportive of this effort.
I think we should be doing it.
**Ted Young (Raintank, Inc. – Grafana Labs)** 45:06 Yeah.
Josh?
**Joshua MacDonald (Microsoft)** 45:11 I want to add, just a little bit of support for the idea that even in languages where you have great performance on… for some uses, that you might find, cases where performance was not great. So, I'm particularly interested in hyperscale computer organizations where you have 256 CPUs, you know, a few terabytes of memory, and so on.
And if you have an instrumented application that's running on that entire machine, you really have to be careful with synchronization and sharing of memory across threads, and being specific about NUMA memory regions and so on. And I think that the experience we've had with the Hotel Aero data flow engine shows that you… if you have a machine like that, and you expect performance, you must do certain things. And that's going to require, a very careful design. I would like to be able to say, this is, like.
SDK 2.0 for hyperscale compute… for compute for, like, large-scale computers as well. Having an option to small… to substitute the small-scale SDK for the large-scale SDK, even in the same language, would be good, and I think that having an ABI that we could target for that sort of thing would be great, to have competition, so you could say, well.
here's your Python, you know, FFI SDK. By the way, if you're running on a thousand-core machine, you should substitute in the high… hyperscale SDK for that binding, and it should work better. And that's something that I'd be interested in seeing. I think we'll, SDK performance for large machines is going to be Something that we target. Thank you.
**Ted Young (Raintank, Inc. – Grafana Labs)** 46:52 Yeah.
And I can see something like that as, like, the first part of, like, what the SIG would investigate is, you know, there's some limitations around if we're… Saying, like, a solution is to bolt an SDK on through foreign function calls.
That itself raises some problems in some languages, right? Like, there's more than one way to do it in Python. Some ways of doing it are less efficient than others, and we see the same thing in Ruby and in Node.js and Ruby. The default way of making a foreign function call, has a lot Of cost related to just generating the objects going back and forth, for example.
So, you know, if you… if that's the… the actual… if the cost of making the call is significant enough, then it kind of doesn't matter how efficient the thing is on the other side of it.
So that would be a useful thing, I think, for the SIG to start with, would be to… Like, just figure out what languages there is, like, a viable way forward to have, like, a low-cost foreign function interface based SDK.
And the C++ SDK, for what it's worth, seems like a reasonable choice to start with. Again, if the goal is to, like, as quickly as possible, give people something better without… you know, having to spin up a whole nother SDK project or something like that.
Though I am super interested in the one you're talking about, Josh, and if what you're saying is, like, hey, there might be, like, this really advanced thing available in Rust soon that we're already working on.
you know, I could totally see that.
swooping in and being another option in addition to the C++ SDK. So I guess what I'm saying is I don't want to overemphasize the C++ aspect of this. It's just that that's the thing we… that's the bird that we have in hand right now, when it comes to trying this stuff out.
**Joshua MacDonald (Microsoft)** 49:01 Sounds good.
**Ted Young (Raintank, Inc. – Grafana Labs)** 49:11 People have any other thoughts? There was some discussion about optionality, in the… In the chat, and I think the main thing to emphasize there is something we notice is the more… The more exporters and options you give this thing, like, the bigger the payload is that you have to download, the more confusing it is in terms of, like, configuring this thing versus configuring the native SDK.
And that's, I think, why we're inclined to say, like, we don't want to be trying to recreate or give, like, complete access to every single option that might be possible to install, you know, in C++. It's more about being, like, giving people a hot path.
And maybe as a trade-off there, giving them less options.
And Alex is linking to…
**Alex Boten** 50:12 Yeah, the call route.
The overhead that you'd mentioned, for anybody who hadn't seen it already.
**Ted Young (Raintank, Inc. – Grafana Labs)** 50:19 0.
Add that into the docs.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 50:30 So how do we go forward from here? You know, this is still a project proposal, and, you know, what I'm sort of hearing is sort of a solicitation for more people to get involved, and such that this can move from, like, an issue to a proposal, and then, you know, maybe properly approved and spun up.
Is that, is that, is that what you, you, you see Alex and Ted? And if so, like sort of what?
What sort of interest level would be a signal for you that this is?
That this is ready to sort of materialize.
**Alex Boten** 51:06 Yeah, I mean, I think… I think the next step here is, to put together, like, a formal project proposal, get people to sign up on the project proposal and be supportive of it. You know, there's a few people on this issue that have already said that they're interested in participating. Diego's put his hand up as well, so I think… you know, there's, I think just creating the… Official project proposal, and it might be that we don't even end up taking this donation as it is, just because, you know, we might just start from The point of view of trying to identify what the best solution is before coming up with an actual solution, so…
**Jack Berg (Raintank, Inc. – Grafana Labs)** 51:48 Sure.
**Ted Young (Raintank, Inc. – Grafana Labs)** 51:54 Yeah.
For me, the case I would make is that even if it turns out there's some issues with Node.js and Ruby that make this not like, super beneficial in those languages. We do have, like, a pretty big problem in Python that seems beyond the ability for the SDK Maintainers in Python to solve.
Certainly without, you know, some massive rewrite of how the Python SDK works, at any rate.
And this does seem to potentially solve that problem in Python. And that alone seems pretty worthwhile, given… Given how important Python is in our ecosystem.
So that's just, I guess, one note I would say, even if it turns out that at the end of this investigation, we decide, it's really just Python where we're seeing a lot of the benefit, I think that would still be worthwhile to give people as an option.
Because, again, like, I don't think now is the right time to dig into, like, how do we create a second SDK architecture for people to go implement?
That, that seems like… a larger discussion than I would want to have. I'm looking more for quick wins.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 53:18 Well, so, I think, you know, we've got plenty of folks from the GC and TC here, so from a project process standpoint.
what I've seen in the past is, like, okay, this has some interest. I don't see anybody saying, like, no, this is a terrible idea. We still need to sort of solicit formal commitments from people to get involved, and that, to me, is the project proposal PR.
So, you know, it seems like you can proceed to that stage, unless somebody disagrees, and, like, see how the staffing shakes out. And, you know, if you get the staffing you want, then, you know, we can move on from there.
**Ted Young (Raintank, Inc. – Grafana Labs)** 54:04 Great.
**Alex Boten** 54:06 Sounds good.
**Ted Young (Raintank, Inc. – Grafana Labs)** 54:07 Sounds like a great next step.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 54:10 Alright, sounds good.
That was the last item in the agenda. Does anybody have any last-minute topics they want to try to squeeze in? We have 3 more minutes before we end, but we can also end early.
**Michele Mancioppi (Dash0 Inc.)** 54:26 I believe there was Andres in the beginning asking about the topic. He wasn't sure whether it was the right place.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 54:33 That was Mario, and we talked about this topic. That's the best fan processor topic.
All right, I'm going to call it there then. Thanks for your time, everyone. Nice to see your faces and see you next time. Thanks.
**Alex Boten** 54:50 Thank you.
**Ivo Anjo** 54:53 Thank you.
