SIG: OpenTelemetry Profiling
Date: 2026-11-12
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Ivo Anjo** 02:34 Hello.
**Felix Geisendörfer** 05:24 Alright, since we're 5 minutes in, I'll get us started.
And share my screen.
Okay, can somebody confirm you can see my screen?
**Florian Lehner** 05:42 That's fine.
**Ivo Anjo** 05:42 Works.
**Felix Geisendörfer** 05:44 Sweet. Cool. Then, yes, welcome everybody to the Profiling SIC, and as usual, we will… review previous action items, and then go to the rest of the agenda. So far, it's looking very light here. Nobody has added any topics, so if you have anything on mind that you would like to discuss or talk about, please feel free to add it here while we go over the action items.
And of course, spontaneous ideas will also be solicited at the end of the action item section.
So, yeah, on my end, I did make some progress on this one here, the TimeUnix Nano Clarification. I believe it's merged now, yep.
So thanks for the quick reviews I got on that. So we can check that off.
over here… And… Then, on the period types, I started working on that, and I guess one… I'm not done yet, but, one of the things that I chased down was in, previous CIC meetings, specifically in February, it's been a while, Frederick and Florian brought up some, profile types that might not, need or have a period type, and, so I looked into them, because they're from the eBPF profiler. It was the off-CPU profile type, and the, the K-probe and U-probe profile types, and I think we're actually better off if we give those, profile types a period, in particular for off CPU, we can do context switch and count, and we can do for the K-propes, probe hit and count, and for the the K probe and U-probe, there's currently no, sampling, so the period would just be 1 to indicate we're taking every event that's coming in. For the, context switches, we actually have a natural.
sampling period, which is 1 over the probability, of, a given context switch being sampled. So if you have, 0.1 as a setting for 10% of contact switches, you get period 10.
And it's not perfect, of course, it's, like, not fully inversible, because there's also, I think, a minimum threshold for the minimum duration of off CPU weight that's getting recorded.
But I think we're all on the same page already when it comes to that, that the period type is more… an informational thing provided about the configuration of the profiler, not necessarily expected to allow you to fully inverse the sampling decisions. But the samples should always provides their values as weights that represent the unsampled quantities that are being represented. And that's actually also what this change here does.
I think from the discussion Florian that we had, you seemed to be open to maybe turning this into a reviewable pull request, so I'm gonna do that next. Yeah, if you want to say something, go ahead.
**Florian Lehner** 08:50 No, no, it looks fine for me, I already looked at it, and
**Felix Geisendörfer** 08:53 It makes sense, I think. Hardware of mic muted.
**Nayef Ghattas** 09:04 I could hear you Florian.
**Ivo Anjo** 09:06 Yeah, me too.
**Florian Lehner** 09:07 Test 1, 2, 3.
**Felix Geisendörfer** 09:11 No, I can' Florian, is it me? Can I not hear anybody?
**Florian Lehner** 09:15 I can hear Felix and Ivo, and now you…
**Ivo Anjo** 09:18 Yeah, it's you, Felix.
**Alexey Alexandrov** 09:21 I also can hear Flora.
**Felix Geisendörfer** 09:22 Can't hear anybody.
Yes.
**Alexey Alexandrov** 09:25 Can you hear me?
**Felix Geisendörfer** 09:26 speakers.
**Alexey Alexandrov** 09:27 Can everyone except Felix hear me? Yeah. Okay.
**Florian Lehner** 09:31 Okay.
**Felix Geisendörfer** 09:32 Cool, I was about to have a meeting just by myself the whole time, but now I think I have audio back. So, sorry for anybody who said interesting, fun things while I was yapping.
So yeah, Florian, whatever you were gonna say, can you say it again?
**Florian Lehner** 09:46 Yeah, the change looks good to me, and I think, yeah, the direction also is fine.
Yeah, it totally makes sense when you're going this way, yeah.
**Felix Geisendörfer** 09:58 Cool. In that case, I guess the question about, like… because what this is going to inform here is whether we should mark period type and period as explicitly optional, or if we should be more like, no, you should provide a period.
I am, other than these two examples, not aware of any profile types from PPROFs that are in common use that do not have a period type and period.
Curious if anybody knows any?
**Alexey Alexandrov** 10:32 I… it seems… it seems… I think it's reasonable. Was there some… Were there any objections before from doing this? I'm trying to remember when we had this discussion. Maybe is there something in the notes, or in the document that I wrote previously?
Trying to dig that out.
Yeah, I think… I think the only objection was that it can be… randomized or probabilistic, so there is no single fixed period, but I think in your proposal.
Yeah, my… but in my document, I also say, but it's unclear Whether we could just set it to the mean.
Period. In… in the.
**Felix Geisendörfer** 11:26 this case.
**Alexey Alexandrov** 11:27 So I think it… I think it makes sense, to me, at least.
**Felix Geisendörfer** 11:34 Yeah, I guess the other benefit, but we have some problems there that we still need to solve, I guess, yeah, we can talk about it in Florian's request here, but having the period does help with, distinguishing potentially similar-looking profiles, from each other, because it adds more to the identity of the profile to some degree. But we already have some problems there, like, for example, in Go.
the, new text and block profile look completely indistinguishable. They do have a period in addition to a sample type, but that period is actually always set to 1, regardless of what the sampling rate is that's configured, so that's not great.
But, yeah.
I guess we don't have a strong use case for, like, setting it completely optional. I'll take another pass over this, but yeah, for now, I think we can basically just remove these two examples for, Profile tabs that don't have periods, and then I will continue working on this and present some more changes at the next meeting, so I wasn't quite done here yet.
Let me just capture the quick summary.
Okay, cool. Any other period-type stuff anybody wants to discuss here?
If not going once, going twice, I'll take us to Jonathan's action item about payload change.
Yeah, Jonathan, you wanna talk about this? Is Jonathan here?
**Jonathan Halliday (IBM)** 13:55 I am here.
this has just been waiting to gather comments. I guess it's probably been waiting… long enough at this point, I think if people are going to comment, they probably have, so I'll take a look at that probably on Monday, and get, get any changes in, and then I guess it can be merged.
**Felix Geisendörfer** 14:24 Okay, sounds good.
Any, any other thoughts on this one?
**Alexey Alexandrov** 14:32 There are some unresolved conversations on DPR, but did you say that, like, those.
**Jonathan Halliday (IBM)** 14:36 Yeah, obviously.
**Alexey Alexandrov** 14:37 solved.
**Jonathan Halliday (IBM)** 14:38 I haven't looked at it, yeah. Yeah, I'll do that next week.
Some of them make absolute sense, they're easy accepts.
less sure about.
I think… was it Rouje who was talking about basically going back to the old way of doing things? We used to have a separate field for the the profile type, and I… Kind of abolished that once we'd added attributes, because we wanted the attributes to be able to… communicate file type anyway, and I thought, oh, we've got attributes now, let's just use that for everything, and we'll just shove the… To type in there, assuming it can't be derived from the file name, which it usually can.
So I'm unsure if I want to go back to a hybrid approach, where some of the information is in dedicated field, and some of it's in the attributes.
It kind of feels cleaner to me just to use the attributes for everything, although… That does mean we then have to specify what the attributes are. We have to have semantic convention for them.
Vote now.
I'll just make an arbitrary decision on Monday.
**Felix Geisendörfer** 15:46 Yeah, I will take another look, hopefully before the end of the week, so you'll have it by Monday.
But I guess my gut feeling is I like attributes as well, but I'll take a look.
**Florian Lehner** 16:16 I just opened the semantic conventions and the specifications, and so far, we have the, for the original payload format, only known values.
Meaning if we turn them into attributes, we should remove them from the specification and just have them in the In the attributes part of the semantic conventions, I think.
Otherwise, it will be confusing to have, known values on the specification, that might conflict with the attributes that you then have on the semantic conventions part.
**Felix Geisendörfer** 16:53 Where are they right now in the spec, or…
**Florian Lehner** 16:55 And the specification, yes.
**Felix Geisendörfer** 16:57 Yeah.
**Florian Lehner** 16:58 Under known values, so I can put, click on the chat.
**Felix Geisendörfer** 17:16 Yeah, that makes sense, but I guess let's figure out what we want to do with this change first, and then the follow-up changes will be evident.
**Florian Lehner** 17:24 Yeah, sounds good. I also tend, to, with Jonathan's, opinion, and… Having this as an attribute.
**Felix Geisendörfer** 17:36 Alexey?
**Alexey Alexandrov** 17:38 Yeah, I think… I think the change is good, the only thing that… I kind of, like, paused on is the data source name.
for the field, because when I see data source.
I think I think less about the payload and more about the producer, in a way. So we have data source, and then it contains the payload bytes, but this is a minor knit, I… probably… I also wondered for a second, but I haven't taken a look whether… We introduced data source, is this just… term that is private to profiling, or is there a similar… is there a similar concept in OpenTelemetry that we could reuse? Because every time, like, we throw in a new term, and I'm like.
**Jonathan Halliday (IBM)** 18:22 I'm like, oh.
**Alexey Alexandrov** 18:23 So, there's some costs to it.
**Jonathan Halliday (IBM)** 18:25 Yeah, I wanted to try and abstract away from using file, because they're not necessarily files. I mean, JFR happens to work that way currently, but, you know, you can just use an in-memory buffer for this. It's really the format of the data that matters.
So data source was really just an attempt to get away from using file, but… I don't think too much about it, to be honest.
I can… Go and take a look and see if there's anything pre-existing in, in Hotel that might align better.
**Felix Geisendörfer** 18:59 format? I don't know.
**Jonathan Halliday (IBM)** 19:03 Data format, rather than data source.
**Felix Geisendörfer** 19:06 Yep.
**Jonathan Halliday (IBM)** 19:07 Yeah, I mean, data format would describe, like, the… the attribute name, maybe, but does it describe the data structure as a whole? Because the… the data structure contains the information, right? It's… that data structure is the source of the original information.
Because it has the payload bytes in there as well.
It's got both the metadata and the actual data.
So it's like a self-describing database.
**Felix Geisendörfer** 19:41 Okay, yeah, I don't feel strongly. I need to look at the specific change to have a more informed opinion, I didn't realize.
**Jonathan Halliday (IBM)** 19:47 Yeah, we'll give that a bit more thought, and yeah, Monday is the cutoff.
**Felix Geisendörfer** 19:51 Okay, makes sense.
I see some hands up. Alexis, you're still fresh or still?
Guess it was stale Nayef.
**Nayef Ghattas** 20:01 Yeah, I just wanted to mention that once we release the braking change in, new portal version. We need to go and update the… And that new portal version makes its way into the OpenTelemetry Collector project.
We need to go and update the version constant in the OpenTelemetry Collector project.
I discussed with a couple of OpenTelemetry collector approver and maintainers, and they said that they would prefer for us to do it.
So, we just need to keep that in mind.
**Felix Geisendörfer** 20:38 Is that part of the proto-release process, or pre-proto release?
**Nayef Ghattas** 20:45 It's after a proto release is done, and that proto release is upgraded in the OpenTelemetry Collector repo.
**Jonathan Halliday (IBM)** 20:54 Yeah, I think it's… yeah, you're right, it's got to be part of the step where… The collector picks up the new version of the proto, so it does a dependency upgrade, basically.
**Nayef Ghattas** 21:04 Yes, exactly.
**Jonathan Halliday (IBM)** 21:05 Yeah.
**Felix Geisendörfer** 21:09 Okay, that makes sense, yes.
But basically, just merging Jonathan's PR does not immediately trigger that. It's just, we need to be watching out for upcoming proto-release and coordinate.
Got it.
Is there… is there a way we can… have, like, a test in the collector that fails if somebody tries to upgrade the proto and they don't bump this? Is there a way to do that?
**Nayef Ghattas** 21:45 Hmm, not sure. We need to think about it.
**Felix Geisendörfer** 21:55 Would somebody want to take an action item?
**Nayef Ghattas** 21:58 Yeah, I can take that.
**Jonathan Halliday (IBM)** 22:02 To support that, might it make sense to… Instead of just having a comment in the .proto file, it says development version.
If we made the natural field.
Then you could programmatically test against it.
Because something like an enum, I mean, admittedly, it would only have one value, right? But it… that would… Code Jane.
when you've… you ingested the product file and generated Go code from it.
you could then test against that resulting Go code, I think.
I've not tried it, I'm not a Go developer. That's how I do it in Java.
**Nayef Ghattas** 22:42 But I, I think we looked at it, and there's no way to encode a constant in a portal?
**Jonathan Halliday (IBM)** 22:51 Yeah, I think you can do enums. Named… named enums? Wouldn't work, maybe? You could certainly do a field number.
You could have some fake data structure that just had a field in it, and that field had a… The whole field time numbers, but if you bump that.
That would be visible in the generated code, I think.
There are probably things we could do. Do we want to invest the time in it?
How often is this gonna change?
**Felix Geisendörfer** 23:26 Yeah, I don't know if we consider techy workarounds, I think we were mostly looking for, first-class constant.
support, but I think some of the workarounds he was suggesting could be viable.
Would you want to take a look at that as part of looking into the failing test casing at Nayef?
**Nayef Ghattas** 23:47 Yeah, I could look at hockey workarounds, but I guess it's a trade-off on… How much time you want to invest in that?
**Felix Geisendörfer** 23:56 I would just ask you to take, like, a light action item on checking what's possible and reporting next time.
**Nayef Ghattas** 24:02 Okay.
**Felix Geisendörfer** 24:03 And if it seems like a pain in the ass, we can totally agree as a group, like, okay, this is only going to be a thing for next few proto-releases, we'll just be vigilant, and it's not going to be worth automating. That's an okay resolution, but I think it would be nice to just check what we might have missed on the first round when we.
**Jonathan Halliday (IBM)** 24:18 Yeah, I mean, it feels like we're still on track for beta by the end of the year, and this is arguably going to be the only breaking change.
I don't think it's… it's worth looking at too deeply.
**Felix Geisendörfer** 24:30 Yep.
Sounds good.
Okay, any more thoughts on this?
I'm old.
Certified deadline Monday… Going once… Going twice… And I will move us to Florian's item about… well-known sample types. Do you want to introduce it?
**Florian Lehner** 25:06 Yeah, well-known sample types, that's one of the items that brings us closer to beta. One of the big requests is that, we provide a list of known sample types.
And probably period types, so they can backends can actually handle the data. At the moment, as we don't specify something like this, the producers can just send anything, and it's part of the backend to figure out what it actually is.
I took inspiration from Go, PProf.
and Perf, what are potential sample types, and, try to cover as much as possible. I'm pretty sure there are cases I did not cover, maybe that are not that used, or, Or maybe I did not know about them. But I wanted to have something that we can start, thinking about it. There's also a comment on the PR about having this as an attribute type.
Instead of, listed known values in the specification.
I'm a little bit against that, with the reasoning that we have dedicated fields in the proto, and we should not remove these fields now, just before, the beta, and have, attributes for them. So, it would also be making compatibility with, PTROF.
harder, I think, if you turn this now into, attributes. So that's why I think having them as, known values in the specification is just fine.
It's really just more like a guidance for backends.
And, a direction for pre-users on, on how to label the data they are sending out to the backends. For the backend, it does not mean they need to accept them, it's just, hey, there's something that could The, there's something that, could look like this.
If backends decide on the sample type, they drop it, they drop it. It's up to the backend. There's no hotel… Specification, how our backend needs to handle certain stuff they receive.
Yeah, otherwise, yeah, I hope that's a little bit of an overview of the PR.
And, yeah, feedback is, welcome.
Also, questions.
**Felix Geisendörfer** 27:37 Yeah, I mean, as I already left comments on the PR, but I'll just state some here for the crew, because I think it's relevant.
I think that… this pull request gets us closer to, I think, backends, understanding what consumers might send, and consumers might aligning around some standardized sample types, which is a good thing, but I think that It's probably not enough to, like, enable certain use cases, like, for example, can… two of these, yeah, profiles, like, two wall clock profiles, or off-CPU profiles, or something from different implementations be considered equivalent in terms of the semantics? Like, if you see a certain… anomaly there, is it the same interpretation valid for that? I think would be one litmus test, and I think there's not enough specification here to guarantee that.
The other one that was proposed by Frederick at a previous meeting was, could you actually… merge these datasets together, like, maybe a good litmus test would be, let's say you have the eBPF profiler collect CPU profiles from an application for one hour, and then for another hour, you have the Go CPU profiler come in and do it.
could you take those both data sets together and treat it as one continuous CPU profiling observation of that application over time? And… The answer is, again, like, probably not based on the information that's in this document, because there's a lot of details involved, but, yeah, I think I can get aligned with… like, getting this landed, even with weaker guarantees, but we should just be kind of clear on what those guarantees are, and not, like, I think, yeah, there's, like, a word here, like, interpreted or something that's doing some heavy lifting, so anything we can do to just clarify what we actually expect producers and consumers to be able to do based on the guidance in this document is my take. But yeah, we can hash that out async.
Just wanted to let the group know that I think that's the state of some ongoing discussion.
Yeah, Florian, if you want to respond real quick, do, otherwise Alexey.
**Florian Lehner** 29:56 No, Alexey, thank you.
**Felix Geisendörfer** 29:58 Cool.
**Alexey Alexandrov** 29:59 Equivalence is an interesting topic.
I wonder, like, to what… how far we want and can take it, because, for example.
Let's say you collect cash misses.
then even on AMD and Intel, there can be some subtle differences regarding whether… I don't know, like, whether prefetches are counted, whether, like, hardware prefetches and software prefetches are counted, or whether speculative traffic is counted, and so on and so forth, so… When we say… do we have, like, specific examples where… We think, knowing that these two profiles are equivalent.
would be practically helpful. Is this about simple cases, such as, like.
CPU time from Go and CPU time from CPU, where we know that, well, it probably uses SIGPROF, for example, in both cases, and it collects stacks, so we're really counting the same thing. I'm just curious, like, for… I'm not saying it's… I'm not saying it's not a good idea, it's just, like, I start thinking about specific corner cases, but maybe I'm taking it so far with thinking about exceptions or corner cases.
**Felix Geisendörfer** 31:10 So, I think that, like, in some cases, some similar-looking profile tabs will never be equivalent. Like, the architecture-specific things you just mentioned is a good example of that, where there might be cache misses or something that are similar enough if you squint a little bit, but then in practice, like, have different semantics.
So, maybe the goal shouldn't be to, like, make these things equal and abstract over them, but the goal should be that you should be able to tell which one you're looking at, and I think this is not currently possible through the sample type, alone. Like, we will need to have another field that says like, this was recorded by Linux Perf on ARM or something, and that clarifies the semantics of the data that is arriving.
And… yeah, I think that's… kind of one thing we need to consider, but then, sort of, for some stuff, we might have equivalents, like, for some simpler cases. Like, CPU is a good thing where, like, OTEL's, correlation idea, I think, should work. Like, for example, if you have CPU profiles.
they should maybe have a correlation to, CPU metrics in OTEL, right? And sum up to the same sum for, like, subserved container, for example, or things like that. And I think… maybe specifying some of our profile types to the point where there can be correlation with an OTEL, or even, like, just cross-checks between different profile implementations, like, hey, if you can observe the same application, over time with this profile and that profiler, the two numbers should be equal. Now, there might always be implementation-based limitations, like, I don't know, the SIGPROF-based profilers will not be able to profile libraries that are turning off signal handling for SIGPROF and things like that, using signal masking. So the devil's always going to be in the details, but I think, like, in some cases, we can try to align, but there will always be cases where we can't. I guess, my take here.
**Alexey Alexandrov** 33:09 One analogy that comes to mind is that on Intel… in Intel PMUs, there is a notion of architectural events, which are kind of, like, guaranteed to be… to have the same semantics between Between different models of CPU.
So, just… just as a thought, like, maybe there could be some small subset of… metric types that are… standardized by OpenTelemetry, and then if you use them, then you are… You are required to follow certain semantics?
**Felix Geisendörfer** 33:52 Yeah.
**Florian Lehner** 33:52 I think at some point in the discussion we had on the PR, additional attributes were very, suggested as an option to differentiate these cases, but I think also looking into the protocol, with the instrumentation scope, we already have some kind of indicator where the data is coming from, and the instrumentation scope tells you what… who is collecting the data? So… it should be possible already to differentiate, hey, this hotel profile was collected by the Go runtime, or by the EVPF Profiler, or JFR, or someone else. So, if the instrumentation scope is correctly filled in, there should already be a case to say, hey, these are at least different sources. If they are comparable, yeah, I agree that's, Hard to tell.
And, you know, if they can be merged.
Maybe… maybe not. I don't know.
**Felix Geisendörfer** 35:02 Yeah, but like I said, for the instrumentation scope, even that would not be enough if you… well, it depends on what you consider the instrumentation scope, but for the block and mutex profile, which would have an instrumentation scope of the Go SDK or something in OTEL, and then you have the same profile sample type and period type, you still need some other attribute, I think.
But, yeah.
Who's next, Christos?
**Christos Kalkanis** 35:30 Yeah, so I think we have three questions here, right, for this information. One is, this information is purely advisory, and it's meant to help the backend interpret the data. We're making no guarantees for correlation and so on.
So, if that's the level that we want to have this information, then attributes would work.
Because I just went through the pull request, and there's a person there that left a few comments, and he makes the case for, okay, let's… like, this would be better as attributes, because then it would be more consistent with the rest of the auto.
So, for this level of looking at the data, this would work. Purely advisory, no guarantees, and no external specification. Then there's a secondary level, which is, we keep this in the specification, because we plan to actually extend them, right? We plan to provide more… usually we use a specification when we give an algorithm, when we specify exactly what the, you know, the attribute means, right? So in this case.
For example type, we would have a paragraph getting into implementation details of how a profiler would actually implement it, or Something to that effect.
So that's still not strong enough to give the guarantee that different profilers with the same sample type can be correlated, because implementation details can still differ, right? And the third level of looking at this data is if we have different profilers, and they all implement this specification that we give them, and that would be the guarantee, then, that you could correlate the data. I don't think… We are at that level, or maybe we don't even want to be at that level, because, It's a coordination problem, right?
But the second level, where We have, or we plan to, in the future, extend the specification to provide implementation details, so that other profilers could actually take that into account, and then correlation becomes possible, because the semantics are identical across different profilers.
Maybe that's something to… to aim towards.
**Felix Geisendörfer** 37:45 Yeah, I would say we definitely can't, like, define all the semantics for all the profile types out there, but I think if we're… wanted to focus CPU Profiling is obviously at the center of a lot of the activities right now, because that's what CBPF Profiler has as a primary profile type, and what just about every other profiler also supports.
And maybe trying to get to the point where we can specify what we think a CPU profile is, and how it correlates to other metrics in OTEL, and when it should line up, I think that could be a useful thing that the CIC should consider in scope, even so we might not immediately do this for all the other types of profiles.
Nayef?
**Nayef Ghattas** 38:45 Yeah, just on… to go back on the instrumentation scope bit, I just got again the instrumentation scope definition in OTEL, and I'm not sure it's the… It's actually the right concept, here, what, like, what the… what the hotel spec says, it's a logical unit of software with which emitted telemetry is associated, so represents a module, package, class, library, or framework.
So it does seem to be a logical module within a… Within a software, rather than something that we could use to differentiate between different profiles.
**Florian Lehner** 39:33 I think it could be an option. Yes, the specification or the documentation around the instrumentation scope was written before, tools like OBI or EVF Profilinger come along, but, if the instrumentation or the tooling is for example, EVPF Profiler in version 123, if the same instrumentation scope says, name EVPF Profiler version 123, then they should produce the same, same result.
**Nayef Ghattas** 40:06 Maybe, but then we should change the instrumentation scope definition in OTOL to make for that use case, I think.
**Florian Lehner** 40:14 So, at the moment, the UPF profile already sets these, these values for that case. I think documentation on the OTA site is not up to date.
But that's… at least that's how I interpret, proper specification around it.
**Nayef Ghattas** 40:29 Then I'm not sure the profiler is, like, respecting the auto spec, because, I mean, the examples that the document give is, like, module, package, class, library, like, it was built with, main… mostly, I guess, tracing and logging in mind, where you define, like, which package or which module is emitting a specific log or a specific trace, so you can link with the… with the source code.
And that is, I think, like, the use case as it is written in the hotel spec. So if we want to use it for something else in profiling, well, we should probably think about that and maybe update the spec.
**Florian Lehner** 41:20 Yeah, makes sense, makes total sense. I can bring it to the spec people next week.
And, ask them what they think about, Introducing such use cases to the instrumentation scope.
Does make sense.
**Felix Geisendörfer** 41:37 Is there a strong benefit of doing that, instead of just having an attribute that we standardize on the profile level, on the profile message?
**Florian Lehner** 41:51 We could have both, I think, and there's nothing that should block us.
The attribute might be faster.
**Felix Geisendörfer** 42:01 I would probably slightly prefer to not, like, get in the business of arguing with people who have created instrumentation scope for their use case, to be like, let's give it… it's also not good for OTEL in general to be like, oh, this is really, like, a free-for-all for any kind of instrumentation scope, imaginations that people have, so I think we would probably be better off just… Having an attribute on the profile message that we say, like, profiler name, profiler version, and then maybe we also, like.
have a registry where profilers can register themselves, as, as, like, a namespace kind of thing.
Yeah, that would be my preference. And we also get the attribute deduplication at that level, which is nice.
**Florian Lehner** 42:45 Okay, it makes also a way forward.
**Felix Geisendörfer** 42:53 But yeah, somebody should probably take an action item. Would this be something you want to carry on as part of this one, Florian, or somebody else take an action item on this?
**Florian Lehner** 43:03 Contact-to-action icon on adding a new attribute, yeah.
**Felix Geisendörfer** 43:08 Okay, cool,
**Nayef Ghattas** 43:23 I mean, also, to be fair, there's already a SEMConf key that is called telemetry.
Hmm… that has telemetry.distro and telemetry.sdk.
So for the SDKs, it's used to set the language, the name, and the version.
And for a distro, like the collector, it's also used to set the name and the version.
So we could probably also use those.
**Felix Geisendörfer** 43:54 Which level are they usually applied on?
**Nayef Ghattas** 43:57 I'm trying to figure that out from the… From the spec.
**Felix Geisendörfer** 44:08 Yeah, I guess we don't need to solve it on this call, but it's a good pointer that we should look at some prior art in that space and see what other, hotel components do right now to… Yeah, keep track of the fact that they're producing telemetry.
**Nayef Ghattas** 44:25 Yeah, makes sense.
**Felix Geisendörfer** 44:29 Cool. Anyway, going back to your original pull request, Florian, I think we… as long as we find, like, a good way of describing, sort of, what this is expected to accomplish and whatnot, I think we can get this landed pretty soon, because I guess it is helpful to… make a list of C.
common sample types that we expect to be in use, and for backends to see in the future. And I guess people implementing this stuff will kind of know for some of the sample types what they usually mean, which profiler produces them, and then we can get better over time to, like, yeah, with the next thing of having a telemetry SDK name or version or something, we'll figure that out in addition.
Cool. Any more thoughts on this topic here?
We certainly have time.
**Nayef Ghattas** 45:22 small note, I did look at a couple of SDKs, and they're all setting them as resource attributes.
**Felix Geisendörfer** 45:34 resource attribute.
Huh. Okay, I guess we could do resource attributes.
Thanks, Nayef.
Then, once again, any more thoughts on this? Doing… Once?
Christos unmuted.
**Christos Kalkanis** 46:01 Yeah, I just had a look at async Profiler, because it supports OTLP profiles, so maybe we can see if it's using instrumentation scope, and then what value is it actually setting?
Just out of curiosity.
Because I think we're making the assumption that the BPF Profiler is pretty much the only profiler so far, but… we should take a look at what else is out there, maybe the implemented profiles?
**Felix Geisendörfer** 46:29 Yeah, I think that's a good idea to check what they're doing.
**Christos Kalkanis** 46:31 I can, I guess.
**Felix Geisendörfer** 46:32 It doesn't mean that we'll have to do it that way, but it's gonna.
**Christos Kalkanis** 46:34 Yeah, yeah.
**Felix Geisendörfer** 46:35 Normative to know, yeah.
But yeah, once we have a strong opinion, we could just send them a pull request being like, this is how OTL wants it done, and if you want to be hotel… UTL native, please, please merge it.
Then, any more thoughts on this again? Going once, going twice.
Three times.
Then, if not, we are staring into the abyss of an empty agenda, and we have almost 15 minutes left. Does anybody have any spontaneous topics that they wish to bring up?
**Florian Lehner** 47:23 Do we have any burning open big items that block us from going to beta?
If you look into the road map…
**Felix Geisendörfer** 47:41 Thank you.
So, I guess we should clarify, like, to what extent the… semantics of sample types… I guess the period type we agreed we want to do, but we have that issue here. I guess the, semantics of sample types, I guess this is this one, right?
**Florian Lehner** 48:04 Yes.
**Felix Geisendörfer** 48:05 Okay, so, okay, we have that one here.
The payload, I mean, we've talked about.
Yeah, I don't know if we have any other topic that… We're not tracking right now. I think those are the three major things we need to get.
Together, and… Then better would be within reach.
I don't know if, the hotel TC or GC has opinions about us moving to Beta, if they have ideas on us doing that too fast within one year, or, like, additional hurdles for Beta versus Alpha.
You're shaking your head, Florian, as in, like, you know the answer is no, or you don't know, and shaking your head.
**Florian Lehner** 48:55 I don't know.
And I'm scared if they come up with something we don't know. I think the only problem for us is that we don't have any representative in TCGC.
At the moment.
That we can ask such a question.
That's… yeah, that's… would be my only concern, but it's an auto organizational… problem, I think. That's something that we cannot solve.
**Nayef Ghattas** 49:29 I mean, it's, isn't it Tigran until he leaves for…
**Florian Lehner** 49:38 Did Titron already left?
**Nayef Ghattas** 49:41 Oh, did he leave already? Because he said that he's going to find us someone to sign.
**Florian Lehner** 49:47 Okay, I'm not sure, because I just noticed that I don't see Tigran anymore in meetings, if I try in hotel specification meetings.
Hmm.
But it's… can just be a time conflict for him that comes up. So that's…
**Nayef Ghattas** 50:05 I did start a DM with him a while ago to ask him who was going to be the dedicated TC point of contact for us. I'll bump him again to see if he has any info.
**Felix Geisendörfer** 50:26 You'll ping Tiquon, or who do you think?
**Nayef Ghattas** 50:28 I think he said, he said Josh, he said he asked Josh whether Josh could be our TCGC member, but then he… did not, say whether Josh accepted or not, so…
**Felix Geisendörfer** 50:42 Okay.
Sounds good. But yeah, other than the governance risks, I guess there's nothing else on the… Roadmap that's missing right now.
**Jonathan Halliday (IBM)** 51:02 Does it make sense to get dual lease on having… Collector, and possibly a back-end.
updated and… Working well with the… The current spec.
I'm thinking of people who look and think, oh, it's beta now, it's mature, let's go and kick the tires, and then find that, you know, actually there's no implementation of it.
Or worse, there is an implementation that's out of date and doesn't need to operate with some other thing.
**Felix Geisendörfer** 51:34 You know,
**Jonathan Halliday (IBM)** 51:35 If we kind of put some… Effort into, you know, blogging about it, or whatever, with the… the Vuda, Getting some click-throughs.
need to make sure there's going to be a decent user experience for anyone who tries to pick it up, otherwise we're shooting ourselves in the foot a bit by… declaring it, oh, yes, please, please come and use this. Oh, by the way, it doesn't work.
**Felix Geisendörfer** 52:02 Yeah, I think it's actually a good idea that we do at least one release that doesn't officially declare us to be in beta, and then we do another release.
**Jonathan Halliday (IBM)** 52:13 Yeah.
**Felix Geisendörfer** 52:13 It makes no changes, but declares us to be better.
**Jonathan Halliday (IBM)** 52:16 Yeah, I was just thinking about the timeline in terms of, you know, we put out the proto release, and then that has to be picked up by the collector, and there has to be a collector release. Do we want to try and get this out by the end of the year, or are we just rushing it, and it's going to get lost because people are on holiday and not paying attention?
Would it be better to do… Well, I mean, we could go Peter by the end of the year and save the blog and… The publicity effort for the new year, when people are kind of paying attention, and I… More interested in, oh, fresh new year, let's pick up some new thing to play with.
Rather than, oh, I'm going on Christmas holiday, I've forgotten by the time I get back in January.
What's… what's best tactically?
I think we'll be finished to work by the end of the year.
**Felix Geisendörfer** 53:04 Hey, fantastic.
**Jonathan Halliday (IBM)** 53:04 There's not that much left to do, but it's not the best time to… To make noise about it.
**Felix Geisendörfer** 53:11 I think that, like, getting the work done by the end of the year, and then being in a position where in January we can pull the trigger, write the blog post, and declare it ready, I think sounds reasonable, and it gives us some time to test the release proto version. We should definitely have a protoversion that we expect to be the final and test it end-to-end with the collector.
Before we make an announcement about that version being the better version.
Or potentially the one after that with no changes.
And I guess from nobody disagreeing, then I guess we just decided that no.
Raise your hand if you disagree.
Cool.
We might need to do the other node change proto-release for it, just because there's some comments in the… I think in our protobuf files that mention alpha, so I guess we'll do that.
Yeah.
I think last time… last time at KubeCon, we were kind of in this in-between stage as well, where, like, the released collector was still maybe the one with… that was, like, had the final changes, but not the common changes or something, Florian, or… I forgot what it was, like, but something like that, right?
**Florian Lehner** 54:50 Yep, something like this. I think the only time-pressing topic is really the issue, the PR from, Jonathan, as it's a breaking change for the protocol.
But if we can bring this in and have a release with this before… Christmas, then we have time, and specification stuff, and attribute stuff is… It's not that time critical, I would say.
**Felix Geisendörfer** 55:19 Yeah, even… I guess a period-type thing is… More of a, like, clarification on how we want it to work, and, like.
I don't think we're gonna remove that field or, like, completely change it, so, yeah.
Okay.
**Florian Lehner** 55:37 No, same, same.
**Felix Geisendörfer** 55:39 I guess the only thing that we should be clear on if we make it strictly required, but I guess right now, I have to check, like, we've certainly, for some fields, like, put optional in there very explicitly. Maybe we need to do that? TBD.
**Florian Lehner** 55:55 I think it's not optional at the moment.
**Felix Geisendörfer** 55:58 I might be wrong. Yeah, I think it's not. But maybe we'll just keep it that way, anyway. We should make a decision on, sort of, like, if we plan to make a major change on it or not, but then if we make minor changes, that could happen, maybe not on the critical path to the better release.
Cool. Any, any more thoughts on beta blockers?
**Nayef Ghattas** 56:23 Not on beta blockers, but I do have a small update for the TCGC person. Tigran reached out to Josh.
And Josh will reach… back… we should expect Josh to reach back to us, maybe when KubeCon is done. I'm going to ping him.
on, on Slack, and hopefully you'll get an answer by next week.
**Felix Geisendörfer** 56:51 Cool.
Thanks.
And then, any more… Thoughts on any of those topics here?
Going once, going twice… in that case, not. Then, yeah, thank you, everybody, for attending today's CIC meeting, for all the work in between, and, yeah, have a nice local time. See you next time.
**Ivo Anjo** 57:25 Thanks, everyone.
**Felix Geisendörfer** 57:26 Right?
