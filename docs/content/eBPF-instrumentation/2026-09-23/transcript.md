SIG: eBPF Instrumentation
Date: 2026-09-23
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Tyler Yahn (Splunk)** 00:11 Hey.
**Nikola Grcevski @ Grafana / OpenTelemetry** 00:15 Hey, Tim, how's it going?
**Tyler Yahn (Splunk)** 00:17 Good. How about yourself?
**Nikola Grcevski @ Grafana / OpenTelemetry** 00:19 Good, good, good.
**Tyler Yahn (Splunk)** 00:21 Yeah.
Does it feel like fall up there?
**Nikola Grcevski @ Grafana / OpenTelemetry** 00:24 Yeah, started. How about you?
**Tyler Yahn (Splunk)** 00:27 Yeah, we got some early rain here in September, which kind of kicked things off, so yeah, it's, it's kind of nice, just, yeah, going.
**Nikola Grcevski @ Grafana / OpenTelemetry** 00:37 We're gonna break from the summer, yeah.
**Tyler Yahn (Splunk)** 00:39 Yeah. Yeah.
Yep, the rivers are starting to pick up, and so, yeah, it just kind of feels like we're moving.
**Nikola Grcevski @ Grafana / OpenTelemetry** 00:45 Yeah, yeah.
**Tyler Yahn (Splunk)** 00:47 I don't have, like, super cold and snow to look forward to, unlike you, so, yeah, it's not as… yeah.
Yeah. Star, too.
**Nikola Grcevski @ Grafana / OpenTelemetry** 00:54 Man.
No, I mean, for me, I think it's just this couple of days, and I haven't even turned on my heat.
Toughing it out a little bit, but yeah.
**Tyler Yahn (Splunk)** 01:04 Yeah.
**Nikola Grcevski @ Grafana / OpenTelemetry** 01:04 I have to wear… An extra layer.
It's gonna get warmer, apparently, next week again, so…
**Tyler Yahn (Splunk)** 01:12 Oh, really? Oh, okay. Yeah.
Yeah.
Yeah, it's definitely… there's definitely a few nights here that have definitely needed the heat.
**Nikola Grcevski @ Grafana / OpenTelemetry** 01:23 Whatever.
**Tyler Yahn (Splunk)** 01:23 Cooler here.
**Nikola Grcevski @ Grafana / OpenTelemetry** 01:24 Yeah.
**Tyler Yahn (Splunk)** 01:25 I mean, I think fall officially just started, like, yesterday? Yeah, so… Nikola Grcevski @ Grafana / OpenTelemetry 01:29 Something like 2 days ago, yeah.
**Tyler Yahn (Splunk)** 01:32 Yeah, yeah.
**Nikola Grcevski @ Grafana / OpenTelemetry** 01:33 Huh?
**Tyler Yahn (Splunk)** 01:39 Giuseppe, are you, you said you're southern Italy, right?
**Giuseppe Ognibene (Coralogix)** 01:44 Yeah, it's easily.
**Nikola Grcevski @ Grafana / OpenTelemetry** 01:45 Oh, okay. Okay.
**Tyler Yahn (Splunk)** 01:47 Yeah.
**Giuseppe Ognibene (Coralogix)** 01:48 Actually.
**Tyler Yahn (Splunk)** 01:49 Beautiful.
**Giuseppe Ognibene (Coralogix)** 01:49 Sicily and Tuscany. Some months in Sicily.
**Nikola Grcevski @ Grafana / OpenTelemetry** 01:53 Oh, yes?
**Giuseppe Ognibene (Coralogix)** 01:54 Tusk, yeah.
**Nikola Grcevski @ Grafana / OpenTelemetry** 01:56 Do you move around? Just with the seasons, or…
**Giuseppe Ognibene (Coralogix)** 01:59 following the My Heart, because my girlfriend, Nikola Grcevski @ Grafana / OpenTelemetry 02:02 And,
**Giuseppe Ognibene (Coralogix)** 02:03 works in Tusken.
**Nikola Grcevski @ Grafana / OpenTelemetry** 02:05 Oh, I see.
How far is it? I've…
**Giuseppe Ognibene (Coralogix)** 02:11 I don't know, one hour by flight?
**Nikola Grcevski @ Grafana / OpenTelemetry** 02:13 Right? Okay, okay. Oh, okay.
Yeah.
Still alive.
**Tyler Yahn (Splunk)** 02:21 So that's like a permanent summer then for you, right? It's always, always warm?
**Giuseppe Ognibene (Coralogix)** 02:27 More or less, yes.
**Tyler Yahn (Splunk)** 02:33 Cool. I'm looking at the… people in the car… oh, okay, there's Mario. And then, yeah, we've got, I think, a full agenda, or I'm sorry, a full, crew at this point. So yeah, if you haven't yet, go ahead and add your name to the attendees list.
And if you had agenda items you wanted to talk about, go ahead and add them there as well. I will start sharing my screen, and we can jump in here.
Momentarily… Okay.
Cool. Alright, awesome. So, start us off, Mario, you wanted to talk about a proposal to remove the Traceos info, metric, I'm guessing, and, talk about reasons?
**Mario Macias** 03:19 Yeah, basically the… the other day, I was normalizing cleaning up, our… our data, and I realized that these metrics… this metric is… Grafana-specific, I don't know, but it's what looks to me.
So I don't know whether these… It's worth maintaining this metric.
in the… in the OB code, or just… or… or just remove it, and we will maintain it in the… in the Vela site.
I've… I've been looking for… I googled for this name, I saw it appear in some Grafana documentation. It also appears in the QuoraLogix documentation, but I think it's just because, since the metric is there, it's listed, documented.
So if it's not really needed by anyone else.
I will… I will suggest removing it from the OB code.
**Nikola Grcevski @ Grafana / OpenTelemetry** 04:21 May I can explain what it… I mean, what it's used for, it's… for host metering. If anybody cares about this, it's like… people in a Grafana Cloud, we met her Based to host certain products, and they need this.
I don't know if anybody else needs it.
Yeah, some customers prefer host metering. They want to pay per host rather than per usage.
And… That's what it's used for.
**Nimrod Avni** 04:56 Is it something that you, like… if we remove it from OB, would you, like, maintain it on the Balo side instead?
**Mario Macias** 05:04 Yes.
**Nikola Grcevski @ Grafana / OpenTelemetry** 05:06 Okay.
**Mario Macias** 05:08 As you prefer. For me, it's fine keeping it in both sides, but… From time to time, I like to remove codes.
**Nimrod Avni** 05:15 Yeah, I mean, I'm for it too, like, I probably, like you said, in CoreLogix, it's only listed because it's copied from the documentation.
**Mario Macias** 05:24 Yeah.
**Nimrod Avni** 05:27 for us, it's fine removing it. I also try, you know, when I try to, like, clean up the metrics and do the, like, comparison between.
**Nikola Grcevski @ Grafana / OpenTelemetry** 05:35 among the.
**Nimrod Avni** 05:36 The Prometheus exporter and the Yota exporter, I ran into it, and I didn't know what it is.
**Nikola Grcevski @ Grafana / OpenTelemetry** 05:41 Goodbye.
**Nimrod Avni** 05:41 I'm fine with removing it.
**Nikola Grcevski @ Grafana / OpenTelemetry** 05:45 Excellent.
**Mario Macias** 05:45 Okay.
**Nikola Grcevski @ Grafana / OpenTelemetry** 05:47 Yep, okay.
**Tyler Yahn (Splunk)** 05:50 That sounds good, yeah, let's go ahead and… Nikola Grcevski @ Grafana / OpenTelemetry 05:52 You know what?
**Tyler Yahn (Splunk)** 05:52 Move it out, that sounds great.
Okay, awesome, so moving on, Nikola, you want to talk about CI as a bottleneck? Proposing merging the integration tests and running them in a single Docker image?
**Nikola Grcevski @ Grafana / OpenTelemetry** 06:04 Yeah, so I was just, realized with how many PRs people put out these days, which is great. We're making great progress, but, I mean, CEI is very slow. I think it's holding us up.
To move in faster, so I thought about this.
A lot of the tests are structured for integration tests, especially the way that Mario and I started long ago. Bela was only able to do sidecar mode. We didn't have multiprocessor support, none of that stuff. So we started kind of doing language by language.
sort of test. So you got, like, the Python test.NET test, this and this and that. So I'm thinking we could just have one composite image, like the multiprocess test is an example of this.
And then we just put them all.
in this one Docker Compose file, and just run all the tests on a single Docker Compose Build.
So instead of running… because once you actually go past the buildup of the Docker files and all the dependencies, everything else just goes real quick.
To actually execute the integration tests.
But it's a whole Docker bring up, teardown, and everything else that goes in between. So I think we can significantly cut the integration test times.
by combining all this, like.NET, Python, all this, make them listen on different ports, and just run all the tests individually as we do right now.
Because they won't collide or anything.
Essentially, we have a test like that, it's the multi-process test, but it was just specifically meant to test the multi-process support when we added it.
By then, we never cleaned up this old stuff.
And maybe we keep one or two around, just to test that sidecar still works.
When it's actually scoped to the container pit, rather than… the host bed.
Mario, you have a hand up?
**Mario Macias** 08:04 Yes, so I, I tried this, One, two years ago.
And it was a bit difficult, because the… the tests, you know, we always look for similar… when we look that the data point is produced, we look for similar path, or similar service name, so… but I think now it will be easier If we can rely on agents.
so we can just produce different type of data on each service. Imagine we have a Ruby.NET, Go, etc. So we should probably parameterize the name of the services, the paths we are… we are… so… so when we look for generated data, we make sure that we are looking for the generated data for that concrete service we are testing. But I think that currently with agents, that will be much easier than… That's what I'm thinking.
**Nikola Grcevski @ Grafana / OpenTelemetry** 09:10 in.
**Mario Macias** 09:10 Some, some, some time ago.
**Nikola Grcevski @ Grafana / OpenTelemetry** 09:13 Yeah, even, like, we can just make sure that all the queries that we do always hit, use a service name, and the service name must be unique across all of these.
for… we'll find them. And when service name is not discoverable, we can just hard-code it.
Yeah.
**Nimrod Avni** 09:33 I think we should probably… unless we want to test the, like, service name detection logic, we should probably hard-code it, because I also remember we had a couple instances like you did with the, like, naming of non-containerized whatever, and it broke the integration tests, so maybe we should just, like, hardcode every test with, like.
**Nikola Grcevski @ Grafana / OpenTelemetry** 09:56 Yeah.
**Nimrod Avni** 09:57 This is the service name based on, like, the name of the test suite or something?
**Nikola Grcevski @ Grafana / OpenTelemetry** 10:01 Yeah, yeah, yeah.
The logs would be larger, I guess, because they'll test all the services in one, so that Docker file, but… I mean, now there's split up files, so it will just be a longer download, and maybe A bit harder to kind of look for humans, but with agents now, I think.
Maybe not an issue.
**Nimrod Avni** 10:21 Indian, Yeah, I just need to make sure that, like, everything, I think you're gonna say, like, we'll have, like, one, let's say one, like, Jaeger instance, one Prometheus, just make sure that everything… is correct there, and also in Weaver, I guess that we need to… Just kinda see how we differentiate between… Nikola Grcevski @ Grafana / OpenTelemetry 10:44 Like…
**Nimrod Avni** 10:46 If one test fails, we want to kind of be easy for it to pinpoint… Which one? Yeah, I can check if there's anything… Nikola Grcevski @ Grafana / OpenTelemetry 10:54 Didn't we.
**Nimrod Avni** 10:55 They, like, do this by service name or something, I don't know, but…
**Mario Macias** 11:01 Yeah.
**Nikola Grcevski @ Grafana / OpenTelemetry** 11:02 Okay, okay.
But…
**Mario Macias** 11:04 Even in obscure… Nikola Grcevski @ Grafana / OpenTelemetry 11:06 Honestly, maybe the thing is, like, I start with combining at least per language.
We have, like, Python with this, Python with that, Python with this, that's just, like, 3, 4 that we can just cut and put them in a single Doc, I suppose.
Yeah. Go ahead, Mario.
**Mario Macias** 11:23 Yeah, no, also mentioning that the OpenTelemetry Collector is very powerful for this kind of stuff.
For example, we, at the beginning, we had the same test repeated for the OpenTelemetry exporter.
and for the… for the Prometheus exporter. Now, for example, in later tests, I just… we just have a single OpenTelemetry collector that collects both Autel and… And Prometheus, and just… just relabels. Set up a different pipeline, and say, relabel, like, collector equals hotel, collector equals Prometheus.
**Nikola Grcevski @ Grafana / OpenTelemetry** 12:02 So there we go.
**Mario Macias** 12:02 This, this, this could also help. I guess we can find some extra formulas for relabeling, or, or, or investigating, or identifying better the sources of the data.
**Nikola Grcevski @ Grafana / OpenTelemetry** 12:20 Okay, cool.
I think we can even do it with the oats tests.
I think oath tests now, same thing.
They start each one.
Build a Docker image. There's no reason why we can't just have one composite one and just have each O test Work on top of the… Yeah.
I can combine them.
**Tyler Yahn (Splunk)** 12:47 Okay, yeah, that sounds good.
**Nikola Grcevski @ Grafana / OpenTelemetry** 12:50 So it sounds like…
**Tyler Yahn (Splunk)** 12:51 prototypes, in the works, then? Yep. Yeah.
**Nikola Grcevski @ Grafana / OpenTelemetry** 12:55 I'm gonna try to make a couple of POCs go bit by bit, see how much I can clamp down. I'm mostly just gonna use agents to do the work for me. I mean, it's perfect for them.
**Tyler Yahn (Splunk)** 13:06 Yeah, absolutely, yeah.
Well, cool, alright. If that's the case, yeah, we'll look forward to the PR.
Nikola, you also have the next item, should we enable some small… some small, large buffers, by default, or handle the small record buffers as large buffers in the code?
**Nikola Grcevski @ Grafana / OpenTelemetry** 13:27 Well, I had this issue, Because we, I mean, I was writing this Ruby Rails new version test, and had a Postgres database backend, and… My SQL calls were not appearing.
I mean, I saw that we were making them in the eBPF traces, but we weren't actually parsing them, and… I realize it's because… It was just, large buffers were not enabled, so I enabled large buffers, and lo and behold. But that makes me think, like, our default configuration that we ship doesn't have them on, so maybe it's time. I mean, this feature has been there for a while. Maybe we add some defaults that are… Maybe not cool, but… I think it was some partial parse problem.
I don't quite… I think it is actually split.
I think in one case, it split the buffer into two. There was one first, like.
8 bytes or something that came through as a TCP buffer, and then there was a secondary part, but the secondary part, which is Missed the first chunk, and it couldn't parse.
Or with large buffers, we append them.
So I think it came, like, 8 bytes and then 256 bytes.
As the normal buffers.
So I thought that maybe what we should do is just kind of, like, I don't know, maybe… do the same logic with large buffers, from the small, tiny buffers that come on the record by default, or we just enable it and make it the default? Or something like, I don't know.
256, or even 512, so we… these protocols actually don't fail.
Just bring it in.
**Tyler Yahn (Splunk)** 15:20 Seems good to me, like, what's the memory impact from this?
**Nikola Grcevski @ Grafana / OpenTelemetry** 15:24 I mean, our diff… Our current, regular record that we have for TCP event is 256 bytes.
for the request, and I think $128 for the response, if I'm not mistaken. So, this would add up a little bit more if we go to 512, or something like that.
I'll have to investigate a little bit. I mean, I just wanted to get past the Ruby issue, so I just added large buffers and suddenly started working, and I was like, okay, I'll deal with this after in a follow-up.
But I… I need to look into… because I saw what was coming out with the payload printing, so I kind of… always sends one record, and then another record of the TCP.
So I was like, either we use the mechanics of the large buffers for the small buffers that come with the payload.
Yeah.
Matt?
**Matt** 16:21 Yeah, I was thinking maybe if we enable them by default, with a small buffer, like 256, we can just drop the… the hard-coded, not hard-coded, the buffer in the event that we have.
**Nikola Grcevski @ Grafana / OpenTelemetry** 16:35 Yeah, maybe that's the way to go. Then, 256 is a minimum, you can't set it… or maybe you can set it lower, but… You must have some… otherwise you set it to zero, you get nothing.
**Matt** 16:46 I think we… there should be no… No impact, like, memory-wise.
**Nikola Grcevski @ Grafana / OpenTelemetry** 16:52 Exactly. So, maybe that's the way to go.
Have, actually, large buffers.
on by default.
always, or we call them buffers now, I guess, and scrap the… The… the small payload.
Yeah.
That should actually eliminate Because right now, when you enable even 256, you gain nothing, technically, in terms of memory.
Of how much you have, because that's how the default has.
And you double the amount of bytes we send on the ring buffer, because once we do it for the large buffer, and once we do it for the actual record.
So… Yeah, okay, I just wanted to hear opinions on this, but I was gonna look into fixing this as a follow-up to the Rails.
4.0.
**Tyler Yahn (Splunk)** 17:47 I would… kind of ties into the next issue, but, like, I'd probably want to do this sooner rather than later, like, before the RC, so ideally in this next milestone.
So, if you could add, like, an issue, so that we could track it in this milestone, I think that'd be ideal. Because, like, I think we could do this after, like, a 1.0, but the impact… the potential impact, I think, is… it'd be helpful to be able to get it out before.
**Nikola Grcevski @ Grafana / OpenTelemetry** 18:14 Yeah.
**Tyler Yahn (Splunk)** 18:15 Yeah.
**Nikola Grcevski @ Grafana / OpenTelemetry** 18:16 Okay.
**Tyler Yahn (Splunk)** 18:19 Yeah, I mean, I like the idea, like, I don't… I think there's ways that we could start here, and then if we do have, like, memory issues.
**Nikola Grcevski @ Grafana / OpenTelemetry** 18:28 Thank you, you're welcome.
**Tyler Yahn (Splunk)** 18:29 Where we want to do further optimizations, we can always look at those in the future, but starting with, like, something where telemetry's actually shipping for users.
**Nikola Grcevski @ Grafana / OpenTelemetry** 18:35 Yeah.
**Tyler Yahn (Splunk)** 18:36 Pretty important, so, yeah.
**Nikola Grcevski @ Grafana / OpenTelemetry** 18:38 Yeah, because it's kind of weird, like, I think people just won't know what's happening, or it's just, oh, he doesn't work.
Right? I know.
**Tyler Yahn (Splunk)** 18:45 That's why they installed Obi, right?
**Nikola Grcevski @ Grafana / OpenTelemetry** 18:47 Yeah, and then… And I was like, wait, how come we can't tell Postgres? And I'm looking at thePF logs, and we recognize it, everything in our Postgres support, and just the user space just doesn't do anything with the event.
Because it's split.
Yeah.
**Tyler Yahn (Splunk)** 19:02 Yeah.
**Nikola Grcevski @ Grafana / OpenTelemetry** 19:04 It was… Yeah.
**Tyler Yahn (Splunk)** 19:06 Yeah, okay.
Okay. Yeah, I mean, that sounds great. I think we should do that.
**Nikola Grcevski @ Grafana / OpenTelemetry** 19:11 Okay, cool.
And I guess the next one is also me, because I haven't done that fix. Okay. Okay.
What's that?
Oh, I had… I thought it was one issue that you mentioned.
**Tyler Yahn (Splunk)** 19:25 Oh, yeah, I did mention an issue, but I just wanted to kind of, like, point it out. So this generic tracer, prevent duplicate trace injections, I closed it, is the thing I wanted to mention, and the reason I closed it is because I don't think it's actually, like.
achievable, and I think it's kind of just a limitation based on the way that, like, we're doing the HPAC, like, header stuff.
Essentially, what's going on here is that, like.
dynamic headers have already, like, shipped on some sort of connection, and at that point, OB starts, and, like, there's just really no way for us to recreate what that header, map is at that point. And so, like.
**I just don't think that there's a possible way. I mean, we could try to, like… honestly, I don't know what we're gonna do there, but, like, we could try to, like, do a best, like, defaulting, is the idea, but the idea that, like, we're gonna… Hmm, I think… Nikola Grcevski @ Grafana / OpenTelemetry** 20:22 Fixed.
**Tyler Yahn (Splunk)** 20:23 it is wrong, and we're probably gonna start shipping wrong to Lumtree at that point, so I think it, like, having this being a duplication is… I think it's just… you know, gonna have to be the way it is, because if we don't, like, if we're like, hey, I couldn't determine if this was, like, a connection that already has dynamic HPAC, like, headers set up beforehand, I'm not going to ship telemetry on here. We're just gonna miss, like, tons of, like, cases when OB is started on existing connections, right? So, like.
I just figured, like, that's just gonna have to be a limitation that we're gonna have to live with. And because of that, I closed it, saying that, like, this is just… this is just the way it is.
Like, we've already done a considerable amount of work to try to, like, catch, like, the cases we can, there's definitely, like, work to… there's great work that Macias was already doing on the HPAC stuff to try to, like, recreate things, work that I've looked at to try to, like, you know, make sure we're doing those as best we can, but at this point, I think it's just one of those things where it's, like, a limitation of OB in itself, the situation.
I do think that if you are able to have, like, bidirectional communication on, like, something with, like, the injector, so, like, say there is, like, a… a different telemetry system that has cog, like, context around, like.
this connection, maybe there's a way to integrate with that at that point, but, like.
outside of that, I don't… I don't really see a way to solve this. So… yeah, I just wanted to bring this up to everyone's attention, that I'm closing this as, like, a, not gonna… we're not gonna fix, it's not planned on the roadmap anymore.
**But yeah, it… Nikola Grcevski @ Grafana / OpenTelemetry** 21:54 Gotcha. Yeah, okay. And so… Right.
Right, because in order to find if there's already one, we would have to scan every field.
And then try to use the detection that Mattia added for HP encoded Transparent, right?
to see… The value looks like a trace ID.
**Tyler Yahn (Splunk)** 22:17 Kind… well, yeah, I think that's probably the way you'd have to do it, right? Like, because you could tell, like, the header value, like you're saying, so then maybe kind of say, like, well, in theory, this could be, like, a parent span or ID or something like that, right?
**Nikola Grcevski @ Grafana / OpenTelemetry** 22:31 But yeah.
**Tyler Yahn (Splunk)** 22:31 Yeah, but other than that, like… Even then, it's, like, not even… You know, what happens if party… Okay, go ahead.
**Matt** 22:40 I wanted to ask, does this happen, always, like, in all cases? Because I think, what I added was to… just to prevent this, like, we scan the value, even if it's HVAC encoded.
**And, if it looks, like, transparent, we… We don't adjust… Nikola Grcevski @ Grafana / OpenTelemetry** 23:01 You stand down. You stand down, yeah.
I think we have.
Fallback, there.
**Matt** 23:07 I think there is an edge case, like, right now we are scanning only for a lowercase, transparent, or some… something like that.
But we… by spec, we should also scan, trace parent with the big T or stuff like that, if I recall correctly.
**Nikola Grcevski @ Grafana / OpenTelemetry** 23:24 Yeah, dynamic table, so transparent is done. You don't ever see that key in the… So the only way to do it is by looking at the value, and if the value looks like a trace ID, which means… I mean, HPAC encoded value will probably have a signature of Trace ID.
some extent. Like, it has two dashes, it has hex numbers only, so that could be… potentially, kind of… determined.
There could be written a detector that kind of figures out, okay, this is an HPAC-encoded trace ID. It's not guaranteed to be 100% safe.
Any other.
**Matt** 24:04 I remember we have something that checks for it, like, that checks for dash at position, whatever, and position whatever.
It's in the gRPC path. I shouldn't be aware of that.
**Nikola Grcevski @ Grafana / OpenTelemetry** 24:18 I wonder if he used it to extract… I think you're looking… I think it's used right now to extract an existing transparent, so we can kind of continue on it.
But we don't… we don't probably… can maybe reuse it for duplicates, but I don't know if it's…
**Matt** 24:37 Hmm.
**Nikola Grcevski @ Grafana / OpenTelemetry** 24:38 Yeah, it's…
**Nimrod Avni** 24:39 I think regarding what you said with the, capitalization, I think… I think the issue is, like, if… even on the connection that we do know, a customer sends, like, a trace parent with, like, let's say, a capital T, we will, like, re-inject our trace parent.
So, like, in the case that, like, it already, like, we haven't seen it, and we want to read it from the HPAC values, I think it's only done by value, or, like, it should be done by, like, the shape of the value.
But maybe another issue… and no, Nick, if that's the issue, the customer… Or, like, I think it was Mario, but we also, I think, found something like it that can be… like, if someone sends it with any capitalization, it might do a double injection.
No, that?
**Tyler Yahn (Splunk)** 25:27 The capitalization stuff should be fixed.
like, I'm 99% sure I, like, actually recently just rewrote the string comparison stuff, and, like, there was a capital.
**Nikola Grcevski @ Grafana / OpenTelemetry** 25:37 We'll see.
**Tyler Yahn (Splunk)** 25:37 like, handle there.
**Nimrod Avni** 25:40 Okay.
**Tyler Yahn (Splunk)** 25:41 But… Yeah, but this is… this is more just, like, it has nothing to do with the key, for the.
**Nikola Grcevski @ Grafana / OpenTelemetry** 25:46 For the head.
**Tyler Yahn (Splunk)** 25:46 Right.
**Nikola Grcevski @ Grafana / OpenTelemetry** 25:47 Just like, cause, like.
**Tyler Yahn (Splunk)** 25:48 The key is, like, 21 or something like that. It's some sort of lookup for a map table.
**Matt** 25:53 We don't…
**Tyler Yahn (Splunk)** 25:53 have access to. Yeah, and so… It's, it's just, it's just the, the, yeah, the valley that's coming through.
**Nikola Grcevski @ Grafana / OpenTelemetry** 26:00 to report here.
**Tyler Yahn (Splunk)** 26:01 Which, I mean, I think, yeah, we could look at the heuristics, but I'm also, like.
**Nikola Grcevski @ Grafana / OpenTelemetry** 26:06 Over.
**Tyler Yahn (Splunk)** 26:07 like, this is an edge case, too, right? Like, you have something that's… that's… like, I think we could also just say, like, you know, that's what I said is, like, maybe just a recommendation is just, like, if you have these persistent connections, try to make sure that Obi's started beforehand.
**And that if that's the case, like, choose to either only use your, you know, manual interpretation, or use OB. Because, like, this is the case that comes in, is, like, it's only through duplication because, like, it already exists on that connection, right? So… Yeah, I mean, I think that, like, if we can… I don't know, it just seems like that's… Nikola Grcevski @ Grafana / OpenTelemetry** 26:41 No.
**Tyler Yahn (Splunk)** 26:42 I'm fine if we want to take a look at, like, value parsing, but, like, I do think that the heuristic approach there could be very, like, problematic as well.
**Nikola Grcevski @ Grafana / OpenTelemetry** 26:53 It won't matter.
**Matt** 26:53 Seeing that, oh, sorry.
**Nikola Grcevski @ Grafana / OpenTelemetry** 26:56 Yeah, sorry.
**Matt** 26:57 The thing that sucks with gRPC services is that they are always long-running connections, like, they always pre-exist.
**Nikola Grcevski @ Grafana / OpenTelemetry** 27:05 Hey, how about this? How about this? I think there's one thing we can probably do is, right now, when we stand down for telemetry generation, because we notice the application is exporting its own telemetry, we just stand down for the generation of metadata. But what we could do is stand down on context propagation.
So, an application that's already instrument that is doing its own OTEL is going to send telemetry, right? So we have the detection.
And we probably go through the… we just need a filter from… popular from user space that says, don't propagate for this pit. It's doing its own… Conflict propagation kind of thing.
You know what I mean? And then… because it's exporting its own traces, so therefore, don't bother with doing the context replication for it.
**Tyler Yahn (Splunk)** 27:55 So, like, don't… don't try to, like, match on… Nikola Grcevski @ Grafana / OpenTelemetry 27:58 Yeah.
**Tyler Yahn (Splunk)** 27:58 actual connection, just say, like, we know from configuration or from, like, detection at a higher level that the pit itself is doing something, so, like, we'll just assume that it's doing context replication as well.
**Nikola Grcevski @ Grafana / OpenTelemetry** 28:09 I mean, if it's exporting traces, it's probably doing context replagation. We don't want to mess with that.
**Tyler Yahn (Splunk)** 28:16 Is there ever a case, like, it doesn't have gRPC Instrumentation installed, but it's doing other things?
**Nikola Grcevski @ Grafana / OpenTelemetry** 28:23 I mean, it could, but that would be an edge case. I mean, they always have the option to disable it.
**Tyler Yahn (Splunk)** 28:27 Yo.
**Nikola Grcevski @ Grafana / OpenTelemetry** 28:28 But… I mean, those are the cases where we would end up… Causing grief.
**Tyler Yahn (Splunk)** 28:33 We could do both, even, right? Like, we could say, like, hey, this is a situation where it's in long-standing connection, like.
**Nikola Grcevski @ Grafana / OpenTelemetry** 28:39 Good.
**Tyler Yahn (Splunk)** 28:40 fall back to this, at least, right? Like, say, like, hey, from the top level, do you know if they're sending it? Then there's a pretty good chance they are, so I'm just gonna, like, stop.
**Nikola Grcevski @ Grafana / OpenTelemetry** 28:49 No.
**Tyler Yahn (Splunk)** 28:49 Yeah, I think that seems fair. Like, using the two as, like, a coupled reasoning seems like a good idea.
**Nikola Grcevski @ Grafana / OpenTelemetry** 28:56 Yeah, exactly.
**Tyler Yahn (Splunk)** 28:56 Boxing's hard.
No.
**Nikola Grcevski @ Grafana / OpenTelemetry** 28:58 No, it's not. Like, if we can't tell there was a trace ID and this service is exporting traces, I think we're gonna just stand down. We just need a map that's managed.
**Tyler Yahn (Splunk)** 29:10 Yay.
**Nikola Grcevski @ Grafana / OpenTelemetry** 29:10 user space?
When we detect that it's exporting its own telemetry, so… I think I have a question. So, when we do double trace ID, do we actually break the protocol? Does gRPC freak out?
Or do we just produce bad television?
**Tyler Yahn (Splunk)** 29:27 I think it's just, yeah, the backend telemetry starts to get a little wonky.
**Nikola Grcevski @ Grafana / OpenTelemetry** 29:31 So… so it gets wonky for one or two requests. We notice immediately that they're exporting traces, and we stand down in the propagation. Because really, I mean, if it's an OTL app exporting OTLP traces, they're doing complex propagation.
I don't know of any SDK that will… I mean, I guess it's possible that somebody would just do manual spans and export them directly and not do the rest of it. It's unusual, though, and… We… we… people have an option to turn this off if they really want this.
To be fair, Maybe we even… I can… just, this would be a performance optimization when you think about it. Right now, the standing down of exporting of telemetry only happens in user space. We practically just say, okay, we got an event from Mobi.
But this is telemetry of application, it's already exporting its own thing, so stop… stop sending these events, so we kill it at the pit filter, essentially.
But what I'm saying is, like, maybe that PID filter, we can push that signal all the way to eBPF, and then we disable your probes. It actually does not match in PIDs anymore. It's kind of like forbidden PID, if you will, or deny-listed PID, and so when the PID filter says, oh, should I handle this thing? We just say, don't handle it.
**Tyler Yahn (Splunk)** 30:55 Yeah, but how do we handle the fact that, like, we're trying to actually integrate with some of these SDKs now, right?
**Nikola Grcevski @ Grafana / OpenTelemetry** 31:02 I mean… Yeah, okay, fair enough. Like, maybe we can produce additional metrics or additional spans for them, yeah, that's fair, but the context propagation, we don't have to do. If they're doing their own traces, we can just disable the context prop, which is going to unbreak this case.
For a majority of people.
Sort of, maybe it'll let one or two requests go bad, and then after that, it'll sort itself out.
I don't know if I'm explaining it well.
No, I think.
**Tyler Yahn (Splunk)** 31:33 You are. I just… I haven't thought it all the way through. Like, I think I'd wanna… maybe we can capture this as an issue? Yeah, I can.
I did want to say, though, that, like, maybe for the V1, we hold off on this, and just go with this stance that, like, for right now, like, this is an edge case that we're not going to catch, and, you know, if we wanted to add this as a… fix down the road. That seems… that seems reasonable to me, but I'd say maybe we don't ship this for V1.
**Nikola Grcevski @ Grafana / OpenTelemetry** 32:01 I think it's doable, man. Let me write the issue I'll explain it in detail. I think it's pretty safe.
**Tyler Yahn (Splunk)** 32:06 Good.
**Nikola Grcevski @ Grafana / OpenTelemetry** 32:07 I don't think you'll have the case where you… if it's… application is just exporting metrics, then I… yeah, sure, we are doing traces, we should probably context propagate. But if it's… exporting just… traces on its own, and it's OTLP, It's a hotel app.
We probably don't have a business in injecting our own trace ID in there.
**Tyler Yahn (Splunk)** 32:29 Yeah, I mean, I see your point. I'm just… so, maybe just going… moving on to the next part of this issue is that, like, so timeline-wise, like.
we're coming up against it, to try to get this V1 out for early November. Like, ideally, I was thinking if we can get this V14 release out, which is a feature-complete, like, version that we want to get out.
**Ideally this week, maybe next week, Nikola Grcevski @ Grafana / OpenTelemetry** 32:56 Okay.
**Tyler Yahn (Splunk)** 32:57 Then that leaves us a two-week window with, having, like, having an RC come out, like, right after that, maybe a few days after that. So that's gonna be early October that we're looking at at that point.
Which means that, you know, having a two-week window of it letting it soak, before we do the full, you know, V1 release, like, the stable V1 release is mid-October, assuming that, like, there's… like, that's with the buffer that there's nothing wrong, right? Like, if somebody comes in and says, like.
there's, like, literal changes we need to make to the configuration or to something else, then we need to, like, do another RC, which would then be another two-week time period and restart the clock, right? So, like, any sort of, gotchas, like, we're coming right up against the wire for, KubeCon at that point. You know, any… our RC3 means we're not going to reach our goal, and we won't get that KubeCon deadline.
So, you know, with that in mind, like, I'm trying to… look at timeline on this, and again, I want to jump back into the V14.
Yeah, gotcha, yeah. A milestone, but, like, so, like, I did want to scope this correctly, and, like, I definitely want to talk a little more, because, Nimrod's doing some really great work on the telemetry stuff, and I think that, like, that's already… I think you need some help there, because, like, I think we're already a little bit at risk of not hitting these deadlines because of the stuff that we need to get done for that. So, I'm fine if you wanted to put some cycles into this, but I definitely want to make sure that, like, we're trying to hit these targets for timeline-wise, if that makes sense.
**Nikola Grcevski @ Grafana / OpenTelemetry** 34:30 Okay, well, I can focus on… focus on making sure that 14… I know I have an outstanding issue, I think, some duplicate request or something, I don't know. Was it this one? Or there was another one?
**Tyler Yahn (Splunk)** 34:41 Let's jump in here, actually, yeah.
**It is, it is in this one, yeah. I did want to ask you about that one as well, and seeing if we needed to get some… Nikola Grcevski @ Grafana / OpenTelemetry** 34:51 No, I just haven't looked at… I haven't looked at it. I think that's my…
**Tyler Yahn (Splunk)** 34:55 Yeah, so yeah, we can jump down here. So, this I haven't taken too much of a look at. I think I might have validated this months ago, but, I've looked at too many of these at this point.
**To be honest. So, yeah, duplicate spans with identical span IDs when GoHTTP client retries, yeah… Nikola Grcevski @ Grafana / OpenTelemetry** 35:17 Thanks.
I think I… yeah, I think it's… I think I have a suspicion of what's going on. I think I… This might have been actually fixed, but maybe it's not.
**Tyler Yahn (Splunk)** 35:33 Well, I can rerun the test that comes with this, and see if it actually is fixed on, like, the V13, or even on main right now, because that's what I'm thinking, too, like, I'm kind of wondering if this is fixed, but, Nikola Grcevski @ Grafana / OpenTelemetry 35:46 I mean, we definitely got rid of the $4.99, So that's reports as zero.
Yeah. But I wonder if… The next one is… So when I re… I wonder if this has to do with, the issue of me not doing the Go Wendy pros, but also it also sends data through the regular tracer, and in the case where I was wondering if there was a gap somewhere when the request fails and is retried, that I'm somehow duplicating it.
**Tyler Yahn (Splunk)** 36:26 Hmm.
**Nikola Grcevski @ Grafana / OpenTelemetry** 36:27 Yeah, there's some issue like that. Maybe… I was wondering if this first one… got sent.
through the regular U-Pros, but when we somehow made a ghost.
request through the KPRO path.
That's what I was worried about.
**Tyler Yahn (Splunk)** 36:48 I mean, there's definitely… I mean, this man name looks different as well, right? If I'm understanding this correctly.
**Nikola Grcevski @ Grafana / OpenTelemetry** 36:53 Yeah. Correct.
**Tyler Yahn (Splunk)** 36:54 So, like, there's definitely… Nikola Grcevski @ Grafana / OpenTelemetry 36:56 I don't know how we did that, to be honest, because OB will cut out this increase max by region, like, we would not… actually do the… I mean, we explicitly have code that cuts off everything after the question mark, so…
**Tyler Yahn (Splunk)** 37:11 Yeah.
**Nikola Grcevski @ Grafana / OpenTelemetry** 37:11 It's beyond me how we even generated that.
But… He's got a repro case, right?
**Tyler Yahn (Splunk)** 37:18 Yeah, yeah, and I ran it and found the same results, so, that was back in, the 12th of August, so that was a little while ago. We have had a lot of fixes since then.
**Nikola Grcevski @ Grafana / OpenTelemetry** 37:29 Yeah.
Okay.
**Tyler Yahn (Splunk)** 37:31 Yeah, so I do wonder, though, like, I could try rerunning this, and I can validate if it's there. I can start trying to jump in as well. I just… I wasn't jumping in because I saw you were assigned to it, so I didn't want to, like, step on your toes, but I'm happy to jump in as well.
**Nikola Grcevski @ Grafana / OpenTelemetry** 37:45 Sure. Yeah. Okay. I haven't had the time to look at it, I wasn't prioritizing it, but I completely forgot about this.
**Tyler Yahn (Splunk)** 37:52 Yeah. Yeah, well… Understandable.
**Nikola Grcevski @ Grafana / OpenTelemetry** 37:57 Okay.
**Tyler Yahn (Splunk)** 37:58 I will… I will take a look, and I'll coordinate with you on that. I actually finished up all the other issues assigned to me, so I'm happy to take this on and pick up some more work.
**Nikola Grcevski @ Grafana / OpenTelemetry** 38:04 Yeah, because there's two bugs there. One is this duplication, but the other one is we didn't cut off the span with… after the question mark, and I don't know how we did that, because that's an even more serious bug, because that's going to create a high cardinality metrics.
Because if we're not cutting off the parameters, there's things with privacy or security, people put all sorts of stuff on there.
Yeah, just two bugs.
**Tyler Yahn (Splunk)** 38:30 Yeah, I agreed. I'll double-check. I was looking at, I think, just the error codes last time I looked at this, but I can… Yeah, I actually don't know if I validated the span name to fail, like what we just saw, but I can take a look again.
Okay.
I did want to jump back in. I think that there's, the Rust Tokyo context propagation stuff, Giuseppe, I… unless, I think, you have a fix coming in in the next few days, we probably are gonna have to bump this, right?
**Giuseppe Ognibene (Coralogix)** 39:01 Yeah, yeah, I… sorry, I didn't have the time to work on that.
**Nikola Grcevski @ Grafana / OpenTelemetry** 39:07 Excellent, yeah.
**Tyler Yahn (Splunk)** 39:08 Understandable. I don't think it's a critical thing for the V1, though. We had only kept it in here because there was, like, active work, right? So, I think that seems… that's totally reasonable, if it seems the same way to you.
**Nikola Grcevski @ Grafana / OpenTelemetry** 39:21 I mean, that's a feature ad, to be honest, and…
**Tyler Yahn (Splunk)** 39:24 Agreed, yeah, 100%. So, OV1.1 totally can have this, in my opinion, yeah, so… So that leaves us with the registry stuff, and the telemetry contract stuff, which is, an endless thing. It's almost as… Maybe even worse than the…
**Nimrod Avni** 39:42 Maybe, I'm hoping I'm coming close, maybe, maybe.
Yes, I saw your comments on both of them, And I think, as I've written here, this one, I think, can go out of the V1.
Because… like, we do, like, we have, like, partial coverage, we basically, like, every signal that goes through, all the test integrations.
go through, Weaver, but we don't have anything that says, like, do we actually cover all the schema that… all the telemetry schema that we declare? And I said there that you suggested doing it via, like, kinda… reading from the Go declarations of the attributes and stuff like that, which is a good direction, but I think for a more complete… solution, we probably want to make sure that every, like, every signal that OB can produce is covered by an integration test that proves that it can, produce it, and then we do, like.
My thought was, like, taking all the suites, aggregating all the results, and then doing some, like, you know, like, score of, like, you know, we cover 90% of what we declare, and then, like, try to get it up to… 100. But, like, I don't think it's required for the V1. It's, like, more of a…
**Tyler Yahn (Splunk)** 41:02 Yeah, okay.
I think that makes… like, the only concern I'd have is, like.
We declare something in the schema that, like, we're never actually gonna include, but… I'm not, like… my risk there is not super high, I just… that was my only concern, yeah.
**Nimrod Avni** 41:18 Yeah, I'm hoping, like, I want to continue working on this even after V1, I'm just saying, like, it might… I can fix, like, specifically the .NET thing that's here, and try to do, like, an audit of that, and even at the… like, you know, the unit tests for it, but… Probably doing the full wiring will take a bit of time. I have some drafts for it, but it's stacked up on the other issue of the… Defining the scheme.
**Tyler Yahn (Splunk)** 41:51 Yeah, that sounds good.
Yeah, so then this, defining the contract then, right? Like, this one… you are trying to get done in the V1, right?
**Nimrod Avni** 42:01 Yeah, so I have, like, one… like, the main one is, do… like, I think I have… in addition to all the things that you, added, which is great, like, adding a telemetry MD and saying, like, you know, basically what we expect… what we expect to be, like, you know, stable.
And I try to think of, like, we should probably, take the stability, levels from OTEL, because we're trying… unless there are stuff of our own, let's say on, like, DNS spans, or span metric skip attribute, which we can, like, kind of declare of our own because we invented them, or any OB internal metrics.
But everything that has an upstream equivalent, we should probably, take the stability level from there and say, like, okay, like, HCP metrics won't change, but MCP spans might, because, you know, that keeps getting involved.
**Tyler Yahn (Splunk)** 42:54 Right.
**Nimrod Avni** 42:55 And… yeah, so, like, the… I think I have, like, kind of, like, a couple more, like, there's one that's open on, like, basically requirement level of attributes, if, like, if it's, you know, it's required, the opt-in can still require whatever, and there's another one of the exact, like, the stability of each signal, and then all the stuff that you mentioned, and I'm hoping… That should be enough. I think that that's, like, the… The end of that, rabbit hole, but… But I should get it done, like, I think it should be done in… I don't know, after reviews and stuff, it should be done before the V1.
**Tyler Yahn (Splunk)** 43:37 So, like, next week is… I'm hoping to get this V14 out, which is… does that seem reasonable to get this out?
**Nimrod Avni** 43:44 Yeah, I think it is reasonable, unless there's some long, like, review cycles, but I'll try to… Push that as soon as I can.
**Tyler Yahn (Splunk)** 43:53 Okay.
And then, out of the things that I listed here, is there something that I can help you with, or another person on the call that would want to step up?
**Nimrod Avni** 44:02 I'm happy to work.
**Tyler Yahn (Splunk)** 44:03 program this telemetry.md, if you wanted help there, but I'm guessing you probably have more context as well, so…
**Nimrod Avni** 44:09 Yeah, if you wanna… if you wanna take a look at that, that'll be, great, and, like, I think you can probably bundle it with… Like, adding references to it, and all that stuff.
**Tyler Yahn (Splunk)** 44:19 Yeah.
**Nimrod Avni** 44:20 And once you have it, I can, review.
**Tyler Yahn (Splunk)** 44:24 Okay, yeah, I can do that. And then, yeah, this other, like, the… this other stuff, I think, seems… seems totally reasonable, so… I will… I will also jump into this. Yeah, that sounds great.
**Nimrod Avni** 44:36 Okay?
**Tyler Yahn (Splunk)** 44:36 And then, for this one, I'm just gonna leave this in Well, actually, I'll move this, actually, right now, because I don't think we're going to get this done, right, is what you're saying? Like, this one's just too long-standing?
Okay, yeah, I'll move this to this milestone just to kind of keep track of it, but, mostly just to keep it in, like, a post V1.
We probably need a label that says, like, POST 1.0 or something like that, but… Okay.
So, that being the case, I will also bump this, Yeah, I'll pick any milestone or something like that at 1.1, and I'll put that and this, this other PR there.
But otherwise, I think we only have 2 issues… to resolve… Although, I'm already blanking. We talked about one earlier, Oh, yeah, Mario, we wanted to try to get this, removed in this milestone, I'm guessing, right?
**Mario Macias** 45:36 Oh, yeah, I think it's something very quick to do. I can send it here tomorrow. We're just removing a section or a few lines.
**Tyler Yahn (Splunk)** 45:45 So we'll want to add that, yeah, probably keep that in this milestone then, yeah.
**Mario Macias** 45:48 Yeah, I'll send the PR tomorrow.
**Tyler Yahn (Splunk)** 45:51 Okay.
And then also, Nikola, the issue for, the small, large buffers, or large buffers by default, let's, let's try to add that to the milestone as well.
**Nikola Grcevski @ Grafana / OpenTelemetry** 46:00 Yeah, I will… I will write the issue and align it to the milestone, and I can focus on that.
**Tyler Yahn (Splunk)** 46:07 Yeah, okay, that sounds good.
I think it… we have a pretty good line of sight on… getting this out next week and completing it, based on what we just talked about, so that seems… seems doable. Are there any concerns, or things that are missing, or things like, People want to bring up about this?
**Nikola Grcevski @ Grafana / OpenTelemetry** 46:26 Now, let's go. Let's go.
**Tyler Yahn (Splunk)** 46:28 Yeah, let's go. We're getting out of crunch time.
**Nikola Grcevski @ Grafana / OpenTelemetry** 46:31 Who's going to KubeCon?
North America, when we're gonna announce this.
**Tyler Yahn (Splunk)** 46:37 Yeah, Nikola Grcevski @ Grafana / OpenTelemetry 46:38 So… I'll be there. Me? You.
**Mike Dame (Odigos)** 46:40 million.
**Nikola Grcevski @ Grafana / OpenTelemetry** 46:42 Mike?
**Tyler Yahn (Splunk)** 46:43 It's gonna be there?
**Nikola Grcevski @ Grafana / OpenTelemetry** 46:44 Yeah? Okay.
**Mike Dame (Odigos)** 46:46 Raphael.
**Nikola Grcevski @ Grafana / OpenTelemetry** 46:47 Thanks.
Any of these?
**Tyler Yahn (Splunk)** 46:49 Yeah.
**Nikola Grcevski @ Grafana / OpenTelemetry** 46:51 Rafael's go.
**Mike Dame (Odigos)** 46:52 He's Canadian, right? Is that part of Europe? Yeah.
**Nikola Grcevski @ Grafana / OpenTelemetry** 46:55 Well, getting there.
**Mike Dame (Odigos)** 46:58 Showing my public education,
**Tyler Yahn (Splunk)** 47:06 Well, cool. Who's, who's going to KubeCon, EU next, march.
**Mario Macias** 47:13 Probably, myself, I'll be there, yeah.
**Tyler Yahn (Splunk)** 47:16 Yeah, it's in your backyard. I'd expect you to be there.
**Nikola Grcevski @ Grafana / OpenTelemetry** 47:20 Talks. Need to submit some talks.
**Tyler Yahn (Splunk)** 47:21 Yeah, we gotta start submitting some talks, I think is kind of the idea, yeah.
Cool. Alright, any other… Topics, I don't see anything else on the agenda that was added, double checking, yeah. Any other projects people are working on? Things top of mind? See, I see you got a hand up.
**Matt** 47:42 Yeah, I had a question about post-V1 release cycle. I wanted to ask if we will have, something like, Feature freeze, and, scheduled releases and stuff like that.
Is this planned, or do we proceed like we are doing right now?
**Tyler Yahn (Splunk)** 48:05 I mean, I think that's up for us to decide. I was just, like, assuming we would continue as what we're doing right now. We're actively working on, you know, milestones, planning them.
Yearly goals, maybe even, you know, smaller goal cycles as well, and then trying to get features out when they're done, but… Yeah, I mean, I… like, if you think more structure around this would be helpful to the community, would be helpful to… signaling our, maturity, like, I… open to any suggestions you have on this one. Or if you say, like, don't do that, like, that's also… I'm… yeah, I haven't thought about it, to be honest.
**Matt** 48:41 I think we need to think about this, because if we are releasing some more stable versions.
It's not good to merge new features, like, one day before the release, or soon.
**Nikola Grcevski @ Grafana / OpenTelemetry** 48:56 Yeah.
Well, maybe. Yeah. Or we have some more stabilization period, like release RCs and… Mmm.
And see how it goes.
**Tyler Yahn (Splunk)** 49:11 Macias, I, like… I think I'm more ignorant about that than you may assume, so if you wanted to, like, maybe, like, we could have, like, a discussion or an issue, or maybe even talk about it next meeting or something like that, like, I'm happy to hear, like, what your suggestions on it are, because, like, I… Like, literally just ignorant. Like, that, what you just said there sounds great, but it's also novel to me, like, I haven't thought through that, so, yeah.
**Matt** 49:36 Yeah, yeah, I'm speaking just… just… it's, it was just a… a thought of a recent thought.
Maybe I can, try to, to gather some, some informations, and we can discuss this in the next meeting. It's not urgent, anyway.
**Tyler Yahn (Splunk)** 49:52 Yeah, agreed. Yeah, but I… I think so. That sounds like a great idea, yeah.
Nikola, you also had your hand up?
**Nikola Grcevski @ Grafana / OpenTelemetry** 50:01 I had two things that I, that I had actually, well, first one, I… I just remembered. I was gonna bring it up, but I forgot to write it down, but I did remember now because of the release candidate. We had a report somebody attempted to use, The trace law correlation.
on Java, and they got some bizarre output.
So I'll try to find that one. Try to make a reproducer, actually. I think I could. They said that they got a bunch of zeros in the logs, and… correlation happened?
And so I think it's maybe Java-specific with what they do with, the logger is on a separate thread, or something like that. I'll try to reproduce it, so maybe if we…
**Matt** 50:50 Zeros in the TTY, or… Nikola Grcevski @ Grafana / OpenTelemetry 50:53 Yeah, yeah, they, they got a bunch of…
**Matt** 50:55 That's expected. If they didn't set up, like, a filter in the… In the log collector, that should be expected.
Because we have no way to… to, like, not to write to the pipe. We need to write exactly those number of bytes, but they will be zero.
That's basically the old log line.
**Nikola Grcevski @ Grafana / OpenTelemetry** 51:19 But how do they set a filter for that? Is it…
**Matt** 51:22 There are some examples in the docs, I can get them.
**Tyler Yahn (Splunk)** 51:28 Is this… this is the Slack conversation, Nikola, if I remember correctly?
**Nikola Grcevski @ Grafana / OpenTelemetry** 51:31 No, no, it's internal. Grafana, somebody opened an issue, but it's not even in the public repo. I can't even link to it.
So, came through our support channel, somebody tried it, and it said they see zeros. But I thought that we handled it, like, zero will not appear.
Okay.
Okay, I'll check this out.
So maybe it was that.
**Matt** 51:59 But, the logline… the loglines that are visible should be enriched.
**If there is a… Nikola Grcevski @ Grafana / OpenTelemetry** 52:08 Okay.
**Matt** 52:08 this context.
**Nikola Grcevski @ Grafana / OpenTelemetry** 52:12 So they need to clean this up. Okay, I didn't know about this. We don't have documentation on this on the Baylor side, so we haven't actually… We've officially told our customers that we shouldn't… they should use this, but Yeah, but I'll take a look at, I think they mentioned in there what kind of job application was it.
Yeah.
And you ask about interesting projects, and going forward, I… There was… an interesting request came from customers that we had, that they wanted to add Like, manual spans to… I mean, any service, really, but through, config in OB, not through actually modifying their code.
And I think we briefly discussed about this, I think Odigos, you guys do it, with Java, and I think Go, and maybe other stuff.
Maybe even more dynamic, rather than through config.
But… I think we can potentially do it post-1-0.
So essentially, it would be, like, you want to instrument this method in your… like, you're debugging something in production, you're not sure what's happening, you redeploy OB with a new config that says, in this process, in the selection criteria, you just say.
By the way, just add… Spans around this function calls.
And what that captures is, like, it basically sets a U probe and a red probe, and captures the arguments and the timing.
Mmm.
And we can do the same thing for the Java agent.
probably even the Node.js.
**Tyler Yahn (Splunk)** 53:59 Yeah, I mean, I… that's… that's…
**Matt** 54:01 I think we had the POC for this, for all languages. Maybe when I have more time, I can, Yeah, yeah.
**Nikola Grcevski @ Grafana / OpenTelemetry** 54:09 I closed it.
**Matt** 54:09 PR because, yeah, I closed the PR because, it was too big, it was unreviewable, but I can, And then maybe start with, with Go.
Because it's the most, Complete one. In God, there was actually, automatic retrieval of the arguments. So if there's a function, you can instrument that, and the arguments would appear.
Regardless of the… unless it's a special type, like a struct or something like that. Yeah, basic arguments would appear.
**Nikola Grcevski @ Grafana / OpenTelemetry** 54:45 We can get, like, scalars and strings, presumably. Yeah. Which is what most people care about.
**Tyler Yahn (Splunk)** 54:51 Can you detect if one of the arguments was the context, and, like, see if there's any context passed?
**Matt** 54:59 I don't remember what the code looked like.
I had to, to recover the PR.
**Nikola Grcevski @ Grafana / OpenTelemetry** 55:07 Yep.
**Tyler Yahn (Splunk)** 55:08 That's cool.
**Nikola Grcevski @ Grafana / OpenTelemetry** 55:09 I've actually… I know of some other products that even go beyond this. I started researching it a little bit, but for Java.
some products let you even define what to call, because ZAL is so… sort of dynamics, so you can call through reflection, actually call a specific function on that object. Let's say the customer knows that this object is of certain Type.
And then… They can just call, instead of just toString on it, they can just call… Run something else, and get the output of that, and… Dump it in a trace in a span.
That's pretty wild, but… Chihuahua.
**Nimrod Avni** 55:48 Yeah.
**Tyler Yahn (Splunk)** 55:49 Yeah. Right?
**Nikola Grcevski @ Grafana / OpenTelemetry** 55:50 Yeah.
**Nimrod Avni** 55:52 That sounds cool.
**Matt** 55:53 What's the, the link in the, in the chat? It's, the example in there is, is the Go one.
**Nimrod Avni** 56:00 Yeah, I like the idea of having, like, you know, like, per language, you probably want different attachment logic, because, like, U-probes and stuff is best for… Stuff like GoBub for Node.js and Java and whatever.
**Nikola Grcevski @ Grafana / OpenTelemetry** 56:16 And now Python actually supports dynamic agents, so we had a chance to do this for Python, too.
I think 314 or something supports injecting an agent, so we could potentially pull this off there as well.
That's four major languages. I think Node.js is doable as well. Node.js, everything is patchable.
I'm 100% sure we can…
**Nimrod Avni** 56:43 I think that might be a, like, a… like, to improve the, like, usability of this feature, if we can somehow make the config of Obi kind of, I think kind of like what you did, Mike, with, like, the PID attacher, but maybe even something more generic, like, Maybe… OPA, like, the OpenMP, like.
like, dynamic config reloading without restarting Obi?
It'll probably be complicated, but could be really cool.
**Nikola Grcevski @ Grafana / OpenTelemetry** 57:15 It's just a file watcher, and maybe we can't reload everything, but these rules.
**Nimrod Avni** 57:19 Maybe just, like, restart specific components instead of philosophy?
**Nikola Grcevski @ Grafana / OpenTelemetry** 57:23 That's right, yeah.
**Tyler Yahn (Splunk)** 57:25 I think that's gonna be the important part of this feature is, like, dynamically being able to find things, right? Because you're like… yeah. Also, like… There's the other side of things that would be really cool, is if you could have OB tell you what already exists there. Because it's one thing to go in and say, like, hey, I really want to instrument this function, but it's another thing to say, like, what functions does this program even have that I can instrument?
**Nikola Grcevski @ Grafana / OpenTelemetry** 57:47 Yeah?
Just to get a list of…
**Tyler Yahn (Splunk)** 57:51 Yeah, like, just surface, like, all the symbols, essentially, that we have, yeah.
**Nikola Grcevski @ Grafana / OpenTelemetry** 57:55 Yeah, we're… oh well.
Yeah, that would be cool, like a command line option, you can run it or something.
Or maybe, like, an API call.
**Tyler Yahn (Splunk)** 58:04 Right? Because then it's like.
**Matt** 58:05 Or maybe a single… Which, which will send you the whole, like, dumb thing.
**Nimrod Avni** 58:09 the binary. That's the log.
**Nikola Grcevski @ Grafana / OpenTelemetry** 58:14 Yeah.
**Tyler Yahn (Splunk)** 58:15 But honestly, this sounds like a really cool thing, like.
just kind of keep in mind, also, like, we are coming up on, like, the last quarter of the year, like, we probably want to start thinking about goals for next year. I think this is definitely one of those, that we could be shooting for as, like, major features being tried to add as we go, to 2.0 and beyond. Yeah, so, like, I think this is definitely a really cool idea.
Nikola, can you, like… I know, Macias has, like, a, PR, but, like, just maybe add a tracking issue for this so that we don't lose track of it, and we can, yeah, start working on it, or just communicating on it, talking about it.
But, yeah, I think this is great. I'm super excited about this.
Okay, we are coming up to the last minute here, so I did want to stop, make sure we're, respectful of people's time.
Thank you all for joining. I will see you all in a week's time. We'll hopefully be talking about releases, next week. So, yeah.
Until then, talk to you later.
**Nikola Grcevski @ Grafana / OpenTelemetry** 59:12 Bye.
**Nimrod Avni** 59:14 Alright.
