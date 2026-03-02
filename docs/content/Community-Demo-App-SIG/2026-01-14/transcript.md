SIG: Community Demo App SIG
Date: 2026-01-14
Duration: 27 minutes
Zoom Recording URL: https://zoom.us/rec/share/UwJcwEw2cwq3WaQh2vHISiat1yaZk3GWruoKHwt4oP50R0Lvkm8QuNrXkuXoKtJ1.kksdBLtMftJhJBGb
============================================================

## Zoom Recording Transcript

**Cyrille Le Clerc** 01:18 Hello?
**Donal O'Sullivan** 01:24 Lou?
Oh, hoardings.
**Cyrille Le Clerc** 01:34 Finally, oh, you have beautiful northern lines behind you.
**Donal O'Sullivan** 01:38 Thanks.
**Cyrille Le Clerc** 01:41 Do you live close to… the north of.
**Donal O'Sullivan** 01:45 No, no, I wish. I'm in Ireland myself, so…
**Cyrille Le Clerc** 01:49 Let's.
**Donal O'Sullivan** 01:51 Yeah, yeah, it's my first time joining this SIG, so…
**Cyrille Le Clerc** 01:55 Okay.
**Donal O'Sullivan** 01:56 Just seeing what things are about.
**Cyrille Le Clerc** 02:00 I'm from Grafana Labs.
**Donal O'Sullivan** 02:02 Cool.
Oh, yeah, I'm from Elastic.
**Cyrille Le Clerc** 02:06 Oh, you're from Elastic, or I am an ex-elastic?
**Donal O'Sullivan** 02:10 Oh, okay, cool.
**Cyrille Le Clerc** 02:11 I used to work with, Alex Fedorjev.
**Donal O'Sullivan** 02:18 Alex… what's his last name?
**Cyrille Le Clerc** 02:20 Pedot, yeah, he was the PM lead for APM.
**Donal O'Sullivan** 02:24 Okay.
**Cyrille Le Clerc** 02:25 Only just left for Clickouts.
**Donal O'Sullivan** 02:27 Okay, interesting, yeah, I've only joined the last month, so I'm just getting up to speed. I know Roger, do you know Roger Call?
**Cyrille Le Clerc** 02:35 I discussed with him on Slack or on GitHub, but, just on allel stuff since I joined before I… yeah, he was not at Elastic when I joined.
**Donal O'Sullivan** 02:46 Okay, cool.
**Cyrille Le Clerc** 02:47 In which team are you at Elastic?
**Donal O'Sullivan** 02:49 I'm on the OLTEL data team, so mainly contributing upstream to Altel.
**Cyrille Le Clerc** 02:55 Okay, who do you, Alex Vert?
What his role, yeah.
**Donal O'Sullivan** 02:59 So he, he's Director of Engineering now, so.
**Cyrille Le Clerc** 03:02 Yeah, I saw this a promotion, yeah, yeah, hot market.
**Donal O'Sullivan** 03:05 Yeah.
**Cyrille Le Clerc** 03:09 Okay, who else is in a guy in Australia?
**Donal O'Sullivan** 03:14 Oh, yeah, I don't know him. I haven't met him yet, but yeah, you're right, there's a… I can't remember his name.
**Cyrille Le Clerc** 03:20 Wilkin?
**Donal O'Sullivan** 03:21 Yes, yes, you're right, yeah, yeah, yeah. I haven't met him yet, but I've seen him…
contributing to Old Telerife, yeah.
**Cyrille Le Clerc** 03:31 Okay. And you have dedicated upstream teams.
**Donal O'Sullivan** 03:35 Yeah, kind of, yeah, so, like, we're doing work for Elastic and doing… and work for Upstream as well, so…
It's kind of a bit of both.
Okay. How about yourself?
**Cyrille Le Clerc** 03:48 I am a product manager at Grafana Labs. I work a lot on,
Hotel support within our products.
**Donal O'Sullivan** 03:56 Cool.
**Cyrille Le Clerc** 03:59 on, within, Prometus on.
**Donal O'Sullivan** 04:03 Cool, interesting, yeah. Yeah, so I've been, myself, doing a bit of work on… so Elastic has a fork of the demo, so I did a bit of work on that, and
Been kind of poking around the upstream demo.
And, yeah, so it kind of led me here, then, just to join the,
the SIG, just to see what was going on.
**Cyrille Le Clerc** 04:25 Okay, in your fork of the… why do you have a fork of the demo? It's to connect elastic…
Technology.
my Zapps.
**Donal O'Sullivan** 04:33 We have our own, you know, the EDOT, or Elastic Distribution of OTEL, so… so, to demo that, we have a fork of the upstream demo, just to demo the EDOT collector.
**Cyrille Le Clerc** 04:44 Oh, yeah.
I'm pushing for something that may solve your goal.
I'm pushing for the idea that we should use the hotel operator to inject instrumentation.
**Donal O'Sullivan** 04:57 Hmm.
**Cyrille Le Clerc** 04:59 And so you would be able to wire eDot, just overwriting the…
**Donal O'Sullivan** 05:03 Hmm.
**Cyrille Le Clerc** 05:04 instrumentation CRDs or the hand charts to use the eDot version of the collector, and so on. But, so far, I have, limited,
success, I got pushback on using the operator, but I am pushing at the moment to use more the collector, yeah.
That's true.
**Donal O'Sullivan** 05:26 Interesting.
**Cyrille Le Clerc** 05:27 To use the collector also to do infrastructure monitoring, which was not the case so far.
**Donal O'Sullivan** 05:32 Yeah, interesting.
**Cyrille Le Clerc** 05:34 Because EU provides support for, hotel collector-based Kubernetes monitoring.
In addition to your own Elastic Agent-based monitoring.
**Donal O'Sullivan** 05:45 Yeah, I believe you're correct, yeah, yeah, yeah.
**Cyrille Le Clerc** 05:49 So I guess you would be interested as well to have the demo out of the box.
Showcasing Kubernetes monitoring in addition to just application monitoring.
**Donal O'Sullivan** 05:58 Yep. Yeah, exactly, yeah, yeah.
**Cyrille Le Clerc** 06:01 So I'm, I am pushing a PR on this at the moment.
**Donal O'Sullivan** 06:05 Okay, interesting.
That's on the hotel demo site, obviously, is it?
**Cyrille Le Clerc** 06:09 On the Helm chart side.
**Donal O'Sullivan** 06:11 Yeah, yeah, I gotcha. Yeah, of course.
Yeah, yeah, yeah.
**Cyrille Le Clerc** 06:15 It's… I will just share the link.
And I, no, I didn't loop in,
Roger on this one, I think I looked him in on some other stuff.
But.
**Donal O'Sullivan** 06:32 Okay.
**Cyrille Le Clerc** 06:33 quickly, I want to materialize into… Nope.
**Donal O'Sullivan** 06:39 He's not.
**Cyrille Le Clerc** 06:43 Not on this one, but yeah, this is the idea to enable,
Kubernetes monitoring, Linux monitoring out of the box, and also to,
Showcase the hotel collector receiver creator pattern.
So that when you want to monitor your Redis, your Postgres, your Kafka.
Instead of modifying your collector configuration.
You just annotate your workloads.
**Donal O'Sullivan** 07:14 Hmm.
**Cyrille Le Clerc** 07:15 with the Kubernetes annotation, so you have a… you change the roles and responsibilities.
**Donal O'Sullivan** 07:20 Yeah.
**Cyrille Le Clerc** 07:21 The deployer is in charge of describing their monitoring.
**Donal O'Sullivan** 07:25 Hmm.
**Cyrille Le Clerc** 07:27 On, if I'm not wrong, it's, elastic as… Initiated the receiver creator.
**Donal O'Sullivan** 07:34 Okay, yeah, no, I kind of get you. Okay, so…
Yeah, do you have a link to the PR?
**Cyrille Le Clerc** 07:42 I just dropped the link in the.
**Donal O'Sullivan** 07:44 A running node of the SIG.
Oh, perfect, yeah, yeah.
**Cyrille Le Clerc** 07:49 I can share this.
Yeah, here.
**Donal O'Sullivan** 07:56 Oh, okay, interesting.
Hmm.
Yeah, I'd have to have a look at it. I'm not hugely familiar, so,
It definitely sounds interesting, that might save a lot of… I love it.
**Cyrille Le Clerc** 08:21 Yeah, it's showcasing, hotel collector receiver creator on,
Hotel Collector deployed on, pods? No, on nodes, as a demand set.
**Donal O'Sullivan** 08:32 Yeah.
**Cyrille Le Clerc** 08:32 To enable also,
Kubernetes monitoring, and to do so, I had to contribute, if you're familiar with the hotel collector, when you deploy the collector as a demand set to collect stuff like cluster metrics, you need the leader election.
**Donal O'Sullivan** 08:53 Okay.
**Cyrille Le Clerc** 08:55 Because you don't want every Kubernetes node to collect your.
**Donal O'Sullivan** 09:01 Yeah.
**Cyrille Le Clerc** 09:01 central metrics.
And so you need the leader election mechanism, and it was not available in the presets of the hotel collector hand chart, and so I had to contribute
Okay. Presets that work as a demand set, not only as a gateway.
**Donal O'Sullivan** 09:19 Okay, yeah, I kinda got you. This is all new for me, so.
**Cyrille Le Clerc** 09:22 Okay, yeah.
**Donal O'Sullivan** 09:23 Interesting, yeah, yeah. Yeah, I, I, like, I can, I can have a look at the PR anyway, and, go through it and see if it makes sense.
**Cyrille Le Clerc** 09:31 Okay. Are you going to Hotel Unplug, the conference, at the end of the month?
**Donal O'Sullivan** 09:36 No, I won't be. That's in… that's in Belgium, I believe, is it?
**Cyrille Le Clerc** 09:41 Yes, Brussels.
**Donal O'Sullivan** 09:42 No, I'm not. I know, I think Damien is going, I don't know, do you know, do you know Damien? He's on my team,
No, I won't be going, unfortunately. And I noticed the KubeCon conference as well, but I won't be able to get to that one either. Hopefully.
Down the line, I'll get to them.
**Cyrille Le Clerc** 09:58 Are you more a new hotel collector? Yeah, I will go.
**Donal O'Sullivan** 10:01 Cool, cool, cool.
**Cyrille Le Clerc** 10:03 what is your focus? Is it hotel collector, or hotel SDKs, or OPAMP, or.
**Donal O'Sullivan** 10:08 Hotel collector mainly, yeah, so it's kind of like Hotel Collector Contrib, Hotel Collector, yeah, and…
**Cyrille Le Clerc** 10:16 Which components?
**Donal O'Sullivan** 10:18 At the moment, host metrics receiver.
So I've been kind of working on that, and maybe Kate, there's the K8s,
Kubernetes one as well, but… yeah, yeah, Skates attributes, yeah, but I haven't done anything there yet, so… just still getting up to speed.
**Cyrille Le Clerc** 10:37 Okay.
**Donal O'Sullivan** 10:38 Yeah, put me on the post-metrics receiver. Yeah, I'm trying to get a new metric in their system, memory shared, but have to make some changes to semantic conventions at the minute, so…
as it's a Linux-specific metric, it's meant, so… but yeah.
**Cyrille Le Clerc** 10:52 Okay, that you need for your,
Host monitoring, capabilities on that you need to get, ported in,
In hotel that you get in the Elastic Agent today.
**Donal O'Sullivan** 11:04 Yeah, yeah, yeah, yeah, yeah, yeah, exactly, yeah, yeah.
**Cyrille Le Clerc** 11:07 Yeah, it's a question of… yeah, sometimes I, I pinged, Roger thing…
Yeah, this metric is not enabled by default on… It's sad.
Well, I guess you need it in Elastic, so instead of having tons of…
YAML config, just let's make it, activated by default on a…
**Donal O'Sullivan** 11:26 Yeah, yeah, yeah, yeah. They're, they're… so we're… I know upstream, they're trying to get, you know, host metrics stable, so they're probably trying to not… yeah, we're trying… probably trying to get away from making changes, but
Yeah, it's probably a bit away as well at the moment, so… Okay. You probably know more about that yourself.
**Cyrille Le Clerc** 11:45 No, I'm not, I'm a lot on the usability at the moment.
**Donal O'Sullivan** 11:52 Okay.
**Cyrille Le Clerc** 11:53 So yeah, contributing to LChart so that it's easier to… you have less boilerplate.
**Donal O'Sullivan** 12:00 Yeah, yeah, yeah.
**Cyrille Le Clerc** 12:01 And now I am looking at, meta monitoring.
Because when you deploy,
When you deploy, hotel collector, when you deploy hotel operator, and you say, okay, now, everything is instrumented, it works.
They have no… conclude, on, we need,
If something goes wrong, how do I troubleshoot?
**Donal O'Sullivan** 12:30 Okay, great, yeah, yeah.
Okay.
**Cyrille Le Clerc** 12:33 Today, if you look at the helm charts,
of Collector or CubeStack and chart,
Nothing is made to help you to, monitor your collectors or your hotel operator.
**Donal O'Sullivan** 12:51 Right, okay.
Okay, so, like, so from an end-user point of view, the difficulty is if something goes wrong, they don't know how to fund and fix it? If you say.
**Cyrille Le Clerc** 13:01 I don't get my data in.
**Donal O'Sullivan** 13:03 Yep.
**Cyrille Le Clerc** 13:05 Say, where shall I look at?
**Donal O'Sullivan** 13:08 Yeah, okay, interesting.
**Cyrille Le Clerc** 13:10 And we can do a lot better, I think.
**Donal O'Sullivan** 13:13 Yeah, you'd need to have a lot of background knowledge, maybe, to just, like, use the tools to figure out what's going on.
**Cyrille Le Clerc** 13:21 I mean, that's not… there is no reason for this.
**Donal O'Sullivan** 13:24 Hmm, hmm.
How are customers using it at the minute? Are they just taking the Helm chart and deploying that, and…
**Cyrille Le Clerc** 13:32 what happens often is you say, oh, you will instrument your application like Java, it will go through a collector, and it will go to…
the observability backend.
**Donal O'Sullivan** 13:41 Only if the customer said, I cannot see my data.
**Cyrille Le Clerc** 13:45 The nightmare begins.
**Donal O'Sullivan** 13:47 Right.
**Cyrille Le Clerc** 13:48 Can the customer have an indicator from the collector saying, I'm up and running?
**Donal O'Sullivan** 13:55 Hmm.
**Cyrille Le Clerc** 13:56 can this collector report,
Here are the metrics I receive in, here are the metrics I successfully export or I failed to export.
or I fail to receive, it's hard to get all this.
**Donal O'Sullivan** 14:09 Yeah, yeah, interesting, yeah, yeah. So, like, you need some kind of…
status of your collector. Yeah, so essentially, they're looking at the… the backend, and it's basically an error on the… they're in some UI, and it just has an error saying, like.
**Cyrille Le Clerc** 14:22 Well, you just say, I don't see it.
**Donal O'Sullivan** 14:25 Yeah, yeah, yeah, interesting, yeah, and then…
Yeah, and then, yeah, yeah, and it's a long process just to figure out… fault line and figure out what's going on.
**Cyrille Le Clerc** 14:33 Yeah. On, something else, and I think, Elastic has not worked on it yet, you… you rely on the… you promote the hotel operator, and I love the hotel operator.
But how do you know if the hotel operator has successfully instrumented a pod?
**Donal O'Sullivan** 14:49 Yeah, okay, interesting.
Are you thinking? Oh…
**Cyrille Le Clerc** 14:53 And so the customer say, I don't see my data, and maybe it's because the hotel operator failed to instrument the pod.
**Donal O'Sullivan** 15:00 Yeah, yeah, yeah.
**Cyrille Le Clerc** 15:01 How do you measure this?
**Donal O'Sullivan** 15:02 Yeah, yeah.
Hmm.
**Cyrille Le Clerc** 15:04 If the hotel operator is producing internal telemetry.
**Donal O'Sullivan** 15:09 Hmm.
**Cyrille Le Clerc** 15:09 But it's only Prometus-style metrics.
It's not exporting with OTLP.
**Donal O'Sullivan** 15:17 Oh, okay. Interesting. Maybe that's the problem then, is it?
**Cyrille Le Clerc** 15:22 That's one part of the problem.
**Donal O'Sullivan** 15:25 Yeah.
**Cyrille Le Clerc** 15:25 For sure.
**Donal O'Sullivan** 15:27 Second part of the problem…
**Cyrille Le Clerc** 15:30 the metric names… suck to me. I don't like them.
**Donal O'Sullivan** 15:35 Hmm.
**Cyrille Le Clerc** 15:37 But first, I struggle because it's exposed as Prometus. I'm Grafana Lab, so it's easier for me. It should be my sweet spot, but
it's still hard to discover where is your, because it's permitted, so you need to scrape them, so you need to configure a component to scrape them, it cannot export. Yeah, yeah, yeah, yeah, yeah.
**Donal O'Sullivan** 15:58 on a U…
**Cyrille Le Clerc** 15:59 to provide good support to a user, I guess you would need to provide this.
**Donal O'Sullivan** 16:05 So is it the hotel operator metric names are bad, you're saying, is it?
**Cyrille Le Clerc** 16:10 I don't like them.
**Donal O'Sullivan** 16:11 Yeah, like, there's prob… yeah, there's probably… semantic conventions would be where.
**Cyrille Le Clerc** 16:17 Not for this yet, yeah.
**Donal O'Sullivan** 16:19 There isn't any, okay.
**Cyrille Le Clerc** 16:20 Nope.
**Donal O'Sullivan** 16:21 Okay, interesting.
That'd be worthwhile creating them if…
**Cyrille Le Clerc** 16:24 Yeah.
**Donal O'Sullivan** 16:25 Yeah.
**Cyrille Le Clerc** 16:26 But for the OpenTeametry Collector metrics, internal metrics, I hate them, but at least I can make sense of them.
I hate them because in the metric name, you have the…
telemetry types you monitor. So, for example, you have a receive success.
**Donal O'Sullivan** 16:44 Hmm.
**Cyrille Le Clerc** 16:45 So you have, the signal type, trace metrics logs, is in the metric name, rather than being a metric attribute.
So if you want to, on a dashboard or on an alert, to monitor ingestion success or failures.
**Donal O'Sullivan** 17:03 Yeah.
**Cyrille Le Clerc** 17:05 You need to create 3 metric queries rather than one, because there are 3 distinct metrics names, one for traces, one for metrics, one for logs.
**Donal O'Sullivan** 17:12 Yeah, yeah, yeah, yeah, yeah, yeah.
The three golden signals of observability.
**Cyrille Le Clerc** 17:18 Only… but we have some hotel collector components, which.
**Donal O'Sullivan** 17:22 Production.
**Cyrille Le Clerc** 17:23 use internal metrics where they have an attribute, that's called hotel signal, where you have… it's either a tracer metrics or log. And, yeah, there are some stuff like that. I think we can greatly improve the…
Monitoring ability of, hotel Corrector.
For humans, not just for specialists.
**Donal O'Sullivan** 17:43 Yeah, yeah, interesting, yeah, yeah.
Do you do… so you… you're… sorry, where are you working again, Cyril? Graphana. So you… like, your dashboard, can you… you can… can you configure to look at attributes now, or…
**Cyrille Le Clerc** 17:57 I have very verbose queries to do it, it's a nightmare to order them. It took me 3X the time that it should have taken, because,
**Donal O'Sullivan** 18:06 Yeah.
**Cyrille Le Clerc** 18:06 Most of the metrics are not… and they are misaligned with the philosophy of Semcont metrics.
**Donal O'Sullivan** 18:12 Yeah, I getcha, yeah. And then a SEMCOM change, it breaks the downstream, yeah, yeah, yeah.
Yeah.
Yeah. Have you, have you spoke, have you gone to SEMCOM, SIGs, or anything like that? No. Talk about that?
**Cyrille Le Clerc** 18:26 But yes, they are not yet talking about, putting some conv on,
internal telemetry, and I think we have bigger fish to fry, like, RPC metrics table, and then messaging metrics table.
**Donal O'Sullivan** 18:45 Yeah, stability is the big one at the moment, I think, isn't it? Because I think OpenTelemetry itself is not stable, right?
There's a CNC?
**Cyrille Le Clerc** 18:53 Yeah.
**Donal O'Sullivan** 18:54 Yeah.
**Cyrille Le Clerc** 18:54 stability on implementation in the SDKs.
**Donal O'Sullivan** 18:59 Okay.
**Cyrille Le Clerc** 19:00 Yeah, with eats, I mean the SDK is not just as a piece of paper, but really actually produced by SDKs.
**Donal O'Sullivan** 19:07 Yeah, yeah, yeah, yeah, I gotcha.
Yeah, interesting.
Cool.
And… so, so regarding the hotel demo, anything interesting?
**Cyrille Le Clerc** 19:21 So, at the moment, I'm working on the meta-monitoring on the demo.
So, adding, plugging, hotel collector monitoring in the demo.
That's my, my focus.
**Donal O'Sullivan** 19:34 Yeah, as you, as, as you said, okay, interesting, yeah, yeah, yeah. Yeah. I, I was just, I was just looking at the upstream…
repo today, just looking at stuff to pick up, and I was… I noticed,
there was an issue there in around… you know, I think Flag D is… so…
Flagd doesn't work when running it via Kubernetes, so I was gonna take a look at that.
**Cyrille Le Clerc** 19:58 For me, it works, but it's fragile. Sometimes it's broken. Like, the UI is sometimes broken.
**Donal O'Sullivan** 20:04 Hmm. Is that when you run it locally, is it?
Are you running…
**Cyrille Le Clerc** 20:10 I even got it broken on DigitalOcean. So, yeah, sometimes it's broken, full stop.
**Donal O'Sullivan** 20:16 Yeah, because I'm just trying to run it locally, and it's… yeah, it's broken, just keeps crashing, so… I know there's an open issue there, I've been trying to,
get it to work locally, so I might, I might, I might look at that.
Yeah.
**Cyrille Le Clerc** 20:32 The load injection is to evaluate.
**Donal O'Sullivan** 20:36 Load… sorry, load injection? Yes, I forgot the name of the tool that is being used, the load generator, but it's so big.
**Cyrille Le Clerc** 20:44 On us, but…
**Donal O'Sullivan** 20:46 That's not for Flag B, you know?
**Cyrille Le Clerc** 20:49 No, it's the, I forgot the name of the load injection technology.
**Donal O'Sullivan** 20:53 Oh, I know what you're talking about, yeah, yeah, yeah. Is that… that's another issue, is it?
**Cyrille Le Clerc** 21:00 And some people, I think there are… there are even some people from,
Elastic, who reported that this, locuster.
**Donal O'Sullivan** 21:09 Yeah, Locust Load Generator, I think is it.
**Cyrille Le Clerc** 21:11 Yeah, and it's so big, on the last problem I have, you cannot do anything for this is open search. The image takes so much…
**Donal O'Sullivan** 21:22 Open search. Yeah.
**Cyrille Le Clerc** 21:23 But here I have something also. As I work at… I recently contributed,
in the demo, an OpenTemmetry Collector dashboard that monitors export failures.
On, you see, export to Prometheus works well, to Jaeger works well. On where do you have export failures, open search, because…
Yeah, it's big, it doesn't work well on a small container as we do.
**Donal O'Sullivan** 21:50 Okay. Okay.
Interesting, yeah, open search. And that's a fork of Elasticsearch, I believe.
**Cyrille Le Clerc** 21:56 A long time ago, yeah, when, we will not name them, but, fucked up with, open source license at Elastic.
**Donal O'Sullivan** 22:04 Yeah, yeah, yeah, yeah.
**Cyrille Le Clerc** 22:06 getting the Elastic license rather than using AGPL or something that the market would have known.
**Donal O'Sullivan** 22:12 Yeah, yeah, interesting. So… so there's a couple issues, like FlagD has resource issues, and the load generator is just consuming way too much resources, essentially, isn't it? Yeah. Is what you're saying?
**Cyrille Le Clerc** 22:25 Yeah, I think the solution for Locust is to replace it with something like K6.
But it's not crushing. As you said, Flagdi, it's really crushing, so it's a pain.
**Donal O'Sullivan** 22:36 Yeah, yeah, yeah, I have to… yeah, I've been doing a bit of… kind of a deep dive into it, and I think I might have found a fix, but I'm not sure. There is a… there's an open issue there, so if I can get the, get it working locally, I might open a PR for… just to… just to fix it.
That's a good one about the, is there an open issue for the load generation replacement?
**Cyrille Le Clerc** 22:54 Yeah, there is one.
Okay, cool. I think there are some about locations.
Yeah, some other stuff,
we should have… I would like us to have, hotel eBPF profiling, which is a donation from Elastic in the demo.
**Donal O'Sullivan** 23:12 Yep.
Yeah. It's not in the demo yet, though, right? No.
Yeah, so, like, half of my team, they developed the eBPF profiler, so…
I'm not familiar with it, but that's.
**Cyrille Le Clerc** 23:25 Oh, they are the… but no, they all left, no, the creators of,
Portalizer, I think the left elastic, the one who were acquired.
**Donal O'Sullivan** 23:35 Oh, yeah, the company, wasn't it? Yeah. Well, I don't know, maybe the founder left, I'm not sure, but I know Christos is here, Stephanie's here.
Okay. If you're Florian as well. But, yeah, that's… I could… that's something I can…
You can look at as well, that might be an intra… is there… is there an issue for that one as well?
Nope.
**Cyrille Le Clerc** 23:57 Mmm, I don't think so.
But for me, we should have the eBPF profiling, As part of the demo.
**Donal O'Sullivan** 24:08 Hmm.
**Cyrille Le Clerc** 24:09 And if I were there, and I am also on some threads about it, I think that Hotel eBPF profiler should be manageable through the hotel operator.
**Donal O'Sullivan** 24:20 Okay, I'm here.
**Cyrille Le Clerc** 24:21 You will… hotel operator now is very popular to manage hotel collector.
It's broadly deployed.
If you want to have hotel EBPF, profiler.
It's outside of it, and you have no clue on how to install it.
**Donal O'Sullivan** 24:39 Yeah.
I think maybe there might be… yeah, I think I may have heard talk about this before, and there'd be a huge refactor just to try and get that to work in it, and it might not work, is it?
In the hotel.
**Cyrille Le Clerc** 24:54 operator, just manageable by it, but it's packaged as a Docker image, no, as a
Kubernetes deployment… you deploy it as a demand set, no?
**Donal O'Sullivan** 25:03 I'm not sure, yeah, okay.
Potentially, potentially.
**Cyrille Le Clerc** 25:07 So I guess, yeah, it should be deployable by the hotel operator. Which, if it's a demand set, it could work. If it's a sidecar, it would work, would be supported by the hotel operator, whatever you do better. But that's my opinion, it's.
**Donal O'Sullivan** 25:21 Yeah, no, no, that's interesting, yeah,
Yeah, I'm gonna… I'll make a note of that, so I can…
Yeah.
This is all new to me, so I have to consume all this knowledge.
**Cyrille Le Clerc** 25:40 Yep.
**Donal O'Sullivan** 25:41 Alright, cool.
**Cyrille Le Clerc** 25:43 Okay. Yeah, on OPAMP, we cannot…
It would be good to demo OPAMP in the hotel demo.
I don't know how, but that would be nice.
**Donal O'Sullivan** 25:55 Okay, interesting.
**Cyrille Le Clerc** 25:57 The premise that I'm not aware of any open source implementation of a server-side OPAMP.
**Donal O'Sullivan** 26:06 Oh, okay. Yeah.
I… yeah, okay, interesting.
And if there's no open source, then it'd be… it won't be possible, is it?
**Cyrille Le Clerc** 26:18 No.
**Donal O'Sullivan** 26:19 Yeah.
Yeah.
Hmm.
**Cyrille Le Clerc** 26:24 But that would be interesting to have, yeah, to showcase, Opam to people.
**Donal O'Sullivan** 26:29 Yeah.
And… Server size…
You know, server-side.
So we'd have to write our own op-amp server, is it?
**Cyrille Le Clerc** 26:46 yeah, we will, yeah, I think we cannot integrate OpenArmp if I.
**Donal O'Sullivan** 26:52 If.
**Cyrille Le Clerc** 26:53 Jay-Z tweezing the demo.
**Donal O'Sullivan** 26:55 Yeah.
**Cyrille Le Clerc** 26:56 It's nobody who will have that space, or, yeah, it will be complicated to integrate, or whatever.
**Donal O'Sullivan** 27:01 Yeah, yeah, yeah.
Yeah.
Cool, okay, okay. Yeah. Alright, cool. Nice to meet you, sir.
**Cyrille Le Clerc** 27:09 It was a pleasure, nice to be meeting you, and say hello to Alex, if you see him.
**Donal O'Sullivan** 27:15 We'll do. Quicker.
**Cyrille Le Clerc** 27:16 Thank you, bye-bye.
