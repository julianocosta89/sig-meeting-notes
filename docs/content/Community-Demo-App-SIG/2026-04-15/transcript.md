SIG: Community Demo App SIG
Date: 2026-04-15
Duration: 34 minutes
============================================================

## Zoom Recording Transcript

**Cyrille Le Clerc** 00:31 Hello, Pierre, how are you?
**Pierre Tessier** 00:36 Good morning.
Good afternoon, I guess, depending on where you are.
**Cyrille Le Clerc** 00:41 Afternoon for me.
**Pierre Tessier** 01:00 I'm happy we're moving these to weekly. I've got a list of things I'd like to chat about, and I doubt we will have time to chat through them all.
**Cyrille Le Clerc** 01:07 Yeah.
**Pierre Tessier** 01:09 And I'm sure other people have things as well.
**Cyrille Le Clerc** 01:12 I, yeah, I, I struggle, because at the same time, I have many things I want to discuss, and I have, committed that space.
**Pierre Tessier** 01:23 Yeah.
He started writing them down in the, the doc beforehand, like, you know what? I'm just gonna write them down so we don't forget, but… Yeah, we'll take it from there.
**Donal O'Sullivan** 01:40 Hey guys, how are ya?
**Pierre Tessier** 01:41 Good.
**Cyrille Le Clerc** 01:42 Hello, Donan, how are you?
**Donal O'Sullivan** 01:44 Good Zero, how are ya?
**Cyrille Le Clerc** 01:46 Einstein.
**Donal O'Sullivan** 01:47 Here's… Pierre, is it? I don't think I've met you before.
**Pierre Tessier** 01:51 Hello! I, I took a… A much-needed break from things for a bit there.
And, back now with my new employer, and they have a mandate that, we make this hotel demo better.
And, I was like, oh wow, I'm just a person for that.
**Donal O'Sullivan** 02:12 Please.
Nice to meet you.
**Juliano Costa | Datadog** 02:18 Hello, hello!
**Cyrille Le Clerc** 02:20 Hello, Giuliano, how are you?
**Juliano Costa | Datadog** 02:25 Alive.
**Pierre Tessier** 02:26 Live, that's positive.
It's positive.
**Donal O'Sullivan** 02:35 Always close.
**Juliano Costa | Datadog** 02:36 Yeah, all natives… English native speakers that I know, they reply not too bad, which is, like… It's not too exciting, to be fair, as well, so… Alive seems… sounds… at least… Something. Cool. So, do we have any… Anything…
**Pierre Tessier** 03:09 We do.
**Juliano Costa | Datadog** 03:12 Where are my Sikh meeting notes? They're gone.
Come on.
**Cyrille Le Clerc** 03:20 Oh, yeah.
**Juliano Costa | Datadog** 03:22 Oh, I lost it. I will… I think we have… On our eternal, right?
**Pierre Tessier** 03:30 Yeah, we've got a lot of things that, you know… and I've got more things I wanted to chat about as well.
But let's see what we can do first.
**Jonathan Munz** 03:42 Just a heads up, I have to go in about 15 minutes, so I think there was one topic related to it.
**Pierre Tessier** 03:47 The first topic is yours, Jonathan.
we're trying, you know, dependent bot's trying to move us from Gradle 8 to 9.
And there are issues with that, with the Android app and the Expo XDK.
And then when I started looking at what was required, I'm like, wow, this is way bigger and way out of my league. And I'm so happy you're here.
**Jonathan Munz** 04:12 Yeah, I was just gonna… I mean, in general, I mean, this is a problem with the React Native ecosystem in general, that, it's… And there's all this tooling around it, too. It's pretty difficult to jump from one version to another. Honestly, I think the way to approach that, and I can take some time to do it, is to create a new React Native. Like, the app is really simple. I think the easiest thing to do is create a new React Native app on the latest… Expo React Native that uses Gradle 9, and just poured over… like, the UI and the changes, like, it's… the actual app is really small, like, the config.
**Pierre Tessier** 04:47 Yeah.
**Jonathan Munz** 04:48 is 90% of it, so I think that's the quicker path to getting a version that works with Gradle 9.
**Pierre Tessier** 04:55 Okay.
Can we get you, then, to take on that task of just moving it up?
**Jonathan Munz** 05:03 Sure.
**Pierre Tessier** 05:03 And then, we will figure out the Dependabot thing, because there's other services that need to push to 9, and we'll just hold back the, the React Native app for now.
**Jonathan Munz** 05:16 Yeah, I think that's the other thing I was gonna say, like, if it's possible, like, I would… I would definitely just upgrade Gradle everywhere else and treat.
**Pierre Tessier** 05:22 Yep.
**Jonathan Munz** 05:23 That directory is independent.
**Pierre Tessier** 05:25 We will, yeah. I need to figure out how to configure Dependent Bot to do that. I'm not even sure I can, but… We will figure that out, or we'll just let Dependent Valley keep on trying to push updates, and we'll just ignore them.
Yeah.
**Juliano Costa | Datadog** 05:36 We… we can definitely configure that. It was like that before, and I forgot the name of the… our new approver. Jesus.
**Pierre Tessier** 05:50 Can we configure it to ignore a dependency for a specific folder only?
**Juliano Costa | Datadog** 05:55 Yes, we can.
**Pierre Tessier** 05:56 Okay, that's.
**Juliano Costa | Datadog** 05:57 I wanted to make sure. Yeah, yeah, yeah. So, Peter from Splunk, he, he added everything back.
And that's when we started getting the, the reactive native into the Pinabot PRs as well. But I think he actually added, because we were getting a lot of security… Security issues that were related just to dependency bumps.
So, he wanted to decrease those security… issues. So, not sure… like, I know that it's not a simple dependency bump for Reactive Native, because it breaks, and it's pretty tricky to test, because sometimes I test locally, it works, I ping Jonathan and say, hey, can you test it? And he says, yeah, it's not working. I'm like.
So, yeah. Okay.
**Jonathan Munz** 06:56 I'd say going forward, it makes sense to have it… even if we don't ignore it, it makes sense to treat the React Native dependencies as separate, just… they like… I mean, it's only very recently that a version of React Native even supports Gradle 9, so… at the very least, there'd be different buckets of Dependabot PRs, and you could treat them differently, even if long-term they're not ignored, but yeah, I would keep that.
**Pierre Tessier** 07:18 It'd probably be a better idea.
Juliano, if we could force the Panabot to… always do the React Native, or almost configure a separate but dependent bot just for React Native. So it's PRs are React Native only, and don't include other services.
I think that probably is our… a better goal there.
**Juliano Costa | Datadog** 07:39 I think… I don't… I need to check the Penabot. I know that this is possible, with Renovate.
**Pierre Tessier** 07:46 Yeah.
**Juliano Costa | Datadog** 07:47 But I, I…
**Pierre Tessier** 07:51 Renovate had its own headaches.
**Juliano Costa | Datadog** 07:54 Yeah, but I'm almost sure it is possible, so… I'll add that.
**Pierre Tessier** 08:01 Awesome. Thank you, Jonathan. We appreciate this.
The other item here is the, The Prometheus is the new info function with resource attributes.
Who is the person who wrote that PR?
**Cyrille Le Clerc** 08:25 It's my colleague Arv, but he didn't join.
**Pierre Tessier** 08:29 Okay.
**Cyrille Le Clerc** 08:31 I forgot to ping him, I didn't have the time.
**Juliano Costa | Datadog** 08:34 I met Aave during KubeCon.
Nice.
Okay, yeah, it's nice to.
**Cyrille Le Clerc** 08:40 tomorrow.
**Juliano Costa | Datadog** 08:41 Person, personally, yeah, yeah.
Cool.
**Cyrille Le Clerc** 08:45 Okay.
**Pierre Tessier** 08:46 My feeling is we're early for this.
I think we're a little bit early for it, and we're trying to force something through, and the rest of the OTEL ecosystem is not set up yet for the transforms that Prometheus needs to make this work properly.
**Cyrille Le Clerc** 09:05 I am a bit biased, I have skin in the game, but I tend to agree with you, and I remember with Giuliano when we were at the Hotelon conference.
talking about Prometheus and hotel, the question of resource attribute was the biggest pain point highlighted by attendees.
And they all said, we do resource attribute promotion, we don't do… we don't like joints.
On joints on infrastructure metrics.
other challenges that they require joint impromities for a hotel infrastructure metric.
have the challenge that they require service instance ID and server name, which are not standardized, not required for Infra-monitoring metrics on… Not that frequently used.
So, yeah, so I am aligned with you, it's a bit premature. But if the Prometus community writes… On its own dock.
We deprecate resource attribute… we discourage resource attribute promotion in favor of, joints.
Within…
**Pierre Tessier** 10:12 Yeah, I think there's also, you know, like, we were noticing, I forgot which ones they… I think they were the Postgres metrics. We had to do all these transforms on them, because they didn't have the right attributes, right?
And then you look at all the other infametrics, like Kafka and everything else, we're gonna be running into very similar things again.
So I would almost prefer if the hotel receivers and the collector would get ahead of that before we started adding it to the… To… to what we do.
**Cyrille Le Clerc** 10:45 Yep.
**Pierre Tessier** 10:46 Only because it's gonna make so much additional code in our transforms, it's gonna make it feel very hard to use OTEL.
When, you know.
**Cyrille Le Clerc** 10:54 Yeah, only it would not be the same pipeline for, It would be a Prometu-specific pipeline versus, all those are.
**Pierre Tessier** 11:05 Other vendors, yeah. Which, okay. So, alright, let's decide to table this until it's further. I think we should have an issue to track for it.
And we should revisit it.
I don't know, in a few months?
let the community catch up a little bit. But yeah, it's definitely something we should support. Just like we support sending OTLP data natively to Prometheus, we should continue to go down the path of honoring that OpenTelemetry and Prometheus marriage.
Just… not… yet.
**Cyrille Le Clerc** 11:38 Yeah, we desire a solu- to have a solution that doesn't require a custom pipeline.
**Pierre Tessier** 11:44 Yeah, and transforms.
**Cyrille Le Clerc** 11:47 transforms.
And I would say plus guidance from the Prometus community, because the Prometus community, in its documentation about the OTLP endpoint, has this big block about resource attribute promotion.
**Pierre Tessier** 12:12 Okay. I'll close the existing PR that we have for this, and it'll create an issue to track.
For future. Make sure that we're all part of that.
And we'll come back and revisit it.
Cindell, are you the one behind this, Grafana's dashboard thing in the helm chart, is that somebody else? I can't remember.
**Cyrille Le Clerc** 12:38 Yes and no. I have been waiting for this, calling for this for ages.
But, it's a community contribution. Rafana Labs is doing something a bit similar. So, if you remember in the Prometheus ecosystem, there is something.
**Pierre Tessier** 12:56 Cool.
**Cyrille Le Clerc** 12:56 Prometus CubeStack Mchart. Yeah. That deploys many things, and that comes with what is called a mix-in in the Prometus Profile ecosystem, which is a set of dashboards and alerts.
On, we, So one community member, took all these dashboards.
that we're relying… that are… we're relying on, promo-style metrics on adapted this to, Hotel collector style metrics.
These dashboards, roughly, they are super battle-proven. The telemetry showed by this dashboard is really battle-proven, because it's the Prometheus ecosystem who took years to build them.
So I think it's very compelling for the hotel community to be able to show that Hotel Collector can produce, such telemetry on, so it's really production-grade for… for, Kubernetes native, for, hotels collector native Kubernetes monitoring.
On AspGraphna is the solution that we… the dashboard solution we have.
The rational that resonate with me.
**Pierre Tessier** 14:19 I am.
**Cyrille Le Clerc** 14:19 Linux dashboard, the MySQL dashboard.
But I'm putting some cons also in the… Into the deck.
**Pierre Tessier** 14:27 Part of… part of me wishes… So I'm all good, like, yes, let's use the hotel demo to figure out how to build the perfect dashboards, but I don't want the hotel demo to… Own these dashboards.
I think they should be owned by something else, somebody else.
And the hotel demo just copies them from that community on a… Regular basis during updates.
So… And I say that because I think there should be a community-recommended way of… if you deploy a daemon set with all these receivers on it, and the standard operational way that we tell you to do things in your hotel community, and you send your data to Prometheus, here's your dashboards in Grafana.
You know what I mean?
And I think that should absolutely be something that the hotel community should have. We could start it in the hotel, but I would wish that somebody else not part of Hotel Demo would take ownership of it, even if it's, like, Grafana takes it over, or something like that, you know what I mean?
Hold on.
**Juliano Costa | Datadog** 15:32 What bothers me a bit about this, and I mentioned to Surreal already, is that the PR has 16,000 lines.
**Pierre Tessier** 15:40 Oh my god, yeah.
**Juliano Costa | Datadog** 15:42 It's just dashboards, I know, but yeah, it's still, like… I don't think… I don't think a person can review 16,000 lines.
**Pierre Tessier** 15:52 No, I think the only way you can review it is by deploying it and actually going through it. Of course, the fear there is, is there something hidden inside that we don't know about?
Because we can't actually read 16,000 lines of code as a human.
I don't disagree with you, Juliano, on this.
I also look at it like, wow, these are… this is a lot of dashboards. There's more dashboards here than we already, like, than we have deployed today.
Oh, yeah, it looks good to me. Oh, funny.
**Cyrille Le Clerc** 16:21 What's your statement, Pierre, about, finding another, home for these dashboards?
**Pierre Tessier** 16:27 Yeah, like, if they could live inside of the Grafana community itself, and say, here are the blessed by the community, I'd love that Grafana could put their stamp on it.
These are the dashboards that if you do the full OTEL stack sending to Prometheus.
Here's your dashboards. I'm sure they already do that today for Prometheus monitoring, right? I would love them to do that for… Yeah.
So…
**Cyrille Le Clerc** 16:55 That makes sense.
**Pierre Tessier** 16:59 For what it's worth it, I think it's okay to use the demo as a means to develop these dashboards.
But I would just want us to have, like, a clear path that they're gonna take ownership of this, or somebody else will, in the community, take ownership of it.
**Cyrille Le Clerc** 17:14 Maybe it would be the Kubernetes Monitoring GitHub project.
Because the mixing, Kubernetes mix-in is not owned by Graphana Labs, but by this project. Maybe it's a good room, who knows?
It's roughly the same people, but at least it's not Grafana Labs, the company.
**Pierre Tessier** 17:32 who owns Kubernetes Monitoring? Is that a CNCF thing?
**Cyrille Le Clerc** 17:37 No, it's just Grafana people.
**Pierre Tessier** 17:40 Oh, so Grafana people created Kubernetes monitoring?
Okay, I'm all… again.
**Cyrille Le Clerc** 17:46 Yeah, maybe that's a good.
**Pierre Tessier** 17:47 It's…
**Cyrille Le Clerc** 17:48 trade-off.
**Pierre Tessier** 17:49 It's very… I… I… I am okay.
**Cyrille Le Clerc** 17:54 Oh, there is one person from PolarSignal, so yeah, it's a bit, oh, no, no, there are two non-Grafana people.
**Pierre Tessier** 18:03 Okay.
**Cyrille Le Clerc** 18:04 Yeah, okay.
**Pierre Tessier** 18:05 in there. I see, I see familiar faces in here.
**Cyrille Le Clerc** 18:08 Okay, there are, yeah, yeah, so that's better, because it's not only Grafana Labs.
Okay, so yeah, I like your idea to say it should be… it should live somewhere else.
**Pierre Tessier** 18:18 Yeah, yeah, if we could get them to adopt owning them… And we'll use YotelDemo to help develop them. I think it's a great avenue where everybody wins.
**Cyrille Le Clerc** 18:27 Yep.
**Pierre Tessier** 18:29 Will you reach out to them, Sadil, or…
**Cyrille Le Clerc** 18:32 Yeah, we'll, try to find something.
**Pierre Tessier** 18:34 I feel like some of them are your colleagues.
**Cyrille Le Clerc** 18:37 Yeah.
Yeah, and by the way, I hope it will… there are people saying, yeah, Prometheus scraping is collecting more metrics than Hotel Collector, so Prometheus scraping is better, and say, do we really need these metrics?
Sure, maybe they are old on, outdated or whatever, and that would be a lot of fun with these dashboards to… to get the wheel meet the rubber.
**Pierre Tessier** 19:02 I like to avoid that conversation, and just say some people don't want to have Prometheus node exporters. They want to go full hotel stack, but they might have Prometheus backend, or a Prometheus-compatible backend, right? They might be using the Mirror, or Chronosphere, or who knows what, they just want the you know, community-bless dashboards for it. That's all.
**Cyrille Le Clerc** 19:22 Yep.
**Pierre Tessier** 19:24 I think that would… you know, and like I said, everybody wins here.
So…
**Cyrille Le Clerc** 19:31 Yep.
**Pierre Tessier** 19:32 Awesome.
**Cyrille Le Clerc** 19:33 Okay, decision…
**Pierre Tessier** 19:40 But let's go ahead and, I will review this PR as well, make sure everything all checks. I know you said some panels are still empty, I think it's fine.
You know, balances.
**Cyrille Le Clerc** 19:50 It's not the number of lines of code, but number of panels of queries.
**Pierre Tessier** 19:53 It's gonna… it's gonna create some potential issues. You know, maybe we put a beta label on each dashboard, I don't know. Does that solve for it? I don't really want to continue changing this PR, let's just get it done.
And, you know, make it a known thing, like, hey, it's a work in progress, and we… expect.
Grafana to own this.
Or Kubernetes mixed in to own it, I'm sorry.
**Cyrille Le Clerc** 20:23 Yeah, who knows what, but something.
**Juliano Costa | Datadog** 20:27 Yeah, I think if we have someone to call as code owner of the dashboard, someone that we can ping and we can rely on, that would be great, like.
**Pierre Tessier** 20:36 That's… yes.
**Cyrille Le Clerc** 20:38 Yeah.
See, my friend.
**Juliano Costa | Datadog** 20:40 Every time for the dashboard… yeah, every time a dashboard crashes, I'm like, oh, I don't know.
**Pierre Tessier** 20:45 And this is a lot of dashboards. This is a lot of dashboards, and Juliani, did you see the same thing? I said? Like, oh my god, the maintenance burden. Oh, crap. But the value is really powerful, and I hear people asking for this all the time, so… I want to do this.
Yep.
Okay.
I'd love to run through a couple more PRs that we have outstanding right now.
Maybe get some of these merged?
We have time?
I think particularly the first one I'm looking at is replacing Link Spectre with… I think it's pronounced Lychee?
The holdback here… Currently on it, I don't think Pyotr is here.
the Z.
No.
I think that the holdback on it is, The internal tooling for Lychee, it's based on Rust. You have to install it manually. You can do a brew install or a cargo install. I'm sure it's different for Linux and Windows.
Previously, we used an NPM package, so it made it really, like, kind of cross-platform, and it was easy to do it. So, I think the one, like, kind of remaining issue is, Do we care that people have to run an extra step manually before they can run check links from Makefile?
I think that's kind of the last thing on that, and if not, then I'd love to get this thing merged, because we have a lot of things we need to merge.
And they're not merging because Link Spectre is, You know, it's like 25% of the time it works now, and I'm like, I'm not doing this anymore.
**Juliano Costa | Datadog** 22:49 I was used to click merge and have the thing merged, and now I click merge, and then, like.
One hour later, I look at the PR, and I'm like.
**Pierre Tessier** 23:00 Didn't I merge that?
**Juliano Costa | Datadog** 23:01 immersed this!
**Pierre Tessier** 23:02 Yes, it's not merged, because you're linked.
Failed.
Randomly. So yeah, I'd love to get that. Like, do we have issues? Do I… should we add comments somewhere to indicate this? Do we care? I don't know.
**Juliano Costa | Datadog** 23:19 I… I think Peter, mentioned there, right, that this will change the… Just the local development.
**Pierre Tessier** 23:28 Anyway, just local dev, yeah.
**Juliano Costa | Datadog** 23:30 Yeah, so…
**Pierre Tessier** 23:31 Who cares? Okay, I am merging this right now.
**Juliano Costa | Datadog** 23:34 Welcome.
**Donal O'Sullivan** 23:35 manual step, so you… we used to do another.
**Pierre Tessier** 23:37 Yeah, beforehand, we would NPM install it for you behind the scenes, right? We have a package, and we install a bunch of tools, they're all based on NPM, so when you went to do local things, it would run the install tools make target, install those tools. Well.
This is not an NPM package, and it's not necessarily cross-platform. It's based on Rust, so depending on which platform you're on, you know, and how you install, so, like, I'm not really interested in creating cross-platform tooling to install this locally.
I think that's just, you know…
**Donal O'Sullivan** 24:09 Yeah. It'd not be straightforward to do in a make… in the makefile to do that, though, no?
**Pierre Tessier** 24:14 I think we'd almost have to write a bashed script.
**Donal O'Sullivan** 24:17 Backyard.
**Pierre Tessier** 24:18 Environment, and then run the right command.
And prompt you to actually approve running that command.
**Donal O'Sullivan** 24:23 Yeah, yeah.
**Pierre Tessier** 24:24 It feels ugly.
**Donal O'Sullivan** 24:25 Yeah.
Yeah.
**Pierre Tessier** 24:28 So…
**Donal O'Sullivan** 24:28 So the only thing is, you might run a local tool at Make, and then that might not… that might break, and you'd have to do this manually, and then go back and run it.
**Pierre Tessier** 24:36 You'll get an error message that Lee T doesn't exist.
**Donal O'Sullivan** 24:40 Yeah, yeah.
**Pierre Tessier** 24:41 Or can't find it, whatever it is.
Lithium?
**Shenoy Pratik Gurudatt** 24:44 is a Docker container, I don't know if you want to use that in the make. That would be weird, though. Pull in everything, and then… Finally, doctor.
**Pierre Tessier** 24:54 We could, if somebody wants to follow up a PR with that, I guess, maybe?
Because if it has a Docker container, and you could get it to mount the local volume.
I think it probably works, you could do it as a single command.
to run and check.
**Shenoy Pratik Gurudatt** 25:13 If we see people complaining, maybe we can do that.
**Pierre Tessier** 25:17 Okay. Pretty good odds.
**Donal O'Sullivan** 25:21 I might have some bandwidth to have a look at that. Could do it, maybe.
**Pierre Tessier** 25:26 I was just hoping to get this merged, so we could.
**Donal O'Sullivan** 25:29 Yeah, yeah, yeah, yeah, not sure, I'm not a blocker. I was just wondering.
**Juliano Costa | Datadog** 25:36 I hit merge on everything here, let's see how it goes.
**Pierre Tessier** 25:41 As long as it merges lychee first, it should be okay.
**Juliano Costa | Datadog** 25:47 I added to the queue, I don't know who'll get first.
**Pierre Tessier** 25:50 There is a way to look at the queue. I noticed.
**Juliano Costa | Datadog** 25:53 Okay.
**Pierre Tessier** 25:54 If you click on Merge Queue itself, it'll tell you who's next.
So, the… the fork one is… the repository fork one is first. That'll probably fail. Then Lee Chi is second.
**Juliano Costa | Datadog** 26:08 Okay.
**Pierre Tessier** 26:10 That's okay. We will… we will… I will happily hit the button a few more times today, okay? Cool. And to reduce the number of poll requests we have outstanding.
I want to mention as well, one more thing. I know there's a PR out there to re-bring back in trace testing.
We took it out a while ago.
And I've told Juliano this, Juliano knows about this. At Resolve, I get a bunch of Claude tokens, and I've used them. I wrote a test harness, or I had Claude write a test harness in Python. It's, like, 300 and something lines of code, it's not big at all, it's… good. It's got a few more things I gotta modify for it.
It follows configs similar to existing trace testing, so still a bunch of YAMLs defined on your configs. It does not support GRPC, though, that's the one big catcher there. So, if we wanted to test something like the Git Currency service, we have to do that through the front end.
And then go check the trace. It uses the Jaeger API to check to see if the trace exists.
It's very fast, and it runs 5 simultaneous tests at a time.
Because typically, you issue a request, and you gotta wait up to about 30 seconds for the data to show up in Jager. Instead of doing one at a time, it's fast to do 5 at a time.
Actually, it does more. We can specify how many we want to support, so it works pretty well. I plan on getting this thing merged. I was hoping I actually had it merged before this meeting, but I'll get it merged here later on this week, or at least a PR written for it later on this week, and the idea here is we could completely delete trace testing when we're done.
I just rely on this.
It'll also make Dependabot PRs much easier to merge.
You know, we could even get down to the point where we just may even write automated rules, so dependent bot PRs are automatically merged.
**Juliano Costa | Datadog** 28:04 Yeah, if we can… confidently say that it's working, I'm all in for it.
**Pierre Tessier** 28:12 Yeah, yeah, yeah. I think that's a great goal to aim for, is for… it detects which services have changed.
Or actually, it just… it reruns the full trace testing suite each time, and if it passes, then it goes ahead and you can auto-merge it.
We can discuss what that looks like, but that would be the idea, because it is annoying to wake up and, you know, buy more Dependabots.
Every day?
So I just want to make that, you know, I'm working on it, and I should have one Give me a couple… give me another day, and it'll be there.
**Juliano Costa | Datadog** 28:52 Talking about things that you are doing, Pierre, I… I know that we have just 2 minutes, and maybe that's not enough, but I want to talk about the Docker Compose thing.
**Pierre Tessier** 29:03 Fuck yes.
**Juliano Costa | Datadog** 29:03 I'm sorry. So… so you… you send a PR.
**Pierre Tessier** 29:09 And…
**Juliano Costa | Datadog** 29:10 I don't like it.
**Pierre Tessier** 29:12 It's, it's…
**Juliano Costa | Datadog** 29:14 Hoping to discuss.
**Pierre Tessier** 29:16 Yeah, so profiles don't solve it.
Because… overwrite a service. If everything had its own service name.
across the different modes, it'd be fine, and you could use profiles, but profiles are to turn things on or off. They're not made to merge Or override settings across services.
And then… and I think you ran into that one as well, like, to do some of that, you still had to specify a dash F to do the few additional overrides.
So, no matter what we do, we're gonna need to layer with "-f. So, my sense was, let's properly layer everything. Today, we don't layer at all. Today, we just have isolated "-F views, but if we layer, then it would be more cascading, like.
CSS, I guess.
But yeah, that's why. And it's because profiles just don't support merging.
Settings within a service is the issue.
**Juliano Costa | Datadog** 30:17 Hmm.
**Pierre Tessier** 30:18 Also, I think something about when you use profiles, they're not applied, predictably.
So, like, if… like, the list of pro… if you have more than one profile you're passing in.
It will try to start them not in order.
Or not in a predictable order. Now, you could use service, like, dependencies to keep that in check, but yeah.
**Juliano Costa | Datadog** 30:50 Okay.
**Pierre Tessier** 30:51 So…
**Juliano Costa | Datadog** 30:53 Okay. Yeah, I don't know if you saw the PR from, jeez, where is it?
from Colonel.
Colonel.
**Pierre Tessier** 31:07 31… 3107, yeah.
That one still uses Dash F to do some overrides. That's why, right?
**Juliano Costa | Datadog** 31:14 Yeah, exactly. But the only "-F that he has is, this compose fool that uses this whatever… Greater than, greater than, or smaller than, smaller than what.
**Pierre Tessier** 31:27 Yeah, yeah, yeah, it uses… it's smaller, it's more minified.
**Juliano Costa | Datadog** 31:32 abuse.
**Pierre Tessier** 31:32 Thank you.
**Juliano Costa | Datadog** 31:33 Yeah.
**Pierre Tessier** 31:33 I'm, he uses, YAML anchors, whatever.
I… Sure.
**Juliano Costa | Datadog** 31:42 I also don't know, like, I understand your approach, I understand…
**Pierre Tessier** 31:48 I want to be clear, though, he has not split off the observability stack in that PR. We would still have to split the observability stack, so there will be two more composed files.
We split the observability stock.
Because Kafka metrics are only picked up when you go Kafka metrics are only picked up when you're in full mode, I guess. And then if vendors want to do overrides.
Oh, sorry.
**Juliano Costa | Datadog** 32:15 God.
Yeah.
**Cyrille Le Clerc** 32:18 For a year.
**Pierre Tessier** 32:18 That's why I did the way I did, right? Like, so I went back to the original issue, and I was like, what are we trying to solve for? How can we solve for all that? And that's what I… that's why I wrote the PR the way I did it.
**Juliano Costa | Datadog** 32:29 Yeah, I honestly don't like the four collector configs.
**Pierre Tessier** 32:34 I know.
**Juliano Costa | Datadog** 32:35 But I don't think we have another way to solve… that's the problem.
**Pierre Tessier** 32:39 Yeah, Collector, you know, it's a merge. It's command line merge.
unconfig, and it's how they're passed in.
**Juliano Costa | Datadog** 32:45 Yeah.
Because my main concern here is how another vendor would… add their thing. So they would need to come, add an extra Compose file, add an extra.
**Pierre Tessier** 33:00 No, no, no, no, no, they just… no, they don't add anything extra. They just modify the… the vendor's… the vendor, Collector config, that's it. It's the only file they modify.
**Juliano Costa | Datadog** 33:13 The extra ones, right?
**Pierre Tessier** 33:15 Yeah, they just do that, and that's it. They don't touch anything else. Because it's always included, every time, we always include the vendor.
**Juliano Costa | Datadog** 33:23 Okay.
Yeah. Yeah.
**Pierre Tessier** 33:26 That was, that was the attack.
**Juliano Costa | Datadog** 33:27 Look at that one.
Okay.
Okay, I'll take a look with.
**Pierre Tessier** 33:35 I know Joe.
**Juliano Costa | Datadog** 33:35 I'm saying.
**Pierre Tessier** 33:36 here.
**Juliano Costa | Datadog** 33:36 Car off.
**Pierre Tessier** 33:37 four configuration files, so I'm like, I know, I don't disagree with you, but I think if you use profiles, you're gonna end up with four anyways.
**Juliano Costa | Datadog** 33:44 Yeah.
But I'm happy that we are renaming docker-compose to Compose, so, yeah.
**Pierre Tessier** 33:50 Yeah, yeah, yeah, I, I, hey, you gotta give it the times, man!
**Juliano Costa | Datadog** 33:56 Okay.
Take a look, and…
**Pierre Tessier** 34:00 And we can figure it out, how to approach it right.
**Juliano Costa | Datadog** 34:04 And I think whenever we have that done, we should think about, shipping a release.
**Pierre Tessier** 34:11 Yes.
Yes, I'm ready.
Take a look at it this week, let's make an agenda item next week for when are we going to ship the next release.
**Juliano Costa | Datadog** 34:22 Okay.
**Pierre Tessier** 34:23 Okay.
**Juliano Costa | Datadog** 34:24 Okay.
**Pierre Tessier** 34:25 Awesome.
Thanks, gentlemen.
**Shenoy Pratik Gurudatt** 34:29 Excellent.
**Donal O'Sullivan** 34:31 You guys…
