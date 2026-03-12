SIG: Android SIG
Date: 2025-10-14
Duration: 56 minutes
Zoom Recording URL: https://zoom.us/rec/share/-vVadza2ghttlLzz4TFqcNaz2dg8mdenfKHEyjzlC1CQFSuFv3mtpZsyI5q5omi7.m_EcrQ3t1J7uBlTa
============================================================

## Zoom Recording Transcript

**Hanson Ho** 00:14 Hello?
**Jason Plumb** 00:33 Good morning.
**Hanson Ho** 00:35 8?
**Jason Plumb** 00:53 These are absolutely the wrong glasses as well. Okay.
That's gonna help out.
Like, I know I'm tired, but I'm not that… yeah.
**Hanson Ho** 01:10 Okay.
I've added the stub in there.
At the three people who were in attendance.
**Jason Plumb** 01:25 Oh, thank you.
That's true.
**Hanson Ho** 01:32 Oh, my God.
**Jason Plumb** 01:33 Empty, empty agenda. Oh my gosh.
**Hanson Ho** 01:39 I'm just…
**Mustafa Haddara** 01:41 Jason, that was a very specific correction.
**Hanson Ho** 01:45 Did the branding folks at Cisco give you a call and say…
**Jason Plumb** 01:50 They're like, in this SIG notes, you need to make sure… no, they didn't.
I'm just being silly, as you.
**Cesar Munoz** 02:01 Hello, good morning.
**Hanson Ho** 02:02 This is our…
**Jason Plumb** 02:03 as our… Good morning.
We have an empty agenda right now.
Whoa, that is absolutely the wrong font.
And it's bold? That was weird.
Okay, yeah, this is interesting. I think I responded to this one.
Oh, yeah, is there another… is it a dupe?
Yeah, it's definitely related.
Thanks for digging this one up, Cesar, I forgot that this existed.
**Cesar Munoz** 02:51 Yeah, no worries.
**Jason Plumb** 02:53 I did ask for a specific example, I'm sure it's trivially reproduced, but it would be nice to have Like, a more fleshed-out example.
But I'm sure it's not much work, but then we can decide which one we want to keep, yeah.
**Hanson Ho** 03:13 The problem is that… Okay, well, we can discuss this, if we're gonna discuss this.
**Jason Plumb** 03:19 Well… Yeah, I was just picking up, I was just looking at issues while some agenda items were filling in.
Yeah. Okay, we can, we can jump over to agenda items.
If you're ready for us, Leonardo.
**Leonardo Serrano** 03:40 I'm ready now.
**Jason Plumb** 03:41 Okay.
**Leonardo Serrano** 03:45 Yeah, so I have two PRs. I know there's some feedback, Especially with this one. Still… I haven't taken a look at this one in a bit. I was looking for more general, like, opinions. I will go and, like, resolve some of these things, like, for example, this one with getting, like, the… number of CPU cores. Honestly, I think we can just remove this bit of logic, since this is really just used to kind of, like, attempt to normalize the CPU value, like.
You know, to be… between 0 and 100. Otherwise, you can end up with, like, values that are… 200, 300, but that's fine. I think that sometimes can be standard.
**Jason Plumb** 04:33 Yeah.
**Hanson Ho** 04:35 The Java thing… oh, never mind, go ahead.
**Jason Plumb** 04:41 Yeah, this is just… this is just a nitpick, you know, this is just, like, some basic feedback, but, Yeah.
**Hanson Ho** 04:47 I'll take… I'll take a look at this today, sorry, the last 3 weeks, I haven't looked at anything. This is a couple weeks ago, I know I'm a bit late, but I'll take a look at this, today. It's in the… Okay, cool. Agile repo, okay, got it.
Let's take a look.
**Leonardo Serrano** 05:07 Thank you!
**Jason Plumb** 05:10 Cool. Was there another one? There was another one. Yeah.
**Leonardo Serrano** 05:14 This is the CPU attributes.
Or, sorry, no, no, the first, we just.
**Jason Plumb** 05:18 Yeah, yeah, okay.
I don't know if I've reviewed… I think I haven't reviewed this yet.
I apologize for that.
**Hanson Ho** 05:26 No, I think.
I'll take… I'll take a look today, too. This is… a bit… tricky.
**Cesar Munoz** 05:33 Oh, yeah.
**Jason Plumb** 05:34 Cesar has opinions.
**Leonardo Serrano** 05:36 Oh, yeah, yeah.
**Cesar Munoz** 05:37 It's related to, CEMCOM VR, so kind of discussing the details there.
I know.
**Leonardo Serrano** 05:46 So… I spoke with Grace about this. We decided that we want to remove the nodes and depth from scope… from this semantic invention PR, as well as my implementation PR, so… We're gonna hold on that. We'd like to propose that later, but for now… Yeah, we have this whole… Screen load…
**Hanson Ho** 06:14 proposal here.
**Leonardo Serrano** 06:15 Totally.
**Hanson Ho** 06:17 I'll take a look at this one, too. There's… There's a… there's a bit of complexity involving… Android loads, because the difference between activity and window, and, when draws fire, when activity lifecycle methods fire, they are slightly, well, they're not part of the same lifecycle, so sometimes there's a bit of, interesting race conditions. So I'll take a look at all of this in detail, Today.
**Leonardo Serrano** 06:49 Great, thanks.
**Cesar Munoz** 06:50 And also, thanks for this, Leonardo. It's just that there's a lot of… Details that come to my mind.
With regards to… How, you know, how intuitive or how clear The intention of these, you know, spans, or… or events, like, one of the discussions that I have in the SEMCOM PR is.
Is the formatting, if it's suitable for spans versus events, things like that.
Also, the idea, my understanding about this.
semantic conventions change is that it's supposed to be… It's trying to define something that is platform agnostic, so… Ideally, we would like to avoid any, you know, Android-specific terms, or iOS-specific terms, things like that.
So, it makes things a bit… I mean, it would be great to have something like that, but it makes things a bit trickier.
Because then we have to be quite… I think we have to be quite clear on what does it mean, like, when a screen is loaded, right? And what does it mean when it's rendered or, you know, ready for, you know, user input, things like that, these kind of nuances.
That I would… really would like to… to have clear there. There are some resolved comments there regarding notes and depth.
that… Leonardo, if you say that you would like to added later.
I kind of will add the same comment there.
As well, because it's… it's really… So for… just… just for context, like, nodes is, like, kind of a number of UI elements on a screen.
which… I added a huge comment on that. It's one of the resolved ones.
It's kind of, like, difficult for me to kind of understand how to get this number, or How useful it could be.
And the depth… It was not clear in the sense that The description kind of mentions something that Kind of related to navigation depth, but then it also talked about overlapping depth.
And then it also talked about C-indexed depth.
So it's kind of like… it's just a bit unclear. So, yeah, I just would like to have a… Kind of like a… Like, a catch, if you will, for all of those… edge cases, like a… like a… I don't know.
A wave, a bath.
Forward.
**Leonardo Serrano** 09:37 No, totally understandable.
I think this needs to be thought of… this needs to be refined a bit more with respect to not just Android and iOS, but also potentially, like, the web instrumentation in the future.
So, thinking about it in terms of, like, web, I mean, you can think of, like, nodes as just… I don't know, if you have an HTML page with just, like, a bunch of divs, then nodes is the number of divs, and depth is the… deepest nested div, essentially. That's, like, the most simplified way to think of it.
it… There are… there is value in tracking this, in your, like… Screen load, whatever, Because these things can be relevant in, like, figuring out how complex a specific screen load was. So, if you have a long screen load span, you can sort of attribute it to, you know, UI complexity, or the complexity of the UI rendering pipeline, stuff like that.
It's an idea, and I think we want to separate this out, so… I'll… create a separate, SEMCONE PR for this.
**Hanson Ho** 10:53 Yeah.
Yeah, I have lots of thoughts, but I will, I will, I'll talk about it first in the, in the PRs.
those are… those… those mean very different things, and all the different platforms and complexity, is… in the UI performance is usually about redraws and recompose, rather than, you know, simply the size. If you could actually lock stuff in, and not re-render stuff, it's not that bad. But… Yeah.
We take a look, definitely.
**Leonardo Serrano** 11:30 Cool.
**Jason Plumb** 11:31 So this… I think the SemConf mentions app start, but your PR doesn't yet, right? Is that true?
**Leonardo Serrano** 11:40 That's true. Well, I mean, yeah. AppStart is… I mean, it's… The explicit intention here isn't to deal with AppStart. Specifically, this is the initial draw slash first draw bit.
**Jason Plumb** 11:57 And I haven't looked to see if that semantic convention for AppStart that's being proposed, how does that work with our existing startup instrumentation? Are they completely different?
Oh, yeah, this is… sorry, no, this is, this is completely navel-gazing instrumentation. This is not… at all apps start. This is when the SDK itself initializes.
Yeah, yeah, yeah. I wonder if anybody is looking at this or using this. I wonder if this is providing any value.
**Leonardo Serrano** 12:35 For debugging. I've used it for debugging.
**Jason Plumb** 12:37 You have, okay.
They're like, well, it got that far.
Alright, cool.
Anything else that we want to talk about on these two PRs? Or the SimComf PR?
Seems like they're moving forward, I am noticing just that these both have red X's on them.
This one is just due to that. This one, I think, has conflicts in the API file, yeah.
So, that'll need a rebase.
Or a merge.
But we should figure… like, this is… is this, like, every PR is getting… these now. Oh, I… Sorry, oh, it's because there's a block on this one, and this one is because of the conflicts?
**Leonardo Serrano** 13:29 The other one is a coverage issue.
**Jason Plumb** 13:32 This one is…
**Hanson Ho** 13:37 I don't think coverage issue is blocking, right?
**Jason Plumb** 13:39 No, but just when you see red there as a reviewer.
kind of makes you pause, and you're like, oh, is this one even ready? Like, maybe I should wait until they fix the… I don't know. I'm just talking through…
**Hanson Ho** 13:50 Oh, there's detect failure.
**Jason Plumb** 13:52 Yeah, so it's that thing, okay.
So these are real, and, you know, they're being called out, so that's good, right? I like it.
I just want to glance and see how many of these are red.
That's not bad. We're pretty good, actually.
That's cool.
Okay, what else we got?
**Leonardo Serrano** 14:15 Just one other very general thing.
**Jason Plumb** 14:16 Oh yeah, okay, this is a lovely can of worms.
So…
**Leonardo Serrano** 14:22 yeah, I tried my hand at doing some, like, app start profiling with Android traces, the system traces.
to get a sense of, like, what is the performance of using this client? And, oh, jeez, I wish I had, like, the actual numbers in front of me right now. Apologies, I didn't come very prepared, but, TLDR, I wanted to try to figure out, like, okay, what is causing… The most additional increase in app start time.
Because of the OpenTelemetry client.
And… One of the primary, like.
contributors was actually the, some initialization logic that happens in the OKHTTP and, HTTP URL connection, startup, instrumentation startup.
So…
**Jason Plumb** 15:26 In the instrumentation, or in the creation of the clients?
**Leonardo Serrano** 15:31 Because there's two… there's two different things happening there, right? We instrument…
**Jason Plumb** 15:35 Potentially, we instrument OKHTTP client for users, so that we can create spans, but there's also the exporter.
It's great.
Do you remember which of those it was?
**Leonardo Serrano** 15:51 I'll have to get back to you on that.
**Jason Plumb** 15:52 That… no, that's fine.
**Hanson Ho** 15:57 Are you using Profetto for this?
**Leonardo Serrano** 15:59 Oh, yes, yes, owes.
**Hanson Ho** 16:02 Yeah, next time you do it, just, you know, dump out a trace, upload it on a drive or something like that, we can take a look.
**Leonardo Serrano** 16:12 Will do, yeah.
**Jason Plumb** 16:14 So that was the main thing that you saw, was, like, something around OKHTTP was the… Kind of the main culprit, like, responsible for a lot of the extended.
**Leonardo Serrano** 16:24 Yo.
Yeah, so… I had the thought that not every instrumentation library needs to initialize at app startup. However.
Maybe some developers, you know, care for certain things to be… loaded in immediately, maybe some don't. Like, if you have an app that is immediately on startup, going to start firing off, like, HTTP requests, then yes, you absolutely do care to have this, like, loaded in at the start.
But maybe you don't care if that's not happening. So… I know this is a super… This is… I'm very phrasing this super, like, vaguely, but… I don't know, open to thoughts.
**Hanson Ho** 17:17 So, so in the Embrace SDK, we've broken down, the various parts of startup, with the SDK, into different modules, and we have load time for modules.
And typically, if it's not doing any disk access, if they're not doing any binder calls, and it's all done in the JVM layer, they tend to be pretty fast. And when it's not, it's usually an issue of class loading, or, or things that can be, you know, managed. So with class loading, you just put it in the baseline profile, and you don't have to worry about it.
you know, it's, it's gonna be way cheaper. So I would, I would suggest, taking a look at.
breaking this down, and then taking a perfederal trace and see which aspect is taking a long time in terms of blocking. I don't know what HTTP OKG would be doing, or rather the initialization would be doing, but I can't imagine it's more than creating, a listener, and then… and then attaching it. And that tends to be pretty fast, unless that's blocking on some disk read, because it needs to read preferences or something like that. And I know there's…
**Mustafa Haddara** 18:32 Doesn't the OKHCTP use, like, ByteBuddy to build some, like, class-level integrations and instrumentation? Like, it might just be doing some complicated class loading that you're talking about.
**Hanson Ho** 18:44 I thought Byte Buddy does it at, at build time.
**Jason Plumb** 18:48 On Android, it is build time. Yeah. Because we can't… we can't inject or do by-code manipulation. We don't, like, we don't have those same agents or instrumentation interfaces in Android.
**Mustafa Haddara** 19:00 Sure, but that may mean that, like, it's loading classes from a different class path or something.
They're white?
**Cesar Munoz** 19:07 Well, it's not a different class, but it does, like, it's exactly what it does is that it adds some logic into, okay, HTTP's Builder.
So that… I think it was the builder. So that it adds the… opens elementaries, interceptor.
Whenever a client is created, so… the… the class… Loaders should be the same as the rest of the app.
But it does that extra work of, you know, attaching the new Well, which is a singleton, so it's like, it's not like creating… a new interceptor every time. That's what it does, yeah.
**Mustafa Haddara** 19:48 Got it.
Yeah. Yeah.
**Hanson Ho** 19:50 So, I mean, I think profiling it would be good. Sometimes what happens is that, logic gets moved up. You know, if there is OKCP client creation necessary later down the line in the startup anyway, if our instrumentation stuff is starting first, that may be the one incurring the class load. But if we didn't do that, it'll happen a little bit later on. So, the fun of Android profiling is that you kind of have to, like, lock everything down, make sure everything is released.
You know, make sure, ideally, you have, the right, baseline profiles, instrumented, so you're not measuring, things that ought to be taken care of in real time, or in production, code. And then… seeing which section contributes to what, and if you remove it, whether it's just gonna be moved back a little bit, because it's loading share preferences, or something like that. It's the first access share preferences, so it's got to load a bunch of stuff.
A lot of times it's that. So, having the Perfetto trace and being able to kind of go in there and seeing, you know, what it's actually doing, would be, would be, would be nice.
**Cesar Munoz** 21:03 Yeah. Also, Leonardo, just have one question. The, The profiling… Like, the… the… the… What you're trying to see is how long does the main thread, you know, or how much is the main thread affected by this, or you're checking all of the threads? Because I think we do some of the initialization in secondary threads, and I'm not sure if that's something we should, worry too much about.
**Leonardo Serrano** 21:38 No, no, I'm not worried about that at all. I'm strictly looking at the main thread.
Got it. Because that is what affects, like, app start.
**Hanson Ho** 21:45 perform, like, the…
**Leonardo Serrano** 21:47 AppStart figure, I guess.
**Hanson Ho** 21:51 I don't… I know there's… I know there's several things that we're doing, in… in startup that, makes things a little bit slower, but… almost… but as you said, there's, you know, cost-benefit, right? Like, do you need it right away, and is it really worth it?
the right-of-way part is… is… is really, you know, eye the beholder. And you can overcomplicate things if you're saving.
you know, a few milliseconds here and there, but if it's significant, then it's probably worth looking into. So it'd be good to know exactly what the breakdown is. Something I'm meant to do for a while, but it's good that somebody else is looking at it, so…
**Cesar Munoz** 22:30 Yeah, definitely.
**Jason Plumb** 22:31 Yeah, it'll…
**Cesar Munoz** 22:32 Just once…
**Jason Plumb** 22:33 Go ahead, Scissor.
**Cesar Munoz** 22:34 No, I was just gonna say that there's just one thing that I know it takes a bit of, processing.
Which is… and it's related to instrumentations, which is the auto discovery, the, the service loader Java API.
Because my understanding is that API does some… Disk reading, you know, to check for the, for the service's names.
In, in the, in the resources.
that's… that's pretty much it, and I… and I'm aware of somebody, I don't know which repo created an issue about it.
At some point, but, like, it was really, like, com… I guess… It took a bit longer than the rest of the processes, but it wasn't, like, too much either, so… because it's only reading.
So… so, that's the one thing that comes to my mind. So… Just to let you know, Leonardo, if that, you know, shows up.
**Jason Plumb** 23:38 So that is… this is an interesting idea, I think, or it touches on something that we've… we've talked about before, which is… When the day comes that we have a custom Gradle plugin, we can move this kind of service loader stuff into the build… into build time, I believe. Or at least a lot of it. So, like, the question is, can we do this? Can we front-load this and avoid service loading altogether? If we just have… a concise list of services to be loaded, then you don't have to walk the class path. You don't have to go find these via service loader, right?
**Cesar Munoz** 24:10 Yeah, it's true. Yeah, it's possible.
**Hanson Ho** 24:13 I mean, walking the class path also, you know, depends how big your app is. Your app is gigantic, you know, you're gonna have even worse performance. So, yeah, taking a look at the structure of the startup via Profederal Trace.
Would be, would be the best place to start, assuming everything's locked down first.
Because you can see, like, you know, on the memory things, you can see, like, GCs making things slower, and you're like, wow, this device is so bad that it's gonna GC.
**Jason Plumb** 24:42 Also, this is a pretty good brain trust, so, like, speculating is, like, also, I think, worthwhile, you know?
**Hanson Ho** 24:48 Yep.
**Jason Plumb** 24:50 I wanted to address, this question.
And I have two things I want to touch on, because I think it is a good question. For me, the number one, the number one challenge about delaying initialization for any of the core components, or even, instrumentation, is that it makes it harder to reason about.
Like, when you're looking at an app doing stuff, if you have… if there comes a moment in time where you're like, okay, here, I know I'm done initializing the SDK, I know I'm done setting up instrumentation. If there's a moment in time, then everything after that is kind of steady-state, like, application performance with instrumentation.
If you can… if you end up deferring some of that, or make it completely dynamic, and core components can be initialized much later, it makes it really hard for a developer who's troubleshooting an app, or looking at a user journey. It makes it really hard… it makes it much harder to reason about, in my opinion, in my experience.
So… I'm just gonna make a comment to that point.
**Hanson Ho** 25:57 Yeah, story time. The Embrace SDK, for a while there, basically asynchronously, loaded the OTel SDK. We basically buffered everything until then, to, to, you know, actually record telemetry when the OTEL SDK started, because the OTEL SDK was adding, like, 40% of startup time, you know, to… or rather, 40% of the SDK… Embrace SDK startup time.
And deferring it allowed us to, you know, make things faster. But the issue is, you know, we'd have to basically know… and let the system know when it's done, and sometimes you have to block, and… And then… The logic around everything is… is a bit… difficult, to reason about. And also, if instrumentation doesn't load immediately, you don't know if you're missing instrumentation… missing telemetry, because things have deferred to load.
Or things just didn't really happen. So the, the, at the end of the day, we basically went back and said, okay, let's just tighten everything else up and, and make sure, startup is consistent, so you don't lose telemetry. Or rather, you can be guaranteed that anything that you, everything, anything that's recorded after the SDK is purported to have started up, will be, properly, or should be properly saved. And at the end of the day, you know, the SDK started up without the native bits, depending on, you know, the device, if it's like a faster device, like a, you know, one of those, you know, Pixel 5 or something like that, you know, it's like, you know, 20 milliseconds, 25 milliseconds, and that's with all the instrumentation.
So, I'd like to see how long, you know.
the current SDK starts on release, with, baseline profiles, to see whether we're talking about, let's just reduce 40 milliseconds to 30, or we're talking about 200 milliseconds to 100, because I think the former will be a lot of work for arguable… arguably 10 milliseconds. The other is 100, which is significant. So, it's good to know, like, the scale of the problem we're dealing with right now.
**Jason Plumb** 28:10 Yep.
**Leonardo Serrano** 28:13 Makes sense. I'll try to come back with you guys… to you guys with, proper trace. I was trying to… dig it up right now, but I don't think it's… it's saved in my local…
**Hanson Ho** 28:22 So you know how to just get it off the phone, right? Yeah. Oh, sorry, directly use the phone to do it, so you don't even need to connect it to anything.
**Leonardo Serrano** 28:33 Actually, I was connecting it to… Oh, no, no, I see what you mean. Yes, yes, yes, yes.
**Hanson Ho** 28:38 Yeah, just, yeah, you get the tile, and you click a button, load, you know, load your thing, and then click it again, and then it pops up dialogue, so you want to save it to your drive, and yeah, so…
**Jason Plumb** 28:49 I haven't done that yet. Yeah, it sounds so cool.
So, yeah, so this, this, like, being able to reason about what your app is doing as developers, the first thing I wanted to mention regarding this question. The second thing I wanted to mention is that I think this is, this is flirting with, this is touching on… an idea that I think we don't… talk about enough, and maybe we haven't. We, OpenTelemetry, have not yet… Done a great job of explaining or clarifying, and that is the difference between A developer who's troubleshooting app performance, and a tool that is geared at doing real user monitoring. Like, I think those… and there's… there's a course there's overlap. If you… if you're having… if your performance is shitty, your user's gonna have a bad time, right? But… There's a whole class of use case out there that's only looking at digital experience, like, what the user is… what their journey looks like, and what screens they're touching, and how long they're lingering on this thing, like, that is… The original use case for this stuff was, like, to do real user monitoring, which a lot of people just call digital experience monitoring, because I guess it sounds less creepy, but it's, like, really focused on, like, the user's experience, not necessarily only looking at raw application performance metrics, right? So… That's something that I think we haven't done a good job of differentiating or explaining, and so I'm curious, Leonardo, if you… if you're also thinking about this, or if you're primarily looking at app performance, or if you're also interested in tracking, like, user journey.
**Leonardo Serrano** 30:25 Yeah, I mean, I mirror your concerns, broadly, so this, I mean… When I initially started poking around with OpenTelemetry, like, a year ago, to me, it… it was… it was very clear… from, like, a debugging use case, and OpenTelemetry is a great tool in general for, like, server-sided debugging. But once you start thinking about it in terms of real user monitoring, I mean, there's obviously different things that matter for real user monitoring, and different things that matter for, like, debugging.
And I think this is, like, a conflict of one of those things, where, there's… certain things that matter for real user monitoring, like figuring out ways to, like, bring down app start. I'm not too sure about user journeys, I'll be honest.
Haven't put a whole lot of thought into that.
**Jason Plumb** 31:28 Yeah, I'm definitely conflating some things there, like user journey, real user monitoring, DIM, like, those are also probably subtly different things. I'm conflating those for sure, but I'm just… I'm putting that in a bucket that is specifically different I mean, there's overlap, but there's… I want to be able to differentiate it, or at least articulate how it's different than just raw troubleshooting, raw debugging.
**Leonardo Serrano** 31:49 Yeah, no, I hear you, yeah.
**Jason Plumb** 31:51 Yeah.
**Hanson Ho** 31:53 So… so I wanna… I wanna, find a video I did at JordCon Berlin, like, 3 weeks ago, that touches on this exact subject.
**Jason Plumb** 32:03 Cool. Yeah, please link it when you find it. Is it published?
**Hanson Ho** 32:07 Some of the videos, apparently, have been published, but not all of it, but I will. So… and I've actually, talked to… Cool.
about this, but yeah, there's basically two use cases. One is the traditional observability use case, which is problem discovery, finding needles in the haystack in production that you didn't know about, and finding the ability to reproduce based on that. And the other is more the traditional Android or iOS platform debugging case, which is find as much information as you can about performance, and then finding structural gaps or inefficiencies in fixing them. So tools like Profetto is especially good at the latter, because it gives you an idea of what it's doing, rather than the actual time. So the time is important in the sense that it kind of gives you a grounding of how much it is compared to everything else.
But those times are also quite flaky, depending on device and conditions and things like that. But the structure you see is what's important. So, you know, you're loading this thing that requires some other bunch of things to load, and, you know, that's what's pulling in all the slow starts. You're like, oh yeah, well, if I defer that, then, you know, it'll be better, because, you know, I don't really need it.
OpenTelemetry is just a base, a way of recording, encoding, context and telemetry into, a platform, or into, like, a common language. So you can use it for both.
But OpenTelemetry itself, I think, is designed more for the server use case, which is you're doing discovery and debugging at the same time, because when you have a complex distributed system, you can't really reproduce it. So you really have to get the data from production, in order to even understand how the different services interact with each other. On mobile, it's always going to be one device, so… As long as you're able to, like, nail down the repro steps, or find a way to basically you know, get your device to that state, you're gonna need something like Profetto to do a lot of the details. So, it's almost like observability is focused on a different problem than, traditional Android kind of debugging.
And where it's interesting is sometimes the bugging information can help with observability, because you'll be able to detect new problems. But how much are you, what's the cost of actually getting that extra information? So, I think with the previous PRs that you had about app startup, things like that, I think those are great. Being able to contextualize app startup, being able to contextualize when things start and end, that's going to be really important for observability.
And I guess looking at this issue is more, I would say.
you want to reduce the performance impact of instrumentation, right? So you don't want it to be like, I want to make things faster or more consistent, but then I incur a 300 millisecond abstract penalty as a result. You want to reduce that to as low as possible. That would be your motivation of looking into this, right?
**Leonardo Serrano** 35:16 Yes. That's… that's the point, yes.
**Hanson Ho** 35:18 Yeah, so it… so having this is… is… is, It's good. But it's almost like… this is separate from the other ones, this is almost like optimizing the Android… hotel Android package, so it's definitely good to know. And that's why, you know, dropping in, just, like, custom sections for Perfetto to take a look at. You don't even have to merge it. I mean, you can merge it if you want, but that's when we'll find the structural issues and make this better. So I think this is worthwhile doing, even if it doesn't end up in, you know, hotel telemetry. This is almost debugging. We're debugging our own tool, basically.
So, yes, awesome.
**Jason Plumb** 36:00 Totally.
**Leonardo Serrano** 36:01 Awesome, thank you.
**Jason Plumb** 36:02 Yeah.
Okay, any other thoughts from anyone else who wants to chime in on this topic?
Otherwise, I'm gonna move on to a couple of random thoughts I had along the way.
Because that's the way the brain works sometimes, especially at 8 in the morning.
So this is probably a horrible idea, and I will preface this with this.
So, concern number one is that when disk buffering is enabled, which it is by default, for good, good reason, the time between we… the time between An event being generated, or a piece of telemetry being generated, and the time that it actually gets exported on the network.
is, like, noticeably long, in my opinion.
Which is… which is fine, for the most part, because sessions are, you know.
not short, they're not… typically, they're not really short-lived, they're long… longer-lived. And there's also not necessarily a rush to get that data off the wire.
But… I think it's also a bit of a liability to have that just sitting on disk, because when the app is closed, that telemetry is just hanging out.
So, what I'm gonna… what I'm going to… to suggest, the seed I wanted to plant is… How terrible is it an idea to switch between I'm gonna call it live, like, network exporting, until we detect that the network is no longer reliable or available, which is a complicated question to answer, but there's ways to do it. And then, falling back to disk buffering. In other words.
Use the network while you got it. When you lose it, buffer when the network comes back.
get everything off the disk and go back to network mode. So, I want to plant that seed, and I'm curious what people think about this.
And they may not care.
**Hanson Ho** 38:07 So… So… oh.
**Cesar Munoz** 38:10 Well, no, I'm just gonna follow up that question, just to see if I understood correctly. So essentially, you're… Suggesting to… Choose always to export it right away, rather than… And only… and only store it in disk.
When there's no network.
**Jason Plumb** 38:32 Yes.
**Cesar Munoz** 38:33 probably, like, a Plan B kind of scenario.
**Jason Plumb** 38:36 anyways. Yeah.
**Cesar Munoz** 38:39 Got it.
The question that comes to my mind with that approach will be… will be… I mean, the thing is that it seems like it… It's based on… I mean, it's trying to target the network issue as the only issue.
You know?
And I think there might be other issues.
Okay. Where, you know, that approach might not be ideal. So, you know, it's… they are getting… stopped by the OS, things like that.
**Jason Plumb** 39:15 So you think in the case of disk buffering, the app getting stopped by the OS is better handled with disk buffering than with network?
**Cesar Munoz** 39:23 I think… yes, because storing in disk.
In theory, it should always be faster than… Sending stuff over the network.
So…
**Jason Plumb** 39:36 I see, for, like, completeness, like, because it's, like, milliseconds or microseconds to put something on the device storage, but it's tens of milliseconds to get it out on the wire. That's a difference, and you're like, well, if the apps being killed by the OS.
and I'm mid-right on the network, it's probably gonna fail, but I'm almost never mid-right to disk.
Like, I think I understand what you're saying. Is that… is that right?
**Cesar Munoz** 40:05 Yeah, well, that's… yeah, that's what I meant.
**Jason Plumb** 40:07 Okay.
**Cesar Munoz** 40:07 And Tori Hanson, you were gonna say something.
**Hanson Ho** 40:10 No, I was just gonna agree. It, it… the first thing we need to do is make sure it gets saved, and then getting it off the device is almost secondary, just because there's too many things that can go wrong during a network request. And when you disk write, when you fail, you know right away. So, I mean, you can always have somebody go and delete it, but, you know.
you can't really control for that. So persisting it first, and then sending it From there, is… is always gonna be the safe thing to do.
**Jason Plumb** 40:45 But what you've done, though, is I think you've kicked the can… I mean, so yes, having this… having this, like, queue, this backlog of telemetry.
is great, but it's great, but it's not great because it's just sitting there and no one can use it until it gets on the wire and goes out. So you've kind of deferred the problem a little bit. You've kicked the can down the road until hopefully the app is launched again, and hopefully when the app is launched, it has a reliable enough network that it can start exporting again.
**Hanson Ho** 41:13 I mean.
**Jason Plumb** 41:13 And then that same problem exists, right?
**Hanson Ho** 41:16 Oh, yes.
**Jason Plumb** 41:16 Killed while it's exporting.
**Hanson Ho** 41:19 Yeah, which is why, you only delete when it's exporting, or when you confirmed it's exported. So basically, having a stable network is always going to be, you know, a prerequisite for getting data off.
It's almost like what the failure mode is if you fail to deliver. With, with disbuffering, it'll just be, well, next time it's available, I'll try again.
You know, not disbuffering, it's like… it's gone. And the problem with that is… it tends to be those situations where you want the network data, or you want the telemetry the most, is when the device is dying, or, you know, whatever it is. So, having it a little bit delayed, is better than having it, not at all. It's at least more consistent.
So, and, and, and even, like.
like, even if you say, hey, you know, we want to deliver… so if the issue is that there is telemetry there that we know we can send out, but we're not, then I think we should look at a better way of re-initializing, or retrying. So, one thing that we do at the Embrace delivery layer is when you go from no network to back-to-network, we basically trigger a resend of everything.
And when we, don't have a network, we don't even try to do it, we just kind of buffer it to disk, and basically when it comes back next, it kind of goes up and then wakes up and does ascending. So if there's… there's this…
**Jason Plumb** 42:45 I think we have that, too. I think the disk buffering module does… looks at the… or… I take it back. It's in Contrib now, so there's no Android code in there.
**Hanson Ho** 42:55 We can certainly write a piece of Android code.
**Jason Plumb** 42:56 Yeah, yeah, yeah, we're like an interface that's like, get with network condition, or something, like, yeah, okay. That's something we're thinking about, though.
**Mustafa Haddara** 43:07 Can we, like… I agree with you, Jason, that the delay on the disk buffering is… is pretty long. Can we consider… like… Switching to a model where… If there's nothing… like, adjusting our logic so that when we have stuff saved in disk.
We, like, looked to send it out.
Immediately, or sooner, or reduce that delay.
Would that mitigate the problem a bit?
**Jason Plumb** 43:40 Sorry, can you say one more time? I was typing other notes, and… Still sleepy.
**Mustafa Haddara** 43:45 No worries. I, I think… Like, coming at this from the, okay, turning on disk buffering is valuable, but the delay that you get between an event being generated and it actually getting exported is…
**Jason Plumb** 43:59 high.
**Mustafa Haddara** 44:01 can we…
**Jason Plumb** 44:02 We can keep the same logic of…
**Mustafa Haddara** 44:05 Write to disk first, and then export, but can we reduce the time, or change the logic so that, like, the first event, if there's nothing being exported, we just export right away?
Adjust our debuffer… debouncing logic, essentially, so that… Things go out sooner?
**Jason Plumb** 44:22 That's a good question. I don't… I think that's configurable, right, Cesarea?
**Mustafa Haddara** 44:26 I think the timing is configurable, but there's still, like, a… Like, it defaults to 30 seconds.
**Jason Plumb** 44:33 Okay.
**Mustafa Haddara** 44:34 And it won't send until… like, I think the way it works is you have events, it writes it to a file, and then it won't do anything for… until… The 30 seconds is over, and then it'll export everything that's in that file.
**Cesar Munoz** 44:48 Yeah.
**Jason Plumb** 44:49 Oh, min, min H for file reading.
**Mustafa Haddara** 44:52 reading.
**Jason Plumb** 44:53 This is when exporting, right? 33 seconds?
**Mustafa Haddara** 44:55 Yeah, yeah.
**Jason Plumb** 44:57 And I think…
**Cesar Munoz** 44:58 Just try and avoid, you know, clashing You know, writes and reads into the same file.
**Jason Plumb** 45:03 Yeah.
**Mustafa Haddara** 45:04 Yeah, which is… which is… like, definitely a strategy, like, okay, you write into this file up to 30 seconds, then you wait another 3 seconds, and then, okay, now you're allowed to read from that file, but it means you're not gonna get your telemetry for at least 33 seconds, 35 seconds, right? And if it's… like, it's very possible that the session doesn't even last that long. People open the app, they tap something, they close it, you never get anything out, right?
**Hanson Ho** 45:31 Well, when we close the session, that should flush it, right?
**Mustafa Haddara** 45:36 I don't think it flushes.
**Hanson Ho** 45:37 Okay, so maybe…
**Cesar Munoz** 45:39 I think what we do is that every time the app launches, it reads whatever is already there and sends it right away.
**Mustafa Haddara** 45:47 Sure, but there's a max age, right? The last bullet point, 18 hours. So, if I, like, have a habit tracking app that I open once a day at night.
**Jason Plumb** 45:57 my telemetry's never gonna get emitted, right? I open it, I check off my box.
**Mustafa Haddara** 46:01 Like, oh, yeah, I, you know, worked out today, cool. And then close it.
That telemetry's never going anywhere.
**Jason Plumb** 46:10 I mean, you…
**Cesar Munoz** 46:10 I mean, it's all configurable.
**Mustafa Haddara** 46:13 Well, that's really…
**Jason Plumb** 46:13 Or, like, you know…
**Mustafa Haddara** 46:15 Yeah, but I think we should configure… we should adjust these values by default.
**Jason Plumb** 46:22 I…
**Mustafa Haddara** 46:22 And I don't know how much of this… these configurable values we expose to our clients.
**Jason Plumb** 46:27 So using… using time for this is… is… has always, like.
made me a little twitchy. Like, like, delaying 3 seconds from file creation, because creation doesn't necessarily mean that the file isn't still being written to, like, those are different things. The way that I've handled this… a long time ago, because I'm very old, is that you would write to a file with a different name, like a temp suffix or something, and when you're done, like, after you've closed and you've completed writing, you rename that file. There's still a race condition there, because what happens if the app dies, like, between the temp file being written?
And the rename, there's still a race condition there, but I mean, these are basically unavoidable, you know, without really complicating things. Anyway, that approach versus the timing allows you to read the file. As soon as you see any file with the matching pattern, you can just read it instantly. Like, you know, because the rename is basically atomic.
**Hanson Ho** 47:23 Yeah, that's what we do in the Embrace SDK.
**Jason Plumb** 47:26 Rename.
**Hanson Ho** 47:27 Yeah, so we also make sure that, like, in the middle of writing, it's not gonna have… we're not depending on the library to deal with overwrites, so we actually write to a different file, do a rename, double check, and then send it out, and then do the thing back.
So, we avoid this. Here, we could basically use, the, the timestamp as, like, a token to basically say.
You know, this is a unique name of the file, and then when you do the write, you have a new file, you start a new one, and, you know, when you read off a thing, and you can use, you can use, you know.
naming conventions, to basically denote these are files that existed before, or if you're using timestamp, you can even, like, reason about, you know, by what the timestamp is, for the most part. So… so I think the problem you're saying, if we don't flush when we background.
Like, if the only way of flushing is after 33 seconds.
Then we probably should look into tweaking some of these values, or modifying some of the logic to do the renaming, or rather, write to a unique name file, with some pattern, as… as a way of go… wait, the way to go.
**Cesar Munoz** 48:46 Right now, the… just for the record, the names of the files are just the timestamp when they were created. That's the… that's the name.
And that's how… This buffering checks, you know, which file has, you know, what's the age of the file.
So it's not like… it's not like… it's not like there's… there's a timer or anything like that, no. It's just checking the file names.
**Jason Plumb** 49:11 Yep.
It's not even checking the stats on the file, it's just, like, getting… it's just looking.
**Cesar Munoz** 49:16 Yeah, just get in the name, yeah.
**Jason Plumb** 49:18 So, cool, like, like everything else, I mean, help wanted on this stuff, like, you know, the more the merrier, but… Cesar, are you still working on the API changes?
I forget.
**Cesar Munoz** 49:27 I think all of the changes are already merged.
**Jason Plumb** 49:31 Okay.
**Cesar Munoz** 49:31 I'm curious… like… the, the quickest.
that I think we could do to address this concern.
Is to override the defaults.
Right now, there's no…
**Jason Plumb** 49:47 In our… in our use of it, in Android's use of it.
**Cesar Munoz** 49:50 Yeah.
**Jason Plumb** 49:51 Yeah, yeah.
**Cesar Munoz** 49:52 Okay. There's no way right now, Mustafa, regarding to your question, right now there is no API that we expose in Android, at least the initializer one.
for users to override these values. So, we could, at least initially, set our own Android defaults And that will be for everybody.
And that could be a start.
**Hanson Ho** 50:19 Is there a flush?
**Jason Plumb** 50:21 So is this true, though? Like, disk buffering config is no longer user-facing?
We hide that.
**Cesar Munoz** 50:26 is… It's not user-facing for the initializer, but it's probably… there for ROM Builder.
**Jason Plumb** 50:34 Yeah, of course.
**Cesar Munoz** 50:34 Sorry, Hansen?
Do we have a manual flush?
**Hanson Ho** 50:40 So, so instead of waiting sec… 33 seconds, you say, hey, I wanna… I wanna send telemetry now.
**Cesar Munoz** 50:47 No, we don't.
Because… Each… if you do that, then… The file that it's currently being written, 2.
It will have to, you know.
Come to a stop, like, like a hard stop at the moment.
And so that any other new telemetry that comes in afterware has to create a new file.
So it will have to, you know, become processed kind of like an emergency button that will kick off other stuff.
So, no, right now, ideally, the timing just helps.
You know, mixing different processes into a single bot.
Because I will… that will make things quite tricky, to be honest.
**Hanson Ho** 51:32 So, why don't we create an issue or two, to track what we want, and then… and then somebody can pick it up, if they have time, because I think it'd be… it'd be useful to… to have a way of… of controlling and say, hey, we want to lock this down now and flush what we have, for cases like that.
**Jason Plumb** 51:50 Are you… are you, are you offering to do that, Hanson?
**Hanson Ho** 51:52 I will… I will create an issue about the manual flush, but if there's anything that you'd want to see, Jason, then you can create.
**Jason Plumb** 52:00 Yeah.
Yeah.
I will create one about the timing thing, maybe.
Whatever. Okay, so we're… in the interest of time, we only have, like, 3 minutes left, so I want to just, I will skip over this thing, but I wanted to call it that we have… Oh, that's not… I think this means something here, let's see.
Yeah, this… so, I was reminded of this recently.
when looking at something else, and this has been out there for a long time, and help wanted. I just wanted to remind people that this is a… I think that this is a pretty cool feature, for users, developers, to be able to wrap their own methods with, like, to automatically create a span and to have bike code weaving that does that for them.
We don't have it yet. It's used pretty heavily for people doing manual instrumentation on the server side, like, people that are using the SDK or the agent, like, use this, so I don't need to say much more about that, but the thing I did want to bring up, too, before we're out of time, is that, instrumentation we'll be releasing this week.
And that's our main dependency, so we will be releasing after that.
probably next Monday-ish, Monday, Tuesday, somewhere in there, and I think we've agreed that that'll be our first release candidate.
Right? RC1?
October? Is that what I told people in a blog post? I think so. We, We have this feedback issue, and it's got a little bit of traction, but it's… I haven't seen anything in the last few days.
Yeah, it was just like… so we've gotten some.
But nothing… I don't think there's anything super strong. I haven't seen anything that's like, we love the current… API, I hate the current API, it's, you know… A little bit.
And, Severin chiming in early and saying, we need docs.
So, I'm… I've been trying to get to that for, like, a week, and I haven't yet, but I hope to, you know.
Hope to this week!
Anyway, release candidate, next week is the hope. And I also need to, verify locally that if I put a release version… some of this stuff is really… some of the release process that handles or does stuff with version strings might be sensitive to putting an RC suffix in there. So I need to do some… additional checking, and I could use another set of eyes on that stuff.
if anyone else wants to take a look at the GitHub workflows and the scripts that are used by them for the release process, to make sure that having an RC1, RC2, RC3, whatever it might be, in the version string doesn't screw up the process. There's probably some regex that needs to be… tweaked a little bit to handle it, but I'm not sure yet. Like, I haven't been able to look, so… I would appreciate it otherwise.
**Cesar Munoz** 54:56 Yeah, I'll have a look at that.
**Jason Plumb** 54:58 Thank you.
**Cesar Munoz** 55:00 Sorry, I didn't hear, from the beginning, but, just wanted to mention that I think We are… in a… in a great position to go with the first RC. I just… the only thing I would like to see, and I don't know if you already mentioned it.
is, the changes that… that Jamie… Proposed…
**Jason Plumb** 55:29 Yeah, they're not merged.
**Cesar Munoz** 55:29 Latest PRs.
**Jason Plumb** 55:31 So this one…
**Cesar Munoz** 55:32 SL stuff.
**Jason Plumb** 55:33 And this one. Yeah, these two, I think, are both important.
**Cesar Munoz** 55:36 Yeah.
**Jason Plumb** 55:38 Yes.
**Hanson Ho** 55:39 They're approved, so…
**Jason Plumb** 55:41 They… Well, I approve them, but, you know.
**Cesar Munoz** 55:44 Anyway, I think because they're quite big changes.
**Jason Plumb** 55:46 It looked like maybe you were waiting on me for this one, Cesar, but, because I haven't reviewed it yet. I mean.
**Cesar Munoz** 55:52 You know, for…
**Jason Plumb** 55:53 Yeah, it's good.
**Cesar Munoz** 55:54 big changes to the API, I would rather not be just, you know, a single approval.
**Jason Plumb** 56:00 Yeah, no, I agree.
**Cesar Munoz** 56:00 Agreed, I agree.
**Jason Plumb** 56:03 And, I think this one I looked at… Maybe?
Nope. Okay, I will do that today.
Those will probably go in.
I remember having looked at them, but I didn't submit a review, so… Here we are.
Cool.
**Cesar Munoz** 56:20 We made it.
Yeah.
**Jason Plumb** 56:25 Well, it's an exciting time.
**Hanson Ho** 56:27 Awesome.
**Jason Plumb** 56:28 Yeah, I think ClientSig is coming up this week, is that true?
**Hanson Ho** 56:31 Yes, I don't know if there's an agenda. I'll be there, but I'll be there by 5 minutes late, so…
**Jason Plumb** 56:37 Okay, I have something I'm gonna bring up.
**Hanson Ho** 56:39 Cool.
**Jason Plumb** 56:40 Okay, see you there. Thanks, everyone. Bye.
**Cesar Munoz** 56:42 Hi, thank you.
