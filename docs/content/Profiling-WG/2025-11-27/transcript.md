SIG: Profiling WG
Date: 2025-11-27
Duration: 44 minutes
============================================================

## Zoom Recording Transcript

**Frederic Branczyk** 02:26 Sorry about that.
How can I remove this thing?
**Felix Geisendörfer (Datadog)** 02:32 You're the one who brought the AI along?
**Frederic Branczyk** 02:36 That seems to have happened automatically. Let me see how I can turn this off.
**Felix Geisendörfer (Datadog)** 02:44 I mean, the meeting is recorded, so I guess it doesn't matter.
**Frederic Branczyk** 02:47 It doesn't really matter, but still.
I literally set this up today. I didn't even know that this was gonna do this.
**Felix Geisendörfer (Datadog)** 06:03 Alright, so it's about 5 minutes in, so I will get us started.
Yeah, thanks everybody for joining, and to the special Thanksgiving edition, which I guess is mostly EU attendance today.
I will take us through the previous action items, and then we have some agenda items in the Google Doc for today. If anybody has some last-minute ideas for new agenda items, I think we only have 3 agenda items on the list, we might have room for more. Feel free to add anything you might want to discuss.
I'm gonna share my screen.
previous action items, I think.
Alexi is not here today, and probably off for Thanksgiving, so probably I'm just gonna mark his action items as no updates, out for… Not… Not attending. And if somebody has an update on one of Alexis, please, Let me know, otherwise I'll just drops it in.
Moves C's up to the top.
Okay, that brings us to the next item. Florian, any updates on OTLP to PPROF conversion?
**Florian Lehner** 07:34 Yes and no. Yes in the sense that… I pushed, PR for the OpenTelemetry collector contract, so 44357.
That's the implementation, and… The no part is the semantic conventions, there still requires also feedback.
**Felix Geisendörfer (Datadog)** 07:58 Feedback from… for us from our.
**Florian Lehner** 08:02 From our sick, yes.
So, the, semantic conventions, SICK wants to see that the profiling SIG is conformed with this change.
I see, okay, then…
**Felix Geisendörfer (Datadog)** 08:16 Let me make note of that.
**Florian Lehner** 08:19 And for the auto collector contract change.
Yeah, I think it pushed it this week, last week? I pushed it, with… since the last meeting, and, yeah, feedback's needed.
**Felix Geisendörfer (Datadog)** 08:41 What needs feedback? This one?
**Florian Lehner** 08:44 just… Yes, but this is new, so.
**Felix Geisendörfer (Datadog)** 08:49 Okay.
Then I will fix this one slightly less.
Called out, but also needs reviews, feedback, right?
**Florian Lehner** 08:58 Nope.
**Felix Geisendörfer (Datadog)** 09:01 Okay, cool, thank you so much for working on this. I think I can definitely try to take a look at this, ASAP.
Alright, any more thoughts on that? If not, I can take us to, Ross says context propagation OTAP.
Maybe Ivo has things to say there?
**Ivo Anjo** 09:26 I do.
Go for it. So, yes, so I, I, raised the OTEP with the hotel specification C, this, on, on Tuesday, and, I think the big part of… the big feedback I got there was, why are we using, like, a custom proto format? Why not just use the… hotel resources, existing proto, also because, that would, make it kind of, like, trivial to support some of the other changes that are being made, in terms of, like, identifying resources in hotel, versus, like, if we have a custom proto, then we kind of needed to… maybe we would need to then change… later change or make additions to support that.
So, I, I think that kind of makes sense, so I've updated the specification, the OTEP, with, basically throwing out our custom proto, and, using the, resource, the hotel resource message instead.
And, and yeah, this will invalidate the PR I had in the Profiling SIG repository that was kind of adding the old proto there, so if we… I'll probably close that PR if we like this direction.
And, yeah, I think the… from the profiling seeing, it'd be interesting to know if anyone has any, ideas on why we should not go in this direction, because, to be honest, this direction seems reasonable.
**Felix Geisendörfer (Datadog)** 11:07 So… Let me… Take a look real quick.
**Ivo Anjo** 11:15 Yeah, if you scroll down, I copied the, the resource format there, just to… as a reference, so if you… yeah, it's that one, the payload format. So that's the proto.
And then it references the common proto, which is the key value, but key value is just, like, a pair that can include… can be of string value or other kinds of value, so it's a bit more flexible than what we had before.
**Felix Geisendörfer (Datadog)** 11:42 Gotcha. And then we basically rely on semantic conventions for, like, the fields that we would… the attributes we would care about, right?
**Ivo Anjo** 11:50 Yeah, yeah, I still, like, this has been something I've been trying to keep in there, although, yeah, if we don't like that, I can remove it, but I think it's kind of interesting for SDK implementers to have a list of, like, this is the ones that we are kind of… hoping to use in the BPF Profiler, and we can kind of add more there as a, like, oh, it would be nice if you can supply us these ones, but you can supply all of them or none of them.
**Felix Geisendörfer (Datadog)** 12:21 Okay, seems reasonable to me, but I definitely need to set aside a little time to go deeper on this. Anybody here have, thoughts, who had a chance to look already, or has questions?
Going once…
**Florian Lehner** 12:42 I'm going twice.
Maybe myself.
I like the idea, new direction, I really like it.
I think there are current discussions with TC on how Profiling should handle resource attributes.
And this will maybe introduce new fields and elements, and I'm wondering if this will conflict with this approach.
Right.
**Felix Geisendörfer (Datadog)** 13:16 Why would it conf…
**Florian Lehner** 13:19 Because it would introduce a key ref value.
But we don't have dictionaries here.
**Felix Geisendörfer (Datadog)** 13:25 Yeah, yeah.
**Florian Lehner** 13:29 Yeah, then never mind, sorry, lost in profiles.
**Felix Geisendörfer (Datadog)** 13:35 No, no worries.
**Florian Lehner** 13:37 Yeah, but liked… I liked the idea.
**Felix Geisendörfer (Datadog)** 13:41 Okay, then I'll just shorten this for the sake of the transcript.
Boop.
**Ivo Anjo** 13:48 If I can add one thing, I had mentioned in the previous meeting that, I was going to open a PR to copy… move over our examples to the profiling, to the Sikh profiling repository.
I started doing that, but haven't finished, because I decided to also update the examples to use the latest format, so that's why I haven't opened that PR yet, but I'll have it soon.
And, yeah, hopefully the specifications will let us know what are the… if there are any concerns, or if we can move forward with this.
And, Finally, on the thread level stuff, that's the more interesting part, we have made some good progress on getting DD Trace Java or, like, Java, library to use, TLS Desk and, WireApp, like, something similar to what, what the, both polar signals and the Elastic have already had. So hopefully, not this week, but, like, in the next meeting, we'll have some of our results and can hopefully start a conversation around that.
**Felix Geisendörfer (Datadog)** 15:10 Okay, cool, thanks. Sorry, my daughter distracted me. If you can fill in transcript information here, that'd be great. But I think I captured the high level.
Yeah, then I guess, Ibo, one thing to clarify also, for the sick, you probably want more refuse from the sick as well, in addition to, other, hotel community members.
**Ivo Anjo** 15:33 Yes, I think since this is, like, a big part of this, we're kind of selling this as we want this for profiling, having more reviews and, like, from the profiling folks, so I think it makes a lot of sense.
**Felix Geisendörfer (Datadog)** 15:48 Yep.
Okay, cool.
Thank you so much for all the work on that.
Then we have Jonathan, who I think I saw here, or does anybody have any last… 6 here, huh?
Yeah, then Jonathan, do you have any updates on these?
**Jonathan Halliday (IBM)** 16:11 One of them's merged, the other one's waiting on people to check my little box saying, I like this. So if you haven't done that, please do it.
**Felix Geisendörfer (Datadog)** 16:21 Okay, this one needs refuel.
I'll mark that.
This one is merged. Okay, so this one, I think we can take from the agenda, right?
724… I already did. Okay, yeah, if somebody could copy it to archived action items as well, that'd be great.
Then yeah, everybody who has the chance, please review this PR from Jonathan. I will also try to take a look.
Do we have Alban here today for… kernel security… It's not.
Okay, Maybe, Florian, we want to do the… the next one first, the P data, because we have updates on the… on the benchmark results below on the agenda, so maybe we'll cover this, and then we jump to the… Head in the agenda.
**Florian Lehner** 17:41 Sounds good.
**Felix Geisendörfer (Datadog)** 17:48 Do you want to talk about the P data?
**Florian Lehner** 17:51 Yes, finished.
No.
**Felix Geisendörfer (Datadog)** 17:56 Yeah, we used to have, we used to use, time.time.
**Florian Lehner** 18:02 as a duration, but time to time points to a point in time, not a duration, so conversion was really… Not nice, I would say.
Now it's a UN64, representing nanoseconds, like it's in the definition, and it will go out with the next release of Collector, I think that's scheduled for next… next week, Tuesday, something.
So collector and collector contract are already updated.
**Felix Geisendörfer (Datadog)** 18:34 Oh, good.
Cool. Thank you, that's great.
Yeah, I think we'll circle to this, in the… I guess we can go ahead with it. Let's go to the benchmarks.
the agenda below, so I think I'll just jump us here.
So, basically, Nev and I have published, a few minutes before this meeting our benchmark results, for Florian's PR to add, dictionary capabilities to resource attributes via key references and value references for strings. For those who haven't seen that, it's this PR right here.
Basically, the two main modifications are the any value type, and now, instead of directly referencing a string value, also reference a string that is in the profiles dictionary, which is only meant to be used if This is data for the profiling signal, and there is a profiles dictionary for the other signals that would not be used.
And… Similarly, for the key value, message, there would be a way to reference a key, so you don't have to repeat the string for a key multiple times. And… Tigran and others have asked for benchmarks that show whether or not we actually get something out of this, and this is what, Neha and I tried to answer, and I guess the, short answer is we think it's really helpful for the uncompressed sizes. So basically what we did is we did, we took some… workload in Kubernetes, where we had the OpenTelemetry demo running.
and another Python application that frequently forks. And we collected data from this environment using the eBPF profiler, using the current version of OTLP, And this is what's called baseline here.
So we collected, this, this amount of data, which is, Don't even know. This is 1.5 megabytes, maybe?
Of data, in uncompressed form. This was 20 separate payloads, so profile export requests, are contained.
And, then what we did with this data is we, implemented a tool that can actually, use the new, OTLP format from Florian's PR, so we basically generated the Go bindings for that version of the OTLP, and then we, Started, first of all, by just, splitting, the data by process, because currently, maybe this is illustrating it well, currently the profiler produces data that kind of looks like this. Every container is sort of its own resource, and then the samples actually have a process executable pass, a process executable name, and a process pit, which you can see here.
But within a container, you usually have a limited number of processes, so this keeps repeating frequently. And… But maybe the bigger problem here is that this is not aligned with the OpenTelemetry spec, which considers processes to be resources. And so, what we want to do is we want to change CBPF Profiler to split by process, which is basically the idea of Moving those attributes that are belonging to the process up into the, resource attributes here, so we would move it up here.
And the problem there is that we now, have many processes, potentially, who have the same executable name, the same executable path, and the same process pit. And unlike, within our, profiling format where we can actually use dictionaries for encoding these. We cannot use dictionaries in the resources right now, because that's not supported. So, what this benchmarking tool also does is then it takes the data after splitting it and applies dictionary encoding using the new changes to OTLP proposed in Florence PR.
And yeah, this is basically for that workload that I described earlier on. You can see that not having the dictionary on resource keys and resource values gives a large increase in OTLP, uncompressed data volumes.
And if we do add the dictionary capabilities as proposed in 7.33, we see about a 41% compression gain, sorry, a gain on the uncompressed payload sizes.
For the GCSIP, compression, like, after we apply GSIP6 compression, which is the default level for GCSIP, which I believe we use for gRPC, we see about a 4% reduction.
That is relatively modest, but we still believe that these 41% are worth squeezing, because this will A be how much data we need to feed into GSIP for encoding and decoding, it will also be the amount of data we feed into protobuf for marshalling and unmarshalling, both on the eBPF profiler side, but also on the collector side.
Going into the collector, going out of the collector, and maybe most importantly, these 41% are also gonna likely correlate with the memory usage In the collector, and significantly reduce the memory usage of processing profiles in the collector. So yeah, this is basically… our results. You can read a lot of details here. We've documented the methodology. We have a link to how this Kubernetes environment was set up. We believe we can reuse this in the future if we want to do similar experiments.
And you can reproduce this, you can run this code. And here's some additional files that we also tried, where you can see different gains. So this was the main one, the headliner that we give, where there's frequent forking.
In environments where there's less forking or less activity, the results can be less, yeah, good, but as you can see here, it's always a win. Like, there's no payloads that we found where it's not a win, and these were essentially idle environments, so I wouldn't… I wouldn't look too much into these. I think this was before we added the forking Neaf, is that correct?
**Nayef Ghattas** 25:12 Yep.
**Felix Geisendörfer (Datadog)** 25:14 Yeah, so basically, this is a… basically, this is the OTEL demo without adding a process that does a lot of forking, so even on just a normal OTel demo, without doctoring it for the workloads that we were worried about, it already shows 25%, and if we do have frequent forking, we see 41% here.
So, yeah, this is pretty much the results. Any immediate questions? We definitely would appreciate reviews on this and comments, but hopefully this will help moving this forward.
**Florian Lehner** 25:46 Thanks for the work.
**Felix Geisendörfer (Datadog)** 25:49 Yeah.
Thank you, as well, for pushing out the change.
Yeah, if nobody has any thoughts, that's also fine, take your time reviewing it. I think from previous discussions, there wasn't anybody skeptical about this being useful in this group. I think this is mostly for convincing the TC and maybe the collector folks, including Bachdan, who was skeptical about our dictionaries in general, I would say.
So hopefully this will unblock the resistance we are facing there.
Cool. Then, I guess… He's also notes, And I guess I can take us to the beginning of our agenda today. Florian, you had, Something about renaming message location to message.frame.
**Florian Lehner** 27:02 Yes, there was a request on our, on the hotel profiling Slack channel.
If you could rename the message location to message frame. In the past, we use, or the message location as we use it today, originates from PTROF.
And, I see the point that it might be confusing for some users, that If handing a stack trace message frame is more intuitive than message location.
But I don't have a strong feeling on that, so, yeah.
I just wanted to raise this.
Get some feedback if we want this or not. Personally, I feel that's… An implementation detail that most users will not care about… So… I would…
**Frederic Branczyk** 28:03 Sorry, I would argue that frame is more confusing because there are inlined frames as well, right? So… Like, we have the lines, array, so, like…
**Felix Geisendörfer (Datadog)** 28:17 Yeah.
**Frederic Branczyk** 28:20 I personally would find it more confusing if it was called frame.
**Felix Geisendörfer (Datadog)** 28:24 Yeah, if you call it physical frame, it's true so, right? Like, that is, I guess, one per physical frame, and then you have the inline frames below it. Maybe that would be the proper nomenclature to call the outer one a physical frame, and the, you know, one inline frame or something, but this is kind of a mouthful.
But I don't feel too strongly about it. I can just say the first time I saw this in PProf, it took me a while to wrap my head around what they mean by location and line. It was not immediately clear to me, so I… emphasize with people who find it confusing as well, but yeah, as you said, Frederick, as a frame as a proposal is maybe too simplistic.
**Florian Lehner** 29:05 maybe I can come up… can come up with some improvement of the documentation.
That we can do on message location. That is, if people look at it, that it's more… or easier to, to handle.
But yeah, I think… I would agree with… People that, We should maybe stay with message location at the moment.
**Frederic Branczyk** 29:31 Actually, thinking about this some more, I think… Even physical frame doesn't feel right, because… You still need a single… frame in the lines array, right? And then maybe lines should be frame.
frames, but I don't know what we would call the alter thing. I think it's kind of bait-shotting, I don't think it's… I don't know how useful of a conversation it is.
I would agree with Felix, that probably the first time I looked at the CPROF, it also took me a minute.
But… Yeah, I don't know.
We had the conversation last time, I think, around… lines, right? And it came up that we maybe want to call it positions or something like that. Now we have frames? I don't know.
**Felix Geisendörfer (Datadog)** 30:37 Yeah, I would… guess, if the person who is in favor of this feels very passionate about it, they should open a GitHub issue and get a few likes on it. If they get, like, 10 likes or something, then it's like, okay, that's a strong signal, but otherwise, this seems like maybe a lower priority compared to the other things we have to worry about, and… Let's… And also, like, we actually don't try to, like, be different from PPROF for just, like, hey, we're OTLP here, like, because we still have to worry about converting between the two, and anybody who has to live in the world of profiling might find it easier if we don't just come up with new names for this.
So, I think we should stay with it unless we see a stronger signal.
Okay, any more thoughts on this?
Going once, going twice… Nope. Then I guess Christos is probably out. I don't know if Loyen or somebody has contacts on this and wants to speak about it.
**Florian Lehner** 31:54 Yes, I can jump in.
we did some, node VH testing, JavaScript testing.
And, we noticed that V24 is not yet supported, but V24 is an LTS version, and we wanted to ask if someone already did take a look.
**Frederic Branczyk** 32:14 I commented just before the meeting, because I only then saw it, but I think we've already fixed this in our fork.
I pinged, Brennan, who was working on this, on the issue.
**Florian Lehner** 32:29 Cool, bringing you.
**Frederic Branczyk** 32:30 We definitely have customers already running V24, so… and doing so successfully, and we've definitely fixed a couple of things for them, so… at the same time, I think there are, like, 3 different code paths in, or 4 in Node.js, so it's possible that there's more.
**Florian Lehner** 32:51 Yeah, if you could, maybe, contribute back to Upstream, it would be nice for us as well.
**Frederic Branczyk** 32:58 Yeah, definitely. This was, like, last week, so.
**Florian Lehner** 33:02 Cool, thank you.
**Frederic Branczyk** 33:03 But that was always the plan.
**Felix Geisendörfer (Datadog)** 33:12 Well, that would be awesome. Thank you so much, Frederick.
Okay, we are done very early today, so unless somebody has a last-minute idea for something they want to bring up…
**Nayef Ghattas** 33:25 I have a last-minute, more of a heads up. So, I was looking into OBI, which is the Open Telemetry eBPF Instrumentation for tracing, and right now they use eBPF, and they use that to generate traces.
And right now, they're distributing OBI as a sort of dedicated container that is not a collector. But in the future, they want to build it as a collector-receiver.
So right now the distribution that we have, is OpenTelemetry ePPF Profiler, which is supposed to run as a daemon set on each host.
And if they were to build it as a collector-receiver, they would also have a distribution, they would need to run on each host that would need to be privileged to use eBPF and do the logic that they have.
So maybe in the long term, it makes sense to have a single eBPF privilege distribution, for all the daemon sets that need to run on each host and do privilege stuff. So I send them a Slack message, just to float around the idea, and they seem on board with it.
So I was curious if they… that we had any… Thoughts on this?
**Florian Lehner** 34:51 I also attended the EPPF Instrumentation SIG meeting, Some… moments. And, yeah, I asked the same question.
Yeah, their plan is to integrate with Collector at some point, but at some point it's not defined.
For the EVP profile, I think.
We make it quite easy.
To use it as a receiver.
in a regular hotel collector, so if you just configure everything Rather correctly.
You can have it as a daemon set, And don't need to rely on, the EBPF, hotel collector EBPF distribution.
But yeah, combining both would be awesome. I think their deployment model is, at the moment, only Helm charts.
And, looking at our approaches with the dictionaries, I see a huge benefit for them also, as they send out a signal per process. So, they have a ton of open network connections.
And, yeah, I think both projects would benefit, if the dictionary approach would be… Used more widely, and also the… the context-sharing approach that, EVU introducing, would also heavily benefit. So, yeah.
Interesting project, A lot of stuff to do.
**Felix Geisendörfer (Datadog)** 36:40 Ivo, go ahead, I also have something after you.
**Ivo Anjo** 36:43 Yeah, I was just going to say, I was… I was going to say what Florian said, and it actually came up during the specification, see where would OBI fit within the process context. So, yeah, I think it makes sense to reach out and see how all of this goes together.
**Felix Geisendörfer (Datadog)** 37:08 Cool, yeah, so my comment was, that, yeah, I agree that we should, look into this, as well, or help them if they want to be part of the same distribution, because for OpenTelemetry users, it would be kind of a mess if they have to, like, install and run two daemon set, distributions for EB.
VPF things and pay the overhead of probably loading a bunch of code into memory that could be shared between the two processes. So… yeah.
I had one follow-up. So, you said they also send a signal out per process. I guess when signal, you mean, like, they kind of have process attributes on their, traces, I guess, right? Like, they produce traces?
**Florian Lehner** 37:57 Yes, yes, traces and metrics, and they do also the enrichment, so they have, dedicated Kubernetes I would say… a Kubernetes thing that connects to Kubernetes.
and does not use the hotel Kubernetes attribute processor. So, while we use only the container ID and let the Kubernetes attribute processor do the rest, and let the user configure, I want this attribute and whatever, they make, Predefined decision on this, and, doing all the job.
**Felix Geisendörfer (Datadog)** 38:34 Yeah.
Yeah, but I guess that would mean that we would have to expand the usage of, dictionary capabilities for attributes to other signals, so that would be an interesting.
**Florian Lehner** 38:45 I have the feeling that TC is not happy about doing so with V1.
maybe another V2 of other signals, but I have the strong feeling that This will not be a V1 topic.
**Felix Geisendörfer (Datadog)** 39:13 Yeah, I can understand that, because, yeah, then you get into this, capability negotiation territory, or, yeah, some solution needs to be in place, so I can see why. But, that also means that OBI will have to… Go on without that for… for the time being.
Cool. Yeah, thanks for bringing that up, Nev. That's definitely interesting, and we should all keep an eye on it.
Any… any more thoughts on this?
No?
Then… I guess that concludes our…
**dalehamel** 39:48 Good, sorry, Dale here from Shopify.
**Felix Geisendörfer (Datadog)** 39:51 Oh yeah, go ahead.
**dalehamel** 39:51 Right before the end here, just an update on the last meeting, PR number 907 there.
So, I've decided to go ahead with basing it on, Timo's PR for variable frame length.
As that allows us to fix the… the line numbers. So that's… I believe… Correct me if I'm wrong here, 946 is his PR, I think?
But it looks like it's, it's been reviewed at least once by Florian here. But, I think, if that lands, I've already rebased my PR on it and included the fix, so I can basically just push a… push a fix to… or update my branch once that lands, and then I think it should be a bit easier to review at that point.
**Florian Lehner** 40:43 Yeah, I think that's the right way forward. We are, at the moment, a little bit short-stuffed, and Sick days and all this kind of stuff, so, yeah, yeah, we will take care of this, and the direction, I think, is super fine.
**dalehamel** 40:59 Awesome, yeah. It'll be easier to, yeah, grok it all at once, rather than thinking, okay, we have to fix the line numbers, we need this other thing, so having it all in one place would be good.
And also, just quickly, I think, was it Evo was talking about context, propagation?
I've actually been looking at that for Ruby as well, but obviously that will build on this work that hasn't even landed yet. But we're doing some… we're discussing with some Ruby developers here at Shopify how we might be able to make that work. So, just a heads up, that might be something that comes down the pipe in 2026 or so.
**Frederic Branczyk** 41:34 When you, when you do, so we already solved this for V8 as well, and we're just about to start for Python as well, so it might be, possible that there's a decent amount of overlap,
**dalehamel** 41:48 Yeah, I've seen… I've been reading a little bit of the literature on this, and I think, you know, thread local storage tends to be a great way to go for this. Unfortunately, Ruby, has to be the black sheep and has its own concept of fibers, Which is, like, on top of OS threads, so we can't just store it on the OS thread, we have to store it in, like, an internal Ruby thing, unfortunately.
**Frederic Branczyk** 42:09 Yeah, that's… vaguely…
**dalehamel** 42:12 I think on the processing side, though, that's probably the case, that we can share some of the plumbing there, but actually getting it out of the Ruby process in a consistent way is what I'm the most concerned with.
And trying to make that efficient as well.
And the moment we open this up, we have developers wanting to jam everything under the sun in there, so we gotta figure out, like, reasonable restrictions as well, so…
**Frederic Branczyk** 42:36 Yeah, yeah.
But we both had to solve… we had to solve the same, like, similar kinds of constraints within V8 as well, so…
**dalehamel** 42:46 So definitely we'll keep an eye out there. I've actually made the decision to subscribe to the whole fire hose for this repo, so I'm sure I'll see the PRs pop up.
**Felix Geisendörfer (Datadog)** 43:02 Cool.
**dalehamel** 43:06 Yeah, we can talk about that offline, Ivo. Some interesting thoughts.
**Frederic Branczyk** 43:10 Yeah, we've tried some of this with Rust. I think, Ivo, you were already talking to Brennan, right?
**Ivo Anjo** 43:17 Yes, but not a lot, did not go very far.
**Frederic Branczyk** 43:23 reach out to him. This is, like, what he's been working on for almost the last year or so.
He has thoughts and experience.
**dalehamel** 43:35 Yeah, we're gonna try and just prototype something with, like, a gem and a native extension, and see about getting it upstreamed into Ruby itself to make it more first-class, but we'll probably just get something going on our little fork here, and proof of concept it, and see what we can do.
**Frederic Branczyk** 43:50 Yeah, that sounds good. For what it's worth, with V8, it took us, like, I think, like, 3 or 4 iterations until, like.
**dalehamel** 43:57 Yep.
**Frederic Branczyk** 43:58 Major architectural changes before we actually managed to get something that, you know, wasn't cost prohibitive.
**dalehamel** 44:06 Yeah, of course.
Got lots of work out there we can take inspiration from, I hope.
Cool.
**Felix Geisendörfer (Datadog)** 44:17 Yeah, thanks… yeah, thanks for all your work on Ruby contributions. Thank you, Dale.
Okay, that would be the end of our agenda, unless we have another last-minute surprise.
Going once, going twice… Okay, then three times is a charm. Thank you, everybody, for attending, and for all the work done between the meetings, and see you all in two weeks.
**Ivo Anjo** 44:46 Thanks, everyone.
**Frederic Branczyk** 44:47 Thanks, everyone. See ya.
