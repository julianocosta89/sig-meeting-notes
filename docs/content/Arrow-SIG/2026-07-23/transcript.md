SIG: Arrow SIG
Date: 2026-07-23
Duration: 56 minutes
============================================================

## Zoom Recording Transcript

**Aaron Marten** 04:46 Laurent, I can't… I can't hear anything, I don't know about others.
**Laurent Querel** 05:03 Can you hear me better now?
**Aaron Marten** 05:05 Yes, thank you.
**Laurent Querel** 05:07 Okay, great. Sorry for that.
Yeah, so my question, I don't know if you hear anything from the beginning.
If not, I will reiterate.
So, I will consider that you, you, you hear something.
So, is there any, regarding this, 1870, OTAP exporter is missing shutdown signal when facing errors.
I think we have someone working on that, but I'm not 100% sure.
Duo, do you know that, or someone else?
I think I would keep this one, because I'm… I need to check… So I will remove the state status, and I will… Keep this one open.
Double-check after this meeting.
Mmm, silicon.
Perf test, add bytes, also going to throughput, Do we have SIGO with us?
Dish.
**Aaron Marten** 06:46 He's not on the call right now.
**Laurent Querel** 06:48 Okay.
Hi, Josh, I didn't see you.
Yeah, I think we can keep this one also, because, It's probably something that we still need to do.
Add broadcast dispatch strategy for node output.
Mmm, I think we have this one, so I think we can, just close it.
Oh, no.
From node outputs.
Yeah, that was an idea that we had at some point.
I think it's still an open question in terms of design.
**drewrelmas** 07:37 I think…
**Laurent Querel** 07:37 Yep.
**drewrelmas** 07:38 Is this not… oh, this is unrelated to topics.
**Laurent Querel** 07:42 Yeah, yeah, yeah. I made the same mistake initially.
I think it's still an open question, Just for context, so, when we have a node with multiple outputs.
By default, as opposed to what we have into the GoCollector.
By default, it's a round robin.
We don't really have, duplication of broadcasts of the messages to the values output.
That could be an option that we add.
to do… to achieve that, in fact, we have a specialized processor, which is named Fanout, and we also have this concept of topic use Between multiple, between multiple pipelines.
I still think it's an interesting aspect of the design that we need to think a little bit more, so I will remove the steel.
No objection.
**drewrelmas** 08:58 No, you, you actually raised what I was gonna say, where we have fan-out processor and, soon-to-be topics to handle this sort of thing, but…
**Laurent Querel** 09:07 Yeah.
But topics are very specific, because it's really across across, pipelines, and sometimes I think this, Broadcast strategy could be interesting inside the pipeline.
Yeah, I'm not sure. The composability of the approach that we have, the fact that we try to develop, usually, Really specialized processor that we can combine together.
make me think that, the final processor is probably good enough, but, no.
But it hurts to think about that a little bit more. Standardized create naming convention. I think this one should be done, right?
**drewrelmas** 09:55 We've danced around this a number of times, and we've never actually gone and made the pull request.
**Laurent Querel** 10:01 Mmm.
Mmm.
It's talking about publishing on press.io, Are we talking about that, or are we talking about naming conventions?
**drewrelmas** 10:18 Well, we're… we're.
**Laurent Querel** 10:19 Tighten-related, yes, okay.
**drewrelmas** 10:21 It's related, yeah.
Basically, like, this would be a prerequisite before we even think about, create releases.
**Laurent Querel** 10:29 Yeah, I think that's something we have to decide anyway for September, so sooner.
Because if we… if we consider that we stabilized, A lot of SIG in the system.
Around September.
We probably… that will be probably the right moment to, to reconsider that.
At least to define definitively what will be the prefix for the crates.
Yeah, so definitively, it's not, stale.
Okay, improved pipeline, core allocation, placement strategy, I think that is related to… We just need to find… create this connection with another one that is, an ongoing… let's see, there is, a PR today.
I think it's from Nalit.
Go… What's the PTROSCO in the shared world.
Placement, okay, 24-7… Okay.
Remove denied tunnel exclusion for Weaver dependencies.
Maybe, Drew, you have a… The idea about this one.
**drewrelmas** 12:26 I know we did this at some point because there was a Weaver… okay, I'll check into this one. I think…
**Laurent Querel** 12:36 Gokhan.
**drewrelmas** 12:37 might be covered now that we've done a bunch of Weber updates.
**Laurent Querel** 12:41 Yeah.
Okay.
**Joshua MacDonald** 12:43 I suspect that's true. Thank you, Drew.
**drewrelmas** 12:45 Yeah, I'll go look at that right now.
**Laurent Querel** 12:47 So you, you close beta if you… Validate that, okay, great, great. Optimize codons to work in place on recall batch. For you.
**drewrelmas** 13:00 Yeah, this is also me. So we have the condensed attributes processor, which was something, it's in the contrib… it's a contrib processor that takes a bunch of attributes and, concatenates them together on a single attribute, which is a use case that we had. There's… really not a good way… I'll take a look at this again, as well. You can put this on me. And I'll either close it as not worked on.
**Laurent Querel** 13:27 Okay.
**drewrelmas** 13:28 Yeah. We don't need to talk about it here.
**Laurent Querel** 13:32 Okay, okay, so… try to open…
**drewrelmas** 13:36 Oh man, these are all opened by me.
**Laurent Querel** 13:39 Yeah.
**drewrelmas** 13:43 So, we are actually doing pretty well in the release process. I would almost feel comfortable with closing this as completed for now.
**Laurent Querel** 13:52 two weeks.
**drewrelmas** 13:53 get to a point where we actually want to release on crates.io. Like, we've already… we've built Rust into… our release process, and we've, you know, strengthened our changelog, tracking, so… I feel we're actually in a good place until we decide to release on Crates.io.
Unless someone else has, feedback, but, you know, I've been trying to do every 3 or 4 weeks, cutting a release, which for Go is publishing a module, and for Rust is currently simply git tagging a commit.
**Laurent Querel** 14:38 Okay.
**drewrelmas** 14:40 Great, thank you, Laurent.
**Laurent Querel** 14:44 Okay, no issues with U.S. CI jobs.
**Joshua MacDonald** 14:51 Anything…
**drewrelmas** 14:53 Yeah, this is probably closed. This was from way, way back when.
**Laurent Querel** 14:58 Yeah, wicked.
**drewrelmas** 14:59 when we first added RustCI.
**Laurent Querel** 15:03 Okay, so close.
**drewrelmas** 15:04 Oh, actually, so the one thing left is on Josh here, not on me.
**Laurent Querel** 15:08 Oh, okay, okay.
**Joshua MacDonald** 15:11 which is the next one in the list, which I think is still not stale. This is about Unicode license, and I've… I see it. I just marked it on stale, so if that helps.
**Laurent Querel** 15:22 You just knock what, sorry?
**Joshua MacDonald** 15:24 I just marked the child issue not stale.
**Laurent Querel** 15:27 Okay, but I think we…
**Joshua MacDonald** 15:28 Okay.
**Laurent Querel** 15:30 Probably keep this one also.
**Joshua MacDonald** 15:31 Do that.
**Laurent Querel** 15:31 Yeah, I don't think there is any RTMS mechanism in place for that.
We… okay… Again, drew…
**Joshua MacDonald** 15:42 That's the same one.
**Laurent Querel** 15:44 Same one, sorry, yes, okay.
Okay, improved load generator, so let's open this one.
Because I'm no longer sure… So, we're using to generate traffic, probably… We did a lot of improvements in this space.
I have the feeling that it's, we made a lot of improvement in this, in this area.
Especially because we had, this, effort for the benchmark, oralty blog post we published on June.
So, I think we can blow this one.
Any objection?
**Joshua MacDonald** 16:42 Nope.
**Laurent Querel** 16:43 Okay, this procedure. Okay.
And finally, local inter-pipeline communication. That's me, let's see.
Whoa.
Yeah, that's definitively, I think, we would keep this one, open.
Especially the… We start to have processors or exporters that require… so, for example, let's take the… there is one processor that, on which I'm working.
At least at the specification level.
Which is, the temporality processor.
That gives you a way to transform delta metrics to cumulative metrics, for example?
And, because of this freight broker approach.
We need some way to root metrics per the identity.
to make sure that every metric with the same ILTT ends up into the same Accumulator, same, state where we will transform this data to… to cumulative. And that's a common pattern, so we need a nice solution, probably based on On the topic, mechanism, To achieve that.
So I will, I will remove the sale. I think that's an important one. We need, Yeah, a standard solution to solve these kind of issues.
And I will keep it open.
Okay, so I think we… that's the end for the style lists, so let's go to the next one, which is the… which are the new issues. So, do we have, oh, that's me, I created this one, but in fact, it's, And then treat… that Shanmi, in fact, created, he had some issue to create the GitHub issue. So, on this one, and I know that Microsoft is also interested by the per-Kafka receiver exporter.
So we, we have something functional.
But I will not qualify the Kafka receiver exporter as production-ready.
So we… We are basically extending… what we want to do is extending the validation framework use the… there is a mock cluster exported by the Lib or the Kafka trade that we use.
And, and we want to exercise, many, scenarios when you add a Kafkafka broker, remove it, increase the number of partitions into the topics, and so on. So all those complex situations, which are Unfortunately, traditionally very complicated to handle with self-care, and that would require also some, some effort on the receiver-exporter side.
So, that's the reason of this, entry. A lot of work there, and that will be the focus, For us, for the next following weeks.
Because we have a dependency on that, for some internal stuff inside a file. And I know that, so drew… or Joshua, I think you, you, you also have some interest on Kafael, and you, you were talking about, Supporting some new format.
**drewrelmas** 21:05 Yeah, I can talk about this. So, the, So yes, we're interested in the Kafka receiver. It's still very hazy on our side, like, I don't have hard, requirements or commitment that we're going to do this, but… One thing I'm thinking about is, syslog Ceph is a very common use case, and we have our own syslog Ceph receiver that has a parser module, which Utkarsh, implemented.
So, my thinking is, if we reorganize things a little bit, I know right now the receiver only targets OTLP Proto and OTAP Proto.
But there's no reason we couldn't support any other, standard decoding type, hopefully re-implementing, or sorry, not re-implementing, hopefully reusing existing parser logic from other dedicated receivers that we have.
So in this way, if we picked, I don't know, I'm picking something out of a hat here, but a certain type of JSON, logs that we wanted to support, we would have one set of decoding that is used both in a native standalone receiver as well as usable in the Kafka, machine.
**Laurent Querel** 22:20 John.
I'm thinking about something, maybe it's just a dumb idea, but, I have the feeling that maybe there is something interesting there.
We… we told Crescently, maybe last week or the week before, about a new type of extension.
I think I name it, the PData Encoder Extension, or something like that.
With the idea of, Generalizing what we already have, so we have a mechanism, a pass-through mechanism, that gives us a way to basically keep… the original OTLP format untouched.
And there are processors and exporters that know how to handle this kind of, OTLP, untouched, un-serialized.
Objects, and just route them to the right destination, or, Based on the signal type, for example.
And we introduced this pilot encoder extension to generalize this concept, and that could be used, for example, for the Parquette encoding.
Where we receive packet, file, we just route them to the right destination, and maybe we have a… A generic object store exporter that takes this packet and put that somewhere.
So I'm thinking that maybe the same… The same, extension could be used by… So, the Kafka is… in this state, it's a message blocker, so we receive a message.
With a specific format, and we do something with it.
Paul, we send, a PDATA object of any kind to a Kafka topic.
So, I think it could be natural to have Kafka receiver exporter using the PDATA extension.
To basically participate to this, pass-through mode.
And then we could imagine that we have a PDAT extension for syslog Ceph.
And, and, and it's becoming, like, like any, like, VOTLP, project we have today.
At any point of time, we are able to go back to of that format, when it's required.
But we also know how to… get from Kafka, or from any, in fact, message broker.
Any, encoding that we support.
**drewrelmas** 25:17 So this is actually really interesting to me, because I know today we talked about how the internal representation of the data flowing through the pipeline is always OTAP or OTLP, but really, we're saying we don't care what the format is, and we'll only transform it to OTAP to do a required transformation or something.
**Laurent Querel** 25:36 Yes. Yeah, I think this PDATA encoder extension is, One of these fundamental pieces that we need to introduce Defined very well.
We need to think about what needs to be, I think the minimal… if we want to keep the… the pass-through mode that we have, which know… and we know that this passcode mode has a lot of advantages in some scenario, and very good performance.
At the minimum, I think we need, obviously, a type to determine Which encoder, which encoding, is there the type of the signal? So, for example, syslog will be obviously logs.
Parquette could be anything. I think the only constraint will be to consider that something encoded with specific type needs to be uniform in thermal signal type. I think that's the… The minimal, requirements.
obviously the lens, and I think that's probably more or less what we need. And on the extension side, we need the encoder-decoderUD.
That the extension will provide.
Yeah, okay, so I think that's, definitely another, interesting area.
that we need to explore, probably before September.
Oh…
**Joshua MacDonald** 27:17 I see, I put a link to your… you called it pluggable p-data byte representations issue in the chat.
**Laurent Querel** 27:23 Oh, yeah.
**Joshua MacDonald** 27:24 I was gonna raise the same thing. I think… I think it's useful to think about this. It would require answering maybe at least one question.
or at least for us to think about. In the syslog Ceph receiver, we receive these byte payloads, and then we batch… we batch apply them to impending OTAP payload, because that's going to be efficient. If you imagine sort of tunneling syslog Ceph payloads through a pipeline, now you're going to end up with these little individual syslog Ceph records, and you're probably still going to want, for efficiency, to batch encode them.
And it makes me… it leaves me thinking that you might… Just have a pluggable representation and still want those receivers to essentially hold the state that is going to accumulate them and put them into an OTAP.
Otherwise, like, later in the pipeline, when you want to put them into a batch, you will then have to Your pluggable representation might need to know about batching, essentially, and the fact that when you use it, you're going to want to assemble batches, not just individual one-to-one translations.
Maybe that's a point of complication.
**Laurent Querel** 28:41 I think it's, it's manageable, because right now, the batch… Processor is already able to, do we have, Mr. Jake with us today… oh, no, you probably don't.
**Joshua MacDonald** 28:54 The batch processor has logic just for byte representation, and it will concatenate OTLP bytes, so you could imagine having the plugin for these extension representations.
**Laurent Querel** 29:04 Yes.
**Joshua MacDonald** 29:05 to the batch processor, you are going to do the plugin batch, which will use the plugins capabilities, yeah.
**Laurent Querel** 29:12 Yeah, we could, we could, imagine extending the…
**Joshua MacDonald** 29:17 At that point…
**Laurent Querel** 29:18 encoder with something saying, okay, there is a very simple mechanical way to batch things together, like we do for OTLP, that we… we could also do that for the syslog CEF.
Because it's basically just, yeah, putting the one after the other.
maybe with a separator, but that's something simple enough to be considered, I think, into the PS encoder.
**Joshua MacDonald** 29:48 And then the syslog Ceph receiver becomes little more than just a network socket and some payloads that are part of an extension plan, and then… Anyway, yeah, looks good to me.
**Laurent Querel** 30:06 Great.
I'm lost, where I am. Okay, no?
**Joshua MacDonald** 30:19 Up top.
**Laurent Querel** 30:19 Okay, okay, okay.
Okay, Kafka receiver announcement, so it's in the same, domain, it's, just a refinement of this one. We just want to… to improve a few things on the Kafka receiver side.
**Tom Tan** 30:37 And I have a question on the Kafka receiver. I think this is a parent issue, right? I think that, like, in the future, if there's any subtasks or… feature requests created under it, maybe we will mostly consider it as accepted, right? Or still…
**Laurent Querel** 30:53 Yeah, yeah.
Yeah, yeah, considering the… I agree. And do you think that it's feasible to… to take into account the hierarchy of GitHub issues, To propagate, Both direction, based on different rules, but propagate the… Stage state, or the… the triage state.
**Tom Tan** 31:19 Okay, thanks, yeah.
I'm clear now.
**Laurent Querel** 31:23 Okay.
So this one, introduce an RFC process.
Oh, I think, we already discussed this one, right?
**drewrelmas** 31:38 Yeah, I don't… yeah, we…
**Laurent Querel** 31:39 Yeah, I think it's, I think it's 7, 7 closed now.
Because we… we started to use the… LFC process.
Do you agree?
I think we can close it.
**Joshua MacDonald** 32:01 I think we can, yeah.
**Laurent Querel** 32:03 Okay.
Okay, add generic load dependency, status, optional readiness, and at this one also, I think we already discussed it last week.
It was about, you open it.
Just to double check.
Yeah, I think we discussed it. So right now, the really easy… elephant… It's just, looking at… Any error, raised when a pipeline is created and we start it.
There is no participation… there is no possible participation By the nud, to express that, we are ready or not to accept traffic. And, and… There are situations where… I don't think we have that right now, but there are situations where Maybe a dependency used by a processor, an external dependency.
We need some, I don't know, communication and exchange.
In order to be ready, let's imagine a cache or something like that, external.
So that's just a way to let nodes declare that they want to participate to this, global state.
We need a design and blah blah blah, but, I think that's something we need to achieve at some point.
**Joshua MacDonald** 33:42 The collector has a module, which I believe would be called Health Check V2, or… it's like a… it sounds a lot like what you've described. I just want to refer to it so that we can, like, at least compare notes.
**Laurent Querel** 33:54 So I'll let you add, maybe, reference to this effect.
**Joshua MacDonald** 33:58 I will do that.
**Laurent Querel** 33:59 Okay, great.
Retry processor, although indefinite retry, yeah, so… I think this one is, Right now, we have no way to say we want to retry infinitely.
It's a reprise that we have internally, for a team. I will not discuss the reasoning behind that. I didn't agree with them, but that's what they want.
So, and does it hurt to support it?
So I don't think it's controversial.
And he, objection.
We're kidding.
Okay… and, So that's still an… so I don't think it's, see, yes, we need discussion for this one. We need to find the time to, at least, for the meter to, to get, a more detailed list there. I think we also had a discussion with Trask.
Regarding, on the, Hotel Arrow Martenere, channel.
But, we… I didn't see any follow-up.
Joshua or Drew, can you, check with, with Trask? The goal was to have like, a working, session with him to think about Phase 3 and… Potential discussion with the governance committee.
I remember, like, a poll where, everyone was saying, okay, I'm available these days, these days, but, we never, we never saw the meeting at the end.
**Joshua MacDonald** 35:58 True. I was on vacation that week. I said…
**Laurent Querel** 36:00 Oh, yeah, that's the reason, okay.
**Joshua MacDonald** 36:01 I'll check in with Trask.
**Laurent Querel** 36:06 Great. Okay, so I think we are at the end of the list, just… I don't know if, obviously mountainers are aware of that, but, we recently added So let me show you where you can find this pull request dashboard.
When you go on the… list of issues.
You have ear, a pinned issue, which is the PolyQuest dashboard. It's a special issue.
Most likely the stale system will detect it. So regularly, we will have to remove the stale, but… This one is, like, a… yeah… An automatically updated issue that a workflow is updating And where we have, all the GitHub PR that are, listed here.
Is there, basically an easy way to capture the state, and what is, where… what PR need attention, basically?
So the, the edge is considered the, the fact that it's, or the CI is working or not, if there is any conflict, so that's a nice way to… for people that want to review PR, you can consult this page and, very quickly.
determine the one on which you have either an interest, I should say, an interest, and are ready for review in terms of, whatever you consider important for review.
Okay, so, let's go back to the… So we have two… Two elements on the agenda today. Gokhan and Josh. So… how much time do you need, Gokhan and Josh, just to determine… we have a pretty, really small list.
**Gokhan Uslu** 38:21 I need a very short…
**Joshua MacDonald** 38:23 Same, it's a short discussion, I'm thinking 5 minutes for me.
**Laurent Querel** 38:28 Okay, so, Gokhan, if it's short, also, let's start with you.
**Gokhan Uslu** 38:34 Yes, so if you can open that link, I recently made a PR that got merged.
And, I consolidated auth-related… started consolidating auth-related capabilities into this folder, and there is this models file, and in there, there's authorized identity that I created there. Models, not mods, not…
**Laurent Querel** 38:57 so it gives you…
**Gokhan Uslu** 38:58 The sort of folder, and that models folder, yeah.
**Laurent Querel** 39:01 Okay, okay, okay.
**Gokhan Uslu** 39:02 And there's, identity.
Object there. So… so a few questions there.
Would, Would it ever be a good idea to have an identity attached throughout the context of the pipeline?
Would it make sense to maybe, work together with, especially tenant-based?
implementations, stuff like that, and how do we want to treat this? Is it having any capability? Is it a good place? Should we even just make it We have its own area, we're capable to use these types, et cetera, stuff like that.
**Laurent Querel** 39:46 Yeah, understood. For me, it's typically… And… a general and, a general consideration, something important enough to create an RFC That we can review, where you will, Investigate the relationship with, like you said, multi-tenancy, for example.
We have another effort regarding multi-tenancy, an ongoing effort on which Joshua is working. So, yeah, for me, the right way to go is to first talk about the modalization, the specification via an RFC, and That will, give you a way to… Yeah, to assemble the various pieces related to that.
**Gokhan Uslu** 40:39 Okay, I can create an issue for that.
**Joshua MacDonald** 40:43 I'd like to add, so some of you have seen an early draft of my first proposal on multi-tenancy designing, and I got a tremendous amount of feedback, basically telling me I was nowhere near finished.
And, so I am incorporating that, working on it right now.
apologize for the delays. I… I don't know that anything I've written is in shape for Gokhan to just, like, build on at the moment.
So I'm worried that we've… that, in some sense, I am blocking this now. I don't mean to.
the… the… in the Go Collector, there is a very clear, cut-out place where you can put We've called transport headers, or, like, request headers at this point, which are just sort of, like, arbitrary key values coming in with a request.
In the Go Collector, there's also a very dedicated place for the result of auth. Like, this is the thing that your auth extension returned at the moment when you ran auth, which essentially says, here's your network port, here's your identity, everything the auth plugin returns has a special place, is all I want to raise.
And… and that, whatever we call it.
is subject to design, but there will be a place, and I would say affirmatively yes to what you're proposing, Gokhan, just that we are going to put the result of auth into the context.
And it will be… Special in the sense that we will know that that result came from auth, not from arbitrary key values that the pennant provided, for example.
**Laurent Querel** 42:27 Yeah.
I think, definitely, there is an interaction between oath and militancy.
But I continue to think that there… we probably have a lot to do regarding authorization.
identity, independently of empty tenancy, so I don't think it's blo… what you are doing is necessarily blocking I'm pretty sure that, Go can, can, like, like you said, investigate what exists in the Go Collector.
Look at the values, mechanism.
that we already use to similar space. You mentioned transport headers.
And, and, and consider all of that, and end up with… an approach that will be compatible with the rest, or… it's still time to make some adjustments globally, if we need, if we consider that maybe what we did for the transport headers are not exactly In my opinion, it's so correct, but maybe I'm wrong, and we just need to refine that a little bit.
But I still think that we can create an independent RFC And at some point, yes, obviously, we will have to connect the dots between the two, but,
**Joshua MacDonald** 43:51 Yeah, I agree. The… then I… then I would recommend that, Gokhan, you… you should continue this idea, of documenting what… what you think we should do. It looks to me like… The auth plugin, the auth component will need to return something which is special, in the sense that it will declare itself as being produced by an auth extension that was… that establishes some sort of trust. That's the main thing that we're trying to get to.
Is that these… these are special types of request metadata that come directly from an auth extension that we somehow trust.
Therefore, we can use those values, keys and values, from the auth extension to say, you know, I've certified this network port, like, I checked its TLS, so you can use this network information that I gave you, because I'm an auth extension, and I assert that. That's the type of thing that we're looking for.
**Gokhan Uslu** 44:47 Okay, would it, maybe a little bit too much, too specific to the implementation part of it, but it kind of helps me, conceptualize in my head.
Would it, would you imagine this being as a module of its own, like, where, art models, or, like, the special types.
Have its own area, maybe in the engine crate, or etc, or could we think of it as I mean, the capabilities are already first class, the types of models in there are first class.
And, you know, just designed the objects and documented such that It is understood that they are being maybe attached to context or something like that.
And any kind of type that exists in Engine could be treated that way.
It doesn't matter where the location is.
**Joshua MacDonald** 45:40 That sounds about right to me, if I heard you correctly.
the… the… whatever special support we need to say this is the result of an auth, that you can use then to… for some sort of trust, would be a self-contained, data type, I would say.
**Gokhan Uslu** 45:59 Yeah, and one of the things that I'm thinking is that if I keep all the related models and capabilities today, that would mean, like.
Any, art-related, Like, definitions should come from capabilities, even though it might be used by other components as well, or extract art-related models.
to its own scope.
Where capabilities or other concepts can also use it, just to prevent, you know, this… situation of, oh, I needed this new author-related model it's not for capabilities, it's for something else. Where do I put it? I don't know. I'm just trying to think about how to approach this, maybe if it is too specific.
Stop me there. But yeah.
**Joshua MacDonald** 46:54 I just pasted in the sidebar a block of text from the collector. It has a file in the top level of the core collector called client. It contains this type called ClientInfo. Client info contains an off data type. I think that's, roughly speaking, what you're going to create here.
**Gokhan Uslu** 47:11 Okay.
**Laurent Querel** 47:12 Okay, guys, I suggest that we move to the other topic.
Alright. So, Josh?
**Joshua MacDonald** 47:19 Yeah, so, I put up a PR. It's not really ready for anyone to review, but if you look at the first link there, you can see that I also opened a spec PR yesterday, documenting an algorithm that's a little bit… it's overdue. People have been asking for this for a while. It's not, like, a huge number of requests, but basically, we finished the exponential histogram spec years ago, and it was… it was a lot… it was a lot. It was just a heavy amount of code and complexity for anyone. So at the time, the simplest approach we could do was to write down how you compute the table… how you compute the lookup function using a logarithm.
So basically, just call your math library, do some math, there's your index.
And, It's a little bit slow, it's a little bit inexact, and this PR is, spelling out an algorithm. I'm… you can see a to-do there. I'm looking for help to document how… why we think this is correct. I mean, I believe it's correct, I just want the best explanation. So this is… spec work that I was… that I was waiting to do and now have done, and in the other PR, which is a draft, I want to just briefly discuss how we integrate this without… before asking you to look at this code. So.
the… inside of this PR, you will find, from a prototype of mine, just the raw implementation of a data structure, and that part, I don't need a lot of review on yet. That stuff I've been testing and reviewing myself for a while. But as far as integration.
So what we have here is a new data type, which is, effectively a plain old data. It's like… whereas one counter in the… is currently one word of data, a histogram is a variable number of words, and so it's a… it's a generic that you can choose how many words you'd like to use, and then it, so there's a small and a large size, for example. You could imagine having a 10-word histogram, which has 80 bits of information, and you could have a 26-word, which has, like.
you know, some number to 240 bits of information, and then within those bits, it's going to automatically scale and automatically widen, so that it's going to use those bits as best as it can without ever allocating more. And if you run out of counter space, it will automatically widen, which is to downscale by one. If you run out of room, it will condense by downscaling, which means to condense existing measurements into smaller numbers of buckets. So, the data structure itself, I want that to be reviewed, but that's not my question. Really, what it is, is in the current code, we have this MMSC type. It was a placeholder for this. Min, max, sum, and count. And min, max, and sum and count are like a histogram without any buckets. So.
I've always liked this idea that the basic level of instrumentation for anything that looks like a histogram is the min-max-sum count. It's all you get, you don't ask for more, you just get four values. It's 4 words of space. Now, if I want to add a histogram to that, I can go to the basic, like, the next level up, which I've said 10 words, because that's a 128-byte struct.
And the 26-word value is a 256-byte struct. Those are two options. Now, if I was to put them inside an enum, I would have this wasted space, where I have an enum, which is MMSC for the base case.
which is 4 words, or I could have the 10… the 16-word structure, or I could have the 32-word structure. And I believe this is useful, but maybe not. Like, we could just say, forget it, just always have one type.
and hard-code it. What I was thinking we wanted was to have a… we have this existing idea of a metric level. There's normal, basic, and detailed. I was going to say basic, you're going to get the MMSC. Normal and detailed, you'll get histograms of varying degree, and we'll use a box so that you will not have to Waste the space when you're not using it.
That's roughly speaking what I have here.
that made me think, well, maybe I always want my metric, my histogram in a box, because it's going to be wasted space when I'm not using the MMSC, if I have the MMSC, like, not boxed.
Moreover, the data types are already copied, so I have to do a pretty big refactoring just to make it so I can box metric values, because they expect to be copyable right now, and box is not copyable. So it was just a little bit of an integration question. I wanted to hear people's thoughts.
**Laurent Querel** 52:01 Yeah, I can provide my feedback, if, except if there is someone that wants to talk about something there.
Okay.
My first reaction is, I think we… not necessarily having this alum.
Because, like you said, if we have a box, or, some kind of winter, to the bucket.
And if we integrate this, detail level, that we already use for In general, into the system. We can, yes, we can obviously, It could be, in fact, an option of bugs, or an option of RC, or whatever.
But, I think an option of bugs is perfectly fine.
In this case, and I agree, we could, we could move from the MMN M, N, SC,
**Joshua MacDonald** 53:13 An MSC.
**Laurent Querel** 53:14 Yeah. To the… to the fully sold one by just, Switching the state of this option, from none to some.
And, personally, I don't see any, any issue with that.
**Joshua MacDonald** 53:32 Would you box the underlying aggregator in all cases? Like, if it's MMSC or a histogram of various sizes?
That means the size of the struct is always an option box of some type.
**Laurent Querel** 53:49 Yes, I think that would be the right way to go, so we… Okay.
**Joshua MacDonald** 53:53 That sounds right to me, as well. That's my whole topic. I'll keep working on this, and when it's ready, I will let you all know.
**Laurent Querel** 54:00 I think that the only argument in favor of something I mean, it's a… We need, maybe, maybe we need a benchmark on that, because, Especially when you are in the detailing mode, where you will get the full histogram.
You will, access a lot, in fact, to the bucket, and any kind of state that you maintain for the histogram itself?
So, that will not have the same signature in terms of performance.
**Joshua MacDonald** 54:38 It'll be one more pointer in direction if we add a box. Yeah, that's… that's really…
**Laurent Querel** 54:42 No, I'm…
**Joshua MacDonald** 54:44 It's fair to say I should benchmark this,
**Laurent Querel** 54:47 And maybe the other consideration, I'm just brainstorming, I didn't put a lot of thought there, but, Is it really, when we decide that something… we want the full detail for the, For the internal instrumentation.
Does… is it really related or connected to the fact that we want Instagram or not?
In other words, could we… Ask for histogram, even when the rest of the internal telemetry is not in detail mode.
**Joshua MacDonald** 55:30 To me.
**Laurent Querel** 55:30 I don't have an answer, I think we need to think about it a little bit more.
**Joshua MacDonald** 55:35 Yeah, this is almost a question of just about how much resolution and specificity do we have for metric instruments, like.
I've described this level, which is really trying to simplify the life of a user who wants to, like, turn it up or turn it down, but you can also imagine for every individual instrument setting its level, or on a component-by-component basis, setting the level of shared instruments and so on. Like, this is just a configuration problem at some level.
**Laurent Querel** 56:06 Yeah.
Yeah, I don't have any answer right now. I think we need to think about that a little bit more.
**Joshua MacDonald** 56:19 Thank you.
**Laurent Querel** 56:22 Okay, any last topic to discuss? We… We are close to the end.
Okay, great. I think we can get back the last 4 minutes, in that case.
Again, good session.
**Joshua MacDonald** 56:41 Thank you all.
**Laurent Querel** 56:41 Yeah, thank you.
**drewrelmas** 56:43 Buh-bye.
**Joshua MacDonald** 56:44 view on the Slacks.
**Gokhan Uslu** 56:45 a good one.
**Laurent Querel** 56:47 Right.
**Matt Wear** 56:48 Thanks.
