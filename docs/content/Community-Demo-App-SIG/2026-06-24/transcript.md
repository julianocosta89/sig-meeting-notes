SIG: Community Demo App SIG
Date: 2026-06-24
Duration: 29 minutes
============================================================

## Zoom Recording Transcript

**Juliano Costa | Datadog** 00:55 Hello, hello.
**FELIX GEORGE** 01:03 Hi, how do you, Dennis.
**Juliano Costa | Datadog** 01:07 Are you?
**FELIX GEORGE** 01:09 I'm good. Thank you, and for you.
**Juliano Costa | Datadog** 01:16 Also good, yeah, busy day.
We're good.
Let's, give them a two, but, I think we can… We think we can start talking about, the PR.
**FELIX GEORGE** 01:43 Yeah.
**Juliano Costa | Datadog** 01:45 regarding the IPv6 thing, I think the other two services work?
It was just one that crashed, right?
**FELIX GEORGE** 01:58 Yes, I think… no, I saw… I think it was just the one. I think it was just the one. Yeah. But I reverted the whole thing back.
**Juliano Costa | Datadog** 02:09 I googled a bit, and I don't know, actually, why it's not working, but, I saw an issue open in 2024 about radio not supporting IPv6.
But, actually, Google gave me the answer that it supports, and the suggestion that Google gave me was exactly the same that we had in the PR. So, I don't know.
But, let's get this one in, and then we can figure that out later, because it is already… more than 2 months that you have this PR open. Well, not this one, this one, but yeah.
**FELIX GEORGE** 02:53 Yeah, kind of, yeah.
**Juliano Costa | Datadog** 02:56 Yep.
I tested locally. I… Yeah, it… It worked.
So…
**FELIX GEORGE** 03:11 It's okay.
**Juliano Costa | Datadog** 03:14 Played around, and .
**FELIX GEORGE** 03:16 Something else.
**Juliano Costa | Datadog** 03:17 To be fair, I haven't played with… I haven't played with, the actual key.
**FELIX GEORGE** 03:31 Beautiful.
**Juliano Costa | Datadog** 03:31 Just with the cash.
**FELIX GEORGE** 03:32 Yeah.
**Juliano Costa | Datadog** 03:33 So… but I'm happy with that, because I think that's how most of the folks will actually use. I don't think people will spend tokens on, playing around with the demo.
**FELIX GEORGE** 03:46 Yeah, so I was thinking that, when I add the load generator for agent as well, so I will be adding more caches for, at least two, two models.
Like, GPT 5.5, or Cloud of Buzz 4.82, you know?
whatever is out there at that time. So, I think if I can add that, people can just use our facilities, right, with the existing Yeah.
**Juliano Costa | Datadog** 04:15 Yeah, my main concern, and I think one thing that I asked for input from maintainers, was the… the trace loop thing.
**FELIX GEORGE** 04:32 Yeah.
**Juliano Costa | Datadog** 04:33 You… you already gave the… the… the reason why you are using Traceloof, but, Yeah, that's my only… That's my only thing here.
**FELIX GEORGE** 04:48 Okay.
**Juliano Costa | Datadog** 04:49 Where is the…
**FELIX GEORGE** 04:50 So, so, for example, one of the… one… the agent, uses the StormyShop application as tools, right? Or the other microservices as tools. So, and, the agent talks to them using the MCP, in the MCP mode.
In the default mode, you can use it like the normal HTTP or default Langraph tools, but MCP is something that's out there, and everybody is using it, so we wanted to have availability as well. So that's why I added MCP.
Am I… Okay.
**Juliano Costa | Datadog** 05:26 But, you'.
**FELIX GEORGE** 05:26 My network, okay? Are you guys able… oh, okay.
**Juliano Costa | Datadog** 05:29 Yeah.
**FELIX GEORGE** 05:30 That was funny.
**Pierre Tessier** 05:30 Can you repeat your last 30 seconds or so?
**FELIX GEORGE** 05:33 Okay, let me just… I changed it to a different room. Okay, sorry, yeah. So what I was trying to say was, the MCP server instrumentation is not implemented yet in OpenTelemetry.
Because of that.
That's why I used, Traceloop, and I was the one who added the MCP instrumentation in Traceloop, so, just because I know that it exists in there.
**Juliano Costa | Datadog** 06:03 Yep, I…
**FELIX GEORGE** 06:04 We can, we can change. Yeah.
**Juliano Costa | Datadog** 06:07 Yeah, exactly. I think that's a good, good point, like, we can… update as hotel matures, and we can also use the demo to showcase what is out there to date.
I'm good with it. I just wanted to hear the other maintainer's opinion, because, yeah, I… I don't like taking, taking, sold decisions.
And we have, Shenoi back, here, live, so maybe I'll just double-check with him.
If he has any… Any… thoughts on that, and… But the PR looks good to me, and if he agrees, and We are good. I'll hit the… I'll click the merge button.
**Shenoy Pratik Gurudatt** 07:07 Hey, hey, hey, sorry I joined late.
Were you talking about the agent thing?
**Pierre Tessier** 07:14 We are.
**Juliano Costa | Datadog** 07:14 We were… we were waiting for you.
**Shenoy Pratik Gurudatt** 07:20 Yeah, I took a look, last week, and it's in a much better state.
I think I'm good for now. Is there any, particular thing that you wanted to discuss, Juliano, or…
**Juliano Costa | Datadog** 07:34 There, there was one thing on the… on the usage of TraceLoop, but, yeah, I think… I think we are good on… having that… S… kind of a… while the hotel matures, and with that, we can also show how people are using trace loop with hotel semantics, or trace loop with trace loop semantics to… to get, Visibility and stuff.
**Pierre Tessier** 08:09 I think it probably makes sense that… as OpenTelemetry matures, and if OpenTelemetry creates deeper.
integrations here within the SDKs itself.
We should migrate to those.
**Juliano Costa | Datadog** 08:20 Instead.
**Pierre Tessier** 08:22 And we should probably have an issue just mentioning that and tracking that, just so it exists in the ecosystem, because every once in a while, people come in.
And they look for issues that they could work on, and You know, so… and that's all I'm saying. It'd be great, just like, to close a loop on TraceLoop, pun intended, is let's get an issue just to track it.
**Shenoy Pratik Gurudatt** 08:46 I, what I was thinking is, to showcase Traceloop with the GenAI normalizer, processor.
in the collector. That way, what it becomes, like, we have these external SDKs that were there before OpenTelemetry had its own.
And then if you are already onboarded to those, how you can use the GenAI normalizer and still get very close to the GenAI semantics and semantic conventions there.
This is one of the showcases, and we still have one, either agents or MCP with, manual instrumentation with the SDK.
So that way, we have two examples in the demo.
Was my thought process there.
**Juliano Costa | Datadog** 09:31 That's actually cool, and it also showcases another component on the hotel system. I like it. There is one thing also that I want to bring up, I don't know how much of you, how much you all are following, but Open Inference, proposed a donation of their their instrumentation libraries, so maybe we'll have something soon in hotel, whenever… well, if that's accepted, immersed in, then…
**Pierre Tessier** 10:04 All it'll mean is that we have to change semantic conventions twice, Giuliano, but it's okay.
Once… as soon as they drop the implementation, and once again, when they finalize implementation. But that's okay.
**Juliano Costa | Datadog** 10:18 Well, we need to just find the time that we spend on the demo, right?
But, back to the… back to the serious work, I will merge when ready, when ready.
the MCP agent and chatbot.
And I think that was the last big rock, right? No, actually, we still need a cleanup before the 3.0 release.
Removing the product reviews, and removing the… tele… not the telemetry tests from Chennai, but the telemetry tests from the.
**Shenoy Pratik Gurudatt** 11:04 Yeah, I'll have a PR for that tomorrow. I have something that I'm working that's in progress.
For the removal part.
Let me get that, raised up tomorrow. We can merge it, and should we just delete, delete, delete stuff. Clean up questions.
**Juliano Costa | Datadog** 11:20 Okay.
I will… so, okay, so I can take care of the product recommendation.
Oh, man.
Yeah, the removal of the service is fine, the change on the UI is not.
But yeah, Cloud can do that for me, I think. Hopefully. If not, I'll ask Codex.
If not, don't beg someone's.
**Shenoy Pratik Gurudatt** 11:49 You can sometimes threaten Claude that if you don't do it well, I'll use Codex, and it does better.
**Juliano Costa | Datadog** 11:56 Perfect.
Okay, yeah, so, I will take notes on that. Let me open the CVT notes here.
Do we have two agendas for today?
You are on mute, Pierre.
**Pierre Tessier** 12:36 Sorry, I copy-paste, forgot to change the date.
**Juliano Costa | Datadog** 12:43 Yeah, it's 24, yeah, okay, okay.
**Pierre Tessier** 12:46 Crazy, yeah, sorry.
**Juliano Costa | Datadog** 12:49 I was like, is it today, today, or what is this?
That was…
**Pierre Tessier** 13:05 Okay…
**Juliano Costa | Datadog** 13:09 Felix, do we have any, have you started, something on the docs part of that?
**FELIX GEORGE** 13:18 Yeah.
**Juliano Costa | Datadog** 13:18 Okay.
**FELIX GEORGE** 13:19 I just started.
**Juliano Costa | Datadog** 13:22 Awesome.
Yeah, and again, really appreciate your patience on that. I know that it took a while, and it was a lot of back and forth, and thanks, Shanai, for all the the reviews.
**FELIX GEORGE** 13:37 What's it?
**Juliano Costa | Datadog** 13:39 I just arrived now, so… Appreciate that.
**Pierre Tessier** 13:49 Okay, so… we still need a PR to remove product reviews, or the GenA part of that, I guess, right?
**Juliano Costa | Datadog** 14:05 We're gonna remove the whole thing, right?
**Pierre Tessier** 14:07 The whole thing, the whole service, yes. Because now we have this, yes, sorry, because it's… And we're gonna remove, The tests, the old test.
Trace Test, whatever it was called.
Oh my god, thank you.
And then just one more general pass cleanup, and we're ready to do a 3.0?
**Juliano Costa | Datadog** 14:32 Yep.
**Pierre Tessier** 14:34 Oh, man. I mean… It's exciting.
**Juliano Costa | Datadog** 14:35 Yeah, it is. I'm not excited to… I'm not looking forward to the Helm PR, but I'm excited.
**Pierre Tessier** 14:43 I, I… yeah, yeah, yeah, I think we can… like, we could fast follow the Helm PR. Let's get 3.0 out the door.
work on Helm PR.
And, I'm sure we'll get a bunch of issues, and that's okay. We'll just have to know how to respond to those issues quickly, say, we're on it, we're working on it, just give us a couple more days.
**Juliano Costa | Datadog** 15:06 Yep.
**Pierre Tessier** 15:07 It is gonna be a big PR, and I would rather have a full release out there than us trying to use these janky images that we have built somewhere else.
**Juliano Costa | Datadog** 15:13 Yep.
**Pierre Tessier** 15:15 okay.
**Juliano Costa | Datadog** 15:20 Why don't… One thing that I want to bring up is… So… Peter has, helped a lot with Dependabot and a bunch of, GitHub actions that, automate a bunch of stuff, which is great.
But now we have most of the services up to date.
To the latest version.
And… in a real, or… in a production, in most of the production environments, we don't have everyone using Java 24, and everyone using, latest Node.js.
**Pierre Tessier** 16:03 Hmm.
**Juliano Costa | Datadog** 16:03 should we configure things to have, like, one services on the latest, one other Java services running on Java 8, and then, like, just to have those realistic, examples, and then we need to, of course, configure… Depending on what to bump that dependency, but not the major dependency, not the major version, just the minor.
**Pierre Tessier** 16:35 Just a minor on it.
**Juliano Costa | Datadog** 16:37 Does that make sense.
**Pierre Tessier** 16:40 Can these be… now that we have Docker profiles, or the layered way of doing Docker, can we make this, like, an add-on something somewhere, somehow?
or make it commented out, and they add, like, add these on afterwards, and they are just all a bunch of very basic services that read off of Kafka, do a thing.
And then… dump off.
But they're 100% optional.
**Juliano Costa | Datadog** 17:11 I… actually don't know, because we've… We would need to change the base image.
So the service, the Docker image of the ad service will be built on Java 24.
**Pierre Tessier** 17:30 No, no, I mean we build music.
**Juliano Costa | Datadog** 17:31 Preston.
**Pierre Tessier** 17:32 We build new services, completely new services, when, you know, make up names for them.
But we call them out, like.
old Java, you know, or, you know, like, special services shipping, Old Java 8.
You know what I mean? That's the service name or something like that, so it's really obvious. Hey, this is your old service, but it's off by default.
It's just, it's hanging out there. It does basically nothing except from reading from Kafka. It posts that it processed the order.
And then it closes.
Right?
Maybe tries to write a file, or read a file, or something like that.
I'm just trying to think of a way that we could do this, and we could support various old flavors of things, like, because I'm sure somebody's gonna want an old node version, and somebody's probably still running Python.
I don't know, 3-3, or 3-2, or something like that, right?
And we're gonna want to see a couple different services that do that, so can we just… They all read from Kafka?
**Juliano Costa | Datadog** 18:37 I think so, yes.
Yup.
**Pierre Tessier** 18:46 Without bloating our demo.
**Juliano Costa | Datadog** 18:49 Yeah, no, the… the… my suggestion here wasn't actually… Adding more stuff would just be… So, because we have, currently we have different services, on… Let me open the Hotel.io for a sec.
We have different services written on the same language.
**Pierre Tessier** 19:14 Yeah.
**Juliano Costa | Datadog** 19:15 For instance, Go, we have checkout product catalog.
net, we have Accounting EndCart.
Python, we have a recommendation, well, only a recommendation, because the product reviews is gone… will be gone.
Well, we have low gen in Python as well.
Java, we have ad service… The other, fraud detection is Kotlin.
Yeah.
**FELIX GEORGE** 19:45 The new 3 are in Python.
**Juliano Costa | Datadog** 19:49 Yeah, exactly. We have 3 new Python services, so… Not all of them are instrumented.
Party.
**FELIX GEORGE** 19:59 Of course, all of them are in Toronto.
**Juliano Costa | Datadog** 20:01 Oh, okay.
**FELIX GEORGE** 20:03 By instrumented, you mean traces, right?
**Juliano Costa | Datadog** 20:06 Yeah, yeah.
**FELIX GEORGE** 20:07 Yeah, yeah, a lot of them are.
**Pierre Tessier** 20:12 I think it covers us for Python. I was thinking more like Java, for what it's worth. Java and .NET.
And I know .NET, we have two of them, but .NET, I think we already sliced them different ways, like, one of them's an agent-based, and the other one is, Code-based instrumentation.
**Juliano Costa | Datadog** 20:27 Yep. Go ahead.
**Pierre Tessier** 20:28 So… But that was me thinking out loud, like, you know, hey, we're gonna need to do this for a bunch of different languages.
Or run times, can we just… Can these just be optional services that are hung off the side?
Right? If you cover Java 17, somebody's gonna ask you to cover, like, hopefully not Java 8, but probably as well.
**Juliano Costa | Datadog** 20:51 I feel that Java 8 is… Out there in the wild.
**Pierre Tessier** 20:56 Oh my god, it's so out there.
It's upsetting. But, you know, there's… I think there's a limited mode that you could run open tree on it, at least.
I'm also, you know, it might require code changes in some parts, because we might have to run different things or whatever, so it's not like we could have one service that we build two different ways.
Because there's probably co-changes associated as well with running older versions.
So… I don't hate the idea, I'm just… I'm scared of bloat.
Right now, we only have Python that we could really do this with.
**Juliano Costa | Datadog** 21:48 Okay, well, let's, let's leave it like that. I don't think that's an urgent thing. I think the most urgent thing is getting 3.0 out there, and… I think the blog post… I want to write it, but I… I would rather wait for the NPR to land.
Wonderful.
**Pierre Tessier** 22:15 U.
**Juliano Costa | Datadog** 22:16 Yeah, before we release.
I mean, we can already raise the PR, because that will take a while, to be on the queue. I know that the hotel.io is… Has a kind of a…
**Pierre Tessier** 22:34 Yeah, well, we should get ahead of that right now. Do you already have a blog post written? We broke the demo, or whatever we were gonna…
**Juliano Costa | Datadog** 22:40 Nope.
**Pierre Tessier** 22:42 Okay.
We should get one written. I don't know if you want to write one and throw it across us in our channel.
somehow that we want to iterate on, or whatever, like, but we should get one post. At least, like, what you said, queued up, saying, hey, we're gonna… we're looking to release on this day.
And I think we are too… red diff PRs away from Running a release prep.
So… .
**Juliano Costa | Datadog** 23:11 Okay, I will… I will draft something to add my name, you know.
**Pierre Tessier** 23:23 And I am so much for the title, we wrote the demo.
**Juliano Costa | Datadog** 23:35 Perfect.
**Pierre Tessier** 23:40 So, can we target to have a release ready to issue by next SIG meeting?
**Juliano Costa | Datadog** 23:49 I… I'm confident that, yes, I don't… Looking at the PRS, there is nothing…
**Pierre Tessier** 23:57 It's just depend upon it.
**Juliano Costa | Datadog** 24:00 Yeah, it's just depend upon. I think that… the biggest PR will be the removal of product reviews, because that affects the AI as well. So that's the… that's what I will touch, unless someone wants to… Take care of that.
**Pierre Tessier** 24:24 Okay.
**Juliano Costa | Datadog** 24:33 If I…
**Pierre Tessier** 24:34 If you hit it today, great. If not, I will take a hard look at it tomorrow.
**Juliano Costa | Datadog** 24:42 Okay.
While we are here… Shanai, do you know… When we opened the PR, We have telemetry tests.
being triggered.
When the PR comes from a person.
it runs, when it comes from, or…
**Shenoy Pratik Gurudatt** 25:08 So, when it comes from Dependable, it runs, and then… Yeah, without the dependable part, if it's just a person, only when we approve it runs.
And there is a gate CI which will check, have we approved it yet or not?
If we don't approve it, then.
**Juliano Costa | Datadog** 25:24 My question to you now is, when is Dependabot? And it already ran. When I approve, it runs again.
**Shenoy Pratik Gurudatt** 25:32 I.
**Juliano Costa | Datadog** 25:33 Whatever my best. Awesome.
Awesome.
**Shenoy Pratik Gurudatt** 25:39 Nope.
**Juliano Costa | Datadog** 25:40 Yeah, but this doesn't affect the, The… the release, so… very good.
**Shenoy Pratik Gurudatt** 25:50 I had… I had one feature that I wanted, where I'll probably post the release, where we can… I wanted to take a stab at database monitoring.
Where we have two databases, Valky and Postgres.
We can get a lot of telemetry out with just, without any instrumentation done in the app layer, just on Hotel Collector's side to get it from host and stuff, and then send it to… Prometheus Open Search in here.
So… not Jaeger, just Chrome. Jaeger already has the app spans going to database and the attributes there. The missing part is logs and, telemetry. For… sorry, and metrics.
So, I wanted to add to that.
**Pierre Tessier** 26:35 We should have Postgres metrics enabled already. Yeah, yeah. It should be there.
**Shenoy Pratik Gurudatt** 26:39 Yeah.
**Pierre Tessier** 26:39 I think we probably don't have Postgres logs properly being sucked in.
we should take a look at that to make sure that's done, but I am all for us having a dashboard, like, database monitoring, and I'm all for us also throwing a lot more load at that Postgres database. It's pretty idle.
Right? I think every transaction should be doing stuffing to that database, if you ask me.
**Shenoy Pratik Gurudatt** 27:07 Yeah, and that combined with a feature flag for each of them is what I was thinking as an end-to-end thing.
So that's…
**Pierre Tessier** 27:15 I would also be… I would also be forward-loading all currencies into a… a Redis.
cache or a Valky cache of some kind, and having some kind of process that runs on the currency service to update it properly, based on some kind of open source Feed that it gets.
You know, maybe once every hour, it just does that. On loadup, it has a static list, but every hour, it updates itself. That'd be fantastic. But this is me thinking really out loud, for no reason.
**Shenoy Pratik Gurudatt** 27:47 Got it. Yeah, that's… that's something you can take a look at as well. Yeah, there's just some… some features in my radar, probably post-release, nothing to block right now.
**Juliano Costa | Datadog** 28:02 And we can always… I think one thing that I would love to have, It's a scheduled release.
Because, every time we… when we decide to do a release, it's like, oh, yeah, we are here for 200 commits, and… We should do a release. Maybe we could have something like, hey, once a month we're gonna do a release, done, done.
then we… Rotate who does the release, just four, yeah.
**Pierre Tessier** 28:36 Maybe every quarter?
We release whatever we have.
**Juliano Costa | Datadog** 28:42 Sounds like a plan.
Okay, so…
**Pierre Tessier** 28:47 That's, you know… Like, it's… whatever it is, whether it's a major release or a minor.
I don't think we should be thinking about patch release, so it should be considered a major or minor release.
We cut a release every quarter, maybe, or every two months, maybe, but I think every quarter is probably more appropriate.
Hotels feel like it's pretty stable-ish now.
So…
**Juliano Costa | Datadog** 29:12 Yeah, except the semantic conventions, but all the rest is pretty good.
But cool. Okay, yeah.
**Pierre Tessier** 29:26 Very good.
**Juliano Costa | Datadog** 29:28 Perfect.
Thanks, everyone. Jonathan, you didn't say much. Do you want to say something?
**Jonathan Munz** 29:34 No, I was just listening in to see what, what the current kind of agenda was, so…
**Juliano Costa | Datadog** 29:39 Cool.
**Jonathan Munz** 29:40 Appreciate it.
**Pierre Tessier** 29:40 3.0.
**Jonathan Munz** 29:42 Yeah, no, I'm sorry.
**Pierre Tessier** 29:43 March to 3.0, that's what we need to do. So, let's get it out.
**Jonathan Munz** 29:48 Cute.
**Pierre Tessier** 29:48 Cool.
**Juliano Costa | Datadog** 29:50 Cheers.
**Shenoy Pratik Gurudatt** 29:52 Thanks.
