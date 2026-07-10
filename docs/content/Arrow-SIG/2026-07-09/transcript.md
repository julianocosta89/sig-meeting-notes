SIG: Arrow SIG
Date: 2026-07-09
Duration: 53 minutes
============================================================

## Zoom Recording Transcript

**Laurent Querel** 00:56 Hello!
**kennedybushnell** 01:00 Welcome back.
**Laurent Querel** 01:03 Thank you.
Okay.
So, I don't know exactly what happened with this, zoom,
**Joshua MacDonald** 01:18 Hi, I've been working on the Zoom problem. I don't exactly know what triggered the fix at this moment. Oh, yeah. Hi, Trask.
**Trask Stalnaker** 01:28 Hey.
When did you all get it?
I think it is.
**Joshua MacDonald** 01:32 I think the moment you logged out is when I maybe worked.
I'm not sure.
**Trask Stalnaker** 01:40 Okay. So, yeah, yeah, yeah, so… You know.
Sorry, like, so that is confusing, because Ted is not your GC liaison, so… but he's the one I want to fix this, because he created the packaging SIG meeting wrong.
But I, as your GC liaison, will bug him and get this fixed before two weeks from now. Apologies.
**Joshua MacDonald** 02:09 Thanks, Trav.
**Laurent Querel** 02:10 All right, thanks.
**Trask Stalnaker** 02:12 See ya.
**Laurent Querel** 02:14 Thank you.
Okay. So… I started to, to create some some agenda.
Feel free to add any new topic.
And, maybe we can start with, the classic triage. I like in the process that we follow. Usually we start with triage. I'd like also to add a very short Time on what has been marked as fail.
So we know we have an automatic process when something is not updated for a long time.
if I remember well, it's marked 1st state, and then it's closed after a period of time.
I don't remember the exact duration of this period.
But, I think, especially in the issue. There are some very old issues that are still interesting to keep, in my opinion.
So, I'd like to add into the… The submitting, a short, review of what has been marked stale recently.
So we have a chance to… To remove the tag, if needed.
Okay, so sure… Okay, can you see my screen?
**Joshua MacDonald** 03:44 Yes. Yes.
**Laurent Querel** 03:46 Right. So let's start with the sale list that is not yet closed.
So we have this one documentation round of grammar choice and supported grammar.
Drew, do you have any, Idea on what it is exactly. There is no description at all. I'm not sure, so… Yeah.
**drewrelmas** 04:14 I'll take this one. It was originally, you know, with our KQL parser, I just wanted to throw together a README showing what grammar choices are available.
I'll take care of this, don't worry. I'll mark it not stale, and I'll try and get.
**Laurent Querel** 04:30 Okay, okay, great.
So for that, that's, that's it for this, week, on this topic. So then the, the second aspect, is to review the, the last, Not accepted, GitHub issue, so let's start. So we have few, this week.
upgrade object store. So this one is probably a no-brainer.
Same code and some permanent migration, I guess. Okay, standardized and adapt, extend live check to validate. So, I know that… I think CGO is working on that, right?
**drewrelmas** 05:10 So Laurent, this is specifically a sub-issue on the metric naming convention and instrumentation issue, which we've been discussing offline.
data point level attributes. Yeah.
**Laurent Querel** 05:26 Okay.
**drewrelmas** 05:26 So I think we we like that's a whole topic to be discussed as a whole. I just had started creating some sub issues under it based on what work I thought needed to be done. So I don't know if we need to do this right now. We should discuss the topic as a whole.
**Laurent Querel** 05:42 Yes, I agree.
Mitchell?
**drewrelmas** 05:46 There's a there's a few like that, so.
**Laurent Querel** 05:48 Yeah, like this one, I guess also. Yes. So for maybe because maybe some of the people in the audience are not necessarily aware of the work that… We we do in this space. So for for background.
We a long time ago we used the open telemetry client SDK Rust. There was version, obviously.
For internal telemetry.
For safe instrumentation. And, we, we decided that.
It could be better for the project basically to to reuse the pipeline system that we have also for internal telemetry.
But we… Give us a lot of advantage. First, we will be able to emit the internal telemetry.
also in, you know, TAP protocol, which is not supported, obviously, by the client SDK.
And we could also exercise all the.
The processor exporter that we are implementing, which is, In my opinion, also like dogfooding for us, making sure that what we deliver is also used by yourself and it's working well.
So that was the decision behind that. So we have already this ITS in place.
But only for logs.
And and right now for for metrics, it's still using the client SDK plus some custom stuff.
So, drew and myself, we decided to focus on that in the next week and finalize this work.
And there are multiple things related to that. So first, st connecting the internal metric delivery system to this ITS, plus a few other things.
Any, additional stuff to add to that, Drew or Joshua?
**drewrelmas** 07:51 The main — and I just linked it in the chat as well. I have a hard — I have to drop today, unfortunately, at 8:25. So I don't think we'll get to this full topic today. We can discuss it next Tuesday. But what I will say is that — I just linked a parent issue 3300 in the chat, which has a lot more of the context. Basically, examining the variety of per signal instrumentation we have today that diverges from each other. And so the goal with this work is to make sure we have more uniform metric emission across all of our different components.
Furthermore, we want to simplify the call sites for all these metrics, so instead of component authors needing to you know, declare separate metric sets based on signal. We should have a single metric that accepts, a, for example, signal attribute as a data point attribute, emit a single metric, and then, downstream, if needed, we should be able to split and partition into per-signal metrics, if required, by the operator.
**Laurent Querel** 09:06 Yes.
What about maybe, just, change a little bit the agenda?
let you present what we discussed yesterday.
Before you, you have to leave.
**drewrelmas** 09:21 Sure. I have, yeah.
**Laurent Querel** 09:23 So I can… Okay, yeah, I think that that that would be enough. So I'll let you share the screen, or you you want me to share the screen.
**drewrelmas** 09:32 If you could share the screen.
**Laurent Querel** 09:35 Can you remind me which,
**Joshua MacDonald** 09:38 30,000.
**drewrelmas** 09:39 is… Issue or sorry. Pr. 3, 3, 6, 9.
**Laurent Querel** 09:47 3, 3, 6, 9.
**drewrelmas** 09:49 Yes.
**Laurent Querel** 09:50 Dot.
What will be useful? I don't know if you had time to read the last comment I sent yesterday.
**drewrelmas** 09:58 I did, yes, and I'm thinking through it.
The entry point to this work is, what we talk about here. If you freeze right there on my… on that large comment… or, oh yeah, we can look at the PR description. PR description works.
**Laurent Querel** 10:14 Yeah, yeah.
**drewrelmas** 10:15 So… Basically, this is an attempt at, like, a draft… this is a draft of a solution to address those wildly divergent per-component metrics that we saw in 3300.
so… The collector in the Go OpenTelemetry collector has standard internal telemetry today that is often per signal, meaning you have export log records, exporter metric data points at exporter spans.
However, they do have a perhaps idealized new RFC doc, which states that they want to prefer Having a single metric with a signal attribute instead.
So, this is the default that I would like to move Otel Arrow to.
Initially, in the first draft of this PR, after I discussed with Joshua, we were thinking maybe we would give operators a choice of if they want to emit telemetry at a… Agnostic level, meaning a single metric with a signal attribute, or at a granular level, meaning multiple Metrics, per signal.
And I was trying to think of a way we could have a single call site for both of these. And it's just a policy on the telemetry side, which one is omitted.
After some more conversation with, Laurent and Josh.
I think we can get away with only emitting one format, as long as our metrics internal telemetry pipeline has the ability to split them back out again, if that's what an operator requires.
So in this way, we are both, by default, moving to the direction that OpenTelemetry Collector wants to go.
But also demonstrating the benefit of our internal metric pipeline.
to produce the legacy shape, if that's what a use case requires.
I had an offline call with Laurent, he left some great feedback on this PR. This is basically talking about how the instrumentation works. We will declare, today, just as another piece of background.
We don't support any data point level attributes. Everything in metrics world is either on the resource or the instrumentation scope.
So, here we're talking about data point level attributes that are either static, meaning they're known at compile time, or Dynamic, meaning they're seated at runtime.
So the classic example is the durable buffer metrics we have.
Which we have eight individual metrics depending on per signal and outcome, meaning dropped or expired. So in this proposal, we're able to get down to from eight metrics down to one metric with data point attributes for outcome and signal.
So this simplifies a lot of the code we have.
and I think it will be… it'll help us maintain a more consistent attribute set across the whole codebase. For example, telemetry signal I would envision that enum being used.
all the way across every component, instead of each component having its own, enums. So… That's the gist of it.
I would pause there, Laurent, or Josh, do you want to add anything?
**Laurent Querel** 13:59 Yeah, I can, I can explain.
**drewrelmas** 14:02 And I…
**Laurent Querel** 14:02 Yeah.
**drewrelmas** 14:03 We'll have to drop at 8:25. I apologize. OK.
**Laurent Querel** 14:06 So I let maybe Josh, maybe if you have any question or.
**Joshua MacDonald** 14:11 Just a brief comment. My, background kind of desire is for OpenTelemetry to, that we are sort of on the, maybe not first priority, but building an SDK on the Dataflow Engine framework.
I consider this to be sort of like a high performance or a hyperscale SDK. In that sense, I want to see us make, I mean, I think our logs pipeline is pretty good right now. I want to see our metrics pipeline be as good. And for me, this to be an OpenTelemetry metrics SDK requires facing this thing we call views, which I've never been completely happy with in OpenTelemetry. It's not terrible, but it's not great yet. And I think So there's some work on the views side and the specification there. What I want to see us do here is to do the best views thing that we can. And the best views thing we can is, in my opinion, to be static so that you can figure out how to make it at compile time. I pin down the metrics I'm going to produce so that I'm not doing runtime transformation just to support flexible metrics. Like, that should be a compile time thing. Somehow, that's my ideal. I don't know if we're going to get there right away.
But that's how I see it. Thank you.
**Laurent Querel** 15:19 Okay. But the the view there is a there is a runtime dimension in view, in my opinion. So Okay, there are probably some element of some type of view that you can have at compile time, but I definitely see also a need for runtime oriented views. And and for that what we sorry go ahead.
**Joshua MacDonald** 15:41 Yeah, I agree. We're going to want to have the ability to do these transforms for a pipeline, say, because some SDK outside of us has sent us this data. But for ourselves, I think we can constrain the problem enough that, as Drew has pointed out, there are eight instruments, logically speaking.
We just need a way to map those eight instruments to eight outputs, and it can be.
**Laurent Querel** 16:04 Yeah, yeah, so.
**Joshua MacDonald** 16:05 Yeah, the different mappings there should be doable at compile time.
maybe it can use the same syntax as the dynamic processors, that would be cool, but I just want to get to where it doesn't cost us at runtime to have this choice.
And it's not because I think that there's a good choice. Both choices are good here. It's that I think we need choices. Because we have two choices here today. And when we get through with one of them, we'll have one choice. But then tomorrow, someone else is going to propose a different schema or a different way to do metrics. And that's why we have views, so that we can keep changing as we move forward.
**Laurent Querel** 16:39 Yeah, we probably have some point of divergence there, but it's not a big deal. I have a different opinion.
I think we need flexibility definitively. I think we also need to avoid to complexify too much.
The, the compilation time. And I mean, why, while maintaining multiple version of the same matrix.
because we don't really have a legacy issue here as opposed to the go collector. I can understand why the go collector needs to maintain 2 representation of the same matrix.
Do we really need that? I'm not so sure, especially because Right now, anyway, we don't have the same metric than the book collector, so there is no need to comply on these two models.
And second, why maintaining two models when we already know that one is preferred above the other? So personally, I would prefer to simplify as much as possible the integration into the code.
And then, because… We have this ITS based on the data flow engine with all the processor OPL and so on that we are building.
We just need to make sure that.
whatever you need will be, you will be able to express it easily, efficiently. During during the configuration in the configuration itself.
Yeah, that's not my point of view on that.
So the thank you, Joe, for the presentation. I will just add few things, because we work a lot together on that, just to explain in more detail the the impact on the metric instrumentation in the current version of the project.
So until now we we expressed a metric set.
There is a name and the collection of metrics which could be Gunter and or various other Build pack linter and so and and other other things like that.
So and the and the attributes were defined by the engine itself. So when when it's a metric related to a node automatically, the the system Obviously, we collect all the attributes that will characterize this data point.
We have an option already that we support that lets the… The node configuration specifies custom attributes.
That will be automatically aggregated with the the standard attributes that are maintained and And specified by the engine.
So the the idea here is to let a node author defining either extra attributes that are known and well-known, well-defined at compilation time. The value could be provided Dynamically, but at least the the least.
of those extra attributes are well known. And the second category of attributes are what we name dynamic attributes. So the dynamic attributes are Things like the one that we have here. So, when we report We want to update a metric.
We will have to provide the value for those dynamic attributes for each data point.
So in that case, for example, we'd like to have Signal type and outcome.
They are defined by alien.
in that case 3 values, 5 values. So we have a cardinality of 6.
And for each data point that will be reported, we will have to provide the value for that, a value for that.
And the way that we are specifying that is, first, we say that we have a collection of attributes.
It's an attribute set that is dynamic.
Because it's dynamic, there is a constraint saying, oh, if it's dynamic, you are only allowed to use an embedded attribute.
So there is a check in the macro that that will come with it.
Because we want to make sure that we have a well-known cardinality.
So because we know the guarantee of each enum as opposed to a number, as opposed to a pure freeform text.
We, we have this, this guarantee.
And then we have to attach — and that's done here — for this metric set, optionally, you can attach the corresponding dynamic attribute set.
And and then the macro will generate the code.
that will give you the option when you, when you are instrumenting your code, you will have to provide the value and it will be enforced by the compiler.
You will have to provide the value of the two enum. And when you want to use this concept of extra attribute, in that case, there are static attributes.
That you will have to provide during the registration time.
So before that, we use the registration, just specifying the attribute set, and then you get an handle to report your metric set.
When this declaration exists, you will have to provide, the corresponding, sorry, here, the corresponding, set of static attributes that are, extra attributes specified by, by the author of the corresponding note. So, in the context of the journal D matrix, where, if we follow this new way of representing matrix.
And we'd like to say, oh, everything that will be edited by the journal metrics are related to log events.
So we attach basically the corresponding attribute set, single attributes, which is defined before.
Euro?
It's only containing this dimension, this dimension, or this attribute.
And because it's an extra attribute or slash static attribute, you will have to report it only during the registration.
So that's what is presented.
year and year. Yeah.
Yeah, and I think that could be very efficient. I'm discussing here the A little bit around the implementation, because the goal was to keep the performance that we have with the existing instrumentation system.
Any question on that?
**Joshua MacDonald** 23:46 You've invented the concept in OpenTelemetry we call bound instruments. I like it.
**Laurent Querel** 23:53 Yep. And I try to think about it also to be compatible with semantic convention registry.
And, the ultimate goal at the end is to.
Let us define the semantic convention, a list, basically the telemetry schema for this hotel project.
Use Weaver to validate the registry and use Weaver to generate an optimized client SDK that will basically generate the code that we see here.
And, with exactly the same performance.
Properties.
So I think what we have is macro-based right now. What we will have, in my opinion, at some point, is a way to generate type-safe client SDK derived from a semantic convention.
using Weaver, And that will give us also a way to, for example, use the live check capability of Weaver.
to validate that we have a good coverage in our test integration test, and so on in term of instrumentation that is triggered when we run this code.
Right now, we already have it.
test coverage. I will say functional test coverage. So we we test how much code we really exercise in our test.
we should have the same thing for the instrumentation. How much instrumentation has been exercised in the collection of tests that we have.
And there is nothing currently checking that. Weaver will give us the ability to To measure that and to maybe create some gate in the CICD pipeline.
at some point.
Okay, So the this one purposely let David talk about that. There is, I think.
There is already in the agenda something around it, so I will not go in the detail of that.
Introduce RFC, that's something I introduced… I created yesterday.
And again, there is also an entry for that. So we can, I think, switch to the rest of the agenda. So Drew already presented the metric set and the concept of dynamic attribute.
David, I think you are with us.
**David Dahl** 26:35 Yes, how'.
**Laurent Querel** 26:36 Good. I'd like, you to… to present. I think that will be interesting for a lot of people.
The work that you did on, oh, that's not the, yeah, that, that's the one, the work that you did on the component inventory. Do you want to share your screen or, you want me to, To squirrel…
**David Dahl** 27:02 Continue sharing, that's fine.
**Laurent Querel** 27:04 Okay, okay.
**David Dahl** 27:06 Oh.
Okay, cool. So, basically what, I'm sort of trying to use Laurent's new concept around the RFC by putting this into an RFC's directory and, or sort of, copying some other examples in the Rust world for how they store RFCs in their repo. But this proposal is basically another mechanism to sort of be able to programmatically understand all the components, either, you know, receivers and exporters and processors, or other types of things like DFCTL and, and, and other, admin server, that type of stuff. From the aspect of, in my personal use case right now, it's for generating a TMA, that threat model assessment that we need inside of where we're consuming OTEL Aero downstream. So… this is kind of a way that will allow us to more automatically, when we update our quote-unquote release, I know there's no crates for this yet, of course, but when we, you know, pin it.
We want to be able to then run our process to discover automatically new or changed or dropped componentry that might be inside of OTEL Aero that just gives us a much faster process for, and an automatic process for, updating our own threat model assessment and helping us try to, at least automate as much as possible, because getting it through, you know, threat models are not always fast to get through, and so this is just a way to kind of do an inventory for components. And it also potentially can help for documentation and other use cases that are mentioned in this proposal. So, you know, obviously we're just looking for some feedback from everyone, and before we start Trying to do any kind of, implementation, so…
**Laurent Querel** 29:22 Yeah, just to maybe to, as as many big companies. Obviously we we have to.
To consider security, Very deeply.
And so we have to comply with some internal process. It's not specific to F5. I'm sure that there are various methodology followed by different company.
Internally, for F5, we use the OpenStrike model, the OTM standard, I think.
Feel free, David, to, to correct what I'm saying. But, I asked David, basically, how can we minimize the amount of effort To maintain those threat models up to date or in sync with durability, because that's obviously the main issue when you have to… usually you review a version There is a set of expert security experts reviewing a project, and they deliver a certain assessment.
But if we follow the methodology, we should also, for any important feature, make a revision of this document, and there are some automation around it.
So we are looking for a solution to make that very easy and making sure that we we have some we have some way to derive the threat model assessment from the code itself. And that's why David worked on this idea of Basically, annotating the code with a macro It's very flexible, it's not specific to the concept of receiver, processor, exporter that we have, where we already have some kind of inventory.
But obviously when we talk about security, it's not stopped by those concepts. We could imagine that obviously the admin API is by itself.
A security… I don't know if that's the right terminology, but a security, Aspect or security point that needs some attention and some declaration.
So we need, we are, we are looking for something generic like this macro component inventory. And there is a series of Predefined field and attributes.
that will be used to construct this automated TMA.
And that's what, David is proposing.
**David Dahl** 32:10 Yeah, thanks.
**Laurent Querel** 32:10 Thanks.
**David Dahl** 32:10 Sarai.
**Laurent Querel** 32:12 Any feedback? Question on this topic?
**Joshua MacDonald** 32:19 Just an FYI.
**kennedybushnell** 32:21 Similar. Oh, go ahead.
**Joshua MacDonald** 32:23 Oh, sorry. Thank you, Kennedy. FYI, the Go collector has a structure for generating — what looks very similar from the configuration. So, for every config, there's a metadata file, like a markdown file generated, that contains a description of all the configurations and defaults and stuff like that.
It's derived from the source, as far as I understand. It looks like it falls into the same category, in the sense that we essentially need a way to automatically document our components and all their configurations.
So… 4 scanners, and so on.
**Laurent Querel** 33:02 Yeah, maybe it's… I have the feeling that it's slightly different, but as I'm not fully aware.
I'm not sure.
**Joshua MacDonald** 33:12 I'll have… I'll give some pointers to David, he can.
**Laurent Querel** 33:14 Yeah, yeah, yeah, yeah.
**David Dahl** 33:16 Thanks. Thank you.
**Laurent Querel** 33:17 Because those things that you have here, attributes, they are really there for the purpose of focusing on security first. They are not representing all the configuration, or they are… they, Yeah, it's… I think it's… obviously there… it's like, saying, oh, we already have the… the receiver, processor, and so on, micro, that describe and… and… Create an internal inventory to let us.
Or to let users specify their configuration and discovering automatically what is available.
Yes, but the focus of the of these specific macros.
for the receiver processor exporter are there for the configuration and for the internal machinery to create those things dynamically and so on. There, it's more focused on purely security and purely TMA. And when we can reuse some information, and that's probably where we need to work a little bit more.
we'd like to end up into a situation where we don't have to repeat ourselves. So if we deploy our receiver, and there is a set of metadata, ideally, we'd like to avoid to repeat, So for example, here there is no ID because we want to reuse automatically the ULN of the receiver because it's probably the best ID for the corresponding component.
So that's the type of thing that we the interaction between the.
Pure component inventory for the security aspect versus, Other concept that we have into the into the engine.
I think, Kennedy, you want… you wanted to say something?
**kennedybushnell** 35:08 Yeah, I was going to say very supportive of this. We have a similar threat model review process internally and things like this dramatically accelerate those efforts.
Having something to store from would be great.
**Laurent Querel** 35:22 Yeah, so we really appreciate any — we would really appreciate any feedback. It's really the beginning of this work.
David internally is focused on, making those CMA, Easy to maintain, so we would like to also to learn from other, Context.
And the output, yeah, so what we didn't mention, here there is the cargo X task.
So we already have for this project, we use this pattern, the cargo is task with values sub command.
The idea here will be to to add a new subcomponent component inventory.
That will, give us a way to Generate a human readable table of all the components or properties, but also in different formats that will be machine readable, that could be used to derive your own.
following your own formalism that you use for the TMA. I think Microsoft is well known for Stride. We use OTM and various people will use some other things. So we want to be able to emit a format that could be used to Recreate whatever you need internally.
And there is also this thing that I think will be super important.
So… With this system, sorry, with this command, you generate the current inventory.
And then let's say we document in the country.
procedure that when you create a new component and we will define what is the component for the security perspective.
But when you… When you create a new component, you will annotate it.
then this command will detect a difference between the component's baseline and what we have now, and then, that could be part of the CICD pipeline.
There is a specific review associated with it. So that that will help us also to to be more aware of the Tma update and and security concern.
Okay.
If there is no other question, I can switch to the next topic.
**Joshua MacDonald** 38:00 This is really cool. Thank you for the last topic.
**Laurent Querel** 38:04 Okay, so the last topic is… So what I observed during the… Last few months.
So first, I'm super happy, and I'm sure that it's shared by many people in this audience, but We we we have a lot of documentation and specification that are happening.
In this project, and, and for, specifically for the, the design specification stuff.
We oscillate between GitHub issues sometimes, sometimes PR description, and sometimes PR content.
Spec, related, where… so, for example, we, What has been described by Drew at the beginning was a PR containing just markdown files describing a potential future way of updating the metric set.
We had that multiple times. Lalit wrote, for example, multiple things like that. Joshua also. So.
and we put those documents into the same at the same level than the standard documentation that we also maintain for the project.
Which is a problem, in my opinion. So what I'm proposing here is to follow a classic pattern that We can see in some projects, one project specifically that, inspired me is open doll. I don't know. I think I mentioned that somewhere.
But OpenDAL is, an open source project, also ROS-based, where they basically have, a directory docs, where you have the documentation, that will, Especially especially a user oriented documentation. But there is a subdirectory.
in these docs where you have the Rfcs.
And RFCs follow a specific template.
There is a process with it, relatively lightweight.
And when someone wants to discuss about a design, it will put a markdown file here.
that will be associated with a PR, there is a review process, and at some point, we will say, okay, we agree on the… on the spec, and so basically, it's just a way to formalize what we already do, but where we already mix different type of documentation. I just want to split that properly. And and I'm describing here.
A proposal for the process.
So, yeah, feel free to to comment this Github issue. And and once we we think that it's the right way to go. I think we will 1st migrate the the corresponding document into the Lfcs.
Updated slightly. We don't necessarily need to follow a very strict structure.
But at least we we have the the.
the pattern for the the file name that we can follow. So that's what David did already for the 1st Lfc.
And, and then, we will try every time when we see a PR that is specification oriented or design oriented.
to, ask people to follow this, this principle.
Yeah, I'll be gl.
**Joshua MacDonald** 41:45 I'll be glad to use this structure for my open PR, which is clearly an RFC. And I have some work to do on it. So I can revise and come back with this format.
**Laurent Querel** 41:56 No.
Okay, cool. So yeah, please read that. It's a relatively long GitHub issue.
I'm sure that you will have some very interesting updates.
But, I think next time, maybe we can, Finalize the discussion on the structure of the RFC, the process, and then start the… Put that in place.
Great. We have 10 minutes left. Is there any additional topic that You'd like to discuss?
For new person in the group that like to.
Introduce themselves, I don't know.
**Joshua MacDonald** 42:49 Okay.
I don't know that we need to put people on a spot. I recognize a few who have joined us that are listening in, and that's OK.
I… So if anyone wants to speak, please do.
I didn't put an agenda on the board here for talking about my big RFC on multi-tenant design, because I've already gotten the feedback from so many people on it, so I don't actually think we should speak about it, but I thank you all for that, who have given me that feedback.
**Laurent Querel** 43:26 Yeah, yeah.
**Joshua MacDonald** 43:26 I'm gl.
**Laurent Querel** 43:27 Are we getting the.
**Joshua MacDonald** 43:27 We missed it last week in the meeting last time. So that was mainly what I wanted to see us cover.
**Laurent Querel** 43:34 Regaining the mid-tenancy, Joshua, I still need to finalize the… So I already gave you a lot of feedback, but I didn't… fill it to the review, I need to do that by the end of the week.
**Joshua MacDonald** 43:47 Appreciate it. I actually read through what you've given me, and it resonated. I see a lot of change I need. First of all, in terminology, I got lots of feedback from people on terminology. So I'm going to make a coherent revision to that, trying to incorporate everything that people have recommended.
And then what I'm also seeing there is that no matter what I was going to write in that document, somebody else would read it and expect to see something different. So the scope is so much larger than just what I was putting together there, which was really about identifying subtenants and tenants and so on, as opposed to, I think, much larger questions about how do we isolate the entire system? Where do C groups fit in?
How do we ensure that we start and don't run out of memory? That kind of question. So Lalit and I are going to be working on that going forward. Kennedy.
**kennedybushnell** 44:40 Yeah, there was a good conversation in the last SIG meeting, and we discussed maybe introducing a concept that kind of first classes routing and routing keys. I would like to hear your comments on that. So if you get a chance to review that meeting or some of the notes, that'd be Great.
**Laurent Querel** 45:01 That was here.
No,
**Joshua MacDonald** 45:05 We did discuss it. I don't know that the notes got written down, but the high level, as I recall from last Tuesday meeting was, the concept that we… We often need to route by tenant, but we also often need to route by metric name or by trace ID or by other features in the data. And so what I just said was that everyone can see a different subpiece of this problem. And one of the big pieces that I didn't really address in my document that I think we all see is this having a need to take a stream of data.
To, first of all, identify it by tenant.
But then also to split it apart, because we want to identify tenants that are a resource value.
And we want to treat metric name like it's a tenant as well, for example, so that when you actually find yourself having, say, a topic router and wanting to distribute load, you want to be able to split and join by both tenant as well as dimensions in the data. I think that's where Kennedy's
**Laurent Querel** 46:12 That's sc.
**Joshua MacDonald** 46:13 referring to.
**Laurent Querel** 46:14 Yeah, yeah, I see. And so so I'm not sure that everyone is aware of that. But Albert will work at some point on this concept of partition processor that will be a generic processor to to partition patches, for any kind of dimension.
That could be used for, to split, batches, when you have a batch with multiple tunnels that could happen, that that should be feasible.
Or if you have to split to target different, let's say, Kafka topics based on some attribute or a combination of attribute that should be feasible. So we will introduce a generic. I think we are following the same philosophy from the beginning in this project. We don't.
We, we, we prefer, so obviously we, we favor our performance.
But we also favor composability. And we — I don't like, personally, a situation where every exporter will recreate the will. For example, we don't want to see an exporter batching. We don't want to see an exporter retry logic.
So that's why we have a batch processor. That's why we have a retry processor, and that's why we will implement also a partitioning or partition processor. So we can compose those things together and get a very, a very flexible and composable system. That's the idea. So that combined with topics and because topics are a way for us to Basically to… It's multi purpose. We can use that in different context. Multi tenancy is one of them.
And, and distribution, yeah, multi-tenancy, because you, let's say you have, an ingestion pipeline with a routing, layer, identification of the, this, routing key, and then we will route, the sub-stream In different subpipelines separated by this topic, each of those subpipeline could have their own either configuration or limit. If we talk about multi-tenancy.
The ability to specify limit pertinent is is fundamental. So in order to do that at scale and very efficiently. We have those let's say.
componentry or way of combining things where we we have a thread.
Where we, we are able to attach, C group limits.
But we could say, oh, this thread is for a specific tenant. So that will be translated into a dedicated pipeline instance.
And the schema that I was describing, where you have a pipeline ingestion topics, routing the information to different pipelines, each of them could represent a tenant, where you will apply a specific limit That's the model, in my opinion, that scale. And that's why we introduced this concept of topic and variance resourcing.
I also seen that We initiated the… This concept of, hierarchical policies From the engine, to the group, to the pipeline.
and to the nerd we have to.
move everything that is policy related following this model. So that's uniform. And and we can, for example, for the the rate limits and the And other things like that, that could be expressed for a specific multi-tenancy, configuration, I think we should follow the same principle that would make the system at the end very uniform and understandable.
And reusable in different, for different purposes.
Yeah, I think that's, What I was thinking, adding to this conversation.
**Joshua MacDonald** 50:33 Thank you. Yeah, thank you. Yeah, so Albert mentioned the topic component routing, partitioning as a matter of OPL. And I see the integration point. Yeah, so now that we've had this conversation, really what I'm trying to do with this document is to separate.
like the the notion of a tenant tenant.
Call them tenant tokens. Maybe the identity of a tenant is somehow a first-class feature that we can use for routing and for batching and for processing and for limiting and for load balancing. And it's somehow separate from all of those things because we're factoring our software in a nice way. So I will continue trying to frame this. I definitely need to put a little more emphasis on how.
Partitioning and rebalancing are one of the major features of a multi-tenant design.
I think that's what I.
**Laurent Querel** 51:29 Yeah, I agree. And for all the design we have, just repeating something that we already said multiple times, but Personally, for me, this project is focused on performance.
So the designs every time need to take that into account very deeply. And sometimes that will prevent us to follow some approach.
So for me, we should avoid at any cost any kind of synchronization primitive across thread across core. Maybe we will have some exception, but if we don't enforce that very strictly, we will kill basically the performance that we have been able to represent at the end of phase two.
very, very quickly. And maybe that will not be apparent for some configuration, and just suddenly someone is using a different type of configuration, this primitive synchronization primitive is introduced, and boom, performance divided by 10.
No, we don't want that. So, yeah, just think about that very, very deeply each time that you have this kind of, design, because that's, in my opinion, a super important property that we want to keep.
**Joshua MacDonald** 52:56 Thank you. Yeah, if it wasn't clear, that was a mistake of mine. I was not trying to introduce any mutexes or synchronization points.
**Laurent Querel** 53:07 Yeah. I I was not necessarily talking about this spec. It's it's more general. Yeah.
**Joshua MacDonald** 53:12 Yeah, I keep flagging. Any mutex makes me curious or curious and skeptical at this point. So keep watching out for those mutexes.
Yep.
**Laurent Querel** 53:22 Great. I think we are at the end of the session. Thank you so much, guys. See you next week.
**Joshua MacDonald** 53:28 Thanks, Laurent. Bye, everyone. Thanks.
**kennedybushnell** 53:31 Thanks all.
