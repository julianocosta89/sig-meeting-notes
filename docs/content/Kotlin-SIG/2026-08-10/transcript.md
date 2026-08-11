SIG: Kotlin SIG
Date: 2026-08-10
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Jamie Lynch** 02:44 Nope.
**Jason Plumb** 02:48 Hey.
9 AM on a Monday, already my second meeting.
**Jamie Lynch** 02:57 Sometimes.
Cool. I will just give it a couple of minutes for more votes to show up,
**Jason Plumb** 03:15 Hopefully, Carlos.
Yeah, have we heard anything from Carlos since last week?
**Jamie Lynch** 04:08 I haven't seen any movement on the issues, or… heard anything via Slack, but he may have just been, like, saving up feedback for this meeting.
**Jason Plumb** 04:21 Yeah.
Let's hope so. I haven't seen anything, but it'd be good, I mean, I want to move forward with those. I think they're looking good.
**Hanson Ho** 04:30 Hello.
You hear me?
**Jamie Lynch** 04:49 Cool, so I'll just give it another minute for folks to add any items to the agenda. Otherwise, I think we're probably gonna be looking at, like, API stabilization discussions.
**Jason Plumb** 05:04 Yep, yep.
**Hanson Ho** 05:15 Not sure if I can hear from you two.
**Jason Plumb** 05:18 Hello, MicCheck1212.
**Hanson Ho** 05:20 Oh, I definitely can't hear from you too, that's why.
**Jason Plumb** 05:22 Alright.
**Hanson Ho** 05:23 I'm sure it's my thing. Don't worry about it, keep going.
Oh, there you go.
**Francisco Prieto** 05:47 Hey, everyone.
**Jamie Lynch** 05:47 That's it.
**Hanson Ho** 05:49 Yeah, I can hear now.
said my thing had low volume, so I thought that wasn't working, and I heard nothing. It's the other one that's not working.
**Jamie Lynch** 06:04 Cool. So, I guess I can just make a start on the agenda items we have, but if you folks do have other things they want to discuss, please feel free to add them to this.
Yeah, so… last week, we were discussing the APIs and how we get them stabilized, basically.
So, as… two PRs… Which, I think everyone agreed on.
a couple of weeks ago to make the baggage API and the context API, stable, just by removing some… Like, just by removing the experimental API annotations.
So… I think we're just waiting to hear back.
Carlos about that.
And I guess… If he shows up, we'll ask him. If not, I'll ping him.
And yeah, basically, all of these other points are also awaiting input from Carlos.
So, I think there's some discussion around whether And no op.
Weather know-op.
counted as, like, parts of the API, or was an implementation in of itself, and how we should bundle that, basically.
But if… Well, I guess, do you folks have any questions about that, or would you like to just continue on discussing where we left off with Tracing API?
**Jason Plumb** 07:54 I think that's cool. I would… I would continue where we left off.
I do… I'm getting… I'm getting antsy about those two. I want to move them forward, and I think you probably do too, Jamie.
**Jamie Lynch** 08:06 Yeah, for sure.
And that's something we could propose, I guess. Like, because it's just removing an annotation, really, it's not… actually stabilizing the API. Right.
**Jason Plumb** 08:21 Right.
Yeah, I think, let's give Carlos a last chance to chime in on those. I think we're probably good to move forward, though. And I don't know… the extent to which Carlos needs to be, like, the final say on every… every corner of the API. I mean, he's definitely our domain expert.
And we love to rely on his expertise there, but I don't know that it's the final say.
We are… We have… we have some agency to make mistakes, right? So, it's not the end of the world.
If we do that. Cool. Yeah.
**Hanson Ho** 08:55 So…
**Jamie Lynch** 08:56 Done.
**Hanson Ho** 08:57 Oh, if we get a blanket, like, okay from Carlos, like, the ones that he's reviewed and all we're doing is doing formalities, maybe if we get, like, one, hey, you can do that, then we'll just go ahead and do that.
Hey, that's a good way.
**Jamie Lynch** 09:15 Okay.
So, I'll ping Olos, and then… I think… if we don't have any feedback by, like, next week, I think let's just merge them.
**Jason Plumb** 09:28 I'm into it. I like it.
**Jamie Lynch** 09:35 Okay, cool. Right.
**Jason Plumb** 09:39 Yeah, regarding stabilization, one thing that occurred to me last week that I'm now remembering is when we… like, when we check all those boxes in the API and we decide that we're stable.
Do we expect to rev the version up to 1.0?
Or should we?
Let me put this in the dock. I…
**Jamie Lynch** 10:00 Yeah, that's a good discussion point.
**Jason Plumb** 10:02 Yeah.
**Hanson Ho** 10:05 I think it should only be 1-0 if everything that we ship, that we want to have stabilized in that first phase gets there.
like, do we… I thought… do we have a milestone of… I thought we had a milestone of, like, what 1.0 constitutes, and include, like, set-rated APIs. Are we gonna be through all these after… after… after the tracer stuff is done?
**Jamie Lynch** 10:33 I mean… I think we have the majority of stuff in the API, apart from metrics, to be honest.
**Hanson Ho** 10:47 Yeah. Then if what we're targeting as a first release, is effectively all… don't have that experimental thing, then I think removing it, clearing 1.0, the API at least, seems reasonable. I mean, if we're not waiting for anything.
**Jamie Lynch** 11:05 Yeah, I assume there's probably some sort of, review from local technical committee when we do get to the point where we're thinking about doing 1.0. Do you remember what happened?
with Open Celebrity Android, JSON.
**Jason Plumb** 11:21 I do, and it was chaotic, It was around the time that there were some changes being made to the stable by default.
policies, and we were effectively grandfathered in. I mean, there's a big push to, like, give SIGs more autonomy, and to let them have the ability to do these things, but at the same time, they want to balance the message of stability across the ecosystem of OpenTelemetry, so… We did not have to go through any sort of, like, formal review. We did a blog post that announced it, and we put out a community poll. There was an issue, like, people could chime in if they had pet stuff, and it largely didn't amount to a whole lot, and so we just went for it, and we just plotted forward.
I guess what I was asking is because… there… when you have kind of a… I don't want to call it a monorepo, but when you have a repo that contains all of these different components.
and they're versioned together, the API and the SDK being versioned together, no matter what. There's… there's inherently, like, a disconnect between the semantics of… semantic versioning, simmer, and what the underlying components have.
Which is why we can account for some of that with a suffix, you know, like keeping alpha, or… something on the suffix of the SDK for a while. I just wanted to make sure that we're aligned on that, because I… I think it's potentially confusing.
To have some components Get promoted to 1-0, but still not be stable, or be alpha.
And it's also one of the… I don't know, I think… I think people put… we, the industry, have been putting too much on Semver for way too long, and it makes me crazy, but…
**Hanson Ho** 13:14 I think for Android, it was a little bit more straightforward, because we are grandfathered in, and what were declared stable was effectively the SDK implementation, so drop this in, it's quote-unquote stable. The APIs are very… many APIs weren't stable, and I think that was… that's kind of our, you know, get out of your free card, you know, there's only a couple APIs that were stable, and then everything else was what it is. I think for us, we're almost going the other way, which is the implementation is what it is, but what we're trying to declare stability is the API, and us… and… and this has a way bigger API surface than open to your Android.
So, being a bit more careful in this instance, and getting more checkbox signed in, or checked off before declare 1.0 is probably the more the right thing to do. And we don't have the whole being grandfathered in, thing, but… I mean, I think if all the APIs we want to target for the first release have been declared stable, we don't have the annotation anymore, then what else are we waiting for to call it 1-0? And we don't even have, like, "-dev or, in the artifacts or anything like that, right? If I remember correctly. So… this is basically a Semver, hoop jumping exercise. I think it's… it's reasonable to do it once… once we're saying, hey, stable equals 10 equals this is the first set of APIs that we're… we're gonna say we're not gonna go back on.
Which is what stability really means, at the API level, anyway.
**Jamie Lynch** 14:57 Yeah, makes sense.
**Jason Plumb** 15:02 Carlos, we invoked your name a bunch before you were here.
**Carlos Alberto Cortez** 15:06 Yeah, I can see that, yes. I still need to review the baggage PR and the context, mostly the context. Yeah, I added some notes, by the way, on the, review the propagator's API issue, You know, I was trying to go and review stuff, so the first thing that I… well, this is related, is that, So, you may remember a pair of different things. One of them was having context.
with a default implementation or not, and long story short, I think that the specification, the rationale is that Languages have… An implementation that you can use instead of trying to allow users to override that.
JavaScript is an exception, because, you know, you need to have different implementations, depending on whether it's Node or the browser.
So in that case, I think we are safe on our side, because there's prior art.
On a related note, on the propagator's API, One of the things is that context should be… become stable, in theory, before you make the propagator's API stable, because you are using that.
And then, besides that, there are two things that I wanted to mention. The first one is that it is mentioned that implementations, that's the second pointer, must offer a facility to group multiple propagators from different cross-coding concerns, which is something that, of course, everybody uses that. However.
the WorkHit implementations may sound like it's in the SDK, but because the expected usage is that you have this in the API, I think that this should exist in the API. And I didn't see that.
in our side, but I think we should offer this. I think this is in the implementation side, but we should offer that out of the box.
That's my impression, and the first one goes back to the previous thing, like, the OpenTelemetry API must use knob propagators.
And this is in case you have a global object, you know?
If we do not expose a global object, it's… That changes things. On that regard, let me add a note there, but Java, at least, and I don't remember about other languages, but they offer, like, a no-op static method at the API side, so even if, like, even if you don't have any actual propagator implementation.
just go off for a no-op, you know, that… the propagator CPA is using on their designs, but also users can use, you know?
**Jason Plumb** 17:46 Yeah, so to that point, Carlos, currently, we do have a no-op text map propagator.
There's an implementation of that, and it's marked internal.
I think we surface it as a default. Is that… I'm guessing that's true.
**Carlos Alberto Cortez** 18:01 Yeah, if that's the case, that's enough, yes.
**Jason Plumb** 18:03 Okay. Yeah, I think… What I didn't say yet is that it's in a separate module from the API. It's a separate artifact.
**Carlos Alberto Cortez** 18:11 Yeah, that goes back to the question we were discussing about separation between NOP and API, yeah.
Okay, so we can take it on that front, but I guess that one of the things that I would like to see is the second point, like the implementation of software facility to group that. That's also in the implementation package. I remember seeing that, but not here.
In the composite.
**Jason Plumb** 18:42 For propagators?
**Carlos Alberto Cortez** 18:44 Nope.
**Jamie Lynch** 18:48 There's this, a requirement?
on the… API surface, like, for folks who are instrumenting, or is it on the actual SDK, so for folks who are, like, configuring the SDK?
**Carlos Alberto Cortez** 19:04 It's… it should be mostly for the SDK, for people configuring that, yeah. There's some, node there that instrumentations Can configure this, but it's… Advice against, you know?
That's for, like, corner case things like ASP.net, you know, doing something funky there, and they need to propagate their own format on top of what you are trying to do, etc.
**Jamie Lynch** 19:33 And, for this first point, about using no-op propagators unless configured otherwise, could I understand… Why that's a requirement.
I'm just trying to understand, like, the use case.
**Carlos Alberto Cortez** 19:48 Yeah, so that's basically, like, that's very related to the… something that we have to… I didn't seem to think about that, but I promised to do that this week, about the no-op versus the, the API separation, and that's in case an application is trying to, you know.
To instrument what, you know, what it's doing, and… you still need the calls to do something there, so in case you say, you know what, I'm gonna disable that for now.
So if you have calls in your code calling the propagators to actually propagate, it's doing nothing, you know?
**Jamie Lynch** 20:28 Doesn't matter what you want to view.
disabled OpenTelemetry.
**Carlos Alberto Cortez** 20:34 You may actually… may want, that's the funky thing, you may want to have the SDK disabled and still do propagation, in case you want to allow pass-through.
**Jamie Lynch** 20:47 Okay.
Sorry, that would be to, like, some other… So, telemetry.
**Carlos Alberto Cortez** 20:53 Yeah.
**Hanson Ho** 20:57 So it's almost like there's… there's a layer of disablement that is… the SDK and the APIs are disabled, but there's still code that… passes… it's almost like a standalone thing. It's like, hey, if you disable this, you enable this implementation, and then it kind of just passes around, so it's almost an SDK into itself, then. Or, like, a late SDK or something like that, or a facility of the SDK being disabled.
**Carlos Alberto Cortez** 21:27 Yep.
**Jason Plumb** 21:30 Yeah, I never understood this use case. It seems so weird to me.
**Carlos Alberto Cortez** 21:35 There's… it's historical from Jaegering, if I remember correctly. The idea is that in case, the owner of a service doesn't want the service to be instrumented yet, because of fears of being overloaded and stuff, but just… people still need to see the trays, like, something happened, I don't know, we don't know what happened, but we can check the full trays, you know?
**Jason Plumb** 21:58 Right, but then you have to ask, like, what's doing the propagation?
**Carlos Alberto Cortez** 22:01 I know.
Yeah.
**Hanson Ho** 22:03 If I were to disable an SDK, and it was still doing stuff.
In the background, I would be… it would be weird for me. So, honestly, even if there's… there's, existing implementations that do this, I would almost want to, like, go back to… to them and say, hey, do we actually want… I mean, for historical reasons, I know certain implementations and APIs, I guess it's SDK, do this, but do we want to No pun intended, propagate this forward, because it feels like an anti-pattern to me.
**Carlos Alberto Cortez** 22:39 Yeah, actually, and to your point, even on top of that.
There's something, I don't remember the exact name, that it, it has a specification, but basically it's, like, called default span or something like that.
In cases, it's been doing nothing, but it's actually helping propagate The context internally, but it's, like, actually not… not a real span, and it's part of that.
**Hanson Ho** 23:05 It just smells really funky to me. That's… that's… from someone who doesn't have historical context, it… yeah.
**Carlos Alberto Cortez** 23:11 Yeah, and I don't even remember it fully. I remember that it came from previous stuff, probably Peninsula took the same thing, and actually, that's a good call, like, for… we should reference in the specification the rationale… rationale, specifically… for cases where it came from, like, an external source, you know? So people can understand. And maybe, when you have that, and it's super clear, you can say, hey, we want to deprecate this, or we don't want to support this, or it's at least not, Not recommended, etc.
**Hanson Ho** 23:43 So, are we at a point where we can say… go back and say, hey, can we not do this? We don't.
**Carlos Alberto Cortez** 23:48 The specification for now, like, whether there's… yeah… You know, the person who may remember better about the context is that Young, probably.
Probably.
**Jason Plumb** 24:05 Who is it?
**Carlos Alberto Cortez** 24:06 They're young.
**Jason Plumb** 24:08 Okay.
**Carlos Alberto Cortez** 24:08 Yeah.
Maybe he remembers more of the context.
If not, we can just dig something.
**Jason Plumb** 24:19 We see Ted sometimes in the client SIG, but we can reach out to him.
**Carlos Alberto Cortez** 24:24 Yeah.
But anyway, I guess that, anyway, the thing about here is that, even before this, yeah, I need to keep reviewing the, the no-op versus, the API. And as I said before, the initial feedback from the community is that, we keep them together.
Because that's what other languages do. But at the same time, there's the thing about the global object, which is part of the same situation, you know?
And it's kind of funny, because, Yeah, like, you may remember that Jack advised against that.
Although, one interesting thing in that front.
is that when you are using, for example, the Java agent.
you, as a user of the Java agent, you're only declaring a dependency to the API, and then you just go and grab that OpenTelementry object and say, give me a tracer provider, etc.
So, in theory, you need, as a user, still a way, a global object, to retrieve something, but not… maybe you shouldn't allow that to be set by the user, because that's where the product is created.
So, in that regard, let me go ask Jack about that. I think that's a good thing that I was thinking aloud here.
Just to clarify that part, because my problem, my impression is that the problem was allowing users to register that, and it's secretive.
side effects.
**Jamie Lynch** 25:58 Okay. But, sounds like a good action.
**Carlos Alberto Cortez** 26:02 Yeah, I will do this, and of course, reviewing the context PR. I will review that first, before baggage, I think that's way more important.
**Jason Plumb** 26:12 But there's nothing top of mind for you, Carlos, that's holding those up, you just want to be thorough and double-check?
**Carlos Alberto Cortez** 26:17 Yep.
**Jason Plumb** 26:18 Can you do that this week, you think?
**Carlos Alberto Cortez** 26:20 Yes, let's do a deadline. I will tell my manager to hold on private stuff.
**Jason Plumb** 26:26 Okay.
**Carlos Alberto Cortez** 26:26 twice.
It's gonna be, like, a cascading over the weeks, you know?
**Jason Plumb** 26:30 Okay, I appreciate that. Yeah, I was… I was hovering over that merge button more than once last week, and I was like, we should just wait.
**Carlos Alberto Cortez** 26:38 If you… I mean, worst case, if you had done that, I would probably have raised, like… I could have done double-check and raised any minor issues still. I don't… I don't think it's the end of the world for now.
**Jason Plumb** 26:48 Okay.
**Carlos Alberto Cortez** 26:48 Future, who knows what.
**Jason Plumb** 26:51 Yeah, okay.
**Hanson Ho** 26:53 As long as we don't cut a release, it's still fixable, right?
**Carlos Alberto Cortez** 26:58 Right?
**Jamie Lynch** 27:00 Cool. Anything further to discuss on that one?
**Carlos Alberto Cortez** 27:06 That's all from my side for now.
**Jamie Lynch** 27:10 Awesome.
So, Jason, I've seen you've added this one about instrumentation. Should we talk about that first, and then Tracing API?
**Jason Plumb** 27:21 Sure, we can keep it short. I just, I noticed that there are some issues, and sometimes PRs will pop up.
Related to instrumentation, it seems like we might be putting the cart before the horse a little bit when it comes to that, and I understand, like.
those are… like, the ones I've seen are core use cases, and so I kind of get that, but would it help us to not be distracted by instrumentation for a little while, and not… I mean, for me, I'm, like, inclined not to even try and think about it while we're working on gelling the API and the SDK.
**Jamie Lynch** 27:55 Do you have examples of which ones you've seen? I mean, I know I opened one today for contact for everyone else on Kate or…
**Jason Plumb** 28:07 Yeah, I thought there were some others. I mean, KTOR's at the top of the list right now, Let's see…
**Hanson Ho** 28:16 I do agree to not be distracted by that stuff, but at the same time, I feel like if there's, if there's desire to start it, at least to a point where, you know, people are sending PRs, we're talking about which ones we want, I think that's healthy.
APIs are only so good if there's an SDK behind it, and the SDK is only so good if you have some, you know, auto-instrumentation. So I feel like getting a handful of those in, or at least getting started, would be a good idea. But I… it is good to be able to create, like, a separate milestone or something like that, and put it all there, because KTOR is… is… We're gonna need it.
**Jamie Lynch** 28:53 Yeah, I think, from my perspective, the reason I worked on that, is… yeah, basically I had a bit of spare time over the last couple of days, and… I felt like it would be helpful to have at least one instrumentation that kind of demonstrates how to use the instrumentation API. Cool.
But yeah, it's definitely low, it's even other stuff.
**Jason Plumb** 29:20 Cool, yeah, I didn't want it to be a call-out, I'm just like, whoa, instrumentation already? But it does make sense, then, I guess, to have… one user of the API and SDK that can be stitched kind of all together as an integration point, so… cool. That works for me.
**Jamie Lynch** 29:35 Yeah, but yeah, I definitely agree it's not as big a focus, and yeah, I think we should probably deprioritize Well, any of us that come in until we've got, like, the tracing and logging. Cool.
**Jason Plumb** 29:48 I was also looking specifically for, like, any hints that, like, people are asking for this, or like, yeah, I built KTOR because we have a user who's, like, already wanting to… I'm like, oh, that, like, that would be exciting, and I didn't know if that were the case, so I just wanted to clarify.
**Jamie Lynch** 30:02 Yeah.
I think from memory, there was one… I think one person might… might have asked about it, I'd have to go through and get up with you.
**Jason Plumb** 30:12 Okay.
**Hanson Ho** 30:15 Once we get to a point where it's, like, ready for review, we can talk about, like, versioning and artifact naming and all that stuff, because, it… I mean, similar to Java, it probably should be a separate artifact, and maybe versioned differently, and I don't know if we need a separate repo for that, or, you know, what have you, but having… having, like, a test case to pull through.
It's like, hey, we're gonna build this pitch on top of this 1.0 stable API. How do we do that? Would be a good, follow-up once we do actually have that.
**Jason Plumb** 30:50 Okay, I'm cool with that.
**Jamie Lynch** 30:54 Awesome. Cool. I guess we can spend a bit of time looking up a tracing API.
**Jason Plumb** 31:01 Yeah, where did we leave off with that?
**Jamie Lynch** 31:03 So I think I was organized naturally, wrote a comment. So, yeah, Tracer and Tracer Provider… We accepted were okay and didn't require more discussion.
**Jason Plumb** 31:16 Okay.
**Jamie Lynch** 31:16 And everything else is basically fair game for discussion.
And yeah, I think we had some discussion about span context and where we wanted to create the object.
So I can just bring up B… API, and have a look at the… Tracing folder.
Okay, so tracer and tracer provider, we said, were okay.
And I think span context was kind of the next one, really.
**Jason Plumb** 31:55 Okay.
**Jamie Lynch** 31:57 Unless folks have another… one I want to look up.
**Jason Plumb** 32:02 That works for me.
**Hanson Ho** 32:04 span context. That's the one thing, it's not a context, but it's span context.
Hate this day, but it is what it is.
**Jason Plumb** 32:15 Yep, it's the portion of a span which must be serialized and propagated alongside of a distributed context.
It should be immutable.
Val, Val, Val, Val, Val, vowel.
Val, Val, Val. Looks pretty immutable to me.
Alright, it has to have a trace ID and a span ID, and a way to retrieve those.
Trace flags.
Entry estate.
**Jamie Lynch** 32:48 Yeah, have a bottle.
**Jason Plumb** 32:51 There's two types of flags, this seems like it should be a sub… A sub-thing, but can we open up trace flags while we're here?
Yes, the same package.
Trace Flags has sampled in random.
Cool.
Is there a reason not to do this as an enum?
Is this just, like, a more flexible… like, is one better than the other in this case? It's, like, a design standpoint. I don't…
**Jamie Lynch** 33:21 You mean the individual Boolean fields?
**Jason Plumb** 33:25 Yeah, rather than this being Booleans, making it trace flags as an enum that just has two options, one is sampled and one is random.
**Jamie Lynch** 33:35 I'd be pretty happy with that.
I'm trying to think of where else we have Booleans in our API.
**Jason Plumb** 33:47 I'm only thinking… I'm only thinking this because it, like, if there's a third state that ever gets added, or a fourth state, then the permutation space gets, like, obnoxious for users to deal with.
**Carlos Alberto Cortez** 33:56 Okay, stupid question from my side. Is it possible to specify the actual values of the enemies in Kotlin? Because, you know, they are actually flags, so it means that they can be both valid, or both zero, you know?
**Jason Plumb** 34:08 It can be both.
Oh, I see what you're saying. Yeah, oh, there's a… these are bit flags, oh yeah. Okay, and this comes from W3C.
Okay, okay, okay, I say we don't… I say we leave it. I say we don't mess with it. Yeah.
Sorry, I had forgotten that these are bit flags.
Thank you, Carlos. Trace State…
**Jamie Lynch** 34:47 So this is basically a map.
I can't remember.
**Hanson Ho** 34:52 This and… and, actual context, and… baggage.
They all seem…
**Jason Plumb** 35:03 Yep, how do you… oh, wait, we're still on span… this is part of span context that'll bring up trace state.
A list of key-value pairs, looks like we've got that. There's no real API discussion around this yet, because it just comes from the W3C.
There's a section on trace state handling, Oh, man.
When setting trace state values that are part of the OTEL ecosystem, they must all be contained.
In a single entry. This is implementation, this is not API.
Okay, I think… I think we're good on trace state for the API so far.
So then… on the trace span context, there's an ISREMOTE, Good.
And… So span context has to have a way, in the API, there must be a method to create a span context.
in the API.
**Jamie Lynch** 36:11 Yeah, so that lives on… be open telemetry.
instance. Yeah, so it's kind of… This is the implementation module, it would be span context factory here.
So, yeah, there's a… basically, you'd get the OpenSelemTree instance, and then you can pass in all the information you'd want.
**Jason Plumb** 36:39 So, help me understand what that looks like. So, you get the OpenTelemetry instance, and there's a method on that.
**Jamie Lynch** 36:46 Yeah, I'll see if I can find a test, as that might…
**Jason Plumb** 36:49 Cool.
**Jamie Lynch** 36:50 make it, more obvious, and I could explain.
Yeah, so… you'd basically get the… span context factory, so I think it would be, like, API.
spanfactory.create, and then you pass in, like, the trace ID, span ID, all the flags and shape.
**Jason Plumb** 37:23 Got it, so the span context factory… is a field on the OpenTelemetry API.
**Jamie Lynch** 37:30 Yes.
**Jason Plumb** 37:31 Cool.
then I think it's satisfied.
**Carlos Alberto Cortez** 37:35 By the way, what's the public side, or the user-facing side of the API?
**Jamie Lynch** 37:44 So that'd be on me.
OpenTelemetry, interface. So…
**Jason Plumb** 37:53 Span Context Factory.
Line 44.
**Jamie Lynch** 37:59 44 guests over here.
**Jason Plumb** 38:04 So that's the API, Carlos, is, like, it's on the top-level OpenTelemetry API called .spanContext.create.
**Carlos Alberto Cortez** 38:12 Okay, I remember what I wanted to ask, then. Yeah, like… You know, I think that for other stuff, it makes sense to have, like, the meter provider and the factory for other stuff, but… Bagash and spam should have a full implementation in the API that doesn't need to be overridden.
just for your information. If you want to keep it as a factory there, it's fine, but yeah, I don't think that… Just to super… to be super clear, we shouldn't allow these to be overridden.
**Jason Plumb** 38:43 Allow what to be overridden?
**Carlos Alberto Cortez** 38:45 like, span context factory, or baggage factory, for that matter. I don't know if… yeah?
**Jason Plumb** 38:52 I don't think the user can override those, like, are these, are these marked? Yeah, can we look.
**Jamie Lynch** 38:55 filter, you know.
**Carlos Alberto Cortez** 38:57 Okay, so… yeah, so that… then that… then we're fine.
**Jamie Lynch** 39:03 Cool.
**Jason Plumb** 39:03 Cool.
That looks like the end of span context, then.
And just to do a time check, I think we're at 7 minutes left.
**Jamie Lynch** 39:20 Okay, cool.
**Jason Plumb** 39:22 Within the same… like, just below… like, it's… Where is this?
Okay, the last… oh man, okay, it's… the dock site is hard to read when you're looking at the specs sometimes.
the… Retrieving the trace ID and span ID from the span context.
The API must allow retrieving of the trace ID and span ID in the following forms.
Hex, and binary.
**Jamie Lynch** 39:55 Yeah, so I think Pat's satisfied by… But, yeah, so we've got a string property and a byteway property for both.
**Jason Plumb** 40:05 Cool, so you can just call… when you call, oh, and the Java doc even says, or the KDoc says hexadecadecimal… And then the bytes is the raw bytes, which is binary.
**Jamie Lynch** 40:16 Yeah.
**Jason Plumb** 40:17 Feels okay to me.
**Jamie Lynch** 40:19 Yeah.
**Jason Plumb** 40:25 Okay, and we already talked about isValid, I think.
We have isValid on spam context? Yep.
**Jamie Lynch** 40:35 Yes,
**Jason Plumb** 40:41 Yep.
It is remote and trace date. Yeah, so I think we're good with that. So we're on to span.
I think we're done with spam context.
**Jamie Lynch** 40:53 Cool.
**Jason Plumb** 40:56 Span, here's a small API for us. We'll definitely finish that in 5 minutes.
**Jamie Lynch** 41:01 No problem.
**Jason Plumb** 41:04 Alright, the span, you can get its context. Bing, line 21. It's name.
**Jamie Lynch** 41:12 You can set the name.
**Jason Plumb** 41:16 Okay.
That, yeah, this does not yet talk about a getter, it just says the span encapsulates a name.
**Jamie Lynch** 41:25 I think it's, right, only this interface.
**Hanson Ho** 41:28 Yeah, explicitly.
**Jamie Lynch** 41:30 which I read…
**Jason Plumb** 41:31 Yep.
**Jamie Lynch** 41:32 Yum.
**Jason Plumb** 41:35 Parent span.
**Jamie Lynch** 41:38 Yep, so you can get the parent span context.
**Jason Plumb** 41:42 And… Right, and we have a choice here. The parent span could be another span, or a span context, or null.
But context is plenty.
I think that matches what Java does.
It's mankind.
**Jamie Lynch** 42:05 Let's see… So, that is not on the interface, but I think… Within the tracer, you can specify the span kind, which defaults to internal.
**Jason Plumb** 42:19 And where does… does that still get attached to the span, or…
**Jamie Lynch** 42:24 Yeah, so…
**Jason Plumb** 42:26 Yeah.
**Jamie Lynch** 42:27 Have a look at readable scan. Look at span data.
Lots of layers. Yeah, there's the spankind.
**Jason Plumb** 42:40 is on span data.
Does that match what Java does? Not like we have to, I'm just curious.
**Carlos Alberto Cortez** 42:47 What was the question again? Sorry?
**Jason Plumb** 42:50 The span kind being on span data.
And not on the SPAN interface.
**Jamie Lynch** 42:57 I think, from memory.
**Jason Plumb** 42:58 That does.
**Jamie Lynch** 42:59 You can set it at creation time, but then you can't access it until… The spam has ended.
**Carlos Alberto Cortez** 43:06 That's correct.
**Jason Plumb** 43:07 That seems great, yeah, that matches Java strongly.
Alright, start and end times… attributes…
**Jamie Lynch** 43:19 Let's see… Yeah, I think, again.
**Jason Plumb** 43:21 It's another interface that I implemented, I think.
Yeah. Attributes definitely are.
**Jamie Lynch** 43:27 on the SAN data, and… and timestamp as well.
**Jason Plumb** 43:33 Yep.
I think attributes were one of the interfaces that implements the span, not span data.
Oh, attribute container. Okay, there we go.
And then… Links? Spam links?
**Jamie Lynch** 43:52 I'm just trying to think where it is.
So there's this span link creator, and also, separately, span event creator, so basically… This is just an interface where you can add either links or events.
**Jason Plumb** 44:17 I'm not in love with that name.
**Jamie Lynch** 44:19 Hmm.
**Jason Plumb** 44:22 I don't… Have an immediate… suggestion that's helpful yet, but I don't love that name.
**Hanson Ho** 44:32 You're bumping up against the repeat of the word span, or creator?
**Jason Plumb** 44:36 Creator, yeah, if I call a create method, I want to get something back that you created for me.
even, like, something like spam link container might be better, because it implies that you're… you're holding a collection rather than making something for the consumer.
This is…
**Hanson Ho** 44:57 I think this is created because you… it… you can't get it back. This is another write-only API, which is… Which is why the name gets kind of weird.
**Jason Plumb** 45:07 Yeah, but I'm thinking, like, if I… if it was spam link container, then you add stuff to a container, right? So you could just say, like, add… add link.
You're adding to the container itself.
Versus having the creator add something to itself, you know what I mean?
**Hanson Ho** 45:27 I see, I see, I see.
**Jamie Lynch** 45:28 It would be consistent with… Attribute container as well.
**Jason Plumb** 45:33 Oh yeah, good call, good call.
Cool, so we can… I can… do you want me to open an issue on that?
**Jamie Lynch** 45:42 Sure, that'd be great.
**Jason Plumb** 45:44 Okay.
**Hanson Ho** 45:46 Event will be the same thing.
I will assume.
Because the naming scheme is the same, okay.
**Jason Plumb** 45:58 I mean, just because I'm griping about it, it's up to me to fix it.
Okay, what else?
Oh, we're not a designer.
**Jamie Lynch** 46:06 time.
**Jason Plumb** 46:07 Yep.
**Carlos Alberto Cortez** 46:08 By the way, I have a small question, like, maybe you know this, this is just random curiosity, but somebody was asking me, like, what's the status of Kotlin versus Swift and all that, and after explaining somebody, I realized that we… yeah, like, I don't know, like.
And what… probably the plan is that this can be offered in iOS as well, and this is a long-term plan, but do anybody of you know Swift as well, or not? Or we will just rely on what people know here from Kotlin multiplatform.
**Jamie Lynch** 46:41 I coded Swift when it was version 2, but, yeah, I mean… the… The implementation, in theory, should work.
on Swift, and I think, like, the core, like, tracing and logging Side of things.
I can't see a reason why it wouldn't work. Having said that, we've not tested it, there's no… Sort of, like, automated coverage to see if an app's actually working, so…
**Jason Plumb** 47:13 And just to clarify, Jamie, when you say it works on Swift, you mean on iOS?
**Jamie Lynch** 47:18 Yes.
**Jason Plumb** 47:20 iOS Target.
**Jamie Lynch** 47:21 We've got an iOS target, although there wouldn't be an impediment to offing, like, macOS and TVOS, if we wanted.
**Carlos Alberto Cortez** 47:30 Right.
**Jamie Lynch** 47:30 Yeah, it's just really a question of, like, testing and… If someone's interested in it, then… We could probably, like, accept contributions for that.
**Hanson Ho** 47:45 It's probably premature to talk about, like, you know, merging or replacing. I feel like this is… when this gets mature, then that discussion could be had whether or not we need, you know, a full Swift API, especially at the SDK level. I think… given where the technology is, and multiplatform on standalone iOS and Swift, I don't think… I don't think, Swift will remain for a while, the SDK, and also the instrumentation, so…
**Carlos Alberto Cortez** 48:19 Yeah, I think that matches my understanding, and yeah, okay, yeah, I didn't want to rush and tell people, like, yeah, we will be replacing that soon. It's like, yeah, long-term plan, like, I don't know, like, let's keep them separate for now.
**Jason Plumb** 48:31 Agreed.
**Hanson Ho** 48:33 let's replace Android first, and then we can talk about… not Android, but, like, the use case in OpenTelemetry Android.
**Jason Plumb** 48:39 Oh, yeah.
**Hanson Ho** 48:40 everything else.
**Jason Plumb** 48:41 Yeah, huh?
I mean, that's… that's kind of our North Star, right, is to have this being used by Android.
It'd be great.
Okay, cool, thanks everyone!
**Carlos Alberto Cortez** 48:53 Totally.
**Hanson Ho** 48:54 Thanks.
