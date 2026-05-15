SIG: Browser SIG
Date: 2026-05-14
Duration: 36 minutes
Zoom Recording URL: https://zoom.us/rec/share/hW8EVlO0QeQEVz4Q1nghGbwGFy0beEuivzFNOlyaBVD07wetH9NIuN_ExOikxxhf.rjph0rRQZ3HJCllT
============================================================

## Zoom Recording Transcript

**Jared Freeze** 02:11 Hey, what's up?
**Joaquín Díaz** 02:14 How's it going?
**Jared Freeze** 02:33 Give people a couple more minutes.
I'll pass the doc.
30 more seconds.
Sift.
vaccine, or… I don't see Ted's gir name.
**Martin Kuba** 03:32 Yeah, I'm not sure, he's been kind of off… on and off.
**Jared Freeze** 03:43 Okay, it doesn't look like anybody's really typing. You can get started.
So, David, do you want to talk about SDK?
**David Luna Bistuer** 03:55 Yeah, yeah, since, on last week, we were, talking about maybe… start, we did already some changes, and the plan is to have, kind of, is to have a new release, a major release on… by the end of June.
That's a target. It's not that we are going to force that, but that's the idea. One of the… major changes that we are going to do is traces, we want to consolidate the trace SDK into a single one.
So, it's, independent from the, from the runtime, the node, or, or browser.
And, yeah, we're just reviewing which APIs and which breaking changes we have to do, and I kind of, you know.
Find this discussion that was previously On a bot, designed to just remove for… Stop using, add events for response.
I know that there are other free instrumentations that are using the span events, like it's fetch, XHR, and DocumentLoad.
But, I came… I don't know, like, I thought that maybe it's an idea that maybe you can just, try to use correlation for logs, and then we can just, you know, get rid of the span. So, I just wanted to know your thoughts, and maybe I would propose to actually remove the At events, pretty good. So, SDK 3.0 will have this, these, APIs, so new instrumentations for browser will not use it.
**Joaquín Díaz** 05:39 Yeah. Sorry, answer there. I am… I just took that up, to do the actual migration. I wasn't planning on doing any, like, other breaking change other than just moving it.
But if we need to get rid of that, I guess this is the moment, like, since we are already doing a braking change anyways.
And if it makes sense to use loss and loss correlation, that sounds good to me.
**Jared Freeze** 06:12 D. Yeah.
Yeah. No, go ahead, go ahead.
**David Luna Bistuer** 06:16 The only drawback I see is, there was a comment on the… the core instrumentations are using this API, so it means that if you remove it.
Those instrumentations were not, update the SDK.
We kind of, you know, making them stop with the SDK 2.0 or 2.X.
And not being able to improve. I don't know if you want to… Just to do that, so, Browsers, people that are instrumenting browser apps, will move to.
our… the alternative instrumentations, which are going to use low correlation.
Hmm.
So, that's kind of my… my question here is, like, so we kind of, make sure that these instrumentations get stuck in 2.0, and, kind of way, forcing people to migrate to the new instrumentation that you're going to be using code block correlation.
Or, do we let users to use whatever they want?
**Jared Freeze** 07:23 I would say, so, Joaquin is bringing Fetch and XHR into browser repo.
Those are marked… everything is marked as experimental. I would say, like, let's just do our work against 2.0, and when it goes to 3.0, we'll just update those. The older ones that are still sitting in Core Repo will just stay whatever they've got, you know, if people find critical bugs or something, they get a patch pool or whatever, but, like, we'll just… I think we should just keep ours moving in… in here, because I think, you know, we don't want to hold work. I don't want, like, a bunch of branches for 3.0 or something, but… Yeah, Santosh, you have something?
**Santosh** 08:07 Yeah, just want to understand, this discussion. So… The title talks about Dropping the ad event.
And they add network span events, and that's still going to be an option, right? It's not… Gonna be a breaking change.
**David Luna Bistuer** 08:28 That's…
**Santosh** 08:28 considering the.
**David Luna Bistuer** 08:29 That's actually the question, so we should.
**Santosh** 08:32 We use it actively.
So, if… If it's, obviously, breaking change is not, acceptable, so as long as there is an option.
You know, to still keep the current behavior.
I think we would appreciate it.
But yeah, you could even default to… The log events, and then we would flip the flag as we use it.
**Jared Freeze** 08:58 Martin?
**Martin Kuba** 09:01 So, David, I saw that you commented on that issue that we have for migrating that package.
**David Luna Bistuer** 09:07 Yeah.
**Martin Kuba** 09:08 And I actually… I'm in favor of your proposal there.
I would, I think… I was a little bit concerned about moving the, these… the XHR and Fetch packages, because they're so widely used.
And I think we would want to move them to the new package.
So I think leaving them in JS as they are.
So that we don't break users, but then, like.
re-implement in the… in our new package?
With the functionality that we want it to be, which could be basically starting with… Out without the span… span events, and just using, blog events.
Instead, that sounds like a good approach to me. But I'm… And I also would be in favor of Since… since it's gonna be in the same package.
If he can try to figure out how to… how to make those two… that instrumentation work together with the resource timing.
instrumentation.
**David Luna Bistuer** 10:13 I'll… have an idea. I guess maybe next week you can… you can, well, during… maybe by the end of the week, at the beginning of the next week, you can have a… and have a PR already, so you can review it, and then we can discuss it in the next… on the next meeting.
**Martin Kuba** 10:28 Yeah.
**Jared Freeze** 10:29 I can add a little… I can add a little something here, too. we… I went to a W3C meeting yesterday, and we're actually gonna pitch Adding what we want.
to resource timing from Fetch, right? Because you can't get… request type, you can't get request body size, there's a bunch of stuff. So, directly adding it, I mean, nobody wants the monkey patch.
Like, nobody likes it, nobody wants to do it, it feels wrong, it is wrong. So, if we could move everything into resource timing, that'd be awesome. Also, it's buffered, so we can load late and look backwards, right? All these good things.
So… obviously, browsers don't move that quickly, but that could be really cool. So yes, I think this… putting these together, you know, I don't know necessarily that we need to change the name to, like, network or something.
Maybe eventually, but, yeah, I like the idea of putting those together, because right now we have, like, dock load and fetch and resource timing all sort of giving you the same kind of information.
Without being united, you know? It's like, you gotta sort through it yourself, so… I think that's really cool.
**Joaquín Díaz** 11:40 Yeah, there is one thing these instrumentation is not doing that we cannot do with the resource timing API, is that they are injecting, the tracing headers.
And so that… that is impossible on the resource timing API, and I think that Alice on WTC, you also.
Talked about, like, having some sort of hoop where you can change the headers of vocals.
That means we might need to keep multi-patching, at least for that.
Yeah, which is… I mean, we may have just different instrumentations, like, one is just… more like a sort of… processor, that instrumentation that adds the trace headers, and then the other one is just emitting span. Well, yeah, I don't know. Maybe it needs to be also there. I know. I think, That's why we keep… we will have to keep doing multi-patching.
At least for a while.
**Martin Kuba** 12:42 Yeah, I kind of… I kind of see, like, there are probably a few different use cases, depending on, like, what you… what you're interested in.
Okay, if you were, like, interested in, like, on just capturing information about all network traffic, I mean, and the resource timing, like, improving that would be better, like, I mean, if you… want to generate traces and connect to backend, your, like, client spans to the backend, obviously, you would need to monkey patch.
That thing's still, yeah.
**Joaquín Díaz** 13:08 At least you can… Disable monkey patching if you don't care about the use case, and you still get information?
**Martin Kuba** 13:16 Yeah.
**Joaquín Díaz** 13:17 Yeah, that sounds good.
David, I was working on, I think, the same thing that you were, so I'll ping you later, I'll… I can share a bunch with you. But again, I wasn't changing anything, I was just moving the instrumentation and cleaning up the code.
But we can talk later to see where… where your thoughts are, and yeah, if we want to do this… Like, yeah, I guess the question is still, like, on the first… The first package that will go out.
Do we still want to support span events as we do on the one on JS, or do we just go all in logs?
But we support both.
I mean, I… I don't think we are going to add new functionality, so anyone in span events can still use the old one, and then… we can use logs. I will be in favor of that, but I'm open to… to the op… I'm open to having support for both.
Anyways, so…
**David Luna Bistuer** 14:21 Okay, sure. Yeah, ping me, ping me, whenever you're ready, and we can discuss.
**Jared Freeze** 14:26 Yeah, just generally, I definitely like the idea of having the Trace API Like, just for… like, you're talking about… you know, taking the best parts of SDK Trace Web and bringing it in.
Right.
Is that… is that right, David?
**David Luna Bistuer** 14:45 Yeah, yeah, so that when you said, you create the spans, so… basically, the idea is just to make use of code lock correlation, so you create the span for the fetch request.
So you have the context, and then you have the, the propagation.
So you can have the fault rates from the front end to the back end, but also then use a mechanism to actually give the context, the right context to the lot.
But you get the resource timing, you get the event, you get all the information, but also you can collect if there is a context.
For that. So, if the resource was for… because of, I don't know, an image being loaded on the DOM, you'd get no context at all, but if it was the fetch request that actually was triggered and was… and has an expired for that.
Then, you get… you get the right context, and then you can attach this context to the log.
**Jared Freeze** 15:35 Cool.
Cool, I like that. Yeah, I think my personal opinion is that we should probably drop the span events.
For this… for this iteration.
Yeah, Martin?
**Martin Kuba** 15:47 Yeah, I think the same, Jared, and… I also wanted to clarify, like, when we say, like, that we, instead of… That we… we would generate log events instead that… We sh… we should try… use… reusing the existing log events that we have from the resource styling instrumentation. Not generating new ones.
Right, that's… that's the… that would be the ideal approach, yeah.
**Joaquín Díaz** 16:21 You mean generating, like, one… so we have the network span, that is going to stay, right? And then we will have one… resource timing log with all the, like, the timings, like, fetch, start, document, domain lookup, whatever, all those things, and just one log that is the entry that is correlated to the span, right?
**Martin Kuba** 16:45 That's what I want.
**David Luna Bistuer** 16:45 Exactly.
**Martin Kuba** 16:45 Yes. Yes.
**David Luna Bistuer** 16:47 Then it means that you need to have both instrumentations enabled.
if you only have resource timings, you don't get the resource timings without any context at all. Yeah. If you have only the fetch instrumentation.
and not the resource timing, you get the spam. You, you know, you're sending also the address parent and three state headers, but not… you're not getting the resource timing log.
If you have both, then you have both, you have the span, and you have the event, and also you have it then correlated.
**Joaquín Díaz** 17:16 That's crazy.
**David Luna Bistuer** 17:17 It's something, yeah, something that we can connect interpret my files and say, okay, this works with the, you know, if you have, I don't know, resource timing, if you have resource timing, if you have fetch enabled, then you get good correlation.
**Joaquín Díaz** 17:31 My concern there is, how do you share?
I mean, you need a reference to this one, but the fetch instrumentation is creating.
How do they connect to each other? Like, how do they know that one is creating a span and the other one knows that that span needs to be in the context?
**David Luna Bistuer** 17:48 Well, I'm using… the idea is just kind of using a similar mechanism on the summitation. The summitation is already… saving the context from how to saving the spans, and… and then there is, from the… from the performance observer API, just, you know, getting the entries, so… Yeah. Querying the entries, and then just matching, matching by URL and the… and the timings, matching, which is the, okay, that resource It correlates with its span, so then… Okay, I'm using a similar logic. We can discuss the logic later if you want details, when I have the PR.
**Joaquín Díaz** 18:24 Yeah, that's fine. The thing is, that works because it's the same instrumentation, so you can keep the reference in there. But if you want to have two instrumentations, one for visual timing, one for French, they need to talk to each other, and I think that's all the idea. So how… that's… that's what I'm asking, like… I think if we do one instrumentation, then it's fine. Everything works. But if you want to do two instrumentations, then they choose how to share the context with each other.
**David Luna Bistuer** 18:50 Yeah, it's… you need a third party, you need another component that actually is… Activating this, this shirt.
You know, to make sure that actually you are not, you know, stashing a lot more information and doesn't grow over time.
**Joaquín Díaz** 19:04 This is stupid.
**David Luna Bistuer** 19:06 That's annoying.
**Jared Freeze** 19:07 Unless resource timing is a feature of Fetch, in which case Fetch is not a great name for it.
**Joaquín Díaz** 19:14 Yeah, right.
**Jared Freeze** 19:15 I mean, that's the third… that's the third option, right? Is, like, if you're gonna make a connector, maybe you just mash them together.
I don't know. Have to think about it.
**Joaquín Díaz** 19:24 I think… Yeah, I would rather go with it.
Simple approach, one instrumentation, that's all.
And then you can turn off on whatever you need from there, but yeah. I don't think we… I don't think it's ideal to have, like, a third component matching them together, just because we don't want to… we don't want one instrumentation doing everything. I think, in this case, that's the easiest path.
**David Luna Bistuer** 19:55 Okay, well, we can discuss implementation details later, so I'll get it to PR, and… well, again, we can have the discussion first, and then I can just, you know.
create the PR when it's ready, and yeah, have the discussion there.
**Joaquín Díaz** 20:10 Sure.
**Jared Freeze** 20:11 Cool. Go ahead, Martin.
**Martin Kuba** 20:13 Yeah, just really quick about, about maintaining the, the existing instrumentations that we would leave in JS Core.
So David, you were saying that, Would we… would we want to deprecate those… Those, span events, or just leave them, and just, like… like, make them work with just the SDK 2.0?
**David Luna Bistuer** 20:37 Yeah, well, based on… sorry, sorry, go ahead.
**Martin Kuba** 20:40 Yeah, and I don't know, like, if there are any other, like, node instrumentations that generate span events, and that, you know, I don't know, like, what their plans… What the plans are for those.
That'd be…
**David Luna Bistuer** 20:52 I'll ask on the note sake. I think that the browser ones, at least in contrip and Core, they're the only ones that they're using in Spanish are the browser-related ones.
And also… by the comments of Santosh, I think that maybe… I'm not thinking about removing it right now, so I changed my mind. Maybe it's just a way of… maybe not deprecation, but a way of showing the devs that if you're using, or the implementers of instrumentations, if they're using Span Evans.
This for browser is discouraged.
Or at least, you know, it's not, the path we want to go. So, I need to figure out, oh.
You know, maybe just put it in the documentation, maybe just put something in the types that You know, that gives a nice warning to say, hey, if you're using a… if you're doing a project implementation, maybe just, you know.
Just call block correlation instead of span events.
Okay, so then we are not breaking anyone, people could continue working on that, and… That's it, Santosh.
**Santosh** 21:54 Yeah, I think one way to force people to stop using the old packages is to stop putting in any changes, including security fixes.
Any… anything and everything that, you know, we put effort into should go into the… into the new packages. Because only when… We build significant things.
you know.
differences in the functionality, you know, in the new packages, there is not going to be any motivation for people to move. So… Yeah, you could make those changes backward compatible and all.
But, I think the current instrumentations, you know, work fine.
For… for a majority of our use cases. It's just that… There is going to be an inertia to move.
to the new model. And one way I was thinking to force people, including, you know, myself and our organization.
Is to, you know, lure them into the benefits.
You know, that we are going to build into the new packages.
**David Luna Bistuer** 23:00 Yeah, makes sense.
Also, we need to highlight the benefit that if you're using the consolidated package, you have the benefits of, Of the bundler, so the bundle size, you control more than bundle sites, depending on the distributions you're adding.
And I won't have… Yeah, so… That is also so important to note.
**Santosh** 23:22 Yeah.
Yeah, that would be developer convenience, but I think product features-wise too, I think if we can showcase That, you know, there is more value than the new Mechanism brings in.
I think, that'll be… that'll help.
**Jared Freeze** 23:41 I think we went on file size right away, so it should be a pretty easy conversation to have, once the Traces API gets a lot smaller. So, no pressure, David.
**David Luna Bistuer** 23:52 Okay.
**Jared Freeze** 23:56 Okay, yeah, cool.
mine, I… I just posted a link for, a refactor of instrumentation base. I noticed… when I was working, on our SDK as a vendor, that the types for instrumentation base actually come from Node, because when you're working in the file system, it doesn't follow the browser key.
And it's not… we… there's no exports key, so it doesn't actually crawl. So the underscore enabled, all the things in it, the reason there's an override in it in the browser instrumentation is because that is sitting in the node instrumentation base. So this was some research into, like.
What does it look like if we use the instrumentation base from, like, the actual browser version?
And, you know, what does it afford us? You know, does it make things simpler to not have to do… You know… Rely on, like, this sort of racy thing of… when the managers load, you know, when the subclass, variables instantiate, like, all these things, like, because we've had… there's… there's notes in every single one that's like, hey, don't forget to use declare, because this will be null , the second you run super, right? And so, it was like, okay, how do we solve that, or what do we do, or whatever. I also just made A change to always be disabled.
That was more just to kind of test it out, see, you know, what we want to do, or whatever, because there is some overhead in just firing off all these, listeners, and setup code, and all these things, so… Having that be opt-in instead of opt-out, I thought, might be good. And I left two ways to do that, so one is to actually pass config enabled, and then there's also, like, an imperative, like.enable, which is already there, but nobody uses it, because nothing's disabled, right? So, anyways, just some ideas. This is not like, hey, can I get reviews so we can merge it? Because I don't know if it's the best idea, but… Something to look at.
Double sick.
**David Luna Bistuer** 26:19 No, I like the idea of having the explicit types and that in another So, both having these declarative things on the classes.
Or something like that, so yeah, I'll have a look.
**Jared Freeze** 26:36 Ted, do you have anything for us this week?
**Ted Young** 26:39 I just, you know, we're running short on time in this meeting, but, one thing I wanted to kind of reiterate, I know we've been having various discussions, but I wanted to, like, say it here around, like, the SDK spec and its relationship to the work we're trying to do in the browser.
You know, the more and more we look at this, you know, the farther away the browser environment is from any of the, like, assumptions that are kind of, like, baked into the spec. Context is, like, a really great example of this, right? Like, the spec really presumes context, and context propagation is, like, a fundamental primitive, but we don't really even have access to that.
Realistically.
So, I just wanna… find a way to more formally propose that, like, the browser SDK just kind of go its own way when it comes to implementing everything.
And as long as, like, we're careful to document our design decisions, you know, in our repo, so it's not like… we went our own way and just made a hairball that, you know, you can only understand by being a maintainer of it. As long as, like, those decisions are documented, I think that's, like, a fine alternative.
I feel like this group of people working on it is, like, really familiar with, like, the spec and open telemetry and the problem space and all of this stuff at this point, so I have a lot of faith in Ball.
to build something that, you know, integrates with the rest of OpenTelemetry in the way that it needs to around, like, the API and, like, the Node API, and things like that, and the data we're trying to emit, but that, like.
bit in the middle about how the SDK should work. It just seems like, even relative to the other clients we're trying to build, like, you know, in Kotlin and Swift, the browser environment is just so unique.
It just feels like that spec work is just kind of preventing us from… It's just making the design more challenging, and it doesn't really seem like it's helping, so… I'm curious what your thoughts are on that. We don't have a lot of time here, but I'm happy to support you all and kind of defend that decision if you feel like that's gonna really take the pressure off in terms of shipping something useful.
**Jared Freeze** 29:06 Yeah, I mean, I think that's already true, right? I mean, we've already deviated. I think one of the issues, probably, was calling it JS. Like, it's the same language, but it's not the same environment, so… I mean, browsers are absolutely hostile, so we have guards that, like, Node doesn't even think about.
You know? Like, you know, we don't have access to storage all the time, we don't, you know, whatever, it's like… Yeah, totally. So, it is different enough that also the spec to go with it, I think, is… yeah, that deviation, Yeah, I appreciate you saying that, for sure.
**Ted Young** 29:40 You can even see, where I… two things that kind of brought it to a head for me. One was, like, you know, starting to explore metrics. Some people, like, want metrics from the browser, but, like, what does that really mean? You know, what would it mean to be giving people a metrics API, but, like, you know, something effective under the hood that could do something good with it?
And it's… it's like another example of, like, well, if you're not worrying about what the spec says you should do, and just worry about, like, what would be… useful for people wanting to create metrics in the browser, you know? Should they be just emitted as events or something like that, but you have a metrics API, so it's clear what you're trying to do, you know? It's not clear what users exactly want there, but the goal should be to make something that's that's useful for people, but still at the other end of the road, you know, it's regular OTLP coming out the door.
So… that… that was one. The other was, like, the entity stuff we're looking at, where I was looking at Martin's latest, you know, prototype, and it felt like the entity SIG was kind of focused on solving, like, metrics, and, like, like, how do we deal with metrics?
In, like, the collector in other areas, so you end up with this four-entity pattern. And, like, that's maybe relevant for trying to deal with a metrics engine, but, like, it's overcomplicated if you're just trying to… You know, batch out events and spans.
With session IDs.
So that's just another place where… you know, that ongoing work in the entity SIG seems to be, like, focused on stuff that's different from what we're trying to ship here.
So, we could keep trying to work in the entity SIG, but, to a certain degree, it's like, well, as long as, like, the data is being put in the right place at the end of the day, what does it matter what we're doing under the hood here in the browser?
Again, documenting everything and, like, checking in with the rest of OpenTelemetry so we're not surprising people, but… It just feels like… We're trying to negotiate with these other groups, and they're trying to be helpful, but what we need is just so specialized that it's just… that's just kind of jamming things up.
**Jared Freeze** 32:00 Yeah, I like the… I like… that you mentioned, you know, there may be a metrics API, but then at the end of the day, it's just logs. Like, that's a good way to frame it, I think, is… I may have asked in the wrong thread, but I said, hey, you know.
what are the practical examples? Like, has anyone asked for metrics?
Maybe I'll ask it more generally, because I can't think of one, but somebody might, you know? I don't know if we just wait till someone asks, or, you know, we think about it deeply now, or whatever.
**Ted Young** 32:29 Yeah, I can see someone trying to be like, I want to count a thing here, why can't I just count it? Why do I have to, like, make an event and then make a thing somewhere else, you know, right? Like, if the user could use the API to Express intent, and then that means, like, we can have a processor under the hood that does that for them somewhere.
you know, I can see that being a nice experience, I could see why users would want that, but it wouldn't be a nice experience to give users, like, a footgun of, like, we implemented a metrics SDK that just, like.
Dumps things on the ground every time the browser reloads, or tries to do some crazy thing to… you know, hold state. Like, what does it mean to try to make a histogram, you know, in a browser page that loads and unloads in 5 seconds?
**Jared Freeze** 33:20 Yeah, yeah.
**Ted Young** 33:21 15.
So… Yeah, but I could also see, like, there being… it being nice to have a metrics API for people who are, like, I'm… I know what I'm trying to do, can I just express the intent?
**Jared Freeze** 33:36 Yeah, cool.
**Ted Young** 33:38 Yep.
Anyway.
I wanted to say that I can… I don't know what the practical next steps are there, but, you know, I'm just happy to work with you all to… To also work upstream and, you know, the, Help everyone know that that's what we're doing over here, and that it's okay.
**Joaquín Díaz** 34:01 Yeah, I'm trying to think all the times that we've encountered this case, where we said, this is the spec, but it doesn't make sense for the browser.
Like, I mean, your examples are really good, but I think we should start just at least having a list.
So we can, you know, go back to that, and once we have a few items on the list, we can actually, like, write something up and use that as some sort of… Document on why we went that way, and then, yeah, we should use it to make these decisions.
But I think we haven't been doing that. We've been just assuming that we cannot do it because of a spec, and just being hard on that.
Yeah. So yeah, we should start tracking that.
**Jared Freeze** 34:44 Yeah, good idea.
Okay, cool.
**Ted Young** 34:50 Well, good talk. It's good seeing y'all.
**Jared Freeze** 34:52 Alright, good to see everybody.
**Joaquín Díaz** 34:53 Right.
**David Luna Bistuer** 34:54 I…
