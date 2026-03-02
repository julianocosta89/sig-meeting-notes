SIG: System Sem Conv Stability WG
Date: 2025-12-04
Duration: 16 minutes
Zoom Recording URL: https://zoom.us/rec/share/hdP6QST9x7dayyGGNFl4QHXIFMUafBpGUVyp_xjT5Bim40SdoaUDkFWk0Vu5P2WF.nMs2CBHe1vPsCsHF
============================================================

## Zoom Recording Transcript

**Fraggle Rock (ca-wat-brt3)** 00:46 Slope.
**Pablo Baeyens** 00:48 Hey, good morning.
Never know what's your time zone. Is it the same as New York?
**Fraggle Rock (ca-wat-brt3)** 00:58 Yes, it is.
Eastern.
**Pablo Baeyens** 01:03 Oh, I see.
**Christos Markou** 01:06 Hello?
**Fraggle Rock (ca-wat-brt3)** 01:08 Hello.
**Dmitrii Anoshin** 01:51 Hi, everyone.
**Fraggle Rock (ca-wat-brt3)** 01:52 Hello?
**Pablo Baeyens** 02:34 Do I have to… more, like, collector-adjson topic, but… If there's any…
purely semantic conventions topic, let's go over that first.
**Dmitrii Anoshin** 03:00 It looks like there's nothing with semantic conventions only. But what collector specific do you want to discuss, Paolo?
**Pablo Baeyens** 03:07 Yeah, so we talked about it, actually, yesterday, but, I want to…
Write something down on how we… Migrate people from old…
some article mentions to NIU on different places, including the host metrics receiver.
But basically… Let me… I think that one's not mine.
Oh, see… We mentioned, the environment variable…
We mentioned using two featured gates…
And we mentioned using, like, a meta feature gate for… for everything,
I get every unstable semantical mention, say, it's guarded by… by a single meta feature gate, and
That way, you don't have to… to enable things. And then, I guess, for the two feature gates, there's still, do we want…
We could do it per namespace.
So, for example… We could have one for the… one pair for the…
Process namespace that is nearing stabilization.
And then a different one for the system namespace. Or we could have a generic one for the component, and then,
We keep on adding.
Things, as they become stable.
I think those are the options we talked about, more or less.
Bye.
I mean, Christos, if you remember some other options we discussed?
Thank you, not it. Bye.
I feel like that was it.
**Christos Markou** 05:13 I think that's, what we discussed, yeah, right.
**Dmitrii Anoshin** 05:18 Yeah, I would say, like, from my point, the only, like, input would be that users need to be…
it should be easily to double publish, and by double publishing, I mean…
semantic convention on all the new ones, but there is some… always there will be overlap.
Means that we stabilized what was already…
used before, so in that case, that… that part of overlap, isn't, like, double published, of course, so we just sent one. But everything else is, sent,
At the same time. That's why I think it's… at least two feature gates is required, two feature gates.
like, is disabled, old metrics, and probably enable, enable, enable legacy, enable new metrics, something like that. And then, for us, we would…
Oh, actually, it should go from beta to alpha, so in that case, it will be disable legacy metrics.
**Pablo Baeyens** 06:19 Enable old, enable new. Yeah.
**Dmitrii Anoshin** 06:21 Right, right, right, right. That's the thing.
And… but asking about namespaces, we've been arguing about that in another issue related to Kubernetes.
I… like, potentially, maybe…
For some… so we need to just strike a balance here, to not make user… to not make it complicated to the user, so they have, like, thousands of feature gate to enable, disable.
And provide them granular enough.
configuration interface. Because, like.
Going too granular, it would be… we would be stepping on the already existing configuration interface when you can just disable particular metrics. Disable, enable them.
But…
I would… from my perspective, I would maybe say that prescriber… to feature gate per scraper would be enough.
So, for HostMed receiver…
**Christos Markou** 07:25 Component, like receiver or processor.
Wouldn't you say is good.
**Dmitrii Anoshin** 07:31 Yeah… do we need something like that for processor? I don't think so.
**Christos Markou** 07:36 We have resource detection processor, which…
**Dmitrii Anoshin** 07:40 Is that one?
**Fraggle Rock (ca-wat-brt3)** 07:43 That'll be covered by SEMConva in a few ways, yeah.
**Dmitrii Anoshin** 07:46 So, that one is affected by the change as well?
**Christos Markou** 07:50 I think so.
**Dmitrii Anoshin** 07:51 Okay. Yeah, I guess token point is…
**Christos Markou** 07:53 stuff.
**Dmitrii Anoshin** 07:54 Yeah, per company, it seems fine. Well, by per scraper, I meant that in cost metrics receiver, we have network, we have CPU, we have memory, so maybe, like…
pure sprayer, but I'm good with component as well. We can do it with one pair across matrix receiver, one pair,
like, pure the whole detection processor, or we can go just a bit level down, saying, like, peer every scraper in host metrics receiver, and peer every detector in reserve detection process, or something like that. And in Kubernetes, it would be… it's just one scraper, but maybe in Kubernetes, in that case, we would have, like, peer entity, I would say, I guess, I don't know.
But, like, I don't know, we can do a voting or something like that, maybe, like, bring it to broader discussion, but…
I would still vote for, like, higher level feature gates.
**Pablo Baeyens** 08:51 I think it also… Oh, you mean?
**Dmitrii Anoshin** 08:54 Yeah, per component, yeah.
**Christos Markou** 08:57 Yeah, I would be, yeah, I like it. It also, I think, from what I have seen, also depends, per use case. For example, I was checking, KH attributes processor.
And this migration will be… I still want you, Dimitri, maybe, to have a double-check there at some point, but I think the only breaking change is one single attribute.
something. So, this one will be super easy. In that case, if we had a single feature gate pair for all KHMAN conventions, we would have to block the processor. That wouldn't be nice. But in that case, we are lucky. So, per component works perfect in that case.
**Dmitrii Anoshin** 09:40 Yeah.
And pure component is something that we typically do in the collector. We typically have feature gate that only affects one particular component. I don't… sometimes we have, like, global feature gate, but it's probably not that widespread.
**Christos Markou** 09:59 My only… let's say, second thought on this. My only concern would be that
Let's say, for example.
I'm not sure about host metrics receiver, but, for example, the kubelet stats, or cage cluster receiver, they already have many metrics that they emit.
If we have…
let's say I'm fine with per component feature gate pair, but we should be aware that this means that we are committing that we're going to cover the whole list of metrics. Otherwise.
it won't be really useful to have this feature gate pair, and wait, like, forever for these to, you know, get stable in some ad conventions so as to port them back in behind the feature gates, right?
That's my only concern, that it will… might take time, and it will, you know, compared to having smaller groups that you can deliver fast… in a faster way, and ship them, forget the feature gate, move to the next one, something like this.
Yeah, I'm fine.
**Dmitrii Anoshin** 11:08 I see a point, I just don't have enough, like, let's say, context about what we are lagging behind. I was under the impression that Kubernetes were almost ready, and there will not be a need to keep it forever. So essentially, we need to stabilize
metrics emitted by a whole company by the time when we switch from alpha to beta. And this is not something that will happen, like, in a week or two. We still need to, like, several months for that, I would say.
**Christos Markou** 11:41 Yep.
**Dmitrii Anoshin** 11:42 And for several months, I think it's enough time to migrate all of the other metrics.
**Christos Markou** 11:50 Yeah, I think if I can, like, illustrate it better, there are some metrics that I'm not sure if we actually want them or not, in components right now. So, by having a single feature gate pair.
we will have to deal with them now, in some ad conventions and in general, and that will be kind of painful for us, but I'm fine doing this, if we agree on this.
**Dmitrii Anoshin** 12:17 Is that necessary? Can we establish a rule that we… there is some exceptions that we just don't care about, and that feature?
**Christos Markou** 12:24 We can do it.
**Dmitrii Anoshin** 12:25 Yeah, I think that's fine. For example, you may… I remember you mentioned OpenShift metrics. Potentially, those metrics might be even, like, a separate receiver.
**Christos Markou** 12:34 Yep.
**Dmitrii Anoshin** 12:34 And we, like, we never really, like, attempted to stabilize them, so I would say we just ignore them for now. They are out of scope.
**Christos Markou** 12:43 Yeah, yeah, yeah. The OpenSheet was just an example, might be other ones, like, I don't know, this utilization madness, discussing if we want them or not, and then Kubernetes is more, it's, yeah, compared to host metrics, we have…
more… more situations like this.
**Fraggle Rock (ca-wat-brt3)** 13:05 We are back once.
**Dmitrii Anoshin** 13:07 Maybe we can discuss it case by case, and decide if some metrics just can be kept out of scope, and I think that's fine.
**Christos Markou** 13:16 Okay.
**Dmitrii Anoshin** 13:17 For them, if it's, like, small amount of metrics, we can handle them separately, like, without any Fisher gates, let's say, and, like, deprecate one metric, make it optional by default and everything, so…
**Christos Markou** 13:29 Yeah, yeah. That would be, yeah, super good.
Okay.
I'm good then. My concern is covered by what you say now.
**Dmitrii Anoshin** 13:40 Cool. Thank you.
**Pablo Baeyens** 13:41 Okay.
I guess my only question here is, like, the meta feature gate, whether we want that or not.
But I think we could start with a feature gate per component, and that doesn't prevent us from adding a meta feature gate in the future if, like, people find it confusing, so I'd say let's start with that.
Yeah.
**Christos Markou** 14:07 I think this meta feature gate would make sense Once you have…
let's say, more areas covered. For example, in Kubernetes, you have
Two different receivers, and the processor, for example, so you have a meta feature gate that will enable the schema transition for all of them in this area.
So we can start small, and we can evaluate this later, I guess.
**Pablo Baeyens** 14:36 Okay.
Alright, so I'll write something down with, all this we discussed.
Anything else we should discuss?
**Dmitrii Anoshin** 15:01 Think we're good for the day.
**Christos Markou** 15:04 Sounds good.
**Dmitrii Anoshin** 15:06 Thank you, Hawks.
**Christos Markou** 15:08 Thank you. Bye-bye.
**Pablo Baeyens** 15:09 to your…
