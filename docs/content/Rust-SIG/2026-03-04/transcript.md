SIG: Rust SIG
Date: 2026-03-04
Duration: 27 minutes
Zoom Recording URL: https://zoom.us/rec/share/19Zm6UtyRJki9Faz8zGO0KwKarlMMlhxYM9AFIhGW31sZ5C2i2LXHDzDrQhga0OW._97ZFOmpBmywrsp4
============================================================

## Zoom Recording Transcript

**Scott Gerring** 00:15 Hello! I think we can wait a few minutes and see if many other people join.
**Parth sharma** 00:24 Hey, how you doing?
**Scott Gerring** 00:27 Yeah, good, how are you?
**Parth sharma** 00:29 Nope, thank you asking?
There's other people gonna join?
**Scott Gerring** 00:34 Yeah, I think if we give it a minute, we can see. I can't hear you so well, to be honest.
**Parth sharma** 00:41 Just a second, let me know.
I hope it… I hope it's easier for drivers.
Sorry, that was also quite difficult.
**Scott Gerring** 01:46 I think it's your microphone.
**Parth sharma** 01:49 Hmm, no reason.
**Scott Gerring** 01:54 Hey, Bjorn.
**Björn Antonsson** 02:00 Hi there.
**Scott Gerring** 03:13 I think we'll just give it a second for Path to jump back on, as I gather he was messing about with his audio.
Cool. Welcome all.
I don't personally have anything to talk about. I'm trying to burn a little bit through the PR and issue backlog that we've accumulated.
Lately, if anyone has anything that they would like to discuss, please jump in.
**Warren Snipes** 04:30 Hi, everyone. I've been trying to get on this call for a little while, I've just missed the last couple opportunities, too.
I think, like, earlier last month, I sent a message in the Otel Rust channel on the Slack.
And, I was trying to figure out, like, how to go about integrating, you know, OpenTelematy Traces into my Rust application.
You know, I'm using, you know, Tokyo Tracing, and I wanted to figure that out, and it… it actually… it took a long time to… to figure that one out, because I… the deployment that I'm doing… They don't have, like, an OpenTelemetry ingestor for logs, so I have to do it, like, the log correlation way with the traces sent to the ingestor.
And, there was, like, no documentation that I could find on how to do this, and I ended up… forking the tracing subscriber I use for logs, tracing log FMT to include the trace ID and span ID, Into the, the log prints.
And I feel like there should probably be some documentation on how to use it, and how to use tracing And OpenTelemetry in this way.
And I just wanted to put that onto the air.
**Scott Gerring** 05:58 Yeah, I think that's still…
**Warren Snipes** 06:00 Great.
**Scott Gerring** 06:00 common way of plugging things together. I'm… I suspect that it's gonna be… back-end specific in terms of the logging format, right? I'm kind of wondering where you're pushing it there, just to fill in the picture a bit.
**Warren Snipes** 06:14 Yeah, I'd say it is backend specific, but I also didn't really understand, because I know there's, like, the Tracing OpenTelemetry project, and then there's, like, the OpenTelemetry tracing a pender, projects, and… I mean, I was trying… I thought that there would be something out there that would kind of do this already, but I realized that, you know, the Tokyo Tracing… Project doesn't really allow you to Kind of, like, push in fields into the tracing spans.
So you… or log messages, for that matter. It's something that has to be handled by the subscriber, or at every, like, info… Macro usage, you know, every span usage.
Which I think is, like, an issue with Tokyo tracing. But I guess… Yeah, I think this, like, this way of handling things, like, this is how I've done it in the past.
Just because I feel like the… You know, the… there's a bit of… more overhead on implementing OpenSelemetry.
Logs, ingestion over just, you know, standard out.
At least for my use case.
So, yeah, I was just thinking, like, we should probably have some documentation on this.
**Scott Gerring** 07:37 Yeah, it could make a cool example, I suppose. I guess the trick would be just kind of separating out the part where you decide how to format the log.
In a provider-specific fashion, so it's clear what the commonalities are.
that are provider-independent. Bjorn, can I… can I throw you under the bus briefly? How do we think about this with DDTraceRS? I guess there we're still expecting people to export the logs to STDart and scrape them separately? Are we doing anything to make that easier? Do you have a view on it?
**Björn Antonsson** 08:11 I mean… We don't really… have… exporting the logs in DigitraceRS, there is now the most recently released one. There is, support for, like, the OTLP export of logs, but what does that… I mean, do you have to hook up your… your Tokyo tracing, thing with the open telemetry tracing appender, and then export it to OTLP if you want that, or… I mean, I guess…
**Scott Gerring** 08:53 I guess our view is that people would be doing it to stand it out as well, and have the agents scrape it, hey? Typically.
**Björn Antonsson** 09:01 Mmm.
I'm not sure if we would… It… it depends.
But, it's, it's, like, right now, we did not… like, the first version, we didn't do anything special, but if you want things to come out and get the trace and span correlation, you will still need to hook something in, because there is no… automatic pickup of traces patent IDs from OpenTelemetry.
in Tokyo tracing.
**Scott Gerring** 09:37 Yep.
I guess it sounds like something that would be useful to have an example for, if we could do it moderately generically, hey?
**Björn Antonsson** 09:49 Yeah, absolutely. I mean, any kind of use cases that… that really drives these things, that we can explain to people, or where we can show how to do things, and also that… It's a test of the integration parts, if you want to… if you want to use them.
**Scott Gerring** 10:15 Warren, if you have the time and the inclination, maybe you… what would be super helpful for us to try and kind of capture the misery and… The document, the way around it, is… if you could raise an issue on the repo and say, like, here, here's the problem that I've just described, that you've just described to us on the call, here's how I've solved it, maybe we can do an example out of that.
Then we can all have a look and be like, yeah, this looks like how we would expect it to work, and then we can pull out what you've done, kind of refactor it to be a generic hotel example.
And incorporate it so other people don't struggle with it in the future.
**Warren Snipes** 10:54 Okay.
I think that there are some… I think the biggest hurdle for this is actually on Tokyo Tracing's side, Because, like, the tracing subscriber implementation, like.
basically, I had to go in there and, like, hard code extracting the span context, and then extract the trace and span ID from there, and then, like, hardcode that into the subscriber, because they don't have, like, a generic way to include extra fields.
Into the tracing subscriber formatter.
**Björn Antonsson** 11:31 And there are, like, a few open… Could the user, like, give, like, an example of what you're doing, or maybe code examples? Because I don't really… Why would you… This feels like there's something missing, or there is something wrong, and we should try to fix stuff.
**Warren Snipes** 11:57 Yeah, so in my environment that I'm deploying to, we don't have an OpenTelemetry log ingestion system. We have tracing for… we have support for tracing, so I can send my traces produced by my application to our ingester, but not the logs.
The logs have to be… Scraped from… from Standard Out.
for the applications.
So, I send the traces, and then I can correlate the logs with the traces.
And… Like, that's fine, but it's actually printing the trace and span IDs in an automatic way, which is an issue when using Tokyo Tracing.
Are you kind of picking up what I'm putting down?
**Björn Antonsson** 12:51 Mmm… not exactly, because, I mean, if you are using Tokyo Tracing, and you use the OpenTelemetry.
like, Tracing log appender, and then… and that goes to standard out.
If you use that exporter for the logs.
Wouldn't you get the right thing out?
**Warren Snipes** 13:20 Yeah, but that… that would mean that now, I'm using the OpenTelemetry… tracing… like, their, their formatter.
like, not… Not the formatter, which includes the… Like, okay, so I'm using, log FMT as my, as my tracing, I mean, as my, log formatter.
And I only want to print log FMT, but if I use the tracing… the OpenTelemetry tracing appender, that won't be the case anymore.
**Björn Antonsson** 13:56 Yeah, no, I completely understand. Okay, then I understand that part. Interesting.
Yeah.
**Warren Snipes** 14:08 Yeah.
Huh.
So, I… I mean, yeah, I think this is… it may be… maybe I'm, like, the… maybe the way I'm doing things is not the normal way people do things.
But… Like, I didn't know that, when we were starting, and then also, like, we have some… Restrictions on the… on where we're deploying to, which… don't allow us to use the OpenTelemetry, logs.
**Scott Gerring** 14:43 Do you want to write down, either in the Slack, sorry if you already have, I can't for the life of me find it, or on an issue, exactly where you got stuck, because that, I mean, that's going to be kind of immutably useful to us to clarify, and then what you've done, and then we can work out either the There's an easier way of doing it that's not obvious.
Or, this is a universal pattern, and we should encode it into a sample in the documentation.
And maybe that'll be also something that… Leaks back over into the tracing side, as you mentioned.
**Warren Snipes** 15:15 Yeah, of course. I did link to my message, like, in Scott's, ping in the Slack channel, opened a thread on that, and I linked.
my message that I sent prior to this.
**Scott Gerring** 15:30 rude.
Yeah.
**Warren Snipes** 15:35 I could definitely open up an issue, on the GitHub, and…
**Scott Gerring** 15:40 Let me go through it asynchronously tomorrow, there's, like, quite a bit to take in, but I don't want it to consume more of your time until it seems like… it's worth the effort, if you know what I mean.
I'll rock it, and then I'll write you back and say, here's what I think we should do, if that works for you.
**Warren Snipes** 15:56 Okay, yeah, no problem.
**Scott Gerring** 15:58 Sweet. But yeah, no, absolutely, anything that we can do to make the onboarding less miserable and less fraught is something that's worth doing, I think.
**Warren Snipes** 16:08 Yeah.
**Scott Gerring** 16:22 Path, is there anything we can help you with while we're all here?
I'm not sure if you're talking, but if you are, I can't hear it. I don't know if anyone else can.
**Warren Snipes** 17:01 Hmm.
**Scott Gerring** 17:13 No worries, but if there is anything… Okay, cool, great, great.
Yeah, and… good stuff. If you would like any assistance working on it, just give us all a ping, either in Slack or on the issue. We're sometimes not super responsive, but we will get there in the end.
I guess, please.
**Warren Snipes** 17:36 I did have, like, one question here, it might be a little, like, off-topic, because I'm trying to, I guess I'll explain, like.
how the system works, and then kinda… I just want your opinion on how I should kinda handle it.
So, we have a Rust application which uses IO3 to go and call into some Python application, and it's a quite large Python application. And right now, the Rust side has OpenTelemetry tracing implemented.
But when I call into the Python function.
you know, I, I would like to connect the trace But I'm unsure if I should be using a… the Python, like, OpenTelemetry tracing, like, exporting from Python, or should I somehow be, like, feeding… the trace information back into the Rust side, and then, like, have it export, because the… the Rust application is, like, the long-lived process, and the Python is just, like, a function call, and then the Python's done.
I know it's kind of like a weird… Set up, but…
**Scott Gerring** 18:52 Can you be here?
**Warren Snipes** 18:53 Warded.
**Scott Gerring** 18:54 Can you be a bit more concrete about exactly what it's doing, just to kind of fill in the mental model?
**Warren Snipes** 18:59 Yeah, so we have a bunch of, so I work for this company, and we do a lot of, like, data science-type work, and a lot of real-time ML inference, and we have this Rust application which picks up jobs from, like, a ETL-type system.
**Scott Gerring** 19:15 And then we… we do some transformations on that data, and then we go and…
**Warren Snipes** 19:21 Call a Python function.
from the Rust code using pi 03.
**Scott Gerring** 19:30 And…
**Warren Snipes** 19:34 And then it just, it just calls a function, it takes about, like, a few seconds to run, and it's a quite large function, or a quite, like, large Python, like, library that we're calling.
And then… Yeah, like, it just gets the result back, and then pushes the job along, and then it picks up a new one. So it's not, like, a long-lived Python application, like, the Rust is really the long-lived application.
**Scott Gerring** 20:02 Yeah, and you want the granularity of having some spans in Python, you're not… you don't just want a span that captures the call into Python.
**Warren Snipes** 20:12 Yeah, that's correct.
**Scott Gerring** 20:15 I, I guess… if… it was me, I would probably try and make the Python thing deal with it separately, because it'll be not very ergonomic to get all of the OpenTelemetry data out and return it to Rust, although if you ask Python to do it separately, you're gonna end up with, kind of, a parent and daughter. Yeah, that's probably right anyway.
Yeah, but then I guess you have this weird thing where in the Python application, you're gonna have to run an OTLP exporter as well, which is… Which is a bit awkward, because then it would have a long-running background thing in there.
**Warren Snipes** 20:54 Yeah.
**Scott Gerring** 20:55 Yeah, I… It's a bit hard. You could think a bit about how much you want to capture, actually, and whether or not it's… like, if it's a finite set of subspans that you want to capture, if you could model that reasonably in the API and return it to the Rust application.
Or if that's really awkward already. Like, if it's so complicated and you want to capture the subspans from any arbitrary thing running in Python.
through the OTEL API, that's gonna be a bit hard to model as a return back into Rust land, I think.
Probably depends the level of fidelity you want.
**Warren Snipes** 21:34 Yeah, and to make this, like, doubly more complicated, the, so we… we use this… So, like, the Python logging library, or… I don't even know… yeah, the Python logging library, it allows you to, like, capture the log calls, and then, that runs a Rust function, which sends the logs to Rust land, and then prints the log messages in Rust land. So then we're all… so that's like a… It's using all the same, like, logging format.
So it's like… really hectic, and I'm… I'm… I'm looking forward to it.
**Scott Gerring** 22:12 eventually.
**Warren Snipes** 22:12 getting off the Python stuff, but…
**Scott Gerring** 22:14 But so it… so Rust calls into Python, and then Python calls back into Rust.
**Warren Snipes** 22:18 Oh, yes, yes, it's very weird.
**Scott Gerring** 22:21 That is… Rather, rather hectic.
Do the logs that go out in Rust magically have the right context on them? So they get the request ID without you… they get the trace information on them without you having to do anything special?
**Warren Snipes** 22:36 No, because those… No, they don't do anything like that, unfortunately. It would just be everything that's from… I think all of that comes in on, like, one span.
Err.
**Scott Gerring** 22:52 But the span… the span of the parent Rust thing, or some other…
**Warren Snipes** 22:56 Yeah, it's like the span of the parent… Basically, how it works is, like, there's a, There's, like, a thread in Rustland that just processes these logs that Python sends to it, so it's, like, completely separate.
**Scott Gerring** 23:11 Oh, okay, so you have, like, one big background thing that has its own context.
**Warren Snipes** 23:16 Yeah…
**Scott Gerring** 23:17 So it's correlated to something, but it's not correlated to the request that spawned it.
**Warren Snipes** 23:22 Yeah.
**Scott Gerring** 23:23 I mean, maybe… maybe a middle ground is that you publish in the span ID… So when Rust calls into Python the first time, you include the span ID of the calling request, and then you emit that with your Python log formatter?
So that the outer Rust log writing thing can at least attach those logs back to the span that's executing. It doesn't help you with nested spans, but it would get you something with less of a nightmare.
If that makes sense. Yeah.
**Warren Snipes** 23:53 That's, that's good, I think that might be a good first step.
**Scott Gerring** 23:58 Bjorn, I don't know if you know any elaborate secret insider tricks for doing FFI context propagation.
**Björn Antonsson** 24:10 No, actually, not… not really. I mean, it's… it's, it's a really messy when… I mean, the… the… a clean way would be to sort of, like, treat this as a… distributed service call when you hand over it, but that's not related. It's too costly.
So…
**Warren Snipes** 24:33 Yeah, that's kind of how I was… like, the mental model, at least, was think about it like its own thing.
But, unfortunately, with how this all works, it's, like, it would be too costly to send the data to an actual other service, which just is, like, a long-lived Python process.
So that's why all this hectic stuff has to happen.
**Scott Gerring** 24:58 you could also… and I don't… I don't think this is a good solution, but I can't think of any good solutions. Maybe the log correlation would be sufficient, but… You could also set up Python so that when you call into it, you give the trace information to the parent, like you normally would for a cross-service call, like you include it in the API.
And on the Python side, you set up OpenTelemetry to start a subspan from that, and you set up the OpenTelemetry Python stuff to use an in-memory exporter, and then you have a separate call from Rustland into Python to retrieve all of the exported data from that in-memory thing, and then use the Rust publisher on the outside to push that out.
But this is getting very elaborate and…
**Warren Snipes** 25:43 Yeah.
I think that is, like, the… Probably the… the best solution in terms of… in terms of performance. But I also, I… I don't know enough about how the exporter functions, and if I can just… how I, like, propagate that span information.
From Python into Rust. I guess that's, like.
Where I'd have to look into doing this, if I end up doing it at some point.
**Scott Gerring** 26:12 Yeah, I guess the tongue-in-cheek, jokey answer for 2026 is use Claude to rewrite it all in Rust, but… Very helpful advice.
**Warren Snipes** 26:22 Yeah, yeah, that is the goal, eventually.
A lot of it's already been written in Rust, it's just… there's… you know, getting data scientists to write Rust is impossible, so it's, It's kind of a never-ending problem.
**Scott Gerring** 26:40 Yeah.
If you do think of a clever way of doing it, let us know in the chat, because I'm very interested, and I can't think of anything sensible to recommend.
**Warren Snipes** 26:48 Yeah, I definitely will. I'm thinking about writing at least a blog post on how I'm handling this, because I think this is, like, a really weird use case, that probably very few people have.
So yeah, I'll definitely link that if I ever do that.
**Scott Gerring** 27:05 Cool.
Alright, Bjorn, did you have anything that you're excited to talk about at the moment, or shall we wrap things up?
**Björn Antonsson** 27:17 I think we should wrap things up. Nothing exciting on my end so far.
**Scott Gerring** 27:23 Cool. Oh well, thank you all for joining.
Have a lovely evening or day, depending on which time zone you're in, and stay in touch.
**Warren Snipes** 27:32 Alright, thank you.
**Scott Gerring** 27:34 Cheers, Warren. Ciao.
