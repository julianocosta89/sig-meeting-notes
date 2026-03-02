SIG: Profiling WG
Date: 2026-01-08
Duration: 39 minutes
============================================================

## Zoom Recording Transcript

**Florian Lehner** 00:48 Bonjour!
**Ivo Anjo** 00:50 Happy New Year!
**Florian Lehner** 00:51 Happy New Year, too.
**Frederic Branczyk** 02:21 Hello, hello! Happy New Year!
**Felix Geisendörfer** 02:25 Hey!
I can hear you.
**Ivo Anjo** 02:26 Happy New Year!
**Florian Lehner** 02:27 Been to you.
**Felix Geisendörfer** 03:25 Let's wait until 5 minutes past the hour, and then we can kick off.
All right, I guess we can get started. I'm gonna share my screen, walk us through the agenda.
Alright, can everybody see this?
Good.
And as usual, we'll start with reviewing the previous action items, so I'll make a copy of them.
And… Alexi is not here… As far as I can tell…
So, I'm just gonna make note of that.
**Frederic Branczyk** 05:37 He just commented that he's on PTO today.
**Felix Geisendörfer** 05:40 Okay.
**Frederic Branczyk** 05:42 It's on your screen, actually. On the right.
**Felix Geisendörfer** 05:46 Oh, well, there's… there's, like, Zoom window with your faces in front of it, but now I see it, like, I was hiding things.
**Florian Lehner** 05:59 Besides from that, I think it needs more attention and refuse from people.
So it's pending already for some time.
**Felix Geisendörfer** 06:13 Alright, okay, I think I can find time in the next cycle to take a look.
Oh.
As usual, put a little alert here to make it easier to find these in the notes.
Thanks, Florian.
That gets us to the next one, Florian, OTLP to P-Prof converter.
**Florian Lehner** 06:34 Yeah, Senconf, was merged, so the first PR.
And the second PR, I think I got an approval from Christos and Felix.
Joe.
someone from Contrapp is needed.
Also, to get… to approve it, to get forward.
**Felix Geisendörfer** 06:55 Okay, this… Antoine, a contract approver?
**Florian Lehner** 07:03 I think, yes…
**Felix Geisendörfer** 07:08 He might be the person to ping, but,
Oh, I guess, no, the lock is on… Songi?
Yeah, something was automatically assigned by the bot, so…
**Florian Lehner** 07:20 Just one of the approvers.
You know, I think I pinged approvals this… beginning this week.
But feedback is, limited so far.
**Christos Kalkanis** 07:31 I would say let's ping Antoine directly, because he was the one who brought this up, and he is the main stakeholder for this.
**Felix Geisendörfer** 07:40 Yep.
Does that sound good to you, Boyd?
**Florian Lehner** 07:47 Not sure.
**Felix Geisendörfer** 07:49 Awesome. Cool.
Okay, anything else on this, or moving on?
Then, next one is Review Process Context Propagation, OTAP.
**Ivo Anjo** 08:06 Yes, I can say things about this one.
So,
Thanks, Christo's helped, helped a lot in fleshing out a bunch of things in the specs, so since last time that we met, we've reworked the plates to be a lot more efficient.
And, we removed the need for falling, for the fallback from, for kernels without, the support for naming anonymous mappings.
And instead, we use, like, a MFD as a base to get the naming as well. So basically, like, it's like a small detail, but it means that the fallback is no longer needed, and we have a cheaper way of doing this that should work.
All the time.
And, I actually, like, I think the question at this point is, what are we missing that would get the folks here to, get the approve button on that PR?
Because I think that, like, okay, once we get the approve from the members here of the profiling SIG, we can, or I can kind of go back to the specification and talk to the other SIGs, and…
push forward and ask them what's missing for their approval, but yes, I think the first step here is getting approval from the folks here.
**Christos Kalkanis** 09:31 Evo, I'm ready to approve, it's just that I wanted to do a final pass over the actual document, and yeah, but I'll provide it today or tomorrow.
**Ivo Anjo** 09:40 It's on to it.
**Felix Geisendörfer** 09:41 Okay, and you can also get a review from me, Ivo. Well, I'll do a pass.
**Ivo Anjo** 09:51 Cool, thank you.
**Felix Geisendörfer** 09:53 It highlights us.
If anybody else has time, please review and approve.
**Ivo Anjo** 10:04 And the… the only other thing I wanted to add is that, we got a bit delayed on the ex… on our experiment with the thread… with the thread level context, but I'm really, really hoping that by the next meeting in two weeks, I will have
Some things to bring up for discussion, so we can start, like, wider, wider discussion about that.
**Felix Geisendörfer** 10:27 That's good. Cool, thank you.
**Florian Lehner** 10:29 I already talked about fret level context already with Evo, and I joined EVPath Instrumentation SICK yesterday, I think it was, and they are also discussing approaches for fret level.
Context sharing.
Their use case is to be able to correlate, traces, metrics, and logs, with span, span, span IDs, and, if I remember correctly, the idea was to use an eBPF map.
But they did not formulate something in a more hotel-specific way.
So, yeah, but, I asked them to reach out and provide feedback to us, for the process context.
In the first step, as this is the base for us to continue with the thread-level context.
**Felix Geisendörfer** 11:22 Awesome, thank you for making that connection, that's great.
Okay, any of those thoughts on this one?
Going once… Going twice.
And 3 times, let's move on,
Yeah, I mean, Alexi's not here, but I guess we can click on the link. Didn't we align on the answer to that in the last meeting?
I feel like we did. If we could go back on the notes…
The one before…
Okay, let's circle back to this when Alexis back, but I feel I can probably find it at some point in the notes.
Okay,
Florian733 reference resources. I guess it gets us into the update down here, but I don't know, do you want to talk about it, Florian? Should I give the update on the meeting, or…
**Florian Lehner** 12:54 Feel free to give the update on the meeting.
**Felix Geisendörfer** 12:57 Okay, so, I'll just move that up here.
So some of you were in the meeting, so you have a good idea of what happened.
But basically…
we met yesterday with, folks from the TC. There was, Tigran and Josh, as well as, collector maintainer Bogdan, who we needed, to get around on.
on this idea, in order to make sure that it's not going to work from the collector's side. There were a lot of discussion, there were a lot of things said, but I think the ultimate outcome was pretty simple, which was instead of doing something complicated in the collector.
we basically, in the collector's internal in-memory data model, pretend there are no dictionaries for attributes. So, the way that would work is when the OTLP receiver receives,
profiling payload, and it discovers stuff that has dictionary references for attributes, it just converts it into the normal P data during the parsing of the protobuf payloads.
And then, all the processors are basically working on existing resource attributes, as they always have, no changes needed for anything there. And then when the Kubernetes attributes processor and other things have added more attributes.
In the final step, there's going to be an exporter at the end, and the OTLP exporter is actually going to be like, oh, I know that profiling… this is a profiling payload, and I know that profiling has these dictionaries for attributes that I can use.
So the exporter is actually gonna take advantage of the dictionary encoding and populate the dictionary references in the resource attributes. And that seems like a really smart, elegant solution. Alexi, I think, was the first one to bring it up during the meeting.
And yeah, basically, I think that convinced Bogdan that he's okay with us going ahead with this.
He still wants us to explore potentially, also having non…
reference-based attribute support for the rest of the signal, like inside the profile's message. I guess I can add that as an agenda item down here. I don't… I think it's kind of attention or orgonal to the main discussion, but yeah, the main thing is unblocked, so I think
We just have to look at the pull request again, 733, make sure this is the way we want it to be, but if it is, I think it can finally go in, which then actually is, to me, like, the major thing that was blocking us going to alpha, which is very exciting.
So, yeah, thank you everybody for churning the coal and working on this for so long to get us to this place, but hopefully now we can close the door on this one.
Yeah, for those who were there, let me know if I missed anything.
Or if this sounds like what we had discussed there.
**Christos Kalkanis** 15:57 Yeah, so, I mean, the only thing I think that's left is concerns about memory efficiency in the collector, right? And the way that we want to handle that is to have the receiver entering strings, right? So, like, from the point of view
Of any processor, nothing's changing. Memory module is exactly the same.
But for efficiency, when we create the data, we can insert all the strings so that we only store one copy in memory, for example.
**Felix Geisendörfer** 16:27 Yeah.
**Christos Kalkanis** 16:29 Yeah, go ahead.
**Felix Geisendörfer** 16:30 I think that's kind of a little bit of an implementation detail, but yeah, we'll probably do that implementation detail, because yeah, it's gonna make sure that we get the same benefits in memory as we get on the wire.
**Christos Kalkanis** 16:41 Yeah.
Because, I mean, there were two concerns, right? One is, okay, payload size on the wire, which we take care of, because we will have dictionaries on the wire, but the other concern was, that Naev has brought up in the past, yeah, you know, what happens with memory in the collector could blow up, and so on. So we have to kind of look at that as well. And, let me share my screen, actually.
I can't share. Felix, you're sharing yours. I just wanted.
**Felix Geisendörfer** 17:10 Yeah, yeah, I'll get fused.
**Christos Kalkanis** 17:13 I'll jam to the… to Florian's pull requests.
So this is the state of our proposal as it is right now, and we're introducing new methods here, right? NERF value.
we've kind of flipped back and forth between two alternative implementations. Initially, I think we didn't have any ref value, we instead introduced a reference inside any value, and I think
like, based on the latest discussion, it makes sense to go back to that. Also, Bogdan brought this up, so instead of creating a new message, just for profiling any refiler nobody else is using.
we can put the reference inside any value, right? And then it's…
actually more compatible with the rest of Otel, and we don't create, like, a separate universe.
messages that Tony Profiling will use.
What do you think about that?
**Felix Geisendörfer** 18:09 I like the older version better, I wasn't sure why we even went to this one, so I guess it's a question for Florian, who's driving this, but…
**Florian Lehner** 18:17 Yeah, any ref value was introduced because there was a request to distinguish between current implementations, like logs, metrics, and traces, that should not use this new value, so this new string value reference.
In one-off, we cannot use, string, and string value ref, as one-off, so embedded one-offs are not possible in the
In the proto, call, and that's another reason,
Yeah, I can, I can add,
A string value reference as an additional field to any value.
This will make the implementation easier for profiling in the collector, I think.
But it will make it harder for other protocol…
that we have to avoid further protocols.
**Christos Kalkanis** 19:16 Why would it make it hard for other parts? Because, essentially, we will extend any value, right? We'll add this.
**Florian Lehner** 19:23 Yes, because… yeah, because, how can we, how…
the discussion, or what I did understand from
Or going a little back, a little bit back, hmm…
the change should just be used by profiles and not by other protocols, because of backwards compatibility. If we just add another value to one-off value here and any value, then it can be used by anything, unless there is a
Like, in any rep value, there can be a comment.
But comments are usually just ignored.
**Christos Kalkanis** 20:03 I think we discussed this yesterday, and Bogdan said that we have a way to enforce it. Josh might have something irrelevant.
**Josh Suereth** 20:09 Yeah, I think… so the difference is… we'll have to talk with Bogdan, but Bogdan's looking from exactly the collector perspective, not necessarily the overall perspective there. The reason we don't want it is because
If you think of, like, an SDK implementing this, they're not gonna be able to fill out that field, but they're gonna have to handle the value in a switch statement. And so, what happens is when we add features to OpenTelemetry that will never get used, it causes a lot of confusion.
Right? So, if you force all protocols to handle this because you put it in any value one of, eventually what's gonna happen is, everyone's gonna have to handle it anyway. So it's like a big churn on the system. That was our original motivation for not having this. If we…
want to put it there, and we're okay with that, that's… that's a discussion, but that's a discussion, I think, to have with, like, the protocol owners. Bogdan is one of the TC that own it. It's basically Bogdan, Tigran, and I are kind of
the three you need to convince there. Tigran and I did not want it in any value. I think Bogdan does, so that might be a discussion for us to have. Again, it… this comes down to not the collector, not the profiler, but, like, any arbitrary…
consumer of OTLP,
We'll have to deal with the fact that there's this reference thing that they can do nothing about.
And it causes a lot of confusion and friction when that's the case, as opposed to having a separate type that only the profiler would use. I think PData could have an abstraction where they have both of those types supported in one thing.
And make the… at least the collector be simple there.
Yeah, but this comes down to, if we had a way to add profiles to all signals without breaking OTLP, I think that's the approach we would have taken. We just kind of exhausted our research budget on figuring out how to do that.
**Christos Kalkanis** 22:01 Not naive?
**Nayef Ghattas** 22:03 Yeah, I think one of the other asks that Bogdan had that is also sort of related to this is that he wanted to support both reference values and inline values at the same time for also profiling specific attributes that are inside the profiling signal.
And I'm wondering whether, having a reference in any value directly as a one-off value would allow us to directly use any value in the profiling signal.
And that would also, like, sort of solve the problem he raised, where he wanted us to support both in… if we want to support both.
So, because right now, my understanding is that we have our own, like, attribute table logic, where we have our own key and our own value that…
**Christos Kalkanis** 23:13 Yeah, we have an attribute table, so we essentially do array indexing for entire attributes, which And, here.
**Nayef Ghattas** 23:21 And they would type, yeah, key value and unit.
**Christos Kalkanis** 23:24 Yeah, and that's our own… Like, nobody else is using this but us.
**Nayef Ghattas** 23:29 Yes, and that thing only supports references and doesn't support, direct values.
**Christos Kalkanis** 23:41 Yeah, so I think Bogdan wants us to use regular attributes for something like this, like the profile here, yeah.
**Felix Geisendörfer** 23:52 Yeah, I don't think Bogdan would be happy, so if we just put this in the any value, the…
Because… We still, like, in the profiling signal, point to an array of, like, attributes, right?
attribute indices, and I think he wants, like, yeah, as it was just pointed out, to directly have the attributes inlined in those messages.
**Christos Kalkanis** 24:26 Okay, I guess we first need to decide whether…
So, Bogdamn, I think, mentioned that
he wants the references to go in anybody. He said that yesterday, 100%,
But if Degran and Josh
Don't like this, then, you know, the consensus seems to be that we can't do it.
So then…
**Josh Suereth** 24:50 So, yeah, was Bogdan asking if we should put in any value in the proto or in P data? That's the other thing that I wasn't sure of yesterday, because I interpreted that as P data.
Nice.
**Florian Lehner** 25:00 Proto. In the produce.
**Christos Kalkanis** 25:01 time p-data.
I think he was talking about the proto, like, we're not gonna…
**Josh Suereth** 25:07 Let's clarify that first. If he's talking about P data, then this is easy. If he wants it in the proto, then let's have that discussion on this PR.
**Christos Kalkanis** 25:25 Okay, so, yeah, I'll add the comment here to the PR, I'll ping Bogdan directly to have another look here and clarify.
**Felix Geisendörfer** 25:44 Cool, thanks.
Yeah, there was another thing here, benchmarks, I'm just gonna delete that. So let me reshare screen.
And I guess, yeah, next step here is Christos pinging Bogdan to get the answer. I'll just note this in the action items here.
Stunned.
We'll sit down later, or somebody else can do it.
God knows, too much of you can do.
Okay.
Any more thoughts on this?
**Christos Kalkanis** 26:41 I guess we can create a proof of concept, right? We don't have to wait to… to resolve it. It's like, we can do the proof of concept regardless, just to see how it looks from the export and the receiver.
**Felix Geisendörfer** 26:51 I guess.
No, Florence shaking his head.
**Florian Lehner** 26:55 Not that easy, I'm…
everyone that did experiment with changes to the protocol and then implemented in the collector knows that this is not just a four days engineering work time doing so. So this is a little bit more work.
I did, some experiments with, having the translation and the P data.
But yeah, we'll not continue and be able to do something more unless the protocol or we have something that
That the protocol is, that I can work on the protocol. At the moment, it's just…
Some constants that… Trust.
Local experiments, if it's possible, even.
**Felix Geisendörfer** 27:46 Okay, then…
next step remains the same as before. Christos, if you can reach out to Bokta and get a clarification on where he wants to go with this, make sure we're aligned between him and the TC and the SIC, and if we do find a combination that we all are happy with, then we can…
Finally gets us in.
Awesome.
Thanks. Any more? Going once.
Going twice, that's three times.
I think then we get to the regular agenda for today. Dale has some comments on Ruby PR reviews. Is Dale here? I think I saw him.
**dalehamel** 28:25 Hey, yep. Yeah, so I put these notes in for the last meeting, of 2025, but it looks like
943 has now been merged.
I got an initial review from Timo on Monday, and so, yeah, I've addressed his comments and just kind of waiting… waiting on that.
So yeah, so there's progress on that front, not much to call out, just sort of waiting for the normal review cycle.
I did notice today, though, like, there's PR1048 that affects the Ruby core dump tests, and there's also, like, new versions of Ruby that are out, so we're just kind of falling a bit behind on
You know, kind of where we'd like to be, but…
You know, it's a big PR, so I understand it'll take a little while to review.
**Felix Geisendörfer** 29:15 But sure, yeah, I saw that. That makes sense.
Yeah, thanks for continuing on this, and hopefully we'll get the final review soon.
**dalehamel** 29:23 Yeah, I have a couple of other PRs that follow on from this, so it'd be nice to kind of just be able to submit them, but I don't want to, you know, overwhelm folks with all the work, so…
**Frederic Branczyk** 29:34 Yeah, I'm actually… it's a little bit further down, but I actually wanted to discuss this topic as well, if there's…
preferences on… order of merging these. The topic that I have as the second-to-last one is essentially the.
**dalehamel** 29:51 Oh yeah, 1048, yeah.
**Felix Geisendörfer** 29:54 Do we want to just merge it in while we're talking about it?
**Frederic Branczyk** 29:57 It's… I mean, yeah.
It does… it happens to also touch Ruby stuff, because we needed to fix it when we fixed the other, the other things there. It is significantly smaller, but I do understand that the other PRs also were opened before, so…
Just wanna hear what people think.
**Florian Lehner** 30:22 My personal preference is to have days first.
for various reasons, and then go on with 1048. It's way smaller.
And I have the feeling that we have to look more into 1048.
That breaks some Ruby stuff, so… Yeah, it actually fixes.
**Frederic Branczyk** 30:43 some Ruby stuff, but…
**dalehamel** 30:44 Yeah, I think I know.
**Frederic Branczyk** 30:45 the problem.
**dalehamel** 30:45 he's talking about, and I had been scratching my head for a long time trying to figure it out, so, yeah.
That's good, it's good to see, just unfortunate timing.
**Frederic Branczyk** 30:58 Yeah.
Alright.
**dalehamel** 31:02 It would just… it would be nice if we could get, yeah, 907, reviewed in first, just to not have to touch it again.
**Frederic Branczyk** 31:09 Then I second that.
**dalehamel** 31:12 And I don't think it should be too bad to redo the core dump fixtures for you, so…
Cool, thanks.
**Felix Geisendörfer** 31:26 Okay, cool, thanks. Any other thoughts on, 1048, 943, 907?
Going once, going twice… No, then the next one on the agenda is…
No version 24, long-term support unwinding. Go, go for it, Christos.
**Christos Kalkanis** 31:51 Yeah, this is from the previous, previous, meeting. It was more a question for Frederick. I think,
Frederick, you lost some comments there on that issue, and I think we assigned the issue to some folks from Polar Signals.
So, yeah, it's just more like an update regarding…
I'm guessing it's on the pipeline.
**Frederic Branczyk** 32:22 Yes. I think this was just just wind.
under, with the holidays, I'll ping…
**Christos Kalkanis** 32:30 Okay. Brendan, internally.
And also something unrelated, but also for polar signals, I think. So we have a draft pull request for low exit unwinding, and the last, I think, activity there is from March 2025.
Yeah, it would be a shame not to… not to match it. Like, we recently added Erlang, it would be great to also have Lu Edit as well.
Just… and also, we got some,
interest from some folks at Elastic. They've been asking about it.
just.
**Frederic Branczyk** 33:05 Yeah, ultimately, we're… we don't want to have this in our fork. Like, I think it was just that last time…
we were waiting for reviews so long, or whatever, it took so long that we started some other work, and that was the only reason why we didn't follow up on it.
We definitely want this merged, and we did… we actually did a number of fixes on top of this. A number of our customers run this in production.
**Christos Kalkanis** 33:34 Okay, so yeah, I mean, so from my end, I can ask Timo to prioritize it. I think the last comment is Timo's, he's asking for a rebase or something, just to bring the draft pulley request into…
To be more current.
And then, yeah, if I see you guys working on it again, then I will…
**Frederic Branczyk** 33:51 I would recommend not necessarily continuing that pull request, because there are tons of fixes that we've done on top of this.
**Christos Kalkanis** 34:01 Okay.
**Frederic Branczyk** 34:01 So, I think I… I'm gonna see… Tommy is working… Tommy internally, originally worked on this, but is now, like, in the depths of NVIDIA GPUs.
So, I don't know when he's gonna get to this.
We'll have to see, I don't know exactly, but my recommendation generally would be not to continue the pull request that's open.
There were a variety of things that needed fixing.
**Christos Kalkanis** 34:35 Okay, cool.
**Felix Geisendörfer** 34:45 Okay, any more thoughts on this? Going once… Going twice… And…
Next agenda item it is. Alexei has raised, sample values, sample timestamp Unix nano would make sense to have a scalar or simple value field for the presumably common case when no array is needed.
And I think this is, Jonathan Halliday saying he's against it. Maybe, Jonathan, do you have… are you here? Do you have something?
**Jonathan Halliday (IBM)** 35:18 I was a few minutes late, but I'm here now. Yeah, I mean, I don't hate it, but…
We already have to jump through a number of hoops to encode.
this protocol. It's… it's fairly complex, and adding more complexity
This doesn't seem like a huge saving to me. A one-value array versus a scaler is, like, yeah, can't be bought, frankly.
**Felix Geisendörfer** 35:46 I agree, because, yeah, we spent a lot of time sorting these fields out, and touching them now would move us further away from alpha than getting closer to that.
**Jonathan Halliday (IBM)** 35:55 Yeah, and it forces us to deal with the corner cases, like, you populate both, which is the right one, and yeah. Skip it.
**Felix Geisendörfer** 36:07 Okay, and since Alexi's not here, let's decided, great. Let's move on to the next one. No, of course, when he gets back, we can…
Or next time he's here, we can discuss it with him. Cool. Anybody else has, strong feelings on this I want to share before we move on to the next one?
Going once, going twice, three times. Yeah, actually, the next one is me, like, the… basically just Bogdans asked for attributes, with… without references in the… in the rest of the signal. I do wonder whether or not that…
We should get him to clarify how he wants to treat any value versus any ref value situation, because that might have some overlap.
But if anybody else has immediate thoughts here, I personally, I don't…
I think I would like to understand from him a little bit more why he wanted it. He just said he wanted it, and then we didn't have a lot of time in the meeting to discuss it. Maybe some of the people who are there can channel Bogdan's reason for asking for that. I know he said, like, he likes consistency, but to me, that's not, like, a coherent…
Case for why we need it.
**Florian Lehner** 37:20 I think one point that Bogdan is not aware of is that we use attributes with units, and, which makes a big difference, compared to Lux metrics and traces, which just use attributes with a key and value.
And,
I'm not sure if he was aware of this difference for profiling, because in the rest of the profiling protocol, we use key value and unit.
Everywhere, and so… Either we bring up key value unit as any value somewhere.
But I don't see this happening, to be honest.
**Christos Kalkanis** 38:02 I will make it… I will make it part of my… like, I will take Bob then and ask him about this as well, so… I'll get him… I'll ask him to clarify this. Yeah, I completely forgot that… I mean, I actually just saw it now when I was sharing the screen. So, key value and unit essentially encodes two values, right? And an OTL attribute.
Only one. So we have a problem, though.
**Felix Geisendörfer** 38:25 Yeah.
**Nayef Ghattas** 38:27 It's also not clear to me if this is something that he wanted in P data only, or whether
This is also important to have on the wire.
**Felix Geisendörfer** 38:38 Hmm.
Good question. Yeah, okay, Crystal, yeah, if you could try to get him to clarify a little bit on that, that'd be amazing.
Okay.
Anybody else has thoughts on this agenda item?
Going once, coming twice, then three times,
I suppose that brings us to the end of the agenda. I guess I can ask if somebody has some last-minute things they want to
race, since we have a little time left. If not, we're gonna get some time back.
No? Okay. Then, yeah, thank you everybody for attending again on the first session for the year. And yeah, enjoy the extra 20 minutes in your day, and make good use of it.
See you next time.
**Frederic Branczyk** 39:46 Thanks, everyone. Thank you. Take care.
**Christos Kalkanis** 39:47 Thanks, bye.
**Felix Geisendörfer** 39:48 Yeah.
