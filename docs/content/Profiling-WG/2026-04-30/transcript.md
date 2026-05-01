SIG: Profiling WG
Date: 2026-04-30
Duration: 62 minutes
Zoom Recording URL: https://zoom.us/rec/share/Ybeh08ebW6L5fpMlkKWuI3Dwjozzo-2VUfxSAJm_KaRlBhOidZCTM-GsX-FdHjhO.c9K6uE4xWNdcuzyR
============================================================

## Zoom Recording Transcript

**Scott Gerring** 05:49 Ivo, what time is it in Tokyo? Or in Japan?
**Ivo Anjo** 05:54 It's the future, I'm, ask me, ask me how Friday is.
**Scott Gerring** 06:02 How's Friday?
**Ivo Anjo** 06:06 Good so far.
**Frederic Branczyk** 06:20 Hello!
**Christos Kalkanis** 08:54 Should we wait a few minutes more? Do you guys know if Felix is joining today?
It's not online in Slack.
**Ivo Anjo** 09:07 He… I think he's marked out of office, so he might not be around… Yeah, it's marked as out of office in his Datalog calendar, so I'm guessing that means no Felix today.
**Christos Kalkanis** 09:20 Okay, okay, cool.
So I guess we can begin the meeting.
Alright.
Let me share my screen.
Okay, so usually we start with the action items, so let's review those first.
And let's see what the first one is about… So I think we've previously discussed this in the last two meetings. This is about increasing the default request size.
Does anyone have any updates on this?
**Alexey A** 10:19 I remember there was something… Felix wanted to post some numbers, if I remember correctly.
**Christos Kalkanis** 10:26 Right.
Okay, so Tegran has blocked it until we get data.
Alright, so I guess there's nothing we can do for this one right now. Let's… we can move on.
Felix and Florian, the key value unit proposal.
So I think initially we had this extensive value with units, and then… to kind of sidestep the issue of introducing units right now, Florian and Felix came up with this proposal, which Make some changes to some medical mentions.
Florian, do you want to… Give us a recap.
**Florian Lehner** 11:09 Yeah, I can quickly talk on this. We actually came up with two proposals in two documents. One is changing semantic conventions, and one is making changes to the protocol. The reason why Felix and I came up with two proposals is… The change to the protocol might be a bigger discussion within the Auto ecosystem, and we, Felix and I, have the feeling we should more continue to for, For a stable protocol, and the changes to this Monday convention is a quick win for us, that we can say, hey, we are compliant with the protocol, we can drop, the custom key value and attribute, and keep the same information in semantic conventions. So, if you scroll down a little bit, it will introduce a num unit, as PPROF, Which, consists of key, value, and unit.
And, adding this to a semantic convention in the scope of pre-prof is quite, or should be quite easy and fast, as we control it.
It will introduce a little bit of overhead on the controller side, receiving and, receiving and sending side, but overall, it does not impact any other existing signals, so this is the, least… I would say the… the fastest way forward, with, which does not involve any work with other, signals.
If you open the other, other, document.
This is then the second approach, extend key value with unit information, so this involves, changing, protocol information. There are some unknowns, for example, around the unit type. At the moment, Hotel is using this, this convention for, metrics, for the convention for units called UCUM, and, PPROF is not specific on any unit, so you can use unit whatever you want.
And this might conflict. So if you say, hey, we go with the changes to key value, and if you scroll down a little bit, then we can see, hey, we're following the same approach we use with, key, string index, and just, have the very same for unit, then… This would be enabled, this would be an enabler for, other signals as well in the future, but this would, require an alignment with other signals, so… As far as I know, Felix and I did not receive any feedback, so far on these two proposals.
But these are possible ways forward. I see a hand, Alexei.
**Alexey A** 14:14 Yeah, I'll… I'll… I'll take a look, Yeah, I saw the discussion somewhere, I didn't realize that there were documents. Sorry, I probably should have seen the links in the… In the list. But yeah, I will, I will, I will, I will take a look.
And, for, for the unit information, like, from other signals from OpenTelemetry, like, from Tigran and others.
it doesn't look like we got a lot of interest, right? Like, because I think at some point… at some point, Tigran said, like, yeah, this might be useful for… For overall OpenTelemetry, but… But it's not like they… it's not like they are, like, ready to drive this or anything.
**Florian Lehner** 15:01 Yeah, I think there's interest, or at least the feedback I get in personal conversation is there. The problem is more like no one has the capacity to bring a… drive it forward.
And, without, the capacity to make this change and driving this change, in a reasonable time, meaning bring in also profiles to a stable point at some… later this year, maybe?
Yeah, that's a really hard road to go.
But both proposals, or both documents, are not mutually exclusive. So, if we say, hey, we go the, the semantic conventions route and introduce the new, element for PPROF, for the type, for the unit information, in PPROF, the PPROF scope.
We can still go this route and later go on with, changes to the protocol. So, they are not exclusive, they are not, excluding each other's ones, so, that's… at least for profits, our way forward.
But, yeah, we need feedback, that's the moment.
**Alexey A** 16:15 Yeah, I'll take a look at the document. One… one question I have, like.
But that's more for the document discussion, whether, like, underscore is unambiguous enough, or… because… Because if you… because maybe the unit name itself can contain an underscore, and the tag name can have an underscore, and then… whether you can parse it back unambiguously, but that's… I'll comment on that, we can discuss in the document.
**Christos Kalkanis** 16:42 There's… yeah, there's also the possibility of a collision. I mean, it's… it's… I think it's highly theoretical, because, in our… like, we could have two separate strings.
that collide, and because of how the key and the unit, like, the prefix of the unit may end up being the same as the suffix of the key, for example. And for that to happen, you would need the unit That, you know, would be… would have to be sort of weird.
But in theory, it's as possible, so maybe, like, if this ends up becoming a specification, like, you have to account for that.
possibility. So it has to specify how collisions are treated.
**Alexey A** 17:23 the joy of software engineering. Look at your number row on the keyboard, and think about what special character to use in this case.
I don't know, like, maybe two underscore or something. We can… but yeah, I think we should make the parsing unambiguous enough, because I… for people, I know that internally we do have tag names with underscores, and we have… and I think we have unit names with underscores as well. But I should double check. Maybe we don't have unit names with underscores. Anyway, yeah, I'll comment on the document. Thank you for putting this together.
**Christos Kalkanis** 18:00 Florian, one small comment here. So, for this example, I think the example, it would be better if instead of embedding the attribute, like, here we would show the attribute table as well, and then this headers would be the indices to the attribute table, because right now, like, someone who's not familiar with how we encode, this could look at this and get confused, right?
I think it was done like that for maybe simplicity, or because it's less data to show, but I think it's better to be explicit here, right? Just show the attribute table separately, like we do for.
**Florian Lehner** 18:34 We don't use the attribute table here. That's completely living in a semantic convention, so it's a list of two strings.
**Christos Kalkanis** 18:47 No, but I mean sample C, attribute indices, right? And then you have an array, and the array contains this, right?
But this should be a reference. This should be a numeric index.
To a separate table, right?
**Florian Lehner** 19:02 Yeah, allocation size pages in this case, yes, but for simplicity to read it here, I think it's easier, to call it out, yeah, but we.
**Christos Kalkanis** 19:11 I'll leave a comment in the document. I think it's best to be explicit here, like, because you're showing an example of the encoding, and this is misleading, essentially, but yeah, I'll add the comment to the document.
**Florian Lehner** 19:26 Yeah, I just want to have one question for Alexei on the, on the second approach, so, changing… the protocol.
Yeah, if we go this route, then… OTEL will probably ask about some conventions about units, and, do you have any information if there is any convention that PProf is falling for units, or is this just like, yeah, whatever you want?
**Alexey A** 19:59 I think there is… there's definitely convention for things like bytes. I think there's some kind of, like… I think there's, like, a fallback that if… If the unit doesn't match one of the predefined units, like bytes, or, what else? Maybe for… maybe time also? Like, there's, like, milliseconds, microseconds, then I think it falls back to Treating it as count.
But I need to take a look at… whether… We just say count explicitly everywhere, or someone actually is actually relying on that fallback and is specifying something else.
We definitely don't use this Ukum convention.
**Florian Lehner** 20:53 Okay, cool. Yeah, feedback on this would be really appreciated, thanks.
**Alexey A** 20:57 Okay, but I understand that if we introduce this… I understand that if we introduce this as a schema change, then… saying that, oh, and by the way, Piprov will put Whatever.
Like, it's… it's either, like, a signal level standard, or it's not. Or it's, like, it's, like, either a signal-level standard, which should have some rules, and people should follow them.
or this is a P-Prof local convention, but… and then it should be kind of documented and used as such. I understand the trade-off.
**Florian Lehner** 21:35 Yeah, makes sense. Thanks.
**Christos Kalkanis** 21:40 Alright, next item. Do we have Jonathan today with us?
**Jonathan Halliday (IBM)** 21:45 You do! Hello!
**Christos Kalkanis** 21:46 Oh, great.
**Jonathan Halliday (IBM)** 21:52 Yeah, so, I've been working on getting the Java SDK to… Talk profiles, and Specifically to interop with DevFiler, which, pretty much works.
Along the way, I came across a couple of issues, which I think, Need a little bit of attention.
Roughly, they're in the category of things we haven't specified, but probably should.
which I think is mostly going to be semantic convention work, so I noticed the back end kind of requires certain metadata, for perfectly good reasons.
But the spec doesn't. So, if you're in a bad temper, you can argue the, the backend is not spec compliant. I think the proper way to argue it is, the spec's not finished.
So, that's sort of one group of things. The other one is things where we don't play nice with the existing specs.
So the specific one I came across was the way we, specify zero encoding and null encoding for links is not compatible with the way that the, trace spec does so.
So there's… Probably some… some spec updates to go in there.
The payload one is sorted, I think.
I don't know if everyone's signed off on it yet, but… it's, it's queued up there. I think I'll probably queue up the link one next to it.
Doing the same thing of just saying, yep, it's here for review, but Don't merge it yet.
And we'll gradually build up a set of things that will merge in a batch down the line.
Yeah, Alexi.
**Alexey A** 23:51 So we, because the pull request for the payload as a dictionary, I think it had some note, like, do not submit, or…
**Jonathan Halliday (IBM)** 24:02 Yeah, so what I don't want to do is break, compatibility right now.
**Alexey A** 24:07 Oh, I see.
**Jonathan Halliday (IBM)** 24:07 We've just shipped the Alpha, and we're still at the stage of trying to get everyone on the same page and get all the things interoperating, and if we push a breaking update now, it won't be helpful.
So, what I'm… I'm thinking is we'll… we'll wait a few months.
Get feedback, and consider it, and then do a batch of changes together and put out, I don't know, alpha 2 or Beta, or whatever we call it, I don't know.
Don't know what the next step is.
But we'll essentially do all the… The potentially breaking changes at once, instead of… Drip-feeding them and being in a perpetual state of having implementations that are on subtly different non-interoperable versions.
**Alexey A** 24:50 Okay.
Is there a way to have some kind of, like, a branch where we would still merge this, but then, like.
batch merge, because… depends on how many changes like this we have, but I just imagine if we have, like, 15.
**Jonathan Halliday (IBM)** 25:03 Yeah, yeah, potentially everything's gonna need rebasing. I mean, fortunately, the product stuff doesn't move that frequently. We're by far the biggest cause of changes in there for the last few months, I think. Everything else is sort of stable. They change the comments occasionally to clarify things, but they're not changing message types.
**Alexey A** 25:24 I mean, even for the profile, for our own.
**Jonathan Halliday (IBM)** 25:28 Yeah, potentially. I don't know how to do branches in the OpenTelemetry profile repo. I don't know if they're a thing.
**Christos Kalkanis** 25:36 I think we don't have the permissions to create the brands there. It has to be on your personal phone.
**Jonathan Halliday (IBM)** 25:41 homes.
**Christos Kalkanis** 25:43 Yeah.
maybe… I'll reach out to Tigger, and maybe we can, I don't know, get an exception for that, or maybe we can think about Make a separate enforcement.
**Jonathan Halliday (IBM)** 25:53 Not as helpful as it appears, because, Certainly what I was finding when I was working with the Java SDK is it's very tricky to get the downstream things, like the SDK, to consume anything other than the official… release of the… the Proto repo.
That might just be a problem with Java, because what happens with the Java one is there's an intermediate artifact that is the Java Stubbs built from the protobuf.
But I suspect it's a problem for other things as well. You basically have to branch everything downstream of it as well, and get that branch to consume the branched version of the proto.
Sweet.
Yeah, it might be nice to try it, but I suspect it's, It's gonna be more hassle than it's worth.
**Christos Kalkanis** 26:50 Okay.
Anything else?
**Jonathan Halliday (IBM)** 26:54 so, I'm sorry, I've jumped ahead a bit, because some of that was… What's coming up in the… The feedback and recommendations bit. But, yeah, as far as… existing… pull request is concerned.
Yeah, it's do not merge, but, please review.
**Christos Kalkanis** 27:19 Okay, thanks, Jonathan.
Alexa, you have the next stripes.
**Alexey A** 27:26 For the second, ISNTPR. This is about, improving the… documentation on, period type and period, please, take a look. Basically, it adds… we had this discussion that period type that can be different from sample type, and when this can be the case, so I added A couple examples for that.
One… thing I was… thinking about when, when, when writing this, oh, I saw… Oh yeah, I think Florian had a comment, I think he responded to that, and… One thing I was… I was wondering, do we have cases where period can be empty?
like, there is no period, and should I add an example for that? But I couldn't come up with, or with… any sort of, like, canonical case for that that I know about, so if anyone… Knows of collections where… We wouldn't have any period. Please comment and we can add it.
**Florian Lehner** 28:46 I think it's hard to add a period for off-CPU profiles, at least how we emit it at the moment with eBPF Profiler, because the time between off-CPU profile samples is not constant. It's changing between… between samples, and that's why I think it's hard to set something to a specific value, where the value in period does not reflect the actual off-CPU samples.
**Alexey A** 29:17 Does it record every off-CPU event, or.
**Florian Lehner** 29:22 No, it does a downsampling of CPU sample, events, because if you would take every off-CPU event, this would overload, the system.
**Frederic Branczyk** 29:34 Right, and I think the last time we talked about this, we said that we can… Infer an average number of events between sample events.
That's what I recall.
**Florian Lehner** 29:46 There was an open discussion, but no conclusion.
**Alexey A** 29:52 Okay. Yeah, I thought that if you… if this downsampling has fixed rate, for example, it's every 1000… 1000th… Oh, okay.
**Florian Lehner** 30:02 It's, not every 1000 event, but more like, a probability, how likely you are take something. So, it's… sorry, it's not, sampling based on, on, on a frequency, but, based on, on a threshold. So, you, you set a threshold.
Where you want to have, off-CPU samples, and, whenever we see a off-CPU, potential event.
we take a random number, and if the random number is above or below, I don't remember exactly, don't put me down on this, but, based on the threshold, we then take it. So, that you can say, hey, I get 10% of, of CPU samples, or, I set it, I think, to… you have to define a set of value between 0.0 and 1.0, where 0.001 means 1%, and 1.0 means 100% of CPU events.
So it's, probability, not, not, a count that, is sampled on.
**Frederic Branczyk** 31:19 I'm not a statistics expert, but, like, intuitively, statistically, that's the same thing, no?
Like, on average, Over a large distribution, the.
**Florian Lehner** 31:40 I… I would not agree…
**Frederic Branczyk** 31:42 The distance between two samples is gonna, on average, you.
**Florian Lehner** 31:46 No, because we… there is an unknown of the… of the scheduler that we don't know. There can be workloads where the scheduler is not interrupted, and there can be workloads where the scheduler interrupts quite often and heavily because of I.O, maybe, or lock contention. So, this can… scheduler can introduce a high variance on this.
**Alexey A** 32:15 But that only affects the number of events, not the… not kind of, like, the rate.
at which you… sample. Like, basically, if you send… if you set the probability at 30%, and then you, like, throw a coin on every event to decide whether you sample it or not.
It's still, like, 30 in 100, basically.
So, the period is kind of like 10 over 3.
**Florian Lehner** 32:44 Right, agree.
But, you don't have any judgment on how often the scheduler will make this call if there is an off CPU event. It can happen way more often, depending on the application, or it can happen way less.
If you set the nice value, for example, for an application, it will maybe happen less often if you say, hey, provide this application with more CPU resources, or… there… I think there's a huge unknown in this case. That's, for example, why the eBPF profiler does not set a period at the moment for… of CPU profiles.
If this makes sense.
And, yeah, the comment I wrote on this PR is based on how we, at the moment, provide data in eBPF Profiler, because we set, 1 to the power of 9 divided by the sampling frequency as the period, and, yeah, that's… That's why the question to try is, hey, shouldn't it be 1000 divided by 10?
In this case, where we have a sampling rate of 10 milliseconds.
I think there was a previous discussion, but I don't recall it properly.
**Alexey A** 34:16 Okay.
One… one thing that we… I should also add… I think we should document more explicitly, is that This field is informational, and all profilers should record unsampled data. Because I think historically, at least in PPROF, And at least a long time ago.
Some profilers would put the data that were… basically, for example, like, the metric would be the sample count, and then period would be X milliseconds, and it… and the consumers would have to sort of, like, multiply to… to get the unsampled value, to get back the inflated value.
One thing we should document, I think, is that All producers should put Already, like, unsampled values, and this field is purely informational, like, it should not be used for any computation by consumers.
**Nayef Ghattas** 35:13 I'm not sure that's possible today, because we can either set the sample value or a number of timestamps.
And when we set the number of timestamps instead of the sample value, we have to rely on the period. I think that's what the eBPF profile is.
**Frederic Branczyk** 35:28 Yeah, exactly. I was just gonna say the same thing. And I also don't see a harm in that.
**Alexey A** 35:36 What, what's the, what's the case?
**Frederic Branczyk** 35:39 like, the eBPF profiler reports, like, the sample type is count.
And the period type is, CPU nanoseconds, I want to say.
And then any consumer, you know, either at ingestion or at query time, needs to multiply the count with the period to get the… Yeah.
actual CPU time.
**Alexey A** 36:08 But I thought we had… I thought we have an encoding where you can specify… Can you… can… I need to take a look at the.
**Frederic Branczyk** 36:17 Well, I… like, based on the protocol, both are valid things.
And I think that's… okay.
**Florian Lehner** 36:31 Yeah, we have either, only timestamps, we have only values, or timestamps and values.
That's…
**Frederic Branczyk** 36:41 I think that's… I think that's kind of a separate, separate thing.
the timestamps.
**Nayef Ghattas** 36:46 I think there's a comment before the sample that explains the… The different setups that we support.
**Alexey A** 36:55 One… one reason, for example, why we, in some of our profilers, we came to, to, like… Make sure that it's unsampled in advance, because the sampling rate can change.
And then, assuming that there is fixed sampling rate is… is… can be brittle.
So… like, maybe we can allow different things, but I also… I wonder if it's… if it makes sense to document the implications and the… And, and sort of recommendations.
**Frederic Branczyk** 37:29 I think a recommendation I wouldn't be against. On the other hand, I think, you know, it feels like we may be making recommendations based on abilities or inabilities of some backends.
**Alexey A** 37:54 Yeah, I don't want to get too kind of, like, meta in the discussion, but one thing, I think one thing that is good about recommendations is that when people see them, and they're more likely to give feedback, they're like, hey, I have a use case which doesn't fit the recommendation, so… Let's… rather than, like, just quietly invent creative ways to use the protocol, but… But I don't know, like, maybe this should be not in the protocol, but elsewhere.
Like a separate document or something.
**Frederic Branczyk** 38:27 I think… I think that… I think this is the right document for this.
I feel like if we… if we keep, if we, like, distribute recommendations through a bunch of places, I don't think people are gonna naturally find them.
**Christos Kalkanis** 38:44 So, I thought that we had, what Alexey mentioned previously, that we recommend the producer store and sample values. I thought we had it somewhere in here, but I don't see it, maybe… Because when I created the data format, markdown documentation, it was brought up there. Maybe it's actually… pending in a different input request, so I will have another look.
Yeah, but right now there's nothing… this is the documentation, for example, we don't specify, like.
either of those things, like, there's nothing related to unsampled values in here.
**Alexey A** 39:26 And why… sorry, just… just a curiosity question. Why BPF Profiler chooses to, like, put the counts, but then put the period… like, why… why not put the actual period in the samples? Sorry, I'm probably missing something simple.
**Florian Lehner** 39:41 We differentiate, at the moment, two cases on CPU profiles. For on CPU profiles, we, if I remember correctly, just report, the timestamps.
And for off-CPU profiles, we report the values and timestamps combination. So, looking at the report of stack traces, we have the first and the third option that we have documented here.
Yeah, as I said, for the on-CPU profile case, we set the period as, 1 by the power of 9?
Divided by the sampling frequency.
And for off CPU profiles, we don't set the period.
That's… that's… that's the current situation.
**Alexey A** 40:32 Okay, so… so essentially what eBPF Profiler does, it's the first case of what's shared on the screen, but instead of, like.
but it doesn't feel like… currently, we say consumers must assume the value is one for each point, but either there should be up… like, we should resolve this, because what it… what ABBF Profiler says, like, it… it basically doesn't treat it as must, and it's… it instead, like, treats the period as the wait.
**Nayef Ghattas** 41:05 That's because the profile type is account.
Like, if it's a sample count, a sample count of 1 is a sample time of period.
**Alexey A** 41:18 I mostly mean that this phrase of, like, consumers must assume the value is 1 doesn't apply today to the eBPF Profiler, and we need to resolve… we need… we need to resolve this.
**Florian Lehner** 41:29 I think it applies to the eBPF profiler. We assume that every timestamp has a count value of 1.
**Christos Kalkanis** 41:39 No.
**Florian Lehner** 41:40 We saved it.
**Christos Kalkanis** 41:42 Is that… So that would… I think Frederick mentioned previously that there is another calculation that's being done, right? So you multiply the value with the period. If that's the case, then… we… the value, essentially, is not 1, right? This is not evident from this, like, what we document here, essentially.
Like, there's an implicit assumption hidden in here.
**Alexey A** 42:13 Yeah, to me, it sounds like we need to either, like, maybe document this all in one place, or at least make it clear how… basically, how these values and timestamps play with period, if some of the producers and consumers do use them together, because right now, they are kind of, like, they're very separate, and it's not clear from the documentation that… period could be used for waiting for, for giving weights.
**Christos Kalkanis** 42:45 Yeah, true.
**Florian Lehner** 42:46 I might be wrong on this, but I think the EVP profile at the moment is correct in the sense that we provide sample and counts, and we don't make any assumption on how long the how long something was. So, if you would go into, for example, a wall clock profile, where we say, hey, we have a timestamp, and for this timestamp, we have the stack trace was on CPU for, I don't know, 3 milliseconds, whatever, just as an example, then we have to go to the third representation, where we say, hey, this is the timestamp and the respective value, but, it's, I think, independent of the period. The period is just… What's the estimated… time of collection, not, not, not, it… it does not require a calculation in the backend, I would say.
**Frederic Branczyk** 43:43 I don't think that this is, like… per, like… accurate when comparing to other profilers, right? Like, I guess, like, what Alexei was referencing was that the, like, Go built-in profilers, they produce both, right? The count and where the sample type is count and a profile that is sample type, CPU nanoseconds, right? And the CPU nanoseconds is literally just the same thing, just all values multiplied with the period.
So, like…
**Florian Lehner** 44:15 The VBF Profiler does not provide this at the moment.
**Frederic Branczyk** 44:18 Sure, but, like, It provides enough information that the backend can do the same calculation.
And that's what Alexei was saying, that, like, we should make a recommendation whether a profiler should report account, or as sample type, or if it can.
report a, you know, CPU nanoseconds, for example.
**Alexey A** 44:49 Yeah, to me, it's like, if I write a consumer, let's say, like, I want to write a UI that visualizes open telemetry profiles, then… Ideally, I would like to have an ambiguous way of just reading the spec, and reading the comments in the proto, and being able to do that.
And so, this is why I think, like, patterns and recommendations should be… should be listed. I can… I can take an AI on, like, taking a stab and trying to… put what I think we discussed into words, and then, and then we can… we can return to this topic. But I understand that the… like, the topic is expressing Expressing fixed… sampling period values when the value is not 1? Like, do you have a separate profile, or… or do you use period for… for that. I think we just, like, need to… document this better.
Like, I don't… I don't… I don't think the eBPF Profiler has to make any changes, but… To… to get convinced, I want to turn this into documentation text and get everyone agreed.
**Nayef Ghattas** 45:59 Should that be covered by semantic conventions for the sample type field?
Because right now we have a comment on sample type that says it can be CPU and nanoseconds of CPU and nanoseconds, and I'm assuming also CPU and count.
And for a heap profile, it says allocated objects count, allocated space bytes.
So maybe that's part of the… The thing that we should document.
Because I think it depends on what we've put on the sample type. Like, if we say we… the sample… when the sample type is CPU and count, can we rely on the period or not to deduce a nanosecond number from it?
or not.
Does that make sense?
**Alexey A** 46:52 I, I, I, I, I, like… how to use semantic conventions, it's… I… I cannot fully think that through, because… I don't know if we have, like, example of semantic conventions referring to a specific string, because I think it's usually… like… fixed.
Value, and, like, how exactly this would encode the Period. This is, like, some kind of, like, meta-information that is attached to… To the specific name of the… sample type, which says use period, or don't use… sorry, I, I, sorry, I cannot fully think this through.
**Nayef Ghattas** 47:33 I guess what I'm saying is that maybe we should document in semantic convention the different types of sample type that are supported.
And when each sample type is used, what does it mean?
I think so far…
**Alexey A** 47:51 Do you mean, like, the actual names of sample types?
like, CPU, off CPU… Hmm.
**Nayef Ghattas** 48:00 nanoseconds, just count, what are the units that we're using, and how those units refer to actual data. For example, CPU and count, what does it mean?
**Christos Kalkanis** 48:18 Should this be…
**Alexey A** 48:18 Maybe… okay, sorry, go ahead, John.
**Christos Kalkanis** 48:21 should this be part of semantic conventions, because semantic conventions will tie us down to specific encoding. We may be… because we have something similar for the, for example, the build ID algorithm that we use, so that's not part of semantic conventions, that's part of the specification. So maybe we could make it part of the profiling specification.
We have precedent there, and we can clarify like, what all of this mean. And I agree with Naev here, because, like, I've always found this bit here problematic, in the sense that it relies on implicit knowledge, mostly from Piprov.
Like, if you're coming to profiles, and you don't have that context, you're completely lost here.
You have no idea what value to use, you know, what this value means, and how to combine it.
I think that's true.
**Frederic Branczyk** 49:09 I did just realize what the right… period type for off CPU profiling is.
We just can't represent that period today. It's probability.
**Christos Kalkanis** 49:23 Right.
**Frederic Branczyk** 49:24 We just can't represent the float today, and… in the period value, which is maybe something we need to fix, I don't know.
**Alexey A** 49:41 I think in one of our profilers, we had a unit called millibytes, because we had to put fractional byte values.
**Frederic Branczyk** 49:48 I was just gonna say, I don't know that I love, you know, you know, like.
one, like, n in a million or something. I suppose we could do that, but I don't know if I love that.
I kind of like that the probability is now a float of CPU profiling.
I feel like, I guess this is, like, going back to the original point, I feel like there is always a correct value of period type.
I think maybe we just don't have enough of a… Enough flexibility in the protocol to… represent everything.
**Alexey A** 50:39 Okay.
Yeah, I think I… I have enough information to make some incremental progress, but we will probably discuss this more.
**Christos Kalkanis** 50:57 Okay, yeah, we're running low on time, let's… move on, I think… so, Felix is not with us today, we can skip this. The next four items are mine, just a quick update. So, a major change is that Ignore requested in the data format per request.
So we have approvals there. The thing is, we need another approval from the TCE for the… specification for a request to be merged, and I'll reach out again to people.
And then… I opened a pull request against the Proto repository, so that's making some documentation changes that stem from the data format work. Alexei has already approved those. I've asked Jonathan to also take a look, but yeah, all of you, feel free to take a look as well. It's just clarifying a few things, and so on.
And then, Alex, you have the last item.
**Alexey A** 51:52 Sorry, didn't, look into that yet.
**Christos Kalkanis** 51:58 I think we discussed this in the last meeting, and the… consensus. I think Tigran mentioned But we cannot delete this.
We cannot delete the previous specification that we had, like, it was an OTEP. We can leave it there, but we can mark it deprecated, and then once this is merged.
Maybe we can have a link to this instead.
**Alexey A** 52:26 Okay.
That sounds good.
**Christos Kalkanis** 52:32 Alright.
**Alexey A** 52:33 I have a quick, quick question on, the documentation. We also have some documentation in the, in the profiles, in the proto itself.
**Christos Kalkanis** 52:45 Yeah.
**Alexey A** 52:45 including the diagram for these cardinalities, like 1 to N, N to N, and I remember we had some discussion about that in your PR, if I'm… Should we, should we make the same updates in the, in the, in the proto itself?
**Christos Kalkanis** 53:01 Yeah, so that's… that's the pull request I've opened in the Proto repository, so it includes the changes to this…
**Alexey A** 53:06 Oh, it includes… oh, okay, okay, maybe it's actually… maybe it's actually this diagram, not… not… not some other one. Okay, I thought we had, like, we have, like, a separate… copy of.
**Christos Kalkanis** 53:15 Yeah, yes, we have the diagram also in the markdown, so there's a documentation page, right, on the OpenTelemetry specification, so that essentially gets this ASCI diagram and turns into a mermaid diagram that's rendered as a graph, looks better, and so on. So we decided to tip it, because it's nice from a kind of visual Architectural point of view.
But what I did is… I removed all the tables, which just essentially regurgitated the fields of the proto, so now I'm just linking straight to the proton. Then the consensus from the last meeting, I think.
Tingaran mentioned, and Felix, that let's keep the proto as the source of truth, in terms of Okay. Documentation for its field, and so on. And then we can use the Markdown specification profile documentation pages to either add examples, you know, for this visual graph that Shows all the different parts of the proton and so on, and the introduction, and, you know, explaining the things we did differently, such as the dictionary, and so on.
But keep the low-level technical details, especially the field documentation, in the proto, and have that as the source of truth.
Alright, yeah.
I guess we can… we have 9 minutes. I don't know what we get to discuss.
So, Felix has the first item. I think we've already… Discuss those.
**Nayef Ghattas** 54:52 Yeah, yeah, I've been, those are the notes from the review action items, I've been filling them up.
**Christos Kalkanis** 54:57 Oh, great. Thanks.
Great.
**Nayef Ghattas** 55:01 I think the only thing that we didn't discuss was Ivo's last item.
I don't know if Evo's still here.
**Ivo Anjo** 55:15 Scott opened that PR, and we're discussing with the OpenTelemetry Rust folks.
**Scott Gerring** 55:29 We'll get there soon.
**Christos Kalkanis** 55:37 That's nice.
Ivo, do we have any updates around the… thread context. I know that it's under review right now. I think Tigran pinged all of us, the maintainers, to… because I think he has no approvals from any profile maintainer at this point.
Maybe you can give a quick update?
**Ivo Anjo** 56:04 Yeah, we've gotten some feedback, I believe Scott is kind of, like, replying to most of the things there, and yeah, so it's a bit, like.
Throw more feedback at us, and we can address more feedback.
**Christos Kalkanis** 56:21 Okay, great, so let's… let's all, have a look there. Yeah, we got process context in, so now thread context is the last one.
**Ivo Anjo** 56:29 Yep. Terra threads. The interesting part now.
**Christos Kalkanis** 56:40 Alright, do we have anything else to discuss today?
I guess not.
Alright, so, yeah, let's wrap this up.
Thank you, all of you, for attending, and see you next time.
Bye.
**Ivo Anjo** 57:03 Thanks, everyone!
**Alexey A** 57:04 Thank you, bye.
**Frederic Branczyk** 57:05 Thanks, everyone. Bye.
