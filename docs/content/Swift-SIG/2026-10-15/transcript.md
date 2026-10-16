SIG: Swift SIG
Date: 2026-10-15
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Marius Ciocanel** 02:01 Hey, everyone.
**Ben Joseph** 02:14 Hi Marius.
**Vladimir Kukushkin (Apple)** 02:16 Oh.
**Ben Joseph** 02:24 Marius, are you from, Dayton?
**Marius Ciocanel** 02:29 No, I saw, I think you're, is there someone else with my exact name and last name? I saw someone joined on, on the Android. Yeah. Hotel, but no. Right.
**Ben Joseph** 02:43 Yeah, that…
**Marius Ciocanel** 02:44 No, I…
**Ben Joseph** 02:44 I was asking.
**Marius Ciocanel** 02:46 I… no, no, different… like, yeah, I saw that, I was like, well, that's gonna be confusing.
But no, I, I joined because like I'm looking into like observable, like I'm trying to learn more about observability, and I was playing around with the code and saw something I could fix.
Thank you, everyone, for, I guess, approving the… the change for the iOS 27.
Crash. So, yeah, just wanted to see what these meetings were about, and if I can help.
In any way, specifically with… Like, on device testing, because from what I've… researched, I think that's an area where… Not a lot of time is being spent on, so…
**Ben Joseph** 03:34 Absolutely. Thank you for joining.
**Billy Billy** 03:38 Yeah, devices are also just, like, annoying. You need to have the devices in the first place. Not everyone has them.
**Ben Joseph** 03:45 Only solution.
**Billy Billy** 03:46 Honestly.
Takes a while to get it all set up.
**Marius Ciocanel** 03:52 And.
**Billy Billy** 03:52 Yeah, that would be great, yeah.
**Marius Ciocanel** 03:55 I tested, I did some on-device testing for the fix, and I had to renew my Apple developer membership, because for some reason I had too many registered devices. I'm like, oh, okay, well.
**Billy Billy** 04:08 It's got a pinwheel.
**Marius Ciocanel** 04:11 I had one lapse from.
In 2019.
So I think, like, I just paid, and it went quite quickly. Like, it took about an hour for it to be live, so… Yeah, but yeah, I do agree.
Testing on device can be a pain.
**Ben Joseph** 05:11 Hey, Billy, do you want to drive the meeting?
Oh, that's right, yeah.
**Billy Billy** 05:18 Sure.
Yeah, not true.
**Nacho Bonafonte** 05:23 a… Sorry, I'm late.
Yeah.
Sorry, okay, let me… Yeah, let me connect my… Can you hear me?
**Ben Joseph** 05:52 Yes.
**Nacho Bonafonte** 05:53 Yeah, thanks.
Sorry for being late, I guess.
This meeting. Okay, yeah, let me… have you started already? Sorry.
**Ben Joseph** 06:05 No, we were waiting for you.
**Nacho Bonafonte** 06:06 Okay, yeah, sorry.
Yeah, Bryce told me he couldn't join.
Oh, he cannot join today, so I will try to… Great, that's cool, that's cool.
Okay, so let me… Yeah, I see you have updated the document, so let me just share it.
Okay… Yeah, this is the document.
Yeah, I see we have someone who's new in this meeting. If you want to introduce yourself.
Yes. I am not so one of the maintainers.
And the rest, I don't know if they will want to also present themselves, but yeah.
If you want to just… Present? You are free to not do.
**Marius Ciocanel** 07:06 Sure, no, I'll… I'll do a quick… I did a quick intro before you… we joined. Like, I'm Marius, I've been doing iOS for over 15 years, and… Recently, I've been working on payments and identity SDKs, and I want to learn more about observability, so… I found the… OpenTelemetry Swift project. And as I was playing with it, I realized it wasn't working on iOS 27, so I saw a chance to contribute, so I did.
I already told everyone else, like, I can help with on-device testing if… Because I know that that could be a bottleneck, and not everyone can… Has the resources to do it, so… If I can help in that way, I'm more than happy to.
**Nacho Bonafonte** 07:51 Okay, yeah, yeah, totally open to any help that you can provide, but yeah, so yeah, just… or with, yeah, some issues, or whatever, we have.
So, yeah, let's… For the rest, do any one of you want to present yourself?
I don't want to block you, if you want.
But yeah, you can see on the document the names and where the people is from.
So, okay.
So, from last week, we had the.
We have here Billy presented his instrumentation contribution plan for next month of October, sorry for this month.
Which was, amazing, so, yeah.
We are gonna try to be there, just… Yeah, approving and reviewing as much as possible.
So, we also had some, here topics from our PRs from Vishwan and Ben.
That I think… all of them are merged already?
**Vishwan aranha** 09:03 Yes, they were all merged. So yeah, those are from last week. Yeah.
**Nacho Bonafonte** 09:07 Okay, great.
And we also talked about some client-side semantic conventions discussion.
About, yeah, the semantic conventions, and if people wanted to join there, or, and add your needs, your thoughts, or your… your… specific things for iOS, for the semantic conventions.
On the… on the client.
That will be great for those who have more experience or have needs in their own libraries. That will be great.
So, new topics we have here, I will start with the first one.
Who brought it to… the table.
Oh, yeah, it was…
**Vladimir Kukushkin (Apple)** 09:58 Right.
Yeah, that's me. Hi, for those who don't know me, I'm Vladimir, I'm from Apple. Confusingly, I'm from that side of Apple that Works more with the Linux and open source Swift ecosystem, Swift on server, so the Wonderful bridges towards Swift observability, APIs, Swift logs, Swift metrics, distributed tracing that OpenTelemetry Swift supports. That's where I come from.
Less on the iOS side.
Right, so, I created a couple of issues.
I don't expect we go through all of them. They are quite minor. I hope we ourselves gonna have some time to work on them in the near future. But one of them Yeah, this particular, worth discussing. So the idea is right now OpenTelemetry Swift is using URL session for its own communication for exporting.
And on iOS and macOS and other Darwin-based platforms, that's perfectly fine, that's the correct solution. But on other platforms, Swift support, Linux, Linux, for example, URL session is not the most optimal, transport. There is the async HTTP client.
And it's possible to create yet another HTTP client abstraction implementation, protocol implementation that is actually based on async HTTP client. One of the big deals for that, apart from URL session being not perfect on Linux, so to say.
Async HTTP client has MTLS support, which might be important for server-to-server communication.
So we can create HTTP client implementation for that. But the question is, if everyone brings it gets it. They have a lot of dependencies, most important is Swift Neo, which is huge, and it's a huge compilation time for everyone. So I wanted to discuss how do you guys think, Should he use a trade?
Or a separate package.
Things like that.
**Nacho Bonafonte** 12:14 Yeah, yeah, I think… I think it's great.
Yeah, if that's needed for Linux, definitely we want to.
Be, good supporters of the platform also.
So, yeah.
We, we already… having Neo and NeoSSL as libraries in the project, they are already, imported by… Protobuf, and something, and gRPC… for the GRPC… exporters, we are linking with SWIFT.
Oh, yeah. Street Neo already, and yeah, lots and lots of libraries, so we're already loading it.
Main… I don't know if you can… work on that, exporter. Probably it will be only Linux.
exporter, right? It will be a version of the… for the Linux exporter, initially. I mean, my main concern with this is version of the libraries.
If it can be done with the actual version of the libraries, or newer.
Third-party libraries are needed.
Which, you know… brings her… Like, a cascade of changes everywhere.
And also, with a minimum Supported version, so… I… We already are using, I think, SwiftNeo, it's on version 2.
102.
Neo Extras, Neo HTTP2, Neo SSL, we have lots of them already imported by the… by the… a waterfall of… libraries that it brings. So… Yeah, I mean, totally open to that. The only concern is about the versions that you need for that.
In order… not to force minimum supported versions for other platforms. So, if that's only for Linux, and it can be… those versions can be just… I mean, if it can be done with the existing versions, it will be great. If that can be done with an ifdef.
just a conditional compilation for Linux, it will be great. Yeah, totally open to supporting Linux in a good way.
But yeah, you know, yeah, dependencies are a lot. Even if you don't import them in your targets, SPM already downloads them. So yeah, but we are already on that, on that.
on that situation already with the existing NEOs. If you need something newer, but still has a minimum version of iOS 15, for example, that's our new minimum now.
That, that will work also.
So basically, Xcode 26, so probably Swift 6.2, and iOS 15, I think that's… we have updated our minimum version now. Yeah. for the latest… for what we expect to be the 3.0 series.
Because we have put back… we were separated into repositories, and we moved back to just one, because maintenance was a nightmare.
So yeah, working now with just one, and we are planning to… yeah, the minimum version is already updated on the main repository. So yeah, totally open. If you need to update any of those libraries.
and it doesn't change the minimum iOS version, that will be great. If you need newer ones, then it can be possible to do only for Linux.
That would be awesome.
Trying, yeah, not to… Yeah, you know, this is… Yeah, what it is,
**Vladimir Kukushkin (Apple)** 16:07 That's it.
6.2 should be fine. We've recently updated all our acquisition, open source acquisition packages to 6.2. So it's 6.2, 6.3, 6.4. We usually support three latest minors.
Okay,
**Nacho Bonafonte** 16:22 Yeah, the only… yeah, it's not 6.2, but also the… what each system supports, right?
Yeah. There are, you know, there are many things on Swift that come with new versions, but are not backported to older iOS, and that's our current limitation, I would say, for that.
**Vladimir Kukushkin (Apple)** 16:41 Yeah, cool. Then I guess the, whether this could be the default transport in Linux, we can discuss later when there is an implementation.
**Nacho Bonafonte** 16:50 Yeah, it can be the fault. We don't mind. I mean, if you say it's… just much better because your recession doesn't work, okay.
we take your word. I don't think anyone has.
real, experience on Swift on Linux on this.
**Vladimir Kukushkin (Apple)** 17:08 correct.
**Nacho Bonafonte** 17:09 Group here. If so, please say.
Say it loud. Cool. But I don't… I think we just have tried supporting by Linux by, yeah, by contribution of the community right now, so… Yeah, great.
**Vladimir Kukushkin (Apple)** 17:24 Yeah, that's basically why I also created all those small issues, just hoping someone from community can pick it up before.
**Nacho Bonafonte** 17:33 know.
**Vladimir Kukushkin (Apple)** 17:33 Get there. Yo.
All right, cool.
**Nacho Bonafonte** 17:36 Yeah, we can ticket them later. We will review all the new issues, and we can ticket them as a first good topic. Yeah, I reviewed them slightly, and yeah, they look like, yeah, just small fixes in small areas.
**Vladimir Kukushkin (Apple)** 17:52 Right, yeah, that's it. Okay, thank you.
**Nacho Bonafonte** 17:54 Great.
Okay, let's.
**Billy Billy** 18:00 Yeah, I think there's, like, a bunch of, general issues with the, like, the exporters for now. I put some of that into, like, my instrumentation plan, like, And then, there's also, like, an existing pattern for, like, having named exports for the various, or named targets for the, various exporters, so it should fit in nicely with, like, what you're, proposing.
Yep, just adds a couple things on.
**Nacho Bonafonte** 18:28 Yep.
Yeah, yeah, the truth is that now the package is a bit complex.
A bit more than it was before.
Yeah, and yeah, if anyone has any idea to order that in a better way, totally open, right? We must try to make things as easy as possible for everyone.
Okay. So, local graphana view for instrumentation, Billy.
**Billy Billy** 18:54 I guess we can just go over the third one, just real quick.
**Nacho Bonafonte** 18:58 Okay, yeah.
**Billy Billy** 18:59 This is something that Vladimir helped us with last week, just so everyone's aware that this happened. Like, there was just, like, a small bug upstream, like, and Vladimir took care of it.
There's… you can just read through it if there's any questions. I like the, the… the issue, I think below.
So… Yeah, so, yeah, thanks, Vladimir, for helping us with that last week.
Yeah, the issue's in the comment above.
on… And then the, the more interesting thing is that, I'm, like, putting together, like, a, local view for, like, all of our instrumentations, as, like, just to help with the development.
it was, like, just between Signas and Grafana, and figured I might as well do Grafana, since we have all these Grafana people here, contributing now. I can give, like, a quick walkthrough of, like, what's.
I'm going to PR if you guys are interested in seeing and maybe you guys have some tips. I don't know. I'm a first time like Grafana user.
Can I, take over the screen share?
**Nacho Bonafonte** 20:09 Yes, sir.
**Billy Billy** 20:12 Thanks.
So, yeah, screens are most right now.
This is the wrong tab.
Okay, so, as I'm doing the instrumentation stuff, like, I needed a better view to, like, see what's going on, and Grafana obviously is, like, very good at this. This is, like, a custom dashboard I put together.
Yeah, please, like, feel free to cut in, because, you know, first time doing this, but… You have your sessions on the left-hand side. Thanks to all the contributions for making the, sessions a little more stable.
in the last, like, couple weeks. You can kind of see what's going on here already with, like, all the device starts and whatever. A couple issues I noticed is that, like, we don't have, like, an event name for.
all the, network spans right now. This is just an events… simple events table that shows both logs and spans, and then you have a simple, like, Gantt chart above, and then here on the right-hand side, you have, like, the selected view. Didn't realize, but yeah, it's just, like, totally custom. You can just kind of, I'll PR this in a moment, but, like.
It's really amazing what we can do, just a couple of JSON configurations. You can also go through some of the crash examples from last week.
Yeah, like, it's… Puts together all of this, the, You can, like, really easily demo with the simulator. If you just have this here, you just click all the you know, the different, troubleshooting scenarios, and then I'll just write to the local collector, and then the Grafana view will just, like.
Pull from the local collector and create this view.
You can see here, I, Wrote a custom log that says, like.
force, caused a crash with the force unwrap. And here, like, the instrumentation, like, recovered the contacts, it recovered the original, session ID and the original timestamp that the actual crash occurred.
It has a really good crash message, like this is all from native KS crash.
It's like really clear what happened. Here's the very, very long stack trace.
Exception type is also really useful.
Anyways, this is kind of what's going on. I might add like another small feature for like if the crash cannot be recovered from the original context, like right here.
Like right here, the crash is at the session start, which doesn't make any sense, right? So in this case, like it was unable to find the original context like it was here. So I probably need an add an attribute to say like.
It just, wrote the, the session ID and the timestamp as is instead of recovering, so I can add that field as well. But, this is just to give you guys, like, an idea of, like, what's going on. Does anyone have any questions?
**Nacho Bonafonte** 23:13 I mean, it looks good. It looks very good.
**Billy Billy** 23:17 Okay, cool.
Alright, that's, like, pretty much it. I'll, PR this, and then, I go back to Sorry, my computer's, like, crashing. Hang on.
Yeah, it's actually crashing. That's crazy.
Oh, no, it's just this thing.
So let's see.
Yeah, and then the rest of the month, I think I'm on target to do the rest of the things. Next things that are coming are the app hangs… sorry, app hangs here, and app launches.
These will be a little more complex. These might slip to the next month.
But yeah, just, just giving you guys a quick update. Let me know if you have any questions.
**Nacho Bonafonte** 24:14 Yeah, it's looking very good.
Thanks, thanks a lot, Willie.
**Billy Billy** 24:21 Cool.
**Nacho Bonafonte** 24:23 Yeah.
**Billy Billy** 24:25 Thanks.
**Nacho Bonafonte** 24:26 Too fucking fun.
Okay, so those were the last topics.
Right.
yeah, any other topic that anyone want to bring? If not, we will go to.
review issues and PRs that are there, Andy.
Okay.
So, let's move to… Yeah, issues… Yeah, here, yeah, there are all the, Vladimir issues he opened today. Thanks for that.
Are all of these, Okay, all of these are… The issues you found, right?
**Vladimir Kukushkin (Apple)** 25:19 Yeah.
**Nacho Bonafonte** 25:19 And should be easy to fix.
**Vladimir Kukushkin (Apple)** 25:22 I believe so. Yeah, maybe this include trace context false. I'm not sure. There's many places where it propagates.
So probably someone who knows what is the intended design should review this.
But everything else is straightforward.
**Nacho Bonafonte** 25:47 Yeah, just to add some, Some labels here, for people to To visualize that, and no, they can take it if they want.
Oh, sorry.
Yeah, we… sorry, I closed that one with the first one, without really taking a look.
So, this is about… Now, this was your proposal.
**Vladimir Kukushkin (Apple)** 26:30 Yeah, this is the.
**Nacho Bonafonte** 26:31 Yeah.
Yeah, and I have food as a good first issue. Sorry, I just messed it.
Okay, Hotel Log 100 doesn't support metadata provider.
Okay.
Oh, folks, back to Estefan Wichita.
**Vladimir Kukushkin (Apple)** 26:49 Yeah, so look handlers have multiple sources where they can get the metadata dictionary and to combine into the effective metadata.
One of them is not supported.
Should be straightforward.
**Nacho Bonafonte** 27:05 Okay.
Great. Yeah, if anyone wants to take one of these already, you can raise your hand.
But… If not, I will just label them.
This is about include trace context for systematic reductive span context to a reload record. Okay.
Yeah, if… Activist.com.
Yeah, I… I don't know exactly about this.
But, yeah, it looks like an issue.
Probably, if you don't want to save that context, we shouldn't do it.
Yeah, clearly.
That should be review, I think this was Bryce who wrote it initially.
Maybe he can take a look back. He's very short on time recently.
Midday data.
Thanks for wrapping up with SNK. There's no way to write a more global metadata. Yeah.
**Vladimir Kukushkin (Apple)** 28:16 Yeah, so, again, those multiple sources, Log Handler accumulates metadata from.
There is semantics on the SwiftLock side, how we treat the hierarchy.
So basically, in the call site, you should be able to override whatever.
And currently it's working the other way around, so whatever you attach to the handler that.
**Nacho Bonafonte** 28:38 It should take more than…
**Vladimir Kukushkin (Apple)** 28:39 Global, yeah, he's taking over.
**Nacho Bonafonte** 28:43 Yeah, that also looks like an easy one.
For reviewing… The phone number providers are not up.
**Vladimir Kukushkin (Apple)** 28:54 Yeah, I would call this more, So, in the code, the default thing should be different, but this is also, I think, a problem of the documentation, so whoever's gonna look into the documentation, they will take the first example.
And don't get any locks.
So there is a third example where logs are actually flowing.
But first two examples have the default configuration that doesn't export anything.
**Nacho Bonafonte** 29:27 Okay, yeah, great. Also looks an easy one.
Yeah, I don't know, Yeah, for Anissa.
On our site, also.
Yeah.
Some of these libraries maybe have not been used much or put into testing.
And that's… yeah, this one, if you want to also introduce.
**Vladimir Kukushkin (Apple)** 29:55 Yeah, this one. So this is not logs, this is Swift Metrics bridge. So how metrics are represented in the Swift Metrics is a metric object is created per… Label and dimensions, type, label, and dimensions.
And right now, all the metrics are squashed into the… Type plus label.
So… The issue is if someone creates the same metric but with different dimensions, they might end up with just wrong values.
**Nacho Bonafonte** 30:33 Yeah, okay.
Yeah, that should also be…
**Vladimir Kukushkin (Apple)** 30:38 Yeah.
**Nacho Bonafonte** 30:39 Yeah, I'm missing.
**Vladimir Kukushkin (Apple)** 30:40 Again, again, should be straightforward. I think, All of them are probably one line, or several lines, fixed.
**Nacho Bonafonte** 30:54 Yeah, so it's basically.
**Vladimir Kukushkin (Apple)** 30:55 about…
**Nacho Bonafonte** 30:56 Yeah, it's very clear. So yeah, once it can be one…
**Vladimir Kukushkin (Apple)** 31:01 and.
**Nacho Bonafonte** 31:01 With these explanations, I think it's easy to reproduce and try to find the things.
**Vladimir Kukushkin (Apple)** 31:08 Yeah, so I think the main challenge here would be to make a development setup to verify this.
We don't have a good example anywhere.
for using Swift observability APIs and Open Telemetry Swift together.
Like the end-to-end example. We have one for Swift OTEL. We haven't migrated that one to OpenTelemetry Swift yet.
So…
**Nacho Bonafonte** 31:32 Okay.
**Vladimir Kukushkin (Apple)** 31:33 Yeah, up to whoever is fixing this to make their own setup.
**Nacho Bonafonte** 31:38 Yeah, that, that, that's, yeah, that's true.
Okay, so, yeah, thanks for that.
Okay.
Okay, so…
**Billy Billy** 31:52 Otherwise, Sorry, I have a quick question. By the way, is, like, Swift Server, like, kind of gaining in popularity right now? Because, I was just kind of curious about that.
This is kind of a question towards Vladimir.
**Vladimir Kukushkin (Apple)** 32:06 Yeah, it's slowly, slowly getting popularity, trying to overcome the, broad, perception… broad opinion that Swift is just for making iOS apps.
So Swift supports multiple platforms, Windows embedded.
And Swift Server is probably the most mature out of them.
The observability is a huge part of it. Another big part is Swift and Java interop.
Another person from Apple, Conrad, is working on, so you can seamlessly interop from Swift to Java libraries, replace piece by piece in your services, things.
Yeah. So the main value we are saying all the time, why should you use Swift on server?
Instead of Rust or Go.
Is, Swift structured concurrency that makes, concurrent applications very easy to comprehend.
And all the performance that comes from it.
**Billy Billy** 33:20 Okay, thanks.
**Nacho Bonafonte** 33:25 Okay, yeah, the rest of the issues have already been here for a long time.
Is anyone interested in reviewing any of this, or let's go to the… to the PRs, or the… Or the pull request.
Nope.
**Billy Billy** 33:53 I think I'm okay, like, maybe that, reintegration issue should be closed now.
**Nacho Bonafonte** 34:00 which… Sorry, which one do you… can you read the number?
**Billy Billy** 34:07 The, 1137? The,
**Nacho Bonafonte** 34:11 Sorry, I… yeah, this is… Don't know why it went.
Yeah, this is the touch spot, the touch keyboard.
**Billy Billy** 34:21 It really says,
**Nacho Bonafonte** 34:24 Yeah,
**Billy Billy** 34:25 reintegrate quarantine.
**Nacho Bonafonte** 34:27 Oh, this is also done? Yeah.
And the other you say, which one? This one is the one you say.
**Billy Billy** 34:33 the.
**Nacho Bonafonte** 34:33 aware.
**Billy Billy** 34:34 Yeah, 1137, yeah.
**Nacho Bonafonte** 34:35 Yeah, this is done.
Okay.
So, for the PRs, yeah, I… I think we have merged many recently.
Thanks a lot, everyone, for reviewing.
So, we still have many URL sessions.
PRs that were opened by Tomari.
But he has not appeared back. Yeah, he… we had several issues here. Now the problem is that many of them, are conflicting.
Because one of the fixes in one of them made the other conflict.
So many of these are working and approved, but The user has not come back, or… for… for fixing them. And I also think we have In some others, apart from the conflicts, that should be solved, that we might also try to solve.
ourselves if it does not appear. Maybe that… if anyone wants to do that, it's also an option. Sometimes you can take the branch and fix it, and sometimes it's private and you can't, so… As it has been… they have been here for a long time. I tried fixing one, and I… and I… and I couldn't.
I think maybe it's this one. I don't know, I couldn't do that. Yeah, we also have here the gRPC script to version 2, but I think this… change, if my memories don't fail, means that we had to update some iOS version to something newer than even 15, but I'm not sure about that.
Yeah, this is the only one I'm not sure about the rest.
We have, yeah, more, renovate here.
We have here one for the active span lookup.
That was from last week.
This one also from last… from last week.
And more… Renovate of libraries.
Yeah, I… oh, this is… this is true authentication, it has a new version almost each day.
Yeah, yeah. Because I think I merged one today with one single one.
**Vladimir Kukushkin (Apple)** 37:10 Yeah, sorry about that. We are fixing this fallout of that merge of the distributed tracing. Should be it now.
**Nacho Bonafonte** 37:20 Okay, yeah, great. Yeah, there are many, many things that are updating. The main problem with this is that From time to time, we break compatibility, which is a bit of a nightmare.
So yeah, we must take care of those.
But yeah, that's… That's what we have to do.
Okay, so, we had this one, with support active span lookup in Swift Tracing Bridge.
Yeah, this has a conflict. I don't think if anyone has checked it.
And.
Okay, I… yeah, I have not checked it.
The, yeah, the thing is getting the active span from the, as it's come from.
Swift… From citizen certification, I can imagine it's in the task, right?
The identifier of the parent.
Because you… you set that inside the task, right?
On, on this, on the… Street distributed tracing?
**Vladimir Kukushkin (Apple)** 38:40 Yeah, so, let me… Let me look at this, I think I, yeah, an hour, yeah, it's, it's not, not a very new last week. Yeah, I think I did a quick, review. The logic's correct, yeah, it follows Swift Hotel, But what, what are the conflicts? Are they just technical?
**Nacho Bonafonte** 39:21 Yeah, maybe… I think it was an exporter. Yeah, Prometheus exporter test, I don't know. We have a conflict with Prometheus exporter, because I think for Prometheus, we were only testing metrics.
But yeah, probably he changed this. Right, right.
Okay.
Yeah, so this is the conflict. It should be doable, I think we can… For the rest.
For the rest of the code.
Vladimir, if you… I'm not expert on civic disability testing, but if you…
**Vladimir Kukushkin (Apple)** 39:56 Yeah, I can give a look and write something, write a comment like, hey, from the distributed tracing point of view, that's fine. Okay, great.
**Nacho Bonafonte** 40:08 That will be great, so we can approve that when… and merge when he… And he fixed the conflict.
He has been active, so probably we'll answer quickly.
Because he also created this other PR.
About reporting exception types instead of error codes.
Yeah, it was also, about, yeah, reporting the names. Ben, reviewed it and asked some more, and… Yeah, and also, he approved it.
I don't know why it's failing.
I think I rerun it.
And it's still failing, so… Probably.
He has to check that, but after… Ben, review here that very quickly, the fix. But I… Yeah, this is the one that's not building, but… That's the last PR that we had for reviewing.
Yeah, 1 of the things he mentioned in this was also about the Linux.
So maybe that also, maybe you're also interested in that. It mentioned that for the Spanish section test Linux blitz.
Type names to NSR domains.
Which must also be normalized. That's what he said.
For… The errors.
Which I believe it could work.
But… Yeah, if you have any take on that also, you can add a comment there in the, in the Yeah, I say to you, because you're the only Linux user here.
So if you… I saw that it had some… it referenced at Linux for that.
So yeah, I don't… We can wait for some comments there for approving.
Oops.
Okay.
And I think those, yeah, these other are more dependencies.
Some of them are approved already.
From Yes.
So Yeah, if they are minor, I hope they don't break. If not, we will know tonight.
Okay, any other topic?
Any other thing anyone want to bring?
Yeah, one thing I wanted to bring, it's not about these PRs or changes, it was about Billy, moving Billy into the approvers list. You have been already helping on the project for a long time. You have been in the Triageura group.
But last… I think it was last week. We, we, we promoted this one, and, and… And then, directly to… to approvers. So, yeah, I think you… you have been helping a lot.
For longer time, really, and we should… move you to approver. Sorry for not adding you to that list already. So if you please can create a PR with that, I will move it as fast as possible, if you really want, right? Sorry for that. I want to say that publicly.
Not having recognized, or taking so long for recognizing your hard work here.
Yeah, sorry.
**Billy Billy** 43:50 That's okay.
**Nacho Bonafonte** 43:53 So yeah, please, please, if you can…
**Billy Billy** 43:55 That's really nice.
**Nacho Bonafonte** 43:56 It's great that, yeah, we will… I will… I will try to move that as soon as possible.
**Billy Billy** 44:04 Thanks.
**Nacho Bonafonte** 44:08 Okay, then if there are no more topics, We can get back 15 min of this meeting back to your More problem.
DVT time.
Yep.
Thanks. Thanks a lot, anyone, for coming. Please review PRs and take any Issue, if you can.
Have a nice week, and a nice weekend.
**Marius Ciocanel** 44:34 everyone.
Nice talking to you. Bye.
**Ben Joseph** 44:37 Thank you. Bye.
