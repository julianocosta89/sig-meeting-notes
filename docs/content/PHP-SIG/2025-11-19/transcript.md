SIG: PHP SIG
Date: 2025-11-19
Duration: 48 minutes
============================================================

## Zoom Recording Transcript

**Chris Lightfoot-Wild** 01:44 Hey, Bob.
**Bob Strecansky** 01:46 Chris, how are you?
**Chris Lightfoot-Wild** 01:48 I'm all good, I'm sorry, how are you?
**Bob Strecansky** 01:51 Potter.
Realizing that you are not preparing for Thanksgiving, I am.
**Chris Lightfoot-Wild** 02:00 No, I wish we were, though, because I live Turkey.
**Bob Strecansky** 02:04 Really?
**Chris Lightfoot-Wild** 02:05 Yeah.
**Bob Strecansky** 02:07 We always joke that turkey's a shit bird. Like, it doesn't taste good by itself, you have to, like, doctor it up with tons of fats and other good stuff to make it taste good.
**Chris Lightfoot-Wild** 02:17 Yeah, I think I prefer it's chicken, but I mean, I… Yeah, I don't know.
**Bob Strecansky** 02:22 It's a bold statement, my man.
Very bold. I am going to smoke a turkey, which is always very fun.
**Chris Lightfoot-Wild** 02:31 Is that… You gonna shoot it, or.
**Bob Strecansky** 02:34 Oh… I am… I am not a hunter. I will not be shooting my turkey. I will be going to the grocery store and buying it like every other American, but…
**Chris Lightfoot-Wild** 02:43 I wasn't sure what angle you were going for with smoking it.
**Bob Strecansky** 02:47 Oh, no.
No, no, the, I have a grill that is… that uses, like, these wood pellets, it's called a smoker.
Yeah.
**Chris Lightfoot-Wild** 02:59 Is it one of those… have you got one of those egg things as well?
**Bob Strecansky** 03:02 I had one, and I replaced it for this. I'll show you what I have now.
Boop, boop, boop, boop.
**Chris Lightfoot-Wild** 03:09 be so good.
**Bob Strecansky** 03:10 Hmm.
**Sergey** 03:10 Hi, guys.
**Bob Strecansky** 03:12 Blue…
**Chris Lightfoot-Wild** 03:13 Talking about Turkey's…
**Sergey** 03:14 How was the conference, was it worth a while?
**Bob Strecansky** 03:19 conference was really good. It was, it was not worthwhile, I would say. Well, I guess I should… that's pretty hasty. I guess I should say, The, the, like, the actual conference talks were… lackluster, like… and they did that classic New Age conference baloney where they, like, well, interweave a sponsored talk with a regular talk, with a sponsored talk, so it's like, oh, cool, I don't want to hear about your startup or your thing that I'm most likely never going to buy, but…
**Sergey** 03:54 But there were probably multiple tracks, right? You can choose which.
**Bob Strecansky** 03:58 There are. There were, yeah. So there were multiple tracks, but a lot of the tracks were, It's… they were, how do I say that? Like, they definitely had, like, specific targeted tracks, right? Like, there was an observability track, and there was, you know, this, that, and the next thing.
**Sergey** 04:15 I know that our guys also presented. Did you… did you have the chance to see the Elastic presentation?
**Bob Strecansky** 04:21 I did not… I should have thought… I did meet somebody from Elastic. Why am I… of course, I'm blanking on his name right now. I met somebody who works… who is also a, I forget what… he might be Rust, or another… he's, like, another maintainer for a different… OpenTelemetry sig. But they gave us these… these, baseball jerseys with Maintainer on the back, and they're kind of funny.
**Chris Lightfoot-Wild** 04:48 Oh, nice.
**Sergey** 04:48 Nice.
**Bob Strecansky** 04:49 This is what I'm… this is the kind of girl that I'm talking about, Chris.
**Chris Lightfoot-Wild** 04:56 Barbecue.
**Bob Strecansky** 04:57 Yeah, it's like… it's similar to a barbecue, but… so, it uses… These are, like, wood pellets, they're, like, about… I don't know, this big. And then that feeds into an auger, and it makes smoke, and that's how you cook the food, and it's… Really cool. Makes a lot of really tasty food… some really tasty food.
**Sergey** 05:21 What is that R? Is it… is it…
**Bob Strecansky** 05:23 I don't… I don'.
**Sergey** 05:24 South Africa?
**Bob Strecansky** 05:26 I don't know, I just clicked on… I just clicked on it through…
**Chris Lightfoot-Wild** 05:29 Incident.
**Bob Strecansky** 05:29 Yeah, I think it might have detected me as… why is it detecting me as…
**Sergey** 05:33 Yeah, R is Rand, yeah.
**Bob Strecansky** 05:35 Yeah, I think… I guess I'm gonna be buying it in red now. No, we use American dollars here.
**Sergey** 05:45 Maybe using a VPN or something?
**Bob Strecansky** 05:47 No, I'm just on my work computer. I think I didn't allow location targeting, so maybe I just, like, went… like, that's so deep. That doesn't make any sense. I don't know. Computers, man. Who knows?
Alright, so the three of us are here, and I'm gonna assume that's about it. I know Sean mentioned that he wanted to come, but maybe he had a conflict. He was asking some questions about vlogging, so I figured we could talk through some of that today.
And… those are all the, like, Standard… where did…
**Chris Lightfoot-Wild** 06:20 I think, actually, and that's maybe up to it.
**Bob Strecansky** 06:23 Say it again?
**Chris Lightfoot-Wild** 06:25 If it's not too late, I might whack something on the agenda topic as well.
**Bob Strecansky** 06:29 You can absolutely work something in the agenda.
**Sergey** 06:33 We were wide open.
**Chris Lightfoot-Wild** 06:34 No, if…
**Bob Strecansky** 06:34 for, like.
**Chris Lightfoot-Wild** 06:35 Seeing the word login, it reminded me.
**Bob Strecansky** 06:37 Yeah.
Goodbye.
I will be, missing this meeting next week for the holiday, just so you'll.
**Sergey** 06:48 By the way, login is also covered by the same SDK, or is it a separate thing that covers the logs?
**Bob Strecansky** 06:55 That's a… that's a really great question, Sergei. So, while we're waiting for everybody, so y'all… I mean, everybody is aware that OpenTelemetry is supposed to be the all-encompassing thing for… for telemetry, you know.
tracing, metrics, logs, now events is another… that's another signal that they're talking about, and just, like, that is.
**Sergey** 07:19 Officially, only 3. The Venza, maybe.
**Bob Strecansky** 07:22 Events are… they're in the process of, like… they're… events are definitely going to be a thing, but they, they're still, like…
**Sergey** 07:30 The spec is official for the first three, right? We already have a spec for those, right?
**Bob Strecansky** 07:34 with a pretty large asterisk, and that's what we're about to talk about. So, tracing and metrics, like.
done and dusted, settled in the sand, like, that they're going to become stable relatively soon. A big point of contention in the maintainer's meeting this week, and I think it was just like a… essentially, it was like an exacerbation of… like, I don't know, the last 2 years, probably? It's… there is this… there's this, like, duality of what people believe logs should look like in OpenTelemetry amongst the maintainers. Oh, here's… here's Sean. I can wait… I will wait, because I know he wants to hear this discussion, too.
Hey, Sean!
**Sergey** 08:18 Aye.
**Chris Lightfoot-Wild** 08:20 initial.
**Bob Strecansky** 08:23 Hi, Sean.
**Shawn Maddock** 08:24 Hey! Can you hear me?
**Bob Strecansky** 08:25 Hey, you showed up just in time, because we were talking about, about logs, or the… the, the current state of logs. I was telling Sergey and… I was telling Sergey and Chris, in the maintainer's meeting yesterday, there was, like, there was a big discussion about this. I think this is some… this is something that we have… that the maintainers and the TC and the G… more of the TC and the GC have discussed at length, and I think it's becoming more and more… prevalent as OpenTelemetry proliferates the observability environment. There are currently… we currently have tracing, metrics, logs, and soon-to-be profiling and events, all as the signals that are available in OpenTelemetry.
logs, or sorry, traces and metrics are like, you know, I think I used the phrase done and dusted with Chris and Sergey, like, there's not a lot of contention on those, there's a lot of spec… there's a lot of… a perfectly written spec for them, so on and so forth. There is a lot of contention in… the log, like, in the logs part of the specification right now. Then there's two trains of thought that are currently active.
some maintainers and some end users feel as if there should be, like, a very, very explicit log API and SDK for OpenTelemetry, and that should be, like.
When you instrument OpenTelemetry, and also.
Spoiler, this is my opinion, too. When you instrument OpenTelemetry.
you should, like, when you instrument traces and metrics, you use the OpenTelemetry API and SDK to implement these and use them in your application.
the current logging spec is, like, yeah, use whatever you want for logging, and then we'll, like, integrate it in via OpenTelemetry via some APIs and SDKs, but we don't have, like, a one-to-one mapping of logging for OpenTelemetry.
And the two trains of thought are… For the people that think that you should use a different logging package, and then, like, essentially the maintainer should tell you which one to use, and so… whatever, is like… If that's the case, then everybody can use their own opinionated logger, and it can just be propagated through OpenTelemetry, through events, or through the, through, like, the standard ad exporter, or whatever.
And then other people are of the mentality that OpenTelemetry should have, like, a very explicit way to implement logs, quote-unquote, from scratch, right? Like, if you instrument the API and the SDK around your logging infrastructure, there should be a common pattern, and that should be up to the language maintainers.
the Java, the .NET, the Go, the Python, the Rust, all of the maintainers chimed in on this in the call yesterday.
And pretty much, like, everybody had different opinions about how this should be handled, because some languages have, like, unbelievable, like.
we use monologue, period. Like, nobody… nobody in their right mind uses anything else in the PHP ecosystem. But that's not necessarily true in some of these other ecosystems, like… Java has log for J, and log for J2, and S4J2 and a couple others. Go has log and S-Log.
NET has some, you know, weird Microsoft thing that I don't care to understand.
Like, the long and the short of it is… I think that this is still, like… still up for debate a little bit, and I think that there are… there are a couple things that… there's, like, a couple open OTEPs discussing this, so if you're more… if you're interested more in learning about it.
then that's, then that's a really great place to do it. Right now, we just use… we just use monologue, like, there's… ours is like a wraparound monologue, so that should be fine for the time being until something else changes, but that's just the current state of logging in OpenClaunch.
**Sergey** 12:31 But wouldn't you say that it's purely theoretical discussion? Like, does it change anything? The fact that, even if we introduce a dedicated API for login.
still, most of the people would want us to integrate with existing libraries that they use, right? So this switch might take… I would say, for PHP, it might even less chance, because if model is so prevalent, why would people suddenly discover something else and change to it?
**Bob Strecansky** 12:54 I think… so, I agree with you, Sergey, with the… the small caveat of… I think that a lot of end users start using OpenTelemetry and expect it to be a one-stop shop, because that's sort of what it's been touted as, right? Like.
you can use OpenTelemetry and get all of your telemetry. And, you know, we know that as tracing and metrics forward, but I think a lot of people are like, I just want one library, and I want to do tracing, metrics, logging, profiling, event, like… I think that was the, like, I think that was the original… the original mindset, you know, maybe 6 years ago for OpenTelemetry was, it's a one-stop shop for everything, but I think the opportunity is that There is so much… like, logging is so much more opinionated than tracing ever was, because tracing wasn't really prevalent in the observability ecosystem. I mean, it was for… like, it was disjointed a little bit, but I feel like OpenTelemetry brought a lot of… tracing together, for lack of… distributed tracing together, for lack of a better word. Like, it became a lot more consistent and prevalent. I mean, OpenCensus and OpenTracing also did that a little bit, but I feel like the convergence into OpenTelemetry really helped with that, too.
**Sergey** 14:16 Right, but it sounds like it's… those are not contradicting approaches. Essentially.
we know that we will have to integrate with existing libraries, right? Because the switch, even if we… so it becomes then, okay, that means that we need to implement integration, and… the question is, how much of a priority to implement a dedicated API that will achieve this goal of being one-stop shop, right? Okay, so you add as a potential additional thing, but it should not… but it's not enough just to have it, so we know that integrating existing libraries has higher priority, because existing applications already use monologue or whatever.
**Bob Strecansky** 14:50 Yeah, I 100% agree with you on that. I mean, I can see both sides of the coin, right? I am… A brand new developer, I'm excited to learn about observability. I install OpenTelemetry, I get, you know, I can auto-instrument my metrics, I can auto-instrument my traces.
Oh, shoot, what do I do for logs now? Let me go see… oh, you have to implement this monologue thing, and then, like, have this abstraction layer on top. I can see… I can see how it would be confusing for people that are not… it's confusing for people who are in the ecosystem. It's even more confusing for people who are not.
**Sergey** 15:25 Yeah, because it's a special case, right? Because you kind of, like, encounter it, because all the rest that we instrument automatically, those are libraries that have other purpose, and we instrument them for the purpose of telemetry. But monologue is itself, its purpose is telemetry, so it's kind of like then we have competing purposes here. So we're using it just to instrument, it doesn't make much of a sense. But I assume… by the way, when you say starting developer, like, starting developers, first of all, Tracy, they will probably take it for granted, like, it's likely they will even involve them, same as… in kind of, like, understanding how tracing works, other than seeing the traces, because they will just see that, okay, I have database traces.
I have my framework being traced, like Laravel, so it's all good. Why would they even need to… they will just install it as an additional thing? It just does the job for them. They will not invoke the API directly, no?
**Bob Strecansky** 16:13 Right, and I think that that's what… Some… that's the vision some people have with logging in OpenTelemetry, too.
Like, it just…
**Sergey** 16:21 Login, you have to invoke it explicitly, unless you use monologue, and then you get it for free as well, right?
**Bob Strecansky** 16:28 I'm not saying… I'm not s-.
**Sergey** 16:29 What I'm saying is that you're trying to compete with the whole thing that already has, you know, like, the whole ecosystem built around it. Like, Monologue has all these extensions, right?
it has all these tutorials, and you can ask questions, and all the information available. You're essentially coming in and saying, okay, I want to replace you, so you'll have to, you know, do the same Do the same work to bring it up to that level.
**Bob Strecansky** 16:51 Yeah, I agree with you. I'm just trying to explicitly state the intended goals. I'm not saying it's right or wrong, I'm just saying that there… this has been a discussion point in the maintainer's meeting, and I think that it will continue to have friction, and I hope they come up with a resolution for it sooner rather than later.
**Sergey** 17:07 But that's what I have to understand. Why is the required resolution? Like, why not just to agree that, okay, let's start with integration-resistant libraries? That sounds like a must and high priority. And then, when we get to the situation when we want to have a dedicated API, then fine, let's add it, but Why should it stop the first? Like, doesn't everybody agree that.
**Bob Strecansky** 17:26 Benji.
**Sergey** 17:26 Is it great with existing libraries?
**Bob Strecansky** 17:28 It shouldn't, and I agree with you, I think, like, for operational… for operational momentum, we should do that, right? Like, log for… like, maintainers need to pick an opinionated… logging library and build in, like, the compatibility layer with their API and SDK, and if they need to build in multiple, then, I mean, that's what they have to do for their ecosystem. I think that that's the right thing to do. Like.
Work, like, use what we… use what we got already, and then when that's good enough, then we can start tweaking.
**Sergey** 18:04 For me to better understand, are you saying that there is this opinion that it is a wasted effort, and people should not do this? Like, is there, like, a competing opinion that let's not do that? Because it sounds like it's a non-starter, like…
**Bob Strecansky** 18:17 Yeah, I think, I think some maintainers are of the opinion, like, hey, yeah, that's cool, like, we could implement another logging… like, we could use another, like, we could use another logging library as an abstraction, but I'd really like to focus on implementing our own.
**Sergey** 18:36 Well, maybe I misunderstand, we don't need additional abstraction layer, we will just instrument the existing libraries, like, we don't… I mean, this ability to be exposed as a library to views directly, that can be treated as a… by the way, I don't know what is even the purpose, like, what is the end goal?
Is the goal to also send the logs to the collector, to the… because there are different understandings what is the goal of logging? Because, you know, for correlation, sometimes, for example, what we did in Classic Elastic, because we switched to hotel.
We constituted, like, for us, login was to actually integrate, kind of, like, inject span ID and trace ID into login, so then later it can be correlated by some means to the, to the tracing.
So the question is, what is login supposed to cover, even? Like, do we want to ship the login? Is that the main purpose? To ship the login to the same destination and structure it, essentially make it structured?
**Bob Strecansky** 19:28 I think that… I think that that's, like, the long-term intent is, again, to have, like, a consistent story across… across open telemetry, right? Like, you install the collector, you instrument your library, and you get all the telemetry you need for your particular project. And I think that the path to that intended outcome Is still, like, surprisingly, a half a decade after the project starts, still up for debate.
**Sergey** 19:58 I guess it's better to define the use cases, like, what is the use case? Because then when people ask, okay, so I have API for tracing, I have API for login. How do I select which one to use? Like, even if we implement API?
So, how people do even understand which one, like, why… why do login not create a span? Or what's the difference between them?
**Bob Strecansky** 20:18 Yeah, and then you can get even more, you could get even more sticky with it too, right? Like, how does… how do the metrics implement with the traces implement, with the logging implement, with the profiling implement, with the events implement? You know, like, there's, like, this multi-layer cake that could eventually take form, and I think, like, that would be, like, essentially, I feel like that's what a lot of observability providers try.
**Sergey** 20:42 In this metrics, you can say that it's, like, aggregation, like, it's easy to understand the distinction between tracing and metrics, right? You say, okay, metrics aggregation, tracing is for each individual execution. All as you can see the difference, but logging starts to compete with tracing.
**Bob Strecansky** 20:56 Yeah.
**Sergey** 20:57 But, let's hear maybe from Sean. Sean, what… you had maybe a concrete understanding of the questions?
Yo, we… you thought something to discuss here?
**Shawn Maddock** 21:08 This one's a lot more theoretical than I was…
**Sergey** 21:13 That's why…
**Shawn Maddock** 21:13 Finger intent.
**Sergey** 21:14 I wanted you to bring it down to Earth.
**Shawn Maddock** 21:16 Yeah, so, I mean, currently, the option is to use monologue.
And so, as we've been instrumenting it, I noticed that the PHP library currently, Takes the context and extra… attributes, which monologue and, uses, like, containers for multiple attributes, and chips them in OTel as a single attribute, like JSON encoded.
So, when we're using an observability platform, we're using Cygnos right now, but same in Loki, or… Any of the others, like, we have to do post-processing At the observability platform level, to break apart that context and extras.
Attribute into its individual attributes, and from reading the spec on… log attributes, that doesn't seem to be the intention of OpenTelemetry, so… My question was, if… we're not to the point of implementing our own logger. Can we update the monologue contribute library? To… Either change the behavior, or have a flag for alternate behavior, where… Instead of… Shipping that, context and extra… component, like, as that JSON encoded thing, it actually breaks it apart into individual attributes, on each log.
**Sergey** 22:57 Should they do it recursively, or are you expecting to do it on the first level?
**Shawn Maddock** 23:03 I would think on the first level, like, Since that's how…
**Sergey** 23:07 monologue to set, Kind of, like, deeper depth objects as a… to set another map as a… as an attribute value?
**Shawn Maddock** 23:19 I mean, monologue seems to treat the… the context as… like, first descendants of context as attributes. And so…
**Sergey** 23:33 By monologue, you mean monologue instrumentation and country?
**Shawn Maddock** 23:37 No, like, monologue.
itself.
**Bob Strecansky** 23:41 Could you.
**Shawn Maddock** 23:42 Or PSR3. I should say PSR3, not long-log.
**Bob Strecansky** 23:46 I don't see a reason why we couldn't, like, separate the attributes in the library, but have you considered using, like, one of the transform processors on the collector? I think those are pretty powerful and could probably… Help you with, like, batch processing of these logs and performing your transformation After they're sent to the collector, rather than…
**Shawn Maddock** 24:08 And that was my… my initial go-to, and we're already doing that with… logs from non-PHP sources, non-OTEL sources that…
**Bob Strecansky** 24:20 God.
**Shawn Maddock** 24:21 were transforming. But then… I started wondering why it was even like this, why that was even necessary.
**Bob Strecansky** 24:30 I'm assuming that was just, like, how it was written at the time, based on what the specs said. I don't… yeah, I don't see a reason why we couldn't implement a flag there for you to be able to change those attributes in a way that you want to consume them, but… I think we gotta be weary of what the spec says, and of what others might want, too. So yeah, if you wanna, come up with a plan for that, that's totally fine.
**Shawn Maddock** 24:54 Okay. Like, to restate it, the context… Array.
**Chris Lightfoot-Wild** 25:01 is a PSR3…
**Shawn Maddock** 25:04 function or attribute, feature. Whereas attributes are the OTEL.
equivalent, and so… Opentelemetry, like, has a bunch of default attributes that It's writing.
But also has room for user… user-defined attributes, and so… Yeah, I don't want to break any existing implementations, but I feel like… At least my understanding of the spec, is that would be more true to it, to have… To… to break out the… the context.
This R3 allows you to set the values of those context keys.
**Sergey** 25:50 Values themselves can be objects, right? It doesn't require you to have primitives as values.
**Shawn Maddock** 25:57 Correct.
**Sergey** 25:58 But then you will not be able to set it as attribute for… for hotel. OTEL requires those to be primitives, right? Those will go to the… A protobuf protocol.
Does it allow certain objects as, as attribute values allows that?
**Shawn Maddock** 26:16 Maybe that's…
**Sergey** 26:20 Because then, essentially you want to flatten the map, but the question is.
Do you want to flatten it recursively, or… Or just the first level?
**Shawn Maddock** 26:32 Yeah, the… That's a good point. I… I still think only the first level, But, yeah, there would need to be some sort of… string of things.
**Sergey** 26:42 Most likely, it probably covers 99% of cases, probably. Very rarely people will put another map as a value.
But technically, I see that you can set, for example, object as such an exception as there, right? Exception is definitely not a primitive value, so it will have it in its own, kind of, like, can be split in its own map.
Quite deep.
Stock Trace.
I don't know what exception includes there.
But.
**Chris Lightfoot-Wild** 27:07 If it helps on the same sort of brainwave as Sean there, because I've seen it in signals where it's JSON encoded, and then you can't filter by that, because it's just, like, a blob, where obviously it's not… It requires some pre-processing.
So…
**Sergey** 27:26 But it sounds like there are two different things. So if what Bob says is, if the spec changed since the implementation, and the right way to split those attributes into multiple instead of JSON code in the first level.
then maybe it will solve 99%, right? Those cases that will still have some attributes that themselves are objects. Okay, then.
Somebody will have to deal with that. I don't know what Spec says about that.
Like, does it even allow? Like, I guess they need to be primitive, so I guess they will be JSON coded.
**Shawn Maddock** 28:00 Peacockers.
**Chris Lightfoot-Wild** 28:03 What was that, sorry?
**Shawn Maddock** 28:05 What are these, pull requests you got, these PSR3?
**Chris Lightfoot-Wild** 28:10 Oh, sorry, I mean, that's… yeah, are you done on that first point, then? Sorry, on the… I can talk about that if, It's got sort of reminded me that it's a very log-orientated discussion today. This PSR3 one, then. So the first link in there was the initial attempt So, to try and detect if you're running under Composer or not.
And then, if you are… disable the autoloading mechanism, of the SDK.
So… you don't run into the PSR3 fatal errors?
It very much depends on the… your application, vendor dependencies.
But then, I added an alternative, and I just wanted to sort of float that idea, I guess.
Which was basically some backwards compatibility layer in there, So there's that… at the root level, there's this compact.php, where it is figuring out whether or not it should try and shoehorn in the, backwards compatible classes there. To beat the autoloader to… be compatible with Composer.
**Bob Strecansky** 29:29 I feel like this is… I feel like this is something that Tobias would have a strong opinion on.
**Chris Lightfoot-Wild** 29:36 Yeah, but not social.
**Bob Strecansky** 29:37 Face them. At face value.
**Sergey** 29:39 But it can happen with many other packages, not just PSR3, right? For example, any PSR that might depend, like PSR message, GTP client, whatever.
**Chris Lightfoot-Wild** 29:49 Yeah, I mean, if this made sense, I guess you could just expand on this compact… well, compatibility layer, but if this is something we don't want to do, then that equally is fine, but… Just throw it in as an approach.
Maybe to consider or discuss. Because I know we've got some backwards compatibility stuff already in the SDK.
**Sergey** 30:11 But they're not 100% following you how you will prevent it. So, essentially, you will only control which PSR you use directly as dependency by SDK code. But if SDK itself brings in surpass, like another transitive dependency that itself depends directly on PSR, then it will bring its own version. You will not be able to prevent it. Like, compat layer will not be invoked for that dependency, right?
**Chris Lightfoot-Wild** 30:35 But this is when it's written under Composer.
**Sergey** 30:40 So Compat is some kind of, like, a plugin that runs for Composer?
I thought it's kind of like a layer that you implemented for SDK not to use PSR directly, but via the compat.
Or maybe I misunderstood.
**Chris Lightfoot-Wild** 30:55 So this is… so, line 13 there is doing that installed versions class exist check, and if you're in under Composer, that is already there at that point.
So, disable automatically loading that class, but if it's under Composer, it's already loaded.
I maybe just require, like, tagging Niva in this as well, and his thoughts on it. But then, it's just trying to say, okay, but I think we're under Composer, so… Make sure that these class definitions exist like this from the… But it's compatibility layer. So, like an older version of PSR3.
**Sergey** 31:37 So it's not a plugin, it will run at runtime, right? When you invoke, then you want to check But even… wouldn't it depend on order? Like, who is the first that loads PSR3? Like, who will require it first?
**Chris Lightfoot-Wild** 31:50 Yeah, it does. There's something else that I guess, was to beat this.
autoloader file from… and try to trigger PSR3 itself.
Then it would blow up somewhere else.
**Sergey** 32:03 Right, and you can only control… okay, I misunderstood what your compat does. I thought that your compat, what it does is that it essentially requires all the usages of SDK, of PSR3 log… PSR3 go through the compat, and then it will check If you already have PSR3 loaded, then it will not load another one that it brought with itself. But you can only do it for SDK itself, right? You cannot control what transitory depends on SDK do. And they themselves can bring in compatible from the composer point of view of version of PSR, And they will use it directly, you will not be able to control them, right? You cannot force them to use Compat.
**Chris Lightfoot-Wild** 32:39 But I guess if you're talking about, like, runtime, So, I've executed.
Do you compose…
**Sergey** 32:51 A composer cannot be, in this case, relied upon, because you don't have a common composer JSON where… you didn't have a phase where a composer could have resolved all the dependencies, right? You're essentially now bringing two incompatible sets of dependencies at runtime, and you want to prevent clashing at runtime.
Composer only works on the install time, then it could have prevented it, but it's too late now, you're now at runtime. You brought one vendor folder, another vendor folder, now you're trying to somehow avoid clutching between them, right?
**Bob Strecansky** 33:24 I think Chris might have…
**Chris Lightfoot-Wild** 33:25 food.
**Bob Strecansky** 33:25 Frozen slash drop. There we go. He's back.
**Sergey** 33:28 thus?
**Chris Lightfoot-Wild** 33:30 Sorry, I think my laptop's just having a nightmare.
Can you hear me?
**Bob Strecansky** 33:36 Yeah, we can hear you now.
**Sergey** 33:39 Can you hear us?
**Chris Lightfoot-Wild** 33:39 Sorry.
I think it's gonna melt its way through the desk in a minute.
Excited to do some background.
**Bob Strecansky** 33:48 Classic.
**Sergey** 33:50 So you want to say something? Can you hear us?
**Chris Lightfoot-Wild** 33:55 I can, yeah. Can you hear me okay?
**Sergey** 33:58 Yeah, we can hear it. So, you started to say something?
**Chris Lightfoot-Wild** 34:04 Yeah.
Sorry, it's very, it's very slow, there's a big, big lag on… on this a bit, so I'll struggle for…
**Sergey** 34:13 We can…
**Chris Lightfoot-Wild** 34:14 But I think the…
**Sergey** 34:14 I'm here in the UK, actually.
**Bob Strecansky** 34:17 Yeah, we can hear you just fine.
**Chris Lightfoot-Wild** 34:18 So, as you understand it, the dependencies for PSR3 are kind of already baked into Composer?
And then this is just a way of trying to make it work, if you're running under Composer.
And, you know…
**Sergey** 34:34 We're now in the same situation as we are in our distro, right? This is what we do in our distro. We essentially bring our own vendor folder with this distro, and we are loading it at runtime, while application brought its own, so application in this case is Composer, but it can be any other application, doesn't need to be Composer. It's just a FAR, but FAR inside of it contains all the dependencies of Composer itself.
But it can be any other tool, like PHP Stan, whatever. So if you look at how PitchPistan handles this, in order to load custom code, like, for example, PHP Stan, in order to analyze the code, it needs to load your bootstrap, right? It essentially needs to load your vendor of the application that it's trying to analyze.
So how does PHP Stan avoid clutching this vendor folder with its own dependency that's brought as a tool for its own use?
And obviously, all the transitive dependencies it's brought. They use this scoper, there is this tool called PHP Scopper.
So it essentially prefixes all the… all the… you can kind of give it vendor folder, it will go and prefix… kind of, like, wrap all the namespaces there in some kind of, like, top namespace that you can name with some unique name.
And then you package this vendor folder with yourself, so Composer seems not doing that, which Pistan does do that.
So that's why you essentially can run PHP stand on any codebase, doesn't matter what dependencies you use, it will load all those dependencies for analysis.
it doesn't matter, it still requires them as PHP, right? It loads them, so if they would clash Directly, like, it… Whatever dependencies PHPstan has, then you would runtime… you would have runtime crashes. But you don't have those with PHP Stand, because this… it uses this scoping technique. It essentially wrapped all its own dependencies in a separate namespace, that's why they don't clash with whatever application is used that it's analyzing.
**Chris Lightfoot-Wild** 36:29 Okay, that makes sense. So, I guess the ideal, then, would be that Composer would just do that as well, with PHP.
**Sergey** 36:35 Well, we can do it, like, this is what I'm working on now for our distro. When we'll finish the contribution, at least for distro, this is gonna be the same mechanism. Whether we want to adapt it for SDK as well, we can discuss it, because there are so obviously tricky things. It's not a guaranteed thing that… some libraries don't behave well.
For example, special libraries that, development tools, like, for example, Code Sniffer, it is aware what its namespace is supposed to be, what composer namespace to be, it does all kinds of tricks with trying to analyze classes which namespaces they belong to, so it's tricky. Not all the libraries behave well when you just wrap them in additional namespace.
It's not kind of, like, straightforward thing. So, as a technique, like, this is what we do in Vowa Distro. We're just wrapping whatever… and SDK in particular as well. Wrap an SDK and everything, SDK drags in as transit dependencies, we wrap it all in some kind of, like, isolating namespace.
So it seems to be working for develop… for those dependencies so far.
But when I tried to do it for development dependencies, like cold sniffer, it didn't work for that so well, so… It's not a straightforward thing to assume, but this is what we're trying to make it work. Like, so that would be a solution, universal solution, where you don't need to treat, like, each library like PSR3 or whatever.
You just wrap all your dependencies, in this case.
all SDK dependencies, and this… well, SDK itself, you don't need to, but… Because you want application to be able to refer directly to SDK API with normal namespace.
But all the… all your dependencies, all the vendor folder.
But again.
With SDK, it's a little bit tricky. It's more considering, because SDK is used as this direct library that people require. So… I guess it depends on the use case, but… So, but forcing Composer to use that, you know, it's hard, because how can you force them? They don't do it, maybe they have some reasons why they don't do it. So if you want to solve it on the SDK side.
Like, that might be one of the solutions.
wrap all the dependencies that SDK has.
**Shawn Maddock** 38:46 PSR 3.1 is… Kinda unique, though, right? Because it's… The fatal errors come when… PSR3 is trying to log an error about OTEL2PSR3.
It's a circular… Dependency, right? That's what this is trying to solve? In the autoloader?
**Chris Lightfoot-Wild** 39:09 It's… yeah, it's trying to prevent an incompatible… abstract class.
**Sergey** 39:14 Yeah, I mean, it's not about doing some action, it even fails on the phase of parsing the code.
At each beam.
Like, for example, I encountered… I didn't encounter problems with PSR3. I mostly encountered problems with PSR HTTP message.
between two versions, so when I… SDK somehow forces it to go down to version 1.1, but then if I try to run it on an application that doesn't require SDK directly.
So it immediately clashes, like, for example, React. React, by default, will bring PSR HTTP message to zero.
And if I will load SDK into that next with its own dependencies, which is, as I said, forces it down to PSR11, then it will cluster on the level of passing the class. It will tell, okay.
He already loaded this interface that I'm trying to implement, which is not compatible with whatever was expected when that vendor folder was built. So, it's kind of like clashes even on that phase, even before running.
**Shawn Maddock** 40:13 Okay, I was thinking of something else.
**Sergey** 40:16 But again, maybe in this case, But it sounds like what you said, Chris, is exactly what I am experiencing with PSRMA. So it's about Amster Class that Trying to implement something, or the interface or obstacle class, that is essentially coming with two conflicting versions, and that's why it's crushing.
**Chris Lightfoot-Wild** 40:36 Okay, well, is it… you've obviously done a lot more, investigations than I have already, so if you've been working on it for your distro.
**Sergey** 40:44 Yeah, I can show you, like, I hope I will have a working prototype soon, at the end of this week, so I can send you the PSR if you want to take a look.
whether, I mean, I definitely want to… my next step is to try to run all the tests for the SDK, at least, to make sure that it passes in this isolated forum.
then the next step would be to do it for Contrib, but, yeah. So the hope that this technique can be used. Then we want to try, maybe even run an older… Tests on all the dependencies in the wrapped form.
Because, like I said, it's not straightforward. Some libraries don't like it when you wrap them.
**Chris Lightfoot-Wild** 41:24 Cool.
So, should I close that? Is that, I could put it, or a link in the channel if anyone else has got…
**Sergey** 41:33 But if you have some temporary solution that satisfies this particular… solves the problem, then… I don't want for it to be interpreted, like I said, it's definitely more kind of like the solution that we're trying to do.
It definitely has more risks, so if you have a solution that is more local, but you think it's less risky, then Not saying that you should close it, right?
**Chris Lightfoot-Wild** 41:55 I didn't take any offense to that, by the way, I just, you know, got two alternatives, and just having a stab at it, but Yeah, if it…
**Sergey** 42:04 So I will send you, when it's ready, whatever we are doing, then we can reevaluate, you can take a look, and we can discuss it.
**Chris Lightfoot-Wild** 42:12 Boom.
Thank you.
Maybe I can just tag, Neive slash Brett in there as well, just in case they've not seen it already, and… The bigger brands than mine can weigh in.
**Bob Strecansky** 42:26 Their brains aren't bigger than yours.
They're the same size.
**Chris Lightfoot-Wild** 42:33 Well, mine's just super smooth, that's what it is.
**Bob Strecansky** 42:35 Oh, that's… I love calling people smooth brains behind their back, it's great.
Alright, cool, thanks for that discussion.
**Chris Lightfoot-Wild** 42:49 Can I just ask, I guess, when you're talking about, with the other, sinks.
Is part of the ideal that if you were to start, like, a completely greenfield project.
OpenTelemetry wants to kind of be that one-stop shop, like, you know, you just add this dependency.
And then we cover all your logging, tracing, metric needs from the get-go.
**Bob Strecansky** 43:11 I think that that has been Morgan and Ted's goal since the inception of OpenTelemetry.
I think how we get… I think how we… I think how we get there is still undefined. I think that that is the long… like, the long-term intent.
**Chris Lightfoot-Wild** 43:26 Cool. And then, I guess just to wrap in my own head, at least, then, from what we… even if that new API came to fruition.
We'd basically have to just have some… adapters are… bridge layer, which… because I thought we already had a log bridge at one point in the past.
To make modeling, basically use that.
New API.
**Bob Strecansky** 43:48 Yes.
**Sergey** 43:49 Yeah, exactly what you said, so I was just wondering, doesn't it already provide this PSR3, provide this solution for library implementers? Like, shouldn't they use PSR3 instead of using even… like, if… so when you're talking about this greenfield project, I would divide it in two, right? Application developers, and, like, and Leaf Flake users, and then library developers.
So for library developers, there is already this PSR3 that they should use, right? They should not use OpenTelemetry directly, or is that the recommendation will be eventually to use OpenTelemetry API directly, even? It will also kind of, like, replace PSR3 as well.
**Bob Strecansky** 44:24 I don't know.
I think that's… that's, like, been the whole debate.
**Shawn Maddock** 44:33 think that… PHP Fig would have to adopt OpenTelemetry.
**Bob Strecansky** 44:40 I think you're right.
**Chris Lightfoot-Wild** 44:47 Cool.
No, very log-heavy meeting today.
**Bob Strecansky** 44:51 That's okay, but that's one of the signals.
Alright, Anybody else have anything else to talk about? I'll walk through the board really quick and see if there's anything. I'm gonna… I'm planning on going through these, the Dependabot slash Renovate things this week, because it's had 2 weeks to bake, and it looks like it's doing good stuff. But it doesn't look like we have a lot of other, things besides your PSR thing, which we're talking about, Chris, so…
**Sergey** 45:21 automatically give up, it doesn't have an expiration date on those PRs, like…
**Bob Strecansky** 45:25 I've blown.
**Sergey** 45:25 Close them up sometime, or…
**Bob Strecansky** 45:27 I would assume… I would assume… well, so, what I have seen is, I think… When both of these tools open a new PR with, like, a new version of the library, it will automatically close the old one.
So, like, I've seen a bunch… I've seen a bunch closed. Like, see where it says bumped? Yeah.
**Sergey** 45:46 It's smart enough not to pile on, on something. So, and then the new one will be accumulating things, like, well, I guess in this case, it doesn't even need to, so it will replace directly from from the old, it was in main directly to the newest?
**Bob Strecansky** 46:01 Yeah, so, like, for example, this one was closed 6 hours ago that pumps right as from version A to version B, and then I think that this one is version C, if I understand, I think this one's version C, like, a newer version, and so that's why it closed the previous one. But again, Dependabot is probably not going to be the one that we are going to use. We'll probably use Renovate.
Again, I gotta do a little bit of digging here, I haven't had time to, like, really fine-tooth comb it, but I would like to.
**Chris Lightfoot-Wild** 46:35 Yeah, I put a message in the chat there randomly, because I started, adding that filter when looking at… like, the PR board, because… It's easy to get stuff lost in the… Oh, yeah.
Yeah, so…
**Bob Strecansky** 46:50 Yeah, I will take the action to work on that this week.
Alright…
**Chris Lightfoot-Wild** 46:58 And also, I have, sort of, eyeballed some of them, but decided again, because I didn't know if… if I was to, like, say, oh yeah, this looks good to me, and I'll approve it, if it just drops off your list or not, because otherwise it marks itself as, you know.
kind of already approved now, so it might disappear, so I've…
**Bob Strecansky** 47:18 Yeah, do you have… you have the ability to approve, but not to merge, is that right?
**Chris Lightfoot-Wild** 47:23 I can approve, yeah, but then I think if I do that, it probably drops off your list, doesn't it? So, I've just been leaving it to you.
**Bob Strecansky** 47:31 I think so, but I will… yeah, I'm… I'm gonna do this this week.
**Chris Lightfoot-Wild** 47:35 Bless.
**Bob Strecansky** 47:36 Yep.
Cool.
Anybody else have active discussion topics?
Alright, well.
**Chris Lightfoot-Wild** 47:53 So there's a login thing that, Sean, you mentioned, between the monologue instrumentation and the PSR3. Maybe I could just, ping you and just try and understand a bit as well, because I'd… in the past, said I'd like to try and get the Laravel instrumentation to actually use the PSR.
Three directly, rather than… It's on Event Listener 1.
Because it… that also handles the log messages a bit differently to the other two, and it's just… It's a bit of a confusing part of the ecosystem at the moment.
you a message, if that's okay.
**Shawn Maddock** 48:30 Yeah, go for it.
**Chris Lightfoot-Wild** 48:32 Cool, thank you.
**Bob Strecansky** 48:37 Alright, thanks, y'all, we'll see you… I won't be here next week, I'll be here the week after.
**Chris Lightfoot-Wild** 48:41 Enjoy the… the turkey.
Thanks, I will. We'll catch y'all on the internet.
**Bob Strecansky** 48:48 Tender freedoms!
**Chris Lightfoot-Wild** 48:52 See you later.
**Bob Strecansky** 48:53 Bye.
