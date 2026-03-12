SIG: Profiling WG
Date: 2025-08-21
Duration: 61 minutes
Zoom Recording URL: https://zoom.us/rec/share/SuBoKg3p8KzJjlTUiumJvQvp-imcGym7X1muzpjq4BIigYv7ItZpNWn5Tl3evUqg.6updUWx8iSaBaawz
============================================================

## Zoom Recording Transcript

**Florian Lehner** 02:24 Hello.
**Felix Geisendörfer** 02:26 8.
**Frederic Branczyk** 02:28 Hello, hello.
**Felix Geisendörfer** 04:36 I guess we can get started?
So, let's start by going through the previous action items.
On the active action items we have… A few 2PRs, 672 and 688.
They both seem to be merged, so thank you everybody who reviewed and got submerged. I missed one of them, so sorry about that, but I saw it get merged anyway, so that's great.
I'll check that off.
… And then… Alexi had to do on writing the consistency checking tool and library.
We had the repo request, I think the repo request has been filled by now. I think we have the repo, so I guess we should close that upstream issue.
… There's still some discussion about the repo being private.
Did it get made public? Just checking….
**Florian Lehner** 05:48 I think the repo is public, and Alexei already pushed the first PR to set up the infrastructure, and I think he will then continue pushing the rest of the code, so I think work in progress.
**Felix Geisendörfer** 06:02 Okay, then… let's update it a little bit.
… Depo has been created… This is in progress now, great.
Okay, review benchmarks from Crystals. Has anybody done more reviews on those?
Guess I see a few comments pending already.
But I guess the last comments have been June 16th, so I don't think there has been updates here.
Christos, I saw you on mute.
**Christos Kalkanis** 06:52 Yeah, I think we can move ahead, because, like we discussed in last week, it was kind of a last call, and I think people have had multiple sessions now, and also your pull request has been… Accessible for a long time as well.
**Felix Geisendörfer** 07:08 Yeah, I was hoping to find more time for it, but it's been difficult lately, especially now going up to GopherCon. I got a presentation to prepare, but I think we're good, so… I think the real test is when we're gonna start, like, cutting a release candidate, which we're gonna talk about in a little bit, and start trying this at scale with some of our… profiling offerings that we have, then I think if we find some performance issues, those will be really interesting, but I think we've done the homework.
Okay… I'm marking this as stunned.
… Yeah, so… The next one was already checked off, moveset from the list soon, … I saw somebody just added again the adding… setting up ProSig Profiling Repo, work in progress by Alexi. I think we already have the action item above for that, so… show what's….
**Alexey A** 08:03 … okay, sorry. There was… I was sending… I sent the PR last night, because I think there was some, like.
We created the repo, but there are some steps.
That, … Like, we need to do, but yeah, if we're tracking that….
**Felix Geisendörfer** 08:25 Do you need… Do you need review on this PR? I see you already got Florian and Christos.
**Alexey A** 08:32 No, I think two is enough. I saw one, one from Flora, and if there is one more, then I think we are….
**Felix Geisendörfer** 08:40 Yeah, 7 hours ago, Christos also gave you Korean one, so that should be ready to merge.
Okay, … Then the next item is Florian, add symbolization attributes to Hotel Semconf.
And profiles remove.
Hess underscore debug info fields.
Any updates that are flowing in?
**Florian Lehner** 09:10 Yes and no, the short answer. From the protocol, we removed the fields, so, there has fields, and also for message location, the folded, I think this PR is also merged.
But there is no progress on the SAMCOM side. So, if you have time, looking at, some multi-convention.
What would be the suggestion for us? Yeah, it would be nice.
**Felix Geisendörfer** 09:42 Okay, so this… Is this blocked by, like, us in the SIC, or from people from the SEMConf?
**Florian Lehner** 09:51 I think, the SimConf people are waiting our, for the, for us, as a, meta expert, basically, so that we can have an proper translation between PPROF and, hotel profiling.
**Alexey A** 10:09 I need to look at the latest state of the PR. One question I had, whether we have ability to set multiple attributes at the same time, because that's, … because that's what PProf has, where it can be, like, has lines, has file names, those need to be separate Boolean flags, basically.
**Florian Lehner** 10:26 Yeah, there was a discussion, I think, Jonathan, with the last sick, or the SIG before that.
And, yeah, and there are no dedicated attributes, because we cannot have In… or if you look at the SDKs, then, they are usually maps, and we cannot have maps, with, various, with the same key, but different values. And so the update was that, these are now dedicated, attributes.
**Alexey A** 10:56 Okay.
And I'll… I will take a look.
**Jonathan Halliday (IBM)** 11:03 I think we reached the conclusion that if there were strings rather than enums, you could… Have a concatenated list of them as the value.
I'm not sure, that's… the best way to do it, but I think… If I remember the discussion right, it turned out to be a possibility, at least.
**Alexey A** 11:26 Maybe separate fields is easier, because.
**Jonathan Halliday (IBM)** 11:28 Yeah, I think Separate Fields is better anyway, as it happens, but….
**Alexey A** 11:33 Because if it's a single field, technically you could wonder, like, is the order important, and things like that.
**Jonathan Halliday (IBM)** 11:38 Right, yeah.
**Florian Lehner** 11:44 Yeah, my takeaway was that the dedicated feeds are preferred, and that's the current status of the PR.
**Felix Geisendörfer** 12:01 And, just started catching up because I was taking some notes, or updating the to-do list, the PR is set the 2522, or the one before the symbolic occasion attributes 25? They're both 2522, I think we have this one twice now, actually.
I got confused.
Okay.
**Florian Lehner** 12:26 Sorry, I think we can remove one. The confusion is that I had a dedicated PR for location is folded.
**Felix Geisendörfer** 12:35 That one I split out into.
**Florian Lehner** 12:36 to-do item.
**Felix Geisendörfer** 12:37 and checked off, so… and I just made sure we don't have the other one twice.
**Florian Lehner** 12:43 Yep, yep, that's fine, sorry.
**Felix Geisendörfer** 12:46 Okay, all good. That's great.
And then we have… review context propagation documents.
Okay.
**Christos Kalkanis** 13:02 We talked a little bit about this in the previous week. I left some comments, … I think the main issue there is going to be… because there are multiple approaches, but we can't just do whatever we want, right? We need to get buy-in and consensus from the rest of Auto, especially the SDK people, because some of the approaches are intrusive. Like, for example, if you need to load the cert library.
and you're doing it in a manus language, now you're introducing that, right, into the application, and some people are not going to be okay with that, I'm assuming.
But yeah, I mean, the documents read good. I had some questions That revolve around semantics, because the documentation of the… a research part of OTEL is not exactly clear.
But I mean, we can resolve those asynchronously. I don't think we need to… Can't waste any time here just for my questions, I think, yeah.
**Felix Geisendörfer** 13:58 Good. Neyev, did we have anything else from our end on this?
You were unmuted, or at least I couldn't hear you.
**Nayef Ghattas** 14:11 Wait.
Oh, yeah, yeah, no, I said no, and thanks a lot, Christos, for reviewing. We'll take a lot of that document.
**Felix Geisendörfer** 14:19 Okay.
Cool.
Then I think we have… done through all this stuff, I'll move the done action items into the archived section later, or if somebody has a free moment here, can do it.
And I'll start taking us to the main agenda.
Yeah, I think this one I put out, … two meetings ago, and then I was on vacation last meeting, so I maybe missed some discussion, but yeah, basically… The idea was that we should probably do some release candidates on the signal, to give a chance for collector to update, for backends to try to implement OTel to update, and, like, give basically all the people here a chance to, like, do internal testing, and, because… We've done a lot of discussions, but I think we'll find a lot of stuff when we try to use it a little bit more. We definitely have plans to do that on our end, and I guess I was curious if that idea of, like, release candidates resonates in this group, and if OTEL typically does that, if somebody here happens to know.
**Frederic Branczyk** 15:41 I mean, especially if the main goal is for this group to implement it.
Does it really make much of a difference?
**Felix Geisendörfer** 15:50 … What do you mean?
**Frederic Branczyk** 15:53 Like, I'm just saying, like, I'm not 100% sure whether, like, release candidates are typical for the protocol versions in OTEL, so if, like, the main purpose is for this group to try it out.
I don't know that we should be blocked on, you know, getting permission from OTEL for that, and we just have, you know, this group implemented at whatever stage we are at.
**Felix Geisendörfer** 16:20 I see, yeah. And I guess it doesn't really matter whether OTEL formally recognizes something as a release candidate. It's more like for this group to be like, we're at a stopping point where we think we've got all the PRs into the protocol that we want to have, there's nothing major missing. Now we test again and see if something shakes out that we didn't anticipate, so we can still correct.
**Frederic Branczyk** 16:37 Yep.
**Felix Geisendörfer** 16:38 But we actually tag the 1.0, because the 1.0 tag is the one that's gonna… be something we want to be very careful about. … I see two hands up, I think Alexi was first, if I got it right.
**Alexey A** 16:52 Yeah, I think a release candidate definitely is… I think it's a good thing to do some testing within this group. One thing I was thinking about also is… I'm… it's like, it feels slightly uncomfortable that we are… with 1.0 release, we are basically jumping from… Like, 20 people know about it, and we can change anything at any time.
To… the whole world can start using it now, and we cannot change anything.
I wish there would be some intermediate state where, I don't know, like, maybe we would… post, like, maybe we would make, like, a blog post, like, OpenTelemetry blog post or something, like, we are near the final phase. This is… this is about to lock soon.
if you have feedback, please give it to us. I don't know, like, I don't know if, like, other signals had something like that, it's just, like, there's this step function, and I feel it makes me slightly uncomfortable.
**Jonathan Halliday (IBM)** 17:48 Right, if you click on the maturity levels thing.
It describes what the maturity levels are, and essentially we're going from a very early one to a somewhat early one. Release candidate does not mean what it means in other contexts.
**Alexey A** 18:05 Maturity level, let me find that link.
**Felix Geisendörfer** 18:09 Just opening it up as well.
No, there is a….
**Jonathan Halliday (IBM)** 18:18 Each candidate at the maturity level calls alpha.
And what the doc says is… The components ready to be used for limited and non-critical workloads.
And the authors welcome feedback.
But there's no compatibility guarantees, and things might go away without any notice.
**Felix Geisendörfer** 18:50 Okay, in other words, are you saying we should go to Beta first, before we go to RC?
**Jonathan Halliday (IBM)** 18:58 We're not going to RC, we're going to Alpha.
**Felix Geisendörfer** 19:01 Oh, we're going from development to art.
**Jonathan Halliday (IBM)** 19:02 release candidate of alpha. It's not release candidate of the whole spec.
**Felix Geisendörfer** 19:08 I see, okay. Because, yeah, in the document I just opened, there is, the level development, alpha, beta, release candidate.
**Jonathan Halliday (IBM)** 19:16 Yeah, we're currently in development, and we're going to Alpha, if you're using the hotel terminology.
**Felix Geisendörfer** 19:33 Okay, I mean, I honestly, I don't care what label we use, alpha is fine for me. I think the most important thing is that we sort of agree as a group that we sort of landed the most important changes to the protocol we want, and then we, as Alexi suggested, make this also known to maybe a larger audience in the group, so other people can come in And give feedback as well, so blog post, yeah, sounds like a really good idea. Antoine had his hand up next, I think.
**Antoine Toulme** 20:02 Hey, … So… I guess I'm part of that larger audience you're trying to gather for this, and my feedback is that I want to see interoperability tests between p-profile And, you know, the proto that you have for this, and the PProv.
Before we can move forward.
Because right now, I don't have confidence that this stuff works, and I tried to make it work, and it does not work.
I know we have a repo that's open for this now, so we're going to be able to work on this. I'm happy to help.
If you have this level of interoperability, even from the point of view of just having a diagram, a workflow, a textual explanation of how those signals map to each other.
That would definitely help a lot. I think you're going to get the same feedback from other SIGs, especially the Java or all the SIGs that have already a memory profiler that's already existing, is how do we map it from the native format that is specific to your SDKs to what you are proposing?
And I think that's a big endeavor, actually. So, I'm a bit worried that whatever you have right now, given what you're about to find out with this type of interop issues.
might… Make your move a bit premature.
Because you're gonna have to… you're gonna have to break stuff.
**Felix Geisendörfer** 21:22 Okay, point taken. I think a few of us here have taken the hotel format already and converted it internally into formats that are also targeted by PProv, so I think we have a sense that this can generally work, but I do agree that if you're somebody who hasn't normally worked on PPROF or the hotel signal, and you're trying to do it, I could imagine that there's a lot of gaps in the documentation and uncertainties on how to do it.
If you have anything very specific, then please point it out, but yeah. Anyway, long, long way of saying I agree with you.
**Antoine Toulme** 21:52 Yeah, you can look at the last meeting I came, I pointed out to my PR, which is trying to map from PPROF to OpenTeometry, and it doesn't work. We have 30 comments on it, I don't know what to do.
So I feel that.
**Florian Lehner** 22:06 Maybe I can jump on this, because I commented also on the PR.
And the conflict is really, like, that we have a lot of things in flux at that very moment. And, this would be also my comment on announcing alpha or a release candidate. We first have to wait before, for the release of 1.8 of the portal before we can make such an announcement.
Because if you make such an announcement, then comes the release, we will break a ton of stuff, not only for PProv processors, but also for the collector. And, if then people say, hey, there is a tag, alpha, whatever, and then we break things that aren't again, then it will… will have a bad view on us, and I agree, at the moment, it doesn't make sense to implement a processor, based on the current status, 1.7 of the protocol, with all the changes that are already merged, but not released.
I think the release of 1.7 was back in March, if I remember, plus-minus. Don't get me wrong, and please point me to the date exactly. But, it's… it was a long time, and we did a lot of progress in the meantime. So, I think we would benefit from a 1.8 release.
Give it 2 free weeks, and then announce alpha, or… release candidate one. I think, then we can also work on Anton's, PR and make the process over….
**Antoine Toulme** 23:40 It's not a processor, it's a receiver, but yes. Okay.
**Christos Kalkanis** 23:49 I think we have one… one big PR, big in the sense of semantic changes, right? And as Felix's PR, the stack.
**Felix Geisendörfer** 23:56 presentation.
**Christos Kalkanis** 23:56 that needs to go, absolutely needs to go in for 1.8, because if we get 1.8 without that, then we have to wait another iteration, right? And that would push us back.
So, I would say, I think the only remaining issue in the PR is cosmetic, and it's updating the ASCII diagram. So, Felix, if you can't do it, I can do it. I think Jonathan has already proposed to do it. Like, if you agree that this can be merged.
We can, yeah, move ahead there as quickly as we can to get this in in time.
**Felix Geisendörfer** 24:28 Yeah, if somebody just wants to make a PR against mine with the ASCII changes, I can definitely merge that in right away. I can also try to take a look later, but as I said, I'm currently, rushing towards my Go4Con presentation, so I'm a little… short on time, but yeah, on the 1.8 release that, Florian, I think, just mentioned that we need to tack on, is that already scheduled? How can we make sure we don't miss that release if that….
**Florian Lehner** 24:59 I don't know of any schedule, so… I don't see… someone from… the technical committee.
In the meeting.
So, you know, I can… I can take away a task and, ask Tigran.
What, what are the… Things to do for 1.8 release, and then come back.
If this helps.
**Felix Geisendörfer** 25:31 Okay, that would be great, yeah.
**Jonathan Halliday (IBM)** 25:33 I seem to remember having gone through this before, and it's more or less on request.
They might ask you to… to do some of the… the lifting of, … just normally you create a… a release notes with the… the changes.
But after that, it just takes someone in authority to push the release button, basically, so it's pretty much, you just pull them and say, please do a release.
**Florian Lehner** 25:55 Yeah, I will take care of this, figure this out, and we'll be fine.
Alright, we'll find out. Thanks.
**Frederic Branczyk** 26:08 For what it's worth, I think some people saw last week I integrated what, like, the most recent state is into Parka last week, and … I didn't find anything specific anymore that wasn't already reported, so… I think we're pretty close.
Other than this step representation.
**Felix Geisendörfer** 26:33 Okay, yeah, we have another separate agenda item for the stack representation, so we'll circle back to that in a second, but I think with regards to the… release candidate, or probably called Alpha, I think we're aligned, I think we want to do it. I think we want to ask about a 1.8 release. Florian is gonna take the action item of checking with Tigran on that, and giving him a heads up, and … Yeah, then basically, once we have that 1.8 release, where we call ourselves Alpha, where we want a blog post where we announce this to more people and basically get this show on the road.
… Then the next agenda item was from Josh, but I don't think he's here. It's about labels on profiles versus PROF versus resource attributes.
Does anybody know enough details to get into that, or should we wait for Josh to join us again next time?
**Florian Lehner** 27:30 I think that's, mostly based on my stuff.
And, … Yeah, with the extraction of the labels, we don't have a semantic convention yet to report them.
I joined the semantic conventions, SIP meeting, and the discussion was around, hey, do we want to report, context information of processes anyway? And there's no clear view at the very moment, and… They are trying to figure out How to continue, and, how to… handle this. At the moment, the eBPF profiler is using a custom label, so process.context.label, similar to how we report environment variables.
But this is just one suggestion that the SIG had. There is no agreement on this. Yeah, the problem with the SIG was also that, at the moment there's a, vacation time, I would say, for the Northern Hemisphere.
And, a lot of people that were, related to the topic are not, They're not attending, so, I will try to follow up with this again.
But yeah, I think everyone would benefit from it if labels could be communicated in a common understanding way. This is not the case at the moment.
**Felix Geisendörfer** 29:00 Sounds good. So it sounds like you'll… you'll follow up with a sick on this. Is there anything you need from the… the… basically the conventional sick. Is there anything you need from the profiling sick people?
**Florian Lehner** 29:14 I don't think so at the moment.
I don't think so. Semantic convention needs to get an understanding how they want to treat, contexts in their way.
And, … I think not only the profiling SIC, but also the EVPF SIC, or the EVPFIC, with OBI, so, OpenTelemetry for instrumentation with EVPF.
They maybe also have an interest in something like this, because they're doing very… the very same, just like we do, just for LOX metrics.
Traces, yeah.
**Felix Geisendörfer** 29:53 Gotcha.
Okay.
Then, I think I saw Nev's hand up.
**Nayef Ghattas** 30:01 Yeah, I just wanted to mention that… Regarding some of those labels, since Josh mentioned that some of them could be mapped to resource attribute, there's a slight overlap with the proposal we did on how the resource definitions done in the OpenTelemetry VPF profiler, because for a subset of those labels, like service name, service instance ID, Things that are generally, container tags, or things like that.
Might make more sense as resource attributes than as labels in the… in the sample, in the profile, to at least align with what the SDKs are doing, … And make it easier to, switch between profiles from the eBPF profiler and profiles from… that are emitted by the SDKs and other signals as well, so….
**Florian Lehner** 31:00 Yeah, I think it makes sense to special case some labels at some point, so, like, service name, to be one precise.
Yeah, and yeah, my concern is a little bit still that if there are too many resource attributes that we allow on the high level, then we kill the protocol. But, if we say, hey, we limit it to service name, for example, and container ID, then I think that's a reasonable approach.
But yeah, we should… we should… I just want to be careful.
**Felix Geisendörfer** 31:41 Okay?
Any other thoughts on this topic?
If not, then we got Jonathan's, simple repeated attribute indices.
**Jonathan Halliday (IBM)** 31:59 Yeah, so sample's a little bit confusing to use.
And I'm just wondering if we… we want to see if there's anything that can be done about that.
Right now we have, … This notion that some parts of sample really define the object, so things like the stack trace are part of its characteristics, and they're used when you're… Deduplicating the raw samples to pack into sample messages.
If you have multiple samples that have the same stack trace, you would hope that's one Sample object on the wire.
And, the timestamps, the repetition there is used to say, okay, we saw this particular sample, this particular stack trace.
At these particular timestamps, and that's fine.
And values, similarly, if you capture some value that's part of the the state, if you like, so if it's a malloc caller, for example, you might want to capture the number of bytes that's being allocated.
Then the stat trace would be the same, so it's still one sampled message object.
But it's got multiple values, because… on the first call, it allocated 4 kilobytes, on the next call, it allocated a megabyte, right? And that's all well and good. So the first point is the attributes, don't work that way. They're a repeated field.
But repeating something in there does not mean the first attribute in the repetition was seen in the first instance of this sample, and the second attribute was seen in the second instance of the sample. So it's not got the same semantics as values and timestamps.
And unless you're paying attention, that's… that's a little bit weird.
Really, what it's saying is that the attributes, the collection of attributes, Works the same way, … that the Stack Chase does. It's part of the… Value that's used as the key when you're deduplicating.
So all instances of the sample would have the same attributes.
**Christos Kalkanis** 34:07 Well, essentially, it doesn't say anything, right? So it leaves us unspecified. Yeah, yeah.
So, somebody could, because it's vague, could use it to be….
**Jonathan Halliday (IBM)** 34:14 Yeah, they could use it the other way. Right.
**Christos Kalkanis** 34:16 So, I think we should specify to make.
**Jonathan Halliday (IBM)** 34:18 But equally, values is a little bit odd in itself, then, because why is the value not just an attribute? If I want the number of bytes that was allocated, why am I not just sticking that in an attribute?
Is it because we think there's a huge use case where a lot of samples just have one value that's special?
And don't have attributes, or have attributes to the, sort of, lesser things.
That are less important than the values, so we want to treat value as a special case.
**Alexey A** 34:48 And also for the list of attributes.
I assume, and I would not be surprised if, even within this group, there are different opinions on this, I assume the order is not important.
Like, if… if I have….
**Jonathan Halliday (IBM)** 35:01 Because when you rehydrate those attributes, you're probably going to rehydrate them into a map, into a key value.
**Alexey A** 35:07 Right.
**Jonathan Halliday (IBM)** 35:08 Yeah.
**Alexey A** 35:12 unlike, for example, because I was thinking, oh, like, in general, attributes are closer to the stack representation than, for example, the values and timestamps, but for the stack, the order is important, and for attributes.
**Jonathan Halliday (IBM)** 35:23 Right, yeah. So I'm not super concerned that this one's on the critical path, because I think it can be addressed by documentation changes rather than by changes to the structure of the message.
But I just wanted to raise it in case someone's got some bright idea about, oh, let's… I don't know, let's… let's change attribute indices to work the same way stack does, so it goes through an extra level of indirection, which makes the semantics clearer.
I personally don't like that one, because I think it's inefficient. But if it's easier to implement, if it's clearer what the semantics are, maybe the inefficiency's worth it.
**Alexey A** 35:57 Another option is, … rename the field. For example, would having set in the field name help?
**Felix Geisendörfer** 36:10 Well, it depends on what we want this to behave like, right?
**Christos Kalkanis** 36:15 I think when we specified this, we thought this as per sample, for the sample as a whole, and not to have any more, like, no increased granularity to go into the… The different instances of the sample are representing these values.
Personally, I can't think of a case.
**Jonathan Halliday (IBM)** 36:32 What I might do is rearrange the order of the fields to group the ones that form the state of the sample, so the stack, the attribute indices, and the link index.
and value.
And then have… Sorry, no, not the value, the, the rep… the repeating elements, the value and the timestamp.
As a separate group, as the… The second, sort of set of fields.
And then we can just use some extra comments to say, you know, this set of fields forms the state that you're deduplicating on, and this set of fields is repeated For occurrences of that state.
**Christos Kalkanis** 37:15 Yeah, that makes sense to me. Also, values and timestamps should be grouped together, because essentially they use the same representation, now it's confusing.
**Jonathan Halliday (IBM)** 37:24 Yeah, so we shift values and timestamps to be the last two fields. Well, timestamps is already last. We shift values next to timestamps, and change the docs a bit.
**Felix Geisendörfer** 37:39 That sounds good to me, but I would say that the semantics of these fields in particular are very important, and… I don't think we can wave our hand and be like, oh, we're gonna fix it with docs later. I think if we put out, like, an alpha version where we specify the semantics of these fields, like, it needs to be clear, I think, once we hit alpha, I think it is on the critical path, as far as I'm concerned, even if it doesn't mean proto-changes, even if it just means common changes.
**Christos Kalkanis** 38:08 Oh yeah, I think we absolutely need to specify. It's too vague now, right? It's… yeah, you can't really… Use it.
**Jonathan Halliday (IBM)** 38:16 I think the overloading of values in particular, because in some of our examples, we're using it as the count of occurrences.
And in some way, using it as a value that was captured with each occurrence, and I think that's problematic.
**Alexey A** 38:32 Also, unfortunately, in this case, even with our profiler consistency check.
it's difficult to… it's difficult to check that someone is misusing this field. For example, if I'm putting if I would put the number of elements same as the number of timestamps and values to the Use that to kind of capture attribute per value.
**Jonathan Halliday (IBM)** 38:52 LU.
**Alexey A** 38:52 But it would still look… like, what… Well, maybe we can check for… I think each key should be unique, per sample, and I think if you… you would try to misuse it, you would probably repeat the key.
I assume, and we should probably document that as well, that, like, each key should appear only once.
Right?
In the… in the attribute list for the… for a given sample.
I wouldn't want to specify, like, label process ID multiple times.
**Jonathan Halliday (IBM)** 39:26 Yes, yeah, that's fair. I noticed that, actually, when I was, … pushing one update this morning, it said that in relation to the dictionary, and I thought, hang on, that's definitely wrong in relation to the dictionary, because the dictionary can contain multiple occurrences of the same key, as long as they have different values.
But yeah, I think for any given set of attributes, like the one in the sample, it has to hold true, yeah.
**Felix Geisendörfer** 39:52 Makes sense to me.
**Jonathan Halliday (IBM)** 39:54 Okay, well, I'll take a pass at the sample when I'm back. I've got a four-day weekend, I'll look at it on Tuesday, probably, and put up a PR suggesting some dox changes and reordering the fields.
And see if we can reach a point where… We can… we can have good enough documentation.
The only other field change I briefly considered was instead of having values, or rather in addition to having values, we could have an occurrence count.
Which then makes very clear the different semantic between Using value as a counter of how often that stack was seen.
Versus using it, as… A way to store some particularly important value that we don't want to just shove into attributes.
So, in the case, if you were capturing memory allocations. The value would be the amount of memory captured, whereas the occurrence account would be how often you'd seen that particular Value at that particular stack trace.
**Felix Geisendörfer** 40:58 Dude, that's interesting as well.
**Alexey A** 41:00 I… I didn't get that one. Could you….
**Jonathan Halliday (IBM)** 41:03 This is confusing, because if we see the same stack trace 10 times.
We might have a sample that contains that stack trace.
And a single value of 10.
And that… we're using value as a current count.
Right? That's the semantic of value.
**Alexey A** 41:23 Right, it's like sample count in this case.
**Jonathan Halliday (IBM)** 41:25 Yes, yeah, occurrence count, sample count, yeah.
But, value might be some piece of metadata we captured as part of the sample.
So if the sample is… a malloc call, it might be the amount of memory that was captured.
So there, it might be 10 again, but now it doesn't mean this happened 10 times, it means it happened once, and it allocated 10 bytes of memory.
And right now, we can't… Disambiguate that very easily.
**Alexey A** 41:57 I assume right now you would have to have a separate profile for that, because, like, we have essentially, like, one sample type per profile.
So you would… you would have… you would have one profile that represents the… found in, you know….
**Jonathan Halliday (IBM)** 42:10 Yes, the type would have to contain sufficient semantics for the interpretation of the value.
So one type might say, this is a memory capture in which the value means the amount of memory, and another might say, this is a memory capture in which we don't record how much memory was captured, we just record how many occurrences of memory allocation happened.
And those would be different types.
**Alexey A** 42:35 Is semantics different important? Because… so, for the values, like, for any… any profile, I assume that the values are cumulative values. Is this kind of like cumulative?
**Jonathan Halliday (IBM)** 42:47 Well, that's the whole aggregation temporality thing that we haven't got to yet, isn't it?
**Alexey A** 42:53 Yeah, I was just curious, like, do you mean the difference, like, gauge metrics, like, instant values versus cumulative values, or, or something else?
**Jonathan Halliday (IBM)** 43:03 I'm not even worried about that.
It's… it's count of how often something occurred versus… What was it occurred?
**Felix Geisendörfer** 43:12 Yeah. If I remember correctly, in PProf, for Go Memory Profiles, this is solved using labels, right? Like, the value field is used to denote the count of occurrences, and the label tells you how big the allocation size was.
**Alexey A** 43:26 No, it's two separate sample types. There's one, I think one is called, like, space, and another is called allocations, or something like that, so one of them captures how many allocations we had, like… I think those are two separate sample types. Labels are used to capture the size of the allocation.
**Felix Geisendörfer** 43:45 That's what I was trying to say, maybe clumsily.
**Alexey A** 43:47 Oh, oh, okay.
**Christos Kalkanis** 43:49 We actually have this in the proto as a comment. Like, if you look at the profile methods, we have allocated objects with counts, and then allocated space with bytes.
So that kind of points that you need to use two different profiles, that's what you're trying to do.
**Alexey A** 44:06 Yes, that's… That's my assumption as well. And… Yeah, labels should only be used for categorical values. Basically, I… That's another subject, but I also wonder if we… Should document this better, because I don't want to diverge. I'll stop here. I can add this as a separate discussion topic.
**Felix Geisendörfer** 44:32 Yeah, I, I think, … Jonathan, if you want to play around with what, like, an occurrence count field would look like, and place a separate PR for that, I would be happy to look at it and think through it.
… But I think, yeah, if we could figure out how to make the current fields work and define the semantics for them, clearly that would be the smaller change here.
**Jonathan Halliday (IBM)** 44:57 Okay, I'll take a look at that next week.
**Felix Geisendörfer** 45:00 Wait, do you want me to add a to-do on top of this list, or will you add one on yourself?
**Jonathan Halliday (IBM)** 45:10 Yeah, that's probably a good idea, thanks.
**Felix Geisendörfer** 45:15 Okay, thanks for adding it.
**Alexey A** 45:17 Can I… can I inject a quick question?
Because it's related to the release discussion. I wonder if, the profile consistency check tool that I'm working on, do we want to tie it to the alpha release?
Like, would we want to have such tool ready?
when we do the blog post, for example, and tell people, hey, if you try this format, also use… I was just, like, I got on this train of thought when we started discussing that, like, maybe documentation is not enough, but maybe if we start getting more people using the profile format, and we can give them a tool.
And the tool complains, and they complain to us, this might help raise useful discussions early.
**Felix Geisendörfer** 46:00 I… I would say that, to some degree, the consistency tool… check tool is… It could go either way, but I think it's not on the critical path, because in a way, it's kind of the first test on how tight our spec is. Like, you are looking through the spec, Alexi, as a consumer yourself, and you're trying to figure out how can I write a tool that actually enforces these semantics. So in some ways, you need the alpha first to build the tool on top of it. We could still, like.
give you time, like, to release it at the same time, but I… and… or basically delay the blog post about it, but I think in theory, we need to get the protocol to a good stage first, and then you can build the tool, or finish the tool.
**Alexey A** 46:39 Okay.
**Felix Geisendörfer** 46:42 Florian?
**Alexey A** 46:43 I think, I think that….
**Florian Lehner** 46:44 … I think when… once the 1.8 release is out there, we first will break a lot of stuff in the collector and collector contract. And, once this is done, I think people can already play with it, already use it in their environments.
and already push in data, push out data. The… receiver that Antoine mentioned is just one part in this whole chain that we will break with the release of 1.8. So there will be a lot of work happening with this release.
But if you want to have a tool that is separate from Autel, let's, just say, hey, this is a protocol outside of the scope of the Ultra ecosystem, then, yeah, Alex's work is incredibly important, I think, before making any big announcements.
**Jonathan Halliday (IBM)** 47:49 I wonder if we can… we can tag something which, sort of, internally, we… we… can tell people it's alpha, like the… the collector team and the SDK teams.
… And then we make the big announcements, and we're around KubeCon in November.
By which time, hopefully, we have some implementations, so that people can actually kick the tires.
So there's a distinction between saying, this is now stable enough for the people who are going to implement it to implement it.
Versus saying this is now stable enough for people who are not implementing it to download an early cut and try kicking the tires.
**Felix Geisendörfer** 48:29 To me, that makes sense. Kubecon is obviously attempting time to announce stuff, but if we could get it done before, then maybe as well, but… But yeah, I'm not opposed to this. I think, basically, as a group, we just want to get to, like, a stopping point where we're, like, saying, let's… let's make sure that no more big changes are coming. I mean, maybe we will discover something, but at least it should not be something we already know about. Then give people who, like, work on the collector and all those things a chance to update, and then if we're happy with how that turned out, then yeah, announcing it to a larger group, maybe KubeCon is gonna be the time where there's good work.
**Alexey A** 49:12 I'll be glad when we get to this meeting, and we, like.
Well, there's nothing to talk about.
**Felix Geisendörfer** 49:20 It will happen.
**Alexey A** 49:23 Yeah, sometimes it also happens as a cliff. Like, you have lots of things, and then suddenly you have none.
Yeah.
**Felix Geisendörfer** 49:32 No, but I think we're very close. … So I think we have a rough plan here. I… Any other thoughts on this train of thought, or should we go to the stack tracing and quickly just get the next steps there settled?
Okay, no answer means we'll go ahead. Yeah, so basically on the stack tracing, yeah, I think on the poll request we've got enough, approvals. I need to resolve some of the open threats. One of them is the ASCII, comments.
I was not sure from Christus, were you saying you would… or somebody else was willing to send a PR to change the comments against mine that I could just merge, or should I try to do it?
**Christos Kalkanis** 50:21 Sorry, it's up to you, it's not a problem for me or Jonathan, I think, to do it, because if you're… shrunk, or anything. I can predict tomorrow, then… The important thing is to merge this. I think we can merge it tomorrow, or early next week.
**Felix Geisendörfer** 50:36 Yeah, I think if I just have to click buttons, I can definitely do it before the end of the week, but I'm… super behind on my presentation, so if it's more complicated, then I'd ask for help this time around, but I… promise to contribute more going forward. So, yeah, Christoph, will you take the action item, or…?
**Christos Kalkanis** 50:55 Yeah, sure. So, hopefully, yeah, I'll have it done by tomorrow.
**Felix Geisendörfer** 51:00 Okay, and then let's try to get the PR then merged tomorrow, or at least in a mergeable state. I think we are actually now… a bunch of us have become spec approvers, if I saw that correctly.
So… I suppose what that means is if… two or more of us are in agreement on something, we don't need to ping Tikuan and Josh.
**Josh Suereth** 51:23 Sort of.
That's me too.
**Felix Geisendörfer** 51:26 Oh, no.
**Josh Suereth** 51:27 You have to ping us to click the merge button, still. But we don't need… like, you guys approve on your own, and you don't need general approvers.
Sorry, I was eating lunch, I can turn my camera on.
Yeah. So you, … the way Approver and maintainer works in OpenTelemetry, approver, those are the green checkmarks that matter, so once enough of those are there, we can actually click merge. And the idea is that, you… the maintainer doesn't have to do… deep investigation of a PR if there's enough green check marks. Sometimes in practice, That doesn't happen.
So let us know if you have high friction, but theoretically, it means when you guys are green checking things, we can merge it through quicker.
**Felix Geisendörfer** 52:12 Okay, yeah.
That's great, and yeah, sorry for misunderstanding, but that makes sense to me, and I think that's already super helpful with getting stuff in.
**Josh Suereth** 52:23 Yeah, the other thing I'll say, we're trying to expand the maintainership of some of these things as well, and try to figure out what that means, but being a maintainer means you need to care about all of the things, not just the profile. So, if any of you are interested in that, that would be awesome too.
You'd have to be able to review, like, the whole scope of the, like, specification or the protocol, right?
**Felix Geisendörfer** 52:52 Yeah, I think, while we're still wrapping up the signal, I think most of us have probably enough backlog, but I could imagine that once we are sort of, like, at a point there where we get to the meeting and we don't know what to do, we would be happy to help with other stuff as well.
**Josh Suereth** 53:07 Yeah, the other thing to think about there is, at some point, Folding back into the specification.
group overall, so the Tuesday meeting where we have all maintainers and specification folks together to kind of talk through general issues, that's supposed to be the ongoing maintenance meeting, right? So, if you get to the point where nothing's happened in this meeting, and you're really looking for more meetings.
No, sorry. And you want to kill this meeting because you want to, like, use your time wiser. You can start using that meeting and check the agenda before, like, before the meeting, if there's something profiling related, come. If not, skip, that sort of thing.
**Felix Geisendörfer** 53:45 Yeah, makes sense.
Cool. Anything else on this? If not, we could… move forward, Florian has nightly builds Of hotel collector's profiling takedaway.
**Florian Lehner** 54:03 Yeah, we did get, I would say a little present from the auto-collector release people.
And, they now have, our profiling in the auto-collector pipeline. So they generate now, nightly release. There's no, fixed tag on it, so it's not, official, it's not a big announcement, but… I'm trust… wanted to share the news that, there is, WCI pipeline that is generating profiles. Be aware, still, protocol version 1.7, so it doesn't work with the most recent ones, so it uses the one of, profiling that is, coming with the OTA connector.
Yeah, but, I think that's, great, in the sense that, once 1.8 is out, we can directly communicate, hey, you can try it out directly, and that's… that's awesome, yeah. Just wanted to share….
**Felix Geisendörfer** 55:02 Very nice, thanks.
And then we have, last but not least, Alexi clarified that labels should be only used for categorical values.
**Alexey A** 55:21 Yeah, I… at least in… in profile product… in profile photo experience, sometimes people would try to use labels to capture… Like, actual numerical cumulative values, for example, and labels should only be used for categorical values. I wonder if we want to clarify that in the docs.
**Felix Geisendörfer** 55:43 ….
**Alexey A** 55:47 Or maybe we want to be flexible, it's just… I think… if… I don't know.
**Felix Geisendörfer** 55:54 I think as a suggestion and best practice, we can definitely add a comment there, like, let's say it should, but I think it should be a weak recommendation, like, it shouldn't be a must or something, because I mean, our main concern here is cardinality, right? Like, which you would expect to be pretty high if you use numeric values, but there are… categorical values that can also have really high cardinality, let's say user ID or something, right? And we certainly want to allow people to put those on the labels if they feel that they add value, right? So, yeah, I would be okay with a should, like, just as a best practice and guidance, like, to aim for lower cardinality, but, like, maybe not make it a very strongly worded.
**Alexey A** 56:37 Maybe we should make, … Kind of, like, consequences clear.
that… Cardinality of attributes matters.
So, don't put… Randomly unique values in attributes.
Like, if you start putting double value that represents the current The current memory usage, for example.
And you don't bucket it in any way.
Then, don't get surprised if… Profile size blows up.
Something like that, maybe.
**Felix Geisendörfer** 57:16 Yeah, I think, like, something of, like, be mindful of the impact of high cardinality labels on profile sizes, or something like this could maybe be enough to give people some We mostly want people to think about before they add stuff to this, right? And different people can come to different conclusions, but we want little warnings here. So yeah, I'd be plus one on adding a little comment on that.
**Alexey A** 57:41 I can add that.
**Felix Geisendörfer** 57:43 Cool Okay, unless anybody had a last-minute idea for an agenda item, we have managed our time well today.
And everybody can get back 2 minutes of their schedule.
Okay? Doing once, doing twice… No?
**Josh Suereth** 58:13 Sorry, this is just… this is an FYI for agenda items. If you need anything from me going forward in this meeting, or you want to have a discussion I participate in, I have a now permanent conflict from 11 to 11.30.
So I can attend the last 30 minutes, and try to address as much as possible then, but unfortunately, I can't make the, first 30 minutes. I'm trying to coordinate with Tigrin to make sure that, like.
We ping pong, if we have to. But if you need stuff from us, just know that I will be here.
It will just be the last 30 minutes. So, apologies.
**Felix Geisendörfer** 58:45 Yeah, thanks, and I think that works for us. I think when we have questions during the meeting and we don't see you, then we'll remember them by the time you join, so that works.
**Josh Suereth** 58:54 Okay. Awesome, thanks.
**Felix Geisendörfer** 58:56 Cool, then everybody have a nice local time, and see you in two weeks.
**Frederic Branczyk** 59:01 See y'all.
**Florian Lehner** 59:02 2….
