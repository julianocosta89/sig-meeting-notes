SIG: Swift SIG
Date: 2025-10-30
Duration: 41 minutes
Zoom Recording URL: https://zoom.us/rec/share/YWNwStG6OSZ2LOHCD_xtd1bxhen4e59lqCqeTV1ulLp6mDVvJzj8Bg5xR-FyvVuo.UtaZx0ieZGgaWmCl
============================================================

## Zoom Recording Transcript

**Bee Klimt** 02:21 I saw Bryce is out this week, so I don't know who's gonna be in charge of this meeting, or if anybody's gonna show up.
Hi, Billy, thanks for the, feedback on that PR. I'm gonna address it today.
**Billy Zhou** 03:04 Thanks, it was super good. Thanks for the contributions.
**Ariel Demarco** 03:15 Hi, Ellen.
Okay, I think… We are all.
Us… So… I think we can start.
I'll share my screen Is everybody able to see?
**Vinod Vydier** 05:09 Yep.
**Ariel Demarco** 05:11 Okay.
So… From the last week, We have a cocoa pots issue.
that there's a compilation error. I was able to look at it.
Let me open… the repo.
I was able to fix that.
So there's a pure app.
Here.
Alright, we'll just… basically… the issue with the PR.
Is that… first of all, the versioning in this way, it was always gathering 2.1.x, so it wasn't able to get the dependency for 2.2.0. And as we made some changes in the OpenTelemetry codebase when… while using SPM, This wasn't compiling, so I did the two things. First of all, remove the patch.
As we already are using the newer version, I just bumped the minimum version.
So that's basically… the change of this PR, I'll include it.
in the notes, so… maybe UV not.
Can take a look at it afterwards.
**Vinod Vydier** 06:30 Sure, sure.
**Ariel Demarco** 06:31 Europe.
I don't remember which was this.
Oh, this is already merged.
already merged.
I made some comments, because they were just launching on iOS, on… sorry, on SPM, but… they were able to also include that in CocoPots. And at the same time, they fixed a bug because it wasn't being published on macOS, so hopefully now we also have a CocoaBots version in macOS.
Billy, this is… this was you?
**Billy Zhou** 07:06 Yeah, so, for crashes, I implemented KS Crash Reporter, but, I'm not sure exactly where to put it, to be honest.
We don't want to add KS crash into the main repo, so… Yeah, I'll have to think about where exactly to put it, Yeah, I have a good implementation, though. It recovers the, original crash context, so it'll keep, it'll be backfilled to the original session and the original timestamp.
Instead of just whenever you observe it, And then for Metric Kit, yeah, I spoke to B, and then Bea went ahead and put out a great PR for it, so thanks, Bea, for that.
I think that's pretty much it. Yeah, when I put out the PR, I'll definitely add you guys to it, and also Alex, what we discussed last week.
**Ariel Demarco** 08:01 Right?
We hope to see that.
Next release, well, the next release is waiting for the PRs to be merged, so… If we can nourish the different VRs that are up, I can go and do them.
I'll probably be doing 2.3.0 instead of a patch, because of the changes on the minimum supported platforms, so I'll probably do Version 2.3.0.
That's all from last week. New topics, B, any feedback or discussions on the metric EPR?
Let's look at it.
Together.
I saw that it wasn't really compiling. I added some comments. I don't know if you had a chance to, look at it. I think… So, Billy made some… added some comments.
regarding… yeah, channel.
**Bee Klimt** 09:02 For the compile error, it seems like the two options are drop macOS support or update the compiler that we use in CI.
**Ariel Demarco** 09:10 Yeah.
**Bee Klimt** 09:11 feel about those?
**Ariel Demarco** 09:14 Yeah, it's… I think that maybe we can try out using Xcode 26 for testing.
I think we tried it out at the beginning, but we had some problems, but it was because of the runners, not because of Xcode itself.
Alex, I think you did something similar on our SDK. Do you remember if this is working just fine right now?
For XL26?
**alexcohen** 09:42 We've got, We run on latest, so 15 and 14, the runners, I don't know if those are the actual macOS versions, and we run with Xcode 16.4 and 26.
So it should work. Obviously, there are gonna be, like, availability issues that you need to… to take care of, but it should work. It requires a, like, more work than usually it's worth it, but for us, it was worth it. I don't know if it's… if it's worth putting that work in here, to get it maybe for tests, we can just, like.
Support what's needed just to make sure it runs through.
**Ariel Demarco** 10:24 Okay, but it seems to be working on our end, with 26.
**alexcohen** 10:31 Seems to.
Yes, but I spent too much time on CION.
Everyone agrees that the GitHub runners are pretty… pretty crappy, especially for… for macOS these days, sometimes.
iOS versions are missing, they're not installed, they're, like, so, it's… it's such a… Yeah.
such a mess. I would get one work in that works well and… and go with that.
**Ariel Demarco** 10:59 Okay.
Okay, so it seems that unless the new runners have the simulators, that I think it was the actual problem that we had last time we tried out.
It's going to be kind of a bummer.
I really don't know how to fix it, because what I checked out is that it seems that every single macOS SDK from… from Monterey until… The new one? No, no… None of them has the metric payload.
interface available for macOS.
So there are two things that we can do. Maybe we can just run those tests in the meantime for iOS only, and that's it.
I know if you have something to detect if you put your own CI.
**Bee Klimt** 11:49 So…
**Ariel Demarco** 11:49 On… on the codebase.
**Bee Klimt** 11:51 It's not just running the test, though, because it won't build, so I think we would have to… We could disable the metric kit instrumentation for macOS entirely until the build tools on GitHub are updated.
**Ariel Demarco** 12:08 orange.
**Bee Klimt** 12:08 I mean, the other option is to somehow make the compilation conditional if you're building for tests, but I'm not sure how to do that.
**Ariel Demarco** 12:16 But you're right that if we use this to build for CocoBots, it's going to break.
The CI. You're right.
Hmm.
Yeah, maybe it's a good idea until we bump to use entirely Xcode 26 in CI to get rid of this. I can work on that, and see if I can make the CI work with OS with iOS 26 and macOS 26, but I cannot promise that it will work. As Alex said, it's a bunch of stuff.
It's painful, and if we also have to download Simulator, it really… adds a bunch of minutes of usage in the CI, so everything becomes slower, so I'll try to see if I can make it work.
**alexcohen** 13:05 A quick question. Does it… does it work on iOS? Are we okay on iOS? Does the CI work? Just… just remove the availability for macOS and get it work… let's get it working nicely for iOS, and then after that, we can focus on macOS. I don't think there's any reason to… to… to not.
**Ariel Demarco** 13:24 delay this.
**alexcohen** 13:25 because it doesn't work on one platform that just became supported with Metric Kit anyway, so, I mean, let's get it working on iOS and then get it working on the next platform after. I think that would be, that would be a good compromise here.
**Bee Klimt** 13:38 That makes sense to me.
**Ariel Demarco** 13:40 Yeah, same.
I'll write it down here.
I'll do an edit.
To just… Edit.
removing macOS support until… we fully migrate to Xcode 26, and CI.
CI. CICI. CICD.
Great.
there are some comments, I think, from Billy.
**Billy Zhou** 14:19 Yeah, sure, I guess I can discuss those.
First one was just about exception.stackTrace.json. I guess for this one, like, we can just add the new… the metric kit stack trace format to the, list in stack trace representation, and, I don't know if we need another, Feel for it, because of the different formats already implied.
And, the second one is, I remember there was some discussion about just capturing MX metric as, a metric. Like, the way, B wrote it, it looks like it's, like, you can extend this to support metrics in the future. Just wanted to capture that, and then, I think the last one was, I don't even remember, it must have… if you… can you scroll down a bit?
**Ariel Demarco** 15:11 Yeah, sure, sure.
**Billy Zhou** 15:12 And, oh yeah, like, we are… I've also been, like, kind of discussing this issue with, like, some of my team, like, like, I wanted to, like, create, like, good crash messages that are, like, able to, like.
group root causes together. It seems like sometimes, like, these messages, like, aren't good enough for that, so I just wanted to call that up. Yeah, there's very small comments, those are the only things.
**Ariel Demarco** 15:36 Okay, I have an opinion on this one, on the exception stratace JSON.
I wouldn't submit this one as the… to the semantic convention. If you read the other ones, like the ones in Python, in Java, and etc, they are the ones that print a simple stack trace. I think in iOS, it's something like… thread.callstack Symbol, or something like that.
I would use this one for the semantic convention.
the why metric it is using this other one, I think it's for the… it's because whenever they have sampling data, they… they show you how many times a method was executed when showing metrics, that's why they need this kind of tree structure, but… I don't… I don't think that… If we want to push this to the semantic convention, that should be the structure.
I… I have no objections on providing the original one, because anybody using Metricit will… will know that it uses that called strict… that's… that tree structure, rather than the… the normal… cold stack that.
iOS provides.
**Billy Zhou** 16:51 I see, because that's not really a normal stack choice, like, okay, that makes sense. Yeah, in that case, just go ahead.
**alexcohen** 16:58 I agree with Ari here. I think… I don't know… I'm not exactly sure, if we're talking about symbolicated or unsymbolicated, but it feels like the stack trace here should… we should parse it out to be just an array of arrays of… Of ink pointers, or 64-bit ints, like the addresses of the stack traces in each thread.
**Ariel Demarco** 17:24 Yeah.
**Billy Zhou** 17:24 I think… I don't understand.
**alexcohen** 17:26 It's not like that on every platform, to tell you the truth.
**Ariel Demarco** 17:31 it feels like on iOS or any Apple platform, that would be the basic way that.
**alexcohen** 17:36 any… Back-end would want to receive, stack traces, so they can symbolicate them easily. And if there's… if there's more to it, we should probably also add the image binary address and offsets and things like that. And I know that, the metric one has them, but, like, reformat them so it's basically a simple… simple arrays.
of addresses.
**Bee Klimt** 18:02 So, I think my, my concern's here, One concern about parsing them like that is I believe in the documentation, Apple doesn't really document what this JSON format is, and so I'm kind of afraid of them changing it on the future, and the… It's harder to adjust for that on the client than it would be parsing it on the back end, so I'm a little nervous about that.
**alexcohen** 18:26 I… oh, sorry.
**Bee Klimt** 18:27 I would say the other question is whether, like, do we leave… whatever… whether we… whether we do what you're suggesting or leave it as it is, do we still put that in exception… in stack trace JSON and have a separate stack trace that's a more standard format, like whatever we're going to end up with crash reporting?
Because it might be weird to have reports from iOS with two different formats for the… For the exception.
For the stock trays.
**Ariel Demarco** 18:54 My suggestion would be the one that is stack trees, exception.stackTrace, should be the native one, that is this one, a thread called stack symbol, that is basically the write of symbols. That's… that's what I think, should be the structure.
In terms of using or not, the tree, I agree that, yes, it's… your… you're at mercy of Apple's changing that structure eventually. I don't think it really changed that much since it was released. They added more capabilities, but they didn't make a breaking change, I think, on the model structure. So I don't think that's going to change drastically.
Could happen, above is above, so, could happen.
So… I don't know, I… maybe we can provide both of them, like, exception.stactoryShason and one parsed, so if for some reason it stops from working.
you still have the original JSON.
**alexcohen** 19:58 I think it is actually documented now, probably on the App Store Connect API version of it.
So it's the same… it's the same thing, and I think that there might be a little bit of documentation in the new metric… in the latest metric kit documentation, I'm not sure. I remember seeing something somewhere where they started talking about it.
Also agree with RA, this hasn't changed since day one. I don't think they're gonna change it. If they do change it, it would be breaking for everyone using it, but not, like, everyone, because everyone… everyone has to parse it out to make it useful in any way, so it would be breaking for… For everyone using, so I don't think… they might add to it, but they're not gonna, like, remove or change the keys and stuff like that.
And as far as, call stack symbols, what Ari mentioned. That's the format that goes into the human-readable version of Of a stack trace, and sorry, Ari, don't want to disagree with you, but I would not use that, because you have to jump through hoops to parse that. I'm looking… I'm thinking of the code that Ari wrote, or someone wrote it in the Embrace source code to… to parse that, and it's… It's a bit nuts, and you can get the same thing out of the… out of symbolication with addresses and stuff. Nothing wrong with possibly, passing that in if we have access to it, but it, like.
what do you call it? Metricit doesn't even give us access to anything similar to that in… directly, so…
**Ariel Demarco** 21:36 Yeah, you're right.
**Billy Zhou** 21:37 From what I recall, it's, like, all the metric hit symbol allocation stuff is, like… I think they recommend, like, HOS or, like, some other, like, tools that you can just, like, Use, like, on your own time, like, not during runtime.
**alexcohen** 21:52 Yeah, any backend that does any crash reporting is able to symbolicate the address with the image offsets and stuff like that, so all the information is there. So that's pretty much why that's what should be passed up, because that's what.
**Billy Zhou** 22:06 Right.
**alexcohen** 22:07 gonna want.
**Billy Zhou** 22:08 And then by parsing the, the, thread callback symbols or whatever, are you talking about, like, going through the crash report and just finding the stack trace of the thread that crashed? Like, what do you mean by parsing?
**alexcohen** 22:22 I'm pretty much just talking about flattening it, because it basically looks like a tree, instead of just one flat list. So it's… it's, like, nodes, like one node with the child node, and then another child node, and another child node, and just flattening that so it's, like, a little bit less like a staircase in… When you look at it in JSON.
**Billy Zhou** 22:42 I see.
**alexcohen** 22:43 Like, no stack trace should look like a staircase.
Ever, except if you're profiling.
**Ariel Demarco** 22:50 Yeah, and that's… that's the main usage for the… the… The tree structure is to basically be a flowing graph or something like that, where you have a bunch of methods weighted, and all that stuff. I agree with Alex, you're right. I think that the thread.callstack symbols is not enough, because you don't have the address, you don't have a bunch of stuff that is super necessary, it's just human-readable.
Maybe we can define something, a simple structure of what a… frame could look like inside a stack trace. I'll maybe do that parsing And create that structure and migrate, or do the parsing from the tree structure to that call stack.
**alexcohen** 23:32 I think you're right, what we're… I think what we need here is some sort of… we need to probably add to the semantic convention of what an iOS frame looks like, and then, basically send up… and what a thread looks like on iOS, and send up an array of those, because it's not just a symbol name, it's, like, the address, the offset.
the library name, stuff like that, the GUID of the binary.
There are a bunch of things that are… that are required, so I think we might need to, might need to look into that.
**Ariel Demarco** 24:08 Yeah, that would be… that would be the best idea. I think that we can include something here.
**alexcohen** 24:15 I'm also wondering, like, for exception, I like that we're using exception, I think we should reuse exception, I hopefully… maybe someday we can deprecate the name… the word exception, and move it to something else, like termination, or… or error, or something. But I think exception only represents, like, the stack trace only represents the thread that the exception happened on, or leading up to the exception, and I don't think there's any place to add, like, the list of threads with their addresses in there, or the stack traces for each thread. I could be mistaken, I'm not sure, I looked at it quickly.
Mmm.
**Billy Zhou** 24:52 Yeah, I guess you're right, like, also, like, I think, like, exception also just, like, gets swallowed usually, like, so yeah, we might need a different, like, namespace for a crash.
**alexcohen** 25:04 Yeah, so I was sort of thinking, like, exception. Maybe threads?
And each of them has, like.
You know, each of them is an array of threads with the frames in them.
an exception.stacktrace, or whatever it is now, is basically what led up to the exception itself. If it's the main thread, it's the main thread, or if it's something else, it's something else. Sometimes you have just, like, if it's a C++ exception, it's gonna be, like, totally out of the thread, it's not related to the threads, it's just gonna be a couple of frames.
**Bee Klimt** 25:35 So, to clarify on this a little bit, For the most part, this is, there are… I didn't want to put things in the exception namespace that aren't in it, but I wanted to capture all of the crash data, or… or exception data, whichever it is. And so, there's… there are… there's a bunch of… there are a bunch of attributes that are namespaced with metricKit, and the path into the metric kit payload.
for… for all of the data, and then in addition to that, I tried to, like.
Come up with what would be the, what is it, the type and the message and the stack trace, if that was available for that kind of crash, and kind of simulate that for the standard namespace.
So we can put anything we want in the metric kit namespace, and it's more just a question of figuring out what to put in the… in the exception one.
**alexcohen** 26:28 Okay.
**Bee Klimt** 26:28 It might be more obvious from looking at the test than the code.
**alexcohen** 26:33 I was… I was sort of hoping, if we do something like this, that it would be like, yes, it's Metricit instrumentation, but it just ends up just like anything else, like, if… If, on Android, they're using whatever Google Play has for, you know, reporting crashes or terminations or whatever, that if they wanted to just add it in in this exact same format, because it's the same thing, it's threads and a message and stuff like that, that they would be able to. If we add a metric kit, a small metric kit namespace or something, it's useful, because then you can use some data that, like, is specific to iOS or metric kit, but I do feel that we still need to have something that's very, very general, so that anyone It can just support exceptions or crashes out of the box, like… I'm not crazy about the fact that this has nothing to do with this PR, but that exception currently has… this is what it looks like on each platform, right? It's still just a list of addresses or a list of symbols on every platform. So I would be in favor of trying to keep it very general if we can.
But totally understand if that's not worth it today or not possible.
**Bee Klimt** 27:46 I mean, I can… I can take a pass on that for the exception.stacktrace field specifically, trying to come up with… at least come up with something that's a little more standardizable and… usable than the JSON coming from Metric Cat.
**alexcohen** 28:00 Cool. I think, I think it's worth it. I haven't really seen anyone just, you know, standardize on what metric it sends, because it's so weird.
**Ariel Demarco** 28:09 Damn.
And the last comment you mentioned, Billy, was related to the messaging.
If… if you want to do something similar, like, I think Alex mentioned last… last time, Emm… KS Crash does something really, really good on grouping things, based on the messaging, and tries to… Diagnose and provide us a human-real diagnosis with messages.
I think it's called KS Crash Doctor or something like that. Maybe you can go and use that if you want to have some sort of human-readable stuff.
Because the grouping is great. We use it internally, as Alex mentioned last time.
I think it really worked fine, for most cases. I haven't… I don't have any concerns or problems with the way it's doing it. I think it's doing super well.
the only one that doesn't… KScratch doesn't capture, and it won't be able to handle, is the… is… oh, sick kills.
that, I think, metric, it already provides some sort of messaging, So, in those cases, I think that it's more than enough.
What metric it provides.
I mean, I… I don't think we want to add KS crash as a dependency for this instrumentation.
No, no, no, for sure, no. Just, just mentioning, to answer Billy's comment here, That if we wanna do some sort of grouping, mapping, or whatever, we can use the same logic, not basically getting the dependency, because we don't want to be tied to KS Crush.
eventually could be an instrumentation or a crash reporter concept that we can include, or something like that for OpenTelemetry, but it's mostly, if you want to look how they do it, they are really good at it.
**Billy Zhou** 30:12 We just think that role has to go through the thicker.
there was…
**Bee Klimt** 30:15 One other big comment that we kind of skipped over, which was, oh. Sorry. Represent this as metrics as spans.
**Ariel Demarco** 30:23 Oh, this one.
**Bee Klimt** 30:24 I touched on this in the README, but I went with a span, Because… of several reasons. I mean, metrics in general and clients seem to be kind of discouraged. I know that's somewhat controversial. The… and also, the way these metrics are pre-aggregated, for one thing, like, we don't actually know the time that the events occurred, we just know that it's an aggregate over a pretty big range.
And for another thing, because they're pre-aggregated, it's like, well, even in the case of averages, if you average a bunch of averages, that's not the same as averaging the original values, so that could be misleading. And also, if you try to combine histograms that have different bucket sizes.
That's a complex problem, and we don't know the bucket sizes ahead of time.
So… I think just capturing them as a span makes more sense. I wrote the code so that if we wanted to also emit metrics, or maybe add an option to do metrics instead, we could, but I didn't implement that yet.
**alexcohen** 31:25 So, I think… I think the way you did it, I would have never thought of doing it the way you did it, and I think it's a great idea. But my… It's not really a concern, I'm just wondering, how would someone use it on the backend side?
Like, they would have to do… a lot of different people would need to do something special to actually start using it, versus if we… like, I understand your concerns around using metrics, and I've never used metrics from OpenTelemetry, so I have no freaking idea how they work, really. But… It just feels like if we're able to fit it into metrics in any way, that will be something that people can probably use out of the box, from their collectors, or backends, or whatever, versus this, everyone's gonna have to do something, so… Unless we think, or unless we plan on building I don't know what you call these, but an extension or something to collectors that will take in this type of metric kit data.
then I think we should… we might want to think about going with… with just regular metrics, taking into account all of the caveats that you just mentioned.
Does that make any sense?
Did I make any sense at all?
**Bee Klimt** 32:41 It makes sense to me. I'm not sure if I agree with it. I mean, I think the… I think that even just capturing his span attributes is still pretty useful.
**alexcohen** 32:49 Oh yeah, for sure.
Definitely useful.
**Bee Klimt** 32:53 I don't know… I guess my two questions would be, one is, like, how do people feel about having a configuration option that lets you decide whether to use one or both?
And also, do we think that we need to… if we decide we want to support metrics.
Do we do that in the first draft of this, or do we try to get this in and then add that as a future feature?
**Ariel Demarco** 33:18 It's a good question. When I, look at the comments, I saw this one, I was concerned about not why you didn't use metrics, because I imagine that you were going to say, Basically, what you mentioned, related to the difficulties of using metrics in the client side, and also the way the data is already digested.
But why spends and not logs?
or events.
**Bee Klimt** 33:51 So… For the diagnostic payloads, I used log events, because it seems like they're…
**Ariel Demarco** 33:58 Yo!
**Bee Klimt** 33:58 street thing.
**Ariel Demarco** 33:59 Bye-bye.
**Bee Klimt** 33:59 It's only for that daily report that's the 24-hour aggregator that I use to span, because it is over a 24-hour span, so it just seemed natural to me.
**Ariel Demarco** 34:09 Hmm, I see, I see.
**alexcohen** 34:11 That's why it makes a lot of sense to me that I… I like that.
**Ariel Demarco** 34:16 No, I think it's… I think it's okay.
And… And to be honest, I don't expect any collector to work with this data. Any metric… any collector with metrics to work with this data, because of the cardinality, it's going to explode.
I, I, I also don't know if… if… Probably the data will be useful, but as you said, the data make… maybe sometimes won't make sense because of the way it was aggregated and digested, and it's not the same doing an average of all the data than doing an average of the different averages, though.
I agree on having intensive plans. I don't have any concerns with that.
Maybe it would be a good idea to be able to switch this, and so if somebody wants to try it out, and see if their collectors explode with using metrics.
Be my guest.
But yeah, that's what I think. I think that having spans is… good enough, I think.
And it will be a nice to-have for metrics, but I don't know if it's going to be useful, in reality.
It's good if you had it here, you said you had it here?
**Bee Klimt** 35:34 I talked a little bit about why it's a span in the README, yeah.
**alexcohen** 35:38 Yeah, the documentation is crazy complete. Really nice documentation.
**Billy Zhou** 35:43 Yeah, it's, like, better than apples.
**Ariel Demarco** 35:46 Yeah, totally agree with that. Okay, this is great. I'll take a look at it, and I'll add some notes on what I mentioned regarding the call stack trace.
I think he…
**alexcohen** 35:59 Before we continue on, if I could, I just wanted to understand, if we have time to talk about this, why this would explode a collector. It is, like, once a day per device. Shouldn't that be really easy to handle? Like, it's just once a day per device.
in one span, with a bunch of attributes and stuff. That should… I mean, if collectors are not able to handle that, then I don't really know what, like, what they could handle.
**Billy Zhou** 36:26 maybe size limit? It was a pretty big span, but that's the only thing.
**Ariel Demarco** 36:33 What's her name?
**Billy Zhou** 36:34 And then there's a… Was there, like, a size limit, concern as well for this? I never… I didn't take a look at that.
I think it was a pretty big spin.
**alexcohen** 36:45 It was all about the metrics, I think, that were… that would be the problem with the, with.
**Ariel Demarco** 36:51 Cardinality.
**alexcohen** 36:52 Cardinality?
**Ariel Demarco** 36:54 Yeah, that… at least that's… that's… I know there are some other arguments in terms of why metrics in client-side is not great, but the cardinality is based on resources, and the resource is basically why it identifies a device and changes that don't… things that don't change over time.
So, it's… it's a mix between the OS version, the device model, and all that stuff. And if you can think of all the different client-side possibilities of, resources. You will have a bunch of OS versions, a bunch of devices. The mix of all of them will generate a bunch of unique resources, and everything is based on the possibility to have a set of limited resources. Imagine that from the backend perspective, that is… that is not going to be a lot of different instances. So… and they even created… for the… for whenever, for example, in Kubernetes, you change the pod name, or stuff like that, they… they already added some… specific mechanisms so resources can be editable, some part of the resources can be editable, but for mobile, or for client-side, let's say, that's… that's not feasible at all. That's why I think that it's… it's kind of complex for collectors to handle, because the cardinality grows exponentially over time.
**alexcohen** 38:18 Yeah, I gotta… don't totally understand. I'm gonna have to understand the… the relationship between resources and metrics. I guess that's what I'm missing here, because, like, this is… is something that's handled by, like, basically every system out there, like, being able to to receive metrics like this, so it's just a curiosity. It seems like anything OpenTelemetry should be able to handle this, no problem.
**Ariel Demarco** 38:45 Yeah, it's a limitation of open telemetry, not of the different tools that are out there. Like, out there, if you… there are multiple resources to use metrics from Metricade and see relevant data, and it works fine. It shouldn't be a problem, really.
**alexcohen** 38:59 In that case, I think that anything that works and will get us moving forward with this, get something out there that we can iterate on in the future, is probably the best scenario.
**Ariel Demarco** 39:09 Yeah, I agree.
Okay, I'll add some comments on the PR, on the call stack thing. I also agree that with Alex, it would be great to go and include something like that in this other thing that… it was contributed regarding crashes. Maybe from there we can start talking about the… How they call stack… how the stack trace with multiple threads should look like whenever you have a crash.
And at the same time, it would be also good to start contributing to this stack pressure presentation from Swift.
I'll take a look at that. I'll probably… create a minimum draft, maybe we can circle up.
I don't know if there's any other topic we want to discuss, or we can go and see if there are some new issues.
No other topic, and go… Wit.
issues.
So… This was the one that was opened last time.
And this one is, yeah, the one that was opened last time, in terms of pull requests.
We have this… From you, Billy?
I added a comment here, I think.
But PR looks fine.
**Billy Zhou** 40:32 Oh, okay. Okay.
Yeah, I kind of forgot I raised that. I'll address it.
**Ariel Demarco** 40:40 No problem. Happens.
And I think this is it. Oh, Vinod, you have also a PR that updates the README and the usage of the OTLT example?
Maybe you converse it. I read it, and it's working fine.
**Vinod Vydier** 40:58 Yeah, I think it's already… has it been merged?
**Ariel Demarco** 41:02 Really?
Funny.
**Vinod Vydier** 41:12 Oh, maybe not, yeah. Okay.
**Ariel Demarco** 41:14 No, seriously stopped.
Yeah, there's only one change on the Docker Compose, probably because of the reference that changed.
But yeah, I think that there are just pending things to merge.
I think this is it.
I think we have 20 minutes back for our time.
Okay, I'll…
**Vinod Vydier** 41:41 Thank you.
**Ariel Demarco** 41:42 Thank you so much. See ya.
**Billy Zhou** 41:43 Bye, guys.
**Vinod Vydier** 41:44 a little bit.
**Ariel Demarco** 41:45 Bye-bye.
