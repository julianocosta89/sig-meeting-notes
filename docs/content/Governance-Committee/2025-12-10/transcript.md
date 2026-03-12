SIG: Governance Committee
Date: 2025-12-10
Duration: 63 minutes
Zoom Recording URL: https://zoom.us/rec/share/eSKre4c7hTY-oRSqT1FaIxs4RWSHGjKlTSkZ_4Z4XamwkIRqh9HmF5_CdseCuK-y.WFywuN-YYegQEr9K
============================================================

## Zoom Recording Transcript

Reiley 00:01:53 Hello, Darcy, Austin.
Austin Parker 00:01:59 Ayyy.
We should have… Jeremy joining us. Oh, there's Jeremy.
Jeremy Morrell 00:02:36 Hey, Austin.
Austin Parker 00:02:38 Howdy, howdy.
Give folks a few more minutes.
Tigran Najaryan 00:03:45 Hey, everyone.
Austin Parker 00:03:47 Howdy.
Reiley 00:03:49 Hello?
Austin Parker 00:04:11 Okay, I see Ted's not here… Ted's in Japan… I don't know.
I feel like we'll go ahead and get started, because we do have Jeremy presenting, and then we have some other stuff, so… This is being recorded, so people that miss it can… Watch it.
Tigran Najaryan 00:04:37 If we want to start with Kotlin donation, then probably worth waiting for Carlos.
Maybe for a minute or two.
Austin Parker 00:04:47 The edge…
Tigran Najaryan 00:04:49 Or we can start with some other topics, if we have anything else.
Austin Parker 00:04:52 Would we rather… so Jeremy's gonna present, and we'll discuss the cleav, and just to present a.
Tigran Najaryan 00:04:59 Oh, I see.
Okay, okay, cool.
Austin Parker 00:05:01 So we have a guest, we should probably do that first, and then we can do the Kotlin stuff and the KubeCon stuff afterwards. Does that make sense?
Tigran Najaryan 00:05:08 Yep, sounds good, thank you.
Austin Parker 00:05:10 Okay. Yeah, so just… to… Lead it off.
I asked Jeremy to come by and talk a little bit about what they've been doing at Cloudflare with automatic tracing for Cloudflare workers, I thought this would be really interesting, because it's a pretty big application of what we've done, and I think it's always great for us to hear, sort of this level, about how people are using hotel in interesting ways, and also adapting it, So, I think we have a couple, little prepared stuff, and then a bunch of Q&A time. So, with that said, Jeremy, if you want to take it away, do some intros, just… The quick… the quick intro for everyone, so we don't waste time, is this is the Joint Governance Committee and Technical Committee, so, If people want to introduce themselves later when they ask questions or introduce themselves in the chat, that would be fantastic. But with that said, take it away.
Jeremy Morrell 00:06:12 Cool. I assume everyone can see my screen.
Cool. Thanks, Austin, for inviting me. Hi. I'm Jeremy, I'm a principal engineer at Cloudflare, I'm working on Platform Ollie, and we recently had this launch of automatic tracing.
Before I get into, like, what that is, how we built it, I'm just gonna give a quick overview of the Cloudflare platform, just so that we, our workers platform, just so we're all on the same page.
First, it's a serverless compute platform.
you run… we have, like, 300-plus pops, I keep… maybe 400 now, I keep… I can't keep track.
And so when a request comes in, we'll spin up a JavaScript isolate and run your script. Generally, it's within, like, 50 milliseconds of where the user is. That was the first product, and then we've added all sorts of things that you would expect from a compute platform. We have an object store, we have the SQL database.
queues, workflows, all that stuff. Now you can build full-stack applications on this runtime, and then what… and then observability, or like, what is happening within my runtime? It was sort of a black box, and so this was a problem that kind of we set out to solve.
Just to give you an idea, this is what a hello world looks like, on the Cloudflare workers. You define a fetch function, and it's just JavaScript. This gets bundled the same way you might bundle a frontend application, the Java front-end application.
So there's… there's no container, there's no Docker build, it's super lightweight, like, this would just be a few… a kilobyte or so.
And that is important because we are sitting on the edge, and people often put Cloudflare workers in front of their app, so that it should load very, very fast, and not add latency to another request, especially if you're using this as a proxy.
This executes on our custom JS runtime, which is not Node, Bun, or Deno, but it's a custom runtime called WorkerD that embeds the V8 JavaScript engine.
And then, important to our discussion today, Workers has this concept called bindings. So if you want to use our KV, service, you added a little bit of config to, your, Worker config.
Say, here's what I want the name to be, here's the ID.
And then you get it passed in, so your effect function gets it passed in into the, into an object called environment, and then you just can call it. There's no… library to install, there's no client library, there's no secrets to manage, like you might use if you, if you've used other, sort of, past providers, and you want to talk to a Postgres. Well, then they inject a secret, and then you have to bring in your own Postgres, client.
You just get… you can just call the function directly, and then we manage all that.
This gives us a lot of leverage when it comes to instrumentation. There's no need for, like, doing the sort of auto-instrumentation, magical wrapping, when you can just build the instrumentation directly into the runtime.
So, we have this… this is the vision we have for tracing. So, like, on day one.
you get best-of-class instrumentation and telemetry just out of the box. The platform has a ton of context, or at least it will.
We know that you just deployed a new version. We know the version ID. We know that it corresponds with this GitHaw, that it was deployed via CI because you merged this PR.
We know when the request comes in, it came from this city, from a mobile device running this version of Android, and it was executed, geographically the next city over.
there's… that's a ton of context, and if you want to thread all of that through for your own… like, if you're deploying on, say, like, EC2, and you want to thread all that context in, that is a ton, a ton of work. I know, because I've… I've had to do this.
And then beyond that, we want to embrace open standards. So, the idea is embracing W3C and OpenTelemetry, and then… Beyond the telemetry that we're generating for you, We want to enable advanced use cases, so sampling strategies, custom processing. This is going to be, sort of a long journey, and this is… the far vision.
the other part of it is that the… we should raise the floor. So, right now, if you… enabling observability is just this little bit of config, and then you get traces in the dashboard. There's no selecting a vendor, there's no, importing an SDK, there's no configuration. Just by default, you get, All of this, sort of, out of the box.
And so, like, this is what it looks like. This is the Cloudflare dashboard, and then you can see here is the root span, and we have a ton of information on this, including the version ID, the region, you can see we tried to match the semantic conventions as best as we can, all the URL, then we also end up with things like user agent, and then we parse, the operating system and browser and all of the stuff you can parse out of that.
Time zone, we know the country, we know the locality, and this is from where the user's, making the request, and then we can also see where it's being processed in which colo.
For fetch, for fetch spans, if you make a fetch, then you get all of the… semantic conventions in the instrumentation that you would expect from any OpenTelemetry SDK. And the important piece is that this, this worker has zero instrumentation code. This is just all built into the runtime.
You can also… we also put that… we also put that data into ClickHouse, and then we have a query builder, so you might, Run queries across all of this data, the spans, logs, any other events.
And then importantly, especially for this, audience, you can add destinations. So, we can emit this data as OTLP, and you don't have to go to our dashboard. Especially for our bigger customers, this is really important. They have their own internal stack set up, they have their Grafanas, and that's where they really want their data. They don't want to have to come to the Cloudflare dashboard. So… As long as they can receive OTLP formatted as JSON over HTTP, and I'll talk about that constraint in a second.
Then, you can send the data, kind of, to any place you need, or instead of a collector to do any translation you might want to do.
So as we started going into building this, we had a couple of constraints.
the whole point of our platform is to be super, super lightweight, so we don't want to add, a ton of performance impact in order to do this work. We don't want to force the user to install an SDK, and, like, make that bundle even bigger. It's gonna slow down their They're cold start times. Ideally, no code.
And then, importantly, the runtime is already this, like, really complex beast with, V8 as a huge dependency, and then workers as well has strict backwards compatibility goals. Once you deploy a worker.
it should always work, even if you deploy it again a decade later. So we're very averse, to adding dependencies, and then we also have strict, performance and privacy, it's a really hard code base to work in, so just pulling down the C++ SDK, installing it was shot down really early in the project.
It's also kind of a weird dialect of C++ that doesn't use the standard library due to historical reasons, but it would just be really hard to leverage the OpenTelemetry SDK here.
So internally, we have these… this is some binding code. This is, if I pull in the KV binding, I'm calling put on it, this is the code in WorkerD that gets executed. We have two tracers. We have one in for our own internal tracing, and then one that is user-facing.
This tracer was sort of loosely based on a Jaeger implementation, but it's sort of evolved since then. Internally, we use Jaeger, and then, the user span Gets translated into not spans that are emitted, but they get translated into a series of events. They get streamed to a teleworker.
So, a request comes through a worker, those spans get created, they get translated into a set of events I'll talk about in a second, and they get streamed as they're happening to a teleworker, and the teleworker can choose to do kind of whatever it wants with them.
And then one tail worker will, be listening to many different workers, which is why this can… this can scale.
So, it kind of works this way. When the worker kicks off, starts the request, it sends an onset event that will have some information about the type of request it is, it'll give the teleworker a trace ID, a span ID, and sort of implicitly create that root span, as well as say, hey, it's a fetch span, here's some headers, here's the URL that it's on.
And then the teleworker decides, do I want to… get this information, and it returns an event handler as an RPC target.
And then that worker, as it's executing, will just send… when you do console log, you'll get a log event. As you start a span, you'll get a span open, and you annotate it, and attributes, and so on.
This is what that looks like in code, Telstream is the handler for this version of the teleworker. We get an onset event, and then we return an array, an object of all the handlers we want.
We currently just have 9 events, Onset is when the worker kicks off. Return is when the user returns a response, so, like, returns a 200 status code. And then outcome is when the determination ends, as well as a handful of instrumentation events.
It should be noted that these are still very much in flux, and this isn't sufficient to represent all of OTEL. Like, you can't, rename a span, there's no way to do that yet. Set a span status, or create a metric. This is all work that we're going to have to do.
So when you, turn the feature on, you get a custom special teleworker, created by the observability… internal observability team.
And we take those events and we stitch them into OTLP, and then we send them off, or… Well, we've kind of run into the problem that if you have an OTLP payload per request, that is going to denial of service your, your, vendor.
So we do batching for the user. We have an existing log push pipeline that, does batching and has some configuration, and this was key to being able to ship, to ship this product at all.
the log push works natively with JSON, and so we were able to send the OTLP, payload as JSON, and then it has some, batching templating, abilities, which we were able to, correctly batch up OTLP, using this sort of, like, template. It's kind of a hack.
But it's a really mature service. It's been absolutely solid and given us no problems in production.
But, the user is limited right now to HTTP and JSON, and then we'll work on extending that over time so that we can also send Protobuf over gRPC. But for now, this is working for users.
So, just like you might have in a traditional server, you might have a sidecar or an agent. This helps offload performance impact from the worker. The worker isn't loading anything into memory, it's just streaming the data out, and that calculation's happening elsewhere. It also doesn't have to linger around and try and make sure that data gets sent off the way it might, on, naive's serverless implementation, or as serverless implementation as a library.
The runtime itself stays simple. Opentelemetry is, essentially just a custom worker that we ship.
And even if the worker itself crashes, we have these open spans that are sitting open in the teleworker, and so we don't lose those. You can still close those and send those off. You can mark them as erred.
Current version has some pretty sharp limitations. Getting out a product is really hard. We made some hard choices, in order to get this V1 out. So, we already talked about, we can only send, JSON over HTTP.
We only have percentage-based head sampling, and sampling is a larger topic, that is… keeps me up at night sometimes.
We're not doing automatic propagation. There's no real reason why we can't yet, except that we need to push the head sampling config down into the runtime, and it's currently ongoing to the teleworker. It also has implications for our users of Where do they make that sampling decision? If they're used to starting their trace on their internal services, and they have workers in front of it, then now they have to make that sampling decision before it gets to their backend, where they may have much less data.
So this is kind of a constraint that, we're not really sure how to work around quite yet.
We haven't added metric support, that's what I'm currently working on. It's hard to figure out where to aggregate all of that data in a serverless environment.
And then, currently, this all happens behind the scenes, and the user can't actually create their own spans or add their own attributes yet at all. This is… the next thing I want to work on, our hope is that we can support the OpenTelemetry API out of the box with no configuration. You import the OpenTelemetry API, you can get the current span, you can annotate spans, and so… I see this as a user progression. So, by default, the user turns it on, and for potentially the vast majority of users, that's good enough.
And then the users that are kind of further along that path are like, oh, I really need to know which… what the user is, then there's a simple, hey, import the OpenTelemetry API, add your annotations. And then for users that have more sophisticated requirements, maybe they want to set different sampling rates on different endpoints, things like that, then we'll probably have a small SDK for the front end.
So we're kind of building up an OTEL sandwich with our runtime in the middle.
our hotel experience, Honestly, I, like, writing this up, like, Austin asked me to write up, like, oh, what are the, like, problems that you ran into, and looking back and reflecting, it hasn't been a ton.
this, especially on launch, was a big success. We had, large name-brand companies, kind of come to us and just say, oh yeah, we turned it on last week. Now it's shipping to our Grafana, like, it works great. And then OpenTelemetry was never, was never a blocker in our development. Building out the tail worker, building out the UI and the query systems, adding instrumentation, especially into, like, a complicated C++ codebase. This all took a ton of time.
But, the tail worker that took these events and then turned them into OTLP was finished very early in the project, and then just… has just worked ever since.
We were able to leverage parts of OpenTelemetry JS, especially for, like, the OTLP generation, and that, and pull out some, like, modular parts of that, and that's been great. And, like, most of the complexity that we're facing is just sort of, like, inherent to the problem space. Like, there's no real way to make sampling a super easy thing.
And then the, just to harp on it again, the fact that OTLP has an option where you can just send simple JSON over HTTP was a huge, huge win for us.
A little bit, challenging because some vendors don't support it yet, but a lot of them have now started to do that in order to serve our users.
There weren't as many of these as, like, sort of challenges or problems that, That I thought.
Here's a fairly small one, is that, we get, sort of, N64s from the backend, and we get those translated into JavaScript as, big numbers.
But OpenTelemetry.js does not support those yet. I know that that comes from Opentelemetry.js needing to support browsers and things they did not support Big Num once upon a time, but it would be nice if it was added now.
This isn't a problem for us yet, but something that we have, sort of, like, in mind in the future, is that the OpenTelemetry API, this, the library, is fairly large. I think this is more of a problem on the front end, and I know this is being worked on, but, any improvements here would also benefit us, as well as we'd really like The future we'd really like is for the OpenTelemetry API to instrument the libraries that our users are pulling in, and for them to just get the benefit of that without them potentially even knowing that it's happening. If they import Next or Hono and get additional instrumentation about their routes, that can just show up in the dashboard, and they don't actually even need to know it's happening.
And then this is a little more of a fiddly one. I know I've complained to Austin about this, but, like, semantic conventions don't use units, which makes sense in the metrics use case, because you have the ability to encode a unit in that payload.
But that… but there's no equivalent for that for, span attributes, and so we have a handful of things where we're trying to follow semantic conventions, and the feedback we get from users is, what is this? Is this… is this nanoseconds, milliseconds?
seconds? Like, we don't know.
I think we can hard code the ones that we're generating, within the product, but it would be nice to be able to, maybe it would make sense to have… be able to attach an attribute that has a value with a unit attached.
I'm not sure how you would, necessarily solve that.
Here again is an attribute, HTTP response size is this… this is bytes, but how is the user supposed to know that? It's another thing that we could hard code.
And then these are not really open… not… from here on, these aren't really open telemetry challenges so much as just challenges that are sort of inherent in the space. But if OpenTelemetry has ways of helping us, then, especially I'd love to learn more about it.
We have this challenge of these strict backwards compatibility guarantees we want to provide our users. If we change an attribute, then… and users have set alarms on that, then maybe we have A thousand people being woken up in the middle of their night, because now their alarms are going off.
So we need to figure out some way of evolving these schema attributes, and that will probably be a version thing. We also want to follow semantic inventions, and some of these are going to… we expect that some of these are going to change out from UNDRUS, because they're still in development stage, and so it's just… it's just a challenge. It's also a challenge for our own instrumentation.
As I mentioned before, sampling is just hard. Originally, this was, there was no way to encode the sample rate in the… in the trace, but I think I missed some releases as I was making these slides, and found out there's some reading I need to do.
But it's still difficult when you make that selling decision at the edge.
if there's incoming trace context, this is gonna be challenging for us, because we can't statically know whether we should inherit it or not. And we'll… ideally, we can make this, we can establish the trace context, before the user code even runs, and so they can get, they can get instrument… they can get telemetry for things that happen before the worker even runs within Cloudflare, or things that may never invoke a worker at all.
And then users always have this very strong demand, hey, can we get telesampling? They usually have very little insight into the complexity of what they're asking for. It just sounds like a very simple problem to them.
given that we've taken on this challenge of, we want to have very good instrumentation for all of our platform, not all of our platform is actually easy to instrument. So here we have a workflow. You can, sleep for, like, 6 months. What does, like, you can't have a 6-month long span, in a trace.
I think this one is work… you can work around, but we also have stateful objects that have a life cycle. I think that these are probably more akin to, like, what you might… a stateful session you might see, like, in a browser session. Things that are happening over time, but it's not exactly the… the duration that you care about.
Rather the actions that are taken.
Or errors that may happen. And so… I haven't found too many examples for, what… what does a good instrumentation look like there. Another example is, WebSockets, which… I… if someone has a good example of instrumentation of WebSockets, please share that with me, because I think it's just kind of a really hard problem, especially given that there's no, headers, to send, information… pass information along.
And that's my presentation. I'm happy to answer any questions.
Tigran Najaryan 00:28:30 Jeremy, Tigran from Technical Committee here. This is brilliant, I love it, actually.
Great to see.
built-in instrumentation in any technology. I have a couple comments, questions. So, first, regarding the 64-bit integers, OTLP spec defines how to do that. You just encode them as a string, so it's there already.
You can do that, and the recipients are expected to treat it correctly.
Just… just to encode them as decimal, strings. That's all you need to do.
Jeremy Morrell 00:29:06 That… That is currently what we're doing. We… if we check the bounds of the integer, and then if it's above what we can safely represent in the JavaScript number, we encode it as a string.
Tigran Najaryan 00:29:15 Yeah.
Yeah, yeah, that's how protobuf defines JSON encoding, and we just refer to that. That's all you need to do. And by the way, do you only support OTLP in JSON format, so no protobuf in binary format?
Jeremy Morrell 00:29:30 Yeah, I mentioned that in my talk. That's something that we do want to support, but because we're… We would have to build that… that batching infrastructure, which has to work at… really, really high volume. We'd have to… we'd have to build that from scratch, and so that was a huge barrier to shipping V1. And so we're able to reuse our existing logging infrastructure, but we'll have to evolve that over time to support Protobuff.
Tigran Najaryan 00:29:53 Yeah.
Okay, okay, cool. And regarding the units, supposedly, the way that you deal with the units is the semantic conventions for the particular attribute, they define what the unit is, so it's not in the payload.
But if you're using a standard attribute.
Then you can go and look up the unit out of band, obviously, but it's not in the payload.
And, we know about this limitation, so there's a chat right now ongoing there, so maybe it's something we can do about it. Thanks for bringing that. But that's how it's supposed to work today, right? It's not in the payload, but you can find it out. You can go and look at the sameconf definition, which will tell you then what the unit is, essentially.
Jeremy Morrell 00:30:39 Yeah, but that becomes a problem for, say, like, our custom things. Like, we have a measure of CPU time, or wall time. If our user is sending that to a third party, then I have to go look up in our docs. It'd be nice if we could send that along.
Tigran Najaryan 00:30:53 Yep, yep, that's correct. Okay.
Cool.
Austin Parker 00:30:57 One thing… just to… I know you've got your hand up, Josh, but one thing to jump in there is one thing that we, would like to do, especially next year.
you start to promulgate the idea of federated SEMCOM more, and allow for imp… implementers to maintain their own semantic convention registries, so the fix in this case would be that Cloudflare publishes a schema of its semantic conventions that include the units, and then implementers would be able to go look those up.
And… and do everything. And then as you evolve your schema, you'd version it.
that version will be passed down in the OTLP payload, and then when… meal.
someone else's Gravana sees it, they would go and look it up, and they would handle the conversions. That's a… like, we have a lot of the tooling in place, or we're getting the tooling in place for that with Weaver.
Josh Suereth 00:31:52 So, Austin, I'm working on that right now, so that was what I wanted to talk about. So, yeah.
Austin Parker 00:31:59 Great lead-in.
Josh Suereth 00:32:00 Yeah, so basically, I don't know if you've seen our Weaver tool, but you can use it today. So, you can actually define all your schema in Weaver today. You can actually publish your schema today. You know how you were talking about migration? One thing I wanted to mention specifically about how do I evolve schema?
We have a thing where we can diff between version A and version B, give you the diff of what that schema is, and automatically generate, like, a conversion that says, here are the attributes I have to rename A went to B, that sort of thing. You can enforce policies that say, hey, across the team, all of your code should be generated by, generated by Weaver so it matches conventions, I can take an existing system, fire it at Weaver, and it will tell you whether or not you're compliant against the definition you have made for your company. So, if somebody adds an attribute but hasn't updated the official docs, you'll get an error, for example, right? That's called Weaver Live Check.
You can have your own custom policies, so if you wanted to have specific rules that you are enforcing, there's an extension mechanism to it where you can annotate the telemetry with your own annotations, like unit.
add it to the docs that you produce, and have enforcement, that sort of thing. So it's very flexible, we're working on federating. We have a preview that's coming out this week for what we're calling our V2 syntax, and so… Anyway, I would recommend that you look into OpenTelemetry Weaver, and I'm happy to help you. That's one of the projects that I maintain and drive. I'm on the technical committee, by the way. That's one of the projects I maintain and drive, and I think it's rather important. So… I also wanted to say that just overall, the work you're doing is awesome. This is in line with what I would expect, and I think you guys are really taking it seriously and doing some really cool stuff here. So, however we can support you, let us know.
the challenges you're having, you're not alone on. None of them were super surprising, but all of them are things that, if you want help with, or you want to help us work on, we should work on that together.
Jeremy Morrell 00:34:01 Yeah, I'm very interested in that. I haven't looked into Weaver too, too deeply, but all of the things that you were listing off there, like, yeah, those are… we'd have to build that otherwise, so I'm very happy to see that work.
Alolita Sharma 00:34:16 I think Josh is next. Josh?
Joshua MacDonald 00:34:19 Oh, hi.
Yeah, thanks. I guess we're just kind of, like, giving you feedback, and I also share the excitement that, Tigran and Josh had. Just as, like, nice to see, sort of a new initiative, like, solving the telemetry problems that actually… that you actually have.
The… the large part about… that you have about sampling, I think it would be great if you could come to a sampling sig, and we could just, like, lay out some of the work that's been done, both on configuration, about composability, and the basic specifications for, propagating sampling probabilities and stuff like that. We've got a handle on it, but it sounds like you could help us as well as we could help you.
Huh?
the… it was also really nice to see in your presentation, going back to the early days of OTEL, we called out this notion of a stateless SDK, and put some other requirements on the API around that so that it would be possible. It's nice to see you doing that. Like, the OTEL SDK for tracing was really meant to, like, let you fire and forget events, and not require you to keep expanded memory, and it's… it's good to see that happening. I think we should solve the long-lived span problems that you mentioned, because, like, that was always there, that was always going to be an issue, and, if you have a stateless SDK, like, every span is a long-lived span, essentially, so… I know that at least one issue has been opened, and there's been at least one conversation in the last year or so on this topic. We can look that up and sort of gather the interested parties. I think if you look at spans of logs, like, it's obvious what you want to do, it's just not clear how OpenTelemetry wants you to do it, so…
Jeremy Morrell 00:35:56 Millie and Brace had the suggestion for span snapshots. Is that the kind of thing you're thinking of?
Joshua MacDonald 00:36:00 Yeah, something like, like, hey, I wanna… I wanna send you a span that's unfinished, and I might send you another copy later when I finish it more, or something like that, yeah. But whatever works, like, I think you're on to the right idea.
The last piece of, I guess, optimism I wanted to give you is that, I think there's talk about Weaver and how we can change schemas, you know, I think it's… I'm starting to feel excited about the Hotel Arrow project with its data fusion-based engine. Like, I think we're going to be able to see, like, efficient telemetry translation soon.
Based on column-oriented translation and so on. So I think there's an opportunity to actually really start talking about schema variation and taking it ourselves seriously.
And that's all I wanted to say. I could say more, but I think we're busy here, so I'll take my hand down. Thank you.
Austin Parker 00:36:56 So, one thing I wanted to… well, first off, thank you for coming and talking about all that. I think it's… One, it's really… cool to see, and I think that it's… this is kind of the perfect example of what we, as a project.
really hoped more people would do, kind of take the ball and run with it, and get this sort of seamless integration for their users built on top of the standard. So, fantastic work you all are doing there.
One, one point you made about, you know.
Ural's vision or hope is that in the future, someone using Hono or Next, or whatever, we'll just be able to pull that in and… get these additional spans, get these additional, hotel data from it. You know, that's also definitely what we would like to see happen as well, and The design of OpenTelemetry is specifically built to enable frameworks, libraries, whoever, instrument with the Bayer API, and then they drop it into an execution environment that has an SDK, or responds to the… or that it implements the API, and then it just works. And I feel like you have the foundation here for that.
One thing that would be great for, you know, and… Cloudflare is a very big name here, and Cloudflare has a lot of people, so if there's ways that we can kind of work together as a project with people at Cloudflare to go and give that message to… the framework authors, right? To the authors of React, or Hono, or Next, or Nuxt, or Svelte… well, Svelte actually does this now. But, right, like, let's… I hope this is not just a one-and-done, and we kind of use this as a jumping-off point to… have Cloudflare and our sort of industry partners advocate for native adoption of OTEL and frameworks, because, as you said, it just makes the experience better for users.
Jeremy Morrell 00:38:58 I think that's something that we'd definitely be interested in.
Yeah, I remember seeing, in one of the conferences, someone asked a question, it seems like OpenTelemetry had sort of held back from pushing, library authors to do this, because… until semantic inventions were a bit more solid. Is that… Is that true, and is that still the case?
Are there any concerns about starting to push library authors down, Adding the… to adding these things because it might not match the semantic conventions or anything like that.
Josh Suereth 00:39:31 Yeah, I can take this one.
we… there's still a bunch of semantic conventions that are not stable, but I think we're at a point now where we know what we want semantic conventions to look like naming convention-wise. So if you look at the naming conventions in semantic conventions, and you see… so, first of all.
Take a look at stability, right? If you're relying on something that is unstable.
check the naming conventions of semantic conventions. We have a bunch of, like, how to write semantic conventions work.
That's been done. Lyudmila here might be able to speak more to, like, things that she sees, but from my perspective, there's a set of things that, we know what we want names to look like going forward. And if you match that with what you do yourself, and you match stable conventions, should be good.
If there are things that are unstable that you're nervous about, reach out to us and we can tell you how likely we think it is that they break based on those conventions.
But we are trying to get to a point very quickly that, you know, we can just greenlight all of this, and there's not a lot left. I'll give you context. The cloud semantics conventions right now have a lot of open… You know, hey, this isn't quite working right.
And there's a lot of people who are pushing on those. Those, I'm slightly nervous about. Database is actively being stabilized, and RPC is actively being stabilized. Database is done. RPC is actively being stabilized. You're seeing changes in RPC. So if you're doing RPC-related things, there are changes coming.
The changes that are coming, we kind of know the shape of them, so we can guide you there.
the rest to SENCOV, as we federate, will have less of a problem here, right? So, The guidance, the TLDR, stick to what's marked as stable, you should be totally fine. We're trying to rapidly get more things marked as stable.
And, the naming conventions are the thing that we've really built up over the past 3 years, now that those are stable. You stick to those naming conventions, and you'll match what we do. So, you'll be able to kind of fit into this ecosystem.
Are there still, like, minor concerns? Yeah, but, like, for a lot of major things, I'm not as worried. Especially since, if we think about your instrumentation and what you're doing, there's a class of metric that you're going to produce that only you can produce.
That metric semantic conventions will never touch. You are the owner of that definition, you should be the owner of that definition. Your company should be the owner of, here are the metrics we produce for our users, and we're going to keep them stable.
Our goal is to give you tooling to make that easy for you to do.
But we don't want to own your metrics, like, when it comes to that. What we want to own is, if you're producing metrics that look like HTTP, and you want to reuse dashboards that are general purpose across the ecosystem, great, we'll do that. But there will be things that are specific to your implementation that people need.
From an observability standpoint, to solve problems.
you should feel free to define those and own those, and those will never be, like, a SEMConf thing, there will always be a, your implementation needs this thing. Does that make sense?
Yeah, we call it a T-shape. So, the T is the general purpose stuff.
That, pay attention to SemConv, take stable. Anything in the deep part, where it's, like, specific to you.
Do what you will, we just ask you keep it stable for your customers, right?
Austin Parker 00:42:58 And I, I…
Jeremy Morrell 00:42:58 Michael.
Austin Parker 00:43:00 Yeah, and I also think, like, a lot of the work, you know, that Josh was talking about with Weaver.
And… having better tooling and ways to evolve schemas in SEMconv.
falls into this as well, right? If we can make it… If we can provide the community broadly, and our implementers and everyone, ways to safely evolve schemas and evolve semantic conventions, then hopefully a lot of this anxiety goes away.
Alright, I think we have some other business to take care to talk about today, so if there's no other questions, Jeremy, how can folks, get in touch with you?
Jeremy Morrell 00:43:43 I am on Blue Sky.
Austin Parker 00:43:48 I was gonna say, if you wanted to, you can also, We can put, like, an email address or whatever in the meeting notes, if… Sheridan.
Jeremy Morrell 00:43:55 Yeah.
Austin Parker 00:43:55 I don't want to put it on the recording.
Jeremy Morrell 00:43:58 no, my email is just jmorell at cloudflare.com. you can also follow me on Blue Sky, tweet, like.
I'm around. I also have my website, jeremyMorel.dev, there's all my contact info there.
Austin Parker 00:44:13 Alright.
Well, thank you so much. Again, wonderful presentation, and really excited that you all did this, and that people were using it, and it's, again, just a real testament to, I think.
the, the vision… working, so… We appreciate, appreciate you taking your time today.
Jeremy Morrell 00:44:37 Awesome. Thank you, thank you guys so much.
Right.
Austin Parker 00:44:40 Take care.
Alolita Sharma 00:44:42 Thank you. Bye.
Austin Parker 00:44:48 Alright, and next up, we have KubeCon EU.
Severin Neumann 00:44:57 Yeah, I added that in to just make sure that we don't lose track of that, because I think Pablo took care of a lot of that already. I think there's a deadline coming up in a few days.
Alolita Sharma 00:45:08 Yeah, this is the Maintainer Summit, deadline.
Severin Neumann 00:45:12 Yeah, and the maintainer track as well. I think both of them have a deadline on Sunday.
Alolita Sharma 00:45:16 Yeah.
Severin Neumann 00:45:17 So… we still have, like, to talk about, Contrip Fest.
Then the question is like, do we want to submit more maintainer talks, track talks?
Pablo Baeyens 00:45:28 What about the lightning talks, and then…
Severin Neumann 00:45:30 Yeah, do we need a booth, or will we have a… observatory, right? And then Maintainer Summit is its own topic.
So maybe we can quickly go through those.
Do we want to… Submit a contract fast, anybody wants to… To raise their hand for Dan.
Morgan McLean 00:45:49 I assume we do want to submit it. We talked about this, I think, when we were in Atlanta, but we haven't… we did not do one in Atlanta. I think we're due to do one in Amsterdam then, right?
Severin Neumann 00:46:00 Yeah.
Morgan McLean 00:46:01 Yeah.
Severin Neumann 00:46:02 I think we, again, need the staffing for that, like, 4 or 5 maintainers or something like that.
Austin Parker 00:46:10 Would Weaver be a good choice for a trip fest?
Alolita Sharma 00:46:15 That would be pretty cool.
Josh Suereth 00:46:20 Actually, with the demo Jeremy just had, what do you think, Lydbilla? We could do a Troopfest on that thing.
Alolita Sharma 00:46:27 Oh, that would be awesome.
Liudmila Molkova 00:46:29 We could do a bunch of things, yeah, and I will be there.
Alolita Sharma 00:46:33 I'll read it.
Liudmila Molkova 00:46:34 that NA can help this country fast.
Alolita Sharma 00:46:41 Yep, I can help too.
So…
Liudmila Molkova 00:46:45 We can also do MCP stuff, which people are excited about. Not sure if we take the contributions to where we would put them.
Austin Parker 00:46:52 Actually, yeah, let's do that. I'll…
Alolita Sharma 00:46:56 Community repo? We could do it there.
Austin Parker 00:46:58 Well, yeah, I can do a… I can submit something for, like… with Pavel, I guess, about, MCP and just, like, AI hackathon.
AI plus hotel.
Alolita Sharma 00:47:13 Yeah, I think that's a great idea.
Pablo Baeyens 00:47:16 Will you take care of the submission, then?
Austin Parker 00:47:19 Yeah, I'll take care of it.
Alolita Sharma 00:47:24 Awesome. And do you want me to put the, maintainer summit, session together, I'll share, then.
Austin Parker 00:47:34 Yeah.
Alolita Sharma 00:47:34 hear that right away.
Austin Parker 00:47:36 Do we… do we know… The one question that we had from Atlanta is, there were two separate maintainer track session submissions, and I don't think we've ever figured out who the other Like, one of them…
Alolita Sharma 00:47:51 It was, They sent the names, Austin. It was, Tyler, Jan, and some of the other folks.
Austin Parker 00:48:02 Oh, okay.
Alolita Sharma 00:48:03 submitted.
Austin Parker 00:48:04 Well, I assume if it happens again, they'll merge them again, so…
Alolita Sharma 00:48:08 Yes, yeah, yeah. They're usually pretty good about that.
Austin Parker 00:48:11 Okay.
Pablo Baeyens 00:48:12 So… Sorry, I lost track of it. What are… what is Hello Leads I'm going to submit?
Alolita Sharma 00:48:18 Pablo, this is… which, which part? I was talking about the Maintainer Summit.
Pablo Baeyens 00:48:25 Inner Summit, okay.
Alolita Sharma 00:48:26 Yes.
Pablo Baeyens 00:48:27 in between your summit.
Alolita Sharma 00:48:29 Yes, that's right. I was just going to compose the.
Austin Parker 00:48:32 Right.
Alolita Sharma 00:48:34 Title session, share it with you guys, and then submit it.
Austin Parker 00:48:37 Yeah, and I know there's a request for a specific Prometheus plus hotel maintainer meeting.
Pablo Baeyens 00:48:46 Yes. Yeah, I can take care of that with Arthur, if everybody's okay with it. I put a link to the, blurb that Arthur wanted to send. This would be, like.
Austin Parker 00:48:57 My…
Pablo Baeyens 00:48:58 meeting from…
Austin Parker 00:48:59 Yeah, my take is, if that doesn't get… if they don't accept that due to, like, lack of rooms or whatever, we should still try to have it, and…
Alolita Sharma 00:49:07 Yeah.
Austin Parker 00:49:08 We can just get a meeting room at a nearby hotel or something.
Alolita Sharma 00:49:13 Can we… can we even, do a BOF, maybe? Because they usually do have allocations, for BOF rooms.
Austin Parker 00:49:22 They do, but those are… Like, they figure those out.
Like, there's a voting thing for that, like, they figure it out ahead.
the s… Maintainer Summit itself, and it's… you know, pretty biased towards Kubernetes, and…
Alolita Sharma 00:49:38 Yes.
Austin Parker 00:49:39 good stuff.
Alolita Sharma 00:49:41 Yep.
Austin Parker 00:49:41 Let's just submit it… I'm fine.
Morgan McLean 00:49:44 I was gonna say, I'm sure we can find a location for it, even if it's not.
Alolita Sharma 00:49:46 Expected.
Morgan McLean 00:49:47 on the books thing, there's usually.
Austin Parker 00:49:48 Right, like, we can… I'm confident that we'll submit it, and then if they don't accept it, then we'll… we'll… We'll put our.
Alolita Sharma 00:49:57 I'm confident we can figure it out, yeah.
Pablo Baeyens 00:50:00 So then I'll… I'll tell Arthur to submit it.
Alolita Sharma 00:50:04 Okay, babe. Good.
Austin Parker 00:50:08 Alright, anything else on KubeCon?
Morgan McLean 00:50:12 I think someone mentioned the observatory, I think Austin, you and I had chatted, so there's the new project booth layout.
Tables, or something like that, so we're gonna do that instead.
Austin Parker 00:50:23 E.
Yes, I think we're… I think… Let's… let's talk about it, async.
Morgan McLean 00:50:31 Okay. Yeah, I've told my folks for now to not do the observatory, but if we want to do it, I need to know very, very.
Austin Parker 00:50:36 Yeah, I think the thing is, is that you have to sponsor the maintainer summit to get the big table.
Morgan McLean 00:50:42 Oh…
Austin Parker 00:50:45 Yeah.
Morgan McLean 00:50:45 Project Pavilion? Oh…
Austin Parker 00:50:47 Well, if you want, like, the big table next to it, I don't…
Morgan McLean 00:50:51 Alright, let me, yeah, let's chat.
Austin Parker 00:50:52 I'm also… I'm also, like, I've… my thinking has somewhat flipped on this, and I kind of want the observatory again. Well, it's just like, I want everything. I would like for us to do everything. The problem is, we really do need, like.
Alolita Sharma 00:51:05 More folks.
Austin Parker 00:51:07 The pro- yeah, like, it's… I don't know. Like, the observatory is good, but I think it… it's good at getting us together, but it's bad at, like, getting other people in.
Morgan McLean 00:51:17 Yeah, agreed.
Austin Parker 00:51:17 people? Right, so we need… both, I think, so I'm wondering if the better thing is, like, maybe we spend those… have that sponsorship dollars give us, like, the bigger table next to the project pavilion? I will DM someone, but let's talk async about it.
Morgan McLean 00:51:32 Okay, perfect, yeah, just let me know what you want to see.
Austin Parker 00:51:35 Yep, will do.
Severin Neumann 00:51:37 Last item is the Lightning Talks, do we… I think we did… didn't do one in North America, right?
Alolita Sharma 00:51:44 No, Windows.
Austin Parker 00:51:45 We didn't, but I…
Severin Neumann 00:51:47 Are we able to do one, or can we just skip it?
Austin Parker 00:51:51 I mean, I don't…
Alolita Sharma 00:51:53 Can we submit it still?
7?
Severin Neumann 00:51:56 Yeah, the Project Lightning talk, I think, is also due on… Sunday, Sunday, right?
Austin Parker 00:52:01 I would really… I think it would be really good if we could have a… if we could put the call out to SIGS.
Alolita Sharma 00:52:08 Yeah.
Austin Parker 00:52:08 that.
Alolita Sharma 00:52:09 Yo.
Severin Neumann 00:52:12 Yeah.
Morgan McLean 00:52:13 It appeared to have fairly good attendance in Atlanta this time.
Austin Parker 00:52:15 There's a ton of people that show up for them.
Morgan McLean 00:52:17 Yeah.
Severin Neumann 00:52:17 Should we say maintainers submit lightning talks, like, there's a lot of people there and something.
Austin Parker 00:52:23 Yeah, just be like, hey, you know, do you want 5 minutes to talk about, like.
JavaScript Auto Instrumentation, or OBI, or whatever, like…
Severin Neumann 00:52:34 Okay.
Yeah, that makes sense.
Alolita Sharma 00:52:37 So, Severin, you'll.
Severin Neumann 00:52:39 I send out a to the maintainer channel for that. Okay. Awesome. I will double-check on the requirements, but my understanding was, like, yeah, we can… one speaker per project, lightning talk, whatever. Yeah, I will figure that out.
Austin Parker 00:52:55 Yeah, we'll just… Yeah, have people do a good job, and we'll just see where the chips fall.
Severin Neumann 00:53:04 They don't give passes for those, right? So, just…
Austin Parker 00:53:06 I… yes, I think you have the… be attending.
Alolita Sharma 00:53:12 Yeah, I don't think they give passes.
Love that.
Austin Parker 00:53:18 So we have 10 minutes… is that enough time to talk about Kotlin?
Alolita Sharma 00:53:24 Meow.
At least let's get started.
Austin Parker 00:53:37 I know Carlos isn't here, but does anyone have the TC… Familiar with this one, Say a few words?
Alolita Sharma 00:53:50 Carlos dropped off, so…
Austin Parker 00:53:53 Yeah, I think he mentioned that…
Jack Berg 00:53:57 What do we want to talk about besides what's in the document?
Severin Neumann 00:54:00 I… I think mostly next steps, right? I mean, like, are we… can we, like… like, it's… it's… it's waiting for whatever next steps for a few weeks now.
I was just wondering, like.
Why it is stuck, and then what is necessary to… to move on with that.
Jack Berg 00:54:23 So the TC, if my understanding is correct, Carlos did the technical due diligence, we discussed it in a variety of TC settings, we got some feedback, we iterated on it, and, you know, we're at the point where we're handing it back to the GC with a recommendation to proceed.
You know, with the caveats in the document.
Austin Parker 00:54:44 Okay, and those caveats are down under the…
Jack Berg 00:54:47 It's just, like, the normal types of caveats, like strip vendor code and, like, you know, all the things in the document. There's nothing that's particularly interesting.
Austin Parker 00:54:59 I think it looks good… do we have Quorum?
Alolita Sharma 00:55:07 Yes.
I think we do.
Did we raise our hands?
Austin Parker 00:55:15 Yeah.
Alolita Sharma 00:55:16 Yeah.
We have everybody's hand up.
Austin Parker 00:55:23 Alright, that's…
Alolita Sharma 00:55:24 Okay, cool.
Austin Parker 00:55:25 Passes. Alright, we will accept it. So… so who's running this on the GC side?
Alolita Sharma 00:55:36 I think Severin was…
Austin Parker 00:55:38 with you, Severin?
Alolita Sharma 00:55:40 I… I was just asking the question, I think Dan…
Austin Parker 00:55:45 Oh, that's what my… yeah, that was my concern that Dan was driving this. Who wants to pick it up?
Severin Neumann 00:55:54 I mean, if nobody volunteers, I can, like, at least let them… Marilla, how's your plate looking?
Marylia Gutierrez 00:56:01 Yeah, I can… can help us.
Alolita Sharma 00:56:03 Yeah, good.
Austin Parker 00:56:04 Okay, maybe, like, Severin, you and Marilla work together, just because I think this would be, Marillia, your first time doing a… Shepherding one of these?
Severin Neumann 00:56:14 Okay.
Austin Parker 00:56:15 Okay.
Great. Love the smell of progress in the morning.
Good, very good.
Anything else in the last 5 minutes?
Alolita Sharma 00:56:35 Okay, good. Do you have a plan?
Austin Parker 00:56:42 I think this is our last meeting for the year, am I right? Because we are going into…
Morgan McLean 00:56:48 The combined group, yeah, I'm pretty sure.
Austin Parker 00:56:50 This is the class combined one, yeah.
Morgan McLean 00:56:52 Yeah.
Alolita Sharma 00:56:53 I think we have one more next week, right?
Austin Parker 00:56:55 Yeah, next week we have GCE.
Morgan McLean 00:56:57 That's a GC dope, yeah.
Pablo Baeyens 00:56:59 I have a topic, maybe more GC, but, there's, the Linux Foundation Mentorship Program, the next round opens in a month.
So January 7th to January 20th would be… I… Don't know… I guess Individual 6 can send project proposals, but I don't know, like, is it cool if I share this on Auto Maintainers to…
Austin Parker 00:57:27 Yeah, also.
Alolita Sharma 00:57:28 Oh, yeah, yeah.
Austin Parker 00:57:29 Jurassi, because I believe Jirasi has done this before.
Alolita Sharma 00:57:32 Yeah, Jurassi has definitely done it, and I have also helped mentor, so… Pablo, definitely share it on the Maintainer channel, and Different maintainers can, you know, one person can submit, or we can have multiple proposals.
Pablo Baeyens 00:57:51 Okay, I'll… I'll do that then.
Alolita Sharma 00:57:55 Yeah. Typically, the more, you know, folks we get, the better it is for different sigs.
Cool. Very cool.
Austin Parker 00:58:09 Wow.
Alolita Sharma 00:58:11 Let me know if you need help, Pablo, I'm happy to help you.
So…
Pablo Baeyens 00:58:15 Droop.
Yep.
Austin Parker 00:58:17 Yes.
Have a happy holidays, Merry Christmas, Happy New Year, all that good.
Alolita Sharma 00:58:21 Totally.
Austin Parker 00:58:22 Take a break, enjoy the break.
Alolita Sharma 00:58:24 Yes.
Austin Parker 00:58:25 Stare at a different screen?
Alolita Sharma 00:58:27 Different screen.
Morgan McLean 00:58:29 Or different things on the same screen.
Alolita Sharma 00:58:31 Exactly. Turn the bad screen off, turn the good screen on. Yes.
Morgan McLean 00:58:36 Exactly.
Liudmila Molkova 00:58:39 Write code instead of talking on Zoom.
Alolita Sharma 00:58:42 Yes. Yeah, right?
Austin Parker 00:58:43 Do some actual work instead of just meetings.
Alolita Sharma 00:58:46 Use cloud more.
Tigran Najaryan 00:58:50 Happy holidays, everyone.
Alolita Sharma 00:58:51 Yeah.
Austin Parker 00:58:52 Hey, and it's, you know, hey, 2025, been a heck of a year.
Alolita Sharma 00:58:58 Yes, absolutely.
Austin Parker 00:58:59 It's been a heck of a year for hotels, so…
Alolita Sharma 00:59:01 Next year, next year, graduation. Yes.
Austin Parker 00:59:04 Yeah.
Severin Neumann 00:59:05 Good.
Austin Parker 00:59:05 Definitely. 100%.
Liudmila Molkova 00:59:09 Next year, a placeholder.
Josh Suereth 00:59:12 When do we get to wear a cap and gown? That's what I want to know.
Alolita Sharma 00:59:16 Yes, we totally… I'm thinking, no, that's an idea, Austin. Cap and gown, for now.
Austin Parker 00:59:25 No, we've already, we're already committed. We're gonna do soccer jerseys for.
Alolita Sharma 00:59:31 But you…
Austin Parker 00:59:31 next KubeCon. Okay.
Everyone, everyone loved the, the baseball jersey so much, so…
Morgan McLean 00:59:39 Yeah.
Alolita Sharma 00:59:40 Soccer is awesome, soccer is cool.
Austin Parker 00:59:43 Yeah, I'm hoping we can… we just need to convince all the vendors that they also need to do, like, soccer balls, and so we can have, like… A whole… whole gimmick.
Alolita Sharma 00:59:53 Oh, that'd be nice.
Austin Parker 00:59:54 Perfect, because next year's the World Cup!
Alolita Sharma 00:59:56 Welcome!
Austin Parker 00:59:56 Nobody can come to in the rest of the world.
Morgan McLean 00:59:58 Open telemetry soccer hooligans.
Austin Parker 01:00:01 Yeah, right? Like, we can… we'll… we'll do… we can do the… the scarves? That's what they do, right? In soccer? Yeah. The scarves? Yes.
Okay.
Alolita Sharma 01:00:10 The scarves.
Fostom actually does a very nice one, every year as a shrag.
Austin Parker 01:00:17 Yeah. It'll be great, no, yeah, 2026 is the year of hotel soccer.
Morgan McLean 01:00:21 Exactly. Cool.
Austin Parker 01:00:24 Alright.
Morgan McLean 01:00:25 Alright. Happy holidays, everyone. See ya.
Armin (Dynatrace) 01:00:27 Holidays, all. Cheers.
Alolita Sharma 01:00:28 Yeah, bye.
Bye. Happy holidays. Bye!
