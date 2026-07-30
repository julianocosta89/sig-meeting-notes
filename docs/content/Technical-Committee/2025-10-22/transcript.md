SIG: Technical Committee
Date: 2025-10-22
Duration: 42 minutes
============================================================

## Zoom Recording Transcript

**Josh Suereth** 01:34 Hey, how's everybody doing?
**Reiley Yang** 01:38 Hey, Josh, Mila.
**Josh Suereth** 01:48 Is there another meeting going on tonight?
Are we just starting late today?
**Reiley Yang** 01:57 I don't think there's another meeting.
**Josh Suereth** 02:26 Riley, do you need edit access to the dock now?
**Reiley Yang** 02:30 I have access… I'm using my personal Google account, so I have to switch, but I'll merge the change after the meeting.
**Josh Suereth** 02:39 Okay, I was gonna say I can, like, do you want your personal account to have access?
**Reiley Yang** 02:44 Sure.
**Josh Suereth** 02:48 I might give my personal account access as well, because I have the same problem all the time.
Okay.
This is recorded, so… is your personal account on the list?
in, Slack.
**Reiley Yang** 03:05 I think so.
**Josh Suereth** 03:06 Okay, I'll get it from there instead of say it publicly.
**Reiley Yang** 03:23 We're, like, 3 minutes past, so let's get started.
Let's see, arming plug.
Okay, so, Josh, go ahead.
**Josh Suereth** 03:40 Okay, if you refresh, you should have edit access.
Okay, yeah, I want to talk about PHP due diligence, so let me… I was grabbing the link, that's why I got distracted. Here we go.
So, effectively, we talked about this before, we had a set of things that we wanted to get addressed, and the PHP maintainers and the C++ maintainers have gotten together and come up with a plan.
So, I actually think this is good to go at this point. The TLDR is that the PHP sorry, the Elastic folks have agreed to, use C++ as a dependency, for key things. For context, this donation is a PHP auto-attributation donation.
it has a few killer features, actually. So, one is that It actually allows asynchronous span writes.
and batch processing over time. So, that's actually pretty killer.
the thing that we were… oh, it includes, a OpAmp C++ client.
for controlling PHP.
we had a couple things from our due diligence that we wanted to get looked at, which was, you know, how are we gonna do, what does security look like, what does code releasing look like, all that kind of things. I've updated the document to include, the criteria, and I'm confirming with the PHP that this is the full set, because we updated this together. But effectively, acceptance criteria now includes working with OpenTelemetry C++ to share capabilities where possible.
So, this would be, leveraging OpenTelemetry C++'s, like, exporter capabilities, resource detection capabilities, and then also taking the op-amp client and contributing it into OpenTelemetry CPP Contrib.
So that other folks can actually make use of this. From what I understand, Elastic is totally on board with this, and I think we have a good set. As future requirements, basically continuing to work with, like, the injector SIG, continuing to work with both SIGs, and making sure that we have a healthy ecosystem overall going forward.
Yeah, I personally think that this is ready to go, and I'm giving it my stamp of approval. So, I'd like to officially denote that in the bug, and just looking for anyone's concerns, remaining concerns here that are unaddressed from the last time we talked about this.
Alright, since we're missing a few people… I will post this in chat.
In the TC chat?
Just… and leave it open until the end of today or tomorrow?
for any further, like, concerns that folks have, and then I'd like to respond to them.
Does that sound like a reasonable timeline?
**Reiley Yang** 07:00 Yeah.
**Armin (Dynatrace)** 07:01 That's good.
**Josh Suereth** 07:02 Cool Alright, give me one second to actually… start the chat message, or I will forget, so… Alright, next up.
Donation… This is another donation proposal.
Embrace.io wants to donate a Kotlin implementation. If I recall correctly, this was designed around, Android and mobile.
And we need someone to do the TC due diligence here. So this would ideally be someone who's familiar with Android, familiar with the Java ecosystem.
And, familiar with, kind of, like, browser-side SIG, if possible.
If not, we'll have to go to the randomization thing on the TC list and pick the next person who's not… hasn't done A due diligence recently.
**Liudmila Molkova** 08:01 I've seen Jack commented on the donation proposal, so maybe we can ping Jack and ask if he's interested, because he's familiar at least with Android.
And Jelly. Okay.
**Josh Suereth** 08:13 Yes. I think, actually, Jack and Carlos would be the two that I think are ideal. If I recall correctly.
Jack just recently did one.
I need to check the… the backlog here, hold on.
Of course, it takes forever to load. On-demand rotations. Yeah, so Jack… Jack actually just did an instrumentation installer donation.
So, for reference, if we go from most recent to previous, I just did the PHP one. Jack, then Riley, then Ludmilla, then Bogdan.
So that's why I was thinking, ideally, it'd be someone who hasn't done one recently.
and someone who has domain knowledge, so let's check with Jack, and if he… if he or Carlos aren't able to do it, we need… we'll have to pick someone random. I do think we need to pick quickly, I'd like to have that also by end of the week.
**Liudmila Molkova** 09:13 I can ping Jack and Carlos on Slack, and we will see.
**Josh Suereth** 09:18 Okay, thank you.
It seems like I have all the agenda items this week, so I'll be doing a lot of talking. Apologies.
Oh, Carlos is here. Hey, Carlos.
**Carlos Alberto Cortez** 09:30 Hey, sorry for being late. Yeah, actually, just in time. I was thinking about this topic yesterday.
**Josh Suereth** 09:36 Yeah, for context, you know, this is a Kotlin donation. It needs Android and kind of, like, browser-y, front-end appy experience. I think that you or Jack are the ideal people to do this donation proposal.
So the question is, do you have time to take it on right now?
**Carlos Alberto Cortez** 09:57 Yeah, definitely. I was thinking that Jack is very busy. I already read the entire issue, the entire discussion there, and I did, sadly, Kotlin in the… no, not sadly, just a joke. But anyway, I did… I did Kotlin in the past. So, it was a long time ago, like, before I joined Lightspept, but I do know stuff. So yeah, I can take that.
**Josh Suereth** 10:17 Great. Awesome.
Let's update that thread. Do you mind commenting on the issue that you're gonna take in?
**Carlos Alberto Cortez** 10:25 Yep, we'll do.
**Josh Suereth** 10:27 Beautiful.
Okay.
Let's move on to the next one. This one might be a little more contentious. I mentioned this in the specification meeting. I wanted to have a brief discussion about it today, because I think we're in a hard spot right now. The Zipkin exporter.
Actually has dependencies on previous semantic conventions, which we have deprecated and removed.
I did not realize… personally, and so I can take the blame for this, that Zip can actually reference the attributes directly in the exporter specification, not in a compatibility specification.
So we, we actually, in compatibility specifications, we actually took those, and we have a section of our spec that says, here are things that SEMCOP has to define.
The Zipkin ones are not in that.
Now, the way this is defined, if we scroll down to… there's this thing where Zipkin needs a service peer.
to export. You have to actually define, like, what you're talking to.
And so… There's a set of conventions it looks at, like the address of the thing it's talking to, that… but we've effectively kind of broken these.
Going forward, I have two questions. One is… what do we… no one noticed that we removed the CENTCOM, right?
So it's either the SEMCOM isn't adopted yet that breaks this.
Or we don't have a lot of Zipkin usage, one of the two.
Going forward, I think there's a few ways we could address this. One is we can add new SEMCOMF attributes at the bottom of the list, which I think would be a non-breaking change.
To help account for this.
we can update the specification of attributes SEMConv is required to use.
So that those attributes actually are, like, things we can't change in SEMCOM, so we… this breakage of Zipkin doesn't occur in the future.
Or option number 3 is… we could actually mark… I don't think we've ever done this, but mark, like, Zipkin compatibility deprecated. I'm curious… the reason I would say that is, like, with Jaeger, right? They support OTLP directly now.
Is that reasonable for us to ask of Zipkin? What do we think?
**Reiley Yang** 13:05 I think it makes sense, at least when I look at the exporter for Jaeger and Zipkin, even if Jaeger, like, as Josh mentioned, has been supporting OTLP, and we've deprecated that, if you look at the download number.
It's bigger than Zipkin.
Like, for something that we've depicated for more than a year.
It still has higher number of downloads.
At least for .NET. And I bet for other languages, that'll be the same situation.
So I agree with Josh, we should explore. Of course, we need to reach out, but, like, what we really want Dipkin to do is they should also support OTLP. And by the way, OTLP is now widely established, a lot of vendors already support that, so I think that's the right move.
**Liudmila Molkova** 14:04 I would imagine that the people with the most opinions would be in the Java ecosystem?
Yeah. And there… I don't know if we have download… probably there is… they're on download numbers somewhere accessible, but they're not public.
I'm… thinking out loud about the options, Joshua mentioned, I don't think it's feasible that we would list all possible semantic conventions that Zipkin Exporter could translate into service peer, and it's… Like, we are doing the best effort with whatever was mentioned in the document originally.
I… would be in favor of deprecating the whole exporter if it does not create some big problems in the Java ecosystems, where it might.
But we can at least deprecate the page that the documents data set it to deprecated, meaning frozen. It will not get any updates in the future, and whatever works today will keep Hopefully keep working until the artifacts are deprecated.
**Josh Suereth** 15:31 Okay, so it does seem like, I was just doing some quick… quick looks, I think the only, the only, OpenTelemetry Zipkin conversion that exists is things that OpenTelemetry cell phones, right?
I don't think Zipkin supports, open telemetry ingestion directly, so we can ask them about that.
And I agree with you, Lyudmila, like, it's not really practical for us to… like, account for all possible semantic conventions with Zipkin.
So, whatever we have today is best effort, and we'll have to remain best effort.
**Liudmila Molkova** 16:16 See, I think there is a module on Zipkin, it's relatively new, that supports OTLP, I'm not 100% sure.
If it's… Part of the service, or it's part of the client.
**Josh Suereth** 16:36 Yeah.
**Carlos Alberto Cortez** 16:40 So you may remember Anuraug.
he was… I don't know whether he still is very involved with Sipkin. I think we should probably reach out to him directly.
**Liudmila Molkova** 17:01 And we can post it up in Telemetry Java. I think the hotel integration with Zipkin was asked by the Spring ecosystem, and they show up there. I can take an action item on, starting a thread and pinging the people.
**Josh Suereth** 17:17 Yeah, yeah, that actually sounds like a plan, and we should do that. I know that there's been some friction there in the past. This particular issue of peer service is one of the biggest, differences between Zipkin and Jaeger, and remains in OpenTelemetry, where we don't… have that as an out-of-the-box thing, and I know that there's been a lot of, Anyway, I don't want to poke at a sore wound. Does anyone still have contact with Anurag to reach out to him? To ask about Zipkin itself?
**Liudmila Molkova** 17:48 Oh, he's on Slack, he actually keeps contributing to the Java, so if we ping him, he might respond at some point.
**Josh Suereth** 17:54 Okay, that sounds great. Let's do that then, as well. So, we can reach out to Spring folks and find out, and we can reach out to, We can reach out to Anurag and find out if he's willing to help us out with this, too.
But yeah, I think, the key thing is.
We noticed we think it's broken.
No one has reported an issue, though.
So… we're in that awkward space of, I'd like to get ahead of this before the community actually starts running into problems, or there's issues. Okay, And in terms of decisions here.
Zipkin support is still important to us, and we need to make sure that we have it, right? It's in OpenTelemetry.
there is a question I have generally around compatibility. Should we take time to take the Zipkin specification and move it into our compatibility section of the spec?
Instead of, like, kind of hidden under SDK exporters that are required.
**Carlos Alberto Cortez** 19:01 Yeah, actually, I think that makes more sense.
**Josh Suereth** 19:07 Okay.
Cool.
One last question, Wazipkin.
What's the impact with our Zipkin exporter and our event decisions?
**Liudmila Molkova** 19:35 event decisions, meaning the span events are being deprecated.
So, we are deprecating them on the API surface, but we intentionally decided to not deprecate them on our TLP. So, the… Logs to span events processor would be the answer.
For Jager and Zipkin, both of them.
**Josh Suereth** 20:03 Okay.
Alright, so, so then… good. Alright, then I think that ends that discussion.
Next one is actually a little harder.
This is around profiling.
So, the profiling SIG showed up at the entity SIG, and was asking about a bunch of IP addresses, and sorry, they were asking about a bunch of entities that they needed to provide. So, like, they want to talk about process, and they wanted attributes on a process, and labels on a process. And we were like, why aren't these just labels on a resource? Like, literally, they're like, we want the ability for users to label a process So that we can identify important things about that process. I'm like, why is that not just a resource attribute? They're like, well, process is not in resource. So we got into details about how the eBBF Profiler works. And… They were like, well, resource is likely empty.
And we said, why is resource empty? Why are all of your attributes about resource on the profile itself? And they're like, well, because we have a cardinality issue.
Why do they have a cardinality issue?
They're trying to fire profiling data every 15Hz, or at a 15Hz cycle.
Okay?
And they want to send, like, little tiny batches of profiling samples very, very rapidly.
So I asked them, is it reasonable for you to just not do that, and send it every minute or so, like metrics do?
Or have, like, batch it longer and do it the same way you would with spans. I think that's a discussion we'll have to get into. That might be an elastic product decision, but their users apparently want this data coming very rapidly and not So that's interesting.
From an OTEL standpoint, I think two things. One, OpenTelemetry is not designed as that kind of a protocol. We are not a fire lots of little pieces of data all the time. We are a batch and send big batches of data, or bigger batches.
Right? It's… OpenTelemetry is about lots of little events.
getting put together. The second thing is, the profiling stake keeps running into this issue where they want to do a lot of data sharing. They want strings to show up in multiple places, and they're unable to use Arrow right now, right? But they want to use OTLP itself.
OTLP itself doesn't have a lot of support for things that PPROF had.
For example, PProf has a string dictionary. All strings in the entire protocol are just index references to that dictionary.
That's how the whole thing works. We have allowed them to do that in the profiling signal.
But they want to do it at the resource level, and they're avoiding putting anything in resource until they can do that.
And so, I want to have a discussion of, can we stop this BS? That seems like… I think we need to… we need… we need two things. One is, what is the conceptual data model we need for profiles to be successful?
And if… and in my mind, if resource and profile is not the same as resource and trace, or resource and metrics, or resource and events, then correlation is broken.
And one of our value props is gone.
So, to me, that is a thing we should not… compromise on.
Where we can compromise is what the stupid protocol looks like to be efficient, to make that Use case happened.
In my opinion, right? So, I think consistency is important, but in this case, I'm suggesting we break consistency for profiling.
And we allow them to have dictionary support in the resource that they have at their top level.
maybe this is something we add to the rest of OTLP, maybe it's not. I don't… I don't want to have that discussion yet, because I think that's a broader discussion we need to have, and kind of discuss between, like, what Tigrin's doing with Steph, what… what Josh and folks are doing with Arrow, like, I think that's a discussion that needs to happen.
don't want to have that just yet. I want to focus on, conceptually.
Do we think that when Profile talks about a process, it should be in resource?
And then, if so.
Are we willing to let our protocol be a little bit different for profiling to optimize this use case? And if not, should we encourage them to not, like, do we need to have a discussion with them about the sampling rate that they're looking for?
**Reiley Yang** 24:48 So for the protocol, I'm curious if that dictionary, like, will live across multiple batches, or each batch, like, after you use that dictionary, it's gone. You don't have to keep remembering everything from the beginning.
**Josh Suereth** 25:03 Yeah. From an OTLP standpoint, the dictionary would have to be sent every single time.
From an implementation standpoint in the profile, they would just kind of have that in memory and just dump it every time.
**Reiley Yang** 25:16 I see, so, so, So if, for example, if we agreed at some point that OTLP will allow this dictionary, even for resource, that That means people can still implement that relatively easily without having to make the protocol fully transactional, like, based on the connection, you have to remember everything from the beginning. So, I just want to check if it's a very stateful thing.
That we'll introduce, which is totally different from the existing protocol, or that's just a minor change.
**Josh Suereth** 25:53 this is… this is just a minor change in the structure. This would not be… like, I… We are not allowing OTLP to be stateful right now.
**Reiley Yang** 26:03 I see. Yeah. Yeah, that…
**Josh Suereth** 26:05 Just be allowing them to have a dictionary in the current stateless protocol.
**Reiley Yang** 26:10 Yeah, then that seems like a viable option.
**Josh Suereth** 26:15 Yeah.
**Joshua MacDonald** 26:20 I'd call that, like, an encapsulation property. We have that in Arrow as well, where there are no stateful cross-request, like, interactions.
And any state of that nature that we build up is hidden in the Arrow IPC reader-writer mechanism, so that once we have a batch of data, it's not… it's self-contained.
**Josh Suereth** 26:42 Yeah.
**Reiley Yang** 26:43 Yeah. This is great. So, I like the stateless fact, because I think OTLP is designed in a way that certain batches can get dropped in the middle.
**Josh Suereth** 26:56 Yep.
Yeah, and to be fair, I think having a stateful protocol Good? Great.
That might be a better use case for this 15Hz sampling thing. And we might want to encourage them to, like, not build OTLP for 15Hz sampling.
But in the meantime, it sounds like we can go back to them and say, look.
It's such a weird… well, they want it to be higher.
They just said currently it's 15Hz, yeah.
what? Dude, it's… everything has to be divisible by seconds, right? So… or, you know, 15Hz… closer to 60Hz. It's a… it's a… it's a power of 2, I think. Anyway… Is my… my math too bad today? I need more coffee.
So… Okay, we'll go back to them, we'll say, look.
The stuff you're putting in profile needs to be on resource.
That's an open telemetry modeling thing.
Let's talk about the protocol itself.
We're, like, we'll allow you to have a dictionary here. Let's talk through what that could look like.
And then, lastly, the sampling rate that you want that's very efficient is not how OTLP is designed. So.
if we're designing an OTLP profile, It's not designed for that.
Architecturally, you need to look a little bit different for OpenTelemetry. If you want to build a stateful protocol on top of that, here are other efforts going on. You can have these discussions, but it's not OTLP.
It's OTLP dash something, whatever that something will be. Or OTAP, I forget what you called the arrow stuff, or…
**Joshua MacDonald** 28:43 OTAP at this point. But again, we've tried to keep the encapsulation property and hide that detail inside of a lower-level system.
**Josh Suereth** 28:53 Yeah.
Yeah.
**Joshua MacDonald** 28:56 The… the… just speaking from my past, the LightStep internal protocol had this same type of design, where there's a dictionary at the front of the protocol buffer, and every string could be an integer, and… I mean, it's totally doable. It gets reasonably good compression, you know, like.
Aero compared with that was, like, winning, but not by a huge margin, you know what I mean? Like, you can get a lot of compression with simple It's not the worst idea.
**David Ashpole (dashpole)** 29:24 Prometheus Remote Write also does this, the 2.0.
**Josh Suereth** 29:29 Yeah, and PPROF does this, so that's where they got the idea. To be fair, profiles already have that dictionary in the current spec of OTLP. We allowed it for profile itself. We just don't allow it on resource, because we wanted them to share the definition of resource for consistency.
to me, I want to share the model of resource, but I don't care about the protocol as much when it comes to this level of detail. Like, I think, okay, cool, let's allow the string table for their resource in their signal.
If we want to come back behind and make that compatible for all signals to have a shared string dictionary, great. Let's… we can figure that out later.
What I want to avoid is what I'm seeing right now, which is the craziness of we're going through weird contortions and getting requests and semantic conventions that are data modeling questions fundamental to OpenTelemetry.
Okay, that's all I have, by the way.
**Reiley Yang** 30:28 So, two points. First, I think the meta might also know, like.NET Monitor is using their own protocol, which does a similar thing here, like… try to compress as much as possible. And that protocol, I believe it can be used for diagnostics, for telemetry, electricity metrics, logs, and also profiling data.
So… so it seems like… like, most folks are doing that, according to the discussion. The second part is, what's the… what's the actual, action item, Josh? So here… here's my guess, what you… you will do. Like, first, you will ask the profiling group, hey, you must put resource in the right place following the OpenTelemetry, con- like, contract. So you're not going to, like, just leave empty resource and put the same thing inside your own dictionary.
So, at least for now. And that's a minor performance problem, but not a breaking change or something for them. Then, if they come and say, but we… like, we have a strong desire, we still want to use dictionary because that's more efficient.
then you would guide them, like, first you would allow them to, like, improve OTLP by having dictionary support on the resource, and then we'll figure out how do we… how do we upgrade the protocol with the backward compatibility and maybe proper versioning, so people can move. And… and it seems like you also believe that having this, like, local dictionary supporting your resource is a good addition.
So that's something, like, if we… like, if we have someone in profiling sake who wants to push for this, then from TC, we should give them support.
Is that correct?
**Josh Suereth** 32:19 Yeah, yeah, I, I… What I'm proposing initially, though, is because profiling is a separate signal, and because the way resource is embedded, we have this notion of resource trace, we have this notion of resource metrics, we have this notion of resource profiles. Resource profile will only have a dictionary-based version.
**Reiley Yang** 32:39 I see.
**Josh Suereth** 32:40 And all other signals will remain as they are.
Yeah. And that would be the path forward for profiling. And then figuring out how and what we want to do to move to dictionaries and other signals, we can figure that out, but that is a large, complicated problem that will involve us.
like, I think it will need TC, or cross-open telemetry, effort to make happen.
Do I want to see that happen? Possibly.
Like, I think there's… there could be some value in having that dictionary in OTLP. I'm not proposing we take that effort right now, I'm proposing we unblock profiling.
And, we would say that that is a direction we would go in OpenTelemetry if we were able to execute on it, and we had the time and the resources. I think we have bigger and more important things to do in OpenTelemetry right now, around stability, around, clearly documenting what's stable around preventing performance regressions. If you look at all the feedback from the CNCF tag around graduation, that should be our focus. So I don't want to spend time on the, protocol, That we don't have to.
At this point. So this is like, let's unblock profiling, we have a direction we can move in the future.
But we're not gonna execute on that direction just yet. We just agree that that'd be fine if we did.
**Reiley Yang** 34:01 Okay. Just curious, maybe this can be sorted out later. Do you see a potential use case that one OTLP batch contains both the profiling signal and some other signals?
for example, if I have similar things to the… Boom.
like the exemplar, I might want to send metrics and traces all together. It makes no sense for me to send two separate batches if I have small batches, right? So, if you see that case, then one having dictionary, another having the same resource, but in the non-dictionary format, that seems like a waste to me, so I… I would suggest at least ask the profiling SEC to do a design. With that in mind, so if we allow Like, a mixture of different signals, then we can have the best efficiency.
**Josh Suereth** 34:52 I like what you're suggesting, Riley, but I don't, like… I think what we're talking about is an OpenTelemetry V2 protocol.
And I think we could actually do that within OpenTelemetry V1. So we have a trace service, a metric service, a profiling service. We could make just a batch service that has a batch signal that has all this data in together.
But again, I don't think it's fair to ask the profiling SIG to design every other piece of telemetry.
That is something for us to do.
So I think we need to do that and step up if we're going to make that happen. And yeah, that's something I'm entertaining. I don't know if you've seen the MMAP stuff I've been doing to improve resiliency between SDK and SDK and Collector, or SDK and Next Step. But one of the things that that has been teaching me is I think we do need to actually… figure out a resiliency model a bit better. There's reasons to have redundant signals. Having profiles on a separate channel actually can mean if profiles fail to send, I don't lose my other observability, so having redundancy isn't bad, in and of itself.
But, the overall data volume of what we're trying to shovel from a process somewhere else, we do need a way to kind of address and account for.
And I think that's… that's… when we talk about, like, performance overhead, when we talk about, some of the things around graduating in CNCF, I think we'll start to… solve these problems and kind of tackle them head-on, and I do think we need to be engaged in that, and kind of pushing it, so… I wish I had more time to drive that, or I had more thoughts here. I just, you know, this is very targeted, what I'm asking for today, is…
**Reiley Yang** 36:38 What can I go tell the profile intake?
Yeah, understood. Thanks.
Okay, so I think these are all the topics.
Any other topic?
**Joshua MacDonald** 36:51 I would, just to tack on to the last topic, add that the Oto Aero project has several times, including a couple years ago and today, imagined a protocol that just mixes all the signals.
Because it's just a batch of error data, kind of either way, with some type of information. It, It raises as many questions as it answers, though, because you… like you were saying, it puts the signals in the same pipeline, it means they're blocking each other, it means that… however, it means they can share resources, so there's something appealing about it, we just haven't really kicked it any further than, having a Essentially, at this point, stated that we think this should be doable, and we know that the current collector is not supporting that type of model.
So, we're, we're there.
But that's all I had.
**Reiley Yang** 37:50 Okay, thanks, Josh.
That, I think we can give 20 minutes back to Arah.
Okay, thanks. Have a good rest of your day. Bye.
**Joshua MacDonald** 37:59 I can't.
**Liudmila Molkova** 38:00 Thank you.
**Carlos Alberto Cortez** 38:00 Dude.
