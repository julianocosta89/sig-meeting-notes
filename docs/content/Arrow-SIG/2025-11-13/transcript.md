SIG: Arrow SIG
Date: 2025-11-13
Duration: 63 minutes
============================================================

## Zoom Recording Transcript

Albert Lockett 00:00:31 Hey, Ukersh.
Utkarsh Umesan Pillai 00:00:34 Yeah, but…
Albert Lockett 00:00:36 How's it going?
Utkarsh Umesan Pillai 00:00:37 Good, how are you?
Albert Lockett 00:00:39 Pretty good.
Joshua MacDonald 00:01:50 Good morning, can you hear me?
Alright.
First time.
I think we'll wait another minute or two, Okay, let's see, who's here?
Just checking. I know I'm expecting Laurent today.
And… He may show in a minute or two.
Otherwise, I've put up the… Notes here, and I'm gonna start writing in some… Total attendees.
I'll do it for you.
All right, who else do we have here? Okay, this looks good. Well, I know, I know that Laurent is gonna come, so I'm just gonna, maybe stall for 20 more seconds, or something like that.
And then, bring you back to… Starting with, I guess, issue triage, And I'm sure we have some… some topics here of varying levels of interest.
So it may be nice to start with the recent issues. I also have a short list that I wrote down that I think we're going to discuss, and then I do want to hold space today for a fairly large proposal. Aaron is here with us.
And, this is a proposal for a subsystem called Quiver that will be our persistent storage layer, we hope. And I've been… working on that, or reviewing for Aaron the design proposal for a while, so I'm pretty pleased that we're here to talk about it in public.
So I want to hold space for that, and then, let's see, any new issues would be, like.
Yeah, somewhere since around 1390. I know that, But I'll tell you… I'll tell you that I want to start with, where do I want to start? Hang on a second.
Still not… still no longer on. Okay, we're starting, everybody.
I'm gonna start with one that I filed before… sort of quick and easy stuff. We are… starting to ask ourselves, when do we publish our crates so that people can try to link against them, or import them into a main function of their own, or any of those things? And I'm sort of, sort of starting to collect all the reasons why we might not want to do that, or what are the blockers for us on that topic, and so I've written one of them here. Like, we have a lot of allow missing docs annotations left over from the beginnings of our project, when we imported the OTel Arrow Rust.
they're still there, they need to get… they need to be taken care of. This is sort of, like, just kind of glaring lint that I see when I look at the code now.
And I also thought that we should start being honest about our changelogs, like, we just don't have them, and we've been building Go change logs for our Go codebase, which hasn't really been changing much at all, and then we publish, you know, Rust crates have been just… we haven't published Rust crates yet, but once we do, we're gonna need versioning, changelog management, stuff like that.
And those are, let's see, the ones that I know are, important to me. Those are sort of administrative. Albert, looks like you've filed something new talking about… Api design for… And I'd love to talk to you about that.
As far as triage, you want to give us a quick explainer for this?
Albert Lockett 00:06:23 Yeah, maybe you could click on, I think it's 1394, was sort of the… the high level, I guess, like, epic that I opened for, the… I guess, like, kind of… for two reasons. A, for tracking the, the learnings that, we had after we did the, data fusion, proof-of-concept kind of columnar query engine, just to try to identify the, the functionality gaps… yes, that's this PR here, 1342. So this Epic that I opened at 1394 was just to try to identify, here were, I guess, like, all the pieces of functionality that, like, weren't implemented.
And then, based on our learnings from that exercise, like, what I think we should do differently when we implement this in maybe, like, a more production quality, less proof-of-concept type of, type of implementation.
So, you can see the feature gaps here, and I won't go through everything here, because I want to… I also want to hear about Quiver, so I want to, like, leave some time. But, the moral of the story here is, so 1497, was just to try to, lay out what I think should be, kind of, like, how we should structure the… kind of the top level of that query engine.
how we should, what should be the APIs that we expose to, to invoke, planning, how should it receive the, the pipeline expression, because what was implemented in that proof of concept 1342 was, extremely awkward.
These next two, are, are sort of, brainstorming, and I'm not sure if I, really like this solution after, working with Laurent, but there are a few things that are a bit awkward if we try to build, a single data fusion plan to execute one of our KQL queries, right? So take, for example.
The idea where we have a query that we want to filter logs by some field, and then update all the attributes for the remaining logs. Well, because our OTAP batches are denormalized in the sense that logs is one record batch, and attributes or another record batch, you end up with this data fusion plan where you have an in-memory table for logs, and then you end up switching to a different in-memory table in, the middle of the plan, and then you end up trying to, like, write that back into OTAP Arrow Records, which is our container for all the, different, record batches for each payload type.
So, The, the second issue I opened there was kind of trying to say, if we did want to do this in one big plan, what would be the custom data fusion operators that we would need to, implement to be able to support that, and how would OTAP aero records actually get passed around?
But after discussing it a bit with LaRom, and I think he's probably right about this, one thing that might be simpler would just be take our KQL pipelines and break them into, some… some… I guess a series of data fusion plans, and then have the top-level API invoke those plans serially while shuffling the correct, record batch into them, and updating OTel Arrow records, as a result. And that way, you don't need some kind of closure over hotel records with some kind of, like, ARC mutex inside it, which is, which is a little bit awkward.
weird.
And so that was… that was what was going on in 1409, and then 1410 was kind of, a similar design for filtering, to say, like, if we did want to have, a custom, data fusion execution plan step, which is a step in the physical plan for filtering where we want to filter by attributes, how would we implement that in an efficient way? Because in the proof of concept that I did, what we were doing is we were doing these joins on attributes to, say, for example, the log record batch, and that got really untenable when there was a lot of different filters that you want to perform on your on your attributes, including, like, logical, ORs and ANDs and things like that, you can see that these are some of the plans that were, created in that proof of concept, so I said, that's… that's extremely awkward.
And, we already have, in our filter processor, some, custom code that just uses the arrow compute kernels for the kind of filtering, and it actually performs better than doing these joins, so… This, the design of this issue is just trying to call out that, if we do want to do, these, these kind of, like, filter by attributes in our data fusion plans, then it might be, It might be more performant to, to create a custom, filter execution operator for that. And, so that… this issue was created to kind of track that.
And discussed what I thought the, the, what requirements of that filter operator were. Now, I've kind of, like, since, like, writing this up, kind of backed away from that, in the sense that, like, in that top-level API, issue that I created, one of the things I tried to do was to say, is there a way for us to have stages of our, of our KQL pipeline that are implemented by DataFusion, and maybe stages of the pipeline that are implemented just using custom compute kernels, which would maybe make it easier for us to share code from our processors without having to wrap them in a DataFusion execution plan?
So, I'm not actually, 100% sure yet if we actually need to do what was documented in, 1410, but I was more so just, like, creating the issue for, sort of her posterity, and also just to try to, like, get my thoughts down on, on paper about, about, here's a potential way we could do, filtering.
So, yeah, hopefully… I realize maybe the, the description of this is a little bit, mixed up, maybe it's a bit of a brain dump, but, that, that was, that was, I guess, like, the raison d'etre pour for these, for these issues I created.
Hope that makes sense.
Joshua MacDonald 00:13:08 Yeah, I think I… I think I follow… at least I… in my own way, reached the sort of similar obstacles when I was fiddling around with DataFusion, in my one little hackathon effort, right? So, I remember kind of doing contortions. I think what you're describing is the same, essentially, thing, like, where I'm… Joining the log attributes.
with the logs.
In one giant query.
Because I can.
But it feels awkward and unwieldy.
And it didn't help. That was just to deal with two tables, where I was joining one with the other, and I don't know how I would handle, like.
the complexity, so I'm glad to see you've… Written it up.
It sounds to me like you've written this for recording's sake, and, are… effectively know what you're doing, and, have been discussing it with Laurent, so thank you.
Albert Lockett 00:14:05 Yeah.
Joshua MacDonald 00:14:06 Very cool, and Great. I'm trying to think about, for the meeting and the agenda here, I think… I have a few things left that I know I want to talk about, but I think we should move on now to the Quiver proposal, which, has been eagerly awaited, and, well, I'd like to introduce Erin. I think, maybe Aaron's been here a few times, but hasn't spoken yet. So this is my colleague Erin. Pleased to meet you, everybody. Here's Erin.
Aaron Marten (Microsoft) 00:14:39 everyone.
Yeah, so I published this, proposal a couple days ago. I saw Laurent had left a few comments, which I've replied to and incorporated in there.
So I, you know, would love to get any other feedback that folks have. It's a pretty, you know, lengthy Issue, so, might be best for offline. But we can certainly go through it, at least briefly here,
Joshua MacDonald 00:15:05 Yeah.
Aaron Marten (Microsoft) 00:15:06 Overview, maybe.
Joshua MacDonald 00:15:07 I've got it shared up now, if you'd like to just talk. I think everyone here is curious to hear a little bit more detail.
Aaron Marten (Microsoft) 00:15:13 Sure.
Yeah, so, this is something we've been, Thinking about and talking about a little bit, So, the main idea is, with OTAP specifically, we've already got the records in Arrow format.
So writing out records to disk as Arrow IPC is fairly cheap.
Additionally, we have the nice benefit, on the other side that, you know, Arrow IPC files are, can be just memory mapped back in, and we don't pay a serialization cost.
Right? So, we avoid that, you know, when you're… especially when you're talking about high volume.
telemetry flowing through, right? That can be very expensive if you're serializing to some kind of format and then deserializing.
When you're going to and from disk. So, the idea here was, okay, we need a… if we need a persistent story to handle You know, Offline periods, crashes, those kinds of things.
we could use this for that. We could leverage our IPC. And so Quiver, is… is a proposal for doing that.
So I want to be super clear about… about two things.
Number one, Quiver, the idea is we would build it as its own standalone crate that OSAP Dataflow would take a dependency on.
And so, we do have… a desire for some other projects that we've got going on, to use this in those as well. So, we'd like to keep it as a separate crate if possible, because that way you know, other projects could potentially leverage in the future. Obviously, though, we will focus up front on making sure OTEP data flow works very well with it, as a, you know, big first hero customer.
And second point is it doesn't exist yet. We've kind of, like, I've done a couple, like, proof-of-concept prototype-y kinds of things, but I wouldn't consider those, like, exactly this.
And so we… we are going to need to kind of build this as we go. Build the core library itself as we go.
Okay.
So with that said, The proposal… the issue is meant to be, pretty, you know, fairly high level. There's obviously a lot of, you know, implementation details underneath that are just simply not specified here, but that will need to be defined as we go along.
But it was more to kind of give the overall picture of generally how things are going to work.
So the idea is… Batches come in, in the context of OTAP Dataflow, since it's… we're doing bread per core, and we want to avoid synchronization between cores. The idea is every core is going to have its own Storage area that it writes to… writes to and reads from.
So there shouldn't be any… at least up front, we're not planning on any kind of synchronization.
There's one or two cases where we may need to do that, further down, but let's get to that.
So data comes in.
The whole idea is we want to get it written out to disk as soon as possible.
So that then we can act to an upstream producer to say, Data is safe.
You don't need to worry about… we're not gonna drop it. It's on disk. If we crash, we'll be able to retain it.
So the, you know, the way you do that is you have a write-ahead log.
So that's the main purpose of the write-ahead log, is we take the batches, we append them onto the write-ahead log.
Let me move on Okay. Over time.
We will, accumulate these batches in both the write-ahead log And an in-memory, what's called here the open segment buffer.
And the idea there is that The write-ahead log is mainly for, like, you know, crash recovery.
But we want to reduce the number of actual, like, rights to disk for the Aero IPC files, and we do need to do some batching of data.
And so that's the purpose of the, the open segment buffer.
So we accumulate some of these incoming record batches, which may be very small, until they reach a certain size, or if at a certain time.
And at that point, they get written out to disk. They get finalized.
Ready with me so far?
Cool.
Okay.
So, we write out a segment file and some metadata, and then the… The main, kind of, way these are consumed is with notification messages.
So we'll… at that point, once a segment is finalized, it is now available We're downstream consumers.
And so, notifications get sent out, there will… we will… Sorry, I'm just looking at the proposal here, where I want to go with the conversation. Okay.
Joshua MacDonald 00:20:41 Can I… I just sort of, like, interject. It sounds like, the… the right-hand log, the open segment buffer we've talked about, we're starting to talk about X and X, or, you know, notifications. I know there's some tricky stuff about how to delete ever to delete anything. It sounds like that you were… that's where you were heading.
So… I… I didn't want… I didn't want to, like, steal your… your, spotlight here on… on the right… the right-hand log or the PubSub notifications. I just know that… that we're… we're getting a little bit lower into the details. Did anybody else have questions they may want to ask you, or anything like that?
Albert Lockett 00:21:24 I had a… I had a question. So, would… and sorry if I screw up the, the terminology here, but would we have, Like, like, write-ahead logs.
Or segment files, like, per, per… payload type, because, like, our OTAP batches, they're made up of multiple, Multiple record batches, essentially, like, multiple, you, like… I guess, like, multiple record batches, right? So, like, logs would be its own record batch with its own schema, and then log attributes would be its own record batch with its own schema. So, if we were to, just, like.
serialize these as, like, a… as a straight-up, like, IPC, file, like, those record batches are different schemas, and so that… I don't know if that would, like, work. So, do we, do we need to keep, Different, like.
files and different buffers, like, per, per payload type, or does this, like, does the format we're using Kind of, like, abstract around that, and we can store multiple record badges with different schemas in, like, the same In the same buffers, or the same files.
And if you don't have an answer to it right now, it's okay, I just wanted to, like, to call it out as, like, maybe something that we'd need a solution for.
Joshua MacDonald 00:23:00 Yeah, so let me see if I understood. So, I like to think about logs in the OTAP because it's the simple… the simple signal, so it has four tables, resources, scopes, attributes, and logs. And I think what you've… what you've said is that those four record batches As we accumulate them.
Certainly have different schemas from each other. Well, actually, maybe not. The resources, scopes, and logged attributes all have the same schemas, maybe. And then the… it's the logs table that has a potential to have, different schema. Of course.
even within a sequence of batches, you can find columns that have been added or not, and so on. So you have Laurent, hello.
So… so I think, Albert, you were pointing to the kind of… Much like with your issue that you described earlier, it's, like, a little bit harder to deal with multiple record batches in the same Payload in the same… query, etc.
Aaron, do you have any, thoughts on this topic, or a question?
Albert Lockett 00:24:12 Oh, Aaron, we can see you talking, but we can't hear you.
Joshua MacDonald 00:24:16 Oh, yeah.
And you're not muted. Oh, now you're muted. No, you're not.
Albert Lockett 00:24:24 Toss.
Joshua MacDonald 00:24:24 I can't hear you, Aaron.
Of course, in the OTEP stream protocol, we, serialize multiple batches from multiple IPC readers, writers.
Into one stream.
I take it that won't work.
You back yet, Aaron? There we are.
Aaron Marten (Microsoft) 00:24:50 Great, okay, I don't know, my audio clips out.
Yeah, so, I mean, generally speaking, when we're working with Arrow, right, like, the schema is very important, and so there's… we would need to keep, Different schemas separated.
Joshua MacDonald 00:25:09 And I think that's probably the easy answer to Albert's question, is essentially to say, we have four schemas for the logs, we're gonna have 4 separate, like, low-level quiver arrows. Low-level IPC log files. So you might get four IPC log files with the four record batches of a log stream.
And there's still… there's still gonna be… there will still be schema variation, I suppose, you know, as one log record may have the dropped attributes count, and one won't, and now you've got an optional column or something like that.
But I'm imagining those can be addressed by one IPC log per… per… or OTAP record.
Laurent Querel 00:25:49 type. I want a catalyst.
So, so, multiple, feedback to that. Hi, guys. So, first.
you will observe the difference of schema everywhere. Everything in the resource attribute, scope attribute, and attribute or logs is quite common.
Just because if you have attributes that are all swinging, and just suddenly they are, Of inType, you will, you will see a new schema arriving.
That's when… one aspect.
So it's common. We need to address that very quick, very well.
The second part is… It's not on… what we have to put into this queue system.
I didn't think about it during the review of the… a very nice document that you created, Aaron, but In fact, we need to also to think about the state of this, protocol. It's a stateful protocol.
If we want to be able to replay it.
We need to keep track on dictionaries and, anything like that.
And in the protocol, we… we also have… For the dictionaries, I think we… yeah, I need… Sorry, I'm trying to… to… to make sure that I'm not, saying things that are just, Not the reality.
Because we, we… when we get in memory, a set of Apache RO records.
when those Apachello records have columns that are, dictionary encoded.
They have a reference to the corresponding dictionary.
So now, when you will stylize… not serialize, but put them into a file.
In, in, into the, the IPC format.
First, usually, you have to store the schema, then… I mean, it's basically what we do in the protocol itself.
We send first the schema, then we send, sometimes, when it's required, dictionaries, and then we send the values batches.
And then maybe we send a delta dictionary at some point, and so on.
So the… I think we have a similar… if I'm wrong, let me know, but I think we have a similar, type of problem to… to solve for the… the… the queue system.
Joshua MacDonald 00:28:58 Let me ask my own question, then. I… isn't it the case that the Arrow IPC writer sort of abstracts all the details you just mentioned, like the creation of that state and the dictionaries that are managed?
Through the writer.
Laurent Querel 00:29:12 Yes.
Albert Lockett 00:29:14 It does, but you can't, one thing I would add, though, is, like, for the IPC streaming protocol, like, what happens is the schema gets sent first, and then, like, the record batches, plus the dictionaries and the dictionary deltas, if there are deltas, but, like, with that streaming protocol, at least, like, you can't, between record batches, like, change the schema. Like, the IPC… writer and the reader effectively would expect, like, the schema to come first, then it would say, oh, I'm gonna keep reusing the same schema over and over and over again. So that's why if the… the schema changes, like, in OTAP, we create, like, a new… IPC Streamwriter, and then we… That's why we send the schema as part of the batch payload, so we know when to create a new reader on the other side.
But, I mean.
Laurent Querel 00:30:07 And this concept of stream, like you mentioned, Albert, we have two reasons to have a new stream.
The one reason is because we have a new schema.
But the second reason is because we want to favor our load balancing.
And then we stop explicitly.
A stream, just to, to, to let, the, the load, be redistributed.
In… in front of… The, the system that, where, where the… The hourly gods are sent.
So, an HTTP tool load balancer will be able to, reroute the corresponding, HTTP to… session, or stream.
To a different destination, potentially, if, if this balancer exists, and if there are enough, pipeline engine, via this load balancer. So… we need to investigate and understand exactly how that plays with Quiver.
Because for Quiver, when you have those AC mechanisms in place, You have a mechanism to… To basically track, based on the set of consumers that you have, how many, AC we received, and when we, we, we reached zero, then we can be sure that we can remove that. That we can remove the corresponding, batches. That's true, but what is not super… I mean, I think not defined at all into the specification is what about the state corresponding to the stream? That is an entity that is not represented into Quiver.
That also has its importance. Like, like, schema, and dictionary, and build a dictionaries, and so on. And how we clean up those states.
When there is no longer any… Consumer of this corresponding string.
Albert Lockett 00:32:25 The other thing I'd throw out is, like, I think it… it might reduce some complexity, but also add some overhead. If we serialized everything with the Arrow IPC file, protocol, right? Because in that… in that world, everything… every batch gets serialized with its schema.
And no delta dictionaries. So you're… the amount of data that you write and the amount of data that you need to consume is… is more, but, there's no state that you need to necessarily keep between.
Laurent Querel 00:32:59 Yeah. That could be under tentative.
Joshua MacDonald 00:33:05 I think I've become confused.
maybe, Laurent and Albert, you could explain a little bit more about what you're… So let me see if I got it, part of it. So.
A stream of OTAP data, if we want each record to be self-contained, has a lot of repetition.
in a ideal streaming file store, I think what you're saying is that we would have some sort of statefulness That's encoded in the sequence of records in that stream.
And Arrow IPC is not giving us this.
Directly.
So we might have to invent it. Now, I know Aaron came in, sort of.
sort of disclaimer at the front that he wants to have a library that's essentially reusable in potentially different environments, where we might have different Arrow sort of realities, and I, But the way I was thinking about it, sort of maybe naively at the start, was, well, here we are trying to persist frames of arrow.
We've got record batches, we have 4 of them per logs.
Payload.
Or whatever. And we're just, you know, like, we are an application with 4 record batches per logs, 8 record batches per span, whatever. Like, you could make a generic library that deals with sets of record batches, but now we're getting down to the details and seeing as maybe not so obviously easy, because schemas change, and then we need to have Statefulness, or good compression.
Is that, roughly speaking, what we just covered?
Albert Lockett 00:34:50 Yes.
Sorry, I was trying to find the, the schema, the arrow IPC schema specification that I could… similar.
Joshua MacDonald 00:35:00 I'm gonna unshare you guys. Let's see what you've got.
Albert Lockett 00:35:04 Sorry, I'm trying… I'm having trouble trying to find it, so, let me answer your question first. I think, I think what we're saying is, like, so, the idea in Quiver, right, is we're going to, we're going to serialize Each batch as it… as it comes in.
And, if we… I think what I, like, what I was trying to call out, at least, is, like, if we were to try to serialize each batch using the arrow.
IPC, streaming format, then there's one… there's some state that you need to keep in the reader as you read subsequent batches, because, there's a schema that comes first, and then each batch, and each batch might have delta dictionaries and so on.
If we were to use the Arrow file IPC format, as far as I know, each batch gets serialized with its schema, and there's no delta dictionary, so there's no state. So, as you're reading a batch out of, off of… wherever they're stored, in Quiver, I guess, from the file that's stored on disk.
Then you wouldn't need to have, like, a stateful, like, reader, necessarily. You could just say, hey, read the next… the next chunk of data, it's in the file IPC format, so I read the schema, I read the file, and then I just have it, and I don't need to kind of, like, having juggling of readers and… or stream readers in their state as I'm reading data.
Out of… Out of quiver.
So the, the, the, the… The overhead comes in, where in the streaming IPC, format, there's no… there's not, like, a schema per batch, there's a schema, like, per stream, and you can have delta dictionaries, but in the… in the file IPC format, you read the schema per batch, and so that… there's, like, an extra little bit of overhead there.
Laurent Querel 00:37:11 Yeah, yeah, just to summarize, I think the two options are either you basically record what is coming on the network, on the network.
So, you have this… you will have on disks this, concept of streams, with the… The schema, and the dictionary, and the different recaps.
And you have to create some kind of bookkeeping To manage, to determine when the corresponding stream information stored on this is, deleteable or not.
It will depend on how much records have been hacked by all the consumers.
And on the other side, like, with the IPC file.
You also have, in fact, in my opinion, to have some bookkeeping, because I think, in the IPC format, you have one schema, one… and a set of dictionaries, no delta dictionaries, but I think you could have multiple our records.
And we could imagine that we consume them, one after the other.
They are… I don't think that they are magically combined, together.
So you still have a need for… For some kind of, oh, there is the beta dictionary?
Joshua MacDonald 00:38:36 Yeah, so I… I was gonna say, I have conceptually thought of Aero IPC as the same thing.
Stream or file.
Laurent Querel 00:38:43 See, yeah.
Joshua MacDonald 00:38:44 And the file is just a stream with a footer.
Laurent Querel 00:38:47 Yes. Yep.
Makes sense.
Joshua MacDonald 00:38:49 So… maybe I'm confused.
Laurent Querel 00:38:53 Ugh.
Aaron Marten (Microsoft) 00:38:55 Yeah, the intent… the intention… my intention was that we use the file format, not the streaming format.
Albert Lockett 00:39:00 Okay.
Jake Dern 00:39:03 Yeah, I think they write all the deltas, in order, like, in the footer, somewhere.
Joshua MacDonald 00:39:11 They're not interleaved the way this stream document says.
Laurent Querel 00:39:16 Okay, so that doesn't change… I mean, it looks like it's very close, but each of those solutions are… Very close, if they are not exactly similar.
More or less. But that means that the bookkeeping that, needs to be done In order to… To delete the segment.
I'm using the terminology used into the spec.
a segment will be basically an IPC file.
In order to determine when to delete it, you have to do some bookkeeping on the internal Record batch.
And you have to keep the states represented by the schema and the dictionaries, as long as this entire file has not been acknowledged.
entirely acknowledge.
Joshua MacDonald 00:40:22 I thought we were… thought the topic started with Albert's question, was… was about… Okay, let me, My mental model for… Arrow IPC.
and for OTAP is that record batches are self-contained. So, you have an OTAP frame, it has no dependencies on other data. You have an Arrow IPC stream.
Payload, it's depending on the stream state, but as soon as you read it, you now have self-contained data that is independent of Everything else.
The topic I believe we're discussing is that when you arrive with a batch of OTAP, whether it came from OTLP or a stream or anywhere, It will have been, are we talking about, like, bypassing the construction of OTAP records and taking this, like.
payload that came off the wire somehow, and, like, mapping it straight into a log file, because I didn't think that was what we were talking about. I thought we were talking about You would receive the OTAP record batches, you would put them into the IPC writer, and then you would be done.
Why is this more hard than I thought it would be?
Laurent Querel 00:41:37 I think, what's, No, I mean, it's fundamentally… so, if you think about the… let's take Bunda Stream.
A stream will have a schema and a set of dictionaries, and when we receive new records, we update the existing dictionary. When we emit in memory, the OTAP batch.
In fact, behind the scenes, those auto batch have art preferences.
to the corresponding schema and dictionaries. If a stream is, close, on the receiver side.
the arc decreased, but the values arc decreased for the schema and so on, but they are not zero, because they are still in flights, they are still OTAP batches in flights, and transparently, it works well.
Now, when you have a file, the real question here is how we mimic this kind of thing.
Aaron Marten (Microsoft) 00:42:42 How, we are sure that.
Laurent Querel 00:42:45 a segment file.
Joshua MacDonald 00:42:47 Could be deleted.
Laurent Querel 00:42:49 Because nothing guaranteed that, Let's say, for some reason, just partially a segment has been consumed and acknowledged.
We restart the process.
And then we have to go back.
We have to make sure that we are able to recreate the corresponding state for this solo stream.
That is on disk.
In order to generate the correct, set of OTAB batches With the correct dictionary and the correct schema.
So that… I mean, it's fundamentally similar, but it's, the mechanic that we have to put in place is not as straightforward as… we could imagine. We… we have. In fact, this concept of stream.
If we mimic exactly what we have in the protocol, the concept of stream has to be To be managed in some way.
We could imagine… a solution where… but, like, I think that's something that, for example, Albert had to put in place for some, for the Parquette exporter.
We could imagine that we do some transformation of schema to make them a little bit more regular.
But in fact, that will not serve the real problem.
So, I don't think it's… it's really interesting to add this override to… To normalize the schema, because anyway, you still have to deal with dictionaries.
And that is entirely dynamic. And you can't imagine To have a single dictionary, because this dictionary could be fundamentally infinite.
when you have many, many streams over the time, we could imagine a situation where the dictionary increases, increase, increase, increase, increase, and it's unbunded, which is not great. So, that's why we also have this concept of streams that have a lifetime into the protocol.
Because fundamentally, that gives us a way to make sure that everything is bonded.
Especially the dictionary.
And that has to be also… in my opinion, addressed the same way for this quiver, infrastructure.
Making sure that we keep track of what needs to be deleted, and once we have that, then we… and combined with the fact that we have those concepts of streams that define a maximum duration for To keep track of the dictionary, data dictionaries, and schemas.
When you combine all of that, that gives us nice properties, like, okay, we are sure that the system will not grow infinitely.
Joshua MacDonald 00:45:43 Alright, I think I understand now.
More about this.
I would have assumed that each segment has its own state, so you're gonna read the one arrow IPC log file segment, and… and any dictionaries will be… Within that state session, so that… I would… I was naively assuming that the logic that Aaron Ruff sort of sketched in the issue would handle this, you know? Like, once that segment's ready to be deleted, like, all of its data can be deleted.
Laurent Querel 00:46:17 What you're describing, Joshua, is feasible, but will add a lot of overhead, because basically, for every batch, you will… you will, you will generate the dictionary, in fact, you will… let's say, install shit, or the… you will.
Joshua MacDonald 00:46:35 But, I was meaning… segment. Like, you, you know.
Laurent Querel 00:46:39 Yeah, for every segment, yes. Yeah, but Yeah, we could have an intermediary step, indeed. Having multiple record batch, representing multiple OTAP batches.
Where the dictionary is… Fully, fully created and concrete per segment.
Even if this segment… but in fact, the segment could be represented as… The concept of, sorry if it's not clear, but the concept of stream that we have, on the receiver side of the protocol part.
Could be bigger than the segment, or smaller than the segment, depending on the configuration of these two things.
Joshua MacDonald 00:47:32 There was a moment in the evolution of this project, I would say 8 months ago or so, when we picked up Phase 2, and I was finally learning the details of the OTAP representation, where I had survived most of Phase 1 without really getting to know every single detail. And I had an aha moment where I was very pleased to understand that there were literally no dependencies, like, between frame to frame. Like, you have your… once you've read the frame from Arrow IPC, it is now… somehow self-contained. But now I see the thing, is it's depending on our dictionary, that some sit on a hidden state.
But I guess I… it doesn't sound like a terrible design to just, for each segment you're writing into, write an arrow IPC file. There will be delta dictionaries and so on that are still self-contained, but they'll be self-contained within one Segment, not within one record.
Or one batch.
But now I see. The topic has come back to me, and it's not as simple as I thought it was.
Aaron, this started with you. I want to turn it back to you, because I got a little bit lost, and we all might be lost here, but I want to make sure we have a step forward, or at least know what to talk about, or… How to resolve this type of conversation.
Aaron Marten (Microsoft) 00:48:59 Sure, yeah, I think I… I don't have as much kind of experience working with the OTAF-specific format, so I think maybe some of the details of that conversation will be lost on… were lost on me, and I'll have to go review it, but we can… We can definitely work through this.
And keep discussing it more offline.
Joshua MacDonald 00:49:18 Yeah, I think another conversation, maybe you and I get together and see if we understand what we understand.
Because I do know some of the details, like.
when we think about the OTAP stream, which might be very long-lived, we… we've… that streaming mechanism has a way to reset the schema and start again, which is like starting a whole new arrow IPC reader or writer.
We… if we ended up doing that, then we would just start new segments every time the schema changed.
And that might work. That might raise the questions from Albert and Laurent as well. But we can, I guess tackle that when we get there.
Laurent or Albert, do you have any, like, firm conclusions from this conversation? Like, oh, here's how I would do this, or something that we can use, or, you know, quickly?
Laurent Querel 00:50:10 No, I don't have that now, but I think, so first, I think it's definitively feasible. A little bit more complex than what is described into the spec.
And I think we… we should, spend the, the, the… I mean, the next days.
To, to complete the spec around this, this aspect, and, and having an open conversation, maybe directly into the GitHub issue, to, To analyze, and, and, and making some… We could imagine multiple, options, multiple approaches.
It would be nice if we can explore them into this little, Issue, and make some conclusion, maybe, for the next week.
Joshua MacDonald 00:50:56 Can I ask Albert one more thing, then? So… Laurent referred to the Parquet exporter, and I've seen the code that's in question. So, when we transition from Arrow to Parquet, we get real about schema.
Because there's no optionality. Once you've started writing a parquet, they have to follow that schema rigidly, and where, as we said in the OTAP stream, we just, like, have a way, because the gRPC protocol, with a higher level control plane, we can say, new stream. We just started… we just reset.
Is there a… do you see a sort of solution, or a, like, half-solution to this, where you follow the Parquet-exporter approach of, like.
Widening and kind of pessimizing the schema a bit.
Albert Lockett 00:51:44 Yeah, so the… the Parquet… I think, like, the… the trick… with this quiver thing, is I think we'd probably want to get back the original, record batch when we, like, read it back. So the thing that the Parquet exporter does is it, it… expects, all, like, the number of columns to be the same, and all the columns to be in the same order when you write Parquet. So what we do is, like, if, like, one record batch comes, and then another record batch comes after, and it is… has added, like, a column or, you know.
maybe, like, that the column is, like, optional in OTAP. What we do before we write Parquet is we, We, like, normalize the schema, which means that, like, we know what all the columns should be for that payload type, and we, and we put in placeholders for all the columns that are missing, and we also rearrange the order of the columns so they're in the same order. What Parquet… interesting thing about Parquet, what it allows us to do, though, is if the data type changes, so for example, if, like, the dictionary if, like, let's say some column is, like, dict keyed by U8, and then all of a sudden we get another record batch that's, like, dict keyed by U16, or is, like, the native type, the Parquet exporter will actually just, like, or the Parquet writer, will just accept those. So that's… so, like, the type changing isn't something we need to worry about, it's the, it's more like, what are the columns and what is their order?
But that said, when you… then when you go read it back.
you, you run into this, into this issue where, like, if, like, you were to read it with DataFusion, say, like, hey, select star from blogs, right? You get back a bunch of columns that might not have been in your original, in your original record batch, and so, like.
I don't know if, like, we would necessarily want to, like, do that same thing.
Because, because, like, when you end up reading the batch out of Quiver to send it downstream, you would end up with, like, extra columns that weren't in the original batch because, because they were either all null or all default value.
And then you just end up, like, having, like, an extra column in memory that, that you… That you don't need.
Joshua MacDonald 00:54:11 I imagine there could be an optimization step where you… Remove those empty or all null columns.
Albert Lockett 00:54:18 We… yeah, we could… we could do that, too. We could do that, too.
Yeah, we could do that too.
Joshua MacDonald 00:54:27 If we were to follow this… arcade approach. It sounds like the segment, if you buffer the whole segment, and that was the design that we saw, is you'll have in-memory builders for the open segments. Then you can know the whole schema if the segment is, like, small enough to, like.
Seal it in memory before you write some of it.
Sounds like that would be feasible.
But then it's the right-ahead log where we have this variation that maybe is… is problematic, and maybe that's a bad place to be using arrows, kind of what I'm hearing.
Albert Lockett 00:55:01 I don't think it's… necessarily… a bad… Okay. There's arrows.
Joshua MacDonald 00:55:10 Just tricky.
Albert Lockett 00:55:12 Yeah, there's just some, some, some, some edge cases we need to under… understand around, like, what do we do when the schema changes?
Joshua MacDonald 00:55:23 Yeah.
Albert Lockett 00:55:23 What do you say?
Joshua MacDonald 00:55:25 And it sounds like, Laurent, you were hinting at something that's like, well, there's incoming stream state.
If we were able to put that incoming stream state somehow into the write-ahead log, then maybe things would be better. I'm gonna stop sharing half-baked ideas now.
Laurent Querel 00:55:39 Yeah, I mean, the IPC streaming format that you have on the screen is fundamentally, stateful. You can't interpret the step 4 without having interpreting all the previous steps.
So that's something that we need to… And the benefits of that is you don't repeat yourself. That's why our IPC stream format is efficient. And if we want to keep this efficiency, then the scheme, I think, has to… in some way, to mimic that.
I was thinking on the previous discussion, on the Parquet file, there are some… exploration that we, we discussed with, with Albert, a few weeks ago, because between the time when OTAP has been designed, and now, some… How encoding has been introduced.
We could imagine that, we… The fact that the schemas are dynamic was there to Optimize the, the, the, the in-memory representation, mostly.
that's why we have these, dynamic schemas. So if you take attribute, the attribute record, we will eliminate… get rid of the set of, columns.
Because they are not used at all into your batch.
And that… that will be, highly beneficial, because If you keep them even an empty column.
Not on the wire, because on the wire, when it's compressed, it's basically zero.
But in memory, the… in the previous iter… in the old days of our, it was taking… some… some memory. It was far from zero cost in that case.
Now there are some encoding options.
if I'm not, making mistakes, they could be negligible. So a column that is In fact, entirely null , because there is no data at all.
Will be able in memory, close to zero.
I think, and then that could, give us some additional options to simplify some part of the design, like, be independent of the presence or not of columns. We could imagine that, okay, we always have the same schema, which we've seen Wait.
Joshua MacDonald 00:58:26 What would you call these new encodings?
Albert Lockett 00:58:29 They're, it's called run arrays, or run-end encoding.
Laurent Querel 00:58:32 Yeah.
Joshua MacDonald 00:58:34 I thought you were gonna say something about sparse unions. I know that was something you experimented with.
Laurent Querel 00:58:39 Yeah, but that's not exactly that, yeah.
Joshua MacDonald 00:58:40 Got it. There are 2 minutes or less in the hour here, and I wanted to, close us off. I have… I have a topic that's pending here, and what I want to say is, let's talk about this in two weeks, because I… because we have the people I want to talk to, which are not the people who've been speaking today, here, who have been listening. And the topic I want to bring up is sort of, like, what's… what's… what's the next 6 or 12 months going to look like for this project? Because this project started with a 6-month plan.
6 months ago, and we've reached the end of it, and we've done everything we said we'd do. We've experimented with data fusion, we've shown the performance of a REST pipeline, we've really gotten to know OTAP.
I believe, in Arrow. I think we're… I think there's a little bit more performance studies that we haven't quite finished and I think there's a few issues with the code before we can release it, but I want to talk about what's Phase 3.
What is… you know, this started out as an experiment. I feel very confident that we've validated our beliefs and our proposals. This is looking good, feeling good. But what is Phase 3 of OTL Arrow? That's the question I want you all to think about.
I'm especially looking at the visitors, especially Pablo, especially Matias, since you have, like, a lot of you know, involvement in vendor space here. I just want to ask you all to think about what you hope to see us say about the future. You know, what are the blockers, what are the advertisements, and so on. That's something for next time.
Laurent Querel 01:00:08 efficiency.
Joshua MacDonald 01:00:08 And… I think we're out of time. If anyone else wants to speak, I'm listening. The floor is open.
3, 2, 1. Okay, well, I gave you a prompt for next time. I hope you, have some thoughts for me then. I appreciate this conversation. I definitely think we have more work to do on understanding it. Aaron, I'll get back to you. Maybe we can brainstorm and try and unpack everything Albert and Laurent just said.
Sweet.
Laurent Querel 01:00:41 Thank you all.
Joshua MacDonald 01:00:42 Have a great day.
Laurent Querel 01:00:44 Yep.
Aaron Marten (Microsoft) 01:00:44 brink.
Pablo Baeyens 01:00:44 Thank you.
Danny Chin 01:00:45 Thank you.
Pablo Baeyens 01:00:45 two weeks.
Joshua MacDonald 01:00:49 Alright, where's my screen control?
