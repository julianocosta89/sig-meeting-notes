SIG: Browser SIG
Date: 2025-07-24
Duration: 36 minutes
============================================================

## Zoom Recording Transcript

**Ted Young** 02:46 Hello, God! It has been meeting hell!
Good to see you all.
**Martin Kuba** 02:57 Good morning!
**Ted Young** 03:03 Okay.
So for today's agenda, do we have Joaquin Diaz? Oh, no, we don't have Joaquin Diaz.
So no, no. Looking at his test harness plan with him.
**Jared Freeze (embrace)** 03:27 Yeah. Joaquin is offline for a couple of weeks.
**Ted Young** 03:34 Okay, maybe we could walk through his plan without him. Possibly is one thing.
Dan, did you wanna give us a presentation about your your browser proposal.
**Daniel Dyla (Dynatrace)** 03:55 Api.
**Ted Young** 03:56 Yeah. Proposal? Sorry?
**Daniel Dyla (Dynatrace)** 03:58 No, it's not ready. Sorry.
**Ted Young** 04:00 Okay.
Martin, would you like to walk us through? All of the research the client Sig had done in the past around the set of events and everything.
That was out there.
**Martin Kuba** 04:22 Yeah, I mean, I can. I can walk through it. I also could now talk a little bit about the session management.
I made some changes to the to the Pr. That I that I shared last week.
But I can. But I can definitely talk 1st about the the events.
yeah, I'm gonna share my screen.
maybe I can share my screen.
Okay, it doesn't seem like I set up my zoom yet to share my screen so I might. I might have to. Either you share your screen, Ted, or I. Can. I have to rejoin.
**Ted Young** 05:15 Why don't you quit and rejoin.
**Martin Kuba** 05:17 Okay, sorry about that.
**Ted Young** 05:18 50, net, net, faster.
**Martin Kuba** 05:54 Okay.
I actually see that Santos is here. So Santosh maybe can help me, because he was part of this exercise, too.
**Ted Young** 06:09 Great.
**Martin Kuba** 06:10 So, yeah, I mean this, this has been a while. This has been maybe a couple of years or or so. So I shared the the information here in in slack so what we what we did back then and it it sounded like very similar to what you were asking for Ted is all the all the different people representing different vendors, like we had a document where we shared basically a list of events or signals that each each vendor's sdks are sending, and together with with their with the attributes that we capture.
So you can see that we had, like new relic appdynamics, headsam, honeycomb aws blank.
And then the outcome of this was a discussion of Let's come up together. Let's come up with some common attributes that we want to capture for the, for the instrumentations we want to build. And that was so. The from this document we created a spreadsheet that captures the different types of events that we want to capture. And we had long discussion about the attributes that we wanted to capture.
So like for page view, you know this, this is what we basically decided on that. You know, we had one for page navigation, timing, event resource, timing event, user action web vitals, exceptions.
And then from that. We did. Actually open a few different prs, so we have the ones that I just mentioned for page view, navigation, timing, resource, timing, user action and the web vitals. The only one that has been actually so far merged is just web vitals.
So I guess we can. I think the ask from last week was from the people in this call, participating now to come with similar similar data from their sdks. So my my suggestion was.
let's you know, let's just add to maybe maybe we can just review this together, or maybe like, if there's something missing, we can also have those discussions directly on those Prs at this point.
**Ted Young** 08:52 Yeah, that's super helpful. I'm glad to see how much work has already been done here.
And is your feeling like this is all still very relevant, I mean, I don't see why.
**Martin Kuba** 09:04 Yeah, I think I think it's I think it is. Yeah, I nothing's changed in the browser world.
So.
**Ted Young** 09:15 So I kind of see like like 2 2 pieces of this is kind of like the the next step one is to like you said we wanna come up with an Api like like a test harness or something.
Does that test harness? And when we're testing, relate in any way to figuring out this set of events that we're capturing? Or do you feel like that's pretty separate.
**Martin Kuba** 09:55 So so, for I guess is that the goal of the test harness is to test some like performance metrics right of the SDK like the bundle size and the maybe like performance and maybe like a browser. Compatibility, too.
is that is that the goal of the harness.
**Jared Freeze (embrace)** 10:17 Well, there's also, yeah, there's also like data integrity checks as well. So it's yeah, it's bundling but also, like, automating a full like applicate like a react app, basically that that like, you can go and click on stuff. And then after that, having like a synthetic like.
you know.
like testing of, you know, Json, or however it might be done easily by the you know, headless chrome, or whatever.
So yeah, checking things like click or or whatever it might be.
**Martin Kuba** 10:53 So so would we want to.
Include.
So we will be checking if things work in different types of browsers. And would we want to test all these different instrumentations then, and I'm guessing. Yes.
**Jared Freeze (embrace)** 11:11 I think so.
**Martin Kuba** 11:12 Yeah.
**Ted Young** 11:14 Yeah.
I mean, like saying that, like our implementation having like benchmarks, that shows that our implementation is like performant as other implementations. But it's only performant because it's not doing any work.
because, you know, checking a bunch more things than we are.
So so that that seems relevant to figuring out our test harness.
I almost wonder if we want.
I'm a little worried that like asking people to go off and like, be like, Go do research on like your own current implementation and like, bring back a bunch of helpful knowledge to the group, might be like a little vague and if we had maybe, like a template for people to fill out. It might be helpful so that we get more like apple to apple comparisons about the different implementations out there in a way that's like useful for us building what we're trying to build.
So maybe we could brainstorm that really quick.
like, it seems like one of the things that we want from, and let me just pull up a place to to write this real quick.
So talking about searching, existing implementations.
What do we want to see?
And it seems like one is like a list of events, right? Like, basically like something basically give people this spreadsheet and say, like.
does this line up with what your implementation currently does? Or does your implementation look pretty different from what's listed?
Here.
**scheler** 13:23 Ted. Maybe I'm not following. Are you suggesting that we get additional vendors to add their in place to that spreadsheet? Because I thought we have some info already.
**Ted Young** 13:33 It seems like we've got some info in this spreadsheet already. What we're asking for in general is we're trying to set up a test harness. We we would like to improve open telemetry for web.
In phase one, we're going to focus on the Api layer plus instrumentation.
Plus whatever little bit of data modeling we need to do. We're not going to worry about the SDK, but we want when we say we want to improve this in terms of performance and everything else. We want to have benchmarks to compare ourselves against existing implementations.
Right? So if people are saying like the package size is too large, right? Or like the load, time is like too slow. It would be good to have benchmarks from the implementations we're comparing ourselves against. So we can say, like.
Well, what do we think a reasonable package size is, what do we think a reasonable load, time or overhead is?
so we want to establish a test harness for our own thing, but also get that information out of other existing implementations. So we kind of know where we're at.
And also so we know where the existing Javascript stuff is at.
So we know the gap that we have to close before we start writing stuff.
It seems like maybe part of that is also making sure our implementation is doing the same work as some of these other implementations, because that could skew. A lot of these numbers, it seems to me, especially if you're talking about performance benchmarks.
you know. If they're doing different work, then they probably will have different characteristics.
**Dan Gomez Blanco** 15:15 Just so that we're makes sense.
Just so that we're comparing apples to apples on that benchmark as well in terms of like, you know bundle size.
And this is a question for anyone. Would you see, like we want to compare the initial I mean the whole bundle size like it's downloaded with like some browser agents where you've got like the you know, the little snippet that you put in the head, and then retrieves the rest.
which is not the approach that you know we follow in hotel.
or would we say we want to compare everything that is part of the agent right?
Because I think you know.
**scheler** 15:56 We.
**Dan Gomez Blanco** 15:56 And.
**scheler** 15:58 We might have that info already. Right, I think. Some of the vendors are like, especially honeycomb, and some of the newer recent companies. They are all in on open telemetry so we could look at, you know the bundle sizes that they have.
Would that be helpful. And and I it's not going to be a surprise that the bundle sizes, I mean the the sizes are going to be larger than you know. The the legacy agents because they did not have so much abstraction layers the the you know the the traces versus spans. Sorry that spans versus events. Distinction wasn't there?
So it's are you looking for? How? How? What is the Delta? How big of a size it's going to be or.
**Ted Young** 16:52 Yeah, I think a lot of the work we're doing in this group seems to be optimization related.
Some of the work is like, are we providing the same data? Right? Is the data that comes out of hotel just as good as the data coming out of these other implementations?
The answer at the beginning is probably gonna be no, especially for, like older, more established implementations, because they have, like so many features we aren't going to like provide every feature that the new relic.
you know, web agent is currently providing, like right out of the box. Right? We're not going to do everything that sentry does.
But for the things that we are doing, I think we wanna like.
compare whether we're providing data that's just as good as these other implementations, or just as useful to those vendors.
And then within that subset, if everything else we're talking about is like optimization of some kind saying, like our current implementation is suboptimal.
I'm always very nervous about diving into optimization work without 1st establishing like goals and benchmarks, right?
Because it's all like trade-offs that you have to do to get this. So it seems like we should be trying to like extract our our goals and benchmarks for these optimizations from measuring the alternatives that are out there.
or at least getting some some baseline for understanding like what these goals should be.
Does that? Does that seem reasonable to you?
**Martin Kuba** 18:34 So so, Ted, my thought on this is, and maybe question is so. I thought that the the phase one of this project would be, as you said, just making sure that the Api is is good and building some basic instrumentations.
So this, this work on the harness and that seems like more like of a prep. Prep. Work for phase 2. Which would be optimization.
**Ted Young** 19:02 I mean, I think, to some degree, the the Apis and instrumentation packages are like part of the problem, right in terms of like performance and and sizes and everything else.
But so I guess it's sort of like, what what amount of this work do we need to get going to to actually evaluate the work we're gonna do in phase one.
**Daniel Dyla (Dynatrace)** 19:33 I I think that we I mean, we know that the the Hotel Api and SDK. Are too big, so like comparing it to the legacy app like, we're just gonna find out that they're too big. We we already know. I think the answers to some of these questions.
To me. It seems like collecting all of the like. The attributes and data collected by all the various legacy agents is maybe going at the problem a little bit backwards, because I think we need to focus on like the core, like bread and butter used cases. And I think you're also gonna find that every single one of the legacy agents handles those well like they have to, otherwise they wouldn't still be around and then there's probably a long tail of features that are like less.
You know, not every single user needs them. But that's where the interesting differences come. But I think that will come much later down the process. I think what we should identify are like the core use cases we know we want like page load timings and stuff like that.
We know that every legacy agent is gonna do that just fine. So I I think that we're probably better off identifying like, what is the minimum set of useful instrumentation.
As opposed to saying like, what do all of these legacy agents do, and and what features do they provide.
**Ted Young** 21:05 That's fine!
**Daniel Dyla (Dynatrace)** 21:05 So maybe maybe we're better off talking to like an end user than a vendor to say, like, what what are the minimum like?
Would you use it if it only did these 3 things? And if the answer is no, then it doesn't matter how big the bundle is, because if it's not useful to them. Then they're never gonna use it.
**Dan Gomez Blanco** 21:27 So that minimum set of instrumentations as well is what we're what you're saying as well as the Api That's needed for it, right? But.
**Ted Young** 21:38 Right.
**Martin Kuba** 21:40 And I would argue that we know, like what at least a few like that don't exist right now that we should definitely do.
**Daniel Dyla (Dynatrace)** 21:49 Yeah, I think that the 1st ones are obvious, like they should be obvious.
the, you know, like I said the page load time everybody knows that that's gonna be. I I think the 1st few should be really uncontroversial.
**Ted Young** 22:05 Okay.
I think that's that's reasonable. And I think the work already been done by this group that Martin just showed is probably like a very solid starting point for figuring that out.
**Daniel Dyla (Dynatrace)** 22:21 Right like I, I would look at the like. We have a set of some Comp. Prs. We would page view navigation resource timing there, there's like a handful of them that already exist. Are there any of these that we don't believe are that should be in that like minimum set?
And there's any. Is there anything we think that's missing? I think we should.
Yeah, I I would lean more towards like, let's actually start getting something that works with the existing Api and SDK, that we know have limitations.
And start producing data.
To see. You know how bad actually is it once you minify and bundle everything together, how bad actually is the impact.
**Jared Freeze (embrace)** 23:11 So I actually have ours open right now. So this is G. Zip. I don't. I don't have the raw right right this second. But it's 30 K with web vitals, and that includes Xhr and fetch everything is like, everyone's right like you need that. So I don't think that's crazy. Non, G, zipped is probably something we should look at. Obviously, look at both. But yeah, I don't think that's a wild place to start, you know, if there's something else that should be included, that's fine, but that that's also including a couple of things that we had for extra page load stuff which is negligible. I mean, it's nothing. G. Zip, it's under a K. So just to give you an idea of where we're at.
**scheler** 23:52 And and just to be clear, does that include the logistic as well.
**Jared Freeze (embrace)** 23:57 Yeah.
**scheler** 23:58 I see.
**Jared Freeze (embrace)** 23:59 So yeah. Api trace base xhr, fetch logs.
Core.
**scheler** 24:10 Okay.
**Daniel Dyla (Dynatrace)** 24:11 But not traces.
**Jared Freeze (embrace)** 24:14 Yeah, trace is in there.
Excuse me.
**Daniel Dyla (Dynatrace)** 24:16 Okay.
**Jared Freeze (embrace)** 24:17 It's try truncated, because it's like a that box. So.
**Daniel Dyla (Dynatrace)** 24:22 And is that using the otlp Json exporters.
**Jared Freeze (embrace)** 24:31 That is, no, it's not which should be included.
That's that's separate for us.
**Daniel Dyla (Dynatrace)** 24:37 Hmm!
I think the exporters are gonna be likely some of the most impactful on bundle size right now.
**Jared Freeze (embrace)** 24:48 Got it.
**Ted Young** 24:51 So like one approach that I think could be really fruitful would be to take, basically build the equivalent bundle of what Jared was just describing that embrace ships right? Like like.
take that, that basic set of things. We're we're trying to target page load Xhr, etcetera.
build out any instrumentation. We're missing on that front. Improve the stuff that we have with our current Apis, and then like ship that right? And then we can say, like, Here's our working thing that works that provides this core set of functionality. You can use it today.
And then we can look at the bundle size and everything for what we're currently shipping and like where that's coming from. And then we can add the new Javascript Api and see how much like that changes everything for us.
**Daniel Dyla (Dynatrace)** 25:52 Yeah, I mean, we have, like, we have the demo app, which I assume is already using the stuff that currently exists. Has anybody done like a a bundle. Analysis on the demo app to see how much of it is actually like from the instrumentation.
The demo apps a little bit different, because they tend to turn on like every single possible knob and feature.
because it's a demo.
But it might be a good place to start.
**Ted Young** 26:25 Yeah, I'm not sure what the browser the state of like browser instrumentation is in that thing.
But we can have a look.
Okay, well based on the discussion we just had is like just getting instrumentation packages written for these different things like, is that actually like step one for this group.
**Daniel Dyla (Dynatrace)** 26:56 I would say, yes, I think that that's step one. And then from there, once we have something that works, we can look at it and say, Okay, what is actually contributing to this? Like, if 30 of the bundle is the exporters, then maybe that's where we want to spend our time, instead of like rewriting the Api or the other way around. Who knows.
**Ted Young** 27:18 Yeah.
I mean, one thing I will say is that the thing about the Api is we want that thing stable, right? The problem with building the instrumentation and stuff first, st and then the Api later is like we have, like a lot of the more of that we have out there, the more thrash happens when we're messing around with the Api. Maybe that's not a big deal.
But you know, if we were gonna like ship this to people.
**Daniel Dyla (Dynatrace)** 27:50 Yeah, I mean, since we're the ones writing the instrumentation, I think you know.
causing thrash on yourself isn't always the end of the world.
And the Api is currently out there like people are writing instrumentations for it. So if we're gonna change the Api, we're already thrashing them anyway. So. Whether we do it now or 2 months from now, I don't think hardly makes a difference.
**Ted Young** 28:11 Not. I don't mean to sound dismissive about that.
I mean it, I guess. Given that we aren't doing any kind of breaking change for the Api. It would be like a separate thing. The old one would still work so.
**Daniel Dyla (Dynatrace)** 28:24 Yeah, the old one will continue to work is my assumption, for you know, a long time, possibly forever, hopefully, forever. If we can make that happen.
**Ted Young** 28:34 Cool.
**Martin Kuba** 28:35 And and, Dan, am I? Am I correct that it's like the signature of the Api will not change like the way the instrumentation interacts with the Api will not change. It's just like behind the scenes, the implementation, how it talks to the SDK.
**Daniel Dyla (Dynatrace)** 28:48 That's kind of an open question, so that the Poc that I wrote is not really meant to be like a suggestion for what we should do as much as it is like a if I started from scratch today, what would I have done differently? It is. The signatures are different. Everything is broken like there's no like. One of the main problems that the Api has is that everything is namespaced which means, like you have to call like trace, dot, star, span, or whatever which means that it's not very friendly to minifiers.
All of the code is is class based and namespace based And today, if I was gonna start it over from scratch, I would not have done that.
I have to say the main reason that I started writing that Poc, in the 1st place, had nothing to do with minification and code size.
It had a lot more to do with the extensibility of the Api and adding new features to it, especially experimental features in a way that doesn't require every single SDK to constantly update all the time, and users to be, you know, very right now. The version compatibility story is.
it's okay. If you know all of the underpinnings. But as an end user who doesn't? It's confusing.
So that was the main problem that we set out to solve. And then the the bundle size and Esm publishing, and all of that is just like now I have a lot more experience with that stuff than I did when I did it the 1st time.
so I know, you know I'm starting from a better place. They're we could do like a very breaking like rewrite like that, but I don't know that that will be the best idea. The other thing that we could do is build on top of the existing Api new versions, like new non namespaced versions of things that the namespaced versions would just call. And then, when you bundle your application together hopefully, the namespaced versions, as long as you don't use them would be tree shaken out, and it wouldn't be a problem that relies on things like tree Shakers.
To do their jobs correctly.
which I have found is not always a hundred percent the way to go.
But yeah, that's kind of where my head's at on that I wasn't. I didn't make that poc as like a I think we should do this. It was more of like a a thought experiment that said, it is way more efficient and essentially every possible way. It's like 10% of the code bundle size. And I, it's significantly more memory efficient, which matters a lot more in node, I think. But does it not matter in browser.
**Ted Young** 32:06 Yeah.
And I would say, you know, as long as we could do something like we did with open tracing, with like a bridge pattern.
you know, there's like different approaches. But like I think it's totally fine to to have a bunch of breaking changes in the Api. If the old Api can still continue to function in some way.
**Daniel Dyla (Dynatrace)** 32:31 Yeah. So in my mind, there's.
**Ted Young** 32:34 You know, or so the SDK doesn't have to think about it anymore.
**Daniel Dyla (Dynatrace)** 32:38 There's a couple of ways to do it. One the SDK. Could support both Apis that complicates the SDK. And some of that stuff.
The old Api could be updated to call the new Api which then depends on you having a minimum version of the old Api, but is better than nothing, or we could have. We could publish some bridge like dummy SDK, that like registers itself with the old Api and calls the new Api.
that's obviously like from the end user perspective in terms of bundle size and performance, probably the worst of all worlds. But it is the easiest for us moving forward, and the assumption would be that eventually users would be on the new Api and wouldn't have to use that. And they could drop it, and it would be like the cleanest long term solution.
Yeah, so those are. Those are the options in my mind, open to other suggestions.
**Ted Young** 33:37 It sounds pretty reasonable. We're out of time on this call.
But I felt like I have some more clarity on how we should attack this.
So I'll try to help organize that a bit more in the backlog and see if we can maybe get some of this unfinished stuff assigned to people.
**Daniel Dyla (Dynatrace)** 33:56 Yep, Martin, do you have like 1 min to talk about the open semcom Prs.
**Martin Kuba** 34:01 Yeah, I do.
**Daniel Dyla (Dynatrace)** 34:02 In in the simcom meeting. They were trying to triage the project board, and they we have these open browser Prs, some of which are like reasonably old.
Very old, unreasonably old in some cases, and they want to know what the state of them is. Are they expected to be revived and picked back up or closed, and I reopened under new owners, or like, what? What is the current state of our our existing Sem. Comp. Prs. And the reason I'm picking on you is because you sent that message earlier yesterday.
**Martin Kuba** 34:37 No, I would hope that we finish those Prs as part of the work we do in this in this group.
**Daniel Dyla (Dynatrace)** 34:43 Okay.
**Martin Kuba** 34:44 Yeah.
**Daniel Dyla (Dynatrace)** 34:45 So should they. Are they ready for? Are these all ready for review? And and whatever do they have prototypes, and such, or like when when they ask, what is the state of these Prs. I don't know what to tell them ever.
**Martin Kuba** 35:00 Yeah, they're they're definitely ready for review. We don't have prototype instrumentations. Is there something that would be, you think good to have? Because we can build that easily. But yeah.
**Daniel Dyla (Dynatrace)** 35:21 Yeah, I I think we should have prototype instrumentations. But even though we don't, I think at least now I have a better idea of what the state of these are. So next time to ask. I don't have to just tell them I don't know.
**Martin Kuba** 35:32 Yeah, I'll let me just make sure that before next next meeting I'm going to make sure that there's no open comments on the Prs. But I would ask this group again, maybe I'll just set a reminder in the slack channel for this group to to take a look at those and and add their comments.
**Daniel Dyla (Dynatrace)** 35:49 Yeah, I think from the Sem Comp group, that's really what they're looking for is they don't feel like they can review them because they don't have the expertise. So they're looking for the people from this group to to say like, this is the direction we're going, or it's not.
**Martin Kuba** 36:04 Yeah, makes sense.
**Daniel Dyla (Dynatrace)** 36:06 So, yeah, maybe we should get should harp on people in slack a little bit more to start reviewing these, or like.
pick one of them and say, we're gonna RAM one of these through and and bother everybody all the time until they actually review it.
**Martin Kuba** 36:23 Okay.
**Daniel Dyla (Dynatrace)** 36:25 Okay.
Sounds good.
Thank you.
**Ted Young** 36:31 Is.
**Martin Kuba** 36:33 Next week.
