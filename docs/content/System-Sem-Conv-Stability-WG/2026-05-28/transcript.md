SIG: System Sem Conv Stability WG
Date: 2026-05-28
Duration: 33 minutes
Zoom Recording URL: https://zoom.us/rec/share/g1NWjSDFo4zzeRp5cYkWejvlhBomXlVX4fOVIp9Hf7IhZGSenJxOPZCoed4rAvBe.F_BXAMrAH3IwVh-H
============================================================

## Zoom Recording Transcript

**Donal O'Sullivan (Elastic)** 01:48 Hey, folks.
**Dmitrii Anoshin** 02:48 Should this stuff.
**Roger Coll** 02:56 It's very… it's very quick. Just a heads up that, A few weeks ago, we added, well, we were trying to add this new feature in the force metric receiver that fits about, changing how we are getting the CPU metrics, well, the CPU values.
In a way that… let's say it's much more efficient in terms of the storage. Basically, we are reducing the noise of, Arithmetic operations, and… Using exactly, let's say, the precision that the kernel gave us.
I'm… The advantage is pretty weak. So, let's say that we reduce a lot the number of decimals in the CPU metrics, while still having the same precision, and… We would like, basically, to push this into the host metrics. At the moment, it's behind a feature gate.
We have already tested, and it works quite well.
But yeah, just a heads up, if, Dimitri, maybe I would ping Braydon as well, if you could take a look, whenever you have some some spare time, it would be… would be great. But at the moment, just to mention that it's behind the feature grain, so it does not change the… The current retrieval, process.
And… Our plan is just to, yeah, have it for the moment behind the feature gate.
Do some benchmarking tests that we have already done, but, just using the, let's say, the main version.
And… and show up the… the storage improvements that are… But very noticeable.
**Dmitrii Anoshin** 04:51 That's good. Storage improvements, which storage do you mean?
**Roger Coll** 04:56 Storage, because, let's say, we reduce a lot the number of decimals that are being stored, so… At the moment, yeah, so for each data point, let's say that the number of the… the float decimals, currently it's very big. I don't remember, like, I think, yeah, it's, like, 15 to 17… the digits… And with this new approach, it reduces dramatically. I don't remember exactly the number.
But the number of digits of the, let's say, the final float of each data point, it's less.
**Dmitrii Anoshin** 05:40 But it's been stored on… in the float anyway, or, like, double… where… what storage do you mean? If it's memory, there is no memory change, right?
**Roger Coll** 05:51 No, no, no, that's… it's on the… it's on the backend itself, so I think in case of… Elasticsearch, it can perform much better compression.
**Dmitrii Anoshin** 06:04 Yeah, I… I understand now, but why… why can't we do that on the back end? Like, just rounding it up? Because we… it looks like we are adding complexity to the receiver to… for purpose of specific backend implementation.
Because insofar as… if I understand correctly, there is no improvement on the receiver.
**Roger Coll** 06:29 No, I think that there is. The issue here is that so the… how the… how the, let's say, the GOPS util… library gathers and gives us, those values compared to the raw ones that we have available from the kernel. So GOPS utils… basically, transforms it to seconds, and then to milliseconds, or something like that. And in this case, instead, it uses the CPU ticks. So basically, you have the… the… I don't remember, I think it's, like, the millisecond precision.
And then…
**Dmitrii Anoshin** 07:13 Okay.
**Roger Coll** 07:14 It correctly transforms it to, To the correct precision, so it's actually much more… accurate DN value.
**Dmitrii Anoshin** 07:25 Okay, accuracy being improved, and I guess the CPU utilization gonna be improved by that? Is that correct, understanding?
**Roger Coll** 07:36 Yeah, yeah, so all the values in the end, so all the… all the RAW CPU,
**Dmitrii Anoshin** 07:43 No, I mean, utilization of the receiver itself.
Especially…
**Roger Coll** 07:48 Yes, because it's…
**Dmitrii Anoshin** 07:48 CPU cycles spent to… for the scraping… for scraping?
Will that be.
**Roger Coll** 07:54 Huh.
No, I think that's the same.
**Dmitrii Anoshin** 07:57 The same.
**Roger Coll** 07:58 Probably, yep.
Yeah, yeah, so here, if you take a look, we use the… Actually, how the, the kernel uses the… the hert? I don't remember, but, like, the Hertz… Oh, yeah.
**Dmitrii Anoshin** 08:17 So I'm trying to understand what specific benefits we provide to the receiver, because I guess it's a complication that we introduce here, we need to maintain that, and we need to understand, like, what's the return of investment into that complication. So, if it's just precision, at least, can we have, like, some kind of Summary of what, what exactly What exactly?
on the precision.
**Roger Coll** 08:45 Yeah, yeah, I think it's… it's… it's explained, and maybe I can start the…
**Dmitrii Anoshin** 08:49 Okay.
**Roger Coll** 08:50 issue about.
**Dmitrii Anoshin** 08:54 Yeah, my point here is that we are not just changing the receiver to… in favor of some back-end implementation, because.
**Roger Coll** 09:04 No, no. Yeah.
**Dmitrii Anoshin** 09:07 Okay.
**Roger Coll** 09:07 I think that's, yeah, that's the test that we did on our backend, and it definitely makes an improvement there, but it's not… just a backend thing. It actually, there's a reason behind… behind that, as the same as we did for the… it's very aligned with the same as we did with the… with the memory metrics that, we had some, yeah, basically excessive, Significant digits that were not, were not needed at all. So we… you have some noise there. And you can use another strategy, gathering the values directly, From the kernel instead of the… of copies util, that it's the one that it's adding this extra, let's say, this extra precision that it's not needed. Well, not precision, but, numbers, and this is due with, the seconds versus how the kernel gives you that value. But I think it's…
**Dmitrii Anoshin** 10:14 Yeah, but at the same time, we are moving implementation from by moving implementation from GOPCTL to the receiver, and if we have a goal going forward to get rid of GOPCTL, that kind of can… That would make sense. But if we don't have that call, and we're kind of in a split situation, for some metrics we rely on GOPS UTL, for some metrics we rely on CPU, and we have this, like, a lot of extra code to maintain this, like, manual calculation.
Honestly.
From my perspective right now, this… Like, doesn't… additional complexity doesn't… and ticket is a complexity that has to be maintained.
That we, like, if something's broken, some bugs, we need… we have to go and fix that. So, like, surface for failures is bigger now, and maintenance burden is bigger now. But the value that we are getting from it, I'm not convinced at this point that the value is… it provides enough value for that. Unless we decide that we go in… we are trying to go away completely from GOPCTL, and if someone can take that, like, assessment and see what it would take to go from GOPCTL, that would be… Another good, good point to consider.
Let me know what you think, maybe I'm happy to… We'll hear Brighton's opinion of this as well.
**N'at (us-pit-bak)** 11:59 it's the mute button.
I liked the first PR, where we reduced the float precision of the… of the… Also of, like, the memory metrics, I thought that was a… A really high value.
for… for… for this one, I… I'm… I think I'm kind of with Dimitri that, like, it's more accurate, but not… Significantly more.
So, I don't know, I think maybe I need to read this again. I had this in my review queue at one point, and I just lost track of it, but… in terms of moving away from Go PSUsil, I think if we were only targeting Linux as our only platform, I would have long ago suggested that we just, like.
Got it, and do it ourselves. It's the multi-platform thing where I'm scared to move away from GoPS Util.
Because it already did a lot of work that we would have to repeat in terms of… Exactly how you… Calculate things differently based on what the system is gonna decide to give you.
for… the only… I don't think you can get… this type of CPU tick, or, like, Jiffy information from, like, a Windows kernel, right? So, any… Any Windows implementation of these same metrics would be using GoPsutel versus us introducing a separate API service just for Linux.
And that might look a little bit… a little bit ugly. I'm… I'm not… Too concerned about the maintenance burden other than just, like, the generic maintenance burden of there being more code anyway?
Just because this… this is not, a part of the kernel that changes a lot. I, like, I don't think we'll have the rug pulled out from under us, I guess.
I don't… I don't have a definitive yes or no off the bat.
the only… the only part I'm concerned about is just that it might be kind of… kind of annoying to understand when you, like, go in to look at the implementation of the metrics, like, all the other platforms are just gonna use what GoPS Util gives us, but for Linux, we do something… something special, and… Presumably, we have to wrap this in some, like.
generic interface so that we're not writing separate… entire separate scraper implementations, and might be… might get… might just get kind of annoying to read.
But I think maybe I need to look at the PR to see what the code looks like, to see how annoying that actually is.
**Dmitrii Anoshin** 14:48 Yeah.
**N'at (us-pit-bak)** 14:49 I guess maybe…
**Dmitrii Anoshin** 14:51 We can just have a look. I have… I… my… same for me, I haven't even looked at this PR yet. So we take a look, and maybe discuss it again on the next call. How does it sound?
**Roger Coll** 15:06 I'll put.
**N'at (us-pit-bak)** 15:06 Yeah, I'll put this back in my review queue, I'm sorry I lost track of it.
**Roger Coll** 15:11 Yeah, no, it's, I think that's… that's valuable enough, Actually, I think I suggest that Salvatore just… trying to move that into GOPS Util, maybe, if it… If they agree there, I'm not sure if it was totally possible.
**Dmitrii Anoshin** 15:33 At least, if we bring that issue to GoBug deal, it would be… we would get some valuable feedback.
Right.
This is also pretty important.
**N'at (us-pit-bak)** 15:46 I do think we have had to… do something separate from what GoPS Util will allow, because… The main one was for the process handles metric.
the GoPS Util wouldn't… Allow us to implement that in a nice way, because they endeavor to keep identical API across ball… Across all systems.
But… process handles is, like, a special, unique concept to Windows, and so they wouldn't… allow… at the time, they wouldn't allow an implementation that deviated just for Windows, like a special function that existed just for Windows to get, like, handles for a process. And so we did have to deviate there. So it wouldn't be the first time we deviated from something GoPSUtil does, and maybe that… Maybe that implementation of process handles is a good, frame of reference for, like.
how annoying has that been to maintain separate from GoPSUtil? It… it… it looks kind of… kind of yucky, but… it hasn't been that bad, I guess?
So, maybe that's a… that's a… a reasonable reference to say, like, we've deviated from GoPS Util, it's not the first time…
**Roger Coll** 17:07 Yeah, and this part of the kernel, actually, I think it's very stable, it's not gonna change in Linux, like the… the way that it's being written to a slash blog, and… the user, frequency, that basically the kernel writes to this file. I think it hasn't changed since… ages.
But yeah, I think we can agree on maybe you can have a, like, a quick look, and maybe next… next week, just… discuss it again, and maybe we can try to… to also bring it to, COPS PDS UTL, and… And see if they would like that, upstream or not.
And… Yeah, maybe then this kind of… if it's actually valuable, or… We have some other way to… to implement it.
Because it's not… I would say it's not that, That'll, let's say, less noticeable, negligible change. You hear one example.
Basically, for this value, like, I don't know if it's a CPU utilization, or what is that, but… You have all these extra digits that are basically, numeric noise. It's.
**Dmitrii Anoshin** 18:32 To be honest, I don't buy this concern. Like, we are not storing strings here. We are not storing every digit. It's a float. Like, why is this a wrong float value?
for me, it seems, like, completely normal. And even, like, even if you have 0.031, how you represent that in float? There is no way you represent specifically that number in float. It'll be… it'll be… A lot of digits anyway, like 000 something something 1, 1, 2, 3, 4, 5.
Right.
I… don't understand that.
**Roger Coll** 19:13 Yeah, I'm not sure about, actually, how the compression on this is being stored.
**Dmitrii Anoshin** 19:18 Like, float numbers, they are not in decimals, they are in, like, Look… wherever, like, binary format. You cannot have exactly 0.031. You just cannot.
**Donal O'Sullivan (Elastic)** 19:35 Yeah, you're always allocated the same amount of bytes for a float, like, underlying the system, so it's always the same size, right?
**Dmitrii Anoshin** 19:43 Yeah, my point is that the value, like, in the float or double that.
**Donal O'Sullivan (Elastic)** 19:48 Yeah, yeah.
**Dmitrii Anoshin** 19:48 store it. It's not 0, 0.
**Donal O'Sullivan (Elastic)** 19:50 Yeah, of course.
**Dmitrii Anoshin** 19:52 It's something else. It's like, if you make it even very, very close to this value, it'll be 0.031.0… no, not that, 000…
**Donal O'Sullivan (Elastic)** 20:03 Exactly, exactly, yeah, yeah. Like, the underlying the number of bytes allocated are the same.
Yep.
**N'at (us-pit-bak)** 20:10 It's the elastic.
float implementation not work like that, maybe? Like…
**Roger Coll** 20:16 I think there's some clever compression, things here, like, there's… you have a lot of data points with a lot of zeros, There might be some compression algorithm that goes through that and just… That's compression. I'm not 100% sure, but I think we have some… there's something like that.
But all.
**N'at (us-pit-bak)** 20:45 I'll still read through. One thing I wonder is whether the… the, like, precision rounding API that we introduced in that last PR I introduced, like, if that isn't enough.
For at least that part. Like, I think maybe the issue is talking about two things, one being the excessive float, and one being the… the fact that GoPS Util does a custom calculation versus just reading the Jiffies directly.
**Roger Coll** 21:22 Yeah, I think that they are… They are related, but… I think was… one was easy to solve, because it was just, let's say, a… It… the extra digits were introduced because of the numeric or algorithm divisions that we were doing there.
While the other, to preserve, let's say, the same accuracy, we cannot do it, because they are already, let's say.
Drunk, or, The ones… the values given by Cox UTL, and that's why, we need to script directly from Prokostats, and also use the user frequency Off the clock, because we get, let's say, the actual we get the actual, ticks and convert them to seconds directly. Yeah.
Well, I think… Wait, yes, you tell not.
**N'at (us-pit-bak)** 22:22 Does GoPSQ still not use the user's clock?
Clock Hertz?
**Roger Coll** 22:27 I don't think so. I don't know. Really? That's weird.
**N'at (us-pit-bak)** 22:33 That's like… that's like when they… they weren't using the… the configured page size, either. That, that…
**Roger Coll** 22:40 What issues?
**N'at (us-pit-bak)** 22:41 Or a random customer wants to.
Interesting.
Would have thought they wouldn't.
**Roger Coll** 22:48 Yeah, well, let me double-check that as well, because I'm not, I don't know, 100%. Yeah, that's a…
**N'at (us-pit-bak)** 22:54 quick look.
**Roger Coll** 22:55 Yeah.
**N'at (us-pit-bak)** 22:56 That is an example of something we could contribute upstream if they're not.
**Roger Coll** 22:59 That seems like.
**N'at (us-pit-bak)** 23:00 A pretty fair… a pretty fair change, but…
**Roger Coll** 23:04 Yeah, definitely.
Okay.
**Christos Markou** 23:09 I only want to add here that, listening to this conversation, yeah, another idea would be, or something to consider, is to find a unified central way to handle this kind of things instead of going and implementing them inside the receivers, because I saw there was a similar request for Kubernetes-specific components as well. So, if we end up having to Manually… to… to codify this, kind of… approach in every single receiver, maybe that's problematic. And maybe, in some components they won't accept it. But if we find a way to centrally handle it, like, in a processor or something.
So user… use cases that actually want to cut this precision, to reduce storage or whatever, they can still do.
No matter what the underlying, receiver does, I'm not sure if that would be possible, but, yeah, I would try to… To consider this as well.
**Roger Coll** 24:18 Yeah, I don't think in this case, because let's say that the values that we are already gathering, we cannot… Let's say, just stream the value, and just get the… Two digits of precision.
It's that the actual value that we are getting from GOPS PS Utils, It's not, I'd say, corrective in that sense.
So… It's not a simple, let's say, algorithm, arithmetic operation.
That's why we need to change how we… Gather those values.
**Christos Markou** 24:56 But how we're going to implement the same thing in other components, like the kubelet SATS receiver, because there are… the numbers that… the metrics that we are already scraping from the API is fixed, so we don't have any different… access to something else to collect them. So we would need to… my impression was that we would need to somehow Cook the data, or, you know… Process… further process them to achieve this result.
**Roger Coll** 25:33 Yeah, I know, look.
I only think about contributing this upstream, and just thinking… Let's say the libraries that get these values, Actually care about the… the precision, if that's… that important.
But…
**Christos Markou** 25:54 Okay.
**Roger Coll** 25:56 Yeah, let's double-check, actually, like, what are the actual benefits of that, and… And maybe considering getting the feedback from COPS maintainers as well.
**Dmitrii Anoshin** 26:13 Yeah, at least submitting an issue upstream property also would be great to see, like, maybe they have some specific… The reasoning behind the current implementation.
**N'at (us-pit-bak)** 26:25 Yeah, it might be good to have record of them saying no, rather than our assumption that they will say no, even though I'm pretty sure they will. Just, you know, if we have them specifically saying no to us, then that's fine.
**Roger Coll** 26:39 Sounds great, thank you. Sorry for taking all that time. Donald, would you like to cut some topic as well?
**Donal O'Sullivan (Elastic)** 26:49 Yeah, so quickly, so the pull request for version metrics in mDataGen is up, Christos has given it, like, a quick review, So it's in a good state now, it's run… I have it running there, it seems to be working as expected. There was a bit of a… Speed bump, so they're just regarding the RFC, I had a question, specifically around… so there's… there was two, I guess, issues around, like, double writing, so, like, different attributes and different metric types. So the first one's if a metric name stays the same, but an attribute is renamed.
We want to emit a single metric with both V, like, you know, V0 and V1 attributes.
That's fine, that's fairly easy to handle in mDataGen. The issue arrives when attribute types change from V0 to V1.
So that's… I don't think, for me, that's not captured in the RFC. Is that something we want to add to the RFC? One is… two, is it something we want to support?
just putting it… putting it out there.
If so.
**N'at (us-pit-bak)** 28:00 Okay, so for, for, for types.
types changing on metrics, I guess it's just, like, between double and int, right?
Is that the only option?
**Donal O'Sullivan (Elastic)** 28:11 yeah, I think so.
**N'at (us-pit-bak)** 28:16 I know that the proto's a bit strange, because, like, you can have both an int value and a double value, and I forget, under the protocol.
If it's, like, if both happen to be set.
Does it, like, invalidate the protocol, or is it told to just take one over the other? I can't remember.
But yeah, changing.
**Donal O'Sullivan (Elastic)** 28:36 Yeah.
**N'at (us-pit-bak)** 28:36 interval is a bit awkward, because it's like, to change it, what you actually do is unset one and set the other.
**Donal O'Sullivan (Elastic)** 28:43 Yeah, so on double writing, where a type change, we just take the latest, so we just scrap the legacy and just take latest, so that's easy to do code-wise. Code, like, Code-wise, handling attribute type changes is a bit annoying, because, like, just the example was, so, an attribute being CPU, where your, the number of logical CPUs on a system, its type currently in host metric receiver is a string, but if you look at the latest matching convention, it's an int.
That's totally fine, but it's just the, handling that in mDataGen, in the template code, again, it… It's possible, it just makes it a bit messier, so it's just kind of awkward, if that makes sense.
And it just wasn't called out in the RFC, so I just thought, is that something you want to add… add to that RFC, or just… is it implicit?
**Dmitrii Anoshin** 29:38 Maybe if we… My point, we don't have to, like, consider all of the age cases. Maybe we… if we don't decide, we can put it in RFC, this is, like, something to consider later, because We don't have those needs. If we don't have those needs, we don't have to come up with the solution.
So, I guess in all of the researchers that we want to migrate, if you don't have those use cases, we probably just… don't bother, and put it in RFCO or whatever, that this is something that we will define once we have that.
Need. Essential.
**Donal O'Sullivan (Elastic)** 30:19 Yeah, yeah, the only reason I ask is because I've had to put it in the pull request, so…
**Dmitrii Anoshin** 30:24 You have to put it on the pull request?
**Donal O'Sullivan (Elastic)** 30:25 Yeah, yeah, so, well, yeah, so the example was, so, I'm testing… so I have this in, in, in the collector.
Core, obviously, updating mdatogen, and I'm just testing it in… in Host Metrics Receiver.
So the example was the… CPU logical number, is the… attribute, being used by, system CPU time.
Whereas if you look at that attribute being used in host metrics receiver, the legacy attribute is just CPU, and it's a string, but CPU, that logical number is an int, so it's something I have to cater for, if that makes sense.
**Dmitrii Anoshin** 31:06 But that example, is that real example? If it's not real, if.
**N'at (us-pit-bak)** 31:09 Well, that's actually happening right now, I think is what he's saying.
**Dmitrii Anoshin** 31:11 Yes.
**Donal O'Sullivan (Elastic)** 31:12 Yeah, yeah, yeah.
I'll double-check that. Look, that might not be real, but from what I could see, it was, so it's just something… it's just a case I had to handle in m.ogen. But let… yeah, let me get back to you about that, so to see if it's… if that's actually, Sweet.
**Dmitrii Anoshin** 31:32 How can I drop? Thank you, folks.
**Christos Markou** 31:39 See ya.
