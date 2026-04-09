SIG: Developer Experience SIG Meeting
Date: 2026-04-08
Duration: 68 minutes
============================================================

## Zoom Recording Transcript

Juliano Costa | Datadog 00:00:12 Hello, hello!
Johanna Öjeling 00:00:14 Hello!
How are you doing?
Juliano Costa | Datadog 00:00:24 Good.
Johanna Öjeling 00:00:25 How was KubeCon, Juliana?
Juliano Costa | Datadog 00:00:29 It was great, actually, yeah. On my ride to KubeCon, I got a text, a message from CNCF saying, hey, your topic was on waitlist, do you want to present on Monday? That was Saturday.
Yes, sure. So I actually gave two talks.
Johanna Öjeling 00:00:51 Wow!
That's great. Were both talks of the same day, or…
Juliano Costa | Datadog 00:00:57 No, so the… this one was for Observability Day on Monday.
Johanna Öjeling 00:01:01 Okay.
Juliano Costa | Datadog 00:01:03 one was on Wednesday.
Well, the observability they want was actually about the hotel demo, so that's why I accepted, because I'm involved in the project since the beginning, so yeah. Yeah. I can talk about the demo for a day if they want.
Johanna Öjeling 00:01:19 Okay, cool. Okay, yeah, and the talk for the main conference was the one about the, kind of costs of auto instrumentation, yeah.
Juliano Costa | Datadog 00:01:30 Jam.
Yeah, I'll share the…
Johanna Öjeling 00:01:33 the recording.
Juliano Costa | Datadog 00:01:34 parties when… no, they… they're not… They're not yet, live.
Johanna Öjeling 00:01:38 Okay, yeah. Yeah, they're usually pretty quick with publishing done on YouTube, so probably within the next few weeks.
Juliano Costa | Datadog 00:01:49 Yep.
Johanna Öjeling 00:01:50 Yeah, good to hear. 2012.
Juliano Costa | Datadog 00:01:53 Thank you, yeah.
So, first of all, how are things, Tristan? A couple of weeks that we don't see you here, so…
tristan 00:02:02 Yeah, that's.
Juliano Costa | Datadog 00:02:03 At least I.
tristan 00:02:06 Finally Things are good.
Juliano Costa | Datadog 00:02:10 Awesome.
Glad to hear.
Okay.
I think on that, but… the agenda… not on the official agenda, but I think on the agenda today, we have… We would have… Some updates on the…
tristan 00:02:35 Blackpool.
Juliano Costa | Datadog 00:02:36 or some discussions on the blog post regarding Keycloth, right?
Perk (Marcin Stożek) | Elastic Ingest 00:02:41 Yes.
Alexander Schwartz (IBM) 00:02:43 And that's when we have allergies.
Perk (Marcin Stożek) | Elastic Ingest 00:02:44 Thunder here.
Alexander Schwartz (IBM) 00:02:45 Yes.
Juliano Costa | Datadog 00:02:47 Awesome.
So, before we jump into that, Johanna, did you hear back from… From the folks from the docs.
Because I think the Adobe one was supposed to be released last week, right?
Johanna Öjeling 00:03:05 Yeah, exactly, and I was on PTO last week, but yesterday, when I got back, I asked Tiffany from the Communications League, and she said that she will schedule it for Today, so, or she updated the day to today, so hopefully later during the day it will be published.
Awesome. So, yeah, and she approved it, so I think, yeah, we're just waiting for it to be merged.
So we'll have the Adobe one published today, and then I've been messaging with Neil from Skyscanner, back and forth, since they needed a bunch of internal approvals, and Now, he provided updated architecture diagrams, so I drew them with ExcalDraw, and I asked for his And a final confirmation or approval, so hopefully he can give that this week, and… We can go ahead with publishing that one as well.
Juliano Costa | Datadog 00:04:09 Awesome, awesome.
Free!
Johanna Öjeling 00:04:12 And then, yeah, the, another blog post was the Grok one, which I've, written the draft in our internal Google Doc, and Tristan will find, Andreas' email address, to, yeah, share with him for this review.
Juliano Costa | Datadog 00:04:37 Okay, cool.
Awesome.
Johanna Öjeling 00:04:42 And I think those are the blog post updates.
Juliano Costa | Datadog 00:04:48 Thank you. Yeah, this is… This is great stuff.
And… okay, so… Hello again, Alex. Thanks for joining.
Alexander Schwartz (IBM) 00:05:04 I don't know.
Juliano Costa | Datadog 00:05:05 I didn't have the chance to meet you on, at KipCon. The week was a bit chaotic.
Alexander Schwartz (IBM) 00:05:14 It definitely devotes freedom for me here.
But maybe we do a round of introduction. I think I did not meet Johanna, at least.
Tristan, was you… had you been here last time? I'm not sure.
Juliano Costa | Datadog 00:05:30 Nope.
You're on mute.
Mute. You're still on mute.
tristan 00:05:36 I clicked it. No, I wasn't here last time, I don't think.
Alexander Schwartz (IBM) 00:05:41 Yeah, then let's start with a round of introductions. So, I'm Alexander, I'm one of the keydog maintainers.
There were a bunch of us, I think 10 or 12 at the moment, I kind of lost track.
I'm not the project lead, that's Dean Torgerson, who's based in Norway.
you might meet me at some of the conferences here and there, so I was also at KubeCon in Amsterdam, We had a booth there, well, a booth… well, a kiosk, as they call it, in the Project Pavilion, we had a half day.
project probably in the afternoon. We had the maintainers talk. There was T CloudCon for the second time at the KubeCon event, as a pre-event.
So, I was actually late arriving for the event because my… well, a plane broke down, which was unfortunate, but from Tuesday onwards, I was there.
I usually work in the, well, SRE space, production readiness of Keyclog, so I was involved in things like OpenTelemetry, observability.
Making Keychdoke in general simpler to run.
on both bare metal and Kubernetes.
Them heading a team of, like.
3 to 5 engineers, so… well, it changed over time.
That handled all those things, like load testing, metrics, observability.
That's what I'm doing.
Uncool.
IBM pays my surgery.
That's me.
Well, handing over to Tristan or Joanna.
Johanna Öjeling 00:07:27 Yeah, pleasure to meet you. I'm Johanna. I work at Grafana Labs as a senior software engineer on the OpenTelemetra team.
And other areas of the hotel where I've been involved is the collector and opam.
Alexander Schwartz (IBM) 00:07:46 Great.
Yeah, love that stuff.
Perk (Marcin Stożek) | Elastic Ingest 00:07:50 Let me introduce myself as well, because I don't know if I met you, Tristan, actually. So, hi, I'm Perk, I'm a project manager at Elastic, working on OpenTelemetry and other stuff. Actually been around for, like, 6 years, but only Jane joined recently.
the org itself.
And I, and I talked with Alex during the… what was it?
Auto unplugged, I believe.
Alexander Schwartz (IBM) 00:08:13 Right, yeah, that's what I meant.
Perk (Marcin Stożek) | Elastic Ingest 00:08:14 Yeah, we had a very brief chat about the key clock, and Alex, you told me that you're using OpenTelemetrator, and then the idea came to mind, like, hey, let's do a blog post about it. So, that's why we have Alex here to do the interview. Thanks for joining.
tristan 00:08:33 Hey, and I'm Tristan, nobody pays me right now, but I've been working on OpenTelemetry for a while now, years, mostly in the Erlang and Elixir API SDK and, some of the spec.
Juliano Costa | Datadog 00:08:52 I think in the hotel space, Tristan is the oldest person that I know.
Well, at least in this call. Well, as everyone introduced themselves… Hi, I'm Giuliano.
I work for Datadog, and yeah.
Glad to have you here, because I think… the more projects from CNCF adopting ULTEL, the better for the project, and for the ecosystem as a whole. So… Yeah, I'm really interested to hear how you're using it, how users can configure their own stuff.
And so on. So… Cool. Happy to have you here.
Alexander Schwartz (IBM) 00:09:39 Great, yep.
Juliano Costa | Datadog 00:09:41 So, in the… in the meeting… in the meeting notes, we have… A tab.
called blog post outline. I think I've shared that with you before, where we… We had a couple of questions. We also have a different doc. I think everyone is in here. Johann is here, Tristan is here.
I think for some… I think it's something related to… to Datadog that removes people from… Chrome… From the.
Perk (Marcin Stożek) | Elastic Ingest 00:10:21 They're a cushion.
Juliano Costa | Datadog 00:10:22 automatically. Okay, yeah, go ahead, sorry.
Perk (Marcin Stożek) | Elastic Ingest 00:10:25 There are questions for the interview with Key Clock at the bottom of the blog post outline.
Juliano Costa | Datadog 00:10:30 Yes, yes, but I… I have another… we have another doc where we draft the thing, so… Oh, sure. I was just thinking about starting there, but we can do this, because this, This meeting notes doc is public.
Perk (Marcin Stożek) | Elastic Ingest 00:10:47 Hmm, fair enough.
Juliano Costa | Datadog 00:10:47 But this call is recorded anyways.
So… I think we can just… Go with it.
I'm just fine. So I'll just open a new tab here.
Or a key club, and… Oi… We go.
Great.
Alexander Schwartz (IBM) 00:11:23 So, yeah, so what… should I just…
Juliano Costa | Datadog 00:11:27 I think, ideally, we just go as a conversation, so you do not need to, kind of, go bullet points, and I think when we feel that there are some stuff that we want to know more, we just ask more. So, I think… Ideally, let's start with the first question, because I think this one is important to everyone. Like, what is KeyCloud?
Why would I use it?
Alexander Schwartz (IBM) 00:11:55 Yeah, so it's, well, as it states here, it's an identity and access management system, so what you can do with that, you can authenticate humans with it.
And actually, you can also authenticate Non-human users with it, so… For human users, you usually have then, oAuth2 on OpenID Connect.
And also SAML.
If it comes to non-human users, you might have things like, MuddyConnect client credential grants, so basically.
all the applications have some credentials where they then can get a token, and once you have a token, you can access APIs.
OpenMID Connect for, I think, I'd say the modern stuff.
Summel for the older stuff, Keyclog then does all the other magic you want to do, like, connecting that to an LDAP, connecting that to, maybe even Kerberus, so if you're logged in with Kerberus, you might exchange that to an… OpenID Connect or SAML token eventually, We now have also a great integration that you can use with Spire to authenticate non-human users to KeyCloak.
You can also use Kubernetes service account tokens.
You can also do a lot of brokerage, so… maybe your organization is using KikTok, another organization is using Okta, they all talk the same language of OpenMuddy Connect, you can do Federation.
And then have users of other companies accessing the services that you then eventually secure with KeyCloak, so all that magic.
That's a… fabric around identity that you're weaving there. Cato can integrate that.
Is that… some answer?
Maybe some crit.
Juliano Costa | Datadog 00:14:01 Yes.
Alexander Schwartz (IBM) 00:14:01 Do you have around it?
Juliano Costa | Datadog 00:14:05 No, I, I think… I think, I think we can move on and, just… come back if… if anyone has any questions.
Perk (Marcin Stożek) | Elastic Ingest 00:14:19 Also, Martin joined? Hey, Martin.
Martin Bartos 00:14:22 Yeah, hello guys, sorry I'm being late after PTO, so, yeah, slow start. Sorry.
Juliano Costa | Datadog 00:14:30 No purchase.
Martin Bartos 00:14:32 Yes, so, just to introduce myself quickly, I'm Martin Bartucci, I'm part of Kikluk Cloud Native team, and I was working on the observability stuff, mainly for tracing.
Yeah, locks, etc. So, yeah.
That's it.
Alexander Schwartz (IBM) 00:14:52 Yeah, great to have you here.
Perk (Marcin Stożek) | Elastic Ingest 00:14:54 And you are at Red Hat, right?
Martin Bartos 00:14:59 Right now, I'm part of IBM, after the transition, the same as Alexander, so we are colleagues, yeah.
Perk (Marcin Stożek) | Elastic Ingest 00:15:08 Thanks for joining.
So we've just started, we've just started the interview part, with Alex. I'll share, We'll share a doc when we work on this, and we just, you know, go out… we just have a free conversation.
Going through all those points.
Alexander Schwartz (IBM) 00:15:28 You're asking.
Perk (Marcin Stożek) | Elastic Ingest 00:15:29 So nowadays.
Alexander Schwartz (IBM) 00:15:30 So you asked, well, how is hotel use in the project? So, that's the next… well, if there are no more questions around IAM, at the end.
So… at some point, we wanted to do tracing. Well, we were doing performance analysis, and our users want to do that as well, and the primary thing where we added OTel to KeyCloc is then that we added But we wanted to do tracing, and… Keyclog is a Java-based product, at least when it comes to the backend, And there was the Java agent, and we used that for a while, but then… That delivered a very slow start for KeyCloak.
So the start is then delayed by, let's say… a couple of dozens of seconds, so that was not something they wanted to support. Also, when it comes to… The Quarkas, well, Cake Dog is built… with Java on top of Quarkus, the Quarkus people always told us Don't use the instrumentation, because you might then lose the tracking of the traces.
And with that… We were waiting for the full support of OpenTelemetry Tracing appearing in Caucus.
And once that was there, we built on top of that, and… Martin adopted that for our use inside of Keyclog, so we'd have some internal APIs that we then interact with.
building, yeah, building tracing into Keyclog.
And… So… Perk (Marcin Stożek) | Elastic Ingest 00:17:09 Can I ask you a question?
Do I… sorry, do I understand correctly, then, that, you had a… you had a performance problem, and you wanted to investigate that?
Alexander Schwartz (IBM) 00:17:19 It's more like we… well, we wanted to ship observability with batteries included with key cloak, and when we're doing then.
Performance analysis of our own load tests.
tracing helps a lot to figure out, like, is it, like, the database slowing you down, the LDAP slowing you down, or an external service slowing you down?
And that's why, or… I'm a big fan of exemplars.
So that when you then can link from a metric.
Directly to an example trace that shows you why this… 99 percentile is so slow with an example.
I was driving for, then, the exemplar support in Caucus to meet our needs, for example.
tristan 00:18:11 Can you say, what is Quarkus? What do you use it for?
Alexander Schwartz (IBM) 00:18:15 Yeah, Cuocus is a… Well… a Java framework.
for enterprise-Z Java, I would say.
So if you know spring, for example, it would be a competitor.
While Spring came up with their own interfaces.
Quarkus, embraced the Java EE, or Jakarta EE standard.
And it then integrates a lot of frameworks.
like, for example, Hibernate, how to do REST resources, what else? Well, the observability of OpenTelemetry for us.
Anything I'm missing, Martin?
What else? What's the other goodness that Quarkus brings for us?
Martin Bartos 00:19:06 Yeah, I think they wanted to improve the Java EE itself, right? Instead of us using Spring Boot or something else to have cloud ready.
framework, let's say, for building applications, right? So, they are bragging about this, fast startup, you know, slow memory consumption and everything, you know, to move on with the Java a little.
Alexander Schwartz (IBM) 00:19:34 Low startup times, low memory footprint, This is what the caucus people are always bringing about, right?
So… yeah, so… with that, I'm just trying to pull up the docs that we have around that. So with… tracing… So we have a doc here, and, well… In the third iteration, we were able to trace only incoming HTTP calls and the calls to the database.
With, later releases, we then included, wrapper for LDAP, so you now see all the LDAP things, and we then eventually also enable tracing for outgoing HTTP calls.
Which then completes the picture. Basically, older… Yeah, all the calls that go into KeyCloak and getting out of KeyCloak are then fully traced.
We made it eventually fully supported.
And all the people… all the key clock users need to do there, they need to, well, point it to… an OpenTelemetry gRPC receiver.
And that's it.
So… Perk (Marcin Stożek) | Elastic Ingest 00:21:00 I have a question about that, if I can, because those authentication flows, well, they can be, like, quite complicated, right? Complex.
Is it… is there something that you prioritize?
Or you just create spawns for everything?
Alexander Schwartz (IBM) 00:21:16 We create spuns for everything. There's a… You can, that's sampler, so you can add a percentage of How many pers… well, if you want to do for 1% or 0.1% of tracing?
And, so everything is then traced. So it's the admin UI, it's the account console, it's the open… IDConnect things, it's the sum of things.
Gasp bands for everything.
Juliano Costa | Datadog 00:21:46 any… any way to configure, that? I mean, there's the sampling, but.
Alexander Schwartz (IBM) 00:21:54 That's all there is. Well, yeah, there's… the other thing is then, if you… if you… yeah, the sampling is then always on, always off. Trace ID ratio, there's the parent-based, always on, always off, and parent-based trace ID. So I think the parent-based… I'm not sure if we disabled that by default, because we are a bit security conscious.
Because we don't want… people… well… you might have key clock running, you connect it to the internet, and then people send you all these tracing headers, and that might eventually enable tracing for all of it.
Maybe you don't want to overwhelm your observability stack in the backend. So, that's a bit of a… thing, I think we disabled it by default. People need to really opt-in into parent-based tracing. And, well, and the nice thing with all that is, if you're having your application landscape and all the applications talking to KeyCloud.
They might start the spans, and then you can see why has this call failed.
why it was slow, all the error messages, what was the LDAP query, what was the SQL query that fired there, all this information is then available in your… Yeah, infrastructure fabric.
Perk (Marcin Stożek) | Elastic Ingest 00:23:18 Interesting. So you have the context propagation between the app that talks to KeyCloud?
Alexander Schwartz (IBM) 00:23:23 Keep close.
Yep, it talks usually HTTP. When it talks HTTP, well, the app needs to forward this tracing headers as part of the OpenModi Connect protocol, and if they do that, they will have all this information available.
Perk (Marcin Stożek) | Elastic Ingest 00:23:36 And what about the context propagation when you, when you call external identity providers?
Alexander Schwartz (IBM) 00:23:42 Yes, we sent this context propagation there as well. It's talking HTTP to the other IDPs, and we propagate that context over there.
So it's there, So you can see that very good when KeyCloud talks to another key cloak, you can trace it… all the calls from one key clock to another key cloak, or from one realm to another realm.
Perk (Marcin Stożek) | Elastic Ingest 00:24:03 Very nice.
Alexander Schwartz (IBM) 00:24:04 Let's just see.
Juliano Costa | Datadog 00:24:09 I… I have a follow-up question on that.
Alexander Schwartz (IBM) 00:24:12 Yep.
Juliano Costa | Datadog 00:24:13 So… I saw that you have a couple of tags here.
Alexander Schwartz (IBM) 00:24:21 I…
Juliano Costa | Datadog 00:24:22 think those tags are, span attributes, right?
Alexander Schwartz (IBM) 00:24:28 Yes, the financial goods, right, yes.
Juliano Costa | Datadog 00:24:30 Yeah, yeah. Yeah, I think that's how… that's how Jaeger calls it, so… Is there any convention on… on that? Any… Is there… the question is… well, let me try to rephrase. Do you know about the semantic conventions on motel?
Alexander Schwartz (IBM) 00:24:53 I know about them, but at the moment, we actually don't care much about them.
Juliano Costa | Datadog 00:24:58 So it's something…
Alexander Schwartz (IBM) 00:24:58 point, well, at some point, what we changed… well… These… spam tags, whatever.
We added them… we added… we kind of reworked the traces between two releases, and Martin Bartos was the one who actually needed to clean it up in a pull request in the docs.
So we moved some of these tags from the parent span to a child span.
And that was… Surprising some people, because for a long time, we were thinking we're creating these bands for humans to read.
But now it appears that actually non-humans are trying to make sense out of that even more than before.
I would claim, even if we move the text around, they're still searchable, you just come up with a different span in the end.
But then it's still… Some users brought it to our attention that we should do better on that one.
Juliano Costa | Datadog 00:26:00 Cool.
To be fair with you, I don't think we have, so, actually checking the docs right now as we speak. I don't think we have any semantic conventions for identity provider at all.
So maybe this is something to, Actually, maybe start discussing, and and… Yeah, come up with… official naming, because I saw that at the moment we are using KCDOT, and KC is…
Alexander Schwartz (IBM) 00:26:37 Kikloquine.
Juliano Costa | Datadog 00:26:39 So, yeah, exactly, totally connected with the project.
If we can have, like, something more generic and, that would big part of the whole ecosystem of identity providers, where if the user is using KeyCloud or another project that I don't know any other one.
They would have the same semantics on those, and that's the goal of semantic convention. But again, this is not the focus of this talk, was just to…
Alexander Schwartz (IBM) 00:27:11 I just posted an issue in our notes here, for the semantic, convention that we opened an issue. I learned about that… more about that, when I was in… in Brussels earlier this year, the unconference, and maybe the session… That there's, like, user, agent, user, and session.
those items… might offer some of these elements that we want to have in there.
Unstable at the moment, maybe we're picking them up Eventually, maybe some people tell us they're useful or not.
Let's see.
Juliano Costa | Datadog 00:27:49 Cool.
Awesome.
Okay, so… moving on, once I enable my… tracing. So, like, if I run the… If I run Keycloth with the dash dash tracing enabled.
Alexander Schwartz (IBM) 00:28:10 Right.
Juliano Costa | Datadog 00:28:10 Will that also enable hotel metrics, or not?
Alexander Schwartz (IBM) 00:28:18 Outlaw metrics and hotel logs are separate, and they arrived as an experimental or preview feature in our January release, and Martin was involved in that, so… That's… Something that came then, like, Second or third, even.
It was a bit dependent on the Quarko support on that, what I understand.
But we want to have that… well, at the moment… well, at some point, we supported files, console, This is Lord.
And we're now adding added OpenTelemetry logging, I think in January or something like this.
Perk (Marcin Stożek) | Elastic Ingest 00:28:59 Cool. So that's logging, and what about metrics?
Alexander Schwartz (IBM) 00:29:03 Those as well. Yeah, yeah. We usually will provide them using the Prometheus endpoint.
Perk (Marcin Stożek) | Elastic Ingest 00:29:08 Hmm, okay.
Alexander Schwartz (IBM) 00:29:09 So that's what we've been doing for years.
But with OpenTelemetry metrics, we're now having experimental support for that as well.
Juliano Costa | Datadog 00:29:19 Is this… I guess this is different from the dash dash metrics dash enabled equals true, right?
Alexander Schwartz (IBM) 00:29:26 this…
Juliano Costa | Datadog 00:29:27 With the metrics enabled, this would be the Prometheus one.
Alexander Schwartz (IBM) 00:29:33 I'm just… Yeah.
Juliano Costa | Datadog 00:29:33 Trying to find other dogs. Sorry.
Alexander Schwartz (IBM) 00:29:36 Yeah, yeah, yeah, yeah, just, I need to look up in the TikTok release notes.
Martin Bartos 00:29:41 Yeah, but the situation about the OpenTelemetry integration in KeyCloak is that, we have the separate, yeah, support, right, for each of them, as right now we are supporting only OpenTelemetry tracing.
Right? But for the metrics and logs, we are still waiting for the full support from the Quarkus, as Alexander mentioned, right?
But it's still going on, right? We try to unify the whole observability stack, you know, not having open telemetry tracing, then having the pool mechanism with the Prometus, right, with the endpoint and everything, then… sending clocks in a different way, right? So right now, we are in a way that we want to unify it, and you know.
just simplify the whole setup of the observability, because, yeah, I've heard a lot of times on conferences and some meetups that people don't know how to set up their observability stack, right? And for KeyCo, they need to, if they want tracing, you know, having the open telemetry collector, stuff like that.
extensions, right, than Prometheus, and different approaches how to… how to aggregate this stuff, so we are in a way to moving on together, so I hope it's… we will be able to do it soon, yeah.
Alexander Schwartz (IBM) 00:31:08 And I just posted a link, and then meeting minutes, That shows how to use the OpenTelemetry for… for metrics and… and logs as well.
I think we're still keeping it preview in the upcoming March release, right?
Martin Bartos 00:31:24 Yeah, probably. Yeah, also the thing about metrics, right, is that we are using Varkus extension called Micrometer to open telemetry Bridge.
Right? As, we are still on the micrometer, as, it has also, powerful tools, right? And, maybe some also benefits. Maybe Alexander will know more about the micrometer and open thermometry metrics, right, difference, but…
Alexander Schwartz (IBM) 00:31:56 Yeah, micrometer is the… library in the Java world that collects metrics, I would say, and it supports several things where you can publish the metrics afterwards, and we only used it to publish the metrics to Prometheus.
Using the scraping endpoint URL.
And another thing is then open telemetry metrics at some point. So it's… provides a great abstraction, I would say.
It has aged over the years a bit, maybe, but maybe eventually OpenTelemetry will take over that as well, but let's see how it evolves. There's no rush and hurry on our side on this.
Juliano Costa | Datadog 00:32:37 Go ahead.
tristan 00:32:38 You haven't looked much at replacing the metrics yet? Because I know Micrometer supports a lot of features that OpenTelemetry metrics don't have, so I would be curious if you've looked at that. Okay.
Alexander Schwartz (IBM) 00:32:50 So, the Quokus people are more into that, and we've known them, talked to them, and… Whatever direction they choose, we will follow, so that's…
tristan 00:32:57 Okay, so they might… they'd be the underlying… so they'd probably implement those features to alleviate any pain there. Okay.
Interesting.
Alexander Schwartz (IBM) 00:33:07 I can connect you to people if you want to talk to those people at some point.
Okay.
tristan 00:33:12 That might be interesting.
Alexander Schwartz (IBM) 00:33:15 Good, so that's our story around OpenTelemetry, but yeah, go ahead with questions.
Juliano Costa | Datadog 00:33:20 So, we have a couple of links already with the… how to enable, but I think from your previous answer, the user, once it enables.
you get what you get, like, you cannot modify or… of course, you can do all the processing on the collector side, that's how folks do, but on the configuration side, you cannot say, hey, I want to capture I don't know, like, XYZ, or I want to get visibility into this specific part of the project, you would need to build your own key clone, right?
something… Well, you recommend.
Alexander Schwartz (IBM) 00:34:04 You can… you can, for example, I think you can disable SQL tracing, you can disable LDAP tracing if you choose to, if I recall it correctly, but… If you write your own extensions for Keyclog, you can… well, we offer you, like, a… Way to also integrate into tracing, if you're into that.
We call it a service provider interface, or SPI, that you can integrate with. You can do the same for metrics, so if you're writing your own extension, you can also provide your own metrics.
That eventually end up in the same sink.
There are… there's at least one community extension that provides more metrics that we currently don't provide.
We don't provide them for a reason, but that would be another call.
those SPIs are called… well, they're called internal SPIs, we don't make them officially supported and stable across releases, but that usually does not keep people from using those SPIs anyway, so… Martin, are you aware of people using the SPIs to add custom traces, custom metrics?
Martin Bartos 00:35:27 Not sure. I do it for custom extensions, so at least one user of the… custom tracing, right? As, we created the interface for them.
To extend the tracing, right? Yeah, provide new traces, so it's quite useful.
Yeah, but not sure how many people using that.
Alexander Schwartz (IBM) 00:35:55 Yeah, I think that answers that question.
Perk (Marcin Stożek) | Elastic Ingest 00:36:06 Juliana, you're a bit, by the way.
Juliano Costa | Datadog 00:36:10 Thank you. Yeah, I was talking for a minute already. I think we already covered the deployment part with, So, it is built for the users, right? You, as maintainers and contributors to the project, you also use, but it's mainly built for the users to view the things that they are running, or…
Alexander Schwartz (IBM) 00:36:35 Well, we use it in our load tests to, like, having a white box load test, in a way. Whenever we do load tests and performance analysis, we use it ourselves, but it's primarily built for the users.
Juliano Costa | Datadog 00:36:49 Cool, and no, Honest question from my end. So, when you test on your, load test, when you're doing your load test, do you test if the traces… if the spins are still connected in the traces, and that type of things, or just if you are producing spins, good, move on?
Alexander Schwartz (IBM) 00:37:14 I think our test coverage is pretty bad on tracing, yeah, I have to say.
Juliano Costa | Datadog 00:37:21 Okay.
Alexander Schwartz (IBM) 00:37:22 I think we now have one or two tests around it, but yeah, it's… Yeah, it's pretty… well, I think we have one or two tests, but we're not testing it extensively.
Juliano Costa | Datadog 00:37:36 Oh, Great, and within the project, do you have any… Update cadence? Are you just, whenever you feel it, you just bump dependencies? Is there, like, dependable, renovate, whatever, automated?
Alexander Schwartz (IBM) 00:37:57 rounds.
Juliano Costa | Datadog 00:37:57 On… on the project?
Alexander Schwartz (IBM) 00:37:59 So the dependencies, we inherit most dependencies via Quarkus, and Quarkus has, like, a major release every, I'd say, 3 to 4 years.
And a new long-term stable release every… Half a year?
Like, long-term, stable, minor release every half a year.
And… So, whatever gets into that minor release… stable long-term minor release, we consume it.
So that's how we work on that.
Juliano Costa | Datadog 00:38:45 Okay.
Huh.
So, just to see if I got it right, you rely totally on the things that Quarkos is using. You, as a key clock, you do not add any extra dependencies.
that you manage on your own? Like, hotel-related dependencies?
Alexander Schwartz (IBM) 00:39:07 I think we might consume the HTTP client… dependency on our own for the instrumentation. That might be the only one we instrument on our own.
the wrapping of LDAP, we built it our own.
But in the end, I think the tracing stuff, at least, is pretty… Stable and just works, and we don't expect any… maintenance on that one, mostly. So at the beginning, we might tune the nesting of the spans, and maybe added another level of nesting.
If you're a Java developer, you have some Java beans that do REST calls, and I think at some point we're… adding, like, which method is called there, like, in more or less auto-instrumentation there. Did a bit of better error handling, and that was one of the bugs that we fixed at some point.
that the span wasn't close to… in some of the ever-handing paths, but then it's… now I'd say it's stable.
We don't plan any changes around it, it just works.
Boom.
maybe… The only thing is maybe sampling.
If people would come… would like to do a custom sampling.
But I never… no one ever approached me on that one.
So, like, people usually ask me, can I sample only the error requests?
And then I tell them, well, that's difficult.
But, in this… well, yeah.
Juliano Costa | Datadog 00:40:45 If they use the collector or not.
But then they need to manage another… another thing. Yes.
Alexander Schwartz (IBM) 00:40:53 Yeah, then you have the collector, but then what I understand, that you basically need to trace 100% in the application itself, which might then give you a lot of overhead, and then you throw away 99.9% of what is collected, and that's maybe not a good answer to that question, I would say, but…
Juliano Costa | Datadog 00:41:11 Yes.
Correct.
Alexander Schwartz (IBM) 00:41:18 Trade-offs everywhere.
Juliano Costa | Datadog 00:41:23 Cool. Okay.
So, if we… I think we are moving to the last couple of questions here. During this process of… adopting hotel. I know… I know that in the key clock approach, you… are mostly, kind of, inheriting from Carcos, so maybe the… most of the pains were from the Quarkus folks while integrating Hotel in Quercus, but on your end, do you have any pains, or are you having any pains on setting up Hotel and using Hotel and enabling Hotel for your users?
Alexander Schwartz (IBM) 00:42:06 So… I think when we looked at the instrumentation via the Java agent, we considered that… well, we got some advice from the caucus people, calling it not Not as perfect as they would like it to be.
So we never shipped that as a solution to users. Still, we used it a lot when… while we're waiting for the Quarkas integration and doing our own performance analysis.
To a lot of things.
We had some pain points when it came to exemplars.
We had a bit of problems with the error handling in an early release in our own code.
We're not closing traces in the right place.
But I think we now overcame those problems.
I'm not sure, do exemplars work with OpenTelemetry metrics?
I think that might be…
tristan 00:43:08 Yeah.
Martin Bartos 00:43:11 Voucher.
tristan 00:43:12 What do you mean in Keith Cloak?
Sorry.
Alexander Schwartz (IBM) 00:43:17 Shall we say again?
Yeah, we need to double-check if, Exemplars work with the metrics that are sampled, or… Through this chain of, micrometer open telemetry metrics.
And to receive in the end. So if that ends up in… in Prometheus eventually to show up in the Grafana board.
That's something I need to check.
Juliano Costa | Datadog 00:43:50 And then… looking back into, this journey that you, you, you both had on adding hotel to the, to the project.
Was there anything that you wished it existed when you were doing? Like, I don't know, better documentation, or…
Alexander Schwartz (IBM) 00:44:13 Maybe a good… well… maybe back in the time, if I would have been more aware of a test harness of OpenTelemetry tracing, I might have Introduced it back then in our test suite.
at the Oak Teland conference in Brussels, I learned that there are now tools that I can use in my integration test that might then verify whatever OpenTelemetry output I produce.
Knowing that everything is…
Juliano Costa | Datadog 00:44:50 You may open the Lantree Weaver.
Alexander Schwartz (IBM) 00:44:52 Yeah, yeah, that's annoying, I think.
No, I'm now aware of the… the name and the project being available. Now that everything is running, If I might… Find the motivation to actually add it to our pipeline.
I'd say unlikely.
But maybe I have a… maybe I find a pocket of time to do it at some point.
At the same time, we're a Java-based project, so anything that you could integrate with the Java test suite.
is usually better received than something that runs externally, put it this way.
Semantic conventions… It's on the… well, we didn't care much about them.
maybe… We should care more about them.
when… People would start complaining, About it more that we're not following them.
Juliano Costa | Datadog 00:45:58 I think…
Martin Bartos 00:46:00 Yeah, sorry, only the thing is that, from what I've seen in our repository and stuff, there's not so many people arguing or complaining, right?
Or something, so we don't have any exact numbers, how many people are actually using that, right? If they are using some workarounds.
or if they need something else, we just don't know, I would say. I'm not sure about Alexander, if the perception is the same, right? But, yeah, we don't have so much data from the users, let's say, so we are just… go in some direction, right? What we see as might be beneficial for a community, and it seems they just live with that, right?
Alexander Schwartz (IBM) 00:46:51 And I might claim, well, traces are for humans, and I still need to be convinced otherwise.
But, I know this is… probably a wrong answer to some people, but I might need to be more of the receiving end of that convincing argumentation.
Juliano Costa | Datadog 00:47:08 Well, yeah, I think we can have another call for that. I'm a huge Trace fan, but yeah, I'm a human, so… Okay, but I… one follow-up question on that.
I think for your own tags, and for your own attributes, it's pretty clear that you created the attribute, because there was nothing on hotel, or you just said, okay, this, this, and this is important, so let's add here. But I guess when you are… using, for instance, the HTTP client instrumentation.
In there, you just have the semantic dimensions, right?
Alexander Schwartz (IBM) 00:47:53 Yeah, so…
Juliano Costa | Datadog 00:47:54 You don't… you don't invent attributes in there, do you?
Alexander Schwartz (IBM) 00:47:59 Yes and no. So, well, we're not inventing our own attributes, that's true.
At the same time, we're using the HTTP client instrumentation out of the box, which might not be very compliant with some semantic conventions. Well, I think we stumbled across your semantic convention when we came across the… Metrics being exposed.
But, well, we use it as it is, and that's… and… People might be okay with it as long as we don't change it or break it. Well, as long as we don't change it, we're okay with what we shipped in initial release, put it this way.
Okay. At least I hope.
Juliano Costa | Datadog 00:48:41 Awesome.
Is there anything… Now, you as a… as a user of Hotel.
Not a user of Hotel produced by Key Club.
He was a consumer of the hotel project. Is there anything you're missing from the project?
The question is valid for you as well, Martin.
Martin Bartos 00:49:13 Yeah, just thinking about that, I would… I… like, to be honest, I didn't dig deep into the documentation about, open telemetry tracing and stuff like that, right? But it would be nice to have some, best practices with great visibility.
You know, because sometimes when you are in docs, it's so easy to go in too much details, right? And you just forget about simple stuff, that you should comply, right? So… Have it some tour guide, you know, or something like that, how to prepare your application, to comply with the open telemetry tracing, providing the semantic conventions, you know, emphasize that these are quite important, right? To not change anything else in the future, with the break-in change.
Right, so having some… some guide on that, because I think there's not so many people, you know, knowing the open telemetry completely, right? They are sometimes newcomers to this topic.
and they just have the requirements from the business unit or something, hey, we need, we need tracings, right, for observability and everything, so the path starts with the learning, right? So…
Alexander Schwartz (IBM) 00:50:42 I need to probably plead guilty towards… well, once the things started to appear in Grafana, I was happy and stopped.
Caring more about the rest.
There might be a lot of docs, but I might have not read them, if there are, so, Pleading guilty to that one.
Juliano Costa | Datadog 00:51:01 Yeah, once you get something, running and it's working, and you're happy with the result, then why touching it, right? Awesome.
Anything you find frustrating about the hotel usage?
You can also say nope.
Alexander Schwartz (IBM) 00:51:26 No, it's… I think it was good. I think at some point, I was also con… well… I was contributing some Java code at some places to the agent, and that was… A good contributing experience, Things were reviewed and eventually merged and ended up in another release, so that was good.
Back in the time I was using it, there was… it was a very active project. I haven't looked at for a while at the agent.
Juliano Costa | Datadog 00:51:59 I, I love this question.
If you could wave a magic wind and change anything about hotel, what would it be?
Alexander Schwartz (IBM) 00:52:10 Maybe we could make it pull-based and not push-based?
But that might be a thing, me being an old Prometheus user.
Yeah, I love this thing about… back pressure… well, the very simple way of Prometheus pulling metrics from an application It's so very nice when it comes to… it has back pressure in it built in, it has… Also, checking if the application is up or not, because it pulls it.
So this is the nice things about metrics and Prometheus, which OTEL never embraced, because it was always push-based.
Not sure if back pressure is now built in or not. I probably need to double-check on that.
Perk (Marcin Stożek) | Elastic Ingest 00:53:07 you could actually cheat here, because you could write all of your stuff in the file and then just pull it whenever you want. Okay.
Alexander Schwartz (IBM) 00:53:16 Yeah.
But then, like… Prometheus, but it can, like.
Pull less things, or then drop things anyway.
If it's not working out well. Something with Prometheus… it's using the same… well, when you have an overload situation with your application, we usually have the situation that the Prometheus endpoint is still being pulled, but will not be able to pull the metrics because the application is overloaded.
I hope to see a better experience with OpenTelemetry metrics, because they're then pushed.
Still pushed while the application is in overload and not accepting any more HTTP requests.
So that might be the upside of the push-based things, so… So I'm not all… Bird was… was pool.
We'll push.
So, both have their advantages.
Martin Bartos 00:54:12 Yeah, maybe for me, I'd love to have the magic wand, just wave, and have everything prepared, set up, and don't care about that.
Juliano Costa | Datadog 00:54:23 Me too.
The problem here is that you… so, like, you are the one providing that experience for the key cloud users, because they… for them, they just dash dash enable tracing, and that's done.
But for… for you, you are the one, like, actually building this stuff, so, Yeah, someone needs to build, so…
Martin Bartos 00:54:50 Yeah, thanks for…
Juliano Costa | Datadog 00:54:50 Or you're before.
Martin Bartos 00:54:52 That's also the situation with Quarkus, right? As we cannot concentrate on the observability, you know, like, full time, and deep into these topics and everything, so we just move some of these responsibilities to Quarkus, right?
And we just trust, trust that, so, that's some… something, like, that we cannot concentrate on that, right, fully. So, it's nice to have someone, that… Prepare something, at least, you know, some base points for you, right?
tristan 00:55:29 Yeah, actually, a question related to that. When a user of KeyCloak configures to use tracing and configures different things about, like, the batch processor or something, are they configuring KeyCloak or Quarkus in, like, their configuration files?
Martin Bartos 00:55:44 Rather, Varcus. We just propagate it, you know, we just provide the interface, keycrook interface for them, and these settings are mainly propagated to the Varkus site, right?
tristan 00:55:57 But they configure it through Quarkus set… I mean, through KeyCloak settings?
Alexander Schwartz (IBM) 00:56:02 Yeah, it looks better.
tristan 00:56:03 Okay.
Alexander Schwartz (IBM) 00:56:04 forward it to Caucus.
tristan 00:56:05 Okay, amazing.
Alexander Schwartz (IBM) 00:56:07 Yeah, one thing for a magic wand, so… All the things, all the labels that are… OpenTelemetry instrumented application sends me, I can't… I cannot trust them, because they're kind of provided by the application.
all the labels that Prometheus adds, I can trust them, because they're added by the trusted Prometheus that scrapes the metrics. So I can really trust from which part this information is coming. I can really trust from which Promises cluster this is coming.
When this is sent by OpenTelemetry, I can't trust this data because it's… Yep.
It can come from… it comes from a TCP socket, that's it.
tristan 00:56:50 Yeah, a lot of times that's actually… people add that by the collector in order to… like, the pod, stuff like that, instead of the application, but… yeah.
Alexander Schwartz (IBM) 00:56:59 Yeah, but then I need to run it as a sidecar as part of that port, right?
tristan 00:57:04 Well, I think you can also run it as… The demons, as long as it's in the same… Cluster and all the…
Alexander Schwartz (IBM) 00:57:10 Yeah, then I can trust that it's from that cluster, but I can't really trust from which pod it's being sent from, so…
tristan 00:57:15 No, I think it collects it from, like, the IP that it's coming from.
Alexander Schwartz (IBM) 00:57:20 Yeah, well… Let it be.
loop.
tristan 00:57:24 But it's still…
Juliano Costa | Datadog 00:57:25 Go ahead, go ahead.
tristan 00:57:25 This'll… Constrain on the user.
Alexander Schwartz (IBM) 00:57:29 I have lots of questions, like what data I can trust that is sent by an open telemetry application to the collector, and then… well, the collector is probably a trusted party.
But then, yeah, there's some authentication that can go on.
But then, how does that affect, like, filtering of labels and data at some point?
Juliano Costa | Datadog 00:58:02 I like that, because even if you have, like, sidecars running within the pod.
Alexander Schwartz (IBM) 00:58:11 Hmm.
Juliano Costa | Datadog 00:58:11 like, a super minimal collector. This data can be modified.
throughout the pipeline till it reaches the user. So, in the end, you actually cannot You cannot trust the data, because if the user is doing some modification in the middle, then…
Alexander Schwartz (IBM) 00:58:30 Yeah, if it's, like, if it's a… if it's a site… if the collector is deployed as a daemon set, as you said, Tristan. Well, it's probably deployed by the platform operators, and then I can trust it.
The collector, but maybe not the data center, the collector.
If it's deployed as a sidecar as part of my pod, then it's probably deployed by the application developers.
and then I cannot trust the data that it's sending.
Neither did… yeah, because it's then… whatever it sends, it's… Not the plat… the trusted platform operators.
managing it.
Perk (Marcin Stożek) | Elastic Ingest 00:59:08 But if you do it… if you do it, like, as a gateway, then you have the very similar experience of what you get with Prometheus, really, because then the gateway scrapes the API server, gets the metadata, the only thing that it… well, has to trust is the IP, but that is exactly the same case with Prometheus as well.
Alexander Schwartz (IBM) 00:59:26 Well, with Prometheus, it will add the pod label. Well, it will add all the Prometheus tags.
Well, it will… Prometheus will be configured by all the Kubernetes metadata in the end, so it will connect to a specific pod.
It will get the metrics from the pod, but then all the labels of From what pot it came from, what pots this… what labels this pot had.
Other than… scraped from the trusted community source, and are not added by the application itself.
Perk (Marcin Stożek) | Elastic Ingest 01:00:02 the API server, but that is the case for the collector as well.
Alexander Schwartz (IBM) 01:00:06 if I'm running the collector on a… as a sidecar, and then scraping metrics from it.
Perk (Marcin Stożek) | Elastic Ingest 01:00:12 No, no, no, as a gateway that is run.
tristan 01:00:14 Deployment, or Demon said, deployment.
Perk (Marcin Stożek) | Elastic Ingest 01:00:16 Or if you want to. Yeah, yeah.
Alexander Schwartz (IBM) 01:00:19 Okay, yeah, okay, well, maybe that's another thing, another topic for another call, but at least that's where I have the questions, what I can trust.
Perk (Marcin Stożek) | Elastic Ingest 01:00:25 Sure, sure. But it's definitely doable. Also, you can actually configure a collector to scrape the metrics just like you would with Prometheus.
But, yeah.
Alexander Schwartz (IBM) 01:00:35 Yeah, okay, yeah, scraping works, that's fine, but then it's all about… it's also about blogs eventually, and it's also about, The traces, and then you might… Need to figure out what to filter or sanitize in what kind of way.
Juliano Costa | Datadog 01:00:55 We are getting out of time, We do have two questions, maybe we… so, like, anything that you would like to… let's try to wrap up the 9 and 10. Anything you like about OTAL, and you would like to add to our… or anything you would like to add to this post?
URL.
Alexander Schwartz (IBM) 01:01:17 Crocus are doing, like, a lot of developer experience, great developer experience for Java developers. Let's emphasize that at the very beginning as well.
Because they kind of integrate. You can spin up a Java application and the developer tools of Quarkus.
And they will spin up, for example, a Grafana instance, a KeyClock instance.
For the application developer to have really, like, getting you They're in the first wave.
So that's what I want to add at the beginning.
That's all.
Come on.
Juliano Costa | Datadog 01:01:54 Awesome.
tristan 01:01:58 Awesome. Quick question.
Here we go. I'm sorry if you addressed this earlier. Were you using open tracing from Quarkus before switching to OpenTelemetry?
Or was that not yours?
Alexander Schwartz (IBM) 01:02:13 No, no. Okay.
We used the OpenTelemetry… well, we used the OpenTelemetry agent before switching to OpenTelemetry Tracing and Quarkus.
tristan 01:02:22 But you didn't use… Yeah, tracing at all before that, okay.
Johanna Öjeling 01:02:29 And I have one more question. Do you have any resources you would be willing to share, like architecture diagrams or configuration methods that we could include in the blog post?
Alexander Schwartz (IBM) 01:02:44 Yeah, I shared two links. One is the tracing one, and the other one is the open telemetry. Those would be the most central ones.
Diagram-wise, I can have a look at previous presentation we had on the topic.
I'll leave that as a to-do with me.
And I'll share the slides.
Johanna Öjeling 01:03:05 Yep, thank you.
Juliano Costa | Datadog 01:03:06 Bob.
I'm totally fine if you need to go, but I want to ask the last one, because I think it's important. Any tips from.
Alexander Schwartz (IBM) 01:03:13 I have another hyphenol.
Juliano Costa | Datadog 01:03:14 other…
Alexander Schwartz (IBM) 01:03:15 Let me… yeah, somebody talking in my door will be back.
Juliano Costa | Datadog 01:03:18 Yep.
Alexander Schwartz (IBM) 01:03:24 Okay, I'm back.
Juliano Costa | Datadog 01:03:26 Thank you.
Any tips for any other project maintainers that would think about integrating OTAL into their projects.
Martin Bartos 01:03:39 I would say, maybe thinking about, integrating the full open telemetry stack, you know, even for the logs, metrics, tracing, advance, let's say, because we were in the situation that in the beginning, you know, we just provided the logs, right? Then the metrics, then switching to open telemetry traces, right? And right now, when we are trying to aggregate it together, you know, we just need to generalize it somehow.
you know, have some better mechanism how to connect them. So, thinking about the full picture of the observability, not individual parts.
Let's see.
Juliano Costa | Datadog 01:04:27 Awesome, thank you.
Alexander Schwartz (IBM) 01:04:29 Yeah, and journey-wise, as I think, observable metrics add a lot of value in the beginning.
And eventually, you want to get to traces.
At least for us, it was this way.
Nope. Nothing to add there.
Juliano Costa | Datadog 01:04:51 Awesome.
Awesome. Yeah, that was really cool. Really appreciate the time and all the answers.
We… Perk (Marcin Stożek) | Elastic Ingest 01:05:01 rates.
Juliano Costa | Datadog 01:05:03 We have just one extra request, but that will come later. Whenever we have the draft, we will request your review on that, and then once we get the approval, we move on to the… OpenTelancer.io blog.
Alexander Schwartz (IBM) 01:05:21 It's always to have Good to have some cross-promotion, within the CNCF.
And with other projects in general.
Yeah, at the moment, it's just one blip on a… on those big lists of things that support OpenTelemetry, that's where KeithLock is already listed. Great to see this blog post upcoming.
Juliano Costa | Datadog 01:05:42 Awesome.
Thanks again.
Perk (Marcin Stożek) | Elastic Ingest 01:05:44 Sure.
Martin Bartos 01:05:47 Very much.
Perk (Marcin Stożek) | Elastic Ingest 01:05:48 Yes.
Johanna Öjeling 01:05:49 Thanks so much.
Alexander Schwartz (IBM) 01:05:49 You bet. Bye-bye.
Perk (Marcin Stożek) | Elastic Ingest 01:05:51 Have a great day.
Juliano Costa | Datadog 01:05:53 Right.
