SIG: Client Instrumentation SIG
Date: 2026-06-09
Duration: 30 minutes
============================================================

## Zoom Recording Transcript

**Hanson Ho** 00:20 Hello?
**Cleo** 00:22 Hello!
**Hanson Ho** 00:29 Let me try to… Actually, is Martin coming? Oh, there it is.
Hey, Martin.
Hey, everybody else?
**Jason Plumb** 00:45 Ayy.
**The Jetsons (ca-wat-brt3)** 00:50 Hello.
**Hanson Ho** 00:53 I can create the, next iteration of the meeting in the doc.
Yay!
So, for folks who are new, hi, nice to meet you. My name's Hanson.
**Cleo** 01:40 Hey, Hanson, I'm Cleo. Brian and I both work on Firebase at Google, and we are just dipping our toes in, starting to… to look at some hotel stuff, wanna get involved here, so… just coming to see what it's all about.
**Hanson Ho** 02:00 Nice.
**The Jetsons (ca-wat-brt3)** 02:01 Yeah, so I'm Brian. We're actually not sure we're in the right place here, to be honest.
**Cleo** 02:06 Yeah.
**The Jetsons (ca-wat-brt3)** 02:07 It seems like there's a lot of different SIGs related to client-side hotel collection.
So I don't know if there's an agenda for this meeting, but if somebody could give us, like, a quick blurb of what this SIGS in particular focuses on, that would be.
be super helpful.
**Hanson Ho** 02:28 So I posted a link to our doc, which is the, kind of, the weekly, or the meeting agenda, and things like that. So this tends to be, a SIG where all the various.
Client-adjacent, and by client, we mean user-facing apps-adjacent SIGs kind of meet and discuss, kind of cross… platform, SIG Topics. This used to be the one and only, and then we kind of broke out into our individual ones. There are ones for Swift, Android, Kotlin, and various web ones.
**Jason Plumb** 03:01 Yeah, the web one's pretty active, yeah.
**Hanson Ho** 03:04 And some talk about, like, SDK, API instrumentation. Others talk about, semantic conventions, which is basically, giving meaning, to telemetry that we log by having official, supported, meanings for attributes and events and things like that. So… this is, like, the grab bag.
If you have specific platforms that you want to investigate or contribute to, it might be good to go to those SIGs specifically. And I don't have the link handy, but somebody could search for… there's a community page that we have that lists all the SIGs in the meetings.
Along with their agendas and, like, Zoom times. So you can peruse the agendas to see if they kind of fit what you're looking for, and then attend those meetings if you wish.
**The Jetsons (ca-wat-brt3)** 03:54 Awesome, thank you.
And the web sig just went… like, the web sig is the browser SIG, is that right?
**Jason Plumb** 04:02 Yes.
**The Jetsons (ca-wat-brt3)** 04:03 Awesome, thank you.
**Jason Plumb** 04:04 Which Martin… I think Martin takes part in that, right?
**Martin Kuba** 04:07 Yeah, yeah, I'm one of the maintainers there.
**The Jetsons (ca-wat-brt3)** 04:10 Cool.
**Martin Kuba** 04:15 Yeah, and this, this, this meeting is only once every other week.
my, And the agenda usually is pretty light, like, it's… we usually only discuss, like, as Hansen said, topics that cross between… between different platforms.
**Hanson Ho** 04:34 I posted in the, in the chat a link to the GitHub community page where all the SIGs are listed, so, feel free to, to… peruse, if you search for platform words like Android or… or Swift, you'll find what you need.
**The Jetsons (ca-wat-brt3)** 04:55 Perfect, thank you very much.
**Jason Plumb** 05:14 Martin, are you facilitating this meeting?
**Martin Kuba** 05:17 I can.
**Jason Plumb** 05:19 You know, I don't mind doing it sometimes, but I'm trying not to since I'd just come out of the Android meeting into this one.
**Martin Kuba** 05:26 I see, yeah.
Yeah, no problem. Yeah, so I…
**Jason Plumb** 05:30 I mean, unless Hansen wants to, like, I mean, we're open to whoever, but, like, I… I honestly don't want to. I will say that. Okay.
**Martin Kuba** 05:39 Alright, well, Hanson, you've got the first topic.
**Hanson Ho** 05:42 Yeah, so, the crash semantic convention got merged, you know, after a long delay, partly of my doing. But, we pulled from it, a couple of attributes and additional things that are slightly more controversial, and somewhat orthogonal to the crash.
One of them is, what I was trying to add, something called async.
I think, like, app.async or something like that, which denotes the fact that telemetry, may not be recorded by the same app instance and SDK instance as, reporting it. So, looking at You know, the app and the environment that the event is coming from, like we typically do through the resource, will be wrong.
Because the resource will tell you basically what, the reporting SDK instance, or app instance, has, or is. But what we actually want to find out is, Where, like, the environment, where the actual event took place.
So it's especially, pertinent for crash, because if you look at, say, like, the app version, an app name, or app version specifically, you want to actually know the version that the crash happened on, and not the version, that reported the telemetry.
So, the idea is to have an attribute, that is, tells you that, that basically says you don't have to figure out, that this is not coming from the thing that it's supposedly coming from, according to the resource, but from something else.
So originally it was part of, yeah, the crash one, but I think I'm just gonna submit a new attribute, separate from it, so it could be discussed in a, in a more, generic way, because any attribute… sorry, any telemetry potentially can have this.
So yeah, thoughts on… on this, Some of you probably have seen this, in the PR and things like that got pulled out, but, you know, just want to put this out there.
**Martin Kuba** 07:53 Do you mind linking that PR?
**Hanson Ho** 07:56 I haven't created the new PR.
**Martin Kuba** 07:58 Okay.
**Hanson Ho** 07:59 Yeah, I will do that. So, this is kind of like, in theory, would… what do you folks, feel about something like that?
**Jason Plumb** 08:09 I think async is the wrong word.
because there's a lot of async, kind of, telemetry and context propagation that happens within, like, Java applications that are, you know, doing threads and fibers and stuff, so I think async… I don't necessarily have a better word. I think I have my head around the problem that you're… the problem space you're describing, but… It's, like, maybe, like, delayed telemetry, or, like, buffered, or, you know, replayed, like, is another kind of… like, you're kind of, like, replaying a telemetry stream from another… instance, I don't know. Just async feels a little wrong.
**Hanson Ho** 08:53 Yeah, I… that's just, like, the first word I came up with, and I have no… I have no, I have no special affinity to it.
**Jason Plumb** 09:01 Do you know… do you know what happens in Android today with our disk buffering implementation when… Stuff is written, the app is… force closed or killed before everything's read from disk.
Does the resource and or the session get… I think the session is an attribute, so that should be on device. But what about the resource? Do you know if that gets persisted?
**Hanson Ho** 09:26 Yeah, I think the entire request is what's being, what's being outputted, right? Or what's being cached. Yeah. So it would include everything in the header. So, like, as soon as it kind of comes out of the exporter, it's locked, and that's fine. So this wouldn't really be an issue where… because… and… where the telemetry's recorded is the same process. So, you know, by the time it goes out the door, it is what it is. It could be revived later on.
when it's sent, and it still has, like, the old everything. Where it gets interesting is basically when we actually try to create telemetry from tombstones, or we detect, oh, look, we have this thing that tells me something about a previous process, or more generically, can one system report telemetry for another system? So, you know, we have issues, we have things where there are obfuscated, files, or, you know, stack traces. One would assume that you want to do something… you could potentially do something in the collector, where that stuff is merged and effectively refired or re… or re-remitted. No one does that, I don't think, but it's… it's possible.
or… or there's, you know, big, OS exit tombstones, like, for Android application, exit info, which contains a bunch of cool information about, like, past processes. One can… one can see instrumentation picking that stuff up and firing, you know, the telemetry for things that happened previously.
So this is kind of like, the workflow that we want to have supported, of which, you know, native crashes, potentially could be that.
actually has to be that. You can't report native crashes in the same process.
So maybe we don't need to discuss, per se, but, like, just want to kind of float this out there, and then, I'll… when the PR is ready, I will… I will post it.
**Cleo** 11:32 And I'm curious, because what is the thing that's actually missing? Because if you emit that telemetry after the fact, like, it's got all of the timestamp, it's got all of the session… so what is… can you just describe that one more time? What is the thing that's… that is missing?
**Hanson Ho** 11:47 Yeah, so OpenSolometry, when you record, like, a trace or a log, has, information about, kind of the environment, that it's being created from. We call that usually a resource, so, when the SDK starts up, it says, hey, what the OS version is, what the, service name, service, a lot of stuff.
That is decoupled, from the actual, login span.
And when it's exported, we create batches where the same envelope, will have multiple spans and logs which have the same associated attributes, so we're not going to be duplicating, like, you know, service name on each.
you know, telemetry. Each, like, you know, signal, log, chase, things like that.
So the… what happened, in the actual crash would be represented in the log, but the environment, it relies on basically the SDK instance that, generates that log to provide. Yeah. So that… that relationship is implied, typically, hey, whatever the resource says I am is where I'm from, and this is basically saying, don't trust the resource that delivered me. I'm actually associated with some other resource.
**Cleo** 13:04 Yeah, and so I guess the question here is, like, do… should there be more tight coupling between the resource and those things, right? In the recovery, you could also recover the resource information as well, as opposed to introducing a new attribute.
And so, like, I think there's also a question of, like, what is the tombstone, and what deserves to be in the tombstone if we're going to be doing these things after the fact? And that's definitely something we're worried about, for Firebase as well. So, would love to continue that conversation.
**Hanson Ho** 13:43 Yeah, I think, being able to recreate the envelope, would… would… would be, I think, the best. But… at… at the level, that we have access to, we can't really do that. That's kind of, like, above the pay grade of… of instrumentation, and… and even S… well, maybe not the SDK, but certainly instrumentation. So, as much as we can, that would be… that would be ideal.
**Martin Kuba** 14:12 It sounds to me like it's something that would have to be supported by the SDK, so it would have to be in the spec, right?
**Hanson Ho** 14:18 Yeah, so, like, I think one challenge, generally, I think, for client, SDKs, or user-facing app, is the model is very different than backend, so there's a lot of things that… that I think is important for us that isn't… just… just isn't built into the SDK, because it's just not something that… that needs to be supported. So… there's usually two ways of doing it. One is trying to, like, do it the quote-quote right way, which requires a lot of threading and a lot of, getting the right folks to buy into this use case as something supported. And other ways are kind of, like, working with what we have, what we can, which is defining, under semantic conventions, what things mean. So, it would be… It'd be ideal to go through, like, the right and proper way, but it… sometimes it just, is difficult.
So, different ways of solving this problem would be, would be nice to discuss. So maybe, you know, We can talk about it next week, or next session again, just for this just to be kind of surfaced.
**Jason Plumb** 15:42 Yeah, I mean, it'd be cool to see a prototype. I mean, I can see a world in which we had like any Android, if you had… if we were to persist, like, session information, session and resource being the main things, if we were to persist those on launch.
With, like, a time… even maybe with a timestamp, and then, like, when there's something that needs to go recover a tombstone, if it can stitch those two together, and then pass that to an exporter that is, like, context-aware, that knows how to do that magic swapping.
That'd be a cool experiment to see.
We have, I think we haven't deleted it yet, but in Android, we have an exporter that can completely rewrite data on the way out, and so that might be a starting point, if you wanted to see that.
**Hanson Ho** 16:30 Including the, the OTLP, like, the envelope?
**Jason Plumb** 16:33 I think so.
find it.
Okay, I think I'm wrong. I think it doesn't change the span… the… I think it does not change the resource.
Yeah, it's really, really hard to change the resource in the OpenTelemetry API right now.
**Hanson Ho** 17:02 Yeah, in the Embrace SDK, we basically take a cache of an envelope, basically create an envelope tombstone, and then we piece that stuff together.
trivial to do, to send to our own endpoint. But, when it's exported, it… it… it… we… we don't control what the envelope says. So, that would be a little bit, misleading, if you take a look at that.
**Jason Plumb** 17:29 I wish I had time to work on this stuff. There's some interesting… I think there's some interesting vectors for doing this.
They all feel hacky, but so does all instrumentation.
**Hanson Ho** 17:42 Yeah, this is almost a way of, hey, we can't do it right, how can we do it? Kind of wrong, but also… it tells you what is going on. So when you see that, you're like, whoa, watch out. it could be ignored because of the semantic invention. And because it's a semantic convention, it could also, be linked to specific events, and those events may specify in attributes that there are these additional things that we typically get from resource. So, a generic solution, I think, is a lot harder, because you have to take care of, like.
all the cases. This is almost like a way of, like.
surgically inserting something that, hey, for a native crash, you could look at this place for the relevant app version, for instance. So it's… it's certainly, not… I would say a change to the platform, but it is a pragmatic way of telegraphing information that otherwise would not have a standard, which is what semantic conventions is all about.
Standardizing the hacks, if… even… even if that's what that is.
**Jason Plumb** 19:07 I'm just taking notes since no one else is.
Martin.
Not to put you on the spot.
Yeah, that's… that's super interesting. I… I think… yeah.
What else… what else kind of falls under this umbrella other than tombstones?
**Hanson Ho** 19:28 Things that are difficult to, get, synchronously in a performant way. So there's certain Android APIs that basically create blobs, whether it's available on device to be parsed or sent to the server and parsed, you know.
profiling manager, for instance, basically does a mini Perfetto, and there's no way we could actually read and do anything with that. there's also other APIs that, are, that require additional processing, that is just not, you know, feasible on device. The clearest use case is things like application exit information, and crashes, like.
just saying, hey, we only know what happened, to this process, or app instance, by these tombstones that the OS writes. So there's a lot of information, when, like, a user terminates, a proper A&R exit, all this stuff, could potentially be events.
And I could also manufacture other, you know, theoretical use cases, but these ones are actual ones.
**Jason Plumb** 20:48 And Embrace already has code that does some of this, right?
For your own stuff.
**Hanson Ho** 20:52 Yeah, so… so this is… this is all about getting things into semantic conventions so that what we export is… is going to be understood by, you know, generic, you know.
embrace, we understand the envelope that we have, we can associate properly, do all that stuff. That's because, you know, the data we send to our own is not OTLP, and we can basically chop and slice and dice however we want.
Versus… we want the exported OTEL data model to, if not optimally, most efficiently, at least, like, in terms of data, be able to represent, In a standard way, what we send to ourselves.
**Jason Plumb** 21:35 Yeah.
**Martin Kuba** 21:49 So, so Hanson, the next step here is for you to… Gonna summarize this in an issue or PR?
**Hanson Ho** 21:55 Yeah, I'm… originally, I was gonna do, like, you know, Crash Part 2, where we put in the fun stuff, like the blobs, but I think the next one I'm gonna look at is just this attribute, and then adding it to the, To the, crash event, to denote that.
**Jason Plumb** 22:15 Oh, so you're seeing this as an… as a… as an attribute on the crash event?
**Hanson Ho** 22:20 On whatever event chooses to opt into supporting it.
**Jason Plumb** 22:24 Yes. And by it, you're… what is it? Like, it's some… it's some record of the previous thing, but I don't…
**Hanson Ho** 22:31 That the telemetry can be delivered, by, produced by an instance. That is not representing, the app, in which the event was recorded.
**Jason Plumb** 22:43 Oh, so that's on the telemetry itself?
**Hanson Ho** 22:45 Yes, so this would be an attribute.
**Jason Plumb** 22:47 Period, okay.
**Hanson Ho** 22:47 That's, like.
theoretically orthogonal to what is being recorded, but really, in practice, only applies to certain, attributes where it makes sense. Like, you know, we could theoretically put this on a tap, but, you know, it starts becoming silly. Hey, I want to report a tap from another instance. Like, really? Do you really need to do that? Versus, for native crashes, the answer is yes, you really need to do that.
There's no other way, I should say.
**Jason Plumb** 23:17 But this attribute wouldn't be relevant to, like, a native crash, right? Because the native crash is written by the platform.
**Hanson Ho** 23:24 The… You talking about the tombstone?
**Jason Plumb** 23:28 Yeah.
**Hanson Ho** 23:29 Yeah, no, so this is just denoting the nature, or, or the provenance of the telemetry itself. It doesn't actually describe, anything about the telemetry, so this could… anything.
**Jason Plumb** 23:46 So sorry, when instrumentation is mapping a tombstone into OpenTelemetry.
telemetry, it would be an attribute on that to indicate that it had… that it had to come from somewhere else.
**Hanson Ho** 24:02 Yes, so when, when you actually.
**Jason Plumb** 24:03 I think I misunderstood you the first time you said it. I thought it was, like, an attribute that you'd spec on the crash event.
**Hanson Ho** 24:11 So with events, you would say, I have this attribute, right?
But you can have other events that have the same attribute.
So, the first event that will have this attribute is crash, but there could be potentially other events in the future that also have this attribute.
**Jason Plumb** 24:35 Got it. I did misunderstand you. So it's an event… sorry, it's an attribute on the event going out that could give a hint or an indication that it came from a separate event.
instance or process.
Like.
**Hanson Ho** 24:47 Don't look at the resource for the version information. It's gonna…
**Jason Plumb** 24:50 Do you think of Fulian?
**Hanson Ho** 24:54 feast.
**Jason Plumb** 24:55 Does there need to be additional context spec'd for that attribute?
**Hanson Ho** 24:59 The… it would be at the event level?
So, that's a good question. It could be a list of strings.
**Jason Plumb** 25:09 What if it's the resource? What if it's.
**Cleo** 25:11 Yeah.
**Jason Plumb** 25:12 So, yeah.
**Cleo** 25:14 That's right.
Because it feels like that's what it is. It is the resource. It's the resource at the time of the crash.
**Jason Plumb** 25:21 Yeah.
**Cleo** 25:22 So…
**Jason Plumb** 25:22 Yeah.
**Cleo** 25:23 it feels like that's the thing that we should hold onto from the SDK, and persist that in some way, such that on recovery, you know, we're stitching together the right things, and that they're sort of tied together by that session ID, because the crash will have that session ID, the resource hopefully we'll have that session ID as well. And that… that… rather than, like, inventing a new mechanism to hold this thing, we have the right thing, it's just we don't… we aren't holding onto it at the right time.
That's what it seems like to me.
**Hanson Ho** 25:57 Yeah, or if not a full resource, but a set of resource attributes that are relevant, because maybe there's a bunch of stuff that's not relevant.
Yeah, it's probably… Seems like…
**Cleo** 26:12 probably, like, app… app ID of some… some sort of app ID, some sort of app version, and the session ID are probably the most relevant things.
**Hanson Ho** 26:20 Yeah, I think in the crash log, we actually, or the crash event, we actually specify, like, I think four different things, to say, hey, these are the things you should look for, but it's not kind of spec'd out beyond, you know, on an event basis, optional attributes. So… This could certainly be… be beefed up in order to, to kind of self-describe. And also resolve the naming issue, too, because now it is more specific, rather than, like, you know, something amorphous.
So, yeah, I could definitely take a look at that and kind of refine that.
Good suggestion, thanks.
**Jason Plumb** 26:59 I think an issue would be a great place to bike shed on this, yeah.
**Hanson Ho** 27:04 This is not bike shedding, this is… there are some naming things that are bike shedding.
**Jason Plumb** 27:08 Like.
**Hanson Ho** 27:09 Class names, but if you're talking about interfaces, names are fucking important.
**Jason Plumb** 27:13 I concede, okay, fine.
**Hanson Ho** 27:17 Let's bite you in on that. I'm kidding.
**Martin Kuba** 27:22 We have, like, 2 minutes left, and I think, Jason, you have just announcement, maybe, or…
**Jason Plumb** 27:27 Oh, no, I mean, it's related to what we've been talking about, but this was a long-standing crash thing that Hanson has been working on for a very long time, and to see it get merged is awesome. We're already using it in Android, so… Within the next release cycle, we should have those weaver-generated constants that we'll be using.
**Hanson Ho** 27:49 Yeah, in this event, the ones that are specified are actual attribute resource attributes, so if we were to do this, in a way, we could basically replace this D2 of the event, to say, look for these instead, here.
**Jason Plumb** 28:07 Is Web gonna use this? Is web able to create a crash event? I know web is, like, much harder to do crashes, right?
**Hanson Ho** 28:13 I was talking to Jared about web, and the notion of crash, it just means, totally different things. So, his opinion is that, this is not something that… that would be useful, because they wouldn't be able to get a lot of this information if it's actual crash. Otherwise, it becomes, like, a… some sort of, event modeled differently, that is not an abrupt termination of process.
**Jason Plumb** 28:42 Yep.
**Cleo** 28:45 The attributes might still be useful, though. Well, I don't know browser versions.
are a nightmare. And versions in general in web are a nightmare, but… I feel like some of those attributes are probably useful in web as well, even if they're being logged as whatever, running events. I don't know, Brian, do you have… Thoughts on that one?
**The Jetsons (ca-wat-brt3)** 29:09 Yeah, cause, I mean, I was looking… I was looking at that.
VR. It seems… I mean, to me, it seems applicable to browser… capturing browser errors, even if they're not, like, actual, you know, process crashes like they would be in Android. Capturing an error in that exact same format. Like, I don't see anything here that would be… If this is what you wanted to capture, I don't see anything that would… Prelude it for browsers.
**Hanson Ho** 29:36 So for semantic inventions, we have a very specific definition of, like, what the event actually is, and then also, like, the attributes under there. So I think, what Jared, who's a colleague of mine, and Embrace, what he was saying is, yeah, most of these attributes do apply to certain things that happen on the web, but it's, like, under a different like, thing, it's like, yeah, it'll be, like, error, which would be recoverable. So, like, likely the event itself would be something else, with largely the same attributes, maybe even, like, exactly the same. So this would be something on the web… for the web folks to kind of take a look at. Obviously, the web produces errors, and it'd be nice to be able to capture it somehow.
**Martin Kuba** 30:19 Just… just a… just a quick comment, Hanson, like, is there maybe, like, a different use case than just the crash for… in mobile, like, when you, for example, when you lose, like, network connection?
Like, you can't export anything for a while, and then, like, your app restarts, and you have, like, a batch of, like, all sorts of different… yeah, anyway, okay.
**Hanson Ho** 30:43 I can… we can talk about that in the issue when we finally rocket.
**Jason Plumb** 30:46 Yeah, let's talk about that one next time.
**Martin Kuba** 30:49 But…
**Jason Plumb** 30:50 Thanks, buddy.
**Hanson Ho** 30:50 Bye.
