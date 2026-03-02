SIG: K8s Semantic Convention SIG
Date: 2025-07-23
Duration: 19 minutes
Zoom Recording URL: https://zoom.us/rec/share/LfxNcAyhODRoEJx4qg9Omtzx0viMCB2hepNZ1k5n8xCTq5b_-ffq8gG2q3-5EdkU.eH_AvG5Ddvjg6ePI
============================================================

## Zoom Recording Transcript

**Stephen Lang** 02:38 Hey? Debbie.
**David Ashpole** 02:45 Okay.
**Stephen Lang** 03:40 So I guess we can go ahead and get started right. It's like 4 min past.
**David Ashpole** 03:44 Yep, why don't we are there any topics, or should we just look at the triage board.
**Stephen Lang** 03:50 Yeah, I didn't have anything specific. So yeah, I could just check out the board.
**David Ashpole** 03:56 Already.
**Stephen Lang** 04:02 So it looks like guess from right to left. There's a couple in review.
**David Ashpole** 04:14 wasn't clear to me. If the container ports was
looks like maybe that's ready for review
and pod phase and pod status looks, good looks like I need to re-review that.
**Stephen Lang** 04:46 Alright, so it's had a bunch of work.
Let's commit 18, th so it looks steady.
I guess that's ready for review.
You're the one
I lost the board.
Where is it?
Oh, that's the same one.
Okay, it's part phase and status reason.
This has got 2 approvals, but it's still waiting for approving approvers.
**David Ashpole** 05:40 Yeah, yeah, I will take a look.
**Stephen Lang** 05:44 Cool, alright.
**David Ashpole** 05:49 Couple in progress.
**Stephen Lang** 05:52 From the top. I guess that was a big one is ongoing, I suppose.
The CPU. One.
Where did we get to?
Do you know what's going on with the utilization metrics in in General K. 8.
**David Ashpole** 06:21 No, I don't know what's going on in general.
**Stephen Lang** 06:24 Yeah.
**Dmitrii Anoshin** 06:26 We've been trying to figure out whether utilization is something that we
like can recommend with with the system semantic convention working group, because, like it cannot be special or aggregated, and everything
we probably won't would like to have it.
but it's at least should be optional.
And also there is a
still be discussion. What? How can we align on CPU metrics between CPU and Kubernetes, in terms of
like, whether usage would be present here and there as a default or time.
**David Ashpole** 07:08 Yeah.
**Dmitrii Anoshin** 07:09 And also why I missed that part. Why do we want to add Kubernetes prefix to the container? CPU utilization? Because I believe it was done without Kubernetes prefix, because it's pretty much same between different orchestration platform. It doesn't really
attached to specifically to Kubernetes.
**Stephen Lang** 07:31 I. Yeah, I don't think that's been brought up on this pr, yet. It's just kind of been assumed that it's all K. 8.
**Dmitrii Anoshin** 07:37 I think.
**Stephen Lang** 07:38 The prefix is already there.
**Dmitrii Anoshin** 07:40 No, no, you if you can see. Oh, container utilization. Yes. For for utilization against limit, request and note. It's kubernetes, right? But usage and time it's
**David Ashpole** 07:57 Discipline.
**Dmitrii Anoshin** 07:58 Values with no coverage prefix. Okay, that makes sense.
**Stephen Lang** 08:03 Yeah. So they're coming from the container right?
**Dmitrii Anoshin** 08:06 Sure. Thank you.
**Stephen Lang** 08:07 But there was one valid point, I think, that came up from this comment about utilization, which is.
if we were to have these Kubernetes utilization metrics.
What happens if you know you have a pod with 2 containers, and only one of those containers has requests set.
what does the utilization look like?
**Dmitrii Anoshin** 08:29 We don't admit that in in that case.
**Stephen Lang** 08:32 So it's just like an all or nothing, you think if you would only have utilization if all containers had the requests or limits.
**Dmitrii Anoshin** 08:40 No, it will be. It'll be
emit for particular container that have
containers that have utilization and requests set or or utilization or request. For example, if I have a container with request being set.
it would emit the container request utilization, but wouldn't emit limited utilization.
So it will be conditional, I believe, and also those metrics should be optional. They should not be something that users would
always want, always see. They would need to enable like or explicitly, hey, Buddy.
**Stephen Lang** 09:20 Okay.
**Dmitrii Anoshin** 09:20 Usage or time should be something that we should rely on instead, always.
**David Ashpole** 09:25 I think we should honestly get rid of container request, utilization.
Or maybe not. It doesn't make any sense for memory, because
container memory requests are just aggregated at the pod level.
But maybe it makes sense for CPU, because you would get throttled down to your requests if
yeah, if if the node ran out of CPU.
But.
**Dmitrii Anoshin** 10:04 So you're saying that limits for memory applied on the port level and not on the.
**David Ashpole** 10:10 Limit supply at the container level and at the cloud level, but primarily at the container level.
But then memory requests, apply primarily
at or apply only at the
memory. Requests only apply at the pod. Level. Memory limits apply primarily at the container level.
**Dmitrii Anoshin** 10:33 Interesting.
**David Ashpole** 10:36 Cpu requests apply primarily at the container level, and
CPU limits also apply almost entirely at the container level.
It's like the pod. The pod CPU limit. Utilization isn't very helpful
at telling you whether you're being throttled or not, because
all the throttling is generally done like the only way that you can have throttling at the pod level
would be if yeah, I don't even know, like.
there's no other sources of CPU usage other than containers, and the pods limit is simply the sum of the container limits. I think they've been talking about adding
explicit pod level requests and limits.
But I don't know if that's actually gone through yet.
**Stephen Lang** 11:28 So that was kind of my point with the pod level CPU limit and request utilization. Because if you have a pod with 2 containers, and only one of those has requests or limits set.
then the utilization is.
**David Ashpole** 11:42 Is gonna be.
**Stephen Lang** 11:44 Some kind of percentage which maybe doesn't make sense.
**David Ashpole** 11:46 It, it matters for memory.
So
memory is managed entirely at the pod level. So if you do care if you're exceeding your memory requests
at a pod level, but you don't care if you're exceeding them at a container level.
**Stephen Lang** 12:02 Okay.
**David Ashpole** 12:04 But for CPU that there's no
well, there's only sort of it doesn't really matter for CPU at the pod level, whether you're above or below your requests.
**Stephen Lang** 12:19 Something might be worth a comment in here, though, because maybe we don't need these right now.
Just the container ones would be enough.
**David Ashpole** 12:26 Session.
**Stephen Lang** 12:29 Is that what you're saying?
**David Ashpole** 12:31 Yeah. But then it's weird to have
those for memory, but not for CPU.
**Dmitrii Anoshin** 12:40 But we can avoid emitting any of them. So we don't emit any potentialization metrics, for now.
Oh, don't define them, memory or superior.
**David Ashpole** 12:56 I mean, it's quite useful for memory, memory, request, utilization.
**Dmitrii Anoshin** 13:01 Okay.
**David Ashpole** 13:01 At the pod level, because that's the thing that will determine.
**Dmitrii Anoshin** 13:06 Whether you're a candidate for eviction or not.
Cool.
**David Ashpole** 13:12 But that's the only one that matters today.
**Dmitrii Anoshin** 13:18 Okay.
**Stephen Lang** 13:31 Still a bunch left on the memory side of that one. I don't see memory.
**Dmitrii Anoshin** 13:35 Utilization here, actually based on the port. Can you scroll up?
It's container only.
Oh, okay, okay.
**David Ashpole** 13:51 Did they decide yet whether it's calculated from working set or usage?
I hope they're using working set.
**Stephen Lang** 14:07 And I haven't seen that discussion.
Okay, Dimitri, was there anything
in particular you wanted to talk about? Because we're just kind of going through the board.
**Dmitrii Anoshin** 14:32 No, nothing from my side.
**Stephen Lang** 14:43 Well, I think, unless there's anything else we can probably call it. Then.
**David Ashpole** 14:48 This will be my last day for 6 weeks, so I won't be here for the next couple of meetings, but I'll try and get reviews in on the stuff that's open before I
go on leave.
**Stephen Lang** 14:57 Great. Thank you.
**Dmitrii Anoshin** 14:58 Thank you. There.
**David Ashpole** 14:59 Alright. See? You guys.
**Stephen Lang** 15:01 But.
