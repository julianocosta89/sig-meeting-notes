SIG: Specification SIG
Date: 2026-06-30
Duration: 62 minutes
============================================================

## Zoom Recording Transcript

Jack Berg 00:03:33 Hi, everyone.
It's 2 minutes over. We're gonna start in just a minute or two. There's room on the agenda if you have any topics that you'd want to discuss.
Please… Also, remember to add your name to the attendees list.
And yeah, we'll get started soon.
Liudmila Molkova 00:04:04 Hello.
Jack Berg 00:04:07 Hi.
All right, we're 3 minutes over, 4 minutes over now, so let's get started. Robert, you have the first topic. Do you want to kick us off?
Pellared 00:05:09 Yeah, hello, nice to see you. You can share your screen.
I think this should be quick.
So the first one is about, the OTLP specification regarding limits, and this was the last PR, which was, so we had the client request limits, client response limits, server request limits, so this is the server response size limits.
And this has already enough approvals. Jade helped me a lot reviewing it and checked the implementation. He even messaged me how he could… how the collector could… So this doesn't… this doesn't have a prototype for the collector. However, Jade checks how it could be implemented.
And he got… he… he added an approval here. So, if nobody finds a blocking command.
I want to merge it tomorrow, because there's also another request to make a new release of the OpenTelemetry proto, mainly because for the things which have been done for the profiling, which I am pretty sure that Fabian and Ivo are very interested in.
Any questions, remarks on the Proto release or this PR?
carlosalberto 00:06:27 I don't know. I think Tigran was providing some feedback. If we could get some approval from him, it would be great. If not, well…
Pellared 00:06:38 Okay, I'll ping him to just double check if it's possible.
Jack Berg 00:06:45 So, I just want to confirm that this is, in sync with the client response limits that were previously added, right? So I think, what we said before was clients should limit parsing response bodies to up to 4 megabytes, and that's the… that's after decompression, and so I think you're… you're keeping the same language here. It's, 4 megabytes… before compression, right? So, like, the compressed… so that's just, like, all in sync with what the client is expecting.
Pellared 00:07:16 to do.
Jack Berg 00:07:16 And where it's trying to limit it, right?
Pellared 00:07:18 Yep.
Jack Berg 00:07:20 And are these two sections just for OTLP?
GRP versus gRPC?
Pellared 00:07:26 Yeah, so the difference is, you know, status code, one is resource exhausted, the other one was, I think, 500, and it was also following some pure art.
Jack Berg 00:07:40 So, if you wanted to go above this limit.
Because it says that the limit should be configurable, then you'd practically have to configure both clients and servers, correct?
Pellared 00:07:50 Exactly.
Jack Berg 00:07:52 Okay.
Seems reasonable to me. Sorry I haven't reviewed this.
Thanks for the ping.
What does Tegrin say?
Has Tigran commented on this?
Pellared 00:08:12 Yes, I think it was his first initial review.
And I think I address… Yeah, I addressed it. It was about, about… I think initially what I was writing was kind of trimming, and I just res… clarified and try to describe it better, how the collector or other implementations can reduce, you know, the message.
So if they can, they can try doing it.
Yeah, and I think I addressed it as much as possible, and Jade also was double-checking this language.
Jack Berg 00:08:57 Okay, so I'll just ping… Tiggering on this one more time, it does look resolved to me, and yeah, you know, he's had 29 days to get back to this, so that's a good amount of time.
Alright, any other comments on this topic?
Pellared 00:09:16 I have just a question regarding the proto, the Proto repository in general.
Are we aware of any issues or PRs that should also be landed if you want to make a release? There's an issue which has been created, so we do not need to answer right now.
I think it will be the, yeah, the first from the top. I created the milestone, so people can manually, you know, add things to the milestone, and also comment here.
Jack Berg 00:09:52 Thanks for that call-out. If anybody knows of any additional issues that should be resolved before this milestone, please add those, or comment on those issues, and if you don't have permissions, and one of the approvers or maintainers can add that milestone tag.
Okay.
Thanks, Robert.
Florian, you have the next topic.
Florian Lehner 00:10:19 Yes, this should be a quick and easy one. The profile signal adjusted their specification and data format explanation, and this is now in the right place, and we need some more feedback, so Tigran already approved it at, we'd like to ask for more feedback, so at the moment, I think there are no, open… Comments?
And it should be fine to go, so if you have time, please take a look.
Jack Berg 00:10:55 So, let's see, do we have any approvers, or… Other maintainers of the spec on the skull that could contribute a green checkbox?
If you're… around and available, please do take a look at this. It already has approvals from, various people involved in the profiling effort, and from Tigrin as well, who's, sort of been the TC point person on this, so… Josh, you have your hand up? You want to say something?
Josh Suereth 00:11:23 Yeah, I haven't had time, I'm sorry. After I pass things off to Tigrin, if you need a second check mark, I can probably take a look, later this afternoon. But if anyone else can, please do… oh, my camera's not on. If anyone else can, please do. I'm just a bit overloaded. But if Tigrin signed off, I'm pretty sure this is good to go.
Florian Lehner 00:11:44 Thanks, I appreciate it.
Jack Berg 00:11:46 And the status is still Alpha, so, you know… None of this is, you know, binding and forever yet, so… All right.
Thanks for that topic, Florian. Carlos, you have the next topic.
carlosalberto 00:12:02 Yeah, basically just, like, a small cloud that's from the CICD group. There's… actually, Robert is here, this is a PR… from Robert, discussing of reviews, and we were wondering whether it's good to go, given that it's only marking this as release candidates, not stabilization yet, and Yeah, Robert mentioned, I think you answered already, that you are good to go tomorrow.
Pellared 00:12:28 Yeah.
I also… I had… I wanted to join today's CICD SIQ call as well, but I didn't make it. I was late 30 minutes, so… So, I'm also trying to clean up all of the implementations, make sure that the docs are good, so if anyone would be able to consume them, they can provide feedback.
So, I still plan to work on the… after… on this, even though it… if you merge, and also add implementations to other languages. But so far, all the people that I discussed with CACD are good to go.
Jack Berg 00:13:02 That's good to know. I didn't know you were working with CICD, Robert, so, yeah, they're… they being the primary consumers of this, that's a good approval to have.
Carlos, did you have anything else that you wanted to discuss about this? .
carlosalberto 00:13:23 No, at all, just basically because, you know, it has a number of approvals, and it's ready to go, and it's only release candidate.
So, yeah, that's it.
Jack Berg 00:13:32 So unless you have a reason not for this to… for this to not go forward, we're planning on going forward with this, so please speak up if you think this shouldn't go to release candidate.
Alright, we are flying through this agenda, only 12 minutes after the hour.
David, you've got the next topic, mergeable views. This one… This one's great.
David Ashpole 00:13:59 Yeah, we discussed this a little bit last week, and as promised, I'm back.
I think the most interesting thing for people to maybe take a look at here are the merge rules, so for… All of the fields we use for Swin, except for attribute keys.
Where we essentially do, like, a merge of the lists, so that it has to be allowed by all of the attribute filters.
In order to get through to the end, which allows you to layer Multiple, like, different views that restrict a set of attributes.
Otherwise, I think, like.
naming is always hard, but, so I'm sure maybe there are opinions there, but I'm actually pretty pleased with the… the way this came out, and I'd love people to take a look.
And thanks, Jack, for the review.
Jack Berg 00:14:48 Yeah, just a minor phrasing thing, but it's, you know, I don't know if you've already resolved that or not, but it's basically an approval for me.
David Ashpole 00:14:58 Okay.
Jack Berg 00:15:00 Yeah, if there's any maintainers here from other languages, please take a look at this.
If you don't have context on this, views are… are problematic to use right now, because if you have multiple views which match an instrument, it sort of has unintuitive behavior in that instead of merging those views together, or just applying one of those views, it actually applies both of those review… views and spits out two different metric streams, or one metric stream per matching view. And so, yeah, views become a sort of problematic thing to extend with new features, because they have this sort of Sharp edge that prevents them being used, you know, easily and practically.
So this is a nice way to solve that. It keeps the selection criteria and the view stream configuration the same, and adds a new configuration property, which basically changes the semantics about how views, the existing selection and view configuration properties, how they are applied. So, it's nice.
you know, one thing changes, and the behavior sort of gets fixed, and they become a lot more usable. So, there's a prototype in Go already. I haven't had time yet, but at some point, I would love to do a prototype in Java as well. I encourage other language maintainers to consider doing prototypes in your language.
David Ashpole 00:16:30 Thanks.
Jack Berg 00:16:37 And yeah, please review this PR as well.
Josh McDonald, maybe you'll be interested in this as a, you know, someone who's worked on metrics for a long time and is probably acutely aware of the problems with views.
Great.
Alright, unless there's any other comments?
We can move on.
Ivo, you have the last topic on the agenda.
And if anybody else has topics, we do have time, so please feel free to add your topics. I vote.
Ivo Anjo 00:17:14 Yes, hello? Yeah, I'm kind of here to do a bit, like, the same as Florine was doing, which is, like, we have the context sharing portrayed, PR, and we have a bunch of, checks and feedback from people and whatnot, so, please give us feedback, so that we can, get the OTEP merged.
In particular, Josh mentioned you're very busy, just, and we kind of already replied to your feedback, so, yeah, if you have some Limited bandwidth, we replied there, and yeah, if anyone has any thoughts, this is something that we're very keen on pushing forward, so yeah.
Jack Berg 00:17:58 This has been open for several months. It has a lot of… er, well, I was gonna say it has a lot of approvals, but We could probably use some more approvals from the folks that would be, you know, consuming slash producing this.
So there's the green check boxes, but the gray check boxes are all… also a useful signal.
Okay.
Ivo Anjo 00:18:21 I'll try to chase more people, that are not in this meeting as well.
Jack Berg 00:18:36 Any other comments on this?
Josh Suereth 00:18:41 If, if we have time, I mean, if we run out of agenda items, Eva, would you mind… we could briefly talk about this, or we could take it offline, out off the meeting? It might be easier if we talk live versus me reading everything.
if that's interesting to people about this one, because I think this does affect all the SDKs and implementations. So I think it's an interesting thing to talk through. We don't have to do it now, though, but if we have time in the agenda, that'd be… I think that'd be nice.
Jack Berg 00:19:09 I think we have time in the agenda. Why don't we… why don't we give this a shot?
I'm gonna pull it up, by the way.
In a readable format.
Right, so… So, you're not the author of this, but maybe you can give us an introduction, and what problems this solves, and… What you…
Ivo Anjo 00:19:32 I've worked directly with Scott, so I think… I claim all of the problems, and the credit. The credit goes to Scott, which is my colleague here at Datadog.
Yeah, TLDR, the, the idea is that this builds on top of our earlier, OTEP for the process, context sharing, and this idea is… when… when an external reader, and we're kind of thinking of the eBPF profiler, or the… or OBI, or something that is trying to, guess, to… not guess, to… to see what's going on inside the process, and to report on it.
It's that external reader, because all of our SDKs are storing information such as what's the current trace ID, or what's the current span ID, in a very library-specific kind of way, because there was never any situation where we needed to not do that. Like, it's very hard for the BPF profiler to figure out, oh, what's the current span IDs, what's the current trace ID, what's, like, some of those things to do, like, correlation. So.
the idea here is by creating this standard mechanism where the SDKs can either use this mechanism as the source of truth, so they can actually say, like, okay, we always store this information there. Or they can use this as a kind of a site mechanism, where they keep their own, like, existing mechanism, and they say, like, oh, let me just write the trace ID and the span ID and some other information somewhere, so that the outside readers can access it.
Then, the outside profiler can kind of say, oh yeah, this is the samples that I gathered.
Related to this trace or this pan, and so this gives this kind of, like, mechanism that the outside tool can, correlates what's going on with the SDK going… that is inside the application.
I think that's the… 2-minute pitch.
Josh Suereth 00:21:32 Alright, so I just read your updates from my comments, and honestly, I don't think this solves the problem.
So if you can scroll, whoever's presenting, if you can scroll to where, what's it called? Attribute Key Map Dictionary Semantics.
Jack Berg 00:21:48 In the, in the, you know, summary view of the PR, or…
Josh Suereth 00:21:52 Yeah, yeah, yeah, like, we should read what's actually said, because it… so they added a new commit. We could just read the commit if you want, but there's a lot of context here. But effectively, I don't think what you're proposing works.
And I think you're gonna get corrupted reads. And you need to specify how multiple readers will read this data, particularly because you're going across different languages and different, you need to have something that's actually safe for languages to do. You cannot leave it outside the scope. So here it says, keys do not need to be registered at process startup. When a key is appended, the SDK must update attribute key map.
The, the, the, the paragraph below that.
The spec does not define how threads coordinate on this update. Implementers may use a mutex or mutation that satisfies the update. The problem here is you have to mutex between the process writing it and the process reading it.
And they're different processes in different languages. And so if you don't specify how that is done.
you get corrupted data reads. If I remember correctly, and again, you can correct me if I'm wrong, attribute key map is inside of a protocol buffer.
Right? Protocol buffers always have length encoded, you know, information. So since it's nested inside of a protocol buffer, it's not like a piece of memory that you just expand key-value pairs in. It's literally, you have to change the entire block of memory.
So you need to define a way that says, hey, this common piece of memory is being overwritten, don't read it right now, it's not safe, or you'll corrupt memory, right?
So.
Ivo Anjo 00:23:26 There is… the process context, OTEP does define a mechanism for that. So the gist of the mechanism is that, it's, there is something that the outside reader can observe, and so when an update is ongoing.
the writer of the update will kind of write a zero to the update at field, and this is the signal to the reader that they can… that an update is ongoing. So there's a few situations, so either the reader observes, like.
the, the, the… The previous one, or updates the newest one, and if it observes the in-between, the reader can detect that it observes the in-between state.
Because the… the spec states exactly that you should see the first… the same… the same update value at the beginning and at the end, so you read it twice, so you use that to kind of match. Was there… was I racing, and did I, did I, miss something? So, I claim that this update protocol solves that.
Josh Suereth 00:24:35 Okay, so basically, there's a block, there's a header block that writes a proto, and you have a version string at the top and a version string at the bottom, and you should read the same thing at both sides. So if you have a corrupted read and you validate that the thing is the same, okay, that's fair.
And so then it can be… like, you need the reader to understand that it has to continually, like, spin-loop reading until it gets a not, you know, corrupted read, right?
And then you also…
Ivo Anjo 00:25:03 One of the options.
Josh Suereth 00:25:05 Yeah. Now, the other thing I'm a bit nervous about is, if we're talking about, like, threaded communication, what is your mechanism to force, like, cache flushing, so I'm not reading a cached value on one thread?
Right, where, like, the value has changed under the scenes to, like, force reading. Or is that just a client concern overall, where you want them to do some kind of volatile read, or, like, make sure they're pulling in the latest version of this block of memory from cache? So that they're not hitting, like, L2 cache?
Ivo Anjo 00:25:34 So there's… there's kind of two ways. They can check the… the updated field, so that the field can be, like, on every, one, on every sample, you can check, is this still the same version, and… or do I need to kind of read it do the full update protocol again and read the protobuf. And, like, most of the times there will be no update, so you kind of go, like, okay, no change.
Right. The other alternative is that you can also hook on the system call, step number 7, and this kind of turns it into an event emission kind of thing.
When the writer does the update, it kind of calls the system call, and if, on the eBPF side, you can hook onto this, and so kind of create an event emission where the application tells you, like, oh, you should look at… there is an update now.
If you don't want to… so you don't need to pull if you don't want… so there's both a pull and as well as a push mechanism.
And the reader can choose which one it wants, because the spec says… the writer kind of does both. The writer kind of keeps the update, as well as does the system call, so the reader has the flexibility of being able to pull or, push.
Josh Suereth 00:26:39 Push.
Ivo Anjo 00:26:39 Yeah, I…
Josh Suereth 00:26:40 I do think for efficiency, like, for dictionary issues, right, you should not be reading this memory every time, because, just the overhead CPU is gonna suck. So, like, on failure to read from the dictionary.
Where it, like, goes past the end of what you thought the dictionary was, then you go reread. Okay, and you can make that volatile on the reader side. Okay, so to confirm the writer's side then, effectively, we need, like, writers are required to have a dictionary that they maintain and own.
And that they provide some kind of single writer principle where, only a single thread can be writing to this dictionary at a time.
Ivo Anjo 00:27:22 Yes.
Josh Suereth 00:27:22 Right? And they're responsible for the concurrency on the SDK side, and because of this, verification you have, you're expecting to have spin reads from readers who need the data.
Where we use the header to make sure that things are consistent.
Okay.
Ivo Anjo 00:27:41 Yes, I think that's… that's it.
Josh Suereth 00:27:44 Okay.
Yeah, I think… okay, I'll read through it. That seems to make sense to me, in terms of, like, I think this'll work. You already have this prototyped and implemented?
Ivo Anjo 00:27:56 Yes, we have this working, with, with, the Datadog Java SDK. We're also experimenting with PHP and, What's the other one? Well, we have implementation, we have a PR for, We either have a PR or a branch for UTLRAS to do this, so we have a few, like, trying to implement this in a view, like, both OpenTelemetry as well as Datalog SDKs, too, and, like, so far it seems to work. And we also have the reader code for the, we have PRs for the reader code.
in the eBPF… OpenTelem 3 EBPF Profiler repo, so that you can kind of see, okay, how does this look from the reader side? I'll… I'll throw in a link. I have the link, here.
Yeah.
Josh Suereth 00:28:43 I… you might want to think about, both for PHP and, say, Python, providing, like, a CABI or, like, a Rust-based CABI that, we could reuse in those other languages.
that kind of keeps the… again, I sent you OTLPM maps, so you can see how I was doing dictionary management in that.
But that was where, we provided something that was kind of native, would handle multiple threads, if you will.
So you're not relying on runtimes that kind of don't really have a strong threading model. You're relying on something else to do… to provide that behavior. I'm also curious how you're gonna handle this on Node.js.
It might be a little bit easier, but I'm just… I'm curious how this works across all the different things that you might be observing, right?
Ivo Anjo 00:29:34 Yep.
Josh Suereth 00:29:35 So, but…
Ivo Anjo 00:29:36 Node.js… oh, go ahead, sorry.
Josh Suereth 00:29:39 No, no, go ahead.
Ivo Anjo 00:29:40 I was going to say, for Node.js, we actually… we have a working prototype for this as well, and the TLDR for Node.js is that You don't, Given the way the runtime works, the… you will still kind of have this, you will have the process block, that works fine, and you will have the… the… the per thread context is no longer per thread, it's per, like.
Node.js context, and so instead of you hanging this piece of information off of a native thread local, we will hang it off of the internal VH structures.
So the reader will need to know, like, oh yeah, I need to follow this pointer and this pointer and this pointer from the internal V8, and then it… he will find the same payload. So it's the same payload, but needs to be, per node's current active context, because it was not, like, very, Doable to hook on this on a native thread local.
Josh Suereth 00:30:38 Yeah, yeah, that makes sense. Okay.
Cool. So that, that actually sounds, that sounds reasonable. So, again, to recap.
Writers need to ensure, consistency and concurrency of the dictionary.
The dictionary can grow up to a maximum, at which point we need to have some sort of error mechanism for it. And, there's a system in place for readers where they will actually be able to detect corrupt reads and retry until they get a valid read.
Yes.
Okay, and we also assume only one writer per, like, section of memory. So if that writer has a, you know, what do you call it?
Why is my brain not working? An ID that goes up all the time for the version number, we're totally fine. We're not gonna have, like, corrupt rights from the same process trying to write to the same block of memory, because inherently, in your architecture, you're picking different, like.
Memory bounds for each… Process, right?
Ivo Anjo 00:31:41 I'm not sure. Can you rephrase the question?
Josh Suereth 00:31:45 Let me rephrase. If I run a process and I get paid 5, And, I put my thread information into a memory buffer.
And then sometime later, I die. Sometime later, PID5 gets rebooted and throws things into the memory buffer. How do I make sure that I'm not corrupt in that case?
Ivo Anjo 00:32:07 the… There is, like, a signature on the memory location, so you can kind of use that as a hint that you might not be… like, if the signature doesn't match, then this is no longer, like, a hotel process context block, so it should just ignore it.
So it is possible for the reader to kind of know, I've read, this is just garbage.
And also, the… because the reader is not… like, the reader is kind of using safe reading API, so the reader is reading this memory as if it was kind of reading from a socket, so it's just asking the OS, can you copy this byte at this address into this buffer?
the reader will try to parse the data, and we'll see, like, okay, the signature isn't there, the PProf doesn't parse, this is all garbage, throw it away, and this is all kind of… you do this in managed code, it's not that the reader will start, like, reading some memory location and segfault and just… blow up, so the reader can read it safely.
Josh Suereth 00:33:05 I'm losing my room, so I gotta go. I will, I'll be back on when I find a new room.
Jack Berg 00:33:10 Josh, the IDs are… they're… they're timestamps, not integers, or not ints, right? So, like, that helps you.
Josh Suereth 00:33:18 Yeah, that's why I was just confirming. So I think… I think we're good. Like I said, I'll read through and make some comments, but I'm probably gonna approve. So thank you, Bebo.
Ivo Anjo 00:33:25 Thanks a lot.
Jack Berg 00:33:26 Thanks. Thanks, Evo.
All right, anybody else have anything they want to discuss with respect to that? That was a good conversation. Hopefully we get some progress there.
If not, Dan, you have the next topic.
Daniel Dyla (Dynatrace) 00:33:45 Yeah, I just tacked this on, I don't really have much prepared here, but… So the context scoped attributes, OTEP just merged, I was looking through… The OTEP itself, which doesn't specify, but the prototypes… Only propagate attributes down. So, like, to child contexts, for example.
Most of the use cases kind of assume that these attributes are being inserted At, like, the local head of the trace.
So, like, the use cases shown are, like, a tenant, or, like, an app ID, or something like that.
One use case that we have.
Is if you have something deeper in the trace, in our case, a feature flag.
And you want to generate span-based metrics, like request metrics, and include that Feature flag data on the request metric.
in a stateless way. So, like, in a… in a… Processor and the collector, or something like that.
you need the attribute to be on the span that represents the whole, like, HTTP request or something like that, which is typically, like, the server span with a remote parent.
So… what I'm proposing here… is that, We can piggyback this mechanism so that when you… Add an attribute to the context.
It not only propagates to child contexts, but also Up parent context until you reach your local route.
This is more just testing the waters to see if others would be… Amenable to that.
Or whether it would… cause obvious problems, or, if this is a problem that… that other people have, this sort of stateless, metric generation issue.
carlosalberto 00:36:01 Sorry, Dan, by the way, I do remember seeing your question in Slack. I was too busy with many things at the time.
Daniel Dyla (Dynatrace) 00:36:08 No worries at all.
carlosalberto 00:36:13 On that front, I, I would like… I mean… It sounds like a tricky thing to solve properly, My first ask would be to get people that, you know.
like, to check whether this is something that people in other Sikhs would need, you know, and how important this is.
Jack Berg 00:36:34 Dan, it seems like the problem that you're trying to solve, and maybe I'm misunderstanding, but I've thought about this a little bit too, which is, like, like, if you need whatever attributes you're going to be setting to be present on, like, everything within let's see, an HTTP request context, you need to have access to, like, that point in code, you know, where the HTTP root span is sort of established, and you need to add the attributes there so that they're present on everything below it, and that's, like, a bit of a challenge.
Daniel Dyla (Dynatrace) 00:37:09 Yeah, we don't actually need it on everything below it. We really only need it on that one span. It's just this mechanism already is putting it on everything. Like, it propagates to children.
And copies at spam start.
Copies attributes onto, like, every created span and log and metric point, for that matter.
So, I guess what I'm… what I was proposing was just to… to make that bidirectional, rather than unidirectional.
Jack Berg 00:37:45 So the things that I'm going to… I'm gonna, like, point out the obvious issue, which is, like, you know, you've got a span.
And, you know, you need to walk up the tree to its parent.
How do you get a reference to… How do you get a reference to those spans, and how do you ensure they haven't ended?
Daniel Dyla (Dynatrace) 00:38:06 Well, in terms of how you get a reference to the… spam? There is no mechanism for that right now. So that's, like, the major… the major problem with it is that there is no mechanism for this right now. We would have to… define that.
In terms of whether the span is… Closed already, or ended.
That would most likely just have to be an accepted limitation, that if a span has already ended, then… You can't change it.
In our particular case, where we're looking at span-derived request metrics, that doesn't matter so much, because if the span's already ended, you can't affect its duration Anyways… But yeah, it is a limitation of the mechanism.
carlosalberto 00:39:01 There was.
Jack Berg 00:39:01 So, back?
carlosalberto 00:39:02 Look, Kev.
Jack Berg 00:39:03 If I can ask one more question, so, you know.
You've got this, like, the root span of, It's like a local root span. It's the root span within a process.
Daniel Dyla (Dynatrace) 00:39:14 Yes.
Jack Berg 00:39:14 You know, you've got… you've got… you're somewhere within the application code, and, you know, you… you want to, after you've established some context, maybe parse something, maybe, like, fetch something from a database or a cache, you want to attach some piece of information onto that local root span.
That was only sort of accessible, available, like, somewhere down in the application's context.
Is… Is that… is that about right? Like, because I guess, like, my first instinct would be, hey, try to… try to just… take whatever that processing is and move it upstream, like, before that local root span is established, but maybe the issue with that is, like, you know, the code, the context, whatever you're trying to attach doesn't exist at that point, and it's not.
Daniel Dyla (Dynatrace) 00:40:04 Yeah, that's…
Jack Berg 00:40:05 somewhere.
Daniel Dyla (Dynatrace) 00:40:05 That's exactly the issue.
Jack Berg 00:40:07 Yeah, so it's not until later, somewhere down the call stack, that, like, you've… you have that information that you want to sort of, you know.
Daniel Dyla (Dynatrace) 00:40:15 Yeah.
Jack Berg 00:40:16 navigate.
Daniel Dyla (Dynatrace) 00:40:17 That's exactly the issue. And the other… the other mechanism that we've been considering, and I just don't have a proposal ready for it yet, but… was to… add an API service like… Set root span attribute, or something along… like, a dedicated mechanism for this.
the… the reason that I haven't done that yet is because this is already in the works, and it seemed like maybe we'd be able to piggyback off of it.
And I don't know, whether other… I guess it would really come down to whether other people generating metrics from spam data are having this problem or not.
And I… I don't know… Whether this is a problem that everybody has.
Jack Berg 00:41:08 Raquel?
Michele Mancioppi 00:41:10 I… I think that this mechanism is something that would come very much in handy for a bunch of use cases I see with end users, where they need… they want to add to OpenTelemetry some sort of transaction identifier.
That is coming from a system they invoke.
And they tend to be very, very confused by the fact that they usually cannot put it on the client span, because the client span tends to be closed the moment the data is available to them.
And, they do not exactly know on which spans they can add it, that they can add it. Sometimes it ends up in internal spans, sometimes it ends up in server spans, and be able to effectively add This attribute to the entire chain, from where you have it all the way to the entry span, so that the first span in In this segment of the trace, in this resource.
It's something that, if we can manage to make it work, Sufficiently, generically.
It would really help customers to To get the data they need without having to become auto experts.
carlosalberto 00:42:27 But when you are calling, like, this client to a server, is that crossing, like, it's like a different service, or is it the same service?
Michele Mancioppi 00:42:34 It, it happens often, for example, when You have, people invoking a third-party service, and that comes up with some tracking identifier.
And they need to store the tracking identifier somewhere.
Very often, this is… I mean, let's face it, most of the things that people monitor are still synchronous. So, for example, the HTTP server span is open, and usually the client span is closed.
By the time they have the tracking, and if they would be able to annotate They're actually on the service pan without much ceremony, that would help them.
I have several times in the case where people just started creating internal spans just to store this information.
Somewhere.
And, it is a pain point for people that are not auto-experts.
carlosalberto 00:43:29 Yeah, probably this is a different, slightly different, because, context scope attributes are for, like, within the process only.
What you're saying, probably something I had a prototype, no.
Michele Mancioppi 00:43:41 It's processed within the same process, within the same trace, in the same process, even within the same subtree of the trace, starting from the latest entry span, so span with the entry flag that's been never implemented in any SDK.
That is something that would really help people out.
Daniel Dyla (Dynatrace) 00:44:06 Yeah, so the proposal… I think what Michele is talking about is, like, a leaf node that makes a remote request. You get some identifier back, and you want to attach that to the whole branch of the trace, crawling all the way up to the root.
Which is very similar to… to what I'm describing.
Michele Mancioppi 00:44:28 It seems to me it is the same thing, just a different application of the same idea.
Jack Berg 00:44:34 So, a couple things I didn't understand about Mikael's, you know, statement. Like, why is the client span closed? Why is that leave span closed? Like, you know, you start a span, you make a request, that span is representing that request's unit of work.
That request returns a bunch of information, maybe in the response body, in response headers, one of which is this identifier that you want to attach.
Michele Mancioppi 00:44:56 I'm lost.
Jack Berg 00:44:57 And, you know, why is the span closed?
Mostly.
Michele Mancioppi 00:45:00 Most of the times, those client spans are auto-instrumentation spans.
And they close before the payload returns in application space.
Jack Berg 00:45:12 Okay, okay, so… okay, so it's like a lower level thing, so the underlying HTTP client is sending a request, getting a response, and as soon as that response is received, the HTTP client library, you know, closes this span, and the application code now, like, has a response body with this identifier, and it's like, okay, now what?
Michele Mancioppi 00:45:35 Yeah.
Daniel Dyla (Dynatrace) 00:45:36 One way that we solved that in Note, because we get similar requests, we have hooks available. So we have, like, response hooks that… Some… you can register a callback function that's called before the span ends, so that you can do something with the response and attach things to the span if you need to.
That's obviously a much simpler mechanism.
Michele Mancioppi 00:46:02 It's also something that I've seen only Note.
NET has also a bunch of these hooks.
Daniel Dyla (Dynatrace) 00:46:09 None of that is specified, or even recommended, or anything, or consistent in any way.
Josh, do you have your hand up?
jmacdonald 00:46:20 Yeah, I was… I'm listening, and I've seen some of these requests before. I don't have a great deal of feedback on exactly the feature that Dan and others are talking about, but I wanted to connect it with a very old, I guess, maybe defect or an omission from OpenTelemetry specification for tracing.
When we brought in OpenCensus, if you recall, there was a field on the span that was the number of children, the number of child spans that you could use to tell whether a chase was complete, in some sense. The mechanism that you need to compute the number of children is also comes out of this topic. Like, we… if you… if you are able to propagate backwards the number of real spans that were created, then you can also have the parent count the number of spans. So I've seen this pattern, I just wanted to say that.
Jack Berg 00:47:09 Yeah, Josh, as these folks were talking, I was thinking about, like, maybe a solution for this class of problems is to adjust span processor with a hook that allows you to, you know, hook into whenever a child span is added.
And that way, you know, a span processor could, you know, for the local root span, could listen for, you know, child spans being added, and do something as a result, like, for instance, hoist a piece of data from a data span… a child span all the way up to the parent span.
And, you know.
that you would still have to deal with some of these issues about whether the span has ended or not, and deal with those semantics, but… and also Mikael's point about, like, the child span doesn't even have this identifier, in this case, so you have to solve that as well, like, you might have to still jump through some hoops to somehow get this callback invoked, but… That's where my head went, was, like, similar to what you were talking about. A mechanism that allows you to count child spans. It looks similar in shape to a mechanism that allows you to hoist data up to a local root span.
Daniel Dyla (Dynatrace) 00:48:18 Yeah, and we initially started with a… with a span processor, to handle this, but, particularly, like, in Node.js, there's limited, support for things like weak references, and making it reliable and not leak memory, is… Not as trivial as it sounds like it should be.
carlosalberto 00:48:41 By the way, there was a prototype, or some idea in the original attempt by Christian about bubbling up, but it was very complicated.
I can probably go and dig a little bit and provide some feedback, like, prior art style.
Daniel Dyla (Dynatrace) 00:48:58 Yeah, it is possible. So, in Node.js, at least, I think this… Bidirectional mechanism would be fairly easy to do, but that might be… a consequence of, like, decisions that we made that were not specified. I don't know how… whether it would be a problem in other languages or anything like that. I haven't… it would need prototypes. Right now, the context-scoped attribute prototype, at least in Java.
just when the span is created, it looks at the context, says, give me all these attributes, and attaches them to the span, and that's, like, the whole mechanism. That's all it does, basically.
And then some bag, too, on the context for those attributes.
But at least in… node… every, like, child context has a reference to its parent context, and you can extract the span out of that if there is one fairly easily. So you can just say, like.
Parent context, you know, all the way up until… You have a context that doesn't have a parent.
Which is the root, which never has a span, so you ignore that one, and you go to the one previous, that's always the root span. So you just look for that, and… and that's it every single time.
It would be… trivial may be the wrong word, but not all that hard in the GIS SDK to handle this right now. But I don't know whether other SDKs Would have more challenges.
Jack Berg 00:50:30 Dan, I, I tend to think… my intuition on what you're saying is, like, this seems like an important capability to have, it seems useful.
It seems somewhat like it could be related to context-scoped attributes, but, also polishfully orthogonal. Like, I don't think it's a slam dunk that if you set context scope attributes, that you want this behavior of them, like, back propagating up all the way up the span hierarchy. Maybe it's, like, conditional, maybe it's opt-in, maybe there's some other sort of predicate or selection criteria for which ones it gets back propagated to.
But, like, you know, so I, like, you know, prototype, context, skilled attributes. I think this is… this is, like, you'd want to track this feature separately than this issue, rather than… and maybe they, like, converge, and maybe there's some things related, but I don't think you want to get, like, bogged down by, like, contact… lose sight of, like, what you're saying through contact scoped attributes.
Like, one thing that comes to mind is, like, if we went down this, like, solution direction of, like, having some sort of extended span processor, or something like that, what if there was a callback that you could invoke when, like, anytime you set context-scoped attributes on a child context, somehow that gets a callback and the span processor is invoked that allows you to access those context-scoped attributes. So, like, a span processor with a reference to the local root span could, like, detect that situation and, like, conditionally hoist up that data.
Something like that.
Daniel Dyla (Dynatrace) 00:52:11 Yep, that would probably work for us if it… if that's… If, if, I'm understanding the mechanism you're describing.
I… I do think that it's worth discussing What is the definition of context in… in the… Oh man, what an overloaded word. In the context of context-scoped attributes, it's worth… Talking about what is the definition of context, because if you have somewhere in the middle of your trace.
You have a spam.
This span is in the context of a request.
So if I attach an attribute to that context, do I expect it to be attached to the request, which most people would consider to be, like, the HTTP span?
In… You know, cases where you have… I don't know, the standard library HTTP server, and then some server framework, and then some application framework, you may, in the OTEP, it describes setting, like, a tenant ID or an app ID or something like that. If I attach that tenant ID, I might expect that to show up on those parent Cause it is still a part of the same… request context.
So I think it may be surprising to users if it only propagates in one direction.
Jack Berg 00:53:45 Yeah, like, to me, the way that you solved that was to make sure that you set those context scoped attributes early enough in the app, in the request lifecycle, that it was…
Daniel Dyla (Dynatrace) 00:53:53 Yeah, but if you…
Jack Berg 00:53:54 propagation. Exactly, so that, there's, like, practical considerations, which is, like.
Daniel Dyla (Dynatrace) 00:54:01 And even…
Jack Berg 00:54:02 that.
Daniel Dyla (Dynatrace) 00:54:03 the particular… in the OTEP, I think tenant and app ID are the two big examples. Both of those… are somewhat likely to come from, like, a database call or something like that, that's not even… you may not have access to it right at the head of your local trace.
So I… I think it's… Yeah, I think it's somewhat likely to be a problem.
Anyways.
Jack Berg 00:54:31 We've got some hands up. Mikael, you first?
Michele Mancioppi 00:54:33 I have, a question that popped up in my head.
So we are… we're talking about, automatically adding to spans, or to pieces of… of telemetry in the context attributes. And, this, brings up, another of the big sources of confusion that I experience with end users.
They expect this behavior with baggage.
People expect this behavior of having the stuff added as attributes on the spans being collected, the logs being created, the metric data points.
Throw the baggage.
Is it something that… do we have any OTEP considering this?
carlosalberto 00:55:19 You mean, like, basically you're writing Bagash, and spans and metrics are getting stuff from Bagash, getting added? That's kind of part of a follow-up that we will be having as part of this, and Josh can talk about that.
Josh Suereth 00:55:32 Yeah, I'll just briefly mention, Michelle, I asked the same question in the previous proposal around context attributes, and the inability to answer it is what blocked the whole thing.
For a very, very, very long time.
I agree with you, I think baggage is super critical, and we really, really need to get it there. I think what Carlos has here is a great start, and I think, like, let's… like, this is the foundation that we then layer baggage-related things on top of, and… I agree with you, like, baggage should be our end goal, it's just, I think this is the foundation to get there. So let's, you know, take that as step one, step two.
And I'm trying not to make the mistake I made last time of saying, hey, let's solve baggage right now, and then nothing happens for, like, 3 years.
carlosalberto 00:56:17 Yeah, I was prototyping how backgash would work if this is in place already and it's straightforward, but yeah, that's a good foundation. What I want to say in my turn, is that, Dan, I think it's very interesting. I don't know… my feeling, honestly, at this very moment is that this is orthogonal.
what you… what you are requiring, what I really suggest we… you open an issue, and I try to, follow up with that So… Either… whatever this way we take, we should really document these things, you know, so the user is not surprised, or, you know, we get proper documentation, and everything is super clear, you know?
Jack Berg 00:56:52 Carlos, why don't we create an overall tracking issue for, context-scoped attributes related child issues, things like prototypes, things like stabilization, ultimately, and things like, like, other things that could be related and might want to be solved, you know, using the same capability set. And this issue that Dan's talking about would be sort of a child issue under that, so we don't lose track of it.
carlosalberto 00:57:16 Yeah, good call. I was meant to do that after I merged the tab. I forgot, it's a good call out, I will do that.
Daniel Dyla (Dynatrace) 00:57:26 Yeah, we're running out of time, with, you know, 15 minutes on my 2-minute topic, sorry.
But I… I guess, as far as next steps go, I can create the issue for this, but what I wanted to say is, like, this… this… the reason I chose this context mechanism is because it's what's here, and it was… I didn't… I wanted to avoid creating new API if something that was already proposed and accepted could be made to fit the use case.
I do believe that bi-directional propagation would be less surprising to users. I think that… it has downsides, like data duplication and things like that, and how do you deal with conflicts? Like, there are definitely some issues that we would have to consider, because if two different parts of the trace try to set the same attribute, what do you do with those?
I had not considered the interaction with baggage at all.
But… I guess in terms of next steps, I can create the issue, but it… this sounds like… a mechanism that people at least find interesting, right? Is it worth following up on and creating an issue and a prototype for it?
Jack Berg 00:58:39 Yeah, this class of problems is definitely something I've come across in the past, so I'm with you.
jmacdonald 00:58:48 Yeah, same for me. I've seen lots of variations on this same theme. I wanted to remind us of a few more. When it comes to sampling and links, we've added the ability to add a link, and one of the use cases there was you have a child span that is the place where you might have the link, and you'd like to propagate that link to the parent in order to influence its sampling decision, or to tell the parent that it's should be… it should write itself out because a child was sampled, and so on. So sampling propagation, comes up for me here as well.
Daniel Dyla (Dynatrace) 00:59:25 That would not necessarily be an attribute that gets attached to the span, right? As much as it is, like, context metadata used by the tracing system itself.
jmacdonald 00:59:34 Right, it's almost like causal… like, we have a causality chain that's, like, forward propagated right now from parent to child, and what I think I'm hearing is that through the life of a span, you then propagate backward something. When you finish your life, you span… you propagate some causal… causal information back to the parent that it can use, which is tricky, but it's, like, very… also very real, and we've seen it a bunch of times. Another… I mean, on the same topic, it's like, I… When I have a parent and the child is sampled, I would like a way to annotate the parent, to say, you know, I had a child that did not get recorded here, like, I want an event to say there was a child that was skipped, for example. It's all propagation from child to parent in my thinking.
Jack Berg 01:00:18 All right, we are at time, so thank you for this discussion, everyone. Follow up asynchronously, and yeah, we'll see you… we'll see you in Slack and on GitHub. Take care.
