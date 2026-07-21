SIG: Kotlin SIG
Date: 2026-07-20
Duration: 45 minutes
============================================================

## Zoom Recording Transcript

**Leonid Stashevskii** 01:23 Damn.
**Anton Makeev [JetBrains/KMP]** 02:12 Nice of you, Vernon.
**Leonid Stashevskii** 02:17 Yeah, it is.
Let's wait for… Amen.
**Hanson Ho** 03:09 Good evening? Late afternoon?
**Anton Makeev [JetBrains/KMP]** 03:17 Hi.
**Leonid Stashevskii** 03:18 Yeah, same for us, late afternoon.
**Hanson Ho** 03:21 Well, it's early morning here, but I figured a lot of folks from the other side of the Atlantic here.
**Leonid Stashevskii** 03:29 Yeah. I sent Hanson thank you for assembling the ticket.
with issues, and I actually… brought Anton, my colleague from JetBrains, who's working as a P&P.
I think he will be the best person to help you with the questions, and if you're there.
**Hanson Ho** 03:49 Perfect.
Hi Anton, nice to meet you.
**Anton Makeev [JetBrains/KMP]** 03:52 Hey, Hanson, nice to meet you too.
As Leonid interface me, I'm working on KMP, like, together with Leonid.
wanted to come by to introduce myself, and just to get some context of what you're working on in scope of his KMP support for OpenTelemetry, which I learned recently.
So, been curious about the current state, and if you have any questions, requests, or, like, ideas how we can assist you with that, I'm here.
**Hanson Ho** 04:25 Yeah, it's fantastic. so, our lead maintainer, Jamie, isn't here today. He's got a… he's got a family thing to deal with, so, he's… he's gonna be, skipping. But we can talk through some stuff, and maybe talk a little bit offline. The ticket we started, which, I, if you haven't seen it, I can send it to you, is, I think, just a first cut of some of the questions that we have, about the project in general, and how it kind of, how can we make it more idiomatically KMP. I think we took a stab, and right now, honestly, our focus is really JVM Android, and getting that, all spiffied up.
And then once that's kind of stable, the API is stable, and the implementation is relatively stable, then we want to move on to the other stuff, but we want to get the foundations solid at this point. It's still, I think, early days. So, Jason, thank you for being able to run this, I assume.
**Jason Plumb** 05:24 Oh yeah, sure.
**Hanson Ho** 05:25 sharing.
**Jason Plumb** 05:25 Yeah.
Yeah, sorry, I just jumped in. I was a little bit late, so mid-conversation. Nice to see you, Anton, nice to meet you.
**Anton Makeev [JetBrains/KMP]** 05:33 Nice to meet you, Jason. Hey.
They're also on the, USAID?
**Jason Plumb** 05:42 I'm on the what?
**Anton Makeev [JetBrains/KMP]** 05:44 In Hawaii, right?
I mean, where are you located geographically?
**Jason Plumb** 05:51 Oh, geographically, I'm on the West Coast, I'm also in the Pacific Northwest of, Of North America, in a different country than Hanson, technically, but we're actually pretty close to each other.
Globally speaking.
**Anton Makeev [JetBrains/KMP]** 06:04 Got it. Mainland, it's, in Munich, in Germany.
**Jason Plumb** 06:09 Nice, nice.
**Anton Makeev [JetBrains/KMP]** 06:10 Summit.
**Jason Plumb** 06:11 Yeah.
**Anton Makeev [JetBrains/KMP]** 06:14 So, regarding the pull request, I haven't seen it, I have just opened the document, what, I'm looking at, right now, what you're sharing, Hanson.
Is there anything specific? It's about the KMP support, right? Or is it about GM support?
**Hanson Ho** 06:31 So, actually, the thing I'm talking about is actually different, so let me, okay. It is, it is actually just a ticket, Oh, whoops, I clicked on the wrong thing. I clicked on the, Zoom screen, so obviously it doesn't work.
Excuse me.
Hold on… so this is the tick… this is the issue that I created. It's… it's…
**Jason Plumb** 06:59 this one that I'm showing.
**Hanson Ho** 07:01 Correct. Yeah.
It is… so, the project started… so, just a brief background. we wanted something in Kotlin, natively to support, OTEL, so that we don't have to use, you know, the Java, implementation. So, I gave a presentation, a year… year-ish ago at Denver about needing the API.
And then, obviously, the implementation.
And for us, KMP is almost like a no-brainer choice, setting up a project, for eventual consumption in KMP. So at this point, we have, what we think is a setup that is… fine, it works, but we aren't really sure how idiomotically Kotlin it is, in terms of… I know the project structure has changed recently. We did a best job trying to figure out how to do it, in a way that sets us up for the future, and we kind of just want a pair of eyes that are you know, experts in idiomatic Kotlin in how we set up the API implementation.
So I think things have gone back and forth, because we are trying also associated here to, the, OTEL API, which is more or less, based on Java. So there are going to be some things that, you know, will work in Kotlin, but, not sure if it is, the most Kotlin-y when you just look at the API and the implementation.
So the ticket details a few things that we want to say, hey, can you take a look at these APIs and see how we can improve it to make it more Kotlin? At the same time, you know.
adhering to some of the principles that we have in OpenTelemetry. So… but… and where it kind of conflicts is where we kind of have to make some decisions. And, I believe we've done that, but, we want… We have experts in… OTEL, who had taken a look at it. So, ideally an expert in Kotlin, and especially KMP, taking a look at it. I think, especially our setup with, with, the, the non, the non-Kotlin native stuff, how we set up the… the JVM and the, you know, other targets, whether that's, that's all sound, so… I think Jamie's gonna add some stuff as well, but the ticket is where it kind of starts.
**Anton Makeev [JetBrains/KMP]** 09:28 Yeah, thanks for getting me on board with it.
So, I think that the, is the first question. Is someone already reviewing that from the Kotlin team, or do you have reviewers?
**Hanson Ho** 09:41 Nope, I think we created this ticket for Leonid to, you know, pass it on to a person, and I believe you are that person.
**Anton Makeev [JetBrains/KMP]** 09:50 Yeah, yeah. Let me see how I will, see inside the team who will be the best person to, look at that. We do have a team who is responsible for supporting libraries and MP libraries, like first party, and they would be obvious choice to provide these sessions, please. So basically, I'll take it from here, ask folks inside, and, See if I can, give you some feedback.
**Hanson Ho** 10:19 Perfect, we're not, like, we're not in a super hurry, so, you know, it doesn't have to be, like, done immediately, but, you know, it would be good to have, someone look at it, and if any, anytime you need feedback, you can contact us directly, through the repo. Replying, you know, to this, I think, issue would be the easiest so that most people, more people can see it. But also feel free to reach out on Slack or on email.
**Anton Makeev [JetBrains/KMP]** 10:45 Yeah, yeah, fair.
**Jason Plumb** 10:47 I'll add a little more, kind of, details to this, just in case… I mean, for anyone who's, like, new to the project, it may not be immediately obvious, but these are all, links to, components within the API module, so this module specifically right here.
There is kind of an OpenTelemetry requirement that the API module contains all of the kind of interface surface area for the core functionality, so there isn't a separate API package for traces and metrics. They need to, according to OpenTelemetry, be in the same module.
like, that's kind of a OpenTelemetry project requirement, so just kind of keep some of that lens as you're viewing these, or as anyone.
**Anton Makeev [JetBrains/KMP]** 11:30 I've used the.
**Jason Plumb** 11:30 and… just know that this is kind of the intent of it. Like, there might be some… there might be some natural seams or boundaries that you discover that kind of we need to keep them together sometimes, and that also includes a couple of default implementations, like, I think no-op tracers and some things like that also in the API package, even though they're implementation.
Yeah, and sometimes, you know, methods or the name of methods sometimes originate in the specification, but we have some flexibility there. Like, the spec is pretty okay when it comes to allowing languages to do the thing that's right for their domain, or for their, like.
**Anton Makeev [JetBrains/KMP]** 12:10 Yeah, I think, like, in any case, the first thing to look would be how automatic the project structure is, how automatic the Kotlin the APIs, and if there's something that is dictated by the open telemetry API rules.
Indeed, yeah.
**Jason Plumb** 12:29 Cool. Yeah, that's immensely helpful.
Yeah.
**Hanson Ho** 12:33 Yeah.
**Jason Plumb** 12:34 We also are using an API generator, if that helps, for, you know, the two packages, but maybe starting with the source is better than looking at, kind of, the output side, I don't know.
This is… this is kind of like the interface, right? These are generated, this kind of shows.
**Anton Makeev [JetBrains/KMP]** 12:50 Oh, oh, so it's…
**Jason Plumb** 12:54 Yeah.
**Anton Makeev [JetBrains/KMP]** 12:54 Okay, okay, okay.
**Jason Plumb** 12:57 And, you know, the equivalent JVM one. These are gonna look very similar.
**Hanson Ho** 13:06 Yeah, the weakness you'll find is the non-JVM slash Android targets. You know, we have them compile, it works.
But, you know, whether or not the way we expose those, platform-specific APIs are idiomatic, or, things like, upgrading Kotlin and not being able to depend on, like, or target, like, a lower version, of, of Kotlin, if you're, you know, things like that.
**Anton Makeev [JetBrains/KMP]** 13:39 yeah, oh, okay. As he, who could, take a look at, on our side, I also can't promise the quick response, because we do have already plans for all the teams, and maybe.
Depending on how much work is that, they might plan it for the next iteration month.
Paris.
Eleven.
**Jason Plumb** 14:03 Every open Project ever.
**Anton Makeev [JetBrains/KMP]** 14:06 Yeah.
**Jason Plumb** 14:07 Yeah.
**Hanson Ho** 14:08 Do you guys use OpenTelemetry inside JetBrains, especially in the calling areas?
**Anton Makeev [JetBrains/KMP]** 14:16 The Kotlin, I think Leonid can comment, I can comment, but, in our IDs, it's, pretty much used. We… Leonid have, the build tool that we are working on, Amber, or Contentful Chain, is also using, the tree, as far as I know.
Do you have any…
**Leonid Stashevskii** 14:36 A lot.
I would currently find the project that does not exist, so…
**Hanson Ho** 14:45 Good to hear.
**Jason Plumb** 14:46 Yeah, yeah, it's good.
**Anton Makeev [JetBrains/KMP]** 14:51 And in general, for you to give me context, Currently, we are, like, me, as a Kimpy, responsible Kimpy, I'm looking at the… so-called library ecosystem aspect of KMP, and it's looking at where the friction coming from, where we have legs of libraries, whether that's good or bad support in some places.
And one of the, obvious things to kind of strive for is to have, rich third-party library ecosystem, for the cases that most, most popular use cases, as such. So, OpenTelemary Telemetry would be one of them, and This is Firebase, SDK, stuff like that. We do want to have This library is provided by this.
their respective first parties out of the box for the campaign.
**Hanson Ho** 15:50 Yeah.
**Anton Makeev [JetBrains/KMP]** 15:50 Yeah, yeah, get too much.
**Hanson Ho** 15:52 Go ahead.
**Anton Makeev [JetBrains/KMP]** 15:52 Yeah, pretty much looking forward for TMP supporting Open Telemetry.
**Hanson Ho** 15:59 Yeah, us too.
**Jason Plumb** 16:04 And selfishly, an Android, OpenTelemetry Android, yes, also, long-term, I think that's the right… the right direction for the project.
Eliminating some of the need for, It's not called shadowing in Android, what's it called?
Still too early in the morning for this on a Monday.
Vendoring, no, it's called, what's it called?
Where you have to… basically, you have to tell Gradle to, like, back… backport all the core, oh, sugaring! Yes.
**Hanson Ho** 16:36 D-Sugar… D-Sugaring, yeah, yeah, yeah.
**Jason Plumb** 16:38 Triggering, yes.
**Hanson Ho** 16:39 Yes.
**Jason Plumb** 16:40 So, not having that be a factor would be lovely.
**Anton Makeev [JetBrains/KMP]** 16:46 And do you have a timeline in mind, anything like… Just… okay, fine. And how many people are working on that?
**Jason Plumb** 16:55 On which project, Android?
**Anton Makeev [JetBrains/KMP]** 16:57 The KP supports for… It's a routine.
**Hanson Ho** 17:01 Thank you, Lisa.
So, it's, it's, it's, it is an open source project, and so, you know, the number of people, kind of, come in and out, and how much time they have, depends. But, so there's almost several layers to this. So, the actual… Kotlin SDK, which has KMP support. You know, Jamie works on it quite a bit, and then, you know, Jason helps out, as much as he can, and I help out as much as I can.
But around that are kind of what's driving the propulsion of this, which is, so I work for Embrace, and our SDK uses the Kotlin API, and soon we'll use the Kotlin SDK implementation. And we want as much features and things like that in there, as possible. So, as a result, you know, we contribute to the project, then we can use it back upstream. Opentelemetry Kotlin is a separate project, which uses the Java, SDK and API right now, for Android instrumentation and, like, agent support.
there is a goal to move that to use OpenTelemetry Kotlin.
API and SDK, eventually. That is… the timeline for that is a little bit less certain, because, you know, we are also in the process of stabling, stabilization. So this is basically OpenTelemetry in general. Our APIs are, used, but they're not officially stamped stable. And for us at, OpenTelemetry.
Android, we want to get APIs stable first, and then be able to rev, like, a V2, and then start doing some of the bigger changes, including, you know, changing the API to expose the Kotlin API versus the Java API.
And for Embrace, we exposed the Kotlin API already, so, you know, the driving force would be the SDK implementation.
So I guess, to answer your question, it depends on what sprint and what month, we're talking about and what we want to deliver. But, and I would say progress in the last 6 weeks or so have been, a little bit slower on the Kotlin side, simply because the main maintainer, Jamie was on, parental leave, so he just came back. So if you looked at, I would say commits in the last two months, it's been, you know, a dip, and it's because, I would say.
75% of the, of the person hours working on this, if not more, was, was, trying to get some sleep, having another kid. But you're gonna see this ramp up, I think, throughout the summer and into the fall, especially as we stabilize the APIs, which really is, is, is, is, I wouldn't say it's a box checking.
exercise, but it's gone through several rounds of, kind of, reviews and stuff, but now we want the final, final round of reviews to basically say, are we, are we sure, are we sure? And getting, you know, some… advice and input from, you know, JetBrains folks, like, y'all would be extremely helpful in this exercise. Not that we can't change stuff after the API's been stabilized, but it'd be nice to do it before.
**Anton Makeev [JetBrains/KMP]** 20:15 Yeah, got it. Thanks. Thanks, Exclamation.
**Jason Plumb** 20:19 And changing after stability is much more challenging.
**Anton Makeev [JetBrains/KMP]** 20:23 Yeah, that's very familiar, that's very familiar.
**Hanson Ho** 20:31 Well, yeah, thanks for, for joining, Anton. We're gonna be probably talking about, like, some of the degree stuff. Feel free to stick around and just see how we operate.
**Leonid Stashevskii** 20:39 Sorry for disrupting the meeting, by the way.
**Hanson Ho** 20:41 No, this…
**Jason Plumb** 20:42 We're open to it. The more the merrier.
**Anton Makeev [JetBrains/KMP]** 20:45 Sure.
**Hanson Ho** 20:46 I love this. This is, like, something worth disrupting for us. This is no disruption, actually. This is, like… it's like a drought, and then there's rain that comes out. Well, we have to, you know, prepare for rain now, but this is rain that is much, much, much desired. So, thank you very much for coming and following up.
**Leonid Stashevskii** 21:03 Thank you.
**Anton Makeev [JetBrains/KMP]** 21:05 It'll be best helpful when I just go ahead and start looking for folks inside.
Cool. Well, we'll, be dropping off. Nice to meet you all.
**Hanson Ho** 21:15 Excellent.
**Jason Plumb** 21:17 Thanks for coming by.
**Hanson Ho** 21:18 son.
**Jason Plumb** 21:20 safely, man.
Do we know… is the full team in Munich, do you know?
**Hanson Ho** 21:28 they… there… there's a lot of them in Germany and Munich, so I don't… I don't actually know, certainly Kotlinkampf is always in Munich, as far as I know, so that's the epi… that's the epicenter, I would say.
**Jason Plumb** 21:43 Okay.
**Hanson Ho** 21:46 So…
**Jason Plumb** 21:47 Are you ready to go on to the next topic, Hanson?
**Hanson Ho** 21:49 Yes, yes. Right.
So Jamie, put up an API for span context propagation by coroutines context. Implementation's actually fairly simple. It's just using this, concept, coroutine context element.
And as the coroutine, dispatcher runs and kind of changes and suspends, the… the thread local is effectively, propagated. And making this an element that is effectively part of the coroutines context ensures that at suspension, whatever context there is saved, and when we rerun, or when it's unsuspended, or… I don't know what the verb is, when it runs again, it will, it will basically still be there.
this would not be true if you simply used, the Kotlin, or the thread local, because the thread that's running, is… could be completely different. So… I believe this is how the existing, thing in Java, does with code routines as well, where it kind of stashes this. But it… it also means that.
it's fairly random, in terms of, how this stuff behaves. You would kind of have to know, especially if you're trying to contribute to a context, or, like, start a, you know, a child span based on the existing context, you're gonna have to kind of know The thread… the coroutines kind of, execution model, to know that, hey, you're not just running on the thread, if you suspend it, you know, what you expect might not be there. So… but this is probably the most, reasonable way of doing this type of, simulating, or not simulating, sorry, the, making context propagation as one would expect from Java kind of work via coroutines, is this way. So, Jamie just wanted me to kind of raise this, because, again, he's not, he's not available today.
**Jason Plumb** 24:04 So, I am pretty fuzzy when it comes to coroutines, and it's, like, specifically on how they're implemented, and especially how they're implemented within KMP. On the JVM, my kind of dumb guy, basic dork understanding is that a coroutine allows you to have Multiple, let's call them functions, but… Coroutines, functions, potentially running on the same thread, and their context can be… their context is an overloaded term these days. Their, execution can be… suspended at certain points in favor of other coroutines being resumed, and a single thread can then multiplex between a variety of coroutines, and let them all kind of Pretend to execute concurrently.
And effectively execute concurrently, but you've really only maybe got one thread, and then you can expand that to multiple threads, and a coroutine… a given coroutine could… suspend and resume across different threads as well. So, multiple coroutines, executing and suspending across different threads. That's kind of my mental model of it.
in the dumbest possible way, I think about something like Node.js or the JavaScript runtime, where you also only ever have one thread, and that you can certainly do a bunch of concurrent things. And I don't think in the JavaScript world that they call them coroutines, it's just the way that the runtime works.
And so you have multiple things that are going, but you are always, like, blocking on I.O, right? Like, everything comes down to blocking on I.O, so you might have, like, 12 different functions, they're all running on… I don't want to say a thread, I'm going to say the thread. I know there's exceptions to all of this, but, like, that's my dumb guy kind of understanding.
So in that case, I don't know what the OpenTelemetry JavaScript implementation looks like for sharing context, but it seems like it should be Kind of easier in that case, versus an environment like… a JVM runtime where you're switching context.
With coroutines switching execution all over the place, and how that might look for saving open telemetry context, right?
I'm rambling for sure, but, like, what I'm getting at is, like, my mental model is a little bit crusty. If this only applies to GAVM, then what does that imply for the other platforms when you're using KMP?
**Hanson Ho** 26:35 It means that you can't really use autopropagation, because, there are no, there's nothing to hang this off of. Okay. So, yeah, describing it and comparing it to the JS problem is good, but this is almost like a… there's like a second prob… a secondary problem?
**Jason Plumb** 26:57 Okay.
**Hanson Ho** 26:57 On it, so, rather than just having one execution thread and many different, you know, abstractions on top of it that are.
different. There's also the problem you described, which is it's one abstraction, but executed under multiple threads. And this This uses a construct, the thread context element.
As a means of passing.
or rather, stashing and unstashing this thing as it kind of executes. So, it is… it is… it is very JVM-based, in the sense that it basically maps to… so, if you resume execution on a different thread, or you resume… well, yeah, if you resume execution even on the same thread, Previously, there's no guarantee that the context hasn't changed, because some other execution has happened on it. This will ensure that the thread local is emptied.
And, and kind of repackage with what you had. So, if you, stash stuff as this, and it suspends.
it guarantees that when you come back, it's still like that, no matter what happened before, no matter if you're executing on literally a different thread. So this kind of solves one use case, which is, as you go through the execution of your suspend function, if in that suspend function, you do stuff like create a new thread, or sorry, not create a new span. You're guaranteed that, What you had previously.
Before suspension is the same as after, so you can depend on that coming in and saying, hey, if you are executing a different, you know, suspend function, and you're like, it's the same dispatcher.
I don't… unless you can somehow, say, share this… this… context, which, again, I'm not super familiar, like, I'm not super familiar with the ins and outs of this.
**Jason Plumb** 29:06 Yeah.
**Hanson Ho** 29:07 Unless you explicitly tie those together, they will not be tied together.
Which… I mean, it basically is a whole set of caveats that will ensure some use cases work, but, equally, there are likely other use cases, even on JVM and Android, where it doesn't work. Let alone iOS and other targets. So… this remains… auto-propagation still remains, I would say, a, generally unsolved problem, in this, in this… ecosystem.
Completely unsolved in non-JVM and non-Android.
partially solved workaroundable, on JVM and Android, but ultimately, It… it… it is not… It… this framework and auto-propagation, the way that… that Java expects it, is very difficult. Even with this. This is… this is like… Here, we can take care of some use cases, but, like, supporting this in general, as you would on other ecosystems, especially since we're not talking about thread-based execution,
**Jason Plumb** 30:24 Right.
**Hanson Ho** 30:25 as what a span is, is… is just… Still a challenge, which, you know, needs to be called out, even if we have this.
**Jason Plumb** 30:38 Yeah, it makes me think that thread local has always been a misnomer to me. It's really thread global, right? It's like, do whatever you want on this thread, and you'll have access to the same thing that other things running on the same thread will see.
So in that respect, you kind of want to force it to be more local to the thing that's executing, but that also kind of… I think it also implies additional… Contexts, like restoration, switching, whatever… whatever's going on behind the covers to restore local function-scoped context, like, needs to be… like, saved and restored all the time, or whenever a pause can happen, or a yield, or whatever we use these days, then… But that's also… yeah.
It's complicated.
I definitely will need to sit with that PR for some time and read through this document to sort of better understand what's happening here, but that's awesome that it's not huge, too.
**Hanson Ho** 31:39 No.
**Jason Plumb** 31:40 It's…
**Hanson Ho** 31:41 In fact, the implementation is tiny. If you look at the files change, you would miss it if you scroll.
**Jason Plumb** 31:47 Yeah.
**Hanson Ho** 31:48 Yeah, yeah. Cool.
**Jason Plumb** 31:51 Was there anything specific about this, or you just wanted to raise it so people review it?
**Hanson Ho** 31:55 Jamie wanted me to bring this up, so people review it. Also… It's almost like this is the best that we can do, we think. I think other opinions would be nice, if it's like, hey, we can actually do this some other way, but I think just…
**Jason Plumb** 32:12 Like…
**Hanson Ho** 32:13 Just from a mental… just from a mental model… just from a mental model.
it is just not something that fits. I think the use case of, I think, most backends, you know, is auto-instrumentation. You drop in whatever context it is, it adds to the existing trace.
there's really no way to say, hey, add this to the existing trace, because there is no such thing as the existing trace. There could be a trace that happens to be on thread local.
But there also could be other traces that are… that have different lifetimes, that… that… that, you know, don't map to… to threat execution, so…
**Jason Plumb** 32:51 Totally. Yeah.
**Hanson Ho** 32:53 JS doesn't… I mean, JS has… doesn't have a solution for this. Their solution is… there's no automatic context propagation, and whatever they had pre… whatever they had previously was built upon an API that was being deprecated and doesn't always work.
**Jason Plumb** 33:06 Oh, interesting.
**Hanson Ho** 33:07 So, JS just doesn't have this. I know, I think, Go doesn't have this, because, you know, you always pass in the context, right? And this is more in line with that. I would say more in line with JS, especially, given that it is more, you know, targeted for end-user apps and things like that. Okay.
**Jason Plumb** 33:29 Cool.
I don't know this test storage class.
This thing.
**Hanson Ho** 33:45 It's, it's faking, thread local, I think.
**Jason Plumb** 33:48 Is it… is it defined in the same… oh, that's why, okay. Wait, no.
Where is that… where is that defined?
Test storage.
**Hanson Ho** 34:01 Somewhere.
**Jason Plumb** 34:06 It doesn't… like, I'm not getting a match on files, so it's gotta be in something else. It's gotta be in another file.
**Hanson Ho** 34:12 It's probably an interface within a different file name.
**Jason Plumb** 34:18 Oh, it's, it is, it is here.
**Hanson Ho** 34:20 Oh, it's just local.
**Jason Plumb** 34:21 Multiple states of binary, yeah, okay.
**Hanson Ho** 34:23 implicit context storage. Yeah, yeah.
**Jason Plumb** 34:26 And it just allows you to get and set, or to set… okay.
**Hanson Ho** 34:29 Yeah, it's like, hey, I'm a Fred Local, believe me.
**Jason Plumb** 34:33 Interesting, yeah, okay, I'll have to find actual concentration time for this PR.
**Hanson Ho** 34:41 Yeah, it's…
**Jason Plumb** 34:42 It's not a casual review for me.
**Hanson Ho** 34:44 No.
**Jason Plumb** 34:51 This is more for Jamie as well, but I still have on my radar to switch us over to using environment secrets in the build. I was trying to get to that Friday and didn't, so it's near the top of my list to do this week.
So hopefully get it done in the next couple of days, I hope.
I'll just make a note of it in case he's reviewing this.
**Hanson Ho** 35:24 And I guess for anybody who's got additional questions for Anton and the Kotlin folks, or the JetBrain folks, please comment on that issue.
**Jason Plumb** 35:33 Yeah, yeah, yeah.
**Hanson Ho** 35:36 I don't want to.
**Jason Plumb** 35:36 I wanted to make sure this was clear, too, like, as they're reviewing, if they see stuff, they're like, oh, that's stupid, like, in Kotlin.
this, like, please open an issue, or a VR, like… Hopefully that's clear from this, but yeah, please open issues, that's welcome.
Cool.
Alright, anything else that people have?
Yes, because We have a little bit more time, so we could look at if there's any new issues. There's definitely some that are new to me.
These look like API stuff, yep.
**Hanson Ho** 36:16 Jamie created a bunch of, issues. Tagged.
**Jason Plumb** 36:20 Good. Yep.
API stuff.
This one is not API stuff.
Custom error handler.
**Hanson Ho** 36:39 Yeah, in the… in the SDK, or the API, there's… you can have an error handler pass into the SDK, Or, yeah.
**Jason Plumb** 36:49 I've never seen this… wait…
**Hanson Ho** 36:52 Yeah, I haven't seen this either until… until, Like, I didn't know this was an OpenTelemetry requirement, to be honest, until I saw this.
**Jason Plumb** 37:00 Oh, this is weird. So, by default, Java uses logging for errors.
J-U-L.
And you can implement this logging filter, which I don't know what package that's in.
But I guess you can register it. Wow, okay.
But that's only for, kind of, logging of errors, it's not a generic handler.
**Hanson Ho** 37:25 No.
**Jason Plumb** 37:25 Hit it.
That's interesting.
**Hanson Ho** 37:29 It is, when shit happens, do you want to know about it thing.
**Jason Plumb** 37:34 This is… this is way different than Java.
Right? This is a straight-up handler, and you can log in or do whatever, you could…
**Hanson Ho** 37:41 Whoa!
**Jason Plumb** 37:42 crash the runtime or exit the process, right? That's very… Carlos! Thank you, I saw your name.
**carlosalberto** 37:49 Actually, my comment was about to, talk about… mention something else.
**Jason Plumb** 37:53 Oh, okay.
I couldn't expect stuff, and Carla's hands went up.
**carlosalberto** 37:58 No, this one is, if I remember correctly, is that this was even before login landed into spec, and the idea is that if suddenly your application is trying to send metrics, or traces, and there's, like, you know, a connectivity problem, you want to see locally what's happening, you know?
**Jason Plumb** 38:13 Yeah, yeah, totally. This, I mean, this makes sense, like… having a pluggable error handler for certain cases seems great. Like, yeah. So, okay, that's cool.
And there's a PR for it, of course.
Okay.
Plenty to review.
What else did you want to talk about, Carlos?
**carlosalberto** 38:36 One thing that is just for your consideration is that Jamie opened also an issue for the tracer configurator part.
**Jason Plumb** 38:44 Yeah.
**carlosalberto** 38:45 And I don't know what to… how to feel about that.
Basically, because this is something experimental in the spec.
And probably should be treated as such. Like, compared to other issues, it should have less of a priority.
**Jason Plumb** 39:01 Okay.
Yeah, makes sense.
**carlosalberto** 39:03 Yeah, so probably, yeah, like, we will need something. I don't know whether Jamie and Hanson and Jason, you guys are already using, like, some kind of a milestone, or, you know… But basically, yeah, I… I mean, I'm thinking from the perspective of users that make one and come and implement something, I would rather have them implement something like zero handler than this, you know? This is nice, this will be super useful.
But it's not even stable.
So I think we should probably just postpone that one.
**Jason Plumb** 39:31 Yeah, he's already got the PR for it, too. I'm just gonna leave that comment, but yeah, I think… I think I agree. It would be a good thing for us to sort of collectively agree upon that stuff that's, like, in development or that is not stable. We can kick that can down the road.
And also doing that allows us time for that to, like, simmer a little bit, and maybe approached more stable before we implement it, so…
**Hanson Ho** 39:56 Yeah, I didn't realize this was not stable, and I don't know where…
**Jason Plumb** 40:01 And unfortunately, they changed the name from experimental to Development, so you just have to do that aliasing in your head. When you see development, it means Experimental.
**Hanson Ho** 40:11 So I don't know where Jamie's working from in terms of, what are the things that we're supposed to have done for the API. He must have gotten this somewhere. Is there, like, a big matrix, maybe, that we're getting this from?
**Jason Plumb** 40:30 I know what you're talking about, there is a matrix.
Don't know how to find it.
**Hanson Ho** 40:39 I think we've added stuff to it on Kotlin, so probably looking at OpenTelemetry I.O, and looking at JME's PRs, we'll probably be able to find it.
**Jason Plumb** 40:50 Yes, okay, I'm following your train of thinking here.
**Hanson Ho** 40:59 Because, yeah, I didn't realize we were doing this as well. It'd be good to, like, have, like, the comprehensive list, and if the comprehensive list is moving, oh, it wouldn't be me, it'd be Jamie.
**Jason Plumb** 41:09 Oh, sorry, yeah, derp, Fractal… Red.
You guys, you jokesters.
Okay.
So… Maybe this has it?
No, no…
**Hanson Ho** 41:30 Not this one.
Oh, yeah, yeah, this is… This probably has it.
Or not.
**Jason Plumb** 41:42 No…
**Hanson Ho** 41:44 Is it in the spec repo, maybe? Maybe it's not in the I.O.
**Jason Plumb** 41:47 Yep, I like what you're… I like what you're thinking.
Oh, you know what, I think I left this is open over there, too. That's the problem, it was probably merged.
Complains we drinks.
**Hanson Ho** 42:06 Perfect. Yes.
**Jason Plumb** 42:07 This thing, okay.
SPET Complaints Matrix.
Python, no.
**Hanson Ho** 42:21 It's a generator out there.
**Jason Plumb** 42:24 Yeah.
**Hanson Ho** 42:25 This is Gundy, yeah.
**Jason Plumb** 42:27 There we go.
So you think that that specific tracing config might be in here?
**Hanson Ho** 42:36 Yeah, otherwise I don't know where he would…
**Jason Plumb** 42:47 Yeah… Well, I mean, he can respond to that later, I don't think it's, like, mission critical, but in general, I think it's okay for us to agree that, like, stuff that's still in development can take a lower priority.
**Hanson Ho** 42:59 Yeah.
**Jason Plumb** 43:01 Yeah, I didn't see it immediately in this list, but… I imagine it's in here somewhere.
**Hanson Ho** 43:10 Yeah, I don't know which list he's working from, so,
**Jason Plumb** 43:13 We do have good pluses going down here so far. Okay.
Cool.
**Hanson Ho** 43:20 I feel like we have all…
**Jason Plumb** 43:21 This would be a great matrix to work from.
**Hanson Ho** 43:25 I feel like we have a… the APIs we need. I think right now it's about stabilizing the ones that we already have, rather than creating new ones. Totally.
**Jason Plumb** 43:36 Cool.
Alright, I think that's it for today.
**Hanson Ho** 43:45 I updated the, SEMCOM fusage thing, per what we talked about, but we should still It's just a demo, but basically, Yeah, we have to get the actual.
**Jason Plumb** 44:01 for Android, right?
**Hanson Ho** 44:02 Yeah. For both, both Android and for this.
Android is actually… Android probably has a lot more stuff that we can actually use right now. For Kotlin, it's basically where you need to wait for the upstream to be created, and then we can switch everything. Or actually, we don't have to switch every… actually, you know what? We don't have to switch anything. I think… Yeah, you know what? I think… I think my… I gotta… I gotta change what… I'm working on 3 different repos, 4 different repos right now, and it's… I'm getting a little confused ahead of myself, so, yeah, maybe I'll take a look.
**Jason Plumb** 44:32 Only, only 4, what a luxury.
**Hanson Ho** 44:34 Just for semantics.
**Jason Plumb** 44:37 I'm kidding, I'm kidding.
You're in the same boat I am, man.
**Hanson Ho** 44:41 I… it's like, I… which one? Oh, wrong one!
**carlosalberto** 44:45 Well, you know what you know what's funny? That, many of my colleagues are in the same boat as us, and the boss is like, what's the problem, man? It's only a few, like, repos, just use AI to solve that. Like, but… Sure.
**Hanson Ho** 44:58 AI helps with a lot of the mechanical stuff, but, like, getting the mental model is that… that… sorry, my brain still doesn't… you still need that in my brain. Otherwise, then I'm not involved.
Yeah, anyway.
**Jason Plumb** 45:13 Yep.
**Hanson Ho** 45:15 Cool?
**Jason Plumb** 45:16 Alright, I'll see you all soon. Take care, have a great rest of your week. If I don't see you before then. Bye. Bye. Ciao.
