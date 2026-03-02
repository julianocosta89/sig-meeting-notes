SIG: System Sem Conv Stability WG
Date: 2025-10-30
Duration: 23 minutes
============================================================

## Zoom Recording Transcript

**Christos Markou** 01:15 Ape.
I was just taking the, Slack discussion, Mr. Commenter, yeah, but… Education should be done.
**Dmitrii Anoshin** 01:35 Peppers.
**Fraggle Rock (ca-wat-brt3)** 02:24 I think this is everyone we're gonna have today.
**Dmitrii Anoshin** 02:31 Should we start with your item, Brian?
**Fraggle Rock (ca-wat-brt3)** 02:35 Sure.
**Dmitrii Anoshin** 02:36 Yeah, that's good.
**Fraggle Rock (ca-wat-brt3)** 02:37 So… I was looking at this PR to add the process executable entity, And I have two questions.
for this group.
The first one might be an easier question.
But should the…
executable even be a separate entity? I'm not sure what the value is in the executable being an entity versus these just being…
descriptive attributes on… process.
I'm not sure… I didn't look at the original issue that this PR was…
Talking about, increased ability to describe processes is all it's saying. Okay, this says dedicated executable, so someone was actually asking for that. Who was asking for that? Oh, James was asking for that, and he made his own PR. Okay, so, I'm not sure who else needs…
Needs process executable as an entity.
So, I don't know. I'm sort of in favor of just adding them as descriptive attributes on the main one.
Hmm.
**Josh Suereth** 03:43 I add some context here. So, first of all, these, like, progresses XYZ things, if that's not something your SIG wants to do, we should comment on the PR, or on the issue, and say, like, hey, this isn't something we want.
there's, like, I think, like, 40 or 50 of those were opened at one point in time. So, like, we need to look at all of those across SEMCOM and say, like, is this a direction we actually want to take? Second thing, I already commented on the issue and brought in the profiling sake.
So, an executable in profiling is an identifiable thing.
And they need this because they need to attach a symbol table.
So, you should look at Felix's response. I think it's either Felix or Florian. But they actually need to understand from a process standpoint, like, what…
the build ID or of the executable is to attach symbol tables so they can convert from, you know, pure, symbols that they get from eBPF or from PPROF, and turn that into,
Like a human-readable name for a function.
Their answer is confusing as hell, though. So, they, they both want the executable name of the process to be identifying, and the ID. The ID is uniquely identifying for the symbol table, the executable name is how you would group for,
Doing flame graphs and things like that.
My thinking here, by the way, I don't know how you feel about this with SIGs, but the one reason I'm stepping in is I think this is a cross-decision between the system SIG and the profiling SIG.
And so I think we… we should make sure that that discussion continues, and that we understand the profile and use case, and then make decisions from there. My initial reaction from Florian or Felix's response, because I forget which one,
Is that we should consider executable a thing that's identifying, because we use that to tie,
Symbol tables to it, but the executable name itself might be descriptive.
And so you can still join based on the name, but anyway, I do think executable needs to be an identifying thing for profiling.
regardless of whether this SIG, like, needs it for host metrics and that sort of thing. This goes into another thing I want to talk about, which is about resource identity of processes and the proposal from the profiling group there. But I'll add that to the agenda. Anyway, that's some context, if that helps.
**Fraggle Rock (ca-wat-brt3)** 06:11 I think that kind of answers my… my second question, which is that,
The name of the executable in a process is kind of an unstable thing to identify an entity off of, because you can change the name of an executable
And that won't change, like, the process command line, like, you can still get the name that was originally used to kick off the process, you'll always be able to get that, but we… the way the attribute is said to…
be instrumented is by, like, reading the name of the file that's the target of the proc, like, XE SIM link, and that will change if someone changes… if the executable, like, file name changes on the file system. So it's…
It might not be that important that that's unstable, because we might just decide this entity does exist, but for our general host metrics use case, we won't gather this information, and so maybe it doesn't really matter that
the executable name is an unstable identifier. That is… that was the concern I had, but if that's less of a concern, who should I… should I talk to Florian from the profiling SIG, or…
Should I… should I try and organize, like, Something more general.
**Josh Suereth** 07:21 Yeah, their SIG is actually immediately after this, if you have time.
**Fraggle Rock (ca-wat-brt3)** 07:25 Oh, okay, sure, I'll just, I'll just do that then, yeah.
**Josh Suereth** 07:28 Yeah, we're talking about some more significant things there. For example, profiling is trying to avoid using resource right now, and that's a different discussion. Basically, they have a bunch of performance-related issues with their protocol that we have to work through.
But this… this is one… this is an example where I want to make sure we are sharing information. Regarding process executable, again, another… another point, I don't think you will have to fill this out in resource. I think this is a thing where, when profiling is in the mix.
It would be an entity that's attached to resource in addition to process.
So you would know about the process and the executable of the process, and therefore you can do the symbol table resolution of profiling that you need. But this wouldn't be needed for, like, process metrics, right? Which is why I think having it as a separate entity is valuable, because you can either attach it when you need, or not.
If you wanted to make these descriptive attributes of a process, I could be persuaded that way as well, but I do think that the identity of the executable is somehow important with profiling from what we've learned from the profiling folks.
**Fraggle Rock (ca-wat-brt3)** 08:33 Yeah. So…
Yeah, I guess the… like, the other… the thing I thought of was that, like, the build ID works as an identifier, too, but only for Linux, and so we would need, like, unique version… if that was the chosen identity, we'd need a unique way to identify it on platforms where there's no…
new build ID.
That's something I can ask in the profiling sake. I can… I'll attend after this, and I'll check it out.
Let's see what they have to say. We can move on to my next,
There is a more general question about, like.
entities about, like, files in general, and, like, the way we identify files on a system, because the way you uniquely identify a file does depend on the operating system a little bit. Like, in Linux it's easy, and in Windows it's not.
But I think we can table that discussion, because it's not as important as the other agenda items.
The next one… Is, the counter reset thing.
James opened an issue on the general
general signals page in OpenTelemetry… on the OpenTelemetry website repo.
To…
Well, I think… so I think based on the way he describes the issue, I think there's, like, a fundamental misunderstanding.
Because the way he said it was, like, counters can go down after a reset, but, like, that's, like…
What… that's, like, the point of counters, and, like, what happens, and, like… like…
counters… like, in Prometheus Land, they get reset when the target has reset, usually, or with these cumulative metric counters, like, the system is rebooted, they're gonna go back down to zero, and so the counters reset. I don't know…
If it makes sense for us to write something
Specifically, like, in our non-normative guidance, that explains, like, for a metric that, like, the system is tracking and then the system reboots, like, obviously the counter should reset.
Presumably to, like, when the reset is recognized.
**Josh Suereth** 10:42 Yeah, let me… let me jump in. I… this floored me, by the way. Like, okay.
**Fraggle Rock (ca-wat-brt3)** 10:47 Yeah.
**Josh Suereth** 10:47 For anyone who uses a metric system like Prometheus, this is just intuitive knowledge. You know this. So, I don't want to have to write this down everywhere, but if you look at, like, Prometheus and how it detects resets and things, there's, like, there's a whole page in Prometheus about handling counters in this fashion.
So we could link to that.
Or… Where this really belongs is probably the metric data model.
Right? Of, like, can someone read how metrics work and understand that that's intended? But the counters are designed to have that reset. It's about the lifetime
And again, this is where entities kind of got to be a big deal, as I walk into what I'm trying to say. The lifetime of the entity really matters.
But counters are expected to reset, like, when a process resets. By design, that's how this works.
And there's a practical nature to it, because when you have a counter, you're actually usually interacting with a rate, you're not interacting with the raw value.
And so rate calculations, you need to have a zero, and you need to move from there, and that's where StartTimestamp solves the reset problem.
you just want to actually have it live long enough, or live, like, the same lifetime as the entity. So if it resets because the entity resets, that's by design, that's fine.
we just don't want to choose horrible entities where identity is shifting every, like, 3 seconds. So, yeah, this is one where, I tried to help comments here to make clarity, but in the metric data model.
This is what counters are designed to do. So the argument you shouldn't use a counter is just mind-bogglingly not correct. So please don't, like, go with that right now.
This is literally what you're supposed to use a counter for. And if we have to add clarification, I think that's in the specification, not in SEMCOM.
Or SEMCOM can link to the specification on this.
**Fraggle Rock (ca-wat-brt3)** 12:51 Okay, makes sense. I will look through, like, the… in the page that…
That he opened an issue about…
it doesn't talk about counter resets, but in… deeper in the metric data model, I imagine it must, somewhere, so I… but I haven't looked.
I'll look through that.
**Josh Suereth** 13:10 We think we took it for granted.
That people would understand that counters are designed to reset?
**Fraggle Rock (ca-wat-brt3)** 13:17 It's possible.
I'll look through the data model and see if I can find anything related to it. If I can't…
I'll… I might try and find some time to, like.
Reworth something in the data model spec to explain it, but…
I don't know if I'm gonna have time.
**Josh Suereth** 13:33 Yeah, so…
I mean, I can share, like, the Prometheus rate function, where it automatically handles resets. There's even a Prometheus reset function, where it specifically looks for them and tell you when it happens from any counter. Like, it's designed… like, again, it's designed to tell you, hey, here's where your process resets, so your counter or your rate might not be accurate.
But there's no solution to… like, going up-down counter doesn't make the situation better, it actually makes it worse, because then you can't calculate rates, and you have resets. So it's just, yeah, like, like…
That is, we probably assumed too much knowledge of metrics when we started writing things, and we need to get more foundational things in the spec. So yeah, please take a look, see if it's missing, and see if we need to have links. If you need a few links from Prometheus Ecosystem World, you can link to the rate function.
Which is what we generally recommend every counter use.
Right? That's, that's, like, counter rate are, are, are paired. And that will automatically handle resets. And then there's also a resets function in PromQL that will, calculate all of the resets based on your counter. That's another example of, like, hey, this is handled by default and expected.
**Fraggle Rock (ca-wat-brt3)** 14:47 Makes sense.
I will do that. The last thing I wanted to talk about was, on that same, pressure stall info PR,
I had recommended that because the original counter is represented in microseconds, that the metric might as well also be represented in microseconds. And then Trask pointed out that there actually is something written in SEMCOMF that says all duration metrics should be in seconds.
what wasn't quite clear to me.
But seems to be the case, is whether, like, Whether that duration…
duration means, like, a contiguous span of time, because they were talking about, like, HTTP request duration as the main example in the issue that was linked, but…
Probably that's not the case, like, probably just means, like, any span of time metric should be reported in seconds and as a double.
Does that make sense? Do we… should we go through and make sure that we're following that… that rule?
throughout our conventions. I don't really have… a…
a deep opinion either way, but the reason I had suggested going to microseconds was just because the original metric is reported by the system in microseconds, and
like, there's no other system that's ever going to report pressure stall information. Like, this is Linux-specific, so might as well just report the… what people expect. Like, people are monitoring this themselves, they're looking at microseconds.
But… I'm also fine with reporting it in seconds, too, and just forcing instrumentation to invert.
**Roger Coll** 16:34 Yeah, we had a similar issue with the, I think, container CPU time. I think Docker and Podman can report it in nanoseconds, but
Semantics said that it must be in seconds, and on the implementation side, we just…
converted to seconds. We didn't care about the more fine-grained… Yeah.
But I don't have a strong opinion, actually.
**Christos Markou** 17:03 Same for Kate. If I remember correctly, Dimitri, we convert from nanoseconds to seconds again.
**Dmitrii Anoshin** 17:11 Yeah, I think it's fine for consistency, if everything is in seconds, which should be just, like…
Easier for users to…
understand going forward that OpenTelemetry, it typically goes in seconds, so they don't even bother with…
Checking the original, like, typical implementation of a particular system.
**Fraggle Rock (ca-wat-brt3)** 17:36 Okay, that's fine.
Is there anything… Else to talk about on the agenda?
**Christos Markou** 18:11 Looks like we don't have anything else.
Unless we want to check the board or, discuss any stability-related… Plans, concerns.
optics.
**Fraggle Rock (ca-wat-brt3)** 18:24 I ended up not making any progress on anything on the board, because I was… most of my Zemconf time was spent on, reviewing.
So, I didn't make much progress on stuff on the board. The things that are on my plate are process status.
And…
Fixing the process entity to actually call out the identifying and descriptive attributes, because right now they just say nothing.
So those are the two things that I do want to get to, just haven't been able to yet.
**Dmitrii Anoshin** 18:54 Same thing from my side, I don't have any updates.
For the system.
Sick.
**Christos Markou** 19:00 the process… there was an issue, Dimitri, the one I sent, that was about defining the entity or something about process. It seems it's covered now.
**Dmitrii Anoshin** 19:11 Yeah, and it's fine, I guess. That issue is specifically about defining process entity, and if that…
PR resolved it, it's good.
**Christos Markou** 19:20 Cool. Probably we could start thinking of… I don't know if it's the right time to do it, but…
Then we could, file an issue for… start thinking about
marking this as stable, or it's too soon. I don't know if just…
Have any comments on this?
**Dmitrii Anoshin** 19:42 I want to discuss something, with… regarding entities with George. Maybe we can use this time.
Josh, we don't have a way to say which entity is the closest in the data model. So, for example, we, like, send pod UIDs… pod utilization, for example, and we have
Podentity Cluster entity, right, attached to them.
But in the data model, there is no way to say which one is the closest and what's the relationship between the entity. Is it something that we wanna think about before we…
have some stability declarations, what do you think?
**Josh Suereth** 20:27 I think… I think we need to sort out how big of an issue it is in practice, yeah. So this is where we need, like, the SDK talking to the collector. We did talk about this, if you remember, and, like, what we don't want to do
Is, we thought it was too expensive to include all the relationships in resource.
**Dmitrii Anoshin** 20:44 Yeah.
**Josh Suereth** 20:45 The other… the other problem there is, remember that you can have, independent graphs of relationships. So, service is a logical
Distinction, and process is more of a physical one, and you have both of them at the same time?
**Dmitrii Anoshin** 20:59 There.
**Josh Suereth** 21:00 Or, like, container versus Kate's container.
**Dmitrii Anoshin** 21:03 Okay.
**Josh Suereth** 21:05 So, like, I think this gets down to the thing that we were talking about. Can there be only one?
When we say lowest, and I think it… the answer is actually no, because service instance and Kate's container and container might all be the lowest at the same time simultaneously.
**Dmitrii Anoshin** 21:27 I see what you meant.
Okay. So, we'll… we'll defer that information to the CSI channel, with entity relationships, essentially.
And once we have
So we're gonna define entities without definition of relationships for now, and then once we have a side channel established, we will add it somehow to the… to the simconf.
**Josh Suereth** 21:59 That's… yeah, like, the hierarchy, yes. Yeah. Still need to report hierarchy, I believe.
**Dmitrii Anoshin** 22:08 We still need to report hierarchy, but not as part of the resource, but a separate side channel, I guess.
Right.
**Josh Suereth** 22:14 Yeah, yeah, I mean, the… the thing… we…
There's still a lot for us to do here, but, I mean, one of the… one of the things, on my mind as we keep moving forward, is basically we need the ability to have multiple entities on resource that are… that are bottom.
But we also then, like, when we report relationships and things, we kind of want Kubernetes relationships to be independent of the other ones, right? So we have, like, here's a graph of Kubernetes, here's a graph of service, here's a graph of whatever.
**Dmitrii Anoshin** 22:44 Right.
**Josh Suereth** 22:45 And we might… yeah, yeah, I…
I think we have to start prototyping some of these things. So when we say, like, the bottom one wins.
we need to figure out how to actually write the code, and I'd rather focus on implementation a little bit, if we can.
Yeah.
I'm ranting a bit, sorry. You're asking hard questions, and I was… I'm actually doing some profiling stuff right now.
**Dmitrii Anoshin** 23:12 Yeah, that's hard questions for me as well. Okay, I'll just keep that in mind, and we'll think about it, maybe discuss it more during the SIG, but it's not something super critical we need to decide right now.
I think that that's it, like, I… if we don't have anything for today, we can probably wrap it up.
Thank you, folks.
**Fraggle Rock (ca-wat-brt3)** 23:37 Thanks, everyone.
**Dmitrii Anoshin** 23:39 Right.
