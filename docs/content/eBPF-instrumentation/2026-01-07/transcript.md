SIG: eBPF instrumentation
Date: 2026-01-07
Duration: 64 minutes
============================================================

## Zoom Recording Transcript

Stephen Lang 00:00:25 Right.
Florian Lehner 00:00:26 Hey, Happy New Year.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:00:31 Happy New Year.
Giuseppe Ognibene | Coralogix 00:01:06 Hi, everyone.
Nimrod Avni 00:01:08 Hello.
Tyler 00:01:16 Hey.
Nimrod Avni 00:01:19 Yo.
Tyler 00:01:20 How y'all doing?
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:01:21 year, everyone?
Tyler 00:01:22 Happy New Year.
Nimrod Avni 00:01:24 Happy New Year.
Tyler 00:01:47 Looks like we can probably get started here in just a second. Still getting set up. If you haven't yet, please go ahead and add your name to the attendees list, and if you have agenda items you wanted to talk about, please go ahead and add them there as well, and then we can jump in here in just a second.
Hmm… I'm trying to share my screen, it looks like it's all going black. I'm guessing all you're seeing is black, right?
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:03:12 Yeah, do you want…
Marc 00:03:13 Me to share?
Tyler 00:03:15 Yeah, maybe that's… it's best.
One sec.
Actually…
We can try one more thing, Nicola, let me see if I can… .
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:03:35 Yeah, it works.
Tyler 00:03:35 Yeah, okay, alright.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:03:37 We're… alright.
Tyler 00:03:39 Cool, alright. Okay, cool.
Welcome, everyone. Yeah, jumping right in then, we can, start going through the agenda. So first off, starting off, Nimrod, do you want to talk about network monitoring?
Nimrod Avni 00:03:54 Yep. So… Yeah, we've been looking for just, like, adding a couple, like, network monitoring stuff, like…
stuff that we already kind of have in… in… to the work of Nikola, stuff like DMS and TCP data, connections, round trip time, a bunch of stuff like that.
And…
I'm looking at the OpenTelemetry Network project and seeing that it has a lot of the stuff that we wanted, but I don't know if it's, like, what… I saw also Mario talking to them a bit about
Setting, semantic conventions for, network monitoring data.
So I just wanted to ask, what do we think regarding… is this project something that is…
like, should be deployed regardless of OB? Is there some future where we kind of unite them? And if we unite them, then…
is the… the… how do we want to do it? Do we just want to, like, start copying?
the, the, like, the kernel code, we can somehow embed this into Obi? I'm not…
Super familiar with this project.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:05:14 I have some background info, unless somebody else wants to go. This was part of the discussions before we made a donation.
So the… the plan is that we would, pretty much implement what they have. So, in… in OB, and then…
they would use OB as the eBPF side, and then keep the user space.
Because they have some… interesting kind of flow-related stuff, especially without Kubernetes, that works really well.
But there's no plans for them to upgrade to a more modern eBPS side and rewrite the code, because right now the approach is you need to bring in LLVM and
Clang on every host that you install, because it's not using… BTF.
Or, this… they'll once deploy everywhere eBPF with LibBPF model.
So, it's really difficult to port for every kernel version, which is why the project hasn't…
And I think there's some issues with maintainers, maybe, and how much effort's been put in to maintain the user spaces written in C++,
There was some talk of converting into Rust.
Things like that. So, when we talked, it was like, as long as we provide the same underline…
data, they were happy to.
Use OB as a backend.
Nimrod Avni 00:06:40 Great.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:06:41 By all means, if you'd like. Now, the network spec…
I don't know what the status of that is, but…
We can just do what they do, imported.
Nimrod Avni 00:06:53 Yeah, so I thought we can start off with, I guess, already the metrics and stuff that they expose is not something that's, like, any, like, semantic conventions. We can start with that, maybe asynchronously, try to set it as, like, official.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:07:08 Yeah. And…
Nimrod Avni 00:07:10 Yeah, and then, like, regarding, because I know Obi already has some, like, network monitoring stuff with, like.
like, network and, like, bytes between regions and stuff like that? Should be… should that be part of, like, the same…
Preset? Should we add it, like, as a different preset?
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:07:29 I think so. I think network folks want to get everything. I think we… we initially started with just flows, but it's been a lot of…
folks that I've heard that wanted, for example, this retransmit errors, and retransmits, and things like that.
Disconnect, resets… That kind of stuff is important to people.
Nimrod Avni 00:07:52 Buckeye's place.
Cool, so I think we can… we'll probably start working on it soon.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:08:01 Yeah, the DNS… I think there's a spec for DNS, but OB follows that, so I don'.
Nimrod Avni 00:08:06 Yeah.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:08:07 their DNS events maybe not be within the OTEL spec, but…
Nimrod Avni 00:08:11 Yeah, I think for DNS, we follow what the semantic convention has, and it's just for, like, TCP stuff.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:08:18 Yeah.
Nimrod Avni 00:08:22 Cool, thanks for that.
Tyler 00:08:23 The semantic convention stuff, I would definitely make sure that, like, we try to follow those as much as possible.
So if there is overlap with what already exists in the semantic conventions, and, like, say the network, the network instrumentation doesn't actually…
follow that, we should switch to following that. Like, we should try to follow wherever the semantic conventions allow,
I think that if we have additional things, that we can… we can look at adding those as well. I don't…
Anticipate there being a large appetite for this networking, semantic conventions to add a lot of this stuff.
But we can try that as well. There… it's pretty…
it's a hard process to get, I think, a lot of that stuff in.
It may be an opt-in thing that we could try to get in the semantic conventions, at least. The problem is that, like, every new metric is very expensive, and so having a lot of new metrics is going to be challenging to promote as, like, the de facto standard.
But I think that if you have, like, opt-in metrics, I think that there's a little bit more of a wiggle room there.
Nimrod Avni 00:09:29 Yes, I think Florian just sent something, and I also said maybe the same.
I saw some, like… Network metrics… I don't know if those are the exact same…
For things that we want to do, stuff like,
TCP, round trip time, and retransmit, and stuff like that. I don't know if that's…
Specked, but there are stuff like…
Connection count, and network errors, and stuff like that.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:10:02 Yeah.
Nimrod Avni 00:10:03 account.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:10:03 Yeah, I think you should follow the ones you sub… you actually…
Network count, network I.O, network errors, packet.
Nimrod Avni 00:10:15 And maybe for the ones that we don't have, we just, like, try to follow, like, network.
retransmit, or something, I don't know.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:10:24 Yeah, exactly.
Tyler 00:10:27 Yeah, I…
So, I think the retransmit one, like, I would definitely try to get a list of things that, like, aren't overlapping here. Like, I would definitely try to do whatever we can do to follow what is happening here. And then the ones that we don't have, I think we want to document that. Like, I think that you can also…
the way I would recommend doing it is to write our own spec for it, which is kind of like…
not… sorry, not, like, spec, but, like, semantic convention, YAML format, so, like, you can define these metrics in the same way that I think
I don't know if this is exactly it, I think it's changed a little bit, but, like, in a very similar way here, because the reason then is because if somebody wants to…
start modifying these sort of things. Like, you can use a lot of the tooling, like Weaver, to, interact with what we're actually going to produce. So if we do go beyond it, I think we'd want to do something like that.
And then maybe even opening an issue and asking, like, if this is something that would be accepted as, like, an opt-in or something like that.
But yeah, sorry.
Stephen Lang 00:11:37 If, if there's a mix of using the upstream conventions and our own
Would our own attributes and metrics, they have to be…
prefixed with OB or something to kind of differentiate the fact that, not all of these things are covered by the convention.
Otherwise.
Tyler 00:11:56 Yeah, that is true.
Stephen Lang 00:11:57 chance for, like, future conflict, if they do make it in some slightly different form interview.
Conventions later on.
Nimrod Avni 00:12:07 Makes sense.
Tyler 00:12:08 Yeah, like, like, I'm just looking at, like, this kind of stuff, like, this is…
This is definitely not following the conventions, so this is something we would want to, like, switch to
you know, Whatever we can do to, like, make network throughput
Follow the network throughput semantic conventions from here.
I don't know if they have annotations with, like, the protocol, but, that might be something we may want to look at as well.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:12:32 That's what protocol name, yeah.
Tyler 00:12:34 Yeah, here we go.
Nimrod Avni 00:12:35 Yeah, I think that's more for, like, it looks like a higher level…
Not like, you have network transport, like TCP, UDP.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:12:44 I think the second link that you posted, Nimrod, I think it's… the network metrics is maybe good to see.
I think that one… that one is the actual metric collection name, and then we can use these attributes in there.
Nimrod Avni 00:12:57 Yeah.
Tyler 00:13:01 Yeah, so this would be the… this is the metric name, yeah.
And then the attributes are down here, where the network interface and the I.O. direction.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:13:10 Yeah, so packets dropped, that's really useful for people. I don't think there's retransmits in here, but we can add it in a similar way.
Nimrod Avni 00:13:19 I think ideally, we also want to add, like,
all the other stuff OB adds, like, like, Kubernetes metadata, and service name, and a bunch of… maybe a bit, that's, like, resource attributes, I guess that's…
Yeah, exactly.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:13:34 It's already in there.
They're part of the… the Kubernetes metadata attributes, so… should be fine.
Tyler 00:13:43 So I do think that we want to think about our… Customization of this?
In some way, because, like, a large amount of thought has gone into, like, the attributes that are recommended or required here.
Because the more attributes you add, the more carnality you add, and potentially an unbounded amount of carnality. So we definitely want to be very careful about that. And we also want to try to make sure that
You know, we have… if somebody doesn't want…
a particular attribute, and it's not a part of the semantic conventions, but, like, we already had it, like, we should have a way for them to turn it on or off, and I think that that's… that's…
pretty standard, I think, in a lot of instrumentation libraries, and so we just want to make sure we handle that.
Appropriately.
I think we have a way to turn off metrics, right? But we don't have a way to turn off individual metrics right now.
Nimrod Avni 00:14:42 I think we have some, like, presets of stuff with, like, the features that you can do, like.
Spend metrics, service graphs, all that stuff.
And I think Network Metrics is one of them.
Tyler 00:14:54 Okay.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:14:54 There's the attributes section, which I think… I wish Mario was here, but it might be possible with the attributes to say…
Exclude, include.
Things like that, but I don't know exactly.
Tyler 00:15:06 Okay.
Florian Lehner 00:15:08 Sorry for the question, but wouldn't this replicate existing behavior of other OTE components that can already strip
add or remove, attributes from certain information, logs, traces, and metrics, and profiles. So, why should it be also in OB?
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:15:32 Yeah, the only.
Tyler 00:15:32 If users don't use these other components?
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:15:35 Yeah, like, sometimes people push straight into OTLP endpoints in the cloud, and they don't have access to that collector config.
Tyler 00:15:46 Yeah, and I mean, I think that,
I think it's fine, we wouldn't need this customization if we weren't doing things outside of the semantic conventions, but even in the semantic conventions, you have things like opt-in attributes.
And I think you want to have that at the… the source. I think you want to not be sending things over the network that you don't actually need.
Is kind of the idea. And if we're going to be adding additional attributes that we already have, then I think we want to be careful about
How users have control over that or not.
Florian Lehner 00:16:21 Just going forward, if Obi becomes a part of OT Connector, and…
If it's part of an OTA collector, then, the distribution can configure
Processors that modify logs, traces and order signals.
and, remove at all these attributes, and that's why I'm a little bit confused. Yeah, I see the point that at the moment, OB is only deployed using Helm, and for this use case, it's essential, I would say. There's no other way. But, for the integration with OTEL, I would
see more…
getting this kind of stuff more removed from OB as a functionality, or only a functionality if deployed via Helm, and having the…
core functionality of OBE, just really like, hey, here you have all the data.
Do your own processing as you like, as you configure it.
Tyler 00:17:23 Yeah, and I think that sounds reasonable, but I think that that's a discussion for when it gets integrated with the collector. Like you said, like, I don't ever see, like, it getting deployed as its own standalone going away.
And if you wanted to wrap it in the collector and say, not accept the full configuration, because you can just, you know, work with it differently there, like, that's something I think we can tackle when that happens.
Okay. So, jumping back in to the agenda, Imrat, I think we have a pretty good understanding of this. It sounds like you're gonna take a look at this.
Okay. Yeah.
Nimrod Avni 00:18:01 Cool thanks.
Tyler 00:18:03 Cool. Bam.
So next up, Mattia, you want to talk about,
Trace contact… trace contact mapping and eBPF. I'm guessing this is so you can do trace contacts… yeah.
Hmm, sharing?
Like, you said…
Mattia Meleleo 00:18:25 Yeah, to expand on this, so basically the idea is that at any given point in time.
regardless of the target application, like, if it's Go or Python with a SyncIO or whatever.
There is one single trace context for, for a single PID,
So I was wondering if, if a single map which exposes this information would make sense?
And,
Yeah, the two use cases, the two bigger use cases for this will be trace log correlation, because right now, I can only access a map.
which doesn't include, like, Golang information, or Python with async.io, or Ruby, or whatever.
And eventually, in the future, the trace to profile correlation
I'm not sure about the profiler, but, having a single map
from which you can access it via PID and get a trace context would be super useful, I think, in that case.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:19:33 there? Yeah. Yeah.
Tyler 00:19:36 Oh, yeah.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:19:37 Good, this is really good. Yeah, I like this idea, and it's been on the to-do list for such a long time, especially the trace profile correlation. I wanted to add a couple of comments there, so,
I think this was something that Nimrod brought recently, which I haven't thought of.
The… especially for Go, that you can actually make a map from Go routine to thread, so you know which thread is currently associated to each Go routine.
And that solves… more than just this trace correlation mapping, but we could potentially use the K probes
For the protocol, rather than instrumenting each individual goal library.
So, that's a big boost.
One kind of thing that we have to find out there would be, whether that puts too much overhead, because we're gonna have to instrument the…
the Go, Go routine when it actually gets added on the thread, when it gets mapped to a physical thread, or not physical, but…
to, OS thread.
So we could… We can do that.
And for the trace profile correlation, I think we can expose this eBPF map and mount it on the BPF file system.
We used to have a lot of code for this, it's in the Bela repo somewhere in history, it's removed now, but…
We used to map a lot of maps as…
For this purpose, so we can…
Steal that code back in, and…
bring it in for this purpose. So then, any external tool could potentially… Read that map.
it, and… Use it.
Mattia Meleleo 00:21:19 Okay.
Florian Lehner 00:21:21 From a profiling perspective, I think that from Steven already shared a link to the hotel specification.
Where there is a discussion sharing such exact,
Information, but in a different way, not, Ebpf maps.
From a profiling perspective, I'd like
we would like to see more, general hotel approach than custom implementation. That's why, Datadog decided to go the official round, have a proper specification and implementation.
And, yeah, having multiple
having multiple solutions for the same problem seems like… like, more like a burden, so that's why maybe you can,
Read through the specification, give your feedback.
This would be nice, and so, maybe… Other components are using this.
I talked with Evo, and there is also feedback already from the ChavaSig.
And, so… Yeah, it would be super interesting to have something that is more specific, rather than…
Rather than eBPF maps. There was a discussion around eBPF maps in the past.
But especially instrumentations don't have the…
required capabilities to use them. So, if you think of Go or Python, They're usually not,
deployed using Capsys Admin or BPF.
And that's why, the different approach as written in the specification is, is proposed at the very moment.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:23:10 Right, so… but I think… I know I've read this proposal, it's really good. It's sort of a way from a user space to push on information that can be read by the profiler at eBPF time, right?
But Obi will have the problem, using that approach, because…
We have no way of writing that memory.
Like, we would like to be able to, but then,
without using something like BPF ProBride user, which is banned, then… We're… we're stuck.
So we cannot write that memory in a format that will be consumed.
Florian Lehner 00:23:48 Maybe that's proper feedback that would be benefit for the specification.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:23:54 Okay.
Tyler 00:23:54 But I also want to point out that, like, this is for resource attributes, though.
which are… are very different, because I think this is something that's specific to, like, something static that's not going to change ever, if at all, and I think that what we're trying to accomplish here, and, like, what Nicola's getting to, is that, like, this is something that, like, the context propagation is very different, it's changing all the time.
Florian Lehner 00:24:17 I see the point, but the specification is flexible in the way that we could something… we could specify,
something like, hey, if you're looking for a trace ID, look at this place. Like, look at this memory address, or if you're looking for something that is related to something else, look at this place. So, at the moment, it's really, like, focused on resource attributes, which, you are correct, change hardly.
But for trace ID, the idea is to…
To have something like, hey, if you're looking for this information, look at this place.
So, would.
Mattia Meleleo 00:24:54 One question. Does this protocol allow for writing and reading from eBPS.
Because if it gets out to user space, it's very racy in this case.
Florian Lehner 00:25:11 At the moment, I would say no, but…
going a step further, I would say.
One option would be to say, hey, if you're looking for
trace ID information like you're proposing, then the…
process context could be, hey, there's an eBPF map called 12345 trace IDs. If you look for them, just look this eBPF map up. So, we need to share the information in some way, and I think that's, the process context should be the right way. If
if this will happen with eBPF wives in the later stage, maybe, I don't know, that's up to discussion, but, I think that's a valuable way forward.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:26:00 Okay, so your proposal is that we actually follow up on this particular OTEP and say we would like to add an eBPF way as well?
And discuss… make a proposal of what that would look like.
The map?
Florian Lehner 00:26:14 Could something like this, yeah, yeah.
or maybe, just extend the specification and say, hey, something could, publish an eBPF map for a particular process or, resource, and say, this kind of information you will find in this eBPF map.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:26:34 Yeah, okay.
Okay.
Tyler 00:26:36 Yes, sir.
I'm a little worried about, like, boiling the ocean on this one, but I do think that, like, we're hitting on an important thing, so I think that, like, there's a, like, good conversation here. The fact that this is, like, prescribing that it goes to analytics, anonymous memory mappings, I think is…
The problem that's gonna, like.
maybe not apply here. I do think the standardized format, though, is kind of the more important thing for a lot of this stuff.
Right? Because, like, that, like, the canonical format that we're actually going to expect it, whether it's in some sort of Linux memory mapping, or whether it's in some eVPF map, I think is going to be more the thing that is… is useful, coming out of this, right?
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:27:19 So you're saying that if we define the format, then…
We should probably make that anonymous memory mapping
Or eBPF map, or another means.
Tyler 00:27:31 Yeah, or some… yeah, similar to, like, what we do with context propagation now, right? Like, where we have
essentially, like, a carrier, and we have a propagator concept, right, where we split the two, where you can say, like.
Here's the format that you're gonna expect it in, and right now we have, like, you know, currently a trace base.
format, right? But, like, or a text-based format, but, like.
we call some sort of, like, format for this for encoding of this information, and then we say, like, this could… this could be shared via Linux, anonymous memory mapping, it could be an eBPF map, it could be, like you're saying, also, Nicole, like, some other…
Some other mechanism as well, right?
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:28:06 Right.
Tyler 00:28:08 I think decoupling these two things would be really helpful in this situation.
Because, I mean, I think that's, like, my next question immediately, is, like.
say we get them to switch to, like, an eBPF map, like, what's the format that context propagation comes in? Because, like, us putting it there, or the profiler putting it there, doesn't really help if the other person doesn't know what format it's in, right? And they try to look for it, or they try to retrieve it in a different way.
Florian Lehner 00:28:34 You're right, that's why we are pushing for a standard format. Right.
Tyler 00:28:38 Yeah.
Nimrod Avni 00:28:39 I think for trace log correlation, at least now, like, because we're doing it inside OB, it doesn't really matter, and we can, like, do something internally. But then, like, once we want to integrate with, like, the profiler, or even, you know.
other, I don't know, other components, like, I don't know, the receiver will actually, like, enrich the logs or whatever, or, like, the hotel collector, I don't know, then we might need to have a standard format.
Tyler 00:29:12 I think that, like…
Yeah, I agree. The other thing that I had a question about is, like,
So this looks like it's trying to map a PID to a trace context mapping, which kind of, like, goes back to this idea that there's, like, A active context per process, but is that always true?
Stephen Lang 00:29:30 There is a note about that in the OTEP. It talks about both process and thread level.
Context. If you have to look at the actual, PR.
Into the, belt, and… It's a bit easier if you do the view
Whatever it is, so you can actually see it rendered.
Tyler 00:29:53 Oh, I see, Jane, yeah.
Stephen Lang 00:29:55 If you, yeah, if you search through for, process.
Or something like that.
It does actually talk about, Process versus threads.
A little later on.
Nimrod Avni 00:30:07 Yeah, maybe we need…
Stephen Lang 00:30:09 Yeah, that's a trace correlation.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:30:17 Yeah, thread-level context sharing.
That's exactly what we want. It's just, for us, the writing onto the anonymous memory of the thread
Would not be possible unless we use the…
the PPL, what we don't want to write.
Florian Lehner 00:30:35 Yeah, fret level will be next up. We just need some base ground.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:30:42 I see, so… Common in here, say, would like to extend this beyond…
Tyler 00:30:51 Yeah, this is specifically for the… the… Profiler, right?
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:30:56 Yeah.
But there's no way for us to share this with a profiler other than through the…
to this trade-level information. I think, I mean, correct me if I'm wrong, Florian, but, I think Elastic has a prototype of something like this for Java, correct?
Florian Lehner 00:31:14 Datador, actually, just for Datador.
But I think… I think you're initially…
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:31:19 donated a profiler, it did support, trace to profile correlation for Java.
Florian Lehner 00:31:24 Yeah.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:31:26 filer does support it.
Florian Lehner 00:31:27 Yeah, that's really, like, something we want to get rid of.
There's an experimental environment where this works, but, outside of this environment, it does not.
And so, yeah, would not recommend using it.
Datadoc… Has the Java example? No, it's…
it's the C and C++ example. But, yeah, in the SIG profiling repository, we have the…
We have, all these experimental code that, goes building these
building these, specifications, so that we can also go to other SDKs, like, Java SDK, which is really important for us. And, yeah, if it's not accepted by Java SDK, then…
We will not go further with it, because, as, Chavaisar.
Unfortunately, widely deployed and used.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:32:28 Yeah, yeah, absolutely, yeah.
Okay, so if this is defined, then…
We just need to ask for possibility for this to be supplied via eBPF map for tools that do support eBPF, right?
it's almost like, unfortunately, either or, right? If you're in user space, you can probably write in the thread anonymous mapping storage, but if you're…
Kernel space, and that writing is not possible.
Or it's possible, but then it will not work on it.
Integrity kernels.
Florian Lehner 00:33:07 Yeah, there are some challenges we have to, we are facing, but…
Oh, I think we record that, or we will… Get to them.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:33:19 Yeah, cool.
We could maybe prototype using the BPF ProWrite user, but… I will have… Limited use.
Tyler 00:33:34 Well, I mean, I… yeah, I think that that's very limited. I think the prototype is more about, like.
So, Florian, if, like, tomorrow we had an eBPF map that had this information, how would we prototype this in the, the profiler?
Florian Lehner 00:33:48 We would share the information to the profiler.
to the EBPath space, that this map exists, and then… just extend the trace with attributes, I would say.
Should be… Barely… straightforward, I would say.
Tyler 00:34:13 Okay.
Florian Lehner 00:34:14 But no guarantee.
Tyler 00:34:15 Right, yeah, that's what the prototype's there for, right? But yeah, I mean, like, in theory, right, like, it should… yeah, okay.
Okay.
Mattia Meleleo 00:34:24 I think it's not that we have a low correlation.
We can start by implementing this map and adding the support in all the places where we…
Where we have the async or goroutine correlation.
And start testing it out, and when we know it works.
Well, we can, we can share it with the profiler by pinning it.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:34:52 Yeah, no.
Tyler 00:34:53 Yeah, I think… I think that works. I think we also want to, like, once we have that working…
prototype that you're talking about, Mattia, is also just, like, ensure that we're including that in the discussion with this OTEP.
And, any other discussion around standardizing a format? Because, like, the format that we're trying to share is, like, the thing that we want to be involved in that conversation, right?
So, yeah, I think, I think if you could jump into that,
OTEP, and just maybe leaving a comment to the fact that, like, well, in eBPF, we need to be able to share this in a map, so, like, we can't do, like, the anonymous memory mapping. But then also, like, talking about the, trace context
being the thing that we want to share, and so, like, I guess just making sure that it's understood that, like, the resource attributes are really important, but, like, we also want to, like.
Think about other data protocols and the standardization of the format.
Mattia Meleleo 00:35:46 Nope.
Tyler 00:35:50 Okay, cool.
Looking at time, we can… I think we can jump on here. Keep us informed, Mattia. Interested… very interested in this one. I think this is, like, really critical for universality of these… these technologies, so yeah.
Nimrod, you wanted to also talk about Obi as an OTEL receiver?
Nimrod Avni 00:36:09 Yeah, we talked about it a bit earlier. I'll try to be short. I…
drafted some PR, and it seems to kind of work. And there was a comment below, I think someone from Rafana, I forgot his name.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:36:24 That's fabulous.
Nimrod Avni 00:36:24 Yeah, regarding a job Rafael did on doing it on Belo. And, like, the way I did it is a very similar way to the way that the profiler did it, which is basically
Can I, you know, basically using the same part of the code that, like, runs, like, instrumenter.run, and just taking the config from the receiver and then running it as, like, running the instrumenter in the same process?
And then, obviously, he mentioned here that it might have some, like, dependency issues of, like.
You know, sharing dependencies between multiple components of the collector can, like.
be… can suck. And I just wanted to, like, consult with you guys. Maybe Rafael will have a more concrete opinion on that.
Because besides that, it works.
Besides also the…
Kubernetes cache component, which I thought maybe we could do as, like, an OTEL extension, but then I consulted internally and
Like, the main reason I wanted, like… like, there's a lot of reasons it's really good, but one of them is, like, having it be managed by the collector. We can manage it with, like, the, OPAMP, OP APM, like, the Agent Management Protocol.
And then I thought the Kubernetes cache can also be there, but I don't think it makes sense, because it's not, like, a data collection agent.
So maybe it should still be managed as, like, a different deployment.
So, I don't know, like, I can… I have, like, a bit of, like, a few changes I want to do here, but just, like, as you're…
If anyone has, like, opinions on that.
Of if it should be run as, like, a binary, or, just embedded as the same, like…
Like, basically using it as a dependency.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:38:24 Yeah, I know… I know a little bit more background here. Rafael is not here for another two weeks,
But I can give you the background on this, we…
So Rafael has a prototype that…
Changes the way we embed,
data into Alloy, which is the ultra collector.
Or a version of something that is future gonna be much similar to the Auto Collector.
But… There's a couple of unanswered,
questions there that I think we need to answer before we see if this approach is viable. Essentially, what he does is he launches the executable standalone, and he's written code says that it cleans up correctly, and it can be reloaded the same way, can be multiple of them running.
There should be no problem.
The only downside is that all communication happens through network, rather than being in memory.
And, essentially, the one main…
To me, sticking point is that it's the, the metrics are fine.
They're not that much data, but the traces do…
need to be serialized by OB, and then deserialized by the collector.
In this format.
That was the…
Nimrod Avni 00:39:52 Yeah, that's what… Like, you kind of need to deserialize it, then pass it to the next, like, consumer.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:39:59 consumer, right? And so it's not like you can just pass in the traces receiver straight up from the collector into OB, and then… which is what we used to… we do right now. So then you're directly writing the traces.
Into whatever the collector supports, because we're both using the P data format.
This…
Nimrod Avni 00:40:19 So… I think I wrote it down there.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:40:22 Yeah, so I wanted… he's got a design document, about doing this, and I think we need back… he's back, we can…
talk about this, but essentially, I want to see what that overhead is like, because Collector, as a component, is very sensitive to increasing memory usage and CPU usage for end users.
So, if this causes significant memory overhead, because of the Go Garbage collector having to go serialize, deserialize something that was done as a one thing.
This will be a no-go.
Because, I mean, a lot of customers are sensitive of how much memory they can throw at the collector, and…
Scaling it and so on.
So I would say keep on working on this, because…
I mean, unless we know the answer to the question, and nothing stops us from changing in the future, right?
I mean…
Nimrod Avni 00:41:20 Yeah, we can change the underlying, like, implementation.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:41:24 Yeah, I mean, if that shows to be superior and there's no issues, then…
then that's fine, we can switch to that. But that's still an open question to… To what that means.
We've experienced issues, I won't lie, on keeping up to date with the changes to the specs and so on, and
Many different components.
But… Actually, I don't know if that's…
More of an alloy issue, or auto collector issue?
Nimrod Avni 00:41:55 I'm wondering with Florian, maybe, because they're doing it with the profiler, maybe he has a…
Marc 00:42:01 Yeah.
Nimrod Avni 00:42:02 of insights.
Florian Lehner 00:42:04 Yeah, so the OTL eBBF Profiler is currently already
able to run as a receiver in the auto collector.
And, for us, that's why I did mention earlier that, we don't…
we removed all this code about Kubernetes cache and metadata from the UPF profiler, because we say, hey, let the user configure whatever he wants and, remove or edit, respectively, with the components. We never did run into,
into issues with dependency, unless they were related to the breaking changes in the OTA profiling protocol. But this is self-made, I would say. So, I cannot blame OTA Collector or OTA Collector Contrape on this.
The profiling signal had a…
Some significant breaking changes over the last…
year, I would say, and there are some upcoming ones, but this is related to profiles, and we'll not
be part of traces or locks, or metrics, I would say. Traces, logs, or metrics protocols are really stable.
Yeah, I really like the approach of,
of how Nimrod, implemented it.
But, I would also see that
I would love to see that all these external components, like Kubernetes, are removed, but I also see the point that there is a need for being able to deploy this Helm chart, and for this case, you need it.
Nimrod Avni 00:43:48 I think even the issue is that we need the Kubernetes cache even without
like, regardless, because the profiler, basically, you enrich only processes that run on the node that you're collecting data from, and with Obi, let's say you're doing a network call to another pod, you still… you want, like, the…
the name, like, you have the IP, and you want the name of the file running on a different node, so you need, like, the whole Kubernetes state inside your cache, and not only the local one. And you can't run, like, the local one will get the whole… the whole deployment, because that will crash Kubernetes.
Florian Lehner 00:44:26 Yeah, I see that point, but we say, hey, that's part of the…
of the correlation in the backend. So, we just…
we just… what we are doing from the profiling perspective is that we extract just the container ID, and let other auto collector components say, hey, based on this container ID, we can tell you its Kubernetes namespace, whatever is important for the user.
And, yeah, yeah, I see that point. I see that point. It's definitely a challenge, and…
Nimrod Avni 00:45:06 Maybe the Kubernetes… maybe we can… I don't know, that's, like, a more general collector thing, like, have some…
like, either extension or something that, like, basically only multiple collectors get the Kubernetes state and share it with all, like, the fleet. Basically, like, what the Kubernetes cache does, but in, like, an hotel way. I don't know if that's, like, way out of the scope, but…
Maybe that's something…
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:45:30 Small steps, right? You can start with this, and then we can…
Florian Lehner 00:45:34 Yeah.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:45:35 Slow word, too.
to a more similar approach to what Profile does.
Florian Lehner 00:45:40 Nope.
with the current approach, I only see the complexity for the end user that they can, and maybe mix configurations. So, let's say, configure Kubernetes for the OB part, and then have a…
Kubernetes attribute processor as part of the hotel pipeline that does something different, or it conflicts, so that's something that might be come up.
I mean, it's not that…
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:46:09 But it's… maybe it can solve with documentation.
Yeah, it's not that bad. If we set up the resource attributes based on the Kubernetes that we've collected, and the auto user writing them, that should win.
the collector will change those. And I think we have examples of that already. Like, people do that. You push your data from OB to a collector, and somebody wrote a bunch of rules there, they'll override what we do, and that's totally fine.
They can change the attributes, use different metadata, Add attributes.
For us, the primary thing has been able to resolve a name of a downstream service. That's why we need the cache, nothing else. Like, the resource attributes, we could live without them.
Pretty much.
If the collector is there.
We don't even need to set them.
Tyler 00:46:56 Yeah, actually, I think it's better if you have the collector, because that could have more context for resource attributes anyways that we'd want to add.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:47:02 Exactly. But it's just the resolving on the names.
Of downstream stuff.
Tyler 00:47:11 Which I think, to Nimbrod's point, like, that may become something that we could have more universal. Like, you can ask… because I think that's also another thing, is, like, if you're running in Kubernetes, that works, but, like, maybe there's some way you could have the collector provide a generic way to say, like, any environment, if it has an understanding of the downstream
like, I don't know, naming structure, then you can get that from it, and so maybe we could hook in that way then. But to start with, I think just using what we have, I think, seems reasonable.
Going back to the question about the binary embedding or not, I'm very hesitant to say that we should be embedding the binary here.
That seems,
I'd like to hear, I think, more of the dependency issues that were… they were… that were being run into. I don't know if that's a specific alloy thing, or if it's a,
What's that?
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:47:56 It could be, it could be, like, I, there's two main reasons why we preferred we explore…
Shipping this as a st… like, a binary, rather than as a…
as a dependency directly into the code. One is the dependency issues we've encountered every time we have to upgrade
dependencies, But I think that will be less of a problem if it's done the way with the…
Auto…
profiler, because it's… everybody's on the same version of the OTEL spec, and all the exporter libraries, everything's exactly the same.
Marc 00:48:34 Yeah.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:48:34 So, I think that should work. I think with AWA, it's not always the case.
Marc 00:48:39 Yeah, I think the main… I mean, the main problem were more with the…
Celium eBPF libraries and transitive dependencies, because we were also embedding.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:48:49 Biroscope.
Marc 00:48:50 And also because alloy has… is huge, and… Every time that…
You have to upgrade hotel, you have to touch a lot of parts.
And in our case, at least in Nobi, when we have to update.
the dependencies of Autel, we just need to change that.
Batcher that is experimental, and it changes in every version.
But, for example, the SDKs, or the tracing…
Stuff, I don't remember that had to change much, so…
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:49:22 No, so yeah.
Nimrod Avni 00:49:22 now I remember that I had to upgrade, like, when I built the collector, I had to upgrade some, like, auto collector dependencies from 140 to 142, and it's, like, a minor change in the config.
It's not, like, a very breaking change, it's, like, some, you know, it's some incremental stuff, I guess, that we can make sure we're kind of updated with the last,
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:49:47 Not collector.
And it's not a bad thing, right? We're updating to the latest collector SDK non-stop, so… which is… has its own benefits.
Tyler 00:49:58 Yeah, I mean, I get, like, the dependency update, especially if you have dependencies that have breaking API changes in non-major versions, which is, like, this happens. It's not common, and in the silly me world, I don't think that that's going to happen.
But, you know…
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:50:11 instance. So, yeah, we mentioned that one, but it's happened only once, right? So there was something with some underlying library that Silium used that changed behavior, we couldn't use it, or something, I don't know.
Tyler 00:50:23 We've worked around it by, I think.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:50:26 Raphael provided a patch to the psyllium BPF or something in it.
He moved.
forward.
Tyler 00:50:31 And I think in the collector contribib, you have a lot more control over that, upgrade, especially if you're not trying to embed a bunch of, like, third-party things as well, right? Because, like, then it becomes a lot easier.
But, like, the main hesitation that I have is, like, I think that there are some good points that are being made, I think you said it's not Florian or.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:50:50 Fabian, Fabian.
Tyler 00:50:51 Fabio, Fabian was making, like, around, like, security and that kind of stuff, I think it does make a lot of sense. Decoupling, like, memory and performance, I think it makes sense. But the… the…
The thing I come back to is, like, if…
if that's… if that's critical for you, then, like, just… you need to run it as a separate process anyways. Yeah, just run it as a standalone, and if you're doing that, then you can… you can have all the control you want. So it seems like if we could…
Get this thing more integrated so we don't have any of these translations, we don't have to go over the network for communication, we don't… like, essentially, like, what we're trying to do, if we run it as a separate binary, is…
Run it as a standalone, but hook it in into one binary, whereas, like, you could have just decoupled them, and, like, you could have just done it that way, right?
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:51:37 Yeah. I mean, the other reason is…
The one other reason that we decided to maybe explore shipping this as a binary rather than as a…
embedded as code is that ability for us to upgrade without…
Having to upgrade their collector.
M.
So…
So here's the… the main issue is that we find a bug, we need to deploy an OB bug fix.
And then you need a new collector, essentially, for everybody that's running, that. So, for us, the hourly releases are much less frequent than our OB releases.
And it's a lot more complicated process, and does a lot more testing and all this effort around that, so…
We'd like to be able to kind of just upgrade that component alone.
And… per customer.
Tyler 00:52:30 Yeah, I mean, that makes sense.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:52:32 Catch.
Tyler 00:52:33 It sounds like it's… it makes a lot of sense for Alloy. I don't know if it makes a lot of sense for, like, the collector contrib as much, but that being said, like, I… if… if…
Ob gets embedded in the collector contribib, is that going to mess with Alloy?
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:52:49 Yeah, then we'll just, start using Obi straight. Like, that's also been discussed. So, because I was gonna pick up Obi, if that becomes part of theirs, then we will not be doing the payload thing anymore.
Tyler 00:53:02 Okay, but then…
But then, it's going to depend on your collect… like, your collector problem becomes more important than if you're gonna depend on this upstream embedding of Obi into…
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:53:13 Yeah. Okay. Yeah, but my understanding is that Ulta Collector
upgrades much faster. The recycles are not…
Tyler 00:53:21 Yeah.
Yeah, I mean… Depending on collector-contrib, maintainers and approvers, but yeah.
True, yeah.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:53:33 So we'll be able to much quicker release a fix, yeah.
Tyler 00:53:36 Okay, alright.
Yeah, I… because, like, that's the only thing, is I'd hate it to, like, us make that decision, and then that means that, like, you guys couldn't ever use the collector can trip stuff, but that doesn't sound like that's the case.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:53:47 No, it's no problem, like, because they're separate components anyways, if they get picked up and it's OB, and people, we tell them not to use that, but use ours so we can upgrade it, whatever. Like, that's… that's totally fine. It will be a different component.
Two code bases will… the binary will be larger, but…
Yeah, right. I would say stay the current course, Nimrod. I mean, let's… let's get that done.
I don't see…
I don't see a problem, and if we ever need to shift in the future and do this binary thing, and it's superior for whatever reason, then we can discuss that.
Tyler 00:54:20 Agreed.
Nimrod Avni 00:54:21 Sounds good.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:54:24 I mean, there's also one other kind of upside to the binary, I don't know, I'm taking too much time, but security-wise, it's not just about running… technically, if you're a privileged process, like, collector's privilege, they can drop… the collector can drop its own privileges after it launches OV, or the profiler.
So…
Tyler 00:54:43 Oh, really?
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:54:45 Well, yeah, you can say, I'm gonna lower my permissions.
Tyler 00:54:50 By permissions, you mean, like, EPPF capabilities, or are you talking about, like…
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:54:53 Yeah, so you're gonna launch these components that are… as the standalone binaries that are higher permissions, then you can lower your collector permissions automatically, right after. So collector is essentially with higher permissions only temporarily.
Tyler 00:55:08 Hmm.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:55:09 So…
Tyler 00:55:09 Yeah.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:55:10 It's… it's something, but then you can never reload the component, because you'll need…
Higher permissions to launch it again, so…
Tyler 00:55:18 Right.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:55:19 That is.
Tyler 00:55:21 Okay, alright, then I think there's a lot to do there.
Steven, I moved your MQTT, in progress to the latest PR, AMQP…
Next, did you want to talk a little bit about this?
Stephen Lang 00:55:36 I mean, we've only got 5 minutes. It's just to share what I'm working on, that's all, so people can check it out, async. There's nothing that's actually integrated and up and running right now. There's no new feature just yet. I just wanted to share what I was working on, that's all.
Tyler 00:55:52 No, that's awesome. I'm super excited about this protocol, so, yeah, I'm really excited this is getting pushed through, so yeah.
Okay, cool. Then, the last question I had, and I want to talk about this more as, like, a precursor, cause… just given, like, the time, is the road to stabilization. I think that, I wanted to maybe just…
thinking about the year coming forward in 2026, I think this is… this is a pretty big goal of mine, to have a road stabilization.
But I may be just more…
Wanted to take a second and say.
Next, week and next meeting, maybe we should talk about goals, because obviously we have some bigger goals that we've already talked about here, an hotel receiver, a generalized context propagation map, like, there's some really big, ideas, network monitoring.
Yeah, so all three of these first issues, yeah, more, more protocols, so there's a lot of really good goals here.
I'd like to make sure that, like, we have an understanding of, like, all of the things that we wanted to accomplish in 2026, and then understanding how that fits into this road to stabilization. I think that,
I'd like to get other people's opinion on this, on, like, where they see the road to stabilization in the prioritization compared to some of these other goals that maybe aren't in line with… not necessarily, like, opposition, but they're not leading towards the, you know, the achievement of that. So, I am…
I think more just asking you to think about this over the next week. I'd love it if you could maybe get some… some notes on what you're trying to achieve. So, obviously, like, Nimrod and Mitya, you're doing a great job of, you know, documenting things you're working on. Steven's doing a great job here as well, but, like.
Maybe next week we can come back and talk about, like, goals that people are trying to achieve more generally, and then we can maybe ask, from all of those goals, what do we need to actually achieve, stabilization, I guess is kind of the next question.
So yeah, obviously, just wanting people to think about that, as the new year starts, so yeah, just a heads up. I'll probably also ping this again in, Slack before the next meeting, just to kind of, like, remind people to come prepared to the next meeting.
But otherwise, yeah, I'm pretty excited. I think that there's a lot of really good work going on here. I also think that this road to stabilization is not as far as I initially thought. I think it's something that we can get accomplished this year. Weirdly enough, I mean, not weirdly enough, I think a lot of that has to do to the fact that Balo is such a mature product that we adopted here. But,
Yeah, I think that's… it's a… weirdly enough for OTEL, that normally doesn't happen as fast as I think we can do it, so, yeah.
So yeah, I just wanted to bring that up. We'll talk more about that next week. I'm gonna try to prioritize the agenda around that next week, so plan to come and discuss, and yeah.
That's about it.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:58:36 I'm grateful.
Tyler 00:58:37 Yeah. Very important.
Okay, 2 minutes left. Any other topics people wanted to talk about real quick, or ideas, or shoutouts?
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:58:49 Oh, there was a blog post somebody posted about using… Obi.
Tyler 00:58:54 Oh. Forgot to share it.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:58:55 I don't know.
Tyler 00:58:56 I don't know if I saw that.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:58:59 It was supposed to be Packer News. Was it in? Packer News. Somebody…
posted… I saw it over the holidays, I completely forgot about it, sorry.
Tyler 00:59:08 Oh, that's awesome. Did, is it in…
Marc 00:59:12 It's supposed to know that.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:59:13 The URLs, I'll post it in the notes.
The Euro sells Vela, but they use Zobi, so…
Tyler 00:59:21 Close enough.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:59:23 Yeah, exactly.
Let's see… What's going on?
I can't click the button.
Yeah.
Tyler 00:59:35 Oh, cool.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:59:37 Yeah, they were talking about zero-code instrumentation, How cool it is.
And how they got exactly what they wanted, so it was pretty cool.
Tyler 00:59:48 Yeah, this is awesome.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:59:50 Yeah, and there's nice diagrams and everything, So…
Tyler 00:59:54 Right? Yeah, this is great.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:59:57 Yeah?
Tyler 01:00:00 Well, cool. Yeah, I'll… Nikola, if you want, can you also post that in the EPF, Slack channel? And just link it there as well? I think that'd be great to talk about, yeah.
But otherwise, we are out of time. Thanks everyone for joining. I will see you all in a week's time. Otherwise, I'll talk to you asynchronously. Alright, bye.
Marc 01:00:21 Yeah, fine.
