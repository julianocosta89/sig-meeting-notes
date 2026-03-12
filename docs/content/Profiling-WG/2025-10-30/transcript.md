SIG: Profiling WG
Date: 2025-10-30
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Josh Suereth** 03:35 Hey, Florian and folks, I am only going to be able to hear… be here for the first 30 minutes.
So, if there's a chance, Braden's here as well to talk about a Semcov, PR.
Braden, I… I hope you don't mind, but I was… I think we might need to address some of the, resource-related protocol stuff first.
If that… if that's okay, would you guys be okay prioritizing that while I… while I can attend?
**Felix Geisendörfer** 04:05 Yeah, sure.
**Josh Suereth** 04:06 Okay.
**Felix Geisendörfer** 04:29 Yeah, in that case, do we just wanna… Start with that agenda item, and then do the review action items.
Yeah.
3 minutes, we can get started. Very much.
**Fraggle Rock (ca-wat-brt3)** 04:44 So, I may have met some of you before, but my name's Braden, I'm at Google, I work with Josh, and I'm a member of the System Semantic Conventions group, so we own the process namespace and the system namespace, and We're mostly thinking about the… you know, the host metrics, sort of like gathering metrics about a VM alive, that sort of thing. But the process executable, which is an important entity.
for you folks is gonna be in our namespace, so nominally we're the ones reviewing it. And while I was reviewing it, the current active PR, which I linked, has the executable name as an identifying attribute.
The executable name strikes me as… kind of an unstable choice, during the lifetime of a process. Like, presumably the executable is going to be related to the process entity in some way. Like, there might be a HASA relationship or something, and the name of an executable can change during the process of a lifetime.
But what that would result in would be the… the name of the executable changing would suddenly identify a whole new resource, according to OTLP.
So… I am not super… not super keen on that being the identifying attribute. It seems like the… The closest alternative to… to that is the GNU build ID.
I don't know if that alone is enough, because in that namespace, we need to be able to say, on any system, this is how you… identify a process executable, and I don't think every executable has a GNU build ID. I think… is that… is that only with GCC, or only, like, with an ELF executable? I don't… I'm not fully familiar with what that… that property is, but it's not universal enough.
So either we could call that, like, process.linux.executable, in which case it only matters that we can identify it on Linux or on certain platforms, or we might need to come up with a A better, more universal way to identify An executable that's relatively stable through the lifetime of the process.
So that's basically what I'm here to discuss. I don't know if anybody can go ahead.
**Christos Kalkanis** 07:05 Yeah, so Rayden, I don't know if you saw the comment I left last night, in that pull request. I think Josh asked for an explanation or clarification from the profiling folks, and I jumped in and left a comment there. So the build ID that I recommend for mapping one-to-one executables is not the new build ID, it's a custom hashing scheme that we came up with ourselves, and we specified as part of OpenTelemetry profiling. So it's a very simple hashing algorithm.
That, you know, you can apply on Linux or Windows, pretty much anything. It's just a way to come up with a deterministic has for any binary. And in profiling, this is what we use when we want that accuracy, right?
Which is typically symbolization.
Because for visualization, so far, we're fine with having multiple different executables collapse under the same entity, and that introduces fuzziness, right? Because you could have different versions of the same executable with similar functionality.
Or even, you know, drastically different executables with entirely different functionality that just happen to have the same name, and then they would be essentially collapsed under one entity.
And then, we leave it up to the user to find other ways to differentiate.
**Fraggle Rock (ca-wat-brt3)** 08:24 Okay.
**Josh Suereth** 08:26 So, I mentioned this in the previous meeting, what do we think about having the executable be identified by the build ID, and have name be a descriptive attribute? Because then name is allowed to change.
So, the idea would be, in the model, the build ID is identifying, and you can use that for attaching symbol tables and that sort of thing. But, because you have the descriptive attribute of name.
people can still group by and find things by name, right? So if you want to make a flame chart with name, totally fine, but the default model is that the build ID is identified.
**Christos Kalkanis** 09:01 So, would the implication of that be that when we do the grouping in the proto, like, the resource… like, we would group by build ID, essentially, right? Is that what this implies?
**Josh Suereth** 09:15 That would imply that, yes.
**Felix Geisendörfer** 09:18 And build ID here refers to the hash that Christos just mentioned, or to a… to be done?
**Fraggle Rock (ca-wat-brt3)** 09:23 to the house.
**Felix Geisendörfer** 09:24 Okay, perfect.
Yeah, that sounds good.
**Josh Suereth** 09:30 I'll give you a second option, okay? The second option is we consider this an attribute of a profile.
I don't know… I don't know how I feel about that or not. Like, the question is, will we need to attach any other data to Right? To build ID.
Or by build ID, that is not a profile.
Will we need build ID for, like, metrics, for logs, for events, that sort of thing? Maybe. Maybe not.
If the answer is yes, it should be an entity, it should be a resource. If the answer is no, it can be a profile attribute.
**Christos Kalkanis** 10:19 I think for the uses that I have in mind, I can't think of any use case where I would want something on top of build ID, because the build ID is enough to, you know, differentiate executable with absolute certainty.
And then… The descriptive attributes, yeah, could be somewhere else.
I mean, the question really is, like, if we do that, then you would need to impose that… the housing scheme that we use, you know, we have to be consistent across, total, right?
Because the entity then becomes a process that's specified by this build ID.
**Josh Suereth** 11:01 Yeah, yeah, I mean, that's kind of what my question's getting at, is, like, the, We want to model this, we want to make sure it works. So this hashed ID, and this notion of executable, is this an important enough concept for us to include at the resource level, which all of OTL could make use of?
And, yeah, I think that, if we… so, I could go either way here, of this is only a profiling thing, and we keep in the profiling signal, and it doesn't show up on the resource.
I could go with, this is an entity, and we share it with everything, because, you know, we don't know if we're going to use it or not, but it's safer to model it there, because it feels right.
the ID that you choose, the way you would specify the semantic invention would just be, this needs to be a hash that uniquely identifies the executable binary in some way, and you could describe what it means without how.
And then you're… that's the idea behind the semantic convention, right? As long as people can use it as a repeatable ID, If we ever need something besides the profile to hash it the same way, then you'd show your code. But initially, all… the main thing we're doing is just describing if someone else builds a profile.
a profiler, and they want to use executable and build ID the same way you use it. What's the meaning of that, you know, attribute? So you can just describe that it is… needs to uniquely address in this fashion, here's where it should be the same, here's where it shouldn't be the same. You don't have to actually expose the entire algorithm.
Make sense?
If you need an example, you can look at the specification for trace ID.
Trace ID is supposed to be relatively unique, right?
And some of the bits need to be random, but not all of the bits. We allow you to do crazy things, like, I think Amazon was putting timestamps in some of the bits, and some of the other bits were actually random.
And that, that's allowed in Trace ID.
OpenTelemetry doesn't do this at all, right? OpenTelemetry trace ID is purely random, and all bits are random.
But the way the specification's written, it's flexible.
So, as long as you can leverage the thing as a unique ID, that's what matters. Go ahead, Felix.
**Felix Geisendörfer** 13:20 Yeah, so… my… Answer to your question whether this should be a resource-level thing for all the signals would probably be yes.
But I think that does imply… that the algorithm is shared, because otherwise you can't do correlation across signals, which is important for hotel, so, Yes, but yeah, I don't think the algorithms and implementation tell us we do this.
**Josh Suereth** 13:49 Okay.
So, because the other topic is going to be rather large, I think, making progress here, if we take the straw man of this, we're gonna have the executable have a unique ID, We're gonna take the algorithm from profiling and find a way to share it over time, and executable name can be a descriptive attribute, and that would be an initial proposal for how to model this.
Does that sound fair?
Beautiful.
This is a good tie-in to the conversation I want to have about the protocol. So, the entire goal behind like, profiling.
Oh, sorry, first of all, Braden, are you good?
Do you have what you need?
**Fraggle Rock (ca-wat-brt3)** 14:37 Yes, I am. Thank you for explaining, clarifying the comment. I didn't understand it immediately when I, when I read it, so that's probably why there was confusion at first. I appreciate that. And yeah, I think I'm… I'm set.
**Christos Kalkanis** 14:48 One last thing that just popped in my head. So that's also related to discussions with Felix and Naev that's working on grouping resources and so on. So if we make the build ID, the group, group by characteristic, then… You know, in many scenarios, we'll have, let's say, multiple containers with the same executable that hashes the same way across different containers, and those containers will have different metadata, right?
And then it will become impossible to have that metadata be resource attributes, which I think is in one of the proposals that maybe Evo or NAIF are working on, or what Datadog wants to do there.
So we won't… we will no longer be able to, attach some metadata as resource attributes.
**Josh Suereth** 15:37 So, so, we're allowing multiple entities to participate in a resource.
This, this is already true today. So, Effectively, you could have build ID and container ID, and then you would hash on the two together.
would be the thought there. So, you know how they, like, their proposal hard-codes specific set of attributes, and I was making comments about, you can't do this, it needs to be a flexible set? It's because, like, in practice, when people create a resource. It's actually a couple identities together, and some of those identities, are only unique within a bounded context.
And some identities are unique, like, more globally. For example, pod name, container name, those sorts of identities might only be unique within a Kubernetes cluster.
If I'm operating within a Kubernetes cluster, they're all I need. But if I'm operating, like, across Kubernetes clusters, I might also need a Kubernetes cluster name to be added.
And that's a decision that we actually let users make.
generally, the way they make that is the cloud provider adds cluster information on top of what the Kubernetes resource detector does, and then you end up with cloud-based things, you end up with Kubernetes-based things, and you end up with other things, like, that you've defined. That's why resource detection is, like, a list of stuff you use.
And that's why we're trying to be very firm about, with this entities group.
trying to simplify the story, because right now, it's a bundle of attributes, you have to consider all of them identifying, and you have to hash all of them when you do your grouping. Every single one.
Which is crazy. So going forward, what we want to do is be real picky about what is identifying and what is just bluff for, you know, groupings later. So we can say, cool, container ID, that's going to be identified.
Build executable ID, that's going to be identified. If you need to group for resource, take those two attributes, that's it.
Right? If somebody gives you 3 identified attributes, you need to group by all 3.
**Florian Lehner** 17:44 I think the question Christos asked introduces more to the topic we discussed on Wednesday in Slack, that we have a lot of these identifying attributes, not on the profiling resource level, but on the sample level, which is a sub-level. And, yeah, and I think that's… the more burning point.
**Josh Suereth** 18:04 Yeah, that's what I'm saying, this… This goes into the next topic of, like, the reason… the reason we want you to use the resource Part of our protocol, is because we want those attributes in resource, so when we… so we all do the grouping and joining in the same way, so we can have correlation.
If the design of the protocol is preventing you from putting attributes on it.
then we basically have failed, because the whole point is, group by resource in the collector should be the same regardless of if it's profile, or if it's trace, or if it's events, or if it's metrics, right? So I can group by resource, so I can understand the origin of things.
That's one of the correlation things we want. If the attributes that people expect in resource are not in resource.
then the whole notion that you can reuse the collector transformation code for resource is violated anyway, right? Because you're not putting the data where people would expect it. The notion that you would have resource key for doing, like, routed pinning. I don't know if you saw, like, there's a… there's a, a way to do consistent hashing and routing in the route. I think it's called the routing connector in the collector, right? That has the notion of using resources, a place to pin things.
If you're not putting the data in resource, you would go to a different spot than any other signal.
So… what I want to solve, like, the real thing we want is the ability to have the correlation behind resource. And so, if the dictionary part of OTLP is causing friction, where you're not putting it in resource.
Effectively all the things that we wanted to avoid building in the collector, like custom handling for profiling.
We would have to build anyway if you don't put the data in resource.
Right? We'd have to customize for profiling, because the attributes wouldn't be where we expect them in the data model.
So, this is why I wanted to have the discussion about, like, okay, what will it take for us to get those attributes there, and to make that aspect of joining, merging, you know, routing working? Because that… let's solve the end-to-end journey, not the little tiny thing that's kind of getting in our way right now.
Okay, go ahead, Felix.
**Felix Geisendörfer** 20:21 Yeah, I think just, using what you just said to answer Krista's question, to me sounds like the answer for the… problem of having multiple containers with an executable with the same hash is that there's going to be multiple pieces of identifying information, not just the executable hash, but also the container ID, and those together, basically all the identifying attributes together are going to do the grouping in the profile payload that we generate.
Does that make sense, Christos?
Sloania has a question.
**Florian Lehner** 20:54 I have a question around resources. So, if you go away and, use references, in the resource attributes, where should the dictionary live?
because, yeah, we can use the profiling dictionary, but then we go back the step forward with making resource attributes, or the changing resource attributes for being compliant with hotel collector, other stuff.
But the profilings Dictionary is… very unique to the profiling signal, I would say.
For the… for testing, I think that that's fine, but we probably need a long-term answer to this.
**Josh Suereth** 21:41 Yeah, that's… that's why… why I wanted to have the conversation. I want to start having those discussions now with the collector folks, and… and what we want to do here. My… my thinking is, first of all, I think the… the dictionary option is really good, the thing that you built. It's a good amount of compression. And it actually would have been good if we had done that for all of OTEL.
In OTLP itself.
I think it's too late to make that change to the rest of the signals in a non-breaking way.
But, because of the way signals are kind of unique, because it's resource profiles, not, like.
Like, you don't have to necessarily put resource in resource profiles, in my opinion.
This is where, when we integrate profiling into the collector, because you are a new channel and a new input, yes, it's going to be more work.
But this is where I think we could design a, like, a resource that would be called, like, a resource ref or something, that will leverage your dictionary locally, and we can design the processing for profiling. I would love for that design, actually, to impact the rest of OTLP at some point, because I think that what you've done, would actually be a clear win for most of OpenTelemetry.
having a dictionary. I actually think, I've been doing some experiments myself with protocols and stuff, and just having a dictionary is a significant win for OpenTelemetry. No other changes.
So, there's a piece of me that would like to see that, but I'm not asking you to do that. I think for now.
what we want to do is make sure whatever we need to get the resource attributes that should be in resource, in the resource section of profiling, should happen. If that means that you… we invent a new resource data structure.
For the profiling signal by itself.
that uses the dictionary, and then we update the collector to engage with that. When the collector engages with it. That's what we'll have to do.
In practice, if you look at the technologies we're talking about.
You can, because OTTL and the transformation languages that are used in the collector are kind of an abstraction on top of the underlying system.
you can actually have a divorce between what people see when they write code in OTTL and the actual representation on the wire. So we can have that engaged with the dictionary.
That is actually a thing we can do. If you need a prototype of that, we can work on that. There's a whole mess of OTTL experiments I've done, if you want to see, like, crap that you can do in OTTL. We can actually… we can solve this, I guess is what I'm saying. It's more work, it's harder.
But I actually think it's worth it. So we can give people a model in OTTL that looks like what they expect for a resource, but we can have it use this dictionary for profiling. And profiling looks different, yes, dictionary is used everywhere, but if it means that you have the protocol that you need.
If it means that resources go in the place that we want them to do correlation within OpenTelemetry, I think end-to-end picture, we're in a better spot.
then if we force you to do things the way OpenTelemetry does it today, and you don't use OpenTelemetry the way it's intended.
Go ahead, Felix.
**Felix Geisendörfer** 25:11 I'm just curious if… we need to go the painful route of potentially doing a profiling-specific resource message type, since I think we can just say that there's going to be… I think essentially what your pull request does, Florian, like, add a new field to the existing resource message, and then the only question is, like, how does it find the dictionary? We can just say the location of the dictionary is signal-specific, and some signals do not support a dictionary yet, right? And that is the implementation detail that the collector needs to be aware of. I checked the collector code.
all the access of resource attributes is done through, a getter API, so there's an actual function call, so we should be able to hook into the code gen for that that generates it, and basically just, check, hey, is this a profiling payload? And if yes, it will know how to do these reference lookups. So, in that case, nothing in the collector other than that code generation stuff that needs to be touched would need to be aware of this change, and it would allow for other signals to adopt dictionaries in the future as well. So I… to me, that seems like Better than trying to go the route of, like, a profiling specific resource message.
**Florian Lehner** 26:28 For me, the question really was around where to have, or which dictionary to use, because if there will be, at some point, a… Signal across, dictionary across all signals.
Then there needs to be a synchronized switch with auto collector components and all, OTEC Collector, and that's… that's the tricky part I want to avoid. I saw… Or I did some of the implementation for OTTL, and it can get nasty in there.
**Josh Suereth** 27:01 Oh, I hear you. I'll answer real quick. So, there will have to be a signal-specific dictionary, because all, like, signals are not sent on the same batch, they're actually different calls. So, we're not going to be sending, like, the same signal and the same thing. So, I think we will have to have a signal-specific dictionary.
If we wanted to evolve to where, like, the dictionary can be shared and there's some sort of stateful thing.
And you can remember the dictionary from call to call, and we want to share the resource dictionary between all things. I think at that point, we're talking a different protocol. Like, that's… that's just a little bit too… too far.
So, we need to talk about what we can do that unblocks profiling and is non-breaking. So, the proposal to add this to core resource, the main thing we'd want to do Is we'll have to advertise that breaking change.
In a way.
That no one engages with it until our, you know, until everything is in place that we feel like people have been aware that this is coming, and then we can unlock data using it. So for profiling, you would use it right away. We can update the collector, we can warn people this might come to other signals, but then it's like a one to two year timeline of, okay, let vendors adapt to understand this is coming.
and deal with the fact that there's a, you know, a dictionary, then we could greenlight it for other signals. But I still, you know, from that standpoint, let's unblock profiling as our number one, and if the timeline for getting other people to support dictionaries is a long time, or… Never, because we don't add the dictionary.
And so, there's nothing to reference, so you can't use it.
Bye.
I'm actually okay with that in the interim.
or okay with that for a time. Like I said, I think getting dictionary and OTLP is a 2-5 year time horizon.
So, it's not something that would be fast for any signal. For profiling, I think it's not a 2-5 year, I think it's a, you know, couple month time horizon that we could do this.
**Florian Lehner** 29:13 Yeah, sounds good to me. I think we have to… do now the work and, start experimenting with it. Thank you for your time, for taking your time, Josh.
**Felix Geisendörfer** 29:24 One question, Josh, before you might have to run.
Since you seem pretty bought into the need for dictionaries, including on the resource level, how much work should we put into benchmarking? Because that's something Tikran is asking on the request.
I'm fine with doing it, I think it's useful to do anyway, but I just want to ask if you think it's unnecessary.
**Josh Suereth** 29:53 No, I think we should benchmark to show this, especially for, like, an average profile. So, if we can get a benchmark, even a trivial benchmark that just says size compression.
I think that's… that's worth it. So, yeah, I… When it, when it comes to, When it comes to the protocol, there's a few things we want to make sure that we have for every change that's provided. One is, you know, a benchmark, a rationale, and a use case, right? I think you have the rationale and use case. We do want to make sure we have the benchmark.
And I… Tigrin also is pushing for not changing OTLP, but having new protocols, like Steph.
I don't think that you can, like… Some of the optimizations that are in other things are not applicable.
where OTLP is used, and so I think that, for a variety of reasons, let's do this in OTLP, at least for profiling. If we don't add the dictionary and the rest of OTLP, and we go to a different protocol, like something like OTL Arrow or Steph, I'm okay with that as well.
for profiling, I think we have to do it this way, the way you're doing profiling now.
So Tigran and I have to discuss. We did briefly talk across all of the TC, and Tigrin, unfortunately, where basically the TC agrees that it would be better for you to use resource and throw a dictionary in there.
Rather than having you not use a resource. So, if we get profiling data to prove this, that will help.
to get Tigrin on board. But I think you need both Tigrin and I approving the direction going forward, so I would write the benchmark.
**Felix Geisendörfer** 31:37 Okay.
**Christos Kalkanis** 31:40 So…
**Josh Suereth** 31:41 Sorry, that was long-winded.
**Christos Kalkanis** 31:42 Thank you.
**Josh Suereth** 31:44 I gotta bailgun.
**Christos Kalkanis** 31:55 some changes that Josh wants, which is essentially a change in semantics, right? We changed the way we group. Nothing in the current protocol, goes against this. So the only remaining question is one of efficiency, right? So we could go ahead today and simply change the code in the generators, for example, the BPF profiler, to group samples profiles differently, and throw the attributes on the resource level, and that would abide by the… what Josh wants.
But they wouldn't be efficient, or we assume it wouldn't be efficient, because we haven't done any benchmarks, right?
Because we have… currently have no way to deduplicate all the attributes.
So the remaining question is one of efficiency, and how that dictionary that deduplicates attributes that end up in the resource looks like.
Is that, is the understanding shared across people, or am I, you know, going in a tangent here?
**Felix Geisendörfer** 32:55 No, I think it makes sense. We will have to try out the benchmarking and see what the difference from the dictionary, but I mean, we kind of know, like.
what kind of payloads are gonna look bad, and which ones are gonna look good under the new proposal.
Essentially, the more unique processes you have that have very little samples, each one of them, the more you're going to benefit from a dictionary, but the more you have a small number of processes with a lot of samples, the less benefit there's going to be. So I think the bigger question is almost about the realistic data distribution.
But I think we can… hand-wavely, like, take what we're gonna do, probably take, like, a Python workload where we take a Python app that spins up one process per CPU core, have, like, 16 plus CPU cores, run a little bit load on that application, and call that, like, good enough for the start of the discussion, but yeah, then we… we'll have to ask the question, like, what do you expect to see more? I think, like, seeing a lot of small processes is actually pretty common, so I don't know what you all think, but…
**Florian Lehner** 34:10 Yeah, I think the fastest way forward with these benchmarks would be to implement a custom reporter package.
That just implement… that just, uses these new protocols and writes down the… Writes down the… Data, like, compressed stuff, not compressed stuff, and stuff, all these… Open questions.
**Felix Geisendörfer** 34:34 I don't know if you saw my comment on your pull request. I made it just before the meeting. Naev and I came up with a slightly different idea. Our idea is we take OTLP data in today's format, and then we're going to write a tool that allows converting it to particular, this proposal, like splitting it, like we're talking about right now, and moving either with a dictionary and or without a dictionary, and… and basically, yeah, just taking data in a stable format of profiling and converting it into future protocol change proposals. That should also be pretty flexible as we maybe discuss other protocol changes.
In the SICK.
And probably a little bit easier to maintain and build than, like, customer portals for the profiler itself.
**Florian Lehner** 35:21 Yeah, I didn't see this comment, sorry.
**Christos Kalkanis** 35:26 Yeah, that sounds good to me. I mean, like, you don't want to do what I did last time, when I benchmarked the different stack representations, because, like, you… it's going to be a mess.
**Felix Geisendörfer** 35:36 We looked at it, it looked like a lot of work, and we were lazy, so we were like, let's try this other thing.
**Christos Kalkanis** 35:42 Yeah.
**Felix Geisendörfer** 35:47 Okay, so… Any more thoughts on this? If not, I would suggest trying to get us back to the normal agenda of reviewing action items. Everybody cool with that?
Alright, maybe I'll also share my screen. One second… So, okay, what do we got here? Alexi is not here, if I saw this correctly.
But I think the status on this one, I know, I think you left a bunch of comments, Florian, and some other people did, and I think we're waiting for Alexi to follow up.
Does that sound right?
**Florian Lehner** 36:42 Yeah, I would say so.
**Felix Geisendörfer** 36:44 Okay, just capture that.
Then… I think this one is done. Sorry, P-Profotel converter is the same thing, right? These two items, and I think I saw that this actually landed. Maybe, Florian, you want to talk a little bit more about this?
**Florian Lehner** 37:16 Yeah, the first part landed, so what is missing is the… the other way around, so converting from… hotel profiling to PTROF.
Yeah, with the most recent discussions, I… did not finish and clean it up yet. I have some code, but… Yeah, motivation.
Did get a strike with the recent discussion, so I have to get it back.
**Felix Geisendörfer** 37:48 Okay, yeah, motivation in the sense, like, just, that the protocol might be changing, and you have to update it again, or what was…
**Florian Lehner** 37:56 Yes, yes, and all the work in Electro Collector Contrib and collector is, it was… this was work over months, and now we have to change it again, it's… It will be a little bit of effort.
Especially looking into OTTL.
**Felix Geisendörfer** 38:17 Can you help me understand a little bit what… what needs to be done there? Because I thought, like, what I was sketching out earlier would be pretty opaque to the… most of the collector.
**Florian Lehner** 38:30 Yeah, as Josh mentioned, we have this translation layer in OTel Collector called OTTL, which is quite transparent for the user to use, interact with the signal.
And, yeah, there is a ton of work that started by Tim back in… February, I would say.
And and there's a lot of specific stuff, and with all the changes we will introduce on the resource level, this… has a high impact, and, our approach of using dictionary there, causes a lot of, code, because, it's some kind of, additional language that is used in the hotel ecosystem. And, this language is used to transform, filter, enrich,
**Felix Geisendörfer** 39:25 You name it.
**Florian Lehner** 39:27 And, yeah, it's, it's really powerful, but, To get it done, it's also a lot of work, so yeah.
But I think we need to get this done anyway.
**Felix Geisendörfer** 39:43 Okay, I will definitely take a closer look to OTLL to understand it a little bit better. Thanks, Lauren.
Plug in there.
Okay, then I will… Lexus 1, and… So, in terms of to-dos, I guess… so this is not P-Prof, hotel collector converter now, we need the other way around, right? OTLP…
**Florian Lehner** 40:10 Right. April.
**Felix Geisendörfer** 40:11 So I'll just update this action item, OTLProf.
I'll… I guess I'll leave Alexis, or do you want your name on it, or should we put Alexia? I don't know why it was posted.
**Florian Lehner** 40:23 You can assign it to me. I think I have some code, Alexi considerates more on the profiling, or on the protocol checks.
and make sure that we are compliant, I think this makes sense.
**Felix Geisendörfer** 40:36 Yeah, oh, sorry for leaking your email address. I don't know why it's doing this.
**Florian Lehner** 40:42 No.
**Felix Geisendörfer** 40:42 All the spam you get, you can forward to me, that's okay.
I will put this in here.
Okay.
Oh, did we put archive on top or bottom? I keep forgetting.
I'll put it on the bottom.
So, A few context propagation documents, so any update evil?
**Ivo Anjo** 41:16 Yes, I have a bit of an update I dropped already below, I can go through it quickly, so it's here. So I… Yes, as we kind of discussed last week, I've opened the PR on the Sikh profiling repository with the proto-format that we're using for process contest. There's already been some feedback there, so appreciate all the feedback.
I also chatted with some of the SDK Tracer folks, and for instance, for Java, they told me that there's this extension mechanism in Java that kind of makes it very easy to plug in automatically to the hotel Java SDK without actually changing the SDK, and I was able to use it and have, like, a nice demo of how we can, like, just kind of say, oh, you add this to the command line, and then, like, and you already have the hotel Java SDK, and you start publishing this information, so… That's another nice thing to demo how it works.
I also spoke at the hotel specification SIG meeting, and they kind of suggested we should turn the proposal doc into an OTEP.
which I'm working on now, I think it makes sense, so I'm… my plan is, probably tomorrow, I have, like, almost a working version, so basically turn the existing document into the OTEP format. I'll share in OTEP profile, so we, hopefully we can get some feedback from this group first, and then, like, sometime, like, maybe mid-next week, if, if people think it's in reasonable shape, I'll open it in the open telemetry specification repo, and we start the discussion there as well. And the thread level stuff, no progress there, so that's the more disappointing part.
**Felix Geisendörfer** 43:02 Okay, cool, thanks for the update. Any… Questions for Evolve?
**Christos Kalkanis** 43:09 If I've been through the… because I've been away for the last two and a half weeks, I was on PTO, so I read your updates as well, looks good to me, I approved your pull request, and then Damien reached out to me, to tell me that you reached out to some of the SDK people with the… Yeah, so it's good to… I mean, if the Java folks have no problem with us using the Java FFI, you know, that sounds good to me, basically, so…
**Ivo Anjo** 43:35 Yeah.
**Christos Kalkanis** 43:36 That was an awful question I had, yeah.
**Ivo Anjo** 43:38 Yum.
They did raise, like, that using the new API, well, doesn't work for existing versions, but I think it was, people understood that, yeah, we might need to have a separate implementation for the older versions, but especially since we have this flexible mechanism, we can always say, like, okay, on… if you're on modern Java, maybe you use this one. If you're on older Java, maybe, like, turn on this flag, or it automatically decides which one to use, so it shouldn't be very hard to fall back.
**Felix Geisendörfer** 44:15 Okay.
Yeah, thanks for all the work on this.
Next item is… I'm gonna skip this one, Owner Wanted, Jonathan, I will copy this here… So, 724, let's see where that is… Sure. Is there… yeah, go ahead.
**Christos Kalkanis** 44:49 Yeah, so Josh left a comment yesterday, I saw it last night, and I replied here, and I'm not sure if he's confused, because I don't see a conflict with… like, I think this PR is ready, and we can match this. I don't see a conflict between this pulley request and what we just discussed today with Josh, like, the new resource grouping that we're moving towards.
Because this pulley request is all about clarifying how we encode different samples, right? To avoid repeating samples. Essentially, how we put the observation points for each sample, which is the value and the timestamp, and how those end up looking.
Which has nothing to do with, resources and where the attributes go, because there is nothing in the documentation, or in the documentation strings in this pull request that makes any, requirements for how one should, or where should you put the attributes, and so on.
So my impression is… That maybe there's some sort of misunderstanding here.
And, we can move forward, but… I would like George to actually reply, yeah.
And of course, the other possibility is that, you know, I'm… I'm wrong, and I'm missing something.
**Felix Geisendörfer** 46:08 Yeah, no, thanks for replying. That sounds reasonable to me, so I guess we could just wait until Josh follows up.
Boom… Florian, at payload format, yeah, do you want to take this.
**Florian Lehner** 46:28 Waits for someone to merge it, did not have success getting someone to merge it yet.
Oop here.
**Felix Geisendörfer** 46:35 No, no, no.
**Florian Lehner** 46:36 people.
**Felix Geisendörfer** 46:39 Yeah, that rings a bell. We discussed this last time, right?
Yeah, thanks for following up.
Alban… Is Alban here?
**albancrequy** 47:07 Yes, I'm here.
**Felix Geisendörfer** 47:09 Hey.
**albancrequy** 47:10 Yes, I emailed security at kernel.org mailing list, but I did not receive any reply. I sent a reminder yesterday, and I said that if I don't hear within one week, I will send, I patched to add a feature on the public mailing list, but without mentioning the details of a security issue.
So, I don't know if… some… I don't know if the absence of reply means nobody cares, or they think there's not, Big deal, or if it's lack of time, I have no idea.
**Felix Geisendörfer** 47:50 Yeah, sounds reasonable to me. Sorry to hear that nobody's replying.
Sounds like a good cause of action to eventually just mail out a patchwork.
Thank you. Any… any other comments on this? If not, I'll take us to the next one.
So we get a bunch of Alexi ones. Maybe I should just actually copy all of these.
My life a little bit easier.
So, where's 732?
I guess this is approved and waiting for merging?
Oh.
Some comments need to be addressed.
Okay.
Okay, let's put that in there.
Mmm… This timestamp duration conventions, I guess… There's no PR for this yet, or does anybody recall seeing one?
Not… I'll just say, okay, yeah.
You know, updates.
Don't see below? Wait.
**Florian Lehner** 49:34 I think we can remove the profile comment string indeed says, action items.
Because we landed, semi-convention, and, we removed already the field from the protocol.
So, I will just mark this as resolved. I think there's nothing left to do.
**Felix Geisendörfer** 49:57 Okay.
Okay, I will… thank you, I will fix this off.
Or you did, yeah.
**Florian Lehner** 50:09 Which you can be copied.
**Felix Geisendörfer** 50:09 to the archive section, that's great, thanks.
**Florian Lehner** 50:12 Just do it.
**Felix Geisendörfer** 50:14 Fantastic. And let's see, where were we?
sample type order attribute, yeah, I think this needs a PR as well, and my X is not here to update.
But I think that was basically because we… want to make sure we can round-trip, PROF with multiple sample types, without losing the sample type order, right? Yeah.
And I think I had a comment on, like, a proposal, I forgot whether it's linked, but I think Alexi knows, so it's probably fine.
Reach out, NF, reach out to the specificationSec, on whether the instrumentation scope email UL lies, Okay, this seems to be done.
It's nice.
**Florian Lehner** 51:19 I will just mark it as completed. You'll do it, yeah.
**Felix Geisendörfer** 51:23 Awesome, thank you so much. It's very useful. Okay, and then Alexi, doc URL eprof attribute. We still need to address it, need to send confr… June… this is closed?
Okay, so I guess it's still pending on a PR on Semicon.
Okay, I think that was covering all the action items, and we have… Don't have much.
remaining agenda items. Florian, you had one, but I don't know if this is overlapped with the conversation we already had.
**Florian Lehner** 52:06 this was just a, topic for… that we can discuss with, Josh, so that's… I just learned about the technical community meeting notes, and in there, there was the decision that we are… that we have to be compliant with the resource attributes.
I wasn't aware until, I think.
this Wednesday, that this even exists, this document, and we can access it.
Yeah.
I just wanted to place something in here that we… I don't have a place to discuss it, but, I think it…
**Felix Geisendörfer** 52:42 Okay.
Cool, excellent. Then, I suppose, does anybody have any last-minute, agenda items they want to throw in the ring?
If not, we can all get 8 minutes of our life, but no, Crystal, I see you on mute.
**Christos Kalkanis** 53:02 Yeah, so, looking ahead until the end of the year.
what do people think? Do you think it's realistic that we'll be able to get an alpha out? Because an alpha would have to, since the TC made the decision, we'll need to now rework how we do the attributes. We have to list them to the resource level.
But… If we do the minimum there, and I think Josh is okay with that, based on today's discussion, which essentially is the pull request that Florian has opened right now, which introduces References for resource attributes.
Right? If we can get that in, then the benchmarking, some benchmarking that demonstrates, performance.
I think we should be sad, like, we don't really… Have at anything else.
**Felix Geisendörfer** 53:49 Yeah, what I don't understand is the OTLL wasn't a critical pass, that sounded like a lot of workflow, Ian. Go for it.
**Florian Lehner** 53:55 I think we cannot, unfortunately, move on to alpha state. With the reasoning for alpha, we need to… some kind of stability in the collector side.
And, if… by any chance, the PR draft I just opened on the proto for the resource gets merged tomorrow. We still need some release of the protocol first, so that we can adapt the changes in the collector.
And there's a long chain of… this happening, so, yeah… will be a rough… there will be a lot of people involved to get this done by this year, I would say.
If we can convince people to match.
Or get an assignment on the references in the resource attributes.
And we get, release of the protocol soon, then… Could be, yes, a lot of work.
**Christos Kalkanis** 55:03 See?
regarding the protocol, we can ask for a release of the protocol anytime we want. That's what Tigran told me last time, so that shouldn't be a blocker. What could be a delay, would be the changes in collector, and also the SDKs, right?
**Florian Lehner** 55:18 Yep.
**Christos Kalkanis** 55:20 But, yes, so in asking this question, I'm more interested in, like, the list of things that we absolutely need to do before the alpha. So I'm more interested in figuring that out, rather than, you know, having an exact deadline, and we say, okay, this is… it looks as if it's… it's gonna be maybe possible to get the alpha out by the end of the year.
If we're not blocked on anything else, or if nothing else, nothing new comes up.
But, okay, so far, yeah, it's good to know that, okay, like, if we do those changes and introduce references for research attributes, it looks as if that's the last thing we need to do. And all the, you know, dependencies for that, right? Including collector, protocol, SDKs.
**Felix Geisendörfer** 56:02 That sounds about right, and I… I think that means that the benchmarking stuff is on the critical path, so we will try to get this done ASAP, so we're not losing time there. And then hopefully we can be in a place where we have the pull request in a state where it could be merged by the next SIC meeting, and then we might have a shot at alpha by the end of the year.
**Christos Kalkanis** 56:24 Yeah, we do.
**Felix Geisendörfer** 56:25 We need to push on this pretty hard in the next two weeks if we want to have a chance.
**Christos Kalkanis** 56:28 So… the reason I keep bringing up the alpha is because, like, there have been a few cases where it became apparent that we need, you know, fresh eyes to look at what we've done here. Like, we are conditioned by our previous experience in profiling, all the work we did, so we need people to start using this, even complete beginners, like, people from different, experience levels, and I know that we… probably don't have anything for KubeCon North America, but I saw that Floria and Felix, you have a session in Amsterdam next year, the KubeCon.
So hopefully.
**Felix Geisendörfer** 57:03 We've submitted, I don't know if we're…
**Christos Kalkanis** 57:05 Gonna get it, bud. Yeah, so hopefully that's accepted, and then that's, you know, hope enough time for us to have the alpha out, at least by then.
And that would be, like, an advertising point to the rest of the world.
you know, we can always write a blog post, but having a live session that gets recorded, and then it's on YouTube, and then we can, you know, if it's something else.
**Felix Geisendörfer** 57:28 Yeah, I mean, we basically… are banking on the fact that we'll have an alpha to show, because it's in the title of the JubCon presentation. So, it would be okay if we're further along, but it would be very embarrassing if we're… less far along, and we have to change the title. So, yeah, that's definitely the goal, and it's going to be a good spot to announce it and ask for people to check it out and start using… giving us feedback.
Cool. Any, any other thoughts?
No, then we still get 3 months back. Thank you, everybody, for participating, and have a nice local time.
**Frederic Branczyk** 58:19 See y'all.
**Florian Lehner** 58:19 I'll see you!
**albancrequy** 58:22 Goodbye.
