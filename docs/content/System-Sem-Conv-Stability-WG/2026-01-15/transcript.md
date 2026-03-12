SIG: System Sem Conv Stability WG
Date: 2026-01-15
Duration: 19 minutes
============================================================

## Zoom Recording Transcript

**Dmitrii Anoshin** 00:31 I don't… don't…
**Donal O'Sullivan** 00:35 Hi, Dimitri, how are you?
**Dmitrii Anoshin** 00:37 I'm doing well. How are you?
**Donal O'Sullivan** 00:40 Not too bad.
**Dmitrii Anoshin** 00:50 Hi, Roger.
**Donal O'Sullivan** 00:55 Hey, Roger, how are you?
**Christos Markou** 01:34 Hello.
**Dmitrii Anoshin** 01:39 Crystals.
Are folks going to… Keep calling you?
Yeah.
**Christos Markou** 01:56 Yes, I'm going.
**Dmitrii Anoshin** 01:59 Nice, nice. Roger, we cannot hear you, it's very quiet.
But I think I heard ES from you as well.
**Roger Coll** 02:09 Yeah, no, it's better, probably.
**Dmitrii Anoshin** 02:12 Yeah, it's better now.
**Roger Coll** 02:14 Okay. Yeah, yeah, yeah, I think the answer was yes. Are you going as well?
**Dmitrii Anoshin** 02:19 Yeah, I'm coming as well.
**Roger Coll** 02:21 Cool, good.
Is that the… you said that there's a collector summit, or something like that?
**Dmitrii Anoshin** 02:27 Yeah, maintainers, board updates, whatever.
**Roger Coll** 02:33 Okay.
Code, something like that.
Good. That would be fun.
**Dmitrii Anoshin** 02:39 Nice. Will be my first trip to Europe.
Since 2000… 19, wow.
**Roger Coll** 02:47 Whoa. Oh, wow.
Well, a good country, I guess, a good place to go in Europe.
For a few days.
**Dmitrii Anoshin** 02:59 Yeah, I would… I would definitely… Had some travel there as well. Besides keep going.
Hybrid and hyperbole.
**Pablo Baeyens** 03:10 B.
**Dmitrii Anoshin** 03:11 So, I guess we can start now.
**Christos Markou** 03:17 I, yeah, I added one item. I was checking the, the board, later, earlier today, and, yeah, it seems that we only have two remaining items in the GA process.
board.
And I was wondering, if that could be realistic.
For us to set a goal, maybe, by KubeCon to… Promote the namespace to something like beta, or even a release candidate, something like this.
I'm not sure, what's your thoughts on this. From my side, I would like to see this happening eventually.
I know, Roger will talk about this as well, during CubeCon show, maybe.
That's also a nice, coincidence as well.
**Pablo Baeyens** 04:18 Yeah, that would be cool.
**Braydon Kains (Google)** 04:21 I think it's reasonable. One of the items on there is, I guess both of them are assigned to me, but one of them that's assigned to me, the process status one, I got most of the way there, but it actually ended up being… fairly complicated, because it turns out this… the concept is not really mappable to Windows in the same way, so I don't know, like… how we handle this in that case. The model is extremely different, so it needs a bit… a bit more thought.
I can at least push a branch for where I… where I've landed so far on it, and maybe we can discuss it as a group, but… the… it's possible that the end result of this is that we just make a Linux-exclusive metric for it, because, like, the concept doesn't make a whole lot of sense on Windows. The task manager will simulate the, like, process status, but it's not really the same thing.
so we can… we can decide as a group. I'll… I'll push… push the branch for, like, what I got so far, and maybe we can decide what to do.
**Christos Markou** 05:34 But it's not, as far as I can understand, it's not an issue with the generic modeling that we follow for this kind of metrics, right?
**Braydon Kains (Google)** 05:42 No, that is fine. I was able to adapt at least the Linux part of it to that pretty easily.
So that's no problem?
It's… it's… it's more at, like, a… like, an operating system conceptual level.
it's easy to… it's easy to model and instrument this metric for… for Linux because of the way it reports process statuses, but Windows doesn't really Do the same… do the same thing, exactly?
**Christos Markou** 06:13 okay.
**Braydon Kains (Google)** 06:14 So I wasn't sure how to design it.
**Christos Markou** 06:17 In any case, this addition is… I don't see this as a blocker, because it's something that we'll be adding. It can happen, like.
while.
**Braydon Kains (Google)** 06:29 That's true. Yeah, it might not have to block a release candidate in the namespace.
**Christos Markou** 06:35 Yeah, but it would be nice to have this added before, like, going stable.
**Braydon Kains (Google)** 06:40 Yes, it's… it's been… it's been requested quite a bit.
There's been multiple attempts to… Okay, so maybe what we can do is, if we have this…
**Christos Markou** 06:54 this other issue, the common attributes and revisiting requirement levels, maybe what we can do is, once we have this, then we can probably start dealing with the issue that I opened.
A couple of, like, a month ago, or, yeah, which is about, essentially stabilizing the namespace, and maybe we can start with promoting the metrics and attributes, what we select, to alpha, then, give a release.
To give some time for the release of some other conventions to happen, and then promote to beta, and so on, if you agree.
**Roger Coll** 07:39 Oh, grouped.
**Braydon Kains (Google)** 07:41 I think it's… Excellent.
**Christos Markou** 07:45 Aside from the processor status, what it's missing?
**Roger Coll** 07:49 It's just the… Let's say, define the common attributes.
Agreed.
**Braydon Kains (Google)** 07:57 It's a general issue about revisiting, like, attribute requirement levels. I had one PR open to address One particular scenario… Where we'll see.
Oh, I think it got… it got closed for inactivity. I did submit it before the holidays, and then… Here, I'll…
**Roger Coll** 08:20 Oh, yeah.
**Braydon Kains (Google)** 08:21 Agenda, just for tracking.
**Roger Coll** 08:27 Yeah, probably I also see that we kind of agree on the… obviously, on the common, so probably we can… Maybe reopen and re-reude.
**Braydon Kains (Google)** 08:40 I'll just reopen them and make the change that we talked about in that comment.
**Roger Coll** 08:49 Here.
**Christos Markou** 08:55 Okay, from my side, that sounds good.
**Donal O'Sullivan** 09:05 Does that cover everything in that issue, then, or…
**Braydon Kains (Google)** 09:09 I think this PR covers… like, I… if I remember correctly, I add requirement levels to, like, Every attribute, basically.
**Donal O'Sullivan** 09:19 So I think so.
Oop.
**Braydon Kains (Google)** 09:26 Hmm, why did I make the fault type recommended?
That's weird.
Anyways, I'm gonna reopen and go over this again, but I think this… this adds the requirement level to every… Every attribute in the process… every attribute that is used on a metric in the process namespace, which is where that needed to go.
And… what else is… So, process status, we're… Might be nice to have for stabilization, but it doesn't need to block us targeting, like, a release candidate or a beta.
necessarily.
And I guess… Technically, that other PR I opened last week.
about where to put the operating system name, I, like, I guess that probably should be submitted as well.
I've been on call this week, so I haven't had any time to spare on… on addressing the review I got on that, but… I will… get to that at the… once I… once I have time again, I'll get to that, and the… and the requirement level PR.
**Donal O'Sullivan** 10:57 I could take a look at the requirement level PR, if that helped, or even the status one. The status one is not really a priority, is it?
**Braydon Kains (Google)** 11:06 Not for the initial release candidate, but I think we do want it for stabilization. I can… I can push the branch that I have and give you a…
**Donal O'Sullivan** 11:14 like.
**Braydon Kains (Google)** 11:14 rundown of where I… where I ended up getting… getting stuck in… in…
**Donal O'Sullivan** 11:19 Trying to figure out what to do from there.
Yeah, cool, that's on the process stylus, is it?
**Braydon Kains (Google)** 11:25 It's gonna be, yeah, for process status. I have… I have a branch, like, where a lot of it is written up, and then I… I got really stuck at a certain point once I started, like, looking deeper into how it's modeled on different operating systems, and, like, it just… I just couldn't make it… map nicely.
**Donal O'Sullivan** 11:44 So it sounds like we want that to just be a Linux-only metric then, is it?
**Braydon Kains (Google)** 11:48 That's probably gonna be the way it goes. I don't know how well that's gonna be received, like, I think a general user would be like, well, if I look at Task Manager, I can get a process status. I can get the status of the process, roughly. But modeling it as a time series metric The actual instrumentation of it is… non-trivia, because Task Manager is doing some weird… Like, aggregations on… This is a long rant, I don't know if we have other stuff to…
**Donal O'Sullivan** 12:18 Talk to another one.
**Braydon Kains (Google)** 12:19 We'll take up time, but, the… Probably it's gonna have to be a Linux-exclusive metric, and then if someone asks asks, why doesn't this exist on Windows? We'll need to have a well-written explanation why, I think, because it seems like… it feels like a generic expectation, but it's not that simple, basically.
**Donal O'Sullivan** 12:41 Makes sense, yeah, makes sense.
Yeah, if you, if you want to maybe just Slack me the branch, or whatever, or we can have a look. Yeah, we can take that. Oh, yeah.
Thanks, Britton.
**Christos Markou** 13:02 Anything else for today?
**Braydon Kains (Google)** 13:09 I haven't had time for SEMCOMF work, but on host metrics receiver in general, I've been trying to fix the context switch count issue, where currently the context switches are only counted for the lead thread of a process.
In my attempts to fix that, I found that there's… a bug in GoPS Util, where if you use, a mounted a mounted, like, host proc… like, a mounted proc FS. The method that I'm using to count the switches for all threads won't work, so I'm working on getting that fixed upstream.
**Roger Coll** 13:51 The solution is to count All the threads, contact switches.
**Braydon Kains (Google)** 13:58 Essentially, yeah, so, like, the… the method that they have to enumerate all the processes on the system uses the getDens syscall, which means we get all the lead process IDs, but none of the subtasks. So what we have to do is, when it's time to count process switches, we enumerate the tasks.
Of that lead process, which includes the lead process itself, and then directly read ProcFS for each… each task ID.
Because there actually are entries in PROCFS for them, but if you use the full enumeration, it doesn't give them all. So then we read them all directly, and the… and we read the context switch of each one and sum them up.
The bug is that when you use a mounted PROGFS, if you… the method that they have for direct reading a new process.
checks just using, like, the Go's, like, OS package, whether the process exists.
But if you're using a mounted PROCFS, that's not… it's not going to necessarily exist on the OS the way the OS checks for it.
So that's the… that's the thing I need to fix.
**Roger Coll** 15:09 Thank you.
And I guess we don't want to provide them… Per thread contact switch, and then just, let's say, kind of… Aggregate, out-aggregate, if you don't define the attribute, or something like that.
**Braydon Kains (Google)** 15:24 So that's been something that's been… rattling around in my brain, but I haven't had time to think about, which is that we don't really have, like, a… like, a thread namespace and, like, provide.
**Roger Coll** 15:33 Yeah.
**Braydon Kains (Google)** 15:34 about, like, all threats. We don't have it right now.
But, like, it would make sense to do so, it's just, like, it's a pretty heavy, like.
metric volume, but I feel like there are probably People who would be interested in, like, semantic conventions around, like, individual threads, especially for people who are just monitoring one process at a time.
So…
**Roger Coll** 15:55 Yes.
**Braydon Kains (Google)** 15:56 It doesn't exist, but it would be nice, I think.
**Roger Coll** 16:00 Yes, and I think it probably will happen for profiling, because I think for profiling… Probably the resource is a threat, not the whole parent process.
**Braydon Kains (Google)** 16:12 Yeah.
**Roger Coll** 16:12 I'm actually looking into that, let me… let me see if I can… pull it back, and… yeah, I was mentioning because I think that we were working on… Aggregation… aggregating directly in the, mdata Gen Builder, right? And… In the future, it would be a matter of just… Let's say, not defining that attribute, and you would still have a nice carbinality, and… And at the same time, if you would like fine-grained metrics, just define the threat ID. But probably it's for a future improvement at the moment.
Looks…
**Dmitrii Anoshin** 16:54 By the way, the reaggregation capability has been merged as a… under Fisher Gate.
So it's.
**Roger Coll** 17:01 Of course.
**Dmitrii Anoshin** 17:02 We didn't want to, like, make a huge PR to upgrade all of the receivers and have, like, gigantic diff, so we… it's currently under FisherGate, and we're gonna just apply it one by one on every receiver in country.
**Roger Coll** 17:17 Cool, thank you.
**Braydon Kains (Google)** 17:18 Makes sense.
**Donal O'Sullivan** 17:29 So I, I also updated the, PR I had for adding the, system memory shared metric, so the semantic convention PR was merged, so that, that name's changed now, so the collector contribute PR, I've updated the, name there as well.
So the PR should be quick for re-review.
**Braydon Kains (Google)** 17:46 Okay, I'll give it another look.
**Donal O'Sullivan** 17:48 Appreciate it.
**Pablo Baeyens** 17:55 I guess I'll mention, So once it commencers migration, RFC on the collector is… Now, Mark, that's great for review. Thank you, Christus, for the review, and If you want to take a look, I'll put the link on there.
On the notes.
**Christos Markou** 18:16 I think it would be valuable for this group to provide feedback, since it's essentially what we have been discussing.
Over the past months. So, yeah, thanks for putting this together.
**Roger Coll** 18:46 Okay? Anything else? So, we can keep it?
Here.
**Braydon Kains (Google)** 18:52 Yeah, I have nothing else for today.
**Roger Coll** 18:56 Okay, then I guess see you next week.
**Dmitrii Anoshin** 19:00 Thank you, thank you.
**Braydon Kains (Google)** 19:01 on.
**Christos Markou** 19:01 Bye.
**Donal O'Sullivan** 19:02 Take guys, bye-bye.
