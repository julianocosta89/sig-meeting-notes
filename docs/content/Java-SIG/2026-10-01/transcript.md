SIG: Java SIG
Date: 2026-10-01
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Trask Stalnaker (Microsoft Corporation)** 04:06 Hey, Fox.
**BRUNO Baptista** 04:11 Hello.
**Jay DeLuca (Raintank, Inc. – Grafana Labs)** 04:12 Hey, Charles.
**Trask Stalnaker (Microsoft Corporation)** 04:34 Doc is starting to get slow. Wonder if we need to rotate.
Yeah, did we discover that we can just do… wait for Jason. He'll… I think he did this the last time.
I think we can just do tabs now.
Instead of creating new docs.
**Jay DeLuca (Raintank, Inc. – Grafana Labs)** 05:10 I think he's actually out today. I saw him post in the Android channel.
**Trask Stalnaker (Microsoft Corporation)** 05:18 Alright, problem for next week.
So, just quickly on the B3 stuff, the last 2X release, just working… getting the last PR… Lori's already approved it, but I… Still working through a couple things on it, and then also spinning up the, The release notes now.
If I could get a… this is an approval on this, I want to run… use the new model for the more newer model, not… For the, Release notes, I think, before… oh, it's not… oh, I guess it was defaulting somewhere else.
It was using 5.4 Mini before.
Gregory A. Yeah, so hopefully that will actually go out today. Did not quite make September.
And then after that, we get to start ripping stuff.
Ripping stuff out. Yes, there's so much… so many things we've… behind that V3 preview flag, and… Or SEMCOM and things. Yeah, that will be fun.
Yeah, and then, Jay, I saw your… the blog post is ready. I'll look over that once the release is actually out.
**Jay DeLuca (Raintank, Inc. – Grafana Labs)** 07:08 Out of curiosity, did you… did you get everything in that you wanted to? Like, if you had another 6 months, is there anything else that you would have tried to get in, seeing as this is, like, a once-every-two-year?
**Trask Stalnaker (Microsoft Corporation)** 07:21 The… I was… kind of wanted to get the RPC.
bump in, and I kind of wanted to get the Gen AI stuff at least aligned all to the latest.
I think those are probably my… 2.
primary regrets, but neither of them are stable yet.
**Jay DeLuca (Raintank, Inc. – Grafana Labs)** 07:44 Right, yeah.
**Trask Stalnaker (Microsoft Corporation)** 07:46 But RPC is so close to being stable that probably… I might consider… before the 3.0 release, depending on how RPC goes, I could… Possibly see that happening.
Gen AI, no, there's too much.
And those are big… I mean, I guess at least… We don't have as many RPC or Gen AI instrumentations, but man, all that messaging… All those messaging PRs, those were messy, and… All the database PRs, those were surprisingly messy, too.
A lot of… A lot of churn.
**Jay DeLuca (Raintank, Inc. – Grafana Labs)** 08:35 Yeah, it's crazy how much you're able to pull off, though.
In the past couple months.
**Trask Stalnaker (Microsoft Corporation)** 08:42 Well, thanks to, obviously, thanks to AI, and thanks to Lori for… Oh, yeah.
Cool, let's, let's just hit up our… Not a lot of topics these not as many topics these days.
Jack. And if anybody else here has topics, please go ahead and throw it on the meeting.
agenda.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 09:19 Yeah, please do that. So… a couple of weeks ago, we were talking about some of the limitations of the SDK, and, from an op-ed perspective, and from a process contact sharing perspective, about, you know, these are… these are different Gary Holness@things that would need to consume the resource that's configured with an SDK to do various things. For opamp, the resource is the source of identity that it uses to communicate with servers.
For process context sharing, this is… the resource is the thing that's being shared across process, so it's the thing that's being written to the shared memory location, so that other processes, like eBPF things, can pick that up.
And, you know, I was talking about how there's been some talks at the spec level about like sort of formalizing this, the notion that you should be able to access the resource information of an SDK and that that was primarily being driven by entities work and that like as soon as there was spec that was, you know, suggesting that we could have an accessor for resource information that, you know, I would go and work and make it happen.
And the spec PR landed. There's, like, a base entities PR that talks about a resource provider as, like, a formalized concept in the resource spec now. And this is… this is my idea of what this looks like.
And so, you know, at a high level, what this would allow us to do is we have our OpenTelemetry SDK object, and OpenTelemetry SDK has accessors for SDK Meter Provider, SDK Tracer Provider, SDK Logger Provider.
And then, now it would have access to SDK Resource Provider. And so anybody that had access to an OpenTelemetry SDK instance.
would have access to an SDK resource provider. And the resource provider has a simple method called GET that you can use to get the, you know, the resolved and current resource of the SDK.
And so, one of the problems that we have to solve with this is that we have this composite object, OpenTelemetry SDK. It's a composite of meter provider, tracer provider, logger provider. And, you know, up until now, you configure the resource on those separately. And so, it's by convention that the resource aligns.
But it, you know, technically, you could build an OpenTelemetry SDK object where the resource with the logger provider was different than the meter provider. And that sort of is in tension with this idea that there's, like, a sort of shared resource provider, which is, you know, represents the full composite. And… And that's something that I had to solve with this. And so, basically, the way that I solved that is, like, you know. the providers, meter provider, tracer provider, logger provider, they have these APIs where you can set the resource associated with them.
And they have a new API now where you can set the resource provider associated with them. And the resource provider, like, the setting of the resource provider is mutually exclusive with setting the old, like, resource.
Like, calling set resource. So if you try to do both, you get an error.
And when you go to construct your OpenTelemetry SDK object, that doesn't actually accept a resource provider as an argument. What that does is it resolves the resource provider from meter provider, tracer provider, logger provider. It introspects at the resource provider from all of those, and makes sure that they're in alignment with each other.
And if they're not in alignment, you know, we return essentially like a no op resource provider. And you, you know, you get a warning message that says that the resource of your tracer provider, logger provider and meter provider don't all agree. So you did something wrong.
But, you know, assuming they do agree with each other, you know, the resolved resource provider of your OpenTelemetry SDK instance is, you know, what you would expect.
So, the things that I expect Resource Provider to do is I want to be able to do the things we do today with it. I want, like, when you're constructing it, I want you to be able to attach static resources to it.
Like, that's what we do today. We, like, you know, we build up this merged, resolved resource by taking one resource and merging them with another. And I want this to be future-proof to this, like, entities future, where descriptive attributes are subject to change.
And so I want there to be a mechanism in resource provider where you can not just register a static resource, but you can register, like, a supplier pattern, and some sort of cadence or signaling mechanism where you can signal, like, when that supplier should be invoked.
And that would — I didn't build that into this today because we don't have a use case for it today. But this is evolvable to that future, which is coming, at least at the spec level.
The other thing that I want to, like, you know, be evolvable into is the idea of, like, registering some sort of, like, watchers for resources. So, if you're thinking from Jonathan's process contact sharing perspective, like.
When do you want to write the resource to the shared memory? You want to write it when it changes.
And so, like, it's nice if you can get a hook into when the resolved resource has changed, because the descriptive attributes of entities have changed.
And so, like, this resource provider, like, I didn't build that in again today, but it's easily, like, evolvable to, like, a watcher pattern where you can register, you know, callbacks.
time.
So, that's the basic idea of this. I'm trying to unblock OpAmp, I'm trying to unblock process context sharing, and I'm trying to… and, you know, other use cases that we've talked about in the past, where just people need to consume the resolved resource of the SDK. Trying to unblock all those, I'm trying to stay within the spec, and I'm trying to be forward-looking to, like, what entities requirements are going to come in the future. And this is all sort of, you know, staged up in this PR as a development feature, you know, experimental feature, so things are in internal packages and, you know, using the various techniques that we have to hide this from the public API.
So… So, you know, from that standpoint, some of this is, is not, like, it won't be available when this PR merge, because, like, you know, there's, like, internal APIs, but if you… if you're okay using internal APIs, then you can access all the things that I just talked about.
And that's my spiel.
**Trask Stalnaker (Microsoft Corporation)** 16:27 What is, what's the use case people are talking about for, updating resource attributes via OpMAM?
**Jack Berg (Raintank, Inc. – Grafana Labs)** 16:38 Not via op-amp, via entities. Op-amp just needs the resource, and I don't really think it cares what the resource is, but it needs the resource to act as the identity that it uses when it's communicating with the server.
**Trask Stalnaker (Microsoft Corporation)** 16:50 Oh, okay, so it just needs access to it, not updating… Okay.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 16:56 Yeah, there's two things that need access. There's, you know, op-amp needs access, process context sharing needs access, and process context sharing needs to be informed when there is an update. And then the things that would update would be, sort of, future, future entity, provider type things.
Where the descriptive attributes are subject to change.
**Trask Stalnaker (Microsoft Corporation)** 17:19 Okay, got it. Thanks.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 17:24 Yeah.
**Trask Stalnaker (Microsoft Corporation)** 17:26 I'm surprised you got that all hidden in internal, Code in only 977 lines.
Usually… Yeah, usually those, like, balloon…
**Jack Berg (Raintank, Inc. – Grafana Labs)** 17:46 Yeah, so I'm reasonably happy with this.
I'm not sure if it's a priority for anybody, but, like, you know, I know at least, you know.
Jack Shirazi and Jonathan would be interested, because we were talking about it a few weeks ago.
And, you know, we've actually long stand… we've had this request for a long time, right? So, you know, in the agent, there's.
maybe not in the agent, but there's, like, from auto-configure, there's an accessor for the resource. They're, like, you know, the auto-configured resource, and, you know, folks have talked about how their distributions need that. I know the Splunk distribution has needed that, and I've heard of other ones needing the auto-configured resource, and, like, you know.
We've sort of been blocked on that for a long time, because the spec made no mention of it, so.
Yeah, maybe.
**Trask Stalnaker (Microsoft Corporation)** 18:34 Well, we have that… we all use that workaround, the… I mean, the auto-configure gives us an internal class that allows us to get the resource off of it.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 18:45 Right, right, and so all those types of usages have been waiting for this, so… And I guess from a naming standpoint, so I called it SDK Resource Provider, and that was intentional. I didn't call it Resource Provider. And.
The reason is, is because some folks in spec and entity conversations have been talking about, like, whether there should be an API access or… you know, operations related to resources. Like, maybe… maybe, entity detectors, our API level. And so, you know, calling it SDK Resource Provider preserves the resource provider as, like, a possible future interface name at the API level.
But not needed today.
**Trask Stalnaker (Microsoft Corporation)** 19:45 Aren't all of the SDK ones… like, SDK, Tracer provider…
**Jack Berg (Raintank, Inc. – Grafana Labs)** 19:53 Yeah, so it maintains that consistency as well.
So… Twofold.
That's all I have to say, so yeah.
If you want to see this happen, go review it.
**Trask Stalnaker (Microsoft Corporation)** 20:15 Yeah, so once this is in… Then.
a… we could potentially… Deprecate that… the auto-configure get resource.
internal hack.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 20:35 Yeah, as long as we made sure that we updated AutoConfigure to… and I saved that for, like, a future PR, so AutoConfigure needs to make sure it returns an extended OpenTelemetry SDK instance.
Right now, Declarative Config does that. AutoConfigure would need to do that as well. And then at that point, like, every caller of AutoConfigure, whether you're using System Properties or Declarative Config, gets an extended OpenTelemetry SDK instance back, which allows you to access this resource provider.
**Trask Stalnaker (Microsoft Corporation)** 21:08 And for the process context sharing.
You need to basically be passed in an OpenTelemetry SDK.
instance.
Like, so it's not… it's not instrumentation, it's not API-driven, it's… it's still reliant on the SDK.
getting passed in.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 21:38 That's how I think of it right now is just some sort of like background thread worker thing that, you know, has access to an OpenTelemetry SDK instance and, you know, does something with that. But Jonathan, feel free to correct me if, if you have a different.
**Jonathan Halliday (IBM)** 21:52 Yeah, I mean, I was interested in what you're saying about pullbacks when it changes, because I don't think this is a thread in the same way that something like an exporter is.
process context is… Kind of a one-off right now, unless it does change.
The way I'd integrated this initially was that I had an agent extension, And, It's just implementing, AutoConfig, customizer provider, whatever it is. That's very early in the lifecycle.
And I don't think it's going to work, because I don't think the resources actually Up at that point.
But if… if the callback treats going from there isn't a resource to there is a resource as a… as something that triggers the callback.
Then, the integration point I need is some way to register a callback.
That callback will publish the context to shared memory.
If any change is made, the callback will get triggered again, and then I don't need a thread.
This is not going to be something that's that's polling for changes. It's Something that's going to expect them very rarely, if at all.
And yeah, the callback I think is the right model for that.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 23:09 Yeah, and right now, Jonathan, there is no way for it to change anyways, so we can just, like, punt on that callback, we can punt on the thread model altogether, and, you know, once… once.
**Jonathan Halliday (IBM)** 23:19 Well, can we put on the callback? What's the integration point for this if it's not the callback?
**Jack Berg (Raintank, Inc. – Grafana Labs)** 23:25 Oh, I guess we're, we need to… there's two possible callbacks. So there's the agent callback you're talking about, where, you know, that's a callback to give you access to the, you know, the… extended OpenTelemetry SDK, from which you access the resource. So you need that callback, we can't get away from that. And then, you know, in my spiel, I was talking about a separate callback.
That is future work that where we would extend SDK resource provider so that you could actually register callbacks to be invoked when the resource changes.
**Jonathan Halliday (IBM)** 23:54 Right.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 23:55 Because that doesn't exist yet, we don't need it.
**Jonathan Halliday (IBM)** 23:57 I guess we're using callback in a slightly different way.
The current extension point, where I'm… using the… The auto configuration customizer is very early in the lifecycle, because the whole point of that integration is that you can change the Configuration before it's set.
Right? It's where you can put in custom config.
And I'm wondering if At that point, I ask the extended SDK for the resource, is the resource actually configured already?
**Jack Berg (Raintank, Inc. – Grafana Labs)** 24:36 So you don't actually need to change the configuration for the SDK, right? You just need to add.
**Jonathan Halliday (IBM)** 24:41 No, I don't need to change it, I just need to access it, but… What's the lifecycle hook I use to get my thing to be called if it's not an agent extension?
**Jack Berg (Raintank, Inc. – Grafana Labs)** 24:51 It is an agent extension, you just have the wrong one. I sent the link over in the chat.
for a.
**Jonathan Halliday (IBM)** 24:56 More than one. Right. Okay, that's the secret bit I need. Okay.
Yeah, that makes sense, right. Okay, so I can change to use that one, and that should be fine.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 25:09 And actually, there's two, and maybe Trask can fill me in on the difference. So there's Before Agent Listener and After Agent Listener. I just sent the Before Agent Listener in the chat in a separate link, and they both have access to the, like, the auto-configured SDK, which would give you access to the resolved resource.
But, you know, one is they're called at different times in the life cycle, and I don't know which one is best for you.
**Jonathan Halliday (IBM)** 25:39 Okay, then yeah, yeah, if I can do that, I think… I think we're in great shape for the process context stuff, then.
The only other bit of configuration surface, I think, for the process context is simply turning it on and off.
I kind of hacked in… I just invented an environment variable out of thin air to do that, but… My understanding is that really needs to be part of the OTEP, part of the spec.
If we're going to do that.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 26:06 You can hack up your own, like, we have plenty of precedent for coming up with our own.
**Jonathan Halliday (IBM)** 26:10 Okay.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 26:11 and environment variables, just be sure to include, like, otel.java.experimental in there. We have a convention for how we label, like, you know, environment variables as, like, subject to change, and…
**Jonathan Halliday (IBM)** 26:25 Okay, so by putting experimental in there, that signals to the users that it's.
potentially gonna go away or change at some point. Yeah, that makes sense.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 26:42 Sweet.
Seems like we have a decent story for this.
**Trask Stalnaker (Microsoft Corporation)** 26:52 Yeah, and I think, so you can actually get, Jonathan, I think that… resource… from this guy… Today, this is kind of the hack we were… talking about,
**Jack Berg (Raintank, Inc. – Grafana Labs)** 27:15 I'll share a link to that, how you can get it from it today.
**Trask Stalnaker (Microsoft Corporation)** 27:18 Thanks.
And… I… I think, generally, the agent listener is the better Place, only because, anything that runs in before Agent Listener and loads classes, that loads before our instrumentation, our bytecode instrumentation is watching, and so… Then we can still re-transform those classes, but we can't change their structure, so we can't inject virtual fields into them.
Which basically… Hurts. Like, we try not to load.
Job util concurrent stuff that we want to add fields into.
Alright, nice, Jack.
And that should help that.
Dory move forward in the spec, hopefully, if people start seeing prototypes around.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 28:41 Yeah, I also want to rebase, Josh Charette's entity work on top of this, although I don't think it's, like, necessarily blocking or anything like that, it's just gonna have some merge conflicts, but, you know, the whole reason… the whole reason that resource provider was added to the spec was for entity reasons. We didn't technically need it, but it helps clear up some things. So.
Yeah, maybe we'll see that, merged into the… the… Core Java sooner than later.
And, I don't know, Trask, if you heard, some of these conversations unfolding about entities, but, like.
There's this debate about whether there should be a, a way to opt into entity behavior, or opt out of entity behavior at the resource detector level.
And Daniel Dilla basically made a decent argument that, like, hey, this whole thing's unnecessary. Let's just… like, as soon as resource detectors, like, can be updated, let's make them entity-aware. And so they always contribute resources with… that are, like, entity-aware.
And, you know, and therefore they'll export that entity information over OTLP, like by default, without any opt in or opt out. And like, it just doesn't matter. It's just like extra bytes on the payload, a little bit of extra bytes. And if somebody is interested in consuming that on the receiving side, then, you know, they can, and they're doing it under the understanding that this is experimental.
part of OTLP.
And so, we got rid of that whole… I think that the entities group is, like, moving in the direction of getting rid of that whole, like, opt-in, opt-out thing, and just, like, simplifying it to, like, hey, make all resource detectors entity-aware as soon as it's reasonable to do so.
**Trask Stalnaker (Microsoft Corporation)** 30:25 I see, so even before it's stable?
**Jack Berg (Raintank, Inc. – Grafana Labs)** 30:28 Yes, yes, that would… that's the key bit. And so, you know, kind of how this would work is we'd go through… like, once we have the ability to record entities in OpenTelemetry Java Core, we'd go update the resource detectors that are in instrumentation, and have them record, like, the entities.
And then, like, all the time. No, like, opt-in, no flag reading or anything like that. And, as soon as that was updated, then, you know, all of a sudden, Java agent users would, you know, be… have access to entity information.
**Trask Stalnaker (Microsoft Corporation)** 31:02 And so there we're just relying on OTLP consumers.
Knowing that the, entities portion of the proto is marked development.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 31:17 Correct. And I'm not the one making these arguments, but I'm also not arguing against it, because I think it's, like, a reasonable interpretation.
**Trask Stalnaker (Microsoft Corporation)** 31:24 I can live with that.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 31:26 Yeah, and, like, I like a simpler story from our end.
**Trask Stalnaker (Microsoft Corporation)** 31:30 Yeah, I would love… I mean, the entity stuff, has taken a while, so anything to remove.
roadblocks there.
Sounds good.
And you said something that I had… I think I had missed. So, resource provider… Is already in the spec.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 31:53 And it got added to the spec, yeah.
That's what… that's what gave me the… the… So…
**Trask Stalnaker (Microsoft Corporation)** 32:04 What do we call it?
**Jack Berg (Raintank, Inc. – Grafana Labs)** 32:06 It is called. Yeah, there you go. That's probably. No, it's provider. That's. It's.
And maybe with a space, though, like you had it. Okay.
Yeah, go to just the resource SDK. There's a… there's a dedicated section for it. If you look at the navigation on the right side.
resource provider. There it is.
So, yeah, it's responsible for, you know, providing access to the…
**Trask Stalnaker (Microsoft Corporation)** 32:45 is.
Do you know if, any other languages have implemented it?
**Jack Berg (Raintank, Inc. – Grafana Labs)** 32:53 No, I… I guess, like, that would probably be in the description of the PR where this was added, but I don't.
**Trask Stalnaker (Microsoft Corporation)** 33:02 Yeah.
Okay. Yeah, just thinking of next steps for, Getting it to stable.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 33:11 Yeah, it would be great if this was stable, huh?
And I guess one thing I forgot to mention is, like, so, you know, in the spec text, it talks about, like, the resource provider is responsible for providing the resource to all the other SDK components, right? And so the way that I, like, wired that in is, like.
The resource provider is now in the shared state of the meter provider, of the tracer provider, and the logger provider, and so every time we are going to, like, construct a span data, or metric data, or log record data record that has a resource attached to it, we consult the resource provider, rather than the statically configured resource.
So like.
You know, this is wired into the deep internals of the SDKs.
And therefore, the SDKs would automatically get any changes to the resolved resource, like, you know, if and when we go to support that, so it all kind of wires together nicely.
**Trask Stalnaker (Microsoft Corporation)** 34:13 This is probably why I missed it, because it very much undersells… the PR title very much undersells adding a… adding the resource provider.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 34:24 Yeah, also, the PR description doesn't talk about any prototypes at all, so I don't know, somehow… I think… Somehow this did not get the scrutiny that, like, normal spec PRs are subject to. Maybe it's because it's been open for 6 months and everybody just sort of gave up.
**Trask Stalnaker (Microsoft Corporation)** 34:44 Well, or thought it was just related to entity, which I guess it is, sort of. I don't know.
Alright, well, we are out of topics. Anybody have any other… Anything they want to raise today?
**Jonathan Halliday (IBM)** 35:01 Yeah, I'll throw in a quick one.
I was performance tuning the thread context stuff. And what thread context does is it intercepts writes on the context storage.
And it serializes certain elements of that.
into an off-heap buffer, which is then exposed via a C plus plus local to the eBPF profile, or whatever else, wants to know what the context on that thread is.
So it's a way for things that can't access the thread local or the storage, because they're not… on the Java heap, To be able to get roughly the same information, and… As part of this, it's serializing, span ID and trace id which are strings.
But it's serializing 2 binaries. It's converting them back into The original form they were in when they were created, ironically, which is… You know binary longs or byte arrays.
And that's turning out to be a little bit of a performance hit. It's not drastic, but I was looking at the code and thinking, there's got to be a better way.
So, the SPAN context interface.
has getters for both forms. You can ask it for the string form, which is… it's just returning the field, because that's the native form that it's stored in, or you can ask it for the byte array form, which is what I need, in which case it's calling a converter function.
How would we feel about changing the internal representation so it's dual representation? It'll store the byte array form.
As well, and pass it around.
As far as I can see, that increases the footprint, but it doesn't change the API because the getters are there already.
It will, potentially take a hit on creation, because what creation currently does is it… Creates a couple of random longs and converts them to strings, and then passes those strings to the The create function.
So we could, I guess, change that so it passes in the… The original form, the long form.
And it's then up to the create function to translate them to strings or We could just have a version of the create function that took the the original form as well as the string form or perhaps just the original form and created the strings itself. But I think that's the only API point that changes.
It changes the memory footprint, obviously, because now all these are carrying around.
**John Watson** 37:50 So what about?
**Jonathan Halliday (IBM)** 37:51 presentations, but…
**John Watson** 37:52 What about doing it lazily, like having a lazy… I mean, I guess here's the question. Is this something that needs to be called a whole bunch of times?
**Jonathan Halliday (IBM)** 38:01 Oh, yeah. Any time context storage is called, because now context storage is in two places, right? You've got the on-heap context storage, which is what lazy storage is doing. It's putting in thread locals.
But those Java thread locals aren't visible to external viewers because they're on the Java heap and they're moving around with the garbage collector in.
they're in Java's internal format, they can't be read, right? So, anytime you write to storage, you also want to write an off-heap copy.
So whenever the context changes, whenever you've got a new context, you write it to storage, and an interceptor Only… the storage.
Copies it to off heap, serializes it to off heap.
I've lied about a little bit because.
**John Watson** 38:46 given… for a given span, for a single span.
You would need to make a call to get the byte array.
**Jonathan Halliday (IBM)** 38:55 Yes.
**John Watson** 38:55 Anytime the content…
**Jonathan Halliday (IBM)** 38:57 Time that's been put into storage.
**John Watson** 38:59 Okay, that makes sense.
**Jonathan Halliday (IBM)** 39:00 Pretty much all the time.
**John Watson** 39:01 That makes sense. That makes sense.
I mean, if you're…
**Jack Berg (Raintank, Inc. – Grafana Labs)** 39:05 Howard…
**John Watson** 39:07 Go ahead, Jack.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 39:08 How are the spanned contexts typically created? Are they typically created from strings? And is it like feasible, tractable to, you know, change the common initialization point to initialize from byte array? Like, is the byte array more accessible than the string?
**Jonathan Halliday (IBM)** 39:24 I don't think it's by the way, I think it's Longs, but…
**Jack Berg (Raintank, Inc. – Grafana Labs)** 39:28 Is.
**Jonathan Halliday (IBM)** 39:28 Essentially, that's the way they're created, right? Random calls next long, I think.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 39:34 Yeah.
Yeah, because I'm thinking something similar to John, like, lazy initialization, and I'm wondering if, like, you can kind of have two-way lazy initialization, like, if you have an internal field for the string representation and the long representation, and you can initialize either way, based on whatever you have, and then the opposite of what you have can be lazily, like, created when you call… when you fetch the accessor for that.
So if you initialize with a long and you call the string, well, lazily initialize that. And, you know, vice versa. If you initialize with a string and you try to access.
**Jonathan Halliday (IBM)** 40:05 That's effectively what we've got going on at the moment, because when I call.
The getter for the bike form.
It lazily converts the string form to byte form, but that's expensive.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 40:19 Yeah, so I'm saying, I'm saying…
**John Watson** 40:20 The expense is going to be, the expense is going to be, we have to, the pay expense has to be paid somewhere, right?
**Jonathan Halliday (IBM)** 40:26 No, you don't, because it was created as a long in the first place.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 40:30 Right, so that's what I'm getting at, is you're.
**Jonathan Halliday (IBM)** 40:32 You just keep that long instead of throwing it away. What happens right now is the binary form is thrown away once the string form is created, and only the string form is passed around.
So if you want the binary form back, you have to convert the string form back into the binary form, because you didn't keep the binary form.
I'm just saying, keep the binary form.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 40:49 Yeah, and I agree with that. Like, you know, that's why I'm saying like two different initializers, one with the binary form, one with the string form. And we've changed the common code path, which initializes these span contexts all over the place from, you know, using the string creator to using the binary creator.
**Jonathan Halliday (IBM)** 41:05 Okay.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 41:05 having.
**Jonathan Halliday (IBM)** 41:05 So, conceptually, you're fine with changing the… I think it'll be the immutable spam context, or whatever it is that That passes this around to passing around both forms.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 41:17 I think so. Like, right now, it's an auto-value implementation. We might have to switch to, you know, a concrete implementation to get these sort of lazy semantics that we want, but.
**Jonathan Halliday (IBM)** 41:28 Okay, well, I'll experiment with it, and… put up a PR at some point then, as long as you're fine with the concept, yeah. All right, thanks.
**John Watson** 41:36 Yeah.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 41:37 an.
**John Watson** 41:37 This is all a bunch of internal stuff, like, we can change this however we want for new use cases without any… without any problems.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 41:48 It might actually help just, like, the general case as well, like, you know, even setting aside this, thread context sharing, you know, if every single time we initialize a span.
We have a generator that generates the binary form, and we're creating a string from it. Like.
if we're doing that unnecessarily, and we can, like, keep the binary representation for very, very long into that span's lifecycle, maybe not even render the string until it comes to export time, then we can get, like, a little bit of extra CPU off the hot path.
No.
**John Watson** 42:19 I mean, it is, unfortunately, the string representation is what is put onto the… like, when you have… throw it in the log… into logs, though, right? So it's… Yeah.
So it's gonna be, almost certainly, the string representation is gonna be needed.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 42:34 If you're, if you're, you know, enriching your logs with that.
**John Watson** 42:37 Or sending it on any export.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 42:40 Right, but if you're doing it on the export…
**Trask Stalnaker (Microsoft Corporation)** 42:42 the.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 42:42 Resolve it until off the hot path.
**John Watson** 42:44 It's true, it's true.
**Trask Stalnaker (Microsoft Corporation)** 42:46 But also does OpenTLP encoded as, Binary already?
**Jack Berg (Raintank, Inc. – Grafana Labs)** 42:53 Oh, I think it's this weird… it's… It's…
**John Watson** 42:57 OTLP is not that simple.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 42:59 It's so annoying. It's like the one VVA.
**Jonathan Halliday (IBM)** 43:02 It is a byte array, but it's a byte array of the UTF-8 representation.
**John Watson** 43:06 Yeah, exactly. It is bytes, but it's not the same.
**Jonathan Halliday (IBM)** 43:09 Yeah, it's text bytes.
**John Watson** 43:11 Yeah.
**Trask Stalnaker (Microsoft Corporation)** 43:11 Okay, okay.
**John Watson** 43:13 And this is why we decided long, long, long ago.
**Trask Stalnaker (Microsoft Corporation)** 43:17 Yeah.
**John Watson** 43:17 Store it as a string because it was actually going to be, it actually ends up being the most efficient.
**Jonathan Halliday (IBM)** 43:22 I did think about changing the process context.
Sorry, the Fed context OTEP.
But we're quite keen to keep the chunk of shared memory as short as possible, so it's as few cache lines as possible.
for performance reasons. That's why it's binary. It's half as many bytes.
**John Watson** 43:43 BRUNO, what's up?
**BRUNO Baptista** 43:46 Hey everyone. So, Jonathan, I got curious about the About the two storages that, that you mentioned.
**Jonathan Halliday (IBM)** 43:57 Yeah, because this is going to be nasty for reactive.
**BRUNO Baptista** 44:00 Yes, that's what I'm…
**Jonathan Halliday (IBM)** 44:02 for virtual feds too.
**BRUNO Baptista** 44:03 Yes.
So,
**Jonathan Halliday (IBM)** 44:06 Is that the aspect you're curious about?
**BRUNO Baptista** 44:11 Yeah, if you could, if you could…
**Jonathan Halliday (IBM)** 44:13 So the external viewers resolve this using a C++ thread local, a TLS.
So they're only aware of, the carrier thread.
So with reactive, where you're using thread per core, or with virtual threads, where you're mounting V-threads onto carriers.
Whatever is doing the context switch, has to… resync the two copies, basically. It has to take the on-heap copy.
which is in the hotel SDK's storage engine.
And in case of Reactive, you've overridden that storage engine so that it's using The vertex context, right?
**BRUNO Baptista** 44:57 Correct.
**Jonathan Halliday (IBM)** 44:58 Yeah. So it's already not using thread locals. The default one is thread locals.
You have to patch whatever is… I'll call it mounting the context, but switching into that context.
to update the TLS to point at the buffer corresponding to the serialized version of that context.
**BRUNO Baptista** 45:21 Okay, so right now we do something like that for the MDC context.
**Jonathan Halliday (IBM)** 45:27 Yes, yeah, it's conceptually very similar, yeah.
**BRUNO Baptista** 45:30 Yeah, so it's just another…
**Jonathan Halliday (IBM)** 45:32 Yeah, and in the case of virtual threads, it's the mount and unmount, where the It's not the JVM, it's standard library code. It's virtual thread.java.
has mountain on mount and it will have to do the same thing.
So I'm talking to OpenJDK about potentially baking that into the JDK.
If not, we use bike code manipulation to instrument mountain and mount to do this.
But yeah, Reactive will have to have similar hooks.
**BRUNO Baptista** 46:08 So when do you expect this to be something that we need to solve?
**Jonathan Halliday (IBM)** 46:16 Whenever you want users of Reactive, i.e. Quarkus, to be able to… Have Fred context that is exposed to.
an external profiler.
So it's up to you when you want to offer them that. You can sit and do nothing and wait for them to come to you and say, we want this to work, please. Or you can do it proactively, or I'll get around to it at some point.
**BRUNO Baptista** 46:42 Okay, okay, thanks for…
**Jonathan Halliday (IBM)** 46:45 I'm concentrating on solving this for virtual threads before I solve it for reactive, and the reason for that, quite simply, is that if we do want to upstream this into OpenJDK, I kind of want to do it before the next LTS, which gives me, at this point, about 9 months to… to get a proposal accepted into OpenJDK, which is doable, but I kind of want to look at the options and Have that conversation.
Not under so much time pressure.
But once I've done that, I'll switch my attention to reactive and try to come up with a plan for that as well.
**BRUNO Baptista** 47:23 Okay, thanks.
**Trask Stalnaker (Microsoft Corporation)** 47:29 All right. Any other topics?
Abdul, hey.
**Abdelrahman** 47:35 Hi. You catched my name directly.
Okay, so, I'm actually new, here, and I was looking to your, like, I want to contribute to Java, OpenTermetry, and, I was looking to good issues, good first issue, I couldn't find some. Could you recommend something first to contribute to?
**Jack Berg (Raintank, Inc. – Grafana Labs)** 48:01 So I think some of us will have different thoughts on this. So I'm one of the maintainers for OpenTelemetry Java, which is, like, we call it, like, the core repo, and then, you know, Trask and some others are maintainers on the instrumentation repo.
So… you know, on the core side of things, the project is relatively saturated. Like, the easy low-hanging fruit has been taken long ago, and there's, like, a load of people that are pointing their LLMs at the issues.
and just, like, you know, scanning for anything that is small and tractable and doable, and they just point their tokens at it. And so, you know, there's, like, kind of a race situation where people are just racing to submit PRs. So, you know, for the reason of the repository is mature, and people are pointing their LLMs at anything that comes up, there's not many good first issues left. I think that, like, that phase of open source development may be behind us.
That's at least my take on it.
There are areas to contribute.
they're just, like, they're more advanced, they're more bleeding edge, you kind of have to be engaged with what's happening at the spec. And, of course, we always need reviews for code as well. That's, like, something we consistently struggle with, is, like, keeping up with the influx of PRs, given the advent of LLMs, so…
**John Watson** 49:33 That's what I was gonna say, is this is actually something that I think a lot of people who are new to open source don't realize, is that the main thing that we need is people to do deep, thoughtful reviews.
Like, that is… that is the… the most scarce resource, is people's time to do deep, thoughtful reviews, not to contribute code changes.
**Abdelrahman** 49:56 Okay, is there…
**John Watson** 49:57 That's the place where you can provide the most value, is if you're a Java expert. Like, those deep code reviews are going to be the most helpful thing.
**Abdelrahman** 50:06 Okay, sounds, sounds fair.
Do you have any some kind of guides for first?
contributions, reviews, or whatever, or should I just, like, try to pick something that I can relate to and… Give some review, if it makes sense.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 50:25 So the repositories are big, and I think it's sort of overwhelming to try to, like, understand everything at once. So, like, the way that I think is a good way to like, explore, get up to speed on BEDS, is to try to go to a domain or an area that you're actively using or interested in.
And, you know, find PRs related to that if you're interested in reviewing, and, like, in the course of reviewing the PR, you know, explore the things that the PR touches, and that sort of naturally leads you around the repository to learn how different things work, and And, you know, the different conventions in the project, and you pick up on things that way, and after you've done that enough times, you start to have, like, a better, sort of, holistic understanding of the project. So… I don't know if there's a similar sort of recommendation in the instrumentation side of things, but yeah, my guidance would be like find an area that you're interested in, like, or are actively using.
**Abdelrahman** 51:31 Right, okay, yeah, sounds fun. Makes sense, thanks.
**Trask Stalnaker (Microsoft Corporation)** 51:35 Yeah, on the instrumentation side.
The… so what Jack said about, things that you are using, so, like, if you are using, like, the best kind of cases.
you're using OpenTelemetry, Java Agent, and you're… the app that you're monitoring uses RabbitMQ, And, you know, you look at how that telemetry is emitted, and, you know, you see issues there, and then, you know, you look at the semantic conventions for messaging, and kind of… Like it really it really helps if you have your own itch to scratch of like here, this is a problem that I'm running into.
That I can… Come at it from a user perspective.
**Abdelrahman** 52:31 Okay, yeah, I will keep that in mind.
Thanks.
**Trask Stalnaker (Microsoft Corporation)** 52:37 Yeah.
Thanks for joining.
**Abdelrahman** 52:39 Awesome.
**Trask Stalnaker (Microsoft Corporation)** 52:46 Alright, we're… Managed to use up most of our hour. Any… Last topics again? Last, last, last topics?
**Jay DeLuca (Raintank, Inc. – Grafana Labs)** 52:57 Trust that, that issue that I put under the V3 review. I don't know if we wanna…
**Trask Stalnaker (Microsoft Corporation)** 53:01 Oh, I missed it.
**Jay DeLuca (Raintank, Inc. – Grafana Labs)** 53:03 I don't want to go too deep into it, but it was just one that we had sitting around, around whether or not we should… keep this instrumentation enabled by default. I don't know that there's been any additional updates since the last time we discussed it, but… Yeah, just figured I'd bring it up again, in case we want to get it in last minute.
**Trask Stalnaker (Microsoft Corporation)** 53:25 For some reason, I removed it.
Why did I remove it?
Probably because I have no idea what to do about it.
Disable.
**Jay DeLuca (Raintank, Inc. – Grafana Labs)** 53:37 Yeah, and maybe we don't need to do anything, but…
**Trask Stalnaker (Microsoft Corporation)** 53:40 Yeah.
Well.
The only way I'm gonna remember to… look at it again, toggle it back into 3.0, and yeah.
I'll give it a thought after the… after the release.
**Jay DeLuca (Raintank, Inc. – Grafana Labs)** 53:58 Okay.
**Trask Stalnaker (Microsoft Corporation)** 54:00 Thanks.
All right.
Thanks everyone for joining.
Good to see you all.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 54:11 Alright, take care.
**Trask Stalnaker (Microsoft Corporation)** 54:12 Till next time.
**BRUNO Baptista** 54:14 Bye-bye.
