SIG: Browser SIG
Date: 2025-07-17
Duration: 30 minutes
============================================================

## Zoom Recording Transcript

**Martin Kuba** 02:05 Hi, everyone.
How's everyone doing?
**Jared Freeze (embrace)** 02:12 Hey? How's it going.
**Ted Young** 02:14 Hello! Hello!
Do you all?
Dan should be here in a minute. We were both just at the entities, Sig.
which is going to be our sibling sig for a bit, I think, while we sort out session management.
Alright. Looks like we've got some things in the agenda feel free to add more things to the agenda.
Do you have something, and to kick it off?
Martin.
**Martin Kuba** 03:53 Yeah, I mean, I don't have much to talk about this, but I don't. I did see that. When you created the board.
there's a session manager on the board, and I just wanted a reminder that there was a work in progress on this from probably probably a year ago.
So please take a look at it. Yeah, I don't know if I don't know like if there's more work to be done on that. But it's I think it's a in a prototype state that can probably can be run and evaluated.
It's based on right now. It's based on. Still, like the the processors.
so I could add stuff session. It's session id attributes on all signals like I said, but it's it's a separate from from the entity provider. Essentially.
**Ted Young** 04:54 Right. See? Seems like we'd wanna update it to to work with them.
**Daniel Dyla (Dynatrace)** 05:01 Unfortunately, I think entities is not quite far enough along to prototype something like this. I think we're getting quite close, though.
**Martin Kuba** 05:12 Yeah.
So the idea with this was like, I don't know how long it's gonna take to to get the entity provider or entities like done so like. In the meantime.
you know.
could we implement something that adds the session? Id attribute? And I think, even aside from that, I think this this design for the session management is still separate, like I mean, there's it. It involves like, how would you configure session management in in the web application. Aside from how the data is sent.
So.
**Ted Young** 05:46 I think that makes sense. I think it makes sense to to add it in its current state.
When we figure out entities, this thing basically won't change right? We'll just change its update mechanism.
**Martin Kuba** 06:00 Correct.
**Benoît Zugmeyer** 06:05 Hey? Hello, I'm from Data log. I'm working on the SDK, and I want just to give a bit of feedback that from my experience, and we have a lot of trouble when reading and writing the same cookie or value in local storage in from different tabs or windows at the same time.
There there are concurrency issues that could be solved by using the the lock Api or the the the Cookie store Api, and and just what what I want to say is, I see that the the current Pr is fully synchronous like you, you get the the decision.
And you, yeah, you read decision from whatever. And your decision. And you expect that to be written.
And if we could change those Apis from synchronous to asynchronous early on in the design that would help.
Future iteration! I I think.
**Jared Freeze (embrace)** 07:26 So are you. Are you suggesting, like broadcast channel and local storage.
like sending an event between tabs potentially.
**Benoît Zugmeyer** 07:37 We we don't need to to send event between tabs. We there is already some Apis to to work on this kind of issues like the lock lock. Api.
we we don't need to like. I I understand that it's a prototy prototype, and we don't need to think about this just how?
But maybe if we can just change the types to. So it's asynchronous instead of synchronous. It could help us in the future.
**Daniel Dyla (Dynatrace)** 08:14 I think what you're referring to is that the Cookie store Api is an asynchronous Api, right.
**Benoît Zugmeyer** 08:20 Exactly. And the locks. Api, too. Yeah.
**Ted Young** 08:27 Yeah, I mean, I think that's that's fair to keep in mind.
the this kind of dovetails with the next thing I wanted to get into, which is just kind of general backlog management. We're trying to still sort of put all of the pieces together.
but one piece that, I think, comes up across the different kinds of work we're looking at. So just to let me see if I can pull this up on my screen real quick.
So I've been putting a backlog together.
Trying to use github projects.
maybe, in a way that's a little more leveraged than we've tried to use it in the past.
And I've come up with kind of like 2 main views that seem helpful.
One is this kind of like roadmap view and at the high level I've kind of broken down our work into what seems like a set of work streams. So the overall work stream is like browser phase, one that collection of stuff we've agreed to do. And the pieces that seem relevant that we could do potentially in parallel. We have a whole bunch of work on semantic conventions that needs to get done including some meta work and kind of like organizing our backlog of work around semantic conventions.
Sessions is just a big piece that we've seen. That touches a lot of things. It's like the last big piece of our data model that we need to sort out. That isn't just semantic conventions, as far as we can tell.
And it dovetails with all the entities stuff that's going on. So that's his own kind of separate stream of work.
And then we know we want to improve the open telemetry. Javascript Api, and we were initially thinking we might need to make a browser specific. Api.
But Dan's done some really good prototyping work to prove out that maybe the Hotel Javascript Api could be Redone in general in a way that would make everyone happier and would totally work for our browser problems around package size and things like that.
I was excited and totally sold by that prototype.
So I think there was general consensus that we move forward using that prototype as kind of our starting point for Api exploration.
**Daniel Dyla (Dynatrace)** 11:43 Yeah, I've been. I know that I promised to do a a presentation about the benefits of this Api and the way that it works. I have been unfortunately haven't had time to do that. There. There are some things in the read me about it. And obviously the code is the code anybody is willing is welcome to read it.
but I don't have a presentation ready. Unfortunately.
There are quite a few of the things here, I think, could be applied to the existing Api. But there are definitely some things specifically around deployment size where backwards incompatible changes are gonna have to happen, and I would reiterate again, I would be way, way happier with a new Api, and then some way to bridge them together as a temporary workaround for people who haven't updated yet.
That eventually probably goes away. Or you know, it is something like that. That's used in both places, I think.
moving forward with 2 Apis for any period of time more than like a year or 2.
I think it's not not feasible.
**Ted Young** 13:00 I I think When it comes to like versioning Apis, you'll often hear us say, like, we're not going to do a 2.0. And I think that does hold in the sense that. Yeah, we're not going to mutate an existing Api and break it and put people in a situation where there's a 1.0 and a 2.0. And instead, the approach we've always looked at in open telemetry is that we would just create a new additional Api, and under the hood the SDK would make both the old and the new Apis work together.
And this isn't even like a new untested concept in open telemetry. This is exactly how we provide support for open tracing. Right? So Otel already has 2 tracing Apis has the open telemetry tracing Api, and then it also supports the open, tracing Api through a bridge right? We'd get on a world where we'd have a new Api, and that would become the native one, and the old one would work through some kind of bridge.
and then eventually we would retire it. But ideally we would just leave it in a functional but deprecated state for all eternity. If we could get away with it.
**Daniel Dyla (Dynatrace)** 14:25 Yeah, I think functional but deprecated, is probably fine for the old Api. Whether we do a new package name or a new version, I think matters less to be honest, I think it would be fine both ways.
**Ted Young** 14:38 A very language specific thing.
There's some languages where it's easy to have multiple versions of one package pulled in to the same package and have that thing juggle references to both of them. And there's some programming languages where like, that's hell. And you don't want to inflict that on yourself.
But anyways getting back to backlog management. There's an Api and a prototype for it, and we want to keep working on that and it would be great to get the details from you, Daniel, on your proposal.
But we've got plenty of other work that we also need to stand up, including a test harness for this. Api and I kind of suggest we almost get started on this piece first.st Because a lot of what is driving our motivations. I'm noticing behind changing things. To make it work in the browser is a lot of like optimization, right? Like there's a number of things you could certainly quantify as targets we're trying to hit. And it seems reasonable to me that we start by identifying what those metrics are and what we think like an acceptable target, would be not the best thing ever right, but like what is an acceptable like package size, for example, was, if we are caring about like load times or other things like that just identify those metrics and identify what a reasonable bar would be for production, release.
and just get that stood up early.
So we have, like our baseline of our current Javascript, 1.0 system.
and then maybe we can get baselines against other systems, or at least measure other systems. So we know that the baseline we're pick target we're picking for ourself is is something comparable to what other systems are doing and not just an imaginary number we made up.
So that's kind of like the last line of work that I see. How does that feel to people like these these 4 tracks of work? Does that feel like one like a good way to kind of differentiate the work that we currently have on our plate and 2. Do you think I missed something.
**Jared Freeze (embrace)** 17:24 I don't think you missed anything.
**Ted Young** 17:26 Well, Martin.
**Martin Kuba** 17:28 Yeah, I was just gonna say like, and I don't wanna like stir things up. But and I know that we have this is like the phase one, and we'll have a phase 2 which will focus on instrumentations. With that, said I just want to put it out. There is that.
you know we could have some quick wins by by just finishing some instrumentations that we have in progress, like we have the errors, instrumentation, and some the web wireless instrumentation that would give that we could probably finish quickly and then give users something to use like the users are already using open telemetry for web. But there's a lot of missing missing data that's not being captured. So like optimizations are great, and I think it's going to take a long time, though, to to do optimizations.
So we could provide some value very quickly from from the get-go.
**Ted Young** 18:25 I think that's a great point.
Right? Like getting to like an end to end working system that people can use feels really good, and we should definitely put a premium on doing that.
I think the only question here is like the 1st stage of this work is completely redoing the instrumentation. Api. So if we also start working on instrumentation at this point.
that stuff, I guess it's either we would write it with the old Api, and then just not touch it.
for now, or it would be kind of like a a moving target.
which is maybe something we want to have while we're working on the Api, but that's.
**Daniel Dyla (Dynatrace)** 19:12 Think.
**Ted Young** 19:12 Chat.
**Daniel Dyla (Dynatrace)** 19:13 It would be helpful, while we're working on the Api to have some instrumentations that use it so that we can get feedback directly. I also think that it should be fairly mechanical changes. I I don't expect the Api to work fundamentally differently.
From the perspective of like all the same methods like start span and span. You know the the emit event, whatever it is, that they will have all the same Apis, just instead of having namespaced calls. We'll have direct function calls.
It should be a fairly mechanical process to update to the new Api. At least, if you were to.
If you were to take my prototype and say, this is now the Api. It would be a very mechanical change to update to it from an instrumentation perspective.
And I expect that to be the case. So I I guess that it's a vote for use, the existing Api, to build some instrumentations and then use those instrumentations to inform the new Api as we design it.
**Purvi Kanal (she/her)** 20:21 Yeah, I, wanna.
**Ted Young** 20:22 That's great. Sorry. Go ahead.
**Purvi Kanal (she/her)** 20:24 I want to, plus one that as well, maybe not for anything like complicated or net new. But in the case of exception and web vitals instrumentation at least. The honeycomb distro has versions of this that I want to just get upstream so that everybody can use it.
and they're they've already kind of been tested because there's a lot of people that are using them. We have unit tests in place and stuff. And it would just be great to for them to live in open telemetry. So it's more of it's not even like writing that new and instrumentation as much as it is like donating stuff that we kind of know already works.
**Daniel Dyla (Dynatrace)** 21:05 Yeah, there's stuff that works and exists with the old Api already, and I don't see any reason to throw that stuff away.
**Ted Young** 21:11 Yeah, so that actually dovetails with a certain kind of information just lost my headphones.
**Daniel Dyla (Dynatrace)** 21:26 My headphone. Oh, you stopped working. Okay.
**Ted Young** 21:28 My advert.
My head stopped working. Sorry? So there's something I've noticed like across all of these different work streams there's a bunch of like pre-existing work. It feels like, basically everyone on this call works at a company that already has a solution to browser monitoring right? And they want to switch to hotel. But there's like a couple of things. I think we want to know about our existing systems, and it would be great. If someone from you know, each participating organization maybe went back and just like did an audit. So one task, I think we could maybe finish out this meeting with is coming up with the list of qualities or inventories that we want to come up with, right? So like top of mind is like, if we just go through our work streams right? So semantic conventions. One is like, what? What is the list of events that your existing implementation already captures right. It would be great just to get that list from everyone and have our initial support list. Just be like that. The union of those lists that way. We at least know no one's losing information by switching to open telemetry.
Sorry. Go ahead.
**Dan Gomez Blanco** 23:00 Do you think that that for phase one, or like having that full list, and then prioritizing some of our ascritical? And then.
**Ted Young** 23:09 I mean, I think we can see how long that list is. But I think 1st thing 1st is just to get the list, and then and then we can just like prioritize the ordering of it.
you know.
But I think it's fair to say to go into production like phase one is like, unless someone comes back. And they're like.
our implementation has been around for 30 years and it captures 4,000 different discrete events. And we're like, Okay, well, maybe not you, but for everyone else like we can probably come up with what we think is a reasonable starting point. But ideally it would be everything that we're currently collecting.
I think it would be a bummer for someone to lose information because they're switching to to hotel. Seems like they wouldn't be able to switch until we added, whatever it is, their current system does so for the participating orgs.
We should do it.
Okay? So that's semantic conventions test harness. Whatever metrics, benchmarks, we think we wanna hit for a new implementation. It would be great to get that same benchmark for.
**Joaquín Díaz** 24:33 For.
**Ted Young** 24:34 Dynatrace.
**Joaquín Díaz** 24:34 Just want to.
**Ted Young** 24:35 Or sorry. Go ahead.
**Joaquín Díaz** 24:37 Sorry I I did share a doc for this one on what we capture at embrace.
And maybe it can be useful. There are some test case that are like more like a fleet testing behavior. But I also mentioned a few metrics that we are looking at.
**Ted Young** 24:51 Great.
**Joaquín Díaz** 24:52 We don't have specific numbers on what we wanna see that we just came up with some numbers, and we're still validating those numbers.
But, as I said eventually, we can cross check with other tools and see like, why is the average and try to hit that or be better, or whatever.
**Ted Young** 25:10 Great.
**Joaquín Díaz** 25:12 yeah. Feel free to take a look at that list. And let me know. Like, if there are any comments or anything you can add, there.
**Ted Young** 25:19 Right. That would be great. And that's maybe research for everyone. You know. Dynatrace, new relic, honeycomb, Grafana labs, Microsoft like for your existing room solution. Do you have benchmarks like? What numbers do you track yourself already?
Around your existing implementation? So those are probably the numbers we want to track.
**Dan Gomez Blanco** 25:47 So in terms of artifact size as well. I guess.
Probably worth mentioning that you know the different approaches that RAM agents tend to take right with the loader script that then fetches the the rest of the of the agent, so, like the initial load, will be.
**Ted Young** 26:03 Right.
**Dan Gomez Blanco** 26:03 A lot, you know, lower, but then you lose the rest of the of of the agent. So that's a different approach that you know. I don't think that's the direction here for now, at least, for now that is like, you know, we just.
**Ted Young** 26:17 I I think the direction is to get to get the test harness so that you could compare those approaches right like you'd want to.
**Daniel Dyla (Dynatrace)** 26:27 Why is.
**Ted Young** 26:27 That trade-off.
**Daniel Dyla (Dynatrace)** 26:29 That relies on something like a Cdn as well. Which obviously we could do. But it it complicates it a little bit.
**Dan Gomez Blanco** 26:41 Yeah, exactly so. But anyway, having the to your point, yeah, having the benchmarks and the data, probably that's the 1st step. Yeah.
**Ted Young** 26:48 Yeah, I also, I don't. Testing environment. I don't know what's out there. Maybe people have recommendations beyond github actions like for simulating mobile.
mobile environments. I don't know if there's like something useful.
**Joaquín Díaz** 27:12 So we we use pay right? Currently, we are not running on mobile devices just running on desktop. Pcs.
I. We consider that, for now is not worth it like But what we capture is the same. Whether this a mobile device or not, like we we wanna know, but I don't think it's important yet for our test. But in any case, we use browser stack for other stuff, so that can also be useful.
**Ted Young** 27:48 Yeah, I meant more for like simulating.
you know, bad mobile network environments and things like that.
Anyways, probably not something we need to worry about yet.
But knowing if we're gonna make a test harness, just knowing what numbers people care about to track right, what should our initial set of metrics. B, that's something.
I think it's just homework for this group.
Go look at what you your company currently cares about and come back and say we care about these numbers.
and I think that's it.
I don't think it relates to sessions at all, but but in terms of getting information back from from each company about your existing implementation. Just what events do you currently capture?
What metrics do you care about? And then I think the last piece is donations. Right?
So instrumentation, or like, what? What stuff do you have sitting around in your implementation that you were hoping to to upstream in some way to open telemetry. It would be good for us to just start getting a list of what people are interested in upstreaming.
So we know what we have.
**Daniel Dyla (Dynatrace)** 29:30 I think that's time. Do we have an owner for the testing topic right now, somebody who's driving that Joaquin you posted that Doc.
**Joaquín Díaz** 29:42 Yeah, I I'm going to be out for 2 weeks, so I can own that. But just know that I'm not going to be joining the next 2 meetings.
**Ted Young** 29:54 I threaten to turn everything in this backlog into actual issues in the Javascript repo.
I can go ahead and do that, and I'll create issues for what we just discussed, so we can get people to sign up for saying they'll they'll deliver their report back from their company about like their current implementation. So I think we need an issue to track that.
**Daniel Dyla (Dynatrace)** 30:24 I promise to ask. I cannot promise to have answers by next week.
**Ted Young** 30:31 Yeah, cool. Alright good seeing you.
**Daniel Dyla (Dynatrace)** 30:38 It's.
