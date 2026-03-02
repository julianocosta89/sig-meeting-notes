SIG: Go Compile Time Instrumentation SIG
Date: 2026-01-08
Duration: 68 minutes
============================================================

## Zoom Recording Transcript

Przemyslaw Delewski 00:02:55 Hi.
Dario Castañé 00:06:50 modern.
And good evening for everybody.
I'm not sure.
Huxing Zhang 00:06:59 Hello, Happy New Year.
Xabier Martínez 00:07:01 Happy New Year.
Przemyslaw Delewski 00:07:05 Here, too.
Should we wait for a few more minutes, or do you think that we can start?
Dario Castañé 00:07:18 Kamal is going to be 10 minutes late, but he said we can't start.
Przemyslaw Delewski 00:07:27 So, I don't know who is facilitator today.
Huxing Zhang 00:07:33 Let me see…
Last, last meeting, we have Camo as the facilitator.
Przemyslaw Delewski 00:07:47 Yeah.
Huxing Zhang 00:07:48 Next one is me.
I'll be the facilitator today.
Przemyslaw Delewski 00:07:55 Okay.
Huxing Zhang 00:07:58 Okay, let me share another screen.
Hmm.
Okay, can you see my suite?
Dario Castañé 00:08:34 Yes.
Przemyslaw Delewski 00:08:34 Yes, we see.
Yi Yang 00:08:36 Yes.
Huxing Zhang 00:08:37 Okay.
So, I don't know who it is, and maybe it looks in good shape, we can…
Start to discuss things.
By these notes, I think, yeah, I…
Przemyslaw Delewski 00:08:55 Yes, so I yesterday added a few points according to the discussion that we had on the Slack channel. I don't know if that's all the points that we would like to discuss, but that's some kind of synthesis.
From, from, from this discussion.
Huxing Zhang 00:09:14 Okay… So, maybe we can start…
The first one, instrument management model.
So, Pressman, do you want to start… start this new, discussion?
Przemyslaw Delewski 00:09:34 Yeah, so I think that regarding this first point, mine…
The main thing is how we should define these, you know, hooks. Should we do this in YAML, or maybe should we do this in Go?
Or maybe we should have both things, so to have Go internally as a kind of internal representation, and maybe YAML on top of that.
And, the domain… my main concern is that
I think that about a year from now.
almost all these instrumentations or role preparing will be done by LLMs.
So…
It means that LLM can… if you say to LLM that you would like to instrument your application in this way, the LLM will prepare you all the rules. And currently, we can't express in YAML everything what we would like to express.
And, so it would mean, for instance, that LLM would need also to, change something in the tool itself, which is much harder. So…
I would like to have some way of specifying
all these rules in a kind of DSL, in embedded DSL, so, for instance, in Go.
And then maybe on top of that, have a YAML to… that could be… that could be used for describing
you know, these simpler rules. That's… My opinion, my idea, and…
Yeah, we can discuss that now. What do you think about it? But there are also other things, as you can see here, how people rewrite this test and document these things.
And, yeah, there is also governance and so on, so…
Huxing Zhang 00:11:51 Yeah, I think currently we support by writing the rules in Go, I think.
And, in the implementation of our, existing.
Alibaba's approach. We use the Go because we think that it's more convenient for the developers, and it's very natural, it looks more natural to their… to them. And I agree with you that this can be a
way that LM can easily, know, and maybe it's friendly to LM, because he knows how to write code in Golan, and it's.
Przemyslaw Delewski 00:12:36 Yes.
Huxing Zhang 00:12:36 for the LM to, implement, customized, rules.
My question is the… what do you think of the scenario of using YAML? What is the advantage of using that over, code?
Przemyslaw Delewski 00:12:57 Hmm…
I don't know, we decided that at the beginning, but maybe we don't need to use YAML. It seems simpler at first, but, you know, these simpler rules you can also easily define in Go itself, so…
I don't know, that was some kind of decision that we made at the beginning, and but I didn't know
That you, in Alibaba, use also Go as, kind of, description language.
Huxing Zhang 00:13:32 Yeah, I think the aux trian supports YAML.
Przemyslaw Delewski 00:13:36 Oh, okay.
Huxing Zhang 00:13:38 why we have that.
Przemyslaw Delewski 00:13:39 Okay.
Huxing Zhang 00:13:43 the… If we want users to migrate.
for easier migration from their own implementation to this OpenTelemetry one, maybe we should support both, I think, for the…
Convenience of their existing implementations to migrate better, easy, easy, migration from the…
a company's approach into the OpenTelemetry, a approach.
So… Maybe then later we can see which one is…
Better for the user, and we will decide how they will go in.
Yeah, that's my thought.
Przemyslaw Delewski 00:14:37 So, you know, if you only need this kind of transformational rules, that where you want to inject some functions before and after, then YAML will be probably enough, but if you need something
More sophisticated, then it will be harder to…
Or even impossible to describe that in YAM.
Huxing Zhang 00:15:03 Right.
Przemyslaw Delewski 00:15:14 So, and one more thing to this point, because, of course, if we decide that we would like to check this go direction, so use some kind of DSL,
GoDSL or any other way, we should, you know, this will require some effort to prepare some kind of API we can
We can use some ideas from this project that I mentioned on the Slack, or we can use also ideas from Alibaba, so…
Or we can… Build something new together, you know?
Yi Yang 00:15:52 Sorry, sorry to Tim. Do you mean… do you mean we don't need, YAML plus Go combination, and we can use the pure Go code?
Instead.
Przemyslaw Delewski 00:16:08 Yes, I think that we can use PureGo.
Or maybe have, you know, maybe have YAML on top of that.
Yi Yang 00:16:18 Oh, okay. For example, we can use register.go to… to… to replace the YAML configuration.
Przemyslaw Delewski 00:16:31 Okay… Do you have any examples of that, what you're talking about?
Yi Yang 00:16:39 I, I just want… I just want to…
I just want to make sure, I'm aligned with your, ideas.
So, so, do you suggest that we, we use pure… we write some pure Google code to, to register, we register hook rules? For example, we… we can write a register
And pass some parameters to… to… to specify what function we want to instrument and, and where we can fund our instrument to code.
Sorry.
Przemyslaw Delewski 00:17:19 Yes, so… So… Something like that. You know, the ideas, you can find some… my ideas.
In this, rationale that I've sent, so…
Xabier Martínez 00:17:39 Can you potentially gates?
Huxing Zhang 00:17:41 Or…
Przemyslaw Delewski 00:17:42 I can share the screen for a moment, so…
Yi Yang 00:17:45 Okay, okay, that sense.
Przemyslaw Delewski 00:18:05 So, I hope you see the screen.
Huxing Zhang 00:18:10 Yeah.
Xabier Martínez 00:18:10 Yep.
Przemyslaw Delewski 00:18:11 So my idea, you know, was to use some kind of DSL, and so I have a DSL here.
You can look… Huh.
Sorry… I mean, not this way.
So, there is a kind of library?
the API is, you know, is defined here in this very small package, and now with using this, you can define something like that. This is more or less what we have currently in YAML, so we can define…
Where we should inject, there is a kind of inject target, there is package function, and we say that we would like to inject something before and after.
And from which package, right?
And now we have functions that we will be injecting.
Before and after, and that's it. So that's basically what we have in this basic rule in YAML.
Huxing Zhang 00:19:16 Wow.
Przemyslaw Delewski 00:19:16 But… But using this language, this DSL,
We can also, you know.
describe something more sophisticated. So, for instance, I also described, runtime, so…
This is what currently we have in OpenTelemetry.
You know, runtime instrumentation, but part of that we have in the tool.
Enter… Here, we have, I have the same description, but only in this Hooke's DSL language.
And the tool itself doesn't know about that, so it uses this instrumentation as a plugin. And I can, you know, I can run also…
Maybe this tool just to…
Just to show you…
So, this very simple project that I have here, I can…
Say that I would like to instrument this.
project with two packages. First.
There is these hello hooks that will be, you know… there are a few functions, full, bar, and so on, and all these functions will be instrumented with these rules before and after.
But there is also runtime, as I was showing you, so I can choose that, and then the tool will… this compiler, hook compiler, will take these two hooks
These two destinations, these two programs.
And we'll use them to instrument the binary, and this will be instrumented with a runtime hooks, as I was showing you, the definition, so we can look at the work directory, what we have here. And there is a main function.
So, main function instrument that looks as follows.
And then there is also a package here for runtime, and we have, all these files, runtime2.go, and so on, and they are, you know.
instrumented in the way that we have, more or less in the OpenTelemetry now, but I am using, you know, these rules from this Hooks DSL. Now, when I will run it.
You can see that this…
Before and after functions are executed correctly, and also context should be propagated correctly according to this runtime instrumentation.
So, that's what I did here.
And that's my idea, more or less. So, you know, you have… I extracted everything, what we have currently in the tool, into the… this…
hook instrumentation, hook runtime instrumentation, so the tool don't know, doesn't know about that, about this instrumentation.
It only uses this as a plugin. So, for this compiler, this low code is a kind of,
You know, program that he needs to use in order to instrument your program, taking the rules from these hooks.
Cook definitions.
Xabier Martínez 00:22:51 I like that idea. I know if it's possible just to have, a pull request with…
This, like, not the whole book, but just, this part.
I think that, it's also interesting, because we can expose,
as it's just go code, we can expose some, for example, thinking that we can dash
the instrumentation packages, because maybe I just want to instrument, the databases.
So we can export those types, so it's easier.
Przemyslaw Delewski 00:23:30 Yes.
Xabier Martínez 00:23:31 people to tag, also, the instrumentation packages. So, I think it has a lot of benefits, and I agree that we can move with this.
My question is, also, are we going to…
wait to have this implemented before adding new cementation packages to the project?
Przemyslaw Delewski 00:23:58 So… if I understand correctly, your question is about having that,
In the project, before we prepare any other instrumentation, right?
Xabier Martínez 00:24:11 Yeah, like, is it going to be hard to refactor, if we start adding new instrumentation packages?
Przemyslaw Delewski 00:24:19 Yeah, so, I think it would be good, you know, to decide now, or have some consensus, if we should go this way.
And, because otherwise, we will be doing some redundant work, maybe, maybe, maybe. Because, at some point, maybe it would be also possible, you know, to use LLM to rewrite the… all the definitions that we have now to the new one, so…
Maybe that's also an option.
Xabier Martínez 00:24:53 Yeah, we're gonna start with that. The idea is to use them as…
an independent package from the tool, no? Like, the tool will import Don't.
Przemyslaw Delewski 00:25:04 Yeah.
Xabier Martínez 00:25:05 I bet.
Przemyslaw Delewski 00:25:05 Yes.
So, if you know, if you like this idea, if we will have consensus, I can start working on pull requests for that.
To show you how it will look like, you know, in the tool itself.
So, maybe to have some draft.
Xabier Martínez 00:25:27 Yeah, I think so, because it will tackle a couple of problems. The first one is the DSL one, and the other one is to have splitted the packages, like instrumentation packages from the tool itself.
Przemyslaw Delewski 00:25:43 It… yes.
Xabier Martínez 00:25:44 So we can handle both things in that period.
Przemyslaw Delewski 00:25:51 Yes, but still it would be good to have very… you know, to do that step is… by step, you know, to have very…
Xabier Martínez 00:25:59 Yeah, yeah, yeah.
Przemyslaw Delewski 00:26:00 Small, small PRs as possible.
Xabier Martínez 00:26:05 Mmm…
Przemyslaw Delewski 00:26:07 And one more thing, the DSL that I presented, of course, the API might be different, because that was my just proposal, you know.
Xabier Martínez 00:26:20 Yeah, but it would be good to have the PR, so we can discuss there with the code.
Przemyslaw Delewski 00:26:26 Yes, that's for sure. At least that's a good starting point.
Xabier Martínez 00:26:33 Yes, we can split afterwards the work or whatever, but
then we can wait for that PR.
Yeah. However, yeah?
Yi Yang 00:26:46 Hey, go on, go on.
Xabier Martínez 00:26:49 Yeah, I was thinking if there is,
What we can push in parallel with this, because this is, like, a key, refactor.
So, just to know if we can put something else in parallel.
But we can wait to see the rest of the bunch first.
Przemyslaw Delewski 00:27:13 Hmm… I don't know, maybe we can think about that parallelization offline, and
if someone will have some ideas how we can parallelize that, we can also, you know, offline mention that on Slack, or something like that.
Huxing Zhang 00:27:41 My question is, if we do that way, and, for our existing, like, instrumentations, will that take,
How much effort would it take?
To, like, migrate because, we…
We have actually, in Alibaba, project, we have a lot of instrumentation already.
Przemyslaw Delewski 00:28:03 Go ahead.
So, my opinion is that if we will have an interface, then I would try to use, you know, LLM to take this, all this instrumentation, and to try to migrate that by LLM.
And if L&M will have some problems, we can also see if… where these problems are, you know, because maybe there will be something not enough in our APIs, or something like that, maybe there will be other problems.
But in my opinion, LLM can do that very effectively, so that's one idea.
Huxing Zhang 00:28:44 Yeah,
In my opinion, I still want to, like.
shall we, propose it officially on the GitHub issues, and, write a proposal of describing the, like, rationale behind and the difference between the current approach and the proposed one, and we can,
For, more people can…
come and, like, discuss, make a final decision before we begin the final decision.
Przemyslaw Delewski 00:29:16 Yes, so that's a good idea, and I can take over that. So, I can prepare an issue.
And with maybe some initial description, some, you know, I, I will…
put there my initial, let's say, API or something, or initial design, and then we can discuss that.
Huxing Zhang 00:29:41 Yeah.
So, I will write down an action we have here.
Przemyslaw Delewski 00:29:52 I think that, Kushing, maybe you can, you know, share this.
Huxing Zhang 00:29:56 Oh, I forgot that, sorry. Yes.
Yeah, our right, action here is that the pre-prepare GitHub.
Hmm, an issue to describe the… idea of DSL approach?
Right.
Przemyslaw Delewski 00:30:21 Yes.
Huxing Zhang 00:30:25 Okay… Okay.
Okay,
We can move to the next, I think. Shall we describe all the topics here, or just this one?
Przemyslaw Delewski 00:30:45 I'm not sure if we are ready for the, you know, discuss… Third and fourth point now.
I don't know what's your opinion, because maybe it's too early, just, you know…
Huxing Zhang 00:31:01 What, what are… what are you talking about? Sorry.
Przemyslaw Delewski 00:31:04 I'm talking about how people will write tests and document instrumentation. Probably it's too early, you know, to… for now, if we… if we will have this new approach.
then… And now discussing that might be too early.
Huxing Zhang 00:31:21 Yeah.
I think it works to create an issue first, and maybe we can discuss.
Next meeting, or… yeah, let's see if… how people feel about that.
Przemyslaw Delewski 00:31:37 Believe me too, huh?
Okay.
Huxing Zhang 00:31:46 So, do you have any other things to discuss here about this?
Przemyslaw Delewski 00:31:57 Not from my side.
For now.
Xabier Martínez 00:32:04 No, I think we can move.
Huxing Zhang 00:32:06 Put the next one.
Okay, instrumentation scope… So…
Przemyslaw Delewski 00:32:15 So next thing I… next topic, I think, is much… very related to the… to the first one, because it depends somehow on…
In my opinion, how we will, you know, define this new DSL and so on.
Of course, we can, nope.
The work with what we have now, so try to define or, you know, migrate this instrumentation to the current approach.
And use current approach, but…
I'm not sure if that, as I said, if that will not be redundant in some way.
Huxing Zhang 00:32:56 Okay.
Przemyslaw Delewski 00:33:01 I don't know what's your opinion, because maybe you have different opinions.
Huxing Zhang 00:33:05 Yeah, my thought is that we want
move this project forward. And, we can…
do some refactoring. To my opinion, this new approach is like a refactoring or migration of the existing approach, so…
I… I would like… in my opinion, I would like to move things… Forward with the current
solution or implementations. We can add some…
Przemyslaw Delewski 00:33:38 Okay.
Huxing Zhang 00:33:39 At least, one instrumentation for the big…
key big areas, like SQL, NoSQL, or…
net, HTTP radius, or like that. We actually… so we can cover the key components of, application that, might be… depend on, and this makes our solution more, complete, and, more…
In a good… better shape than towards the…
A complete solution, you know, in my opinion.
And we can discuss, in the meantime, we can discuss, if there's a better one that can be replaced the existing approach, and we can do the migration
In parallel, I think, maybe.
Przemyslaw Delewski 00:34:30 Okay, so, yeah, so then, yeah, then we can work in parallel, so…
Some people can work on, you know, on preparing this instrumentation in the current… using current approach, and then…
you know, for instance, I can work on this new approach, proposal.
Huxing Zhang 00:34:51 Yeah.
Xabier Martínez 00:34:54 Yeah, I think that migrating… That's my rating from,
one implementation to another shouldn't be too hard. In the end, there are, like, fix structures.
So, like, we are just moving from a YAML to a…
Go and fix a structure. So, in the end, it should be easy to migrate.
Dario Castañé 00:35:20 Yeah, also… as… as Datadog, we were planning to work on the…
on the instrumentation for specific libraries this quarter, so we don't mind to start working with the YAML and then migrating as
it was mentioned before, using LLMs to the new DSL, but by the way, it looks great, the one that you showed.
Przemyslaw Delewski 00:35:42 Okay, thank you. So.
The, the one important thing is, you know, when we will be doing this work, to, to…
In preparing instrumentation for all these kind of libraries, it will be very important to…
to know if we will need something like a change in the tool itself, because maybe we will not be able to express that in the YAML, and then we will need to prepare some fix in the tool itself. So that's very important for me, because I need to
You know, to be aware of that, to prepare.
Or maybe think how we can express that in this DSL.
Huxing Zhang 00:36:29 Yep.
So… Okay, I'll write it down, keep the current.
And, discuss… the SL.
In parallel.
Okay, I'll read this, and it's not a very… it's not a clear action item, but, right on the conclusions that we have.
So, talking about the instrumentation scope, so, currently we have GRPC, then HTTP. We can… we can discuss the… what…
Next, we can do.
I think, yeah, the detail, like, a high, like, high priority…
Libraries that we want to instrument.
Przemyslaw Delewski 00:37:44 I don't know.
Maybe… because,
You know, I'm currently not working with the users that are using this instrumentation, but maybe, from your perspective, you know some knowledge about that, some data.
Huxing Zhang 00:38:01 Yeah, yeah, my message is since as you, someone written here, ready,
my SQL, SQL and, possibly messaging, like Kafka, or… will be the most, active, dependent, libraries that, application might…
Yeah, my dues, and we can work in towards that.
So what, what are your opinions about that?
Przemyslaw Delewski 00:38:46 From my perspective, everything what is related to databases might be interesting, so…
Red, this is a good…
Good idea.
Huxing Zhang 00:39:04 Yeah, I think we can add the one… and a Kafka here.
Yeah, though.
Dario Castañé 00:39:13 Golden standard of this kind of…
Integrations are usually Kafka, databases, NetHTTP, as we already have it, gRPC.
Huxing Zhang 00:39:23 But I think we already have it too.
Dario Castañé 00:39:29 And do we have any kind of information, telemetry, anything that we can use?
OpenTelemetry?
Regarding what are the most common…
Libraries used by the… by the customers.
Przemyslaw Delewski 00:39:46 I don't have such knowledge, so…
Huxing Zhang 00:39:48 Yeah, I don't think we have some information from our telemetry side.
Dario Castañé 00:39:53 maybe a survey or something like that, that would… maybe a survey that those that are done around Go, that might be a good source of information about what
Libraries we should prioritize, too.
Huxing Zhang 00:40:07 Yeah, we can actually create an issue in GitHub and let people vote, maybe.
Xabier Martínez 00:40:18 That's a question.
I don't have too much context about your previous project, But,
What are the changes that we need to do to your current instrumentation packages?
Like, you are already…
instrumenting Redis or MySQL in your project? Like, can we export directly that? Like, it's working and tested?
So, like, why not create a plan for, like, taking everything and moving to this project?
Huxing Zhang 00:40:58 Yeah, I think that's what we are…
thought, we are thinking about, and, I think the migration effort won't be too much effort there, and, because there's, quite a lot of, like,
several, like, 20… like, 30 or 40, I think, there, but we can't do it, at once. We can't…
prioritize some, instrumentations first, and then we can do it, others later. So I'm just trying to pick up the most, valuable or, like, the promising instrumentation that looks,
good to users, so what I'm proposing is that, actually, we want to migrate as much instrumentation as possible, but, I… from my point of view and the
Alibaba instrumentation and the, Deadog one, they are some difference, because, the developers in China or in the US, they may
Have used different, popular open source
project. So we are… we're actually focusing on…
more developers that, in China, and maybe they use different frameworks. So, we can focus, on them, these, these, instrumentations first, and, maybe Dadog can contribute, some, instrumentation from,
developers that are mostly used in U.S. or in Europe.
And, so we can have a more…
Like, a bigger one, support, a big support, support scope.
That's what I'm thinking about.
Xabier Martínez 00:42:56 Okay, but in the end, the change will be minimal, no? Like, the effort required for migrating a package.
Huxing Zhang 00:43:03 Yeah, yeah, I think so, I think so, and we can definitely try to, like, to try to do that.
Xabier Martínez 00:43:12 No, I see it okay just to start my routine first, some of them, but I wanted to be sure that.
Huxing Zhang 00:43:18 Yeah.
Xabier Martínez 00:43:18 Yeah, and you are going to, yes.
Move the… all the logic that you have, all the packages, to here.
Huxing Zhang 00:43:24 Okay.
Xabier Martínez 00:43:27 Mmm.
And also, regarding how we are going to Like, the structure of, on the package itself?
Are we going to require to have some kind of tests, or format, or…
Oh…
Oh, I, like…
for example, we have right now, for HTTP and GRPC, some end-to-end tests, integration tests, and so on.
Like, are we going to enforce, to have those kind of tests for all packages?
Like, which are the minimum requirements for a 13 instrumentation package?
And if we are going to follow a format.
Huxing Zhang 00:44:18 Sorry, your question, if I'm understanding right, you are looking for, like, a practice, how we can
Write a test case, test for the instrumentation.
Xabier Martínez 00:44:34 I'm correct.
Yes, like, thinking on a person that wants to create a new instrumentation package for a library, without too much context about this project.
we'll have, like, okay, the new DSL structure, with the hooks.
But then we need to ensure that that's working correctly.
So, we need to provide some kind of framework for testing that easily.
So, I don't know, that would be interesting also, because if we need to review those, packages.
at least we need to ensure that it's working correctly. And the best way is to create some kind of end-to-end test, something like that.
But maybe we can standardize those tests.
For all, like, I know, like, some kind of structure.
Because if not, maybe it's a bit,
Confusion, like having 30 libraries and, like, 30 packages, and each package being tested in a different way.
Huxing Zhang 00:45:45 Yeah, I think that's a good idea for, you know, standardized test.
Like, framework providing… you're talking about providing a standard testing framework to test a different kind of library instrumentation, right?
Yes,
I don't know if we… I don't think we currently have someone, and then if you are interested, I think you definitely can…
working on that, and, provide such things. I think that looks, very good for me.
Xabier Martínez 00:46:21 Yeah, I will create the issue and discuss that.
Because my idea, like,
you can run, like, whatever service you want, like an HTTP server or a Redis, but at least we need to ensure that
the spans are being curated correctly with respect to attribute, so all the tests will have, like, same kind of assertion.
Huxing Zhang 00:46:49 Yeah.
Xabier Martínez 00:46:50 But, I will try to create an issue describing all this.
Przemyslaw Delewski 00:46:53 Okay.
Huxing Zhang 00:46:55 according to my knowledge, in, like, Java instrumentation, Auto Java instrumentation, yeah, we have
kind of abstract, like, abstract layer of testing that we can verify each, like, span attributes are there, and they are in exact, we…
order or in the, right, content that we have. So, including, spans or metrics, I think there are some abstract layer for that. Maybe you can take a look at the.
Yi Yang 00:47:34 Java instrumentation to…
Huxing Zhang 00:47:38 Try to find something you can, like, maybe you can learn from that.
Xabier Martínez 00:47:43 Sure, if you come… put, later the link to that.
Huxing Zhang 00:47:50 I will put… put that down.
I'm not writing, create an issue…
Yi Yang 00:47:59 2…
Huxing Zhang 00:48:01 Tandem… stone.
Yeah, and I'll just… I will put the link here.
So, yeah.
I will assign to you.
Okay.
So, shall we move to the next?
Top tweak.
Xabier Martínez 00:49:04 Maybe we can discuss the vocal contriv.
Huxing Zhang 00:49:09 what?
Xabier Martínez 00:49:10 There.
Like, I don't know, what do you think about that?
Because OpenTrift provides for example, the HCP instrumentation.
For open telemetry, and we are, like, generating our instrumentation. So…
I don't know if there is a way. The gold contract is not prepared, so we can consume it, but I don't know if we can talk with them.
Because in the end, we are just, like, we are providing the tool for instrumenting.
But in my opinion, it would be great if we can reuse the main logic that is already developed for instrumenting an HTTP
Server or client, for example.
Huxing Zhang 00:50:08 Yeah.
I think we did… we have discussed this in the previous, in the previous…
meetings, and, I think the KMO has provided the idea that
eventually our instrumentation will be, like, separate with the tools. They are… maybe there will be…
Two, projects, and, In the… in the go-to contribute can be, possible…
One, or we can… Create another repository to put the instrumentation there, and the idea is,
we can… we can use this, instrumentation both for SDK or compile time. They… they can use… the developers can choose whether they use, use. So, if we want to achieve that, maybe the instrumentation
It's better for the information to be, like, a separate repository.
With the current… current rotten one. I think…
Przemyslaw Delewski 00:51:24 Yes, but I think that this is more about preparing rules that will be… that can be used to, you know, to use GoConTrip. Is that correct, Xavier?
Xabier Martínez 00:51:37 Yes, I'm not sure if the change should be in our site or their site.
I'm not sure, but from a developer perspective, like, I'm using GoConrieve, and…
Przemyslaw Delewski 00:51:55 Yes.
Xabier Martínez 00:51:56 some logic for instrument in my server, and suddenly I change to this.
And it's also under OpenTelemetry, but now the implementation running in… for my service is different.
So maybe the behavior in the end is going to be different, and that's something that I wouldn't like to experience.
Przemyslaw Delewski 00:52:17 Yes, but for me, this alignment means, you know, this… to have rules for using GoContrict, but…
The other question is where these rules will be, you know, in the repo. They can be in the country, they can be in our tool repo, or they can be in the other repo. So that's the other question for me.
In fact.
Xabier Martínez 00:52:44 Hmm…
Przemyslaw Delewski 00:52:47 So, first point is to have these rules, you know, to, to… to, to use… Go country.
Xabier Martínez 00:52:56 But can we do it right now? I think not, like…
we can't use them directly, because of how our instrumentation is working. Like, we need the before hook and after hook.
And the logic for instrumenting an HTTP server, for example, is not prepared for.
Przemyslaw Delewski 00:53:16 Yeah.
Probably, we are not prepared for, for, you know, for this alignment.
But, this is probably because our language to express all these things is not good enough.
Maybe there are some other issues that we will, you know, experience, but I think that we have to start working on that to see what is needed.
Xabier Martínez 00:53:47 Maybe we need a different kind of rule, or… yeah, we need to… We need to see.
Przemyslaw Delewski 00:53:56 That's also something that we can, I think, do in parallel, so…
Maybe someone can look at it and try to, you know, To prepare this alignment.
Huxing Zhang 00:54:12 Yeah, another idea is we can talk with the guys, folks in the Go Country maintainers, to see what if their thoughts.
Przemyslaw Delewski 00:54:24 Yeah.
Xabier Martínez 00:54:30 Okay,
Let's create an issue first, maybe in our site, to discuss, like, our ideas, and then we can propose.
Huxing Zhang 00:54:39 Those ideas to them.
Xabier Martínez 00:54:41 To see the… Because it would just go with an open question.
It could be harder, like, without giving them more context.
Przemyslaw Delewski 00:54:53 Yeah, yeah, yeah, that's a good point.
Huxing Zhang 00:54:55 Yeah.
So, Shabbert, would you like to work in on that?
Xabier Martínez 00:55:01 Yeah, I will create the issue, and… and try to take a look.
Huxing Zhang 00:55:15 Okay.
So we are… I think we are finished here, right?
Przemyslaw Delewski 00:55:26 Yeah, I think so.
Huxing Zhang 00:55:30 Let's move to the next one, tuning.
Przemyslaw Delewski 00:55:35 Yeah, so this is… this point is about, this kind of tools that I was showing you.
If you… if we would like to have something like this, you know, this kind of IDE, where you can look
how the instrumentation, final instrumentation looks like, when you can look, you know, you can debug this code, and so on. So, that's the question, if we would like to have such thing in the… in OpenTelemetry.
Huxing Zhang 00:56:08 So you mean the tools that you just showed?
Przemyslaw Delewski 00:56:12 BS.
Huxing Zhang 00:56:13 Yeah, that's definitely a very interesting point to me. I think we are more than welcome to have that in this project, I think.
Przemyslaw Delewski 00:56:26 So then I can, you know, prepare issue for that, and, start working on some…
Huxing Zhang 00:56:33 draft PR.
Right, let's… That's fair.
Przemyslaw Delewski 00:56:37 So you can create an action item for me for that.
Huxing Zhang 00:56:43 Okay…
the… None.
212… project, I think. Maybe… my…
Do you have a name of that tool? What do you want to name about that?
Przemyslaw Delewski 00:57:26 No, I don't have yet, so…
Huxing Zhang 00:57:28 Okay.
Przemyslaw Delewski 00:57:29 This will be some kind of IDE,
I don't know, maybe we can think about that later, maybe.
Huxing Zhang 00:57:37 Okay.
Yeah, more to go really into ideas, that's what.
Przemyslaw Delewski 00:57:45 This is prob- this is probably something that we discussed that.
Huxing Zhang 00:57:49 Yeah, yeah, yeah.
Przemyslaw Delewski 00:57:49 The first topic, you know.
Huxing Zhang 00:57:52 Okay, the last one… release…
the release, the schedule, I think. I think we have this… want to discuss this. Shall we have, like,
Regular release, like, monthly ones.
I think that, keep a good, release,
Pace will be good for the developers.
To know about our progress.
Przemyslaw Delewski 00:58:28 Yeah…
Huxing Zhang 00:58:30 Yeah.
Przemyslaw Delewski 00:58:33 I think that's a good idea.
However, I'm not sure if every month we will have something, you know, that will be…
is able to… something new to the user. I'm not sure about that, but still, there will be probably some fixes and so on, so it's good to have.
Regular releases, in my opinion.
Huxing Zhang 00:59:01 Yeah, but if we can not do monthly, we can do one or half or two months.
One… yeah, just to, to… I don't… I think we can discuss, yeah.
Przemyslaw Delewski 00:59:17 Yeah, yeah.
Yi Yang 00:59:19 Yeah, we, we haven't, we haven't, released the first major version, version, so we… I think we can… I propose we can, release monthly, as they are not very, very important, just to… just to show that we are.
Move, move on, move forward.
Przemyslaw Delewski 00:59:43 Yeah, I agree. So, maybe…
Yi Yang 00:59:45 Yeah, and I've already created the automated release pipelines, so we can easily push a tag monthly, and they and the pipeline will… will release a new, we'll publish a new release.
Przemyslaw Delewski 01:00:04 So, maybe we can start with monthly releases, and then if something will…
Not work, we can change that.
Huxing Zhang 01:00:12 Yeah.
Yi Yang 01:00:13 Yeah, yeah, I agree.
Huxing Zhang 01:00:22 So, I think we can decide the, like, release… how to say, release manager of that. We can…
like… Have different release measures each time.
So, I will put on… so, if we… if you're someone who He's willing to…
I'll be a risk manager, we can… I can put, like, a note here, and we can…
Yes.
Decide who's the next release manager.
Przemyslaw Delewski 01:00:58 Okay.
Yi Yang 01:00:59 Yo, you, you can put me, initially.
Huxing Zhang 01:01:04 Yeah.
Okay.
Okay. Any other one would like to… be in this list.
Przemyslaw Delewski 01:01:32 I can be also a Reece manager.
Dario Castañé 01:01:36 Yeah, me too.
Huxing Zhang 01:01:38 Yeah, so… So I, I will… I will put all the… maybe the maintainers plus the… the… approvers?
In this one, if everyone's no oblique, no… obligation to that.
What do you think?
Przemyslaw Delewski 01:02:06 Yes, you can do that,
But I think at the beginning of each month, we need to know who will be the release manager, right?
Huxing Zhang 01:02:19 Sweet.
to…
Okay, so…
So, maybe we already have three, and maybe we can put it in the next meeting, we can discuss the other candidates, because of the time is…
Przemyslaw Delewski 01:02:51 Here, maybe we… Yes.
Huxing Zhang 01:02:53 Yeah.
Finish today's meeting.
Przemyslaw Delewski 01:03:00 Okay, thank you very much.
Huxing Zhang 01:03:02 you…
Dario Castañé 01:03:03 Thank you, bye.
Xabier Martínez 01:03:05 Thank you.
Przemyslaw Delewski 01:03:05 Next time, bye.
Huxing Zhang 01:03:06 Phoenix.
Yi Yang 01:03:07 To yours, bye-bye, bye-bye.
