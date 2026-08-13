SIG: Zig SIG
Date: 2026-08-12
Duration: 24 minutes
============================================================

## Zoom Recording Transcript

**Francesco Gualazzi** 00:03 We don't have a lot of computers going out, correct?
**Giovanni** 03:41 Hello.
**Francesco Gualazzi** 03:44 Hey, Dev!
**Giovanni** 03:47 Huh.
Are you on holiday?
**Francesco Gualazzi** 03:58 Yep, I am in the seaside, though.
I'm giving this And, and here with my daughter, actually. Do you see me okay, if I turn the phone like this? Okay.
**Giovanni** 04:16 Perfect.
**Francesco Gualazzi** 04:18 So, there is an interesting proposal from Bach Garage.
Yeah, that's true. In the hotel demo.
I was hesitant at first, because Apologies, because we don't have yet a stable API, if you really think about it, but… This is, this is a good idea to… to do the… and it's a good proposal. Actually, let me link this one here.
And then… By the way, Okay, let's discuss this one first. I haven't even opened the repo yet.
Let me see the issue… here it says, new Zig service to showcase Ziggo in Telemetry SDK. Nice.
Feature request. Open Telemetry Project as a feature SDK.
Although the project is in the first stage, it's worth a piece of demo written in Zig so that it can be available, a bank report, could be reposed via demo. I posted this initial result of ZRA and got positive feedback. If demo container sees this is not fit.
To add a new service, I can proceed with implementing it. Thank you for your attention. Well done, Barak.
I'm in favor of that, okay? Nice.
I think I can reply, we can just say… in the meeting here, Drandon, this is… Reaction from one maintainer.
of Hotel Demo.
So, BAC has already been contributing the SEMConv module, which I'm about.
**Giovanni** 06:09 Yeah.
**Francesco Gualazzi** 06:09 Unless you have an objection, Giovanni, I will just acknowledge it.
**Giovanni** 06:14 Yeah? Okay.
**Francesco Gualazzi** 06:15 Okay, squash and merge, and there we go.
Other than that, there's a… Wow, a storm of PRs.
**Giovanni** 06:27 Yeah.
**Francesco Gualazzi** 06:27 Look at this! Nice! I didn't expect that!
I… I would like to first… understand if you had the chance to review my follow-up PR to use lazy dependency in the portal module.
**Giovanni** 06:46 Not yet.
**Francesco Gualazzi** 06:49 Okay.
**Giovanni** 06:49 We can discuss a bit.
**Francesco Gualazzi** 06:51 Well, yeah, this is just a small follow-up of, another PR, which I could not…
**Giovanni** 06:59 Yay.
**Francesco Gualazzi** 07:00 I could not, I could not do.
I could not do it in the original PR, because force, force push are not allowed.
Lots.
And, because push are not allowed.
I… I could not… I could not rebase and, and add this change here, but this is… This is to… wait, files change 6?
Yeah, yeah, yeah.
So, basically, here, what I'm doing, I'm removing entirely the submodule.
to use what is called as a lazy dependency. Basically, the lazy dependency doesn't have to be built.
by the built system, it is.
**Giovanni** 07:51 It's fast.
**Francesco Gualazzi** 07:52 regularly via Git.
by the Zig fetch command.
And then it is cached locally, and only used if referenced in a project. So, only if a project tries to build something with it, then it tries to consume its… build.zig. Of course, there is no build.zig in that file, in that repo, but we use it as a package to just, get the proto files. So, because it's in the cache, we don't need a submodule anymore, and the build.zig Helpers have been updated to mention the cache path instead of the submodule.
**Giovanni** 08:43 Which is much better running days.
So, because I honestly relate, the Git models, so…
**Francesco Gualazzi** 08:53 I think it's a nice simplification, and the…
**Giovanni** 08:57 Yeah.
**Francesco Gualazzi** 08:57 Suggestion came from Antoine.
**Giovanni** 09:00 Yeah, Antoine, there's a lot of interesting things. I can approve if you want.
**Francesco Gualazzi** 09:05 Thanks, I would love to merge it, because I think it's a… it's a good, it's a good step forward on all the modules.
Also, I suggested that we use the same technique in the same variable.
In the SEMCOM module, sorry.
I quit.
Look.
**Giovanni** 09:25 But, for the… Let me check… come on.
Yeah, that's true.
**Francesco Gualazzi** 10:23 Let me know if you approve the Giovanni.
**Giovanni** 10:25 Yes, I put in, yeah.
**Francesco Gualazzi** 10:27 Okay. Hi, it's members of the call. Okay. Well, I can… I agree, I would agree.
Don't get from evil.
Hi, Will!
And then I'm very happy to see these new PRs.
This… Yeah, yeah, yeah, I know what this is. Thanks again, Giovanni, for the suggestion that you did, because when you told me that I should level with help wanted and good first tissue, then it really started to get people contributing.
**Giovanni** 11:18 Because people, it's, some, there are some software that are, scanning for projects for, these, tags, okay?
**Francesco Gualazzi** 11:28 Correct.
**Giovanni** 11:29 wanted, for help wanted, or… so, for this reason, I said this suggestion, because they use this kind of approach, okay?
**Francesco Gualazzi** 11:40 That's great, I mean, that…
**Giovanni** 11:42 The only problem, the only problem, the only problem is that we have to check, really, we have to spend a bit of time More than, let me say, a contributor that we have, it's come in our, SIG meeting, because, sometimes the contribution is full of, AI slope, so we should.
**Francesco Gualazzi** 12:09 Would be, yes.
**Giovanni** 12:10 We should take care about this stuff, because in some cases, also the contributors are kind of, let me say, fully automated, the contributors, so we should also take care of this kind of problem.
**Francesco Gualazzi** 12:26 I see, thanks.
I will, we'll have to find some time to… to look into this one. In fact, this is not straightforward to understand it.
Giovanni.
Giovanni?
**Giovanni** 12:56 -Oh.
**Francesco Gualazzi** 12:56 a toute.
Okay, I will, find some time to… to review this a bit more in depth. Actually, I see… Okay, it's a bit weird, because hex converts would be… Should be… should be straightforward without… without this.
Egg leaves.
Yeah.
Okay, thanks for letting me know. I'm happy that we have these more piats. I just need to figure out how to best invest my time.
**Giovanni** 14:14 Good job.
**Francesco Gualazzi** 14:14 Also, you know, I'm on holidays, so I will still be spending some time on the.
**Giovanni** 14:19 Yeah, this is… I understand, totally, and this is the first week that I'm back from paternity leave, so… I know the feeling.
Anyway, Francesco, I think that you should enjoy your, your, holiday, okay? I'll be here in the meeting if someone wants to join, okay? And in case I'll try to drive the discussion, okay? Don't worry.
**Francesco Gualazzi** 14:55 The only thing that I wanted to discuss is, is the profiles, so there is this issue.
**Giovanni** 15:02 implied, yeah.
**Francesco Gualazzi** 15:03 the profile signal, which is.
**Giovanni** 15:05 Yeah.
**Francesco Gualazzi** 15:05 It's going to be more and more… prominenta, more of you.
And I would like to see how… I mean, how to spend… how to drive the discussion about what needs to go.
in our own repo. Because, for example, one thing that could be very well suited, because of the… because of how Zig compiles to WebAssembly, is a visualization tool for flame graphs, for example, you know?
So, I would love to see a standardized way, although there is already some literature and some implementations. I would love to see one way that we can deliver visualizations of flag graphs based on the Open Telemetry profiles.
Signal data, data points, actually, because those are data points.
And visualizing a flame graph, or a heat map, or, you know, a sort of a library for… visualizing those type of data, that are coming from the OTLP specification.
And rendering them on the fly, you know, as they come, as they come, as they are ingested.
**Giovanni** 16:24 Woo!
**Francesco Gualazzi** 16:24 After they are aggregated.
**Giovanni** 16:26 Okay, if I understand correctly, what you want to… what you want to do is a kind of cite the library to draw the profiles, okay. But it's outside the Open Telemetry, or you want to…
**Francesco Gualazzi** 16:43 What…
**Giovanni** 16:43 Because it's the standard, I mean, maybe we can…
**Francesco Gualazzi** 16:46 Sanda is already there.
**Giovanni** 16:48 Yeah, excellent.
**Francesco Gualazzi** 16:49 The usefulness, let's say, of Zig with regards to profiles, aside from exposing the bindings, because, you know, there are… there are already some profiles that are entirely written in Zig. For example, microscope from Jim Calabro.
**Giovanni** 17:07 Hmm…
**Francesco Gualazzi** 17:08 And of course, they would benefit, they would want to use the bindings, which are already part of the proto package, if you want.
But we could be creating some abstractions to wrap the prototypes, the auto-generated types, with some functions, for example, I don't know.
gather… gather… gather CPU profiles, for example. Imagine this unique abstraction in the API of the repo.
That is used to take a handful, for example.
10,000 profiles coming for the same span of time.
And then it creates one blob of data.
that is used to feed a backend, or something like that, you know? So I would love to see… well, first of all, I would love to drive the discussion and see how Zig can be helpful.
**Giovanni** 18:16 -
**Francesco Gualazzi** 18:18 for C profiles, C++ profiles if needed.
And open Telemetry, so how we… how we augment the profile… the existing profiling ecosystem.
with our own repository. Okay, okay. So maybe we'll write some documents, maybe we'll write some design documents with.
**Giovanni** 18:38 Yeah. Yeah, yeah.
**Francesco Gualazzi** 18:41 And also, the visualization stuff is something that I think is very suited to Zig, because again, we can compile to WebAssembly, we can create an API that bridges WebGPU with WebAssembly, and, you know, there are very helpful things that we can do with regards to profiles in the ZRAP. It's not strictly… I have.
**Giovanni** 19:05 I have a question.
**Francesco Gualazzi** 19:06 tied to the SDK, you know, but…
**Giovanni** 19:08 Yes.
One thing that, I have a question, very simple, it's, do you know the others, what they are doing, you know? Like, related to… how to draw… draw the, the profiles, data… so… like, I don't know, go do something particular…
**Francesco Gualazzi** 19:36 No, usually, usually those are, like, proprietary stuff. So, Grafana has their own implementation, Elastic has their own implementation.
**Giovanni** 19:48 -
**Francesco Gualazzi** 19:49 Polar Sigras has their own.
**Giovanni** 19:52 Hmm.
**Francesco Gualazzi** 19:52 Either, either it be coming from BPF profiling, or, like, regular, runtime profilings.
But what… what I don't see, maybe there is, I don't know, what I haven't seen yet is a… single library under Open Telemetry that draws the… that defines the specification for visualizing the flame graph for the profiling.
**Giovanni** 20:20 Kidding, Janice.
**Francesco Gualazzi** 20:21 You know?
**Giovanni** 20:22 Yo.
**Francesco Gualazzi** 20:23 So that's something that I would propose.
**Giovanni** 20:27 Yeah, because I saw, for example, in the documentation that you pointed that Elastic open-sourced the desktop application called DevFiller.
**Francesco Gualazzi** 20:36 The filer, yeah, yeah, that's…
**Giovanni** 20:38 Violet.
**Francesco Gualazzi** 20:39 It's from my last two years.
**Giovanni** 20:41 Hey, so…
**Francesco Gualazzi** 20:41 That's a nice one. It's written in Rust, and it uses immediate, immediate UI, but that's limited to one file, so that's not… and for, files, or even aggregated profiles data. So if you have, again, a handful of machines that you are profiling constantly at a sample rate, there is… there is no… a single way right now to or a standard way to visualize all of this data in multiple ways. That would be, you know, frame graph is the most used, but there could be heatmaps, there could be San K diagrams, other visualizations that are helpful, in my opinion. You know, I spent… Five years in profiling.
**Giovanni** 21:31 I know.
**Francesco Gualazzi** 21:32 Very hot.
**Giovanni** 21:33 Yes, obviously.
**Francesco Gualazzi** 21:34 to the… to the topic, you know? So, yeah. That, again, let me… let me finish my holidays and wrap up in something to add.
**Giovanni** 21:43 I don't know.
**Francesco Gualazzi** 21:46 synergies.
**Giovanni** 21:47 No, no, no, because I like that you pointed the discussion about that, because again, I have time to take a look, and honestly, it's something that can help me on, on some stuff that I'm doing, because, I mean, apart from this kind of things, related to Open Telemetry, I'm working on, native build for the bid Zoom, so this kind of stuff doesn't work with JMX, so I have to use Open Telemetry or some, Profiler, in any case, to have the flame graph and to see, you know, at points.
So, this is a nice, stuff to… To… to… to take a look, so… Yeah.
Food for toads, so, yeah.
Anyway…
**Francesco Gualazzi** 22:38 Right.
**Giovanni** 22:39 I think that you should enjoy, yeah, you should enjoy your already… okay.
**Francesco Gualazzi** 22:47 Yeah, thanks. There is no… there is no really more to discuss, and it's just you and me, so… okay.
**Giovanni** 22:53 As a waste of the world.
**Francesco Gualazzi** 22:56 The hotel demo stuff from Bach is good, and again, I will try to find a bit more time to do the reviews of these new PRs that came in.
And then, and then, you know, working as usual, asynchronously in the repo, as well as in the Slack channels.
Okay, I haven't really made… been very vocal that the Open Telemetry SDK exists, I will… try to spread the word a bit more, and then this will even attract even more contributors, I think.
**Giovanni** 23:32 Yeah. For sure, the example is a good starting point.
**Francesco Gualazzi** 23:36 Total demo is a starting point that I enjoy, and Buck seems very proactive, so I think we gained one new contributor, which is always nice.
**Giovanni** 23:48 - absolutely.
**Francesco Gualazzi** 23:50 Alright, Giovanni… Enjoy the rest of the week, and your… family, family… days.
**Giovanni** 24:00 Yeah, exactly. Bye.
**Francesco Gualazzi** 24:03 Bye!
**Giovanni** 24:04 Goodbye, bye.
