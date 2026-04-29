SIG: K8s Semantic Convention SIG
Date: 2026-04-28
Duration: 39 minutes
Zoom Recording URL: https://zoom.us/rec/share/_1hyjMKIhemFLqjKso8oSczo2AuNlvnMrdjB7HvW75TpvbD1cVytCfN3ke_tawIE.pZ49kh-HVAWMdrMY
============================================================

## Zoom Recording Transcript

**Christos Markou** 02:21 Hey folks, I was just trying to remove the bot.
**João Marques Correia** 02:27 Ain't nothing.
**Stephen Lang** 02:29 Excellent.
**Christos Markou** 02:31 Let's wait a couple of minutes, and we can start.
Seems attended short today.
Hello?
**David Ashpole** 03:37 What is on our agenda today.
**Christos Markou** 03:45 I have added, one topic, we can discuss it here, mostly.
I wanted to raise awareness of the ongoing discussions, which is around When we should use container namespace for metrics.
Compared to the kh.container namespace.
So, the idea there is… was that Whenever something can be generalized on container level, we use the container namespace, but when it is something cage-specific, we use the cage.container namespace.
And there are several… I had filed an issue a while ago about revisiting the existing metrics that we have introduced.
And there is also another request, I think David, someone from Google is, asking for this to add some file system container metrics, and there the argument is if we should use, so there.
the kubelet exposes things like, the root FS file system, but also, the file system that the logs of the container consume.
But in con… in pure containers, in pure container level world.
We cannot, we don't have a… straightforward way to collect the usage of the logs. So, CAdvisor, for example, only exposes the root FS.
Usage and stuff. So, there is this ongoing discussion, something that we need to tackle.
But this is more or less the story. I don't know if you, Joao, or you, David, want to highlight anything.
But this is, in short, the summary, I guess.
**David Ashpole** 05:33 No, yeah, the only thing I would highlight is, the log.
usage of containers in particular is definitely something that's Kubernetes-specific, because it's measured as the amount of… Space used at a particular file path, which is defined by the container runtime interface.
in Kubernetes.
**Christos Markou** 05:54 Right. Just to note here, I think the metric was introduced in somatic conventions, quite… Recently, I think I introduced that. I chose the generic one by looking into Shedvisor. It seems the current implementation in Kubelet SAS Receiver uses only the root of S.
But I think now, based on the discussions, I'm fine, using the kh.container namespace for this one, use the attributes to differentiate the file system type.
And I think we could even deprecate the generic one for now.
And at some point in the future, if someone wants it back, for… to cover other use cases from other untang, we can consider it. But we can have this opinionated metric for containers, for Kubernetes-specific environments.
We mostly agreed on that. I think what is missing here is what we need to do for the old metric, if we should deprecate it or just leave it there.
Don't know, what do you think?
**David Ashpole** 06:57 Do you know how the cubelet gets its, container… file system usage? Is it… it may even be through the container runtime interface as well.
**Christos Markou** 07:07 this from C-Advisor and CRI, so I think, from what I saw and based on the discussions, could be equivalent from… equivalent to what Shadvisor exposes directly. So, container file system usage, it can be exposed from… can be derived from kubelet metrics, using the root effects part.
But also for pure containers from CAdvisor as well.
What is Kubernetes-specific is the logs, though.
So it's a bit weird how we want to design it, specifically.
We can always go for Kubernetes-specific based on this technicality, I don't see… Any need coming, quite soon.
For other runtimes.
they can always use their own, namespace, like, like Docker, for example, Docker namespace.
We can have the generic one as well back, which is only the root FS part. I don't see anything conflicting there. The only problem might be that we might have some kind of duplication, so the KH container file system usage for root FS will be essentially the same metric with the generic one, that we already have now. That only could be the problem, potentially.
**David Ashpole** 08:38 Yep.
Do we have a… Do we have anything for empty dir volumes today?
At the pod level?
**Christos Markou** 08:51 Don't think so.
**David Ashpole** 08:56 Maybe we'll add that in the future, then.
But yeah, I like the idea of going with something Kubernetes-specific that makes sense.
**Christos Markou** 09:05 For pods, though, that would be easier, because the namespace is GatesPod, anyways.
**David Ashpole** 09:12 Yeah, yeah, that would definitely be easier. It's more, I was just so… For ephemeral storage, you're supposed to compare the log usage and the writable layer usage to the container's requests and limits.
And then at the pod level.
You sum all of the container usage together.
And… add in empty dir usage and compare that to the pod-level requests and limits. So if you… if you were trying to… Like… Graph it either at one level or the other, that's what you would end up with.
But as far as container-level stuff, I think the current proposal is something I'm happy with.
**Christos Markou** 10:04 Okay, and I guess the same will apply for, yeah, we need to… I think one… one thing we need to do is to revisit, container usage metric, because it seems it's Kubelet-specific, the interval is derived from… it's something Kubelet does.
Same utilization, again, is derived from… but I don't think… we have KH utilization, nothing container utilization, so we're fine. And then, similar for memory. I think for memory, it's more straightforward, because we don't have this issue with usage and the interval that we use for calculations.
Yeah, by the way, there is a non-normative guide that we had introduced. I will share this On the issue that, describes the CPU, principles, the principles around CPU metrics, and what should be, optional, what should be required, and what's recommended. I'll post that on the issue, mostly for the user.
**João Marques Correia** 11:08 I tried to share a comment in the issue. I can try to summarize it.
Some trouble today, but In general, I feel like usage, especially how Kubernetes does it, maybe should be Kubernetes scoped.
Mostly because it has a fixed interval.
And so, that means using, like, so the formula itself is very common, even if, like, Docker probably is not exploring that value, but since Kubernetes enforces a 10-second window, let's say, for example, if you put a collection interval of 60 seconds.
it means you actually end up losing values, right, because Kubernetes only gives you the latest that it has computed.
And losing those values actually means you might lose understanding of spikes, of what exactly is happening, so it's not, like, super useful, I feel like.
for actually understanding the container behavior, it might be more like of a metric to probably understand what values the autoscaler can use to define the behavior and scale, like, the containers, but to track how the container is behaving, it might not be the most useful one, because again, a lot of data might be lost if you have a longer collection interval, because it's not like using time, and it has a fixed sampling window, but it's not adapting itself based on the collection interval. So… For me, that one, I feel like it should probably be moved.
For container utilization, if it doesn't exist, I actually forgot to check that. I feel like maybe that we should introduce one to align somewhat with an issue that was on the system metric side, where they have tried to introduce utilization to have a sort of simple metric.
That can be used to at least get, like, a general feeling, right? At least you can… like, seeing CPU usage in percentage tends to be very normal, right? Docker will export it that way as well, like, your system and all that sort, so it seems a little bit more natural, and at least it could be a more general way if you want to have a very quick dashboard, like a sort of presentation metric.
To have a rough feeling of what is happening could be useful.
Or some alerts.
And it's easier generalizable, because again, it's just a percentage. Even if the formula used, for example, Docker might not use the same computation way as, for example, Kubernetes might do.
I think in Kubernetes, we grabbed the usage right now, and I'm dividing it by the limit. So, whilst Kubernetes, I think it's… Docker would probably just do it in time, and then move it to, percentage-based, but again, it's still, like, a percentage that you can roughly see. Is it a 10%? Is it 90%, right? So you just get a very rough feeling.
of what the CPU level usage is, if that makes sense. So that one, I feel it might make sense to have at a marginal level, if they don't exactly mean the same thing, but it gives a rough… understanding.
I hope it made sense.
**Christos Markou** 14:22 I think, you know.
**David Ashpole** 14:23 Goodbye.
**Christos Markou** 14:24 we had, the argument that this is, again, something gate-specific.
I think the most critical part is that usage. It is derived also from usage, and usage is gauge-specific, so you end up with a metric that is also gauge-specific. And also, again, the limit that you should use can be controversial. You can use the limit of the container.
is the… of the… cage container.
And any other stuff, and it's not always easy to be sure that you can define the limits in a very unique way across different runtimes, because you need to check every single runtime, and how Docker defines the limits, and all that stuff, while in Kubernetes, it's quite straightforward. These are the limits, that's how we calculate this, and this is how we derive the utilization, essentially.
So I think that might not… be a good idea to revisit this. It is already settled.
**João Marques Correia** 15:23 Shit.
**Christos Markou** 15:23 hesitant to do it. I don't know what other… others believe, but that would be my week.
**David Ashpole** 15:28 Are they currently opt-in, or are they currently enabled by default, these utilization metrics?
**João Marques Correia** 15:35 definition sites.
**Christos Markou** 15:37 are opt-in, and these are the guidelines that some ad conventions also imply on.
within the implementation, kubelet starts receiver, it's… it's outdated, the implementation, but in any case, I think, they are also, disabled by default in an, well, yeah, since they were introduced. So, should be fine.
**David Ashpole** 16:00 In that case, I think we're following the semantic conventions, right?
**Christos Markou** 16:04 Yep.
**David Ashpole** 16:05 Was… is there something you… Xiao, that you wanted to have us change about what we're currently doing? Or were you just.
**João Marques Correia** 16:12 Okay, I felt like at least the usage, like right now, which is in container, I'm not sure if it makes much sense to share the Kubernetes value there.
Again, because, to… well, probably, like, a lot of other… actually, container runtimes probably won't contain… compute that usage.
But similarly, like, I feel the way Kubernetes does it might bring in problems, in the sense that you have a fixed sample window, right? Yep. That will not be adapt, or at least not adapt to the collection interval, and will lead to data being loose, right?
**David Ashpole** 16:49 I totally agree, but the current guidance is that that should just be opt-in, right?
**João Marques Correia** 16:53 I think it's Octane, yes.
**Christos Markou** 16:56 Yeah, but we use the container namespace for these, which might not be so accurate, because you use container usage… you… get this from something that Kubelet does, in a very opinion, in a specific way.
And we should enforce that all containers provide the metric in the same way.
Which is not possible, I guess. So, I think that what we have now is not correct. We should make it, KH container.
I don't know, Dmitry, if you have any insights why it was decided like this in the past.
**DA Dmitrii Anoshin** 17:30 I was talking about memory usage.
**Christos Markou** 17:32 container CPU usage.
**DA Dmitrii Anoshin** 17:35 And then your CPU usage.
**David Ashpole** 17:36 Which is a windowed usage over time, right?
**DA Dmitrii Anoshin** 17:40 Yeah, and it's pre-aggregated on Kiddler's site, and I guess that was taken just because of ease of use.
So users don't need to, like… Use time with roll-ups and, like, manual… Window aggregation, right? So…
**Christos Markou** 17:59 Yeah, but what.
**DA Dmitrii Anoshin** 18:00 Listen.
**Christos Markou** 18:01 name… we'll talk about the namespace. I think what is there is.
Okay, since we get it from Kubelet, maybe.
**DA Dmitrii Anoshin** 18:07 Oh, yeah.
**Christos Markou** 18:08 Change the namespace, that is there.
**DA Dmitrii Anoshin** 18:09 Why, though?
Because it's different?
**Christos Markou** 18:13 because it is generic, and it is container CPU usage.
that if I get this from Kubelet, might be calculated based on the kubelet's logic, and then if I have a Docker stats receiver, and I get this from the Docker API, do some sort of calculations, can be different, because…
**DA Dmitrii Anoshin** 18:33 I guess the assumption was that the logic is pretty much similar, but it might be a wrong assumption. So you're saying that Kubelet has different logic than Container Engine?
**Christos Markou** 18:45 Kubelet has a specific logic, and… My concern is that we cannot really ensure that all runtimes will have… will follow the same logic. I'm pretty sure that Docker has something else.
**DA Dmitrii Anoshin** 18:58 Yeah.
**Christos Markou** 18:58 Formula, it looks different.
**DA Dmitrii Anoshin** 19:00 I guess it was for consistency, because container, container CPU time would be pretty much the same value. There is not much logic to be added on top of that, but the window aggregation, right, can be different.
So, yeah, I guess it was, like, defined like that for consistency, just because container CPU time has pretty much the same value and the same logic, so we went with usage as well. And I, to be honest, I don't see a big problem with that.
**David Ashpole** 19:34 I probably also agree. I think even if the windows they choose are different.
Like, we should just document that, like, basically they're non-aggregatable.
Like, that people should use CPU time.
And that it's just, like… I don't know if it matters that much, is all I'm saying. It's like, if I'm looking for average CPU usage, then I'm already losing Like, I'm already not gonna have an accurate… number, if I try and do anything with it.
**DA Dmitrii Anoshin** 20:07 Right. We actually discussed this in an interesting problem in system semantic convention is that currently OpenTelemetry format doesn't provide you a way to specify a time re-aggregation window.
For… for a temporal aggregation, right? And sometimes it's confusing, for example, for this metric, for, like, if we have a native field, an open telemetry metric, for example, which would say the window.
where this metric was re-aggregated, it would be pretty fine… pretty good, right? We can add different values on that field.
from Docker and from Kubelet, if we knew what was the value in the kubelet.
Because it's one use case here, but in system it's much more. It's, like, load over 15 minutes, over 5 minutes, and everything, and we would like to actually, like, provide users that information in some way. So if we had that thing, potentially we can discuss it in Open2Emity spec, meeting. If we had that field, I think that would actually solve this problem as well, from my opinion.
No, I think.
**Christos Markou** 21:21 So we are saying that it's fine to keep it as is today?
If we ensure that the definition is clear, and we explain how it is, calculated, essentially by Kubelet, and ensure that what we document… what we define there is actually what Kubelet… the logic that kubelet follows, right?
**DA Dmitrii Anoshin** 21:40 Yeah, I think the difference in the value is not significant, it's just different aggregation window, right? So, I don't believe it warrants having a separate metric for that.
**Christos Markou** 21:53 Yeah.
It can be, because it is… what we get from Kubelet, it is fixed, and the period is fixed, based on what Kubelet decides. But if, for example, I have Docker starts receiver and kubelet starts receiver enabling the same, let's say, metric.
Or… anyways, these different metrics end up in the same backend.
The internal might be different, and… in that case, the numbers that I would see would be inconsistent.
**Stephen Lang** 22:24 Because the island phase, though, right?
**Christos Markou** 22:27 Sorry, what.
**Stephen Lang** 22:27 even if you had a fixed interval, and say you knew it was 10 seconds, and you had this rolling window, it's not necessary that your collector, receiver, or whatever is going to be within the same phase. You know, you could be collecting at 9.
**Christos Markou** 22:41 Different phases.
**Stephen Lang** 22:43 You could either drop into the previous collection or the next, so…
**João Marques Correia** 22:47 Oh.
**Stephen Lang** 22:48 Yeah.
**João Marques Correia** 22:49 There is a slight difference, I feel like, because… if I understand correctly, because in one case, let's say if I collect at least if we can manipulate the collection, or at least the interval, right? I could collect one value at point A, a different value, like the clock value, so I'm talking about time first, right? At point A, at time A and time B, and those values are absolute, right? So they are always correct, like, they will always show everything.
And then I can just basically do the difference between the wall clock time at time B minus time A, right? And at least I get, like.
I get all the data that happened within that time frame.
The problem with how we do it with Kubernetes, right, with Kubelet, is that it's always doing that calculation every 10 seconds.
So, if I'm collecting, let's say, every 60 seconds, there should be, like, 10 values that Kubelet computed, right?
But I'm only grabbing, let's say, the last one of them. But maybe the spike happened during 30 seconds, but that value is lost, because I'm just seeing the change that happened in the last 10 seconds, and not what happened before.
**DA Dmitrii Anoshin** 24:03 It…
**João Marques Correia** 24:03 Is that…
**DA Dmitrii Anoshin** 24:04 I think the aggregation window for QBlit is much higher, it's 60 seconds, or something like that. In that case, you will see the data, it's just, they will be kind of spread across last…
**João Marques Correia** 24:17 it's 10 seconds. I feel like Kubelet is doing, like, the housekeeping. There's, like, a loop inside it that either calls CAdvisor or will call the container runtime, depends on how it's configured. I think it's, like, 10 seconds that it's pulling a new value. It's just that kubelet has a ring with multiple values, but the stats API that people that receiver uses only reports the last value. So when you put in DPI, you get the last.
Kubelet has much more information, but it only gives you the last one that has that last 10-second window.
**DA Dmitrii Anoshin** 24:50 Right, it's the last one, but the aggregation on cube website, I'm pretty sure, is pretty higher, because otherwise, the metric will be very spiky, and I have… I never saw that metric to spike a lot. So the aggregation… temporal aggregation window must be much higher than 10 seconds, I'm pretty sure about that. Because if you… if you run this kubectl usage, what I recommend.
It would never.
**João Marques Correia** 25:14 For a spot.
**DA Dmitrii Anoshin** 25:14 It would be, like, showing you, like, very gradual change. So that's a difference.
**David Ashpole** 25:20 metric here. It… so that metric is served. So the way that that metric, if you do, like, kubectl top.
The metrics server fetches metrics from the kubelet using the kubelet Resource Metrics API, and that returns cumulative counters for CPU.
And then the metric server is doing the rate computation based on its collection interval. So, changing the… Resolution of the metric server fetching will change.
the window of the resulting average CPU usage metrics you get from kubectl top.
So, I guess Kubernetes has followed this guidance as well, and does not use the windowed metrics. It does the rate computation properly in the…
**DA Dmitrii Anoshin** 26:05 Understood.
**David Ashpole** 26:06 In the server side.
**DA Dmitrii Anoshin** 26:08 And in that case, the kubectl command itself applies some temporal aggregation, because I don't see the spikes there. Okay, I see.
**David Ashpole** 26:18 it's… it's… Usually, I think the default metric server collection interval might be 60 seconds or 30 seconds, so that's… it's whatever window it's using.
**DA Dmitrii Anoshin** 26:27 Okay, okay.
**David Ashpole** 26:29 You tune it based on how large your cluster is, and…
**DA Dmitrii Anoshin** 26:32 Makes sense.
**David Ashpole** 26:32 how much CPU you want to spend on the metric server.
**DA Dmitrii Anoshin** 26:35 Interesting.
So, yeah. We're not just exposes something that doesn't even use it itself.
**David Ashpole** 26:42 No, no, it's, it's, like, Kubernetes considers this Uber Legacy.
And does not recommend people use it.
**DA Dmitrii Anoshin** 26:51 Interesting, okay, that's a good point.
**Christos Markou** 26:53 Isn't it used by eviction something, or, another controller that… actually, whenever this controller, Fetches this metric, that's when the update happens, and this is how the interval is.
**João Marques Correia** 27:09 Agent.
**Christos Markou** 27:10 That's what I found last time I checked.
**David Ashpole** 27:13 The… you're right that the eviction manager runs, it usually runs on a… 30 second interval?
it does do an on-demand fetch of metrics, but keep in mind that eviction is only done for memory and disk space. So it may be driving the CPU rate calculation inadvertently, but the goal is just to get very fresh memory metrics, mostly, so that it can Respond to memory pressure reasonably fast.
**Christos Markou** 27:43 Yeah, yeah, in any case, I think we can always, look for it and find it and share it here, but… I think, in general, this discussion shows that it is a very opinionated metric from Kubernetes, and if we are fine defining what Kubernetes does under container namespace, and say that whoever wants to use this metric should take this definition into account.
Or we just make our lives easier, and we say we do it cage-specific, so it's cage.container.usage instead of containerusage.
See these two options, but we can discuss it on the issue you prefer, because we are running out of time here.
**David Ashpole** 28:28 Just to confirm, like, we do actually want this metric in some form.
Because the other option is, we just don't have it, and we tell people to use the cumulative one, or the, like…
**Christos Markou** 28:38 Just the CPU time.
**David Ashpole** 28:40 Non-widowed my training.
**Christos Markou** 28:42 Yeah.
**David Ashpole** 28:43 Yeah, I…
**Christos Markou** 28:45 That's an option as well. We have container CPU time, which is generic, it's easy to retrieve, whatever you use.
Yeah.
**João Marques Correia** 28:57 The only counter-argument… and again, it depends on what we would prefer, but there was a push in the system metric side at some point. There was an issue there, to have at least one presentation and somewhat simple metric to be able to use, where you don't need to account, like, for, you don't need to do… basically any formulas, like, you don't need to compute the rate or anything like that, you can just query that metric and have, like, the dashboard running. So, again, I'm not sure if that's something we want to consider or not, but looking at the system metric side issues.
that was a push that they had. So, either usage or utilization, it's kind of what it's doing, right? It's at least giving you some sort of very simple presentation metric that you can check.
Without having to computer-grade or anything like that, but again, I guess just something to consider.
**Christos Markou** 29:49 I think it is covered by the generic guidance that I mentioned before, how CPU measures should be calculated, and the argument there is explicitly that if something, you can derive it directly from Kubelet, and it is kubelet-specific or environment-specific, you are free to do it.
So something that is usage based on logic that kubelit implies, then it is… should be namespaced under the KH namespace. Same for utilization.
If this domain sees this as useful. The guidance is also that these metrics should be opt-in, and only CPU time should be, required.
I'm not sure if we want to go this, you know, aggressive and remove all those.
But definitely we need to do something, or… because what we have now seems problematic, or unclear.
I talk about the container CPU usage metrics specifically.
**João Marques Correia** 30:51 Oh.
I guess, maybe just to make it clear, my stance would be to move it as well to the Kubernetes namespace. I feel at least we get to keep it, it's opt-in, and at least we are able to document, I guess, the Kubernetes caveats there more easily, but… again, if we document them in the container namespace, it would also be possible, but then it just opens, let's say, if Kubernetes has some caveats, we are documenting them there, and then every runtime that potentially could use that would also be documenting, like, a lot of caveats in the same metric, but… So yeah, my preference at least would be to move it.
**DA Dmitrii Anoshin** 31:25 I'm actually surprised that that metric is discouraged from being used. Not the metric, but, like, a source for that data in Kubelet. Potentially, we can just ignore it and compute it from the cumulative, and use collection interval instead, right?
**David Ashpole** 31:41 We could, if we want to.
**DA Dmitrii Anoshin** 31:45 In that case, it'll be aligned with Docker.
**João Marques Correia** 31:49 Okay.
So, your proposal would be to… we compute it based on time and the collection interval based on… on the kubelet set receiver, and then basically report it again in that case through the container namespace, right, because then it becomes more general. Is that the case?
**DA Dmitrii Anoshin** 32:07 I've suggested something, but I don't know.
**João Marques Correia** 32:09 Yeah.
**DA Dmitrii Anoshin** 32:10 100%, happy with, because it's gonna change, it's gonna be another kind of breaking change that we need to somehow, like… propagate to the users, right? Because they will see, like, metric being stable, now it's spiking all of a sudden, so they would need to apply some temporal aggregation on top of that, which will be even more confusing, so I don't know. But I don't like moving it to a separate namespace, because it's gonna be, like, just a pres… precedence that we never had before, kind of, we don't have any CPU usage in Kibrosis namespace, and now we have one.
And, if we don't have anything else like that, like times, file system, or memory, it's gonna be kind of awkward.
and given that that data source isn't recommended to be used at all, so I'm just throwing, like, other ideas.
And, I don't know, maybe we can even just depregate it in general, or something.
**Christos Markou** 33:10 Yeah, I would prefer to remove it entirely if we have to reinvent a specific formula and force everyone to use this formula.
That makes our lives easier.
**DA Dmitrii Anoshin** 33:21 And also, we don't have it… we don't have it in system. We don't have usage there. We have time and utilization.
**João Marques Correia** 33:27 intersectional.
**DA Dmitrii Anoshin** 33:29 This kind of matrix is off already.
**Christos Markou** 33:34 Yeah, the only argument was that since Kubelet provides that, we get, we get it directly.
And it was also useful in cubelet starts receiver, because you can divide it with a limit and get the utilization.
**DA Dmitrii Anoshin** 33:47 Excuse me.
**Christos Markou** 33:47 get the limit and get, like, an estimation how close you are to the limit. I'm not sure if this calculation is used, though, actually, by the Kubernetes system itself.
We need to check it. Show usage is not used entirely.
**David Ashpole** 34:02 Which is never used anywhere, yeah, I can… Anywhere.
**Christos Markou** 34:04 Okay.
**David Ashpole** 34:05 Whatever, yep.
**DA Dmitrii Anoshin** 34:07 Boom.
**Christos Markou** 34:07 Okay.
**DA Dmitrii Anoshin** 34:07 Should we investigate what's the, like, long-term plan for that from Cobrata's standpoint? If it's gonna be deprecated and removed in future, I think we should…
**David Ashpole** 34:21 I mean, I'll tell you the most recent discussion, but it's not, like, has nothing to do with this metric. So, let's see, who remembers Sergey?
**DA Dmitrii Anoshin** 34:32 So…
**David Ashpole** 34:33 The K, Sergey, used to be on the GC.
So, him and I hilariously swapped places about… four years ago, because I was working in Kubernetes on Signode, and he went and now does all the things that I was doing, and I came to OpenTelemetry.
But… Basically, they are looking for a new owner per se advisor.
And they wanted OpenTelemetry to own it.
And I don't think anyone from OpenTelemetry is that interested.
And so, now what they want to do is to remove CAdvisor entirely from Kubernetes.
And remove all of the stats APIs.
Entirely.
They tried to do the CRI stats thing, where they get some small set of them from the CRI, and those will probably stick around, but that's just very basic stuff.
So, the latest proposal that I had heard was they want to remove it all.
But… and hope… hope that something springs up to replace it.
But I don't think they're planning on trimming… when I was working on it, my goal was to Try and trim metrics around the edges, but it's just so hard because there's always someone who's depending on them, and there's no easy way to like, especially as a Kubernetes provider, like GKE, there's no, like, way to ratchet down the number of metrics you support without just breaking a lot of integrations. So, that's why this metric still exists, even though all the Signode people have hated it since it was added in, like, 1.2.
**Christos Markou** 36:16 Based on this, we also… we don't only have this metric that is affected, we also have… every single Kubernetes utilization metric that we have in the receiver, but also already in smart conventions, that is Based on these so, either we, arrest them all at once, and keep on the CPU time, or we.
You need to decide what to do.
Essentially.
**David Ashpole** 36:44 Yeah, I think that if that happened, it would be a bigger can of worms than just this metric, but there's nothing special that they're planning for this metric.
And I think they're… they're trying to decide if they… Yeah, the Resource Metrics API, which is the one that would stick around, only has, cumulative CPU time.
It doesn't… it doesn't have any of the, windowed stuff.
**DA Dmitrii Anoshin** 37:12 Interesting, that's good to know.
Is there any, any, like, discussion in open space around that?
Or just…
**David Ashpole** 37:21 refund.
**DA Dmitrii Anoshin** 37:23 Thank you.
**David Ashpole** 37:45 I think they came to the collector seg at one point.
It's fine. Or maybe…
**Christos Markou** 37:52 Oh, the C-advisor thing, the generic discussion.
**David Ashpole** 37:55 Yes, so here it is.
**Christos Markou** 37:58 I think also Bryden, shared that at some point with… Collector, maintainers, approvers.
**David Ashpole** 38:09 Yep.
There it is.
**DA Dmitrii Anoshin** 38:31 I posted it in the chat?
**David Ashpole** 38:33 I… oh, sorry, I put it in the, Meeting notes.
**DA Dmitrii Anoshin** 38:37 Okay, thank you.
Yeah, I think… We probably need to somehow align with the plans and conferences and see.
Yeah, given that it's gonna be potentially either removed or kind of handed over to… us, I guess. I'm not that opposed to moving it to a separate namespace at this point, but at the same time, if it's gonna be removed, potentially, maybe we just can deprecate it.
Sorry.
**David Ashpole** 39:19 We are overtime, so if there's anything else…
**Christos Markou** 39:23 Yeah, continue on the issue.
**David Ashpole** 39:25 That's spec sake.
**DA Dmitrii Anoshin** 39:27 I'm sure.
**Christos Markou** 39:28 Thank you, folks. See you next time.
**João Marques Correia** 39:29 Bye.
