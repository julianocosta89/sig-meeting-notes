SIG: Browser SIG
Date: 2026-01-15
Duration: 35 minutes
Zoom Recording URL: https://zoom.us/rec/share/WwveriJIDIZ9BpCMCDGnAcQFZudBdh4kNlcrXCM3NwyLmZv45oI1N56K5yXSq859._yRysZugdl4loFX2
============================================================

## Zoom Recording Transcript

**Jared Freeze** 02:45 Hey, everybody.
**David Luna Bistuer** 02:51 Hello, good morning.
**Martin Kuba** 03:29 Hey, everyone.
**Jared Freeze** 03:44 So, Grace, who posted, it looks like is not here?
But… I think… She had something for the agenda?
I don't see it on the agenda either, so… just kind of hoping to go over that.
But, you know what I mean…
**Martin Kuba** 03:59 Yeah, I think she was here, I saw that.
She put it on the agenda, and then she took it off.
Seems like… but I actually had a question about the timeline of the Phase 1.
of our Phase 1.
So maybe we can talk about that a little bit.
**Jared Freeze** 04:24 Okay, yeah, we'll do it after your stuff gets listed, I guess.
**Martin Kuba** 04:27 Okay.
Yeah, I guess we can get started. I do have a couple… Things on the agenda,
And they're both related, actually, so we have… we have a PR for council instrumentation.
Open. If you haven't looked at it, please, please take a look at it, and more reviews would be appreciated.
There's a feature that the author added, which is, for the… for the logs?
That the instrumentation generates, like, if there is…
If the page has a meta tag.
With the context, with the trace context passed in from the server.
Then, that context is attached to those logs.
That, that functionality was implemented in the document load, document load span instrumentation that's been around for years.
But I'm… but I… which makes sense there, I'm not sure if it makes sense for… for this instrumentation, or, like, in general for all types of… all instrumentations that generate
logs, so my question was gonna be, like, do we…
should we include this? Like, do we have any opinions about, This, this feature.
**Wolfgang Therrien** 06:01 I've definitely seen customers
ask for that kind of parent-child relationship, right? Where they can easily see what has been associated, right?
you know, I see the, you know, the bullet point below, Martin, about sort of, like, other network requests, right? I think a lot of customers expect to see, like, hey, this is the page,
trace, and then these are all the things that happen under it. I don't necessarily know whether to call that correct or not, but I know that that is something folks are expecting to see.
And so it could be something where
maybe it needs to be configurable in some way? It's not quite… I haven't thought about it too deeply, but, like, it seems…
We might want it in some cases, but not others.
**Martin Kuba** 06:59 Look, my kind of… my mental model about this, has been…
That we've decided that we don't want to represent the whole page lifetime as a trace, right? Like, we have the session for that.
And maybe we introduce another attribute to tie all the different events on a page.
So, like.
But it makes sense from the use case of if I want to… if I'm surveying a page.
And then I want to see, like.
the, like, how long it… while the page was loading, so I want to see that relationship, that makes sense.
So, I guess, how would it be useful, like, if you had, like, a page that lasts, you know, minutes or hours, and you had, like, you could associate
Some random console event down the line with the original
backend trays that serve the page. Is that… is that useful?
**Jared Freeze** 08:13 Yeah, I mean, I think it… I think it is. Only because, you know, if you have a query, right, like a SQL query or something that is feeding this page, and then somebody just doesn't interact for a while, I think it's still relevant if they do something in the UI that is directly tied to that. I mean, the document is the backend in a lot of ways, so…
The question is, do we default or not? Because I think some people are… are using it, right?
So, that's… that's the question, is like, is it optional? Do… do we use it if it's there?
**Daniel Dyla (Dynatrace)** 08:47 I think if you do something…
If you do something down the line that, like you said, triggers a SQL statement of some kind.
That would be, I mean, a new…
XHR or fetch request, which would trigger a new trace, and you would associate it with that one, not with the initial page load. The only way that I would see wanting to associate a log with the initial page load would be if something in that initial page load caused that log, but just much later in time.
Which… is theoretically possible, but I think is not the common case.
**Ted Young** 09:27 I'm curious, you know, we have session ID, do existing solutions also do, like, a page ID or something like that?
like, I don't think I would want to use a trace to look at this, but if you're saying, like, we want to be able to index and associate everything
That loaded on this page, so there's some way to just quickly access all the things associated with this page… page versus a session.
Maybe that's, like, too fine-grained, but that's the only other thing that comes to mind.
**Benoit** 10:01 I opened an issue to discuss this kind of thing, and… Let me show it…
There is already a bit of comments there.
We are talking about document.instance.id, for example.
Yep.
**Martin Kuba** 10:28 Yeah, I think this would be useful, like, we just need to… I think we just need to figure out what that…
Attribbooth should be, yeah.
And I think… I think this… this trace ID passed… passed in from the back end. I think it's a separate…
thing that, like, I'm just… like, if he… if you really think that it's… there's a use case for it, then I think what we should do then…
Let's figure out a mechanism to apply it to all signals that we generate in the browser, not just, like, random ones.
No.
**Benoit** 11:03 Yeah, I agree. Maybe it makes sense to have it for the navigation and navigation timing?
I… I really… Do you see that?
Like, having a way to correlate, like, client-side timings with the backend span.
It's a good thing.
I think at Datadog, we do something like this.
But for random… for other events, I'm not sure if it's really needed.
**Martin Kuba** 11:48 Okay, I might, I might just ask the author of this PR to, like, remove it for now.
And…
Until, like, we can always add it, like, later, like, if he… if he have more use… actual, like, concrete use case for it.
**Benoit** 12:02 Okay.
**Ted Young** 12:03 Yeah.
I know that, like, back in the day on, like, organizations have concerns about IDs not generated.
You know, under their control.
So…
And, like, being able to spit a trace ID back to the browser so that it wouldn't generate it, so that all of your IDs were… like, it makes sense to me, but it, like, it feels like a solution in a world where you assume there's only one trace getting started by the browser, right?
like… So that…
Yeah, I don't know. And then you're generating your spans and everything else over there. So I kind of wonder if it's, like, an idea that's been sitting around for a long time, but is maybe…
Like, an outdated model.
Just in terms of what data we're trying to produce.
**Martin Kuba** 12:56 Yeah, I think so too.
Okay.
That's all I had on that, pavon, you have the next…
**Pavan** 13:14 Thanks, Martin.
Hi, everyone. I suppose this is my first time joining the browser-sig meeting.
I've been a sort of a regular participant in the GenAI SIG calls that happen almost every Tuesdays, and Ludmila has basically asked me to also, sort of, join the browser SIG and get some of your feedback.
Essentially, you know, like, what we are trying to do is, you know, we are, trying to define, like, new.
you know, conventions for, capturing, agent-to-agent interaction, you know, some, for example, like, multi-agentic, you know, sort of systems where there is explicit agent, handoff.
And, you know, we essentially want to ensure that we sort of capture the full end-to-end, you know, workflow of sorts, and the idea being that these workflows will span, like, multiple traces.
Right? And each individual, you know, like, Gen AI agent that you see could be, sort of.
decoupled, in the sense that, you know, one can start at any time, it can do a handoff using some of the agentic protocols out there, like A2A, MCP, for example, and then another agent runs for however long and then gives back the output, like, you know, to the user, and
We essentially want to tie in the user interaction with the headless, you know, agents, or even, like, the system
that, sort of, the user interacts with, which could be a chatbot. And those… and that chatbot could basically have, like, n number of agents all working, you know, in the background to accomplish that particular task. So, we feel that, you know.
In order to capture this whole end-to-end
quote-unquote session of sorts, and the fact that, you know, there is an explicit session.id within the GenAI, you know, attribute registry, we weren't sure if we could sort of reuse this
session.id within our GenAI namespace, right? Because, you know, we feel that introducing a new attribute, like, let's say, gen underscore AI dot session.id, could sort of be,
a bit, you know, problematic, because then there would be, like, some diff… like, somebody would ask, like, what's the difference between, like, the normal session.id versus this?
So, the fact that BrowserSig has already defined conventions, there is, like, clear, you know, semantics, and you have already documented who creates it, how it propagates, and things like that, we just want to see if, you know.
if there is any… if our understanding of session.id violates any of your assumptions, and, you know, we just want to see if there is any semantic consistency, you know, for this across namespaces.
It's sort of a loaded topic. I… I understand maybe, you know, I could link a document which sort of tries to explain what our rationale is, but I don't know if I sort of explained it in the
You know, last one or two minutes about the problem statement, and…
I don't know if you have any initial parts.
on that.
**Wolfgang Therrien** 17:08 Yeah, I think, like, session ID as a correlating attribute, I think could make a lot of sense, for… for things like agent-to-agent systems.
And I think, you know, coming from a client, like, that's where a lot of these conversations could initiate, right? And so being able to plumb that through, to your system, right, regardless of whether that's all the way back to a database call, or it's been handed off to some, you know, group of agents to do some work.
for me, that speaks to sort of what the intent behind a session… session idea is, so I think it's a perfect… it's a good candidate for reuse here.
**Ted Young** 17:48 Yeah.
I, I feel like…
The degree to which we're saying sessions are about a client having a sequence of arbitrary interactions, and you want to just understand this is all coming from the same client.
In that sense, like, what's going on…
with AI agents is basically the same, right? You have a client session.
If it's not basically the same in basically a client session, I think that would be a reason to pause. So maybe that's a thing
you all can explore in the Gen AI SIG. Is this really just a generic client session, or do we feel like there's something super special about these AI sessions, and they need to be modeled differently?
**Pavan** 18:31 It's mostly, like, a user-initiated task, right, that sort of spawns n number of agents in order to sort of help, you know, achieve that particular goal, in some sense. So, we were wondering if, you know, this reuse of session ID
could be, sort of, done, because, like, the general definition of session ID, sort of.
you know, also applies to us clearly, but we just want to ensure that, you know, the, the terminology, the, the way how, you know, BrowserSig is actually using it, in some sense, doesn't necessarily… or our understanding doesn't necessarily, you know, violate any of your,
Yeah, sort of conventions of sorts, but, yeah.
That's… that's the idea.
I know Ludmela did mention that she'll actually start a conversation in the,
in the Slack, you know, in the channel, but I feel, you know, maybe she was busy, but hopefully, you know, Friday or Monday, we could just have, like, an initial thread, but yeah, that's the intent.
**Wolfgang Therrien** 19:43 Yeah.
If… if there's a document y'all are putting together, or an issue where you might be outlining some of these, agentic use cases, I'd love to… I'd love to read it.
**Pavan** 19:56 Of course, of course. I'll link it in this Google Doc.
**Ted Young** 20:01 The other thing with sessions that's a bit of an open question is around entities, right? Like…
we want session to kind of operate as a resource, right, because we want it to apply to just all telemetry coming out, but it is something that changes, so the entity provider is seen as, like, a necessity.
To get around the fact that right now resources are mutable and can't change in existing implementations, and entities is still…
a little bit… You know, not fully baked yet.
And I think the one place where that is a bit of an open question is, like, in terms… long term, in terms of, like, marking, like, start session, end session.
You know, that seems to be, like, entity state changes and stuff like that, but then it's like…
if we're waiting on that, or it seems like that's not meant for this purpose or something, I could still see some other world where it ends up being, like, a start session event and an end session event.
So I just wanted to flag that there's a little bit of, like… we kind of all… want it all to work with entities, but, like.
We also don't… Want to get held back by entities anymore.
So, just letting you all know that that's… that's a bit of a situation that has to get sorted out until entities are stable.
**Pavan** 21:27 button.
Just one question. Is there, like, a sort of a way where, you know, in the instrumentations, you stamp, like, you know, when a session starts, when a session ends? Or is that sort of linked to the entities that you just mentioned?
Like, we just want to see, for example, in any of our libraries, there is this whole auto-instrumentation that, you know, we sort of use one of the callback mechanisms in order to define when an LLM starts, when an LLM ends, in order to capture most of the attributes, metadata. But for session, we know that, you know, given that it's sort of the client or the user who initiates it.
There needs to be some…
Way, where we can at least let the system know that, okay, this is the start of the session.
So, our thinking is that it needs to be, sort of, you know, explicit, explicitly sort of defined, but we don't know how exactly you are actually, dealing with that thing.
**Ted Young** 22:32 Yeah.
I think, Martin, you were working on entities and session management, right? You have a prototype of that?
**Martin Kuba** 22:41 So there is an implementation of Session Manager without entities, though. I worked on the entities prototype a long time ago, I think it was before there were some other decisions made since then.
So yeah, I'd love to get back to it.
**Ted Young** 22:57 Yeah.
But that's one of the open questions, Pavan, is like, you know, how to… because resources get used everywhere, yeah, how… is it, like, a listener, and everyone's listening to, like, event changes? Like, how… how to… something we discovered with this stuff and entities is actually very easy to model a session manager and entities, all that stuff.
That part's easy. The tricky part is, how do you take an existing SDK and integrate it with this new concept in a way that isn't, like, rewrite everything from scratch, and, like, make a big mess out of your existing architecture? It turned out that was a little more tricky.
So that's a place where I think checking in with the entity SIG about, like, how is… what does the Python implementation of this look like? Because I assume you guys are talking about Python.
**Pavan** 23:46 Yes, yes, yeah, got it.
Yeah, sounds good.
I'll link, the, issue, you know, that we have been discussing, and also sort of a doc here, so that, you know, in case if there are any other questions or queries, happy to,
answer them, but thank you. It's been really useful.
**Martin Kuba** 24:25 Okay, great. We've got, like, 5 more minutes, so we can quickly talk about, the timeline of the phase, Phase 1.
There was a question about it in Slack, someone was asking.
So…
Yeah, let me just share my screen, I guess.
Yeah, I mean, so these are the things that we had kind of planned in our milestone one.
I was looking back at,
What we decided to work on, it was,
Building out some core instrumentation along with semantic conventions.
There was some data modeling that we, worked on, that we already documented in the project.
I think we're making progress on the instrumentations.
there's maybe a couple more that… that I think we want to finish,
Like, the Web Vitals one, the resource timing.
The navigation timeline, there's a PR for that.
The other thing that we… for Milestone 1 that we…
Talked about is, deciding on browser compatibility, or, like, what we're gonna support.
And we also talked about reviewing the existing, APIs.
From the JavaScript SDK to make sure that they work for us.
I think when someone, at least for… I think where the most important, from my perspective, is…
Like, to finish the core instrumentations that we think are important.
And be able to do a release, so that, like… and have some documentation along with that, so that users can start using them, and start giving us feedback.
So I think we're actually making some good progress here.
I… as far as timeline, I'm kind of thinking maybe we can…
We can get this done, like, in a month or two?
What do others think?
Like, does anyone need help with the things that they're working on?
**Jared Freeze** 26:51 It'd be nice if somebody owned… The credentials and publishings?
So, like, literally, like, the… Nuts and bolts of, like.
Are we gonna copy everything over?
And then versioning, of course. I think versioning is settled. It's not written down, but it sounds like we're all on the same page. It was just 0.1.0, and we just are independent from core repo. But the actual…
Like, getting publishing done, like, should be… At least assigned, you know.
**Martin Kuba** 27:22 Yeah.
**Jared Freeze** 27:27 And it may just be copy and paste the workflows. I mean, that may be it, but, you know, having an owner, I think, would move it along.
**Martin Kuba** 27:35 Okay, yeah, if you don't have an issue for that, I can… I will take a look and create one if you don't have one.
**Ted Young** 27:47 Besides instrumentation, it feels like sessions, since we just talked about it.
**Martin Kuba** 27:53 Yeah.
**Ted Young** 27:54 Like, the other thing.
**Martin Kuba** 27:56 So we do have an implementation of sessions now.
It's not based on the entities. Like, Ted, do you think it's important, like, to…
Like, to look, like, at entities as soon as possible.
**Ted Young** 28:08 I mean, I don't wanna… I don't wanna…
have a thrashy, breaking change, obviously, right? And if…
We start emitting entities as events, and then later move it over to this, like, entity stream thing.
you know.
It would be nice to, like, if we knew we were going that direction, just to skip that step.
But if that stuff is not ready, I don't want us to wait at this point.
**Daniel Dyla (Dynatrace)** 28:37 It's not ready.
**Ted Young** 28:39 So, I think we should just ship with it being events for the time being, and then we'll just have to manage…
Essentially, that being a switch, probably.
Or something. Okay.
It's a bummer, but…
**Martin Kuba** 28:54 Yeah.
**Daniel Dyla (Dynatrace)** 28:56 I mean, the…
The data model stuff is there, like, there's a lot of the underlying work that's done, but there's no…
stable SDK support for it in any language.
**Ted Young** 29:11 Yeah.
And I feel like the entity stream stuff is not something that SIG has, like, thought.
As much about.
Along with it.
They've been thinking.
**Daniel Dyla (Dynatrace)** 29:22 The… the new signal you're talking about, like, the emitting the change events and stuff?
**Ted Young** 29:27 Yeah.
**Daniel Dyla (Dynatrace)** 29:28 Yeah, well, so that's not done either, but I don't think that would be required in order to model sessions as entities and have entities change over time.
**Ted Young** 29:38 Right. That was… I guess what I was saying is, like, I think we can go ahead and just do it all. The only thing that would suck for our users is if…
In the long run, if those state changes are going to be going out through entity state changes.
Getting people used to the idea that they're…
logs is, like, kind of a breaking change. It'd be nice if we didn't move that on people.
But that's the only piece I can see…
where we're being blocked by the entity SIG, because they just haven't thought about it enough yet.
Like, I think we can make a prototype implementation of everything else and be fine. And if it breaks or something, that's not stuff users are really gonna notice.
The thing they would notice is, like, the data.
Disappearing from one location.
Showing up somewhere else.
**Martin Kuba** 30:31 Hmm.
**Ted Young** 30:36 I don't know.
**Martin Kuba** 30:36 Okay.
**Ted Young** 30:38 Whatever.
**Wolfgang Therrien** 30:41 Aside from sessions, are there other… other things that we will eventually want to model as entities, right? So I think we're gonna have that as, like, a similar problem maybe somewhere anyway, right? So it's maybe…
like, not an entirely different flavor of problem, but it's just about reducing the amount of the blast radius? Is that sort of what we're trying to mitigate here?
**Ted Young** 31:06 It's just about trying to find the right place to put this stuff, right? Like, it's easy enough.
to put this stuff anywhere, right? But the most efficient place is to put it as a resource, and if resources are gonna change, in theory, the way that will happen in the future is through entity state changes.
In some sense, I don't think it's, like, a… in terms of functionality, if we're omitting them as events.
you know.
It's kind of equivalent, but it's more just, like, if in general, in the future, all of these resource-y looking things are supposed to go out to this other channel.
It would just be a little bit of a disservice to the people who work on databases at the different vendors to track them, you know, that's all.
I can hear them howling.
From here.
**Wolfgang Therrien** 32:04 safe.
**Ted Young** 32:04 But they can also just deal with it.
**Martin Kuba** 32:10 So there is the part of emitting the logs, the logs or events that represent session starts at session, session end. There's also, like, where we actually put the session ID attribute. Right now, we're putting it on all the signals, not in the resource.
**Ted Young** 32:26 Right. That… that needs to change. I think… We need to get…
to that level with our session management, that at least it's being modeled as a resource using entities. Even if the state changes are getting emitted as events or somewhere else, because that's not done.
I don't think we should be asking people to test it when…
That's working in just, like, a completely different… way.
**Martin Kuba** 32:53 Okay.
**Ted Young** 32:55 Or at least I'm a little worried about that.
**Martin Kuba** 32:57 And that's… that's possible now? Would that be possible now without… without what the entity…
SIG has not finished yet.
**Ted Young** 33:06 I think that's a question for how…
For… for the JS SIG, almost, and our relationship with the JS SIG.
**Daniel Dyla (Dynatrace)** 33:14 It would be possible in the prototype,
But none of that's merged yet. And the prototype is not, like…
It's… it's written as a prototype, I wouldn't just merge it as is.
**Ted Young** 33:30 Okay.
**Daniel Dyla (Dynatrace)** 33:31 I don't think there's any… anything stable… there's no stable entities work in any SDK at all.
**Ted Young** 33:38 There isn't even…
**Daniel Dyla (Dynatrace)** 33:40 experimental SDK specification yet.
**Ted Young** 33:47 Hmm.
**Martin Kuba** 33:52 Well, if we're really hosed, then I would say let's just go with what we have.
**Ted Young** 33:58 And just warn people.
Don't… don't worry about sessions right now, just look at everything else.
**Martin Kuba** 34:06 Yeah, just make it very, very, like, explicit that it's experimental at this point.
**Ted Young** 34:11 Yeah. Like, I would almost even just, like, not have it on or something and tell people that's coming in the future.
I just worry… maybe I worry too much about people.
Getting used to these patterns, but…
**Martin Kuba** 34:26 Okay.
**Daniel Dyla (Dynatrace)** 34:27 Could it be… Like, a span attribute?
**Ted Young** 34:31 That's the way we're currently doing it, and that's…
**Daniel Dyla (Dynatrace)** 34:34 That's a problem.
**Ted Young** 34:35 And, like, it's one thing to thrash people to be like, this data point moved from here to there, it's another thing to be like, you used to grab it off of every attribute and tried to… like, I don't want anyone putting the work into trying to sort out how to do session management out of that mess.
I would feel sad if someone put that effort in.
So, we should just tell people to not…
Not mess with that part, if it's…
If it's not ready to at least be emitted as a resource.
**Martin Kuba** 35:11 Okay.
Okay, well, it's gonna be secondary for us anyway, so,
We're 5 minutes over time, so…
We can, we can take this offline.
Thanks, everyone.
**Ted Young** 35:27 Yep.
**Martin Kuba** 35:27 What's better.
