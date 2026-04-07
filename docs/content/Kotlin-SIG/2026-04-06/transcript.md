SIG: Kotlin SIG
Date: 2026-04-06
Duration: 46 minutes
Zoom Recording URL: https://zoom.us/rec/share/GrzGFtSv7a3Pu0oBwob0dz-lQYeZw80vPP9O6BR3OB8kByZzYUgBV939kIirKgVN.41jsIp3bTa_rK2av
============================================================

## Zoom Recording Transcript

**Hanson** 00:05 Oops.
Can they not wish?
Easy.
So, it's a real dog.
Hello?
**Jason Plumb** 01:25 Good morning.
**Hanson** 01:28 How's it going?
**Jason Plumb** 01:29 Pretty good. My calendar says that, Easter is observed in Canada today, is that true?
**Hanson** 01:35 Kind of.
Kids have school off, some things are off, but it's not a… public holiday in British Columbia. Okay. It is in Ontario, so it's always, it's always, like, you know, who knows? So, Yeah, so I'm working.
**Jason Plumb** 01:58 That's cool.
Screen shared here.
**Hanson** 02:04 See lots of agenda items from, from Harlos.
**Jason Plumb** 02:08 Yeah, I was kind of expecting him to join then, but… Might just be the two of us, we'll see.
I saw some typing in here earlier, so maybe he's the wombat, or are you the wombat?
**Hanson** 02:23 I should be logged in, so…
**Jason Plumb** 02:25 Okay.
**Hanson** 02:28 Oh, I'm a unicorn.
Oh, weird. Why am I anonymous?
**Jason Plumb** 02:31 Oh, it's rare! It's the rare one!
**Hanson** 02:41 You're the Quagga?
**Jason Plumb** 02:44 Yeah, you can't see yourself, though, apparently.
You know, like, I'm not in this list, but I believe that I'm a quagga.
**Hanson** 02:51 Yeah, I don't even know what a… is these all Australian animals, I guess?
**Jason Plumb** 02:55 Yeah, the Australian unicorn.
**Hanson** 02:57 Yeah, exactly.
**Jason Plumb** 03:01 Alright, well, we'll give it a couple of minutes while Carlos is joining, and we don't have to take up the whole time, obviously.
**Hanson** 03:08 No.
**Jason Plumb** 03:08 I did want to, just touch on, and we can talk about it here in case Jamie watches the recording or whatever, but.
More of a maintainer thing, but we do have… a few remaining security issues in the scan. It was… we had, like… last week we had, like, 15 or something, and, like, half of those were high, and I spent… more time than I should have, looking at and thinking about how to fix these, and it turns out that I think a lot of them were redundant.
And when I made one small change to one, like, it fixed, like, all of them in one go, so I forget what that pull request was. It was, like, one of…
**Hanson** 03:46 Is it the read one? The read permission, the default?
**Jason Plumb** 03:49 Yes, this one. This fixed, like, 7 of those, or 6 of those, or something.
So just having this at the top level fixed a bunch of the high warnings. So without this, you know, you get token default permissions, which means that any job potentially could do something nasty. Anyway, this helped, and so it's in much better shape now. We do have… missing branch protections, so I will add those today.
**Hanson** 04:15 Okay.
**Jason Plumb** 04:16 That will happen through Terraform in the admin repo. And then… Yeah, aside from that, I think we're in pretty good… though, there's another one that's marked high, and it's a default… setting scan… a scan setting for new repos. So, your repo has to be around for, like, more than 3 months before it's considered maintained. So we're, like, we're still flagged as, like, an unmaintained repo.
**Hanson** 04:43 It's funny to me.
**Jason Plumb** 04:44 the mitigation for that is, like, do nothing, this will fix itself if your repo is active. And I'm like, okay. So I expect us to be fine after this. We should be in much better shape, and then maybe we can consider putting a badge on this thing.
You know, like, at the top of the README.
But… cool.
That's all I wanted to talk about. So, we are in much better shape.
**Hanson** 05:08 So basically, we're always gonna have a high security warning until 3 months. Like, for 3 months, basically.
**Jason Plumb** 05:15 That's what it sounds like, yeah. It's like, this is a new project, you should be careful, which I think is, like, a reasonable… thing to warn people about, you know? It's worth flagging.
**Hanson** 05:26 Not something we can fix.
**Jason Plumb** 05:30 Yeah.
Yeah, there's one downside with the release protect… the branch protection on the release branches, and that is It can make… patching a little bit harder, because it does, like, small little tweaks do require approvals then, but it's the right thing to do, and I think we have that elsewhere, so…
**Hanson** 05:58 Nope.
**Jason Plumb** 05:59 I will just do that today.
**Hanson** 06:00 Yeah, I think…
**Jason Plumb** 06:01 Carlos…
**Hanson** 06:02 Hey, Carlos?
**Carlos Alberto Cortez** 06:04 Hey, hey, hey!
**Jason Plumb** 06:07 Hey, hey, hey!
So, you have a bunch of agenda items, are you ready to talk about them?
**Carlos Alberto Cortez** 06:12 Yeah, I am, yeah. You actually, yes, yeah, actually, I was reviewing them before the call to make sure that, they're aligned with what I was checking.
Do we jump into them?
**Jason Plumb** 06:25 Yeah.
**Hanson** 06:25 Yep.
**Carlos Alberto Cortez** 06:26 Sweet. So, yeah, as you may remember, Jamie was asking for, you know, doing a logging stability process.
Single's going through the… all of the items that I see that are important and real blockers, like, not minor stuff.
One of the things that probably is not very obvious is that if we want to make logging stable, it means that anything that exists at the API level that… can be used at the API level, has to be stabilized. That goes with attributes rotator, for example.
But that also, includes are the OpenTelemetry object, you know, the one that you use to fetch a tracer provider, logger provider, etc.
And also other stuff that exists there, like context. So, long story short, I would say that even going 1.0 for API, for logs.
it will be a longer process than expected, I think.
that's the reality, and this is something that has happened for other SIGs, like… When they were… stable with tracing for the first time.
they had to also make everything else at the API level stable. I think that the exception was when you were adding… when Six were adding a new signal.
But everything else is already there. Like, attributes mutator, let's say, context, everything else is already stable. And then you are actually just adding a new API, like, let's say for metrics, for Java in the case of Java.
So, in that case, you're making only that part of the API stable, and that's fine, it's a small thing, but because everything else at the API was stable already.
So that's the thing that we have to review. And part of that is, for example, that, correct me if I am wrong, but there's no new implementation at DPI All the interfaces are defined there, but you actually need to import to separate new package.
If that's the case, that needs to change, because the idea is that instrumentation or users can just import the API and actually call the API, even if it does nothing. But, you know, like, so you don't have to implement, like, to bring something else and install that, you know?
**Jason Plumb** 08:45 You're talking about this thing, right?
**Carlos Alberto Cortez** 08:47 Yeah, correct.
**Jason Plumb** 08:49 So what about this? You want this to be stable first, right, is what you're saying? Because this has the OpenTelemetry object?
**Carlos Alberto Cortez** 08:54 That's correct, yes.
**Jason Plumb** 08:56 So the challenge with that, though, is that it depends on all this stuff, like.
**Carlos Alberto Cortez** 09:00 Yeah, right, right.
**Jason Plumb** 09:01 So it's a catch-22, right? How do we deal with that? Right.
**Carlos Alberto Cortez** 09:04 Rick, yeah.
**Jason Plumb** 09:05 room.
**Carlos Alberto Cortez** 09:05 Yeah, actually, that was the last point. I think that that's something… we can jump into that now, since you mentioned already. Yeah, I don't know, honestly, what to do on this for this, and this is also something you will have to decide, because The thing is that… as I was mentioning in the example of Java.
They… for them, it was easier, but at the same time, for example, Java has this incubator.
Like, artifacts, where they are adding experimental stuff.
But for… and HC has to find ways to do this in the proper way.
**Jason Plumb** 09:43 Yeah.
**Carlos Alberto Cortez** 09:44 And, yeah, so that's, I would say, the challenge.
Yeah, I think that, yeah.
**Jason Plumb** 09:52 We do have this experimental API attribute annotation that we've been putting on stuff, and that's a signal to users that a certain piece of software is not yet determined to be stable.
**Carlos Alberto Cortez** 10:04 Yeah, I would like to, check with other Sikhs how this, whether this is enough. I think… so, honestly, I think that the fear in the past is that So this is, like, also, like, a kind of funny thing, because I think that we didn't want to expose Experimental stuff easily.
Because then users could start using that right away.
And then come complaining once this becomes stable, and maybe there has been a change between what they were using, even though you were telling them in the past that That wasn't stable.
**Jason Plumb** 10:39 Yeah…
**Carlos Alberto Cortez** 10:39 This whole idea.
**Jason Plumb** 10:40 Stable by default, yeah, I know that discussion.
**Carlos Alberto Cortez** 10:44 Yes.
**Hanson** 10:46 I think this is pretty typical on mobile, and it's so much easier to change, I think, on mobile from version to version. I think making our ex… intentions explicit is what's important. I don't think we're gonna use this, for all non-stable, artifacts, I think we were actually truly putting… I think we're thinking of a more evolved use of this. Actually putting these on things that are truly, like… like, it's almost like, by default, it is stable-ish. When you look at… you look at the designation, whether the API is stable.
And then there are, amongst the things that are marked, in the API as unstable. There's gonna be more unstable, which is, like, the experimental, and then there's, like, the less unstable, which is ones that are not marked as experimental. So I think the top… at the top level of open telemetry, that probably should be removed, as we… as we get to… to closer to stabilization. But I think the way we… we work around the, the, the whole, you know, one depends on the other, and, you know, is, is, marking certain, members as either experimental or, or, well, I guess that's the only way in code. You said, you know, the tracer provider is experimental, but the entire, OpenTelemetry object is… is not. That is probably something we could discuss, but, I… That's… I think, I feel that's a good way of telegraphing what the intention is.
**Carlos Alberto Cortez** 12:24 Yeah, yeah, I think that could be the plan, if we… if we agree on that… on the… on the fact that, you know, putting this experiment… experimental API annotation is, It's actually conveying that message, yes.
This probably may be a silly question, but if you have any reference or blogs or anything where… I can go and check that actually the mobile space is more flexible when it comes to changes.
like, you know, compared to more, like, server-side stuff, it could be great for me to know, in case the TC asks, because I will probably have to talk to them briefly about this.
Yeah, I will explain that. I do remember you, Hansel, mentioning that in the past.
That, the ecosystem for mobile is much more flexible and dynamic.
So yeah, I remember that part, for sure.
**Hanson** 13:14 Yeah, the platforms themselves are, like, well, I guess with the platform here being, Android, are pretty rigid in terms of, like, declaring certain API to be, deprecated and, you know, but entire libraries, often ship, and people use it in production, in alpha, And worst is we've taken elements of a package, like Gradle or something like that, and, like, monkey patched it, because they couldn't fix it.
So things like this happen all the time, and the good thing is, you could do things, if it's a feature that you can block off, you could use feature flags to kind of, like, enable, disable, and worse comes to worse, it's, you know, you could just have a new version out, and it's… it's generally pretty safe. So, I think we should definitely be, mindful of what we declare as stable and non-stable, but until we actually have version 1, you know, it's all unstable, and we're at a point where there are things that we think are close to being there, and I think classif… or having a way to identify that subset, and having that out there, and then incrementally moving the stuff out. But I definitely agree that, like, anything that, like, context has to be stable, mutator attributes has to be stable for, you know, any API that depends on them to be stable. So I think the next step is to figure out, and list basically all the other.
what do you call it? Sub-APIs, or component APIs?
and get those stable. I feel like we've implicitly said that, you know, we're pretty happy with it, but they still have the experimental API, or some of them still have the experimental API annotation on it, so I think we should, Remove them, or, or review them and then remove them, so that we could, like, at the very top, say, hey, context is good, attributes is good, because we modified, you know, all that.
For that reason.
**Jason Plumb** 15:22 Would it help us here to also have these APIs be in their own module?
Like, right now, you know, we're publishing stuff presumably with, like, alpha suffixes, and we have these sprinkled in here, but, like, logging… is just part of the common API, it's not its own module, right? And so, like in Java at least, you can depend on and use only the logging API, or you can only have the tracing API. I'm pretty sure, I'm 93% sure, that those are different artifacts.
**Carlos Alberto Cortez** 15:54 Really? .
**Jason Plumb** 15:56 on the API, in the SDK for sure, but in the.
**Hanson** 16:00 I think they are different artifacts.
**Carlos Alberto Cortez** 16:03 I… well, if I remember correctly, in Java, they are in the same artifacts, but the SDK components, they are not imported, like, they are different packages.
**Hanson** 16:13 I thought API, the API package included…
**Jason Plumb** 16:17 None of the same. No, it's one.
**Hanson** 16:18 Are they the same?
**Jason Plumb** 16:19 It's one for the API.
**Hanson** 16:20 Okay, so maybe that's the SDK, then.
**Jason Plumb** 16:22 So, really.
**Carlos Alberto Cortez** 16:23 Yeah, he's.
**Jason Plumb** 16:24 Yeah, yeah, so really, when we talk about, like, logging API stabilization, we're just talking about API stabilization.
Because that's one module, right? So that's a big surface area, or bigger. And so I think it's good to call out stuff like the attributes mutator, all this stuff that's, like.
you know, available in there, those also have to be stable.
Yep. Where is that attributes mutator?
That's also in the API. So yeah, we're talking about, like, basically doing the entirety of the API at once.
**Hanson** 16:55 So if you look at the API, the API, file.
**Jason Plumb** 16:59 Yeah.
Which one?
**Hanson** 17:03 Jvm.
Probably.
**Jason Plumb** 17:07 Yeah.
**Hanson** 17:08 Everything here has to be stable.
**Carlos Alberto Cortez** 17:12 Right.
**Jason Plumb** 17:13 I think that's correct.
**Hanson** 17:17 So basically, Tracer… I mean, it's, it's, it's Tracer and logger.
Essentially has to come together.
**Jason Plumb** 17:25 Yeah, unless we want to move… part of it out, right? So that's another option. We could move, for example, if we wanted to do tracing first.
Or if we want to do logging first, we can move tracing out, stabilize the API, and say, we just support logging. Logging is stable, we have a stable logging API, and then piecemeal start moving pieces of tracer in.
Right? And then… Yeah.
But once it's stable, you know, the only things that come in have to be stable immediately.
**Hanson** 17:55 Well, how far… I mean, I think we wanted to get that done because we thought it was going to be quicker, but effectively, if the overlap is, like, 95%, and we're just talking about, you know, the 5% that is new in Logger and Tracer, why don't we, you know, have a list of, like, what do… like, moving stuff around like that just to be a month early or whatever, in stability, seems to be a heavy lift, and I'd rather not do that, especially the artifacts will be inconsistent and all that stuff. I mean, if we started here, everything here, let's just… I would wanna… I would just wanna wait and just do everything at the same time, if we're just talking about the API, especially now that we don't have metrics in here.
So, we're just talking about those two.
**Carlos Alberto Cortez** 18:40 Yeah, actually, there was a thing I was wondering, like, it's up to you in the end, but there are those two options. Either you said something that, you know, Jason said.
Which, which is what other cities.
If there was a rush, or you think that tracing is going to take 3 more months. But if you think that you can wait in the timeline, you know.
is still fine, then I would suggest that, yeah, we wait a little longer, and we work towards, you know, towards having both of, like, tracing and logs API ready, even if the SDK portions still come after, you know?
**Jason Plumb** 19:12 Yeah…
**Hanson** 19:13 I want to say the more controversial stuff in Trace, that is yet to be, you know, conceptually stable is the context stuff.
Especially the current context. And if that is required for logs anyway, because we have contacts, then, you know, once we figure that out, tracing could be pretty fast. So, I think, we can start the discussion in, probably in Slack, and then continue next week when Jamie's back. But, I think if the option is to, like, do a bunch of, like, moving around.
I'd rather just… do it here and wait however long it takes, because I don't think it's that long.
**Jason Plumb** 20:00 I think I agree with you, it's kind of a lot of thrash to do that, just for, like, very little benefit, so… okay.
What else is being called out here, though? So, like… So we agree that, like, what we're talking about is, like, stabilizing this surface area, right? This is what we need to stabilize.
**Carlos Alberto Cortez** 20:20 There, also, the API needs to have a no-op, implementation.
**Jason Plumb** 20:25 Yeah, yeah, yeah, so that's… that's a good one that… so that doesn't exist yet?
**Hanson** 20:29 I think it's in a no-op extension. I don't know if you have to implement, excuse me, bring in a separate project, but it is not… I think it's one of those things where it is… part of what you need. And… like, I think that project is… is… Like, I think… I think… I don't recall what the specifics are, but there was a reason we didn't want to include it in the exact project, but…
**Jason Plumb** 21:00 We have to, though. Like, it's per spec, I think. Like, the no-op implementations have to be in the API.
**Carlos Alberto Cortez** 21:06 Yeah, correct.
**Hanson** 21:08 then I think we could either move it, or do something, where, you bring in the coordinate that, that you're expected to use, and brings in this as well. Because I want to say it doesn't have to be explicitly, brought in, but it just lives outside for clarity.
But I think this is easy to resolve, either moving it in, or having it effectively just be a dependent.
**Carlos Alberto Cortez** 21:40 Yeah, the idea is that, like, when users or instrumentation are using that, they can use a single import, and just bring me a full API, let's say, or something like that, or, you know, or API, but that already has this part in. But the idea is that, of course, they can just call the actual API, And, of course, send actual telemetry if there's an SDK installed, if not, nothing happens, you know, but there's an actual implementation there that they can call.
**Hanson** 22:06 Yeah, no, there shouldn't be… there shouldn't be an exception, like, you know, class not found. Like, it should… it should… it should know up properly.
**Jason Plumb** 22:14 That's the idea. Does the API depend on this no-op module? Do you know?
**Hanson** 22:19 I'm looking at the, Gradle file right now…
**Carlos Alberto Cortez** 22:22 At least the other way around.
**Jason Plumb** 22:24 Yeah.
Like, this one will depend on the… Yeah, the API.
Which, that raises the question to me, then, if you just import the API class, a module, dependency, and you call… OpenTelemetry, get logger provider, what do you get?
Like, can I even make one of these? Like, how do I make one of these?
Through a builder.
**Hanson** 22:59 The OpenTelemetry object itself, I think… I wanna say it's an extension function.
Because it depends on the platform, but I will see.
**Jason Plumb** 23:12 I think the spirit of the spec, Hansen, is that… it should be easy for users to include OpenTelemetry and use it. Like, you can sprinkle references of OpenTelemetry all around, and do things with tracers and loggers, and if… you choose to turn off OpenTelemetry, basically have a no-op, like, don't have the SDK wired up, then it should be extremely lightweight. Like, everything is just a no-op, right? That's the spirit.
**Hanson** 23:39 Yeah, so, I remember, because I remember talking about this, and… and that… this was a one import, and it works. So, I need to figure out currently what the mechanics are. Because right now, just the API, it doesn't even include implementation of OpenTelemetry. So, obviously, there has to be implementation of OpenTelemetry in order to return that, and I want to find where it is. I wonder if it's in the… factories…
**Jason Plumb** 24:11 Dude, this is what… this is what Java does.
**Hanson** 24:13 Right.
**Jason Plumb** 24:14 They have a default open telemetry, get no op.
**Hanson** 24:17 Right.
**Jason Plumb** 24:18 And that's, I believe, an API class.
How do I jump to that? Default, this one.
**Hanson** 24:26 Yes.
**Jason Plumb** 24:27 So this default OpenTelemetry that's just all noops exists in the API.
**Hanson** 24:32 Let's take a look at the README. I'm sure this is… I'm sure this is covered in the README.
**Jason Plumb** 24:36 Of the top level.
**Hanson** 24:37 Yeah… Because.
**Jason Plumb** 24:47 So this is what the underlying… OpenTelemetry SDK from Java.
**Hanson** 24:52 That's the… that's only the compat usage, so… Oh, it includes no op, here.
**Jason Plumb** 25:00 So, I'm in… so how big is that package? I'm inclined just to move all this stuff into the API.
Because it's, like, 4 or 5 classes, 4 or 5 no-op implementations.
**Hanson** 25:11 I don't recall why we made that. It might be just me saying, hey, we should separate them.
**Jason Plumb** 25:17 This is this, right? That's… I think this is the thing.
**Hanson** 25:22 So you explicitly provide an implementation. But that's not in the instrumentation, that's in the, that's in the SDK usage, right?
**Jason Plumb** 25:30 Is it?
**Hanson** 25:31 Well, the instrumentation shouldn't have to provide a, shouldn't provide… have to provide an implementation.
**Jason Plumb** 25:37 Agreed. Agreed. So where… do we have one of these, Noah?
Yeah, we do. An impulse, and that is in the no-op package. Yeah, I'm inclined just to move all this into the API, and then it gets, like, real simple.
**Hanson** 25:51 I think the… I think what this is saying is that the app will pass in the no-op implementation down to the instrumentation. The instrumentation only has access to the API, so the instrumentation doesn't actually need the implementation. It just gets it from the interface. So if we want to just include this by default, effectively, move all this stuff back inside the API, That's probably doable.
But yeah, I want Jamie to comment on this, because I honestly don't recall why it's like this. Again, it could be… it could be me insisting, because, you know, it makes sense for the app to declare what its intentions are, and… And the app builds with, the app has to build with an implementation in order to pass it in. So it's actually impossible for the app not to bring in, an implementation.
And instrumentation, doesn't need to, bring in implementation, because it depends on whatever's passed in. So, in the way this is used, the only, the only, the only, thing that has to bring in implementation is the app. And at that point, that's where the decision to say no op or op is Because we don't have the model where we just let the instrumentation, you know, auto-load. Basically, the app has to kind of, you know, from up the top, provide down. So maybe that's the reason why things are separated as they are.
**Jason Plumb** 27:23 Yeah, I mean, take instrumentation out of the picture, because I think it complicates it. Let's just say that there's a library. Somebody's writing a Kotlin library, and they want to do instrumentation with it.
And they depend on the API. Like, they code to the API, right? They're not depending on anything deeper, they're not using even any instrumentation APIs, they're just using the OpenTelemetry API and creating a few metrics, a few spans. Anybody that depends on that library Should be able to just use that library.
And if they're not using OpenTelemetry, then what the… at runtime, what the library is using is just the no-op implementations.
**Hanson** 28:02 Yep.
**Jason Plumb** 28:03 And until the underlying SDK is wired up, or the application creates that SDK and connects it to OpenTelemetry, it would just default to the no-op. And I don't know how we achieve that right now with separate packages.
**Hanson** 28:17 the library will have to bring in. So if the.
**Jason Plumb** 28:21 I know off.
**Hanson** 28:21 No op, yeah. If the app is aware… is unaware of OpenTelemetry, then none of it depends on OpenTelemetry. The library itself will have to say, I'm gonna bring in a no-op, or I'm gonna bring in, you know, a compat, or I'm gonna bring in, you know, the native Kotlin implementation. So, somewhere along the way, someone higher than the instrumentation.
level, in this case it would be the library, has to decide, or if the app is instantiating OpenTelemetry by itself.
Or the app is using a library that says.
hey, library, I can pass you this implementation, use it. Then… then it will pass in either an OAP, or it will pass in, you know, a functional one. It'll be up to the App, and if the app is unaware, it'll be up to the library.
**Jason Plumb** 29:09 Okay.
So, Carlos, this is the spec language. Do you think that, the fact that we have a no-op implementation available satisfies this?
No, I…
**Carlos Alberto Cortez** 29:21 I think it doesn't, because, If you are, like, an application, and you want to install this, then you would have to be calling another artifact.
And especially for instrumentation, that could be more painful, I would say.
**Hanson** 29:39 the instrumentation wouldn't have to call the artifact, and somebody has to decide to put in an implementation, or… somebody has to choose an implementation. And I think, at this point, it's importing, you know, whatever package, and then referring to the code.
If we don't have the op goes inside API, they just kind of use it, and things kind of go out, and nothing happens. But that's almost an anti-pattern, because the application itself is saying, or sorry, the application who's supposed to be picking the implementation.
is saying, oh, just give me whatever, instead of actively choosing the no-op.
**Jason Plumb** 30:20 Yeah, yeah. I like what you're saying a lot, Hanson. So… Are you following that thinking, Carlos?
**Carlos Alberto Cortez** 30:27 Yeah, yeah, yeah. Okay, in that case, let me ask away some people here, and I will think a little bit.
And, that's a good point. The only thing is that, I guess that I am a little bit stuck in my box, mostly because most 6… I think all six have this no-op implementation at the APA level.
**Jason Plumb** 30:49 Yeah.
**Carlos Alberto Cortez** 30:49 I'm thinking now, yeah.
So let me ask the TC, discuss that with them, make a point about this operation.
**Hanson** 30:57 I think with mobile apps and folks who are not used to instrumentation, making decisions explicitly is important, because too often, they just drop something in and it works, and it's like, hey, cool, it works. And it's like, hey, where's my, where's my implementation? Like, where are my logs and traces? And they're like, oh yeah, it defaults to no op. And they're like, what? What's going on? I don't know, I don't know how this works. And then they go and figure it out.
So I…
**Carlos Alberto Cortez** 31:25 Okay, yeah, okay, yeah, let me then discuss that with the TC folks and get their feedback on this one. I think that's an interesting point.
Yeah, I would like to get a second opinion on this one before I give my blessing. Okay, cool.
**Hanson** 31:38 I'll put something in the group to discuss, because also Jamie needs to sign off on this. This is just kind of my opinion.
**Carlos Alberto Cortez** 31:46 Yeah.
Right. Yeah, actually, that's what I want to say. Since he's not here, I think we should discuss stuff, but not make decisions.
**Hanson** 31:53 Oh, yeah.
**Carlos Alberto Cortez** 31:55 Yup.
**Jason Plumb** 31:56 Yeah, that's cool, that works for me.
**Hanson** 31:57 You can put an action item for me to summarize the discussion in the Kotlin group, so other folks could, could, chime in as well.
But I think the most important thing is that instrumentations don't have to worry about this. So, instrumentations just imports the API package, nothing else. They don't have to worry about bringing an implementation. I think that's very key. We can't say, hey, you gotta pick implementation. In fact.
it'll be antithetical for instrumentation, to pick instrumentation, depending on what the app wants to do. The app is ultimately choosing whether it's the Java, or the Kotlin, or the NOP that it's using.
**Jason Plumb** 32:38 I wonder if that… I wonder if that needs clarification and spec, too, like, that… that's… I mean, it could just be an oversight or an assumption that we've all just assumed that, like, the instrumentation would never pick which implementation, because most languages have one or two if you include no op.
**Carlos Alberto Cortez** 32:54 Yeah, I think that the problem with the specification, especially with… with basic stuff, is that It was written in a way that From the perspective of a group that we already agree on something, and we have this shared notion.
And we just wanted to put something that describes, like, summarizes stuff, but it's not.
**Jason Plumb** 33:14 Dude.
**Carlos Alberto Cortez** 33:14 Yeah, so… This is why, especially the GOSI, they were coming back because they were the ones, stabilizing metrics the last. They were coming back, making amendments to the specification to clarify things. Things that everybody knows, but yeah.
They need more details. Okay, yeah, good one.
**Hanson** 33:35 I want to see what the Gosei talked about in terms of context as well, with the default context, because that's.
**Jason Plumb** 33:42 Yeah.
**Hanson** 33:42 That's also a contention that, that, I was bringing up to, to, to, to JV. I'll probably raise it in the next, next, SIG. But, I strongly believe that we don't want to expose a default context, or, for, in the Kotlin API. So…
**Carlos Alberto Cortez** 34:02 Yeah, definitely.
**Jason Plumb** 34:02 Okay, let me…
**Carlos Alberto Cortez** 34:03 Yeah, because in theory, I… now I'm thinking that on the context part, I need to check whether there's something in the spec or not, but I think the idea is that the API provides a context, like a full implementation, I need to double-check that, so that's me.
Before we can discuss it further.
**Hanson** 34:20 Oh, yeah, no, an implementation of the context, we definitely need to provide a default for. I think the thing I was referring to is, current context. So, the fact that there is a current is problematic in a world where threading is abstracted away from many app developers.
**Carlos Alberto Cortez** 34:41 Because of the… because of the coroutines.
**Hanson** 34:43 Because of coroutines, among other things, yeah. And also, You have different libraries working in concert.
not being aware of each other. If they are setting contacts, and they somehow are incompatible, it becomes… the only place to manage contacts is the application, and if you have instrumentation, that depends on what the context is in order to create child spans, it becomes really problematic. Like with HTTP, for instance, calls, running on coroutines, you know, it's… it's… yeah.
**Carlos Alberto Cortez** 35:21 lecture in the…
**Jason Plumb** 35:22 We can't be the first language to have to deal with coroutines, though, right?
**Carlos Alberto Cortez** 35:27 Yeah.NET has, has them, and, but they use something that is fake in the language, at least for the coroutines part.
**Jason Plumb** 35:35 Yeah.
**Hanson** 35:36 Passing it through a coroutine is actually possible, you can pass it through a coroutine's context. The problem is when… it's suspended and something else executes, but it's the same coroutine. I don't know if I'm using the right words, but there's complication abstracted away from Android developers, and, you know.
**Carlos Alberto Cortez** 35:59 developers.
**Hanson** 35:59 So, I think Jamie and I are going to talk about that and, you know, talk about it in the group as well, and then come back, and, discuss it further, because I know this was going to be controversial from the beginning.
**Carlos Alberto Cortez** 36:13 Based on what you're saying, I think that's even more important than the no-up, for now.
**Hanson** 36:18 No, no, yeah, that, that is… that is, yeah.
**Carlos Alberto Cortez** 36:21 Probably we should just get the ball rolling, gathering ideas and doing brainstorming, because it sounds like it will be a longer discussion, for sure.
**Hanson** 36:29 Yeah, the, API, so, with… if you use a Java implementation, you… we do bring in that current context, and sending that current context will work, but, it's the API level, whether we want to have that, if you're not using the Java implementation, whether we still have that, because it could lead to a mess.
**Carlos Alberto Cortez** 36:54 Yep.
Yep.
**Jason Plumb** 36:58 Alright, we have, we have 9 minutes left. I want to make sure that we cover a few more things, so… let's look at this…
**Carlos Alberto Cortez** 37:05 The next, yeah, the next two are relatively minor, by the way. The first one is, like, attitudes Motator, like, the way it's defined.
If you're fine with that, I'm fine with that as well.
That's the way how you are specifying attributes.
You're getting this interface object, and you put stuff on it.
Yeah. And when you're passing that, you're getting a function that, yeah, provides you this.
**Jason Plumb** 37:36 Yeah, so I don't know that this is at all contentious. I mean, one thing that struck me when I was looking at this, I don't know, a week or two ago was, oh, that's cool, all keys are strings, right? We don't have this, like, problem that Java has, where, like.
They went through an extra layer to try and force the typing on the keys, to match the values, and that means you're having to create these key objects that are strongly typed all over the place, and it makes me insane.
So I think that this is kind of nice. I think I do like it.
I think there's some stuff that's missing here.
Specifically, any.
Right, so…
**Hanson** 38:18 I remember Jamie… oh, maybe that was just a log API, the body that has… supports any.
**Jason Plumb** 38:26 Well, everything now supports any…
**Hanson** 38:28 Right, right, right.
**Carlos Alberto Cortez** 38:29 But it's very new, it's very new. Yeah. We could… we could probably forget about that for now, But, before we go stable, yeah.
Or if we go stable, like, in 3 months, then we can add that.
**Hanson** 38:43 Well, it…
**Carlos Alberto Cortez** 38:43 If we weren't, yeah.
**Hanson** 38:45 If we have any, do we need all of these?
Or do we just, like, figure out what it is and call the appropriate one in the implementation?
**Carlos Alberto Cortez** 38:57 didn't do that.
**Jason Plumb** 38:59 I mean, it sure is nice to just say set attribute.
**Hanson** 39:03 Yeah, this, yeah.
**Jason Plumb** 39:06 And in fact, with all of these right now, with all of these being typed, except for the… Type erasure on this crap.
Right? Because of these lists.
All of these… Like, these, I think, would reduce down to said attribute.
**Hanson** 39:23 The other one could be reduced to, to, to, set list attribute, or whatever.
**Jason Plumb** 39:28 Exactly.
**Hanson** 39:28 So it's good to talk about that. I would rather not have 8 methods if you don't have to.
**Carlos Alberto Cortez** 39:38 Yeah, I don't… I mean, yeah, yeah, I don't know, I have experience about that, but we can play with that, see whether users would complain about that, I hope not, but what if there's an unexpected torrent at the SDK detection? But yeah, that's something we can prototype and discuss, yeah.
**Hanson** 39:57 Yeah, the type of Razor, we have to worry about… we have to worry about, compatibility for, the other platforms. For JVM, it's fine. For Android, it's fine, but the other ones, I don't know, especially JavaScript. So… It may be good to keep this, but it's worth thinking about, when we go through this.
**Carlos Alberto Cortez** 40:19 Yeah, also, yeah, yeah, yeah, I'm just thinking because, you know, Weber, in theory, Weber may provide, like, some API out of semantic conventions definitions, and they will be providing the type along.
Yeah, I don't know, that could be interesting how that would interact, but anyway, that feels like things down the… way down the road.
**Hanson** 40:45 that Kotlin… Kotlin should support this nicely. It's whether or not Yeah, the platforms.
**Jason Plumb** 40:55 So we have, variance here in this. Is this different than what the spec has?
**Carlos Alberto Cortez** 41:01 Actually, it's not important. I was just wondering whether the first value… like, I am… maybe it's not important, I was just mostly curious, like, between Java and Kotlin. I don't know if we will have people that have used the Java one.
**Jason Plumb** 41:15 What does the spec say?
**Carlos Alberto Cortez** 41:18 Oh, it's very open, if I remember later.
**Jason Plumb** 41:20 Really?
**Hanson** 41:22 I honestly… both are fine. Unknown and undefined is… unknown is an explicit undefined, I suppose. So, whatever, I'm totally okay with. I don't care.
**Carlos Alberto Cortez** 41:38 Celebrity number.
**Hanson** 41:39 It's optional, so…
**Jason Plumb** 41:41 Where is the severity?
**Carlos Alberto Cortez** 41:45 No, they were.
**Jason Plumb** 41:45 number… Oh yeah, and there's no zero at all.
**Carlos Alberto Cortez** 41:55 Yeah, that's why it's, like, on the fine, you know? And probably we should have it there.
**Jason Plumb** 41:59 Over here.
**Carlos Alberto Cortez** 42:00 Either one.
**Jason Plumb** 42:01 Unspecified. They use yet another… we should call it unspecified. So now we have unknown, unspecified, and undefined.
**Carlos Alberto Cortez** 42:11 Yeah.
**Hanson** 42:12 Java calls it undefined.
**Jason Plumb** 42:14 Yeah.
**Hanson** 42:16 Not null , but undefined. Zero.
**Jason Plumb** 42:19 Yeah…
**Hanson** 42:22 Yeah, that's…
**Carlos Alberto Cortez** 42:23 Not important, just if you're wondering, yeah. They're also the same.
**Hanson** 42:29 Unspecified and undefined is closer than… well, than unknown.
I suppose. But, yeah.
**Carlos Alberto Cortez** 42:36 I think so.
**Hanson** 42:37 We can pick one.
It's an easy change. No one should care about.
**Jason Plumb** 42:43 Yes.
**Hanson** 42:44 It goes in zero in the OTLP anyway, so…
**Jason Plumb** 42:48 I mean, that's my… that's my thinking, too, is, like, it's gonna be interoperable with Java by the identifying number, right?
Yeah, okay, what's next? Does this have to go away before release? I think… It depends on where you're asking about this, right? I mean, I think we'd like it to.
Yeah.
**Hanson** 43:09 It should go away on all the interfaces that we're calling stable, but the actual annotation will remain.
for us to basically call out things within Sable implementations, or Sable APIs that, have new things being introduced, to them.
**Jason Plumb** 43:28 We're doing this in Android as well, and this is a nice way for us to basically do what Java's doing with incubating, without having to have all this repackaging nonsense that they have to jump through.
Which I think you've probably seen that, right? Like, this is.
**Carlos Alberto Cortez** 43:44 Yeah, of course.
**Jason Plumb** 43:45 You can just annotate it.
And call it out as, like, not yet stable.
**Carlos Alberto Cortez** 43:50 Yeah, if that has been… if that has been, clear enough for the Android folks, which is both of you and Jamie now, I'm fine.
**Jason Plumb** 44:01 Yeah, because there's something you have to… as a user, you have to jump through hoops acknowledging… there's an extra step that a user has to do to acknowledge or allow the use of an experimental API.
**Hanson** 44:11 Yep.
**Jason Plumb** 44:12 I wonder what that looks like, though.
**Hanson** 44:13 Oh, they basically have to either suppress the warning, or, opt-in.
**Jason Plumb** 44:19 very often.
**Hanson** 44:19 on the method call, or the class, or the module, you know, whatever. They have their ways to basically snooze this, but it has to be explicit, at least in the code level. People, you know, they'll just do whatever to get things building, but.
**Carlos Alberto Cortez** 44:33 But out of curiosity, when you do this, like, when somebody's testing an application using this API, and they hit a thread, say, thing, they don't get any warning, right? Because the notation is defined at the OpenTelemetry API level.
So there's no lint rule or anything that could… Get them a trigger.
**Jason Plumb** 44:55 The thread-safe annotation, you mean?
**Carlos Alberto Cortez** 44:57 Yep,
**Jason Plumb** 44:58 Yeah, I don't know.
**Carlos Alberto Cortez** 44:59 No, no, the Experimental API.
**Hanson** 45:03 Yeah, Experimental API has the opt-in, but the thread safe, I feel like it's something that is documentation,
**Carlos Alberto Cortez** 45:12 No, no, ThreadSafe is fine. Yeah, it was, yeah, yeah, yeah, Experimental API. But anyway, yeah, I think we're disclosed enough, and we have one minute.
**Jason Plumb** 45:21 Oh yeah, okay.
**Hanson** 45:23 Can't believe we used the entire time.
**Jason Plumb** 45:25 It's only 45 minutes. Goes quick.
**Carlos Alberto Cortez** 45:29 Nope.
**Jason Plumb** 45:31 Alright, we… and so I just added these down here, so, like, I think we do have to… we agree that we, like, basically are talking about stabilizing the entire API, and what.
**Hanson** 45:39 Yeah. I… I… I… I mean, let's talk to Jamie, but I really don't want to move things out. That's…
**Jason Plumb** 45:47 Yep, yep.
Okay, we did it.
**Carlos Alberto Cortez** 45:51 Thank you so much.
**Jason Plumb** 45:52 Thank you, good to see you.
**Hanson** 45:53 Carlos, thanks for all the review. We need this. Thank you.
**Jason Plumb** 45:56 Super helpful.
**Carlos Alberto Cortez** 45:57 Yeah, thank you so much.
**Jason Plumb** 45:58 Right, right.
**Carlos Alberto Cortez** 45:59 My pleasure. Giselle.
**Hanson** 46:01 Bye.
