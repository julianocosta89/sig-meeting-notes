SIG: Swift SIG
Date: 2026-04-30
Duration: 72 minutes
============================================================

## Zoom Recording Transcript

Vladimir Kukushkin (Apple) 00:04:04 Hello.
Moritz (@slashmo) 00:04:06 Hello…
Alolita Sharma 00:05:12 Hi, Nacho, how are you? Hi, folks!
Nice to see you, Sy. Nice to see you.
Right.
Bryce Buchanan 00:05:21 Hey there, how's it going?
Alolita Sharma 00:05:22 Hey, hey, how are you, how are you?
Good to see you guys.
Bryce Buchanan 00:05:27 Yeah.
Alolita Sharma 00:05:29 Alright, so I think, Nacho and Bryce, let me just introduce both of you, and then we can also do intros on some of the folks joining in from the core Swift team, which is pretty cool.
Nacho and Bryce, again, are core maintainers on the Swift, hotel, library, and, have been, you know, long-term Swift, users as well as contributors in the larger community. And again.
you know, we've all worked together on Hotel for the… for a while. So, super happy to kind of, introduce you guys. I… we have been… obviously, we have been working on Hotel for a while, and internally, also had… having many discussions at Apple.
So, super happy to kind of have some of the folks joining in today.
Sy and Vlad, did you guys want to introduce yourselves, and…
Si Beaumont 00:06:40 Sure, thanks, Alice. Yeah, hi, nice to meet you both. I'm Sy. I've been at Apple a little while now, coming up for 10 years, I think.
Yeah, it's just, we kind of want to just sort of come along, and Alita invited us to come and sort of just meet with you folks, work out what's happening in the sort of OpenTelemetry Swift ecosystem, I don't want to speak entirely for Vlad, but Vlad and I both sort of have a focus on the sort of Swift server ecosystem specifically, and sort of building out a set of maintaining a bunch of open-source packages for, like, high-performance server-side Swift, and I think it's a natural fit for us to sort of make sure that we're looping in with what you guys are doing, and seeing how we can sort of work together in places where possible, but yeah.
Alolita Sharma 00:07:28 Awesome.
Vladimir Kukushkin (Apple) 00:07:30 Yeah, hi, I'm Vladimir. I'm not so long with Apple as Psy.
recently-ish. But I'm working on the Swift Server, observability packages. That's my primary area, the API packages we have, Swift logs, metrics, distributed tracing. So, yeah, as I pointed out, this is natural for us to Be interested in OpenTelemetry SDK to also follow the same ecosystem, be compatible at least, yeah.
Alolita Sharma 00:08:06 Awesome. And, did others want to just do a quick round of intros?
Ari.
Reds. I've been nud.
Ari 00:08:17 Hey, everybody.
Are y'all?
No, it's full. It's a full day.
Alolita Sharma 00:08:24 I know, I know. Ari is also one of the maintainers on the Swift Hotel, library, and Vinod, of course, has been a long-time reviewer, contributor, and steadily worked on the Swift Hotel library also for many years now.
And, Ritz, did you wanna… Quickly say hi. Yeah!
Moritz (@slashmo) 00:08:46 Hey, nice to meet you. I don't work at Apple, but I still work in the server-side Swift's ecosystem. I created the distributor tracing library as my Google Summer of Code projects, and then that led to creating the Swift Hotel project as well.
Yeah, looking forward to… to aligning here.
Alolita Sharma 00:09:10 Awesome, awesome.
So back to you, Nacho, and Bryce, and Ari, and we can get started. And then, you know, please feel free to ask any of the questions that we've always loved to ask, you know, and wanted to ask about the Swift server, improvements, and, you know, again… On our end.
nacho 00:09:31 Yo.
Yeah, okay, So, regarding this project, it… it has been, maintained by, by us for a long time. We have had different, level of… of time, that we have been able to, to, to, to put into this project. So, At the beginning, I had lots of time, wrote lots of code, now I'm working at another company, which makes me work on this project on my free time, with my own things, which is something that, yeah, doesn't let me work much here.
For the last years. So, but yeah, basically this project has been used mainly On, on mobile, on mobile apps, so… We don't know of… Yeah, sorry. We… Don't… not many people from the server side has come to this To DC. We don't know exactly how many people are using it on server-side, or using it on the desktop.
except for the… I think that, some… there is some usage, I think, at Apple, using the metrics part.
Or the private computing thing?
Somehow. Because I saw that there were some, references to this project there.
But… Yeah, we don't know much about the usage in the server side.
So mainly it has been… Basically moved by the needs of mobile apps and mobile solutions that we have had so far.
So yeah, and also some of the implementations that we have probably are not the most Performant?
Because some… some of them were written with Swift 3, probably, or even three, four, so… and has not been updated so far. We are currently trying to move to Sweep 6, but not, to… To a structured concurrency, because, you know, it's a big change, and there is not much time in the… maintainers. So we tried to… Add as much features as possible, and we try to Tangle all the, peers that the community, creates and adds Nice, asset.
As quickly as possible from our side for that to happen.
So yeah, basically that's, like, a… description of how… on the state… of the current state of the project, I would say, probably Bryce Camp.
explain it better, in a better English, also.
Alolita Sharma 00:12:29 Not sure what I said, did you guys also want to kind of, highlight what you would like to see added and, in the, you know, in the, implementation,
nacho 00:12:44 Yep.
Okay, I don't know if we're… I have a pair of things that I think are critical and must be provided by Apple, that, we are… in risk of losing, or in risk of not having the best of the support currently. One of them Is the, the method we use for keeping the active context between threads We use ActivityContext for that. We use a… I think a quite a smart way of Getting, the active span from any thread, and having different contexts from different threads, so we can Handle that very, very, very well.
But there is always the, you know, the fear of losing that thing that we lost temporarily with the async.
Await the staff, because He took some versions of Swift, To just copy that.
from the active scene to the async methods, for example. So that's one of the risks, we, we have faced so far. And the other is about, how to instrument in the not working stack.
we, we, We basically, were doing, method swindling on URL sessions in order to… to instrument network, because there are no other good ways of doing that, or there were not before. So, currently, in the async, methods.
The delegates are not being called as they are documented to do, so we had to, reduce much of that.
things, or much of the things we can do there, and also some of the methods that should include the content, for example, are not in the async.
Path, and… or have been lost, at least recently, with the last two versions of iOS, I think.
So we… we have different kind of support, because the library just doesn't… I mean, probably the… the async URL things move to something that's not Objective-C, or that is not built on top of something Objective-C that can be shizzled properly. And yeah, using other kind of Injection, code doesn't seem like that.
Very elegant. So, yeah, that's our… that will be, for me, the things that we… it will be great to have. I know you on Apple for the… For the… tracing library, you use the structured task in order to To… to keep the context on the article span.
But that's not… Like, a good solution if you are not writing that code from the start.
And many of our users, what do is they inject into existing apps. So, in fact, they can do that without writing more than 20 lines of code, that would be great. So everything is just instrumented without them needing to do that.
And that's something that, that… we only could do with the OS activity stuff. That is a very old API, probably not very well supported, we had to do some some tricks in Swift to use that properly.
And yeah, that… so that's another, thing that… I don't think I am missing anything, Bryce.
Nice Fenton.
Nipso.
Bryce Buchanan 00:16:29 Yeah, I mean, I think that's a pretty good summary of, like, the really… Kind of big concerns that we have.
I can't think of anything off the top of my head at the moment, though I'm sure there's lots of little idiosyncrasies that we've run into.
nacho 00:16:50 Yeah, for example, regarding… We have support for Swiss metrics into OpenTelemetry, so we have an importer of Swiss metrics for OpenTelemetry, which was working well, I think. I don't know if they are updated currently for latest metrics in OpenTelemetry, but that has been used quite a lot, by some users. Now, there is also another person who's working on a PR To bring, shift tracing into OpenTelematy, because they add some more, complex, necessities that what it was offered, offered by… by that library, and they wanted to have that, also that, like a… like an importer of AutelSwift structs into… into OpenTelemetry, Swift into the… So yeah, we are, supporting them, and we are trying to help in those, efforts, but those are mostly independent efforts currently.
Because the maintenance time is basically… Trying to maintain the things, and trying to keep up with the spec, trying to keep up with the changes needed.
Si Beaumont 00:18:08 That's great, I mean, I… Don't know if this is an appropriate time to jump in. I'll say… It's really helpful to get an overview of, like, where you're at, where it's… how it started, what it was… what it's for… what its primary audience was.
and some of the gaps you're struggling with. I think this latest discussion about SWIFT metrics and Swift distributed tracing is a very useful segue, I think. I just want to just check in with you, like, what's your vision for the package when it comes to… like, the entry points for the OTEL SDK that you are maintaining, like, Because I guess… the OTEL SDK… there's a spec for that, which is, like, you know, if you want to use OTEL, this is how you do it. And then, obviously, these other, abstractions, for observability in the Swift package ecosystem, like Swift Metrics, SwiftLog, Swift Distributed Tracing, they're sort of a different entry point for users. Is that something you see as, like, like, a thing on the side? Is there some… or is it you think it's sort of complementary? Like, how do you see them composing, and, like, for your users?
nacho 00:19:13 Yeah, regarding package, and yes, not to forget that. We had a… or we have had a really big limitation with SPM as a way of handling the package. It was used since the beginning, but the problem was that the OpenTelemetry spec forced us to have support for many exporters, at least until probably next week, where they, I think they updated that Alolita, as you know probably better that.
Alolita Sharma 00:19:42 Yeah.
nacho 00:19:43 So that implied that we had to… Add lots of code and lots of third-party libraries.
some of them from Apple, or Protobath, for example, that really brought, like, A storm of… of dependencies that made the project grow a lot, and that was a big problem for many users who just wanted to build the API.
And SPM didn't allow you to just download the packages that you depend on, because it downloads everything that's in the package, so that meant, like, you know, 200, 300, 400 megabytes of hundreds of files.
just for building some. We moved to having two repositories, which brought some other problems, because you have to keep synchronized, you cannot release so easily, and we are struggling just to release since we changed that. And, yeah, that, that…
Si Beaumont 00:20:43 Have you folks considered using package traits, or explored what it might take to move to package traits?
nacho 00:20:50 Yes. Slightly, because the problem is.
The same problem always happens with Apple is that you only can use that in the new versions of things, and when you have to support older versions of things, then you cannot use new features.
so easy. I mean, it's great. We will be able to probably use that in 4 years from now. Great. But if we are supporting now users that, you know, are using maybe old X codes, because they have to support I.O, macOS, you know, 10.
10, for example, you know? Some of our.
Si Beaumont 00:21:29 What is your support policy? I think it'd be super helpful for us to understand.
nacho 00:21:35 I think we are 10.7, Bryce? Maybe we updated a bit more than that. I don't remember. The thing is, we have tried to keep as much as possible people there. I know that Xcode and the App Store now is forcing you to have Xcode 16, for example, and that means that you cannot Link for something on there.
But the truth is that for some users, they are using old X codes, all systems, just because they need to support very old versions of iOS, so you cannot really move really far into the tech stack, you know, I think if you… yeah.
Bryce Buchanan 00:22:12 No, sorry, not Joe. I think we recently, like, reviewed, what versions we can support, and, you know, based off of the, stakeholders, like, the latest that we… that we think we can get away with is, version, like, 13 of iOS.
version 12 of macOS, and that's kind of where we're at. Yeah, so we're really kind of stuck way back there.
Si Beaumont 00:22:40 I don't think that's a particularly… particularly limitation. The deployment targets being quite old is something that, in the server ecosystem, we… Also have to support, like, so a lot of our… cross-platform.
libraries, The minimum deployment target is very, very low, like, you know, 10.5, or sometimes we don't even express it in the package manifest, which means it can run anywhere.
But the minimum supported developer toolchain for the package moves forward.
And most of our packages in the ecosystem have… Roll with a, sort of, three-release window.
So, like, we'll support… the latest Swift version, and, like, aligned Xcode, and, like, the two before that, and sort of roll people forward that way. I mean, that's obviously an arbitrary window, it's the one that we're working with with a lot of our packages, and it doesn't mean you guys, will or should do that. But I think… thinking about… I mean, maybe it's… it sounds like I might miss some of the nuance here. Decoupling the sort of development… toolchain required to build your package from the minimum supported deployment targets might widen your options. But from what you said, Nacho, and I might not have enough context here, some people might genuinely be tied to older Toolchains? Is that what you were saying?
nacho 00:24:05 Yep.
Si Beaumont 00:24:06 Okay.
nacho 00:24:06 Yeah, because, They… usually, if they have contracts with public entities and things like that, in the contracts, they have, like, very old versions and things like that, and we have really had Some users of the library saying that they couldn't they couldn't update so, so, so, so much, because they, they had… and especially because Many of the users of the library are middleware.
who package the library in another bundle that just provided full service to the final user. And they had contracts that make them limit what versions they have to.
So, that has limited us.
Alolita Sharma 00:24:54 Yeah, yeah, and I mean, typically, Sy, as you know, in the industry, and also we follow it the same way in Apple, is that there's at least 7 years of support that is provided for, you know, existing versions in the industry. So, that's pretty standard across many of the providers, and especially folks who are providing, You know, a platform.
For mobile developers, for example, where they have compatibility, backwards compatibility, maintained for 5 to 7 years of backward, versions.
Si Beaumont 00:25:36 No, that's…
nacho 00:25:38 Yeah, we have a… we have an end user with… Old machines, using old versions of.
Alolita Sharma 00:25:44 It was cold.
nacho 00:25:44 It's just because they must build with that, right? Which is like a… it's like a joke, but they need to do that. Sorry, Ali.
Ari 00:25:53 No, no, it's basically what you mentioned, that most of the users of the OpenTelemetry SDK and API are… observability SDKs, which bundle the OpenTelemetry API or framework, and… which causes to… they have to support multiple different types of apps from different places, and if they have… if those apps have a 1% or a 2% of people in iOS 11 or iOS 13, In order for them to implement or to consume the package.
They have… we still have to support those minimal deployment targets, too, and that's why we were a bit limited.
And obviously, I think the last years, we need to make multiple migrations. Now with the Swift 6, I think it's kind of a big migration, because of all the concurrency.
Thanks, so… Currently, we support Swift package 5.9.
Correct me, guys, if I'm wrong.
But that's… that's the base, basically it, and as far as I know, trades are allowed since 6.1 or 0.2 of the tool package.
So, we're somewhat limited in that aspect. I think it would be awesome at some point, but… you know, sometimes what we have in the package support is not what people are asking for. Like, for example, XC frameworks, which are completely difficult to build with packages.
So, we have that mismatch, because the tooling, that it's really, really useful for the server side, like, you don't care about exit frameworks at all, but for mobile applications and stuff like that, XE frameworks are… Super, super useful.
And we… we have to… to… to balance those things out, because most of our… of the users of the… Open Symmetry SDKs are mobile developers, or developers, SDK developers.
With mobile customers, and not that many server-side customers or users.
Si Beaumont 00:28:02 Interesting I mean, I can carry on, but I'm a bit nervous that I'm not, like, adhering to the way you run your SIG, I'm just, like, jumping in. Like, if you've got… at least, how do you typically chair these meetings?
Alolita Sharma 00:28:15 Typically, we have a meeting notes and agenda doc, and we do add items for discussion in it, but it's, it's totally okay to have a free-flow conversation.
nacho 00:28:29 Yeah, yeah.
Alolita Sharma 00:28:29 You know, there aren't any other items we want to cover. This is the doc, that You know, and it's an open dock. You guys can definitely add to it whenever you have any questions or any areas you want to dig into.
Si Beaumont 00:28:43 Soria, sorry, fire.
Alolita Sharma 00:28:44 No worries.
nacho 00:28:46 Yeah, no, no, yeah. I mean, we… you can see that that's not very complete, no, no, and we don't follow that fully. Yeah, yes, it's more a tracker, or a… or a… Or, just to know what, what to talk about more than… than other… Damn, yep.
Alolita Sharma 00:29:13 So, I think, Sy, one of the things that might be useful also is that, you know, you guys have been working on a, on the, making the… Swift server-side, you know, instrumentation also, enabled with the Swift OTEL, you know, implementation, In… in the Swift repos. So, maybe, you know, kind of talking about some of the objectives there, and… you know, how they can be leveraged both by OTEL, as well as with… through the SDK, as well as, in some of the use cases you guys are trying to address, might be helpful.
Si Beaumont 00:29:57 Absolutely happy to give a brief overview there, like, I think so, just before I do, like, a little observation, just looking at my own notes I've been taking, you've mentioned a lot of things here around, like, OS activities, method swizzling, most of your customers are, like, mobile developers. I think, sort of.
well, my take… and you have people asking for XC Frameworks, my takeaway here is that, like, you… your primary audience has been, at least for… For the time of all.
nacho 00:30:25 Yep.
Si Beaumont 00:30:26 On app developers, and…
Alolita Sharma 00:30:28 Yes, yes, yeah, definitely. Yeah, that's definitely the core target, because, you know, most of the observability frameworks that are distributed by observability vendors, have to support that larger mobile ecosystem, right? Both… and OTEL has a commitment in terms of supporting Android as well as iOS, and… And web, clients, right? So, there is a lot of effort in terms of maintaining compatibility and providing that, last mile, you know, support, for app developers.
And… and as Nacho rightly, you know, called out, and Ari did also, the… ecosystem of mobile developers, obviously, is also based on the devices, versions of, you know, what is running on the devices, and hence the backward compatibility, in Last Mile.
Ari 00:31:31 Yeah, that said, we have support for Swift server-side. We have in the CI a bunch of different jobs and stuff to test on Linux directly to see if everything of our usage, of the APIs we're using are compatible and all that stuff. So… The only problem is that we didn't have so many people asking for server-side-specific stuff.
Which is not that we don't… we don't care about it, it's mostly, like, we… we are… We have the two tenants, like, staff that is being asked from people, and that is mostly stuff, or SDK for apps and stuff.
and other things that are, you know, things from OpenTelemetry that we have to do, and we have to catch up in terms of the specs. So, those are our main… foundational tenets, I think, of things that we are doing.
That's a… .
Alolita Sharma 00:32:28 Yeah.
Ari 00:32:28 supports server-side.
Alolita Sharma 00:32:30 Yeah, and then to Ari's point, you know, again, the spec… that OpenTelemetry defines, again, is to standardize the way that, you know, the libraries are available and usable in a standardized way by users, but It's also that the spec continuously evolves. When we see a gap, you know, which is drawn out by a particular use case or a scenario, you can always submit an enhancement proposal. It's typically very similar to the Kubernetes enhancement proposal process, where you do submit an open telemetry enhancement proposal.
And you can, you know, definitely recommend improvements, because sometimes languages have specificities, right? And it may not be handled by a completely generalized specification. So there are, you know, the capabilities of making those changes when needed.
Si Beaumont 00:33:33 Well, I mean, I can give you a sort of brief summary, I guess, of… where we were… some of the investments we've been making in the Swift Server observability ecosystem, and, you know.
once I've done so, I guess Vlad and Morris also might want to comment on some of these topics, but As a jumping-off point, it's probably worth expressing that Well, your, like, primary audience, or at least seems like a lot of your customers' focus and interest is around, Swift as a app for… as Switzer's language for app developers on Apple platforms.
Swift, obviously, is… A general-purpose language, and there's an ever-growing interest in using it in all sorts of contexts, both on server-side, but also, like, in other areas, like embedded and on other platforms as well, like Windows, and Linux, and Android.
And so as I think that's… as the language ecosystem has broadened from being primarily focused on app developers.
the server-side ecosystem is… Also, trying to create a sort of… Sensible ecosystem of packages that allow people to build high-performance servers in Swift. What, with it being a memory-safe compiled language, it's good for performance, it's good for safety.
all the things people love about Swift for the device, no reason they can't have all those things on servers.
To that end, I think a lot of the Swift package ecosystem sort of branched out with, you know, we've got things like the NEO stack with all the… and the protocol implementations.
And one of the things that's sort of at the core of some of the principles in the ecosystem is these these thin abstractions. Very similar to the way OTEL, sort of.
splits its spec between an API spec and an SDK spec.
The Swift ecosystem sort of developed its own sort of abstraction layers for telemetry, with Swift logs, Swift metrics, and Swift distributed tracing. The idea being that these would be the thinnest thing that anyone could depend on in any package with a very small and stable API.
for… I guess, recording telemetry in their libraries, and that the backend, or the, or the exporter, I guess, to use a different terminology, is entirely pluggable, and so decouples, the entire ecosystem from any one format, any one, Anyone, sort of, exporter, and that seems to… been reasonably… accommodated in the ecosystem, like, a lot of packages will use SwiftLog or Swift Metrics.
And it means that they're able to sort of remain performant, not pay the dependency costs of taking on large Observability packages, and any performance costs of… Recording telemetry, when there is no backend configured.
I think so, I think when… Morris will be able to talk to the genesis of Swift Hotel better than me, but, like, I think Swift Hotel was there to sort of fill the gap of, like.
For folks that are using this as their entry point.
Like, so… or, like, they're depending on a bunch of dependency packages that are using Swift metrics, or Swift Logs, or Swift distributed tracing.
how are they going to export all their stuff? And OpenTelemetry was obviously a… a popular format people wanted to, get things out on. So Swift Hotel sort of evolved as a specialized backend.
And it wasn't necessarily committed to.
Like, providing the full SDK experience. It was more… if you wanna… But we've always, like, if you want to be full OTEL, there's an official OTEL SDK, but if you want your metrics out of SwiftLog, Swift metrics tracing, we needed a way of doing that. Now, I think there's a bit of overlap now in the goals. You know, you've said already, you've got a metric shim, you've got a log shim.
Don't know about distributed tracing, sounds like that's a work in progress.
But I think it's worth a sort of, like, Revisiting, like.
who are the audiences of these packages? What do they need out of their entry points? What's gonna be a, like, a good ecosystem for Swift for… people that's clear, like, you know, what can we get out of anything, out of these two packages?
Or is there, you know, what does the official OpenTelemetry SDK want to provide for the server?
use cases that, don't need all the same things that you've mentioned that are on-device concerns. They need to remain extremely lightweight, like, extremely performant, with very stable dependencies.
I don't know if that's… set the scene enough, or answered your questions. I mean, so Vlad is now taking a bit of a steer on the low-level abstraction packages themselves, with log metrics and distributed tracing. He might be able to talk to some of the things going on there. Moritz, of course.
did a whole bunch of the legwork in Swift Hotel, he'll be able to talk to things I've missed there, but… from an overview, that's my position of, like, where we're at. We're just looking to be available Make sure we're sort of, like, at least meeting with you guys, understanding, like, is there any common ground here where… You know, the ecosystem can benefit from us having more joined-up thinking, or at least a better joined-up story.
nacho 00:38:51 Totally.
Ari 00:38:51 I can give you my two cents about the why.
at least from my perspective, obviously biased by what I do, I work as an SDK developer on observability companies, so… I think that the thing that is completely attractive, from… for, frame.
for mobile developers and different companies, whenever they use observability SDK that supports open telemetry, is that they support an open standard, which different components can understand and talk to. Like, it's not that we just have Prometheus or your, I don't know, any sort of closed source format.
we… if the SDK supports this OpenTelemetry standard, you know that you are not vendor locked in. You can go and, in no time, go and switch to your own backend, to your own thing, because you just plug your instrument once, in one single way.
obviously, you can use the vendor-specific APIs, but you can use the non-vendor-specific, that is the one that OpenTelemetry provides, like a tracer, using the tracer provider, or a logger with a logger provider.
And once you have that, you just plug in your processor, your exporter, that communicates with your backend, or even your collector, and everything should work fine.
So, I think that the main benefit today is that you are not vendor-locked in, and you own the data. And that's something that a lot of companies are asking is that they want to own their data, and sometimes they even want to own the infrastructure. So, if we as SDK providers provide that possibility, then people are more… They are probably going to be more willing to use your SDK, knowing that they are not locked forever with you, and if they want to switch in some moments, they don't have to go and change their whole APIs, the whole way they instrumented their application, and all that stuff. Even though every single application in the world has an abstraction to tracking analytics, or stuff like that, or observability. In the end, you just use one single API. That is tracer.starspan, and that's basically it, or logger, and emit a log, and that's it.
So, I think that's… that's the main benefit, at least from my perspective as an SDK developer, that it provides. And obviously, it's easy because I can even test things with a no op, like a… I don't know, like a console.log exporter. I can see everything while I'm developing. I create… I can create something similar to see it in the UI.
And I can do something, so whenever I export, I import to my backend in my own format. So, I think that's the main benefit, or why people are using OpenTelemetry, at least when I'm talking with customers, that's also what I see from them.
Sorry, naturally.
nacho 00:42:00 Yeah, one of the… when this project was started, I mean, OpenTelemetry Suite, It was thought, initially, to be, Zero-effort way of adding telemetry to whatever you did.
I… Did it for a test observability project, many years ago, you know.
startup, and donated the first thing to the community. And after that, I have been continuing maintaining.
And yeah, and adding many things, but the… I think the key point was that You could have… with just… 10 lines of code, and linking a library you have your app ready, and showing traces, and showing things, and showing life in any place you have. It could export those traces for OTLP, but could also export to any other trace, like, that was supported in the spec.
So, you so easily got something working, and then you can just specify what you need on your specific things that you need. So you have something that initially works, you have something, and from there, you just Iterate on the things that makes your app different, or makes your product different to others, but you start with a very simple base that gives you that. Also, there are many SDKs. I never work on an observability product for generic, right? But I was always very focused on having an easy-to-weight wait for… standard users without using an intermediate SDK to have also a path to that. I mean, having an intermediate SDK, like, like, like the… like Watari does, or Bryce, that's great, because they have much more value. If you really want a great product, probably, that's the way to go, having a middleware that offers you a lot of richness and a lot of things very easily. But also.
start by having something that just works and offers basic stuff, I think that that's also very key. And that's why I was so focused on having The, the, the… the two things I said at the beginning, right, is having the active span automatically calculated everywhere. That's something that you have. You have… you put your link delivery, and you put the Network instrumentation just running.
probably 5 lines of code, and you have all your app and all your network requests just as spams. And you see all the flows and all the threads and all… everything that's happening at the same time.
And that's… Yes, 4th grade.
just linking and adding some basic configuration, and I think that that's key. Also, for middleware, because probably you can start with using this basic network instrumentation we have, but you can move to having something more complete, or offering other things to your customer later.
like, I mean, URL configurations that just they can set, but Having something simple and something that provides solutions, quickly, I think that's also key.
For… for their people to have.
And yeah. So, having… I think it's a bit like the Swift… swift ethos at the beginning is, like, have something really easy to have there, and just spend time improving when you need.
So, I don't know what was… there is something said similar to that, right? So, something simple to have.
easy solution, and give you a possibility to really improve and iterate there. And I think that that was… And that's key for this project.
Si Beaumont 00:46:08 Just to make sure, so, I mean, so the primary benefit, I think, was sort of outlined as an abstraction with no vendor lock-in, and then, like, this ability to quickly get something very useful out. I have an app, and I want to instrument it, and now it's very simple, few lines of code.
Lots of it.
nacho 00:46:24 You don't need to know anything about observability to add it.
I'll be honest. Yeah, starting… The configuration and… and plugin, or the… OpenTelemetry SDK, or any of the middleware there. Just 10 lines.
plug your… this… this SDK, this library, and you have And you have everything, right?
Si Beaumont 00:46:45 My question?
Ari 00:46:46 Open… oh, go ahead. Oh, sorry.
No, no, and the openness to go and create your own set of instrumentation, and suddenly you contribute that Either to the community or internally, because you just plug in that instrument, and everything should work fine, because it uses internally a tracer lover or metrics provided.
Alolita Sharma 00:47:06 And I think I would like to add here that, you know, from a production perspective, typically there's also the need to have a single pane of glass in terms of not only the edge, you know, client observability data that is being, you know, again, instrumented and collected through the SDK and then sent to the backend, but also.
looking at a single plane of glass along with other components in a service transaction. So, or a user request. So what that means is that you're not only leveraging, often only the Swift, you know, libraries, but you're also looking at other, you know, components in the entire trace, or in the entire including infrastructure, and that single pane of glass is, very important in production when you're especially looking at, you know, latencies, degradations, errors, failures. So it's not only a single ecosystem there, right? You're really looking through the entire, flow.
Si Beaumont 00:48:19 I think there's no denying the benefits, like, when you've got that.
at the… when everything's been collected, and it's all… it's all been, sort of, like, donated and visualized all together, that's, like, where the strength of distributed tracing really shines. I guess my question was going to be about… the network effect of, like.
You have an app, and you… Add some instrumentation, But how does… your dependencies contribute to the instrumentation. Let's say you have a Swift And you're, like, depending on a bunch of other, like, third-party libraries or packages in your Swift app.
To get the telemetry out of those apps, those dependencies.
in your exports, will they also need to have been depending on OpenTelemetry API package, at least, and being… contributing to the counters, or the spans, contributing… creating their own child support.
nacho 00:49:15 I mean, for example, the network instrumentation creates child spans by itself and joins to the active span that is automatically generated. So you can call ActiveSpan anywhere in the app, whatever the thread it is, and you will get the active span for that explicit context. That means that you add a third-party library that you network, and as it's using methods tweakling on URL session, you will get all the network stuff that that does, for example.
Si Beaumont 00:49:48 But no one can create a span within.
nacho 00:49:51 I mean, yeah, if you, if you… In a third-party library, if they wanted to add a span, they need something that swizzles the methods, or they have to add it manually. Yeah, that's true.
yeah, there is always the… If you use, for example, other binaries, there is the trace parent as an environment variable, for example, so you can On the server and things like that, but not on mobile, but on desktop you can do that, like, running.
running other binaries that takes the trace parent from the environment variables, for example, and they can follow your trace, and things like that. But yeah, it depends. I mean, if we could methods we sell, for example, core data, and that library uses Core Data, that will be great, because we will have that visibility. That's the idea. I mean, our goal is Or at least my aim was adding as much visibility to your app for free, as much as possible.
And yeah, we can do that with networking, but if you think about what a mobile app is nowadays, usually.
is just network stuff. You are just connecting, and you are… you are just, 80% of the app are just web pages that are drawn in a phone with some buttons, right? So that covers, possibly, most of the needs.
Alolita Sharma 00:51:22 Or coming soon, talking only to LLMs. Yeah.
Si Beaumont 00:51:28 So I think it makes a whole bunch of sense that, like, auto-instrumentation and method swizzling works there if that's the sort of granularity at which you want to see things.
nacho 00:51:36 Yeah.
Si Beaumont 00:51:37 But once you sort of, I think, sort of bring the other perspective of packages, the observability package in the Swift ecosystem, is, In a, like, a large server environment where you're depending on a bunch of library packages, you're gonna want to have visibility into… what those packages are doing beyond just the network calls. And I guess, bringing it back to the… you guys said, oh, you know, the main selling point of OpenTelemetry is this, like, single abstraction. Obviously, that's so compelling, it's so true. I think the Swift observability packages essentially are trying to do… it's a similar model, right? They're trying to provide this thin abstraction layer that everyone can unify on.
But it's at a different… it's at a different level of abstraction.
So rather than being OpenTelemetry, which I guess is cross-language.
cutting concern. It doesn't matter what language you're coming from, I can pick up an OpenTelemetry SDK, and I know how to use it, I know the APIs.
I guess the Swift Observability package is, like, the metrics logged into stupid tracing, like.
It's like a language-level abstraction. And I'm wondering, how do we marry these two things together, so everyone wins?
nacho 00:52:43 Yeah, that also brings me some of the peculiarities of the people that use our library, is that they are usually multi-platform developers.
They are, or full-stack developers, or they do… mobile development, both in Android and iOS, or they don't have much experience on Swift.
So the truth is that… They are no experts in doing many things in the language, so that, yeah, that could also explain some of that.
But yeah, the truth is, yeah, it will be great if those third-party libraries, could, you know, take the active span, if they link with OpenTelemetry API, they could Take the active span and continue that, or doing spans themselves.
hanging from the spand that's active when the library is called. And with our current approach, that will be possible. So you can have a third-party library that links with Swift API, that links with an app that has started OpenTelemetry.
And if you… Just call getActiveSpan, you will get the span.
That… in the app you have linked with… with the ORS activity.
So you can release.
Yep.
That's alright.
Ari 00:54:07 And also, to put in context, as you guys heard already, our main consumer are app developers, and I think that from Subjectively speaking, you know? That, in backend, in server-side, observability is a more first-class citizen than in mobile.
So… The fact… the… the… even the culture of adding spans, traces, or logging, it's completely different from a server-side developer than a mobile developer. That's why most of those developers rely heavily on third-party SDKs, like the ones I create, that basically abstract that, and all you have to do is just plug your… plug the SDK, and suddenly you have all the necessary information, and obviously, as you know your code, you are the one that go and instrument that piece of thing that you want.
But many, many, many times, we get requests, like, hey, I would want to know what is happening on this third-party SDK, or this other thing, and we have to figure out a way to hack it.
Huckily doing it with fish hook, swistling, whatever, technique.
But, yeah, as Nat just said, it would be really good that those, third-party providers could embed or have as a dependency open telemetry and be able to go grab the active stand, or even instrument their code with the tracer provider, get the tracer, the current tracer that is available, and instrument their code, so everything Works in a similar way.
But obviously, that… that depends on multiple factors, like, can they… distribute their SDK as a dynamically… a dynamic framework, because if they statically link it, you'll have problems with symbols and all that stuff, that it's… Kind of common in the mobile industry.
nacho 00:56:11 Yeah, the import-export dance in Swift has been very fun, so… For so long.
Vladimir Kukushkin (Apple) 00:56:17 Sorry, buddy. Yeah, sorry, I want to jump in. Probably, ask Ari, so I get the automatic instrumentation.
Thing, that's, like, value of this is undoubtable.
How do you, you probably know how your users… combining this automatic instrumentation with, well, everything else. Like, they still need to write log lines, emit logs. They at least emit logs. How does this combine together, in your view?
Ari 00:56:54 So, obviously, it's somewhat difficult, because, again, it's a cultural thing that you have to start even teaching, like, when is the best moment to log, what the log should have, and all the stuff. But also, different companies have different types of limits, so… It's… it's… it's… it's complicated, because you have to tell them to… how to log, and… and teach them how to log, in… in… OpenTelemetry, you have different ways to kind of log things, because you have the span events, or now the events API directly. You can just create logs with a different entity. So, you have to basically tell them how to do it and all that stuff.
And as time goes by, there are things that we cannot instrument automatically. Like, for example, you are already… everybody knows about SwiftUI, And people want to have SwiftUI instrumented, but sadly, that's not something we can swiftly. Like, you can do some really hacky stuff, but I wouldn't recommend that, that some providers are doing.
But basically, what you provide, it's a way to instrument your view, that under the hood, uses spans, logs, and all the stuff. So, that's basically… we try to make simpler, in the language.
mobile developers understand, but in the end, what the SDKs are doing, the third-party SDKs are doing, is basically wrap all the OpenTelemmetry entities and APIs while providing that instrumentation.
Alolita Sharma 00:58:32 Yeah.
nacho 00:58:33 For example, in Apple systems, unified logs are great, because they are very powerful, they are very fast, but you cannot capture them, for example, right? That would be great. We could capture the OS log that the user has.
It will be marvelous, because you… we could add automatically to the spans, we could add automatically to the active span, so be in a span event, or… or just… You know, refer that log from the… from the… but… but…
Alolita Sharma 00:59:07 Yeah, but the system doesn't.
nacho 00:59:08 That doesn't allow… I know for the server side, there is a… OS log, also library, I don't know exactly what the names are, because they are so similar that I probably missed them, that it will allow… and I think… I'm not sure if we added that as a demo or a beta version, OS log importer, into OpenTelemetry.
So in the server-side, if you use that, it will capture those logs and will assign that to the active span where the log is written, but only for the server-side log library.
Vladimir Kukushkin (Apple) 00:59:46 I'm not sure what service site OSLock library… so OSLock is Darwin-specific that could be working on that.
nacho 00:59:53 Wasn't there a log… wasn't there always log library for server that had a very similar.
Vladimir Kukushkin (Apple) 01:00:00 Swiftly.
nacho 01:00:02 Mini Trove.
Vladimir Kukushkin (Apple) 01:00:03 Yeah, OpenTelemetry Swift SDK provides the lock handler compatible with SwiftLog. But I think what's an important part here, and we're kind of getting there from different directions.
is the… the goal of the observability API packages, with clocks, with metrics, with distributed tracing, is to… provide a layer of abstraction across all the platforms Swift supports.
So, it… it doesn't… you don't need to find a hacky way to grab OS log log logs, unified logging. You need… you don't need to swizzle some… something somewhere automatically. You have this API layer, which libraries support. Libraries, SDK, applications support explicitly-ish.
And then, through the… through these APIs, it's wired onto the concrete implementation, which can be OpenTelemetry, Swift, or can be Swift Hotel, or could be anything else, could be platform-specific logger into the console log, OS log, for example, or Android log, or whatever people use, wherever. So… That's the main idea, that libraries don't care, and they use this abstraction language-level… I like how Saeed put it, this is a language-level obstruction.
Si Beaumont 01:01:30 I think one of the key differences is it relies on a network effect of people choosing to contribute telemetry, as opposed to an emphasis on auto-instrumentation, where you are pulling tricks to try and extract telemetry from your dependencies. Auto-instrumentation is, like, some of the coolest things ever, particularly some of the, like, really cool stuff that happens.
Under the hood. But swizzling's not even an option for some platforms, right? That's a very, like, Objective-C runtime-type construct.
Doesn't exist on… For other runtimes, so… Yeah, I think, as Vlad's pointed out, I guess we're running at time, but I'm wondering if, like.
Is the… I wondered if there's a world where… an official opener… open telemetry SDK will… would want to cater for these people if it's just outside of scope, you know, these cross-platform concerns.
Alolita Sharma 01:02:20 No, no, it's… I don't think it's outside the scope of the project. It's more that… You know, again, the hotel, language libraries are very much focused on supporting the users who are, you know, actually, coming to the project and working interoperably, you know, across languages, as Nacho pointed out.
Definitely, I think, Sai, the next step is here, really, to continue the discussion and also figure out you know, the coverage in terms of just leveraging the power of also what the language is doing, right? And being able to actually then pull it under the hood into the hotel.
libraries to be able to distribute, you know, and leverage the network effect, if you will, of having that, a wider audience being able to leverage that, right?
So, I would say that, you know, I know we're almost the minute off, but To kind of, you know, really invite all of you to kind of participate, really, be, you know, all work on this collaboratively and figure out, some of the areas we can actually, build out together.
Si Beaumont 01:03:40 Yeah, I mean, I'll just say, I think someone invited me into the CNCF Slack, so I'm happy to hang… I'm now there, I'm happy to hang out, happy to continue this discussion.
Alolita Sharma 01:03:49 Yeah, yeah, and you, you know, again, just invite everybody, you know, please join the CNCF Slack. It's just very easy to communicate, and our… the hotel SIG channels are very… Very useful.
And, and this meeting is weekly, so anytime Cy, lad, you know, Ritz, you guys have time, you know, please… please just join in, or, you know, work with me. I'm happy to help.
Okay, cool, we're at time. Thank you, everyone, and we'll circle back with more. I did add some notes, but if there's anything else, you know, we'll continue adding.
And I think, Sai, you got a lot of questions, and Lad and Moritz were answering, so… please take a look at them, too. Lovely to meet you. Thanks. Really nice to meet everybody again. Thanks, everyone. Take care.
Moritz (@slashmo) 01:04:49 Thank you. Bye.
nacho 01:04:50 Thanks. Yo.
Alolita Sharma 01:04:51 Right.
Ari 01:04:52 Bye-bye.
