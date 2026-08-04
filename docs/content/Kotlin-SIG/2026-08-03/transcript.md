SIG: Kotlin SIG
Date: 2026-08-03
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Ramachandra Bhardwaj** 00:37 Hello, Jim.
**Jamie Lynch** 00:40 Hey, how you doing?
**Ramachandra Bhardwaj** 00:43 Yeah, I'm doing fine. How about you?
**Jamie Lynch** 00:47 Yeah, I'm good. Still getting used to this new meeting link.
**Jason Plumb** 00:56 My meeting ran long, and I need to update my meeting… my copy meeting invite.
**Jamie Lynch** 01:02 Yep, me too.
**Jason Plumb** 01:07 I'm just gonna do that now before I forget.
Okay.
**Jamie Lynch** 02:07 I'll just give it a couple of minutes for folks to add stuff to the agenda, which I think is still in the meeting invite.
Yeah, it might be quite a light session, as I know that Hansen's out.
**Jason Plumb** 02:27 Yep.
**Jamie Lynch** 02:57 Cool, I guess we can just make a start. So, yeah, the… only real topic I came into this with was, I've created two PRs which mark the package API.
And the context API are stable.
So that's… Following on from what we discussed last time, basically.
So, yeah, these basically are just removing the experimental API annotations from The baggage and context interfaces.
So… I think everyone on the call Last week was okay with that, but it'd be good to get, some additional reviews and… If Vegas are okay with that, I'll just merge that down this week.
**Carlos Alberto Cortez** 03:54 Yeah.
**Jason Plumb** 03:55 Yeah, I think it's on track… yeah, I think it's on track. Go ahead, Carlos.
**Carlos Alberto Cortez** 03:57 Yeah, thank you. Yeah, sorry, I was busy with, other stuff, but this week I will have finally time. I'm reactively open, like, wide open, actually, so I will finally do a proper review for this one. Thank you so much for bringing that up.
**Jamie Lynch** 04:13 Awesome.
**Jason Plumb** 04:19 Yeah, I think it's in line with what we talked about last week, and so I think we're on track. I think both baggage and context are pretty… I don't think there's anything pending on those two at all.
**Carlos Alberto Cortez** 04:29 And were there.
**Jason Plumb** 04:29 Were there milestones for those?
**Jamie Lynch** 04:34 I think we have milestones. I think the milestones… to, yeah, the context API on any issues, at least tracked for that.
And… same with baggage, I think. We may have even closed that out.
**Jason Plumb** 04:50 Cool.
This is sort of a gut check on that one, but I think… Let's see… Yeah, nice.
**Carlos Alberto Cortez** 04:58 So, I have to say that Bagger seems straightforward to review, context is a little bit, It's going to be a little bit more interesting, I need to… check into the details, especially because, if I remember correctly, in Kotlin, there's no context out of the box, so that means that both, the backend and the mobile sites, they have to implement their own context stuff.
which is kind of unusual, but they found that JavaScript does the same, or that seems to be the case?
develop.
Maybe we… yeah, there's something that… We can compare there.
Bottom line, yeah, context could be taking longer. Either way, an initial review will happen this week, but yeah, backup seems straightforward so far.
**Jamie Lynch** 05:46 Awesome.
Yeah, I think just to… Clarify what we actually reviewed last week.
It was basically the actual API surface, rather than, like, the SDK implementation, so it was, like, creating a key.
Getting a value. Setting a value.
We didn't look at, like, the publication API in… Oh, we didn't look for, like… propagators, API, oh, like, creating different propagator types.
**Carlos Alberto Cortez** 06:19 Yeah, the only… you could say that the only thing which is kind of funny, and probably that comes back to what I was saying, is that, context is actually an implementation, like, you… you most of the time have an API and the SDK together.
how it's in Java or Python, for example, and they may rely on, you know, stuff belongs to the language, but I would say that JavaScript And Kotlin will be the… are the only ones that will have these two separations, you know?
**Jamie Lynch** 06:48 Hmm.
**Carlos Alberto Cortez** 06:49 He's become the check that, even though it's only the API, we have to make sure that this will be effectively something that would be nice for people implementing this to work.
So it just requires a little bit more of, double-checking that everything is good, yeah.
**Jamie Lynch** 07:05 Cool.
**Jason Plumb** 07:07 Yeah, and if I remember, the use case for that was applications that aren't doing any instrumentation, that still want to pass along context, right?
I think… was that the whole… Am I remembering that right?
**Carlos Alberto Cortez** 07:20 Yeah, there's something about that, yeah.
**Jason Plumb** 07:22 Yeah.
**Jamie Lynch** 07:25 Makes sense.
**Jason Plumb** 07:27 Kind of. I mean, it's… it's… I don't know, it's like you have an implementation at some point.
**Carlos Alberto Cortez** 07:32 Yeah.
**Jason Plumb** 07:34 Yeah.
**Carlos Alberto Cortez** 07:34 I remember in Java, back in the open tracing days, just for your amusement, we had different context implementations.
We had one for ACCA, which is a synchronous framework, and it was… Interesting, let's say, you know?
**Jason Plumb** 07:51 Yeah, I bet.
**Jamie Lynch** 07:59 Cool, so that was my topic, I will… open it up if anyone else wants to chat about things. Otherwise, we could take the time to review another interface, if folks feel like that would be a good use of time.
**Jason Plumb** 08:16 I think it would be.
Yeah, so what we did last time, Carlos, we kind of just went through, our list of, like, what was remaining to be stabilized in the API, and one of us was going through kind of the spec, and the other person was kind of going through the implementation, or whatever issues are open, and we're just kind of doing a comparison.
just, like, vocally, like, on this call, to just talk through, like, oh, do we have this, do we have this? And I thought it worked out pretty well.
**Jamie Lynch** 08:46 Hmm.
**Carlos Alberto Cortez** 08:46 Okay.
**Jason Plumb** 08:47 I lost him.
**Carlos Alberto Cortez** 08:48 Sounds good.
**Jamie Lynch** 08:51 Cool. So it's got to be one of these three, logging, tracing, or propagators. Any preferences?
**Jason Plumb** 09:02 Maybe logging?
**Jamie Lynch** 09:05 Okay.
**Carlos Alberto Cortez** 09:05 Yeah, login should be good, yeah.
**Jason Plumb** 09:09 Because it's a small API? One hopes.
**Jamie Lynch** 09:12 Yes.
We shall see.
Okay, so… logging should… We'll be under here.
So… Yeah, I think it's basically these three interfaces. We've got a logger provider, the logger itself, and the severity number.
Are you okay to bring up a spec, Jason?
**Jason Plumb** 09:44 Yeah, I think I just pasted it into the chat, so…
**Jamie Lynch** 09:47 Okay.
**Jason Plumb** 09:48 Logger provider… Do we have a default?
Like, if you don't… if you don't… because you need to be able to set… Or register a global default.
Logger provider?
**Jamie Lynch** 10:07 I think that comes down to the question of whether we want a global singleton Basically. Like, if you have an instance, That's a good point, actually. I don't know if we do have a, like, default logger implementation.
**Jason Plumb** 10:23 Is it on the OpenTelemetry interface? I bet it is.
**Jamie Lynch** 10:27 Yeah.
**Jason Plumb** 10:28 Like, you probably get a no-op or something, right?
Yeah, so what happens if you just get this?
What's the… what's the default?
**Jamie Lynch** 10:39 Whoa.
**Jason Plumb** 10:39 No diesel.
**Jamie Lynch** 10:42 So there would be a no-op implementation of this OpenTelemetry interface, or it's backed by a real SDK, so you'll always get something back, but…
**Jason Plumb** 10:56 And that is a… I mean, this is kind of outside of logging API now, but there's gotta be a way, when you create this OpenTelemetry instance.
to customize these. Like, in the Java world, they have the… Logger Provider Customizer, or logger… I forget the exact API, but they have a way to, like, configure The default logger provider.
**Jamie Lynch** 11:19 We can have a look and see what we do.
**Jason Plumb** 11:22 Cool.
**Carlos Alberto Cortez** 11:24 Yeah, there's sometimes the thing about… and I don't remember now what Java is doing for logging, that… driven exposed in the class itself, like, some noob method, like, returning, you know?
That's aside from the OpenTelemetry instance. I don't know. That could be an option, or Plan B.
**Jason Plumb** 11:43 Yeah, the thing… I guess the thing I'm describing is probably more part of auto-configuration.
**Carlos Alberto Cortez** 11:50 Yeah.
**Jason Plumb** 11:50 Where they have these customizers, but that's… it seems fine, so…
**Jamie Lynch** 12:04 So, yeah, I think it would be this logger provider config.
Which is on the DSL that currently would be how you… kind of, like, set of log limits, and
**Jason Plumb** 12:15 Yeah, yeah, this is… this is kind of the analog to the auto-configure in Java.
Great.
Okay, so back to the API. Sorry for pulling us far afield.
The only thing the logger provider has to do is to give you a logger, which is clearly there.
And it has to take a scope.
So getting a logger should take an instrumentation scope name, and I think that's missing.
**Carlos Alberto Cortez** 12:44 Which one again, sorry?
**Jason Plumb** 12:46 I guess the name is the instrumentation scope. Yeah, name is the instrumentation scope. Okay.
The spec's a little bit confusing, because it calls it two different things. It calls it both instrumentation scope and name.
So…
**Jamie Lynch** 13:01 That's the combination of name, version, and schema URL. Right.
**Jason Plumb** 13:06 Yeah, yep. Name, version, schema, URL, attributes.
That's cool And then let's look at logger.
**Carlos Alberto Cortez** 13:17 Tori, before we move there.
**Jason Plumb** 13:18 Yeah.
**Carlos Alberto Cortez** 13:19 But, yeah, so I was checking, now that you mentioned this part of spec, JSON, I saw that in Java, indeed, the logger provider interface provides this, static method where you return something. That kind of helps if somebody doesn't want to check on the OpenTelemetry instance.
And then you just pass it around. Like, for example, you're writing custom, like, instrumentation as part of a library, as Mongo, and you just rely on that if there's nothing.
That's very optional, of course, but we can consider that.
**Jason Plumb** 13:55 You're talking about the no-op?
**Carlos Alberto Cortez** 13:56 Right.
**Jason Plumb** 13:57 Yeah.
**Carlos Alberto Cortez** 13:58 Raya, the logger provider interface, yes. So, based on what we were saying before, if OpenTelemetry as an interface provides a default knob, that's probably fine, but probably there's, some advantage to having this also as, you know, here, a component here.
**Jason Plumb** 14:21 In the API.
Yeah.
**Carlos Alberto Cortez** 14:23 Although that circles back to what we were discussing in the past about whether we provide API with a knob or the knob separate, so…
**Jason Plumb** 14:34 Yeah, the spec doesn't require it.
So even though Java has it, it doesn't… I don't really read that in this spec, that it needs it.
**Carlos Alberto Cortez** 14:44 Yeah, the problem is that it doesn't, but it needs that in some places, like here, you know?
So, like, for example, in the part that you mentioned in the spec, it says logger provider. Normally, the logger provider is expected to be accessed from a central place, thus the API should provide a way to set Access a global default logo provider. Okay, never mind. Sorry, I misread that.
**Jason Plumb** 15:09 And I don't know where that is in Java, do you? Like, is there a way to set the global… Logger provider? Yes.
**Carlos Alberto Cortez** 15:15 Yes.
**Jason Plumb** 15:16 Where's that?
**Carlos Alberto Cortez** 15:17 In the OpenTelemetry, object, let me look for that.
**Jason Plumb** 15:22 I think we looked at this last week. No, I think you're right.
**Carlos Alberto Cortez** 15:25 Yeah.
**Jason Plumb** 15:25 It's… oh, so they… yeah, we did look at this last week. This is the… this is the kind of the trick they do with the log… with the logs bridge.
**Carlos Alberto Cortez** 15:35 It is discouraged, to some degree, if I remember correctly, even, but they have it.
**Jason Plumb** 15:39 Yeah.
It seems like they were reluctant to do, like, a true, you know, static singleton, and so… you can call… you can get the logs bridge… And that will give you a logger provider, but if I remember, the implementation on the SDK… I thought we looked at this last week.
Yeah, I'm not… I'm not remembering this correctly.
Yeah, sorry.
**Carlos Alberto Cortez** 16:16 What…
**Jason Plumb** 16:17 Well, do you think that's a blocker, Carlos?
**Carlos Alberto Cortez** 16:19 I think that we…
**Jason Plumb** 16:20 calling it stable?
**Carlos Alberto Cortez** 16:21 I would say, let's open an issue and send that to me. I can do some digging and ask Jack for his opinion initially.
**Jason Plumb** 16:29 Okay.
**Carlos Alberto Cortez** 16:30 I mean, yeah, we can do that, just in case, you know?
**Jason Plumb** 16:33 Okay.
**Carlos Alberto Cortez** 16:34 Assigned that to me, yeah.
**Jason Plumb** 16:38 It's really the concern about the, like, being able to set the global, that's the main thing we're… We're picking apart from the spec.
**Carlos Alberto Cortez** 16:46 Yeah.
**Jason Plumb** 16:46 Right? Yeah, correct.
The no-op is not a blocker.
**Carlos Alberto Cortez** 16:53 It's a separate topic, maybe it will be, because it will come as a whole, you know, for tracing and logging and eventually metrics.
Actually, if we have such issue, I would like to probably tackle that first.
Or maybe we can… if we don't, let's create, Jamie, or I can do that, create an issue to discuss that again, once more. I think we had it somewhere.
**Jamie Lynch** 17:15 To discuss, like, Like, a global…
**Carlos Alberto Cortez** 17:20 the new, the new op, whether it's part of the API or it's separate.
I think we had it, I remember.
**Jamie Lynch** 17:31 Right.
Let's see… Well, I can't see it, so I will create a new issue, and then we can discuss on that.
**Carlos Alberto Cortez** 17:48 Yeah, and send that to me, so I can, like, do the digging on the front.
**Jamie Lynch** 18:05 I think, for the record, my opinion is the API should be separate of any implementation, and I think the know-op counts as an implementation, but I'd be interested to see What other, like, distributions are doing for this.
**Carlos Alberto Cortez** 18:23 Yeah, I mean, the only thing I remember now, and this is just for your information, is that I very briefly brought that to the specification call, and other maintainers think that there's some merit in keeping Kotlin as uniform.
To the other languages, because, you know, they have these two.
But that's the only thing for now.
**Jamie Lynch** 18:44 Hmm.
**Carlos Alberto Cortez** 18:44 Very initial, like, feedback.
**Jason Plumb** 18:48 And just to refresh you, Carlos, in case you'd forgotten, there is a module in Kotlin called Noop.
It's literally the implement… it's a no-op implementation of the API. So, like, a user who wants That, by default, is able to get it, but they do have to take a dependency and wire it up.
**Carlos Alberto Cortez** 19:06 Yeah, yeah, yeah, yeah, I remember, yeah, yeah, yeah. Okay.
**Jason Plumb** 19:08 I just wanted to call that out.
**Carlos Alberto Cortez** 19:09 Yeah, that's why I was thinking, like, whether, like, we bring that module into the API, or we keep that separate, no? Yeah.
So that's, yeah, I think.
**Jason Plumb** 19:19 Okay.
**Jamie Lynch** 19:21 Boom.
**Carlos Alberto Cortez** 19:21 Yeah, don't forget to send that to me, yeah, that's for me.
**Jamie Lynch** 19:24 Yeah, I added a note to it, so I knew.
Cool.
Anything else to discuss about logger provider?
**Jason Plumb** 19:38 No, I don't think so. It's pretty, pretty straightforward. You can get a logger.
And the logger takes the things we talked about, There's a little bit of implementation in the spec here, but whatever.
Yeah, logger needs to be able to emit, yeah.
Alright, timestamp.
Observe timestamp.
Context.
Severity number, severity text.
Body… attributes.
Event name.
We don't… oh, we do have a VIN name, okay.
**Jamie Lynch** 20:22 Just fine.
**Jason Plumb** 20:22 just the order is slightly different, but I kind of like… I don't know, do I like the order? I don't know.
I don't think it matters. Like, by convention, Kotlin's gonna use… for a method this large, Kotlin's gonna use name parameters anyway, so order shouldn't matter.
Okay.
There's an optional exception or error.
Which we have. Good.
Okay, and then we can move on to enabled.
The logger API should allow the user to see if it's enabled.
And it accepts context, severity, number, and event name.
Looks like we've got those.
a context… It's… it looks like context is required, but we have it as nullable.
Okay, when implicit context is supported.
This parameter should be optional. That's gotta be why it's nullable.
So, I guess the implementation would look at the implicit context in that case, which makes sense to me.
**Carlos Alberto Cortez** 21:45 Yep.
**Jason Plumb** 21:46 Okay, so I think we've got those covered.
And it's a Boolean… yes.
There's… the spec even calls out.
The documentation for the method, which needs to say that you need to call this more than once.
So, that the value returned from the enabled check is not static.
And that, the API should… I'm quoting here. The API should be documented that instrumentation authors need to call this API each time they emit a log record to ensure they have the most up-to-date response.
**Carlos Alberto Cortez** 22:30 That was because of synchronization between threads, you know? Like, whether you are actually seeing the latest value or not.
**Jason Plumb** 22:37 Yeah, you shouldn't cache the enabled value, is the thing.
**Carlos Alberto Cortez** 22:40 Yep.
**Jamie Lynch** 22:41 Cool.
So, my readers, we could probably update the docs on that function.
**Jason Plumb** 22:47 Yeah.
**Jamie Lynch** 22:48 be a bit more explicit about that.
**Jason Plumb** 22:50 I agree.
**Jamie Lynch** 22:53 I can do that.
**Jason Plumb** 22:57 It wouldn't be the end of the world if we had marked that stable and needed to, shore it up by adding some Javadoc or KDoc.
**Carlos Alberto Cortez** 23:05 No, that was added, actually, also, like, relatively recently, so it's…
**Jason Plumb** 23:11 Oh, okay.
**Carlos Alberto Cortez** 23:11 I am.
I think…
**Jason Plumb** 23:19 Ergonomic API, what is that?
**Carlos Alberto Cortez** 23:22 That's in case you want to add some API on top of the specification API.
**Jason Plumb** 23:30 Yeah.
**Carlos Alberto Cortez** 23:31 Make it easier for users, you know?
**Jason Plumb** 23:33 Yeah, I don't even think it needs to be in the spec. That should just be a given to me, but it's nice to have it listed.
**Carlos Alberto Cortez** 23:41 Yeah, I remember it came from Glow, and I don't remember the details now.
**Jason Plumb** 23:46 Yeah.
I mean, Android has… On its top-level interface, it has, emit event.
We made an ergonomic event API.
That's it, that's the bottom of the logging spec.
**Jamie Lynch** 24:04 Oh, awesome.
**Jason Plumb** 24:04 Yeah, I think we… I think we did it.
**Jamie Lynch** 24:07 So that would still completeness.
**Jason Plumb** 24:10 Yeah, we found just that one little, oh, severity number. I don't even think it's… Severity number is not even… is it in this spec?
I think it links to the spec, let's see.
Yeah, 1 through 4… Y-yeah, you got it.
So zero's unspecified, does that map over to what we have?
**Jamie Lynch** 24:42 boat.
**Jason Plumb** 24:48 Yeah, that seems good.
**Jamie Lynch** 25:01 Cool.
Anything further to check? I think we've got to the end of all the fees, haven't we?
**Jason Plumb** 25:09 I think so.
Was there some benefits in keeping that as an enum?
**Jamie Lynch** 25:17 Severity number.
**Jason Plumb** 25:18 Yeah.
**Jamie Lynch** 25:23 What else would we send it as, like, as an int, maybe?
**Jason Plumb** 25:28 Or even if it's a class just, like, with a… A fixed number of implementations that are… you know, Java static, or static in this case. I guess it wouldn't be Java static, but static.
So, you know, private constructor, and then just a bunch of constants defined with these values.
Or even a range of values. I don't know, it's just… the… I'm being super-duper nitpicky and pedantic, by the way, so this is ridiculous.
There's a weird asymmetry between error and error 2, because error doesn't… is not error 1, and the numbers that are ref… those suffixes that are appended onto the enum names.
don't map over in any way to the actual severity number, and it's just… these ranges, I don't know, like, it's… it's silly to have these, like.
discretized ranges, in my… in my opinion, but… Like, does anybody really care or know about the difference between severity number 6 and severity number 8? Like, there's just debug, right? Like, most people don't care about that.
**Jamie Lynch** 26:32 I agree.
**Jason Plumb** 26:33 Clarity.
And it reads funny to me.
**Carlos Alberto Cortez** 26:35 I think that the problem came from trying to support many legacy login systems which may have, like.
**Jason Plumb** 26:43 Yeah.
**Carlos Alberto Cortez** 26:43 And suddenly, you want to… We wanted to be as… Compatible with them as possible, so…
**Jason Plumb** 26:51 Yep.
Yeah, this is… this is fine, I'm just… I'm being… I'm being super nitpicky.
**Carlos Alberto Cortez** 26:58 Yeah, that's the phone with 14 leggas stuff.
**Jason Plumb** 27:01 Yeah.
**Jamie Lynch** 27:05 Okay, so… I will update the KDoc, and I'll also add a comment where we discussed everything else, and we're just waiting on, these two actions.
**Jason Plumb** 27:20 Cool.
**Jamie Lynch** 27:35 Cool.
So, I think we've got about 15 more minutes. Were there other topics? Did folks want to start another API service, or should we just call it early?
**Jason Plumb** 27:49 I think we could start.
Cool. How do you feel?
**Jamie Lynch** 27:54 That's fine by me.
**Jason Plumb** 27:58 What was last left? Tracing metrics, what else?
**Jamie Lynch** 28:04 Let's have a look. I think it was Tracing and propagators.
**Jason Plumb** 28:08 Maybe we could do propagators.
**Jamie Lynch** 28:12 Cool.
Yeah, so we had this… Same discussion last week about Whether setting a global propagator was required, and what kind of use case was for that before.
So, we could dive into that a little bit, or just look at the interfaces.
**Jason Plumb** 28:41 Yeah, if we did this one last week, we may not need to go over it again, although having Carlos here is nice.
**Carlos Alberto Cortez** 28:47 Yeah, I would say that, This is probably the exception, and that's something that is important, because, you need the application, like, it doesn't matter what you're doing, at some point, the user installs something, and you want to use the same. You may not be needing to use the same login, the logger provider, or trace provider, but propagators, in theory, you should be using only one.
But, reading on the ticket, on the issue, Can you send it to me as well? I will be doing some follow-up, just in case, you know? Yeah.
Okay.
So we'll be doing the previous one and this one this week. Okay.
**Jason Plumb** 29:43 Cool, yeah, that's super helpful, Carlos.
**Carlos Alberto Cortez** 29:46 Let's do that.
**Jason Plumb** 29:47 Yeah, I don't know that we should go through this again, because we went through it last week. Yeah.
**Carlos Alberto Cortez** 29:51 Nope.
**Jamie Lynch** 29:56 Cool, I guess that leaves… tracing,
**Jason Plumb** 30:03 Yeah, metrics.
**Jamie Lynch** 30:04 Metrics, which will definitely just take 10 minutes.
**Jason Plumb** 30:08 Yeah, that's all.
**Jamie Lynch** 30:11 Okay.
So… I guess we would start in Teresa Paveda, which is… Probably a mirror image of Logger Provider.
**Jason Plumb** 30:38 Yeah, sorry, they put time stuff first ahead of the tracer provider.
**Jamie Lynch** 30:42 Hmm.
**Jason Plumb** 30:42 Which is just, like, it's kind of contextual, just background, like, we do stuff in nanoseconds, or millis.
Okay.
Tracers can be accessed with a tracer provider.
That looks good.
Tracer provider, access from a central place, get and set the global. So, same question here.
**Jamie Lynch** 31:09 Yeah, so it's accessed in a… the same way as…
**Jason Plumb** 31:12 Yeah, yeah.
**Jamie Lynch** 31:13 blogger providers are just on the OpenTelemetry interface.
**Jason Plumb** 31:17 Cool, so the parameters to get a tracer from the tracer provider… Name, version, schema, attributes.
That's it.
And… optional, name is required, yep.
Cool.
Mmm… There's some implementation details in the spec, of course.
Context.
**Jamie Lynch** 31:56 Was that on Tracer Provider, sorry?
**Jason Plumb** 32:01 No, it's the next part of the tracing API, though, is…
**Jamie Lynch** 32:03 Oh, okay.
**Jason Plumb** 32:04 It's really interesting. So, I historically was very diligent about always calling this either a span context or a tracing context, but it seems like over time, the idea has really gelled into just the context, but the spec is kind of interesting here, in that I mean, the context… it's a section called Context Interaction that does mention context, but later on it also mentions span context.
So, the API must provide a way to get a span from a context.
**Jamie Lynch** 32:47 Get spammed from a context.
I think that's in there somewhere, so… I think it's in one of these two.
**Jason Plumb** 33:07 There you go.
**Jamie Lynch** 33:08 Yeah.
So that would be on the OpenTelem degree interface, and you'd call from spam context.
**Jason Plumb** 33:21 And then there needs to be a way to combine the span with a context instance, creating a new context.
**Jamie Lynch** 33:31 So… This is where an example.
**Jason Plumb** 33:40 Is that the spam column?
**Jamie Lynch** 33:41 Examples would be…
**Jason Plumb** 33:42 Factory, maybe? Span Context Factory?
**Jamie Lynch** 33:44 Let's have a look.
**Jason Plumb** 33:50 No, these are from making span contacts.
**Jamie Lynch** 33:55 Possibly on… span itself.
I know, but it's possible to do this, I just can't remember what…
**Jason Plumb** 34:09 Yeah, do we…
**Jamie Lynch** 34:10 Who knows?
**Jason Plumb** 34:10 Do we have a straight-up context interface?
We do, right? It's in context, though.
**Jamie Lynch** 34:15 Yeah.
**Jason Plumb** 34:24 Okay, so within span context, I need to skip ahead in the spec, because there's a section about context, and how it should interact, like, how the… tracing APIs should interact in a few ways with context, not span context, but just context.
**Jamie Lynch** 34:39 Hmm.
**Jason Plumb** 34:40 And then below that is spam context, so… We gotta get through the tracer operations first, though. Okay, so back to the tracer… Can you create a new span?
Yep.
**Jamie Lynch** 34:58 Yep, so that's… Star's fun.
**Jason Plumb** 35:05 And, report if a tracer is enabled. So that's probably on… yep, line 28.
no parameters, returns a Boolean… Not static, so the same docs problem exists here, too, probably, for enabled.
**Jamie Lynch** 35:29 Hmm.
**Jason Plumb** 35:30 This should be invoked each time, we have it already.
Yeah, to get an updated response. Cool. So we got that covered. Okay.
Now we're on to span context.
Okay.
Trace flags, trace state.
Span context.
is remote.
Yeah, the way that the spec is structured here is not my favorite, but let's kind of try and stumble through these. Okay.
Span context represents a portion of a span.
It's W3C. It contains two identifiers, trace ID and span ID. I certainly hope we have those.
Okay, and then… sorry, just going through very slowly here. Trace flags is the next thing.
**Jamie Lynch** 36:29 That's a week.
**Jason Plumb** 36:30 have, and then the trace flags… If we dig into that, just to walk the tree here, sampled in random… Good.
Okay, back out to span con… oh, wait.
Yes, back out.
Okay, then isRemote… And… The API must implement methods to create a span context.
These methods should be the only way to create a span context.
So the spec is pretty strongly worded about this, but the API must implement methods to make a span context.
**Jamie Lynch** 37:15 Yeah, so that would be these two.
**Jason Plumb** 37:19 And where are those implementations?
**Jamie Lynch** 37:25 What's the implementation of this?
**Jason Plumb** 37:28 Yeah.
**Jamie Lynch** 37:31 would be… spring complex factory limits.
**Jason Plumb** 37:38 Cool.
**Jamie Lynch** 37:39 Yeah.
**Jason Plumb** 37:40 Yeah, like, line 25. Yeah, that looks good.
And this is part of the API.
Or is it not?
**Jamie Lynch** 37:52 So, this is a meat implementation.
**Jason Plumb** 37:55 So this is one of the cases where the spec is pretty clear about this, and it says, the API must implement methods to create a span context. These methods should be the only way to create a span context.
That's a little squishy. But, the next sentence, this functionality must be fully implemented in the API and should not be overwritable.
That part about being fully implemented in the API is pretty strong to me.
**Carlos Alberto Cortez** 38:27 Sorry, was that about trace flags, or…
**Jason Plumb** 38:30 No, about, span context.
**Carlos Alberto Cortez** 38:35 Right.
Right, yes, yes, yes, correct, that's how it's in Java, yeah.
**Jason Plumb** 38:43 Well, I think we might need to move this.
Unfortunately.
**Jamie Lynch** 38:47 Hmm.
There we go. I'll add an action to have a look at that.
**Jason Plumb** 38:53 And they cannot be overwritable. So, I don't know if that is the case yet.
I'll just put a convenient link in the doc as well, just to the… to the thing.
And cool, we're cutting it a little bit close on time, and there's no way we're gonna finish the tracing API, but… Okay, that's one little friction point. The retrieving the trace ID and span ID, the API must allow the retrieval of the span ID and trace ID, then it talks about their format.
the… Span context is remote is valid.
And then is, trace state… Yep.
And trace state is just sort of a key value bag.
**Jamie Lynch** 40:19 Yeah, basically.
**Jason Plumb** 40:20 Yep.
Delete…
**Jamie Lynch** 40:23 Excuse me.
**Jason Plumb** 40:23 Yeah, okay. I think we have all that.
And that's it for, span context.
**Jamie Lynch** 40:33 Okay, cool. So, I think we'll probably wrap up.
Fair. So…
**Jason Plumb** 40:40 Good to meet. Yeah.
**Jamie Lynch** 40:42 We've, what interfaces were we okay with, and I know there was… Yeah, like, spam context seems like we need to look at the spec again and kind of review what's happening there.
**Jason Plumb** 40:57 With that implementation to create one.
**Jamie Lynch** 41:00 Yeah.
**Jason Plumb** 41:01 Yeah.
**Jamie Lynch** 41:04 Cool, so that's one… And… I think… Were we okay with Tracer provider and tracer? Or is there stuff to do on that?
**Jason Plumb** 41:18 I think we were okay with those.
Yeah.
**Jamie Lynch** 41:23 Okay.
I will update the issue to note that we've looked at those, so… And I think I'll probably create a list of all the interfaces we do need to review,
**Jason Plumb** 41:34 Cool, yeah.
I'll just make that note, too. Like, we did leave off before.
Span.
Why am I a dingo?
Want to be a dingo.
**Jamie Lynch** 42:00 Awesome.
**Jason Plumb** 42:02 Thanks for running that, Jamie. Yeah.
**Jamie Lynch** 42:04 Yo.
Thanks, everyone. Thanks, everyone, for coming.
Yeah, and I guess I'll see you next week.
**Carlos Alberto Cortez** 42:11 Yeah, particular line.
**Jason Plumb** 42:13 Alright, thanks everyone.
**Ramachandra Bhardwaj** 42:14 Yeah, I just have a small, doubt, or…
**Jason Plumb** 42:19 Oh yeah, what's up? Yeah, we're wrapping up, but what's up?
**Ramachandra Bhardwaj** 42:22 Yeah, I'm sorry. So, basically, I just kind of went through the setup and kind of having it all, you know, set up in Android Studio, and I was working on Measurements API. So, while looking at that, I saw that, you know, for each particular measurement, like, we have for counters, gauge, and histograms.
In Java, we kind of have a particular data type, specific classes which are there.
And we don't have a measurement per se, an interface or a class. That's completely different than compared to Python, because in Python, we have a class for measurement.
So, that's the reason I was thinking when we kind of need to implement Measurements API here, we need to have it for observable measurement, because that's where the actual marker interface is.
and in Java, and each kind of, instrument which is there, like, observable instrument, that kind of, you know, extends that, observable measurement interface and adds it. So, I just thought that maybe I can kind of do that thing, because there is a PR open currently, that's for counters and stuff, so the, is my understanding kind of right for the Michelleman?
**Jason Plumb** 43:37 I can't give… I can't give an authoritative, answer on that, I'm sorry.
**Ramachandra Bhardwaj** 43:43 Okay, so, I mean, the thought process, like, just to kind of have it one-to-one mapping with Java, is that correct, right? Like, we don't have…
**Jason Plumb** 43:53 No, we want to err on the side of making it spec compliant, but also idiomatic for the Kotlin language. So, just because Java did something doesn't necessarily mean we want to follow the same pattern. In many cases, we do, because what they did, like, is just natural and falls out from the spec.
But there's nothing that strongly binds us to do it the same way.
If that makes sense.
**Ramachandra Bhardwaj** 44:19 Yeah, that makes sense, okay.
**Jason Plumb** 44:22 Yeah, I mean, we wouldn't want somebody to come in and be completely surprised, like, being like, oh, Kotlin did it completely differently. Like, that's not one of the goals. We're not trying to be too clever, but we are also trying to keep things aligned with, idiomatic Kotlin constructs where we can.
**Ramachandra Bhardwaj** 44:38 Understood, okay.
**Jason Plumb** 44:39 Yeah, sorry, I have to drop, and I'm sorry we didn't get to it. If you want to bring this up again next week, or just ping us on Slack, we can continue this conversation.
Is that cool?
**Ramachandra Bhardwaj** 44:49 Yeah, I'll… yeah, I'll ping on Slack regarding this, and I'll just go through it again.
**Jason Plumb** 44:54 And feel free to have it, like, as the first item for next week, too.
Like, put it in the agenda. Okay, cool. Thanks.
**Ramachandra Bhardwaj** 45:01 Thank you.
**Carlos Alberto Cortez** 45:03 See you!
**Ramachandra Bhardwaj** 45:08 hi, David.
Yeah, it is distinct from synchronous instrument. I was just talking about your PR, actually, because you implemented the counter one, right? The thing was, Java also does the same kind of thing for each data type. We kind of have a particular class for counters, gauges, and metrics.
So, yeah, but for the observable instruments, that's completely, like, that's the same thing which I said, but an interface is there at the, like, top. So, yeah.
**DavidGrath** 45:43 Oh, alright, thanks.
I'm on…
**Ramachandra Bhardwaj** 45:52 Yep.
Take care. Bye.
