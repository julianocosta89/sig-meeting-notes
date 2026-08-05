SIG: K8s Semantic Convention SIG
Date: 2026-08-04
Duration: 30 minutes
============================================================

## Zoom Recording Transcript

**Christos Markou** 02:33 Hello?
**Stephen Lang (Raintank, Inc. – Grafana Labs)** 02:37 Bye.
**Jina Jain** 02:44 Good folks.
**Christos Markou** 03:19 I'm not sure if we expect anybody else from my side, I just, shared the PR, but… Tries to promote the… uptime metrics? Oh, I see Jina approved, okay, thank you for this.
Yeah, so my plan is to allocate some time in the following weeks and months to continue promoting metrics to release candidates. I was thinking to Focus on metrics that are used by the cubelet stats, receiver.
And once we have this list complete, maybe we can try to port them back with a feature gates mechanism.
We have a similar approach in the host metrics receiver already, and this will be, like, in place for some of the scrapers there. Once this is done, we can follow the same pattern for the kubeletSaat receiver.
So, yeah.
Other than this, I don't have anything else.
**David Ashpole (Google LLC)** 04:27 Hey, sorry.
**Tyler Helmuth** 04:27 Christos, do you have a list of, like, issues… that you would want help on, or are you just gonna, like, keep opening the PRs like you've been and get reviews?
**Christos Markou** 04:41 I think we have a board.
Which is, this one.
And we mark, we have the… this view.
GA's ability.
Items… So… few things that I think would need some love is the… utilization metrics, both for CPU, but also for memory. Those are kind of controversial ones.
And then… Beyond this, anything… from the metrics that we have already defined that are in development, and they are used in the Kubelet SARS receiver, for example, yeah, anybody can pick anything and evaluate these, suggest them for Release candidate, for example.
Okay. We don't have a meta issue, maybe I could create one to list all the metrics that are used by Kubeletch Receiver. I have one for my notes, maybe I can publish this.
**Tyler Helmuth** 05:45 I guess I'm kind of wondering… We know that there's blockers for the utilization metrics.
**Christos Markou** 05:51 Yeah.
**Tyler Helmuth** 05:52 the other metrics.
Should we just, like, make an issue that proposes everything else as stable? Are we at that point?
Or is it better to go, like, in little… in smaller groups?
**Christos Markou** 06:05 I like to go smaller groups, because I take some time to just… Verify everything again, collect some information.
Instead of just YOLO, promote everything.
So yeah, but it's up to you, I mean, if you want to group them together, some of those at least, you can still do it.
**Tyler Helmuth** 06:26 Okay.
**Christos Markou** 06:32 Usually, it makes sense to group them by concept, like, all the memory metrics together, then… All the related network metrics together, and, following this pattern.
But, quarterback.
**Tyler Helmuth** 06:48 Makes sense to first promote… Any of the related attributes?
Or have you been promoting the related attributes with the metrics? Like, for example, like the errors?
the network errors has a… or attribute, like, network interface I just saw got recommended for promotion, separately.
**Christos Markou** 07:08 That is a requirement, yes, so whenever we spot some attributes that need to be promoted as well, we need to do this first.
**Tyler Helmuth** 07:15 Okay.
**Stephen Lang (Raintank, Inc. – Grafana Labs)** 07:20 Tyler, can you link to the… the network interface attribute promotion?
**Tyler Helmuth** 07:25 Yep.
**Stephen Lang (Raintank, Inc. – Grafana Labs)** 07:26 Thanks.
**Christos Markou** 07:46 I think also…
**Tyler Helmuth** 07:47 Yup.
**Christos Markou** 07:48 There are some, Like, incoming requests, Here and there, for either implementation, dishes, or… Usually implementation additions lead, lead to… Semat Convention Edition, so… yeah, any help there?
would be appreciated, I guess. Either comment, reject, approve, I mean, accept an addition, or, sponsor it.
Or supported, whatever.
Right. Anything else?
3 to 1? No.
Okay.
Thank you, folks. See you.
**Tyler Helmuth** 08:41 Cheers.
**Stephen Lang (Raintank, Inc. – Grafana Labs)** 08:41 Thanks.
**Christos Markou** 08:42 Bye-bye.
