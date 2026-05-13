SIG: K8s Semantic Convention SIG
Date: 2026-05-12
Duration: 38 minutes
============================================================

## Zoom Recording Transcript

**Christos Markou** 05:19 This time, we were bombed by… bots. I had to remove two.
Let's see if anyone else is joining, and we can start.
Steven, are you going to Global Mobility Summit?
**Stephen Lang** 06:08 Yeah, next week.
**Christos Markou** 06:11 Nice. Is it, which state is it?
**Stephen Lang** 06:15 Minnesota.
Yeah, it was a bit of a last-minute thing. The original speaker couldn't make it.
So, yeah, bit short notice.
Are you gonna be there?
**Christos Markou** 06:31 No.
Yeah, it's getting harder to travel to the US.
Yeah. So it's mostly, I guess, European ones that I will be going.
Probably.
I guess unless you have a talk, right? But you have a talk, so it's easier.
**Stephen Lang** 06:52 Yeah.
It's sponsored as well, so… that helps.
**David Ashpole** 07:11 Hey, folks.
**Christos Markou** 07:13 Hey, cool, so we can start.
**David Ashpole** 07:17 Yep.
**Christos Markou** 07:17 Yeah, I will just share my screen, just to… I'll share the agenda.
**David Ashpole** 07:25 Add yourself to the attendance list.
**Christos Markou** 07:28 Yeah.
I just started… two, topics.
We have already quite, involvement there, all of us, most of us. So, yeah, it would be nice if we can come to a conclusion regarding the CPU modes.
So I think the main… the main… Let's… the… what is missing here is to decide if we want to… Slightly mention in the notes that, there is this very small discrepant, difference between system and user, modes.
Compared to total, I'm fine. I mean, I'm… either way, I am fine with both, options. We don't explicit… the idea that I had here is to not explicitly add other in CPU modes.
But kind of mention it here in the notes, so as to, Keep the door open for any implementations that might need.
To… might want, or might decide to do it.
I don't foresee, actually, anyone doing this, at least soon.
Docker starts receiver is not super active. If they decide to do it at some point, it's on them. But yeah, we need at least something now to show us to proceed.
So, I don't know if we want to discuss it now, or if we want to continue the discussions on the PR.
But I guess that's the only one pending, to resolve this one.
David, since you were, you had opinions there? What do you think?
**David Ashpole** 09:21 Is… this is just about the… Yeah, I don't… I don't think we need this, CPU mode other. I thought we discussed that that was, like, in practice, essentially always basically zero. I'm okay adding it if it turns out to be meaningful.
But if it's just, like, a rounding error, then… I don't think it's necessary.
**Christos Markou** 09:50 Yeah.
I agree, I know we decided this one, so… I definitely don't want to add it as, like, an enum value.
But I thought that maybe we can just mention it in the notes, like, in theory, that this thing, happens.
So as to be fully transparent and not maybe hide anything. That's how I felt, but if we agree on completely removing this section… So, essentially, we're talking about this section here in the notes.
If we agree to remove it completely, I'm also fine.
But, yeah.
**David Ashpole** 10:31 I think the question in… If we want to leave a note, that's fine, but if… If we decide that we're not actually going to use it in any of our implementations, then it doesn't seem very useful to put in the notes. Like, it'll just mislead someone in the future.
**Christos Markou** 10:46 Yeah, we don't…
**David Ashpole** 10:48 It's okay documenting that system plus user can be less than total. I think that's reasonable.
**Christos Markou** 10:54 Yeah, I think we definitely don't gonna use it, in KH implementations.
But I don't know what others want… would decide to do in Docker Stats Receiver, for example.
And if they will decide to be extremely accurate or whatever, for any reason. Potentially, we can just remove it now, just mention that there is small difference.
And if they decide to come back and implement it in another way, the way the semant conventions work with enums say that if, one of these values is applicable, use this one. If you want to add an extra one in the implementation, it's okay to do it. So, it's not gonna be something breaking.
Technically. Even if they decide to do it later.
Okay, yeah, I don't know, I can remove it, if that's… Preferable, if it's less confusing then.
Okay, cool.
And… Okay, and the next one… Anything else on this one? From anyone?
No.
Okay, and the next one is, maybe if we can, get back to this one and… maybe… Again, come to a conclusion.
We discussed last time about, how… CPU usage is controversial, and that it's not actually used anymore.
In Kubernetes, in general, so… I… my first idea was, then maybe we can remove it.
But then what happens with the utilization metrics?
But then David also suggested that maybe we can keep utilization metrics for convenience.
And… this is actually what also Host metrics receiver is doing, calculates the, the delta on the fly, over the, scraping window.
And, yeah, here it… we don't divide by the limit, because the limit is always one, because we do it per core, but in Kubernetes, I guess we should… we will divide it by the limit. So… Yeah.
I don't know, what do we think as a group?
First question is.
Are we okay with removing usage? Should we remove, actually, usage entirely, since it is kind of misleading or controversial?
For containers, pods, and nodes. And then, just calculate utilizations.
within our implementations, on the fly. Yeah, that's it.
Question.
**Dmitrii Anoshin** 14:01 Do we currently, calculate utilization based on time?
**Christos Markou** 14:08 Currently, we divide, CPU usage as we get it from, Kubelet, and we divide it with the limits, Limits, or requests, or whatever.
**Dmitrii Anoshin** 14:21 Yeah, we need first to see how utilization would be updated, and then… I mean.
My point is, let's figure out how we transition utilization first.
Open, if you… I guess transition, transition and utilization?
It's, probably… Should be done anyway, regardless of the decision we are making for the usage.
So we are aligned.
**Christos Markou** 14:51 yeah.
**Dmitrii Anoshin** 14:53 host metrics as well, but that's my opinion, what do you think?
Does make sense.
And also, we are…
**David Ashpole** 15:05 Sorry, go ahead.
**Dmitrii Anoshin** 15:07 Yeah, I just want to say, we are removing… we're thinking about removing the usage because it potentially can be removed from the… from the Kubernetes API, right? This old deprecated metrics API, right?
or resource, I forgot how it's called.
**Christos Markou** 15:28 deprecated, it's not used, and… Based on our discussions, it's super controversial.
Or, you know, confusing.
**David Ashpole** 15:38 Which one? Sorry?
**Christos Markou** 15:40 the usage.
**Dmitrii Anoshin** 15:42 Gotcha!
**David Ashpole** 15:42 Okay.
**Christos Markou** 15:43 mechanism.
**David Ashpole** 15:44 Don't use that for anything.
**Christos Markou** 15:46 Yeah.
**David Ashpole** 15:46 I think… we're all… we're talking about opt-in metrics, so I feel like… Even if there's some caveats to them, like, I'm not… super strongly against making them included as opt-in. I feel like utilization can be very useful. Like, it's… we're doing quite a bit of math for users, so… I can see someone wanting to turn that on and put it in a dashboard.
usage, I feel like, is less useful, because Like… the… the actual query change is, like, almost nothing in most… like, the prom QL to get the rate.
from a counter is not very difficult. I assume it's not hard in other systems.
I think we definitely shouldn't use the windowed value from the qubit. We should compute it ourselves for all of them, regardless.
And then… I'm I'm not super opinionated on… whether we have… Just utilization, or utilization and usage.
As opt-in metrics.
As long as they're computed from the diff, like the host metrics receiver snippet did that you showed.
**Christos Markou** 17:04 Okay, okay, I see. Cool. I can then write this down. We can start, probably, with the utilization.
Yeah, since the intention is to move away from what Kubelet provides for usage.
I guess we can decide if we want to do the calculation as well, but another thing to consider here is the fact that what host metrics receiver does, it could be nice to have alignment there, and if host metric receiver is going to provide CPU time and utilization.
We can do the same, and also reduce the amount of things that we maintain.
Because it's also easy if you, emit CPU time, they can do the rate and get the usage, if it's useful. But utilization is, like, a convenient thing to provide. And also, it's less braking, because now we have Removing all of them at once would be quite intrusive, I guess.
Okay, yeah, I agree, we can start with maybe the implementation and see, what we do with the spec then.
**Dmitrii Anoshin** 18:15 I'm curious to see how value is gonna be… gonna change, because if you calculate it based on usage, it means that its utilization currently is pretty spread out over some unknown time window.
Like, no, not sorry. It's, kind of… Aggregated over one time… one window, which we don't know.
And it's… it's… it's pretty smooth, right? But if we transition to time, and we are taking into account only window from the previous collection, it's gonna be… it's gonna change significantly. It will be pretty spiky, right? Compare… which is fine, we potentially can document that, but… This is some kind of an exercise when you need to… Run and provide users, like, More details about this.
**Christos Markou** 19:08 Yeah, we can definitely compare it and see, how it looks like, based on different windows, but… after all these discussions, I tend to, conclude that… What we were doing was kind of wrong, because we get a random metric that we don't know exactly what is the, you know, the interval, and then no matter what is your interval and the collection time, you do things, so maths will be very weird.
**Dmitrii Anoshin** 19:34 Right.
**Christos Markou** 19:35 On top of this.
**Dmitrii Anoshin** 19:36 So, my point here is that users might be already Used to this, like, smooth.
utilization representation, right? And if we align it with the open… with the host metrics receiver right away, it'll be based on the collection windows only, and it will be spiking. So, maybe… I agree, we need to make them consistent. We need to provide the safe calculation on the host matrix receiver and then the kubelet.
But maybe we, can have another… Let's say, configuration option.
To specify that window.
For, for the temporary application.
**David Ashpole** 20:22 We… we can't, though. Or, like… I guess you're saying that you could choose a window that's longer than your… Collection, because obviously, like, if you're collecting it every minute, you can't have a… 10-second window, like the summary API currently.
**Dmitrii Anoshin** 20:36 Yes, you can… you cannot make it.
benefit me.
You cannot make it… I mean… Like, probably it will not change anything from the representation, right?
If you change it to lower.
Well, I mean, math will stay the same, it just will not change anything, essentially, as far as I understood. But if you make it longer, right, we probably need to accumulate more state in the receiver, but we can provide users an option to Whoa.
Like, keep the same representation.
Of utilization metric for keyboard receiver.
If they know what qubit window.
what Kubelet uses for the window.
**David Ashpole** 21:22 Right, so it's… I think it's 10 seconds.
But the issue is, like, if your scrape interval is 25 seconds, like, there's no… it has to be, like, a multiple for it to work properly. Like, if you scraped every 5 seconds.
You could do a 10-second window, because you would have a point every 10 seconds, but… it relies… like, it… I feel like it's too specific.
Do it with a feature gate, and give it a long time, and if people.
**Dmitrii Anoshin** 21:54 Okay.
**David Ashpole** 21:55 Notice or care, then we can reconsider, but…
**Dmitrii Anoshin** 21:58 Oh, I see what you mean.
**David Ashpole** 22:00 Like, you would have to have a scrape window of 5 seconds to be able to do a 10-second window, because you need.
**Dmitrii Anoshin** 22:06 Understood.
**David Ashpole** 22:07 To line up, yeah.
**Dmitrii Anoshin** 22:09 to saying that on the kubelet's side itself, the measures are more frequent.
But how that metric is exposed, it's, like, those measures are aggregated in the state of the kubelet metric server itself.
**David Ashpole** 22:28 Right, in the… Okay. Yeah.
**Stephen Lang** 22:31 If users want control of them, then they can do so at query time with the time metrics.
Yeah. And then they can choose.
**Dmitrii Anoshin** 22:40 Makes sense. Yeah, maybe that's a complication, and will be pretty confusing to implement. We can… We can go with FeatureGate and see.
**Stephen Lang** 22:51 Yeah, just represent the… or just document that the utilization metrics are kind of you know.
Taken as is, at face value, and then if you want more control over the calculations, you can You know, use the time metrics instead.
**David Ashpole** 23:06 Yeah.
It's actually a nice property that comes out of this, which is that if we're essentially calculating a delta.
When we compute the usage and use it for utilization.
than someone who literally has the delta, or the… Like, who takes a rate over the… original time metric will get the exact same value, right? So, today, that's not the case, where you can, like, do a rate over your CPU.Time, and look at the usage, and they'll be different.
Because they're over, like, misaligned in different windows, but if we make this fix, then actually they will always match.
Assuming you're at a resolution where You can see all the… Like, where you get the granularity to be the same.
But anyways, it sounds like we'll… we will do a feature gate, is that… The conclusion? Or there's gonna be a feature gate anyways.
Yep.
But we can do… we can make sure that the change is feature-gated in some way.
**Christos Markou** 24:19 Depends if we want to introduce it earlier, the change in the implementation, before we are going to change the SMAT conventions.
If we want to test it early, then we need another pair of feature gates, maybe.
**David Ashpole** 24:36 Is it, yeah.
Is this… actually a change in the semantic conventions, like… Do we say specifically that it's computed from field X in the summary API?
**João Marques Correia** 24:48 Right now, at least… wait, for… it depends, because for pause, there's nothing. For containers, there is, right? So for containers, it might not need a change.
**David Ashpole** 25:04 Okay, cool. I was just curious. I don't think it changes too much.
**Christos Markou** 25:12 Okay, yeah, we can, yeah, I will update the issue, mention that, in order to proceed with it, we need to first check the implementation.
Compare the results and see, what we think about it.
Sounds like a good plan.
**Dmitrii Anoshin** 25:33 Actually, can I bring back what I originally said? I think there is some misunderstanding. I looked at this CPU usage metric from the user perspective.
And it seems like there is a time average aggregation applied over a longer window than even the collector scrapes it from, even longer than, like, one minute.
Because if you look at that metric, it's pretty… It changes pretty slowly.
So, I don't know details about the implementation of the Kubernetes.
On the QBlood side.
But it seems like the window that aggregation is applied, like, around maybe 5 minutes or something like that. David, is it wrong assumption?
**David Ashpole** 26:24 Yeah, that's not correct. It's… the diff is calculated over a 10-second window, from what I remember.
I'm actually looking at it right now.
**Dmitrii Anoshin** 26:34 It's calculated over 10-second window, but is there, Time aggregation.
With average, like, sliding window aggregation.
**David Ashpole** 26:49 There's no, aggregation.
**Dmitrii Anoshin** 26:52 Oh, really? Because it, like, if you look at the time, and you try to apply rate to time.
like… rate, to the time metric. It'll be much spiky.
than usage. Usage changes slowly.
**João Marques Correia** 27:12 Problem with usage, at least right now, if you look at it, is that you might have some data loss. So, for example, some of those spikes, you might be losing that data if you have, like, a big enough collection interval, if that makes sense.
Because, again, like I explained last time, since it's doing it every 10 seconds, right, if you happen to collect your data in a moment where the pod might have less activity, then it will basically stay at that baseline, if that makes sense. You might lose some of the activity from the way it works right now.
Not sure if it makes a lot of sense or not, but basically, the summary would be, right now, the way it works, if you put, like, a long enough collection interval, you are definitely losing some data by querying that value.
**Dmitrii Anoshin** 27:59 No, I understand.
**David Ashpole** 28:00 Interesting, though, because… I need to figure out what happens if it comes from the CRI, because if it comes from the container runtime interface, it's possible that Docker is serving it or something, and it's doing… Something like that.
Let me double check, I've almost found the… The code that implements this.
Been a few years.
**Jina** 28:50 Is the window you're in question the housekeeping interval of the C-Advisor?
**Dmitrii Anoshin** 28:57 Right.
**David Ashpole** 28:57 Yes.
**Christos Markou** 29:08 One concern here is that… In this way, what we have today is, like, we completely rely on what we're getting from an external service.
Could be much cleaner if we just know the internal intervals and everything.
And we don't rely on how things are done on a different thing.
**Dmitrii Anoshin** 29:29 Of course, yeah.
**Christos Markou** 29:30 Hmm.
And also in alignment with, other components, like host metrics receiver.
**Dmitrii Anoshin** 30:26 Now I'm looking at the charts, with the usage and time, and it's… It's less spiky, but not to the extent that it would… imply… Long rolling window.
So, yeah.
**David Ashpole** 30:49 you know.
I found it in CAdvisor, and it just does a diff with the previous… whatever the previous stats are that it had. So… Like, each time you… actually, each time you scrape No, each time the eviction manager runs, or… Every time the housekeeping interval goes.
It… It recomputes the… cumulative CPU usage from cgroups, and then compares it to the most recent one.
So it should be 10 seconds, because that's the housekeeping interval.
Yeah, it is a little… This would be hard to write down in the semantic convention, I guess. It's 10 seconds, assuming that Kubernetes doesn't… Decide to change it.
**Jina** 31:41 What if we moved container.cpu.usage to caters.container.cpu usage and put all this No answer there, that this is specifically You know, tied to the… interval, which is set in your Kubernetes cluster, and we suggest you set your collection interval for this metric, same as that interval if you want to use it. Otherwise, use the time metric, and just go, like… Wait a second.
**David Ashpole** 32:08 That would work, it's just, I feel like you end up with a worse metric than we've been talking about by just using our collection interval.
Like, it just misses data otherwise.
**Christos Markou** 32:22 That was the original idea, actually. That's where the debate started, to rename it like this.
**Dmitrii Anoshin** 32:32 Cool.
**David Ashpole** 32:33 Love that, but…
**Dmitrii Anoshin** 32:36 David, based on your description, it means that if we have 10 seconds collection interval on the collector side.
It would mean that time and usage would be the same.
Right? If it just compares the diff between previews.
Or if we… I don't know, like, but if it's 10 seconds, specifically, it should match, right?
If we… Go ahead.
**David Ashpole** 33:09 Yeah, it will match.
Do we get the… Does the summary API include the timestamp at which the metrics were collected?
The only other wonky thing here is that the housekeeping interval is not… is not tied to collection, so you're getting… the stat… the summary API serves metrics that are Up to 10 seconds old.
**Christos Markou** 33:37 There is a timestamp, but I'm not aware.
**David Ashpole** 33:40 Okay.
But regardless, if you… if you queried it every… If you queried it every 10 seconds.
There is some jitter that's added intentionally.
So it's… It's not always going to be.
the same?
But it's mostly going to be the same.
**Dmitrii Anoshin** 34:02 Same.
Can I… can I share my screen quickly?
**David Ashpole** 34:07 Sure.
**Dmitrii Anoshin** 34:09 Just, just curious.
So… This is what I get, the dime one is spiky.
**Christos Markou** 34:21 We see a chat, not, Zoom.
**Dmitrii Anoshin** 34:25 ASSM? Okay, sorry.
Let me… Let me stop sharing.
Oh, sorry.
Okay.
**David Ashpole** 34:58 Oh, I know what's happening. Okay.
So, depending on whether your container runtime ends up using CAdvisor, or whether it ends up using That's actually really funny.
So the kubelet doesn't even have consistent behavior here.
It's the… This container runtime interface.
The cube… if the cubelet gets its metrics from the container runtime interface, it uses a 10-minute window.
And if it… Gets it from the… If it gets it from C-Advisor, C-Advisor always uses the housekeeping interval.
**Christos Markou** 35:46 It's shown, interval, right? She advises.
**David Ashpole** 35:50 10 seconds.
**Christos Markou** 35:51 Yeah, and the other one is based on the eviction manager, whenever it is called the API from the Eviction Manager.
Okay.
Both should be 10 seconds, though, or… Anyways, I don't remember.
**David Ashpole** 36:08 The eviction manager's every 30 seconds, but the… basically, C-Advisor has its own interval, and then the eviction manager comes in and overrides it.
**Dmitrii Anoshin** 36:16 Oh, okay.
**David Ashpole** 36:17 it wants fresh stats. But all that is to say, like, the kubelet doesn't actually have a consistent, Interval that it computes it over.
If I'm reading this correctly.
**João Marques Correia** 36:33 There's also one thing, I think it's called a metric server that is used for the autoscaler. I think it also computers the usage, but I think on a 15-second window, and that's also doing it based on time, if I remember correctly. Like, it's pulling the time.
And then doing it based on a 50-second window, so I guess we could potentially just use… I guess the formula's unknown, but I guess we could just go based on that if we wanted to.
**David Ashpole** 36:58 The metric server is configurable, though, from what I remember, so it's not like… It's not like we can pick a time and then match it. We could match its default if we wanted.
**João Marques Correia** 37:06 Yeah.
what I mean is we can, I guess, grab the same behavior, right? Again, using the same sliding window, or based on the collection interval, right? But the way, I think, things are being computed, like the formulas and somewhat, that could be somewhat, I guess, how the metric server does it, if that makes sense. Use the same data somewhat.
**Christos Markou** 37:27 Well, we're a bit over time, but yeah, Dimitri, if you have any concerns about usage, please feel free to share them on the issue.
**Dmitrii Anoshin** 37:35 I don't have concerns, it just seems like representation of usage Jeez.
pretty good birthday here. Yeah, it's just, It's easier to use, because it's, like, less spiky, than… Time… on the time you need to apply a rolling window.
So that was the only thing from my side, but yeah, I agree that it's… even if it's consistent from the Kubernetes API, we cannot rely on it.
**Christos Markou** 38:10 If we still want a metric, we can always calculate it on our side, though.
**Dmitrii Anoshin** 38:13 Right, right, of course.
**Christos Markou** 38:16 Okay, yeah, let's, yeah, wrap it up here, and continue on the issues. Thank you for all.
**Dmitrii Anoshin** 38:22 Thank you, folks. Bye.
**João Marques Correia** 38:23 Thank you.
**Christos Markou** 38:24 See you next time. Bye.
