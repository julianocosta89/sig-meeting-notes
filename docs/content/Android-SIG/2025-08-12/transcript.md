SIG: Android SIG
Date: 2025-08-12
Duration: 58 minutes
============================================================

## Zoom Recording Transcript

**Jason Plumb** 01:24 Hello, everyone.
**GZ Gregor Zeitlinger** 01:29 Hi, Jason.
**Leonardo Serrano** 01:33 Hey, hey, no.
**Jason Plumb** 01:44 We'll give it another couple seconds.
**Hanson Ho** 01:53 Hello?
**Jason Plumb** 01:57 Hello!
**Cesar Munoz** 02:02 Hello.
**Hanson Ho** 02:05 This is Earth.
And Jason, I guess, and everybody else.
**Jason Plumb** 02:26 Alright, let's, let's go ahead and get started. Please add yourself to the attendee list, and if you have any agenda items that are not yet represented, feel free to add them.
Looks like Leo's up first.
**Leonardo Serrano** 02:44 Yep, I have added 3, issues.
Sorry for just rapid-fire, like, putting these out here. These are all things I just would like some opinions on before I…
You know, start… doing some formal prototypes and submitting some PRs, but essentially, yeah, I…
these are just a couple of… it's like a big wish list, right, of things that can help, with the exception, I guess, for the last one. Like, that one's a more… that one's kind of a different story, but…
I was just having a play, like.
I've been playing around with OpenTelemetry Android, and I've been trying to answer a few things, like, okay, can I…
onboard this to an Android application and start to get value out of it, like, out of the box. And when I say value, I mean value in the context of, like.
performance monitoring, for real user sessions. And one of the things that I think is missing
are draw signals, so… This issue that you have open is describing two standards that, the…
Android Vitals documentation establishes TTID and TTFD.
DTFD might be a little… I'm not too sure about implementing that, but…
Yeah, TTID, in a nutshell, is the time diverse draw, which is actually a
I think that that has a…
Analog on the web, as well.
Like, a web vital for that? …
Basically, you know, I'm talking in this issue about how this can be done, you can register a
add-on raw listener for the view tree observer. My question is, and I guess this is the same question for…
all three of the issues that I have here.
What is the scope of this…
repo. And does it make sense to include things like this?
**Jason Plumb** 04:55 My short answer is yes. I think it would be in scope. We don't have a nice, clear, written statement about, kind of, what the boundaries right now are, or even, like, the long-term vision for what this repo needs to become.
We could do better with that.
Historically, this, …
like, if you kind of don't know the history, Splunk donated this as RUM instrumentation, so it was very specifically geared at real user monitoring, looking at a user's flow, and determining, what a user did in a given session.
And less about application performance monitoring, but certainly, the behavior of the application and timings and performance
relate to user behavior, and so an app that is slow to render or takes a long time, they might… they might do something differently in the cases where it rendered slowly versus the times that it rendered fastly. …
So, I think… for me, I think it's definitely in scope. I think having an event that indicates how long it took till the first paint is great.
Curious what other people think.
**Hanson Ho** 06:09 So, the Embrace SDK, which kind of went the other way, it started off as more of a, tracking mobile performance and stability and all that stuff, and then we moved to OpenTelemetry. So we have, metric, or we have data like that, collected,
So, the Embrace SDK is similar to the Openet Telem2 Android in the sense that it wraps, a language SDK, provides some measure of platform smoothing, for Android and, you know, other things. And then does both,
auto-telemetry collection, auto-instrumentation, as well as providing APIs for you to do manual, for bespoke things.
the way I see it, eventually, where I want, kind of, OpenTeleNetry Android to be, and OpenTele… and embrace Android, is that they both
share an API, that is kind of like a, I don't know, Android platform shim, and providing a bunch of common services, so that
we could upstream some of this, some of the guts of this. …
including in that is instrumentation for app startup and time to first draw, and things like that. But, unfortunately, it depends on that layer of Android that differs depending on what version you're using. So, if you look at the Embrace,
implementation of, App Startup and UI load. There's a myriad of different factors determine what could be recorded, depending on the Android version.
So the instrumentation, will require either handling of these version-specific peculiarities, or depending on API, which does that for you.
So, to move forward with this, we either build it in
right now to OpenTelemetry Android, or start doing this API extraction so that we can have instrumentation that sits on top of and outside of, you know, whatever agent is using it. But
which could offer up APIs that the instrumentation could use, so that we can build things like this without having to do all the shim and all the underlying, version, mess, that you otherwise would.
So, …
I think, depending on what specifically you're talking about, the level of, sophistication for the shims is gonna be a little bit different. Even the on-draw stuff is… is… is not…
quite the same. You could… like, if you use Compose, for instance, TTID fires very quickly, almost immediately, before anything loads. But if you want to do, draw detection, you have to look at the tree observer, which is…
a little bit… which is tight the window, and not with the activity. So, …
it gets a bit complicated, just because of the API we're dealing with, and depending on how reusable this is. So if you want this to make this implementation
only tied to this package, or usable by anybody without having to use, you know, OpenCenter Android, then you would kind of do something else. My… what I want is the latter, but we're… we're not quite there yet.
**Leonardo Serrano** 09:40 Gotcha, okay. Yeah, I ran into similar peculiarities with, like, versioning.
I think the add on draw listener, there's… there's… yeah, I encountered some… I have been trying to, like, prototype this myself in an environment to see, like, what can work, and I ran into issues with, like, API versions under, I believe, 26 have some weird things, and they behave differently,
Yeah, I can't speak to, like, how exactly you want to, like, what it… how do you want to make this, like, consumable and extendable, you know, outside of OpenTelemetry Android? I haven't really thought about that, in all honesty.
**Jason Plumb** 10:22 This is good.
**Leonardo Serrano** 10:22 Feedback, then.
**Jason Plumb** 10:23 No, I think having it in OpenTelemetry would be great, that way people can iterate on it and continue to make it better over time. And also, I asked this question if it can handle all different sorts of cases, like if there are apps that don't have activities or whatever.
But honestly, I don't want that to be a blocker. I think if we can… if we are providing instrumentation, or have available instrumentation.
That is helpful to even, you know, half of the users out there who are interested in this, then it's better than nothing.
So I would, I would opt for, yes, I think this is a good issue. Cesar, do you know if your distro measures time to first draw?
**Cesar Munoz** 11:00 No, not right now.
**Jason Plumb** 11:02 Okay.
**Cesar Munoz** 11:02 There, there's… the thing is that there's many ways, and probably… many variations across APIs and, and, and…
Also, it's difficult to actually get the right
Place where to, you know, start counting, where you… if you want to check how long it takes.
That… I mean, right now.
What we're trying to do is just wait.
to… See what a customer might need, because, you know.
I mean, the thing is that there's so many variations, and many… so many ways we can gather this data.
That, we can spend a lot of time trying to figure out what's the best way, and And…
It kind of feels wasteful, unless we actually have a use case
For a real, real-world use case.
So, I don't know, it's, …
I mean, I'm open to suggestions, but yeah, right now we don't… just waiting to see how can it be useful for anybody, which we haven't gotten.
**Leonardo Serrano** 12:16 Yeah.
**Cesar Munoz** 12:16 That kind of feedback yet.
**Leonardo Serrano** 12:18 Good point, about the use case. I…
That is also something I'm not 100% fully convinced of, but thinking about it logically, like.
I think there can be, right? Like, this can measure if there are any delays in your UI pipeline, like… so I… there's some Android documentation that describes, like, the steps that
your UI pipeline takes before, like, the first draw is rendered, there can be delays on that, and there can be certainly some actionable signals you can get from, like, a delay in that.
Something to play around with. I'll… I'll play around with this.
**Jason Plumb** 12:57 Yeah, I….
**Cesar Munoz** 12:58 Yeah, no, definitely.
**Jason Plumb** 12:59 I think there's value there.
**Cesar Munoz** 13:01 I'm also glad that
You know, we're talking about this stuff, because maybe… maybe if somebody has a use case, they didn't know where to talk about it, and now, you know, there's a place for it, so….
**Hanson Ho** 13:12 the main use case that we found is through navigation, specifically an app startup. So I linked in the doc kind of our implementation. It's a bit complicated, maybe it could be simpler, but, we gather the data on app startup, various points. When we determine app startup to have ended or have been abandoned, we say.
Go ahead and log a trace.
And with this information, we're able to basically, …
you know, recreate, based on the data points that we have, what happens. So we have to deal with,
cold start versus warm start. So if the process has been created before, depending on the version of Android, you have different information about when the actual start is, etc, etc, etc. So, …
this instrumentation requires that level of dealing with, and if there's an agent API that basically tells you this information, then the instrumentation is basically just building off of that and recording, you know, whatever telemetry you want to record, a span or a VN or whatever. So if…
taking a look at what you want in terms of the use case, and kind of just paring it down to something simple that you don't require a ton of things. So, for instance, if you just want something to fire an event for,
TTID, or, sorry, TTFT, or not, it's not like TTFT, but whatever, the report fully drawn one, you can always add a listener listen for that, and then, and then, you know, fire an event, and say, this is the time that first drawing was reported. That doesn't require,
complicated support of, you know, various other timestamps. All you need is when that is invoked, you log an event. And it'll be a start. You can't really quite calculate much with it, because you don't have enough starting point, but it's a start. And then you can kind of build on top of that, depending on what you want to do.
**Leonardo Serrano** 15:14 Brute, okay.
**Jason Plumb** 15:17 Yeah, to that same point, yeah, I'll stop after this, but, I think, …
just, like, starting with small and getting something that kind of works and has, like, a consistent place that we're measuring to, I think is a good… is a good way to start, and then we can revise as needed.
**Cesar Munoz** 15:34 Also, I think if we come up with a solution that it's available
from a quite newer version, newer API version, but not for older ones. I think it's also worth
Starting with… adding only support for these newer APIs, and then if in the future somebody requires that
Functionality for older ones, which is…
If it's possible, it's most likely it's gonna…
Take a lot of work to… to… Gonna make it backwards compatible.
then we could… we could do that, but, like, just in case, you know, somebody wants to, create a PR, and they… they are… they may be…
I don't know if, … Worried about the fact that they will have to
build a lot of code that… to make it compatible with all of the APIs that we're supposed to support, which is from 21 onwards. I don't think that's the case. I mean, we… for me, starting small, as Jason mentioned, could also be just starting with whatever is available, even if it's only available
from newer APIs onwards. So yeah, if that makes sense.
But yeah.
**Jason Plumb** 16:53 Alright, should we move on to the next one?
**Leonardo Serrano** 16:58 Yeah, yeah, let's do it.
**Jason Plumb** 17:00 Okay.
Monitoring relative CPU utilization for client spans.
So….
**Leonardo Serrano** 17:06 Yeah, this…
This is an odd one. This, to me, sounds like, as I was thinking about it, the responsibility of, like, a metrics exporter, right? You'd want a metrics exporter, in theory. I think this is how it works in the backend side of things.
to periodically sample CPU utilization for a process, or thread, or core, or whatever unit of whatever, … Which…
It's great, and that can work, but it can't really give you, like…
per span approximate relative utilization, like, given the actual duration of a span, what was the sample of CPU utilization for the process?
Given that, you know, Unit of work that was done, which is the span.
So this one's more of a…
It's a little more out there. I'm not….
**Jason Plumb** 18:01 I'd appreciate it.
**Leonardo Serrano** 18:02 opinions.
**Jason Plumb** 18:02 Yeah, I think… I think your idea is, I want to see, how much load this… this request, this client span is, like, putting on the system. Or, like, what was the impact of this client span?
Like, how much CPU did we waste doing this one operation? Is that….
**Leonardo Serrano** 18:20 Exactly.
**Jason Plumb** 18:20 Thinking, yeah.
Yeah, that's a very tricky one. I don't think, in general, across OpenTelemetry, we… I don't think anywhere that I've seen yet do we have a good way of measuring, like, per operation CPU. And that's because those two things are very different. Like, a single client span
might execute across several different threads, right? It might even spread across cores. Depending on what framework and what you're doing.
… And so… and there could be multiple spans concurrently operating across that pool, of course.
So, determining in a meaningful way which one belongs to which, and how to attribute that to a given span and not something else, I think is…
you know, pretty, pretty tricky. Curious what other people think.
**Hanson Ho** 19:12 There's also the fact that there are other processes running outside your control, within the OS. There could be Spotify playing, there could be YouTube playing.
you could be throttled because your battery is low, so your… the CPUs are operating at 50%. And also, you can't really get CPU information directly very easily, very reliably. Reading the proc files, not gonna help. There's a new API, that's available 35+.
That gives you a bit of perfetto tracing, in production, but the data that it generates is quite voluminous, and also in an opaque format that you can't pull out.
you basically… it generates… it basically takes a very simple, or, you know, a very redacted profile of the process, and gives you very detailed information about it. But then processing that is… is hard. And again, like Jason said, attribution is, nearly impossible.
**Jason Plumb** 20:12 But maybe, maybe attribution is not the goal here. Like, maybe the goal is you have a client span that normally takes 30 milliseconds, and this time it took 80, and you're like, oh, why did that happen? And you happen to also see that the CPU spiked.
Like, maybe…
Maybe you can kind of flip that around, and you don't necessarily attribute it to the span, but you can at least say, well, my client span
was slower than normal during a time at which the CPU was much higher than normal, so maybe it caused it, or maybe it was a symptom of the CPU being spiked by something else.
I don't know.
**Leonardo Serrano** 20:45 That's my.
**Jason Plumb** 20:45 Like, I was wondering what Leo was thinking.
**Leonardo Serrano** 20:48 Yeah, that's my thought. So, I was playing around with cases where, like, I have an app, and I do something silly, like, I create, like, a… like, a massive for loop inside of the onCreate, logic.
And in cases like this, then your activity, life cycle spans will actually be
delayed. You'll see a longer duration for, like, onCreate, or, like, whatever, … We created spans, etc.
It's, it's very difficult, if you're just looking at, like, the spans,
it's very difficult to attribute that to anything. Like, okay, what do I do about an increase in the create spam? I can't really do much with just the information provided, so…
CPU utilization, can help you at least understand, like, is something in the process, which might not even be the current thread that's executing the span, but is something in the process potentially delaying things?
**Jason Plumb** 21:49 Yeah, that's an interesting… go ahead, Cesar.
**Cesar Munoz** 21:53 I would love to have this Possibility of having this information.
I just don't know how.
We can get it.
In it for two reasons. I mean, if there was a way.
I'm up for it, but … Here's the prototype. Maybe there is.
My, my point is that… I…
The reason why I'm saying this is because of two things, one of which I'm not fully sure, so I'm gonna ask the question here.
The first thing is what… …
it's basically what Hanson mentioned, which is that usually the Android OS APIs are not
Flexible enough to provide, like, a lot of information on this.
And also that maybe the information that you might get, if you happen to get something.
You know, might not necessarily… Any correlation with the…
with the stuff that you want to measure, or with your application in this case. So… so, in that case, it kind of seems like even if we manage to get information, it might not be
Accurate information for you.
As a, you know, after you're looking at the data.
But apart from that, let's say that… that we… we get… we get it.
… My understanding, and this is where I'm not sure.
Is that this kind of information
generally speaking, in OpenTelemetry, it's captured Using metrics, if I'm correct.
And so….
**Leonardo Serrano** 23:28 Correct, yeah.
**Cesar Munoz** 23:30 Got it, so… So this is interesting, because I'm… I'm not aware…
of an existing mechanism in OpenCelementary that would allow you to kind of match … metrics to…
to other signals. I mean, we can do that with logs and spams.
But I think metric is kind of like the…
exception here. I'm not sure if that's gonna change in the future, but probably, if somebody's looking for
a reason?
to push this upstream, to have this kind of, like, relationship between metrics and other signals. I think this could be a nice
Use case example, if that's happening again.
**cleverchuk** 24:19 There is exemplus.
**Cesar Munoz** 24:23 Sorry?
**cleverchuk** 24:24 Examples.
**Jason Plumb** 24:26 exemplars.
**Cesar Munoz** 24:28 Exemplary.
**Hanson Ho** 24:29 Exemplars are about samples, so you basically have to basically have an interval. It doesn't actually tell you when it's happening or what device it's happening on. So the problem with this API is it's not actually measuring CPU time, it's measuring how long the process has run.
**Jason Plumb** 24:46 Right, that's why I pulled this up. I was like, is it actually, like, CPU time, or is it, like, clock time?
**Hanson Ho** 24:52 Yeah, and there's a lot of factors that affect this. They typically don't, affect.
It typically is not that the span is doing more work, it's things like GCEs happening. It's things like you've been… there's an app running in the background, so the data you get from this is very noisy. Even from one device, it can be difficult to compare different instances of launches. You could have a new app start up, and the cloud profile isn't ready, so it just takes more time to
do class loading. And when you aggregate this across the fleet, this number is gonna be… like, unless you're making gigantic changes.
You're… there's gonna be so much fluctuation that the data you get, even if you can get this, is not going to be, super reliable or consistent.
Looking at other signals that the app could potentially get is probably more useful to be able to, tell you what's going on. And also, unlike back-end data, you don't necessarily need,
You don't necessarily need the data itself,
for debugging. The data is most useful to identify issues, and debugging tends to be… you could tend to be able to do it with, a reproduction case, because we're just talking about one device. We're not… we don't need to set up a complicated distributed system, you know, to have a certain load in order for… to generate, you know, certain conditions where you can reproduce.
To, to find structural issues, you could use, Perfetto. so if you're doing a more… if you're doing, like, a binder call on the main thread or something like that, in a new version, and, and what you've detected in your telemetry is that, there's a 20% increase in some spans,
you know, runtime. You kind of plug in the version, take a perfano trace, and, you know, look at it, and determine structurally what's wrong. So that tends to be the debugging use case, and not through fine-grained data like this.
So, I just have not encountered any measurement of CPU, that…
Does very much to help solve problems.
Or to even quantify potential issues. The delay or the increase in time is
is a good indication. And for debugging, you kind of have to look at things in detail, because sometimes it only affects a certain type of device, or certain types of architecture, or something like that, so….
**Jason Plumb** 27:18 I've never used this API, but I was like, we should look at the docs, and that'll make it clear. This is no clearer after reading these docs. It's like…
It doesn't actually tell you. The fact that it's from API level 1 is maybe suggestive of it being, like, a long history, and they don't want to get rid of it, but it doesn't tell you it's, like, time on the CPU, it's just telling you the time…
like, elapsed time that the process has been around? Is that the way to read that? Yeah. I don't know. Anyway….
**Hanson Ho** 27:51 And depending on… depending on the OEM, that could be different.
**Jason Plumb** 27:54 It's huge.
**Hanson Ho** 27:54 if you're doing, you know, pre-creation. So, …
you can't even know what core, if it's a multi-core architecture, you can't even know what core, you're running on. So, you can't even benchmark. You can have, like, one span that at one time was assigned a crappy core, and one time assigned a fast core. And you're like, wow, it's faster this time and slower the other time, you know, why?
Nothing has changed, everything is the same. Well…
sometimes, you know, the scheduler says, you get a fastcore, because we have one free. Sometimes it doesn't. And… and you can't even get this information. So, this level of detail is
difficult to get on Android.
**Jason Plumb** 28:35 Leo, it sounds like you kind of knew this one would be weird coming in, so I appreciate you.
**Leonardo Serrano** 28:38 Yeah.
**Jason Plumb** 28:39 Discussion.
Yeah.
**Leonardo Serrano** 28:42 Yeah, I totally get that. There's two issues, right? Yeah, there's, like, the semantics behind, like, actually collecting CPU metrics in a span, which I recognize that is, like, super, super weird, but I don't see, like, a better alternative for relating metric data with
span data, but that aside, I totally agree. I'm not super confident the actual, like, utilization information
In the context of spans, would actually help anyone relate any issues to, like, you know, what's actually happening in their telemetry.
I… Yeah, go, go ahead.
**Hanson Ho** 29:23 Oh, what's probably more useful is if you took, call stacks.
Throughout the life cycle of the span, and just to kind of sample what the hell it's doing, and then aggregate that. That's what, in the Embrace API, or the Embrace, in our detection, this is what we do, so we can actually create, flame graphs, to see, oh yeah, this is actually spending a ton of time, you know, blocked on a binder call or something like that. So that type of information would be useful.
… Because it's literally telling you where the code is.
**Jason Plumb** 29:57 If anybody who is interested in metrics on mobile or client-side, hasn't seen this issue, I just linked it in our doc.
Santosh opened this, trying to… trying to suggest that we get some guidance to, like, steer people away from using metrics on mobile for various reasons, and there is a big-ass discussion, so if you haven't seen this, feel free to give it a read-through and chime in.
**Leonardo Serrano** 30:19 Well, thanks, thanks for this.
**Jason Plumb** 30:22 Yeah.
**Hanson Ho** 30:23 We actually got the, stubs merged in OpenTelemetry I.O, so we actually have a stub for, general recommendations for, for kind of, you know, client-side apps, as well as Android, iOS, and web. And, people… to summarize the discussion, people were apprehensive about putting it,
use case-specific things in the spec recommendations. So I think what we're going to do is we're going to put, you know, client recommendations in the client document, yeah.
**Jason Plumb** 30:49 Yeah. Or, oh yeah, we discussed this, yeah, I forgot, on the website, yeah, thanks, thanks for….
**Hanson Ho** 30:54 And then I think, Severin and I were talking about getting, something, generic in language into the spec itself, saying.
under these scenarios, so not specifically mentioning client or whatever, you know, this may not be appropriate. Like, if the resource is short-lived in duration, it doesn't make sense, and etc, etc. So I think we can write this in a way that… that dissuades, from a… from a… from a detail perspective that's agnostic to use case, in the spec itself, and have very specific recommendations, over in the website.
**Jason Plumb** 31:28 I like that.
Alright, in the interest of time, are we ready to look at zero code?
Do people are….
**Leonardo Serrano** 31:33 Yes, yes.
**Jason Plumb** 31:34 Okay.
Let's move on to this one.
Zero-code instrumentation.
**Leonardo Serrano** 31:40 I'll be brief about this one, since this has the least amount of information of the three.
So, I… I know that there was this whole improvement into the, …
the… we have this now OpenTelemetry Rum Initializer, which is great. Just throwing this out there, there's a slightly less, like.
We can use content provided, and I think that the issue that… or the pull request that I saw, this RUM initializer was authored in, people were talking about this as a potential solution for, like, something that is a little more plug-and-play. Like, in Gradle, you can just add in the dependency for your agent or whatever, and…
content provider would automatically initialize things. Granted, it would need some configuration, like.
We would need to read it from JSON or something, for, like, the exporter endpoints and whatnot, but…
What do you guys think?
**Jason Plumb** 32:34 Yeah, so the work… the configuration work that you touched on most recently is under active development for the SDK. The Java SDK is under active development for supporting file-based configuration, and that's an open telemet… that's a large cross-project open telemetry effort.
Once that lands in the SDK, we should be able to also use that when we initialize the SDK. How it plugs in, I'm uncertain. I know that, from Cesar's initial design, I think he had already always planned or expected to have a Gradle plugin, is that right?
For the initializer?
**Cesar Munoz** 33:11 Well, yeah, yeah, I think we'll be… well, Agra Project will help with a lot of stuff, but yeah, and this could be one of those, yeah.
**Hanson Ho** 33:19 And Jamie's made some good points here.
In the, in, in the, in the dock, or in the, in the.
**Jason Plumb** 33:24 You're saying?
**Cesar Munoz** 33:26 And yeah, I agree with you.
Jamie?
**Jamie Lynch** 33:30 Yeah, ….
**Cesar Munoz** 33:32 Oh, yeah, yeah, I agree. It's, it's, I guess the…
Good way of doing the contract-providing initialization with the startup library.
**Jamie Lynch** 33:42 Yeah, I'd just say that I think this is a good idea, it's the sort of direction I'd want the project to move in. I'd probably suggest making it, like.
You've got opt-in or opt-out.
And… Yeah, that could be done via, like, a separate module or something like that.
**Leonardo Serrano** 34:00 That's how I view it, too, you know.
**Jason Plumb** 34:05 Alright, well, if you think that, give it a thumbs up if you like this feature. That helps us to understand, like, what people are upvoting.
Of, like, what people are interested in.
**Cesar Munoz** 34:14 Anything that I wanted to mention, now that we touched on the initializer?
It's, … it's kind of bare bones right now, the initializer. I just… Kind of created the class.
I'm kind of trying to find what are the configurations that might be common for, common use cases to make
easier for people using Kotlin to initialize it.
However, it's missing a lot of…
features, one of which I realized recently, there's no…
There's no parameter in the initializer to provide a service name.
Which is kind of… kind of basic, and it's not there. So, things like that. So, if you happen to spot
Anything that we could add to the parameters here?
That could, you know, just make this easier for users, but, you know, just don't hesitate to open a…
Happy hour on it.
**Jason Plumb** 35:17 But if you use the initializer today, you should still get a service name, right?
**Cesar Munoz** 35:23 I think you get unknown service or something like that.
**Jason Plumb** 35:26 I… that's a… that's a bug. If that's true, then that's a bug, because it should come from the Android resource.
**Cesar Munoz** 35:33 from the….
**Jason Plumb** 35:35 I believe it should come from this.
Yeah, so it's reading the app name, and it puts the app name in the service name resource field.
**Cesar Munoz** 35:43 Oh, okay.
**Jason Plumb** 35:44 How does it read it? It reads it from….
**Cesar Munoz** 35:47 And then….
**Jason Plumb** 35:48 This wad, yeah.
**Cesar Munoz** 35:52 Got it.
Is this code new-ish? No, I think it's….
**Hanson Ho** 35:59 It's been around for a while.
**Jason Plumb** 36:01 Yeah, yeah, yeah.
**Cesar Munoz** 36:02 Okay, then it should be fine. Still, though, you know, the label….
**Jason Plumb** 36:07 It's just a refactoring.
**Cesar Munoz** 36:09 I don't even know if that…
Getting the label of the app.
I'm not sure if it's even consistent, you know, across languages?
But, …
Yeah, I still think it's worth, you know, providing a way for them to override the service name, because it's such a basic
Part of the, the resources.
**Jason Plumb** 36:30 Well, and let's be clear, when we're setting service name, what we actually mean is app name, like, that's what we've decided, and that discussion comes back a lot, but, you know, we're using service name to mean app name on mobile, and.
**Cesar Munoz** 36:43 It's a long discussion.
**Jason Plumb** 36:44 As an application developer, when you first create an app, one of the first things you specify is the name of the app, right?
It doesn't that go into… into the… into this stuff?
**Hanson Ho** 36:53 Yeah, this by default, pulls it from there, but if you're getting it from a resource, it means it may be localizable.
Yeah. Which would be… which would be a problem. You should be probably getting it from the, the package… package name or something like that. So there is an API to pull this. It's just… it's a binder call.
**Jason Plumb** 37:14 If this is using the wrong API, please file an issue and or fix it.
That'd be awesome.
Okay, so I think we got a little bit far afield, but I think, in general, we like this idea.
**Cesar Munoz** 37:31 Yeah, it sounds good.
**Hanson Ho** 37:33 Yeah, the indeterministic part
makes it a little bit tricky, because you can have bad stuff happening before, and you can have bad stuff happening, as a result, and it's hard to determine, because you don't get to control. You just basically say, Android, please initialize this for me. So….
**Jason Plumb** 37:54 Yeah, and for our purposes… go ahead.
**Cesar Munoz** 37:57 Having users might… Yeah, users are definitely able to disable the contract providers.
Like, the global, concert provider, …
And maybe not realize that it would affect OpenTelemetry's initialization, just in case, it just… it's something that it's…
Granted, For this kind of, initializations.
But, it's still… I mean, it's still good that we would provide something like this.
**Hanson Ho** 38:27 I think as an opt-in, it's great. Somebody who wants to use it chooses to use it, and says, hey, I don't really care, give it to me, so I don't have to do anything. I think that makes sense.
**Cesar Munoz** 38:39 Dead.
**Jason Plumb** 38:41 Okay.
Cool, so I marked that as an enhancement, give it a thumbs up, looks like people are already doing that, great.
Does that help with that one, Leo?
**Leonardo Serrano** 38:53 Yes, it does.
**Jason Plumb** 38:55 Awesome.
**Leonardo Serrano** 38:55 Thank you.
**Jason Plumb** 38:56 Yeah, thanks for… thanks for bringing these up. I think these are all good issues for us to talk about.
Cesar, disk buffering.
**Cesar Munoz** 39:05 Right, I saw an issue to move this buffering to a more stable status, and before doing so, I wanted to apply feedback that I received.
With the current status?
So this is it. This is… well, this is not the entire…
A work, but it's, like, the definition of the new… API service.
I wanted to keep it simple, that's why I just changed… the files changed here, I only focus on the new API, and if there are no issues with that approach, then the next PR is going to be huge, because it's going to be migrating
from the old API. So… so that's pretty much it. If you have some time, please take a look at it.
**Jason Plumb** 39:54 So, one of the… one of the things we discussed last week was, moving disk buffering towards stable, because people get grumpy when stuff is marked alpha, and they get twitchy. Understandably so.
And I think what we concluded was that disbuffering was a pretty good candidate, because it's been around for a while, it has not had many changes, and now you're proposing to make a bunch of changes.
That gives me pause. I support making changes more than I support getting… going stable, but that's just me.
**Cesar Munoz** 40:24 I know it might sound scary, Right?
But what I… what I mean with a different API is one that can…
More easily… actually more flexible and more easily to… to… To work on top of.
In the future, because even though, I mean, we might mark this as stable right now.
And then we're gonna be blocked and having… or adding a bunch of breaking changes.
in the future, because of the current state of the API. So, essentially….
**Jason Plumb** 40:57 Yeah, no doubt we need to improve it. Okay, that's… I'm with you on that.
**Cesar Munoz** 41:00 Like, it's… If anything, I mean, if it helps.
the changes that I'm proposing here are actually going to make the API even more flexible.
So it's not like I'm trying to, you know, make it more difficult to use or anything like that, it's the opposite, so…
And I think it's necessary, otherwise it's gonna become dependency… maintainancy hell for me, and I really don't want that, so….
**Jason Plumb** 41:25 Okay, and it's also… yeah, it's also gonna be….
**Cesar Munoz** 41:29 more useful. That's… that's my idea, the nutshell, for… for it, so….
**Jason Plumb** 41:36 Cool, I haven't seen it yet, I'm happy to take a look soon.
**Cesar Munoz** 41:40 Yeah, thank you.
**Hanson Ho** 41:44 I think what we're doing….
**Jason Plumb** 41:45 Please review, because I want people to… that are not necessarily just me to review it.
**Hanson Ho** 41:50 I thought what we're doing is just making it into beta, so I think it's, like, experimental right now, and we're just saying, hey, let's put it into beta. That still allows us to make modifications, right?
**Jason Plumb** 42:04 Nice.
**Hanson Ho** 42:06 How locked in are we? Like….
**Jason Plumb** 42:09 So I… after our discussion last time, I opened this issue, and Trask pointed out that…
Well, first of all, I mentioned the wrong… the wrong thing.
But there is a Gradle properties entry called otelStable equals true, and that's what can land you stable on that main page. Like, on the… on the README index there. This thing.
So right now, disk buffering is considered alpha, here.
I guess you'd progress to beta.
Which is strictly a nomenclature thing, and this… this issue that I filed is because beta artifacts also get published as alpha.
So, this GCP auth extension is published under alpha, even though…
GCP auth extension is… oh, that is alpha. Maybe it's GCP Resources?
Damn it. I swear I've… I swear we found examples of this.
Maybe it's this one. Yeah, so this one is also, published as alpha, even though GCP resources is…
Beta.
So that suffix doesn't match. That's why I filed this issue.
But Trress did a good job of pointing out that, like, the stable thing is real, so stable artifacts do drop the alpha.
Which, if we look at that list… X-Ray SDK support… X-ray… Maybe this one?
Yeah, notice there's no alpha on these.
**Cesar Munoz** 43:46 Okay, so if we want to prevent people from
Avoiding this buffering, because they see an alpha there and they don't like it.
Then we'll have to move into stable, not to.
**Jason Plumb** 43:59 That's true. That's true.
**Cesar Munoz** 44:03 Unless….
**Jason Plumb** 44:03 We can market beta on this main page, but it really has no recourse unless somebody looks at the README.
**Cesar Munoz** 44:09 Yeah.
**Jason Plumb** 44:11 ….
**Cesar Munoz** 44:12 Another way of saying discourage them from avoiding it is to say, encourage them to adopt it.
Got it.
….
**Hanson Ho** 44:22 I'm the fact….
**Cesar Munoz** 44:24 Do you know if Trask has plans to change it? Like, to make other states….
**Jason Plumb** 44:29 Like, beta?
**Cesar Munoz** 44:30 Statuses, reflect on the, on the version.
**Jason Plumb** 44:35 I mean, the discussion… let's see…
So, it looks like help wanted, yeah, it looks like… looks like that work would be, an open, acceptable change, and that there's some prior art to crib from in the Java Core repo.
**Cesar Munoz** 44:52 Got it.
**Jason Plumb** 44:56 Sound good?
So that's also a top one.
Yeah.
**Cesar Munoz** 45:00 Yeah.
**Hanson Ho** 45:01 So, so looking at that list, like, everything is alpha.
**Cesar Munoz** 45:04 most….
**Jason Plumb** 45:06 Contrib, yeah. Yeah, it very much is contribib, yeah.
**Hanson Ho** 45:08 So, so, so maybe it's actually maybe not that big of a deterrent, because unless, like, everything in here is, like, anything that's not marked stable is a deterrent, which, in which case, it's like, don't use contribs, ….
**Jason Plumb** 45:24 Hanson, I wish that were true. I think it is absolutely not true, because what people do is they come in here, and they're like.
cool, I'm a mobile developer, and these guys, I've heard about OpenTelemetry, they have a thing, and they come and look at it, and then they see…
you know, how to get started, right? We have, like, a little bit of this, that's cool. And the very first thing they see here is this, right? They're like, oh, it's super young and unstable. And then they're gonna, like, go and try and install some instrumentations, or they're gonna look at our agent, and they're gonna see…
I think the agent has the… Disk buffering, right?
Or no, it's in our TOML file, right?
**Hanson Ho** 46:06 Yep.
So I think it's important to get OpenTelemetry, Android, to stable, but this buffering, you know.
like, people… because we're talking about people using disk buffering without using what's telling them to your Android, right?
**Jason Plumb** 46:20 Yeah, yeah.
**Hanson Ho** 46:20 So I think, I think, I think that was the issue that I opened, and… and for that one, that may be less important, but… but certainly getting this project to stable is important. And we're already… I mean, we're using, Alpha, for,
semantic conventions and things like that, so having that alpha shouldn't preclude us for using it here, and then declaring the stable, right?
**Jason Plumb** 46:47 It shouldn't prevent us. I mean, there… there are… I'm sure that there is another discussion that will have to happen about, …
which components of OpenTelemetry Android can be considered stable if they depend on artifacts that are not stable?
… But I don't want to have that discussion now.
But I think that would have to probably happen.
**Cesar Munoz** 47:12 In any case, what I wanted to say, at least specifically regarding this buffering, is that this PR
I hope it's the last like, API design that I will apply to this offering.
Because it's flexible enough to… to… to board anything. So….
**Jason Plumb** 47:33 Cool. ….
**Cesar Munoz** 47:34 But before that, there's definitely gonna be…
breaking changes, if anybody wants to use this offering right now, you know, before those VRs are crunched.
**Jason Plumb** 47:43 That's fair.
**Hanson Ho** 47:46 are the breaking changes, like, behavioral, or are they, like, syntactic? Because I think it, you know, if it's just, like, changing this method name to something else, I think people will be less worried about that. But, if we're, like, we're, you know, doing something totally different under the hood, I think that, that…
Is more, worrying.
**Cesar Munoz** 48:05 No, you're gonna be able to achieve the same behavior. It's just that you'll have to…
You know, write different… different code… different code to make it happen, but it's… the behavior.
**Hanson Ho** 48:18 Yeah, so it's not that bad, then.
**Cesar Munoz** 48:21 Yeah, hopefully not.
**Jason Plumb** 48:23 All new. Is this true? All new code?
**Cesar Munoz** 48:28 There's a new API, ….
**Jason Plumb** 48:29 Yeah.
Yeah.
Cool.
Okay, swapping GRPC exporters….
**Cesar Munoz** 48:41 Oh, this is quick, this is an issue somebody created, essentially, when you shut down a gRPC exporter.
And he was trying to connect to the server.
And it didn't succeed before you shut it down.
You'll get a crash.
That's basically it. So I, … Create this PR.
I added more details there. I'm conscious of time, but… Oh, look!
**Jason Plumb** 49:08 Oh, Jaska's in here.
**Hanson Ho** 49:12 minutes.
**Cesar Munoz** 49:13 Right, so… I'll have to explain.
But yeah, it's pretty much it.
**Hanson Ho** 49:19 It should reject all incoming and then just drain the queue, right?
Sounds like a bug if it's… if it's….
**Cesar Munoz** 49:26 It might be a bug from Augship, to be honest.
But I don't know how… Easy it is to make them add changes.
**Hanson Ho** 49:36 I don't think it's an OHT bug, I think it's a bug with the instrumentation, like….
**Cesar Munoz** 49:42 It's not about instrumentation, it's just the exporter.
Trying to connect to a server.
**Hanson Ho** 49:49 It's the interceptor… it… anyway, well, I'll take a look at that.
**Cesar Munoz** 49:54 Thank you.
**Jason Plumb** 50:01 Cool.
Please review.
And another SUMCOMPR to add build ID. I know this one, this has been on here for a minute, huh?
**Cesar Munoz** 50:15 Yeah I just….
Just to add that attribute to identify the build.
And, you know, if you're interested, It's happening.
**Jason Plumb** 50:26 Cool.
**Cesar Munoz** 50:28 I essentially copy-pasted the OS build ID.
Which already exists.
**Jason Plumb** 50:38 What was the one that Serbi proposed and got merged a long time ago?
**Cesar Munoz** 50:42 I thought it's something the server already did, to be honest, but I couldn't find….
**Jason Plumb** 50:47 It wasn't in… it wasn't in-app.
**Cesar Munoz** 50:51 I didn't find it.
**Jason Plumb** 50:52 So weird.
**Cesar Munoz** 50:53 But I don't… I do remember….
**Hanson Ho** 50:54 You're remembering this, right? Yeah, there's a bunch of these IDs, that are, like, for different mobile platforms and web, it's, like, different, because there's, like.
Like, it's not a version, but it's, like, a build, so the public version is whatever, but the build is, like, an extra, like, a fourth.
Dimension, or something like that.
**Jason Plumb** 51:15 Was it… was it OS?
**Cesar Munoz** 51:17 I just need a way to identify the bill. ….
**Jason Plumb** 51:21 I couldn't.
**Cesar Munoz** 51:21 Funnywise.
**Jason Plumb** 51:22 I get it, I get it.
Let me find it. I just kinda have to know.
**Hanson Ho** 51:30 I thought it was, like, it's in the same namespace as, like, app version, or something like that.
**Jason Plumb** 51:40 I forget how… She spells this.
**Cesar Munoz** 51:43 the outdoor, tab.
**Mustafa Haddara** 51:46 Is this… is this build ID for the application itself, or for the OS version?
**Cesar Munoz** 51:52 for the app.
**Jason Plumb** 51:53 Yeah, it was supposed to be for the app. It's like, every time you build, you get a unique ID. Yeah. Because, like, the ProGuard files, or the obfuscation map, or whatever is tied to a given build identifier.
**Mustafa Haddara** 52:07 We just stuck it on the Honeycomb SDK, since there was no SEMCON, we stuck it on appdebug ProGuardID.
Because it was very ProGuard-specific for us.
**Jason Plumb** 52:17 Got it.
**Mustafa Haddara** 52:17 generic one.
That would be better.
**Jason Plumb** 52:24 That's… that's interesting.
It's not the same thing, but…
Yeah, I'm not finding it. I know… I know it happened, though.
**Hanson Ho** 52:36 Yeah.
**Cesar Munoz** 52:39 Well, there was a… there was a discussion.
**Mustafa Haddara** 52:41 Cesar, the PR that you had linked….
**Jason Plumb** 52:45 It was os.buildid.
Okay.
But different than… it's different.
But I think that… that it might…
It might be used for this.
**Cesar Munoz** 52:59 OS, I do.
**Mustafa Haddara** 53:00 I don't know, that sounds like an OS build number.
Like, a very….
**Jason Plumb** 53:04 That's right.
**Mustafa Haddara** 53:05 version of the OS version.
**Jason Plumb** 53:06 Yeah, it's a different thing. Okay.
That's me confusing it, sorry.
**Mustafa Haddara** 53:11 Cesar, the PR you had thrown up for app.buildID, that's just on SEMCOMF, right? We haven't started implementing that?
**Cesar Munoz** 53:19 Yeah, it's just saying gum.
**Mustafa Haddara** 53:21 Okay.
**Hanson Ho** 53:27 So it's… it's an… it's analogous to, like, service…
version, or whatever that is then? Or, like, it adds on to that.
**Cesar Munoz** 53:36 I think it, it, it… no, it's more specific.
**Jason Plumb** 53:41 It is more specific.
**Hanson Ho** 53:42 Right, no, it… so you could have the same, service ID, so the app version could be the same, but it could be coming from two different builds, so you're basically attaching that. Okay.
And this one, we're okay with using app, I guess, because…
services don't need builds, I guess.
They're no versions.
**Mustafa Haddara** 54:03 Well, that's not… like, a service would have a Git shop, at minimum.
like, a deployed backend service, you could version that by GitHaw, and that would be really useful.
**Hanson Ho** 54:17 Yeah.
**Cesar Munoz** 54:18 I'm on for… I'm up for service, too.
**Jason Plumb** 54:21 You know, so….
**Hanson Ho** 54:21 Yeah, no, I don't want to complicate things. This is fine.
**Jason Plumb** 54:24 I disagree with Mustafa, because for a given GitHash, you could still have multiple builds, you could build twice.
Right? Off the same Shaw.
**Hanson Ho** 54:34 Like, for this one, it could be, like, obfuscation, no obfuscation, it could be, like, you know, using a different, source.
**Mustafa Haddara** 54:39 Sure.
**Hanson Ho** 54:41 SEPT.
**Jason Plumb** 54:42 And there's some entropy, right? Like, these obfuscators, like, have some amount of, like, randomness baked into them, don't they?
**Hanson Ho** 54:48 … yes, yes. Yeah, probably. I think the IDs aren't stable, or I don't think they're guaranteed to be stable.
**Jason Plumb** 54:57 Yeah, it's, like, purposefully not repeatable.
**Mustafa Haddara** 55:00 Huh.
**Jason Plumb** 55:00 Okay.
Cool. So please review that one as well.
I added this one in here just because I think we've talked about it before, and when Cesar was making the very good point that, …
you know, main… like, building and maintaining features that people aren't using is kind of a liability, and maybe wasteful. So I'm like, are people using Volley? Is that project even still supported?
**Hanson Ho** 55:27 No, it's….
**Jason Plumb** 55:28 deprecated years ago. Really?
**Cesar Munoz** 55:30 I haven't… I haven't heard of a use case on the Elastic side for it.
**Hanson Ho** 55:35 The only instrumentation we find that is not using OKTP on Android is typically some library that is, you know, needing a fallback.
**Jason Plumb** 55:44 Okay, so I think we should deprecate it. What do you think?
**Hanson Ho** 55:47 Yes, yes, plus.
**Jason Plumb** 55:49 Deprecate it, and see if anybody complains, and we'll follow back in 3 or 6 months or something, and just remove it.
Does that sound good? Yep. I'm seeing the odds, okay.
**Cesar Munoz** 55:58 Okay.
**Jason Plumb** 55:59 I'll take an action item.
**Mustafa Haddara** 56:01 Bali's is a different HTTP library?
**Hanson Ho** 56:04 Yeah. Volley builds on top of, OK… sorry, HTTP URL connection, and adds some things, …
It's what you would use if you started an Agile project 10 years ago.
**Jason Plumb** 56:16 And we don't have auto build time support for it, I don't think, and I think there's an issue to build that, and so I'm just gonna close that issue, too.
While we're talking about it.
This one, right?
Yeah, what else was it worth?
Okay, so we wouldn't need to do that, we wouldn't have to do that… okay, so this is gonna just save us some other work as well.
**Cesar Munoz** 56:42 Yeah, I actually think Bali is the only instrumentation that we have that it's
I don't think it's usable, actually.
Because there's no… installation, … method for it, I think.
**Hanson Ho** 56:56 Oh!
So, by definition, no one's using it?
**Jason Plumb** 57:09 Okay.
Thanks for entertaining me on that. As far as, we're… technically, we're at time. As far as release schedule goes, I think… so I released Core last Friday, and that means that I think instrumentation should release this week.
Which means…
Are we waiting on contribib? Is there anything… I don't think there's any changes in Contrib this time.
**Cesar Munoz** 57:35 Not that I'm aware of.
**Jason Plumb** 57:37 Yeah.
So we're at 148 3 weeks ago? Yeah, I think we're already up to date on that, so…
We should expect to build either late this week or early next, and do a release.
Just to keep on our… A regular cadence, which is… has been historically very irregular.
But now we'll get… we're getting back on track.
Okay.
I think we're… I think we're good. Cool.
Thanks, everyone. This is a good, lively, full hour of discussion.
And I appreciate it.
**Cesar Munoz** 58:16 in.
**Jason Plumb** 58:17 We'll see you soon.
Bye.
**Hanson Ho** 58:20 Right.
