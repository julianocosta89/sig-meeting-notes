SIG: Arrow SIG
Date: 2026-04-02
Duration: 67 minutes
============================================================

## Zoom Recording Transcript

Saroj Kumar Patra 00:01:19 Hey, hi, Aaron.
Aaron Marten 00:01:24 Thanks, Rich, good morning.
Saroj Kumar Patra 00:01:28 Yeah.
Laurent Querel 00:03:26 Hi, everyone.
Aaron Marten 00:03:33 Good morning.
Albert Lockett 00:04:37 Hello?
jmacdonald 00:04:42 I look very pale in the screen today. Maybe that's how I feel.
You can hear me say something.
Laurent Querel 00:04:53 Cheers.
jmacdonald 00:04:54 Very good, very good, you can hear me.
Well, here we are, This is, I didn't realize that we have, because of the alternating Tuesday-Thursday, we end up having two of these query transform meetings between a Tuesday and a Thursday. Here we are. I have not been going to that meeting. Maybe we could ask once in a while for Albert to give us an update from that meeting.
Since he's here. But, not to put anyone on the spot.
It's like we don't have our… we can, okay, Honestly, just woke up today not feeling ready to run a meeting, but we can try.
Let's do our issue review, yeah?
Laurent Querel 00:05:44 Yes.
jmacdonald 00:05:45 Cool.
Laurent Querel 00:05:47 And this week, it was so…
jmacdonald 00:05:49 Yeah, like, wake up.
Alright, so today is Thursday, April 2nd. Last time we met was March 24th.
Fourth, according to the meeting notes, yeah?
Alright.
Well… And I know we have a lot of new issues, because this project is on fire, everybody.
Laurent Querel 00:06:16 this…
jmacdonald 00:06:16 So… let's work through them in, like, the reverse order. How's that?
As I recall, last Tuesday, we were, right about to merge Laurent's large PR called 2370, which introduced a second completion channel and began our work to solve some shutdown problems that we were having.
And… If we go back that far… I remember we probably talked about this introduced ACNAC failure handling, so there's a concern that each node has to handle its own ACNAC failures, and wouldn't it be nice if we had some sort of standard counting? Like, just to count how many of those fail? So we're moving in that direction. Sorry, I clicked the wrong thing.
But here we are on page 2, and then let's just kind of, like, talk through these. Protect direct callers and effect handlers. This has been done. If it didn't merge already, it should be closed. I'm not gonna worry about it. And thanks to, Samir, on my team, for doing that.
Further optimized coalescing of sets.
planning in OTAP. Albert.
Albert Lockett 00:07:33 Oh, we talked about this one last time.
jmacdonald 00:07:35 Okay, so I am an… I have gone back too far, is that true?
Laurent Querel 00:07:40 Yes.
jmacdonald 00:07:40 Good, good, okay.
Yes, now I'm remembering.
Laurent Querel 00:07:46 Yeah, this one we, I think has been merged with the work that you just mentioned.
jmacdonald 00:07:53 This one.
Laurent Querel 00:07:53 Oh, no, sorry, and also, Sleepy. Sorry, the unified internal telemetry around, I think this one could be interesting to discuss.
jmacdonald 00:08:07 Yeah.
Laurent Querel 00:08:08 That's okay.
jmacdonald 00:08:09 Oh, yeah, yeah.
Laurent Querel 00:08:10 We did.
jmacdonald 00:08:10 We discussed this last week.
Laurent Querel 00:08:12 Yes, okay, so…
jmacdonald 00:08:15 Totally awake now.
Laurent Querel 00:08:17 Okay, so that's a little bit.
jmacdonald 00:08:20 But that one is, well understood, and I'm personally hoping to get some work done on this topic, as a creator of SDKs and so on, OpenTelemetry Hat.
Okay.
And there is some interesting ongoing work in OpenTelemetry spec land. We've talked about bound instruments recently. We've also talked about context scope attributes recently, and I know that there's an issue coming up in this list about context scope attributes, so I'm going to get there in a second.
Okay… it's like I can't read today. Telemetry signal names… Okay, there's something… these are… these are, like, the long list of issues that you filed in association with 2405, so I'm gonna skip past many of these.
But not all of them were about metrics. We get to this orchestrate shutdown, ordering, And there's been, in the next page ahead of us, a few more new issues that you've filed about how to handle shutdown, Laurent, I believe.
And actually, since you've merged a couple PRs, I'm gonna skip past these issues now, and we'll get to your PRs. Does that sound okay?
Laurent Querel 00:09:28 Yes.
jmacdonald 00:09:29 Okay, moving quickly. Jake's been working on a temporal re-aggregation processor, and I've seen some of the PRs. Since I don't see him here, I will…
Jake Dern 00:09:38 Oh, I'm here, but nothing to share.
jmacdonald 00:09:41 Okay, good. Sorry, I'm not seeing… oh man, I'm having a bad morning. All right. Oh, I see 10 people now. Okay.
Okay, so this is, 2424 is in this list that, Laurent, we're going to talk about your PRs, and I'm going to ask you to do all of them at once. Lalit has opened something about process-wide memory limiting, and this is going to be a major focus for us over the next 6 months, I know that much.
Let's click and see what it says. Often we see people asking for a maximum in-flight or discontrol budget. Okay.
So this is asking for… some memory pressure controls, and so on. I fully agree. Does anyone want to discuss this right now?
Don't see Laowa.
Laurent Querel 00:10:31 Yes, I will be interested. That's definitively a topic where… We need some coordination.
Before to start the implementation.
jmacdonald 00:10:43 Yeah.
Laurent Querel 00:10:44 Yeah.
jmacdonald 00:10:46 I also need to come up to speed a little bit more. I know that we have capability of monitoring and limiting memory allocations per core, per… NUMA region and globally, and that, again, for me for the next 6 months, I know we have to do something about memory controls.
Laurent Querel 00:11:07 So… So the question I will have, maybe Laliti is not there, so… We can have this discussion of land.
But, I think there is one fundamental question, I think, that you can answer, Josh.
is, so, on the F5 side, what we target, but the platform that we target, Essentially, it's Binance.
So some advanced capabilities, if they work only on Linux, is fine for us.
So my question for you and the Microsoft team in general is, for this kind of advanced capabilities.
What, what are you, what are the… The perimeter, the scope of, those advanced functions.
Because we could imagine that they are only working on a specific grading system.
So that's the question I had, personally.
jmacdonald 00:12:12 I have to… I have to wonder what sorts of advanced capabilities we're thinking of right now, because I don't know, but I can also follow up with this.
Laurent Querel 00:12:20 So, when we talk about CGOO, for example.
It's a nice way to, to define, at the OS level, some limit.
For example, limiting the… The number of CPU cycle.
That your thread is able to, to use… So it's relatively straightforward to achieve.
For example, Docker, Docker containers, are using these kind of capabilities to… and then in Kubernetes, you can specify the number of minutes into you that you can assign to XYZ container. We can definitely, go in this direction.
And apply that at the pipeline level, super granular.
Which, in my opinion, is really great for us.
Because we want to build a really, I mean, a native multi-tenant pipeline system.
Which will be super fast, more fast… faster than if we have one process per pipeline, and then let Kubernetes manage that.
We have the entire control, and that's the direction we are taking.
It's achievable and relatively easy to achieve that on Linux. I don't know about Windows, maybe? I'm not familiar enough with Windows to know if it's a bug or not.
jmacdonald 00:13:52 Got it. Well, keep in mind that we do run a lot of Linux here as well, so even a Linux solution is good for us, but we do care about Windows, so I'll make sure we follow up. Lala did join us. Lala, do you have any thoughts about, we're looking at your issue here, and talking about whether this implies, I guess, advanced operating system-like features. Cgroups, for example, in Linux can let you control CPU.
Do you have any thoughts?
lalit 00:14:18 just now I joined. I mean, we're talking about this at process-wide memory, we are limited for… Home protection? Okay.
Yes, this, this was specifically when I, when I, I think wrote this issue, this was specifically thinking about the Linux… So it was… that includes the cgroups-related memory capping, but yeah, Windows, I even… I think I was not thinking much when I was writing it, but yeah, this should basically… should take care of all the three platforms, I mean, eventually.
So, I did do some draft, but that was totally on Linux, for Linux.
Laurent Querel 00:15:00 So, so Lanita, the… Andrew Schwar, the… not for now, but… I think we need to de- to, if both sides, Linux is definitively, one of the primary targets, I think we agree, based on my understanding of what Lalit said, and you said, Joshua, that we will, use as much as Linux OS-level mechanism, That could help us to… to, to manage those limits, either at the CPU level, at the memory level, and so on.
And, and for me, it's like… it's like a stretch goal.
to be able to reproduce that when that exists on Windows.
And I don't think on macOS, personally, on macOS, we need to work, the system needs to work, because a lot of developers will use macOS, But they will not use macOS to run at scale, the system.
And this kind of capabilities are more addressing the upscale and the obviousness of the system when you are in production.
So, it's perfectly okay, in my opinion, if… Some of those capabilities are just not supported, and it's relatively invisible, anyway.
they could be ignored. For example, if there is a configuration file defining a limit for the the CPU usage.
It does not really matter if it's not, perfectly addressed on my quest. So that's my.
jmacdonald 00:16:49 Have a warning, for example.
Laurent Querel 00:16:51 Yes.
lalit 00:16:51 Nope.
jmacdonald 00:16:52 For me, I'm interested in making sure that we have some way to make back pressure happen. Like, you're out of memory, we don't… we don't just want to start failing, we want to, like, push back, and I'll, you know, we'll follow up on this topic.
Laurent Querel 00:17:03 Yes.
Nikhil Manchanda (SlickNik) 00:17:05 So… This is, yeah, I just wanted to chime in. I think the direction here is great. I'm super interested, sort of, like, in it from a Windows perspective, and, the, like, I don't want, sort of, like, perfect to be the enemy of good. I think CGroups is a great, sort of, place to start with, and it would be… I'll be following, sort of, the conversation there fairly closely. There's equivalents on the Windows side, like the job objects and the job API, and so on. We'll have to figure out, sort of, like, how we can map those equivalents in terms of the conversation that we're having with cgroups, and how this will sort of, like, ultimately, figure out the plan for Windows, right? Like, so, so I think what we have, starting with cgroups is great, and we can start the conversation there. I think it's important to do that and sort of make progress, and then we'll have folks on the Windows side also sort of engage and see, sort of, okay, what are the parallels and how we want to look at it from a Windows perspective.
Laurent Querel 00:18:05 That's it. I mean, I'm super happy to have Microsoft with us.
To, to make Windows a first citizen in this solution. That will definitely be, Excellent for the project.
jmacdonald 00:18:20 Thank you, thank you. Alright, well, let's move on then. Thank you, Nikhil.
So this is… there's a few issues that I'm going to kind of summarize and go past. So, Laurent has done a bunch of work on, bounded completion and shutdown here.
And so there's some issues covering that. I also want to skip past the ones about exponential histogram, because I keep talking about it. It's sort of a topic that I'm very interested in, and you don't have to be.
But we have some work in progress there, and it's going to pause while we work on our internal telemetry story for metrics. We can't really instrument the exponential histogram right away.
Again, another one of Laurent's issues, we're gonna let them all… we're gonna batch those all together. And then, wow, a whole other page here. Okay, skipping past strength and shutdown, prevent shutdown, again, again. Okay, let's talk about Drew's issue.
We are getting rid of a dependency on the Go collector, as it complicates our build in a huge way. If you care, you can follow up with these two issues, but it doesn't matter.
Laurent Querel 00:19:21 Good news.
jmacdonald 00:19:22 Again, I'm not going to talk about exponential histograms.
Lalit has done some work, and this is interesting, I think we should talk about it. There's a PR open, but I'd like to hear it sort of in words, if you wouldn't mind, Lalit.
lalit 00:19:35 Yeah, this is basically… I mean, we want to use… I mean, if we want to use the hotel arrow, as a library.
There are lots of… common constructs in the… in our main.rs, which probably should be shared as a library so that we can use that.
So this basically is some small scope of functions which we can… Make it available for the libraries to use it.
jmacdonald 00:20:05 Alright.
Laurent Querel 00:20:07 Yeah, I read the PR yesterday, I'm fully supportive.
the, yeah, we have the same, basically, setup, that you are… that you are following.
We, on our side, we have an internal, Rust collector.
reusing, massively this, OTAP, data flow engine.
And, the idea of… Moving the… what will make sense for any person creating a search risk collector?
for their own purpose, and creating a library, That will help, basically combine those main components. I think that definitively makes sense.
I suggested something, in your PR edits, I don't know if you already saw it, but, I'm… I'm think… I was thinking about, collude function or, Some kind of attribute macro that we can put on top of the main.
To basically encapsulate the code, and add, for example, the crypto initialization automatically, and in the future, we have to do some additional pre-initial aviation, like that. That should be transformed for the… For people that are creating a search collector.
lalit 00:21:39 Got it, yeah. Yeah, let me go through the PR comments, and I think that looks to be a good idea, yeah.
jmacdonald 00:21:45 Thank you.
I marked that one accepted, I'm doing my job here. Let's see.
Where were we? We were here… okay, so exposing observed state handler for… okay, so I happen to know what Lalet's working on, and this is one of our efforts to integrate our code with other libraries and other main binaries and so on. Any particular notes about observed state handle, Lalet?
lalit 00:22:11 No, it's just that, I know we can get the state of the pipelines through admin, port, but I think, this is something which is already as a library, we don't need to… hit a port and get that, state. Instead of that, if you can just call the library functions, it would be more straightforward. Something which is already available in the memory.
instead of going through the HTTP, directly get to the state. So, the PR which I have raised actually is… covers both these issues.
jmacdonald 00:22:41 Got it.
I have thought to myself, I know that we've been doing some benchmarking to determine what's the lowest amount of memory we can use, and it makes me think, oh, I should turn off the admin handler, because that's going to take memory if I don't want it. Maybe.
And it makes me think that this is an alternative that would be slightly less resource intensive than the admin handler, and maybe I'm wrong, that the admin handler doesn't use very much memory.
Laurent Querel 00:23:08 So… On default, The long-term solution that we discuss is, reducing the internal… our own pipeline engine.
To process, internal telemetry.
And the… one of the reasons of doing that is to have a very flexible internal telemetry pipeline system that will be able to leverage all the flexibility and the And the capabilities that we offer for regular telemetry.
And that will also mean that we will create some very specialized processor or exporters, just for the purpose of internal telemetry. Some of them will be general enough To, to be used by a regular, telemetry system.
So why I'm talking about that? It's because… so that's perfectly okay to use the, the observed state handle for now, and I understand why Lali did that.
I think any big modification that we want to apply to this current observed state system, I think we need to think about it two times instead of one, because we know that long-term, we will go into this full integration with the pipeline system.
And we need to prioritize, in my opinion.
Okay, is it a great value to invest a lot of time there, or do we want to invest more time for the migration, and then we will end up with… Relatively, generalized system.
So that's the maintenance, we're getting that.
jmacdonald 00:25:02 I think I follow… I mean, the idea being that instead of having this sort of special object that's having sharing semantic problems right now, we would just… in the long term, we will put all of our events into a pipeline and take them out as any other consumer of events would, meaning we have an internal Like, some sort of bridge from an exporter, as you said, to our state.
that was a custom exporter. It makes sense to me. It doesn't sound like a priority.
To go there, so…
Laurent Querel 00:25:33 Yeah, so, the, the, the… An example where Lalit used the observed state handle, it's… Lalit created an example.
So basically a basic cross collector, a basic cross collector, as an example. And, and this… in this example.
if I remember well, the… the system produced on the… in the terminal, the console, displayed, some event or some matrix.
Related to the, to this internal, telemetry system.
We could imagine exactly the same thing by manipulating the internal pipeline definition.
And then we'll end up writing into the terminal exactly the same information.
Without even, having a need to get access to this handle. That's, Yeah, so if you look at the example, custom collector, on the left, Yeah, you are… yes, this one is basically writing on the terminal, Some information that are produced from the observed state on the…
jmacdonald 00:26:54 Is there a callback somewhere? I'm not seeing it.
Laurent Querel 00:26:57 Yeah, here, the… I think here you have the… the thread…
jmacdonald 00:27:00 There it is.
Laurent Querel 00:27:00 Yes, sir?
jmacdonald 00:27:01 Lost my screen.
Laurent Querel 00:27:03 Yeah, and it's basically asking for a snapshot and displaying the snapshot every 5 seconds.
What I'm seeing is… That could be achieved at some point, not now, by changing the configuration of the internal telemetry system.
With a special exporter to display the same information on the console.
jmacdonald 00:27:31 Got it. I… I think this is good. So, short term, we're just gonna have to figure out how to, like, negotiate the… the, like, not-quite-perfectness of our solutions.
But, I think we should move on. Thank you.
Okay, so… I've… so we have some flaky tests, let's assume they're going to get fixed. And I've said I'm going to skip over all of Laurent's issues so we can talk about them all at once. I want to get to the top. Centralized runtime version, okay, so this is a topic that's actually pretty important to a bunch of people in this room.
is that… we are… Trying to figure out we're sort of limping along using the DF engine binary right now, and its build process is a little bit… brittle or static. Like, we need to be able to control the version numbers right now, and it's hard… we don't have a proper release process. So, I was just, there's been some discussion in here about whether we would use a build info crate, or whether we would hack our build or Xtask system to… Copy other environment variables, or we would… Point is, I actually don't understand what's best, and we've been talking about it, but I'm gonna presume that people in this room can help us solve it.
Laurent Querel 00:28:50 So, I sent you, did you see my message, regarding.
jmacdonald 00:28:55 Yes, you did, and I, I.
Laurent Querel 00:28:57 Okay.
jmacdonald 00:28:58 So there are a couple of versions. This is roughly what your… your message to me was. I actually… this… we were DMing about this yesterday.
Laurent Querel 00:29:05 Yes, and, and I reviewed, many well-known projects, just to… To figure out the trend in this space.
And most of the big projects, they are basically not using any dependency.
And they are just creating a build.errs, which is a standard pattern.
And using the cargov.
And, and adding the information that they want.
That's definitively, it's not too hard, and there are many, many examples.
jmacdonald 00:29:42 no dependencies for that, so that sounds good. I couldn't find what you were looking at, but I'm not an expert.
Meaning, I went and looked at some of those projects you named. I didn't copy them because I couldn't figure out what you were looking at.
Laurent Querel 00:29:56 Yeah, Zed is an example, the editor, yeah.
jmacdonald 00:30:00 So if we go look at the Z editor, we'll find a cargo and a build.rs somehow.
Laurent Querel 00:30:04 Yes, yes.
jmacdonald 00:30:05 Plenty of problems.
Laurent Querel 00:30:06 Yes.
jmacdonald 00:30:07 I'll leave you.
Laurent Querel 00:30:08 Otherwise, Shadow ARS is probably a good option.
jmacdonald 00:30:11 Okay.
Laurent Querel 00:30:11 But, definitively with a much more…
jmacdonald 00:30:15 So then, moving forward.
Laurent Querel 00:30:16 This is a…
jmacdonald 00:30:16 Gokan is here with us today and, has been focusing… sort of investigating the same prop- property problems that you have been, Laurent, and we've both seen the document, but this is here for, you know, everyone else to read.
This is, I think, a proposal that is similar to yours, and I'm sure complementary.
And it's nice that… I don't mind that we're sort of… repeating each other's work at this point. I think this is an exercise in learning a lot. So, this is Gokan's, presentation of the same. Now, you… I skipped over all of your issues, so I feel I shouldn't dwell on this one too much, but Gokan, I wanted to know if you, would like to speak.
Gokhan Uslu 00:31:03 Yeah, so… Last, week, Lauren told me to, you know, share how I think the message channel could be simplified, and basically.
I figured that, the message channel, Mainly takes care of sending synthetic shotgun and drain deadlines, etc.
And I looked into how to sort it out.
And while I looked into… while I was looking into it, I also ran into situations in the code that seem like good cause, you know, during shutdown, due to… use tuition dead.
It's like race condition, correct me if my understanding is wrong, but… And, because of that, I was like.
Updating the shutdown process in a way that prevents data loss.
When the shotgun can be handled gracefully, obviously, because 50 shut down.
And not the end of this fully within the… Timeline that it is given, then they tell us to always happen, but at least I figured that, Changing the shutdown sequence.
Could have the… how the drain is done, and also unwinding egg necks for the client, eventually, without missing I'm losing any of them as well.
Bye.
You know, this coming up, like, this… Two-phase, shutdown, mechanism, which, you, thresholds are up, because in the alternatives I mentioned, what approached them, I had Starting with, progression on it, which will happen to utilize for that.
The data loss, can happen.
Anything that was, you know, work that I was… During so, you know, came back with this design approach where, because the data flows both ways, you know.
The reigning, of the… P data, and, you know, fleshing out the state of which company could be done in the phase one, where the shutdown is handled in topological order.
And because ACMACs travel and go in the backwards.
This Black Max could be handled in the case here, where the shutdown is to go in reverse topological order.
Respecting the dependency order, of course, occupied, because, you know, this is just open.
jmacdonald 00:33:46 Thank you. Go, Ken, I'm having a little trouble hearing you. I think I understood almost all of that, but I just want to question your microphone. I also, Just want to say thank you. I appreciate the investigation and the summarization here. I understand the big idea, I think, that you were just summarized is that there's a two-phase shutdown, where you start something, you start draining things, and then you report that you're done. You have to do this in topological order.
There's two phases, etc. I don't… I want to give Laurent a chance to, go through his issues, which overlap with this mightily, and I don't… and I hope that we can then have a fruitful conversation on top of that.
Gokhan Uslu 00:34:30 Yeah, just to… one to add to that, it seems to me like, based on, you know, quickly skimming over, what Lauren has been doing, has been doing, this, this is… Yeah, a little bit overlapping, but it has the complement the aspect to the data also.
It was close to working, but, you know, having a time getting everything before that.
jmacdonald 00:34:55 I've got my volume all the way up, Goken, I'm having trouble… little trouble hearing you.
Laurent Querel 00:34:59 Yeah, no.
Gokhan Uslu 00:35:02 Yeah, sorry, I'm, outside right now, sorry. I'll mute.
jmacdonald 00:35:07 Okay, well, so, this is progress, and this is productive, thank you. I want to… let's see, I'm aware that there are at least 15 more issues in front of us, and I'm, like, looking at the time, and I… So where were we? I'm gonna skip some of them. License, we need to be fair with licenses, and recently we added the Boost Life software license, and I'm not sure it's perfect, but it requires us to do some stuff. And we still have some CNCF questions.
Laurent has asked for the status, the endpoints to be versioned, and there's a co-pilot PR trying to do that.
Laurent Querel 00:35:46 That's an experiment, but outside of the experiment, I just want to make sure that it's not a problem on your side.
jmacdonald 00:35:57 I did not see a problem. The only thought I had was that usually Prometheus, people expect it to be on slash metrics, and maybe that could be an alias.
Laurent Querel 00:36:04 Yeah, we could have, we could have an alias, for that. But on Kubernetes, you also have the slash API slash V1 or slash V something.
So I just want to make sure that I will not break… It's still early for the integration production, I guess. I don't think that's right.
jmacdonald 00:36:28 anything for us. Okay.
Laurent Querel 00:36:29 Perfect.
jmacdonald 00:36:31 There's a duplicate filed here. I happen to know what it's about. It's related to your PR2466, which introduced some duplication, I think. I want to lump all of your conversation together, Laura, if you don't mind. Let's move past.
columnner, Albert's done some case-insensitive work. It looked really cool. You keep talking about what Arrow and Data Fusion do. Doing better.
the, there's been some flaky test issues. I want to get to the ones that matter here. Allow selection of metric views with scope name. This is… Drew, are you here? I read it. I don't think that we should dwell on this, because it relates to the OTL SDK, which we're going to try and remove.
So I'm not gonna… and we're low on time here. There was one I really wanted to get to, though. Okay, so Andres is in the call, and we've had a discussion Well, he may be in the call. We've had a discussion about, documenting our metrics, and the Go Collector has a metadata file, and it's, like, all very automatic and nice. We filed this because right now we're doing manual documentation. It's not perfect, no one loves it, but it's better than nothing.
And this is about how we should follow the suit, or, you know, go with… the program, we should be auto-generating our documentation, and Laurent has some ideas about how to do it with Weaver, and I think we should take this conversation offline.
And, okay, so where…
Laurent Querel 00:38:03 Just one thing.
jmacdonald 00:38:06 Yes.
Laurent Querel 00:38:07 So, semantic convention format is… is official for OpenTelemetry.
And using Weaver will give us… in our CI pipeline.
way to check the instrumentation of our own code, because with the semantic conventional G3 or telemetry schema.
We will express, basically, a contract saying, oh, that's what the system is able to produce in terms of telemetry.
Weaver will be initialized with that, with a special command, to listen on OTLP, It doesn't supportotap right now, but let's say OTLP will be enough for now. And in the CI, every test could be configured in a way that every telemetry will be produced and sent to Weaver for tracking and check. And that will give us, basically, for free.
the equivalent of a test coverage that will be applied to instrumentation coverage, and I think that will be great help. We will see any gap between what we document and what is the reality of the instrumentation.
jmacdonald 00:39:19 I like this.
Laurent Querel 00:39:20 And there are many other things that… and by the way, we are already using Weaver for the traffic generator, for example.
jmacdonald 00:39:26 So then, would you say that the documentation lives in a completely separate place? We write the documentation of what we expect, and then.
Laurent Querel 00:39:32 No, no, the documentation is generated from a semantic convention file, which describes it's more… it's richer than the… the M data gen, 5. But that's the… the… I wouldn't.
jmacdonald 00:39:50 So, we will…
Laurent Querel 00:39:50 The same idea, but relatively close.
jmacdonald 00:39:53 I think I get it. I think the idea, though, is that we're not going to, put our documentation strings in the source code. We're going to put them in a semantic conventions file.
And then we're gonna test that the code produces the semantic conventions that we put in the file.
So, somewhere in our code, I don't want to find it right now, there's a… there's, like, a Rust macro that says, I'm a metric. Below is the… here's the name of my metric.
We will not be putting, here's the description of my metric. We will not be generating descriptions from source code. We will be generating descriptions.
Laurent Querel 00:40:26 Yes.
jmacdonald 00:40:27 Say what the names are, and give the documentation.
Laurent Querel 00:40:29 So the process is entirely described in the telemetry doc that we merged more than one month ago into the repo, so it's not a new thing.
jmacdonald 00:40:43 As if.
Laurent Querel 00:40:43 Because I… yeah, I take the time to describe this process, It's not this telemetry at .md, there is an entirely, yes, that's here.
There is, in docs, a telemetry folder with a lot of files describing the… The direction, and describing also the principle that we try to follow in this project.
jmacdonald 00:41:10 Not the top… we've got two docs directories, that's a.
Laurent Querel 00:41:12 Yeah, yeah, it's in the… not the tab, the… I'm basically always referring to the doc that we have into the OTAP engine.
jmacdonald 00:41:20 Okay, here.
Laurent Querel 00:41:21 Yeah, yeah. So, that has been reviewed by many people.
And inside, you have, something talking about, Weaver and how we could integrate it. For me, the long-term vision is The code that we have into the… into the source tree.
some of this code will be generated from Weaver. Weaver is also a code generator.
And it will generate exactly the same code, so that the… what I'm saying is… What we have in the code today that has been manually created.
will be basically created, exactly the same way, but by WIVER, on, a telemetry schema or semantic convention regime.
jmacdonald 00:42:06 I see, I see.
Laurent Querel 00:42:08 So, yeah, so, that doesn't change anything on what we have today, except that the source of truth will be those YML file representing the single, and… but the client… the internal client SDK will be exactly the same that we have today.
Because with Weaver, you can generate code, doesn't need to be a regular open telemetry Client SDK, or based on that. It could be just… Rust code that, is generated from this telemetry schema.
jmacdonald 00:42:49 Is it using templates and so on?
Laurent Querel 00:42:51 Yes.
jmacdonald 00:42:52 Yes, very good. Sounds neat.
We're almost there, everybody.
I thought I was gonna find one… oh, this is it. This is the one I wanted to discuss. So, the title… makes sense to me, but only because I read it once. And I want… this is where I want to bring in, a connection with what the Oakland Telemetry Specification Group is working on right now. So, just for… for everybody else here, gRPC and HTTP requests come in with headers, and it's very common that we want to take those headers and turn them into telemetry attributes, and I think this is what this is about.
I… this was filed, like, yesterday, so I haven't read it entirely, but I saw the, sort of.
Laurent Querel 00:43:37 We can talk about it if you…
jmacdonald 00:43:38 Yes, why don't you talk about it, and I will find, at, while you do, a link for us. Please.
Laurent Querel 00:43:46 So… For one of the internal projects we have at F5, we need this kind of, a capability, which is the ability to transport, for example, trace ID, Across the… our pipelines.
So the… similarly to the GoCollector, the GoCollector can, play a role of, for sort for the trace ID context.
We want to do the same thing, so we… It could be, either the traffic coming with a TLP, OTAP, or some other receiver.
That have errors attached to their message.
And those headers need to traverse the pipeline, and whatever, exporter Using transport compatible with this capability of adding an error on a message.
All on the Dutch.
We'll retrieve the header from the PData object, and we'll reattach, reassign those headers. So, for example, a W3C trace context, a V3 trace context, or… Whatever, interesting header could be, authentication-based, headers, all this kind of stuff.
need to traverse transparently the pipeline. That's the purpose of that.
And, I'm trying to… To integrate that in a very generic way.
Because it's… it's not… Only a configuration for a TLP receiver and exporter.
It could be applied, in fact, to any… Receiver-exporter, leveraging a protocol where headers are a thing.
So, so that's why I… I try to imagine this, configuration as a policy, because we have, no, A policy-based, pipeline engine.
that… and this configuration is hierarchical. We have the engine level, the group level, the pipeline level, and that's a way for us to basically group some configuration For multiple pipelines inside one group, or at the global level, engine level.
So, so I, I identified, How to extract headers, and how to… propagate those headers.
And, they are both represented as policy that could be applied, like I said, at different levels. Ultimately, they can be applied to a specific node instance, if needed.
jmacdonald 00:46:42 So this is, I brought up an issue that's been debated recently. I just approved this PR myself yesterday. This is, an old idea that kind of never gained enough traction, because it was sort of I think early… too early in the OpenTelemetry history, but this was one of the most popular OTEPs for years, basically saying, we want a way to, like, add tenant information from the context to everything. The span, the metrics, the logs, whatever it is, so that the idea of a generic context scoping mechanism has been wishlisted for so long in OpenTeometry, whereas if you ignore this topic, what you have is trace… the tracing spec talks about context, which is sort of a general-purpose mechanism for what we call a cross-cutting concern in OpenTeometry. So you always have a context, and then it has in it a span context for your distributed tracing instrumentation. And there you get the trace IDs, the trace flags, the… The trace state, the baggage, like, the standard stuff.
But then, that's not enough. Like, people want custom attributes. So then you… then you look at, like, the collector architecture, and you've got… gRPC and HTTP can each give you what we call client metadata, and that's just a set of headers behind a sort of opaque like, interface, so that you can't see them. You can ask for them by name, but you can't iterate through them because there's sensitivity. There's, like, security questions and so on. So, so then you're in the collector, and you've got this keys and values baggage, but it's not the same as the OpenTelemetry context. And… So what I pulled up is that what we're discussing in OpenTelemetry is essentially the policy that you sort of described, which is, like, how do I, as an operator of my collector, say which attributes I want to put on my telemetry?
Because I know I have tenancy, for example, I need to put my tenant ID on all my metrics, so here's how it would be done, and you'd have, like, this is a list of attributes which you would like to admit as context that can be automatically added to every piece of telemetry on the pipeline.
So this is the closest thing that I could imagine to what you just described about a policy. This also runs into, we should… we should move on, because I know I talked about it, but this also runs into If you look at how rate limiting is done, especially multi-tenant rate limiting in places like Envoy, you will end up having a split between concerns. You have one piece of configuration that says, what are the attributes you're going to use for your rate limiting decision, and how do you get them? And that will be different depending on which protocol, or which endpoint, or which path you're on. So that you have one piece of configuration, which is the policy for extracting the keys that you care about.
And then another piece of policy, which is, like, how do you do rate limiting based on the keys that you've already extracted? So that you end up with configuration almost like this to say, how do you get the keys for your rate limiting decisions later?
again, it's from the headers, and so I fully agree, this is an interesting area. I hope I've not slowed us down by saying all that.
Laurent Querel 00:49:44 So, so just, complimentary information on… on this topic, and what I was discussing before. So, the terminology I used is transport headers, but I'm totally open to, Personally, I prefer transport headers, because it's not necessarily client. Any proxy in between can add headers.
And, it's super important for us to get that in one week.
jmacdonald 00:50:14 I'm not gonna slow you down.
Laurent Querel 00:50:16 We can discuss, but not too longit.
jmacdonald 00:50:19 Okay.
Laurent Querel 00:50:20 And, and the other thing is, this thing described… Propagation of headers, in a non-participant way.
I would, for… let's… in the context of distributed tracing.
you could have a transport mechanism, like the GoCollector, for example, is, transporting or propagating the trace ID and span ID transparently. It's not participating To this trace.
is not participating, because its own logs are not tagged with the trace ID coming from the incoming telemetry. That could be done, and it's a separate, for me, it's a separate, task that we will also… on which we will also work at some point, because we need that on our side.
jmacdonald 00:51:23 So you're not trying to trace the data flow engine, you're trying to let your customers trace information pass through it.
Laurent Querel 00:51:29 Exactly the purpose of this one, but it's designed in a way that we will be able to leverage this infrastructure to achieve exactly the… the, the second step, which is, you are in a processor, and, and the specific P data, There is an issue inside, and we have a log, a structured event.
are saying, oh, this, this thing does not comply with XYZ rule.
The log that will be generated if we are in this participant mode.
we'll take the trace ID and span ID and create a log event with the… reusing this information. So… From a global observability perspective.
this future data flow engine will participate to the… to the… not only to the trace propagation, but also to the trace itself. So that's the… The second step, which is not represented into this document.
jmacdonald 00:52:34 All right, we've reached nearly the end of the hour, and I kept skipping over all of the issues that you filed, and as well, we… I know.
Laurent Querel 00:52:42 I think you can, you can open the 2465, that will be… Okay, thank you.
jmacdonald 00:52:48 Thank you.
Issue 2465 has an overview of what's been done.
Laurent Querel 00:52:52 And I want to put the.
jmacdonald 00:52:53 rest of this meeting for you to talk about it. So here we are.
Laurent Querel 00:52:58 So, this one tried to address entirely the… the issue 2431.
And prepare the… basically solution for, the four other, PRs.
Oh, not PR.
jmacdonald 00:53:15 Yeah, these are all the issues I skipped past.
Laurent Querel 00:53:17 Yes. So, what I did for the general idea is… We already split the pipeline control channel that we initially had, where all the pipeline control messages were going.
We already split it in two parts, the pipeline control channel and the completion control channel.
And then, and then we have on the… for every node, we have what we name the control, the control channel, the node control channel. So it's… it's something that is attached to each node.
So, and it's basically, an M… an MPSC or SPSC, channel, basically, something between the… the… the controller and the NUD.
So, what I did here is, a refinement of this control channel per node.
To be much more, optimized, in my opinion, and, where… We will provide a lot of guarantee to minimize or to remove contention, and to remove, also, to define perfectly the priorities between those messages, those control messages.
So instead of, for example, having a single buffer channel. For all the nut control messages.
there are some… we have different class of control messages. For example, the drain… drain ingress, or the shutdown are a different class of control message than, the… the timer, or the collect telemetry, or the… the, the ACT NAC, control messages.
So, that's basically what this long list of PR are doing. They are basically first creating, An optimized and well-defined control, channel.
where the properties, and the guarantees I just mentioned, differ… differentiation of, control message, plus, passes, a bunch of tests that make sure that those guarantees are addressed. So that was the 2466. I did it in a isolated way.
So it's not fully… it's not integrated into the engine, but the… this central channel, data structure is entirely defined in this PR.
Then, I was considering… for me, naming is important, because for the future maintainability of this project.
We need to be crystal clear on those, engine label, constructs.
So, instead of having this concept of message channel.
That is, after thinking a bit again about it, I think it's a little bit fuzzy in terms of, meaning, so I renamed that, inbox, because we have those nodes that are basically tasks And, like an ACTOR model, there is basically one inbox per task.
And… and those inbox… Manage the complication… the complexity of the machinery to process the P data and control message together.
So that's… that's… that's why I renamed that inbox.
And… and then, Reading the… how the values control message are used, there is one category of control message which was named delayed data.
And, it happened that we have 3, currently we have three, processors that are using delayed data.
The original one, retry processor, And we have the batch processor and the durable processor, which are also using the delayed data, but I will say Like a workaround.
They are using delayed data without P data.
So… What I decided is… Using this, refactoring of the… The control channel data structure.
To, basically split, this, delayed data in two parts, something that will give us a way to recue a pilot, polluter.
That's the need for the retry processor. And it could be done locally. By locally, I mean we don't need to involve the entire controller, and that will remove a lot of contention going this way.
So that… that means that we will have less message processing the entire system. That will stay with the… inside the… inside the inbox mechanism, basically.
So, so that's the reculator approach.
And for… The batch processor and the durable processor.
What they really need is a wake-up API.
So, a mechanism to set up a timer, cancel it when they want, and they do that many, many times. And again, that could be done locally, and so now it's a separated API.
And I think this WakeUp API has been merged yesterday, yes, I think yesterday night.
Not entirely sure, but definitely that's the… either the current or the one that has been merged yesterday.
jmacdonald 00:59:27 And I can say that I'm the one who added the really cheesy implementation of this delay mechanism, which was used in both places, and was not efficient in either place, so thank you.
Laurent Querel 00:59:39 Yeah, no, for them, I mean, it's… we… That would be the easiest thing I could have attempted.
Yeah, sorry?
jmacdonald 00:59:47 I was just saying that the use of that delayed data mechanism was a hack from the beginning. It never felt right, and I appreciate that you're fixing it right.
Laurent Querel 00:59:55 Yeah.
And So then, we… once we have these two, new, capability into the inbox, the wake-up and the reculator, that is basically the delayed data.
Then we can remove the global delayed data runtime that we had initially.
And then, we can integrate the control channel Finally, into the engine.
And then we have some, work to… in the UI, the admin UI, and the obsolability, some signal, new signal that will, be delivered by the… this new implementation of the control channel.
With the goal of… Providing… Matrix and event that will give us all the, The necessary… necessarily telemetry to observe a liveness problem.
Into the system.
So, at the end of this, seven, the last PR, We will get, that fully implemented, some additional metrics and events, with the goal of being able to observe, understress the system and see what is going well or not.
jmacdonald 01:01:21 Can I ask, I know we're really at the end of time here, I'm sort of asking the question Goken might be thinking, and I know his microphone is not working too well, but I've understood the prerequisites, you know, steps 1 through 4 and 5 are open right now, but it sounds to me like the meat of this is right here, which is what Goken was Issue is all about, as well.
Laurent Querel 01:01:42 Yeah, yeah, yeah.
jmacdonald 01:01:44 After we use the new control, we're going to sequence shutdown so that it's bulletproof, and it makes progress, and doesn't deadlock, and doesn't live up.
Laurent Querel 01:01:53 Yeah.
jmacdonald 01:01:54 So there's a lot… May your fussy sleep?
Laurent Querel 01:01:55 Pretty different from what Go can describe, but I think we… I basically started this work, probably at the same time Gokin created.
jmacdonald 01:02:07 Yeah.
Laurent Querel 01:02:07 document, I don't… I don't remember exactly, but…
jmacdonald 01:02:10 No problems there. No problem with duplicating this type of research.
Thank you. I think we've reached the end of the hour, and unless there's any last words, we should… we should, call it, and then see each other, next Tuesday, and on Slack, and, I'll be glad to take point on any of… any problems that we've slipped under the rug in the last hour.
Last words?
Thanks for that.
Gokhan Uslu 01:02:42 Will the message channel changes stuff?
jmacdonald 01:02:47 Thanks.
Go, Ken. I think.
Gokhan Uslu 01:02:49 Yeah, I was just saying thank you for the work that Lauren has been doing in those message channels.
jmacdonald 01:02:57 Yeah, alright.
Gokhan Uslu 01:02:58 shut down, or…
jmacdonald 01:03:00 Thank you all. I'll see you next time. Have a good day, everybody.
Laurent Querel 01:03:04 Where they are.
Saroj Kumar Patra 01:03:05 Thank you, bye.
Laurent Querel 01:03:07 Thank you, buddy.
