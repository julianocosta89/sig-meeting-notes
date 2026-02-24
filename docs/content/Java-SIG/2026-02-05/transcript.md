SIG: Java SIG
Date: 2026-02-05
Duration: 34 minutes
============================================================

## Zoom Recording Transcript

**Gregor Zeitlinger** 02:12 Hello!
**Peter Findeisen** 02:19 Hello.
**Ivo Anjo** 02:23 P?
**Jack Shirazi** 02:32 Rask was having, some problems in the last meeting, so…
It might need somebody else to, share.
**Jason Plumb** 03:03 I nominate Jack Berg. Oh wait, he's not here. I nominate… oh, Trasky's here.
**Trask** 03:11 I'm still having computer problems,
**Jason Plumb** 03:16 I nominate Watson.
**Trask** 03:19 I thought he was skipping today.
**Jason Plumb** 03:21 Nope.
He's muted, though.
Or we can't hear you, John.
**John Watson** 03:27 If nominated, I will not run. If elected, I will not
I'm not in a position to… I'm not in a position to share my screen about this stuff.
**Jason Plumb** 03:43 Jack is here, a burger's here.
I would do it, but I have to drop, so it's silly.
**Trask Stalnaker** 03:51 I think my computer is functioning again here.
So let's give it a go.
Alright, let's… just jump right into topics. Oh, our one topic. Alright.
Jonathan and, Hey.
Do any of you want to share?
**Jack Berg** 04:54 Ivo, you're on mute, if you're talking.
**Ivo Anjo** 04:57 Yeah, I can go ahead.
Okay, so, the… I can share, yes.
Does this work? It works, yay. So, yes, the… we…
And the meeting on the 22nd, which I didn't attend, but I caught up in the recording, there were some discussions about the…
process context that, the profiling SIG, and me, I'm trying to, we're trying to kind of, push, this spec to have this con… this way of sharing context from inside applications with the profiler.
And we also have this demo implementation that was out of date, so I've now updated the demo implementation to match the current version of the spec. So, like, upstream, we were discussing a few things, and we evolved a bit, and I forgot to update it.
One of the details that I believe got discussed in that meeting… well, I don't believe, I saw it, sorry, just a way of saying it. And one of the things that got discussed on the meeting on the 22nd is that,
this approach that we're taking here in this example is using the, the new, foreign function and memory API, which is, like, one of the Panama… part of the Panama OpenJDK project. And, in practice, this means that
without extra flags that probably people are not going to enable, like, enable preview features, it's only from 22 and above, which means, Java 25 in terms of LTS.
Which, would mean that I think one of the questions is if this was okay to say, okay, this feature will only work on modern Java versions, and for older ones.
will…
Maybe not be able to support it, or if so, we'll need to, like, pull in a native extension to do so.
**Jack Shirazi** 07:10 Yeah, so I… that's my comment just below that about the.
**Ivo Anjo** 07:13 you.
**Jack Shirazi** 07:14 The other spec, the 4855.
Yeah. Which is fully Java compatible for… going back to Java 8, and so if they're gonna take that approach.
And if that's going to be implemented anyway, why…
Why wouldn't we just use that same approach for all For all the comms.
**Ivo Anjo** 07:40 Yeah, so that's a good question. So, let me pull open that one so it can all kind of follow along.
So, the thing about this one is that, this one…
So OBI is the OpenTelemetry, eBPF instrumentation, so it's, like, the, instead of instrumenting the app with an SDK, you instrument it using, eBPF.
And so, kind of like, you manage it in the kernel, the active spans, the active traces, and then you emit the traces, etc.
The… and, and this PR is about, okay, if we want to know between, like, the eBPF instrumentation and the OpenTelemetry profiler what's going on, let's put this in what's called,
an eBPF map, which is, like, an in-kernel, like, hash map, hash table, to, of, like.
trail ID to… and then, like, associate the trace ID and span ID so that the… like, you can ask from one side to the other. The key thing about the OBI approach is that it requires OBI, so…
if you are using the OpenTelemetry BPF instrumentation on your Java app, it works, but if you are using the OpenTelemetry Java SDK, and you don't plan on using, eBPF, then this doesn't work, and that's why, I… that's why, like,
this option might not be available for everyone, so at least, like, if they want to use the Java SDK, which I believe offers a lot more features than doing it from the kernel side, I think you would still need the other mechanism to provide the same capability, if that makes sense.
**Jack Shirazi** 09:29 It's not the… it's not the OBI, piece that I'm asking about, it's about.
**Ivo Anjo** 09:33 Oh.
**Jack Shirazi** 09:34 The communication proposal that they have there.
Could… you could just as easily use it for your one?
And…
You know, just having that, that memory map file in the same, you know, in a given location.
And that would be compatible with everything going back to Java 8, and I think all languages,
Well, most languages have the same mechanism, so… I'm just wondering…
**Ivo Anjo** 10:03 I might be misunderstanding, but I believe this is using, like, an eBPF map, so this is not using a regular, like, in-memory location, so this is something that the Java applica… if we want to use this without the OBI, there would need to be something that calls into the kernel to write into this map.
Explicitly.
**Jack Shirazi** 10:31 I mean, it's a memory map map.
At a specific.
**Ivo Anjo** 10:34 Okay.
**Jack Shirazi** 10:34 in memory, so…
**Ivo Anjo** 10:36 No, no, no it's not. Like, at least, like, I'm… I might be misunderstanding it, but I believe this is an eBPF map, which is, like.
the in-kernel, like, thing that eBPF can access, and the other parts of the kernel can access, but it's not, like, a regular memory map for the application.
**Jack Shirazi** 10:53 Yeah, I agree that that's the case, but the general concept here is just that we have a path with a specific location where there's a shared memory.
And that… that works for all languages.
So why… why can't we use that mechanism? Because then it's supported all the way back to Java 8.
Lord, am I missing something there?
**Ivo Anjo** 11:20 the… the thing is, like, to be able to use this approach without pulling in the OpenTelemetry BPF instrumentation, we would still need to have something that calls into the kernel to write and read into the map. I don't think…
Or at least, like, this one. There is another version where we could say, what if we change this from an eBPF map to something that is in the application memory space?
Which would be, I don't know, effectively equivalent to saying, like, what if we implemented homegrown thread local variables, and then have the kernel or the profiler read from them?
And the problem with that is that you would still need to manage the thread locals in… from the app, so…
I'm not saying it's impossible, I'm saying it's also hard.
**Jack Berg** 12:32 Maybe some clarifying questions, then, on this PR over here?
you know, I think the two groups that are doing, sort of.
Inter-process communication, and are looking to…
have eBPF tools that are talking to, you know, processes instrumented with SDKs.
We should have one…
community-wide communication mechanism that we all agree on, and so I think, like, these two groups need to kind of get together and sort out what's best and why. I don't think we should have two mechanisms.
**Ivo Anjo** 13:12 to, to clarify, I, I, like, we did speak, with, the, like, we are speaking with the, the OBI folks.
And that's why… that's why I was kind of saying, like, this mechanism… this mechanism works very well for OBI, because OBI is already in the kernel, and the BPF profile is also in the kernel, so it's very natural for them.
But… and the approach that we're taking is not… does not work very well for OBI, but the kind of reverse is also, is also,
Where the OBI approach, like, does not work very well for user space applications.
And we kind of discussed, and we were like, okay, maybe it's… we will have both, but this one, this mechanism kind of only needs to be between OBI and eBPF Profiler, and nobody else needs to change for this. It's kind of the magic of the OBI instrumentation.
**Jack Berg** 14:06 Okay, that's what was lost on me. I thought that this was a mechanism for eBPF profiling to get trace information from SDKs.
**Ivo Anjo** 14:14 No, bro.
**Jack Berg** 14:15 No, it's not.
**Ivo Anjo** 14:15 How about SDKs? Yes.
**Jack Berg** 14:16 It's for eBPF profiling to get trace contacts from OBI EBPF tracing. So it's like eBPF to eBPF, they're both in the kernel space already. Okay, that was lost on me.
**Ivo Anjo** 14:29 Yes.
**Trask Stalnaker** 14:30 That was lost on me, also.
So, why… what's the… so, what's the Java angle, then? Like, it's kind of.
**Jack Berg** 14:41 there's…
**Trask Stalnaker** 14:41 They're talking to each other, but through JavaSpace?
**Jack Berg** 14:45 No, there's no… there's no Java angle for this OTEP. The Java angle is in the other OTEP, Ivo's OTEP, which is trying to talk about the communication between EBPF
profiling in EBP… in SDKs, in, you know, the Hotel Java agent.
**Ivo Anjo** 15:05 Yes, that's the intention.
**Trask Stalnaker** 15:06 Oh…
**Jack Berg** 15:07 But ideally, eBPF OBI would also be able to talk to the SDKs.
Right?
**Trask Stalnaker** 15:15 Right, that's something I think they haven't tackled yet, is how to correlate OBI with the SDK, like, how to… right now, I think you…
like, you use OBI, but you don't get…
compatibility with your traces, your manual traces, kind of like a story like the Java agent and the SDK.
That we've had the bridge there.
**Jack Berg** 15:42 Right, so that's not tackled, and it's also not tackled how eBPF profiling would get trace correlation from the SDKs, right? So those are both of the…
unresolved areas.
**Ivo Anjo** 15:54 Yes.
**Jack Berg** 15:59 Hey, Ivo, has there… I'm sure you all have explored this, but, like, is there any mechanism that would involve the, the eBPF profiler accessing this context information, just off of, like, a network protocol, off of, like, a well-known port?
**Ivo Anjo** 16:20 So, there is some prior work, I believe… let me… I believe it was from Elastic…
**Jack Shirazi** 16:32 Yeah, that's basically how we do it in our, pre-donated product.
**Ivo Anjo** 16:40 But, but I believe, at least from my understanding, is that, like, you at Elastic were using both approaches, I think?
So, I believe this was the documentation of the approach, and I believe it actually kind of used both, so, like, one in-memory thing, and then the sockets as well?
I'll share the link as well.
**Jack Shirazi** 17:14 Yeah.
**Jack Berg** 17:17 Yeah, because the socket-type approach would be…
more robust against different Java versions, but, probably comes with some issues. You have to agree upon a port.
For example.
**Ivo Anjo** 17:33 Yeah, that's why… that's why we were a bit,
This is all still a proposal, so it can still change, but we were somehow hesitating a bit to go in the direction of a port.
Because then you, you go, like, okay, but, like, who can access the port? And what happens if you, like, you, like, you're in, inside the container, but the PPA profiler is, like, another container? And there's… obviously, there, there can be answers to these questions, but it's, we,
Yeah, there's a bit of a thorniness once you start doing really weird deployment scenarios.
**Jack Berg** 18:14 Like, so personally, and I don't speak for the whole JavaSig here, but, I don't think it's problematic to go forward with this Java 25 Plus restriction. I think it can be an opportunity to solicit feedback.
you know, if we go forward and when you say you need Java 25+, and, you know, that becomes a big thorn in the side of users, because lots of people want to run this with versions that are lower, then we can kind of go back to the drawing board and explore other mechanisms.
**Ivo Anjo** 18:48 would it be, like, the way I've kind of… kind of expected would be that customers that were really interested in having this in Java 8,
We could give them, like, a separate
dependency that they pull in that provides the features via a native extension. But rather than kind of forcing everyone to have this burden and to have to pull it in, they would kind of say, like, I want this, so they would pull in, like, the hotel SDK, and they will pull in hotel SDK
extra native thing, so they have opted in, and they now have this feature. This was kind of what I was thinking of for supporting those customers without annoying everyone else that doesn't really want, like, a native extension living in their application.
**Jack Shirazi** 19:35 Having a native extension is very doable, that's exactly what we do with the infrared spans.
The question is, who is going to support it?
**Trask Stalnaker** 19:48 What, Jack, where… where is the native extension in… inferred spans?
**Jack Shirazi** 19:54 It's the async Pro Follow.
**Trask Stalnaker** 19:57 Oh, okay.
**Jack Shirazi** 20:02 And, obviously.
We don't need to support async Profiler, we just need to support packaging it, which is nice and straightforward, but even that has, like, a level where there's different architectures and different, yeah, so…
it's less about whether that's doable, and it's acceptable. It is acceptable to customers, we've seen that, definitely, but it's who's maintaining it.
**Ivo Anjo** 20:32 Yeah, at Datadog, we also do the same thing. We have a sync profiler, and we are, we have a few of our extra bits that go together with a sync profiler.
For similar reasons. In the DDTrace Java, Tracing SDK.
**Trask Stalnaker** 20:52 I like the option of… I mean, the proposal to,
Have the native extension just be an opt-in.
Seems like a good compromise.
**Jason Plumb** 21:10 I'm sure that this was hashed out previously, and I wasn't privy to it. I know that, using environment variables to share resource information was rejected. Was there any consideration given to, like, named pipes?
**Ivo Anjo** 21:25 We did look into it, it's kind of similar-ish, problems with, what about containers, what about forks, what about, etc. Yeah, yeah.
**Jason Plumb** 21:38 Okay.
I gotta drop. Bye.
**Trask Stalnaker** 21:58 anything else?
To discuss about that?
Yvo.
**Ivo Anjo** 22:06 That's all from me. I can keep sharing if you want the screen, or I can stop.
**Trask Stalnaker** 22:12 I can… I can grab the sharing back. Thank you for the offer.
All right. Yes, we have a release date tomorrow.
Complex attributes…
**Jack Berg** 22:31 Can't believe the day's come.
**Trask Stalnaker** 22:34 Yeah, our 6-month waiting period finally, elapsed.
And we did the work.
**Jack Berg** 22:43 I mean, it's more than that. That conversation has been… Talked about that.
**Trask Stalnaker** 22:48 Oh, yes, yes.
**Jack Berg** 22:48 Years and years. Oh my gosh.
**Trask Stalnaker** 22:54 Nice to have…
**John Watson** 22:59 Just a quick question on the complex attributes. Is there any… there's not… we're not planning on using any of that in the standard agent instrumentation, right? It's mostly going to be used for Android.
**Jack Berg** 23:11 No, I think it depends, John, on the semantic conventions. So, like.
**John Watson** 23:15 Sure.
**Jack Berg** 23:15 There's all this semantic invention guidance that, you know, tries to restrict and cap the usage of these complex attributes, but, like, one place where they're starting to emerge that might end up in the agent is with GenAI stuff, which wouldn't be limited to Android.
But I think most of the places where they would be used, so the limit… the usage is limited, and it's all net new.
**John Watson** 23:41 Cool. Yeah. Because these things, like, as we know, like, lots of backends don't support this for any sort of…
Actual usage, right?
**Jack Berg** 23:52 Well, there's a lot of work done on that, and it's not as bad as you would expect.
So…
**Trask Stalnaker** 24:00 Yeah, and they may not be queryable on backends, but that… that was why we gave the 6-month,
Grace period after introducing it in the spec.
Was for backends to, at minimum, just serialize as JSON internally.
**John Watson** 24:25 Well, hopefully this doesn't open up the floodgates to ridiculous garbage being thrown into backends, because you could imagine this being abused pretty badly, right?
**Jack Berg** 24:36 Oh, yeah.
**Trask Stalnaker** 24:39 I mean, people are already… serializing JSON into their attributes.
**John Watson** 24:50 Now we make it easy for them, though, right?
**Jack Berg** 24:54 Little bit easier.
**John Watson** 24:55 Yeah, anyway, whatever.
**Jack Berg** 24:58 I, I, back in my previous employer, we had some metadata tracking about, like.
Attributes and sizes, and, like, sometimes we would see attributes that had, like, 2 million characters in them.
So, there's all sorts of crazy stuff people do well before this.
I think 10 million was the biggest.
**Trask Stalnaker** 25:25 So is this… This is not just benchmarks, this is…
**Jack Berg** 25:30 This is work, but it's a strict refactor. There's, zero functional change in the actual code
Well, maybe there's a little functional change in one of the code paths, but, like, so right now, we have,
We have this metric storage, which is, it tries to bundle together
a bunch of things into one, into one class. There's, you know, the dimension of whether the temporality is cumulative versus delta, and there's the dimension of whether, the memory mode is immutable or reusable.
And, like, you know, there's all sorts of if-else type statements throughout the storage that, like, is conditional based on different combinations of the temporality and the memory mode.
And it's really hard to reason about, and it ends up meaning that we pay extra performance cost for cumulative, which isn't necessary.
So, like, this, this change is about teasing those apart, so, into just, like, a dedicated, cumulative path and a dedicated delta path, for improved maintainability and also to avoid, unneeded work for, for cumulative.
So…
I can get into what that unneeded work is, but, you know, you can kind of see it in the benchmarks, what happens after you…
After you get rid of that unneeded work.
And I have more performance work that's coming that's, you know, this is kind of the first step, and…
A couple, but… We get some nice jumps for free.
Here, if you scroll down, I think I call out one in particular.
**Trask Stalnaker** 27:22 Under 4 threads…
**John Watson** 27:24 Yeah, the biggest difference looked like it was down at the bottom on the cumulatives.
That's right.
Yep.
**Jack Berg** 27:31 So, like, in the 4,000 to 5,000 operations per second range, depending on the instrument, and then if you go up to the previous, what are we at?
Like, 1,000… 1,500.
**Trask Stalnaker** 27:48 Nice.
Gregor… Let's see, you've started reviewing, how far… How comfortable, far along.
Do you feel, in your review of it.
**Gregor Zeitlinger** 28:18 I think it's pretty good, yeah, but having another review would probably help.
**Jack Berg** 28:27 It really is just strict decomposition of, like, one sort of Uber class into various subclasses. Like.
And the only, I guess, functional change is just removal of one little tracking bit in the cumulative path that is no longer necessary.
Yeah, there's sort of subclasses now in here for… for delta and for cumulative.
Close to a strictly factor.
**Trask Stalnaker** 28:57 failed.
**Jack Berg** 29:01 And then there's a cumulative one there, or below.
**Trask Stalnaker** 29:10 Okay.
I see, okay, okay.
**Jack Berg** 29:15 Because they just have slightly different, you know, things that they need to do for record and collect.
So, split them out.
Get rid of the if-elses.
**Trask Stalnaker** 29:26 I'll leave that, I'll leave this open and…
Try to take a look at it later.
**John Watson** 29:35 This is an interesting case where I wonder whether…
In the real world… I mean, I think it's a good refactoring. I'm just wondering about benchmark… micro-benchmark-wise, like, in the real world, you're only going to be in one or the other, and it seems like the JIT might end up solving for that.
**Jack Berg** 29:53 No, because this isn't, like, the extra work that I'm avoiding, it's like, it's not something that JIT could be privy to. It's like, you know, in the Delta case, we need to do this coordination task between the record path and the collect path.
to make sure that, every… there's no partial rights, or missed rights, or duplicate rights. And so, every single time we record, we're also incrementing this atomic long, which acts as, like, the coordination point between those in this sort of sophisticated way.
And so, like, that's only necessary in the Delta path.
Because deltas get reset after each collect. In cumulative, if you, you know, you're not doing any reset work, so you don't need this coordination task. And so, like, you know, it's, the cumulative path
was always doing this extra work before, even though it wasn't necessary, and, like, I could have added an extra if block to skip it if it's, if it was cumulative, but, it just would have cluttered the code further.
**John Watson** 30:56 Got it.
**Trask Stalnaker** 31:04 Alright, we have hit the end of our agenda.
Any… Thing that anyone still wants to chat about?
**John Watson** 31:15 I just wanted to mention that, it looks like the, CodeQL Kotlin 2.3 support is… has been merged, but not yet released, should be released in the next day or so, so we'll be able to do that upgrade soon. I'm… I'm keeping an eye on it.
**Trask Stalnaker** 31:41 Alright, folks, good to see you.
Till next time.
**Jack Berg** 31:46 Next time. Bye.
