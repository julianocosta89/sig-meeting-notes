SIG: Community Demo App SIG
Date: 2026-09-02
Duration: 30 minutes
============================================================

## Zoom Recording Transcript

**Juliano Costa | Datadog** 00:15 Hello, hello.
**Felix Felix (IBM India Pvt Ltd)** 00:20 I… Hi, Juliano.
**Juliano Costa | Datadog** 00:23 How are you?
**Felix Felix (IBM India Pvt Ltd)** 00:24 I'm good.
audio.
**Juliano Costa | Datadog** 00:27 Good, good.
Don't know if you saw that I post, I mentioned you on LinkedIn.
I recorded a video… I recorded a video talking about the chatbot with a colleague of mine here at Datadog.
And then I tried the awning thing because, yeah.
**Felix Felix (IBM India Pvt Ltd)** 00:52 Oh, okay.
**Juliano Costa | Datadog** 00:54 You created the thing, so…
**Felix Felix (IBM India Pvt Ltd)** 00:57 Okay, I didn't get a notification, I'll check it out now.
**Juliano Costa | Datadog** 01:05 Cool.
I don't think… I know that Chennai won't be able to join.
**Felix Felix (IBM India Pvt Ltd)** 01:17 Agreed.
**Juliano Costa | Datadog** 01:18 You pinged me.
I have… he added one thing to the… To their agenda?
But we already kind of discussed that.
So, hey, Donal.
How are ya?
**Donal O'Sullivan** 01:42 Good, good, how are you?
**Juliano Costa | Datadog** 01:47 Good. Alive.
Surviving.
**Donal O'Sullivan** 01:53 Always good.
**Juliano Costa | Datadog** 01:55 Yeah.
I was mentioning to Felix that we have only one entry on the agenda for today, regarding a thing that we already actually discussed before.
About adding the… change log generator. I think it's a tool that will tell… I know that the collector… in the collector they use, the CH loggen.
**Donal O'Sullivan** 02:24 Yep.
**Juliano Costa | Datadog** 02:25 And Chenoy opened up PR to… to bring that in, yeah.
**Donal O'Sullivan** 02:33 Nice. No, that's definitely… that's a good addition. That's a nice tool. I use it a good bit, so it's… it's very handy.
**Juliano Costa | Datadog** 02:45 True. I see that you replied, Peter, here, on the…
**Donal O'Sullivan** 02:52 Yeah, the pod man… the podman issues… so, no, I was a good point, like, using root was weird, so I ended up, just updated the telemetry Dockerfile, so, like, it was using its work… its workspace, or its work there as, like, as root, so I just changed it to the home.
**Felix Felix (IBM India Pvt Ltd)** 03:09 Well, today I'm…
**Donal O'Sullivan** 03:11 So… Huh. Cool.
**Juliano Costa | Datadog** 03:14 That, that, that was me. That was me speaking, on Felix.
**Felix Felix (IBM India Pvt Ltd)** 03:22 Yeah.
**Donal O'Sullivan** 03:24 Oh, yeah.
But, Yeah, anyway, anyway, so yeah, I just updated the Docker file, so it's… it's now using the non-root user Weaver, so it… it's, it's… and it works both on Podman and Docker, and it's actually cleaner, because the… it shouldn't have been using root in the first place. It's only for the build step, but even before I added user root, it was still using the root there as the work directory, which is a bit weird anyway, you know, so… But yeah, it's… Cool. I've updated it, I'm not sure if all the checks are… Probably not familiar.
**Juliano Costa | Datadog** 04:04 they're still running, yeah. But whenever they pass, I'll… I'll just… I need to merge.
**Donal O'Sullivan** 04:12 Awesome.
Sounds good.
**Juliano Costa | Datadog** 04:14 Cool. The other… there is another… so I'll just add that to the agenda. I think here it's like… Great to go.
This one is also good to go.
And then there is this new… a really… awaited PR.
On adding purses to the demo?
I already gave a quick look, so the person that opened the PR What's his name? Augustine. His, he's missing one config on the front-end proxy, so we cannot actually access Persys. But the other… I mean, I haven't checked all the dashboards, JSON, I would test that whenever I'm able to visualize.
But, yeah, whenever that's working, I would… Go and merge.
**Donal O'Sullivan** 05:21 Cool.
**Juliano Costa | Datadog** 05:22 C…
**Donal O'Sullivan** 05:22 So, yeah, I had a quick, quick scan, just sorry to interrupt you there. So, they're not removing Grafana, so we're.
**Juliano Costa | Datadog** 05:28 I'm gonna find out.
**Donal O'Sullivan** 05:29 Kinda. We're gonna keep them side by side for now, is it?
**Juliano Costa | Datadog** 05:31 No, I would… I would remove Grafana.
**Donal O'Sullivan** 05:34 Yeah, that's… that would be the same. Yeah, I might comment here, just asking, could they remove Grafana altogether?
I think as well, was there… maybe I missed it, but I don't know if there was a Dockerfile for Percy's on it?
I guess they're…
**Juliano Costa | Datadog** 05:48 No, not really.
We don't know. They have just, the compose observability… PMO, where they had two volumes?
The provisioning and the config.yml.
**Donal O'Sullivan** 06:05 Okay.
Yeah, yeah.
**Juliano Costa | Datadog** 06:11 The only thing that I… I may push back a little is this cleanup interval of 1 hour. I don't know…
**Donal O'Sullivan** 06:24 I…
**Juliano Costa | Datadog** 06:25 I mean, I never run the demo forever, and whenever I run it for longer, I do not use Rafana to visualize my stuff, right? I use… Datadog, and I think all the vendors are doing the same, but, I don't know, maybe someone uses the demo to… To showcase stuff, and then this cleanup may be… Ms. Linney, or… I don't know.
Well, any opinions here?
**Donal O'Sullivan** 07:02 Yeah, like, I would have thought maybe it should have been… a shorter interval, I wouldn't have, yeah.
Like, we won't be using… we, like, yeah, our fork is obviously using a cabana, like Elasticsearch, you know, so, yep.
Yeah.
**Juliano Costa | Datadog** 07:25 Okay, so, yeah, let's, Question for you, not related to that. I was checking the… I was checking some Helm charts, and I saw that the Elastic doesn't use the… hotel PE endpoints.
You, you used the Elastic endpoint to ingest data?
**Donal O'Sullivan** 07:54 No, not necessarily. We… so we are using OTLP, so we have… so Serverless and ECH, so, like, Elastic Cloud Hosted are both using OTLP, like, managed OTLP, but then self-hosted is still using, the Elasticsearch Exporter from Collector Contrib.
Yeah, so… Anyway, why did you have a question about it, or…
**Juliano Costa | Datadog** 08:19 No, it was just… it just came into the discussion when we were talking about the Datadog exporter.
And, someone mentioned that Elastic was also using the Elastic Exporter, and I was like, huh? Really? I thought they had, like, OTLP one, but yeah.
**Donal O'Sullivan** 08:38 Yeah, because I think the community guidance is, I think, if you're to use OTLP, and if you use OTLP, you don't need your own bespoke exporter.
Is the, Is the argument. I think there's been a lot of deprecated exporters from Collector, because they're now using OTLP, but… I actually, funnily enough, I had a meeting today about this, and we're trying to have feature parity between OTLP and our Elasticsearch exporter. There's more features in OTLP for us on the ingestion site, and we have a few reasons why we want to keep it around the Elasticsearch exporter for now.
It's, yeah, look, pros and cons, but
**Juliano Costa | Datadog** 09:23 Yeah, I think that that's… that's the way it is for all the vendors that were there before OTOP, right?
You know, it's, it's tricky, yeah.
Okay, cool. Yeah, it was just, out of… out of curiosity.
**Donal O'Sullivan** 09:42 In… in the… in our fork, though, so on the… for the Elastic Hotel demo.
We don't use… so we're using OTLP now, we just… we just don't use the Elasticsearch Explorer anymore, so…
**Juliano Costa | Datadog** 09:53 By the way, that also brings me to another question. I'm updating the Datadog one.
**Donal O'Sullivan** 09:59 Okay.
**Juliano Costa | Datadog** 10:00 Do you also point, profiling to… to Elastic?
**Donal O'Sullivan** 10:05 We actually don't have profiling in the fork yet, unfortunately, yeah.
Kind of a… Some stuff… we're just waiting on some stuff internally.
I think we… yeah, we're… there's just a kind of a few things that have to happen. We… we have to update… Elasticsearch, I think Roger's actually kind of working on that. I think that's actually been done, so there's a couple things that have to be done before we can do that.
Because… Yeah, OTLP doesn't… does… I can't remember, OTLP, does that… that supports profiling?
Am I wrong there?
**Juliano Costa | Datadog** 10:43 No, it supports. So, like, the… the current… the current, setup that we have exports OTLP to FirePit.
**Donal O'Sullivan** 10:53 Oh, okay.
Oh, sorry, yes, oh yeah, for the, yeah, for, for the demo, but in terms of… so for us.
I'd ingest, you know, for telemetry ingestion… ingestion, can't even speak English, We, I'm not sure if we support profile in OTLP yet, so that's on the Elasticsearch side.
**Juliano Costa | Datadog** 11:18 As on the… okay.
**Donal O'Sullivan** 11:20 Yeah, yeah, yeah.
**Juliano Costa | Datadog** 11:21 If I'm not mistaken, yes, because… Two years ago, Felix and Damien were on stage at KubeCon presenting, profiling, and if I'm not mistaken, Damien, presented the… Otlp profile being…
**Donal O'Sullivan** 11:38 Okay, okay, yeah, yeah, because I… yeah, because I think you're right, because it's… I haven't looked at it, but it's one or the other. It's either the Elasticsearch exporter doesn't support it, and OTLP does, or it's the other way around, but I think you're right, I think it's the OTLP is actually supporting it, because that would make sense, I think.
Yeah, yeah.
**Juliano Costa | Datadog** 11:57 I'm… I'm… Yeah, I, I'm playing around, with Datadog, and, yeah, I just, yeah The trickiest part for me was getting a cluster that it actually worked. I didn't want to spin up a full cluster, so I tried Kind, I tried Minikube, I tried a bunch of other different configurations, but whenever I enabled profiling with the Helm chart, it crashed everything, so I.
**Donal O'Sullivan** 12:27 Really?
**Juliano Costa | Datadog** 12:27 BPF profiler, because I think Minikube has to have, some… trace, FS stuff, enabled, and I wasn't able to enable… so then I gave up, and I went to, GKE, spin up, spun up a cluster, and it worked.
**Donal O'Sullivan** 12:46 And then expired.
**Juliano Costa | Datadog** 12:47 I was like, huh, yeah.
I was like, oh, damn it, I spent, like, hours trying to make this work. I could have this cluster in a minute and test it.
But yeah, it looks cool, actually, and having the profiling being sent, too. The thing… And that's where my question is coming from. The thing is that, Datadog also has a… I think in Elastic, you also have another profiler that is not the hotel provider, right?
**Donal O'Sullivan** 13:21 Yeah, yeah, we have universal profiling, but that's the older kind of… that's… Kind of what we built before… so we donated the eBPF profiler to OTEL, but that's what we built internally for the Universal Profiler.
For a good… for a number of years, yeah.
**Juliano Costa | Datadog** 13:38 And you do have symbolization, right?
**Donal O'Sullivan** 13:41 Yeah.
**Juliano Costa | Datadog** 13:41 Yeah, so that's the thing, so whatever… whenever I send OTLP directly, I don't get symbolization, and the experience is kind of meh.
Yeah, because you just…
**Donal O'Sullivan** 13:53 They have byte addresses, or whatever.
**Juliano Costa | Datadog** 13:55 Yep.
**Donal O'Sullivan** 13:55 Yeah, yeah.
**Juliano Costa | Datadog** 13:56 Yeah, exactly.
**Donal O'Sullivan** 13:57 Yeah.
**Juliano Costa | Datadog** 13:59 But yeah, I'm still discussing with the team what is the best solution here. Let's see.
**Donal O'Sullivan** 14:06 Yeah.
**Juliano Costa | Datadog** 14:08 Cool. Okay.
Anything else?
**Donal O'Sullivan** 14:20 Oh, I think.
**Felix Felix (IBM India Pvt Ltd)** 14:21 I have a general question, which is not related to OpenTelemetry Demo, but with respect to OpenTelemetry Collector. Is it a good practice to write custom Autel collector processors?
For any, you know, specific requirements. So my requirement is to, you know.
So, we have an application which has a multi-line logs. For example, each transaction is indicated by a, you know, a bunch of logs.
which I can split by some delimiter, like, from one first delimiter to the second, it consists of one batch, okay? So, like, I'm assuming the application is not multi-threaded, so the logs are not interleaved.
So, each… each chunk will always give you some, you know, each, like, from one delimiter to another delimiter, you will always get only logs from one transaction. So, this is some assumptions that I am making. If that is the case, do you guys have any suggestion that is, like.
Can I use any custom… should I use any custom auto collector… auto processor, or can I leverage some existing processors?
**Donal O'Sullivan** 15:31 When you say custom, you mean write your own processor, is it?
**Felix Felix (IBM India Pvt Ltd)** 15:34 Yeah.
So, I'm trying to extract some kind of values and create a JSON from this chunk of logs.
And sometimes the chunk of… like, the chunk of logs can differ from application to application, which I can identify somehow.
So… Yeah, it's not just always one format, it can be different as well.
So I tried which will work for one single application, but if it's a mixture of different things.
**Donal O'Sullivan** 16:06 There is the logs… logs processor, Logs Transform processor. I haven't… I haven't… I don't really have experience using it, but you can… I think you can do, like, regex patterns and stuff like that.
So you can use that in, like, your telemetry pipeline.
In your hotel collector, and you can just specify… I guess you can… yeah, it looks like you can just, like, specify, like, a regular expression pattern, maybe.
So if you… if you… you're probably log… like, all your logs are probably in the one file, you can probably just crawl that, and it will process that, and you can grab whatever you want via regular expression.
**Felix Felix (IBM India Pvt Ltd)** 16:42 Okay, okay. So…
**Juliano Costa | Datadog** 16:44 The…
**Felix Felix (IBM India Pvt Ltd)** 16:44 What's.
**Juliano Costa | Datadog** 16:44 There is also the… Go ahead.
**Felix Felix (IBM India Pvt Ltd)** 16:48 log processor.
**Donal O'Sullivan** 16:50 Logs Transform Processor. I can put a link here.
Yeah, go ahead,
**Juliano Costa | Datadog** 16:56 We also have OTTL, right? That, basically you can use the transform, and, OTTL is OpenTelementary Transforming Language that you can use to break stuff down and do whatever.
It's super powerful.
I would, I would try this, this, the one that Donal, suggested first. If it doesn't work for you, then I would go for a transform processor.
And the last option would be creating my own thing, because the problem is not create… I think creating a component is… creating and deploying a component is pretty straightforward on Deflector. It's super extensible.
My main concern is, like, maintaining that forever, because then it's your component now, and it's super custom to your application, you cannot even contribute upstream and get help from the community to maintain and stuff, so yeah, that's the tricky part.
**Felix Felix (IBM India Pvt Ltd)** 18:00 Yeah, thank you. I'll check these two things out. Thank you.
**Donal O'Sullivan** 18:04 Yeah.
**Juliano Costa | Datadog** 18:06 And I… by the way, I know customers that have plenty of custom components all over, so yeah.
They need to remove one thing, they go create their own component, remove the thing, and that's… that's it. So, yeah.
Okay.
Any… anything else, anyone, right? I would call a day.
**Donal O'Sullivan** 18:39 All good.
**Felix Felix (IBM India Pvt Ltd)** 18:40 Hey, Mae, Courtney. Cool.
**Juliano Costa | Datadog** 18:42 Then, see you all next week. Cheers.
**Donal O'Sullivan** 18:44 Guys, bye-bye.
