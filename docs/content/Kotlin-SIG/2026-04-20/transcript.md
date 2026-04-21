SIG: Kotlin SIG
Date: 2026-04-20
Duration: 37 minutes
============================================================

## Zoom Recording Transcript

**Jason Plumb** 00:36 Boy.
**Hanson** 00:37 Hello!
**Jason Plumb** 00:39 You are very loud.
**Hanson** 00:41 Oh, shit, I turned it.
**Jason Plumb** 00:43 No, it's on my end.
I was in a meeting with quiet coworkers, so I had it cranked.
**Hanson** 00:51 The ones that would describe me as quiet, so… Ugh.
Hey, Jamie.
**Jamie Lynch** 01:00 Hey, how's it going?
**Hanson** 01:03 Not bad, it's, gonna be 20 degrees today, so, welcome to summer!
For, I guess, the Pacific Northwest. I don't know what it's like in Manchester, but…
**Jamie Lynch** 01:13 Getting close to Spring.
So, maybe, like, about 14 degrees. So, pretty good, all in all.
**Hanson** 01:21 Yeah, we skipped past that 14, I think. We're at, like, single digits, and then suddenly, hey, how about shorts?
**Jason Plumb** 01:35 Yeah, it's gonna be 22 here today.
**Hanson** 01:39 Welcome back, to work, I guess, too, Jason. You were out for,
**Jason Plumb** 01:43 Yeah, I've been on the clock for an hour and a half, it's… yeah.
I have a lot of catching up to do, let's say.
I did a very good job of not looking at work. Like, I left my laptop at home, and I checked my phone a few times, but then I was like, no, no, like, anytime there's anything pressing, I'm just like, no! I pushed it away, and I did a really good job, actually, so… Now I'm screwed.
**Jamie Lynch** 02:07 Good.
**Hanson** 02:09 You know what? I figured… You would have to deal with it.
whenever you came back, so it's almost like, pick your poison. If you feel like stretching it out, that's got downsides. If you like just spending a day catching up, that's got downsides, too.
**Jason Plumb** 02:26 Yep, yep.
**Jamie Lynch** 02:32 Cool. Yeah, feel free to add additional topics to the agenda. I guess we can just… Kind of go through the map.
So, first thing I wanted to discuss was protection… branch protection on the release branch. So, we added some… Settings on the admin repo, but… added branch protection to a release branch, and the CI workflow… For preparing for releases failing as a consequence of that.
Basically, I think OTOBOT is no longer authorized to push branches.
So… I figured there's a few ways around that. The way I tried to solve it is I've opened a PRMB admin, that will… Basically, copy what OpenTelemetry Android is doing, as we're using the same workflows there.
I'm hopeful that should just resolve the issue.
**Jason Plumb** 03:42 Can you link to that PR?
Well, it's the admin repo, so it really doesn't help. I think.
**Jamie Lynch** 03:50 Do you want me to link on there, or…
**Jason Plumb** 03:53 Yeah, if you don't mind, because I can review it, I can merge that.
Yeah, sorry about that. I hadn't… hadn't considered it. I was, like, way more focused on getting those security alerts taken care of, and…
**Jamie Lynch** 04:05 Hmm.
**Jason Plumb** 04:06 Sorry that I broke the build.
**Jamie Lynch** 04:14 I didn't think of it at all during the view either.
**Jason Plumb** 04:17 Oh, yeah.
**Jamie Lynch** 04:18 I'll just send it to you via DM, just because… I guess. Okay.
**Jason Plumb** 04:23 Cool.
Yeah.
**Jamie Lynch** 04:27 Sorry, I just… Link.
**Jason Plumb** 04:31 Well, you sent me a link to the repo, you didn't send me a link to the PR.
**Jamie Lynch** 04:35 Yep, that's a real one.
**Jason Plumb** 04:37 What is it?
**Jamie Lynch** 04:39 Okay, so natural.
I also have Monday rain.
Cool.
**Jason Plumb** 04:49 Yeah, so you're switching to rule sets, that's good, because I think, in general, we want to be using rule sets, and when I sat down to do this, I was like, I don't know how these work, it's too complicated, but basically just, like, cribbing from Android seems like the best approach, so that's great. Cool.
I will get that approved.
**Jamie Lynch** 05:09 Awesome.
**Jason Plumb** 05:10 So we didn't go ahead with a release.
**Jamie Lynch** 05:15 No, we haven't, so… assuming that all works okay, I can carry on trying to do that release workflow.
**Jason Plumb** 05:23 Cool.
Okay, I will look at doing that this morning.
**Jamie Lynch** 05:33 Thanks.
Cool, next item… We got a bug report.
So… I think this was… relatively… straightforward to fix, basically the protobuf export, Seems to… not do too well when an attribute has an integer value instead of a long, it basically frozen unsupported operation exception. So… I think.
be… fix to that is basically going to be altering this code to support ints as well.
I think this user was also looking… A few other things, so again…
**Jason Plumb** 06:27 Sorry, Jamie, was this on the way into Protobuff, or on the way out of Protobuff? Is it on the way into Protobuff?
**Jamie Lynch** 06:35 Does that…
**Jason Plumb** 06:37 Cluster makes sense.
**Jamie Lynch** 06:38 Take a look at Burst Stack Trace. So…
**Jason Plumb** 06:42 It's on the protobuf, a spand-gated on protoconverters, yeah.
**Hanson** 06:47 Hmm…
**Jason Plumb** 06:50 Oh, so the… it's… I guess, does it matter that it's an array type? Probably not.
I guess what I'm getting at is, is it possible for there to be attributes on our span, before it hits protobufs, that are of type int?
**Jamie Lynch** 07:09 No, I don't think so.
**Jason Plumb** 07:11 Okay.
**Jamie Lynch** 07:11 But I think somewhere along the way, it's getting interpreted as an int.
**Jason Plumb** 07:18 Okay, cause the… the, the statement that you showed where we could handle int, my hunch, or my instinct, is that that might be too late, that maybe we should be converting it to long earlier in the API.
**Jamie Lynch** 07:32 Hmm.
**Jason Plumb** 07:34 But that's just… Just a passing thought.
I mean, preventing the crash is the most important thing.
**Jamie Lynch** 07:44 True, yeah.
**Hanson** 07:45 is INTA supported attribute type?
**Jason Plumb** 07:48 It's not… I don't think so. I think it's just long and double.
**Hanson** 07:54 So, if OTLP doesn't even have ints.
how did we get to this place? Are we… are we… are folks putting any into, into the attribute map, and then we're converting that too late?
**Jason Plumb** 08:11 I think that's what's probably happening.
**Hanson** 08:15 So how does…
**Jason Plumb** 08:16 Using any, or if we're always going through any.
**Hanson** 08:21 Yeah, so, I mean, we need any for complex attributes.
But… Into a primitive, so it's almost like we need to cast all primitives To something that we understand, and then… Catch, other types that we don't… No, it… So I guess there's two things we have to do here.
**Jason Plumb** 08:47 Yeah, Jamie, can you show that code again that does the dispatch?
Yeah, so this is on…
**Jamie Lynch** 08:57 So…
**Jason Plumb** 08:57 Version side of things, right?
**Hanson** 09:00 So we throw, it's good.
**Jason Plumb** 09:02 exporter. So this is, like, way… so we've already got an any sitting in the attributes that is of type int.
That seems to be a bigger problem. I mean, that seems to be, like, the root… more of a root case, root cause, and I guess we just pass… we probably don't do any touching when we set the attributes, do we?
Can we look at the attributes implementation?
**Jamie Lynch** 09:28 Whoa.
Hmm.
What is it called?
**Hanson** 09:36 Mutable, yeah.
**Jason Plumb** 09:38 Yeah, I was hoping you would know it off the top of your head, because I didn't know it.
**Jamie Lynch** 09:42 That's the test, a piece model, actually.
**Hanson** 09:52 Yeah, how does that… how does complex attributes get resolved?
**Jason Plumb** 09:58 So all of these specific typed ones, like Boolean, long, string, all those are great, and then when you get down to any.
Where's that?
**Jamie Lynch** 10:08 So… I've got a feeling that what's going on here is the actual backing implementation is a map of string and any.
**Jason Plumb** 10:17 Hmm.
**Jamie Lynch** 10:18 And then I think we've got some extension functions that allow you to basically pass in a map, so… Perhaps.
folks aren't actually… all of the folks, in this instance, aren't using, like, these APIs.
They're using, the extension.
Bitch.
Yeah.
Would allow you to pass in a map.
**Jason Plumb** 10:45 But there's the dispatch again right there, right? So that's where we could be doing the conversion.
Right, we're walking these attributes and… coercing them, so INT is falling into… Wouldn't it be… wouldn't an int in there fall into that else?
**Hanson** 11:02 Yeah?
**Jamie Lynch** 11:03 Yeah, and then maybe when we… Further along, if we've read that back.
And tried to pinch up to…
**Hanson** 11:14 We would… we would interpret that as a string.
like…
**Jamie Lynch** 11:19 Hmm.
**Hanson** 11:20 Like, here, unless it's a collection, or an array.
But then we go in there, and we also deal with that explicitly.
Or we drop it.
**Jason Plumb** 11:32 But if we change, like, line 20 to be, like, isLong or isInt, Right? Then that kind of… That's… that's the moment at which we coerce an int into a long, and then it's a long.
And it's fine, right?
**Hanson** 11:46 Sure.
**Jason Plumb** 11:47 And I guess we have to probably do something similar in the other method there.
**Hanson** 11:52 Do we want to do that for double floats as well? .
**Jason Plumb** 11:56 Probably… Okay, does that… is that worth making a note of in the issue?
**Jamie Lynch** 12:04 Yeah, I will… I don't know, Herman added to the issue. So… What, dude.
And…
**Hanson** 12:17 So how are complex types serialized?
Because, right, like, that code will set anything it doesn't recognize into a string.
But we want… we want… That to be… I don't know, some protobuf? Like, you know, if I have, like, my Foo type, which is a complex… How does that work? How does Java do it?
**Jamie Lynch** 12:49 In the Kotlin repo, at least, I'm pretty sure we don't support complex attributes other than we let you set a string.
**Hanson** 12:58 Okay.
**Jamie Lynch** 12:58 And then you could contain, like, Jason, I guess.
**Jason Plumb** 13:04 But in the protobuffs, it, I think, is kind of geared at or intended to support, like, this, like, rich kind of object tree structure.
And I'm not sure if Java marshals it yet, but I think there's some… there was some guidance, like, a year ago.
about… using, like, a string format like JSON or something if you hadn't… if you didn't have, like, proper support for it. That's from memory.
But… I don't know what Java's doing today, I will try and find it right now.
**Hanson** 13:36 So, if we don't support complex attributes right now, then that's fine.
But then… then I think maybe the exporter should also be a bit more aggressive in… in… in casting. I mean, we clearly should fix the SDK side to make sure that whatever we write to the map is something that, theoretically, we should all support, but the exporter It makes sense to have types that it doesn't know, and then deal with it.
Because imagine if somebody had a different implementation of the SDK, then they would have to deal with it.
At the export level.
I guess what I'm trying to say is we need to fix it at both places.
**Jamie Lynch** 14:27 Yeah. I can also go away and ask.
How exactly they're, like, getting an int and this scenario, like, what?
like, how they're setting attributes, I think that would probably be helpful for the discussion.
**Hanson** 14:42 Yeah, because I feel like you've taken care of the cases there. There is an else branch that says, hey, everything else is a string.
Might be wrong, but, you know, it doesn't… it shouldn't throw.
There should be no ints in that map.
**Jamie Lynch** 14:57 Hmm.
**Jason Plumb** 15:02 if you go to the Java repo, I can tell you that what… I'm really confused by what's happening here, but there's two classes. There's something called the Attribute Key Value Stateless Marshaller, and there's the non… whatever, let's just look at the stateless marshaller. And then there's also the AnyValue Stateless Marshaller.
And those don't look like they handle any values very well, even though it's in the name.
Like, I'm sorry, it doesn't look like it handles complex attributes very well.
**Hanson** 15:33 Well, maybe it's not supported yet.
**Jason Plumb** 15:36 I think that might be the case.
**Hanson** 15:38 Okay.
**Jason Plumb** 15:38 But there's been a couple of implementations, like, over the last year, Let's see…
**Hanson** 15:46 Is it in experimental, or what do you call it, incubating, or something like that?
**Jason Plumb** 15:50 Might be.
**Hanson** 15:51 extended attributes.
Yeah, it must be a backing map, I guess. There's no other way.
**Jason Plumb** 16:04 No, there's… oh, man.
Okay, let's see what this is. I'm gonna add this to the… Pr is a doozy.
**Jamie Lynch** 16:24 Do you want me to open that up?
**Jason Plumb** 16:26 Yeah, you don't have to, but buried in there somewhere is gonna be an implementation.
Ben.
So this is, like, this is stabilizing it, so probably there's a lot of package… Packages being touched.
And… I think they've kind of done away with any value, and I think it's just value now? Yeah, exactly.
So there's, like…
**Jamie Lynch** 16:49 Any…
**Jason Plumb** 16:50 value type…
**Hanson** 16:55 I was just gonna code everything.
**Jason Plumb** 16:59 bytes.
And when was this? This was pretty recently? February, yeah.
Well, anyway, I don't think we have to dwell on that too much. I mean, let's… let's fix the… let's fix the immediate, like, ints long problem.
And to your point, Hanson, if we don't have full support for complex types out of the box.
I think it's, you know… Yeah. Fine. We should, we should… we need a path forward to build that, but otherwise, I think it's fine.
**Jamie Lynch** 17:59 Cool.
Okay… next.
topic. I was gonna offer the chance to talk about how we, like, stabilize either the logging or tracing API Next. Did anyone want to discuss, like, these two issues first, before we do that?
**Hanson** 18:22 Sure. Minus tasks.
But Carlos is probably longer, so… Hey, Carlos.
**Carlos Alberto Cortez** 18:30 Hey!
**Jamie Lynch** 18:35 Cool, do you want to go… go then, Hanson?
**Hanson** 18:37 Oh, okay. Oh, yeah, so, one implication of semantic conventions being in this repo is that, when we do a release, it'll pull in the latest semantic conventions, by definition. So, I guess it's been a few weeks since we've done that, which, which is, which is fine, like, I just had a quick look, and, That's fine. Nothing to be discussed. It's just… it's just, hey.
like, I think in other repos, like, when the core one was released, they released a new one. This is just gonna be, like, part of everything, so… Yeah, I don't even know what I put it there.
**Jamie Lynch** 19:19 Yeah, I think we do have a open issue on whether we should host semantic conventions in another repo, Hi, Phil.
For now, it's probably okay just staying in this one.
**Hanson** 19:33 Yeah, I agree.
**Jamie Lynch** 19:39 Cool.
**Hanson** 19:40 I'll type up a summary of…
**Jamie Lynch** 19:44 Thanks.
Coloss, do you want to connect?
**Carlos Alberto Cortez** 19:50 Yeah, so yeah, basically, I don't know if you are actually following the Java… the JavaScript channel in Slack, but I was asking, maintainers there.
And Jack, yeah, basically said that, when it comes to the OpenTelemetry, the simpleton object, you know, which they use for the agent, but they don't recommend for… for any other use case, he said, his recommendation is that we don't add it for now, and that's something that exists in specification, and that's why a lot of things like the Python one have it, but it… it doesn't come for free. There are some initialization issues that have to be protected, you know, etc.
So, in that regard, I think we are safe by not adding it for now.
It can be added later. Awesome.
**Jason Plumb** 20:41 That's good news, I think.
**Hanson** 20:43 Later or never, right?
**Carlos Alberto Cortez** 20:47 Right, correct, correct, correct, exactly. On that front, however, I just want to remind you, that, the recommendation from the maintainers at the seat is that we still put the no-op implementation in the API, because otherwise it's gonna be, like, going against what other 6 do, so it's, like, of uniformity.
And one of the specific cases, which I very briefly mentioned last week, is what, like, like, you need to special case, like, for example, I don't know, actually, how many insta- like, libraries, like, Android libraries.
will, in the future, support out-of-the-box instrumentation, you know? But for them, it's like, it's… they actually have to call some no-op by default.
And in this case, it's very simple, if they just rely on the API, you know, which already has this. So this could be something useful, yeah.
Yeah.
**Jason Plumb** 21:43 When we… sorry to jump in, when we talked about the no-op, like, a couple of weeks ago, there was a little bit of pushback, and the intention was to sort of force… the application builder to decide at build time which implementation they were using or something? Like, I forget what the pushback was. Yeah. Is that it?
**Hanson** 21:59 Yeah, and they're generally instrumentation… you can't just drop a jar in the class path and have it, you know, instrument things. You have to include it in a build.
So there is intention. So instrumentation that is designed for Kotlin, won't necessarily need to pick up its, you know, default implementation. It will be provided at… construction time, or something like that, an implementation. And if that's the case, then the app or the library using the instrumentation, will be responsible for providing that, rather than having, you know, the SDK, or the instrumentation itself say, hey, if, you know, if no one is providing an instrumentation, I will use, you know, the one that comes with the API.
So, if the goal is to not force instrumentation writers to include anything other than the API modules. I think this is done. I don't think we need to say there has to be an implementation there in order for things to work. And I think this is even more, kind of… like, I think one thing we didn't answer here is, the, the, propagating, the, the baggage and context propagation stuff, that lives in the NOAP implementation in Java and other places, and whether or not That is… is… is… Actually, no, let's forget about that, let's just… let's talk about this first. Instrumentation writers don't have to provide, an implementation.
**Jason Plumb** 23:34 They should code only to the API.
**Hanson** 23:36 Yeah.
**Jamie Lynch** 23:36 Yep.
**Carlos Alberto Cortez** 23:38 Yeah, probably we can discuss more when that time comes. So two things. Bagash and Context have, in theory, to provide, like, full implementations as part of the API.
Tracer provider, logger provider, meter, whatever, all those things, they don't have to come at all, like… Yeah.
**Jamie Lynch** 24:01 Do you know why that's, the case? Sorry.
**Carlos Alberto Cortez** 24:09 What was that, sorry, again?
**Jamie Lynch** 24:10 Do you know why that is? I'd just be interested to know why context and baggage are different compared to all the other APIs.
**Carlos Alberto Cortez** 24:19 So, context is something that we said that we don't want every SDK to re-implement that, so we wanted to provide out-of-the-box implementation for that.
Baggage is the same. With baggage, it's like, it's simple enough, it's straightforward.
there's no need, like, even less on context to have, like, different implementations, and that's why we're adding it there. And it's kind of related to the previous point, like.
If you are, like, having an instrumentation, you can use, like, even if you're doing no op operations, like, let's say, for logger providers, you are actually doing nothing, you might still want to do propagation, you know? So, basically, no log record or expans are created ever, if you're using an op, but the actual propagation is happening, so that will cover context and bugs, you know?
**Jamie Lynch** 25:16 Hmm.
**Hanson** 25:25 I'm trying to understand that use case, whether or not… especially if at Kotlin we don't have a… A default context to propagate.
**Carlos Alberto Cortez** 25:36 Yeah, actually, that's the other thing, that I am still looking into that. As you may remember, I was, you know.
trying to gather evidence, because, you know, there's also a specific use case, like, that we use the context from Java when we use Java on the, you know, on that side, but on Android, it's completely different.
So maybe we can postpone the decision for now. My impression also is that the TCA members, who may have to do a second review once we went to West Table.
they will probably prefer an op at the APA level, but we can always discuss that later on. And pro… I mean, this is just mostly an update on what has been happening. We don't have to go and cover all that. I think context, baggage.
Are things that have to be solved first.
And this is still on me on the context part, so yeah.
Or to provide more feedback soon.
**Jamie Lynch** 26:31 Cool. Thanks.
I guess… If there wasn't anything else on this specific topic, we can open up the floor for… Talking about… stabilizing APIs. So I think one of the things we discussed last week and the other week is that, APIs, but… Like, the logging API depends on, such as attributes and context needs, completing first before we can consider stabilizing the logging API.
So basically I've just created a few more milestones with… a couple of tickets, of what I think has already been mentioned.
as necessary to do that. So, if folks can think of more issues, Yeah, just… either add them to a milestone, or done them in the SIG documentation, in the SIG doc, and we can see if we can get them fitted in.
**Jason Plumb** 27:43 Cool, this looks good.
It's good to see these.
**Jamie Lynch** 27:50 Yeah, and I think that definitely… It feels like they're not exhaustive right now, in terms of the issues we're in there, but hopefully it's a good… Start for figuring out.
Well, all the remaining, like, Bits and pieces are.
**Hanson** 28:10 Yeah, these are more stabilization… milestones more than the… like, there is, Attributes API, there is a Resources API, and there is a API, it's just… we gotta check the checkbox to see if, it's, you know.
Done, done.
**Carlos Alberto Cortez** 28:29 Oh, by the way, I don't know if, sorry, I don't remember that from the top of my head, but the API, as part of the API, we should also provide propagators.
For trace, contacts, and baggage, out of the box.
**Jason Plumb** 28:45 You're saying it does need to?
**Carlos Alberto Cortez** 28:48 It has to, yeah.
**Jason Plumb** 28:48 Yeah, yeah.
**Hanson** 28:51 I think they're in the implementation right now, but if what you're saying is that it needs to be in the no-op API, or, say, the no-op implementation, then we should probably move it to… to that.
**Carlos Alberto Cortez** 29:05 No, I think APA is totally fine. I would rather keep them there. If they are there already, yeah.
And actually, I guess that my point was that I don't even remember whether there's a baggage propagator. I don't remember looking into that. So if there's one, that's great.
French context is still their one we need.
And then there are a bunch of others that are optional, good to have, but, you know, not required, so we can postpone them.
**Jamie Lynch** 29:34 Cool. That's good to know.
**Jason Plumb** 29:40 Yeah, I don't think we have a baggage propagator yet.
Do we?
**Jamie Lynch** 29:45 No.
**Jason Plumb** 29:46 Cool.
Do we have an issue for it?
**Jamie Lynch** 29:51 I think we do, I can check now, now that we have milestones.
**Jason Plumb** 29:59 Baggage API, yeah, and Compat.
Cool.
**Jamie Lynch** 30:09 Cool. Anything further that anyone wants to discuss?
**Jason Plumb** 30:14 So the short… just to confirm, the short-term, first kind of stabilizations that we're looking for then are likely to be attributes.
And… Propagators?
**Jamie Lynch** 30:30 Yeah, I think definitely attributes, that feels like a… easier target to get stabilized.
**Jason Plumb** 30:38 What about… what about resources?
Because the milestones are great, but I'm just trying to know what to focus on first. Who am I kidding?
**Hanson** 30:52 Yeah.
**Jason Plumb** 30:52 Focus, focus.
Focus.
It would be nice to have stated, or to be able to refer to something that says, like, what order we think we want to do these in.
**Jamie Lynch** 31:03 This is environmental variable configuration, which… It's kind of… Yeah, I feel like for Attributes API is probably the one that could…
**Jason Plumb** 31:14 Burst.
**Jamie Lynch** 31:15 gain most from us looking at, because I think There have been, like, different opinions on… like, what the API should look like for that, so… Yeah, we can get feedback for, yeah, it's outside of Invace, and, have lots of folks look at that.
**Jason Plumb** 31:34 Cool.
**Hanson** 31:36 Yeah, some of these are, like, we have implementation, we just need, like, somebody to look at it to see if it's correct, the API is correct. Some of these, we don't even have implementations, like the Popgator stuff.
So I feel like… I feel like, you know, getting… getting the ones where we have something to show is probably good, simply because that might take a little bit of… a while to kind of, you know, get the cycles going.
Attributes being first makes a lot of sense. Resources, we have an API, obviously, so that, I feel like… should also kind of… it's also pretty fundamental, so I think… Those two, we should definitely have.
outside input.
Sooner rather than later.
Well, actually, no, never mind. This is actually not the API, this is the… the issue in here is DTAC resources from the environment, so it's… Different.
Okay.
Nevermind.
**Jamie Lynch** 32:52 Yeah, it may be the case.
that, I need to go and create some, issues based off the spec for that milestone, so I can take a look at that.
I think.
Probably.
looking at the API and discussing that is also good, and I'm not sure that necessarily fits in a ticket.
**Hanson** 33:18 There's the checklist, right? And I think that's finally emerged.
where… the Kotlin SDK has a column?
We can go by… we can go by that, at least, as, as, you know… What do we need, like, checkmark?
you know, API signed off.
**Jamie Lynch** 33:46 Yeah, I feel like checking against the spec compliance matrix would probably be… A good step as well.
**Hanson** 34:00 But yeah, attributes number one. If we can get that going, that'd be good.
**Jamie Lynch** 34:09 Cool. Anything else?
**Hanson** 34:17 Maybe we should start thinking about this, we've got about 10 minutes, in May and June, is that Jamie? Or July as well? Your capacity's gonna be… Yeah. …a lot lower, so… Does anybody know that?
**Jamie Lynch** 34:36 Yeah, that's a good point, actually, I forgot to mention. But I'm going on paternity leave, At some point in my next… whoever knows how long. But yeah, I'll be off for about 6 weeks.
I may… may still be around, like, lurking, but I guess we'll see. I'll be a lot less contactable than normal.
**Carlos Alberto Cortez** 35:00 Yeah, probably you shouldn't be around. Just saying.
Gotcha.
**Jason Plumb** 35:05 Congrats, is this your first?
**Jamie Lynch** 35:07 Second.
**Jason Plumb** 35:08 Second, okay. Yeah. So you've been around this game before. Yeah, congrats, though, that's awesome.
**Jamie Lynch** 35:13 Yeah.
No, thanks.
**Hanson** 35:17 I think the, it'll be good to line up everything, you know, before that happens, so we can start doing, like, what Carlos is doing, so just getting feedback. And if we can't immediately, you know, make changes, at least we can create tickets to say, hey, these are the things that we need to do. And then, you know.
those of us, if we have time, we can start picking them up, individually, and see if we could, like, you know, once we have consensus, agree, hey, this is how we should do it, and then go ahead and do that. And, like.
I don't think the momentum would be quite as strong in the next, little while, but I think we could still keep the ball rolling. And it's important to keep it rolling, however, however, reduced the velocity is, so…
**Jason Plumb** 36:05 Yeah, yep.
**Jamie Lynch** 36:07 I think we also may have another contributor from Embrace, joining around that time, so hopefully that'll help a bit with momentum.
**Carlos Alberto Cortez** 36:16 Yeah.
**Hanson** 36:17 Definitely.
**Carlos Alberto Cortez** 36:17 And that's what I want to say, that you may remember that there were many people interested in helping the project, didn't work out in the end, but there's still hope that somebody may show up, and it would be great to have already tickets ready, so they know what things have to do.
**Jamie Lynch** 36:30 Yeah.
Yeah, I've created, quite a few issues on those milestones, but I can give it another pass.
**Jason Plumb** 36:39 There's no shortage of issues.
**Jamie Lynch** 36:41 And, we are starting to get PLs and issues through. Like, we had two issues from… Like, someone external to the SIGs today, and someone's writing a PR.
Which is currently in draft, so yeah.
Hopefully, it picks up.
**Jason Plumb** 37:02 Nice.
Well, this day is gonna require more coffee, so I'm gonna go do that.
**Jamie Lynch** 37:11 Awesome. Nice.
**Jason Plumb** 37:12 See, everyone. Bye. Take care.
**Hanson** 37:14 Thanks. Bye.
