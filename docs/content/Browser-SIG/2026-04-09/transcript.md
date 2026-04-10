SIG: Browser SIG
Date: 2026-04-09
Duration: 32 minutes
============================================================

## Zoom Recording Transcript

**Joaquín Díaz** 00:41 What's up?
**Jared Freeze** 00:42 Hey, how's it going?
**Joaquín Díaz** 00:44 Hey, Christopher.
**Christopher Arredondo** 00:48 Hi everyone, how are you?
**Jared Freeze** 00:51 Good, good, didn't you?
**Christopher Arredondo** 00:53 Yeah, thanks for asking.
**Jared Freeze** 01:02 Hey, Hugo.
So, I think, Martin said he was… About this week.
We'll give… just… then everybody a little bit of a shot.
**Ted Young** 02:00 Hey, hey, how y'all doing?
**David Luna Bistuer** 02:06 Doing it again. Yep.
**Ted Young** 02:09 Good to see ya.
**Jared Freeze** 02:38 Oops. I think, Martin said he was out this week.
**Ted Young** 02:42 Oh, okay.
**Jared Freeze** 02:43 Yeah, I think we can, probably get started.
So it looks like, Waco, you got the… the first item? End-to-end demo for Fonda Dashboards?
**Joaquín Díaz** 02:56 Yeah, not this week, but last week we talked about having some sort of place where we can see what we are collecting while we are emitting from the SDK.
So I created a PR without Grafana dashboard, and, a few widgets showing metrics, so we collect what we have right now, and some of the… Old JavaScript… instrumentation, mainly the fetch one. We definitely don't need to go through the PR right now.
But maybe, I don't know if you are going to show the… Or I can show it.
I can show a few screenshots, because I have it down right now.
Hold on for a second, I'm not looking for it.
Can you see my screen?
**Ted Young** 04:11 Yep.
**Joaquín Díaz** 04:13 Okay, yeah, I don't want to spend too much time right now, here, since there are other topics, but yeah, basically, I created We found a dashboard with metrics, with what we collect. These are just some samples.
Logs per second is also another way of counting logs, spans per second, spam duration… Then I have a few more that are more browser-specific. These are all web vitals.
I used the demo that I think Maxine created, so, these are, like, synthetic data.
For web vitals, it's tricky to generate, like, a valid Web Vital.
So these are just sample values, But yeah, like, the rating, which is all good, because it's a really small app.
Hc… I'm sorry, are you seeing the graphs when I take this?
**Hugo Levy** 05:16 Yes, we do.
**Ted Young** 05:16 Yeah.
**Joaquín Díaz** 05:17 Okay.
these all HTTP data, like, amount of requests grouped by status called, P95 of requests.
Group by host.
And then just call my host.
This is another one that is, web-specific, these clicks.
go by element ID, or the CSS selector.
And finally, some blocks.
These are all the logs, and these are error logs.
But yeah, hopefully that is what we have in mind.
And I am not… definitely not an expert on setting up a collector or Grafana, so… If you have any comments, please let me know.
**Ted Young** 06:10 That's awesome.
**Jared Freeze** 06:12 Yeah, it looks really nice. That last graph is pretty cool, too.
It just looks cool.
**Joaquín Díaz** 06:18 Yeah, looks like DNA.
**Jared Freeze** 06:20 It does.
**Joaquín Díaz** 06:24 Okay, thanks.
**Hugo Levy** 06:26 Okay.
Okay, sorry, just one question. When you, when you check out the, the clicks, and you want to see on which, element you clicked on. Which attribute… did you use a tag name, or did you use, the equivalent of the CSS?
Target?
**Joaquín Díaz** 06:43 Yes, we have both. We have the tag name, but I use, CSS selector, I think it's called. It's one of the attributes that we need.
but the issue with that is that we may have things with the same selector, Awesome.
we may want to use, like, I think it's called XPath or something else.
But that is… It should be fairly simple to add it to the instrumentation.
**Jared Freeze** 07:13 That's probably worth standardizing on, because some people are gonna care about the text.
Or some people might only want the attributes.
You know, so there's the data-otel, which I think is… One of the hooks for clicks.
So I wonder if… There should be options and stuff there.
maybe we can make an issue for that, for how to standardize, because I know, like, XPath is pretty… Standard, but grouping and parsing and all those things is… It's pretty high cardinality, which I know we want to limit, so… If you use text, it's, like, the worst.
But, that's really… that's interesting.
**Joaquín Díaz** 07:56 Yeah, I don't think… that was just an example, I don't think anyone will… Grow up by… Click element, because, like, you can click under some things in this page, so you will get, like, really high cardinality on that.
But I guess if you set up filters or whatever, maybe it's more useful for you, but yeah.
We can definitely… we should definitely… Sync on what we want to show, like, what we want to use as an element identifier.
**Jared Freeze** 08:33 Bill? Thanks. So, I think, So, Amy, do you have the, browser package draft?
**David Luna Bistuer** 08:41 Yeah, well, let me share with you, and then… I think I can explain a little bit better.
Yeah, you see, right, the PR?
So that's the link to the PR. Basically.
This is following, something that we were… kind of, testing in Elastic, and then, since we merge all the instrumentations, and we used the extra paths to control a bit which instrumentations are you using, and then you control… therefore, you control the bundle size.
kind of, were tempted to actually do a project for the same for the SDK. So, this PR introduces a new package, which is the browser package. There was a discussion about this on the release process.
to have a new package that includes SDKs and other config options.
Excellent. So, that's the… there was a first approach, and we got… I got the… the, comments from Martin. We were… I was using classes at first, but then… He proposed to use, functions. So, long story short is, the new package, has different exports.
has one expert per signal, so you can configure signals independently, and then you can combine together.
The result is that, if you just import just one signal, you just get only the code that, refers to that signal.
Processors, exporters, etc.
And then, Also, we provide kind of a convenience method to combine the SDKs. So, for example, in this example.
This, for example, I'm just using the Logs SDK.
I'm just configuring the log SDK, so only I have… I only registered a log provider, a logger provider, therefore, I just emit logs.
With this other example, we can just, you know, import logs and traces SDKs, but then combine them together.
And I've used this kind of API, or at least these options objects, because there were previous works from Martin, about creating a web SDK, and one recurrent, comment was about having separate entries for configuration, so having traces configuration, and then blocks configuration, and then metrics configuration, so… This is kind of more type-friendly, so you combine the SDKs using logs and traces, and then you, as a result, you get A function that, accepts a global configuration, and then you have a single-specific configuration.
then you can, what this, what this does, for example, this is kind of an example. You can set up more genetic.
endpoint.
That's, that it works for all signals, so then… or… or if you want, in the logs entry, you can set a specific endpoint for the logs as well.
So, that's kind of the approach.
I just wanted to present it here. It's still in draft because, well, only tests are missing.
But first, I want you to just jump in.
Look at the code.
give your feedback, and, I don't know, maybe just get into, the final decision on the design, on the API that we want for this package, and then move forward.
Okay, so, if you want to have a look at this, and give me your opinion.
If we are agreeing with that, I will remove the draft, and then I'll finish the tests.
**Jared Freeze** 12:26 Cool, that is awesome.
**Ted Young** 12:28 Yeah.
I'm curious how much it diverges from how, you know, Node.js SDK installation works.
**David Luna Bistuer** 12:38 Hmm… Well, basically, the NodeGS have, just a single class that.
**Ted Young** 12:45 Yep.
**David Luna Bistuer** 12:46 As, you know, holds the whole configuration.
And then, So it pulls all the SDKs, logs, metrics, and traces.
And then… yeah, it doesn't have… so all configuration is merged in a single object. This one, the difference, this one is, like, you… you are just picking exactly which signal you want to configure, and then you can combine together. That's… that makes the… you get… this comes with the benefit of just controlling the bundle size. So I don't want metrics, for example, or I do want metrics, so just… I just pulled the metrics SDK. It's not there yet, because we are not using it. For now, you only have logs and resources, but for example, if I'm only interested with logs.
I use a TLOC SDK. If I want to use both, for example, in our case, in Elastic, we want to use both.
We just combine them together, we get a bundle size bigger, but we like to both signals. And then we can, we can have this, this… default configurations, for example, the endpoint, or you can have more specific ones. In Node.js, it's just… you get everything, so you set an endpoint, and it's for everything. Or maybe you can tweak a little bit some environment variables.
But, you know, it's like, it's a big configuration for Node. This one is more, sliced.
Let's saying that word.
**Ted Young** 14:09 Cool.
**Jared Freeze** 14:13 Nice.
**Hugo Levy** 14:15 Good.
**Joaquín Díaz** 14:15 Sorry, one quick question about that. I was just looking at the coda, so I don't know.
Can you also disable or enable instrumentation when you initiate the SDK?
**David Luna Bistuer** 14:30 Yeah, instrumentation here, now I'm just focusing on the SDKs.
But then… you mean dynamically, so once already they are revisited and enabled?
You want to, you want to disable them at runtime? Yeah?
**Joaquín Díaz** 14:49 like, for example, let's say I only want, like.
I don't know, click instrumentation, like, I… first of all, I think… Based on this, I have to set that up.
manually, right? This…
**David Luna Bistuer** 15:02 Yes, for now it's just the configuration of the APIs, yeah. Okay. Now it's just… we were just configuring the signals.
Then, we can have a follow-up on that, or maybe we can discuss here on how to include the instrumentations.
since this is something new, I would prefer to just… just review this part, and then… and then, continue with the instrumentations and all that. But now with the… with the current implementation, you just, you know, start the… starting the SDK, just register the… uses the API to register logger provider and tracer provider.
Then you can import instrumentations from the instrumentation packet and register there.
Then you start. So it's more… it's still manually in this case. So you have to have the friction to set up everything, but then you have to register these limitations yourself.
**Joaquín Díaz** 15:52 Yes, makes sense. Thanks.
**Jared Freeze** 15:56 Yeah, I think one of the things that was, that I'd like to see is, like, when you're including instrumentation, like, I know you're not working on this, but when you include instrumentation, to be able to pass, like, enabled To each one. So that way, you're not having to, like, spread on an object for, like, weather to.
**David Luna Bistuer** 16:14 Includes.
**Jared Freeze** 16:15 something or not. That way, you can just have, like, environmental variables that control sort of what comes in or out. I mean, you could always keep two arrays, but it might help to dedupe those things. Because we had talked about, you know, what default instrumentation looks like, and how to sort of make it magic out of the box.
But yeah, that's really cool.
So, that'll be nice. Definitely review that and check it out.
**David Luna Bistuer** 16:38 Okay, thank you.
**Jared Freeze** 16:40 And then the last one, the… I just added it, Dan, who is here.
had a PR up that… removes HR time from fetch instrumentation. Fetch, I guess, is gonna get migrated, but I actually had a concern that when we upstreamed, Web Vitals, that I messed up.
Because it didn't get wrapped in HR time?
And then, to see that PR come through.
was good, I guess, because we don't have that precision anyways, right? And the browser introduces noise. We don't actually get microseconds or nanoseconds or anything like that. So, Yeah, I guess, as a policy, it's… I guess it looks like we're just gonna use DOM Hi-Res timestamp, just what comes out of performance.now, and not convert anything, to any other unit or format or anything like that. Which is good, because I think that's… Totally appropriate. I mean, that's what we get, that's what we should use, it does… it is not… OTEL, right? Like, OTEL requires nanoseconds, I believe, from reading the specs. So, I assume we're just gonna move forward with Milliseconds, you know, as it's… as it's constructed now.
I'm not sure if you can comment on that, Ted, or Dan.
**Daniel Dyla (Dynatrace)** 18:07 Yeah, I mean… the… the nanoseconds thing, I guess, like… There's a lot of reasons that we used the high-res the HR time in the first place, but that was primarily the reason.
In the browser, it doesn't make any sense, because the browser fuzzes your timings anyways. I think you get, like, plus… Yeah, like, you get anywhere from, like, 1 to 5 millisecond like… The browser will just lie to you.
So, in Node, it makes sense to have those super high resolution times, but in browser, it doesn't.
Even the DOM high-res timestamps have, like, they'll lie to you.
So… it doesn't make any sense in the browser to use those. The PR that I made against Fetch.
All it's doing is… Taking out a bunch of, like, unnecessary conversions, because the… the web… instrumentation was converting those timestamps to HR times, doing a bunch of math on them, then converting them back, and then, like, it… they were all completely unnecessary. So even if the SDK continues to use HR time, those should go away. There's no point in the browser instrumentations.
Ever using that format.
**Jared Freeze** 19:33 Now, is that a concern for… the… shared conventions.
Right? Like, if I have an endpoint that accepts, you know, node data and browser data.
Like, they're gonna be getting different numbers.
**Daniel Dyla (Dynatrace)** 19:50 What sort of endpoint do you… you mean an OTLP endpoint?
**Jared Freeze** 19:54 Yeah.
**Daniel Dyla (Dynatrace)** 19:55 Because in the end, OTLP is gonna be receiving the nanosecond, like, fixed 64 no matter what.
**Jared Freeze** 20:03 Okay.
**Daniel Dyla (Dynatrace)** 20:04 No matter how we represent the time, it needs to be converted to that in the end.
We… If you use just, like, the Node.js number type.
you get unacceptably low resolution. Like, you get… there… you cannot represent timestamps with sufficient accuracy, with just a basic number. So you either have to store it as two numbers, which is what the HR time is, you have the second part and then the nanosecond part.
Or you store it as a big int, which didn't exist back in the day.
But also has some performance implications, because it's not a fixed-width integer. Some of the low-level math that's done during the serialization is slower.
There's trade-offs to all of these things. I think after some… some thinking and profiling, I don't think removing the HR time from the core SDK is really doing us much good, but at least removing it from the browsers is.
**Jared Freeze** 21:13 Okay, cool, I get it. That sounds good.
**Daniel Dyla (Dynatrace)** 21:16 The serialization of that HR time to protobuf is really fast, because we can do some, like, bit manipulations that aren't really possible if we use other formats.
Particularly with Mark's custom protobuf serializer, is really fast. It's almost not worth optimizing more than it already is.
**Jared Freeze** 21:38 Correct me if I'm wrong, but we don't use that in browser at all, right? Like, there is no protobuf.
It's JSON only.
**Daniel Dyla (Dynatrace)** 21:46 I mean, right now, people are using the Protobuff, I think.
Very common.
**Jared Freeze** 21:53 on the web.
**Daniel Dyla (Dynatrace)** 21:54 Yeah.
**Jared Freeze** 21:58 Okay.
**Ted Young** 22:00 Amazing to me.
**Jared Freeze** 22:01 Yeah, I don't think that's possible. That was my understanding.
**Daniel Dyla (Dynatrace)** 22:06 Well, people are definitely using it, because otherwise we wouldn't get bugs, like, people report, the Protobuff.js-generated code uses eval.
Which.
**Jared Freeze** 22:16 No, that's…
**Daniel Dyla (Dynatrace)** 22:17 complain about?
**Jared Freeze** 22:18 Yeah, that's different, though. That's the static analysis that Webpack complains about, because it has to be included if you include, the trace package. So, it actually is… Not in use, but it's in the way, basically.
Got it, that's the issue. So.
**Daniel Dyla (Dynatrace)** 22:37 Well, in any case, it's still, like, the… the… even if you're serializing to JSON, it's not, like, a very… it's a… it's a quick process, because even if you have, like, the… the second part and the nanosecond part as two separate numbers, string concatenation is all you're doing there, and that's really fast in JavaScript.
**Jared Freeze** 23:00 Yeah, totally. I follow you.
Cool. Well, that's awesome. Well, I'll be interested to see both, I don't know if you guys are active in Slack, but I've been harassing Google all week, for 2 weeks, to release Protobuff, and they were like, yay, we did it, which is great. I'm not, like.
you know, no shade to them, but there is the sub-libraries, the packages that do not get published with Protobuf itself. That's where the eval actually lives, and so I've been digging around, trying to find somebody, there's, one guy who doesn't work there anymore who's been reaching out to people that still work there to try to get that released, but if we use this new Protobuff serializer, I think that goes away.
So, it may be a non-issue, but I've been trying to hack away at that a little bit. We got close, but yeah, that package hasn't been released in 9 years, and they fixed the bug, like… 2 or 3 years ago, I think. It's just that it hasn't gone out the door.
So, so yeah, I'm glad to see that solution.
**Daniel Dyla (Dynatrace)** 24:07 Yeah, I mean, the custom protobuf serialization has other advantages also in nodes, so there's a lot of other reasons to do it, regardless of whether it ends up used in browser or not.
**Jared Freeze** 24:17 Yeah, absolutely.
Okay, cool, that's all that we have on our agenda list. Does anybody have anything else, or questions, or… Anything they want to go over?
**Ted Young** 24:34 I'm stoked to see this coming together, and I'm glad to be back.
**Jared Freeze** 24:37 Yeah, awesome, good to see you.
I guess there's one other thing I want to… oh, go ahead, Dan.
**Daniel Dyla (Dynatrace)** 24:43 I was gonna say, I do have, with that Fetch PR, it's a draft right now, because… It makes a breaking change to, like, the SDK trace web package, which doesn't really do anything. It's kind of my assumption that that package will go away, that's kind of the plan. So I… because I didn't know… what the browser plan is around that. I just left that PR as a draft, as, like, this is one way that we could do this.
Should I just… Instead of making that breaking change, copy the code into the instrumentation and get that fix out the door for now, so that it can be used.
Or is it better to just hold off and wait for everything to be migrated to the browser package first?
**Jared Freeze** 25:30 I mean, I saw… I saw that it got marked breaking.
those things… Yeah, I think are not mutually exclusive. I would copy it to the browser instrumentation and let people start using it.
Is it generating… spans?
It is.
**Daniel Dyla (Dynatrace)** 25:52 The fetch instrumentation? Yeah.
**Jared Freeze** 25:54 Yeah, so, I don't know, I mean, that kind of doesn't fit into the new model, but we also haven't, like, completely solidified that new model, so copying it over and generating spans might be confusing, because there's already documentation that says we're moving to logs.
we should probably settle that first before you copy something over.
But yeah, if you want to make the breaking change in the trace web, I… yeah, that's up to you.
**Joaquín Díaz** 26:20 sync… Batch is where spuns may make the most sense. I wouldn't move them to logs.
**Jared Freeze** 26:27 I agree with that. Yeah, because it's like, if you want a waterfall, they are spans.
**Joaquín Díaz** 26:32 Yeah, and then we have the header, the trace part, and something. Yeah, I think we may have other things inside there, so yeah, I wouldn't move that one specifically to log, so I think it's fine that it's, That's fun.
**Jared Freeze** 26:49 I… yeah, I'm concerned that issues with context, the fact that people are not really using context at the moment.
And it's a copy…
**Daniel Dyla (Dynatrace)** 26:58 I think we're referring to different copies. You're talking about the copying over into the browser instrumentation. I'm talking about copying that utility function that's in the trace web directly into the instrumentation so that I can make the change to it without making a breaking change? Like, does that have enough value to do right now, or should I just hold off on that?
**Jared Freeze** 27:19 I would go ahead and do that, yeah. I would do that. Sorry, I misunderstood. Yeah, copying it into browser instrumentation, I think, is the larger conversation. Yes. I think you should do that. That's my vote.
**Daniel Dyla (Dynatrace)** 27:36 Okay, I'll do the same thing with the XHR instrumentation, and then, yeah, we can decide what to do about that trace web package. It's been… Yeah.
I… I will not be sad when it goes away.
**Jared Freeze** 27:52 Yeah, that sounds good.
Yeah, if we were to rep… I mean, if we were to convert something from spans to logs, if… that was desired, I don't even know what that would look like.
Hmm.
Alright, well, I guess we're pretty much out of time. Nobody has anything else?
Okay, cool.
See ya.
**David Luna Bistuer** 28:27 Bye.
