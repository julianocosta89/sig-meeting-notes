SIG: Client Instrumentation SIG
Date: 2026-04-28
Duration: 30 minutes
============================================================

## Zoom Recording Transcript

**Jason Plumb** 01:02 Hey, Martin.
**Martin Kuba** 01:04 Hi, Jason, how are you doing?
**Jason Plumb** 01:08 Pretty good, how about you?
**Martin Kuba** 01:11 Not too bad.
bread.
Tuesday mornings are, like, the worst.
**Jason Plumb** 01:19 Yeah, cause you have to start early, or…
**Martin Kuba** 01:22 No, no, I mean, I thought I felt like Monday was kind of easing back into work.
Tuesday is, like, when it really hits, so…
**Jason Plumb** 01:32 Yeah, we have an 8AM Android SIG meeting on Tuesdays, and that's entirely too early for me.
**Martin Kuba** 01:38 Yeah.
Yeah.
**Jason Plumb** 01:43 Well, not to draw this out too much, but I ran into our coworker Ray from New Relic yesterday.
If you remember him, he was on the agent… he was the agent developer on what team?
I don't remember, Ruby, maybe?
**Martin Kuba** 01:57 Okay, yeah, okay, I know what you mean, yeah.
**Jason Plumb** 01:59 Yeah. Really into purple, likes purple a lot. Yeah. Ran into him yesterday, like, lives not too far from me, it turns out.
**Martin Kuba** 02:08 Okay.
**Jason Plumb** 02:08 Yeah.
That's cool. Someone has also screwed up this dock.
Do you want me to share my screen, or do you want to drive this, Martin?
**Martin Kuba** 02:22 Go ahead, it's… you could… Okay.
**Jason Plumb** 02:26 I'm not gonna make a habit of this.
Okay, so this is our doc. This is linked from the community site, right? So… Like this.
**Martin Kuba** 02:38 It's…
**Jason Plumb** 02:39 Somebody's completely just, like, pasted some shit in here. Okay, so let's… let's fix that, first of all.
And then let's make a new meeting!
Look at this.
We're so far behind.
Okay.
**Martin Kuba** 03:06 Yeah, I try to remember, like, last time I joined, maybe there wasn't anything to discuss.
**Jason Plumb** 03:10 Yeah.
**Martin Kuba** 03:11 Yeah.
**Jason Plumb** 03:12 Well, I have one thing, and whoever else wants to add their names to the attendee list.
and or the agenda, please feel free to do so. I will add the first item… Alright, so we in Android have this pull request, which has been open for a while.
And this, renames our existing crash event from what's now currently device.crash into app.crash.
Which, if you think about it, is a little more narrowly scoped, and hopefully makes more sense, because we're not logging, or we're not eventing that the entire device has crashed, we're just inventing that your application has crashed.
And there is a corresponding… so there… this is the Android PR.
And this is the corresponding Semantic Conventions PR, which addresses this, and this has been open since February.
So we could really use some other ayes and approvals on this. So we've… there's been a lot of discussion, 31, you know, comments already on this semantic conventions change.
And what it really boils down to is dialing in the name, right, which we've decided is app.crash.
And then adding a little more detail about what What that event means, like, what the semantics behind it are, and then what… attributes can be available on that. So, we have… on this PR, we have two approvals.
of component owners. One of them is me, and one of them is Cesar.
I believe.
No, one of them is Hansen. No, this is Hansen's PR.
One from… one from Cesar, and one from me.
And just yesterday, or recently, one of the maintainers, Lumila, on… has marked this as, needs more approval.
So, it was awaiting code owners, and now… so I guess they have a pretty complicated process over there now, where they have this multi-stage approval thing, but whatever, we need more approval.
So if you have opinions on this, and you're in this meeting, please give it a look, and even if you are not a component owner, if you give approvals, it will help to move this forward.
**Martin Kuba** 05:48 Well, I can… I can say for sure that, like, this is very much of interest to us.
**Jason Plumb** 05:53 Cool.
**Martin Kuba** 05:53 So I will bring it up to our team, to our mobile team, and have them look at it, yeah.
**Jason Plumb** 05:59 Okay.
**Martin Kuba** 06:01 Yeah, thanks for sharing.
**Jason Plumb** 06:02 Yeah, yeah.
Cool, I don't think we have to belabor that, but the links are in the doc, and yeah, so please take a look at those. If you have any questions, raise them, and if you can give an approval, that'd be killer. Let's move on to Santosh, because I think we only have half an hour for this meeting, right?
**Martin Kuba** 06:20 Yeah, only a half hour.
**Jason Plumb** 06:22 Cool, so Santosh, it sounds like, from this, it sounds like you might be kind of loosening up on this a little bit. You're coming around to my weird world, where I also was very against metrics on client side, and I'm starting to warm up to it, yeah.
**Santosh** 06:36 Yeah, and I'll tell you, you know, what made me… you know, rethink on this. We were… We're working on… WebSockets instrumentation, and we noticed that you know, WebSockets is, you know, plain… like, it's very hard to, you know, build instrumentations other than, you know, your initial, hey, I started my WebSocket, and this is how long it went. But when you want to provide insights about you know, what's going on, you know, inside the WebSocket. You know, there are frames that are exchanged. People want to measure You know, how long some of their, you know, frames, whatever applications, you know, application protocol they have, that, hey, I'm sending certain requests in my frame, I'm receiving a response, I want to measure, you know, how long it took.
And it… it felt… it appeared to me that, hey, in the back-end applications today.
all over the code, we put all sorts of metrics to measure, you know, various parameters. It would be nice if we had the similar ability here, where customers could, at random places, you know, wherever they want to measure, you know, they put in counters, histograms, you know, whatever, and then just, you know, view them in the dashboards.
It is not always a need for, you to view the individual events, because you're really looking at an aggregate.
The moment you talk about metrics, you know, you're really only worried about, how things are in aggregate. And maybe, you know, you do need certain exemplars, but given that the metrics API supports exemplars, we will have to think about it. But there is a possibility to… annotate your metadata points with additional data, you know, in the exemplars, if people want to look at You know, certain events, certain, you know, point-in-time events that, you know, could help you With, you know, additional insights. But that said, I think, I'm sold on the Metrics API now, but I'm not sure about the reliability of shipping them to the backends. I think there are still concerns that we need to think through. With RAM, unlike the, you know, the backend, you know, infrastructure, you know, situations.
the RAM clients, you know, have reliability issues. You know, connections are choppy, mobile apps go offline.
Your data, you know, ends up… Reaching the server late.
So I'm not too… familiar with how to handle things there, but that's one part, I'm thinking we should, think through.
There are… I'm also worried about, like, one other concern that I had, you know, mentioned in the original issue that I created. There are too many connections, you know, our RAM clients now have to open, one for each signal.
and… Y-you know, it's possible that we could still transform the metrics And export them as events.
But now that the events have a standard structure representing the metrics, it will be easier for the, you know, some backend component to… you know, recognize the high cardinality Attribute high cardinality dimensions, drop them.
And then put the metric back.
As a metric data point and send it to the metric systems. So, these are some thoughts,
**Jason Plumb** 10:41 Yeah, Santosh, so I like this… this question about, like, where… so one… the reason I've come around a little bit on this metrics usage on client side, too, is because I think Sending the data points and letting your backend, or letting your pipeline deal with it is probably, in many cases, preferred Over having the agents, the clients, be too smart and make all the decisions up front.
If you're sending those data points, and they're also very high cardinality, you can, in your backend or pipeline, drop dimensions there.
Or if you have a high cardinality, you know, time series database, you can just throw them in as is. But at least getting them out of the process allows you to later do this aggregation that you're talking about.
I've put a, I put a link to this PR that I made a while back. Wrong window.
Come back to me.
Let me just show it here. So I linked to it, it's… I was just mostly playing around with seeing what it would look like to… To do, kind of, this massaging of metric data points on the client side. So, I took… What starts out as, this is what the resource looks like.
And in most backends, I think the resource attributes become dimensions, and I was like, well, what does it look like to take metrics and trim that down to a certain subset that maybe people will care about? And is much lower cardinality.
And I kind of experimented by choosing the OS, the type.
the OS information and the service name, right? So just distilling it down to that. And the way that we do that is with this customized… this… I think this used a custom exporter that just drops or mangles the data points on the way out, and, you know, it's not a great idea, but it was just an experiment to see what it would look like.
I'm still… I'm with you, I'm kind of leaning these days toward setting the high cardinality out, allowing it to be that, and if it gets dropped, it gets dropped.
But, to your point, doing that is kind of expensive, right? There's a cost on the client side in terms of using that data connection and, you know, having an unstable network in which to do so.
**Santosh** 12:54 Yeah, I think the cost is definitely higher, with in this situation than a backend, because the aggregation, right? You know, we have to do… when we say drop high cardinality, it is not just, you know, dropping that, you know, dimension. You have to… Aggregate, you know, all the metadata points, you know, within.
**Jason Plumb** 13:13 Yeah.
**Santosh** 13:14 that dimension, and then, you know, drop that, because it is no more relevant.
Typically, in a backend application, you know, you would be doing… you would be actually You would not be sending a metadata point for every individual event. You would be doing some sort of you know, aggregation, let's say you are exporting every 10 seconds, or every 1 minute, you're pulling, you know, the data points for that duration. You're doing some sort of aggregation.
**Jason Plumb** 13:42 works.
**Santosh** 13:42 client, situation.
You might do, let's say, you know, in your example about, let's say your Core Web Vitals are emitted multiple times, you know.
you know, then you would aggregate them. But it's minimal, I think.
You would still… you would still have to aggregate across all your users.
So the cost is definitely higher.
**Jason Plumb** 14:07 Yeah, yeah.
Yep.
Anyway, I… you mentioned, only because you mentioned, WebSockets, I don't know if you ever… this is totally off-topic, but I don't know if you ever… saw when you were working on this stuff. Did you ever see this thing I wrote, like, a while back?
**Santosh** 14:25 I see.
**Jason Plumb** 14:26 I can send this to you.
**Santosh** 14:28 Yeah.
**Jason Plumb** 14:28 This is definitely on the Java side of things, and really focused on Stomp, but I can send this to you, because…
**Santosh** 14:34 Okay, perfect.
**Jason Plumb** 14:35 interesting. I'll just send it to you on the corporate Slack.
**Martin Kuba** 14:41 So do I, do I understand correctly that, like, you, you feel like… There are use cases where… where users might want to collect metrics, regenerate metrics from the in-the-client SDK, But… But we need to obviously solve the high cardinality, and we need to, you know, solve the aggregation across clients.
So, is this more kind of just, like, an API kind of ergonomics?
issue, or is it… is it…
**Santosh** 15:19 There are two, two parts there, Martin. I think, like, firstly, you know, we… we always wanted metrics, you know, in the RAM applications. It's just that the… we… we were not sure whether to really use the metrics API or create events that, you know, get aggregated into metrics on the backend, so… Either ways, you know, you would… the outcome is, you know, you create metrics.
Now… The… concern, or rather the argument that Hansen also made.
was that many a times, you know, you need the individual raw events to make sense.
which I believe, you know, is really important, but there are, today, if you look at, you know, your backend applications code.
at least I have seen that people do put a lot of metrics all over the place, you know, because they want to measure many things, and they don't necessarily, you know, care about individual instances.
And luckily, you know, the Metrics API supports the concept of exemplar, so you do put a… Like, a maximum of, let's say, 5 or 10… Sample, events per data point.
Your data point could accumulate, let's say, you know, 10,000, events, but you, you, you keep, let's say, 4 to 5… a very small number of.
Events you save with the metadata point, so that You know, you do get a chance to inspect, hey, if there is a spike, hey, show me some sample events that You know, contributed to this spike.
**Martin Kuba** 17:08 And really, it's answering…
**Jason Plumb** 17:09 Go ahead, Martin.
**Martin Kuba** 17:11 I was gonna say, but anyway, like, from… That is true, you may not care about actually collecting the events, but from, like, the SDK perspective, like, if you're not doing, like, a lot of aggregation in the client instance itself, then it doesn't really matter, like, if you send an event or a metric data point.
like… And, like, if you were aggregating on the backend, right? I mean, you could just, like, aggregate on the back end, and then just, like, toss the… toss the event, I mean… But, you know, so, like, I… I've been thinking about this a lot, too, and actually, like, from a different perspective, I've been talking to the entities, SIG, because I… I think we… like, one of the things that, like, we also need to… we need to, like, finalize or… or work on is… is, representing sessions.
and maybe, like, even other things in browser as entities, which means that, like, the session ID would no longer be an attribute that you put on all signals, but it would be a resource attribute, which has… has an impact on… on metrics. And when I talk to… because… because of the… because of the dimensions. And when I was talking to, to Josh… Josh Surath about this, he was… he was saying, like, well, maybe… maybe, like, the client… client 6 can move forward if we agree that then, like, we would not be sending metrics from… from, from the SDKs. That would simplify things a lot.
Or we could… we could have, like, a metrics… like, a very simple API for metrics, but behind the scenes, it would just send… send events.
And not do the aggregation.
So that's… that's kind of my… my kind of, angle on this right now, like, I would like to… To get the sessions, you know, figured out as entities.
And I'm a little bit… I'm a little bit worried that, like.
This might… this might take it in a different direction, but… I'm curious what you think.
**Santosh** 19:30 I think in general, what attributes… get onto the metrics. Today, along with the attributes you specify in the metric data point, the resource attributes also guaranteed, right? I think it, it, it's, it's something that the… back-end metric systems, you know, how they… I don't think the OpenTelemetry has any guidance, Other than saying, hey, this is what we sent, but what you… use on, you know, as dimensions on your metrics, it's up to you.
With the exception…
**Jason Plumb** 20:09 With the exception of resource attributes, right? It's kind of assumed that the resource contains a ton of dimensions.
**Santosh** 20:16 Right, right. And that is where I feel like, you know, this cannot be avoided. I think the, No matter what we do, you know, our client instrumentations, you know, we do identify Session ID is, is, is, you know, is not the only one, right? There are, there are, there has always been device identifiers, let's say, in mobile, you know, your, that is high cardinality, you know, that goes into a resource as attribute. Even on the mobile, even on the web.
We do want to identify every individual user, you know, maybe It may not be common, but… I think we should consider it a given that resource, in the case of client instrumentations, is high cardinality.
And, you know, the backend receivers have to make a call.
Explicitly, you know, which dimensions in the resource they want to keep.
**Jason Plumb** 21:16 Yeah, I mean, the way I kind of think about it, too, is, like, I imagine, like, an application developer ships an app, and they're working with a product owner, product manager.
And the product manager's gonna come and ask them, like.
how long does it take to load that second screen, right? Those are the kinds of, like, business-level questions that a product person's gonna ask, and you're like.
I don't know, let me go and look at our observability vendor, and I have metrics around that, because I was very smart, and I used OpenTelemetry, and now I can tell how long it took. And you can tell your boss then, you can say, oh, loading the second screen takes 1.3 seconds, takes 1300 milliseconds.
But that's not telling the full story, right? You can tell your boss that, and maybe they're happy with that, but… it's taking 1300 milliseconds on some devices in some countries some of the time, you know? There's a… there's definitely a continuum, there's a spectrum, there's a histogram of these durations, and it's broken down by Dimensions, which include things like what device you're on? Are you on a new phone or an old phone? Are you on a new OS or an old OS? Are you on… a slow network or a fast network, are you on 3G or Wi-Fi? You know, it's like, those things actually matter a lot to answering the question, and people will gloss over that, and sometimes they don't care. Sometimes they're like, what's… what is the average user experiencing? Like, what's my median user experiencing? That's… sometimes that's enough.
But to have some dimensions, and at least if you're getting the raw data out of the app.
With all of the cardinality, all the dimensions, at least you can then later decide in your backend, without having to push a code change to a million handsets, you can decide, okay, Region is now important to us, and we want to start indexing on region, right?
I don't know. That's where I'm coming from. That's the way I'm looking at it these days.
**Martin Kuba** 23:12 But it… so the way you're describing it, that sounds to me like an argument for not sending metrics from the SDK.
**Jason Plumb** 23:19 I would send them from the SDK, and I would send them full fidelity, and then the backend can deal with it.
**Martin Kuba** 23:28 So the backend would have to then process the metric endpoint, the metric the metric, well, I mean, in that case, why… If you have to do, like, processing on the backend, why not just send an event, then?
**Santosh** 23:42 Yeah, you can. I think that is where the ergonomics topic comes into the scene, where… The metrics API, even I used to feel the metrics API is complex. Like, today, my legacy, you know, RUM, interfaces had a very simple metrics API, right? You know, you know, create metric, and then you do things. But now you have to you know, use counters, gauges, histograms, so it becomes, you know, a lot more complex, but I think it's a step in the right direction. You know, people are familiar with these concepts when they create metrics in the backend applications, then why not have the UI engineers, too, adopt the same APIs?
So it's the one standard API, be it… you know, front-end, back-end, whatever, right? I think you're… it's a standard API.
**Martin Kuba** 24:36 income.
**Jason Plumb** 24:36 Yeah, and Martin, to come back to your kind of conceptual question, like, why… like, why use a metric instead of an event? That… that's the age-old question about all of this telemetry stuff.
it all could be distilled down to logs again, right? Like, this whole observability game started with logs, right? We were all emitting logs in the 1970s. Like, we can still do everything that we want to do now if you had enough logs.
But there's certain things, like.
The idea of an event is like a point-in-time, zero-duration thing that indicates that something happened.
And yeah, you can, you can pack other… other contextual information in that event, like account of something, for example.
But we also have the idea of metrics, one of which is account. And so, if you're expressly doing things like tracking the value of something over time, that's maybe a gauge, right? And if you have… if you're just counting a number of times that something happened, that… that is a counter. Like, we have these metric types for that reason, is because they… they distill down these aggregated concepts in a way that, you know, events may not, or it's less natural, I think, for an event to represent that.
**Martin Kuba** 25:59 So I guess… I guess, like, I don't really have… like… I think I need to, like, look into this a little bit more detail, because I feel like if you have… if you are actually running the metrics SDK in the client, then the aggregation happens in the SDK itself, based on the dimensions that you have.
in the SDK, we charge the resource attributes.
**Santosh** 26:21 No.
**Martin Kuba** 26:22 Which, which I think… right?
**Santosh** 26:24 No, no, the… when you say aggregation happens, you still want another round of aggregation across your users.
**Jason Plumb** 26:32 True, yeah, and that can happen on the back end, yeah.
**Martin Kuba** 26:34 How does that happen, though? Because, like, if you have… like, if you're not sending just one event, but you're, like, you're actually doing some aggregation using the metrics SDK in your client, and it's… the metrics SDK is built to use the resource attributes as dimensions, and then you send it off to the backend, that you have to, like, unpack those different types of metrics into You know, and, like, combine them… Like, into different metrics, or how, you know…
**Jason Plumb** 27:02 I mean, to be fair, resource attributes are not exactly dimensions, but I think everyone treats them, or they should be treating them.
**Martin Kuba** 27:08 Awesome.
**Jason Plumb** 27:08 Right? Because they identify the unique source of that telemetry.
But the aggregation is such that, like, if you have… if you have a one-minute collection cycle.
and you're counting something, and it happens a thousand times a minute, you're not generating a thousand events, you're generating one metric data point every minute that represents those thousand, right?
**Martin Kuba** 27:30 And, like, we have… we have, like, known use cases for that kind of stuff.
**Jason Plumb** 27:33 I think so. But then it comes… when it comes out of the agent, the client side, the mobile agent or whatever, it's gonna have a very rich resource that has a lot of stuff on it. It's gonna be super high cardinality when you take it across a million handsets.
And so, that's where the backend would need to be a little smarter in how it… how it drops stuff.
**Martin Kuba** 27:55 Do you know, if you… Sorry, do you know, like, if there are any, collector… Plugins that can do that right now?
**Jason Plumb** 28:05 Yeah, I mean, you can certainly drop and aggregate in the collector, yeah. I mean, aggregation's tough, because there's constraints, but definitely you can drop resource attributes, yeah.
**Martin Kuba** 28:15 Okay.
**Santosh** 28:17 Yeah, and I want to add to that that this is not something the metric platforms are Ready with today.
They do expect that before you ingest data, you know, you drop the high cardinality dimensions.
some metec platforms provide the ability to, you know.
do the aggregation and drop, but not all too. So I think we need to… You know, study this further, in that the data will still have to be routed through another intermediate aggregation system before the existing metric platforms can take those.
**Jason Plumb** 29:02 Yeah, I have to play Time Cop a little bit, but Martin, go ahead.
**Martin Kuba** 29:05 Sorry, like, I just want to say one more thing before we disconnect. So, I'm actually been, like, wanting to work on a prototype.
For the browser SDK around sessions and metrics.
Because specifically the entities, Josh and the entities SIG has asked for this, and, like, if you want to push for, again, like, coming back to this for sessions being entities, then, like, we… like, Josh has specifically asked that, like, we demonstrate how we envision this to work.
**Jason Plumb** 29:35 Yeah, yeah. I think.
**Martin Kuba** 29:36 I have a.
**Jason Plumb** 29:36 I backlog to try a prototype of this as well, based on some work you already did. I'm not gonna get to it this week, maybe not next week.
**Martin Kuba** 29:43 Yeah, so I might… I might need your help, then. Like, if you… if you feel strongly about this direction, then I might need your help to, like, to, like, give you some… some feedback on that.
**Jason Plumb** 29:52 Okay, cool. Yeah, I'm fully expecting to need to rev to 2.0 on Android, because we have stabilized our session.
API. So, I put a note of that, you can review it, but we're out of time, so we have to call it.
**Martin Kuba** 30:06 Sounds good.
**Jason Plumb** 30:07 Alright, thanks everyone.
**Martin Kuba** 30:09 See you later.
**Santosh** 30:09 Thank you.
**Jason Plumb** 30:10 Bye.
