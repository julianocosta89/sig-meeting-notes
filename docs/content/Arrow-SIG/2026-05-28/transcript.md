SIG: Arrow SIG
Date: 2026-05-28
Duration: 109 minutes
============================================================

## Zoom Recording Transcript

Laurent Querel 00:02:27 Hello, Luen.
drewrelmas 00:02:30 Hello, good morning.
Or whatever time it is for everyone.
Laurent Querel 00:03:55 Okay, grofo is missing… I think I can start with, maybe some updates on what, happened last week during the Absarity Summit event.
We had two talks, one from, Joshua and Siju, Looking about, Among other things, among other things, talking about the, OTAP protocol.
We had multiple discussions following this talk, so that was great. And then we had also, Datadog, talking about, cost and efficiency, On three dimensions, protocol.
Or transport, storage, and query.
And, for the transport dimension, the dimension, the OTA protocol also.
So that's an interesting momentum for us.
So, is there… so, Jake, do you have anything else to add? You were present during this, this event?
Jake Dern 00:05:11 No, I think, yeah, that's a good, a good high-level summary, of the two talks.
Laurent Querel 00:05:19 Okay. Otherwise, on the pure observability, space, The important information that we capture that reinforced, What we are doing in this project.
It's clear that everyone working with AI workload observe, An important increase in term of, delivery volume.
different explanation behind that. The… for me, the most, Important ones, or, or, the one that, at least, Can be easily understood.
The fact that those systems are under the undeterministic the fact that, Obviously, the number of interactions is increasing. It's no longer human-based, but, agent-based.
The number of, systems in… integrated of… Inside a prompt or a query is also increasing.
So the… and also the need for audit, for, Security, for, privacy purposes, is also, increasing. So, it means that transporting, processing, telemetry stream is, More and more important and need to be improved.
Which make the… this project, I think very well aligned with those changes.
Okay, I think we can start with the classic triage.
And for that, I will share my screen.
Except if someone else wants to do that.
I will not be against, having someone, changing this role with me today. But if no one is okay, I can do it.
Okay, So, this is the document that we use to track the agenda, so please add any topic that you'd like to discuss, demo that you'd like to make.
As a reminder, we have a first part where we talk about the existing non-approved GitHub issues.
Also add your name there, if you can.
And then, I see that we have one, One topic from Drew, regarding the changelog process.
So please add additional ones, One or two additional ones will be nice.
So let's go to the issue, and Looks like we have been able to… So the, the… We just have to review this.
List for today, much smaller than the other weeks.
So, Pocket Exporter, how do we add retry configuration and flush else metric from LAIT?
Lily, do you want to… I mean, for me, it's, obviously interesting. Do you want to add some, additional information on this, on this one?
Literally.
Albert Lockett 00:09:05 while it's here, but… Yeah, okay.
Seems reasonable. Yeah.
Yeah, transient object store write failures, we should retry them. Yeah, sure, that's, seems totally reasonable to me.
Yes.
Laurent Querel 00:09:23 So, just maybe as a reminder for people that are not aware of this exporter, that's something that Albert created now multiple months ago.
And, it's… I think at this point, it's more like, It's not a production, really, exporter, but it's more like a proof of concept to demonstrate The storage of, telemetry signals who has it direct from, Hotel Arro to, to Parquet? Obviously, there are some, transformation in between, but it's much more direct that, than… an OTL fee-based… Batch to… to a parquette representation.
Okay, so, I will update the status, also when we'll update the status, I will not do it in real time, it's… too cumbersome. So the filter processor add-pass and kick count observability matrix, I think this one is just about improving the internal telemetry, so that's obviously good.
Exposing process, control plane handle from start to turn.
Not sure to follow this one.
And…
drewrelmas 00:10:58 Yeah, I don't have context on this either. It'd be, more ideal if Lalit were here to speak for it.
Laurent Querel 00:11:07 Oh, okay, okay, okay.
Yeah, I think that's… Yeah, I will, I will, definitively read this one with attention. I think I know what it is, but I'm not entirely sure. So I will, Just take a note of reviewing this one with more attention after this meeting.
Okay, hypertling governance, that's related to the user event receiver.
So that's, A receiver that has been recently integrated.
That's the counterpart of the ETW receiver.
the Windows, low-level, transparent mechanism.
So yes, it looks like, yeah.
Definitely, a nice, property to have, but… Tristan's routine.
It's good.
Engine, structured cross-node validation, relation, yeah, so this one is… So we… what we have in the… Maybe, Ukarche is there, I don't know.
Utkarsh Umesan Pillai 00:12:31 Yep.
Laurent Querel 00:12:32 Okay, do you want to, talk about this one?
Utkarsh Umesan Pillai 00:12:35 Yeah, so, I mean, like, while working on the ETW receiver, we came across this situation where Like, any given node can check the configuration for itself, but then… If there are multiple nodes of the same receiver or the same exporter, then, let's say.
two HTTP receivers. Two syslog receivers shouldn't be listening to the same endpoint, two different syslog nodes.
Likewise, ETW also has this session name thing, which should be unique for each node.
And the network-based receivers the problem for network-based receivers goes up another level, where, like, ideally, you wouldn't want to have an OTLP receiver and a syslog receiver.
Listening to the same endpoint.
So… That way, I think those kind of validations are better done at the engine level, where, like, a node can specify that this is something that has to be unique.
unique for my configuration, and yeah, and that should be… like, it's not easy to do it within the node.
So, I also, like, suggest that an approach may not be the best one, but yeah, like, just… This approach is essentially saying, like, we define this in… we define this enum. TCP endpoint and UDP endpoint are very standard things, so they can be a first-class variant within the enum, and then for other, like, file-based receivers, ETW receivers, you could have a… More general variant called that distinct field, where the node can specify, the uniqueness that it's looking for.
And, yeah, we… there's also some code about, integrating that in the engine.
Beautiful.
Laurent Querel 00:14:26 Yeah, that's, definitively a fundamental, Thing we need to address.
I don't think it's only related to… purely TCP, or UDP, infants.
you… you could imagine that for, the… the Linux user event, or… So, having the ability to… Define resources that need to be, unique.
your pipelines.
And unchecked at the pipeline level.
Yeah, yeah, definitively, we definitively need to… to think about… I will read that with attention, I don't know if it's, Yeah, I will give you my feedback directly on that, but definitively super interesting.
Utkarsh Umesan Pillai 00:15:15 Yeah, thank you.
Laurent Querel 00:15:21 Okay, hello, configuring a base URL pass, so ambient can be mounted under… yeah, so that's, Oh, it's already accepted, so that's nice.
I will just, go to the ones that are not yet accepted. Add benchmark indicators.
For situation behavioral.
I created this one. Oh, yes, so this one is related to… I don't know if people look at this, and I will let probably Jake also describe that in detail.
But, so this… GitHub issue is related to, A refinement related to this symbol that we have here, back pressure detected.
And, I'm just suggesting here to… Use some kind of color code.
to… To qualify the type of back pressure, because we have sometimes good back pressure, and sometimes… Something that is not necessarily back pressure, but a combination of back pressure and… And signal loss, and other… or lead delivery.
So, in those benchmarks, we will be able to detect that automatically.
And then, showing when something is… Could be considered as, a good behavior, or, a deficient, CSEN, and then the corresponding benchmark needs to be, just not considered as valid.
Oh, that means that the system is not in, in a working region.
Okay, I think there's…
Jake Dern 00:17:19 Definitely some, just, like, quick comment on it. Definitely, like, agree there's some, like, better, indicators that we can provide, particularly, like, around, I think you mentioned late delivery somewhere in here,
Laurent Querel 00:17:31 Yes.
Jake Dern 00:17:31 Sort of, like, latency that we're observing.
One thing that I was kind of, you know, not sure if this is, like, a place where we should, really be, like, trying to provide, any, like, testing or, like, guarantees, but there's also some, like, mention of… Showing when a configuration, like, does not provide an end-to-end, like, delivery confirmation property. So, like, basically, you know, like, stuff is saying it's delivered, but we're detecting data loss, or something like that.
you know, this is something that we, like, sort of do today by comparing, like, the sent and, like, receive counts, but I wasn't sure if there was something, more that we wanted to do here, because there was also, like, a mention of saying, well, if we detect that data is ACT before, like, our backend receives it, for example.
And so, like, while we can kind of, you know, make sure that, like, the received counts on the backend and the sent counts on, like, the load generator are matching, it's kind of like a… definitely like a step up to say, like, oh, we're going to detect when the engine acts something before our backend got it.
Laurent Querel 00:18:32 Yep.
I agree.
Jake Dern 00:18:36 So maybe that's, something that's.
Laurent Querel 00:18:38 So, do you, do you want also to present, maybe, in detail, the last present?
Not now, but at some point during this meeting? Or is… do you think it's too early, and… You can do that, you know.
Jake Dern 00:18:52 No, we definitely can. I think the… the results, the data that we published this morning, it's… it is very interesting. So, yeah, if we have time.
Laurent Querel 00:19:00 Yeah, that would be great. Excellent.
Okay, with this.
Stu, no, sorry.
Kubernetes attribute processor, so this one is nice.
Looks like, okay… So, I think for this one, I don't know if Joshua is with us today.
Looks like he's not.
But, So for me, it's like a placeholder. We definitely need to… that's a very interesting processor to implement, but we need for, like we did for the us matrix, for the file log receiver.
I think John F.D. also has been, defined this way, we definitely need to create a more, a specification, a complex specification. I think that's what also, Joshua is adding here. We have a set of guidelines, to… design new components, especially in the context where they already exist, either in the Go Collector or in some other telemetry data plane.
So, I see this entry as a placeholder, we just need now to go to the next step, which is the full detailed specification.
And learning from the existing solutions.
a benchmark indicator… sorry.
I have some issue with my screen.
Okay.
Really spot-up data flow engineer binary in GitHub, Yeah, that's something… That looks abuse right now.
drewrelmas 00:20:51 I'm not sure if it happened to everyone else, but your screen went just black, Laura. I don't know if you could try resharing.
Laurent Querel 00:20:57 Yeah, I have an issue with my, With my herb, multiple scream on it, and sometimes it's just, not behaving well, so let me share again my screen. I think that will fix the problem.
British.
The use of this clean?
drewrelmas 00:21:26 This is back.
Laurent Querel 00:21:27 Okay.
Yeah, so maybe, Drew, do you have something to add to this, GitHub issue?
drewrelmas 00:21:34 Yeah, I mean, I can talk about it briefly, it's slightly related to my changelog topic, but this was something that Josh raised to me. I know for a while we've talked about various methods of starting to release some of our Rust code, be it through publishing crates, or, this is another approach that Josh came to me about, and it spurred me to take, like.
actually move forward with some of the Rust changelog tracking, which is my next topic, because as soon as we release something, we have to talk about versioning of that release, and without a changelog, we can't really have versioning. Yeah.
So, I'm in support of this. I, you know, Josh isn't here to talk more about his exact reasons for wanting it, but, I think anyway it's… Causing good… A good direction in the repo overall.
Laurent Querel 00:22:34 Great.
So you created also this one.
Yep, duration metrics.
drewrelmas 00:22:43 Yep, I had an offline conversation with Aaron about this already, but in summary.
There's a couple of additional, metrics that I want to pull into… er, I want to expose from Quiver and the durable buffer processor. First, we have storage bytes used and storage bytes cap. Oh, no, your screen went black.
Laurent Querel 00:23:05 Yeah, so yeah.
drewrelmas 00:23:06 I can share mine.
Laurent Querel 00:23:08 Yeah.
drewrelmas 00:23:08 I'll be taking over anyway, in a moment.
Yes.
Laurent Querel 00:23:13 Feel free to do it.
drewrelmas 00:23:15 One second… Share this… Can you let me know if that's, working well?
Laurent Querel 00:23:26 Yes, it's working with.
drewrelmas 00:23:28 Okay.
Here we go.
So, we have storage bytes used, storage bytes cap. One thing that I wanted to get out instead is storage utilization, meaning a division of used over cap.
This is similar to… I mean, not… it's not dissimilar to what we have for CPU utilization. We emit a value between 0 and 1, and downstream systems can, if they need to, for example, multiply by 100 to get a percentage.
But, you know, I… for one of my use cases, it's convenient for me to have a metric for the utilization percentage.
right out of the gate, instead of needing to do this division myself later. The other thing that I think is relevant to talk about is There's two ways of… or there's two metrics That durable buffer processor uses to talk about, dropping items, either when Something like a storage cap is violated, or when the expiration time expires.
And it only emits metrics for, with the unit of items, whereas a lot of other metrics in the processor, emit per-signal metrics, meaning with underscore log records, underscore spans, underscore, metric data points.
So, that's, the other thing I want to do is, for my use case, I need per-signal variations of these metrics. So, I think I've talked offline with Aaron, and he's fully supportive of adding these, no huge issues.
Laurent Querel 00:25:18 Just one comment, I think the… we are trying to apply the same, naming convention parametric set.
drewrelmas 00:25:28 I think.
Laurent Querel 00:25:29 I think there is a slight, divergence there.
the Utah.
drewrelmas 00:25:33 Are you talking about this thing?
Laurent Querel 00:25:34 Yes, yes. The OTAP prefix there, I think, is not following the naming convention that we, Okay. We decided to follow up.
drewrelmas 00:25:42 So, yeah, and I know.
Laurent Querel 00:25:44 Just double-check, but if I remember correctly, it's… doesProcessor.durable buffer.
drewrelmas 00:25:50 Sure, I will confirm that as well.
Laurent Querel 00:25:55 And I know that Siegel, is, also working, actively on integrating Weaver with the project, which is super cool.
And, and we will be able, progressively, also, to create legal policies?
To… to basically express the… this kind of naming convention that we have for this project.
They will be automatically detected at some point.
drewrelmas 00:26:26 Okay.
sounds good, so I…
Laurent Querel 00:26:31 Okay. So, maybe we can switch to the, the main topic… Sure. So we have you with the… getting the changelog around.
Regarding the issue, triage process, CGO, safe observability, and JEC, the benchmark.
So, we have a lot to cover, Let's try to do it, so… Please, yeah.
drewrelmas 00:26:58 I…
Laurent Querel 00:26:58 the…
drewrelmas 00:26:59 That's at least.
Laurent Querel 00:27:00 Whoa.
drewrelmas 00:27:00 We'll probably be quite short.
Laurent Querel 00:27:02 Okay, perfect.
drewrelmas 00:27:04 So I mainly wanted to do just an informational thing for everyone on the call.
For a number of reasons, and honestly, we've had an issue open for this for a long time, since last November.
about, doing a proper changelog process with all the Rust development work. As everyone knows, we have quite a high PR velocity, so it's getting harder to track what all has gone in.
And in addition, with Josh's, new issue talking about releasing, an engine binary. I think it's time to finally make the push on this. My proposal, which I've, put into this pull request so far is adopting almost exactly the process from collector and collector contribib, if people are familiar with that. It uses something called CHLoggen, which… instead of every contributor having constant merge conflicts over a single changelog file, essentially, every time you make a change, you leave a little YAML stub in a certain directory, and then at release time, we have automation that will concatenate them all together, and place it in the changelog Markdown file. So… I encourage everyone on the call, if you're interested, to read through and see what's going to happen. There will be a new workflow running at CI time that tries to enforce this. It's not marked as required for the moment, while we just test it out and see if there's any problems.
But the expectation will be every pull request should have a, changelog entry added, except for, ones marked with CHOR. So if there's CHOR in the title.
it will not need this, as well as, you know, the standard dependency upgrades from Renovate or Dependabot, those will also be exempted.
CJ, you have your hand up, you want to say something?
Cijo Thomas (Microsoft) 00:29:13 It's more like a question like the, is the biggest motivation behind the tooling to avoid merge conflicts?
drewrelmas 00:29:22 Yes, I think so. You know.
especially at the volume of contribution that Collector and Collector Contribute have, I'm not surprised that they opted for this sort of route.
I know in OTEL, I think you're probably speaking from your experience in the OTEL Rust SDK, which, had a manual markdown, or a manual changelog file, if I recall correctly.
Cijo Thomas (Microsoft) 00:29:45 Collector, yeah, except collector, like, everywhere, including the specification, we just use the manual update.
and deal with conflicts when it occurs. I'm not opposed to this one. The only thing which I left as a comment also in the PR is, it looks like a lot of Oh… Things for a newcomer, or someone who's not familiar, just to make a simple contribution.
They have so many things to grasp, to generate just some… something very simple as, say, changelog. So that extra overhead is something which was not very, fun for me when I contributed to Collector and other reports in the past, because all I did… all I needed was just a simple change and one-line entry to the changelog, but… the amount of… effort I had to do that was, non-trivial.
So that's something which we'd… I'd like us to consider, like, if… We really want the… contributing guide to be talking about all these things, like use, make a man, and, use the…
drewrelmas 00:30:47 Yeah, I have relaxed that language a little bit, like, for context for people. What I would expect a new contributor to need to do is… there's this template file, I would expect them to copy and paste it, rename it, and fill it in. But, so, like, the make stuff isn't actually necessary. Oh, okay.
Cijo Thomas (Microsoft) 00:31:08 You already changed something. Okay, got it.
drewrelmas 00:31:09 Yes, I did.
Laurent Querel 00:31:11 Nope.
Cijo Thomas (Microsoft) 00:31:12 It's not a bad thing at all, I was just generally saying, like, for a simple contribution which requires changelog, the amount of thing which the contributor has to first read through.
and make it happen was somewhat non-trivial, so that's why I wanted to see if we can make it easier, but it looks like you already removed the make script requirements. Okay.
drewrelmas 00:31:33 Yeah.
Laurent Querel 00:31:34 Can we just, maybe, draw also… maybe it's already there, I didn't read in detail the corresponding PR, but can we make sure that we have… when this system fails in CI, this check would pull fail. Can we add… Documentation or link, that will definitely help Fix…
drewrelmas 00:31:58 Oh, God.
Laurent Querel 00:31:58 And I'm.
drewrelmas 00:32:00 That's a good idea. Yeah, I can… I'll take a look at that and make sure it points.
Laurent Querel 00:32:04 Yeah, and also, maybe, in this new era, based on the Agents and so on, can we make sure that We have either in Contraven D, or… In the adjunct ND Something that explains what to do when someone wants to create In order to make this thing crazy automatic.
drewrelmas 00:32:29 Sure, yeah. You're saying, so, any, you know, AI contribution will do the same?
Laurent Querel 00:32:35 I mean, not only AI contribution, I mean, people are using a mix between AI and what they are doing themselves.
But when the, when they create, when they push a new PR, That could be nice, to have instructions for an agent to finalize this PR, so creating this style.
Feeding the… the values field with, the component description, and the note, and so on. That would be relatively easy to automate for an agent once the code source is there, or whatever has been pushed.
drewrelmas 00:33:16 Yeah, yeah, that makes sense to me. I do want to get to the end to allow others to have time. The last point I wanted to list is I've chosen to isolate the changelogs for our Go… our, kind of legacy… not legacy, but, steady-state Go components compared to the rapid development we're having in OTAP Dataflow. So there's two separate, changelog files for these.
Okay.
Laurent Querel 00:33:46 Great.
drewrelmas 00:33:47 I think.
Laurent Querel 00:33:48 we know…
drewrelmas 00:33:48 In the world, we're not doing anything besides continual, dependency upgrades.
Laurent Querel 00:33:55 Yeah.
Excellent. Okay, so let's move to the, other topic.
Ahole?
Aaron Marten 00:34:08 Hey, I'm gonna go ahead and share my screen here.
So I have this as a draft PR right now. I didn't quite get it completely ready to go here before the SIG meeting. But this is the thrust of it. So I… I was recently added to the triageers list. I am… We'd like to propose that we have a more formal triage policy, and the main motivation behind this is to just timebox and reduce the amount of time spent In the SIG meeting, on triage, so that you handle more of it async.
So the main change, is essentially just moving from right now, where we just have triage deciding and accepted, to this basic state diagram, Where, you know, offline, the triagers are going to be expected to go from deciding to either needs discussion, if we want to escalate it to the SIG meeting.
If it's a more, you know, substantial issue, or just go straight to accepted, in which case we'll just skip the, skip the triage discussion. And then also there's another state which just needs info, where, you know, we're blocked on it, maybe mention the person that opened the issue.
And see if they can provide some additional information or context.
The document, which you'll see when I publish it, I'll go into a little bit more detail, but this is the… The main, main part of it.
Laurent Querel 00:35:36 makes totally sense for me. That would be great to have a little bit, A better triage station, definitely be a good idea.
Aaron Marten 00:35:46 Okay, so, yeah, for now, I guess it's, if anybody has additional comments, we can discuss now, otherwise, Keep an eye out for the PR.
Laurent Querel 00:35:55 Okay.
Rates.
drewrelmas 00:35:58 Laurent, I want to interject very shortly, if we've reached the end of this topic, but I think if there's conversation in the chat. We actually skipped a few issues.
Laurent Querel 00:36:09 Oh, okay.
Okay.
drewrelmas 00:36:15 So I don't know how you want to handle this, but I felt bad. I told someone we'd talk about them and then forgot.
Laurent Querel 00:36:20 Sure, sure. So which one we skipped?
drewrelmas 00:36:24 In particular, 3068, I think. But also, I don't know if we opened…
Laurent Querel 00:36:29 66.
drewrelmas 00:36:30 in 67.
Laurent Querel 00:36:37 I don't share my screen. Can you share your screen, maybe?
drewrelmas 00:36:40 Sure.
Aaron, I truly hope I didn't cut you off, but it sounded like we were reaching the end of that talk.
Aaron Marten 00:36:49 Boom. I'm all good. Yeah, we can follow up on the, issue stuff in the PR.
drewrelmas 00:36:54 Oh, one second, I'm in my fork.
This one.
So Samir, I don't know if you'd like to say any words, but this was your issue.
Sameer J 00:37:18 Yeah, like, a couple of months back, there was a change done related to exposing DFEngine as a library, so that the host could get access to, Engine in Proc.
And so, as part of that, already there was the observed state handle exposed to the hosting process. What this issue is about, to also expose the telemetry registry handle so that access to internal metrics is available to the host.
And why this is necessary is as, like, in the observability pipelines that we will be hosting this library, there are things that we want to light up about the… about the engine.
Laurent Querel 00:38:03 Yo.
Makes sense, and so I need to read that in detail, but what is, very quickly, what is the mechanism used to communicate between these, Our, engine and this, post-system.
So, exactly.
So you have this observed state under that you want to make you want to explode, right? Correct. And then get… okay.
Okay, okay, I think that makes sense to do that this way.
I just need to think about it a little bit more, because we, as you maybe know, we… We all, refactoring a little bit the internal telemetry system.
It's a slow process right now, but that's still a goal.
And, the ultimate objective for us is to have, like, We like to reuse, basically, the telemetry the pipeline engine that we use to process external telemetry. We want to reuse the same engine for internal telemetry, so that means that people will be able to use all the processors, all the exporters.
Even for internal telemetry. And in this situation.
We could also imagine that, things like, deriving Liveness and readiness.
From the internal event and metrics.
Could be also achieved this way, so maybe the… these, So that's why I need to think about it a little bit more. Is sharing this under compatible with this ultimate goal or not?
Sameer J 00:39:54 I see.
Okay.
Laurent Querel 00:39:58 But anyway, I think it's, fundamentally important. It is well aligned with, With the goal of this project being a system that could be embedded into a bigger system, we also have the exact same need for F5.
Sameer J 00:40:18 Sounds good, thanks.
Laurent Querel 00:40:19 Okay, so we have, 20 minutes, and we have two topics, so let's cut that in two, and, so CJ?
Can you.
Cijo Thomas (Microsoft) 00:40:31 Yeah, I won't be able to share my screen, so if anyone can share, that would be helpful. I'll take more.
Laurent Querel 00:40:36 We are both in the same group, so…
Cijo Thomas (Microsoft) 00:40:40 Maybe, like, you can help, Sherry.
Laurent Querel 00:40:42 So, what about Jake? Because Jake will talk after that, so…
Cijo Thomas (Microsoft) 00:40:45 Oh, yeah. Preview.
Laurent Querel 00:40:47 resolution.
Jake Dern 00:40:48 Do you have a… there's a link in the document, I take it.
Cijo Thomas (Microsoft) 00:40:52 Yeah, so once you share your screen, they'll put one entry to the agenda towards the end.
Jake Dern 00:40:59 Yep, yep.
Cijo Thomas (Microsoft) 00:41:04 So while you open that, I'll just briefly try to explain what I'm trying to do. So this is all about improving the self-observability story for the Dataflow engine itself.
It's part of something which I'm doing across Open Elementary, including other SDKs.
So the main goal is to start with a schema in mind, like, you define upfront what telemetries you want to emit, metrics logs. We actually use events, not logs. And then use official tooling, which in our case is Weaver, to generate the code From the schema.
And then use that in the actual engine, the generated code to emit metrics and logs. And lastly, integrate that in our CI, so that we actually use Weaver itself to validate we produce all the telemetry we claim to be producing in the exact same format, all the attributes and things. So, it's a big effort, and we don't even have all the capability in the tooling. Like, Weaver itself does not have the ability to generate today. So what this PR, which is a very basic attempt, Joby.
Step one towards that direction is using… a YAML to define the event. So this is starting with events, not metrics, so I have a YAML which describes the event.
And we produce events by hand, like, we don't have the code generator from Weaver yet, so we'll produce events by hand.
And then there is a CI check, which starts the engine and uses Weaver to verify that you are producing the events which you are defining in your schema.
And if there is any variation or any violation, it'll fail the CA, saying that, hey, you're supposed to produce these many events with these many attributes, but you did not produce it, and it'll fail your peer. So that's the idea. So this one is a very basic MVP.
defines 3 events. So, if you go to the simcon groups directory, it has 3 events being defined. So the… yep, yep, those 3. So, event.
the event name.yaml. So there are 3 events defined here, and the name of the event is the only thing which we are currently validating. That matches what we emit from the hotel info, hotel trace, or hotel warning macros, which we are using throughout the codebase.
So the goal is, like, eventually we'll have everything, generated by Beaver, and validated also by Beaver. So this is, like, step one, and there are a lot of, things to be done before, we're done. So my ask is just to take a look at this initial MVP, see if this is directionally, acceptable.
And if any feedback, I'd be glad to take that. You would see a lot of boilerplate code in the workflow, the GitHub workflow. That is something which I expect to trim down eventually, by improving Weaver itself, so I have some work in the Weaver upstream. So Weaver itself can do a lot of the, common things, so we don't have to script it here.
Anyway, again, I started with events, but eventually we expanded to old signals, but it will be a long journey.
Lauren, go ahead.
Laurent Querel 00:44:14 Yeah, so that's a fantastic initiative. I have three… Three feedback. So the first is about metrics. I think for metrics, that will be super easy.
We already have, I think it's schema… schema matrix endpoint.
That automatically generate a semantic convention, like… File.
Based on whatever nodes are present in the configuration.
So we… so we could… so it's not ideal, because obviously, depending on the pipeline configuration, you get a different answer.
But, I think you can reuse the code that is there.
Press the… The component discovery, Mechanism that we already have in this project.
To basically generate a first, version of the matrix description that could take the form of those semantic convention files per matrix. So that's one thing.
We don't have that, unfortunately, for events, so like you said, that will be a long process, but that's something that we, yeah, so, okay, matrix. Then the second thing is… the policy capability that Weaver is offering.
So, like you said, in the CI, we will have Weaver to live check the, The instrumentation that we… and the telemetry that… Any integration tests or tests in general, generate.
Against these, referential, the semantic convention, or the custom semantic convention registry that we will maintain for this project.
But the Weaver is also coming with some extensions.
And… customization, I should say. And this customization Can be expressed in this, language… language name rego, which is something that we, reuse from OPAD, the Open Policy Agent.
So you can express policies that will validate additional custom things on top of the… what we observe from the… The… the instrumented application.
So, for example, if we want to detect that something like, for example, your two first events here, OTLP, Exporter, gRPC, receive.
And the other one, the event OTLP exporter, HTTP exporter, if we decide that things like prefix, OTAP, OTLP, or… Slightly redundant, I'm not sure of that, in this specific case, but we could imagine that we have a search rule that we can have to revert to detect that automatically.
And, the… the ultimate vision… That is partially described in the… slash docs slash telemetry, I think.
Is… once we have this, This custom registry, describing all the instrumentation, That is checked.
Following the… the rules that the CMOT Convention Group defined, and so on.
Then we can start to codegen, to generate code.
For, that will be basically reproducing what we have with the matrix set, for example, which is currently based on A set of macros.
that will generate… the… the client SDK, or the optimized client SDK, to minimize the… the overhead of capturing multiple metrics at the same time. In fact, all this thought could be, at the end of the day, generated… could serve as a way to generate a type safe.
client SDK. And I think that will come in a… future step, but for me, that's the ultimate goal. Being able to create a self-exploratory, type-safe client SDK, leveraging all the optimization that we, we implemented already in this project.
Cijo Thomas (Microsoft) 00:48:55 Yeah, yeah, so one observation there is, like, for metrics, we kind of created our own macros to generate that, but our long-time goal is we expect Beaver itself to do that for us from the schema.
Laurent Querel 00:49:07 Yeah, yeah.
Okay, any other direction before we move to.
Cijo Thomas (Microsoft) 00:49:14 Yeah, I don't have anything else, so, Jake, all yours.
Jake Dern 00:49:21 Cool. Yeah, so we have, recently we added a whole bunch more, benchmark results, to the dashboard, and a couple, like, particularly interesting ones, I think, in the last day or so, so I'll show two.
Both of these are doing, like, a log attribute rename operation, and using either the transform or the attribute processors for both, the data flow engine, or the OpenTelemetry collector.
And so the first one that we have is, like, varying the rate.
And we can see, like, a couple interesting things on this graph, just because we're also plotting the baselines on it, and it kind of shows a few interesting properties, so… If we start out by looking at, the data flow engine results, so that would be… let's just look at, like, 400K here. So if you look at the 3 on the left, this is for the data flow engine, we have the baseline, which is not doing any work, which is the orange.
We've got the attribute processor, which is kind of like the specialized processor, for just doing attribute operations over on the left, that's this one. And then the transform processor, which is, like running an OPL program to do the same thing.
And there is, like, a little gap between the attribute processor and the transform processor. Albert, you can correct me if I'm wrong, but I think this is just a case where we're not skipping decoding transport-optimized IDs, and I think there's actually an issue that was filed that I noticed before I even pinged you about this. So I think this gap is expected to completely disappear.
But kind of the more interesting thing here, in my mind, is if you look at the, the gap between just the baseline measurement, so the orange.
And then, like, the attribute processor on the left, like, it's basically nothing, at every single rate, so I think this is just kind of demonstrating, like… You know, the sufficiency that we see, in terms of, you know, we don't really pay, like, an additional cost to operate on the data in terms of OTAP.
Beyond just, you know, what it takes to, To get that data into memory, so, that's kind of a good… Good result there, So, and we're looking at just the data flow engine on this chart, so if we compare this to the OTLP results for the data flow engine, you can see we actually performed, like, really well in a pass-through scenario, but we do choose when we actually have to materialize the data and operate on it to transcode it into OTAP.
So you see we'll pay, like, a pretty big cost, you know, bumping from, like, this 15% CPU utilization all the way up to 46% or 48, in order to actually do the operation on the data.
And then what we'll see in, like, the next graph is, like, once we do that, you know, we… basically the price has been paid, and then we can reap the same benefits, that we do with OTAP in terms of doing transformations, so… I'll just kind of, like, pause there in case, anybody has, like, comments or questions.
Alright, so let's look at this graph. This one is also very interesting. So what this one is doing is, like, also doing log attribute renames, but we're doing multiple of them, so either 1, 2, 3, or 4. So these are log record batches that have 12 attributes each, and we're renaming 1, 2, 3, or 4 of those attributes. And we're doing this again across the data flow engine, the OpenTelemetry Collector. So if we look at the results for, Just starting with, like, the data flow engine, and for OTAP in particular. So you see that same, like, kind of bump that we saw before between, you know, the attribute and transform processors? It's not really super important here. What is important is, like, as you go across and you go from 1 to… three, four renames, you can see that basically the results are completely within noise. Like, in some cases, like, I think, for two, you can see that, like, we actually, like, you know, kind of slightly went down. I mean, this is definitely just, like, noise in the measurement, but you can see that basically the marginal cost for, like, doing more than one rename is effectively zero.
if we look at, we can see this, I think, kind of, like, nicer if we look at OTLP as well for the data flow engine, so you can see, like.
Yeah, there's a big gap here, between, you know, OTAP and OTLP for the data flow engine, but once the price is paid, you know, again, you can see that, like, for 1, 2, 3, or 4 renames, because we're converting to, to OTAP internally.
It's again, like, effectively free, and all the measurements are within, you know, error, basically, of each other, just noise on the machine, which is pretty cool.
We have a couple results for, the OpenTelemetry Collector, then on the right, so this is, OTLP results for the OpenTelemetry Collector.
And you can see for, like, 1, 2, 3, or 4 renames, we're actually paying, like, a pretty consistent fixed amount of cost, you know, whether we're using the attribute or transform processors, for the OpenTelemetry collector, so we're… we're paying roughly, you know, looking at the chart, like, 5% CPU For the single core, per rename, going from, like, 77 to 82 to 87 to 92. It's, like, pretty consistent.
And similar thing for, the attribute processor, although slightly less, like 3.5% to 4% each. And then the last bar on the chart here that I plotted was just, the OpenTelemetry collector, using, OTAP, which is, in general, like, not… an amazing, you know, thing to be measuring, just because there is, like, a huge conversion cost, you know, for us to convert from the OTAP representation to the internal.
you know, P data representation of the OpenTelemetry collector, but, you know, this is just, like, kind of showing that, like.
it is, you know, to get these benefits of OTAP right, you know, you kind of need to be using the OTAP representation internally, like, you can't just be, you know, receiving it translating it into some other representation, and then still getting those benefits. So, that's why I plotted this one on here, just to kind of, you know, make that point. You really need this, like, end-to-end arrow, pipeline in order to, to kind of see these benefits, so… Yeah, I think those are… those are the results that we have. So, I think for folks that are familiar with the Dataflow engine and the OpenTelemetry Collector, this is probably not surprising.
You know, hopefully for those that are less familiar, these are, like, pretty illustrative, I think, examples of, you know, what we're… what we're trying to do, in Hotel Arrow, so…
Laurent Querel 00:55:35 Yeah, I think that's the best demonstration of why we created this project in Portugal. That's basically exemplified, The rational and, the expected result, The fact that we have a… we changed the internal representation of batches, From, hierarchical, object-oriented.
Representation, to a columnar representation, where Data processing will be able to leverage, a better memory layout, data locality, CMD instruction set, and so on. That's what we see here. We see that processing these things is so much faster than Exploring and traversing this, A huge amount of, Small memory object, that are not necessarily, In the same location, where you can… you can't leverage, properly the… the cache line and so on.
And that's why we see, every time these things are increasing.
And more we will have complex pipeline with more and more data processing, bigger will be the difference between these two… two types of NG.
That's, really, really cool.
To see now, just, exposed as a set of charts.
Jake Dern 00:57:01 Yeah, it's definitely nice to see, like, your, your hypotheses, like, you know, borne out in the data. I think this shows it pretty clearly. I'm definitely happy with these.
Laurent Querel 00:57:12 Yeah, yeah.
Excellent. Any other reaction to that?
drewrelmas 00:57:25 I just… I would just say that the one that's most illustrative for me is, sending OTAP into OpenTelemetry Collector, because I know We also own the code that's being used there, because it's in our repo, so it's just funny to see. I know we don't have active development happening on the Go world, but I wonder if there's ways we could even improve that, although I know it's not the highest priority.
Laurent Querel 00:57:53 So… Not because I don't want to change things, but I think that's illustrating the reason why we created, this new, Arrow Dataflow engine.
the, you can't improve the Go implementation without changing the internal of the pipeline engine inside the Go collector.
Because… you can't magically remove this conversion cost or tap to the internal representation we see, which is a OTLP-based representation.
So you will always have to pay that. And, so you have something OTAP, so web data or well-aligned, then you convert that internally into the GoCollector.
In this, hierarchical, EV in terms of object allocation representation.
And then you apply transformation on that, and every processor as part of the GoCollector ecosystem expects this type of representation.
So, that's why we had to change the entire system to get the full benefits end-to-end.
So there is no way to reduce significantly this green bar here in the chart, in my opinion.
drewrelmas 00:59:15 Yeah, and I agree. I'm not… I wasn't advocating for, oh, let's go improve that. I just… I just found it funny that it's, no, I think it's a very, very good.
Laurent Querel 00:59:26 Yeah, the best and the worst are in the same repo.
drewrelmas 00:59:29 Yeah.
Jake Dern 00:59:31 Yeah, and this is pretty consistent, like, you know, in terms of, like, if you're looking just purely at, at CPU, like, yeah, obviously, like, OTAP, in the OpenTelemetry collector is always gonna do the worst, because, you know, we're paying this additional, like, producer-consumer decoding, cost, like, in addition to sort of, like, the baseline, You know, costs of everything else, so… Yeah, we see this pretty consistently, yeah.
Laurent Querel 00:59:53 Can we, Jake, I think it… I think, Drew, make a point there. Maybe we can fix that in some way.
Can we add, a short, text?
Under, some specific chart, like this one.
Where we explain, we have a chance to explain, the charts. So, in that case, we could focus on, we are aware of this, inefficiency for the, OTC, OTAP, scenario, and… and we explain exactly what I explained before. We explained that, that's the main reason why we… we put so much effort into the, our raw data flow engine.
then people will look at that, and that will, I think, will be super nice.
Jake Dern 01:00:52 Yeah, absolutely. Yeah, I've got a branch where I'm working on something related to this. I was kind of playing around with how exactly to present the information, and… Also to, like, reduce any, like, duplication. I think, like, for some of these charts, there are, like, a lot of, details that are helpful to have, like, on the page that are common across everything, and then there's additional details that are sort of, like, chart-specific about how, things are designed.
And then I think there are also, like, you know, kind of, like, chart-specific, like.
things that we want to point out, sort of in terms of, like, interpretation, like you mentioned. And I'm trying to, yeah, basically model that somewhere in the manifest that we have that generates the site, and yeah, not have to, like, basically have, like, copy-pasted blobs of text for all of these, comparisons, yeah.
Laurent Querel 01:01:44 Great, yeah, excellent. Cool.
Okay, 9 AM, so end of the meeting. Thank you so much, guys.
Great session, and I think I will update the… The status for the values, so…
drewrelmas 01:02:02 I agree.
Laurent Querel 01:02:03 I already did. Perfect. Thank you so much, Lou. And next time, we will follow what Aaron was, Or describe.
drewrelmas 01:02:12 Yeah, I think I was looking at Aaron's thing as well, I think, it'll help us save a lot of SIG time, so I'm very sorry.
Laurent Querel 01:02:18 Yeah.
And if someone in this group wants to undo the first start of this meeting, that would be great for me. Not necessarily the best for this kind of thing.
Or at least we can alternate, that will be, also, very good.
Okay, thank you so much, and, have a good day.
drewrelmas 01:02:41 Yeah, the buyer.
Sameer J 01:02:43 Thank you.
