SIG: K8s Semantic Convention SIG
Date: 2025-09-17
Duration: 19 minutes
============================================================

## Zoom Recording Transcript

**Christos Markou** 00:39 Hey, how's it going?
**David Ashpole** 01:34 Hey, hey.
**Stephen Lang** 01:36 Okay.
**Christos Markou** 01:38 Hello.
**Stephen Lang** 02:23 So I had a look at some of the discussions and PRs from last time.
And so one thing that I learned was…
the attributes have to be globally unique, and I thought that they were scoped to individual metrics.
So… That was, that was new to me.
**Christos Markou** 02:45 Yeah, it… it's, yeah, now some other conventions use this global…
Flat registry, let's say, were all attributes.
Are, registered there, and… We consume them from metrics, entities, resources, and so on.
**Stephen Lang** 03:08 Okay, yeah, so… I need to be really careful if I'm, creating any new attributes.
**Christos Markou** 03:13 Yeah. I think there was also… One year ago?
Should be more than one here.
A new constraint or,
ruling in some other conventions that Attributes should be namespaced.
Like…
Yeah, so you cannot have a similar approach to what Prometheus metrics have, for example, where tags can be permetric or whatever.
Which is good, but also it's also bad, because, brings other problems for us.
Quick and start. What do you think?
And share… Can share my screen, too, about the agenda.
In front of us, so…
Yeah, I added two topics for today, if you have anything else you want to discuss, please.
added here. So…
Yeah, one thing is that, I took the liberty to create a new tab, in our board, and, explicitly start collecting
Issues that, we should tackle as part of the stability, of this area.
And, there are issues that were already present, that were already, there in the main board, or issues that I created last week,
And the reason for this is that, working on this, like, revisiting this meta-issue here, the big one, which is actually the phase one of this group, which tries to do the initial implementation of the SMAT conventions, some metrics are more straightforward.
From the leftovers, some were… were more straightforward, while others,
could be considered as part of the stability phase. So, for example, this, CPU utilization metrics, that we also discussed last week, for example, with the introduction… with this new feature of Kubernetes that limits can be set on pods level, and in general.
CPU utilization is a controversial thing, but I think we can tackle this as part of the stability phase. No need to block the first phase.
Now, based on this. And, same for memory, for example. Here, again, we have utilization
metrics, and also the way that we calculate the utilization might be…
not necessarily wrong, but not really useful, because somebody had raised in the collector that utilization is not really meaningful. If you do the ratio of the usage, it should be the working set, because that's what the, eviction.
eviction mechanism on Kubernetes users, I don't remember the name of the component. So we need to consider all these,
all these things. But for now, I think we're good, and…
Yeah, for this huge meta issue, I think there are only 3 open issues.
So… David already approved these memory metrics.
Oh.
PR.
Show.
Stefan, if you want to take a look as well, please.
Feel free. And, podface, I think this one is…
We shouldn't block this, because it was blocked based on the guidance PR that Bryden is working on, but I think we don't have any pushback anymore, so probably this can be merged as well at some point. I will ping the maintainers for this.
And the last one is the… this one about OpenShift metrics.
yeah.
And after this, I guess we can close this issue and probably announce that first phase was… first phase is complete, and start thinking about stability.
Phase.
What do you think about this? Any comments or concerns, or…
sections.
**David Ashpole** 07:52 Sounds good.
Been a long time coming.
**Christos Markou** 07:56 Yeah, yeah, glad to see this, being completed at some point soon.
And, yeah, by the way, if we have… if you have, or, any… anything that…
you consider… we should consider them as priorities for stability. Yeah, we can start collecting them already.
And,
yeah, in the following months, I assume we will start discussing those, and we will start working on this. Probably, David, we can… you and I, we can, think on this and think how we're going to approach this stability.
effort. My, my main… so, for system, for system working group, we're a bit stuck, actually.
And, I think one reason is that we had been trying to stabilize the whole area at once, and this might not be a good idea. So, probably for Kubernetes, we can start small and say, for example, metrics that are
straight… super straightforward, not… not controversial at all. We can… declaring them as stable in a release candidate, and, start doing POCs in the collector behind the feature gate, to prove that these actually work.
And once we have something that works, we can do the release, and we can start using them already in the collector. This will
Provide great benefit for the users, because, yeah, having 5, 4, 10 metrics that are already stable,
will, increase the confidence to the project, I guess.
**David Ashpole** 09:43 Yep, and then we can do,
Yeah, I think that's a good approach.
We'll have to think about what the initial subset'll be, that we're… we think are not controversial at all.
**Christos Markou** 09:58 Yeah, yeah.
**David Ashpole** 09:59 But other than that, yeah, I like that.
**Christos Markou** 10:02 Yeah, and after this, I guess, anybody that, want to stabilize something, they are free to do it. I mean, we can do it, collectively, not necessarily as part of this
working group. For example, I think… this idea came to me because working on these, where is this? These OpenShift metrics, I thought, yeah, do we really need them, or do we really need them now? So, if we were to include them as part of the stability phase.
That will delay us a lot, and same for other metrics. So, we can keep these sort of things in development.
And then, if anybody wants to, actually start focusing on stabilizing this, yeah, they're… they would be more than welcome to do it.
But we should focus on smaller and more simple things first, I guess.
**David Ashpole** 11:06 Sounds good.
**Christos Markou** 11:07 Okay,
I think that's all I had. Yeah, let's see how these 3PRs will evolve, and I will try to push… to ask maintainers to…
For example, yeah, specifically this one, which is around for long, to merge this at some point, and yeah, we can wait for these two, because I filed them this week, so…
Probably folks, spend time in this yet.
Cool. Anything else?
**Stephen Lang** 11:42 Just a question. Why does OpenShift have its own set of metrics? Because all of those that were on the list, just there with the resource quotas, they're all just in…
Kubernetes as well.
**Christos Markou** 11:56 Yeah, probably, yeah, that's a good question.
**Stephen Lang** 12:01 at least all of those features are. I don't know if those specific metrics are.
**Christos Markou** 12:05 Cluster quota… cluster resource quota is a specific resource of, OpenShift.
So it's not part of the standard Kubernetes API, so I guess that's the reason that back then,
Led implementation to this direction.
**Stephen Lang** 12:24 Oh, okay.
**David Ashpole** 12:25 The thing is, like… That's a custom resource, right? Cluster quota?
Bye.
We could be here a long time if we're defining metrics for all custom resources.
I'm not… You know, like, now that we've done it.
It's fine. I think we should…
I know that CubeState Metrics has struggled for a long time to effectively
define ways to produce metrics for custom resources, so…
this is definitely something that I would not want to be part of the initial
Release candidate or anything, but…
because they already exist, I think putting them in the semantic conventions is a good thing.
**Christos Markou** 13:11 Cubesat, I don't remember, yeah.
does CubeState metrics, deal with OpenShift-specific?
resources. I think… I had seen, no?
**David Ashpole** 13:26 Oh, I didn't think so, I mean…
**Christos Markou** 13:30 I remember I have seen something, but I don't remember juggling.
**Stephen Lang** 13:44 I don't remember seeing anything OpenShift-specific. I know they've got the custom resource feature.
**David Ashpole** 13:48 What is it called? Cluster… Mr. Coda, yeah, there's nothing,
No hits for OpenShift or Cluster Quota in, CubeState metrics.
**Christos Markou** 14:01 Okay, probably, yeah, I don't know if there is any OpenShift, like, an extension or something that…
OpenShift installs.
Could be.
**David Ashpole** 14:12 I mean, I mean…
**Christos Markou** 14:13 Especially…
**David Ashpole** 14:13 Okay.
**Christos Markou** 14:14 Yep.
Okay, yeah.
In any case, we can…
**David Ashpole** 14:20 It's not like…
**Christos Markou** 14:21 It's a development thing, so… can leave it there.
**David Ashpole** 14:26 There is one, yep.
**Christos Markou** 14:29 It's a fork?
**David Ashpole** 14:30 statement. OpenShift still metrics.
**Christos Markou** 14:32 Yeah, yeah, yeah, probably that's it, what I had in mind. Okay.
Okay, cool. Anything else?
I guess that's all then for today. See you in two weeks. Thanks for.
**David Ashpole** 14:54 See you guys.
