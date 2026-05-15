SIG: System Sem Conv Stability WG
Date: 2026-05-14
Duration: 12 minutes
============================================================

## Zoom Recording Transcript

**Braydon Kains (Google)** 08:12 Hey, not sure if we're getting anyone else today.
**Christos Markou** 08:17 Hey, yeah.
I just saw, Donald mentioned.
He's not coming.
**Braydon Kains (Google)** 08:29 Yep, that's… I think… I checked the… the… Maintainers… Want us to… Stabilize the entity at the same time we… Stabilize the attributes.
I'm not sure if the… Entity is necessarily ready for stability, even though the attributes are.
**Christos Markou** 09:11 Yeah.
**Braydon Kains (Google)** 09:11 So, I'm not sure how to handle that, but…
**Christos Markou** 09:15 we… did something similar in, Kubernetes.
So, we promoted to release candidate attributes, or a selection of attributes that we are going to need.
In the process, or without promoting the entities yet.
And we even promoted some, metrics, Kubernetes… the first Kubernetes metrics, three of them, were promoted to release candidate, even if it's not clarified yet if Entity stability is… Required for metrics.
Yeah.
Because the… the way that the registry and the attributes work.
the very single piece of, let's say, information is the… just the attributes. You can use them whenever you want, so… doesn't harm. When you go to metrics or entities, things become more… complicated, I would say. So…
**Braydon Kains (Google)** 10:18 Yeah.
That's kind of what I was thinking, because, like, I can see why they want metrics.
an entity to be… to go stable at the same time, like, you… you wouldn't want to stabilize… I can see why you might not want to stabilize metrics before the entity, but the attributes don't feel like the same the same calculation, because, like, the attributes… Can be stable, even if how exactly they're used on the entity in particular isn't stable.
That seems fine to me, but…
**Christos Markou** 10:49 are we going to… I don't think we're going to promote from release candidate to stable the attributes.
Without, first, also, doing some work also with entities or whatever. I just think we're doing this Gradually, right? So…
**Braydon Kains (Google)** 11:05 Yeah, I think so.
**Christos Markou** 11:07 The first killer is the… The release candidate, and we're targeting to move everything there.
not… Take the attributes from beta, whatever it is now.
to release content and then to stable without caring about the rest of them, so maybe we can also clarify that.
**Braydon Kains (Google)** 11:28 Yep.
**Christos Markou** 11:34 Yeah, I don't scarve anything else, for today.
I don't think I do either.
Yeah, so… Donald mentions.
He was supposed to work on the… Right, the migration.
Code refactoring.
Yeah. She will send the PR, he says, okay, so the PR is not up yet.
**Braydon Kains (Google)** 11:59 I'll watch out for it.
**Christos Markou** 12:00 Yeah, cool. Me too.
Yeah, alright, yeah, if that's the case, maybe we'll think.
Rocked up here.
**Braydon Kains (Google)** 12:10 Okay, sounds good.
**Christos Markou** 12:12 Cool. Thanks, brother. See ya.
**Braydon Kains (Google)** 12:13 Talk to you later. See ya.
