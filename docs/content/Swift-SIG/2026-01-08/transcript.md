SIG: Swift SIG
Date: 2026-01-08
Duration: 43 minutes
Zoom Recording URL: https://zoom.us/rec/share/70EkgawFlNij70FFAlU3eNhaQSqlWcxmSelxpHj0DRw6I9fFemUMOBIC670inkEE.qOiFHcn-GIph-HZ_
============================================================

## Zoom Recording Transcript

**nacho** 02:07 Hey, Brad, it's Happy New Year.
You are on mute, but I can imagine you, also.
**Bryce Buchanan** 02:19 Hey, Nacho.
Happy New Year!
What is even going on with this project? I don't remember.
**nacho** 02:49 Oh, I thought I had approved that before. Maybe I forgot, or you don't have your view updated?
**Bryce Buchanan** 02:58 I don't know.
Oh, wow, everybody just showed up.
**nacho** 03:04 approved, I don't know why.
**Bryce Buchanan** 03:05 Wow.
**nacho** 03:06 I have been reviewing, for sure.
**Bryce Buchanan** 03:13 Hey, everybody!
**Martin Holman** 03:16 Little.
**Bryce Buchanan** 03:17 Happy New Year.
**Martin Holman** 03:20 Happy New Year.
No one showed up on the 1st.
Or Christmas Day, not.
**Bryce Buchanan** 03:33 Yeah, what the heck?
**Martin Holman** 03:34 I don't think.
**Bryce Buchanan** 03:40 Yeah, yeah, the meeting, had double holidays this year.
Okay… Let's bring some of these topics forward.
Alright, anybody with any new topics, please add them to the agenda, and we'll get to them after we review.
Previous topics, so let's take a looky-loo.
Try to remember what we were working on before the holidays.
Alright, so configuration options for metric kit instrumentation.
**Ariel Demarco** 04:36 Hey, yo.
**Bryce Buchanan** 04:38 Hey, Ari.
Okay… Make this a little bit bigger.
**Bee Klimt** 04:53 So, yeah, I tried to make this similar to the other instrumentation configuration, especially URL session.
It should be pretty straightforward, just let you change the tracer, let you switch between the two different JSON formats.
**Bryce Buchanan** 05:08 Cool.
I mean, it looks like it's been approved, so we can probably let it merge. Ari, your… your comments have been…
**Ariel Demarco** 05:18 Yeah, yeah, they've been solved, and I saw that Nacho already approved the PR, so I'm fine on merging it.
**Bryce Buchanan** 05:25 Let's do it, then.
**nacho** 05:27 Yeah, it was… yeah, clean and… Perfect. So, yeah, yes.
**Ariel Demarco** 05:31 Yeah, nice BRP.
**Bryce Buchanan** 05:32 Cool.
**nacho** 05:33 Yep.
Definitely.
**Bryce Buchanan** 05:38 Alright, found solution for this issue. PR ready for review.
And this is the, background crash that…
Nacho thought he already approved, which he has now approved.
**nacho** 05:56 Yeah, I also agree with that.
Yeah, it was also a great approach, just having a…
a method that we can add whatever new background task Apple decides to create.
So yeah, that… yeah, that was also a very, very good solution.
**Ariel Demarco** 06:18 I did some tests.
**nacho** 06:19 So, it…
**Ariel Demarco** 06:20 We prevent to happen, these kind of crashes.
As time goes by.
It's hacky.
But… You'd work.
**Martin Holman** 06:34 I know all of your analysis and stuff is hickey, isn't it?
**Ariel Demarco** 06:38 Yeah.
Yeah…
**Bryce Buchanan** 06:43 Very good. Cool.
Oh, we can merge that one too.
Let's see, what was this one? Monotonic Clock… oh, yes, I vaguely recall this now.
It could go… it can go backwards.
**Bee Klimt** 07:06 Yeah, we talked about the solution for this at the last couple of meetings, and I think we were in general agreement on it, so…
**Bryce Buchanan** 07:13 Go right in this one.
Very good.
And then that workflow issue was resolved, the tests were run, and it's been approved, so let's merge that one as well.
Very good.
Cool, cool, cool.
And then we have this Swift 6.
Upgrade…
And then that one… Oh, this one hasn't been updated yet.
So that still needs to get,
I wish that I could, like, do a force…
Force update, like, when you have it set to allow it to… to merge,
Without, being latest, then that doesn't even show… the option to, like, have it merge main is not even an option.
I wonder if there's a way to, like, set up GitHub to have it there, but not make it required.
So, it looks like…
**Ariel Demarco** 08:23 Yeah, I don't know in forks. I remember that it's feasible with simple PRs, but when merging forks.
I don't know, maybe we can ask.
Somebody from… TNCF.
**Bryce Buchanan** 08:46 Alright, so I'll have…
Just ping Will to see if he'll fix that. Cool. Alright, so I see there's no new topics for today. Why don't we just take a look at…
our issues… okay, so we got that one.
And then this one as well.
Yeah, this is the issue where they want to use… yeah, I guess they're… maybe we can ask, or have them,
Look at the new… Metric kit, instrumentation.
For that one.
**Ariel Demarco** 09:35 Yes, I don't know where they want to export this, but the cardinality will be…
A bit problematic for the collector.
**Bryce Buchanan** 09:45 Yeah…
Okay.
And then for pull requests, so we've got Will's PR, and then a doc update from Will as well.
Well, it looks like there's just some feedback on there.
Let's take a look at… the main repo…
**Martin Holman** 10:39 How is the split working out? Has it been overall positive, or…
**Bryce Buchanan** 10:45 I think that it's been okay.
not a great deal of, added overhead, I think. And most of, I mean, as you saw with that, the build issue on Core that kind of snuck under the radar for a while, like, Core doesn't seem to get updated too often.
And most of the work is still in the main repo, so…
**Martin Holman** 11:12 That's good.
**Bryce Buchanan** 11:17 I don't know if anybody can hear that, but…
Oh, never mind then. Cool, okay, so… We've got a couple…
**Vinod Vydier** 11:28 So you're saying, Bryce, you're saying that,
Core is… is kind of, with all the APIs and SDK, they don't change much, and we are making all the changes now in the Swift? Is that…
**Bryce Buchanan** 11:44 Yeah, that seems to be the case. I mean, there are a couple of, there are a couple of things going on in a course, such as, like, the monotonic clock bug.
But, you know, since we've made Core, there's only been, what, 27 PRs that have been merged?
And some of them are, like, just releases, yeah?
**Ariel Demarco** 12:04 Which is reasonable, because…
**Bryce Buchanan** 12:05 Ma'am.
**Ariel Demarco** 12:06 API, it's purely interfaces, that they are all defined already, and SDK is implementation, and probably
During the span of these years.
Yep. Many of the problems were already fixed.
**Bryce Buchanan** 12:19 So it's understandable that instrumentation.
**Ariel Demarco** 12:22 It's the one that tends to fail.
**Bryce Buchanan** 12:25 Yep, yep, totally.
**Vinod Vydier** 12:28 Okay.
Sounds good.
**Bryce Buchanan** 12:33 asynchronous processing…
Trace Exporter has an issue where it always returns success, yes.
**Ariel Demarco** 12:45 Oh, I missed this.
**Bryce Buchanan** 12:49 Okay, I think we were waiting on the CLA to be signed, and…
**Ariel Demarco** 12:57 I reviewed this, but I never came back to it, so this is my bad.
**Bryce Buchanan** 13:02 Oh, yeah.
**nacho** 13:03 Yeah, but… but… Yeah, but basically, you were true. I mean, we don't…
want to block there. Or we wouldn't like to block there, because…
**Bryce Buchanan** 13:17 Yeah, this is…
**nacho** 13:18 It seems how you configure… we have had this conversation many times, right?
**Bryce Buchanan** 13:22 Yeah.
**nacho** 13:23 That if we block while waiting for the export to happen, We… we are missing the…
We are waiting for it, maybe in the main thread, because depending on how they configure, how they…
Sent up the project.
Waiting for that, it's really expensive.
**Ariel Demarco** 13:45 Yeah, and I think that the initial feedback was that there was no way to actually get rid of that.
Waiting, so… Based on the spec, it is… it is required to…
It isn't required what he's asking for, and at the same time, what is required is that
It timeouts, eventually, so the export is not waiting forever.
**nacho** 14:12 Yeah, this is the kind of… Peters that will really need a sync support,
some API support for some async methods, at least on our code, but yeah.
**Bryce Buchanan** 14:28 Is that an issue that we should add, is to update the exporters to be using async await?
**nacho** 14:38 I think that will be really useful.
But… We would… should also have to… Like, how to say… surfaced that async results.
To the user, because it usually happens very…
Very far from the user, and it's not easy to really report that, but… Yeah, so it's not like…
Changing only the supporters, but also we'll need some.
**Ariel Demarco** 15:08 Oh, there.
Shall this happen… shall this be a change on the public API, meaning OpenTelemetry API?
Or is an implementation that uses async await, like using tasks, being able to use?
**nacho** 15:24 it should be part of the API, because if you are the user of the library, and you are having issues, you want to log them, or you want to act on them, right?
**Ariel Demarco** 15:36 Yeah, bro.
**nacho** 15:36 Wouldn't you be interested in knowing that it's failing, the exporting, so you can… At least report that.
**Ariel Demarco** 15:45 I don't know.
There are pros and cons. The pros is that if it's, by default, a SQL weight, like the exporter and the processor.
The consumer will also be using async await, so you can have, well, the new concurrency mechanism.
So, if you yield, because you have, I don't know, complex tasks to do on the processing or in the exporting, and another runner can take the tasks, that's going to be awesome, because the whole mechanism works with async await. If you just do
On the exporter, an implementation that uses async await.
it will behave exactly the same, but under the hood, it's working with the new concurrency mechanism. I don't know if it has so much benefits in there, rather than the tooling that is new, and that is useful to do all this kind of.
**nacho** 16:42 Yep.
**Ariel Demarco** 16:43 task control that is way much better in new concurrency.
**nacho** 16:50 Yeah, I really think it should be handled at the user level, if possible, because then you can really export in another task, await in a different task for that exporting to happen, and then act on the problems, and know
And really handle the errors if needed.
Right? If you don't… we don't… currently don't surface that.
And you cannot really act on any issue that can happen, or wait, or even decide to export slower or faster, because things are happening. So that will really be…
I think useful, but yeah, it's…
It's not such an easy task, but…
**Vinod Vydier** 17:34 I wonder how the other, Language agents do that.
Because if it's optional… Are they all… Sending the…
You know, if it's exported or not, response back to the user.
We can maybe check on Java or something, right? Because we have it modeled after that.
**Ariel Demarco** 18:01 Like, I love that.
**nacho** 18:02 Dude.
**Ariel Demarco** 18:03 What?
when answering the PR, I looked at the Go and Python implementation.
One of them is waiting, the other one is not. So, that's where I found out that it's not mandatory.
In the spec, so… I don't know, it depends on us, I think, and in terms of
the API structure also, it's on us. The only problem is that these public APIs will need
iOS 13, and OpenTelemetry API and SDK use iOS 12 as minimum.
**nacho** 18:40 Yeah, we could also make that.
option. I don't know if… I mean, that…
You can have both a sync and synchronous, approaches.
Yeah, it probably adds even more complexity, but yeah, that's something that… Might work.
Yeah, because we are not supporting callbacks for handling that, so that's something that also simplified things.
**Ariel Demarco** 19:09 Okay.
**nacho** 19:10 Or limited complexity, right? Do you have everything with callbacks, it's also very difficult for… I mean…
Not very difficult, but more difficult to use.
**Ariel Demarco** 19:20 Yeah, it's brunch.
**nacho** 19:21 status.
**Ariel Demarco** 19:21 Not calling the combination handler, whatever.
**Bryce Buchanan** 19:27 Okay.
Does this look, sufficient? So, we don't necessarily… do we just want to add APIs to allow for async await with, you know, optional wrappers, like for the, iOS version?
Or, should it be completely new, exporters that allow async await?
I guess maybe an investigation needs to be required.
**Ariel Demarco** 19:55 Yeah, I think that, maybe we can…
provide the possibility to use the two, as Nacho said, at least when we start trying this out.
And eventually, when we migrate to… iOS 13 or above.
And we tested it out, and it works fine. We can just get rid of the old one.
**Bryce Buchanan** 20:16 Sounds good.
Alright.
I'll create that for now.
If anybody is brave and wants to, pick that up, feel free.
Okay, so let's go back to…
Alright, I think that…
kind of, we're up-to-date on all of the PRs there. Let's take a look at the issues.
Persistent span exporter decorator does not retry on export failure.
So this is a new issue.
Has anybody had a chance to look into this at all?
**Ariel Demarco** 21:09 Yeah, I checked it out, and he's right, like, it's… the other… the log, the persistent log exporter decorator, it's working as intended, that it's basically telling… exporting that you should need to retry or not.
and the persistent span exporter is not doing it. So, yeah, it's a bug, and the proposed solution, I think it's… it's right, too, because it's the one that the metrics… persistent metrics export as the creator, and the persistent log export as the creator are using, so…
**Bryce Buchanan** 21:42 Okay, cool.
**Ariel Demarco** 21:43 It's okay.
**Bryce Buchanan** 21:46 So, maybe we can just ask for a PR?
**Ariel Demarco** 21:50 Yeah.
**Bryce Buchanan** 21:50 If it's just this, yeah.
**Ariel Demarco** 22:01 Youth.
the… if you… If this person can do the PR, that would be good.
**Bryce Buchanan** 22:23 Alright, cool.
**Ariel Demarco** 22:31 I mean, investigating this one.
One thing that I wanted to maybe discuss, I was going to add it to the issues, because I've been looking at the different things we can get from URL session WebSocket.
But my question is…
If you have a bunch of data coming through, and a bunch of events coming, let's say.
the amount of exported data, or processed and exported data, will be huge. So my question is, shall we start with something simple, like when the socket task starts and ends?
As, like, a very minimum, and then as time goes by, or based on feedback, include more of this.
**Bryce Buchanan** 23:17 Yeah, I think that's a good place to start, like, a rudimentary, or, yeah, it doesn't need to be totally complete, necessarily.
We could leave stubs to implement further details, or even, you know, add flags to allow, you know, users to turn on and off which particular parts of that instrumentation they want.
Depending on, like, data restrictions.
**nacho** 23:42 Yeah. Yeah, maybe you should not.
Continuous span, for… for… for the socket itself, and maybe sending events.
For, for each connection could be…
a good solution for that, because having many spans, Ronnie can be.
can't be represented, probably, too noisy, right?
**Ariel Demarco** 24:14 Yeah, yeah, yeah. I was thinking of a single span, and as new connections arrive, or new data arrives, you just create a new event, a span event, and that's it.
I looked at… to see if there was a part of this as a standard on OpenTelemetry, like in the spec or something like that. There's nothing.
there are, I think, two libraries in the JavaScript world, one in Node, and the other one, I don't remember if it was related to web browsing.
that they have something, so I'll probably go and copy-paste the attributes from there.
To actually do this.
But yeah, I think this… it's kind of experimental, because there's no specs for socketing.
This type of data coming through.
By the way, if somebody finds something or has any comments around that, like… Ping me already down there.
It would be great.
**Bryce Buchanan** 25:15 Hmm…
**nacho** 25:17 Yeah, I think the spans were created before WebSockets existed.
**Ariel Demarco** 25:21 Yep.
**nacho** 25:23 So the… yeah, it was not in the… in the expectations. Yeah, it's true that…
Yeah, having that behavior is difficult to model, right?
**Ariel Demarco** 25:33 In a useful way.
Yeah, I think that it's related to the amount of data, because it depends on the socket and the task that
that socket is for. Like, it is for something that receives information every 100 milliseconds, the amount of data you're going to export will be huge, regardless of the format.
So, that's… that's why I… it's… it's kind of complicated to model.
But…
all in all, I may provide some callbacks whenever you receive some data, so if you want to log an event, or create an event, or something in particular, you can do it, and that's it.
**Bryce Buchanan** 26:14 I wonder, if a metric would be more…
Appropriate for that sort of thing, because…
If you have, like, a socket that's open,
You know, name that socket, and then you can just attribute bytes sent or received to the metric.
**Ariel Demarco** 26:36 That's… that's a good idea.
And you would make the metric and the span that starts and end, or you would make different metrics, like the duration.
They bites in and bites out.
What would you do?
**Bryce Buchanan** 26:52 Maybe have, the start and end in events, and then the data transferred using, like, the same name as the event,
To… to scope it.
bytes and received in the metric itself.
**Ariel Demarco** 27:11 Okay, that's a good idea.
I'll try it out.
**Bryce Buchanan** 27:18 I'm surprised that there's no spec on how that should be done.
**Ariel Demarco** 27:22 Yeah.
**Bryce Buchanan** 27:23 Yeah.
**Ariel Demarco** 27:23 I want her price, too.
It's really weird, and I found some issues, and even, like, people saying, like, why would you need a spec for this, like…
So, it is weird.
To be honest.
That said, we have some customers at Embrace requesting this type of
Having information about these type of requests, and all the times that we ask them, what information would you like?
They are not really able to respond.
What in particular thing they want, rather than the connection is done.
**Bryce Buchanan** 28:04 I just want all the data. Yeah, exactly. I just want all of it.
**Ariel Demarco** 28:10 So… I'll know what to do with it when I have it.
But I'll… I'll try it out and see how it goes.
**nacho** 28:20 Yeah, I, I think… Yeah, apart from that, I think that the connect and disconnect
Should be… should create a span, also. Apart from the metric to really have information about the socket.
because… Currently, the rest of the network connections are in spanse, and we can
follow the process of things through SPANS and the network connection.
If we don't have a spank here, we will be losing the… relationship.
At least a direct relationship, and that will… and we will need something on the back end.
To really match.
The… the span with… Who was calling on? Who… what was happening because of what?
**Bryce Buchanan** 29:07 Yeah, yeah, I think… I think the span is valuable, at least for the, distributed trace.
**Ariel Demarco** 29:15 Yeah.
Yeah, that's an important use case, yeah.
Okay.
**Bryce Buchanan** 29:27 Cool.
Yeah, maybe we can… we can come up with a good spec, and then…
submit it to the… the community and see what they say about it.
But yeah, it sounds like a combination of events, spans, and metrics might be appropriate, depending on where we see, like, the,
The best trade-offs for those things, particularly.
Cool. Yeah, just play around with it, Ari, and hopefully, something…
Falls into place, that makes sense.
**Ariel Demarco** 30:04 Yeah. Shall I include it in the URL session instrumentation, or shall I create a specific one for WebSocket?
**Bryce Buchanan** 30:12 Oh…
**Ariel Demarco** 30:12 My… my last question.
**Bryce Buchanan** 30:18 I think.
**Ariel Demarco** 30:19 It's part of your session, so…
**Bryce Buchanan** 30:20 Yeah, I think that it would be probably appropriate to include it in the URL session instrumentation, but maybe not in the same file, if we can avoid that.
**Ariel Demarco** 30:30 Yeah, yeah, I can do another one.
In the meantime, it's a beta feature, so…
**Bryce Buchanan** 30:36 Yeah, yeah.
**nacho** 30:37 It's complex enough, right?
**Bryce Buchanan** 30:39 Yeah.
Cool.
Hello.
Web browser, are you still alive? There we go. Come on.
Alright, so that was that,
the, random flag, so this was…
A new issue that was added by Carlos.
I think, yeah, this… this… I think that should be a relatively easy issue if anybody wants to pick that up. Good first issue for… for anybody interested.
I don't think there's been any… Feedback since this, but okay.
**Ariel Demarco** 31:34 Huh?
**Bryce Buchanan** 31:35 Probably just close that one.
give it maybe another week or two if they ever come back with any questions. And I think that covers all of the issues, the new issues that we've received.
Any other thoughts or comments?
**nacho** 31:55 there wasn't one comment in the Slack channel.
**Bryce Buchanan** 31:59 Oh.
**nacho** 32:00 about… Http headers.
**Bryce Buchanan** 32:10 That's right, I recall this.
Fucking…
Come on.
Okay, so… Let's see here, so it says…
I'm following up from the last SIG meeting regarding the HTTP headers. There was a closure in the trace exporter I could use to provide dynamic headers, however, I'm not seeing a closure instead, just a dictionary.
The goal is to add custom values in the baggage. HTTP header, this value can change.
And it's not available until after the user logs in.
Okay, so… Was there an issue… I thought that we created an issue for this…
**Ariel Demarco** 33:23 Yeah, long time ago, I think.
**Bryce Buchanan** 33:34 Yeah, I think… I remember… I remember this conversation as well, let me look at the notes here, maybe.
May not have been written down.
Hmm…
**nacho** 34:09 Yeah, I think we had a similar issue with the exporter feathers.
with the HTTPS protocol headers, or something like that.
Oh, that one?
Maybe that. Hello?
Yeah, probably excuse me.
But this was all… I don't know if we finally addressed it.
But it was similar, yeah.
**Vinod Vydier** 34:38 I think it was fixed. There were some issues with the HTTP header that were fixed sometime back.
**nacho** 34:45 Yeah, but this user wanted to change the baggage here?
I don't know which is the…
**Bryce Buchanan** 34:54 I vaguely recall that, that it wasn't…
It wasn't the actual baggage that they wanted to change, because the baggage is… Meant for, like, distributed tracing?
not necessarily distributed tracing, but it's meant for, like, transmitting information through the distributed tracing. And they wanted to do something else with it.
They wanted… oh, maybe, yeah, maybe it wasn't.
**nacho** 35:24 Because the baggage, you can't change the baggage, right?
You can dynamically change the baggage whenever you want, in any place of the stack.
Yeah.
Change the… the… I was not in that SIG meeting.
But the baggage is something that you can change. Always.
Because it's her, like, like the…
Like the active span, you can check the active baggage and modify it, right?
**Bryce Buchanan** 35:54 Yeah, yum.
**Vinod Vydier** 35:56 But what he's saying is, adding the baggage on the HTTP header, right? The baggage would be on the span.
Correct?
**Bryce Buchanan** 36:06 But it is, I believe that the baggage is applied to the headers.
**nacho** 36:13 That's okay.
**Bryce Buchanan** 36:14 Yeah.
**nacho** 36:15 transmitted with you.
**Bryce Buchanan** 36:16 Yeah.
**Vinod Vydier** 36:17 The header, okay.
**Bryce Buchanan** 36:20 Yeah, so it seems like he wants to be using the baggage propagator.
So… If he adds…
To the open bag… or to the active baggage, his… the headers… the header values he wants.
that should achieve what he… what he wants, I believe. We can follow up in the thing, or in the… in Slack here.
**nacho** 36:44 So it's like, yeah, that's true. But yeah, I… if… yeah, but as I said, I mean, you can change the active baggage, and you can modify.
Or that should be the…
**Bryce Buchanan** 37:04 Entries set… okay, yeah, so for each entry, the active baggage…
**Vinod Vydier** 37:11 So, how is this on the HTTP header?
I still don't get it.
**Bryce Buchanan** 37:18 I think that… so, hmm, oh…
Yeah, it sets a span here.
But if we look at… This might… yeah, this is in concert with the URL session instrumentation.
Hmm… maybe under the logger.
Nope, it's not garbage.
Here we go. Custom baggage… And it is added into the, propagation header here.
Yeah.
Yep, and then that's added to the trace headers.
**Vinod Vydier** 38:08 So if you have something large in the baggage, that is gonna go on the HTTP header.
**Bryce Buchanan** 38:13 Yeah.
**Vinod Vydier** 38:15 Hmm.
**nacho** 38:22 Maybe it's not well documented.
**Bryce Buchanan** 38:25 PM.
**nacho** 38:26 As many things, but that's the idea, that you can…
That you can have also different baggage per execution context.
as your half-a-span. So, you can be…
Exporting spans that have some baggage, depending on where you are executing.
**Vinod Vydier** 38:46 You're right, right. So if you have, let's say, a trace with a bunch of spans…
And these pants have, potentially…
Multiple baggages, they all go into the header.
**nacho** 39:01 If they are in the same execution context, yes.
But you can have… I mean, like, you can send some… Spans that are in a… Secondary, or maybe…
Some kind of testing, or sending to some different
Place, and you can have different baggage for them and for others that are different.
**Vinod Vydier** 39:24 ABS.
I know baggage can be some… a big blob, but also it can be linked to some… some other resource or something, right? That's… that's the idea for baggage, but I didn't realize that, you know, if you have something like a big blob that is gonna… it all gonna sit on the header.
So, you could have potentially a lot of… Things…
If you have large trays with the MD, you're using baggage?
**nacho** 39:56 Yeah, but this is thought for sending communication through the, distributed, context.
Of all the… so you can send messages through the network to the… to the other endpoints that are in the…
**Vinod Vydier** 40:13 I'm quite a.
**nacho** 40:13 Participating in the… in the communication.
**Vinod Vydier** 40:16 Yo.
No, I mean, I always thought of it as, you know, like, you could have a…
**nacho** 40:21 For example, you could use it to set priorities to some spans, and not to others, so you can ingest them faster, or you can give them priority for ingestion.
Versus others, so you can set priorities, different priorities for different spans, or for different Areas?
Of your code, and… and you could…
And that will be part of the…
**Vinod Vydier** 40:45 Nuggets, yeah, okay.
**nacho** 40:48 Yes.
**Vinod Vydier** 40:54 Now, I was thinking more from, you know, if it's even on the same context, you could have, like, you could have metrics associated with it, resources associated with it, but if there is something that is not associated with that, you can add it to the baggage, and that link would give you
you know, access to that, right? Because you can… this is a…
You have things in the context, and then you're adding additional context to that one specific span within the trace. That is my… my canonical use case for the baggage. But, you know.
You could have lots of spans with lots of baggages, and…
You know, they can all sit in the header.
**Bryce Buchanan** 41:34 Oh yeah, it actually… it actually looks like the… Baggage processor isn't necessary.
Oh, but the instrumentation configuration baggage provider…
But yeah, they could use the baggage processor, the propagator.
**Vinod Vydier** 41:57 not…
**Bryce Buchanan** 41:58 I'll take a little closer look and then have a more concise reply to this.
Okay.
Cool. Any other…
topics. Thanks, Nacho, for bringing up that, it's always a good idea to keep an eye on the Slack channel. I always forget to check it.
Cool.
Alright, anything else? If not, I… we can probably call it here.
**Vinod Vydier** 42:45 Correct me.
**Bryce Buchanan** 42:46 Sounds good.
Alright, have a nice rest of your week, everybody.
**nacho** 42:51 Yep.
**Ariel Demarco** 42:52 Yo.
**nacho** 42:53 See y'all. Bye.
**Bryce Buchanan** 42:54 See ya.
