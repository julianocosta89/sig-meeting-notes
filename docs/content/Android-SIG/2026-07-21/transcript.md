SIG: Android SIG
Date: 2026-07-21
Duration: 58 minutes
============================================================

## Zoom Recording Transcript

**Jason Plumb** 00:58 Good morning. I was a little bit concerned that I was joining the old meeting. I know they're in the process of switching all of the CNCF meetings to a different Zoom account, or Zoom structure, Zoom org?
And… I guess we haven't been touched by it yet, but I think it's coming, so… if you join this meeting soon, and it's broken, just check the community calendar, there's probably a different link.
**Hanson Ho** 01:27 Hello?
**Jason Plumb** 01:29 Hello.
Yeah, let's see, so… let me share my screen.
I don't know when it's gonna happen, but let's see, calendar, this thing… So some of these will be on… yeah, see, it's a Zoom LFX platform, like a Linux Foundation one.
And I think this Android one has not been switched yet. When they switch it, just be prepared when it switches for us to have some… Some people that are confused, or joining the wrong meeting, or getting 404s, or whatever it looks like, but just know that that's happening.
And I don't know what order they're going in or how quickly, but it looks like… Looks like half of them or something have been switched. Like, all the big ones, it seems like, have been switched.
like… I don't know.
That one hasn't. Anyway… That's a problem for future us.
**Hanson Ho** 02:38 Somebody who first notices it, posts on the Slack, so more awareness.
**Cesar Munoz** 02:57 or anxious.
**Jason Plumb** 02:58 Good stuff.
Hey, Cesar.
I think that's who I said that.
I wasn't looking.
**Cesar Munoz** 03:07 Oh, sorry, I didn't here.
**Jason Plumb** 03:12 Okay, let's jump into the first one, which is Ben's topic on some PRs.
**Ben Joseph** 03:19 Yeah, so, I know, like, last time we discussed some of this, and, like, I did not have a clear shape at that point, so this was, I prototyped this so that, like, we can… I can get some feedback.
So I come up with what I feel like is a good shape, or a good starting point for Compose Navigation.
So, yeah, that's the first PR. I've added, like, nav controller extension functions and a convenience function, that should help with, Generating the events for, it does not generate, events yet. Like, it fires an event, but that gets overwritten by our spam processor at this point.
So, that would be a next step, but, I just wanted feedback on, like, what this initial approach looks like.
I know David, reviewed it, and… Said he was okay, but, like, yeah.
Looking for, any, any feedback?
**Jason Plumb** 04:25 Cool. Yeah, I have not gotten to it yet, that's awesome. Do you know why this band processor is stomping over it?
**Ben Joseph** 04:32 So it's not yet wired into the visible screen tracker, so that's, that's, we use the activity light cycle callbacks to update that. It's a global, state, and any… for every signal that we send, the attribute, screen name is, replaced with whatever is added in, is available in Visible Screen Tracker. So, I… I use the same, attribute, so that… that's why it's getting overwritten.
So, at this point, this does not introduce any sort of behavior change. It's a new module, and does not cause any changes to the existing behavior.
Okay. Yeah, so how we wanna, you know, change… how we wanna generate the signal, and, like, if we should use a different attribute name, all of that, I'm open to feedback, but I thought, like, this would be a good, small starting point.
**Jason Plumb** 05:31 Cool.
Yeah, that's great. We've been needing something like this, so I haven't had a chance to dig in and look at it yet, but this is great. Has… I mean, David's looked at it. Anyone else?
Have cycles to take a look at this?
**Hanson Ho** 05:42 Yeah, I'll definitely take a look at this.
**Ben Joseph** 05:45 Thanks, Hanson.
**Jason Plumb** 05:50 Cool, yeah, that's awesome. I think… I mean, I am definitely in the camp of favoring smaller PRs right now, because the amount of reviewing is… pretty intense across all the repos. So this is, you know, above our 500, but it's fine, like, this is… this is manageable, it's not 2,000, you know?
**Ben Joseph** 06:08 Yeah.
**Jason Plumb** 06:09 Yeah, and then as long as it's clear in the description that, like, this doesn't… complete the work, that there's additional follow-up work. And what can be also be helpful is to file issues to follow it up sometimes, because we all get busy, and if you get pulled onto a different project, or something happens.
then we can lose sight of that, and then a year later, somebody comes along and is like, I was trying to compose instrumentation, and it doesn't work because of the span processor. So sometimes having a follow-up issue Or staging it out can be helpful.
Absolutely.
**Ben Joseph** 06:40 I…
**Jason Plumb** 06:40 That's great.
**Ben Joseph** 06:41 I'll create issues and link it here, but I also wanted, so what, so I, for the next step, I have questions like, what is the best way to, you know, prevent this override or things like that.
Is there, like, I understand, like, we can discuss in the SIG, but, like, if we want to do it async, what would you recommend? Like, create a spec, or start a discussion in Slack? What would be the best way to get feedback there?
**Jason Plumb** 07:10 I think having an issue that kind of… because you have this called out as a follow-up item, I think having an issue, linking it here, and then just doing the discussion on that issue… Like, describing what the problem is after this one lands, and then saying, hey, what do we want to do about it? I think that's…
**Ben Joseph** 07:24 Okay.
**Jason Plumb** 07:24 That would be the normal way to kind of handle it async, is with an issue.
**Ben Joseph** 07:28 Okay. Yeah, sounds good. I'll follow that route.
**Jason Plumb** 07:31 Okay.
Cool, let me just make a quick note.
Okay.
Any other talk about Compose now from anyone before we move on to the next issue, or the next PR?
Going once. Going twice. Sold. To the next PR.
So that is this one. No, that is this one, right?
**Ben Joseph** 08:30 Yes, this is my colleague's PR, so I think there's already an approval, Just wanted to bring it up, like, if… I know we need one more approval.
Or if you… if anybody has any feedback.
**Jason Plumb** 08:45 Yeah, so I left some feedback on this kind of late yesterday, late…
**Ben Joseph** 08:48 Oh, okay.
**Jason Plumb** 08:49 Pacific time. I saw that Jamie approved it, And I raised some concerns. I put a block on it because I wanted us to actually talk about it today, so this is a good time for that. It looks like… in the last 15 hours, it's already been addressed, so I haven't seen what that looks like. I was sleeping for half that time, or part of that time at least, and so it's the way that works sometimes, but it looks like… so I was raising a couple of concerns.
Mostly that the previous signal handlers, when they're invoked, they're invoked from our agent's context, and they don't have all of the same necessary parameters that the handler might expect. And there also seems to be, like, an ordering problem if something had registered handlers after us.
And was chaining it to us. Like, if user code, like an application was wiring in handlers after us, then I think the ordering is not preserved, but I think it looks like they've already addressed it, so…
**Ben Joseph** 09:47 Okay.
**Jason Plumb** 09:50 I would love smart people to give a thorough read of this PR, because it has native code, and because it's a little bit… I would say it's quite technical compared to a lot of the other recent PRs we've had. I just want to make sure, as a maintainer, that we're spending the correct amount of time kind of scrutinizing it, and that it really is looked at under a microscope before we proceed. But I know that this doesn't… also doesn't finish the issue.
Like, it doesn't finish the native crashes, so this is, like, a very important piece that I want us to just be able to take some time to scrutinize.
So, if… if I'm being… more slow than… slower than normal, or a little extra conservative. It is just because there's, like, native code in here, and it is… it has the potential to, like, you know, crash apps and stuff.
**Ben Joseph** 10:39 Understood, yeah.
**Hanson Ho** 10:41 crash up silently, because we don't have native crash handling if it doesn't work, so… Exactly. That's the biggest one.
**Cesar Munoz** 10:48 Yeah, it's Horrible.
I haven't had a chance to look at it, but I'll find the time this week.
Probably tomorrow.
**Jason Plumb** 10:58 Thank you, Cesar. Yeah, that'd be great.
**Ben Joseph** 11:00 Thank you.
**Hanson Ho** 11:01 The fact that Jane…
**Jason Plumb** 11:03 Go ahead.
**Hanson Ho** 11:03 I was gonna say, the fact that Jamie has looked at it, gives me great confidence. But yeah, more eyes is never bad.
**Jason Plumb** 11:12 Yeah, I figure the worst thing that can happen is a user is like, I installed the crash handler, and now my app crashes. Like, it's not the… it shouldn't be the crash causer.
**Ben Joseph** 11:21 Awesome.
**Hanson Ho** 11:21 It's, it's… If the problem is there, it's gonna be super subtle, because it's gonna be, like, a clash of signal handlers, it's gonna be an ordering, so you might not even see it until a very specific use case that… so… yeah, but doing our due diligence is all we can do at this layer, so, you know, let's do that.
**Jason Plumb** 11:40 I mean, these… both of these are pretty niche, and they involve having other handlers there. I think most apps don't install signal handlers, so…
**Hanson Ho** 11:49 I mean, a lot of libraries… a lot of libraries do, that's…
**Jason Plumb** 11:52 Yeah, yeah, exactly. In other crash reporting libraries, that's the thing I really worry about, so… Yeah.
I know, like, in the Java world with the Java agent, we say pretty explicitly that we don't interop nicely with other instrumentation libraries. We don't have that same thing in Android yet. I hope that we can avoid it. It seems like it should be fine to install multiple crash handlers, multiple instrumentations, but we haven't… Yet bumped up against that, so… That's not where I wanted to be.
Okay, let's move on to the next one, David.
Automatic coroutine hotel context propagation.
Oh, yeah.
Yep, Kotlin SIG, and there's a PR for it.
Yep.
So, one thing that's interesting is long-term, as stated in the roadmap.
We do want to switch to the Kotlin implementation at some point.
In which case, this kind of falls out naturally.
So, I think it wouldn't, in the short term.
Because we're using the Java implementation.
And really, we would need Hotland to be stable.
Which is probably not that far out.
For many components.
But yeah, this is interesting, the cases… the case that it covers, according to the PR, says… so, and also, just to set context for everyone else, like, the Kotlin project is really targeting Kotlin multiplatform Which means you write whatever in Kotlin, and then you compile it down to… Java bytecode, or JavaScript to be put into a browser, or Node.js, or you compile it to native code on some platforms, such as iOS, or… probably… x86, or whatever the 64-bit equivalent is these days, AMD 64.
And then, Android is also a target, right? So JVM, bytecode, and Android are separate targets, is that true?
**Hanson Ho** 14:51 Yep.
**Jason Plumb** 14:51 in CAMP.
So… what we would… what we would need eventually is an Android target, but what's interesting is that this says that the implementation here is only available on the JVM, I don't know if that's true of Android. It's a question worth asking, and Jamie's not here to answer it, but I don't, I'm not sure if this also exists on Android.
**JM Jason Morris** 15:16 This is… he means JVM as in all JVM targets, JVM and Android.
**Jason Plumb** 15:22 Okay, so it is on Android as well.
**Hanson Ho** 15:25 Yeah, I think…
**Cesar Munoz** 15:26 what Jamie added there looks like the country… no, not the country, the… upstream Auto Java SDKs.
coupling or a team, extension. I think that's the name.
**Jason Plumb** 15:40 Yes.
**Cesar Munoz** 15:41 Which allows you to turn a… a cotling… No, but it's, yeah, an hotel context into something that you can merge with a couple encouraging context.
Now, when I created the issue, there.
Was mostly because… The ability to… Kind of like… To this, has been there for a while.
what I… what I… what I meant when I created the issue was that… If we could somehow make this Happened without users having to write any code.
So, kind of, like, automagically.
And that will essentially mean I mean, at least what I had in mind.
back when I created this, was to create an instrumentation that will Manipulate the bytecode where a corouting is launched, so that you will add this Extension, code there.
Now, based on what you said, Jason, if you understand correctly, the, there is a plan, so if I understand correctly, there's a plan for the hotel coupling, API to… allow this to be… to happen automatically, to spread the hotel context to… into current teams without… having to judge an API.
**Jason Plumb** 17:10 No, this provides an API, so you'd still have to… you'd still have to use this, right?
So I think… I think this doesn't solve our problem. I mean, the question raised originally by David is, like, do we get this for free? Like, does this solve our problem? And I think it doesn't. Even if we were using Kotlin.
I think we still have to use the APIs. This API.
**Hanson Ho** 17:33 And I think if you kind of read deeper into this, it provides a solution, to pass, or to have, the hotel context survive, suspension, within a coroutine execution.
That means that if you pause and you switch execution on a different thread, or another thread comes in, or another execution of a suspend function comes in on the same thread, those hotel contexts are preserved.
But… It doesn't mean that you are still able to wire the context in an automatic way, simply because there is no there's no concept of current, when you're executing in a… potentially in a, an environment where you're not saying everything running on a particular thread is the same trace, which is basically what automatic context propagation requires. So, to be basically able to automatically assign, what a parent of a span is at creation, there's nothing to tether it.
And, and in fact, the way we're using, local.
thread local, the Java implementation in our project is kind of a bit iffy. You kind of have to understand what everything else is going on on the same thread in order to actually be able to tell that, hey, is this the appropriate thing to do? Which is why sometimes with execution of HTTP requests.
when you're doing, parsing afterwards, things may not come and go in the same thread. And if that's the case, the automatic context propagation will not work. This bridges a gap in some execution scenarios, but it doesn't ultimately solve the model problem, which is what we have.
In the sense that we're not profile… we're not tracing execution of a bunch of things on a particular thread, or to originate from a particular thread. We are… we are… we are conceptualizing traces in a different way.
So, I don't know if there's ever a way to do this automatically, just like the way the JS folks, don't have a way of doing it automatically, because everything runs on the single thread, but everything is not one trace.
**Cesar Munoz** 19:58 Got it. Thank you. I mean, it makes sense.
And I'm just realizing.
that this is a PR. So, I thought it was an issue, I don't know why.
Probably it's quite late for me already in the day. I thought Jamie was talking about that.
project that I just shared in the chat.
It's very similar, but I get that this is… something… what Jamie's had in there should work for all.
other platforms.
**Hanson Ho** 20:28 Yeah, it's probably exactly… The implementation's very… probably very, very similar, if not exactly the same.
**Jason Plumb** 20:35 Yeah.
**Cesar Munoz** 20:37 God.
Yeah, trying to propagate context Automatically, definitely would require some… thread stuff that, as you say, maybe is not the, maybe it's not ideal.
And probably not even possible in other powers, so… yeah, it's a tricky one.
**Hanson Ho** 21:03 By default, there is no automatic context propagation on Kotlin, or on OTel Kotlin. You can use, the Java thread-based one.
And I think using a Java thread-based one, and this, this, the new API can simulate what you would previously get, on… on Java. And if you are running, basically, you know, creating a backend service with Kotlin, then that… this stuff definitely works, and you can use it with coroutines, assuming you're executing on a thread level.
But… the… the Android use case is probably a little trickier than that, or a little bit more tricky, so…
**Jason Plumb** 21:45 Oh, I had… I'm just now seeing this. Do you see how many thumbs up this issue has?
That's gotta be a record. I mean, that has to be our number one issue right now. There's a way to sort this.
Reactions. Thumbs up.
Yep, that's our number one.
Like…
**Hanson Ho** 22:09 Bye.
**Jason Plumb** 22:09 Fourfold. Like, way more than any other one.
So, you know, we're supposed to be using… You know, reactions as, like, an indicator of interest from the community, and that certainly seems to have more interest than any other issue right now.
I'm… I'm learning this as… as this call unfolds, so… Cool.
And it has been around for two and a half years, so it's… yeah, getting some traction on that would be nice.
The question then is, like, what do we do about it? Like, we had it slated for 1.0, we dropped it. What do we do about it now? I think there are certainly enough Android users using coroutines for it to be important.
We could look at mimicking what that Kotlin PR does, or using the Java extension.
I just don't know what the right approach is right now.
**Cesar Munoz** 23:06 in the Java station.
has always been there. It's… it's that… it's… it's the automatic using of it, but
**Jason Plumb** 23:15 Yeah.
**Cesar Munoz** 23:16 If in the future, when we switch to autocoupling, It won't be possible, or… If I understand correctly, then… Then, it's probably not worth… I mean, we could create an instrumentation right now.
That does it, and it's optional. Maybe, I don't know, maybe that… you know.
Help.
**Jason Plumb** 23:42 Yeah, yeah.
**Cesar Munoz** 23:46 Included in the edits.
**Hanson Ho** 23:50 Any way to make this easier would be… would be… would be… and more transparent would be good, even if it doesn't solve all the cases. If we explicitly want to opt in, and say, hey, I do execute, you know, as if thread local or code is a thread local, then I think it's perfectly reasonable to have it automatically wired up via the DSL or something like that.
how we do it under the hood, you know, maybe when we switch to Kotlin, we can use that. Until then, we use, you know, whatever we have in the Java. But I think, on the surface, it's a reasonable thing to automatically opt in, or easy way of opting in and supporting.
**Jason Plumb** 24:27 I mean, anything that's bytecode weaving has to happen at build time, and therefore is kind of implicitly opt-in.
Until we have the Android… Open Telemetry Android Gradle plugin, or whatever. Until then, everything is opt-in for byte time, like, build time, bytecode weaving.
**Cesar Munoz** 24:44 Yeah.
Well, I, I, I can, I can take a look.
at these instrumentation?
**Jason Plumb** 24:59 It seems pretty cool, I mean, people… people want to use it, so… Yeah, I think that's awesome.
David, thanks for bringing that up. That's been out there for a while, and I had no idea that it had so many thumbs up. I certainly know that people are leaning toward coroutines more and more.
Like, as of 7 years ago, or whatever.
**Cesar Munoz** 25:19 Also, I forgot about this, so thanks, David, for… reminded us.
**Hanson Ho** 25:26 I just posted something in the chat, Bugsnag has, an implementation that allows child coroutines to basically take the parent's, contacts. So, it's another… implementation. You still need the… the wiring.
But it's another thing to consider, to be able to, like.
declare, hey, we can support co-teen context propagation via… Via this way. So…
**Jason Plumb** 26:01 Cool.
I'll put it as a reference.
**Hanson Ho** 26:10 Like, there's… there's… there are means to do it, it's just the… the automatic and how you actually set that up, wire it up, is… is the… The challenge right now, so…
**Jason Plumb** 26:21 Yep.
**Hanson Ho** 26:21 And documenting what support means.
So people don't get, don't get, surprised.
**Jason Plumb** 26:29 Cool. David, any other comments or questions on this before we move on to your next topic?
I don't hear anything… Still don't hear anything.
Alright, well, feel free to jump in if that changes or we're missing something, but I want to move on to your next one.
Which is… let me close some tabs… Crap!
Yes, leave sight. Oh yeah, I do have comments, sorry.
I don't care about those comments. Here we go. Okay.
I went too aggressive there. Nope.
Here we go.
Next one is this one.
Oh yeah, what was this? So… Add hotel information for hotel span annotations.
**Hanson Ho** 27:37 Oh.
**Jason Plumb** 27:41 Don't know what this is.
Build time auto-instrumentation for with span, okay.
And why did it get closed? So this was last year, late last year, and it got closed… for being stale. So we needed author feedback.
from January, and they disappeared on us, so… I think if you want to reopen this, it's totally fine.
It seems like there were some comments… Cesar did a review… It was originally draft.
They took it out of draft.
Says I reviewed it.
There's some comments… It looks like maybe they made these comments because it's outda… made these changes because it's outdated, outdated.
And maybe this was still open?
But… They did have a couple of follow-ups. Yeah, I think reopening this is great. Reopen this and tag them and be like, yo, this got auto-closed, we want to continue it, are you around to help us? What's left? Because it's probably out of date now, too.
You have this button available to you, David?
**DavidGrath** 28:52 And if… Yeah, I think I do.
**Jason Plumb** 28:54 Okay, cool.
Yeah, since you brought this up, I'll let you do that, but I think it's… I think it's great to do it. I have no hesitations with this. Cesar?
**Cesar Munoz** 29:01 Yeah, sounds good to me.
Thank you, David.
**Jason Plumb** 29:05 Interesting feature, like, I think it's kind of cool.
**Hanson Ho** 29:09 is with Span? I thought that was part of Contributor or something like that. I thought something existed already, in instrumentation, or maybe, or something that does annotation-based. Is it just wiring it up on Android, or… Yeah.
**Jason Plumb** 29:22 Yeah. Okay. Yeah, the job instrument.
**Cesar Munoz** 29:24 does exist.
**Jason Plumb** 29:25 Yeah, yeah.
**Cesar Munoz** 29:25 Yeah.
**Jason Plumb** 29:27 And it doesn't use annotation processing, it uses bytecode weaving.
**Hanson Ho** 29:31 Okay, that's why, because we don't have that. This is… okay, got it.
**Jason Plumb** 29:35 Yeah.
Cool.
Whoa, why am I pink?
That's weird.
**Hanson Ho** 29:51 Always pace without format.
**Jason Plumb** 29:55 Is there a special key for that?
**Hanson Ho** 29:57 It's like Shift Control, or Shift-Apple V, or something like that, I think.
**Jason Plumb** 30:09 Alright.
Yeah, well, however I will butcher your name, I'm so sorry.
Joao.
**João Oliveira** 30:15 Joao.
**Jason Plumb** 30:17 Joel.
Close.
**João Oliveira** 30:19 That's good.
**Jason Plumb** 30:20 I will always only be close on that, I promise, I'm sorry.
**João Oliveira** 30:24 Yeah, it's, honestly, for non-Portuguese-speaking people, it's very, very hard. So, really, any approximation is fine, I'm very much.
**Jason Plumb** 30:34 Thank you, bye.
**João Oliveira** 30:34 No. No worries.
**Jason Plumb** 30:36 Thank you for being patient.
and understanding.
**João Oliveira** 30:38 none.
Yeah, yeah. This is actually a bit similar to, what we're just… what we were just discuss… discussing. There's this open issue, so basically, we, we had, a customer that was interested in having TTID, TTFD, this is something we measure ourselves, so I sort of took around.
On this issue, found a closed pull request.
It seemed to have a bit of traction, there was some discussion, there was, like, an open debate on some things, and then suddenly, like.
Sort of ground to a halt.
I try to reach, the author, they don't really seem… I try to reach them on the CNCF Slack.
I didn't touch the… the… any of the pull requests, to be honest. I don't know exactly what sort of the polite way to do this is, but we are very much interested in this. We would be happy to move it forward. I wonder if someone in this meeting… for this? Do you have any context, you know, why it tied down?
**Cesar Munoz** 31:52 Yeah, I remember, vaguely, Under some comments there.
Because it was tied with the semantic conventions PR, and then we were kind of discussing The attribute names, and… Shoot me out of stuff.
Across those two, and… I think for the semantic convention, I was waiting for some answers.
And… but they didn't game.
income, so, yeah.
She got closed.
But, if you're interested, yeah, This would be a nice, addition.
**João Oliveira** 32:31 I'm happy to, like, recompile, try to recompile anything that's still open, try to reach out to people that were… participating, to get it, moving again.
**Hanson Ho** 32:44 I'll also kind of take a look at what you fully want to actually achieve, because I think You know, the actual… the first line says, activity instrumentation, so are we talking about, like, every activity start? We want to actually know when the activity is first created, when first draw happens, or… because… and then… and then stuff got looped back into app startup, which is, I think, a tougher problem.
Because of what you're determining to be, you know, app startup. So, the folks asking for this on your side, are they looking for, something to time the creation of activity, when it first renders, or is it more like an app startup thing, where they want to end it on first draw?
**João Oliveira** 33:28 Basically, like, I've been trying to find the time to look at exactly what our process is, but the way, the way we do it at Taylor with our own SDK is… so there's, there's basically, like, like, there's 3 months in time.
There's the first one, like, that's immediately when the process starts.
So that's, that's, like, say, D0.
And then, as soon as anything that's not the splash screen is displayed on… is displayed.
That's… let's, you know, let's call it T1.
And if I recall correctly from the pull request, that would be TTID, and that was sort of settled on, I think, TTFT, final… time to final display is the more complex one. That would be, let's call it T2, which is when the final thing is… is, It's completely drawn, and that… on, on our, on our own SDK, and even on, on, on the PR itself, that usually involves the API supporting sort of the, the application to self-report on, hey, a finished, a finished drawing. So you don't, really detect that. You, you support the call. And I think one of the active discussions, and I apologize if I'm not ready to discuss specifics, it was, exactly how we should transport that, or emit that signal that, you know, hey, I've finished… I finished drawing, you can… you can count TTFD.
**Cesar Munoz** 35:17 I don't remember, vaguely, there were a couple of questions… And now that, actually, Jason was scrolling through the comments, and I saw the… like a diagram, because I also didn't understand exactly what they wanted… capture, so I even draw something like, do you want this part?
**João Oliveira** 35:37 Yes.
**Cesar Munoz** 35:38 or this part.
Like, what part of the, you know.
lifecycle they wanted to capture. It was not clear to me, and also, I think there was a debate over using spans or logs.
But yeah, I… Right now, I don't remember the details.
**Hanson Ho** 35:56 So, if you're talking about, like, draw stuff, we're not even talking about this life cycle. We're probably talking about the window lifecycle, like, detecting, like, the first frame, and then… and then if you're talking about, a final display, you're talking about, like, a whole different a process, like, Android has, like, a report for Straw, that API. So… this is where things are… gets confusing, because we're talking… if you even bring an app startup into, you know, the… the end of the equation, there's probably four life cycles we're dealing with, and trying to mash things into… into one coherent thing, which is… which is… which is difficult.
So, to start off with.
Some of this discussion talks about drawing trees and firing listeners.
That… that is, A very, very tough thing, because things don't… stop. You could potentially render, render, render. First is easy, because you… easier, because you're just detecting, you know, frames. And it's… it's not… it's not even, you know, looking at the… the actual… what is actually producing the frame. Final, potentially, it is listening to a, an API call, or, or, you know, wiring using the activity stuff.
So, I think deciding what you want to measure.
first, and then kind of narrow the scope into, like, the most useful, smallest bit, and then expanding it out. So first, maybe, if we have initial activity instrumentation that does, the activity lifecycle instrumentation stuff, like, create, you know, start resume, maybe we want to have something after resume, or not, I wouldn't say after, would be, like, alongside resume.
That reports, like.
frame detection drawing, so that you can, you know, either add it to the existing trace, or create events that would, you know, augment, whatever instrumentation you have right now.
finding the precise timing, and then firing an event is the easiest thing to do, but it may not be useful enough. You may want, like, your customer may want, like, a timing. So, you know, then you have to figure out where it starts and where it ends, and then create a span for that, if it's, like, a timing thing you want. And if there are intermediate steps, you may want to add, you know, span events or, you know.
Child spans, probably not child spans.
And go through there. So I would… I would… just look at the requirements first, and then kind of build it back up, because I think this issue went a lot of different ways, and that's where things got a bit, I think, tripped up. I think going from small to big is better.
**Cesar Munoz** 38:40 I, I agree.
**João Oliveira** 38:40 I would not be against, sort of, separating the two things a bit more, rather than doing one mega pull request.
Because they generate… I mean, they have a common sort of T0, like we were saying, but then the two timings are vastly different things.
And I would happily sort of organize… try to organize these in two PRs, and… Organize the discussions between both of them.
**Hanson Ho** 39:09 So…
**Cesar Munoz** 39:10 Sounds great, and I just wanted to add, on top of what Hanson said, that I think the reason why we like, went back and forth and sideways, I don't know if that's an expression.
that's.
**João Oliveira** 39:23 Yeah.
**Cesar Munoz** 39:24 there was not a clear, like, use case. Like, it's like, of course we can do a lot of stuff, like, we can put a lot of, you know, callbacks and lifecycle shenanigans all over the place, and report Telemetry for it, but, like, it was not clear.
how was that useful? And then we didn't know… because we didn't know what was the use case, then… We didn't know How to present the data, or exactly which parts to collect of the life cycle, if that was the case, or if it overlapped with existing instrumentations that maybe what's… Better for users to use instead of this kind of stuff, so… It sounds to me that you do have some, some use cases, and I think that… that's… that's, major improvement from that side. That's the case.
**João Oliveira** 40:21 Yeah, that's maybe something we can help with, in sort of two ways here, because this is something we manage with Datalog SDK, and existing customers are using. And in this case, like, we can even reach out to this particular customer who's, like, experimenting with hotel, and specifically said, hey, ATT ID, ATTFD, they're very important to us.
And it's, it's pretty easy for us to reach out to them and say, hey, exactly what are you looking for here? We're trying to… No.
port this to… to OTEL, and That would be… Understanding exactly what they want to measure is… is…
**Jason Plumb** 41:00 Yeah, I think that's great. I mean, and I want to remind everyone that, like, we don't have a spec for these things yet. We don't have even semantic conventions for them, so having a development in, like, a piece of instrumentation that does something is still, I think, better than instrumentation that does nothing, or no instrumentation, because at least we can establish a baseline, and from there, we can gather feedback, and users can say.
You know, that's not really the time I was looking for. You're ending it too earlier, I really need it over here. We won't get those feedbacks if there's no instrumentation at all. So I think, you know, incrementally, having some in here, splitting up the difference between those two timings, awesome.
If you want to chime in on this issue, we can assign it. I think taking the existing art in the form of those other two PRs, and borrowing from that, if the authors are not responsive, and they haven't come back, then I think that if you need to borrow parts of that code, I think it's totally fine. It's still in the repo.
**João Oliveira** 41:55 Yep.
**Jason Plumb** 41:56 Yeah. Okay.
**Hanson Ho** 41:58 So I pasted in the Embrace implementation of App Startup, and we try to flatten this by basically having various instruments detect what's happening on the platform.
firing events for that, and then handling it in a way to basically piece the information together. It is specifically for app startup, but, you know, removing that and tying it to activity creation is also you know, fine.
we did this with a span and child spans. In retrospect, we probably would not have done that, knowing what we know now. So I wouldn't take… I wouldn't… I wouldn't look at the, the data modeling as… as something that's like, you know, crib from. But… but certainly the idea of how do we kind of normalize These disparate life cycles, that fire, unfortunately, async a lot of the times, and are processed async.
how do we take that information together, and they basically bolt together instrumentation? It's not quite like, diplom instrumentation in that, you know, you record as it happens.
sometimes you have to basically figure out what the hell's going on, and then create the span, just because you don't really know if it's a cold start, if you want to do app startup stuff, which actually, the initial one, I would… I would not tie an app startup, I would… I would just look at rendering an activity that makes it a lot easier.
But yeah, feel free to…
**João Oliveira** 43:27 I think, yeah, I don't know if we want to introduce that immediately, but one thing we do with the sort of metric that we end up emitting for this, is we separate… we tag it by, sort of, cold start, or around cold start, because that makes these timings widely different. Yeah. And I guess the question a lot of times that you're trying to answer is, you know.
How long is the user taking to, like, you know, see anything, or see the whole thing?
And, you know, if… if… If, You want to understand how… how it is on a cold start, and you… you know, it's sort of polluted with timings from a warmed-up start that… that's… Much faster.
The information gets a bit… Weird.
There's…
**Jason Plumb** 44:17 I think there's something in the agent right now that… determines cold start? I can't remember. I feel like that's in there somewhere. It would be nice to have that as, like, a global attribute for the rest of the run, right? Like, if we had something that was, like.
If we detected cold start early and had a global attribute that we could slap on everything.
That might be nice.
**Hanson Ho** 44:40 Yeah, it's… the platform gives us a bunch of signals, and how we turn them into telemetry or metadata is up to us.
**João Oliveira** 44:52 I guess that sounds, complex enough for a different discussion, maybe, and then we'll…
**Jason Plumb** 44:57 Totally.
**João Oliveira** 44:58 Then it'll converge.
**Hanson Ho** 45:01 It really depends on where you want to, like, where your customer wants start to come from, because that is an extremely loaded question. If it's activity… if you want to basically measure the creation and the activity to when it renders, that's a much more constrained and easy, thing to do. But I suspect when they say words like TTID and TTFD, they're talking about startup.
Which, the hard part actually isn't… isn't the display, it's… it's determining where the start is. So if you want to extend it, it's… you can basically have what your expectation currently does and extend it out, basically, where it stops.
If that's exa- if that's really what they want, so…
**João Oliveira** 45:45 All right, so I'll, you know, I'll take all of these actions, I'll maybe separate the two things, I'll go through the open discussions that we've, we've, before, and I'll also try to… Shine a little more light into exactly what we might want to measure.
**Jason Plumb** 46:04 Yeah, yeah.
**João Oliveira** 46:04 We'll see… we'll see from there.
That's great. It's like, it's not gonna be an easy one, but at least it's.
**Hanson Ho** 46:12 It's a constellation of telemetry from a set of shared signals, so…
**Jason Plumb** 46:20 This is a complete non sequitur, but I wanted… I meant to ask, and I forgot to, so I'm gonna do it before we get to Hanson kind of final topic here. Ben, I think you said, that one PR was from your colleague. It seems like they have been, doing a bunch of reviews in the repo.
**Ben Joseph** 46:39 Huh.
**Jason Plumb** 46:40 Are they not able to join SIG, or are they in a different time zone, or…
**Ben Joseph** 46:43 So today we had an all-hands, so I covered the SIG and.
**Jason Plumb** 46:48 Okay.
**Ben Joseph** 46:48 Over there, but, like, he'll… he'll be joining.
**Jason Plumb** 46:50 Okay, cool.
**Ben Joseph** 46:51 Okay.
**Jason Plumb** 46:52 Yeah, just pass on the fact that it's… those reviews are noticed, and they're very helpful. Thank you. Yeah.
**Ben Joseph** 46:57 Absolutely. I'll let him know.
**Jason Plumb** 47:00 Yeah.
Alright, Hanson Semkov, we have about 8 minutes.
**Hanson Ho** 47:07 So, yeah, basically it's one question. How do we want to do SEMConf? What we're going to generate, what is already generated are constants for the main core OTEL semantic conventions.
anything that we define ourselves in a federated semantic convention repo for Android, or eventually whatever upstream end-user one exists, there are no default source files generated. And it's fine, because we could generate everything in Android.
And this PR, in fact, is what it does. I'm importing events upstream and generating it, ourselves, and using it, because the upstream, events classes uses the Kotlin API, and we want to use the Java API. So… all I did was basically, hey, import these events, do the generation, and then use it.
I feel… I feel the core dependency for Spanish conventions really is the registry. So, the fact that we generate, all the source files for us to use internally.
is perfectly reasonable. I don't think… it's maybe a bit more overhead, you know, to run it, but we're generating some classes, it's gonna be fast. So I guess what I'm proposing here is.
Let's just generate everything we can't get upstream.
And not worry about things that don't exist upstream for constants or things like that.
when we want to… if they exist one day, it's easy to turn off our generation and import whatever they generate. But this gives us the flexibility to basically have classes the way we want to have them. And for constants, it doesn't really matter, because it's just strings.
But eventually, we may want to have attribute keys, we may want to have… I mean, for the events, it actually takes in a logger, and then admits the event. So, implicitly, there is an API, a dependency, and to be able to generate our own classes means we manage what API we depend on, in terms of version. So, I feel this is probably a… the correct way of generating and using semantic conventions, and I kind of want to see where everybody, sits with this.
**Cesar Munoz** 49:30 I like that idea, especially the one that allows you to create events.
Just by calling this generated code, that's pretty cool.
So, yeah, it'll be off… so you say that we can just… we can pick and choose which… events we want from Upstream, like, we don't have to generate, like, everything, and that sounds great.
**Hanson Ho** 49:48 the filtering is, unfortunately, based on filters, good or bad. It means it could be very, expansive or very narrow. So, what I did here is just imported events, so if you look at, I think, a registry, I just imported, wait, no, actually, that's a definition. I created a definition here, it's… it's a manifest, maybe.
I don't know, it's one of the files. Events, maybe. Who knows?
**Jason Plumb** 50:19 Yeah, is it… I mean, this is the event definition, this is the manifest that says what we depend on.
And… that got bumped a version, but then also there's this, right?
**Hanson Ho** 50:32 Yeah.
**Jason Plumb** 50:33 Yep.
**Hanson Ho** 50:33 Oh, no. Oh, did I paste in the wrong one?
**Jason Plumb** 50:37 Is this the wrong PR?
**Hanson Ho** 50:38 I might have pasted in the wrong PR… Ugh, I have so many of these going. Anyway, there, there, there was a PR that basically I, I import an event, from, Oh, yeah, yeah, yeah, this is the one, this is the one. Yeah.
Sorry, yeah, the other one is… don't worry about the other one.
I'll correct it.
The other one is using upstream static conventions and generating everything, but that doesn't exist yet, so don't worry about that at all.
**Jason Plumb** 51:14 Yeah, so through this, we can import single events from… upstream, right? Like, this is what this is doing.
**Hanson Ho** 51:25 Yep.
**Jason Plumb** 51:26 So, in our registry, which already takes a dependency, On Upstream, is that correct?
**Hanson Ho** 51:32 Yes.
**Jason Plumb** 51:34 Then, in here, we can say… in the model, the slow rendering module, depend on Semconf, and then our AppJenk reporter doesn't have to do all this legwork, because we can get this event generated automatically for us.
**Hanson Ho** 51:49 Yep.
The template for that is already defined, JSON already did this, you know, it just wasn't being used, so…
**Jason Plumb** 51:56 Right, the base class of this AppJank event is, like, an OTEL event, and there's a bunch of those that we're generating with our local semantic conventions, but not for the remote semantic conventions. Yes. And this is… this PR is one example of how to do that. And I think I like it, like, so, I mean, this is supposed to read positively, if that's not clear, like…
**Hanson Ho** 52:15 Right.
**Jason Plumb** 52:16 You can just specify, like, what upstream events you want, and then we get events that… event classes, like, it's like… it's lovely. It's, like, super magical, and I kind of love it.
**Cesar Munoz** 52:27 Yeah.
**Jason Plumb** 52:27 What this also does is it breaks our… Gradle or Maven dependency on external projects, and it kind of hides those now behind this YAML dependency, and I'm not sure which one is more fragile or prone to breaking. Like, I don't have a good mental model of which one might be more robust, but I think it's more straightforward to depend on the YAML and get the other opinionated event and constant generations out of our critical path, right? Like, then we own the whole stack.
**Hanson Ho** 53:05 We could have, GitHub workflows to check that versions that we depend on are in sync, you know, things like that. There are things that we could do to basically harden.
The dependency, but what we effectively have is a… is a true federated, or I don't know if I've made changes for that, a true federated semantic convention repo that consumes semantic conventions as they were meant to be consumed, which is via registries, extending, and importing, and the code generation is, is, is… The registry that we create basically pulls in what we need.
And then the code generation is kind of, like, a little bit separate from that, which takes the merged registry and generates, you know, source files that we need. And I think that's… it's quite powerful, and it allows us to kind of own the actual source file, not, as Jason said, pull in dependencies.
That… that may not jive with what we're trying to do.
**Jason Plumb** 54:03 Cesar sounds like you like it as well.
**Cesar Munoz** 54:06 Yeah, to me it sounds great, especially those events.
Cool. Curated.
Classes, yeah.
**Jason Plumb** 54:13 Nice, and I would say… It… go ahead.
**Cesar Munoz** 54:17 Just wanted to… just to make sure then, so… Even though this PR shows events.
Are you proposing, Hanson to also replace just regular Other stuff, like just simple… Add through the names.
Constance and stuff.
weird.
Generated code in this… in this repo, or we… or we still reference those?
From upstream.
**Hanson Ho** 54:45 So… it would simplify dependency management, because right now we're implicitly taking, Kotlin, whatever version of Kotlin we take in.
and the semantic convention version that it's generating. So, I think Kotlin right now, the latest shipped one is 1.4… 1.41. So the constants from that will be for that version.
But we ourselves declare an upstream dependency on a specific version, so if it's 1.43, then… well, why do we want to wait for Kotlin to do this when we can just generate? Especially if it's something as simple as, you know, constants. So yeah, I think I am proposing severing that, and just say, screw it. We're gonna… we're generating stuff for Android anyway. We might as well expand the scope of what's generated.
Have everything in there, and then… let R8 take care of, things that are generated but not used, and so it doesn't, like, you know.
bloat the binary that we ship.
**Cesar Munoz** 55:51 Got it. Well, I think, I think… To me, it's fine. It's a big change, but I think it's fine.
And at the end of the day, it should be… transparent to the end use, so… so… That's great. Also, I'm guessing that if, in the case of events, generated classes, if they had to reference constants, it would also be easier if those constants are the same, you know.
Generated ones from the same tooling and everything, so… Yeah.
**Hanson Ho** 56:22 Sounds good.
**Cesar Munoz** 56:23 Thank you.
**Jason Plumb** 56:25 The way I kind of see it as well is that if we have to already take a Weaver dependency to generate our internal, like, bespoke Android semantic conventions events and attributes, then it's not much of a stretch to just do it for the ones from upstream that we care about, and then eliminate the code dependencies.
And then we only take the semantic conventions, YAML, dependency, and Weaver.
**Hanson Ho** 56:48 I want to say that we probably don't even need to reference semantic inventions in the Tamil anymore.
**Jason Plumb** 56:56 Right. No, I think you're right. I think we can get to that point, and that's kind of a win.
**Hanson Ho** 57:00 Yeah.
**Cesar Munoz** 57:01 Yeah.
**Jason Plumb** 57:01 Yeah.
Okay, so please review, add your… add your review to Hanson's PR, and then… what's the follow-up from this, Hanson? Like, to create another issue to identify the remaining ones, or how do we… how would you want to proceed with that?
**Hanson Ho** 57:15 I would say create an issue that says sever dependency on upstream, or on Kotlin, hotel Kotlin for SAMconv, and replace it with locally generated, and that's probably just a registry change, and changing package names of imports, if we're going to keep the existing package name that we have, which is.
**Jason Plumb** 57:35 Great.
**Hanson Ho** 57:36 trivial.
**Jason Plumb** 57:36 I put your name on that one.
**Hanson Ho** 57:38 Sure.
**Jason Plumb** 57:39 Okay, cool. Thank you. Alright, we are at time. I want to get a couple of minutes before the next, Client Semantic Conventions SIG Meeting, if you are attending that.
I appreciate you being here and showing up and helping out.
Thanks, we'll see you soon.
**Hanson Ho** 57:57 Right.
