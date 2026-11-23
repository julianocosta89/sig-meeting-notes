SIG: GenAI SIG
Date: 2026-11-17
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

Liudmila Molkova 00:05:30 Hello, hi everyone.
Tammy Baylis 00:05:35 Hey, Ludmila, hi everyone.
Pam Dixon 00:05:40 Hi there!
Shuwen Pan 00:05:42 Boom.
Liudmila Molkova 00:05:48 Let's give people a few minutes to join.
And in the meantime… Let's see if we can… Put things on the agenda.
Okay… If you have anything, please add it there. Please add your name to the attendees list.
See, we have… Lew items from the past… Oh, while we're waiting, a quick recap, if you… Haven't been to the KubeCon, we had a good… a discussion in person with the… for the office hours at KubeCon.
We talked about a few different things, like what… Have we done, in 2026, the stabilization efforts?
There is a proposal from Google around the Agent Trajectories ATV2 format.
And, there is interest in making it play nicely with OpenTelemetry, and we talked about this.
And I saw there were people from OpenSearch. I hope they were able to join.
Or maybe we'll be able to join this call at some point, because turns out they've been using the old.
Zoom invite.
It was old meeting information, but they brought up some interesting ideas for the evaluations, where They would like to collect more information for the, the relations SDK used inside test suites.
And some additional information about the test cases.
Okay… Trask, I wasn't able to join yesterday, it seems you were, thank you.
And, is there anything to call out here?
Trask Stalnaker (Microsoft Corporation) 00:08:23 Yeah, Steve had kind of a question about, evaluation systems. I think, it was… Getting at, like, say you do evaluations… say you have a next… another evaluation system, and that's already storing your evaluation results.
and whether… the evaluation… Result event should still be emitted in that case?
And… Sort of the… rough advice I gave, but I, sort of bring it here, like, in case other people have, experience with this type of… evaluation system that's already storing that result.
Was that, like, I guess in some cases, it sounds like some observability vendors are doing that already, doing, like, integrated evaluations, and in that case.
Right? They're already integrating the telemetry and those evaluation results, so, you know, maybe there's not Need for the evaluation result.
But in other cases, like, you still want that to be… like, it's nice to have that all in your observability system correlated with your, Evaluation result events.
And so, it seemed to make sense to me to… Emit them still.
Liudmila Molkova 00:10:10 Yeah.
Cool.
Josh Bonczkowski 00:10:14 as an observability vendor, I would agree with that. Or the… a lot of customers want that single pane of glass, so it makes sense.
Actually, as you're going through it, I was trying to think of… I don't think this… Beck has a link back to the original source, like, trying to link your observability vendor back to the original evaluation, that was the third party. I don't remember if there was actually… is there a remote link on the event?
Liudmila Molkova 00:10:41 The link to the…
Josh Bonczkowski 00:10:43 So…
Liudmila Molkova 00:10:44 System that did the evaluation.
Josh Bonczkowski 00:10:45 Exactly, right. Which takes you out of scope, it's no longer a single point of glass, but giving you the reference is kind of handy, if it's available.
Liudmila Molkova 00:10:56 Yeah, I think there were discussions, but and maybe there were some ideas, but we didn't… Ever documented this.
Yep. This would be an interesting challenge, because… Ideally, the event is emitted.
Correlated with what's being evaluated.
If you know the context, And then… How to record another context on the event is an interesting question.
Josh Bonczkowski 00:11:26 Yeah.
Trask Stalnaker (Microsoft Corporation) 00:11:33 And then the other question that, Steve brought up was, about… the, and release plan for the GenAI Symante Convention Repo.
Liudmila Molkova 00:11:50 Yeah, I think we've been… We didn't do the release because we didn't want to give people something they would depend on that we know that will break.
And we were going to do a release once we have, we're ready to call the RC.
We can't spend some time thinking how far we are from this, and… I think, Trask, you have this awesome issue.
Trask Stalnaker (Microsoft Corporation) 00:12:31 Yeah, and I mean, we can… well, we've got time, but, I could also try to prepare something for tomorrow's stabilization meeting.
This is not fresh in my brain.
Liudmila Molkova 00:12:48 Yeah, and maybe it's good to just briefly… Go through it here, that… And get, like, people's opinions, on this, that it sounds like we're… We are moving towards The first release candidate, and after the stabilization for this four operations, and corresponding span duration, the metric and exception event.
Oh, we probably… should we include the usage? We should include at least… Some of the usage here, right?
Trask Stalnaker (Microsoft Corporation) 00:13:31 The usage metrics…
Liudmila Molkova 00:13:33 Yeah.
Trask Stalnaker (Microsoft Corporation) 00:13:34 Yeah, but I think that's in scope.
Alright. Stabilization.
Liudmila Molkova 00:13:40 Yeah, so… Almost everything that's concerning this, these four operations.
And it sounds like… This is a list of things that we need to tackle, some of this are done, but it sounds like these friends are not in the scope, it doesn't mean they will never be stabilized, it's just that they're not in the first wave.
Okay.
So, are we still comfortable holding the RC for a little bit longer? And I think what we discussed during KubeCon is that we'd like to have the RC by the end of the year, which gives us pretty much one month, and then people will disappear.
Trask Stalnaker (Microsoft Corporation) 00:14:38 I had a question. Is the Python GenAI repo, adopting any of the new semantic inventions, or is that still pinned to the previous cement… the last semantic convention release.
Liudmila Molkova 00:14:55 Oh, it's pinned to this repo, but not to the latest version. It does not, for example, rename the metrics yet, at least not all of them.
So, it's been to some relatively recent version.
Okay. I can check how far behind we are.
Oops, sorry.
Trask Stalnaker (Microsoft Corporation) 00:15:29 So, I guess the point there is that we're, already… Sort of… Leaking out those changes, those breaking changes.
Liudmila Molkova 00:15:45 Yes.
that does it… In your mind?
mean that… we can release.
Beta, whatever, the dev version?
Trask Stalnaker (Microsoft Corporation) 00:16:06 I mean, if people wanted that, would… Yeah, I guess I was trying to… for, say, Alibaba, for external folks.
Yeah, we had kind of wanted them to stay on a fixed version, a released version, and… Not introduced lots of, you know, incrementally breaking changes, but… At the same time, I'm fine if that's what we're doing.
in Python already.
It does help us.
Yeah, it does help us to move those forwards.
At which point, it's maybe less… important to not, I mean, to hold the release.
Since backends, sort of, are already getting those versions.
Liudmila Molkova 00:17:10 I mean, there were a lot of asks to do the release.
Across different Slack channels, and also, I know that people are very confused when we go to OpenTelemetry I.O, And we go to the… Semantic conventions.
And, there is essentially no OpenTelemetry I.O. content for this.
This is… how it looks. Right. And people… I've… I've heard complaints about this.
And if we do release, before RC, we will train the release muscle, and we will figure out what to do with open telemetry I.O, and then by the time we do RC, we could do a better job, and it would be smoother.
Trask Stalnaker (Microsoft Corporation) 00:18:05 Makes sense.
Jamie Danielson 00:18:06 It will also be useful, to start having that new like, we're still planning to do a new number, like, separating the version of the GenAI semantic conventions from the main semantic conventions, right? So we'll start having our .01, or whatever it ends up being.
So people can start getting used to that… that part as well. I know one thing I've seen related to this is when people are trying to refer to what version they're using today.
They are referring generally to the main semantic conventions, but it is a little bit of confusion with the… what to do about those GenAI ones.
Liudmila Molkova 00:18:51 Yeah, and it gives us the schema URL that we can put on the telemetry.
If there are no objections to the release.
We can work on this, we can have something out.
And, I think we're done with the major renames, so at this point, the changes… I don't… I've said it multiple times, I don't expect a lot of breaking.
Every time it happened, but now I really don't.
Like, some, like, new attributes and metrics, maybe some final polishing, but it sounds like, in general, we are… That was the big refactorings.
Trask Stalnaker (Microsoft Corporation) 00:19:49 Yeah, let's, let's make that our main topic to maybe tomorrow's stabilization meeting, I'll try to… I'll prepare… Sort of an update on what's… remaining… And we can decide… If there's any other sort of renames we want to try to get in before the release.
Liudmila Molkova 00:20:21 Yeah, awesome, thank you. Surya.
Surya Teja 00:20:24 Yeah, Liudmila, we, I opened up an issue on GenAI, for porting the Workflow span, and… combining them, that with internal agent thing. So the question that I have is, should I wait till the Wivo version is updated?
So that I can bring those changes that… I forget the name of the person, but someone combined those two spans to GenAI UTL.
Liudmila Molkova 00:20:57 And Max did, but, like, why… why do we need new reverb for this?
Surya Teja 00:21:02 No, no, I was… I joined late, so I was not sure, so the question might be a dumb one, but just wanted to see if I can bring those new changes to GenAIA Util.
Liudmila Molkova 00:21:17 Yeah, it's merged, so… but, like, maybe if you want to send a PR first, that pins through the new version?
And they're… some dumb conformance tests screaming for some new things, so it just, pin the version, regenerate the… The reports and, fix… New violations, and then… We can tackle the… the… Utl changes.
Surya Teja 00:21:49 Okay, so first is conformance test changes, and then the util ones.
Did I get the sequence right?
Liudmila Molkova 00:21:57 Yeah, so, like, just pin this to the latest commit.
Surya Teja 00:22:02 Yes.
Liudmila Molkova 00:22:02 Let's see what, what breaks.
Nothing, then awesome, but something probably will. There will be some new findings, or, some things that are not findings anymore, stuff like this. Maybe we can fix some of them.
Right away.
Surya Teja 00:22:19 Yeah, cool. I got this. Look, I'll see what I can do. Thanks a lot.
Liudmila Molkova 00:22:24 Awesome, thank you.
Okay.
So we're good on this topic.
Awesome.
Okay, let's move on. Let me just close this, alex, is Alex on the call?
Doesn't seem so… The usage talking on fetch response.
Okay, so I think this is a good discussion to have, and this… this is important for… Stability as well.
So, there is this fetch response operation.
and… We didn't include tokens on this.
Because we're… we're afraid, I was afraid that people would… Get into the same problem as… I think discussed an issue… I even remember the number.
19th?
Yes.
So… Another Alex… Asked for this aggregated attribute to put on agent Spence.
the… internal agent spends, so that when… the assumption is that people would query But right Aquarius, like, give me all spans, and… Sum up the usage input tokens across them.
And it's not a bad… it's not… it's not a good query to write.
But it seems people do this.
And… we can take two paths here. The first one is, okay.
It's a… it is never a right to… Write a query like this.
Where we do all the precautions necessary that if people do this, they get reasonable results.
I think we… we've had the similar discussion with Felix.
That there is nested… there could be multiple nested inference operations.
If… if the hosted agents, let's say, are also instrumented.
And then you would be summing up across different inference calls.
And back to this one.
Trask Stalnaker (Microsoft Corporation) 00:25:39 I'm not sure how we… how we would solve for the nested inference clause.
Because, since you don't… Really even know you're… An outer inference call at that point.
Liudmila Molkova 00:25:56 Yeah.
But this… Probably is an argument.
for… You just cannot write a query like this, because this is a different operation, and you don't know how many times you would fetch the same response.
Or, if you maybe previously counted it as on the inference.
And now you're counting it again, and this is not aggregate.
So you cannot write a query without filtering by the spend type or some other heuristic.
Trask Stalnaker (Microsoft Corporation) 00:26:37 Yeah, Pam.
Pam Dixon 00:26:39 Yeah, thanks. So, it just seems, from a strictly governance point of view, that this is a query that just shouldn't be written. I don't know how that can be arranged, but it… the number of problems that are visible just right away are pretty significant.
I think the nesting, and then, of course, the stacking of inferences would be really difficult, and then if you take it over a long period of time, that could be really, really problematic.
Just… stray thoughts. Thank you.
Trask Stalnaker (Microsoft Corporation) 00:27:17 Yeah, we had thought… to try to influence people by… I mean, we can create some non-normative guidance, documentation in this repo that highly stresses that point.
basically, Trying to get, like, official documentation into the, Agent knowledge, agent, training data.
So that they know not to do this for people.
Pam Dixon 00:27:55 Yeah, I can just… I can just imagine the kind of errors that would crop up if folks did this, and then relied on the results, and just… I can just see this long trail of perpetuation of certain types of errors that would be really hard to find retroactively.
Thanks.
Liudmila Molkova 00:28:35 Okay, so then it sounds like for this PR, Solution would be to accept it.
Because it does contain usage details, and it could be useful.
And, we would have some way… we would need some way to document… That it's… Right. Way.
2 cards, tokens.
metrics… Queries that filter by type.
Trask Stalnaker (Microsoft Corporation) 00:29:28 So with this, fetch response, Ludmila, would you… for the… I'm assuming you won't get the final… token count… I mean, you would basically not capture token… you would… if you were doing this summing.
You wouldn't, over the token count on the inference call. I don't know if the inference call in this case even gets… a token count… And then, because the final token count's gonna come at the… Fetch response when it's completed.
Liudmila Molkova 00:30:11 I see what you're saying. So you would usually fetch response In cases where you… Had the async inference, and you didn't receive the result first time.
And… you would.
Need to write some custom query if you know your application does it right.
And we would not report… well, we wouldn't report the… inference token usage for this operation. We could report another metric, but it's much less interesting.
Trask Stalnaker (Microsoft Corporation) 00:31:01 Oh… yeah, I hadn't thought about how that affects metrics.
Liudmila Molkova 00:31:24 Yeah, so from the peer operation name, it would be a different metric if we introduced it.
Trask Stalnaker (Microsoft Corporation) 00:31:38 And you would have to dedupe.
Or only record it.
When you get… actually get back the full… Because I assume fetch responses… Just gives you… may not give you anything when you call it if it's not completed.
Liudmila Molkova 00:31:56 Right. So, like, the right way to write a query for this would be to get all the fetch response operations and inference operations.
I get the sum of tokens by… Sorry, the, the token… the max token count by response ID.
unique response ID. So it's doable, but it's a very complicated query.
Trask Stalnaker (Microsoft Corporation) 00:32:23 So why not, why wouldn't we record it into the inference token count?
Liudmila Molkova 00:32:32 Because it's… you can fetch response multiple times, right? For example.
I don't know, I don't store a state in my publication, and I go and fetch previous responses, and then they are counted multiple times, and by… when they do a fetch response, I don't actually… it doesn't affect my billing in terms of inference rate.
Doesn't introduce new quests.
Trask Stalnaker (Microsoft Corporation) 00:33:03 Yeah.
I guess if there was a way.
To know, though, like, semantically, it would be inference token usage.
Just reported in a different place.
Liudmila Molkova 00:33:20 Yeah, if we could dedupe it, right?
Trask Stalnaker (Microsoft Corporation) 00:33:30 Alright, a lot of, interesting questions for this VR.
I'll look at it also.
Liudmila Molkova 00:33:41 I think we at least should hold on defining any metrics for this.
Like, token usage metrics.
Trask Stalnaker (Microsoft Corporation) 00:33:56 I'm just trying to think of, like… so if you have a framework, Say that does… an inference call, and then, you know, it's doing a fetch response, and you know you're just doing that fetch response because it's async. You're just checking, waiting for it, and once you do get it, you carry on.
In that case, you're… Framework.
could… Accurately attribute those token counts to the inference operation.
Liudmila Molkova 00:34:31 Oh, I see. So you started this, and you know for sure that Wouldn't it be fair to say that when it happens, you actually have some… inference call API.
And you, you essentially instrument this layer.
Or you're saying you have means to know that you started?
users… used you to poll, and then you… you return this.
Even if it was, like, for top-level API calls.
Trask Stalnaker (Microsoft Corporation) 00:35:13 Yeah, I'm thinking less, like.
you may not be able to… probably can't… I mean, you may not be able to auto… auto-instrument an inference, library… But if you have… you may be able to… If you have a framework, an agent framework.
You may be able to instrument those inference calls at a higher level, where you're able to Tell that.
Liudmila Molkova 00:35:46 I see, so, like, the color… Can do this, either the Agent AutoTest limitation, the higher level thing.
Yeah.
Trask Stalnaker (Microsoft Corporation) 00:35:58 Possibly.
Liudmila Molkova 00:35:59 Yeah.
This is another good case for, like, Agentic frameworks instrumenting the… Another…
Trask Stalnaker (Microsoft Corporation) 00:36:06 conference calls.
Liudmila Molkova 00:36:07 The inference scores, yeah.
Trask Stalnaker (Microsoft Corporation) 00:36:37 Yeah, because it's painful to me that just because you're using an async API Suddenly, you don't get any… you don't get the most… one of the most important metrics, the token count.
Liudmila Molkova 00:36:52 It's also fair to say that they probably… the good idea for them to instrument the whole inference operation, like, everything about this operation, right?
Trask Stalnaker (Microsoft Corporation) 00:37:06 Yeah, I wonder if even the inference operation duration In that case.
Be the… until async completion.
Liudmila Molkova 00:37:19 Yeah.
Trask Stalnaker (Microsoft Corporation) 00:37:21 Matches how we would do, like, an async HTTP call.
Liudmila Molkova 00:37:29 Oh, that's interesting.
So… We do not.
Sorry.
We do not have the span type for, let's say, this.
Right?
It could be the async call.
Just to start.
And this is just the, let's say, HTTP or gRPC call.
And we don't… Have it.
Defiant. We probably shouldn't.
But then, okay, then there is no problem with suppression, because we do not want to suppress this call, whatever it is, because it's a different operation, just to start.
Trask Stalnaker (Microsoft Corporation) 00:38:25 Oh, I see what you're saying. Okay, yes, so the out… the inner… at the inner inference API, we don't have something… we don't have a… Operation for start, inference, async.
Liudmila Molkova 00:38:40 Right.
Okay, so then we probably should reflect it, maybe… In Agentic frameworks, or… Maybe somewhere in the inference page saying that if your agent does, or you call inference.
In a synchronous way, you're responsible for the Reporting this inference things.
Okay, let me… Put an action item underneath.
Aaron Abbott (Google LLC) 00:39:21 Do we know, like, the… was there a use case mentioned in the PR? Because… I… I guess, like, if you're doing… If you're doing it asynchronously, I wonder if the client library, already wraps it up And the agent needs to do it at all, or if the client… this would be text for the client library.
Liudmila Molkova 00:39:46 If client library does it, then client library is responsible for the whole entrance operation instrumentation.
But if Agent calls the library in the way that it's asynchronous, then the caller, whoever it is, is responsible for this. It's not… I don't think this is in scope of this PR. It's just the side, this question that Makes this experience better.
Aaron Abbott (Google LLC) 00:40:11 Yeah, okay.
Liudmila Molkova 00:40:16 So I want to track it in a different issue.
Yep, Pam?
Pam Dixon 00:40:23 Just a super quick question. So, if you have a federation of agents, this… I'm trying to figure out where this would set. Like, if you have a mesh.
network of agents running. Where would this kind of a situation sit? Would it be the control agent, Agent Zero?
How would that flow?
Liudmila Molkova 00:40:46 So let's say Agent A calls agent B.
Pam Dixon 00:40:51 I'm sure.
Liudmila Molkova 00:40:51 And then Agent B.
does this flow?
So the…
Pam Dixon 00:41:07 Yeah, and Agent B would be tasked with this flow, right?
Liudmila Molkova 00:41:13 Yes, the edge and B would be whoever is calling the inference.
Immediate… the immediate caller would be responsible for… for this.
Pam Dixon 00:41:22 Okay.
Liudmila Molkova 00:41:24 And by saying response…
Pam Dixon 00:41:25 Yeah.
Liudmila Molkova 00:41:26 Sorry, go ahead.
Pam Dixon 00:41:27 No, no, go ahead.
Liudmila Molkova 00:41:29 By saying responsible, I mean that if there is an instrumentation, For this, It should do this, but, like, applications, we cannot enforce them in any way.
It's just the guidance we provide.
Pam Dixon 00:41:44 Yeah, it's really interesting.
Liudmila Molkova 00:41:49 Yeah, we have the same story for… client agent calls, because the A2EA semantic conventions that were added by Surya recently, they are exactly this. The A2EA is Usually asynchronous. So you do the start, and then you get task state, or you get notified.
And then… you… the A2EA spans do not replace Agent spans, because the Agent spans are this outer layer around the A2A.
So maybe we can document it as a… As a pattern for these asynchronous things.
Aaron Abbott (Google LLC) 00:42:39 Yeah, I… I do… I do kind of think this might be used in, like, a way that we can't… like, the agent doesn't run from start to completion, necessarily. Like, I feel like part of the use case here is the kind of durable execution models, where The agent starts something, and then… it gets paused and resumes later, and then all of the state is stored, like, in the inference API.
It would be… I'm not sure if there's a good way to always implement the… The kind of bullets we put above.
Liudmila Molkova 00:43:16 I mean, if… yeah, but, like, if it's… if it's not implementable, we cannot implement it, but, like, usually it is, because the agent… you would… like… At least proxy the stream from inference to user, in some way.
Right? And if it pauses it, it's the same story as for inference library, too, when the stream is abandoned for the time.
or post.
Aaron Abbott (Google LLC) 00:43:44 Yeah.
Liudmila Molkova 00:43:57 Okay, should we move on?
So Trask, you're going to take a look at the PR, you're also going to take a look at the PR, and I'll create an issue for the… Duh.
our side quest.
Awesome. Radhika, support for setting the content capture programmatically.
Radhika Gupta 00:44:21 Yes. So I just created this, prototype, So the idea is that a lot of, users are not able to set the, environment variable, for a setting like the content capture mode.
Right now, we can only set it through the environment variable, right? So, the users want the ability to be able to set it programmatically.
So this is, a prototype which will enable them to, set the content capturing mode when they instrument any of the instrumentations. I just have taken LandChain as an example. And then this value will be passed on, throughout the instrumentations, because this will be set in the utensils.
I also saw a PR by Dylan, where he was trying to add the content capture mode in declarative config, but that PR was closed, so I wasn't sure, like, which direction we wanted to go with. I can share the PR link in the chat, I have it handy.
Liudmila Molkova 00:45:22 Oh yeah, please do, thank you.
Radhika Gupta 00:45:29 Yeah, I just showed it.
Yes, we just wanted to get everybody's opinion on what… which direction we want to take, with this.
Liudmila Molkova 00:45:50 I was kinda… Mmm… Maybe, Trask, you can help, like, in Java.
When you define where you support declarative config in instrumentations.
Do you, or through the configuration properties, do you also define the programmatic config?
Trask Stalnaker (Microsoft Corporation) 00:46:23 We… Do have, we'd… Sorry, I guess I'm not sure. You mean, do we have programmatic config, or do we… Documented… In the… yeah, we generally do have programmatic config.
Liudmila Molkova 00:46:44 And it's, like, some… something… coherent with the declarative config core and or environment variables.
Trask Stalnaker (Microsoft Corporation) 00:46:54 We'd try, yes.
It's not, like… uniformly… Defined… Like, the method names… Yes, we try.
Liudmila Molkova 00:47:18 you're… you're happy with this practice. And I don't have any concerns for this, except that, if we… if I have some prior art that… that tells that we should only do declarative, for example.
And there is some reasons not to do both.
And it sounds like there is no… nothing like this that… that would be problematic.
Trask Stalnaker (Microsoft Corporation) 00:47:42 No, I mean, honestly, we've… in Java, we've… had the… The status quo has been the opposite, because we haven't… we've been waiting for declarative config, and so we have explicitly said that other than the Java agent, where programmatic config isn't possible for library instrumentations, we only support… we've only supported programmatic config for the longest time, because we didn't want to… we were kind of waiting until we had declarative config.
And in, like, the Java SDK, for example, there's more… the programmatic config is a superset of declarative config.
Liudmila Molkova 00:48:30 Yeah, which makes sense, because you cannot represent everything with… declarative config.
Trask Stalnaker (Microsoft Corporation) 00:48:36 Yeah, also, declarative config is sort of… has to be agreed at, like, specification level, cross-language, all of that, so for the SDK, at least, there's some options that Haven't been… push through declarative config, and so… we have options there. Maybe, like, Java… some Java-specific stuff, also.
Liudmila Molkova 00:49:04 Okay.
And so then, let's, imagine we define the… the programmatic config for GenAI.
We kind of already do, we have the hook.
We have the content, capture mode.
And we have Enum for this.
And… There's some config for the hook.
Let's see what was in the Dylan's PR. Maybe, Dylan, you remember by heart what was there.
This is… Dead.
Dylan Russell 00:50:03 I had another proposal for this in the SEMCON repo I can try and dig up.
Liudmila Molkova 00:50:12 Oh, in the Simcoe GenAI, okay, maybe this, this friend. Yeah.
And it was some of the old versions of it.
Dylan Russell 00:50:22 I think I have an open issue.
Because we were considering maybe making the Content capture, like, more granular?
So you could decide, like, which attributes on which span.
You might want to opt into.
Instead of just, like, one…
Liudmila Molkova 00:50:42 Whoa.
Dylan Russell 00:50:44 Correct.
Liudmila Molkova 00:50:45 Right.
Dylan Russell 00:50:48 So… I think I have an open issue where I laid out what that could possibly look like.
Liudmila Molkova 00:50:56 Let's see… Find it.
Dylan Russell 00:51:13 The one below that, yeah.
Liudmila Molkova 00:51:26 Yeah, so I think we also, at some point, discussed, like, okay, maybe we should have something special for video, audio, and images, or some… Size limit that triggers the upload versus attribute rate.
I'm thinking…
Dylan Russell 00:51:45 Looks like…
Liudmila Molkova 00:51:45 this.
Dan, it seems in all the proposals, there is this one, global… Mod thing that wouldn't necessarily change.
Dylan Russell 00:52:05 Yeah, that's like…
Liudmila Molkova 00:52:05 Could be more, yeah.
Dylan Russell 00:52:12 Mmm.
Right, because you need to know if… yeah, if you enable it on the span or… and the event, or neither.
Liudmila Molkova 00:52:26 Yeah, and in the lack of other configuration, this becomes… the… The only… Bing.
It's like, what… what can change in the future, that we could have some… Object for config.
Or multiple properties.
And then, in theory, we could, because it's Python.
Well, we cannot change the content capture mode, but, this would be a new property.
Okay, It sounds like there is no concern with saving the programmatic option, and we probably have a path forward, and we're not stable yet, so we still have some time to… make changes if needed. What should we do? Radhika, have you thought about this? What should we do if both are provided? The… the… the… Programmatic and environment variable.
Radhika Gupta 00:53:44 So I thought, like, if we could get… give precedence, to the programmatic config over the environmental variable.
But, like, I'm open to suggestions. What do you guys think?
Jamie Danielson 00:54:00 Isn't this the general thing throughout?
hotel today, where some favor programmatic and some favor environment variables.
Are we able to… like, this right now, are we asking to set a precedence in Python, or are we asking to set a precedence at a spec level, because I think it gets trickier if we're doing it at spec level versus individual language.
Because the spec today doesn't… Have a clear… Guideline for other instances of programmatic versus environment variables.
Liudmila Molkova 00:54:41 Well, what… I don't think we're saying that it should be the spec level.
what Java does in this case… sorry, JavaScript, do you have both… do you support both programmatic and environment variables? What do you do?
Jamie Danielson 00:54:59 I haven't checked, and last I checked, we were somewhat inconsistent, which we have been trying to fix over time.
But I think that would be sort of the general thing, is like, whatever your… maybe whatever the… Language currently does.
do that, because it's, like, some languages prefer MVARs, and some prefer programmatic, just because that's the way they were set up, you know, years ago, and that's a very difficult thing to change. So maybe, like, if… If your general guidance for that.
language or that SIG or that project is one or the other, then just continue that for consistency.
Liudmila Molkova 00:55:36 What?
So, for this, it's probably, like, when it comes to Python or JavaScript, it's the GenAI OTLs that essentially decide, right? They take They read one or another.
But, like, why would anybody Prefer NVR over programmatic.
Jamie Danielson 00:55:59 Operators. Depends on what part of the stack you work from.
Trask is waving his arms.
Yeah, that's… that's the general, thing as operators. I can't touch the code, or, you know, I'm the one who is setting it at the NVAR level.
There have been extensive, debates.
on this over the years.
Yeah, because I was the same. I thought, well, programmatic, I'm right there next to the code, so I want that to be the most specific thing.
But my… Colleague who's more of an operator in his time.
vehemently disagreed.
Liudmila Molkova 00:56:50 Do we need to take his opinion here?
Jamie Danielson 00:56:55 I think the main concern at this point is really just consistency. If a language currently chooses one or the other, they should just keep the The… whatever they are… they are doing, which is not ideal.
Because they're different, but I think it would be more confusing If we did set this now, and it differed from That language's, or that project's current behavior.
Trask found the… One of the issues.
Trask Stalnaker (Microsoft Corporation) 00:57:29 Yeah… Where are we?
The spec failed to answer the question of whether programmatic or environment variables take precedence.
Liudmila Molkova 00:57:44 that they are… essentially… When it comes to declarative config, it ignores environment variables unless you put the placeholder.
Jamie Danielson 00:57:59 Right, once it's started using that declarative config file, any other environment variables are meaningless, unless they're specified within that file.
Liudmila Molkova 00:58:08 Right, which is a way to say the preference. It's not programmatic either.
Is it fair to say that if it's common for instrumentations Like, I think in Python, the programmatic currently takes precedence.
In JavaScript, we can check. I can buy an argument that if all the instrumentations behave in the same way in this language, then we should just follow this path, because otherwise it's super confusing. It's more confusing.
Jamie Danielson 00:58:45 I think we have to do that. I would love if we had decided this in the spec a long time ago, but we didn't, and so I think it's… That ship has sailed.
Liudmila Molkova 00:58:59 Aaron, Dylan, am I right to say in Python, the programmatic is the one to win?
Aaron Abbott (Google LLC) 00:59:09 I would have to double-check, but I think… I think that's true, which has been… Yeah, I've had the same discussion that Jamie was mentioning a bunch of times, so I think… Yeah, for better or worse, I think it wins if you do programmatic.
Trask Stalnaker (Microsoft Corporation) 00:59:27 Java's the opposite.
I'm a big believer in environment variables.
Oh!
Liudmila Molkova 00:59:34 Wow, I didn't expect this to be such a, like, a controversial topic.
Trask Stalnaker (Microsoft Corporation) 00:59:41 Oh, it is.
Jamie Danielson 00:59:44 I would love to find some of the issues where there's been some back and forth in the comments.
Everyone's right.
Josh Bonczkowski 00:59:52 For our agents, like.NET has some weird behaviors, too, just because of the way it has to load data in.
Liudmila Molkova 01:00:10 Okay, so then, it sounds like, Radiko, can you check what's common in Python or Pink Heron to confirm?
Radhika Gupta 01:00:19 Yeah, yeah, I'll do that.
Liudmila Molkova 01:00:22 Awesome.
Wow.
Cool.
So then, I'll take a look at the PR, no concerns in general.
Is it still a prototype? Do you want to take it out of draft?
Radhika Gupta 01:00:38 Yes, I will, and I need to also update it for other instrumentations. I'll ping in the Slack channel once it's ready for review. Thank you so much.
Liudmila Molkova 01:00:46 Okay, cool. Awesome, thank you.
So we have 5 minutes left, and nothing on the agenda, should we call it? Any last-minute thoughts?
Victor  Lu 01:00:57 Document, it doesn't need to be discussed.
is the document I'm creating.
To discuss about the three concepts, Agent identity, agent credential, and agent skill.
Liudmila Molkova 01:01:11 Okay.
And skill, interesting. Why skill is there?
Victor  Lu 01:01:23 To be honest, this… the discussion first started in the OpenID Foundation. There's an AIM meeting, working group. Mainly the same people who are behind the MCP security.
So, so agent identity, agent credential, consensus to be most important, and then we just want to make it 3, so it's, I guess the, I don't know, 3 seems to be the right number, so it just goes kind of packed into the… Top 3. So the first two are most important.
Liudmila Molkova 01:01:55 Yeah. Is this the hotel attribute? Or can we do something to unify?
Victor  Lu 01:02:02 Yeah, the… the agent identity, there's multiple definitions in multiple communities that's just different.
The reason I use the one from OCSF, this one go into not only definition, but actual attributes.
Because without attributes definition, it's hard to, you know, get into the details.
Liudmila Molkova 01:02:24 Yeah, like, from the VAC description there is here, it matches exactly what we call the GenAI Agent ID or GenAI Main Agent ID, depending on the scenario.
And, like, can we… if the definitions vaguely match, and this is the stable identifier for the agent, can we do something to make the attributes the same?
Victor  Lu 01:02:49 Awesome. Yeah, I mean, actually, when it comes to telemetry monitoring, having OTEL and OCS set up to be on the same page, that's the most important, actually. If you say this is exactly the same, that's perfect.
It's…
Liudmila Molkova 01:03:07 Well, exactly with the given that nobody can define the agent, but yeah.
Victor  Lu 01:03:12 Yeah.
So, yeah, so, so the COSI folks who are, I guess creating issues here is also working with OCSF. So, yeah, so identity being definitely the most important concept.
The second one is different. The second one is Agent Credential, that's from COSI Community. I actually talked to AIF people, the… that community at this point, thinks Credential does not need to be defined.
But in other communities, this is one of the most important concept to be defined, so that this is kind of differences that need to be, I guess, looked at more closely. But this particular one, Agent Credential, is not from those communities. This is only from COSI. And the only reason I'm using it, because it's not defined in other places. So, just use it as a kind of a first one to debate on.
Liudmila Molkova 01:04:08 Yeah.
Yeah, Don?
Don Branson 01:04:13 So I think this is an interesting discussion. One of the things I'm curious about, in terms of agent identity, has there been looks at… in terms of what was done with blockchain, or maybe business-to-business type integration?
Might be a bigger question, but…
Victor  Lu 01:04:31 Whoa.
Don Branson 01:04:31 It's…
Victor  Lu 01:04:32 It's… yeah, you're right, there are people who are proposing protocols that, you know, looking at, blockchain, but that's just one type of proposal. Definitely, I think it needs to be… have a consensus for everybody, so, definitely should be in discussion.
Don Branson 01:04:50 I would say not just, LLM and Agentic-type integration. I think the precedents are there. That's the important, sort of, message I'm thinking about.
Victor  Lu 01:05:02 Yeah, this is still early, trying to get everybody's input to know the landscape first, before we can agree on any concepts.
Liudmila Molkova 01:05:10 We have a lot of hands up, but we are out of time, so Victor, can you please make this document, like, so people can comment?
Victor  Lu 01:05:21 Yeah, sure. The reason I haven't… yeah, please, just submit your request to be a commenter, or, you can… so you can comment, add to the… to the comment list.
Liudmila Molkova 01:05:31 Yeah. Maybe we should discuss it next time, because I think it's a good topic.
Victor  Lu 01:05:36 I'll come next time to, discussing.
Liudmila Molkova 01:05:40 Yeah, sorry, Erin and Pam.
Maybe we'll talk about this next time.
Aaron Abbott (Google LLC) 01:05:46 No worries, I was gonna say the same thing.
Pam Dixon 01:05:48 No worries.
Liudmila Molkova 01:05:49 Okay.
Yeah.
Thank you both. Oh, sorry, thank you all. See you next time, then.
Aaron Abbott (Google LLC) 01:05:57 later.
Liudmila Molkova 01:05:59 Bye.
Pam Dixon 01:05:59 Bye, a la prochaine fois.
