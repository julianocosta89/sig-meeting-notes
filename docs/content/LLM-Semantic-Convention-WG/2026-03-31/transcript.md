SIG: LLM Semantic Convention WG
Date: 2026-03-31
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Liudmila Molkova** 01:48 Hello! Hi, everybody!
And… James, fellow note-taker, we are not authorizing you to record this thing, because it's already recorded.
You're fine.
Okay, let me share my screen.
Let's get started.
Okay, so… we have some… Us topics, agent servers, and let's move it here. I dropped some notes from KubeCon discussions, would love to talk about it, so maybe… I think maybe 20 minutes.
Feel free to add your things to the agenda, please add your name to the agendas list. Can you hear me, by the way?
**Trask Stalnaker** 03:06 Yes.
**Jamie Danielson** 03:07 Yes.
**Liudmila Molkova** 03:08 Was it this call where I spent, like, 10 minutes talking, but nobody heard me?
**Trask Stalnaker** 03:13 I don't remember.
**Liudmila Molkova** 03:14 Good, good.
Okay, and while people are joining and putting things into the agenda, let's take a look what's going on on our project board.
By the way, one of the KubeCon discussions was that I saga project management, if anybody wants to take care of the…
**Jamie Danielson** 03:37 I don't think that was the wording that even yourself used.
**Liudmila Molkova** 03:42 I did use this wording.
**Jamie Danielson** 03:45 No.
**Liudmila Molkova** 03:47 but yeah, so…
**Trask Stalnaker** 03:50 don't want to… you just don't want to do it. You just want somebody else to do it.
**Sergey Sergeev** 03:55 Was it a strong geomort?
**Trask Stalnaker** 03:57 No.
**Liudmila Molkova** 03:58 No, no, I'm… I… I… no.
But yeah, I'm… I definitely would appreciate any help that people are interested to offer with the project, board project management, driving the call, Yeah.
Okay, so, what do we have here? We have some of the things in progress.
And some new issues. Let's take a look at the in-progress things.
So… okay, this one, I think, is to reveal, and it's a good change.
Just to clean up, right?
Who invests… I think there was one discussion around it.
Sorry, this was the main change introduced in this pull request, right? That we are no longer tracking usage on the Invoke agent.
**Trask Stalnaker** 05:06 on the internal.
**Liudmila Molkova** 05:08 On the internal.
Yankid?
**Ankit** 05:19 Yeah, so, I had a question about that, like, and then I think there was another comment that, the token counts, if needs to be calculated on internal span, it should come from the corresponding LLM calls.
And which probably will require your L&M costs to be implemented, which is obviously not always a guarantee.
And, So, I think there was a confusion there for me. If, CLM calls are not, instrumented.
then I don't get any token counts, so should it be the responsibility of the framework who is creating that invoke agent span to kind of measure that Those token counts are made available.
Right, rather than relying on the instrumentation library to kind of provide those token counts.
**Trask Stalnaker** 06:11 Do you mean specifically on the internal invokeage and internal spans?
**Ankit** 06:17 Yes, yes, because those will be mostly created from the frameworks, right?
And I think I added a comment about that as well to the PR.
**Trask Stalnaker** 06:31 I think that part of the problem is that the internal, at that layer, It doesn't know if the… Underlying client, inference calls are instrumented or not?
**Ankit** 06:47 Agree, agree. And, I think, my, like.
like, the point I'm trying to put forward is, that's the exact reason why it should be framework's responsibility. Like, when it makes the LLM call, I'm assuming, for example, in responsive API, you do get the token comes back, and then… That framework can put those token counts on the invoked internal span, rather than relying on, like, that LLM… those LLM calls being instrumented and capturing those.
Right.
**Trask Stalnaker** 07:18 Does the framework, orchestrate those?
All of those inference calls?
**Liudmila Molkova** 07:37 Surya?
**Sergey Sergeev** 07:39 Yes, Harry, can you say it again? I missed…
**Surya Teja** 07:43 Yeah. So, one thing… I have been digging more into this, so one thing what I wanted to add is.
the current Claude agent framework.
is using a CLI process, which is not having any instrumentation around it.
So, in those scenarios, I feel that Invocation Client Span, which, the other one that, Trask has created, can help create, can help track.
the EA, tokens and, stuff.
For that, and the internal agent, span can, the invoke agent for internal agents can, pretty much leave the token calculation and everything, and for the OpenAI agent framework, pretty sure if someone is using the Python construct on that one, they can add dependency of, responses, instrumentation, which is soon to come, which will track the, LLM inference calls, so that way we are the current… design works well for both OpenAI Agents Framework as well as for the growth Cloud Agent SDK, if we write the instrumentation to cater for token calculation.
So, I just wanted to support the current design and say that it is well thought out, and it supports two widely used frameworks.
**Liudmila Molkova** 09:14 By current design, you mean… Not recording them on the outer span, or And.
**Surya Teja** 09:22 Not recording them on the outer span, and just recording them in the inner span, that is, after the invoked agent internal span is recorded.
**Liudmila Molkova** 09:36 Yeah.
**Trask Stalnaker** 09:37 I'm kidding.
**Liudmila Molkova** 09:37 Thanks.
**Trask Stalnaker** 09:38 When I was looking, I think I only found one example framework. I'm trying to find it, which… add the… Token count even available on the internal span?
**Ankit** 10:00 So, right now, like… Probably most of them should have it. I know Microsoft Agent Framework has it.
If you have…
**Liudmila Molkova** 10:12 It's not internal, it's client, the Microsoft.
Agents, right?
**Ankit** 10:21 Yes, yes, it's fine. That's right.
That's… Oh, actually, right now, like, everything is client, until, like, after we make a decision on which we are, right? This, or, like, at least a client-side, like, orchestration-based Adidas client. But I think there was also discussion, like, when we introduced the, Invoke Agent server.
spend that… the spans created by the, like, these frameworks, like Mangchen and other, can be marked as internal that we are running the same span, right?
product. That's also there in the spec right now.
If it's running in the same process, then… They, like, the client span type can be internal.
**Trask Stalnaker** 11:12 What about as an action plan for this?
question, Ankit. Let's put together a list of, internal Invoke agent spans… That… support capturing these, even, because I think that, there's kind of two… there's a couple questions here. One is if it's even available on internal Spans, from frameworks at this point.
The other is… The other is, do we want, this deduplication, across the internal and nested client spans for… it sounded like there was some use cases for wanting to sum up But I… let's take that secondarily. We could bring that back next week.
**Ankit** 12:13 That's good.
Definitely happy to work together on that.
**Trask Stalnaker** 12:18 Because I think that that was the main reason I left it out, honestly, from this PR, was that I didn't find supporting, Frameworks for it.
But it's very likely I missed stuff.
**Liudmila Molkova** 12:40 Thanks, let's, spend a few more minutes triaging. This is in progress, and I'm curious… Why multi-agent semantic conventions, I kind of feel we have the skeleton of this.
We still don't have any notion of task, or task-agent relationship.
But other than that, I think we're done with it.
Oh, I moved it to in progress. Interesting, I don't know what my motivation was.
So you see, I suck at project management.
So I'm going to put it back to to-do.
I think we're… probably can… Merge multiple issues around this, and maybe close this one.
Okay, let's take a quick look at what we have.
And new issues.
the skills pan… I think we talked about it, and I think we kind of realized that this is something useful, and we should… Do this, but specific details are probably… Need to be figured out.
So I'm going to move it to too-do. Anything else interesting here?
Reinforcement learning.
I think this is… somewhat out of scope of our current work. This is the training process, right?
And we don't tackle it, at least… yet.
**Jamie Danielson** 14:49 Yeah, I think.
**Liudmila Molkova** 14:50 What? Yeah.
**Jamie Danielson** 14:51 Not specific to this, but more of… I guess, like, one of the things that we talked about with, planning out, like, roadmap and future work that also makes it easier to respond to issues like this is if we're able to, kind of find a couple of these general topics and put them into sort of, like, a list, so that we can point out, like, these are the things that we're currently working on, and then these are the things that we might get to one day, but we're not there yet. And that also helps kind of set expectations for people coming in to know what's in progress.
**Liudmila Molkova** 15:27 Yeah, that's a great point.
**Jamie Danielson** 15:32 Also helps us kind of remember what's sort of ahead and what will be coming up.
I guess if it's helpful, I can, like, start something somewhere, and then say, okay, go throw more things into there, maybe just start a Google Doc, and then once we kind of have a rough idea, we can make it sort of an issue that's, like, a live… document that we can update as we go along. That's sort of what we've been doing in OTel.js.
**Liudmila Molkova** 16:04 That would be awesome.
I'll share some links with you, I think we're… we… I'll share later. I think we did a game where we… try to prioritize things that we work on, and we have an Excel sheet somewhere.
**Jamie Danielson** 16:24 I think I have a… yeah, I think I have that saved somewhere. It was sort of like, if you could choose what features we would have, everyone kind of voted on what was important to them.
Right.
**Liudmila Molkova** 16:34 Yeah.
**Jamie Danielson** 16:35 yeah, I don't have a ton of all of the background, and I don't want to take up too much time on it, but that's where I figure if I just start it based on what I know is there, and what I can find, just to kind of get the ball rolling, and then you can come in and tell me what's wrong and what needs to get added in and moved around and all that.
**Liudmila Molkova** 16:53 That's… that's great, thanks a lot, Jamie.
So this is the link to the doc that we had. I treat it as a soft contract, but, like, It's just the, the… the list of things that people are interested, it's not the, it's not… it's not official, right? It was a game. There were, like.
15 people on the call, but it's a good signal.
Okay, wonderful. So, this one is to-do for this one.
Let's maybe… Hood… And another swim lane.
Pronouncing, Not, not in scope.
How do people feel about it?
Yeah.
The alternative is we just remove it from the GenAI board.
**Jamie Danielson** 18:04 I think it makes sense to start with not in scope, and if it becomes unwieldy, if that list ends up getting really long, then we can look at moving it to even, like, a backlog board. But for now, it might give us good signal to start.
**Liudmila Molkova** 18:17 Okay, yeah, thanks. Okay, so let's put it here… Okay, so let's just spend two more minutes talking about this, too.
This is… somewhat similar?
Still, it's the server, it's internals of the inference calls. It's super interesting, it's relevant, but I feel this is nowhere in our… Priorities list for now.
And I know that VLLM is heavily adding metrics for this, with Prometus, and maybe it's not a bad thing if they can move separately, and maybe eventually we can converge on something in common.
Aye.
And feel free to leave comments and, like, suggest, if you're interested.
So this, this, this is the grouping, I think this is the same as a React span, So I'm going to link the React span here, I should probably link… Does anyone have any strong thoughts or opinions about this?
Have anybody looked into… this issue…
**Jamie Danielson** 20:26 I might have opinions, but have not looked at it yet.
I and my, team, they've been instrumenting some stuff internally, so I'd like to see what they think about it.
Now that I'm back.
**Liudmila Molkova** 20:40 I think Martin has opinions about it. He was interested in something.
**Jamie Danielson** 20:44 Martin does have opinions on it, that's true. So I want to sit down with him a little bit and get some notes together.
**Liudmila Molkova** 20:52 Awesome. So then, I'll keep it in the new status, and if anybody, have interest thoughts, let's take it, asynchronously.
**Aaron Abbott** 21:02 One question, sorry, sorry.
On that issue, like, the thing that's… the thing that's missing is… one which we already have. Like, there's already an issue for it, right? So, what's actually being asked for in this issue?
**Liudmila Molkova** 21:17 That's a good question.
**Aaron Abbott** 21:23 Like, I didn't get the… the number… the number 2 thing about type… types?
So maybe we could just get some… That's a lot.
Yeah.
**Liudmila Molkova** 21:52 Yeah, my generic proposal is not to come from, okay, I look at this trace, and I want to see more, but more from, okay, I'm instrumenting this library, what can I even achieve?
**Aaron Abbott** 22:04 Yes, exactly, I… yeah, that's exactly what I was thinking when I was reading that.
Okay.
**Liudmila Molkova** 22:15 Cool. So then, let's move on to the agenda. If we have any additional thoughts on this, let's come back to this issue next time.
regular 5 minutes to people who are new? Do we have anyone new?
Do you want to come and say hi?
Okay.
I'm going to assume nobody wants to introduce themselves, that's totally fine, but if you change your mind, feel free to do this.
Cool. So, we are… we're moving on to the KubeCon updates. So, we had a nice, like, maybe 10 people showing up at the AI, Sieg office hours. Thank you, everyone who showed up. It was a great discussion, and essentially.
We talked about a bunch of things, mostly around… how we can speed things up, how can we make progress, how can we focus more and better? And I think we identified a few proposals, and these are… The proposals, and we want to hear your thoughts about those, and maybe you can see other issues or suggestions.
So, the common theme was that maybe we want a separate repo. It might help Python to move faster with instrumentations, but also we want a separate version for semantic conventions.
So it's kind of cool to separate slightly semantic conventions. They're still governed by Autel, they can live in semantic conventions, they can live in a new repo, but they have a different Version from the rest of them.
What it gives us is the possibility to major version bump them faster, because AI space is new and is super fast.
So we will be able to say, okay, maybe every 6 or 12 months, we release a new major version of semantic conventions and instrumentations.
I think 12 months is a cadence for Java, instrumentation for the agent.
No? But, okay, you have…
**Trask Stalnaker** 24:45 About 2 years.
**Liudmila Molkova** 24:46 About 2 years. Okay.
So, I think we can pick the faster time, and we can be more conservative or less conservative, but we should have some predictable schedule.
And we can keep allowing to opt in the bleeding edge.
We can allow to, as we release new major version, we can allow to opt-in into previous major version.
This, gives people at least twice as much time as our release cadence to update their backends, and, like, it's not too… too aggressive.
It seems the common theme that the instrumentations for Autel are… somewhat behind other instrumentation sets. It's not really that the semantic conventions are behind, it's more that they're implementing these instrumentations across the, ecosystem is slower. And what can we do to speed things up?
So we can actually not consider semantic conventions pull requests.
Without, actual instrumentation work.
That would eliminate a lot of pull requests we have that are more theoretical, than practical.
And we automatically, yeah, we automatically deprioritize them.
It might be that we, like, spend a lot of time reviewing things because we didn't document the contract, like, what… how… how to make things successful with contributions.
And we can say, okay, this is how you analyze different libraries, or different systems, this is a list of systems we consider to be diverse. Let's say, I don't know, Google, OpenAI, Anthropic, Microsoft… well, we should identify the list of things that we care about, most, the most, and we should use them as guinea peaks for new features that people propose. And they would analyze how the thing they are proposing applies to them.
We can then compare terminology, we can see if things are generic.
And again, if it starts with the instrumentation, that it's much harder to… Actually… It's less obvious how to make progress, it's more practical.
So if we could document this checklist, and we can ask people to follow it, we can at least help twist the reviews and not repeat ourselves when people contribute things.
And probably the most important part, we can automate everything. We can do better with unit tests, we can do waiver life check with, for the conformance, we can report conformance. I think Trask has some amazing, outcomes of, doing conformance. Maybe you want to share at some point.
We can leverage AI to help us with the first round of review.
And… what I heard from Alibaba is quite interesting. They automated the whole process of instrumentation and bringing features.
You can guess how, but they might send some demos, to share, and maybe we can learn something from them.
That's my take, Aaron, Jamie, others who were there. Did I miss something? Do you have some other impressions from KubeCon?
**Aaron Abbott** 28:51 No, I think that was pretty comprehensive from, the kind of feedback I heard.
Yeah, I think maybe one thing to mention is… Like, if we do a new repo.
kind of do this federated SEMCOM thing, like, there would be some, I guess, leadership bootstrapping we would do, so we would want to, like, involve other people. Maybe involve more companies, because, you know, like, right now, with the current structure, we're… in Python Contrib, and I'm pretty much the only maintainer there, and I don't want to be, like, a bottleneck. So, you know, I think people would hopefully be excited by that, and we could, you know.
gauge interest.
Yeah.
Jamie, sorry, anything from you?
**Jamie Danielson** 29:38 Yeah, no, I think everything is covered here, at least that's what I had in my notes also. The only thing I was gonna suggest is if we want to create, like, a parent issue of, like, checklists of some of these things, of, like.
getting some of them done. So, like, for example, we said it would be really nice to have a checklist for instrumentation, submissions, so, like, if someone picks up that as a small issue of, here's a checklist, let's put that into a contributing guide or whatever else, and… similar for some of the other things. I'm happy to put that into an issue, too, to start, same thing, since I'll be doing the other admin piece anyway.
And then that way we can kind of make sure that we're able to… To get the things done and have them there.
**Liudmila Molkova** 30:21 Yeah, awesome, so then we would… What is actionable here? I think this is a big actionable piece, like, what do we need? How do we need this? I think there are some discussions, that are happening, in different… places… like, I don't think we're ready to decide right now how would it look like.
But, this is definitely an, there is an action item here.
Duh… checklist, this is another action item. Jamie, you want to create an issue for this?
**Jamie Danielson** 31:04 Yeah, I can do that.
**Liudmila Molkova** 31:05 Yeah, awesome.
So, this are probably, very specific pieces that we can already tackle. And, I would be happy to own, let's say, the unit testing, or if people who work on GenAIRTLs and Python are interested in having common helpers.
also defined. That would be a great contribution.
Yeah.
**Surya Teja** 31:42 I have been working on integration testing a little, like, last time we discussed, right, you suggested a few comments on my Anthropic thing.
I'm trying to come up with a helper, like you suggested, for integration tests.
**Liudmila Molkova** 31:59 Okay, cool. For integration tests, I think we have the tool that's… covering it pretty well, the Weaver Life Check. It's, like, it's language agnostic, and it's based on semantic conventions.
But it would not cover all the… like, behavior specifics, right? So, for example, you, enable content, disable content, you expect an error, you don't expect an error, and then for this, it might be… It might make sense to… Half, like, like, tests and Latin… language-specific tests.
Oh, okay. But it's, it's probably we're talking about the same thing, but you, you're… You mentioned it as integration tests, and I'm thinking about it as,
**Surya Teja** 32:46 Yeah.
**Liudmila Molkova** 32:47 tests.
**Surya Teja** 32:48 Yeah, it's fairly from your idea that I borrowed, so I… I get it, yeah.
**Liudmila Molkova** 32:56 Yeah, so do you want to own it?
**Surya Teja** 32:58 Yeah, sure, I'm fine to own it, actually. So… I have put a few things that I learned from Java OpenTelemetry Repo. I can own it, and I can share some of the things that I learned from there.
**Liudmila Molkova** 33:14 Nice. That's great.
And I think, Trask, you already made so much progress with Weaver Life Check, I'm sure you want help.
But, like, what are your thoughts? Do you want to own it? Do you want to, I don't know, talk about it some other time?
**Trask Stalnaker** 33:30 Yeah, yeah, I'd love to share the… the conformance report stuff.
Maybe, how about at the end of this?
block here, I will… Sure.
**Liudmila Molkova** 33:47 Cool, yeah.
**Trask Stalnaker** 33:49 I had a… Couple questions about the separate repo.
for… one question was, kind of open question, is should it be Python only?
Should we have… You know, for… should we have separate repo for… also for JavaScript?
Java… net.
Combine them all into one repo.
It felt to me like, the Python was the separate Python repo was clearly the biggest win. I… from the job, I know from Java.
We would probably want, actually, Prefer to keep those instrumentations in our repo.
Just because that's where we have all our, infra… Set up.
The other question I had was, for Python, there's a shared… there's some shared code in the Python contrib that they… all the GenAI, all the instrumentations reuse.
And so, I didn't have a sense of… if that… Code is fairly stable and not changing that much, that it wouldn't be problematic to… for the new repo.
To just depend on releases of that.
**Aaron Abbott** 35:36 Talking about the, like, GenAI Utils package?
**Trask Stalnaker** 35:39 No, I think there was a general instrumentation package.
**Aaron Abbott** 35:44 Oh, yeah, yeah, I think that's okay.
**Trask Stalnaker** 35:49 Cool.
**Aaron Abbott** 35:50 Yep.
So one question I had to ask on… like, the Java repo. I think one of the impetuses here was, like, the… the CNCF graduation is, you know, all about showing which parts are stable, and we wanted to federate the semantic inventions here with, like, a faster major version release cadence, right?
So, you know, presumably, if those instrumentations live in the Java main repo, you know, they would… they could probably consume the Weaver schemas if they were in the separate repo, but is that going to be an issue with the stability stuff we're working on, like, throughout OTEL?
**Trask Stalnaker** 36:32 I think the only issue would be the, the versioning bump.
And that's definitely an advantage to having it in its own repo.
To follow the version bumping the GenAI some kind of… as it is right now, the way we handle it is we'll just have opt-in mechanisms to opt-in to the latest, or the stable, or the V-next.
In the Java repo, but we won't make that the default until whenever we release the next major version bump, which is… Not as ideal.
**Aaron Abbott** 37:28 Okay.
**Liudmila Molkova** 37:28 How many instrumentations do we have in Java for AI?
**Trask Stalnaker** 37:33 I think 2 or 3.
I forget.
**Liudmila Molkova** 37:40 And for JavaScript, it's just one, right?
**Jamie Danielson** 37:44 I feel like it… I haven't looked in a little bit. There was at least a couple in progress. Last I checked, there was just the one for… just the one, but I think there was some lang… Smith Langviews, I forget what it's called.
Lang Chain is in there now.
**Trask Stalnaker** 38:04 I think OpenAI and Bedrock, And vertex? No, no, that's Python, sorry. I'm reading the wrong columns.
**Jamie Danielson** 38:17 OpenAI, LangGene…
**Aaron Abbott** 38:23 Jamie, would you be interested in separate repo, or do you think it would be better to keep it in the JS contribib?
**Jamie Danielson** 38:30 I would have to check with the other maintainers.
There's definitely pros and cons to both, and we've kind of gone back and forth, because we have a similar issue with browser stuff, of deciding when to split out or what to split out, so I can check in with them and see what they think, and get back.
**Aaron Abbott** 38:51 Yeah, I think… I want to say it was Trent was coming to the SIG for a while, and… it was difficult to get code owners for the OpenAI one, if I remember right, so… Yeah, I don't know. I guess… I guess he'll go back to them and see, but it seems like they had the same kind of issue.
**Jamie Danielson** 39:10 Yeah, I mean, it's hard to get code owners for most of the things, I would say. We do have, like… and the other thing that we try to figure out is we have, like, a… we're trying to avoid adding too much auto-instrumentation, but also want to have some of the things that are super common and really asked for, which is all the AI stuff right now.
But there's always a general concern of making sure we don't break something else, because we have an auto-instrumentations node agent in there. And so lots of people use that, so the fear is if something breaks, if it's trying to take that in,
**Aaron Abbott** 39:44 Yeah.
**Jamie Danielson** 39:44 Yeah.
**Aaron Abbott** 39:45 Yeah, we have, like, a default distro for hotel, Python, zero-code, auto-instrumentation, whatever. And they're… it's probably a little bit more flexible than, Like, you can install and remove stuff, but we still have, like, a default list of things, because there's this separate bootstrap script which can look at your dependencies and install stuff that's needed.
But yeah, it's a good point, like, Trask, would the distro, like, the Java agent… I assume these would be Java agent instrumentations, and would they go in the default distro?
**Trask Stalnaker** 40:17 Yeah, they could be either library instrumentations, Java agent instrumentations, or both. Ideally, we have both.
I think for Bedrock, at least, we have both.
But yeah, we would pull it in, but we can do that. We already do that, for some other instrumentations we pull from another repo.
**Jamie Danielson** 40:44 Yeah, so if it was something that… I have to double-check what the latest is, if these other, like, if, like, the OpenAI instrumentation, for example, was added into Auto Instrumentation's node, I'm not sure if it was, because that is one of the current limitations we have.
With that is that we can't do, like, the one-line registering of auto-instrumentations using an instrumentation that isn't in our, repo.
That's, like, a thing to sort out one day, but we're not there yet. So… I'm not entirely sure how people currently expect to use these instrumentations, if they do the one-line register, or if they, you know, manually configure it. So that would be a big… a pretty big thing, I think.
If we… if we need to have it in the auto instrumentation package, we would need to, today, keep it in that rebuilt.
**Trask Stalnaker** 41:38 And for Java, that actually is a good point because, we wouldn't… We… it wouldn't solve our version bumping problem.
By having it in a different repo, we… while we could version… That instrumentation separately, and the library instrumentation we can release separately.
But we wouldn't be in the distro. We wouldn't… we don't take breaking changes into our distro without a major version bump.
Anyways…
**Liudmila Molkova** 42:13 Yeah, it's a great question, how we would solve it for Python as well. Would we… Pull this new instrumentations into the… Python distro… And… it's not stable, so we assume we would major version bump it. Sorry, we would… Pay-breaking changes, but… That's tricky.
**Aaron Abbott** 42:36 Yeah.
I think… I think for Python, it's pretty flexible, because, you can kind of… there's, like, this entry point mechanism, which is built into the language. It's kind of like SPIs.
But it's pretty easy to, like, you know, basically just look at whatever's installed, so… I think we could… we have, like, a meta package that has a list of all the instrumentation, so we could make another such meta package with, like, the Gen AI ones in a separate repo, so people could easily pull them in. I think it would be doable.
**Liudmila Molkova** 43:09 Yeah.
Last thing on this, I think maybe Microsoft people, maybe Tao can correct me if I'm wrong, but in .NET, it's pretty common to have native instrumentations.
And most of the AI instrumentations are native.
**Tao** 43:30 Yeah, for Microsoft Agent Framework, both .NET and Python instrumentation is native.
**Aaron Abbott** 43:47 I was gonna ask… I don't know, is anybody interested in… on the leadership point?
Is anybody on the call interested in, like.
You know, being a maintainer of this new repo, depending on which languages are in it.
Like, could people volunteer time to do that? Is that something interesting?
**Jamie Danielson** 44:13 I can confirm internally, I think Mike from Honeycomb had started working on the Python stuff. Aaron, you would know more than that. He's on a different team for me now. But I think there's probably a decent chance that he would want to, I'd want to check on our side. We might have a couple of people who would be able to.
**Aaron Abbott** 44:34 Okay. I mean, I think… I think for this to work, this is kind of the most important part, like.
getting the right people involved who have time to commit to it, and… I think, like, creating a new repo is some initial work that's gonna be probably higher than if we just stuck it in the existing places like we're doing, but there might be benefits in the long run, like.
you know, Building… Kind of shared knowledge of this thing, and… getting more people involved in hotel, generally, so… Yes, Surya's interested, okay. Yes, Surya, what's up?
**Surya Teja** 45:12 So, are we scoping down how many languages we are going to target for this, stuff? Like, say, scoping it onto one or three languages would be a good starting point?
but I'm just curious to see if we are targeting all the language, like .NET Go, Rust.
Java, Python, and everything.
**Jamie Danielson** 45:37 I think a lot of it probably comes down to also prototyping and how quickly we can get prototypes in, right? Like, I think we'll have less of an issue with like, number of total languages, as much as just getting at least maybe two to implement a SEMCOM. Trask, I cut you off, though.
**Trask Stalnaker** 45:54 Just say, yeah, I think it's a… We don't really… of, the Python, would we want it? I guess one question, like, if we decide whether we want it.
whether we would want a monorepo with multiple languages or not. If we don't want multiple languages in a single repo, then it's easier to say, okay, well, let's at least start with Python and Then we can… if there's desire for other languages to split out, we could do that.
**Surya Teja** 46:36 Yeah, thanks, thanks for that, but I'm not sure, have to proceed on that one. I'm just looking for guidance from the maintainers on what is the right path and right way to do this.
And my question was more on that thing.
**Liudmila Molkova** 46:54 My, gut feel is that we should solve it for Python.
It doesn't feel like a huge problem for other languages, just given the volume of work happening in the AI world.
And maybe, we can solve it in other ways for other languages. I think what's important for me is that we have different companies participating, and maybe I would love to pull other players in, trace loop slash service now, arise, so I would love to have a diverse set of Maintainers, and… the… people who have a set of instrumentation libraries out there should have a say, and maybe we can, ask, like, we can resurrect Hotel practice to require different companies to approve PRs, so that we… we fight, like, over-representation or whatever reservations people have against each other or hotel, was the, like, making sure people work together. It actually, of course, it depends on this other companies being interested in participating.
**Trask Stalnaker** 48:23 So, sounding like there's some consensus on the Python GenAI repo.
But blocked currently on… Deciding on, maintainers… List Maintainers and approvers list.
**Liudmila Molkova** 48:43 And I feel this also makes sense for the same set of people to be maintainers of semantic conventions for GenAI.
So, this thing's… yeah.
**Aaron Abbott** 49:00 Go ahead, Jamie, I was just agreeing.
**Jamie Danielson** 49:01 Sorry, yeah, I was gonna say, like, Python is a big one, like I think Aaron pointed out, because it does have some of the known problems to sort out, and it's a very, you know, probably the most common language. But yeah, I think we talked about, in general, using that as sort of our… our… Standard, like, generic, commonplace to keep things moving quickly, both in, like, testing and prototyping and instrumentations and all that, too.
**Liudmila Molkova** 49:35 Cool. So then, we are way over time on this topic, and we have just 10 minutes left.
I think we've identified some action items. We need to keep working on the separate repo, I think we need to identify the maintainers, and as Aaron mentioned, it's mostly the time commitment rate.
And we want to have a diverse set of them.
Think… We will need to come up with some proposal on how things will work together.
I can take an action item on this, but I'm not sure if we can make the progress during the next week, because I think there are some Some big questions to answer.
And I'll try to summarize the proposal up in writing, at least on the high level.
And Jamie, the connection item, too, for the checklist.
And we will work on the automation. This is not the rocket science.
Okay, Trask, you wanted to take a… to share the conformance, maybe we can do it next time, given…
**Trask Stalnaker** 50:56 Yeah.
**Liudmila Molkova** 50:56 10 minutes.
**Trask Stalnaker** 50:57 Yeah.
**Liudmila Molkova** 50:59 Let's put it here… Yay, one last thing from KubeCon that came up, and, where Alibaba folks have interest in contributing.
they have interest, and they have capacity to spend time on the instrumentations, but it's actually very hard for them, because we have one meeting bi-weekly, and usually it doesn't happen because of… I'm the only one who can make it from the Pacific time.
And I don't… it's not that I can't join every time. So they feel a little bit excluded. It happens on Mondays at 5 PM Pacific?
So on the West Coast and, Asia.
Can make it, but it would be… They are just looking for ways on how they can contribute in a more synchronous manner, or how we can include them better.
Okay, it's important.
But I don't know the answer.
Maybe more people can join, let's see.
Let's… Let's see, is there anything absolutely urgent that we need to discuss today and the remaining 8 minutes?
**anksing** 52:42 If there's, like, nothing urgent or, like, there on the agenda, I would like to discuss about the invocation service plan. I think it's already in a state where pretty close to, getting invoiced, so… but if you have something else which is more urgent, then we can…
**Liudmila Molkova** 52:58 So I think last time we stopped, at the point where, like, is it different than internal?
Span, add goal, internal invoke agent.
Do we need a separate?
Server's pen.
**anksing** 53:14 Yeah, so I think, something came up, and I shared some, spec in the… there's an open response spec as well, which basically defines responses API as a protocol to be used.
And, and that sounds very similar to how we have MCP spec defined as well. MCP is a protocol, based on our PC, and we have a well-defined spec for it, and… This also kind of goes in the direction of, if we have these protocols, then can we have, like, your server spends to kind of… and, I mean, the same argument applies to HTTP spans as well, I believe, so…
**Liudmila Molkova** 53:57 Tell me there is another, another AI protocol.
**anksing** 54:00 Yeah, I also came across it recently, I shared task as well, I was like, okay. Yes, there is another one. But it's, basically, yeah.
**Liudmila Molkova** 54:13 Can we… I'm sorry, can we do the exercise, or maybe we've done it already, can we say, okay, this is what I ate, makes sense for A to eat, this is what makes sense to… this new protocol, this is what makes sense to cloud providers like Microsoft who want to host Agents on the server.
**anksing** 54:37 I see, so the… so the ask is, like, to kind of put down together some information about, like.
These different protocols, and then different providers are supporting them.
Borrow.
**Liudmila Molkova** 54:52 So, I think that the… the… difficult place is, like, what makes you pursue separate server span? Like, why do we need it? Is there something… important? Like, what… what stops you from starting with, let's say, in… Turner's pen. I, I, I see… Why?
But… Do we have it?
**anksing** 55:18 I think I'm dead.
**Liudmila Molkova** 55:19 Did we explore all the options, and do we know why we're doing this?
**anksing** 55:23 To serve me.
**Trask Stalnaker** 55:24 For me, I think Ankit, the ask is concrete, examples of… Frameworks or cloud providers that would need to capture… that would want to capture it as a server span.
Where that makes sense.
**anksing** 55:45 Can you turn?
**Trask Stalnaker** 55:46 Over an internal span.
**anksing** 55:48 And… Yeah, definitely, I can put that together.
**Trask Stalnaker** 55:52 Based on our prior discussion in… a couple weeks ago in this meeting, there was, like.
Oftentimes, there's a HTTP server span, and then, you know, it, invoke agent internal span underneath that. That modeling makes sense in a lot of cases.
But based on some of the conversation you and I had last week, you know, it seems like there are some cases where… the… There's now a protocol, basically an agent-to-agent protocol layer, and so… It makes sense to… Capture and invoke agent server span for that.
But we need to lay out those specific examples to justify, that this is… Needed and has… use cases.
**anksing** 56:49 Definitely, yeah, yeah, I'll work on that, add that, to the here.
Okay, we can discuss next week.
Thank you.
**Liudmila Molkova** 56:59 Awesome. Thank you.
Okay, and since we have 4 minutes… Peace, do you want to talk about the toolkall name?
**Keith Decker** 57:14 Sure, that was, based on a comment you made earlier today about how, we have tool name as recommended in some conventions, but it looks like it's… kind of required when we go in through instrumentation. Just wanted to get other people's thoughts on that before… or just… add comments to this, PR as well.
**Liudmila Molkova** 57:40 Yeah, and it's probably more a question to semantic conventions, because it's listed as recommended, but in practice, like, if you don't have a tool name.
I don't think there is ever a case where we don't have a tool name.
**Keith Decker** 58:00 Right. So, If you want, I can go throw an issue up here in some column of an ad as, changing it to required, and we can do a discussion there.
**Liudmila Molkova** 58:11 Can you send a PR, maybe?
**Keith Decker** 58:13 Yeah, sorry, Pio.
Yeah, I can go to that.
**Liudmila Molkova** 58:18 Awesome. Thank you.
Cool.
So, there are some PRs to review. Surya, thanks a lot for sending them.
This one is probably… For the future, Ross, for the next time to discuss.
And thank you. Great to be back and see you all.
Great discussion today.
**anksing** 58:46 Thank you. Bye.
**Liudmila Molkova** 58:48 Thank you.
**Tao** 58:49 Right.
