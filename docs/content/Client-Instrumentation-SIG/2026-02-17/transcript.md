SIG: Client Instrumentation SIG
Date: 2026-02-17
Duration: 30 minutes
============================================================

## Zoom Recording Transcript

**Santosh** 00:59 Hi, Martin.
**martinkuba** 01:03 Hey, Santosh, how are you?
**Santosh** 01:06 I'm good, I'm good How are you?
**martinkuba** 01:09 It's been a while. Good.
**Hanson** 01:10 Hey, yeah, it's been a while.
**martinkuba** 01:13 It's like the old group.
**Jason Plumb** 01:16 Getting the band back together.
**Hanson** 01:18 Yeah, and talk about an old favorite, metrics.
**martinkuba** 01:23 Yeah.
**Santosh** 01:25 Let me add to the agenda, so Martin knows.
**Hanson** 01:28 Cool.
Should I just copy the entire thing and…
**Santosh** 01:53 Yeah, yeah, I'm doing it.
**Hanson** 01:54 Okay, cool, sweet.
Get some water in a second.
Back.
**Santosh** 02:34 So, Martin, I was just speaking about… on this topic with the Android team, and Justin suggested that the… this client SIG is right after the Android sig, so we said we'll continue talking about it. We didn't speak a lot, we only spoke for 5 minutes.
**Jason Plumb** 02:51 Just so you know, Santosh, it's every other week, 30 minutes.
**Santosh** 02:56 Okay.
So we don't have a lot of time, so, this is a controversial… Actually, within the group, it is…
But maybe it's beginning to get, interesting, right? Now that you are, you're changing your, you have new thoughts, so…
Maybe let's dive in. Are there any other topics, or, is this a topic we can…
Take the entire 30 minutes.
**Jason Plumb** 03:21 I think so, no one else has put anything on the agenda, so…
**Santosh** 03:25 Okay, we can start talking then.
**martinkuba** 03:28 I do have potentially one other topic, but it's not urgent, like, we can see if we have time or not, so…
**Hanson** 03:34 I mean, I think the topics from last week, or two weeks ago, seem interesting to, two men who missed it.
**Jason Plumb** 03:40 Yeah, no, it was like, no one was there, and the agenda was, I think.
Empty, and we just started riffing on stuff, and that's how we ended up with this, but,
So, I'm thinking about metrics these days in, kind of, application concerns. I think… I'm thinking from, like.
an applications developer's perspective, and they're like, cool, I have this… this awesome new tool called OpenTelemetry, it's at my disposal, I put it into my app, I get all this whiz-bang instrumentation about crashes and, you know, A&Rs and stuff like that, great, but I also… now… now that I've got the sort of baseline, like, RUM,
Stuff wired up.
I want to expand my use of that. I want to add some manual instrumentation around my application behaviors. Like, I want to know the number of times a button gets clicked, or I want to know the number of times that…
Or I want to know the average amount of time that a user spends in a certain screen.
Right? That kind of stuff.
So…
one way of doing that is with metrics. Of course, there's more than one way to skin a cat. You can omit a start event and an end event, and come up with all of your own custom stuff, and sit those together in your backend, however you want to do it, right? But…
At least, if you have open telemetry at your disposal, and you're doing things like measuring, to me, it seems like metrics are what people will think of instantly.
And because… because the way of doing measuring, specifically, like, with an instrument.
is so closely tied with metrics that I think users will just naturally assume that they can use things like
Counters and histograms.
You know, to get measurements.
So that's why I'm relaxing on this stance a little bit. How you deal with the data on the backend is still gonna be complicated, but… and I don't think that open… I don't know if this has ever come up before, but something that occurred to me last meeting was if we had some sort of…
Equivalent of a metric view, but if it applied to resources.
Right, so metric views are these really powerful tools
But we almost need, like, a resource view.
Which applies to some metrics. Or, like, if somehow the resource could be accounted for in metric views, then you could do these cool things where you're like.
I don't care about the install ID for these types of metrics to reduce the cardinality. But again, backend can do that, right? You see a metric with this name, just throw a bunch of that resource information away if it's not important.
Anyway.
That's what I'm thinking about.
**Hanson** 06:32 I mean, ye…
I think where I'm coming from is, I think I agree with the assertion that metrics is very natural. The API, like, hey, I want to count some stuff, let's count some stuff. and the API is very natural for you to, like, tie it to spans and things like that.
So almost like the API, I like, and feel like there should be, you know, some level of support for.
where it gets a little bit tricky is what the data looks like when it gets back to the server. So, assuming high cardinality is not a problem,
every… every measurement, will be… will have information to distinguish, that, hey, I'm looking at the data usage for this particular device, in this particular session, like, whatever you choose the resource, you know, to be. So that when you go into your dashboard, you can say, hey, there's a really high usage.
what generated that? You map back to the session, you map back to the device, here's the information, oh, that's the reason, cool.
Once you anonymize that.
And you basically say, you're in a fleet of 2 million devices, used a total of… So many terabytes.
And there are so many, you know, app startups and events.
You have a very big denominator, and an even bigger numerator, and you can divide that.
I think in… in… if you… if you… if you're in a factory… if you're in a warehouse, and your devices are, not, like, you know, web browsers or Android apps running the world, there is a use case for… for bringing all that in, which is why I think the API, supporting the API and all that stuff is, I think.
something useful, because there is a niche use case. But I think the generalized use case, because…
we have to basically get rid of, whether it's on the client or on the back end, the identifying dimensions, and let's just not even call it high cardinality, the identifying dimensions, as well as the time component. I mean.
We're not even… we're, of course, only talking about things that… that… for which time doesn't matter too much, or could be tied to some other dimension.
then that could be useful.
But what Santosh is saying, is, like, by default, a lot of instrumentation, like with HTTP, will emit a bunch of metrics.
And they will not be useful for client-facing apps. So…
Based on that, I don't mind,
the recommendation and the stipulation explain all that stuff. But it doesn't mean that we don't want to support at the API level, and it doesn't mean that eventually we don't want to have a way of dealing with
metrics where the resource can be a bit more identifying than what it currently can be. But that will, I think, take a bit of a leap.
**Santosh** 09:41 So… Yeah, I mean, thanks, I think this is,
helpful. I want to add one more thing to what I said previously.
And I think it's more about ergonomics. Like, my point of view, I'm pointing out.
a different view. I think my reasons for not… Emitting metrics is… For instrumentation simplicity.
And we have seen, in the industry, people…
Choose certain parts for the sake of like, you know.
like, designed by convention, right? You choose to do a certain way first for some reason, and for simplicity.
Because… It helps you with scale.
And in this case, I'll… I want to cite one more example, one more possibility.
that imagine… You know, somebody wants to also emit application logs.
Which are different from events.
But the underlying data structure is, is log records.
You know, you might… You might want to…
I, I, I… if my understanding is right, there is no separate SDK for events, you know, you, you have to…
explicitly configure Two log exporters.
And, and then… And then, in those exporters, you have to explicitly filter out, you know.
log records that are not of interest to you. So there will be one pipeline, export pipeline for the application logs, another export pipeline
emitting log records, but emitting the non-application logs are the events. I think, thankfully, you know, we have a convention that which log records are events, the ones that have an event name, right, or whatever is the API conventions. Conventions, you know, that were introduced for the purpose of
Apis.
**Jason Plumb** 12:05 I missed why… sorry, I missed why we're switched to talking about metrics, or logs pipelines instead of metrics.
**Santosh** 12:11 Right. I was trying to make this point, Jason, that There is also,
A path to a more complex instrumentation setup that customers will love to do.
our application developers will have to do, if they were to also emit logs, right? I think now we… the… they will have to set up pipelines for logs.
**Jason Plumb** 12:38 If they want to emit logs and have a backend that can't differentiate correctly, or, you know, if you need to export to different backends, or events and application logs, then yes, there's a slightly more complicated setup, yeah.
**Santosh** 12:54 Right, and I think we should… we should… Open Telemeter should have an opinion about it, given that we are…
like, I think so far, like, my participation in these meetings is very, very, you know, small, but I have not seen,
The amount of consideration that it deserves to.
**Jason Plumb** 13:15 When you say it, be specific, what do you mean? What's not getting the consideration it deserves?
**Santosh** 13:21 The… how the backends are, configured.
How the receivers are configured.
**Jason Plumb** 13:28 So…
**Santosh** 13:29 It is considered to the extent where collector is.
Is involved.
But beyond Collector, I haven't… seen much concentration.
**Jason Plumb** 13:42 I mean, as a consortium, a bunch of different vendors that have different backend implementations, different architectures, I think a lot of consideration has been given. It just may not be always easy to identify where that's expressed in the specification and the SimConf, but I think it's there.
**Hanson** 13:57 And I believe a lot of this stuff was discussed in the log sig, about whether it's one pipeline or two pipelines. I mean, I think they went back and forth and back and forth, and…
it eventually became one with a distinguishing attribute, so this does favor the ease of configuration. You don't have to set up two pipelines, it's one pipeline. If you can distinguish and you want to kind of fork out, you know, at your end or the client's side, it's up to you.
**Jason Plumb** 14:23 I mean, you could say the same thing about manual instrumentation with spans. You could be like, well, the user's manually created spans should go to a different backend than the instrumentation spans.
Should they? I don't know. Depends on… depends on what you want to do.
**Hanson** 14:37 But that… but that's not the API, so… so, like, I think, I think,
the concern about, the API and whether end-user-facing apps use that API and therefore create these things that the backend has to handle,
I believe there… it can potentially be a use case, but maybe not in the mainstream one.
the backend aspect of this is, I think, where your concern lies, so it's almost like…
It's almost like… it's… it's…
It's almost like you're saying back-end collectors, hotel collectors that are taking information from, end-user-facing apps should not have to configure, metrics as a default, which is…
kinda not where I'm approaching this from. So you may actually find more, more, informed opinions if you talk to the collector folks.
Because I would be coming from a different perspective, and I don't know if it's going to be the same. Because you're talking about, basically, collector configuration. Don't bother configuring it.
To receive it.
**Santosh** 15:52 Yeah, collectors are, are typically, for… for rum… Apps.
for the RAM architecture, you know, typically there is no architecture, there is no collector involved.
Because the… the rum… Clients are out in the wild in the… on the internet.
And they reach your target systems directly, you know, instead of being routed through collectors.
**Jason Plumb** 16:21 I'm sure
I agree… I agree with that, Santosh. I think there are… I think there are vendors that run a fleet of collectors behind a load balancer.
**Santosh** 16:27 Okay, okay.
**Hanson** 16:28 Yeah, that's.
**Santosh** 16:29 That's possible, but it's, it's, it's, yeah, okay.
So, where are we?
So, if metrics is something that we want to adopt, then I think we could you know…
Use it more as well, more than we currently do.
**Hanson** 16:55 But there are fundamental reasons why it can't be used right now in a useful way. It's almost like…
We would like to use it, but we need certain changes. But until then, it's very limited. So, it should be only used in a certain way, knowing that these limitations are, you know, are in play.
Therefore, unless your use case fits these very, very limited things, where you want to count for the entire fleet, or some sort of low cardinality dimension.
**martinkuba** 17:27 without any time, you know, abound.
**Hanson** 17:32 don't do it. That's what I want to say on the API side, or the usage side.
**Santosh** 17:38 Yeah. So, if… if we go…
the direction that I'm, thinking, then ideally, we would add a guideline to our individual reports. This can't be a spec level…
Guidance, but at least within the
instrumentation reports will add a guidance saying, hey.
You know, do not emit metrics, because that we agreed to not do.
And therefore, we will remove or move away from anything, you know, like the couple items I pointed out, you know, we would remove them and then replace them with events.
**Hanson** 18:17 I don't know if there are any end-user-facing instrumentation, exclusively end-user-facing, app instrumentation that uses metrics. Except maybe the OKHTP, it's not OKHTP, the, the HTVR connection one that Serbi added on Android.
But the OKHTP one has metrics, but it's also used for backend applications, and that's totally fine.
For them to do that.
**Santosh** 18:42 Okay, so right now, unless an exporter is configured, you know, those…
metrics emitted will just get ignored, right? They'll get dropped at the source itself.
**Hanson** 18:52 go up.
**Jason Plumb** 18:56 Yeah, right now, I also don't think there are any Android instrumentations that emit metrics.
We've… and I think we've discouraged it, like, we've shied away from it and said no, I think, a few times.
**Santosh** 19:06 Hmm.
**Jason Plumb** 19:07 When it's been asked about…
**Hanson** 19:12 So, maybe it might help you, if there's, like, an intermediate kind of recommendation, which is on the instrumentation side, that instrumentation should not
anticipation exclusively used for end-user-facing apps at this point, should not emit metrics unless it fits a certain set of criteria, which is basically codifying what… the advice that we've been giving.
And that could… that could go into OpenTelemetry I.O, just like the… the best practices. And then, I think if you want to develop something more comprehensive about… about pipeline configuration and auto-instrumentation, you could use it based on that.
If that makes sense.
**Santosh** 19:58 Yeah, it does, but I think it'll be helpful to also provide an example.
of… Even if it's hypothetical.
As to when it might be… You know, considered.
**Hanson** 20:14 Yep. Like, yeah, like, if you want to track the total number of clicks on a button for the entire fleet.
**Santosh** 20:20 Hmm.
**Hanson** 20:21 This is useful.
Do you want to do that, if you can't do any divisions?
**Jason Plumb** 20:27 Because if, yeah, because if you have a business goal of, like.
You know, we want to get to a million clicks on this button before the end of the year, like, you know, having something that tracks that.
And, I mean, clicks are stupid. I mean, you can count events and make a lot of events, but if users click that button very fast, that becomes a lot of events.
Right? Whereas if they're aggregated permanent, then it's much simpler in some implementations.
**Hanson** 20:54 Yeah, it'd be probably at lower level, it'd be, it'd be like, you know.
something where events is… is… is… provides too many, too many things to count up. So, yeah, even button clicks, you don't necessarily need to do that. You could, but you don't need to.
**Jason Plumb** 21:11 Yeah, Martin…
**Hanson** 21:12 Whoa!
**Jason Plumb** 21:13 You gotta turn that camera thing off, man.
**martinkuba** 21:17 dominated.
**Hanson** 21:17 That's.
**martinkuba** 21:18 It just, like, started doing this, I don't know why…
**Jason Plumb** 21:21 It's a totally a Mac thing, and I forget how you turned it off. It's called… Center stage.
**martinkuba** 21:28 Oh, okay.
**Jason Plumb** 21:29 If you click on the green… it's green on mine, up at the top when you're recording.
A thing called Center Stage, and you can turn that off, and then it won't…
Change your camera on you.
**Hanson** 21:42 Okay, so… What do you want to put where, I think is my question.
**Santosh** 21:49 Yeah, yeah, yeah. Let's hear Martin. Yeah.
**Hanson** 21:53 Oh, okay, oops, yeah, sorry, heads up.
**martinkuba** 21:55 No, I just wanted to clarify, so I think we've, in the past, talked about, that we couldn't think of use cases for collecting metrics in the client SDK, but there were use cases, like, on the backend, so, like, if you were sending events, you could generate metrics from those events.
is… so, am I hearing correctly that you actually think there might be use cases where
there are so many events happening in a single instance of the client SDK that it might make sense to send it as a metric instead of a lot of events from that particular instance.
Is that it, or…
**Jason Plumb** 22:31 I'm… I'm starting to come around on that idea. Like, historically, we've said no. I'm starting to warm up to it for the reasons I said earlier. We don't have anything that does it yet. I mean, you can, but we're not using metrics out of the box yet.
**Hanson** 22:47 So, I think my feeling is that,
there probably is, but it is very, very remote. My issue with making this, you know, like, not having this is people will try to use it in the cases where hotel metrics do not support it.
Because they'll be like, hey, how come I can't track the number of data used for this particular user? I can't track the number of clicks from this particular session, or whatever. And it's like, yeah, sorry, high cardinality, what can I say? And then they'll be frustrated. So, I think…
the recommendation, in my opinion, is really to set expectations about what can and can't be done. And I think at the API level, you know, we should allow it, because there is a possibility for this to be a thing, especially for, like, IoT devices that, you know, that can act as a fleet or something, you know?
**Jason Plumb** 23:43 I think you touched on something interesting there, Hanson, like, within a session. I still think session-based metrics are bullshit. Like, I don't think there's a good use case for those.
**Hanson** 23:52 Session is, for me, a coarse way of giving some time dimension. That is… so I also don't… so for… we don't use session-based metrics. We don't… we don't… session is not part of the resource.
it's… device is much more important. But I could see somebody somewhere out there wanting to do that, which is why I kind of said it. Maybe I just shouldn't add it to the,
No, no, it's…
**Jason Plumb** 24:18 It's… I think it's good to talk about that.
**Hanson** 24:20 Because the lack of dimension out… the lack of a time dimension makes… makes, like, bursts, for instance, difficult to… to account for, because of the way the periods are… are… are… are not,
Or, you know, not dynamic. Which is why having events is much more useful, because then you could kind of control that. Here's a burst of data, or whatever. So, I think there are advantages to,
to the… using events API to track certain things, but I think…
there could be a world where hotel metrics are more useful, for end-user-facing apps.
**martinkuba** 24:56 So is… Is the… is the reason to optimize…
like, the network traffic, or to make the user… make it more intuitive, the API more intuitive to the user who's…
**Santosh** 25:09 Yeah, she was in Palestinian, yeah.
**martinkuba** 25:10 The latter.
**Santosh** 25:12 I think… Jason…
point is the latter, but my point was the former. Like, where I want to optimize for, you know.
Developer Simplicity, developer who's setting up
You know, the application instrumentation.
**martinkuba** 25:33 Okay, I can see that then.
**Hanson** 25:35 like, from an API perspective, I could totally see using, you know, counting the number of, I don't know, database calls as a metric, you know, on a span or something like that. That's completely a reasonable way of using this information, the API. It's just that the data gets produced, you know.
hey, your entire fleet used, you know, 3 trillion, you know, DBE calls.
Cool.
**Santosh** 25:58 Okay, so, Hansen, I think you, you asked, what I,
prefer at this point. I think one option, and let me know what you folks think, that one option could be we could just state
That, hey, you know, as of now.
You know, we have stayed away from, you know, emitting metrics.
But, you know, but if you have a valid use case, make sure that you set up an exporter, because…
Without it, they will get dropped. Maybe just a subtle…
**Jason Plumb** 26:31 Well, that probably depends on the implementation, right? iOS, Android, web? Like… for…
For Android, I think we do set up the exporter.
Let me double check.
**Hanson** 26:49 Yeah, you set up the exporter, but the resource is not customizable, so it's going to include installation ID, so.
**Jason Plumb** 26:53 Totally.
**Hanson** 26:54 If you actually turn it on, kapow!
**Jason Plumb** 26:56 You are getting hired, yeah.
**Hanson** 26:57 I mean…
**Jason Plumb** 26:58 Yeah, maybe the caveat is, if you end up generating metrics, you will get high cardinality metrics omitted.
Martin.
**martinkuba** 27:09 I guess I'm just, like, thinking through this, and, like, what we want to advise to our users,
Like, so the option is, like.
This is just basically, like, making it more… the API more intuitive.
I guess, but we could also, like, just have…
have that documented, right? And I say, like, if you want to count something, or if you want to, like, aggregate some things from the client, this is, like, this is how you do it. I mean, we don't, like, necessarily have to, like, provide the API, but, like, I would just wonder, like, if it would make sense more, like, to focus on, like, building out maybe some conventions or some, you know.
Collector processors, or… That make it easy for users, like, to do these kind of things, so…
Instead of, like, sorting it, like, in, like, in the SDK.
I don't know.
**Hanson** 28:01 Yeah, I don't think there needs to be any API changes in the SDK. I think there needs to be some recommendation about what to do and not to do. But something like, yeah, something on the collector side that, you know, basically counts the number of events, of this name, or matches this criteria, and produces a metric, or something like that, that seems like, you know.
Very reasonable to have, if someone were to, you know, want to contribute that.
**martinkuba** 28:26 Yeah.
**Santosh** 28:33 I think that is also a route we can take.
Where you… if… if I… I… I… is… is there a collector, a processor in the collector that can…
Build metrics out of spans and events today.
**Jason Plumb** 28:47 Metrics from spans?
**Santosh** 28:52 Yes? Okay.
**Jason Plumb** 28:53 I think so. I think there is, yeah.
**Santosh** 28:56 Okay, okay. So, we could build a…
A story where we could say, hey, you know, such a…
Processor is available, and… and then we could evolve that to say…
that if you want metrics to be automatically created, here is how you define… you emit events in a certain format with this convention. So any event emitted with this convention will give you a metric of this type, but
You know, they will be, you know, representing one Client, one user.
Right? And, you know, it will… you know, you will have to further configure your processor.
To drop, you know, this, you know, dimension that
you know, results in high cardinality, but otherwise, beyond that, you don't have to do anything. You know, if you want metrics, start emitting events in this fashion.
**Hanson** 29:52 There you go.
**Jason Plumb** 29:53 Yeah, there's a span to metrics connector that replaces the old span metrics processor.
**Hanson** 30:02 Of course, if you want to use it for client data, you have to deal with a long tail of data not coming in within the first 10 minutes or whatever. So, but that's… that's…
I don't want to worry about that.
**Jason Plumb** 30:13 Yup.
**Santosh** 30:17 Alright, let's, let's… Think through this, and maybe we…
Continue two weeks from now, maybe in this same forum.
**Hanson** 30:30 I can… there's a 20% chance I'll draft up something, with what I'm talking about.
And, yeah, put it on the OpenCellGIO, and just… Yeah.
**Jason Plumb** 30:43 Cool.
**Santosh** 30:44 Okay.
**Jason Plumb** 30:46 Alright, everyone, thank you.
**Santosh** 30:47 Thanks a lot.
**martinkuba** 30:48 See you guys.
