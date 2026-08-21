SIG: Swift SIG
Date: 2026-08-20
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

Alolita Sharma (Apple Inc.) 00:01:46 Oh, hi, Si. Hi, Vlad.
Good.
Good morning. How are you?
Nacho Bonafonte 00:01:52 Good afternoon.
Alolita Sharma (Apple Inc.) 00:01:53 Hi Nacho, how are you?
Nacho Bonafonte 00:02:30 Now let's keep several minutes more.
Yeah. Seize more people when I get them. Yeah.
I know Bryce is missing today.
Alolita Sharma (Apple Inc.) 00:02:44 Yeah, is he on, is he out on vacation?
Nacho Bonafonte 00:04:02 Yes, as Alolita said in the chat, if you have any topic you want to handle today, apart from the usual PR reviews, or issues reviews that we will handle later.
We will start with those topics.
So I, I think we, we might.
Maybe a third now?
Yeah, sounds good.
Alolita Sharma (Apple Inc.) 00:04:26 Austin. Yeah.
Nacho Bonafonte 00:04:27 So… I'm sharing the… Documented, you can't see it.
Yep.
So… yeah, probably, from… From last week, some of the topics we had were some reviews and some PRs that had to be reviewed, approved, and merged.
The truth is that this week has been… there have been lots of comments and lots of PRs, thanks, thanks to everyone who has, helped with it. Some of the… them, include… Improving a lot of the URL session instrumentation, so thanks for that.
I have tried to review most of them, and some of them have already been merged, and… And, lives under review.
Yeah, apart from that, remember that we… are gonna… release a final version compatible with CocoaPods, would probably be end of August, beginning of September.
that will be the last official version, except if there are some issues with that. After that, we… We'll merge the core repository again into the main library, because maintenance of having two repositories is horrible, as we have talked in the past.
And it only has brought much more work to the… to the… To the Sikh?
So we are putting that back, and our plan is to just copy the files into core from main. So whenever we release a version, we will copy all the… API and SDK.
Files into the other repository, where people that only need that can still take that. But the development and everything Else must happen in the main repository, and that reduces the… a lot of the time.
And after that, we will also talk. Rally, that will be after Apple releases the new version of… all the systems.
So we'll probably reduce some of the minimum supported versions that we are… have now in the library.
Also publicly saying what we want to cut, just in case anyone wants to.
Or needs support for some old versions because of contracts or whatever they have with third parties.
So, yeah, that's the… Those are the… The reviews from last week.
For these weak topics, who added the ECU cleanup, who…
Vishwan aranha 00:07:24 I did add this issue cleanup. I think we briefly touched on it last week as well, like, I was wondering, like, if we can clean up some of the issues that are not valid anymore. I see some issues from 2 to 3 years ago, so I was wondering, like, if we can go through them.
And cleaned it up.
Nacho Bonafonte 00:07:41 Okay, we can, we can… We can add some of the time at the end, when we review issues on NPR, and add some of the old, issues, and start removing them. Yeah, some of them definitely are moved.
Early updated, yeah. Yeah, that's a good idea.
Vishwan aranha 00:08:02 Sounds good. Thank you.
Nacho Bonafonte 00:08:07 Okay, the second topic, the Swift Observability APIs integration.
Vladimir Kukushkin (Apple Inc.) 00:08:13 Yeah, this is mine, hi. Again, Vladimir from Apple, for those who haven't, Met me a couple of months ago.
There's… Si and Azeem from, promato as well.
regarding systems with APIs.
I don't know… Alolita, did you have a chance to share the doc, with Nacho or others?
Alolita Sharma (Apple Inc.) 00:08:40 Actually, Vlad, I just discussed it, but I… please feel free to share.
Vladimir Kukushkin (Apple Inc.) 00:08:57 Don't… I do the piece for a moment, I tried to… Attach the dock.
Espito.
Nacho Bonafonte 00:09:08 Do you want to share screen?
Alolita Sharma (Apple Inc.) 00:09:10 Do you want to just share it on the screen? Might be easier.
Vladimir Kukushkin (Apple Inc.) 00:09:13 share it on the screen, and I just…
Alolita Sharma (Apple Inc.) 00:09:14 Thank you.
I'll edit.
Vladimir Kukushkin (Apple Inc.) 00:09:16 I'll, I'll both, do both.
Alolita Sharma (Apple Inc.) 00:09:20 Okay, I'll let I can help, Ed.
Vladimir Kukushkin (Apple Inc.) 00:09:23 I'm sorry, that's good.
So people can also download the doc. Yes. Right, can you see what I'm sharing?
Vinod?
Alolita Sharma (Apple Inc.) 00:09:38 Yes, we can see it. Yeah.
Vladimir Kukushkin (Apple Inc.) 00:09:40 Perfect, perfect. Yeah, so, I don't know how much you remember from the last time.
But not everyone also attended at the time when we, Okay.
So, we… the context.
We are moving several Swift Observability API packages that, originally created in this solver world. SwiftLog, Swift metrics, Swift Distributed Tracing.
We are moving them to Swift Plank.
And we want them to be the language-level obstructions.
As a result of that, we want Swift… OpenTelemetry Swift SDK to play nice.
And basically support them, as the… first-class feature of the SDK not be on the… on the side.
So we came to discuss what… what are the… what are the current challenges, open challenges with ZK sees? How can we help as the maintainers of the visibility API packages, and what can we do about that?
So… We created a kind of pitch of, how we… Not propose or recommend, but… where… the way forward for the OpenTech, where we can offer help from the observability API side as well, to maintain compatibility, things like that.
So… The main idea, again, to make API packages a first-class support… feature supported by the SDK. I've noticed recently, changes since last time the distributed tracing support has been merged.
That's, create achievement, and progress.
So… Conceptually, we are covered with all the observability packages.
the main… This is a doc, right?
So, again, I didn't quite catch… Alolita, did you share the doc beforehand?
Alolita Sharma (Apple Inc.) 00:11:52 No, I did not. I did not.
Vladimir Kukushkin (Apple Inc.) 00:11:55 You did not? Okay.
So that'll be…
Alolita Sharma (Apple Inc.) 00:11:57 I think Vlad, you can step through it, that would be…
Vladimir Kukushkin (Apple Inc.) 00:12:01 Okay, yeah, that's what I'm asking. Yeah, so, the current state of the SDK as it basically couples together the Swift part and the iOS and Darwin Platforms instrumentation in general together.
If we want the SDK to support all the platforms Swift supports.
This is a much broader context than just iOS instrumentation. So, ideally, it should have a version that supports all the platform's Swift support.
and an iOS instrumentation and Darwin-specific functionality to the site.
So we want to discuss this, if maintainers, willing to look into that direction, separating Swift and IRAS.
Nacho Bonafonte 00:12:57 Yeah, we currently have support for Linux, for example, also.
Yeah.
But we have noticed support for some of the Apple server technologies.
Or instrumentation for some other things, yeah. But, but we have, sort of, multi-platform support currently.
there are some limitations for Linux, especially for we set the, the active context, how the active context is used is something that's limited in Vinux.
Because there is no support for, the OS activity.
That you've used on Apple platforms, but… Yeah, they can still… use Linux, and that is, tested also in the… And just have that runs everything and validates that it builds and runs in Linux.
Vladimir Kukushkin (Apple Inc.) 00:13:50 Right. Do you know if Opportunity Swift SDK has any users outside of Apple platforms and Linux?
Nacho Bonafonte 00:14:02 we… I mean, the Linux portal came from a user, so I can expect that they are using… the user who promoted that code, probably that they are using it, but no, we don't have… People doesn't come and say, we are using you.
That's not how it works. People just take the project and use it. We don't… we only know about the people that Say about it.
For example, Apple, I know it uses for the, private computing thing. It uses our metrics of OpenTelemetry shift.
for some reports, because checking the headers of the public code that Apple published had that.
But we had had no, no official word about that usage. So, yeah, the same happens with other companies. There are other Companies that are using it, but we don't know exactly where.
If we knew that, it would be great, because we could reduce many of the minimum OS versions that we are supporting.
And we could probably simplify some code, but yeah, we, we just… released, to people, and if people have problems, as for that.
Yeah, that's… we don't have a register for… of that, yeah.
Vladimir Kukushkin (Apple Inc.) 00:15:18 Right, yeah.
Yeah, then…
Vinod Vydier 00:15:21 We've had… we've had a few issues on Linux that people have opened, and but it's, yeah, mostly, I don't think… Yeah, Linux is… The server side has not been, you know.
Well, we don't have too many users opening issues on that.
Nacho Bonafonte 00:15:38 Yeah, it's true that we've had some issues in the past. We don't know if they are still actively using, but yeah.
That's true.
Vladimir Kukushkin (Apple Inc.) 00:15:45 Right, right. But you haven't heard anything about Windows, or… other platforms.
Nacho Bonafonte 00:15:51 No Windows. Probably no one is using Windows currently, because it will need another another branch, or if they… someone is using it, definitely they don't have… upstream their changes, to the library, but probably, probably, I would say probably not.
Vladimir Kukushkin (Apple Inc.) 00:16:11 Yeah, okay. Yeah, this… this would be definitely… a large topic, if we want OpenCylenter Swift SDK to support all platforms Swift supports.
Obviously, instrumentation is platform-specific in many situations, but in such situations.
in some situations, instrumentation through switched observability APIs could also be cross-platform, and this is one of the, big reasons to support those subsidiary TPS, because people are already using those packages. So, for those who haven't had the chance to use API packages, they are thin API layers. They don't provide any implementation that actually exports box metrics or traces.
the API package you use to instrument your libraries or applications, and then an application is free to install the backend, they seem appropriate. It could be multiple backends, could be OpenTelemetry file.
Console, any other things.
And right now, there are basically two options for the OpenTelemetry. One is the OpenTelemetry Swift SDK, There is another package, Swift Hotel that provides, API backends for the hotel, based on the official OpenTelemetry.
Interfaces, yeah.
Nacho Bonafonte 00:17:41 I don't think that's exact. I mean, that's more of a OTLP.
Proper on Swift?
Because it doesn't follow the API and the SDK. That's part what… of what happened telemetry is.
Pentarimeter is not just OTLP. It's not just a protocol and a collector.
I must say, sorry, but that's not… Open telemetry.
OpenTelemet is a set of APIs, SDKs, and The way they… Are constructed, and the way they communicate.
That's what we are doing with Open Director Street.
Sorry.
Vladimir Kukushkin (Apple Inc.) 00:18:18 Yes. Yes, yes.
Nacho Bonafonte 00:18:20 everything, I mean, you can say OpenTelemetry compatible.
Because you support OTLP, but it's not open telemetry.
Alolita Sharma (Apple Inc.) 00:18:27 Yes.
Nacho Bonafonte 00:18:27 Trimity must have…
Alolita Sharma (Apple Inc.) 00:18:29 That's good.
Nacho Bonafonte 00:18:29 The correct separation of the libraries, the correct responsibilities for the objects, and the names, and the methods, they can be a bit Change for each language?
That's valid, that's valid on the project, but… Pen telemetry is all about the… API calls.
The way things work, similar, or almost the same way in all the platforms.
Vladimir Kukushkin (Apple Inc.) 00:18:59 Yeah, I… I correct myself, yes, OTLP, not the, open telemetry in JL. Yes, yes, that's… absolutely fair.
Then the big part of the open Zoom space SDK, sample platforms, automatic instrumentation, URL session.
And the thing is, this support is, on the path to being… phased out, as Apple SDKs and moving out, moving from Objective-C to Swift.
And if observability APIs become the language labels, We can expect for example, open source packages, the networking stack developed in the open source, to support those APIs for instrumentation.
So, it would also be beneficial for the OpenSignature SDK to fully support those APIs.
And this is… we are not inventing anything here specific for Swift. Rust OpenTelemetry SDK, operates in the same way. There is a thin layer of API packages facing, tracing logs.
the main ones, everyone is instrumenting their applications and libraries as tracing crate.
And then the, breach.
packages reach crates to Bonsai imagery or something else. This is a decision that could be made later, so we… Wait, do we propose to follow that pause?
There is another example separating platform and language with the OpenTelement for Java, OpenTelement for Android.
This is also what we think OpenTeometry Swift should follow, because, again, Swift is… The language is larger than just the iOS.
Or alias and macros.
Yeah, potency and long-term risks, I've touched that.
Swift, again, is working on the first-level HTTP APIs.
Yeah. So, Basically, what we'd like to align on, if this is a direction that the maintainers also like to follow.
support the bridges.
So the, for example, pull requests, We open, I open, my colleagues open.
that would improve the support for the API packages would be something maintainers desire to invest… have… plan to invest time into reviewing, working on that.
that part, that we can, on the… on the opposite side, we can eventually, when packages… packages start using observability APIs, we can help with adoption.
those?
The goal… is… if an application or a library is instrumented with the observability APIs, plugging OpenTeameter Swift SDK should be as simple as just wiring the internals.
of the observability… Swift Observability stack.
a visual picture, I myself think this is a very good picture, and it also correlates with what we discussed 5 minutes ago with the APIs. So, we see there are three pillars of the instrumentation around OpenTelemetry and OLTEL.
You can have Swift Visibility APIs as the entry point for instrumentation. You can have OpenTelemetry SDK APIs as the instrumentation. Those are working side by side. No one is forced to use one or another, both first class.
And the old instrumentation.
is on the side. It could be using any of those APIs, it could be inside OpenTelemetry SDK, this is, irrelevant to the API, pretty much.
So this is the ultimate goal picture that we wish to see around Swift availability and all the telemetry.
That, there's… Yeah, this is the API I was talking about.
This is the example of using the observability APIs, some details, again, if you haven't seen how it works, we have logger, we have metrics object, objects, we have the… spam APIs and distributor tracing.
It's very… it's very small.
surface of API, comparing to the OpenTelemetry SDK APIs, and that's the goal of it. So we provide a very thin layer of APIs that anyone using Swift language can use.
Obviously, it's a subset of all the features of the telemetry.
And if someone doesn't need that, they can use Swift APIs and live happily.
plug OpenTelemetry SDK happily.
Yeah, so… This is the continuation of the story, what we propose. We don't propose to… rewrite SDK or anything, or say that the availability APIs should be the only APIs. No, they live side by side.
Yeah, and the practical things, time has passed since we wrote this speech and started discussing this with Alolita, so distributed tracing is now supported.
I personally haven't had the chance to check that out. I will do.
Yeah, so, bridges support… We eventually help.
adopting the APIs, and also Swift Lang.
As the… as the language for this infrastructure can help with the platform we have, Switzlang has, groups of people who work with the language support on various platforms.
Excellent.
Community will be there.
as well.
So… I guess if Alolita hasn't shared this doc beforehand.
I've shared it in the chat.
So, anyone can download it. I don't know what would be… The best way to share it with people who haven't attended today's meeting.
Alolita Sharma (Apple Inc.) 00:25:49 Vlada, we can add it to an issue. I can add it.
Vladimir Kukushkin (Apple Inc.) 00:25:52 Great, great, thank you, thank you very much. So… We are not seeking the answer today, right now.
That probably would require some… discussion, and… among the maintainers, we're happy to join, next SIG meeting to discuss this in details.
Or if you have any questions, but please… Take a look at this doc, read it.
And what we need is if you agree with the general direction, so whatever contributions we make.
Whatever issues we file, they are not, in… A position to what do you plan to do, basically.
Nacho Bonafonte 00:26:38 Okay, yeah, I can offer… I mean, basically.
or I'm missing something, or what you are offering is helping with the breaches that we have with the observability libraries from Apple?
So, that can work.
better with OpenTelemetry Strict, and use that instrumentation instead of the API and SDK directly.
If that's what you are offering, I can say that we are totally agree with that. I mean, we have the bridge to help users use their existing instrumentation.
As I said before, I mean, we still need to have API and SDK. We cannot give that in benefit of the Apple way of doing things, because it's not what open telemetry is about.
But if you… If your interest is helping with the breaches, then that's great. I mean, we are totally open to review your PIs, to… to… To merge those peers and to, you know, improve the reach as much as possible.
And yeah, that totally, totally agree with that. I mean, there is no discussion there, right? Everyone who wants to improve it It's totally open to do it, and we will, we will review, and we merge things, and we also try to, release versions when people is interested, because they have a bug fix, and we… I mean, we are quite dynamic there in the… Versioning, or releasing versions.
So I… Is there anything I'm missing from that? I mean…
Vladimir Kukushkin (Apple Inc.) 00:28:24 What, yeah, let, let, let me then ask,
Nacho Bonafonte 00:28:28 I mean, English is not my, you know, my mother, my mother language, so maybe I'm missing something, but I don't know what it could be. I mean, what… couldn't we agree with this document? That, that's the…
Vladimir Kukushkin (Apple Inc.) 00:28:45 That, that, that, that's very, that's very good to hear. What do you think about separating Swift and iOS parts.
Maybe moving, Moving either specific instrumentation to a different target, or a different package.
They… I mean, he's…
Nacho Bonafonte 00:29:07 They are in different packages already.
Alolita Sharma (Apple Inc.) 00:29:09 Yeah, I mean, they are pretty.
Vladimir Kukushkin (Apple Inc.) 00:29:10 All right.
Alolita Sharma (Apple Inc.) 00:29:10 Some packages.
Nacho Bonafonte 00:29:11 I mean.
Alolita Sharma (Apple Inc.) 00:29:11 The targets are all different.
Nacho Bonafonte 00:29:14 Yeah, if… yeah, it would be great if… if… if SPM just didn't download the… The dependencies of the targets that are not included.
Alolita Sharma (Apple Inc.) 00:29:25 Yeah.
Nacho Bonafonte 00:29:25 when you…
Alolita Sharma (Apple Inc.) 00:29:25 Because that has been a big issue.
Perfect.
Nacho Bonafonte 00:29:29 But yeah, we… actually, all the instrumentation and all the libraries, even API and SDK, are different targets. You can only link with some of them, you can only link with OTLP exporter.
HTTP, OTLP exporter, and… and… and some importer, like, there is no need. I mean, everything is in one project, and in fact, as I said at the beginning of this meeting.
we are gonna put… we did some separation in the past to move the SDK and API to another repository, but That's how… that has been a nightmare of maintenance, so we are moving again to the same project, same SPM for everything, but definitely in different targets. That doesn't change from what's now So, each target can't be independently updated, and yeah, and We could also, I mean, change some of the ownership of those… of some folder directories if Apple wants to update their bridges independently. For example, that will be… I mean, we will be okay with that.
If, you know… I don't know, but that… If that's the question. We are totally open to any improvement or help with maintenance. I know, for example, that logging has changed recently, and we have no force to update that.
We need, someone who helps with… with that. So, yeah, if it's Apple, it will be perfect, because you, you, you also know that.
Oh, the sauce.
from inside, so, yeah. So, I don't know if anything more, He's being asked here.
Alolita Sharma (Apple Inc.) 00:31:13 I think, I think, here, Vlad, as Nacho said, you know, again, it's… you know, again, the targets are built differently, so, I think there is no issue in separating out Swift from, you know, the other targets that are iOS or Mac OS or any other of the iPadOS and other builds. But, the key thing that he's calling out here is that in order to keep the bridges compatible, you know, with the baseline APIs that the language is, you know, maintaining.
it would be helpful to have Apple, you know, engineers, come and, you know, support them on the… to ensure that they are, you know, compatible. Whether that's even, you know, having a suite of tests that ensure compatibility as the APIs are, you know, evolving on the language layer.
But maintaining those bridges is additional, additional, work, right?
Nacho Bonafonte 00:32:23 Here.
And the other thing I read about removing Switzerland, yeah, I mean, I'm totally open. I mean, the thing is that there is no other way to get that information, right? Currently, Apple doesn't offer any other way to get that information.
From the networking APIs.
For the… at least for the use… clean site, or the phones, or from a Mac that's not a server, or not using Suite Neo, or something like that, that I don't even know if that's happening there, but… If we… We need to be able to… To dynamically do things there, and I… Or there is something new, or there is nothing like that in the Apple networking.
libraries that there are. So that's… I mean, totally… I mean, Switzerland is a problem itself, because it's really complex, it's very prone to errors, Apple change something, things get broken. Yeah, that's a maintainability problem, but at the same time, we need to dynamically do things. We must be able to dynamically intercept.
calls.
We cannot expect that the final user is gonna instrument their own code.
Right.
Currently, we are adding instrumentation to existing code.
compiling time, right? But we're adding that.
We are being able to have an application from a user that doesn't know anything about observability, that he cannot.
OpenTelemetry on top of it, and automatically has the observability information that That's a really powerful thing. People doesn't need to be observability experts for that. That's a key value that I think that this library offers, and that's probably why it's being used.
For observability more than other options, that of lies, I don't know if that's correct, but that forces you to add all the observability at, data.
Alolita Sharma (Apple Inc.) 00:34:38 Yeah.
Nacho Bonafonte 00:34:39 And that's something that currently only Swizzle, access. If the other libraries have some kind of callback, some, some kind of options that you can implement like that, like delegates. I mean, delegates is great, because if delegate can answer methods, you can You can just write your code there, but the thing is that In the newest libraries that… dynamicity, or that… way of… Getting inside is… it's time or difficult, so… If Apple provides that, it would be great, but expecting that the users will add all the observability information When they write their code.
It's a no-go, because especially the observability developers that work with this library and with many others are usually multi-platform.
Alolita Sharma (Apple Inc.) 00:35:34 People are saying.
Nacho Bonafonte 00:35:35 That works in many platforms, not… iOS experts, or Mac experts, or Swift experts. They are observability experts that the same time they write Java, they expect, that the Android library has the same methods exactly than iOS, because the same people is doing the same code.
And that's something that our users Have that.
You know, that, that, Property is that they are not expressing the platform, they are expressing observability and just that is on top.
And that's what we try to do, basically, and that's the people we try to help. I've been in the Apple platform for more than 25 years. I have no problems with that, but the problem is that that's not the people that use the library, usually. And that's a… And that knowledge of the API in all languages is what really makes OpenTelemetry being as standard possible, I think.
Vladimir Kukushkin (Apple Inc.) 00:36:40 Yeah, that's no, no, objections there.
What we try to, what we try to also support is users who I'm not experts in OpenTelemetry, or, And they are working just with Swift, maybe multiple platforms, but one language, one Swift language.
So they want instrumentation, And they want instrumentation to work.
was swift.
OpenTelemetry So, yeah, this is good.
Alolita Sharma (Apple Inc.) 00:37:12 I think that here, a larger question, you know, and this might be, you know, more future-facing, is that, as Swift language, you know, the language itself is multi-platform, like Linux is supported, or Windows, you know, is being called out. So, you know, as you are looking at multi-platform from a language point of view.
Do you see, you know, the, the, the, you know, objectives of the language in terms of supporting observability, data, you know, being exposed from the different layers, being… diverging from, Diverging for each plat… each, you know, platform that's supported?
Because that's exactly what, you know, Nacho's also highlighting, that when folks, you know, come in to… as a mobile developer, for example, to support and build out an Android, you know, implementation, as well as an iOS implementation, for example, they are expecting the same library, you know, and the same data being surfaced for metrics, or tracing, or… Or, logging, right? And that's why OTEL becomes very compelling, because it's standard, right? It's the same set of metrics, or same set of traces, tracing and logging that is expected as a baseline. So.
would you say that, you know, as Swift adds an observability API, which is very cool, it will maintain that compatibility across all the platforms, which are not.
Vladimir Kukushkin (Apple Inc.) 00:39:09 mess.
Alolita Sharma (Apple Inc.) 00:39:09 You know… Okay, so that's, that's pretty cool.
Vladimir Kukushkin (Apple Inc.) 00:39:12 At least that's the goal. Yeah, that's the goal. Of course, not every single piece of API is supported, can be supported on all the platforms, like Swift supports embedded.
Sure. So there might be some limitations. But the goal is, yes, to have language-level features, the same level as all Swift language users have, I don't know, a dictionary API, and they expect this dictionary API to be the same on all the platforms, so you can actually build cross-platform libraries. You can, with the Swift Observability APIs, you can instrument cross-plus of libraries, and expect them to work regardless of the backend, whether it's OpenTelemetry, or File, or whatever, or, for example.
Alolita Sharma (Apple Inc.) 00:39:54 I think that's really a great direction to go in, because it really gives the language a lot more power and flexibility to interoperate across different platforms.
And that's… that's again, you know, as observability engineers, typically you're looking at the observability, you know, data that you need from the platform, and for your app, right? And that's… that's what people are looking at when they're using OTEN, so both… both layers is, you know, great, because if somebody's working in Swift native and building out Linux.
Working on Linux.
Nacho Bonafonte 00:40:35 To be honest, we have not had any… Server user asking.
Alolita Sharma (Apple Inc.) 00:40:42 Yeah.
Nacho Bonafonte 00:40:43 telemetry Swift.
And the fact that proves that is that we Have no libraries, or have no code to read the headers from a trace.
We have no way to read the traces from a header to.
Alolita Sharma (Apple Inc.) 00:40:58 Yeah.
Nacho Bonafonte 00:40:59 Because no one ever has us for that. That's our reality.
Alolita Sharma (Apple Inc.) 00:41:04 I mean, there's not much use…
Nacho Bonafonte 00:41:06 Because they are using… maybe because they are using… maybe Swift metrics, right, instead of internal metric swift, I don't know. But the truth is that To our project, Never, ever… Anyone has asked for that, because if they had us, we would not have had them.
Alolita Sharma (Apple Inc.) 00:41:24 Yeah, yeah.
Nacho Bonafonte 00:41:25 all of our users are always client-side. Usually… Yes.
iOS, so, most of our users are phone-oriented, developers, or iPads.
But, yeah, iOS is our main platform.
That's the truth. We support.
Alolita Sharma (Apple Inc.) 00:41:44 Yeah, and I think, I think,
Nacho Bonafonte 00:41:47 And also, we have some watchOS, for example, users that use it. We have some desktop or Mac, macOS target, but always as client and never as service. That's our reality. So, yeah, I mean, we cannot support to anything that's needed.
At server side, we are not close to that, but… If we follow what people or users have asked, it's basically that.
Alolita Sharma (Apple Inc.) 00:42:16 I think, I think it's a good call-out, though, Nacho, because, lead, again, the point is that, you know, when you go into the cloud-native world, especially where you are running, Kubernetes clusters, for example, and, you know, much of the cloud is Kubernetes, at that point, you know, all the server-side services and applications is As well as application services, platform services, as well as, cluster-level, metrics, or… you know, are either Kubernetes native, or they are Go a lot, you know, some Java, some… you know, Rust, but it's not… never has it been Swift, right? So again, as you… as the language evolves in that direction, which is, I think, what you guys are, you know, kind of, working on.
That's great, because, I mean, I think that that support will get built out. But in the cloud-native world today, at least, you know, if you were to have a clear understanding of what are the core languages that are being used for the platform layer above on top of Kubernetes, for example, you know, they are different languages.
So I think that's the layer you are targeting, with the language, you know, it can take some time.
Nacho Bonafonte 00:43:46 But regarding this, I mean, as said, we are totally open to any.
Alolita Sharma (Apple Inc.) 00:43:50 Exactly.
Nacho Bonafonte 00:43:50 collaboration, help.
Alolita Sharma (Apple Inc.) 00:43:52 Yes.
Nacho Bonafonte 00:43:52 improvement to the libraries. So, if you can improve the bridges, so they… work, seamlessly with, with, with OpenDeremity Swift, and use our exporter, or, or use your exporter. I mean, that's not… I mean, we are totally open to have the best support for Apple, observability libraries to… for the native Swift observability libraries. Totally open. I mean, we want to have the best support possible, because We… maybe there are users that, you know, just want to mix.
things. They want to mix swift tracing with other metrics, or with other things that are… so, yeah, totally, I mean, we… we are very constructive.
we want to add everything possible, as easy as possible for users. That's our, our, our goal.
And whatever help it comes, it's great. And also, if you… apart from EUC, I mean, the OTLP spec that the Open Direct District currently has is probably outdated. If you want to help improving that because you need that for something new.
I mean, we are totally open to open a PR, or to… or even to add, you know.
keys of the code to people from Apple who is really willing to help the code and to bring it up. But we cannot, as said, I mean, we still need to have SDK, we need… still need to use the API, Because that's, you know, that's part of the project. I mean, the… even the API is reviewed by the committee, right? Alolita.
Alolita Sharma (Apple Inc.) 00:45:34 Yes.
Nacho Bonafonte 00:45:34 You're reviewing that. The name of the methods are what you want, or…
Alolita Sharma (Apple Inc.) 00:45:38 That's.
Nacho Bonafonte 00:45:39 what OpenTelemetry expects from the name of a method, right? So that's part of the… you can have some specifics, and we have some in Swift, but for the rest, yeah, that… That's a must of the project. We cannot… We cannot deviate much from there.
Alolita Sharma (Apple Inc.) 00:45:57 Yeah, and I think that to Nacho's point, Vlad, the, you know, wherever the spec needs to be brought up to date on, you know, to represent some of the changes that are coming in the observability, you know, APIs for Swift, the language itself.
Again, work with us, so that we can actually, you know, we can absolutely make those proposals and, you know, incorporate… get those, reviewed by the… spec…
Nacho Bonafonte 00:46:30 Yeah, and what's more, I mean, if you see that some importing is not efficient enough, because there is something in the library that's not efficient, or very old, or would need some improvement. We are… the same, I mean, we are totally open to anyone, in any area of the project to help.
yeah, probably there are some. The only thing is that that… I know it's not what usually Apple does.
we… Try to keep compatibility with many With a minimum version that's quite low. Because many of our users are not final.
developers, they are middleware.
That they have their observability library that they build on top of a 10mm street, for example, and they have contracts with other developers that Have contracts with government that still forces them to use This or that other version of the system, which… Sometimes it is difficult and limits a bit.
the minimum version that we have. But, for example, we are moving now to Swift 6.
0. And async, methods, for example, so we tried to iterate, but at the speed Enough that keeps our users happy, and that we are not creating problems for them.
To update. So probably there, we are a bit… More outdated, but that's because of that.
But that's something that we also plan to.
to… to improve a bit, probably move to iOS.
50, or so.
Alolita Sharma (Apple Inc.) 00:48:17 16.
Nacho Bonafonte 00:48:18 Something like that, as minimum.
Vladimir Kukushkin (Apple Inc.) 00:48:23 Right, then that's all from my side. Yeah, and again, I'm… Happy to hear that this aligns with what you want to see in the year.
Absolutely to Swift SDK, yeah.
Alolita Sharma (Apple Inc.) 00:48:36 Cool. So, I think, Nacho, what I would recommend is that, We, you know, have, some of the issues clearly, you know, kind of created, and I can help with that, in terms of the, bridges that need to be maintained, you know, for Swift, itself, and, and, you know, maintaining compatibility there. And kind of then Vlad, we can figure out, you know, how we can support That, because I think bootstrapping it was a good thing, then we have more community members who can actually maintain it, help maintain it, but I think you guys are the experts, so at the end of the day, you know, these bridges will be very important.
Nacho Bonafonte 00:49:20 Yeah, what…
Alolita Sharma (Apple Inc.) 00:49:21 Some of your input.
Nacho Bonafonte 00:49:22 Yeah, regarding the bridges and the Apple libraries, It's something that I don't know. When you have a target in a SPM, Can you have different minimum targets? I mean, for example, can you have, like, if you use a dependency on Swift, on Swift log, for example, that is iOS 18 or iOS 26, because it uses something very new.
Can you have that in the same SPM, that API and SDK that… Could have way lower minimum version, for example.
Would that work? Or is the minimum version… Said by… no, it will be by each target, right?
So we could still have, different… I mean, if you need… I mean, I know Apple, usually has very, you know, has support for… for newest… developments, usually.
Si Beaumont 00:50:28 I mean.
Nacho Bonafonte 00:50:28 But you can still link that, right?
Si Beaumont 00:50:31 The answer to your question is no, you can't take a dependency on something that raises your minimum platform versions, but the good news here is that these, Swift, wide.
observability libraries.
Don't state a minimum platform Version. Deliberately, so they are.
They can be a dependency of any project without impacting them.
So, for some of our more fundamental ecosystem-wide dependencies, like.
crypto libraries, observability libraries, we don't impose a minimum version on anyone that takes the dependency.
Nacho Bonafonte 00:51:06 Okay.
Vladimir Kukushkin (Apple Inc.) 00:51:08 It would mean in practice that some features might… some features for APIs might not be available, because they are marked with the ad available for newer platforms.
But the package itself, yes, doesn't, Enforce a new platform.
Nacho Bonafonte 00:51:23 But if, for example, you don't… depend on, on, on SWIFT metrics.
just by being in the SPM, does it force your minimum? No, right?
Even if you impose a minimum version of the… I mean, the thing is, I am thinking about maybe a user who uses Swift Metrics, on top of OpenTelemetry Swift, but Swift Metrics is very updated.
would that make a problem for the other users of the library? For that user, you know, they are using a library that has a minimum version that's very new.
So they don't have superfluid systems, but only links with that, right? Would that work?
Having that dependency…
Vladimir Kukushkin (Apple Inc.) 00:52:10 Yeah, so if… if OpenTelemetry Swift would… the upper limit version for the observability packages, and someone trying to use it, and also has dependency for the observability packages for the newer version goes beyond the CAP and the SDK. Yeah, that's gonna be a problem.
But usually for those API packages, it's recommended.
Not to have the cap?
Because we maintain the compatibility, if someone is willing to use the newer APIs, that's only available in the newer… platforms.
Then they would have, yes, an application, with a lower boundary or lower version of the API packages.
could be higher than the Open Sternature Swift SDK.
But…
Nacho Bonafonte 00:53:07 Yeah, we found that with the gRPC library, for example. Version 2 of gRPC had a minimum version that was much higher.
So we couldn't link with our, with… we… in fact, if you check our version of gRPC in the project, it's currently on version 1 still.
The latest one of one, but we didn't move to version 2 because it had incompatibilities.
If we move there.
with… With the… with the minimum version of the… of the, of the library itself.
Inc.
Vladimir Kukushkin (Apple Inc.) 00:53:43 Creativities.
Nacho Bonafonte 00:53:45 Yeah, because it uses… I think it was maybe Swip 6, or minimum iOS version, much higher than what we have. I don't remember exactly, but I know we didn't… that library to a newer one, because it killed… I mean, gRPC was a base base for most of our users in the library.
For… for the OTLP compatibility, so maybe that… That was a bit bigger, but if it's just an important target, maybe it's not such a problem.
But yeah, I don't… I don't know about… The specifics there.
Si Beaumont 00:54:27 I think it's something to probably consider.
in your evolution plan, like, gRPC Swift V1 is not getting any… it's end of life, it's not getting any support.
Sort of potentially going to hold you back.
So I think it's worth looking at what it would take to move to V2, and what impact that might have on your adopters, and thinking about what a… Migration strategy might look like for them.
And I think it… you're right to say, I think it does come with some… Raising the floor on some of the other requirements.
But I think that might be unavoidable, because I think gRPC Swift is… Not gonna go backwards.
on those.
Nacho Bonafonte 00:55:11 Yep.
Yeah, that's… that's the only, the only doubt that I have about Updated to the latest things everywhere.
Yeah, because dependencies in Swift VMs are a bit of a nightmare, even if you don't link with it.
Everything gets downloaded,
Si Beaumont 00:55:29 TwifPM hasn't…
Nacho Bonafonte 00:55:30 So, yeah.
Si Beaumont 00:55:30 a feature called Package Traits, which is a… Potential way out of this, where…
Nacho Bonafonte 00:55:37 Yeah, I think we investigated that. One of the maintainers investigated that, Ari, and he found that it was not a… that doesn't solve the problem of downloading everything, even if you don't link with it. Yeah.
Si Beaumont 00:55:54 That's great. It doesn't stop you cloning the dependency, but it will get you out of your… raising your minimum platform requirements for users that do not enable traits.
Nacho Bonafonte 00:56:06 Okay, that, that… Yeah, that could work, right? And the users, GIS will have to import that with a specific trade when they use the library.
Si Beaumont 00:56:18 That's right.
into the weeds a little bit with the details, so I'm happy to sort of, like, you know, park this one.
Alolita Sharma (Apple Inc.) 00:56:23 Yeah, but I think… I think, Si it doesn't, address the, you know, the issue that the middleware vendors, you know, have in terms of dependency, imports.
Right? Like, they're trying to maintain a very lean footprint on, you know, for supporting many of the Client-side implementations that they are providing, and…
Si Beaumont 00:56:53 I think… I think we sort of touched on this last time.
Alolita Sharma (Apple Inc.) 00:56:56 Yes, yes.
Si Beaumont 00:56:57 further discussion.
Alolita Sharma (Apple Inc.) 00:56:58 Yeah.
Si Beaumont 00:56:58 And that your primary audience appears to be… these iOS contractors who are potentially having to support quite dated toolchains for quite long periods of time.
Alolita Sharma (Apple Inc.) 00:57:10 And they're vendors, right? Observability vendors.
Si Beaumont 00:57:13 And,
Nacho Bonafonte 00:57:13 Yeah, I…
Si Beaumont 00:57:14 We just need to sort of work out how does that marry up with the Swift package ecosystem? The majority.
Alolita Sharma (Apple Inc.) 00:57:20 Yeah.
Si Beaumont 00:57:20 moves to a sort of last three Swift versions.
Alolita Sharma (Apple Inc.) 00:57:24 Yes.
Si Beaumont 00:57:25 model, and… I mean, it's come up with some story where…
Nacho Bonafonte 00:57:29 that we can.
Si Beaumont 00:57:29 evolve this together.
Alolita Sharma (Apple Inc.) 00:57:31 Yeah.
Nacho Bonafonte 00:57:32 Yeah, that's, yeah, I remember, for example, Embrace had a problem with that the last time we updated, because they… I still had contracts with… with companies that had to support… maybe it was iOS 11? Yeah, I know, I know it seems silly, right? But… It's.
Alolita Sharma (Apple Inc.) 00:57:51 You know?
Nacho Bonafonte 00:57:52 in my… yeah, in the product I work, we, we just support Three versions, yes, last three versions.
And we drop as soon as possible, because, you know, also support is a nightmare, the more you have, but…
Alolita Sharma (Apple Inc.) 00:58:10 But I think, I think this will also Because I think that, you know, as you go forward with the new devices, Apple is also recommending, you know, upgrades for,
Nacho Bonafonte 00:58:26 Yeah, but…
Alolita Sharma (Apple Inc.) 00:58:27 application.
Nacho Bonafonte 00:58:27 they don't have any users, right, in iOS 11, but they have a contract that say iOS 11.
Alolita Sharma (Apple Inc.) 00:58:33 It's supported, yes.
Agreed.
Nacho Bonafonte 00:58:36 And that's… that's the source of truth, right? If the contract says something, you know, you… you have to be… you are tied to that, even if no one uses that. And… and… That's a problem we face, but yeah, I totally agree. We should try to, to use the newest possible, but yeah,
Alolita Sharma (Apple Inc.) 00:58:54 Yep.
Nacho Bonafonte 00:58:55 Okay.
Alolita Sharma (Apple Inc.) 00:58:57 Okay, cool. So I think, Vlad, thank you again for stepping through the doc, and, you know, I'll make sure that it's available, as part of an issue, and we will circle back with creating some of the issues also, in terms of the support for the Swift language bridges, to maintain full compatibility.
And of course, you know, hopefully you guys can join more often.
at least try to do so, you know, it would be pretty awesome to have… have your knowledge and, you know, contributions on the project.
Sounds good.
Vladimir Kukushkin (Apple Inc.) 00:59:39 Thank you.
Alolita Sharma (Apple Inc.) 00:59:40 Thanks, thank you, thank you. Thank you, Nacho, and we'll, we'll circle back. I think we're at time.
So, thank you again.
Nacho Bonafonte 00:59:48 Yeah, we will continue, reviewing the… next week, we will review PRs and issues if, if time permits. Yeah.
YD Yasura Dodo 00:59:58 Last minute, like, I wanted to know, like, when we're gonna release a new version of the hotel suite.
Nacho Bonafonte 01:00:06 Yep.
YD Yasura Dodo 01:00:06 Because I fixed bags, and I wanted to, ship with my project.
Nacho Bonafonte 01:00:11 Yeah, I… our idea is releasing on the end of August, to sync with the latest support for, CocoaPots.
Okay. So, the idea is merge… Is this release in August trying to be the last one with CocoPot, so… Does it work for you? Would you need another earlier version? If you really need it, I can rush it and…
YD Yasura Dodo 01:00:40 It would be great if we can release a new version from the bug I fixed today, and so, like, I can, I can ship with my project, and yeah, like, it would be great, like, if you can release a new version from the master or main.
And I've finished.
Nacho Bonafonte 01:00:59 Okay, okay, does it include also OpenTelemetry Core, or just in… in the…
YD Yasura Dodo 01:01:06 No, just, just, only, like, OpenTelemetry safety is fine.
The core part ways are still okay, yeah.
Nacho Bonafonte 01:01:13 Okay, I… okay, I can work on releasing a,
YD Yasura Dodo 01:01:16 Thanks so much.
Nacho Bonafonte 01:01:17 Maybe? If that helps you, yeah.
YD Yasura Dodo 01:01:19 Yeah, thank you so much.
Alolita Sharma (Apple Inc.) 01:01:22 Okay, thanks, Nacho. Thank you again, everyone.
Vinod Vydier 01:01:25 Thanks.
Alolita Sharma (Apple Inc.) 01:01:26 Take care. Bye.
Vinod Vydier 01:01:27 Bye.
YD Yasura Dodo 01:01:28 Alright, thank you, guys.
