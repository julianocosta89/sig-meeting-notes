SIG: Developer Experience SIG Meeting
Date: 2026-04-29
Duration: 44 minutes
============================================================

## Zoom Recording Transcript

**Fabri** 00:23 Hey! Good day, Johanna.
**Johanna Öjeling** 00:25 Hi! Nice to meet you!
**Fabri** 00:27 Likewise… I'm from the, the comms 6.
**Johanna Öjeling** 00:33 Yes, I figured. We talked about it last weekend, that you would be invited today, so I'm.
**Fabri** 00:38 Right.
**Johanna Öjeling** 00:38 You were able to join.
**Fabri** 00:39 Right, yeah.
I could make it in the end.
**Johanna Öjeling** 00:43 That's good.
**Fabri** 00:44 Let's see if Perk also joins, right?
**Johanna Öjeling** 00:46 Yeah, Perk usually joins, and Juliano and Tristan as well, so let's see who shows up today.
So, then you work with Tiffany in the communications, I guess?
**Fabri** 01:04 Yes, yes, I do. You work at Grafana?
**Johanna Öjeling** 01:06 Yes, I do. Okay. So we've also been working together on the same team.
Good, good, good. They park.
**Fabri** 01:15 So, Tiffany is handling, I believe we're gonna talk about collector components?
**Johanna Öjeling** 01:23 Potentially, yes.
**Fabri** 01:24 Yeah, let's hear from Perk also, because Tiffany is taking care of the collector documentation improvements, so maybe we will have to relay anything we discussed to her as well.
**Perk (Marcin Stożek) | Elastic Ingest** 01:40 Yeah, hey guys, I'm traveling, I'm traveling this week, so, gotta be without video. So, hi Fabri, I'm not sure if we talked only about the collector.
To be honest. I think that we talked about like, you know, OpenTelemetry as a whole, and the gaps that might be there that we find in here doing the interviews with, you know, other… other… other companies.
or projects.
**Fabri** 02:07 Yep.
**Juliano Costa | Datadog** 02:08 I think one thing that we, that we could hide, by the way, Giuliano.
**Fabri** 02:14 Hey, how you doing?
**Juliano Costa | Datadog** 02:15 I think we already spoke at GitHub one day or the other. I'm a maintainer on the demo.
So… I think… the work that we are doing here on the… on the Developer Experience SIG, We… at first, we thought it would take one path.
But after the end-user survey, we… We kind of saw that the community was… craving real-life examples of, how people are using hotel in production, and that's how we started… how we started the… the… the series of blog posts. And then…
**Fabri** 03:01 Right.
**Juliano Costa | Datadog** 03:01 This series is coming to an end.
And eventually, it will become the blueprints, or kind of, sort of, But the goal of having you here is just to discuss a little bit what we should focus next.
Why?
Because we do see that sometimes the… we have some processes within the… within the whole OTAL project.
that affects the user experience, which is the goal of this thing. So… for instance, new components being released and marked as GA, but there is no proper documentation of this component.
**Fabri** 03:47 Indeed.
**Juliano Costa | Datadog** 03:49 So, I don't know, we were discussing and brainstorming if we could have something, on… on the spec level, or whatever, on GC.
**Fabri** 04:00 Yeah.
**Juliano Costa | Datadog** 04:01 Military level, where the… each seek would be responsible for, responsible for having a file on their repo, or READMEs, or I don't know, whatever template we define.
**Fabri** 04:17 Yeah.
**Juliano Costa | Datadog** 04:17 and then that would backfeed, or just… that would feed the docs, but without the maintainers having to maintain a different page under the dock, because I…
**Fabri** 04:29 Yeah.
**Juliano Costa | Datadog** 04:30 I know that this cross-repositories sync is a mess.
**Fabri** 04:35 Well, we do it, I mean…
**Juliano Costa | Datadog** 04:37 Yeah, yeah, I know, but, like, for them, I'm not just blaming everyone, I took the… I took the guilt as well. For instance, the demo pages that we have are not up-to-date to the latest things that we have.
Yeah. And I know, and that just bothers me, because I know the pain, and, like, I… but I also… don't have all the time that I need to do all those cross… things, so that… that's the problem. Now, I want to hear from you. I don't know if, Johanna and Park, if they want to add anything, but…
**Fabri** 05:16 Yeah, well.
**Johanna Öjeling** 05:16 No, I think you're…
**Fabri** 05:18 Yeah.
**Johanna Öjeling** 05:18 Rusted in a good way.
**Fabri** 05:23 I'm having just a look right now at the, The current collective documentation for the components, and… Yeah, essentially for now, we're just linking to them.
the… the documentation is, like, the quality and the consistency is… varies widely. So I understand, like.
would you like to get, like, the old components documentation inside, inside the OpenTelemetry official docs? Is that the goal?
**Juliano Costa | Datadog** 06:02 I don't know, I want to hear from you. I don't know if we have stats on pages that users are mostly reading.
If users are used to go to the GitHub directly.
**Fabri** 06:16 Exactly.
**Juliano Costa | Datadog** 06:16 checking the READMEs on the…
**Fabri** 06:19 No, we don't.
**Juliano Costa | Datadog** 06:20 You have it.
**Fabri** 06:20 I think we don't have outbound traffic stats in that sense. I also think that… Like, in most cases.
Users will use just, like, there's a subset of components that are very popular.
And it's difficult to find a way of finding them, filtering them.
I can tell you from my experience where I was at Splunk.
we were, like other distros, we were bundling components, and I believe Datadog also does something similar. We ended up documenting, creating our own curated Custom documentation for the components that we were bundling, because… Of course, there were, like, some… we were bundling them with some presets, as all the teachers do.
And then eventually linking also to the upstream documentation when it was required in GitHub.
So I guess the documentation should… the Redmi files, at least, should stay there.
The moment we start creating manual curated documentation for components, we are taking a stance.
So the wider question to me is, should the OpenTelemetry documentation be opinionated?
and like… you know… For a developer, it would be useful, because developers want to get started with the things that work, and that are mature, and, like, be guided.
But the documentation so far, I think the upstream documentation, the open source documentation is not really… Taking that path.
And this is just my opinion, not the Sig's opinion. It's… we are, like, on purpose, we are being agnostic as to how you want to use it, what you want to do with it, and I think that's kind of painful for some developers. So… Even if we included all the documentation, from… from the components as docs. I mean, that would enhance, maybe, search?
But the developer would still be left with the question of, what should I use, or how do I use it, you know what I mean? And I guess that distro somehow filled that gap, because it's where the opinionated angle comes in.
But now I'm, like, wondering if… If we should have, like, a third upstream distribution that is not… You know, not core, not contribrib, but, like… Something else called, maybe, curated, or… the risk there is that you might end up, like, hearting some… some egos, because you picked a component and not the other, you know what I mean.
**Juliano Costa | Datadog** 09:12 Oh my god.
**Fabri** 09:13 I'm…
**Juliano Costa | Datadog** 09:15 I think on that, I don't know if you're following the new stabilization initiative on the.
**Fabri** 09:22 Not very… not closely, you know, tell me about it.
**Juliano Costa | Datadog** 09:25 Y-yeah, so, like… Currently, Contrip ships everything.
But from, a time in the future.
They will only ship the… the… the… Stable components, or something like that.
**Fabri** 09:43 Yeah.
**Juliano Costa | Datadog** 09:43 Some components will still leave under the… under the contrib repo, but I think the end goal is to have vendor components to be maintained by the vendor, rep on… under the vendor, repos, so then the.
**Fabri** 09:59 Yep.
**Juliano Costa | Datadog** 10:00 Now it's, like, the hotel giving the recommendation of encouraging people to use OCP.
**Fabri** 10:08 Yeah.
**Juliano Costa | Datadog** 10:09 Which is… from the… from the researches that we… from the surveys that we have read, not everyone uses, not everyone likes it, and it's not… Something that people like.
contrib is easy, you just, you need to update to just book the image, and that's it, and you have everything, but I think that will change whenever we start dropping components from there. So then… like, I… now I… I kind of got lost here on, what I wanted to… to hook on… on your,
**Fabri** 10:49 This thing about it created the third option?
**Juliano Costa | Datadog** 10:51 Yeah, exactly, exactly. So, like, the created one… will be 3 key, because, like.
I mean, of course, resource detector, transform, like… Biological components.
**Fabri** 11:05 for example.
**Juliano Costa | Datadog** 11:07 Yep.
**Fabri** 11:07 It's a big one.
**Juliano Costa | Datadog** 11:08 Another one is that everyone… we know that everyone uses… that's great, but, like, if someone uses, I don't know, Kafka, and another one uses RevMQ, like, will we ship both, or just choose one, and then once we choose one, we are… Recommending a specific technology?
**Fabri** 11:32 Yeah.
**Juliano Costa | Datadog** 11:33 It's so nice.
**Fabri** 11:34 I don't know if they… because I also haven't followed that one, I don't know if the Blueprints project goes into that direction, but it would be interesting, maybe.
for when it comes to components in OCB, And the modular nature of the collector is… if there was a way of… like a tool.
that generated, like, an OCB Configuration that you just feed to the tool.
and like a supermarket of components, and you have that documentation being rendered, so I think a tool there Could ease some of that friction, perhaps?
**Juliano Costa | Datadog** 12:12 Yeah. This is one thing, but, like, this solves the collector part.
**Fabri** 12:17 Yeah, yeah.
**Juliano Costa | Datadog** 12:18 And we have the whole… hotel ecosystem. Like, for instance, Weaver. It's been around for 2 years already, and we don't have one single doc page on it.
**Fabri** 12:31 Yeah.
**Juliano Costa | Datadog** 12:32 like, okay, it's not stable, it's in development, great, yeah, but so the semantic conventions, and we have 700-plus attributes documented on the docs.
Yeah. So, like.
**Fabri** 12:47 How would you, like.
what would you like to… let's maybe walk backwards, like, what is the final state you would… yeah, what's the final state you'd like to see in the docs? Like, you get in, what was the experience like?
**Juliano Costa | Datadog** 13:02 I… Honestly, don't know. Like… I feel that… Okay, what is hotel? How do I get started? Okay, so, like, getting started, of course, and then maybe an overview of, like, what hotel is, and… here it's tricky because OTEL is a bunch of stuff, and we have APIs, SDKs, we have some tools, we have the collector, we have Weaver, we have the operator.
We have… What else we have?
We have the demo. So, like, it's… I don't know… This is my opinion, and I think here, the problem is… And I feel that this is valid for the four of us. We are already too involved with hotel.
To know what a newcomer wants to see.
So, like, it's… we have an initiative, like, new contributors, there is a hotel CNCF, Slack channel for newcomers.
maybe we should try to take advantage of it, of them, and say, hey, when you open the OpenTelemetry.io, what you are missing, and what… where did you go, and .
**Fabri** 14:31 Yeah, yeah.
**Juliano Costa | Datadog** 14:31 What do you expect?
**Johanna Öjeling** 14:33 Possibility.
**Fabri** 14:34 the… Sorry, go ahead, John.
**Johanna Öjeling** 14:36 No, I think, like, when I… when I think about, like, when I use OpenTelemetro I.O. versus when I look at GitHub repos, I think when I go to OpenTelemetro I.O, I want to… it could either be, like, to find some kind of reference, or… like, understand what is this to get, like, a higher understanding, but also some kind of guidance, how to guide, like, how to use this. Like, for instance, if I wanted to look at, like, what is this weaver thing, then I would expect to learn like, okay, introduction to it, and also how can I use it, and that may refer to other sources. But I think that's how I see OpenTelemetro I.O, and I think it's a great idea to check in this Slack channel if we can gather data there. But I also wonder, if, like, we mentioned, I think last week also.
like, Slack analysis. I know Tiffany has run some on the collector channels to identify a good structure, so we could analyze what questions people ask in the CNCF Slack. Yeah. And then I… Also, I want… probably you have access to that, the… it's called Kappa AI?
Yeah. That's used for… yeah, if, based on the conversations that users enter, to get some AI assistance, whether we can expect some insights on…
**Fabri** 16:10 I mean, is… do you know Patrice? If you can… If you can reach out, reach out to Patrice Challen.
let me write the name here, is, is the, admin of, of Kappa.
So he has access to it, and I think he'll be able to dig a bit into the search data and provide you with some answers there.
**Johanna Öjeling** 16:33 Great.
**Fabri** 16:35 There's one thing, really, that I think I once suggested in the context of development experience, but it was, like, maybe 2 years ago or something like that. But then I kind of forget about it. And it's… like, OpenTelemetry is… you have the demo.
But mostly, what it is, is a specification.
And a protocol, and a few components wired together.
But it's… then it's very hard When we talk about mental model.
To tell users what you can do with it, if we don't have also… Like, our own backend.
Because the purpose is to do something with the data, is to get them somewhere. And the vendors, of course, have their own stories, right? We all have, like, Grafana, Elastic, Datadog.
And we have our stories, and we tell the stories, but… It's… it would be nice if… and I believe some of the demos, or there's this idea of using, maybe, Jagger, I don't know, but… I'm not saying we should develop our own open source OpenTelemetry backend, but maybe we should, in the sense of… Having, like, a basic… Back-end experience that we could use in flows and in educational materials, etc.
Where, even to just test out things.
And, like, get people to really get a feeling of the whole end-to-end flow of the things we're doing.
I don't know how vendors would feel about it. We're not talking about a competitor, we're talking about, like, a… I mean, ClickHouse created, like, a logs analysis tool, I think they vibe-coded it.
a year ago, and they released it, like, I think it's open source somewhere?
And what prevents us from creating, like, a test backend?
You know what I mean. I don't know if… does this idea make sense to you? Because when I create vendor documentation at Elastic or at Splunk, when I created it.
The end-to-end journey was very important, and it's… it's really hard to explain things if you cannot visualize them, if you kind of see what they… what they… what they look like, etc.
**Perk (Marcin Stożek) | Elastic Ingest** 19:04 You know, I very much, I very much agree with what you say, but I don't think… I don't think we need a backend, necessarily, for that, you know? Like, whenever I talk with people, and they ask me, okay, why would I use OpenTelemetry? And I say, hey, because OpenTelemetry means that now every vendor competes on the back end, that's where they should compete, but you get exactly the same data, so it's only a matter of how do you create dashboards, right? And the information that is on the dashboard is the same for everybody, so it is really comparable, no, in a way. So, maybe we don't need a vendor, but we need.
**Fabri** 19:42 Hmm.
**Perk (Marcin Stożek) | Elastic Ingest** 19:43 to say, okay, if you wanna see your traces from your apps, this is what you should see. If you wanna see your telemetry from the collector, this is what you would like… what you should monitor, you know? And then, this actually is applicable to everybody, I think, you know?
But otherwise, I agree with you. It would be… it would be easier if there was such a, like, a backend, like, a virtual or whatnot, you know.
**Fabri** 20:15 Yeah.
**Juliano Costa | Datadog** 20:16 I… I shared here on the… on the chat the Aspire, dashboard.
So this is a .NET project from Microsoft.
And this Aspire dashboard, you can run as a Docker container, and you'll have traces, metrics, and logs.
**Fabri** 20:36 There you go.
**Juliano Costa | Datadog** 20:37 And they accept OTLP, so, like, but the thing is, it's… encourage… well, it's not encouraged for production, because it doesn't have a backend. So, as long as your container is running, you have the data. If it dies and restarts, it restarts with fresh data.
So, I don't know, maybe we could, reach out to Microsoft folks and see how we could integrate that into… because this is… vendor agnostic.
**Fabri** 21:12 Yeah, but something like this.
**Juliano Costa | Datadog** 21:15 Provoise.cncf, so…
**Fabri** 21:17 Let me see… it's… is it open source?
It is. And… And I really… I understand, like, the aspiration here is to always keep it, like, open source, they're not, like, It's like a kind of a community project?
Oh!
Yeah, I'm looking at the repo. It's MIT licensed? I mean.
If you wanted to create a fork, we could, right? I mean…
**Juliano Costa | Datadog** 21:47 Yeah, but I mean, Microsoft is a big, contributor to the hotel.
**Fabri** 21:53 Yes.
**Juliano Costa | Datadog** 21:54 community, so maybe we could sync with them, and… I don't know.
Maybe move, because… Aspire is, a whole framework on, on .NET.
But maybe we could have the Aspire dashboard donated somehow to Hotel. But I know that there are other tools that GC already rejected Because OTAL doesn't want to be, back-end.
So, if we have a tool that is a backend, then we are now a backend. So, not easy.
**Fabri** 22:37 Yeah, but when we say, when we say we… sorry, Perk, go ahead.
**Perk (Marcin Stożek) | Elastic Ingest** 22:42 Yeah, I just wanted to say, Juliano, I think there are very good reasons for not to have a backend kind of vendor telemetry, you know, if you ask me. I mean, you know, come on, all of us are here from the vendor… some vendors, so I think that makes sense for Tony.
**Fabri** 22:57 Yeah, but the thing is, if we recommend, like, if sometimes we mention Jager, which is not a… Is it a CNCF project? It's not, right?
**Juliano Costa | Datadog** 23:07 It is, it is.
**Fabri** 23:08 Oh, it is, okay, okay. I mean… it's there, right?
But, it's just… Well… Jagger is just traces, or is this signals?
**Juliano Costa | Datadog** 23:20 Just traces.
**Fabri** 23:21 Yeah, that's the thing.
**Juliano Costa | Datadog** 23:22 If it was the three signals, we would have the problem solved.
**Fabri** 23:26 Exactly.
Yeah, but when you say that GC rejected, like, who's that? Because… I mean, maybe we should have that conversation with GC first, you know.
**Juliano Costa | Datadog** 23:37 Yeah, I think we had, like, a hotel desktop UI project. And I don't remember the old… the other one. Like, this is something that comes… Abe.
**Fabri** 23:53 Periodically.
**Juliano Costa | Datadog** 23:53 different discussions.
**Fabri** 23:56 I guess that the…
**Juliano Costa | Datadog** 23:58 I heard that before.
**Fabri** 23:59 I had to guess… I guess that they don't want to have anything that resembles a product that they have to maintain.
Right, because there's a maintenance burden, there's an image thing.
There's, like, a side competition feeling with vendors.
That they want to avoid.
But something, like, kind of scrappy, like Aspire Dev, or even simpler, I mean, that's something that… Even if we… I mean, we have the tools of coding that ourselves, if we wanted to.
I think it would still be nice to have something like that, just for… just for educational purposes, and I mean… like, deeply… So, like, the auto generator, for example, you know, when you generate fake telemetry, that's not a product, right? But we still use it for testing, we still use it for… but you need something at the other end as well, without… without having to sign up for a trial.
**Juliano Costa | Datadog** 24:58 This is a big discussion also on the demo, because on the demo, we use Jaeger, we use Prometheus, but we need somewhere… to visualize metrics and logs, so logs we send to OpenSearch that has their own full set of solutions, and… but we also use Grafana, and now that… Grafana is, growing, some competitors are like, hey, we should think about using another thing.
And I'm like, I understand their… their side as well, because I work for a competitor, so…
**Fabri** 25:35 Yeah.
**Juliano Costa | Datadog** 25:36 It's like, huh, how can we… How can we… fill all the gaps and, have everyone covered. So, it's tricky.
**Fabri** 25:46 It is, it is. You know where we are seeing also lots of that tension? In the blog, because I think that… The wheel of explaining end-to-end flows.
it's not possible to do in the docs easily right now, so people resort to blog posts, but blog posts inevitably are gonna use, maybe, vendor solutions, like Grafana, and it's difficult there. Let me just have a look, because there was an idea surfacing Yeah, so one idea that Patrice in the ComSig surfaced the other day is… is actually, he sent the email to the CNCF leadership about this.
So you might want to sync with him as well, is this idea of having, for the demo.
So, let me just read that verbatim. One vision is for us to run a closed version of the demo in a loop.
With user scenarios being played out during the next hour cycle, and then we could invite vendors to provide state-of-the-art examples of dashboards over this demo.
That's another thing he's suggesting, and I think it's also… it's interesting, because it invites vendors to participate.
And, and to, like, kind of show what you can do with that data from the demo.
So that's also a way, I think, of… you would avoid having your own backend.
But at the same time, you would show, like, the end-to-end flow.
**Perk (Marcin Stożek) | Elastic Ingest** 27:24 But it will also show the thing that users matter… that matters for the users, that users care about, which is, you know.
how do I… how do I set up my monitoring on the vendor side? Like, how do I set up my dashboards? Is it a terraform? Is it a script? Is it an API? Is it, like, a UI click, click, click, click, click, you know? So, I like that suggestion, because actually, it exposes The vendor capabilities, which might be great for dealers, then users can, you know, check out for themselves.
**Fabri** 27:56 What do you think?
**Juliano Costa | Datadog** 27:57 household…
**Fabri** 27:58 Good work.
**Juliano Costa | Datadog** 27:58 Bye.
I like the idea, but I also have another, Point to, to, to bring, that is, Some vendors require… Extra components.
So if we run the demo, if we run the demo OTLP in OTLP out, just with, let's say, a resource detector and a transform that we have already on the demo.
That would provide, data, like, raw data, traces, metrics, and logs, but I know, for instance, Datadog. If you add the… an extra resource detector, if you map a host, whatever, and you do, environment tag.
when the data reaches the platform, you have a way better experience, because we can correlate infra with your service, we can add the MTech, so, like, all those specificities of the vendor, Will be lost, because the vendor will not have the control over the collector.
**Fabri** 29:07 He's.
**Juliano Costa | Datadog** 29:07 That's.
**Fabri** 29:08 kind of a… it's kind of a litmus test for how well do you get, like, country data in, and vanilla SDK data in, and… Which is kind of… vendors will probably want to avoid that trap. I mean, as a vendor, I would.
So I think it's also very interesting to explore the Aspire Dev, let's call it like that, path, because it's… it's like, you have, like, full control of that demo running on Cycles, you know?
**Juliano Costa | Datadog** 29:36 Yep.
**Fabri** 29:40 Yeah, that's a.
**Juliano Costa | Datadog** 29:41 index.
**Fabri** 29:41 Oh my god.
**Juliano Costa | Datadog** 29:42 And I know that Elastic also has some distros, right? Like, even SDKs, not just the collector.
**Fabri** 29:49 Yeah.
**Perk (Marcin Stożek) | Elastic Ingest** 29:49 Yeah, it's a hard thing to say that a vendor would like to build on top of hotel, and then at the same time, the more you are hotel vanilla.
The better for your, how to say it, interoperability between vendors, right?
I wonder what the Aspire dev, the problem is that Because nobody will use that on the production. I wonder how usable that will be for the users, no? How much value would that bring? Because they will… they could see what is possible, they will… Not necessarily maybe reuse that, or maybe they would, if… if you don't have to add any specific vendor-specific components.
On top of that, right?
**Juliano Costa | Datadog** 30:32 On the demo, currently, we have 42 different vendors, showing how to send their data to Each one of them.
So… some vendors go in an approach that you have, like, just whatever you need to change on the collector, and some other vendors have blog posts, like Dana Trace and DataDoc. I have a whole doc page where I explain, like, hey.
at this, here is how you run, and done. And here is what you get. So I also have screenshots from the product.
maybe Aspire… because I think all of that to say that I think Aspire would solve the educational cases that Fabri is mentioning.
**Fabri** 31:21 I think so.
**Juliano Costa | Datadog** 31:22 And if we… if you want to take a look at how vendors are using Then we can maybe just have a link to… to the… demo README, where I have all the vendors listed, and… I think vendors will… Whenever we kind of put a spotlight on that, vendors will be more interested in having their names there and being… updated, because I know some vendors that haven't touched the demo for a while, so most probably, if you just click and navigate, you'll have a broken experience.
**Fabri** 32:00 Yep.
And… I would also push it a little further and say.
nobody wants to contribute to Jaeger today, because, I guess, or not so many people, because it's just racing.
But if we had, like, a back-end project, experimental, educational only, whatever.
I mean, that opens… that opens contributions also to front-enders, not just back-end Go developers. And it's an interesting front, that one. I mean… If we talk about developer experience, how you show the data, you process the data is also… part of the experience, and… and I think companies can also contribute some of that, like, you know, maybe you came up with a flame graph visualization that you want to open source, and… Where are you gonna… where are you gonna contribute the source of that, you know?
So it's like an additional avenue for contribution, which I wouldn't rule out.
The question is, what do we do next? Like, could you pitch Juliano this idea, or would you run… would you like, maybe, to run this first, inside a group? The proposal, a draft, whatever? What do you think?
**Juliano Costa | Datadog** 33:13 Excellent.
**Fabri** 33:14 You could do it here.
**Juliano Costa | Datadog** 33:15 So, do you think we should… what… Because here, we have two groups that we need to talk to. One is the GC.
**Fabri** 33:25 Yep.
**Juliano Costa | Datadog** 33:26 When… and then GC will only accept if we have a TC supporter, so this is within OTEL, but we also have the Aspire folks.
**Fabri** 33:38 Right.
**Juliano Costa | Datadog** 33:39 That we would need… we would like at least to have their… I know that… From their license, we could simply fork it, but it would be better if it was a proper donation, and…
**Fabri** 33:52 Yeah, but my impression is… My impression is that if we go to GC saying that aspire folks are open to it, they will get… GC will get nervous, because it's like, oh god, I mean, you promised something, and I don't know, it's Microsoft, or, you know, and… I think they might get nervous. And also, to be honest, I think… we could fork it, but we could also think of… we can provide the two options, like, we chase a project like this, which might be Aspire or somebody else, someone else, or we create one. That's… that's the other option. So I would probably reach out to GC first with… with the proposal.
**Juliano Costa | Datadog** 34:31 And just because I know, I think we should, also consider the… or have at least in mind, the open search project, because it now became part of Linux Foundation.
So I know Dota?
he'll probably, pitch, like, hey, why don't just use something that is already part of the Linux Foundation?
**Fabri** 34:57 True, just as, like, a third option, yeah.
**Juliano Costa | Datadog** 35:02 But the problem here is that OpenSearch is actually, Let's put here, in quotes, production-ready, product.
**Fabri** 35:12 Yeah.
**Juliano Costa | Datadog** 35:13 So this is, again… Put us back on the tricky path.
**Fabri** 35:19 Well, but hasn't OpenTelemetry competed with proprietary agents for years? And the companies ended up adopting OpenTelemetry and supporting and maintaining OpenTelemetry, and they ditched their own proprietary agents in most cases?
**So… you know, maybe… maybe that's the answer. I mean, otherwise, why… why is it… I mean… it's like the elephant in the room, if it's part of CNCF, why ignoring it? But… Perk (Marcin Stożek) | Elastic Ingest** 35:48 I would, I would say…
**Fabri** 35:49 I would certainly… I would certainly offer it as a third option.
**Perk (Marcin Stożek) | Elastic Ingest** 35:52 it's part of the Linux Foundation and not the CNCF, and I think I'm… I think there's a good reason for that.
**Fabri** 35:59 Haha, okay, got it.
That's an interesting, yeah, information.
Well, decentral politics, and I'm not really sure about the power dynamics there between the Linux Foundation and CNCF, but…
**Juliano Costa | Datadog** 36:18 Oh, a Linux Foundation, or CNCF?
**Fabri** 36:21 Yes.
**Juliano Costa | Datadog** 36:21 So, it is the same, but not the same.
But, yeah, I… You were about to mention some… a third option.
**Fabri** 36:37 Yeah.
**Juliano Costa | Datadog** 36:37 Probably.
**Fabri** 36:38 No, that's… that could be the third option, I think.
**Juliano Costa | Datadog** 36:41 Okay.
**Fabri** 36:42 search. But, so what would you like to do? Maybe create a draft that we could discuss between DevEx and SICCOM, maybe?
And then pushed it to GC, or just message GC, depending on how you feel comfortable with it.
**Juliano Costa | Datadog** 36:59 I have close connections with Jurassi and Pablo. Pablo works with me. Gerasi is Brazilian. Brazilians usually like each other.
**Fabri** 37:11 And Paolo is half… well, he's Spanish, so there's a Latino thing. I mean, if you want it, if you need that, Giuliano, I can also join a call and remake the arguments about from the dock side.
**Juliano Costa | Datadog** 37:26 list.
**Fabri** 37:27 Because I think it'd be interesting to… if you need, like, some, some… you know, some support, I can… I can be there, if needed.
**Perk (Marcin Stożek) | Elastic Ingest** 37:36 I think even if that's not a public thing, maybe it would be useful to just have it in the demo as a baseline.
So, having the most Hmm. Most simple tool.
that accepts OTLP and provides dashboards as one of the many platforms, but this one specifically being open source.
You know, from the outside, not vendor-specific and so on.
So, even if you are not successful with this discussion about having a backend as itself by OpenTelemetry, I think you can still do something here, you know?
**Fabri** 38:16 Okay, you mean, but, like, as part of the docs, or as part of… Perk (Marcin Stożek) | Elastic Ingest 38:20 as part of the demo.
**Fabri** 38:21 Yeah, yeah, yeah, yeah, yeah.
**Perk (Marcin Stożek) | Elastic Ingest** 38:23 Yeah, so you have the auto demo with everything.
**Fabri** 38:25 I mean, nobody's gonna… who's gonna forbid that? Nobody, I guess?
**Perk (Marcin Stożek) | Elastic Ingest** 38:31 Yeah, exactly. So, Juliano, yeah. But I have my copy here, you finished it? No, oh yeah, this one.
**Juliano Costa | Datadog** 38:40 Thanks for supporting the Costa family.
**Perk (Marcin Stożek) | Elastic Ingest** 38:44 Or maybe we can convince him, somehow.
**Juliano Costa | Datadog** 38:48 Right.
Yeah, so… on the demo, we are… Currently in the middle of this discussion as well. So, like, We are adapting the way that we spin up the demo to make it easier to other vendors to fork and maintain their forks.
But also to… to make it easier to vendors to configure and send hotel demo data to their backends. And, in the middle of this discussion, it came, like, discussions about if we should replace the backend that we have, because currently, as I said, we have Jaeger, Prometheus, OpenSearch, and Grafana, and we do not use, like, like, the Grafuna approach would be… Lgtm stack?
the open search approach would be, like, the whole experience in open search. Jager and Prometheus on its own, they do not provide any experience, so…
**Fabri** 40:02 Yeah.
**Juliano Costa | Datadog** 40:03 Like, at least not end-to-end.
**Fabri** 40:06 maybe we don't know yet, but how heavy is open search, say, if you wanted to, like… is there a possibility to spin, like, a read-only… instance that, that, you know, deletes itself every 24 hours, like.
Like, security-wise also, like, is it, like… Possible, you think, or…
**Juliano Costa | Datadog** 40:26 I think we have, I think OpenSearch has a running demo.
**Fabri** 40:31 Oh, let me see…
**Juliano Costa | Datadog** 40:32 If they do.
**Fabri** 40:33 True, that would be perfect.
**Juliano Costa | Datadog** 40:41 I don't know where it is… But I…
**Fabri** 40:44 And…
**Juliano Costa | Datadog** 40:45 I can find.
**Fabri** 40:49 Community…
**Juliano Costa | Datadog** 40:51 Yeah, so if you go to… here it is, I'm sharing, you know…
**Fabri** 40:55 So…
**Juliano Costa | Datadog** 40:56 You have the… in this space, you have the live playground.
And in here, you'll have the.
**Fabri** 41:04 Oh, I'm ready.
Wonderful. So that's… Okay, it's not super fast, but… I guess… I guess Aspart is… is way quicker, but… Yeah.
**Juliano Costa | Datadog** 41:21 But I think this is also what vendors want to… Not the best platform to showcase, because… Then they can say, hey, ours is fast. Faster.
**Fabri** 41:34 Yeah, but the thing is… I don't know if that's possible, Juliana, but I'm looking at this now, and It would be great if… I mean, I would… from this demo I'm looking at.
I would just keep, like, the Discover menu.
Probably, and maybe at two others, but all the rest, it reminds me, like, alerting, for example, we don't need that for demo.
We probably also don't need the machine learning features, we don't need the user management, the… you know, there's lots of things that I think we don't need that, because it's… we need something way simpler, like a… like an explorer with some graphical capabilities, like, you don't need to set up a dashboard.
For a demo, I think.
That's… that's my opinion.
**Juliano Costa | Datadog** 42:27 So, this is a thing that we discuss a lot on the demo.
Because we do have, I think.
10, about 10 dashboards in Grafana and alerting.
Yeah. On the demo, we want to showcase OpenTelemetry, but we also want to showcase what you can do with the data.
**Fabri** 42:47 Yeah.
**Juliano Costa | Datadog** 42:47 That includes dashboarding, alerting, and all the other things.
**Fabri** 42:52 Yeah.
**Juliano Costa | Datadog** 42:53 We want to… teach folks under… under the observability, field. So…
**Fabri** 43:02 That's, that's probably where…
**Juliano Costa | Datadog** 43:04 It's complicated.
**Fabri** 43:05 Yeah, that's probably where Patrice's idea could come into play, where you have the vendor Like, collaborating, maybe providing, like, a live environment where, oh, look at all the fantastic things that… There have been, you know, people have built, But I think… I think we are onto something here. I think we all agree on the core, which is… To have, like, a backend experience to enable end-to-end an end-to-end DevEx experience for newcomers and people that want to learn and experiment, so… I think… that, I think, is the core idea we are kind of agreeing on.
**Perk (Marcin Stożek) | Elastic Ingest** 43:49 Unless all this data should go to F3, and then you have AI agent, no.
Thief through all that, and give you, you know, answers on the fly.
**Juliano Costa | Datadog** 43:59 Johanna, you didn't say much. I want to hear your opinion as well.
**Johanna Öjeling** 44:04 Yeah, I think, these are really interesting ideas, and I need to, also check these for, stacks, that you link to. But I actually need to drop now, so… I'll need to catch up later, but thank you, also great discussion, and, thank you, Fabri, for, joining. Sure. And let's, let's catch up.
**Fabri** 44:28 record.
**Johanna Öjeling** 44:29 I think.
**Juliano Costa | Datadog** 44:30 Boom.
Bye. Thanks.
**Fabri** 44:32 Thank you.
**Perk (Marcin Stożek) | Elastic Ingest** 44:35 Thanks, bye.
**Juliano Costa | Datadog** 44:37 See ya.
