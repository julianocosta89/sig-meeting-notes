SIG: Profiling WG
Date: 2026-02-19
Duration: 62 minutes
============================================================

## Zoom Recording Transcript

Felix Geisendörfer 00:03:37 Right, maybe we'll… Let me get started. Hey everybody, and thanks for joining.
We're gonna start with going through the previous action items, and I'm gonna share my… Green… A.M.
I'm gonna propose to go a little bit out of order here and start with Florian's, because I think we have Josh, and Josh might… has to jump earlier, so this is probably the part where we're gonna need Josh, so I'm gonna put this here. If anybody has agenda items that they would like to cover today and don't see on here yet, please add it to the list.
I'm actually gonna copy this whole thing here.
Oops, there's something being typed in.
I'll copy that again in a second.
And I think these two are done… I'm gonna move this up… Here we go.
So, the first action item is the… Work being done, or adding… dictionary references to resource attributes, which is a pull request to the OTLP proto, which you can find here, as well as now a pull request to the OpenTelemetry collector from Florian. Florian, let me know if you want to introduce it, or if I should do a little bit since we synced, but up to you.
Florian Lehner 00:05:14 No, feel free to go wrong, please.
Felix Geisendörfer 00:05:16 Okay, so, Yeah, for those just catching up, basically, we… we're trying to add, references to the dictionary, because we have attributes that are going to be repeated many times, attributes that are shared across processes, environments where processes are frequently spawned, and each process is being modeled as a resource.
And so we sort of have consensus around, I think, the OTLP level representation for that.
Which is just a quick reminder for everybody.
We are essentially modifying the common, what's it called? Any value message, and we're adding a string value ref, and the way that is resolved is if it's a profiling payload, then we look at the profiling dictionary and find the value of that string reference, so this is an index into the string.
table. Similarly, for the key value message, we have a… key ref, to reference the string representing the key. And as we have benchmarks showing that this greatly reduces payload sizes for workloads that we think will be frequently encountered by, people who want to use OpenTelemetry profiling. And, I think we, earlier this year, made, kind of breakthrough with, with the meeting we had with Bogdan, and Tigran, and Josh, and a few others, where we kind of aligned on that, and more importantly, also, Alexi contributed a cool idea on, sort of, making this, you know, doing this in a way that we don't have to rewrite all the processors to become aware of these, attributes, keys, these references into the dictionary.
Which is basically… the idea is that when we unmarshall the payload, we, yeah, we basically unmarshall the key references and the value references, but then we actually translate the resource back into the way how it would look like without these references in memory, and so everything… down the pipeline, including through the processors, can operate on resources exactly how it has before. That's a huge unlock, in terms of, simplifying things for the whole ecosystem. And, in terms of memory usage, we can also just allocate the strings that are used for keys and values once, doing string interning.
Clever, Chuck, I think you're muted, unmuted. And, Yeah, so then the last trick at the end of the pipeline is once we export an OTLP again, then we actually go through the attributes again, and we try to encode it in a more efficient dictionary representation on the wire again. But basically, the entire collector ecosystem, except for the receiver and the exporter for OTLP, can stay unaware of all the fun dictionary stuff that helps us optimize the profiling signal.
And Florian has done a great job creating a pull request for that.
And there's already some good discussion with Tigran and some others on there. I guess one important blocking point that we've reached is Bogdan, who was very involved in the earlier discussion, has been difficult to reach for the last few weeks, and for that reason, I pinged Josh earlier.
to potentially see if we… if we can all agree here, if the TC can agree, if there's award in where we could move forward and get this on the road, giving Bogdan a chance to maybe rewarded if he's really unhappy with it, because KubeCon is coming up in a couple weeks, and we were really, really hoping to announce the alpha of profiling at that point.
And the only way to do that is if we can get alignment on these two pull requests very quickly and get some landed very quickly.
So, yeah, Florian, if you have anything to add, please let me know, but if not, maybe Josh's thoughts would be the most interesting here. Probably no updates yet, since we just pinged him earlier today, but I wanted to recap it for everybody.
Josh Suereth 00:09:12 The basic update, Bogdan's in the middle of travel.
But we got his attention, and he's reviewing the PR, and it's… and basically we're saying, look, we need you to confirm that you're okay with this approach, and then we can move forward. So, I think that's, he was going to try to review the PR before his next connection flight.
I don't know if that happened, because he had a very narrow time window, but he wasn't able to join the meeting because of that. I would, Yeah, basically, we're gonna try to get you feedback as quickly as possible from Bogdan on that particular PR, so then we can move forward with the proto-change and get things done. But for confirmation, what I wanted to find out, you want to announce profiling as alpha.
Right? This is the major blocker. This is, like, number one blocker. So, we need to make sure this is here.
do you have other things that we also need to make sure are getting prioritized attention? So I want to get a list of those to make sure that we have… at least are making progress, and that folks who need to pay attention know to pay attention now, so that we don't run into the kind of slowdown.
Felix Geisendörfer 00:10:22 So, I would say in terms of major technical blockers, as in, like, more changes considered to the OTLP format, or collector changes, I think this is pretty much it.
Somebody correct me if I'm wrong. There is adjacent things that would probably be nice to have for an alpha, such as, like, some more in-depth documentation and, and, other things, but, those are probably softer in terms of being blockers as compared to the technical stuff on OTLP and collector's side. If anybody sees something that I'm missing, please chime in.
Alexey A 00:10:53 does… does the actual rename of the directory in GitHub needs to happen before we announce? Because I think now it's called, like, V1 Development, like, does it need to get renamed to V1 Alpha?
Felix Geisendörfer 00:11:05 Probably?
Josh Suereth 00:11:06 Oh, you mean on the proto-repo?
Alexey A 00:11:09 Yeah.
Josh Suereth 00:11:10 Oh, God. Yeah.
Sorry, I… that's… that's like a nuanced tidbit thing that's really frustrating. I… let me confirm with Tigrin and Bogdan what their thoughts are there. I… I can see us going one of two ways.
One is, we leave it in experimental.
And when you're ready… when you're ready to declare it stable, we move it to… be stable, because other… every… if every time you go from alpha to beta to release candidate, we're breaking every single receiver because we're moving where the proto is, that's a little awkward.
Jonathan Halliday (IBM) 00:11:47 Yeah, that's the, we discussed this on Slack a long, long time ago. That was basically what we said. We're not going to change the package name.
Josh Suereth 00:11:56 Yeah, I… let me just confirm that, though, because what I don't want to have happen is, we had that discussion on Slack.
Memories are not great. And so we don't want to have suddenly a, hey, we should change the package name again discussion. We should document it and actually write it down in the Proto repo. So I'll take an AI to actually write write up that as a PR to the proto-repo, of here's how we're going to do experimental things. This impacts more than profiling, like, we have the entity stuff that's going on that's still experimental in the same way. So, Does anyone have concerns if we leave it labeled experimental?
Through the entire process until we get to release.
Christos Kalkanis 00:12:36 I think that the current package name is Development, right? So it's not experimental.
Yes.
It's V1 development, which for me, it's perfectly fine.
Josh Suereth 00:12:46 I will write down that policy as a documented proposal for the proto-Repo, and push that, and get alignment on that now, so that you guys have a clear signal that it's totally fine, and that's what we'll do going forward.
Alexey A 00:12:59 Sounds… sounds good. And I… also, another discussion at some point, there was something about documentation, like, do we need to update or publish documentation somewhere, and, like, who is doing that, and .
Christos Kalkanis 00:13:11 Yeah, documentation is… we can do it. The reason it hasn't been done so far is because of this last blocker. Like, I want us to have the road clear ahead of us, so that we know, okay, we have the last hurdle behind us, and then we can immediately jump on it. We already know you know, who's going to work on it, and so on. So we have the resources, it's just that… We've been blocked on this last item for so long that we haven't really done the work yet.
So, essentially, the sooner we put these, the references behind us, the faster we can start on documentation.
And I guess, I mean, all I need is consensus. Like, if I… if Bogdan is okay with this, like, we just need to… we don't even need to… merge the PRs, as far as I'm concerned. As long as we know that Bogdan, Tigran, and Josh all agree, then I'm fine to start on the competition.
Alexey A 00:14:09 not to be skeptical, but sometimes you don't know if everyone is… like, merged PRs, I think I actually prove of… the best proof of agreement, because otherwise, like, something always can come up, and… but… but yeah, I… I… I… I agree. For the documentation, like, I understand the references thing, but… that's just, like, one nuance, and I would expect that there is, like, a bulk of documentation that can be, like.
Can we make sure, like, everything is ready besides that? Because it's an important aspect, but it's not kind of like the… It's not, like, the 90% cornerstone, if you see what I mean.
Christos Kalkanis 00:14:47 Okay, yeah, it makes sense. I can… I'll have an update for you for the next meeting. Hopefully, we can get the process started.
Alexey A 00:15:00 Does anyone outside of this group needs to sign up, like, needs to sign the documentation, or, like, what's the… Or is just us updating the documentation in the proto, or elsewhere? Sorry, I'm not super familiar with, like, how.
Felix Geisendörfer 00:15:16 I mean, I would say the source of truth is the proto and the collector implementation, and the documentation should match that, but if we ship some documentation that doesn't match that, then we're just gonna fix it and iterate on it. It's not… To me, at least, the end of the world for an alpha.
Alexey A 00:15:33 That makes sense.
Thank you.
Florian Lehner 00:15:36 from an outside perspective, I think a good point for documentation is always the OpenTelemetry site, where also the semantic convention is linked and the other signals.
And there we can extend on the, profiling signal, definitely.
Josh Suereth 00:15:53 Dope.
Just, just to confirm, when you guys are saying documentation, like, yeah, the question of where and what documentation is important. I agree, the… what you've written in the proto should be, you know, what matters. What's written in the collector is what matters. If you're not already onboarded to OpenTelemetry I.O. with, like, hey, it will… So, for context, OpenTelemetry I.O. has this thing where it will pull documentation from Git repos that you own. So if you have Markdown documentation locally.
They will actually take it, transform it, and make it publicly available in OpenTelemetry.io. They have a process for this for other SIGs.
If you're not already on board to that.
and you'd like to do that. I don't think that will be a requirement for Alpha in my mind. I'll confirm that with the TC.
But I think you do want to start that process early for getting a release candidate out, right? Because we'll want to have public docs there. And that… there's… there's, for context, there's someone that CNCF hires to kind of, like, help with our docs effort, who runs all that and… and that infrastructure.
And it'd be good to go to the communication SIG and kind of sort out, hey, we have all this profiling documentation that we'd like to have on OpenTelemetry IO, we want to figure out what that looks like, and get that sorted out in that SIG.
With them. So it'd be good to send someone to that and find out what you can do. For Alpha, though, my view is whatever you have in the proto repo automatically synced OpenTelemTree.io.
OpenTelemetry I.O. has a concepts page, that you can contribute to OpenTelemetry I.O. directly, whatever concepts you think are important around your alpha.
But I don't think you need, like, formal, you know, here's how to onboard as if you're a user who's gonna use this in production for an alpha.
yet. I think if you have those docs still in your repo, that's fine, and we can figure out how to get them on the OpenTelemetry I.O. site over time. Like, that… I would say that that's definitely going to be needed for, again, release candidate.
maybe for beta, you want to try to get it in there in that time, just to get broader reach, but I don't feel like you need that right now.
Felix Geisendörfer 00:18:08 2…
Josh Suereth 00:18:08 Oregon, boarding.
Sorry, go ahead.
Felix Geisendörfer 00:18:11 Go ahead. Just quick, on… does onboarding document… documents need to be imported, or could we just also maintain them upstream?
Josh Suereth 00:18:20 That's a question for the SIG. I think you can just contribute them upstream. They have the onboarding thing for convenience for SIGs, so, like, if you want to keep your docs close to developers, like, here's my rule of thumb, right? If I'm making a feature.
And I make it a requirement on the PR, where when the feature's committed, the docs are updated at the same time.
that… Sometimes leads to better docs overall.
We're doing some crazy experiments in other parts of hotels, so, like Weaver.
We're having trouble getting docs written.
So what we did instead was we require really thorough unit tests and integration tests that are end-to-end examples, and we have an agent updating features in Docs, just to see how that works.
it's… let's say it's decent. It's decent enough that it's better than nothing.
But I don't know if I'd recommend it yet, right? But that's just something to think about. Like, that's why the import thing… like, for example, semantic conventions are the docs, and so we import that into OpenFilm.io. I think Java, they're importing from somewhere.
into the docsIG as well, if I recall correctly. And it's kind of like what you're comfortable with, right? If you, as a community, are willing to go update the docs and keep them maintained separately, great.
Personally, I'm more of a, the person writing the feature, updating the docs at the same time, and making it part of code review.
is, I find more success with that myself, right, and the projects that I'm running, so…
Felix Geisendörfer 00:19:56 Yeah, I think long-term, that's probably where we want to be, but I think short-term, it would be really sweet to go to alpha at KubeCon, so whatever's gonna get us there, I think.
Alexi?
Alexey A 00:20:07 Do we want to get a blog post before KubeCon with the alpha announcement? Because if we do, I can… I can take, if this is useful, I can take drafting the text and, like, circulating with… with the folks here.
Felix Geisendörfer 00:20:22 I think that would be excellent to have a blog post.
Morgan McLean 00:20:25 You probably want to… like, in the past, we've usually timed it so the blog posts go live, at KubeCon.
But you'll definitely want to draft it in advance.
Alexey A 00:20:33 Yeah, we can, we can discuss, like, the timing, but I can start, like, drafting it in a Google Doc and, like, circulate it to folks here, and we can, yeah.
Morgan McLean 00:20:42 Yep, great.
Felix Geisendörfer 00:20:42 Will you create an action item on top, Alex? Yeah, that'd be awesome.
Alexey A 00:20:45 Yep, yep, yeah.
Felix Geisendörfer 00:20:46 Awesome, thank you so much.
Okay, then just to recap, next step is getting Bogdan's attention, and hopefully he'll unplug us. I am cautiously optimistic, because I refused the PR with Florian earlier today, and my impression is It's really just local modifications to the receiver and exporter side. Nothing else in the pipeline is impacted, nothing else in the pipeline is exposed to new APIs that could confuse people or create future maintenance problems. There's no overhead to the existing signals when they do their resource unmarshalling, and the benchmarks for profiling itself show minor changes in performance that seem totally acceptable for some payloads, so hopefully we can get this on the road, and then we will finally be in alpha stage. That'd be amazing.
Okay, anybody else has more things here? If not, we can move on. Going… Once?
Going twice, three times?
Okay, then we're gonna continue with, previous order, I think… was Alexis actually first? I think I got… no, I think, the context stuff is first, so is Ivo here?
Ivo Anjo 00:22:02 Yeah, but we can do the Alexis items first if it's preferable. I'm okay.
Felix Geisendörfer 00:22:10 Up to the two of you.
Alexey A 00:22:12 Yeah, I can, I can mention mine. The initial commit was submitted, it's in GitHub, and I will continue to… I'll probably call this action item done, but, duplicate an orphan's check to add, and I will, I will add them, but… haven't worked on that yet. Maybe I will add this separate, like, maybe we can call this done, because this one is just, like.
outstanding for so long, I just want to cross it out, and I can add the new one for the remaining work.
Felix Geisendörfer 00:22:47 That sounds good.
Alexey A 00:22:49 Okay.
I will add, a new one.
Felix Geisendörfer 00:22:57 Do you need help from anybody else here? Are you blocked on anything?
Alexey A 00:23:01 I would encourage people to, like, when you collect, for example, for people who are producing the… like, when you gather the format, for example, with the collector, with the PPF collector we have, I would appreciate if people just, like, start trying to use this tool and give feedback.
Like, or if you have some representative profiles, feel free to share them with me, and I can try them on the tool.
I just want to make sure, like, as people start to produce the data, we start using this tool and kind of, like, iterate. I want this to become some sort of, like, feedback loop with bugs and feature requests.
Felix Geisendörfer 00:23:40 I think we can do that on our end. And I guess some things that's a little confusing here in terms of how we get this laid out. This to-do set sample type order, default sample type attribute, but I believe you were talking about the validation tool just now, right?
Alexey A 00:23:52 Yes, I was actually talking about validation tool, because I think the sample order was actually… like, that's done already? I don't even see that action item.
Felix Geisendörfer 00:24:03 Did I… what did I do?
I copied that from up here, Active Action Items, this is where I got it from, Alexi.
So, just this line right here.
Alexey A 00:24:13 Oh, yeah, this is… I don't know why I was talking about the validation tool. Sorry, I… sorry, I completely confused myself.
Felix Geisendörfer 00:24:20 I mean, it's fine, we can… I'll just update it a little bit in the log, so it's less confusing.
Alexey A 00:24:25 Yeah, I will… yeah, I think we already crossed out the validation tool. I will add the follow-up action item.
Felix Geisendörfer 00:24:32 Yeah.
Alexey A 00:24:32 Yeah, so it's probably, like, early morning, and I just, like, I… my, my, my, my mind wires crossed.
Felix Geisendörfer 00:24:40 No problem. Do you still want to talk about the sample type order defaults?
Alexey A 00:24:43 I think that is done… I think that is done and merged, so I don't feel there's anything to discuss.
Felix Geisendörfer 00:24:51 Okay, then maybe you can just check it. Awesome. Thank you so much.
Alexey A 00:24:54 Maybe, maybe, well, maybe one thing that… the question to Florian, probably, like, this… this… the use of this attribute needs to, needs to be added to the PROF conversion.
Florian Lehner 00:25:06 Might be done once it's available. The problem is… So, two points. Yeah, it's not released yet, so cannot be done unless someone comes up with a hack.
And, the second one with the validation check.
I think I wrote a comment at some point in the review that, EVPF profile, I cannot use it because it works on P data and not on… at the V1 Development Proto, so there would need some additional conversation happening, so we cannot just drop it in and say, hey, we want to use it.
Alexey A 00:25:42 Sorry, I actually meant the sample type order attribute.
Or… or did you.
Florian Lehner 00:25:50 Yeah, yeah, that's not available yet. Okay, okay, so, like, two months…
Alexey A 00:25:56 Two points were, like, they were about the two different things. The first one was about the sample type order, the second was about the validation tool. Yeah, like, validation P data, yeah, like, currently the validation tool works on the, on, like, on the actual proto, not on the P data.
We can discuss separately.
How to deal with that.
Florian Lehner 00:26:16 Otherwise, I would have already suggested to drop it in your eBPF profile.
Yeah, if we do it now, it, it costs us conversion.
Alexey A 00:26:25 For the sample type order, is it okay if I at least, like, I will add an action item to you, like, to do this once it's available in the release?
Florian Lehner 00:26:35 I'm following the SamConf release, and if the SEMCONF release is done, then the Go release, and then it will become available. So, yeah, I'm having this on my radar.
Alexey A 00:26:47 Okay, do you want an action item, or not really?
Florian Lehner 00:26:50 I just have it already on my list, so I don't need an extra night.
Alexey A 00:26:54 Okay.
Felix Geisendörfer 00:26:59 Okay, I try to do my best to demultiplex the multiple conversations to the right parts of the notes here. Hopefully I got it right. If not, feel free to edit. Any more thoughts on either validation tool or sample type, or default sample type attribute?
Going once… Doing twice… All right, moving us on. Ivo, your time to shine.
Ivo Anjo 00:27:24 Yes, me. So, there's been a couple of updates and a couple of things that are under discussion in the process context, OTEP.
One of them is the question of, like, the… it seems kind of easy when you… when we have only one resource, but what does it mean, like, with the evolution of the whole entity thing, like, what does it mean to… because, like, people were asking, and that's the link that I left there, like, the resource representation, there's a comment saying, like, oh, what does it mean for, having processes that have multiple hotel SDKs?
And we've been discussing this internally at Datadog, and we are kind of unsure a bit, like, well.
What would we want in the process context?
for a process that has multiple SDKs, and possibly multiple entities in those SDKs, it's kind of unclear how would, like, what we would want out of this.
Felix Geisendörfer 00:28:25 Can you refresh people's memory here on how we end up with this? This is when, like, you build an application out of different languages with… different tracers or SDKs, or…
Josh Suereth 00:28:36 I can… I can speak to this, because the OTEP's coming out of the entity SIG, which is one of the ones I run. So, the use case is, like, let's say I am an SDK, and I'm observing multiple things.
like, I have multiple tenants, for example. It's kind of a tenancy thing.
Or, what's really motivating it is the browser, folks. So, the SDK lives for the entire lifetime of, like, a page being open, but a session Is a different kind of scope.
And so what they're trying to do is actually, like, make an SDK that lives for the lifetime of the page, and then create a new entity for a session, and report data against it.
Another thing that we do, We actually do this inside of GCP.
is for some of our SDKs, we might have a server that is actually running on behalf of multiple things.
And so, we will, kind of allocate a resource for those different things, and tie metrics to those different things, and fire them out separately.
So, but that's kind of the multi-tenancy use case.
the OTEP in place is to solve both of those needs. It's basically, the SDK can say, cool, There is a default resource for the SDK.
that represents the SDK itself, and information about that SDK. And in a basic scenario.
The resource and the process are the same.
But for some advanced servers, I'll give you an example, like Apache Pulsar is one that ran into this problem, right? They might be reporting on behalf of someone else.
or, the old-school Tomcat stuff in Java. I only know this because I was in the Java SIG for a while. You might have different web applications that are being hosted from the same process.
And so you need someone to divide the world for you, where they understand what that tendency is and are doing that division.
I do not know how you would handle this from an eBPF perspective, but from a profiling's perspective specifically, I would expect that you need one of two things to be true. Either someone gives you enough information that you know this sub-piece of a profile belongs to this application over here.
Or you just report against the whole thing as your resource, because you don't know. You have… the data has not been divided for you.
For EVO's proposal, the question would be.
how could we tell eBPF about that tenancy division? Is there a way that we could get that context in place where you could understand that, like, okay, when I calculate, you know, the CPU usage of this method, it's on behalf of this thing, as opposed to on behalf of that thing, when the same method can be used for two purposes. Is that something you need to do in profiling?
That would be the use case here for this multiple resource world.
Felix Geisendörfer 00:31:35 My initial thought there would be right away that Splitting a single process into multiple applications is, like, a thread-level context propagation thing, because the… whatever the thread is currently executing, that context will tell us which applications it is for.
I don't think we'll be able to take stuff, like, if there's a shared garbage collector or something across these applications, to, like, split that out, so we will… by default, we'll have to report against the whole thing, the process being the resource, but if we have thread-level context, we report on the more fine-grained context. That would be my first guess here, but… Happy to hear something else. This is actually very interesting, so, because we have this idea of, like, linking thread and spend… no, sorry, ignore me, I think I'll stop here, because I think I'm… Talking beyond what I've thought about.
Christos Kalkanis 00:32:25 One more thing to note here is that the process context in Evo's proposal is not specific to eBPF profiling, really, right? So it's specified to be more generic, so any consumer could technically read the data and use it. It doesn't have to be the eBPF profiler.
Josh Suereth 00:32:42 Yeah, and if it helps, the thing you were just mentioning, Felix, with, like, the garbage collector versus the process, in this multi-resource world, I'm finding the proposal so I can send you what it looks like. In this multi-resource world.
Let's say I have a Java server, the… the default would be, like, I have this default resource for my SDK that I report against, and my Java garbage collection will go against that.
It won't go… it won't divide by tenancy. I would have to explicitly opt in my… my… like, I… right now, the proposal is you explicitly have to slice your, instrumentation to know about tenancy in some fashion.
There are proposals on the table to actually find a way to do this with context. That is not what we're doing initially. Initially, we're trying to do it where, like.
you can explicitly understand what these are and fragment in instrumentation, and it's only for scenarios where, like, I have a limited number of things I'm reporting against. So I'm doing, like, you know, 10 to 20, not hundreds or thousands of divisions.
So it's not actually… it's not doing, thread-based context, it's doing kind of lexical context in the programming language.
If I'm using words, sometimes I invent, or I take, terminology from when I did language compiler design, and I throw it into observability. So if I use any of those words, just yell at me, please. But yeah, so, like, we're thinking of lexical scope, not runtime scope.
If that… if that resonates, if you, like, if you understand what I mean there.
Yeah, I'll get the… I'll get the proposal in the notes.
Felix Geisendörfer 00:34:28 Yeah, I think I would like to do some more reading on the proposal I'm talking about, what I imagine the world to look like on that side.
Ivo Anjo 00:34:35 So, I guess, like, so I think it does make sense that, part of this intuition of the different, resources, or, like, what the thread is, like, on behalf of who the thread is executing right now is very natural… I think, very naturally mapped to the, thread context.
I… And it maps to the fact that, like, the entity… I don't know, maybe entity is not the name. The thing that is setting the current trace ID, the current space, the span ID, the thing that will need to do the writing, the SDK, implicitly knows what SDK it is, because it already has spun ID, trace ID, a bunch of things, so it knows how to identify itself.
I think that the big question is, I guess two things. One, how, like, the, the, the fallback stuff, so when there is no thread context, Like, do we just say, like, okay, there is one… the one default resource and everything gets attached to it if there's nothing else?
And the, the other question is.
Okay, assuming that we have the thread context.
how do we, do we relate the, how do we model this in the thread context, in a, I guess, an efficient way?
Because I'm… Possibly we don't want to put the whole resource in the thread context every time, so we maybe want to say, like, okay, we maybe have a… have some kind of a link where we put the resource the extra resource is somewhere in the process context, and then we say, like, oh, I… this thread belongs to resource number 2, and resource number 2 is, like, the full resource with all of its attributes and things. Maybe?
Josh Suereth 00:36:43 So, I… I'm gonna jump in. I think… the discussion we're having, just one meta point, I think this is something that we'll need to kind of discuss, broadly, because there's a lot of impacts across OpenTelemetry. I think there's this whole thing is something we've been kind of diving into briefly, and it's an area that OpenTelemetry doesn't serve well, and we have to sort it out.
To go specifically to answer you, I would argue, like, we need a set of simple defaults, and the idea is for a given process that's running, right, there's an SDK in that process, if we make that assumption. That SDK does have a default resource, that's what our OTEP currently has. So if you were to say.
there's thread contents that tells me about, you know, what the telemetry should be generated for. Like, it gives me the tenant for which I'm… calculating information. I would use it. Otherwise, I don't know what the tenant is, and so I just go back to the default and aggregate at that level. That, to me, is completely reasonable and in line with what we were trying to do with our proposal. So… so I'd be a fan of that.
That said, like, when we think about these decisions, we need to think about not just, like, the eBPF profiler side, we need to think about the SDK side, what the, you know, because, Yeah, anyway, I'm probably talking too much, but… the cooperative nature between the SDK and eBPF is a thing I want to sort out.
when should the SDK be giving you information to do this? And when is it okay just to kind of aggregate by default? Because you're… you're… in EVPF land, basically covering the gaps of instrumentation.
Florian Lehner 00:38:29 Not sure if this is the case, but I think we run in exactly this unknown resource.
territory.
if the… span and trace ID comes from… Something else, something that is, running… like Obi, that just reads the information and provides the information, to eBPF Profiler.
Yeah, in this case, we just have the span and trace ID and don't have the resources and cannot, Make it account to something like this.
Felix Geisendörfer 00:39:07 Let me rephrase this to make sure I understand. So, OB is instrumenting the application from the outside in using eBPF as well, so it's not an SDK-based approach, and because of that, we actually don't have something like a span or trace ICE that's associated with the current threat. This is all sort of managed Outside of the context of the active process, and so we will never be able to do that kind of, Thing? Yeah, I think that's…
Florian Lehner 00:39:36 Yes.
Felix Geisendörfer 00:39:37 I think that sounds roughly right, and I guess the only thing we could do there is at some point, for having OB and the eBPF profiler to be more… sympathetic towards each other, and actually maybe being one or the same thing. I know that there's been discussion about having, like, an eBPF collector distribution that sort of marries the two technologies more closely.
Yeah, I think that's the only path there to make it work. If not, then the answer for now is just it doesn't work, right? Like, it's always a default resource.
Yeah, trust me.
Josh Suereth 00:40:13 I, I think… the, in my mind, and I might be oversimplifying this, because I know Obi does a lot of heuristics for this, but if we had… if we could extract somehow context propagation understanding in eBPF as a shared thing that basically the eBPF Profiler and Obi would do similarly.
That would be my holy grail here, because again, when I think of OpenTelemetry, the foundation is the context propagation. This is where the context library in our spec is probably the most important.
the instrumentation that makes sure the context is propagated between threads when one request that you handle gets sent to a different thread, or goes through async, or coroutines, or all that hell, that is the most important piece of technology in all of OpenTelemetry.
And so, I think having a dedicated eBPF solution for that, that's cooperative with the SDK, to me is a big enough effort that, like, you could dedicate a set of resources to it, and then sharing that between Obi and between the profiler, so that you get good context. You know, you can rely on whatever the hell it's tracking. If you say, I need context for this current thread at this current time.
and I have a signal here, I can ask it information about what the current context is.
again, I'm speaking not really knowing your architecture, but knowing, like.
Felix Geisendörfer 00:41:41 It'll be… Can I ask a question from my understanding? With Obi, there is no SDK, right? Like, you're instrumenting the application without an SDK, so there is no shared SDK, there's only two things in this picture, OB and the BPF compiler.
Josh Suereth 00:41:53 Yes, and what OB's doing, from my understanding, is it's actually tracking IDs of, like, where a request came in, and it's using heuristics to say, at this point in time, what should my contacts be? And it's trying to connect the dot of the thread passing that happened.
And so, it'll instrument, like, areas where something might pass to another thread.
It'll instrument and try to understand if GoRoutine A calls go routine B, I'll put a connection there, so I can track back to the context that I needed. But it's basically doing a trace manually in eBPF, and trying to tie context that way.
Because that's, like, again, that's what you have to do for tracing.
So that's why I'm thinking if we get that capability as a, as a, as a, just a dedicated thing.
it is the foundation of OpenTelemetry. Like, that is… if we're gonna have eBPF instrumentation, in my mind, that's the most important thing to get right, for OpenTelemetry to kind of hang together over time.
That said, profiling, I think you can independently be useful without tracing. So, with that caveat, for the rest of OpenTelemetry, I think this is, like, the foundation. And so, I'd love if we, like, really focus on that and dive deep, but I also, you know, what is it? Don't put the cart before the horse kind of a thing?
we're starting to explore how deep this can go, and, like, the problems. But, you know, Evo, you've been working on this, trying to figure out what the… what this looks like. It might make sense to put a dedicated effort around that problem.
Felix Geisendörfer 00:43:27 Yeah. In terms of, like, just priorities, I think if we can get, like, the eBPF profile to work with the SDKs, that's probably the first priority, because that's what probably most people have.
in use right now, and the OB stuff is going to be, like, the next giant leap after that, at least in my mind. Does that sound roughly right, Josh?
Josh Suereth 00:43:45 Okay, yes, but I have one fear.
Obi is so darn easy to use.
Right? It's so easy to use.
And so, one thing that I do expect to happen, you know, there's a set of limitations with it.
But it's so easy to use that it could see explosive growth as soon as it becomes stable.
That's the… that's the only caveat I'll give you. This is my expectation. If you think of, like, the Java auto-instrumentation versus Java SDK and API, one of these we consider a bit more stable, and we'd like to have more native instrumentation.
Versus having an agent go rewrite your code. But guess which one is highly used, and, like, really low friction for users?
It's the agent, right?
So, I… I… that… I see that same thing with eBPF here.
Felix Geisendörfer 00:44:37 Yeah, a small comment on me. I assume when you say agent, you mean, like, the Java agent concept, which is, like, something you injected into Java?
Josh Suereth 00:44:44 Yeah, I think it's called the Job Instrumentation Agent. It's a… it's a thing that, when you load classes, it rewrites the bytecode.
Felix Geisendörfer 00:44:51 Yeah, yeah, it's just terrifying because the term agent has, sort of, many interesting meanings these days. Thanks.
Josh Suereth 00:44:56 Yeah, we're… internally, we're no longer allowed to call observability things agents agents, we have to call them.
Felix Geisendörfer 00:45:02 something else. Our main observability collector thing is unfortunately called.
Josh Suereth 00:45:06 Yeah, exactly.
Felix Geisendörfer 00:45:07 That is… that's interesting. Yeah.
Josh Suereth 00:45:10 Yeah, anyway, it's fine. Go ahead, Eva.
Felix Geisendörfer 00:45:12 But I gotcha, like, I think that, yeah, you're right, it could grow very quickly, so, a very, very close P2 after the SDKs. Okay, I'll let some other people go. Ivo and Alexi, I think, is the order.
Ivo Anjo 00:45:25 Yeah, I just wanted to say that there is one thing with Toby that… I think it's a bit of a tough note to correct, which is, ideally, we would like the same solution for the SDKs and for OB.
But… We have not yet found one solution that does not kind of suck for the other, because, In terms of overhead, especially. So, like, you can definitely have a solution that works for both, but the kind of, like, the fact that, like.
spend and contacts are being, installed and switched and wherever all the time means that, like, a solution that's really nice for OB, kind of sucks for a pure user space solution, and kind of Back and forth, so… Ideally, this is a problem that maybe we can crack and unify them, but there is a non-zero chance that we might need at least two different solutions, one that is kind of nice to stuff that is in kernel space, and the other that is nice to stuff that is in user space, and we might not get, like, a one that is nice for both.
Felix Geisendörfer 00:46:35 Makes sense.
Thanks, Alexi.
Alexey A 00:46:39 Is this, like, one or the other, or a particular process could actually have an SDK in it, and also it's profiled by Obi, and they kind of, like, overlay in a nice way?
Felix Geisendörfer 00:46:51 So…
Josh Suereth 00:46:52 The… the… I'll just say from the TPC perspective, we want these to overlay in a nice way. Whether or not it's true today, that's where we want to get to.
Alexey A 00:47:02 Okay. And also, a question for multiple SDKs in the same process. Are there kind of, like, canonical cases where this happens? Because I could think of, like.
Either, like, multi-versioning for some reason, or multi-language in the same… Language in the same process for some reason, or… Are those two, like, kind of canonical, or is there something else? Just, like, curious, because we said, like, oh, there might be multiple SDKs in the same process, but I wonder, like, if we know this is, like, this is where it happens, like, 90% of the time.
Josh Suereth 00:47:43 That's… that's a hard one to answer, so… The… It's… what we're trying to do is avoid having multiple SDKs where it's not useful to have multiple SDKs. So if an SDK has the same export path and pipeline, that's what the proposal's trying to solve, so you're not creating more than one.
Today, though, if you… if you had to have a different resource you're reporting against, you have to have a different SDK. That is different than, like, the process layering thing you're talking about, so that would be… This is another discussion that has been in the background for a long time. Python, right? Python has native libraries and native extensions. PHP. PHP's auto instrumentation's written in C++.
And there's a native extension, and it's using, like, C++ hooks and part of the C++ SDK.
We don't have a good story around that layered problem.
And I think we do need to get one in OpenTelemetry around that, but that is another can of worms to address over time. There's rumors and stories and things, but we're still kind of… you know, making things work, and then optimizing that piece right now. In terms of, like, where we see the multi-SDK, it's mostly around, what… I have a process, and I want to report against two things. Like, I'm observing something remote to me. The collector, for example.
Any collector-receiver could actually be observing a remote thing. Like, there's a, you know, a MongoDB might be observing a Mongo cluster. We want the resource to be something remote.
If I needed.
Alexey A 00:49:23 Or a sub-process, maybe?
Josh Suereth 00:49:26 Or a sub-process, sure, sure.
So… so that… that's… that's the need right now that's driving it. It's not the multi-layer problem. The multi-layer problem, aware of, do not have a solution for yet. That's one of those open questions, and you know, with infinite headcount, we'd address it right now, but… there's not infinite contributors to OpenTelemetry, and even if there were, just coordinating would be, you know, hard. So, that's a problem to tackle in the future, and I think eBPF and, is gonna be a good… Technology that forces us to solve that problem.
Alexey A 00:50:02 Yeah. Yeah, thank you, Josh, this is a very clear prioritization, I understand this much better now.
Felix Geisendörfer 00:50:09 Boom.
We have two more agenda items, but if anybody has another sort here, please go ahead, Ivo.
Ivo Anjo 00:50:17 I wanted to, like, there was one more thing I wanted to clearly… sorry, not clearly, quickly bring up, which is the… we have this timestamp right now in the process context, the published NS timestamp.
And there's kind of two small questions I wanted to ask about that, which is, right now in the spec, we use the publish.ns as a synchronization point for updates, but not for the initial publish, so I'm… someone raised that, and I… I was planning on changing that, unless anyone is concerned. Like, so, in particular, right now, when we create the context, we kind of say, populate all these fields, and then write the signature last, and so the signature is a synchronization point when we create. And on update, we say, like.
do the, 0D published, write everything, and then set the published. So the published is a synchronization point, so I wanted to, like.
Use it for, for, both creation and updates.
So, if no one is concerned, I'll just do that. And the other thing is, there were some discussions about, What happens if, the… the time… the clock goes back and whatnot. And we kind of said, okay, maybe what we say is, like, we don't care if the clock goes back as long as it's a different value, but there were still some people, asking, okay, but does that mean that the… publisher of the context needs to track every… possible publish that, that it has used to make sure that it doesn't repeat the publish that. And, to be honest, like, I'm not sure this is a big problem, this is one of those, like, in theory, this can happen, so I'm not sure if we want to solve it, but yeah, solving it would mean, like, we have, like, a sequence number, and we move over to it, so… I wanted to ask, here as well, if people had thoughts.
Felix Geisendörfer 00:52:11 Yeah, my first thought is, maybe that's a stupid question, but there are… shouldn't there be monotonic clock sources that don't suffer these fun things?
Ivo Anjo 00:52:19 That's the thing, like, should we just switch to a monotonic, or we just have… we have the timestamp plus the monotonic, and we use the monotonic for the synchronization, so that's the question.
we can… Get the monotonic time source, or just use a version, an incrementing counter, or something like that, if needed.
Felix Geisendörfer 00:52:37 I guess I don't have strong preferences, but I guess what you're saying is if we do use something else, we still need a timestamp? Or is the timestamp then not needed at all?
Ivo Anjo 00:52:46 We don't need, but we can keep it if we like it. We just don't use it for synchronization, and so we no longer have these problems of, like, what if the timestamp does this or that or wherever, but we can still keep it if we like the idea of having a timestamp.
Felix Geisendörfer 00:53:00 I think I would slightly prefer a monotonic clock reading over a sequence counter, and to me it's almost as good as a war clock timestamp, because if something, like, doesn't realize something has changed right away, and it sort of comes in late, it knows how stale, sort of, or how long ago the update was, and it can do that with a monotonic clock source just as well. Actually, even better than with a wall clock, normal clock source.
And with sequence numbers, you lose that sort of, like, time delta between the update happening and you being aware of it.
And if we don't need the wall clock timestamp ever, like, I think then that is the sweet spot here. It's just my quick thought.
Alexey A 00:53:43 As a suggestion, maybe it would make sense to discuss it in one of the future meetings, just to dive a little bit deeper.
So that we don't… don't trash it, unless it's… unless every… it's… because, like, I… I kind of, like, I understand it's, like, 60%, but everything involving timestamps… Like, stack unwinding and timestamps are my two favorite… two of my favorite topics, probably, in profiling, so…
Ivo Anjo 00:54:12 I think this is not a blocker for our other work, so let's discuss this again next meeting. Happy to.
Felix Geisendörfer 00:54:24 Okay, sounds good. Then… Second last call for this agenda area. Any more thoughts? If not, we have two more agenda items. Going once, going twice.
No, then, Frederick, who I think is here, has period type unit value.
Frederic Branczyk 00:54:42 Yeah, so, I just happened to notice this the other day, that, currently the VPF profiler doesn't set period type unit, and therefore also no value, for off CPU and for the probe, counters.
And just kind of coming from PPROF, that felt odd, because I don't think I've ever seen a PProv that didn't have these also set, and so I was curious how… where we stand on making these potentially mandatory, and or what we would think. And Florian and I had a short conversation, on Slack about this, but I felt like it might need a larger conversation. What we… if we think so, then what would off-CPU and probe count?
Profiling… profiles B.
I feel like there should always be a description of what is between samples.
But Florian did have some valid points that it's potentially difficult to determine for some things.
Florian Lehner 00:56:04 Yeah, just to recap the discussion we had on Slack.
My point is that, something like off-CQ profiling and probe, probe profiling, doesn't happen in a regular interval, so it does not happen every X times, but it happens on events that can be any time. Can be… quite often can be quite large in between, or… whatever. And, so I was thinking, that's just my personal thinking, hey, I cannot describe something that is in between, that is not on a regular base, but I might be wrong on this.
For on-CPU profiling, we set this value, just not for these event-based, profiling, kinds.
Alexey A 00:56:53 Frederick, what would you expect it to be set to for the off-CPU? Because if off-CPU profile is more like… effectively, it's more like a trace, in a sense, because we intercept specific kind of, like, events, so I… it's unclear, like, what… what exactly would it be set to?
Frederic Branczyk 00:57:11 So, one of the ideas that I brought up on Slack was we essentially have… Statistically speaking, we have an average distance between samples, which is 1 over the probability, but that is only statistically the average, right? It can be faster, it can be shorter, right?
That… that was the only thing that I could come up with that sort of made sense to me for off CPU.
Alexey A 00:57:40 what probability, though? Because I kind of assumed that off CPU profiler, I trace every off CPU event.
Frederic Branczyk 00:57:46 No, no, weird.
Florian Lehner 00:57:48 We trace every event, but we downsample them, and I think the downsampling is that Frederick is referring to.
Alexey A 00:57:55 So it's, like, every nth, every nth… Event.
Florian Lehner 00:57:59 Yeah, I have a clip.
Felix Geisendörfer 00:58:02 I think expressing the sampling rate in the period type does sound fairly reasonable.
Alexey A 00:58:08 Yeah, or period type should actually be, like, different from the metric. Like, the metric is the actual CPU time, and period type should be set to something like, I don't know, like.
Event count 1,000.
Frederic Branczyk 00:58:22 That, that, that was exactly what I, proposed.
Alexey A 00:58:26 You're okay.
That would make sense, I think.
We should probably update the docs in the proto to kind of, like, document common cases like this. Like, if it's just, like, sampling based on the metric itself, then it should be sent to the base of the sampling period.
If it's… if it's, like, something, like, off CPU, where… Like, we sample every nth within… yeah, I… I can see that this is being confusing. I… I can take an action item to think about it, and maybe… maybe raise a PR with… Documentation improvements, and we can discuss there.
Frederic Branczyk 00:59:10 Sounds good to me.
Felix Geisendörfer 00:59:16 Awesome, thank you, Alexi. Then, yeah, just put it on top. We have 30 seconds left, but that might be enough to get to Florian's question about right access to this document.
Florian Lehner 00:59:24 Yes, just a quick question, and maybe if you follow it on Slack, this document was, was… The content of this document was cleared, at least two times in two weeks, and the question is, should we, lock down, in some way, the document, so that only authenticated user can write to it, or only a subset of people can write to it, so that people are not scared if they open this document and see a pirate flag.
Like it used to be.
I think… if… whatever we decide, I think the maintainers need to go to GC and ask for the permission then.
Josh Suereth 01:00:13 I might escalate this to the GC directly. I think Morgan's not here anymore, but, like, you're not the only SIG that has a public document that anyone can modify, and if you're getting attacked, that might be a thing that we want to make sure, whatever you decide to do, we can Apply across a hotel.
So, was there literally… it was deleted and there was a pirate flag? That's what was happening?
Frederic Branczyk 01:00:36 I was, like, hacked by blah blah blah.
Josh Suereth 01:00:39 Wonderful. All right.
dalehamel 01:00:41 Not exactly a hacker.
Frederic Branczyk 01:00:43 Yeah, I think…
dalehamel 01:00:45 I think at least requiring it be authenticated, then we would know, like, okay, it's this person, let's kick them out forever. If you just allow anyone on the internet to go and click a link and mess with your stuff, that's a different story, so… I think it's reasonable to say, if you're editing our document, we should know who you are.
Josh Suereth 01:01:05 Yeah, yeah, I think that's fine. I'll ping that on the TCGC chat quick, and see if we can get a quick decision, but yeah, it… You shouldn't have to deal with that crap, that's… that's bad.
dalehamel 01:01:17 I guess the one… For what it's worth, there's definitely… You need a Google account, but… yeah.
Sorry, who did I interrupt?
Frederic Branczyk 01:01:26 No, no worries, I didn't raise my hand.
There was definitely precedence for this in the Kubernetes project. I remember a couple years ago, this started in the Kubernetes project as well, so, you know, victim of our own success, I guess.
But there's precedence for this in the CNCF, is what I'm saying.
Felix Geisendörfer 01:01:47 Yeah. Yeah, Josh, let us know what you hear from the GC.
Josh Suereth 01:01:51 Yeah, in the meantime, can you open a community issue about how your document's getting attacked, and you'd want to change the default policy for document sharing? And then I can point at that as well. I'll escalate it immediately, but, like, it'd be cool if we have an issue to track it to make sure it actually But we update our guidance recommendation. Community is where all the, like, setup things for SIGs happen, so if we change the guidance there, we can change it for everyone.
Florian Lehner 01:02:16 IT people do this.
Felix Geisendörfer 01:02:19 Thank you, Florence.
Okay, I think that concludes today's meeting. We're already 2 minutes over time. I want to thank everybody again for the great discussions, and for all the work being done in between, and yes, see you all on Slack and the next meeting, and have a nice local time.
Ivo Anjo 01:02:40 Thanks, everyone.
Frederic Branczyk 01:02:40 Yo.
dalehamel 01:02:42 Cheers, thanks everyone.
