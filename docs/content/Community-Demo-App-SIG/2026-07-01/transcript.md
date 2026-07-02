SIG: Community Demo App SIG
Date: 2026-07-01
Duration: 35 minutes
============================================================

## Zoom Recording Transcript

**Matt Wimpelberg** 01:29 Hello, how's it going?
**antoninbruneau** 01:32 Hello! How are you?
**Matt Wimpelberg** 01:34 Doing well, yourself?
**antoninbruneau** 01:36 Good, good, thank you.
It's rare that I'm available for this type of calls, so… Once I have the time to join, I'm doing it.
**Matt Wimpelberg** 01:51 Thanks.
Where are you based out of?
**antoninbruneau** 01:59 In Paris?
**Matt Wimpelberg** 02:01 Oh, so it's already, 5 o'clock, right?
**antoninbruneau** 02:04 Yep.
**Matt Wimpelberg** 02:05 Cool.
**antoninbruneau** 02:07 Where are you?
**Matt Wimpelberg** 02:08 New York.
**antoninbruneau** 02:12 early morning.
**Matt Wimpelberg** 02:14 11. Not too bad.
It's the first one I've joined, so I don't know what, attendance usually looks like.
**antoninbruneau** 02:36 Sometimes nobody drawings, sometimes people do.
Are you working on the demo environment, or using it?
**Matt Wimpelberg** 02:54 Yeah, both. I was using it for a while, and I started contributing a couple weeks ago.
**antoninbruneau** 03:00 Nice.
**Matt Wimpelberg** 03:01 Actually have a PR in now to replace Locust with K6 furlough testing.
**antoninbruneau** 03:06 Oh, yeah, that's you, that's a nice one.
**Matt Wimpelberg** 03:09 Thanks, yep.
**antoninbruneau** 03:11 Yeah, we're struggling with, with low cost, so it's… it consumes so much memory for… Not doing anything.
**Matt Wimpelberg** 03:19 Yeah, the… Let me see… Juliano has been… We've been going back and forth, I think it's in a good place now, but… are you one of the reviewers or maintainers?
**antoninbruneau** 03:32 No, I'm, new contributor.
**Matt Wimpelberg** 03:38 Cool.
**antoninbruneau** 03:39 I'm part of Tsuga, a new French observability company, and…
**Matt Wimpelberg** 03:45 I quote.
**antoninbruneau** 03:46 We're using this demo environment a lot for, well, demo purposes.
**Matt Wimpelberg** 03:52 Yeah.
**antoninbruneau** 03:52 And so when we can, we contribute.
**Matt Wimpelberg** 03:56 Cool.
**antoninbruneau** 03:58 Hey, FedEx.
**FELIX GEORGE** 04:00 Right.
I do.
**Matt Wimpelberg** 04:01 Ethics.
I don't have anything in particular other than that PR at the moment.
**FELIX GEORGE** 04:28 We recently added some agentic demo application integrated with the OpenTelemetry demo.
No.
Since you said you are already using it for demo, can you… if you try it out, I have added that PR, if you have tried it out.
to share your story.
**antoninbruneau** 04:46 The in-hab agent?
**FELIX GEORGE** 04:50 Yeah, so we added an agent MCP server and a chatbot to the hotel demo application. So, you will get the agent traces, like the LLM call, the token details, like the request response, those kind of traces also you will get.
**antoninbruneau** 05:09 I was waiting for the release to test it.
**FELIX GEORGE** 05:14 Yeah, it's already merged again, try it out.
**antoninbruneau** 05:17 Yeah, but I was waiting for the, like, a real release to be made, so I can update the hand chart.
But yeah, I hope that's the locally.
But you don't… so you have to provide an LLM provider.
**FELIX GEORGE** 05:34 So, for any kind of request, for it to execute any kind of request, you have to provide an API, but we provide some sample request where we have a cache for the LLM responses.
**antoninbruneau** 05:46 Okay.
**FELIX GEORGE** 05:47 GPT 5.5 and Opus 4.7.
**antoninbruneau** 05:51 Okay, so for load generation, we can just use the cache and…
**FELIX GEORGE** 05:56 We are not at that stage yet, we only have, like, 3 requests where we have the cache, but we will be adding more requests soon.
So we are also trying to build a natural language load generator. Like, right now, the logist uses a predefined request, right?
**antoninbruneau** 06:17 Nope.
**FELIX GEORGE** 06:18 Where it keeps on executing from a Christian bank. Similar to that, we will have a natural language Christian bank, where we will pick one request.
executed.
So, it won't be, like, a multi-turn request.
Right now, we are planning a single down request with, like, what is the cheapest product in any particular category, like that.
Yeah.
Hi, Shinoy.
**Shenoy Pratik Gurudatt** 06:48 Good luck, hi, everyone.
I'm not sure if other maintainers are joining in.
Today, probably, we can start.
Felix, did you have any PR in particular to check?
**FELIX GEORGE** 07:02 Yeah, so that was… Yeah, there was a mistake in the initial PR, where the MCP Is point… is a dependency of the agent. NCP is dependent on the agent, but it should be the other way around.
I have added it in a new PR.
It's already approved, it's pending to be merged.
**Shenoy Pratik Gurudatt** 07:25 Okay.
Let me just check.
**FELIX GEORGE** 07:29 Yeah, 3 sites here on it.
**Shenoy Pratik Gurudatt** 07:32 Okay.
MCB port dependency… Our agent.
I'm just wondering if… This is… The issue with the compos, how is the agent?
So…
**FELIX GEORGE** 07:50 Yeah, so…
**Shenoy Pratik Gurudatt** 07:51 That's even working.
**FELIX GEORGE** 07:56 No, without in the MCP disabled mode, agent won't try to connect to the MCP.
So, in the MCP-enabled mode, agent will try to connect to the MCP and it will fail, because MCP port is waiting for the agent port to start up.
And, it… because the HTTP URL is not available, it's crashing out right now.
**Shenoy Pratik Gurudatt** 08:18 I see.
Let me do one thing, then. I see the PR is approved.
probably what I can do is I'll update the branch. So, you know, we have telemetry tests now, right, which will actually test Jaeger spans, open search logs, and Prometheus metrics. Juliano added a PR last week, where we'll also do some testing on the agent spans that are generated.
**FELIX GEORGE** 08:45 Okay.
**Shenoy Pratik Gurudatt** 08:46 So, if I just update the branch, it should pick it up, and then from main merge, it will run the agent tests as well.
Okay, I can re-approve once, the CI stuff.
**FELIX GEORGE** 09:01 I'm kidding.
**Shenoy Pratik Gurudatt** 09:02 Yeah, so let's see that basic, Yeah, that should be good. Also, I have a PR, since you are here. I added it to the docs as well.
Where we are… Trying to add the GenAI normalizer.
**FELIX GEORGE** 09:21 Hmm.
**Shenoy Pratik Gurudatt** 09:22 So, we take the traces and spans coming in from open elementary trace loop thing that we have instrumented, and then it converts it into open telemetry GN AI attribute style of conventions.
So, you can test it out locally.
I was thinking, if you could help do… generate the VCR again with this added in, probably after we merge it, then it will be great for some, follow-up PR that you're doing on load generator and other stuff.
**FELIX GEORGE** 09:55 How does the VCR get affected if I… if I add this? If it's just a change in the auto collector, right?
**Shenoy Pratik Gurudatt** 10:01 Yeah, I don't think so. VCR will get affected, because VCR is only for.
**FELIX GEORGE** 10:05 11.
**Shenoy Pratik Gurudatt** 10:06 Responses, yeah.
Okay, yeah, that makes sense. That's why the test would pass, I think. I was trying to run it locally, and… I think I tested it out with local VCR stuff. It did work.
Okay. Probably, yeah, probably then just load gen and the Grafana update. That's the only one between… From other things… I see you also had the documentation update. I took a look at what the changes you were making in the OpenTelemetry.io website that look good. I'll approve it. I don't know if it is merged or not, but if not, I will…
**FELIX GEORGE** 10:53 It's waiting, like, 9 workflows awaiting approval.
**Shenoy Pratik Gurudatt** 10:58 Yeah, that, I think someone from the demo SIG… oh, sorry, someone from the telemetry.io SIG needs to run it there.
We can ping them again. If not, I'll ping them, yes.
Should be good.
Cool.
Yep. I see others on the call as well. Hi, everyone.
My tanduni.
Do you guys do… Introduce yourself, do you have any topics to discuss?
**antoninbruneau** 11:30 Damn.
**Shenoy Pratik Gurudatt** 11:30 For the first time.
**antoninbruneau** 11:32 Yeah, no, so, I'm… So, I'm Antonin, I'm based in France, contributed… I had two pairs that were merged already. The last one I, Push was to, propagate trace contacts from the service to the database logs, so we can do the correlation between what's happening on the service side and on the database side.
**Shenoy Pratik Gurudatt** 12:03 which database was it? Was it Postgres, or…
**antoninbruneau** 12:05 Yeah, Postgres.
**Shenoy Pratik Gurudatt** 12:06 Okay.
**antoninbruneau** 12:08 The product catalog, if I remember correctly.
service.
**Shenoy Pratik Gurudatt** 12:13 Yep.
**antoninbruneau** 12:15 And yeah. But that, that's merged already.
**Shenoy Pratik Gurudatt** 12:22 Anything in particular that you wanted to discuss, or…
**antoninbruneau** 12:25 No, just because I saw a lot of, updates coming, soon about, services being removed and changed, and because this is gonna affect us, as we use that for our demand environment. Just wanted to see a…
**Shenoy Pratik Gurudatt** 12:44 Yeah.
**antoninbruneau** 12:45 How it's going, where it's going, and when it's happening, so we can prepare.
**Shenoy Pratik Gurudatt** 12:51 Yeah, so, Juliano and Pierre did mention that we wanted to cut a branch, this week for 3.0 on Docker.
And then we'll… Take some time to update the Helm charts.
So… It was supposed to be happening this first round, first half of July.
So let's see when that will happen. Yeah.
Hey, man.
Do you want to chime really quick before you get pulled off?
**Matt Wimpelberg** 13:19 Yeah, sure. So, Matt Winpelberg, I work at Grafana Labs. I have submitted some PRs. One includes replacing Locus with K6.
Juliano and I have been working on that back and forth.
And yeah, I'm really happy to start contributing to… to open source and open telemetry in particular.
It's great to meet you guys.
Sorry, I have to drop.
**Shenoy Pratik Gurudatt** 13:41 that we are at all cases, it's pretty nice. I'll also take a look, and then try to get it working and stuff, and see how it goes. But it's really a good conversation. Thanks so much. Thanks for the feedback.
**Matt Wimpelberg** 13:51 Thank you, appreciate it.
Talk soon.
**FELIX GEORGE** 13:53 We will also use it in the future, like, locker space moving from 2K6 for load generator. I'll also have to, take a look at it, right?
**Shenoy Pratik Gurudatt** 14:02 Yep, yep, yep.
**FELIX GEORGE** 14:04 Thank you.
**antoninbruneau** 14:06 And, yeah, maybe a question I had for you, on the… Prometheus community, you have the mix-ins to monitor Kubernetes cluster.
But I didn't find anything similar based on OpenTelemetry metrics.
I was wondering if you knew of any project like that.
**Shenoy Pratik Gurudatt** 14:35 You mean mixing for Grafana dashboards?
**antoninbruneau** 14:38 for Grafana or something else, but based on OpenTeametry matrix instead of Prometheus ones.
**Shenoy Pratik Gurudatt** 14:45 We do have Grafana dashboards right now that are inside the codebase itself.
Which do… a combination of things to get traces from Jaeger, logs from OpenSearch, and metrics from Prometheus all together.
So, we don't maintain mixed-in dashboards today.
But that'll be a good addition if you want to add.
I don't have particular views on how will it be used, because what I've seen with mixed-in dashboards is, it's usually used for production-grade things. So, I work for OpenSearch Observability Team, so there, we have a Prometheus Exporter and OpenSearch as a plugin. And with that plugin, we do distribute, mixed in dashboards for Grafana, but that's for a production-style setup where you would actually monitor open search with Prometheus and Grafana all together.
Whereas for OpenTelemetry demo, I'm not sure how it would help the users, because it is more like plug and play, try it out, and then… change your backends and see how it works. So, even if we change the backends, the mixing dashboards will not work for downstream folks.
But yeah, if you have something very concrete, you can create an issue, we can discuss it there.
**antoninbruneau** 16:05 Yeah, no, it's more that… For now, if you want to monitor Kubernetes, you have to rely on… and want to use McSense to have a ready-to-use system, then you have to rely on Open… on Prometheus.
Where now OpenTeometry has similar receivers, and we could probably build equivalents of Prometheus mix-ins, but based on hotel.
And was wondering if you've heard of something like that or not.
**Shenoy Pratik Gurudatt** 16:39 There is a separate Helm charts repository, right?
Where we deploy everything for the demo, and also for other things in OpenTelemetry.
**antoninbruneau** 16:52 Yep.
Yeah, I'll look into it.
**Shenoy Pratik Gurudatt** 16:56 Yeah, probably that's the one where we should start, if you're thinking specifically for Kubernetes.
style dashboards and looking at KITS resource attributes and other pieces.
So… yup.
But yes, let's start an issue, and then discuss it there.
I'd like to know other maintenance views as well.
But I had one follow-up from the previous point that you mentioned about PostgreSQL. I was planning to add some extra things to… the demo, for database monitoring in particular. Something like server-side metrics, logs and traces for Postgres, and also for Valky.
Currently, I see there are some pieces in database monitoring that we can enhance in the OpenTelemetry demo right now.
**antoninbruneau** 17:52 Yes.
**Shenoy Pratik Gurudatt** 17:53 So there are two sets of views, right, for database monitoring. One is the APM view, where you see services talking to a database, and then there is the server-side view of the database itself.
**antoninbruneau** 18:02 Yep.
**Shenoy Pratik Gurudatt** 18:03 Cool. Yeah.
**antoninbruneau** 18:04 So that's why I started, like, doing this, so you can have the trace ID in the query logs.
Because they are passed as, SQL commands.
And if you go… if you want to go further, I can share with you a hemp chart that we've built that, is… specifically built for Postgres database monitoring.
basically, use an OpenTeametry sidecar.
with, presets of Bostgres functions.
to collect system metrics in the Postgres database, about query time, about… Number of rows written by queries, things like that.
That you can then use to have, deep visibility into your database.
**Shenoy Pratik Gurudatt** 19:01 I see.
Got it. And, You said you had a fork of a jet, so is it, like, a demo fork, or is it something else?
**antoninbruneau** 19:12 So in that case, it's just a chart.
**Shenoy Pratik Gurudatt** 19:15 Okay.
**antoninbruneau** 19:16 share. It's independent from the OpenTeamatory dimmer, although it depends on our instance of it. But if you go to… This one?
I'm not sure if I can share my screen, just to show you. I've put the link in the…
**Shenoy Pratik Gurudatt** 19:41 Okay.
**antoninbruneau** 19:42 Can't do that.
**Shenoy Pratik Gurudatt** 19:43 I see.
Oh yeah, this is… this is exactly something that we can… Add to the demo is what I was thinking.
**antoninbruneau** 19:56 Yeah, it's open source, it has nothing to do with Sugaran specifically, but it's something we use to… To help our customer observe, their… their data.
And basically, what it does is it has this, PG monitoring setup SQL.
And it's a bunch of… SQL statement, and to create functions.
That queries, tables.
And then in the hotel config, it's just… so you have the default Postgres one.
Yeah. You have a set of SQL queries that queries those pre-built functions.
And extract metrics out of that.
**Shenoy Pratik Gurudatt** 20:50 Because it's more like a monitoring user who is extracting out telemetry on some interval?
**antoninbruneau** 20:56 Yeah, so the… the templates, it basically creates, So, the way you use it is you enable it for Postgres, you pass the credential use or the connection strings for your database.
And, then for each database, it will create a secret.
That will be used to create a user in the database for this, observability part.
And then you have a sidecar, that it gets created, and I use the… Argo CD event, so when a Postgres database with a label On it is crea- is… boot.
Like, basically all you have to do on your database is add… Where is it?
Yes.
cycle, andject, so all you have to do on your Postgres database is add this label.
and the sidecar name, and it will inject it. You have a job that prepares your database with all the functions, and then you have your sidecar that just streams the data to… from a… or collect the data from the database, and push that to… your Jimin said, for example.
**Shenoy Pratik Gurudatt** 22:27 I see.
Yup, like, this is something valuable.
We can… if we can replicate it here.
We do have Sidecar, I think. Now, at least we'll add it now, if it is not there. I know the gateway is there, for sure.
But, yeah, I'm just thinking from a demo point of view, what all we can add, and then how we can showcase.
Because we do have monitoring user, as far as I remember in the demo.
If we can… Have something like a feature flag?
That would… create some issues in the Postgres side.
And then we look at telemetry from the database, and help users to drive a root cause from the dashboards, or using the telemetry. That would be really helpful as a showcase in the demo.
**antoninbruneau** 23:22 So that's something else we worked on, and, basically what we do is, Services.
We have, what we've put is a proxy between the services and the databases.
That we can deploy, and this proxy, introduced some fake latency.
In the database query.
And so, we choose to be 50-50, but you can configure it, actually.
In this way, and it also… Simulate, the fact that it's a… new Postgres database. So, for the service point of view, it's pointing to a second database. The role… the goal is to mimic, like, a database migration you would do, and you would have, like, an A-B testing at the beginning, and the new version would have a 50% error rate, or an increase on the latency compared to the previous one.
And so you could deduce from… The telemetry that the migration is not working properly, because you have 3300 milliseconds more latency than on the previous version.
So, so we've done that…
**Shenoy Pratik Gurudatt** 24:52 This… this is super cool. This… this is some really nice showcase of how we can, like, mimic some tactical use cases for users. A-B testing is one, then migration is second, and then the fake latency is something for sure.
Yeah.
Do you want to contribute this back to the hotel demo?
**antoninbruneau** 25:14 Again, yes.
**Shenoy Pratik Gurudatt** 25:16 That'll be a super cool setup, because it touches everything. Some real production scenario, it touches the feature flag, and then, we actually help users to drive a root cause on database monitoring.
**antoninbruneau** 25:32 Yep.
And if you want to… on… for the feature flag, we also have this… Spicy gremlin. It's basically something that randomly enables and disables feature flags in the demo environment, and so we use that to randomly generate errors, on different services on the Demo environment.
**Shenoy Pratik Gurudatt** 25:59 So there's, like, a chaos engineering tool? Yes.
**antoninbruneau** 26:02 Always, yeah.
**Shenoy Pratik Gurudatt** 26:03 And it uses all the Flag D service APIs, right?
Okay.
Nice.
This is amazing.
Do you mind sharing the second link, that you're showcasing?
I want to take a look for…
**antoninbruneau** 26:24 Sorry.
**Shenoy Pratik Gurudatt** 26:25 Do you want to share the second link that you're It's appropriate.
**antoninbruneau** 26:29 private repos. I can share, but you won't have access.
So, I'll figure out how we can contribute that to the…
**Shenoy Pratik Gurudatt** 26:36 Yeah.
**antoninbruneau** 26:37 doing a 2D map.
**Shenoy Pratik Gurudatt** 26:39 Well, this is… this is exactly what I was planning to do with Valky, though, where I would have a new feature flag, but it would be on the memory side. Like, you have it on the latency, and A-B testing style of things. I was thinking of… Changing some database config using the feature flag service, so that it trips up the database and you'll start seeing errors, in the spans.
**antoninbruneau** 27:05 The, the… I mean, in our environment, for demo purposes, we are… More and more dropping the feature flag system to generate, issues.
Because, when we showcase our root cause analysis agent, it's too obvious that there is a feature flag being triggered.
And so that's why we use this proxy, and we also have a system with Argo CD and faulty versions of the services that get rolled out.
Frequently, so it's less obvious that there is a feature flag being triggered, and more like a faulty version of a service that's been deployed and then rolled back.
So…
**FELIX GEORGE** 27:52 I had, there is IT bench.
Sorry? So, there is an… there is a project called ITBench. It is a mechanism, it's… it provides some default ways to inject faults in a dummy application. So, they do support astronomy show.
Oh, okay. Yeah. I'm not sure it is just for databases, I'm afraid it's not just for… it's… it's across microservices, like latency, payload.
Like, you can inject wrong payload.
**antoninbruneau** 28:27 Okay.
**FELIX GEORGE** 28:27 So… If you want.
**antoninbruneau** 28:29 Put the name in the chat.
**FELIX GEORGE** 28:31 Yeah.
Can share the link.
**antoninbruneau** 28:42 Yeah, agents are too smart. Yeah.
**Shenoy Pratik Gurudatt** 28:56 Yeah, I think, some chaos engineering will also be helpful, because I saw the same issue when I was using agents and trying to root cause stuff. It just knows about the telemetry coming in from the astronomy shop. That's one thing. Like, it has inherent knowledge about the feature flags itself.
So the demo usually doesn't make sense that way.
**antoninbruneau** 29:19 It's a bit hard to do it in… pure Docker Compose. That's why we are using… in our case, we are on cube with ArgroCD, because it's easier to just… Ask it to run a new image of the component, and this image contains the faulty code.
and then roll back, and it's less obvious for the agents that… I mean, the agent knows that the new version has been released, but doesn't have access to the source code, and there is nothing in the log, or in the trace, or in the payload that that tells that there is a feature flag.
**Shenoy Pratik Gurudatt** 30:01 Do you also add, deployment and CICD logs in? I'm just wondering.
**antoninbruneau** 30:08 In our demo environment?
**Shenoy Pratik Gurudatt** 30:10 Yeah.
**antoninbruneau** 30:11 Yeah, we monitor the GitHub repair, the GitHub Actions for CI visibility.
**Shenoy Pratik Gurudatt** 30:20 Hmm.
**antoninbruneau** 30:20 Trade, yeah.
**Shenoy Pratik Gurudatt** 30:22 Yeah, just because people are using it as an additional signal these days, that agents can use and debug things with.
So if something goes out of box, they'll check the deployment, and then they'll go back and revisit the code change.
**antoninbruneau** 30:37 Yeah, I mean… we don't push it that far, but it's more like you… you… it's more to provide insights on the performance of the CI, so how long it takes to release, how long… from the release on the CI to the availability on the website, on the… Pods, how long it takes.
Things like that.
**Shenoy Pratik Gurudatt** 31:05 That's super insightful.
**antoninbruneau** 31:14 Okay?
**Shenoy Pratik Gurudatt** 31:15 Cool. Yeah, so I would, really request if you could push anything on the database monitoring side more, that would be helpful.
**antoninbruneau** 31:26 On the database monitoring?
**Shenoy Pratik Gurudatt** 31:27 Yeah, for the proxy thing that you mentioned. It's a really good addition, I feel.
To start with, and then… Yeah, the chaos engineering part is also really nice to demo it later on when… I know all the downstream folks that are there for Astronomy shop are going into agent observability and agentic observability both. So that's where something like… something like a chaos engineering tool will also help.
Because it deviates from your regular feature flags.
Yeah. We can see what's the difference between Kubernetes and Docker, and how to mimic something similar, where you have two container images and one spawns up. But I know it's very easy with Kubernetes, it's not that easy with Docker.
**antoninbruneau** 32:12 Yeah.
**Shenoy Pratik Gurudatt** 32:13 Yeah, one monitoring, process that is missing.
**antoninbruneau** 32:20 They're kidding.
**Shenoy Pratik Gurudatt** 32:21 Boom.
Mental check.
**FELIX GEORGE** 32:23 I tried out your changes, so I did a simple way, I just copied, the changes in the auto collector to my branch.
it out, but I'm still seeing trace loop spans.
**Shenoy Pratik Gurudatt** 32:39 It should have both, GenAI and TraceLoop both.
To have general prefix attributes as well.
**FELIX GEORGE** 32:47 Okay.
But I, I, I don't see… okay. Yeah, I can see both.
**Shenoy Pratik Gurudatt** 32:53 Okay, that's the… I think the aim is to just append and add some extra stuff.
**FELIX GEORGE** 32:58 Okay.
**Shenoy Pratik Gurudatt** 32:58 Yeah, if you want.
**FELIX GEORGE** 32:59 I can also share the trace that I got with.
**Shenoy Pratik Gurudatt** 33:02 Yeah, yeah, you can put it, and then… I have a review comment there.
So that Juliana also has some, context.
**FELIX GEORGE** 33:11 Yeah, I didn't add that.
**Shenoy Pratik Gurudatt** 33:13 Cool.
**FELIX GEORGE** 33:14 So, I also had one more PR, which is, like, to fix some… Documentation issues, are based in the chat.
**Shenoy Pratik Gurudatt** 33:23 Yeah, that I think Donald already approved, right?
**FELIX GEORGE** 33:28 Yeah.
**Shenoy Pratik Gurudatt** 33:29 Yeah, I saw that it's a pretty, normal one.
**FELIX GEORGE** 33:32 And also, you ran the other one, right? MCP port dependency, you merged it with the main, but again, see that agent telemetry test and build demo images, they are skipped.
**Shenoy Pratik Gurudatt** 33:44 That's only when someone approves it. If…
**FELIX GEORGE** 33:48 Okay.
**Shenoy Pratik Gurudatt** 33:48 either approve the PR, I'll, re-approve if you want.
the board stuff… Is it skipped? Yeah, it is skipped. Let me re-approve this, and then it will run again.
**FELIX GEORGE** 34:00 Okay, welcome.
Fuck.
**Shenoy Pratik Gurudatt** 34:06 Hmm.
You see the two ones.
Yeah, I don't know if these guys are releasing the code this week for 3.0.
But if not, if it is pushed to next week, probably you can think of getting the load gen in. I know it's a big pull.
Yeah.
**FELIX GEORGE** 34:25 Yeah, but with the new change, sure, because we already have a version for the Locust one.
**Shenoy Pratik Gurudatt** 34:32 Hmm.
**FELIX GEORGE** 34:33 Locker-based logging.
**Shenoy Pratik Gurudatt** 34:34 The A6 also changing, you don't want to do it twice.
**FELIX GEORGE** 34:38 Yeah, because I don't have the context with K6, I'll have to check how I can port this. But the questions, I think… I think I have a… I also have sent the, questions to you, right? Like, a JSON list of questions.
**Shenoy Pratik Gurudatt** 34:55 That was looking good, like, it's the basic, scenarios that we have, so…
**FELIX GEORGE** 34:58 I think it's just about plugging those in, those questions in into… Like, yes.
I can… yeah, once this case is code merged, I will… I'll try that.
**Shenoy Pratik Gurudatt** 35:12 Got it. Then just to take a look at that PR.
**FELIX GEORGE** 35:16 Yeah, I'll update my comments, and the praise that I got.
**Shenoy Pratik Gurudatt** 35:21 Cool.
And that should be good.
Oops.
**FELIX GEORGE** 35:25 Thank you.
**Shenoy Pratik Gurudatt** 35:25 Thanks, Felix, for joining in. Bye-bye.
**FELIX GEORGE** 35:27 Bye.
