SIG: Java SIG
Date: 2025-11-27
Duration: 27 minutes
============================================================

## Zoom Recording Transcript

**Trask Stalnaker** 00:24 Hey again.
**Steve Rao** 00:26 Hey. Hey. Yeah.
Yeah, let's wait a moment.
**Trask Stalnaker** 00:32 Sure.
**Steve Rao** 00:43 Okay.
**Trask Stalnaker** 01:44 Cool, let's jump in, we could… Go to… start with NQ's… Topic.
**Minghui Zhang** 01:54 task.
Hmm. Yeah.
Can you hear me?
**Trask Stalnaker** 02:00 Yeah, good to see you.
We hear you.
You don't hear us?
**Minghui Zhang** 02:08 Yes.
Of course. But I can't share my screen because I joined this meeting with my phone, sorry.
**Trask Stalnaker** 02:17 No problem. I'll share.
**Minghui Zhang** 02:19 Yeah, so, let me open this link.
Give me a second.
So basically, we… I want to, discuss about the… the PR, you, you could just, yes.
Yeah.
Basically, we just have, concern about the complex attributes that we have, discussed before.
I, I tried to use the, extend data instrument, no, extend data to the provider to capture the, complex attributes, but I think it's not a good idea because, we have two, Modify many, many scenes in our, in our codes, and it looks like, Not… not so cheap.
So, sorry, so let me, give a, background about that. In the hotel 1.37, We have to capture the input and output messages of the generative AI instrumentation in span or in Log, and it depends on people's, users, users' config… config… configs.
If they want to, capture them.
in, span. So we just, we just record them, as, string, or, structure, structure object in the attribute. But now we can't… we are not support… supporting for the, com… Com… complex attributes yet. So we, how to, capture them as, as a JSON string.
In span. And if people want to capture them in log, we have… we could send the.
We could emit the, input and output messages, in log with, complex attributes, and it's, kind of, easier than, capture them in span, and that's the background. So, now I want to solve, resolve the, problem to capture them in span in a JSON stream. And that means I have to, In my before, solution, I had to, import the, Jackson library to… To finish the serialization while we, set the attribute to the spec.
And that's our, solution. But this solution have a, have a shortcut. We have to import an external library, and it's not allowable… it's not allowed by instrument… instrumentation API module, and that's the problem.
**Trask Stalnaker** 06:10 Okay, so… The… let's see, we have, So… Eventually, you're going to need to store them as complex attributes, right?
**Minghui Zhang** 06:34 Yeah.
**Trask Stalnaker** 06:35 Based on the semantic conventions.
This PR, that adds the incubating implementation, so this supports complex attributes on, spans and logs.
So this… This has been merged and will be in… The release at the end of next week.
**Minghui Zhang** 07:02 Oh, okay, I got that. So, at the end of next week, we could… so when will you replace the SDK library in the newest version in Java Instrumentations?
**Trask Stalnaker** 07:21 Generally within a couple of days after… The release, the core release.
**Minghui Zhang** 07:31 Okay, so… Pretty much.
**Trask Stalnaker** 07:34 very quickly.
**Minghui Zhang** 07:36 Okay, I mean, oh, let me have a look about the PR items.
**Trask Stalnaker** 07:44 You could also, work on the PR… Using the snapshot.
Of, you know, just build this locally.
Use the snapshot from… the core repo of the SDK.
If you want to get your PR ready for once that lands.
**Minghui Zhang** 08:09 Yes?
**Trask Stalnaker** 08:11 But if there's not a rush, so normally, This repo will release… One week.
The first week of the month, and then the instrumentation repo will release the week after that.
So…
**Minghui Zhang** 08:31 Yeah.
**Trask Stalnaker** 08:32 It's a… are you trying to get this into the next… Instrumentation release… Or is it… Or do you care if it goes for a month after that?
**Minghui Zhang** 08:46 Yeah, we, we sure. Yeah, sure, we want to merge it before the next release, Okay.
**Trask Stalnaker** 08:53 So, so then I would, Just locally build… This… We have a snapshot Repo, but it's actually… we just… it's not working right now.
It's failing our snapshot builds.
So, what you'll need to do is build this locally.
And then… Yeah.
Yeah.
**Minghui Zhang** 09:28 It's not a problem. I will do that. Cool.
**Trask Stalnaker** 09:31 Yeah, and you can get… you can basically do the PR, you know, and it's… Gonna probably be… Like, just ignore the failures, but you can get it ready and… and… presumably reviewed…
**Minghui Zhang** 09:51 Yes, looks like that the figures is not… import by my PR.
**Trask Stalnaker** 10:00 Oh, okay, yeah, what are… I didn't see these, oh, yeah, yeah.
**Minghui Zhang** 10:08 sorry, I have a concern about the… the complex attributes PR, food. I want to confirm that, could we use the… extended attributes, or create extended attributes in to our, normal tracer? I mean, could we just set attribute… set extended attributes into the normal span Rather than extended span.
**Trask Stalnaker** 10:51 You will be able to, after January 15th.
Oh, yeah. We're not allowed to stabilize it until then.
When… when we mark… when it's stable, then we will put it, on the normal tracer.
And the normal logger.
**Minghui Zhang** 11:15 Yes, but I think that's, that's a problem.
is. So, if we… we have, so now we have, we have to, set the… set the extended attributes into, extended span, right?
**Trask Stalnaker** 11:37 Right.
**Minghui Zhang** 11:39 That… that means we have… we couldn't, I mean, we couldn't emit the span… leads, that was, instrument in Java instrumentation, right?
**Trask Stalnaker** 11:56 I… you should be able to.
I'll show you an example. Like, we are using, Extended Log Record Builder.
In multiple places.
**Minghui Zhang** 12:12 Yes?
Oh, I know.
That means I have to, create, something like an extended twister provider in, our instrumentation, right?
**Trask Stalnaker** 12:32 No, it's already… you should be able to, so if we look… The tests here… Let me find an example… Oh, that's not a good example, let's find out.
Excited, I will share… So, you just get your normal logger provider and your normal logger.
and you call log record builder, so you… and then you can cast it to this.
Same first.
**Minghui Zhang** 13:54 I mean, how could I, emit the attributes if we want to set them into span?
**Trask Stalnaker** 14:06 Yeah, so Span should… let's see, we've got… So, extended… What did we do? I forget.
So… Yeah, that's a… maybe I might have missed… Something… maybe I only… Added this, let's see, log record… We've got extended attributes. I see. I think… Okay, good point. So this… only… adds… that to extended… attributes, it only adds it to the logger. Okay.
**Minghui Zhang** 15:52 Yes.
**Trask Stalnaker** 15:55 Okay.
Okay.
Let's see… I know that… Jack was kind of hoping not to create a bunch of incubating stuff, unnecessarily.
But I think this is a good reason. I think that if we add… That adding it to… Bands will unlock this.
So… and we do want usage and user feedback So… Will you do me a favor, and will you open an issue Here.
**Minghui Zhang** 16:49 He asked?
**Trask Stalnaker** 16:50 about extended attribute support on spans, and mentioned that you need it for this PR.
**Minghui Zhang** 17:01 Of course.
**Trask Stalnaker** 17:02 And then I will… yeah, and then I will… I will, I will take a look at that and, should be able to get that into this upcoming release, because we do… I think this would be a good thing.
Good usage and feedback for us.
**Minghui Zhang** 17:22 Yes. Cool.
**Trask Stalnaker** 17:24 Thank you for… thank you for explaining that to me. I was… I completely… I don't know how I'm… Forgot or missed that.
**Minghui Zhang** 17:37 Yes, thanks, thanks for your help, That… and that's important for me.
What more I want to, I want to, give a, give an additional point is that, if, I, I, I see… If we just, allow… allowed to, capture the complex attributes in span, we, even do… we… we will come to do better.
Before our normal choice provider or our normal spend, allowed the extended attributes to be set.
Because our spend is created by Instrumenter, and the chaser is, great, or is created in the generalization of the Java agent. So we couldn't… we can't modify it into the extended tracer.
And that means we couldn't…
**Trask Stalnaker** 18:53 So, it will be, it will be an extended, Logger and extended tracer, no matter what.
So, if you look at, It's… if the SDK sees the incubator on the path, it will build the extended version automatically.
**Minghui Zhang** 19:24 Mmm… do mean that if the, for the Java agent, when we, neutralization.
When we're… when we utilize it… initializing it.
The feature will be the extended feature.
**Trask Stalnaker** 19:47 Yep.
Always.
**Minghui Zhang** 19:50 Hmm.
**Trask Stalnaker** 19:54 So, that's…
**Minghui Zhang** 19:55 That's not so far.
**Trask Stalnaker** 19:56 Code. That's why this code works here.
**Minghui Zhang** 19:59 Yeah.
**Trask Stalnaker** 20:00 Extended Log Record Builder.
I mean, we do protect it with an instance of check.
But this is always… in the Java agent, this is always going to be true.
**Minghui Zhang** 20:15 Okay, oh, oh, cool, I don't, I don't know that.
**Trask Stalnaker** 20:21 Yeah.
**Minghui Zhang** 20:21 Thank you.
**Trask Stalnaker** 20:22 Yeah.
**Minghui Zhang** 20:24 So let me have a try. I will create a… I will send an issue in the Java repository, and I will do some… Have, have, have, have a try about the… With a snapshot.
**Trask Stalnaker** 20:42 Yeah, try it out with the log… on the log side.
And I will work on getting the span side, To the same place.
**Minghui Zhang** 20:53 Yeah, cool, thank you very much.
**Trask Stalnaker** 20:54 Yeah.
I do need to drop in 10 minutes. Huxing… no, no, sorry, Do we have Zooming? No, we don't have zooming.
Anybody want… To chat about this topic.
**Huxing Zhang** 21:24 I think Sumi is not in the meeting. Maybe we can discuss this next time.
**Trask Stalnaker** 21:34 Sure.
Sounds good.
Alright.
**patrickpok** 21:41 At Trask, I have a very small question, if maybe, like, I can, just ask it, I would say that tech teaming's place, if it is possible. Sure.
**Trask Stalnaker** 21:49 Of course.
**patrickpok** 21:50 Just once again, let me prepare the sharing.
Please come and share, so, close.
So, I'm learning this Zoom thingy on how to share.
Desktop… And then… yes, can you guys see my screen?
**Trask Stalnaker** 22:07 Yeah.
**patrickpok** 22:08 Yes, so it's a very small question, and I know you have the hard stop. It's about, like, tracing for batch operations. So, I'm just going to set some context. Let's say that we have, like, producers, different producers, like, they don't know about each other, they just produce some messages, and then puts it inside Kafka.
They don't know about each other, but let's say that they trace all the messages that they put inside Kafka, meaning that the message arriving inside Kafka is also already properly traced, have a valid header.
And now, let's say that there is one consumer that consumes all the messages of all those producers that don't know each other, and they apply some business logic. Here, like, is the green part, which is, let's say, like, they do, like, an uppercase, business transformation. They text the messages, just do the uppercase operation.
And then it inserts it inside, like, a database. Let's say, like, for example, Redis, like, for the… using the latest API.
or anything from the incubate… or from the OpenTelemetry instrumentation, like Cassandra, etc. And this flow will work as of today, meaning that from this, we will be able to see the trace.
From all those producers, which they have their own trace, and they don't know about each other, and the consumer who takes all of them is able to create those trace and this path all the way from the producers, all the way from consuming, as well as inserting to the database. And we can see, like, even, like, the insert statement, the SQL, or the insert operation.
And that is very clear, like, we can see those. Unfortunately, if the problem is, if we show this to any, like, database expert, they will say, this is not… this is very beautiful in a tracing point of view.
But this is not good in terms of the database point of view, because you are making one insert, or, like, one connection, or whatever, and one write operation into the database. So, they obviously ask the producer to, at some point, batch all those messages, and write one insert statement.
So, in which case, and which is absolutely possible from the code point of view, but in terms of the design, and in terms of the tracing and the observability, and this is where we'd like to ask you guys for advice.
Then, how do we visualize this in terms of trace? Because we don't have this kind of trace anymore, because this was… which is very normal, like, one trace, one transformation, one insert, and this is very traceable. But now we have this, like, the consumer batches them and writes ones. So, what is this… what will be the information of this trace? And that's my question. First of all, did I ask my question, like.
correctly. Did you guys understand the question?
**Trask Stalnaker** 24:40 I think so. I think I understand.
**patrickpok** 24:42 So, trust, from your experience, what do you think would be the, I would say, the correct way of, like, representing this from a tracing point of view?
**Trask Stalnaker** 24:51 So this is where SPAN links.
are useful.
And if you look at the messaging, there's… if you look at the messaging semantic conventions.
Is the one place where… Spam links are used heavily.
Already.
And, they're specifically because of the, kind of batching nature of a lot of messaging systems.
So… I think you'll find… Kind of the modeling there, but briefly…
**patrickpok** 25:33 Let me read.
**Trask Stalnaker** 25:35 Briefly, what I would do is the insert batch span, Ideally, would have spanned links, to the other… The places where it kind of got merged in from, so it can have a one-to-many relationship there.
**patrickpok** 25:54 Okay, okay. And the trace of this batch insert itself will be a new trace, but it has the links to all the one-too-many messages, am I correct?
**Trask Stalnaker** 26:07 You could model it that way, yeah, you could, yeah.
Yeah, if you look at the messaging, that's sort of what is happening with messaging batches also.
**patrickpok** 26:19 Okay, and let me… let me read that thoroughly. Like, I had a… I had a feeling that we'll, like, I should be investigating that route, but now that you confirmed, like, I'm going to thoroughly read through it and try to come up with an example. So, thank you so much, Rask. Yeah.
**Trask Stalnaker** 26:32 Sure thing.
**patrickpok** 26:36 I'm just going to stop sharing, etc. And apologize for hijacking the meeting.
**Trask Stalnaker** 26:40 Oh, no.
**patrickpok** 26:42 Nothing else from my side. Thank you, guys.
**Trask Stalnaker** 26:45 Cool. Then I will see you all in 2 weeks.
**Steve Rao** 26:49 Yeah.
Yeah, enjoy your holiday.
**Trask Stalnaker** 26:53 Thanks.
**patrickpok** 26:53 Happy Thanksgivings, Rask.
**Trask Stalnaker** 26:55 Thank you.
**Minghui Zhang** 26:56 Yeah, happens as smoothly.
