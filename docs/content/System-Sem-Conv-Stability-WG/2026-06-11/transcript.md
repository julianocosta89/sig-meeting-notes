SIG: System Sem Conv Stability WG
Date: 2026-06-11
Duration: 20 minutes
============================================================

## Zoom Recording Transcript

**Pablo Baeyens** 03:59 B.
**Dmitrii Anoshin** 04:00 Hi, Baba.
**Pablo Baeyens** 04:03 I think it's just going to be you, me, and Raylon today.
**Dmitrii Anoshin** 04:08 Okay.
How do I know Braden is joining?
**Pablo Baeyens** 04:14 He said it on the, the private tunnel, the second tunnel.
I've missed the last few weeks, but I don't know if you've discussed the… I don't think there's been time to discuss it. The PR to promote Process metrics on the entity to release candidate.
Could not be merged, because… there's something on Weber complaining about… some… attributes… not being stable.
**Dmitrii Anoshin** 06:24 haven't discovered that.
**Pablo Baeyens** 06:27 Okay.
Yeah, that's a bummer, but it makes sense.
So it's disk I.O. direction, network I.O. direction.
System.paging.fold.type.
**Fairly OddParents (ca-wat-brt3)** 08:00 on Zoom, do something. Okay, there you go. Hello!
**Pablo Baeyens** 08:04 Hey.
yeah, so I was just mentioning, This, on the… I don't know if you saw the… PR to promote the process entity, metrics to release candidate, there's an error because There's 3 attributes that… What three metrics I'm using.
that are not stable, and they are not in the process namespace. It's disk I.O. direction, network I.O. direction, and system baging hold type.
**Fairly OddParents (ca-wat-brt3)** 08:44 Oh.
**Pablo Baeyens** 08:45 Which is…
**Fairly OddParents (ca-wat-brt3)** 08:51 Oh, that's tricky, because the policy is specifically if the metrics are opt-in, but for network I.O. direction, That is not opt-in. I'm pretty sure that's, like, as a required attribute, so… Player on that one.
**Pablo Baeyens** 09:06 Yeah, no, we need to… Mark them as staple, or… Or decide that they are not required, but I think… I mean, I haven't checked the metrics back.
Based on the names, it feels like these are required attributes.
Or should we…
**Fairly OddParents (ca-wat-brt3)** 09:23 I'm pretty sure they are. We used to have… the I.O. as, as two different metrics. Like, the in and out were two different metrics, and we changed it to being… Based on an attribute, and that was on purpose when we did it.
So I assume you still want to do that.
I don't see a reason we couldn't.
We couldn't stabilize, though.
at least the network and disk I.O. direction. What was the third one, sorry? There was one in the system namespace you mentioned?
**Pablo Baeyens** 10:02 Yeah, system paging fold type.
**Fairly OddParents (ca-wat-brt3)** 10:06 Right. So that one… that one's easy, because that's ours.
not used by anyone else other than this metric, I think it's fair for us to just… stabilize that. I don't think we have a problem with that attribute.
For network and disk I.O. direction.
I don't think anyone else is using those.
attributes either?
So, we… We made it.
deliberate… there was a deliberate reason that we moved it. The reason we moved it was because of that… name prefix thing, like, if we already have… there's already a metric called system.network.io.
So we can't have system network I.O. direction, because a metric name can't be a prefix for an attribute. So we solved that by moving it to the network namespace.
I don't think anyone else is relying on either of those, though, right now.
So… I wouldn't have a problem with just, like, trying to stabilize them and see if anybody yells at us.
**Pablo Baeyens** 11:24 I'm checking if there's other… uses… There's a mention on the Kubernetes migration.
document. I don't know why.
**Fairly OddParents (ca-wat-brt3)** 11:46 migration document.
**Pablo Baeyens** 11:50 Yes, year.
it sounds like… the metric… from Kubernetes were stabilized.
With this attribute not being stable, So… We should not change it.
**Fairly OddParents (ca-wat-brt3)** 12:23 I guess it was… it was before the, Before that policy that… that forced that to happen.
**Pablo Baeyens** 12:31 Yo.
And then, there is one usage, actually, on the hardware metrics, but I don't think this is something that we should… be too concerned about.
**Fairly OddParents (ca-wat-brt3)** 12:42 Yeah, hardware… That whole namespace needs another look, needs some… Some trimming.
I don't know if the people who use those metrics are still, like, participating in SEMCOMF at all.
**Pablo Baeyens** 13:01 Yeah, I don't think so.
Okay, then for disk I.O.
Container.disk.io uses disk.io direction?
**Fairly OddParents (ca-wat-brt3)** 13:27 Oh, okay, makes sense.
**Pablo Baeyens** 13:31 Well, the same thing, system paging fault type is used by container.memory.paging.faults.
**Fairly OddParents (ca-wat-brt3)** 13:39 Which I think… if I'm not mistaken, those metrics were kind of based on Same ones we came up with for… For system A.
**Pablo Baeyens** 13:48 Yeah.
**Fairly OddParents (ca-wat-brt3)** 13:51 So it's probably not controversial for us to stabilize them.
**Pablo Baeyens** 13:58 That's what I mean?
Make some notes.
**Fairly OddParents (ca-wat-brt3)** 14:01 I think, I think, Christos and Roger are… Part of the owners for that, like, container namespace, too, so maybe we could just let them know?
When they, when they come back.
**Pablo Baeyens** 14:11 Yo.
**Fairly OddParents (ca-wat-brt3)** 14:11 Awesome.
**Pablo Baeyens** 14:13 Yeah, So… Website, that worked… Sorry, I'm going to make notes for next week.
But I have a lot of things.
on, since it's the three of us, I'll just use the opportunity to… ask about things from previous meetings I couldn't be on.
That's hard.
the network working group, is it about system.network?
**Fairly OddParents (ca-wat-brt3)** 15:11 It's… it's mainly about network, a little bit about system network.
**Pablo Baeyens** 15:18 Okay, on… What is under network?
Or… brother, I guess What I'm interested in is, like, who uses that? Who uses network?
Not system.network.
What?
**Fairly OddParents (ca-wat-brt3)** 15:34 EBPF really wants to use it.
My hope is that Is that system.network is… Still specific to, like, tracking network stats on a host.
Whereas the… the general, like, network namespace can be… More for, like.
things like SNMP data is a really popular thing that they really want to get working. Like, I don't think that should necessarily live in system, I think that should live in… under the network namespace, or maybe get its own SNMP namespace, not sure.
the main participants in the group are overwhelmingly from the EBPF, Group?
people who want golden signals, and people who want SNMP data, so…
**Pablo Baeyens** 16:23 Okay.
**Fairly OddParents (ca-wat-brt3)** 16:25 Appears to be the main reason.
For the… for the group.
**Pablo Baeyens** 16:32 Fucking… and then… I haven't taken a look yet at, data and PR for version metrics.
I'm not going to promise I'll take them next week, but if I have time and I take them next week, anything I… Hmm.
Jack, is there any open discussion? I assume?
rate or approve it. I assume Christos didn't approve it, because he's out.
Sorry, I saw Dimitri corrected. Oh, not right.
**Fairly OddParents (ca-wat-brt3)** 17:20 I haven't taken, like, a code-by-code, like, code line review. I agree with where we've landed for the approach, for the most part, but I haven't looked at, like, the PR to, like, add it to mdataGen yet.
**Pablo Baeyens** 17:35 Okay.
**Dmitrii Anoshin** 17:37 What are you talking about, HPR?
**Pablo Baeyens** 17:40 This one, 15309.
I think you're reviewed.
This week, maybe yesterday.
**Dmitrii Anoshin** 17:46 Yeah, I… From Donald, right? Yeah, I checked it yesterday. It's… seems pretty good to me.
if we… I agree, like, it's… Like, this court is not… super critical. If it breaks, it breaks, whatever is being generated, and, like, it's generated code, so…
**Pablo Baeyens** 18:07 Realigned, yeah.
**Dmitrii Anoshin** 18:09 I haven't, like, looked, like, by line as well, but in general, like, I looked in the parts that are… I'm more… worried about the data model for this new thing, and how it's been generated. What's the difference from how it affects current generation, and some other, like, questions I will… I was concerned about, and then everything was good.
And yeah, I just left a comment that there is some, like, probably redundant test that was added.
That's it. If you, like, can take a look, or, Braden, if you can take a look, I think we should merge it to unblock the work.
**Pablo Baeyens** 18:54 Okay, yep.
Yeah, I'll try and take a look either tomorrow or Monday. If I don't get to it, feel free to merge it without.
**Dmitrii Anoshin** 19:04 Sounds good.
**Pablo Baeyens** 19:25 Yeah, I don't have anything else.
Find.
**Fairly OddParents (ca-wat-brt3)** 19:33 I don't either. Between the batching project, the network group, and some internal stuff, I haven't been able to… Spend much time on these tasks.
**Pablo Baeyens** 19:44 Yep.
Same here. I mean, at least DataOx conference was, finished yesterday, so I finished the things that I was looking for, that I'll be a bit more free.
**Fairly OddParents (ca-wat-brt3)** 19:57 That's good.
**Dmitrii Anoshin** 20:00 Cool. Thanks, folks.
**Fairly OddParents (ca-wat-brt3)** 20:02 Thanks, everyone.
**Dmitrii Anoshin** 20:03 Yeah, yep.
**Pablo Baeyens** 20:03 Thank you. See ya.
