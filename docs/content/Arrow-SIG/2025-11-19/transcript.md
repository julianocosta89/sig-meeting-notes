SIG: Arrow SIG
Date: 2025-11-19
Duration: 62 minutes
============================================================

## Zoom Recording Transcript

Albert Lockett 00:00:24 Because…
Aaron Marten 00:00:29 Blue.
Danny Chin 00:00:30 Hi. Hello.
Albert Lockett 00:01:10 Were you guys, affected by the GitHub outage today?
Danny Chin 00:01:21 I… I mean, out there… GitHub.
Albert Lockett 00:01:32 Josh?
Aaron Marten 00:01:35 It was amazing not being able to push for a little while.
Joshua MacDonald 00:01:45 Okay, everybody, I'm gonna put the meeting notes in the channel, and then invite you all to enter your names, or perhaps agenda items.
Here we go… And I'd be glad to… Share my screen.
Alright.
So, as this meeting becomes more and more popular, we should do this practice of writing our names and so on, so we know who was here and what was discussed. We've been starting to have a good practice of going through the issue, triage, the new issues for the last week, so I'll start us there. And… Then we can go on to any agenda items that you all place in the meeting notes.
I also would like to do a little round of introductions, since there aren't too many people here. Let's see… I do see, I believe, a new member who has not joined us necessarily much in the past. Oh, let's see… Kennedy, I believe this might be your first time here. Would anyone like to say hello, or greet the group?
Kennedy Bushnell 00:03:20 Hi, is my audio working?
Joshua MacDonald 00:03:23 Cool. Hi, Kennedy.
Kennedy Bushnell 00:03:25 Yes, my name's Kennedy Bushnell.
I, I work… With Aaron and Josh at Microsoft.
We're starting to get involved in this project, so wanted to… Join and… See how this goes.
Laurent Querel 00:03:41 Nice, welcome.
Kennedy Bushnell 00:03:43 Thank you.
Joshua MacDonald 00:03:44 Thanks, alright, so, as far as the, new item agenda, the new issue triage… I flipped over to the PR's list, but I want to bring us back to the issues.
So, it looks like we have a few. Drew filed one, I filed one, and Albert filed one. So, I'll start in the chronological order they arrived. Drew filed one, since I don't see him, I'll summarize it myself.
We have an application here for syslog, and if you know what CEF is, it's a format that is layered within Syslog.
One of the practices that we have here is to map that data into a Microsoft schema that's very well defined and fixed. So we have this long list of fields, we want to map them. And the issue here, which I'll click into.
Is that… we want to be able to take all the items that don't match this list of keywords that we have, and lump them into one attribute. So, the issue here by Drew shows, basically, the motivation. I would like to, since I speak in Prometheus terms a lot within OpenTelemetry, I would like to call out at least this connection with Prometheus. If you've looked at the Prometheus configuration for relabeling, it does have this case called LabelMap, which is something that does Quite similar stuff is what we're doing here, or what we're requesting here, which is to take a bunch of labels that you may not have specific information about and throw them into another label.
a single label, that is, and it reduces and controls cardinality. So, Albert, it looks like you gave some useful feedback. I know, Drew was excited to read it, and then Utkarsh has also read up on this issue. Could I ask Utkarsh, or Albert to speak?
Albert Lockett 00:05:44 Yeah, I'll speak first, because I gave my… I guess we'll go into chronological order with the comments. Yeah, so I was, I didn't really come to a conclusion here, but I guess I was just trying to, like, give Drew some, some guidance on whether this makes sense to do in the syslog receiver, or whether it makes sense to do in the attribute processor. And so, my thinking is.
If we do it in the syslog receiver, it's probably gonna be better performance, because we… we don't end up materializing all these extra attributes in the attribute processor, and then having to then go modify it after the fact. We can just build that, condensed attribute one time. Now, that said, there's, you know, there's a… there's a few problems with doing that, right? Number one is if you actually want to do some post-processing on those attributes after the fact, then you're going to need to uncondense them, otherwise you could just do it in the regular attribute process, right? So it depends what you want to do.
The second thing is, if you were to transmit this condensed attribute, you do lose some of the benefits of dictionary encoding, because, essentially what we do with our attribute arrays is we dictionary encode them, right? So every value is only in memory once, and then it's only transmit, and the buffer that we… transmit once, but with this condensed thing, every unique combination of key and value is going to be there, right? So, depends on the use case. If you need to condense it anyway before transmitting, it's not really, you know, something that's important, but… If you want to defer that and get, you know, the dictionary encoding in some kind of… in transit, then maybe that's something to think about.
And the last consideration I was trying to call out here was, like.
you know, if, like, if there's utility in doing this attribute condensing thing, like, outside of just syslog, then maybe that's another reason to do it in attribute processor, but, like, if the only use case we have is, like, for syslog, then, you know, maybe it makes sense to do it in the receiver. So, anyway, that was the feedback I gave Drew on this.
you know, where he and I kind of landed when we were chatting on Slack on Friday night was.
You know, we were kind of leaning towards doing it in the syslog receiver, but But, but, you know, interested to hear what the rest of the group has to say as well.
Utkarsh 00:08:20 Yeah, and I couldn't… Also, like, just, mention… what I think about this issue. So… The, condense operation seems… Very specific to be… put in the generic syslog Ceph receiver, you know, and to provide it as a config that's very, Again, yeah, I mean, it's not generic enough, I feel, to be put in the receiver. That's my main concern with it. And definitely, performance is gonna be… you'll get the most performance if it is done in the receiver.
I totally agree with that, but… Yeah, the… the component wouldn't seem generic enough. It's like a very… I would feel like it's force-fit if I offer a config where, like, there's a list of… give me a list of values which you don't want, and… Then give me a name that you want me to put them all in.
Yeah, and then that could open up doors for, like, other, I don't know, APM vendors then coming up with their own requirements, and then I think… We could have, like, a very… config explosion, in the syslog self-receiver later on, if we set this precedent. Like, renaming and simple rename filters, those things are, I think, common enough.
But this one, this particular condensed operation seems very specific.
yeah.
Laurent Querel 00:09:45 So, so I, I also read, I didn't comment at all, but, I was not aware of this, since… before this morning, so I… following a discussion with Joshua this morning, I… read it, so… I think the… we… first, we should to separate… we should separate the codons upon the renaming. That's two different, like you mentioned, I think with Karch and Albert, they are two very different, requirements. The cadence one.
We will question, if it's a real, requirement. Because if the goal at the end is to, To send the information somewhere.
we better have to keep the structure of those attributes as is, like Albert mentioned, to get a better compression ratio.
So I'd like to better understand exactly what is the… The need for condoms.
So that's why I think it's interesting to separate these two operations, because there is one that is clear for me, and the other one that… Is still super unclear.
And regarding the renaming, I think having it as a generic operation directly into the receiver could make sense.
I mean, this idea of normalizing A schema is generic enough to… To be very optimized.
You have that, we have that also at F5, and I'm… I'm guessing that it's a very, very, very common situation, so… Offering a very highly optimized solution in this specific, for this specific function makes sense for me.
Joshua MacDonald 00:11:36 Hey, Kennedy, what you got to say?
Kennedy Bushnell 00:11:40 Yeah, so I… I like that we think performance first, but have we seen any evidence that the more generic, like, attribute processor-based approach doesn't meet perf goals? Are we prematurely optimizing Should we start there, and then revisit?
Joshua MacDonald 00:12:01 I think that's a fair question.
I… it occurs to me… I'll just, add sort of a detail from my kind of perspective over in the GO collector sort of world. There's… once you… once you reach a point of having kind of a… good baseline coverage of all the features we need for the pipeline, then people start talking about extension interfaces, which is, like, you know, a special feature that you might want to be able to plug in one or another implementation of.
So, if I were to see something like we've talked about done, I would sort of expect to see it done like an extension, so that there might be an interface called Remapper.
And there's a remapper extension point, meaning it has, like, a trait, like, that you can call to do the various operations of, and then the way this works generally in the Go Collector is you'd have, the component configuration would have some sort of field to configure its extension or extensions.
So, for example, in middleware, you have a list of extensions, but in auth, you have one extension. And then there's a dynamic component lookup that happens to find an impulse of that particular trait, or whatever.
So that would be as we mature, if we really want this type of feature.
For performance, for example, to run some sort of standard logic inside a receiver.
like, whatever it may be, that's where I would go.
So, for now, it sounds like we have at least reached some conclusions. We should probably just go ahead without doing, the condensed operation, and if it becomes a performance issue, take a look at it later.
Just to be sure to understand the confusion, Joshua.
Laurent Querel 00:13:50 You are saying that… We are, doing the mapping on the receiver side, on the attribute processor, and we compare the two.
Or you are saying that we start first with the attribute processor, I'm not sure to understand the.
Joshua MacDonald 00:14:11 Yeah, I think it would help if we have Drew here. I mean, I think that there's two ways we could talk about this. One is, sure, it's a cardinality problem. It's like, at the end of the line, we don't want all of those columns in the database somewhere.
it's gonna cause us too much… it's gonna cause too many column groups, or whatever in the data set. So… As for whether OTEL Aero Performs the condense, or whether we do it somewhere later in the pipeline.
It's going to happen somewhere. And I think that Drew would probably say something like, we want this component because we want the data transformed, whether it's for performance or not.
Laurent Querel 00:14:54 Okay, okay, I understand for the condensed part, but for the filtering, what is the conclusion?
No, not the filtering, the renaming.
Joshua MacDonald 00:15:05 I didn't reach a conclusion. I think Albert's.
Laurent Querel 00:15:07 Oh, okay.
Joshua MacDonald 00:15:08 Really, to say and suggest that If the cost is because we're building another schema and generating a new vector of arrays and a bunch of reference counting work. If that's too expensive, then I think probably yes, we want to do it in the receiver to avoid two schemas.
But I would guess that's not the performance cost.
There we have.
Kennedy?
Kennedy Bushnell 00:15:36 Yeah, so… I would hope that we have, like, principles defined, or if not, we should probably get those defined around aspects like this, but… Any… anything that we put into the syslog receiver as a feature.
that's not inherently going to be accessible by another receiver, right? So something generic… well, what I would consider generic of, like, renaming and dropping columns seems like something that we should probably have a layer outside of the receiver, or at least accessible to all receivers. So we implement once, utilize everywhere.
Oh.
Laurent Querel 00:16:14 But that's the case. That's what we usually do.
I think the question here is… So we have this attribute processor, we have the filter processor, usually what we do when we act on data.
Daryl.
Combine into a processor to do whatever is… The generic transformation we want to apply.
It looks like, this, for this specific case.
And if I understand well, the Microsoft side is to optimize as much as possible the sea slug, scenario.
Because that's the one where you want to save the most of the money, so the… if the question is, how can we accelerate this process, I think the answer is… Okay, you can use the virtual processor and the filter processor to do that, but if you go even… more performance, the other option is to, to create maybe a dedicated T-stock receiver. That's the, The next step in optimization.
Joshua MacDonald 00:17:24 I guess the reason I took it… I helped Drew make this proposal, so I'm sort of now sort of trying to stand in for him. The reason I found this potentially appealing was because, and I think this is sort of repeating what Kennedy said, is this CEF format is a standard that does not only move through syslog. You can have Ceph moving over… other formats, and I don't know what those other formats are exactly, but you can end up with Ceph embedded in an OTEL field that's not from a syslog, let's suppose.
And if, in that case, you would want to have at least a library for sort of taking this string field and turning it into a bunch of key-value fields. So I guess there's also a split the Ceph Aspect of this.
I guess, Ukarsh, you… you can clarify this for us. We do split Ceph as an option from Syslog, and it probably is a reusable library.
Utkarsh 00:18:27 So in the current syslog set receiver implementation, We try to detect if the message contains SEF.
If it does, then we parse the… we do the CEF-based parsing.
So… It's not an opt-in right now. It's more like the receiver is dynamic enough to understand The legacy syslog format, the new syslog format.
pure CEF, raw Ceph, which is not in any syslog format, and a Ceph that happens to be in one of the two formats.
So, it does this detection, and then parses the fields accordingly.
Joshua MacDonald 00:19:10 All right, yeah.
I think we should call time on this issue. I know Drew will be able to listen to the recording, and we can talk about it more.
Utkarsh 00:19:19 I still wanted to, like, just ask one clarifying question here, so do we have any conclusion here, or, like… because I remember, Josh, you said.
that we don't want to do this, but I didn't… I didn't catch if you meant we don't want to do this in receiver, or attribute processor, or, like.
Joshua MacDonald 00:19:38 Oh, yeah, I don't think we want to do this in the receiver until we see a definite motivation to do so. If we did it, then I would want to figure out, is this just a one-off reusable library, or is it an extension, generally speaking, where you might plug in something else?
a different implementation, or… in other words, I'm not sure which one it'll be.
I'd like to hear what Drew thinks about it.
We still do want this transform, though, somehow.
Utkarsh 00:20:08 And another question, so if you're doing it in the processor, we then have two choices, either put it in attribute processor itself, or, like, have a different custom processor do this.
Joshua MacDonald 00:20:18 That's right, and we did not think this really belongs in the attribute processor, I think, is the starting point of the conversation.
Utkarsh 00:20:27 Okay.
Joshua MacDonald 00:20:29 And it will encounter this, memory issue that Albert raised as well, so I think it's worth asking whether it doesn't make sense to do this on a receiver somewhere, but it could be another OTel Arrow data flow, you know, like, receiver that has, the Ceph Condens… decondenser… condenser that we want.
again, as a custom component.
All right, well, I know.
Utkarsh 00:20:56 By the way, we have Drew on call now.
drewrelmas 00:20:59 I apologize for that, I just sent a message. I've joined late, I was… I had another internal call, only to find we're finished discussing my issue, so, I think we should move on for today, and I'll try and watch the recording.
Joshua MacDonald 00:21:12 Thank you, Joe.
All right, and please add your name to the list. I will get to adding my own name at some point.
So, let's see, we were looking at the issues list, we had 3 new ones, I think the next one was mine, and Unless anyone else here could speak better to it, I don't see the… it's hard to see the list while I'm talking and sharing.
So I'll just briefly summarize this one.
We have this, in my opinion, really coming together P data library, which is the protocol data manipulation layer for converting between OTLP and OTAP, or OTAP, and there are a number of ways that you can access data without copying it.
that we've built so far, and Albert led most of this. So, this views mechanism that we have is currently useful for, consuming either bytes of OTLP or message objects of OTLP. So we can use message objects and bytes, and we've been doing some upgrades of this and that over the… over time. And then on the opposite direction, when you have OTAP data, there is a view for, essentially, I'm coding myself now view, that's really a way to encode OTLP bytes, again, without copying them unnecessarily. Like, we're not building up proto-message objects in order to encode, we're just directly encoding OTAP.
And the thing that we want here now that I've just… that we've seen sort of two copies of is an exporter that's basically written for a row-oriented protocol, like an OTLP, except different. So it's a vendor-specific, row-oriented protocol, and it's been written based on the OTLP objects because we're in OpenTelemetry land. So, if you have one of these use cases, then you're going to want to write your library with these OTLP objects.
But we don't want to do an extra copy to get there. Currently, we are doing an extra Copy, decode, and re… re-parse that message into the objects that we know how to handle.
Which is obviously inefficient. So, I've filed the issue to describe what I'm talking about, which is a view backend for OTAP records, so that you can start with OTAP records, and then walk through it, just like you see OTLP objects, meaning one resource at a time for each resource, one scope at a time for each scope, one thing at a time, records of… log records, spans, etc.
And that is something that our team is really interested in, and, I asked Lalit to look into that for us.
Any topical questions on that topic for me?
Laurent Querel 00:23:54 So it looks very similar to what we already have with the BOTAP to a TLP autobyte representation, except that you won't Your own representation instead of the protobyte.
Joshua MacDonald 00:24:08 Right?
Right, so currently we have this code that, takes the OTAP records object and then produces bytes without copying intermediate.
Laurent Querel 00:24:20 Data. Yeah. But it's not…
Joshua MacDonald 00:24:23 I'm not able to use… much of that code would be almost reusable, I think, and this is probably where we're heading, but, like, instead of having it immediately write out podobytes, that it would have some sort of view… that it would implement the views that we've already, worked out, and I hope that that's feasible, and we are definitely interested in that, so that we can avoid extra copies for arbitrary protocols. I would assume that we could do, like, a JSON encoding this way as well, to kind of, like, walk through the OTLP and generate JSON, which probably one day we'll want to do.
As the, author of Views primarily, Albert, how do you feel about this?
Albert Lockett 00:25:07 Yeah, I think that, I think that should be totally doable.
Joshua MacDonald 00:25:11 Cool.
Albert Lockett 00:25:12 Yeah, it, that should definitely be doable. Great. No serious problems. Sweet.
Joshua MacDonald 00:25:23 All right, well, we can move on then. I know that, this one looks here, looks pretty simple. I mean, unless you have a topic here, Albert, we can just move past it, and I know that, Aaron is waiting to discuss this… Update. Erin, would you like me to click in, or would you like to control the screen?
Aaron Marten 00:25:41 You can go ahead and keep presenting, that's fine. I just wanted to highlight, thank you, to both Albert and Laurent for the comments and feedback so far.
I've been trying to incorporate, that into updates. And this, this document, just as a point of, kind of, like, workflow order, is getting a little bit unwieldy to manage as far as, like, revisions between it. I know you can go and look at the history, but I do… I am keeping a… I have a branch where I'm keeping you know, updates to this, so we can go back and look at that, or I can provide a pointer if necessary.
Okay. Anyway, I just wanted to highlight, so Albert brought up, he, you know, wrote out a lot of his concerns that he expressed in the call, last time, which was super helpful to go through, offline, and So the… I made some updates to the original proposal that, go with, kind of, what's described here in our first comment as the middle ground approach, which is The segment files, instead of being just pure Arrow IPC file format, would actually be kind of a wrapper around the Arrow IPC file format.
And the… the rationale for that is to allow us to have a single, kind of.
you know, OTAP, OTAP Arrow Records.
you know, collection. I don't know the exact term, but one of those things, the unit that you generally work with, of an OTAP record, keep that all in the same file, so that we're not splitting across a bunch of different files.
And so that way, you know, it's just gonna be a lot easier for Quiver to manage. It does also try to address the concerns about, or not even concerns, but just the point raised about, like, you know, these are only single schema.
Whereas in OTAP, it's common for there to be some variance when you're looking at a specific payload type, as you kind of go down. So, it tries to address that by, actually, probably the best place to look, to visually to kind of get the point across, if you scroll up, Josh, I… I created a diagram that… It'll be a lot easier to talk over.
Joshua MacDonald 00:28:03 Yeah, okay, fantastic.
Aaron Marten 00:28:04 Keep going up, no, keep going… there we go. Yeah, scroll up a little bit more.
So this is just an example of, like, you know, we may get a bunch of… I'm calling these record bundles. It's kind of a generic term, we can come up with another term. It's better, for the quiver layer, at least.
But the idea is you get, you know, a bunch of these things, so in this example, you can see we have, some of them have the scope attributes versus attributes missing. We also see the schema in… if you look at just the first two columns.
As you go from 0 to 1 to 2, that, you know, there's… there's variance in the schemas.
And so… If you then scroll down, you'll see how that would kind of get, represented in the segment file. So we'd essentially have a manifest at the beginning.
It would have pointers to these various offsets. And then we would have schema-specific streams, and each one of these individual streams is an Arrow APC file.
And the idea here is that we can still then, with one of these segment files, that is the manifest plus all these arrow IPC file streams.
We can memory map that whole file in.
And then we can still use the standard Arrow file reader.
to just read those IPC segments. And so we still get all the benefits of Of, you know, zero cost Deseralization and, you know, zero copy reads.
That Arrow provides us. We don't have to deviate, And come up with our own completely custom format.
Because this is really just intended to be kind of a wrapper.
Around that domain file format.
Laurent Querel 00:29:54 Looks nice. So the record bundles are more or less equivalent to Put that batch, in fact.
Because I know that batch is, in fact, a collection of RO records, That's, Need to be interpreted together.
So, yeah, I think the recall bundle is probably renamed into OTAP batch. And at the end of the day, what we get is segments that are very well aligned with the OTAP protocol by itself.
Which is fantastic, yeah.
Yeah, I think it's… it's great.
Joshua MacDonald 00:30:34 On that point, I have realized a point of confusion in the code, because what we're saying then is that there's an OTAP batch, which consists of four arrow batches, and so you see this variable called batches, and then you see a loop over the batches and get more batches out of them. It's like… I'm iterating over batches of batches, guys, and it's a little confusing, so I'm not sure batch is the right word.
After kind of experiencing that explosion.
Laurent Querel 00:31:03 Okay, but currently in the code, we are using OTAB Batch, right? The…
Joshua MacDonald 00:31:08 There's… yeah, okay, so there's the OTAP… Well, wait a second.
OTAP arrow, P data, OTAP arrow, OTAP… OTLP proto bytes, OTLP proto-message. I don't think we have batch… aero batch in that.
Laurent Querel 00:31:25 I think that's the… let me check, but I think that's the definition in the protograph file.
Albert Lockett 00:31:31 Batch.
Joshua MacDonald 00:31:32 Feral Records.
Laurent Querel 00:31:33 Yes, batch of records, yeah, it's not… yeah, batch of records.
Joshua MacDonald 00:31:37 Bar and Barkay.
Laurent Querel 00:31:38 Yeah, yeah, yeah. Okay.
I'm not against to the… to define.
Joshua MacDonald 00:31:44 But…
Laurent Querel 00:31:46 Or more, or less ambiguous names.
Joshua MacDonald 00:31:49 something we can work on. I've also noticed that we struggle to find exactly the right term for when it's an… OTAP records.
payload, that's the term I'm using in my head. OTAB records payload, that it has 4 tables, or 7 tables, or 17 tables, or whatever it is.
Which are also sort of, like, the relations of an OTAP frame, that's another word I use anyway. Those are just some of the ideas I have.
Alright, well, and so, I, I actually, I was, I was studying, Erin, the, diagram, which is under our… under my cursor now. And… and I… I think I got a little confused by this diagram right here.
The batch manifest is, at the end of a file, so this is sort of like, as we've invented a file full of interleaved IPC stream records. This is the equivalent of the footer, is that right?
Aaron Marten 00:32:53 Yeah, sort of. I mean, it's not… it's not like an arrow footer. It is… it is truly, you know, unique to our… our file format, but it's essentially this… I mean, it's the data you see, you know, represented here. It's just going to be kind of the mapping between You know, the tables, the record bundles above, and how that then maps into the the physical underlying streams in the file, right? So we can go back and find the original Record batches.
As they were… were ingested. So that when we're reading them spec out, we can… we can, you know, provide a quiver segment file reader that will that'd be Send those along to the next processor.
Albert Lockett 00:33:38 Would it… would it be, Sorry, I… I didn't… I didn't get a chance to, to read this before, but would it, like… Would your batch manifest and your, segment streams be… two separate files? Or would it be, like.
One file where you, like, you write out all the segment streams, and then you write the batch manifest at the end, and then you, like, close the file, and then that's… that's kind of it.
Aaron Marten 00:34:05 Yeah, that's all supposed to be in a single file.
Albert Lockett 00:34:08 Okay, okay, cool, gotcha.
Joshua MacDonald 00:34:14 Yeah, I think that might have been the point I was confused by. So I kind of imagine that one file contains first the segment streams, and then the manifest at the end, is that correct?
Aaron Marten 00:34:24 Yeah, I had a little kind of proof of concept that I didn't, didn't share, but, like, it has the benefits at the beginning, but I don't think beginning or end really makes much of a difference.
Joshua MacDonald 00:34:33 I see. Well, it might be actually easier at the beginning if we are assuming that these things stay in memory until they're written, then great, yeah.
Cool.
Are there any other questions in the audience that we'd, or curiosities, or other questions, or discussions about this?
Utkarsh 00:34:56 I had a question. I mean, I don't understand a lot of the Arrow… manipulation and even the requirements, but I'll just ask, so… You said it's… like… Different schemas are gonna be present in the same file, or, like… Like, let's say your log schema… In your example, that L1, A1, so are they all going to be in the same… same file?
And if yes, like, when you… have to delete… I have also heard, like, the files are immutable, so, like, how does that, like, do we wait for a lot of the records to be read before we can delete the file if they're all in the same?
But yeah, I do… I don't think I understand a lot of the things mentioned in the proposal due to my lack of Arrow IPC, and just Arrow knowledge in general.
Aaron Marten 00:35:45 Sure, yeah, so I'll just address the… address those briefly. Those are… I think those are answered pretty… pretty thoroughly in the existing doc, so if you just go through it, you'll find the answers, but just really quickly. So yeah, the new format that I'm proposing here It isn't just a single ROIPC file, because those only support, you know, you can only have a single schema, right? It's just basically schema, and then a list of the batches. So this is kind of a meta file that would sort of contain a bunch of you know, arrow IPC streams of various schemas, because like you said, logs, logs attributes, resource attributes, those are all going to be different.
Different schemas.
So, and then to the second question about… I think it was about when processing data and when we're done with these. I had mentioned in the initial proposal that I thought, like, oh yeah, we would do ACs on segments, so you get an ACK or a NAC.
on the segment from a subscriber, but I think it's actually on the bundle, not on the full segment, because we may have, in fact, by design, we would be probably batching up You know, a number of these bundles into a single segment file.
To reduce the total amount of I.O.
And so… The… I did make some updates in the proposal so that the ACT mechanism Which, you know, lets us determine when we can safely delete one of these segment files. The acts are per bundle, because that's actually the unit we're going to be working with.
Through the pipeline. So I updated that to be finer-grained.
Utkarsh 00:37:25 Thank you.
Joshua MacDonald 00:37:29 All right, well, I think, all of us should reread this proposal now that it's solidified, and thanks for all the detail, Aaron.
It looks good to me. I want to read it again, though.
And I'm sure that this detail is going to help us. So… Back to where we were. So that's… that definitely finished the issue triage. Oh, I wasn't doing a good job taking notes. And, I… if you ask me what to do next with this agenda, I would turn it to Laurent. I think we would like to talk about the GRPC implementation. Jokes about a thousand lines of code or less aside.
Laurent Querel 00:38:06 True.
Let me share my screen.
Joshua MacDonald 00:38:11 I will… I will… where's… Yes, I'm having trouble finding my controls, to be honest.
Laurent Querel 00:38:17 Yeah, that's happened.
Joshua MacDonald 00:38:18 I don't know where they went.
Laurent Querel 00:38:19 Sometimes to me.
Joshua MacDonald 00:38:22 Yeah, okay, well, you can steal it from me if you'd like. Where… where is it?
What if I kill the window that I'm sharing?
Aha, there it goes.
I'll do it.
Laurent Querel 00:38:34 Okay, sure… That's the one.
Yes, that's the one.
So, I was working on, experimental, receiver for OTLP and OTAP.
Combined together.
So that's the topic of this PR.
And, I'm trying to… to get the maximum of performance, because that's definitely the two most important, in addition to the syslog, obviously, but OTLP and OTAP receiver will be the most important receiver that we want to support, so optimizing them is definitely top priority.
So right now, the current situation, we already have a TAP and OTAP. They are both based on tonic.
Which is the… the most, I mean, known and used, gRPC implementation, client and server in the Rust ecosystem.
On the receiver side, there is one constraint that Tonic, Forced us to… to comply with, when you create a tonic-based gRPC server, you have to create features that need to be sent.
Which is not a requirement that we have into the engine.
But we support it.
That means that every feature that will, be used in this, VIPC-based server we'll have to use Arc, Mutex, and other things like that.
Which will be enforced, basically, by the compiler.
There is also a set of… so that's the first set of reasons why I was… Thinking or visiting this, this approach?
Be more aligned with the… The thread-per-core, nut sand approach that we use in the engine everywhere.
Except in these two receivers.
And that will give us, at least on the… Ideal world, better performance at the end.
The other, thing that I was looking for is, a better understanding on the value snubs, That exists correctly into the… the TCP, HTTP2, and GRPC layer.
when you combine all those, tonic is relying on Hyper, relying on H2, relying, obviously, on the the TCP layer that is exposed by, Tokyo.
And then you have the OS part.
So, we know that we want to make sure that we have a proper understanding on how much memory is allocated, and how to constrain that, As efficient as possible to keep the system healthy and reliable.
So, I end up with the conclusion that, rewriting our own GLPC, OTLP, OTAP-based receiver.
Will give us more performance and more control.
And… and that's the… basically the… the purpose of this PR. So if we look at this, This representation, it's… basically the design, implemented. We have the TCP listener, it's a regular TCP listener with the SO Reu Sport option.
That's the… The socket option that gives us a way, basically, to load balance traffic.
incoming, coming to the specific port, to the different, CPU cores that are currently, started when we start the… this, Rust OTAP engine.
And, and then, once, a new circuit is accepted, we enter into the, the H2, so the… basically the crate that is part of the Tokyo ecosystem to interpret HTTP streams.
So we rely on that, and… The nice property of this crate is they don't, force you to use send or non-send, feature. It's, it's up to you.
And then we basically reimplemented, a gRPC router. It's relatively simple on this part.
We receive, HTTP2, requests?
And then we can, based on the… the nature of the request, the URL, we can… we can basically select what will be the… the GRPC endpoint, that will manage the corresponding stream.
And then I did some, rework on the, what I name now the Ike Registry, which was something that, Joshua Put in place, so we receive From downstream component hack and NAC messages.
So, through this controller channel that we have for every component into the system, And then, if the… the waitForResult property that is, in fact, just a property to express the fact that we want to get an end-to-end acknowledgement mechanism. If this property is enabled, then the ag registry is on the pass.
If it's disabled, then we go directly and send the messages.
that we decode, either OTLP or OTAP.
Directly into the, the async, Bundy channel that is, provided by the engine.
For, for the receiver.
So in terms of, if we, if we think now in terms of, concurrency.
So we have, one, asynchron time per core.
So, it's basically a single threaded asynchron tile. Right now, we are… we are using the… the Tokyo… we configure Tokyo to run in this node.
And then, for the receiver, the receiver itself ran into a local task.
And for each new connection, we have a joint set Again, with, a local task.
And then for every stream inside a TCP connection, every HTTP2 streams.
we again have a job set. So we have basically a nesting of, local tasks.
And the first results are, really promising, so we, I was able to, So it's published into the hotel row dev.
There is a comparison between the previous implementation based on tonic and the new ones.
And, and in terms of results, or, OTAP to a TLP, So the… basically, I… I use the continuous benchmark infrastructure that we have, where we have multiple scenarios. OTAP to a TLP is basically, OTAP receiver with an attribute processor and OTLP exporter, and we have, values combination, OTAP to OTAP, OTLP to a tap, each time with an attribute processor in between.
So… The biggest improvement is OTAP to OTAP.
Basically what I observed is, 33% improvement in terms of CPU usage.
You know, and, for the memory, usage, in average, 22% improvement.
For the OTAP OTLP, I think that's the one where… it's still very interesting. It's a 9.5% improvement for the CPU.
Usage, in average, and, 20%.
22% for the memory usage in average.
So I think it's, it's a good, validation that it's… Definitely a good direction, and, that gives us also a lot of, In my opinion, flexibility for the next big step, which is, improving this part. I didn't talk about that, but the admitter. So we, we, We have a beginning of, An emission control mechanism into this implementation.
And when the admission is, basically rejecting a new TCP connection or a new stream.
we try to basically inform the client. Either we close the circuit, or we just return a a GRPC message, the status message, to, to specify to the client that, we, for whatever reason, we decide to not honor the the corresponding request.
So the… the next step will be to… To, improve the emitter.
Right now, it's relatively basic. It's based on, a maximum number of concurrent connection, concurrent stream per connection.
But if you look at all the parameters.
that, we… someone, some user can, configure. It's huge and very, very complicated to, to determine Which one needs to be, updated to get the maximum performance for a specific, scenario.
And even with that, it's relatively hard to determine, how to protect… to protect, basically, the… the engine against, out-of-memory, issues.
So, the next step will be to have an emitter that will simplify the, the story.
and express how much CPU usage you You like to… to get at the maximum in your system, or how much… Maximum memory usage, you… you are ready to accept And then having some admitter that will, dynamically decide when we can admit A new connection, or a new stream, Based on those, limits that are now… So, based on those limits, we will determine what will be the… The profunder of the queues, or the death of the queues, or the… Some other parameters.
Well, that's, I didn't start at all to work on that, but that's the next, Entropy for me.
Any question on that?
Joshua MacDonald 00:50:32 Well, I'll say something. So, I made a joke about a thousand lines of code for a gRPC implementation sounding like a good deal, because I've worked with gRPC for a long time, and it's just always been a monster of complexity.
I recognize all those flags from, like, just the HTTP2 level, and then you think about the gRPC codebase on top of it, and I've never been able to really understand it, so… if you give me a thousand-line gRPC implementation, I will love it, because I don't have to understand gRPC, sort of. So that's my… that's my feeling. I think it's probably good, very good, to do this.
Laurent Querel 00:51:12 Yeah, I think we… So, just to be clear, it's not a generic GRPC implementation, it's a tailored implementation for OTLP and OTAP, but yes, I agree. Because we focus so much on performance in this project, I think that's… Worth it to, to get the maximum we can, and this receiver side is definitively… same thing for the exporter, but I did not work at all on it. But definitively, because we have now a well-defined protocol, OTLP and OTAP, For me, it makes sense to… To invest and make sure that we have the total control on that.
And… and if we… If we want to leverage some very exotic, potential options, for example, I.O. Eoring, if we're going to leverage that. Right now, there is no, tonic implementation, but on that, I think we are closer to be able to achieve that with this, with this work.
Joshua MacDonald 00:52:20 Or a Windows IOCP implementation.
Laurent Querel 00:52:24 Yeah, yeah, the Corp.I.O. project is an interesting, one.
Which is leveraging, IOing on Linux, and what you mentioned on Windows?
Joshua MacDonald 00:52:40 Cool.
All right. Well, is it… did anybody else have, either feedback on the last topic, or, more to say in the agenda today?
Utkarsh 00:52:51 Yeah, I had a question about the… the PR that Laurent was talking about. So, it looks like we have the same receiver accepting both the OTLP unary, and the bi-directional OTAP streaming, so… What's the reasoning behind that? Like, we could have also had dedicated receivers, maybe. I was thinking, like, if it would have made things easier for the user when they're thinking of providing a config in terms of max concurrent connections, so now they would have to factor in like, how many OTLP clients might be sending… trying to connect, and how many OTAP clients. So if we keep them separate, maybe That would have made things easier, but…
Laurent Querel 00:53:34 Yeah, so the… so there is nothing preventing to, to instantiate to… so… This new receiver is named hotel receiver.
you can instantiate as many hotel receivers you want, and we could imagine that we… we can have a flag specializing it for OTLP or OTAP.
But I was thinking that… Covering also, another usage where you, you just want to open one port to, for, for these two protocols is also an interesting, Benefits?
So, the current implementation, in fact, will now cover these two scenarios. Either you decide to dedicate an hotel receiver instance only for TLP, and you put the corresponding limit on it.
And you can create another tab that is separated, or you can just use one, And that will, in fact, simplify also the… Potentially, that could simplify the configuration and also the integration of the system into The rest of your infrastructure.
Makes sense.
Utkarsh 00:54:49 Yep, yep.
Joshua MacDonald 00:54:51 I wanted to add that the Go Collector has this sort of precedent that's kind of established for us in this space. The OTLP receiver We'll receive both gRPC and HTTP2, or HTTP on the same port.
So, you end up with, like, one component is doing logs, traces of the metrics, profiles, and it's doing gRPC and HTTP. And it, when… during phase one, we cloned or forked a copy of the OTLP exporter and receiver, and we had this as part of our design philosophy then as well, which is what we're going to try and get as close to OTLP as possible by sharing a port, even.
Because OTL Aero is really meant to be, like, 100% convertible to and from OTLP, so that was the argument we made. So I think in one sense, we're just kind of continuing that here, which I support. But also, it's pretty normal to have one receiver do all the forms of OTLP, even, where you're gonna see a gRPC and an HTTP configuration side by side.
I'm used to it, at least.
Laurent Querel 00:56:00 Yeah, right now, we don't support the… OTLP over HTTP.
But, yeah, definitively, that's something we could imagine with this approach.
And we could even imagine some other protocols that will be a little bit more involved, but The fact that we have this level of control, and we… we basically reimplement everything except the HTTP2 layer, give us a lot of potential options.
to integrate other protocols that are either based on HTTP1 or HTTP2.
Joshua MacDonald 00:56:47 This sounds good to me.
I saw… I saw Andres asked in the channel, about other protocols as well, I… I was wondering what those… what ideas you had there.
Andres Borja 00:57:01 Aw.
No, I was basically thinking on what your slot and respond, right?
I was mentioning it more in, You know, like.
if we are worried about that, right? So, someone comes and says, hey, but I have these logs, and I want to send it for the same port.
It sounds awful initially, but… If it doesn't have, like, a lot of overhead selecting the protocol.
Joshua MacDonald 00:57:35 In my old company, we did just what you're describing. We had a single, sort of, collector-like thing that would speak OTLP and all these internal protocols, like Jaeger, or, like, thrift variations of other stuff that we had from internal days.
And it was pretty hard to get working in the gRPC Go implementation, and also, I guess there's a complication in HTTP2, Involving clear text, and, you know, like, it works if you're clear text, but not if you're on an SSL connection. You have to do a downgrade to get And if you're inside of a data center, you're probably going to want clear text. So, it became complicated, is all I know. And it was always much easier to give one port per protocol.
Of course, OTLP and OTAP and the HTTP versus gRPC felt like a special case. I would like to actually ask, I know we have, like, zero time left, if… this has come up at least once in my internal discussions over the past week, like, could you have an OTAP bytes data datagram that was just a single HTTP request, that doesn't require gRPC, that doesn't require a stream, that just is, like.
I'm gonna accept the compression loss, I want to send you one arrow payload.
I know it can be encoded in Arrow IPC, it's just identical to a stream with length 1.
Laurent Querel 00:58:58 Yes, yes.
Joshua MacDonald 00:58:59 I remember years ago, when we first proposed to use streams and gRPC for OTO Arrow, that it was a lot of, like, resistance to the idea of a streaming protocol. That's why I raise it now, is I think we almost have all the pieces to do a single, one-off, a unary OTAP request.
It's another thing that might share the same port.
Laurent Querel 00:59:22 Yeah, technically, I agreed to add on to a stream of one… One batch.
Yeah, we will lose the… all the… The fact that we are not sending again and again schemas and dictionaries, and we just send delta dictionaries.
So that will have a cost, definitively.
In fact, what we use, what we leverage is more the statefulness of the protocol, the fact that it's a stream, so we know that All the, the network infrastructure between the client and the… and the server will… will, Comply with the statefulness of this protocol, and we will end up always to the same server.
And then we can accumulate the state on the server side to make them… To, to make the… that, much more efficient.
And we did, for people that didn't follow the OTAP protocol from the beginning, but in order to be friendly with load balancer, what we did is… Like, a trade-off between having A stateful protocol, and keeping the streams, in terms of lifetime, relatively short.
So we… and having multiple of those, streams in parallel, so that means that we can load balance Those streams, pretty efficiently.
So I think it's a good trade-off.
And give us, maximum of performance in terms of compression rate.
Joshua MacDonald 01:01:06 Yes, thank you. I feel like a lot of people are sort of having this knee-jerk reaction to streaming, and that's why I asked, because I put up also this compression results diagram that you made years ago. I suppose we could repeat this experiment.
Again, but this is, like, to point out how much compression you're getting. People are willing to give you back that much compression at some level for a stateless protocol.
Laurent Querel 01:01:31 Yeah, I agree. I mean, we could support that definitively.
Joshua MacDonald 01:01:35 And still, even if we don't have the benefits of the compression, right?
Laurent Querel 01:01:40 We will have the benefits of, having, zero deserialization cost, and zero serialization cost, and much faster data processing speed. So, I agree. That could be definitively a good, A good, scenario.
Joshua MacDonald 01:02:01 Yeah, I think it didn't make sense in Phase 1. Like, the benefits of having an arrow representation and zero copy are kind of lost in the GOAT pipeline.
Laurent Querel 01:02:10 Yes.
Joshua MacDonald 01:02:10 Alright, well, we've come to the end of the hour. Thank you all.
I think we can call it, and, I appreciate you all. See you in a week, in a couple days.
Oh no! It's Thanksgiving!
Two weeks from now, right here.
Sorry.
Laurent Querel 01:02:26 And I will not be there, so in two weeks…
Joshua MacDonald 01:02:29 Go to the meeting if.
Laurent Querel 01:02:29 vacation.
Joshua MacDonald 01:02:32 Albert, I think you might be, on your own.
Laurent Querel 01:02:35 For that… that one. You can… you can call it off. All right, thanks all. See you… see you next time.
Andres Borja 01:02:40 Oh, God.
