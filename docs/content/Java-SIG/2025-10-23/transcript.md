SIG: Java SIG
Date: 2025-10-23
Duration: 62 minutes
============================================================

## Zoom Recording Transcript

Jay DeLuca 00:01:14 Hey, Marlia.
MG Marylia Gutierrez 00:01:17 Hello!
Trask Stalnaker 00:01:17 Hey.
Jay DeLuca 00:01:20 Hey, Jessica.
Trask Stalnaker 00:01:53 Oh, our meeting dock is starting to get slow. Might be time to roll that over again.
Alright…
Jason Plumb 00:02:12 It's only been a year! Like, it bottoms on September 2024.
Trask Stalnaker 00:02:18 Sounds about right. I think we've got 3 archives.
Feels like it's, like, a year… year and a half.
Jason Plumb 00:02:28 Well, 3 is now a pattern, so we have a yearly cadence.
Trask Stalnaker 00:02:35 Alright, Jay, time to write a GitHub action to roll us over every year.
Jay DeLuca 00:02:41 I'm on it.
Trask Stalnaker 00:02:58 Alright… So I've got a couple of… special attendees, so I bumped their topics to the front, make sure we get to them.
Marillia, Go for it.
MG Marylia Gutierrez 00:03:14 Sure. So yeah, for those who don't know me, I'm Aurelia. I… I am part of a couple of different SIGs, but one of them is the contributor experience that I'm a maintainer. So I don't know if you… any of you noticed, but sometimes when there are PRs from people, they're not contributors, you see a message saying, like.
Hey, I want to know how was your experience answering their survey? So, I keep tracking the answers on a weekly basis, and once I have enough, I go back to the respective 6, and just share the responses. So, yeah, I came here to share. There are not a lot of answers for both… here I'm combining both the, like, country instrumentation and things like that. So we got 7 from this one, and 5 out of 5, which is great. A lot of comments just saying, like.
It's good, it's great. Not a lot of detail, so people, in general, are very happy. Happy to help.
Trask Stalnaker 00:04:05 their PR merged.
MG Marylia Gutierrez 00:04:06 Yes, but then I see a comment that is happening more often, not only on this report, in several others, so this is why I came to bring it up, is there are, like, some confusion to after the approval. So a lot of people are saying, like, okay, my PR got approved, why it's not getting merged?
So, I think some of them is… some cases that I've seen others, I don't know if that is the case here, is that a code owner approved, but that does not mean that they can actually merge, so they still require a maintainer to… to actually do the merge, but that is not clear, for people, so people are getting confused, like, why it's taking so long?
To actually get my things merged.
So yeah, just wanted to bring that topic here.
Jack Berg 00:04:55 John, I think you're on mute, you're trying to talk, but…
John Watson 00:04:57 Yeah, there's another case where this would be delayed, and that is Jack and I are the only two maintainers on the core repo.
And Jack's been on paternity leave, and when there are API changes, we like to have both of us approve them before we move them forward, so things have been definitely delayed.
And there's also just cases in general in the core repo where… And I'm also just a volunteer, I'm not getting paid to do this, so, my time is very limited, so I think there's probably a bunch of cases where I approve things, and I was gonna wait until Jack was back from leave, or had a chance to look at them as well before. So there are definitely cases where we want more than one approver, and we probably don't document that anywhere, and make that clear, so I think that's a… it's a valid, possible point of confusion.
MG Marylia Gutierrez 00:05:48 Yeah. Also, I guess, in that case, something to consider, I see that not on the card, the other, they are more… maintainer's approver, so maybe… Another thing is trying to bring more maintainers to the core as well, so it's not depending on person, especially if one is out for vacation.
Trask Stalnaker 00:06:06 Better said than done.
John Watson 00:06:07 Yeah, he's using it.
Jack Berg 00:06:09 We've been soliciting additional contributors for, like, 2 years now.
Very active on it.
Trask Stalnaker 00:06:15 Even on the main README over here is a whole Help Wanted section.
John Watson 00:06:23 Yeah, and I think that this is actually, really, for you, it's probably some interesting information to have, is that I think a lot of people come in thinking that the way to move towards approver and maintainer Is writing code.
And that's not the thing we need.
We need people doing very deep, careful reviews.
of… of other people's PRs. We don't need more contributions. That's really not what we need. What we need is people actually doing reviews, and that's the thing that we're going to… we're going to favor when looking towards more adding a maintainer or adding more approvers, is people who are actively working on doing deep code reviews.
MG Marylia Gutierrez 00:07:03 Do you feel like there's confusion in that? Like, people just don't know what those status means? Because that is something that I can do a more, like, not specific for Java, but more broadly, not only, like, dating documentation, but maybe even, like, creating a blog post, like, hey, this is the path if you want to become… do you think those type of things will help?
John Watson 00:07:23 Yeah, I think this is actually a common misconception in open source, that people think what is needed is a lot of people writing code, and that's exactly the opposite of what is needed. Like, we have plenty of people writing code.
we need… we need deep, careful reviews, and that's… that's the… the… and that's the thing, it's not fun. That's not a fun job, which is why people don't jump into it and do it, but that's what open source needs more than anything, is that real careful… Thoughtful, deep reviews.
Jack Berg 00:07:52 Definitely the critical path, and I'd say that the… I'd also add that the contrib story is a little bit different than the core repo, so I think it matters, whether these, survey responses were for Contribut Core, because I… Contribber's a bit of an interesting story. It's like… You know, it's this repository of a bunch of independent artifacts with their own code owners, but the code owners don't have the permission to merge stuff directly.
And so, it's like, there's a few maintainers on it that are… probably stretched too thin, that are looking for, you know, an approval from the code owners, and, you know, I guess in that case, should just merge when that happens. But I think in practice, the maintainers, at least I feel like some obligation to understand the code that I'm merging, rather than just, like, merging it blindly.
You know, there's no trust?
Trask Stalnaker 00:08:46 have a… I don't think we have a bottleneck in Contrib, because I'm pretty, liberal.
Jack Berg 00:08:52 Zez-faire.
Trask Stalnaker 00:08:53 You know, I will scroll through, but I won't spend more than, like, 5 minutes.
MG Marylia Gutierrez 00:09:02 Yeah, just to confirm, I did check, and all…
Trask Stalnaker 00:09:05 Component owners. It's component owners.
MG Marylia Gutierrez 00:09:08 Yeah, those comments are coming from the Java instrumentation repo.
Trask Stalnaker 00:09:12 I thought so. Yeah, I was gonna ask, because, I know that we've actually had people, make those comments in our PRs themselves, like, when is this going to get merged? Yeah.
MG Marylia Gutierrez 00:09:25 So we do… we did add something recently to the JavaScript one, I don't know if it helps, because a lot of times we miss when it was actually approved by the code owner, so we do have now just, like, a script that adds, like, has owner Approval. So this way, the maintainers just have to check whenever this label is on, and we can just, like, merge and do things like that.
Lauri Tulmin 00:09:49 We don't have code owners here. We only have two maintainers.
MG Marylia Gutierrez 00:09:55 So that is something that we did specifically for this case. We created a different group that is just, like.
contribute, like, code owners, so they have permission to approve their things, but they don't have permission to merge anything. So, at least this is a way that really helps out the code owners parts, but I guess if there is no separation, it's just by the same.
Lauri Tulmin 00:10:16 We have approvers, but, but what we usually do is we add a release milestone.
And, if it requires a second review, then.
Jack Berg 00:10:30 Trust usually merges them right before the release.
MG Marylia Gutierrez 00:10:33 Oops.
Jack Berg 00:10:35 So the Contrib repository has code owners, and, you know, as Trask mentioned, he's pretty open about just merging them as soon as he sees an approval from a code owner. The instrumentation repository, which is where this feedback is coming for, as Lori's mentioning, just has two maintainers, and… has just an absolute mountain of code. And so there are approvers, but there's just two maintainers, and I guess I just wanted to clarify that, because I think we're getting some wires crossed with contribib versus instrumentation.
Lauri Tulmin 00:11:07 And, apparently the approvers don't want to become maintainers, so they aren't doing too many reviews.
Trask Stalnaker 00:11:16 For the instrumentation repo, one thought is, Because I think on those cases where we had the user feedback, I think there were two where they actually commented on the PR recently.
And I think both of those were that case where Lori reviewed it, approved it, added a milestone so that it would go into the next release, basically, and it was just kind of waiting for me to review it before the release.
MG Marylia Gutierrez 00:11:51 Hmm.
Trask Stalnaker 00:11:51 but we could do something where, when it's… I think people aren't… don't understand or don't notice that we tagged it with a release milestone and know what that means.
So we could have an automation where when we tag it with a release, we could add a comment that says.
You know, this has been added to the next release milestone.
to make.
MG Marylia Gutierrez 00:12:19 Yeah, because I don't think that is clear, yeah, yeah.
Trask Stalnaker 00:12:25 Yeah, and in cases where, like, even though it's not coming from the… or where we are waiting for Like, Jack, you know, to review some, you know, API thing.
I think, John, typically you do, like, mention that in the PR anyways, but it's just kind of a good… Practice for… in all the repos, like, if we are… if we do approve it, but are waiting for something else, just to say that to make it clear to the… expectation.
John Watson 00:13:01 Yeah. There's another possible gap, which I don't know how often it happens, and that is… a PR gets approved, but the build isn't done yet, and then whoever approved it it falls off their radar, and then it's not necessarily… like, when the build… when the build is done, it might not be… they might not… might not be top of mind anymore in Virgin. I don't know how often that ends up happening, but it is a possibility. If it's a small PR, but the build still takes a while to run.
Jason Plumb 00:13:30 Auto squash.
I mean, we have that set up in a number of repos, and it's super helpful for that exact use case.
John Watson 00:13:41 Yeah, but this is a case where, if it does happen to be an API change, we wouldn't want to do that.
Jason Plumb 00:13:46 Yeah, legit, yeah. Different story.
Trask Stalnaker 00:13:50 Well, it won't… it'll fail if the, It won't merge if the build fails. Right.
John Watson 00:13:56 No, no, no, I was just thinking, like, if there's an API change and I want… we want to maintain.
Trask Stalnaker 00:14:00 Oh, yeah.
John Watson 00:14:00 review it. We wouldn't want to auto-merge that.
Trask Stalnaker 00:14:04 Yeah, y'all don't have auto-merge enabled for the core repo.
John Watson 00:14:09 I don't think we do. I don't think we want it, either.
Trask Stalnaker 00:14:11 Okay.
John Watson 00:14:14 Unless we want to do, like, have something where two approvals from maintainers, but then that's gonna… I mean, I don't… I mean, if… I guess if two maintainers approve it, we could auto-merge it.
Lauri Tulmin 00:14:24 Oh, it's convenient, for example, when you have, like, a renovate pull request.
That you just approve before the build is done, and if the build passes, you want to merge it anyway.
Trask Stalnaker 00:14:38 Convenient, but it's your call.
Jack Shirazi 00:14:40 The, the feedback for that, the particular comment there is you should just have an automated message in the PR that says.
This needs two approvals, and then will be merged Before the next release.
After that. And that's it.
Lauri Tulmin 00:15:05 Well, we don't get, like, that many contributions, so this might be an overkill.
John Watson 00:15:11 Yeah, on the… on the core repo, yeah, I think it probably… it probably is. I don't think… I don't think this has been too much of an issue over there in the core repo.
Jack Berg 00:15:21 My thought a minute ago, and I think somebody was suggesting something to this effect, is just like, hey, let's get in the habit of, when we approve PRs, being overly communicative.
Right? Because, like, there's so much context. Like, a PR could be something that's, like, you know, lightweight, and we just don't have the time to click the merge button now, because we're waiting for something else to merge first, or it could require a second approval, or it could just, like, not be the right time for some other reason, and let's just… let's just articulate that whenever we're approving.
Trask Stalnaker 00:15:56 And probably don't need to do that on if we know the people making the PRs.
Jack Berg 00:16:01 Yeah.
Trask Stalnaker 00:16:02 But for, like, keeping that eye out for new contributors.
MG Marylia Gutierrez 00:16:08 Yeah, to be clear, like, all this feedback is focused on new contributors, precisely because we say they don't have, like, the tribal knowledge, so that is the issue that is happening with a lot of people. They just, like, don't know what is going on, so I think those are the ones that, if you really want to have new people contributing.
Those are the ones you had to focus on, making things easier for the onboarding.
John Watson 00:16:31 I think the other thing that I… especially for core repo… unsolicited… pull requests, is I really like those people to come here.
And… and just say hello and introduce themselves. And that's probably not something that's necessarily understood or expected, so that might be something that we could try to communicate better.
MG Marylia Gutierrez 00:16:55 So for this one, we tried to not push a little, like, the feedback that we got, because a lot of, sometimes, the feedback we got that English is not the first language of a lot of people, so they are okay with, like, writing codes, writing comments, but they don't feel comfortable, like, coming to a meeting and talking. So this is why we, like, say, if you are comfortable, you can join, like, just listen in, but we don't, like, force people to say hi and things like that.
John Watson 00:17:21 Yeah, I think for me, it's more of, like, in this era of supply chain attacks, and AI contributions and things like that. Like, I want to… I like to see people's faces, I'd like to see who… there's a human behind what's going on, and I know it's not necessarily guaranteed, but it certainly is helpful.
To kind of just close that loop and give a little bit more security.
Trask Stalnaker 00:17:50 Cool. Well, we should probably move on.
Thank you, Amelia.
Really cool to… See that feedback loop in place.
MG Marylia Gutierrez 00:18:00 Yeah, and to confirm, I am a real person.
Just… Tras me saw me live, so he can confirm. Yeah, sure.
Trask Stalnaker 00:18:08 Indeed.
Alright, Evo!
Ivo Anjo 00:18:15 Hello, I am a real person. Do you mind if I share my screen?
Trask Stalnaker 00:18:19 I would love for you to share your screen.
Ivo Anjo 00:18:21 Yes, cool. So, let me share stuff.
So, so… Thanks for the time, and I'll try to focus on the important details and be brief on the other things, so please ask me about anything if I went too fast.
So, a bit of context, I'm Evu, I work at Datadog, and I've been participating in the hotel profiling, SIG, so that's why I'm here, and a big part of the… oops, yes.
The big part, a big part of the output, that we, of the SIG so far is this thing, the OpenTelemetry eBPF Profiler.
that relies on the Linux eBPF built-in, like, VM thing to collect data from the profiler that… and does allows us to support a bunch of different runtimes, including Java.
And this gets me to why I'm here, is because of, context sharing. Specifically, Elastic was the one… so the folks in Elastic contributed the initial version of the OpenTelemetry eBPF profiler.
for OpenTelemetry, and they, also, like, had this blog post from some time ago.
Where they share about the problem of, okay, we have… we have traces, we have profiles, they are completely separate, but we would like to have a mechanism so we could match the profiles that happen during some kind of… some of the traces, so that we can kind of say, okay, this is the profiling data we got for this trace.
And, the… basically, this blog post describes how they did it, and, but this feature was relying on the, Elastics Hotel, like, distribution.
And we are now trying to kind of come up with the spec, which is the thing I linked in the meeting notes document.
Which is kind of us trying to, the level of the OpenTelemetry profiling, so he proposed a specification for how do we do this beyond just, like, the old implementation that Elastic had that actually, I think, was only for Java and Go, so we want to kind of create a spec for this and have this go in the multiple SDKs.
And, effectively, right now, what this allows is an application to kind of publish a bunch of, like, information, things like the deployment environment name, service instance ID, service name, etc.
for, like, a reader that's on the outside of the process, such as the EPPF profiler, to access this and be able to say, oh yeah, this was what this was the application I profiled, and what was going on inside the application when I looked at it.
And, we even have, like, a Java POC for the thing that we're proposing, which is this thing.
don't over-index on it too much. This is kind of just us trying to demonstrate, okay, we can implement this with the new foreign function and memory API in Java, and we can kind of build in, like, a full example where we publish this information, and we are able to read this information from the outside of the process.
with… 426 lines of Java code. That's… it's all in. And basically, yeah, I'm here to kind of ask feedback from this document, which is linked here.
And in general, the… the point of view is, like, we're going to try to standardize this at the hotel level, and want to, at some point, kind of come back to the Java SIG, and kind of say, here's a PR, here's us trying to actually implement this for real.
But at this point, we're more like, okay, is this completely mad? Are we missing something that is a completely bad idea for Java? Like, what can we improve here? And yeah, that's kind of it.
Jack Shirazi 00:22:11 Yeah, you're missing one thing, which is Java 8 support.
Ivo Anjo 00:22:16 So, that's a good point. So, I am aware that the FFM is only on newer Java versions.
So, for older versions, we have multiple options. For instance, we do have a C implementation or a C++ implementation, that actually we are using in DD Trace Java to support older Java versions, so we could go with, like, okay, there's, like, this native library that needs to provide this functionality for older Java versions.
Or… something. So basically, I think we can publish, like, an extra library that allows us to give compatibility for older Java versions, so that's why, yes, I think we can… we can have that solution for older customers that still want this feature set.
And, and even, like… oh, sorry, go ahead.
Jack Shirazi 00:23:07 Sorry, you're saying older, but basically every Java version out there is older than FFM.
Ivo Anjo 00:23:14 I know, I know, right, I'm not, I'm not, like, yes, I'm basically saying, I think we, it's not, the, the level of complexity of the C version is, like, around, like, 300-400 lines of code. I can link it here as well. So, I think, hopefully it will not be too painful to kind of say, maybe we ship, with the FFM version for the versions that allow it, and have, like, a fallback that people can add, on the, like.
Older versions.
But yes, I'm aware that, like, 99% of the world, or more than 99%, is not on a version that allows this yet.
Jack Berg 00:23:57 Okay, so this is, this is kind of new to me, so, can I ask some clarifying questions?
Ivo Anjo 00:24:03 Yes, please?
Jack Berg 00:24:04 So, alright, so the… we've got this language-agnostic profiling tool.
And the expectation is that maybe a user is, you know, running OpenTelemetry Java with the agent, or maybe just the SDK without the agent, and separately, they're running this profiling tool, and that profiling tool is producing, you know, the profiling OTLP payloads to a collector.
that ultimately go to a backend, and we want to make sure that, you know, this backend can correlate all the data that comes from the agent or SDK, the metrics, traces, and logs, with the profiling data that's coming from the profiling tool. And so, essentially, we need some way for the resource, which is, you know, a description of the telemetry-producing entity, to be identical.
for the profiling tool as it is for the agent. Is that about right?
Ivo Anjo 00:25:02 Yes.
Jack Berg 00:25:04 Okay, and there's some historical context. Jack, do you have context about how Elastic is doing this currently?
Jack Shirazi 00:25:12 I mean, we used a C implementation, where it says that it was standardized and it was shared memory.
And… the, the Java process just writes to the shared memory, and reads from the shared memory, and so does the eBBF profiler.
Jack Berg 00:25:29 So there's kind of coordination between the profiling tool and the Java process, they both are kind of aware of how this data is being written to shared memory, and they can kind of coordinate based on that, that information?
Jack Shirazi 00:25:42 Correct.
Just a quick, quick question, Eva. Do you actually need… is it just traces, or is it metrics and logs as well?
Jack Berg 00:25:52 Probably the resource, right?
Trask Stalnaker 00:25:55 This was just about… my understanding, this was just about resources at this point, but yeah, the trace correlation… I assume is a future step.
Ivo Anjo 00:26:07 Yes, exactly. So we, in the future, we also, yeah, get… want to know what's the current trace ID, what's the current span ID. We are working on that, but, I think the TLDR is that… While for, this, this kind of, like, the, the resource, the resource information here is something that, like, will… maybe we'll set up once when the app starts and never change, or maybe it will change.
a handful of times, so very rarely, and it's, like, for the whole app, like, it kind of makes it very easy to create something that a bunch of different runtimes can kind of standardize on. For the thing about, like, how do we access the current trace ID and the span ID, It will be something that, like, is changing all the time, it's, like, new spans are coming in, spans are coming out, so it's probably going to be a lot harder and look, like, slight, like, slightly too more different than this one, so that's why we kind of… I'm trying to say, okay, let's separate them out, let's keep one for the resource information, and then we are actively working on having, like, a reasonable proposal for the the trace and span one, and that actually might need to look different even for Java and other runtimes, because it must not impact performance, and that one will be a lot more performance sensitive.
Jack Berg 00:27:33 Yeah, so the entity group is trying to work on stuff that would allow the resource to be mutable. I mean, historically, it's been immutable, but I think that's… they're trying to change that and figure out a path forward on that, so the resource would potentially change over time. I'm wondering… how useful it would be to, like, have some sort of resource-sharing bit of code that, like, you know, doesn't work for the trace solution. You know, separating them is nice, because, you know, you solve the easy problem now, and you kind of punt on the harder problem, but if you solve the harder problem, then presumably whatever solution you come up with, the harder problem also works for the easier problem. So there's some… There's some merit to doing that.
Ivo Anjo 00:28:19 Yes and no, and I, maybe, like, it's possible that, like, we'll, that we might end there, end up there, but I suspect we won't, because in particular, like, all of the existing solutions, that we've, that have been looked at so far.
For this, usually rely on having, like, some kind of, like, a block of memory where we set up this information, and this block needs to be per thread.
And so, you probably want to have, like, as little as possible information in there, which is why, like, like, keeping… this one is the more, like, flexible one, you can add, like, a bunch of information, there's space to add, like, arbitrary key-value pairs.
Whereas, like, figuring out how to, to kind of put this information in the thread local one might be a bit… a bit more… a bit harder, and that's why, we kind of went in this direction. But yes, presumably, we could kind of say, okay, like, all of that information is set on the thread local 1, and we… Wouldn't need both.
Jack Berg 00:29:32 Jason, I think you were raising your hand.
Jason Plumb 00:29:33 Yeah, is there an assumption that there's a one-to-one mapping between operating system threads and JVM threads?
In this approach?
Ivo Anjo 00:29:43 Yes, those are all the questions that we are working on, like, looking into, and that's why we're kind of shying away on this version. And another kind of reason or thing why we ended up here is that, for instance, in the OpenTelemetry eBPF Profiler, right now there's already built-in support for the goroutine PROF labels.
Which are kind of like thread local, coroutine local variables that you can, that you can read. And so, for instance, for, actually the full end-to-end solution, you can now kind of already have it, with Go, we have it working at Datadog.
based on Elastic's earlier solution, where you basically get the trace ID, the span ID, from the application, as well as, like, the resource information, and it all works.
The problem is, for instance, that mechanism is specific for Go, so an application, the eBPF Profiler does have, like, support for, like, figuring out where that, where that information is for Go.
But we kind of found that the resource-level information is kind of useful for other things other than the profiler, and it's kind of annoying to… require everyone else to re-implement the code to read, like, the Go routine, like, thread local stuff, if all they want is to identify the resource, so that's kind of why we went in this direction of separating them as well.
Jason Plumb 00:31:07 Yeah, I mean, resource seems like table stakes to make that data useful.
Jack Berg 00:31:12 Yeah. So this is, like, interesting conversation about, you know, the trace context versus the resource context sharing, but I think it might be potentially, like, you know, you know, premature to have this conversation now. Ivo, you talked about how you want to work on a specification for how to do this, to kind of have a standard that is somewhat language agnostic about how this functions. And so, like, the way that that I don't know how much of this you're familiar with, so if you already know this, just forgive me, but so, you know, if you want to define a specification for something, you know, you write up the text for the specification, it seems like you have a design doc where you've gone into some stuff, that's good, but you also want to have a prototype. And so, like, how do you actually get this type of thing functioning in Java? It looked like you had a… a little kind of project that demonstrated how to do this, and how do you actually wire it in to do the real thing? Like, so, you know, if you're using the Java agent, there's an extension mechanism, and you can… when you start up an application with the Java agent, you can point to a particular Java agent extension.
and these agent extensions can get a callback to get a reference to the fully configured OpenTelemetry instance. And so, like, you know, one path forward to actually kind of build a working prototype of this with the Java agent would be to build an extension in the contrib module and publish it, and this extension, you know, could just get access to the, you know, the fully configured OpenTelemetry SDK instance, and use whatever mechanism you're kind of discussing at the specification level, and, you know, make that available in shared memory, or whatever mechanism you're doing it. And that's an essential part of writing a specification, because you've got to have a prototype.
You know, you could kind of demonstrate how it would work for us, and you could also use that as, As a reference for when you're proposing your specification.
Ivo Anjo 00:33:21 Yeah, that makes sense. I… We've already… we kind of done that for the Datadog library, so we have it there, it can be enabled.
in the latest version, and but yes, like, to your point, I think we've not done that yet with the Java SDK. I think part of me trying to come in here a bit earlier is that I'm trying to… we kind of have this loop where we've been discussing this with the profiling SIG, but the profiling SIG is not the SDK SIGs.
So, we're kind of, like, doing, like, a two-phase commit where I'm going to, like, trying to go to, like, oh, does this Does this look reasonable to you? Does this look reasonable to you? So that we can kind of start coalescing on, like, okay, this looks kind of reasonable, let's all try to implement this and make sure that it works.
And that's kind of the game I'm trying to play.
Jack Berg 00:34:11 Yeah, no, it makes sense, and I think, conceptually, there's a problem here that you've identified, and Elastic has identified as well, and it would be great to have some sort of specification around this, and common tooling around this. At least that's my opinion of this. I can't speak for everybody, but…
Ivo Anjo 00:34:27 Thank you.
Trask Stalnaker 00:34:28 Yeah, I think the current solution relies basically on when you're configuring the profiler, you have to feed it the same, like, resource attributes. I mean, that's the other option, right, is not to get it automatically from the SDK to require user intervention, but I think that it makes total… this makes a ton of sense to get it from the SDK and ensure that… At least you're correlating the resources.
Jack Berg 00:34:57 Because what we've never really formalized is what are the identifying attributes for resources right now. So, like, you know, if you're doing this via environment variable sharing or something like that, like, you know, you might have some of the resource attributes the same between the agent and the profiling tool, but not all of them. There's going to be some differences, because, you know, the agent has all these auto-detection mechanisms, so it's going to be hard to get them completely in sync.
Ivo Anjo 00:35:24 Yeah, that's the thing, like, we are also planning on, like, reading the environment variables in some cases, but yes, like, exactly, there's a bunch of things that the… it's done via code, and so it's… it's very hard for the profiler to know what happens to things done via code.
Trask Stalnaker 00:35:41 True, and we… we… generate service instance ID inside the SDK itself.
Ivo Anjo 00:35:48 The most important one.
Trask Stalnaker 00:35:49 Yes, yes, okay.
Ivo Anjo 00:35:50 this.
Trask Stalnaker 00:35:50 Yep.
I'm sold.
The only… I wanted to just confirm it, this solution would be limited to a single SDK per process, per JBM?
Ivo Anjo 00:36:05 Yes, that currently is the plan, that, like, this mechanism is kind of for global, but again, like.
This is one of those things where super useful feedback, let us know if this mechanism being global is a super bad idea.
Trask Stalnaker 00:36:20 I mean, for the Java agent, it's totally fine, and that's, you know, at least a majority of the Java users.
It would be nice if there was a path towards… for people who weren't global, but that then starts to get super complicated, like the trace correlation, where… to connect those things together, so I don't, I like the simplicity of this.
Solution.
Jack Berg 00:36:52 It's more than that, too, Trask. It's, like I said, the profiling tool, which, you know, is trying to build up these profiling objects and, like, introspecting on various things within the process. It's like, it needs to decide and, like, sort of classify which things are part of SDK1 versus SDK2 versus SDK3. How would it even do that? Like, that's all, like, programmatically determined.
Trask Stalnaker 00:37:15 I mean, it comes down to which SDK is active in the current thread.
Jack Berg 00:37:20 Oh, okay.
Trask Stalnaker 00:37:22 That the profile samples.
Jack Berg 00:37:25 I see.
Trask Stalnaker 00:37:26 Yeah.
Ivo Anjo 00:37:28 Okay, to be… one of… oh, go ahead.
John Watson 00:37:30 I was gonna say, I think in that case, it's the resource, is the thing. Like, each of the SDKs has their own resource, and the profiling tool would have access to the resource, and that would be the thing that would tie things together.
Jack Berg 00:37:41 Or some hash of the resource.
John Watson 00:37:43 Yeah, or some… yeah, yeah, exactly.
Yes, that's where the identifying bits of the resource are, yeah.
Ivo Anjo 00:37:51 Yeah.
Oh, I was just going to add that, like, we really want to make… to, get it so that, the… even the per thread thing has some, like, flexible space to grow in the future, so maybe in the future, if we wanted to go in that direction, we could, add more information in the thread local to allow the eBPF profiler to identify these things. And actually, the mechanism, the process level mechanism itself, as we're speccing it right now.
In a way, there's nothing stopping you from, publishing 10 different ones. The problem right now is that, like, if you publish 10 different for the same process, like.
which one should the profiler pick? So I think there is some space for growing in there, but definitely right now, we were kind of, like, hoping not to go there yet.
Trask Stalnaker 00:38:47 Cool!
Yeah, thanks for stopping by, Eva.
Ivo Anjo 00:38:52 Thank you!
Trask Stalnaker 00:38:55 Come back anytime.
Alright, Jay.
Jay DeLuca 00:39:02 Yeah, and I'll be quick, I know we've got a stacked agenda, but can I share my screen real quick?
Trask Stalnaker 00:39:06 Yeah.
Jay DeLuca 00:39:08 So I wasn't here last week, but I watched the recording and saw that you guys had talked about, configurations.
And wanted, kind of, a… single page where you could do, like, a Ctrl-F type search. So I just put together a very quick this isn't full because I haven't finished, mapping out all of the metadata, but, this does kind of just show, like, if you want to see which ones either have AWS in the… configuration name or apply to, like, an AWS instrumentation. I have this, like, search, so if you want to see, like, what instrumentations have, like, the known methods, you can come in and see that, along with them being on the individual pages. But why I bring this here is I also opened an issue, so… I don't know, the UI aspect of it is still kind of… iffy, and I don't know the best way to display this information, but I'll continue iterating on it, but I just wanted to bring that up. If people have ideas of ways to display it, or other things that they want included.
Let me know.
Jason Plumb 00:40:09 Was that built entirely for existing metadata?
Jay DeLuca 00:40:12 Yes, yeah, so it's from the instrumentation list. So as that continues to be built out, it'll be more populated.
Jason Plumb 00:40:19 And does that not include configuration items from the SDK?
Jay DeLuca 00:40:24 No, not yet. Yeah, that's.
Jason Plumb 00:40:27 I assumed that was true, I just wanted to verify, yeah, cool.
Jay DeLuca 00:40:30 Yeah, the contribib and the SDK are… are more… are on my radar. The SDK, I feel like, has some documentation in, like, the configuration repo now, but yeah, pulling it all together would be… would be good.
Jason Plumb 00:40:44 Yeah, cool.
Trask Stalnaker 00:40:49 I… so the… So, instrumentation ex- from the Explorer… I'm trying to think whether, like, having a static page in the website Or, like, how much we want in static pages on the website versus in the instrumentation Explorer.
From a discoverability… perspective, especially with the Java agent For Java Agent users, where… It's sort of like, here's all the bundled things, in the Java agent.
I mean, I… like, having it in the Instrumentation Explorer is great, and that's gonna be extensible for… more instrumentations and more languages, but specifically for the Java Agent Distro, this might be a case where it might be useful to generate that page from the metadata in the… as a static page in the website.
Jay DeLuca 00:42:05 Yeah, I could certainly do that, I guess it just comes down to how we would want to… display it. Because, like, we could have a standard table with, like, all the names, the descriptions, the types, the defaults.
But I think where it comes, or it gets a little wishy-washy, is just the part of, like, which instrumentations that each one applies to. And a lot of them are simple, like the ones that are one-to-one with an instrumentation, but, But yeah, we could also put, like, common ones or, like, cross instrumentation ones in a different folder. I'll take that, you know, I'll come up with something.
As, like, a starting point, we can discuss further and iterate on it, but… Yeah.
Jason Plumb 00:42:49 I wanted to specifically look at the, the use case that that issue was centered around, which was the application server JMX target systems, and… Like, I put JMX into that tool, and I don't see any results for configuration.
Jay DeLuca 00:43:05 Yeah, I haven't… I haven't doc… that one's also an outlier, it kind of is a different pattern, so I still need to think about how to… shoehorn that into the system, but yeah, I haven't… I haven't done the JMX instrumentation documentation yet, but it's on my radar.
Jason Plumb 00:43:19 Yeah, cool, okay.
Trask Stalnaker 00:43:23 For connecting it to the instrumentations, I'm… Almost not sure that's needed in that page, like, the description of the, the configuration option typically scopes it to what's expected, at least in the Java agent.
Jay DeLuca 00:43:42 Okay.
Trask Stalnaker 00:43:43 Maybe.
But yeah, play it well, like, it's hard to tell without seeing it.
Jay DeLuca 00:43:49 But yeah, I'll do an implementation, and we can take it from there.
Trask Stalnaker 00:43:52 Awesome.
I'm gonna skip over complex attributes.
Because I'm not super prepared for that discussion, and I will probably ramble, and I may just need to ping Jack.
Jason Plumb 00:44:12 I have a comment question on one of those trusts that has not been responded to, but it's fine, like… Do you really have to do right here?
Trask Stalnaker 00:44:18 Okay.
Jason Plumb 00:44:20 I'm just asking about the, the possibility for duplicates in this implementation.
It's like, performance style works… I mean, we're not… Yeah.
Trask Stalnaker 00:44:32 It still has map heuristics, Yeah, I mean, just…
Jason Plumb 00:44:36 We have to build, which we have to implement then, right?
Meaning no duplicates.
Trask Stalnaker 00:44:42 I mean, we can have duplicates, it's just when the… it's… when we serialize to Proto.
It has to… I guess, technically, even in Proto.
I don't know what… what do we say, Jack, in Proto?
Jason Plumb 00:45:01 You're muted.
Trask Stalnaker 00:45:02 you hear me out.
Jason Plumb 00:45:02 But it's no duplicates in Proto.
Jack Berg 00:45:04 That's right.
John Watson 00:45:06 Yeah, like, for example, our core attribute implementation right now Not for lists, but internally, while you're building it up, allows duplicates, and then just when we realize it, we dedupe. So, something like that could also probably happen.
Jack Berg 00:45:26 Yeah, like, what do you call that, an associative array? That's, like, the internal implementation is like an array, and it's just, like, a deduped array of key-value pairs.
Jason Plumb 00:45:35 And I don't think that's a deal-breaker or a huge hang-up, I just wanted to point that out as one implementation concern.
Interest, not concern, interest.
Trask Stalnaker 00:45:45 Yeah, I tried to, list pros and cons of the two approaches here.
So definitely take a look at that, and if you think of other pros and cons, let's update this.
I think I even called out…
Jason Plumb 00:46:02 Yeah, okay.
Trask Stalnaker 00:46:03 here.
Jason Plumb 00:46:06 Cool.
Trask Stalnaker 00:46:07 And, I mean, I kinda liked option A, but, you know, again, there's some pros and cons.
Ability, so we… We're going through a graduation process with the CNCF, And one of the pieces of feedback we got from the CNCF based on their adopter interviews Is that it's not always clear what's… what's stable or not, or what guarantee, like… And it's… I think part of the problem is that… well, there's a lot of… Things around that.
So, the… there's gonna be a discussion next Tuesday in the spec meeting about this, But I did want to share a couple of, Pieces from… oh, and it looks like… just one minute ago, Austin, Posted this, And this is, I think, what we're going to discuss Next week. But there's a couple things in here that… would affect… us, primarily the Java agent.
And so I just wanted to start… Gathering, getting feedback, and, this is not written in stone, Let's see, So… oh, I will share this, PR.
In the notes.
So that Fox can review it.
So… by default, stable components should not automatically include unstable components.
So a stable distribution of OpenTelemeter Java agent, Should not include alpha or experimental… Processors, samplers, exporters, you know, any of that stuff by default.
So, it's… not… Like, the… definitely… and then there's another piece about, semantic… wet, semantic conventions… And I think there's some carve-out of this, this idea of, like, beta semantic conventions. You could then declare an instrumentation as stable.
So what it could mean… oh, and then, like, having some global way for users to opt in to unstable things across all of OpenTelemetry.
So certainly we can continue to have unstable things in the Java agent, they just have to be behind, a flag.
And so some things we don't… like, I realized the, the rule… the rule-based route… routing sampler for health checks, which we pulled into the Java agent recently.
By default, that we didn't hide that behind a flag.
And so, there's potentially, you know, that is a… Unstable component. We haven't marked that component stable.
Jack Berg 00:50:14 Well, I mean, on that front, let's think about, like, the mechanics of actually using that. You have to set, like, OTEL experimental config file and specify, you know, a reference to that rule-based routing sampler in YAML, and so the name of the environment variable you set has experimental in it, so it's, like, it's kind of nuanced about how you actually get access to some of these things, and it's probably on a case-by-case basis.
Trask Stalnaker 00:50:39 Yeah, but as soon as declarative config is stable.
We're… that component is there, so yeah, good.
Good point, I hadn't thought about that in that particular case.
Jack Berg 00:50:54 So there's something in there that seemed, like, kind of contradictory. You're talking about how, like, you know, the default stable distributions of things, and I think the Java agent was mentioned specifically, shouldn't include, you know, experimental components, but then there should be, like, a global opt-in for experimental.
maybe I'm being, like, pedantic here, but does that kind of suggest that there should be a sort of, you know, stable distribution of the Java agent, which has nothing bundled into it, which is experimental, and then a separate, you know.
you know, kitchen sink version of the Java agent, which is what we published today, and… which has, you know, opt-in flags for those experimental things. Like, is that kind of what he's getting at?
Trask Stalnaker 00:51:37 That… yeah, that's a good point. That wasn't how I read it. I read it as… I put the words by default in here, in my brain.
Jack Berg 00:51:47 Should not include, maybe, like, not instantiate? Like… Yeah.
instantiate experimental components by default?
Trask Stalnaker 00:51:56 Yeah, should not enable.
Jack Shirazi 00:52:00 From a very different point of view.
our customers require… well, they care about two things, and stability is neither of them.
Trask Stalnaker 00:52:10 They won't…
Jack Shirazi 00:52:11 the… they want something to be GA, Because there's a subset of customers that will not put a beta into production.
And the other thing they want is support. They want it to be supported. They don't actually care about stability.
Jack Berg 00:52:28 These are just different words, like, that imply similar concepts. What I call G, what you might call stable.
Jack Shirazi 00:52:35 No, not at all. Because, for example, the collector has never been stable.
But we're supporting it.
Well, that's on this. And I know that it's gonna keep changing.
Jack Berg 00:52:46 that's on the support front, but, like, my… what I call GA, you might call stable, or vice versa, or they might have, like, overlapping concepts in there.
Jack Shirazi 00:52:56 But the Java agent is actually GA.
So that's.
Trask Stalnaker 00:53:00 It doesn't have an alpha tag on it.
That's the…
Jason Plumb 00:53:08 It's been generally available since the first version.
Trask Stalnaker 00:53:14 1.0, not the… all the… we had a lot.
Jason Plumb 00:53:18 0.0.1, that was available. What is GA… I mean, GA, people… that is such a dumb term.
Trask Stalnaker 00:53:24 means no dash beta dash RCE.
Jason Plumb 00:53:29 Yep.
Jack Berg 00:53:31 And what does that mean? No dash beta dash RC?
Jason Plumb 00:53:35 I mean, this is… this… this whole conversation is, like, very much, like, relevant.
to Android, because we're trying to release RC1.
Like, now, and this might throw a wrench in that.
I mean, I think it does actually throw a wrench in it.
John Watson 00:53:56 Does Android use dash alpha instrumentation to pull some of that in? Is that why?
Jason Plumb 00:54:02 Well, not yet, but the intention was, with RC1, to allow the agent to be designated as release, and the instrumentation to still be designated as alpha, following the pattern that was established.
In the job agent, and… This seems like it throws a wrench in that.
Trask Stalnaker 00:54:19 Which, is it just HTTP instrumentation?
Jason Plumb 00:54:22 No, it's all of it.
John Watson 00:54:25 What all goes into Android aside from HTTP, though?
Jason Plumb 00:54:30 for instrumentation.
John Watson 00:54:31 Yeah.
Jason Plumb 00:54:33 I mean, it's, it's startup stuff, it is crash reporting, it is…
John Watson 00:54:39 Right, right, so Android, some Android-specific stuff, rather.
Jason Plumb 00:54:43 Yeah, yeah, sorry, not sourced from upstream. Yeah, the only things we source from upstream here is HTTP.
John Watson 00:54:50 Got it, okay.
Jason Plumb 00:54:50 And disk buffering. And disk buffering from contribib.
Jack Berg 00:54:54 add resources into there, right? So, like, all resource detection is technically experimental, because nothing has been stabilized with that.
John Watson 00:55:02 But on Android, that's not going to be an issue.
Jack Berg 00:55:03 I know, I know.
Jason Plumb 00:55:04 It's different, though.
Jack Berg 00:55:05 Generally, no. Yeah.
I… so, stepping back, I… I think… I think… I like this. I would like it if there was… if, you know, by default, only stable things were turned on, and you had to explicitly opt into them so that users were more aware of what they were doing, I think there's, like, a number of problems with it. There's, like, the fact that it's a breaking change.
Right? So, you know, if you're using one version of the Java agent, and everything's on by default, and the next version you use, you have to add a flag to turn the experimental stuff on by default.
That's a breaking change. We have a mechanism for that. We have these major versions, so we can change the behavior in that. We also have, like, a communication problem, right? So, you know, somewhere, we need to, and maybe Jay's work can contribute to this, but we need to have a holistic list of all the instrumentations and their status, and how you enable them if they're not turned on by default.
And, you know, maybe related to this, and maybe there's already logging for this, but, like, you know, if I'm running the Java agent locally, I should be able to tell at a glance, either from logs or something, you know, which things, which instrumentations were candidates to be installed, and which ones were actually installed and enabled based on, you know, the preferences, the set of, like, you know, the things I enabled, or the things that are stable and enabled by default.
But, you know, what I do like about this is that it makes it much more obvious what's experimental versus stable for users, that's a good thing, and it also creates, like, an incentive for us to work faster towards stable instrumentation. When… when… We've lingered too much, too long, on these, you know, instrumentations and semantic conventions, which are, you know, kind of, like, effectively stable, but not actually marked stable, and that's kind of bit us, so…
Trask Stalnaker 00:57:09 the… biggest question that I have, for the Java agent is, that currently it's completely unusable. Like, we would have zero users of it, without the experimental flag.
Because literally none of the, instrumentations… are… well, I mean.
Jack Berg 00:57:32 What's stopping the HTTP ones from being stable?
Trask Stalnaker 00:57:36 Me.
Jack Berg 00:57:37 Okay.
Lauri Tulmin 00:57:39 Well, the thing is that, There are some core instrumentations inside the agent.
that… Need to be enabled for anything to work.
And even if the HTTP instrumentations are stable, if the core instrumentations are stable, nothing will work.
Jack Berg 00:58:01 What do you mean by core? Can you give me an example?
Lauri Tulmin 00:58:04 For example, the instrument class loader, load class method, to load our injected helper classes.
Jack Berg 00:58:11 Well, I think what they mean by, like, by these… you know, experimental versus stable instrumentation. So that's like an… that's an instrumentation in our minds, but, like, if it doesn't actually emit any data.
Any OT?
Lauri Tulmin 00:58:27 What about, like, for example, our executor's instrumentation?
Jack Berg 00:58:33 What are… what kind of data do those emit?
Lauri Tulmin 00:58:35 It doesn't emit any data, but it provides context propagation between threads.
Jack Berg 00:58:40 Right.
Lauri Tulmin 00:58:40 The problem is, it's kind of a weird instrumentation. It probably isn't the best approach that we are taking.
Jack Berg 00:58:48 Right.
Lauri Tulmin 00:58:49 Nobody would want to declare it stable, but it could be essential in keeping other instrumentations running.
Trask Stalnaker 00:58:56 I think we just have to declare it stable.
Live with major version bumps.
Lauri Tulmin 00:59:05 All of it seems like a ton of effort.
Like…
Trask Stalnaker 00:59:12 But there's…
Lauri Tulmin 00:59:12 We'll probably continue as we have been doing for now.
Trask Stalnaker 00:59:17 the executor's instrumentation, there's no… I mean, if… as long as we're talking Java agent, There's no public API.
Lauri Tulmin 00:59:25 True.
Trask Stalnaker 00:59:26 And so…
Jack Berg 00:59:28 There's no public API, and there's no data emitted. So, like, what do we lose by, like, marking it stable? Do we even have to answer that question, or do we just call that…
Lauri Tulmin 00:59:36 I think.
Jack Berg 00:59:36 internal tooling.
Lauri Tulmin 00:59:37 Because, like, if you do behavioral changes to it, then existing, like, the applications might break.
For example, like, we had this, idea of, like, instead of using virtual fields, wrapped around nobles.
But it has, like, a downside. It breaks, like, one use case when there is executor that uses a cluster task queue.
Which isn't arguably… it isn't common, but, still, like, some application could change if you want to, like… Oh, I don't know.
Maybe, maybe, yeah, it would make more sense to just, like, declare everything stable and, continue doing, doing, like, major version pumps every year, so we could, like, correct our mistakes.
Jack Berg 01:00:27 Are those internal instrumentations?
Trask Stalnaker 01:00:28 Thank you.
Jack Berg 01:00:29 Yes.
Trask Stalnaker 01:00:30 The question for me is the instrumentations that don't emit stable telemetry. Like, what is our… What is our guarantee on the telemetry stability front? So, are we going to be allowed to mark all the messaging… none of the messaging semantic conventions are stable yet?
Or RPC semantic conventions, so will we be allowed to mark those Java agent instrumentations as stable.
Jack Berg 01:01:00 Yeah, and it's like, you know, think about this, like, okay, we cut a new major version, and now you have to opt in to these experimental instrumentations, because, you know, the SEMCOM isn't ready to mark them stable, or whatever. And so, like, you know, great, we have, We've improved our story because… in some respects, because now it's more clear what's stable and it's unstable, but we've also hurt the majority of users, which were depending on things being turned on by default and not really caring about this.
Trask Stalnaker 01:01:32 We hit time, and this is a big topic. But, yeah. Ponder… ponder it, and let's, chat more next week about it.
John Watson 01:01:42 And comment on the… the… on Austin's PR.
Jack Berg 01:01:47 Yep.
Trask Stalnaker 01:01:49 VR.
Jack Berg 01:01:49 Yep.
Jay DeLuca 01:01:50 Yeah.
