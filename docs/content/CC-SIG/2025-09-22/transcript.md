SIG: OpenTelemetry C/C++ SIG
Date: 2025-09-22
Duration: 60 minutes
Zoom Recording URL: https://zoom.us/rec/share/ARIE_jESlG7lErgCiXrqxpJpXz-1hghivQjO950cGneFhffygfIaLVN3_VKqUtkr._BCo7kCTRq8d2_CC
============================================================

## Zoom Recording Transcript

Nikhil Bhatia 00:01:11 Hi, Mark.
malff 00:01:13 Hi, Nikhil.
Hi, Tom.
Tom Tan 00:01:29 Hi, Mark.
Hi, Nikkihu.
Nikhil Bhatia 00:01:32 Hi, dog.
Tom Tan 00:01:38 I think Ladit will also join today's meeting.
malff 00:01:41 Okay.
Hi, Lalit.
Lalit 00:02:24 Yeah, hi, Mark.
Hey, hi Nicole. Hi, Tom.
Tom Tan 00:02:29 I don't know.
malff 00:03:16 I don't know if Doug is joining. He was around recently, but I don't know if he's coming tonight, so… Okay, as for topics to discuss, there is a big one, which is some donation proposal for PHP.
Which may involve, openTelemetry C++.
And that topic is likely to take a lot of discussion, so I guess we can start with that. Any other quick things that you want to discuss before that, before we dive into the PHP details?
Hi, son.
Ehsan 00:04:13 Hey, everyone.
Tom Tan 00:04:15 Oh, you know, so…
malff 00:04:31 Okay, so for the… the… PHP discussion.
I don't know if all of you are aware of it, but there is a proposal for donations of some PHP code.
That does automatic instrumentation.
And some of that code is using, C++ code, and internally, so I haven't looked at the details yet. But I think internally, it is using some, Well, it is using C++ to send the data, and there is some question about To do with that, and whether it should use the C++ implementation instead for the SDK exporters, or things like that.
Personally, I'm just starting on that, I'm, I'm just trying to figure out what the… Whatever donation is.
Lalit, Tom, and Hsan, did you have the chance to actually look at that proposal and see, Just to try to see if you… what you understand of it.
Lalit 00:05:45 Yeah, I mean, I have some idea about this proposal.
So this is basically, I mean, I think the Elastic, they have come up… they have… This, this, this, I mean, donation is basically the auto-instrumentation of PHP.
libraries?
And they internally use C++, To send the… to export the… Logs, metrics, and traces.
to OTLP, collector.
And they use their own custom C++ implementation.
True… export to OTLP. Their requirement is that whatever library they are using, that should be asynchronous.
That's a limitation in PHP. PHP does not have any asynchronous, export. That's what I could understand from this documentation which was given, and so they came up with Native Safety Displace, which does Probably it was easy to, do PHP to C++ calls, so maybe they used C++ as a means to do the export.
To collector, and… So they just wanted us to… they just wanted us from us to know that if they can use OTL… I mean, OpenTelemetry seems to do the same?
malff 00:07:10 Okay.
Lalit 00:07:10 I mean, ideally they can do that. There is nothing which is stopping them to not do it.
It's just that what… what… I mean, I'll be more… more concerned what would be our role as the maintainers if they want to do something like this.
And there is another thing, OPA, AMP, C++ code. This is, this is the OpenTelemetry Management Protocol.
This basically can… it's a protocol between to send the configuration to collector, and also get the stats of the collector, so this is… this is a protocol which is defined to do that.
And this donation also includes a CPS Space implementation of that.
So that could be one candidate that this, this, OPAMP protocol implementation can be contribut… can be maybe, donated to the Contempor, but somebody… somebody has… if it is donated there, somebody has to really maintain and own it.
And whether it would… it would be us as OpenTelemetry, C++ maintainers, or not. Baldi, I think these are the two.
malff 00:08:17 So, for this, OPMP code, is it… What is it doing exactly? Is it pulling the configuration from downstream?
Like, it.
Lalit 00:08:27 It will push it, I mean, if… I haven't seen the implementation, but the protocol basically gives the interface… I mean, it basically has a specification to push the configuration to the collector.
And also, to get the stats of the collector.
Probably, probably that could be the contributions.
Okay. So, yeah, it's a kind of independent thing. I mean, it's probably… anybody can use it if they want to really… anybody who is using C++ can use this as a plugin to really… to really manage the agents.
So, something which could be helpful, and it's good to have this as a donation contract repo, but If done, I mean, what would be our role? That's something.
malff 00:09:19 Well, I guess there are several, Several layers of questions.
I guess the first thing is to decide what to do with the code, and once we figure this out, then the second question is, who does it?
But that… that can come later.
What, what, so… It, from what you are describing, it looks like the OPEMP code is a different feature altogether.
Yes. I don't quite get what it does. It reminds me of Jaeger Remote Expo… Yeah, the Jaeger remote sampler that can basically take its configuration from downstream to apply it locally. Is it doing something like this, or…
Lalit 00:10:06 I just shared, I just shared the link, probably, if you can just open, we can just see there what it is doing.
Okay.
In the chat.
malff 00:10:15 industry.
Lalit 00:10:15 that link.
malff 00:10:16 I'm in the chat, let's see… If I can find it.
Lalit 00:10:20 I always have difficulty, even meeting scientists.
malff 00:10:39 This one?
Oh, OpenPage PHP, okay, I have that somewhere.
Is it what you wanted to look at, Ladit?
Lalit 00:11:44 Oh, sorry, I'm on mute here, I didn't realize it.
malff 00:11:47 Oh, okay. Yeah, yeah. Yeah, for some reason, copy and paste is not even working.
Lalit 00:11:52 Oh, okay, maybe you… Maybe just search for OPAMP, and you will get in the…
malff 00:11:58 Okay.
Lalit 00:12:17 Oh, it should be, the first one, yeah.
malff 00:12:19 Okay, sorry about that.
So, I get this is for the configuration of, locally of the node itself, it's not even… To export things.
Okay, so…
Lalit 00:13:23 Oh, okay, I was muted.
malff 00:13:24 Yeah, from… yeah.
Okay, so, yeah, from… so it looks like a totally separate thing, so that, yes, that can definitely go into contrary, but I don't know how we can… We can consume it, but that would be interesting to see in details.
The other part I don't… quite get from the… Where is that? From that proposal.
So, if I understand correctly, there's a proposal to have automatic instrumentation, We've all.
Lalit 00:14:04 Enjoy you.
malff 00:14:04 change in PHP.
Lalit 00:14:05 Which is the donation proposal, but on the same time, we have also the PHP SIG.
malff 00:14:12 Which is exposing an API, an SDK, an exporters, so that you can manually instrument the code.
Lalit 00:14:19 Yes, yes.
malff 00:14:21 What I don't get is how the two are supposed to… coexist together.
Lalit 00:14:30 So… so these are the… I mean, we already have in other six, like, if you see, Go Instrumentation, they have… one is one… one repo for manual instrumentation, and one repo for auto instrumentation.
So, so they, already, they have, I mean, they are… Language 6, this already do that.
As a different repose.
Even .NET has that separate repo for auto-instrumentation, and one for the diff… the standard manual instrumentation. So I assume that this will go as a separate repo?
owned by PHP, we won't own that, it's the complete implementation, but they will… internally, in that separate report, they will be using OpenTelemetry, C++, OTLP, export, exporter for, for exporting.
malff 00:15:21 Okay, so how do we have a SIGs that do have automatic instrumentation do that? Do they… Do we point to the same SDK under the cover, or do we have a different implementation in the whole stack?
Lalit 00:15:34 It… It depends. I know that at least the Go Auto instrumentation, they are using… they use a CB, I mean, internally, they use… They, they have written us, I mean.
They have written this API in SDK in C, and they are using that. Not even C++, they have written that in C.
malff 00:15:59 Okay.
Lalit 00:15:59 Do you think PHP is doing that in PHP itself? I don't know, I haven't seen their internal… I mean, but… but if you are… .NET does it in .NET, but… but your goal will go users C.
For doing the actual export.
malff 00:16:13 Well… Just a sea wrapper, or the entire thing in C?
Lalit 00:16:18 I think it's the entire thing in C, entire thing… sorry, it's, No, the SDK is a go, but… but the… some… they have a thin layer of C, To create these spans and logs.
Because they go into instrumentation, I mean, what I have seen, they use eBPF, so the code has to run in kernel.
So it can only run Seek, so creating the spans and creating the logs, all this happens in kernel, but the export happens from the user space. So they use GoExporter I mean, in user space, but the actual span creation and all those happens through a C code.
malff 00:17:03 So…
Lalit 00:17:05 Mmm.
It's a bit different, but I think… I mean, so to summarize, like, languages have their own separate repos for auto and manual.
And… This is what they're going to do for PHP, also.
malff 00:17:21 Okay. Well, separate ripples, I mean, that's fine, but the…
Lalit 00:17:25 Beautiful.
malff 00:17:26 My… my question is, what goes under the cover? Is the… So, for the manual instrumentation, there's the classic API, SDK, and exporters.
Lalit 00:17:38 Yes.
malff 00:17:39 And for the automatic instrumentation, I'm assuming that at some point or another, it goes back to the SDK itself.
And here, in my understanding, this proposal is to use the C++ SDK instead of the PHP SDK.
Which is… A bit weird, because then you end up with two SDKs in the same process.
Lalit 00:18:05 No, not, not… 23Ks?
I mean, I was assuming that they are not going to use OpenTelemetry C++ as an SDK, but they may just use our… OTLP exporter, somehow they may create an FFI layer on top of OTLP exporter and directly use it.
malff 00:18:30 Well, not sure yet.
Lalit 00:18:32 Thank you.
malff 00:18:33 I think, from what I understood, that they have their own exporter today.
which is a different flavor of OTLP. I mean, it's a… not a different flavor, it's a different implementation of OTLP exporter.
Lalit 00:18:47 Sorry, sorry, which one? This, this, this, like, this Tunisia library?
malff 00:18:51 The donation, yes.
Lalit 00:18:52 Okay, and that is in PHP, or that is in…
malff 00:18:58 I think it is in C++, let's see.
Ehsan 00:19:05 Yeah, it's C++.
I don't know how it works, but it could solve a really big problem for PHP.
malff 00:19:21 Yeah, they have a bunch of C++ code in their repo.
quite get how it works. I mean, there is code which is just to hook up to the.
Lalit 00:19:34 PHPNG itself.
malff 00:19:35 But then there is also some.
Lalit 00:19:40 Yes, you see me.
Some of the code… Some of the code I see, configuration and all these things would be OPAMP, but this HTTP thing, probably these would be only one which they are doing… they would be using. So I don't see, them… them really having the SDK as such.
In the sense, I don't see processor and all. If you're talking SDK, I think it would be all processor and export. I don't think they have done that. They're just using… export thing.
Looks like they're exporting right away. Yeah, so they probably, they want to use just our export, not anything else.
And they may be using the SDK… so they would be using… they probably would be using the SDK, the PHP SDK.
Because if they start using two SDKs, there would be more issues in terms of context propagation and all those things. I don't think that would be easy. So they would be just using PHP, SDK, and Which is then calling this native C++ to export.
Because they wanted an async export, so I think C++ provides async export, so that's what they are using C++, just to async export.
malff 00:21:01 So, the synchronous export is because of a batch processing, which is basically a background thread.
And OTLP as well, yes.
Lalit 00:21:13 Yeah, so… Yeah, so this one is CHB Transport Async, async, so they… They just needed the async functionality, and they went for C++ for that. I mean, at least for the export thing.
malff 00:21:27 Okay.
Ehsan 00:21:29 Yeah, with PHP, it's not possible.
Lalit 00:21:31 Yeah.
Ehsan 00:21:32 If you switch the, like, I think it's, like, process or something.
I mean, during the calls, it's asynchronous, but when you want to switch your process, you have to do this, flush that you export everything, and that could be… that is blocking, so if your collector is slow, then you are done.
And the way they work around it is they deploy a collector next to the, I don't know, the host, like, if it's Apache or something, then they do… One collector, Just working for that service.
malff 00:22:21 I see.
Ehsan 00:22:23 And…
malff 00:22:26 So we just upload the data to a corrector, which is next to it, and then we can asynchronously send that away.
Ehsan 00:22:34 Yeah, just, just, just, just the workaround. There is also a module for Apache, from… it was… I think it was from Cisco.
If you recall, they contributed that somehow solves this issue, that it becomes completely asynchronous, but the problem… and that's also C++.
But the problem is, you don't have flexibility on creating these pants, so if… If you want to add new spans, That's not possible. Heather protection.
malff 00:23:08 Interesting.
Ehsan 00:23:08 possible.
malff 00:23:12 Yeah, so it looks like we have, we have an OTLP exporter written in PHP.
Lalit 00:23:21 -Oh.
I think most probably this would be calling C++ thing, it would be the CFFI layer.
malff 00:23:31 Okay.
Ehsan 00:23:44 If this solves as they claim, I think PHP users will really… Appreciate it.
malff 00:23:52 So… Do we know what are the comments from the PHP, SIG?
I'm on the…
Lalit 00:24:00 They don't have any comment, they don't really understand C++, so they haven't really done any comment, so they wanted us… with C++ expertise to give.
malff 00:24:09 Okay.
Lalit 00:24:14 I mean, the problem is, one thing which I'm thinking now, that… whether they can directly use our OTLP exporters or not, because our exporters are really tight to recordable and all those things.
then… which… which means that it's not… just not plain exporter? I mean, it… Also, not…
malff 00:24:34 Oh, it's…
Lalit 00:24:34 Sorry.
malff 00:24:35 Yeah, it's not only the exporter, it's the SDK.
Lalit 00:24:39 It's e-holistic, actually, right? Yeah.
It… Yeah, so that's something, probably, because we don't have an API which… where they can just give a OTLP payload, and it will export it asynchronously. We don't have that API in our exporters. We just… we have exporters, which takes recordable, and then it will… do the exp… it will create the OTLP payload from that recordable, and then it will do export.
So we don't have that kind of API. They just want to do… use our… uploader, OTLP uploader kind of thing, which can… if they ask us that… provide us an OTLP uploader, which they can use.
to do the upload without any other SDK constructs.
We don't have that.
Boo.
Are the review provides them something.
Ehsan 00:25:36 Which they can use it, or…
malff 00:25:44 Well, I'm just trying to figure out all the… Pieces in the puzzle.
Because on one hand, we have an existing HDK, sorry, an existing PHP, Implementation with manual instrumentation.
which, as Isan described, has some limitation, because you cannot basically spawn a thread.
So, everything has to be done synchronously.
And on the other hand, there is… automated instrumentation, which is using hooks in the PHP engine itself.
collect data and do things. However, this thing is using a different stack.
And doing its own exporting, inviscode, basically.
And… And so this is written in C++, and of course, we have a third part, which is the OpenTelemetry C++ implementation.
with its own SDK and exporters, And so this is… We… Three moving parts altogether, so… The question is… It feels strange to have all of them at the same time, for sure. And the question is, which one do we need to make this work?
Lalit 00:27:10 Thank you for coming in.
Yeah, sorry, I think, Mark, just probably… probably, I think, as I understand, the first phase of this is that they're going to The current implementation as it is will go To the separate repo.
The no changes, as of now, immediately.
And then we have to start working with… with the… probably the owner of this repo, or maybe they have to work with us.
To start integrating step-by-step, phase by phase, how they can use TLP uploader from our.
malff 00:27:49 Ripple.
Lalit 00:27:50 So, it would be more of a phased approach. I mean, piece by piece, they have to take it and start doing it, and it may… they may have to… I mean, if there is some change required in OT… OTL… in our OpenTelemetry CPP, I mean, basically.
malff 00:28:03 Yeah, we can do that, yes.
Lalit 00:28:05 I mean, either we do it, or we tell them to do… tell this… the elastic donation team to do that, I mean… Should we do it? I mean, do we have… if we have bandwidth, I think we're in good, otherwise we can ask them to do it.
malff 00:28:17 Okay.
Lalit 00:28:17 I mean, my suggestion would be let's not take more of the responsibility in terms of doing anything, I mean, any changes in the code.
Unless until we have the… Sweet.
malff 00:28:30 Apart from the OPENP protocol, which is a separate feature itself.
Lalit 00:28:36 Yeah.
malff 00:28:37 So this one, yeah, probably can go to contribute, but apart from that, everything else which is sending to… OTLP and things like that.
I can definitely see this code calling OpenTelemetry C++ instead.
Lalit 00:28:54 To take a dependency on the library instead of.
malff 00:28:57 reimplementing the OTLP protocol, so that should be doable.
But the next part is, I don't get how that coexists with the native, PHP instrumentation. If you have an application which is… Corning something which is automatic… auto-instrumented, and calling something else which is manually instrumented.
All the different spans working together, and… And hole… how is the data going to be shipped if we have two different SDKs working below the cover?
Lalit 00:29:37 there cannot be two different SDKs, that's what I'm saying, because if there cannot be two different SDKs, somehow we have to provide For OpenTrMV means OpenTM to see CPP has to provide an uploader interface Using this, they just… I mean, they just give a payload to that… that payload would be OTLP payload? They just give that… And that should do the upload.
So, so they… they may, they may do this, I mean, the… the serialization to OTLP would be done in PHP, and they just use the FFI interface to call our uploader to do the upload.
So, instead of, like, right now we provide export… Oh, yeah.
malff 00:30:24 Yes, so you mean from the donated code?
Lalit 00:30:28 Yeah, so donated code will do a serialization to OTLP payload, and then they somehow invoke our async function to do the export.
malff 00:30:37 Okay.
Lalit 00:30:39 Yeah, so which means that if CO, OTLCPP provides any such async function, which takes in… which takes the input as the OTLP payload.
and it pro… it does an async upload, they… I think that's what they need from us.
I mean, we don't need to worry about that how the auto-instrumentation things work in PHP.
I think we should be more concerned about what they need from OTL CPP to make this work.
And… That the best is this Elastic team can provide us the information.
So, looking into the code, it looks like they just need a function, async function, which takes the serialized OTLP payload and just do the export, but I think they are the best to tell us what they need.
Ehsan 00:31:38 I mean, there is also a third option, that we just accept what they have.
And keep what they have. I've seen this approach, like, in Envoy Proxy as well. They do their own… Exports and posts for it, and… HTTP and gRPC.
Lalit 00:31:59 Yeah, I think that's… that's… that's what I think the… I mean, I found the Phase 1 would be… And then start exploring if they can use it. I mean, good to use it instead of having their own… The hotel CPP is definitely better tested than what they would be providing here.
So, definitely better to use that, yep.
malff 00:32:37 Okay, well… It will need a lot of… Investigation, for sure, to figure this out, but Just trying to get a feel for the…
Lalit 00:32:46 Mmm.
malff 00:32:46 Overall puzzle today.
Lalit 00:32:49 Yeah, yeah, exactly.
Still a black box for us, I mean, haven't we have to see you?
malff 00:32:53 lots of things. Yes.
But I still don't get how this is supposed to coexist, or if it should coexist with, the current PHP, implementation.
Regardless of whether we use OpenTelemetry C++ or not.
Because this is only two different SDKs in the same process.
Lalit 00:33:22 Oh, yes.
Ehsan 00:33:23 There is already existing this PHP auto instrumentation.
Lalit 00:33:30 Oh, can you share the link?
Ehsan 00:33:32 Have to check it, but… If I recall correctly, there's already… Hmm…
Lalit 00:33:42 There is something called zero code, yeah, there is something, I don't know what exactly… how exactly it works, but yeah, there is some… something, you're right.
It is in PHP contrib here.
malff 00:34:43 Interesting.
Ehsan 00:34:55 Now I'm confused. The existing one also needs a C compiler.
malff 00:35:05 You mean the plain PHP itself?
Ehsan 00:35:07 No, no, the existing auto instrumentation.
Lalit 00:35:12 Also, that also needs a…
Ehsan 00:35:14 And that's also… that's also using C.
Lalit 00:35:42 I just shared another repo, I think that's the correct repo for auto-instrumentation, which they have.
malff 00:35:47 Okay.
Lalit 00:35:48 It's…
malff 00:35:50 Oh, PHP implementation, okay.
Lalit 00:35:53 Yeah, this, this has… Oh, and it's kind of surprised that they already have something in place, and…
malff 00:36:04 with… Okay, copy and paste is not working for me today, I don't know why, but… BHP Instrumentician.
Okay.
Lalit 00:36:33 Yeah, and this is… this is also… they have a C… they are using a C layer on… so they have written, I think, probably in C inside this. If you open the EXTs, everything is in C.
But everything, but almost everything.
malff 00:36:47 Looks like it, yes.
You know… I've been conveniently ignoring every other thing, like .NET, PHP, Java, and whatnot.
Looks like everyone is doing some strange things all over the place. It's interesting.
Ehsan 00:37:22 I, I think the most, strange one is PHP.
malff 00:37:28 Okay, yeah.
Ehsan 00:37:29 I was shocked that it's not possible to have something asynchronous.
in PHP.
malff 00:37:39 Well, I guess it's… At the end of the day, well, I never wrote anything in PHP, but my understanding is that it's a scripting language that renders an HTML page at the end of the day, so… It has to stop so that the page can be rendered.
Ehsan 00:37:57 Yeah, that's when you have the problem with telemetry. If the collector is slow.
So you will notice it… you will notice only when the process is closed, and your collector is slow.
malff 00:38:11 Which could happen. Yeah, so you have to offload to a different process right away.
Ehsan 00:38:19 Yeah, or you just get a timeout.
Lalit 00:38:25 I think now we need to ask PHP people that why they have lots of things, and internally they are using some C code instead of using a C++ or something.
malff 00:38:36 Well… Push things off.
maybe all those things have a way to interface with the PHP runtime itself.
Lalit 00:38:44 Yeah, it's.
kind of correct, I mean, because it's easy to interface using C, then using C++, so most of the code Agency, yeah, that's true, but…
malff 00:39:13 Okay, more code to look at to get a full picture, I guess.
Ehsan 00:39:22 Could we ask for a requirement? I would love to see, like, a test with a really slow collector.
This could be simulated by, like, an Envoy proxy.
Lalit 00:39:39 Sorry, can you come again?
Ehsan 00:39:41 I mean, I would love to see, like, a test with the simulated slow collector.
Because otherwise, I don't see what value this adds, this project adds.
So, the simulation will be, like, you could have an Envoy proxy that you could have fault injection, and fault is… Just make it a reply.
Slow, maybe 10 seconds.
Okay. And then your test should show it immediately. If it doesn't finish… It misses.
Lalit 00:40:18 Oh, sorry, I didn't get that. How NYProxy will come here?
Ehsan 00:40:22 S… it's about simulating this slow collector, I want to see that it's really solving this asynchronous problem, because…
Lalit 00:40:31 Oh, you're saying…
Ehsan 00:40:32 You, you will not see it, In the tests.
So it's, like, two phases where you have these PHP stuff, like, you… Once you earn a script.
And you're working, everything is asynchronous, but when you close your process, you have to flush.
Yeah, all your spans that you have collected so far, and you are not… you haven't exported them yet.
And when this thing happens, and your collector is slow.
And then everything is slow, like…
Lalit 00:41:11 Which is okay, right? I mean, they may be in some queue, may not be flushed, but the more important thing here is that the user space thread should not be blocked on doing export.
Ehsan 00:41:20 Which is the…
Lalit 00:41:21 more important.
Ehsan 00:41:22 Yeah, exactly, and they claim that they solved this.
Right?
Lalit 00:41:28 Yes. With the asynchronous synchronous, that should get solved, right? Because asynchronous means that it would be running somewhere else.
But the user thread is not blocked. The user thread can do its own business logic.
Ehsan 00:41:39 Yeah, so it's like they send this payload to some thread that is doing in the backup.
Lalit 00:41:44 Yes, some async 30 or some async thing which is doing it here.
Ehsan 00:41:50 Yeah, this could be, like, one requirement for the CI, then, that they show all this.
Lalit 00:41:57 I mean, I'll be more… inclined to let them tell us what… what features they want, and let them implement if there is something required in C++, rather than me telling them, suggesting them.
We can tell them that, I mean.
OTL… we have OTLP Exporter, which provides async, but this is more tied to the SDK constructs in terms of recordable and all those things, so you cannot directly use it.
If… you may have to look into the C++ code and… If there is some reusable API you want to add there, we are supportive of that. You can add it, and we can review, and we can provide you.
Instead of we trying to… look into the PHP, how auto-instrumentation works, how they are integrating with C++. I mean, let them do it, and we are supportive to reviews and provide them suggestions if they want.
I mean, I'll be more inclined in terms of the current bandwidth, which I see, we all are… not fully, fully dedicated to C++, what is C++, and we are… I mean, that's what I feel, right now.
malff 00:43:10 One thing I've noticed about OpenTelemetry C++ is that they are using the semantic convention as is today.
Because all that code is actually code generated from OpenTeametry C++.
Lalit 00:43:25 Okay, dear, okay.
malff 00:43:26 So, this is… so it's… It's right out of a generation script, it's not even formatted with the same format, but this is exactly, byte-for-byte, the code that we have in OpenTeametry C++.
But just for the semantic convention, I don't know… I don't know what they're using it for.
But this is part of CPP itself already.
Lalit 00:43:52 Okay.
Yeah, interesting. I didn't notice that, you know.
malff 00:44:01 Of a… the same comfort.
Lalit 00:44:06 They may be using it, adding some resources and all those things, maybe in the… in that export thing, and they thought that, let's use that, I don't know.
But this is also something they can use it, probably.
From Seedless.
malff 00:44:38 Oh, so this is using OpenTelemetry CPP itself?
Looks like it.
Lalit 00:44:43 No.
malff 00:44:44 I don't think so.
Lalit 00:44:46 Who is it?
Oh, no, I didn't… Please, yes. Oh.
This is the photograph.
No, but we don't provide, like… we generate these libraries on… during the build, right? We never have these in the… okay.
We don't export them. Yeah, so they, they may be, mostly, they may be creating it, and they have checked in, and they may have created somehow or something. Not from Open Delivery, for sure.
Because we never check in deals.
malff 00:45:14 But very close, because they are using the same protot, message VFAN.
Lalit 00:45:19 Yeah, it will generate the same if they… they may be doing the way we generate it, the same prototy, and then it will generate the same file. Could be.
But I think that is also another discussion that… why do we not check in these… This protobuf, why we only auto-generate.
malff 00:45:41 Sure, yeah.
Lalit 00:45:42 Yeah.
malff 00:45:53 I'm just going randomly to some files to just get a feel for what is there.
Lalit 00:45:58 Hmm.
malff 00:46:11 Nikhil, does that sound familiar?
Nikhil Bhatia 00:46:14 Yeah, Mark.
malff 00:46:30 Okay, so… overall, I guess it's, some interesting things to look at. We have to… Figure out what, how the puzzle will fit together, to see what… What to do with it.
If a PHP donation uses some C++ code to export things.
I guess it should not be too hard to take a dependency on a pan telemetry C++ instead.
If this is what they want to do.
Lalit 00:47:08 Hmm.
malff 00:47:09 Yes, so we might have to… To provide some helpers to a tree.
Make it easier to upload some data.
Lalit 00:47:17 Yeah.
malff 00:47:25 Can you just open…
Lalit 00:47:26 Can you… sorry, can you just open their, that HTTP async? Yeah, probably HTTPtransportASync.h, let's see what exactly is there.
In court.
malff 00:47:36 for producing.
Lalit 00:47:38 Yeah, just, this, this file here.
malff 00:47:40 This one?
Lalit 00:47:41 Yeah, yeah, this one, yeah.
I just come down, I just want to see if it is… Initialized connection. I just want to see the export thing, Oh, yeah, yeah, that's here only, yeah, the span, byte… yeah, they… so yeah, this, this one only. std, span, std byte, payload. Yeah, so they already have that payload, yeah.
Just go to the NQ function, I think that's important. I just wanted to understand how… So there is the NQ function, Yeah, this is using the… the bytes, the payload bytes here, so they just need the functionality which accepts the serialized ODLP here.
malff 00:48:22 If this is already a protograph message of a proper format, yeah.
Lalit 00:48:28 That's what I think, yeah.
But if that's the case, why do they need this… proto-generated headers, probably we need to see the code again, sorry, I think.
There's a protogenerated header, that means that they may be using those for serialization, yeah.
Hmm.
malff 00:49:06 And debugging all this from a PHP application would be even… The new experience.
Yeah, so this is definitely using thread mute mutex and things like that, so it's…
Lalit 00:49:30 Hmm.
malff 00:49:34 if there is the… if in PHP there is a constraint that it has to be to finish.
I can see.
How we need to offload things.
Okay, well… Thanks for sharing this. Based on the discussion, I think I will… know a little bit better about where to… where to look at code to get a better understanding.
So… Yeah, not sure what we can do. I guess we can definitely have a dependency on OpenTeametry CPP, if it helps.
We can also have, One… one part of the code, which is this, AMP thing going into Contrib, that should be… That would be doable.
For the rest, we also need to see with the PHP team what they… what they plan to do. I'm still a bit confused by the fact that we have two different SDKs implemented two different ways in the… for an application written in PHP.
Because at some point, if you have some native code… if you have some PHP code instrumented manually, but invokes some PHP code instrumented automatically, and vice versa, those things has to work together to create a… a span that works for the tree, and I don't see how that is going to work.
Lalit 00:51:42 No, that will work because the context would be still managed in PHP. I don't think they're using C++ for context management.
So, as long as the context is managed in PHP, even the mix of auto and manual should work.
If the span is created using manual, and if the code… And then it calls an auto-instrumented library. That should be able to get the PHP context and find out the parent, and then do it.
So, should be possible, but… and… If they are using context in C++, that's wrong, and I don't think they will do it, because that's a basic… they cannot mix two different contexts from C++.
malff 00:52:17 didn't.
Lalit 00:52:18 PHP, so… Yeah.
malff 00:52:42 Which feels like… a logger interface, maybe there's a trace interface, I haven't seen it yet.
Lalit 00:52:48 I thought this is just internal logging, I didn't see that, but that's…
malff 00:52:51 Oh, internal logging, okay.
Lalit 00:52:53 I don't know, I mean, I just spilled something in.
malff 00:53:12 In order to what?
Lalit 00:53:15 Yeah, that's interesting to think.
Yeah, here it is converting, from… probably from PHP…
malff 00:53:27 Happy to see you.
Lalit 00:53:27 Yeah, yeah, yeah, that's the FFI part, maybe. Yeah, it's taking PHP, and then it's converting it to… Okay, so they do convert it, and… So there would be a challenge.
malff 00:53:41 Zoom.
Lalit 00:53:42 Sorry, we don't provide… No, I mean, this would be a challenge, because we don't provide, sorry, we don't provide of the pH… the… the… or the… the generated protolib headers, so… Ugh.
That would be a challenge here. I mean, how can they use our code or not?
malff 00:54:05 Yeah.
So… M… I'm wondering what that does, because it's calling a method by name, given dynamically, So… Is this, by any chance, diving into the SDK from the PHP SIG itself.
Lalit 00:54:26 I think it's… this would be… This would be PHP only, span.call matter, right? This is somehow the… the FFI export objects the span object would be something which is exposed from PHP to C++ to C++, and they are calling that… Call method and getting the contacts and something.
Getting the parent from there, and… So this is just getting the parent, and then… Using that to populate the the proto… C, press, press through two things.
malff 00:55:09 Just looking at what this thing… Just in case this thing… this thing exists in the PHP side.
Lalit 00:55:31 So just see if it is really PHP, see OTLPHP, or… I don't know.
malff 00:55:40 I have no idea where he stands.
Lalit 00:55:43 It could be from HotelPhp also, right? Probably just go to that directory and search it.
If you have it here?
malff 00:55:56 Oh, bingo.
Lalit 00:55:57 Hmm.
So everything is coming from the.
malff 00:56:07 So this… so this lens, yeah, so there is a way to… from C++ code to go back to PHP, it seems.
Lalit 00:56:14 Yeah, yeah, that's…
malff 00:56:17 Interesting.
Okay, so… I guess this is quite a few pointers to look at to understand the picture.
Lalit 00:56:49 Yep.
malff 00:56:54 Any other things you want to discuss quickly? Otherwise, we can just discuss it next time. I don't have anything special for myself.
Lalit 00:57:02 Hey, Mark, do we need to… Give, because those guys may be waiting for us to give some conclusions.
malff 00:57:09 Some feedback, yes. So, I will write a few notes with a few comments.
Lalit 00:57:15 Thank you, yeah.
malff 00:57:16 Mostly with a lot of questions as well.
Lalit 00:57:18 Yeah, yeah, please.
malff 00:57:19 But yes, they need to hear something from us, yes.
Lalit 00:57:23 Yeah, yeah, so then I'm not going to reply there, I mean, I'll wait for your reply to that.
malff 00:57:27 Okay, I, I…
Lalit 00:57:28 Thanks.
malff 00:57:29 I pushed something, Ben.
Lalit 00:57:30 Yeah, sure, thanks.
malff 00:57:37 Okay, so that was an unusual meeting, discussing everything but C++.
Fortune.
it's getting late, yeah, so anything else you want to discuss right now?
Lalit 00:57:55 And Nikhail, I think you do anything quickly you want to discuss? I think it's late at your… maybe if you've joined, if you wanted to discuss something.
Nikhil Bhatia 00:58:02 Yeah, actually, I wanted to discuss, with Mark that, On my PR, you commented, right, so, should I create another, detail namespace for, the hash part?
malff 00:58:17 Let me trick that… Yeah, so I'm assuming this is about this comment.
Just so… let's see… It looks like there is a hash implementation, which is part of that file, attributeProcessor.adafile. Just put it, it's inside its own header file.
Not inside attributes processor, because it's a generic hash function that can be reused elsewhere as well.
Nikhil Bhatia 00:59:05 Okay, so, exactly where should I book it? That was my question.
malff 00:59:11 Commons, I guess, should be a good place for that.
I'm not sure if we have a lot of things there.
some… some SDK comments.
You know, that… That looks like it's, it would be okay there.
Nikhil Bhatia 00:59:40 Yeah, okay, I can do it.
Okay.
malff 00:59:43 Thanks.
Nikhil Bhatia 00:59:45 Thanks, Mike.
malff 00:59:57 Alright, well… Thanks, everyone, Ben, and thanks for the… knowledge sharing about how PHP works, which is interesting.
Okay.
Thanks, everyone. Bye now.
Ehsan 01:00:14 Thanks, everyone. Thanks.
Nikhil Bhatia 01:00:16 Everyone, bye.
Lalit 01:00:17 Thank you, bye.
