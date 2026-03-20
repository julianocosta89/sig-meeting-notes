SIG: Arrow SIG
Date: 2026-03-19
Duration: 70 minutes
============================================================

## Zoom Recording Transcript

jmacdonald 00:01:31 Good mornings.
Laurent Querel 00:01:34 No, New.
jmacdonald 00:01:37 Okay, we have notes coming together.
I'm looking at them.
And… And… Gokhan Uslu 00:01:53 on a little bit further.
Glad to see you.
jmacdonald 00:01:56 Agenda items coming in, We can begin soon, I think. Well, soon.
Lots of updates from Laurent this week, very good, very good.
And I would bet we can go back and look through some new issues as well.
So I'm gonna look over these while we wait for a couple more minutes.
Okay, alright. Now we're at 803, or something like that.
And, I propose we start our meeting.
I'm looking at who's… how many we have. All right, all right. Small group. Maybe some more will arrive.
And I would like to… Okay, let's begin.
I have pulled up all the new issues, it looks like about a page or so, because I know some of this stuff was… was, filed by me right after the last meeting, and I don't know if we need to go there.
But, just, just looking at the first page here of results, I can briefly breeze through these with you all. I filed a number about creating memory profiles, because we've been having, some sort of, like, last-minute Production testing and, like, recognize that Memory usage is a little higher on the Windows tests than the Linux tests, and we don't know why. So, like, we just need developers to have a better… a better time and understanding of how to, like, run this and actually see where the memory's going.
So I would like documents, because I know that this knowledge is out there, but I want it to be in the repository so that it's easy for us.
And… I think CPU profiling is easier, so memory profiling is what we're after here.
The… the upshot of all that is also that we want to begin adding the continuous testing for Windows, and, I believe CJO has, maybe gotten one PR in, so this could be… Maybe closed already, but I'm gonna have to go check. This is sort of just more of the same. We want to make sure we understand what is the low memory. Like, I'm interested in how small can I get it, and what's the largest request that I can send when I'm in a small configuration.
So, can I send a request that's half of my memory size? That's a lot, but… but maybe, maybe not. So that's the question there.
Acceptance tests for that. Okay, so then I… this is just… again, this is, like, a lot of internal conversation that I'm trying to make… make issues about so that we can bring in more people to work on stuff. So I found one about profiles, like, I think it's probably time that we, as we mature here, that OpenTelemetry has been adding profiles in the other signals.
in the other parts of our system ecosystem, so there's… the SDKs are added.
collectors and eBPF agents and so on are adding profile support. So, that's something that I think is inevitable. And then I wrote this one collect… this is a Microsoft profiling project that I think is meant to be useful to people like us. It's a Rust library.
That knows a lot about system profiling. It knows how to look up Address maps and shared objects, and all the sort of things that you need to do to actually symbolize a stack trace.
So that's there. I don't expect to discuss it much here, but I'm looking for somebody with an interest in it, and I'm going to reach out to that team as well.
So that… so now, like, that was just, like, me filing stuff, but… but I know that there's a number of open issues that I want to discuss here. Laurent, I think you have something for us on AC and NAC, so… so that… this may bleed into your topic, but I… I'm just going to, like, just, like, summarize them all. So we've got this one about supporting back pressure in the batch processor.
We've got one about receive when false does not detect P data channel closure, so there's something about that. There's batch processor before retry guidance, unsafe. I don't even know what this means, but there's something that's, like, there's a bunch of issues that are all around control, flow control, and how to control blocking when you are both reading and writing X and X, the way I'm thinking of it.
So then we've got Replace Unbounded Edge and Events channel, that was sort of connected.
And then, well, those are all the ones that are specifically related to, ACNAC channel fullness and deadlock and so on.
I would rather not look into each of those individually. They seem like symptoms of a larger problem, and Laurent's going to talk about ACNAC.
So, what else do we got? We got some bugs, So a request by our team to put a, essentially, a log view for the admin console, like, I just want to see some recent logs, because everything else is failing. And there's a PR on that, which I've already given some feedback on.
Looks like there's a bug here about OTAP dictionary handling, Albert, would you like to tell us?
Albert Lockett 00:08:13 Yeah, I can speak to this one. Basically, like, if you were to use a transformer and try to write, like, an OPL program to say, like, hey, I want to, like, remove this, this attribute value, it will, like, semantically remove it by, like, changing the attribute value, but, like, if the attribute value column is dictionary encoded, there's certain cases where, like, the actual value stays in the dictionary, even though there's no keys pointing to it, so if, like, your whole point of writing that program was to say, hey, you know what? I want to remove that, like, attribute value from the data entirely. Well, you didn't really do it right, so this is the issue, just to fix that, basically.
jmacdonald 00:08:51 Makes sense. So this stays in the dictionary, we just don't have a way to get rid of it right now.
Albert Lockett 00:08:56 Oh, that's right, yep.
jmacdonald 00:08:57 Got it.
Alright, thank you.
Okay, so I filed one asking for a file log receiver. This is, again, just sort of, like, someone reached out to me and asked, was there anything like that? I said, no. I mean, like, we understand that FluentBit and Logstash, like, there's a bunch of these things. It's… a request is for us to be able to do this with our Rust code. And I linked to, you know, like, we should be looking at what Vector's doing, because they're the largest, thing in this space that probably does that. So, also, here's the Go code that's… was donated by a company called Stanza. So, like, this is how you build a fairly robust log ingestion pipeline for files.
And there's interest in that.
So I skipped… I'm skipping over all the ones that feel like they're about acne act, full control, Looks like a bug in Geneva Exporter. I'm gonna skip over that one, if you don't mind.
We've got one about… Attributes transform signals with no attributes.
Albert Lockett 00:10:06 Yeah, I can… I can speak to this one, because I have some context on it. Basically, like, if you try to, like, use the attribute transformer to insert or update attributes, and there was no attribute record batch to begin with, it, like, doesn't do anything or doesn't behave correctly, so… That's, that's basically, like, the issue here. So I was… I was actually gonna try and, like, fix this next week, probably.
jmacdonald 00:10:28 So, like, if you have a log table and there's no log address table because there's no attributes on the log.
Albert Lockett 00:10:34 Yeah, basically, and then say, I'm gonna insert attributes, like, we say, oh, I can't find the existing attribute record batch, I don't know what to do, and then, Doesn't work correctly.
jmacdonald 00:10:43 Alright, we're gonna skip over this one. Parquet exporter template schemas have minor inaccuracies.
Jake, wanna talk about it?
Jake, I can't hear you if you're speaking. I see you unmuted.
Jake Dern 00:11:04 Yep, thank you. Lost, power to my microphone. Yeah, so just a couple minor, like, data type, like, inaccuracies or, like, missing fields, for the Parquet exporter. So, some data, like, some columns could get dropped, if, like, they're not present, and then… jmacdonald 00:11:21 template, what's this mean?
Jake Dern 00:11:23 This is… so there's basically, like, a… yeah, when I say the word, like, template, there are, like, these, you see, like, in the code snippets there, like, metrics template schema. This is, like, the unified schema that, the Parquet exporter tries to normalize everything into, is my understanding.
jmacdonald 00:11:37 Huh, I see.
So this is a Parquet representation of OTAP, and it's just a little bit manual.
Jake Dern 00:11:44 Yeah, I think they're still arrow schemas, but there are ones that, like, will nicely convert into the Parquet ones we want to use.
Albert Lockett 00:11:52 Yeah, basically, like, when we're trying to write the Parquet table, we can't just take, like, the OTAP schema and then, like, write that straight to Parquet, because, like, the columns might change between batches depending on, like, whether optional columns are present or not, so we just… we put it in a representative schema where all the columns are present and all the columns are present in the same order before we write it to Parquet.
jmacdonald 00:12:13 Got it.
Cool. We understand that Parquet and Arrow are not quite the same, so that's good.
Drew has been moving, things, and we're close to the end. Drew, do you… would you like to speak about your progress?
drewrelmas 00:12:33 Oh, yeah, sorry, I just logged in, sorry, I'm a few minutes late today.
jmacdonald 00:12:37 No worries.
drewrelmas 00:12:38 But yes, I can speak on the spot.
So, we've moved, we've refractored from crates OTAP into core nodes and contribib nodes. These are, like, the core pieces of every, component we have, receiver, processor, and exporter. What's left in Crates OTAP is sort of Shared content, miscellaneous code, that, you know, could be treated as common, would be another way to say it. Josh and Albert had some ideas in the comments of 1847 that I've linked there about where some of this code could go. So, this isn't a super high priority task.
So for example, Josh, you were like, hey, there's a PData file, it should go into P… create's PData. So I see an actual contributor. I haven't opened this PR yet, but it looks like an independent contributor.
jmacdonald 00:13:34 Yeah.
drewrelmas 00:13:35 There's a star linked to it.
jmacdonald 00:13:37 Right here.
drewrelmas 00:13:39 Yeah, I haven't looked at this yet, but I'll put it on my list.
jmacdonald 00:13:43 I also have not… drewrelmas 00:13:44 I think they just renamed… jmacdonald 00:13:46 Yeah.
we don't… I'm not sure we know who this is, but it's nice to see contributions. I'm not sure I want common. I would like to maybe remove a crate, but I will look at this today.
I'd be happy to, like, be the point person for this one if you'd like.
drewrelmas 00:14:01 But, sure, the, the good news is, like, the pressing need is done. Everything else is just… jmacdonald 00:14:09 We moved to major components, and now it should be less disruptive, is what I hear you saying.
drewrelmas 00:14:14 Yes.
jmacdonald 00:14:15 Good, good, good, good.
Laurent Querel 00:14:17 Can we, Can we… when we add help on it, can we make sure that we have a clear description of what we want to achieve?
I'm not sure that was the case.
drewrelmas 00:14:33 I think I left it a little too open to interpretation.
Laurent Querel 00:14:37 Yeah, so, I think it's, because… jmacdonald 00:14:40 This is not the first time someone has… Laurent Querel 00:14:42 What we will see, and it's super nice to see, people coming to the project, and obviously they will look at El Ponti, the first contribution, and they will go right away So we have a very strong interest to make that super clear on what we want, because those are ones that will be super deceptive for them. We will do exactly the same thing that we did last time.
Oh, by the way, that's not exactly what we want. Please rework.
drewrelmas 00:15:11 Okay, I understand. That's a great point, and I will be a little more careful about that in the future.
jmacdonald 00:15:19 Check. We've got 6 good first issues here, we maybe should go over them.
I'm not sure they're all good first issues, but… That's without looking at them.
drewrelmas 00:15:30 That's a good point, Laurent. Thank you for saying that.
Laurent Querel 00:15:33 We… Utkarsh Umesan Pillai 00:15:37 These are headphone issues, Josh.
Not the good first ones.
jmacdonald 00:16:04 That's not a good sentence. Okay, mostly a sentence. So… We were close to the top of the issues list, and I would just add a few more. Jake, found a bug about Root payload at position 0. I can imagine what this means.
I can also click in, but Jake, do you want to tell us?
Jake Dern 00:16:29 Yeah, this is just basically the same thing as what we saw with the Go code, except I'm not actually sure why nobody has hit this before, that part was not clear to me. I would think we would, because we send, like, rust to Rust all the time.
But the code, like, very clearly is looking at, like, payload0.type to, like, do some branching, and so I just… this is something I noticed when I was working on that, that PR that's out right now about spec compliance.
And I just flagged it for… for follow-ups.
jmacdonald 00:16:57 Okay.
What are we to do about it?
Jake Dern 00:17:01 Oh, well, the code change will be very, easy to make. I think I mentioned something in here. Yeah, it just needs to, like, do the conversion to log metrics, traces, OTAP batch store, and then check for the root payload presence, so, yeah.
jmacdonald 00:17:16 So we don't require the order among batch arrow records.
Content types.
Jake Dern 00:17:24 Yes, yes.
Laurent Querel 00:17:26 But, we… I think it will be a good practice, like an optimization, that, An exporter will, put, record zero, ideally, the main record, even if it's not required.
In order to, minimize the work for the receiver.
When we have to, connect or connect it together.
Jake Dern 00:17:54 Yeah, we can definitely, definitely look at it. The main reason why I haven't seen, like, a huge benefit for it is just the fact that we already have 3 separate endpoints. So, like, when the data's coming in.
You kind of already know, like, oh, well, this is supposed to be traces, this is supposed to be logs, this is supposed to be metrics, so you kind of know the root payload type that you're looking for.
But it, you know, if it's missing, then yeah, you can find it faster, or find it out faster if it's at zero.
Laurent Querel 00:18:22 the type, the type router, I think, only has access to, to the table right.
The signal type router.
Doesn't know which entrance you reach.
And sometimes, for example, syslog to, the syslog receiver.
We generate, our records.
So that there is no, Grpc input, Signaling, so we obviously know that it's a log.
what I'm seeing is, this information, regarding the endpoint, I don't think is currently, represented into the OTAD batch.
Albert Lockett 00:19:12 Yeah, I mean, the OTEP batch that we send around is an enum internally that has, like, logs, records, or logs, traces, metrics.
Jake Dern 00:19:19 Yep.
Laurent Querel 00:19:20 Thank you.
Okay.
Jake Dern 00:19:22 Yeah, there's 3 implementations of that, OTAP batch store, yeah.
Laurent Querel 00:19:26 Yeah.
Thank you.
Jake Dern 00:19:29 But yeah, if there's, like, a reason I'm not aware of, I didn't quite follow the Ceph, stuff that you're talking about, but yeah, we could definitely spec this out. I was just kind of erroring on the, the side of, like, less requirements, and simpler spec is better than having, like, this position zero, yeah.
jmacdonald 00:19:45 the same kind of confusion comes in with the OTLP representation as well. You have some bytes, and it's up to someone else to tell you what those bytes are, like, which signal type they are.
And if you parse them as the wrong type, you'll get something that, you know, you didn't intend, because… They are not self-identifying.
those, those types of data. So I think the same is true of Arrow, like.
Unless we're careful, and… You can… you could mistakenly put, like, a traces arrow data, OTAP batch, and call it logs.
And it would be somebody downstream would maybe detect the error.
Just like Jake was saying, I think.
Jake Dern 00:20:28 Well, hopefully after my PR goes through, that will happen much faster. And in one spot.
jmacdonald 00:20:36 Anyway, I think we all understand at least what we're discussing, and it sounds like a corner case we should take care of.
Before we move on to the main content, there's a few more here. I… I think that, actually, the two of these are, are quite connected. I filed one based on an internal conversation, because we're looking for, like, top-of-line Windows performance, and then Ukarsh has signed… has… Who's here on the call, has filled in, I suspect a related topic, and I would like him to discuss it with us.
Utkarsh Umesan Pillai 00:21:09 Yeah, sure. So… This was mainly to, support our flexibility in, in future to choose a different async runtime if we desire.
So right now, we are very tied to Tokyo, like, the individual nodes, such as receivers, processors, exporters, they explicitly call Tokyo APIs.
And that basically is relying on the assumption that these tasks, the exporter tasks or receiver tasks, they are being driven by a Tokyo reactor or a Tokyo runtime, and… ideally, what we want is they just call some abstraction API. That abstraction could reside in the effect handler.
So that, The engine is the only component aware of what actual runtime gets used, and if we want to make a switch, we can do that switch in the engine, and we don't have to make changes to any of the nodes.
So, that's the whole, idea.
Oh.
Yeah, and then there's a lot of details about, like, the usage, the current usage, and, like, which ones are going to be tough to abstract out. Like, Tokyo Select Macro is going to be a little tricky than, the other ones.
So, yeah, not strictly related to the Windows SOD support.
jmacdonald 00:22:30 Let me, yeah, let me pull that up just then, because… because this was, like, a, statement that essentially says that SO reuse port is not how you do this in Windows, and then Ukarsh has given us a rather… complete.
pseudocode of how you do this in Windows, and it might require some runtime changes, is what I'm imagining.
Utkarsh Umesan Pillai 00:22:51 Yeah, so this pseudocode is still, relying on Tokyo runtime, like, I think you would see, I'm, like, creating a current, current thread runtime instance here.
So, as long as it's residing in the engine, it's fine. It's easier to make a switch to, let's say, from Tokyo CurrentThread, we want to move to Glom I.O. or Mono IO later on. It's possible. This wouldn't be… like, the nodes wouldn't see this, so… that's the relation in terms of the Tokyo runtimes, but yeah. Like, this one is more about the SOEU support not being supported.
jmacdonald 00:23:26 Yeah.
Utkarsh Umesan Pillai 00:23:27 Yeah.
jmacdonald 00:23:29 My sense is that LaRot was dreaming of abstracting the runtime at the start, and I know we've discussed this with Microsoft Oxidizer team. Everyone loves this idea, and it's super, super hard, I think is what I've heard.
Laurent Querel 00:23:44 Yeah, I would be super happy to see that, and I know that that will be a definitively complex But, if we don't try, that will never happen. And regarding the oxidizer team, Could you give us, maybe, if it's public, or shareable in this group.
Maybe a status on this project, because we had a discussion at the beginning.
If I remember well, it's a thread per core.
jmacdonald 00:24:19 Well, I… yes, I'm and what I know, I don't think I'm saying anything that's not public, but this is a project that Microsoft is backing and has an internal and an external, like, the wish is to open source everything, but really the driving goal is to improve Rust performance for internal Microsoft services.
And they're… they're open sourcing things At a pace that they feel comfortable with.
So… even though we have talked with them about exactly this problem of runtime abstraction, they see the problem, they are excited about it too, they know it's super hard, we all agree it's super hard, but this is what they've been doing.
And this is actually… the last time I looked at this page, there was only two packages published, so a lot has happened since the last time I looked. I've been using the data privacy package myself for something personal, but this is, Anyway, this is what they're doing, and we do have a meeting with them, I do, next week, so I can answer this better, this question better.
Laurent Querel 00:25:21 Okay.
jmacdonald 00:25:23 Alright. Well now, there was one more here, last but not least, Jake. Timestamps are hard. Oof.
Jake Dern 00:25:32 Yeah, I think this is just, like, a thing that maybe we didn't think about, but you can specify a time zone, an arrow, for your Unix time. So, like, that specifies, like, what time zone the Unix epoch, like, moment was in. I think in Go, I discovered that we do use UTC explicitly. I think in Rust, it looked like we didn't.
And so this is just a small thing to just say, I think we should require UTC time zone attached.
Because technically omitting it is ambiguous, and we should just specify that and be done with it.
jmacdonald 00:26:06 I agree.
the handling timestamps in SQL databases has always been a challenge, but let's use the timestamp with time zone, not the other.
Cool. Alright, now we're back in the main topic.
Laurent has a… draft PR that is going to address all of our woes, related to ACNAX and deadlocks.
Here we are.
Laurent Querel 00:26:40 Yeah.
jmacdonald 00:26:41 Exaggerating.
Laurent Querel 00:26:43 It's still work in progress, and it looks like it's going well, based on Lalit feedback I got yesterday.
Can I share my screen? Yeah. Various things to… jmacdonald 00:26:58 Let me… there I am.
Laurent Querel 00:27:03 Okay… Yeah, let's start with, There's this bar that is there.
Sorry. Just need to reorganize.
And not on a big stream, a big stream.
Screen today, and the real estate is, My TV is smaller. Okay, so… Like most of you probably know, we had, following some, internal, tests on Microsoft.
We observe various issues related to graceful shutdown.
Related to, ACAC, some deadlock.
some, acne, like… Lost… lost message.
So… For me, that was the sign that probably we have some issues, into the internal architecture of the engine.
And, so I decided to look at that and, and try to… To figure out the… the root cause… well, the root causes, in fact, in that case, of the values issues, and see how we can, Better design the engine to remove those issues, and also how we can, Validate, as much as possible, the engine.
And that's why I introduced, This concept, the deterministic simulation testing.
But, so I will talk about that a little bit more, that it's basically how can we, simulate… Border cases, complex situations.
On the existing code?
To, validate that, the corner cases, the deadlock that we observe, for example, is no longer something that could be, observed with the existing engine.
So, what I understood from the values, and I'm not sure that I covered every aspect, but at least I think I covered The most important one. And it looks like, based on the, the small run that Lalit, did yesterday.
On your internal Microsoft test.
he didn't observe any issue with the PR.
Except one for one of the exporters, I think it's… I don't remember if it's the Geneva Exporter, or the Azure Monitoring, blah, I'm not too familiar with that. So the… you were thinking that probably it's more something that is related to the… Custom code of the exporter and not related to the… The machinery that we have into the pipeline runtime.
So, It's a little bit complicated in terms of diagram, but I will try to do my best to summarize that as much as possible.
So, one aspect that was, not properly, designed, initially, I think is, how the Graceful Chip Dunn, need to be achieved… is achieved? And is there a way to do it, in a, in a… In a way that, makes sure that every external source, when… When the system is configured with the wait for result.
How can we ensure that a graceful shutdown under… good condition will return systematically AC for a remessage.
scent.
So initially, we… what we did, is when we receive a shutdown.
could be, achieved initially. So now we have two ways to, to achieve a pipeline shutdown.
Either with the admin API, or if we receive an OS signal, I think that's something that has been recently introduced.
by CJ, if I remember well. So, we receive a pipeline shutdown.
And the system was sending a shutdown Signal, a shutdown control message to the receiver.
And the problem was, basically we… until… before the current PR, what we did was… We have this loop inside each receiver that consumes There is a competition between, consuming The control channel and the external source.
external sources could be TCP, UDP-based.
In the future could be file-based.
So the… the… once… once we receive, the… initially, once we receive the… the control message shut down.
We did some… Work to clean up, and then we, We exit the loop, and we return the terminal state.
It means that every ACNAC message that we're not yet Return, to the receiver.
We're basically lost.
So what I, I did is introducing, A two-step process, only for the receiver.
There is no real changes, for the processor and the exporter.
And I will, extend that later.
So, the split consists to… Let's see, we reserve a shutdown, so the runtime control message manager will emit to the receivers.
a drain ingress. It's a new control message. And when a receiver receives that, it has permission to stop… Any, incoming traffic?
So, either new connection or existing connection. So, obviously, new connection will be just, not accepted.
an existing connection, New incoming information will be rejected.
But we will keep the connection open in order to return result regarding AC and NAC.
So once, so the drain ingress phase stops once the receiver As, his own internal, Axelot?
ACNAC slot, I don't remember the exact name that we use for that, but basically we have a data structure that maintains the, Like, a completion, a set of completion tasks.
And, when we receive from the, what I name now, the return pass, or the completion pass, from downstream component, we receive an AC or an AC, If the wait for result was obviously enabled for the receiver.
Then that will update this, Completion slot, data structure. And once this… the structure is empty.
It means that we are at the end of the drain ingress stage.
And, and, the receiver is, required to, notify the, basically the, the runtime.
Or receiver, drained. Well, drain instead of drainer.
And that will trigger a shutdown, for the… A shut-down process for the processor and the exporters.
And also, once it's done, the receiver will terminate.
That will have, a cascading effect.
It terminates, so that means that this sender for the pilata channel will be no longer there, and the channel is in a state where you can drain, but once there is no longer message, the piloted channel will be basically closed.
And that will have a cascading effect.
The processor, will, consumed the last P data, we receive the shutdown, and we'll, we'll end, and so on. Obviously, if everything is going well.
That's why it's named a Graceful Shutdown, because, obviously, when we have Let's say some panic or something that is not well understood.
The system will not magically, transform, this graceful… I mean, this issue in a graceful shutdown.
The panic will be captured. That will not break the entire system.
That will just, make the corresponding thread of this pipeline.
Failing, but that's it.
So the, the, the second, important thing that I did is, in order to avoid to have some… very, So we observe a deadlock because we basically had… we basically had A pipeline control message channel, Combining different types of, control messages.
the ones that are related to AC, eye volume.
High volume in terms of number of message, not in terms of… necessarily in terms of, pure volume size. Sometimes that's the case, because we… we have this, Sometimes the… the data that is embedded into the… this, ACNAC message.
And we have what I name now the Runtime Control Channel that is basically, Things like, we want to start or cancel a timer, a collection, telemetry signal.
Or delayed data, this kind of stuff.
So, I split these two.
And I made, here also another change to make sure that we we can't be in a state where, because we are no longer able to publish P data.
And because we are waiting for ACNAC… so there is, now, what I name a bonded fare mechanism.
we, we basically consume a budget of control message if the… if this not control channel is Contains some content.
And after, consuming this budget, we make sure that we, we consume some piletta.
Yeah, and so there is, a more, precise description of those value stranges in the, I think, in this page, in the REME.
where I try to, to describe precisely, the… Let's see… Yeah, that is okay. Yeah, here I'm describing why I split, basically, the, The, the pipeline, control message channel into, two, control, let's say, runtime.
control channels.
And, yeah, a description of the, an example of, deadlock.
Is described there, if you are curious.
Yeah, I'm not sure describing the dynamic of those things, and so I think the… In order to, to keep, this part of the… the report not too long. I think the important or interesting part is… I'd like to talk about the DST.
Yeah, that's in the stability… Yes.
So that's something that is… not fully… I mean, we… I already have multiple scenarios.
I definitely need to expand that a little bit more.
It's a technique that is used In databases, in general, when you have a complex, system.
With concurrency or distribution.
it's becoming very common to use DST, so the deterministic simulation testing.
In order to capture without running real tests. That could take, forever.
The goal of the deterministic is to make sure that If we detect an issue.
we are able to reproduce it just with, a SID number.
So the idea is we… We, we exercise the system.
With, many simulations, with different seeds.
And those simulations will, will, basically attack the system in different, on different angles, and if we identify an issue, we are able to reproduce it. And that, so that means that once this system is in place.
If, in the future, we, We change something into the, the logic of the engine.
Or if we add some new features.
That will be much easier to determine if we are still compliance with, the contract, that are expressed by the DST scenarios.
And if we are not, we are able… so that the system will deliver the seed, and then, As the contributor of this change, you will be able to reproduce it in a debugger, for example, and look at exactly what is happening.
So that's the idea behind that.
In order to do that, and to be deterministic, One of the major issues is… there are two major, non-deterministic functions, the time and, randomness.
So, what, is done there is, an abstraction of clock.
And so, in, Production mode. So if we create a release, a standard release.
We will use, as before, the exact same, Tokyo-based, Set of timers, and and, the… the API to get the current time.
When we are running in a DST mode, we have a sync clock.
which exposed the same API, except that we, we, We are able to accelerate the time, and we are able also to, Yeah, we are able to accelerate the time, and around them, Same thing, we… we are able to, to regenerate, to seed the random function with an explicitly… an explicit seed.
So, it means that if we rerun the same, simulation, we end up with exactly the same sequence of events.
So I described here the scenario on which I'm working, Yeah.
Yeah, in the failure mode, also, I try to address.
So, as I said, let it run various tests. I don't know the test that you are running. I did some tests also on my side.
And I run both, various DST scenarios.
I think it's, in a better shape than it was before.
I'm not 100% sure that we covered every issue, but at least it's going in the right direction.
Any question on that?
jmacdonald 00:45:05 I have quest… a question, and I'm not sure… how to say it other than to ramble right into it. So… I remember, like, in university studying operating systems, and, like, there was a lecture on deadlock. I'm just kind of revisiting my, you know, my learnings on deadlock avoidance.
And, at some level, I'm… I'm, like, worried that we got this far without thinking about this before, what was I thinking was going to happen here? I think I was assuming we would just drop the axe and knacks, which is still an option for us. Like, we don't… we have not promised the system must deliver every single act and knack.
Because it's our only safety valve, our only pressure relief valve, if there's going to be a deadlock.
Laurent Querel 00:45:55 But… jmacdonald 00:45:56 But still thinking in sort of the abstract, general sense, if there's a node like an exporter or a processor, which is trying to send an ACNAC and is going to block what I ex… backed from, I guess, first principles, is that it has to begin servicing its P data channel instead of being ACNAC blocked. Like, the basic lecture that I remember was, if there's a danger of deadlock, read the network before you write the network, because… if you don't read, then someone else is waiting for, you know, is blocked on you, and you can't send to them. So, there was a sort of general guidance, was read before you write.
And… I guess I'm wondering, how do we… how do we service the input channel While we're blocking on the output channel.
Laurent Querel 00:46:45 So, so that's why I split first the… What we name initially the pipeline control channel.
Because, for example, if we want to make some progress in The retry processor, or the batch processor.
We need to receive the timer messages, the timer tick, And, if, we… we share the same… pipeline control channel, between the, the ACNAC and, and… Those more runtime-oriented, control message.
we definitely have, like you said, a risk of deadlock. Second, there is this, guarantee now, which was not the case before.
that we will always consume Pdata channel.
Even if we, we, we have still things to consume into the… the, not control channel.
jmacdonald 00:47:52 I'm thinking through this case of a batch processor. I know there's an issue about The batch processor, has a map of inbound context and a map of outbound context, so it's… it reads data until it's finished a batch, and then it… it keeps some record of each input while it sends the output batch, and it's waiting for the output ACNAC, and then it goes back to the input and ACNAX all of those. And there's a point where the input context map is full.
if we read another P data, like, we can't handle it, we don't have anywhere to put it. So we are blocked.
We don't want to read the P data channel.
We do want to read the node control channel.
Laurent Querel 00:48:37 That's why the accepted data has been introduced, I think.
jmacdonald 00:48:41 I guess I'm just concerned that if that batch processor happens to be writing a node, an ACC NAC itself.
And the completion control channel is blocked… blocking it.
and something is blocking the completion message dispatcher because the receivers aren't listening to their ACMEX because they're trying to write to their channel. I guess I'm sure… I'm still imagining a deadlock, but I… Because you've separated these queues, but there are still fixed capacities. I guess is what I'm… what I'm thinking.
Laurent Querel 00:49:21 Oh, yeah.
jmacdonald 00:49:21 When do we start dropping?
Laurent Querel 00:49:23 Yeah, I mean, there are situations where the system will be blocked, but I think for good reason.
The one that you described, or the… so the one that you described, let's imagine that the exporter Downstream exporter or exporters.
For whatever reason, they are not able to make any progress, because the… The downstream backend is not building well, or not accepting anything.
Not behaving properly.
So, there is no point to continue to accept Pilata, right, in that case. Because, anyway, we will not be able to do anything with it.
So, it's totally okay, in my opinion, in that case, to block And basically propagates the back pressure to the… To the external source, or sources.
Yeah, and, and, and adding, Unbounded data structure, like, channel, in the mix.
We'll just make things even worse.
So, At some point, when we are no longer able to make progress because the exporters are not responsive.
Yeah, we progressively fill in the various channels.
We, and… and if we are not able to make any progress on one… one side or the other, the… either the… the control, or the PDATA channels, we backpropagate the… we backpropagate all… yes, we backpropagate the pressure, and we, we just stop to accept any traffic.
I was thinking about a receiver situation.
Yeah, so another example of situation where it's better to block and not having… An unbounded, ACNAC channel.
If we have, an external data source that sends signals the receiver… And this receiver is configured with the wait for result.
And, and the corresponding protocol used by this external source accepts, there is a return pass, and we… and we accept ACMAC, let's imagine.
What's your view, what's up?
So… In that case, we want to be protected against A misconfigured, a mis… Implemented, or a bad actor that… We'll send, data, but we'll never… Accept any, return messages, I think.
So, we, we will accumulate in that case, the ACNAC.
In the… Do not control… did not control, Channel, and potentially the compulsion control channel.
Just because we have an external source that blocks us to… in fact, does not interpret at all.
And doesn't read at all the… the return message we send back to the source. So, in that case, In my opinion, the best reaction is, once we reach this point, which we stop, basically, to consume pilot.
And and either, because it's not… it's an abnormal situation.
And, it's probably the best option we can do when we have a… A bad actor, and if it's a misbehaving but, valid, let's say.
Good actor, external source, that's also, the best answer, in my opinion, because, They have to fix their issues.
Did I answer your.
jmacdonald 00:53:49 Yes, I think you have. I maybe want to spend a little bit of time thinking a little bit more about why I think, there's something That I don't quite understand. But.
Laurent Querel 00:54:01 I think the, yeah, this player is definitely a work in progress. I think that would be nice to have, Open distribution there, in order to, If we have any issues, still, just, iterate on that, and making sure that we have, A scenario that exercised the… the issue that you… potentially, describe.
And we validate that the system is able to, to behave properly or not.
jmacdonald 00:54:36 I will, lend a moment to thinking about that, myself, and I'm gonna ask if anybody here wants to comment on this now that you've presented it.
with Karsh.
Utkarsh Umesan Pillai 00:54:48 Yeah, Laurent, could you go back to that diagram? I had a very quick question. So, so I see that for, receivers shut down, there's, like, a drain ingress and receiver drain.
So are we not gonna do this for processors and exporters? Would they just receive a shutdown signal directly?
Laurent Querel 00:55:06 No, because the way that the… the grace food shop done was working, and still working. That's the… the only modification I did, but, initially, the shutdown message… was initiated there, And, and, technically, we… the… let's say, the controller of the pipeline runtime is not directly sending shutdown message to processors and exporter. It's an indirect, event that happened because the PDAT channel has been closed.
by the upstream, node. So, in this example, Once the receiver, terminates.
The corresponding channel, the sender side is closed.
So there is, A generic mechanism in any channel.
So the… The receiver side is aware of that.
And we… we can drain the remaining PDAT channel, and then… That will be, so we have this, like, helper script, that is used by processors and exporters, which is named message channel.
And the message channel is basically generating internally a shutdown to let the processor and exporter do their… their job, but It's not the same shutdown method that we have here, emitted by the… the… the pipeline runtime controller.
So, true.
Utkarsh Umesan Pillai 00:56:50 The processors and exporters would continue to just, look at the channel closure To determine if it's a shutdown.
Laurent Querel 00:56:58 No change there, yes.
Utkarsh Umesan Pillai 00:57:00 Okay. Yeah, I was asking mainly because there were some PRs recently about that, I think, like, trying to send a synthetic shutdown signal somewhere in, like, a receipt bin, and there were some issues, but I'll also just, like, go and check the code changes more, too.
Laurent Querel 00:57:15 Yeah.
Utkarsh Umesan Pillai 00:57:15 Figure out.
Laurent Querel 00:57:16 They will receive a shutdown, but it's a shutdown that has been, generated by this message channel that is the helper that you are using to basically process the PDATA channel for the processor.
Or for an external.
And this message channel helper does not exist with the receiver, because we have a different, situation.
We have an external source that competes with a control channel, a not-control channel, and, and that's the responsibility of the receiver to To manage this loop properly, as opposed to the processor and the exporter, where the… The interaction between the… the controller… the nut control channel and the PDATA channel. This logic is handled by the message channel, and it's a common code reused by the processor and exporter.
jmacdonald 00:58:30 I see the difference between the receivers in this case, so I guess I… it makes sense. I also see a comment in the sidebar from Aaron saying, we're all going to think about this. So, I definitely like the separation of completion, dispatch, and runtime control. That part seems necessary, because we were… otherwise, we were ahead of queue blocking, you know, when we needed to deliver certain messages. I still want to convince myself that there isn't a deadlock, especially involving the batch processor.
But I would be glad to think about that, you know, after the meeting here.
We're almost out of time, and I know there was a… Laurent Querel 00:59:10 I don't have a mini brain on that.
jmacdonald 00:59:12 Yeah, yeah, yeah. I know we're almost out of time, and I wondered if we want to just briefly advertise the other work that you're doing. I know that it's not.
Laurent Querel 00:59:20 So… jmacdonald 00:59:20 of mine for us, but… Laurent Querel 00:59:22 It was, in fact, something I was working on for one, two weeks.
And then when we had this recurrent issue, they decided to put that in a standby mode, and but… and focus on that to serve various issues. So that is… a requirement we have, for i5.
Which is, the ability to… Manage the lifecycle, of, pipeline.
Dynamically.
So we should be able to shut down a pipeline at any time.
And we should be able to, reconfigure a pipeline.
And the reconfiguration of a pipeline could be… Oh, you already, you already signed, the DAG?
Internally, or you, you want to, to, Scale up or scale down the number of cores for the corresponding pipeline.
So… So that's the purpose of this PR.
And, so I, I basically created, I will go very quick, try to retrieve.
The infants, where are they?
So, yeah, I don't retrieve them right now, but, so I basically extended the admin API, which is currently a REST API, I think we should, decide and investigate, if we want to support OpAmp.
as a second, type of API for the management of the configuration.
as far as I know, OpAmp has been designed just for that, so that will be nice. I think, if we can support it.
Alternatively, And, So the… I don't have any demo to do there, because basically I didn't add this morning, the time to prepare the system, but it was working. I need now to merge with all the changes that happened in between, but With this modification, we are… we should be able, for example, to have a situation where we have a group with an ingest pipeline and a processing slash export pipeline.
Or an ingest, and multiple tenant-based, pipelines.
And let's say you want to increase the number of calls for a tenant.
This feature will give you this capability.
Or if you want to change the configuration of, the data processing related to the… to a tenant, again, we'll be able to do it. So that's the… The goal of this, and that will obviously require to have a very good, graceful shutdown, mechanism.
So when I did the test, I was not in color cases, it was working well, but obviously, based on the feedback We, we got from various tests, That didn't work, in any situation, so the… Once we have the… this redesigned Fully implemented and tested than this one.
We'll just narrate the improvement.
And the way… something I didn't mention, so when we have a pipeline that needs to be redeployed.
It's a rollout. So we basically… let's say the pipeline is running on streetcore.
We have a new configuration.
So the way it's working, we start… We over-provision, so we start the new configuration, On one of these scores.
So we basically, for one core, we have a… we all… we use this… but we have two versions of the same pipeline, or two generations of the same pipeline running at the same core.
For a short period of time.
Based on the… the system event, once we… we… we observe that the… the pipe… the new pipeline is ready.
Then we shut down the… The previous generation, and we go to the next one.
And we do that, until we reach the end. And obviously, if there are some, Problem during this rollout.
We, we roll back to the, to the previous version.
I'm sure that we will, put in place some policies to, To make some variation on how the system is behaving when we do this kind of operation.
But, right now I… Just implemented a basic policy.
jmacdonald 01:04:35 This is just for pipelines, because we can restart the thread.
Laurent Querel 01:04:40 Yes.
jmacdonald 01:04:41 No.
Laurent Querel 01:04:42 Yeah, right now, the library configuration is at the pipeline level only.
it's not at the node level. That could be… implemented, but I think it's… more complicated.
jmacdonald 01:04:57 Yeah.
Laurent Querel 01:04:58 And I'm not sure that it's really… fundamental to support it.
Maybe we could at some point. But definitely, the ability to do that at the pipeline level.
Offer, in my opinion, a lot of, interesting characteristics.
Just being able to add more resources to a pipeline is one example.
There are some limits with this system which are detected.
So… One limit is… The, the… so, with the topic mechanism that make the… Communication across pipeline possible?
The topic, the system that is, deciding which topic, Implementation to use is based on the analysis of the topology, the initial analysis of the topology of the different pipelines.
So when you run in an optimized way, mode, If the new pipeline, for some reason, will involve a change into the implement… the optimized implementation of the topic, that will be rejected.
But if it's compatible, the pipeline reconfiguration will be accepted.
We could run… we can run it, I think, in this, Here, it's already supported. If you know that you want to be very flexible in terms of topology of pipelines and how they are.
Connected to, to, to, to topic. You can run, You can run the engine initially in a mode where Any topic can be consumed For the way that they are consumed, the various type of subscription.
Can be dynamically changed, and then in that case, we don't have this limitation.
But, in the, in the tenant, example that, I think Lalit, mentioned, it's not, it's not a problem, because we… We basically have, one topic, pertinent.
We don't change, really, the… we don't have to change the internal optimized implementation in that case, and then the pipeline can be, Or configured. You can add additional steps, you can add more cores or remove cores.
That we, that we.
jmacdonald 01:07:49 When you say optimized implementation, it's the particular choice of topic connector that was made?
Laurent Querel 01:07:55 Yes, so the… for the in-memory topic, that will not, that will not be something that we will apply to, for example, once we have the a quiver-based topic.
Oh, Kafka-based topic.
They… they will probably not have this limit, this limit. But for the in-memory, because the in-memory have been designed to Get the maximum throughput possible?
When we don't run in the non-optimized, and that's the default one, when we are… When we are not running in the optimized version of those in-memory topics, we, We have to… the engine decide If it's a purely, load balanced… if the… all the subscribers are purely consuming in a, with consumer groups, so load balancing.
Or if the consumers are only, broadcast-oriented.
And if we have a combination of two, then the system will decide, oh, okay, that's, a mixed, Situation, and we… and we use the… the less optimized version of the in-memory topic.
jmacdonald 01:09:14 Got it.
Okay, well, we're out of time, and I think, this is a good introduction, so if you do open this PR in the next week, we will know what we're looking at.
Laurent Querel 01:09:27 Yep.
jmacdonald 01:09:29 Okay, thank you. I think many of us have agreed that we're going to think about the deadlock question. I know Aaron said he would, I will, and And I'm gonna follow up on that, because I think there's… I have still a few questions that I have.
So that's what we'll do.
Laurent Querel 01:09:46 Sure.
Perfect. Thank you.
jmacdonald 01:09:48 Well, thank you all for listening through a meeting. Here we are again. I'll see you next week.
Laurent Querel 01:09:54 But…
