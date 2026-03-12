SIG: Community Demo App SIG
Date: 2025-11-19
Duration: 39 minutes
Zoom Recording URL: https://zoom.us/rec/share/RQMGZbEba_j6WlIW-DcQbi_jkS4tTYTRrnS8GOakv07BJ9LNmOHvGI849X48sdko.d6KAxhv3m13ytSDw
============================================================

## Zoom Recording Transcript

**Cyrille Le Clerc** 05:04 Hello?
**krish aryan** 05:33 So, my name is Krish, and I'm a newcomer in Open today.
**Cyrille Le Clerc** 05:39 Nice.
**krish aryan** 05:40 So… they… Before this, I was, studying for my, certifications, like, in Kubernetes certifications, so… I became a CubeStrod, and I thought that I should explore more areas of cloud native. So I, like, saw that the second most popular project in CNCF is OpenTelemetry.
So, I started studying about it, and I'm, like, I want to contribute to it, so I am… I am trying to… attend all the, SIG… So that I can find which is, like.
fits best for me, and, contribute. Like, if any Sikh, requires any, like, work, like, if any, Sikh, leader, like, is willing to mentor, I'm willing to learn and contribute.
So, that's it. That's my introduction.
**Cyrille Le Clerc** 06:47 Okay.
So… My name is Siri Leclerc, and I am a product manager at Grafana Labs, and I contribute to the hotel demo. I've been contributing for a bit less than 6 months, I think.
To the hotel demo.
And I try to… yeah.
Oh.
bring a PM point of view, product management point of view on the… The way we work on stuff.
Which may be a bit different from an engineering point of view.
We will see.
Hello, Jonathan. Hello, Pierre.
**Jonathan Munz** 07:31 Hello.
**Pierre Tessier** 07:50 Oh, hello.
**Cyrille Le Clerc** 07:53 Hello.
**Pierre Tessier** 08:02 Okay, Juliana will not be making it.
Remain.
**Cyrille Le Clerc** 08:06 Okay.
You good.
**Pierre Tessier** 08:10 and KubeCon last week.
Yid.
I did, and I enjoyed it.
I was the only one from the demo team there, and none of you were all there.
**Cyrille Le Clerc** 08:20 No, there was not.
**Pierre Tessier** 08:25 Okay, hold on, I am just trying to… What?
Did Google just stew to my calendar?
Okay.
I seen your ongoing PRs, Cyril, by the way. I was looking at the PRs in the hotel demo, or for… in the helm charts this morning, really trying to do some triage.
on, naming things, for what it's worth.
Once those are in, I think we should absolutely have a mode to deploy the collector and daemon set mode for the hotel demo with the right things configured on it.
**Cyrille Le Clerc** 09:28 Would it make sense to you that it would become the default, that demand set would become the default, even?
To be, yeah.
If the presets aren't here.
**Pierre Tessier** 09:39 Yeah, Sid, but let's talk that through a little bit more.
I think if it's a default, I think that's fine, as long as we have a way that's not too hard for a user to say, I really just want a deployment model, because I've already got statement sets. I think sometimes people, when they deploy this, they may be restricted on being able to create daemon sets.
**Cyrille Le Clerc** 10:00 Okay.
**Pierre Tessier** 10:01 That's why I'm trying to get to that, so I want to make it easy for them to bail out of that.
**Cyrille Le Clerc** 10:06 Yep.
If the presets are here, it's, Super.
**Pierre Tessier** 10:11 Yeah, if there's… I think it needs to be an easy way to flip between one or the other.
And we… our configuration also knows how to… evolve around that, or we well document, hey, you need to change these three things, or these… you know what I mean? Like, it's got to be well understood how you go from one mode to the other mode.
Because I think you even have issues with, getting the Postgres and the Redis and the other metrics as well.
Because you don't want each daemon set doing that. You need to use leader election on them.
**Cyrille Le Clerc** 10:42 Yeah, and it's why I proposed to use, hotel collector, receiver creator.
Which can be debated.
And one reason is that it's… I think there are glitches in it.
But, let's wait and see.
**Pierre Tessier** 10:57 Okay. Alright, but you're…
**Cyrille Le Clerc** 10:58 I think we eat ya.
**Pierre Tessier** 11:10 We had a PR that we discussed… so that's, yeah, for… Doing all that, we need to get the other PRs done first for the collector, like you listed right here.
**Cyrille Le Clerc** 11:20 Sorry, which PR?
**Pierre Tessier** 11:23 1941… I don't know what 1918 is.
**Cyrille Le Clerc** 11:28 So what I am doing here is that I am… aligning OpenTeametry Collector and chart on OpenTelemetry CubeSatCampSark.
And I think I got validation from Tyler.
and Moose, that it makes sense to have the same, to have feature parity between them.
**Pierre Tessier** 11:50 Correct.
**Cyrille Le Clerc** 11:54 Without breaking things, of course.
**Pierre Tessier** 12:02 I try to log in the issue for this as well. The K8's Attributes Processor, or preset.
Or, the collector chart, does not follow semantic conventions.
**Cyrille Le Clerc** 12:19 It does not enforce, yeah.
On the hotel.
**Pierre Tessier** 12:21 It does not follow, it actually does not even follow them.
Nodes and labels, and to make matters worse, if you have the same node and label, B.
From, like, a node label with one key, and a pod label with the same key.
They will stomp onto each other.
**Cyrille Le Clerc** 12:41 Whoa.
**Pierre Tessier** 12:42 Non-deterministically, to make it even worse.
Because of the way it's done, there's no name… like, just all node labels, pod labels, node annotations, pod annotations, end up without a prefix. They just, whatever their keys are, that's what ends up going… being pushed into your.
**Cyrille Le Clerc** 13:01 Yeah, I remember.
**Pierre Tessier** 13:02 attribute space, but they should be prefixed with khs.no.annotation, khs.no.label, case.pod, like, so on and so forth.
I thought I created an issue for this, and I'm not able to find it now, which makes me a little sad.
**Cyrille Le Clerc** 13:19 Do we use this capability in the hotel demo today?
**Pierre Tessier** 13:22 We do.
**Cyrille Le Clerc** 13:25 They have labels.
**Pierre Tessier** 13:26 I don't think we have labels, but if somebody else has labels on there.
**Cyrille Le Clerc** 13:29 Nodes, for example.
**Pierre Tessier** 13:31 They just show up as… Not good things.
Yeah, I don't… Okay. It's not the demo specifically, but as we expand upon this, and as we think about being more Kubernetes native, we should make sure that the whole stack is Kubernetes proper.
**Cyrille Le Clerc** 13:59 Yep.
And so, yeah, what we say is we want to… you and me, we say we want to add this, infra-monitoring capability.
We want to add it.
As the demand said, but we also want to support the deployment mode.
Correct.
**Pierre Tessier** 14:17 Yes, we have to support the deployment mode.
**Cyrille Le Clerc** 14:21 We won't.
**Pierre Tessier** 14:22 Where… where… for what it's worth, that means we won't be collecting Kubernetes… we won't be collecting qubit metrics in that case.
**Cyrille Le Clerc** 14:31 And maybe…
**Pierre Tessier** 14:32 for the demo It's a way… maybe it's an easy way we configure in the demo where we say, you know, in the Helm chart, collect Kubernetes infra enabled yes or no. And if it's enabled, we go in name and set mode with all these settings, and if it's not enabled, then we go in deployment mode without them.
**Cyrille Le Clerc** 14:50 Let's… yeah, maybe, maybe like, some… For me, it's… you can collect maybe… yeah, maybe I was assuming that kubeletStat, you can collect them, centrally.
**Pierre Tessier** 15:05 No.
**Cyrille Le Clerc** 15:05 I'm wrong.
**Pierre Tessier** 15:06 No, you have to… you have to be in a Damon set to get them, yeah.
**Cyrille Le Clerc** 15:08 Okay.
on pod logs, and I think it's very important to show people how to collect pod logs.
I would love to.
And…
**Pierre Tessier** 15:16 Yeah, I…
**Cyrille Le Clerc** 15:18 We need to…
**Pierre Tessier** 15:22 coming from other vendors who have Kubernetes agents to collect Metrics, traces, and logs.
I'm disappointed in the OpenTelemetry's Podlog collection, or lack of pod log native collection receiver.
I will call that out right now. There's no way to target a pod when you want to collect logs in Kubernetes.
**Cyrille Le Clerc** 15:44 On here, I like the.
**Pierre Tessier** 15:46 It's a way to target nations.
**Cyrille Le Clerc** 15:46 Receiver creator, the receiver creator.
**Pierre Tessier** 15:49 You could target a namespace, but you can't target a pod. And every other… Agent out there allows you to target pods.
**Cyrille Le Clerc** 15:59 Yeah.
**Pierre Tessier** 16:00 Most specifically, they allow you to target pods based on selector labels, which is a Kubernetes native thing. Now, I don't want to debate this here, I've had this conversation with Tyler as well.
on… on the collector side, and I said, I'm very disappointed we don't do that yet, because it is… it is a mechanism, like, just saying, get all logs and namespace is… it's… it really feels like a… you know, get everything and then filter it out later, excuse, instead of just get what I need, right? It feels like, like, I don't care about compute, go waste it.
**Cyrille Le Clerc** 16:37 Yeah. Only if we… we can… I see the hotel demo as a great candidate to be the test compatibility key to help these teams implement the future.
**Pierre Tessier** 16:47 I understand. Yeah.
**Cyrille Le Clerc** 16:49 Or is it, outside of our goal?
**Pierre Tessier** 16:52 No, no, it's absolutely a great… that's what I think we should be doing. We should be going back to the SDKs and the agents and the collector SIGs and saying, hey, we said this is going to work, we had set this out as a mission, but reality is, this is what we're experiencing.
Absolutely, we should be able to provide that feedback back to the individual SIGs as the one. In fact, all morning, I've been spent all morning on trying to stabilize Prometheus over the long term in our demo.
And one of the reasons why I believe it continues to be unstable is that the metric exemplars coming from the Go SDK are out of order.
on metrics.
**Cyrille Le Clerc** 17:34 I believe there's a bug in the.
**Pierre Tessier** 17:35 Go SDK. I believe there's a bug in a Go SDK that only really manifests itself when we export to Prometheus.
**Cyrille Le Clerc** 17:43 bucket.
Yeah, and we see, exemplars out-of-order messages in the.
**Pierre Tessier** 17:48 Yes. Err on ingesting out-of-order exemplars.
There's 2 sets of them.
One of them does not… if you turn on detail logging, you catch a second set. The second set comes from the collector itself.
The collector self-metrics.
**Cyrille Le Clerc** 18:03 They're able to add the metrics, but something like the exemplars are airing out, but the error gets swallowed and does not make it to standard logging.
**Pierre Tessier** 18:12 The feature flag service As a slightly different error, but again, related to exemplars.
That also uses the Go SDK to emit metrics.
And I've been able to track down… I could turn on… if I downgrade the feature flag service to before they added metrics at the Go SEK, it works.
So I could… and when you turn on detail logging, you see which errors they are. So I gotta write this up a little bit more, but there's definitely a bug somewhere in the Go SDK.
Or, in the way that we are… doing something with metric exemplars somewhere in a pipeline with the collector, when we're omitting the use of Prometheus. It could be a bug in Prometheus, I don't know, but there's a bug somewhere.
I've also added a few more settings to Prometheus to significantly reduce its memory footprint.
A while ago, when we moved from ES3, we went to native.
OTLP protocol into Prometheus. We removed the scrape, because before we were scraping from Prometheus. Well, I guess, inadvertently, we allowed the default Prometheus scrape config to be deployed, and the default Prometheus scrape config for Kubernetes is quite extensive. And Prometheus is trying to do a lot of scrapes, and just… they didn't exist.
So I removed all the scraped configs. I've been able to significantly reduce Prometus' footprint as well.
My hope here is I get this thing to run stable for at least 2 days without crashing.
but yeah.
We have some stability things to get this hotel demo to run for more than a few hours.
That we need to probably address.
I've got several memory updates I'm going to make, just to increase memory. For example, accounting service needs to go to 160 megs, payment to 140, Grafana sidecars to $120, and Grafana Core to $175.
And we're gonna properly use collector self-telemetry as well.
remove Prometheus scrape configs.
So, I'll be sending off a series of PRs here with all this kind of tied into there.
really all focused on stability for the demo inside of Kubernetes, with the intent here of cutting a release very, very soon. I know we wanted to get the SDKs all in HTTP, But, let's just kind of release before that happens.
We have the LLM now working nicely, and I'd like to get that LLM out there for the world.
**Cyrille Le Clerc** 20:36 Okay.
So… collector self-telemetry for your information. We… related to this, we have identified the that the… in Grafana, in the Grafana of the hotel demo, the OpenTeametry Collector dashboard, has glitches, so I'm working on it.
**Pierre Tessier** 20:57 The glitch I found is just the base rate.
**Cyrille Le Clerc** 21:01 I think I had some no data issues as well.
**Pierre Tessier** 21:04 Yeah, you just removed the base rate.
Oh, maybe when I fixed on myself, telemetry, I fixed it, and it just works for me right now, locally. I could show you what I have working, and you could tell me what.
**Cyrille Le Clerc** 21:15 Yep.
**Pierre Tessier** 21:16 you have not noticed working, but I have, I've noticed some things as well.
with this?
So this is it running. I restarted a few things recently here.
But when I change this mid-step to 30 seconds, I get charts.
**Cyrille Le Clerc** 21:31 Oh, nice.
**Pierre Tessier** 21:33 Anything below 30 seconds does not work. You have to change this.
or change this and not be 15 minutes, change it to be 2 hours, for example. Hold on, I got cameras in my way. Or 3 hours, and then you can change this back to auto, and it'll work.
**Cyrille Le Clerc** 21:49 Okay, that's good to know. Yeah.
**Pierre Tessier** 21:52 That's… that's what I was experiencing. Everything is now flowing. Oh, not this down here, I'm not sure what that is.
And I probably should have checked all these other things as well. Oh, boy.
Okay, I'm mistaken. A lot of things were working.
**Cyrille Le Clerc** 22:08 No, I think it's doing too much.
Now it's… we should really focus just on the hotel collector telemetry, like, what is the health check of inbound.
I thought this dashboard is a community.
**Pierre Tessier** 22:22 community-developed… I thought this dashboard was a community developed dashboard that we just copy in.
**Cyrille Le Clerc** 22:27 Yeah, and I think it deserves to be, so my mental model is to have an aggregated view.
Like, the view of the inbound saying… with the error rate, on the rate, aggregated on all inbounds.
Same on outbound.
on a view from the processor, like, I am… dropping, losing data in processor, but very aggregated. Onus, if you scroll down on the dashboard, the second layer, where we would have details.
Per receiver, on per processor, on per exporter.
to zoom out to start with, and then zoom in. But I, yeah, it will take me a few…
**Pierre Tessier** 23:08 If we need to redo this, we should redo it at the community level, and then… we'll just take in that version. I'm not even sure where the community dashboard is ultimately stored, but I believe it's somewhere.
**Cyrille Le Clerc** 23:18 Yeah, exactly.
**Pierre Tessier** 23:19 like, some Grafana.
community placed, I think?
**Cyrille Le Clerc** 23:22 Yeah, yeah, it's a community.
**Pierre Tessier** 23:27 But yeah, that would be my intent, is to make sure that we stay in sync with that. And if we want to say, hey, we're doing the demo, and we're noticing, you know, really putting the collector through its paces.
This is a more, you know, effective way of having to, you know.
I just don't want us to have our own version, and then the community has its own version.
**Cyrille Le Clerc** 23:45 Yeah, yeah, yeah, you're right. Totally.
On the… I know the… the author of this, Of this community via dashboard, he's in France, and I know him, so I will iterate with him.
**Pierre Tessier** 23:58 Perfect. And if there's a way to set this so the default is not 15 minutes, but 3 hours.
That'd be fantastic.
**Cyrille Le Clerc** 24:04 Oh yeah, that's okay.
**Pierre Tessier** 24:05 as well.
**Cyrille Le Clerc** 24:06 I don't think it works at, like, 30 minutes, or 15 minutes, or any of these don't work. Yeah, it does.
**Pierre Tessier** 24:13 I can show you that I have the collector now configured, To really be doing… Here, I will show you.
These are the logs from the collector, you can tell I've been testing this, but I really got it, so it is very much… trying to use the default settings here, so I just have self-telemetry going back into itself.
Okay, I know this is against a lot of the things you do.
**Cyrille Le Clerc** 24:39 But…
**Pierre Tessier** 24:41 the demo. So it goes right back into itself.
And that's it. There's no other weird configuration, and to configure for this, I used our defaults Right here.
It's how I configured for it.
**Cyrille Le Clerc** 24:59 Yep.
**Pierre Tessier** 25:00 Okay? And I would like this to be part of our chart. I know this is subject to change, that's okay, we can follow it. We lock versions, so we'll be okay.
But I'm trying to, like, and I also removed… we used to have self-telemetry down here, so it's find a pipeline, wherever it is. I removed that self-telemetry. I'm only using it from the preset now.
**Cyrille Le Clerc** 25:21 Yeah, that's great. And I was wondering, on the cell telemetry, Usually, metamonitoring, we recommend to use an external monitoring system. You don't monitor yourself. It will go bad one day.
**Pierre Tessier** 25:35 so let's put comments in there and say, we don't recommend you ever do this, we're doing this because it's a demo, and we need to send it somewhere.
Okay, I completely agree with you.
**Cyrille Le Clerc** 25:47 I was thinking it may be…
**Pierre Tessier** 25:48 collectors, for honeycomb that we use for our own production uses, they do…
**Cyrille Le Clerc** 25:54 Hmph.
**Pierre Tessier** 25:55 Collector's self-commerce Center.
**Cyrille Le Clerc** 25:57 collector. They always send to the upstream one, and then the upstream one itself sends directly to Honeycomb.
**Pierre Tessier** 26:02 But not through itself.
**Cyrille Le Clerc** 26:04 Only here, what I was thinking we could do, is to have the meta-monitoring, so self-telemetry, sending directly to Prometus or TLP endpoint.
**Pierre Tessier** 26:15 We could.
**Cyrille Le Clerc** 26:17 Or maybe asking Prometheus to scrape. Export… expose… OpenTeametry Collector, self-Telemetry using the Prometus Exporter.
with a web page, but we are the only export. Like, this is really simple to configure, right?
**Pierre Tessier** 26:36 And we could just comment our way there, instead of trying to create a… I… I'm trying to get Prometheus not to scrape.
It consumes a lot of memory to do that, apparently.
So, anyhow. Perfect.
I'm going to be submitting a series of PRs later on this afternoon. I have blocks on my calendar to work on this.
So I will be submitting a series of PRs later on this afternoon on both the OTEL demo core site for Docker Compose to give a little bit more memory to these components, as well as on the Helm chart.
I think we're ready to merge and cut a release for all of this. On the demo itself and on the Helm chart, we're in a good state for them. I'd like to get moving forward on cutting a release, so we can have a release out perhaps even by this weekend. If not early next week, we can have a release cut.
I would bump the major on the demo side for the release, as we did add an LLM component.
I think we still have known to do work to do. We want to get all COM to be protobuf, HTTP protobuf, instead of JRPC.
for the OTLP export protocols, or the telemetry export, I should say.
Also, I want to move Postgres to a more shared database. Right now, we embed an SQL inside the image, we should be mounting it.
It should be a method that's config map in Kubernetes, and a volume in Docker.
**Cyrille Le Clerc** 27:58 Regarding, was great.
Can I share with you something?
**Pierre Tessier** 28:06 Yes, please.
**Cyrille Le Clerc** 28:08 I guess your seeds… in your Tracer's view.
**Pierre Tessier** 28:14 Today.
**Cyrille Le Clerc** 28:16 the database name is called Hotel U, or Hotel.
Oh, my God, yeah. On a turbo. Until I pushed the PR, to rename from Hotel to ShopDB.
**Pierre Tessier** 28:28 Can you call it astronomy, DB?
**Cyrille Le Clerc** 28:30 Sorry? I'm sorry.
**Pierre Tessier** 28:32 AstronomyDB, because it's the astronomy shop.
**Cyrille Le Clerc** 28:35 Oh yeah, our Astronomy DB.
**Pierre Tessier** 28:37 Yeah, like, I get what you're saying, but we need another… shop is too generic.
**Cyrille Le Clerc** 28:42 Yeah, so you say it's not a ShopDB?
**Pierre Tessier** 28:49 Instead, Astronomy TV.
you've got a weird thing going on with your A there, but I know what you're trying to do.
**Cyrille Le Clerc** 28:58 Yeah.
**Pierre Tessier** 28:59 -Oh. You had the, the, the AXA, Exxon Gadav, is what you're using.
**Cyrille Le Clerc** 29:03 Yes, I am French.
**Pierre Tessier** 29:06 It's all good.
**Cyrille Le Clerc** 29:09 Okay.
And for me, there is another thing also that I want to fix, and I think it's important.
we should not demo with people using the root Postgres user to connect with the hotel collector.
**Pierre Tessier** 29:25 No, they should be using a user that we've created.
**Cyrille Le Clerc** 29:28 And so what I proposed, in this PR that, got, so I evolved the init.sql script.
I created ShopDB that we will rename, as you said, that's great.
on… I created… A user, a monitoring user.
That is exactly using the, postgroup…
**Pierre Tessier** 29:52 So we could use that for the… Yeah, yeah, I understand what you mean.
**Cyrille Le Clerc** 29:57 Because there is this, this role called monitoring user.
Baked in out of the box in, I think it's monitor, but there is a privilege out of the box in PostgreSQL, and I think we should use it.
**Pierre Tessier** 30:15 Okay, I'm confused. We don't specify anywhere the name of the database is OTEL.
**Cyrille Le Clerc** 30:19 We do it in the ENV.
And we do it in…
**Pierre Tessier** 30:30 Oh.
Where is it inside the NetSQL?
I say create user, but not create DB.
**Cyrille Le Clerc** 30:39 It's because it's in the Docker image itself.
It's very… it took me quite some time to… Get heat.
Environment.
**Pierre Tessier** 30:56 post-grade DB here.
**Cyrille Le Clerc** 30:59 So, here you pass PostgreDB to the Docker image. By default, Postgre… DB is mapped to Postgres as a… built-in database.
But with a Docker image, you can change this, but I think it's not meant to be changed by your business-oriented instance, it's when you want to obfuscate stuff.
So this is a trick we do with the END, which is… it took me…
**Pierre Tessier** 31:28 A lot of time.
**Cyrille Le Clerc** 31:29 To understand.
**Pierre Tessier** 31:29 Okay, to unwind all that and figure it out. Fair.
**Cyrille Le Clerc** 31:33 Okay, okay. I take it for a DBA.
Yeah, ideally, like, as long as we have one database.
**Pierre Tessier** 31:42 With a separate schema for each service.
So, accounting will have its own schema.
And I think we have that already in there, and then, reviews will have its own schema.
And… Is it.
**Cyrille Le Clerc** 31:56 our database in Postgres, I thought it was called…
**Pierre Tessier** 31:59 There's schemas in Postgres.
The database is the thing that spins up.
and then you create schemas in Postgres for each…
**Cyrille Le Clerc** 32:08 Okay. Service.
**Pierre Tessier** 32:10 That's at least what it looks like. That's what I'm staring at right now in… Maine.
That was a couple weeks ago when we added the LLM stuff.
created a new schema. This was also… this is where it was split up. We now have two schemas inside of Postgres, one for accounting, one for reviews, product reviews.
And I'm starting to look at this, and I'm starting to wonder, like, I don't think you have… Those changes in here, do you?
**Cyrille Le Clerc** 32:40 Nope.
I did this some time ago, and it got closed, because this is a 3-week sold door.
**Pierre Tessier** 32:49 Okay, things have changed.
I don't know if the database… the database might still be called OTEL, though.
We have a schema, we have a schema called accounting, we have another schema called reviews, or product reviews, I should say.
And then, eventually, I want to bring the product database in here, and we're going to create another schema called product.
And instead of using a JSON file, we'll just have products go to this. And my real dream here is we're gonna get all this in its SQL file will be mounted.
like a config map. So a user can create their own config map with their own products, their own product reviews, all their own stuff.
And then just deploy the demo, and just say, use my config map instead of, you know, don't create the config map for me, use mine.
**Cyrille Le Clerc** 33:36 That'll be good.
**Pierre Tessier** 33:37 it as the init, and then Docker will… and then Postgres will do its things. I'm not sure how MySQL does this, but I believe MySQL has a very similar initialization capability as Postgres here.
**Cyrille Le Clerc** 33:48 I am not clear on the difference between the role of init.sql as a file on the config map, because I… okay, yeah.
**Pierre Tessier** 33:57 I have a file called, in Postgres. If you have a file called… Docker-entrypoint dash init dash db.d Everything inside that folder, gets… run if there's no database that already exists on initial startup of the container. The first time the container starts up, if it doesn't have a database, it'll go ahead and run all those scripts. MySQL has a similar capability. I think the mount path is a little different.
We only have one file that we put in there, it's called initSQL. The idea, though, is you use, like, Linux naming, like, 00- and 10-, and then you can have a bunch of different things in there.
I don't think we need to do that. We could have a single file. If we want to split it up, it's fine, I don't care.
I really don't care how we do that, as long as we mount it, is all I care about.
Oh, no.
**Cyrille Le Clerc** 34:45 That's music.
**Pierre Tessier** 34:46 I want to mount it at runtime, not a… Docker creation time. And ultimately, we wouldn't be able to stop using our own Postgres image. We'd be able to move to the Postgres official image if we did this as well.
Yeah. So MySQL has similar capabilities. We'd have to do the same thing there. I think we talked about doing this for MongoDB as well, which would really change some of the dynamics of how all this works.
But one thing… one step at a time, so… .
**Cyrille Le Clerc** 35:14 on… yeah, to come back, so now I see the changes that happen after I submitted my PR. I think that this user hotel you.
Zaddy's, deserve to be replaced by either, astronomy, or accounting user, blah blah user, or monitoring user.
**Pierre Tessier** 35:38 Okay. Let's make that a separate PR, because this is all internal to the platform. We need to make sure that the services have the right username and password as well, passed into them on their connect strings, but that's all environment variables. That's some PR.
**Cyrille Le Clerc** 35:52 Yeah, but does it make sense for you that, the monitoring user that will be used by hotel collector, PostgreSQL receiver.
It's a very specific.
**Pierre Tessier** 36:03 Yes, there should be a specific…
**Cyrille Le Clerc** 36:05 monitoring role.
**Pierre Tessier** 36:08 And a separate user, because that's… that would be the best practices that the post… I would hope the Postgres receiver tells you to create a user as well, with those capabilities and those permissions. Let's follow this… let's follow those steps.
**Cyrille Le Clerc** 36:18 Perfect. And for what it's worth, test out the receivers, read me.
**Pierre Tessier** 36:23 And if it doesn't work, we can go back to them and say, hey, your instructions were wrong.
**Cyrille Le Clerc** 36:29 Okay, yeah.
**Pierre Tessier** 36:30 Do you think you do that PR this week? Do you think you'd do that this week?
**Cyrille Le Clerc** 36:34 Oh, no.
**Pierre Tessier** 36:34 Did you get that done? No? I have, some other crazy PRs to do.
Okay, fair enough. I'm gonna get us to a release today.
We're at time. Chris, you've been quiet.
**Cyrille Le Clerc** 36:46 Yep.
**krish aryan** 36:47 Actually, I'm new to OpenTelemetry, and I… I'm just exploring all the six to see which one can I contribute in. I know the basics of Kubernetes, and That's it. I'm, like… I just want to contribute, like, I'm new here.
**Pierre Tessier** 37:08 You know, I know it's not a… The funnest contribution, but… We could always use more documentation.
**krish aryan** 37:16 Yeah, okay.
**Pierre Tessier** 37:16 For what we do.
more instructions on how to run the demo properly, and what the various different attributes, and capabilities are that we're exposing. Like, we're talking about adding Postgres monitoring here. I doubt it is documented at all anywhere on the OpenTelemetrees Docs site, or the community site.
So if you're looking for something, like, I want to get into it, I want to get started, I feel like some of the easiest and greatest ways to start contributing to OpenTelemetry is helping us write docs. It's an area that we lack significantly within the community today.
**krish aryan** 37:51 Okay.
**Pierre Tessier** 37:53 Yeah, for sure.
**krish aryan** 37:54 It's okay.
**Pierre Tessier** 37:55 Run the demo, be frustrated by running it, and then document how you got around your frustrations.
**krish aryan** 38:02 And I see the, like, some resources in the OpenTelemetry demo, application sake meeting notes, like, at the repository design documentation, application requirement. Is there anything else, that you would like to mention for me, to get, like, to study it, and, like, that will be helpful for me to understand these things, because many of the things, like, that you mentioned in the meeting, like, it just went over.
in my head. So, so… I was just wondering if, If I don't understand it, how can I just, like, contribute? Like, even in the docs, I need to understand this stuff, right?
**Pierre Tessier** 38:41 Yeah, we definitely are talking about some advanced topics, sometimes here in OpenTelemetry. I, I, you know, docs OpenTelemetry.io.
It's definitely a great resource for that. And we also document the entire demo there as well.
So, and some of the concepts, I think the more difficult concepts we were talking about were around gRPC and HTTP and collector configurations.
That's because myself and Cindy, we've been doing this for a long time, we were rarely entrenched into them, so maybe we're talking a little bit of lingo that we should maybe avoid and be a little bit more, new person friendly with, if you understand what I mean. I do have to run, I'm so sorry. I'm 3 minutes late for my next meeting, but I, you know, if you're looking for somewhere to get started, docs, docs, docs, either our SIG, the demo SIG, or the Community I.O. SIG itself, which is where the doc site is held.
**krish aryan** 39:34 Thank you, Ken. Awesome, thank you. Bye-bye.
**Pierre Tessier** 39:36 Yep.
