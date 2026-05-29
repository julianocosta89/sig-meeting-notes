SIG: Java SIG
Date: 2026-05-28
Duration: 41 minutes
Zoom Recording URL: https://zoom.us/rec/share/JPBlryuj7We2bVknbbmeUGMnjEuV5X6s_4Bq-znnP8ejcBSMncq6alsF9U6EfM1b.J9yP2iVzFRyTXdlF
============================================================

## Zoom Recording Transcript

**Trask Stalnaker** 03:14 Hello, hello.
**Jack Berg** 03:24 Bye.
**Trask Stalnaker** 03:45 Where are we at?
Move… 28.
Should I erase all the names and make everybody re-add them?
**Jason Plumb** 04:00 Yes.
No.
**Trask Stalnaker** 04:04 Let's see what we've got.
Jason… That's what you get for being early, is you get your name left over.
**Jason Plumb** 04:15 Oh, but I'm moving mine down. There's no way I can be at the first. Okay.
**Trask Stalnaker** 04:50 Alright, so let's, Jason.
**Jason Plumb** 04:55 Yeah, I put this in a couple of days ago, and it just hasn't been touched. It's… I mean, it's kind of large, but it's mostly just… it's because Weaver makes a lot of code, and it's just the event names.
is what it is right now, and I want to be able to refer to those consistently, especially in Android, without having to just have my own set of semantic conventions in the repo.
**Jack Berg** 05:22 Makes sense.
**Jason Plumb** 05:23 Yeah, if this seems reasonable, then, you know… I also think there's room to maybe… Do something a little bit more helpful with, like, actual event classes?
That sort of encapsulate the name and, you know, have methods for the… required attributes and stuff, but I didn't want to do that in the first pass.
**Jack Berg** 05:44 Yeah, there's a similar story with metrics.
**Jason Plumb** 05:46 There's.
**Jack Berg** 05:46 another PR open that I linked to in the notes that's adding, generated metric names, units, and descriptions, and, you know, the… The idea that's always been in my head is, like, that's a nice start, but it'd be nice if there were helper functions to help you generate the attribute sets that were reflecting the conventions for those metric names as well.
And yeah, same thing for events, same thing for spans.
**Jason Plumb** 06:16 etc.
What did we do in that IBM MQ thing? We have some… we have a bunch of metrics in there.
I'm just not fresh in my brain.
**Trask Stalnaker** 06:33 What is this one coming from?
**Jason Plumb** 06:37 Yeah, the only stable one is what that is.
**Trask Stalnaker** 06:42 Yeah, but.
**Jason Plumb** 06:43 It sucks.
**Trask Stalnaker** 06:44 It's for span events.
**Jason Plumb** 06:48 I think it is.
**Jack Berg** 06:50 Well, it's… isn't it for the migrated version of span events, right? Which are just events now?
I want to capture an exception span event.
You do it like this.
**Trask Stalnaker** 07:05 So we're… like, for… Database, so we've got, these more specific names now.
**Jack Berg** 07:18 I see.
**Trask Stalnaker** 07:21 And I think we agreed on having exception… As sort of a fallback.
I was just surprised to see it under stable.
**Jason Plumb** 07:38 Yeah, yeah.
**Jack Berg** 07:41 Here's the link. I'll send it in the meeting notes.
**Jason Plumb** 07:44 If…
**Jack Berg** 07:44 On the data model from semantic conventions?
**Jason Plumb** 07:47 Yeah, if you want to, If you think that we should filter it and not include that, then… I think that's a valid thing to consider.
**Jack Berg** 08:01 I don't… I'm… I'm generally of the position, and I have, like, an exception to this as I'm about to say it, but that, like, in semantic conventions, Java, we should be sort of uninated about the conventions themselves, and just be opinionated about the generation logic.
And just, you know, defer to whatever semantic convention says. And the exception to that is, like, you know, we don't want to include .NET runtime attributes in Java, because they'll never serve any purpose, but… I mean… with… With that said, I think I'm generally just like, hey, defer to semantic conventions.
Because the semantic conventions will have to deal with this, like, you know, if… If they don't like people generating events with the name exception, well, there's a stable event with name exception, so…
**Jason Plumb** 08:55 Right.
**Trask Stalnaker** 08:56 Oh yeah, I'm only raising this with my SEMConf maintainer hat on.
**Jack Berg** 09:03 Oh, I see.
**Trask Stalnaker** 09:04 Sorry, yes, confusing.
And my, involvement in the, event, SIG.
Too many hats.
Exception… Do we say for…
**Jason Plumb** 09:33 There's also no rush on this, it's just like… There was an empty agenda, and I put it in a couple of days ago, and thought it might be a little bit contentious, but it sounds like it's not too bad.
**Trask Stalnaker** 09:43 No, no, and I think this is… Even though this dock is not stable.
No, stable work except for otherwise specified.
Event name… oh, event name is in development.
But we'd… It does say for… like, it is a legit… Event name, so… I see.
**Jason Plumb** 10:12 We still have the event name attribute in SumConv as well, which is deprecated, but is it just gonna stay deprecated forever, we think?
This is totally outside the scope of what this sick should be talking about, I guess, but…
**Trask Stalnaker** 10:25 Yeah, I think we'll probably… So, event name attribute. Which…
**Jason Plumb** 10:35 There's no…
**Trask Stalnaker** 10:36 drops…
**Jason Plumb** 10:37 Yeah.
**Trask Stalnaker** 10:42 I think we're gonna drop support for it in the logging bridge.
In 3-0?
And only support hotel.event.name.
**Jason Plumb** 10:51 Okay.
That's cool.
**Trask Stalnaker** 10:57 I think that's already in there behind the V3 preview flag.
**Jason Plumb** 11:23 So I linked to the way that the metrics are created.
from Weaver, in the IBM MQ stuff, if anyone cares about that, but also… I wanted to point out the… PR that I put into Android to switch over to the Kotlin semantic conventions, because Kotlin is also generating its own And I don't… I don't know that… it might be premature for us to be doing that, but, It's kind of interesting.
**Jack Berg** 11:54 So, this is… the IBM MQ stuff, I think, is an example of, deleg… Federated SEMCOMF?
Right, so those are conventions that.
**Jason Plumb** 12:06 Yeah.
**Jack Berg** 12:06 exists for IBM MQ.
And, if I understand correctly, it's like we're bridging in metrics that are recorded in a different system.
**Jason Plumb** 12:19 True.
**Jack Berg** 12:20 And so, like, when we've done that previously, for example, for example, with Kafka clients, Kafka Clients has its own internal metrics. You know, I held this position a while back, and I think it ended up, like, sort of becoming what everybody agreed with, which is, like, don't try to create conventions for, you know, systems you're just observing, but you don't control. Because if you try to codify those in semantic conventions, and then that system goes and changes what metrics it exposes, like.
you're just, like, dead in the water. You can't do anything about it, and so you sort of, like, over-promised with your, like, you know, marking a semantic invention for that as stable or something like that, and then you can no longer fulfill that promise. So, like… applied to IBM MQ would be like, hey, stabilize your transformation logic, like, how you go from, you know, the IBM, MQ Metrics, you know, whatever their names are, to open telemetry names, but don't try to create your own conventions.
And I'm not really sure… Where this stands, because… You know, there are a bunch of constants. Yeah.
**Trask Stalnaker** 13:32 We've kind of blended, like, it reminds me of, like, the JMX metrics, where we're bridging, we've got a bunch of, kind of, pre… filled transforms for bridging Tomcat JMX metrics.
But in that process, we have sort of applied semantic convention best practices to that. It's not just.
**Jack Berg** 13:54 Mike.
**Trask Stalnaker** 13:55 strict transform.
**Jason Plumb** 13:59 Yeah.
**Trask Stalnaker** 14:00 Yes.
**Jack Berg** 14:00 So not, like, not dynamic and open-ended, but, like, strict in the sense of, like, like, it's… It's like a static list of things you're trying to transform.
**Trask Stalnaker** 14:12 Yeah, and I think that's worked out well. I think the… sort of the line… Like, we definitely don't want that stuff in the semantic convention repo.
And I think we have… so I think this federation helps, it lets people still do some curation if they want to.
Yeah, so this would be, like, a great.
**Jack Berg** 14:38 gray area, right? Like, is it worth doing, like, you know, documenting the model of your static list of metrics that you're bridging?
in YAML, such that you have Weaver generate the constants, and then you reference those constants in the static transformation code. It kind of seems like… I don't know, what do you… maybe it can add you some, some… It can make it harder to make breaking changes accidentally.
I'm not… I'm not sure what other benefit you would get.
For jumping through those extra hoops.
**Trask Stalnaker** 15:16 user documentation… .
**Jack Berg** 15:21 That's true.
**Trask Stalnaker** 15:21 To be able to point people at the… I think it could play… better in sort of the broad ecosystem of semantic conventions, like, once people are like, okay, in my backend, I now can point to the SEMCOM URL… schema URLs for all of these, sort of, federated pieces, and sort of get a little bit more goodness there.
**Jack Berg** 15:50 Yeah, the schema URL bit, that's something I didn't consider, so, like… Actually, Tras, if you don't mind going on a tangent for a second, so there's a… there was an OTEP merged, I think it was Lyd Miller's OTEP, and it was about Federated SEMConf, and the idea was you have schema URLs.
that, are now a schema registry, and somewhere in that schema registry is a link to, you know, the actual The actual, like, resolve telemetry schema.
And, would that… and there's, like, there's… there's, like, semantics that are documented about, like, you know, how a schema registry server works, and, like, how it resolves, like, these links and, like, content negotiation, I think, something like that.
And I guess what I'm trying to ask is, like, could something like IBM MQ Metrics, could it, like.
could it participate in this federated SEMCOM and have, like, a schema URL or a schema registry URL that was just, like, a GitHub link? Like, a link to a, like a permalink to a, you know, a raw GitHub content?
**Jason Plumb** 17:11 It seems reasonable to me.
**Trask Stalnaker** 17:13 So… Yeah, there… there was just a little bit about the content negotiation for, I think, zipping gzip purposes, but I gotta assume that the GitHub support will… Let's see… So, the server must support GZIP compression, and, you know, this is just pretty standard HTTP.
There's no, like, dynamic logic that needs to be implemented on the server side.
**Jack Berg** 17:46 That would actually maybe… I'm not sure if that's called out in here explicitly, but maybe, like.
somewhere in, like, the motivation or the explanation, it should be like, hey, all of this is written in a way that you should be able to have, you know, a YAML file chucked into a Git repository, and, like, that is sufficient to, you know, serve as a schema registry.
Like, you don't need to have a dedicated, stood-up server that's, like, to act as your schema registry. You can just use your GitHub as the source of truth.
**Trask Stalnaker** 18:22 Yeah, I like that, because we don't… I don't think we necessarily want the contribib components needing to coordinate with, like, the OpenTelemetry website to, like, publish things over there.
Which is an option, But… for simplicity.
Yeah, new URL pattern, so this…
**Jack Berg** 18:51 Open an issue, then, in the spec, and just, like, tag Ludemila and be like, hey, are you thinking about this? This would be a nice feature.
**Trask Stalnaker** 18:58 Yeah, yeah.
Definitely.
**Jack Berg** 19:02 Or where's the… where's the best place? The spec or the Weaver repo, or…
**Trask Stalnaker** 19:18 I don't know.
**Jack Berg** 19:20 Alright, I'll just smack them.
**Trask Stalnaker** 19:22 You could ping her on Slack.
**Jack Berg** 19:28 I can always transfer the issue if I get it in the wrong place.
**Trask Stalnaker** 19:30 Yeah, right.
I mean, ultimately, like, there's… Yeah, I think with… because there's also Josh's, OTEP here.
So… They are trying to, kind of, Add more specification around… be around it.
Even though the implementation is happening in Weaver.
**Jack Berg** 20:14 Right, well, that was quite a tangent.
**Trask Stalnaker** 20:25 Log bridge names. Oh no!
**Jack Berg** 20:32 Oh, no.
**Trask Stalnaker** 20:36 This… every time I have this discussion, I have to, like, repage in so many things that I have, like, paged out and forgotten.
So much context here.
**Jack Berg** 20:50 Wait, wait, wait, maybe, maybe actually, maybe this isn't worth talking about. I think, what I was… why I added this was something that was said earlier, like.
Piqued my memory, and was like, Like, so in Java.
and Java are, like, are log bridges. Like, they bridge log for J, they bridge log back.
Into OpenTelemetry, and they map the logger name from each of those upstreams into the scope name.
And so every single time we process a log record, we say, logger provider get logger for this logger name, which was, like, you know, the logger name from LogBack or log4j.
And, you know, behind the scenes in the implementation, I've done some things to make that fast.
So, you know, what is being suggested here is, like, hey, you should also capture, like, the log bridge name as well, and we should do that in scope attributes. And Java doesn't support scope attributes yet, and there's been a couple of false start attempts at that.
But, you know, assuming we did.
it would be sort of a… like, the code path for log back and log for J appenders would change, and we wouldn't be able to just, like, say, hey, get me the log… get me the OpenTelemetry logger for this, you know, Log4J logger name. It would be… get me the OpenTelemetry logger for this log4j logger name, plus this, you know, static set of attributes.
And so the… the identity of the… the logger changes, and And I think, like, the lookup takes a little bit longer, than it did previously.
**Trask Stalnaker** 22:43 So, I have a question. Could we… because the log bridge name and log bridge version would be static for a given log bridge.
Could we move… could we essentially cache… dot logger… By log name there, in the log bridge itself.
**Jack Berg** 23:07 Yes. But you still have…
**Trask Stalnaker** 23:08 that.
**Jack Berg** 23:09 And that's what CJO and I reached. That's the conclusion we reached. But basically, every log appender you have now has to have this cache.
And… I don't know, maybe it's not that big of a deal, but That's what we would have to do to support this type of thing.
If we're the only ones writing log appenders… Maybe it just isn't that big of a deal.
Alright.
**Trask Stalnaker** 23:42 Yeah, it definitely does seem like, like, some warning text we'll need to add to the… logger provider… Forgetting a logger.
If you provide also the scope attributes in that.
**Jack Berg** 24:02 Yeah.
I think what I was worried about was the allocation, because, like, the performance optimization that I was talking about was, you know, you can, from a logger provider, you can directly get a logger Or you can create a logger builder, and, you know, build up the properties of the logger incrementally, setting the name, the version, the schema URL.
And, like, the performance optimization is that if you are just getting a logger by name, we never allocate for a logger builder.
We just directly jump to the end logger.
But, you know, I imagine if we had scope attributes, that it would be a setter on the logger builder. And so that's what I don't want every logger appender to have to do, is to, for every log record bridged, to be… have to, like.
allocate for the log… for the logger builder, and then the log record builder, and then the, like, when you call emit, the, you know, the n log record itself.
**Trask Stalnaker** 25:15 Come on, GitHub!
Let's go.
Hmm.
So the… yeah, I had missed that piece, I'm still on the internet, though, I can see you all moving.
**Jack Berg** 25:36 Yeah, yeah, we can hear you.
That's not good, by the way.
Just the IP address. DNS isn't working, oh no.
**Jason Plumb** 25:48 VPN? Oh.
**Trask Stalnaker** 25:50 There we go.
**Jack Berg** 25:50 Alright.
**Trask Stalnaker** 25:53 Blog, it's provider, where the…
**Jack Berg** 25:58 That's right.
That's right.
**Trask Stalnaker** 26:00 Okay…
**Jack Berg** 26:02 So there's a short circuit GET, where if you just call it what.
**Trask Stalnaker** 26:05 I see. So, all of a sudden, you have to go from this to this.
**Jack Berg** 26:12 That's right.
**Trask Stalnaker** 26:12 And this starts allocating. Okay. Yeah…
**Jack Berg** 26:18 And again, like you said, we can cache these loggers in the appenders, and make it so that it doesn't really hurt you that bad, that You have to have this extra allocation, you're only doing it once per distinct logger, but… Stinks if you're writing extra or other logger appenders.
It's just bad ergonomics.
Anyways…
**Trask Stalnaker** 26:46 At least it doesn't leak into users.
Who will… If they're using that directly, should cache that in a same way you would cache any logger.
Pranav.
Ayy.
**Pranav Sharma** 27:05 Hey, hey folks, saw an empty agenda, and so I thought I'd ask a question. I don't have a lot of experience with OpenTelemetry specification or writing specification in general, but I was wondering if I need, something, like, this is a proposed issue, and I was wondering.
if I wanted to do this in Java, would I first need to go through and get it added to the spec, or can I just… to this in the Java, like adding an option to the view to append a prefix to metric names.
**Jack Berg** 27:41 Yeah, so, generally the hotel Java is… the scope of the project and all the features is restricted by the spec. With only a few exceptions, we just… we say that, like, you know, the APIs and everything, there has to be a corresponding section in the spec that describes it.
And, you know, we build our APIs to conform to that. The exceptions are things like, if there's things that are, like.
you know, syntactic sugar or idiomatic in Java, where, like, our implementation just would be impractical without… without that. And so, you know, maybe we'll add that despite, there being no explicit text in the spec. But as a general rule, it's in the spec first.
But what… what are you after here? Because, like, when I read this issue, you know, it's from 2020. It's from before there was a Stable Metrics API. It's really old, and, I just, like… I wonder if the prefix, as, like, a concept, is sort of… replaced by, by scopes? Like, you know, was prefix an attempt to, like, namespace metrics by some distinct unit of code, such that, like, two different HTTP client libraries, you know, you can differentiate them, in some way? What are you after here?
**Pranav Sharma** 28:59 So, yeah, this is mostly, like, to help us with the migration stuff, like, migrating to the OTLP exporters. Like, Google Cloud Monitoring, uses, like, the concept of, monitored resources, which are… Defined… which were defined by the prefix in the metric name.
So if we are trying to migrate the users over to the OTLP exporters, we'd ideally want to prevent breaking their dashboards and alerts in the meantime, because the prefix becomes part of the metric name. So, because the OTLP does not specify or allow you to specify a prefix, a metric called HTTP, Request Latency, in Google Cloud would have a prefix attached to it, and so the met… automatically attached to it, and so the entire metric name would become something like… workload.googleapis.com slash HTTP request latency. So, once they move to, OTLP exporters, that prefix will be removed, and so their existing dashboards and alerts tooling would break.
And so I thought that prefix was a… this… this would… adding a prefix in the views would, be an easy way to prevent breaking those users.
**Jack Berg** 30:18 So, is a… is the prefix sort of constant for all metrics emitted by an application?
Is it, like, is it… okay, it's something… it's sort of akin to, like, some sort of resource attribute, where.
**Pranav Sharma** 30:31 Yeah, yeah, yeah, yeah.
**Jack Berg** 30:34 Okay, so… Hat… Getting… getting the spec people to, to… To add a new feature, like a prefix to a view, it's like… it's, it's, it's… It's… it's a long process. You know, you have to… you have to get people to agree that we… we should do this, and then in concept, and then open a PR and have a backing prototype to show how that works, and then it gets merged and it's in development until, you know, there's enough Implementations of that.
that people feel comfortable enough with the concept that they want to promote it from development to stable. So, it's… it takes a while, and, like, by all means, go for it if you think that that's the best solution. But just as I'm listening to you talk, there might be, like, another solution.
Which would be, you could have a… you could have an exporter wrapper. So you have your OTLP metrics exporter, and you could have a wrapper that, you know, wraps the OTLP metric exporter, and before it calls that, it could rewrite the metric names to include this prefix on all of them.
**Pranav Sharma** 31:49 Right, so this wrapper would be a specific exporter artifact that we publish, and we ask people to use it while they're migrating.
**Jack Berg** 31:58 Something like that, yeah.
**Pranav Sharma** 32:00 Okay, yeah, just wanted to hear your thoughts on it, yeah.
I'll look into it. Thank you.
**Trask Stalnaker** 32:09 Yeah, I think the hardest part about getting something like this into the spec is getting multiple… People from multiple different, you know, companies, organizations who are facing this problem and really need it.
**Pranav Sharma** 32:26 Yeah. I just got excited because I was…
**Trask Stalnaker** 32:29 If there was an issue, yeah.
**Pranav Sharma** 32:31 And there was an issue about it, so, you know.
It's okay.
**Trask Stalnaker** 32:34 We're not very good at closing out old… stale issues.
**Jack Berg** 32:40 Is the collector in the pipeline of the services that you're talking about? Is that, like, guaranteed to be present?
**Pranav Sharma** 32:45 I mean, not all times, but we're aware that if a user is already using a collector, this becomes much more easy with the OTTL and transform processors, so, yeah.
**Jack Berg** 32:55 That's all I was gonna say, yeah, so…
**Jason Plumb** 32:58 Bogg didn't even ask that, like, in that issue, like, 5 years ago or something.
So I used one of these recently. These are… these have been around for a minute. I think I contributed them, like, 3 years ago, I can't believe that.
**Jack Berg** 33:14 Oh my gosh.
**Jason Plumb** 33:15 I know.
They've been sitting in the incubator for a while. I don't know, has anybody else ever touched these? Does anyone care? I just… I think the span processor is great, but, like, so many times you only want to do something on head, and you don't care about tail, and so having the on start is kind of a nice little shorthand.
**Jack Berg** 33:35 and start… So… on… I thought that the main thing that these added… like, so you added some sugar on this, but the…
**Jason Plumb** 33:44 That's all it is.
**Jack Berg** 33:45 But there's also this concept, which is, like, that allows you to mutate the span before it ends. It's, like, on-ending. Where does that fit into?
**Jason Plumb** 33:57 Yeah, that's somewhere else, that's a different… that's a different thing. That's the extended span processor.
**Jack Berg** 34:03 Okay.
**Jason Plumb** 34:04 It's not related to these two.
**Jack Berg** 34:06 And that's not in the incubator? Is that, like, in the.
**Jason Plumb** 34:08 I don't know where that is, actually.
**Jack Berg** 34:10 I think it has to be in an internal package, actually, within the existing, you know.
**Jason Plumb** 34:15 Yeah.
**Jack Berg** 34:21 I have not used these, but I don't write a lot of custom span processors.
**Jason Plumb** 34:26 Okay.
Well, I guess, you know, process question then is, what does it take for these to move out of incubating?
Like, if I wanted… if I wanted to assert that I wanted to move them out of incubating, which I honestly don't care that much, but, like, I think it would be nice. Like, if I wanted to, what's the process to do that?
**Jack Berg** 34:48 Wait, wait, wait, wait, wait, wait, wait. I don't think this necessarily needs to be spec'd, because this is, if I understand it right, it's just sugar.
**Jason Plumb** 34:55 It is, yeah.
**Jack Berg** 34:57 And the sugar is, like, what… So, onEnd is a… is a… is a functional interface.
**Jason Plumb** 35:05 Yeah, it's at the very bottom.
**Jack Berg** 35:07 Oh, it's defined in part… okay, yeah, so you have a functional interface that… okay, I get it.
Yeah, I mean, I don't hate this thing.
So I, I, like, yeah, it adds a little sugar, it's not super heavyweight, propose, propose, bringing it to the, the core, or promoting it out of the incubator, and, like, I guess we'll see, we'll see what it looks like.
**Jason Plumb** 35:41 Do you want that proposal to be a PR or an issue?
**Jack Berg** 35:44 I think a PR is fine.
**Jason Plumb** 35:46 Okay.
**Jack Berg** 35:46 I think we're such a busy repo these days that we need the formality of different distinguished.
**Jason Plumb** 35:53 I love being.
**Jack Berg** 35:54 issues in VRs.
**Jason Plumb** 35:55 Okay, cool.
Thank you so much.
**Jack Berg** 36:01 And, like, I guess, like.
We'll just see what people say, and, like, one way or the other, we'll either, like, promote it, or… Or kill it. Like, we should reach a conclusion with it, you know?
**Jason Plumb** 36:13 Yeah, okay, that's fair.
**Trask Stalnaker** 36:20 Since… Joo-do.
just a, This is deleting a bunch of code. I guess, really, I should get the code owners. Oh, is Peter here? Peter's is here! Hey, Peter!
If you have.
**Peter Findeisen** 36:48 Yeah.
**Trask Stalnaker** 36:49 time to look at this, let's hopefully… oh, there's some co-pilot, comments.
**Jack Berg** 36:58 Wait, so, what's the gist of this? You're… are you fully deleting it, or are you replacing the internals with stuff that's, already inside the core?
**Trask Stalnaker** 37:11 I'm deleting, so there were these, kind of, two different implementations, already.
And so, I'm converging them into one, basically dropping the old, And then I'm rewriting… basically removing the things that have been moved into Core, and updating the other pieces to use Core.
**Jack Berg** 37:39 And is there anything that can completely go away? Or is it, like, you know, these are still useful samplers to keep around?
In perpetuity, in, like, a contrib context.
**Trask Stalnaker** 37:53 Yeah, there's… I mean, there's some things that are gone completely, because they were moved into Core.
And there's some things that have… basically, I just… if there was any… I didn't… Yeah, if there was additional features that didn't get moved to Core, I left those and updated them to use the core foundation Okay. But I think… Yeah, probably… well, Peter probably knows better in terms of when spec would land for those other pieces.
**Peter Findeisen** 38:32 Yeah, the old… the old pieces were, I think, deprecated about 2 years ago.
We were keeping them around just for… For people who might depend on them.
But I think it's time to retire them entirely.
I'll be happy to have a closer look at this.
**Trask Stalnaker** 38:52 Okay. Awesome.
Yeah, happy to delete more stuff.
**Jack Berg** 39:13 Alright.
Any other topics?
Does that take us to the end of the notes?
**Jason Plumb** 39:25 Yep.
**Jack Berg** 39:27 I guess there's one tiny thing, so, I'm gonna merge the PR that I have open in Core that's about, removing shared internal code references from the Zipkin exporter, and if you remember, there's… there's one change to the public API surface area, this, like, it's like an instrumentation suppression utils thing that is, like, a coordination point between OpenTelemetry Java Core and instrumentation so that the, the exporters themselves are not instrumented. So, yeah, new… implementation, public API surface area, and we'll need a change in the next Java… before the next Java instrumentation release.
**Trask Stalnaker** 40:24 Cool!
**Jack Berg** 40:27 Alright, y'all.
**Trask Stalnaker** 40:27 Let's call it.
**Jack Berg** 40:31 Till next.
**Jason Plumb** 40:31 I'll see you tomorrow, right?
**Trask Stalnaker** 40:34 Damn.
**Jason Plumb** 40:35 Alright.
**Trask Stalnaker** 40:36 It's looking rainy.
**Jason Plumb** 40:39 Of course. I haven't even looked.
**Jack Berg** 40:43 Sounds like a safe assumption.
**Jason Plumb** 40:45 It's Portland.
**Trask Stalnaker** 40:46 Today's beautiful, today's gorgeous. Yeah. I don't know why tomorrow is… .
**Jason Plumb** 40:54 It's gonna be great. It's gonna be warm. Yeah.
Alright, take it easy. Bye.
