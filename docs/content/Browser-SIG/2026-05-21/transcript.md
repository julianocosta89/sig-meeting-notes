SIG: Browser SIG
Date: 2026-05-21
Duration: 30 minutes
Zoom Recording URL: https://zoom.us/rec/share/Et5Q6v2E1MlgzHMTSu3OJN3JTVcYeF2TtnXoIoFgpMKQupuhS0zzoRgAcngGN_5s.hsHdBsCSRH4XZ4n1
============================================================

## Zoom Recording Transcript

**Martin Kuba** 01:00 Hi, Jaron.
**Jared Freeze** 01:02 Hey, what's up?
**Martin Kuba** 01:05 Okay, how are you doing?
**Jared Freeze** 01:06 Good, good.
Booking for the dog.
**HL Hugo Levy** 01:29 Nope.
**Martin Kuba** 01:31 Hey there.
**Maxime Quentin** 02:06 Hello?
**Martin Kuba** 02:08 I'm the same part.
Okay, that'll let everyone.
Let's get started, I guess.
So I have, I have one, just, Thing that I wanted to bring up, if you haven't seen… So, I'm just gonna… I'm gonna share my screen.
So we had this, yeah, this PR from… From contributor, like, there's a… The quo… what they were trying to do is, and… This body to, like, all of these instrumentations, which is kind of like a… like a descriptor, like a user, like a human readable descriptor of what the event does, and I think, you know.
the… motivation here was that in Grafana specifically, like, that's… the message is used. Like, if you do, if you do queries, like, it's used as, like, the display message. Without it, like, you see nothing.
I was looking at the spec, and the spec does actually talk about this, surprisingly.
I opened… I opened an issue in semantic conventions, though. I'd like to ask about this specifically, because the spec here… Does say… this is for the system.
spec for… similar conventions for events. It says that events should not use body except for… to represent a string display message of the event.
I don't know if this means… That you can, or you should, so… I, I opened this, this issue here.
I mean, this… this sounds to me a lot like… Span… span name, to be honest.
And, like, if we… if you want… if you wanted to have those descriptions, then, I think that there should be defined semantic conventions, but I just wanted to get, you know, anyone's here.
Opinions about what you think about this.
**Jared Freeze** 05:30 My initial thought is, in the interest of File size? Network size?
I wouldn't necessarily default to a sentence for, like, every single log, Also, I think exception… like, one of those was an exception, right? Doesn't it already have a message field?
**Martin Kuba** 05:49 It does, yeah.
**Jared Freeze** 05:51 But yeah, I think my, again, general concern would be… Adding this.
Everywhere, all the time, when in fact, a lot of people are gonna say.
you know, hey, I just want to count. Like, I don't necessarily want all these repeating strings all the time.
**Martin Kuba** 06:18 Yeah, I don't know, like, if this is a real friction point.
For, for, for ingest, now, obviously, all the information is in the attributes, and backends can… generate these.
But you do have to do some extra work to do that, right? So…
**Jared Freeze** 06:39 What's the… what is the navigation string that got added?
It's like navigation colon type.
**Martin Kuba** 06:51 Yeah.
I mean… I mean, if he… if he did decide that we want this, that I… I'm not… I would not… probably accept these right away. I think I would propose them as part of semantic conventions for the event.
Right, we can… and then we can decide what they would be. I think my… my question is, do we want to have these at all?
**Jared Freeze** 07:18 I mean, these are… my other thought, sorry, real quick, is the body is supposed to be, like, the thing that you use whenever you're worried about high cardinality, and these… this is, like, there's only 3 of these, so I don't know if that affects it as well, but yeah, sorry to interrupt.
**Joaquín Díaz** 07:35 No, I… I guess, like, this is something that you can go around by… Looking at different attributes.
When you are, like, listing logs in Grafana, you can just make priority in some of this.
the event name, probably… More, like, enough to give you some context, and then some attribute.
Yeah, I think I would jerry on this one, like, We will be adding, like, all this… Strings, just so it's easier to read sometimes.
Yeah.
Not… I don't, like… I wouldn't say I'm totally opposed to adding them, but I will try to not add them, and again, I also agree with you, like, if we will add them, it needs to be something that we… have some consistency on, like, not just whatever string we Figure out that will make sense at this point when we're creating an instrumentation.
Yeah.
**Jared Freeze** 08:36 It does seem to kind of work against the many conventions too, right? Because, I mean, this is, like, rel… it's sort of structured, where it's, like, navigation colon. If you start trying to parse that, or somebody parses it and then it changes, there's… it's not really documented anywhere. Like, it's not an attribute, right? So…
**Martin Kuba** 08:54 It's not an attribute, no, and it's… It's… yeah, that's why I was… this kind of makes me think of… it's very similar to spam names.
You know, like, they… like, I don't think you would ever, like, be parsing actual data from… from the names, like, it's… it's the… all… it's there just for… just for the, for the display purposes. Convenience.
Right.
**Joaquín Díaz** 09:22 Yeah, but as fun names, like, you only have, like, a few names, right?
I think on one of these, they were adding I think the error message or something, was it?
I don't know, attribution type.
Yeah, so… these look like they're limited, so… maybe we can do or change the… well, in that case, how you have… Any.
But not that many.
I guess.
Maybe we can improve the event name to be… That does it, and they need to be… Like, static, or can it have some information about what we are reporting?
**Martin Kuba** 10:11 The event name?
Yes. I think the event name should be static.
**Joaquín Díaz** 10:18 Okay.
**Trent Mick** 10:19 The event name's part of the… set of… fields that is meant to define the schema for that event, right? So, you don't want to be throwing… interpolated data, but…
**Martin Kuba** 10:31 Correct.
**Joaquín Díaz** 10:32 Right, okay. In that case, yeah, I guess.
And that field would make sense to look at.
**Martin Kuba** 10:43 Okay.
Alright, well, that's… that's all I wanted to… I just wanted to bring this up and see. I guess if you have a… if you have any other thoughts, there is this, there's this issue that I opened in some other conventions, I might… I might… Join next week and bring this up as a topic there.
**Jared Freeze** 11:07 So, if they wanted guidance on, like, they… if… so if this, you know, person really wants this, they would just make a processor.
All the logs and generate their own strings, right?
**Martin Kuba** 11:17 That's right, yeah.
**Jared Freeze** 11:18 Okay.
**Martin Kuba** 11:19 That's… that's… yeah.
That's the other way to do it.
**Jared Freeze** 11:24 Okay, cool. I mean, if they really want it, maybe we just recommend that. So that way it's not, like, a dead end for whoever asks.
**Martin Kuba** 11:31 Yeah.
Okay, yeah, let's move on.
David, you have the next topic.
**David Luna Bistuer** 11:39 Yeah, that's me.
So, working on, so that PR that I just linked on the document, well, it's merged already. Basically was just, updating the semantic conventions for the process detector, but I noticed something that then, okay, it's aligned with the semantic conventions, if you can see.
The note that is pointed, it says that the… So it's about user agent. So, you have… we have this, resource activity which is user agent regional. It was changed, not long ago.
But it is a note that says that, you… you should set this value.
if the user agent data API is not available.
Okay.
So, well, I have my thoughts here, it's like, okay, so user-cent data is not baseline yet.
And also, I know that it's available on Chromium browsers, but not on Safari, which means that, okay, most desktop processors will report the… The, brands and… and platform.
But then, most of the mobiles, will… We'll report only the user isn't.
So, you want to… well, I don't know, maybe just for correlation or for aggregation of data.
For, your website being… browser.
available through mobile and desktop, maybe you want to do some of this kind of migration, so you have the same You have logs that have us in logs that they don't have it.
So, okay, my… I don't know, it's like, my, my, my… Kind of mixed feelings about, okay, should we… if this is not baseline, maybe you should have us in all ways or not.
I don't know, maybe it's just… I was wondering, maybe, how do you handle it on the backend?
But yeah, it's something that it's challenging in the way that you want to do some kind of aggregation across different device types.
Then you have this, the data that you cannot use a single field to Just to select, you know, So I wanted to know your thoughts, and maybe I don't know how you handle it, and… Maybe, I don't know, I don't know, it's like, I think, does it make sense that maybe just say that maybe it's better for now? Just use your agent?
Instead of having this kind of, Exclusive or… between browser brands and…
**Jared Freeze** 14:17 I like both. I do think, yeah, I mean, all… any backend record I've ever seen is the full user agent, because it's easy, and I think it's just part of the… like, normal request. So, you have an… you have an else here. I'm wondering if we should just pull it out and put it as a sibling to language, so it's always included?
And then the richer data is the newer API.
Or make it an option.
I kind of hate options, though, because then it's, like, leaves a lot of, like, inconsistency, like, across, like, whoever implemented it, so I would say include it all the time, just so you can match it up, because you can do exact string matches, like, on the backend.
Also, I don't think a lot of systems are using this new data because, again, it's not baseline, as you called out. So… The other thing, too, is because it's not baseline, means that it could change over time. So, like, the definition of mobile, like, I don't really know what that means.
Like, is it… does it mean touch? Does it mean small screen? Does it mean slow?
doesn't mean it has a radio, like, I don't really know what that is, so, like, having the full… you know, like, iPad or whatever, I think would be useful as well, which I don't think is here. I'll have to look at what platform is.
But I don't know if it just says iOS or not.
**David Luna Bistuer** 15:37 The description is just a single value about the OS, that it's, it's running on, so you get macOS or something similar.
Okay.
**Jared Freeze** 15:48 I see.
Yeah. Yeah, I mean, having something that's, like, not baseline or the standard, the current standard.
I would say I'd probably want both.
That's my take, especially because WebKit is, you know… Every… every device.
Yeah.
**David Luna Bistuer** 16:08 Should we… should we remove the node then from the semantic conventions and then, Does that make sense? Oh.
So the semantic convention says that, you know, it's like, the user agent should be added if this, if the API is not available.
I guess that the… this restrictions should be removed, and then…
**Jared Freeze** 16:29 I don't think they're equal, though. There's more information in the raw user agent than what is presented here, right?
**David Luna Bistuer** 16:37 And also, the user edition is the stable already?
In other words, they're still in development, so…
**Jared Freeze** 16:44 There's a link here.
**Martin Kuba** 16:46 Maybe we just change the recommendation in semantic conventions to say Should be sent, or… Always, always, instead of… Yeah.
**Trent Mick** 16:57 So I think that the language that I posted in chat is the language that's pushing the browser detector implementation to have that else in there, rather than just always including user agent.original. I think it'd be more useful to downstream handlers as I think you're agreeing, Jared, that if useragent.original is always provided, but… If we're gonna do that, we should consider updating the semconf here.
**Jared Freeze** 17:23 Yeah, I think the device is included, and I don't see device. And I do think that's… Important to some.
**Trent Mick** 17:30 Oh, and user agent original, right, so saying that… okay, it's… yeah.
the UA client hints is not providing a full replacement for all the data in there, so there's your argument for dropping that. Okay.
**Jared Freeze** 17:46 Which is sort of surprising now that I'm seeing it. I haven't dug into this before.
**Trent Mick** 17:53 The language here in SEMCOM is interesting, you're saying?
**Jared Freeze** 17:55 No, the fact that it doesn't explicitly include device name, if they have it.
Not… not the… some.
**Trent Mick** 18:03 Yeah, yeah, absolutely. Yeah, yeah, yeah.
**Martin Kuba** 18:06 I think there is also some data that you have to request specifically.
Like, you don't get it automatically, I think.
**Jared Freeze** 18:15 Oh, they do have it, it's just not… in MDN, it's called Model.
somehow it didn't make it into, what gets exported. So there you go.
**Trent Mick** 18:33 Oh, that's the model header field that you're looking at, at the… In the client hint spec?
**Jared Freeze** 18:38 Yeah, I think so.
Because it's a.
**Trent Mick** 18:42 I'm sure you ain't.
**Jared Freeze** 18:43 bubbles Boolean?
So… But yeah, I think as far as, like, browser support goes.
I would probably not have as an or. I think that's my vote.
**Trent Mick** 19:10 Okay, so it sounds like propose a semicolom change there, and then change browser detector implementation.
**David Luna Bistuer** 19:22 Yeah.
Thank you.
**Martin Kuba** 19:35 Alright, are there any other topics that anyone wants to bring up?
**Maxime Quentin** 19:40 I was wondering, Martin, if you had the chance to make progress on the entity subject.
In a sense that, you know, I worked on a small POC to start instrumenting browser URLs, but it's also against the long-term goal of having entities for that. So I was wondering if it was still worth for me to work on the processor approach, or should I just drop it and… Wait for entities, support, or how do you see that?
**Martin Kuba** 20:17 Yeah, I mean, that's a good topic for discussion. So I did open… I did open, like, a PRIC, I think, a couple weeks ago, that, that's in… not going into main, but that's going into the demo. I don't know if you've seen that, like, it's… it was, like.
**Maxime Quentin** 20:32 Yeah.
**Martin Kuba** 20:33 prototype of, adding sessions and the document URL.
And I was… I was wondering… If that… if everyone thinks that this is a good approach that we should, pursue.
that PR could be just merged into the, you know, prototype branch, that's fine. And then, like, if we agree on that approach, then I would say, we could… We could wait until the… I guess the question then for me is, like, how exactly… to implement it.
Like, I don't… I don't think it should be… should be an instrumentation.
Because it's not… it doesn't really… it's something that, like, applies to all instrumentations, it's not just, like… so I think… I think it probably would make sense, in my opinion, to have… to implement it as part of the SDK package.
That David's working on right now.
So I would, you know, I would… I think that we would wanna have that package first, and then add it to that.
**Maxime Quentin** 21:45 Yeah, makes sense. I mean, also, like, the antiquity approach, and it shouldn't be, like, some kind of instrumentation you turn on.
Should be, like, out of the box, and… But yeah, I think it makes total sense to have it as an entity and wait for, like, the food package and kind of bug it out of the box there.
**Martin Kuba** 22:07 Yeah, Yeah, like, did that, did you have a chance to look at the, the prototype that I… I don't know if… if I… I think I went through it last time real quick, but… Yeah, like, take a look at it again, and maybe, like, If it looks good to you, just approve it so we can… Put it into the prototype branch.
**Joaquín Díaz** 22:33 Yeah, like, I'm… I'm wondering now how that works, where that's the thing that sets, say, entity goals, like… It's not an instrumentation.
It's not a processor, because… well, maybe.
Like, it's not changing every logo, every span, it's just applying the entity to each one of them, like… Where do we… where do we see that happening?
I know you have that, or what's the name? SetEntity, I think, is a function, or something like that. So where are we calling that?
**Martin Kuba** 23:09 Yeah, I mean, it's like a… let me show my screen again.
So, so I, like… This mechanism… I don't think this mechanism is defined At this point, That's.
**Maxime Quentin** 23:38 I think I shared the… the link in… In Zoom.
**Martin Kuba** 23:44 Okay.
**Maxime Quentin** 23:45 Okay, I mean, that's its one.
**Martin Kuba** 23:49 Yeah, so, so this is kind of sketching out, like, the SDK package here, and then… This, this, like, this is the vlogger provider that manages, like, the resource behind the scenes.
But then I think, Joaquin, we were asking, like, how, like, which thing would be actually calling this for entity, right? Or this set entity.
It's… so, like, I think this… this was in… Let's see… Yeah, so this was happening, like, in… at the… like, at the place where the SDK was being initialized, like, there's, like, let's say, like, it's for the session, like, this… for sessions, like, we have this session manager class that's… right now lives in the webcommon package in CoreJS.
So that, like, when the session manager is initialized together with the SDK in the same place, and then, like, when it observes… detects that a new session was started, then, like, it has in this place, like, it has access to the logger provider and sets it here, so… for the document tracking, like, I don't… like, I just, like, created, like, this separate class, Document Tracker, for now.
this is not set in stone, I think. I think once, like, the entity… like, API, or is more fleshed out from the spec perspective, then I think we can replace this, like, with something… More standardized, but, you know, basically something like a class that just, like, detects this and calls this in the same place, yeah.
**Joaquín Díaz** 25:40 But that will only work for people using the, like, the SDK.
For someone who is not, that just, you know, has their own setup, Do we need to… Expose Session Manager, Document Tracker, however we call it, so then… so they can't use that, like, individually or manually.
Or we just let them manage the session and the team by themselves.
But it's not something that we only support for SDKs, pay for the browser SDK as a whole, or… Oh, do we want that to work?
**Martin Kuba** 26:18 Yeah, I mean, that's a good question. I don't know, like, if there's… if people will want to create their own SDKs.
**Joaquín Díaz** 26:26 I mean, I feel like this is a good feature, But I don't know if… if we cop… Some mechanism that is built into the… by the current semantic conventions, like, that's these kind of things. As I said, like.
it's not an instrumentation, and it doesn't quite fit the… I don't feel like it fits the processor.
Like, entity, so I, I.
**Martin Kuba** 27:00 Yeah.
I don't know, I don't have… I don't have the answer. Like, I… I was… I was just, like.
I mean, this whole thing is gonna be experimental, right? It's gonna be evolving, so I think… you know.
Yeah, it'd be nice if, like… and we're… even, like, with this approach of, like, this entity-aware logger providers, or these providers that have… they can manage entities, like, that's not gonna be in the spec, so… you know, like, I don't know, I think I wanna just get to a point, like, where we… where we generate, like, the right data that we… the thing, like, as Ted was describing last time.
Yeah. And then, like, we figure out, you know, how to actually, if you… if you need to, like, standardize the SDK in a way that, like… or, like, these… all these, like, all these components so that other people can compose them in a way that they want.
That's, like, it seems to me like a, like, more long-term topic.
**Joaquín Díaz** 27:58 Yes, definitely.
**Maxime Quentin** 28:00 Yes.
**Joaquín Díaz** 28:01 That makes sense to me, like, we can figure it out once we know the data is worth it.
**Maxime Quentin** 28:06 On my side, I think it's a very good, like, use case to, like, showcase what is an entity.
So, even if the implementation, today it's a document tracker, tomorrow it's something else, but it will really help advocate for the concept and how it is leveraged, why we're using entities and not something else.
So, I'm… I think it's a good initiative, and we should just, like, Add it to the demo, and see later what we do with that.
**Martin Kuba** 28:37 Yeah.
**Jared Freeze** 28:39 Can you explain real quick how this affects the backend?
Like, once you have this data, what… then what… what happens when it's, like, collected?
**Maxime Quentin** 28:51 You're talking to Martin, or me?
**Jared Freeze** 28:54 Yeah, anybody. I mean, it's a… it's like… it's not a resource, right? So, I'm just curious.
**Martin Kuba** 29:00 It is a resource, like, I mean, it's…
**Jared Freeze** 29:02 As a resource.
**Martin Kuba** 29:03 It is sent over the wire as resource. Okay. All the entity… all the entity attributes are sent as resource attributes.
**Jared Freeze** 29:12 Okay, so it's an array of resources?
Yeah. Is that what this does? Okay.
Gotcha.
**Martin Kuba** 29:18 So, yeah, like, what it means… what it means for… But, like, from, like, the protocol perspective, like, the resource… It's kind of the envelope, right, for all the signals underneath.
So, like, from the backend perspective, like, you don't have to… Like… like, you can just get the session ID from, like, the envelope instead of, like, from each signal individually.
**Jared Freeze** 29:45 Yeah, I'll be… I'll be interested to see, like, how this works, because, you know, we kind of talked before about… you know, especially when you're on a page, like, you have things that start on a certain URL and end on a different URL, things like that, and what that might look like, or, you know, if query strings are eligible to be navigation, you know, et cetera, et cetera, et cetera.
**Maxime Quentin** 30:06 True.
But Roy did not think about it.
why the processor will, will tag the, the URL, when you generate the signal, so you… if you have several signals, you have several URLs.
Where the entities are shared by all the… Yeah, true.
**Jared Freeze** 30:31 Cool.
**Martin Kuba** 30:35 Alright, we're out of time, so… See you on the internets.
**Jared Freeze** 30:41 Huh, cool.
