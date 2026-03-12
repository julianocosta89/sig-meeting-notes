SIG: eBPF instrumentation
Date: 2025-08-06
Duration: 65 minutes
============================================================

## Zoom Recording Transcript

Rafael Roquetto 00:01:00 Hi. Tyler.
Tyler Yahn 00:01:01 Hey, Raphael, how's it going.
Rafael Roquetto 00:01:03 I'm good. How are you?
Tyler Yahn 00:01:05 Doing? Well, yeah, just chugging along. Yeah.
Rafael Roquetto 00:01:10 Yeah, it's already. Wednesday. Man.
Tyler Yahn 00:01:13 I know it's already August.
Yeah, yeah, it's happening. Yeah.
You got any fun plans for the weekend.
Rafael Roquetto 00:01:24 Not much, maybe. Just go to the mountains. How about you.
Tyler Yahn 00:01:29 Yeah, probably just go to the beach. Actually. So the other yeah.
Rafael Roquetto 00:01:33 Sounds good to me. Hi! Nico.
Tyler Yahn 00:01:36 Yeah.
So I was looking at the agenda. I was just added, what we had from last time with Nimrod giving a little Demo, and then do a little review of Prs.
But if you guys had some ideas or topics, you wanted to add.
Go ahead and add those as well.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:02:07 Sounds good. Mario's away this week, actually, next 2 meetings as well. I think he's back the last week of August.
Tyler Yahn 00:02:18 Okay, yeah, that sounds good. Then, I won't be waiting.
Yeah.
Well, cool. Yeah, we could. Actually, I probably don't need to start sharing my screen.
yeah, I guess I guess we could just jump in here. Then I see Mattia and Nimrad you've also joined. If you haven't yet. Go ahead and add your name to the attendees list, Nimrod. The only major thing I had on the agenda was having. You give a little demo of the Hotel Demo. If you're still able to do that, that'd be great. We can start off doing that.
Nimrod Avni 00:03:08 Yeah, for sure prepared a couple stuff. But then we can like go through, I think, a lot of the stuff that we encountered, and like all the I don't know if we had like major differences in exactly what we did to showcase Delta Demo, so I'll just share my screen. One second.
you good! You see my screen.
Tyler Yahn 00:03:40 Yeah. Yep.
See? A. Yes, a dashboard. So, yeah.
Nimrod Avni 00:03:45 Yeah. Yeah. So just quickly, like something that me, and have been working on basically taking the hotel demo, there's like a open, open telemetry demo.
Where is it? I think there's like a yeah, it's basically like a set of micro services communicating with each other. I think it's based on this is like, Google, like, they call like, online boutique, something. It's like the the micro services demo, and yeah, just the this report, like contains a couple of them. We also kind of did a a bit. A couple of modifications on them mainly added a bit more of like a database communications to like showcase, the the full range of ob abilities. And also did like couple more stuff that I'm not sure if they were were necessary, or if they weren't like like removed the like, the manual. All the applications here are kind of manually instrumented.
Basically, I don't know. We can look at like, I'll take something that I know the language of, not ruby. Let's go like recommendations or something. And yeah, basically, like, everything here is kind of instrumented with the hotel Sdks recommendation service.
Yeah, I think basically gonna open and telemetry.
Yeah, I guess it does like kind of you know.
instruments the whole like all the services I kind of. I removed a couple of them, because then I saw that some of the context propagation stuff worked better, better. I think I talked about it a bit with Nicola about basically the the way that the services, generate their own trace and spend ids, and they read it from the headers kind of clashes with how like, how we do it! Am I correct Nicola saying that?
Yeah. So that's like something interesting that we might want to consider, you know, either like patching or having some sort of way to like, override it, to make sure that people that do have instrumentation can like also have it like basically would, we will. I don't know either communicate better with the the sdks or or the way that they like extract and and propagate trace context. Yeah. But like, very simply like. We deploy this on kubernetes and kubernetes. We ran the ob alongside it, sending traces in this case to core logics. But of course, anything that you want and yeah, like a couple like it took like a bit of trial and error. It wasn't like it wasn't.
We got a lot of insights at first, st but we kind of needed to configure exactly the stuff we need. And I think we also discovered a couple interesting like bugs. I don't know if it's like bugs or just missing things from it, but most of the stuff kinda worked really great. I know we can look at some features we have in in corelogic sector service catalog catalog. Basically, you know, having full this, this is like relying on on spend metrics that obs exporting. So you can see, you know, basically all the services, and like how they export the you know, on the spans. And you can see stuff like. I don't know.
If you look at shipping, we can look.
you know, it's like per like, I don't know per type of round and all that stuff.
We can look at stuff like. I kind of made example of the stuff that we we did recently with like database calls like seeing stuff here, like errors in in all the Dbs stuff like postgres. And and my sequel, and I don't know. I think this is yeah. Also errors in Redis with like the dB namespace, like the actual database that Redis is connected to also propagating in the span the the Mongo stuff.
and yeah, did some more. There's like some interesting thing about like the distributed tracing that some of it some of it works really well, but some of it. Kinda because you see here that this is kind of the same trace this is, if it will look like at the actual spans. It's basically.
we have the shipping and that it propagates context correctly to the quote service.
And we also have, like, it's kind of disconnected here from the the email service, the but the actual, like checkout service, has the like, the remote link that we like add, I think, with like server, like client address and client port, but it doesn't fully propagate traces.
But that might be something that I just explored, I think, with Nicola so explored it with Mattia about let me, I think it's here. Yeah, I I because I saw this log in my like ob my ob instance, basically this one.
And so cops. Yeah, yeah. So like we did, we tried to like explore and see if if you know, stuff like this, like all the C group stuff is mounted correctly. Just that we have C group v, 1, and we try to explore like, if if it's a actual prerequisite to sock up you know type programs. And I'm not really sure. So I don't know if if anyone has a bit more, and that I think that's something that might cause issues with context propagation. Because I think most of the context propagation we have now is either the the go one, like the one that writes the headers or the like, the local one that does like, because we're only running on 2 nodes. I'm guessing a lot of the services are deployed on the same node and context propagation that way. Kind of works. But I think between the different nodes might not fully work.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:10:13 Yeah, I think for that, you need the this, this. So cops thing.
Yeah, I actually don't remember personally, like, I think some community member hit an issue with C group v, 1. And they added this before we donated a code.
We didn't think much of it. I think the original code would just trying to get onto it.
Honestly, I don't know if it's a limitation. Maybe we just need to make it work with seekers. We want.
Nimrod Avni 00:10:47 I mean, we can. Also, I think we can also up. That's probably because we have some old. I don't know how old machines are probably like couple of years old, or like the version will be the.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:10:59 Maybe it's maybe it's good. You have that because we can make it work as equal as we want.
Nimrod Avni 00:11:04 Yeah.
Mattia Meleleo 00:11:05 It seems to be distribution that doesn't have the C group v. 2 is Amazon Linux, because we are using exactly that one exactly on version 5.1 0.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:11:15 The day.
Mattia Meleleo 00:11:15 Newer one should have it already. The B 2.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:11:19 Okay? Maybe we can check that.
So you said, 5, 10 is what you have. Amazon, Linux.
Mattia Meleleo 00:11:27 Yeah, we have Amazon Linux, not the 2023 one, but the previous one, which is 5 dot 10. Yeah.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:11:34 Okay. Alright. Yeah, we should try that. I'm curious now, because I can get it going on a Vm. I hope.
Nimrod Avni 00:11:48 That's gonna be like, that's
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:11:51 Yeah, I have no idea.
Nimrod Avni 00:11:52 Improve. I'm hoping that probably will improve all the you know, all the context
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:11:59 Oh, yeah.
Nimrod Avni 00:12:00 Like, he said.
I'm guessing because stuff like this here like that I'm I'm guessing this is local we can look at like I don't know. Let's look like here, I'm guessing we'll have, like, the node is like, yeah, 80 55. And my guess that yeah, it's kind of the same node here. But if we go to checkout, that's like a different node, so that that might be like the you know the issue there.
But yeah.
Besides that, I think that most of the stuff like work really out of the box, and did like complete observability on everything which is really cool. The only like minor stuff that we encountered are with Kafka. That's like, if we look at let's do like messaging system.
Not like messaging system. Kafka, remove this like, I think we can look first.st This like stuff like here, where the destination name is is Star. And I looked at the code a bit. I think it's some like Kafka Api version above, above a certain version. They don't send the topic anymore. They just send some id. So I I had like an idea of basically doing some similar type of enrichment that we like the reddest one. Basically, I don't. I don't know if it's exactly when you connect like, if the when the consumer connects 1st time to Kafka, or is it happened like continuously. But there's like this meta metadata message, that kind of maps, the Id to the actual name. And we can do like that enrichment in user space.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:13:53 Cool. Yeah, alright, yeah, yeah. That's a good idea. Yeah, yeah, that's right, because they're yeah.
Nimrod Avni 00:13:59 For that.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:14:01 Yeah, I remember, like, yeah, in the protocol, they ended up at some protocol version of that of the send message. Whatever is the produce, whatever they call it. They.
they optimize that. So it's just an id that means nothing.
Nimrod Avni 00:14:20 Yeah. And then about the wait. This is like just some diagram of the architecture. We change it a bit. But just to show.
Like, we also think this kind of connection is also broken. I think, like we know, I think I know what the issue is, because we had some similar issues with our agent.
when, specifically, like Kafka Java clients over some version.
do some funky stuff where they kind of split the packet where they send like the header in one packet, and then the rest of the body in another, and then we like you don't classify it so maybe like where we thought like doing the same thing we did with like Mysql and and Postgres, and like doing like the kernel space inference that will probably solve it. I'm guessing.
At least, that's what we hope, because I think that's like, under specific like above, like 2.8 or something that happens And also here, there's some like stuff with, maybe I need to export this more because I saw stuff with what sort of yeah, like the checkout service.
Basically it it the there are way fewer publishes than like fetches. But this might be caused because of like batching, because each like operation also takes couple of minutes.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:15:59 Minutes.
Nimrod Avni 00:16:00 So I don't know if that's like intentional, that's like it's a producer batch that, like I don't know sends the 1st packet, and like, I'm not fully sure. Maybe I need to. I don't really know how all the specifically the uprobe stuff with sorama works.
That's also gonna be something interesting, too, that we want.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:16:22 Okay, that one is in Goa.
Nimrod Avni 00:16:25 Yeah, this is specifically in go. And I think that's I don't know if we I don't know if we document anywhere that's like.
what instrumentation it is. But I think it's that's a Sarama. I can look at the code.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:16:39 Yeah, I think, so, yeah.
Nimrod Avni 00:16:41 And where is it?
Think it's check out.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:16:54 And producer.
I'm guessing. That's oh, it's the yeah. It's the newer version of Sarama. Thankfully.
Nimrod Avni 00:17:02 Yeah.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:17:04 Interesting.
Nimrod Avni 00:17:06 That's yeah. And that's like that.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:17:11 There might be a bug there like. That's pretty long time. 9 min.
Nimrod Avni 00:17:17 Yeah, I I don't know if yeah, I don't know if that's like a bug or that like, it's like intent. Maybe we can. I don't know. I'll try to set like some minimum producer batching size, and that will other work. I don't know.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:17:33 And what are the Nas that you're getting there.
Nimrod Avni 00:17:36 And a yeah, I it's like, it depends on, like the the view of core logics. Basically, we have. This is like a span view. And that's like a trace. And and they basically means like, here we try to show like the root span. And in some cases the discovery.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:17:55 Yeah, it's not found. I see.
Nimrod Avni 00:17:57 Like usually like it looks like the span, but that it's still like one span takes like some.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:18:04 Very long. That's very long.
Yeah.
Maybe we misinterpret the time or something. I don't know but it could be like what you say, batching, although it's pretty long batching. 10 min to batch.
Nimrod Avni 00:18:15 But, like, on the other hand, like each spend, there's like a almost a 10 min difference, and it takes 10 min almost that might like make some sense of like, you know, it might actually be batches.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:18:30 Maybe. Okay. Maybe it's periodic or something.
Nimrod Avni 00:18:33 Yeah.
Yeah, there's some time out, maybe in the client. I don't know.
yeah, I I think. Besides that like we we want to, you know, keep like improving this. And like ideally, you would want want to see something like, you know the full, you know the full trace from everywhere. But we still have some stuff here that.
like we know we can do like we can't even like we can't like propagate traces. Let's say here like this, I think typescript service, and it communicates with Grpc, which is something that we still don't support. I think there's some other stuff with grpc, like, yeah, mainly.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:19:16 Yeah, we'll get that. We'll get that work.
Nimrod Avni 00:19:18 Yeah, and we'll get annual. I think there'll be, you know. Maybe we can even do something like that. And I know. Put it in in Jaeger, or something that's like open source, and we can have it continually, like monitoring it. It helps us, like, you know, in in core logics like me and Mattel, like, kinda monitor ex exactly what? No.
what what you know, what features does ob has. And when we can like show. Okay, this is like a very complicated microservice architecture, with all like A, B and C types of databases and communication and languages, and make sure that it all works.
I know. I thought this would be something interesting to show, and it will help us like kind of close the gaps of what we want to do.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:20:04 For sure. Yeah, it's just a matter of time.
Nimrod Avni 00:20:07 Yeah, for sure. And that's gonna be.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:20:09 That's great work guys like you found a lot of issues.
Nimrod Avni 00:20:13 And you, and like, by the way, and Nicola and and Mario and Rafael really helped us with a lot like I. Also, we discovered like that the issue with the the restarts of the Kubernetes and lot of other stuff. And that's gonna be, you know.
Thank you guys, for all the help.
Sure. Yeah, I think that's that's it for me. Regarding that.
Tyler Yahn 00:20:38 Awesome. Well, thanks, Nibroad. I've taken some notes on some of these issues, just so we don't lose track of them.
I think we could also maybe put them into the issues themselves. But yeah, I think I think we can at least start with this.
so yeah, cool. If you. If I miss any, please go ahead and add them here as well, and then we can keep track of them. I think. Yeah, I think probably building out issues for each one of these is probably worth worth looking into.
Nimrod Avni 00:21:11 Yeah, yeah. Open it?
Tyler Yahn 00:21:14 Cool.
Okay, next up, I wanted to do a little review of the open Prs. We can jump in here.
Looks like there's a few more. So there's this test server components that still needs, I think, to be taken a look at just for the upgrade.
Oh, no, this is to exclude it. That sorry? Yeah. And so it's just it's more configuration. So, Nicole, you are assigned. But you're also leaving soon. So I imagine if you don't get to this I can. I can take a look at this as well.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:21:48 Yeah.
Tyler Yahn 00:21:49 Okay.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:21:50 So skip this repose all together, and maybe that's the best.
Tyler Yahn 00:21:54 Yeah, I think. Well, I mean, at least this portion of the repo right.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:21:59 Yeah, that's right, yeah, yeah, yeah.
Tyler Yahn 00:22:02 Okay?
And then
Nimrod Avni 00:22:07 Next up the initialized host. Info metric on 1st span.
Tyler Yahn 00:22:12 This is something I think we talked about last week as well. I think this is just a work in progress, Nicola. You had been working with them. It looks like there's some feedback. Yeah.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:22:20 Yeah, I think he's almost done. I think.
yeah, I think, yeah, I'm thinking, I don't know what's the hold up. I really need to think, Jorge, he's he works in your phone. So I think it just needs to be completely resolved. And I think tests were added. Everything else looks good. It's just little bit to get it over the finish line, I think.
yeah, it doesn't look like it's too far off. So yeah, if he works at Grafana. I'm.
Tyler Yahn 00:22:59 Yeah, I'm not as worried about it getting eventually pushed over. But yeah, okay, okay, cool.
next up this, it's a dependency updates. Oh, I think I was looking at this yesterday. It's just the tests are failing on this.
yeah, no. It does look like something needs to be updated. That's right.
Yeah. So it looks like, maybe the way we're interacting with the collector or using the collector Api, I haven't looked too deep into this. I don't know if others have.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:23:32 Was this the Kubernetes one, or is it the collector? One l. Collector.
Tyler Yahn 00:23:36 This is the collector. Yeah.
looks like there's a compile error somewhere in here. This is not really that helpful.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:23:45 Profile, no expert data for P data, p profile.
Tyler Yahn 00:23:53 Huh!
I imagine this might mean that it needs I didn't look at too closely at this.
See? It may be that it's only like a partial upgrade, and that there are other collector. No, okay.
it is still updating Pda.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:24:10 Maybe it's the P. Data that somehow has an incompatibility. There.
Tyler Yahn 00:24:16 Yeah.
I mean, there's I'd be very shocked if the collector released something that this was incompatible with this. But I don't.
I bet you. I feel like it has more to do with what we're doing with the P data structures is probably what's going on. So I'll have to. Oh, wait a minute. Did it say, profiling, yeah, I mean it said profiling, yeah, okay, well, there you go. There's your problem.
that things changing all the time. So there's there's probably just an Api change that we need to include here.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:24:46 Yeah, yeah, probably.
Tyler Yahn 00:24:48 Yeah, okay.
Alright. So just I'll take a look further, I imagine, pull this down and then just run this locally. It'll be very obvious where the where the fixing is.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:24:58 Yeah.
Tyler Yahn 00:24:59 Yeah.
Okay, Mark, fix invar substitution for open telemetry operator.
Think this is something he's opened yesterday. It looks like Nicola has already reviewed it.
Test issues.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:25:15 Yeah, okay. So it might resolve them, I guess. Yeah.
Alright.
Tyler Yahn 00:25:19 Okay, so it just needs more review.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:25:21 Yeah, yeah.
Tyler Yahn 00:25:21 Mark anything you want to say about this one.
Marc 00:25:24 No, I think I fixed the linter. And yeah, let's see.
Tyler Yahn 00:25:32 Okay, yes. Just needs to review.
Marc 00:25:34 Cool.
Tyler Yahn 00:25:38 Okay. Bpf infer packet type based on server port. I saw this one open up, I think, yesterday.
Mattia Meleleo 00:25:47 Yeah, this has already been reviewed by Nicole and Rafael. I'm addressing the review comments.
yeah. Should be ready soon, I think today or tomorrow.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:26:02 So.
Tyler Yahn 00:26:05 Cool!
No blockers on that right.
Mattia Meleleo 00:26:08 No no no blockers.
Tyler Yahn 00:26:10 Yeah, alright.
Next is just an automatic update. I saw this. The Ci was being flaky this morning. Oh, looks like it got its past. So this just needs to get merged. So not much to say there.
Same here with the Mongo driver, the test for being a little flaky. But I don't think there's anything wrong with that this one. I didn't look at this yet, so it looks like there's a remove. Additional valid char config option looks like it's already been reviewed. So it doesn't really matter from my.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:26:42 Yeah, it's it's this classifier. It's it's interesting, this apparently. Jorge proposed this classifier to the auto collector as a processor. But then people had different ideas. But now people come back. Somebody else is working on the same thing. So it seems like the code we have here is gonna end up being part of the collector as well.
Oh, was confused about the I don't know. Like the change there was this change, for this is valid character.
I was mostly just kind of looked at the code, and I noticed that there was an additional loop. But supposedly this loop is actually faster than the or statement in go. I was a little bit surprised.
so it was a little bit back and forth. I think he's just trying various benchmarks to make sure it didn't regress performance. But it was something like this. So And there's these characters. So this or statement sees great on the name. Whatever used to be a little bit bigger there was like, or dot, or underscore, or something.
Tyler Yahn 00:27:49 Hmm.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:27:49 So he added, this default config additional valid charge, but then thought that would be slower. But supposedly it's not so. I think he's trying.
Rafael Roquetto 00:27:57 So, strange. Yeah.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:27:59 Yeah, I think he's trying with a table now that you can just hit it. That should be the I don't know better. But who knows? Maybe the memory load. Somehow it's it's slowing down. So he's experimenting with like ensure that it doesn't slow down this implementation.
The code is sort of ugly. The way that this cluster does the kind of like transformation. What this do does is actually reduces a high cardinality route into a low cardinality route by figuring out which parts of the URL can be compressed can be can stay like But it's necessarily complicated, I guess, because we were really concerned about performance.
like typically you do is you do a string split by the root components, and then you check each one of the components is not gibberish, which means like it's not.
doesn't contain numbers and various combinations that would not make sense like ids, sort of thing.
and then compose it back into a low cardinality route.
But it's very slow, like, if you do, string splits and all these things and compose back strings, it's it takes a lot. It does a lot of allocation. So it's very slow. So this has been tuned to death.
but apparently the collector. They're taking this. They reference this code, but they're I just asked them on the on the Pr to benchmark because they took. I mean initially, when I 1st wrote that I did a string split and then recompose it, and then Mario called me on it and said, Well, hold on a second. This is gonna run in every route we process like So it's just an improvement, I think.
so I don't know like this is related to. Maybe something you told me, Nimrod, that there's a there's, I think, get quote wasn't recognized as a value route by this heuristic thing, because I think T. And Q don't come together very often in regular words, and.
Nimrod Avni 00:30:16 Like a couple of like manual route patterns in in the.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:30:22 Exactly.
Nimrod Avni 00:30:23 The demo. And yeah, get quote, I think was one of them.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:30:26 So Jorge actually trained a new classifier. So the classifier that I initially found that was like somebody on the Internet, Alessandro, somebody that that had this. This classifier was trained on regular words like, not specifically related to roots and patterns of web Apis, and so on. But then Cork actually used a different corpus, something that's specifically targeting like Apis, and so on.
So he's already contributed the new Corpus. And so this classifier is a lot better now.
But I think it's just this performance questions here.
Tyler Yahn 00:31:10 Is there a reason that it's creating a valid chart table for each instance of this, instead of just using something like a file level, variable.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:31:19 I don't know.
No, I haven't looked at this new implementation. I approved the previous one.
Tyler Yahn 00:31:25 Oh!
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:31:26 So, but I was. I was shocked first, st that the or statement was slower than adding a loop, which she added.
Rafael Roquetto 00:31:36 Could it be not your statement about this range and the fault config that it's
Tyler Yahn 00:31:41 Well, it's not a it's not. It's not a, or statement versus a loop, though right.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:31:46 Well, I mean.
Tyler Yahn 00:31:47 Index.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:31:48 Yeah, so what I, this is, this is the final version. But what was before? Is that the way that we had the code before. This might be like if you open the history of the file. Maybe that's an easiest. I think. He merged that in layers change I missed it. Yes, this this particular thing.
So this was the original version. That's 1 of the live 1 41.
And so this, apparently the way is with this or statement. It's slower, supposedly, than taking these additional characters and putting them in this additional valid chars, and then.
Tyler Yahn 00:32:27 I mean, I think that makes sense right? Because each one of these is a as an operation, right to make that distinction right? So you're looking at a CPU cycle per or and so the index is itself. I don't know. Maybe I mean, it's just. It's retrieval, probably from a local registry, and and then it's really quick. Look up right? And so I mean, I.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:32:53 The table right, the table right.
Tyler Yahn 00:32:55 Yeah, yeah.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:32:56 Yeah, but I I don't understand why this, the way it was line 1, 41 was the way the code was, and then he changed it to a loop.
So he took out those extra or statements, the dash underscore Dot and and the space. Yeah. And he turned them into this loop, which is online 144. So 144 did not exist. So he moved these 4 characters into this additional valley chars.
And so supposedly doing. The or statement is slower than doing the additional value charts. So if you take those 4 and you put them in this array, and you range over it. That supposedly is faster.
which.
Rafael Roquetto 00:33:40 How? How has he rate benchmarked this? I find this very strange.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:33:45 I mean I unless the go compiler is doing something stupid with your statements. I I can't believe it. Yeah, I don't know like.
Rafael Roquetto 00:33:54 Maybe we should ask him like, how is it being benchmarked? And maybe.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:33:59 Well, he committed a benchmark now. So okay.
so he's got a benchmark now.
So, but I'm curious if maybe we're not hitting that path or something. Maybe he's mistaken. Maybe it's like the cache, because this cache is also the.
There's an allow you cache also, which the every cache makes sure that, like you have an answer for a previous, but like clustering, you get the answer back right away. So maybe there is no difference, because he's hitting the cache.
We should run a benchmark without the cache or something like that. I need to see this because I I actually I was like shocked. I was like what you're gonna write a loop, even if it's unrolled, it's still gonna be much slower, because it's gonna have to do the bound checks, and all this I don't know.
Rafael Roquetto 00:34:49 And I, I assume, like the final code is gonna optimize the hell of these our statements. Like I, I compilers. We do so much shit in terms of batch. I don't think it's gonna do one. Our statement per time. It's probably gonna just do in one or 2 operations. Everything altogether. I mean, we can see the generated code later.
Tyler Yahn 00:35:09 Yeah, I mean, that's the other thing I would look at right is just looking at the the actual byte code, right? Or the instructions.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:35:15 Yeah.
Tyler Yahn 00:35:16 That's right, like, yeah, that that might help clarify.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:35:19 Analyze it.
Tyler Yahn 00:35:20 Yeah, I, yeah, I don't know.
I'd also, yeah, I, yeah, maybe try to reproduce the benchmarks because that may help clarify. Maybe there were like some things staged that weren't getting actually tested, or something like that.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:35:36 Yeah. My guess is that he's hitting the cache, and there is no actual difference in the version, because the he's he's getting a fluctuation.
Yeah.
Tyler Yahn 00:35:52 I think that that's probably a good guess as well like trying to isolate this is is going to be important to show that also without cash.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:36:03 He's doing without cash. So yeah.
Tyler Yahn 00:36:08 Yeah, this is also.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:36:09 So the ore chain, supposedly, is the slowest or very comparable to the loop.
Tyler Yahn 00:36:16 Wait! Wait! This is this is just one instance of a benchmark. He's oh, this is no, this is not. You shouldn't do that.
I mean, we're looking at. We're looking at differences on the order of less than like 3% here, right like this is really small. And you have statistical deviations in like the machine just running the benchmark. So you need, you need like statistical samplings. I bench. That is what we always use for this.
Yeah, I would. I would highly recommend that this is used so essentially, what you use is like.
yeah, this says comparisons. But it also does single runs where, like you run 10 of these, and then from there it'll give you a statistical like sampling of that, and like you'll be able to tell if you actually have something significant. There.
Yeah, I'd be very surprised if there's that big of a difference. Once you start looking at yeah.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:37:14 Yeah, maybe there's no difference, actually. And maybe that's a that's a good answer, like the loop is simplest to understand what's going on.
I mean, cleanest in terms of code.
Tyler Yahn 00:37:27 Yeah, I think that's fair. I think that that's a good justification. But I would definitely be suspect of single benchmark runs trying to, even if they're over long periods of time like that doesn't necessarily tell you much.
Yeah. And I mean, obviously, like.
if you can get rid of these allocations. That's where the actual performance is gonna come from. But.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:37:48 Right? Yeah, it's it's low, right? The allocation is low, but still could be better. But I like you're still replacing the original string. I think you still take the original. You take original string, and you're producing an output.
Tyler Yahn 00:38:05 Yeah, so there's going to be some sort of.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:38:06 Translation.
Tyler Yahn 00:38:07 Yeah, yeah, some allocation there. But yeah, that's definitely yeah.
Okay. So it's also pretty new. So don't wanna nerve type too much. We can keep looking at this one. Thanks for taking a look already. Everyone. And then we can keep going.
Okay, that's it, for pull requests going back to the Doc, or I've got Raphael. You want to talk about copyright headers.
Rafael Roquetto 00:38:34 Yeah, real quickly, because Mattia brought up a good point in one of the Prs where the the headers are inconsistent. And I know that you, Tyler added, like you were the one whether you went on, and all the headers. So you fix them all so I was just wondering. Is it possible?
Excuse me to add some sort of a Ci check that verifies the headers and make sure that they are compliant? Or is this something we we do. We have that already, or.
Tyler Yahn 00:39:08 Yeah, we should have that. Yeah.
I thought I included that in the Pr.
Mattia Meleleo 00:39:13 I think we have that, but for only for go files and some other extension. But we are missing that for Dot, C and Dot, H.
Tyler Yahn 00:39:23 Yeah, you are 100%, right? Yes, that just needs to get updated. That's because I copied this from ago project that didn't have any C code in it. But yeah, that yeah. Good good question. And we should do that. We should fix. That shouldn't be too hard.
Mattia Meleleo 00:39:39 Also we should make sure to exclude the all the Linux and the Bpf. Bpf. Core headers and that kind of kind of stuff.
Tyler Yahn 00:39:47 Yeah, yeah, and you can just do that. Obviously like this could probably go get cleaned up. But yeah, I mean, you can start making exclusions here in this find command is where this is being done. So you should be able to do it from here. Yeah.
Mattia Meleleo 00:40:00 Alright!
Tyler Yahn 00:40:02 Yeah. And this is, I think there may be like golang Ci lint checks that do this as well. I think somebody pointed that out. We've always used this just because it was really easy. But if it starts to get too complicated, we could look into using something else as well like, I'm not like married to this.
But yeah, Mathia, the good question definitely would would be happy to see a Pr to try to update this for the C code. Yeah.
Okay. And then, Raphael, you also wanted to talk about sock Ops message stream, vert programs.
Rafael Roquetto 00:40:42 Yeah, just because, like, we briefly mentioned it earlier. So on Matthias. Pr, I like how he's tracking the the connection lifecycle. You know, we don't need this case of accept and listen calls. We're using K probes, which I think fits very nicely with what we how we currently have things structured. But I just wanted to mention, just for future references. No action item or anything like that. I've been playing with these different kinds of Ebps programs socket programs mostly message sock message and and string parser and string verdict programs So these programs. They are attached to sockets.
and the cool thing about them is that they about to the life cycle of a socket, and obviously especially for Tcp connections.
If you're tracking requests and and whatnot, it makes it very trivial to figure out the life lifecycle of senior connection requests. I mean, if this actually is being reused as a different matter.
And but when, when, like, we have a lot of lru maps where we start information, this gives us a a way of literally know when the socket dies, all that part information, connection, information dies with it and with the stream verdict and message programs.
Because one is ingress and the other is egress driving the socket direction or the package direction is also trivial. So yeah, it's just like, if you guys ever I don't know if you've ever played with that, it's something that I've been messing with in the background.
If it's useful. I just thought I would bring it awareness or something. It doesn't really fit our model right now, so it wouldn't be that easy to adopt. But you know something to bear in mind.
So I found that they're really useful. The other thing with the these programs especially like soft message and string well, sock message, it operates in app level payloads. So you're not dealing with packets. So it's also really easy to like deal with. A big Http requests. For instance, right? When you do, it spends multiple packets. You don't have to worry too much about that.
And on the other on the other. Ingress is also very easy, easy, even easier to to deal with requests, because the socket, the string verdict and and parser programs they go hand in hand. So the way they work is 1st the parser program runs and then it ships to the verdict program. So what is the the parser program, basically. Lets you tell the kernel, do I have enough data to parse this back? This data, not package this data? And you can say yes or no, and if you don't have enough data, let's say you haven't found the end of a Http. Request the frame boundary. Whatever you can just say to the kernel, Hold on, and then the kernel takes takes care of buffering this for you, so we don't have to do manual buffering like we do at the moment. And then once you say, Okay, here's the boundary good. And then it passes. Once you okay, that it will pass the a second frame or Http frame. Whatever frame. Grpc, whatever you decided, it is to the string verdict program the verdict program, then the the the original intent right is to be able to look at something and drop or accept. That's why it's called verdict. We don't have to do much into it, but it lets us at that stage parse, for instance, I was using to to parse Http requests no encrypted, and it became really easy. I don't need to know if the request is is done or the headers. In that case, that's what I I just have a framework which contain the Http. Headers, and it makes it very, very easy to extract those. So these are interesting programs. They have cavets. For instance, if you're parser program, never says you have enough has a bug, and it never says, Okay, buffer, more, buffer, more, and never returns it to the verdict. You install the connection install. So it has performance implications, or even like you can break the application so it's not all bells and whistles, but it's an interesting concept, because you can. You can tie storage to a socket, you can tie lifecycle to it. There are no file descriptors access but you have socket cookies instead. So if you're trying to.
yeah, identify a connection at the moment, we use 5 descriptors for several reasons, and maybe that that would be a showstopper but you don't have that kind of access with this program you need to use like cookies instead, which Bp supports. So yeah, I just thought I would mention it, since we are all looking to these things just to bear in the back of our minds.
Tyler Yahn 00:45:56 Cool. Yeah, thanks for bringing it up good to good to spark some thoughts. Yeah.
Rafael Roquetto 00:46:01 Yeah.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:46:01 Yeah. I also wanted to mention something related that material just showed us, which I didn't know existed until your latest pr, that you could add these iterators on sockets to get you the information. So you can actually say, run this Bps program and all open sockets or something.
Mattia Meleleo 00:46:22 Yes, on all the system sockets. It's very full.
and it's a very, very performant as a as the other way of of iterating from from user space, like like broadcast, for instance, or stuff like that.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:46:40 Yeah, that's pretty cool. And so we had this long standing issue. That. So for our context, propagation relies on this Soc message. Soc. Ops program that Raphael is talking about. But for that you need to be able to track the socket.
So the way we track the socket is by registering.
Listen, essentially, that Sock Ops program listens for any new sockets that are created that are going to be outgoing.
I forget, passive or active, I think, one or the other, and then, once you see it create it, we add it to this map and this map from then on helps us attach this Salk message program, which we then use to extend the packet and slap in the trace parent in there.
The problem is, if we don't see the socket creation.
What happens then?
Then? We cannot actually extend this payload because that socket is never tracked. It's not in the map, because it needs to be added in the map, but we don't know of it.
So what we do. Instead, we use this backup path which uses traffic control if we hit traffic control a socket we haven't actually seen. Then in there we add into this map it's sort of like backup pad, but that requires traffic control to be available, which means, if you're running cilium and the people haven't configured properly the ordering, you don't have traffic control working properly.
So when we saw this yesterday, we're like, Oh, but then we can program this to give us to walk in, and then we actually do it for us. You can add that.
Mattia Meleleo 00:48:25 Yeah, we can just add the socket to the map, and that's it.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:48:28 Yeah, yeah, yeah, very cool, very cool. I was, yeah, I was like, Oh, I didn't know this existed. This is so much better.
Rafael Roquetto 00:48:36 1 1 question that I have. I mean, this is way better than anything we have. So we should. We should definitely adopt this is, if there is a way of filtering but like a a lot of our code, has this valid pit on the start of Cape probes or whatnot, so that we don't run the code, for you know process we're not tracking, and I don't know if there is a way with these iterators to kind of like filter things out. Probably I don't think not by pitch for what I've what I've experimented. But do you know what you.
Mattia Meleleo 00:49:16 Sorry. What is the question? If there is a way to.
Rafael Roquetto 00:49:19 Yeah. So, for instance, on your Pr. The iterator will enumerate the sockets, look for, listen sockets, and store the ports. That's doing for every everything in the system, and that's fine. I mean, it's a fair price to pay, but it's going to iterate for every port, even even for process. We're not tracking so that maps gonna get a bit bigger.
I think that's a fair price to pay. It's not a it's not a a big deal, but I'm wondering if there was a way to, you know. Given a port in your, for instance, in your case. But in more general questions given like you look at a socket. Is it a socket we want to track like a lot of our code has this valid pit. So we see. Oh, the whoever's invoking the escape probe is not is not. Our is not a process. We're tracking, so we don't do anything about it. I was wondering if you could do the same for these iterators. I don't think so, because the in terms of speed, for instance, it runs in the context of ob. In this case the pit is always going to be ob speed but maybe I wonder if there's a way of saying, okay, this sock belongs to something
Mattia Meleleo 00:50:21 This iterator is global. So it's meant to be run globally. So it it runs for every socket. But I don't think there is any problem in reading from a map and filtering based on the content of that map. So if we have a map of valid pits, I I think I can just filter on those.
Rafael Roquetto 00:50:40 Yeah, the the yeah. The problem is like, you don't know the beat of the associated with the socket. Right? You. You see, you get a socket, for instance.
and you don't know to who's process. That socket belongs.
Mattia Meleleo 00:50:53 I see what you mean.
Rafael Roquetto 00:50:54 Yeah.
Mattia Meleleo 00:50:55 Yeah, but.
Rafael Roquetto 00:50:55 Think that's fine?
Mattia Meleleo 00:50:56 If we are doing that for performance, I think the the map lookup would cost more than just adding that to a map.
Rafael Roquetto 00:51:04 Yeah, yeah, yeah, I agree. No, I'm not agreeing with you. I'm just wondering more like I said in more general terms, I'm just using your peer as an example, because that's the 1st time I encountered it. If you know there are ways of selectively a bail out of these iterator programs like we do for K. Probes or other things. That was my question. More in general terms. I think you're you're oh, is a fair price to pay.
Mattia Meleleo 00:51:27 The pit context. I'm not sure about that, because because I think this.
I think this is a globe. It has to be seen like a global instance of something running. So it doesn't run in the process that you are that you are tracking. So you don't know that the process context in this case. But if you wanna bail, I think there is a way to bail. So, for instance, we bail. If the socket is not listening. In that case.
Yeah, we don't have the context of the process, so we can't bail on something we don't know.
Rafael Roquetto 00:52:01 Fair. Enough. Yeah. Okay.
Cool.
Tyler Yahn 00:52:05 Cool. We're running close to the end of time. We still have one more thing on the agenda, so I'm going to move us forward here, Nimrod, you wanted to ask about the Http header and body extraction issue that you opened.
Nimrod Avni 00:52:20 Yeah, we can like talk about it quickly. But I saw that Rafael as well commented here, it's just like a suggestion and thing that might be interesting. Basically.
both, like anyone can, of course, look at it and give his opinion that we like specified exactly what we want to achieve, which is basically on Htp spans, at least. For now, Htp, we want to get like both like attributes of the header and the payload in the case that you know, the client configures it. And I'm guessing that's gonna be like the gonna impact performance in some way. Because, like right now, I think we only track in Http. We kind of do all the parsing in kernel space, and we ignore everything from the headers beyond. And if we want to start doing stuff like, send them to user space and even the body. And we need to do stuff like obfuscation and filtering of of headers and payloads and all that stuff that might cause some performance overhead.
We thought implementing, this is gonna be with the large buffers that Matthia added. Basically like kind of riding on that, using the the kernel part of Http to send like a buffer in the configured size. And basically like, I'll try try to do a lot of the parsing in user space of, like the headers and stuff and all those other stuff like obfuscation there might be. There's also some interesting point that I don't think there's any like auto convention for the like Http. Payload like I don't know if I remember like like previous, like customers of us like wanted to send their all like the Http payload, and they're like, which they just like generate something like Htp. Dot payload, or whatever. So we can either like invent some convention, or we can like, I don't know. Try to actually push it in the hotel, and that might be interesting. And yeah, and I think Rafael mentioned stuff about, maybe you want to benchmark some of the large buffer stuff. And I also was like interested in.
You said you had some thoughts about it, and like exactly what we want to. You know, what do we want to benchmark and what are exactly like, what do we hope to get from that.
Rafael Roquetto 00:54:40 Yeah, so marginally, I mean, like I said at the end of day.
it's the usual like CPU and memory.
I think this is. This is a good idea, like, the idea of processing things in user space is nice because it's super flexible with what you can do, and then it's much easier to to deal with Ebpf. So personally, I'm all for it. But my only concern is that I've I've been hit too many times with, you know, moving large large chunks of data from kernel space user space and then processing it there. So at the moment I'm actually investigating one bug that has to do with moving exactly that like it is related to network flows. It's nothing to do with this. But we are hitting a lot of locations and and some CPU usage as relevant. So when once we start doing that.
it becomes very easy for for us to just be careless. Not. I'm not saying you or me like in general, right? Because it's easy then to just push things in and start doing all kinds of processing, which is what gives us flexibility. On the other hand, so I what what I mean with benchmark is like, for instance.
write write a benchmark that starts pushing lots of large buffers with fake. Whatever fake data doesn't even have to be Http. And then how are we gonna be parsing it? Because as soon as you get the buffer, and then, if you, for instance, don't parse you don't parse that in place. You people keep allocating like the other Pr that we saw with the characters right? That still has, like 59 allocations.
things like that. That's gonna impact performance the CPU a lot a lot. And and that's that's a big problem, you know, for costs and and things like that. So I'm I'm interested on, you know the how much. How much can we stress the the large buffers, for instance, how how much can we do with them? How how many events per second? You know all the all, the kind of things that that would be my starting point to see if there an actual viable approach for this. Because, you know, Http requests are gonna be everywhere all the time. So that that's basically where I'm coming from.
Nimrod Avni 00:57:01 Yeah, that's like like the other. Like, I thought of it. More of in in the context of like, this will also increase the like. The the like. If we're sending spends like that's the use case for it. They're gonna make the size of spend significantly larger. And in that case we might even want to consider something like.
I don't know if it should like connect to the same sampling mechanism that already, like auto and stuff have. Maybe we can say something like, you know. Add these like attributes of the body and headers, or only just the body on, like X percent of spans like, I don't know. Maybe because if you want to limit the amount of of data that we increase, yeah. But that's more of like the the cost thought of it. Not more like the performance, but we can like like. Also I wrote like at the bottom, that it will probably be also good for, for, like post Htp classification for stuff like elastic graphql, like all like protocols, are, are built on top of Htp. And when we have, like headers and body, we can kind of infer them easily and like narrow down the scope of the span, which can be good for, for you know.
like we can like follow like hotel conventions for a specific protocols.
So if we can like, enable that like instead of I don't know, because, if not, we'll probably need to do some more like inference in kernel space, and that might be difficult, like, I know, parsing some header of like Aws, header in kernel space and inferring from that. And the route looks like F. 3. I don't know if we have all that data, and we can do it in user space.
No.
Rafael Roquetto 00:58:45 I think I think if we can pull this off, we're gonna is gonna give us a lot of flexibility. We just have to like that would be like, really good. We just have to make sure, you know. Be mindful performance. So that's what I mean. Yeah.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:59:00 I just want to say quick word. Sorry, I mean I haven't had time to review it in detail. I know you and I never talked about this. I also think it's a really good idea, and nothing stops us from taking negative approach, especially if it's disabled by default, even if the overhead is significant of the header buffers, nothing stops us from continuing with the work to make a higher level parsers or Second Level Parses, essentially or protocol detectors beyond. So we detect initially the Htp. Then we have this extra body, and then we do a second Level protocol detection that can extract. This additional more useful information like S. 3. But, you pointed out, is a really good example. Right? I. It's very. It would be much useful, more useful if I knew what bucket I'm talking to, rather than just seeing an S. 3 call through Http right.
Nimrod Avni 00:59:53 Yeah.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:59:53 That's what customers want to see. They want to see that I'm doing a bucket read over here, or or pushing new object to a bucket, and what's the bucket? And so on.
Even what we have today. If we can adapt it, I think we can take approach. And then.
if this is too expensive, then we'll have to be, you know. Go back to the drawing board and figure out how to do more efficient buffers, I think?
I I don't think we we wanna block any work towards this.
Nimrod Avni 01:00:27 Yeah, I think we can, you know, because.
Tyler Yahn 01:00:30 Okay, I gotta. I gotta jump in here. So we're at right time. I want to be respectful of people's time. And so we can definitely continue the conversation in the issue. So I definitely appreciate bringing it up. Thanks in Rod for doing that. Yeah. And definitely, let's let's continue there. Thanks for joining. I will see you all next week.
Bye.
Nimrod Avni 01:00:46 16.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 01:00:47 Right.
Rafael Roquetto 01:01:27 Hey, Mark, how's it going.
