SIG: System Sem Conv Stability WG
Date: 2026-05-07
Duration: 16 minutes
============================================================

## Zoom Recording Transcript

**Donal O'Sullivan** 05:07 figures.
**Dmitrii Anoshin** 09:22 Alright folks, sorry for joining late.
**Donal O'Sullivan** 09:38 low…
**Christos Markou** 09:43 Shall we start. I, I only added one, One topic for today, seems Braden is not joining, and I'm not sure about Pablo.
But maybe we can… I can just quickly highlight this, and then we can wrap it up.
There's nothing else.
So… Yeah, I… I filed an issue to suggest the… promotion of CPU mode attribute, and, the reason for this is that, it is a shared attribute between system process, containers.
And I'm not sure if anything else… and I think .NET also uses that.
From what I saw.
And, on another work stream, I am trying to start promoting some container and Kubernetes metrics.
And the first one is, for example, CPU time of container, and this metric has CPU mode as… conditionally required.
But yeah, the point for this group, the system group, is, that we need To consider about it.
The CPU mode one, and… yeah, if we all agree, we can already… I can already send the PR to promote it to Liz.
Candidate?
And I also have another one, that I link here, PR number 30… 3700.
which, adds some additions. Actually, it removes state mode.
from the members, the kernel, because, while taking the container metrics, I realized that, we had added kernel mode to accommodate for metrics in Docker Stats Receiver, but it seems in general that all container runtimes and all implementations, it's essentially system, so it's… we can use system, which already exists, and remove kernel. That should be, like, simple change. And, yeah, so I would appreciate any reviews on this one, and if you have any, like, concerns or thoughts about proceeding with Doing… promoting it to release candidates, let me know.
**Dmitrii Anoshin** 12:20 No concerns from my side. Sounds good to me, thank you.
**Christos Markou** 12:25 Yeah, there was a… yeah, we can discuss it maybe in another scope, but Dmitry, maybe if you are interested, the discussion around container CPU time, because yeah, we had an extensive discussion with David about this on the PR. Yeah, feel free to have a look as well, but it seems that we have a clear path forward. The… confusion, at least from my side, is that in containers, the CPU time when you retrieve it, for example, from Docker Stats, or CAdvisor, or any pure runtime stats API, You can have both the total as a… Standalone metric thing.
But also, you can get more granular statistics about the user and the system.
Cpu time.
And… At the same time, in Kubernetes, using the kubelet starts API, we only retrieve the total, because the way that kubelet starts works.
it gets this metric directly from CAdvisor and uses a standalone metric.
So, back then, when we defined that metric, we said that the mode should be conditionally required. So, when this metric is used by Docker StatsReceiver, for example.
the modes are populated, the attributes, but when it's used in Kubernetes context, you just emit it without, any attributes implying that this is the total. I'm not… I was not sure if this is valid when it comes to, like, modeling in general in OpenTelemetry, and if that would cause any issues with Prometheus, for example, but David seems to, agree that it's not an issue. And the second issue was that, aggregating, summarizing system CPU time and user CPU time, might not always be equal to total, but we figured out that with CGroup V2, the difference will be quite insignificant, like 1 microsecond, something like this.
So it seems that we are safe to, like.
have the two modes, system and user, from Docker Start, for example, and do not emit the standalone metric. And users that want to, like, produce the total, they can just aggregate the two modes, based on this attribute, and produce something that's, like, super, super close to total.
In most of cases, that would be equal, but might be different, but the difference is only 1 microsecond, so it's not a significant issue.
Yeah, that's the… that's the story there, and it's also related to the changes that I do for the CPU mode, removing the kernel mode, and also adding some additional Clarifications on container side.
how these modes are used and what it means. So, yeah, would appreciate a review there.
**Dmitrii Anoshin** 15:26 Sounds good, thanks for… thanks for, providing the summary.
I… I need to find that issue. If you can… if you have it handy and you can send me, that would be perfect, but I don't have any employees.
Anything is true. Any strong opinion, I agree with what you said, so… I just… I'll take a look.
Just…
**Christos Markou** 15:49 Yeah.
**Dmitrii Anoshin** 15:50 For my information.
**Christos Markou** 15:51 Yeah, I sent the PR here, I also added that on the agenda, and the generic one is about CPU mode, graduation is the second one I sent.
On the first one, you can find the link to the PR for Container Metrics, if you're interested.
But this would be, like, later. I mean, we still need to clarify if we are allowed to stabilize metrics.
Without entities, but this is another discussion.
now it's kind of blocked on GPU mode, let's see.
**Dmitrii Anoshin** 16:25 Thank you.
That's good.
**Christos Markou** 16:29 Okay, cool. Yeah, that's what I had, yeah.
So… If we don't have anything else, we can… Wrap this up, or… yeah.
**Dmitrii Anoshin** 16:42 Sounds good to me. Thank you, folks.
**Christos Markou** 16:45 Okay, cool.
**Donal O'Sullivan** 16:46 I suppose.
**Christos Markou** 16:46 Mike?
