SIG: Community Demo App SIG
Date: 2026-02-11
Duration: 30 minutes
Zoom Recording URL: https://zoom.us/rec/share/BMlqTkGCQ3mxk-0SpBQnKxJi6qiflUNfTyakykKof-aE6g534nte8PjMcIM8He3q.r5Cyu5Db3ZG5WNKH
============================================================

## Zoom Recording Transcript

**Juliano Costa | Datadog** 00:12 Hello, hello!
**JM Juande Manjon** 00:15 Hello?
**Juliano Costa | Datadog** 00:17 How are ya?
**JM Juande Manjon** 00:19 Hi, good, how you doing?
**Juliano Costa | Datadog** 00:21 Oh, good, oh good.
Is it your first time? And .
**JM Juande Manjon** 00:27 Yeah, this is my first time.
**Juliano Costa | Datadog** 00:29 Cool. Yeah, welcome.
**JM Juande Manjon** 00:31 Thank you.
**Juliano Costa | Datadog** 00:32 Let's just give a couple of minutes to see if anyone else will join, but in the meanwhile, do you have anything in mind that you would like to discuss?
**JM Juande Manjon** 00:44 Yeah, so I… personally, I think yesterday I opened an issue to support Opam in the OpenTelemetry demo.
**Juliano Costa | Datadog** 00:51 I saw, I saw the issue, yeah.
**JM Juande Manjon** 00:53 I used to work with the Pansi.
I'm not yet a maintainer, but mainly helping with the… Agent and server example.
**Juliano Costa | Datadog** 01:04 Okay.
**JM Juande Manjon** 01:05 moving then to help the community to understand better how Open can help OpenTelemetry users.
**Juliano Costa | Datadog** 01:15 I like the idea.
We just need to…
**JM Juande Manjon** 01:28 Yeah, I've been looking…
**Juliano Costa | Datadog** 01:29 There's a bit…
**JM Juande Manjon** 01:30 Yes. To see how that would fit.
**Juliano Costa | Datadog** 01:33 Because currently, the demo has one collector. I mean, for demo purposes, having O-PAMP would be nice, even if it's an overkill, but yeah, I like it.
**JM Juande Manjon** 01:44 Right, so for the Docker Compose, it's easier, right? It's only one collector, but maybe on the Kubernetes, it's… is how to deploy Open using The operator, how we can… Manage different collectors running in different nodes.
**Juliano Costa | Datadog** 02:07 Yeah, currently, we do not have, we do not use the operator.
We have a Helm chart.
for religious.
Mainly because… Ugh, give me a second, I need to check that.
Because we… we recently changed, the Helm chart.
Let me see… I don't think we are using… The operator.
**JM Juande Manjon** 02:38 Right.
**Juliano Costa | Datadog** 02:38 Go ahead, sorry.
**JM Juande Manjon** 02:39 Also, also in the Docker Compose, you can scale up and have more than one collector.
To simulate that you have a collector gateway where other collectors are sending information, and you can dynamically modify the configurations.
**Juliano Costa | Datadog** 03:06 Where is the… Changelog… Yeah, so last addition was running the collector as a daemon set.
And enabling kids, info monitoring.
But we do not use the operator.
of… I think our choice there was mainly because the operator would, instrument the code, and we do not want Because the services are already instrumented.
So the double instrumentation would be… Well, it would crash, stuff.
**JM Juande Manjon** 04:00 But I think it won't be a problem, because basically, the… There is a supervisor that is a cycle process that actually will communicate with the, collector.
And so the collector will communicate with the supervisor, and supervisor will communicate with the PAN server.
**Juliano Costa | Datadog** 04:20 Cool.
**JM Juande Manjon** 04:21 employ the supervisor using chart, I think, but I need to double-check with the… With the supervisor owner.
**Juliano Costa | Datadog** 04:29 And a quick question on that, we would need to add one extra service to the demo? Like, the supervisor, or, like, not the supervisor, but, like, the opam server?
**JM Juande Manjon** 04:42 Yes, the OpenServe it.
**Juliano Costa | Datadog** 04:44 That… It would be that. And then in the collector, we configure the extension.
**JM Juande Manjon** 04:50 We use the Alpine extension.
straightforward.
**Juliano Costa | Datadog** 04:56 Yeah, cool. Yeah, one thing that we had… so, I don't know if you know, but last week we had a community event called Hotel Unplugged.
In Brussels, And, we had a bunch of, So, it was an unconference, and people could… Choose what they want to discuss.
And one of the discussions that we we sat together to discuss was about the demo. And one thing that we wanted to do was creating a smaller demo to be able to run locally, because actually that was the goal initially.
I know that nowadays the laptops are super powerful, but we still have folks that do not have a super powerful laptop with 64GB of RAM, so sometimes they cannot They are not able to run the demo locally.
So they were thinking on how we can reduce the size of the demo in order to… run locally. And, yeah, we are always, like, how can I say, new service.
concern… we always have concerns about adding new services, but I feel that this is a good, a good service to be added, so, yeah.
**JM Juande Manjon** 06:27 Yeah, it consumes very low resources, so we… recently, we had an option to scale up the number of agents, or the number of collectors. So we do some benchmark using, like, a source and collector running.
And… and overhead was minimal.
**Juliano Costa | Datadog** 06:47 Cool. Okay. Yeah, let's, let's do it. Would you be able to, work on it? Yes, yes.
**JM Juande Manjon** 06:57 I would… maybe for the Kubernetes part, maybe I'm gonna need some support for the Docker Compose is… Good.
**Juliano Costa | Datadog** 07:05 Yeah.
**JM Juande Manjon** 07:06 I look at that, I don't see any problem. So, I saw that the Docker compose for the minimal configuration is broken.
He has some issue with, with the SQL server, I think.
**Juliano Costa | Datadog** 07:23 Okay.
**JM Juande Manjon** 07:24 Yeah, but for the Trevor Docker Compose, I ran it. I was able to integrate the Open Server.
Easily.
**Juliano Costa | Datadog** 07:34 Okay.
**JM Juande Manjon** 07:36 Aquinity and E2 again.
To see. So, maybe we can do it in two steps. The first step is doing a quick demo with the Doki Compose.
So being working on a new UI that… because the current UI is very rudimentary.
But, hello. So, yeah, I mean, we can do this two-step.
**Juliano Costa | Datadog** 08:04 Yeah, definitely. I like the idea.
And… Everything that we release on… So, everything that we merged on the demo on the demo repo, it's just updated in the Helm whenever we have a new… A new release.
So, as long as we do not push a new release, we can take the time that we want on adding that to Kubernetes.
But, that's cool. Johnson, just so you are aware, we are discussing about adding your pump to the demo.
**Jonathan Munz** 08:54 Adding what, sir?
**Juliano Costa | Datadog** 08:56 OPEMP.
like, the… Supervisor to manage fleet collectors.
**Jonathan Munz** 09:04 Oh, okay.
Okay. Hello.
**JM Juande Manjon** 09:07 Yeah, so to provide the ability to change the collector configuration on the fly.
**Jonathan Munz** 09:13 Yeah, interesting. Okay.
**Juliano Costa | Datadog** 09:15 Juan, let me ask you one thing.
How much, actually, People use it.
Not saying that it's useless, I'm saying that I like the idea, but we also have… a lot of… users using GitOps, so Argo and stuff. So, like, if they want to change collector configs, they push a PR with the config changes updated, and that's applied to their whole cluster.
If I do via OpEmp, I do not have control over the configuration that I'm running, because this is not updated to my REPL, so… How… how… how do you see this being used in real life?
**JM Juande Manjon** 10:10 In real life, commercially, actually it's used by buying plane. I don't know if you have seen biplane, so you can manage a fleet of collectors connected to, observing, pipelines, data pipeline between the collector and the backend. And, and, and by plane, not for biplane, but, commercially, this is the one that is on top using Open, so you can manage the fleet in terms of changing configuration, changing rotating certificates, and so on.
Bye.
**Juliano Costa | Datadog** 10:47 Are you…
**JM Juande Manjon** 10:48 Well, no.
**Juliano Costa | Datadog** 10:48 Are you with, Bain Pain? Sorry?
**JM Juande Manjon** 10:51 No, no, I'm not working there. I'm working at Intuitive Surgical. My goal is to use a pod to manage, to supervise and control the robots in the operating room in the hospital.
**Juliano Costa | Datadog** 11:06 Oh, nice.
**JM Juande Manjon** 11:08 Yeah.
I was saying that with the PAN capability, you can… First, check the health of the collector.
In case of biplane, they have extra, A processor that can help to identify how much data you're processing, and you can tweak on of different flags to reduce the amount of data that you are sampling, for example.
On this kind of stuff.
**Juliano Costa | Datadog** 11:43 Yeah, no, no, I do see the value of it, and I was just wondering.
What is the feedback that we get from the community, like, from end users, when we think about this going… going exactly against, what the world has been pushing for, like, Control the… get… have everything as config as code, and then you have, your configuration versioned.
And if you need to change something, you change there, and then this is applied across your nodes and your fleet. But you managed on the code side first.
This is, like, out of curiosity.
**JM Juande Manjon** 12:32 You have your initial configuration.
But when you deploy that node, so you can change that configuration depending on the circumstances in real life.
**Juliano Costa | Datadog** 12:43 Yeah, but then this is the… this is my… This is my main, main question, like, if we change the things on the fly without updating our… our version code.
we kind of lose control over what we have on the REPL and what we are running.
**JM Juande Manjon** 13:08 Yeah, so… That's true.
But on the other side, you will have only one static configuration that you cannot change at all.
I mean, you need to handle, like, a thousand of collectors, and you… It depends. So, there are proprietary solutions, so basically, you can define groups of collector And when the collector belongs to that group, you can adapt and change and apply different configuration to different groups.
Or different regions, for example.
**Juliano Costa | Datadog** 13:42 Cool.
Okay.
Nice, nice. Yeah, no, I… I… I like it.
**JM Juande Manjon** 13:49 On the other hand, you can set up Open on the collector side in the extension to see how much of things you can set up. I only want to report the health of the collector.
So, the server cannot reconfigure the collector.
Okay, and the other thing is, the open does is when you apply the configuration, if the configuration fails, the supervisor will roll back to the previous configuration, for example.
So imagine that you modified the configuration, and now that configuration doesn't work.
For any reason. So what you can do, you need to deploy again.
The collector, you can dynamically solve this kind of problem.
**Juliano Costa | Datadog** 14:35 Okay, yeah, in that case, makes sense.
But we… yeah, yeah, you said that it rolls… rolls back automatically to the last working one. Okay, yeah.
Cool, yeah, no, let's, let's go for it. I think, the world.
lacks OpenMP demos, so adding that to the… To the hotel demo is, is nice.
**JM Juande Manjon** 15:05 Yeah, so would the… The palm is completely as an optic, So, we're meaning that there are some… Changes on the extension to support a telemetry collector, but it can use it in different use cases.
For the demo, basically, it's OpenTelempty Collector Support.
But depending on what feature you want to use, so basically we can… Restart the collector with a new configuration, or we can monitor the health.
There are other options where the Open support custom messages, where you can't have your custom extension.
And you can send information between the collector and the open server.
But in that case, you need to extend the OpenServer to support this kind of communication.
**Juliano Costa | Datadog** 16:03 Yeah, I think we can start with the basic thing, and maybe evolve from there.
Yo.
Cool.
And I need to fix the minimal build. Thanks for that.
True.
I, I, I, I don't want the minimal… Anymore.
**JM Juande Manjon** 16:27 Thank you.
**Juliano Costa | Datadog** 16:28 Okay.
**JM Juande Manjon** 16:28 Wasn't installed with the Podres server, something like that?
**Juliano Costa | Datadog** 16:32 Okay.
Prosperous.
**Jonathan Munz** 16:36 I had noticed, yes, I… had spun it up recently, I believe I un… I… commented out one of the dependencies with Postgres, and then it worked, but yeah, there was something that wasn't spinning up correctly on Minimal.
**Juliano Costa | Datadog** 16:54 Okay, yeah, we had some changes recently.
on the… on one of the services, I think Image Lo… Image… it's too many services now, I don't remember the name. Like, the image provider, and I think Image Provider out now fetches the… the images from… From a database, or whatever.
And… Yeah, maybe… PR forgot to add to the PR, and I forgot to validate, and yeah.
So, that's why I didn't want to have two Docker composed. Actually, we have four. Ideally.
Ideally, we would have one.
**Jonathan Munz** 17:45 And… maybe work with profiles?
**Juliano Costa | Datadog** 17:49 We discussed, just to… something that I, I, I shared with Juan de Jonathan. We… We discussed a bit on the autoimplant last week.
**Jonathan Munz** 18:02 Okay. And there was a big push from… from the folks in the room to kind of have,
**Juliano Costa | Datadog** 18:11 Lighter version of the demo?
and… one of the… so it… Yeah.
So we sat together, and we started discussing, and people were like, yeah, maybe we should remove all the dependencies from the vendors. So, like, do not have Provitus, Grafana, OpenSearch.
And then that already reduces some memory consumption, because just open search is, like, 1 giga?
And I was like, yeah, that's cool, but, like, how people would… view their stuff.
No, but then we could provide, like, A default one, and I was like, and how is that different from what we are doing now?
**Jonathan Munz** 18:58 Yeah, yeah.
**Juliano Costa | Datadog** 18:59 Because people can change their backend as they wish. That's what I do. When I run the demo, I send the data to DanaDoc.
But… if, like… Yeah, so this is the thing, it's, yeah.
**Jonathan Munz** 19:19 I think it's what… yeah, I think it's worth a deeper dive. I mean, this is what I find. I was about to mention open source, like, that's a good example where open search is in the minimal. I usually comment that, because… has that extra overhead, and in a lot of, like, quick things I want to do, I don't care about it, and so it's easier just to not have it.
So, I think a solution where there is one Dockerfile and there's reasonable defaults, but it's highly configurable, is kind of where you want to go. It's like, okay, this is everything, and we know it works, and we know it's internally consistent, and here's your local .whatever configuration where you turn on or on… and whether you start from the bare minimum and go up, or start from the full and go down, I think either works fine, as long as it's clear.
okay, I have my preferred set of things, but yeah, I think it's a larger discussion, because I agree, having two completely different Docker files is just gonna… it's gonna be easy to introduce inconsistencies again, so…
**Juliano Costa | Datadog** 20:25 Yes.
Have you heard of Aspire before?
I have no idea. So, there is this, .NET thingy… thingy?
And they have… They have this… Aspire Dashboard?
And it's a single container where you can see traces, metric slots.
And they accept OTLP.
The problem is that they are not a CNCF nor Linux Foundation, project. They are open source, they are, I think Microsoft, yeah. They are Microsoft, Microsoft project.
Open source, 50 contributors, whatever, yeah.
That could be, like, a workaround?
Because then we could… drop.
Open search.
Prometheus.
Grafana… Jaeger?
And replace with one single service, this Aspire. And then, of course, oh, do you want to use Grafana? Cool. Here is the link to the Grafana stack.
And then Grafana provides an extension on the Docker Compose file, where they have LGTM.
Because when you are sending stuff to Grafana, they… I think they would rather you use LGTM other than OpenSearch and Jaeger.
I mean, I think behind the scenes, they use Jaeger, whatever. But, like, for Datadog, send everything to Datadog. You do not need to have, all the other services. So, this would be something But, yeah, this is, like, a bigger discussion, as you said, and… yeah.
**Jonathan Munz** 22:28 Yeah, it looks cool.
**JM Juande Manjon** 22:30 I used SPI a couple of times, My only concern was that the UI just is not very friendly, Especially when you're trying to look for attributes, to filter by attributes.
**Juliano Costa | Datadog** 22:45 Yeah, and also the metrics, it basically gives you all the metrics, like… And, of course, we cannot… demo all the other cool stuff that you can do with, like, alerting, and create a specific dashboard for Collector, as we have now with, with the Grafana dashboard that we have embedded. So… again, I don't know. We had a big push from Dalton, from, OpenSearch, like… He, he wanted to, to have… The open search… solution. I think they, they support traces, metrics, logs, everything, so we could simply send to OpenSearch, because… OpenSearch is a Linux Foundation project, and then we would drop Grafana, Prometheus, and, Jaeger.
But, honestly speaking, how many companies actually use open search in production compared to like, what… When we… when we chose to deploy Grafana in the demo, we chose it because it was the most known in the open source space, and this was one thing that I shared… I shared with the room, like.
nobody from Grafana was in that discussion, and we still chose Grafana. Like, it was myself, a character from Microsoft, Pierre from Honeycomb, and Alstein was in another company that I don't remember.
But, yeah… Like, and still we chose Grafana. So… Honestly, I don't know, like, and I need a bigger group, I need the rest of the maintainers to discuss this.
And also, of course, you guys, and whatever other folks that are using the demo.
So… Should I open a discussion, just an issue, and start this, like.
Brainstorming this? What do you guys think?
**Jonathan Munz** 25:02 I think so, my only comment would be, I think there… I think I would… I would… push for that to be a different discussion of what we first started. Like, I think the issue.
**Juliano Costa | Datadog** 25:10 Yes.
**Jonathan Munz** 25:11 Docker and Docker minimal and wanting different profiles is separate from… because I think that helps. I think if you reduce… The amount of things?
getting rid of open search in favor of one, that helps that issue, but there's still that fundamental issue of having those two different setups and switching that to more of a… profile-based or, or, you know, whatever, whatever the solution is. So, yeah. But yeah, that sounds good, starting a discussion.
Or starting an issue, I mean.
**Juliano Costa | Datadog** 26:19 Okay.
Yeah, pool.
I think if we can… the thing also is, like.
There are a couple of leave services that are easy to drop. For instance, quote.
We could have a feature, we could have an environment variable there on the… on the… shipping.
That if that environment variable is on, do not call quote, just return a value.
And, like… That would produce one service. And we can do this with a couple of others.
a couple of other services. And I think in the minimum.
Today, we do not have Kafka accounting and fraud detection.
So this would also be something, But then we would just need to have a proof, like.
discounting the profile way of doing, because… then we can keep in one single container… in one single Docker file.
Okay, yeah.
I need to sit and write down, some issues.
So we started working.
Cool, yeah.
Jonathan, I, I want to ask you one, one favor.
**Jonathan Munz** 27:59 Sure.
**Juliano Costa | Datadog** 28:00 We got a PR, from Dependabot.
That bumps the… the… Grado version for the Reactive Native app.
would you be willing to take this PR and also maybe bump all the other dependencies? And just to… because I think we do not have… them up to date.
**Jonathan Munz** 28:34 Right? We…
**Juliano Costa | Datadog** 28:36 Yep.
I think… I think we removed from… from… What is it called?
**Jonathan Munz** 28:48 This one, right?
**Juliano Costa | Datadog** 28:50 From the Pentabot.
2975… Yep, exactly.
**Jonathan Munz** 29:01 Yeah, so basically just… Making sure everything still builds with that bump, and then seeing if there's other stuff in there that's worth bumping at the same time.
**Juliano Costa | Datadog** 29:12 Yeah.
**Jonathan Munz** 29:12 Okay.
Yep, and feel free to… I think…
**Juliano Costa | Datadog** 29:17 Huh.
I think you do have permissions to push to this PR… to the PR itself.
**Jonathan Munz** 29:26 I believe so.
**Juliano Costa | Datadog** 29:27 Yeah, so feel free to push to the PR if you need, and then I can review the whole thing.
**Jonathan Munz** 29:34 Oh, okay.
**Juliano Costa | Datadog** 29:36 Awesome, yeah, thank you.
Yeah, it's been… I think Roger is on holidays, Pierre is away, so, Oh, like, I'm here crying under the shower, like, all by myself.
Cool. Appreciate it. Yeah, thanks. And, yeah, Juan, hope to see the PR coming?
So, if you want to discuss anything related to that, yeah, happy to.
**JM Juande Manjon** 30:09 Okay, thank you.
**Juliano Costa | Datadog** 30:11 Awesome. Thanks for joining, and hope to see you more time.
Yep. Thanks, everyone.
**JM Juande Manjon** 30:18 Okay, bye.
**Juliano Costa | Datadog** 30:19 Bye.
