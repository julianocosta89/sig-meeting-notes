SIG: .NET SDK SIG
Date: 2026-08-04
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Martin Costello (Raintank, Inc. – Grafana Labs)** 00:47 Hey.
**Matthew Hensley** 00:51 Hello!
**Martin Costello (Raintank, Inc. – Grafana Labs)** 00:57 To get the car stuff also sorted?
**Matthew Hensley** 01:04 What was that? You, cut out a little bit.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 01:07 Oh, I said, did you get all the car stuff sorted?
**Matthew Hensley** 01:10 Yes, yes. Luckily… It was the smoothest day emergency could go, so… Problem solved.
**Alan West** 01:24 Smooth days.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 01:28 Yeah.
**Alan West** 01:29 Ayo.
It might just be us, since, Raj says he couldn't make it.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 01:44 Oh, I'd missed that.
**Alan West** 01:52 I'll just say up front, I'm… sorry, it's taken me so long to get to your other two PRs, the probable… probabilistic?
Samplers.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 02:03 Yes, that they're stolen you.
**Alan West** 02:04 it is still on, my radar. I'm gonna try to get to that today or tomorrow.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 02:10 Okay, cool, no problem.
**Alan West** 02:13 And then there was that, that, database one, too.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 02:18 Oh yeah, yeah, which I stupidly accidentally closed as well.
Oh, but…
**Alan West** 02:23 Have you reopened it?
**Martin Costello (Raintank, Inc. – Grafana Labs)** 02:24 Yeah, it's re… it's reopened now, but
**Alan West** 02:27 Yeah, yeah.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 02:27 I was deleting a load of old branches, and I thought I'd… Picked the right ones to keep, but clearly failed.
**Alan West** 02:36 Cool.
And then did Steve's get merged? I actually didn't pay attention.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 02:45 The scaffolding one has… I think there's just… there's two reviews on the declarative config one. I think there's just one comment from you.
that you need to check you're happy with, and then I think that's ready to merge.
**Alan West** 03:04 I think my comment on that, I'm forgetting what it was, but it wasn't… things to do. Good blocking.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 03:12 alpha, beta…
**Alan West** 03:14 Oh, yeah. That's what it was.
Yeah, I didn't really necessarily see that as blocking, I was just, like, there was a discussion on there about, like.
when to release it, and whatnot.
And I guess maybe I was more intending to pose a question, like.
would it be so bad if this were released? It's a brand new package, you know, just so long as we can… You know.
make it an alpha and whatever, it's not like… I wouldn't anticipate a whole lot of use from the package, at least at this point in time.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 03:51 If we bundled it… like, we could make it an alpha bundled under core unstable, but there's currently some stuff we're already shipping under the unstable tag that's beta-ish.
So, potentially make those things kind of go backwards, even though they're the same level of quality.
**Alan West** 04:13 I gotcha, yeah, so that's the thing, that's the thing that I wasn't quite remembering, whether they're like that.
the Mintag version, Core Unstable, was basically coupled with… You know, beta versus alpha versus, like, whatever.
I…
**Martin Costello (Raintank, Inc. – Grafana Labs)** 04:28 I guess… Technically, it's not if we don't have anything in the works.
But there was some stuff for the environment variable carrier in the last release that was under beta.
for that.
So I think that would sort of… that's the… I think that's the only fly in the ointment there.
**Alan West** 04:48 Gotcha. Yeah, if that's… if that's the case, then… Then we probably… we'll probably ultimately will need another… Separate, like, kind of alpha channel, essentially.
Thanks, because I would anticipate the declarative config to… be still in alpha for at least some time now, right?
**Martin Costello (Raintank, Inc. – Grafana Labs)** 05:12 Yeah, yeah, I think the proposal to start with was to give it its own… prefix?
**Alan West** 05:19 Yeah.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 05:20 So it's just for declarity config, and then when it's a bit further along, we can decide where to move it to.
**Alan West** 05:27 Yeah, that makes sense, that makes sense.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 05:34 So the only thing I put on the agenda is… I've written a… currently using a Grafana Google Doc, but I've been working on a blog post about how you can use the new Prometheus Exporter to, Sort of dual export.
to Prometheus and OTLP at the same time, so you could do, like, a migration.
And I want to put it on the hotel blog, but I only looked today what the process to actually do that was, because I've looked at it before.
**Alan West** 06:04 Hmm.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 06:04 And assuming the process is the same for everyone.
And it's… and you don't get, like, a preferential treatment if you're a maintainer. It says you have to get someone else in the, like, the, quote, target SIG.
to look at it, so… I haven't yet put it in a form where anyone outside Grafana can look at it, but, would you be willing to, like, give it a review, other than sponsor it?
**Alan West** 06:31 Sure, yeah. What's the requirement? So, like, so, oh, so you're saying the target SIG is the .NET SIG?
**Martin Costello (Raintank, Inc. – Grafana Labs)** 06:38 Yeah.
**Alan West** 06:38 In that way, and you're basically looking for somebody, not Grafana, to, like…
**Martin Costello (Raintank, Inc. – Grafana Labs)** 06:43 Yeah, essentially, yeah.
**Alan West** 06:44 Take it over. Sure. Yeah, yeah, sure.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 06:46 It… it… I think… I think… modulo, you know, font sizes and stuff, it's, like, one page.
It's mostly just… sort of pimping out the fact that the Prometheus exporter is now, like, more spec compliant.
So that you could… you can, like, safely use it to do stuff. Whereas, I think for the last 2 years, it's just been a bit bitty.
**Alan West** 07:09 Yeah.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 07:12 So, it shouldn't be too in-depth, but, but yeah, thanks. I'll, I'll stick it into a GitGist.
And, send it your way, and then I'll open an issue up and tag you on it. Because, yeah, it says, like, you have to create an issue in the blog repo first.
**Alan West** 07:30 Got it.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 07:31 And then you can do the PR to add the content, so yeah. I'll stick it in the gist so you can check it over and be happy with it. Or at least happy with it enough that, yeah, it sounds like something sensible to talk about.
And then I can do all the rest of the work.
**Alan West** 07:47 Sounds good.
Did I hear you right? That the focus of the post is about… OTLP and… Old school, like Prometheus?
**Martin Costello (Raintank, Inc. – Grafana Labs)** 07:56 Yeah, yeah, the idea is kind of trying to… describe the use case. If you're using Prometheus and you wanted to move over to OTEL, now it's gone… now it's graduated.
you can use the OTel Prometheus exporter and the OTLP exporter in the same app, and send your data off to two backends at the same time.
While you're, like, mulling over your migration.
or if you wanted to stick with Prometheus for metrics, but then add on OTLP traces and logging.
you can use just the OTEM SDK and get all of that.
without having to, like, do two sets of telemetry libraries, if you wanted to use, like, the Prometheus client.
**Alan West** 08:42 Right, right.
Cool, okay.
Sounds good.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 08:49 And let me just… I'll just get up the… to the dashboards.
And… I'm on share.
My typical thing where I've got too many tabs open and then I can't tell which one's wrong.
And then… get a stored.
So… go ahead… So… or the SDK repo… There's a couple of… So I've been trying to chase, some test flakiness in the Prometheus tests. I had one PR merge today, there's another one that I think hopefully fixed the problem. It's… Usual thing with, Flaky tests, as soon as you try and fix them, they keep passing, and then you think you fix them, and then as soon as you manage it, one fails.
Also, there's a PR… Actually, this one might be worth a quick discussion point.
So there was a change I made to the Prometheus exporter from some performance stress testing, where I found that it couldn't do more than 100,000 metric series.
Only occurred to me this morning.
Maybe OTLP has a similar problem?
I mean, it turns out it does.
But it's not as bad. It can, like, only do about $300,000 to 400,000, and then it hits, like, a hard-coded limit, and you can't do anymore.
So, I've opened a PR to resolve that.
excuse me, through, like, a new option, but on reflection.
All you can really do with the option is go up to double what the default was.
So I'm wondering if it's worth having the option and instead just Increasing how far it'll go up to internally.
Like, allow it to go bigger than the previous limit.
But only up to as far as would practically work.
Because the range of configurable values is quite small.
**Alan West** 11:09 So 256.
Is the… is the largest.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 11:14 Yeah, I had Claude do some experimentation with it, and because of the way the values are encoded, I think when it gets up to somewhere a bit it's either exactly or just beyond 256MB, then it can't actually store bigger numbers anymore, because the OTLP encoding isn't large enough.
to go bigger anyway?
**Alan West** 11:39 Interesting.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 11:40 So, and I did… I did look into… well, sorry, I looked into it, I asked Claude… Claude to look into it, like.
Could we change things to undo that change? It was basically, like, a whole bunch of changes here and there to, like, change how the values got encoded.
I figured that was a problem for later, if ever.
So…
**Alan West** 12:02 Where's… where's the main, like… bottleneck? Is it… is it, like.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 12:07 to be concerned.
**Alan West** 12:07 Or is it…
**Martin Costello (Raintank, Inc. – Grafana Labs)** 12:09 So, the bottleneck here is… let me find the file… it's literally that constant.
**Alan West** 12:19 Oh, we had something to find before in my memory.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 12:24 So it would… it would start just south of a megabyte.
And do, like, a doubling thing.
But once it got to 100MB, it would stop.
**Alan West** 12:36 I see. So this was introduced, likely, as part of… Raj did the work to… Hand roll.
The protobuf serialization.
Before, we were using, just the… regular protobuf library from Google.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 13:00 Because there was a similar constant like this in the Prometheus Exporter, but that one had a comment next to it that said, like, maybe we should make this configurable one day.
**Alan West** 13:09 And the Prometheus exporter was also… developed by a member of Raj's team.
So there's probably some, like… Yeah. Shared.
knowledge there.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 13:26 Because the… the thing… the thing that came up in the Prometheus investigation, which applies to this one as well, is, like, the 100MB is also a bit of a wasteful cap, because… because it does the doubling.
You effectively just end up with, like, 28 meg left over.
that don't get used. So, like, you've allocated it, and then you've gone, oh, it's too big.
So, this change does what the Prometheus Exporter does, which is, like, ups the default to 128, so it's, like, aligned on a power of 2.
And then… through experimentation, you can go up to 256, and then it won't work for different reasons.
But, so yeah, it's just whether or not we actually need the configurability, because… Because there's not actually much… Many values you can actually give.
the property.
within the range of the flexibility. I just wondered if maybe instead it just internally will go up as high as it can, if needed.
And then it will stop.
**Alan West** 14:41 Yeah.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 14:41 That was the end question I had on this PR.
**Alan West** 14:46 Have we run into… well, I guess… with… in the context of Prometheus, did… A customer run into this, or a end user?
**Martin Costello (Raintank, Inc. – Grafana Labs)** 14:54 So, in Prometheus, the way it came about is I asked someone internally who works on Prometheus.
If they had, like, a good, sort of, finger-in-the-air number to target to write, like, a stress… benchmark.
And they said.
quite in quotes millions, because, Cube… I've forgotten the name now, it's like… there's a Kubernetes… tool that can… CubeSat metrics?
State metrics, something like that. And that generates, like, millions of metrics.
**Alan West** 15:29 Gotcha.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 15:29 So they said that was, like, a good benchmark to, like, for an extreme case.
And when I tested that out, that discovered that you couldn't go beyond about 100,000 because of the hard-coded limit that was arbitrary and internal.
So then off the back of that, I was like, oh, maybe there's a similar limitation that's arbitrary in OTLP, and it turns out there was.
**Alan West** 15:55 Yup.
Makes sense.
Yeah, so with respect to the configuration, it is… I mean, one.
That would have to go through the SPAC.
And… my… Finger-in-the-wind guess of how that would go is that it wouldn't.
I don't…
**Martin Costello (Raintank, Inc. – Grafana Labs)** 16:18 Oh, I assumed it would be outside of the spec, because it was an implementation detail.
**Alan West** 16:23 Yeah, well, that's the thing. It's an implementation detail, but we'd be exposing it as, like, an OTLP configuration option, which is governed by the spec.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 16:33 No, I ju… I just added a property to the exporter options, like HTTP Client Factory and things like that.
**Alan West** 16:43 Yeah, HD… yeah, okay, so there's a little bit of an asterisk, I guess, next to my statement.
Based off of just… our previous history as a SIG.
The HTTP client factory… is something that was introduced to the OTLP exporter, A number of years ago.
And… at that time, I kind of hemmed and hawed whether we really should do that.
And… With the momentum, we just let it slip in.
And I don't think it's necessarily a terrible thing. The HTTP Client Factory is just, like, this, like, escape hatch.
To basically enable you to do… Whatever.
And I think that there are some other SIGs that have… Followed a similar thing.
But… I think that we should be… We should consider that.
kind of a… an exception.
And not necessarily… A new norm to just kind of create implementation.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 17:57 Well, I guess that kind of… answers the question, if it's, like, if it's… if there's not much range in how configurable you can make it.
And then it gets into this grey area of, is it a hotel setting or not?
I could just change it to remove the setting.
And just go up to the number we know it'll fall over at.
**Alan West** 18:21 Right.
And with respect to Prometheus, did you… was the 256 megabyte?
Large enough.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 18:32 So, on that one, I think when I set it to… yeah, I set it to int max value.
And it got up to something like 2 million metrics, at which point it hit the ceiling of how big an array can be.
**Alan West** 18:49 Okay.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 18:50 So, Rebecca basically hit the in32.net limit.
Whereas this… this one hits a different internal constraint.
**Alan West** 19:01 Interesting. Okay, okay.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 19:04 So, I guess… On the one hand.
it could potentially use a little bit more memory if you hit the 100MB limit than before, but previously, if you hit the limit, it would just… At that point, you'd have accrued so many metrics.
That you wouldn't be able to export anymore anyway.
**Alan West** 19:26 Hmm.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 19:28 So, it just moved… so, I guess… On the one… for some users, it'll just mean instead of you suddenly having too many metrics.
You can keep going.
And then on the other hand, it might have been, you were dropping metrics, but now it turned out, actually, you were 2… you were 2 kilobytes away from your memory limit, and now it ooms.
But yeah, I guess it… I guess, what I should do, at least for now, is change the PR just to remove the setting.
And expand how far it… how far it can go if you're a really big metrics user.
And then see where we go from there.
**Alan West** 20:13 Yeah, and what does that actually… so… so by making it bigger, it's… Maybe you already said this, but does that mean more allocation up front somewhere?
**Martin Costello (Raintank, Inc. – Grafana Labs)** 20:22 No, it just means that when it's doing the doubling, It'll do one more.
**Alan West** 20:29 Okay, that's right, that's what… you did already say that, yeah.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 20:33 Yeah, so it's like, I asked it to just see how far you could go.
And… the current version in Maine.
Is you can get up to, like, 390,000 and 1.8 million.
And then, with being able to go up to 256, it doubles.
And that's about… and that's pretty much this little re-rated.
**Alan West** 21:02 it seems reasonable to me to just up the limit. I'd… I'd… be curious to get Raj's input, because, again, he's the one that did the hand-rolled serialization, so I don't know if there was, like, deeper… Reasoning that he had… he had for choosing the limit that he chose.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 21:21 Yeah, it's just because it was exactly the same as the Prometheus one, and that one had a comment on it that was just sort of a 100MB?
**Alan West** 21:29 Yeah. Yeah, fair enough.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 21:31 But, yeah, I'll put that back into draft, I'll make those changes tomorrow, and see what other people think.
**Alan West** 21:38 Cool. And then, yeah, all this, like, just makes me mildly curious about, like, what… the OTLP exporter… how the OTLP exporter behaved, Prior to the hand-rolled serialization.
There had to have been probably some similar, like, limits somewhere.
I'd imagine.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 21:58 Hmm.
**Alan West** 21:59 with, with the Google protobuf.
library, but… I'd guess that it was probably somewhat different in nature.
I'm not suggesting that you go and, like, run that down. I'm just… again, mild curiosity, I'm just…
**Martin Costello (Raintank, Inc. – Grafana Labs)** 22:34 Yep.
There you go.
**Alan West** 22:39 Alright.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 22:42 Science breaking up a… Miami.
**Alan West** 22:46 Oh yeah, you're breaking up a little bit.
No worries.
Okay.
Anything else?
Oh, you might still be breaking up.
Or maybe it's me. Can other people hear me?
**Matthew Hensley** 23:21 I can hear you.
**Alan West** 23:22 Okay.
That must be Martin.
While we're waiting for Martin.
Did y'all have other topics?
I didn't actually ever pull up the agenda.
**Matthew Hensley** 24:15 I don't have anything… Really, just working through a whole backlog of stuff and instrumentation to fix up.
Lots of small errors.
And then I caught up some of the schema experimentation using the Weaver schema.
Wrote up some for the SQL client instrumentation process in Redis.
Hopefully… Later this week or next week, I'm gonna start seeing what it looks like to generate docs and maybe have nice tables and READMEs of what telemetry library emits.
**Alan West** 24:55 That's cool. And yeah, Weaver helps you out with all that?
**Matthew Hensley** 24:58 Yeah, it has decent tooling and a schema format, so all of SimCom is in there.
I'll drop one in the CNCF.net channel, a link, just so you can see the diff.
It's, definitely… Need some polish.
But, yeah, if, now that semantic conventions are starting to be federated, there's a pretty robust set of tools now, because, like, I don't know if you saw, but GenAI split off into a separate registry.
**Alan West** 25:30 Yes, yes.
**Matthew Hensley** 25:32 So, that's been driving lots of improvements very quickly.
And there's gonna be some other registries, so… Hoping to get it to cover instrumentation also, and… Yeah, that'll be… Very convenient, if we can figure it out.
**Alan West** 25:50 Cool, yeah, yeah, yeah.
I think I'm in some automated documentation.
That actually shows what instrumentation produces would be phenomenal.
**Matthew Hensley** 26:00 Martin just messaged me, the weather in the UK has, Besides it's not cooperative with a warm laptop.
I think he's gotten thermal throttled enough that, like, it shut down.
**Alan West** 26:14 Shit. Wow.
The heat wave must have come back, huh?
**Matthew Hensley** 26:19 Yeah… Leica AC.
It's, not stuff I tend to think about, but… Yeah.
**Alan West** 26:32 Belt.
**Matthew Hensley** 26:33 I'll drop a link to the, kind of, my current progress, but it's definitely not done.
But it's… it's starting to look like something reasonable, so…
**Alan West** 26:45 Nice, yeah, cool.
Love to take a look.
Alright, well, doesn't sound like Martin's gonna come back. I don't have anything else, personally.
But… It's good catching up.
**Matthew Hensley** 27:07 Alrighty.
**Alan West** 27:09 See y'all next week.
**Matthew Hensley** 27:10 See?
