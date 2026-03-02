SIG: System Sem Conv Stability WG
Date: 2025-11-06
Duration: 15 minutes
============================================================

## Zoom Recording Transcript

**Roger Coll** 00:50 Hello.
**Pablo Baeyens** 01:48 Ay.
I think we can start, because…
Josh and Braden are not joining today.
**Dmitrii Anoshin** 03:24 Overdue.
**Roger Coll** 03:38 the topic yesterday.
And… it's basically about, threadon name, and to give a bit of context, it comes from the…
well, some profiling folks within Elastic, that basically, in a profile, you have… in a profile definition in OpenTelemetry, you have different stack traces.
But all the stack traces, Let's say, are related to a specific, process threat.
Not, let's say, a process in general.
And… They had some concerns, because they noticed that, in the process, let's say, entity definition,
this thread ID or thread.name is not part of the identifying attributes, and… Basically, they were,
They didn't know, actually, how to
To deal with that, or how to…
To make it happen, because in, let's say, in profiles, this would be an identifying
attribute that identifies, let's say, a smaller
Entity than a process, but it still needs all the process and resource attributes?
I brought it here just to have some opinion, and I guess there's…
different ways to… to tackle it. I don't know if it would be possible to make an identifying attribute as optional.
within the process entries, that… I don't know, actually, if it makes sense in the definition of identifying attributes.
Or another one is to create, let's say, a completely different thread entity, and then in the profile, just have reference to two of them.
The process on the… on the threat, one.
**Dmitrii Anoshin** 05:41 Yeah, I think the second option is, probably… ideal, because…
If process can have several threads, it doesn't… it's not a process anymore.
**Roger Coll** 05:54 It means that process.
**Dmitrii Anoshin** 05:56 It's a parent of a threat, which is another entity.
And, yeah, an identifying attribute of a thread would be thread ID in that case.
Because an identifying attribute is supposed to be unique only within its parent.
So it's not supposed to be globally unique.
**Roger Coll** 06:18 Okay.
**Dmitrii Anoshin** 06:18 As long as the thread ID is unique within the parent vicious process, it can be another instance.
**Roger Coll** 06:26 Okay, makes sense. And then…
**Dmitrii Anoshin** 06:29 If you said that there is, like, more globally uniqueness is required, it means that they would need to attach a process entity as well, so it'll be two entities attached.
**Roger Coll** 06:40 Okay, and it's not an issue to have different entities as…
Part of identifying in the profiles.
**Dmitrii Anoshin** 06:48 No.
**Roger Coll** 06:49 Okay, the… The process one and the threat 1.
**Dmitrii Anoshin** 06:53 Yeah, they will be assigned to the same resource. A resource can have several,
**Roger Coll** 06:59 Okay.
**Dmitrii Anoshin** 07:00 And all… each entity would have different identifying attributes.
**Roger Coll** 07:05 Okay, and then I guess the follow-up question would be…
how we define these attributes, let's say, because in our head it makes sense to be process.thread.name.
and process.thread.iv.
Yeah, I think…
**Dmitrii Anoshin** 07:24 process.thread would be an entity. I also don't think that thread by itself is a good enough name for that entity.
**Roger Coll** 07:33 Okay, and we create… we can create an entity for the… Let's say namespace process.thread.
**Dmitrii Anoshin** 07:40 Yeah, not namespace, it's gonna be type of… entity type itself.
**Roger Coll** 07:45 Okay.
**Dmitrii Anoshin** 07:46 So we would have… process entity, and process that threat in another entity.
**Roger Coll** 07:54 Makes sense.
**Dmitrii Anoshin** 07:57 Thank you for working with the…
Profile and seek, by the way. Like, it's definitely… we need to bridge the gap.
Because so far, even from the beginning, it looks like Profile Manage was kind of detached from the rest of OpenTelemetry, and…
**Roger Coll** 08:15 Yeah.
**Dmitrii Anoshin** 08:16 Maybe they miss some, like… Let's say… Come on… standards that, we allow…
**Roger Coll** 08:26 Hmm.
Yeah, yeah, it's pretty new, and also, I think they have…
use cases that, from the system level, we haven't thought of. Like, also, they heavily use
In, in ElasticProcess.labels.
And these are kind of some…
attributes that you can add, within a process with, p-proof and different options, and actually they are… they are pushing to… for that, but it's quite valuable, so it's, I think, at this point where system and profiling
intersects, and… Would be nice to work together.
**Dmitrii Anoshin** 09:07 We can add those. We already have similar semantic conventions for pod labels, for container labels, I guess, as well, so it should be fine to add.
**Roger Coll** 09:17 Yes, I… I will share the issue, because there's a… there's a discussion on that with, Josh, etc.
**Dmitrii Anoshin** 09:25 Fine.
**Roger Coll** 09:27 But yeah, this part, I think it makes sense with, the work I shared with them, so thanks for the feedback.
Guess we can jump to the other one that is checking the… reward.
I can share my screen if I want.
**Pablo Baeyens** 10:08 Okay.
**Dmitrii Anoshin** 10:09 Thank you.
**Pablo Baeyens** 10:10 Thanks.
**Roger Coll** 10:24 All right, so, yeah, finally yesterday, I think we closed the… the one about renaming…
Linux system where the OS,
Happens to be in the name.
So this is closed in the end.
Two, we have just 3 left.
In progress, I guess.
Define common attributes under existing levels.
I think Brighton probably… Said that he's… yeah, assigned it to him, so maybe you can ask him.
Next week, if anyone.
Yeah, any update?
That one also, yeah, looks like all of them are Brian is working on. The other one is process status.
Let's get you in an update. Okay, next week.
Okay, so wait a moment… on a PR, but the decision was made.
And the last one… Change, process, open file descriptor.
I think we've had a decision as well.
**Christos Markou** 11:58 Alright, we can move it to decision-making.
**Roger Coll** 12:04 Okay, cool.
Well, we can ping, but I don't know if he has some time. Maybe we can have.
Have that one.
Yeah.
Looks like that's it. This is for the…
process area, we want to check, system one, or… I guess this is the…
Important one at the moment.
**Christos Markou** 12:41 Anything else that, we could consider doing? Because it seems that…
Right now, most of those are, waiting in Brighton, so…
Yeah, what would be the next steps? Any… Thoughts on these?
For process, specifically.
**Pablo Baeyens** 13:06 Is there anything to discuss about the process for stabilizing the metrics?
**Roger Coll** 13:13 I think that…
Those ones that are decision-made, and the other one interesting… let me open… I just have the link…
But probably it's not blocking the stabilization. It's about the one that I was mentioning, this process.label.
That it's needed for profiling, but… Yeah, absolutely.
We can add it now or afterwards. This needs to be…
Probably I can add it to the board, no, but this is the GA one.
But yeah, aside from that, I… No course, anything like that.
**Christos Markou** 14:06 Do we need to do anything,
On the process entity level, yeah, I guess…
This should also, become stable along with the metrics, right?
**Dmitrii Anoshin** 14:22 I think that merged is process entity definition.
**Christos Markou** 14:29 Okay, so it's all, it's all about changing the stability level once we… Decide on this, right?
**Dmitrii Anoshin** 14:35 I guess so, yes.
**Christos Markou** 14:38 Okay, sounds good then.
**Roger Coll** 14:41 Cool.
**Christos Markou** 14:42 So, yeah, it's…
**Roger Coll** 14:44 I agree.
**Christos Markou** 14:44 yards for Bright… from Brighton and then.
a fourth PR to… make them stable, I guess.
**Roger Coll** 14:54 Nice.
Yeah, that's a good… Check next week. What's date.
**Christos Markou** 15:02 Cool.
Thanks, everyone.
**Roger Coll** 15:06 Thank you, again.
**Christos Markou** 15:08 memo.
**Roger Coll** 15:08 too.
