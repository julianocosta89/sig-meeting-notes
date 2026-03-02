SIG: Java SIG
Date: 2025-12-04
Duration: 49 minutes
============================================================

## Zoom Recording Transcript

**Jack Berg** 00:35 Bye.
**Trask Stalnaker** 01:06 Hey folks, welcome to December.
**Jack Berg** 01:14 Hello.
**Trask Stalnaker** 02:22 Alright… yes.
Release already tomorrow.
**Jack Berg** 02:29 That's right.
I don't have anything that is, you know, I've been trying to get in.
But, I guess, you know, I just wanted to see if there's anything that other people think is important to get in before this release.
**Trask Stalnaker** 02:55 Jonathan, the… Proto update, do you want that in?
**Jonathan Halliday (IBM)** 03:05 I don't think it's critical. I'm on vacation from tomorrow, so I'm not going to have time to do anything with it.
**Jack Berg** 03:13 Perfect. Now, also, it's a bit…
**Jonathan Halliday (IBM)** 03:15 nobody's worked on it yet, and, you know, profiling is having a lot of churn, so I don't think it's realistic to…
**Jack Berg** 03:21 Get those changes in by tomorrow.
**Trask Stalnaker** 03:40 All right.
Going once, going twice.
Ship it.
Cool, let's… I haven't done my… Reading for this, my homework.
So… and it kind of merges… into…
This topic, so why don't we…
talk really more about the concrete Java… Remote config, dynamic config, and then…
Yeah, I just wanted people, especially if you're interested in that topic, to follow this, and I will do my homework as well.
Cause I want to make sure that
were… well, not make sure, but I would like to…
use Java as potentially a proving ground, for… this…
Jack, I know I saw you had thoughts, and I…
Totally get the… there's… there's this weird overlap between this propo… between this and declarative config.
But I also… The thing that I like about this is it…
It answers the question, sort of, of… Which pieces of config?
Can be dynamically updated, which is…
**Jack Berg** 05:23 Exactly.
**Trask Stalnaker** 05:24 I think we've struggled with.
Because I think it's unrealistic to say that Everything should be dynamically updatable.
**Jack Berg** 05:36 Totally, yeah.
**Jack Shirazi** 05:37 And…
**Jack Berg** 05:38 You know, I… I guess the question in my head is… so, we've spent a long time coming up with a data model for how we express SDK concepts in a structured way.
And, what this could become.
if it's not, I think, carefully groomed, is yet another data model for expressing a subset of SDK concepts in a structured way.
And so, like.
I really like the aspect that they're going for, where they talk about, like, hey, we want to be able to do this discrete set of things. We want to be able to modify the sampler. We want to be able to, you know, change the log level. We want to be able to enable and disable, you know, instruments or scopes for traces, things like that.
And, like, I just…
I think we'll have to kind of walk a tightrope and figure out where there's overlap, how we can leverage the existing pieces, and where there's not, not trying to fit a square peg in a round hole.
**Jack Shirazi** 06:42 As it is, it's a fairly simple pipeline at the moment, so it's… I mean, I can fit it into my… the stuff that I'm doing very easily. It's a pipeline of read from sources, whether it's op-amp or a file or whatever, aggregate
the, whatever you've got, the JSON that you've got, I just aggregate it, and that disambiguates into various different things that you can change, and then just apply those changes. So that's…
That's the only… all that's specified in there is pretty much that pipeline and some example things… examples of things that will be changeable, or things that they think can be changeable.
And, like, you know, the simplest and most straightforward example is, sampling rate.
So yeah, that's like… there's a pipeline there which just says.
read it from, let's say, a file, read it from a local file, keep reading that file for every n seconds. If you see a change, pass it on to the aggregator, and then the aggregator passes it on to the provider, which then applies that to the sampling.
Their suggested mechanism is to, Just create a new sampler.
And install that, which is fine, and that works.
So, yeah, it… it all… it's all straightforward and, and…
Straight… straightforward to implement as it currently is.
**Jack Berg** 08:13 Yeah, so, like, one opportunity we could potentially have is, like, this example that you were using for the sampling rate. You know, I think sampling rate is a bit too narrow in vision. Like, I think what we want to do is be able to modify the sampler.
And, you know, because not all samplers will have a rate associated with them, especially if you look at this, like, this new composite sampler stuff that the sampling seg has been working on. They're rule-based, and, you know, you might want to do things like change the rules, add new conditions, new things like that. And so.
One thing you could… we could… one direction we could go is to leverage not the entire declarative config schema, but specific types within it. And we could say there's a command to say that you want to update your sampler to this.
And, you know, just leverage the existing, you know, type definition of what a sampler is in declarative config.
And, you know, the aggregator, the thing that's responsible for interpreting that and applying that would be, you know, responsible for, like, parsing that incoming description of what the sampler is.
Creating a sampler from it, and then applying it to the tracer provider.
**Jack Shirazi** 09:21 Yeah, and they've, dave… Responded to your comments there with that the…
that, like, that bit would be embedded within declarative config, rather than…
its own section, which makes perfect sense, because then you're talking about a very specific thing that can change, rather than the whole config that can change. And then, so you only just look at that node and the subnodes.
And you can see the differences there. And that works fine, yeah. That, so, yeah, that's, that, that's a…
perfectly… acceptable way to proceed.
**Jack Berg** 10:02 Yeah, and I'm really supportive of this. I… I… I…
I think it's nice that so many people are interested in this, that's great, and then also, like Trask said, the, you know, the attempt to…
to kind of tame the Wild West of, like, everything's reconfigurable, to know, we just want to support these… these specific, things as reconfigurable. That's…
That's great.
**Jack Shirazi** 10:27 I'm actually doing the tea.
**JP Jason Plumb** 10:29 And the resource is one of those things, right?
**Jack Berg** 10:33 I think that's Josh Shirath, who opened this P… this OTAP, is separately pursuing resource dynacism with entities, so.
**JP Jason Plumb** 10:43 Yeah.
**Jack Berg** 10:44 So not today.
**JP Jason Plumb** 10:47 Not this year.
**Jack Shirazi** 10:49 So the, the, the… that's, that's actually the previous link.
Rather than this one, because this one, this link is really separate.
And that was talking about…
You wanting a more generic approach to instrumentation that is dynamic, or that will be dynamic, and how to handle that.
So… yeah, so I've just put a concrete proposal in there. Just… it's not, like, that's not the final version, that's… as it's because it's draft, obviously. That's just somewhere to get us started,
Which is just…
a mechanism for calling back. There's for the… for the instrumentation to register that it can receive
Changes, and for something there to,
Look… look through changes, and then…
Pass that through to the instrumentation.
**Trask Stalnaker** 11:50 So, won't this…
**Jack Shirazi** 11:53 proportion.
**Trask Stalnaker** 11:54 proposal address that.
**Jack Shirazi** 11:57 This proposal.
**Trask Stalnaker** 11:59 would be that, I mean, we would need a…
Telemetry policy provider, or something for…
People to register for callbacks for that.
**Jack Shirazi** 12:12 Yeah, there's a… there's a missing piece.
Which is… If you plug this in as an extension, how does it tell the instrumentation in the agent?
what to do, so there needs to be something that connects those.
**Jack Berg** 12:30 Isn't that config provider, just extending config provider with some sort of callback or registration mechanism to say that you're interested in updates?
**Jack Shirazi** 12:37 That works perfectly if you have declarative config.
If you don't have declarative config, then… and you try to use the config provider, then the instrumentation says, okay, I'll use that, hang on, where's all my config?
And then it dies.
So…
**Trask Stalnaker** 12:59 There's actually,
Gregor is working on, we've discussed this in… around declared a config of the agent.
Synthesizing a declarative config model from the system properties.
So that we could essentially carry forward, and… because I would like instrumentation to not have to look at both
places.
**Jack Berg** 13:31 Right.
**Jack Shirazi** 13:33 And then instrumentation could start leaning into…
**Trask Stalnaker** 13:37 declarative config.
And… but it would still pick up, sort of, the old system properties if people haven't migrated yet.
**Jack Shirazi** 13:46 So the draft that I have there linked, it has an implementation, and it has, in comments all the things that you'd use for a config provider implementation.
Because at the moment, if I… if I use the config provider.
It would just break the instrumentation at initialization time, because the declarative config is not there. So then, if I declare a config provider.
then instrumentation says, okay, config provider is declared, that means there must be declarative config, I'll use that, and then it goes in and it has no actual config in there, and so it breaks at initialization, which is why, you can't actually use it at the moment.
**Jack Berg** 14:31 You can't use it at the moment, but in Gregor's proposal.
**Jack Shirazi** 14:33 Yeah.
**Jack Berg** 14:34 config provider would always be present, regardless of whether declarative config was used or system properties. And, you know, then we kind of gradually standardized instrumentation to use the config provider everywhere.
**Jack Shirazi** 14:46 And that would be fine, that… and that works, and, like, the… if you look at the other one, the callback registry, it would work both ways. It would work…
with one or the other, and failover, and yeah. So we could go with one now, and then add the other one, and it would be seamless, but yeah. So this is just, I guess, look at this, and…
Let's see whether we can move forward.
Before…
**Trask Stalnaker** 15:16 God.
**Jack Shirazi** 15:17 we wait for all the config provider to be available, unless that's going to come in January, which would be nice.
**Trask Stalnaker** 15:25 I… yeah, so I think we can… I'm okay with moving forward, sort of, in a non-standard
Path here,
**Jack Shirazi** 15:36 people fine.
**Trask Stalnaker** 15:37 Until we have, like, something standardized in the SDK. But I would like to…
**Jack Shirazi** 15:43 Lean into declarative config.
**Trask Stalnaker** 15:46 If… if we can make this just around declarative config, and at least very initially, you know, while we're kind of prototyping, that it only supports if you are using declarative config.
**Jack Shirazi** 16:02 in order to be…
**Trask Stalnaker** 16:03 And then hopefully we'll get that working with this… this kind of bridging.
**Jack Shirazi** 16:09 Well, if we do that, then it doesn't work until… the… the declarative config… config…
Replacement is available. So that's what you're saying, is that,
We need to wait for that, for this to work.
**Trask Stalnaker** 16:28 You could test it with declarative config.
But for it to work with system properties, for people who haven't migrated.
Which is, you know, we understand most people at this point. But it is,
I mean, there's active work, and you could help, contribute to that.
I think this is… I think this is it.
So it's not like it's something… it's not like a far-fetched… Idea.
**Jack Berg** 17:07 And just to kind of extend this idea further, so, you know, if we…
If we have this goal to eventually migrate all instrumentation to Consume Config Provider, and Config Provider will surface configuration from multiple sources, declarative Config or from
system properties. You know, that's… that's a long project, right? But what you're proposing, Jack, is… is net new, like, updating very specific configurations that are interested in consuming dynamic bits, things that are subject to change. And so, like.
you know, as long as Gregor's initial bridge is there to be able to access system properties through config provider, then as we're kind of migrating instrumentations to be able to have this dynamic bit to them, you know.
I guess what I'm trying to say is we don't have to solve that full project of, like, migrating everything to use config provider. It's just, like, on a case-by-case basis.
No, that doesn't work, so… No.
**Jack Shirazi** 18:06 If any instrumentation
if you create a… if we provide a config provider, then every instrumentation that is expecting a config provider will use that by default. And if it doesn't have the underlying config, it'll break.
So, it's not enough for us to just provide… I'm only looking at the methods instrumentation. It's not… if we just provided the methods instrumentation and put that into the config provider, every other instrumentation that then loads a config provider will break because it doesn't have the appropriate config for that instrumentation.
So once you've created a config provider, everything expects their config to be there.
**Jack Berg** 18:50 Right, right, right. But Gregor's solution is generic. Gregor's solution isn't going to, like, go property by property. It's just going to expose every single system property and environment variable through config provider in a standard way.
And so, like…
**Jack Shirazi** 19:03 But that would have to be mapped to the declarative config structure, because that's what the instrumentation that's using config provider is expecting. It's expecting that node path, it's not expecting the flat environment variable path.
**Jack Berg** 19:19 Oh, yeah.
**Jack Shirazi** 19:20 So, that has… that mapping, yeah.
**Jack Berg** 19:23 But it… we already did the mapping one way.
We already say that, like,
I guess I'm trying to think about what Gregor's doing differently than this, because we already say that you can read,
system properties through config provider.
**Jack Shirazi** 19:44 And we can just go… if you just go to the methods instrumentation, then you can see, because it's got these two alternative paths. It says, okay, if I've got a declarative config, I'll use that, and if I don't, and…
**Trask Stalnaker** 19:57 Oh, yeah, but we're gonna change… We're gonna change that.
**Jack Shirazi** 20:00 Yeah, no, but I'm saying, at the moment, if you provide a config provider, every instrumentation that does this has these two different routes, and they're expecting different structures in the two different routes. So if you look at the methods one, it's expecting a node structure.
And if it doesn't have that, if it's got the flat environment variable structure, then…
It does a different thing.
**Jack Berg** 20:22 Yeah, so when the structures diverge, then we have to do, like, a multiple paths thing. Like, when we, with declarative config, found a more optimal way to represent this information, I think you're right. There's no way other than to support both for the time being.
Or for some period of time. So.
**Jack Shirazi** 20:38 houses.
**Jack Berg** 20:39 Yeah.
**Jack Shirazi** 20:40 Yeah, so every instrumentation that has these two different paths.
Will, if you provide a config provider, will then break, unless the config has been mapped into that other structure.
And so you can't do it piecemeal. It's gotta be all or nothing.
**Lauri** 20:58 But the thing is that there aren't too many instrumentations that I have two paths.
Order?
**Jack Berg** 21:06 There shouldn't be, because there's not very many things that, you know, we're trying to express complex, structured information.
**Lauri** 21:12 I think there is the Methos instrumentation, Something with the rule-based sampler.
That doesn't have the system property thing at all.
and HTTP route customization.
Is there anything else?
**Trask Stalnaker** 21:29 we're planning to do… I mean, the goal here is to do that Across everything.
So, I mean, we… that is the goal here. Whether that goal succeeds, maybe you can chip into this PR and provide specific feedback about why you don't think it's going to work?
But… Ayy…
I mean, I'm hoping it works. I really want us… if we can get it to work, it will vastly accelerate our ability to push forward in declarative config.
Which is a huge win, because instrumentations today, there's no public API, library instrumentations especially, there's no public API for, accessing configuration, and so we have very limited configuration options.
**Jack Shirazi** 22:26 I mean, from what Laurie says, you know, if we've only got, like, 4 things that have these different paths, then it should be straightforward. Everything else will be using the flat environment variable value, and then it's really simple. Everything would be provided. So…
That would work, because that's a very constrained set of things to do.
**Lauri** 22:50 I'm not sure, like, how many there are, but I think there are too many. Gregor probably would know, because he worked on this, I think.
**Trask Stalnaker** 23:00 Yeah, I mean, let's push forward with this.
And see if we can get this to work, because if we can get this to work, that solves…
These issues, right?
And then… because what I… what I would love to see here is, the change listener
being, declarative config node.
Right? So that you could register for a whole sampler and get that whole rule-based sampler node.
to kind of Jack's earlier use case of, like, one of the things that would be great to be able to drive from remote configuration is the rule-based sampler.
Even the methods instrumentation,
The… we can model so much richer methods instrumentation by using declarative config.
That that also benefits, I think, versus trying… limiting it to the key-value pairs.
**Jack Shirazi** 24:09 Okay.
Can you just add Gregor's link in there?
**Trask Stalnaker** 24:22 Oh, yeah.
**Jack Shirazi** 24:22 Look at it.
**Trask Stalnaker** 24:23 Yeah, yeah.
Alright.
hey, all our topics are from JAX.
Logbridge.
**Jack Berg** 24:59 Yeah, okay, so…
I've been spending the last couple of days thinking about how to solve this problem. I would call it an oversight, which is, when you use the OpenTelemetry Logs Bridge API, which the community is trying to elevate to be a user-facing API to record events.
those… Records you record cannot participate in standard log
output. Log back, log for J2, joule.
And, you know, if you actually kind of look at the Java log ecosystem, I've been kind of studying this,
all the different APIs that exist, all the different SDKs or implementations that exist for those APIs, whatever you want to call them. OpenTelemetry is the odd man out. We are not being good participants in the ecosystem, because everybody else, you can bridge from any API to any SDK.
Except for OpenTelemetry. The only place OpenTelemetry logs can end up is over OTLP.
impractical, in, like, in practical terms. There's… you can… you can qualify that if you jump through, like, a lot of hoops. You can get them to appear in other places, but…
So what do I want to do about this?
I want to make it so that when you… I just want to do that. When you call the OpenTelemetry Log API, that you have a natural path for those logs to get, you know, exported via OTLP, but also that those logs participate in, you know, whatever, you know, logs implementation you have installed on your… in your application, whether that be LogBack or Log4J2. Those are the popular
setups.
And so, if you're not using the agent, how I think I… we ought to model this is with a log record processor, which bridges log records to SLF4J.
And so, if you can imagine the path, you know, you would record a log via the API, it would get processed by the SDK, the SDK would route that log to SLF4J, and then your SLF4J implementation would, you know, route that log to your console, or to files, or wherever.
That story, it's pretty well solved. I've got some good prototypes for it. There's some interesting things we have to do with cycle detection and prevention, but I think they're all tractable problems.
The other story is when the agent is installed.
So,
if you can imagine, you know, you've got the Java agent installed, and the agent itself has usages of the OpenTelemetry Logs API to emit events, like, you know, from its instrumentation that it publishes.
But then, you know, when the agent is installed, we also have this pattern of, like, hey, get the agent open telemetry instance via Global OpenTelemetry, and use that for your own custom application instrumentation.
And so, you know, ostensibly, we want to allow users to be able to get that Global OpenTelemetry instance and record logs and events, and have those logs get routed to the SDK that's installed by the agent, and also, you know, appear in their standard console logs with Log4J2 or whatever.
And so, if you think about what's happening here, we have to do something similar to what we do with this property, OTel Java Agent Logging application.
So, you know, this is the tooling that we have internal to the agent that tries to take internal logs and route them to the application's SLF4J instance.
So that they can, you know, just be, you know, appear in the application's standard logging configuration, whatever they've configured.
So I've been looking into that a little bit. There's some kind of gotchas I have to solve, but one of the key things that is special about OpenTelemetry Log API records versus the Java agent's internal logs is that the OpenTelemetry Log API relies heavily on structure.
And, yeah, the current…
you know, tooling in the Java agent to route to SLF or J uses SLF4J1, which is just, like, log string messages. So, like, what I'm thinking is try to constrain this to SLF or J2, where they introduced
a fluent API for structured logs, and say, like, hey, if you want this feature, you have to use SLF or J2 in your application.
John.
**John Watson** 29:35 Yeah, this is a little bit of a side question, but when you've got this working.
Should we consider changing our logging API usage inside the SDK to use our own logging API rather than Juul?
**Jack Berg** 29:51 Yeah, this is a question on the front of my mind, like, how can we recommend other people use this if we're not using it ourselves?
**John Watson** 29:56 Exactly.
**Jack Berg** 29:58 And, there… you know how it's a real pain in the ass to, get…
do internal metrics within the SDK because of the initialization ordering issues.
It's basically that problem.
Like, Juul is super convenient because it relies on… and all the logging APIs rely heavily on globals. Like, global logger, Logger Factory, Log Manager, whatever you want to call it, these global static methods that you get… use to get a logger at, like, your class's initialization time. And with OpenTelemetry, we kind of…
we kind of avoid globals, right? We use instance-level stuff, and so, we kind of have
The design of the, the, the…
tracer provider and meter provider, which leaked into logger provider, has made it difficult for us to use our own stuff, I would say. But maybe there's a route.
So, I guess the reason I wanted to bring this up here is I wanted to poke the instrumentation
maintainers' and approvers' brains to see if, like, hey, does this strike you as reasonable? Do you know of any, like, you know, big hurdles I'm gonna come across with this agent-specific story?
**Trask Stalnaker** 31:37 So I, I, I mean,
Makes sense what you're proposing of using…
Because we do have that sort of reverse bridge.
Already. The reverse bridge is… weird in the Java agent.
In general.
**Jack Berg** 31:55 Yeah, it's a different kind of instrumentation. It doesn't work like the others.
**Trask Stalnaker** 31:59 Yeah.
But it makes sense. I don't…
I mean, I don't have a good feeling how many people are using That… And therefore, how…
Comfortable we'd be with… Restricting it to SLF or J2.
**Jack Berg** 32:25 I would actually propose, keep the SLF for J1 requirement for the general Java agent internal logs.
And then, for this part where we try to bridge.
OpenTelemetry log API logs back to SLF for J… restrict that to SLF for J2.
So, like, you know, it's basically, like, if you want this new feature, which doesn't exist right now, then we're gonna have this additional requirement.
And I don't know if it's possible to express that, but that's, like, the idea in my head.
**Trask Stalnaker** 32:59 And would we be able to…
use our log? Would we be able to replace our… internal, SLF4J usage with the log…
Hotel Log API, then?
**Jack Berg** 33:19 I think you would,
I think it'd be a lot more realistic for the agent to use the OpenTelemetry Log API internally than it is for the SDK to use the log API internally, because the agent doesn't suffer from this initialization ordering problem nearly as much as the SDK does.
There are… there are agent logs that, like, precede any SDK being initialized, so those ones are sort of like a special case.
But any logging that happens after SDK initialization should be pretty straightforward.
Hmm.
But, you know, that's obviously a big project, so, I wouldn't try to…
Do that all at once, by any means.
**Lauri** 34:07 The thing is that the agent currently uses the Cello UT Logging API.
**Jack Berg** 34:12 who only has an API.
Yep.
**Lauri** 34:15 It rewrites the usages of the API to something completely different.
**Jack Berg** 34:20 Yeah.
**Lauri** 34:22 So, you're proposing that we use the OTEL logging API and do the same, rewrite the usages to something completely different?
As we do now.
**Trask Stalnaker** 34:33 I think he's saying we would replace Juul with our log API.
**Jack Berg** 34:40 That's, like, a separate goal, like, right? That's about, like, you know, using the stuff that we recommend to users, internally, but my main goal, like, you know, this is kind of like scope creep, actually, like, figuring out what to do about Java agent internal logs, but my main goal is just to make sure that log records recorded via the API
are routed to whatever log implementation, whatever log SDK your application has.
Okay. That's what I want more than anything else.
**Trask Stalnaker** 35:08 setting aside… yeah, because I think that… that started to blow my brain a little bit, trying to think of using our log API for our internal… replacing our logging usages with our log API.
**Jack Berg** 35:23 Yeah, it's a nice pie-in-the-sky idea.
**Trask Stalnaker** 35:26 Like, yeah, I got confused… I got quickly confused trying to follow those cycles.
**Jack Berg** 35:33 I mean, it would be nice, especially if we make the API more ergonomic, to do, structured and, you know, event logging as a first-class thing.
you know, if the agent could do that internally, we sort of lead the way for this vision of what logging ought to be. Always structured and always with an event name identifier.
**Trask Stalnaker** 35:55 And you could define which logs you want to go to console, and which logs you want to go to OTLP.
Which should be something that people would want anyways.
**Jack Shirazi** 36:06 So, in our distribution, we've, we've installed it so that…
the logging goes to Log4J, just using the standard Logging provider capability.
And…
I guess my only feedback would be make sure that we don't get two logs for, like, one through this mechanism and one through that mechanism.
Oh yeah, that's… fridge look.
**Jack Berg** 36:34 Yeah, initial prototypes when I was working on this, I got, like, stack overflows and stuff. Cycle detection is the main problem that you have to cope with, but I think there's fairly simple techniques to do that. I'm trying to propagate… use our context propagation mechanisms to detect and, you know, stop cycles.
And that works most of the time until you get into async logging situations. And so, what I have to figure out is, like,
you know, what other mechanisms I can use to send that signal so that logs don't get duplicated. And, you know, I think you can embed… encode the same information that we do in context in things like map diagnostic context.
Or attributes, and, you know, then look for that type of signal, or magic bite, if you will, or marker, whatever you want to call it, and break the cycle.
So…
**Trask Stalnaker** 37:29 Good luck
We're… we discussed your comment in the log sig yesterday, because Robert had proposed closing the cycle detection spec PR,
And I was like, no, Jack volunteered to, to prototype that, so let's…
**Jack Berg** 37:49 Wait, what did I pro- Is this a long time ago?
**Trask Stalnaker** 37:54 No, no, no, very recently.
Let's see, call enter, Jack.
Is this? Wait, one of these… Maybe…
Maybe Robert didn't create it?
This one. Oh, you created the issue. Yes.
This one.
Event APIs should loop back to log frameworks without cycles.
**Jack Berg** 38:44 Yeah, this is essentially what I'm trying to solve, but, like, in two contexts, with and without the agent, so,
You know, one thing that was just, like, as we're talking about this, one thing, I was considering is we have this field in the protos called log flags, and log flags is, like, it's a 64-bit integer, where, you know, the bits are divided, and I think 8 of them are dedicated to trace context.
And, we could just steal a couple of bits of those flags as standard representations to indicate whether the SDK has already seen a log.
Right? That's essentially what I'm doing to prevent cycles, is I, like, I'm encoding some information in context that allows me to detect that a cycle is happening and then stop it.
And so, if you can encode information in, like, you know, an integer, then, you know, you can just choose how to propagate that integer to make it sure it's, like, available. And you can do that via context propagation, or MDC, or attributes, or whatever is most convenient for you, whatever tools you have available.
So, these are the ideas in my head.
I don't know if I can get the whole community to agree on, like, dedicating a couple of bits of these log flags.
Oh, it's not in here, it's in the proto, though.
**Trask Stalnaker** 40:09 Oh, okay.
**Jack Berg** 40:14 Yeah, I…
**Trask Stalnaker** 40:18 And it's different than trace flags?
**Jack Berg** 40:20 Yes.
Search flags in here.
**Trask Stalnaker** 40:31 Flag record… flags…
**Jack Berg** 40:37 Yeah, so the first 8 bits are for trace flags.
Then there's a bunch of other bits reserved for… it's 30… 32 bits, not 64, sorry.
**Trask Stalnaker** 40:50 Plenty of bits.
**Jack Berg** 40:51 Plenty of bets for me to steal a few.
**Trask Stalnaker** 40:57 Alright, well, yes, good luck, look forward to seeing
Are you planning to send… what… what would be, like.
prototype, or actual, like, log record pro… I guess…
**Jack Berg** 41:13 So…
It's kind of complicated to, like… there's a lot of moving pieces in this. You have to do work to the agent, you have to do work to the SDK, you have to provide, like, you know, custom processors, and then you have to demonstrate this in working applications to, like, show that it, you know, nothing's gonna break. And so, I'm thinking of creating sort of a…
like, a document or, like, a meta-issue that, like, links together PRs across a variety of repos and shows, sort of, all the things involved, and tries to talk about it coherently.
Go ahead.
**Trask Stalnaker** 41:46 Cool.
**Jack Berg** 41:46 Lots of coordination.
**Trask Stalnaker** 41:53 All right.
Well, we have hit the end of our agenda. Anybody have anything else they want to chat about?
**John Watson** 42:03 I just wanted to throw out some kudos to everybody. I'm working with our internal observability team.
Helping them, or advising them on how to get instrumentation into HBase and other Apache big data stuff that Cloudera helps maintain.
And they… I was… my first organization was, well, just, like, plug in the agent at runtime and see what happens. That's the first thing you should try, always.
And they're like, oh, I don't know, we don't know how to do that. I'm like, just, it's very easy, here it is. And they tried it, and they're like, oh, it just worked, cool! And, so they're… it's very impressive.
And we are…
**Trask Stalnaker** 42:44 Magic technology, like code instrumentation.
**John Watson** 42:47 Yeah, and I am going to hopefully…
start advising them on getting native instrumentation built into those Apache… that Apache stuff.
Awesome. Right now, they're only… we're only gonna get, like…
the… whatever… whatever JMX metrics they produce right now, if you turn them on, and whatever standard client libraries they happen to use. Although a bunch of that stuff uses Thrift, which I don't think we have instrumentation for, so…
Yeah, I'm going to hopefully, hopefully, fingers crossed, start helping advise them, at least, on how to get all that instrumentation to Apache Projects Native.
**Jack Berg** 43:27 That's great feedback.
John, just something caught my ear. Thrift is, like a message encoding technology. Is it also… like, it's just binary encoded for messages? Is it also, like, like a PubSub system?
**JP Jason Plumb** 43:44 RPC…
**John Watson** 43:45 Yeah, it's RPC.
**Jack Berg** 43:46 C.
**John Watson** 43:46 I see, yeah, and I think there's a… it uses its own transport, so it's not going to be necessarily going over… it can… I think you can do Thrift over HTTP,
But I don't think… I think by default, it uses its own transport, so…
**Jack Berg** 43:59 So the word's overloaded, it's like, it's, it's like, you know, used to both refer to, like, a message definition and encoding, and also an RPC framework built on top of that.
**John Watson** 44:09 Yes.
**Jack Berg** 44:11 like, it'd be like gRPC and Protobuff, but in Thrift's case, both are called Thrift.
**John Watson** 44:16 Yeah.
**Jack Berg** 44:17 As far as I understand. I'm not an expert, but as far as I understand, yeah.
**Lauri** 44:21 There should be, open tracing implementation for tracing thrift.
And I believe it's fairly simple.
As far as… like, somebody from Splunk, I think, ported it to OpenTelemetry in, like, a day or so.
**John Watson** 44:39 Yeah, right now we're more concerned with getting, like, request metrics.
request response metrics, and that sort of stuff. But yes, I think you're right.
**Trask Stalnaker** 44:53 Alright, on that note… Good luck on the release tomorrow.
**Jack Berg** 45:00 Yeah, hoping I don't get rate limited.
**Trask Stalnaker** 45:03 I know… oh…
**Jack Berg** 45:05 I just wish they had some docs that indicated, like, you know, hinted at what the heck is going on with them, like, what are the limits?
**Lauri** 45:14 the meters work. Has anybody tried contacting support?
**JP Jason Plumb** 45:17 I'm tempted to open a ticket on it, because it's…
**Trask Stalnaker** 45:21 Do it.
**JP Jason Plumb** 45:22 Yeah…
**Lauri** 45:23 We could use something else to publish the snapshots.
**John Watson** 45:27 I think we did get a successful snapshot release. We did.
**Trask Stalnaker** 45:30 Last night, it worked. Yeah, it closed the, the issue, I saw that.
**Lauri** 45:37 like, the snapshots and actual releases, I think they are handled by completely different repositories.
So, the actual release might not be affected by it at all.
**Jack Berg** 45:48 Yeah, exactly. They might have completely different meters for snapshots versus Dot.
**Lauri** 45:56 And if it is, then you're welcome to port over the release stuff from the instrumentation repository. Oh, God.
**Jack Berg** 46:06 What is that a reference to?
**Lauri** 46:09 Like, we have a custom hackery that does the release a bit differently.
We don't, like,
It doesn't upload each artifact separately, but it does, like, it creates a bundle, and it's uploaded as a single file.
**Jack Berg** 46:22 Oh, okay. So there is no way it will get very limited.
**Trask Stalnaker** 46:26 We, we broke, we broke, when they migrated, the instrumentation was too big, and so we broke it. We broke them, or they broke us.
And so Lori created this magic RE where it bundles it all together, uses the underlying REST API for, Sonotype, and…
Pushes it all at once.
**Jack Berg** 46:50 So, okay, so maybe you don't run into the limit for individual requests, but maybe you run into the limits for, like, maximum size of a single request? Have you reached that limit yet?
**Lauri** 47:01 No. Seems to be okay. The REST API is actually the one they want to be using for…
they want people to use to make releases to Central, but the unfortunate thing is that it doesn't have an official plugin from,
from either Cradle or Sonata.
**Jack Berg** 47:18 and…
**Lauri** 47:19 And, Trust didn't want to use, like, a plugin from some random dude, so we had to do it ourselves.
**Jack Berg** 47:27 Yeah.
Ugh.
**Lauri** 47:30 Luckily, it wasn't too difficult.
**Jack Berg** 47:34 problems with being one of the most complicated repos, Java repos on the internet.
**Lauri** 47:42 Well, I think it isn't actually that bad, like, there is plenty of huge repositories out there.
**Jack Berg** 47:51 How much you do it, List?
**Trask Stalnaker** 47:53 It's got, like, 500 modules or something. It's… it's getting kind of big.
**Jack Berg** 48:00 Kind of big.
**JP Jason Plumb** 48:02 Too big, one might say?
**Jack Berg** 48:04 Don't start.
**John Watson** 48:06 You just gotta make 500 individual little sub-repositories, right?
**JP Jason Plumb** 48:10 Let's start.
**Trask Stalnaker** 48:10 Oh, that'll be so much more… so much easier, yeah.
**JP Jason Plumb** 48:13 Maybe we start with two.
**Lauri** 48:17 Yeah, and let's have all those repositories versioned separately and released separately.
**Trask Stalnaker** 48:23 And update all of… every time we have to update or fix the, the dependencies and…
Yeah, oh my goodness.
**Jack Berg** 48:33 Trask, you'll just do that.
**John Watson** 48:34 AI open.
**Trask Stalnaker** 48:36 I mean, we still have to click all the buttons.
**Jack Berg** 48:39 Hell.
**Trask Stalnaker** 48:46 Alright.
Enjoy your… enjoy the 12 minutes back.
**Jack Berg** 48:52 Alright, take care, everyone.
**JP Jason Plumb** 48:53 Thanks, everyone.
