SIG: System Sem Conv Stability WG
Date: 2025-10-23
Duration: 30 minutes
Zoom Recording URL: https://zoom.us/rec/share/riyOIAZKi4S7bxw7kQtRYVVM2vyX8L4DLGZAfrWi2ZNuYjCJuYQLYrhHQrE15b63.Lhn9CCgNhtZRVqsX
============================================================

## Zoom Recording Transcript

**Pablo Baeyens** 00:31 Hey.
**Christos Markou** 00:35 Hey, hello.
**Pablo Baeyens** 03:22 I guess we can… Sorry, if there are nasal peaks.
**Christos Markou** 03:42 Probably checking the board if there is anything… no, if there is nothing else.
**Pablo Baeyens** 03:58 Back on TikToks.
Huh.
Yeah, and I also wanted to know if there's any…
guidance from above in terms of the…
**Braydon Kains (Google)** 04:13 Okay, good to you.
**Pablo Baeyens** 04:14 I see recommendations, or… How does that affect semantic conventions? I don't know if that's something… Josh, maybe new.
Thought about, or… Or not.
We can do that after taking the board.
**Josh Suereth** 04:30 Can you say that again? Sorry, I'm on my… on my phone, my computer audio is having trouble today.
**Pablo Baeyens** 04:36 Yeah, no, I was wondering if the…
semantic conventioners have thought about the TOC recommendations, and if there's anything that is going to change, or, like, that we should focus on.
**Josh Suereth** 04:54 Yeah, I don't think we've discussed it specifically. I can tell you my own thoughts are, I've been going through a list of all the areas of OpenTelemetry.
that a reasonable adopter of OpenTelemetry needs.
And… and looking through, do we have something in place to stabilize that area or those needs for a reasonable adopter of OpenTelemetry as quickly as possible? We do… we have been on a journey with semantic conventions to make sure it's very clear what's stable and what's not.
But I don't think it's really clear to downstream consumers, and so, yeah, there's work to do there as the TLDR. So, this is an example, SIG, of, I think we need to get to a point where things are stable, and we need to ask ourselves, like, okay, of the work that y'all have done, right,
how much of that board is really necessary to unblock an average adopter of OpenTelemetry?
And let's nail that as quickly as we can, and then… and then have a clear, okay, here's what's stable. And then we can work on the rest over time. But from my perspective, we have way too much that is considered unstable that people depend on, and we have to start addressing that as quickly as possible.
I haven't really thought through other alternatives besides just collecting the list for now.
**Pablo Baeyens** 06:18 Okay. I mean, I guess we can check the board on, like, seed with this new perspective.
I don't know, I can share my screen if…
Actually, if somebody else can share the screen and share the board, I would appreciate it.
**Dmitrii Anoshin** 06:44 I can do that.
Systematic conventions, right?
Systematic Convention's one, yeah.
**Pablo Baeyens** 07:11 And we can look at the… the GA…
So if you… See the tabs, below the…
the board name. There's one that says GA Board.
**Dmitrii Anoshin** 07:33 Okay.
**Pablo Baeyens** 07:37 And I guess we can start with the ones in review, and then… Will… Look at the others.
Does this one have a PR open?
**Braydon Kains (Google)** 08:00 The… the paging…
Paging one is done, the process state one, I don't think it's a PR yet.
**Pablo Baeyens** 08:12 Huh, okay.
**Christos Markou** 08:13 Is this ready?
state… I believe there was something missing, or at least, that's what the…
Issue was stating some time ago.
**Dmitrii Anoshin** 08:27 There is a PR to rename process state attributes.
**Braydon Kains (Google)** 08:30 Oh, yeah.
**Dmitrii Anoshin** 08:32 Okay.
**Braydon Kains (Google)** 08:35 Oh, and I… we're trying to…
Get them not to do the briefs, because…
The briefs are explaining something that's obvious from the Value.
ends.
**Dmitrii Anoshin** 08:48 Yeah, and I think that's addressed. So, Chris just can take another look, and we can do that as well, I guess.
I'll put it on my queue.
**Christos Markou** 09:01 I will check.
**Dmitrii Anoshin** 09:05 So, yeah, this one is clear. There is work that we can do.
On this one.
And, this one…
Memory… rename… Okay, I'm not sure we've been through a lot of discussions about this one. Are we, like, aligned now that Linux goes after?
**Braydon Kains (Google)** 09:29 Yeah, I think so.
**Dmitrii Anoshin** 09:30 Okay, cool. So, there is PR…
With this one, that we need to…
**Pablo Baeyens** 09:37 Yeah. The other one night.
**Braydon Kains (Google)** 09:39 Oh yeah, I guess we could probably…
I'll probably close this issue, I get… I don't know if I…
If we ever specifically, like, decided that, like, oh, now, like, we've officially, like, said that the OS comes second, it's just, like, the discussion kind of stopped, I guess.
**Dmitrii Anoshin** 09:58 Okay, can we maybe summarize that semantic? I remember that we, like, at least within this group, we decided that,
Oh, we… Like, operation system goes second, so maybe we can just…
State our decision here, and
Close it, what do you think?
**Braydon Kains (Google)** 10:18 Yeah, sure.
**Christos Markou** 10:20 Covered by guidance, Brighton, that you created.
Oh, I remember.
**Braydon Kains (Google)** 10:27 Yeah, in our non-normative guidance, I think I did write
I wrote the reasoning that I thought it should be that way, but people didn't, like…
super agree with me, I think?
In the maintainers group.
**Dmitrii Anoshin** 10:40 Did you merge that?
**Braydon Kains (Google)** 10:42 Yeah, it's in docs slash non-normative, Slash… Group slash system.
**Dmitrii Anoshin** 10:52 Ugh.
**Braydon Kains (Google)** 10:54 It's in the…
**Christos Markou** 10:56 Design?
**Braydon Kains (Google)** 10:57 design, I think.
**Dmitrii Anoshin** 11:01 Okay.
Okay.
**Braydon Kains (Google)** 11:26 Yeah, maybe I didn't explain it here.
**Pablo Baeyens** 11:32 Yeah, if you go above it… There's a bit more… Text on that, so… Where is it?
There's somewhere where it says this section, and then it links to the process C group.
Thing.
Or maybe I'm not looking at the same.
**Dmitrii Anoshin** 11:57 This one?
**Pablo Baeyens** 12:01 Right, yeah, so there… it talks a bit more.
But, yeah, it's not super explicit.
**Braydon Kains (Google)** 12:14 Okay, oh, Opera, is it…
**Pablo Baeyens** 12:17 Oh, operators.
**Braydon Kains (Google)** 12:18 System in names, is it this section?
**Dmitrii Anoshin** 12:21 Yeah, yeah, this one, actually. Alright.
**Christos Markou** 12:31 Yeah, it says we will not have Linux.
**Dmitrii Anoshin** 12:34 That's cool.
Okay, in this note.
**Braydon Kains (Google)** 12:40 And the reason for that was that we didn't… want.
Like, the root namespace… You still want it to be…
if it's a memory metric, but there's some Linux-exclusive.
**Dmitrii Anoshin** 12:55 Okay. Special thing, like, the memory available.
Okay.
**Braydon Kains (Google)** 12:59 want to have to look in the Linux namespace to find that information. That's basically…
**Dmitrii Anoshin** 13:03 Makes sense. So I'm just closing this by… this PR actually closes this issue, I guess, right?
**Braydon Kains (Google)** 13:10 Yeah, I guess so.
**Dmitrii Anoshin** 13:12 Okay.
SSS.
This is absolved by…
And now we are…
Okay, any doubt about this one?
It's still… Okay, we have a guidance in place, but we still don't have…
**Braydon Kains (Google)** 13:43 But I guess this… this rename still needs to be…
**Dmitrii Anoshin** 13:47 Still in place?
**Braydon Kains (Google)** 13:49 I think s'… So…
**Dmitrii Anoshin** 14:03 Okay, let's register, yes, it's still in place.
Okay.
**Braydon Kains (Google)** 14:10 in this Linux directory, so likely we will…
**Dmitrii Anoshin** 14:13 Yeah, it's here, right?
**Braydon Kains (Google)** 14:15 Boulder, you know?
**Dmitrii Anoshin** 14:16 This is, like, actual what we have in semantic conventions, so…
**Braydon Kains (Google)** 14:20 Yeah.
**Dmitrii Anoshin** 14:20 Has to be updated.
Let me mention this.
VR again… Another major guidance.
Just mentioning here.
**Braydon Kains (Google)** 15:03 this…
**Dmitrii Anoshin** 15:05 Pass.
There's no… And be renamed… Yeah, and that we have the… guidance…
So… Is Roger on the call?
**Roger Coll** 15:32 Yeah, I can… I can work on that one.
**Dmitrii Anoshin** 15:34 Okay, awesome, thank you.
Nice.
So this one can be closed, and go back to the board.
Okay, this one is probably in progress, right?
I guess.
**Roger Coll** 16:01 Yeah, better.
**Braydon Kains (Google)** 16:02 Yeah, I think so.
**Dmitrii Anoshin** 16:03 that they don't have a PR.
And this one is…
**Braydon Kains (Google)** 16:10 This is the one that has a PR, I think.
**Dmitrii Anoshin** 16:14 Okay.
Yeah, we'll take a look.
Then we have introduced information and optional normalized total CPU utilization magic.
Okay, this is what I've been working on.
I'm… the PR for CPU being opt-in. A CPU number being opt-in is now… Mersked?
What is this?
Okay.
I found this PR, completely forgot about it.
Okay.
**Roger Coll** 16:55 I guess the only part missing is the aggregation strategies in the collector, right?
For the CPU utilization metric.
**Dmitrii Anoshin** 17:11 Sorry, what do you mean?
**Roger Coll** 17:12 No, no, I mean for the other issue, the one about introduce an option, yeah, that one.
I guess the only part missing is the… Aggregation of stress, yeah.
**Dmitrii Anoshin** 17:26 Yeah, aggregation itself, and then, yeah, I've been working on that.
I'll probably have another PR today, like, towards that direction, but eventually we need to ping the person who submitted the original PR I've done.
some work…
**Roger Coll** 17:41 Okay.
**Dmitrii Anoshin** 17:42 like, guiding him and everything, but I believe she's now on PTO.
So… Let me see… oh, look, I have it referenced in my PRs.
And.
**Christos Markou** 18:00 an issue for SamConf, or…
Do we need anything on SEMCON's side to do?
**Dmitrii Anoshin** 18:06 No, we don't think… actually, you're right, it's like, it's something that would block collector migration, but it's not… it doesn't have to do anything with the sameconf itself, so…
**Christos Markou** 18:16 Right.
**Dmitrii Anoshin** 18:17 Yeah, anyway, I'm on it, probably.
Pew.
Oh, shut up.
**Christos Markou** 18:24 Can we close this then, or just mention that it will be covered directly from the implementation?
Shoot.
Yeah, if there's nothing to be done, Shamcon.
Maybe.
**Dmitrii Anoshin** 18:38 I'm, like, this issue is big, I'm, like, I'm not sure if utilization of opt-in completely covers it. Roger, what do you think?
**Roger Coll** 18:50 I think so, but probably I can double-check it with the PR that we have in the collector, and then cross it.
Okay. So, results.
**Braydon Kains (Google)** 19:01 I also had a…
a gist that I wrote up related to this, and I haven't gone back to fix the feedback on it, but…
**Dmitrii Anoshin** 19:09 Okay.
**Braydon Kains (Google)** 19:10 It was… it was the, sort of, explaining…
like, here's how utilization is calculated. You should use CPU time if you can, but if you really need to graph CPU utilization…
you have to do a moving average over a window that aligns with the sampler rate. There's a few things in there. I'll link it here, but I will…
try and get to fixing up that gist, so that maybe we can include the guidance somewhere in our…
**Christos Markou** 19:38 Yeah.
**Braydon Kains (Google)** 19:38 too.
**Christos Markou** 19:39 There is guidance for this, by the way, not for this specific one, but for, the CPU usage, CPU time, CPU utilization one, and yeah, Brighton, I… when I sent the PR, I also included some of your parts.
**Braydon Kains (Google)** 19:56 Oh.
**Christos Markou** 19:57 That's good.
**Braydon Kains (Google)** 19:57 Okay, I think I must have missed that one.
**Dmitrii Anoshin** 19:59 Can you… is that PR merged, Christos?
**Christos Markou** 20:03 Yeah, it was merged, like, weeks ago, but…
**Dmitrii Anoshin** 20:07 Can you please send me…
**Christos Markou** 20:08 Who's linked to the… Yeah, the issue that you were checking before.
**Dmitrii Anoshin** 20:14 Okay.
**Christos Markou** 20:15 That was… Closed.
The other one, probably linked into this one.
**Dmitrii Anoshin** 20:21 If you go down…
**Christos Markou** 20:25 You opened another one, which is about opt-in guidance, whatever.
**Braydon Kains (Google)** 20:30 Oh, I remember this now.
**Dmitrii Anoshin** 20:33 I see, I see. Yeah, I remember I opened it, let me find it.
**Christos Markou** 20:39 It is linked on the bottom, you find it from there.
**Dmitrii Anoshin** 20:43 Sure.
This one?
**Christos Markou** 20:44 More to the bottom. More to the bottom.
**Dmitrii Anoshin** 20:47 This one?
**Christos Markou** 20:48 Oh.
**Dmitrii Anoshin** 20:50 No?
**Christos Markou** 20:51 It's like, yeah, addition, guidelines, whatever.
**Dmitrii Anoshin** 20:55 Oh, okay.
Okay, both. Thank you.
**Christos Markou** 21:00 Yeah, it was merged. If we see niche improvements, we can… Chronic News.
**Dmitrii Anoshin** 21:07 Just wanted to quickly check it.
**Braydon Kains (Google)** 21:09 I think the only thing is that the… when I first wrote those PromQL queries, I didn't realize anything with a dot needs to be surrounded in quotes, so we can…
**Dmitrii Anoshin** 21:18 We can… I'll… I'll just…
**Braydon Kains (Google)** 21:20 Quickly submit that fix to the dock, but…
**Dmitrii Anoshin** 21:22 I like this. This is what we're discussing, and what we decided to do, because this one is, like, the raw metric code, you can do anything with that. You can aggregate temporarily, spatially, whatever you want, but this one is complicated, this one is complicated, this one is complicated, this one.
easier, but… but, Christos, question to you. I believe in Kubernetes, we have only this one, we don't have time.
**Christos Markou** 21:48 We'll have time in Kubernetes, we also…
But, with there is that it's coming directly from Kubelet.
stats API, and it is calculated in a very good way, but with namespace, so it's quite straightforward that we are deriving it from this API, so we don't calculate anything on our side to make a.
**Dmitrii Anoshin** 22:13 Okay.
**Christos Markou** 22:13 complicated.
**Braydon Kains (Google)** 22:14 Yeah.
**Dmitrii Anoshin** 22:15 So we still need to make that…
**Christos Markou** 22:17 mentioned here.
**Dmitrii Anoshin** 22:19 Okay, so we need to make some changes to the human rights matrix.
**Christos Markou** 22:25 I think they are open.
Yeah, we will need to change them, to revisit them and fix them accordingly. This specific… Sure, go ahead.
**Dmitrii Anoshin** 22:36 I won't say, at least on the collector, I'm pretty sure we emit both by default, so we would need to update semantic conventions and update the collector code in that case.
**Christos Markou** 22:47 You mean, yeah, in the collector, that usage is…
Is this by default? Probably, yeah, I will check.
**Dmitrii Anoshin** 22:55 I remember they're both by default, enabled by default, so it's probably maybe aligned with…
With the transition to new semantic conventions, or we can do it quickly, sooner, that should be fine as well.
Okay. Okay. Thank you.
**Braydon Kains (Google)** 23:09 Yeah. Does… so does this document end up saying that? I actually forget, but it says, like, because CPU usage in Kubernetes is just a pass-through from Kubelet, it's, like…
It's… better than… When you aggregate it in your own instrumentation or something.
**Christos Markou** 23:27 I tried to cover this… I tried to cover this in the doc there, so this, Kubernetes-specific one was explicitly mentioned as an exit.
The thing is that, the kubelet itself, does the aggregation, based on a specific interval, 10 seconds or something like this, so it's safe to just…
collect this directly. And since this is prefixed with a Kubernetes namespace, it…
But for system, for example, because we would need to decide on the interval and all that stuff, so…
It's better if we skip this.
**Braydon Kains (Google)** 24:12 Yeah.
**Christos Markou** 24:12 So, the rationale is that if something can drive from an API directly, then that's fine to have… to have this. If not, then it's, up to users to calculate this on their balance or whatever.
**Dmitrii Anoshin** 24:26 Makes sense.
But still… Cool. So I guess, yeah, this is… This is good.
We would need to… Yeah, we'll follow up on this one, I believe, and can close it.
**Braydon Kains (Google)** 24:44 Probably just to, like, make the change based on the
the guidance suite ended up merging.
**Dmitrii Anoshin** 24:51 Sounds good.
And,
What is this one? Why is it locked?
Bullard by entities. Ross of entities. Okay, it's on me.
Yes.
**Pablo Baeyens** 25:19 I think we had a rough idea, though, of what we wanted to do here. Like, we knew the required attributes.
The PID and the timestamp?
**Dmitrii Anoshin** 25:32 Yeah.
So, identifying attributes, we have them, we decided on them.
So… Define common attributes and requirement levels.
But this one is specifically about requirement levels. Is that… this is actually a question that is still confusing to me. Maybe, Josh, you can help answering. Do we say that required resource attributes
are the same as identifying attributes of the entity, and the recommended attributes are descriptive.
**Josh Suereth** 26:09 This is a good question. We… we have toyed with that notion, but we haven't pulled the trigger on it. So, I… I am not convinced that required has to be identifying. I think it's possible we could require descriptive attributes.
That are important for you to do navigational.
things that are not the identifying attribute. I think that might be a thing that we do. So, I do think that right now, all identifying attributes have to be required.
So, like, if you're gonna take that dance, I would focus on the required recommended opt-in level for descriptive attributes, and then all identifying should be required, and that's what I would do.
**Dmitrii Anoshin** 26:49 I actually, working on metadata gen, you know that, in the collector, and introducing entities there, and I'm following the same idea, that at least all identifying attributes has to be required.
Okay.
Cool, but in that case, this one isn't blocked by entities. At least we… we have to make…
timestamp and PID required, and then we can decide what else is required, recommended, or optional.
**Braydon Kains (Google)** 27:22 You can… you can assign this one to me. I'll… I'll look over it.
**Dmitrii Anoshin** 27:27 Awesome, thank you.
Cool, thank you.
I guess this is not blocked anymore, right?
**Braydon Kains (Google)** 27:40 I don't think so.
**Dmitrii Anoshin** 27:41 I think we… we know what… we know enough to actually be able to.
**Braydon Kains (Google)** 27:44 To move forward on that one.
**Dmitrii Anoshin** 27:46 But, follow-up question, Josh, I had looked through the Weaver definitions in our semantic conventions, and I haven't found where we distinguish identifying attributes from required attributes.
That's not…
**Josh Suereth** 28:02 In the midst…
**Dmitrii Anoshin** 28:04 It's not there yet, right?
**Josh Suereth** 28:05 There's a VQ schema that'll make it obvious. It is actually there. So, on the attribute ref that you declare, there's a role that you can put on an attribute. And so, if you want an example, look under model slash service.yaml, and you'll see, you'll see an example. So, yeah, under semantic conventions.
We don't require it right now, but we do require it before you're allowed to mark yourself stable. So if you look under entities, you can see here, when you ref an attribute, you can say the role is identifying or the role is descriptive.
That is… that is what it looks like now. In… in… we're making a new syntax for this file, where actually you'll define an entity at the top level. So you'll say entities colon, and under there, there will be an identity and a description, and that will have the attribute reps in it.
So, we're fixing this over time, but V2 is not out for the YAML.
And for now, they're compatible. So that's where you want to do it.
**Dmitrii Anoshin** 29:07 Okay, so a role would be a key on top of all of the attributes, replace the attributes here, right?
**Josh Suereth** 29:15 In, in, in the entity, right? Yeah, a role isn't…
Yeah, yeah, a role… so you can put a role on an attribute anywhere, it's just only paid attention to for entities.
In fact, we might actually crash if you put it anywhere but on entities, on purpose.
**Dmitrii Anoshin** 29:30 Mexico.
**Josh Suereth** 29:30 because you're only supposed to use it here. But it's a new, you know, how attributes have an ID, a name, a description, that kind of stuff. Role is one of those things that we have to support entities right now.
**Dmitrii Anoshin** 29:41 I see. I know, like, metadata YAML schema is different than Viewer, but I'm trying to make it at least, like, somehow close.
So we… at some point, if you want to merge them, it'll be easier. So, in my idea…
**Josh Suereth** 29:57 We should look at our V2.
**Dmitrii Anoshin** 29:59 Okay.
**Josh Suereth** 30:00 You should… you should be following our V2 schema. Yeah, so, let me… I'll get you a link. I have to… I have to bail for another meeting, so I will put a link in our chat. Is that okay?
**Dmitrii Anoshin** 30:09 Okay, yeah, thank you.
**Josh Suereth** 30:10 I gotta go to a service sim company, so I'll put a link in chat to the V2 so you can see what we're doing, but the current syntax is really gross and non-intuitive.
**Braydon Kains (Google)** 30:18 And…
**Josh Suereth** 30:19 and we're making a V2 that is more intuitive. If you're gonna move metadata, V2 is almost here, and usable. You can still use V1, and you'll be able to use V1 and V2 together, but I'd rather you guys adopt V2, because it's going to be way easier for users to figure out what the hell we're doing. The whole groups thing is too confusing. Yeah, okay, alright.
**Dmitrii Anoshin** 30:39 Thank you, Josh.
Yeah, I think we're out of time, but yeah, we probably did a great progress today.
**Braydon Kains (Google)** 30:47 Yep, I'll… I'll get on the… the two things I agreed to.
**Roger Coll** 30:51 Thank you.
**Pablo Baeyens** 30:52 Thank you. Bye.
