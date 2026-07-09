SIG: Zig SIG
Date: 2026-07-08
Duration: 47 minutes
============================================================

## Zoom Recording Transcript

**Antoine Gagniere** 03:08 Good.
**Francesco** 03:15 Hey, how are you doing?
**Antoine Gagniere** 03:17 Great, and you?
**Francesco** 03:18 Not too bad, not too bad. I mean, doing fine.
I… we missed the last time together, no? Because, you were not here. And Giovanni, actually, Giovanni just, had his daughter be born earlier this morning, not sure if you know. So Giovanni is in the hospital with his wife.
**Antoine Gagniere** 03:45 Of course.
**Francesco** 03:46 Let me know earlier. How are you doing instead, Antoine? All good?
**Antoine Gagniere** 03:51 Oh, great, great, great, yeah. Congratulations to Giovanni.
**Francesco** 03:56 Nice.
Yeah, it's. I am already a father since a couple of years, three years now. And I have to tell you, it's. It's an incredible thing anyways. Yeah.
**Antoine Gagniere** 04:07 I am, I am since, what, 20 months?
**Francesco** 04:11 Oh, okay, good.
**Antoine Gagniere** 04:12 Yeah, it's intense, and yeah, I don't have a lot of free time recently.
**Francesco** 04:17 Yes.
**Antoine Gagniere** 04:18 Okay.
**Francesco** 04:20 So, yeah, today I wanted to talk about mainly, the… the change that I'm gonna… to make… I'm going… the change that I'm trying to make to the repo to make it modular, you know, so… to make it look like, Like, like, the last one, basically. I don't know if that's, The right thing to do, honestly, but, it seems like we have, we have a way forward.
I have a branch in my, what to say, in my… In my fork and that one I am preparing it to.
To raise the PR, but I want to get, you know, some ideas from you. Maybe, I don't know if it's worth, if you want me to show it to you directly, what do you think?
**Antoine Gagniere** 05:16 Yeah, I can look at it.
**Francesco** 05:19 Okay, so let me send the link. What is that?
**Antoine Gagniere** 05:23 Okay.
**Francesco** 05:24 I haven't created the PR. What is my fault?
Oh, it's down here somewhere. There we go.
By the way, I also fixed the… the documentation. So, the documentation now renders correctly in the link that is mentioned in the README, and Giovanni updated also the… the… the documentation, they read me with some interesting, interesting ideas, some interesting content, so if you take a look at this… Okay.
Okay, so this is what I'm trying to do, and again, it feels a bit awkward, honestly.
In the… it's not a regular… thing that you see often in Zig repos, but I think we can make it work somehow.
And how we make it work is the interesting challenge.
So… yeah. But, Let me know what you think, you know, let me know if you wanna go through it, Together, I don't know.
**Antoine Gagniere** 06:40 Yeah, so, so I'm guessing because Rust, they have this, notion of, I don't know, they call it like a monorepo, so they,
**Francesco** 06:49 Yeah, okay.
**Antoine Gagniere** 06:50 Okay. And okay, so in Zig. So yeah, for now, the build.zig is only in the SDK. Okay.
Makes sense.
**Francesco** 07:01 Yeah, yeah, there is no way, unfortunately, to… to run, multiple build.zig in the same repo, because when ZigFetch fetches one repo, it expects to find build.zig in the root and build.zig does on.
So, yeah, that's… that's what… I mean, we have to do it this way, unfortunately.
And,
**Antoine Gagniere** 07:29 But… And so we could have a bit.zig in each folder, I guess.
**Francesco** 07:36 No.
**Antoine Gagniere** 07:37 No, because.
**Francesco** 07:37 Because there is no way to specify A path.
That ZigFetch will have to fall.
**Antoine Gagniere** 07:44 Sure. Sure, but…
**Francesco** 07:47 Is there a way? You know a way?
**Antoine Gagniere** 07:49 No, no, no, I was thinking about the… Referencing the subfolder as… As packaged in the dot zone… in the root dot zone.
But yeah, I'm I'm thinking it through. Maybe it's it'.
**Francesco** 08:05 So the test that I did was… Putting the whole thing into a different, older?
I didn't test that, and it didn't work because, zig Fetch was saying there is no build.zig at the root of the project.
So that's what was happening, unfortunately.
**Antoine Gagniere** 08:28 Yeah, you're right. I mean, I'm looking at the branch you sent me, there's no build.zig at the root for now, so… Hmm hmm.
But I'm guessing you intend to put the…
**Francesco** 08:42 Isn't there what.
**Antoine Gagniere** 08:43 at the root.
**Francesco** 08:44 Wait a sec.
So that must be…
**Antoine Gagniere** 08:46 Of course.
**Francesco** 08:48 Oh, let me check. If I didn't, I'm an idiot.
**Antoine Gagniere** 08:52 Dude…
**Francesco** 08:52 Well.
**Antoine Gagniere** 08:53 your,
**Francesco** 08:54 Yeah, sorry for that.
**Antoine Gagniere** 08:56 There's no problem. It's your experiment, I guess.
**Francesco** 09:00 Yeah, no, but I wanted to, to push and I don't know why.
**Antoine Gagniere** 09:04 Okay. Yeah, yeah, yeah. Push, push. Sorry.
the…
**Francesco** 09:09 Okay, so… You.
**Antoine Gagniere** 09:15 But, like, what's the… Expectation from consumers of this repo, I'm guessing they expect the SDK?
then…
**Francesco** 09:25 There is SDK Proto and SamConf.
**Antoine Gagniere** 09:28 Right, but I'm guessing the expectation could be that the same curve is a dependency of the SDK, and…
**Francesco** 09:36 Not really, no, because you can use SandConf without the SDK. Also, in theory, the API should be a different module, but we can keep it, say, module in the sense of Zig module, and not a different, say, package, a different folder.
Right, right.
**Antoine Gagniere** 09:55 There you go.
**Francesco** 09:56 Yeah, I just pushed, see if you pull it.
**Antoine Gagniere** 10:00 Okay.
**Francesco** 10:01 Okay, now… Yeah.
**Antoine Gagniere** 10:06 at, To your multi-module?
**Francesco** 10:09 Yeah, well, wait, no, no, no, wait, I… I, no, I didn't push, I don't know why. Multimodule, non-fast Also, why?
**Antoine Gagniere** 10:19 to the folder.
**Francesco** 10:21 No, sorry for that. Yeah.
This one… the one that you were seeing was my first test, so I was trying to use ZigFetch on that test, and this is the error that I got.
**Antoine Gagniere** 10:37 Right, right, right.
**Francesco** 10:38 Let me show it. I can pass it here in the meeting chat, here.
This is what… this is what… this is what happened when I… Was trying to zig fetch, and there was no bid.zig in the…
**Antoine Gagniere** 10:50 Right.
**Francesco** 10:51 In the route.
**Antoine Gagniere** 10:52 So but so I'm we're thinking either we We have this rule, build.z.
**Francesco** 10:59 Mmhm.
**Antoine Gagniere** 11:00 be the SDK only?
And have the same company have their own SDK, or…
**Francesco** 11:07 Yes.
**Antoine Gagniere** 11:07 You want a big build SD, build SD.
**Francesco** 11:10 To be discussed, to be decided, honestly. I think there is no way, unfortunately, at least in 0.16, I know Andrew has been reworking that for 0.17.
But I think there is no way in 0.16 to call build from another build.
So you…
**Antoine Gagniere** 11:34 I have.
**Francesco** 11:34 Maybe I can, maybe we can do when I have to try, I don't.
**Antoine Gagniere** 11:38 Okay, yeah, yeah, I can. I can try. I will do experiments, maybe in about if I have time.
**Francesco** 11:43 Okay.
**Antoine Gagniere** 11:44 Because I mean, yeah.
**Francesco** 11:45 Yes.
Oh, please, go ahead.
**Antoine Gagniere** 11:48 No, no, I was just thinking, like, like, yeah, keep a single bill.zig, but it can… it can… Yeah, we can, like, yeah, the code of the build.z can be split in multiple phase, right? Just…
**Francesco** 12:08 Yes. Wait, I didn't push for that. Sorry. Build. Yeah, I need to add one more comment. Sorry.
**Antoine Gagniere** 12:16 Oh, de.
**Francesco** 12:16 Add build helpers. What I did… sorry.
Git push multi-module. What I did in this branch, and you should pull it again now, and you can actually run zig build here, because I didn't change the targets, so this is working for the SDK.
And what it has is, this build folder.
That is supposed to keep the build helpers for each component.
**Antoine Gagniere** 12:46 Nice. And then.
**Francesco** 12:47 There is the main folder of the module, which is OpenTelemetry SDK. The problem with that is that you can only get the package once. So when you do Zig fetch OpenTelemetry Zig.
it gets you, as a dependency, the name OpenTelemetry, which is what it is defined in line 9 of build-zigzon, no?
**Antoine Gagniere** 13:14 Yes.
**Francesco** 13:14 And from that one, you will… be doing in the build process of your own project, be dependency OpenTelemetry.module SDK, and then you get the SDK, you know?
So, for example… well, let me share my screen again.
**Antoine Gagniere** 13:35 Yeah, yeah, correct. This makes sense.
**Francesco** 13:37 Yeah, let me show you what I did here.
**Antoine Gagniere** 13:41 Yeah, I think it makes sense. Yeah.
**Francesco** 13:45 So… this… So… You see, once I pushed my changes, and I did that… I can do, again, zig, fetch, save, and this is going to be multi-module.
Oh, this is not the right one. Sorry. It's Yes?
**Antoine Gagniere** 14:13 Yep.
**Francesco** 14:13 So this works, you see?
Let me know if it's readable, otherwise I'll make it bigger. And then, what you get, like, in a sort of a test project, in your own build.zig.
Okay, you can do something like const SDK equal B dependency.
and see OpenTelemetry.
And then… you get… nothing here, I don't remember… Yeah.
Something like this.
**Antoine Gagniere** 14:57 Yeah, would you or?
Yeah, exactly. So, yeah, so it's a single… Yeah.
Edit.
And it's fine, yeah, I think it's good.
**Francesco** 15:12 I don't remember how I defined it. Let me check if I called it… How did I call it to you?
**Antoine Gagniere** 15:21 to…
**Francesco** 15:22 Yeah, I remember I exported the module here somehow, but add module… module.
SDK. SDK.
**Antoine Gagniere** 15:37 So…
**Francesco** 15:38 So in the other project, one would go and say, const SDK mod, module SDK, and then you're gonna use it, to inject in an import, no? So…
**Antoine Gagniere** 15:48 Sure, yeah, yeah.
That is…
**Francesco** 15:50 For example, here, imports, and then you call it .name, OpenTelemetry SDK, And then module becomes. So that seems doable. Actually, let me test this out. SDK mod, this is working. Basically, if now there was a build, this should work.
But it's also working because I don't use the dependency at all.
Well, let me try that, so the source… main.zig, I can go here and say in the main… I don't even remember the API now. I know, yeah, well, first of all, here I need to do const sdk hotel sdk import SDK, if not OpenTelemetry SDK, because that's what I defined in the build. And then I can go here and say, oh, Telemetry SDK.
Yeah, dot, metrics?
Yeah, there you go. So, meter… Provider, yeah, so const.
Meta provider, there is, init.
So… Whatever, standard, heap, SMP allocator, and then… the init, so init.io, no? Yeah, that's how we do it. So, you know, this should be working, and then I can do meter provider.
that, dot, dot, dot. Yeah, try. Sorry, I forgot that.
Because I want to see it in action, actually, you know? So, meter provider, get meter, and, without an instrumentation scope… Or maybe I know that I do need an instrumentation scope, so name… Esta?
Okay… So, const meter… So, okay, I cannot type.
Right?
And then meter… Finally, create counter. Okay, there you go. So, it's gonna be a signed 64, and a name, an example counter, and then this is gonna be a counter. This is gonna be a var, actually.
So this seems to be working, no? So if I can do counter.add… Why can I do Canteramba?
**Antoine Gagniere** 18:42 I'm guessing it's a low case. Yeah, low case.
**Francesco** 18:45 Is it? No.
Yeah, no, sorry, because again, I'm forgetting to do the try, and it's, the… like, under 24… And can be empty.
And this should compile at least, right? So… The build. Oh, okay, yeah, perfect. It worked.
So, what? Can I even do this? What is returning ad?
Oh yeah, no, last I can just say.
The bug?
I should be much faster, actually. But okay, yeah, this builds, and the… the… say, the proof, if I do… Dig out, been, Hasta tal ziga, grappa?
Yeah, there we go. Woo hoo hoo! Woo hoo!
**Antoine Gagniere** 19:54 Oh, it's… I'm surprised it… It has a counter of all those types included, even though you did not use them.
**Francesco** 20:04 Good point.
**Antoine Gagniere** 20:05 But I'm guessing you just have to build in release and they will not be there, right? In release, yeah.
**Francesco** 20:10 So.
minus The Optima.
**Antoine Gagniere** 20:15 I don't know, when you do zigbee, it's just dash dash release.
**Francesco** 20:18 Oh, really?
**Antoine Gagniere** 20:19 Small or fast, yeah.
**Francesco** 20:24 Okay.
**Antoine Gagniere** 20:24 Equal, yeah.
**Francesco** 20:26 I didn't know that. I was always using the optimize, which is the legacy way. Thanks for letting me know about that.
**Antoine Gagniere** 20:32 The the the optimize works when you use.
Build lib or build exec.
**Francesco** 20:40 Okay. It also works with ZigBuild, no?
**Antoine Gagniere** 20:43 Yeah, it also… yeah, correct, but it's… You can even set in the build.zig, you can set a default. You can say, like, if I'm built in release, I want to be really safe.
And then we can just build dash dash release.
**Francesco** 20:57 Beautiful.
Of course, it is taking forever in Lincoln, but okay.
You know what I'm talking about.
Okay, so this is what we need to agree. Is this okay? What do you think? I will open a draft PR.
**Antoine Gagniere** 21:16 Yeah, I think I agree. I would just wanted to propose that we can split the code, even if the behavior is the same.
like, instead of having a huge build.z, we can split it, but which you already did, right? You started to split it, with a build folder.
**Francesco** 21:37 Yes, yeah.
**Antoine Gagniere** 21:38 And so, yeah, I think it's the right direction. We can split it in multiple phase.
yeah. And I mean, initially, I thought maybe we could have what is specific to the SDK in the SDK folder, and what is specific to some code in some code folder. But if you put everything in the build folder, it's maybe even… more explicit.
**Francesco** 22:01 Yes, no, I think you're right. So you're suggesting, basically, if I go, let me get this on the screen. So So you're saying, instead of… Instead of, using, for example, this thing here, right? Define the static library.
in here.
and also… and also to install, you know, basically have a build step in the main build.zig that calls into something that sits in build SDK, right?
**Antoine Gagniere** 22:42 Yeah, but also, yeah, I I've been doing too much. See?
package with where it takes a lot of code. But here I must admit, yeah, it's quite short. So maybe it's not useful to split I'm guessing what takes a lot of slides are more like the build examples and tests.
**Francesco** 23:05 No, but you know what you said, that is very correct. If I want a build step here, that is, build the SDK.
**Antoine Gagniere** 23:13 Right.
**Francesco** 23:14 I'm expecting that it runs also the tests.
Fork the SDK.
So you cannot… you cannot build it without running the test, right? Do you think this is legit, or would you prefer to have everything split, in multiple, multiple steps?
**Antoine Gagniere** 23:30 Wait, you mean when you build it only bits, but it's when you build test?
It runs until.
**Francesco** 23:37 Okay, no, fine. Right now, we do zig build, and it does the build, zig build test, and it builds, sorry, and it builds and runs the test.
But if we are introducing more and more folders here, so there's going to be OpenTelemetry SDK, OpenTelemetry SandComp, OpenTelemetry Proto, now the test here becomes obnoxious. What are you testing? Which module are you testing, right?
So we can then either use build options, so, like, module X, but then we are forced to have The same set of build steps in every, in every component.
Or, we have… you know, per component steps. So build, Zig build SDK, Zig build SDK test, Zig build SDK example, and then Zig build SEMCOM test, Zig build SEMCOM, Zig build SEMCOM, you know, so.
**Antoine Gagniere** 24:39 Right, but I mean, the tests already have, a filter, right?
**Francesco** 24:47 Yes, they have a few. You can already.
**Antoine Gagniere** 24:49 filter test or maybe I forgot. Is there a way to No.
**Francesco** 24:53 Yeah, that is a way.
Yah.
There is a way to feature the test.
**Antoine Gagniere** 24:59 You are correct that when we do the build, it means install, and then it installs what? It installs all the libs?
**Francesco** 25:07 Exactly. So the build, what does it build out of all the components? It's a bit awkward, no? So that's the point where I think we need some consensus before I actually merge anything in the… in the code, because once we do apply a certain direction, then we… then we commit to it, no? So, maybe I will bring this into the Slack, actually, let me put this in the… in the…
**Antoine Gagniere** 25:34 It's true, I had opened the PR a long time ago, Be friendly.
**Francesco** 25:40 Yeah, no, I remember. Yeah, yeah, yeah. It's still there. It's still open, I think, in the old repo. Zig observability. Oh, by the way, nice haircut.
**Antoine Gagniere** 25:49 Oh, thank you.
**Francesco** 25:51 I just noticed now.
**Antoine Gagniere** 25:52 Let me think, find my old PR.
**Francesco** 25:57 Mmhm.
**Antoine Gagniere** 25:58 or maybe we already merged it.
**Francesco** 26:03 I think we did, yes.
**Antoine Gagniere** 26:05 Okay, yeah, I forgot about. Yeah.
don't have a very good memory. Let me let me.
**Francesco** 26:14 That's why we have logs.
**Antoine Gagniere** 26:17 yeah, I mean the Pr. About the build. Z.
**Francesco** 26:24 Mmhm.
**Antoine Gagniere** 26:25 Oh.
**Francesco** 26:26 There was… there was one open with the gRPC build options, but I think that's,
**Antoine Gagniere** 26:31 Yeah, yeah, no, that's another one. Let me check.
**Francesco** 26:35 the integration.
**Antoine Gagniere** 26:35 I found it, I found it, split building and running the integration, exactly, yeah.
is… Yeah, I think that's a bit the same idea. Actually.
**Francesco** 26:49 So let me write down what you just said. How do we agree?
On the build steps?
Multiple modules means… means we have to come up with a strategy.
To dispatch… Build steps.
to the upper module.
Also.
Uhm… We have to come up with a strategy. And then, yeah, confirmed that.
We cannot host.
Multiple.
build.sig slash build.sig.zone files in the repo.
We have to have one in the route.
What is weird is that… Standard build… I cannot call standard build.
On another build file. Yeah, no, because, yeah, because Zig does this, this wiring automatically. Never mind, sorry.
And the other thing, of course, is… Dispatchable steps and dependencies, so… Managing… Managing dependencies… E… then, Ross… module.
Let's see.
Define a strategy. Okay, I have, you know, I have some items.
written down.
And, yeah. Probably we bring it to the Slack. I'm not sure how much, Any other will be involved in this, unfortunately.
So the first point that I have in the agenda, I didn't do anything.
I have to create some social media posts to try to attract more people to the project. Let the people know that it's out there, actually. It's been accepted as part of OpenTelemetry. I haven't been very vocal about it.
Because I've been very busy at work, but I have to… Find some time to make it.
We'll make it.
**Antoine Gagniere** 29:14 Yeah, right, right.
**Francesco** 29:17 Also, if you have someone in Datadog also that is interested in… Lucky man.
**Antoine Gagniere** 29:22 Yeah, yeah, but… Yeah, the our opportunity team is small. So and then.
**Francesco** 29:29 Can you please remind me which team are you exactly in?
**Antoine Gagniere** 29:32 So the… in Datadog, there are two teams that work for OpenTelemetry. The one was… the historical one was, is, like, more involved in Upstream than my team.
**Francesco** 29:45 Okay.
**Antoine Gagniere** 29:46 They are, Like, basically working with, like, Tracy's SDKs and…
**Francesco** 29:54 All right.
**Antoine Gagniere** 29:54 Like, yeah, traces and such.
But my team is specialized in the collector side, let's say.
**Francesco** 30:01 Okay, thanks.
**Antoine Gagniere** 30:02 Yeah, in the… What runs on the… Customer machine on, like, on the server, right?
**Francesco** 30:09 Oh, yeah. Yeah.
**Antoine Gagniere** 30:10 a part of. So yeah, I'm not really.
Exposed to SDK that much?
But yeah, to the collector, we are really doing custom collector.
**Francesco** 30:21 Nice.
So, you're working a lot with Go, I suppose.
**Antoine Gagniere** 30:26 Yes, it's go. Yeah. So yeah, my colleagues are not doing so.
**Francesco** 30:31 Look, what would you say if I told you?
That I have a collector implementation.
In my, in 1 of my personal, play posts that I haven't made public yet.
**Antoine Gagniere** 30:45 Oh.
**Francesco** 30:46 And that is, able to run.
Processus.
supporters and receivers as WebAssembly.
**Antoine Gagniere** 30:58 I have also, but I did not go as far as you, I think.
**Francesco** 31:03 Oh, okay.
**Antoine Gagniere** 31:04 Yeah, I have this as an experiment, but I was a bit disappointed.
**Francesco** 31:10 Oh, really?
By the performance, or what?
**Antoine Gagniere** 31:14 Or, no, no, no, like, which runtime do you use?
**Francesco** 31:19 I wasn't typ.
**Antoine Gagniere** 31:21 Wasn't that? Yeah. So it's yeah. You use a better runtime, but it's not… Like, the OpenTelemetry community forbids Seagull.
So.
**Francesco** 31:34 Yes.
**Antoine Gagniere** 31:35 Like, like, yeah, your processors cannot be upstream.
in country.
in the collector complete.
**Francesco** 31:42 No, yeah, of course.
**Antoine Gagniere** 31:44 Let's say on a non-Go binary, right?
**Francesco** 31:47 No, no, of course. What I'm saying is to develop, I mean, to actually release a collector binary that is separate from the current OpenTelemetry.
**Antoine Gagniere** 31:56 Oh, yeah.
Okay, okay, yeah, because, wait, my experiment was to add like, wasn't capital… to an existing.
**Francesco** 32:06 Yeah.
**Antoine Gagniere** 32:07 Upgrad.
**Francesco** 32:08 I don't know, for that I used Wasiro actually.
**Antoine Gagniere** 32:10 Yeah, exactly.
**Francesco** 32:11 When I did it in… yeah, because that's pure go.
**Antoine Gagniere** 32:14 Yep.
**Francesco** 32:15 But that was really crap.
**Antoine Gagniere** 32:17 That was disappointing. Yeah, exactly. Yeah, so I think we agree on that.
On that, but even, like.
**Francesco** 32:23 Now I know what you… now I understand what you mean.
**Antoine Gagniere** 32:26 Yeah, but yeah, wasn't time is a good runtime, but, and I'm especially interested in the Z components.
Because…
**Francesco** 32:36 Yeah, yeah, yeah, no, that's… I haven't gotten that far. I just do… I don't do host interaction right now.
So, the exporters are just, working with, memory… memory passing, let's say, bytes from one to the other.
**Antoine Gagniere** 32:53 Okay, okay.
**Francesco** 32:54 And then the Zig part, and then the Zig part is doing the I.O. connection.
**Antoine Gagniere** 32:58 Exactly, because one of the limits is, like.
I want WebAssembly plugins for the most niche components.
**Francesco** 33:06 Yeah, yeah.
**Antoine Gagniere** 33:07 Our processor, performance-intensive processor, it's not…
**Francesco** 33:12 Good.
**Antoine Gagniere** 33:13 to use WebAssembly right there. So I want WebAssembly for the receivers, mostly. It's the mostly things that people Like, some customers want a specific receiver, but most others don't, etc. The problem with receivers is that you want to share a port, for example.
And for, like, yeah, for logs part of the receiver, and the trace part, and the metrics part, they all want to share the same port, but… They must be independent.
threads, and yeah, in WebAssembly, it starts to be… to become complicated.
**Francesco** 33:49 Yeah, no, it's… it's not easy.
**Antoine Gagniere** 33:52 Yep.
**Francesco** 33:52 But, the C… the C API for Wasm time is not too bad, and I was able to build that in the…
**Antoine Gagniere** 33:58 Ozone time is pretty good, yeah.
**Francesco** 34:00 Anyway, sorry for the diversion here. I would still love to see a collector module in this repo, honestly, and run a very simple Very simple.
comparison with the Go one in terms of throughput, unlike the EpiPath, you know, so gRPC receiver.
Log processor, and HTTP exporter, whatever, so the silly thing, huh? Or batching processor, and then, whatever exporter, like, Datadog exporter.
**Antoine Gagniere** 34:39 Yeah, okay.
**Francesco** 34:40 But yeah, let's keep that for another session. Now, do you have anything to discuss today?
**Antoine Gagniere** 34:48 I'm… I no, I do not have prepared anything.
**Francesco** 34:53 Okay.
**Antoine Gagniere** 34:54 If we could just, I would just check the.
list of years that I need to open.
**Francesco** 35:01 Yeah, there's a bit of backlog that we may want to… actually, no, let me ask you this. Do you want to take on… do you have bandwidth to take on adding the gRPC support in this current codebase?
**Antoine Gagniere** 35:17 Yeah, I guess it should be my priority, right? Okay.
**Francesco** 35:21 And then I assign to you this one.
**Antoine Gagniere** 35:24 Right, yeah.
**Francesco** 35:25 Number 13.
**Antoine Gagniere** 35:27 Okay.
**Francesco** 35:30 I'm not sharing the screen anymore. Sorry. But yes, issue number 13 in the board. I'm looking at this one.
**Antoine Gagniere** 35:35 Let me check the board…
**Francesco** 35:38 Yeah, I'm sending a link in the meeting.
**Antoine Gagniere** 35:40 Okay, good for you, nice.
**Francesco** 35:41 Sorry for that. I thought I was sharing.
**Antoine Gagniere** 35:45 Check the board. Yeah.
GRPC, yep.
**Francesco** 35:50 Okay, then I assign it to you, and you decide when to work on it. Again, no rush, there's no… there's no… There's no need to.
**Antoine Gagniere** 35:59 Yeah, yeah, let me create the tickets of for For example, so the resource detection, I had opened the PR in the old repo, so maybe I can create a ticket here.
**Francesco** 36:11 Okay, yeah, yeah, you can. I think you can. Let me know if I should first merge the PR with the new module structure, if, you know, if that's something that you need to depend on, which I think you do.
**Antoine Gagniere** 36:26 Yeah, yeah, yeah, I think you can merge first.
Okay. Yeah, yeah. And we can always improve later, like. Right.
Yeah, let, let… Exactly, because the PR I had opened in the old repo about the build.zig was because currently, when you do zig build.
Examples. It builds example, but it also starts ruining them.
**Francesco** 36:52 Yeah, yeah, yeah.
**Antoine Gagniere** 36:53 Yeah, and I prefer to have separate steps, because, yeah, to be able to.
**Francesco** 36:58 Oh.
**Antoine Gagniere** 36:58 them manually,
**Francesco** 37:00 Okay. I mean, building the examples…
**Antoine Gagniere** 37:05 without running them.
**Francesco** 37:06 Without running that, do we have any value for that? Because again, we've been abusing the example as sort of test in the past, but now we have the integration test. So what you're saying basically is compiling the examples will help, just compiling instead of running will help to… speed up surfacing some issues, but then allocations only happen at runtime, so… because we've been using the examples with, debug allocator, and trying to catch there some, let's say… Memory leaks that are usually not caught in unit tests. Well, whatever, let me know.
**Antoine Gagniere** 37:46 Hello, Abby.
**Francesco** 37:47 Maybe, yeah.
**Antoine Gagniere** 37:48 It's like, when they run, they run in parallel.
**Francesco** 37:51 Mmhm.
**Antoine Gagniere** 37:52 And, I mean, someday I wanted to run them, really manually, like, to really, like, use the binary path and run it.
**Francesco** 38:01 Okay.
**Antoine Gagniere** 38:01 One, only one of them, so that I can change the environment, or like… Because also, when I run on my dev machine, there's usually a collector running already in the background.
**Francesco** 38:12 I'm wrong.
**Antoine Gagniere** 38:13 And so it…
**Francesco** 38:14 1 is yeah.
**Antoine Gagniere** 38:15 Certain tests fail because they expect not to be a connector or whatever. So yeah.
**Francesco** 38:21 Yeah, there's a, there's a mix up there. Some, some examples expect a collector up and running and some use a mock at the stub.
**Antoine Gagniere** 38:28 So, yeah, so, I mean, it was, I, I wanted to split the build and run. Okay. To be able to, to run them manually.
**Francesco** 38:36 There's a filter, there's a build option that is called, examples filter, no? No, maybe there is.
**Antoine Gagniere** 38:43 Yes, but…
**Francesco** 38:44 Is that…
**Antoine Gagniere** 38:45 Still, there is, there is, but it's still, Runs, instead of just building, yeah, yeah.
**Francesco** 38:52 Oh, is it? Examples filter?
Oh yeah, because it's not used.
**Antoine Gagniere** 38:59 I mean.
**Francesco** 39:00 No, it is used, it is.
**Antoine Gagniere** 39:01 It is used, but it will filter which examples are built and run.
But it will still run those that are filtered.
**Francesco** 39:10 Okay.
**Antoine Gagniere** 39:11 About.
**Francesco** 39:13 Yeah, yeah, I see what you mean. Okay.
**Antoine Gagniere** 39:15 But yeah, I mean, okay, I will open a PR anyways.
**Francesco** 39:19 Yeah, again.
I have to… I have to, let's say, figure out… we have to figure out a good strategy for bundling all these These steps… In a way that makes sense for the… structure of the repo that we will have, which is, you know, one module, and maybe we could use build options, like, nested build options. For example.
Zig build minus the project SDK or OpenTelemetry SDK and the test step or a minus the step, whatever, for example, or, you know.
I don'.
**Antoine Gagniere** 39:59 Yeah, I feel it would be would complexify.
**Francesco** 40:03 Mmm.
**Antoine Gagniere** 40:04 But yeah.
**Francesco** 40:05 I will try to come up with something and, you know, open the draft PR and see what happens.
**Antoine Gagniere** 40:10 Yeah, yeah.
For now, I think, like, SDK-Test.
Or SDK dash examples, or something like that would be.
**Francesco** 40:19 That could work, huh? Okay.
**Antoine Gagniere** 40:22 Yes.
Okay.
**Francesco** 40:24 Nice.
What else do they want to touch base on? No, nothing.
**Antoine Gagniere** 40:29 Let me see. So okay.
Yeah, I see the resource, the detection. You already have a ticket for that.
**Francesco** 40:39 Resource detection, yes, I ported everything back from Zig observability into here.
**Antoine Gagniere** 40:53 So yeah.
Yeah, so you, yeah, you have the resource detection, I had the proposal of structure logs, and adding the source location, so maybe I,
**Francesco** 41:07 Yeah, that's also there, I think.
**Antoine Gagniere** 41:08 It's there? In the ticket?
**Francesco** 41:12 Not… I mean, that one references the other ticket, so… That's, that's…
**Antoine Gagniere** 41:19 Okay.
**Francesco** 41:21 Let me see.
So.
SDK support… independency dash… resource detectors, other runtime attributes, no.
**Antoine Gagniere** 41:36 Yeah, yeah, this one, yeah. Yes, okay. You have. Yes.
**Francesco** 41:40 Off detector, less detector.
**Antoine Gagniere** 41:48 Yeah, I mean, so yeah, I mean, this ticket is already there, so it's good.
**Francesco** 41:53 Number 17, right?
**Antoine Gagniere** 41:55 Yeah, exactly. But so I can create other ticket for the structured logs.
Oh.
**Francesco** 42:02 There was one, no?
**Antoine Gagniere** 42:03 Or structured logs.
**Francesco** 42:05 No?
Okay, no, maybe.
**Antoine Gagniere** 42:07 Let me… let me…
**Francesco** 42:08 I'm looking in the older repos.
No, there is none, no No, no, no.
**Antoine Gagniere** 42:15 It's a PR, not an issue, so…
**Francesco** 42:19 That's why, okay, yeah, yeah, yeah. Structured logs, yeah, yeah, yeah, I Yeah, now I remember, okay.
This is difficult to recall,
**Antoine Gagniere** 42:33 Yeah, yeah, it's been a while.
**Francesco** 42:35 Okay.
**Antoine Gagniere** 42:36 I should really get back on.
But, yeah, always a lot of things to to do.
**Francesco** 42:45 Take it easy, Antoine. So, for me, the gRPC… This is the most important thing, I guess. We all agree on that. And we already said that for now, taking on the C dependency looks good. And also, if you have this wrapper that is… Sitting in your, personal, Organization on GitHub looks good. If you want to move that into the repo, even better for me, but not a problem.
And, yeah, what else? Let's, let's put it out there first. Because once we have jRPC support.
And the SDK is working as expected, which we know it is, because we have all the testing and integration tests, and also I've been using it in… some capacity.
we can, you know, be really explicit that this project exists and people should be using it if they're using Zig, which is Already out there in a lot of projects, so ZML, Tiger Beetle, they might be using the OpenTelemetry official repo.
**Antoine Gagniere** 43:56 Yeah, yeah, I I yeah, I met the Zml team in Paris. Yeah.
**Francesco** 44:03 Good.
**Antoine Gagniere** 44:06 Then to Bezo. They use Bezo a lot.
**Francesco** 44:09 I know, I know.
I am in touch with Guillaume, the CEO and co-founder.
Nice. Also, Kemal knows him, so… I don't know how, though, but we said when I stumble in Paris, we're gonna meet in person.
**Antoine Gagniere** 44:24 Oh, that's nice.
**Francesco** 44:26 Do you also work in Paris?
**Antoine Gagniere** 44:27 Yes, yes.
**Francesco** 44:29 Bye. Then I will first meet you and then Guillaume.
**Antoine Gagniere** 44:33 Right, but Kemal is not in Paris, or…
**Francesco** 44:35 No, he's in Berl.
**Antoine Gagniere** 44:37 Oh, yeah.
**Francesco** 44:37 In fact, I don't know how they know each other, but okay.
**Antoine Gagniere** 44:42 Yeah, yeah, okay, okay.
But.
Guillaume or with Guillaume is The CEO, you mean?
cinnamon skew.
**Francesco** 44:55 Guillaume Le Strat, the CEO of ZML.
**Antoine Gagniere** 45:00 Oh, yeah, yeah, we could. I I know Guillaume, but I'm I was. I'm surprised it's called CEO. I thought, yeah, because I I was thinking about Steve to be the CEO. But Okay, maybe I'm just okay. I didn't know the the titles.
**Francesco** 45:15 It's okay.
**Antoine Gagniere** 45:15 Interesting.
**Francesco** 45:18 Yeah, I'm wrong. I don'.
**Antoine Gagniere** 45:20 Yeah, this is ultimate choice.
Okay, okay. Yeah, no, no, no more points for me. Good.
**Francesco** 45:30 Nice.
What else?
I think we… we happily end the meeting then, and whatever you can… whatever you can manage to… whatever you can do to… to bring the… the gRPC back, that's perfect.
Okay.
**Antoine Gagniere** 45:50 Yeah, yeah, let's, let's do this. So yeah, you, you open your PR for the build.
Oh, the new structure, yeah.
**Francesco** 45:58 I will do that, later. I… I have to figure out… no, I don't have to figure out anything. I want to… to do as you said, to… consolidate all the things that are for the SDK in the SDK build folder.
And not splatter them in the build of Zig and leave it a bit more clean.
So for example.
because I moved examples and everything else inside the SDK folder, but not integration test, I will probably leave just the integration test step helpers in the build.zig, and I will redirect to something in Build SDK for the examples and testing.
**Antoine Gagniere** 46:48 Okay. Yeah. Nice. Nice.
**Francesco** 46:53 Awesome! Thanks a lot, Antoine, and see you next time, then.
**Antoine Gagniere** 46:58 Yep, see you.
**Francesco** 47:00 Enjoy, bye!
