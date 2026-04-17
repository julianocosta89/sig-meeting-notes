SIG: Browser SIG
Date: 2026-04-16
Duration: 87 minutes
============================================================

## Zoom Recording Transcript

**Hugo Levy** 00:51 Hello?
**Martin Kuba** 00:57 Bye, everyone.
**Jared Freeze** 01:04 Hello?
Welcome back, Martin.
**Martin Kuba** 01:14 Thanks.
**santosh** 01:26 Hi, Martin.
**Martin Kuba** 01:27 Hey, Santosh, how are you?
**santosh** 01:29 Hey, Britt, how are you?
**Martin Kuba** 01:31 Good.
It's good to have you join.
**santosh** 01:38 Yeah, I'm driving, so my other… my… I have a conflict usually, which is we got canceled today, so I thought I'll join this.
Yeah.
Maybe I'll ping you separately, I want to catch up with, you know, all the work that you guys have done, I want to explore how we can start testing what you guys have built.
**Martin Kuba** 02:04 Yeah, that'd be… that'd be great.
**santosh** 02:07 Yeah.
**Ted Young** 02:09 You should check out the demo that Joaquin put together.
**santosh** 02:15 Oh, I see. I see. Okay, yeah, sure.
Hey, Dad.
**Ted Young** 02:20 Like…
**Jared Freeze** 02:21 Yeah, and Maxine has another one coming.
Like, more of a dev environment, so… Yeah.
**Maxime Quentin** 02:29 Hey, everyone.
**Ted Young** 02:33 Hello.
**Martin Kuba** 02:44 Alright, we can get started. I have the first.
Thing on the agenda?
Let me share my screen really quick.
So, the topic that I want to talk about is, the resource timing, semantic conventions. So we… we just… merged recently, the resource timing, instrumentation, and it has its own set of semantic conventions, which is, I think, browser, resource.
I actually have a screenshot of that here.
So, like, this is… these are the attributes that we're currently… currently would be ascending. This hasn't been released yet, but that's what we have right now in… on the main branch.
There has been… A proposal… 2… to, define unified HTTP semantic conventions that would be used for… would be used for… could be used for this, and would basically align browser and mobile. So there's been a discussion on this for a while now, with, and basically the proposal is to… to have to use… reuse some existing conventions, and then introduce new ones, but in the HTTP namespace.
Rather than browser-specific. And I think we talked about this, you know, a few weeks ago, and, like, the next step was going to be to, actually try it out, what it would look like in the instrumentation.
So that's what I… I actually worked on that this week, and opened this draft PR to, to help us make a decision here.
So I would… I would like to, Yeah, I would like to make a decision soon, because I think there is, there is… this… this, issue has been open for a while, and also Hector, who was here last week.
I don't know, 2 weeks ago, I think. He has got a separate PR open in semantic conventions to introduce just… it's very similar to the thing that we… what we have right now.
So while I was working on this, There are a few things that… I mean, we knew this going in, but it just became obvious that there are just some ergonomic things that are non-intuitive, and so that's the main takeaways for me, were these things, that if you look at these, if you look at these two, these two screenshots compare what we have now and what this would become. So we have, first of all, instead of, you know, these basically map to all of the fields from the resource timing directly, so if I was looking as a browser web developer in the console or network.
You know, payloads, you know, it would be obvious to me to what these are.
Here is, like, the second screenshot here is the unified semantics.
And… some of them, you know, you can guess, some of them, maybe not so much, like, I think the, the request header start time, for example, that's, like, the… the response start would match to the response start. So, you know, like, you would… that's not obvious.
And then the other thing that would be different is… is that the… the values themselves Currently, the browser gives it to us as relative timestamps relative to time origin of the document. The proposal is to use Either absolute timestamps, or… Timestamps, relative to the start of the… of the… Request itself.
So you can see those differences here as well.
And also, the proposal was, if we went with relative timestamps, the first one, like, the start time would be the absolute timestamp, and then the rest would be relative, which to me is actually… doesn't look great, because if I was looking at this, and I saw that, like, the call start time is really a high number.
And time is a very small number, that doesn't seem intuitive, but… So, all that to say, like, I have this open, And I would like us to make a decision, So we don't keep, keep, circling on this.
Any questions for what I said so far?
**Hugo Levy** 07:58 I have a small question on this one.
So this is for instrumenting, browser, I mean, resource timings.
is… is it possible plan to have the… also, traces that would be generated from these, events at the same time? For example, if you have, like, front-end calls and then back-end calls at the… that are infering from… From this, request, for example.
And if so, would there be a trace ID, part of those events?
**Martin Kuba** 08:30 Zoom in, like, on the back-end generator span from these events.
**Hugo Levy** 08:34 For example, I don't know if it might be… Possible to do so later.
**Martin Kuba** 08:40 So it's… it's possible. There's… there's also a separate… separate instrumentation for… that generates spans, from… Patching the, the fetch and XHR APIs.
And those do… that's actually separate instrumentation from the events.
**Hugo Levy** 09:00 Okay, I was thinking of, linking them with a… maybe adding Trace ID inside this event, or… any… Any way to link, at some point, the back end, the front end?
**Martin Kuba** 09:13 Yeah, I think the existing instrumentation, if I'm correct, does… add the… does attempt to do the… to do this, and adds currently, The resource timing, attributes as… as… Events on the span itself.
So I think that could be updated, too.
tooling, yeah.
**Joaquín Díaz** 09:43 Do you know if the mobile side of this is also going to do this absolute start time? Like, using the start time as the absolute number for the duration, or… Is that something that you are proposing for web?
**Martin Kuba** 10:00 So I don't know what they're actually… what they're leaning to. I know that there was some… there was some questions from that group on that issue. Why aren't… why we are not using absolute timestamps.
And, I think the reason was coming from… from this group, from Browser, because we don't… we, You know, because the API does send relative, but I… yeah, I don't… I think they would probably, if I had to guess, I think they would probably prefer absolute timestamps.
**Joaquín Díaz** 10:37 Yeah, like, given that we are doing all this work, so we have the same naming convention, I think we should have the same roles on how these attributes are filled, because, like.
In the back end, if you want to see how this looks like, you shouldn't be… that you shouldn't have to think differently when you are looking at web resources versus, like.
Not a person's case.
**Martin Kuba** 11:04 Yeah. I mean, so, so I think, I think it already, like, it already comes down to if it's more… if you feel it's more important to have Like, cross-platform consistency.
Or, like, if, like, if we feel as a group here that it's more important to have browser, like, browser ergonomics better, like, make it more intuitive for… For our users.
**Joaquín Díaz** 11:33 My take on this is that if there is something you want to look at, and you want to compare, like, if you have a web and app.
Applications, and you want to compare things.
We are making it easier for that person trying to compare. If we use the same semantics.
So, I believe, like, everything that we can… Be on sync, or we should try to be on sync.
Except that, like, I think HTTP and all these things are easier. It's just a naming issue.
Other words, thanks.
I think we've had that discussion for UserClick and other stuff that… It's harder to meet in the middle, because, like, everything is so different, like, what we get on web and what you get on mobile.
But, like, resources, you fetch resources from everywhere, so I think in this case, I would agree on being consistent.
But I can see how we can not do that, and other things that are… That are, like, we have to work really hard to meet in the middle and have, like, the same conventions.
But to me, this looks fine. It's just a matter of getting used to the names.
**Martin Kuba** 12:52 Okay.
Does anyone have any other thoughts?
**Jared Freeze** 13:04 Yeah, I mean, when you say… when you say it's a little easier, like, it's intuitive for people, I mean, this is exactly the sort of thing that… will be obscured. Like, this is the problem for us, but, like, it shouldn't be for anyone else, so… I… that's, like, I'm putting my vote towards, shared as well, be… you know. And also, I was just actually just looking at the server timing spec. Server timing spec doesn't include any timestamps, so… They're not in sync, like, the server and the client, like, almost are never in sync, just based on, like.
regions and all sorts of other things. So, yeah, time origin, and then… Yeah, I don't know, I guess I don't have an opinion on the timestamp and time origin yet. We have to figure that out. But, I know with back-forward cache, there was an issue where… actually pulling time origin. It's not always what you think it's gonna be.
So we can figure that out, but yeah, as far as Unified, I think it makes a lot of sense.
**Ted Young** 14:08 I think if we go with the Delta, you know, just the small knit, I would say is maybe add that into the name or something if we can. I know that's modifying it, but… I think that's, like, the one gotcha. If we say start time and end time, and end time's a delta… And the only place you know that is in the notes.
That's a little confusing, but I want to see it in the name.
**Maxime Quentin** 14:31 Yeah, I agree.
We should have, like, relatives somewhere, but then we don't match with the… the browser API, and .
**Ted Young** 14:40 So…
**Maxime Quentin** 14:41 Yeah, so…
**Martin Kuba** 14:44 So just… just to be clear, like, the end times right now, like, they're not deltas from the start time. They're… they're, they're deltas from… from, like.
the time… either the time origin of the document, if you were matching the web's web API, Or… or they would be from the beginning of the request.
Which is… which is also, like, basically how the… how the web API works. It doesn't have durations in there. I mean, the… the other… The other option is, like, what you mentioned, Jared, in the past, is that we could just calculate the durations that we think are useful, instead of sending the raw data.
**Jared Freeze** 15:31 Well, yeah, I mean, I put that forward because we already have timestamp, on… The, on the log itself.
An observed timestamp. So, if you set timestamp and then have durations, it's less data.
I don't know if that's really a priority. I mean, reporting, like, the raw sort of data, like the from-time origin, I think is also useful. It really comes down to, like, how much math do we want to do on the SDK, or do we leave it up to the back end?
In our SDK, we actually do both right now, because, you know, it was sort of like, let's figure it out, but I don't know if anyone has strong opinions on that either. I know that file size is sort of an issue, like, network size, generally.
Until we have compr- like, real compression, since there isn't any right now in, in OTEL natively.
So that… that was… that was, like, another thought, but… Longer discussion, I think.
**Martin Kuba** 16:30 Okay.
Alright, so it sounds like we're leaning towards the unified semantics.
In which case, I would ask this group to take a look at this PR.
And specifically on the open questions, I think there are some things that would need to be resolved, and then we would need to update the, Our instrumentation, which hasn't been released yet, but if you want to do it really soon, we should address these things.
So please, take a look at it.
Alright, I've taken quite a bit of time on this.
Maxime, you have the next topics.
**Maxime Quentin** 17:19 Yeah, it would be very quick. It's just, like, I've noticed that the formatting of the event names are different. If you check, like, browser navigation timings, and browser resource timing, one is using underscore, and the other is using a dot.
And I think even in your previous PR, You add, like, two examples with, one using underscore for resource timing, and the other with a dot.
What is the standard, and can we make sure we kind of stick to one of the two?
Or is it, like, a way of having a namespace with different, event names? Like, you know that you have browser.resource and a lot of Event names, or…
**Martin Kuba** 18:12 I think… I think in this case, I think it's, probably a mistake, and we should… we should, be consistent in both.
My proposal would be to change the resource timing to match navigation timing.
**Maxime Quentin** 18:25 Okay, so…
**Jared Freeze** 18:27 Oh, sorry, go ahead.
**Maxime Quentin** 18:29 No, no, I was just saying that, makes sense to me.
**Jared Freeze** 18:34 I have two questions. Is there… any sort of commitment we want to make to having, like, just 3 keys? Like, just 3 parts, or something like that? Or are we allowed… like, could there be 10? Not that we want that, but is there… is there any sort of direction there? Does that matter?
**Ted Young** 18:58 I think we've favored generally trying to be as flat as possible.
To assume that, you know, if someone's turning these into dictionaries or whatnot.
It tends to be better to not have deeply nested stuff.
**Jared Freeze** 19:15 Okay.
So, I think, like, for the ones, you know, we've been sort of making up, like, you know.
on our side. We've tried to stick to, like, 3, and made it sort of intuitive. So, like, browser.resource underscore timing dot whatever. I could also see the case for, like, browser.timing.
Whatever else you've got going on.
I don't know if we need to do that, but I mean, that's, like, how namespaces normally work, where they sort of, like, stair-step down.
I guess I… I like the underscore here. I think that would be my vote.
Keep it simple.
**Maxime Quentin** 19:54 Yeah, I mean, if it's an event name, I don't think we will have nested event name or stuff like that, so maybe rather.resource underscore timing makes sense.
Yeah, so that was just my, my question.
And, second point, yeah, the issue about, how we track, URL.fool and the location of, all the events in the instrumentation is still open. So if, We have a bit of time to review it, or maybe, like, during the next semantic, conventions, Ask if we should go, like, with a browser-specific, like, namespace where we can bring everything we need, or do we want to push for a document?
Do we have more insights than last time, or do we… are we still, like, waiting for some… semantic… Like, feedbacks.
**Jared Freeze** 21:05 Yeah, I forgot to write back here, but, our mobile team did not care.
**Maxime Quentin** 21:10 Okay, cool.
**Jared Freeze** 21:12 So, they don't have either one, so they're like, whatever, you know, you guys… Use what makes the most sense.
**Maxime Quentin** 21:22 So should I… can I open my PR again on… using, like, a… Brazel.url.co.
**Martin Kuba** 21:30 My proposal is just to… Yeah, yeah.
But… I think browser documents.
**Maxime Quentin** 21:41 browser.document.url.full.
Perfect.
Yeah, that's what it is, so… I'll, open my…
**Jared Freeze** 21:55 Yeah, so Martin, in that world, would it be, like, Browser.worker.url.full.
Is that something you would… Consider.
**Maxime Quentin** 22:09 Ozone…
**Martin Kuba** 22:12 Does Worker have its own URL?
**Maxime Quentin** 22:15 Or iframe.iframe.document.
Beautiful.
I don't know.
**Jared Freeze** 22:24 I'm just curious if that document portion would be swapped in and out for something else.
Bye.
**Martin Kuba** 22:31 I mean, I'll get to the.
**Jared Freeze** 22:31 Yeah, I would reopen it.
**Martin Kuba** 22:33 Yeah, yeah, I think it would make sense if there was some other… entity that had a URL as well.
Yeah, I mean, this is experimental. I think this… I mean, if there's, like, no strong argument against this, I would say let's just go with this.
I think it fits, like, the semantics, like, in the web API, and… Jesus.
**Maxime Quentin** 23:08 Could I work on a smaller instrumentation to propagate this, like, the browser location, to populate the browser.document.uril.fool, or is it something… That makes no sense.
Like, a browser location, instrumentation, or that we could register, and… We just, like… Populate the, the field.
**Martin Kuba** 23:40 So I think this is something that's… Kind of similar to… to… to session… session ID, from my perspective, like, it's… it's, kind of like an entity in… That's… Or, like, a context for all the events, or all the events and spans generated from the SDK.
**Maxime Quentin** 24:05 Yeah.
**Martin Kuba** 24:07 And… Like, we don't have anything like that yet, like, we don't have any instrumentation or any, like, mechanism, like, to generate those things yet. But part of the, the demo that we've been working on.
I think one of the goals of the demo was to prototype something like that, some kind of mechanism that would You know, how they would generate these entities and resource attributes.
So I think… My suggestion as a first step would be to… to prototype it in the demo, as a part of the demo.
**Maxime Quentin** 24:45 Yeah, so I could do that. I could, like, have some kind of custom attribute that would work as an entity, and that would be added to any event or spans.
In the set box, and then… Reiterate.
**Martin Kuba** 25:01 Yeah.
**Maxime Quentin** 25:02 If that works well. I'll, I'll take notes of that and work on it.
**Jared Freeze** 25:07 Can I make this more complicated? So, there's a URL when something starts, and there's a URL potentially when it ends. It's kind of like timestamp and observe timestamp.
Do we care? Does anyone have a use case?
like, we've already seen this, right, with SPAs, where something will cross a boundary.
Long, long-running task, or something like that.
is it sort of always at the start? I mean, that's the intuitive thing for, like, most things, but I do think there are times when you want to know you know.
I don't know, you might be able to work it out with, like, durations and things, but you won't ever really have that URL. I think deriving that would be really, really difficult.
So, something to consider. I don't know if that matters to anyone.
**Maxime Quentin** 25:57 Yeah, that's a good point. I think we could start with, like, you generate the event, you get the browser allocation, and you tag it to the field, and… Indeed, we might… we might need another… Field later to kind of reflect if you change your location while, generating the… the event.
I'll look at it. Maybe the demo will be a good place to showcase this issue.
**Martin Kuba** 26:32 I think the same issue would apply to sessions, right?
Yep.
Okay, any other… Topics?
**Jared Freeze** 26:54 Do you want to do a release after we fix the dot to underscore in resource timing?
**Martin Kuba** 27:02 So my… I guess my question is, like, Do we want to release?
with… before we… With the semantic convention, with the semantics, like.
Now, they are not unified in the resource timing.
**Jared Freeze** 27:16 Probably not. I mean, it's market experimental, but I also don't want to make it hard on people for, like, 2 weeks or something. So, yeah, okay, yeah, that's…
**Martin Kuba** 27:24 So let's make that change and release, maybe later.
**Jared Freeze** 27:27 Sure.
**Martin Kuba** 27:30 Alright?
Thanks, everyone.
I'll see you later.
**Jared Freeze** 27:34 Dear.
