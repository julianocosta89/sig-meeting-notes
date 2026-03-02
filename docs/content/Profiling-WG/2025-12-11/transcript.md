SIG: Profiling WG
Date: 2025-12-11
Duration: 117 minutes
Zoom Recording URL: https://zoom.us/rec/share/Ap6t62qKHj3tocR81TUzUisqJm0RSsmeO5QyvEVd2OdGuIyherR06JJoIUZ2QY5r.7qr7H5PaawHy1kgY
============================================================

## Zoom Recording Transcript

Frederic Branczyk 00:02:30 Hello!
Felix Geisendörfer 00:05:34 Alright, we're, 5 minutes in…
So, I'll get us started. Thank you, everybody, for joining today.
I will share my screen and take us through the agenda.
As usual, we'll start out by reviewing previous action items. So I'm gonna copy all of this stuff from here, and then go through it.
Do we have Alexi here with us today?
Alexey A 00:06:11 Yeah, hi, hello.
Felix Geisendörfer 00:06:15 Alright.
Alexey A 00:06:15 I… I updated the pool request addressing the comments that were there. I think… all…
to my knowledge, mandatory checks are there, so I think this initial pull request is…
is good to merge. There are still optional things for orphan entries in the dictionary and duplicates that I need to add, but I plan to add it afterwards. I mean, I plan to add it on top of the initial change.
Felix Geisendörfer 00:06:48 Okay, so call to action for everybody is to… To take, yes, to take a look and, leave comments or, or LGTM.
Okay, sounds good. Everybody who has a little time, please do. I will try to do it myself as well. Thanks for the update and all the work on that.
I'll just put a little… Alert here…
Okay, then, next item is Florian OTLP P-Prof Converter.
Florian Lehner 00:07:28 Yes, these are two PRs, both still need feedback.
The first one, semantic conventions pull request, got some attention.
A few hours ago.
Yeah.
No difference to last time.
Alexey A 00:07:48 Florian, I wonder for the semantic convention one, would it make sense to…
like, pull the sample order change into a separate pull request and discuss it separately, and… because I think everything else is non-controversial. The only discussion is about sample order. On the other hand, it's kind of like overhead to split this thing, so I think it's up to you, just… just as a thought.
Florian Lehner 00:08:10 I can remove the sample order if this helps.
Felix Geisendörfer 00:08:15 I think it would make it easy to approve. I think everything else, yeah, is uncontroversial, but, yeah, if we don't already, we could take an agenda item to discuss the sample order. Maybe we can also resolve it if we have time at the end of this call. What do you think?
Florian Lehner 00:08:30 Sounds good.
Felix Geisendörfer 00:08:32 Okay, then I will, discuss sample… Order for pre-proof attributes.
with that.
Here, and then, yeah, we should probably get to it, given what we got on the agenda today. And the other one basically still needs refuse in general, right?
Florian Lehner 00:08:54 Yes.
Felix Geisendörfer 00:08:54 Okay.
Okay, thanks.
Then the next one, context propagation OTAB, Evo is gonna join later today, and I've added an action item for him here, so, I'll just make note.
Do we have Alban today?
Florian Lehner 00:09:30 do we still need this action item or agenda item? Because, I think Ivan received feedback from the, security guys of the Linux kernel.
It will not be treated as a CVE, as far as I remember. And he pushed,
PR that introduces a new flag to the Linux kernel. I don't know the exact status of this at the moment, but, I think for us, there's nothing that we can do for the moment.
Felix Geisendörfer 00:10:04 I think I agree with that, so I think we can drop it, and if Alban wants to bring it up again, of course, he's free anytime he wants to join.
Okay, I will… Perhaps this for next time.
Or maybe, yeah, can somebody maybe move it to the, archived action items? That's what we typically do, if somebody could do that, it'd be great.
Oops.
Then we have two more from, Alexi, PR clarifying start timestamp Duration Conventions.
Merged.
Alexey A 00:11:01 Yeah, that is done and merged.
Felix Geisendörfer 00:11:04 Okay, so I guess we shouldn't even have a hat here, so if somebody could just take it into the…
Alexey A 00:11:10 Yeah, I'm… I'm calling it.
Felix Geisendörfer 00:11:11 Well, I'll leave it here, but yeah, if somebody could take it out of section items, that'd be great.
So, and I guess this next one is sort of…
the same as 3078, so I think we'll circle back to this.
Alexey A 00:11:29 Yup.
Felix Geisendörfer 00:11:40 That gets us to 733. We gave some updates on the benchmarks here, and there have been some further discussions.
I am currently unsure if we're now unplugged on this, and we can go ahead with the approach we had. There was also an idea floating around of doing hierarchical,
resource trees, which I have not fully wrapped my head around yet, but it sounds like that's probably not going to be something we want to do right now. I don't know, Florian, do you have a more clear sense of where we are here?
Florian Lehner 00:12:13 Not, but, I see that Josh joined, and maybe Josh can, because the hierarchical approach
Originates from Josh.
Josh Suereth 00:12:26 Yeah,
This… so, we… I was… I was hoping we'd, I don't know if you have other things you want to get to, because this might be a long discussion.
Do you want to do that now, or do you want to go through some of the other agendas?
Item.
Felix Geisendörfer 00:12:39 I…
I would say that this is, like, in the critical, critical pass of what we need to get out, so I would be okay with blocking on this right away.
Josh Suereth 00:12:49 Alright, so, I think the TLDR is… there was a lot of, confusion around why you needed this that we have gotten resolved.
I think now folks understand the problem. There were a couple proposed solutions here, but we basically don't have a great solution for you.
We have things we want to do in the future.
And we have things that work today.
let me walk through some of the, the, like, where we're thinking about this. So…
I sent a proposed change to the proto, where we would have hierarchical resources. So, for example, you could actually record in a dictionary and say, I'm on a host, and then the resource that's attached to the profiler would be the process.
And could refer to the host.
there's general agreement that that would be cool if we did that, because that aligns with what we want to do with entities in OpenTelemetry Protocol, but that it's way too early for us to figure that out, we don't want to rush it, and we think it might be semi-breaking across… like, that would be something to do across OTLP.
So there's that. And again, the idea there is not to actually just be a dictionary, the idea is actually the model of OpenTelemetry would be shifting.
Because we actually do have an issue where there are layers of resource, and people are shoving all of them into the same thing, and we can't figure out what the real identity of a resource is, right?
Okay. That's the proposal that I had put. I don't remember if that was on the public chat or the private chat, because I get them confused, so apologies. We had, like, a private discussion on, like, design ideas.
If that wasn't public, I can throw that… it's in my, my own branch of OpenTelemetry Proto, you can see what that looks like. It's not…
It is not…
well thought out. It is a design idea from the direction we're going with entities. It needs a lot of, like, deep thought. So, I think that would actually be a long path to success.
Tigrin removed his block from the dictionary because, we now understand more the need of what you're dealing with, what it looks like, and we don't think we have an alternative solution that is faster, easier for you.
the reality here is the biggest friction point, I sat down with, like, David Ashpole, and we walked… he walked me through why this is so hard in the collector.
I… We haven't found a solution that will not involve a lot of work on the collector.
for supporting this use case, with the way PDAT is designed, and the way this will be efficient.
And I think that's our number one blocker at this point.
In terms of picking a direction forward. So…
We were trying to have our cake and eat it, too, of if you're gonna make changes for profiling, and it's gonna be a huge problem in the collector to make this work.
Let's make that change really worthwhile and see if we can make dramatic improvements that affect everybody.
Right.
There's resistance on the collector around that as well. So…
I'm not sure what path will be successful here, just honestly. My thinking right now is that I am fine, and I can continue to drive this in the TC, we've had discussions, if we add the dictionary for profiling.
And only profiling, and figure out what's going on there. Antoine told me, is there a result? Yes.
I think Bogdan will be the one we need to, discuss this with. It might be good to schedule, like, a one-off meeting.
With, like, if you get Bogdan, Tigrin, and I to agree on something in the protocol, generally, you know, we can get that through. Bogdan still has a bunch of concerns, and I think there's been a lot of good discussion with him in one of these chats.
But I would say, like, if you want to know the people that we need to address, those would be the three. Tigran removed his blog…
Go ahead.
Antoine Toulme 00:17:12 Yeah, we're trying to… I'm trying to make it so that we can actually, rather than discuss the merits of the model, I'd love to use it so we can get some feedback from
Actual users.
Even if it's awkward, if it's not perfect.
So we initiated a proposal for a PPOF receiver, which I think is a really cool idea, to have the collector report its own profiles, right?
I've been working
with Australian and others here for about a year now, to try to get to the point where we'd be able to express that.
We are… we have landed something in the collector.
But we don't seem to be able to agree on how we want to leverage the translation code.
Because I have the PProf Receiver ready there, and for installing, I don't want to open the API at this point.
So, I'm stuck, because I think if you want to move things forward, it's not so much that Botan cares, it's that also getting some real feedback from people, whether it's useful or not, is going to make a whole world of difference. I think… do we agree on that?
Josh Suereth 00:18:17 So, so, let me, let me pull something out of what you just said. You are unwilling to use what you have today because the format might change.
No. True?
Antoine Toulme 00:18:27 I don't care. I actually want this to break. I would like it so that we can…
Rather than having a discussion about the format. I would like it if we actually used profiles for something and see if people like what they can do with it, because then it would fuel investment. Pretty much, the way I would say it is.
At this point, people are looking at profiles like, that's a nice science experiment. Can we get some value from this science experiment, so that we can have a discussion about investment?
opportunities and RI. I want this to be real. I want this to be something that people use in their day-to-day, when they collect profile for the collector, so we can have a meaningful conversation about how to make it better. Not just based on how we should build it, what the transport should look like, what the API should look like. I know it's painful, I hate it too.
Happy that you take on the pain.
I think it's real, right?
Josh Suereth 00:19:18 Let's… let's talk about the options, Ben.
Antoine Toulme 00:19:20 Does that make sense?
Josh Suereth 00:19:20 Let me just walk you through some options, okay? Okay.
Felix Geisendörfer 00:19:23 And just, FYI, Florian had his hand up as well, so maybe he can go after you, Josh. If you want to go ahead, do it, but then let's…
Josh Suereth 00:19:32 Laura, you might have something salient to say. Go ahead and talk first, and then I'll walk you through the options as I see them. Go ahead.
Florian Lehner 00:19:37 I think it's a direct answer to Antoine, and I hope it will.
I have opened…
this is already closed Xcraper for profiles and XScraper Helper for profiles, so… and, collector… and collector and collector contract to unblock, things like the PProf, receiver and translator. So, once…
we get feedback on these, you should be able to get these report, exporters and all these elements landed. I think it's a little bit unrelated to the discussion with the resource handling, because this part of the protocol will likely not change, I would say.
Felix Geisendörfer 00:20:24 Okay.
Christos Kalkanis 00:20:26 Also, Antoine, one small thing maybe to add here. We've had profiling in Auto working for quite some time now. People are using it, right? So that's people in the OpenTelemetry community, maybe people who only care about profiling, and they use profiling in Auto, because that's kind of the only way to get the
continuous profiler. So, we are running it elastic with the Edit Collector, with the OpenGLMIT collector as well.
It's being deployed, it's not, you know, something that people are not using at all.
the only issue is that the constant breakage, right? The protocol keeps changing, we keep breaking things.
But, yeah, and that's what, like, our top priority right now is to stop that at some point, to get something out that stayed more stable than what we've accomplished so far.
Josh Suereth 00:21:15 Yeah, I… that's also my goal here, is to give you guys
The quickest path to stability we can that sets us up for future success.
Right? And so, I think we have, kind of, a few options on the table.
Option number one.
Is you keep the profile signal as is today, with inefficient resources.
And that is an explosive growth. What we do to mitigate that, right, is… is we…
One of the things I'm curious about with the benchmark, and we can talk through this, it is benchmarking based… a couple hosts batching data together.
If we talk about, like, a single host, or, like, batching, processes separately.
we can work around some of the issues with the known inefficiency in the protocol, right? So, like, keep things as is today, move those resource attributes where we want them for processing, and just kind of…
Work with that for now.
as we, on the side, work through faster protocols for profiling, right? So that's option one. That's the do-nothing option. There's always a do-nothing option, right? Option two.
We push for this dictionary representation.
The dictionary representation, the amount of compression you're getting on resources is significant, and I think actually applies to any collection thing that works on a heavy node in Cates, and has to, like, grab data together.
There's gonna be debate about whether this dictionary should be something that, you know, all of OTEL can engage with, they're just profiling. My proposal to get this out the door is, I don't…
We evaluated a lot of alternatives for how we could make that dictionary not be a breaking change for other signals, and we were unable to come up with a solution.
So, that doesn't mean there's not one, it just means I think that what that… the second option looks like is profiling only dictionaries on all things, including resource.
And then a lot of work in the collector to support that. And that's what the profiling signal looks like when it comes out the door, and we might have other changes to protocols and things in OpenTelemetry going forward.
to, like, learn the lessons that we learned in the SIG, and apply them to the overall protocol.
Option number 3…
is, this, this, hierarchical resourcing, or the entity SIG. So entities is trying to make changes to resources.
One of the problems entities has right now is we're not encoding The parenting relationship.
In resource.
We could look at proposing that we encode the parenting relationship. So, for example, when you report a profile, the only piece of information you need in the resource section is the process PID,
Right? The process start time, or whatever descriptive attributes you need for a process, and then a reference to its parent, which would be the host.
And that other information will be stored in some dictionary at the top level of the signal. That is something that entities may want in OpenTelemetry going forward. I don't see that
like, we don't know how to do that without that being a breaking change. So that's also why, like, 3 is a possibility.
But you will need something in the interim before we get there, right? Like, that's using what we have today.
Or number two.
So that would be number 3. Number 4…
And this is where things get a little bit crazier, is we basically think about, we…
try to figure out a way, what was I… how was I gonna phrase this? Number 4 is we take…
what you're doing, and kind of make a V2 of OTLP.
Where profiling is in the V2 directory, not the V1 directory, and we can start making fundamental changes to OTLP in V2.
Right? And so, you would be the first signal that is V2, and there would be, like, eventually everyone else would come up to speed with V2, and there'd be a V1 and V2. That is not a trigger we want to pull right now, because we're focused on stability. That's, like, the craziest of these options.
It's possible that that's actually… well, anyway. Okay. I talked way too much. I want to hear feedback. Alexis first, I guess?
Alexey A 00:25:47 I was curious if these difficulties of, option 2, supporting option 2 in Collector, which is profiling specific dictionary support, are they, like, written down somewhere? I was just curious, like, for the audience, might be interesting to kind of, like, see the summary.
Josh Suereth 00:26:03 I would love if they were written down. I'm not aware of them being written down,
like, I had to have someone walk me through it, but it… the contextual reason is, inside of Go, allocations are very expensive, and so the interface that we have for dealing with these things is not an interface, it's actually a raw structure.
And so if we wanted to, like, hide the fact there's a dictionary, and have, like, an interface that says, you might have a dictionary, you might not, that's actually really inefficient in Go.
And so, for performance reasons, they have designed their system to kind of be very raw in terms of how P data represents OTLP.
Felix Geisendörfer 00:26:42 You know what?
Josh Suereth 00:26:43 And so you have direct access to structures, which means every user of PDATA will have to have if this, then this, and that bleeds across the collector codebase.
Alexey A 00:26:55 I don't know how helpful this will be, but this just feels something that would be good to write down, so that there's, like, an extra pair of eyes on this. Maybe other people will come up with some…
With some ideas of how to overcome the concerns.
Josh Suereth 00:27:09 Yeah, actually, that's a, that's a great, a great point. I, I should,
Antoine, are you going to the Collector SIG after this?
I'm trying to find someone who's in the collector to write this down. I think that would be ideal. Because if I do it, it's gonna be from the 10,000 foot level, not as useful.
Antoine Toulme 00:27:29 There's no sync today.
Josh Suereth 00:27:33 Well, I mean, just next week, before we cancel… before OpenTelemetry kind of shuts down. If we could get someone from the collector to write that down, I can also just ping Bogdan and see if he's willing to write it down, because I think that would be useful.
Antoine Toulme 00:27:46 Work on that, that's fine.
Florian Lehner 00:27:50 Hmm…
Antoine Toulme 00:27:50 I can work on it.
Thanks.
Florian Lehner 00:27:53 Yeah, I think it would be awesome if Bogtan would write it down.
Because he has the most critic, and then we could work out with him what's the reasoning.
I don't see a big advantage of a V2 for profiling versus the option 2.
With the, with the reasoning.
That the changes need to be done in the collector, for both, so it would not make a difference.
At the moment, profiles in the collector is always in a sub XXX package, so X receiver, X gripper, X processor, so there's already a clear separation. And, for option 2 versus option 4, it would not make a difference for the implementation part.
With… the option 3.
I think there are… I get the idea, it… it sounds tempting, but I think it's not…
Not in a state that can be used,
Properly, with the reasoning that,
At the… as far as I know,
parents are referenced as two resource messages, and a resource can have multiple attributes, and it's not clear defined how they can be mixed, how they should be filtered, and I think there's a huge step that needs to be done first.
Before this can be applied somewhere.
So, my personal favorite would be
go with option 2. I see the work that needs to be done in the collector, definitely, but I don't see why we cannot make this happen.
Josh Suereth 00:29:46 Do you want me to respond, or should we go through all the hands first?
Felix Geisendörfer 00:29:51 I think if you have a quick response, it's fine, otherwise.
Josh Suereth 00:29:55 Yeah.
The ones… I… I totally get what you're saying. That's why I think, like, right now, Tigran and I are of the opinion, like, 3 would be ideal if we were further along, but it's not viable today. If you look inside of, like, semantic conventions, we're starting to get those bundles together.
where you can understand hierarchical relationships, it's just it hasn't landed. So it's not, like, ready to use. And that's why I think 3 is probably a no-go.
It, like…
pie in the sky, that's the option I would want, but I don't think it's ready now for you, and so I don't think we're going to be recommending that. Alexi.
Or wait, was Christos next or Alexi?
Alexey A 00:30:35 I think Christos was first.
Josh Suereth 00:30:37 Okay, Christmas.
Christos Kalkanis 00:30:38 Yeah, so just to clarify the option one, keep signal as it is today, inefficient with lots of resources. So that already includes a dictionary, right? So the signal as it is today already has the profiles dictionary, which contains locations, mappings, files, and so on. What we don't have is reference attributes.
So what, like, does option 1 mean the signal as it really is today, with the dictionary, but without reference attributes? Or we go back to an earlier state of the protocol?
without a dictionary at all. Like, what do we actually mean here?
Josh Suereth 00:31:11 Yeah, one is as is today. So the idea behind one is, code is a collector that leverages PData and does resource detection, resource augmentation, can work on the profile signal.
So if I have… if I send a profile to the collector, and the collector has a… by the way, I should have mentioned the use case that we're thinking of first. The only use case we really want to be optimized for profiling right now is enrichment of resource. So if I send a profile to the collector, and the collector has more information than the original, like, generation of that profile, I want,
Oh, sorry if my mic's crying.
Felix Geisendörfer 00:31:48 Yeah, yeah, it's very good.
Morgan McLean 00:31:49 It's really crackling.
Yeah. Let me switch. I think my USB is on the Fritz again.
Florian Lehner 00:31:56 Maybe I can jump in in the meantime to answer Krista's point. The discussion we have around, pull request 733 is, the resource messages, and these are the essential part where we don't have the dictionaries approach.
To be compliant with OTEL, we need to have all the resource attributes we currently attach to the sample on, on the resource level, so push them way up. This would increase
as the benchmarks from Naev and Felix showed the data quite significantly. That's why I think option one should be not preferred.
Christos Kalkanis 00:32:39 Okay, but in terms of the load for the collector people, right? The point that Antoine and Josh previously brought up, like, if option 1 already includes the dictionary, like, it seems to me that any code in the collector that has to work with profiles has to take that dictionary into account. So the difference.
Florian Lehner 00:32:58 Not yet, not, not yet for the resource profiles. Yes.
Christos Kalkanis 00:33:03 The only difference is whether that includes resource profiles, reference attributes, or not.
Right?
Felix Geisendörfer 00:33:10 No, I think, Chris, I think the main challenge here is we're thinking about touching the resource message itself, which exists in the common part of OTLP, which impacts all the signals, so resources referenced from traces, metrics, and logs. So if we add, like, a dictionary reference in there.
then it gets awkward with profiling. This is the whole issue. And also, anything in the collector that just operates on resources, and there's a lot of, like, enrichment processors that do that, will need to be aware of that change, and I think this is where the complexity comes from.
Right, even if profiling is the only user of that reference? Even if profiling is the only user. It basically impacts every processor that has ever been written, and a lot of things in the collector.
Josh Suereth 00:33:51 The other thing that's true today is the resource… by the way, is my mic better?
Felix Geisendörfer 00:33:55 Yes, a lot better.
Josh Suereth 00:33:56 Okay, sorry about that. The other thing that's true today, you can, with PDATA, fire resource through our resource detector.
And through, like, transformations in OTTL, with never touching the profile signal. So, like, the existing code that deals with resource, if resource looks the same way as it does for other signals.
we can get the resource detector to work, we can do augmentation, we can do enrichment, like the Cates attribute processor thing that adds, like, deployment and stuff. That would all work with profiling.
That's… and the focus here is that, because we think that's actually something people want to do with profiling, it's a real-life use case, your example data has that data in it, so that's the thing we're really focused on here, is how do we make that successful?
Okay, Alex.
Alexey A 00:34:48 Yeah, slightly related to, to Krista's,
for what it's what, like, I wasn't, like, super closely following the resource discussions, but one thing… like, one point of confusion I have, like, initially there was this issue from Wogden on premature optimization, and the concern there was about having dictionaries at the top level, and the question was, like, why dictionaries are not, like, per profile, or per scope, or per resource, something like that.
And that issue is not closed, it's still there, but now we're discussing that apparently Bogdan is okay with dictionaries at the top level, and the only concern is resources. I… I just kind of, like, want… it would be nice to… like, maybe it's already, like, confirmed offline, but from my perspective, like, it's not clear
like, whether the collector folks' concerns are actually just resource, or are we still also, like… but apparently, like, not. Apparently, like, everyone is fine with, like, dictionaries at the top level overall.
Josh Suereth 00:35:42 So, so, yeah, I think partly that was Bogdan is not… wasn't up-to-date on profiling, and partly he hadn't looked at the actual benchmarks yet.
So, I don't know if he actually feels like this is still premature optimization. I think that's something we're still…
discussing, and so, I'll see if he can come to the SIG going forward.
to have those discussions with everyone, but I know from Tigrin and my perspective, as your liaisons from the TC, we looked at the benchmark and we think, like, yes, this is a very legitimate problem that needs some sort of solution, like a dictionary or a reference of some sort, to avoid the duplication you're seeing.
And, the, when we looked in the benchmarks, you know.
we had, we had a big discussion in the TC meeting, basically, about looking through those.
Tigran and I did an offline one, too. You know, you're…
your use case is legit, right? This is based on real data, these are based on hosts, so the assumptions we have in OpenTelemetry around resource.
for tracing, for metrics for things, like where Bogdan's concern comes from, is why is this not a problem for other signals? And if you want the answer to that, what we looked through, the reason it's not a problem is other signals were batching a single resource in a process, generally, and they're actually kind of stored on process.
And then we send to a collector, and when we batch against that collector, we're batching against a time window where it's unlikely we have to join so many resources together, the way profiling is.
I think your problem will become an issue for any EVPF-based instrumentation. So, like, the new OB instrumentation, I think we have the same problem.
And that's why I think I want to take a short and long-term approach here of, let's solve profiling, get things working, and then we're gonna have to do something for the rest of OTLP, because we're gonna run into this issue other places.
That's… that's my… my current view. And again, it's… yeah, go ahead.
Alexey A 00:37:45 Yeah, thank you, and just as another, like, the fourth option, OpenTelemetry 2, this sounds very heavyweight, because, like, well, Python 3 started in 2008, and we still have Python 2 and Python 3. This… these things, like, take a long time, and it almost feels like kicking the can down the road for, like.
Like, really far down the road.
Josh Suereth 00:38:08 Yeah, if we were to make a version 2 of the protocol, I think that version 1 and version 2 would have to be supported in tandem
Forever.
it's not a thing we want to do at all. And so that's why we're focused on trying to find backwards compatible ways to address, like, existing signal problems, and I don't know if we'll be able to.
So, there was a discussion in the specifications, SIG about, like, content negotiation.
that's… that's another thing that, like, maybe there's… there's room there. I… I personally don't think we can add content negotiation without that being a breaking change.
to OpenTelemetry.
So I don't think we have viable ways to…
fix this problem in existing signals. That's… this is where… if you want to know where I stand individually, not as a TC, this is Josh, I don't think we have a viable way to fix this without having a braking change somewhere. So what I'd like to do is have profiling do the best that it can right now. It will look different than other signals, and that is okay, with me.
That is what the message I'm trying to drive through the TC as well. Tigrin and I are kind of,
mostly aligned on, like, getting things through this way, and we're working through the rest of this. But that's where things stand on our side.
Felix Geisendörfer 00:39:32 Okay… Thank you, everybody.
what is the next steps we can do in the profiling stake? Is this, like, still in the TC's court? Is this in our court? Both courts? What should we do?
Josh Suereth 00:39:48 I think probably what we need to do is schedule a meeting with Bogdan to discuss the collector concerns specifically. I think from this discussion.
I want to check, is number one an option to make progress, or do we all feel like we need to go for number two here?
Felix Geisendörfer 00:40:12 I think we've felt mostly in the sick in the past that
if we go with number 1 right now, and we go alpha, we're basically trying to tell people we're not going to make major changes anymore, and this is gonna be a pretty major change. Like, we have not achieved anywhere… any step closer to stability if we just call what we have right now alpha, if we're still planning to change it.
So we would probably not see that as a solution for our desire to finally get something out of the door here.
Yeah.
Josh Suereth 00:40:44 Alright, so then, I think…
the next step would be, let's sit down and see if we can schedule some kind of meeting with Tigran Bogdan. You can include me as optional. I'm there to support you, but I think, really, we want to get the concerns aired out.
on the dictionary approach, and let's try to push on that as the path forward.
It may make sense to take these notes and, like, reformulate them into all the things we discussed, pros and cons, of, like, here's the possibilities and documents and why we're going with this as a decision.
That… that could help that meeting, that it… I… I think the, from…
my interaction so far, I think just the in-person meeting will be necessary to kind of work through the details here, and get the attention you need, so…
Felix Geisendörfer 00:41:35 Okay, so Bogdan, you as optional, anybody else? I mean, of course, anybody.
Josh Suereth 00:41:39 I would, I would include Tigran, yeah.
Felix Geisendörfer 00:41:41 Integrin, okay
Okay, Florian, you had your hand up, is it still, or… went away?
Florian Lehner 00:42:00 No, just wanted to join this discussion.
Felix Geisendörfer 00:42:03 I see, I see, yeah, yeah. Yes, you would absolutely be on the invite list. I will probably…
I'll figure out a way that everybody can get a chance to join. I'll schedule it and post a message, or find a calendar where I can add it, where it becomes visible, something.
Alexey A 00:42:19 Felix, can you also include me?
Felix Geisendörfer 00:42:22 Okay.
Alexey A 00:42:24 Kinda 1, 2… To help us again.
Felix Geisendörfer 00:42:31 Yeah, I will post, so anybody who also wants an invite, checks the Slack channel, the profiling Slack channel, I will post a message there with a date.
Now, I'll do my best to find something that's, like, a time slot that works for US and Europe.
Okay, then I think we have…
the next step. Anybody has any last thoughts, or should we… Move on through the agenda.
Going once… I think twice, then…
Lexi, do you want to talk about simple values and timestamps Unix Nano?
Alexey A 00:43:18 This is not urgent, so we… if there are more important things, we can push this down, if, like, if we want to discuss…
just based on gut feeling that, something is pressing, or… like, for example, even I think, the sample order, the default sample order, I think it, it would come… it should come first.
Felix Geisendörfer 00:43:41 Okay, well, I guess you can trade your slot, so…
Alexey A 00:43:45 Okay.
Felix Geisendörfer 00:43:46 We'll do… we'll do sample order for a second. If anybody has a light item on the list that they really, really want to get out today, also please raise your hand and we'll try to make the order work out.
Simple order for PPROF attributes. So…
Alexey A 00:44:03 Yes.
Felix Geisendörfer 00:44:04 That's what I…
Here's a problem, do you want to introduce it? Because I think, like, maybe you, me, and Florian have context, but maybe the others don't.
Alexey A 00:44:11 Yeah, I can… I can introduce it. So the… there's also a document that also has some background, if anyone wants to read it in parallel, but the thing is that, PProf has…
In Piper of a particular profile has multiple sample types, which are metrics, and that is kind of like the same in hotel.
protocol, except, like, we structure the hierarchy a bit different, but conceptually it's the same. And then PProf has this convention that there is default sample type, attribute or field.
that instructs consumers which of sample types should be open in the UI or in CLI by default. And there's also a convention that if default sample type is not specified.
then, then the last sample type should be used. It's… it's like, it's historical, it's like, I… I don't even have all the context why this, like, last sample type is the default was… was chosen, it's not…
like, it's hard to defend, to be honest, at this point, rather than this is historical decision that we need to, we need to respect. And then, when we convert PROF profiles into OTEL,
we need to figure out how to handle this, and so that the round-trip conversion is also possible. And in OTEL, we don't even, I think, document explicitly, maybe we should, but the assumption, like, we don't have this last sample type is the… or last profile is the default. We'd rather say, like, the first one would be the default, because this is more natural.
And so…
we need to kind of define the semantics of this conversion. And what we said previously, we would have people of specific… and I think what we said previously, we would have these people of specific attributes in the hotel schema.
One for default sample type, and another is for sample type order. And so, when we convert PROF profile to Autel, we reorder the
Sample types into profiles in a way that the default
In PPROF speak, the default sample type becomes the first in the hotel, profile array.
And then when… if backward conversion happens, then we can restore the original type as it was on PProv, so that the, the order is the same. And…
And then the document basically proposes an approach, but then Florian reasonably asked, like, oh, do we even need to reorder anything? Can we just specify the default sample type?
But then I think, like, another thing is that these attributes are PPROF-specific, and so… so I think we need to reorder them to make the default one the first one, because otherwise we don't want to instruct consumers, oh, you need to consume this PROF-specific attribute. This would be kind of, like, weird, right? They don't know…
they don't know anything about people… like, ideally, no one except People should know about people of namespace, of attributes, right? Like, we don't want to say.
or this needs to become a, an, like, default sample type… default profile should become, basically, hotel, profile's signal attribute, not people specific. I hope I'm clear enough, the document kind of has more details, it's… I'm trying to be,
Compact in words, but there are also some nuances, so feel free to ask questions or, share opinion.
Christos Kalkanis 00:47:37 So, Alexi, in essence, you're essentially saying that OTL profiling needs to adopt the default sample type semantic convention, and adopt it as a native convention in auto profiling as well, right? Not just something that's purely for compatibility with Piprov.
Alexey A 00:47:56 We can keep it PPROF-specific, but then I think we need more attributes, so that we can reorder sample types in a way that the default one from the PPROF perspective becomes the first one.
And then we can restore the order. And to me, it seems that it means we need two attributes, one to capture the order, and another is default sample type.
Felix Geisendörfer 00:48:17 Let… yeah, and maybe… maybe this is clear to everybody, but just to be very clear here, the goal is to round-trip P-Prof, right? So we want to be able for PProf to go into a collector, be converted to OTLP, and then somebody should be able to take this OTLP and convert it back into a PPROF that we consider semantically equivalent.
To the one that started the process. And we believe we cannot restore that.
Losslessly if we don't add the order.
Of the original profile types, flooring go ahead.
Florian Lehner 00:48:47 Hmm…
That's just a personal opinion. I think the order of the profiles in Otel should not matter at all.
And, I think from the hotel perspective, we don't have a default profile at the very moment.
So, having just, PPROF, Attribute that says, hey, this profile is the default profile.
would… just, justified, round-trip conversion, so with this, it's already, possible.
It can happen that the water of…
Profiles in the conversion can be different.
But with the default profile attribute, We need to… or…
the tooling that is used to generate, hotel profiles, PPROF from hotel profiles, needs to make sure that, the last one, is the default profile. I think we should not add additional
Complexity by requiring people to, reorder profiles in some way.
Felix Geisendörfer 00:50:02 Can I make sure I understood the full comment? You said…
either… did you say that OTL doesn't have an idea of default profile type? Because we do.
Florian Lehner 00:50:11 Yes.
Felix Geisendörfer 00:50:12 No, we…
Florian Lehner 00:50:13 We do.
Felix Geisendörfer 00:50:14 Yeah.
Tools that visualize profiles should prefer displaying the first resource.
Florian Lehner 00:50:19 Okay, then my fault, sorry.
Felix Geisendörfer 00:50:21 profiles by default. So we have put something there.
Florian Lehner 00:50:25 Okay, then… We probably don't have a chance, other than reordering.
I missed a comment.
Felix Geisendörfer 00:50:32 Yeah, and I think this is, yeah, why we were, like, commenting the way we were,
Then maybe the action is to, like, put that in the conversation very explicitly, so it's written down, and…
Yeah, if you…
If you see another way to, like, get us to roundtrip, at least now we'll be on the same page, and… yeah.
But maybe we'll end up with just the ordering thing. I agree with you in general that let's not make it more complex than it has to be, but in this case, we might not have a choice unless we change this as well.
Florian Lehner 00:51:06 we have…
Felix Geisendörfer 00:51:07 Solve one problem by creating another one, by opening another can of worms, so…
Alexey A 00:51:12 Felix, and just to confirm, we do need two attributes, right? The order and default sample type.
Felix Geisendörfer 00:51:16 That was my understanding last time I felt really hot about this, and so…
Yeah, but this is key, that we've set this, so I will… I'll make a link to that in the notes now as well.
Huh.
Christos Kalkanis 00:51:29 why do we need default sample type if we have this convention, right? If we specify that the first profile is the default, why do we also need the attributes?
Alexey A 00:51:38 But what do you do on the backward conversion?
Christos Kalkanis 00:51:42 Promotal to people.
Felix Geisendörfer 00:51:46 Yeah, I guess what you could do is you could mix the first one in OTEL the last in PProf.
But here's where it gets now problematic. If…
Well, let me think, because there's, like, two cases. There's, like, what people…
Alexey A 00:52:07 It was not necessarily the last one, right? Because if you just make it the last, like, maybe it was in the middle.
Felix Geisendörfer 00:52:14 Yeah, yeah, because you can have two cases in PPROF, right? So in PProfs, the input cases are you got a bunch of profiles, or sample types in PProf, and if there's no default sample type, then you basically end up picking the last one for display, that's the default one.
And if there is one picked in, via the default sample type, then you would… basically, that one would become the first in OTEL, or otherwise the last one would become the first.
So, I guess we could restore, sort of, just putting the right profile as the last one in PProf. I think we have enough information about that, but then for the other profiles, we wouldn't know the order. Is that correct, or am I missing something?
Alexey A 00:52:55 Yeah, like, the round trip would not be equivalent if you don't capture that. Let's say, like, you have ABC in PPROF.
Felix Geisendörfer 00:53:02 Yes. And B is… B is the default type.
Yes.
Alexey A 00:53:06 is the default sample type. Or, maybe you have A, B, C, and C is the default type.
Felix Geisendörfer 00:53:12 Right. So, basically what we would do in that case, like, if B is the default type, and we would round trip this without an ordering, then B
we would produce a PPROF on the last conversion that doesn't have a default sample type, and just B happens to be the last one.
Which is not how the original one looked. The question is, do we consider that semantically equivalent, right?
Alexey A 00:53:34 That is, I guess… I… Like, from the broad perspective, it's not cool. Like, it feels like a stretch.
Florian Lehner 00:53:44 It's a lossless conversation.
Felix Geisendörfer 00:53:48 No, so, like, the user-facing, you can already notice it in the drop-down in Pprofs, that's probably ordered in the order of sample types, so it would just change the UI ordering of sample types.
That's my guess. That's what it does.
Alexey A 00:54:05 Yeah, I…
Felix Geisendörfer 00:54:07 So the question really is, is the sample type thing in PPROF an ordered list? Like, ignoring the case, like, of what the default type is, is it generally an ordered list? If it's an ordered list, we need to reproduce it in exactly the same order. If it's an unordered list, where we just have a default item, then we could do without the explicit reordering.
Alexey A 00:54:24 Right now, right now, it's ordered list, in the sense that, like, it's visible in the… in the tools when you open a profile, and it's… it's… it's, like, it's presented in the same order as
Good.
Felix Geisendörfer 00:54:36 But it's not an absolute order. The only element that has significance is last element, right? That's as far as the proto-definition goes.
Alexey A 00:54:44 Like, a specific producer could choose in what order they put
they put the sample types in, like, maybe they are grouped, for example, like, a log object, a log count, in use objects, in use count, and that order just, like, looks nice in the UI. If you reorder it, it just starts to be, like, it starts to look…
Messier, but this is subjective territory.
Felix Geisendörfer 00:55:11 Yeah, that's what I was trying to get at. I think the conservative choice here is to say this is an absolutely ordered list, and we need to reproduce it in exactly the order we found it in in the original P-Prov. In that case, we do need to note down which order that was, or if we're willing to…
consider that to be a mostly unordered list, except for the significance of the lost items, which is only significant if there's no default sample type, then we could get away with one less attribute. And really, I don't know, to me.
is this really adding a lot of complexity to Dadsys attribute? I would rather probably err on the side of, like, let's try to be as lossless as possible without guessing.
Alexey A 00:55:46 My…
Felix Geisendörfer 00:55:46 With all the people.
Alexey A 00:55:47 preference with.
Felix Geisendörfer 00:55:47 Outside, too.
Alexey A 00:55:49 my preference would also be add that attribute, because I think even for, like… also for the round-trip conversion, even for…
checking the equivalents, adding more complexity of, like, oh, the order can change and can be the same. It's like, is it really…
It's not clear that it's worth it.
Felix Geisendörfer 00:56:07 Florian, go ahead.
Florian Lehner 00:56:11 Yeah, I'm still not getting why we should keep the original order of profiles.
For a lossless converse conversion.
with the reasoning, we also have different IDs.
in the conversion.
So the IDs are different between the different mappings and locations, for example. The data is the very same, but the IDs are different.
So,
where do we define, glossless? The information stays the same. Maybe the representation for the user is different.
I see the point that, default sample type is something
important, and we should have somebody, and for auto profiles, it's the first, and for, for PTROF, it's the last one, or it's defined.
So that needs to be respected, no question.
But, I'm not sure about that we need to have the very same order to have a, lossless conversation.
Alexey A 00:57:22 IDs are… I think IDs are different because IDs are not user visible, and the sample order is user visible.
Felix Geisendörfer 00:57:28 Yeah, and I think we even, at least in the tick, we decided that IDs are not significant. I don't know if we ended up writing it down, but I think we had a plan to write it down.
And this is really, like, in terms of, like, lossless
information, right? Like, you have a list, right? Like, do you consider the list to be a set or to be a list, right? That's the key question here. If it's a set, then it doesn't matter. If it's a list, then it does matter. And, I…
think we don't really know what all the PROF tools out there do and expect. Maybe there is some tooling that has given more significance to the order of the sample types than we anticipate right now, and so the conservative thing would be to go through the complexity of having the ordering attribute, is my
my take. Otherwise, we're taking a small risk of, like, breaking some P-Prof use cases that we are currently not aware of.
Alexey A 00:58:24 plus… plus one. For me, I would go with two attributes, just to be as lossless as possible, and…
Yeah, and follow… follow the semantics, because from people's point of view, it's an ordered list.
Felix Geisendörfer 00:58:43 Yeah, and I guess Alexi's as close as we'll get on, authority on what PROF semantics are, so…
I think that should settle it. Like, I agree with you, Florian, that it's, like, seems complex, and maybe something simpler could do, but since we're not sure, I think we should go be conservative and do that.
ordering.
Okay.
Sounds good. Will you… will you make the update, or should we do it, or do you want to split it? Like, what do you prefer?
Florian Lehner 00:59:15 Can I remove the default cyber type from my PR, and do… Create a new one, Alex?
Felix Geisendörfer 00:59:21 Yep.
Florian Lehner 00:59:21 What if it'.
Felix Geisendörfer 00:59:22 Over for you? Or that way.
Okay, we have not much time left. Does anybody see something where they think we can have a meaningful exchange in a minute?
Christos Kalkanis 00:59:45 Yeah, I was hoping we would discuss the process context updates. Evo has done a lot of work there, and I also spent a couple of days,
talking to Ivo and making suggestions, I think we're making good progress, yeah.
Probably don't have time to discuss it today.
Ivo Anjo 01:00:03 Yeah, I think the, the, the, I can add on top of what Chris is saying, is, I'm hoping that,
once we've… there's a couple of things that Chris has pointed out that we're still discussing, and I'm hoping that once we do that, we can have folks from the Sea give it a pass, and maybe give it an approval, so that we can kind of push on the specification side.
And… or if you don't agree, or you've seen something that still concerns you, let's fix it so that we can then push. So I think that's the main… the main next step is, like, if you see something that you're not convinced about, please tell us, or,
Or in that, or otherwise, I'm hoping that, in one week or something like that, or in the new year, you come in, like, all fresh, and you say approved.
Felix Geisendörfer 01:00:51 Okay, I guess that sounds good. Everybody, please take an action item to give some feedback. I already looked at it, and it looks good to me.
So, yeah, would be good to have at least one or two more people to look at it from the SIC.
Okay.
And yeah, also, if anybody wants to have conversations in between these meetings, we have the Slack channel, and everybody's free to also schedule things, so,
Whatever we can do to move things faster, please feel free to give it a shot.
So, yeah, that being said, I think we're at the end of time now, so thank you everybody for, showing up, for all the great work in between the meetings, and, yeah.
So you all, sorry, one important thing, holidays are coming up, so I think in the New Year's is the next meeting, so…
All right A nice local time, and a Happy New Year. Bye.
Florian Lehner 01:01:54 Thank you, it's here.
dalehamel 01:01:55 Thanks, everyone.
Ivo Anjo 01:01:58 Thanks, everyone.
