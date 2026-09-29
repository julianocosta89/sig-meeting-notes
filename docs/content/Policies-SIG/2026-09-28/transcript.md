SIG: Policies SIG
Date: 2026-09-28
Duration: 30 minutes
============================================================

## Zoom Recording Transcript

**Dinesh Gurumurthy** 01:57 Hey, Jack.
patient.
**Jack Shirazi** 02:01 Hello.
**Dinesh Gurumurthy** 02:04 I can't hear you. One second.
**Jacob Aronoff** 02:19 Hello, sorry I'm late.
Let's see…
**Jack Shirazi** 02:24 Hello!
**Jacob Aronoff** 02:25 So, we don't have Josh or David, I'm gonna just ping them.
Real fast. Pablo, how are you?
**Pablo Baeyens** 02:36 Doing fine. What are you…
**Jacob Aronoff** 02:38 Well.
This time is good for your, absurd schedule.
**Pablo Baeyens** 02:46 Yeah, this works.
**Jacob Aronoff** 02:47 Nice. Good to hear.
Let me just… I'm gonna message Josh.
**Pablo Baeyens** 02:54 Okay.
**Jacob Aronoff** 02:55 David.
And then, let's just get started here… Okay, so… oops, sorry.
Okay, so I think, I think we should just get started. We'll wait for them to join.
I think today will be relatively brief, sort of introductory.
The main goal is just gonna be talking about the open PR that I have.
Which I'll put in the agenda here.
This.
Here's the initial spec document.
4… New policy… Okay.
I can share my screen, actually, and just… Get in here.
We have a bunch of reviews already, so thank you for commenting. Jack, have you seen it yet? Have you looked at it yet?
**Jack Shirazi** 04:02 I'm looking at it right now.
**Jacob Aronoff** 04:04 Great, great. It's long. This is gonna take, you know, some time to… get in and get right. But we have a bunch of feedback already, which is great to see.
And my goal today is to essentially just iterate on it. So, if you have any feedback for it.
Do let me know.
Or I guess put it on there, and then we can have a discussion about it.
The main thing of… interest… is probably… Around how we want to handle.
Determinism.
Relating to, the, like, merging rules?
So, Jack, I know this is something that you had thought about before.
In my initial versions, I was doing it via alphanumeric, sorted order.
With a… Clause that you… cannot… Or it's… Well, one of the issues with it was… If you have two matching IDs, how do you decide which one to keep?
Is, is another one, and so.
Like, how do you… like, sort of those tie-breaking rules are interesting, and so… We can talk about it now, but I'd also love your feedback on this, so that we can have a discussion on the PR as well.
**Jack Shirazi** 05:34 Yeah, I haven't seen enough of the PR to feedback, but I'll feedback on the PR.
**Jacob Aronoff** 05:42 Thank you.
And then… Yeah, one of the thing… One of the things that… So… I'm just trying to go back to this part.
One of the things that David was interested in was Being able to… Have explicit keeps, rather than… Drops always winning. So, the idea being, like.
If I have N matching rules.
For policies that drop.
piece, and then I have another one that is an explicit keep.
Will we have precedence for the explicit keep?
Over the drops.
And that's where it gets a little funky. In my initial version of this, it's easy when You're going on it's easy to it's easy to deduplicate and do the merging rules with most restrictive wins. And so the idea of being able to have an explicit keep being the highest precedence.
I.
Could mess around with that.
So, I'm interested to hear if anybody else has thoughts on that problem, or if I need to explain more. Sorry, I'm like… my brain is very deep into the syntax, and so I know that I'm… Maybe skipping some explanation here.
**Pablo Baeyens** 07:29 I also think I need to go through the… document before having… No problem.
**Dinesh Gurumurthy** 07:37 Yeah, yeah, same.
**Jacob Aronoff** 07:40 Yeah. I mean, it it's large, but hopefully digestible. I think the best way to go through it is looking at the… Examples that are in there, just to get a better sense of, like, what each of the sort of things look like. I mean, it's verbose in the way that, like, a lot of hotel Specs are verbose, which is unfortunate, but just kind of the nature of writing spec, right?
But hopefully the examples help. You can also always look at… I have in my, like, company repo.
a whole… corpus of examples, so… I'm gonna link that in here.
In the, meeting notes?
So you can look at them. The other thing that we're gonna be adding in, once we… Once we get this merged, sort of as, like, a follow-up, is going to be adding in these… conformance tests?
So you can see that I linked both of those right now.
I actually might just share my screen really fast to just show.
What is the point?
Cool. Are we able to see my window here?
Thumbs up, yes? Yep. Cool.
So this is the conformance suite that I've been writing, internally. Well, it's not really internal, it's public repo, but… this is what we're gonna upstream once we are sort of set on the spec. I'll modify these examples as needed.
But I have this, like, huge amount of test cases here to deal with, kind of, like, all of the edges that one might run into.
They're pretty exhaustive. I'm sure that there's, like, some samples that I have not come up with.
But this will at least give you a sense of, like, what the grammar can do.
today. So an example of that is, like, maybe just this one that's interesting. So the way all of these work by having a input JSON.
Which is just the, like, Proto JSON proto like, OTLP proto JSON format.
With mostly zeroed-out fields, it's just extra verbose for kind of no reason.
later on, this is one of my older tests, later on, I realized that I did not need to, like, have all the zeroed-out fields in. So, some of the later ones are, like, a lot simpler to read, but yes, minor, minor fix.
And then you have an expected shape.
So, this is, like, I expect… this to be the input, and this to be the output, and then I expect, these stats to be recorded for this policy.
essentially.
And then this is the policy that I'm running. So… Given this ID with this name.
Name is mostly just for, like… user help, not a, like, thing that the machine will read, really. It's dropped by the engine, so it doesn't really matter.
But here, I'm, like, matching when the log attributes HTTP method is post, and I'm saying keep none of them, so drop all of them, right?
And so we can see that in here, we have two logs.
One of them is HTTP method GET, another one is HTTP method POST.
And, we expect to only keep The one was get.
Right.
So… That's the setup for all these tests.
I have some more complex ones in these, like, compound files. These are essentially, like, sequenced things, where… I want to check that if we have… I… one of the things I support is, like, rate limiting, and so I want to see that if I send, like.
you know, and hundreds of requests, and I read limit at, you know, 10 per second, then I only keep 10 of them, right? So, things like that.
And then these ones are usually testing the merging behavior of, like, multiple policies and how they function in that way.
But… Take a look, there's a lot of them in there.
And I think they'll be really useful for this type of thing. The thing that I'm particularly… proud of slash excited to see more of is this, like, expected stats stuff to verify that, you know, we are doing the meta-reporting correctly. Yeah, question.
**Dinesh Gurumurthy** 12:20 Jacob, which code base are you running these tests again?
**Jacob Aronoff** 12:24 This is in the policy conformance suite.
**Dinesh Gurumurthy** 12:28 So even the code base is within that conformance, it's…
**Jacob Aronoff** 12:32 It's the second one right here.
**Dinesh Gurumurthy** 12:35 Okay.
**Jacob Aronoff** 12:37 The, examples one are all… these are just, like, YAML examples, so they're pretty boring.
So this is just, like, you know, given a log body that has this, redact it with that, you know. They're all pretty… they're small, is what I would say. Most of the PR that I'm making comes from this repo and the Google-made repos.
So… That's sort of the merge of them.
**Jack Shirazi** 13:03 Yeah, Jacob, I just had a skim through. So one of the things that was missing from the original specification, I still think missing is being able to do an operation which affects the SDK… But it is not a transform filter, so the example is changing log level.
to debug.
Hmm.
Which… Isn't directly supported by the specification.
But needs to be, because… like.
**Jacob Aronoff** 13:33 It should be. That's definitely supported. I have an example for that, actually.
So.
And here… I should have one for level.
That is supported in the syntax. So, the way that… Certainly.
One of the fields in here should be… oh, you know what? It didn't make it through.
It should be in there. I'll add that in. That's a mistake. In the original version of this, so the one that I have here, I'll show the proto format.
I might not have documented it, which would be incorrect.
But, in here, one of the targets that I support is the… Severity text.
But that's not the level, right? There's another field for level, isn't there?
**Jack Shirazi** 14:29 So the… but you're talking about… The log level of logs.
Whereas I'm talking about the log level of the SDK.
It's like you want to turn logging to debug or on or off.
For the SDKs itself.
I see. It's not really… it's not trace metrics or logs, it's… I mean, you could put it into under any of those, but it's really… Core, or… and also it's… It's not a filter, or a trace, or… not a filter, or a drop, or a… It's… It's kind of an operation at the core level of the SDK.
**Jacob Aronoff** 15:09 Yeah, I see what you're saying. This is something similar to what, Josh wants to be able to do with the metric rate, the recording rate there.
I think we have to think about that. I don't know if that's in the initial version of this, or the follow-up of this. Like, a thing that we build on. Like, the thing that Josh was talking about.
in here, Is the idea of… this… Envelope.
As optional, and then what we would do is, like, add in different, definitions. So one of them would be, like, log level, right?
would be one of these definitions, where it's not a log filter, it's not a log transform, it would be, like, a policy… a SDK-specific policy, right?
**Jack Shirazi** 16:03 It's not… yeah, but it's not even SDK-specific, because you could… you want to turn debug off and on for anything, right? So… It's… it's… it's kind of a core, rather than metrics. It's not a signal, it's core, if you like, so it's a kind of a different… And a different level.
**Jacob Aronoff** 16:28 Metrics don't really have a concept of being a debug metric today, right?
**Jack Shirazi** 16:34 Well, that's what I'm saying, is that… so we've got… you're looking at it as a signal, logs, metrics, or traces, but there's kind of a fourth pseudo… Signal, which is core.
It's… it's the… the… The core component that is running.
**Jacob Aronoff** 16:51 anyone.
**Jack Shirazi** 16:51 affect the core component.
To do something different.
So I think we're kind of missing that completely.
**Jacob Aronoff** 17:00 I think that that, though, is still within… Like, like, in my mind, based on this, you would define that as a, like.
you know, log-level policy, not a core policy, because you're still targeting, like, the logs SDK, no?
**Jack Shirazi** 17:20 No, that's the… you're not targeting the log signal.
Because, for example, if I want to put debug on for the traces, so that I can see trace-level output in the logs.
Then I'm not turning debug log on the log signal. It's debug on the traces.
Which come out in the logs. So it's really kind of a fourth pseudo signal where you're saying component level operation.
**Jacob Aronoff** 17:54 Yeah, I guess the question that I have, that I'm not sure of the answer, for what it's worth, is if that would be an individual policy for… Each of those cases, or if that would be one policy for, like.
you know, change the core level, because I can see it going either way, where… you know what I mean?
**Jack Shirazi** 18:17 I I understand what you mean, but I don't think there's any component in OTEL where you can turn debug logging on for one signal.
It's pretty much the component. You turn debug logging on for the component, or you turn it on.
**Jacob Aronoff** 18:30 thing. I thought that the, when I was working on the metrics SDK, though, it was a… For metrics, it's like you're setting… the… on the trace… sorry, the tracing SDK, you set the, global… it's a global for the trace API, isn't it?
**Jack Shirazi** 18:52 It tends to be a global for everything.
**Jacob Aronoff** 18:55 For everything.
**Jack Shirazi** 18:55 I mean, I know the Java SDK. I'm pretty sure with the other ones.
You just turn debugging on or off. There isn't… I see. I can't say turn it on for these… Subcomponents or this signal and that or that signal.
Yeah. It's all or nothing, pretty much.
**Jacob Aronoff** 19:14 Let me just look at what the.
Yeah, because you're doing it on the global OTEL API, right? Like, you would say, like, OTEL.set.
yeah. I wonder about the actual Go docs.
**Jack Shirazi** 19:27 I would add that it's not even part of the API. So every language has its own mechanism.
It's not set in the API. Even the log levels are not set in the API. Yeah.
There was an attempt to, to… To define log levels as part of the specification, but it went nowhere.
And for example, the Java SDK only has debug on or off. It doesn't have levels, whereas some of the other languages do have levels, like I think the .NET one does. So it's, yeah.
It's… it's not as… but the… the… I'm not really looking at the implementation. What I'm saying is that we're missing… a… A sort of pseudo-signal here, where it affects the component rather than… it's not filtering or dropping or doing anything to the actual signal. It's changing the core component.
The way the core component does something.
**Pablo Baeyens** 20:35 Do you have other examples where it is specified and it's like a core thing?
**Jack Shirazi** 20:41 Well, turning instrumentations on and off.
That's… that's, again, It might or might… it… It usually affects… More than one signal, so traces and metrics can both be affected by some instrumentations.
That's… those… those are the two, main areas, which I think…
**Pablo Baeyens** 21:06 Yeah.
**Jack Shirazi** 21:07 we can fit into, you know, I can create a policy for it and just pick one of the signals and just say, okay, it's in this signal, but it's really kind of a different style.
I'm fine with just picking a signal to do it.
But conceptually… We're not handling it.
**Pablo Baeyens** 21:34 Yeah, I guess what I would be wondering, with the example that you said about setting instrumentation on or off. I think this is something that you could do with the Clarity config, and… Yeah, something that's unclear to me is like, what?
When do you want to use Policies or declare a SAC config?
**Jacob Aronoff** 21:51 Yeah, that's a good question, Pablo, and maybe I'll expand on that as a brief aside.
For a second?
Still not sure.
To me, declarative config is not… it's more for defining the… like… Point in time initialization configuration.
It does not do… The, like, large… larger scale, like.
Filtering, transformation, and dynamic nature that people want access to.
**Pablo Baeyens** 22:29 So.
**Jacob Aronoff** 22:30 like… The declarative config is very static.
And meant to be the… like, global shared thing that all of the implementations, like APIs and SDKs.
can run for consistent behavior, and Policies I see as the dynamic layer on top of that.
So.
It's closer to… making, like, OTTL accessible in declarative config, but also we couldn't do OTTL for the reasons in the initial document, right?
Yep.
**Jack Shirazi** 23:04 I'd add further that I've discussed this with Jack Berg.
And he's got no… Impetus to support dynamic capabilities within the declarative config, mainly because In order to do that.
you would… you would have a change to the declarative config, and then you'd need to do a diff of the declarative config in order to see what's changed, in order to notify the policy, the telemetry policy, to say, this has changed, and you need to do that. And that becomes really complex, because there isn't a good YAML diff capability.
And even, you know, saying that the SDK needs to, or whatever is reading the declarative config needs to handle that becomes really complex, so… Like Jacob said, declarative config is very much initialization and static, and there's no, there's no likelihood that it's going to be supporting dynamic things.
At all.
**Pablo Baeyens** 24:05 Yeah.
**Jacob Aronoff** 24:06 Yeah, the… and that's where, you know, the goal of this project is to enable distributed dynamic configuration. Like, one of the challenges that we have in the operator group Is, you know, one of the most common requests, which is, like.
why can't I just define my collector config piecemeal, and then the operator can figure out how to, like, put it together, essentially. But doing that in practice is, like.
kind of this impossible task, because doing YAML merging combined with Individual, like, component validation and verification is really, really difficult.
And just because, like, there's no good way to know what components an image supports without running it and testing it, and so you can start up a collector config that's just, like, fully broken.
really easily in that world as well. So, the goal with these policies is that they are just, like, these piecemeal Tiny things that have a very well-defined merging syntax and merging rules.
That anybody can define any amount of them, and they'll merge into something that is, confirmed to work in any of its implementations.
And work consistently in its implementations.
**Pablo Baeyens** 25:24 Yep, yep.
**Jacob Aronoff** 25:24 Yeah. But it's a good question. I think that there will definitely be some confusion outside of this group relating to that. So it's important that we're clear on what our merging semantics are.
**Pablo Baeyens** 25:37 and.
**Jacob Aronoff** 25:38 how we will work with the other sort of efforts within OTEL. Like, the other one that, I think was of interest to a bunch of people was how this works with, like, OpAmp, and, you know, does this conflict? And the answer is, like, a really easy no, it doesn't conflict, because OpAmp itself does not define a configuration syntax.
Right. In many ways, like, this… project stems from that challenge, right? Where, like, people want to have, a defined configuration for doing dynamic, reloading.
But, you know, OpAmp just is agnostic in that way, which actually is beneficial for us, where we can just, like, ideally be able to send down, you know, boatloads of policies to whatever implementation, and then they know how to run it. We can piggyback off of a lot of the What's the word?
capabilities guarantees from the OpAmp protocol.
To ensure that implementations run the policies that they are able to run. Like, they actually receive the ones that they're able to run.
But anyway, I'm getting ahead of myself.
**Pablo Baeyens** 26:50 No, yeah, but thanks. That clarifies things. Yeah.
**Jacob Aronoff** 26:52 Yeah, once we do the op-amp stuff, also, like, there's one… specific change that I've had requested for OpAmp that I'll probably have to do in the next year, which is the.
like, minimal diff set change within OpAmp, so that ideally, like, what you want to be able to do, and what is really challenging today with Collector Config, is you want to be able to send… Only the smallest change over the wire, so that you don't waste needing to send, like, a full report back and forth over the connection.
Because otherwise you'd be doing that a lot. It's, like, kind of a ton of bandwidth, unnecessarily. And so, what we will be able to do is take a hash of a policy set.
Compare that in the implementation for what their running hash is, determine the difference between those versions, and then only send the changes, like, the actual change set for them to run.
Such that they don't need to get down all of the policies, they just get down the, like, minimal set of the changes that they should make.
It's an optimization, but… one that I think will be really valuable, and one that is, like.
actually a lot easier to do with this syntax. But that's a later project.
Anyway, David, thank you for joining. Sorry, this is, like.
Okay.
**David Ashpole (Google LLC)** 28:15 So sorry I'm late. I knew that we had scheduled a meeting and I never copied it to my calendar.
**Jacob Aronoff** 28:20 You're all good. I made that mistake so many times with Zig and Injector, and then they moved times, and I didn't realize it, and I kept joining the wrong meeting. So, very fun.
Anyway.
We're mostly just doing, like, I'd say introductory things while people are going through the document, sort of answering any questions that people have. Now that you're here, we could maybe do… Some more discussion on one of the key topics that you brought up?
In the document?
**David Ashpole (Google LLC)** 28:52 Yep.
**Jacob Aronoff** 28:53 Relating to… well, there are two things that I wanted to discuss.
By the way, one of them… oh, go ahead.
**Pablo Baeyens** 29:01 Before we move forward, I made this half an hour. We could make it one hour. I wasn't sure about that.
**Jacob Aronoff** 29:07 I think it's fine to do half an hour. I mean, we could stay on a bit longer here, just to… just because it'd be good to chat with David about this before I…
**Pablo Baeyens** 29:16 Okay, yeah, sure.
**Jacob Aronoff** 29:17 These changes, but I think going forward, half an hour will probably be fine. I think today was just, like, we're all getting accustomed to timing, so… Yep. Which is the nature of it.
**Pablo Baeyens** 29:27 Makes sense.
**Jacob Aronoff** 29:28 But but thank you for the the timekeeping. So just very important.
So, yeah, David, the two things that I wanted to talk about, one of them was the, deterministic behavior for.
merging, doing it with, like, alphanumeric was my idea, and then the other one was, your idea of doing… allowing a… Explicit keep to be… The highest precedence rule.
**David Ashpole (Google LLC)** 30:00 Yeah, so that… Yeah, so let's go into the first one. I think I haven't seen any disagreement over alphanumeric.
for policy ordering. So, unless we get some, I think we should just put that in and let anyone voice their objections.
Cool.
And then for… Yeah, for keep and drop, I was trying to figure out how to… I was trying to figure out how to make keep.
Not be a no-op?
Because Keap is, like… At least when I was reading, I was like, okay, like what can policies do? They can say to drop something.
And so, it's like, if keep… Just means, like, hey, I want to keep these 3.
Then I guess if there's a drop that comes before it, like then the ordering really matters, right? So.
**Jacob Aronoff** 30:54 if.
**David Ashpole (Google LLC)** 30:55 There's like ordering precedence between keep and drop.
I think my worry is just that it's, like, really hard to reason about. Like, in an ideal world, nobody would ever rely on alphanumeric intentionally. It would just be, like, a thing that gives you consistent behavior.
But that hopefully you never build on, right?
**Jacob Aronoff** 31:16 Yep.
**David Ashpole (Google LLC)** 31:17 And I'm sure people will build on it, but that's… That's kind of their problem. Yeah.
**Jacob Aronoff** 31:24 Yeah, in my initial, like, design here, the… as you said, like, the explicit keep is a no-op, in that it's really… your goal is more to run the second stage, which is transformations, right?
The idea being that, like, you have all of your drop rules, and maybe there's some overlap, and then you're dropping… so, like, if I have 3 policies with differing levels of restrictiveness.
I… Use the drop semantics of the most restrictive theoretical.
So, like, if it's… you know, I want to keep 5%, keep 10%, keep, you know, 50%, then I will respect the 5% decision over the other two.
**David Ashpole (Google LLC)** 32:08 I guess what I would say is, like, I would rather it.
If keep 5%.
Is exactly the same as drop 95%.
**Jacob Aronoff** 32:19 Yeah.
**David Ashpole (Google LLC)** 32:20 I would prefer that everybody just write drop 95%.
**Jacob Aronoff** 32:24 Yeah, that's super fair.
**David Ashpole (Google LLC)** 32:26 And I think we have… I don't remember if this was just in my prototype or not, but I think we have an invert.
In the…
**Jacob Aronoff** 32:34 Chris.
So…
**David Ashpole (Google LLC)** 32:36 If, if like writing out a keep rule or if writing out a drop rule is hard because you like.
You want to keep everything except X, then, like, we already have inversion there.
**Jack Shirazi** 32:48 So yeah.
I'm missing something here. Are we talking about defining this per policy? Because that's not generic. There's no way for you to say 5% is the more restrictive number for a generic policy.
Compared to 10%.
5% could be the less restrictive policy for a different policy. So, if this is per… if you're going to define it per policy, it becomes very unmaintainable. And if you're going to define it generically, you can't say that 5% is more restrictive than 10%.
**Jacob Aronoff** 33:19 What do you mean?
**David Ashpole (Google LLC)** 33:19 Give an example, yeah.
**Jacob Aronoff** 33:20 Yeah.
**Jack Shirazi** 33:21 So, yeah, for tracing, it's true that 5%… if you're sampling 5%, it's more restrictive than 10%, but for something else, it might be completely different. 5% might be less restrictive than 10%. I can't think of something immediately, but generically.
There is no way of saying that one number is more restrictive than a number in a generic way. You can only say that on a per-policy basis.
**Jacob Aronoff** 33:46 Yeah, this is for the specific log filter policy, not for the, so we're… there's two sort of structures that we're, defining here. We have the thing that we're calling, like, the envelope, which is the sort of larger proto-message that contains the individual, like, policy definitions, and then we have the policy definitions, which are, like, log filter, log transform, trace filter, whatever. And so, when talking about the merging semantics, we're really doing that on a… policy definition to policy definition basis. We're not going to have a… We're not defining the restrictiveness semantics on the envelope. Does that answer… does that make sense?
**Jack Shirazi** 34:31 It does, but it I I think you're still wrong because even if you take any particular policy, you can't say that comparing this policy with it with another instance of that policy.
This is more restrictive than that. Why not? Because the policy might be something where 5% is less restrictive than 10%.
**David Ashpole (Google LLC)** 34:55 Restrictive is maybe a misleading word.
I would, I would just say that All policies are always applied to all telemetry, right? For things like keeping or dropping.
And if… In, in the, I think in the current design, if any policy drops something, then it's gone, right? So what you have You end up applying the union of the set of policies.
And so it ends up being.
each additional policy can only further restrict the set of things that flow through it, right? Yes. We don't have any… There's no concept right now of, like.
you know, an overriding veto policy that lets a batch of things through, right? Policies only Further restrict the set of telemetry that flows through.
**Jack Shirazi** 35:43 Yeah, I get it.
I think what I'll do is I'll put it into the document, because I don't think you're understanding my…
**David Ashpole (Google LLC)** 35:51 I'm not on… yeah, so…
**Jacob Aronoff** 35:53 Yeah, I think an example would be helpful, Jack, to, like, understand the counter example, the, like, counter that you're coming up with. Sure.
Because I think, in my mind, like, the system is what David describes. But I'd be interested to understand why that, you know, that may not work. Would be good to know.
So.
**David Ashpole (Google LLC)** 36:17 In terms of keep versus drop.
I think the, the like classic example of where people might want an overriding.
type behavior.
Is if, like, you're sampling at a particular rate, but you want to keep all the errors, right? And so, figuring out how someone would, like.
Write that.
It's… it's tricky, right, because… Or.
I could also see us just not having keep to start and just having drop.
Be an enum with only one option for now.
**Jacob Aronoff** 36:52 Yeah, no, definitely.
**David Ashpole (Google LLC)** 36:53 If that's where we want to start, so I'm happy to postpone the discussion to somewhere where it's not like.
Tangled up with everything else. But I do feel like.
**Jacob Aronoff** 37:00 keep.
**David Ashpole (Google LLC)** 37:01 In its current state, it's, like, maybe a little… Misleading, because it doesn't do anything.
**Jacob Aronoff** 37:08 Yeah.
Document 1.
Okay.
Yeah, I definitely understand the confusion from the current term.
I think doing, like, a one-of enum is definitely fine. And I think also fits within, sort of, the… design standards that I'm trying to go with for the proto itself.
I think I say this in the document. If I don't, I should, but… One of the things that I'm trying to do with, policy proto is prevent any, like, conflicts or, like, validation problems. So, that's, like, using one of For things where you don't want… multiple possible behaviors. So, it creates some duplication in terms of fields, but it also results in… Ensuring that, like.
if I can write a proto-JSON, correctly, then I am confident that that will, be able to be run. The idea being that, like, you don't want to allow users to shoot themselves in the foot and, like, write bad grammar.
Right.
Eventually, like, you could imagine, a world where you define an actual, like.
you treat the proto-JSON almost as, like, an AST, and then you have a custom syntax that then translates into that AST. And because you're confident that the AST is always valid, then you can do better things with, like, a simplified syntax.
Great.
But that's, like, obviously not a goal of this, is I don't want to write a language. That would be, I think, way overkill, but that's, kind of the idea, is that, like, you want to prevent users from doing that and, like, needing a bunch of validation rules.
Anyway, okay, so that's a good… that's a good point, David. I'll make that change. Is there anything else in the document that anybody else wants to discuss? I mean, we are over time, so we can… Drop here.
**David Ashpole (Google LLC)** 39:24 interested in discussing and especially hearing your thoughts, Jacob, on regular expressions. I feel like that.
**Jacob Aronoff** 39:31 Yeah.
**David Ashpole (Google LLC)** 39:32 Biggest cans of worms, but… I feel like I would like to have, like, 20 minutes for it, and I do have a meeting that I should…
**Jacob Aronoff** 39:39 At 11, or right now?
**David Ashpole (Google LLC)** 39:41 10:30.
**Jacob Aronoff** 39:42 Let's maybe do this. Let's just talk about it in Slack, and then continue from there. I have a lot of thoughts.
You know what? I'm gonna save it for Slack.
**David Ashpole (Google LLC)** 39:55 There's some cool performance advantages that are probably on your mind. If we don't use regular expressions, but I also, you actually, I think have a quite a few users already trying this out. So I'm sure they've already written many regular expressions and would be.
**Jacob Aronoff** 40:10 Yeah. But also, like, we can… we can adjust as needed. Like, there is a world where we support both. I'd prefer not to, but, like, we can talk about that.
**David Ashpole (Google LLC)** 40:21 Cool, cool, cool. Let's, let's just… Alright.
**Jacob Aronoff** 40:23 Okay, we'll go to Slack. We have a question.
**David Ashpole (Google LLC)** 40:26 up here.
**Jacob Aronoff** 40:27 Yep.
Oh, hand down. Never mind.
**Isha Bhardwaj (Individual Contribution)** 40:36 Alright, so I also went through the log policy file in more detail, and I did notice one thing, that the log redact says that non-string values yield no change. Is that intentional as a field open safety choice, or should there be a way to, like, redact a numeric bool field?
For example, like, an account ID stored as an int by converting it to its, like, string representation first.
Because right now, there's no way to know.
**Jacob Aronoff** 41:08 It's an interesting question, but the redaction… to me, that's not… redaction, that's transformation. Redaction, I think, is a more specific thing for… Strings, specifically?
Where you're trying to identify, like, pieces of actual, like.
pieces of PII, and then give them a, like, a specific redact… I mean, redact in many ways is just, syntactic sugar.
For law… for transformation, right?
It is nice.
**David Ashpole (Google LLC)** 41:43 that they happen first. I could see someone as well wanting to redact like bytes in case it's like a token or something or like there's a.
It's very interesting, but I.
**Jacob Aronoff** 41:54 Yeah.
**David Ashpole (Google LLC)** 41:55 I agree that, like, The need is met just through transformations rather than redactions today.
**Jacob Aronoff** 42:01 Yeah, I think that there's no, no issue necessarily with adding it to redaction, though. Like, if we… if that's what we want to do. No redaction mode. Yeah.
**Pablo Baeyens** 42:14 There's people that have complaints.
**Jacob Aronoff** 42:15 very relevant thing.
**Pablo Baeyens** 42:16 Yeah, yeah, with the reduction processor.
**Jacob Aronoff** 42:19 Huh.
Actually, super interesting, so maybe we should… we should support this too, then.
**Isha Bhardwaj (Individual Contribution)** 42:25 Also, I, commented on the log record field body, as suggested by David.
about the observation on proposing the reusing attribute path for structured body traversal.
**Jacob Aronoff** 42:41 Where is this?
Can you, like, link to a comment?
Yeah, David, thank you. We'll continue discussion on the, in a Slack.
Could you link, the comment you're talking about? Just so I got it.
Thank you.
the way that GitHub does, like.
comments now is very frustrating to me. I don't know if anybody else I just found that… I found it frustrating. Pablo, do you find it frustrating? Or am I alone in this?
**Pablo Baeyens** 43:12 What exactly is 45%?
**Jacob Aronoff** 43:15 The thing that I find frustrating with GitHub… let me… let me rant for just a moment. Like, the way that it's… when I'm reading through a document like this, I don't know where people are commenting without, like, the tiniest little hint on the sidebar here.
Or I could do the comments panel, but this stuff is still disconnected, like, from the lines that it's on, right?
And so I could do this.
But it's like, I don't know, it just feels like a lot of button clicks, you know? Like, I want to be able to scroll through and just read comments, you know?
**Pablo Baeyens** 43:49 know.
**Jacob Aronoff** 43:50 But again, maybe that's just my personal frustrations with things.
**Pablo Baeyens** 43:55 There's many things to be frustrated with with GitHub.
**Jacob Aronoff** 44:00 Don't don't get me started.
So it's not with the rule that if body isn't a target, it's treated as absent.
So.
I have to… if I… one second.
Yeah, I have to think about this. I don't know if I have an immediate answer.
But we can continue chatting about this on the issue and in Slack as well.
**Isha Bhardwaj (Individual Contribution)** 44:40 All right.
**Jacob Aronoff** 44:41 Actually, I need to read through this. This is a good technical question that I don't want to give, like, a snap call to.
**Isha Bhardwaj (Individual Contribution)** 44:47 Alright.
Thank you.
**Jacob Aronoff** 44:50 Well, thank you, everyone. Jack, thanks for your comments, and let me know, when you… Well, I'll see on my GitHub notifications, but we can also continue discussion in Slack and go from there.
So, thank you very much.
Thanks, everyone.
**Isha Bhardwaj (Individual Contribution)** 45:06 Okay.
