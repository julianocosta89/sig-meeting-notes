SIG: Community Demo App SIG
Date: 2026-02-25
Duration: 34 minutes
Zoom Recording URL: https://zoom.us/rec/share/mxHxE0jDkY49FAEWtEEPfQpVXC2MfTxouP8V36IjCWBMGyO-zX6fYDOASmIwgM3m.HjgIYACcX0yxZeZS
============================================================

## Zoom Recording Transcript

**Juliano Costa | Datadog** 00:44 Hello there.
**Donal O'Sullivan** 00:48 Hello.
**Juliano Costa | Datadog** 00:50 Hey, Donald, I saw your message, and I also saw your PR.
I just didn't have time to take a look at it, so…
**Donal O'Sullivan** 00:59 No worries, no worries, Ed. I'm new here. Nice to meet you, Juliano.
**Juliano Costa | Datadog** 01:05 Yeah, thanks for… for sending the tiara, actually, and the fix is… is awesome. Yeah, I… I want to test it out, but yeah, as I said, I just didn't have the time.
**Donal O'Sullivan** 01:21 No worries. Yeah, no, it's nice, because it's… when I run the demo now locally, like, in Kubernetes, it just… it actually doesn't even run, it just crashes, and it's basically, yeah, flag the UI as just, like, 2.3 gigs, and it's just… once you… once you do this fix, it just goes down… it goes down to, like, 2.30 or so, so… 230 megabytes or something like that, so, simple fix, Nice one to get done, I think, so…
**Juliano Costa | Datadog** 01:48 Cool. Yeah, we had, when… when the PR was opened to introduce the FLACD service, the FlexDUI service, I remember discussing with the alter, I think… I don't remember his name, no.
But the guy that introduced the, like, the UI, and I also discussed with Tristan, because we saw some increase, increase on the memory consumption, and I discussed with Tristan to see if there was any… feature flags, or environment variables, as we have for Java, with the… dash XMX, to control, like, the JVM memory, and also the Go, there is a GoMemlin.
**Donal O'Sullivan** 02:40 Yeah, yeah, yeah. Also limits the memory, because.
**Juliano Costa | Datadog** 02:43 For some reason, they are in a container, but they do not respect the container limits.
**Donal O'Sullivan** 02:48 Yeah, yeah, yeah. I think it's… I think there's a difference between how Docker interprets the memory limits versus Kubernetes. I think Docker might, like, give some leeway, and Kubernetes is, like, a hard no.
On the limits, I believe, could be wrong there, but, That actually leads me on to another question. So I noticed when running the demo locally.
The Java services do… I… so I haven't set any environment variables. The Java services do… have memory pressure issues, so I have opened an issue about it, But is that because… so is there an environment… as you say, there's an environment variable that has to be set for the JVM, is it?
**Juliano Costa | Datadog** 03:38 Well, actually, Java shouldn't be… shouldn't have any issue. I think the environment where we set…
**Donal O'Sullivan** 03:47 Okay, I gotcha.
**Juliano Costa | Datadog** 03:48 One thing that we have is a feature flag that, makes the… the memory consumption have a spike, and then it also, like, I think we have something related… another feature flag related to garbage collection.
But those are controlled via feature flags, and if they're disabled, then the application should run smoothly.
**Donal O'Sullivan** 04:15 Yeah.
No, I'm just finding the, like, the latest version of main when I run it locally.
In kind, like, the ad service, the fraud detection service.
Are constantly crashing, they're getting out of memory kills, and then… Kafka, every so often, will restart as well. And I actually… I took off, I just got rid of the memory limits altogether, and… They kind of… they… they run above their memory limit, so, like, 300 and something, and… for ad, I can't remember. I think it's in… I opened an issue about it, but I don't know, is this something that you guys are experiencing?
It's just that I just… was just running it locally, and I was like, oh, that's annoying, it's just… it's just not working. Like, I don't think I had any… I had to change anything, I literally just pulled main and then just ran it.
If that makes sense.
I can share the issue in the chat if… sorry, I don't want to overtake the conversation here either, but I did link it, the… Yeah.
The vocal code work.
Yeah.
**Juliano Costa | Datadog** 05:30 3034. Yeah, okay, I saw that you also added it to the… to the meeting notes, so that… that should do.
Cool.
**Donal O'Sullivan** 05:43 So I guess, yeah, it's probably the Helm chart. Anyway, look, anyway. Cool.
**Juliano Costa | Datadog** 05:49 Well, yeah, I think we need to… tried out? The, the… the…
**Donal O'Sullivan** 06:02 Why, sir.
**Juliano Costa | Datadog** 06:02 Like, the behavior on Docker and, Kubernetes From there.
on the service itself shouldn't be different, like, on memory consumption and stuff, but we know that, yeah, works on my machine doesn't…
**Donal O'Sullivan** 06:20 Yeah, yeah. Always who works. Yeah, yeah, yeah.
**Juliano Costa | Datadog** 06:25 So, yeah, we would need to take a look.
**Donal O'Sullivan** 06:29 No worries.
**Juliano Costa | Datadog** 06:29 But I think you already created the issue, so…
**Donal O'Sullivan** 06:33 This already helps a lot.
Cool.
**Juliano Costa | Datadog** 06:36 Just so I add properly here on the meeting notes, you are from Elastic, right?
**Donal O'Sullivan** 06:42 Yeah, correct, yeah.
**Juliano Costa | Datadog** 06:42 Okay, cool.
**Donal O'Sullivan** 06:43 Yep.
**Juliano Costa | Datadog** 06:49 Hello, hello!
**Cyrille Le Clerc** 06:51 Hello, long time no see!
**Shenoy Pratik Gurudatt** 06:53 Yeah.
**Juliano Costa | Datadog** 06:53 On time of sea, indeed. How are you doing?
**Cyrille Le Clerc** 06:56 Fine, fine.
Holiday's next week, so that will be nice.
Oh.
**Juliano Costa | Datadog** 07:05 Cool.
So… We have, like, a huge topic that we need to discuss. I think… half an hour is not enough to discuss, to be fair, and I feel that most of the folks that are Pushing the things that are… Changing the way that the demo is deployed today are not on the call.
Yeah. So… Yeah, so let's try to discuss and see what, But we think about it, and, maybe… Put an update on… on the… on the issue, and… and… And see how that develops.
So… just to give… I don't know if… I think everyone is aware of the ongoing issue, maybe don't know not, or are you also aware?
I don't know if Roger or Damien synced with you about.
**Donal O'Sullivan** 08:06 Yeah, yeah, I'm aware of the issue, yeah, I'm aware of Damien's suggestion as well, so I'm not 100% up to date with it, but I have an idea of it.
**Juliano Costa | Datadog** 08:17 Cool.
So during Old Town Unplugged, one of the discussions that we had in the room was… how we can make the demo lighter, a lighter version of the demo. Today, there is the Docker Minimo, but is it still big, because… Well, I would say that Logen and OpenSearch are the biggest services. Both of them are consuming more than 1 giga each. In the minimal, we drop Kafka, fraud detection, and accounting, so we do not have Kafka, which is great.
But we still have the low jam and, and OpenSearch.
So they were… The discussion started, and then everyone was like, hey, what if we drop… the observability stack, and keep the demo as just a demo. And I was like, yeah, but what about the users that want to start the demo and see something?
And then one of the suggestions were, but for those users, we can provide an opinionated version, and then my counter-answer was, and isn't that what we are actually doing now? So… Then we kind of… got back in… running behind our own tail, and I think we didn't come up with any conclusion. That's… that's why I brought everything into the… into the issue.
Damien brought the idea of… what he called ODB, which is the OpenTelemetry Demo Builder.
I'm not sure how much I like this idea. It is interesting.
but I'm not sure how much I like, mainly because… I, I feel that… OCB is, like, too much, and people… most of the folks do not use, and then we are introducing another tool that people will not use as well. So I would like to have an easier experience to everyone.
Another suggestion on the… on the discussion was bringing having a Dockerfile that doesn't have the… any vendor stack, or any observability stack, and then all the vendors would have their Dockerfile… Rafana, Dockerfile Elastic, Dockerfile OpenSearch, Dockerfile, Datadog, and so on. And… what I don't like about this is that when someone… so, like, if we keep… if we keep that into the vendor's REPL, I'm good with it.
But if we keep that on the Devos repo, then… I see this as a problem, because… if the user tries to run, let's say, I don't know, whatever vendor, like Coral Logix, And… it doesn't work. I don't know anyone from Corelogix. I just accepted the file.
And if they don't reply, I have an issue on our record, and, like, yeah, sorry, I can't help. And the maintainability of the thing becomes, like, hell, because we have 42 different vendors. We would have 42 different Docker files, yeah. So… But I think I kind of, spit it out, so I want to hear. Yeah, I said too much, sorry.
Go ahead, Sue.
**Cyrille Le Clerc** 12:12 Yeah, as I tried to say in the GitHub issue, I would see value in clarifying what are our key goals, and maybe get consensus.
Is it just to reduce the memory consumption, which Donnell has discussed some challenges today.
Is it about the… observability backends that are included today, that they create problems, and so I work for Graphana, I understand that some people bring this point.
do we want to really, stop having, an OSS distro, some… yeah, a distro with OSS backends that we can use? There are many benefits to this for practitioners who want to test, but also internally to us as hotel demo maintainers to test.
I can share with Juliano a screenshot of Jaeger, and we understand what we mean.
It's a lingua franca. If we don't have it, how do we work?
they are… if we reach out to a project like, Henshart's, team, this is the lingua franca we have.
Do we talk about Docker Compose, or do we talk about Kubernetes? Because I felt that with the Kubernetes deployment, it's extremely easy to Disable the batteries included.
Yeah, we, I… Feel it could be interesting to… Get content to get people prioritized on… Express their voice on what matters to them.
And then probably tell them, yeah, okay, but we need some help. Okay, you ask for something, how much can you… how much are you willing to help? Because, if you have some… for something that is very hard, or, but you are not ready to help.
It's like the chicken on the pigs.
In the agile metaphor, I felt.
I don't know if it resonates.
**Juliano Costa | Datadog** 14:21 So, one thing that I shared with the group during Auto Unplugged was that when we were discussing what tools we would include in the demo.
we all agreed that Grafana was the open source approach to do, like, there was no other open source tool, and Grafana was the most used one in the open source space.
But today, I think the project is 2 years, 2 years and a half. I think… Grafana started bugging the competitors, and then, like, yeah.
**Cyrille Le Clerc** 14:58 Change, yeah, governance position change, maybe there is process.
**Juliano Costa | Datadog** 15:03 Yeah, of course.
**Cyrille Le Clerc** 15:04 questioning.
**Juliano Costa | Datadog** 15:05 Yeah, exactly. So I see… I don't see it as a problem, because I'm pretty sure the stack from Rafana is not Rafana with OpenSearch and Jaeger. Most probably you guys push for LGTM.
So… Like… the hotel demo experience is not the same experience that a Grafunnel user would have using the Grafana stack, and the same for OpenSearch stack and all the other vendors, so… I'm a huge fan of Jaeger, I wouldn't remove it. I don't think Jaeger is a problem, but we also have metrics and logs, so we need to… Yeah.
Yeah, I don't know, I don't know. I'm in the middle of this, like, people are shooting from roadsides, and I'm, like, in the middle, and I don't know what to do.
**Shenoy Pratik Gurudatt** 16:04 I'd like to add something to what Cyril mentioned, like.
We… we talked… we had this big discussion around batteries included versus not.
And you brought up a good point, that Grafana itself, when a user comes to Grafana style, they don't use it the same way as we have it in our demo.
And there was a lot of talk between vendor agnosticity coming from the hotel world.
What I like about the demo today is it is vendor agnostic, because you can have mix and match of your vendors.
And then create the stack.
Whereas, if we go into the silos for it, everyone will have their own Docker components with their own stack elements.
That is, like, semi-vendor locket situation, I feel, where if I'm using, open searches, for example, stack, I would just use all of the open search elements.
I'm using Grafana stack, I introduce all of the Grafana elements. It defies some of the purpose that we have in the OTL tenets itself.
So, that's where I collect the… current way that we have. We have a mix and match, and… users who are new to the hotel understand this is part of the vendor agnosticity. You can bring your own stuff for your own storage visualization, and then make it work.
**Cyrille Le Clerc** 17:31 And to add to what you said, Chenoy, Yeah, or maybe OpenChurch can be the umbrella to take them all, because it's ENTF and so on, but as Juliano said, Jaeger is Jaeger. We expect Jaeger, I think. I think somewhat, we also expect Prometus, and I am a bit biased, but And I think if the hotel demo ends up with a batteries-included version that, let's say, consolidates everything on OpenSearch.
then typically us, Grafana Labs, we will create our distro, that will not be Jaeger, that will not be… but that will be LGTM, all our stack.
And it's likely to be very popular.
Because Jaeger, sometimes Tempo has some parity perception, or is getting closer in terms of perception to Jaeger.
on… on then the hotel demo, community would not govern What is likely to be a very, very popular distro of the demo.
And I'm not sure it's, it would be good for the, the hotel demo and the hotel community.
**Shenoy Pratik Gurudatt** 18:38 Good, yeah, I do agree that one stack is not the right way.
Yeah, I would go.
Also, point towards the battery included as a good option, with different stacks. Doesn't make sense to have, like, a CIOS thing.
**Juliano Costa | Datadog** 18:58 There is another, proposal from Roger, Roger Cole.
Also, at the moment, Taylor, the link is on the… on the README, but I can't… on the README… on the Seek Meeting notes.
But I can share my screen real quick, as soon as I find… Which one I need to… to share? Yep, there you go.
So, his proposal is about decoupling the telemetry services from the main Docker Compose.
And then we would have some extra… Compose files.
And what is… Nice about this approach is that everything is controlled With the .env file.
So, in the .env file, you specify all the… Oh, the… Is it… is it in here?
da-da-da-da.
Okay, yeah, so here we have, like, different collector configs… Oh, and then we have different Docker Compose… Jesus. Yeah, so… in the make file, what it says is that, hey, use the Docker Compose file, also the telemetry, open search, Docker Compose file, and the Grafana Docker Compose file. So, this is… this is interesting, but at the same time, it brings the… the first thing that I… that I brought up about maintainability, because imagine we having… everything under this telemetry folder, and we having to kind of answer users whenever vendor XYZ dockerfile doesn't work.
For some reason, because we are on the bleeding edge of OTEL. I think that's the goal of the project, like, keeping up to date to the SDKs, APIs, and semantic conventions, so things break.
Because, yeah, that's what we do. And… When the integration with another vendor breaks, then we cannot guarantee And, yeah. So… Again, I think we are back to square… 1 or 0? I don't know how… how… how do I count here? I'm not a baseball guy.
But, from… Yeah, the Docker Compose profiles is… It's nice, because we can… we could have… the same way that we have Docker Compose and Docker Compose Minimo.
We can set up profiles within the file, and then we just say, docker-compose dash dash profile.
**Cyrille Le Clerc** 22:13 No.
**Juliano Costa | Datadog** 22:14 full start, and it will start all the services. And if we want the minimal, we just set the minimal, but the Docker compose file is one… one single file, so we do not need to manage multiple files, have… like, the… the minimal was broken because we introduced Postgres, but we forgot to add to the minimal, so, like.
All those things that are, like, painful and manual.
Would go away with the profiles.
But on the other hand, Cindy, if we do profiles, We would have… Well, actually, we could have a profile with the… the backend.
And then, if we do not pass this profile, Then it wouldn't start.
**Cyrille Le Clerc** 23:07 Yep.
**Juliano Costa | Datadog** 23:08 the back end.
They didn't fall?
**Cyrille Le Clerc** 23:11 And we can switch the default value of the profile, maybe for the moment for Parity, we said the default profile is batteries included on, Maybe later we say, no, the default profile becomes a no-only backend.
That looked compelling to me.
**Shenoy Pratik Gurudatt** 23:34 Yeah, even, from… fork maintainer. I've maintained the open source fork. It's very difficult for me when the Docker Compose updates. I need to change everything, and Kubernetes is the altogether next thing. We are not even up to date to manage the, Helm charts and other pieces.
profiles and adding, switching few components with profiles, it's easier for me to extend as well.
for what is there as profiles in the default hotel demo. I can add my own profiles and then change it to what.
We want, in the fork.
**Juliano Costa | Datadog** 24:11 Well, I like that very much.
So, should we… should we bring the… I'll adhere… To the notes that, files.
**Cyrille Le Clerc** 24:40 Yeah, generally, if you had an OTLP endpoint, it would make our life easier, I think.
**Shenoy Pratik Gurudatt** 24:46 Yeah, I'm… I'm pushing a lot internally.
those are different, talks, I would say, but yes, yeah, I'm thinking of… like, I'm… I'm in, talks with our internal ingestion team.
I can give you some open search background, like, as well. We are pushing more towards, adding more, like, contributors to the OTL open search exporter, as well as, the hotel demo, because, there was one issue that Juliano raised, in the collector content for OpenSearch Exporter.
I believe that was around the default config setup. It's going for a toss. We merged that PR in, hitting the next… Collector wheels will have it.
What do you have?
**Cyrille Le Clerc** 25:38 I think that the hotel collector monitoring, meta monitoring only supports OTLP.
When you configure your hotel collector to export its own telemetry, which is critical for trouble treating.
You can export as Primitus metrics, and I think the other… the only other one is OTLP, and so what we have to do in the OTL demo ease… we send… the internal telemetry, internal logs of the hotel collector, we resend them in the hotel collector.
So that we can send them to OpenSearch.
**Shenoy Pratik Gurudatt** 26:12 I see.
Okay.
**Cyrille Le Clerc** 26:13 So please… Which is a complete anti-pattern. Please convince your team.
To expose them.
**Shenoy Pratik Gurudatt** 26:20 We used to do something similar for the hotel collector matrix itself, right?
**Cyrille Le Clerc** 26:24 I think we…
**Shenoy Pratik Gurudatt** 26:25 W.
**Cyrille Le Clerc** 26:25 Or, I already pushed to stop because it's,
**Shenoy Pratik Gurudatt** 26:28 Yeah, it's very bad. You should not… Yeah, I couldn't understand the config first, and I remember the metrics, but I'll… I'll double down on this with the team. I'll take a look.
**Cyrille Le Clerc** 26:44 No, there's Monster Help us, yeah.
**Juliano Costa | Datadog** 26:47 Well, I think I can't say anything here in this… on this matter, at least not for now.
**Cyrille Le Clerc** 26:55 have an OTLP endpoint in Datadog?
**Juliano Costa | Datadog** 26:57 We do have, yes, but yeah, it's completely different. Well, yeah, let's not talk about that. So I added here as, a to-do for myself to bring that back. Jesus, I just messed up everything. To bring that back to the… To the doc… to the… a GitHub issue?
And kind of revive the discussion. Not revive, I think, like, the discussion is very active.
And, yeah, maybe we can take a look from there. Two things that I would love to have insights from, I know that we are talking about reducing the demo.
But there is an open PR, from Martin Twitz, that adds Weaver.
And I think it's, a nice service to have in the demo. I'm a huge fan of Weaver.
But it also brings an extra service, because we are, generating, generating docs with Weaver, and then we run the docs together with the demo, so it would be an extra service. I tried to… I played around with his PR and changed a couple of stuff, so we just have NGINX, with static files, so it's really minimal, but it is still an extra service, so that would add an extra service to the demo, and yeah, I don't know what are the opinions of the others.
So, if, you guys could take a look, that would, help.
And we have a couple of open PRs, so Donald shared, one that, is improving, like, the UI. So, I really need some help reviewing them. Yeah, so any help would be… Helpful.
**Shenoy Pratik Gurudatt** 29:03 I'll take a look at the Flag D1. I took a look briefly. That is a good improvement in the randomly crash memory. Yeah.
**Juliano Costa | Datadog** 29:13 Yeah.
**Shenoy Pratik Gurudatt** 29:13 I had a very untimely PR on the… LLM edition. I don't think so that's needed, it's just good to have. There are current, mocks, mock service… Is using some pre-generated telescope reviews, adding an actual LLM to it.
To… and using GenAI SDK, or at least, mimicking the GenAI SDK with some attributes, so that it follows the GenAI functions.
**Juliano Costa | Datadog** 29:46 This is one thing that I didn't understand, because we have a mock-up NLM service that returns the replies, but we also have the option to, if you replace the environment variables on the .env and put the OpenAI key.
it actually calls, OpenAI. And this service that it calls OpenAI is already instrumented with, Python auto-instrumentation, and it generates GenAI, semantic conventions.
The problem is that Python with OpenAI is not on the latest gen AI semantics, but Rudimila is working on the PR to have that, so whenever that… I'm following the PR, whenever the Python PR gets merged, then we can push the feature flag… the environment flag.
On the demo, so we use the latest GenAI, so the tools that ingest the data work.
Well, go ahead, Sir.
**Cyrille Le Clerc** 30:48 Yeah, sorry, on, Weaver.
I'm super excited by the idea to have schema-driven custom metrics and attributes.
I think Donald, coming from Elastic with ECS, you would not say no. Julia, no, you also have a schema at Datadog that customer can extend, so I guess you will also line. On Chenoy, with your Elastic DNA, I guess, so I guess we… We… yeah, we will, all be interested in this, concept. Now, I was surprised that it was about publishing a website with docs.
**Juliano Costa | Datadog** 31:28 The what? Sorry?
**Cyrille Le Clerc** 31:29 that the PR was about publishing a documentation site.
**Juliano Costa | Datadog** 31:33 For me, which would…
**Cyrille Le Clerc** 31:34 What really resonate is to have this shared schema.
in the repo, and to generate in Java.NET, C++, whatever.
**Juliano Costa | Datadog** 31:43 That was my first pushback on Martin's PR, and he was like, hey, but we can start here, and then do the other things, because we can also add… I also want to add the live check.
So we validate the metrics that are coming, like, the new stuff that we are producing.
**Cyrille Le Clerc** 32:01 Maybe these are.
**Juliano Costa | Datadog** 32:02 profile.
**Cyrille Le Clerc** 32:02 That helps us.
**Juliano Costa | Datadog** 32:04 Yup.
I need to drop, but I didn't have the chance to say hi to Antona. Hi, welcome to the… to the demo.
Were you here just to hear us.
**antoninbruneau** 32:21 arguing, or… No, so, I'm part of Tuga. Probably never heard of us yet. We're just a new player in the game, but we are… Using a lot the demo environment as our demonstration platform.
So, we have a couple of PR in preparation, that we'll submit soon.
Maybe also wanted to check, we have, like, a cow's monkey, thing running on our demo environment to randomly trigger the feature flags.
To generate errors. It's more like to see how the platform responds to random errors.
But, but we'll be very, happy to contribute, to the student environment in any way in the, in the future. So I just wanted to say hi, And also see if we can contribute in any way.
**Juliano Costa | Datadog** 33:31 Yeah, definitely. We are always looking for contributors, and yeah, I'm already excited about the things that you… you promised, so I'll ping you. If I don't see you back, I'll ping you.
**antoninbruneau** 33:47 But I'll test it on our own environment, and then we'll push it to you.
To the official repo.
**Juliano Costa | Datadog** 33:55 Cool.
Thanks, everyone. Yeah, see you all in the next one. Yeah.
**Cyrille Le Clerc** 34:03 It was great meeting.
**Donal O'Sullivan** 34:06 Bye, nice meeting you.
