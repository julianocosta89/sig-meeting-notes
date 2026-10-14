SIG: GenAI SIG
Date: 2026-10-13
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

Liudmila Molkova 00:06:04 Hello, hi everybody.
Any volunteers to run the call?
Trask Stalnaker (Microsoft Corporation) 00:06:19 Pick me, pick me.
Liudmila Molkova 00:06:22 Okay, go for it, no?
Why did you give me a false hug?
Okay, We are… here, please add your name to the agenda, I think it has some part that we discussed.
in the call at 7.30 Pacific.
One of the highlights… I think the only thing we got to is that Kubernetes… there's a new Kubernetes SIG that is going to work on model serving signals.
Do we have anybody? It doesn't seem so. So, folks came to the previous call and shared their… Doc, the design, they would like to, Unify the semantic conventions and telemetry for the model serving.
And we've been discussing whether this convention's where they should leave, who is interested, the Alibaba folks are interested, there are some people from Google who are interested, they work on LLMD, which is nearby, but not exactly the same. And the important part we've been discussing, that maybe The development should at least start in this repo.
It's vendor neutral, they have a Slack channel, they would have a meeting, so this could be a good forum to design and iterate fast on the first version, and if there is an interest in, like, bringing the serving wholesale to OpenTelemetry Semantic Conventions GenEI, we can discuss it then, but maybe it's a… this is a good place to start.
And I think the people from Kubernetes are going to maybe post on the Slack channel, but anyone who's interested.
I think, we didn't talk about the next steps, but there is already a Slack channel message from one of the people working in it, from Omer, I think.
Comment there, create issues here, it would be… Awesome.
Okay, so… Moving.
On to this call. I think this is where we guide first, the 7.30.
Let's see. Let's start with Ankit. It seems you're here. Are you here?
Ankit 00:09:05 Yeah, sorry, I had to join from my phone. I was driving for an appointment.
So, I might… So, of… So on this PR for the, real-time… Model inference, I've addressed, Probably all the comments so far.
So, would appreciate, reviews… And if any… comments are unresolved and need some input, I would definitely work on those.
I didn't check if there were any new comments yesterday night, so…
Liudmila Molkova 00:09:46 Yeah, no worries. I posted some comments. I think the only big one I have… well, I think I have two. I don't completely understand the child and sibling patterns, but Maybe, most importantly, We sometimes are not able to capture the two calls, and even parts.
And I think we need to find a way the way doesn't have to be implemented in this PR, but we need to know how we are planning to do this with this model.
If you're on the phone, it probably doesn't make sense for me to share or type here. But like, if you can take a look at the comments and share your thoughts, that would be great.
Ankit 00:10:35 Okay, yeah, sounds good. Definitely, we'll share. So.
So the only open or the comment that's open is about, like, if the tool calls cannot be represented.
Or cannot be captured as a part of the inference call? Is that the… Major open question, or…
Liudmila Molkova 00:10:56 Yeah, and it's related to the other one is like you have two patterns for the child to call and sibling to call.
And I think this, this is… .
Maybe I understand that there are the need for two patterns, but I don't think the child or sibling is something we can totally control.
Somewhat arbitrary in which context tool is executed.
Ankit 00:11:24 I see.
I see. Okay.
Got it, okay. So, I think if I remember correctly, for, GPT models, I think the… When a tool has to be executed, it does, and that, I'll be able to make the first… I think, probably I need to actually get those details, but then I remember, like, it follows the same pattern where, like, in French colleges.
kind of ended, and there are events to figure out, where, okay, model says now we need to execute a tool call. And I think for Gemini.
I forgot whether it was 2.5 or 3. There were no, like, events that could help identify that boundary.
Yes, sir.
Liudmila Molkova 00:12:16 For the… there are two cases. In one case, we know that there is, like, there is one inference call for all Yeah. Full executions, and for Gemini 3, and for… Openai, it's… The same as regular inference.
And if it is the way we model it, we kind of need to know where to stick to Parts into.
Which we don't today.
Ankit 00:12:48 Oh, I see, I see, I see, I see. Okay. So in the case where the tool calls cannot be identified separately, then where do we put the tool parts in a way, right? Yeah. Got it, got it. Okay, okay, that makes sense.
Okay, yeah, I'll definitely address that. I have thoughts on that, yeah.
Liudmila Molkova 00:13:06 Oh.
Thank you.
So, moving on… The next topic is Dylan.
Schema for opt-in, opt-out.
Dylan Russell 00:13:23 Yes.
So, this is sort of what I came up with.
Which is to have some global set.
Of attributes, like a global config for opting into attributes.
So you would list the attributes you want to opt into.
Across, like, all span types, all events.
And then, if you want… You could have the more fine-grained thing.
And you list which attributes you want to opt into for, like, a particular span or event.
And that would override the global.
and I was thinking we could get really carried away, and… You could opt… make all attributes, like, opt-outable.
And, same thing, you can make All operations, like, opt outable.
And we just decide which ones are… I think right now, all operations are… On by default, and you have to… There's no way to opt out.
But… Yeah, that's… That's what I was thinking. Let me know your thoughts.
Liudmila Molkova 00:14:58 I'm thinking maybe we… Like, there is a non-controversial part.
And that's what we kind of… need… Very, like, soon. It's the part of the stabilization, which is environment variable.
And then there is the configuration options that we probably will spend some time on.
Let me separate them into two different PRs, and then the first one would go in pretty quick, and then we can spend time and design a good thing for the configuration.
Dylan Russell 00:15:36 Okay, yeah, that sounds good.
Liudmila Molkova 00:15:46 Yeah, for this one… I need to read through and think about it, but if people have thoughts, that would be great.
Aaron Abbott (Google LLC) 00:15:57 Yeah, one question, Dylan, you said it's global, but it looks like it's in a GenAI namespace.
And.
I wonder if it would be.
like, opt-in is a standard thing in SemConf, I wonder if it would apply across, like, subgroups of SemConf.
Dylan Russell 00:16:20 I don't know if that makes sense… I mean, it could… could make sense if you… Because we're really just talking about a set of, like, operations and a set of attributes.
But that… Yeah, that… Would probably be a bigger discussion.
I was thinking, yeah, GenAI-specific section.
Yeah, that's interesting.
Trask Stalnaker (Microsoft Corporation) 00:16:47 There's a few, existing ways to sort of opt in and out of things.
There's… Tracer enabled, logger enabled.
So if we're giving, you know, tracer names and logger names for the events.
Declarative configuration already has a way to enable and disable based on those names.
There's also, the… For spans, there's the configurable sampler.
Which… I think it's in declarative config now, because it's in the spec now, where it's… you can define rules, like, you can say.
Don't, you know, sample out this specific span with this specific attribute.
Nikhil Chitlur Navakiran (Microsoft Corporation) 00:17:46 Mmm…
Trask Stalnaker (Microsoft Corporation) 00:17:48 And then, for event names, I don't… we really should… I have a general way to kind of sample in and out event names.
But I don't think we do at this point, but that would potentially be, like, a standard log processor that you would add into the… SDK configuration, as opposed to Like, the more of that stuff we can get under the SDK configuration, reuse those pieces.
And then… Only things that we really need in the… not trying to do something generalized like that, too generalized under the instrumentation.
Node.
Probably would be easier to move forward.
Liudmila Molkova 00:18:46 Here we kind of want individual attributes.
And if I heard… if I understand Aaron's proposal that maybe there should be a generic way in semantic conventions to enable opt-in attributes one by one, but I kind of feel it's… Too general, and usually they come and, like, it's a feature gate, but that… combines multiple things.
Rather than, like, just enable the attribute, like a Boolean.
For one thing, and… I think this is a GenAI-specific configuration.
And how I would probably approach it is, like, what configurability do we need?
Put in content, like, a global flag, like, with environment variable, I think, like, just general gate, all or nothing.
Makes sense, because we have it so far, and we didn't get a lot of complaints about it, actually.
Maybe the other part is a binary content.
Then there is an uploading that we have.
And, like, if we list all the options that we want configurable, Then it would simplify, How we… what is the design?
Trask Stalnaker (Microsoft Corporation) 00:20:09 Yeah, it's definitely easier if we can… Design it in terms of, like, feature flags.
Nikhil Chitlur Navakiran (Microsoft Corporation) 00:20:19 Mmm.
Trask Stalnaker (Microsoft Corporation) 00:20:19 Boolean.
Kind of the way that environment variable.
Is… if we need… it's okay if we really do need attribute level, like, named things, but that's… we don't really have… I don't think we have any precedent for that.
So, it opens a lot of questions.
Dylan Russell 00:20:47 Okay.
Aaron Abbott (Google LLC) 00:20:53 Just so I understand, it sounds like we're leaning we're saying it's just, like, instrumentation level config, or would it be across all of GenAI? Like, per instrumentation, or all of GenAI?
Trask Stalnaker (Microsoft Corporation) 00:21:06 It just, it should be GenAI, like, that's the right place to put it, under General GenAI, I think.
So that it applies across all instrumentations.
Dylan Russell 00:21:23 Yeah, I think that makes sense, because we're… we have a GenAI-specific, like, SEMCOMS.
Which should be adopted by, like, every instrumentation.
Trask Stalnaker (Microsoft Corporation) 00:21:35 Yeah, and it matches what we have for, like, HTTP and.
I think we have… I forget if we have a database there or not, but we have a couple, SEMCON things under General today.
But, mostly I was just suggesting if, the Boolean, like, flat, like, feature flag kind of approach, if that works for us.
is… aligns… more with the… it doesn't open all those questions like Aaron was getting at of, like, hey, this sounds cool, can we do this for all of the instrumentations and be able to opt in and out of individual attributes?
Dylan Russell 00:22:30 That's kind of what we have now, with just… you can either opt in or out to, like, all… all… Content capture attributes.
Liudmila Molkova 00:22:41 Yeah, And, like, we should keep it.
It should be still easy, right?
Dylan Russell 00:22:47 Yeah.
Okay.
Liudmila Molkova 00:22:53 So, next steps, we split, and maybe we will talk about what exactly that we want to be configurable.
Done.
The specific options.
Dylan Russell 00:23:06 Okay, sounds good.
Liudmila Molkova 00:23:07 Thank you.
Anything else before we move on to the next topic?
Okay, is Hanchi on the call?
Hanchi Wang 00:23:17 Yes, I am. Hey.
Hello, Anne. And nice to meet a few folks in this, setup.
And, yeah, so, I guess this is, like, a question slash discussion on The intention behind removing the agent ID, From the internal spans of agent invocation, right? And… This actually has caused some problems on my team, which is Microsoft Foundry, because of how we execute agents.
The way we do that is, you know, like, we try to group the spans.
and traces based on a common agent ID, and the… Sometimes, like… There is only server-side expense.
Right, like, there's no client, because, like, the client may not be instrumented at all, so the request kind of starts from service. And all of those spans that we generate from the service side are internal spats, right? And now, with the agent ID being removed, again, like, there's not a way we can group all the server-side spans and traces for a given agent. And that kind of, Break some of our assumption.
So yeah, I guess concretely, the proposal is to add it back, if possible, or even add it back as optional.
Liudmila Molkova 00:25:04 I see. So I think this is the part of the context I was missing. So if I understand correctly, this is the server side agent and it has an ID. This is the ID of the hosted agent being executed.
Hanchi Wang 00:25:17 Yes, yes.
Liudmila Molkova 00:25:19 And what do we have for this today?
Is, an entity. It's the thing you said, not on the spans, but on the… Resources, like, it's something that's attached to all spends in the process.
And it is, I think, called Hanchi.
Aaron, do you remember where is it?
Aaron Abbott (Google LLC) 00:25:47 Yeah, should be in that file, entities.
Liudmila Molkova 00:25:50 Yeah.
Aaron Abbott (Google LLC) 00:25:50 Oh, yeah.
Liudmila Molkova 00:25:51 So, it's called Main Agent ID. So you would set it on the process level, or, like, at some higher level place.
And, in the OTLP traffic, it looks like there is the scope that contains this main agent ID, and then there are multiple spans that are reported under the scope.
And.
This means that if you have sub-agents in the same process.
Or you call somebody else, like, another…
Hanchi Wang 00:26:25 you.
Liudmila Molkova 00:26:25 Remote agent.
There, this is where you would have agent ID, which is the ID of that agent, not your agent.
Not the whole.
Hanchi Wang 00:26:34 most.
Liudmila Molkova 00:26:35 I'm kind of curious if… This model works for you instead of having span attribute.
Hanchi Wang 00:26:45 Yeah, I think this is useful in the scenario where That, you know, there is a… you know, like, the manage layer, like, in Foundry, it's, like, kind of the hosted agent scenario, like, kind of… customer register an agent and give it an ID, right? But underneath that, there's, like, another agent framework.
Like, in execution, right? I think this is helpful in that case. But the scenario I was talking about is actually not a case. The scenario I was talking about is that the agent runtime and agent execution is purely managed by Foundry.
Right, so you create an agent, And… then the runtime… is, like, isolated for that agent, and only, kind of, being executed for that agent ID.
And there's no, kind of, main agent versus sub-agent concept in that… in that setup.
Liudmila Molkova 00:27:56 Is it fair to say that then there is just one main agent?
Hanchi Wang 00:27:59 Yeah, there's only one agent, like, throughout end-to-end.
Liudmila Molkova 00:28:05 Yeah.
Trask Stalnaker (Microsoft Corporation) 00:28:06 Still fits… yeah, it still sounds like it fits the semantic definition of a main agent.
There's just not sub-agents in that case, but it's still… a process-wide Agent.
Hanchi Wang 00:28:27 So you believe, like, the idea of main agent still makes sense, even if there's no subagents? That's what you mean?
Aaron Abbott (Google LLC) 00:28:35 Yeah.
Hanchi Wang 00:28:36 So then we will have this inconsistency, right?
Again, like, it may work in other scenarios, but, like, for this case that… there's, like, only one agent, no subagent, then on the client side, it's called Agent ID, but on the server side, it's called May agent ID…
Liudmila Molkova 00:29:02 Yeah, because they are slightly… different.
On the client, you are executed in some.
Context, probably another agent.
And you're talking about the remote agent you're calling.
And on the server, or in this isolated environment, you know that You are the agent that executes operations.
Hanchi Wang 00:29:40 Why?
See, okay… Hmm.
Okay…
Ankit 00:29:50 And, is the main agent a resource attribute now?
Super, or…
Liudmila Molkova 00:29:56 Yeah.
Ankit 00:29:58 Yeah, oh, I see.
Daniel Rolles 00:30:05 and.
Liudmila Molkova 00:30:05 Danielle.
Daniel Rolles 00:30:06 Hanchi, are you making the point that Maine is a relative statement?
Hanchi Wang 00:30:12 Yes, yeah.
Daniel Rolles 00:30:14 That's exactly where I'm coming from as well.
Hanchi Wang 00:30:16 Yeah.
Daniel Rolles 00:30:17 Mate, you need to know what Maine is.
Before you can state that there's a main.
Hanchi Wang 00:30:22 Yeah.
Daniel Rolles 00:30:24 Which, in your point, I think the point you're making is it's relative and fractal, right? You don't know in advance what's going to be main, because you may spawn multiple, or may… Yeah.
Is that your point? Did I understand correctly?
Hanchi Wang 00:30:38 Yeah, that's a great clarification, thank you for that.
Liudmila Molkova 00:30:42 In this case, main means main for this process, for this isolated environment.
Trask Stalnaker (Microsoft Corporation) 00:30:53 In… yeah, so it's true, in some cases you don't know, but in some cases you do know. And in those cases.
Stamping the main agent.
entity.
provides that context.
For that whole process, including any in-process subagents and tool calls and, inference calls that it makes.
Hanchi Wang 00:31:24 I see. So is this a breaking change, by the way? Like, I remember Agent ID was there.
In internal agent invocation spans, and then it was removed, right?
So… I guess kind of the breaking change part is something that kind of, Came me as a surprise.
Liudmila Molkova 00:31:49 It is a breaking change, though it's a development, stability spec. So, unfortunately, breaking changes are expected at this point, and we have stabilization effort.
Where we try to, like, I think this would be in the scope to get it stable, and then there won't be breaking changes for a foreseeable future.
Trask Stalnaker (Microsoft Corporation) 00:32:13 Outside of major version bumps to the specs.
Hanchi Wang 00:32:16 I see. But what's the herd policy?
Liudmila Molkova 00:32:18 Perceivable so far.
Hanchi Wang 00:32:19 Yeah, sure. But what's the hurt if we have both main agents and keep the original agent ID?
And in the case of, that main agent and subagent do make sense, to the scenario, then those are applicable. But, like, in case there's, like, no main versus subagent, there's just only one agent, throughout the… process, then, like, the original GenAI.agent ID can still be used.
Is that a possibility?
Trask Stalnaker (Microsoft Corporation) 00:32:55 So, I think if there's… if there's only one agent used throughout the process, then we really want people to stamp main agent on that, if they know, because that's, like.
the best information that you can have, and as a resource attribute, that gets automatically stamped on all metrics, bands, events, across all the, you know, inference calls, tool calls, everything in that process. So that's, like, a hugely useful piece of information for users, consumers of the telemetry data.
So that's kind of, like, priority one. If that fits your scenario, that's, like.
a real… a big benefit to your users to use that to stamp Main Agent on it.
Felix Becker (Anthropic) 00:33:43 But also, this only works if… Since it's a resource attribute, if they're, like, if main agent and resource or process or service map one-to-one, right?
Like, if you have a multi-tenant… Managed agent product. If, like, fundamentally, we can't set that.
Whereas the… Agent ID said Hanchi is talking about our disband attributes, so we could use them.
Trask Stalnaker (Microsoft Corporation) 00:34:14 Right, so I guess that's a question to Hanchi, is this a multi-tenant environment.
Hanchi Wang 00:34:20 It.
Trask Stalnaker (Microsoft Corporation) 00:34:21 where.
Hanchi Wang 00:34:22 It is.
Trask Stalnaker (Microsoft Corporation) 00:34:22 So you have multiple tenants in a single process?
Hanchi Wang 00:34:27 It's yeah, a shared service. Excuse me.
Trask Stalnaker (Microsoft Corporation) 00:34:32 Shared service or a shared actual process?
process boundary, OS process boundary.
Is what's important here.
Hanchi Wang 00:34:43 So… let's say… excuse me. So, let's say, like, I can have, maybe 3 agents registered to my service, right? And I can invoke each of them, and each of them will be executed in An isolated process.
Trask Stalnaker (Microsoft Corporation) 00:35:05 Right.
Felix Becker (Anthropic) 00:35:06 Visa's attributes map one-to-one with the service.
Where's the…
Trask Stalnaker (Microsoft Corporation) 00:35:12 process.
Felix Becker (Anthropic) 00:35:17 But if it's just a service emitting.
At the, like, service boundary, you can still have multiple, like, multiple resources.
Like, different sets of resource attributes?
Trask Stalnaker (Microsoft Corporation) 00:35:34 Yeah, like service ID, if you have a cluster, your service is everything in your service ID.
is per… Your host site, your host name, there's lots of things that can be different across the process boundaries.
Felix Becker (Anthropic) 00:35:54 So can each span have a different… Like resource attribute.
Liudmila Molkova 00:36:00 No, it's per process, so everything emitted within this process would share resource attributes.
All the time.
Felix Becker (Anthropic) 00:36:10 What I'm confused by is that process seems like an implementation detail, right? Like whether a service spawns multiple processes or multiple threads or.
Hanchi Wang 00:36:20 Yeah, exactly.
Felix Becker (Anthropic) 00:36:21 So, like, why does the process boundary… why should that matter?
Liudmila Molkova 00:36:28 It's actually the implementation detail of OpenTelemetry historical that we are trying to change, but essentially, this is the limits of SDK configuration.
So since SDK is essentially a single ton in, like, the client applications. then it unfortunately has the resources as a single ton. Eventually, it would change.
Felix Becker (Anthropic) 00:36:49 And if a service emits OTEL without using the OTEL SDKs?
Liudmila Molkova 00:36:56 Dan, it's an interesting question.
Aaron Abbott (Google LLC) 00:36:59 Yeah, I mean, you can do whatever you want, right?
like, if you look at the collector, there's receivers that set process resource attributes, and the collector's a single process. So, like, you could do host metrics and have per-process metrics, so you can kind of do whatever you want in the data model. I think What Trask is saying about service, he means, like, across a horizontally scaled service.
The resource has to have some.
Like, distinguishing attributes, so there's… instance IDs and stuff like that.
It's not… It's not just a single horizontal service has one resource.
Felix Becker (Anthropic) 00:37:32 So, just to act up, historically, OTEL defined resource attributes as, like, mapping one-to-one processes, but in the GenAI conventions.
We now say, well.
it's not strictly the process, it should just map one-to-one with agents. Do you understand that?
correctly.
Liudmila Molkova 00:37:55 We would like to…
Felix Becker (Anthropic) 00:37:56 It could be one with processes too, but doesn't have to be.
Trask Stalnaker (Microsoft Corporation) 00:38:01 Currently, it's one-to-one with process, just let's say that. The future, the… if you've heard of the entity, like, work in the specification, the goal there is to be able to have resource attributes that are more fine-grained than process.
Specifically to support things like multi-tenancy, where you have an entity, you know, a session, something that is more fine-grained than a process. So that's… The direction, but today we only have… Think of it as process.
Felix Becker (Anthropic) 00:38:45 Okay.
Liudmila Molkova 00:38:48 Having said that, if I were to design a hosted agent.
telemetry.
in multi-tenant environment.
Would there be an agent ID?
Probably yes. Would it be a main agent ID? Probably no, because… or maybe both.
Because.
If I'm a hosted agent, and I know my ID, and it's static, and I'm the… I… And the GenAI agent attributes represent who am I.
Or, like, what is the scope of the agent executing this? Then it should be an agent ID.
And in a truly multi-tenant environment.
it makes sense to have an agent ID, but maybe it shouldn't be an internal span, maybe it should be some refinement of internal span?
We're… a new flavor. We've been discussing, do we need a server, GenAI execution, or not?
Maybe we should have hosted agent.
Specialized, somehow.
Trask Stalnaker (Microsoft Corporation) 00:39:59 Yeah, that's a whole, yeah, worth discussing, the internal versus, and I think that's part of the problem here, is that That invoke agent internal span is what we've modeled at Where Hanchi and other… some other people. have wanted, like, an invoke agent server span.
to represent this better and agent ID could make more sense on that server span.
Hanchi Wang 00:40:34 Hmm.
Oh, I see. So I saw the…
Ankit 00:40:38 So what?
Hanchi Wang 00:40:39 to solve that. That sounds like no.
Ankit 00:40:43 Yeah, so I want to mention, I think, bring up one more point, so… So right now for any, like the agent building framework, right? If they emit any spans, those are invoked into internal spans, right?
So… here, like, the scenario is, okay, I created an agent, right? And then I… Took that code, and now I'm running it behind a service, right?
So would that behavior change entirely for that code to emit now a different kind of spam, which is not an internal spam, now it's a server spam, right?
Or should there be another service plan before it, service limits, right?
That adds to the complexity for me. Please.
Does that make sense? Like, I guess we are talking about, like, a new version of the new cadence plan, but then, like.
Would that mean that the invocation span that's being emitted by the instrumenting library changes based on where it's running?
Interesting.
Does it make sense?
Liudmila Molkova 00:41:55 Yeah, I mean, it's, like, so there are a couple of questions, so if we have it, different flavor.
So I think this is what you're asking, what kind should it be, and if server… Then, what about… The outer layer, the transport layer.
Ankit 00:42:30 Yeah, and the other thing is, like, it's the same instrumenting library, which is emitting that, whether it's a server versus internal span, right? And it would matter where it's running, right? If I'm running it behind a service, would it emit a different type of span versus when I'm running it locally on one machine, right?
Trask Stalnaker (Microsoft Corporation) 00:42:52 I think that's why we have kind of been stuck on this, and the internal is the one that we've implemented, and that… Matches, like, the open source frameworks that we emit the… emit that span from.
Those are internal spans. They're… they are… frameworks, libraries that you call, you wrap them with some other kind of Service handling.
But where things… Where a… potentially a server span, a real server span, could make sense is if you are a hosted service yourself, and you are implementing that whole, agent.
Service and invocation, and you know, then, that that is a server span, you know that you can add a few more guarantees there than, like, an ID, agent ID, which… We haven't found that these… frameworks have something called an agent ID, which is why we removed it.
Right. There wasn't any instrumentation, any, you know.
Ankit 00:44:10 straight.
Trask Stalnaker (Microsoft Corporation) 00:44:11 That's using that.
Hanchi Wang 00:44:12 Hmm.
Ankit 00:44:13 Okay.
Liudmila Molkova 00:44:14 It was actually even worse that agent ID, there are some instrumentation that have a notion of agent ID, but it's a, like, hash address of the object, essentially. And then it appears on metrics, and it creates crazy problems for metrics there.
Hanchi Wang 00:44:34 I think for this one, then you should not only look at the agent framework.
Right? Like, because this is also important to the managed agents scenario, whereas, like, the orchestrator is not an agent framework, it's not an SDK, it's story-side logic.
Right. And that's where, like, we, at least for Foundry, we still have this notion of agent ID, and that's actually pretty critical to group all the relevant service size, spans, and traces together.
Aaron Abbott (Google LLC) 00:45:08 Yeah.
I mean, we have in Google as well, and I think that that was where I was coming from with the main agent proposal, like… The goal is to solve that, and… just for, like, resource… like, it doesn't… it doesn't matter if it's server or internal. Resource is included on everything. It's on the metrics, it's on spans, so… I think, like, please take a look at it and let me know if it doesn't work, but I think given the multi-tenancy model in OTEL is kind of immature right now, and I know, like, there's lots of work, I think Java just merged a prototype for entities, or just released it, actually. Maybe we can, like, make sure the data model works, and then… if there's an issue with the SDK, implementation, we can… Figure out how to make it a little easier.
Trask Stalnaker (Microsoft Corporation) 00:45:58 Well, and we have… I mean, if multi-tenancy is an active concern.
We have Ludmilla's PR proposal to add main agent as span attributes, I believe.
Liudmila Molkova 00:46:15 Right.
Trask Stalnaker (Microsoft Corporation) 00:46:18 And so that could be the path forward.
in the short term, if… again, that's only if multi-tenancy inside of a single process, which it sounds like isn't the case for Hanchi.
And so I… I think the main agent.
ID… is… Going to actually give your customers better telemetry.
Then… David Ensign, P.D: even because that will be on all of their telemetry for that process, because it's a resource attribute. That will give them better telemetry than only stamping agent ID on the invoke agent.
Span.
Hanchi Wang 00:47:06 But yeah, maybe I'm not following, but like in this case, again, like by managed agents, my definition is that customer don't even write code.
Right? It's all, like, logic that we manage on behalf of customers. Right, like, we pick, we use the model customer picked, we use their system prompt, we use the tools they have chosen, and, like, kind of orchestrate everything together.
Right, so… I don't see any benefit for this specific scenario to leverage the main IDE, that, you know, the agent ID cannot give us already.
Because, you know, all the logic is controlled by us on the service side, right? We can just… stamp all the… Spans and metrics, like, like, whatever we want.
Liudmila Molkova 00:48:01 The benefit is that from semantic conventions perspective, from OpenTelemetry perspective, this is the guidance we give, and we expect and hope that there will be a lot of products that would leverage it out of the box.
And by adding Agent ID to the internal spans, we create more harm, and we create more ways to represent the same data. So if it's technically possible for you, to emit main agent ID, that would be our recommendation.
Felix Becker (Anthropic) 00:48:32 I mean, is… is there… are there plans to resolve the, like, multi-tenancy problem, or, like, the process coupling? Because I… I don't see how this can be, like, you know, adopted in… many of those cases, so I said it feels a bit weird to say, like, oh, this is, you know, the recommended way to do this when it doesn't work for many cases.
Trask Stalnaker (Microsoft Corporation) 00:48:55 So that, that's the PR that I, Lidmilla's PR of adding the proposed… we could add main agent.
As a span attribute.
Right, and that solves the… essentially, that's just… that would be, the exact same thing as doing agent ID. You would do main agent ID, main agent name on that server span.
And you could do that.
Daniel Rolles 00:49:23 The PI does it.
Don't know whether the PR does it, but then you need to state your assumption that you know in advance what Maine is.
Absolutely. That's the key, but I think that's where we're getting hung up, and what we're not clear here is the use case scenarios.
Right? Because I think we're talking at cross-purposes of what the use case scenarios are.
Felix Becker (Anthropic) 00:49:43 Sorry, note in advance.
Daniel Rolles 00:49:44 But.
Felix Becker (Anthropic) 00:49:44 What?
Daniel Rolles 00:49:45 that you know what Maine is.
Felix Becker (Anthropic) 00:49:48 That's the assumption.
Daniel Rolles 00:49:49 So.
Felix Becker (Anthropic) 00:49:50 What… at which point?
Daniel Rolles 00:49:51 be…
Felix Becker (Anthropic) 00:49:51 to know it.
Daniel Rolles 00:49:52 In advance of the… span being… now, that's a really good challenging question, let me get it clear. And Hachi, please jump in here and help me out, but I think it's when the process… and sorry, guys, I'm brand new, so let me just… give me… give me a chance here. When the process is being… Seeded, you know which is going to be the main agent.
Felix Becker (Anthropic) 00:50:17 Is the is your worry basically when it's a recursive?
Called the Fractal.
Daniel Rolles 00:50:22 Exactly.
Felix Becker (Anthropic) 00:50:23 instead.
Daniel Rolles 00:50:23 personal.
Felix Becker (Anthropic) 00:50:24 I don't know anymore if they're a Mainer.
Daniel Rolles 00:50:25 Exactly. Even now, we…
Felix Becker (Anthropic) 00:50:27 Parents could, like, the actual main could pass down, like, you are not main, right?
Daniel Rolles 00:50:32 Then you got parent trace ID. Exactly. So if that's how we're doing it, then fine. But that's where I am with Hachi.
You still have to assume that you know what mine is.
Hatching the use case.
Felix Becker (Anthropic) 00:50:45 Distributed systems case, it's like hard.
Daniel Rolles 00:50:48 Correct.
Felix Becker (Anthropic) 00:50:49 pass that.
Daniel Rolles 00:50:50 Correct. And sorry, and I'm actually here from the Open Lineage community. We've had exactly the same recursive problem over there.
Right? Exactly the same, because you don't always know what your main lineage job is.
So we've had to straight away this one. Sorry, again, I'm new to this community, sorry for jumping in so much on my first meeting, but it's literally an equivalent problem we've had over there. So we can't assume which is the first lineage, which job kicks off the lineage, because it could cascade and be recursive down.
Felix Becker (Anthropic) 00:51:20 So, just to clarify…
Trask Stalnaker (Microsoft Corporation) 00:51:21 If I… if I can, the… the main agent in this, in Semantic Conventions GenAI is main agent for a single process. It's not for a distributed trace, right? So it is a local main agent.
Daniel Rolles 00:51:38 And that's where you put the constraint when you place… Sorry, Felix, I was just… when you place that constraint, that's the assumption that state… that flows, that says you now know what main is.
Trask Stalnaker (Microsoft Corporation) 00:51:51 Yeah, and you might, in a distributed trace, you might have multiple main agents, right? And that's okay with us.
I mean, obviously, there's future problems to solve, but we're.
Daniel Rolles 00:52:02 Exactly.
Trask Stalnaker (Microsoft Corporation) 00:52:03 problems we can.
Daniel Rolles 00:52:04 incremental.
Trask Stalnaker (Microsoft Corporation) 00:52:05 Mentally.
Daniel Rolles 00:52:05 And that's when I jumped to the analytics side. It's like, no, no, no, keep the agent ID. And then the analytics side needs to determine when on your collector side, the analytics side needs to determine which one was made. Right. And that's where, yeah, again, we've ended up.
Felix Becker (Anthropic) 00:52:19 to give.
Daniel Rolles 00:52:19 Sorry, this is my first meeting and I feel like I'm being too vocal, so my apologies.
Felix Becker (Anthropic) 00:52:24 In like cloud managed agents, for example, you have both Like, sub-agent system inside of one session, so that just, like, that one session can spawn out different.
Hanchi Wang 00:52:39 something.
Felix Becker (Anthropic) 00:52:39 It's not, like, literally restricted to only one model context, but you can also have That session, just, like, call a completely separate agent.
And.
Daniel Rolles 00:52:52 In the IQI situation, exactly.
Felix Becker (Anthropic) 00:52:53 Trying to basically always model those things as new main agents, even when it calls out to another, like, main agent, basically.
And if you don't have that layer of.
Which one was mine?
Huh?
Daniel Rolles 00:53:09 That's… that's… which one was mine?
Liudmila Molkova 00:53:11 The main is relative.
Daniel Rolles 00:53:14 In that case, exactly.
Liudmila Molkova 00:53:16 Textual. There are multiple top-level agents that participate in this operation, and by the hierarchy, you can establish who was the first one. Let's try to close on this topic. We have 10 minutes left, and a lot of other things on the agenda, but Aaron, go ahead.
Aaron Abbott (Google LLC) 00:53:35 No, I was gonna say the same thing as you, Ludmila, like, I think this is a distributed trace. If there's multiple main agents, they show it. Like, there's no… there's no decision to make, it's just kind of… Part of the data model that you choose.
Hanchi Wang 00:53:47 That's a good example, Felix, brought up, right? Like, there can be an agent, and then spin up, like, subagents, right? And then for the subagent spans, does… then does that make sense to… for the subagent to have both the main agent ID as well as its own agent ID?
Liudmila Molkova 00:54:07 Oh, yes, absolutely. So if you're calling a remote agent, you address it by its ID.
Hanchi Wang 00:54:12 So this is not the remote yet, like, you know, main agent spin up a local sub-agent scenario.
Liudmila Molkova 00:54:18 I understand. It's the problem is that at some point, it can start calling a remote agent, and we need to design telemetry in the way that you can stem both. Who am I calling, and who am I?
Hanchi Wang 00:54:30 Right.
Liudmila Molkova 00:54:31 Or, who tells me?
Felix Becker (Anthropic) 00:54:32 to distinguish them, you can make one the main agent and make the other the, like, not main agents. If you can't distinguish them, you can just make all of them main agents. There's nothing that stops you from doing that.
Aaron Abbott (Google LLC) 00:54:45 I think the key thing is that when you design this hierarchy or whatever, you — logically have chosen a main agent. So, like, you guys are saying, oh, it's a subagent within the same managed agent. Like, you've kind of made a decision already, so it's sort of up to you.
I think… If they're like different main agents, then make them different main agents. If not.
It should… it should work.
Hanchi Wang 00:55:11 Yeah, I think I'm arguing that there will be a scenario that both main agent and specific agent ID are applicable, right? And I'm saying that we should make both of them.
Possible, or allowed, for invoke agent spans.
Trask Stalnaker (Microsoft Corporation) 00:55:25 So, if I can interrupt here, Hanchi, why don't you set up some time with me internally, and we can chat more. I can catch you up to speed on all the prior discussions, because we've discussed this a lot in this SIG before.
And, we can give some time back to the… a whole 10 minutes for the rest of the meeting, Ludmilla.
Hanchi Wang 00:55:46 Okay, okay, so sounds good. Thank you.
Liudmila Molkova 00:55:51 Yeah. Erin, you still have your hand raised. Is it still or?
Aaron Abbott (Google LLC) 00:55:58 No, I lowered it, sorry.
Liudmila Molkova 00:56:00 Yeah. Moving on to the next topic, Pam, do you want to talk about World Privacy Forum?
Pam Dixon 00:56:07 Hi, I'm Pam Dixon. Yes, I'm founder and executive director of the World Privacy Forum. I work on the, I do a lot of work on complex governance, AI and quantum primarily. In regards to my question here, right now I'm deeply involved in the ITUT SG17 process, which is multi-agentic identity.
And it's really messy. And at some point, your conversation really needs to go over there, and that conversation really needs to come to this group, because the different definitions and articulations of the configuration are emerging.
I think, for what it's worth, I really like the main agent idea. I think it works in all sorts of ways. I wasn't, aware that, agent ID for invoke spans was gone, but that's fine. Main agent works just great. So my question is this.
In regards to creating a register that can, eventually, be audited, by comparing traces, etc. We're very interested in seeing if it's possible to add a field to the invoke agent span.
Which would facilitate, figuring out, or somehow articulating, who man… or what the mandate… what the mandate was. Who mandated this agent? Who or what? This is not the same as authorization. Most people immediately assume this is authorization. It's not authorization, it's just a record.
of what either did or did not mandate. It's either here's the mandate or no, there's no mandate.
So this really facilitates post-auditing. So that's the question. I don't know where this belongs. I know it belongs somewhere in this conversation, but I'm trying to figure out where and how I could discuss this calmly with people and try to figure out this problem. It's really thorny.
On the ID side.
That's it.
Neil Yashinsky 00:58:14 Yeah.
I'm happy to take first bat at this, Trask and Ludmila, if you want, just because I'm not a, you know, I'm not… welcome, Daniel, first. Everybody who's new to OTEL and Pam, if it's your first meeting, you know, welcome. As well. Oh, great. So, and I don't want to speak for Ludmila or Trask, but I think I've heard variations of this question before, and My sense is that you kind of, reached an interesting intersection, and so the way that, they think the semantic conventions are designed is, like.
And.
finding the answers to the most pressing questions, in a kind of prioritized fashion, and I think you bring up some really interesting ones, and I think.
there's… there's overlap between what you want and what I think they're working towards, but also not overlap, if I may say politely. And so just trying to find the right way to… join the process, and… and learn about, like, the priorities firsthand, like you're doing right now, I think is the best way to have that first start, and I don't think there's an easy, you know, one single answer to any of the questions you ask. They're good, but I think they're a little bit, you know, will take some time to.
answer properly, and the answer oftentimes might just be, like, your involvement will drive the things that you're most interested in doing, and so coming here is, right, the best place to do that, and then, like, I personally have been trying to connect the most pressing issues on the project boards with where I think my you know, my concerns intersect, and then go from there. Trask was that… Liudmila, did I… Aaron, did I do a pretty good job of, like, as a kind of outsider person trying to just, like, you know.
Pam Dixon 00:59:59 weird.
Neil Yashinsky 00:59:59 here trying to Without having to say, like, the official ruling, you know, right? Because I don't think there's… that's the thing where… Is that right, Trask? I see smiles, but no talking or validation.
Liudmila Molkova 01:00:12 I think you you you think that we own the road map. We don't. You folks own the road map. We are, curating it and help make trying to help make it happen.
But yeah, I think, Neil, you should drive this meeting.
Neil Yashinsky 01:00:25 Oh, gosh. Okay, everybody, put your seatbelts on, make sure all, you know, your items are put away, your trays, etc.
Trask Stalnaker (Microsoft Corporation) 01:00:38 Pam, yeah, this is a tricky… this is a tricky issue, and it's been… raised, Before, and it is sort of… I think we sort of see it as orthogonal.
to GenAI in terms of.
We do have the, like, user… I mean, it applies to anything, like, who's running something, what authority authorization process has.
So… I… I'm a little… I don't know whether it's better to take this, you know, also to explore within The General Semantic Convention SIG meeting?
Are there… like, if… when you look at the general semantic conventions, there's the user.namespace.
Is that what you want?
And one thing we've discussed in the past in the general semantic conventions is this idea of embedding namespaces. So, like, under GenAI, we could embed the user namespace, because, for example, on a single span, you might have You know, there might be multiple concepts of a user. Right.
So, that's… yeah.
But nobody is really pushing this forward right now.
Pam Dixon 01:02:21 Yeah, I think your comment is very precise. There can be multiple mandates sitting on this.
That makes it very sticky and difficult to manage. I acknowledge that freely. It's not an authorization. It's a record of what was the actual mandate.
Or if it existed. It's basically almost a yes or a no, and what it was.
Neil Yashinsky 01:02:52 I feel like you're… I kind of feel like, in a way, Pam, your question is connected to Daniel's before, and it's like, it's a question of, what's the word I'm looking for? Provenance, around instantiation.
And I think what we ran into, and again, Daniel, come in and correct me if I'm wrong, but Trask, I think what we… it's like, the perspective right now is, like, of the main, of the one single thing, we have to kind of get the original spawning agent correct.
And how it works. And so getting to how subagents work is.
Pam Dixon 01:03:26 If I may, if I may, I think you're kind of misunderstanding what I'm saying. I probably totally.
Neil Yashinsky 01:03:31 Yeah.
Pam Dixon 01:03:32 Yeah, this is really different than what you're describing. This is… this is really a registry question, more than anything else. I'm in provenance. Yeah, what's on the registry regarding provenance? It doesn't confer provenance at all, and so it's just really… just a record of what is, or is not. That's it. But there are… it… the record can be complex, so it raises the issues that Trask was talking about. So, I think, so my question is still, what's the best way forward? We're at a minute over or so. So, is it possible to open an issue, or is there someplace I can lurk and discuss this?
Liudmila Molkova 01:04:20 It would be great if you… oh.
Yeah, it would be great if you could open an issue and explain what the mandate is. If it's something defined somewhere, there is, it's the spec, or there is some external thing we can be grounded in if it's widely used.
What's the properties of this mandate? How… in which cases we should capture it, and things like this? Like, what are the user… scenarios that… around it, and that would tremendously help to understand, because currently, I was going to bring up identity, but you kind of said it's not identity, like the AAM. It's not, so I'm now lost what is it, and how to scope it to something I understand.
Pam Dixon 01:05:07 Yeah, so this sounds good. I will, I'll be… Ludmila, I'll be in touch with you to… to open an issue, and then just… we'll hope to have, robust discussions, and I'll… I'll try to make calls.
I'm overseas a lot, and I'll just try to figure out how to do it. Thank you very much. I'll pull myself off camera now. Thank you.
Liudmila Molkova 01:05:32 Thank you.
And we are at time. Thank you all. Please come to the next call if I didn't get to your topic and I'm sorry. It was a great discussion though. Thanks.
Neil Yashinsky 01:05:43 Yeah.
Trask Stalnaker (Microsoft Corporation) 01:05:44 Thanks, everyone.
Neil Yashinsky 01:05:45 Thanks Ludmila, Trask, Aaron, et cetera. Felix.
Trask Stalnaker (Microsoft Corporation) 01:05:47 I.
Neil Yashinsky 01:05:48 Bye.
