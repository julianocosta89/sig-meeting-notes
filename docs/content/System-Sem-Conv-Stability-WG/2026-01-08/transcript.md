SIG: System Sem Conv Stability WG
Date: 2026-01-08
Duration: 27 minutes
Zoom Recording URL: https://zoom.us/rec/share/QRl5sP3CTF5a-iRWf6EXjqOgyNt5XcVZcmfu6EI1aOsVmxEZAFaj86q0P9Ryr7SR.gv_DeBO0TA5Gzsrb
============================================================

## Zoom Recording Transcript

**Donal O'Sullivan** 01:08 Whoa.
**Braydon Kains (Google)** 01:13 Hello.
**BhupinderSingh** 01:42 everyone.
**Roger Coll** 01:43 Boom.
**Braydon Kains (Google)** 01:45 Happy New Year.
**Dmitrii Anoshin** 01:46 New Year.
**Donal O'Sullivan** 01:47 Blue.
**Dmitrii Anoshin** 01:58 It's pretty good attendance for a first meeting in the year, comparing to other OpenTelemetry 6.
Typically, I join, and no one else.
**Braydon Kains (Google)** 02:08 I joined one on Monday that had nobody.
**Dmitrii Anoshin** 02:11 Yeah, same thing. Maybe it's just Thursday.
**Roger Coll** 02:19 Yeah, probably get it in Spain, it was holiday until yesterday.
**Dmitrii Anoshin** 02:24 Oh.
**Braydon Kains (Google)** 02:24 Oh, yeah.
**Roger Coll** 02:25 on Tuesday, I think many, many countries in Europe celebrate Tiffany's Day, or something like that.
**Dmitrii Anoshin** 02:32 Smo.
**Roger Coll** 02:32 Holy one.
**Dmitrii Anoshin** 02:36 I'm from Russia originally, and their… their holiday break shifted after the new year, so it's from 1st to 10th of January, because of…
**Braydon Kains (Google)** 02:47 the Orthodox.
**Dmitrii Anoshin** 02:50 All the gauntlet.
Christmas is on several things.
**Roger Coll** 02:55 Nice.
**Dmitrii Anoshin** 02:56 So, like, spraying somewhere in between.
Apparently.
**Roger Coll** 03:04 Good to know.
**Braydon Kains (Google)** 03:05 Congrats on getting the talk accepted, Roger. I saw on the schedule.
**Roger Coll** 03:10 Yeah, I know that the title is a little bit clickbait, I think, because probably we won't have the stable 70 conventions yet.
But, yeah, I guess the first lesson will be that naming takes time.
So… and more than expected, so… Yeah, thank you.
**Dmitrii Anoshin** 03:32 What's the title, what you're gonna talk about?
**Roger Coll** 03:35 It's… It's a 10-minute talk, it's just about, it's lessons, From stabilizing system semantic conventions. Basically, I think I will go through most of the… some of the most important challenges that we have faced.
During probably the last 2 years.
Oh, yeah, it's just so it shouldn't have…
**Dmitrii Anoshin** 04:00 No.
**Roger Coll** 04:01 Any of you planning to attend as well, or not this time?
**Braydon Kains (Google)** 04:06 My talks didn't get accepted, so I won't be able to.
**Dmitrii Anoshin** 04:10 I… we have, maintainers, maintainers.
panel.
for Collector.
I'm not sure if it's accepted or not. If it's accepted, I'll join as well.
**Roger Coll** 04:23 Good.
**Dmitrii Anoshin** 04:32 Should we start?
**Braydon Kains (Google)** 04:33 Yeah, we can get started. Mine was first, I just wrote this up, this morning, and, like, submitted the PR, like, 5 minutes ago, so there won't be much to talk about until people have read it. Maybe we can talk about it next week, or in PR comments, but, This is basically… Updating our design philosophy document to include some of the new decisions that we made about naming and write it in a bit more A bit more of a clear manner, because we've had some… discussions on different PRs where there was confusion about what our stance was and where the OS name should go and why, so I tried to basically rewrite the section to update to our current decisions and explain why.
So… Take a look at that PR when you have a sec.
Give it a read-through, make sure I'm still on the right track. One thing I… one thing that I ran into while writing that that I realized maybe we didn't, like.
put our foot down about, and maybe this is just, like, an opinion I had that I started spouting without… Confirming with everyone, but… for… this… this came up in the PSI… Psi PR.
Where there was a question of, like, well, this is Linux exclusive, so the Linux name should go in, and I thought that was a bit redundant, because PSI is pretty… it is a Linux-exclusive system, so the fact that PSI is in the name already implies that, and putting Linux in the name feels redundant.
And that sort of applies to… things like CGroup as well, where we already put the OS name in, so I don't know if we want to I don't know if people agree with me on that or not, or whether we should… change CGroup, or whether we should just say that Linux should go in something like system.psi.
If anybody has opinions on that, immediately we can talk about it here, or we can just talk about it in the… in the PR.
**Roger Coll** 06:49 I think it's a little… A bit related, yeah, a little bit related to my second topic. I wanted to discuss about the… They actually did PSI PR, but they are trying to… To add these new metrics.
And it comes, again, maybe a little bit, the issue about either including the Linux or not, right?
But yeah, maybe we can… we can discuss… The specific use… the specific case later, but, that sense, the refractor looks good to me, I will have a closer…
**Braydon Kains (Google)** 07:31 Motivated.
Okay, sounds good.
We can move on to the next topic, then.
**Roger Coll** 07:40 Yeah, so the… It's mine basically a few months ago that I asked if maybe I can share the screen, someone created a PR to add the PSI metrics, either on the… I think also in the collector as well, but also in semantic conventions.
And they are, let's say, requesting our… our attention.
Mmm… So, as Brandon just mentioned before, the PSI, it's a very specific link thing, so this was added a while ago in the kernel.
But basically, if you cut Brock pressure, you have per-resource information about the pressure, so the amount of tasks that were installed on each of the resources.
And, yeah, this is… I think it's really useful information, and for example, for some of the Elastic integrations, they are already, shipping this information.
So basically, to sum up, they created, this PR that adds, this couple of new metrics, system, Linux, PCI, pressure.
And, and then, for example.
They parameterize the time window from 10 seconds to 60 seconds, or 30 seconds, and then the total time, because… Basically the output Let's say that the… The kernel aggregates some of the seconds and computes the average by itself, and then it also gives you the total.
That's what… why they are proposing these two metrics.
the issue is that, for example, this does not align, for example, with other, let's say, time windows metrics, like the CPU load average that I was taking a loop before, so… Also, I noticed that those, for example, are not in SEMConf yet. Probably I will loop an issue for that.
But I was wondering, for example, if we should continue to follow this.
This format for, let's say, pre-aggregated, values already.
un… In this case, let's say I just recommend using the dot, I don't know, 10 seconds, 30 seconds, and… See, 300 seconds, that's… it's already provided by the kernel.
For the pressure, That's one… one of the things.
And the second one is that it looks like you can also gather some kind of related information for Darwin.
And I think, yeah, there was a PR here.
that in the host metric receiver, basically, they wanted to add system.memory.darwin Pressure. There's a syscall in the Darwin OS that gives you this This pressure information that's… let's say… semantically similar to the PS, let's say the memory PSI, information that Pengado.
So yeah, my… what I wanted to discuss here a little bit is, one that… that's item.
metric naming format, if the time window should be an attribute, or should be part of the metric, as we do for CPU load average.
And secondly, if, let's say they… should they include the Linux, or we should try to find an abstraction?
In my opinion, the second one for the Linux.
I think… that it… in this case, it lands to the OS-specific metrics, because I tried to find the Windows equivalent, and there's… it seems that there isn't.
And the same for, let's say, CPU, or, I think there's, like, a queue also.
Yeah, resource metrics.
So it looks pretty leaning to specific ones.
Yeah, Dimitri.
**Dmitrii Anoshin** 12:12 Yeah, so regarding the first question about the… Whether it goes to attribute or… Magic name.
we said for the load, CPU load metric, we added as a suffix to the metric, specifically because of the guidelines that we have.
The guidelines say that if… information should go to attribute.
Only if re-aggregation of the values, like removing that attribute, would give you meaningful information.
In that case here, it doesn't provide any meaningful information. If you aggregate over pre-aggregated time windows, if you remove that attribute, it will give you kind of a garbage value. So, I think we should follow the existing That's, like, recommendation, and the same… same thing that we've done for… for load metric.
So it'll be, dot… 10 seconds, or dot.
Look, 30th.
**Roger Coll** 13:16 Yeah.
**Dmitrii Anoshin** 13:16 Yeah, considered.
Probably .10 seconds.1 minute.5 minutes, something like that.
And, regarding adding Linux or not, I don't have a certain opinion there. My… like, thought process would be that PSI, is it something that Like, the abbreviation can be reused for something else in any other And any other… OS, or potentially if Darwin or Windows can Come up with something like this as well.
And if they come up with something like this in the future, will it be aligned with the… With the Linux, right?
So… Like, maybe we can think about not what we currently have, but what potentially can happen in the future.
I think… maybe… if we… if we… if we think that PSI is something that can… something can go to other operating systems going forward.
Potentially, even if they use different aggregation windows.
potentially, we can remove Linux in… Just adopt the same if it ever comes up.
Adopt the same pattern.
**Roger Coll** 14:43 Yeah.
Probably, I… Probably I will ask, internally if someone is more familiar with Maybe the kind of the same pressure metrics could be derived in the… Indeed, are we notor or Windows systems from other metrics?
Because… At height level, it seems so.
**Braydon Kains (Google)** 15:10 Basically, just…
**Roger Coll** 15:12 for example, for CPU, it just tracks the amount of tasks that are installed, right? So, I think this thing can be derived or computed in other… in any other OS, so… maybe not natively, but could be somehow, Calculated.
**Dmitrii Anoshin** 15:32 And the pressure that's been added by another PR for Darwin, that one is pretty much same information, or it's, like, some different semantics?
**Roger Coll** 15:44 I… so it's different in semantics, I think this is just the value of utilization, like the total one, not, let's say… Not the average per 10 seconds, 30 seconds, 300, but just the… the total as a percent, and… and just for Darwin memory.
So…
**Dmitrii Anoshin** 16:08 Oh, and that's for memory only, okay.
**Roger Coll** 16:11 Yeah, but I think the equivalent would be, let's say, hmm.
**Dmitrii Anoshin** 16:19 Yeah, what is the big equivalent?
**Roger Coll** 16:25 Yeah. Probably the… Average every 10 seconds, or something like that.
And I guess it depends on the… how the… Collection of the… the collection is done, because this is a syscall in… in Darwin, that fits, yeah, PM something.
Hmm.
**Dmitrii Anoshin** 16:50 Do we need to be assigned in that case, if we just say system Linux pressure, for example?
Or… I don't know.
System PSI… pressure, maybe… Good as well.
**Roger Coll** 17:08 Yeah, this is…
**Dmitrii Anoshin** 17:10 I'm just thinking, maybe we drop pressure in that case? Because, like, I'm just thinking that it's… redundant, few redundant words, right? Linux, kind of, implies that… PSI implies that it's Linux, and also in PSI, there is P, which is pressure as well. So, like, we have three… three parts of the… in the metric name, which are kind of related to each other.
And, for example, P and pressure, it's pretty much same word.
Beautiful.
**Roger Coll** 17:44 Exactly.
**Dmitrii Anoshin** 17:45 I would be open to shorten it in some way.
**Roger Coll** 17:48 Yeah, for example, myself, I was thinking on, First, does resource be part of the metric name, so… Not as an attribute, as we have, but.
**Dmitrii Anoshin** 18:04 Right.
**Roger Coll** 18:04 let's say, memory, what, I.O, CPU, etc. Yeah. And then, yeah, it's just… remove the PSI, because I agree that it's, probably redundant.
**Dmitrii Anoshin** 18:17 Huh.
**Roger Coll** 18:18 Just follow, kind of, this… this structure.
**Dmitrii Anoshin** 18:21 In that case, it'll be aligned with the PR that we already have for Darwin. It'll be same? No, we would need to change Linux and CPU, or change Darwin and memory, because in that PR, Darwin comes first, so we need to decide on the ordering.
**Roger Coll** 18:38 Yeah, exactly. I think that… this with the order should be just described on the PR that Brandon shared before.
**Dmitrii Anoshin** 18:47 Yeah, that sounds… sounds better.
**Roger Coll** 18:50 Okay, cool.
**Dmitrii Anoshin** 18:53 Brandon, do you want to add something?
**Braydon Kains (Google)** 18:57 The main thing I want to add is that the… I'm… I'm not sold on the duration being in the name. I understand the reason for it, but… it's… it's easy enough in, like, a Prometheus world to have, like, suffixed durations and, like, that… It's probably what users are familiar with, but, like, when we're… When we're making semantic conventions documentations, having… having to… Make a new metric entry for every… Every time window, and also… Enforcing that specific time windows Like, if we… if we have 3 metrics for, like, the 3 different… for 3 different time windows, what if they want… what if there's some other metric in the future tracking time… usage over different time windows that, like.
is dynamic, or, like, they're deciding what window to use, but there's no metric available that has that, that has that duration in the name. If it was an attribute, they just put their own duration for whatever they're currently trying to record, and that can remain dynamic, like, we don't have to enforce it. But if it's in the name, we don't exactly have a way right now in the schema to say.
like… system… now, PSI is a bad example, because PSI… the interface only has 3 windows, and I don't think you can change them.
But in a scenario where you could potentially change the window, we can't say something like system.cpu.pressure.
dynamic time window value.
We would… We would somehow need to… like, maybe this is a Weaver feature request or something, but…
**Dmitrii Anoshin** 20:43 We already have such problem in Kubernetes cluster receiver when one part is, like, kind of dynamic. Let's say, let's… there is a standard set of values, and there are some values that can be added.
on top by cloud providers, and they kind of can be dynamic. That's why we have a problem defining them in metadata AM.
Because of that.
**Braydon Kains (Google)** 21:08 Yeah.
**Dmitrii Anoshin** 21:08 But that rule that I mentioned, it's, like, actually written in specification, so… Yeah.
If we're gonna diverge from that role, we probably need to… Amend that and make a… say, like, an exception.
**Braydon Kains (Google)** 21:27 It feels like a pretty reasonable exception to me to… to say that, like.
This is a scenario where an attribute exists for a purpose other than aggregation. It exists for, like, multiplexing over a dynamic value.
the… I don't know if I agree with that original… premise of, like, the attribute only can exist if aggregating over it is… Is providing some other… some useful value or something.
**Dmitrii Anoshin** 22:00 Yeah, we… again, we should make it, like, we should… submit an issue or PR against the… guidelines in that case first, and then see, like, providing this reasoning that you've… that you mentioned.
**Braydon Kains (Google)** 22:18 Is this… this is in the specification, the OTLP specification, or in the semantic convention specification?
**Dmitrii Anoshin** 22:26 It is in… It's in this block, I pretty much… I'm, like, I can find… But, yeah, it doesn't respect.
Like, guidelines for… Mediterranean naming… I think it's somewhere in the tablet, let me quickly find it.
**Braydon Kains (Google)** 22:49 Yeah, that's fine, I'll… I'll… I'll open an issue about it in this case, because this… this feels like… Either… either Weaver needs to somehow support us making, like, dynamic metric names, Or… We need to accept that this is an alternate… this is an alternative scenario where an attribute that isn't aggregatable still makes sense.
**Roger Coll** 23:13 And I also sent you the…
**Dmitrii Anoshin** 23:16 thing that we… the problem that we currently have with, you know, with Kubernetes Cluster Receiver, it's no condition or something like that, I believe.
**Braydon Kains (Google)** 23:27 I'll take a look, yeah.
**Dmitrii Anoshin** 23:29 But we can actually find it quickly right now, I guess. Let me try as well.
**Braydon Kains (Google)** 23:35 I think we even have some… Some cases in… in our conventions where we have… some…
**Roger Coll** 23:47 Some attributes that exist only to.
**Braydon Kains (Google)** 23:52 Only as enums that you might not necessarily aggregate over?
I feel like that exists somewhere, I'll…
**Dmitrii Anoshin** 23:59 Yeah, we need to bring more, yeah.
**Braydon Kains (Google)** 24:02 Some, like, specific cases, if we're gonna turn this into… Into an issue.
It looks like the last thing on the agenda all kind of… ties into the OS naming stuff, too, so we can talk about that quickly, but… We may already have our answer.
You can go ahead, Donald, if you want.
**Donal O'Sullivan** 24:46 Yeah, hey guys, how are you?
And, yeah, so just, last one there, so I have a PR in collector contrib, just to implement, system memory.
Shared, feature, and it is Linux only, so Braden, thanks for the review of the PR. You brought up the valid point that the semantic convention should probably include Linux in the name, so I just opened an issue in… in the semantic conventions repo, just to… To get that name change, so I think it's fairly straightforward.
**Braydon Kains (Google)** 25:19 If that makes sense.
Yeah, when I commented, I was sort of second-guessing it, because, like, looking at the name System Memory Linux Shared is ugly.
**Donal O'Sullivan** 25:28 Okay.
**Braydon Kains (Google)** 25:29 And, like, I don't actually… I don't love it, but when I thought more about, like, why we came up with that rule, it makes more sense. So, probably, yes, system memory Linux… memory Linux shared is likely what we're gonna do, and it's just a… it's just gonna be a matter of… Putting the rename in.
**Donal O'Sullivan** 25:43 Yeah, cool, so I have an issue opening in Samantha Conventional, so I can just open a PR against it, I guess, and… I guess you guys can have a look, if that makes sense.
**Braydon Kains (Google)** 25:52 Yep, should hopefully be straightforward.
**Donal O'Sullivan** 25:55 Cool. I assume there's no need to deprecate or anything like that, because it hasn't been implemented yet, right? So it's just, like, change your name.
**Braydon Kains (Google)** 26:03 Good question.
I think… I think, no, I think there is no need, because it… it's… I think it technically has made it into some… Schemas at some point.
**Donal O'Sullivan** 26:15 But…
**Braydon Kains (Google)** 26:17 No, I don't think… I don't think… I don't think anybody's consuming it. I think we can just change it. I don't know if we need to…
**Donal O'Sullivan** 26:23 Cool. Okay. Yeah, sure, I'll open the PR, and I guess, yeah, I'll wait for feedback. Maybe someone knows if it's been… been implemented or not, but yeah. Cool. Thanks, guys, I appreciate it.
**Braydon Kains (Google)** 26:34 Thanks.
Anything else to talk about while we're here?
**Dmitrii Anoshin** 27:00 No, I'm trying to find that thing, but I cannot do it quickly, so I'll probably send it in the Slack channel.
**Braydon Kains (Google)** 27:07 That's fine.
**Dmitrii Anoshin** 27:13 Thank you, Urva.
**Braydon Kains (Google)** 27:14 Thanks, all.
**Roger Coll** 27:16 14.
**Christos Markou** 27:16 Folks.
**Donal O'Sullivan** 27:17 displayed.
