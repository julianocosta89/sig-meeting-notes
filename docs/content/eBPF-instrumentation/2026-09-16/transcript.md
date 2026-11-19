SIG: eBPF Instrumentation
Date: 2026-09-16
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Tyler Yahn (Splunk)** 00:09 Hey, Mario.
**Mario Macias** 00:22 Hello? Sorry, I had the microphone disconnected. I was talking to you.
**Tyler Yahn (Splunk)** 00:29 Oh.
Yeah, how's it going?
**Mario Macias** 00:34 Pretty good, pretty good, yeah.
**Tyler Yahn (Splunk)** 00:36 Nice, yeah.
**Mario Macias** 00:37 It's rainy here, but after very warm days.
Now, some… some fresh air is… Is very welcomed.
**Tyler Yahn (Splunk)** 00:49 Yeah, oh yeah.
Where are you based out again? Are you Barcelona?
**Mario Macias** 00:54 Near Barcelona, not in Barcelona City, in a small city.
**Tyler Yahn (Splunk)** 00:59 Oh, okay.
**Mario Macias** 00:59 there's… Hmm.
**Tyler Yahn (Splunk)** 01:01 Yeah, yeah, yeah, yeah. Yeah, I was talking to, Diana, I can't remember Diana's last name yesterday, but she's from.
**Mario Macias** 01:08 So they are.
**Tyler Yahn (Splunk)** 01:09 Yeah, yeah, yeah, yeah. She's from Valencia,
**Mario Macias** 01:13 Yes.
**Tyler Yahn (Splunk)** 01:13 Like, yeah.
I think, in school, you have to take, like, a second language here in the US, and, like, I always took Spanish, and, like, they always talked about Spain, and I've always wanted to go, but I've never actually been, like… But not, like, Mexico a bunch of times, but it's like, yeah, I've always wanted to see some of the, you know, the sights there, so, yeah, it'd be cool.
**Mario Macias** 01:32 I think KubeCon next year, too, KubeCon Europe, I think it's in Barcelona, so it's a good opportunity to come.
**Tyler Yahn (Splunk)** 01:40 Yeah,
**Mario Macias** 01:41 It's like.
**Tyler Yahn (Splunk)** 01:42 I've never wanted to go to a KubeCon more. It's also, like, Barcelona in… in March. Like, it's, like, the perfect time to come. Like, I'm just…
**Mario Macias** 01:48 Yes, I think it's the perfect time, yeah. It's nice weather, but not too warm.
**Tyler Yahn (Splunk)** 01:57 Right, yeah, exactly, exactly. So, yeah, I'm hoping… hoping I get a talk accepted or something, and I'm able to go. I'd be really excited to go.
Yeah, I'm sure for you, it'd be great, because it's in your backyard.
**Mario Macias** 02:09 Yeah. Yeah.
**Tyler Yahn (Splunk)** 02:11 I don't know why you wouldn't Right? Yeah.
**Mario Macias** 02:14 Yeah, I'll do… I'll do my best. Probably I will just go, even if I don't get any talk accepted.
**Tyler Yahn (Splunk)** 02:21 Yeah, absolutely, yeah, now that makes sense.
Hey, everyone else Looks like people are joining. We might actually have quorum at this point. We're coming up on 3 minutes in. So, welcome, everyone. If you have, agenda items, go ahead and add them to the agenda.
If you… Haven't yet, please also go ahead and add your name to the attendees list, and I will, start sharing my screen, and we can jump in here.
Awesome.
Okay, cool. Alright, Mara, you wanted to start us off by stop using, the OB test image package and, build these before the test?
**Mario Macias** 03:15 Yes, I… I think that, we are… those images are built on the month, manually.
the issue I see is that we… they are used for testing, they get the… the dependencies with Renovate, they… they get updated, but if… if they get broken.
Nobody will notice if… because the dependencies get updated, but no tests run, those images are not used in… in any test until you manually update them. So… Yeah, I don't know what should we do, whether we should integrate it better, so every time a dependency is updated, run tests, and so on, or just, stop using them.
And in the integration tests, just build them, build them manually, as we did before, at the very beginning. Build them manually, and use them. The… so, if any dependency gets updated, we would… immediately realize whether something has broken or not. The issue is that it might slow down integration tests, because building the image is always slower than downloading it.
But I don't know if the same… the same way we have a task for, building all the VPF, for compiling all the VPF code and sharing it with the tests, probably we… we can do something similar, like having a initial task that compiles the images, and then runs the test, shares it with the tests. I don't know how easy it will be with Docker.
I don't know, what do you think? If you think it's fine, just keep as we are now, and fix things as long as we realize it, I'm also okay.
**Tyler Yahn (Splunk)** 05:27 No, I think that… that's probably not great. Yeah, your point about, like, the, you know, updating, renovate and not actually testing whether it works or not is not… not ideal. So we should probably fix that.
I definitely am interested to hear what Steven thinks about, like, just switching back to just building these, every time we run CI. I don't know, like, I'm thinking, Steven, you might have been the one who moved away from that, right?
**Stephen Lang (Raintank, Inc. – Grafana Labs)** 05:52 So there's… I think there's… there's edge cases to… to consider.
Because there's… so it depends where the container image is coming from. Like, we've got the GHCR, the GitHub Container Registry. There's also a few other registries that we… like, public registries that we use. Some of them are subject to limits, which we've seen, so we've had, like, is it 429 or 529, which is too many requests.
And so, like, in some respects, you need to build locally in order to avoid, rate limits on the registry.
But then, like, on the flip side, you've got additional compute and time that it takes to build the image.
So we are using, like, a mixture of… Both repositories, but… and approaches as well. So that… I did see a step, I'm sure, where we have, like, a pre-build of the images that's then, kind of, you know, you do an image export, and then you store it as an artifact in the job in GitHub, and then all the other jobs, just pull on the artifact.
So that is a way that we can sort of build the image locally, kind of reduce The amount of pressure that we're putting on the upstream repositories, but also, at the same time, reduce overall compute, because we're sharing the pre-built image that we do in the workflow.
So it's probably not a big deal if we're, you know, building it on the workflow itself. It does introduce, like, a bit of a… a linear weight, you know, because you have to sort of wait for all the images to build first. I don't know how long these images take to build, but One thing I noticed, because I worked on these images recently, and I noticed that they weren't built automatically, it was like a manual job.
And that job took… well over an hour, twice. One, because, it used to be linear, and it was… it was slow, but even when I parallelized it, it took over an hour. And this was because on the day, surprisingly, GitHub was having issues.
And it was taking ages to allocate runners, so now that the individual jobs only take, like, a minute to run.
That's not… that's not great if you're waiting 20 minutes for GitHub to allocate a runner.
So… I guess what I'm trying to say is.
If we don't pre-build the image.
There's, like, a risk that we could be spending a long time waiting for compute just to build those images as, like, a prerequisite before we can even kick off all the tests.
So… Maybe it's a good idea to keep the pre-built images, but we should definitely look at automating, Either with cron, or maybe just doing it on demand, like, whenever the code changes or the dependency changes, we, like, automatically publish a new version.
I did make a change to get Renovate to pick up The new versions automatically. So if you do do a publish.
then Renovate should pick those up and propagate the changes. But what we're not doing is, like you said.
If a dependency of one of those test images changes, we're not automatically publishing a new version. Maybe that's all it needs.
**Mario Macias** 08:58 Regarding this manual job that takes… hours. I'm the… I'm the guilty of… of this, but, I did it, okay, linearly, let's do it simple. The… it takes… it takes ages to compile, basically because, of the, if we haven't… if you haven't fixed it, and I didn't realize, because of the, cross-architectural builds. Oh, that's sorted now.
Okay, that's all… that's all… also in the… in the… in the images, okay, okay.
**Stephen Lang (Raintank, Inc. – Grafana Labs)** 09:34 Yeah, so we build multi-arch, so this is why I got into it, because I was looking at the arm support, and we only had, like, a few x86 images, they weren't multi-arch. Some of the images were multi-arch, those were kind of built with cross-compilation on x86, which was slow.
But now, like, I reworked that image workflow.
And it separates out into, like, a fleet of arm runners and a fleet of x86 runners. Each one… each image now only takes, like, one minute to build per arch.
And then at the end, it kind of just brings all the manifests together in the same… same way that we do with the main OB image.
So it should be much faster, as long as GitHub can allocate the runners quickly enough.
I would think that the entire workflow to rebuild all the test images should run in maybe, like, 5 or 6 minutes now.
**Mario Macias** 10:26 Okay, okay.
**Stephen Lang (Raintank, Inc. – Grafana Labs)** 10:26 So.
**Mario Macias** 10:27 So, you suggest to stay, as we are now.
**Stephen Lang (Raintank, Inc. – Grafana Labs)** 10:31 Yeah, so we're using now the GitHub Container Registry, which I don't.
**Mario Macias** 10:35 Okay.
**Stephen Lang (Raintank, Inc. – Grafana Labs)** 10:36 subject to a need, limits, as far as I'm aware, and I would expect the limits to be quite high, because it's GitHub runners accessing the GitHub container registry. You'd think it would be, like, internal traffic or something, some kind of internal code.
**Mario Macias** 10:49 Okay.
**Stephen Lang (Raintank, Inc. – Grafana Labs)** 10:50 I don't think we've hit… So the only limits that I think we've hit have been against Microsoft Container Registry and against Docker.
I don't know if anybody's seen, other limits. I mean, we've seen AT, you know, from upstream AT mirrors as well, we've seen limits there.
But I haven't seen… too many requests on the GitHub Container Registry. So yeah, I suggest we keep the workflow, but I can take this on as well as an action, so that when the dependencies get updated, or anything that's touching something that's relevant to those.
Test components, we can, you know, maybe automatically publish a new version.
The only risk is, you know, if we introduce some kind of new automated release, it could potentially break everybody's build.
But then, I mean, maybe that would happen anyway, you know, if we were just building those new images independently on every workflow.
All of those workflows would fail independently, so… I think it's fine.
**Mario Macias** 11:48 paid.
Okay.
Great, yeah, thank you for the… Update.
**Stephen Lang (Raintank, Inc. – Grafana Labs)** 11:54 Yeah, sorry, I said a lot. I think we should keep the images, we should continue building multi-arch. It's a good idea to have a workflow to do this for us, because it's a lot of manual work, and it's easy to introduce inconsistencies. Like we had before, we had some x86, some were multi-arch, we weren't consistent with this, the version numbers were all over the place.
There's also still some images that aren't being built as part of that workflow, which could be.
So it kind of puts, like, the maintenance in a single place.
So I think we should keep it, but just, maybe a bit of TLC to automate the publishing.
**Mario Macias** 12:27 Okay.
**Tyler Yahn (Splunk)** 12:28 Yeah, I think… I think a trigger there, like you're saying, Steven, makes a lot of sense. In fact, it should solve a lot, I guess there is, like, the… you won't know until after you commit the PR, but I guess you can always revert the PR, and then, yeah, we can… at least we'll know, you know, right away instead of a week from now, or something like that. So, yeah.
Okay, cool. Steven's got an action item on that one. Thanks a bunch.
Moving forward… I wanted to talk about this proposal for eBPF-based process and I.O. observability.
This is an interesting one that came across, 3 weeks ago? I think it's… interesting. Yeah, so… I guess there's definitely people on the call who've dug into this a little bit more than I have, I think. But the idea, from a high level, is essentially looking at, process access to the underlying, file system, and seeing, you know, some sort of way to, like.
put observability into that. It's, you know, I'm not exactly sure how this gets bubbled up. It was talked about maybe just showing it as an event, you know, I don't think that there was, like, a tracing thing, so there's definitely, I think, a question I had around, like, how this actually gets, like, displayed, but the idea, I think, is really cool. Essentially… you know, showing these, interactions with the underlying system can be a security-based, thing, it could be a performance-based thing, it could be a, you know, just a general visibility into, like, what an application is doing-based thing with the underlying file system. So, yeah, I thought that was, like, kind of cool.
there was an open question here from Mario, I think, correctly, like, asking about, like, if this exceeds the scope of Obi. I definitely think it, like, it does… exceed the initial proposal, but I'm also not too… I'm not too worried about getting, like, a proof of concept out on this one, or stopping and asking for permission, from, like, a TC perspective, right off the bat, just because I don't see a lot of work in this space, or any work in this space, going on in, like, the collector, which is, like, the other place where, like, the file, process-based metrics were coming from. So I definitely am not too… worried about this. If other folks think otherwise, like, we could definitely loop in the GC and the TC on this.
you know, if you have two people in a conversation, there's probably three opinions, so, like, I'm sure there's, like, a lot of, different thoughts on that one, so, like, yeah, like, we could definitely leap through them in. I do also think that, like, the thing that really stands out to me, though, is just more about, like, timing. I'd want to, like, pause on this one.
In the implementation until after KubeCon, but, Yeah, I wanted to bring this up and just see what other people's thoughts on this were. If they haven't taken a look, take a look. Definitely think it's really interesting. But yeah, just pause here.
**Nikola Grcevski @ Grafana / OpenTelemetry** 15:34 Yeah, I… I had a thought when I first saw this, and I was like, yeah, it's similar to the process observability we had before, but it's not, actually. And… Recently, I've kind of been looking at you know, agents or whatever, and I think this is where Hai Bing is coming from, and… the security concerns, what people used to have, like, if you say you build a tool like Falco or Tetragon a while back, you were just looking at Linux events and whatnot, but To eliminate a lot of the noise.
I think the right thing is to kind of bring some of the higher-level concepts from OB into those system-level events. Without them, you just get too many noise. Like, the example I gave, like, running who am I as an admin on a Linux host, it means nothing. Like, they're just checking to make sure they're running in the right user. But then, who am I, from a web service.
that's pretty bad. So, knowing that this is HTTP service, and it's doing who am I, that actually is something. But you don't know HTTP service unless you have OB.
I mean, tools like Falco and Tetradron cannot actually get that information.
So… I think there's a lot of potential here. I was gonna… I think I… I agree with your statement there, there probably should be post-1-0.
But we can actually, if they're keen on working on this, we can suggest that they actually Create a branch.
and start experimenting in the OB with, you know, building this additional tracer for ZigV and whatnot, that could be potentially enabled.
I know branches are not great, but it's just if they want to prove out their concepts.
This can get really good, like, the thing I was thinking of, like, so the OSEL profiler, which we already import, I believe to some extent, can walk stacks and… Getting that together with… the system calls.
The stuff we capture in OB, the payloads and the stacks, I mean, you've got the I honestly think it's the best security product on the market, if you do all that, because you're monitoring all stacks, everything from the application, and with the agents.
Doing all sorts of things.
This becomes more important, so, yeah?
**Tyler Yahn (Splunk)** 17:55 Yeah, I definitely agree. I think all those are really good points, and I think it's like… it's one of those things where I think it's gonna be super valuable, but I don't even fully understand, like, the feature set, but the more we build it, I'm sure I'll be like, oh, this is actually cooler, because we could do this, or this, or this, so… yeah.
**Nimrod Avni** 18:11 I think we can even, correlate it to… to, like, incoming requests and stuff, like, we can… I don't know what's the end, like, goal, if we… if it should be, like, spans, logs, whatever, but anyway, it can be, like, part of the same… session, or whatever, it'd be really cool.
**Nikola Grcevski @ Grafana / OpenTelemetry** 18:27 Yeah, you'll be like, this request did an exact V here.
I don't think anything can tell you right now. You know, if you just want to say, track security over here, and you get, oh, during this transaction, you can do the syscalls.
Maybe that's a red flag.
You know, and… and… I mean, today's day and age, like, any security solution, or even just… you don't actually need a security solution to do a lot of this, because… Like, the agents are pretty good at looking at traces and figuring out what's going on.
Actually, to try this, I enabled, the payload extraction, sort of, Hold on.
And just… and I created sort of an application that maybe is acting maliciously. Once in a while, you call it, and it does something weird, such as export some sensitive data out of your service to an additional endpoint. And I just asked, Claude, is there anything malicious going on?
Straight up.
Josette.
that particular transaction, this service, at this time, did some, like, export private data that the application is not doing. It was like, I didn't have to do anything, I just said, I have this service, look at my traces and see if there's anything malicious.
That was it.
**Tyler Yahn (Splunk)** 19:52 Cool. Yeah, that is really cool.
Okay, yeah, I mean, I think it, like, I left a little blurb about it, but yeah, go ahead, Mattia.
**Matt** 20:04 I couldn't unmute myself. So, I wanted to ask, since we are leaning into security, do we stop at observability, or do we want to… Proactively stop some threats.
Because we can.
**Nikola Grcevski @ Grafana / OpenTelemetry** 20:20 We can, yeah. And it sort of, again, goes back to the story that Ovi is the right place to do this, again, because we actually understand the HTTP request.
It's not just anything, we could actually tell this request needs to be stopped.
you know, in a sense that… It's like looking at the network level and whatever it may not actually be, but… Maybe we can do some of the payload extraction at eBPF level, and see if something is actually trying to export PI data, and cut it off there.
You know, right now we do it in user space, but maybe some of it could be retrofitted to be done Or it could be, we let it go once, but then after that, it's not there anymore.
You know, or you can say, this user needs to be blocked, but not the IP, but this user ID.
I mean, that would be somewhere in the headers, in the auth header, and you can just say, oh, this user ID is coming in, that's in the header, don't let it go again.
We can just block that particular… User.
Without parsing the protocols and all this, it's impossible to do some of this more advanced Sort of.
defensive measures.
**Stephen Lang (Raintank, Inc. – Grafana Labs)** 21:43 That's like… Yeah, I think we should.
**Matt** 21:44 the… Oh, sorry, go ahead, Steven.
**Stephen Lang (Raintank, Inc. – Grafana Labs)** 21:47 I was just gonna say, it's like verging on service mesh, though. I mean, sounds really cool, but what are the boundaries for, like, how far you take it, and where would you think about integrating with Other existing, like, dedicated services, and, like, where Like, what is… what I'm trying to say is, the scope creep on this over the next 12 months could be huge. So, like, given, like, a direction and a vision for what the scope of OB could be with something like this, like, what would the boundaries that you could sort of define and say, well, at this point.
you know, it's worth having a separate project which doesn't exist that could be dedicated to this purpose, or, you know, at which point could we integrate with, I don't know, other existing projects, which are sort of big in this field?
Otherwise, it's like, you could bring so much into Obi, just because eBPF can do it.
You know, it could… it could just be, like, a huge, you know, guard process, effectively, and… I think without some upfront decisions as to how far to take the architecture, it could, I'm just worried it could be messy, you know, the implementation, if it's not thought about.
It could be overwhelming.
From an architectural point of view.
**Nikola Grcevski @ Grafana / OpenTelemetry** 22:56 Yeah, it's a fair point. We can make it sure that maybe OB's just a module that can serve and export some of this data that can be shared by, like, actually consumed by other tools that do some of the more advanced stuff.
**Stephen Lang (Raintank, Inc. – Grafana Labs)** 23:07 even if we build those tools right, I'm not saying that we don't do it.
**Nikola Grcevski @ Grafana / OpenTelemetry** 23:10 I'm just saying, like.
**Stephen Lang (Raintank, Inc. – Grafana Labs)** 23:11 Where are the boundaries?
**Nikola Grcevski @ Grafana / OpenTelemetry** 23:13 Yeah.
**Tyler Yahn (Splunk)** 23:15 Yeah, I mean, I think that that's actually a really good point. Yeah, I have the same concern, but I'm also just, like.
that integration, I think, is actually even more powerful, right? Because it kind of follows the vision of what this is meant to be, where, like, you know, if you could integrate with something that is going to do those proactive security, you know, actions on your behalf, or a platform that does this, right? Like, you're really enabling, like, through this, like.
technology, right? And I think that that's… that's a… that's a good idea. So… Correct scoping sounds great. I mean, I definitely think for the initial offering, at least, like, we should try to just get data, but, like, I think, yeah, to Tia, Steven, and your point, like, just that integration, at least, into preventative actions, like… even proactive actions, eventually, would be, like, really cool. So, yeah, I think that that's really good ideas, and we should keep that going.
Okay.
**Matt** 24:08 I think it's important to specify this in the issue, because.
**Tyler Yahn (Splunk)** 24:12 Yeah.
**Matt** 24:12 If we want to do proactive stuff, we need to architecture this to… from the base to work with some technologies, like, for instance, I think LSM probes would be the best here.
But if we just have to observe, maybe trace points are just fine.
**Tyler Yahn (Splunk)** 24:35 Yeah, that's a good question, actually.
**Nikola Grcevski @ Grafana / OpenTelemetry** 24:39 Yeah, I mean, just… why don't you ask that, Mattia, on the issue, and say, yeah, maybe we can give them the recommendation, start working on it in a separate branch?
And let's see how this works out, and… Ask questions, do you wanna… You know, stick with just seeing rather than acting on, and… Maybe if they…
**Tyler Yahn (Splunk)** 25:01 And, well, and I think it's, like.
I mean, I definitely… I would recommend that, but it's also just, like, how do you… how do you plan to integrate with the things that are doing the acting on, right? Like, if we wanted to build something that uses whatever we built here, to Macias' point, like, are we building the right infrastructure for that?
Yeah.
Or is there just a better way to, you know, build it if we're just going to observe it? It's definitely interesting to think through, yeah.
But yeah, we, don't need to solve the problem on this call. Macias, I think if that sounds great, if you wanted to leave that feedback, that'd be… that'd be…
**Matt** 25:33 Yep, I will.
**Tyler Yahn (Splunk)** 25:38 Okay, cool, yeah.
That's… that's pretty exciting stuff. Let's… Keep an eye on that one going forwards. Okay.
Next up, I also wanted to follow up on the AI policy discussion that we had last time. I took a look at this after the call. One of the things that came out of it was that our AIPolicy.md is, it's a bit contradictory, it's a little bit of an interesting one. We have Claude.md.
agents.md and an AIPolicy.md. I'm guessing I'm not saying things that most people don't already know, but, one of the kind of confusing things is, like, obviously Claude recognizes Claude, and then these import both of these other two. Agents is something that, like, Codex, and, like, a bunch of other, free, models and other, runtime agents are, like, using.
nobody defaults to AI policy, but it's imported from each one of these. I was looking at recommendations on how to structure these, and they were saying that, like, doing, like, file imports is usually not ideal if you wanted to actually have agents, follow instructions.
It also is, one of those things where, trying… like, it can… I think you can load something like… 128, like, kilobytes of an AI policy, but they say, like.
Once you get past, like, 200 lines, it starts to not really follow the directions either. So keeping these short and sweet is also one of the other things we want to look at.
the main thing, though, is that there's, like, some contradictory statements, across these, things. So, one of the things that, like, kind of stuck out is that probably need to make some decisions on this. Like, there's definitely things like saying, like, you know.
an AI agent's not allowed to do anything besides boilerplate, but also an AI agent needs to, like, do all the work, kind of thing. So, it's a little bit, yeah, even just self-contradictory when you read through the whole thing. But, one thing that was, like, kind of obvious is that we can, like, probably structure these a little better and see if we can then, like, get a better, adherence to this, I think, is kind of the goal.
I did want to ask, though, like, is, do we want to have the AI policy be something that is human-read, and it's for humans to be reading, and use Claude and… or Cloud.md and the agents.md as, like, the agent, like, the bots-only kind of policy, or the bots-specific policy?
That was kind of, like, my first question. It's definitely, I think, an open question.
I think that there's also, you know, questions around, like, I think we copied our original AI policy from, Tetragon, maybe? I can't quite remember, I think Rafael did it. So, like, I think it was one of those things where it was, like, it was a starting point.
But it says that, like, agents are not allowed to do anything other than boilerplate implementation changes, which… I don't know if that was actually intended, but I did want to ask the group if, like.
we're okay removing that, because it is also self-contradictory with a lot of the things that are in the other policies. So, yeah, I needed just some thoughts on that one.
Yeah, there's also language saying that coding agents are not able to draft issues, descriptions, pull requests, descriptions, reviews, comments, or substantial human revisions.
But then there's also language saying, like, when they do do this, to use these particular forms. So, again, self-contradictory of, like, should they be doing this, or, you know, are we okay with them doing it? But then, like, let's go back to what we were talking about last time, where it's more about crafting statements about how they should be doing it, I think is kind of the thing.
And then, yeah, so, yeah, other things being, which review, attribution, and disclosure reminders, should agents provide?
It's not quite clear in our policies, around this one.
which restrictions must be enforced, by tooling, or CI, rather than expressed, yeah, as the module, instructions. But this, I think, is the… more of a capture of what we were talking about last time, rather than what I've found in the… deep dive into these, policies. So, yeah, I just want to pause here, get some thoughts from folks, and, happy to iterate on this, but… Yeah, until we can kind of answer some of these questions, I think we're kind of not providing agents a lot of guidance here.
Right in Japanese.
**Nikola Grcevski @ Grafana / OpenTelemetry** 30:01 Yeah, your question about non-boilerplate, I think that ship has sailed.
Yeah, I mean, there's so many changes that are being done, but… I think it's impossible. I think we need better instructions for the agents doing the work. To be honest, I've had a lot better success I have to kind of repeatedly go, and I don't know, maybe this is just normal, but the first iteration just dumps everything into a single file, makes functions that have multiple concerns rather than splitting them, but you have to go and specifically say, no, I want you to split every single one. I've actually had even asking it make the code more human-readable for reviewers actually does a better job at actually writing the code in a better way. A lot of times, it just looks like this spaghetti, but then they'll say, make this something easy humans can… something humans can easily understand. It actually does a much better job.
So maybe that's… neat.
I mean, it won't slow down, the slop, but… and people not thinking through problems, but… Like, yeah.
**Tyler Yahn (Splunk)** 31:12 Well, I think it's more… yeah, I think that's a great suggestion. I think that's a great line we should add. I think it's just about, like, if we can… we're always gonna get people that are not gonna pay attention, or they're gonna tell their agents to ignore it, right? Like, that's… Yeah, that's not… I think… those are not people who really want a part of the community, let alone, like.
ones we want to structure these for, but I do think that what we want to do is provide, like, guidance for people that are trying to effectively use this. So, like, yeah, structuring agent NMDs, or Cloud NMDs, like, appropriately would be helpful with, like, things like what you just described. Another thing that I found is that, like, you can do, a… like, a hierarchical structure, where certain, like, you know, maybe put it… like, I've read that, like, you can have AgentsMD, like, within the structure of your code, so, like, within our eBPF code, we could have another one with additional instructions versus, like, other Go packages or something like that. So, like, yeah, maybe there's, like, specifics we can try to break it down, because again, like.
It's about context window, and, like, the more we have there, the more it's gonna start to, like, you know, ignore it as it gets, you know, more and more. So, like, yeah, maybe there's just ways that, like, here you want to load in the eBPF ones as well as these other, like, top-level ones, so… Yeah, I think that sounds, like, totally… It's an improvement case, I think I just saw, like, a Martin Fowler skill for refactoring. I think if that's… Also something we can do is, like, in our AI policy, is list maybe particular skills that we find useful, or things that, like, we find very helpful for users, and, like, things they should be, you know, including in their development process. I think that that's also very interesting, helpful, to engage the community on that one.
**Nikola Grcevski @ Grafana / OpenTelemetry** 32:55 Yeah, yeah, I think that will help. I think we should try it. We should try to improve this, and let's see what the effect is. I mean… Yeah, it's not like… like I said, it's not gonna stop… stop bad PRs, but hopefully it gets… better ones. Like, for example, I was fixing this last one.
That was this, finding in every PID namespace all the open ports and whatnot. And if you look at the PR, the code actually eventually, after back and forth, became clear what it's doing, but For every new pit added, it was iterating across all the pits.
And then… I mean, it had this back-off period, so it doesn't do this, but if you look at the function itself.
it actually queries all the PIDs and then walks them individually. So when you add a new PID, just walk that PID. Why do you have to walk all the PIDs again and repeat all this process, right? There's no point. You can't stop that. I mean, if a person is not actually trying to understand the change, and just submitted a PR with an agent.
If the agent is not smart enough to click that, it's not smart enough. There's nothing you can do about that.
Or we just need to stand back and just kind of… You know, not accept those changes, or…
**Tyler Yahn (Splunk)** 34:14 Yeah.
Okay.
If there's other thoughts, we could talk a little more about it. If you have answers to any of those questions that I asked, I'd appreciate it if you commented in that issue. I'm looking for feedback on that, and looking for, like, maintainers specifically having direction, but the rest of the community as well.
And then we can go forward and try to update the policies from there.
Okay, moving on. Next up, Mara, you want to talk about metadata beyond Cates?
**Mario Macias** 34:51 Yes, so, for example, for some of our telemetry, like service graph metrics, or we're showing remote peers in the metrics.
In Kubernetes, it's easy to do because we are able to build a map of all the IPs and their respective entities. But this becomes more complex outside of Kubernetes, where we don't… we don't have this kind of, central entity.
So, I'm thinking on… on expanding the utility of OB beyond Kubernetes.
And we are investigating or considering some approaches to provide a central service.
To… to share the metadata. Like, for example, the current Kubernetes catch service improve it so every Vela can push data to it.
Or even being able to let users providing an external… an external dependency on… on Juice, but we would like to start with something simple, and that doesn't require extra friction in the setup from users.
So… yeah, you might expect some proposals, some proof of concept in modifying the current catch service to… to get data, or to expand it beyond Kubernetes. I don't know, what do you think. We can discuss it once we get the proof of concept.
**Tyler Yahn (Splunk)** 36:39 So, I definitely think that that's important, and if I'm not mistaken, Mike has been working on, like, doing something similar for, like, annotations in this space.
But the first thing that comes to mind is the… the, The single point of failure that the cache then becomes is definitely… something where I think we can probably try to solve that, right? We would probably want to have, like, some sort of, like, distributed, caching service that, like, already exists as, like, a backing technology, something like a, you know.
**Mario Macias** 37:07 Yeah.
**Tyler Yahn (Splunk)** 37:08 Something like that, where, yeah, we can… we can then… front it with, you know, our own API, just because I really would not want to re-implement, leader elections and things like that.
**Mario Macias** 37:19 Yeah.
**Tyler Yahn (Splunk)** 37:20 Something in that sense, would be great.
But yeah, I… and then, if we have that API, like, that sits in front, the pluggable nature of what you just described as well would be really cool, so then, like, other third parties could extend it, or, you know, have all these different modules. But yeah, I like the idea, though, in general, yeah.
**Nikola Grcevski @ Grafana / OpenTelemetry** 37:38 Yeah, we had other ideas, too. I mean, I don't know if, I mean, we had a POC that… One side was shipping all the information to the other side through headers.
For HTTP, so we can extend that for HTTP2. We have response headers as well, say what the other side is, because you need both to actually create service graph without having a central repository.
Yeah, the other thing is, like.
We're also kind of thinking about, maybe some way of… It's not technically gossip, but it is gossip, so if OB can have a port to which one service can send to the other, it's known services. So, let's say… So we have network metrics, and the network metrics fly through, but… so we know which server… which OB is talking to which OB. This is almost like thinking it kind of broadly, it's like a sidecar mode, where instead of each… each one OB instance monitors a whole cluster. It's like, each per container, you have its own OB. And then how do they know about the names of the services they're communicating? So technically, if OB… each OB had a port that was exposed, then… it can actually, be asked about… they'll tell me about… I see I'm talking to you, through the APIs of something that we recognize, then tell me about your names of the services you're monitoring.
And then each one can ask the other.
Oh, I can see that I have requests coming from this IP address. Does that one expose an OB metadata port that we can ask about their services?
So then you don't need a central repository, for that, but sort of more, like, it's on demand.
And then, eventually.
Or periodically, they can scan, or they see a new, something new coming through, they can ask again, or things like that.
**Mario Macias** 39:45 I think Nimrod raised the… his hand.
**Nimrod Avni** 39:49 Yeah. So I wanted to, like, to discuss mainly what Tyler said with, like, using an external component, let's say Redis or something, because we already, rely on the Kubernetes cache And I think I had a proposal a while back to try to make it, like, integrate it into, like, a collector somehow, just to… to be, fully, like, you know, compliant and not have this kind of, oh, we have, like, OB, which can be embedded in the collector, and that's good, but you also have to have this, like, random application, in order to make it actually, like, perform on high scale.
But, I'm not sure, like, I'm trying to think if that's the correct direction, because if we're gonna say, like, that we're gonna have, oh, sorry, that's my dog.
**Nikola Grcevski @ Grafana / OpenTelemetry** 40:45 Yeah, maybe that's a good idea, just kind of build this into the collector somehow, like a metadata service.
**Nimrod Avni** 40:51 Sorry.
**Mario Macias** 40:51 Yeah.
**Nimrod Avni** 40:52 But what I suggested is basically, I don't know, maybe have it as some sort of, like, collector extension, or… and try to make it, like, generic. Like, I mainly thought about in the context of, like, the Kubernetes attribute processor. You can, like, drain that information so you can have a kind of a distributed cache and use the Kubernetes Attribute processor the same, but maybe if we want to enrich other stuff, then, I don't know, maybe we need to think some, like, more generic solution? I don't know.
**Nikola Grcevski @ Grafana / OpenTelemetry** 41:31 I like your collector idea for this.
**Mario Macias** 41:33 Yeah.
**Nikola Grcevski @ Grafana / OpenTelemetry** 41:34 Kubernetes. Kubernetes is a little bit complicated, because Collector is usually also going to be on the same node as Obi is.
And the collector, by default, only looks at the current node metadata, but Obi, to be able to do the service graph independently without traces.
Across services on different…
**Nimrod Avni** 41:53 Yeah, that's why I thought maybe having a collector as kind of like a… instead of a demon set collector, more of, like, a deployment collector that's with a So, like, kind of like a gateway or something?
**Nikola Grcevski @ Grafana / OpenTelemetry** 42:06 with runners, like.
**Nimrod Avni** 42:07 Like, you know, as a deployment with a set of replicas for, You know, surviving… That's true I don't know.
**Nikola Grcevski @ Grafana / OpenTelemetry** 42:16 Oh, okay, sorry, Maya.
**Mario Macias** 42:18 No, I think… I think your idea is good, but the scenario we're considering, actually, is when we don't have Kubernetes.
**Nikola Grcevski @ Grafana / OpenTelemetry** 42:26 November.
What it means is, like, have a collector, but you're gonna have to have a collector anyways.
So you're having…
**Mario Macias** 42:32 Yeah.
**Nikola Grcevski @ Grafana / OpenTelemetry** 42:33 I mean, unless…
**Nimrod Avni** 42:34 And the main thing is we need some central component, and, like, it might be some Redis, it might be something that we implement, and we need, like, have it have, like, different fetchers for, like, you know, one fetches Kubernetes data, one fetches… whatever, container data, AWS, I don't know.
So I'm trying to think if we… standardize that component.
**Mario Macias** 42:59 Rela will push.
**Nikola Grcevski @ Grafana / OpenTelemetry** 43:01 Yeah, Obi… Obi will push through this collector Through a different interface of some kind.
But that's actually a good point, because you would expect that in this environment, you must have a collector of some kind where you're sending your data to, from all these, if you will, sidecars.
And then This collector could be the central data point, because we already have one.
I mean, we discussed that maybe we should query Prometheus, but we abandoned that idea, because it's… I mean, it's non-standard and whatnot, but… This would be similar, we query the collector, It's almost like a…
**Nimrod Avni** 43:39 It would be like a collector if we make it a collector extension that basically.
**Nikola Grcevski @ Grafana / OpenTelemetry** 43:43 Right.
**Nimrod Avni** 43:44 export this endpoint and has, like, I don't know, populated some… somehow.
I guess we need to check if, like, that behavior… like, it basically… I don't know if it forces you to run OB with another… not even, like, a collector on your node, with, like, a central collector deployment.
But I think it's better than forcing you to run it with, Kubernet, like, with, like, a random image that we built.
Yeah.
**Nikola Grcevski @ Grafana / OpenTelemetry** 44:13 Okay. Yeah.
**Mario Macias** 44:14 Okay, yeah, I like the idea. Yeah, our… regarding the comments, Tyler repair, respecting the single point of failure, our idea was let the users choose The level of… operational overhead.
Either if they had a… small cluster, maybe using this single point of failure is fine. Then, if they want some replicas that share data, the problem there was, we found that in cloud, these self-discovery mechanisms in bare metal are simpler, but in cloud, you have some extra layers, so this discovery will be a bit more complex, and you will need to give some credentials from your cloud provider. So that's why we were thinking on some… different solutions, from a very single point of failure to something distributed, or even directly going for readies, or for a compacted topic, or something that is provided externally, depending on your Performance and security and fault tolerance requirement.
**Tyler Yahn (Splunk)** 45:25 Right? Yeah.
**Nikola Grcevski @ Grafana / OpenTelemetry** 45:26 And over the Nimrod's idea of the collector, I mean, that's maybe a sole problem, because people know how to set up load balancing collectors and whatnot, and…
**Mario Macias** 45:35 Yeah.
**Nikola Grcevski @ Grafana / OpenTelemetry** 45:35 Let me consider a collective cluster, yeah.
**Mario Macias** 45:39 They will any ways to share data, right?
**Nikola Grcevski @ Grafana / OpenTelemetry** 45:41 Yeah.
**Tyler Yahn (Splunk)** 45:42 But, yeah.
**Mario Macias** 45:43 Okay.
Okay, and anyway, I like the idea of reusing the collector.
**Marc Tudurí** 45:55 When you mean collector, it's OpenTelemetry collector, or… Nikola Grcevski @ Grafana / OpenTelemetry 45:59 Yeah, yeah.
**Marc Tudurí** 46:01 Yeah. Okay.
Yeah.
**Tyler Yahn (Splunk)** 46:07 Alright. So, yeah, that sounds, that sounds good. Definitely some work in progress there, but Yeah, I think I'm super excited about that. I think, Mike, if you wanted to jump in on that as well, like, I know you've been working on, these sort of level of… granularity outside of Kubernetes, so yeah, I'm sure… I'm sure Mario could enjoy the collaboration, yeah.
**Mario Macias** 46:28 Sure, sure.
**Tyler Yahn (Splunk)** 46:31 Last step, Nikola.
**Nikola Grcevski @ Grafana / OpenTelemetry** 46:32 I think I mentioned, I mean, related to what Mike was talking about, we… I think we need that feature, essentially, to create, network metrics per service. Because right now, our network metrics are global.
So, having them for service is going to be required for this, because otherwise… It's kind of hard to tell what… all the noise that you're gonna get from.
**Tyler Yahn (Splunk)** 46:56 In other words, it's just gonna be a bunch of IPs, yeah.
**Nikola Grcevski @ Grafana / OpenTelemetry** 46:58 Yeah.
**Tyler Yahn (Splunk)** 47:00 Yeah.
Okay, cool.
Nikola, you wanted to talk lastly about Ruby 4 doesn't have context propagation? Looks like you've already gotten a response from Nimrod.
**Nikola Grcevski @ Grafana / OpenTelemetry** 47:10 I was just gonna ask Nimrod if he intends to work on it, or should I put it on my list to look at, but…
**Tyler Yahn (Splunk)** 47:17 But sounds like he's already, worked on it, so she's looking for reviews. Okay.
**Nimrod Avni** 47:22 I just… I just disabled… I think… I think I already merged it. I just disabled it, but I don't know how to make it work, like, on… on Ruby 4.
**Nikola Grcevski @ Grafana / OpenTelemetry** 47:30 Yeah, I'll take a look to see what's happening. Maybe it's not possible using the same mechanism. I mean, that was kind of, like, a weird… We did this, like, I was detecting which threads in the Puma were involved, and as the worker threads, which ones were actually given the work, and…
**Nimrod Avni** 47:47 Yeah, I tried to, to, like, you know, like, I try to, to search, any other way to do it, because I think the current way might be kind of, performance heavy, because you basically hook allocations, like, every time.
**Nikola Grcevski @ Grafana / OpenTelemetry** 48:02 Yeah.
**Nimrod Avni** 48:03 You know, every time that we basically allocate any object, even, like, the BPF probe itself, it's just, like, the, you know, the fact that you hook that U-probe.
**So I tried first to gate it, and then I tried to find, like, if we can connect to any, like, Puma, whatever, but I don't… I don't think it worked, but maybe I need to do more exploration, but… Nikola Grcevski @ Grafana / OpenTelemetry** 48:27 No, no, it's all written in Ruby, unfortunately, there's no… there's no native symbols, so the only thing I can…
**Nimrod Avni** 48:36 I poo myself.
**Nikola Grcevski @ Grafana / OpenTelemetry** 48:37 Throwing myself as Ruby.
**Nimrod Avni** 48:39 Yeah.
**Nikola Grcevski @ Grafana / OpenTelemetry** 48:41 So, the only… so, there's basically two things, two approaches I kind of looked at. One was to kind of… Put a probe on their lock.
The other one was to put a probe on the alloc, a specific alloc, when they extend the array or something. It wasn't just a… because I think they have cheap allocs, but this one required a more expensive alloc.
So I stuck the probe in there, and to kind of capture And I'm detecting which thread is doing it, so I know that it's the one that actually is gonna put the new item on the list.
And that's where I record one information, and the other guys, as they pop it. So, I know it's expensive.
I didn't measured.
**Nimrod Avni** 49:26 Maybe we can do with, like… similarly, I don't know, like, I don't know Ruby at all, so… but maybe we can do something with, like, how we do Node.js with, like.
**Nikola Grcevski @ Grafana / OpenTelemetry** 49:34 Yeah. Like, injecting…
**Nimrod Avni** 49:36 code at runtime? I don't know.
**Nikola Grcevski @ Grafana / OpenTelemetry** 49:40 Yeah, I don't know if they… yeah, maybe that's a way… maybe that's a way to do it. I don't know if Ruby… I mean, it definitely can dynamically load an agent on start. That's easy. Yeah, you supply it with RubyOpt. I don't know if you can… do it on… The process is running.
**Tyler Yahn (Splunk)** 49:54 Yeah.
**Nimrod Avni** 49:55 Do we do it with, like, Java? No. Do we… Nikola Grcevski @ Grafana / OpenTelemetry 49:57 Java, same thing, they do have an interface to load dynamically an agent.
Python added it in version 3.12, Mark, right? Or 3.14. Python is doing… we're able to do it in.
**Marc Tudurí** 50:11 145 numbers.
**Nikola Grcevski @ Grafana / OpenTelemetry** 50:13 protein.
**Marc Tudurí** 50:14 Cool, yeah.
**Nikola Grcevski @ Grafana / OpenTelemetry** 50:15 So maybe we can write a Python agent, but I don't know what happens in Ruby.
**Tyler Yahn (Splunk)** 50:25 I feel like Ruby.
**Yeah, I mean, it may exist, but… Nikola Grcevski @ Grafana / OpenTelemetry** 50:30 But… Yeah.
**Tyler Yahn (Splunk)** 50:31 I think we'd have to do some research on that one. I'm not exactly sure, yeah.
**Nikola Grcevski @ Grafana / OpenTelemetry** 50:35 It's not a bad idea to look into that. I never considered that, So, yeah, the reason it's not working, I'm guessing they changed the thread names or something, or… maybe they're… I mean, it should be Puma-specific rather than Ruby-specific, because I'm looking at the exact Puma versions, but maybe they… Puma updated as well, and it's… Using different names for the worker threads and whatnot.
We don't match them anymore. I have to see what happens in the log.
But the way, actually, I managed to figure it out is by putting… I used, what is that? BPF trace tool that I can trace?
Now you can write your own custom tracer, so I… I wrote a custom tracer for the Ruby runtime, and I was just watching what it does when I ran a transaction after transaction, and tried to figure out at which point in this Ruby API can I attach to? That sort of makes sense out of that, though.
Yeah. I know Mario noticed it as well, like, just the other day, he was… he wrote a new Ruby app, and I think it was Ruzzy Rue before, and we couldn't context propagate.
**Mario Macias** 51:52 Yeah, exactly.
**Tyler Yahn (Splunk)** 52:01 Okay, well, sounds like some more work in progress on that one.
Looking at the agenda, we are at the end of the agenda. We've got, less than 8 minutes left. Any other topics folks wanted to talk about? Announcements? Projects they're working on?
**Nimrod Avni** 52:20 Thank you for merging my, PR, Tyler. I worked on it so long.
**Tyler Yahn (Splunk)** 52:26 Yeah, yeah, well, well done on that one.
**Nikola Grcevski @ Grafana / OpenTelemetry** 52:29 The schema? The schema?
**Tyler Yahn (Splunk)** 52:30 Yeah, yeah, the full, the hotel, yeah, yeah.
**Nimrod Avni** 52:34 And I'm finding a few more issues, but at least we have, like, the main one there, so we can improve it a little bit.
**Tyler Yahn (Splunk)** 52:43 Exactly.
Rupesh, I see you have your hand up.
**Rupesh Punna** 52:46 Hi, guys. I'm Rupesh. I'm a Grafana program attendee.
So, because I worked in eBPF and, Java as well. So, I'm thinking, like, if I can do some contributions to this OBI, and, I found an issue where OBI… I mean, I've looked into an issue where OBI is not differentiating between which JVM language it's been detecting, like, everything is, like, Java, not, like, scale or another.
So I was thinking, maybe, if I can work on it, my direction would be something like, let's… How would you find, like, a… take, like, a whole class path?
Of, of the process, and see, like.
**Which main class is being loaded, and then take the jar file from that and differentiate between which I mean, I'm not sure if this is the right approach, but this is what I'm thinking about, so… Nikola Grcevski @ Grafana / OpenTelemetry** 53:47 Yeah, that's the one up. I'd say yes, go for it. I think it'll probably detect the… By looking at the classes, that exist.
You can probably guess whether it's Gallo or… Kotlin or some of the other languages, based on some detection of what classes have been loaded. But you have to do loaded, rather than if it's just in a jar, it may not necessarily… if it's on disk, it doesn't mean it's loaded, right? So… If you can do loaded classes, that would be better, but… We have a way to talk to the JVM to give us the loaded classes, I just don't know how expensive that call is. We had some issues in the past.
But, Jamie was not responding on time and things like that, but…
**Nimrod Avni** 54:35 I remember we… I don't remember, I think we talked about some… that issue, and we thought maybe… I don't know, like, if it should be in the same, like, attribute as telemetry SDK language, or should it be, like, another… Like, runtime, because they're gonna theoretically, right, break, you know, something… like, consumers don't know this, like, enum, I don't know, like… we maybe should consider it, but I think we are… Nikola Grcevski @ Grafana / OpenTelemetry 55:07 Thank you, yay.
**Nimrod Avni** 55:08 Like Dino or something, so maybe.
**Nikola Grcevski @ Grafana / OpenTelemetry** 55:10 anymore.
**Nimrod Avni** 55:11 Maybe we're good. Maybe we should, like, I don't know.
**Nikola Grcevski @ Grafana / OpenTelemetry** 55:14 Brands.
I think also there's a complication there, because especially with the JVM, doesn't necessarily mean that Do you see Kotlin, that your application is just Kotlin?
I mean, people mix them up. They have Scala, they can just import a Scala jar.
like, something… a library that's written in Scala, and you can just use your Maven build and bring in the dependency. Doesn't necessarily mean that application is written in Scala, just because you have some Scala code.
**Nimrod Avni** 55:42 as… Nikola Grcevski @ Grafana / OpenTelemetry 55:43 It's complicated.
**Nimrod Avni** 55:45 maybe it's on how you build the… I don't know, with, like, if you build with SBT, or you build it with Kotlin, you might have… Nikola Grcevski @ Grafana / OpenTelemetry 55:52 Yeah.
**Nimrod Avni** 55:53 Some traces of it? I don't know.
**Nikola Grcevski @ Grafana / OpenTelemetry** 55:56 I think it should be probably a separate field, and we list all the languages we found, sub-languages in there, because then you say this is Java, Kotlin, and Scal in here, or something like that, like an array attribute.
**Rupesh Punna** 56:08 I don't know, I bet.
**Nimrod Avni** 56:12 I think maybe in the future, like, I don't know if Mario already did the Deno, like, adding it as a language, but maybe… Maybe it should be, like, I don't know, if you have, like, Node.js as a language.
**Nikola Grcevski @ Grafana / OpenTelemetry** 56:26 Yeah, it's tough.
**Nimrod Avni** 56:27 Whatever, like, and then you have, like, the framework… not framework.
**Nikola Grcevski @ Grafana / OpenTelemetry** 56:31 Yeah, yeah, I know, yeah, yeah.
**Mario Macias** 56:33 Yeah.
**Nikola Grcevski @ Grafana / OpenTelemetry** 56:34 Yeah.
**Mario Macias** 56:34 Yeah.
**Nimrod Avni** 56:36 Might make sense, I don't know.
**Mario Macias** 56:38 Yeah, the use case was to follow the… somewhat the standard, despite, I think, the language should be JavaScript, of course, yeah.
**Nikola Grcevski @ Grafana / OpenTelemetry** 56:48 Yeah.
So this would be Java, but I think we can list the Kotlins and Scalas, or JRuby separately.
Because think of it this way, like, I have JRuby, I can just… bring it as a dependency on my project that's written in Java, and have a… Merubi interpreter in my job application that runs sometimes.
And so, just the presence of JRuby existing doesn't mean your application is actually… written in JRuby.
**Mario Macias** 57:18 Yeah.
I don't know if the manifests of the JAR files To go simple, to manifest, say something.
Not mandatory, I guess.
**Nikola Grcevski @ Grafana / OpenTelemetry** 57:29 Yeah, could be. Could be that something in the manifest would tell us what's the main language. Maybe that's the right way to go about this.
Yeah, but…
**Tyler Yahn (Splunk)** 57:39 Do you have access to the manifest?
**Nikola Grcevski @ Grafana / OpenTelemetry** 57:41 Yeah, yeah. We parse it now. This is how we find the routes.
Because I had to rewrite it.
**Tyler Yahn (Splunk)** 57:47 Oh, I see what you're saying, not the… okay, not the build, okay, yeah, I got you.
**Nikola Grcevski @ Grafana / OpenTelemetry** 57:51 I know the build manifest. It will be some of those meta-inf files in the jar. Yeah, I agree. They might actually… if they squiggle something in there, what's the main class that's pulled, and if that looks like… but you can't tell Kotlin versus Java.
Maybe. He needs to research, needs to research.
**Mario Macias** 58:09 Hmm.
**Tyler Yahn (Splunk)** 58:10 Well, okay, we're coming up on the end of the hour here. Rupesh, hopefully that was… not too much of a stream of consciousness, but I think that there's some good direction in there.
Hopefully that helped.
Okay.
**Nikola Grcevski @ Grafana / OpenTelemetry** 58:24 Thank you.
**Tyler Yahn (Splunk)** 58:24 Alright, cool. Well then, let's, Right, in the meat.
Go ahead, yeah.
**Nikola Grcevski @ Grafana / OpenTelemetry** 58:31 4 unique.
Who's the advisor?
**Tyler Yahn (Splunk)** 58:34 Sorry, I didn't… Catch who was talking on that one.
Yeah, okay, cool. I think we're at the end of the meeting here. Thanks, everyone, for joining. We will see you all in a week's time, or asynchronously. Until then. Alright, bye.
