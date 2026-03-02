SIG: Profiling WG
Date: 2025-06-26
Duration: 61 minutes
Zoom Recording URL: https://zoom.us/rec/share/0WKp0bOOv0EF9fIcTA6gR_xA9do0aBUnoKMmEZrL_1n2TtmYmkyclkf1JfNZENM0.cdVDtHuPqCtvpxr2
============================================================

## Zoom Recording Transcript

Felix Geisendörfer 00:03:42 No.
Frederic Branczyk 00:04:41 Hello!
Felix Geisendörfer 00:05:12 We give it another minute or so, but might be a smaller meeting today.
hey? I guess we're 5 min in. So maybe let's get started.
If anybody feels like moderating other than me. Raise your hand. If not, I probably made some mistake, and spoke up so
willing to accept my fate.
okay, then let's get started everybody should have link to the meeting notes. But if for some reason not, I'm dropping it in zoom.
and we're gonna go down the agenda. If anybody is here who's thinking about an agenda item, but hasn't edited yet. You should probably go for it like, for example, I saw Jonathan. You had a message in
hotel profiles from 3 days ago, or something that hasn't gotten replies. Yet. If you wanna bring those up, feel free to add it to the agenda. If anybody else can think of think of something, please add it now. The 1st item, however, is pretty clear. We're gonna review previous action items.
so the 1st one is revise any current use of optional and the pro don't get rid of remaining ones. This one says it's awaiting review. So
and it is actually merged.
That's awesome. Yeah, thank you. Jonathan, for raising that. And everybody who reviewed and get it merged. I think we can check this one off.
I'll I'll move it to the archived action items later, or if somebody else can do it be great.
So then there's a second one that's called done. But let's see what that is about, returns.
Jonathan Halliday (Red Hat) 00:07:58 That's the spin off from the one we just closed.
Felix Geisendörfer 00:08:01 I see? I see. Yeah, should we should we? Is there a discussion you wanna introduce.
Jonathan Halliday (Red Hat) 00:08:07 No, I mean, it's very straightforward. It's just a doc improvement to say that we're
specifying that all the dictionary fields should have a a 0 element
beginning, regardless of whether we actually need it or not.
which is kind of defensive at this point. If we evolve the specs so that we want optional fields into the other ones. At least, we've got some consistency and can do that whereas we don't do it. Now, when people start using the 0 slot for the things
we're not going to be able to fix it in the future.
Felix Geisendörfer 00:08:45 okay, I think that makes sense to me, I'll give it a closer read, but yeah, basically this just needs reviewers, right
okay.
that's what it means. So yeah, everybody who who can refuse this in the next couple of days that'd be great. I'm adding a list something to my list.
Yeah, unless there's a question about it, I think we can
carry on. I'll just update the action item to say, review, pr.
the next one is alexei had an item for writing a proto consistency check tool library. Any updates on that, Alexei, I think you're here today, right.
Alexey A 00:09:35 No, no progress on this one.
But I'll I'll keep it.
Felix Geisendörfer 00:09:46 No worries florian has 6, 4, 9 up
Florian Lehner 00:09:53 Yeah, not much progress
Still waiting for a few more, refused to get it merged or approvers.
Felix Geisendörfer 00:10:03 I think technically, we have enough. Right? We have 2 approvals. Or do we need.
Florian Lehner 00:10:07 In this case. Yeah, yeah, yeah, yeah. I can now start ping, the specification sector.
Felix Geisendörfer 00:10:15 Right. So I I guess at this point it's more like a last call. If anybody disagrees with what's in this pull request. Raise your voice now, or have a more difficult time undoing those decisions later.
Florian Lehner 00:10:26 Yeah.
Alexey A 00:10:28 I'll see. I'll take a look today.
Felix Geisendörfer 00:10:31 Awesome. Thank you.
my action item, I have not progressed on, but I think we actually have an agenda item, or if we don't I want to have an agenda item about stack trace representation? I'll add it to the bottom, because last time we had conversations that requires feedback from you, Alexis, so maybe it will.
We'll do that
Christos Kalkanis 00:10:51 Yeah. So should we address this now? Because I think it's prudent to to get this wrapped up at this meeting, and not because it's been delayed for a couple of weeks already.
Felix Geisendörfer 00:11:00 It.
Christos Kalkanis 00:11:00 And yeah.
let's let's do this first.st I mean, because it also falls under previous action items. It's something that we left unresolved.
Felix Geisendörfer 00:11:08 That that may. I'm totally fine to go. It could go a little in depth, depending on whether the conversation leads us, but I think we should make time for it. So let's do it now. Do you want to introduce, or should I, Christos?
Christos Kalkanis 00:11:20 Yeah, I I mean, so we've been examining alternative stack based representations for some time now. So Felix and and Florian worked on a proposal. Alexi worked on on a different proposal.
I wrote some benchmarking code to to do some runtime benchmarks to see you know where we are in terms of wire overhead.
both the pre compression and post compression.
So if you look at the the agenda that the pull request is in the Epf profiler repository. All the data is there. You can actually run it yourselves with alternative workloads and see if it fits your scenarios.
But based on the data we have so far, it seems that like if Felix's and Florence proposal is the way to go which introduces a new message called stack and it groups locations together. We're getting rid of the the slice indices array for location indices. And we just keep the single location table.
Yeah. So I mean, my recommendation would be to go with that.
It's it's simple. It's slightly better than what we have right now, if we deduplicate locations which the upper profile is not currently doing.
But I have a draft pull request that's going to to address that.
And then, Alexis, proposal is always better. If compression is not used and that uses 2 integer arrays, it's it's a platin, 3 representation
but post compression. I haven't found a single workload that that it performs better than the Felix's employees proposal. And it's actually, can. It can get more than 50% overhead
compared to those. If the workload has a lot of redundant traces, so the more redundancy, the worse it performs with compression.
So unless we have scenarios where we cannot use compression. Yeah, I would say
we should go with Felix's proposal. And if there are such environments where compression cannot be used, maybe we could consider Alexis as an as it's something we could additionally support. But not this. The only option.
like an alternate encoding.
Alexey A 00:13:35 That sounds good to me going with the Felix's proposal. I I think it's if there are no like obvious.
I would say, like order of magnitude.
Whatever base we use, 2 x or 10 x no obvious wins. Then just like a like a separate separate message for stack. That is just like flat representation of stack. I think that's also like definitely easier to grasp, I think.
And for a protocol such widely
that, like we? We hope that will be as widely used as as open telemetry. I think it it also.
I think simplicity is also an argument for just like being able to easier consume the consume the Api.
because, even like my proposal like I,
it's like, it's it's nothing like
super complicated, I think, but but a few people when they looked at it. It was obvious from the feedback that it's not immediately
obvious, and which is probably also means that it's more. It's more error prone. So yeah, let's go with the with what Felix proposed.
That's just from my feedback from my side.
Felix Geisendörfer 00:14:46 Cool anybody here who is still unconvinced, who wants to bring up more challenges? Or should we plan on trying to get that landed? Because then I think next action item would be for me to update, I think, as it's still in draft mode, I need to check. If everything was ready for review. But I basically take another look and make it market as reviewable.
Christos Kalkanis 00:15:09 Yeah. And ideally, another pair of eyes looking at my pull request with the benchmarks would be great, because so far, I think nobody has actually reviewed it at all, so there could be, you know, mistakes there, I don't. Wanna.
And it's
since the last time there someone took a look. And actually there was a bit of back and forth discussion. It's all in the in the port request. You can see the comments if you scroll down. I think someone had the concern where they were still examining a stacked representation where we take the leaf frame out.
and
but the the benchmark that that person was using it. I forget his name. It's CPU bents and CPU bends is essentially stressing all codes on your system. But every call runs exactly the same code. So you end up with very few number of different stack traces. So it's a really bad benchmark to.
for you know, alternate factors, representations, because you're not generating a lot of stats. Essentially. So what you're benchmarking there is ideal essentially a timestamp encoding because you end up with, you know, hundreds of Timestamps.
but the stack trace is the same.
Felix Geisendörfer 00:16:22 Yeah, makes sense. Maybe I'll I'll add an action item for the for the group on top.
a few benchmarks from crystals. And I'm giving myself the action item. Get simple stack trace at Ep. Already.
Chris was in the action. Active action item Section. Could you link your benchmark. Pr for me. Thank you.
okay, any other thoughts on this, for now, should we continue the action item list.
I guess we can continue so Francesco had another item, but I think he's not here today, so we'll
and probably skip that one.
I feel like it might have gotten. Let me double check that link.
Florian Lehner 00:17:37 I think we just have to wait until it get merged. It's has approval. So many approvals.
Felix Geisendörfer 00:17:42 Yeah, yeah, that looks like it has
strong consensus. There's a markdown link check and Markdown lint check that's failing. Somebody might need to do that.
Florian Lehner 00:18:02 I think he also fixed Mark Tom Lind in another pr that already got merged.
But this is should also be unrelated to the Pr he made.
So yeah, I will. I will ping a specification group to ask him to watch.
Felix Geisendörfer 00:18:21 Oh, thank you so much. That's great. Where do you ping them? Do they have a slack channel on Cncf or.
Florian Lehner 00:18:25 Personally write them in direct message, essentially.
Felix Geisendörfer 00:18:29 Got it. Okay, makes sense. And who do you Ping Tikran and Josh, or.
Florian Lehner 00:18:33 Yes.
Felix Geisendörfer 00:18:34 Okay, thank you so much for doing that.
okay. And then maybe the next one. No, the next 2 are the ones we added, today we do not need to review them recursively. That would get awkward.
I guess. Now we're into the official agenda for today, and I think
we have been discussing, trying to get profiling out in August in previous meetings, and I guess everybody was in agreement that we're getting in shape with a signal as we have it right now. But I guess one thing we have not asked ourselves with enough clarity yet is.
what about symbols? Can we announce something to the world that we have open telemetry profiling now without symbols, because arguably, it's only half the story, especially for the Ebpf profiler.
On the other hand, for runtime profilers which can adopt the format. They they are not bottlenecked by symbols. They could start tomorrow and even the Bpf. Profile to some degree could work when there are symbols on the host. So
it feels
like we could make a decision to say, I I think we I think there's no question that profiling isn't done until we have simple support. But like making a big announcement around what we have ready soon could could make sense, regardless and calling that one dot O, and then making a profiling symbol
signal, or whatever that's gonna look like. So second thing, we we do as a group. I think I'm slightly in favor of that, but I'm curious to hear different voices, and how people feel.
Christos Kalkanis 00:20:08 So I I think what we have today, like the the current profiling signal, as it is specified, allows for alternative implementations regarding symbol upload so anybody could come up with his own symbol. Upload protocol. That's not obviously not specified under a hotel, but upload the native symbols to any back end, and so on, so so like as an interim solution. That seems
fine like. Personally, I, my prime concern right now is to work towards profiling 1 point O. And get something stable out there. But the other auto teams, especially the collective team, can coalesce around so we can generate rapid progress, and like I wouldn't want symbols to delay that. If we can do that we can make it happen
without delays. I'm all for it, but I don't think that's that's possible given the timelines and also given, you know how we've been working, and like the amount of time it takes us to to generate progress here. So yeah, I would agree with Felix that let's work towards profiling 1.0, and then symbols would be our top priority past that after that. That's announced.
Frederic Branczyk 00:21:14 Yeah, I would agree. I I think, given given the timeline, I don't think and how long it's taken us to get to this point. I don't think it's realistic. Also, I think there's
it looks. It's it's more complicated than it looks@firstst and then, you know, it's strictly additive. So
I don't see why adding it later would be a problem.
So yeah, I agree.
Alexey A 00:21:42 Agree from my side as well. I think it's
I think it's good to publish the format so that people can start looking into this, and then the and giving feedback that is specific to to the format or try to evaluate how they would adopt it, and also give feedback based on that. And again, it would be nice to have symbolization, of course, but and maybe people get excited about the format, and we will have more contributors and participants, and including people, would be able to
contribute to this immunization effort as well.
Frederic Branczyk 00:22:20 Also what one more? One more time also, yet again confirming with what Crystal said, like we already see at least 2 like I know of the of at least 2 alternative, like mechanisms to do symbol uploads. So like clearly, everything is there to make it happen right.
Felix Geisendörfer 00:22:40 Yeah, I think we spend enough time like talking about the build identifiers and things like that that I think we're really critical to be in the main profiling format. But I think then, the
way that simple data gets uploaded is, perhaps
we, we know that there's multiple working paths. We just have to create on one as a group and then
standardize it as well.
Okay, then, anybody else before we
sort of trial or conclusion here.
Yeah, I think then it's mostly just a Comms issue where we we tell in whatever blog post we make sure that to mention that that this is something that opentelemetry is sick is still expected to deliver and opentelemetry plans to own that scope. But we think we have something useful even without that.
Okay.
Alexey A 00:23:35 Just as a thought, and I'm obviously like.
be proof of biased I wonder if it's at the time of the launch having a round trip converter
to people from paper off would be useful
as part of as part of like connection to existing tooling.
Or maybe it's an Overkill. It's just in, but it's just something I thought of and
like right now, and and just wanted wanted to voice it to see if anyone has any obvious opinions.
Felix Geisendörfer 00:24:12 I I know I think this is an important one, because I think we made an agreement to say that the hotel format needs to be a super set of people off, and being able to run, trip, convert people off to hotel and back, would proof that we have achieved that. I I feel like we have, but like seeing it in action and having a tool doing it would be pretty nice.
Florian Lehner 00:24:30 There is already an altered processor in work that converts people to delta presentation.
but it's in work, and with the changes to the the stack representation this will require will require even a little more more work. So there is progress. But it's not there yet.
because the hotel community also wants to have this this feature, I would say.
Alexey A 00:25:02 Okay. I have.
Frederic Branczyk 00:25:03 Let's say.
Alexey A 00:25:04 Either.
Frederic Branczyk 00:25:04 Sorry go ahead! Go ahead!
Alexey A 00:25:06 I just added to the burn down list, so that we keep struggling.
Florian Lehner 00:25:12 Sure.
Christos Kalkanis 00:25:14 Yeah, I think it would be great to have, because paper has massive adoption and like, it's always better to to give people a bridge to use what you're advertising immediately without them having to implement it from scratch. And you know anybody can get hold of paper office. And then immediately being able to convert them into this format is nice.
Felix Geisendörfer 00:25:35 Yeah, double checking flow. And if I because I was typing and trying to listen, not very successfully, did you say there's a processor or a receiver, or what? What's in the works in the collector.
Florian Lehner 00:25:48 Just let me look up the it's receiver.
Felix Geisendörfer 00:25:53 Recipient. Okay, yeah.
If you could drop a link that'd be awesome.
Florian Lehner 00:25:55 I would just add the link.
Yeah.
Alexey A 00:26:06 Frederick, I think you had something.
Frederic Branczyk 00:26:09 Oh, yeah, it it's not. It's a more more general statement that we are still making changes to the wire to the protocol is.
does make me a little bit nervous, because it means we don't have a single backend that actually supports it right now in the sense of how we expect it to be.
That was more a general statement.
Felix Geisendörfer 00:26:34 Yes, but I think this text trace representation might be the last one.
Hopefully.
Frederic Branczyk 00:26:42 Yeah, I I'm I'm just saying it. As a you know, we. We've done this for some time now, and that that is the only part that makes me a little bit nervous. But I I would agree that you know it's not a massive change and back end should be able to adopt, adopt to it pretty easily.
Christos Kalkanis 00:26:59 Felix, when we discussing at least, maybe it was you or someone else brought up an alternative. Timestamp representation as well. Is that still on the table? Or does that go away now.
Felix Geisendörfer 00:27:10 No, I think we have said.
I think that's a Pr. That we have 2 approvals on now that Florian made. I think it's
the 6, 4, 9. Pr, I think that basically clarifies how the stack tracing is supposed to work.
No, wait, I said. 6, 4, 9.
Florian Lehner 00:27:31 It didn't touch times.
Felix Geisendörfer 00:27:33 It. It did clarify how they work. Right? Wait. Let me double check.
Yes. So basically, sample type must have at least one values or timestamp unix entry. If both fields are populated, they must contain the same number of elements. Blah, blah. So I basically
this, this Pr, even so it's called use single profile sample type. I think it actually does a little bit more to clarify the semantics around Timestamps, and we believe that by having a single sample type. That actually is what made it disambiguous on how to the timestampsing really works, because previously the values could be like used. You have a list of them, and each entry corresponds to one sample type, and I think this ambiguity is now resolved, and we we do have
probably fairly efficient Timestamps in the latest version. Once that marches.
Florian Lehner 00:28:31 I think.
Christos Kalkanis 00:28:31 Great. So that sorry. Go ahead.
Florian Lehner 00:28:33 Maybe I just understood. When talking about the format of the timestamp did you think about Delta timestamp and the real format, or just a clarification. How the how they are just.
Christos Kalkanis 00:28:47 Yeah, we we discussed deltas like some time ago, and then the the benchmarks I did for the stack trace encoding also have timestamp deltas in there, just to to show you what the theoretical best case is like. If we 0 all the time stamps, and then the simplest delta representation, which is the delta from the time the starting timestamp of the profile itself. So no sorting requirement, for for example.
but I think the like the best case that we could get. Is not that high? So like in my mind, it's not worth the complexity.
So we talked about this in the previous meeting, and we said, Okay, let's not do this.
But I was just wondering if there was something else about Timestamps, because I also wasn't here during like I missed meeting. I was in in Vegas with the other last folks. I'm wondering if that was clarified there. But anyway, yeah, so it's just good to know that after those alternatives encoding once we decide on that, we don't have any major
or minor braking changes to the protocol covers.
Felix Geisendörfer 00:29:50 Yeah, at least, I was not planning to touch Timestamps anymore. I think they're suitable after this. I mean, we can continue bike shaving forever. But I think we're in a pretty good place after we do this. And we we looked at Delta, encoding quite a bit, found it not to be very effective, and
I think the conclusion is what we have now should work.
Of course we all like. Once we, the dust settles. More. People here will probably try to update their their backends and other tools to to make use of the the new encodings, and if we find something where we like made a mistake, but I think the chances are small. We looked at this quite a bit now, so hopefully it will work very nicely.
Christos Kalkanis 00:30:30 Also regarding the back end. Frederick, I'm not sure if you're aware, but elastic open source the filer, so anybody can contribute now, so like, as far as backends go. This is kind of the the test demo back end that we use to prove aspects of the protocol. So feel free to get engaged if you want.
Felix Geisendörfer 00:30:55 Makes sense.
yes. So I think we had a few spontaneous agenda items appear here. But I think we can now go to process, information and context propagation.
This would be Elsa.
Alexey A 00:31:15 Sorry, quick question for the time. Stamps, do we have a Pr. I recall there was a link to the comment. We described the proposal, but I I probably missed it. Do we have a full request that.
Felix Geisendörfer 00:31:27 Yeah, yeah, 6, 4, 9. And and and then so basically.
once that's landed, I think Timestamps are what we want them to be.
Alexey A 00:31:34 Okay. Thanks.
Felix Geisendörfer 00:31:41 Anything else on timestamps.
We can come back to them later, if we want to. We we still have half an hour left, so we might have time. So yeah, basically.
Alexey A 00:31:53 Sorry.
Felix Geisendörfer 00:31:54 It's probably.
Alexey A 00:31:55 Quick! Quick! 4, 6, 4, 9. The only quick feedback, probably to Florian. I think it would be good to rename the pull request. That's kind of just mechanics, but it says default, sample type. It doesn't mention Timestamps. So maybe just put a short story in the title.
Felix Geisendörfer 00:32:13 Yeah, I agree. That's roomy for loop for a second, too. But like, yeah, the the link in the Pr description clarifies sort of what the scope is with the examples there. But yeah, maybe a better title.
I don't, Florian. If you're speaking, you're mute.
Florian Lehner 00:32:32 Yeah, just updated, sorry.
Felix Geisendörfer 00:32:35 Oh, excellent. Thank you so much.
Okay, then, so time is a charm. We have an agenda item called process information and context. Propagation basically also on our end, has been looking into this topic a bit and basically wants to pick up a conversation to sort of align between what all of us have done sort of separately, and see if we find
maybe a good solution for this. Elsa, do you want to take it away?
Elsa Keirouz 00:33:12 Yeah, sure.
Yeah. Okay. So 1st of all, Hi, I'm Elsa. I'm an intern on the profiling team at datadog. And I've been working on context propagation for the open telemetry. Bpf profiler since
February, March. And yeah, I think we're at a point right now in my research where where we have some relevant information to to present. So we can start discussing how we'd want to specify that kind of behavior to do context propagation between instrumented processes and the Eppf profiler.
So I'm going to share my screen on the document that I wrote. I wrote a document. That sort of goes over all of the prior art. So so far, context propagation has been used to do trace to profile correlation that was contributed by elastic, and I am pretty sure it works only with their Java agent. So there's that. There's also something that was recently recently contributed by polar signals
to. So the custom and go labels. So custom labels is for native languages and go labels is for go to propagate custom metadata along alongside profiling data. And so I just wanted to go over what the main things that we're going to need to make context propagation work for the profiler are. So 1st of all, we're going to need process
level information that's going to look like our service names, our deployments, environment. And so that's the type of information that we only need to collect once because we'd like to assume that it will not be changed throughout the process lifetime. And then we also need thread level information in order to get thread, level observability.
so that, for example, in the case of trace to profile, correlation would be trace and span ids.
So so far the way that it's been implemented in the Ebpf profiler.
So for process level information, elastics implementation that's been contributed uses a global variable to share process level information. So how that goes is there is a global variable whose symbol is going to be exposed in the elf symbols, and the profiler is going to go through those symbols try to find the corresponding one, and
and once it retrieves the address, go, read at that memory address in the instrumented process that it's profiling.
And while that's a great approach in terms of low overhead, it's not optimal, because we can't really sort of predict the way that users are going to build their instrumented applications in the case where they're going to statically link them. They could also strip their binaries, and then we won't be able to find
the symbol for the global variable and context propagation is not going to work at all in that case. So we've been looking for alternatives that allow us to
sort of go around that for 1 1 thing that we thought of is using custom elf sections.
And we've also thought of sort of exporting those static symbols as like into the dynamic symbol table for our final binary. But those solutions are not optimal. The 1st one doesn't always have a native support in languages, such as go, for example, and the other one requires users to change their builds, which we would like to avoid.
So the alternative that we prefer that we found so far is using named anonymous mappings. How that works is we're going to m up a memory region, basically. And then, as a sort of fairly recent Linux kernel feature. We're able to give that memory mapping
a human, readable name so that allow us allows us to easily find it when we're going through our processes. Mappings.
And why that is great is, 1st of all, we don't have to handle any symbols, so we don't have to go through our elf symbol tables. We don't have to worry about stripped binaries, and also the Ebpf profiler goes through the process mappings, anyway. And in the case where that mapping is created. After the discovery of the process.
we are thinking about using K. Probes on maps or any other relevant Syscall to to inform the profiler of of that of the presence of that mapping.
and that's also compatible with all programming languages without the need for a native component.
However, there's the main challenge for this is that it's a fairly recent feature of the kernel. So it's been released in Linux Kernel version 5.1 7. So we're proposing to either have the other 2. So the other sorry options used as a fallback.
or, to use non-named anonymous mapping so regular anonymous mappings and have them have clear identifiers, such as a really specific size and magic bits to sort of be able to confirm that this is indeed the mapping that we're looking for. Then for thread level context propagation. The way that it's been done in the 2 contributed solutions so far
has been using thread local variables. So it's leveraging a thread local storage. Specifically, Tls desk. So it's a descriptor based Tls dialect.
which is a really performant model. But there are a few drawbacks. The 1st one is, it has limited support across tool chains, notably for x 86, 64. So there's no support in rust for now, and the support in clang is really really recent. It came out in Clang 19.1,
and then it also implies that since it's based on a shared dynamic library. We're going to need a native library in all of the hotel Sdks, which is also not ideal. And then, finally, since it's based on native threads. It will probably not be compatible with complex concurrency models such as go routines and go.
Which is why we're sort of trying to think of alternatives for Tls desk or using Tls at all.
But yeah, that's that's basically everything we've gathered. And we just like to sort of start and kick off the conversation around all of that. So thank you for your time.
Frederic Branczyk 00:40:27 This is super cool. Thanks for putting this together. 1 1 thing that I'll that I'll note is so we we just landed the like go label support right? And we've actually been working on like custom label support for v, 8 as well. And we've basically landed on. We probably need something. Custom for v. 8 as well.
For a variety of reasons. I'm not actually sure about the all the details, but, long story short, we basically couldn't get the like native approach to work with v, 8, because of the V 8
specific thing, basically. And so like, I wonder how much we should be focusing this entire effort on solving this for all languages versus potentially. Maybe we should just scope this, for you know, CC. Rust.
That's just, you know, a more general observation from having been developing this for some of our customers.
Florian Lehner 00:41:40 Oh, yeah, thanks for the great. Write up.
I think we have to differentiate a little bit more between the what we want to have as a process information that, like service name stuff like this. Because this is already possible in the hotel just with hotel components. So if you just use the container id, and then get the container. Id, you can just say, Hey, this is service, this service name deployment, whatever.
But to me the the most interesting part is really about the tiers tax. So the threat information
that can be leveraged. Then to collect information like span id or trace. Id. So, yeah, the second part is
definitely super interesting. I think how.
Felix Geisendörfer 00:42:38 Yeah, go for it.
Nayef Ghattas 00:42:40 Yeah, I think on the process level specific information. Yeah, indeed. If if it's a tag that we can associate with a specific container, things are going to work. But my understanding is that if it's something that is going to be pro process or on the process level, we cannot associate with the container. Id. So let's suppose you have 2 processes running in the same container, or use cases like this. This will not
going going to work next.
Florian Lehner 00:43:09 Esther.
So then, that the pid is also reported. So
if you write your own reporter, the information is there.
Felix Geisendörfer 00:43:21 How would the Pid tell you what it is like? I think the example is like you have, like a sidecar in the same container right now, that's what you're thinking about. And yeah, one is a site call. One is the main application, and the Pid is not going to tell you that.
Florian Lehner 00:43:39 Yeah, yeah, you have a little more more like metadata, like process executable.
Oh, yeah. Good point. I have to think about this.
Frederic Branczyk 00:43:57 Sorry I'm I'm actually not fully fully understanding this, like
at least the way that we and our customers use this feature is purely to communicate, communicate, like application specific things to the profiler.
I I actually, I like, I don't understand this. This point with the container actually, like.
Felix Geisendörfer 00:44:20 Okay.
Frederic Branczyk 00:44:21 Can someone reiterate on this.
Felix Geisendörfer 00:44:24 I think the main use case that we're thinking about is just providing users users with a service oriented view of the profiling data because they think about what they deploy as services. And so like, yeah, if you have like a go application, it probably has a name that you're using internally in the code base, and that's how you pull the service. But then, if you deploy a sidecar in that same container, you probably want to
give that a different name like, and yeah, that's what we're trying to distinguish. Like, basically, you get a list of services and the the go application and the site call that would be maybe in the same container. Maybe not, would always show up as separate services. That is, I think maybe the rough problem statement here.
Florian Lehner 00:45:02 If you differentiate the sidecar based on the environment where you will.
then we can already do this because the environment variable is already reported.
You just need to whitelist it if you say, Hey, I'm I'm looking for this specific one.
If this would help.
Christos Kalkanis 00:45:25 So I think it would be great if we had specific examples of where. Yeah. So there are 2 approaches, like, for instance, one approach is to communicate that information all the way down to the kernel to the so the kernel can access it and attach it to the profile. And that's, you know, ideally, we wouldn't go there. We'd only go there. This sounds to me like a last resort. If we can do it without going there. Then it's preferable, because it's more flexible, we can attach more information, and so on.
So let's 1st examine if, if, for the kind of information you have in mind. The latter is possible, like we can do it without sending the data down to the camera.
So having specific examples would help with that, because then we know what what we're looking for. Alexa.
Alexey A 00:46:06 Which languages the the proposal that was presented today covers or targets
probably question to else.
Felix Geisendörfer 00:46:25 Yeah, 2, 1, 2.
Elsa Keirouz 00:46:27 Yeah, sure. So what we, what we were aiming to do with this proposal is sort of cover as many languages as as possible with one same yeah, one unified solution, basically. So which is why for the process level, we're proposing anonymous mappings or named anonymous mappings. Whatever is is more suitable.
But yeah, for for for the thread level, it would be any language that we're able to that either native. So C, plus plus C rust or any language that's able to have a native component. So
basically, that would be the the main requirement to use Tls desk, or else we would want to have a separate solution for languages that can't support that.
So yeah, I hope that.
Alexey A 00:47:21 How much, how much is in scope discussing how context actually like propagates and travels within within the process. Because in go, for example, this happens through the concept of context that go and like supports natively. And I would expect any solution we have for propagating the context like it has to
somehow interact with the language runtime, either explicitly or implicitly to, because, for example, for the example of interacting with containers and services, we accepted the request. But then things within the process they start to kind of get delegated to other threads, and and so on, and so forth. How?
How would that be handled, because I think that's an important part of the mechanics.
Felix Geisendörfer 00:48:14 I have my hands up. But I wanted to say something else. Elsa, do you want to take this one or.
Elsa Keirouz 00:48:22 I'm not sure I fully like I fully understood the question I have. Could you maybe take this.
Nayef Ghattas 00:48:31 Yeah.
Alexey A 00:48:31 Think.
Nayef Ghattas 00:48:32 The sorry. Go ahead, Alexand.
Alexey A 00:48:34 I think it would be good to add, like one or 2, but at least one end to end example in this document, like, what is the what is like end to end flow that we're trying to enable? I think the the the example that Felix had, that we are in like in cheeky environment, probably. And my program is handling
like requests of different types that belong to different services. And then I want to be able to break down the profiling data by service
and then describe and to end how this would work, because my understanding would be that we can. We can probably like, figure out how to associate the the initial request with with the service. But then things start to travel
like it's it's rare that, like it's single single thread that handles everything
within. Within the server, things will inevitably get delegated. So how that will work end to end, I think.
that's that's kind of like I'm trying to match that with the with the current document. But I think it could be more explicit.
Felix Geisendörfer 00:49:41 I mean, maybe I can take it. I I think the the idea is that the
Hotel SDK would probably need to be aware of what we're doing, and there needs to be an Api for the SDK to say, Hey, I am now executing this span on this red. And that is, basically when the data would be stored in sweat local stores. So the profile I can find it there for CC. Plus plus rust. I think that that's pretty clear how that would have to look like for go, I think the the proposal here is to just use people off labels. Which? Yeah, you still need the
go SDK, to also sets the people off labels when you create a span. Maybe we need an Api for span activation as well like. If you take a span and you send it through channel to another. Go routine, and then you do some work on behalf of suspend there. Maybe that's that's also needed. But yeah, generally for go it would be the people of label, and even more generally like the Sdks would have to be updated to basically put the context in a place where the follow can find it.
Alexey A 00:50:43 I see. So this is only the proposal is only for a mechanism. How to kind of put there some state that the profiler can then record, and then but but then open telemetry. We rely on context propagation in open telemetry, and on communicating that state to this mechanism.
Okay.
Frederic Branczyk 00:51:01 Yes, like one more time. The support for go has already landed like it was merged yesterday or 2 days like sometime this week, so like
that that basically already already exists.
Felix Geisendörfer 00:51:14 Well.
Frederic Branczyk 00:51:15 Kind of a.
Felix Geisendörfer 00:51:16 What has landed for what has landed for? Sorry, what has landed for go like the Ebpf port, right? But have we landed something in the hotel sdks.
Frederic Branczyk 00:51:23 No, yeah, you're not not in the sdks. Yes, that's right. But people can already attach go routine labels, and they will see it show up in the Evpf.
Florian Lehner 00:51:33 Do you contribute the changes to go? SDK.
Frederic Branczyk 00:51:36 Sorry.
Florian Lehner 00:51:37 Do you contribute the changes to the Go SDK, or is the.
Frederic Branczyk 00:51:41 No, no, this is just. If you use standard library, go routine labeled.
Florian Lehner 00:51:46 Okay.
Frederic Branczyk 00:51:48 So I I think I think I I would be in favor of kind of separating this proposal into 2 2 things, one, that is like process specific metadata. And like.
yeah, I don't know thread level or like application context. Information. I I think I'm kind of with with crystals that I'm I'm not a huge fan of
communicating the like process level. Information through something like this. I do think there's enough information available like the way we do this, and we do exactly what I think, Florian or Crystal said we. We wrote a custom reporter that collects enough of this information so that you can do this so that you can say, you know anything that has is in this container. Add this label, or something like that. Right? So
not saying that that is how everyone should do it. But the information is available through other mechanisms already. But the threat level thing. That is exactly why we wrote custom labels. That's very much a problem that continues to need solving.
Felix Geisendörfer 00:53:00 Yeah, one thing I want to bring up, and also because I forgot why, where we ruled it out. I think we had discussions about it. I think Ryan brought up the environment variables. It's a evpf profiler now has support for collecting environment variables. And I think we talked about using those to identify the service. But I forgot how we ended up with the M maps instead, because I didn't see the environment variables listed at all.
Nayef Ghattas 00:53:25 Yeah. My understanding is that when you import the hotel sdks you are able to either configure them directly in the code or configure them via environment variable. And if you configure them directly in the code, well, basically, we have no way to extract that bits of configuration that is hard coded in the code, or pass through as config flags.
Felix Geisendörfer 00:53:50 But in theory, if we.
Nayef Ghattas 00:53:51 The environment.
Felix Geisendörfer 00:53:52 But in theory, if we're willing to update the sdks, the sdks could update the environment of the process right?
Nayef Ghattas 00:53:58 Yes.
Felix Geisendörfer 00:54:02 Okay, and I mean, that's really we need to do that anyway. Because if we want to set like something in an M app. Like also, the SDK needs to be updated to do that. So that that needs to happen regardless of what we choose. So
maybe we should go back and reconsider environment variables as a primary mechanism? Or was there another reason.
Nayef Ghattas 00:54:25 I'll follow up and look at our notes, too.
Felix Geisendörfer 00:54:28 Because I feel like we had another reason that now I just can't think about it anymore. So okay, we'll come back on that one.
Christos Kalkanis 00:54:35 It would be great to add that those reasons, or the the thinking behind it in document, because then we have everything in the same place, and we can all look at it exactly.
Nayef Ghattas 00:54:43 Yeah, sure.
Felix Geisendörfer 00:54:45 Yeah, maybe also. And if can you add an action item on top? So we follow up on this, and I'm trying to catch up on notes here a little bit.
Frederic Branczyk 00:54:55 I'm also gonna try to get Brendan and Tommy to have a look at this, who both worked on the go and custom labeled stuff on our side.
In in general, we're not married to our implementation, like we've always communicated that this is experimental and that it's likely to break with our customers. So you know.
happy to find something that works for everyone, and ultimately.
Felix Geisendörfer 00:55:25 Thanks.
Nayef Ghattas 00:55:26 Yeah, I think 1 1 important bit that we sort of wanted to surface is that whatever solution we choose, we need the hotel sdks to implement it for correlation to work. So it needs also to be approved by the SDK maintainers, and an appropriate solution from that point of view.
Frederic Branczyk 00:55:43 In in that sense we're happy, like I've always said this ever since we initially created it. We're more than happy to also contribute our custom labels code base to to the open telemetry project, or whatever is most useful.
If that's, you know, helpful.
Felix Geisendörfer 00:56:02 It is. Yeah.
Alexey A 00:56:08 Would logging also be interested in this like to capture the service name and the logs or something? I I don't know how logging mechanics works
work today.
Maybe they already do that in some way.
Felix Geisendörfer 00:56:24 Yeah, I don't know, either. I I just know that logging is like the odd one out in terms of the
hotel signals in the sense that they decided not to like. Be like an SDK level signal and instead focus more on like, hey locks already exist. We're not going to dictate an Api and library for doing them. But.
I don't know the more than that.
Alexey A 00:56:49 Because nobody is going to change how they are doing, logging.
Felix Geisendörfer 00:56:53 Yeah, there's always just too many libraries and solutions out there. And they were like, I mean kudos to whoever was involved in that, because hotel seems to always be very tempted to add another one to the stack, you know. So this is actually pretty nice.
cool any any more thoughts on sort of context propagation. If not, I think we have a clear action item on the service name problem and maybe splitting it up either way. Whatever we find we'll document, and then we can continue the discussions. Async, in the Cncf. Like, I think.
Florian Lehner 00:57:27 I think it was already mentioned in the Cncf slack, but as Krafana contributed Belay Evpf solution
which should already have some information about the context.
Maybe that's a way going forward by
bypassing the sdks and just using this approach from Billy.
So let delay and dbpf profiler communicate in some way. And just, added Brookton.
I I don't have details how it could could be done, but from conceptually it should be possible.
because that delay is also instrumenting and extracting this information.
But I don't know details.
Christos Kalkanis 00:58:13 But the problem with that is that you introduce an additional requirement, right? You need to have the profiler plus Baylor running at the same time. Baylor also does a lot more things. It's more expensive. Maybe, you know, can think of environments where I wouldn't wanna run both, like, I only want the profile. For example.
Florian Lehner 00:58:29 Also in this case also are also not coming for free. So
just depends where you put the overhead.
Christos Kalkanis 00:58:35 Nice.
Felix Geisendörfer 00:58:36 But but everybody has the sdks adopted already in hotel tracing? I would think so.
Florian Lehner 00:58:40 Yep.
Felix Geisendörfer 00:58:42 Miff.
Nayef Ghattas 00:58:44 Yeah. One thing I wanted to add is that my understanding was that Bela isn't extracting the information from the hotel Sdks, but rather creating its own trace, Id and span id context for the traces and spans it generates.
So we still have. So I think we we roughly have 2 problems to solve. How do we get that information from services that are instrumented with Beta and with a new Ebpf instrumentation? Because I think customers are going to.
Some of the customers are going to have Bela installed and the Bbpf. Profiler at the same time, and they'll probably expect correlation to work. But we also need correlation to work for customers that install the auto sdks and the profiler at the same time. So we probably have 2 separate problems to solve.
Frederic Branczyk 00:59:32 Will also say, Oh, sorry know.
Felix Geisendörfer 00:59:37 Yeah, I was gonna ask. But I meanwhile, I've been Googling. What's the status of the donations? Because last time I checked it wasn't finalized yet, but it seems like they made, since it's initial code drop. I still think there's a question mark on what that means for adoption, and I I think
maybe, at least in the beginning it might not be
that quickly adopted. But we'll we'll have to see. Like I I think. Basically, we'll we'll deal with more hotel users that use the sdks for a while and that should maybe be initially the focus. But thinking about bailout probably can't hurt if they're already
code dropped at this point.
Frederic Branczyk 01:00:10 Yeah, I I just wanted to note that, like Cu- custom labels like
distributed tracing correlation is one way that custom labels is used by our customers, but is used for way more things than that.
Like. It's just one interesting thing to do with it.
So that that is whatever solution we come up with, that would be something that we do require.
Yeah, 2.
Felix Geisendörfer 01:00:36 We're 100% with you there. We also use labels internally for all these same use cases and have a lot of customers who get mileage out of them. It's very, very useful.
Frederic Branczyk 01:00:49 Just wanted to make sure, because, like the beta thing would only if if it even works, it would only provide context, or like distributed tracing ids.
Felix Geisendörfer 01:00:59 Yeah.
okay, we are pretty much at time today. So unless anybody has something urgent that we
should discuss, we can finish it off here.
and I want to thank everybody for their time and the discussions.
Good stuff. And yeah, wish you a nice local time. See you next time.
Frederic Branczyk 01:01:28 Thanks everyone, bye.
