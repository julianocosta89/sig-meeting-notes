SIG: Arrow SIG
Date: 2026-02-05
Duration: 63 minutes
============================================================

## Zoom Recording Transcript

Laurent Querel 00:00:15 Hi, on…
Albert Lockett 00:00:20 Hey guys.
Laurent Querel 00:00:22 Fair enough.
Doodle.
So…
Who knows?
jmacdonald 00:02:01 Hey, everybody.
Laurent Querel 00:02:05 Hello.
Sure, sure.
jmacdonald 00:02:06 I'm,
I wanted to say I'm… I'm coming down with a cold my family's had all week. I'm not feeling super good. I wouldn't mind if someone did more of talking than me.
Thank you.
Laurent Querel 00:02:19 Okay.
Hi, everyone. So, I encourage everyone to,
to have some, topic for discussion in the agenda.
And also, Pierre to discuss if you, if you have anything.
on your side.
jmacdonald 00:02:40 I have… I'm expecting at least one person with a topic today that's not in the room. Let me find them.
Laurent Querel 00:02:46 Okay.
jmacdonald 00:03:13 Ugh.
Laurent Querel 00:04:50 Did you find a…
jmacdonald 00:04:52 So I'm, I'm trying to reach Gokan. He and I have been talking about this, topic.
Laurent Querel 00:04:58 Okay.
jmacdonald 00:04:58 I pinged him, maybe he'll show up. I… you know, if he doesn't, we can… I have the links there, and then we can… I can say what I know he's doing, and we can at least get some
Some initial feedback, I guess.
Laurent Querel 00:05:10 Yeah, so, So can you add approximately the number of minutes that you need to…
For the corresponding, discussion.
jmacdonald 00:05:23 Sure.
Laurent Querel 00:05:25 For everyone.
I think it's smaller than the two cities, than the 550 units.
Because, based on the number of,
the number of discussions, and I don't think that we will have time for everything.
jmacdonald 00:05:46 Yep.
Laurent Querel 00:05:47 We'll probably have to, to select, oh, extension interface, okay.
jmacdonald 00:05:57 And that's an early piece of work, but I've been looking at it with Gokan, and it's getting to where it's ready for people to talk about, but, it could also wait. I think it's not urgent.
Laurent Querel 00:06:13 Okay, except if there are issues to discuss, I think we can skip it.
jmacdonald 00:06:22 Yeah, I look.
Laurent Querel 00:06:23 November or December.
jmacdonald 00:06:23 over them, there's nothing shocking and new, I would say.
In the last…
week, other than people kind of making issues for the stuff that they're working on, so I don't see any, like, major discussion topics or new surprises in the issues.
Laurent Querel 00:06:40 Okay.
Okay, great. So let's, skip issue triage and go directly to the discussion. There is,
I don't want to start with me, so let's see,
So, Gokal is not that right, for now.
jmacdonald 00:07:04 Not here, as far as I can tell.
Laurent Querel 00:07:06 Okay. So… so, Jake, can you talk about your, OTAP spec, maybe in 5 minutes max?
Jake Dern 00:07:15 Yeah, yeah, I think so, definitely.
Laurent Querel 00:07:16 I will text a note.
Jake Dern 00:07:23 Oh, sorry, you meant… you meant right now, not to… can I do it in 5 minutes? Okay, I thought…
Laurent Querel 00:07:29 No, otherwise I'm ready to go by side, huh?
I'm just afraid to take more than 10-15 minutes because the topic is big, so I'd like to put it at the end, if possible.
Jake Dern 00:07:42 Yeah, definitely. Yeah, I just wanted to bring it up and, and mention it was something I was starting to think about. I feel like it would be, like, something that's pretty valuable to have, for a number of reasons. I mean, onboarding is one, but then, of course, like.
There's also situations in the code that I encounter where I'm like, well, can this happen? Can this not happen? I need to go, you know, check what the go implementation does, that kind of thing. Ask somebody else. So I just feel like it'd be good to have a, you know, kind of a formal spec written down somewhere.
Or we can point to it and be like, this is the behavior that we decided, you know, something that's quick to reference, and…
And yeah, that would just make things, a lot clearer. So what I started doing was just kind of, like, writing down some…
Some things that we need to document, and then maybe also some things that we need to discuss.
And then I just kind of been encapsulating that, in the issue there. And I remember… one thing I did want to bring up is, Josh, I remember you had opened up an issue, I think, in, like, the OpenTelemetry specification repository at some point?
About also, like, you know, like, what it means to have, like, I think an official or, like, alternative protocol for OpenTelemetry. I can't remember the exact phrasing, so I thought that might tie in.
No.
jmacdonald 00:08:55 Yeah, I would say so, yeah, the, like, if we're going to have that, we would need a more formal spec than we have, today. And I agree that I've had the same types of confusion, where you're like, I don't know, it's like, there's a list of types here, which types are valid? Look at the other implementation, that's a thing. So that would be good.
Yeah, for the, for the, for that topic, the major piece of feedback I got when I talked about it in the spec SIG with OpenTelemetry was that
There's not a non-breaking change that we can make, to OTLP or to OpenTelemetry's spec that would just
That would… that would work, like, without some sort of new feature being added that, like, lets you opt in to new stuff. Because there's just not room in the current specs to, like, extend it that way. So we end up talking about content negotiation.
And so that's a very separate topic from how OTAP is specified, but it would be… if we can… sort of like the tax we would pay would be to do work on content negotiation for OTLP in general, and then maybe there's, like, a fast path to get into Arrow that we could spec out.
Jake Dern 00:10:10 Yeah, no, that makes total sense, and I do think, like, yeah, as you were mentioning, maybe it's kind of a different thing, you know, having a formal spec for what OTAP is, and then also getting it, you know, accepted as, like, an alternative protocol for OpenTelemetry. Like, we can probably tackle those separately, but definitely wanted to, to make sure it was at least written down, at some point. And then…
Kind of like a related thing to this,
But… and I'd been tracking this on another issue, about stabilizing the batch processor, but something that I'd like to start, at least thinking about doing is going, and adding some validations to OTAP arrow records.
And, kind of like, so…
today we have this, like, you know, I think it's… is it OTAP Arrow Records? I always get the name wrong, for the type, because it changed at some point, but it's OTAP Arrow Records, and then underneath that, there's, like, some trade, OTAP Batch Store, and we have, like, this function, you know, you can set, like, a payload, right? So you can give it,
You know, you give it the payload type, and then you can set it and say, like, this is the record for that… that payload type.
And so I was curious if there's, like, any thoughts about, you know, maybe adding
Or I guess, like, making this, like, construct kind of a centralized place via which we validate data that's coming in. So, like, for example, if you're going to set, like, some record
on one of these, you know, maybe we check, like, does it have the required fields? Are the fields of the right type? You know, that kind of thing. We can have APIs for, like, setting it unchecked if we, you know, do some, like, transformation, and we know that we did, like, the right thing, that kind of thing.
But it might be nice to say, like, hey, if I have one of these OTAP arrow records, like, I know some things about, like, what's inside, and, like, some minimum, you know, like, number of guarantees that we can then leverage, like, in the rest of the pipeline, so we don't have to kind of defensively code around, some cases, everywhere. I don't know if that makes sense.
Albert Lockett 00:12:05 Yeah, that… that definitely makes sense. I think it's, like, it's…
I think there's, like, two… two aspects of it. One of them is, like, definitely, like, having those validation checks when we set, like, record batches, and the other thing that would be really nice is if there was a way that,
We were able to return data to callers from that construct.
In a way that…
we didn't have to, like, just receive a record batch and then, like, make those implicit assumptions about, okay, well, here, like, I know what all the validation logic is, for example, and so I know that, like, I can always call, like.
column name type dot unwrap, right? Because you know there always should be a column name. Like, it'd be nice if we could expose an API off
OTAP, arrow records that made it so, like, we didn't…
Have to, you know, like.
rely on the validation, but also write code that, like, technically could panic if the validation failed, so… Anyway, that was, like, something I was gonna start trying to look at next week as well, is, like, like, if we can change the interface to make, like, hotel arrow records more…
like, easier to use for, component authors and things like that. So, anyway, just calling that out, because there's probably some… some overlap between that and the validation.
Jake Dern 00:13:36 Oh, yeah, 100%, that'd be great. So you're saying, like, okay, yeah, like, literally maybe having, like, a, like a wrapping-type…
Over the top of those for, like, each payload, and then you can access via some kind of, like, getter or something,
And then you, like, know for sure that it's… it's in there. Yeah, that's… that's really interesting.
Albert Lockett 00:13:55 Yeah, that's kind of, like, the direction I had with it, or that I was thinking about, without having thought about it too deeply at this point.
Jake Dern 00:14:04 Okay, yeah, no, that's cool. I definitely don't want to take any more time, like, in the meeting, but I will just, like, mention that I also… if there's going to be, like, more, like, types and capabilities here, another thing that I thought could be potentially cool is… so the first thing that I do
Or this was done before to, like, some degree, but just kind of scattered, like, in the batching as I go through all of the records, and I create, like, some kind of index, over the top of them.
It would be kind of cool if, like, well, maybe, like, the OTEP, you know, Arrow Records, like, just…
like, we kind of created that index, or at least part of it, like, on construction, and tracked it as there were modifications, and then, you know, certain operations, like, everywhere, you know, could leverage that index and not have to be, like, reconstructed, so…
Anyway, just a thought.
Albert Lockett 00:14:47 Zoom.
Laurent Querel 00:14:48 Thank you so much, Jake. I think it's, definitively,
It'd be important for us to have this,
Famil specification, and in addition to that.
The validation that could be done in the construction phase to To ensure invariant and properties.
We want to go next? Ideally, not too long.
Josh Buchan, are you already on your side, or not?
jmacdonald 00:15:22 Good question. I…
Don't see Goken. I… I would propose that we should take your topic. It's not… I don't think I'll do a really good job of this myself today, and…
Without Gokan, I don't feel comfortable… I mean, I just don't think we should go forward.
Laurent Querel 00:15:42 Okay.
jmacdonald 00:15:42 He said he'd be here.
Laurent Querel 00:15:44 Okay, maybe just before Tom or Drew, do you think that you can address your discussion in 5 minutes?
Bitch.
drewrelmas 00:15:54 Yes, mine.
Can do that.
Laurent Querel 00:15:57 Okay, so, go ahead.
drewrelmas 00:15:59 Okay, there's… this is just.
jmacdonald 00:16:03 Very quick thing about…
drewrelmas 00:16:06 We had a broken CI yesterday because PR added,
it split some of the Rust CI jobs from just happening on Ubuntu Latest to Ubuntu and Windows.
We actually do Rust CI jobs for a number of different OSes, but we, have only been really requiring the status checks on Ubuntu Latest.
So I just wanted to pose a question to the group, should we be requiring all the Rust CI jobs to pass on all platforms as a precondition for Merge?
Albert Lockett 00:16:51 I think…
like, my impression was theoretically yes, but I thought that, at a certain point, we had some tests that were failing on
Windows, and I think we just, like, went back and ignored those, and now the Windows is… is passing, so… Like, I… if I recall correctly, like, those failing tests were the reason that we decided to make it not required in the first place.
So I think that, like, to me, that sounds reasonable. I don't know if, like, but I don't want to speak, definitively. If folks have other thoughts, like, please share.
Laurent Querel 00:17:30 Makes sense for me.
drewrelmas 00:17:32 Okay, it's relative… it's very easy to do, and I also opened another issue. I think there is a way we can avoid,
the problems we had yesterday, I talked with Trask.
In a side chat, but it's not a high priority. For the moment, I can go require, at least the windows. I'm looking at CI… at Rust CI.
We also have…
Ubuntu 24.0 for ARM, and we also have Mac OS latest. Do we want those as well?
Albert Lockett 00:18:12 Yeah.
Laurent Querel 00:18:12 Why not? I mean, it's not… for macOS, I don't think it's a typical target for this kind of thing, but,
We, we can always, like mentioned, I advert, make them, not required.
jmacdonald 00:18:26 Yeah.
I've done some macOS work just because I'm, like, after hours trying to finish something, but it's not a big deal to me.
drewrelmas 00:18:39 Okay, so I… sorry, how should I interpret that? Just do Ubuntu and Windows?
jmacdonald 00:18:45 That's not… I would say so, sure. Having it, show so that people can see how they're breaking macOS is useful, I think… but let's not overdo it.
drewrelmas 00:18:56 Okay.
That concludes my topic.
Laurent Querel 00:19:00 Yeah, so I'm just adding, add some non-required targets, such as… Macos…
I don't know, you've mentioned a few other things.
So, developers that are using macOS, we'll see, but we don't put it as a mandatory target in terms of success, because that's not a deployment, a typical deployment target.
Okay, Tom?
tom 00:19:32 Yeah, sure. This issue, the issue of labels renaming also, I think, brought up by Joe on… a few weeks before, and currently we have,
I think 50 labels, and many labels, I think, overlap each other, the name. So, I proposed the renaming, and it is… the renaming is also based on the
There's a… there's a suggested triage process in OpenTelemetry. I put a link, I think, at the top there, but that one seems… the second one, that process seems, too general.
for open television, not, like, it focused too, has too much focus on the document, so I did some change based on that process, like.
So… but the structure is very close, like,
We put our top-level namespace, and then, for the remaining name, put, organize them in tree-level structure to show the… to show the hierarchical…
view or naming, so make it more easy for us to… to scan or decide which label to apply. And with the new structure, I think we can apply multiple labels to one issue, yeah, because they could be… belong, like, to multiple… on the multiple namespaces, right?
language ROS and, the area engine, both can apply to the same issue and, do not.
jmacdonald 00:21:08 cost any…
tom 00:21:09 Like, understanding issue, like that.
Laurent Querel 00:21:15 Okay, any, feedback from, on this group.
jmacdonald 00:21:22 I've looked at this, it looks good to me. I think if I had to pick, like, nits at it, I wonder why we use the word type. Like, type dependencies and type validation maybe left me feeling, like, a little confused. I'm not sure what type does for me, but other than that, it looks good to me. Thank you, Tom.
tom 00:21:41 Yeah, okay, I mean, you should have either feel free to propose that you want.
Laurent Querel 00:21:47 Yeah, in that case, validation was about,
testing? The process… the process of validation…
jmacdonald 00:21:57 So we have traffic, we already have continuous benchmarks to.
Laurent Querel 00:22:02 Detect performance progression.
Here, it's to validate the… that,
functionally, I mean, at the functional level.
Or at the semantic level,
Whatever pipeline you are testing, is doing exactly what you expect in terms of data processing.
So if you have a filter, the output is exactly what you expect in terms of filtering.
That's the type of,
The validation process that we started to put in place.
Which is not, finalized, we have various discussions, I don't necessarily want to enter into this detail today, but, so, yeah, type is,
Maybe test validation, or something like that.
tom 00:22:50 Okay, yeah.
Laurent Querel 00:22:54 Okay, yeah, for me it's fine also. I don't have any, particular, comment on that.
It's probably not the end of the story. We probably need to think about the…
How that will be, leveraged and used,
In order to simplify the overall process.
Right now it's more informative, but most likely there are some,
Some… some process to put in place to make things a little bit more smooth.
Okay, so, if… And.
tom 00:23:34 once more, I think, also one more, question based on this renaming. I think I also, at the bottom, I added some, like, traged labels, so that's about the traged process, currently we don't have. I mean, like, once we have these labels, like, can we…
Like, do the charge process, like, for new issues coming, we apply automatically, like, the label charge, deciding, and then…
Maybe I can help to add some label? But don't remove the tragedy siding. And then during the SIG meeting, we can charge all the new issues labeled, like tragedy siding.
Laurent Querel 00:24:15 Perfect, yeah. I think that's the type of,
Process that we can put in place based on those levels that entirely make sense,
I would say, focus on… Triage, oriented label.
Sorry.
And we can try to put that in place for the next, similar to you.
We start by reviewing the…
Like you said, you name it, triage deciding, and we can discuss very quickly,
tom 00:24:57 If it's something that is duplicated, that we don't want to fix or accept it, blah blah blah.
Okay, I'll follow up on the traged labels at the first, and then next meeting, maybe we can do trash and decide maybe other, other labels.
Laurent Querel 00:25:11 Yeah, makes sense.
tom 00:25:13 Perfect.
Laurent Querel 00:25:14 Okay, so, Josh, so no, you, you confirm that right now GoCan is not there.
I think, so let's, I can share my screen on…
jmacdonald 00:25:26 I'm really interested in your topic, so I don't think it's more important to talk about extension interfaces, especially without Gokan here. I could, if you wanted me to, but I won't.
Laurent Querel 00:25:35 No, no, no, no, no, no, no, no, no.
jmacdonald 00:25:38 So let's see, need to share a different screen.
Laurent Querel 00:25:44 I think that's this one.
Yes.
So let's do some… Clean up, and then I will…
I'll make that a little bit… is it big enough, or do I need to, increase the size.
The, the police, the fault.
Okay, take that as, it's okay.
Okay, so,
the context. We, we, I opened a series of, proposals already with the goal of improving
to stabilize, basically, the configuration model that we use for the OTAP DFNG.
And it's covering many aspects. There is already a PR, I don't remember if it's already merged, but there is a PR to normalize the URL.
And we have two,
poor representation, a shortened version, and, a fully qualified URL.
I think we already agree on the…
yeah, the goal and the approach. So now I'm moving to…
some thought regarding the… the structure, the overall structure of the configuration model. So, before to… to explain the…
the current situation.
the proposal target. I like to go back to what we have, and what are the limits, and also the benefits of the current GoCollector configuration model.
So here we, we have,
Sorry, not this one, this one.
So this is an example of, a typical… I don't know if it's a typical, but, let's say, a structure representing, the GoCollector configuration.
So we have three sections. I didn't mention connectors there, just for simplification, but we could talk about that. So we have receivers, processors, exporters.
I just reused our own existing receiver, processor, exporter. Obviously, this one, for example, does not exist into the GoCollector ecosystem, but
The structure is the same.
So we… the way that it's working, just as a reminder, we have here the…
let's say the type of the receiver, and we have some kind of additional ID.
this entire thing represents, is the ID of this specific receiver.
If you just specify a filter, it's the type, but also the ID. So that's the type of,
rules followed by the GoCollector to, to simplify, to get, to get basically, a relatively, easy-to-read, YAML configuration file.
And then you have this section, service pipelines, where you express
pipelines. Note that both pipelines are per signal type.
Metrics, logs, traces.
If you want to mix them, you have to use the connector concept. And then, there are some implicit rules, like, fan in and fan out.
So, receivers, this collection of receivers.
Pan in, this chain of processor.
And, the last processor rendition
pan out into these two exporters, and that's the same mechanism every, every time. So if we want to represent something like… so this, this configuration file
Represent something like that.
So we have two traffic generators.
a chain filter batch, and, final OTLP console.
And, and we have an additional,
an additional OTLP receiver connected to batch.
the translation of this, DAG
into the legacy, the GoCollector configuration is slightly more complicated, because
we can't really represent a DAG. We have to…
Do some, so first we have to do that for each,
Signal type, and then we, for this specific case where we have
this type of connection. We have basically to replicate
OTLP batch, OTLP console as a separate, set of, Pipeline.
Nothing to… no comment on that?
drewrelmas 00:31:00 Yeah, I wanted to say one thing, and it might be what Josh is getting to.
Which is, Josh, you and I have talked about this, doesn't the Go collector end up, creating separate instances of processors under the hood when they're, mentioned in multiple places?
jmacdonald 00:31:22 Yes, it does create separate instances per pipeline that refers to it. That is only for processors, and that's my understanding.
And I… and I know that you and I, Drew, have discussed how, you know, if we are trying to replicate a Go configure… a Go Collector configuration, we might end up
You know, compiling it into multiple instances of the same
Node to do the same thing.
Laurent Querel 00:31:51 Yeah.
So, there are… so my, my,
Let's say, set of observations or conclusions based on this, existing
Go collector configuration. There are many implicit things, like the fan in, fan out, the duplication of processors.
So that's one aspect, and there are also limitations.
It's sometimes very complicated just to
to create, to represent something that is a relatively complicated, pipeline that you want to implement. You have to think about it, and it's not necessarily super easy. Sometimes you have to go… if you want, for example, to combine multiple types of signal.
you have to use connectors, and some of them exist. For example, something translating OTLP logs to metrics.
But all the combination does not necessarily exist, or you have to implement a new type of connector yourself.
So the… that's an additional set of, I think, limits, in my opinion, is the fact that if you want… if we… if we wanted to add some,
generic, behavioral Per receiver, per processor, per exporter.
The fact that we directly have the custom configuration
At the top level of the component definition.
is, is problematic, in my opinion, because then it's very hard. If I want, for example, to add something like a lifecycle.
Something describing how to
To describe the behavior of, like, let's say, a reliable configuration, but in a generic way.
for any component into this, pipeline.
Nothing guaranteed that this lifecycle will not be in collision with some configuration of some component into the ecosystem.
So there are multiple things like that. So now,
What we, currently have in terms of configuration.
It's not necessarily super sexy, but at least it's fixing some issues.
So we… but we have a lot of redundancy, it's definitively perfectable, and that's why I'm talking about that, because I think we can do a much better
Work, and still keep the nice property of the existing system.
So first, fundamentally, we are not describing, like,
flat pipelines where you have, a lot of implicit things, fan-in, fan out, and just a linear pipeline where you combine multiple processors. We can just probably, a DAG with this system.
Second, we, we have this, level, systematic level config, which makes, possible to add additional, engine-level, field.
that could be attached to any node. So I will provide some examples in the final version to show you what that represents.
Then we also have the support with those outputs, so we can name outputs. By default, there is one output, but we could have multiple.
And it's very useful for some category of processors, or in fact, for any kind of receiver and processor, we could imagine that.
But there are a lot of redundancies. We have kind, and then we have the plugin year-end, but we also have the same information, basically, here.
the output is also, a little bit verbose. There is this, round robin, stuff, dispatch strategy, in the mix.
We discussed, I think, with Andres, the fact that, yes, by default, we should have a fan out. Right now, it's not implemented. We have some solution now, but,
When initially we implemented that, that was not present.
So that's the current situation, and to implement the Fanahoot, we introduced this Fanahoot processor.
As a way for us to support a lot of,
various scenarios regarding fan out. We can fan out sequentially, like the GoCollector is doing, we can fan out with a parallel strategy, and we can specify various configuration regarding timeout, fallback, and so on.
So it's much more rich.
But it's for… for me, it's an exploration, so we have a very,
let's say, complex, complex, not complex, it's a, it's a very,
capable, finite processor.
At some point, we will implement,
Edges where we could describe, either its,
a broadcast, or it's a fan-out, or it's, A load balance strategy.
And then I will explain how that will be done, but right now, that's what we have.
So… Based on the, on this,
current representation, I thought about simplification, but keeping the same kind of properties.
So you will see that it's a mix between the initial GoCollector approach and, also I'm using some feedback from Andres, that was put in some of those proposals.
And try to end up to something that is, easier to read, easier to interpret.
So I'm reusing the concept of splitting the description of the various nodes, receivers, processors, and, exporters.
I'm reusing also the mechanism used to express both the type of the node and a specific additional alias or ID when it's required.
same approach that we have into the GoCollector configuration file.
But I'm keeping this intermediary level config for the reason I mentioned before.
So an example of that, I think, is there. Let's see, the first, the receiver.
So imagine that you have a receiver, and we have, let's say, for every receiver, a mechanism to express
where the tenant ID information is defined, in order to tag into the OTAB batch a tenant ID, which could be a first,
citizen field into the system. So, it's something that will be defined at the engine level.
That, any, receiver could use. So that's…
An example of how to leverage this additional level that we have into the configuration.
For, the processor, I'm going even further, so the…
Here, we have lifecycle and telemetry at the same level and config. So let's say telemetry, you want to… for this specific component, you want to specify that, oh, let's say debug, and I want to debug specifically this node and not the other ones. So,
That could be an example of, regular configuration available for any nodes into the system.
lifecycle, once we support targeted library configuration, we could imagine also that for some component, we support or we don't support some type of library configuration. So that's an example of, configuration that we can imagine.
Okay, so now, once we have this,
Definition of, nodes categorized by the three-category receiver, processor, and, exporters.
Then we… we can define, the… the wiring or the connectivity between the… Between those nodes.
And,
And then, so that… so we have a form too, and… and we have this syntax. So, for example, in that case, I'm just trying to represent exactly this, this thing.
So we have two, from… so it's a fan-in example.
Going to a filter processor.
And then we have this OTLP receiver.
That is going to, I should say, something like that.
going to the batch processor. So we don't have to replicate multiple pipelines, because we super natively DAGs, and we don't necessarily have to duplicate processors also, because they are, reusable in different places into the DAG.
And then when we have port, I use this syntax, so the fan-out processor primary export port will go to this one, and so on.
We could, extend this mechanism this way if we want to, oh, sweet.
Once again, need to fix that.
What's it, Ben?
Okay, because it's… okay, I see.
So the… in that case, we have, an example of, fan-out, expressed directly with this, hyperage, with a policy-type broadcast here, and, when we have multiple, destinations. And here we have,
Again, a fan-out representation, but with a good balance, and a strategic, of-type would rather be.
I see that Andres has some, comment or question.
Andres Borja 00:43:13 Yeah
First, thanks for taking this. I think it's… it's great. We are… we are going in a great way.
I'm curious… So far, we haven't separated, like.
Explicitly the concepts of receivers, processors, and exporters.
Beyond just the label, that is…
I mean, they are just notes, at least… as of now, you know? So… I'm curious about…
This strategy is, is, is…
Laurent Querel 00:43:46 why it's there? Yeah, I can explain. I mean, it's definitively,
a preference, but not necessarily a strong preference. The alternative will be… so we, right now, we have that.
And, if I'm just taking, let's say, a few of those examples.
Just to… to express the…
Let's imagine that we have that.
We… in order to do that, we'll have to systematically
this kind of thing, but we can't because, process, or, it's not valid, so we have to put the… the cut
And then, yeah. So we, we, we… if we want to reuse the… so it's either that.
Or, it's, let's say, a receiver one, and… type… Traffic, gen… Emilator, receiver.
That could be also another, option.
So I was thinking, if we want to remove, duplication.
This, this approach is… is nice because you… you basically don't have the issue that we have here.
Or you don't have to repeat yourself many times when you have multiple receiver processes, and so on.
slight advantage, but, I mean, I'm open also to the previous model if,
If there is a strong preference.
Andres Borja 00:45:42 On that a preference or not, I'm just seeing that it's a slightly…
I mean, different in terms of the model, so…
Laurent Querel 00:45:52 Yeah, I'm aware… I mean, I'm using this,
The fact that we want to stabilize the configuration model, with the…
The values criteria that we express into the,
the GitHub issue, improving the user experience was one of the top, priorities.
So that's why I, I…
I try to take that into consideration.
reusing the… what I think is…
is good into the Go configuration collector.
the Google Connector configuration.
But still having the additional capabilities that we already support.
So that's why the… I moved to this, in this direction.
Andres Borja 00:46:44 the… The, the, the other… comment or question is,
in… in… in the Go Collector.
I feel like we are confusing a little bit the terms or the usage of them, right? You describe the objects, you describe your receivers at the top. It doesn't mean that it's a single instance or multiple instances.
Laurent Querel 00:47:11 Yes.
Andres Borja 00:47:11 By the time you put them in a pipeline, it's a new instance in memory, you know?
Laurent Querel 00:47:16 Same CEO, yeah.
Andres Borja 00:47:19 The case of the receivers is another instance. Just because they share the same port, that's another story, right? You can share the same port, but two instances.
I think that is particularly, I mean, important to…
To align is because the processors, they cannot share the same instance, just because if you are using them in different pipelines.
Think on an aggregation processor, you know? It's… it's gonna be auth to process.
Laurent Querel 00:47:49 Yeah, yeah.
Andres Borja 00:47:50 That are aggregating things from different pipelines, right?
So… Yes.
So, I would not… I would separate those concepts, right? One thing is the definition that you can do. It's more like…
The definition, yeah, the declaration of what is the object is gonna look like, but by the time you put it as part of one pipeline, whatever it means.
It's a new instance, right?
It's like the definition of the class versus the object.
Laurent Querel 00:48:21 Yes, so that, so I, I understand. In my mind, the… so let's remove that. In my mind,
the small difference that we have here is… let's take the processor, because that's, I think, your point.
If we have batch… And that shoes…
So, in my mind, batch is… once we see it, it is instantiated, and then we have the wiring process here.
So if we have a multiple time batch, that's the same, in fact, into the DAG in this model.
It's not like, if you want to create two batch instances, you have to create, let's say, batch, batch one.
And, and, and batch 2.
That's, I guess, editions.
Andres Borja 00:49:18 Because they're part of the same graph.
Laurent Querel 00:49:20 Yes. Could be analogous to the same… part of the same pipeline.
Yeah.
Andres Borja 00:49:25 But if you have multiple grabs, right?
Which I would expect that to be mapped more to a pipeline. I would expect, if you want to.
Laurent Querel 00:49:34 Yes, and we have this pipeline group pipeline mechanism that I didn't represent there, but that's exactly that, yes.
Andres Borja 00:49:39 So, if you reference… so, I totally agree. For me, this is…
A single graph, so it's analogous to a single pipeline, so yes, it's the same instance, right?
But, but if you want to use it, I mean…
I'm having a hard time to think on where… how… why would you want to reuse the same batch or the same processor in different…
Places of the same pipeline, but…
Laurent Querel 00:50:08 Yeah, yeah, we have that here.
Andres Borja 00:50:13 In the Go Collector, you had to basically artificially.
Laurent Querel 00:50:19 Duplicate the batch.
But fundamentally, in our system, we could reuse the same.
So there is, filter and OTLP that point to the same batch.
a PIN that we could end up to aggregate, to batch.
smaller batteries from… coming from traffic gen and coming from a TLP, which is… .
Andres Borja 00:50:46 Yes.
Laurent Querel 00:50:47 something that you can't do with the GoCollector.
Andres Borja 00:50:50 Yeah, that makes sense.
So, anyway, independent on that, right, if it is part of a…
Of the same pipeline, yes, definitely it should be the same instance, right?
Laurent Querel 00:51:09 So do you see, do you see, and then after that, I will,
I think Joshua was, asking,
was ready to comment or ask a question. So, just to, finalize this discussion with you, Andres, do you see any important modification, in this, approach?
Or do you, overall agree with the… with the direction?
Andres Borja 00:51:41 I like it, I like it in general. I mean, I'm still trying to process the…
The change on the model of having receivers, producers, and exporters, and…
Laurent Querel 00:51:52 Yeah, versus nuds. I think this one is, could be, yeah, still,
Andres Borja 00:51:57 So, or alignings with the graph, because when you talk about process of receiving exporters.
you think sequentially, a graph is more like a graph, right? So…
But, but, but yeah, I, I think, I like it, right? So,
I was also trying to justify those things, like the receivers, processors, and exporters. I think the way you described them is that
more like a class, again, that they can have their own properties, right? So I think we can have some properties that belong to any component.
But some properties that belong to processors, some properties that belong to receivers, and then some other properties that belong to the particular
Watch.
Laurent Querel 00:52:41 Yes, indeed, this, config versus those things that are top-level
Engine-level configuration versus the… the pure, specific node configuration.
Andres Borja 00:53:03 The other thing that somehow… I mean, it's also…
Popping out of my head is this.
process, or… capable of doing fan-out, right? So…
somehow conflicting with… because we are doing that in the node, right? We have multiple destinations, and then we can configure them
this is like when you design a graph, right, and then one particular type of node is the one that splits the data, or is part of the node itself, right? Is it somehow…
Laurent Querel 00:53:42 So, yeah.
Andres Borja 00:53:44 Well, I'm gonna hold them?
Laurent Querel 00:53:46 Yeah, Andres, I think the… I, I agree. So the… the… that's the, for me, the… the, the…
when you have something simple, a simple fanart or a simple fanine, I like to be able to express it with just the hyper edges.
Ideally.
For me, the fan-out is something where you have more complicated situations.
And right now, we are exploring the finite route processor as a way to
first, support, scenario that we currently don't support into the processor, so it's like an exploration for me.
And ultimately, it will be a fan-out processor to support the most simplistic things that will be, relatively, hard to express with this concept of hyperage.
For example, the fallback mechanism that we mentioned here is an example of a such,
complicated, thing. That is a reality, in common scenarios, but,
So, for me, most of the situation will be expressed this way, ultimately.
But for the very complicated ones, we can rely on this final processor.
Joshua, you want to say something, I think?
jmacdonald 00:55:14 I… I don't think so. My head's kind of… I'm kind of… I'm not feeling great. This is… I'm glad you all are… this is great.
Andres Borja 00:55:21 I feel like Drew mentioned something in the chat that, you know, like, I would, I would say, I would expect, or, or, you know.
how I would see it is one or another, right? But not both. I would expect, if we define, like, a specialized component for doing that.
routing, or… Find out, or…
you know, I'm not sure how to call it, but,
like, edge splitting or something like that, right? If you have specialized components for that.
that we can grow and make it more complex in time.
Yes, good, but let's… don't put them in the notes then. If I am a, I don't know, an OTLP receiver, all I need to know is that I need to review this and send it to someone else, you know, not… not having all this complexity of, oh, it's multiple receivers, and then…
And then…
I don't know what's the strategy, and so on, oh, just the next node. If the next node is a processor that is capable of doing distribution of those messages in a complex way, sure, so be it, but… but I don't want to have that responsibility in my nose, you know?
Laurent Querel 00:56:33 Yeah, I'm not sure to entirely capture the… .
Andres Borja 00:56:40 The decision of the next North.
Laurent Querel 00:56:42 Yeah.
Andres Borja 00:56:43 The way you are describing it here as an external process, or is a component that is…
smart enough to do that logic and complex, you know, to have
all the different possibilities of different broadcasting mode.
Laurent Querel 00:56:57 So, okay, so the conclusion is, you agree with this approach, I think that's, and it's more or less what you suggested, I think, in one of your comments.
Andres Borja 00:57:07 Yeah, yeah, but let's move them out from the component itself. Let's move that out from the…
Laurent Querel 00:57:14 And I agree with that, and I think that's, makes the overall experience better, and it's still keeping the same kind of,
Extension or extensibility into the system.
Okay, so I think we are in phase. Is there any other feedback from anyone else?
jmacdonald 00:57:36 So, can I see if I can summarize what I've been listening to now on this very topic here? What I'm… and Drew's comments on the side, it sounds like we've all kind of circled around this now. There's… there's simple nodes, and simple nodes just sends to one destination, and that's the collector's model as well. And then there are
we're going to say complex nodes that most people are not going to implement, like the fan-out processor, maybe more, but, like, it's the one that we have today. And whereas the Go Collector kind of hides that complexity from you by inserting these special nodes, we're just going to have these special nodes, and we're going to work on them. And later on, when we have this working really well, we can syntactically do tricks like the Go Collector does to hide that creation of a complex node.
for FanOut, is that right?
Laurent Querel 00:58:22 Yes, the… yeah, I think that summarized well this part that I put into comments, because…
It's definitively something that we could support. Yeah, I agree.
Andres Borja 00:58:33 It could be even a different type, you know? It's so disruptive in my head that I cannot match it with a processor, right? It has its own…
use case, right? So, it's not really processing, it's clout thing, you know?
So maybe even the language and the properties on it might be different. It's not a processor, but maybe it's a router.
jmacdonald 00:58:55 You know, that actually brings up some of the hidden complexity in the Go Collector, is that a routing component is really hard to write in that model, and you have to be a connector, and the connectors have special privileges to look at their routes, basically. So I would say we're actually finding the same types of complexity and patterns as the Go Collector here.
Andres Borja 00:59:14 Or is a connector, yeah?
jmacdonald 00:59:16 A connect… the GoCollect connector has the ability to be a routing processor, but normal processors don't have any routing. As a normal processor, you can't choose your exporters, but a connector can.
Andres Borja 00:59:28 Yeah, maybe it's a connector, yeah.
jmacdonald 00:59:30 Yeah. It's like a connector in this, in this model.
Laurent Querel 00:59:34 Yeah, but I don't think we need to add an additional type. I mean, for processors, maybe,
A term that is a little bit, over… over,
I mean, not perfectly aligned with the meaning there, but…
For me, the processor nodes in our system are…
something that could achieve, not only data processing, but also routing. I mean, it's a… it's a very flexible component.
Andres Borja 01:00:04 Once we have multiple grabs, is it gonna be… Allowed to send?
Data to another graph.
Laurent Querel 01:00:12 Yes, we introduced that into the… one of the proposals with the topic mechanism.
jmacdonald 01:00:19 Wouldn't that make them one graph again? I mean, like… That's… maybe that's semantics.
I.
Laurent Querel 01:00:27 Okay.
jmacdonald 01:00:28 this was productive.
Andres Borja 01:00:30 That is closer to the behavior of the connector, that's what I'm asking, you know?
Laurent Querel 01:00:37 Yeah, it is, but will that be really different? I mean, in terms of implementation, that doesn't change anything.
Andres Borja 01:00:45 That's exactly the same thing for us.
Laurent Querel 01:00:47 So why… why are introducing the… this…
Renaming for something that already exists and already do the same thing, in fact.
Andres Borja 01:00:55 Whoa…
Laurent Querel 01:00:55 Or…
Andres Borja 01:00:56 because the use case is fundamentally different, right? Think on the properties that you were assigned to that. They are not the same properties that you assign in another processor, but… but it's very specific. The use case of routing is very different from the use case of batching data, you know?
The outputs are different, outputs are different.
Laurent Querel 01:01:19 What you are suggesting is adding, A first-class citizen… A connector, a connector? I don't like it, personally, but, router, if you prefer, but…
jmacdonald 01:01:29 terminology… this is just terminology, I think. We're lumping everything that kind of has an input and an output and calling it processor, and we're saying maybe we should have two terms, but I don't think this… I don't think this is a big deal, other than the naming right here.
It would be okay with me if we talked about simple processors and complex processors, and one of them is able to route, and one of them just… you never think about it, because you're just a simple processor.
Laurent Querel 01:01:57 That's the protocol, unfortunately, yeah, yeah.
jmacdonald 01:02:00 people…
Laurent Querel 01:02:00 Let's mature that, and, so I will put that into a GitHub issue, attached to this, set of proposal. I like, if you have any feedback or,
please, comment the corresponding GitHub issue. I lacked in one week max to be in a position where we can start to
plan the transformation of the existing configuration to this new version, or some variation of it, in order to stabilize definitively the configuration model in the coming, in the coming weeks.
jmacdonald 01:02:45 Thank you. I agree this is a pretty urgent matter. If we're going to change the config, we should do it quickly.
Laurent Querel 01:02:50 Yep. Thank you.
jmacdonald 01:02:52 Thanks, thank you all. I'm sorry that much… I couldn't talk, and my head hurts. Bye. Have a… see you next week.
Andres Borja 01:02:58 survive.
Laurent Querel 01:02:58 Thanks, bud.
