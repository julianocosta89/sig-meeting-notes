SIG: System Sem Conv Stability WG
Date: 2025-11-27
Duration: 13 minutes
Zoom Recording URL: https://zoom.us/rec/share/xd5OwJ0BD8478IeznzNW0hsgx3xG90dkvIdMFa1CthfI-mLpw-SNEsfGcy32y4Yd.g5-DplcjicwV88nG
============================================================

## Zoom Recording Transcript

**Pablo Baeyens** 00:19 8.
Oh, how's it going?
**Braydon Kains (Google)** 00:25 Good, how are you?
**Pablo Baeyens** 00:28 Doing fine.
We… Wired with Thanksgiving.
**Braydon Kains (Google)** 00:34 Yep, yeah, I can imagine.
Most of my team is Canadian now, so… Same… same old for us.
**Pablo Baeyens** 00:44 You have Thanksgiving, but at a different date, or something like that?
**Braydon Kains (Google)** 00:48 Yeah, we have it second weekend of October.
**Pablo Baeyens** 00:51 Okay.
Maybe we can start, and we can… We can discuss the… your PR on the… Cpu mode… thing.
**Braydon Kains (Google)** 02:23 Yep.
**Pablo Baeyens** 02:26 I think your comment makes sense. I just realized that there's another… Metric, that also has that.
description, the other one… the… CPU utilization one.
**Braydon Kains (Google)** 02:43 Right.
I think it… I think it… Applies the same way?
**Pablo Baeyens** 02:55 I think so, yeah.
**Braydon Kains (Google)** 02:56 Yeah, cause…
**Pablo Baeyens** 02:58 Yeah, I'm not even…
**Braydon Kains (Google)** 02:59 What's a percentage of.
**Pablo Baeyens** 03:02 Right, I'm not even sure that…
Aggregating over that has a meaningful…
value for CPU utilization?
**Braydon Kains (Google)** 03:14 Yeah, I remember that…
There's one… Node Exporter has something about this, where they, like, give you a prompt QL for all
Non-weight states for the utilization?
But, like, even still, I would just prefer…
We tell instrumentation to always produce the mode, and, like, you can… query your…
You can carry your weird aggregations if you want.
**Pablo Baeyens** 03:51 I agree, that sounds… That's not reasonable to me.
**Braydon Kains (Google)** 03:55 you know, I think it's… I don't know every backend in the world, but I can't imagine there's a backend that would…
Benefit from, like, doing this aggregation at collection time, but I don't know.
But I think if we're all in agreement, I can make the change on that, on the PR today.
**Pablo Baeyens** 04:22 for me?
**Roger Coll** 04:26 So, you were discussing about the… But also, soupio down?
Okay, okay, sounds good. Excellent.
**Braydon Kains (Google)** 04:39 The only other thing I had for this group is that I'm…
Working on the process status metric?
I got hung up on it.
Because this whole time, I kind of thought.
Windows had this concept, and it turns out it doesn't.
like, Task Manager will tell you a process state, but it's just, like, a simulated…
thing that they do. It's not, like, an actual, like.
concept on the Win32 process class. So, we can't exactly…
like, I think I'm just going to have to make the description of the metric say, like, it doesn't… this isn't reported on Windows, and I don't know what the equivalent is.
But… I think that's the only option, like… the… the…
Individual threads of the process have the real, like, in-depth, like, point-in-time state enum, but the process as a whole does not.
So… We could start getting down the rabbit hole of, like, Process thread status?
And, like, that one would be reported on Windows, but the… The overall process status wouldn't.
I think that's probably the closest we could get.
**Roger Coll** 05:57 Hmm.
Does this mean that the general process does not run, but…
**Braydon Kains (Google)** 06:05 Yeah, in Windows, a process is, like.
Basically, just a box for threads.
**Roger Coll** 06:11 It's not like a…
**Braydon Kains (Google)** 06:13 An actual running unit of something?
**Roger Coll** 06:15 Okay.
Nice.
**Braydon Kains (Google)** 06:19 Yeah.
**Roger Coll** 06:20 I guess it makes sense just to provide the threats, and…
Make it optional for the process, in that case.
**Braydon Kains (Google)** 06:29 Yeah, I think that's probably… Because…
**Roger Coll** 06:35 That was a metric, right?
**Braydon Kains (Google)** 06:38 Yeah, process, process.status. It didn't exist yet, someone was requesting it.
**Roger Coll** 06:44 Hmm.
**Braydon Kains (Google)** 06:45 we had…
The status, like, the various states as an attribute, because when we produce the running process count for the whole system, it's broken down by state.
I think that just doesn't work on Windows. I think… I don't know what gets reported for that on Windows. I haven't looked.
Maybe we just say they're all running, which doesn't feel right, but…
**Roger Coll** 07:20 30th.
**Braydon Kains (Google)** 07:22 So, yeah, not… not much…
not much more constructive to say on that. That's just what… that's where… that's where I've landed so far on process status. But I am working on it, because it's stability… it's one of the stability blockers assigned to me. So that's… it's the thing I'm tackling next.
**Roger Coll** 07:39 I think it would be valuable for Linux as well, right, to have this
Losses threat status, we will have them.
**Braydon Kains (Google)** 07:48 Yeah, I think so. And, like, probably it would just use the same, because, like, if it's a thread in Linux, it would be, like.
It would be, like, in the proc tasks, but, like, it would kind of… it would have the same… it would be structured the same as the process status one.
So I would need to…
And then, like, probably what would happen would be
on Linux, we'll produce… under a process resource, there'll be a process status.
and then there'll be a process.thread.status that comes with a thread ID.
**Roger Coll** 08:25 Can you do it.
**Braydon Kains (Google)** 08:26 And then on Windows, there's no overall process status, just thread statuses.
**Roger Coll** 08:31 Yeah, makes sense to me as well.
**Braydon Kains (Google)** 08:34 Yeah, I think… I think I'll… I'll try that.
**Pablo Baeyens** 08:37 What are the… The possibilities for a process thread status?
**Braydon Kains (Google)** 08:42 They are…
**Pablo Baeyens** 08:43 on Windows?
**Braydon Kains (Google)** 08:44 they're similar, but not quite the same. So you still have running. There's also, like, ready but hasn't been given CPU…
access yet.
which is also a state on Linux, so those two map pretty well. The ones that don't map super well are Linux will have,
stopped by, like, a… by, like, a job signal or debugger or something, and it will have I.O. wait and idle.
On Windows, all three of those are under the same enum. They're… it's just like a waiting state, and you'd have to go dig more deep… more deep with various syscalls to figure out
like, which… like, what is… what it's actually waiting on? Is it waiting on something in I.O, or is it…
Just sitting there, idling.
we don't know. So that's the annoying thing about, like, how…
I write the attribute descriptions, like, I'm gonna have to put a bunch of, like, random details in the attribute… in, like, the state…
enum descriptions for, like, when you see this on Windows, it could mean this or this, this, and on…
This state is only produced on Linux. Windows will be covered by waiting, or whatever.
I tried to… Come up with a better,
like, Weaver-related way to say that, like, with annotations or something. I didn't really get anything nice.
the… the one feature request I was thinking of submitting to Weaver Which may be…
maybe I could do as a project, because I know Weaver needs more help, it's just rust is hard.
But the… If we could have… conditionally…
Is it… no, it wasn't conditionally required, it was,
Just some sort of way to, like.
Say, conditionally required for platform, like… like this…
Or, like, this attribute will only be produced on this… this enum value will only be produced on XYZ platform.
I don't remember what my idea was.
I'll remember when I go back and look.
Yeah. Well, that's where I landed on that.
I am on call for my team the next couple weeks, I don't expect
it to be super busy, but that may hurt my time I can spend on SEMCOM stuff, too.
**Pablo Baeyens** 11:36 Okay.
**Roger Coll** 11:50 So these were the… the last two features, right, for the processor stability, just the…
CPU time and the status, right?
**Braydon Kains (Google)** 12:00 I…
**Pablo Baeyens** 12:02 There's a third one, there's the…
**Braydon Kains (Google)** 12:04 The file descriptor one.
**Pablo Baeyens** 12:06 Right.
**Braydon Kains (Google)** 12:07 Yeah. So, once those three are done, I think those are the last, like, net new things we have to do, and I think after that, we'll just sort of do…
One more comb through and make sure we feel good about everything we want to mark, and then…
And then… Make… make the stability level change.
**Roger Coll** 12:28 Right.
**Braydon Kains (Google)** 12:36 If someone else wanted to do the…
the file descriptor one. I think it's… it's pretty cut and… cut and dry.
piece of work, if… if someone has… has any time. But I will… I'll… should be able to…
Get to it, if not.
**Pablo Baeyens** 12:59 I'm not going to promise to do it, because…
There's always something to do for the collector, but
If I find the time, I'll… I'll take a look.
**Braydon Kains (Google)** 13:10 Yeah, it'll depend on my on-call load for the next couple weeks.
Cool, I guess we can get some time back if we don't have anything else.
**Roger Coll** 13:30 Sounds good.
Thanks for the update.
**Braydon Kains (Google)** 13:33 Yep, for sure.
**Roger Coll** 13:34 Oh, a good one.
**Braydon Kains (Google)** 13:36 Zero.
**Pablo Baeyens** 13:36 Do you…
