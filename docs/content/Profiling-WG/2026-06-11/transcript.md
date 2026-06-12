SIG: Profiling WG
Date: 2026-06-11
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

Felix Geisendörfer 00:06:29 Yes.
5 minutes in, so we may as well get started. As usual, I'll share my screen and take us through the previous action items.
And then discuss any agenda items for today. I see we have a few items, so let's try to get through them.
Let me do screen sharing… Okay, can folks see my screen?
Okay.
Thanks.
Then I will try to get us started.
So, usually copying stuff from up here… Okay, this first one has my name on it, so let me remind myself what this one was about.
I think this one is done, I think we tried to mock this as done before. I don't know why it wasn't checked off yet, I will do that.
Maybe somebody can move it to archived action items later for me, or I'll do it later. Just don't want you all to watch me fumble with that right now.
Yeah, so the key value unit proposal, I didn't actually get around to ping the TC yet, but Evo, who's here today, and I chatted a little bit about this, and if I remember correctly, Evo, you said you'd be interested in maybe taking this over, and maybe you could take the TC ping as well?
TC.
Ivo Anjo 00:08:11 I can, I can do that.
Felix Geisendörfer 00:08:13 Do you know who to ping on the TC, or do you need some names?
Ivo Anjo 00:08:17 I do not know who to ping. I was thinking of, when I read that, I could ask in the, specification SIG meeting, but maybe there's a better place.
Felix Geisendörfer 00:08:28 I think specificationSec Meeting is a great place to take this, and if you don't get the right people there, then I think pinging maybe Tikran and Josh directly could work, I think.
Ivo Anjo 00:08:41 Sounds good.
Felix Geisendörfer 00:08:42 And just let me capture this here. Oh, sorry, in the wrong section.
Seems like my screen is jumping while people are editing up there.
Ivo Anjo 00:09:02 Sorry, that was me.
Felix Geisendörfer 00:09:04 No problem, thank you for… Taking care of the action item above, Evo.
Okay, maybe at this point, it's also worth announcing that I may not be here for the next couple meetings. I mean, I will try, but I… our second child is due in the next two weeks, so I might be a little preoccupied for a little while, but I will return after that.
And maybe I'll still join if time allows.
Then what do we get here? Johnson, PR for moving original payload to dictionary. I think we actually don't need to keep this on. I think this is basically on hold until we decide to do the next, Basically, we're queuing this up for the better release of profiling. We don't want to break the alpha, all the time.
Jonathan Halliday (IBM) 00:10:09 Yeah, exactly, it doesn't need revisiting every meeting.
Felix Geisendörfer 00:10:12 Yeah, so I think… Do we have it on the… on the roadmap issue?
Yeah, let me, let me just take it out from up here.
And… Profile…
Jonathan Halliday (IBM) 00:10:30 I don't know, do we need a, like, a burndown for the… next release, we had one for the Alpha.
Felix Geisendörfer 00:10:37 Yeah, I did create that.
Jonathan Halliday (IBM) 00:10:38 You kind of did a separate document for that, didn't you? Yeah, that's the one.
Felix Geisendörfer 00:10:41 Yeah, yeah, so we have that on there, so I think we'll just keep track of it here.
Jonathan Halliday (IBM) 00:10:45 Yep.
Felix Geisendörfer 00:10:47 Maybe I'll link that up here as well.
Just for everybody.
That Yes, I think this is a good place to keep stuff so that we don't need to go over every meeting.
Then, do we have a Lexi here already, or today in general? If not, I'm just gonna move his stuff down here. Yeah, I don't think I see him.
Ivo Anjo 00:11:23 Yeah, there's a note at the top that he cannot make the first 30 minutes, kind of regularly, so he should be coming soon.
Felix Geisendörfer 00:11:32 Yep.
That makes sense. We can circle back to this later.
So this one, I don't have an update, but I talked with NAF, and it's possible that he'll help me with this.
So that's the update there. Do we have crystals?
But I think we don't need him to remind people to refuse these if they're still pending.
Yeah, so I think we have… 2, 3, 6 reviewers on this.
Maybe this one… Let's see what's this waiting on… Okay, this is… seems to be pending on Christos resolving conflicts.
So I will update that.
Then the second one… 780 seems merged.
So let's take 780 off, or maybe, Ivo, you can do it again, and I'll try to deal with the… jumping screen.
And I think that gets us through the action items, and we'll circle back to Alexis when he comes back.
So, let's go get on with the main agenda. We have… Oops.
There are my screenshots again.
Let me know when you close it again.
Okay, cool. Yes, so… Shay H, which I guess is Jonathan Halliday?
Jonathan Halliday (IBM) 00:13:27 It is indeed, yeah, so the first one's just there because, Everyone tends to miss stuff in the very noisy GitHub notifications. I've just spun up an issue to… To track this, relatively minor problem that we're seeing as we start to implement the spec. I came across this one first in the Java SDK when I was trying to make The default element for the first element of the lookup table array, is supposed to be encoded so that it's zero length on… you know, the product buff wire format, and the SDK kind of made that impossible, because the SDK wants all elements to be valid.
According to the… the semantics of the… the spec, and that occasionally requires them to be non-zero length. So we've… we've kind of created this problem for ourselves, where we want elements encoded in a way that the SDKs don't want to encode them. So I… I don't think it's super urgent, I don't think it needs discussion now, I just wanted an issue there so that we have something to refer to when people hit this, we can say, oh yeah, we know about that one, go and discuss it over here.
It might be worth copying it into the burndown for the beta, just to make sure we revisit it and we're happy with our design decision.
I think for now, M.
I can definitely see alternatives and trade-offs there, but… My inclination is to leave it as is.
And see what others think. For now, I think the Java SDK I did is the only one that exists.
I think other people will hit this as they… They get into doing implementations, and in particular, I think the collector will hit it.
Mmm… But for now, it's… it's just, yeah, this thing exists.
The second one.
Felix Geisendörfer 00:15:29 Let's just capture the conclusion here real quick. Sorry, yeah, I just…
Jonathan Halliday (IBM) 00:15:34 Nothing to do right now, copy it into the burn down for the beta involved.
Felix Geisendörfer 00:15:39 Yeah, so I agree with adding it to the…
Jonathan Halliday (IBM) 00:15:41 It was beautiful.
Felix Geisendörfer 00:15:42 burndown, can you… can you do it? I think you can add.
Jonathan Halliday (IBM) 00:15:44 Yeah, yeah. Okay, awesome, great.
So the second one is just a heads up, async Profilers doing a metadata API, span API, so right now, the thread context stuff we have is looking at how do we do this externally.
But for some languages, the profiler's in process. That's certainly the case with JFR and async Profiler for Java.
There, it's an API problem.
How do we… Use the, the profilers.
exposed API surface to pass down.
thread context.
So async Profile is adding a span API, and really it's just there as, Java people should take a look at this and, I want to try and head off the problem where they… they put out some API, and we try to use it, and it doesn't… Like, fit the, the use case we've got, Sort of unified ecosystem here where we can interop, so, If, for example, you've got the hotel.
Trace SDK, and you've updated things in there. It's already got hooks. It would be nice if Tracing Profiler could use those hooks and… Copy the new chase state down into its own internal state so that it gets serialized as part of the the JFR file that, will be written out by… async Profiler.
And then also, of course.
how that manifests, it'll probably look like a Subway JFR event, so the code I have the Java SDK that reads JFR files back.
and translates them into our OTLP format.
We'll need to understand how Async Profiler is encoding spans there, and Translate that back into link elements in our… OTLP.
Felix Geisendörfer 00:17:50 Yeah.
Can you maybe touch just on a high level, was it?
the details… They're introducing, basically, the concept of spends in the same way.
Jonathan Halliday (IBM) 00:18:00 Yes, it has…
Felix Geisendörfer 00:18:01 But it's not for distributed tracing.
Jonathan Halliday (IBM) 00:18:02 It's very conceptually similar to a Spanning hotel, you know.
Beginning to year, end of year.
I haven't looked at the details, because I've been on vacation, so that's in my backlog of… Basically, go read the proposal, go look at that code, and make sure that it's going to interop with what we have.
I just want to avoid.
Felix Geisendörfer 00:18:23 Yeah.
Jonathan Halliday (IBM) 00:18:23 The case where they publish something that's incompatible, and we've got this kind of fragmented ecosystem, and we have to scramble to try and bridge things somehow. It would be much cleaner if we can get in early and say to them, hey, look, It would be great if you could tweak this in this way.
I don't know, it might work already.
I get the impression the async profile of people aren't really deeply into To hotel stuff, so it's… it's worth someone who is taking a look and… Checking it out.
Felix Geisendörfer 00:18:55 Well, are you suggesting you can do it.
Jonathan Halliday (IBM) 00:18:57 I'll try to get to it, yes, but if there's other Java-adjacent people on the call who would like to take a look as well, that would definitely be worth it doing. The more eyes, the better, I think.
Felix Geisendörfer 00:19:17 Okay, cool, then I'll capture this as an action item for now.
Okay, any more thoughts on this, either from… You, Jonathan, or anybody else?
Jonathan Halliday (IBM) 00:19:36 Nothing else for me, that's, that's all I've got. I'm still playing catch-up.
if there's things people are expecting me to do that I haven't done, please ping me again, because I've been away for a week on vacation, and… Yeah, the inbox is a mess.
Felix Geisendörfer 00:19:52 No worries, I think you're good.
Okay, then… If there's no more thoughts on this one, then I think rhetoric can take it away with talking about process context implementation.
Frederic Branczyk 00:20:07 Well, so, basically, I, finally took the time to open all the, issues for all the SDKs, and while doing that, I kind of realized that, you know, Go is sort of a special case in terms of, you know, what we typically call thread context, right? Because we grab the Go labels directly, and so… First, like… I wanted to make sure that there's consensus here with… that we don't… Plan to implement thread context for Go, right? Like, I don't see a reason why we would, but I just want to make sure that we're, kind of aligned. And if that's true, then what exactly does that mean for, process context.
And I… because I have not been able to pay too much attention to it, I just wanted to, I guess, raise it for Evo.
We should make sure that, you know, all the things that relate to Thread context is optional, in process context, if it isn't already, like, I'm just saying that, you know, I haven't been able to, pay much attention to it, but, like, for example, the label definitions or whatever, they're obviously disconnected here, right? Like, because go labels, specify the full key and value.
Directly. So I just wanted to bring that up and make sure that, you know, we've thought about this.
Just because I realized there was a slight inconsistency in the world here.
Ivo Anjo 00:21:48 Yeah, I can… I guess I can… can… can share a bit here. So, So yes, like, I would expect Go to have… still have the process context, but not the thread context, and actually, we've been kind of implementing this on the Datadog SDKs to make sure that there are no unexpected problems, and to test this, and whatever.
And we do… we kind of already have this, so DD TraceGo, the Datadog SDK for Go, does have process context and not thread context for the reasons that you're saying.
And the way that we envision this in terms of, like, the keys and wherever, is that in the thread con… in the block that configures the thread context, there's, like, a field that is called the… the schema version, and what we would… what I was thinking, I'm not sure if we put that down in the document, maybe we should, is that we would have… a schema version for Go that is kind of different, and so, like, an external reader can kind of see, like, oh, this is Go, and so if you're in the Go schema reader, you know that you need to use the Go code path, and in particular, you would not have the dictionary in no keys, because you're, like, in Go.
So the keys would only be there if you're in the, like, generic format or something like that.
Frederic Branczyk 00:23:06 Sounds good. I guess then we're aligned with, let's make sure that we write this down.
Ivo Anjo 00:23:13 Yep.
Felix Geisendörfer 00:23:17 Eva, is that the action item you'll take?
Ivo Anjo 00:23:19 Yeah.
Yes, I was going to say that, yes, I can take an action item to make sure that we have this in the OTEP PR.
Frederic Branczyk 00:23:28 Perfect. Okay. I imagine Go is not gonna be the last… one that's a special case. I know for a fact already that, like, V8 is gonna be at least slightly special.
Ivo Anjo 00:23:42 Yes, and in the… since we're also experimenting with the V8 version, the thinking is that for V8, it would be kind of similar, so we would have, like, a schema version that is, like, specific for Node or V8.
And then, I think for V8, we're also thinking of having the keys, but kind of like each schema that we might have that needs additional… for VMs that The generic mechanism, for some reason, cannot work.
we would have, like, a variant here. Ideally, we wouldn't have, like, have one for each runtime, so as much as possible, try to push to adopt a generic format, but in some cases, we can't right now change the runtime, so if we can't change the runtime, we can only change ourselves.
Frederic Branczyk 00:24:29 Sounds good.
Felix Geisendörfer 00:24:34 Okay, cool. Any other thoughts on this topic?
Going once, going twice… Then we are moving on to Mattia talking about GPU profiling.
Mattia Meleleo 00:24:49 Hello. Yes, I wanted to talk about GPU profiling. I wanted to ask, If there is, like, appetite or willingness to have GPU profiling in the profiler.
And yeah, I also made a POC, which I will leave in the chart.
Felix Geisendörfer 00:25:14 Can you actually add it to this document, or maybe so?
Mattia Meleleo 00:25:18 Yeah, maybe it's better to add it to the document as well. One second. I will add it later. So, I wanted to ask also what are the best… if there is appetite, what are the best next steps? So, should I open an issue and an umbrella issue and track it?
Should we… Should I split it in, like, multiple small PRs? What's the best way to… Go for it.
Frederic Branczyk 00:25:47 I should… I should also say that, I mean, I've mentioned this in past meetings, but we… we actually just yesterday open-sourced our, or launched our, like.
PC sampling, feature for NVIDIA CUDA as well, which is already open source, and we've always intended to contribute it to this project, and we've already done quite a bit of the groundwork to make this happen.
like, Tommy… Tommy and Brennan have been working on this. So, like, a bunch of things about, like.
you know, when we… how we discover that, you know, like, CUDA was loaded, or whatever, because it's always loaded via DL Open, all of these things, we've already implemented a bunch of the groundwork as we've been kind of going through this project. So, we fully intend to… contribute our implementation anyways. So, you know, happy to kind of work on that together as well. But there's definitely a bunch of, like.
groundwork that still needs to happen.
To make this work. And also, of course, you know, if you took different approaches to what we've done, I'm happy to reconcile that as well.
Mattia Meleleo 00:27:06 Yeah, let's, maybe we need to, to compare, to compare and see what, what are the differences. By the way, I read the blog post just one hour ago. I found it on LinkedIn by, by chance. And, yeah, I've also discussed with, with Tommy, I think, I think it was more than a month ago.
About, about contributing the USDT groundwork to the Silium library.
But I think that that one is, like, kind of lower priority for now, since you have already done the big job of doing the library by itself.
So yeah, I think, I think for next steps, we… we should, compare both of the implementations and see… see what's… what's… what's the best, the best way to proceed there? Maybe we should create an umbrella issue as well.
Frederic Branczyk 00:28:01 Yeah, that sounds good to me.
There are definitely lots of different paths that one could take. There are lots of trade-offs here as well.
Mattia Meleleo 00:28:16 Yeah, the NVIDIA ecosystem is… is crazy. It's very convoluted.
Frederic Branczyk 00:28:22 Tell me about it.
Felix Geisendörfer 00:28:27 Okay.
Yeah, sounds like the two of you can follow up on CNCF Slack or on GitHub, and figure this out, but yeah, thank you so much, Mattia, for offering to contribute in this area, and I think everybody on the SIC is aligned that having GPU profiling in the eBPF profiler would be really nice, and as Frederick mentioned, they have interest in contributing what they've done so far as well. So if the two of you can.
Mattia Meleleo 00:28:51 Nice.
Felix Geisendörfer 00:28:51 figure out how to align that, that'd be awesome.
Mattia Meleleo 00:28:54 So…
Felix Geisendörfer 00:28:57 Cool. Any other GPU comments while we're at it?
Going once… Going twice, then… The next one is… a different thing called .NET, and Matthew has some thoughts on that. Go for it.
Matthew Hensley / Grafana Labs 00:29:17 Yeah. Hi there, one of my colleagues asked that I come share some background and context.
Since they weren't able to make it today, But, saw this request come through, like, an hour ago, and… I want to give some, like I said, some background here about some of the difficulties that the SDK is going to face here, and there's going to have to be some design work. So, it's all fairly straightforward, but, on .NET, especially older .NET versions that are Windows only.
You can only attach one profiler.
But profiling is also how the zero-code instrumentation works today.
And so there's… Not necessarily going to be that slot available, to attach a profiler. So… there's that already, but also in the SDK, there's not much appetite right now for adding C or C++.
Into the codebase. Right now, it's all C-sharp, all on the managed side.
So… And then, where it gets real fun is there's multiple generations of the profiler, so they're usually additive, and they build on each other, but there's a lot of versions of .NET that are still in scope for support, so I think right now there's something like 15 minor versions, and across that, like, 5… different profiler implementations or so, and there's a lot of overlap between them, but there's gonna have to be a whole lot of design work there, and… Specifically.NET Framework on Windows, which we have lots of customers using, is going to require some cooperation between the SDK and Zero Code Group to figure out exactly how to get it implemented, so…
Felix Geisendörfer 00:31:05 Cool. Yeah, thanks for the summary, I don't know if anybody here has particular thoughts on how .NET profiling should do in the CC++ parts. Obviously, that seems like a… limitation that would be annoying for this kind of work. Maybe there's… I don't know if there's a path towards maybe having a separate library that provides profiling that can… take a different appetite and risk for when it comes to CC++. I don't know how feasible that sounds, and maybe something could be done in the main .NET SDK to make that harmonize, especially when it comes to trace context propagation and things like that. Does that sound maybe like a pass?
Matthew Hensley / Grafana Labs 00:31:46 It's possible, but because the zero-code instrumentation has to be implemented as a profiler, especially for older .NET versions, it gets… So there's already, like, a partial profiling implementation, out there.
And so figuring out where to draw the line, and is there gonna be just, like, a dedicated library just for SDK users, versus… a different implementation for Zero Code.
It's going to be, gonna be an interesting one to have to figure out here.
Christian Simon 00:32:22 I might misremember that, but I think the zero-code implementation, isn't that also based on a fork of the Datadog tracer profiler, which is in C++?
Matthew Hensley / Grafana Labs 00:32:33 Yes. It's, a very old fork, from, like, 2023, I think.
Not earlier.
Felix Geisendörfer 00:32:46 But, doesn't that imply that there is C++ usage now in the SDK from that, or… Matthew Hensley / Grafana Labs 00:32:53 So.NET's, maybe a little different from some of the other, instrumentations out there. The SDK and the Zero Code project… so the Zero Code project uses the SDK, but it's definitely a superset, and… It adds all kinds of… things, like profiling. The SDK today, because of how .NET works, can't do things like dynamic rewrites of dependencies.
And that's what the zero-code instrumentation has to do. So, it's implemented as a profiler that can intercept library loading and do all kinds of fun things to wire instrumentation automatically.
Felix Geisendörfer 00:33:37 Okay, so… I didn't realize that the zero code thing was a separate project that's sort of wrapping the .NET SDK that… Good to understand.
Yeah, I mean, I don't have strong thoughts or opinions here, because I'm not very familiar with the .NET ecosystem in general, and not the hotel one other for .NET.
But yeah, any… anything we can do as a SIC to maybe help? I don't know if we have anybody on the SIC who's specifically familiar with .NET. I have a colleague who, who knows . Who's working on .NET, who actually works on the… net profiler for us, I could ping him, and maybe, especially if the serocode instrumentation stuff was a fork of Datadoc stuff eventually we could chat about.
ideas of… what we could do there, but yeah, I don't have the expertise to comment myself, but I can certainly mix that connection if it would be useful. Matthew, what do you think?
Matthew Hensley / Grafana Labs 00:34:34 Yeah, I think the SDK SIG would be interested.
And that, and I'm sure the Zero Code folks, too. As much as anything, just wouldn't… To come and just provide some background that this is not, like.
Just a quick and easy implement it.
for .NET, because of… Some weird constraints as far as, like, how the projects are arranged, but also technical limitations with the runtime.
Frederic Branczyk 00:35:08 I think…
Felix Geisendörfer 00:35:09 Yep.
Frederic Branczyk 00:35:10 So, sort of, sort of a meta, meta statement.
not that, like, in-process, like, CPU profilers are not useful. Obviously, they're definitely, like, also the only choice in some contexts.
But I would say SDKs should probably, if they implement each of these kinds of profilers separately, they should probably focus on, you know, things that we can't grab with the ePPF profiler ever. Again, I realize there are, like.
like, serverless, etc, where, you know, having the eBPF profiler is effectively impossible, but I think if SDKs try to prioritize here, they probably should focus on the things first that the eBPF profiler is likely to never be able to Capture.
Matthew Hensley / Grafana Labs 00:36:07 Yeah, I'm not gonna be surprised as this gets shaken out, that there's gonna be some limitations like that.
You know, just grab what… we can, in the best spot possible. And I saw in the chat a question about eBPF on Windows. It's like, Microsoft has that project in progress, but… There's… it's not even signed where you can run it without making serious changes to a… install, so it's… They have no timeline. It'd be awesome if they would actually make eBPF on Windows real, but I don't think that we're gonna see it anytime soon, and it's gonna be runtime-specific APIs for the foreseeable future.
Felix Geisendörfer 00:36:53 Yeah, you will go, and I'll queue myself up after you.
Ivo Anjo 00:36:58 I have a question that kind of came up out of curiosity. I usually think about this in a very pragmatic way, and I know that there are many ways of thinking about this. This to say, do you think there is a world where we could say, oh, we only support profiling on Linux, on the latest, NET Core, and we say, like, okay, if you're on an older one, we just don't support it, or do you think this kind of features, this kind of integrations, we would only have them in the hotel.NET SDKs if we can say, like, okay, we can… we support this across all of the supported versions from the hotel SDK, and there is no kind of carve out of saying, like, oh, this feature is only for some runtimes on some OSes, yeah.
Matthew Hensley / Grafana Labs 00:37:48 I think long-term, it needs to support, all of the runtime versions that are covered by the SDK, whatever is possible, especially because the Windows-specific .NET framework is still in heavy use, and doesn't have an end of life. I think the earliest it'll be end of life is 2040, right now.
So, there's gonna be this going on for a long time, and We have lots of end users that we talk to regularly, and they are running Windows .NET Framework apps at huge scales still, and frankly, can't migrate to the modern runtime just because of the size of their codebases. Just… it's not a… Practical project for them with how long it would take, so… That's one of the big concerns here, especially, it's like, oh, for modern .NET, having, you know, the zero code, and then having a profiler that cooperates with it is not a big deal, but for the older runtime that's still in heavy use, it's just… that's not a thing that exists there, and it's not going to get added.
Felix Geisendörfer 00:38:58 Can you clarify why you think that long-term profiling would need to be supported by all versions? Of course, like, it's ideal, but at the same time, like, it's better to support for some versions than to just say it's all or nothing, right? Like, this is just the goal that you would like to see, or is it a strict requirement?
Matthew Hensley / Grafana Labs 00:39:17 Oh, I mean, I get asked probably once a week, every other week, from Get Customer Requests, asking about… NET Framework Windows profiling support, so there's a lot of demand for it, and especially, if you think about it, and it makes sense, the people who are on the latest versions of the runtime are the ones that have the most ability to make changes. They could adopt whatever, and some of these older applications, even, like, doing a deployment and a build is a struggle, so having Being able to attach a profiler to an older application and get some insights into it is… Really important for them.
Felix Geisendörfer 00:39:57 Okay, I get it, that makes sense. Question out of curiosity, are all these applications also deployed on Windows, or some of that stuff on Linux as well with .NET Framework?
Matthew Hensley / Grafana Labs 00:40:08 NET Framework is Windows only, and then .NET, now the only versions supported are 8 and higher, are cross-platform. They run pretty much everywhere.
Felix Geisendörfer 00:40:25 Okay, so eBPF is not an option for .NET Framework at all. It only becomes sometimes an option for, .NET… what did you say, 8 or later?
Matthew Hensley / Grafana Labs 00:40:35 Yep.
Felix Geisendörfer 00:40:36 And so, yes, I guess we do need an answer that's not eBPF for… 4.NET Framework. Okay, that makes sense. Cool.
Any, any other thoughts or questions here?
The one comment I had that I just remembered.
when the profiling SIC is, like, pinging folks working on the SDKs, and we're suggesting, like, profiling being implemented, it's not like we're… requiring you to, like, stop everything and, like, do this right away. It's just, basically, we wanted to let SDKs know that we're now at a point where if SDKs have bandwidth to do… start thinking about this work, that we would appreciate it, and we're happy to collaborate, but it shouldn't be seen as, like, a… A, like, you have to do this, or something, like, just in case that wasn't clear.
Matthew Hensley / Grafana Labs 00:41:32 Oh, no, totally, just wanted to go ahead and provide some early context that it's gonna take some time to design this one, but there's a lot of interest in Finding a solution here, especially for the older runtimes, so… But, Tim, just wanted to… get a generic, we'll look into it, reply. There's a lot of practical things that are going to have to be figured out, and some folks here can undoubtedly help, since we have colleagues, like I said, that have worked on similar aspects of this already for .NET, so…
Felix Geisendörfer 00:42:06 Yeah, I will certainly ping my colleagues. Where would be the best place to start chatting with the right folks? You mentioned the SDK big. Also, I guess, this issue, maybe, to start the conversation there, or… Matthew Hensley / Grafana Labs 00:42:21 Yeah, that issue's fine. The zero-code folks, keep an eye on that, too, and we'll see it.
Felix Geisendörfer 00:42:28 Okay, and I'll point the .NET folks to the meeting notes and the recording later, so they can catch up and chime in.
Awesome.
Sweet. Thank you so much.
Okay, we are now out of official agenda item, but the fun is not quite over yet, because I think I saw Lexi joining, so we can certainly circle back to the action items.
That we skipped over earlier, and in the meantime, it's maybe shaping up to still have some time left at the end. If anybody thinks of a last-minute agenda item, feel free to add it right now.
But let's circle back to Alexi's items. Add duplicate and orphan checks for the conformance checker.
Alexey A 00:43:12 No progress on this one.
Felix Geisendörfer 00:43:16 Okay, no worries.
What about the next one?
Alexey A 00:43:23 I… yeah, there was… there's a comment… there was a comment on DPR that I addressed locally, but need to send it, but as I was updating it, I actually wanted to discuss this a bit more.
I think the discussion… So, basically, the discussion was around whether… whether period is optional or not, and what are the semantics when it's specified, and people… last time, people pointed out use cases when So currently, when we describe the shape of values and timestamps.
We say that if you only specify timestamps.
That means the, weight of 1.
But I think last time when we discussed it, Frederick, correct me if I'm wrong, but I think you mentioned that, like, there's also semantics where consumers may assume that it's not 1, it's actually the period type.
Like, if you, if you specify the period, because, like, if you want to have fixed weight.
For your events, and you also want timestamps.
Then you might specify just the timestamps.
and count that as the, like, actually, like, the weight of the period. The question is… Yep.
Frederic Branczyk 00:44:38 So, basically, the case where I see this happening is when sample type is count of something, sorry, is count of occurrences, right? Like, count of samples, and the period type is… CPU nanoseconds, that's, like, the classic one, right? Because then one is equivalent to 1 over the… or the sampling frequency, right?
So, yes, exactly.
Alexey A 00:45:13 Yes, yes, because, And an alternative would be you would have… you could have sample type that is, like.
Like, why not specify the values in the, in, like, specify values and timestamps? I'm just, just curious, like, why… Is it, is it, like, to save space, to basically avoid repeating, repeating the number?
Felix Geisendörfer 00:45:37 Yes, I think this was only, included in the, like.
proposal for how this should work because of this idea of saving space, when it's really redundant. Like, if you would always encode the same value, that's completely redundant, right?
So that was the thought behind it. So it would be nice to retain that, but if it becomes a huge complexity source, I think that could be revisited, especially since compressors should be able to compress this pretty efficiently. But.
Alexey A 00:46:08 I'm… I'm more like… I'm more like what we want to document, because, like, I started, like, I wanted to type something, like, oh, and it's one, or if period type is specified, like, what are the exact conditions? So I'm… But it, like… I wonder, like, what the high-level agreement from this group is, like, this is a valid use case, and… because currently the documentation… our documentation doesn't reflect it.
We say that if the value is missing, then it's the weight of 1.
Frederic Branczyk 00:46:41 I think, I think this, this, like, this whole concept.
Doesn't just apply for timestamp only. Like, it applies just as much for counting occurrences And then multiplying those occurrences by the period.
Felix Geisendörfer 00:47:01 So what you're saying is, like, let's say you have a mutex contention profiler, which has, like, a sampling rate of 1 in 100, and you would somehow want to express the sampling that's going on there using the period? Is that what you're hinting at, or…
Frederic Branczyk 00:47:17 Are you asking me right now?
Felix Geisendörfer 00:47:18 Yeah, yeah, I think so.
Frederic Branczyk 00:47:19 No, I'm, like, giving the example, like, I just wanted to make sure, because Alexei always talked about timestamp and the weight being 1, right? I'm trying to say that, like, when I say that like, the period value being important, I don't see that just in the context of timestamps, but also in the context of, you know, the value of the count is, I don't know.
300, right? Like, whatever, however often you've seen this occurrence, and the consumer may still want to multiply the occurrences times the period, right? Because that reflects the total CPU time, for example.
Alexey A 00:48:00 In that case, you are not even… in that case, you are not even saving space, correct? So you could.
Frederic Branczyk 00:48:07 That's correct. We happen to support this, because customers produce all kinds of data. And, like, counting tends to be a little bit simpler than, you know, knowing what the sampling frequency is in whatever place that you're doing the counting.
Alexey A 00:48:25 Okay.
Felix Geisendörfer 00:48:28 It's going…
Alexey A 00:48:29 Oh, sorry, Felix, go ahead.
Felix Geisendörfer 00:48:31 Yeah, but I think going back to my previous example, I think your answer was sort of a yes.
to my question, I think you're saying that the period can express the fact that there's sampling going on, and knowing the period allows you to take the counts that are in the samples, which are the sampled values, which are not all the occurrences, and then you multiply by the period to get the real occurrence.
Frederic Branczyk 00:48:55 Yes, yes, yes.
Felix Geisendörfer 00:48:56 So.
Frederic Branczyk 00:48:56 Yep.
Felix Geisendörfer 00:48:57 Okay, I think we're on the same page. I'm trying to remember… I think this is kind of annoying for compatibility with, for example, Go, because I think Go always already extrapolates.
So…
Frederic Branczyk 00:49:13 both.
Felix Geisendörfer 00:49:15 dispose.
Remind me.
Frederic Branczyk 00:49:17 the CPU profile contains both.
Felix Geisendörfer 00:49:20 Yes.
Frederic Branczyk 00:49:21 It contains the sample type count and the sample type CPU nanoseconds, and the CPU nanoseconds is just the count multiplied by the period.
Felix Geisendörfer 00:49:32 Yeah, I was thinking about other profile types, like, for example, the matrix profile. I think they actually, already upscaled the values that they put on the sample, so the sample values are the real occurrences, and you kind of have to know the sampling rate if you want to get back to the… how many samples were actually taken.
So, we sort of need to agree on one there, because it can't be both if we want to assign strict semantics to this.
I mean, you can convert between the both, so it's fine, but we need to agree on which one it is. Like, either the… what's in the samples, the values, or the… Sampled occurrences, or they are the, yeah, upscaled occurrences in.
Frederic Branczyk 00:50:15 Well, it depends on what the sample type is, no? The sample type describes that.
If the sample type is a count.
Then you are allowed to multiply the count with the period.
Felix Geisendörfer 00:50:31 I'm saying that's not what the GoPro files do, I think.
I think for the Go profiles, you would do it the other way around. You would take a look at the sample values and divide by the period to get the sampled counts.
Frederic Branczyk 00:50:45 I didn't know this off the top of my head.
Alexey A 00:50:47 I, I think… I think high-level options are… First… the first one is come up with an approach where there's either always multiplication, or there's always no multiplication.
Felix Geisendörfer 00:50:59 Yup.
Alexey A 00:51:00 The second one is encode in this schema in some way, whether there is multiplication or not. I don't know, like, boolean flag in sample type, convention on the name, I think Frederick mentioned, like, oh, if it's count, then you multiply. If it's not count, then you don't multiply, but some sort of that schema.
And third, say that it's, like, up to consumer, somehow, magically, figure out whether the multiplication should happen or not.
I think this is kind of, like, the solution space that we… if there's… if I missed anything… And I think, like, third would be my least preference, because… Well, maybe it's fine, like, I'm just, like, just saying, well, the consumer will somehow figure this out. That seems too… too brittle. People will just come up with their own local conventions, and it's… and it will be, like, one or two, just, like, in a hackier way.
So I think, like, realistic choices between either 1 or 2.
Frederic Branczyk 00:52:04 My preference would be 2, as long as we don't find existing conflicts in the wild, like in the GoProfiler. I don't know… like, I know for a fact what, like, CPU profiles look like, I'm not 100% sure about all the other ones.
Felix Geisendörfer 00:52:24 Can you remind me what option 2 was, and option 1?
Frederic Branczyk 00:52:27 It's that if sample type is count, Then… The consumer is allowed to do multiplication.
Felix Geisendörfer 00:52:39 That's option 1 or 2.
Frederic Branczyk 00:52:40 That's option 2.
Felix Geisendörfer 00:52:42 If sample type is COUNT… Consumer should multiply by a period.
Right?
Frederic Branczyk 00:52:51 Yep.
Alexey A 00:52:51 Yeah, option one was figure out, like, whether we always multiply, or we… like, if period, for example, like, if period is present, then always multiply, the, the sample type in that profile. Or… don't always multiply. Basically, option one is, like, no conditional logic, just define, like, it's one way or the other always.
Felix Geisendörfer 00:53:14 Yeah.
Frederic Branczyk 00:53:15 Option one is the producers have to produce The upscaled version already.
Felix Geisendörfer 00:53:23 I am probably slightly leaning towards that, because I think that's what the users want, and… making it easier to deliver what the users want to see in the end, is probably the right thing to do, because a lot of tools are going to forget to do this little multiplication, even if we write it in the spec, and so if we just make it so that by default, displaying the value from the samples is meaningful, I think that's strictly better.
But I could be convinced otherwise.
Frederic Branczyk 00:53:54 I don't feel terribly strongly. We've supported it because customers have written data In Option 2 way in the past, and actively do.
But if we… if we make that very explicit, then I don't feel… I don't feel too strongly.
For what it's worth, option 2… Can get really… Yeah, can get kind of complicated when you have… when you want to, for example, compare profiling data at different frequencies. Like, we have… we have some customers that essentially, Profile at very high, or, you know, comparatively very high frequencies in, like, cannery, environments, to be able to build, like, statistical significance very quickly to compare to production, for example.
And that gets… you know.
That would be completely wrong if you… Don't multiply by the period.
Felix Geisendörfer 00:55:02 Yeah.
I think another reason for letting the consumer upscale is that it's sometimes not trivial to do the upscaling, it's not a simple multiplication, so for example, the Go Memory Profiler would be a good example, because it does this sort of sampling by setting exponential sampling points, and then the inverse of that sampling mechanism to get back to the true sample counts is actually a little bit more complicated equation than a simple multiplication, and I think if we… Assume that it's always as simple as dividing by some number, then that's maybe overly simplistic for some more sophisticated sampling techniques.
Alexey A 00:55:44 this… this includes the timestamps case, right? So, for example, for CPU profiling, you will, like, if you want timestamps, you will repeat the same large value multiple times.
Felix Geisendörfer 00:55:56 I was talking about memory profiling right now.
Alexey A 00:56:00 Okay. I'm talking about, like, any fixed weight Sampling, like, profiling, where you want to capture the timestamps.
Because our… our current default is 1, so if… if your sampling weight is not 1, then you have to spell out the value explicitly multiple times, correct?
I'm fine with that, I'm just… I'm just… I'm just… I'm pointing this out as a case where I think people who want to capture timestamps might be most opinionated about, like, oh, I don't want to, like, why do I have this redundancy? We can… our answer could be, oh, well, decompression will fix that.
Felix Geisendörfer 00:56:44 Yeah, I actually need some time offline, I think, to look at this more to form a strong opinion, because I think it gets a little tricky, like, discussing the timestamp case versus the non-timestamp case. At least, right now, I feel a little confused.
But I think it's important that we sort of write this down cleanly and agree on what we want to do here, even if we might not manage to do it in the last couple minutes here.
Frederic Branczyk 00:57:10 I also… actually, I'm… maybe I've confused myself now. Just because we keep saying the consumer does the multiplication, even an option But no, in option one, producers don't do the upscaling, and consumers never do any multiplication. Okay, sorry.
And yes, I also think the timestamp case is… Weird.
It's not.
Felix Geisendörfer 00:57:38 Again, I think, just to be clear, if we can make everything simpler and easier to understand by just saying, hey, spell out the value every time, even if you use a timestamp, I would be open to that. It's sort of nice to not have redundant values encoded over and over again, but if we could make our life easier, I would be open to it.
Frederic Branczyk 00:57:55 I think I agree.
Alexey A 00:57:59 I'm… one thing I'm curious is, like, what is confusing about the timestamp keys, because to me, it's kind of just the same value unrolled into… into two arrays, where currently we say you can also skip the values if it's one.
I'm… I'm… I'm asking… They're trying to see if I'm missing something.
Frederic Branczyk 00:58:21 I guess I'm trying to say that we're then implicitly saying that A consumer needs to look at the period value to determine the timestamp value.
Alexey A 00:58:40 I think what we are leaning towards is that we will say that The consumer should put that exact value multiple times in the…
Frederic Branczyk 00:58:50 That I'm okay with. I'm saying if we don't do that, then it gets confusing. Yes, I agree.
Alexey A 00:58:58 Well, then I have a question why the case of 1 is special, but this is.
Frederic Branczyk 00:59:02 Well, that's… I agree. That's why I'm saying it would be confusing if we keep it that way.
Felix Geisendörfer 00:59:09 Yeah, I need to go back and read what we have in the spec right now, as well as what I wrote originally when I proposed this, because I feel there might have been something that got lost between the two versions of this. So, yeah, as I said, I'm currently too confused to have a strong opinion, but I agree, we should look into it.
Okay, yeah, I'll definitely take an action item to look into it and comment.
Any… so I think we have, like, 2 minutes left. I don't know if there was any last-minute additions here. If not, we can maybe… Get back a minute or two.
2-hour day.
So yeah, unless somebody has some last thoughts, thank you, everybody, for joining, thank you, everybody, for the good discussions and all the work, and have a nice local time.
Frederic Branczyk 01:00:09 around.
Ivo Anjo 01:00:09 Thanks, everyone.
Frederic Branczyk 01:00:09 Right.
Marc Sanmiquel 01:00:10 Thank you.
