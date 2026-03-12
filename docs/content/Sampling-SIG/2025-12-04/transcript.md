SIG: Sampling SIG
Date: 2025-12-04
Duration: 36 minutes
============================================================

## Zoom Recording Transcript

**Kent Quirk (he/him)** 02:50 Ayy.
**Alf Kenny** 02:52 Hello.
**Kent Quirk (he/him)** 02:56 I'm… I missed the last meeting, and… I went to… try to look at the agenda doc, and it's private.
I don't know what happened. I had been using it, and…
**Alf Kenny** 03:16 I saw the same thing.
I just… I'm not a part of the SIG, I'm just… I joined because I wanted to talk about a PR, but I also noticed that, I guess, like, last week was American Thanksgiving, and so… Everybody…
**Kent Quirk (he/him)** 03:31 Well, last week, we wouldn't have been meeting, but two weeks before… Ago. The meeting's every other week, and…
**Alf Kenny** 03:39 Oh, okay.
**Kent Quirk (he/him)** 03:40 Two weeks ago, I couldn't make it. So… Hey, Peter.
**Peter Findeisen** 03:48 Hi.
**Kent Quirk (he/him)** 03:51 Do you have access to the agenda doc, or is it…
**Peter Findeisen** 03:54 No, actually.
**Kent Quirk (he/him)** 03:55 For you, too.
**Peter Findeisen** 03:56 I, yeah, it's blocked.
To my surprise. Yeah. Something is wrong.
**Kent Quirk (he/him)** 04:12 Maybe Josh knows about the dog.
**Joshua MacDonald** 04:15 Hello.
**Kent Quirk (he/him)** 04:16 Hey.
Josh, do you have access?
Duck?
**Joshua MacDonald** 04:21 Yeah, I don't have it. I don't know what happened.
**Kent Quirk (he/him)** 04:24 Okay, somebody commented on, Carlos commented in, on November 21st, that somebody made the doc private.
And it's still… Private.
**Joshua MacDonald** 04:37 That's weird, I can't imagine… who owns it? I thought I did, but that's weird.
Yeah, so I've requested access, I don't know who owns it.
**Kent Quirk (he/him)** 04:50 That's true.
**Joshua MacDonald** 04:50 manage.
Well Let's do it without notes today.
Is there an agenda?
It's the usual crowd plus hello, Elf. I remember you've visited us once before. Welcome back.
**Alf Kenny** 05:08 to be back.
**Joshua MacDonald** 05:09 Yeah, I, I was only opening the notes to see if anyone had entered in an agenda. I did not. I, I… sometimes Carlos comes to talk to us about, like, discussions in the SPECSIG. I know there was a… A minor topic about just pushing forward, first, the randomness requirements.
That we've already merged. I don't know that I have much to say about that. I think… if you are familiar with OHL, like, politics right now, there's been a, like, GC… the Governance Committee is pushing to sort of talk about stability and comprehensiveness of the SDKs, and… while that's happening, I think we're just holding onto the fact that the sampling stuff is not implemented as part of the problem, with that we have these inconsistent implementation statuses across the SDKs. So, I know that we're… stalled, and I think that's just the way it's gonna be.
Do we have any topics? I know that last week it was… Declarative configuration is maybe on the horizon.
**Kent Quirk (he/him)** 06:15 Yeah, it seems to be.
**Joshua MacDonald** 06:17 And there was, there was, some talk of that. Does anybody have anything that they would like to say about it?
**Peter Findeisen** 06:26 Well, I, had a look, I reviewed and had some comments, but this is… this is a fairly early stage, and everything there is marked experimental.
It's good that they recognize, the work that we are doing. It's definitely… Not a final version, so it got approved by Jack Burke.
I'm not sure if it got merged.
to anything? I don't think so, but… Probably will get merged soon, and we'll continue working on that.
**Joshua MacDonald** 07:03 Great.
**Peter Findeisen** 07:04 Now, there was one question that you asked two weeks ago.
**Joshua MacDonald** 07:07 Sure.
**Peter Findeisen** 07:09 Which was about compatibility of the… Parent-based sampler with… with a new… version of the trace AD ratio, I don't remember what was the new name.
Well, so it will work only if we get rid of The version of the parent-based sampler… With 5 arguments.
when we… Can specify different samplers depending on whether the parent is sampled or not, and whether it's local or remote.
That will not work with a new schema, so the only way we could use the old one is with… With only specifying the root sampler.
And the rest would follow.
I think this will work correctly. I didn't see any issues with that.
**Joshua MacDonald** 08:14 I know the context of this, I don't remember the question two weeks ago.
this is about the original parent-based sampler API, is 5 arguments.
**Peter Findeisen** 08:30 Right.
**Joshua MacDonald** 08:31 My impression is that it's not widely used. The four other arguments are not widely used.
And… just the way I remember it is that we added this, marking attributes… Sampler to do roughly the same, but without breaking the concept.
**Peter Findeisen** 08:52 Yes.
**Joshua MacDonald** 08:52 So, what was the… What was the reason we were discussing this two weeks ago?
**Peter Findeisen** 08:58 The reason was that we proposed the newest version of the trace ID-based ratio, which is… but we did not really propose anything which would replace the parent-based sampler.
So, I believe the question was whether we have to do this at the same time, or whether we can postpone it till later.
That's my understanding.
context.
**Joshua MacDonald** 09:29 And… let me see if I… Framed it correctly. The… The new composable parent-based sampler stuff we have.
Is correct.
And as long as you are willing to ignore the four other arguments.
The delegated to, local, from, etc.
Then… and you just want to use that one argument, then the replacement of parent-based would be composite of Composable parent-based.
Or just composable parent-based with a single… With a single, composable sampler in it.
So I take it, then, the question was from… Carlos was about… whether we… how we support that old API. Is that right?
Okay.
Honestly, don't really care, but Okay.
I see, I see, I see. Okay, so maybe it would be nice to have, like, a… A warning, or something like that, like… Yeah, I'm not too concerned about this, but now I remember it, at least.
**Yuanyuan Zhao** 10:54 I, I have a question on the status of the implementation of Trace ID, ratio-based, and the OTE, the THP, we implemented in goal, what are the other languages?
that are implementing. I think some time ago, you mentioned, what was that, Microsoft thingy?
**Kent Quirk (he/him)** 11:17 net.
**Joshua MacDonald** 11:20 We don't have .NET. I was trying to find someone, and I've lost track of it.
**Yuanyuan Zhao** 11:24 Okay.
**Joshua MacDonald** 11:25 So, the…
**Yuanyuan Zhao** 11:27 What are the other languages? We have it?
**Joshua MacDonald** 11:29 So the… in the collector repo, there's a library that does TH calculations the way the spec wants, and it's used in a couple of Components in the collector.
I… did not propose to try and reuse that code in the GoSIG, I just sent them a sort of separated, copied version of it that kept the core logic.
But I don't think it's moved anywhere. I just filed an issue saying, I'd like to help, this is my prototype, I didn't go the next step. Which I could, but I have lots of priorities here, so I haven't.
**Yuanyuan Zhao** 12:07 So you're talking about the collector. What about the SDK?
**Joshua MacDonald** 12:12 The Go SDK was prototyped, but it was sort of sent as a draft PR, and it never made it further than that.
Okay. Same with Rust. I prototyped it, and I've… Got it sitting there, and that's in a case where many of my colleagues here at Microsoft are the owners of the repository, and we still aren't doing it, which is… again, prioritization. I don't have any… feeling for when someone's gonna demand us to do this. So I'm, you know, we're in the same boat.
I know Java is well covered, but it's still in the contrib repository.
And I don't know, that's another topic that I think has not had much discussion. Like, when does… When does it come out of Contrib, the prototype that Peter and Atmar wrote?
into the Java SDK.
I think that's a question that Jack is going to be able to help us with.
Have I answered the question? I know that there was… In the SDK land, I've seen Python and JavaScript take steps, but I don't think there's any reusable code Likely to be there.
**Yuanyuan Zhao** 13:23 So… I can't see whether, we can do something, Datadog, because we plan to support The new, like, the OT keys, the TH keys, and to, calculate, spam metrics.
And we need some stability of the, of the spec. I know it's kind of, like, de facto, right, but it's not formally.
established. We need some stability on that, and we can see… we also are interested in seeing Like, the SDKs… These are supported in SDKs, various SDKs.
**Joshua MacDonald** 14:13 Let me ask, then, for your help, I guess. I know many people who work at Datadog. I don't know who has their best control over an SDK, but if there are any languages where you have maintainers or approvers or, like, motivation to do this in an SDK, it would be helpful, to just push it forward a bit. I'm linking you to the package that I went… this is the collector package that is now stable, in my opinion, like, hasn't changed in more than a year, that implements TH and RV and is used in the To the probabilistic sampling processor.
So, but I hear your request. I think we should, We should… be able to… Consider stabilizing the RV and the TH and the trace state stuff.
And… That lines up with what Carlos was asking. Like, the question is, can we stabilize the randomness parts first, and then ask the SDKs to at least get the randomness bits, like, settled? Go to trace context level 2, set the random flag, ideally. That's, like, least controversial, I think.
And I think…
**Yuanyuan Zhao** 15:32 Because that's, that's part of the trace context at, Level 2. Last time I checked, it was still kind of, like, draft, right?
**Joshua MacDonald** 15:44 Well, that's the…
**Yuanyuan Zhao** 15:45 Not formal.
**Joshua MacDonald** 15:46 of chicken and egg problem, where we don't think there's anybody that can finish this except OpenTelemetry.
So that… so that we view stabilizing in OpenTelemetry first.
as the path, and then once OpenTelemetry has stabilized it, we will tell the W3C, we're ready, please stabilize this. That's what I… my understanding.
So, from this, I would take away… that there is now an interest, I'm hearing a second time, I think, in stabilizing the TraceState Handlings document. The trace state… definition, including TH and RV.
**Yuanyuan Zhao** 16:28 Bye.
**Joshua MacDonald** 16:28 As well as on the SDK side, the trace context level 2 stuff.
And that can leave the trace ID ratio for later, or that can leave parent-based, which is what Peter was talking about for later, I guess. At least it's step one.
Which is also the order we did the PRs in the spec. So this… the randomness came first, and then trace ID ratio, and then composable samplers.
Okay, I will… I will, commit to pushing that for you. I go to the spec sig every week. I can put an item on it saying, that there's interest in implementing this, and we think it really should be stabilized first. And I think everyone here can rec… is everyone here recommending that we stabilize what we just talked about?
**Peter Findeisen** 17:20 Yes, I think everyone does.
**Yuanyuan Zhao** 17:22 Yeah, I think this is for everybody's interest, right?
**Joshua MacDonald** 17:26 So… I'm gonna say the first milestone, then, would be… getting the SDKs to follow level 2, and getting us to stabilize the trace state document. And that leaves us lots of room to keep refining exactly the details of trace ID ratio, if we must, and composable, parent-based, if we must.
I think that's… that's the right way.
**Yuanyuan Zhao** 17:49 Yeah. Okay.
Would it help, that if we go to some session of that SIG, Tuesday SIG meeting together.
**Joshua MacDonald** 18:00 Well, I go to it every week, and just for background, but, if you… would be interested in saying the same thing in front of the group, it would help, absolutely, to have someone from Datadog saying, we want to implement this in our backend, and we just want to kind of, like, make sure it's not going to change again, and the entire SIG here agrees, and And I'm… I think it's… I think it's prudent to not stabilize the SDK parts. Like, the trace ID ratio is… it's… I think it will stabilize, but I think we should leave it open a little while longer, and then, you know, after that, the composable and the configure… the declarative config and stuff can all come later on.
**Yuanyuan Zhao** 18:42 First, the keys, right? The, the, trace states.
**Joshua MacDonald** 18:48 Yeah, alright, well, I can.
**Yuanyuan Zhao** 18:51 And also, the other, part of the trace state, the, trace parent, that flag.
**Joshua MacDonald** 18:59 That's part of Level 2, yeah, the random.
**Yuanyuan Zhao** 19:01 Right, right. The two things introduced in Level 2, we need to have it slagonized, and… So that should give at least, the post-SDK, spend metrics calculation something to build on.
And, trace ID ratio base, the actual implementation in different languages also needs that as the foundation. And who… can contribute to build the various… for various SDKs is something that we can talk about afterwards. Okay. And that's probably multiple People can't help over here.
**Joshua MacDonald** 19:43 I also… I ought to be able to provide a .NET, like, that's hard on Microsoft, for sure. Okay, well, here's what I propose. Tuesday the 9th, next week, there's an 8 o'clock Pacific meeting, 11 for you, I guess. If you would like to… to… join us, I will… I will help facilitate or… or collaborate and communicate with you. I, you know, you can say what you want to say, I can clarify or help discuss it with the group, if you'd like. And then hopefully we come back two weeks from now. Two weeks from now is gonna be, like.
**Yuanyuan Zhao** 20:18 Next week, I think I'll just dive in to get some background without saying anything first, and then after that, we can talk about how we want to move forward.
**Joshua MacDonald** 20:30 Okay, if the meeting looks light next week, maybe I'll just say something, but if you'd like to dial and listen, that'd be great.
I suppose… Two weeks from today will be the 18th. It's… I'm gonna be here, so maybe I'll see you, maybe you won't be here, if it's holidays early for you all. But that sounds like a plan.
Either next Tuesday or the Tuesday after, some… we'll get some feedback on that from the spec sig.
Any other agenda items?
This stuff moves slowly. I think that's… it's good. We're making progress.
**Kent Quirk (he/him)** 21:13 We think Alf wanted to talk about something, right, Alf?
**Joshua MacDonald** 21:16 Let's, let's talk.
**Alf Kenny** 21:17 The last time I was here, I brought up a change for adding, essentially, a knot around some other policy, and I have a PR that's sitting inside of the Contrib repo right now. It's just waiting for a review.
**Joshua MacDonald** 21:36 Okay.
Thank you. I… Thank you for showing up to say that. I could, in the future, feel free to Slack me, if you're like, Josh, just, just go look at this now. But yes, let me find it.
Because I want to help that effort. And… So… but… but I'm sure I can find it.
Oh boy, there's 140 open PRs.
**Kent Quirk (he/him)** 22:04 Give a.
**Joshua MacDonald** 22:06 Yeah, I mean, I mean…
**Alf Kenny** 22:07 a number.
**Joshua MacDonald** 22:08 I'm not gonna see it.
**Alf Kenny** 22:11 It's, the pull request number is 44378.
**Joshua MacDonald** 22:16 Not even on page 2.
**Alf Kenny** 22:18 It's been sitting there for a little bit.
**Joshua MacDonald** 22:21 That's okay, I found it. Yeah, okay. Great.
I will, I will look at this this morning. I think, if there's anything that stands out or you'd like to talk about here now, that's welcome.
**Kent Quirk (he/him)** 22:36 Can you just paste the link, Jack, real quick?
**Joshua MacDonald** 22:38 Oh yeah, let me find it.
Yeah.
we've already talked about the reservations that many of us have about tail sampling processor in this room, so, but I also view it as a clear sign that the community wants something. Anytime someone's willing to help contribute, like, to make it better, absolutely support.
One day, maybe we'll talk about, You know.
bigger improvements, but I don't wanna… I don't wanna hold it back.
As you may remember, some of us here are interested in, like.
the statistics of… of it all, but, but this is great, and I think… I think, I think… it's important that we keep people who know this code, so, Elf, you're becoming an owner of this code.
**Alf Kenny** 23:29 Just so you know.
**Joshua MacDonald** 23:30 Alright.
And the… the only thing that I… this reminds me is that there's a feature flag in there that, like… did you… is it still there? Did you see it?
**Alf Kenny** 23:43 For… for which feature? Is this the.
**Joshua MacDonald** 23:44 There's a feature flag about inverted matches.
**Alf Kenny** 23:47 Yep.
**Joshua MacDonald** 23:48 it's weird. My recommendation has always been to finish it, meaning get rid of the feature flag, whichever way it is, one way or the other, because the tests are currently covering both sides, and it's weird. So, but I'll look at it, and I will approve it, for sure. I'll also see if I can find out how to get rid of that feature flag, as I do.
**Kent Quirk (he/him)** 24:11 Yeah, be really careful about that, because, I mean, knots and sampling get ugly.
**Joshua MacDonald** 24:18 Well, okay.
**Kent Quirk (he/him)** 24:18 Very worried about it.
**Joshua MacDonald** 24:20 Okay, I want your help then, Kent, too, because my impression is that it was already ugly. The feature flag was.
**Kent Quirk (he/him)** 24:24 Well, yeah.
**Joshua MacDonald** 24:24 it, and then alpha's adding back not in a different way.
**Kent Quirk (he/him)** 24:29 Okay.
**Joshua MacDonald** 24:30 Alright, so we're gonna make sure Kent reviews this as well.
**Kent Quirk (he/him)** 24:34 Alright.
I'll put it on my list.
**Joshua MacDonald** 24:37 Alright, sweet.
Yeah, so unless we want to talk about how it works, or belabor this point about inverted matches and knots.
Well, do we… do we want to do that?
**Alf Kenny** 24:50 I mean, I can give a brief overview. I think.
**Joshua MacDonald** 24:52 Yeah, why don't we?
**Alf Kenny** 24:53 Inversion, you're… Do you want me to share my screen, or…
**Joshua MacDonald** 24:59 I was gonna try to, but… Yeah, I can… I'll get it. Here it comes.
**Alf Kenny** 25:06 So I… I also… I mean, I pointed this out primarily in the… in the issue, as a… that I originally brought up, but… I… we need to be able to… My specific use case was that I want to be able to determine if a process is generating spans that have no root span, implying that they are a continuation of a distributed trace.
So, some other application is sent to context to this application, that application is using that context to continue a trace that started somewhere else. And… We're doing some fancy sampling, where we'd like to, do sort of two layers. One layer of filtering out useless traces next to an application, and a second layer of filtering out distributed traces that we have collected in, one, you know, a namespace containing a bunch of, like, a tempo backend.
So to do that, we want to prevent this, a section of a distributed trace from being removed.
From being sampled out.
Because it could be that the remainder of that distributed trace is actually important. There's an error that happens somewhere else in an application upstream or downstream, and so this is a very useful section of that trace, even though nothing important happens in it. So, one of the things we need to determine is, has this application just produced a part of a distributed trace? And the easiest check for us to do there is to say, are none of these spans Do none of these spans have a root span?
Are none of these spans stating that their parent span is 00000?
So we essentially need to run the same check across all of the spans, and once we've determined that All of these spans have a parent span, then we can say, okay.
do… we want to sample this, or we don't want to sample this? And so, the inverted doesn't really allow us to do that, because inverted is looking at… I think it's, individual spans, and saying the moment I hit some… some criteria, then I'll either say, yep, good to go, or nope, inverted, not.
we need to look at the entirety of the spans being generated by this application. So a NOT would allow us to say, take this policy, apply it across all of these spans, and then take the knot of the result of that.
**Joshua MacDonald** 27:34 Now, somehow this is, like, conceptually complicated.
**Alf Kenny** 27:38 Yeah. Yeah. I think if you look at the very top of the, of the issue here.
You can see that, basically, sampled, if not any of the spans in this trace are a root span.
So currently we can say, you can use OTTL, Rules to say, to locate whether or not the parent ID is zero, is all zeros or not?
But the problem is we match on the first one, we see that it hits that criteria. So if we say that, like, my criteria is I don't want all the… I don't want the parent ID to be all zeros, the moment we see one span that matches that, then we stop looking at the rest of the spans.
which, in our case, if the criteria is all… the parent ID is not all zeros, so let's say, yeah, in this distributed trace, you have a… I guess I'll draw on the screen, that's a visual thing here. So if you've got, A application that generates a bunch of… of spans.
And if we look at… if I just show the parent ID of each of these, let's say it's 111222333.
And 333 is pointing to this, 222 is pointing to this, and 111 is pointing somewhere else that was generated by… somewhere else in the system.
as this is a continuation of a distributed trace. So if I wanted to say, only sample this set of spans here.
If… If and only if, all of these spans have a parent ID.
the non-zero parent ID. Then if my criteria is look for a non-zero parent ID, the way it currently works is the policy would go, oh, I see a non-zero parent ID, therefore I'm going to sample this trace.
There's no way to say, look here for non-zero, then look here for non-zero, then look here for non-zero, and when we're satisfied that all of these spans have a non-zero parent ID, then we sample the trace.
And by inverting, sort of, I hesitate to use the term invert, but by, Looking for the opposite criteria by saying instead.
match on a 000 parent ID.
**Kent Quirk (he/him)** 30:04 You're buying to Morgan's Law here, you're saying, you know, you're getting not, you're implementing AND with OR and NOT.
**Alf Kenny** 30:12 Exactly, yeah. Look at the Boolean logic of it all, yeah.
Look for 00, we don't match here, look for 00, we don't match here, look for 00, we don't match here, therefore I'm not going to sample. Pass it through a knot.
Therefore, we do sample.
**Kent Quirk (he/him)** 30:27 So, I'm just… I just want, as a piece of data, this isn't a commentary on whether this is the right answer or not, but Honeycombs Refinery handles this problem with the individual decision being allowed to be set to, a scope of trace level or span level. And if you say, I want trace level evaluation, the condition must be true.
On at least one span, and if you, say.
It's actually… no, it's not quite the same, now that I think about it. Most of its decisions are made at the trace level. And then… and we do have a… you can ask, does it… does a root span exist? It's just an option, like… On the… on the condition. You can add to the condition. If root span exists, then do the following condition. So that you can make decisions like this based on that. And then we also have this concept of a scope being, do all of the fields of the condition have to happen… have to be true in the same span, or they can be true for any span in the trace?
So you can do, you know, I see errors, and I see this Service name, and then therefore sample the trace, even if those two things happened on different spans.
Anyway, it's just… I just wanted to provide… there is a different context for a different model for how this is done. What you're talking about.
makes sense to me. I… I… I was just providing additional data there.
**Alf Kenny** 32:04 This is… I think… I would be totally down for that if I could… if I could actually apply a condition across a whole trace, as opposed to just individual spans. I couldn't see… I'm not familiar with Honeycomb. Is that something that's… it's a different product, or if it's, like, is it something…
**Kent Quirk (he/him)** 32:21 Honeycomb is a service provider that has, .io.
Yeah, Honeycomb Refinery is a trace-aware sampling proxy that we… that we make, that, has been the thing I've been basically responsible for largely for the last few years, although I'm moving on to other things now, but… but this thing is basically, it does tail sampling.
with a very sophisticated kind of rule model. And, so we're… we're a service provider that does, you know, takes open telemetry data. One of the things that's interesting about Honeycomb that's kind of unfortunate in this context is… Refinery receives hotel, but it doesn't send it, just for historical reasons, it pre-existed anything having to do with Hotel, and it sends all its data using Honeycomb's original formats, and we haven't made it so that it sends Hotel data yet, because the main reason is because it turns it into something that's not OTEL internally, reconstructing hotel on the output, it wouldn't be the same as the one you sent in, so we, you know, we've been doing work to get us to the point where we can process the data without destroying it.
**Joshua MacDonald** 33:32 Got it.
**Kent Quirk (he/him)** 33:33 So that's why…
**Joshua MacDonald** 33:34 enemy.
**Kent Quirk (he/him)** 33:34 That's why we don't just tell people, hey, go throw this in your hotel systems.
But, yeah.
**Joshua MacDonald** 33:42 But yeah, there's a…
**Kent Quirk (he/him)** 33:43 Rule-based language for it.
**Joshua MacDonald** 33:45 We also wouldn't expect you to just open source this stuff, even if it, you know…
**Kent Quirk (he/him)** 33:49 Refinery!
**Joshua MacDonald** 33:50 It is open source, but this… this…
**Kent Quirk (he/him)** 33:53 The problem is that it receives the data and immediately turns it into basically just a bucket of fields, so it destroys the hotel context, and so then we can't reconstruct that hotel context easily on the output side, so we just continue to just send it as honeycomb data.
**Joshua MacDonald** 34:11 That sounds, like, totally familiar to me as a vendor, a former vendor of Trace System, anyway. Yes.
Okay, well, I, I, the way I took that comment was, there's other ways to think about this, which would probably be more powerful, But…
**Kent Quirk (he/him)** 34:29 But we have the code we have.
**Joshua MacDonald** 34:31 We have the code we have, and we… none of us love it, but but I… and I think what Alfa's describing has made sense enough. I want to look over it again, And I'll… and I think… any of these reservations that we have are not going to be strong enough to say, let's not do this. Like, this code is… is… you know, incrementally improving. If it helps ALF and it's well-designed, on, you know, incrementally well designed, I think we should do it.
So, I will take care to approve this today, and make sure I understand it.
Elf, if you feel like there's an aha moment where you're like, I could totally change this with a simple thing, and, like, get trace-level scoping, or whatever, you know, Kent just described.
Think about it, but I wouldn't require it.
**Alf Kenny** 35:20 Sure.
**Joshua MacDonald** 35:22 Alright. Yeah, I mean, we're… my team's using…
**Alf Kenny** 35:25 Using sampling quite a bit, so it could be that we'll… we all have that aha moment eventually.
**Joshua MacDonald** 35:29 Yeah, well, anyway, I'll make sure we get this approved, and I can push the people that press buttons to merge it as well, once the time comes.
**Alf Kenny** 35:38 Cool, I appreciate that.
**Joshua MacDonald** 35:39 I mean, this one, yeah.
Okay, well… Now I think we may have passed through our agenda.
Any last comments? Otherwise, December 18th. If we're here, we're here, and I'll see you then.
And Yuan Yuan, next Tuesday, or the Tuesday after that, I will… I'll ping you.
**Yuanyuan Zhao** 36:03 Yeah, next Tuesday, I'm going to dial in, to the Something Sick. Oh, sorry.
**Joshua MacDonald** 36:09 the spectrum.
**Yuanyuan Zhao** 36:10 specs, like, yeah.
**Joshua MacDonald** 36:11 Great.
Alrighty, cool. Oh, I have to find my controls. Thank you all. I'll see you next time.
**Peter Findeisen** 36:18 Thank you.
**Yuanyuan Zhao** 36:18 Have a great holiday, if we don't see you, see each other.
**Peter Findeisen** 36:22 Yes.
