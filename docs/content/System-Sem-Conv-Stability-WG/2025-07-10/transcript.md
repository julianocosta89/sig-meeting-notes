SIG: System Sem Conv Stability WG
Date: 2025-07-10
Duration: 8 minutes
Zoom Recording URL: https://zoom.us/rec/share/ORiUR1SDgwugu1DWWMCba2suBIzvKpicVtlXoULtcfdub5JtCclKva5iYncz_1TV.qEIgqfRUpfb5wUpq
============================================================

## Zoom Recording Transcript

**Pablo Baeyens** 01:02 Hey!
**Christos Markou** 01:06 Hello!
**Pablo Baeyens** 01:11 Been a while since I joined. Sorry.
**Roger Coll** 01:17 Think we canceled a few meetings so.
**Pablo Baeyens** 01:22 Okay, well, not about it.
**Roger Coll** 01:25 Like.
**Dmitrii Anoshin** 01:28 Heard of them.
**Roger Coll** 02:05 Looks like, right. I'm just keeping today's meeting.
Maybe you can kind of stuff.
I just so I just put it one topic here that it has been open for a while. And well, they didn't provide much context.
But basically, someone made a Pr about changing the current superior.
Sorry the host architecture attribute and moving it under the CPU. Let's say namespace in the middle. And well, it was initially approved. But then I was just answering if it would be, let's say, feasible to move it to the CPU namespace, because we have a CPU namespace as well at the moment. There's just one attribute that it's a CPU dot mode, because it's used across the containers, the Kubernetes and the system metrics.
So a while ago well, we decided to move it there.
and it looks like this CPU dot architecture. It's also off possible or reliable to to put it or use it from within other.
Let's say, metrics that are on not only a system.
And yeah, I was wondering if what should be the reasoning between keeping it into the host or moving it to a more narrow it name a space. Only don't know if there has been any yeah discussions around that already.
**Dmitrii Anoshin** 03:55 Yeah, I think, as you mentioned, that makes sense. If it's shared between different other namespaces, different metrics like container host, etc. It can be moved to CPU.
**Roger Coll** 04:09 Okay thing is that I'm not sure if at the moment it is using any Kubernetes container metric.
I'm not. I don't think so, but it could in the end, and just
**Dmitrii Anoshin** 04:23 Yeah.
**Roger Coll** 04:24 So.
**Dmitrii Anoshin** 04:27 Yeah, I think potentially it could be used. It's still a valid reason.
**Roger Coll** 04:33 Okay.
**Dmitrii Anoshin** 04:34 But but that's my my opinion on that.
**Roger Coll** 04:40 Sounds good. I think the same. Maybe I will add a comment just maybe referencing the the CPU. That mode issue a while ago, and we can. Maybe you can use that one.
**Christos Markou** 04:57 Do we have CPU entity? Because, if I can understand, if I understand this correctly.
they should be entity attributes or or not.
**Dmitrii Anoshin** 05:09 No, we. So far we haven't. We decided to not have CPU entity as a separate entity. Because typically when when you like, the reason to introduce an entity is that if you, if you can associate.
it's a limiter for that particular entity. But it's not the case for CPU, because typically, you will like emit metrics for the whole host, for the whole container, etc. Not per CPU.
Otherwise you you would have let's say, CPU utilization and CPU would be a resource by itself, which is not the case. We have system CPU, like time, for example, in force, matrix receiver, and we have CPU logical count as a metric attribute, but not as a resource attribute. So we don't like consider CPU as something that emits entity by itself.
**Christos Markou** 06:14 Okay, so the entity here would be host.
**Dmitrii Anoshin** 06:17 Right and oracle, or anything like that.
**Christos Markou** 06:24 Yeah, and sure, go ahead.
**Pablo Baeyens** 06:27 I was thinking about the issue. That movie store guy open a while ago where he mentioned a system with multiple CPU sockets with different cpus. I guess.
Yeah. Identifying a host with a CPU doesn't make sense in a in a system like this, where there's it's like one too many relationship instead of a 1-to-one relationship.
Oh.
I don't know if that affects the the entity discussion, but it does affect the namespace discussion at least.
**Dmitrii Anoshin** 06:59 Yeah, thanks for posting this.
**Roger Coll** 07:17 Oh, thank you. I guess then that's it from my side. Don't know if there's any other topic.
**Dmitrii Anoshin** 07:30 I'll bring this issue to, and statistics.
Thank you.
**Roger Coll** 07:36 I'll give anything else, or we can. We can keep it short today.
**Pablo Baeyens** 08:14 Yep.
**Christos Markou** 08:17 Sounds good.
**Dmitrii Anoshin** 08:18 Sounds good to me.
**Roger Coll** 08:19 Okay.
Bye-bye.
**Dmitrii Anoshin** 08:21 Alright!
