SIG: Kotlin SIG
Date: 2026-11-16
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Jamie Lynch (Palo Alto Networks)** 00:49 Morning.
**Jason Plumb (Splunk Inc.)** 00:50 Hello.
**Jamie Lynch (Palo Alto Networks)** 00:52 That was KubeCon.
I'm assuming you went.
**Jason Plumb (Splunk Inc.)** 00:56 Yeah… yeah, it was good. It was good to see everyone.
The pulse was a little bit quiet this time, it felt like.
there weren't as many people, I think I heard some numbers that it was, like.
significantly diminished. I think there's just a bunch of different reasons why, but… It's interesting.
That's fun.
as fun as Salt Lake City can be, and I'm glad I got out of there before this Ground stop hit, because it did, it did hit some of my colleagues.
who might have made it back, I'm not sure in some cases.
the Monday morning fallout is still very real.
From that travel snafu.
**Jamie Lynch (Palo Alto Networks)** 01:44 Yeah.
I can imagine.
**Jason Plumb (Splunk Inc.)** 01:49 I'm just glad it's not being attributed to a Cisco router.
**Hanson Ho** 01:56 one router that's… not… redundancy, and… A lot of words, it's not.
**Jason Plumb (Splunk Inc.)** 02:05 Yeah, let the conspiracy theories flow rampant now.
**Jamie Lynch (Palo Alto Networks)** 02:17 Cool. I've got to head off in about 25 minutes, so I think I'll just make a start now, and if folks add to the agenda as we go, then we can… Yeah, kind of hopefully cover it within that time.
So yeah, first up was CI caching.
So… I've… put together this PR… That basically tries to enable caching on CI, so… Originally, we disabled this due to… I think Sysmor Scanning, came up with a couple of issues about cache poisoning.
So, I think the long and short of it is we basically just, disabled.
caching entirely on CI, which is… Beginning to cause a bit of pain as the project is getting bigger.
So what I've attempted here… is… I've, made the cache read-only and removed it from the release build, which I think is going to resolve the… Original, like, security warning.
But yeah, I think it would be good if I could get your eyes on this, Jason, and I've tagged Trask on it as well.
**Jason Plumb (Splunk Inc.)** 03:47 Yeah, the idea being that any merge to the main branch will still trigger a build that uses caching.
But when we go to do a release, that's gonna be the slow, full…
**Jamie Lynch (Palo Alto Networks)** 04:00 Yeah.
**Jason Plumb (Splunk Inc.)** 04:01 Full process. That makes sense.
**Jamie Lynch (Palo Alto Networks)** 04:05 Yeah, and hopefully that should just speed things up a bit.
**Jason Plumb (Splunk Inc.)** 04:09 Cool. Yeah, I'll look at it.
**Jamie Lynch (Palo Alto Networks)** 04:11 Awesome. Thank you.
**Jason Plumb (Splunk Inc.)** 04:12 It's real short, I'm looking at it now, and it looks pretty good, so…
**Jamie Lynch (Palo Alto Networks)** 04:19 Cool, and then one more update from me. So, I think the changes to the context API and Propagator's API are pretty much Done for me.
So, I'm gonna ping Carlos. I just want to put together some examples to make it kind of easy to review, and kind of update the docs on how it all works, but I think it… aligns a lot more with what the spec is expecting.
So, I'll try and do that, sometime this week.
Cool. Here we are.
**Ilia Liferov** 05:08 Yeah. Oh, how old?
Just, to let you know that, I'm currently working on gRPC, support for exporting.
And, like, my next step would be to research available gRPC solutions, as we discussed, Jamie, with you in the issue.
to research the available solution for target platforms and SlideQuery. Understand what… what platforms we are going to cover.
the first, and, like, probably some platforms, won't be ready for JRPC yet, so I'll… map out.
Or the results of the research and the issue, and we'll, like, take a look, and… do them. I'll cover the platforms, like, Sequentially.
Yeah, that's… Just to let you know, we… On which issue I'm working on right now, and just to mention that I'm waiting for membership requests to land.
to help you out, on the project, as treasure.
In charge of the role.
**Jamie Lynch (Palo Alto Networks)** 06:28 Go ahead.
Yeah, alright.
**Ilia Liferov** 06:30 basically eat.
From my side.
**Jamie Lynch (Palo Alto Networks)** 06:33 I will… Add an action for me to, chase our membership requests. I think they put them out.
**Ilia Liferov** 06:45 Thank you.
**Jason Plumb (Splunk Inc.)** 06:47 Yeah, let me know if you need seconds on any of that stuff.
Like, if those membership requests are out there and just need, like, a thumbs up, let me know.
**Ilia Liferov** 06:56 Oh, EF.
and if I'm not mistaken… I've mentioned, you and Jamie.
**Jason Plumb (Splunk Inc.)** 07:04 Yeah, I think the challenge is that if… Unless… Unless I've been involved in that PR, I don't know that a mention creates a notification, but also, I'm in notification hell right now, as are some other people, so… It's better just to let us know directly.
**Ilia Liferov** 07:21 Okay, okay, sure, yeah.
**Jason Plumb (Splunk Inc.)** 07:22 Cool.
**Ilia Liferov** 07:23 Okay, yeah, point taken. I will send you a link, directly.
**Jason Plumb (Splunk Inc.)** 07:27 Awesome. Thank you.
**Jamie Lynch (Palo Alto Networks)** 07:29 I will… I'll double-check, because I think there's one other, person who's been contributing as well, so I'll… I'll message you as well, Jason.
**Jason Plumb (Splunk Inc.)** 07:37 Great.
**Ilia Liferov** 07:38 Okay.
**Jamie Lynch (Palo Alto Networks)** 07:42 Okay, Cool. This all sounds great to me in terms of GRPC, I think, just figuring out what the… libraries look like for KMP would probably be a good first step, and then we can figure out where we go from there.
So it sounds like a good approach to me.
**Ilia Liferov** 08:00 Cool.
Thank you.
**Jamie Lynch (Palo Alto Networks)** 08:07 Okay. Jake, Was there anything else?
Was there anything else on that last one, sorry.
Okay, cool.
Jason contributing.
**Jason Plumb (Splunk Inc.)** 08:28 Yeah, this'll be real short. The TLDR is that nobody picked up any of the Android or Kotlin issues. Everybody wanted to work on collector stuff. Shocking, I know. There were some people working on Go, whatever. Once again.
We're the cool kids off in the corner.
So, what I intend to do is the few that I made, I think those top 3, I'll just submit PRs for those, because they're all very simple, like, intentionally like, one-liner is kind of simple. So I'll just… I'll do that. What do we want to do with the two that had closed PRs, and what do we want to do with the rest of them, is the question.
I'm inclined… to just reopen those PRs, and then I'm inclined to remove the ContribVEST labels, And then, Yeah, thank you, Jamie. And then, you know, I think they'll get picked up, probably.
**Jamie Lynch (Palo Alto Networks)** 09:31 Yeah, that feels like a good outcome to me. Okay. And then, if we do want to do ContribVEST for the next KubeCon, we can just kind of pick out some appropriate ones.
**Jason Plumb (Splunk Inc.)** 09:42 Totally. And, I mean, in full disclosure, these top 3, I just had an agent create them. I'm like, find me, like, one-liners, like, easy stuff, and, you know, does a reasonable job.
Cool. I can do that.
**Jamie Lynch (Palo Alto Networks)** 09:55 Okay.
**Hanson Ho** 09:57 Any general updates from KuCon? Like, state of the… state of the project and all that stuff?
**Jason Plumb (Splunk Inc.)** 10:04 Yeah, so… there was a lot of buzz about the fact that OpenTelemetry had graduated, so that happened earlier this year, and there was a celebration around that. We had, like, a graduation party.
And, you know, that helps us get certain status, which I'm… it's too early in the morning for me to remember, or enumerate, like, specifically, like, what or how that helps the project, but it definitely does, at least in terms of marketing, but no, there's… I think there's actually more concrete stuff that… whatever. It's been a long time coming, there's a lot of work that's been put into it, so there's a lot of buzz about that.
There was a surprisingly, there was a lot of talk and buzz about Obi.
And this is from my perspective, so that's the, you know, EVPF instrumentation with some packaging.
And… There's also a little bit of buzz that I was surprised about, about Arrow.
Which is kind of, you know, it's both a, like, a wire format, it's like a columnar… Format that kind of I don't want to say competes with, but is an alternative to OTLP, the… the format kind of coming first dictates how some of the processing on either end operates. Like, you can imagine a column store being a little more stateful and requiring some… Like, some changes or some different processing, and so there's some buzz around that.
The thing that handles Arrow… may not be a collector, so I don't know what that really looks like. I think it's still being figured out what that fully looks like.
And it's still young, but, like, there's a lot of excitement around it, because it's considerably more compact on the wire, and if you write it to disk, then also it's, you know, considerably more space efficient. And there's trade-offs, like, everything. What else?
You know, outside of observability, I didn't really, Go and watch a lot of talks in other, kind of, areas.
You know, it's a huge conference, and there's a lot of tracks, so, like, there's… I don't know, 15 or 20 different tracks?
there's a lot of talks about a lot of different topics, and even the zero-day stuff, like… Observability is, like, one of the things, but there's, like, there's days for everything else, like… OpenTofu, like, has a track, like, a whole day, like, you know, there's… there's a lot of co-located events, and I… you know, I was kind of hands-off on most of that, and focused just on observability.
Let's see… Yeah, nothing, nothing groundbreaking. I mean, also unsurprising.
80% of the talks, 90% of the talks, and probably 90% of all booths have the word AI in them.
or agents, or LLMs, or, you know, something along those lines.
So, we're just gonna keep doing that for a long time, I guess.
But there's, you know, there's always interesting stuff there.
No shortage of it.
**Hanson Ho** 13:23 But no active, hotel, because last… I remember last year, or last one I went to, there was, like, you know, the state of the, project, and there's, like, awards and all that stuff. Like, did all that stuff happen? Was there… was there extra, hotel maintainer swag this year? Because every… every year, it seems like there's, like, oh!
Nice.
**Jason Plumb (Splunk Inc.)** 13:47 I wore it today. Yeah, New Relic, I think, put up for these t-shirts… for these, sweatshirts, and they're… they're pretty warm.
Yeah, that was the swag for maintainers this year, and… There were community awards.
I forget… Who all won.
I know that… I think Tyler from… Splunk 1, Tyler, yawn.
And… I think Tiffany from Docs, and I think someone else, I forget.
**Hanson Ho** 14:24 Cool. Should read the blog post or whatever that comes out. Seems pretty quiet. Well, I mean, maybe I've been paying attention to the right channels, I was pretty busy last week, so…
**Jason Plumb (Splunk Inc.)** 14:32 Yeah, I got some interesting insight from Tiffany, who runs the blog, and she's like, I want to kill it, it's too much work! Like, they're getting just hammered with submissions, so there might actually be a fork in the blogosphere around this topic. I mean, at least that's, I think, what she was leaning toward.
something where it's, like, just for, like, internal, like, developers and maintainers, and others, like, companies that want to put their use cases, their user studies, whatever, like, on… because there's a lot of… that's all being blended together right now on the blog, and it's a lot to maintain. Like, they have a really full backlog, and it's taking… A lot of time and effort to work on that stuff.
**Hanson Ho** 15:17 And they announced, Hotel Unplugged again this year in Brussels, or next year.
**Jason Plumb (Splunk Inc.)** 15:22 Brussels, yeah.
Yeah, in early, like, spring, maybe?
Like, February or March?
Yeah.
**Hanson Ho** 15:30 Is it gonna replace, or rather be the European version of the, the, what's that thing they have in the middle of the year? the one that got merged with, with, like, observe… I forget these names now, the one that was in Colorado last year, like…
**Jason Plumb (Splunk Inc.)** 15:49 Yeah, the summit. The… the… was it… the Open Source Summit.
**Hanson Ho** 15:56 Yeah, there was, like, two things that got merged into one, and then, you know, they wanted to do this thing in Europe, so I wasn't sure if… if, like, who's gonna go to what… which one, and,
**Jason Plumb (Splunk Inc.)** 16:10 Yeah, I'm not… I'm not sure. I think the… so OTEL Unplugged, they've done it a few times, and I think it skipped a year or something, and then I think this is, like… a reboot, and… I'm not sure of all the reasons why, organizationally. I think you can just reach out to Austin. I think he's the one… I think it's his baby.
**Hanson Ho** 16:32 Okay.
**Jason Plumb (Splunk Inc.)** 16:33 Oh, yeah, it's part of Fostim. That's cool.
**Juan Vega (New Relic, Inc.)** 16:37 Are any… are any of you coming to… to Russex?
In 2027? You don't know yet.
**Hanson Ho** 16:48 It's too early. Brussels is… it's a long way to travel for one day, so unless I was going to the entire conference, it's like… it'd be nice, but I don't know if I want to, you know, it's one of those things where it's a trade-off of traveling.
**Jason Plumb (Splunk Inc.)** 17:04 I'm in the same boat as Hanson, and I'm trying to do Barcelona, so having those, kind of, two months, like, one month apart is gonna be tricky.
**Juan Vega (New Relic, Inc.)** 17:13 Barcelona is, Kubernetes, or which.
**Jason Plumb (Splunk Inc.)** 17:16 Dear.
**Juan Vega (New Relic, Inc.)** 17:17 Yes, Marcela.
**Jason Plumb (Splunk Inc.)** 17:18 Yeah, KubeCon EU is in Barcelona.
**Hanson Ho** 17:22 When's the submission deadline, or is that… has that passed already?
**Jason Plumb (Splunk Inc.)** 17:24 It's passed, but the maintainer summit still has RFC open.
So, that's still a possibility, if y'all want to submit to the Maintainer Summit.
**Hanson Ho** 17:34 Observability Day is… is… is that, is that… that's also closed? Okay.
**Jason Plumb (Splunk Inc.)** 17:38 Yeah.
**Hanson Ho** 17:41 Oh, yeah.
**Jason Plumb (Splunk Inc.)** 17:43 I know, it's like… This just, like, happens so quickly between North America and South America. It's like, you finish one, and then you're already, like, working on the other one.
**Juan Vega (New Relic, Inc.)** 17:53 But QCOM… But it doesn't have a code for papers, no? It's closed. So the only way to go is, through sponsors.
**Jason Plumb (Splunk Inc.)** 18:04 That's right. The CFP is closed, but the maintain… I think the Maintainer Summit still is open.
**Juan Vega (New Relic, Inc.)** 18:13 Okay.
**Jason Plumb (Splunk Inc.)** 18:14 Let me see if I can find a link.
**Juan Vega (New Relic, Inc.)** 18:20 I mean, I went last year to Ruses, because it was a… Share flight, but it was, like, 6 hours.
round Grid.
But yeah, if I could go to Barcelona, it's better for me, because it's just 3 hours, so half of the trip.
**Hanson Ho** 18:39 Barcelona's pretty far, but Barcelona's pretty interesting.
**Jason Plumb (Splunk Inc.)** 18:43 Juan, where are you based out of, Juan?
**Juan Vega (New Relic, Inc.)** 18:47 Sorry.
**Jason Plumb (Splunk Inc.)** 18:48 Where are you based out of?
**Juan Vega (New Relic, Inc.)** 18:49 Canadian Islands, like, west coast of Africa.
**Jason Plumb (Splunk Inc.)** 18:54 Oh, my God.
**Juan Vega (New Relic, Inc.)** 18:55 Nia, near to Sahara, or Morocco, yeah, Western Sahara, Morocco.
**Jason Plumb (Splunk Inc.)** 18:59 Cool.
**Juan Vega (New Relic, Inc.)** 19:03 Well, this is actually Spain, but yeah, it's, like, far away from Europe.
**Jason Plumb (Splunk Inc.)** 19:07 Yeah.
Cool.
I think… Yeah, so the… observability Day… Closed October… the CFP closed October 18th.
**Juan Vega (New Relic, Inc.)** 19:23 Hmm.
**Hanson Ho** 19:28 private.
**Jason Plumb (Splunk Inc.)** 19:28 And then the schedule ahead of that, so it's gonna be Barcelona and then New Orleans in the US.
Then, next… the following year, Berlin. So I think that's the current trajectory.
**Hanson Ho** 19:42 North America is in America again.
As always, it will.
**Jason Plumb (Splunk Inc.)** 19:47 I know, we actually talked about that, they're like, why can't we find a good spot in Canada?
**Hanson Ho** 19:51 Every year, it's…
**Jason Plumb (Splunk Inc.)** 19:51 Plenty of…
**Hanson Ho** 19:52 I was like that.
**Jason Plumb (Splunk Inc.)** 19:55 I would support that, I'd be stoked, yeah.
Yeah.
**Hanson Ho** 19:59 Me too.
**Jason Plumb (Splunk Inc.)** 20:01 I mean, Vancouver, it's obvious.
**Hanson Ho** 20:04 I mean, I would love Vancouver, but, you know, it's, It's pretty far for people in Europe to get here, so I get it.
**Jason Plumb (Splunk Inc.)** 20:11 It's true. I could do Toronto, or literally anything.
**Hanson Ho** 20:15 Montreal.
**Jason Plumb (Splunk Inc.)** 20:16 Yeah, there you go.
**Jamie Lynch (Palo Alto Networks)** 20:18 Right, I've got, one, so…
**Jason Plumb (Splunk Inc.)** 20:20 Yeah, I think that's it. We're pretty good.
**Hanson Ho** 20:22 Thanks. Bye.
**Jason Plumb (Splunk Inc.)** 20:24 Right.
**Carlos Alberto Cortez (Dash0)** 20:25 See you.
**Ilia Liferov** 20:27 too, bye. Thank you.
