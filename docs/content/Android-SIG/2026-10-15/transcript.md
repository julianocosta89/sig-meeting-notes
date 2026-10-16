SIG: Android SIG
Date: 2026-10-15
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Ben Joseph** 04:41 Hey, David.
**Jason Plumb** 05:19 Hey, good morning.
**Ben Joseph** 05:22 Good morning, all.
**Jason Plumb** 05:29 Let me bring up the docs.
**Cesar Munoz** 05:48 Hello.
**Jason Plumb** 05:50 This is our… We have a couple of topics front-loaded, but if anyone has anything they want to add, there's… looks like there's plenty of room.
I'll give it another 30 seconds.
Okay, Vishwan, why don't you start us off this morning?
**Vishwan aranha** 06:45 Sure, sounds good. So I wanted to get, like, your input on the remaining session work before I take it further. And I have added, like, diagrams to help explain the startup and replay flows in the respective links that I've added there. But there are, like.
three related questions that I have, like, for sampler configuration and, like, sharing sampling decisions with logs and, like, restart attribution, so… We can take them one at a time, so it's easier to discuss and go through it.
So, if you have 2096 open, so you can see Jamie's comment on there, like, Jamie suggested, like, allowing a general sampler in DSL, which makes sense to me, so I use, like, a factory, because the session-based, like, sampler needs the final session provider before instrumentation starts, like.
But how would you, like, prefer to expose that? Would a general factory receiving the provider work, or would you prefer, like, another approach for this?
**Jason Plumb** 07:50 So I want to make sure I have context, just to rewind a little bit. So the… This, I think there's an issue on this, but… so, session-aware trace sampling… This already exists, but this is just stitching it up to the DSL.
**Vishwan aranha** 08:07 Yeah, basically, yeah.
**Jason Plumb** 08:08 Okay.
So, session, sampler, and then you specify an implementation. Without looking at the code yet, this is how that reads.
**Vishwan aranha** 08:17 Yeah, and I think it was recommended by someone, like Jamie or Cesar, I don't remember. But yeah, I added that, added this based on their recommendation.
And the session-based trace, like, sampler already exists for sure, but this PR, like, wires it into initialization, so, like, it receives the final session provider before the instrumentation starts. And.
Log sampling basically is, like, separate from this discussion.
**Jason Plumb** 08:44 Got it, okay, cool. Thanks for setting that basis. And so what was the feedback? What was the comment?
Jamie, looks like you were like, we should just be able to pass in a sampler, but that's… that's kind of what this is. Oh, it's not… it's a session sampler instead of just a sampler. Yeah, okay.
**Vishwan aranha** 09:04 So it's a general and session center.
**Jason Plumb** 09:07 Kind of like inverting those two, the relationship there.
I see.
**Jamie Lynch (Palo Alto Networks)** 09:12 So I guess my comment on this was basically saying, do we want the ability to just generally set a sampler instead?
Because otherwise you could potentially end up with, like, precedence issues.
**Jason Plumb** 09:28 Definitely think you'd want to be explicit, too. I mean, I don't know what sampling for logging looks like off the top of my head right now, but definitely we would want to make that distinction, I think, between log sampling, span sampling, and in this case, if there is… I think I saw this issue that kind of tries to tie those two together, or to be able to make sampling decisions for both based on the session ID, which I think makes a lot of sense.
Then we gotta figure out how that fits into both, or do you just require it to be passed into both? How… Yeah, I'm not sure. What do people think?
**Cesar Munoz** 10:06 Well, the way I see it as it is now, the proposed DSL.
will be that I set a sampler that will sample the whole session.
So, everything that… gets created in that session. At least that's… intuitively what it looks like to me.
**Jason Plumb** 10:28 Okay.
**Cesar Munoz** 10:29 And, which I… based on what you said, Vishwan, it's probably not correct, because this only affects spans.
So is that right?
**Vishwan aranha** 10:40 Yeah, and I'm happy to make the configuration general for that. The factory that we already have, like, it already returns a regular sampler. The session-specific part is, like, the access to the provider. So, I can make any changes if everybody is, like, in the same page.
**Cesar Munoz** 10:59 I guess, I guess, personally, the thing is that I don't have a… like a hard preference. I'm trying to see, like, if we put the sampler option outside of the session object.
I guess I'm trying to think what use cases that could help with. And so, could it be that… We could provide a sampler that… Mmm.
Could be anything, could be attached to a session or not.
**Jason Plumb** 11:33 Yeah, or maybe the app, like, for example, an application that has, like, a login, maybe they have a test user, and they're like, oh, we don't want any telemetry from test user, right? So they just want to drop it all and not, you know, so normal sampling use case could just be, like, drop everything.
**Cesar Munoz** 11:49 That sounds more flexible, which I like because.
It will be, like, if we tie it into sessions, and then… Yeah, I wouldn't want somebody else in the future coming and saying, I want to sample based on whatever, and then I can't.
**Vishwan aranha** 12:05 Yeah.
**Cesar Munoz** 12:06 Or maybe they do…
**Vishwan aranha** 12:07 Someone's good.
**Cesar Munoz** 12:08 Yeah.
**Vishwan aranha** 12:08 And someone could want, like, automated tree sampling without trying it… tying it, like, to sessions for itself. So… A general option would probably support both, so it would make sense.
**Cesar Munoz** 12:22 Yeah, it sounds good to me, then, the general option as well.
**Jason Plumb** 12:28 So, instead of session kind of being at the, I'm saying top level, but at this level, at this configuration route, it would be sampler, and then inside of sampler, do we have, then, a section for spans, a section for… Logs, and then a section for session.
Is that the way we expect this to work? How would we envision that?
**Cesar Munoz** 12:54 So.
**Vishwan aranha** 12:54 So.
**Cesar Munoz** 12:56 Yeah, sorry, go ahead.
**Vishwan aranha** 12:58 So my thinking is that, that could work, like, with each signal, like, configured explicitly. Like, basically, I wanted to agree, like, overall shape, but.
One distinction for the test user sampler is, like, setting the trace sampler alone without… wouldn't, like, drop logs or anything, so…
**Jason Plumb** 13:22 I'm just riffing on what it might look like here, so…
**Vishwan aranha** 13:24 Yeah.
**Jason Plumb** 13:25 Like,
**Vishwan aranha** 13:29 I think it could probably have included, like, both sessions and other things in, Add it in that, so that would… That's what my assumption is, so I have to cross-check and see if that works out.
**Cesar Munoz** 13:50 Oh, I see.
**Jamie Lynch (Palo Alto Networks)** 13:59 Hey.
This might be a… Interesting question.
Are there samplers for anything other than tracing and open telemetry?
**Jason Plumb** 14:09 So.
**Cesar Munoz** 14:09 I'm aware of, no.
**Jason Plumb** 14:10 I don't know that these exist yet. Like, I don't know that you… I don't know that there is a log sampler, but I think there is a way to accomplish it. I just don't remember off the top of my head how to do it.
So, certainly punting on this in the short term seems okay to me.
But I… I just expect that to be a use case that people will ask for.
There also is, like, a lack of, kind of, symmetry or parity between those two.
**Jamie Lynch (Palo Alto Networks)** 14:37 Yep.
**Vishwan aranha** 14:39 And I think there's a Java sampler interface. We're using it, is that tree-specific?
And for logs like the proposal is like filtering through the log processor. So we shouldn't assume the same sampler. Api works for both.
**Jason Plumb** 14:53 You're saying that is the recommendation?
**Vishwan aranha** 14:56 Yeah. Okay.
**Jason Plumb** 14:59 Through a log processor?
**Vishwan aranha** 15:03 Sir, what is it?
**Cesar Munoz** 15:04 Yeah, it could be.
processor… even the exporter. But I guess it depends how deep we wanna.
**Vishwan aranha** 15:12 Yeah, and that's the approach I think was proposed in 970. We haven't agreed, like, to… on, log API yet.
For this, I'm happy to, like, keep the scope to general tree sampler configuration as we go.
**Cesar Munoz** 15:29 That sounds good.
And, and, and the way Jason has proposed it… I'm not sure if it's the best option, it probably is. I'm just saying that it's nice that It seems easy to extend.
Later, you know, if we want to add… other signals.
So so I guess, based on this, we will add sampler session and trace only for now.
or just session, I don't know what's the scope of this.
This is only for… no, this is for both.
Session and trace.
Well…
**Vishwan aranha** 16:15 I'm open to adding them both, and we can, like, build upon it, but what are you guys' thoughts on that?
**Cesar Munoz** 16:22 But the session… so if we add something to the session option here in the conference that Jason is providing.
That will only affect traces, still. So, it's kind of redundant to see that, and then trace.
**Vishwan aranha** 16:39 Right below it. Yeah, both would like still configure. Trace something here.
the.
**Cesar Munoz** 16:45 So maybe…
**Vishwan aranha** 16:46 Session-based one, like, sampler is, like, one kind of a trace sampler, I believe, so… I'm thinking out loud, like, here, if we, like, expose separate session and trace blocks, are those alternatives, or should they, like, compose when both are set?
**Jason Plumb** 17:09 Is the ask, like, are we intending to change the semantics of session sampling to include both?
**Vishwan aranha** 17:16 Yeah, should we include both, or… yeah, that's the open question.
**Jason Plumb** 17:21 I mean, I can tell you for sure that this predates having any events in the SDK, so… That's… it's… I'm sure it's only historical. I… I can't think of any valid reason why someone would want one or the other sampled? Like, oh, only sample the traces, or only sample the logs.
Like, the goal is to reduce your data volume, and if you want to do that, let's do it across the board for all the signals. Like, when you… when you don't sample a session.
And that, again, the OTEL terminology has always been confusing about what it means to sample. When you sample something in for inclusion, then, yeah, you create telemetry for it. If you don't sample something, then I think it's… I think we should omit Omit both… Or all signals for that.
Session, or during that session.
**Cesar Munoz** 18:19 I agree with that. It's just that I think we don't have the… mechanism to do that right now. So…
**Jason Plumb** 18:27 Don't, right, yeah, so,
**Cesar Munoz** 18:30 Either then, we should… Kind of block this until we have it, or maybe add it all as part of this work, or… If… If we like the idea of just providing a way for users to add a trace sampler.
Then we could just leave the sampler.trace.
object.
which could receive a session… session… Stampler.
implementation.
Which will just affect traces.
Per session.
That's… but yeah, I mean, that would probably clash with this idea of… I guess it depends on them.
what we want. It will brush with this idea of having a session sampler affect all of the signals.
I'm not even sure all of the signals, I don't know if metrics… 2, so…
**Jason Plumb** 19:29 Yeah.
**Vishwan aranha** 19:30 And I think Cesar, the last option, kind of works for me, like, keeping this 2096 focused on, like, trace sampler configuration, including, like, any session over implementation that need the initialized provider, so then we can handle, like, shared trace and, like, log sampling in the next ticket, which was, like, 970, I believe. So.
I just wanted to see if everyone agrees to that scope. So if any issues.
**Hanson Ho** 19:56 So.
**Jason Plumb** 19:57 So you're asking, I want to be clear, you're asking if it's okay or if you should.
change this PR to be scoped only for configuring trace-based sampling.
**Vishwan aranha** 20:10 Yes, so we could, like, include update. I can update it to just have, like, trace-based sampling Like Cesar mentioned in his option, like, which would include, like, session over implementation that need, like, the initialized provider.
**Cesar Munoz** 20:26 I mean, that will be an option that will keep the existing functionality that we provide with Core.
But with the DSL.
**Jason Plumb** 20:37 I'm okay with that. I want to make… I want to… I want to make sure that you… did you, when you wrote this, or thought of this, did you have a design on how we would… Adapt this or evolve this to include sampling of log events?
**Vishwan aranha** 20:53 I did have it, like, I thought it was, like, about a month ago, so from what I recall, yes, I did have… like, everything in mind, like, how we would go around. Like, I have a sketch for logs in, like, a different ticket.
Okay.
**Jason Plumb** 21:09 Is it one of these? That's it.
**Vishwan aranha** 21:12 970, yes, 970. So, but not a finalized API. The idea is, like, for trace sampler and a log filter to use, like, the same session decision, with logs filtered before buffering using their, like, original session ID. So, metrics, would, like, still need separate design work. I haven't settled how to expose all of that in the DSL, so I'd welcome input on, like, keeping this Configuration, like, easy to extend, so we could, like, update it later on without affecting anything.
**Hanson Ho** 21:43 Did we resolve Jamie's question about precedence? Or are we saying now session is the first one that we apply, and everything else comes after?
**Jason Plumb** 21:55 Precedence for sampling order?
**Hanson Ho** 21:57 Yeah, so is session the first one we do, and then everything goes after, or is that configurable? Like, I think it's reasonable to say you do a session one, that takes the first cut, and then everything else is applied after that. But that should be documented and codified, and not just left to the reader, because it goes first, or something like that.
**Cesar Munoz** 22:18 My understanding is that we decided to go with Jamie's Proposal. To make… to make this config Like, leave outside of the session object.
Now… The… the thing about… Talking about sampling sessions right now, is that… It will essentially be alive, because we can only trace sample traces.
Right now. So… so, in order to… I guess, keep the existing functionality, and yet provide something within the DSL.
One option was that the… the… this DSL that would be outside of the session object.
will only allow you to provide a sampler for traces.
Bye now.
**Jason Plumb** 23:13 Which is, I think, what's being proposed for this PR.
Not in this current state, but I think Vishwan intends to adapt this to cover the trace sampling case for the DSL. Is that true?
**Vishwan aranha** 23:26 Yes.
**Jason Plumb** 23:27 Okay.
And I don't think the configuration the… I still don't think it does speak to the, ordering thing. I think we should get consensus on that.
**Hanson Ho** 23:38 I mean, it does if we literally say, this is gonna go first, and nothing… everything goes after. Right. But if we don't want that, then we need a way to specify it and make it clear. So that's the one thing I think we need to clarify before locking in.
**Jason Plumb** 23:53 Jamie, do you have an opinion on that?
Did you did you feel strongly about that?
**Jamie Lynch (Palo Alto Networks)** 23:58 I don't have strong opinions, I just think… Yeah, we should make sure that there is a precedence and it's documented.
**Jason Plumb** 24:07 Okay. I I think I agree, and I think it seems fairly safe to have the session sampling go first.
**Hanson Ho** 24:18 Yeah, if session sampling, or the way session sampling should work going forward, doesn't go first, the data is going to be very messed up and impossible to analyze, because you're going to get basically broken sessions.
Or missing data within a session because it was sampled up prior to the session sampling decision being made.
**Cesar Munoz** 24:40 Yeah.
Now, the reason why I… Also, like Jamie's proposal is that If it stays as is, as it is right now.
As it is in the PR.
I think it's confusing, because again, as I was mentioning earlier.
The way it looks like right now is that you will set a sample for the whole session, but in reality, what you'll get is a sample for traces.
**Jason Plumb** 25:14 Yeah, but we don't need to fix them both of the… you're right. I mean, you're totally right, but I don't know that we need to fix them at the same time.
I think we can take what's… so it's always been that if you opted into using session-based sampling, you only sampled Traces, it spans. We can expand that, though, to include all signals.
But I don't know that we need to wrap that up in the DSL change. Like, I don't think those have to come at the same time.
As long as it doesn't make the DSL confusing, which it might be for a window, but I think…
**Cesar Munoz** 25:48 it.
**Jason Plumb** 25:48 You're worried about that window.
**Cesar Munoz** 25:50 So, okay, so let me, so let me… I think it's fine. I just want to try to recap.
because we're we're we're talking about a lot, a lot of stuff.
**Jason Plumb** 26:01 It's true.
**Cesar Munoz** 26:02 At the beginning, we were talking that maybe some users would like to sample stuff.
For other reasons other than session.
And because of that, then a… Brother, I guess.
higher level sampler.
DSL will make more sense.
And this rather higher-level sampler could also take care of sessions.
So… It sounds like now we decided to flip it back.
And so does that mean that The only way that we want to provide sampling.
Configurations is if it's tied to the session.
**Jason Plumb** 26:51 I don't think they… I don't… I say no.
**Cesar Munoz** 26:54 Got it.
**Jason Plumb** 26:54 I think there needs to be other ways as well to sample.
**Cesar Munoz** 26:59 And where does that leave then the current PR from Vishwan?
**Jason Plumb** 27:05 So the… It doesn't.
**Vishwan aranha** 27:07 Go ahead. Yeah, so to answer your question, no, as well, like, the proposal is still, like, a general trace sampler option outside session. The users could, like, supply any trace sampler. Like, session-based sampling would just be one implementation. What we are deferring is, like, extending the session sampling to logs and other signals, from what I understood.
Correct me if I'm wrong.
**Jason Plumb** 27:31 I think you're correct, and I don't know that it needs to be in the same PR.
**Vishwan aranha** 27:35 Yeah.
**Cesar Munoz** 27:35 So for this pr, maybe we can go with what you have there, Jason, but only with the trace part. Yeah.
**Jason Plumb** 27:43 Just the trace part. Yeah, yeah, I think so.
**Cesar Munoz** 27:46 Yeah, I just wanted to…
**Jason Plumb** 27:47 Because this sampler is a trace sampler. Yes, I agree.
**Cesar Munoz** 27:52 Okay.
Okay, nice. Yeah, I just wanted to.
**Jason Plumb** 27:54 So this would be, like, a future edition.
Yeah.
**Cesar Munoz** 28:01 Cool. Thank you.
**Jason Plumb** 28:03 Okay, I'm just gonna… I'm just gonna comment this, like, some notes from… laughs.
**Vishwan aranha** 28:08 Yeah.
I can also add, like, discussion notes later, and see what we settle with, and so everybody's, like, aware of the changes that we discussed.
**Jason Plumb** 28:22 Sounds.
**Cesar Munoz** 28:23 you.
**Jason Plumb** 28:23 Yeah.
Oh, this heater is so hot.
**Vishwan aranha** 28:27 For 970, like, it kind of generally flows, so I will just bring that up. I mentioned it there, but the next question is, like, where the session, where the, like, shared session decision should live, so both trace sampling and, like, log filtering can use it.
The third ticket, 970, I'll link that.
**Jason Plumb** 28:50 Yeah, I think I have that one open, yeah.
So, yeah, the question is, where does that live?
**Vishwan aranha** 29:01 Yeah.
So, we want to make sure, like, both the trace sampler and the log filtering can use it, so we want to think about that.
**Jason Plumb** 29:19 Right, so the… The session ID-based sampler today… When, I mean, the API design for sampling in traces in OpenTelemetry is such that every span you have to ask, is this span sampled, right? Like, should you sample this?
That's the API, essentially. And the implementation of our existing… our existing implementation just doesn't look at the span, it looks at the session, right? That's… that's the design, if I'm explaining it okay.
So this about… about, like, deciding for every log or span, like, the OpenTelemetry design for spans… Like, the decision does have to be made for every span as it's being created.
But it doesn't necessarily use the contents of the span in that decision. It uses the current session.
**Vishwan aranha** 30:12 Yeah, and I think the trace API itself, like, asks for spam, but this implementation bases its decision on the session. So, the piece, I'd like, like, logs to reuse is that session-level decision without trying, like, logs to trace the sampling API itself.
**Cesar Munoz** 30:32 There's just one thing with the tracer sampler that we are reusing OpenTelemetry Java sampler.
API, and there's no API that we can reuse here for logs.
Which is fine. We can probably create a similar one to the traces sampler.
**Jason Plumb** 30:47 We said log… we said log processor, right?
That's what I think Vishwan said log processor.
**Cesar Munoz** 30:54 Yeah, yeah, that's an option.
**Jason Plumb** 30:57 And then you implement, instead of like on emit passing it to a batch processor or whatever, you just… You make a sampling decision, and then you either pass it on or you don't.
That sounds right. Yeah.
**Vishwan aranha** 31:12 Yeah, and that's right, like.
I think the log process is where we would, like, apply the filtering. The shared piece could be, like, a decision lookup by session ID, with, which, like, both the processor and the trace sampler consult.
**Jason Plumb** 31:26 Yeah, so it needs to be… so I think… I think you've identified, like, an API, even if it's an internal API that's missing, and it's some sort of, like, session-based predicate. Right? That's what we're talking about, is, like, a predicate that's session-aware.
That's what a sampling decision, a session-based sampling decision basically looks like.
I think.
And I don't.
**Cesar Munoz** 31:48 We have it.
The one that we have for, for traces right now.
**Jason Plumb** 31:54 Yeah.
**Cesar Munoz** 31:54 It's an implementation of the upstream sampler. Correct. And of course, the upstream sampler, it's a very basic API, so it's not aware of sessions.
So maybe, if we want… these configurations from the DSL.
to allocate to… to allow for not session-related sampling stuff, then probably the base API should not be aware of sessions. And then we can create a… An implementation that does know about sessions.
which essentially will make us have the same thing as we do with traces right now.
That'll be my opinion on it.
**Jason Plumb** 32:45 I think we're saying kind of the same thing.
**Cesar Munoz** 32:50 Right, but the base API should be kind of dumb.
**Vishwan aranha** 32:53 So, I believe that… I believe the base CP, it can, like, stay generic, like, with session-aware behavior in an implementation. And I think that implementation could, like, share the session predicate with the trace sampler, so callers wouldn't have, like, to use the session-based sampling.
And I, yeah, if… that's what's your point as well, right, Cesar?
**Cesar Munoz** 33:16 Yeah.
**Vishwan aranha** 33:17 Yeah.
**Jason Plumb** 33:24 Yeah, so the existing implementation just piggybacks on like some existing history that exists in probably in the spec too, but there's an implementation in Java. So we didn't reinvent it. We just use the existing upstream trace ID ratio based.
But this predicate that we're talking about could certainly just wrap that.
Right, because we're using that, and instead of passing in the span ID, we're passing in… I think the way… if I remember, the way this works is instead of passing in the span ID, we're passing in the session ID.
Right, so that's… that's basically what in… for… for traces, this, this predicate, this hypothetical new internal API, which is like a session predicate, one implementation of which could just wrap this, right? It could do exactly this, and then this sampler could evolve to use that predicate.
And that predicate would then also be used, reused, the same instance even could be reused by the logging.
Oh.
processor.
**Cesar Munoz** 34:29 Yeah, I mean, like, in a way so that we can… So that we don't have to reinvent the wheel.
**Jason Plumb** 34:34 Exactly.
**Cesar Munoz** 34:34 Yeah.
That would make sense.
I mean, if it's possible, that would be nice, yeah.
**Jason Plumb** 34:39 Okay.
**Vishwan aranha** 34:40 That's exactly, yeah.
**Jason Plumb** 34:41 Okay.
Cool.
And, okay, so was there any more to talk about on this one?
I think we skipped over it.
**Vishwan aranha** 34:53 Yes, for 2087, yeah, this… I wonder when, It was added, like, just one case for the… Let me see, like, let me log into it.
I forgot about this one that I added to.
So this one was, like, I added this as.
as, like, a continued session-based work for how we would, like, approach, like, the restart linking process. Like, can we… I think, it was brought, like, if we can add, like, a small previous session hook for.
For the, for the, for the first, like, decision?
for the first, like, start, start event, session start event, like, keeping persistence and, like, restart policy outside the SDK. And.
like, following, like, Cesar's feedback, I believe I tried, like, keeping storage and restart policy on the Grafana side. The gap is, like, passing the saved, like, previous session into the first session start event.
My question was, like, would a small optional startup hook make sense upstream, so we can, like.
start, like, a new session with, like, session previous ID pointing to the old one.
**Jason Plumb** 36:22 So the intent here is to be able to have, on a fresh launch.
Continuation, or at least not continuation, but an indication of what the prior session was on a fresh launch.
**Vishwan aranha** 36:35 Yeah.
**Jason Plumb** 36:37 Okay.
That seems fine to me. I mean, it seems… Do we want to default that?
It's definitely more complicated, it's more involved, I don't want to say complicated, it's more… There's more moving pieces.
**Vishwan aranha** 36:54 Yeah, it's like a new session with, like, previous ID included.
**Jason Plumb** 36:57 attribution.
**Vishwan aranha** 36:57 Who could, like, supply that context for the first session start event?
**Jason Plumb** 37:03 The question is, what would provide that?
**Vishwan aranha** 37:07 The hook that we add would provide that.
**Jason Plumb** 37:09 Yeah, yeah. I mean… This seems… I mean, that approach seems reasonable to me.
**Cesar Munoz** 37:18 Yeah, sounds good to me as well.
I haven't taken a look at this, I don't know how it will look like, but… Yeah. Enabling that sounds good.
**Vishwan aranha** 37:26 And the application would supply. Like, in our case, like, Grafana's startup code, like, would read the previous session from its own storage before, like, initializing the SDK, then pass that context through the hook. So, it would be, like, an opt-in, like, without it, like, existing startup behavior stays the same, so nothing is affected.
So, it's, like, gonna be the safest update.
**Cesar Munoz** 37:48 Sounds good.
**Jason Plumb** 37:48 I think the challenge is that the session is initialized so early in the agent or in the SDK that reading from a like blocking that startup and reading from anything in storage is always going to be contentious.
**Vishwan aranha** 38:03 Yeah.
**Jason Plumb** 38:06 So it's probably opt-in. I think we probably cannot get away with defaulting it.
to on…
**Vishwan aranha** 38:11 Yeah, that's why I'm, like, planning to keep it often, definitely, like, so it's… would not have any issues. Defaulting, it could have problems, but yeah, definitely… I mean, we'll…
**Jason Plumb** 38:23 We'll get people that raise the alarm on that just because of strict mode.
**Vishwan aranha** 38:30 And could the hook, like, accept, like, an already loaded value, so the SDK itself doesn't know, storage I.O?
the application would, like, still own the cost of, like, loading its… loading it, like, before initialization. If it isn't available in time, could we, like, proceed without the session, previous session link?
**Jason Plumb** 38:55 I'm not… I'm not entirely following you, so you're saying, what if we push the responsibility of loading from storage into application prior to initializing the SD… the agent?
**Vishwan aranha** 39:08 Basically, yes, so… .
I'm, like, thinking about it, like, as I go, like, would that make sense? Like, basically, the application would, like, load its own saved session and, like, pass that value as configuration.
**Jason Plumb** 39:24 I mean, that… yeah, if you need that, like, if an application wants that, that probably seems fine, but then we have to expose a hook for it. Like, we have to expose some API surface to provide that.
Prior session on… on startup, on creation.
**Vishwan aranha** 39:40 Yeah.
**Cesar Munoz** 39:41 the.
**Vishwan aranha** 39:42 make.
**Cesar Munoz** 39:42 I'm confused. Isn't that the same hook that we're talking about earlier?
**Jason Plumb** 39:54 I'm still on my first cup of coffee, but I don't.
**Vishwan aranha** 39:56 I don't…
**Jason Plumb** 39:56 I think we were, were we?
**Vishwan aranha** 39:58 The…
**Cesar Munoz** 39:59 We were talking about a hook that would provide the previous.
**Vishwan aranha** 40:01 Yes, it's gonna be the same hook. Like, I was just clarifying for this, like, that it would accept, like, an already loaded value, rather than have the SDK read storage. Like, I'm not proposing a second hook, for sure. Okay. That would be the thing.
**Jason Plumb** 40:15 Got it, got it. I think I didn't understand that. That's on me.
**Cesar Munoz** 40:22 Wow, I didn't understand it. I mean, I guess… It's just a bit difficult to visualize it, you know, without… An example of how it will look like.
as we had in the previous PR.
But,
**Vishwan aranha** 40:43 Did I add a diagram for it somewhere? I don't recall.
Thought I did.
**Jason Plumb** 40:51 Let's see. Oh, there is. Yeah, you're right.
**Vishwan aranha** 40:53 There it is, yeah.
these mermaid diagrams are easy to build. I don't like, Excalibur, that, Excalibur, sorry. It kind of, is hard, but mermaid diagrams are, like, easy, so it's… and GitHub… I'm glad that GitHub uses it, that's why I will try to add these more often, so it's easier to explain.
**Jason Plumb** 41:15 I also like Mermaid, I think it's great for this kind of stuff.
Alright, so this all is happening before we try and get to the OTEL SDK, so we do a little load if it's there, and then we initialize it with the previous session somehow. Like, this doesn't exist yet, but that's kind of what this PR is proposing.
**Vishwan aranha** 41:39 And.
**Jason Plumb** 41:40 then We always do this anyway, but then this event would now… like, the data inside of this session start event would also have the previous ID. Is that… the semantic conventions allow this, right? It's just a… it's just a session start event, and that has an optional previous ID, right?
**Vishwan aranha** 41:59 Yes, exactly, like, the SDK creates, like, session B, and the supplied session A becomes, like, the previous ID on that first event. Like, that's the focused hook-only change I'm, like, proposing here.
**Jason Plumb** 42:14 Seems fine to me.
**Cesar Munoz** 42:16 It sounds good. Just to confirm, when you say hook, you're talking about a…
**Jason Plumb** 42:21 It's an API.
**Cesar Munoz** 42:22 Right, but it's like, would be, like, a passive, so it would wait for, the SDK to call that.
**Vishwan aranha** 42:33 Yeah, like an optional, optional, like, configuration API for supplying the previous session context during initialization, so…
**Jason Plumb** 42:43 And what does it look like in this PR?
**Cesar Munoz** 42:44 But it would be like something that the… like a… like a method that the SDK will call on initialization, or would it be like a setter, you know? Where you set something… In memory, on a variable that's… this is the previous session.
**Vishwan aranha** 43:01 I think, let me check the draft API, so, yeah, I recall…
**Jason Plumb** 43:09 Is it this one?
**Vishwan aranha** 43:10 Let me see. Yes. Yes, that's the one.
**Cesar Munoz** 43:12 That sounds… seems like a flag.
**Jason Plumb** 43:15 I don't know what this does.
It's unclear to me what this is intended to do.
**Vishwan aranha** 43:21 So, there's, like, in the current draft, like, if you go… if you search for, like, link previous session on restart.
Yeah, yeah. So, it makes the SDK read the configured storage during initialization. The smaller API in the diagram is still, like, a proposal.
We could make that, we could make that, like, an accept and, like, already loaded value through configuration, rather than, like, call back the SDK involves, invokes, like, I should add, like, a concrete API example so the distinction is clear. That's on me, I did not add that.
**Jason Plumb** 43:55 I think that would have helped a little bit to this discussion, at least, but, you know, it's still a draft, so whatever. Yeah. So the intention is, you would set… you would, like, in the config block for the session, you would say.
Set link previous session on restart, which is like a bullet, like it's enabling that feature.
And then the implementation of how to go about that is opinionated and internal? Is that… is that how this is currently coded?
**Vishwan aranha** 44:20 Yeah, I believe so. In the current one, yes. So that…
**Jason Plumb** 44:24 Go ahead.
**Vishwan aranha** 44:25 Yeah, but I'm planning to, make some updates based on the proposal. This was, like, added a while ago for the… and as you mentioned, like, it works for the current draft. Yes, the flag makes, like, the SDK read the configured session storage, and link that saved, like, session to the first new one.
And.
**Jason Plumb** 44:46 But you want to move that out, and you want to maybe make that… You maybe want to pull that out of this PR. Yeah. Is what it sounds like.
**Vishwan aranha** 44:55 Yeah, and, as of now, like, I believe the caller can, like, supply the storage implementation and the smaller follow-up with, I'm planning, proposing, like, what we're discussing is, like, would instead let the caller pass the already loaded previous session value directly.
And, it would, like, make it simpler and easier.
**Cesar Munoz** 45:19 I like the idea of enabling this.
The, It's just that based on how it looks like it will be executed.
I mean, it seems like we're gonna have to introduce some flags.
And I usually, I… I usually try to avoid flags as much as possible, otherwise, you know, we'll be enabling, disabling, enabling, disabling a lot of stuff.
Benny.
If it's the only way, or if it's the easiest, that's fine.
But the way I see it is that if… maybe I'm misunderstanding, please let me know. And probably we can discuss it further in the PR once it's not a draft.
But if…
**Vishwan aranha** 46:05 evolved.
**Cesar Munoz** 46:06 If all we need is some way to allow… the SDK to get the previous session, if there was any.
To me, it would sound like adding a getter for a previous session.
in some existing API, you know? It would be, like, the storage, for example.
I think right now has one getter that returns the current session. Id.
Maybe we can add a second one that returns the previous session ID and defaults to null.
And to me, that will… that will… That would probably solve.
Like, a lot, really, without having to introduce Flags and stuff.
I don't know if that would work. I don't have the context, but just… Pointing it out to… as a way to a simpler, you know, Blacklist.
**Vishwan aranha** 46:59 I think that could work, too. The requirement is, like, to capture the previous session before initialization overwrites it, then use it, like, for the first session event.
Getter, I think, could, like, return an already cached value, so I wouldn't… so it wouldn't, like, have… to perform, like, the disk I.O, I can explore that shape and, like, add, like, a concrete example to the PR, but for the smaller API, my idea was, like.
I have a question, like, could supplying the previous session value itself be opt-in? Like, if it's, like, omitted, like, startup behaves as it does today, that could avoid the separate enable flag, and that would make it easier, but I can, look into your approach to Cesar.
**Cesar Munoz** 47:44 Thank you.
**Jason Plumb** 47:48 Just to recap, so I understand what Cesar's suggesting, it's to expand or change the session storage API to be able to provide both the current session and the previous session.
And then the.
**Cesar Munoz** 48:01 Yeah.
**Jason Plumb** 48:02 And the implementation of which would then… You could swap the implementation with one that is file storage aware to be able to snarf the prior session.
**Cesar Munoz** 48:13 Yeah, it will be implementations.
**Jason Morris** 48:16 It has the added benefit of you become completely agnostic as to how many previous sessions there might be, and any complications around that as well.
If you've got a file storage that only ever deals with one session, obviously you need to read whatever was there to get that previous value before you overwrite it, but you might have, like, a queue or something like that, and it… Removes… separates you quite nicely from that.
**Jason Plumb** 48:46 I see what you're saying. Like like, if you had stored a history of every session or something, then you read the the last one. Yeah. It definitely abstracts that away, which is nice. Yeah.
It doesn't solve the read from file at startup problem because, yeah.
That's still gonna happen when that event is created. Okay.
Yeah, that feels pretty good to me. What do you think, Vishwan? Want to try that?
**Vishwan aranha** 49:12 Yeah, I'm gonna experiment with that and see how that works out, and if I find any edge cases or issues, I can just document it on the ticket and ask you guys for your suggestion.
The one thing I like that it, like, abstracts the storage policy, but, like, doesn't… by itself, I can remove the startup IO.
I'm thinking of making the retiming, like, explicit in the proposal, so… and, like, check how the cache previous session value would work.
like, before the current session gets overwritten, and I can, like, document everything and, like, probably provide a diagram, and maybe we can agree on that async and, like, go from there, if it works for you guys.
**Cesar Munoz** 49:51 Very good. Thank you, Vishwan.
**Jason Plumb** 49:53 Yeah, sounds sounds good.
**Vishwan aranha** 49:55 Thanks, guys.
And I hijacked most of the meeting with my session.
**Jason Plumb** 50:01 No, you're good. I mean, we had a light agenda. So, and I also did a pretty poor job of taking notes today. But, yeah, we can capture that in those PRs. Jamie, do you want to talk about PR stacks, which are enabled in Kotlin?
**Jamie Lynch (Palo Alto Networks)** 50:14 Yes.
So…
**Jason Plumb** 50:16 Hanson very excited about this.
**Jamie Lynch (Palo Alto Networks)** 50:19 Yeah, I figured… I should bring this up, because we've enabled it in Gotthen. I personally find them really useful.
particularly when there's, like, larger changes, like, I think, like, the session stuff we've been working on would probably be helpful. We could, like, stack the changes up and… Review them that way.
I think the way it works is we have to change some admin settings, and… then I think approvers and maintainers are able to create PR stacks.
So yeah, I'll just… Open the floor.
**Cesar Munoz** 51:01 It sounds good, and I've heard Hanson talk about this feature a while ago.
I never try, it's just… I don't know.
what it does. So, but essentially, is it, is it like I can create I guess I manually create… let's say, two PRs that are related.
And then I… I have to point.
One to, like, the second one to the first one speed, branch, and then the first one will be pointed to main.
**Jason Plumb** 51:35 Yep.
**Cesar Munoz** 51:36 And then… Which is something that I can do right now, so I'm trying to see what enabling this does.
So, I guess if I merge the.
The second one? The last one first?
Then, I was gonna see if there was.
**Jason Plumb** 51:59 Do you have any existing stacks in Kotlin right now?
**Jamie Lynch (Palo Alto Networks)** 52:01 Yeah, there's adding the API for creating context key. That's part of it.
**Jason Plumb** 52:06 Oh yeah, yes, you can see that you can see there's a stack icon right here.
**Cesar Munoz** 52:10 Oh, okay.
**Jason Plumb** 52:11 So you get this, like, cool UI experience, and it shows you what the stack looks like.
**Cesar Munoz** 52:16 Nice.
**Jason Plumb** 52:18 And so what happens, I think, in the GitHub UI is, I believe that when this gets merged, like, I don't… I don't think you can… can you merge these, like, in… yeah, so… it's unable to merge as a stack, but if you go to the first one.
Now that I've screwed it up.
**Cesar Munoz** 52:36 Oh, you can merge like them all at once, thanks to this. Okay, that's very cool.
**Jamie Lynch (Palo Alto Networks)** 52:41 You can choose to merge them independently as well.
**Cesar Munoz** 52:46 Got it. And if I have to update something.
on the first PR, I guess that automatically updates the second one.
When this issue is enabled?
**Jamie Lynch (Palo Alto Networks)** 52:56 Yeah, there's options to rebase it, and I think that works for the simple case, but otherwise you just have to go resolve the conflicts manually like you normally would.
**Hanson Ho** 53:09 It's very… the syncing mechanism's really nice. You're allowed to basically… if you don't have, you know, edge cases, you can just go sync repo, and it'll just sync down main and rebase your entire stack, so you don't have to, like, manually go there. And the UI breaks the changes down into separate PRs. If you have, like, 6 commits, and they kind of overlap, you can view them one by one, fix it in the correct PR, or rather correct stack, as a new commit, instead of having to, like, you know, redo everything, if you choose to. So, this is a reviewer's dream.
And it's also a… it helps you do a lot of the Git stuff that gets really annoying if you have large stacks that need to be rebased, because, the repo changes all the time, so I'm a big component… proponent of this.
**Cesar Munoz** 54:02 Sounds good. And actually, based on what Jason is showing right now, it's also nice to Have a single place where we can see all of the related.
PRs.
**Jason Plumb** 54:11 So, as a reviewer, do you kind of…
**Cesar Munoz** 54:12 striking.
**Jason Plumb** 54:13 Kind of start at the closest one to Maine and start reviewing up? Is that the idea? And then… Well, it's…
**Cesar Munoz** 54:21 Cool.
**Jason Plumb** 54:21 But they all have to be approved, right? Like, before you can merge the stack, is that right?
And no merge conflicts, obviously.
**Jamie Lynch (Palo Alto Networks)** 54:29 Yeah, if you wanted to merge an entire stack at once, that would be true. But if there's like a couple at the bottom that are approved, then you could like merge the bottom two, for instance.
**Jason Plumb** 54:40 Yeah.
Cool.
**Hanson Ho** 54:42 this.
**Jason Plumb** 54:43 So.
**Hanson Ho** 54:44 Oh.
**Jason Plumb** 54:45 I'm okay with enabling that. I think, I don't think there's really any harm in doing that.
Me, personally, I… I think a stack of, like, 6, I would already get lost around, like, the third one, and I would just be like, I'm gonna go do some other work while this… like, I'm just… it's too… I can't keep that context anymore, it's just, like, it's too much. But I love that people can do that, and that's a nice way of dividing what would normally be, like, a 3,000 line PR into, like.
More digestible units that are already created without pushing the entirety of the rebase burden to a developer who's, like, gonna lose interest. So, I think this is helpful.
**Vishwan aranha** 55:24 Maybe what would help is, like, what if we, add the title, like, 105, 205, 305?
**Jason Plumb** 55:30 yourself.
**Vishwan aranha** 55:31 contact.
**Hanson Ho** 55:31 It's automatic.
**Jason Plumb** 55:33 It could help, but you do get, like, these numbers here, but it's unclear, like, which stack they're maybe part of, right? Like, 4 of 6, but if there were, like, multiple.
**Vishwan aranha** 55:42 just.
**Jason Plumb** 55:42 You don't kind of know which one.
And that would be true of the title change as well, but that could… maybe that would help. I don't know.
**Vishwan aranha** 55:49 Some context around, like, one of… 5 session, replay or something like that, we can add, right?
**Jason Plumb** 55:55 When you're looking at an individual one, it's still pretty obvious, and you can get the stack here.
So, I don't know.
Maintainers, I say yes.
**Cesar Munoz** 56:05 I think Jamie liked it.
**Jason Plumb** 56:06 Cesar, you cool with it?
**Cesar Munoz** 56:08 Yeah, I hope we have the, I guess we have the right permissions to do those ourselves, but we'll have to call Trask. I don't know.
**Jason Plumb** 56:17 No, we just did this. No, we did it in Kotlin. So it's just a PR change into the admin repo.
**Cesar Munoz** 56:24 Got it.
**Jason Plumb** 56:24 Which only maintainers can see. Yeah, yeah. So it's cool. But for those that want to leverage this feature, just be aware, it doesn't work across forks, so what this means is when you're doing work, and you're pushing branches, you need to push those branches to create the stack. You have to push branches to… the repo, the OTEL repo.
And that's only allowed for maintainers and approvers, so that random people still can't push branches. You just have to be aware, it's a change in workflow. Like, for the last 5 years, I've only ever been pushing branches to my forks, and… It'll be a change. You'll have to push those branches, and they have to be named like this. The branch name has to have your prefix in it.
So, it's also a slight change in, like, how you name your things, but, like, I mean, it's kind of trivial to just do another branch creation before you push, right? So… Okay, cool.
**Hanson Ho** 57:20 For reviewers, think of the entire stack as one PR, and each of the component PRs as a diff on the, one commit. So you can comment like that. If you choose to review the entire thing as a whole thing, you can do that. Otherwise, you can just go one by one, and if it is a 3,000 line, if you do can't hold the context for that long, you can go step by step, and merge as they… as they're done. Or, you know, wait.
**Cesar Munoz** 57:49 Nice.
**Jason Plumb** 57:51 Jamie, you instigated. Do you want to take that as to do?
**Jamie Lynch (Palo Alto Networks)** 57:53 Yeah, I can… I can do that.
**Jason Plumb** 57:56 Awesome.
Just ping me on the admin repo if I don't see it or respond to it within a few hours.
Cool. We are… if we want to end 5 minutes before, we are nearly there, but I wanted to at least give a shout out and say hello to Rohan and Prasad, who may be joining us for the first time, and I apologize if I just don't remember you.
But I wanted to say hi, and thanks for joining, and welcome.
**Cesar Munoz** 58:24 Yes, welcome. I think already Rohan has also created a lot of PRs.
**Jason Plumb** 58:30 Cool.
**Cesar Munoz** 58:30 So thanks for that.
**Jason Plumb** 58:34 Yeah, sorry, this might even be the second time I'm doing this, I feel so bad, but…
**Ben Joseph** 58:38 can.
**Prasad Sawool** 58:41 Yeah, I'm joining for a piece of the job competition.
**Jason Plumb** 58:47 I… that was unintelligible for me, sorry.
**Prasad Sawool** 58:52 Yeah, I've previously joined the Java implementation personality.
**Jason Plumb** 58:57 Yeah, your audio is like… it sounds like you're talking to a pillow.
Muffled.
But I think you're saying something nice, so thanks.
**Ben Joseph** 59:09 I think he said he has previously joined Java SIG.
**Jason Plumb** 59:13 Oh, cool. Okay. Awesome.
**Ben Joseph** 59:16 Yeah.
**Jason Plumb** 59:17 Nice, well, welcome, yeah, appreciate you being here and helping out, it's awesome.
All right, well, I think we did it. Thanks, everyone.
**Vishwan aranha** 59:30 Thank you.
**Cesar Munoz** 59:32 I…
**Ben Joseph** 59:33 Thank you.
**Jason Plumb** 59:33 See you next time.
**Vishwan aranha** 59:34 Yes.
