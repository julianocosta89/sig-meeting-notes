SIG: .NET SDK SIG
Date: 2026-07-28
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Martin Costello (Raintank, Inc. – Grafana Labs)** 01:18 Hey.
**Matthew Hensley** 01:21 Hello.
**Alan West** 02:04 Hey, everybody.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 02:07 And…
**Matthew Hensley** 02:08 Hello.
**Alan West** 02:11 How are you?
**Martin Costello (Raintank, Inc. – Grafana Labs)** 02:13 Not bad, thanks.
What about you?
**Alan West** 02:19 Oh, fine.
Weather's cool.
Sunny?
Can't complain.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 02:58 Hey, Raj.
**Alan West** 03:01 Hey, Raj, welcome back.
**Rajkumar Rangaraj** 03:03 Hey, hello everyone. Thank you.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 03:08 I didn't think you were back until next week.
**Rajkumar Rangaraj** 03:10 Oh, yeah, I… I just started yesterday, it was back last week, Friday.
**Alan West** 03:20 Cool, hope you had a good trip.
**Rajkumar Rangaraj** 03:22 Yeah.
Completely out of work.
For some…
**Alan West** 03:25 day.
**Rajkumar Rangaraj** 03:56 Are we waiting on anyone, or should we start?
**Martin Costello (Raintank, Inc. – Grafana Labs)** 04:00 Don't, don't think so.
**Rajkumar Rangaraj** 04:02 Yeah, I couldn't share today because my… like, I came back and my, like, desktop is scattered with a lot of information, so… Someone else could drive your son.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 04:19 Give me a second.
**Alan West** 04:21 You wanna take it, Martin?
**Martin Costello (Raintank, Inc. – Grafana Labs)** 04:32 No.
Closed the down tab, didn't I?
When they are limited by Zoom properly.
So, all there is on the agenda today is, look at the… PRs and issues.
So, you might not have seen this yet, Raj, if you've been away.
**Rajkumar Rangaraj** 05:11 This is interesting, this is nice.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 05:14 So this is something that I think Trask came up with?
And it's a… there's a shared… there's a new shared workflows repo in the OpenTelemetry org.
And I did a PR to onboard us there, and there's some app running in, like, Netify or something, somewhere.
And it listens to webhooks in the org, and then keeps this issue sort of fresh and hydrated.
So I've pinned this to the issues for, main… the SDK and contrary prefo, and then it's just got a list of things we need to look at.
**Rajkumar Rangaraj** 05:53 Awesome, I like the way it's been organized. It reduces a lot of work on us.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 06:00 Yeah, so it's nice, rather than trying to click through and see what there is.
And the age column is handy as well. Although it doesn't sort by age, I think it sorts by when it was last touched.
Or something like that.
So, this one, I think this one's, waiting on you, Raj. Not sure what we want to do with it further. You left a comment on this.
Inc.
**Rajkumar Rangaraj** 06:33 Take a look at this one. I did not get to the, the older… Sure. Issues it.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 06:42 Yeah, I think… I think this one, you left a comment, but the… the PR author hasn't replied since, so I'm not sure what we want to do with it, but it's been hanging around for 3 months now.
This one, I saw, you've approved this, so I'll merge it a bit later on. Thank you Raj. So… I think I mentioned it last week, there was a PR to add Blazor test coverage?
That's been merged now. This one adds Android with an emulator.
Once this is merged.
I'm gonna try with an agent's help to try and add one for iOS as well.
But that might be trickier, given Apple.
But, we've at least now got… some end-to-end coverage for Blazor, which covers the change that got made the other months.
for the OTLP exporter, and then… Android also does some code to do with HTT… HTTP2 for Android apps somewhere in the OTLP exporter as well, so that covers that.
So far, there's been no need to actually change any of the product code.
It's just been increasing the test breaths, so not flashed any… issues out with those yet, but they're very high-level happy path tests. They're not testing everything, so there could still be issues lurking that we've… not seen before.
And then I believe all of these are working, waiting on whoever opened them.
to get back. Actually, this one, and for Raj and Alan.
So, this… this PR Steve opened for the declarative config stuff, it's got some merge conflicts now.
I was happy with it. Piotta had a look at it, but didn't approve it before we went on a holiday. So if someone else could take a look at this and… Be happy with the approach, then we can get this, merged and… Steve can then start working On the declarative config stuff further.
**Alan West** 09:04 Yeah, apologies, I haven't gotten this yet. I was hoping to find some time this week to… Spend on it.
**Rajkumar Rangaraj** 09:11 Yes, same. I'll also spend some time on this week.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 09:15 Okay, cool.
I think… I don't think anything else is worth any specific conversation at the moment, and they will need the original authors to do something on them.
So that's this to carry her.
Then, on… Contrib, so there's another PR here, good to get a plus one from someone. So, Steve's also picked up some work to implement stuff for the dynamic control OTEP.
this PR's just scaffolding and stuff, but if someone else could, be happy with it as well. Then we can merge that, and the scaffolding's then to start implementing other bits and pieces.
**Rajkumar Rangaraj** 10:04 I have some questions related to that one, Martin. Oh, I didn't… actually, I saw up here about that. I did not read the issue or something to it, but it was speaking about some dynamically changing the configuration, I believe. So,
**Martin Costello (Raintank, Inc. – Grafana Labs)** 10:19 Yay.
**Rajkumar Rangaraj** 10:20 You know, what is the goal of this project?
**Martin Costello (Raintank, Inc. – Grafana Labs)** 10:25 So, if I… I've only read the OTEP once, and it was about 2 weeks ago, because I hadn't heard of it until this PR was open.
it's basically… I think it's adjacent to the, op-amp stuff.
And it's about, like, dynamically controlling what the SDK is doing in real time when it's running.
through arbitrary… ways, like, whether you, like, change a file, it calls back to, like, a command or control infrastructure, I can't remember all the specifics, if I'm honest.
**Rajkumar Rangaraj** 11:07 Okay.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 11:08 But it's sort of, like, adjacent to OpAMP, but it's not exactly the same as just reloading configuration.
Because I don't think it's tied specifically to the format of declarative config.
**Rajkumar Rangaraj** 11:22 Okay.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 11:26 So that's that one. There's a bunch of PRs here from me that I don't think are particularly controversial, they just need… Some eyes on… Oh yeah, another one to add to your pile, as you did mention it last week, Alan, I've still got the consistent probability sampler.
**Alan West** 11:51 Pr weight.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 11:52 for reviews, as well, Raj, if you've got time to look at this sometime soon.
This is… implementing… Yeah, this is a bit of the spec.
And… Piazza suggested that initially it went into Conjob into an extensions, and then at a later point, it would move to the SDK.
There's a couple of… Actually, there's a G for one as well.
**Rajkumar Rangaraj** 12:23 Yeah, I saw yesterday Geneva and one collector, somehow I reserved them for today's review.
Oh.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 12:29 Yeah, these are two minor bug fix ones, but this one… I didn't really know the details on that one, so I've left that one.
View… Talked about this one… Not that one. This one last week, discovered that… The lambda… Instrumentation doesn't redact HCB growth strings, so I've implemented… that, following the patterns all the others have done. It's… you can opt out of the environment row, which reminds me, I did say I would look into whether the spec has formalized, the opt-out stuff, and I forgot to look, so I'll look into that.
Tomorrow… Oh, and then… and I've… I've had a quick look at this PR.
If people want to have other opinions. This is at the point of, like, here's a proposal of what's something we could do.
So if people have opinions on this, Someone opened an issue about being able to, like, extend or override how the query reduction works.
And I think the motivation was for non-SQL-like queries.
So there was a chat and an issue about a possible proposal of what could be done, which this PR does for the EF core provider, but then I think in the process of opening this.
the person who opened it went, oh, but it doesn't work with Cosmos at the moment, so that's a different issue, but we already had an issue for that, and we declined to do the support for that.
So I don't know whether that will change this person's motivation for doing this change in the first place, if… We're not gonna actually support Instrumentation for other providers that would actually need the support.
**Alan West** 14:26 What was it, Cosmos?
**Martin Costello (Raintank, Inc. – Grafana Labs)** 14:28 So, in F-Core, when it's not, like, a SQL-ish… provider, the extensibility hooks it goes through in EFCore are, like, completely different, and we don't listen to any of them.
So you get no telemetry.
And then there's an issue somewhere that I opened about that, and then I think we had the discussion about it, and… we went down the path of, well, EF core should just have native instrumentation.
So, we shouldn't have to do a non-trivial amount of work to make it work with other things when EF Corp can just build it in.
I still think there's probably value in Letting people change the sanitizer if they've got some weird bespoke reason to that isn't, just that they're using a provider that the telemetry doesn't work with.
Which is separate to that, but but it does involve having to expose some public API service in the EFCore provider.
**Alan West** 15:38 Right. So, let me just make sure I understood. So the main concern is that you're basically exposing something That is not applicable to all things that the EF Core library might otherwise instrument.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 15:56 I think so, yeah. So I think… I think the motivation for this was the person saw the redaction wouldn't work on, like, JSON queries.
So it was like, rather than… so I suggested, rather than doing a bunch of work internally to make it understand all those things, we could just provide a hook.
And then you could do whatever you wanted to make it work differently.
But then, I think the motivation for him wanting to do that Is actually for something it doesn't do anyway.
So then, his specific use case, having this extensibility, would probably be Not be useful, because the underlying instrumentation that you would use it with isn't there.
**Alan West** 16:41 Okay, I get it, I, okay, I get it now. But I think…
**Martin Costello (Raintank, Inc. – Grafana Labs)** 16:44 there would probably still be value in allowing it to be changed, but I don't know what a concrete use case to want to do that is right now.
**Alan West** 16:53 Yeah, allowing it to be changed was an early consideration of mine when I was originally thinking about this sanitization stuff.
Obviously, I didn't do it.
But… I guess my… My main… Reasoning was, like, if… The sanitizer that we have isn't doing something for somebody, or if maybe it even has a bug, like it's… you know.
exposing secret stuff. If people have a way to override it, we might be less likely to discover that bug.
I don't know, maybe that's a little… Too defensive, but, like… I… I kind of erred towards wanting to… Have, like, a stream of feedback about our sanitizer, and… You know, improve it.
If needed.
I think the one… one use case, that… might be nice for people is to just say, like, I don't want sanitization at all.
For whatever reason, you know, like, that seems risky, but like… just, like, an on or off, but, like, you can change it to anything you want type of thing. I was a little hesitant to…
**Martin Costello (Raintank, Inc. – Grafana Labs)** 18:23 So the way this is implemented at the moment, it's like a nullable property whose default delegate just runs the code we already have today.
So you could turn it off by saying it to null.
But yeah, it's like… I'm not… given that we're not going to support Cosmos, I wonder if the motivation to actually expose it is still there?
But it still might be useful, I just… it's one of those things where I can see why, if you needed to do something, it would be useful, but I can't think what the something could be.
But, the author of the PR hasn't replied to the comment I replied to originally, which was like, oh yeah, we don't support Cosmos, and we're not planning to.
So, I don't know whether that'll change his motivations.
**Alan West** 19:17 Okay.
Okay, yeah, makes sense.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 19:25 Mmm… I think that's… All there is that's worth discussing, unless there's anything that people… sorry, anything that catches someone's eye.
Oh, they've got a different topic they'd like to discuss?
There's nothing on the agenda, so…
**Alan West** 19:50 Nope, nothing on my end. I will try to get eyes on that probability sampler and Steve's PR as well.
This week.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 20:00 Oof.
Anything you need us to catch up on, Raj?
**Rajkumar Rangaraj** 20:06 No, I think I'm good.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 20:11 Anything from Yuma?
**Matthew Hensley** 20:15 Nope, all good.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 20:20 Sure, monitors.
See you next time.
**Alan West** 20:23 You too soon.
