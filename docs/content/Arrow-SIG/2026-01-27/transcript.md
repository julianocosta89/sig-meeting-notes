SIG: Arrow SIG
Date: 2026-01-27
Duration: 30 minutes
Zoom Recording URL: https://zoom.us/rec/share/uc_yyREvl3NoRW5vE1Tv3zok78SgA35fWsG95bGvJbh6-dnrNsNzH8h7egFdzJIy.a6OITCrtQhZF7lyS
============================================================

## Zoom Recording Transcript

**jmacdonald** 03:17 Hi, everybody.
I'm gonna put meeting notes in the chat, just in case you want to link
I'm gonna wait a few minutes here, and… I'm hoping…
If you're here, you'll add your name to the agenda, and, any topics that you'd like to discuss.
I am hoping to see Laurent here. He mentions some important topics.
That I'm aware of.
So, have at it.
Okay, well, we're closing in on 5 minutes, and I'm maybe ready to start.
Let's see, who do we have?
Well, if we don't get, many of the F5 people, I, will feel free to move on.
And… I will say no more for now.
Okay, we can do issue triage.
I looked over the issues, Didn't see,
A great deal of new, since we spoke about
Up through Proposal 8 at the last meeting. Proposal 9, I believe, came right after the last meeting.
So, new issues that we have, on, on the list today are one about Calmnor Query Engine.
supporting the inserting of attributes. I know that Tom has been working, on a feature for the attributes processor. It may have merged already, which would be a different code path than the one Albert is posting about here.
If that sounds correct.
to anybody… I saw Jake… an update from Jake about public transit. Okay, okay.
Very good.
Okay, so without Albert here, Tom, if you have anything to say about attributes, since I mentioned you, you might speak up, but otherwise we're going to move on.
Okay, nothing to say. There's one from, from Chanley, and I've taken a look at this. I actually… there's a draft PR that's up.
And,
there's some talk about tagging the messages as they go through the graph to essentially to annotate their path, so that you know when there's a Fanian arrangement, which node was your source.
this PR is open, and I'll say I already looked at it. There's a… I made a comment, and it's… it's about how…
Well, there's a very large change implied by this fragment right here, is right now, all of our P data objects are pure traits, generic traits that have no bindings. They have no requirements, and therefore, you can say generic over P data basically throughout the code.
If we add this where and a binding.
I can see the benefit of doing so, and the comment is I looked at doing that myself, and then I just turned around and didn't do it that way. So I've given that feedback.
The idea of a message source sounds good to me.
I'm going to look into responding to this more. I'd like us to be considering the use of the context to store this, not a message… not a trait binding.
Anybody have comments on that?
Okay.
We'll go right back.
Other new issues, to look over, Would be…
Panic value is less than previous value, oh boy, haven't seen this one yet.
schema Builder, Metrics Builder, Producer… Okay, the code snippet.
**Jake Dern** 08:25 I, I did happen to skim that one. I think it was just the case of overflowing IDs because the batch sizes were very large, like 100,000 records.
So it's kind of a bad error message.
**jmacdonald** 08:38 Gotcha.
**Jake Dern** 08:38 But, yeah. Anyway, that was what Albert commented.
**jmacdonald** 08:42 Okay, so Albert's made a comment. Yeah, we're limited to 16 bits of address space for metric data points. That has been an issue in the past.
But mainly when people are exercising this code, and they turn it up past 64K.
Happened in the Go Collector as well.
I don't know if that's a major issue, or… it seems like it could be a non-breaking change if we were just to fix it in all the implementations.
So…
So, yeah, totally confusing. Okay, well, I think we can resolve that. Someone can fix that. I'm sure that there's a solution.
columnar engine, support multiple assignments in one set, so I haven't been following this OPL project very closely. Without Albert here, I don't think we should spend much time talking about it. I say I haven't been following it very closely, I have been following it, and…
It looks like they are continuing to develop it.
Last I read this one by Drew, talking about how we need to do something like the Go Collector has done, meaning to make it, totally optional whether you use gRPC or HTTP or both.
That looks fairly non-controversial to me.
Having an option here totally makes sense.
I don't know about flatten and default.
Going back to the Go Collector example,
like, half the difficulty of understanding the Go codebase is understanding how hard configuration is, and whether a value is a nil or a struct with default values, and whether an optional is present with default values and all, so on, is quite complicated.
So I would say we probably want this to be not flattened, and make these There'd be no default.
Or something along those lines.
no sort of default.
this would bleed over into my general sort of confusion, a little bit of confusion about and or worry about configuration. How we do configuration is something that we're going to have to sort out quite soon. There was also an issue about that, but we went over it on Thursday.
That one is 1830… 18… 32.
Right here. So, we've got some work on configuration. But once we, do, we should be able to make HTTP and gRPC independent options. Okay.
Any topics that you'd like to talk about, following the issue triage there, or something I missed?
Alright.
Okay, well, no pressure. I was hoping to see, a discussion here about global Channels?
I understand that the terminology that I'm using might be opaque. The term is probably misleading, and I've also heard Laurent speak to it about it as a
more of, like, a subscription mechanism where you have topics, but the point is they're named. Named topics, that we would be, that we would somehow be able to configure to cross thread boundaries. That's the conversation I was hoping to have.
However, there is no new issue, and no one here to talk about that with me.
So… I think… That can be a next time.
I…
Am not aware of any, broad, generally applicable topics to… to put on the agenda right now.
Myself.
I did create this PRs to Discuss section.
And I would be glad to move into that area, unless anyone objects.
No one's objecting. We don't have to have meetings on Tuesday afternoon, you guys.
**Aaron Marten** 12:58 Hey, Josh, can you hear me?
**jmacdonald** 12:59 Yes, hi, Aaron.
**Aaron Marten** 13:01 Oh, hey, so just in case we do have a little time, maybe… maybe… I know there's not a big audience here, but on that Global Channels one, and the topics, is the main driving thrust of that just to have cross-thread communication mechanism? Like, like, I was trying to under… I think I read the Proposal 7, I think that's what this one is about.
And I was having trouble understanding
You know, just the… some of the concrete reasons why we…
**jmacdonald** 13:28 Thank you.
Right, well, that's, thank you. Let's dive in a little bit. I have to refresh my memory exactly on this issue, because I've heard it… I've already used the wrong term. So we're gonna call this, sort of, topics, or the config…
And… and… Named Rendezvous Point,
I… I don't know how to answer your question, because I have to read this. Obviously, this is a lengthy one, and I haven't read it in detail. But, the… the use case that I'm aware of,
comes down to, the idea that eventually you need to rebalance load, which can't always be rebalanced at the receiver. You know, the processor load is different, the data is different, and so…
If you're going to have something like the Go Collectors, load balancing exporter.
So you've got some sort of, like, stable hash, or consistent, like, hashing mechanism, or rendezvous hashing mechanism, or whatever you call it these days, then you will, look up your set of
targets, which will have a fixed number, and then you will hash onto that many nodes, and you will re… and you will shuffle the data onto that many nodes. Whether it's foreign endpoints or even
topics in the same pipeline. So you could imagine having
Like, multi-core receivers, and then going to a, essentially, broadcast to, like.
One per core topic to, like, shard the data or to, like, load balancing export it, so that you can divide work from one core and split it onto all the cores.
And I know Laurent has talked about this concept called… he refers to it that's from an academic paper called Morsel-Driven Parallelism.
And I think that that's a… a similar… a term for a similar type of, like, architectural arrangement, where you take large pieces of work, you split them into pieces, and you… you redistribute them amongst yourselves across thread boundaries, and then continue.
Does that sound like what you were expecting me to say?
**Aaron Marten** 15:40 Yeah, that's super helpful. I will go look up that paper to give myself a little bit more context.
**jmacdonald** 15:44 Yeah, I don't know too much more than that, but I know you and I have spoken a little bit about, sort of, stream processing generally, and you end up with needing something in this space here, and I think that's what we're looking at.
**Aaron Marten** 15:56 Thanks.
**jmacdonald** 15:57 Nice. Okay, cool, so we spoke about that for a minute. Good job.
I, while I was speaking, I moved the, the list of,
issues so that you could speak ahead of me, Erin. I have a brief… to mention my PR is no big deal, but, I… I have been,
personally falling a little behind on reviews. I know you've got a big one out. This is the number 1882. I haven't dove in yet. Dived in? I didn't dive in yet.
But we know what this is, and we've been looking forward to it, so thank you. This is finally the first component that uses your new library from the Dataflow engine. I take it.
**Aaron Marten** 16:44 Yeah, yeah, so this is… I mean, it's pretty self-descriptive in the title. This adds a persistence processor.
into OTEP Dataflow, that uses Quiver to power its… It's persistence.
So, thank you for everybody that's reviewed and left comments so far. I published this on Friday evening, and it's already gotten quite a bit of
quite a bit of participation, so I appreciate that. There is one kind of major comment still left unresolved that I'm… I'm working on right now. Lala had said, asked about
You know, we really do need to do some kind of retry.
you know, retry mechanism as part of this. And so I was working on that. One thing that we… that I don't need for this PR, but I think we should probably talk about in a follow-up, is this second paragraph of my comment here, which is that NAC messages that we get back
from the exporter, all they have on them is a string that has a human-readable reason. So there's no machinery to be like, do we know this? This is… what kind of failure was this? Because if it's a permanent failure.
there's no sense in us continuing to, like, persist that data and retry it. We should just drop it right away, because we know it's, poisoned, or it's gonna cause, you know, repeated permanent failures.
Versus, you know, temporary failure, like.
Network was down, and it might come back up in 2 minutes, you know?
So, that would help here.
**jmacdonald** 18:16 Yes.
**Aaron Marten** 18:18 But it's not strictly required. I do have another commit that is a…
you know, another significant size commit that I… that I'm planning on pushing up to this…
branch pretty soon here, that will provide, a retry strategy that we can get with for now, so…
**jmacdonald** 18:37 Got it. Have you… okay, so,
That's good information. I did consider adding an error code, like the gRPC code or the HTTP status code, directly in the AC when I first prototyped, and it was just such a big piece of work that I took out as much as I could, so it never made it in.
And, so, that's appropriate, that's something that we should get done quickly.
I would…
I would… I would propose just we… we add it to the NAC structure, and, you know, it shouldn't be too… too hard.
**Aaron Marten** 19:16 I think what I would personally really want on that is not even, like, a gRPC code or HTTP code, because then all you're doing is, like, pushing that logic back up
here, where it wouldn't necessarily belong. Just, like, a Boolean, even, that's, like.
**jmacdonald** 19:30 Is this retryable or not?
yes. I actually had a permanent Boolean, because those codes are kind of, like, not useful information at some level. Have we considered what it would take to… and this might bleed over into another conversation, but what it would take to just rely on the retry processor
which will face the same question and doesn't have an answer for it. It just does retries right now, and I think I left a to-do there saying, we don't know if this is a permanent
**Aaron Marten** 20:02 Right. So, my strategy for now is I'm not using the retry processor.
In part because that would require
Sending the data down the… you know, keeping it in memory.
Basically, and a big part of this is, like, we don't want to have all of this in memory, right? Like, while we're waiting to do a retry, we might as well just drop it, because why keep consuming the resources? So what I'm… what I'm doing right now is I am using the effect handler delay data.
And just putting in there, you know, a pointer that basically says, okay, here's… we've got a bundle that we know we need to retry in whatever amount of time.
Call me back after that amount of time, and then just… just relying on that mechanism.
**jmacdonald** 20:49 Got it.
Cool, I think I can get on board, that makes sense. I would say that the…
memory question…
this is why I knew it was going to bleed over, and I might take a moment now to…
take us to Lowitz PR, which is about the fan-out
processor, which… which sort of… has some conflated issues right now with that same topic.
So, thank you. We've talked about your PR. I will review it, and that's a helpful pointer. Those are a couple of very helpful pointers.
By the way, on that, the collector SIG, the Go Collector SIG, is currently ironing out details about the partial success response, which is another thing that you end up returning from your exporter back to your
wherever, saying just metric information about how many points were actually successful and not. So that's all, to me, kind of like future work. Returning error codes, permanent error status, and so on. Okay, so into… to allow its PR,
And we'll just say we did that. Valid's PR, is huge, which is why I haven't reviewed it all the way yet. And he was very enthusiastic about it, and I know he's not here, so, we can just briefly look at how,
There's some questions here about… Well, this was the places where it bleeds over, so…
If the retry processor is designed not to hold any copies of the data, it's a stateless retry processor, so everything is in the data itself.
Including a stack of ACNAC intents, basically. So,
the danger of the retry processor is that you're going to send this data and then not hold onto it, and then it comes back as a NAC, and if it doesn't come back with its data, it is useless. The retry processor can then not proceed.
So even though we've got reference counts and so on, so that we're not duplicating memory when we clone, there's… someone's gonna hold that memory until they don't. And if they accidentally drop it.
the retry processor doesn't have a copy of its own. So that will… so what we're talking about here is how the further you get from your exporter, the less reliable it is to expect return data to come back to you, because anybody in the middle can drop it, and I think we should only really expect exporters to do that.
they're going to borrow the data for their purposes, usually, and then be done with it and return it to you. Whereas processors are going to change the data, and we don't want to ask people to remember what they came in with so that they can properly return it. That's just not a request.
Therefore, we may consider, How to…
Well, I think we might be able to solve the question with… with retry and not worry about memory.
Anyway, it's worth looking into, and I'll take a consideration for that when I'm looking at your PR, Aaron. At the bottom of this, I made a comment, because I think Lauett
maybe missed a detail about how ACK and NAC work. So my comment here is… is that we're hoping for this mode that we call primary, where the fan-out consumer… whose fan-out processor is going to have one primary where it sends the AC and NAC responsibility, and then it's going to have
One or more secondaries where it's just a fair and forget motion.
So the idea is you never need to do subscribe to, you're just passing the context to one output and creating fresh context for two more outputs, or whatever, if you have three outputs. So we shouldn't require any memory in the fan-out processor when you have a primary case.
or it's all fire and forget. But, if you have a fan out and you want to count X and X,
and only respond once the first act comes in, for example, then you would need to keep some memory and state, and so that's what Laoweth PR is kind of working on. So I think we can make some improvements,
And they will,
potentially impact… I think there's, like, a way that we can be a little bit more strict and careful and safe with handling these P data objects.
So that we… So that retry isn't so hard, basically.
I just wanted to touch on that PR. This will get reviewed over the coming days, and it's big because it has a lot of tests. It's not too… super complicated.
Okay, let's make sure that we put notes that we spoke about it.
And then I'll just briefly mention my PR, since I have a captive audience, maybe. I am working on, I would say, the final steps of getting our internal telemetry pipeline to a state of completeness at some level.
Not doneness, but completeness, like, it's minimally complete. And so, the thing that I want to get done this week is to encode scope attributes. Scope attributes are the open telemetry terminology for some keys and values that describe the instrumentation, and
It was introduced without
a ton of guidance on how instrumentation should use it. So it's been some years where we have this data type modeled, but no instrumentation patterns. So the instrumentation pattern used here
is the one that already existed. We have this entity concept that Laurent created. We have thread local variables with entity information in it. You can look up the current node, or the current pipeline, for example.
And there's a telemetry registry that knows how to map those identifiers, which are opaque.
FFI-safe tokens, map them back into attribute sets. So, my two-part PR here, this is the first one that's open right now. I've tried to split this in a way so that it was two easy reviews instead of one big hard review.
This is some refactoring for… just sort of, like, code quality. This formatting logic is… is dealing with Tokyo events, Tokyo metadata, and OTLP bytes, and I'm adding the ability to print a suffix.
The suffix… I'm going to show you the original PR now. It's closed until later, but just because it has some examples.
So, this is a log line here, and if you go…
this is already done with the current code at head since last week, but now what I'm adding is this piece at the end, which says this log happened, it's got an entity context associated with it.
And we're still sorting out some details, like, how do you… I don't want to print every log… every attribute on every log line, that would be a blow-up. I don't want that to happen, so I want some sort of short identifier for the console logs.
That refers to the pipeline. And then the idea is that this is a pipeline entity definition.
So, you know, it has,
The event name is Registry Define Entity. This is where, if you're just using console debugging, you're gonna have to go up in your log to find the definition of the entity.
But here we have the entity name as default pipeline, and this is subject to change. Laurent commented on it, it's not specific enough.
But the idea is that this is the definition, and all these attributes will be associated with that identifier if you have a way to look it up. So, that's what this log record here, was printed, because the console async
Andler thread as the telemetry registry, so it looks up the entity and it prints the keys, the short name.
This… this display at the top is what we get from the console exporter.
So that's a, remember, a component in the pipeline that just prints to the console, but it's receiving OTLP data, not log events from Tokyo. So it has the full OTLP structure, and it's printing a three-line
data with pipes, ASCII pipes, to connect the resource and scope and the logs. So, right now, my PR, this incomplete PR, is still handling singletons.
You'll always get one… three lines for every event.
one resource, one scope, and one event. In the future, though, I'm going to file an issue saying it's, like, a good first task for somebody to add batching at this level. If we batch at this level in the internal telemetry receiver, we should be able to put together multiple events per scope, and then print the scope once
Per buffer, if you will, if we want to do some batching.
Anyway, this PR, the first one, the one that's open, would like some reviews, but maybe only one of you, just, it's an easy one. And what it does is it sets up a log context.
A context function, which will be a thread local in the future, and prints it, basically.
That's me. That's my PR. Thank you.
Let's see, would anyone like to raise a topic, discuss a PR, or chat about anything Hotel Aero?
And if you don't, we get to end the meeting half an hour early.
All right, meeting's over. Thank you all. See you next time, which will be a Thursday in a week and a half.
**Andres Borja** 30:22 Thank you.
**jmacdonald** 30:24 Ping me on Slack or on Teams, anybody who needs me. Thank you.
