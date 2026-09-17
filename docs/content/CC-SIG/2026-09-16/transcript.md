SIG: C/C++ SIG
Date: 2026-09-16
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Marc Alff [MySQL]** 00:22 Hi, Nikhil.
**Nikhil Bhatia** 00:25 Hi, Mark.
**Marc Alff [MySQL]** 00:46 Hi everyone, I Nikhil and Dug.
**Doug Barker** 00:49 Hey, Mark, Indico?
**Nikhil Bhatia** 00:51 Hi, Doug.
**Marc Alff [MySQL]** 00:53 Yeah, works better with, headphones, pour it on.
**Doug Barker** 01:04 How are you guys doing?
**Marc Alff [MySQL]** 01:06 Doing okay.
**Nikhil Bhatia** 01:10 I'm also doing good.
**Marc Alff [MySQL]** 01:12 Yeah.
I barely looked at OpenTelemetry today, so I don't know if there are any things to discuss. I noticed a couple, but I have not prepared a… My agenda yet, so let me go quickly.
**Doug Barker** 01:33 I just, copied some of the links so I can share.
**Marc Alff [MySQL]** 01:36 That's true.
**Doug Barker** 01:37 Mark, if that would help.
**Marc Alff [MySQL]** 01:39 Yeah, okay.
**Doug Barker** 01:40 Alright, one second.
So I think probably we can start with the one open item from last time. Do we still want to change these meetings to Monday?
**Marc Alff [MySQL]** 02:12 I think yes, because the Wednesday is not really working for me, but I haven't done the… I have not filed the community issue yet, so I still need to do that.
Could you zoom in a bit?
On the meeting notes? Okay, much better. Thanks.
**Doug Barker** 02:45 See if there's any here that need discussion.
Is the SIG store?
**Marc Alff [MySQL]** 02:50 Yeah, there's one I just noticed, so… After the release, it looks like I went to Verilyse and tried it in his environment.
And for… I don't know what is the real reason for that, but he's not using exception in his build.
And he noticed that now that the configuration core library is mandatory.
And because we use exceptions in it, yeah, the blue break.
So, there's this, this, yeah, this discussion about whether to… What to do, basically.
**Doug Barker** 03:25 Beautiful.
I know it's, at least for me, it seems like it's a broader issue that needs to be discussed, too. Like, what are the expectations when you build without exceptions, and which components Should we support that with?
**Marc Alff [MySQL]** 03:38 Yes.
**Doug Barker** 03:39 Because, you know, the truth of the matter is, like, we're using STL libraries throughout even the core SDK, so exceptions are a reality.
And if we turn them off, then we can't meet the requirements from the spec that, you know, the telemetry library shouldn't Terminate, or shouldn't… Crash, the main instrument and application.
**Marc Alff [MySQL]** 04:04 Yes.
**Doug Barker** 04:05 So, even in the API, I think we're using the STL libraries quite a bit that it can throw, so… you know, I don't know if this has come up before, but do you recall, Marc some of the The history on the no exception build, and what's driving that, about what the expectations are.
**Marc Alff [MySQL]** 04:25 It's, it's very ancient, so I don't know Why it was decided to do it this way.
from what I know, so, yes, we may be using the SLibrary, but otherwise, all the code so far in OpenTelemetry was not using exceptions, maybe with one or two lines somewhere as… For special cases, but, most… for everything, no exception were used.
And this is why we have builds that are compiling without exception support.
Now, on top of that.
when I did the file configuration with the YAML parser, I mean, the YAML parser, Not using exception is extremely painful, because then you have to check every return code of every function when you, Navigator tree.
And, in my opinion, it's not worth it, because you end up with code which is so ugly and so hard to maintain, but… It's very easy to miss a return code that you don't check, and then you end up with a crash anyway the day an exception is… should have been raised in the same place.
So, for the configuration parser, I used the exception.
With the understanding that, hey, this is a new feature anyway, so it's an optional feature, you may or may not use it, up to you, but if you use it.
The prerequisite is to have exception for the configuration file.
And the configuration parcel.
And… We had no feedback at that point, on that.
So, people… basically everyone was happy to… To build with exception if they are using the file configuration.
Because it was optional.
But now that the config core is… configuration core is… is no longer optional, OANT is bumping into that.
So… I, I think the… What we could do here is, make the configuration call library optional anyway.
To simplify the build.
But you are correct that it doesn't resolve the fundamental issue that Building without exception support is not a guarantee that a thing will be robust and will ever crash anyway.
**Doug Barker** 06:58 Yeah, I think that's… that's probably my… my core question, because it's… you know, even that, Bazel no-accept build already has for many years now, exceptions like the Prometheus exporter, there's all kinds of components.
But naturally have exceptions, so you… And currently, like, the resource detectors also throw and catch exceptions without any kind of… to compile those out.
I think, I agree with you. I think Making it optional again could be… the right path?
But my concern… I guess the promise of having a schema-based configuration, even programmatically, is that it standardizes that interface.
And it would be nice if we could drive users, eventually, to use that for all configures.
**Marc Alff [MySQL]** 07:49 Perfect.
**Doug Barker** 07:50 Yeah, even programmatically.
That would give us more flexibility to change the implementation details in the future.
with the SEK classes and instances themselves.
**Marc Alff [MySQL]** 08:02 Yes.
**Doug Barker** 08:03 So, my, I don't know, my… Ideal would be to keep it, Always, always building. And then the question is, is can we do so without exceptions?
**Marc Alff [MySQL]** 08:15 Yeah.
**Doug Barker** 08:15 Or, as a whole, do we still need to support a no-exception builder, or somehow… Share more about what you can expect when you do that.
**Marc Alff [MySQL]** 08:24 Guys.
**Doug Barker** 08:25 It seems like it's probably… if your goal of building without exceptions is you don't want your application to crash, it's almost the opposite. Now, if you build without.
**Marc Alff [MySQL]** 08:33 Well, it's… I don't know so much about Owen's environment, but looking at the very weird builds that he used to have in the past.
I don't think it's so much a question of whether you want exceptions or not, it's more a matter of Which compiler you use, and the fact that the compiler may have Incomplete support for exception, or no support at all, I don't know.
Because… He's also… Orwell was also using some extremely old versions of GCC, extremely old… versions of gRPC because of that, and things like that.
And my understanding is that this was, caused by the requirement of the tooling he had for… For his application, which was very, very old.
So it's not… it's not so much that it's a choice to… To build with or without exception, it was imposed by the tooling.
**Doug Barker** 09:41 So…
**Marc Alff [MySQL]** 09:42 But since then, So, I think Owen changed jobs, so I don't know if he's still working on the same application or not.
And the application also, has changed over time so that, he used to be very insistent of using C++11 only.
And later, it looked like C++14 was okay with him, so… I don't know.
What is the full story there?
**Doug Barker** 10:19 Well, just looking at what he proposed, I think we should rule out option one immediately, because by design.
**Marc Alff [MySQL]** 10:24 Yeah, yeah, no, no way. Never.
**Doug Barker** 10:26 report, and then I think you're advocating for potentially bringing back option 2 as a, as a, as an optional component.
I've… I propose looking at option 3, because I think, at least for all the builders, like SDK Builder, they all return smart pointers, so it won't be a big, heavy lift without… and it won't require a lot of API changes to have them just return null pointer if it fails and log an error.
I think the question will be on the document note, though.
**Marc Alff [MySQL]** 10:57 Oh, yes, it's… I mean, having returned code in the document node all over the place, it will just be so… Producing such tedious code, and… code which is fragile and bogus.
Because when every, every single, function in the configuration parser needs to return a return code now, and you need to check every single thing every time you access a node. I mean, it's… It will be putting us so much, Back in the past and backward.
**Doug Barker** 11:38 Okay. Well, I'll take a look at it.
and just see what the impact would be, because the document node class itself is the only one that Configuration Core needs in its interface.
Yes. Footprint is relatively small, so, like, certainly we should have exceptions in the YAML parser.
**Marc Alff [MySQL]** 11:56 Things like when a node is required, and we don't see it in the YAML document, we raise an exception saying, hey, sorry, node XYZ is missing.
Doing the same thing without exceptions?
Okay, so… you invoke a method that… to say, find me node XYZ, and then this thing returns a return code or a Boolean, and then you need to check it.
And if it failed, then you return a Boolean to the caller, and so on and so on.
Oh… But… I don't see us maintaining that code. It's, You end up with more error-ending code in the codebase than code actually doing the parsing.
**Doug Barker** 12:43 Alright, it kind of follows the typical pattern if you use, like, stood expected.
Like, a value or error return type.
**Marc Alff [MySQL]** 12:59 I mean, if there's a clever pattern to… should do that in such a way that the code is not too ugly, why not? We can… we can investigate that.
**Doug Barker** 13:10 Okay. Yeah, I think it's worth… it's worth looking into, because like I said, it… to me, it feels like the win is if we can shift all configuration, you know, to use the schema-based configuration, whether it's programmatic or YAML.
defines a, a spec-driven surface for actually configuring the SDK.
**Marc Alff [MySQL]** 13:29 Yes.
**Doug Barker** 13:29 It's non-optional, that's ideal, but… I think it's worth… At least a short investigation to see if we can make this document node in a… without it being too ugly, if we can make it exception-free.
**Marc Alff [MySQL]** 13:44 Yeah.
So, yeah, if we can, it would be great. My concern is really the… what the code will look like, and if it's maintainable or not.
**Doug Barker** 13:58 Alright. And then, what do you think, Marc? Like, separately, do… Should we define a policy? I mean, we need a policy for error handling and exception handling generally, but it seems like we need to set some expectations about if you're building without exceptions, you know, what should you expect?
**Marc Alff [MySQL]** 14:15 Yeah.
**Doug Barker** 14:16 The SDK does use, throwing, STL types all over the place.
**Marc Alff [MySQL]** 14:23 Yes, well, I guess we need to dig back in history and find where this… no exception code is coming from. If it's really… I mean, if there is a real reason for it, fine. If it's something that was… I'd done several years ago, one way, because of a reason which no longer applies today, maybe we can revisit it.
But, I don't know what… I don't know which one he needs.
There is a real, real use case to not have exceptions at all, or not.
Maybe Owen can also describe a bit why his pretty depends on that.
That could help you understand, you can taste, I guess.
**Doug Barker** 15:11 Okay, yeah, I'll post, after the meeting with, with kind of the next steps, and then ask Owen if he could clarify the use case a little bit more.
**Marc Alff [MySQL]** 15:21 Okay.
**Doug Barker** 15:38 So we had this one come in, and it's kind of related to this topic of the OTLP recordables, or these different recordables. We don't have a standard recordable type.
for all of our exporters, so the OTLP recordable has its own Performance characteristics, and on the recording path, it's… it's worse than the… like, native… C++ type span data class, which is the span data. We use that for the, in-memory and, Ostream exporter… exporters.
So… this, contributor did a profiling and kind of showed where the OTLP recordable is doing much more dynamic memory allocation.
Because we're recording directly into the protobuf messages, or the protobuf types for span.
**Marc Alff [MySQL]** 16:33 I don't know.
**Doug Barker** 16:34 And that is more costly, and that's also what I found previously. And we're not able to, say, record directly from a span into a protobuf message that can be exported, because of the way that Protobuff works, there… the export message that we create now uses an arena.
And that arena is not shared with the span itself.
And Protobuff has no way to, say, move data from one arena to another arena, or from the heap to an arena. So therefore, you are forced to do a deep copy, and that's where this whole… idea of, like, the fast path of recording directly into Protobuff and then immediately exporting it, that falls apart, because you have to do a deep copy no matter what. Unless… unless you're able to somehow have one big arena that you create up front, and then you always record into that, and the recording side, and then always export messages from that. But that's not the case now, and that would probably be a very complex and error-prone architecture if we tried to implement that.
**Marc Alff [MySQL]** 17:45 Okay.
**Doug Barker** 17:47 So… This is kind of the state that we're in now, is we have Protobuff, recording into Protobuff, but not the advantage of, say, a, a faster recording path, or a faster export path. It's… it's kind of… A hindrance on a lot of fronts.
**Marc Alff [MySQL]** 18:06 Yeah, and I guess because of a deep copy, well, not only we need to spend time to create all the data, doing a lot of memory allocations.
But on top of that, by the time we need to clean up.
There's also a lot of time spent doing, deallocation of every fragment of memory as well.
Right. Which… If you have a tree with a lot of complex things and attributes, list of attributes all over the place, and maps and things like this, it's… It's a huge structure. I don't know the photography arena at all, but… Looking at all the things we do, we have also some, for my application, we have some, Things like, memory pools that we can allocate from, and, at the end… so everything… when everything is allocated from a, from a pool, There is no need to delete every single pointer individually. The pool is just destroyed, and everything which is in it just goes away at once.
And this saves a lot of time, destroying… A very complex structure, which is where everything needs to go about together, anyway.
So I'm assuming that the the Polybuv, arena, works the same way. It's easy.
Not only do you allocate from a different place, but also it's easier to tear down.
**Doug Barker** 19:32 Yep.
Yeah, that… that's right, and that's the advantage of using the arenas, and they are… they are much better than just, say, using the dynamic allocation for every… every single attribute, or every single string, or… or value that goes into the protobuf message, so it is faster that way. It just… is, it's more expensive to record into… even with the arena, it's often more expensive to record into that structure than it is the normal C++ types. And one of the… the spec requirements that we're currently missing, which I think is an important one, is enforcing the unique attribute keys. So, with the protobuf message, it's just a flat, like, vector of the key any value types for I did some prototyping to try and see if we could implement, enforcing unique keys on recording. I think enforcing it on recording is important, because we want to still maintain the span limits and keep any kind of growth Memory from spans or recording attributes, you know, limited.
And… that means that you need to check or enforce it on recording. That happens with spam data, because we use an unordered map, so it naturally hashes and And… has unique keys, but the protobuf message is not that way, so if you had a loop that just wanted to set an attribute.
With the same key, and many different values, it's gonna duplicate those.
Over and over again. Eventually, if you have implemented the span limits, it will… stop updating, but you'll no longer get the most recent updates of that value. You will get, you know, whatever the The limit was that you hit, typically 128 attributes.
**Marc Alff [MySQL]** 21:28 Okay.
**Doug Barker** 21:29 So, I think this one's important to fix. It's gonna be hard to fix with this protobuf type, though.
Because once you implement something that actually checks the keys, the performance degrades pretty rapidly.
**Marc Alff [MySQL]** 21:46 And, I think this came up before, and with some discussions on it, the… One concern is to be able to.
Just unplug that, that code that enforces uniqueness.
Because it's, It detects applications which are poorly instrumented, which are reporting the same attribute over and over again.
But once your application is clean and instrumented properly, it's typically the kind of things you want to avoid doing in production all the time.
So there's, I don't recall the discussion, but I think there was some, desire to… Yes, it's okay to enforce uniqueness, but as long as there is a way to unplug that.
**Doug Barker** 22:33 Yep.
Yeah, so that's kind of the, I guess, the gist of this one. So the contributor has added an arena to the span and log recordable.
it doesn't… necessarily solve the, you know, it improves some, like, reduces the dynamic memory allocations, but it has its own trade-offs, because now you're spending more time allocating a big hunk of memory that you may or may not use. So they've been, you know, testing with different, size arenas.
So, it comes with its own challenges, but… I marked this just for discussion, because I think… long-term or near term, we need to look at replacing these credible types with something else. And the other reason for that is that this multi,
**Marc Alff [MySQL]** 23:27 Military exporter, yes.
**Doug Barker** 23:28 Yeah, multi-exporter, multi-processor use case. It's almost, you know, if you care about performance, you're just not going to have multiple processors with OpenTelemetry CPP, because it's.
**Marc Alff [MySQL]** 23:37 No.
**Doug Barker** 23:38 Duplicate me.
**Marc Alff [MySQL]** 23:40 I'm still not getting the use case for multiprocessors and exporters, I mean… This is, like, you know upfront that you are exporting data to two different places, and on top of that, you know that you want some Different attributes, or different sampling, or different something, so that it's not the same data sent to In both places, but it needs to be processed.
in parallel.
All the way, this is a very weird, use case.
**Doug Barker** 24:15 Yeah, the main…
**Marc Alff [MySQL]** 24:16 And also, yeah, and also keep in mind that this is also the kind of features that the OpenTelemeter Collector can do, so… Right. Yes, if you have a collector, you have yet another process, and that needs resources and so on, but at least the data comes out of the application.
In one stream.
And then, outside, you can slice and dice it and send it to multiple backends if you want to.
**Doug Barker** 24:44 Yeah, I think… I think that's certainly the case, and I feel like this event to Spranbridge definitely fits in the collector more than in the recording path.
But there are cases, like, if you wanted to implement your own filter that filters based on something other than the severity, or if you want to add in a sanitizer or something that, within the process, you know, is filtering out data that you don't want to.
be sent over the network. This is an important use case, and certainly the YAML configuration and the spec supports these kind of.
**Marc Alff [MySQL]** 25:17 concentrated.
**Doug Barker** 25:18 responsible.
**Marc Alff [MySQL]** 25:18 Yep.
**Doug Barker** 25:20 But our implementation would make it such that, you know, implementing something like this, you basically have to replace Batch Processor with your own wrapper around this, and then create your own pipeline inside, so… Anyways, I bring it up because I think it's all tied to this, design choice of having each.
**Marc Alff [MySQL]** 25:43 showing.
**Doug Barker** 25:43 Or define its own… exportable type, or recordable type, and if we can standardize on a faster, you know, a better type that's good for recording, and can be exported to OTLP, or Ostream, or whatever.
Then we can move closer to being able to support.
this use case.
**Marc Alff [MySQL]** 26:04 Yes.
**Doug Barker** 26:07 So…
**Marc Alff [MySQL]** 26:09 Okay. So, yeah, definitely something we need to investigate and discuss. I have not looked at the PR itself and all the discussion, but it's, Yeah, something intricate.
**Doug Barker** 26:33 I think some of these we probably have already discussed. We can remove the flag.
label.
Yeah, I think probably the one that… Still needs review, is this one.
Again, this is metrics, so maybe… And the leg can help.
**Marc Alff [MySQL]** 27:12 Yeah, I don't know matrix that much.
I'm using metrics, but in a very special way.
OpenTelemetry has synchronous and asynchronous metrics, and I'm only using asynchronous metrics.
So we've, this is just for the data collection itself.
And aggregation, all the things you can do on a metric, I'm not using it currently, so I'm… I don't know all the… All the stupidity is there.
And I know that there are a lot.
With histograms and whatnot, and…
**Doug Barker** 27:59 Take a look at this one, because it might… it might be related to your application. It's basically this async… these async attribute sets, like, once you record an attribute once to an async.
metric, it stays there for the life of the process, and this change will allow them to be to be phased out, so if you don't record an attribute set for a given recording cycle, then it will be dropped from the export, and that's what this one does. So that… this may be important for your use case, then.
**Marc Alff [MySQL]** 28:30 True.
**Doug Barker** 28:35 Okay.
**Marc Alff [MySQL]** 28:37 Yeah, this one, I need to take a look. It will be definitely a very shortcut to make the code more efficient.
We absolutely should do it.
**Doug Barker** 28:51 Yeah.
I'll, I'll ping Tom.
this one, but I think hopefully this one's straightforward, but this is… performance optimization for the drop agitation that we should have.
Yes.
**Marc Alff [MySQL]** 29:09 I think I recall a PR talking, doing something with exemplars.
Where there was a discussion about, how to… Cool.
When we offer a measurement, whether we can take a shortcut for the drop aggregation or not, things like that.
And the discussion at some point was quoting, Pieces from the spec itself, saying, oh, the behavior should be this, the behavior should be that.
I agree. One thing… so, the spec tries to define what the functional behavior is.
So, if you have input A, B, and C, and in that configuration, the expected result is that.
But it's by no means a design and a way to implement the code. So, if we find a code which is doing exactly the same output for exactly the same input.
And if it's implemented differently, for example, by dropping By not even considering measurement, if we know that, Mmm… The data will be dropped anyway, we can take shortcuts.
So, all that to say that when the spec says something, It does not mean, at least in my opinion, that the code should be architected and coded that way.
**Doug Barker** 30:36 That makes sense. Yeah, and I think that the good thing is the spec, especially around drop aggregation, it was recently updated, I don't know when maybe a couple releases ago, but it now says that if all of the views of an instrument have drop aggregation, then the instrument should behave as if it's disabled. So that would support, you know, doing zero work.
**Marc Alff [MySQL]** 30:57 Yes, yes.
**Doug Barker** 30:58 In that case, so… That one, I think, even our implementation can be aligned with the spec.
**Marc Alff [MySQL]** 31:05 Okay.
**Doug Barker** 31:13 Nikhil, are there any, PRs that you want to review?
**Nikhil Bhatia** 31:17 No, Doug, nothing as such.
**Doug Barker** 31:21 I know that you had one, did that get merged already?
**Nikhil Bhatia** 31:24 Yeah, that got merged.
**Doug Barker** 31:26 Okay.
**Marc Alff [MySQL]** 31:27 Okay, great.
**Doug Barker** 31:29 Are there any that you're, interested in taking on next?
**Nikhil Bhatia** 31:34 Yeah, I'm going through some issues, I think I'll, Keep a comment on what issues I'll be taking up next.
**Doug Barker** 31:42 Okay.
**Marc Alff [MySQL]** 31:44 Okay. So, one thing that happened recently also… so, first of all.
I guess you know that, because you did the review, but so we just released, OpenTelemetry 29?
And the size of the changelog was just huge compared to previous releases.
I don't recall the exact number of PRs that went into this, but it's very massive.
So, a lot of changes there.
We still have the issue of, Well, keeping up with all the PRs that we have, and… To do something with them, and review them, and… Presumably, if it's okay, merge them. So, still a lot of backlogs to process.
In the meantime, also, the configuration… the configuration repo for the YAML configuration also just made a new release recently.
So, there is a new schema, which is schema 1.2, which has a couple of changes.
So, we will also need to adjust and implement, those changes. From memory, There is a new, composite sampler, which is to always record something.
So we need to implement it.
There is also something for views… for metrics, sorry, where an exporter can have a default, aggregation?
Specified somewhere.
And, also something that was detected a while ago.
In the OTLP exporters, I think there are new parameters to specify the minimum and maximum… well, minimum, I don't know, but the maximum size of a request and a reply.
So we need to capture those, and… well, at least in the YAML, and then see if we can implement that in the SDK to support those configurations.
So it's still… It's still changing, Not that many changes, but we still also… we need also to, Keep track of the most up-to-date schema there.
**Doug Barker** 34:07 Yeah, that makes sense, and we saw a few, things from the old the previous schema that we can complete. I was looking at the… OTLP file.
exporter configuration. It has, like, a parameter that should default to… exporting JSON to standard out, and we currently don't Use that parameter so that… To be one, also to complete, Given… given the comment, I think you're… you're right, Mark, we have 52 open PRs is probably the most we've had in a while.
Should we… continue to log issues for things like that, and accept new PRs, or should we get a focus here on… Driving down and getting some resolution on the 52 that we have.
**Marc Alff [MySQL]** 34:57 Well… the way I see it, so if there is an issue, first of all, if someone logs an issue, and the issue is valid, we should keep it.
Whether we fix it right away or it needs to wait, it's a different story, but at least it's a valid… if a report is valid, we should, keep issues and not discourage people from reporting existing problems.
So, unfortunately, it creates a lot of, issues which are piling up.
And the second part is, once we have all those issues piling up, some people are writing PRs, which are… which is a good thing.
But now, of course, we have a lot of them to consider and to review, which is the main bottleneck.
Other reports have implemented some limiting folding features, like, oh, there is an option in GitHub somewhere that says.
You can… you can restrict a user from having too many open PRs, for example.
I don't want to use that, because I think it would be counterproductive, I mean… First of all, it doesn't affect so many people, it's one or two users who is very positive with a lot of issues, and also… if we start doing that, instead of having 10 small PRs, we would have one big one with the same code inside, and… And an issue which is harder to… To review and to merge, because, There is no way to merge the fix for issue 1, 2, and 3 if there is some some discussion on Issue 4, so I don't think we should go that way.
So… I'm okay with having a lot of issues and a lot of PRs.
It's, we need to find a way to deal with that, but… I don't think we can do much about it, anyway.
**Doug Barker** 36:58 Yeah, I think that… that makes sense, I agree with that. So, just leaving the limit.
**Nikhil Bhatia** 37:03 Oh my god.
**Doug Barker** 37:04 unlimited as is, and then trying to do our best to keep processing these. One area that I've seen, and it's often when somebody requests a change.
But then… the, the follow-up may take a long time, yeah, so…
**Marc Alff [MySQL]** 37:21 Yes, yes.
**Doug Barker** 37:22 If the, if the contributor… addresses the changes, it may take a while, you know, maybe many weeks for the reviewer to come back and look at it again.
And…
**Marc Alff [MySQL]** 37:34 Yeah. I've seen this pattern, and it happens a lot, first of all, with new contributors.
Because they may expect that, hey, the PR is written, we just take it and do nothing else. The contributor does not need to do anything else about it.
So this is one thing, and… the more we wait to give initial feedback as well, I think increase the likelihood that the contributors are disengaged and will never reply.
So Maybe we should, when a first OPR is first, filed, Well, I mean… I try to read a lot to see what is going on there.
But unless I have reviewed comments, I tend to not say anything, so maybe we should make an effort to at least acknowledge that, yes, we have seen the PR, we are investigating it, we are looking into it, and… And maybe with a… with a word saying, okay, it may take some time, but we are not forgetting it, we are looking at it.
At least it will keep, The contributor… well, the contributor will know that we are actually looking at the code and, Oh.
Prevent people from, going away and looking at it elsewhere, maybe.
**Doug Barker** 38:57 Yeah, I think that makes sense. One thing I've seen, some of the other SIGs doing is this, I think it's like a PR dashboard, it might be a bot or something, but it… will comment on PRs and say, like, who… who… what the PR is waiting on. Either it's waiting on.
**Marc Alff [MySQL]** 39:13 Games.
**Doug Barker** 39:13 or it's waiting on a reviewer. Now, certainly that's going to drive a lot of work.
**Marc Alff [MySQL]** 39:17 No nuts. Yes.
**Doug Barker** 39:19 what we want, but maybe that's… that's something to consider, to at least, like, have it be clear what the PR is waiting on.
**Marc Alff [MySQL]** 39:26 Yes, and that came up before. I think for some PRs, touching especially the ETW code.
There are some piers there where the status is not even clear. It's… looking at the history of comments, I don't even know if… It's waiting for a reviewer to finish the review, or if it's waiting on… Implementer to… To… do a change, It's… the status of it isn't clear, and this is why PR… some PRs are falling away… falling apart.
**Doug Barker** 40:07 I've also seen some of these have, like, a stale flag, and there are some other states will automatically close stale PRs. Is that something that… Yes.
**Marc Alff [MySQL]** 40:16 So, that… so, this is something that actually I disabled a while ago. Okay. So there is… There is a process which is tagging things as stale automatically as a way to notice, to note that, hey, nothing happened on that PR.
And then the same process, when running again, after a grace period, will just close automatically things.
And… from, a contributor point of view, this is extremely frustrating, because you do a PR, you get zero comments.
zero… Zero comments, zero reviews, and then it's closed, and… You don't even need… you don't even know if it's closed because it was bad, or if it's closed because nobody had time to take a look at it.
And it gives the impression that things are flowing because PRs are not stacking up and they're getting closed, but… The point is not to close PR, the point is to merge them. So…
**Doug Barker** 41:20 True.
**Marc Alff [MySQL]** 41:24 I had the… had the same case in, And also, keep in mind that, it takes some privileges to reopen an issue or a PR, so once your PR is closed, you cannot even reopen it. You basically need to take the code, file another PR again, to… Bring the issue up again.
Which means all the discussion, if any, is lost, and starting from zero, and I don't see that as a good process.
**Doug Barker** 41:55 Yeah, I think that… that makes sense.
Okay. Well, it sounds like there's probably nothing to change immediately about the process other than… Yes.
you know, maybe we can just keep adding comments to PRs to try and…
**Marc Alff [MySQL]** 42:13 Yes.
**Doug Barker** 42:14 Both either reviewers or, contributors.
**Marc Alff [MySQL]** 42:18 So, one thing which is… to say is that, depending on the subject, some PRs take the fast lane, and some PRs are waiting forever.
Typically, code cleanup to fix warnings, those get reviewed very quickly and make it and are merged.
And go out of the way. So, things like this, because of their nature, it's easy to approve.
A review approved, and the code is covered by CI, so you see if it's working or not.
Other things depends on each area. Typically, for all the YAML code in the file configuration, you and I are both very, Knowledgeable about that codebase.
In fact, I don't even know if my name is Sylvian Giedblame, because of all the code you moved.
So, But we… when there is a change there, it's easy for both of us to take a look at it, because we… this code base is fresh, we know it, and then get the PR approved and moving.
But, another example is for metrics, for example.
Personally, I don't know metrics so well. I might know a little bit, but not enough to improve a PR.
And in that case, the PR is waiting, basically because we need reviewers.
Oh, no, Viteria.
And so this is true for older parts of the code that Lalit and Tom touched.
Earlier, or even parts that, are way, way more ancient.
And so for things like the ETW exporter, for, There is another exporter also that we, But I've never used and rarely, rarely used.
Various metrics, and a couple of, couple of areas which are, We're getting reviews and making progress, he's all the…
**Doug Barker** 44:27 Yeah, I think probably the good thing is that there are more people contributing to metrics, so hopefully we can promote some contributors to reviewers. We certainly need,
**Marc Alff [MySQL]** 44:36 Yes.
**Doug Barker** 44:37 Need… need help in that area.
And, Nikhil, that may be one area that you can help in if you see some, you know, we certainly need help reviewing PR, so if you see a PR that has been stale for a while, and you think you can add some feedback, you know, feel free to comment and share a review.
**Nikhil Bhatia** 44:56 Yeah, sure, Doug.
**Marc Alff [MySQL]** 45:00 So… One thing that seems to work well is, every time we advertise some Easy… I forgot the name of the label, but… oh, good first issues and Al Pantody Shoes.
People tend to pick them up very quickly and provide some, some PR.
So, the question is, So, first of all, we need to have a lot of… a couple of issues ready for people to pick, so… Always advertising them in the… in the contributor welcome issue, so people can see them and it's easy to pick.
Maybe we can also… list issues in areas that, first of all, we know that it needs to be done, it is obvious, but not only that, but also on areas where we know we have the capability to review it.
So this has been working well for, YAML configuration, for example.
Hmm.
Because if we… if we know… if we ask for some… someone to contribute and help… with Help Wanted, and end up with a PR that we don't know to review. It's, it's not efficient. Otherwise, if we ask someone to contribute in an area that we basically know the code, we basically have an idea of how it should be done, it's only a matter of time, because we don't have the bandwidth to write the code itself. At least, we have a good idea of what should be done, so… Therefore, we should have a good idea of, how to review the PR and provide useful feedback, so that it's, It's more likely to proceed and be approved and merged.
**Doug Barker** 46:54 Yeah, that makes sense. I think that the actionable thing there that we talked about from last time is to focus on all the clank tidy, wrapping up.
**Marc Alff [MySQL]** 47:03 Yes.
**Doug Barker** 47:03 So that's… that's one area that we can, Continue to log issues on.
And then…
**Marc Alff [MySQL]** 47:10 In performances.
**Doug Barker** 47:11 Yeah, performance, and then also the YAML configuration, there's still a few, Schema items that we can support.
Okay.
Is there anything else, Mark, that you wanted to cover?
**Marc Alff [MySQL]** 47:33 No, I think it's… this is it for me.
So, trying to… to stay afloat with all the… all the PRs that we have.
And also stay afloat with other things which are going on, because I'm not only working on OpenTeometry as well, so…
**Doug Barker** 47:57 Okay.
Well, like you said, there was a lot of, a lot of improvements to the last release, so looking forward to getting feedback on that, moving towards the next one.
**Marc Alff [MySQL]** 48:07 Oh, yes, there's only one thing, so, two things, actually. So… For Owent, complaining about the compiling with or without, exceptions.
So… We need to decide what to do, but, Technically, this is a regression compared to what we used to advertise before, so… But… Like, namely, before you could build without exception, now you cannot.
But, the fix itself will take some time and some discussion, so I don't think it's, The question is basically, do we need to, do risk fix quickly and do another release of version 29, like, say, a 29.1?
To fix that.
Would think not.
I mean, boo.
First of all, it depends on, what Ovent would like to do exactly, I don't know if he's… We need to see his use case.
But in any case, once we have a fix, he's also capable to cut his own branch if needed, and so I don't think we should make a new release just for that.
Of course, if someone else complains that it's a break, which is affecting them, we may… reassess and see where we are, but I don't see this as a pressing issue so far.
And the second thing was, there are some open deprecations which are, getting… ready to be implemented, because we said a couple of things will be removed in October 1st.
So, I will probably, file a couple of PRs to remove You know, those things, the plant removal part.
I'm on purpose waiting at least after the date there.
I don't want to… to have a PR that remove something merged today in September, because it prevents us to do a new release in emergency if we need to.
But after that date, I will fix those three things and clean up the code there.
**Doug Barker** 50:25 So, do you expect any changes, with respect to these three planned removals, or…
**Marc Alff [MySQL]** 50:31 Just could clean up to… to just drop the options and cut the code there.
This thing has been advertised long enough, people should be aware of that, and… We had some pushback in the past.
With some changes, people complained that, hey, you are changing that it was not advertised, and it's breaking me.
So this is why, there is this whole deprecated document to clearly say in black and white, hey, we are announcing that we are removing this and that and that, to let people know, It's so that it is documented, and then after 6 months, when we finally say we remove it… when we finally remove it after… after having said that 6… 6 months earlier, we… The point is to do it, and then… If someone complains, at least we can point them to the… notification that was posted, well earlier, so Adwee should be aware of it and should have said something.
**Doug Barker** 51:41 Yeah, I think that makes sense.
And this has been posted since April, looks like.
**Marc Alff [MySQL]** 51:46 Yes, yes, yes.
**Doug Barker** 51:50 Okay.
Yeah, that sounds good. So I think, Ben, we're still… on track.
To have a, release sometime in… October, and then, like you said, we can address the exception handling from configuration for that release, and then address these removals.
Have some performance improvements, and then hopefully have the, cling tidy, issues to zero.
**Marc Alff [MySQL]** 52:15 Yeah, that'd be nice.
**Doug Barker** 52:20 Cool.
Okay.
**Marc Alff [MySQL]** 52:25 No fingers for me.
**Doug Barker** 52:27 Yep.
**Marc Alff [MySQL]** 52:29 Thanks for joining, and thanks for hosting, as well.
**Doug Barker** 52:33 Yep.
**Marc Alff [MySQL]** 52:34 Thanks, Nikhil.
**Nikhil Bhatia** 52:37 Thanks, Mark.
Thanks, Doug.
**Marc Alff [MySQL]** 52:40 Okay.
**Doug Barker** 52:41 Have a good day. Bye, guys.
**Marc Alff [MySQL]** 52:42 Bye. Bye.
**Nikhil Bhatia** 52:44 Bye.
