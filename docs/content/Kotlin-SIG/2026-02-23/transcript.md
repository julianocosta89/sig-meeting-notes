SIG: Kotlin SIG
Date: 2026-02-23
Duration: 41 minutes
Zoom Recording URL: https://zoom.us/rec/share/2X0e6f1bCGFKHTWY9sWR7kRa_pnwzxOaTd8Yo9iQ13qb38jg7s0dmpLHcPWQYwl1.tGBRpHREWOjVhlpy
============================================================

## Zoom Recording Transcript

**Jamie Lynch** 00:19 Mornings.
**Jason Plumb** 00:22 Hello.
**Jamie Lynch** 00:50 Have you got the Google Docs link okay?
**Jason Plumb** 00:53 Yeah.
**Jamie Lynch** 00:54 Brother.
**Jason Plumb** 01:02 So while people are still joining, I just want to… Talk about this PR… which would be cool to get merged with the new meeting information, like the GDoc and the Zoom stuff.
**Jamie Lynch** 01:19 Okay.
**Jason Plumb** 01:20 The format of this… YAML file, so I did one of these… Hey, Francisco.
**Francisco Prieto** 01:29 Hey, Ron.
**Jason Plumb** 01:30 So, I think all of the SIGs are in here, right? But, like, if you just pick one, right? If you just, like… here's one.
there's, like, textual information about the meeting. There's a… there's a link to the GDoc, but it's, like, just by ID, and presumably…
**Jamie Lynch** 01:47 My god.
**Jason Plumb** 01:48 the automation, like, populates a URL with that or something, but then, okay, cool, Slack channel ID… I don't know that we have… We do have that Slack channel and the ID in this PR, but I don't… does it have the GDoc? I think it does not have the GDoc.
Oh, it does, but the value's missing. So, okay, so that's maybe an easy thing to fix.
It's probably just, like… I don't know. How do you get the idea of your dock?
**Jamie Lynch** 02:20 I guess there's some URL, maybe?
**Jason Plumb** 02:24 Right, do you think it's… this string looks too long?
**Jamie Lynch** 02:28 Well, there's an underscore.
Mr. Ink, maybe it's like…
**Jason Plumb** 02:32 Yeah, does it… what do these other ones look like? Oh, yeah, okay, so… Let's go to the… Sorry to be wasting the time doing this, but it'd be nice to get this set up.
I'll timebox it to 3 more minutes, I promise.
So if we go to, like, I don't know, I think it was this first one… go to that Google Doc… Hmm… I guess… I want to find, like, the stuff probably before the underscore?
Aha! Oh, that's a long one.
Okay, so they have the whole thing there. Okay, so maybe that's just what we need to do.
Alright, I will do that right now, and then I'll stop sharing so we can actually do important stuff.
**Jamie Lynch** 03:45 Cool. I will post the Google Doc.
In the chat, so if anyone does want to add items to the agenda, Feel free to do so.
wise, I guess we'll give it maybe a minute or two, and then we can make a stop. I think some folks are arriving late.
**Jason Plumb** 04:07 I think Alolita said she was gonna be there at the start, and Carlos is gonna be late, and Hanson's gonna be late.
Here we are.
**Jamie Lynch** 04:19 Let me try sharing a screen.
**Jason Plumb** 04:22 So, after the release, congratulations, by the way, on getting that out. I know it's a slog, like, getting all of.
**Jamie Lynch** 04:28 Understood.
**Jason Plumb** 04:29 Kind of lined up is pretty tedious, so congratulations.
After that release happened, I went out to… Sonotype, just to… just to browse the directory and make sure, and I was like.
Wow, there's a lot of modules! Holy smokes, like…
**Jamie Lynch** 04:45 There's, like, a hundred modules or so. It was, like, so many.
I guess it's… The fact that it's a module-based SDK combined with that, it's targeting a load of different platforms.
**Jason Plumb** 04:57 Oh, yeah. Yeah.
Yeah, that's not necessarily a critique or anything, I was just… I was surprised.
**Jamie Lynch** 05:03 Yeah.
**Jason Plumb** 05:05 Hi, Alolita.
**Jamie Lynch** 05:07 Who?
**Alolita Sharma** 05:08 Hey, hey, hey Jimmy, how are you? Hi, guys, how are you?
Sorry about the long process of getting everything set up, but we are almost there.
**Jamie Lynch** 05:21 Yeah. Yeah, I think… I know how it is.
Cool, there's a link to the Google Doc in the chat, so if anyone has items they want to discuss, just add them in there. Alolita, if you wanted to go first, I think you mentioned you had something interesting.
**Alolita Sharma** 05:43 Yes, yes, just a couple of things. Again, I think, at least in the initial meeting that we had.
Somewhere in my notes, I had noted bi-weekly, so sorry about, you know, if we are thinking of weekly and we can maintain that cadence, then I can definitely change the invite.
And, make it weekly. So, that's something, again, you guys can decide what cadence works for you.
I think, I think it was based on, Hansen and others, you know, who had joined in, in that meeting, just… so it just happened to be in my notes. So if weekly is the cadence you guys want to go, then I can just change it.
**Jamie Lynch** 06:29 Got it.
**Alolita Sharma** 06:30 And then, I'll update the SIG directory in the community repo. I think there's already an open PR I had filed, but I wanted to add the Zoom link.
Because, the Zoom link required a lot more permissions, and admin access, and, you know, we finally have that. So, we should be good.
Those are the two things I wanted to call out. Is there anything else that you guys, Needed to get, you know, into… A groove here, and typically, projects or SIGs maintain a project board as you get organized, and I know we had talked a little bit about it in the initial, you know, sync, but I think maybe once we have a nice backlog, then we can easily create a project board.
**Jamie Lynch** 07:25 Is that done via GitHub or something else?
**Alolita Sharma** 07:28 It's on GitHub, yeah. It's on GitHub, and it's on the, it's attached to the hotel Kotlin repo.
**Jamie Lynch** 07:38 Okay. Yeah, we have a couple of milestones already, so we could maybe look into turning that into a project board initially, I guess, and then add to that.
**Alolita Sharma** 07:51 Yeah, sounds good, sounds good. I mean, I think we can even see the examples.
I don't know if you guys can actually see the project ports, they are on the hotel.
GitHub.org.
Let's see…
**Jason Plumb** 08:08 We are not using a project board on the Android.
**Alolita Sharma** 08:12 Okay, nois.
Whatever works, I mean, in terms of tracking the milestones, because typically the larger SIGs do use that, just because there's so much going on.
**Jason Plumb** 08:27 Yeah.
**Alolita Sharma** 08:28 But, you know, as we're getting started, I think there's… We don't need to, but we can easily get organized once you're there.
**Jamie Lynch** 08:37 Got a…
**Alolita Sharma** 08:37 We can just do labels, or, you know, whatever works.
Labels are easy.
**Jason Plumb** 08:43 I want to call out, too, in case anybody on this call didn't… it would be easy to overlook this fact, but, we promoted Jamie to maintain her on Android as well.
So… Awesome. Yeah.
**Jamie Lynch** 08:56 Cool. Yeah, I guess, one other thing to mention is, I think Embrace is gonna be, like, putting together a blog post on our side, kind of announcing that OpenTelemetry Kotlin is a thing.
I think we… we were also reaching out to a few people in… within hotel to… like, kind of coordinate with that a little bit. So you may have, like, a couple of folks from the base reaching out to you, if that's okay.
**Alolita Sharma** 09:25 Yeah, yeah, yeah, and just, to be aware, again, the project does have marketing guidelines for all the vendors who actually participate, so please point them to that, because, it's good to be aware of.
**Jamie Lynch** 09:43 Yeah.
Yeah, I've pointed them in that direction. I think they're quite keen not to make any, like, faux pas.
**Alolita Sharma** 09:50 Awesome, awesome.
All good.
But again, highly encourage also you guys, you should make an introductory blog post even on the project blog, because I think it's nice for, you know, the SIG to announce and invite more folks to join.
**Jason Plumb** 10:10 It would be a good follow-up to the Call for Contributors blog that went out in September, so this would be a natural follow-up, I think.
**Alolita Sharma** 10:17 Yeah.
**Jamie Lynch** 10:18 Yeah.
Yeah, I actually have a draft, which… It's not a PR right yet. Right now, but it should be a PR within… Hopefully a week. Yeah.
**Jason Plumb** 10:29 Yeah, nice.
**Alolita Sharma** 10:31 Very cool.
And we have Carlos here, too.
**Carlos Alberto Cortez** 10:36 Yeah, yeah.
Sorry to be late, but yeah, better late than never.
**Alolita Sharma** 10:41 No worries, Carlos.
**Jamie Lynch** 10:46 Cool. I guess we could discuss meeting cadence, how did Vegas?
Feel… would be, like, a good frequency to do this.
**Jason Plumb** 11:02 I'm a little bit of two minds. I think that because the project's young, having… Weekly cadence is… is a little better for coming up, like, ramping up, getting up to speed, but also… It's a, it's a, it's a lot of time.
So, I'm… I'm torn.
**Carlos Alberto Cortez** 11:22 100 TVs that we could do 30 minutes each week.
Or if you prefer… I don't know what Jason, what would be your preference in that regard? Like, one hour every two weeks, or half an hour?
**Jason Plumb** 11:34 We talked about 45 minutes previously.
**Alolita Sharma** 11:36 Yeah, that's what I set up the invite to be.
**Jason Plumb** 11:40 Okay, cool.
**Alolita Sharma** 11:41 If you guys run over, that's fine, because the… I think the link stays active for the whole hour.
But, Again, you guys decide what works for you.
**Jason Plumb** 11:58 I mean, I'm inclined to… I'm… go ahead, go ahead.
**Jamie Lynch** 12:06 Okay, I'm pretty happy to go with the majority view, to be honest. So… Yeah, okay.
**Jason Plumb** 12:17 I'm inclined to say status quo until we have a compelling reason to change it, which is, let's keep it weekly at 45 minutes until we want to change it.
**Carlos Alberto Cortez** 12:27 Yeah, I could support that. And I wanted to say that, for example, in the TC, it's very common that people are busy, so they… sometimes they come and they… if they have a topic to discuss, they come for the first 15 minutes, for example, you know? And it's totally normal, you know, they can follow up with the notes.
Yeah, so let's keep… yeah, I suggest we do a JSON set, that's cool, and we can revisit that in a moment or two.
**Alolita Sharma** 12:51 Yeah, absolutely.
Sounds good. Jamie, I'll update the, Jason, I'll update the meeting invite.
**Jamie Lynch** 12:59 Thanks for that.
Okay, cool. So I guess we've got two other topics right now to discuss, kind of, like.
Mmm… yeah, kind of, like, technical parts of the SDK. If anyone else does have other things they want to discuss, feel free to add them in.
So the first thing I wanted to discuss was just what our min Compile SDK should be.
So I'll see if I can open this.
Up.
Can folks still see the screen okay?
**Jason Plumb** 13:38 Yep.
**Jamie Lynch** 13:40 So basically, we… updated to use Android Gradle Plugin 9, because that's the latest major version.
And one behavior change is the minimum compile SDK that you can set.
defaults to whatever the compile SDK is.
So… The compile SDK is basically the version of Android you're compiling against, and the minimum version is just the minimum, but we allow Library consumers to use.
So, commonly we've… Set it at 36, which is a little high, but not… super unreasonable, I guess. So, I guess my question is… Do folks feel like it's reasonable to set that a bit lower?
The consequence of not setting it lower is people who are on older Compile SDKs won't be able to use the library.
**Jason Plumb** 14:51 Do we know what the usage distribution looks like for those different versions? Like, for real-world users?
**Jamie Lynch** 15:01 I'm not aware of… any statistics on it? I do know that 36 is the absolute latest, unless you're compiling against the latest beta version of Android.
So… I'd say it's fairly likely there's folks using 35, possibly 34, but Google Play does kind of ratchet the version up, so it would be… Yeah, I don't think anyone's on anything lower than 34.
**Francisco Prieto** 15:35 I am expecting that this will become more of a theme as libraries start bumping to 3DC to HTTP9. This will start to be imposed.
And… Usually, it's not that big of a change. You usually just set it up to 36 and forget, because there aren't that many ranking changes, so I would say that we could start with 34 and then see what, I don't know, Compose or other big libraries do.
But I am expecting for them to, like, be pretty aggressive in that.
**Jamie Lynch** 16:09 Because it's not that hard.
**Francisco Prieto** 16:12 Bump.
**Jason Plumb** 16:16 Did we get to 34 on Android?
In the Android project?
**Jamie Lynch** 16:21 That's a good question.
I'm not sure what Android uses.
**Hanson** 16:27 We can take a look, but effectively, it's… I… sorry, showed up late. But it's really hard… Oh, no, that's pretty good one.
It's really hard to use anything lower, than, if you want to support the latest Android version, it's really hard to use anything that is not, like, the one that targets it. You have to have workarounds. Android Studio doesn't really support… the latest versions don't really support these low, these low compile SDKs. But folks who kind of have a building already, they're using, like, frameworks like React Native or Unity, they don't care, don't use Android Studio, then those are the ones that are really, you know, impacted.
But… It… it… Yeah, So even if it… so even… what I want to say is, even if it's not minimally set, I think, effectively, the people who are actually using 33 and below is… Very likely. Very, very small number, probably.
**Francisco Prieto** 17:27 I'm actually in the process of fixing the PR that bombs Android to HTTP9. I left that for a lot of time, and I'm now back to it. I should actually fix it today, and I set target SDK to 34.2, mostly because it's the minimum version that Google Play supports, so it should be, like, similar, and it should be the same discussion, too.
**Jason Plumb** 17:54 Yeah, thanks for taking that on, by the way.
**Francisco Prieto** 17:57 It took way longer than that.
**Jason Plumb** 17:59 It's fine.
It's fine.
**Jamie Lynch** 18:06 Okay, well, I guess if there's not objections, I will assume that 34 is a reasonable default to service at, and I will merge this down a bit later.
**Francisco Prieto** 18:22 There is something that I saw in that same blog, the AAR metadata. There's… I'm not sure if it is new, but there is a flag for a minimum HCP version, like, to enforce it. It would be nice to investigate that and see if that That's useful, because… I think we currently just say what's our minimum HTTP version, but we don't really enforce it in any way.
**Jamie Lynch** 18:52 That would be quite cool to investigate.
**Francisco Prieto** 18:57 I'll check where the link is and paste it on the Google Doc, so at least we know.
Worries.
**Jamie Lynch** 19:07 Yeah, I think that'd definitely be useful.
for… us internally at Embrace, as we've got a Gradle plugin, and I guess it would be… Useful… Generally.
If you're trying to use, like, a really old version of Gradle with OpenSelemetry Kotlin, Or over telemetry Android.
Okay, cool. If there's no other thoughts on that one, we can move on to the next part of the discussion. So… Yeah, I guess this is kind of, Opening up, like, a talk about Combined with the OpenSelementary specification.
So, I figured a good way of doing that would be to discuss When we want to allow writing, When we want to allow writing, telemetry, and when it should be possible to, in introspect, what is in telemetry.
I think right now, the Span API, for example.
It makes it possible to read what is in a span when it's being created, and I think that technically goes against the hotel spec.
So… Basically, I created… this PR with… Attributes that kind of split it into two interfaces, so one which writes, one which reads.
And… Yeah, I guess. At a very high level.
I'd just be interested in people's thoughts on what approach we should take with this.
**Jason Plumb** 20:59 I gave a review and an approval pretty late on Friday, but overall, I think it's a good change. I like that it's matching Java in a number of ways, and I like that there's a… it seems like there's a better symmetry with the readable and mutable, or I forget the term you use, but it seems like it's more symmetric.
**Carlos Alberto Cortez** 21:19 Yeah, I guess that in that front, after reading myself, Jason's review, I also think that probably the names need a little bit of tuning, but I really like that, yeah, we are more aligned. Actually, there are so many things that are…
**Jamie Lynch** 21:34 Kind of open in the specification.
**Carlos Alberto Cortez** 21:37 But I think that if possible, we should try to do something similar to Java, so, you know, there's no, So you're not spending too many cycles if you're coming from the Java API, you know, should be great.
Yeah, too much.
I guess that my, my only… for my, my, my, well, I don't know, but regarding specifically, and we don't have to talk about that now, but, or I need to think more, but… The first one is that when you are defining the readable attributes, I would prefer myself, they are called only attributes.
unaccreetable attributes, I don't know. Like, honestly, I know, as Jason himself said, there are… in Kotlin, builders are not a thing, but I don't know if we can make an exception or something. Or readable is something that actually exists extensively as a suffix. In Kotlin, we can probably keep it. But for… yeah, I would rather remove the readable from the attributes part.
**Hanson** 22:39 So… Sure.
**Jason Plumb** 22:40 Just call it… just call it attributes.
**Carlos Alberto Cortez** 22:42 Yeah, correct.
**Hanson** 22:45 I think, I think the issue here is that, readable is not implicit.
if you take away… take that away from attributes, because the hotel specification says that, spans and telemetry in progress should not be, introspected. Therefore, a span is technically not readable, and attributes on that span is not readable. So, you have this attributes thing, and you have this you know, spam. It's not readable.
by having the readable, prefix, you're basically saying you can introspect. So, I think… I also don't like extraneous words, which is why I like the mutable and kind of nothing before, but I do agree that aligning with Java is something good to do. I think I gave this a review initially and thought it was merely a rename, and I would be okay with that.
But embedded here also is the fact that it takes away the readable aspect, from the default span, so a span, like Java, is no longer readable.
And that, I think, is the part that is probably gonna be, that probably needs a little bit more drilling, to… for us to figure out whether that is, like, a must-must-must-not, or a, we would recommend not, given the use cases in Java. And, you know, if there's any, ability to kind of open that up a little bit for other use cases.
**Jamie Lynch** 24:14 Yeah, I think that's definitely the bit that I'm interested in discussing. Like, I'm pretty open to, like, renaming interpaces and whatnot, but I think… Crucially, it would be good to decide whether it makes sense To be able to, like, read attributes in a span before it's ended.
Because I could see if there's, like, a long-running span and you want to check if there's an… A specific attribute. In Batspan.
**Jason Plumb** 24:45 I think it's so much worse than that, though. I think it's actually because people build a bunch of spam processors that fight each other. So they… they end up reading and, like, reassigning attributes, or changing the span on the fly. I think that's the main problem.
**Carlos Alberto Cortez** 24:58 Yeah, correct.
**Hanson** 25:01 I think the processor is read-write span, if I'm correct, right?
**Carlos Alberto Cortez** 25:05 Span processor, you get a read-write span, which is in the SDK as an interface, for only span. Well, sorry, only start, and for end, you get only the readable part.
**Jason Plumb** 25:18 That's right, so you can't change the span on tail sampling, or, you know, on tail operations. Like, it's assuming that when the span is ended, it's ended, and you can't continue doing stuff with it.
**Carlos Alberto Cortez** 25:28 Yep.
**Hanson** 25:30 So, correct me if I'm wrong, but right now, basically, you know, when you have a span in a processor, when it's kind of active, you could, both read and write to it.
So on the on start, and the on-end, onEnding, I believe, or not on end, but onEnding.
for the exporter, it's merely readable at the export part. You know, nothing, nothing crazy. But the span interface itself, you can't read start time, you can't read attributes, things like that.
prior to this, change, I think, correct me if I'm wrong, Jamie, but, the span processor and span exporter, the, the availability of reading and writing is the same as Java.
So the only difference is that span, is… readable. So you can look at… so when you… when you create a span, and you have, like, a reference to it, you can look at when it started, which is something that you can't do, in Java. You can look at the attributes within it, like, has this been… has an attribute been added, to it?
So this… prior to this, this is allowed, but after this, it's not allowed.
**Jason Plumb** 26:55 Yeah, I posted a link to the Java interface if you want to open that, Jamie.
**Jamie Lynch** 26:59 Yep.
**Jason Plumb** 27:02 Just so we're on the same page.
Oh, sorry, I put it in the Zoom chat.
**Jamie Lynch** 27:05 I didn't see my job, okay.
**Jason Plumb** 27:07 Good dummy.
So, yeah, so on start, what you get is the context, and then a read-write span. So, in your span processor.
When the span is starting, you can monkey with it. Like, you can change its name, and you can poke at the attributes, but on end, like on line 79, the only thing you get there is a readable span.
**Hanson** 27:28 Yep. Because it's immutable, basically, by the time it's done.
**Jason Plumb** 27:31 It already ended.
**Jamie Lynch** 27:35 Yeah, that makes sense. Yep. …that it would end.
I guess… I might be getting this wrong, but I think from memory, like, the… in between on start and onEnd, I think it's not possible to introspect, but I don't think it's possible to, like, read attributes.
**Hanson** 27:53 If you look at the.
**Jamie Lynch** 27:54 Silver.
**Hanson** 27:55 Yeah, if you look at the span interface, in the API?
**Jason Plumb** 28:02 Yo.
**Hanson** 28:04 there is, you… you can't get… You can only set.
And I guess what it returns, you know.
you maybe drive, you know, hey, it's returning, so it's correct. But, like, you can't read the start time, for instance, and I think…
**Jason Plumb** 28:27 I think it's also… I think that's it by design. I think it's to reduce the number of places where the spin can be… you know.
kind of… it's not change… I mean, sure, the span can be changed in a bunch of places, but it can't be based on prior state of the span.
You know what I mean? Like, you can't read a thing and say, if… if the, you know, time is whatever, then I'm gonna change this attribute, like, of it.
Does that make sense? Like, you can make changes to it, but they can't be based on the current state of the span.
**Hanson** 28:57 Right, which is… and that is the part, I think, that is… that we're kind of, like, you know, you know, trying to figure out what to do, which is we do want to know that. So, I think, outside of the processor, just having a reference, so this is instrumentation and not, like, SDK or whatever, we want to be able to figure out if this is… the span's been running for 10 minutes, or if this span has some attributes added to it that identifies it as something.
Because there are instrumentation use cases, I think, you know, and user-facing apps, where that is extremely helpful. And telemetry is… I definitely understand the philosophy of the Java SDK and just OTEL spec in general, that telemetry is a byproduct, and you should not have instrumentation, or even code, especially code, that you know, depends on it. There is a coupling that you could have between instrumentation and application logic, which potentially is problematic. So, if that's not seen as necessary, disallowing it is absolutely the right thing to do.
But there is added utility, I think, for the end-user-facing app use case, such that relaxing that. I think I mentioned in the review, if the default one is, is, is too… too easy. Maybe we increase the friction, you know, to make it a little bit harder to get, like, another interface, like, you know, get readable version, or… I don't know what it is. Just to kind of add a little bit of, you know, padding.
not total safety, but a little bit of padding to the edges. But, like, completely disallowing it forces people to do, like, what Embrace does, which is wrap it, which sucks.
Because of the back-and-forth state, of having to, like, well, I'm gonna set something, but I gotta set something there, but I gotta keep a copy, and then when you end it, I'm gonna just do it there, and it's all… unnecessary, or I'd be… it'd be nice if that were not necessary. And by being able to read it, we could just have one, state, without any wrapping.
**Jason Plumb** 31:20 I'm reading… I'm going back over the spec to see if it's very opinionated about this topic.
**Hanson** 31:30 Based on prior research, it feels like it's opinionated, but I don't know the.
**Jason Plumb** 31:35 Yeah, I thought so too, I'm still skimming.
**Hanson** 31:41 And I definitely understand why you would not want that by default, especially when telemetry is just supposed to be logging go or recording go, when instrumentation is decoupled from app.
**Jamie Lynch** 31:55 Yeah, and we might be able to… Present this as a, like, opt-in Option.
Like, I think that's… something we could potentially do. Like, we have this API extensions module.
It feels like it could be a good fit for this, if it's technically against the spec, but could be useful for some use cases.
**Hanson** 32:18 extension function or something like that, you have to explicitly import it.
**Jamie Lynch** 32:21 module.
**Hanson** 32:22 So that, you know, it's not on the interface, but you can effectively call it from there, as if it were thanks to extension functions.
**Jamie Lynch** 32:31 And magic.
**Hanson** 32:32 A monkey ate.
**Carlos Alberto Cortez** 32:34 But, Jamie, do you have a, like, a use case that would benefit from this, or is that just potentially having something that could be useful?
**Hanson** 32:43 So, Embrace does this already, to do, various things.
I'm gonna have to take a look. Oh, I mean, Jamie, off your… off the top of your head, you might.
**Jamie Lynch** 33:00 I will also have to take a look, but I do remember that we use this, for some introspection.
**Jason Plumb** 33:08 So, one thing I've seen this, wanting to be used for is for re-entrant code, so that you're not restarted, like, creating a bunch of spans when you've already got one started, if you have code that's re-entrant.
Like, there's some instrumentation in Java that has to keep that… keep track of that for this purpose.
**Hanson** 33:25 Hmm…
**Jason Plumb** 33:27 I don't know, I can't think of many other use cases for it, but…
**Carlos Alberto Cortez** 33:32 Yeah, I would really love to, before we do something.
like, this API X package, go and check the use cases, probably modify or add something in the spec.
Instead, first, you know?
**Hanson** 33:48 Yeah, I can… I can take it on and, Add some use cases.
**Carlos Alberto Cortez** 33:55 Yeah, thank you so much. Oh, by the way, Hanson, sorry, I didn't know you worked in Embrace as well. That's why I was asking Jamie, I thought, for some reason, I was under the impression you were working at Splunk, so my bad, sorry for that.
**Hanson** 34:07 No worries.
**Jamie Lynch** 34:15 Cool. Yeah, so we can go away and… come up with some concrete examples of how it's used within Invace, and hopefully that will help the discussion.
**Hanson** 34:28 Is the renaming contingent on this, you think? or… or… Or can we probably… Get it so that we basically merge most of this, but keep the existing relationships.
**Jamie Lynch** 34:43 Yeah, that's a good point. I think we could do the renames and keep the existing relationships, and then split the rest off into another PR.
**Hanson** 34:54 Yeah, it's the… it's the do we… are we idi… you know, do we align with Kotlin naming scheme, or do we align with hotel naming scheme? That's… it's always the, the choice. I don't have a strong opinion about that, so…
**Jamie Lynch** 35:11 Cool. Anything else on that, or any other topic?
**Hanson** 35:24 Oh, I have a topic. I'm gonna… I'm gonna redo all my stupid, reviews, basically get rid of all but the top one, and just try to do it in a more reasonable manner. It's… yeah, it's… every time I have to rebase, I have to, like, do a whole dance, and it's fucking annoying, so I'm sure it's annoying for everybody else, too. So, I'm gonna basically… since there's, like, no… there's material comments in, I think, one or two of them, but, you know, I'll clean it all up, and create new ones, so… We don't have to do this fucking dance every time.
**Jason Plumb** 36:00 Do we know if randoms can push branches? They shouldn't be able to, right?
I think you… I think you're able to, because you're an improver.
**Hanson** 36:09 Probably.
**Jason Plumb** 36:11 I don't think Randos can. I hope not. I should try that, I can try that from my personal account.
Let me just try it right now, because it's fun. You don't have to wait for me, though.
**Hanson** 36:24 But yeah, that's it for me. Nothing else. Apologies again, because I… yeah.
And hi, fan.
**Jamie Lynch** 36:35 Cool.
**Francisco Prieto** 36:37 in one of those PRs, let me know if you… So that… Like, I can look at it again, but I don't promise that I will be able to review them.
**Hanson** 36:48 stories.
**Jamie Lynch** 36:52 Okay, Bo… If there's no other topics, we can all get a bit of time back.
**Hanson** 36:58 Awesome.
**Carlos Alberto Cortez** 37:00 Oh, by the way, sorry, the last thing is, in case you are… oh, actually, that's a problem. Anyway, but the thing is that I got a reminder from somebody that, since you're a maintainer, you know, sorry, since you're a new SIG, you should be coming to the specification call every Tuesday. The problem is that you have the Android call at the same time.
So, probably could be useful, if you could actually read the notes from the spec meeting.
just to, you know, stay in the loop, you know, what's happening there. And of course, for example, if there's something that has to be changed in the spec, I can bring the topic myself from your side, but… Like the clock, the clock, instance that Hanson, you mentioned, but, yeah, generally it would be great, you know, so you are in the loop.
**Hanson** 37:54 we can… there's enough heads, we can probably, you know, spare one for that. I'm… I'm out tomorrow, so, you know, but… but the week after, I think we can… we can discuss, How to assign, folks.
**Carlos Alberto Cortez** 38:07 Yeah, for the clock one, you mean?
**Hanson** 38:09 For the clock… well, for things in general, yeah. But I won't be there tomorrow for the clock one, so, you know…
**Carlos Alberto Cortez** 38:14 No, no, no, no, just like, no, no, actually, that's… anyway, yeah, but that's just thinking loud, loudly, but yeah. Okay, perfect. Let's do that.
**Jason Plumb** 38:22 Well, Hanson, now that you told me that you're not going to be there tomorrow, I have a question for you, because I put it on the Sig Notes for tomorrow, but, do you know if we have any data yet whatsoever from the last Android release in the Play Console thing that you wired up?
**Hanson** 38:37 When did it get released?
**Jason Plumb** 38:40 Like, a week ago, or two weeks ago?
**Hanson** 38:43 Not 2 weeks ago, right?
like, the actual Los Angeles release? Five… yeah, 5 days ago. Okay, yeah, okay. It says it's about 7 days, they should get an email, the registered email address should get an email. I'll let, I'll let Severin know that, we released 5 days ago, and, I… believe no one needs to actually use it. I think once it's published, it should be picked up. But, you know, who knows Google and their timelines. It's pretty random.
**Jason Plumb** 39:13 Are you and Severin gonna be the only person, only people starting out that have access to it?
**Hanson** 39:18 I don't have access to it. It's whatever accounts everyone use to create it, which is, I think, admin.opentelemetry. I think once that happens, then they can grant access to individual, Google accounts.
**Jason Plumb** 39:33 Oh, good. Okay, okay. Okay. That's cool. Google accounts, ugh. So we just went through this transformational process, which killed all… like, they destroyed all of our Google accounts, basically, because… Cisco's a Microsoft shop.
**Hanson** 39:47 If you have a personal one, I think that works too.
**Jason Plumb** 39:49 I think it's gonna happen, but it's not associated with another GitHub activity at work. Anyway…
**Hanson** 39:54 Okay, I see. Fun.
**Jason Plumb** 39:57 Okay.
**Hanson** 39:58 Oh, speaking of release, it's out, and… but there's, like, another… yeah, so… Did we… yeah, okay, anyway, nothing we needed.
**Jason Plumb** 40:09 Yeah, I was curious, like, in that release process.
How many hiccups there were, and how many of those were because it's the first time doing it, versus, like, oh, we have actual improvements to help automate here.
**Jamie Lynch** 40:24 Yeah, I think it took about 3 or 4 goes.
And I think a couple of those were just due to the version script.
Always assuming there's a previous version.
**Jason Plumb** 40:36 Oh yeah, both.
**Jamie Lynch** 40:37 The… it's just taken from over to Laboratory Android, so I assume it got written after the first version was created, but… And, yeah, Ben, there were… Like, a couple of… signing… things, like I… Yeah, I think I set the case slightly wrong for the secrets, so, that failed it, but… It was reasonably smooth, so hopefully next release should be as simple as just running the workflows.
**Jason Plumb** 41:08 Sweet That's great.
**Hanson** 41:11 We can… we should probably just do a second release for the hell of it for testing, like, you know, in a few days or something like that, just, you know.
Because why not?
**Jason Plumb** 41:20 Is, is Kotlin also doing the changelog, automation and filling in the, like, is it putting the release… is it automating the release in GitHub as well?
**Jamie Lynch** 41:30 Yeah, it automates the release, and it's got a workflow that drafts for changelog notes, and then I think there's, like, some human editing.
**Jason Plumb** 41:39 Cool.
That sounds good.
**Hanson** 41:45 Sweet.
**Jamie Lynch** 41:48 Cool. Anything else?
**Hanson** 41:50 Nope, done for real now.
**Jamie Lynch** 41:54 Thanks, everyone. Thanks, everyone.
**Carlos Alberto Cortez** 41:56 We do, to help.
