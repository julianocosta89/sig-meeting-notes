SIG: K8s Semantic Convention SIG
Date: 2025-07-09
Duration: 17 minutes
Zoom Recording URL: https://zoom.us/rec/share/bMg6qk9ogdr6M1AAxkVfFLisa-ekrxaf-A6jy5EzZgmlLNjstm1DNqw13ha7FCuU.a69Y31iFHmK0kcSY
============================================================

## Zoom Recording Transcript

**Christos Markou** 00:41 Hey! Hello!
**Stephen Lang** 00:44 Hi! How are you?
**Christos Markou** 00:47 Good! How are you?
**Stephen Lang** 00:50 Depends.
**Dmitrii Anoshin** 01:54 Hi! Everyone.
**Christos Markou** 01:57 8.
So we start.
okay, seems we don't have any
like specific topics for today other than this call for reviews that I have added here. So this
file system metrics.
Is up for 3 weeks now, David already approved. But we have this rule. We need another approval for the seek, and then we can send it to the convention approvers or maintainers to review or just merge it.
And then there is another one
about pod phase and pod status region. Again, David has approved already. So we need another approval for this.
And in general, I think we have these 2
Prs that are in re review right now, waiting for this to approve or to review. And then there's another one waiting for the Maintainers to review and or merge.
Yeah, I will be off until end of August.
So if you could spend some time to review. These would be nice to have them in before me, leaving otherwise no worries
and
I also know that David will be off
2 weeks from now. So probably the meeting in 2 weeks from today will be the last one then we will resume early September, I guess. But yeah, we can use the
slack channel for us in communication if needed. I guess.
**Dmitrii Anoshin** 04:19 Where will be off?
We want to cancel. But do we need to cancel it when he's back.
**Christos Markou** 04:27 David will be back. I don't know when exactly he will be back. I will be back end of August, so I can just post on the Channel, and we can start again. So once I'm back, I I will let you know, and we can resume the meetings
if we agree.
**Dmitrii Anoshin** 04:45 All good.
**Christos Markou** 04:47 Yeah, in general, for the 1st pay for this phase now, transferring the metrics from the collector to conventions. There is not a lot missing. So if these 3 Prs finally make it
we have some metrics about open shift, we can. Probably we can.
Yeah, would be nice to have them as well. And then we have few metrics about
CPU. Those one this would be
those might be bit controversial because they involve utilization. And we have some ongoing discussions from the system work group about utilization metrics. Maybe we can. Yeah, we can discuss it then? Or we can just
yeah. We could even leave them out for now and
discuss them as during the stability period, and give some time probably for the system metrics working group to come with conclusions. And yeah, again, the metrics, the memory ones. Yeah, there are some that are more straightforward. But again, I assume utilization metrics would be controversial again. Especially for metric, for memory, because
we'll have several.
I'll have few types of memory here.
So, yeah, calculating utilization.
Yeah, which one you should use. So probably this is something that we need to leave out eventually. Yeah, this is more or less a start, so I don't know if there are any comments, questions.
**Stephen Lang** 06:33 Sounds good. Thank you. Christos.
**Christos Markou** 06:37 Yeah. Sure.
**Stephen Lang** 06:39 Just on if you go back to the CPU one I left a comment on the end.
Just about because there's there's been some comments around. The inconsistencies between some of these and I just kind of collated all of these into a table.
But it includes some of the utilization metrics you just mentioned. There's no indication
on this issue that the utilization metrics are, you know, maybe
influx. It might be worth dropping a comment on there, or link to wherever the discussions happening.
**Christos Markou** 07:12 Yeah. My, my, yeah, my expectation would be that. Whenever we try to introduce them.
We can have the discussions there and try to decide if which of those we actually want to. Introduce in the smart conventions. And yeah, for example, CPU limit CPU request. Maybe those make sense because they are opinionated metrics for kubernetes. And those are also used for eviction policies.
yeah, that the Kubernetes controller U users as well. Others like the node utilization. We might need to reconsider. Probably not. But yeah, it's a discussion that need needs to take place at some point so what I'm saying is just like
thoughts that we have here and there, and nothing concrete. So yeah.
**Stephen Lang** 08:17 Yeah. So, for example, like the node, utilization is kind of odd, because
there isn't a way to see the number of cpus from this receiver. Right? You you would typically find it from another receiver.
**Christos Markou** 08:31 Yeah, yeah, that's true. The weird thing with this metric is that? Yeah, what? What should be the limit? My only concern would be. What should be the limit that you calculate the utilization against.
because Node has this allocatable information and has also the capacity the current implementation. The collector uses the capacity of the node as the limit. But there is also the allocatable thing that you can use.
So yeah, if we come to a consensus. I would be fine to to have this. Yeah, but I would like to ensure that we will not introduce something that is either controversial or something that will be problematic will end up being problematic in the future.
That's my only comment for this.
**Stephen Lang** 09:23 Sure. Okay. Thanks.
**Roger Coll** 09:26 Just wanted to say that from the system Semantic Commissions group and specifically
is working on a guidance document across utilization metric tricks that then we can reference and and discuss this kind of
utilization metrics.
So it's a work in progress. There.
**Christos Markou** 09:48 Okay, cool. Thanks. Thanks for the contact, Roger. Probably the safest option here is to try send the pr that introduces all of them.
And then, yeah, we can collect feedback and check if there are arguments against introducing them, or some of them. Probably. That, that would be the right time to do it, and if not, we can just introduce them.
That could be an option.
**Stephen Lang** 10:23 Sure. Okay.
Thanks.
**Christos Markou** 10:27 But for metric, for memory is yeah, it's it's not that easy. It's even harder. Because.
yeah, you have
working set and usage when a pod is killed without of memory the calculation uses the working set. But
yeah, should we use this? And why not to use the usage. Should we have 2 utilization metrics? Yeah, it get. It gets more more complicated. And we had an issue in the collector repository about. Why not using working set for utilization, since this is the one that actually is used by kubernetes.
But yeah.
**David Ashpole** 11:11 We can discuss it.
**Christos Markou** 11:13 As part of this issue.
**David Ashpole** 11:15 Yeah, I agree with using working set.
**Christos Markou** 11:19 Yeah.
Probably it's safer to to leave it out. I mean less thing to maintain or justify about.
But you can.
**David Ashpole** 11:30 Utilization, Metrics.
**Christos Markou** 11:33 That's a discussion that we had. Probably we need to decide on this and
potentially decide to leave some of them out. If yeah, don't make, don't. Don't make sense for us.
Cool anything else.
**David Ashpole** 12:02 No, thank you for all the all, the work.
**Christos Markou** 12:07 Thank you for. The reviews. Yeah. Left some issues here already approved by you, David. Thanks. Will be nice to have them in soon.
hoping also the Maintainers to check the other one that is approved by the seek. So
should be good.
So I guess that's all for today.
**Dmitrii Anoshin** 12:33 Thanks folks.
**Christos Markou** 12:34 Thank you.
