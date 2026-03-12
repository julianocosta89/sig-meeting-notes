SIG: Java SIG
Date: 2025-10-30
Duration: 66 minutes
Zoom Recording URL: https://zoom.us/rec/share/y4ncdNO7UR021QN9mGt65O7GjFVWSWKQBS1y_Ng17_phnHeVLOBwpj0dcTrAowja.OM-hedERmLX_wt9m
============================================================

## Zoom Recording Transcript

Robert Niedziela 00:01:03 Hello?
jberg 00:02:14 Hi, everyone.
John Watson 00:02:21 Good morning.
Jay DeLuca 00:02:24 Hey, Jack. I think Trask said he won't be able to make it today, is that true?
jberg 00:02:28 Yep, that seems right, so I will… be the designated screen sharer today, I suppose.
Give me a second.
Alright, We'll give it another minute or so, then we'll get started. If you have any topics, please add them to the agenda.
Alright, we're at 3 after, so let's get started.
Who added these screenshots at the top? What's the context here?
Jay DeLuca 00:03:57 I did. I just… I started tracking, just as a time series, our open issues and open PRs, and after we added the, stale automation. We've cleaned things up a lot, and I just thought it was satisfying, so I included that.
jberg 00:04:11 Nice.
Anything else we want to talk about with respect to issue triaging?
By the way, so did this, the stale detection, did that get added to contribute instrumentation, but not core? Is that… is that the case? I think I saw some things floating around about that, but I obviously haven't been as gauged… as engaged as I'd like to be, so…
Jay DeLuca 00:04:40 I think it's replicated across all the repos now. I think we did core as well.
jberg 00:04:46 Okay. Is this, like, your own internal tracking, or, like, what's…
Jay DeLuca 00:04:51 Yeah, I have… I have, like, a GitHub action that runs every 10 minutes and generates metrics and sends them to my Grafana cloud. I track, like, build times, and then some other Random things.
jberg 00:05:04 Nice.
That's cool.
Okay.
If there's no other thoughts on that, let's move on.
Stack Overflow, we haven't checked this in a while.
The agenda seems light today, so maybe we take a look at that.
Oh, it's been a while, apparently, since I've… or a new machine.
Ugh.
JP Jason Plumb 00:05:32 Wait, is that a stair? It looks like a stair.
jberg 00:05:35 I don't know, man.
I can't even do a good job of answering these, because I'm not signed in. I'm the wrong person to do this.
New machine, still configuring it.
Let's see… Looks like there's two relatively new… issues that are from October.
Jay DeLuca 00:06:08 I think this person also showed up in Slack.
And I think they figured it out.
jberg 00:06:18 Let's see if we can, I find that in Slack, huh?
What was the person's name?
wallet?
There we go.
Jay DeLuca 00:06:35 Probably kidding.
jberg 00:06:43 If anybody's interested, we could just copy and paste this answer in, Let's see… I'm not gonna do it right now, because I'm not signed in, but if nobody else does it, I'll do it asynchronously.
And then, skywalking.
What's the question here?
So this doesn't really seem specific to this project.
They're just, apparently skywalking this vendor.
accepts OTLP data, and there's no sort of indication on what the problem is on the client side, but the data is just not missing, so… If anyone on this call is from… works for this vendor, that'd be great, if you could answer it, or else I think we'll just skip this one.
Lauri 00:07:49 Kaya walking is an Akbachi project.
jberg 00:07:54 Isn't there a managed version of it? What am I forget? What am I confusing that with?
Lauri 00:07:59 I think skywalking is mostly used in China, probably.
jberg 00:08:32 It linked to a GitHub issue, but.
Lauri 00:08:36 Since the session seems to be more about skywalking, I think we can ignore it.
jberg 00:08:43 I'm happy to do that.
All right, moving on. The next… the first issue, I guess, of the agenda is from myself. So, is Bruno on the call? Bruno normally joins, or sometimes joins?
Bruno 00:09:03 Hey, yeah, I'm here.
jberg 00:09:05 Bruno, I've got a PR to, sketch out what is necessary to make the sender APIs public.
And, you know, properly supported.
And so, I think you're the number one user of that.
And… when I was reviewing things, I found a lot of things that we ought to do before we make this part of our public API. Basically, if we were to make the APIs public as is.
a ton of other APIs just get dragged along with it, especially from the martialer packages.
And so, there's a bunch of simplifications and things that need to happen before this is ready to, be promoted, and… I think John Watson's on the call, right?
So, John, my thought with this is, like, hey, I have this as a draft PR, it's a big draft PR, I can break it down into smaller pieces, I know how to do that, but, I'd like all of the pieces to be.
John Watson 00:10:17 merged?
jberg 00:10:18 Like, sequentially, in one release cycle, because it's gonna be a lot of churn.
And so, you know, folks like Bruno, who actually have an implementation of this using the internal APIs today.
let's just put that aside for a second, but, like, you know, it would break Bruno a lot more if we did this over the course of, like, 3 or 4 releases, as opposed to one, and so I don't want to kind of start the work of breaking it into smaller pieces until, like, we're all on board about, like, what the changes are, and You know, the schedule.
John Watson 00:10:50 Yeah, I don't know how much time I'm gonna have to dig into a 1500-line PR.
Do you have… is… does this include the public API changes as just a… an overview? I haven't had a chance to look at this one at all.
jberg 00:11:05 Yeah, so this is, like, this is a draft of what the final result would look like, and so, like, we get JAPI, the diff, in terms of What would be promoted? So, it's compressor, and, you know, that's a little, extension point that we have that has been internal up to this point. That could be promoted as a separate thing.
And it's associated compressor provider, the SBI, for that.
And then, we need this, an abstraction, which I'm calling, a gRPC message writer, or a… HTTP message writer, but basically, so that we don't drag the entire martial layer package up into the public API, we need something that just has, like, a simpler interface that is responsible for writing to an output stream and, you know, has a pre-computed length.
And so, this is my answer for what that minimal API looks like. It's just like, you know, something that writes a message and, you know, knows its content length, and this allows us to hide Marshaller in internal And then… You know, the sender and sender providers themselves get promoted.
John Watson 00:12:19 Can I ask a quick question? Just… Yeah. Just looking at… so the… that sender writer… the API was a… It's like, write message that takes an output stream as a parameter. Is that writing to the output stream, or writing the contents of the output stream?
jberg 00:12:37 This is responsible for, one of these is passed to a sender.
when, you know, the sender is responsible for performing an export. And the sender, you know, obtains an output stream.
for its request body, and, you know, invokes this method write message, with the output stream corresponding to its request body. So, you know, by calling this, you're saying, hey, write the message to this output stream.
John Watson 00:13:09 How does it know what it's supposed to be writing?
jberg 00:13:12 The implementation of these, which is, like, provided by the internals, it's basically an abstraction over marshaller. So, like, the marshaller is going to, when you call writeMessage, that basically is, an abstraction that says, hey, marshaller, write all of your bytes to this output stream.
So we are… we, the internals, are the only people that are implementing these, like, this writeMessage, function.
John Watson 00:13:40 And it pulls data out of whatever its source of telemetry is.
And writes it to the output stream. So, basically, the basic idea?
jberg 00:13:50 Yeah, we have, like, a collection of metric data, or span data, or log data, and that has already been translated to a martialer, and we're writing the serialization of that to the output.
John Watson 00:14:00 Okay, so there's some… there's a, like, some inherent state assumed by the user of the message writer. So rather than having… having something that passes the data to the message writer, the implementation's responsible for holding on to that, or knowing what it needs to write at the right time.
jberg 00:14:18 Yeah, and this avoids us having… this allows us to write the messages incrementally, rather than, you know, writing all of them to a big byte array in memory, and then having to, you know, just copy that to the output stream, so… we have… none of this implementation detail actually changes. It's all about minimizing the API surface area.
John Watson 00:14:42 Cool.
Yeah, so I think if, Bruno, if you can take a look and see if this feels like it's going to be something usable for you, that's kind of the most important thing, is the primary consumer of those new APIs.
Bruno 00:14:57 I guess I'll have to… to check out the PR.
build the SDK and see what happens.
jberg 00:15:06 Yeah, from a working branch, so that's a little bit annoying, but… So, there's one other thing that, I guess I wanted to call out. So, previously, or currently, senders are responsible for doing this thing, which is, like, one of the parameters is, whether or not… whether they should serialize to JSON… the protobuf JSON representation, or the protobuf binary representation, and that's just… That's something that a sender shouldn't have to worry about. Like, senders shouldn't have to know about, like, what the bytes are. They should just be writing bytes to, an output stream, and, like, all the details about what those bytes are are abstracted away from them. And so, that's something we have here, Bruno. So, if you look at, like, the config options that are being passed to one of your… one of these senders when it's initialized.
It's… these have changed and become more narrow. There's, you know, you no longer have to be concerned with whether you're exporting protobuf JSON, or just binary, amongst other things, but that's a… that's a good example.
Bruno 00:16:17 Correct.
So… Yeah, so this, this configuration… So those, structured objects below, so SSL content and… The trust manager.
Okay, I'll have to find a way to set that in there.
But.
jberg 00:16:43 Those are there today.
Bruno 00:16:45 Okay.
Yeah, but I'm not… I don't think I'm using this.
jberg 00:16:52 It's possible you're ignoring them, yeah.
Bruno 00:16:54 Yeah, yeah.
And also the executor's service, yeah.
So this is for the retry, I imagine.
jberg 00:17:06 It's not just for retry, it can, it depends on the, the, like, how the implementation works. Like, OKHTTP has a, has background threads that actually do the work. It's a… it's kind of like an asynchronous, client, and so, you know.
rather than letting OKHTTP spin up its own thread pools to execute, you know, by setting the executor service, you're saying, hey, when we're… okay HTTP, when you're gonna do your asynchronous work, do it on this thread pool.
And that's important for certain implementations that… or certain users that really care about thread pool management. I think, JetBrains in Intelliga was one of the people that really wanted to closely manage their threads.
They didn't want us to go creating thread pools on their behalf, and this kind of facilitates that.
Bruno 00:18:03 Yeah, I think I will need to use this as well.
jberg 00:18:08 Yeah.
Bruno 00:18:09 Yep.
jberg 00:18:11 Okay.
Bruno 00:18:12 Okay.
jberg 00:18:15 So it's a decent amount of work, and I'd love a review from you, but at least we have a framework to get forward to a public API, so it might take a little bit more time, Bruno, but we're getting there.
Bruno 00:18:28 Yeah, I don't promise you that I will be able to go very deep on this on the next two weeks.
But, it's certainly one of my priorities, okay?
jberg 00:18:39 Yeah, no rush. I'm not in a rush to do this. I was making this happen for… For you.
Bruno 00:18:48 Yeah, and thanks very much for this. It's out of code.
jberg 00:18:53 No problem.
Alright, if there's no other conversations on that, let's, let's move on.
Jay, you want to talk about extensions?
Jay DeLuca 00:19:04 Yeah, so, we don't need to go too deep in this meeting necessarily, but I… there have been a couple issues and discussions in Slack threads, with people having some questions about extensions and how to find documentation, and I think that we have… we have pretty good, documentation within the Java agent.
codebase in the example, but I was kind of… pushing some of this to the OpenTelemetry site. So, a couple asks is, one, I don't have first-hand experience with extensions. This was, like, a learning experience for me. I played around with the extensions a lot and created a test project and all that, so… people who have more exposure, I would definitely appreciate a look over, make sure I didn't miss anything, or anything like that. And then second, it's really big, so I'm… Interested in, kind of, the initial reactions around whether we should include all this stuff or strip it down, and then if we do want to include it.
I know that there's been several ways that we've embedded code snippets into documentation. I know, Jack, I think you did a lot with the SDK stuff in particular. Curious about your experience with that, whether you think that that's the way to go, and But yeah, just looking for gut reactions initially, and if also, because the PR is so big, if… we would prefer that we do it in chunks, like, I can do sections at a time, I could also do that, but…
jberg 00:20:35 That's where I was navigating to right now, is an example of one of these code snippets. So the way these work, Jay, and I'm a big fan of them, so, I would highly recommend we use these liberally, is, so we have… you know, if you want to reference a code snippet in Opentelemetry.io, you use a syntax that looks something like this. So, you know, here we're saying, like, what specific file we want to reference.
there was talks about the maintainers, with the maintainers of OpenTelemetry.io, about being able to specify specific lines from within a file, but that was punted on for future work. So that's, like, one of the downsides of this, is, like, you need your files to be somewhat focused, or else I think you drag in a bunch of things that aren't related to the concept you're trying to talk about.
But assuming you have a focused file, you know, you reference it like this, and there's some metadata at the top of this file that says, like, hey, which project or repository are we gonna even source this project, this file from? And, but, you know, basically we say, source it from OpenTelemetry Java examples.
And then, like, you know, the specific file in here is resourceconfig, that's the one we're referencing in this example. And this content gets pulled in, and it's, It gets pulled in as part of the, there's, like, a build step that you run, and so, like, you have to… you know.
update Opentelemetry.io's, you know, git ref to the specific version of OpenTelemetry Java examples, then run this build step that pulls in the contents of the files that you're referencing at that ref.
And then, you know, you check them into source code, over here. And, you know, it's an error if these things are out of date, essentially.
Okay.
Jay DeLuca 00:22:33 Cool, yeah, I'll definitely… because Gregor and I were talking about it, and I think it makes sense to have everything in… And examples, whether it's the main repo or the examples repo, so… That's good feedback.
jberg 00:22:48 So what were you thinking about, like, synchronization? So, the… this content, I think a lot of it either comes directly from Java instrumentation, or is, like, a… like, maybe a, you know, your own edited version of the content that's in there.
Do you… are you foreseeing, like, making this the source of truth for this information and scrapping it from OpenTelemetry Java instrumentation, or what?
Jay DeLuca 00:23:17 I was not thinking that. I was thinking that the… the other codebase would be the source of truth.
Because that's where we… I think that's where most people know to look, so… .
jberg 00:23:34 So, two copies of it?
And where do we talk about that? It's in, like.
Jay DeLuca 00:23:39 spot.
No, it's in the examples.
And then if… yeah, there's a… yeah, right there. And then there's a extension right here.
jberg 00:23:51 Yeah.
Jay DeLuca 00:24:01 And, like, there's also the approach of, like, I… Was very verbose with a lot of the examples, and calling out the extension points and all that, and maybe that's… not needed. Like, maybe we just focus on the high-level concepts.
on the OpenTelemetry docs site, and then just expect people to… Come here and reference more… technical deep dive.
jberg 00:24:28 Well, I'll let Lori and Trask and the maintainers of Java Instrumentation weigh in on this. I know Trask isn't here today, but Lori is. So, personally, I don't like having two sources of truth for the same information. And, you know, we… on the… in the core repo, basically promoted all of our docs for the source of truth to live in Opentelemetry.io. That's kind of frustrating in some respects, but at least there's only one place where the information is defined.
I'm not sure how to juggle that with instrumentation.
Because it definitely is nice to have this information here in the examples directory, you know.
Jay DeLuca 00:25:10 Yeah. Alongside the working code.
I don't think that there's… enough here to feel like it's, like, a ton of duplicated, like, the… a lot of the documentation in this codebase is, like, inlined, like, in the examples, or in the Gradle file, and then this overview here.
So, it doesn't feel too gross to me to have the two, And I guess I wasn't… it didn't feel like this API will change a whole lot, but… I don't have a great sense for that, in terms of, like, how often we would need to update things in both places.
jberg 00:25:48 Yeah.
Any other comments on this?
Lauri 00:25:58 And you also use environment variables to specify extensions?
jberg 00:26:06 You can.
Jay DeLuca 00:26:08 Oh yeah, I guess I didn't… You mean using this Java agent extension system property, but just as an environment variable?
Lauri 00:26:20 Yes.
Would that work?
jberg 00:26:24 Pretty sure it does, I'm pretty sure I've tried that.
Jay DeLuca 00:26:28 I'll, I can do a test, and then update this accordingly with both approaches.
Laura, do you have any gut instinct around… Like, the verbosity of this… If you want to take some time to digest it and come up with an opinion, that's fine too, but…
Lauri 00:26:53 Yeah, I think I need to read through it, but… I'm pretty sure it's fine.
Jay DeLuca 00:26:58 Okay.
jberg 00:27:01 Alright, well, thanks, Jay.
Jay DeLuca 00:27:04 Yeah, no problem. Thanks for the input, guys.
jberg 00:27:09 Hi, Vo. Welcome back.
Ivo Anjo 00:27:11 Hey, do you mind if I share my screen again?
jberg 00:27:14 Go for it.
Ivo Anjo 00:27:16 Okay, so, speaking of extensions, I think it's, like, I got, like, a really good, like, intro, because, And… is it this… is this the window?
This is window.
I've been playing with it, so last week, I was here talking about this document, which, from the profiling SIG, we want to… have this way of having, being able to communicate some, attributes from the hotel SDKs to the eBPF profiler, and we have, like, this whole mechanism we're proposing for it.
And there was a very good suggestion to try it out using the extension mechanism and see how that works.
And actually, I, got that working. So, I… exactly the… I took the extension docs we were already looking at, and I basically added, like, a very simple extension, and so… I was able to get, like, an application that uses the hotel Java SDK to, when I run it, it's, I can then use, like, a very simple bash script that prints kind of this information, and this is kind of the idea, is that, the hotel profiler can kind of see, oh yeah, this is the service instance ID, this is the… service name, etc, from kind of outside the application. This is just a bash script, and I can show how… Well, if you know the extension mechanism, and we were just talking about it, it's kind of quite simple. I just create an auto-configuration customizer that gathers the information that we need.
And then there's, this implementation. It's still, like, the same implementation I was using last week, so it uses FFM, so it requires modern Java versions. For older Java versions, we'd probably have, like, an alternative version of this extension that, possibly uses a native extension instead of FFM to solve this, but it's… It's kind of, like, weird-looking code, but it's, 300 lines of weird-looking code, so it's not very bad. And this includes, like, encoding of the payloads into, like, protobuf.
without using protobuf as a dependency, just kind of, like, has a very minimal 100-line protobuf encoder. And yeah, the bash script I was… I was looking at, it's… I was showing it's kind of very simple as well. It kind of just reads stuff and uses the protobuf tool to print, protobuf stuff.
So yeah, kind of just showing, and I am also preparing now, an OpenTelemetry extension proposal to send to the hotel specification SIG, and hopefully, we'll start the process of getting more feedback from this and standardizing it, so if you have any feedback, if you want to play with it, yeah, please look at it and come talk to me.
JP Jason Plumb 00:30:08 I think this is awesome, I have a couple of questions.
In the, so the script is essentially mimicking the behavior that we would expect to happen in the eBPF function, right?
So it's like, it's like the… the eBPF profiler is taking, samples periodically, or somehow, like, taking samples, and it needs to know what the context is at the moment it's taking a sample, right? And the script is sort of short-circuiting or pretending to be eBPF, right?
Do I have that correct?
Ivo Anjo 00:30:40 it's… It doesn't need… so this part.
JP Jason Plumb 00:30:43 It's just for demos. It's just for demoing, right?
Ivo Anjo 00:30:46 Yes, this part actually doesn't need a eBPF, and even the OTAL profiler doesn't use eBPF for this part, but yes.
JP Jason Plumb 00:30:55 Okay, that's cool. So… the… is… I guess what I'm… what I'm thinking about, what I need to ask, I should just say it concisely. Is there coordination between the writing of the memory and the reading of the memory?
And does that need to be coordinated? If the right is not atomic, does there need to be coordination?
Ivo Anjo 00:31:19 So, this is a really good question. So, right now, like… the way that the protocol is kind of set, it kind of creates this coordination, because the memory that we get from the kernel, it's already zeroed out, and there is, like, a specific order in that we write the fields, and then we kind of make that memory read-only, it's, like, the final step, so a reader can kind of look at it and see, okay, are all the fields non-zero? Is the memory read-only? If all the fields are non-zero and the memory is not read-only, then we know that, like, we observed the full final version of the spec. So that's how we ensure that we observe, like, a consistent version, not an in-between version.
JP Jason Plumb 00:32:05 Okay, I like that answer, I think. I don't have my head around it fully, but I like it, thank you.
Ivo Anjo 00:32:10 And actually, as an extra cool thing that doesn't affect Java, because Java doesn't use the fork API to create, like, more Java VMs, just to start external processes.
But we actually… one of the things we also do is we mark the memory as not inheritable by children, which means that you don't accidentally end up kind of carrying this if you start more processes from a process, like… they… yeah, basically there's a flag in the Linux kernel that says, like, don't carry this over, don't inherit this, so we… that's another check that makes sure that we don't… Carry around stale information in some certain situations.
JP Jason Plumb 00:32:51 Cool.
Jack Shirazi 00:32:52 Have you looked, at, supporting memory map files to use this? Because that would make it much more widely… available from… Everything else.
Ivo Anjo 00:33:07 There's a few trade-offs. So, there is, like, I have looked at… we have looked at it, we actually have, like, a similar-ish thing in Datadog that uses memory mapping for files. We kind of, So, for instance, like, this case of, like, when a process creates children is one of the challenges we have in that, and we kind of have had a few challenges, so… in between, we kind of said, pros and cons, we prefer to try to push this one, but I will include… I'm actually preparing the OTEP specification proposal, and I include that, and the reasons why we said We prefer this one as one of the explicitly, kind of rejected possibilities, so, yes, we will kind of include that in the list and explain, why.
jberg 00:34:09 If… If this does get accepted by the specification, if your OTEP gets accepted and, And there's, like, a route to stability, ultimately. I'm thinking about where this should live. So, right now, you've modeled this as an agent extension, that's cool. Agent extension gives you a callback where you can access the auto-configured OpenTelemetry SDK.
And you extract these bits of information from it and expose it to the shared memory location, that's cool.
But, in terms of scope of where stuff lives, so we have 3 repositories, OpenTelemetry Java, OpenTelemetry Java Contrib, OpenTelemetry Java Instrumentation.
what's the right home for this? And the scope for the core repository, OpenTelemetry Java, we say is, like, anything can be in there that, that is, you know, part of the spec. That's… that's our scope.
And so, you know, if you are successful with your OTAP, it would make sense, I think, to have this live in the core repository. And then the question is, like.
okay, how do you actually use this thing? Like, how do you indicate, when you're building up an OpenTelemetry SDK, that it should make its information exposed in some sort of shared memory? Like, you know, because you can use the SDK in a standalone capacity, and then it's, like, automatically installed for you when you use the Java agent, so, Yeah, I'm just trying to think through what that mechanism would look like.
wondering if John has any thoughts on that.
John Watson 00:35:52 Yeah, so I agree with what you're saying, that it… if it's spec'd, it should… this is something that should probably be built into the SDK itself.
And… I mean, I guess we would probably just have configuration that would enable it, right? And turn it on… turn on the option to write this information when we read the… when we do the resource processing, or whatever additional thing we have to do. I don't know, we're still just talking about resources at this point, right? We're not… we're not moving on yet to spans.
Ivo Anjo 00:36:22 No, not spent yet, although I want to get there, but not in this spec. We'll create a separate one to that.
John Watson 00:36:28 So it seems like it's just, like, some configuration that would, at, SDK construction time.
would then, as soon as the resource is read. And resources are still immutable, though that's gonna change, right, soon. And that's gonna make everything a lot more complicated, and I think, actually, to Jason's question about… If the resource changes and we have to rewrite that information, we would be going from a state of all non-zero to another all-non-zero state. And so we might… if resources are mutable, we might have to have an intermediate state where we zero everything out before writing the new one. Just something to think about.
Ivo Anjo 00:37:09 The spec kind of mentions that, so the idea is that you just drop the current one and create a new one, instead of mutating, so…
John Watson 00:37:18 Yeah, but they, like, the reader… the reader-writer coordination, like Jason, that Jason was asking about, like, we would have to make sure, atomically, like, the… the… the read… Like, how would… how would the reader know that it needed to update itself, I guess, is another question.
Ivo Anjo 00:37:36 Yeah, there's… there's kind of two ways. The… so the, the reader can do the, the classic, read the, read the data, and then kind of read again to see if kind of read, like, a consistent view.
There's also, like, a timestamp on when the context got created, so you can use that to realize, like, okay, has it changed?
And finally, and this is where EZBPF comes in, it's actually possible to hook on, one of the steps that we are, that, on when the context gets published.
So, if the reader, if the reader can… is using eBPF and can hook on a Linux kernel, can… can use that as an event source for, like, oh, this application just published the data, so… and already published is kind of the same. So, there's a few… There's kind of an option the reader can choose to pull, or can use that as an event source for… to know when that thing got published.
JP Jason Plumb 00:38:39 Does the approach with FFM, is that completely portable? Like, will that work on Windows, even if there isn't, like, the eBPF compatible? I mean, I know the eBPF on Windows is… like, kind of a thing, but I'm not necessarily, like, asking if they're compatible, but is the FFM side of it compatible with… Windows and other platforms. Should be, right?
Ivo Anjo 00:39:00 No. Like, this is, like, Linux-specific for now.
JP Jason Plumb 00:39:04 Okay.
Ivo Anjo 00:39:05 it's… we could maybe, maybe find out, like, something similar for the others, but right now this is, like, Linux-specific, not because of the FFM usage, but because of some of the API calls and the things we're doing. I think even on macOS, we'd need to do a few changes, because.
JP Jason Plumb 00:39:20 Okay.
Ivo Anjo 00:39:21 I'm sure we get all of those flags and things.
JP Jason Plumb 00:39:23 Cool.
Jack Shirazi 00:39:24 So just… just for the OpenTelemetry Java discussion.
This is less for you, and more for Jack and John.
if… if… they're including this in OpenCleverage Java.
the only way it works is if you include a CLIB as well, because… That's the only thing that's going to be Java 8+. So are you going to be distributing a CLIB with… the SDK. I don't quite understand how that's going to work.
jberg 00:39:55 I think this has to be modeled as some sort of separate component.
For a couple of reasons. One, we don't want to bundle all this stuff together and force people who are just, like, taking a dependency on the SDK to automatically, you know, include this CLIB and other things that are… might be included in here. And then the other reason is, you know, if you think about how we model our OpenTelemetry SDK object, and then, you know, we have these It's a composite of SDK Tracer Provider, SDK meter provider, SDK logger provider, and each of those can technically have separate resources associated with them.
And that's kind of weird, that the resource isn't, like, a top-level thing associated with the SDK. It's like.
it's associated with these child providers. And so, like, I think naturally, where you'd want to model this as is, like, in the auto-configuration module, there's this thing called a, like.
It's like a… callback, an initialization callback or something, where, you know, you get access to the OpenTelemetry SDK instance that's been configured, not the individual providers, and you could build an extension module, like, with its own artifact, that implemented this you know, this… this callback that I'm talking about. And, you know, essentially, you would get this behavior if you included this special artifact that we would start publishing on your class path.
Then, you know, this callback would be detected as an SPI implementation, it would be automatically invoked, and everything would just work.
And I guess then the question would be, like.
Should the agent include that by default or not?
Right? Because the agent has to make decisions about which artifacts to include or not include by default. Like, should… should you just be able to flip a switch, a system property, and get this when you're using the agent, or do you have to include, like, an agent extension jar in order to turn this thing on and also flip a… flip a switch?
John Watson 00:42:00 All good questions.
jberg 00:42:02 Yeah, and I think we can work these things out. Jack, I think that the important thing is that we don't want to include a CLIB or other dependencies for all these users who are not interested in this thing, so we'll definitely take precautions there.
John Watson 00:42:18 Yeah, I think… I agree. It should be a separate component that gets pulled in separately.
No matter what.
I mean, it's not going to work for all versions of Java on all platforms anyway, so you're going to want to pull it in selectively.
jberg 00:42:33 Yeah, as Ivo was talking about, it doesn't even have Mac support, like, you know, now I'm worried about how we actually test this thing, and, like, and how we build it locally. You know, I might have to, you know.
remote into my Linux machine over there just to write the code for this thing and maintain it, so that's… that's kind of annoying, but… We'll work through these things.
John Watson 00:42:56 Yeah, and that's a good maintenance. Maintenance will definitely… require… the maintainer developer to have access to the Linux machine to work on.
So that is… that is, something to… something to at least consider, think about.
Ivo Anjo 00:43:20 just going to say that, like, yeah, one of… that's one of the reasons why we have, like, some of the, like, bash scripts and whatever, is that, like, hopefully have it easier in CI or something, where… And the testing we've been doing is mostly, like, end-to-end, so we have just the Java portion of the code, write it, and then, like, use something else to read it and report it back.
For unit tests, yeah.
jberg 00:43:49 Yeah, well, I wish you the best of luck, with the specification. If you want… when you're opening specification, PRs, and an OTEP doesn't have this requirement, but, like, you know, once… if the OTEP lands, and you have to go and actually codify this thing in the actual spec.
You know, you'll… you'll need a prototype, and I know you have a prototype, but, like, feel free to, you know, work with us and figure out how to land an initial version of that in the core repo. We can figure out where to put it, how to package it up, things like that. So…
Ivo Anjo 00:44:23 Thanks a lot. Thank you.
jberg 00:44:25 Thanks, Avo.
Alright, next topic. Sylvain.
Sylvain Juge (Elastic) 00:44:31 Yes, so the next topic is mine. So while working on JMX metrics, We discussed, a while ago, to, like, there is no, specification, in semantic convention about, what we call state metrics.
And so, there are basically… Two minor changes that are name-related were, in the example, we promote using the semantic conventions, so using state as a suffix in the attribute name.
As you can see in the example a bit below on Tomcat.
and using status as suffix in a metric name. So, those conventions are only, like, in the YAML file, so it's not, like, changing anything.
And, the only breaking change is, previously, we were using, like, empty, unit.
as a way to indicate, lack of units. In semantic convention, everything is using 1 as, lack of units.
And so, this introduced a breaking change, and I looked a bit at it, and if we introduce, like, a configuration option.
it will likely require to implement the same in, JMX scraper in country repository, so I wonder if maybe adding one more, breaking change, as we did, recently, would be maybe the best option, instead of, keeping, like, the breaking change for 3.0.
JP Jason Plumb 00:46:05 So while we were talking about this, I approved it. I think it's a good idea to align with the correct part of the spec.
I think it's a good change.
jberg 00:46:17 I don't have context on the last breaking change that you're talking about.
And whether this is sort of aligned with that and has similar reasoning, but.
Sylvain Juge (Elastic) 00:46:28 So, like, over the last, more than 6 months, I worked mostly with Robert on, JMX metrics, and, most of the times, sometimes, like, for example, we change the unit and the name of the metrics, so there already has been a lot of breaking change around JMX metrics, and… Which means changing the unit…
JP Jason Plumb 00:46:50 It's always possible that someone somewhere is depending on that empty unit, but it seems unlikely to me.
Sylvain Juge (Elastic) 00:46:56 Yes. What I wrote in the comment is it's likely to be, like, breaking some mapping, but they are very unlikely to make any use of this empty string by default.
JP Jason Plumb 00:47:07 Yep.
jberg 00:47:12 Well, it seems reasonable to me, but I don't have all the context, so…
JP Jason Plumb 00:47:17 Robert, what do you think? Seems good, right?
He said very leadingly.
Robert Niedziela 00:47:21 Yeah, basically, we did a lot of braking changes already, as Sylvan mentioned, so one more shouldn't be that painful.
JP Jason Plumb 00:47:33 Cool.
jberg 00:47:40 Alright.
Sylvan, or Robert, do you want to go and approve this?
To indicate your support?
Robert Niedziela 00:47:49 Yeah, yeah, sure.
Sylvain Juge (Elastic) 00:47:51 Thanks.
jberg 00:47:57 Any other comments?
Alright, moving on, last topic. We don't have that long for this, Jason.
JP Jason Plumb 00:48:08 That's fine, I figured… figured we wouldn't. It got smushed in at the end of last week's as well, I believe, so… This is the blog post that's being worked on by Austin to… Declare some amount of… Organizational… support for stable components. There's some wording in there that's, like, a stable agent would only include stable components and stable instrumentation by default, which is not something we currently do, and I'm wondering if there's been any further discussion, progress, thoughts about How we, especially in the agent, are going to handle this.
What I heard on Tuesday… from Daniel in the Android SIG is that largely, the expectation is that users will need to opt in to using Exper… like, if you want every… if you want the kitchen sink like you get today, well… Okay, there are some instruments which are not enabled by default, but I will say kitchen sink because we get most things turned on by default.
If you want that, you're going to have to opt into that, is what I think the… the short story.
But I'm curious if there's been any other discussion that I have not been aware of around this, and how we plan on handling it.
jberg 00:49:32 Did you attend the Tuesday Spec Seg?
JP Jason Plumb 00:49:35 No, because I think it conflicts with Android, I think.
jberg 00:49:39 Okay. Well, I'll try to articulate something that was talked about there. Okay.
And…
JP Jason Plumb 00:49:46 Or you just told me to shut up and go watch the recording, I mean, that's also fair.
jberg 00:49:49 No, it's good for everybody, I think, to hear and solicit some feedback. So, suppose we have some instrumentation module called Foo, and, you know, Foo has a property that enables it or disables it, and it's experimental right now, so by default, it is not enabled.
Right?
And, and later, Later, we promote this foo instrumentation to be stable, and so we want to say something like, oh, the default is now true.
And, this is a problem.
for… declarative config, just like in probably any configuration system, you know, changing the default behavior of a property should probably be considered a breaking change. So, like, the promotion from, you know, an experimental to a stable instrumentation, like, implies that you have to break something.
And that's kind of annoying.
And so, what the… you know, and there's a bunch of other contexts to this conversation, but one suggestion that came up is, from Austin Parker was, like, what if we have a property, like, named something to the effect of.
Default, instrumentation, stability, threshold.
And, you know, by default, it was stable.
But other options… Include things like, you know, beta, alpha, etc.
And what this property would dictate is for all of your instrumentation libraries, you know, you'd have to indicate that each one of them has, like, some sort of stability indication on them.
And this is… this, like, this one property dictates the threshold across all your instrumentations, Which, which… of which instrumentations are installed by default, right? So, you know, if you switch this from stable to beta, any instrumentation beta or higher would get installed by default, where if it's stable, that's obviously a smaller set. And so, like.
this kind of solves the problem that we were… that I was talking about before, about a property's default value changing when you go from experimental to stable, because you know, essentially, there is no default value for whether an instrumentation is enabled by default. The default value is dictated by another property.
and so, I think this kind of solves one of the issues I had with this, With this… blog post in this recommendation that was coming, which is like, hey, only stable instrumentation should be enabled by default. It's like, okay, if we're gonna do that, we need a lever to allow users to restore their previous behavior very easily. And this type of option could represent that lever. It's like one single place that you could set to alpha or beta, or whatever and get the behavior we have Currently.
And, you know, if you're… if you're, you know, more conservative, you can leave it at its default value of stable, and… And get the results from that, so…
JP Jason Plumb 00:53:14 Yeah, I wish that was flipped. I'm sure somebody said this in that PR, but, like, you kind of want the status quo to be the default, and the people that are, like, militant about having stability can opt in to stability.
I mean, that's… my preference, and I'm sure I'm not completely alone, but… Okay, so that's gonna be a breaking change, then.
jberg 00:53:35 Th-this was just a… this was just a conversation.
JP Jason Plumb 00:53:37 Oh yeah, for sure, but for us, for Java, that's a breaking change.
Oh, definitely. Yeah.
jberg 00:53:43 And, you know, there's still conversations, like, you know, I think this blog post itself talks about you know.
library should not include alpha or experimental instrumentations by default. But then there's, like, Austin is calling out some special, like, status where beta means that it can be included by default. So I think, like, you know, in… in, like, Austin's opinion, the default would be Beta, not stable.
Okay. And, you know, this is still a breaking change for, you know, OpenTelemetry Java, but I guess it's not as breaking because more things would meet the criteria for beta than for stable.
So there's wiggle room, I guess, in this conversation. There's still…
JP Jason Plumb 00:54:27 It's adding so much complexity, though, for users to have to juggle, like, mentally juggle the difference between beta-alpha and stable.
Ugh. I mean, and think about troubleshooting that, like, users are like, hey, this thing didn't work, and you're like, well, what's your stability compatibility threshold? And… I don't know, seems… seems complicated.
jberg 00:54:47 Yeah, I think for any of this to be feasible.
We'd have to have very good definitions of what the different stability levels are, And… and document them all, so every single instrumentation module has to have its stability level, like, you know, clearly documented and discoverable, through a variety of means, and then we'd have to even do something else, like, when you run the Java agent, we'd have to be able to, you know, log out some metadata that says, like, hey.
what threshold did you set, and what instrumentations were detected as candidates to install, but were not installed because, like, you know, your threshold was too high, right? You need to be able to discover at a glance, like, you know, something… an instrumentation library was not installed because, you know, you were too conservative with your threshold.
John Watson 00:55:38 Distribute…
Lauri 00:55:39 There's actually one more hurdle, is that even if you know that an instrumentation library was installed or not installed, you need to somehow figure out what that instrumentation library does.
jberg 00:55:51 Right, and that's… Jay's been doing some work on that, right? With, you know, automatically generating docs related to what, what data is spit out by each instrumentation library, but it's a… it's a hard problem with how many…
Lauri 00:56:06 But even there, like, it's hard to say, like, If you don't know that some random HTTP client library actually depends on NetE instrumentation, then, like, good luck.
jberg 00:56:19 Exactly, so some of them aren't emitting data, right? They're just, like, they're glue instrumentations that, like.
Lauri 00:56:26 And the relations there aren't necessarily obvious.
jberg 00:56:29 Right.
John Watson 00:56:31 And… Distros would be allowed to set… excuse me… would be allowed to set their default threshold to whatever they want, right? Like, if Splunk wanted to have their own distro and set it to alpha, that would be okay for them to do.
JP Jason Plumb 00:56:46 Yeah.
jberg 00:56:47 I don't see why we would get in the way of that, like…
Lauri 00:56:52 I want to point out another thing is that we currently don't have any stable instrumentations.
to… I think we are actually, like, a couple of years away from this actually becoming an issue, because if you'd want to change the stability threshold to stable, then you would end up with a non-functioning agent.
Jack Shirazi 00:57:15 Or an alternative approach is to declare everything stable and just accept that we're going to have breaking changes and major versions every time we want to.
Lauri 00:57:23 You can't declare them stable, because they don't conform to the semantic conventions.
jberg 00:57:27 No, we can, we can… like, that's… That's actually, you know, we are treating them as if they're stable today, because when we break them, we do so in major versions. So, by some definition of stable, they are stable. Like, we jump through hoops to avoid breaking users in minor versions with these things.
Lauri 00:57:48 Well, I don't want to annoy them, like, Actually, sometimes we change stuff in minor versions also, like…
John Watson 00:57:59 I was gonna say, the semantic invention bit is, I think, gets to what Jack was saying, like, we need to have very crisp definitions of what stable beta… stable and beta mean.
like, does beta require stable, like, semantic invention stability? This is a… this is, like, this would be a core question, right?
Lauri 00:58:20 And there are even, like, more annoying issues, like, for HTTP clients, I think the semantic conventions define two ways of instrumenting.
The two kinds of telemetry.
And one of them is the preferred way, but we implement the not-preferred way for some HTTP clients.
So, that could also be, like, kind of a blocker for stability, because icon.
Changing the instrumentation to follow the preferred conventions would be a breaking change.
jberg 00:58:59 Yeah.
Lauri 00:59:00 This is going to be a nightmare, like, if anybody wants to, like, move this thing forward, we need… more engineers, I think.
jberg 00:59:10 Like, this concept… This concept doesn't seem like a bad thing in principle.
Lauri 00:59:17 Yeah, but we are probably a couple of years away, at least, for it to become useful.
jberg 00:59:22 Yeah, right. So, like, imagine that… imagine us in a scenario… in a scenario where, like, 80% of our instrumentation was stable, and we had 20% that was, like, you know, experimental, that was being added and developed actively.
You know, in that type of thing, in that type of situation, you know, it would be perfectly reasonable to set this as stable and to… Like, to want to be able to have one property that allows you to have broad brushstrokes. Like, you don't, as a user, want to go and enable each individual of those instrumentations that represent the last 20%. Like, if you want to be more risk-prone, like, you just want to set one property that says, like, hey, like, turn up my level of risk, install everything that's applicable.
So I think it's, like, a good thing in principle, we're just, like, not there yet.
Lauri 01:00:09 I think users mostly want magic and fairy dust, they just want their stuff to work.
They don't want to configure stuff and figure out, like, what they need to enable to make things work. If they want to do that, then they could go, like, the manual instrumentation route.
jberg 01:00:25 Oh, I'm agreeing with you there, which is why, like, you know, I think one option is better than, you know, having to individually configure all the instrumentations you want to enable.
That's… this single option is closer to Magic and Fairy Dust, in my opinion.
Lauri 01:00:39 Yeah, but it definitely would be awful, as Jason mentioned, when, Things don't work for somebody because they have turned the stability threshold to stable.
While the instrumentations that they are interested in aren't stable.
JP Jason Plumb 01:00:54 Yeah, just think about troubleshooting that.
Lauri 01:00:57 Yeah.
JP Jason Plumb 01:00:57 We've had time.
John Watson 01:00:58 Oh yeah, we're out of time, I was gonna call it.
jberg 01:01:03 I think it would be helpful.
JP Jason Plumb 01:01:04 can of worms.
jberg 01:01:05 I think it would be helpful if some of the instrumentation, more focused folks can, like, go and comment on this, because it just… I think I agree with Lori, it just… it seems like the right idea, but just we're not ready for it. So, like, you know, what do we do?
What do we do now?
JP Jason Plumb 01:01:23 Yep.
jberg 01:01:26 Alright, well, anyways… the discussion, everyone. Yeah, thanks. Take care.
JP Jason Plumb 01:01:31 See ya!
Robert Niedziela 01:01:34 Right?
