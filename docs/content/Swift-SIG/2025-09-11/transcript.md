SIG: Swift SIG
Date: 2025-09-11
Duration: 54 minutes
============================================================

## Zoom Recording Transcript

**Bryce Buchanan** 00:23 Hello, how's it going?
**Billy Zhou** 00:26 Hey, Bryce.
**Bryce Buchanan** 00:28 Hey, Billy.
Hi, Martin.
**Martin Holman** 01:16 Hey, how's it going?
**Bryce Buchanan** 01:17 Good.
We'll give a minute for Ari and Nacho to show up.
**Martin Holman** 02:19 Sounds good.
**Bryce Buchanan** 03:05 Even on.
**Vinod Vydier** 03:06 Hey, hello.
**Martin Holman** 03:11 Blue.
**Bryce Buchanan** 03:27 Financial.
**nacho** 03:29 Hello.
**Ariel Demarco** 03:32 Hello, everybody.
**Bryce Buchanan** 03:34 Hey, Ari.
Alright, let's get started. Let me share my screen here.
Okie dokie…
Alright, topics from last week.
I mean, there are a lot of topics from last week.
Alright, so… Let's take a looky-loo… if anybody…
Took this on, doesn't look like it.
That's okay.
I think, I think that this… this issue, the metrics filter, could be a relatively
low complexity edition, but I haven't really looked too closely at it, but if anybody's interested, please take a look. It's the one… it's one of the few,
features that actually has somebody asking about it, so it'd be nice to get it implemented.
Data compression follow-up, the PR is still open, and I don't think there's been… oh!
That's a different PR.
Yeah, the PR to the actual data compression is still open with no movement, and so we just brought in what we needed into our own project, and did that fix our CocoaPods issues, Ari?
**Ariel Demarco** 05:27 We have to do a new release. I think that with the OpenTelemetry core now included, we can… we can try it out.
**Bryce Buchanan** 05:35 Okay, cool.
**Ariel Demarco** 05:36 We also made some changes to the CI, so it's a rerunnable job, just in case, I don't know, there's a timeout or something with CocoPots.
**Bryce Buchanan** 05:46 Yeah, that's good. Thank you. Thank you for doing that.
So we still do not have a new Slack channel for notifications.
I'm not sure…
who we need to talk to about this. Maybe I'll message, I'll message, Alolita about it.
To do document release behavior for Swift Core Swift,
I guess we're still kind of in the process of figuring out what that is.
I guess we can discuss it more. I think you've got some topics here regarding that, Ari.
Simcon, that's not important. It looks like the sessions was merged.
Oh, nope, still… oh, this is, still not merged.
**Billy Zhou** 06:46 Yeah, fixed the flaky test. I think it was, like, a rebasing weird thing going on, and then, yeah, it just, it fixed it and needed another review.
**Bryce Buchanan** 06:57 cool. I, I, I like this, this feedback.
**Billy Zhou** 07:01 Okay, I can do that.
**Bryce Buchanan** 07:03 Yeah, so,
And I'll update the branch as well. Well, and I'll get this merged as soon as that feedback's,
Dealt with.
**Billy Zhou** 07:15 Okay, cool.
**Bryce Buchanan** 07:17 Okay, so this path, continuing down. Oh, is this the, remove NEO? So you, Martin, this has been… this is ready for review?
**Martin Holman** 07:28 Yeah, it's been reviewed, I think Nacho and Ari reviewed it. I had another… I put it as a topic for today, but,
I haven't investigated this at all, but I was just, like, double, you know, crossing the I's and dotting…
the Ts, and noticed that there are two files in there that still have, like, references to NEO. I haven't touched either of those, but I removed the dependencies on NEO from that target, so I would have expected them to fail compilation.
If anyone happens to know why that is, let me know, otherwise I'll just keep poking at it. Or we could still merge this, probably, because, like, it works, and look at that later, but it just seemed weird to me.
**Bryce Buchanan** 08:08 Yeah, that is really weird. I'll take a look at that.
**Martin Holman** 08:10 See?
**Ariel Demarco** 08:12 But… What you're… you are mentioning there, are the exporters.
you removed it from OpenTelemetry, which ones…
From which targets do you remember?
**Martin Holman** 08:24 From the tests, and the references are in the test files.
**Ariel Demarco** 08:31 The test target of which…
target in particular, but… because I think that at some point, we wanted to remove it from OpenTelemetry API, SDK, and some others, but those tests are referencing to the exporters, maybe…
it's okay on those exporters, because already they depend on NIO.
**Bryce Buchanan** 08:56 Yeah, that might be… that might be why they're showing up, yep.
**Martin Holman** 09:03 Got it.
So it's like a transitive dependency between…
**Bryce Buchanan** 09:06 Yeah, yeah, so gRPC, the exporter depends on gRPC Swift, which has NEO as a dependency behind… underneath it.
**Martin Holman** 09:15 Got it.
**Bryce Buchanan** 09:16 Yeah.
**Martin Holman** 09:20 Okay, this is probably ready to emerge then, and then we can look at those, the two other references to NEO in those tests later.
**Bryce Buchanan** 09:26 Cool. Alright.
Okie dokie, let's hop into matching core version, main repo, initial core release to satisfy CocoaPod assumptions. Yep. Yeah, so that's Ari. Ari's taken care of that, and here we are at the new topics, so we have…
Swiftcore release at 2.1.1.
And I saw your message about the pre-release Ari.
And that was just kind of like a final fail-safe I had in the… in the, automated release process.
But, the… I just, you know, go in here and check the set last release.
Her latest release on that, and so I just went and updated that.
For both of these. This one's… this one's just not pre-release, so it's not the latest.
But… Oh, that's interesting, though. You could potentially set the latest to be…
a non… a non-latest version, which is interesting. Just realized that, but… Stop it.
**Ariel Demarco** 10:26 It's mostly… I think it's mostly for stability, or for suggesting which version you should use.
**Bryce Buchanan** 10:32 With the latest.
**Ariel Demarco** 10:35 But, yeah, mostly asking because some customers of us asked why we tend to use pre-release versions, and I was, like, confused. And then I saw that some of the releases are marked as pre-release.
So maybe it's mostly just asking if it's… if it's something we need, or we don't. Mostly… mostly…
**Bryce Buchanan** 10:55 Yeah, it's, I just had it set as just, like, a final fail-safe, just in case, like, we run the release, and something goes wrong, or it's bad, and we don't have an immediate, like, thing that gets pushed out to anybody using…
our… our, SDK just automatically, and so, I just, like, let it sit, and then flip it to… to release once…
Once it looks okay. But we can… we can remove that. I mean, it doesn't seem like we've had any issues in the past, so it might not be necessary, it's just I'm paranoid, so…
**Ariel Demarco** 11:33 It's okay. We can leave it one day or two, or while we test it. I have no problems.
**Bryce Buchanan** 11:41 yum.
**Ariel Demarco** 11:58 In terms of doing an OpenTelemetry Swift release, now that it has 2.11 from Core included, shall we wait for something specific to do a release?
We… or we could do it.
Right now.
**Bryce Buchanan** 12:13 I think we should do it right now, because we do have, there is, someone asking about a good Cocopods release with the HTTP exporter working properly.
they are working on a, like, CocoaPods
like, observability SDK embeddable for React Native?
Or, yeah, so, so I think we should, try to get that out ASAP.
**Ariel Demarco** 12:49 Okay, I can, I can do it.
**Bryce Buchanan** 12:51 Cool, thank you.
Alright, yeah, and then sessions. Again, thanks, Billy, for putting this together, it looks really good.
**Billy Zhou** 13:00 Thanks, I just had a quick question about the…
like that. We're adjusting… we're extending the session to end event with, duration and end time, which wasn't in the semconf. So I just wanted to check in with you on, like, how to, like, put that into,
Like, the actual semantic dimension.
**Bryce Buchanan** 13:21 Oh, That would be through,
You'd probably want to go into the semantic invention, repo, and…
Like, work with, the maintainers there.
If they want to get that added, or… yeah. Yeah, I mean, they might have a good reason why they didn't add that, but, you could probably open an issue or a pull request to add them in, and start a discussion on that.
Let's see, so, if I go to, like… Excession…
I think that these… if I remember…
It's under General Docs. You probably… there's, like, a couple of different places, because you probably want to update the model as well for,
I wonder if it's under session, yeah, so session here, so…
**Grace Lim** 14:16 They have, like, a contributing…
README, and then there they give you the commands that once you update the YAML file, they have, like, scripts that'll update the specific doc files.
**Billy Zhou** 14:30 Oh, okay.
**Bryce Buchanan** 14:30 Yeah, there you go. Yeah, so you could… you could… yeah, I guess you don't need to, update the doc files yourself. You… you update the, model. So you come in here and add your, add your, additions here.
**Billy Zhou** 14:43 Okay, great. And then I saw you left a comment about, like, some, like, process for, like, there are Swift semantic conventions, like, some… there is, like, some process.
That, what was that about?
Back in the PR, you left a comment.
**Bryce Buchanan** 15:02 Oh, yes, that's right. Yeah, let me,
actually, you might actually be able to, to do this now, so that's not… I'm glad that you brought that up. Where is your PR? Here it is. So,
We have some generated, generated code from the semantic conventions that provide you know.
I guess, an enum that actually holds the names of these, of these attributes, so you don't have to, have them, hard… hard-coded.
If I can find them.
Not right now.
Where is my comment? Where is my comment?
Here we go.
Yeah, so, like, session ID, so…
if you go into… now, I guess it's gonna be in Swift Core now.
**Billy Zhou** 16:07 Oh, I see.
**Bryce Buchanan** 16:09 and then source, and then I added them to… Apis, and… Common, was it? Semantic attributes…
And then semantic conventions, yeah, so, these are all, like, the generated semantic conventions that are defined in the semantic conventions repo, and so you can reference, you know, semantic conventions.session, dot ID, and then, like, raw value, because that's just what we have to do, I guess.
And that way, you don't have to hardcode those values.
**Billy Zhou** 16:42 Oh, that's great. Okay, I'll make that change as well, thanks. Yep.
**Bryce Buchanan** 16:46 So it seems… it seems like it's incomplete. There should be some…
Seems like there should be some other ones, shouldn't there?
**Martin Holman** 16:54 I put in… I put in the chat as well, it looks like you're starting in terms of, like, epoch values, and I think OTEL mostly uses,
RFC 339 for step times.
**Bryce Buchanan** 17:13 Oh yeah, these probably need to be nanoseconds.
**Billy Zhou** 17:17 Oh, yeah, yeah, yeah.
**Martin Holman** 17:17 I don't know if, like, if you look at span, start, and InTime, they use,
RFC 3339 format for those.
**Bryce Buchanan** 17:27 Oh, okay. Okay, I see.
Okay, so I guess there's still a couple few changes there for you, Billy. Oh, okay, great.
**Billy Zhou** 17:40 Okay, we'll do, we'll do all those things. Thanks.
**Bryce Buchanan** 17:43 Cool.
**Billy Zhou** 17:45 That's it.
**Bryce Buchanan** 17:47 Alright, okay, so Grace, semantic conventions for screen loading, app launches, and app attributes.
**Grace Lim** 17:55 Yeah, so along similar lines as Billy, we're kind… we plan on making a lot of contributions, at least to the semantic convention.
repo, just to make sure the changes we're planning are, like, future-proof. So, with that being said, there's a couple things that I want to run by you guys before I go to client sick.
Just to see if there's any concerns, oh, I was…
Is it okay if I share screen real quick?
**Bryce Buchanan** 18:25 Yeah, go ahead.
**Grace Lim** 18:26 Nice.
**Bryce Buchanan** 18:26 Let me stop sharing here. There you go.
**Grace Lim** 18:29 Okay, let me find my screen, hopefully it's this one.
Oh, no. Okay, yeah. So, as of now, I haven't fully fleshed out what the span definitions would look like, but these are the attributes that I plan on proposing, so…
For… to start with, for screen loads, to give context, I have an open PR, actually, to add app.screen.name as a proposal, so…
Currently, the…
OpenTelemetry Android SDK is using just screen.name, and so when we were implementing, you know, monitoring UIKitFuse and
SwiftUI views. Like, since the terminology is very different, right? We were kind of using Vue.name, but we wanted to see if clients had had an idea of what we might want to use
That's, like, agnostic of the platform, and so the…
attribute that we landed on was app.screen.name. So, I have an open PR, it's still, going through a bit of back and forth regarding the comments, but given…
you know, this is kind of what we're going forward with, like app.screen.star. These are the other attributes we were
thinking of adding, which includes type, so, like, for Swift, that would be, like, SwiftUI UIKit. In case, like, to the app owner, they want to know the difference between the type, and then similarly… similarly for Android, it would be, like, activity or fragment.
Yeah, so that's the second one, and then there's, like, depth and nodes for the screens as well. I think,
I don't know if we made the contribution yet to upstream Android, but this is also something that we're adding, at least in the AWS distribution of it. So, yeah, let me pause here for questions or comments.
**Martin Holman** 20:20 I always don't…
**Bryce Buchanan** 20:22 Alright, go ahead, Martin.
**Martin Holman** 20:27 I was just gonna say, I always thought the app, prefix was for, like, developers, like, custom attributes.
**Grace Lim** 20:37 developers, like, custom attributes.
**Martin Holman** 20:40 Like, I'm instrumenting my app, I would use the app, like, prefix to be, like, app.mycustombusiness thing, and that auto-instrumentation shouldn't stomp on that, but I could be wrong.
**Grace Lim** 20:51 Mmm, I see, okay. So, yeah, I'm kind of new to this space as well, so I can run this by them as well, but…
like, I had asked them, like, okay, do we want to just keep screen.name? Because that's what Android is using, or should we have a separate one for Swift? And then they're like, no, we should do app.blahblahblah. So I wasn't aware of app.star being something, like, custom.
to a specific application, but I can, ask them again next week.
**Bryce Buchanan** 21:20 That doesn't appear to be the case, just based off of the, app namespace in the semantic conventions. It looks like it is dedicated for,
**Grace Lim** 21:29 you know.
**Bryce Buchanan** 21:30 Apps used by end users.
desktop.
**Martin Holman** 21:34 Okay, sweet.
Oh, yeah.
**Bryce Buchanan** 21:38 Alex, did you have a question as well?
**alexcohen** 21:40 Yeah, so, we've been thinking about something similar to this a lot, not specifically screen load, but more about… more about navigation, or more about where you are on screen, at any moment, which can be a little bit similar to screen load, in a way.
But we… we ran into the… an issue that,
you know, a screen is not always the screen, because, like, say you look at iPad, for example, you can have.
**Grace Lim** 22:09 Man.
**alexcohen** 22:10 multiple windows open at the same time, now. So a screen does not become a screen anymore. It's more like, what is… what is the area that you're looking at? And we… we ended up with something more in the vein of, like, surface, or… or some wording like that, like surface load, since you could possibly have two or three of them going on at the same time.
Depending on what you're looking at, and that also moves over to the desktop pretty well as well.
So I just wanted to mention that. And I can, if you, if you share your, I don't know if it's, if it's open source, but yes it is. If you share your, your PR, I would, I'd love to, to go look at it and comment on it a bit.
**Grace Lim** 22:57 Nice, okay.
Yeah. So that was actually something we had discussed in the thread, like.
**alexcohen** 23:06 Oh, cool.
**Grace Lim** 23:07 Yeah, so they wanted to make sure, like, what is a distinct view? And they did mention, for example, on tablets, there can be multiple screens. And so, for me, the scope of the screen I was thinking about was not, like, the entire screen of the
Device, whether that's a phone or tablet or,
desktop. It was just, like, bigger than widget, but it didn't have to cover the entire screen. So that was kind of the clarification I had made in the definition for this attribute. So yeah, maybe, you can also, you know, provide your insight on this when you take a look.
**alexcohen** 23:49 Yeah, I, I, I will. I, screen has, has an actual meaning, right? A real.
**Grace Lim** 23:54 Hmm.
**alexcohen** 23:55 screen of a display of the full area that you're looking at. So yeah, I do think that we… I'm definitely going to go comment where it ends, we'll see, but I'll go comment on it, see what happens.
**Grace Lim** 24:08 Nice. Alrighty, sounds good.
**Bryce Buchanan** 24:12 Cool. Yeah, I think… I think that's a very astute thing to point out.
Okay.
**nacho** 24:21 On what… sorry, on what the depth and notes, is related to?
Oh, yeah. Could you repeat?
Yeah, yeah, just to understand what depth and notes, covers… what means that for… for debut.
**Grace Lim** 24:44 Yeah, so
Okay, I did review the PR, but honestly, it's been a while. So yeah, so depths and notes, it is kind of like that, like, whether there are…
child components of the view, I think that is what the nodes is, and then for depth, like, if it is a child, like, how deep, like, is it nested? I think those are what, that's what it's describing.
**Billy Zhou** 25:07 Yeah, nodes is the count of total children, and then depth is just the height of the tree.
Up to you.
**nacho** 25:17 Okay, and can that be, got… can you recover that in SwiftUI, for example?
Yeah, just couriers.
**Grace Lim** 25:28 Oh, no, so actually, the reason why I brought this here was… I wanted to ask that question here as well, because I'm not a Swift developer per se, so that was also one thing I wanted to run by, to see if this… there was, like, an equivalent of this in the iOS world.
**nacho** 25:47 I… for UI kit, I think you can navigate for your parents.
And all your depth, but I don't think you can do that with Sweet UI, for example.
**Grace Lim** 25:57 I see.
**nacho** 25:59 I have not researched a lot here, but…
**Bryce Buchanan** 26:04 Yeah.
I… I think you might be able to…
to get at that if you just count, like, pushes and pops, but I don't know how accurate that would be.
And I'm not sure if nodes…
I'm not sure how you would calculate nodes.
I don't think that would be available.
**Grace Lim** 26:25 Or also UIKit, or just SwiftUI?
**Bryce Buchanan** 26:28 Just, just in general, yeah, just for… I see. Yeah, on, on,
On iOS. Maybe there's… it's just not… it's not anything that I've ever considered before, so I'm not sure.
**nacho** 26:39 Yeah. If there is a.
**Bryce Buchanan** 26:40 way to actually do that.
**nacho** 26:42 Yoikit Hassa.
parent-child relationships, so you can navigate that tree, that's possible, but Trip UI, I don't think…
you can do that, because it's… all the UI is implicitly set.
And you cannot.
You have… you don't have much control over that, or you don't have much control over getting that information at that one time.
**Grace Lim** 27:09 I see. Okay, yeah, so definitely not a required field if we do add it, but it might still be nice to have, yeah. Okay.
**Bryce Buchanan** 27:17 Cool.
**Grace Lim** 27:18 Nice. Okay. Are we good to move on from screen, though?
**Bryce Buchanan** 27:22 Yep.
**Grace Lim** 27:23 Nice. Okay, next is App Launch. This one, I think, is less complex. So, for the upstream Android one, they, like, the only…
specific attribute for the app launches is just, like, the start type. So, for Android applications, they do have the concept of, like, a cold, warm, hot
launched, but I think, for iOS, it seems like it's just cold and warm, at least that's what I perceived from the docs. So this is…
what I wanted to propose as the app launcher attribute.
Yeah, I didn't… I didn't think there'd be much concerns here, but yeah, let me pause for questions.
**alexcohen** 28:04 Is there any reason why it doesn't start with app?
Why it didn't start.
the.
**Grace Lim** 28:12 That's a fair point. No, that's a fair point. I was only looking at what we were currently using, but given the convention of app.star, we could do…
Not that, I like that. Okay, nice.
**alexcohen** 28:25 I mean, I don't know if… I don't know if that's the right thing to do. It seems like app is used in some places, application is used in others, and.
**Grace Lim** 28:31 Dude.
**alexcohen** 28:32 used as well. So, like, everything's gonna be in an app at some point. Absolutely. There's a way for it to not be in an app, I think.
**Grace Lim** 28:40 Beautiful.
**alexcohen** 28:43 So it's just really a question, I don't think it…
I guess it matters some way, I don't know.
**Grace Lim** 28:47 Because I think, like, within the context of this
span. Maybe this would become redundant, because we know it's for an app launch, but in the case, it's not.
specific, then maybe we do want to add it. So yeah, I think this will probably depend on the span definition as well, but yeah, thank you for pointing that out. I think it's a good call.
**alexcohen** 29:07 Okay, cool.
**Grace Lim** 29:10 Nice, okay.
Thank you.
Want to… oh, yes, alright.
**Ariel Demarco** 29:15 No, one… just one thing. On iOS, it's just cold and warm, and also a difference is the… if it's pre-warmed or not. So, a warm lunch could be also pre-warmed.
**Grace Lim** 29:27 That's a good point.
**Billy Zhou** 29:29 Yeah, there's… yeah.
**Grace Lim** 29:41 I… are there any concerns with the dash? Else, I will… Just keep it.
**Bryce Buchanan** 29:49 I don't think that's a problem.
**Grace Lim** 29:51 Okay.
Alrighty, are we good to move on from, launches?
**Bryce Buchanan** 29:55 Sir?
**Grace Lim** 29:56 Nice. And then lastly, for app attributes specifically, I don't think…
this will, like, go into specific… will be specific just to a singular event or span, but for this one, I don't… I didn't see…
the Samantha convention, like, describing or defining a version for app?
yet, so I wanted to add app.version. I think, like, on our end, we're kind of using application.version, but seeing how everything's using app. I was thinking we can just shorten it.
**Martin Holman** 30:29 Wouldn't you just use the service.version, or whatever it is, semantic convention that has version?
**Grace Lim** 30:35 Oh, which one, which one is that?
**Martin Holman** 30:37 Is it like.
**Bryce Buchanan** 30:39 I think it's service.version, is the kind of… I know it's… it's annoying because it's a service and not an app, but I think that's just what… what have… what has been…
**Martin Holman** 30:50 It's like service.name and service.vue.
**Bryce Buchanan** 30:51 Yeah, service version, service namespace, yeah.
**Grace Lim** 30:55 Oh, I see.
**Bryce Buchanan** 30:57 Yeah, that's kind of been the convention that's been used.
**Grace Lim** 31:03 Okay, so… The suggestion is to use service.version instead of app.version.
**Bryce Buchanan** 31:11 Yeah, yeah.
**Grace Lim** 31:13 I see.
I see.
**Martin Holman** 31:24 Like, common between every single…
**Grace Lim** 31:27 implementation across everything.
**Bryce Buchanan** 31:30 Yeah, yeah.
**Grace Lim** 31:30 Gotcha, gotcha, gotcha. Okay, so this one is obsolete then. Nice. Okay, one… one less thing for me to do. Okay, yeah, I didn't… I wasn't aware that we could reuse this then. Okay, this makes a lot of sense. Alrighty, so…
I will be going to Kleinsek with this as well to see what they say over there, and then probably, or hopefully next week, I can also…
Kind of flesh out the span definitions for these, then?
Alrighty, that was all from my end, yeah. If there's no any questions, I'll hand it back. Nice, thank you.
**Arri Blais** 32:02 So I have… I've attended several of the,
browser sigs specifically, and they're also working on something similar, so I don't know if you've talked with them, but it might be good to just sort of, like.
work with that, because they're working on something like page load and stuff, Might have some overlap.
**Grace Lim** 32:23 Gotcha, yeah. I… only know…
like, one client in Android Sig is, but yeah, let me dig that up, and then I'll also join them to see if they have any input. Thank you.
**Bryce Buchanan** 32:39 Awesome.
Alright, so I think that covers everything on our, agenda.
Let me just pop back here, make sure there's nothing else. Yep, that's it. I just wanted to do a quick review of some open issues.
Okay.
So, one thing that happened when we upgraded to the actual stable metrics is that we lost…
This, like, workaround of the raw metrics, where it just allows you to create a metric directly
Into, like, the metric store, rather than having to, like.
you know, add a counter, and then slowly add values to it. You could just create a whole histogram all at once.
And this helped a lot with, like, the app launch metrics for iOS, because they just give you a report in histogram format of a daily usage.
And, I'm not sure if there's a way to do this in, the stable metrics.
But, I would hope that there is, but I just haven't explored it.
So, that's something that… that needs to get looked at. I haven't had a chance to do that.
And I'm gonna be on a PTO all next week, so it's gonna be a while before I can actually really investigate this.
If anybody's interested in taking a look and seeing if that's possible.
And it also is a… it's a big… eventually, I'll have to get to that, because the Elastic agent, iOS agent, depends on that as well for the app launch metrics, so I'm gonna have to solve that problem one way or another.
Let's go to…
**Vinod Vydier** 34:30 So, so…
**Bryce Buchanan** 34:31 and pick them.
**Vinod Vydier** 34:32 So, we do have support for histogram in the Erx 2.0, right?
**Bryce Buchanan** 34:36 Yeah, we do. And the solution might just be that we have to create the histogram and then load it with the data, like, through a loop, which is fine.
But,
I think that the problem we had with the old implementation is that it wasn't really feasible to do that.
And so we created those raw,
Those raw, metric interfaces.
**Vinod Vydier** 35:10 Okay.
**Bryce Buchanan** 35:12 Okay, let's see here. So, we have a, new issue, says that the agent is causing, or the SDK is causing…
Crashes in test flight builds due to a, watchdog timeout, that's interesting.
It looks like…
Alex has already asked them.
If they could share a little bit more details there, we'll look forward to that. Crash and OS logs.
I'm not exactly sure what's going on here.
Or the… it's just not very… descriptive issue.
I think we just need to follow up with a little bit more details. It might be that they're targeting an older version, and the OS log is causing problems, and they're wrapping it?
Or… Yeah, it's not entirely clear.
I'll just… I'll follow up and say… ask for more details.
Okay, supporting new attribute types.
Investigating whether it's possible and acceptable to extend the OTL Swift API and SDK With new attribute types,
Complex types.
So this looks like, a new… Some… some, additional attributes Interesting.
So maybe we can have a little homework, and we can all take a look at that and see what that's actually all about.
Prototype demonstrating the feasibility of adding new attribute types.
**Ariel Demarco** 37:34 And remember that, those extended attributes type?
I went to the… I think it was in the logset that they were talking about it. It's basically whenever you have, like.
super big, chunks of data that you want to send, let's say slack traces or stuff like that.
That the way attributes work today.
It was not scalable for those kind of things.
And that's where Complex Attributes was born.
**Bryce Buchanan** 38:05 Oh, okay.
I was too lazy to implement bytes.
Cool, well, yeah, I'll take a look at that and, give my feedback. If anybody else wants to take a look and, respond as well, that would be very helpful.
**Ariel Demarco** 38:27 Sure, I will.
**Bryce Buchanan** 38:28 Thanks, Arianne.
User defaults cannot be saved. We've… this has popped up a couple of times.
And it… and it seems to have to do with… the,
Alamo Fire SDK, or at least our instrumentation of it. It's very, very odd.
Nacho, do you remember seeing this before?
**nacho** 39:05 Nope.
**Bryce Buchanan** 39:06 No.
**nacho** 39:07 I don't… I cannot see that.
relation with you for Defos.
**Bryce Buchanan** 39:17 Say again?
**nacho** 39:18 That I cannot see why that is… Making user defaults fail.
**Bryce Buchanan** 39:25 Yeah, and it's weird, too, because we depend on user defaults in a lot of different places.
So it's, yeah, it's quite bizarre. That this would happen.
So, with this code, user default set test test for key will only take effect in the current startup.
And we'll be restored next time, but…
It didn't reproduce in the demo. Can you provide a switch to turn off?
this logic, so that you do not monitor a, Alamo Fire network.
I think that is possible, right? Does our… does our, our… we can,
We provide a list of things to not instrument, right?
**nacho** 40:21 Yeah. Is that part? Yeah.
Yeah, we, we… That's what we do there.
That… but why that is related with the user defaults not working is what I don't catch.
**Bryce Buchanan** 40:36 Yeah.
**nacho** 40:37 That, that, that's really weird.
**Bryce Buchanan** 40:40 I swear… I swear I've seen this ticket before.
**Ariel Demarco** 40:46 I remember there was a problem in a beta, I think it was last year, on Xcode.
16, I think.
that there was a problem when… with persisting user defaults. I remember… I think I answered that with the actual
It was today from my boss.
But I don't remember… If it was sold or not.
**Bryce Buchanan** 41:27 Yeah.
That's curious.
Hmm… Well, I can't find… I couldn't find the issue that's… That I'm thinking of.
That's very bizarre. Okay.
Hmm, hmm… I'm not sure what to do with this one.
T-Martin was.
**nacho** 42:00 So… The fix is that…
**Bryce Buchanan** 42:05 They want to disable instrumentation for Alamo Fire.
**nacho** 42:09 Yeah, or he has another… has a fixed task.
**Bryce Buchanan** 42:13 more of this.
**nacho** 42:14 event.
Or that one.
**Ariel Demarco** 42:18 I think I would ask, the producing a project, or a way to represent.
**Bryce Buchanan** 42:23 Yeah.
**Ariel Demarco** 42:24 I got an 8-bed?
Ehh.
**nacho** 42:26 That's why he says that he cannot reproduce in the demo.
When I first missed message.
**Bryce Buchanan** 42:32 Yeah.
**Ariel Demarco** 42:33 Because I see no relation between, like.
**Bryce Buchanan** 42:36 Hang on.
**Ariel Demarco** 42:37 entering, the resume method from Adamo Fire.
and user defaults not working and persisting. They are, like, totally different things.
**nacho** 42:48 Yeah, the only thing is that… Maybe he has some…
Like, distributed user defaults, so he's catching the user defaults and saving.
in the network somehow. Maybe in… In the cloud, somehow?
Some… data solution, so he has that Connected somehow?
You know what I mean?
Instead of keeping the user defaults in your system, you also keep a copy in, in,
Yeah, we know, we neighbourne.
Yeah.
for example, in iCloud. And then he uses I'll am a fire to… To keep that synchronization?
That's the only explanation I can find.
**Ariel Demarco** 43:49 But the thing is, we end up calling the AF
resume method. So, independently of what happens.
Inside that method, that should still happen.
Like… That's… that's why I don't understand what's the relationship between amplifier and use of defaults.
not being…
**nacho** 44:08 Yeah, yeah.
**Bryce Buchanan** 44:23 Yeah.
Pretty bizarre.
Okay.
Issues are here.
Okay, so, issues with stable meter provider, initializer…
Oh, this is closed. Am I still enclosed? That's fine.
Okay.
User defaults can't be saved.
Aggregated asset download task does not support current request property.
Yes.
Fix for this and merged into main… oh, you did that yesterday, okay.
Awesome, alright, cool. So that's already fixed.
Instructions for getting started.
Yes.
Inaccurate.
And then we have… NeoHack here.
And they just haven't responded. I guess that covers all of them.
I wouldn't have thought that the getting started instructions would have changed very much.
since… It ought to be… You know, they… they should be getting the,
OTEL Swift Core just through using, Our SDK.
That's Cocopods there.
But maybe we can, just review this and make sure that I'm still…
Still is accurate. Does anybody want to take a look at that?
Banad, I nominate you.
**Vinod Vydier** 46:31 Sure, sure, yeah, I can look into that.
**Bryce Buchanan** 46:33 Thanks, buddy.
**Vinod Vydier** 46:36 Great.
**Bryce Buchanan** 46:43 Alright.
I think that covers just about everything. Are there any other topics anybody wants to discuss?
Oh, I did want to talk about this. What are we to do about all these dependency updates? Should we just merge them if they're good, or do we need to look a little bit more closely at them?
Like, there's, like, a couple like this one that… Seems to not be cooperating.
I don't know if Nacho or Ari, if you have any strong feelings about these.
**nacho** 47:15 Yeah, I… They're extremely noisy.
Yeah.
And the Slack channel is full of this, and my inbox also.
**Bryce Buchanan** 47:27 M.
**nacho** 47:27 The truth is that some of them makes a lot of sense to update.
some others should be taken with care, because I… if I remember correctly, it wanted to update some of our libraries that will make
us not being able to release to older versions of iOS or macOS?
**Bryce Buchanan** 47:45 Right, yeah.
**nacho** 47:46 They are a bit noisy. I don't know if we should…
just… I don't know if we can silence them somehow and keep them somewhere, so from time to time, we can take a look and update to the latest, as if there is… if there were something like that, it would be great.
And those that we don't want, if we close the PR, it won't auto-generate more.
But maybe we are… We are losing some, security… real security issues.
**Bryce Buchanan** 48:17 Yeah, yeah.
**nacho** 48:18 It's difficult.
**Bryce Buchanan** 48:19 a look at a couple of these, and if they look okay, I'll approve them and merge them, but…
**Ariel Demarco** 48:28 Yeah, I think… Yeah, for most…
**nacho** 48:30 No.
**Bryce Buchanan** 48:31 Like, this one's fine, like, this is just a script thing.
That's not a big deal.
**Ariel Demarco** 48:40 Yeah, I think that most of… most of them, like, don't really matter, because most of them are from GitHub Actions that are updated, and as they are using.
**Bryce Buchanan** 48:49 Oh, that song I just did.
**Ariel Demarco** 48:50 Amid Hatsha.
**Bryce Buchanan** 48:52 That gets updated.
**Ariel Demarco** 48:54 constantly. So, if CI doesn't fail.
I would just merge them, approve them, merge them in most cases. I think that when Nacho mentioned, it's important, like, whenever there are Swift package dependencies, I would take care.
Not only if everything works fine, but also if it makes sense.
**Bryce Buchanan** 49:23 Cool. Yeah, I think that's reasonable.
Alright, I'll at least go through and merge all of the, GitHub Action ones.
And maybe a couple of the… of the…
I'll pull down, like, a couple of the Swift…
Dependency ones, and just verify that everything's looking good, and then merge them, if they're… if they're alright.
**nacho** 49:53 Yeah, my main concern with those libraries is version support.
**Bryce Buchanan** 49:58 Yeah, I'.
**nacho** 49:59 We don't have… Old, targets?
For building, I don't think we have them. Maybe we should… It should be.
**Bryce Buchanan** 50:10 We should get hairs in the… in the…
build pipeline, though, if we're targeting
deployment targets that are below what our dependencies allow, right?
**nacho** 50:23 Do we have the oldest possible target deployment in GitHub?
**Bryce Buchanan** 50:30 I'm pretty sure we do.
Let me take a look. Where is our package? There it is.
So I've got 9… Version 13, yeah?
**nacho** 50:44 Yeah, but yeah, what Amen is?
if one… I'll use… You mean that if…
We link a package that is new, where it will fail.
**Bryce Buchanan** 50:57 Yeah, I believe it will, if we… if we have a dependency that is targeting a platform above what we're targeting.
like,
Let's see. I don't.
**nacho** 51:14 Yeah, it could be.
**Bryce Buchanan** 51:18 like, what was it? Were we looking at, was it gRPC Swift that, went to 2.0.
Like, if we… if we flip that, it'll… it'll complain about our target, I believe.
Or maybe it… maybe it'll complain about our Swift version, actually, because that's using Swift 6, isn't it?
Wow.
I'm not sure… I'd have to look through it to find one to actually…
I guess we could do, like, a… a Swift Core, like, bumper.
**nacho** 51:50 Yeah.
**Bryce Buchanan** 51:50 do a test, bump the… bump the platform version on SwiftCore and see if it complained in Swift.
But I'm pretty sure that's… that'll… that'll not allow it.
**nacho** 52:05 Okay, yeah, yeah, then we can link.
You can.
run everything.
**Bryce Buchanan** 52:14 Okay, alright. Well, I'll take a little… I'll spend a little time on that today. All right.
If there's no other… no other topics that we want to discuss, I guess we can call it here.
Alright, have a good rest of your week and weekend.
**nacho** 52:33 Okay, guys, see ya.
