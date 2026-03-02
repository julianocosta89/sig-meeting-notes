SIG: Client Instrumentation SIG
Date: 2025-09-02
Duration: 28 minutes
============================================================

## Zoom Recording Transcript

**VP Valentin Pertuisot - Datadog** 00:16 Hello!
**Hanson Ho** 00:17 Hello?
How's it going?
**VP Valentin Pertuisot - Datadog** 00:21 Great, and you?
**Hanson Ho** 00:23 A bad?
Ugh.
So Martin is not around today, and since you presented last meeting, Jason, I could present.
**Jason Plumb** 00:41 I would love that. That would be nice and helpful.
**Hanson Ho** 00:46 Volunteer.
**Jason Plumb** 00:47 I've also… I've also not really been keeping up with client concerns very much lately.
Specifically, this meeting.
**Hanson Ho** 00:55 Fair enough.
I always leave it too late to, to add topics, and that's… I know that's not very useful, and I will… I will endeavor to do better.
cool.
Everybody can see the, document? Yeah.
We'll wait a couple minutes, or just one minute, maybe, it's at least, I know, 2.
Let's see who shows…
Missed the last iteration, because that was the way, y'all talked about Datadog involvement.
**VP Valentin Pertuisot - Datadog** 02:35 Yeah, very quickly, I was sharing why… why I joined this group, and
And what, Datadog wants to do, related to OpenTelemetry on the client side, instrumentation, SIG.
**Hanson Ho** 02:52 or altered.
**VP Valentin Pertuisot - Datadog** 02:52 And since you were not there last time, maybe I can… Like, give context again.
**Hanson Ho** 03:00 I don't… I don't mind, but I can also go and just watch the presentation from… or the meeting notes from last week as well, unless other people hear…
**Jason Plumb** 03:10 There's no notes, we can watch the meeting, at least. Oh, okay.
**VP Valentin Pertuisot - Datadog** 03:13 It was very, very short, short. We had… stayed, like, 5 or 10 minutes, because there was only a few of us.
**Jason Plumb** 03:21 Yeah.
**Hanson Ho** 03:26 But awesome, welcome.
OC people.
**VP Valentin Pertuisot - Datadog** 03:29 Thank you.
**Hanson Ho** 03:32 Alright, let's get started. We got… oh, we got 3 items, that's good.
I added two of them, so…
Help myself. Okay, so the first topic, so this is from a few weeks ago. We want to add more client recommendations to the website documentation. Specifically, this is for metrics, and saying, hey, we don't feel metrics is a good use case for a client-facing apps because of a number of reasons.
I think, Santosh had a, PR, or rather an issue,
And he was gonna go update this. I was wondering if, well, he's not around, but, if there's any progress there, or if any other people have, have…
similar desires to add, kind of, documentation like this, because right now, the page is just a bunch… well, it's just stubs, but there's probably best practices for both.
web, Android, iOS, and, you know, other client-facing platforms. So, be curious if anybody's thought about
adding this or anything in there. I personally want to add some stuff about sessions and other things, but it's a bit, you know, farther down my list of things to do, but I'm curious where other people are at.
**Jason Plumb** 04:55 No cycles to help with that, sorry.
**Hanson Ho** 04:58 Fair enough.
**Jason Plumb** 04:59 I want that. Yes, I do.
**Hanson Ho** 05:06 Yeah, I think, what we were trying to do originally was to add warnings and things like that to the spec, and I think, some good discussion was generated, the spec being platform agnostic, those are probably not places where, you know, this stuff should go. But the website seems like a great location, so if, we'll keep pushing this, and maybe anybody who has time has an opinion that, you know.
folks agree with, we can start adding to this stuff. I wouldn't say the priority is super urgent, but it would be better as more people stick their nose into OpenTelemetry and want to do client apps, that there's
stronger, recommendation and guidelines about what to do, because right now, it is fairly,
Wild Wild West, we'll say. And it'd be nice if there's a little bit more, order to it.
Cool, next topic, Jason, Jank PR got merged.
**Jason Plumb** 06:06 Yeah, this is, it's already 2 weeks old, but since I missed last meeting, I'm not sure of the timing. I just wanted people to be aware that this,
PR was a little bit slow going, but it did manage to get merged, and if you click that, Hansen, we will see that…
This PR creates semantic conventions around the event that you can send in the case that you have rendered slowly. So if you are working on web or iOS, and also want to emit an event to indicate to your backend that some slow frames were rendered, here's the first stab at what you can use for that.
And, revisions are also welcome. This is based on another PR that I linked to there that was also open for quite some time, that I think had a lot more discussion and people had issues with it, so we've shrunk it down, it's, like, much more streamlined now, and so…
that's what we got, and let's… let's move forward with it. I'm just… it's mostly an FYI that I bring this up in case you missed it.
**Hanson Ho** 07:05 Yeah, this basically codifies, the existing implementation, no-tell Android, and basically, periodically, event will be admitted, with some… the correct metadata of how many frames are dropped. So if, if, iOS, has, like, hangs and things like that, and you want to kind of do things similarly, that works.
there are also probably some other types of Jenk events that could be reported, and if that were the case, we can either amend this or propose a slightly different one, but this is a great start to have, because previously there was nothing. Now there was something.
**Jason Plumb** 07:40 Yeah, and by codify is, like, it's still experimental or whatever, but I would love for other distros, other developers to use it and be like, you know, it's really missing this, or we don't need this, like, you know, let's make it… let's make it good, and… slow road to stable.
**Hanson Ho** 07:55 Yeah, the, for Embrace, what we do is, is, fire them ad hoc. So instead of there being a period, we kind of gather, gather, and if it reaches a certain threshold, we fire or something.
**Jason Plumb** 08:07 You've said periodically, like, a few times, we pull periodically to see if there are any… any slow-rendered frames, but there… like, most of the time, that pulling should yield nothing, right, in a normal app.
And so…
**Hanson Ho** 08:19 Oh, yes.
**Jason Plumb** 08:20 It's checked periodically, but they're not fired periodically.
**Hanson Ho** 08:23 Right, the interval is fairly random, right? Because it's, like, chunk of time, chunk of time, chunk of time.
**Jason Plumb** 08:30 And usually there's, like, no events, no events, no events. Oh, there was a couple of, like, slow renders, here's what those look like. Yeah.
**Hanson Ho** 08:36 Right.
And, and…
I think it's a perfectly reasonable way of defining that, but another way is to kind of just, instead of, instead of, the defining the start and stop of period, you know, fairly arbitrarily, we could, you know, detect that, like, persistently monitor that, when it reaches a certain threshold.
grab it, fire it, so…
**Jason Plumb** 09:00 After the fact, compute your period? Is that the thing?
**Hanson Ho** 09:03 or not even… not have a period, so there's no… there's no checking period, basically. But that's a different way of, basically.
doing the same thing. It may be more event-driven, because, you know, there are certain times where things are more, likely to, to be like this, and instead of, like, you know, having a time that starts slightly before, just because of how the period works.
But, you know.
different horses for courses, so… so this is totally a good, first step into, you know.
**Jason Plumb** 09:32 And that's slightly more of the how instead of the what. Like, the event that you send hopefully is interoperable? Well, I guess… you'll tell us.
**Hanson Ho** 09:41 Oh, yeah, I mean, we would put, like, a zero in the period or something like that to indicate it. So, it could totally be used that way, but, like, with a slight amendment kind of thing, so…
**Jason Plumb** 09:49 Okay.
Cool.
**Hanson Ho** 09:52 Third…
**VP Valentin Pertuisot - Datadog** 09:54 Some context on the Jenk stats. So, I've been trying to catch up of the work that has been done here recently.
And I can provide some insight on how we solve this at Datadog in our SDKs.
And so for the Jenk stats on Android, we use the Google library that actually, like, you give you a listener that gives you the jank stats directly.
So it's not… there is no polling, it's actually just the system giving you callbacks, and it also gives you, like, I think it's some data that… it's not reported yet in the current,
model that, that got merged, is that we have actually the duration of every jank.
So, the way right now we… it's not open telemetry, but the way we report this, it's basically an array of all the frames, and the timestamp, and the duration, the jangst duration.
So, we can actually, like, provide the users, like, some value of… it's not just a jank, it's, like, a jank of 300 milliseconds, or it's a jank of 17 milliseconds, which, actually, you don't really care sometimes.
**Jason Plumb** 11:03 Right, yeah, so the, the, specif… sorry, the, semantic invention did have, some threshold…
amounts previously, or… I forget exactly how it was structured, but yeah, we didn't want to report every single duration, because there could potentially be lots of them.
**VP Valentin Pertuisot - Datadog** 11:19 Hmm.
**Jason Plumb** 11:19 But we were trying to, like, bucket it into the… originally, we were trying to bucket it into slow and frozen, which is, like, the Android guidance, you know, so the 17 milliseconds or whatever, versus the 700.
Yeah, we also use the framework to register a listener for that thing.
**VP Valentin Pertuisot - Datadog** 11:37 Okay.
**Hanson Ho** 11:38 Yeah, the implementation is a little bit decoupled from the Spence Convention, which basically just says, describes what is fired rather than how it's obtained. So, you know, you can certainly, you know, listen to the choreographer and count frames, you know.
Or you can just, you know, pull stuff from there. Or you could have other means of determining whether the UI is responsive by not necessarily counting the frames, but rather looking at responsiveness of the UI thread and things like that.
how you determine if there is jank, which, you know, one way is dropping of frames via the platform Jank stat. Other means, you know, are fine as well. It's, you know, the, the, I think the important part is
my opinion, at least, is that the… when it goes out into the world, it looks the same. So, regardless of how implementation is being done, so…
Yeah.
Cool.
Awesome. I should update. Oh, man, I can't do two things at once. I have to add notes. I'll do that after. So third topic, is, the Kotlin API and SDK. So,
Embrace, for folks who are new, we're trying to define.
a new API for Kotlin, and then had a nice scan top of that, or underneath it, I guess, so that it could be used in, non-JVM use cases, so KMP specifically.
So, we've got, an API defined, through iterations, we're looking at it. there have been calls for feedback before, but just a quick update here is that, we've gotten an…
implementation done as well for tracing and logging, that, that is just pure Kotlin. So Jamie, who's on this call, did the bulk of the work and has a sample that, you know, has a KMP app that, is… targets iOS and JS, or…
web, and Android that… for which this works. Obviously, the API has an adapter implementation that allows you to use the, Java SDK.
And, we are looking to, make the Embrace SDK use the SDK implementation as well, soon. So this is kind of just, an update that, hey, there's progress being made, and, if folks want to come and take a look at the API again, please, especially if you have, expertise in.
multi-platform work, and how this is going to be used on iOS or Android, or sorry, iOS and web.
It would be nice to get some feedback, because the initial use case is very much focused on Android, and we realize there's a few, you know, things that we could probably improve of the API, if we really want to make it a multi-platform API.
So we're talking to, some folks, about donating, and, spinning up, Project Doc, or maybe a SIG for this in the future, to make it all official. So…
Yeah, we certainly need another maintainer for this, other than somebody from Embrace. So if you're interested in this work, please have a look at the, at the repo. Thanks, whoever pasted in. Jason, maybe?
**Jason Plumb** 15:00 Is that the right… is that the right repo?
**Hanson Ho** 15:02 Yes, correct.
**Jason Plumb** 15:03 That was me.
**Hanson Ho** 15:04 Yeah, we have daily builds, snapshot builds, we release fairly frequently. The API and the wrapper implementation is, in production for Embrace already. So, you know, feel free to, to comment, and, and, play with it.
Anything else you want to say, Jamie?
**Jamie Lynch** 15:29 I don't think that's covered it, unless anyone has questions.
**Hanson Ho** 15:36 Awesome. We'll make them the push on the slacks, so for people who are not attending this meeting, so…
Alrighty, jason… Web… iOS.
**Jason Plumb** 15:52 Oh yeah, so we've also recently converted our ANRs in Android to use an event.
I just wanted other people to be aware of this. I'm curious about if any iOS or web developers are also emitting A&Rs. ANRs, I don't know if that's a universal acronym, but it means Application Not Responding. I should probably unpack that.
So, if you click that link, Hansen, it'll show the PR that does this thing, and I made a comment here, which I just think
might be nice to talk about, but, this PR changed the name of the event that we were admitting. If you scroll up, yeah, well, that line 90 there, you can kind of see, that the event name is not device.anr, which is… I think does not exist in semantic conventions at all, so…
It used to be a span, like, if you look at… Oh, I don't know.
How did this used to be structured?
Maybe the ANR detector class was emitting the span? I'm just trying to figure out what the span name used to be.
**Hanson Ho** 17:02 Well, the SPAN name is pretty arbitrary, right?
**Jason Plumb** 17:05 I mean, it was before, and the event name is now, so that's what I'm… what I want to talk about.
So…
**Hanson Ho** 17:13 We'll just have a chat?
**Jason Plumb** 17:14 Try the A&R detector, maybe.
**Hanson Ho** 17:17 You know, the texture…
**Jason Plumb** 17:20 Down a little.
Right there. Up.
**Hanson Ho** 17:23 Oh, yeah.
**Jason Plumb** 17:24 Yeah, was this one making spans?
Yeah, right there.
No, maybe.
Mmm, no.
No.
Well, I forget what our old… I forget what our old span name was, but it certainly wasn't device.anr, and we went ahead with device.anr in…
In spite of there not being a semantic convention for such a thing, so… it'd be cool…
if any other platforms have an opinion on this, or if anyone wants to bootstrap a semantic convention PR, otherwise, I guess I might do that.
**Hanson Ho** 18:00 So, at Embrace, the telemetry log is a span, but we don't only log the basically terminal call stack at the fifth second. We basically take, you know, call stack samples throughout, and we add them as span events, so you're able to kind of look at, you know, and create flame graphs, from those, samples.
So, that is, I think, materially different than what this is, which is,
You actually, you know, get…
well, you're trying to basically say, at the end of 5 seconds, this is the call stack. So,
That would be, I think, something different than this,
But, you know, in a similar vein, I guess.
**Jason Plumb** 18:46 Yeah, so help me understand that, Hansen. So, you… you… when you get an ANR, or detect an ANR,
You make a span event for that.
**Hanson Ho** 18:57 No. So, Jamie may be a better person to explain the implementation.
**Jamie Lynch** 19:04 Sure. Basically, we…
capture a span at the start of when the application's main Fed has been blocked for more than a second.
**Jason Plumb** 19:16 We do, too.
**Jamie Lynch** 19:17 captures of stat tracers at regular intervals, and we… Advos as span events.
**Jason Plumb** 19:25 to the A&R span.
**Jamie Lynch** 19:27 Yeah.
**Jason Plumb** 19:28 Okay, so you're, like, you're backfilling, like, some historical context of the stack on your A&R event.
**Jamie Lynch** 19:36 Yeah, basically.
**Jason Plumb** 19:36 Okay, okay. Yeah, and our current implementation, I think, just gathers the one, right? Like, just the…
Maybe? I forget.
**Hanson Ho** 19:45 Yeah, yeah, it's… I think at the 5-second interval, if it's still blocked, it takes the, the call stack and fires, I think it was a zero-width span, because you don't capture the… the start time, right? It's just… not width, zero,
**Jason Plumb** 20:00 Right.
**Hanson Ho** 20:01 Yeah, so I think for the implementation in OpenTelemetry Android, it definitely makes sense to be an event, because it is a point in time.
**Jason Plumb** 20:10 So it's hidden behind the instrumenter interface, but that A&R detector is where that span name is created, and it's,
It's, like, line 59 there on the left, so…
that builder is building this instrument, or the instrumenter knows how to craft a span name, it's that stack trace to A&R. That's a, like, a callback that the instrumentation API will invoke to get the span name, but that just, like, goes away. So it used to be called all caps ANR, that was the span name.
It's now going to be called device.annr, and neither of those have a semantic invention.
That's what I wanted to bring up. And, yeah,
There's a… there's a side convo in the chat, thanks for that. Yeah, on Android, definitely, we're just, like, detecting the main thread blocked for more than a few seconds, like 10, or 5, or whatever it is.
**Hanson Ho** 21:01 Yeah, so the A&R terminology is probably, a bit problematic, because Android has actually shifted what ANR means. Like, at the very beginning, it does mean Android not responding, in the UI thread.
**Jason Plumb** 21:17 Oh, Android not responding.
**Hanson Ho** 21:19 Or application, yeah, you know. But subsequently, they've built other conditions.
by which an A&R event, can be triggered under the hood. Main thread blockage being the most popular, but also not the only one. There's, like, uses of foreground services and a whole bunch of stupid things that really isn't related to main thread blockages that can cause it. So if you have, like.
A&R exits in the play dashboard, they're not 100% from main thread being too busy to respond. So, I think we're embrace looking to genericize this notion, and basically have something that is…
tries to use the right terminology, but also uses terminology that people understand, which on Android is still A&R. But effectively, this is main thread blockage, which, for the most part, will lead to an A&R, but is not exclusively the cause of A&Rs. And other platforms, iOS, I think, calls it hangs. I don't know if web has anything similar to that.
Maybe they do, but generally, we just see…
a pop-up that says, you know, JavaScript not responding, you know, I'm gonna kill it. So I don't know if there's API access. Web folks may want to illuminate us and say, hey, is there any way of detecting unresponsive main thread, I guess, for JavaScript, there's only that one thread, so…
**Jason Plumb** 22:48 Definitely, if A&R is too Android-specific, let's figure out a middle ground between that and Hang, or just call it Hang. Let's figure out the kind of the common thing that we think all Roam vendors will want.
**Bee Klimt** 22:58 On, on React Native, there's a version that a lot of people call Slow Event Loop that I think is… I think is analogous to.
**Hanson Ho** 23:08 So basically, the… what the users see in that case would be, basically, they click, or they tap, and nothing happens. So the UI is unresponsive, kind of thing, right?
**Jason Plumb** 23:24 Yeah, I think that's the idea.
**Hanson Ho** 23:25 Yeah, so I think something to do with, like, UI unresponsive, or something like that probably makes more sense. then we can kind of, you know, Android, keep our own naming, even if it's not technically correct, but the event itself may be a bit, more generic about, hey, your UI is not responding, and I think that that's…
that's definitely a problem for iOS as well. However they get the data, I think MetroKit will provide, you know, Hang data and things like that. Hang and… what's the other one? I don't remember.
**VP Valentin Pertuisot - Datadog** 23:54 You cheers.
**Hanson Ho** 23:56 Glitches? Yeah, right. That's a shorter one.
But I'm…
**Jamie Lynch** 23:59 Sorry, Hansen. But Android, I'd also add that even if a main photo is blocked, it doesn't necessarily mean that the UI is being blocked.
You only get an ANR when the main thread is blocked if the user's actually interacting with the app. It kind of gets silently ignored if it's just happening in the background. So…
That's another fun consideration.
**Hanson Ho** 24:24 But we might think about naming this.
**Jason Plumb** 24:26 Do you… do you account for that in your distro?
**Jamie Lynch** 24:31 Yeah. So I think the most foolproof way of getting…
like, an actual ANR by Google's definition is via the Application Exit Info API.
Yeah, so potentially that's something we could…
Think about changing OpenTelemetry Androids to Capture?
**Jason Plumb** 24:52 Yeah, because I don't think we capture that at all right now.
**Hanson Ho** 24:54 Yeah, I… oh, yeah, because I think we need… with application exit info, it's a big blob tombstone, so you have to basically pull it out and, you know…
figure it out that that last exit was one fire it. So it's almost like there's two events here. One is, like, literally, Android tells us an A&R happens, regardless of origin or cause, and what basically all the instrumentation, we can get at real time is, which is, you know, main thread blockage,
it'd be nice to know if iOS has, you know, a similar differentiation, or they pretty much couple the two, and I guess on web as… or React Native or web as well.
But there may be two events here. One is… because, you know, 5 seconds is fairly arbitrary. You kind of want to know 2 seconds, 3 seconds, 4 seconds as well. And that's not an ANR, but it is… it is main thread blockage, and it's useful information to have.
So, if we want to go with the science convention, I think we should go with something right now that is, you know, what it's doing, which is main threat blockage. And in the future, also consider, like, a more stringent and specific
ANR, or, or, like, Fire OS, Hangs, or something like that. So I think there's, there's multiple ways of, of, of kind of looking at this.
Cool. So, Jason, are you thinking of, of, of, of just, some hang event that basically gives, like, a time, and, and indicates that, hey, the UI is blocked?
**Jason Plumb** 26:30 Yeah, that's all I was thinking. Keep it simple to start, and then we can amend it as needed.
**Hanson Ho** 26:36 again, we… this is already what it's doing, and… and it's good to have something in there rather than nothing.
**Jason Plumb** 26:42 Yeah, because, I mean, anybody that's looking at the telemetry that's coming out of the thing is gonna be like, oh, what is this? I don't see a spec for that anywhere. What does that mean?
**Hanson Ho** 26:52 Yeah, I think it's also useful to, to, in the convention, even if we don't have a name that has A&R, I don't think we should, we should, you know, describe it. You know, situations like this on Android, you know, would cause an A&R.
**Jason Plumb** 27:08 So… Yeah, even in the docs, yeah, totally. Yeah, definitely.
**Hanson Ho** 27:19 Cool. We got 2 minutes left. Are there any action items here? Or, Jason, are you gonna just, like, set up a draft eventually, when you have time, kind of thing?
**Jason Plumb** 27:31 Yeah, I really don't want to, but I probably will.
**Hanson Ho** 27:35 Let's chat offline, because, yeah, it's… I do want to reconcile the embrace implementation with the span, with an event implementation.
So, yeah.
Alright, cool. Any other topics, or are we good?
Cool. Next time, if I have topics, I'll put this in a day in advance and announce it in the client channel. Doing it a minute before doesn't give people much time, which is, which is,
Not great, but, you know, sometimes that's what happens.
**Jason Plumb** 28:12 Yep.
**Hanson Ho** 28:14 And is it Valentin, or Valentine, or…
**VP Valentin Pertuisot - Datadog** 28:17 Very local.
**Hanson Ho** 28:18 Valentine, okay. I will take a look at last week, so it's just so you don't have to repeat yourself, about, you know, what you're doing.
Awesome.
**Jason Plumb** 28:28 Cool.
Thanks.
**Hanson Ho** 28:30 Alright, see y'all in 2 weeks.
Bye.
