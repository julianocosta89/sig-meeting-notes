SIG: Ruby SIG
Date: 2026-11-17
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Robb Kidd (he/him)** 00:31 Hello!
**Kayla Reopelle (New Relic, Inc.)** 00:32 Hello!
How's it going?
**Robb Kidd (he/him)** 00:36 It is… it's going.
**Kayla Reopelle (New Relic, Inc.)** 00:39 Did you get caught in that FAA…
**Robb Kidd (he/him)** 00:42 I did.
**Kayla Reopelle (New Relic, Inc.)** 00:43 I'm sorry to hear that.
**Robb Kidd (he/him)** 00:46 I got the announcement as I was leaving the hotel for the airport. I was like, oh, hell.
**Kayla Reopelle (New Relic, Inc.)** 00:50 Oh, no.
**Robb Kidd (he/him)** 00:52 And then I spent a little time at the airport, and then went, as I saw the flight get delayed later, later, I'm like, I'm just gonna go book a hotel, and rebook my flight for tomorrow, and… On Saturday, it was fine.
**Kayla Reopelle (New Relic, Inc.)** 01:07 Oh, nice, that's good.
**Robb Kidd (he/him)** 01:08 So, mostly, I think we were delayed, like, an hour because of…
**Kayla Reopelle (New Relic, Inc.)** 01:10 Okay.
**Robb Kidd (he/him)** 01:11 fallout, but…
**Kayla Reopelle (New Relic, Inc.)** 01:12 Yeah, yeah.
**Robb Kidd (he/him)** 01:13 Yeah.
**Kayla Reopelle (New Relic, Inc.)** 01:14 It's not bad.
**Robb Kidd (he/him)** 01:15 It was sort of my fault for, like, I'll just leave on Friday, and then the only flight available to me was late on Friday, and then that put me in the…
**Kayla Reopelle (New Relic, Inc.)** 01:23 I mean, the likelihood of a nationwide airport shutdowns.
**Robb Kidd (he/him)** 01:29 Doesn't happen that often.
**Kayla Reopelle (New Relic, Inc.)** 01:30 Slim, yeah, so I don't think you can really blame yourself on that.
**Robb Kidd (he/him)** 01:34 Yeah.
Yeah.
**Kayla Reopelle (New Relic, Inc.)** 01:36 Hi, Bart!
**Bart de Water** 01:39 Hello.
**Kayla Reopelle (New Relic, Inc.)** 01:40 How you doing.
**Bart de Water** 01:41 you have… Hope you had a nice QCon.
**Kayla Reopelle (New Relic, Inc.)** 01:44 Yeah, that's nice.
**Robb Kidd (he/him)** 01:45 Pretty good.
**Bart de Water** 01:47 Airport troubles aside.
**Robb Kidd (he/him)** 01:50 Aside from… that was technically after KoopCon, so, yeah.
**Kayla Reopelle (New Relic, Inc.)** 01:57 Hey, Hannah.
**Hannah** 01:59 Hey guys.
**Kayla Reopelle (New Relic, Inc.)** 02:02 Okay, I think we can get started, share my screen… Okay, so I wasn't able to make it to the spec SIG today.
Was anyone else there who would like to give a recap?
**Robb Kidd (he/him)** 02:36 I was not there.
**Kayla Reopelle (New Relic, Inc.)** 02:50 Looks like some discussion about span lifecycle events… And exponential histograms by default.
Anything that… People who are here today want to jump in together.
to look at.
**Matt Wear** 03:14 I can just add to the span lifecycle events, I feel like that was the longest conversation.
**Kayla Reopelle (New Relic, Inc.)** 03:18 Hmm.
**Matt Wear** 03:19 Yeah, basically a way to represent spans through logs.
was the, was what was really being discussed, so just kind of send, like, a… a start event before when a span starts, and then, I think send, like, an end event when spans end.
And,
**Robb Kidd (he/him)** 03:41 What?
Okay.
**Matt Wear** 03:46 Yeah, so, I mean, technically, like, this is, like, a completely different, tracing model, but I… I think there are, like, there are tracing systems out there that actually work this way.
So it's not… it's not crazy, but what is crazy, I think, is that, Is that the author was trying to just, like.
implement this by… by… via semantic conventions, just going to the semantic convention SIG and not really involving, like, a further discussion, but I think people are like, you probably need to know tech for this.
**Robb Kidd (he/him)** 04:27 Yeah, yeah.
**Matt Wear** 04:30 But…
**Robb Kidd (he/him)** 04:30 I guess, what problem is this solving?
**Matt Wear** 04:33 So…
**Robb Kidd (he/him)** 04:34 Is my infamous question of, like.
**Matt Wear** 04:36 Yeah.
It solves a legitimate problem. So, one of the problems with, like, one of the problems with our variety, with our flavor of tracing is that, like.
You're keeping spans open in memory.
And for, like, long-running traces, that's not, like, a great situation, usually. And I think, historically, Our answer to that has been, you should not have long-running traces, but…
**Robb Kidd (he/him)** 05:03 Okay.
**Matt Wear** 05:04 like, regardless, there are things that have long-running traces. There's always been, like, workflows that are long-running, and I think it's… probably only becoming, like, more prevalent in the agent age, as well. Like, if you want to instrument, like, agents themselves, I think trying to, like, figure out, like, what is… what is, like, a unit of work in there? But,
**Robb Kidd (he/him)** 05:31 Yeah.
I don't… I have opinions about that, too.
**Matt Wear** 05:40 Yeah, yeah, I think there's no… yeah, there's… this is not happening imminently, but I think, it has been something that has been discussed, like, periodically throughout The… throughout the history of OTEL, and I think the, Yeah, I think the one… the one thing that people were bringing up is, like, once you have two ways of creating spans, then it's like.
**Robb Kidd (he/him)** 06:08 Why not have 3? And then we have… we're…
**Matt Wear** 06:11 Yeah. Yeah, I mean, you can… you could, like, build tracers around, you know, this log way, and then, people have to support that one way or another, and that's kind of… that means something different on ingest now, if, like, you're trying to… Look for special logs to create spans that make it into your, you know, tracing part of your, of your backend, so… Oops.
**Robb Kidd (he/him)** 06:41 Yeah, stitching it back together after sending a start and then an end.
In a backend seems… ill-advised.
**Matt Wear** 06:50 I mean, like I said, there are tracing systems that work this way, so it's not impossible, but… In order for it to, like, be useful, like.
people who are supporting OTEL, I think, would kind of have to, like.
They would have to do both.
**Robb Kidd (he/him)** 07:08 Yeah.
I keep… I go back to, what problem are we solving, and is this the right solution for that problem? And if it's… long-running things… well, front-end… front-end has long-running things, front-end sessions, agents have conversations, those things have IDs. I think you could… stitch those things together with a shared ID, and not have to make one mega root span that you don't know when that thing's gonna end.
**Matt Wear** 07:34 They did bring that up, like, as an example, actually, in favor of, because that's kind of how session tracing works, to a degree, but…
**Robb Kidd (he/him)** 07:44 Are you in favor of doing this instead of having a shared ID?
**Matt Wear** 07:48 It was just kind of brought up as… another example of, of how this could be handled. So, yeah, I think… Obviously, we're not solving this problem here in SIG, but I think…
**Robb Kidd (he/him)** 08:05 Thank you for the explanation of what is being talked about there, about these lifecycle events.
**Matt Wear** 08:09 Yeah, I expect your exact questions are going to be, talked about at length as this, Yeah, as that conversation continues.
**Robb Kidd (he/him)** 08:22 Alright.
**Kayla Reopelle (New Relic, Inc.)** 08:24 It's a very spicy idea for our most stable signal.
**Robb Kidd (he/him)** 08:29 Yeah. Yeah.
**Kayla Reopelle (New Relic, Inc.)** 08:30 Cool. Okay, thanks for… for sharing that.
Interesting to see where that goes.
So, for CORE, the first topic we have on the agenda, which I think might be also related to this pull request that you linked, Matt, the naming of our exporters is currently inconsistent, James is proposing to standardize implementations into exporter protocol variant signal, with variant being gRPC HTTP file.
Variant and signal apply only when the exporter supports multiple, and metapackages can bundle everything, like exporter OTLP contains HTTP, gRPC, and eventually files.
So, yeah, I think… We had talked about this a little bit in a previous SIG, and there was some hesitation about Creating so many cascading gems.
But this… this is, like, standardizing you know, is helpful because it's predictable, we do have more variants and protocols than we used to, but I don't believe we've… released anything… I don't think we've released HTTP or gRPC yet, so right now we just have exporter protocol signal, I believe.
Yeah, I'm skeptical, but what do other people think?
**Matt Wear** 10:07 I'm for uniformity, the cascading gems, I am… I'm kind of for in… just because, like, each one of these gems, like, mainly, like, GRPC and Protobuff, they both have problems, and, giving… Users a way to avoid pulling in those dependencies.
I think is necessary, actually. Because, This is one of these things where we can get into it.
situations where a customer's version of, like, Protobuff can conflict with our version of Protobuff, and then you just can't use the hotel.
So, like, and… gRPC, I don't know if it has exactly the same issues, it might, but it's also, I think, like, a pretty big dependency, so it's like.
All I'm saying is, I don't want… Us to have, like, one, you know, export or OTLP that bundles, like, JSON, gRPC, and HTTP protot all together, because then you're forcing users to install all of those dependencies, and those dependencies can't conflict with theirs. Whereas if we.
**Kayla Reopelle (New Relic, Inc.)** 11:32 We haven't.
**Matt Wear** 11:32 them.
individually, then, then there's an option for everybody, I guess.
**Kayla Reopelle (New Relic, Inc.)** 11:39 No.
**Matt Wear** 11:40 That will work. It might not be the best, but…
**Robb Kidd (he/him)** 11:44 It'll be less bad.
**Matt Wear** 11:46 I think it'll be less bad, and, In this case, you know, the… the sprawling gems, I think, are worth it.
And I think consistency and naming is worth it, but I just… I think… I haven't looked at what our current names of what people are currently using are. It will probably break, is what I'm thinking.
**Kayla Reopelle (New Relic, Inc.)** 12:13 Yeah, yeah.
Yeah, the migration plan is something to consider, because I don't think we can use our current names, and might have to just retire those gems, or just make them kind of aliases for the new gem names.
Which seems complicated. I think there's also some concerns about, like, when we do this. I don't know if our OTLP traces exporter is stable, but if we're looking at stabilizing metrics and logs, do we do that?
Now, I guess names don't have to be stable. Sorry, I'm just thinking a lot out loud.
Names can be changing, but we'd need to update our documentation and probably… Make it pretty clear about what's going on, and maybe have some kind of… dual support period for a while. I think the only time we've done… Something similar that I'm aware of is with… helper gems inside of Instrumentation, where we renamed… I think it was, like.
the SQL obfuscation helper gem to SQL processors, or just SQL, something like that, and… left them kind of as aliases for a while. I don't think we've fully removed the other one, but That gets back to needing to define, like, a clear archiving policy of how we deprecate our gems and what we do with them when they're done.
Which I don't think we've really documented yet.
So, steps to consider, not necessarily a reason not to do it, I think.
Uniformity is good. I don't think we probably… Could have seen all of this coming when the initial ones were released, too, with naming I mean, maybe one other thing to think about would be, are there other… variables that we need to consider with naming for future names? Do we think that there's other things besides protocol, variant signal.
That, yeah, that we would eventually want to include.
**Matt Wear** 14:32 Yeah, and maybe… I guess, while we're talking about this, I think… I'm definitely for, separate gems for… protocol variant, I think?
signal… I'm a little more open to combining things on, like, I haven't given a lot of thought into if there's, like, yeah, if there's future value in having exporters broken down per signal.
I kind of think if you have, like, the… Boom.
you know, like the OTLP HTTP proto library, for example, I would be fine having that have metrics, logs, and traces available in there.
I think the reason that The reason they're divided right now is that you can't have like… they're all at different levels of stability, and you can't have unstable packages mixed in with a stable package, so I think we're trying to set us up for stable packages.
But… I would be fine for, like, ultimately, like, migrating those into the stable package so that we don't have… such… Such significant sprawl.
**Kayla Reopelle (New Relic, Inc.)** 15:57 I think that makes sense, too, and then… For the ones with protobuf, we're not including a bunch of irrelevant protobuf files for, kind of, the sub-variants as well.
Is… Yeah.
**Robb Kidd (he/him)** 16:12 in this naming scheme of exporter… of exporter, protocol, variant signal is protocol, protobuf versus JSON.
Basically.
**Kayla Reopelle (New Relic, Inc.)** 16:21 Mmm… hmm.
**Matt Wear** 16:24 So I think it's, like, gRPC versus… I would argue that you would want HTTP protobuff and HTTP JSON as separate,
**Robb Kidd (he/him)** 16:36 Yep.
**Matt Wear** 16:37 Separate gems, because, like…
**Robb Kidd (he/him)** 16:40 That's how you get off of Protobuff. If you want.
**Matt Wear** 16:42 HTTP JSON is, like, the escape hatch, for people whose protobf conflicts, but it's…
**Robb Kidd (he/him)** 16:49 I guess I wasn't…
**Matt Wear** 16:50 like a…
**Robb Kidd (he/him)** 16:51 I wasn't clear on the exporter protocol variant, and the variant was gRPC or HTTP, or file. What's protocol, then?
**Matt Wear** 17:03 So I think protocol is gRPC HTTP, but I think… We could simplify this scheme if we say the… Transport. The second thing, whatever you want to call that. It's probably not exactly protocol.
**Robb Kidd (he/him)** 17:18 HTTP and file might be transport.
Them being transport protocols.
And then I'd say the variant is, like, What's going inside that transport?
Protobuff or JSON, or…
**Matt Wear** 17:36 I would like to see us come up with, like, the… the end goal of what packages we want, and what we would like them to be named, and then we can…
**Robb Kidd (he/him)** 17:44 That would be good.
**Kayla Reopelle (New Relic, Inc.)** 17:46 Yeah.
**Matt Wear** 17:46 Specify exactly what each parts of that name actually is.
**Robb Kidd (he/him)** 17:52 Yep.
**Matt Wear** 17:55 But, yeah, so I guess, ultimately, we would probably end up with the ones that we've been talking about. gRPC, HTTP Proto, HTTP JSON, File.
This file, maybe another… Wanted to throw in there just to make sure that we have enough abstractions.
**Kayla Reopelle (New Relic, Inc.)** 18:13 Yeah.
**Matt Wear** 18:16 And for file… Yeah, let's just make sure that we… we have a story for those, and I feel like if we have a cohesive story for those, then we can, probably, yeah, just see if we are aligned on what that actually is.
**Kayla Reopelle (New Relic, Inc.)** 18:38 Good.
Okay, cool, is… I wonder if there's an issue. So, is this the issue related to that?
Shared OTLP types.
Hmm… not… quite, but maybe kind of related? Okay, so maybe…
**Robb Kidd (he/him)** 19:08 This would be one… this would be a gem that… included in the Cascade, this would be a… and types, Jim, that the things could… the thing speaking OTLP would use this, too.
**Kayla Reopelle (New Relic, Inc.)** 19:21 Okay.
**Robb Kidd (he/him)** 19:24 Agreed of that… the purpose of that one.
**Kayla Reopelle (New Relic, Inc.)** 19:27 Take as a to-do, figure out where to put these notes.
If there's an issue or something else that we can use, to continue the discussion.
**Matt Wear** 19:37 Yeah, and I added this in here just because, Thompson Telwo pinged me, because I approved this a long time ago, merge, and I… I just wanted additional eyes on it, but now that we were having this conversation, I think the other thing that I need to, validate is that this is not going to somehow… Boom.
Yeah, that we're not gonna somehow end up with… Like… dependencies that we don't want.
**Kayla Reopelle (New Relic, Inc.)** 20:10 Oh,
**Matt Wear** 20:12 Everywhere.
So, at this point in time, I actually kind of forget a little bit what this does, and if these… if the shared types has, like, a protobf dependency, is kind of what I'm… what I'm trying to tell myself I need to look into.
**Kayla Reopelle (New Relic, Inc.)** 20:33 Okay, so this might be… Something to wait on until we decide how we want the rest of the gems to cascade, kind of as a dependency.
**Matt Wear** 20:44 I think… we should verify, or… yeah, I think we should answer that question. Is this something that we should wait on?
Given that, or is this okay as is? I need to kind of look at it in that context. I was kind of… I looked at this a while ago, when those When our, kind of, exporter.
**Robb Kidd (he/him)** 21:06 A quick read on this PR, the one that you had linked, 2236, is that there is a new OpenTelemetry Types OTLP gem.
That depends on Protobuff.
And, and this PR updates many of the OTLP exporters to depend on the types, so… There would be a… Some transitiveness into… Google Protopuff.
**Matt Wear** 21:33 And I would be fine with that, as long as it's the… Protor, HTTP, and the gRPC.
**Robb Kidd (he/him)** 21:38 Right, the new exporters are constrained to… I'm the protobuf one.
**Matt Wear** 21:49 And…
**Kayla Reopelle (New Relic, Inc.)** 21:59 Okay, so trying to put… Protobuff into its own.
Gem?
**Robb Kidd (he/him)** 22:06 I… my quick read on this is that, this new types gem is what everything would depend on, and the types gem happens… it's OTLP types, and it has a dependency on protobuf.
Google Protobuff.
**Matt Wear** 22:25 And really, I think… Like… We really only have gRPC and proto over HTTP today, right? We don't have JSON or HTTP, so,
**Kayla Reopelle (New Relic, Inc.)** 22:36 There's a pull request open to add JSON that I think is pretty close, but we don't have it today, and we might want to wait to merge it until we know how we want to name things.
**Matt Wear** 22:47 Cool, yeah. So… So I guess that's one thing that we should keep in mind when reviewing this PR, is, what does this look like when JSON lands?
And if there is, like… Yeah, we just don't want Protob to end up in JSON, so if there is some part of the types that are… that need to be shared that are not for Protobf, then we need to kind of split this, probably, is what the… And Bizarre would be.
**Robb Kidd (he/him)** 23:18 Yep.
This does appear… this type's OTLP library does appear to have a whole bunch of the PB classes generated from Protobuff.
**Matt Wear** 23:32 That was my… That was my recollection. I think this is mostly… I think this is going to be a dependency for the Protov Based exporters.
**Robb Kidd (he/him)** 23:44 It's been a long time, and I didn't go deep on it. I don't know if these protobuf-generated types are also what we would use to produce JSON.
For consistency. But…
**Kayla Reopelle (New Relic, Inc.)** 23:55 I don't remember. Yeah, I'd have to look at that.
Yeah. I can.
Yeah.
**Matt Wear** 24:01 I guess that's a good question on the JSON exporter, is does that actually free you from Protobuff, or are you just… Protocol buff JSON transcoding.
**Robb Kidd (he/him)** 24:10 It… yeah, or is it, That the protobuf becomes the JSON exporter's development dependency?
**Kayla Reopelle (New Relic, Inc.)** 24:19 Mmm.
interesting.
**Robb Kidd (he/him)** 24:22 So that's.
**Matt Wear** 24:22 That's fine.
**Robb Kidd (he/him)** 24:23 Todd doesn't need it, but to build.
**Kayla Reopelle (New Relic, Inc.)** 24:24 Yeah.
**Robb Kidd (he/him)** 24:25 Produce the classes? I don't know.
**Kayla Reopelle (New Relic, Inc.)** 24:34 Interesting.
**Robb Kidd (he/him)** 24:36 I only did the OTLP JSON shenanigans in Go, and that was, you know… Doesn't really matter how you do it over there.
The dependencies are not the same problem with mixing dependencies, and both gRPC and Protopuff are happy in that ecosystem.
Cool, alright.
**Kayla Reopelle (New Relic, Inc.)** 24:58 Is there a reason why we would want to call it types over just, like, protobuf?
or something?
Like, do you think there's other types that we would eventually… I mean, that's a question for the PR.
**Robb Kidd (he/him)** 25:09 Yeah.
I mean, it is… it is… the classes generated from the OTLP protobuf definition.
**Kayla Reopelle (New Relic, Inc.)** 25:23 Okay.
Let's keep going, we have more topics. Last call on this one. Any other thoughts before we move on?
Okay, Bart. Tell us about Ruby GC Metrics.
**Bart de Water** 25:41 Yeah, months ago, I was looking into adding those onto spans. I've been cured of that idea, and now that metrics are maturing, I was like, let's take another stab at this and read Ruby's gc.stat periodically and see what, you know, comes out if we stick that into our observability backend.
And this is really a side quest, so I will admit I just threw an agent at it while working on my actual project.
But it reported back that there was an issue, and turns out that someone else also found it, is that the asynchronous instruments, are not working correctly. Someone has attached a fixed PR.
But yeah, in order to sort of, like, even propose a, how Ruby GC metrics could be a gem, that other people could use, this is kind of like a hard blocker, so I was wondering if someone could… Take a look at that.
**Kayla Reopelle (New Relic, Inc.)** 26:43 Yeah, I only saw that one this morning, so… I'll get those workflows running, but I think we should be able to look at that one this week.
**Bart de Water** 26:55 Alright, thank you.
**Kayla Reopelle (New Relic, Inc.)** 26:58 That's exciting, thank you for, looking at the GC metrics.
I think we'll eventually want to start looking at self-observability metrics, too. Those may or may not become a condition for our eventual stability pitches.
**Robb Kidd (he/him)** 27:14 Observability metrics.
**Kayla Reopelle (New Relic, Inc.)** 27:16 Self-observability, yeah, so, like, replacing the metrics reporter with something that's been spec'd out by those.
**Robb Kidd (he/him)** 27:22 Aha.
**Kayla Reopelle (New Relic, Inc.)** 27:23 Of, like, how many spans and traces and successes and failures and such.
**Robb Kidd (he/him)** 27:28 What, so the… it's almost like, dare I say, semantic conventions. What does an SDK report about itself?
**Kayla Reopelle (New Relic, Inc.)** 27:35 I don't remember. Yeah.
**Robb Kidd (he/him)** 27:38 that. Okay, I see.
**Kayla Reopelle (New Relic, Inc.)** 27:40 Maybe…
**Robb Kidd (he/him)** 27:42 Also, Bart, if sometime you want to talk about putting metrics on spans, I'd be happy to have that conversation.
**Kayla Reopelle (New Relic, Inc.)** 27:46 Here we go.
**Robb Kidd (he/him)** 27:47 Even though it's kind of off-spe I smell what you're cooking, and…
**Bart de Water** 27:52 Well, like, I… we… so actually, the reason I was looking into that is that we just saw, like, memory growth that we had trouble explaining, and in the end, I just cooked it up in our app.
It didn't really give us the signal that we were looking for, or at least not the smoking gun.
And, sort of, like, by chance, someone else on my team figured it out a couple of weeks later, is that we were not… initializing GE malloc the way we thought it should be initialized on our background workers, so it was just using the standard malloc, which comes with all the well-known memory fragmentation and growth problems in Ruby. So once we fixed that, all of a sudden, all of our memory issues were just, you know, gone. So I've been completely barking up the wrong tree there.
**Robb Kidd (he/him)** 28:40 There is some prior art from Shopify before we had a metric signal of putting, things like memory utilization and GC stats on spans.
**Bart de Water** 28:51 Yeah.
Yeah, you see that also in, like, in some blog posts where people are like, oh, you know, just, like, captions.
**Robb Kidd (he/him)** 29:00 Capture it on… it's a processor, capture it on start. Now that we have on ending.
**Bart de Water** 29:06 Yeah.
**Robb Kidd (he/him)** 29:06 When the span's still mutable, you could, like, capture stuff at the end.
**Bart de Water** 29:09 Exactly, or it would be all the math.
sidekick middleware around every job, just report it, like, whatever, you know? Yeah. I'm hoping to build something that is a little bit more, I guess, normal and on the supported path, and…
**Robb Kidd (he/him)** 29:22 Doing it with metrics is the right way.
**Bart de Water** 29:25 Yeah.
**Robb Kidd (he/him)** 29:26 But that way exists.
I feel like is a… is a… if you want to do shenanigans, because you don't want to omit data points, you just…
**Bart de Water** 29:34 Oh, yeah. For instance…
**Robb Kidd (he/him)** 29:35 Backends! Backends that are columnar, and… and fields are free.
Yeah, as an example, randomly.
**Bart de Water** 29:44 Yeah, like I said, in the end, it didn't help us figure out what was going on, so…
**Kayla Reopelle (New Relic, Inc.)** 29:51 Maybe the next problem, it could help.
**Bart de Water** 29:54 Who knows?
**Kayla Reopelle (New Relic, Inc.)** 29:55 Who knows?
Okay, sweet. Alright, with Contrib, I just… oh, go ahead.
**Robb Kidd (he/him)** 30:03 Related decor, I know Hannah and I have.
**Kayla Reopelle (New Relic, Inc.)** 30:04 Yeah.
**Robb Kidd (he/him)** 30:05 last week about the schema URL.
when I'm ready to review, when… Hannah, you've got… The changes we talked about.
**Hannah** 30:14 Yeah, I have them up. The PR is open. The last thing I kind of wanted to do before I asked everyone to review was have an agent review it first for any, like, easy misses. But I think it should be pretty good. It follows the same pattern, as adding metrics, and… Sorry, scope attributes, and… there was a PR opened a long time ago, that… this pattern kind of always already was approved on, so I think this should be pretty straightforward, but I will ping the channel when I… after I have the agent review.
**Kayla Reopelle (New Relic, Inc.)** 30:56 Sounds good. Did you say it was already open?
**Hannah** 30:59 I think I did open it.
**Robb Kidd (he/him)** 31:00 I think it's open and in draft when we were looking at it last week.
**Kayla Reopelle (New Relic, Inc.)** 31:07 Okay.
**Hannah** 31:08 It did open, okay, cool.
**Kayla Reopelle (New Relic, Inc.)** 31:09 Okay, nice. I just wasn't seeing it.
Cool.
**Robb Kidd (he/him)** 31:25 And I, have… That sidekick proposal? Oh, that's Contrib. Sorry.
Wrong section.
Ignore me.
**Kayla Reopelle (New Relic, Inc.)** 31:32 bed?
Yeah, but you can still dive into it.
**Robb Kidd (he/him)** 31:39 No, I'm jumping the queue, no.
**Kayla Reopelle (New Relic, Inc.)** 31:41 Okay. I just took these, links from… the Slack, the Otel Ruby Slack that Thompson Tomo requested review on.
I put them in our agenda here. They are… All related to the CI, I believe. Dockerfile… PIN dependencies and appraisals… And… Consolidate Ruby version definitions. I have been open for a little bit.
Yeah, I am not a CI wizard, but, I'll take a look if someone else who is… has a grander vision for CI connections, could also review, that would be great.
**Robb Kidd (he/him)** 32:36 I thought I was a CI wizard until I got into this in toys. It's complicated.
**Kayla Reopelle (New Relic, Inc.)** 32:42 This is complicated.
This is a lot going on.
**Robb Kidd (he/him)** 32:47 So this was my proposal for Sidekick to add, we've gotten requests for, reducing the number of span events that come out of Scik, because, In the mists of time, the spec says if things happen in a point in time, like a job getting created and a job getting enqueued, those are point-in-time things. There should be span events!
The most useful thing that you could do with a… knowing when a job was created and when it was queued and when the job was started is compute queue latency.
So this is a proposal to optionally move those Timestamps of job creation and being put in a queue to optionally have them as attributes on the span we create.
And optionally do the Q latency math in the instrumentation.
I foresee a time… I would ignore these options that you have shared, because, feedback on this was… the options should be a little bit more in line with declarative… the way that declarative config options are set, where… so the options that we have in our instrumentations currently are very Ruby-ish, and declarative config is very not.
So my last… my latest comment on this is a new proposal for the options.
Which are Booleans. Whether to record the timestamps as events, and it is currently true, because that's kind of her spec.
Whether to record them as attributes, that is… that would be false.
By default.
In the comment above it would be the, attributes that would be added to the span if you were to enable this.
They would be strings.
According to an ISO time format at millisecond precision. So if people who wanted to could parse that thing and get timestamps back out if they want.
The real useful thing is the last one, record job latency.
And it would be… Seconds as a float, because that's what… Histograms usually are.
I want on another PR to add it as a metric. I kind of wanted to tease apart the… manipulating what goes and what doesn't go on the span, and then when we want to… if we choose to add, SIG job latency as a metric, that would be a separate effort of adding metric… Meters to the instrumentation.
basically, there was a bunch of conversation about, what should we call the meter? And I'm like, meter wasn't the request I had from my customer, it was just…
**Kayla Reopelle (New Relic, Inc.)** 35:29 Hmm.
**Robb Kidd (he/him)** 35:29 Reducing the span of it volume, and… And doing something useful with the… recording the job latency, if you… if you chose not to record anything, if you only cared about job leads.
So that's the new proposal of Scopit 2 just spans those new options with attributes being added or not.
And…
**Matt Wear** 35:50 So the problem this is solving is reducing span event latency.
**Robb Kidd (he/him)** 35:56 Reducing span event volume. Reducing event volume, because span events come in and…
**Matt Wear** 36:01 Yeah, I don't know why I added.
**Robb Kidd (he/him)** 36:03 Why did they get charged for it?
But, like, the useful thing you do with the information on those spanned events is compute queue latency, so… Add it to the instrumentation, so you can opt in to having that math done for you, and then throw away the timestamps if you don't care about the timestamps.
**Matt Wear** 36:22 So I feel like I have a handful of questions, and, like, does this cascade to other background jobs? Are we recording these things as events?
**Robb Kidd (he/him)** 36:32 I could go investigate. I don't know if the instrumentation for other background job thingies, do the same thing. I could go investigate that and see if this is… If there's some prior art that we've already done elsewhere.
**Bart de Water** 36:45 I'm 99% sure that's not the case. We're active job users who don't remember seeing this in our backend.
**Robb Kidd (he/him)** 36:54 But I could do that survey, because certainly this would… I would propose this as a pattern for other background job things of… so that we could record… we could give a consistent configuration surface of… Do you want to follow spec and get these things as span events? Do you want them timestamps on the spans, or… and do you want us to compute the latency for you?
**Matt Wear** 37:16 And then, yeah, I feel like the other… question I have is… Ruby's not the only, you know, ecosystem with background job frameworks. Yep. Curious, like, what's going on, like, in the Python world, for example.
**Robb Kidd (he/him)** 37:30 scroll up back to the description, I have a little bit of, research on what are the other languages doing.
It's in the, first.
issue… the issue description. There's a section of, like, history or prior art.
I don't remember what I call it.
Other instruments, other hotel instrumentations do it.
They… naming's all over the place, because these are not… SimConf fields.
But… .NET will record a job creation time as ISO 86… as an ISO format.
Java's Kafka, and RabbitMQ record queue times.
In milliseconds.
the semantic conventions do say that if you're gonna record a time.
As an attribute, it should be ISO 8601, so following that.
It's kinda all over the place.
So inasmuch as there are conventions, I followed them in this proposal.
**Kayla Reopelle (New Relic, Inc.)** 38:33 Yeah, conventions are difficult for background jobs. We have found, because the messaging submitted to conventions don't want to own them. They consider it different enough that they don't fall into messaging.
And, at least with Sidekick, you know, reaching out to… Like, per him, it sounded like he didn't want to own the telemetry either, or have opinions on the names, so… It's a little bit of a gray area, which could warrant its own semantic conventions field, especially if Python or other areas have semantic conventions, but I think we talked previously about defining them in maybe just the Ruby namespace, or… having… Something else there, if we were gonna post them?
That might have been a different issue.
**Robb Kidd (he/him)** 39:20 I remember conversations about that, but they were a while ago, and I don't remember the details.
sorry, I can go and update the main description of this issue with the latest proposal, so that The story is clear, you don't have to read all the comments.
**Kayla Reopelle (New Relic, Inc.)** 39:41 That'd be helpful. Bart, what do you mean by hotel alignment chart? There might be something…
**Bart de Water** 39:46 This is a bit of a meme that we have going on on our team, where we're like.
**Kayla Reopelle (New Relic, Inc.)** 39:50 Oh, okay.
**Bart de Water** 39:50 on the, you know, alignment chart on this subject. Like, you know, is a hot dog a sandwich kind of thing?
**Kayla Reopelle (New Relic, Inc.)** 39:55 I see.
**Robb Kidd (he/him)** 39:57 Do we make up our own names, or do we go to the committee? Yeah.
**Bart de Water** 40:00 Exactly, yes.
**Robb Kidd (he/him)** 40:01 Please, Mother, may I have a name.
So I would not include messaging anymore, James had a good point in here that… that, at this point, we're so off the beaten path of messaging that maybe we just go vendor-specific with Sidekick.
And it sounds like Mike Perham isn't interested in, like, getting involved at NoTel to a point where he would declare what the names would be, so, I could look and see, what does Sidekick admits its own… observability metrics, I could go and see.
**Kayla Reopelle (New Relic, Inc.)** 40:44 Yeah.
**Robb Kidd (he/him)** 40:45 how these names align with what's there, so that people who are used to looking at, like, the Sidekick dashboard that's emitted by Sidekick itself, if they're used to those names, we could use those.
**Kayla Reopelle (New Relic, Inc.)** 40:55 I think that would be helpful,
**Robb Kidd (he/him)** 40:58 I will survey that, too, then.
What… what do… what does Sidekick call these numbers? Yeah.
**Matt Wear** 41:07 I'm kind of wondering, though, like… Just semantically, like, if these are not span events, then… what really should be a stand event? Because these seem like they fit pretty well to.
**Robb Kidd (he/him)** 41:23 They… they are span events. They are span events. I've just had people ask not to send them.
**Matt Wear** 41:31 So I feel like… That is more of a… are you running a hotel collector? Can you drop them at the collector?
**Robb Kidd (he/him)** 41:39 Yep, they could, but then asking a customer who's just running a simple Ruby app to, like, how would you like to run more infrastructure to strip these things off?
has been an unpleasant response.
Yes. Currently, the workaround is run a collector, have it look at these two span events, do the math, put the attribute, drop them or hoist them.
And that is… there is a workaround. You could do this mutation in a collector.
But not our own.
**Matt Wear** 42:13 I feel like…
**Robb Kidd (he/him)** 42:14 Not everybody wants to run a collector.
**Matt Wear** 42:17 I feel like we need to draw a line somewhere at some point, otherwise you will end up with, you know, endless knobs for things that you can do easily in a collector.
And I… I would… question… yeah, I… I personally would question anybody working in a hotel… using a hotel at their company who is unwilling to run a collector somewhere.
That it might not be a good fit for, for them, But…
**Robb Kidd (he/him)** 42:48 I think that there are small enough shops who run a Ruby thing who don't want to have to run a… like, you spin this thing up in Heroku, and now you have to figure out how to run a collector in Heroku.
But I… I also hear you, yeah. Infinite knobs. Like, where do we draw the line?
**Matt Wear** 43:09 Yeah.
**Kayla Reopelle (New Relic, Inc.)** 43:10 Anything to keep in mind with span events being deprecated? Like…
**Robb Kidd (he/him)** 43:15 That's an interesting one.
**Kayla Reopelle (New Relic, Inc.)** 43:15 They're going away, they're becoming logs, like, how does that… These do seem like span events, but span events… Kind of aren't supposed to exist anymore.
**Matt Wear** 43:28 I need to think that through, because I don't know that it's… that they don't exist anymore, it's just they become… Your boss?
**Robb Kidd (he/him)** 43:34 Yeah, you're discouraged from using them.
**Matt Wear** 43:37 They become logs, but you are… but you have, correlated them with, like, your… trace and span ID, so they still can be.
**Robb Kidd (he/him)** 43:47 So what… In a world where we didn't do span events, would we log the job creation time? And would we log the… Job and queue time.
**Matt Wear** 43:58 So, here's… here's the reality of the situation, is that… In open tracing, these were called logs, and…
**Kayla Reopelle (New Relic, Inc.)** 44:06 Hmm.
**Matt Wear** 44:07 When, Yeah, and when we merged into… to form OpenTelemetry, we had discussions about what to call these things, so logs and span events.
They're the same thing.
They're just… Right. The name was changed.
**Robb Kidd (he/him)** 44:25 I would say that in a world where we were emitting these as logs, separate signal, it will be… Hard to impossible to do the workaround in the collector to drop them and do the latency math.
Because, the span events today, the span events ride along with the span when they're exported, so you… a collector has span and these two things and can do the… The mutation and whatnot, right then.
You'd have to have a collector holding spans and holding logs for a period of time before, like, okay, do I have logs correlated with the span?
Doing the mutation across two signals.
I don't know if it's possible, and if it's possible, it'll be hard.
And I'd be asking people who are running a simple Ruby app in Heroku to do Really complex stuff with a collector at that point.
**Matt Wear** 45:18 Yeah.
**Robb Kidd (he/him)** 45:19 Which circles back to, would you like to know how long this log… how long this job spent waiting in the queue?
That's… that's the problem I'm trying to solve. They just want to know how long this thing sat in a queue.
**Bart de Water** 45:32 Dumb question, is it then not just two span attributes?
**Robb Kidd (he/him)** 45:37 That is this proposal.
**Bart de Water** 45:39 Yeah. Okay.
**Robb Kidd (he/him)** 45:40 Record the times as span… record the times as span attributes, record the queue latency as a span attribute. You could opt in to either, or both.
**Bart de Water** 45:48 Yeah, no, sorry, I'm…
**Robb Kidd (he/him)** 45:50 That's the proposal. Record this on the span, because we know it.
**Bart de Water** 45:53 like you're…
**Robb Kidd (he/him)** 45:56 I agree that, yes, you could choose once we have a meter in there.
Like, sidekick job queue latency could be a histogram.
But there are backends who are happy getting this job queue's… this job's queue latency was X, and then you could aggregate later.
**Matt Wear** 46:17 I feel like…
**Robb Kidd (he/him)** 46:18 It's really the proposal. I want to put queue latency on the span. The timestamps, I really could care less about.
**Matt Wear** 46:25 I feel a little bit more, like it's a reasonable thing to put Q latency on the span.
Like, I don't feel so much that, like.
That needs to be an event, or that needs to be derived from, you know, events.
Something like that.
That, I feel, sounds reasonable.
**Robb Kidd (he/him)** 46:43 Okay, so… so there's no controversy with put Q latency on… like, optionally put Q latency on the span, and at some point we'll have a meter that will put out a histogram of queue latencies, and… and… Users could choose.
**Matt Wear** 46:57 Right now.
**Robb Kidd (he/him)** 46:58 It's the time.
**Matt Wear** 46:58 There's nothing that makes me think…
**Robb Kidd (he/him)** 47:00 Okay.
**Matt Wear** 47:01 Yeah.
Nothing makes me think that's crazy, but…
**Robb Kidd (he/him)** 47:04 Okay.
The timestamps are where there's a little crazy.
**Matt Wear** 47:11 I mean, this does seem like these point-in-time things during a span that you would… Historically have gone as a span… span event, or a log in the open tracing days.
**Robb Kidd (he/him)** 47:27 Okay,
**Kayla Reopelle (New Relic, Inc.)** 47:34 Oh, then looking at this… Record job latency attribute is what we'd be… keeping? Or how does that… how does that change this?
**Robb Kidd (he/him)** 47:45 Well, the bottom option, I think, has been agreed to, like, that's reasonable.
**Kayla Reopelle (New Relic, Inc.)** 47:49 Hmm.
**Robb Kidd (he/him)** 47:50 I don't know about the other two, of deciding whether to emit the timestamps as… events. Or logs.
**Kayla Reopelle (New Relic, Inc.)** 47:57 Hmm.
**Robb Kidd (he/him)** 47:58 Or, attributes.
On one hand, other instrumentations are doing it.
On the other hand.
The more options we give, the more knobs, it gets complicated, and where do we stop?
Which I respect.
**Matt Wear** 48:16 Yeah, I kind of feel like we could get away with this with no knobs if we just said that Queue time is a useful thing to add, and I don't see, like, any… The only thing we have to do to do this is a subtraction somewhere, so as long as you can do that subtraction in a point in time where you have access to the span, it seems reasonable to me that.
**Robb Kidd (he/him)** 48:43 The implementation is trivial. Like, in the implementation.
**Matt Wear** 48:48 Yeah, I think for a trivial implementation and one attribute, I don't think this needs.
Hadab?
**Robb Kidd (he/him)** 48:58 So we'll just do it. Like, we're going to add queue latency to the spans. Enjoy.
**Matt Wear** 49:03 I mean, is that a crazy thing to do?
**Robb Kidd (he/him)** 49:05 I'm…
**Matt Wear** 49:06 Stop me if it is.
**Robb Kidd (he/him)** 49:07 I'm wholeheartedly, I just didn't want to, like, start adding new behavior to people. Yes, I'm a huge fan of just put Q latency on it. We know what it is. We put it on there.
**Kayla Reopelle (New Relic, Inc.)** 49:16 Yeah.
**Matt Wear** 49:17 And I feel like there could be an argument for doing this on the rack span, too, because I think we kind of have that same.
**Kayla Reopelle (New Relic, Inc.)** 49:22 situation.
**Matt Wear** 49:22 where we record… We record something as an event, that helps you compute the… It's all latency, or maybe it's already there. If it's not there, we should do this to rack also, I think.
**Robb Kidd (he/him)** 49:39 Okay, I can investigate that. And I can investigate, I think there was a note earlier about investigate what our other, instrumentations for background job runners do.
**Kayla Reopelle (New Relic, Inc.)** 49:50 Okay.
**Robb Kidd (he/him)** 49:50 Job and other things, and see if we can… Make this a consistent experience across… So… alright.
I still would like to drop those span events, but… If that is… people need more time to think about that.
**Kayla Reopelle (New Relic, Inc.)** 50:07 Drop them as in…
**Robb Kidd (he/him)** 50:09 Just don't…
**Kayla Reopelle (New Relic, Inc.)** 50:10 them? Yeah, don't them?
**Robb Kidd (he/him)** 50:11 Don't send them, or… Maybe somebody cares about the times, but doesn't want to pay for span events because some backends charge per event.
Put them on a… put them on the span as attributes was the… was the other half of this proposal.
**Kayla Reopelle (New Relic, Inc.)** 50:29 Maybe that's a discussion topic for next time, is how we want it.
deprecate… span events, what that looks like for us in our Ruby instrumentation.
**Robb Kidd (he/him)** 50:39 Okay. Then in this issue, I will… Trim down the proposal?
I guess it's, trimming down the proposal, like, I'm gonna put queue latency on spans, which seems not controversial, and not even an option.
**Kayla Reopelle (New Relic, Inc.)** 50:53 And I guess it could be a subtask if you wanted to leave the metric stuff in there, and we just keep working on it.
**Robb Kidd (he/him)** 50:59 This issue with the, like, Sure.
**Kayla Reopelle (New Relic, Inc.)** 51:03 Or whatever it's called in GitHub, they're related.
Dropdowns. Okay.
Okay, cool. We're getting close to the end of our time.
Anything on auto instrumentation, or… Other… actually, I do have one more contrib thing, since you're here at Bart. I wanted to make sure that the rack and action pack, IP attributes went out at the same time, so those releases will go out after this meeting.
**Bart de Water** 51:42 Zoom, thank you.
**Kayla Reopelle (New Relic, Inc.)** 51:51 Alright, comments?
Good advice.
See you next week!
**Robb Kidd (he/him)** 51:59 Bye-bye.
**Kayla Reopelle (New Relic, Inc.)** 52:00 Thanks, everyone.
**Bart de Water** 52:01 Right.
