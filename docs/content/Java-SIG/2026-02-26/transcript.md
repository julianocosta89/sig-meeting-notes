SIG: Java SIG
Date: 2026-02-26
Duration: 54 minutes
Zoom Recording URL: https://zoom.us/rec/share/2xLlGPRC-iZcYiJ6o5OrhJx0cg6LCViFptZqSVbsC6pGJLXxDGVviiySi4pI2wqk.HlpjbqDjfAxFhQrA
============================================================

## Zoom Recording Transcript

**Gregor Zeitlinger** 03:45 Hello.
**Trask Stalnaker** 03:48 Hey, thoughts.
Alright, let's jump into, our… Only topic so far.
**Jack Shirazi** 04:25 This is, this is Sylvain, my colleague.
And he's changing the instrumentation for a servlet.
And normally there's no feedback when you've got a draft PR, so he was just asking if we would look over the approach that he's taking. So it's intercepting on a get input stream, it's intercepting the read.
Of the request body, and, putting that into an attribute.
Up to a certain size.
And all of this would be opt-in, and… Limited.
So, I think it's less the code and the approach that he wants us to look at.
So if you flip back to the conversation.
Yeah, this is… so he's got a couple of config options. One is to turn on the feature. The next is a size of how much text would be put into the attribute.
And then what it's doing is when you do… when the app does a get input stream, it's copying that in memory.
Up to that size, and and it's only limited to the request body.
Yeah, so he uses that HTTP request body at text for storage. It's not yet a sem called…
**Trask Stalnaker** 05:50 What do you… what do you mean, limit… what does it mean, limited to request body?
**Jack Shirazi** 05:56 He means that that's the only thing in the input stream that we read, just the request body, which, yeah, that's a good question, I'm not sure if there's anything else it reads. Okay.
I'll use the provided char set or UTF-8 if nothing's there.
It's only servlet 5.
And the tests and implement… implementation just limited to Tomcat and Jetty-specific versions. The last thing he's saying there is that he's not doing GetReader only Get input stream, which… Yeah, it's questionable, but… This is a very specific opt-in feature for… We had a lot of customers on our old agent who wanted this. So it's… it's pretty much a… Just duplicating what they've asked for, rather than trying to make it extensive.
**Trask Stalnaker** 06:59 So, question about this, because I think there was some discussion… where did we discuss this?
**Lauri** 07:11 I'm just curious, you mentioned that a lot of your customers asked for it in your old agent.
Did you ever implement it for the old agent?
**Jack Shirazi** 07:21 Yeah, yeah, it's there in the old agent.
**Trask Stalnaker** 07:31 There was a discussion about this somewhere, and I can't find it, where… that Sylvain had… mentioned… this… I thought he was talking about, and maybe I'm getting this mixed up, but I thought he was talking about capturing it as bytes.
And… 64 bytes…
**Jack Shirazi** 07:56 Yeah, I mean, that's the… the best approach is to assume base64 and keep it like that, because it could be binary.
But… I forget what he's, Yeah, there is… there is a… Like, trying to decode it if it's text.
The thing is that most times, when this is required, or asked for, it's text, and they know exactly what they're asking for, and they know what they want to intercept, so it's… I think he's, he's… Like, in our old one, we didn't do the Base64 encoding, we just did a… A decode into text.
But you're right, I remember also that discussion, and I don't remember…
**Trask Stalnaker** 08:46 Where, and where it went.
Okay.
**Jack Berg** 08:52 Now that we have… In order to have stable, complex attributes, we should be able to capture just, like, a byte array directly instead of base64 encoding bytes. But, another thing that I was.
**Trask Stalnaker** 09:03 That was exactly what I… I commented on this, that… I made that comment somewhere, but I… like, disappeared.
The whole conversation.
**Jack Berg** 09:12 I also like that, you know, this thought about, like, hey, text is the most important thing, because, like, if you're just sending a byte array to a backend without any additional metadata to tell you, like.
context about that byte array, like, what the encoding is, what type of thing you're capturing with that. That's really hard to do something with usefully. So, like, I don't know, maybe an initial approach might be to capture the request as text if it's UTF-8 encoded, something like that?
**Jack Shirazi** 09:48 Or if the child state is provided.
**Jack Berg** 09:53 Yeah.
**Jack Shirazi** 09:56 Yeah, I mean, that's… that's… I think that's what he's saying there in the approach, is that… that those are the conditions under which it would be… it would be captured. Otherwise.
it would either be ignored, or Base64 encoded.
And I think… Ignoring it is probably the better option.
**Jack Berg** 10:19 Until people demand otherwise.
But…
**Trask Stalnaker** 10:24 Yeah, so I thought that he had left it off, this was 2 days ago, a comment, that I think a Base64 encoded is probably the simplest, most straightforward.
But yeah, I agree that… If we can do… if we can… and we can capture it, We can make it an any now.
So that we can capture the same… like, it could be text or a byte array.
So if we can…
**Jack Shirazi** 10:59 If we do not.
**Trask Stalnaker** 11:00 So the encoding, the car set, we can capture it as text.
In that same field.
Or we can capture it as bytes in that same field. We don't have to… before, we had to pick, like, one data type only.
**Jack Shirazi** 11:17 Okay, so, I mean, it sounds like there's no objections to the overall approach that he's taking.
Just… some tweaking…
**Trask Stalnaker** 11:30 Yeah, I think it's, I think it's a good time to open a SEMCOM PR.
To… You know, to get broader… Try to get some broader input.
Even though, you know, it won't be stable, and we'll pick, you know, we'll move forward with the prototype.
One other… question I had was, if there's any overlap here with the, We'd added a feature to inject JavaScript snippet. Oh, that was the response. Okay, yes, so no overlap.
**Jack Shirazi** 12:17 It would be good to…
**Trask Stalnaker** 12:21 Explain not supporting this is the idea that this often Uses this under the covers, and so you typically get it supported.
**Jack Shirazi** 12:36 Yeah, I think there is that, and there's also where it doesn't use that, it's often binary, or… What?
very odd Unicode.
**Trask Stalnaker** 12:51 But I would think that this would be better. Like, I would have thought this would have been the one that we would support, because it's more likely text.
**Jack Shirazi** 13:05 Yeah, I think whenever it's texted, it's always… Copy… it always uses the input stream underneath it.
because this is HTTP, it's not, you know, there isn't… It's always going to use the input stream in those cases.
I think it almost always does anyway, but… There are situ… I think… JSON encoding doesn't?
I… I can't remember exactly. I will ask him to clarify why.
**Trask Stalnaker** 13:35 Cool.
Yeah, and tests.
Right, like, it's… that's probably the most important… Piece of it is good comprehensive tests, across… Ideally, not just limited.
to Tomcat10, Unless we're gonna only turn the feature on for Tomcat 10.
**Jack Shirazi** 14:07 Done.
**Trask Stalnaker** 14:09 support the feature in Tomcat 10.
Hopefully, we could write the test just in, you know, once, basically, in the base class here.
And… if he sends it to CI, we'll find out which ones… which servers it fails on, and that… that could help us find edge cases.
**Jack Shirazi** 14:36 I think…
**Jason Plumb** 14:40 Jack Shirazi, I'm curious if in your existing implementation, if you ever encountered a case where Users, customers expected to have the entire request body in the telemetry, but it wasn't there because the servlet didn't read the entire request body.
**Jack Shirazi** 14:57 Pardon me.
Yeah, it's entirely dependent on the application reading it, so… Yeah, yeah.
**Jason Plumb** 15:02 But do you know if that was ever… did you ever see that being a problem?
**Jack Shirazi** 15:06 No, that probably wouldn't have reached us. That would have just been… that would have been an enhancement request, and I don't remember that being…
**Jason Plumb** 15:14 Okay.
**Jack Shirazi** 15:15 Like, we… I remember, and I had requests for the response, as well as the request, and the response… we always said no to the response… yeah, we always just said no to the response, because it's just… that's just a rabbit hole, but, the request…
**Trask Stalnaker** 15:33 Oh, okay.
Okay.
**Jason Plumb** 15:40 That's cool. I'm… yeah, I mean, I'm trying to think of the cases, like.
I'm trying to… I don't have my head around people… we get the same request all the time, and… I mean, for responses as well, and I'm… I just don't know how people want to use this data, other than just, like, engineers looking at it when something goes wrong.
**Jack Shirazi** 15:58 Yeah, for the most part, it is exactly… they're using observability also for debugging. Right. But debugging in production, and they want to be able to turn that on and see it both ways. Okay.
**Jason Plumb** 16:13 And in terms of responses, we analyze that, and the overheads are just ridiculous, so we always just turn that down.
**Jack Shirazi** 16:20 And what we always used to do is recommend that they use one of those replay tools, which does that, records both sides.
I think at one point, we even tried to… tried to link up to a specific replay tool, but that never went anywhere.
**Jason Plumb** 16:41 Makes sense, thanks.
**Trask Stalnaker** 16:46 To answer these questions, I… I don't have a… I don't personally have a preference, like, I think it's fine if we want to… limit the feature to certain things, like Java Agent Servlet 5X… I… I'm more interested in if we… support… if we say we support Servlet 5X and Java Agent, That we… Run that the tests cover all of the… All of those use cases.
Jetty… Tomcat, what else do we eat?
Test… Lori, outside… I know in the smoke tests, we test a lot of them, but in… integration tests, I forget.
**Lauri** 17:44 I think the… We usually have Tonkat and Cheti.
**Trask Stalnaker** 17:53 So, maybe that's a good… maybe that's good.
**Jack Shirazi** 17:58 And there was one more question down there, which is about whether it needs to be in the library at all.
Which, I don't think it does, personally, but…
**Trask Stalnaker** 18:11 Yeah, I think it's fine not to be. We barely added servlet library instrumentation a few months ago.
I think it's fine for it to be lagging in features and… Futures can be added later.
On demand.
**Jack Shirazi** 18:33 Fabulous, thank you.
**Trask Stalnaker** 18:45 Anything else?
Remote.
**Jack Shirazi** 18:50 everyone's getting the AIs to answer their questions.
**Jack Berg** 18:58 Yeah, I was going through the, the Java repo and trying to see if, if anything was worth discussing here.
I don't know.
**Jason Plumb** 19:09 And I'll add one.
**Jack Berg** 19:11 Yeah, go for it, Jason.
**Jason Plumb** 19:12 Yeah, sorry. I'm curious if, Why is this font… oh, it's doing the thing again.
**Jack Berg** 19:30 That's awesome that it affects Jason more than anybody else.
**Trask Stalnaker** 19:35 mentally.
**Jason Plumb** 19:36 Yeah, I mean, definitely mentally. So I raised an issue, in the op-amp configuration, or in the configuration repo about OpAmp, and I'm just wondering if we've thought or put any consideration into shipping the op-amp client in the instrumentation agent.
If we see that maybe happening one day.
**Jack Berg** 20:01 Let me share some context. Here's the link to the issue that Jason opened. I thought it was a good discussion.
**Jason Plumb** 20:08 Yeah, thanks.
**Jack Berg** 20:08 something that's… you know, that has been missing for a while. So the missing piece of op-amp is, like, it's this generic client-server protocol that is sort of unopinionated about which things it's configuring based on communication with this remote server. And, you know, everyone knows that there's tooling to configure the collector with it, and everyone kind of assumes that there should be, tooling to configure SDKs with it.
But, you know, that… it's like there's a missing abstraction, and we've talked about that at the SIG in the past. Like, what are the actual commands that a server would send down to an SDK to configure it, to update its configuration, and, like, what does that protocol look like?
And what are the behavioral expectations? And so… Yeah, that's, that's a little bit of context, so I… Jason, do you know of, just to put you on the spot, do you know of any, like, work that's been happening to kind of define that additional abstraction, the additional, commands? I'm familiar with this telemetry policy, OTEP, that might be worth discussing.
**Trask Stalnaker** 21:14 I thought that's what this was. That's how I was viewing this.
And it's kind of tied very much into the work Jack Shirazi's been doing on dynamic configuration.
**Jason Plumb** 21:26 Right, yeah, that's also the work that I would be citing.
Yeah, I think, you know, like, telling the agent to do stuff can happen… In a couple of different ways. Like, there's certainly the op-amp commands, which you kind of made reference to, Jack, but there's also just the, like, the sending of configuration as a natural… part of the op-amp protocol.
**Jack Berg** 21:52 You mean, like, initial state configuration? Like, initial sort of, like, static configuration on… on start?
**Jason Plumb** 21:58 I don't think op-amp makes that distinction. I don't think it gets… I mean, so, yes, there's still a gap there.
**Jack Shirazi** 22:06 Jesus.
**Jason Plumb** 22:06 configuration. It's not initial configuration.
**Jack Shirazi** 22:09 Yeah, I mean, I've looked at this fairly extensively, so there's… you have to separate out runtime changes with static initialization changes. The initialization changes That requires, basically, the SDK to start, and then wait until it gets the declarative config from somewhere, wherever that's going to be.
And for that to happen, it would need to have probably an op-amp agent or something or other that's going to read it from somewhere. OpAMP would be the ideal situation for that. I… I suspect that is something that some people want, but I don't think it's very extensive.
To have the agent fully configured from a remote declarative config. But yeah, some people definitely want that, and I think that's a… that's a… a feasible approach to just have the SDK sit there and wait until it gets it, and then fully configure. For the runtime changes, that's… We're all heading towards that telemetry policy, which is basically the simplest example is just, like, a little… I've even implemented it as a key-value pair, so the key being… let's take the example of sampling rate. Key is sampling rate value is 0.5, or whatever value you want, and that's sent And that can be sent through any mechanism. The telemetry policy says op-amp, HTTP, and file are the three standard mechanisms, and it also says you can have custom mechanisms. So… Yeah, it could be OPAM, it could actually just be an HTTP server somewhere that you read and get the changes, and that would be… You take that key-value pair, you convert it into a policy, and then you apply that policy to In this case, the sampler.
So that's… that's the intention of how it… how the telemetry policy is… is… is gonna work.
Or is… currently, anyway.
**Jack Berg** 24:12 And Jack, if, I think a couple of weeks ago, we were talking about something similar, or in a… yeah, in a PR, we were, like, kind of sketching out how some approaches for this might look. And I think, if my memory serves, we landed on something at least amongst, like, Trask, yourself, and I, because we were talking about this, where, you know, there's a… there's a component within the, there's, like, an SDK kind of level component that's analogous to, like, tracer provider, meter provider, logger provider, that indicates that it connects to some remote server, and is listening for telemetry policy changes.
it is the component that's responsible for interpreting those and applying those to the other SDK components.
**Jack Shirazi** 24:58 Yeah.
**Jack Berg** 25:01 So, Jason, that, like, what that would look like is, like, in a… just to kind of think about this in terms of declarative config and YAML config, it's like, you know, you have your file format, you have your resource meter provider, logger provider, tracer provider, and then you have another provider, which… what were we calling this?
Jack, did we… did we have, like, a name for this?
**Trask Stalnaker** 25:21 Policy provider.
**Jack Shirazi** 25:22 Was it… that was.
**Jack Berg** 25:24 Policy provider. Maybe it even wraps up into config provider, because that's already something that we have. I don't know. Or it could be a separate, like, thing, policy provider. But yeah, you configure policy provider with a remote URL, maybe some credentials or headers to authenticate with, and you know, behind the scenes, that will cause a policy provider component to be initialized that connects Waits for these commands, applies for these commands.
**Jason Plumb** 25:52 And then, presumably, anything that's using that, or the contents of that, has to, like, go through… it has to not… cache or hold onto references, right? You have to make sure that it's, like, getting the new thing every time.
**Jack Berg** 26:05 It needs references to, like, SDK tracer provider, SDK meter provider, SDK logger provider, and if it's going to be updating instrumentation config as well, I'm not sure where we've landed on that, but, like, the, like, SDK config provider as well. It might need a reference to that.
But those are… those are static, you know, across the lifes… lifetime of, like, an agent anyways, so I don't think it's that big of a problem to hold references.
But maybe you're referring to something else?
**Jason Plumb** 26:33 Yeah, like, if, if there's a component, I'm just using that term broadly, if there's something in the agent somewhere that's holding onto a tracer.
And… the behavior of that tracer changes due to a configuration change.
then that tracer could be basically no longer compliant, or it wouldn't be doing, like, what the new configuration says to do, if it's held onto for a long time.
Well, so, because if the layer… sorry, if the layer of swapping is, like, above tracer, right? If it's the tracer provider that implements the changes, and someone holding onto a tracer at a lower level.
Then when the changes are applied to the tracer provider, then they're not seen by anybody holding the tracer.
**Jack Berg** 27:18 So, we have actually some programmatic ways to do this today. So if you go look at SDK Tracer Provider, there are internal APIs to be able to update the enabled or disabled property of individual tracers, and so we've kind of sketched out how this works at the programmatic level.
And, you know, the next stage would be kind of hooking this up to remote servers and making it sort of dynamic.
Or not dynamic, but, I don't know, just, like, completing the whole picture instead of just having APIs. And so, what happens with these under the covers is, like, imagine you're an instrumentation holding onto a tracer.
What are you doing with that tracer? It's like, you know, you're processing HTTP requests, and you're calling StartSpan, and you're calling end span on those tracers. So under the hood, the backing SDK tracer, its implementation is going to change at runtime. And there's, like, a flag in SDK Tracer that, like, checks, hey, is this individual SDK tracer enabled or disabled?
And, you know, the behavior of the start span operation, it changes based on whether it's enabled or disabled. So, that's kind of how this works for that type of swap.
**Trask Stalnaker** 28:31 Yeah, it's very case-by-case, and yeah.
something.
**Jason Plumb** 28:34 You know, basically, anything that's being made dynamic kind of needs to be implemented all the way down the implementation stack.
**Jack Berg** 28:43 Yeah, and we actually had to be careful about which things we make dynamic, because as travelers.
**Jason Plumb** 28:47 Right.
**Jack Berg** 28:48 mentioning, like, they each have their own sort of behaviors and.
**Jason Plumb** 28:51 Sure, like.
**Jack Berg** 28:52 idiosyncrasies.
**Jason Plumb** 28:55 Yep.
**Jack Shirazi** 28:56 I mean, there's a bunch of things… there's a bunch of things that are dynamic that, we've put in dynamically in our distribution, and that I'm trying to contribute up to the Condric repo.
I think.
**Jason Plumb** 29:11 Yeah, that stuff is awesome, and I think… I mean, we have an op-amp client in our distro now, and you do too, and I'm like, if every vendor is, like, putting an op-amp client in their distro, it doesn't make sense for us to have one in the main upstream distro?
That was kind of weird.
group.
**Trask Stalnaker** 29:26 As soon as we have a vanilla… use case.
**Jason Plumb** 29:32 Okay.
**Jack Berg** 29:33 And that's what this telemetry policy is.
**Trask Stalnaker** 29:34 The work that…
**Jack Berg** 29:35 promises to provide. It's that vanilla use case. It's like, you know, all of a sudden there would be a specification somewhere that describes what SDKs are supposed to do with a op-amp client in a general way.
**Jason Plumb** 29:49 That's cool, that makes sense.
**Jack Berg** 29:53 And then at that point, the Alpam client can, it can be promoted to the core repo as well.
Because it's within the scope. So, then it's, like, a really easy fit into the agent, because the agent doesn't have to make this questionable dependency on a component.
**Jason Plumb** 30:11 Cool.
Good discussion, thank you.
**Trask Stalnaker** 30:19 Jonathan?
**Jonathan Halliday (IBM)** 30:21 Hey, alright, a couple of quick ones, just for awareness.
Bruno presented some work on, performance issues, overhead of observability earlier in the year.
I supervise students from Newcastle University. These are post-grad computer science students who do, approximately 5 months of project work is their, sort of major effort in the, the course. It's about half their, half their marks, half their credits.
So we've got one who wants to look at observability overhead.
So he'll be continuing the kind of work Bruno was doing.
I have a ton of questions for him, particularly around the profiling stuff, you know, what's the overhead of profiling, what's the optimal way to configure it for low overhead, and so on.
But if there's questions you had from Bruno's work that you think Yeah, we could have taken that further, we could have looked at this, ping me on Slack, and I'll see if we can work them into the project.
Ideally, I'd like him focused on doing some kind of reusable tooling.
That we can use to run those kind of benchmarks.
So we can deploy, you know, a little sample app and configure it with different levels of observability and get a feel for what the overhead of those is, particularly startup time and footprint.
So that's the first one.
Second one, progress from the profiling single SIG.
It looks like we're transitioning from, you know, early stage into alpha, which is the point where we say, we're going to try not to break it.
That'll happen.
publicly around KubeCon time. I think the actual release will be whatever the next release from the proto library is. 1.10, I guess it'll be.
So it would be nice to start shipping some support in the Java SDK shortly thereafter, so the maintainers can expect me to be asking awkward questions about what exactly we want to ship, and what we want the API to look like, and things like that.
What?
**Trask Stalnaker** 32:38 It does? Yeah, I was actually just looking at that, because there was a doc, PR… That was adding the profiling signal.
**Jonathan Halliday (IBM)** 32:51 Yeah, so one of the things we want to try and get ready for the public announcement is some documentation that explains what it does and how it does it. It's not really fully under-user documentation yet, because we don't have all the pieces in place. We can't write something as smooth as, you know, go and download this and set this config option and that kind of level stuff. It's more conceptual.
But yeah, we're trying to get the ancillary stuff beyond the spec into shape, so the various components that implement this, the, the eBPF profile, obviously, is the, the one that's most mature and most likely to be used, but on the Java side, people might want to use async Profile or JFR, and then export that data through the the OLTP, so putting in place options for that is a priority as well.
**Trask Stalnaker** 33:47 Is this module essentially what you would want to… is this the public…
**Jonathan Halliday (IBM)** 33:52 What I've been putting into the repo so far is the low-level bits for encoding.
The product above.
Onto the wire.
above that, there will not be a traditional API, because we don't really expect the users or their applications to be using it, but there'll be some kind of tooling, most likely initially something that you can point at a JFR file.
And it will convert that JFL file to the… OTLP format, and use the exporters to send it out over the wire.
So that's… that's kind of the initial focus, but I'm open to suggestions on what the kind of order of priorities is, and how we package it, and so on. I think there'll be a jar that has most of this in, and it'll be marked as an alpha jar.
How you configure that is… undefined. There aren't sort of well-defined config properties for it at this point, and to what extent we want that to be… tied into the way you configure everything else is up for grabs as well. We can't tie it into Global OpenTelemetry because there's no API, right?
You could, you know, get profiling, but it would have to return, like, object.
Unless we commit to… to an API.
**Jack Shirazi** 35:15 Have you got a high-level roadmap of… because you've mentioned 3 different profilers, and I'm just wondering…
**Jonathan Halliday (IBM)** 35:22 So, the async profiler people have been looking at the spec a bit, and they have the ability to write OLTB to disk.
So, async Profiler captures its own internal memory format and can export various things. It can export JFR, or something approximating JFR. I think there's a few bugs in it, frankly, but That's their main route to get data out at the moment. So it will export… From the sea level.
to disk.
So then there are questions of… Do we want to work with them to add something where… you can grab their data from memory and export it through the Java SDK pipeline instead.
Which would give… the SDK, the opportunity to annotate it, or filter it, or manipulate it, and would give users the ability to configure that export in the same way that they configure the other hotel signal types.
Because right now, they would have to configure, you know, the three existing signals.
in the SDK, and then configure profiling by talking to async profilers, proprietary, whatever.
Which is a bit clunky.
Jfr… doesn't support… OTLP in any way at the moment.
They, they only write to disk.
In their own proprietary format.
**Jason Plumb** 36:50 It's all for the event.
I just want to make sure there's consideration given to the events in the newer JVMs. Like, you can do a recording that's just providing events into, you know, program space.
**Jonathan Halliday (IBM)** 37:02 Yeah, so there's various things we can do there.
My initial pass will be… some kind of tool, you can point at a JFR file, and it will convert it and send it out over OTLP.
The next stage is then to be able to configure that logic through the SDK, perhaps, so that you can turn on JFR, with whatever JFR options you want.
And simultaneously tell it where to send the converted data.
So then it starts to look a bit more like the rest of the SDK.
**Jason Plumb** 37:35 Hey, Jonathan, I haven't been, involved in the profiling SIG in a couple of years, at least. I know that at one point, someone, I think it was… I think it might have been Datadog, they had some Golang code that was able to parse JFR. Do you know about.
**Jonathan Halliday (IBM)** 37:48 Yes.
We are aware of that, yes.
**Jason Plumb** 37:51 Okay.
Is it dead, or is it alive? Well, there's a couple of ways to handle JFR.
**Jonathan Halliday (IBM)** 37:56 You can reverse engineer the spec for the file format from the open source code in OpenJDK, and write something that will read the file.
If you're writing Java as I am, there is a Java API to the file that will give you the event stream as Java objects. Yeah. So, right now, I'm using that. It is far, far easier from a programming point of view, and it is far more reliable, because obviously they… being, you know, the Oracle JFR people, they change that code and keep it in lockstep with the file format.
So it doesn't break, whereas… Right.
They explicitly say the file format is not part of Java's public API. It's a proprietary implementation detail of Hotspot, and… You're on your own if you write anything against it and it breaks, you know, tough.
I've tried in the past to nudge them towards making it part of the spec, but they're not biting.
**Jason Plumb** 38:54 Yeah, I mean, I can also not blame them for not.
**Jonathan Halliday (IBM)** 38:56 Yeah, yeah, I mean, I get where they're coming from. They're very short-handed. I think they've got two engineers on.
JFR total.
**Jason Plumb** 39:05 The only reason I bring that up is because there's some desire for people to get that parsing of JFR out of process space, like, into, I don't know.
**Jonathan Halliday (IBM)** 39:13 Yes, so one of the options I was thinking was, if you're running the collector as a sidecar.
Can you have a module in the collector that will use Goline code, similar to Datadog's? You point it at a directory, it foul watches it, it says, oh, there's a new.
**Jason Plumb** 39:27 Right.
**Jonathan Halliday (IBM)** 39:28 file, it grabs it, it passes it, it exports it.
**Jason Plumb** 39:31 Yeah.
**Jonathan Halliday (IBM)** 39:32 I have a Google Doc, I think it is referenced from this SIGS document somewhere months back, but I can repost it, that outlines all these options.
Cool. Describes the different ways we could go.
And really, I'm looking for guidance from users or from this group on which ones are the priority for engineering.
**Jason Plumb** 39:52 Yeah.
I mean, one thing to keep in mind around this topic, too, and sorry, Jack, you've had your hand up for a minute.
**Jack Berg** 39:58 No worries.
**Jason Plumb** 39:58 Is that, there's kind of, like, a new policy in the collector that they're trying to get away from ever launching subprocesses, especially.
**Jonathan Halliday (IBM)** 40:06 Jamie.
**Jason Plumb** 40:06 VMs, because they don't want to have to bundle those, for very good reason.
**Jonathan Halliday (IBM)** 40:09 Yeah, yeah.
**Jason Plumb** 40:10 So… Just, that's something to keep in mind around that.
**Jonathan Halliday (IBM)** 40:13 Yes, if the collector was going to pass the code, then doing it in Go instead of… Calling out to Java to do it makes thermal sense.
**Jason Plumb** 40:20 Yeah, with all the protocols there.
**Jonathan Halliday (IBM)** 40:22 Have we got maintainers who want to, you know, take that burden on?
**Jason Plumb** 40:26 You know, I think we know the answer. Okay, cool.
Jack.
**Jack Berg** 40:32 Yeah, so just a couple of comments on, like, the… like, what does the footprint of profiling look like in the SDK and API? So, I'm happy enough to kind of let this let design sort of emerge organically. You know, if there's exactly one implementation, then it kind of seems silly to have anything except for the OTLP exporter piece.
But, like, if there's multiple implementations that want to leverage it, maybe they want to do similar things around, like, batching and exporting, right? Analogous to, like, you know, how the batch span processor, batch log processor, you know, batch everything up and export on a regular cadence, so maybe you want to introduce some shared code there.
Just on the, on, like, the global open telemetry piece, and, like, so I'm hearing some… some bits that are reminiscent of, how the conversation emerged in logs. Like, originally, when the log signal was emerging, there was only an SDK that was proposed.
And we eventually split out an API for some of the same things that you're working around, which is, like, you know, like, yeah, it becomes, like, awkward to have something that's instrumentation that has a dependency on the SDK, that doesn't really work with Java agent patterns. And so, like, maybe, maybe there's a way to make this work. Maybe, like, it's, like, it's not traditional instrumentation, and it's closer to sort of, like, resource detector level instrumentation, which is like a version of instrumentation, which lives strictly in SDK space, so maybe we can kind of wrap our heads around a new pattern for that. But, yeah, you know, in logs, we ultimately ended up with, like, an API, which is, like, a very thin wrapper around the SDK. It's essentially like a pass-through, and even having, like, a pass-through helped, you know, work through certain, like, design issues. So, yeah, we'll see where it goes. Like, if you can just, if you or whoever's working on this, like, start to commit these, like, these implementations to places where we can take a look at them. Maybe we can find, you know… maybe we can decide if there's opportunities for code reuse or not.
**Trask Stalnaker** 42:47 And for what it's worth, I don't think we'll have the same problem in the agent as we did with logging, because with logging, we are instrumenting logging libraries that the user pulled into their user space.
**Jack Berg** 43:02 Right.
**Trask Stalnaker** 43:02 because in the Profiler case, I think it probably would just all be SDK. We would just expose configuration options for people to opt-in to Async Profiler, and we would bring that whole package. We wouldn't have users bringing Async Profiler and us sort of bridging from that.
**Jack Berg** 43:24 Yeah, that would be a helpful simplification assumption.
**Jack Shirazi** 43:29 Sorry, just to go back to… the roadmap you're talking about here. We've got… there's at least four different options, so let me just go through and see if I understand them right. A potentially async profiler bundled in with the agent, or being able to be pulled in with the agent, and it'll write to OTLP to disk, and then you're going to have Something that will take that and send it out to the, the backend.
That's one option. And then the same with JFR, which you can just… that's already in the JVN, so that you don't actually have to have to get anything, bundle anything with it, and that's just gonna… trigger JFR to write out the file, and you'll convert that to OTLP, send that to the back end? Is that… is that the.
**Jonathan Halliday (IBM)** 44:15 No, no.
**Jack Shirazi** 44:15 that approach. And then we've got two eBPF approaches. One is the native one that only works with Java 25, An app, where the memory can be shared.
**Jonathan Halliday (IBM)** 44:28 That's… that's about… Context propagation, which is a separate issue.
So, the, we might want the Java process to expose either process level or process level and thread level.
Metadata to whatever is doing the profiling.
And if what is doing the profiling is EBPF, then the spec that was discussed a little while back, by Ivo is the, The one that will be used to export process-level information.
It's basically encode the metadata into a product buff and then stick it in a chunk of shared memory.
**Jack Shirazi** 45:09 And that's… that's still… that's the third profiling option, right?
**Jonathan Halliday (IBM)** 45:13 Well, the way that you get that metadata depends on what profiler you're using. If you're using eBPF, you use that protocol. If you're using JFR, then you don't need to, because the profiler is in process already.
So the way that you… Expose the metadata is different.
**Jack Shirazi** 45:30 But I'm thinking about… the options that we get to… at the back end, we're going to see a profile, and there's… we're talking about three technologies here that can generate the profile, which is async Profiler, JFR, or EBB.
**Jonathan Halliday (IBM)** 45:43 Yep.
**Jack Shirazi** 45:43 And with eBPF, we've got the native correlation for Java 25+, or if we want to do it before that, then it's going to be the C library that we have to.
**Jonathan Halliday (IBM)** 45:56 pull down or include. So these are the four… Or no context correlation. I think we probably don't do it. No one's got the appetite to look after that library, right? It's a lot of work.
**Jack Shirazi** 46:07 Right.
Without context correlation, it's… It's much less useful.
**Jason Plumb** 46:17 So we… we have context correlation for JFR. I think we've talked about this before.
Where we emit… we emit custom JFR events on context switch.
Which is not lightweight, but it's a way of propagating context. It's a way to, like, get context correlation working for profiles.
And then for async, no idea. Has anybody even thought about how to do it with async?
**Jack Shirazi** 46:45 And we're kind of already doing async and for… spans, so… It's… I don't think it's that difficult to change it over to do profiling as well. It's more the overhead involved.
**Jason Plumb** 47:00 Yeah.
**Jack Shirazi** 47:00 So the inferred span uses the async profiler, but it's very targeted in order to keep the low… the overhead low.
**Jason Plumb** 47:08 Yep.
**Jonathan Halliday (IBM)** 47:08 Yeah, the… the async profiler… has a… a way to attach context. It's got its own kind of API for this that is, usable in at least some context.
Cool. Loom virtual threads are the… the headache, right? Because, Yeah. The JVM doesn't expose user hooks for freeze and thaw, so you don't have any kind of callback unit you can attach to when the context changes.
**Jason Plumb** 47:40 Yep.
**Jack Shirazi** 47:41 Is there a site or somewhere that I can look at to see the… where we get to… I mean, what I'm really interested in is when we have something that you can… you can try out.
So…
**Jonathan Halliday (IBM)** 47:55 Yeah, No, not yet. Part of what I want to do, we as the Profiling SIG want to do for the launch is, have some kind of list of what components and what state they're in. I think we want to launch at KubeCon regardless of whether we've got an end-to-end demo, but certainly the priority for me is to have at least one path where you can go from generating profile, they're having it displayed in a backend somewhere. So we need to rustle up a back end, which obviously is, you know, out of scope.
the profiler will likely be the BPF1 initially, and JFR as soon as I can make that work. Because the exporter will read JFR files, it will work with either JFR or async Profiler, since Async Profiler can write JFR's format.
So that'll be the first step, as it were. And after that, we'll work on fleshing out, easier ways to configure those, and… And perhaps some more options in the collector.
But no, right now, there is no page you can go to that says, you know, download this, configure it with these things, and… This'll work.
I struggle with that even for development, because… I'm running on one version of the spec, and DevFiler, which is the ideal backend to use for dev work, is not on the same version. So freezing the spec will be very, very welcome. It'll give everyone a chance to get on the same page about what the wire protocol is.
**Trask Stalnaker** 49:31 Cool. Alright, we got, our agenda keeps… Growing. Jack?
**Jack Berg** 49:39 I added this when I thought we were gonna be finishing before the 30-minute mark, and so I just wanted to share a sort of status update on this. We've been making some progress on, on doing benchmarking as part of CI.
And, you know, this work was initially landed by, Tyler Benson maybe a couple of years ago now. He provided his scaffolding to, like, have a benchmarking GitHub action that, reports this to, and publishes this to a GitHub page.
And it uses, you know, dedicated hardware so that the benchmarks are more repeatable. But what I've done recently is I…
**Trask Stalnaker** 50:21 So much, and yet still so noisy.
**Jack Berg** 50:24 Well, that… there you go, that's one of the things. So, like, that I talked about, what we can do next is reduce the variance. So the hardware can be a factor in the variance, but so can the tests themselves. Maybe they need to run longer, for example, to let garbage collections normalize, things like that.
But yeah, so, what I've done kind of recently is that, I… I… you know, Tyler, the benchmarks that he was… that he was publishing were ones that we had. They were just things that were laying around that were sort of micro-benchmarks we wrote as maintainers for specific problems, and if they were published, they're not really useful for a user, because, like, the user is like, what is this thing? Why… why are you telling me, like, how long it takes to fill up a bag of attributes, like, that doesn't mean anything to me. So, I've been sort of, reviewing them and adding a layer of, like, standardization to the benchmark, so we're gonna benchmark Things that we can all understand and frame them correctly for users so that they can actually be useful.
And so that's where we're at now. There's now simple, record-level benchmarks for each of the three signals.
And kind of what comes next is… I have a list here, so I want to tune the displays of these things. It's not really easy to see what each of these series represents, and so I want to kind of go outside the defaults that we get from this GitHub Actions benchmarking toolkit and, you know, kind of customize the CSS and HTML so we can… it can be easier to… consume.
I want to expand this from just record-level benchmarks to look at, like, the export-level benchmarks, so we can see, kind of, the progress on our various exporters, OTLP in particular over time, see if we make improvements or degradations in OTLP serialization.
I talked about variance. I want to reduce the variance of these tests so that they're tighter and that they have more signal when something changes.
And I want to talk about these publicly. So, like, now that we have something that I think is actually useful for end users, I want to talk about that on Opentelemetry.io and link to them, and maybe link to them from our README as well. So, yeah, just a quick status update on this.
**Trask Stalnaker** 52:54 Nice.
Yeah, but… That would be really cool.
to, like, have a complete story around that. It's a hard one to… it's a hard story to put together.
But, I like where you're going with it.
**Jack Berg** 53:14 Record and collect. Those are the two things we want to characterize, and we want to characterize them independently, and we want to talk about them in plain English, so everyone knows what we're testing and why, and why other things don't matter.
That's funny.
**Trask Stalnaker** 53:27 And we want… and we don't want, what's this look like? Like… 30% variance, run to run.
**Jack Berg** 53:39 We want to… ideally, variance should be, what, below 5? Maybe… maybe 7? Something like that.
We'll get there.
**Trask Stalnaker** 53:52 All right.
Thank you all for joining.
Good chatting, as always.
**Jack Berg** 54:00 Alright, see you later.
**Jason Plumb** 54:01 Take care, everyone.
**Trask Stalnaker** 54:03 Bye.
