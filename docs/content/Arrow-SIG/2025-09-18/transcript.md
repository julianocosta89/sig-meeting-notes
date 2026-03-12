SIG: Arrow SIG
Date: 2025-09-18
Duration: 34 minutes
============================================================

## Zoom Recording Transcript

**jmacdonald** 00:37 My video's not coming on today.
There's Albert. Can you… you must be able to hear me. You can hear me.
**albertlockett** 00:45 Oh, yeah, we can hear you. Okay. Yeah, I can hear you.
**jmacdonald** 00:50 Camera won't come on. Oh, there it is! Hey, came on.
**albertlockett** 00:53 It's…
**jmacdonald** 00:54 All right. Well, I know Albert… I know, Laurent is out this week, so we might have a quick and short meeting, I was gonna pull up an agenda. The smaller it is, the less we need it, though.
So… So, yeah, there's a couple useful things I want to ask Albert. I have two questions in mind for my agenda, and I'm glad you're here. Thank you for being. So, for me, I'll just, edit this notes real quick. We got 3 of us.
So… Let me start with a real question that's not about my hackathon that we just had.
Cool. Alright, so I have an issue number, I need to find it.
But I'll share my screen.
Okay, you see my screen now? Good. Okay, here we are. Just to keep it quick then, I like to have quick meetings on a Thursday morning, by the way.
I opened our issues list.
And… these issues are newer than I… so there's some new issues here, maybe we could talk through, I see Laurent filing some… I'm trying to find the one that I filed.
Because I'm curious about this one. Okay, so, so during the past week, I saw Laurent comment, it was on one of David's PRs, Josh is busy working on this, which is sort of true, but sort of not true. I got stalled.
So, the comment started in my work on back propagation. This was one of my… my drafts.
I was… The path that I was on, Laurent and I have talked about a bit, I think the high-level ideas are correct. So, what I'm… what I'm trying to do is, make back pressure work by finishing the ACNAC mechanism, and I basically understand how it works, and how it shall be done. According to Laurent, what we're going to do is pass the AC and the NAC back through the pipeline control channel. That way, the pipeline controller Has a whole view of the system's back pressure.
This is only one of the ways we could have done it. The other way would be to have every node know about its routing table to get… to send direct routing messages, so that… but right now, nodes do not start, or components do not start with a map of all other nodes. They only start with channels that they've been handed.
So, to send an ACK NAC, we are going to push the pipeline control message with an ACK to deliver. The pipeline controller will then use its routing table to send it to the correct node. And it can also then intercept it, do whatever logic it wants, that's the idea.
So the PR in front of us is where I realized that things were falling apart.
So there were some simple mechanical changes that I needed to get done. First thing I did, and this is already done, is to add a generic P data to the node control message. When it came to finishing the task, I also wanted a P data generic on the pipeline control message.
So… The issue is about the problems I encountered when I tried to do that.
So here is a example of the change I'm looking to do, and this is a pure mechanical change. All I'm doing is adding P data to all the pipeline control types. So P data, P data, it's like nothing to see here at all.
Of course, we're not using it yet in this PR, so I put a phantom data in one place, but basically this is, like, super dumb. Problem is that this doesn't compile. And the reason is, getting into territory that I feel very uncomfortable with as a still quite new Rust programmer. So… that's when I put it into the issue. So the issue is that, the admin crate has P data bounds for its generic, which includes send and sync, and static.
And clone and debug.
So… this issue… And the comment that spawned it was Laurent saying, yeah, I can fix that. I want to sep… I want to do something about this, because as soon as I add that generic on pipeline data, pipeline data becomes bound by sync and send and all those things in ways that I don't think we want.
And so, he said he was gonna do something about it, you know, but I… so I thought I'd wait, but then he went away for a week, and now I've been waiting for more than a week. So this is where we're stalled.
I also had a hackathon, so there was a good distraction, and I'll talk about that.
But, I don't really know what to do here. My hunch… high-level idea, is we're going to create a new type of channel that lets the admin have it sync and send, and only certain messages need to become sync and send to send to the admin controller.
Meaning having a separate type of, I guess, Separate pipeline control for… For admin, then for the rest of the… system. At this point, I'm out of ideas, I'm just saying what I'm confused by.
And we have a couple people join us, so just to bring up what we're talking about here, I, I ran into this problem. It's caused me to stall in my work about delivering ACMessage and NACMessage. And, well, that was what my question was about. Any ideas, Albert?
**albertlockett** 06:59 I think I'd need to go a little… bit deeper into it, like, to speak to it, like, authoritatively, just because, like.
I'll admit, like, that some of the pipeline mechanics just haven't been something that I've, like, been super deep in. I've mostly been…
**jmacdonald** 07:19 on LinkedIn.
**albertlockett** 07:21 We did a transformation in some of the components, but… Like… without… Without thinking about it too deeply, and without being able to call out any of the caveats, like… I think that what you explained, like.
makes sense. So the idea would be, like, we have, these, like… Admin control messages that are kind of, like.
I guess they need to be sync and send, because they get… Sent to every instance of the pipeline, which are local to a particular thread, but then we have these pipeline control messages that, like, need to be sent within… A particular pipeline, and those… need to be generic over the P data, and… Because the PA does not send, those can't be sent? Is that the idea?
**jmacdonald** 08:17 Yeah, that's the… that's the problem we're having, kind of.
**albertlockett** 08:20 Okay. And the feature of this design that we're working on is that the ACT message and the NAC message.
**jmacdonald** 08:26 begin to contain a P data in them. If the request fails, we only had one copy of the data, we're handing it back to you, this failed, so it goes back through both channels, the node control and the pipeline control.
So yeah, then, I think at the high level, I understand what's needed. I don't have a, like, clear picture of what to do in the close, like, near term, so what I'm going to do is kind of wait on this.
And ask Laurent for help.
Probably because I'm not… I'm not super stalled in reality, and I'll explain that there's a few other things going on.
Yes.
So, thank you for letting me speak through that one.
**albertlockett** 09:06 Next week, Josh, like, so, like, I think that, like, like, next week we have some, like, company meetings, and… in, in Seattle, but, like.
Depending on, like, what his travel schedule is like on Monday, he might have time to respond.
**jmacdonald** 09:23 I think if he gives me an approach, just, like, if he gives me some high-level guidance, I can handle this. But since he said he was gonna do it, and then didn't, I kind of ended up waiting.
So cool.
I have another item to put on the agenda, since it's right in front of us.
So, I had a hackathon this week. Ukarsh was partly with me for it, but it was sort of like I wanted to do something, and Microsoft invited me to have a hackathon, so it's my first time here doing a hackathon, and I took the opportunity. I… hinted at what I was kind of curious about last week. Albert, you mentioned some pseudocode for how a Parquet receiver could be written. Ukarj pointed out right away in my little hackathon journey that I was taking a detour in an unnecessary direction. Why do you need a Parquet receiver to do a hackathon project about tail sampling, for example. And the answer is, I don't. He was correct.
So… but I… but I… but I'll… I'll bring that story back around. The… the… The, We all have hackathons.
So, I… I started with a receiver that, you know, and I kind of, like, learned a little bit about this and that, you know, like… but… but basically, I now really do understand the Parquet representation.
And I used the output from the Parquet exporter, and I, ended up writing some code with lots of help from Assistant, that, sort of does a streaming merge join for the, the various tables.
coming in, and then it reconstructs OTAP.
barely got this to work. I think I have an idea, roughly, of what I'm doing, but I wanted to, like, now that I have a basic framework in mind for what this… what this does, there's so many ways to use Arrow, and I think I am… coming… coming to want to say, well, if… if you were to sketch out a Parquet receiver for somebody, and you know how to do Parquet reads.
So you're gonna get this stream of record batches from… each Parquet file, and then you can string them together in an order so that you can get a stream of batches after a stream of batches after a stream of batches.
So then I get my primary table out of, say, the logs Parquet file.
And I see it has, you know, IDs 0 through 100, and now I want to, scan through one of the other tables, like loggers, and I want to find all the rows.
I want to find all the rows that are… matching parent ID 0 through 99, or whatever.
And then I want to take those rows and move them into my output stream.
Meaning what I… meaning I want to take those rows, And… form them into a, output.
I have to reconstruct a new set of arrays.
And I'm asking, basically, at this point, what are the low-level arrow code paths or mechanisms that I would use. My first instinct, of course, is to, like, row by row, just copy them, whatever that means. Array builders for the output. Each row I see, I'm gonna move it, but I… I'm just not enough familiar with Arrow's, like, philosophy and framework and primitives for this.
If you were doing this, what would you imagine with more experience?
**albertlockett** 13:06 So, or are you using Data Fusion for this, or are you using…
**jmacdonald** 13:14 Well, I, first of all, have done a lot of fiddling with DataFusion in the last 3 days. I did at one point ask myself, can I do that? I can do this with Data Fusion. I can… I can write a query that joins the two, et cetera, et cetera.
it sounded like overkill at some point. Like, DataFusion makes my compile… my machine, like, overheat, honestly. I need a bigger dev box to use DataFusion. So, I started that way, and then I decided that it would be better to just go directly with Parquet readers and so on.
Before I end up, as I said, the idea of this as a hackathon project, why are you working on a Parquet receiver if what you want to do is fiddle around with sampling? That was a valid point.
my next idea would be to say, okay, the default mode of the Parquet receiver is to just read all the files and put them into OTAP. The alternate mode is, here's a query.
That selects which records you want out of the Parquet.
from the primary table, do anything you want with DataFusion, and then still produces a stream of primary records. You can then join back together the records that match in all those other tables, I suspect.
But then again, I'm just kind of, like, waving my hands at this point.
Yeah, I think I just want to know, like, when you think of this, what code paths would you end up… Taking.
**albertlockett** 14:40 So, yeah, so I guess.
**jmacdonald** 14:45 to…
**albertlockett** 14:46 to restate the problem, to make sure I understand it, it's like, we've got our… we've got our root record batch, let's say it's logs, right? And we say, like, I just… I read these logs from the, like, the logs Parquet file, and then I want to turn around and say, okay, now I need to go get the, The arrow, or the… what do you call it? The, log adders, right? Something that's, like, joined to it by parent ID. And then I want to reconstruct that into OTAB. So, the first thing that, like, jumps to mind that, like, might be helpful is the, generally the, arrow schema Does get, like… written to the Parquet metadata. So by default, when you read it back, from Parquet, using that, just using, like, the Arrow RS Parquet reader, it will read it back in this, like, the Arrow schema that it was written. So that means that, like.
Like, the… the data types and whatnot that it will read back, like, should be, like, the… like, the data types that, like.
like, our… I guess, like, relevant for OTAP. Like, it's the correct OTAP data types. So I don't think you'd need to make too many modifications. Like, one thing that would need to be modified is probably, like, the ID columns, because I think we… we.
**jmacdonald** 16:19 Yeah, so we see 32-bit IDs, and then I read a batch of those, and then I offset… I compute the mapping back into zero origin. I'm not sure that that's necessary, actually, so each batch would have a zero origin.
major… and you mark them as plain encoding so that they look memory optimized, and it is actually functioning, what I have, but I had doubts. There were a couple of column-type transformations that had to be done. One was a UTF-8 view that was turned back into a UTF-8. This is where I was, like, pretty much, like, barely understood what was happening.
But, what you said makes sense.
I'm still sort of, like, mechanically speaking, when you're dealing with this arrow question, so now I've… I've selected from one Parquet reader all the logs I want, and I wanted pull in all the log attachers with matching parent IDs from the same set of Parquet files, or from the equival… you know, the sibling data tables.
now I imagine I'm consuming a batch, I see a batch of log etchers, I know they're sorted by parent ID, I can now say.
From this batch, I want to take… as many rows as… until parent ID is, exceeds a threshold. So I'm going to say, okay, the first 200 rows of this file, of this… of this stream I'm just… or this record, I want to copy 200 rows from this record into a new… a new array.
And then I would do that column-wise.
Maybe there's nothing special at all about this, except to embrace that there are arrow primitives that can copy those arrays.
**albertlockett** 18:16 like, sorry, I guess I'm… I'm not, I'm not getting, like, the array copying thing. Like, when you… when you read the record batch back from… back from Parquet, it's already… in… it's already an arrow record batch, right? So, like, is the copying that you're saying just, like, the few… like, copying the few columns that you need to modify, like, copying the data and then changing the type?
**jmacdonald** 18:37 Well, I might… I might read a record batch from my loggers and get, like, a thousand of them, but only the first 200 need to move into my first batch, and then the next 800 will be part of my next batch.
**albertlockett** 18:48 So I wanna… Yeah, okay, sorry. No, sorry.
**jmacdonald** 18:53 I think I can just directly refer to those arrays.
No .
**albertlockett** 19:02 Okay.
**jmacdonald** 19:03 Depending on lifetime.
**albertlockett** 19:05 Yeah, yeah, I see what you mean. So, it's like, you kind of… yeah.
It's like, you kind of need to… you want to, like, slice the… you essentially want to create a slice of the record batch. Like, I've got the IDs, like, from this offset to this offset in the record batch, like, correspond to the IDs that match my parent. And then it's like, I want to create a new record batch of that.
like, from that offset to that offset. I assume they're all lined up.
**jmacdonald** 19:38 They seem to be.
**albertlockett** 19:39 Okay. Yeah, I think… I think that would be… so, yeah, I'm not sure if you… if you slice the record batch, if it, like, if it copies the arrays or not.
I don't know that offhand.
**jmacdonald** 19:52 I would want a copy anyway for the framework we're building here. It's fine. I think I… I just, this was more or less me fishing for the, like, the… what does an experienced arrow programmer reach for when they see a record batch they want to take?
200 rows from.
Copy into a new batch.
And I think the answer is… probably not… not very surprising. You will end up copying sub… you know, slices of one record batch to form another.
And, well, we've reached the end of my question.
Thank you. I learned a ton, and I feel very good about First of all, I'm comfortable with the Parquet format now. I did succeed, even though it's messy code.
So I'm very happy with my hackathon. I, we've reached the end of my agenda item. Looks like, Albert, you had a hackathon, too. It's the time of year when one has hackathons, apparently.
**albertlockett** 20:55 Yeah.
**jmacdonald** 20:56 Corporate plans. Everybody do their same week hackathon.
**albertlockett** 21:01 since Laurent is on PTO, I get to do whatever I want, because I have no supervision.
**jmacdonald** 21:07 I also have my manager out of town right now.
**albertlockett** 21:12 Yeah, let me see if I could share, and then I'll show what I did. So, this is… this is gonna be a lot, like, shorter, and, Maybe less flashy, but oh no, how do I share the… Share the desktop.
Oh, I need to restart the Zoom. Okay, hold on.
I need to stop and rejoin, because I didn't have sharing permission. Be right back.
**albertlockett** 22:05 Okay, sorry about that. Oh, wow.
Desktop 2… Okay, hopefully this works. Yeah, so what I wanted to try this week was to try to dig into what has been happening in the query engine crate, because, I hadn't been in there, and So, I guess we don't have Drew or, mike on the call, but… That's… that's…
**jmacdonald** 22:33 May I… we're recording, I will send them back to this. I could probably try and bring Drew in, but he's under a pressure to release something right now, they're kind of having a drill.
**albertlockett** 22:42 Yeah, and this, like, this isn't, like, a super interesting thing, so it's definitely something you'd, like, check out after, but, basically what I did was I took their, their KQL parser code that, they wrote, and this creates, this, This thing called, like, a pipeline expression, which has, all these… I guess it's like our intermediate representation of the, the KQL query, and you can see it's got all these expressions, and whatnot. And then what I did was I tried to take those and create, like, a mapping between the KQL, or the, like, our intermediate representation data expressions, and the data fusion, logical plan expressions. So you can see what, like, there's some code here that, like, does that, tries to take a logical plan builder and say, like.
It's not all the way done, but if it's a… like… OTAB data flow discard expression, then that means it's a data fusion filter expression, and then we go down and we… parse the… the… the filter expression, and parse the source and the static values. And anyway, this is, like.
not, like… I didn't go very deep, but what's cool about this is that, you can see I wrote out some Parquet files using our Parquet exporter, and then we can go and we can query them using KQL, using our KQL parser. So if I run this… This will… Spit out, a query result.
For, log attributes that we specified, The output that we want using… KQL. And so, you can see some of the other… query types that I got working here. So, anyway, that's… that's the entire demo.
**jmacdonald** 24:46 That's sweet, though. That's awesome. First, that you've picked that up without guidance from Drew and team.
Fantastic. Can you show us how you join the, the attributes in, like, where in your logical plan are the attributes joined together, or queried by I'm, I'm…
**albertlockett** 25:09 I haven't… So I haven't… I haven't joined them yet. This is just operating on one table, so…
**jmacdonald** 25:17 Yeah, so… Gotcha, gotcha, gotcha.
**albertlockett** 25:19 Just, I said, like, just use the attributes table, and then this is just querying…
**jmacdonald** 25:24 Oh, I gotcha, I gotcha.
**albertlockett** 25:25 Yeah, I didn't… I didn't… I didn't know KQL, like, well enough to figure out, like, how you would represent a join or anything like that yet, but…
**jmacdonald** 25:35 Yeah, yeah, yeah. I was… That'll be a good area for us to talk about in the future. I think, the… And this is sort of the same topic I've been starting to think about myself, is that, like, I want to write queries that look at records with both attributes and timestamps and names and so on all at once. And I know how to join those in SQL, And I don't know how we would… but my understanding of the KQL syntax, and this is, something that Drew and Michael have gone deep on, is, like.
When you refer to an attribute, sometimes, like, it should be the attributes, sometimes it's the scope, sometimes it's the resource, and they had worked out ways to be explicit so that you could, like, clarify which one you were looking for, and so on.
So I expect there's some sort of implicit joins that are required just to put together the OTAP into a record. It's not talking about joining KQL multiple record streams, exactly. But this is, well, really cool to see. I… I'm sure every one of us could learn something by looking at what you've done, and I'm still enthusiastic about data fusion.
**albertlockett** 26:47 Let me drop the code in… And, I'll drop the code in Slack.
**jmacdonald** 26:54 Sweet.
**albertlockett** 26:55 And then, we can have it there.
Qql.
Data… Asian code. Oops.
Disgust.
on SIG.
I guess I could drop it in the meeting notes, too, that probably makes more sense, so then people…
**jmacdonald** 27:16 Yeah, sure, that'll help as well. This is really, really cool.
Appreciate your demo.
We… So assuming that was the end of your demo, I would say we have time to talk more, and I don't necessarily want to, but I accept that Jake put a question in the chat, and now I want to bring us back to it, make sure of one thing.
The… the… the… what I realized is that I don't need to… So I'm reading a batch of logs from Parquet. They come with ascending IDs.
But there are UN32s, so I can read up to 65,000 of them before I run out of a D space.
Okay, I've answered my own question right here in front of you. So, at some point, I'm going to run out of IDs. I can… the first batch of vlogatchers in that same space, I don't have to modify. They will come in with the same parent IDs in range 0 through 65,000.
As I continue reading these, if there's more than 65,000 records in the Parquet files.
I am now gonna have to start remapping my ID space.
So that independent batches have no more than 2 to the 16 rows.
So, but I think, Jake, your question maybe was something about, well, in… there are common cases where I receive a bunch of data from Parquet. I can kind of just Copy subranges of those arrays that I just read from Parquet, except for the ID columns, I can't. I have to change their type and offset them so they fit 16 bits.
But all the other fields in those tables, I think I can, if I was able to, in the Rust mechanics, you know, memory-wise, if I was able to borrow those rays, I could reference them in another record batch.
Through subs… like, slices of those arrays. So I could take one record batch that was thousands of records, I could slice every one of the attribute columns, or all the non-ID columns.
to get the range I want, but then I need to synthesize a new ID column to, like, put numbers on those rows that are in the 16-bit space.
If everything I said just now makes approximate sense, we're finished.
If there are questions or comments or discussions, I'd love to hear it.
**albertlockett** 29:53 That… that makes sense to me. Yeah.
**Jake Dern** 29:56 Me too.
**albertlockett** 29:57 Yeah, I think you could, like, you could take your batch, and you could say.
If it's sorted, you could do… like, there's an arrow compute, kernel that you can, like, subtract a scalar from the… From the array value. So you could subtract the first value from the entire array, and then you can use the arrow compute cast to… To turn it down to a 16-bit.
**jmacdonald** 30:24 you call that an arrow compute kernel. Those words make sense. Do you know what it's actually named, or how I would really find it, or…
**albertlockett** 30:31 It's, air, yeah, arrow, arrow, colon, colon, compute, colon, colon cast is the… That's the… to change the type.
**jmacdonald** 30:46 So, it's the arrow… colon, colon, compute crate.
Where all these kernels are.
**albertlockett** 30:52 this, module here.
And so there's, CAST is in there, and then I think in, there's one called… Oh, kernel… I think it's kernel numeric, or kernel… Kernel numeric add that you can use to… or there's a subtract one as well, which I guess is probably what you're gonna try to do, subtract…
**jmacdonald** 31:20 Got it.
I see. I mean, I can figure this, I can find this.
**albertlockett** 31:24 Yeah.
**jmacdonald** 31:25 Cool.
Numeric, compute kernel numeric, got it. All right.
Sweet. I'm gonna put some of those, just links in the notes. Appreciate your guidance and your wisdom on this topic. I feel like one day, I won't be able to write arrow code the way you do.
Maybe.
**albertlockett** 31:47 Yeah, I don't know if I'm… the expert, either.
**jmacdonald** 31:50 Well, I don't know, I just, as a relative newcomer here, I've read some of, you know, the changes that you and Michael are writing, and it just seems like next level. Like, you know, when I first learned Rust, I was like, wow, there's this whole set of types that I really need to get, like, under my thumb. Like, I just really need to know the option.
the result.
the iterator, you know, like, these are your basic Rust types, and until you are comfortable with every, like, all the ins and outs of those options and results, and basic… you can't write any Rust without… without stumbling over yourself constantly. But once you begin to know those option and result basic types.
your fluidity with Rust becomes much better. I want to reach that level with my arrow, and I'm just not there yet. So, I see you guys reaching for all this stuff, knowing that the kernels are there, and so on, and just, like… So, I admire your code, and I'll keep learning from it. Thank you.
**albertlockett** 32:42 We'll learn from each other, that's, it's a good price.
**jmacdonald** 32:45 Well, thank you, folks. I will follow up with Arant on the item at the top of the meeting. Unless we have more to talk about, I think we're finished, and have a great Thursday.
Hi, Tristan.
**tsloughter** 32:56 Actually, could I say one thing? One thing?
**jmacdonald** 32:58 Sure, love it.
**tsloughter** 32:59 Well, I just started at Grok, with a Q, and… when I got here, I learned that they actually used the Hotel Arrow, in the Go Collector, the receiver and… receiver and exporter, so that was cool. They still have to look into… well, I'm supposed to, switching the metrics and logging over to using it. It's only traces right now.
But, yeah, good work, and we'll get metrics and logs moved over, too.
**albertlockett** 33:27 That's cool.
**jmacdonald** 33:29 Yeah, awesome. Good to hear. I know I've seen, steady progress in turning OTAP back into OTLP for the metrics and the logs with Albert's work, especially. So, yeah, thank you all. This is still an exciting project.
Grok with a Q. I have to look into it. Not Grok with a K, I understand. Swish.
We can be non-political in this space. Alright, Thank you all, have a lovely day.
See you on Tuesday, next week.
**albertlockett** 34:02 Hi, everyone.
