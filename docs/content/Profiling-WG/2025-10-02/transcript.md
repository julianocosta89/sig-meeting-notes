SIG: Profiling WG
Date: 2025-10-02
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

Frederic Branczyk 00:00:22 Hello, hello.
Florian Lehner 00:00:28 Hello.
Ivo Anjo 00:00:32 Hello.
Felix Geisendörfer 00:03:44 I guess we're 5 minutes in, so let's kick it off. Anybody feel like moderating other than me?
Going once, going twice…
All right, and hello and welcome, everybody, to our Profiling Sig meeting. I will run us through it, and as usual, I think we will start with reviewing
Active action items. Let me just prepare my screen for recording.
Play my screen…
And… yes, so we have…
Two items from Alexi, but I don't know if he's here, did I see him or not?
Alexey A 00:04:40 Yeah, I'm here.
Felix Geisendörfer 00:04:41 You're here. Okay, then we can jump into the ease.
Alexey A 00:04:44 Yeah, yeah, made some more progress on the checker, haven't sent the PR yet, but,
Slowly but surely.
Getting there.
Yeah, these two weeks I didn't have a lot of time to work on it, but.
Felix Geisendörfer 00:05:10 And the next one is, the P-Profo converter, there's a DR here.
Alexey A 00:05:15 Yeah, the converter, I saw Florin sent a pull request. I made a couple comments, but I will review it more.
Florian Lehner 00:05:29 Yeah, as Anthony is in the call, I would appreciate his feedback.
I also paint him in the PR, but I think…
Maybe it got lost in the… Somewhere.
Alexey A 00:05:44 Florian, do you plan to implement also reverse conversion so that we can round trip?
Check.
Florian Lehner 00:05:50 It would be nice to…
Alexey A 00:05:52 good.
Florian Lehner 00:05:52 It makes sense.
Alexey A 00:05:53 It would be nice to convert, and then…
See if the diff is equivalent.
Florian Lehner 00:05:59 Yeah, from the… from the…
Auto perspective, the complementary part, I think, should land in export or something.
export a P-Prof, maybe?
But yeah, did not start on this part yet.
Alexey A 00:06:22 What do you mean by next proto?
Or maybe I misunderstood, sorry.
Florian Lehner 00:06:30 Sorry, the second part of this for the full conversion between that we can do a cycle, pre-prof, hotel, hotel, pre-prof.
The second part maybe should land in, export, PPROF.
Yeah, but I'm not sure, I'm not an expert on this, but I also didn't work on this yet. I wanted to have a first step in PPROF2OTEL, and then we can still continue.
Alexey A 00:07:03 Sounds good. Thank you.
Felix Geisendörfer 00:07:05 Yeah, I think Antoine is here, right?
Want some immediate feedback?
Hey.
Antoine Toulme 00:07:12 No, I didn't get a chance to review.
Felix Geisendörfer 00:07:14 Okay, no worries.
But… And that's next step.
Okay, so next step is basically we'll keep the action item for it open, and next step is to review this and give some feedback. And I think it makes sense to do the receiver side first, and then the OTLP to pre-proof, we can…
do as a separate thing. Cool, awesome things. Thank you, Florian, for raising this and working on this.
Then, let's see, what's next under active action items? The context propagation documents, can somebody give me a heads up if we have an agenda item for that? I suspect we might do.
Neff, did you… do you want to go over the general thing, or…
Nayef Ghattas 00:07:58 I don't think I have an update for the folks document resource definitions, but I don't know if Evo
Was there any updates, Joshua?
Ivo Anjo 00:08:07 Yeah, I've replied to most of the feedback, I believe, but, beyond that and the proof of concept, I don't yet… yeah, I'm actually kind of…
I, haven't been able to do one big thing, which is chat to folks in the hotel tracers about this, but, which I think is, like, one of the big next things, but other than that, so open to feedback, and, yeah.
But I think that's the current state.
Felix Geisendörfer 00:08:39 Next step is more feedback, or…
Ivo Anjo 00:08:42 I guess from this group, more feedback, and for me to go and talk to the Hotel Tracer folks to see if they have feedback on this as well, so that we can kind of start pairing both sides, the reader and the writer.
Felix Geisendörfer 00:08:55 The OTL SDK6, yeah.
Ivo Anjo 00:08:58 Yep.
Felix Geisendörfer 00:09:00 Okay, cool. Unless somebody else wants to chime in here, we can move on to the next action item. Owner wanted,
Yeah, has anybody… Decided they want to own this.
This is still pending for now, we can circle back to that. Shaunessen PR for, field order and sample group keys together are 714, that's probably waiting on review now.
Yep, so Alex has already reviewed Christos as comments, on these…
mostly resolved, or I definitely need to take a look here.
Jonathan Halliday (IBM) 00:09:46 So there's two aspects to that PR. One is, grouping the fields that form the key together, which is a breaking change.
And the other one is the, documentation, the comments.
And it's the comments that are…
Seemingly controversial, because that's getting into…
How can we detect if a single non-timestamped value is an aggregate or not?
Felix Geisendörfer 00:10:10 Isn't it the same as the previous action item here? Document the values times? Oh, okay, cool, then we, I guess…
And you have become the owner, whether you wanted to or not.
Jonathan Halliday (IBM) 00:10:20 Yeah, I mean, I can roll that into the same PR. It's also a documentation change to the same message.
Felix Geisendörfer 00:10:27 Well… okay.
Jonathan Halliday (IBM) 00:10:30 It's a bit of scope creep, but…
Felix Geisendörfer 00:10:32 Yeah, yeah, wouldn't it make sense for your PR to, like, cut it down to the initial scope of, like, grouping the keys together, which seems we have alignment on and could land without much discussion, or…
Jonathan Halliday (IBM) 00:10:45 Yeah, we can go either way, I can… Back out the…
Change the dot comments, we'll just defer that and say we haven't figured it out yet, but we'll get the… change the message structure in.
Felix Geisendörfer 00:10:58 I would slightly lean towards that, I see thumbs up from Alexi.
Jonathan Halliday (IBM) 00:11:01 Yeah, okay, I'll do that.
Alexey A 00:11:03 Yeah, especially given that it's a breaking change, because it changed.
Jonathan Halliday (IBM) 00:11:07 It changes field IDs, I think, just getting… Yeah, it makes sense to get it done sooner rather than later.
Felix Geisendörfer 00:11:30 Yeah, so you'll… you'll push that forward, thank you, and then, I will just make a note here that this is, the same thing. I will…
overlap, maybe I'll make a…
a note up here, even so that PR might become different scope, I'll just link it to this item here.
You overlap this 714.
And yeah, then we can raise a new one that replaces 714 that just has the comments that we need to align on, on how the semantics should work, and we can…
do that separately. Depending on how much, like, discussion there is that we want to retain, you could also go the other way around and keep 714 on the comments and remove the key changes and raise a new one for that, if most of the comments were about the comments in the
Rodo, so I'll leave that to you, Jonathan, but, just food for thought.
Okay, anything else on that? If not, we can go to this one. Yep.
Nope, then next action item… Alexi.
Alexey A 00:12:48 Yeah, I'll, I will… I will send this soon. I… I forgot about this action item, I saw it 20 minutes before… before the meeting, and I… I almost have the PR ready, I will send it soon.
Felix Geisendörfer 00:13:00 Okay, no worries.
No worries. And then we have Florian.
at payload format.
Another declaration.
Florian Lehner 00:13:12 Yeah, this is… From working on the… P-Trov to hotel conversion.
I noticed that we… We usually have the lookup tables in the dictionary.
Except for, message…
Alexey A 00:13:37 I think this is related to the previous bullet, actually. I think it's from the, I'm looking at the payload.
Florian Lehner 00:13:45 Oh, sorry, sorry, sorry, sorry, Mr. Mike, for that.
Alexey A 00:13:47 Yeah, I…
Yeah, I think it's the same thing, it's just we split, we said, you will send the PR for semantical.
Florian Lehner 00:13:55 specifications.
Alexey A 00:13:56 I mean, for the convention, because you've… you… you did similar PRs before, and it's probably easier for you to just make the change.
Florian Lehner 00:14:05 Yeah, my fault, I mixed, things up, didn't, didn't count to this, didn't come to this yet.
Yeah, but, I spoke on…
I think it was Monday or Tuesday this week to the communication sick.
And, yeah, they are very welcome, with more input on the specification and semantic convention sites profiling, especially as we are moving on to, development and alpha.
And, people should get more, should get more…
documents around this, how things work, how things are structured, and so on. So, yeah, but, I, I didn't, didn't manage to do this yet, sorry.
Felix Geisendörfer 00:14:53 Okay, so what's the next step, Sarah, just to be specific?
Florian Lehner 00:14:56 I need to write them.
Felix Geisendörfer 00:14:59 To reach out to them. Okay, cool. This is, like, your thought to yourself around lookup tables? Should I lead this? Was that relevant, or…
You're muted.
Sorry, I have a dedicated agenda item for this later on, sorry. Okay, okay. I'm sorry. No worries. Cool. And then Christos has completed the to-do of open…
hotel profiling documentation issue is opened. We now have 7874, which is tracking the,
addition of documentation for profiling. I don't know if you want to say anything about this, Christos, if you have to feel free… is Christos your email?
Florian Lehner 00:15:46 Christos is on PTO, and that's why I joined the SIG meeting, and yeah, they are welcome.
Getting us landed there.
Felix Geisendörfer 00:15:56 Okay.
That's awesome. I'll tell him thank you when he comes back.
And I'll just put it into the list here.
And with all of this out of the way… sorry, let me just box this.
With this out of the way, we can get to the regular agenda items, and I suppose, Florian, you will cover Krista's items today, so take it away if you want to. If not, we can skip them.
Florian Lehner 00:16:29 I cannot speak that much, I just know that there are…
There are, some security reports that the maintainers have to deal with.
Felix Geisendörfer 00:16:38 Hmm.
Florian Lehner 00:16:40 But I don't know any detail, any more details about this.
Felix Geisendörfer 00:16:45 I, I do know.
Florian Lehner 00:16:46 resolve it.
Felix Geisendörfer 00:16:47 about those.
Let me just read what Christos was writing, discuss coming up with service premise, documenting as part of the project.
Policies here…
Yeah, so I think what I can say is that the vulnerabilities that were reported were
I think in both cases, denial of service, where you could do some stuff that would just stop the VPF profiler from working. I think in one case, it was getting hung up in an infinite loop, in another place, it was just…
stopped on a syscall or something. They were…
maybe a little obscure, like, it basically just assumes you're running very untrusted code that, is, trying to… to tax a profiler, which I would guess most people would who deploy OpenTelemetry observability just run code in their environments that they trust.
To not be malicious towards the profiler. But yeah, we basically need a sort of policy on what is, sort of, the goal for security for the project.
Which sort of attacks we consider to be,
yeah, reasonable, as far as, like, the design of the profile is concerned to… to address, and which ones we're just saying, like, yeah, for example, very specifically.
saying, like, hey, running completely untrusted code, we guarantee that this is not going to break out of the profiler and give you… give somebody root, but we're not going to guarantee that you can't DDoS the profiler and basically disable it.
By doing something crazy. I think I should probably, since this is recorded, shouldn't disclose the details of how these attacks worked, but, they basically allowed that, and they didn't allow, like, the privilege escalation. So I think…
we need to agree as a group on, what security guarantees we would want to give, and I think there was an initial discussions alignment around
Yeah, DDoS… Protection for use cases of multi-tenant
environments with untrusted code is probably not something that's feasible, but privilege escalation protection probably is feasible. I don't know, Florian, you probably have thoughts just as I'm saying this, but…
Florian Lehner 00:19:05 I have no idea what was recorded or in the editor, so… I cannot speak about anything.
Felix Geisendörfer 00:19:13 Okay, yeah, I think I can…
Alexey A 00:19:16 Is this about the OIS on the backend, or…
Felix Geisendörfer 00:19:21 No, on the profiler itself. So basically, you run a program on a host that also runs the eBPF profiler, and then through some magic things that that program does, you would basically stop the profiler from working. No other impact, it's basically just either idle loops in, like, a for loop, maybe it burns up one to CPU, one CPU in that.
But basically, it just stops sending profiling data, it stops doing the thing it's supposed to do, but it's not giving the attacker any…
potential path towards further escalation or doing something else with it. That's the current state.
And I think at least one of these, attacks was very obscure in the sense that also, like.
It seems like there was no mitigation even available, because it assumes that the attacker has a workload on the host and has already elevated privileges in that case, so this was a workload where the attacker actually has
more than normal privileges to do something on the system, and, like, at some point, there's nothing you can do. If, like, some other workload has root on the system, they can do whatever you want. I think it was not quite rude, but it was, like, an elevated privilege, related to…
file system access, or mounting things, and, yeah, I, I think that…
basically, we… we just have to, at some point, formulate this. I think we can't have an intelligent discussion, I think, without the details, which I don't know if I should disclose here, but I think I can ask Florian to… for you to be added to these discussions.
I don't know, I think I saw Frederick here from Polar Signals, you all maybe have also an interest in these discussions, or maybe thoughts on what security guarantees you want to provide as a commercial offering. Maybe you can speak for a second what you have seen, or…
Frederic Branczyk 00:21:05 We also have a definition for the parka project, so, you know.
It's helpful for us to reconcile both of those.
Felix Geisendörfer 00:21:16 Yeah, what is that definition? Do you want to share a little bit?
Frederic Branczyk 00:21:20 I don't know off the top of my head, I would have to check it as well, but it's documented in our,
In our open source,
documentation. I think it's, like, if… I should just check it, I don't remember the exact details.
Felix Geisendörfer 00:21:38 Okay.
Yeah, I think the next step here is, to get interested parties like you, Frederick, and Florian, to be part of these…
reports that have been filed, I think that should be doable. I'll just have to check who can make this happen, and then we can take it from there, but…
to me, none of them look like there would be actual issues for the way most people would want to use this profiler, or expose anybody. So I think we're good, but we at some point need to just write that down, what the expectations are, so we can systematically deal with some potentially similar reports in the future.
So I'll take that as an action item. Let me take that.
Frederic Branczyk 00:22:34 Like, we had a case, this was years ago, but we had a case where… I want to say it was possible to cause, like, a…
a kernel deadlock or something. I think that's, you know, a reasonable vulnerability.
Yeah.
Felix Geisendörfer 00:22:59 Yeah, deadlocking the kernel might be… I mean, basically, with all of these, if there's, like, a small effort involved in mitigating and protecting against it, obviously we should probably always consider doing that.
Frederic Branczyk 00:23:09 Yeah.
Felix Geisendörfer 00:23:10 But in some cases, like, when it's clear that there's nothing we can do, because,
the operating system and the profiler interact in ways where it's just not feasible, then at some point we have to say, like, hey, this is a thing for trusted workloads. And be clear, because it's also useful for our users. It's useful for our response, but also for the users who want to deploy that.
to know whether or not this profiler is suitable in a multi-tenant environment with untrusted workloads. That's going to be an important thing to clarify. And I mean, they can still deploy it and use it, just know that maybe some very bad customer who doesn't like you comes and stops your profiler.
Frederic Branczyk 00:23:45 Yeah.
Yeah, agreed.
Florian Lehner 00:23:47 maybe some… some history. There was actually a bug, some music back in the Linux kernel, that caused,
kernel freezes.
If you call BPF probe.
And I was able to manage this with the help of UI and Mita, and this was also backported to the other LTS kernels.
Frederic Branczyk 00:24:13 Yeah, I remember seeing your involvement in the patches.
Felix Geisendörfer 00:24:19 What was the issue again? We had an issue with…
Florian Lehner 00:24:22 There was a bug in the Linux kernel, that if you use BPF, BP probe read, so reading memory on… in the.
in ePPF space from user, for example.
That the file system can, run into a deadlock.
And, this was a bug that was, happening in the Linux account, so…
Even if you are on the…
On the application side, you cannot mitigate this.
And, yeah, with the help of UOI and Meta, this was fixed.
Felix Geisendörfer 00:25:00 Yeah, I think this is, like, the box that we've seen would also be in a similar camp where, like, the kernel would have to change for us to be able to mitigate them, potentially, and we can certainly file things like that, but yeah, I think it's not a guarantee we can give others a box for now. Alexei, I see your hand up.
Alexey A 00:25:17 Yeah, I was curious if this is different from, like, a program being able to affect any other system components, for example, Kubelet, which runs on the host as well, or other BPF programs that…
Like, it's not like there are zero BPF programs on a modern host.
I think.
Felix Geisendörfer 00:25:39 I don't think it's… I think it's the same class of issues. Like, if one program is able to interact with another program in unexpected ways, especially, like, with low capabilities, then yeah, it's the same class of issue, I think.
Okay,
I think, yeah, I'll take the next steps as discussed, and then we can move on to the next action item, unless somebody has something here.
Going once, twice, three times? Okay. Does somebody have context on this one from Christos?
Alexey A 00:26:25 I think it would… I think… I think it's the PR that we discussed, and we decided to split it.
Felix Geisendörfer 00:26:29 the same one.
Alexey A 00:26:30 in, in, in.
Jonathan Halliday (IBM) 00:26:30 Yeah, since we're going to split the protocol change and the change in the comments, let's just defer discussion on this one until Christos is back next time.
Felix Geisendörfer 00:26:42 Okay.
Cool.
Then, next one is… Naif, is the lack of schema URL for the instrumentation scope attributes expected.
Nayef Ghattas 00:27:06 Yes.
So… The answer is yes.
Nope.
No, so, currently, in the portal, there are two schema URL fields.
One that is specified at the… Resource profile level…
And, the comment says that this, schema URL applies to…
semantic conventions for resource attributes. So, schema URL is… my understanding is that it's a way to specify the version of the semantic convention that is used
For, specific attributes.
And there's a comment on… there's another field on scope profiles.
For a schema URL that applies, for all the profiles under the scope profiles.
But there is no, schema URL that applies for scope attributes.
And I noticed that was also the case for the other signals.
So, I was curious to know if that is something that is expected, if this is something that we want to fix, before the 1.0?
Yeah, I'm not sure if anyone has any context on this. If not, we can also park the item, and I don't know if Josh is going to join us in the second part of the meeting.
Felix Geisendörfer 00:28:40 Yeah, I think it's probably one to, defer until we get time from Josh, or if we don't get some… somebody knowledgeable here today. I mean, somebody speak up if you have context, but I… I think we need some, general, spec approval or knowledgeable people to answer the question on why the…
Other signals have historically not done this for scope attributes, the schema URL thing.
Alexey A 00:29:26 And the idea is that schema URL would be a field
Inside of instrumentation scope message, correct?
like, if… If it would be there.
Nayef Ghattas 00:29:42 I think that is…
Inside the… yeah, I'm… I'm not sure. Or we could update the comment on the instrumentation scope.
that schema URL to say that it applies both on the attributes and the… And the underlying profiles.
Felix Geisendörfer 00:30:15 Yeah, I mean, we can quickly open it up, just so everybody has seen at least once what you've been talking about.
So you said there's two schema URLs, so there's one under resource profiles and one under scope profiles.
And the issue is that…
Alexey A 00:30:34 instrumentations.
instrumentation scope is a message, and it has attributes inside itself, I think, so I think the…
I assume the question is, like, what schema, what's… right.
Nayef Ghattas 00:30:48 Yep.
Felix Geisendörfer 00:30:50 Yeah, and so one way to… would be just to change this comment here, right?
Nayef Ghattas 00:30:56 Yes, to say, like, it applies to all profiles in the profile field, as well as the instrumentation scope.
Felix Geisendörfer 00:31:03 Yeah.
Alexey A 00:31:05 But it should probably be consistent between all signals, so Josh's feedback would be good.
Felix Geisendörfer 00:31:11 I mean, also, one way to push that forward would be to raise PR on the protorepo that makes that change for the other signals, and just force a discussion that way. That could be maybe a step forward.
Nayef Ghattas 00:31:26 Yeah, sounds good. If we don't have Josh, I can follow up on that. Maybe send a small message on the SIG Slack, and if I get no answer, always appeal.
Felix Geisendörfer 00:31:49 Yeah, I mean, you can try to ping him on Slack if he doesn't show up here later today, and then if not, you can
Look into that, that'd be awesome, thank you.
Okay, any more thoughts on this? Going once, going twice…
No? Then I think we are ready for Lexi's zero-index values discussion.
Alexey A 00:32:10 This was, there were some comments on this. The pull request itself is submitted, but there were comments about… so currently, we require that dictionary tables are always non-empty. For example, even if you don't have links.
that there should still be the zero value, and there were questions like, oh, did we consider allowing them to be empty? And the explanation I gave that, well, we wanted
indices to dictionary to always be valid. So, because if… if you have somewhere, if you have, like, a link
Index field somewhere.
in… per proto-conventions, the default value is zero. So, if you have,
If you have empty dictionary, then technically it's invalid index, because it, like, there is no in empty link table, there is no element with index 0.
But the comments were from people, like, oh, but maybe this could be special-cased, and
Yeah, and then… So, I just wanted to bring this, like, I think what we have… now is…
self-consistent.
I don't think change… any change needed, but I was curious if anyone has any thoughts. One thing I did notice, for example, is when I… when I'm writing unit tests for my schema conformance checker.
code. I need to kind of, like, in the test cases, I need to declare this, like, one element dictionaries
Even though they're… it's kind of like… it's getting a bit more verbose, but it's not a big deal, so I honestly don't think any change is needed, but I was curious if anyone has an opinion, like, an opinion that is stronger than mine.
Felix Geisendörfer 00:34:07 I mean, I think we had several discussions around this and aligned on the.
Alexey A 00:34:11 Yes.
Felix Geisendörfer 00:34:12 And so, my only comment would be thanks for defending it to the reviewers and getting it through. And I don't see any compelling reason for revisiting this, especially since you got the change landed.
Alexey A 00:34:24 Okay.
Felix Geisendörfer 00:34:35 yeah, if anybody else disagrees, let me know, but I saw some people nodding, so I think, you know, Lauren sums up,
So I think we can just leave this where it is. And…
That would take us to the next one. Also, Lexi, dictionaries, any objections to adding a comment about value identity semantics?
Alexey A 00:34:56 Yeah, this is… this might be cryptic. So we…
We discussed in the past, like, do we want to have a check that, like, for example, when we, when we check, when we check the schema, that values in the dictionaries are…
transitively unique for example, if I have, let's say, like, I have code location, like, the location table.
In general, there is no good reason to have duplication.
We said in the past, like, it's not a must, but it should, and maybe in the checker it can be a warning.
I wonder if we want to add a comment about this, because I don't think we currently document this.
Felix Geisendörfer 00:35:42 I would be… yes, we should…
document our intent. Our intent is that
we would prefer for implementations to not put duplicate stuff in the dictionaries, because it kind of defeats the point, but it's not a strict rule. If a implementation wants to go out of its way to be inefficient, or actually has good reasons for being inefficient at the time of data production, then so be it. So yeah, I would say plus one to adding a comment.
Alexey A 00:36:07 One thing is, I would like to add… and I can… I can add documenta… like, update the documentation, but I would like to make a stronger statement about…
the… like, use it… I don't want people to use
Values that are logically duplicates for any semantical
Like, to bear… to… to bear any semantic load.
I want to say something like that Compacting a profile.
Like, if someone takes your profile and compacts it by uniquely… by making the dictionary values unique.
It must not break or alter the meaning of the profile.
Oh.
people, like, should not rely, like, oh, I'm putting this
location, and then, like, the next location, and they are the same, but then I'm kind of, like, using the order of the index for some special meaning or something, because if you do that, then merging profiles becomes very tricky.
I think, like, dictionary… I think dictionaries, when we compact them or merge them, that common code, I think it has to…
It has to… it has to respect the… it has to do the compaction, or at least…
like, written in a way that is, like, can do the compaction. If… I don't know if I'm clear, but I hope I…
Felix Geisendörfer 00:37:28 I think you are, and I already see Florian's thumbs up, my thumbs up as well. I think that taking two duplicate messages in the dictionary and refuse…
removing that duplication should not alter the semantics of the profile. It is important to specify that, because otherwise it allows…
for weird side-channel semantics to enter the payloads that we definitely want to discourage. I don't know how likely that is for people to abuse a proto this way, but since this dictionary thing is kind of new to OpenTelemetry.
And kind of unique to profiling, better be safe than sorry when it comes to laying out the semantics we expect.
Alexey A 00:38:05 Okay, I will… then I will, propose a PR and, tag,
Tag all of us and see if anyone else has any objections.
I will add…
Felix Geisendörfer 00:38:22 You'll add an action item? Thanks. Yes. Awesome. Awesome.
Okay, then the next one is also Lexi, profile timestamp Duration and sample timestamps.
But you can take the action item and then respond, you can wait a second.
I hear you have a keyboard that's very notable.
Alexey A 00:38:49 Yes, I just typed some… I typed something just to make sure I get back and add more details to the action item. Yeah, for this one, I had this question when I was writing timestamp checking code.
We currently say in the… we have duration field in the profile, and we say that it's, like, it should be present when it makes sense. I think we say something like that in the comments.
And in general, I assume
Zero duration is a valid duration, for example, for something like live heap profile, because when you take a live heap profile, it's not taken over a duration of time, the values are taken at that moment.
We also have,
I assume we have a requirement, but this is something to discuss, that sample timestamps must be within the profile timestamp plus duration range.
Combining these two facts, does this mean that profiles with duration
of 0 cannot carry any sample timestamps. That's kind of like…
how it implies to me, but I was… I just wanted to have a discussion.
Felix Geisendörfer 00:40:13 My first instinctual response is that, yes, it would be weird for a profile with duration nano equals 0 to have
samples with timestamps, unless they're all the same timestamp.
But that would be kind of weird.
Alexey A 00:40:33 Oh, you mean, you mean, like, if it's duration…
Well, but I assume you would have duration of 1 in this case, because to me, duration of 0 is… means, like, there is, like, it's, it's like open-closed range of, where…
Felix Geisendörfer 00:40:49 I mean, what's the smallest unit of time? Can we get a physicist in here?
Oh, okay.
No, but without getting into that level of detail, yeah, I mean, that's a valid viewpoint as well. You could say that this would require durations nanos 1. I agree there would need to qualify some description here.
I do think that…
duration nano equals 0 is a valid duration, and I think we should discourage putting timestamps anywhere, because that also sidesteps the whole discussion about whether duration nano should be 1 in that case. I think 0 basically means no timestamps in the…
profile.
Alexey A 00:41:28 The only case I was thinking about is, let's say, like, you take the heap allocation, the live heap profile, which is a duration of 0, I think even in current Golang profiles, the heap profile carries the duration of zero. But then.
But then, technically, you said, like, you could say, like, oh, I want to record the timestamp of when the allocation sample was taken, for whatever reason. And that would be somewhere between now and the program start.
But I would argue that if you have a profile like that, then the duration should be… then you probably want to set the start timestamp at the timestamp of when the process started, and duration
Should be, like, up to now, something like that.
And also, this seems like a more exotic case, so I didn't.
Felix Geisendörfer 00:42:16 Yeah.
Alexey A 00:42:17 I didn't…
Felix Geisendörfer 00:42:18 There are actually kind of use cases for keeping track of the…
time of the allocation alive profile, because it kind of tells you how long an allocation has been alive for, which can be interesting, because it's actually for Ghost GC, long-lift allocations would be more expensive, because they have to be marked over and over again.
So I don't think it's that crazy. It doesn't exist right now in Go, but, like, somebody could build a profile in the future that exposes this. I think, actually, on the issue tracker, there were discussions around this.
So… Yeah, how do I.
Alexey A 00:42:54 But then I…
Felix Geisendörfer 00:42:54 represent that. Maybe, maybe we don't need to…
define semantics on this, like, yes, you can have timestamps when duration nano is 0. You convinced me just to flip my opinion here.
Alexey A 00:43:05 Okay. Well, and I was modeling my, profile schema checks over what, what the parkas…
Checker has, and it does have this range check.
And it seemed useful, at least, like, because imagine, like, you work on a new profiler.
And you do follow the semantics that all timestamps should be within the profiler range, then it would be useful to catch cases where they are not.
So, I don't know, like, maybe it should be more of optional language in the documentation, and more of a warning in the checker?
Something like that.
Like, by default, we expect that timestamps would fall within the start plus… start and start plus duration range. If they… if they don't, then you're probably doing something more exotic, so make sure you know what you're doing.
Does that sound reasonable?
Felix Geisendörfer 00:44:10 I think so,
Yeah, it is a little weird to, like, yeah, basically make the duration essentially… I mean, in the worst case, your duration will be the start of the program, because some allocation at program start will actually always be kept alive, because it typically initiates some stuff in main that allocates and stays alive.
The question is if it's going to get sampled or not, but yeah, it basically implies that in most cases, the live heap profile would have a start time, the program start, and the duration of the… whatever it takes to get through the current timestamp, and then all the things would fall in between.
I think that's okay. I don't see an issue with that. I think that's okay, and it's actually nice to think through that, and maybe…
Document that.
Alexey A 00:44:57 Did you just flip the opinion again, or…
Felix Geisendörfer 00:45:01 I…
No, I mean, I think my initial opinion was that there should be no time since when duration nano is zero, and now we're saying, like, okay, maybe.
Alexey A 00:45:11 Okay.
Felix Geisendörfer 00:45:11 Nano should never be zero, and then that opinion flies out that it's not even needed anymore, because we're not supporting that.
Okay.
That's actually the question, do we still have a use case for duration nano equals zero, then? Do we ever want to allow that?
I mean, the two are not mutually exclusive, right? Like…
We could say, like, if duration nano is 0, then…
No timestamps, please, on the samples, otherwise those timestamps need to fall into the start of the profile and plus duration of the profile.
Alexey A 00:45:43 I think the question is, do you want to have the timestamp of when exactly this, live heat profile was taken? Because if we set it to…
Timestamp of the start of the process.
Felix Geisendörfer 00:45:56 And, you know, what.
Alexey A 00:45:57 Well, I guess… well, I guess the end timestamp is when the profile was captured, then. Maybe that's fine. You would have… you would have, like, the start timestamp is when the process started, and then the duration is essentially the uptime, and the sum of those is when the profile was taken, maybe something like that.
Felix Geisendörfer 00:46:15 We… let me just see what we have. So we have TimeUnix Nano, which is,
Time of collection, so we have some semantics on that.
And then the duration of the profile, which would probably go backwards from that. So we have the collection timestamp, and then duration would go backwards to where the collection started, I suppose.
Alexey A 00:46:38 I thought it's the reverse. I thought it's when the collection started, and then the duration is, like, plus that.
Felix Geisendörfer 00:46:47 Oh, well, that depends on how you define a collection, I guess. Like, to me, I would have read this as, like, the collection is finalized, like, it is collected, but I can see your interpretation as well.
So…
Alexey A 00:46:58 I think… I think this is also how it's defined in PROF, so I'm… I'm biased to the old… to the PROF semantics.
Felix Geisendörfer 00:47:05 And that's probably what we intended, because we were copying bupren initially.
Alexey A 00:47:10 But clearly, this is under-documented.
Felix Geisendörfer 00:47:13 I would say so.
I would say for a third party who has not
been exposed to PPROFs, they would not know how to reliably interpret this.
So I think we need to…
Alexey A 00:47:25 Maybe I'll send a PR, to improve the documentation, so that's just, like, to put my interpretation of all the considerations we discussed, and then.
Felix Geisendörfer 00:47:34 Yeah.
Alexey A 00:47:35 And then we can discuss there, or next time.
Felix Geisendörfer 00:47:39 Yeah, I think we could get, like, lost in the back and forth here, but I think the agreement is that the semantics are not well-defined right now, and we should have a PR, so maybe starting the discussions with PR, that just adds your idea of what would be a good semantics, and then we can review that and comment on it async.
Yep.
Thank you, and thank you for, like, I suppose all these use cases come up because you're working on the,
tool to check the consistency of the profiles, this is super useful, because I think we're discovering a lot of issues with the specifications through that. Thank you.
Alexey A 00:48:13 Yep, yep, sure. Yeah, yeah, you're writing code, and then you're like, hmm, I have a question.
Felix Geisendörfer 00:48:19 Yeah, yeah. Text and code, like, two different levels of thinking.
Alexey A 00:48:24 Exactly. I think it's like speaking and writing foreign language as well. Like, when you speak, it just, like, allows so many imperfections, and then when you start writing in the language you learn, it's just so different. But, sorry, don't want to sidetrack.
Felix Geisendörfer 00:48:40 Yeah, indeed. Okay, then I propose we move on from this issue, going once, twice, three times, and jump into…
The last one from your list, Alexi, should profile common string indices be an attribute?
Alexey A 00:48:57 Yeah, this was… we have, I think this is also from, like, historically from PPROF, we have this field, that is called Comments, and this is…
an array of string indices, and the question… and Perov didn't have concept of, like, profile-level attributes, so this is why comments are a dedicated field.
And again, like, I was writing code, and I was like, hmm, interesting. Like, OpenTelemetry attributes, as far as I remember, and I think I checked this, they have ability to express, arrays of strings.
So, do we want to make this an attribute, or does this really deserve to be a top-level profile level, like, profile level field?
Felix Geisendörfer 00:49:42 I would say that we definitely added this field because of our goal to be PPROF round tripable, so we want to go from PPROF to OTLP and back.
And so, I think we already started turning some of the PPROF-specific data into attributes, and…
because of that, I think it would make sense to continue that line of thought here, but I'll let Florian go since he raised his hand as well.
Florian Lehner 00:50:06 I would object, to be honest, with the reasoning, the elements that we put into attributes on the semantic convention side.
are just Booleans, and a Boolean can only be there for a single time, for a message, either be a line, location, or a function.
But with, this comment string in need tests, we can have multiple, and,
I think we will get a pushback from the semantic conventions.
If you want to say, hey, yeah, we want to have a generic comment field, generic semantic conventions for, for comments and
also… also looping in the discussion around uniqueness. I think it would be best if we keep it that way, but it might be a personal
opinion on this, but yeah, I would… I would keep it as a top-level, top-level
field in the protocol, and if it's empty, then it's empty, not set. There are no comments, but…
I think easier handling would be at the moment for top-level fields. Alexa?
Alexey A 00:51:23 I wonder if it would make sense to check whether there are existing attributes in semantic conventions that already, like, array of strings.
I… I vaguely remember I saw something like string, open, square bracket, close, open bracket.
As a type of attribute, because if it's a type of attribute.
then it should not be a problem, right? Because I would… like, if you… if semantic convention… convention allows having a value that is
Like, defined as a type as string array.
then…
I wouldn't expect, like, no guarantees about the order in that value. I can see, like, no guarantees regarding the order of attribute, like, attributes themselves, because it's a map.
But if you have a value of string slice, then…
I would expect ordering semantics, like, ordering to be preserved.
Florian Lehner 00:52:21 From the top of my head, I don't remember… semantic question attribute
That is using a slice of strings, to be honest.
Alexey A 00:52:32 Okay.
Florian Lehner 00:52:37 But I can be wrong, so I don't know every semantic convention, so…
Alexey A 00:52:42 Yeah, I'm also not, very far from expert in them.
Felix Geisendörfer 00:52:47 Okay, but just as a sort of experiment, Florian, if there was prior art for that, would that ease your concerns about pushback from the semantic convention group, or…
Florian Lehner 00:52:57 Yeah, if there is prior art, there should be… it should be fine, I think. We already established the PProf attributes.
Semantic convention, and then it would just be another…
attribute in this PProf list.
So, pre-profile comments, for example.
At the moment, these are all Booleans.
Felix Geisendörfer 00:53:24 Okay.
So… how about… Alexi, do you want to check if you can find prior art and make a decision based on that?
Alexey A 00:53:31 Yep, that sounds good.
I'll add another item.
Felix Geisendörfer 00:53:38 Thank you so much.
Alright.
Anybody wants to add to this? Going once, going twice…
And we are going for Florian's. Do we want protocol consistency? Who doesn't want protocol consistency? But please tell us more.
Florian Lehner 00:53:59 Yeah, when writing the, receiver for PTROF,
I noticed that we have no line table in our dictionary.
And that's the only, message in the…
In the… in the protocol that we…
We do not index, but have a direct…
direct, elementary, basically, so…
It doesn't have an impact, as far as I can tell, on compression at all, so it's really just consistency in using, the protocol
So, just wanted to hear the thoughts of everyone, hey.
Felix Geisendörfer 00:54:45 So we will not…
Florian Lehner 00:54:47 How did you determine.
Felix Geisendörfer 00:54:48 In that it has no impact on the data sizes?
Florian Lehner 00:54:53 So I did run the benchmarks for… that, Christos wrote.
a few months back, and that we also had, referenced in these discussions earlier. And, the differences were below 1%, so I would not say these are representative in any way.
And, I think it was,
It was Tigran, yeah, Tigran. Tigran also, commented on the PR and says, hey, there is probably no impact with his experiments.
And so, yeah, we will not get any, any… Improvements on this.
So that's… it's just more like, hey, how… how you interact with the protocol, in a consistent way.
Felix Geisendörfer 00:55:48 Yeah, Alexi has his hand up.
I think it's stale, but… Oh, okay, sorry.
Alexey A 00:55:57 But nevertheless, I do.
Felix Geisendörfer 00:55:59 Now you need to respond, now you need to respond.
Alexey A 00:56:01 Yes. Yeah, I looked at this, and I commented on the pull request. It didn't… it didn't… it didn't strike me, like, as an obvious case for another indirection.
Because one thing is…
whenever there is, like, one more level of indirection, there is also runtime cost that is harder to measure, but… but still, like, for example, in Go.
or in, like, any garbage collection language, it's in directions, so, like, there's more garbage collection pressure. So I think… and also, the line message is fairly small.
I think it's, 364-bit fields.
So, it, and also, like, people doesn't have a dictionary for this, so I'm… my People, like.
IProof schema knowledge also, like, says, like, oh, we don't need this because we didn't have this. So I… I don't know, like, I'm… I'm leaning more against this than for this.
Florian Lehner 00:57:01 Yeah, no hard feelings, it just was like, hey, when I was writing the code, I noticed, hey, why do I do it this different than the other messages that we have?
Yeah, we also have, lookup tables for other simple elements, like, stack, and stack indeed says, so, or function is also quite, a simple one.
Huh.
Felix Geisendörfer 00:57:25 Yep.
Can I ask you just a stupid question real quick?
We think that line… like, in theory, I could see a profile having a lot of lines with the same function and line number, right? But we do… deduplicates this already on the location level in most cases, right? This would really just be when there's different inlinings, or something like that?
Florian Lehner 00:57:44 Yes, I expect this, more heavy impact if the, the line is different, yeah.
Felix Geisendörfer 00:57:50 Okay.
Alexey A 00:57:59 Yes, you could… you could have the same, like, the same by-value line message in different inline stacks.
But… How much is that? It's… it's… it's hard to say. And also, the win is…
Like, it's… this one is currently, like, 64 times 3.
And then you still need the time… you still need 64, like, 8 bytes.
Felix Geisendörfer 00:58:29 I mean, it's… this is VAR-And encoded, right? So it's actually more compact, typically.
Well, in memory, I was thinking in memory. Oh, in memory, okay, sure.
Alexey A 00:58:39 Yeah.
But yes, on the wire, it's… it's less than that.
Felix Geisendörfer 00:58:48 Okay, I don't feel too strongly about it,
Let's continue discussion in the PR, or… Somebody wants.
Florian Lehner 00:58:58 Yeah, sounds good to me. And, if there's no feedback, we can also close it.
That's also fine.
Alexey A 00:59:12 But, thanks for raising this. I think… I think whatever the outcome is, it's a useful discussion, and I think it's, yeah, every time we spot an inconsistency, we should make a conscious decision.
Whether this is just, some sort of legacy and carried over, or we actually are okay with… with… to live with this for years.
Felix Geisendörfer 00:59:35 Yeah. We're out of time, so I'm just gonna do a closing thought, which is KubeCon, is coming up, call for paper closes, I think, October
12 or 13, so very soon. That's general call for action for anybody who wants to be at KubeCon, because we could all gather there together, so submitting a talk is a good way to have
your trip approved by the employer. Floyd and I were talking about maybe doing a joint presentation for OpenTelemetry.
There's a maximum of two male speakers for KubeCon or CNCF events, so if somebody else is interested, please raise this ASAP, because we need to sort out who would want to present. Florian should definitely do it, because he was interested last year, and…
Damien ended up doing it. I did it last year, so I would…
sort of have to drop out if somebody else is interested, so just raise your hands. If you are, we can do this offline in Slack, but anybody who's a member of Sysik should obviously have a chance to…
Be part of this, if they're interested.
And with that being said, thank you all for attending, as usual, and, have a nice local time.
Florian Lehner 01:00:48 Good, Joe.
