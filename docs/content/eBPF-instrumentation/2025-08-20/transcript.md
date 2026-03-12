SIG: eBPF instrumentation
Date: 2025-08-20
Duration: 26 minutes
============================================================

## Zoom Recording Transcript

**Mattia Meleleo** 00:29 Hello.
**Tyler Yahn** 00:32 Hey!
How's it going?
**Mattia Meleleo** 00:35 Good, good. What about you?
**Tyler Yahn** 00:38 Yeah, also well.
Mattia, your time zone, are you, after dinner at this point?
**Mattia Meleleo** 00:49 Dinner, no. It's the 5 o'clock here.
**Tyler Yahn** 00:53 Oh, okay, that's not too bad then.
Yeah, I'm over here just starting my day.
**Mattia Meleleo** 01:04 Where are you from, Tyler?
**Tyler Yahn** 01:06 In Portland, Oregon, here in the United States. Oh, okay. Yeah.
**Nimrod Avni** 01:21 Hello?
**Tyler Yahn** 01:26 Hey, how's it going?
**Nimrod Avni** 01:28 I'm good, what's up?
**Tyler Yahn** 01:31 How much?
**Nimrod Avni** 01:34 Thanks for the late PR yesterday, or early, I think maybe it was early for you.
**Tyler Yahn** 01:38 Yeah, it's, I was just talking about that, yeah, midday for me, pretty much, yeah.
**Nimrod Avni** 01:44 It was, like, 10 or 2 p.m.
**Tyler Yahn** 01:47 Oh, yeah, yeah. What time is it there right now for you?
**Nimrod Avni** 01:50 I know it's 6, it's 6.
**Tyler Yahn** 01:52 Oh, okay.
**Nimrod Avni** 01:52 Yeah.
**Tyler Yahn** 01:54 Mattia was just informing us he hasn't even eaten dinner yet.
I'm also a….
**Mattia Meleleo** 02:00 Italy, we have dinner very late, at least here in South Italy. We have dinner at 9 or 10 in the evening.
**Nimrod Avni** 02:08 I ain't no time.
**Mattia Meleleo** 02:10 Yeah.
**Nimrod Avni** 02:11 When do you go to sleep?
**Tyler Yahn** 02:12 Yeah.
**Mattia Meleleo** 02:14 Very late.
**Nimrod Avni** 02:17 with Italy thing.
**Tyler Yahn** 02:20 Yeah, that's a Spain thing too, right? I've heard?
**Nimrod Avni** 02:23 I know, yeah, I know, so they also sleep at Dev Siesta, right? Or they sleep, … Do a nap at lunch.
**Tyler Yahn** 02:32 Sounds fantastic, yeah.
I like that idea.
**Nimrod Avni** 02:35 To get beds in the office.
**Mattia Meleleo** 02:40 We also have that, like, in South Italy, usually stores close after lunch, and they reopen at, like, 4 or 5 in the afternoon, but in North Italy, it's different, because they stay open all day.
**Nimrod Avni** 02:54 Maybe it's a tourist, or something.
**Tyler Yahn** 02:59 It's probably the heat, I think.
**Nimrod Avni** 03:01 Boom.
**Mattia Meleleo** 03:01 Yep.
**Tyler Yahn** 03:02 Yeah, I could definitely see taking a few hours off.
So I'm looking at the agenda, I don't have too much, I just wanted to maybe do a review of the open PRs. I know that, Raphael looks like he's gonna be running a little late, so, yeah, we can, we can jump in here, but if you have, agenda items you wanted to talk about… go ahead and add them there as well. If you haven't yet, please add your name to the attendees list.
Yeah, and then we can… We can just get started here.
Okay, cool. So to start us off, this PR has been on for a while, it's still on me, Nicola's out on vacation at this point to try to, reconfigure Dependabot to fix this. There's definitely a lot of security issues still, … Hopefully this resolves a lot of them, but, yeah. Still working on this one.
Let's see, Mark has just opened this one, I think, last week? So, this is using Test Eventually to try to fix the, … The testing failure? … oh, it passed. Yeah, the… Test for being a little flaky. It looks like this is actually ready to merge, so, unless there's any opposition, I'm just gonna merge this right now.
**Nimrod Avni** 04:32 Yeah, looks good.
**Tyler Yahn** 04:34 Cool.
Okay.
Awesome.
Okay, next up… Mateo, I think you added this one, this Kafka 2.8 and 4.0 integration test?
**Mattia Meleleo** 04:48 Yeah, I did some, some changes, like, for example, the Kafka spun name was not following the conventions, and I added some test coverage.
And some coverage for the newer API versions, … And today I fixed the failing test, the oats tests that were failing, so I think it's good to go, or good to review, at least.
**Tyler Yahn** 05:15 Okay.
Yeah, it looks like it just needs some reviews, so, if you're on the call, yeah, looking for reviews on this one.
It looks like it's, yeah, all ready to go. Okay.
I think we can jump on then. So, next up, Nimrod, you also opened up, Trace Exporter internal metrics, plus BPF Internal Metrics.
**Nimrod Avni** 05:36 Yeah, I think Mark, did a review, like, a couple hours ago, and … I mean, yeah, … Yeah, basically adding some stuff that were only… some metrics that were missing, and some of them that, like, were only via, like, internal, like, Prometheus, metrics that should be also available in also metrics.
So I added that.
**Tyler Yahn** 06:05 Okay, cool.
Well, it sounds like there's a little bit of feedback, I don't know, ….
**Nimrod Avni** 06:11 There's one, like, fix in something, and I think most of it is, like, discussions.
**Tyler Yahn** 06:17 Yeah, okay. So, this also needs more review, I guess, is the idea then, so if you have time, there's nothing blocking this, so please take a look at this and also provide some review.
Okay.
There's another one that says, do not review by Raphael, which… I guess we could just skip this one.
Also kidding. There's also this, ensure error is checked ASAP. I don't know….
**Stephen Lang** 06:46 That's mine.
**Tyler Yahn** 06:47 Steven, thanks. Yes, so, it looks like… We have a panic that this is addressing at this point.
**Stephen Lang** 06:55 This is only in the integration tests, so it's not anywhere else. And it just so happens if you delete the test output directory, you can get a segfault, because the It's, was just not checked.
Early enough.
But when I went to check usages of this particular pattern.
Turned out to be all over the place in the integration tests.
So, the changes are just to move, the error checking.
To be as close as possible to where the error is actually defined.
**Nimrod Avni** 07:27 So….
**Stephen Lang** 07:27 So there's no new, there's no new code here, it's just moving up of the require.noer.
To be, immediately below where it's, created.
**Tyler Yahn** 07:39 Yeah, that's, … this looks… this looks great.
**Stephen Lang** 07:42 So the only difference is, whereas before you'd get a segfault, now you get the actual Which says, you know, files not found.
**Tyler Yahn** 07:51 Which is preferable, instead of….
**Stephen Lang** 07:52 Yeah.
**Tyler Yahn** 07:54 Okay.
Yeah, this, this looks great. I think that was an easy enough one to review.
… Yeah, it also looks like it's ready to merge. Any other topics people want to ask questions about this one before I merge it?
**Rafael Roquetto** 08:11 Merge it.
**Tyler Yahn** 08:13 Cool. Alright, let's make in progress.
**Stephen Lang** 08:16 Right, thank you.
**Tyler Yahn** 08:18 Yep.
Well, yeah, thank you, as well, for finding that.
Okay, next up, Postgres, decreased log level to debug.
This is you again, Mattia, right?
**Mattia Meleleo** 08:30 Yeah, this, I thought this was happening only for malformat packets, but this happens also when the buffer is not big enough.
And with the default settings, it can happen very often, so the bug message is fine here.
**Tyler Yahn** 08:48 Oh, I see, yeah, because otherwise it's just gonna spam.
**Mattia Meleleo** 08:51 Yeah, yeah.
**Tyler Yahn** 08:53 Okay, yeah, that sounds good. It looks like, Raphael, I think you already reviewed this, so this looks ready to go.
Any other comment on this before I merge it?
**Nimrod Avni** 09:07 Perfect.
**Tyler Yahn** 09:08 Yeah, making a lot of progress today.
**Mattia Meleleo** 09:11 tanks?
**Tyler Yahn** 09:13 Yo, thank you again.
Okay, feature, log, config, JSON.
**Nimrod Avni** 09:20 No, this is from Nimrod.
Yeah, essentially, it's just, one of our clients, we wanted to… Just tell me if you think it's something that can be useful. Like, one of our clients, we wanted, like, to help them debug some issue. We wanted to get, like, the config… the exact config they're using after all the, like, environment variables, default sending, all that stuff. And when you print it as YAML, most logging, like.
logging, systems, and, like, they just capture logs line by line, so you don't actually see the full config as one log, you see it as… tons of logs when we print it out as YAML, so I made, like, a setting to the already existing log config to print it out as JSON, so you can view it as, like, a singular line.
And yeah, it's, it's not… Man, it's, it's kinda either just, like, I marshal it to YAML, and then from there, re-marshall it to JSON.
Tell me if you think it's something that's… maybe, like, help debugging issues when you don't have, like, I don't know, like, the actual cluster that you run on for, like, customers and stuff.
**Tyler Yahn** 10:34 So why… why Marshall it to YAML at all? Why not just go straight to JSON?
**Nimrod Avni** 10:37 Because I actually did it at first, and then Mattia suggested, for that, we need to, like, annotate all the… all the config with both YAML and JSON annotations.
And you need to remember to, like, every time you write, like, a YAML martler, you need to write the equivalent JSON marshaller and all that stuff.
And that's, like, as far as, like, performance, it's, like, only once at the start, so it's not very, … And it's only, like, when you specifically say to do it in debug.
**Tyler Yahn** 11:08 Yeah, I gotcha. Yeah. That's kind of unfortunate we… use YAML-specific features, you can't just do that, but okay.
**Nimrod Avni** 11:16 Maybe if you have another idea, like, I don't know a better idea to do that, the side.
**Tyler Yahn** 11:20 No, I… you're probably right. Yeah, I'm sorry, I just, … yeah, I… because YAML is a superset of, JSON, so… It's kind of… like, I just thought you could just go straight to it, but yeah, you're right, like, if you don't have, you know, field tags or something like that set up, then this could just get really wonky pretty quick, so… okay, that makes a lot of sense.
**Rafael Roquetto** 11:41 maybe, maybe if I can suggest, just add a comment, a small one, just, with this context, so, like, next person who stumbles in the store don't, doesn't, like, go like, why, why? You know, because it's not obvious, but yeah, makes sense.
**Nimrod Avni** 11:54 Yeah, I can lay the comment, for sure.
I'll do that.
**Tyler Yahn** 11:59 Yeah, cool.
This is great. I like the idea, though. We also have this in the auto-insertation where it's on online, which is really annoying, when you do this, but you can take this and pretty print it any way you want. So that's way better than trying to figure out where in the logs, this ends, I guess. So yeah, I like that.
Okay, cool.
Alright, so we'll wait for the update on it, and then, more review.
And then this last one was just, a dependency update, so… Not needing for review here.
Cool. Okay, with that then, that is… all this stuff I had on the agenda. So any other topics people wanted to talk about?
If not, we can also end it early here.
Yeah, any cool projects? Also, I'd like to ask about that. Any cool projects? Maybe you guys have been using this? I know, Nimrod, you had been looking at, instrumenting that whole, EP… or, I'm sorry, the hotel demo.
I'm guessing probably a lot of other things going on. Any cool projects along those lines, or anything like that?
**Nimrod Avni** 13:15 We tried, like, the issue that, the PR yesterday was a very interesting one. That's why, like, that's originally why we tried to insert all the internal metric. We thought it was, like, a PPF issue, and it was really hard to debug the signal thing.
Yeah, but that was interesting.
Yeah, I think maybe we can talk, since we, like, have a lot of time. If anyone wants to talk, we and, like, me and Mattel, we had some plans. Maybe it's gonna be more in the future, but, like, plans of something that we want to do.
is to, and a lot of customers have been asking for us, is basically, trade… I think someone also opened an issue in that.
Which is, like, trace-to-law correlation. Basically, correlating, like, logs from the application with the trace and span ID from OB.
… And we're trying, like, we try to think of, like, … because we're not… Lobi doesn't actually send the logs.
It just, like, it sent only the trace of the metrics, so we thought, like, maybe… Like, our idea is maybe somehow to, … let's say the simplest thing is, like, if it's, like, JSON logs, we can somehow, … kind of capture when we try to print a CD out or something like that, trying to print, … print, like, see if it's JSON by some heuristics, and then, like, correlate the BPS, like, the transparent context that we save in OB based on the process.
… we didn't, like, we didn't do, like, too much digging around on that, but it's something that might be interesting, and if anyone has, like, any… thoughts about that? We can, like, I don't know, open some discussion? It'd be interesting.
**Rafael Roquetto** 15:02 I know that Nikola was… skinny on doing something like that, or wanted, so it's… it's good. The guys are… are… you know, curious about that, and I think, his idea was pretty much what you… what you're saying, which is, like, maybe tap into, you know, the STD out and try to see what we can get, yeah?
….
**Nimrod Avni** 15:26 Yeah, I think for text logs, it might be, like, way more complicated, because you need to not destroy formats, and, like, detect the format somehow dynamically, and all that in BPF.
Not sure how we'll do that.
At least you're gonna give me a good start.
**Rafael Roquetto** 15:40 Or, I mean, if you want to keep it simpler, I mean, I haven't thought about it at all, so forgive me if I'm fucking shit, but … I guess one of the premises we were discussing is that if… and that's the problem, might not be true at all, is if a service is printed into STDR, it's probably logged.
And if it's printed just the error is probably errors. So, you might not even want to parse the JSON, I don't know, and just assume that this is, like, the process output is what you're interested in, and then… and then maybe, in user space.
You want to categorize that, if it's, you know, get that as JSON, because, especially, I don't know how you intend to tap into the STD out, but if you're gonna use a K-probe.
depending on where you put it. Performance issues aside, let's… don't worry about that.
you might not get, like, the entire JSON, or whatever, log, string chunk at once, it might be fragmented, and then you would need to reconstruct that, and that might be more a pain in the ass than just saying, hey, this is what this process is outputting, is this a logger? No, do we care? Like, can we just… I mean, I don't know, maybe there is some… like you said, if you see something that relates as… that looks like JSON, you don't even need to be parsable. Maybe you heuristically classified these, oh, this looks like a log, maybe I'll ship it Somewhere, … But if it doesn't, you drop it, or you just ship everything, make it configurable, I don't know, you just think about it. So the interesting thing is also….
**Nimrod Avni** 17:17 do we want Obi to be the one responsible for sending those logs? Like, do we capture from STDL and then send ourselves? Because the hotel collector usually does that stuff. We thought maybe we can only, like.
But that's the issue, then we can't, like, collect it to user space and categorize it. We need to do, like, all the kernel space, add the context, maybe with some, like, BPF probe right stuff.
Cool.
Like, if we decide to send the logs, we need to tell people, turn off log collection, and the collector will be responsible for sending the logs, but then it, like, causes load, and….
**Rafael Roquetto** 17:53 Yeah, no, you're right, you're right, I don't think that makes sense. So we just want to correlate, and we need to tag this correlation somewhere. I mean… Riding to the… Right? Tagging the log? It's gonna be… tough.
**Nimrod Avni** 18:09 Because….
**Rafael Roquetto** 18:11 I wonder if there's another way, I don't think there is, but I wonder if there is another way that we could be smart about it, like… maybe, again, take this as a block of salt. Instead of tagging the log, we can send some metrics somewhere that kind of… that we can correlate at a higher level, saying, okay, at this stage, this… this… around this millisecond, when the program outputted this string, this is a log, and then later we can tie it together at a higher level, instead of trying… I don't know if that will work.
Because I don't know how we're gonna write the law, like, tag. If you use BPF probe rightUser, it will work for, only… a subset of… use cases, I guess. A lot of people are running with lockdown kernels that… you know, that's not, … that's not available. Like, VPF Pro Revisor's not gonna work, so… I mean, it will work, but I don't know. Just something to bear in mind with that….
**Nimrod Avni** 19:10 No.
**Rafael Roquetto** 19:10 liberal.
**Nimrod Avni** 19:12 Interesting.
**Rafael Roquetto** 19:12 Yeah, but I don't have a better idea, so… not very helpful.
**Florian Lehner** 19:17 I don't know how the story looks like for OB into the… for the integration into the Auto Collector, but I think from the profiling side, we have Where we face a similar issue. We want… to combine something that we connect, get from eBPF space with logs, traces, and metrics.
And, … Yeah, we extract process context That is, at the moment, not, in the scope of hotel semi-conventions.
So we can… we can extract this, we get the information, we have the information, but we cannot report this and then correlate the information. The first thing we do at the moment is using labels. For example, if you think about, PPROF, In the context of pre-prov, where labels are often set, labels can be quite interesting to follow, stuff.
And we want to, report these labels. At the moment, it's not possible. The same goes for span and trace IDs. We want, or we can.
Not yet.
But, we will be able to extract spam and trace IDs from the process, and, attach them to the protocol information, and then, based on the span trace ID, the hotel collector or the hotel part should be able to correlate the information, but, … Yeah, it's a long road. We just managed to get into Ulti Collector, so….
**Nimrod Avni** 20:51 ….
**Florian Lehner** 20:52 Yeah, and then resource attribute… … Enrichment is another level.
**Nimrod Avni** 20:59 No.
**Florian Lehner** 21:01 Yeah, but interesting to learn that you're facing similar issues.
**Nimrod Avni** 21:07 Yeah, so… I'm not sure how we… I guess we'll do some exploring of, like, if it's… how possible and how permissive it is if we, like, either edit logs in place, or we kind of decide that we overtake the log reporting. I don't know. I guess we'll need to see.
**Florian Lehner** 21:27 You know, what we did learn is that, what differentiates profiling from the rest of OTEL, and that's probably the same for Obi, is that our solutions operate, as Demon said, on systems, and not sidecars. And, if we write out as a sidecar, like every other solution is doing for hotel, then we blow up the auto collector, because not everything will fit into memory. That's why we have a, I would say, kind of special profile.
profile protocol, and we deduplicate a lot of information. That's probably the very same for you. You will often write the very same information and just increase significantly the data you transfer over the buyer.
So, but yeah, that's… I think that's a general, … Open telemetry issue.
**Nimrod Avni** 22:30 Yeah.
**Florian Lehner** 22:31 Sorry for the sutrix.
**Nimrod Avni** 22:33 No, it's all good.
Total.
**Tyler Yahn** 22:35 Yeah, no, that's really interesting. Thanks for the info.
**Rafael Roquetto** 22:39 Would it be possible to correlate based on timestamps?
like… You know, the log has a timestamp, we don't touch the log, but when we push the traces, it has a timestamp on it, that then you can… you can see the timestamp of that span of the trace, and then you can kind of correlate it with that. Like, I don't know.
**Nimrod Avni** 22:59 I think there's, like, yeah, there's, like, a couple of methods of, of, like, correlating different, signals, I don't remember the name, yeah, signals. Like, you can do either, like.
time-based, and I remember we also, like, we thought about in CoreLogix, about, like, trace and profile correlation, like, like, for when you talked about, like, it's either you do it, like, based on time, but that might be… not super accurate, because it's time, like, what, on the time of the pod? It's like a range, but, like, if you do a range of time on the pod, then it can be, like, multiple different threads and processes, and, like, each one is a different trace.
And if you have, like, the exact, like, correlation in place between, like, … and I saw there's no, like, specific convention for, like, trace-to-log correlation. I think in JSON, you just put trace ID equals something, log ID equals something, and you expect it to kind of work. I think that's most, like, how, … like, instrument… like, logging instrumentations of OpenTelemetry do it. And if it's free text, I'm not sure if there is any convention. Maybe it's like, if you do Log4J, it's like that. If you do whatever, it's like that.
**Rafael Roquetto** 24:11 ….
**Nimrod Avni** 24:13 We can do it, like, based on time, but I think that's probably each, you know… Each, … each system that stores, like, the telemetry data kind of needs to implement that, context based on time, but if you have, like, hard context of, like, trace and span on each, like, log event, that's, like, the best correlation, because then you can, like, jump directly from the log to the trace, for example.
**Rafael Roquetto** 24:38 Right. I wonder if you could do something like… When we see the log.
… maybe that's not gonna work, but probably not, but you actually create a hash of that string, and then you store that hash And then… And then you, you, you correlate That has to… to a trace ID, for instance, and then later on, when you see the log, you can rehash it again and bring back the correct… I don't know. I'm just thinking of ways… because you're right, otherwise you need to tag the log, and I don't know how we would do that reliably.
Maybe that's the only way, I don't know. Like, riding, but… Anyhow.
**Nimrod Avni** 25:23 Yeah, just something we thought would be cool to talk about, and if you have any ideas, … No, talk to me, because we're looking.
**Tyler Yahn** 25:33 Cool. Well, thanks for bringing it up, Nirad. Yeah, I love these little side project ideas, so it's a great place to talk about it.
But yeah, if anyways have more… conversation. Also, to people watching the recording of this, yeah, hit Nimrod up, and … Keep the discussion going.
Cool. Alright, well, if that's the case, I don't… let me double-check the agenda, in case anybody added something. Nope, nothing's been added there.
We can probably end the meeting early here. Thanks everyone for joining, appreciate your time. I'll see y'all in a week's time, and we'll keep on working.
Bye, everyone.
**Mattia Meleleo** 26:12 Bye.
