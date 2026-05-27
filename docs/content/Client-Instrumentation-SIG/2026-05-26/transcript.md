SIG: Client Instrumentation SIG
Date: 2026-05-26
Duration: 32 minutes
============================================================

## Zoom Recording Transcript

**João Oliveira** 01:45 That sounds so sh… crazy.
**Santosh** 01:49 Lowe.
We generally have more folks in this meeting, at least the ones I have joined.
**João Oliveira** 02:06 Yeah… Let's see if anyone else joins.
**Santosh** 02:19 Are you, family with the metrics, conversation we have been having with, Let's say, Martin, Jason, and Henson.
**João Oliveira** 02:30 Yes, I've… I have been following that conversation. I've actually been, meaning to, maybe ask around a bit in the… in the… in the Slack, because I… I… Well, I do understand the overall problem, Hey, Martin.
But it… it's a bit unclear to me, and I don't want to clutter this meeting, we can talk about it in Slack or something. For me, it's still a bit unclear.
What exactly in practical terms it means for… for us to, support or not support find-side metrics? Is it through… providing or not providing a fully-fledged API? Is… is… is it like a footnote saying you should not be sending client-side metrics.
or not, or you should. That's… it's… it's just unclear to me at this point what it means Okay.
**Santosh** 03:29 Yeah, I can give a brief, you know, overview of, like, background on this topic, and, you know, that'll help us, you know, get into the core of the discussion. But before that, do you work on the browser side or the mobile side?
**João Oliveira** 03:44 Actually on the backend side. I work more in the ingestion side, so I'm not… no expert on either. I know a little bit.
**Santosh** 03:54 And what, what is your interest, in the client, Client sick.
Would you work on the ingest of the client telemetry?
**João Oliveira** 04:04 Yes, I work on the ingestion of Datadog's RUM product.
**Santosh** 04:11 I see. Okay. Okay, so the background is this, right? I think, so far.
most of the instrumentations, originally, you know, they only emitted spans. And at some point, we said, hey, you know, because this is… the spans and traces were the only… relevant signal, you know, that was supported in OpenTelemetry. There was no concept of events, top-level events. And… and then… the effort was put in to introduce events as a, you know, a top-level concept. It existed only within spans, and then, when that was approved.
The new instrumentations, you know, the team built that… Started emitting, events.
And now we have, instrumentations that emit spans only for network requests, but for everything else, it's, it emits, events. And, And every once in a while, a discussion comes about metrics, and the… Guidance, or at least the standing from many of us, has been that metrics is a server-side concern.
you know, because… you know, every client represents only one user, and by emitting metrics, you know, I had a bunch of concerns, but I changed my mind later. I think the concerns were mostly around, hey, you know, adding metric support means… Adding, you know, more, heavier, client-side code, client-side agent, I think it is prohibitive for the browser, you know, typically.
You know, every signal comes with its own exporter, it comes with its own, you know, connection.
And, you know, it again is an overhead.
**João Oliveira** 06:08 The cardinality concerns of…
**Santosh** 06:10 And more importantly.
**João Oliveira** 06:10 Yeah.
**Santosh** 06:12 Right?
**João Oliveira** 06:12 That, that I can, I can totally understand, yeah.
**Santosh** 06:15 Correct, correct. Now, the cardinality concern so, the… When the backend applications generate metrics, they… There is a guidance there, too, that, you know, people should avoid inserting attributes or labels that have high cardinality values.
**João Oliveira** 06:38 Yes.
**Santosh** 06:38 But in the client side, if all the resource attributes end up being Metric attributes by default, you know, it invariably creates high cardinality.
And if we send these metrics directly to metrics.
Pipelines that most people, most vendors have.
you know, you need to be careful, right? You need to be explicitly dropping those cardinality, attributes. Performing aggregation.
And therefore, our guidance was that, hey, you know.
Let's stick to ingesting events and spans, and we anyway create metrics, we anyway have functionality to convert Events, or aggregate events and spans into metrics.
And, you know, let's just stick with that.
But what really, you know, made me turn around and go back to supporting metrics on the client side, you know, advocating for it now, is, I think, the ease of use, right? I think in backend code, you know, you being a back-end engineer anyway, you see that people, you know, very freely You know, create custom metrics to measure, you know, various things.
And then put them… visualize them in the dashboards. That… Level of ease doesn't exist for the client engineers today.
Right? If, let's say, I want to measure how many people are clicking this button, you know, I can't just, you know, say, create a new counter, and then increment a counter every time the button is clicked. It's just two lines, right? You know, you define a counter and then do an increment.
you have to define an event, so the API ergonomics are very different.
So, I felt that If we introduce the client-side engineers to the same level of ease that the Metrics API brings in.
That'll be, you know, super nice.
Whereas behind the scenes, you know, we will work on addressing the challenges. We will work on how that metrics are shipped, those metrics are shipped, how those metrics are shipped into a different pipeline that has Support for dropping the high cardinality, You know, attributes.
So those back-end plumbing is what I think we will need to work out.
But the API interface, it'll be nice to keep it super simple, you know, that Metrics API supports today.
**João Oliveira** 09:24 Let me… let me see if I understand correctly. So, because… you know, ultimately, I guess, you know, any customer can take the metrics API, And have your, your own browser application, like, just, send metrics, but it's all very, you know, very, let's call it manual, very, cumbersome. So… Does this mean… Because I see two interpretations here. One is, we are going to take Some of the signals that exist.
And model them as metrics, rather than, logs and spends.
**Santosh** 10:10 Let me ask…
**João Oliveira** 10:11 Is it…
**Santosh** 10:11 clarify that part, right? I think I am not suggesting that we change any of the instrumentations that are already built today.
to Emmet Metrics. In my mind, the metrics is… Purely for custom use cases. Custom… metrics that people want to introduce, because if you see in the backend code too, right, people use metrics for all custom metrics.
Most… I mean, of course, there are, standard, instrumentations that meet standard metrics too, but the convenience is more for the developers You know… Inserting custom metrics code.
I want to measure.
**João Oliveira** 10:55 So, in fact.
**Santosh** 10:56 You know, there is a level of ease there.
**João Oliveira** 10:59 So, ultimately, when it comes to semantics, this doesn't really change anything. What we're discussing is that the reference implementations of the SDKs that Opal Telemetry provides Have a platform in place and systems in place for you to very easily create your custom metrics and ship them, and also some systems to address the issues, like we discussed, like, you know, the cardinality issues, the… you know, all of the other things that, that might show up. So it's not, it's not really a, a semantic thing, it's more like creating the space For, customers to, to… or users to ship their, their… their metrics, without having to, you know, jump the amount of hoops that they might have to otherwise.
**Santosh** 11:55 Correct, correct. I think we, we all…
**João Oliveira** 11:57 Thank you, that's quite more clear to me.
**Santosh** 12:00 Yeah, yeah. Today, if I look around the documentation of, you know, various vendors, you know, most have, their, you know, their own APIs to emit metrics.
You know, measure something and limit metrics, but, you know.
unifying the API, you know, using OpenTelemetry API would… would be one step forward, where Any… Custom instrumentations customers do.
you know, will not have to change when they switch vendors. I think that is basically bringing in additional power to the customers.
You know, through open telemetry.
**João Oliveira** 12:42 And so what… and I'm sorry, please stop me at any time if I'm asking too many questions. And Martin, do you want to say something before I…
**Martin Kuba** 12:51 Yeah, I… I just wanted to, like.
ask Santosh, like, it sounds like you've done the research to… to see, like, if… Vendors, like, different vendors, different libraries.
for web do provide APIs for For capturing metrics.
**Santosh** 13:08 They are very vague, though. Like, for example, like, for example, at Splunk, right? At Splunk… the documentation says to emit metrics, to build custom metrics, you have to emit custom events first. And then, you know, there is a mechanism to, you know.
**Martin Kuba** 13:31 Okay.
**Santosh** 13:31 Visualize those events in the form of metrics.
**Martin Kuba** 13:35 Yeah, so I can… I can say, like, from… from Grafana's side, like, we don't have that. And, like, we… we… like, but we provide, like, in the backend, we provide, like, clear language that can generate aggregate logs, right?
**Santosh** 13:48 It's the same thing. So, like.
**Martin Kuba** 13:49 It just depends, it depends what the vendor does in the backend, also.
**Santosh** 13:52 Right, of course.
**João Oliveira** 13:54 That's what we do, too. So, basically, it's what we call the run-to-metrics pipeline, which you can create queries, and it's not… you're not navigating the events like they're metrics, we're actually, like, generating metrics as the events are… are ingested.
Then basically, you know, all of the cardinality issues and that sort of thing, we handle it ourselves in the… in the… in the server side.
Again, nothing would stop a customer from, you know, instrumenting their app with the metrics API and sending those metrics.
It's just that, you know, they end up in the metrics product as a metric like any other, and they're not, they don't have any sort of attachment to the RUM product.
which I guess, you know, then ultimately each… Vendor would handle these metrics, either as any other metrics, or eventually as, you know, client instrumentation-specific.
Things.
But… Muslim.
**Martin Kuba** 15:08 I think, you know…
**João Oliveira** 15:09 Yeah, go ahead.
**Martin Kuba** 15:09 Sorry.
**João Oliveira** 15:10 I'm just… I'm curious to what, turned you around, Santosh, in opinion. Was it the case, from what you're explaining.
My understanding is that this is bound to happen, and so we might as well… .
**Santosh** 15:26 No, not exactly.
**João Oliveira** 15:27 Have it our way.
Our way, or provide a proper way to do it.
**Santosh** 15:32 So let me share my screen quickly, oh, I… Share through Zoom.
Okay, do you see my screen?
**João Oliveira** 15:45 Yes.
**Santosh** 15:46 Okay. The front-end user metric.
Alright, give me a second.
Yeah, so if you see, you know, this code, there are, there are only two parts here. You know, you… you… let's say… I want to view how many times somebody, you know, viewed a particular product page, right? So I create a counter for it.
Right, and then the record product page view. And, you know, so I just say, you know, take this counter, and then just say add. And then I put the product ID as an attribute. So it basically simplifies the, you know, API ergonomics, you know, what the, developer intends to see is, hey, he wants to plot, you know, a chart with You know, showing how many people clicked on this product page, or, you know, how many people placed the order, and then he would see that graph is later on.
Whereas, if we were to add an event.
you know, it is an extra cognitive effort for the, you know, developer that, hey, what I'm adding is I'm recording an event.
And, you know.
And then somebody's going to convert that into a metric, and then how that event converts to a metric, there is a lot of semantics that I have to rely on somebody else. I'm not responsible for, you know, converting that event to metric. It's somebody else, you know, doing that, and therefore.
There is… there's extra effort through the process.
**João Oliveira** 17:45 I miss him.
**Martin Kuba** 17:46 So I think on… on… like, on one hand, like, we have this, this API is, like, the one concern, and on the other side, the other concern is if we decide, how do we ship it to the backend, right? If you don't ship it as a metric, if you don't actually aggregate in the client, and we ship it as an event.
Then, would we need some kind of convention to, like, say, this event actually represents a measurement?
That you need to… that the backend needs to aggregate.
**Santosh** 18:20 Right. I think, so that is, that is where I think we need to do some, some survey. So, generally.
generally, we don't deal with, in the open telemetry, we don't deal so much with the backend, right? I think… In fact, the Metrics API already exists in the OpenTelemetry demo, when I, tried to you know, do this prototype. The packages that I needed to use, you know, are already there. And the packages did seem to be very, you know, thin anyway, so… the API, the SDK metrics, and the exporter. The API we already include. Maybe, you know, through tree shaking, the metrics-related APIs, you know, get removed, but But, you know, the APIs is one, Martin. The second is the SDK metric. In the SDK metrics, I was, you know, looking what exactly is the functionality. It only has, like, a periodic exporter. Every… A few seconds, or whatever interval you configure, you know, it, you know, pushes the current snapshot of the metrics into the exporter.
And then the exporter is the one that actually sends it out, so the HTTP exporter. There are no other processors or samplers, like we have for spans in the, in the… as part of the SDK.
So it's, it's relatively, you know, simpler. Now, whether… whether we want to convert them into events, something that I am considering for our internal purposes, for our pipeline. That's something… It depends, right? I think it depends on… in an individual vendors, you know, situation. You know, it's possible that your metrics pipeline might be able to support functionality to, let's say, you know, take Prometheus, right? I could be wrong, but, it's possible to… Defined rules to, to collapse let's say, you know, certain dimensions. So, maybe there are ways to, you know, address the concern that we have to reduce the cardinality. So it really depends on how seriously, you know, we in the OpenTelemetry community needs to solve, you know, this problem.
But if we need to, then, yeah, we could certainly come up with conventions.
To, to convert, you know, metrics to events.
**Martin Kuba** 20:55 Yeah.
Yeah, from semantic conventions, I mean, perspective, like, so, like, it's like a signal to the back end, like, if you're going to like, if every vendor's doing something different behind the scenes, then, like, what's the point? Like… Like, we, you know, like, we can't… we can't just have an API that sends events anyway, right? So… Because that doesn't… doesn't really solve the problem. So you're gonna have to have some kind of convention that tells, like, that, like, all the vendors or the backend's gonna… unify on, I guess.
**Santosh** 21:31 Yeah, yeah.
**Martin Kuba** 21:39 I've kind of, like… I've kind of… resolved, like, from the browser SDK perspective, like, I… I feel like we have bigger issues to solve first, but I want to just… I want to just document this so that people know, like, what our… what our stance.
**Santosh** 21:57 I think there is no serious action items here. You know, I just want to… you know, pull back, you know, the issue I created earlier, where I originally… Had an issue Asking for guidance to… guidance in the, in the, you know, somewhere in either in the spec report, semantic conventions report, even in the documentation, a guidance against using, you know, metrics API. But now that I… I've changed my mind, you know, I'm thinking of, you know, closing that issue.
And especially, you know, if you guys… Also see some value with the Matrix API.
Hansen was also opposing it, right? So he seems to be okay with it, too, using the API.
We need to work out the export.
Topic, so we could continue working on that.
**Martin Kuba** 22:52 Yeah, I feel like I… I think that… I don't know about Hansen, but I think Jason has changed his mind, like you.
**Santosh** 22:59 Yeah, yeah, he was the first, and I followed him.
**Martin Kuba** 23:01 Yeah, okay.
Yeah, I was gonna say, the thing that I would say, like, if people want to use the Metrics SDK, Like, they can, you know, I'm not gonna stop them.
But there are a couple things they need to be aware of, like… One thing that it's, like, it's not optimized. It's not gonna be optimized for the bundle size, like you said. And… and also, Also, there's an issue, like, if you model sessions as entities, then that they should not, you know, they should be aware that it affects the metric SDK the way it's written right now.
So… .
**João Oliveira** 23:48 In what sense, Martin? Sorry, and we can take this discussion I'll find food.
**Santosh** 23:54 So, I, I, I think, and Martin will know more than me. I think the way the metrics Spec, defines what attributes are finally part of the metrics that get exported, you know, they include the attributes you put on the resource.
And Martin is saying that there is a plan Today, the, the client-side telemetry only has things like, hey, what is the, browser, user agent.
You know, some basic things in the resource.
That itself may be a large kernelty, even if it's not a… super large, you know, the number of browser varieties are, you know, in hundreds, are definitely more than Two digits. But imagine if the session ID You know, becomes a resource attribute.
Then you will have… very high cardinality for if the session ID goes as an attribute on the metrics.
**João Oliveira** 25:13 And so, as it stands, if you… you were saying it impacts the metrics SDK as it works now.
Yeah, basically, as it works now, it's kind of…
**Santosh** 25:24 But, you know… Transportation.
**João Oliveira** 25:25 session ID.
**Santosh** 25:26 Yeah, yeah, it defeats the point, right? I think your metrics are supposed to represent aggregate information, but you are ending up creating a metric data point for every individual user.
So it will explode in the…
**João Oliveira** 25:41 Yeah, it was… Yeah, I understand why.
**Martin Kuba** 25:44 grateful.
**João Oliveira** 25:45 it's just… I didn't… I was not aware that the metrics SDK would automatically pick it up, and… Right.
But yeah, that being said, I can see how it's an issue.
**Martin Kuba** 25:55 So it's a little bit, like, fuzzy to me, like, what the real issue here is, because I don't think that backends take resource attributes automatically and use them as dimensions.
Like, automatically. I think the… so, it's possible that some… some will do that, but… but it's more… it's… my understanding is that, like, it's more, like, of a contract… contract issue, like a spec issue.
Because in the spec, it says that the resource is part of the metric identity.
So you have… You know, like, so, if you change the resource, like, in the SDK, like, it changes the metric series, essentially. It's like you get a new metric series.
So, like, it really depends, and if the backend does something, like, to identify the metric series, and it's all of a sudden getting something different.
Then, you know, per spec, it's… it's, you know, it's breaking the contract, right? Like, you can't say, like, we added some… we changed some attributes in the resource, but it's still the same metric series.
But, to actually… the way… the way the metric SDK is implemented is… is… it's really difficult to… The rep… like, it's impossible to replace the resource, so what you have to do is basically start a new instance of providers, like metric meter providers.
And because the existing meter providers have state.
So you have to, like, manage, like, fleshing out, and then starting new meter providers.
So, like, the complexity of that whole thing, like, in the client is quite high.
Way more difficult than… than in, like, with logs, logs, or spans.
Yeah.
So I guess, like, to circle around, like, I… like, if people want to use the metric SDK in the client, it's fine, but I think my suggestion would be, like, don't put resources You know, that could change.
On the… on the meter provider, so…
**Santosh** 28:13 I think that might be a harder, topic, martin, I… Like, not putting the resources onto… The metrics might be a bigger topic than, let's say, you know, warning the users.
That, hey, what we produce is high cardinality.
You know, and then be prepared to, you know, address that.
You know, on your ingest pipeline, in your ingest pipe… pipeline.
Because I think there are… even if the session ID is… is not to go into the resource, I'm… I'm sure, you know, people do put Other high cardinality… That's in the resource.
**Martin Kuba** 29:05 But it's, like… so, like, just to be clear, like, it's, like, two issues. Like, one is high cardinality. Like, we already have that, right? Like, I mean, it's gonna be, like, browser name, browser version.
**Santosh** 29:15 Yeah.
**Martin Kuba** 29:16 And then there's, like, the… the mutate, like, the… The resource attributes that could mutate.
So that's, like, they're, like, two separate issues in my mind.
**Santosh** 29:27 No, so that's what I'm saying. The resource mutating… Which results in… let's say, you know, session ID, or any, you know, parameters that you put into resource, you know, are now… Getting changed.
Is… is… it is still with respect to one client instance.
But even if the, you know, mutation doesn't happen, you know, you still have a high cardinality. Accra, when you look at, you know.
**Martin Kuba** 29:56 Correct.
**Santosh** 29:56 thousands of, you know, your users. So that problem exists invariably, you know. Your guidance needs to be, you know, highlighted in any case.
**Martin Kuba** 30:07 Yeah, correct.
And my sense is that in practice, like, in reality, it's not really an issue with the high cardinal. I don't think any backends will automatically take resource attributes and use them as dimensions, right?
Like, I think… I think they… I think, like, Prometheus itself only has, like, uses, like, the cert… like, couple of them.
Right? By default.
So you'd have to, like, you have to pick the ones that you want to use as dimensions from the resource. Like, it just doesn't… And I don't think anybody… I can't imagine that vendors do that, but… .
**Santosh** 30:48 Actually, in your… actually, I need to go, but maybe next time, let's maybe… C… How would, let's say.
like, I have made changes to the OpenTelemetry demo, I can, you know, push that into a, you know, a branch. And then we should see how… that would work end-to-end. If Prometheus were to, you know, script those metrics, you know, will it still go through a collector? Like, in your cloud, Grafana cloud, you know, do you guys… For ingesting metrics, you know, is it through, you know, some collector-like service where, you know.
Prometheus would then, you know, pull the metrics, or, you know, is it typically that At the customer network itself.
you know, the metrics are supposed to go into a collector from where the, you know, the local Prometheus scrapes, and then there is a Prometheus to Prometheus federation. I think we need to understand the architecture.
**Martin Kuba** 31:46 Yeah.
**Santosh** 31:46 End-to-end, and, you know, and then… C.
**Martin Kuba** 31:51 Yeah. And by the way, Santosha, I don't know if you've seen this, but we have, we have a demo demo in the browser SDK repo for this. Like, there's already some…
**Santosh** 32:03 Okay.
**Martin Kuba** 32:04 Like, so I can… maybe next time I can… I can demo it here, so… Yeah.
Alright.
Okay, alright. That's good.
**Santosh** 32:13 Thanks, Paul.
**João Oliveira** 32:14 Gross.
**Martin Kuba** 32:15 See you later.
**João Oliveira** 32:15 Dear.
