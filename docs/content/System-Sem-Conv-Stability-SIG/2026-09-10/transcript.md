SIG: System Sem Conv Stability SIG
Date: 2026-09-10
Duration: 30 minutes
============================================================

## Zoom Recording Transcript

**Dmitrii Anoshin (Splunk Inc.)** 04:20 Hello, everyone.
**Donal O'Sullivan** 04:26 How's it going?
**Dmitrii Anoshin (Splunk Inc.)** 04:29 No, no, thank you.
How are you?
Do we have anything on the agenda today? Sorry, I don't… I didn't… I don't see the notes yet, but if we don't, maybe, Roger, we can discuss the Slack thread that you… Started today. Or we can add it to the end of the agenda.
**Roger Coll** 04:54 Yeah, I will add it, just open the doc, and it seems Donal has something to share, so… Yep.
I really love Should we… start already, I think it's past 5.
**Braydon Kains (he/him)** 05:19 said he'd.
**Roger Coll** 05:20 Join a bit, so… Oh, okay.
**Braydon Kains (he/him)** 05:27 We can probably start with Adam.
**Dmitrii Anoshin (Splunk Inc.)** 05:31 I will have to drop maybe in, like, 10-15 minutes.
**Braydon Kains (he/him)** 06:11 Is it… Possible, maybe, that you could… Remind me what… why… There's so much precision.
was a problem. Like, I remember… I remember going through this in a few other scrapers where we El Salvatar had done a bunch of work to… Allow for ratios that removed some of, like, the heavy amounts of digits of precision after the value.
And I'm… I can't remember why we decided that was… worth it? Like, in… it's not like it's… like, it's still a float64, it's not like it's more data, so I was wondering if I… if we could… you could remind us why… Like, where that heavy precision actually is causing a problem.
**Dmitrii Anoshin (Splunk Inc.)** 07:03 I actually have exactly the same concern, and I don't understand, like, all of the work that's happening. I think we should revisit whatever was merged before, because we are… I don't think we've made it better, essentially.
With those, like, Draw-dropping of the, digital.
**Braydon Kains (he/him)** 07:22 Like, in a vacuum, I'm actually okay with adding computing usage via ticks as an option just separate from this precision thing. Like, I can see a reason for that, but the precision thing, I still just, like, my brain isn't computing the problem.
**Roger Coll** 07:41 Yeah, I don't remember the precision at the moment, either, that we… we did for the memory.
can revisit the PR.
But I think in this case, it's another story, right? If I remember correctly, it's the… it's the precision with the ticks, right, and the… the use… the hertz that the CPU is going, so basically, I think that in Procostat.
You have the ticks of the CPU, I'm… let's say that, if I under… if I remember correctly, GOPS Utils, basically devise that for the… for the… for the clocks, or the CPU clock, right?
And it gives us the floats. And if I understand correctly, when we are computing the deltas, dividing the floats by floats.
Seems that we are, let's say.
Adding… and adding more, digits that… Into the… into the final value that are not needed, let's say, and these are introduced because of the arithmetics of the floats.
And it seems that if we have the ticks beforehand for computing the utilization.
Basically the… we can reduce a bunch of floating digits. I think that was the… the idea behind this PR.
Maybe what it can help, maybe I can ask, salvatore for some, For some numbers, some real numbers, and… exactly see the… the difference there. I think he… he did it already internally, and so the, let's say, that the producing numbers are… cost much less digits, let's say.
But maybe we can… we can put a… a guest somewhere with the… With the actual numbers, if that helps.
**Braydon Kains (he/him)** 09:57 I think I'd be in seeing that, because the only thing I could think of is Like, does the, does the Go runtime… do more work if the float 64 has more precision? Like, does it take more work on the processor to do the floating point math or something?
**Roger Coll** 10:19 No, I think it's not related to the work that the runtime does.
It's more on the, let's say, on the resulting value for the utilization that it seems that we are carrying over.
Some visits that are, let's say, arithmetic redundant.
I'm… Because of the floating operations, but…
**Donal O'Sullivan** 10:46 I… Yeah, the actual issue is when you do a float calculation and you cast it, so I think the division might be casting the two floats and then doing… so if you cast a float to an integer and you divide it on both sides, you'll get a different… you'll get a wrong result, versus if you do the float division, then cast, I think that… is that not the actual issue?
**Braydon Kains (he/him)** 11:05 That does sound wrong. Is that what we do?
**Donal O'Sullivan** 11:09 I think that's how GoPSUtil is doing it.
**Braydon Kains (he/him)** 11:12 Oh.
**Dmitrii Anoshin (Splunk Inc.)** 11:12 That's the issue for the latest PR. Exactly, and that's why we are trying to get to the ticks instead, because in that case, like, we have two integers.
And then we get, like, more precise result. But the work before that was done when we just drop some amount of… when we actually Let's call it round to a particular like, mantis of the float, that work. I would assume in some… it's just a runt approach, essentially. Like, this approach, when we want to switch to ticks, gives us a correct result. But that approach, probably solving a similar problem, but for some calculations, it can make calculations more correct, but for others, it, like, it actually makes them worse. For others, I mean where there is, like.
When the part that is being dropped is not Meaningful. It's actually meaningful.
But we still drop it.
Right. And for those, we are doing it, making it worse.
So, it's like… the whole approach, I think, is incorrect. But for this one, for the ticks, it kind of makes sense, but at the same time, do we really care about the error of, like, minus… 10, magnitude, which is, like, 10… 10 digits after… after 0, I don't know.
I, I think we… we should not care.
**Roger Coll** 12:56 Is that the error?
**Braydon Kains (he/him)** 12:57 error margin we're talking about, like a 1E minus 10?
**Dmitrii Anoshin (Splunk Inc.)** 13:00 Exactly, for the latest PR, yes. When we switch to… Okay.
and compute integers first, and then we cast it to float. Because GOPS utils cast to float, like, the actual ticks and the total, whatever is being used for that, and then do the division. That's where the error comes from.
And it gives us error of, like, yeah, 90 inches, after the dot.
**Braydon Kains (he/him)** 13:34 That seems pretty small.
Like, I'm just wondering if it, like, if that issue compounds, like, if we're getting… Procstat has CPU ticks… for the whole CPU, not, like, per core, right? It's… for the… It's for the whole CPU, I think.
Man, I'm so fuzzy on this part. It's just, I'm thinking, like, if we're… if we calcul… if we do that calculation, like, per core, and there's 16 cores.
Each one has, like, a 1E minus 10 error margin, but as we start to calculate the utilization across all the cores and get, like, a proper full CPU utilization, could we be off by a more significant amount if we keep on doing… if that error margin is on each core, and then we compound all the cores? I'm not sure if that is significant or not.
**Dmitrii Anoshin (Splunk Inc.)** 14:29 Yeah, minus 8 at max.
**Braydon Kains (he/him)** 14:33 It's still not that much.
**Roger Coll** 14:38 Yeah, I think we did it for each core, right? I think the core is an optional attribute.
I don't know, actually, on the results. I can… maybe I can ask on the Salvatore, let's say. I know that he… he tested, and it seems that the the storage in Elasticsearch and the compression that then later they apply.
It seems to be better, but I'm not sure about the actual, let's say,
**Dmitrii Anoshin (Splunk Inc.)** 15:08 Yeah.
**Roger Coll** 15:08 trunks.
**Dmitrii Anoshin (Splunk Inc.)** 15:09 I think I looked at Lucy and what it does is actually converts them to integers at the end with some kind of a precision. So, it actually helps specifically for Elasticsearch.
But I don't think that that's the problem of the receiver. I think it should be translated somewhere downstream. At the receiver side, we should just, like… we should not care about the, Representation, we should care about just, like, correctness.
And yeah, if we say that minus 10 is something that we care about, we can switch to ticks, but this… precision dropping.
And that was done before, that one is… I think that should be reverted.
**Roger Coll** 15:57 Yeah, but then the… let's say that if… even if it's just, let's say, very few of the correctness, you would push back because of the Let's say, manual parsing of the profile system.
Yeah, cool.
**Dmitrii Anoshin (Splunk Inc.)** 16:12 Because GoCills has, like, they… they follow all of the… like Linux and the other OASs in journals, and if something changes, they could care about that, and we just update to the latest version, and we get the support out of the box. And now we have to do that work by ourselves.
Which, we don't have enough of, like, attention to.
address here, I guess.
That's my concern.
**Roger Coll** 16:42 Okay, yeah, just two things. The first one, I think that we cannot move that, let's say, downstream on the pipeline. I think I added this comment.
on the PR from another discussion that we had.
And in the GOPS utils, maybe… Let's see if they agree on adding that on the… Let's say the… the extract, but basically it's the mechanism in Opsutil to get Linux-specific, Fields, and maybe if they agreed on having the ticks there, we could use that one.
We solve the maintainability concept.
**Dmitrii Anoshin (Splunk Inc.)** 17:27 Yeah, at least we don't have… we don't even have an issue submitted again, scope, right? It would be good to have…
**Braydon Kains (he/him)** 17:33 Yeah, exactly.
**Roger Coll** 17:34 Morning.
**Dmitrii Anoshin (Splunk Inc.)** 17:38 It would be good to have an issue there and see, like, there is an explicit rejection.
**Roger Coll** 17:46 Oh, good.
**Dmitrii Anoshin (Splunk Inc.)** 17:47 Beautiful.
Using integers before casting to float.
for the division. It kind of makes sense, like, why wouldn't… I mean… Maybe if… In some cases, when… Division doesn't end up with, Like, the number… integer number, so if there is a loss after that decision, after that division.
Maybe that was the reason? Like, for example, you divide 3 by 10, or something like that.
Oh, sorry, yeah, Blake.
10x3 or something like that, but I don't believe it's possible.
According to Salvatore, it seems like the… The total value we… Here's what the division, as always.
Like… Yeah, it doesn't produce those results that I mentioned.
But yeah, it would be good to see what the feedback from… from GovC.
**Roger Coll** 19:03 Yeah, I guess ScopGTL gives a flow, maybe, because in other… systems, it's already computed by the OS.
**Dmitrii Anoshin (Splunk Inc.)** 19:13 Oh, okay.
**Roger Coll** 19:15 I mean, that might be, yeah, the reason.
**Dmitrii Anoshin (Splunk Inc.)** 19:22 Yeah, in that case, the pushback should be consistency, and if it's clear from them, hey, we don't want to overcomplicate the code, then at least we get a clear signal from them.
But otherwise, potentially can go there, right? They can… for Linux, they can… Use a different approach.
**Roger Coll** 19:41 Okay, sounds good. Let me push, then, this issue and get some feedback from them. I will also check what the… Prometheus, proc FS package, gives to the user.
Because I think this is, like, the Linux by default, reader for ProcFS.
Yeah.
**Dmitrii Anoshin (Splunk Inc.)** 20:03 That'll be good to see as a reference.
**Roger Coll** 20:06 But yeah, sounds… okay, then I will keep an eye on that and see, you know, where can we go.
**Braydon Kains (he/him)** 20:13 GoPS Util already does the proc stat parsing, so the problem is just about, like, we want them to expose the specific numbers, right? Like, they just… they don't have it in the API right now, and we want them to expose it.
**Roger Coll** 20:28 No, dude.
**Dmitrii Anoshin (Splunk Inc.)** 20:28 we want them to change the calculation, right? We want them to use integers for the division first, and then cast the float, is that correct?
**Roger Coll** 20:40 Yeah, correct, but I don't… probably they… they cannot do it in the… let's say in the main API, we might need to use, like, the Linux-only one, that I think it… this is something that, Braydon New Shirt on… well, in one of the SIGs.
that it's a pattern in OPS Util to just… name it X, and then the platform, and… In that sense, you can get the platform-specific values, because probably they cannot change the… D times struct API for all the platforms at the moment to do.
That's good.
**Braydon Kains (he/him)** 21:23 That's what I was thinking, if they could… if they could have, like, a Linux-specific struct where they give us the… the ticks directly from proc stat, then we could do the math that we want, rather than having to force the calculation downstream. Like, at least we'd… we'd inherit the proc stat reading from GoPSUtil, and then if we needed to do different math, because we disagreed.
like, that's not nearly as much of a lift as we have to now parse procstat ourselves and have, like, a map-per-kernel version of what we're reading like that. It sounds annoying. I'm actually not completely opposed to doing that if there was a good reason. I'm… I'm just struggling to parse… like, what we're really gaining from it is… that's the blocker for me. I'm not getting it.
**Roger Coll** 22:10 Okay, then let's do this couple of things. I will push the GoP as utils their opinion as well, and secondly, ask for maybe some Benjamas on exactly what we are gaining.
Not if they… If we are gaining precision, and we are reducing the digits and copies utils, it's fine. Yeah, we can move on.
Yeah, thank you.
**Braydon Kains (he/him)** 22:43 I think that's my biggest question, is just, like, this level of precision. Like, the only perspective I have is the Google backend, and… The Google backend does not care. If you give a float64 with lots of digits or not, it does not matter.
**Roger Coll** 23:00 I'm.
**Braydon Kains (he/him)** 23:00 I'm curious why… why it does on a different backend.
**Roger Coll** 23:04 Okay, sounds good. Yeah, sounds reasonable.
**Dmitrii Anoshin (Splunk Inc.)** 23:09 I gotta drop. Thanks, folks.
**Roger Coll** 23:11 Thanks again.
Yeah, I think probably that's it for this topic.
Sorry, Dano, you wanna go next?
**Donal O'Sullivan** 23:28 No worries, Roger. Yeah, so I had a PR there to promote the system attributes to release candidate that we use for system metrics and host metrics receiver, and… Got a bunch of approvals, but Lalidma pushed back with some open issues. I just linked them there. There's… there's some of them… I know we don't have much time, but I'll… I can… put in the Slack channel as well, but just at a high level.
There's, system device, I know there was, like, an open issue around that to merge that with, Was it hardware ID, or maybe namespace system device? So instead of system device, it'd be like system device ID, or system device name.
So that's one… I don't know, does anyone have any thoughts on that? I think maybe namespacing it makes sense to me, but…
**Braydon Kains (he/him)** 24:20 I… anything to do with hardware, I'm always like, man, the hardware namespace is killing me, man. We never look at it, everybody wants to use it, but… like, it's old, and hasn't changed in ages, and probably doesn't follow all the rules, so… Yeah. Whenever it comes to, like, should we merge stuff with hardware ID, or align it with the hardware namespace, I'm always like, I don't… I don't know. We need to have…
**Pablo Baeyens** 24:49 I don't think we need to decide on merging with Hardware ID now. Like, we'll do that whenever we want to stabilize that part, or… Or removal.
**Donal O'Sullivan** 25:00 like, the other idea was namespace system device, so you have… instead of just system… so at the moment, the attribute is system device, so we changed that to system device ID, or system device name, which I think is… Better than merging with hardware.
Because you could have a system device that's virtual, it's not hardware, right? So, like, I think that doesn't make sense to merge it with hardware, like… You could have a hardware device, and then a virtual system device, but it may not be a hardware device, so how do you merge the two?
**Braydon Kains (he/him)** 25:31 Oh, is that what they're saying? So, yeah, that, I think, is just a misunderstanding of what… system.device is, because, like, we're… system.device is used for, like.
network interfaces and… and memories and stuff like… stuff internally. It's very Linux… Linux-y, that… or I guess Unix-y is the way you'd call it, very Unix-y, that… that… verbiage of system.device, but yeah, device is not the same as, like, my phone is a device. So that… I think that's maybe just a misunderstanding.
And we can… we can probably clear that up by at least improving the system.device description, if not doing… making the change to system.device.id, I think that's fine.
Yeah.
It's possible that device ID and device ID… device name are separate.
**Donal O'Sullivan** 26:23 Hmm.
**Braydon Kains (he/him)** 26:24 I mean, you kind of see both usage of the verb, but, like, You might call… the device name SDA1, and then the device ID slash dev slash SDA1, or, like, the actual… Thing that identifies it on the system.
Maybe I should… look… A little bit at some, like.
Some writing on that, and see if… see if ID and name really are considered separate things, or if people just call it always ID, and if the ID attribute should just always be the full device path.
Yeah, yeah.
Like, I think from Luke.
**Donal O'Sullivan** 27:03 Currently, we just…
**Braydon Kains (he/him)** 27:04 God.
**Donal O'Sullivan** 27:04 do the name.
Sorry to interrupt you.
**Braydon Kains (he/him)** 27:07 Yeah, that's fine. I think right now we just do the name, I think.
**Donal O'Sullivan** 27:10 Yeah, yeah, I believe so.
But it's just system.device, there is no, like, namespace with it, it's just, like, an attribute.
**Braydon Kains (he/him)** 27:17 Yep.
Okay, yeah, let me take that issue and respond to it.
**Donal O'Sullivan** 27:25 Cool, cool, thanks, thanks, Braydon. There's just quickly a couple other things, so, like, CPU, logical number. I know there was talk of wanting to add core to the description. I think that doesn't make sense to me, because you can have a logical… Number versus the actual… like, you could have a hyper-tighted system with, like.
16 cores that only actually has 8 physical cores, so I don't think there's any point in adding core to the description.
**Braydon Kains (he/him)** 27:52 That is… that is the point of logical numbers, that it's representative of the virtual cores. And so maybe that's what we say, like, just make that more explicit, but…
**Pablo Baeyens** 28:03 I, I… I put a comment there, but, like, I don't think we need to spend a lot of time clarifying the descriptions if they are It's clear to us, like, It's nice to do that eventually, but, like, I don't think it's necessary for… really is going to… Wow.
**Braydon Kains (he/him)** 28:24 I think as long as it's not immediately confused with something else, I think that's the case.
**Pablo Baeyens** 28:29 Right, like, yep.
**Braydon Kains (he/him)** 28:30 if it was… if it was reasonable for someone coming in with no context to see CPU logical number, and then something else that could mean the same thing and not know what the difference is, then we would want to clarify the descriptions, but… I think the idea of CPU logical number, like, it's the only thing in our namespace, as far as I know, that could possibly mean virtual cores.
**Donal O'Sullivan** 28:54 Yeah, yeah, that makes sense. I know with the interest of time, we're gonna run out there, so there is a list on the… on the system attribute promotion PR, of… Issues that Lalidma found, so… I can post them in the Slack channel or something like that, and we can, I don't know, async, just take care of it, or… Or what do you… what do you think?
**Braydon Kains (he/him)** 29:20 I think that's okay. Putting it on the Slack is good. I think of the issues here.
the ones that… we definitely, definitely could do with the dressing, or the system device one, and the CPU namespace one, which… I opened and then lost track of, but I will… I'll follow back up on it.
**Donal O'Sullivan** 29:46 Thanks, Braydon. Appreciate that.
Yeah, that's all I have.
**Braydon Kains (he/him)** 30:01 Okay, if that's everything, then we can go. Also on my list is the host IDPR, I saw there was new movement on that, so I will take a look at that soon.
**Igor Peschinskii** 30:10 Thanks.
**Pablo Baeyens** 30:10 Yeah. There was also a PR from Ludmila marking it as the identifying attribute for the host entity.
Yeah, I think that should not be controversial, so…
**Braydon Kains (he/him)** 30:20 Yeah, that's fine. I think that is our intention, so… Alright, thanks everybody.
**Roger Coll** 30:29 Figure.
**Donal O'Sullivan** 30:30 See you guys.
