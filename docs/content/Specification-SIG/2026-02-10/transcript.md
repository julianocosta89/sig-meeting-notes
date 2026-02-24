SIG: Specification SIG
Date: 2026-02-10
Duration: 70 minutes
============================================================

## Zoom Recording Transcript

Ted Young 00:01:49 Yo.
Carlos Alberto Cortez 00:01:53 Hey, hey, let's start… let's start in 1 minute, maybe 2, I think it's only 1 minute past.
the hour.
let's wait for more people to join. We have 9 people, 10 people now, which is great. It's just…
wait a little bit. In the meantime, as usual, please add any important items to the agenda. We have a few items already, but in case you're missing something, please add that there.
Also, don't forget, too, that if you have something, it's very helpful to have
The, the time that you think it will take for your item to be discussed.
One minute, we can start.
Ted Young 00:03:00 Austin, I see you've got a big, important topic, and we've got a number of, like, little things. Should we, like, rearrange…
Austin Parker 00:03:08 Thanks, good.
Ted Young 00:03:09 Total announcements done.
Austin Parker 00:03:11 Yeah, probably put the little things up first.
Carlos Alberto Cortez 00:03:15 You just came… Excuse me.
If that's okay, let's do that. Yeah.
I will move it there, then. Let's try then to stick to the time that we have for each item, so we can make, you know, make room.
Okay, let me share my screen in that case, we are 3 minutes past the hour, so I think we are ready to roll.
Wait, I forgot to repaste that at the end.
There we are. Okay, let me share my screen now.
Okay, let's do this. Okay, thank you so much for joining, EVO. First item, disclose the next steps for, PR for the… for the 719.
Ivo Anjo 00:04:08 Yes, hello, so I, we've been discussing that, like, from time to time, and, we've already, like, in this OTEP, we've already been iterating on the feedback, and, like, got… I think, the people from the Profiling SIG are kind of happy with the current state, so…
And also got some feedback from the Java and the Rust SIGs, so kind of the big question is.
What's kind of…
What are the next steps to, to, to, that, that, for me to look into to kind of get this merged in?
Carlos Alberto Cortez 00:04:48 So, we need more reviews, from the hotel side. And this, I see a few approvals here, so they mostly from profiling, I'm guessing, which is great. So Josh has one approval, we need one more.
I see that Tigra and David and Robert already provided some feedback here. It would be nice to have,
We need one more approval.
So, basically, we need more, more reviews.
Do we have Tigran, Robert, or…
David, in the call, maybe you can comment if you have time this week for reviewing, again.
Tigran Najaryan 00:05:24 I'm here, but I haven't had the chance to take another look at the PR. I'll see if I can find time to do that.
Ivo Anjo 00:05:31 Thank you!
Carlos Alberto Cortez 00:05:33 Yeah, let's hope this week, yeah, you get more and more feedback. Yeah, it's… it's a good sign that you have some reviews here on this site.
Okay, that's all for now, so yes, if you haven't, please also consider reviewing this, PR.
Okay, moving on. Teth, hotel block, please.
Ted Young 00:05:55 Yeah, we'll have a much more in-depth report back coming soon on the blog.
But we threw Hotel Unplugged last week in Brussels. It was a lot of fun. It was a unconference, so basically a way for us to come together as a community in person and host a bunch of sessions.
with topics that we decide on the day. People really enjoyed it, had about 120 people. We'd like to throw another one in North America, in not the United States.
Thinking about Canada, Vancouver in particular, because it's so close to the Bay Area and Seattle. So there seems to be a lot of interest in that, but we don't know exactly when, in the year to aim for that, so we'd love, you know, feedback from people.
What time of year would be good?
But you'll hear more from us in the future, just letting you know.
That's all I got.
Carlos Alberto Cortez 00:06:59 Any comments on that front?
Okay, thank you so much for the update.
Yeah, it's great to know that there were… there were 120 people, that's always good. It's a good sign.
Okay, moving on. Jack, please take a look at the system packaging project proposal and consider participating. Let me open the PR.
Jack Berg 00:07:21 Yeah, this is, I just wanted to pitch this new community project proposal, from Mikel, and basically the idea here is to take the various components that
OpenTelemetry has created things like the collector, the auto instrumentation projects, the injector, the eBPF tools, the eBPF profiler, the eBPF Auto Instrumentation solution, and package them up into RPM or DBN packages.
And then to create a sort of meta package, you know, the OpenTelemetry package that would allow you to have a one… a single command install, to install OpenTelemetry on a Linux machine.
So if you can think about what this kind of means, you know, there's a lot of decisions that have to be made, about sort of things that, like, you know, the package topology, and what it means to install open telemetry, and what the defaults are for that. And so, you know, I have this comment here on this, on this community issue, where I basically am saying that I think the success of this project is going to depend on broad participation.
From contributors to all the different components that are going to come together into this sort of open telemetry package.
folks from the collector, folks from the language SIGs, etc. And so, this is just me soliciting you to all go take a look at this, and if you can lend some attention to this, please do. When I say participate, I don't mean that everybody from all these different groups need to actually do the work, but, like, you know, maybe they own little subsets of this. Maybe they own, you know, the
the parts where, you know, the Java agent is loaded in and what the defaults are for that. Or maybe they own the parts where, like, you know, the collector is packaged up and what the default configuration is for that. So yeah, please take a look.
Comment on this, and consider participating.
Carlos Alberto Cortez 00:09:27 Do you have any comments on that one?
Okay, so in that case, consider reviewing this one, you know, the issue still there, the PR, sorry.
So please, take a look.
Okay… Thank you so much for that, Jack.
Okay, moving on then. Florian, 5 minutes, a priority of different auto-instrumentation mechanisms. Yeah, please, go ahead.
Florian Lehner 00:09:57 Hi, everyone. This question was asked, by Luke Miller in an, open, in a OTEP.
As there are more and more instrumentation mechanisms, like OBEI, SDKs, profiles,
There's the question… the question comes up, who wins which information is more… is high… which information is more higher priority?
And, yeah, that's… I wanted to raise this question in this scope. What do you advise who…
Where should we maybe document?
What priorities and fidelities of the different data mechanisms are.
I think this is a change in how observability
a consequence of the change how observability is doing at the moment, so profiling in OBI is more like a daemon set, and before that, I think there was not such a conflict with SDKs, as they were more independent and not…
Overlapping, so my question is,
How can the group advise on… on resolving these priorities?
Tent.
Ted Young 00:11:11 I actually see this as directly related to the packaging SIG that Jack just brought up. Like, as part of that packaging work.
It's true, we're tackling, like, Linux package management as our first target, but because it's the very first target, where we're trying to bundle up all of this collectively, where you just say, install OpenTelemetry, and you get it all, like, what does it mean to get it all?
is one of the things we have to figure out. And, because there is a bit of overlap.
Figuring that part of it out is one of the things. I think it's actually pretty easy to sort some of this out. Most of the overlap shows up because there's been…
you know, for the last year, a gap in how easy it is to install things like OB, like, if you're an operator, versus installing, you know, the SDKs, if you're an operator, like, getting them out everywhere, and so that's put some pressure to start recreating some functionality, but I think…
With the injector and other things, with this new approach.
That gap is much smaller, so I think it becomes much easier to say, like, you just don't turn tracing on in OB, you use the SDKs, for example.
So, I guess that's what I would say, is like, let's use this packaging SIG as sort of the place to… to sort all of that information out.
Liudmila Molkova 00:12:43 Yeah, I wanted to explain, I've read the ATAP, I started reading the ATAP.
And it just…
lacks the context that I need to understand what it does, right? It's not the question of you need to change the approach, it's the question of, can you help me understand what this ATEP is about, and how it works with the
applications. I don't think I'm alone here, because a lot of people in the community didn't work with profiling or OBI, so I think I'm just expressing the lack of context for anybody beyond this to groups to review this OTAP.
Properly.
Ted Young 00:13:31 But does that… does my response also help you, Florian? Like, would you be able to… To maybe, like…
use that… New Packaging SIG is a forum for discussing this stuff.
Florian Lehner 00:13:45 I'm not sure if the packaging sig is the right place.
I could imagine that priorities… Are defined on a…
solution level, like OBI, let's say that OBI becomes a configuration, like, hey, this wins all the time, for example.
SDKs, have… have priority over,
our, over spans and traces, by OBI.
Yeah, yeah, I think we… Need to work on this.
And also expand, like, Lut Miller says, on, on the… on the background information. I think, he would… did a good job with the…
resource sharing context and process, sharing context in the other OTEP.
This is similar here, I think, and maybe it needs to expand here. Thank you.
Carlos Alberto Cortez 00:14:56 Yeah, perfect too much for the… Oh, go ahead.
Tyler 00:14:59 I would also add to that, just kind of, like, maybe heads up on this, I'm not 100% sure on this OTEP,
But I do know that, like, I've worked a lot in the OBI, or the OB project.
And,
we definitely see, I think, a little bit more of, like, a partnership going on here with, like, the SDKs, and the ability to do, like, a lot more enrichment.
and bidirectional communication between the SDKs, which obviously, like, this is kind of the start of.
But one of the goals that we saw is, like, you know, from Obi's perspective, it actually can gain more information about, like, what's going on in a system.
Outside of, you know, just a particular process running a particular language. And if you're able to, you know, annotate traces in a particular way,
maybe encapsulating traces, that'd be really ideal. It'd also be really ideal if there was bidirectional communication telling you, like, in the SDK, like, hey, this is the metrics that we're collecting, and Obi's like, that's cool, I actually can add to that. Like, currently, right now, like, we actually take the priority of…
you know, the SDK is going to be better positioned to get a lot of information, so if it's exporting
traces of its exporting metrics, OB doesn't do any of that.
But there's a good…
chance that, like, OB could actually supplement what is being sent. And so we are looking into that this year. That's actually one of the goals we have for this year.
So, like, I do think that there's a very rich ecosystem for, like, ability to, like, actually supplement, not necessarily it being a black and white, like, on or off thing. Ted, do you have a question?
Ted Young 00:16:37 Oh, yeah, I was just gonna clarify that, like, regardless of the SIG or where we work it out, it's fine in an OTEP. I think, specifically, I was maybe more responding to
this OTEP feeling like it being kind of point-to-point, just talking about the profiler and Obi, and I was trying to point out we should be looking at it a little more holistically, kind of like what Tyler was saying about these things working collaborative with each other.
And I wouldn't want to start sorting it out by trying to just think about point-to-point communication between the individual tools, because that might get a little gummed up if we go about it that way.
So it'd be easier if, like, all the stakeholders could at least…
take a look at an OTEP that sort of mapped out collectively, how all these pieces are supposed to fit together.
Which is more work, so, apologies.
Carlos Alberto Cortez 00:17:40 I am listening in silence, hearing silence, sorry, and we are on 5-minute mark, so unless there's something more, let's move on, let's keep on iterating on that offline. Thank you so much, Florian.
Okay, the next one is mine. I'm talking about this one, this issue on behalf of the Kotlin Sea.
This is about making clock… the clock interface, be available in the API.
Basically, as you can see, this is, you know, many of the SIGs have their own clocks, but it's defined at the SDK level.
Basically, this could be useful for instrumentation as well.
Especially when you're, like… for example, there's one example here of one instrumentation.
OKHTTP, which is super popular in Java, and they are trying to add underworld timing attributes, but for that to be, like, really correct, you need a clock interface, which, as I said before, it does exist in SDKs.
But it's not an API thing, you know?
Go ahead, Josh.
Josh Suereth 00:18:47 Yeah, I just… I want to say I'm very supportive of this, and I wanted to add, for those… those who might not be aware, or if you use Go, where they hide this, there are two clocks in your system, right? There's the one that has a timestamp, and then there's the one that we use to get nanoseconds, and since we do nanosecond resolution, that's more based on CPU cycles.
The way a lot of instrumentation works is you'll grab, at the start of a span, nanoseconds and system time, and then you'll do diff-based time that's very efficient, or more efficient to grab.
this, like, clock speed. So there's actually a huge efficiency win, if we have… if we know that we've already grabbed
The one timestamp and don't have to call the other one.
And when we did the metrics implementation in Java.
We used a bunch of dirty hacks in the SDK to go grab this clock off the span to try to do this diff-based time.
And I think this is important enough that we should provide that capability in the spec, for folks to have access to in some fashion, as long as it pulls off a context, in some fashion. I, I, yeah.
Anyway, that's all I had to say.
Jack Berg 00:19:56 Hey, Josh and Carlos, do you all have, some ideas of how this clock might manifest in the API? Just to, like, sort of orient me? You know, because we have… we have meters, and we have tracers, and we have instruments within the meters, and spans within tracers.
And, you know, we basically… it sounds like we want, we have two goals. One, highly accurate clocks, just for… In this issue, I think they're trying to add, time as attributes on spans.
So that's a little bit different than what you're talking about, Josh, which is just like, hey, how can we, like, have this sort of SDK-level clock concept, to record highly accurate measurements to metrics? So, like.
Do we just offer an abstract clock somewhere higher order than tracers or meters, or do we somehow, like, embed it into spans? Or do we introduce this timer measurement, timer instrument type that we talked about years ago, right? Like, which is this syntactic sugar over a histogram specifically for timing things.
Josh Suereth 00:20:59 I, I, so, so, I'll jump in, sorry. The, the thing that,
The thing we… that would help in Java today.
And this is not necessarily what the spec should be, is every time you create a span in Java, you instantiate one of these clocks, where you grab the system time, and grab the current diff time, and then while that span is in context, every time you take a time measurement, you want to try to use that clock.
So, what I'm thinking, and this is very naive, and I didn't have a chance to read through the full proposal, I just think this is a thing we have to figure out, is that you would be able to say, give me a clock against current context.
And if one doesn't exist, you can start at that point in time.
a highly efficient clock. And then we can use that clock to do span start time, and we can use that clock to do, like, metric measurements and exemplars and all that kind of stuff, because there's one in context. And so, there'd be… the API would be something about, you know, like.
Create a new clock and put it… and put it in… create a new clock from context if it doesn't exist, or instantiate a new one.
and then make the clock active in context for all measurements going forward. And then when we do measurements, we look for that clock in context. That's kind of what I'm…
what I'm envisioning this API would look like, very rough, and I haven't thought about other length… like, in Go, I don't think you even have to care, because you only have one API, and it does both calls to both clocks for you at the same time, so you don't… you don't have anything you have to do.
But for languages where you do have that, like, access to both.
I think this could be really valuable, and I think having an optional
you know, spec for it for languages where you care would be really valuable. Especially, it would have made a lot of… a lot of the hacky things we did in Java much more elegant, and kind of, like, you know.
Simpler.
Tigran Najaryan 00:22:55 Yeah, I was about to refer to the Go implementation. As you said, when you access the current time in Go, it takes both the clock, the wall clock, and the
the monotonic clock, right? And when you're doing,
diff operation between two times. It uses the monotonic clock to give you high-precision nanosecond durations.
is this the business we want to be in, in OpenTelemetry? Like, the language, it seems to be part of a language runtime. Like.
the, like, goal demonstrates, right? Is this something that we want to mimic in OpenTelemetry? Is it a business we need to be in?
Or we should have a recommendation about how you deal with the clocks, but not necessarily provide an implementation?
What's the… what's the thinking here? Is it… is it purely… For calculating high precision… time differentials.
Or is it more than that? I'm not sure I entirely understand what the goal here is.
Trask Stalnaker 00:24:04 I think it's slightly more than that. It's to get high precision nanotimes, like epoch nanos.
That are… Consistent against the span start time.
Jack Berg 00:24:25 Yeah, but Trask, what I kind of misunderstood about that is, like.
Okay, so you've got the span, start, and end time, which use a high-precision clock, and so you're trying to record intermediate events between start and end that, like, you know, fit within the range of that high-precision clock that don't disagree, so everything's consistent.
This person is trying to model those timestamps as attributes on the span.
If this person modeled them as events on the span.
They'd get a high-precision clock by default.
Are we modeling this wrong?
Trask Stalnaker 00:25:08 That's a… That's a whole different question. Yeah.
I know from the instrumentation, the use case Josh was talking about, on the metrics side, we've suffered from that, not having this clock in the Java instrumentation.
Where we have to re…
Because we want… we can't reuse the disk, we have to do… like, when we're stamping span and metrics at the same time, we have to generate our own timing and populate. There's something… I can't quite remember all the details in my head right now, though.
Jack Berg 00:25:49 No, I got it right, Trask? Because, like, we have these duration metrics that are recording the interval between the two times, and we have a span that's tracking that same interval, and the duration recorded to the metric is not consistent with the duration of the span. There's slight variations that can crop up because they're not using the same clock.
Trask Stalnaker 00:26:10 Right, that's it, thank you.
Tigran Najaryan 00:26:12 So it's about providing an interface to the baseline time recorded when the span was created.
It's not just a general-purpose block API. Somehow, it needs to be tied to a reference point that was created when the spam was started.
Or some other instrument began measurements, if it's not only about spans, maybe somehow it needs to be about other signals as well.
Trask Stalnaker 00:26:43 Right, because we can only get epoch time in millisecond precision.
Tigran Najaryan 00:26:48 Which is inaccurate, yes, yeah.
Trask Stalnaker 00:26:50 Right, and then we're kind of stamped… we're making up the nanotime on top of that, diff-based.
Tigran Najaryan 00:26:58 And you can't obtain it again when you need a high-precision
timestamp again, because it's not going to be accurate. You have to obtain it by referencing the first one that was obtained previously. That's how you get the high precision.
Okay, so… okay, I get the… I guess the…
what the problem is. Not entirely sure what the API can look like for this thing.
Let me let you have your hand up for a while, sorry.
Liudmila Molkova 00:27:29 Yeah, no worries. This is also a logs problem.
And even timestamp precision is not enough. You probably don't always… can't always get this kind of second precision. It's also across threads, so things become very interesting with logs, but it's… it came up there. I added a link to the agenda.
Tigran Najaryan 00:27:51 Especially if you are repeatedly creating new log records, and you have to put that high precision timestamp on each.
You do not necessarily have a good way to do that, unless you somehow try to measure the time passed since the previous one was obtained.
to correct… and now we're in a realm of doing something like the NTP servers, which is…
I think too much complication, probably, for us. So you'd have to…
Take into account both the wall clock time that you…
can obtain right now, but also the time that has passed since it was a… since the High Prism timestamp was obtained last time, and try to…
Maybe… maybe adjust?
Whatever is cut… the wall clock time is not going to be inaccurate. Okay.
This needs some thoughts there.
Jack Berg 00:28:44 The theme that I'm hearing emerge is sort of like, you know, spans have highly accurate clocks used to start this… used to record the start and end time, and we have other signals that are correlated with spans, metrics and traces, that record intervals and timestamps.
that may be inconsistent with the data recorded on the span. And so this is where I think, like, the context-based APIs that Josh was proposing could be, like, a good match to it, because you could do things like
You could do things like, within the metrics SDK, record their timestamp on exemplars using the same clock that the span uses. Within the logs, when the log SDK, when the log SDK is trying to record the timestamp on the log record, use the same clock from the span if there's a span in context.
And the one thing I don't see an answer for is the intervals on metric durations, like, because that still has to be recorded outside of, like, the SDKs.
But maybe if there is a mechanism for the instrumentation itself to get this clock from context.
Trask Stalnaker 00:29:51 Yeah, we can stamp the end time, the high precision end time on both the span and use that for our duration metric.
Jack Berg 00:30:01 Yeah, I'd still like more work for instrumenters than I'd like. I really do think that the lack of, like, a timer instrument is a disappointing
Reality, but, maybe it's enough to get us by for now.
Carlos Alberto Cortez 00:30:15 Yeah, by the way, we are almost… well, we have just more time, so John McD, and then, we move on. Yeah, thank you so much for this. I will add some notes. John McD, please.
jmacdonald 00:30:30 Hi, I just wanted to respond that I've basically support what Jack was saying strongly. I feel like we have an opportunity to not let the user touch the clock here. Like, this is… instrumentation is about the meaning of the event, and it should be the SDK's responsibility to do the clock for you.
In the case of this metric thing, why don't we, like, just take the span and compute the metric after the span is finished? You'll use exactly the same clock value, and you won't call the clock twice.
I just say, like, for every case that you have, there should be a first-class API to do what you mean, and not touch the clock, and get the right result. We have work to do, but I think we should not be handing clocks out to instrument, right?
instrumentation, especially because when you turn off all the SDKs and all the instrumentation should be off, you should never be touching a clock, and you don't want to have to, like, check, is my SDK enabled? I want to do some high-precision timestamp stuff.
Just because you're using a clock.
My thought.
Carlos Alberto Cortez 00:31:33 But just out of curiosity, I'm sorry for using 30 seconds more, but an API like the one that Josh mentioned, like, context-based, which could be private to the SDK, could that be fine for you?
jmacdonald 00:31:48 The context-based solution sounded good to me, I just, because again, it hides the clock from the user. You're just getting the right answer, and you're doing instrumentation at the level that makes sense to you, not thinking about this precision issue.
Carlos Alberto Cortez 00:32:04 Perfect. Thank you so much for that, then. Yeah, I think I have some, reports, back for the… to the Kotlin… for the Kotlin Sea. Yeah, let's continue discussing that offline. Thank you so much for that. Sorry for using more time, but this was very interesting and very useful. Lyudmila.
Liudmila Molkova 00:32:21 Yeah, thanks. So this is just a heads up. The, some conf schema V2 is undrafted. It's ready for you to review. I think it's related to the next topic, the stability by default. So what it gives us, the ability to federate some conf.
Ability to version and stabilize them separately.
It gives us the ability to express whether we, use…
experimental version of conventions, or the stable one via schema Euro?
And finally, it gives the ability for the consumers to see the whole semantic conventions and do something
wisdom.
I think we should probably spend more time talking about stability by default, and maybe we will return to this type as we talk about it.
Carlos Alberto Cortez 00:33:19 Yeah, thank you so much for that. Let's hope people review that one, especially now that it's undrafted. Thank you so much.
Liudmila Molkova 00:33:26 Thank you. Okay.
Carlos Alberto Cortez 00:33:27 Sweet. Okay, we have less than half an hour, but almost half an hour. Austin, you want to kick off it off? You want to screen your… sorry, share your screen? I can do that for you, otherwise.
Austin Parker 00:33:38 I mean, do you… I don't have anything to share, if you want to, like, go to the OTEP.
Carlos Alberto Cortez 00:33:44 Sweets.
Austin Parker 00:33:45 Yeah, I was just hoping that we could have a synchronous discussion about, sort of, the outstanding issues, on this OTEP.
My… sort of… Summary of where we stand.
Is… it seems like there's… Still… Confusion? Or,
Not alignment on the idea of instrumentation
stability splitting from, SEMCOM stability.
So…
Was there any other… Well, I guess, two things. First,
to address that specific point. My understanding, and I thought this was…
maybe it's not clear from the OTEP, but my…
understanding of splitting these things is that it… what it… we would say…
is that if you are an instrumentation library, and today you depend on unstable Semconv, that is fine.
You can stabilize, you can say, okay, we're going 1.0 because the underlying instrumentation code
Has not changed in 3 years, and we trust it.
In the future, when the SEMCOM that you depend on becomes stable.
you can update, you can pull in those new Semconv.
And doing so would constitute a breaking change. You would need to do a major version bump, you would need to go to 2.0, because you are changing the outputs of your instrumentation.
But… What we are trying to unblock is the ability for instrumentations that have stable Instrumentation code.
and unstable SEMCOM. Right now, they are held back, and they are saying, look, we can't stabilize, we can't go 1.0 because the SEMCOM aren't stable, and it is giving users a…
Incorrect assessment of the production readiness of the instrumentation.
So I guess we can start from that.
Gosh.
Josh Suereth 00:36:23 Yeah, so I… again, this is with how it's being phrased. I… I want to make it clear that instrumentation is not allowed to break the telemetry it's producing.
After it declares stable.
That is… that is… that is not… we don't want people depending on stable instrumentation and experiencing breaking dashboards and alerts, which is what you said, but the way it's phrased in the document
still implies that you can break that stability. What we're changing, like, let's talk through a process of what we're proposing from the federated SEMCOMF world, right? You're depending on semantic conventions that are unstable. So what you do as instrumentation is you create a local repository
Where you actually mark everything you're doing as stable today.
Great.
And then we're gonna give you a set of policies that will actually keep your definition stable.
In tandem with the version of the instrumentation you're releasing, so that you cannot break that guarantee.
That is what we're proposing. So, we're not divorcing, like, the stability of the semantic conventions. What we're saying is, no.
You can have your own semantic convention that you will keep stable for your instrumentation component.
And it will abide by all the same policies of stability we have around generating telemetry to not break the ecosystem. And you're now responsible for that, not SemConv.
for that, for your component. When you want to migrate to stable semconv, the global thing.
you will take your, you know, dependency, you'll make a breaking change where you switch your local repo to just import Semcov and expose it directly.
And you'll do that in a breaking change. So, like, the same effect happens, but I want to make sure that it's clear to people that you don't just arbitrarily start changing metrics and logs and traces without considering it a breaking change.
to users.
That is the thing I'm worried about with how this is phrased.
Austin Parker 00:38:22 Okay, so I was just thinking about, like, wordsmithing, because what I don't want to really do is I don't want this to…
over-solutionize in the OTEP, right? I don't want to say…
like, I want to talk about goals and outcomes, not necessarily, you must do it this way, because I feel like…
That those specific decisions are better left up to maintainers and people implementing it.
So…
If we just had, like, a big banner in there, or we just had, like, a very big part that, like, specifically said, the goal, you know, that said.
Basically what I said before, the goal of this…
Proposal is to allow instrumentation libraries to stabilize based on the instrumentation code, But… we…
You know, we must always… but also, we always must consider telemetry changes or output changes to be braking changes.
Josh Suereth 00:39:27 Yeah, like, there's a… like, we're not going to break the output of that instrumentation, is the thing that I want to make sure is clear.
You can make changes.
And there's rules we have in place to make sure those changes do not break users, as best as we're able to.
But there's a set of changes you shouldn't make, because we know that they do cause breakages to, like, observability systems. And that we don't want you to do without making major version bumps, or feature flags, or that sort of thing. That's what SemCom is built to do for instrumentation. That piece, all we're doing is saying, instead of it having to happen in the central repo.
You are able to take control and define your own destiny.
with your versioning scheme, and you can declare what you produce as stable, and you still have those same sets of rules around creating feature flags and making sure you do major version bumps, but you can do so locally. That's what we're changing.
Carlos Alberto Cortez 00:40:26 Deb.
Austin Parker 00:40:27 Okay.
Ted?
Ted Young 00:40:31 I feel like there might be an even simpler way of describing what we're proposing, which is we're literally not changing anything at all about how we're doing business, we're just bumping everything to 1.0. It's that 0.x gets treated differently
By end users from what we intend. And if we just bump everything to 1.0, but don't change otherwise, like, how we approach handling instrumentation code and breaking changes.
Then we're just back in alignment with…
What our users perceive our code to be.
So it's almost like, just kind of like a one-off, if that makes sense.
Austin Parker 00:41:14 Sure, I think right now there's a perception that because it's not 1.0, and thus it doesn't fall under the…
published guidance about 1.0, that there's a risk in adopting non-1.0 stuff, because by rules as written, you could
Get a minor… Version that has a braking change.
Ted Young 00:41:38 People should expect a 2.0 coming for any of these packages where the semantic conventions have not reached stability yet.
Austin Parker 00:41:46 Right.
Ted Young 00:41:47 Like, that's something people should expect.
For these packages. But there's nothing special about how we handle 2.0 or 3.0.
Austin Parker 00:41:56 Right, we want to normalize… we want to normalize this, really. We want to be able to say, no, look, like, we're not just sitting in…
Pre-1.0 forever…
Ted Young 00:42:07 We want to jump up to 1.0 with instrumentation as soon as we feel that the code is ready to be used in production.
Austin Parker 00:42:16 Yeah.
Ted Young 00:42:16 Right? It might be the case that the semantic conventions aren't stable yet, so there may be a 2.0 coming. People need to read the notes on the instrumentation to understand where that's at.
But… by…
staying pinned to 0.x, even though it's safe to run in production, we've been hindering adoption in, like, a pretty important way. We've gotten this feedback pretty extensively from end users, so that's… that's the motivation for the change.
Austin Parker 00:42:49 Okay.
I can update that and make this more explicit.
Was there other, sort of, big, sweeping, or… Like, outside the specific
stability stuff we just discussed. Were there other sort of concerns, or… larger scale… Like…
Things we would like to… Is he clarified, or… Da-da-da-da-da.
Liudmila Molkova 00:43:46 Austin, I want to check with you. During the Hotel Unplugged, we had the voting.
And the stability, like, in general, the topic of stability in general, was not…
a priority for people who attended the conference. But everything specific, like collector stability, some kind of stability, was important.
The year… think… like, I really support defining the stability criterias and everything, but…
How do you think about it? Is it the priority for the community, or…
Is it something we generalized too much?
Austin Parker 00:44:30 I mean…
I don't know, I think the number 4 thing was people just wanted us to say SEMCOM was 1.0 and get it over with.
Liudmila Molkova 00:44:44 Yeah, so everything specific was high. Everything in general was low.
Austin Parker 00:44:48 Yeah. I mean, I think that it's… I mean, stability…
Like, my honest opinion is just that… people…
My honest opinion is just, like, every… it's not that everyone wants something different, it's just that there's not a…
Is that…
what people want, and I don't think they're unreasonable for wanting this, right? But what people want is…
They want, you know… fast, cheap, good, pick all three. They want, like, this is…
That this solves all the prob- this solves the same problems as, like, a commercial solution does.
in the same way, with the same, like, polish, and the same support guarantees, and da-da-da-da-da-da, right? Like, I don't think that's… like, that's maybe minimizing it, or is slightly cynical, right? Like, I'm not saying that's 100% what people want.
But the revealed preferences of users is definitely that, oh…
we would like all of the things that we… like, if you look at the actual, you know, voting results, right, what do people want? They want, like, all the shit in browser to work, right? The feedback that we kind of got through graduation was very much like, oh, we're not happy because we can't use this in the front end.
Right? Like… the… the… you know… I don't know…
We don't pay any… you know, we don't… we can't just hire people to go work on stuff.
What I think… is important.
From, kind of, talking to people and reading this and talking to people, outside of…
you know, that are on the border, I guess I would say, right? People that are not day-in, day-out hotel users.
Most people that I talk to are very happy with OTEL, right?
Now, they're very happy with it in the sense that
OTEL, to them, is the thing that I install that gives me distributed traces, and those are really cool.
And it works for them, right? And then you get one step beyond that, and you talk to people that are implementing this stuff, like, systemically, or as part of…
You know, some bigger sort of migration, you know, and that's where you get into more of these specific questions about
the specific pain points, I should say, about, like, stability, and 1.0, and…
Semantic dimensions, and da-da-da-da-da, like…
But that second group is a much smaller group than the first one.
And what I would like for us to be able to do as a project, and what I think is important for the long-term health of the project.
is making everything about OTEL just more interpretable.
Make it smoother. Make it something that people don't need to go and dig through 20 billion different like…
docs and specs and Arata, and jump on a bunch of calls about, like.
to Ted's point, I would like OTEL to be more invisible, and I think that having this stability proposal is really, you know, how we get to making it more invisible.
Because I think people…
I don't know how much people should care about
the visibility or lack thereof, right? But I do think that right now.
There's kind of a mixed user… like, we do ask a lot of people, to really…
get a lot of knowledge of a hotel, and I think that we should ask ourselves, how can we make that ask smaller and smaller and smaller over time?
Ted.
Ted Young 00:49:12 Yeah, just… Ludmila, to get back to your original question about, like, the… maybe the enthusiasm gap.
A lot of… when we dig into the details about why people want stability for different components, it's…
Often related to security and security audits. That's why 0.x is so triggering for a lot of organizations trying to adopt OpenTelemetry. They're just trying to follow best practices for security.
And this is getting flagged, and so they want it to be resolved. So it's not something they're excited about, it's not like a feature that they want, it's just that they're getting blocked in their adoption in various places. And so people are bringing up the various
portions of OpenTelemetry where they personally kind of got blocked on their adoption journey.
But most of the time, if you look into, like, what literally blocked them, it was something more like a security audit than them
Not wanting to use it.
Austin Parker 00:50:13 Yeah.
Certainly a bigger issue inside, like, as you go into larger and larger enterprises, or…
less, like, tech-forward enterprise, I guess I would say.
But I think that's also why you saw, like… oh, sorry. But I think that's why, like, just make SEMCOM 1.0. I think that's why that was so popular, right? Because it neatly solves…
A lot of these problems.
While making 20 more.
Liudmila Molkova 00:50:44 how I read it, that…
The goal for us should be to find ways to stabilize individual components and make it attractive to… for people to stabilize them.
And also, help them do it properly.
And this is the, the, essentially the goal of this ATAP.
Ted Young 00:51:06 And to make sure that the default thing that you get when you, say, install OTEL is just stable things.
That… right now, if you say, get me the collector, you get a mix of stable and unstable stuff. If you say, get this SDK and its instrumentation, it's… it's a mix. And we just want it to be, like, you have to opt in to the unstable stuff.
Josh Suereth 00:51:31 So, I'm just gonna jump in, like, I agree with this high-level discussion and everything. I think the OTEP itself, let's keep making progress here.
again, when I read the OTEP, Austin, all the things you said about stability don't come through in the OTEP. When I read it, like, my NITS is not actually what we want to do. My NIT is what is written and what people will read.
Again, what LLMs will find and tell you about OpenTelemetry.
If I were to ask, like, is it acceptable for me to break
The telemetry I produce within a major version of instrumentation, of that instrumentation stable, the answer should be no, because our end state should be
Someone relying on OpenTelemetry can trust us.
To take a dependency on this, and it will continue to work, going forward.
And that if we make a breaking change, we effectively communicate it, right? That… that is what I care about here with stable by default. I think it's important to it. The wording of the thing does not tell me the things you just said in this meeting when I read it. And I'm making points about how to fix those, and I think, to me, that's the only thing I need to see to approve this.
Yeah, like…
Austin Parker 00:52:40 And I'm… that… that is changing.
Josh Suereth 00:52:43 Okay, but let's, like, for the purpose of this discussion.
Let's get this OTEP through. Like, what other blockers do we have? Like, I'm telling you my blocker, which is the way it's phrased around instrumentation is important. And it's important because I want to make sure when folks in OTEL read this.
They know what we're doing and what's allowed. Like, this kind of writing has a lot, like, a dramatic impact, so it can't be loose. It can't be like, okay, we all know what we mean here. It should actually say it directly. And if it's worded in a way people can misinterpret, people will misinterpret. So I'd like to fix that.
Is there anything else that we need to, like, cover to get this through? Like, does anyone else have major concerns with this direction and things that we do?
Carlos Alberto Cortez 00:53:28 So, with direction, I think I'm fine. I really love the way you put things, Josh. I think, at some points, I honestly feel I'm…
I don't want to deviate the discussion, but I think this object is kind of big.
So, he…
if that can help in the future, Austin, if you see that you're not making progress, consider cutting scope, keeping this part, regarding, you know, what Josh said. I think that's pretty important. Other than that, yeah, I am really supportive of this one.
Austin Parker 00:53:58 Yeah, I mean, so, with the…
With the idea that we're gonna go through and tighten up the language about
what we just talked about, were there other, sort of, major things? Looking at the comments, I didn't…
I see… there's something about… Some dits about the collector… And some phrasing stuff.
Are there things that people feel like should be taken out entirely?
Like, if… since you brought it up.
Carlos, like, was there anything that just, like, feels super…
Carlos Alberto Cortez 00:54:40 Yeah, I did a review, like, weeks ago, and I remember something about performance regression, I think it was.
There are some things that come probably left as follow-ups, something like that.
Well, to your point, specific things, let me do a review later today.
If people are fine, I'm fine as well, but if there's no agreement, we can probably just…
postpone them, you know? But yeah, let me do a further review, yeah, second review.
Austin Parker 00:55:11 Sure, yeah. Well, I'll make the changes that we just talked about, like, right after this, and then…
Maybe people can review it again.
Trask Stalnaker 00:55:20 In terms of your ask of, what things… I agree that the performance benchmarking was the only section that, kind of, I have a lot of unknown feelings about still, but I am also okay with it.
the way that this is phrased of being, you know, here are our work streams, and go figure out the details in the work streams, I'm…
Austin Parker 00:55:45 Yeah.
Trask Stalnaker 00:55:45 comfortable with that.
Austin Parker 00:55:49 And maybe it would be… would it help to kind of put something on there that's, like.
Just to reiterate that… you know.
These are… the goals of these work streams were not…
These are the problems that we're trying to solve. We're not saying they have to be solved in one specific way or another.
Like, this is kind of…
Or do you think that that's, like, clear right now?
Trask Stalnaker 00:56:24 Overall, I thought it was at a good level, like.
Austin Parker 00:56:27 Okay.
Trask Stalnaker 00:56:27 of… the… Just defining the work stream, the what, not the how.
Austin Parker 00:56:36 Yeah.
Okay.
So, I'm getting that the biggest thing is just kind of the…
Really dialing in the points we were making about what does it actually mean to…
Split this SMCOM from the instrumentation code stability.
So I will get that changed.
And… I'll get that changed right after this, and then we can re-review it, and then we can…
Trask Stalnaker 00:57:20 Since we have a minute, can I follow up on a, Josh, something you said earlier about the, instrumentations.
Basically taking their own… having their own, like, if they want to stabilize
They would have defined their own semantic conventions.
essentially taking a copy of, you know, the state from SEMCOM repo, I'm assuming.
Are you thinking that that would… require…
Doing that formally, in the sense of actually hosting that semantic convention in the instrumentation repo.
or informally is kind of what we were… have been doing, like, in at least Java instrumentation, of being like, okay, when we wrote this, we adopted this instrumentation.
version… From SemCom Repo, and… We just…
Are careful, you know, to not break… introduce breaking changes to the telemetry that they emit.
Josh Suereth 00:58:33 Yeah, so…
Trask Stalnaker 00:58:34 asking because, like, while I love the direction with the federated SEMConv,
Want to know if that is a blocker, and we need to accelerate that stuff.
Josh Suereth 00:58:47 Well, you've noticed I've been spending a lot of time accelerating it, but, okay, I'll just start with, I don't trust myself. So when it comes to stuff like that, I would rather have protection, like tests.
That's why I like typed-based languages, because I know I'm gonna make a mistake.
And so, having something that can catch it for me, like, in Java, you have the API diff thing to catch breaking changes, right? Like, specifically for that, to make decisions. So, like, we agree, end state
You would actually have something locally you can enforce.
I am comfortable if you're… you as a maintainer are signing up to maintain it, you know, manually, and treat breakages as if they're breakages and regressions.
with how you maintain your instrumentation, that you don't need the tooling. The tooling just makes it easier for you to do it.
Right? The important thing is that users can trust it, and we're not breaking their ecosystem. That's the important bit. We're building out this tooling and getting it to you as fast as we can so that you can actually have this validation, have this safety, get the same thing we're doing in SEMCOV over time.
Great. That's our long-term vision. So I would expect, you know, let's say, hopefully next year, but possibly in two years, every single piece of instrumentation OpenTelemetry will be covered by some kind of a test to make sure that we're not breaking things. That's where I'd like to be.
But, for this year, we can roll it out piecemeal, we can be incremental. Like, let's be practical here. You know, if you're willing to sign up to keep it stable, great, do it. But it, yeah, like I said, I don't trust myself not to make a mistake here or there, which is why I like to have the tooling behind me to support that.
Trask Stalnaker 01:00:30 Thanks for the clarity.
Austin Parker 01:00:33 Alright, I will get the changes made here right after this, so…
Carlos Alberto Cortez 01:00:37 Nice. Really appreciate it. We'll review that again. Thank you so much for that, and we're on time. Have a… have a good day. See you around. Cheers.
Trask Stalnaker 01:00:45 out.
