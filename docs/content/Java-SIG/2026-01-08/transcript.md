SIG: Java SIG
Date: 2026-01-08
Duration: 61 minutes
Zoom Recording URL: https://zoom.us/rec/share/93tGmDeiLNW9KHD9Ax65ysE-7qaD60nFQetlFgnTAVy69OJOmc3ZEWxJDtGnBCET.X7UNfacKLAWKKnz2
============================================================

## Zoom Recording Transcript

Bruno Baptista 00:00:27 Hello.
Trask Stalnaker 00:01:10 Happy New Year, early birds.
Jason Plumb 00:01:15 Happy New Year, Trask!
Look at all this sun we have outside, it's weird!
Trask Stalnaker 00:01:26 I see blue sky, but I see no sun yet.
Jason Plumb 00:01:30 I had sun earlier.
John Watson 00:01:31 Yeah, just wait. It'll probably…
Trask Stalnaker 00:01:33 We've got a hill, yeah, we've got a hill here.
Jason Plumb 00:01:35 God.
John Watson 00:01:38 Yeah, just wait, it'll dump another inch on us, and then, you know, soon enough.
Jason Plumb 00:01:41 It definitely will.
GZ Gregor Zeitlinger 00:01:47 Happy New Year!
Trask Stalnaker 00:01:51 Give me a… Let's get going. Bruno, you wanna share?
Bruno Baptista 00:02:52 Hey, yes, are you hearing me?
Jason Plumb 00:02:55 Yep.
Trask Stalnaker 00:02:56 Yes.
Bruno Baptista 00:02:57 Cool. So… So I'm gonna share a presentation that I created, Based on our… On a work, long-running work that we've been doing on my team.
So… So this is basically the performance impact.
of, telemetry frameworks on Quarkus.
And so this has been done by… by me, by Luis Pereir from the performance team, and… Ben Evans, that most of you might know, and also Francesco Nero, which is the… the performance wizard in… In the group.
And so, I'm gonna talk… talk to you the… the baseline for… the tests that we did, and how we collect the results, the runs that we did, and some conclusions.
So, and the initial purpose was to… capture the impact of observability, in the user experience when using a Java framework. So, and this is under high load.
So the idea is to stress the system to the maximum, and understand, on those conditions, what's the performance impact of telemetry.
And so this… this was done on Quarkus, and So, let's… let's get the result. So… So, this is the profile of one test that we do.
So, on the top, we can see the… The latency of the requests over time.
So, the… the green part is the ramp-up.
Where we increase the request from 0 to, in this case, 6,000 requests per second.
And… and then we measure the… the overall results that I'm going to present on the main phase, in blue here, where everything is already stabilized. And, Since recently, we started also to measure the first request, just the first request, to see how long it takes to Start the app and serve something to the user.
Yeah, and the bottom… is the more juicy part. So, these are the percentiles of the response… the response times of… for all the requests.
So basically, 100% is the… all the response time, so the maximum in here was 100 milliseconds, around 100 milliseconds.
And all the requests took less than that.
Yeah.
So, this is for one test, and on each test run, we do four of them.
So, we tested, for the same code, for the same conditions, we tested micrometer.
micrometer press plus open telemetry.
we, also measured the baseline, so no observability at all, and also with the OpenTelempty Java agent.
So, some, some, some e… something that I need to clarify. So, Quarkus metrics, automatic metrics, are implemented in micrometer since a very long time ago. And to have metrics on the OpenTelemetry Sorry.
We basically use the instrumentation that is available on the OpenTelemetry instrumentation for Micromotor. So, this is basically a bridge that implements a micrometer registry with the OpenTelemetry SDK. So, in practice, this is… The results follow the semantic conventions of a micrometer, but it uses OpenTelemetry Most of the time.
On the cycles. And, yeah. So, this makes the app, outputs equivalent metrics And, traces, both for the extension.
on Quarkus, and when using the OpenTelemic Java agent.
Yeah. Of course, when we use the Java agent, it's like observability off, so no extension, observability extension is active.
So, and, so based on the… the graph from before, so we have a bunch of requests with, latency here, and… So you can see that we do a… For each run, on this case, around 1.8 million requests.
And this is the… those… these are the main percentiles that we, that we collect, so the 50th to the 99.99.
And… for the results that I'm presenting here, and that I will present, we do 3 consecutive runs, because there's quite a variance from run to run, so we average the results here.
And everything is in milliseconds.
So, So, one important thing to keep in attention is that the mean means nothing here, because these results follow a Poisson distribution, not a normal distribution, as you can see in this curve, so this is an exponential thing.
So, the mean… means nothing. So, what is really important here is the median.
And, well, the… the… higher percentiles. I find on my, my tests that… The two top percentiles are very noisy.
And there's quite some fluctuation from, I don't know, C2 compiling, garbage collection that takes a bit longer here and there. Even with all the precautions that we take on the environments to be as less noisy as possible, we still have some noise.
Okay, then, if we take the previous results, so what we see here, and we place it on a graph.
For the percentiles, and with, logarithmic scale, so it's 1, 10, 100 here, so we can better understand what, what's going on here.
And what we are seeing here is that a particular test condition, so… The graphs that I've shown you is for a particular… the response to a particular REST endpoint, which does GET of a list.
That has, A list of items that is randomly chosen.
from the database, but we also do posts in parallel, so there's posts and GETs, but we only measure the gets. Well, we have to stick with something.
And in this case, yes, John?
John Watson 00:10:04 Do you… so the off, does that mean no instrumentation of any kind?
Bruno Baptista 00:10:09 Exactly.
John Watson 00:10:11 Okay, that's strange that that's slower than micrometer.
Bruno Baptista 00:10:16 Yes. I was going to talk about that. Okay.
Yeah.
And, So this, this is doing one, 1,500, post request requests per second, and 6,000 GETs per second on that list.
This is the particular carcass version. So, 0.1 means that we are doing a 10% sample of the traces.
We are using stock garbage collection and 124MB, so 1GB of RAM.
Basically.
So, and when we do that.
We can see that, as expected, the agent and the extension take longer to respond.
And, well, if you see here the yellow, off, is… when things… are well-behaved, it's… it resp… it replies in less time.
However, when we have noise, things, well, can go a bit random for one or the other, but That happens on the noisy part of the app. So, and we have also two inflection points here. So, the first inflection point here is around 90. This is where the applications start to struggle.
And there's a second inflection point around, well, when… that converges to the maximum response time. And we can say that after this inflection point, things start to behave not very consistently.
and that this app is struggling, actually. We should reduce the throughput so it behaves properly, because it should have a more linear profile until the 99th percentile, at least, if we want to have good performance on the application running in production. So this app is struggling, that's why we see that micrometer taking less time, but It's just the maximum, for some reason.
Sometimes, more time More work changes the way the scheduling is done on the processor, and you get weird things.
Okay.
So, what's the context of this? So, some of it I already explained, so this app has two endpoints. It uses Quarkus micrometer OpenTelemetry extension, which has both frameworks for instrumentation.
And, the agent that we are using here is quite old, but the Quarkus Vernon is also old.
Because, well, this took a long time to collect, and we wanted to keep things stable.
I will be doing something more up-to-date soon. I already have the environment set up, but this requires a lot of runs, and each run takes 40 minutes.
So, yeah.
And so we have these carcasses… Sorry?
Trask Stalnaker 00:13:36 On that last slide, what do you mean by marked stable, but instrumentations are not?
Bruno Baptista 00:13:43 It's because some of the instrumentations, well, are still alpha.
on the agent itself. So, the instrumentation that the agent uses.
Trask Stalnaker 00:13:54 That's… not true.
I mean, the agent is marked stable.
I'm not sure what… what you mean by what… What is breaking…
Bruno Baptista 00:14:07 No, it's not about breaking or not, it's the status, so… When we go to the OpenTelemetry instrumentation, and we see all the instrumentations in there that the agent uses, some of them are not stable.
Lauri 00:14:22 You mean that all of them are not stable?
Bruno Baptista 00:14:27 Yeah, yeah, that's what I mean here.
Trask Stalnaker 00:14:31 but the ACTP… but the telemetry… is… like, the HTTP telemetry is stable, I'm not…
Bruno Baptista 00:14:41 Like… Yes.
Jason Plumb 00:14:42 I think the concern is only that there exists an alpha suffix on the artifact. I think that's the only concern.
Trask Stalnaker 00:14:49 Yes. Because there's no API… there's no public API, so I'm not even sure what… what… you mean by stable or not stable when it comes to the Java agent instrumentation?
Jason Plumb 00:15:00 And to Jay's point, it's probably not relevant to performance.
Bruno Baptista 00:15:06 No, it's more the point of view of, So, when… imagine that I have a corporate app that I want to support for 10 years.
those instrumentations are not stable. There's nothing that guarantees in the next version they will Be different, or instrument different methods, or something like that.
Trask Stalnaker 00:15:26 From that point… Is it different in… in what… yeah, I guess that's my question, is what does stable mean to you in that context? Because there's… it… there's no API, so there's no… even concept.
Bruno Baptista 00:15:42 Yeah, it's more the implementation, of instrumentation.
Trask Stalnaker 00:15:48 what does… what does it mean for an implementation to be stable? Like, can't you change internals of something?
Bruno Baptista 00:15:57 Everybody changes.
Trask Stalnaker 00:15:58 Just internals of things.
Bruno Baptista 00:16:02 Yes, the behavior.
Usually, the behavior is maintained.
And if there's a behavior change, there's a… there's a major version, or some dot version that changes.
Trask Stalnaker 00:16:17 Which is exactly what we do.
Lauri 00:16:19 Or, like, HTTP? The only thing that matters is actually the telemetry that they produce.
Trask Stalnaker 00:16:27 Yeah.
Bruno Baptista 00:16:30 Okay, okay.
So… Let me continue.
Trask Stalnaker 00:16:34 Sorry, the reason I call that out is because the micrometer folks keep spreading that FUD.
Fear, uncertainty, and doubt.
And so I'm assuming you got that line from them.
Bruno Baptista 00:16:49 Yeah, but in part, I agree with that.
Trask Stalnaker 00:16:51 I knew it.
Bruno Baptista 00:16:52 But in part, I agree with them.
Trask Stalnaker 00:16:55 But isn't that, like… But that's what I'm trying to ask, is why. Like, it's the behavior, like, the telemetry stability is what matters. And we… specifically, the Java agent takes major version bumps when we do breaking changes to HTTP, telemetry. The next major version bump is going… we're holding off to break database and RPC, telemetry stability. So we are exactly… and that's why the Java agent is marked Stable.
Because we take major version bumps when we make behavioral…
Bruno Baptista 00:17:37 Bro…
Trask Stalnaker 00:17:37 breaking changes.
Bruno Baptista 00:17:39 So, when I do an instrumentation on a library in Quarkus.
I know that I'm not going to change the implementation, unless something, forces me because I found a bug or something.
I don't have that same guarantee in alpha artifacts on the instrumentation project on Open.
Trask Stalnaker 00:17:57 Library instrumentation is different.
than Java agent instrumentation. So what are you talking… are you talking about Java Agent or Library Instrumentation?
Bruno Baptista 00:18:06 The libraries, and because…
Trask Stalnaker 00:18:10 Your bullet here, your bullet here is under Java Agent.
Bruno Baptista 00:18:13 Yeah, because the Java agent does… use… does use instrumentation from the libraries.
Trask Stalnaker 00:18:21 But there's… it doesn't expose any public API, and we guarantee the stability of the telemetry itself. What behavior… what is… what are we breaking in users?
What is a practical example?
Bruno Baptista 00:18:39 Well, from the… from what you said, I would have to come up with examples, but there are a few.
Trask Stalnaker 00:18:50 like…
Bruno Baptista 00:18:52 I don't know, but you know that there has been a few over the time.
Trask Stalnaker 00:19:02 I mean, I'm not saying there's zero, like, there's been a bug, or that, you know, that there's been to minor, you know, something like Twilio, or something that, like, one user uses. Maybe there's been a breaking change, but… our policy is… for that artifact to be stable, and for the telemetry to be stable, and that's exactly why we take major version bumps on the Java agent when we need to do breaking changes.
GZ Gregor Zeitlinger 00:19:36 Do we also have that for configuration options?
Trask Stalnaker 00:19:42 for non-stable.
For stable configuration options, for unstable, for experimental, configuration.
GZ Gregor Zeitlinger 00:19:50 I mean, I'm… If the Java agent uses the library, and the library is unstable, and the library has a configuration option.
I could imagine that we're allowed to do a braking change to those configuration options, but I'm not sure, that's why I'm asking.
Trask Stalnaker 00:20:06 The Java agent configuration is independent. Today, the library instrumentation is only programmatic, right? So there's no correlation there.
You're probably thinking of the future world where… of declarative configuration.
GZ Gregor Zeitlinger 00:20:22 No, I don't have a use case in mind. I just wasn't sure what the rules are in this case.
Trask Stalnaker 00:20:29 the Java agent is its own beast, right? How the sausage is made.
You know, the pieces that bundle inside of that.
don't… matter to end users, right? There's no public API, all that matters is behavior, the telemetry that's emitted.
GZ Gregor Zeitlinger 00:20:49 So configuration options are also, considered, stable.
Trask Stalnaker 00:20:53 Yeah.
Bruno Baptista 00:20:56 Okay, guys, this, this is, obviously, a bit controversial, so…
Trask Stalnaker 00:21:02 I don't think it's controversial, I think…
Bruno Baptista 00:21:05 At least for me. So I suggest that we probably discuss it with more preparation in the future and move on.
Lauri 00:21:15 I guess the main takeaway from this is that adding the alpha suffix wasn't a good idea.
Trask Stalnaker 00:21:24 And also that micrometer continues to… micrometer folks continue to spread this FUD, and it continues to go wide.
And other people keep buying into it.
Because we added the alpha, because, as Laurie said, there's an alpha suffix on it, even… even though, like, it's not on the Java agent.
So why… why don't you believe us when we… the Java agent is marked stable?
Bruno Baptista 00:21:56 Yeah.
Trask Stalnaker 00:21:56 And doesn't expose any alpha APIs.
Bruno Baptista 00:22:00 You're just buying into the micrometer.
Trask Stalnaker 00:22:04 Who cares? You can use… there's… how does that affect users?
Bruno Baptista 00:22:07 I care! How does that affect…
Trask Stalnaker 00:22:10 No, breaking… Stability means you don't break users.
How does it… how does changing an internal API break users.
Bruno Baptista 00:22:27 If the tests, are good enough.
Trask Stalnaker 00:22:33 Have you seen our tests? Have you seen our Java agent test?
Bruno Baptista 00:22:37 Natural them, yes.
Trask Stalnaker 00:22:38 We have a…
Bruno Baptista 00:22:39 But I…
Trask Stalnaker 00:22:40 Brilliant, and they test… they verify every telemetry, every telemetry attribute for every span.
So, we know if… Anything is breaking in the behavior to users.
Bruno Baptista 00:22:54 Right, but it's necessary that those tests pass, and…
Trask Stalnaker 00:22:58 do pass.
Bruno Baptista 00:23:00 Yes, but… Are we sure that all the instrumentations that are marked alpha have tests that are reliable enough?
Trask Stalnaker 00:23:09 Yes, they all are.
Bruno Baptista 00:23:12 Then good! Then I will remove this.
Trask Stalnaker 00:23:14 Thank you.
Bruno Baptista 00:23:18 Okay, so…
John Watson 00:23:20 I mean, I just want to comment, Bruno, you think it's funny, but this is really serious. Like, there is a.
Bruno Baptista 00:23:25 Well, I know it's serious.
John Watson 00:23:27 I know, but you're kind of laughing, like, it's not a serious thing, but, like, there's a lot of FUD going around about this, and we really need to stop it.
Because it's not true, and they're making users confused, and you, obviously, and you're more than a user, also confused about this. So I think it's pretty serious that we do… Like, in the communication about this, that we are accurate and, like, actually saying things that are correct.
Trask Stalnaker 00:24:03 Bruno, you understand the difference between library instrumentation in the instrumentation repo? The library instrumentation is alpha because it has a public API, right, for people who use it.
And so those are… alpha, and those have public APIs that Can still break.
The Java agent does not have a public API, any public API, other than the telemetry stability, and that's why it is marked stable.
And it is… it is stable.
Bruno Baptista 00:24:46 Okay.
Should… should we continue?
Trask Stalnaker 00:24:51 I'd rather, I mean, we've hit our time box here.
Why don't you come back next week, and let's finish off, because honestly, I know you're… the important thing to you is this performance discussion.
But the important thing to us is that we iron out How, you know, we want to iron out what stability means, and if there's some feedback you can provide to us that would help us to… Explain this better, and document this better.
I'd like to do that.
That is the more important piece to us. Stability is… I don't know if you saw the recent OpenTelemetry blog post.
about stability… stability?
That is really… if somebody could drop that link in chat for, for Bruno.
That is a really…
Bruno Baptista 00:25:46 Critical component.
Trask Stalnaker 00:25:47 The open telemetry.
Bruno Baptista 00:25:50 diagonal, but… So… Probably, there's… not many people that hit the problem of stability in OpenTelemetry as I did.
Because I, I do, library instrumentation with, instrumentation API.
Trask Stalnaker 00:26:13 Yeah, library instrumentation is alpha. You are 100% correct.
Bruno Baptista 00:26:19 And I've… all the changes that you… Everyone has implemented in the, instrumentation API, I had to do the same, but for quarkers everywhere.
And, let's say that has been a lot of work.
And I don't regret it, but it has been a lot of it.
And, I know a few libraries… that I've been using quite a lot from the instrumentation repo.
And… What I can say is that the amount of tests in each of them is very… it's very different from library to library, the depth of the tests.
And… That's… that's probably my main concern.
Trask Stalnaker 00:27:12 What do you mean, the depth of the tests? .
Bruno Baptista 00:27:15 So, how thorough the tests are done on these instrumentations?
Because it's not like we have an SDK, or, sorry, a TCK where, okay, we have to pass this test, and there's a list of tests that we need to pass, and that's fine. So, these instrumentations passed the test that the developers created at the time.
good or bad. Usually people are… try to be thorough, but… Some of the instrumentation libraries have better tests than others.
And I think that's… normal, it shouldn't be… Preposterous.
Trask Stalnaker 00:28:02 So there's some subjective number of tests that you would like to… I'm trying to decide… understand what… how that… like, library instrumentation we fully agree is alpha, right? And we fully agree that there have been A hundred breaking changes.
in those libraries, and we do apologize. We know that they have hit you hard, because you have been, using them.
All I can say on that front is the… the HTTP library ones, actually, I think are… I should… Chuck, I had been trying to get those to actual stable.
And I forget if there's anything… remaining there.
Or if we were just waiting for a version bump to remove deprecated stuff.
I… yeah, I think… Yes, so anyway… one sliver of… hope there.
For you, sorry. .
John Watson 00:29:52 I have a… I have a quick question for Bruno, just before we move on. I asked in chat, you probably didn't see it because you were presenting, what, what exporters do you have configured for this?
Bruno Baptista 00:30:03 So, I'm using the vertex exporters that we created.
not the OTLP, not the ones based on OKHTTP.
John Watson 00:30:17 Okay, so that's interesting. That's probably worth calling out, that you're using a custom exporter and not one of the stock ones.
Just in your presentation. It's probably worth mentioning that.
Bruno Baptista 00:30:29 Okay.
Trask Stalnaker 00:30:30 FX1's not non-allocating.
Bruno Baptista 00:30:36 We basically, piggyback on the… on the private API that is currently available, and we just change the senders.
So all the rest is kind of standard. We use the stock exporter that is available there.
Trask Stalnaker 00:30:58 Does that mean it's the non-allocating?
Bruno Baptista 00:31:02 It's a non- Probably, yes, yes.
Jack Berg 00:31:05 Yeah, it's… At least for… It should be, it should be, yeah, because, he's just, Bruno has just re-implemented the sender SPI.
And, and so, you know, you're still using OTLP HTTP span exporter, or equivalent, and, you know, just the thing that's actually executing the HTTP request is being replaced. And part of what that sender is provided is, you know, a marsh alert, and so the marsh alert is either low allocation or not.
Based on, you know, configuration, which is a higher level than what Bruno's dealing with, so…
Jason Plumb 00:31:40 I asked this in…
Bruno Baptista 00:31:41 Yes.
Lauri 00:31:42 Do you remember when was the low allocation thing enabled by default?
Bruno Baptista 00:31:49 I… we are still using the higher location one on this… on this test.
But the… But the agent is using the default, so it should be using the low occasion one.
Lauri 00:32:05 Yeah, but the version of the agent you're using is.
Bruno Baptista 00:32:09 Quattel.
Lauri 00:32:10 It's fairly old, like, it's more than a year old, so it could also be using the high allocation one.
Jason Plumb 00:32:16 That's what I was getting at with my question in the chat. Same, same question.
Lauri 00:32:21 Anyway, do you just did the measurements, or did you also do some investigation to see, like.
Whether there is anything we could do to improve the performance?
Bruno Baptista 00:32:35 I did.
And… but that's on the other part.
Trask Stalnaker 00:32:40 Since we've spent half the meeting on this, Bruno, do you mind coming back next week?
Bruno Baptista 00:32:46 No, I don't, I don't mind.
Trask Stalnaker 00:32:49 Cool.
Yeah, yeah, no, I'm excited to see the, also the other pieces of it as well.
But we've got other business also.
Gregor…
GZ Gregor Zeitlinger 00:33:09 Yeah, Trask, I saw that you added a point about SDK release, which is scheduled for, This week, do you want to do that first?
So that we have enough time to talk about it.
Trask Stalnaker 00:33:25 Sure, sure.
John, Jack, anything you're… Want to call out or need reviews for…
Jack Berg 00:33:44 I don't think so. Gregor, I'm gonna try to get this PR that we just pushed in the discussion. I'm gonna try to get that merged for the release tomorrow.
GZ Gregor Zeitlinger 00:33:52 Fourth.
Jack Berg 00:33:54 And your Prometheus one as well.
GZ Gregor Zeitlinger 00:33:58 Thanks.
John Watson 00:33:59 Yeah, my time is incredibly limited as I'm starting a new job, and still, I'm not having much hotel time at the moment, so…
Jack Berg 00:34:10 There's one PR, I think, that could use a review. I'm gonna put it in the notes. Sorry, I have a million things open right now.
So this is… Since the last release, we merged changes to update to the latest version of Declarative Config, the RC3, and this is just, like, ironing out, some of the patterns for how we, load component providers.
There was a bit of, you know, drift from you know, plug-in to plug-in, like, samplers, we're enforcing different things than exporters, and so this is just sort of like a refactor and cleanup. And, I guess the reason I care about this is just to have a nice bow on, on our OpenTelemetry configuration, RC3, on that whole implementation.
And John, you reviewed this, I think, a week ago or so, or maybe two at this point, I'm not sure, but I addressed your feedback.
John Watson 00:35:12 Yeah, yeah, I took… I… I took a look. I… as I said, I'm probably not going to have time to dive in any deeper than I have at this point, so someone else… someone else could pick it up, that'd be good.
GZ Gregor Zeitlinger 00:35:23 Yeah, Jack, feel free to ping me, then I can also do reviews.
Jack Berg 00:35:27 Okay, thanks, Gregor.
Trask Stalnaker 00:35:37 I was seeing if hiding white… if there was, still a lot of, looks like a lot of stuff moving around. Okay, cool, cool.
Thanks, Gregor.
Yes, so this… hopefully in the release. Was there anything… I mean, I thought we had approvals… On it, was there anything you wanted to call out?
Gregor, other than…
GZ Gregor Zeitlinger 00:36:08 I wasn't sure if this… there's still something, To be talked about, or if this is good to go now.
Jack Berg 00:36:17 This is good from my perspective, and so I think everybody else has… I think at one point, John had requested changes, but I think he's rescinded that, so, I just haven't gotten around to merging this in the last day or two, so… because I was busy with something else, so yeah, this is good from my perspective.
GZ Gregor Zeitlinger 00:36:35 Okay, cool. Now, I created a separate issue about stabilizing, and how this changes with stability, but… I think it's not urgent to discuss it now.
Jack Berg 00:36:45 Yeah.
Trask Stalnaker 00:36:47 Thanks for opening that spec issue, Gregor.
GZ Gregor Zeitlinger 00:36:53 Yep, thanks.
Trask Stalnaker 00:36:58 Alright, This… okay, so… We have, The traditional way to enable and disable instrumentations in the Java agent has been… our properties to enable and disable. We basically enable and disable the bytecode instrumentation entirely.
With… declarative configuration… Now, we have another option.
That… covers… a lot of the… I mean, I would say, at least… Majority of folks disabling instrumentations are doing so because they're noisy, because they don't want to pay for the telemetry, they don't want to store the telemetry.
As opposed to… There's another group that, you know, are disabling because of maybe more fine-tuned performance or bike code, you know, just, they need to completely disable that bytecode.
So, what I'm… Wondering here is if we can kind of lean into this as our… Default recommendation for people to enable and disable telemetry.
And that would cover… you know, native instrumentation, spring Boot Starter, and Java Agent, And, and Lori called out, you know, we… There still is a very valid reason to want to disable The bike code instrumentation entirely.
It can, you know, some people want to micro-optimize the startup time and, you know, the bytecode. It may have some expensive matchers there.
They may have really large class loaders that Incur, you know, higher startup overhead.
And so… kind of, I guess, what I'm proposing here… what I'm proposing, and Gregor opened in this comment, is… moving the… In declarative configuration, world, moving… the… these properties, which currently are… we've got, like, this fermentation… Common, default, enabled… And… Moving these… to the Java agent.
node.
Jack Berg 00:40:37 So there's kind of two… two handles to enable or disable each instrumentation. There's the, You know, if you're doing it within the… the Java agent block, that is going to You know, enable or disable the bytecode instrumentation altogether.
And if you do it within the scope config blocks within the SDK, then it's like the bytecode is still going to be applied, but, you know, the scopes will be enabled, so everything will be no-ops.
Lauri 00:41:11 I think there are two things, like, If we want to recommend something, like, That, instead of disabling the bytecode instrumentation, users should disable the telemetry, then that is basically a documentation issue.
The way I see it.
And also, Besides the agent, Spring Starter also uses total instrumentation-enabled properties, I think.
Trask Stalnaker 00:41:38 Do we think the Spring Starter needs that Yeah, I guess, so I was thinking for a spring starter, that… this… would be enough, because it doesn't have the problem of bytecode instrumentation.
the startup overhead of bike code instrumentation, the… Problems that can occur, like bugs that can occur.
Lauri 00:42:08 It has the same issues. It has the problems that instrumentations may behave in undesired ways.
Or it may be that the user wants to disable the instrumentation and replace it with a new instrumentation.
Because he needs to modify it.
GZ Gregor Zeitlinger 00:42:29 And startup is also an issue.
Trask Stalnaker 00:42:33 Okay.
GZ Gregor Zeitlinger 00:42:33 I don't have time.
Trask Stalnaker 00:42:36 So… okay. So… What about… Then… Spring Starter… should the… could these be… I guess what I'm kind of… I was trying to get them out of the common area.
Because… In the common area.
It… like, these are feeling more like distro settings to me, of… my distro, I want to include or exclude these instrumentations from my distro.
And when they're… if we're modeling them under instrumentation, Java common… I feel like then we're saying they apply to native instrumentation also, which doesn't really… this seems like a bundling question of whether they're being bundled into a Activated in a distro or not.
GZ Gregor Zeitlinger 00:43:54 But it's not only for distributions. End users also… Use this when troubleshooting.
Or at least I have.
Trask Stalnaker 00:44:06 in the Java agent.
GZ Gregor Zeitlinger 00:44:09 Yep.
Trask Stalnaker 00:44:10 Yeah, sorry, I consider the Java agent a distro.
GZ Gregor Zeitlinger 00:44:14 Yeah, yeah, that's clear, but I understood you that this is for distribution providers to say, for the Microsoft distribution, I want to disable something.
I'm just saying that also end users do it.
Trask Stalnaker 00:44:29 No, no. I meant that it would be under… Under the Java agent… node.
GZ Gregor Zeitlinger 00:44:38 Right, but I was talking about the use case.
Not, how to do it.
Trask Stalnaker 00:44:44 Oh, yeah, yeah, end users definitely use this, yes.
I don't think anybody's…
GZ Gregor Zeitlinger 00:44:52 Then the question is, is it more convenient for users that they can use the same setting both for Java Agent and Spring Starter, or if that would be different settings. If… if that's not a concern, then we also don't need to make At the same setting.
Trask Stalnaker 00:45:16 I don't… See a need for them to be the same?
They have very different lists of instrumentations.
Jack Berg 00:45:28 And they have different mechanics, too, right?
GZ Gregor Zeitlinger 00:45:32 That's also true.
Trask Stalnaker 00:45:56 Alright, I'll leave this comment, and we can kind of… stew on it a little bit more, Gregor.
GZ Gregor Zeitlinger 00:46:05 I'm happy with that.
Trask Stalnaker 00:46:12 I think when we discussed it earlier, we were thinking that this could be useful for… native… Instrumentation path as well.
But after realizing, thinking, remembering about this, this really feels like the… right path for native instrumentation.
For enabling, disabling that.
Jack Berg 00:46:37 But, you know, one counter to that was, like, Trask, the, on the native instrumentation bit. So, the problem with the SDK, you know, scope config options is that, Native instrumentation can't introspect into that.
So, like, if Native Instrumentation wants to disable itself wholesale, not just, like, get a no-op tracer and a no-op meter, you know, it… it's not able to.
Trask Stalnaker 00:47:12 Candid call is enabled on the tracer?
Jack Berg 00:47:16 Not on the… Yeah, I guess I can do that on the tracer, but on, that's not on the meter, because… folks wanted it down at the instrument level, at, like, the, for metrics, and so you have to, like, initialize an instrument, and then check if the instrument is enabled or disabled, and then you're sort of, like, you know, treating that as a heuristic for whether the whole meter is disabled or enabled, so that's kind of weird.
I wish there was, like, a way you could just, like.
ask the API, is this scope enabled or disabled?
Trask Stalnaker 00:48:03 Because, one thing I actually really like about this… Is we've had, we've had multiple requests To be able to disable only tracing and not metrics.
Jack Berg 00:48:20 Right.
Trask Stalnaker 00:48:21 and… Today, our solution, our, the setting disables both.
And so that enables that feature.
Jack Berg 00:48:33 Well, we can go with this and treat this as, like, a future enhancement to, like, so basically, my critique of this is that native instrumentation doesn't have a mechanism to, like, be as performant as possible.
Right? Like…
Trask Stalnaker 00:48:45 No op… no OPI as possible.
Jack Berg 00:48:48 as no OPI as possible. It's still, like, you know, it has to, you know, call… tracer is enabled, it has to, you know, check if instruments are enabled, and it could short-circuit that altogether if there was a better mechanism to check if that scope was enabled or disabled.
So, like, but yeah, we can, we can, we can treat that as a, as, as future work.
Because I do think it is solvable, it's just, like, not solved today.
GZ Gregor Zeitlinger 00:49:23 I mean, the current convention we have, is… is a possible solution to that, Jack. If we just standardized on one one node to look at, and then native instrumentations would also look at that, then it would already work.
Jack Berg 00:49:47 Yeah, but then you get back to Trask's critique about, like, you don't have control over metrics, traces, and logs individually.
Right, so it's just, it's kind of a blunt instrument.
GZ Gregor Zeitlinger 00:49:58 -Oh.
It's not an either-or, you can have both.
Trask Stalnaker 00:50:03 Yeah, but I think that becomes confusing, like, I think the user story is more confusing than why we have both, and then it's not a standard open telemetry thing.
like, I think what Jack is proposing is… If other languages… if this is a real issue for native instrumentation, then we should solve it for other languages as well, in a unified way.
GZ Gregor Zeitlinger 00:50:30 Yeah, we're just kind of saying that we should either put it in… not in the instrumentation part, so in something that is SDK controlled, or just have a semantic convention that applies to all languages.
Trask Stalnaker 00:50:41 Right, right.
Yes, under general, put it under the instrumentation.general, is what you're saying?
GZ Gregor Zeitlinger 00:50:51 Regardless of where, just have something that works across languages.
But you have the same formula.
Trask Stalnaker 00:51:02 I think my main… Objection is just… like, we have this thing that is actually really nice. I'm, excited for this to be rolling out.
And it feels like it is for this purpose.
And so having… Like, I'm trying to, like, not have multiple Different.
Solutions… in OpenTelemetry for the same… problem.
And you could argue, Jack, that native, like, native instrumentations that want to be super perform NOAPI.
should be checking is enabled on the instrument anyway, to get to know if it's been dropped? Like, to opt out of each one if each one has been dropped on an individual level?
Jack Berg 00:52:07 Yeah.
Yeah.
That's true.
So maybe, like, I guess what you're saying is maybe the existing tools are sufficient.
GZ Gregor Zeitlinger 00:52:22 Maybe we just need to document this, somewhere.
S, performance guide or something.
Going full into that, you could also argue that the agent And Spring Starter could also check for those instruments, but that would be a lot of work.
Trask Stalnaker 00:53:23 Yeah, it's… I mean, but it's… it's… yeah.
it's not a bad thing. I mean, it's still, level up below… Disabling the bytecode completely.
GZ Gregor Zeitlinger 00:53:38 No, no, I'm saying have, have both. So, based on the metadata that Jay generated, we could have a mapping of module to, to, spend name or, instrument. And then we would, go to that list, and before loading the bytecode.
we would check for the scopes. So, something that is more fancy, but, we have… All the tuning in place.
Trask Stalnaker 00:54:07 So we'd have to check if tracers and meters… yes, yes, I understand, I see what you're saying.
Now… There's one other factor for Java 8, the propagation.
Right, like, Jack, if you disable… Say you disable OKCTP, tracing… Do you still… you still get context propagation, right?
Jack Berg 00:54:39 Yeah.
Yeah, so, Context propagation is treated as orthogonal. So when you disable a tracer, what's going to happen is, like, when new spans are created that would be children of that span.
they are associated with a parent that, like, you know, was as if that code didn't exist, was as if that, you know, that tracer never existed, so you don't get broken traces. That's to keep it.
But, like, if you imagine an HTTP client that is, like, the okay HTTP instrumentation, and it's got… it's doing two things. It's doing, like, it's creating client spans.
And, it also is doing context propagation. And so, like, you know, in some ways, that's like… it's almost like it's two bits of instrumentation. One to create the spans, and one to do the propagation, and, you know.
you know, it's not like if you… if that OKHTTP instrumentation, if it asks for propagators when it's disabled, the propagators will return a no-op. That's… that's not what happens.
This is, you know, another way to say this is, you know, none of this scope config has any impact on propagation at all.
Lauri 00:55:51 So, if the treasure is disabled for OKHTTP, HTTP client span isn't created, But, The remote service receives some sort of parent span.
Jack Berg 00:56:04 Yeah, and you know, I think in most cases, or I guess it would depend on the context, but that that parent would either be an internal span.
Lauri 00:56:12 Or another server span. So you would have a trace that has a server span as a parent of another server span.
Jack Berg 00:56:20 Yeah, and I don't think that that's, like, wrong on its face.
Maybe it's unexpected, but, like, you know.
Yeah, I guess it's not clear what the correct thing is to do there. Like, is it correct to, like, when you're disabling a tracer, to also disable propagation?
Always. Or, like, you know, does it… does it depend?
GZ Gregor Zeitlinger 00:56:44 At least it would be less surprising if it would be the same as disabling the entire module.
Jack Berg 00:56:53 Yeah. I don't know.
Trask Stalnaker 00:56:53 Oh, I'm not sure. I'm not sure I agree.
Cause… I mean… tracer… like, I feel like this is… I do this to avoid the noisy… spans… But breaking up, breaking trade… breaking context propagation, is, like… The worst case, like, for users.
Lauri 00:57:25 Well… Usually HTTP clients aren't the noisy ones, I guess.
Trask Stalnaker 00:57:30 Yeah.
Probably not a big problem in practice.
We are almost out of time, and heck, you learned OSGI.
Jack Berg 00:57:51 Oh my gosh.
Yeah, I've been banging my head against the OSG eye wall for a day and a half.
But I made progress, and I think, like, I understand the concepts enough to at least be dangerous. So, yeah, like, this is the most popular issue in the core repo right now, so that's kind of the motivation here.
And, you know, also, it's just along the lines of thinking of, like, remove the reasons why people wouldn't use OpenTelemetry Java. And so, I don't know how popular the OSGI community is, but the thumbs up.
suggest that it's, it's, it's non-zero. And so, yeah, we're out of time today, but, like, if you get similar asks to do OSGI in the instrumentation repo.
And I think that is a reasonable follow-up request, at least for library instrumentation. You know, we can… we can share notes, and I can, you know, describe this in more detail, just like the things that are going on, just so hopefully the learning curve isn't as steep as it was for me.
Jason Plumb 00:58:59 I haven't heard an ask since I've been in with Splunk.
Just as a data point.
Jack Berg 00:59:05 That's a data point.
Jason Plumb 00:59:09 I'm not sure if Peter or Lori.
Trask Stalnaker 00:59:10 as…
Jason Plumb 00:59:11 show that, but…
Trask Stalnaker 00:59:13 I can see the SDK being more… I mean, because, like, that's the low level, like, people using OSTI are, like, hardcore, like.
They only want minimum dependencies, they want yeah.
Lauri 00:59:28 They're actually explicit. I actually think they… If you don't have those descriptors, then they can't easily use the library.
That's the problem they're having, but…
Trask Stalnaker 00:59:50 In our last minute, Robert, let's make a call out to… oh, yes, no, we don't have time for this.
Robert Niedziela 01:00:01 Yeah, I think it's too short a time to discuss it.
That weekend. Okay.
take it offline, or continue next, seek.
Jack Berg 01:00:11 Just one thing I would add on this, Robert, is that, we were talking in the spec seg the other day, and, you know.
we're… I think it was just Trask and I from Java that were there, but, like, we're committed to figuring out how to make sure that distributions, like the Splunk distribution you're working on, can access this… this block of the config. So, yeah, like.
even if this spec PR doesn't end up getting merged, we'll find an answer, so…
Robert Niedziela 01:00:39 Yeah, so I'm sure it's doable, probably I know how to do it. I just wanted to somehow, you know, don't leave it as orphan, because all the nodes in YAML have some support in API, and this one will not have the support, it's just hanging. Maybe we should… invent different mechanisms, or maybe not. But I thought that a config provider could be a good candidate for it, obviously.
It's a pleasure.
Trask Stalnaker 01:01:07 Let's talk about it next week. We'll add it to the agenda for next week? We'll get it near the top, and yeah, it's a good topic.
Robert Niedziela 01:01:16 Good.
Trask Stalnaker 01:01:17 Cool.
Alright, thanks all.
Robert Niedziela 01:01:19 Bye.
Trask Stalnaker 01:01:20 a…
Jack Berg 01:01:21 But…
Robert Niedziela 01:01:21 Yo.
Bruno Baptista 01:01:24 But…
