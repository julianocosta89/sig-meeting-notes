SIG: System Sem Conv Stability WG
Date: 2025-09-25
Duration: 20 minutes
Zoom Recording URL: https://zoom.us/rec/share/OdaMkvbl0pMOD3VVD0B82CbvDhVXLXG4r-JEZU8jml6rQmUmyh8JwRR0_o-TpOEY.fgoIiZGndieQg2RL
============================================================

## Zoom Recording Transcript

**Christos Markou** 01:47 Hello?
**Roger Coll** 01:48 Hello.
**Christos Markou** 05:45 I think Dimitri's not joining, probably will wait for Bride and Mangas.
There's no joining, too.
**Pablo Baeyens** 05:58 I did speak to him over Slack.
Earlier today, so… Probably he is.
I guess we can start.
Considering, if you can…
Is there anything.
**Roger Coll** 07:08 to discuss today.
I see There's nothing, at least on the agenda.
**Christos Markou** 07:17 I shared here in the Zoom chat the draft here that I have for, creating guidelines for, the requirements… requirement levels for CPU metrics. It's still draft, probably, it's ready for review.
But yeah, I assume, lots of discussions will, came out of this.
**Pablo Baeyens** 07:50 Do you want reviews, even if it's in draft, or…
Are you still working on it?
**Christos Markou** 07:58 I don't think that I plan to add anything else, probably just minor, changes, minor improvements.
Like, we read English and changing small stuff.
**Roger Coll** 08:32 Will this issue help unblock, the guidelines about limit, usage, utilization, etc, etc, or…
What's the… the contacts of that, yeah?
**Christos Markou** 08:46 Yeah, yeah, it's about this. So, Dimitri filed an issue, some time ago about providing guidelines about…
Which metrics should be recommended, and which should be opt-in.
And last time, we discussed a little bit, and, I think we kind of agree that, within this group, that CPU time should be the only one being, required or recommended.
As we call it. And then the rest of them can be added if needed, but then they should be opt-in. For example, some of those make sense for systems like Kubernetes, where utilization against a limit or request makes sense.
Also, CPU usage is coming directly from Kubelet Stats API, so probably we can collect this directly. Makes a bit of sense. But, yeah, for system or process, doesn't make sense to calculate usage, for example.
Because of the issues that the time window brings into the table, if it's not, specified.
So, yeah, it's more or less a summary of this discussion, and I try to formalize this approach.
**Roger Coll** 10:06 Okay.
That's good, thank you for the context.
**Christos Markou** 10:10 Yeah, and applies for all the areas, that's a… that's a point. Kubernetes, system, process.
containers.
And probably some others, like JVM or whatever, but configure a shot.
**Josh Suereth** 10:24 I really like this guide, by the way. The rationale, I think, is spot on.
And, yeah. I think you should take it out of draft so I can mark it as approved.
**Christos Markou** 10:35 Okay, now I feel more confident about… about this. Cool, thanks.
after Brydon's guideline PRs, I think the bar is really, high, so… Yeah, that's…
I will notice, too, ready for you.
And, yeah, then since we're done…
Yeah, since we don't have anything else on the agenda, just a, like, heads up, I chatted a little bit yesterday with, several people, and with Brighton. It's mostly a follow-up from the discussion we had last time, and,
yeah, filed this issue. I'm planning to work on this, soon, in the following weeks.
And, yeah. The goal is to have a more specific process of
Starting, moving metrics into stability.
focusing on specific… I… from my perspective, like, focusing on process CPU time, for example.
To make… start, will help, will unlock us. And, I could also try to have this, like, end-to-end, which means from semantic conventions down to the collector, probably a draft PR or something.
And, yeah, I'm not sure what is missing, Bryden. Maybe, since she joined, can comment on this. Probably something about mdata gen or something.
But yeah, I'm also working on some PRs to add to exposed ability level per metric in the collector components, and my next thing would be to…
try to see how we can add an extra field to provide information about SMAT conventions.
where it is documented in some other conventions, something like this. Yeah, but this will come next. I think with this, we should be fine, too.
Start doing the implementation.
Or adapting the components in the collector.
**Braydon Kains (Google)** 13:02 In terms of what the collector was gonna do for…
implementing SEMCOMF, my thought process was… Feature gate?
And behind the feature gate.
within each… each scraper, there would be… there would be two metadata gen config files, one for the SEMCOM schema and one for the original.
And… It would decide, based on the… Based on the…
Future flag, but the future gates on or off.
Which, which one to use.
I don't have a PR together yet, and that's mainly because I was… looking into… Whether we can…
like, leverage Weaver for tests in some way. Like, my thought was that… If we could…
the problem is that you need… we start to require the use of Docker, which I don't think in the collector we force at the moment, but if we could spin up a Weaver instance and
start firing semconf… the SEMCOMF version of the schema at it, and see if it's right.
That would… Probably be… be helpful.
I don't have anything… working yet. And I know we also talked about the potential of
leveraging the actual SEMCOM schema from Weaver somehow in mDataGen, which I think the…
the last time I remember talking about it.
they weren't a fan of adopting the Weaver schema whole, like, wholesale, but… Potentially allowing, like.
Weaver config, like, referencing, or, like, referencing Weaver config from the mDataGen or something? I don't think there's been any movement on that.
If we could just, like.
somehow directly generate off of our semconfigs, it would be much better, but I don't think that's gonna be…
Doable in the near term without more…
more development time. So I think I'll start by just putting together
maybe just for one scraper, like the… the feature gate will be at the receiver level, and then for one scraper, I'll show an example of the two… the two packages thing, and I'll put that up as one PR so we can see, and then…
if we all agree on the implementation and move ahead with it, I can…
Add the other scrapers, one by one, to…
to have, like, SEMCOMF… SEMCOMF… separate SEMCOMF schemas as well. I'm thinking one… one feature gate on the… at the receiver level.
rather than a feature gate per scraper, but…
I might change my mind on that. We'll see.
That's where I'm at on the implementation stuff.
**Christos Markou** 15:51 For Cage, we have this migration guide, and we have decided to have.
a feature gate… actually, two feature gates, one for the stable and one for the legacy schema, on gauge level. So it's like semconv.cage.stable and .legacy.
One… there is one argument, there is a PR on… in the collector, and, somebody, questioned this decision, because…
Batching many metrics behind this feature gate might be… might cause trouble to users, so, yeah, the… the alternative would be to have different feature gates.
Per, let's say, batch of metrics or specific metrics.
But I'm not sure about this. Probably something to consider, we can evaluate this.
**Braydon Kains (Google)** 16:47 Yeah, per batch of metrics,
I could… I could see it. For host metrics, I could see the argument for making it per scraper, because those will presumably be different namespaces.
like, maybe a… maybe a per namespace feature gates is… is fine, it's just there'll just be a lot of feature gates, and it's kind of cumbersome, but…
**Christos Markou** 17:12 Yeah.
It will be hard to maintain configurations, then.
Managing all the different feature gates.
**Braydon Kains (Google)** 17:19 Yeah.
**Josh Suereth** 17:24 Think about consumers here, too. It might, like…
As much as people hate bundling things together, because you can't control timelines, it might make sense to just have a…
we're stabilizing a big… a big chunk, you know, for a lot of them at once. Like, I understand what you're trying to do of keeping it small and incremental, but,
The user experience of that, remember that as long as you're in transition between non-stable and stable, users are dealing with churn.
And so, there's a balance between the value they get of going through the churn, and how often you force them to do it.
So, in this case, is it valuable enough that users are going to be using those feature flags?
to move from A to B? Or are we just kind of, like.
You know, creating a whole bunch of churn.
Instead of one instance of it.
That'd be… that'd be my… my concern here.
I think the issue of whether it breaks is… is…
That's gonna happen, right? But it's more…
how does someone interact with it? Feature flags do help with the breakage?
But if you're having so many of them, it might just give users the, you know.
I already said this, but again, just to reinforce, you don't want to give users the sense that this is continually breaking.
**Braydon Kains (Google)** 18:45 Yeah.
That makes sense.
Did we have any other topics today? That was the main thing I was gonna talk about, was the…
the implementation work I was starting.
**Christos Markou** 19:59 Seems that's all, at least from my side.
**Braydon Kains (Google)** 20:13 Alright, then we can probably end early if nobody has anything to… to bring up.
**Roger Coll** 20:20 Sounds good, Tony.
**Braydon Kains (Google)** 20:23 Thanks, everyone.
**Roger Coll** 20:24 True.
**Christos Markou** 20:25 See you. Bye-bye.
