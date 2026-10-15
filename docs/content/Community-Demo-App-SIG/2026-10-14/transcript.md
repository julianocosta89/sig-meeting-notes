SIG: Community Demo App SIG
Date: 2026-10-14
Duration: 30 minutes
============================================================

## Zoom Recording Transcript

**Felix Felix (IBM India Pvt Ltd)** 02:11 Hello.
**Maxime Quentin** 02:18 Hello?
**Felix Felix (IBM India Pvt Ltd)** 02:20 Hey.
Am I… am I audible?
**Maxime Quentin** 02:25 Doric?
**Felix Felix (IBM India Pvt Ltd)** 02:26 Am I… am I… am I audible? Can you hear me?
**Maxime Quentin** 02:29 Oh yeah, yeah, for sure.
**Juliano Costa | Datadog** 02:33 Hey Maxime.
**Maxime Quentin** 02:34 Right.
**Juliano Costa | Datadog** 02:39 Let's just give a minute to see if everyone else… Or anyone else would join.
Oh.
Cool.
Huh. Great, we have Donald here.
**Donal O'Sullivan** 03:35 Hey guys, how are you? Sorry I'm late.
**Juliano Costa | Datadog** 03:39 Cool, cool, cool. Nice.
So… Hello everyone, we have… A special guest here today.
Maxime is from the browser SIG.
And we were discussing internally, so he's also at Datadog, and we were discussing internally to… about adding the browser SDK into the front end.
I think it's a good idea.
But I think that will change a couple of stuff, so, I asked him to join the SIG meeting and talk us through what would change and what we need to consider before, like.
Giving the… the green light to it.
Maxime, the the stage is yours. Feel free to.
**Maxime Quentin** 04:39 No problem.
**Juliano Costa | Datadog** 04:40 Yeah.
**Maxime Quentin** 04:41 So, I'm really not familiar with the demo and the way it's implemented, but what I've checked, it's like, it is still using the Node.js SDK for the front-end JavaScript instrumentation.
Given that we made some good progress in the browser SIG, I think it could be very valuable to migrate the Node.js instrumentations to the browser SDK.
And.
the one big question, as I'm not super, aware of the connectors in the demos, some of the Java, Node.js instrumentation, like, I don't know, for instance, the documentation, instrumentation… the document instrumentation that Kind of showcase when you navigate to a new page.
Has been deprecated toward a navigation timing, instrumentation.
And this is just one example of stuff that has changed since Node.js.
And so, if I wanted to kind of contribute in the Dibo and update the… And.
like, update the SDK for the front end, how could I… Kind of measures the impact on the collectors.
who could, kind of help me a bit on updating connectors if I need to, change some kind of, Like… in the example of the document instrumentation, how should I improve that or migrate that too?
Yeah, so just my main question, But yeah, I don't really know how they're implemented and what they're doing, so… Cool. I'm here.
**Juliano Costa | Datadog** 06:27 So, the good thing is that, at least good for you, is that none of us is a front-end developer, so we work on the best fork here.
So, yeah, we got the front end kind of donated from some folks that were working on, Trace test.
Back when we started the demo?
So they did a whole React thing, and this new front end, and since then, they left. Well, the company doesn't exist anymore, so the person that was kind of helping us maintaining and all that stuff is gone. So we… we work on… Best effort and, best AI that can help us here.
I can share a couple of stuff with you that I know.
HNI.
So if you go to the open telemetry, Demo source front end.
And under utils, we have a couple of, things, and then, on the telemetry.
We have the front-end tracer, which is… The one I assume you would change?
**Maxime Quentin** 07:48 Yeah.
**Juliano Costa | Datadog** 07:49 And here is basically what you would need to update.
**Maxime Quentin** 07:55 So, From what I've understood, all of the instrumentation in the front end and the trace providers and everything are kind of loaded manually. With the browser SDK now, the approach is more like you load a bundle and you have a lot of stuff out of the box.
And I think all that, I've had a look, and I think it's… I would be able to be autonomous on that.
My question is more like, do you have, for instance, collectors in your backend service that kind of check this dedicated field and that could be broken because the field does not exist anymore because we migrated it to something else?
**Juliano Costa | Datadog** 08:39 We do have collectors, but I don't think you would have any problem here. The thing is that the demo is not running.
at least not ours. We do have some projects that have the demo deployed and up and running. I think Chenoy has one on OpenSearch. Jaeger has one, if you go to jaegertracing.io, you… You'll be able to navigate on the on the demo running, but ours is not.
So, we do have, as I said, we do have some configs here, but I don't think you should, actually care about this. I think that the main point that you should actually care, and we already, had that when we first implemented the front-end tracer, is that… The front-end traces, they do not go from the browser to… to the collector. They actually go from the browser to the front-end proxy, and from the front-end proxy to the collector, right? Because, when you are deploying on the… on a, let's say, AWS or on a cloud provider.
The browser that the user is accessing your application doesn't have access to the collector, so you need to send through a public endpoint.
So this is already here, so if you keep, this environment variable here, that we called Next Public.
Otel, exporter, Otlp, blah blah blah that That would already work.
**Maxime Quentin** 10:18 Okay.
**Juliano Costa | Datadog** 10:21 other thing… another point that you would need to worry, but I think just if the tests actually broke, if the tests actually break, is the test telemetry.
**Maxime Quentin** 10:34 Okay.
**Juliano Costa | Datadog** 10:34 And in here we have tests for traces, metrics, and logs.
So, currently, the front end Do we have it?
So, currently, the front end… has traces, metrics, and logs.
If you change something that.
Kind of removes one of that.
**Maxime Quentin** 11:03 This…
**Juliano Costa | Datadog** 11:04 will kind of crash the tests, but I don't think it would actually… No, sorry. So, you would actually change the front-end web, trace.
So in here, we have traces, metrics, but no logs. So if you add logs, I would just ask to update here, and then the test would test if the front-end web logs are actually arriving.
on open search, and that's it. So no Yeah, I I think the the contribution here would be easy.
**Maxime Quentin** 11:42 Okay, cool. And when you mean test, do you mean, like, integration tests, where you run locally your web, you run locally your collector, and then you… Kind of.
Like, make sure you… you receive in the collector the provided metrics and traces, or are the tests For the web and for the collector separated.
**Juliano Costa | Datadog** 12:08 We have a CI that Chenoy contributed that actually, Runs the whole demo?
And then, we… with the demo, we have a load generator, and the load generator also sends, playwright sessions. So it actually goes to the browser and navigates, so we also have run data.
And then the the tests validate. If traces are arriving in Jaeger, if logs are arriving in open search, and if metrics are arriving in So that should be automatically. Of course, you can run the test locally if you want. But if you can, if you don't want just you can. You can just open a Pr, and whenever someone someone approves it, the test will run, and we will know.
**Maxime Quentin** 13:02 Yeah, perfect.
Yeah, because one thing that could be complex during the demo locally is, like, a lot of instrumentation are plugged on the browser API.
For instance, like resources, the way we intercept fetches and everything. Sometimes you can have like cross-origin issues, like if you have your collector in a local port, whatever, and then your web on this other local host.
Which means having a CI would be very valuable for me to… Like, to see if I broke stuff, or…
**Juliano Costa | Datadog** 13:38 just.
**Maxime Quentin** 13:38 Thank you very much for the tour.
**Juliano Costa | Datadog** 13:41 Yeah, no worries. And if I come here to the collector itself.
I think… It's not this one, maybe here.
Where is the… do you guys remember where the… The course thing is configured.
So yeah, we have here on the on the hotel co-config. So this is the main one, the base one, and we do have course allowed from anywhere.
So, that shouldn't be a problem, because, as I said, we already have some, Rum data. It's primitive and basic, like, click, and, like, the event.
I guess whatever you guys did on the browser SIG is way more, sophisticated.
than what we have now. But if you need to… to change anything on the course, just, you… we can update here on this, hotel call config YAML.
**Maxime Quentin** 14:52 Okay.
No, perfect. Like, on my side, I still need to bring the point to the SIG, like, making sure everyone is, aware that I might work on it, and that everyone is aware that the browser is in good shape, so we can start demoing it.
But I don't think I will have blockers.
And in terms of HEA, I don't have a bandwidth like this week, and maybe I can start working on it next week if the SIG is okay with it.
So yeah, that's pretty much it on my side.
**Juliano Costa | Datadog** 15:28 Yeah, that looks cool. I'm excited to see that, actually.
**Maxime Quentin** 15:35 Yeah, you'll have a lot of new events, like all the Web Vitals, all the… like modern instrumentation we've introduced, it will be valuable, I think.
For a demo.
**Juliano Costa | Datadog** 15:47 Cool.
Cool. Now, you guys also have the… The… the page, right?
Yeah.
It's here. I don't know if you, everyone else, if you guys saw that.
**Maxime Quentin** 16:01 Oh, yeah, yeah, the sandbox, you mean?
**Juliano Costa | Datadog** 16:03 I.
**Maxime Quentin** 16:04 Yeah, yeah.
**Juliano Costa | Datadog** 16:06 I was aware of that, but I don't know if Felix Donal and Shenoy, they are aware of that. So the browser… SIG created this sandbox.
That you can actually, like, See the things that are being produced, but live.
Basically.
**Maxime Quentin** 16:27 Yeah, so also a very useful tool to QA our instrumentations because you can plug your OTLP URLs and make sure that payloads make sense and everything.
So yeah, like…
**Donal O'Sullivan** 16:46 Thanks.
**Maxime Quentin** 16:47 the.
**Shenoy Pratik** 16:48 Cool. Sorry.
**Donal O'Sullivan** 16:49 Is it… are you running a collector there? Is it WASM or something, or…
**Maxime Quentin** 16:53 No, so that's the thing, like, we don't have a collector on top of it. It's just, like, sending the raw instrumentation payloads to whatever URLs you're using, but, like, to make sure that you have the correlation between the spans and the resource.
Or making sure that, like, you introduce a new instrumentation, you want to make sure it catches the navigation, or it catches whatever browser thing that happened.
Yeah, it's our way to making sure we… our features are working.
Yep. Thank you for… What was the drawing, yes?
**Juliano Costa | Datadog** 17:36 No, thank you for the for the tour. Actually, yeah.
The demo is a place where we try to demo everything. This is actually a problem, that we… That we are, starting to face now. But I think this, for you, it… For this, you don't have competition, as of now.
Which brings me to the second topic that I want to discuss here. I don't have a link.
Give me just a second, I'll try to find… I sent to Donal, so I have a link there.
On our chat.
over to the… The docs… Too many tabs, sorry.
Oh, Lord!
There you go.
So… Just added to the agenda.
And now… share my screen. Well, I actually do not need to share the screen. What happens is that CDL is opening a PR.
to add, the compile time instrumentation to one of the services, from Go. So this changes a bit, it… It is a pretty cool project, because you do not need to like, do the manual steps and everything to configure the SDK.
He's not removing the… the Api instrumentation. So the the manual instrumentation so that Still, it is still part of the project, but he's… replacing the SDK, so he's removing the SDK and then adding this Hotel C compile time that adds the SDK and auto-instruments the code automatically. So, like.
The user doesn't need to actually configure the SDK and all the manual steps.
This is super cool.
The problem is that we have 2 goal services on the Demo.
The checkout service and the… product catalog.
Yeah, product catalog. So, checkout was showcasing how to manually configure the SDK, and product catalog was showcasing how to use the config file to configure the SDK.
We got, Alex Bolton, when he raised the PR to show the… to showcase the config file, he actually added the config file to check out and product catalog, and I asked him to… to kind of leave one service manually config… being manually configured, and one service with the… the config file.
And now in Go, we have a third way of doing it.
So, the thing is, if we replace checkout with the HLC, we will not have.
any demo of how to manually configure the SDK.
I asked around, and Robert Payak. I think you all know him. He's from the Go SIG.
He said that… he doesn't think it's a good idea to actually remove the manual SDK configuration, because the hotel conf actually lacks some features.
So, we have now 3 ways of doing the thing, just one is complete, and we… and in this PR, we are removing exactly this one.
So I want opinions.
**Shenoy Pratik** 21:52 From the GoSIG folks, what is their recommendation for a new person trying out Go instrumentation?
So what's their recommended thing? Is OTEL 3 even part of their recommended or like first two recommended steps?
**Juliano Costa | Datadog** 22:09 So that's the thing, it will depend on who you ask.
We have different Go instrumentation. We have different Go folks. We have the SDK Go folks. We have the OTel config.
Go, folks! And we have now, the compile… Hotel C. Folks. Now.
So, Hotel C, of course, will say that Hotel C is… Good?
**Shenoy Pratik** 22:41 Yep.
**Juliano Costa | Datadog** 22:43 I feel that the only one that is… actually feature complete, or has all the features, is the manual approach, like manually configuring the LTOC, the SDK.
And the others are trying to kind of, catch up.
**Donal O'Sullivan** 23:09 Yeah, I… I think, from what Robert said there, like.
Hotel comp is not stable, so… And, like, the demo is used by… People to see how to, like, set up instrumentation under apps, and… In a production sense, and… Also, like LLMs are obviously reading the demo and using that for training and giving people answers when they ask how to instrument an application, so Is it advisable to… I, I've obviously OTEL itself has been working towards stability, you know, If Hotel C is still kind of.
New… like, is this something we want to use?
That would just be my thinking of it, like, if Robert is saying as well, like, he's, he's a maintainer of the Go SDK, so I would value his opinion.
If we remove the manual configuration here, sorry, you mentioned earlier, does that mean we don't have any examples of manual configuration anymore?
**Juliano Costa | Datadog** 24:20 Yeah, we could think about removing… We could think about removing hotels, the config file, the hotel conf.
from Go, and maybe add to a Java service, so we would still showcase how to use the config file to configure the SDK.
And then we would have product catalog showcasing manual SDK configuration and checkout.
showcasing Hotel C.
So then, that would be, like,
**Donal O'Sullivan** 24:59 Yeah.
**Juliano Costa | Datadog** 24:59 an easy win, so to say.
Because I do like the idea of using the demo to also test these things. When CDL opened the PR, he noticed that the SDK resource attributes weren't being populated.
He already opened the issue, the folks already fixed it, and now on version 1.2.0, it's already in. So, the demo is also great for maintainers, too.
Keep up the…
**Donal O'Sullivan** 25:30 True, yeah, yeah, yeah.
**Juliano Costa | Datadog** 25:31 things.
**Donal O'Sullivan** 25:33 Yeah, I remember, yeah. Yeah.
Yeah, yeah, that's a good point.
Yeah.
**Juliano Costa | Datadog** 25:39 Oh.
I, I don't.
**Shenoy Pratik** 25:40 I think we should keep the manual instrumentation for sure.
That is like the base to start with, right?
**Juliano Costa | Datadog** 25:49 Yeah, manual instrumentation is in, manual configuration, it would be dropped.
And to be honest, I don't know how many folks actually do the manual configuration of the SDK. It's a lot of work.
**Shenoy Pratik** 26:04 Okay.
**Juliano Costa | Datadog** 26:07 If you think about folks that use Java, whenever they see that, they are like, no, thank you.
**Donal O'Sullivan** 26:16 Sure. The bloody configuration for a Java service alone is insane. But anyway.
**Juliano Costa | Datadog** 26:23 But for Java, you can just drop the agent and it's done.
**Donal O'Sullivan** 26:27 Yeah, yeah, yeah.
Spring Boot is notoriously annoying for configuration, but anyway, separate thing.
**Juliano Costa | Datadog** 26:36 So, yeah, I think, I think that's a good… That was an idea that I just had here while we were discussing.
I think maybe we can… Push towards adding the hotel config file to a different service.
And then we have product catalog showcasing manual SDK configuration.
And… check out using the HLC.
Because then we can demo, like, everything.
Oh.
Yeah.
**Felix Felix (IBM India Pvt Ltd)** 27:12 We have,
**Shenoy Pratik** 27:13 I like that we are testing OTEL C because Even though things are in alpha, like, OpAmp had the same question when it came in.
Even if it's not stable, it's still, like, a good starter for anyone who is learning the new stuff on the portal.
community side. So yeah, I'm totally up for adding it. The how part is the thing that we need to double down on. But yeah, I think you can put your… comment there, Juliano. I'll also look deeper into this today. I didn't get time last time.
Sorry Felix, I cut you off.
**Felix Felix (IBM India Pvt Ltd)** 27:48 I was thinking that we have an overload of Python services, maybe if we can convert some of the Python services into Go.
**Juliano Costa | Datadog** 27:57 What… From your addition of the three Python services, we actually added one of the things that were pending for a long time, like the… we just landed a rewrite on the recommendation service into Spring Boot 4.
I know that we already have a couple of, well, we have one Java service, one Kotlin service, but Spring is one of the most.
**Felix Felix (IBM India Pvt Ltd)** 28:25 Post.
**Juliano Costa | Datadog** 28:25 used frameworks in Java, and we didn't have any demo of that on the demo, and now we have.
But that was just possible because we now have a A bunch of, Python services in.
And, I know that we are kind of at time, but we also have a ZIG PR, which is super cool. So, yeah, I don't, like… People will have to have, like, a server to actually run the demo.
Computers will like laptops won't be enough anymore.
Oh.
**Donal O'Sullivan** 29:08 It's definitely cool seeing that SIG service. Yeah.
Yeah. I don't know any SIG, but yeah, it's a cool language.
**Juliano Costa | Datadog** 29:18 Who knows, like… But, okay. So, I think we… I think we have a nice, idea here. So let's, I will update CDL on the… on the thread.
And… Yeah.
Cool.
Anything else that anyone wants to to share, discuss.
Okay, so Maxime, we wait on your PR then.
**Maxime Quentin** 29:59 Yep.
**Juliano Costa | Datadog** 30:00 Yeah, take your time, no rush.
**Maxime Quentin** 30:03 I'll try to do my best, maybe next week.
**Juliano Costa | Datadog** 30:06 Cool.
Cool, cool.
I don't know if you know, but this is, like, all my Datadog access will be revoked by this Friday.
So, I'm, I'm… I'm leaving the company, so… but feel free to reach out to me on LinkedIn, and on 2nd of November, I'll be active again on Slack, and I can.
**Maxime Quentin** 30:34 Cool.
**Juliano Costa | Datadog** 30:34 And of course, I can review the PR in the meantime, so, yeah.
**Maxime Quentin** 30:39 Yeah, understood, thank you.
**Juliano Costa | Datadog** 30:41 Cool. I don't know if you are on the CMCF Slack, but I'm also reachable there. I just won't be reachable on the Datadog Slack.
**Maxime Quentin** 30:50 Yeah, I'm not part of the Demo Cnf.
**Juliano Costa | Datadog** 30:54 Oh.
**Maxime Quentin** 30:55 Which one's the channel?
**Juliano Costa | Datadog** 30:56 Well, I'm also… I think I… No, I'm not on the browser one, but you can find me on the CNCFs like Juliana Costa if you want. But we have a hotel-demo, no, hotel-community-demo.
**Maxime Quentin** 31:16 deal. Okay, cool.
No.
I got it now.
Thank you.
**Juliano Costa | Datadog** 31:22 Cool.
Yeah.
Thanks, everyone.
**Maxime Quentin** 31:29 Bye-bye.
**Juliano Costa | Datadog** 31:30 Have a great rest of the day. Cheers.
**Donal O'Sullivan** 31:32 you guys.
