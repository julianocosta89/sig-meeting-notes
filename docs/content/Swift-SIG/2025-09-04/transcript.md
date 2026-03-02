SIG: Swift SIG
Date: 2025-09-04
Duration: 41 minutes
============================================================

## Zoom Recording Transcript

**Bryce Buchanan** 00:38 Hello, hello?
**Arri Blais** 00:40 Hello!
**Martin Holman** 01:09 Bloom.
**Bryce Buchanan** 01:10 And…
**nacho** 01:13 Hello?
**Bryce Buchanan** 01:15 In a nutshell.
**Martin Holman** 01:16 Good morning.
Good evening. I'm not sure, actually, where you are now, Joe.
In time zones.
**Bryce Buchanan** 01:24 What's that?
**Martin Holman** 01:26 Oh, I just said good morning to Nacho, and then I was like, actually, I don't know what time zone you're in.
**Bryce Buchanan** 01:30 Oh yeah, it's evening for Nacho.
**nacho** 01:32 Yeah, it's 6 PM here.
**Ari Demarco** 01:54 Eyon.
**Bryce Buchanan** 02:22 Alright, looks like we got everybody here, so, let's,
Let's get started. Let me share my screen.
Let's pull that here… And… share… that.
Oh, where did it go? Oh, there it is, okay.
Zoom always, like, throws all the windows in all different directions whenever you start sharing something, so it's, like.
Alright, so let's take a look at topics from last week. So, we got the, repository division.
**Martin Holman** 03:04 If you're sharing the docs, yes, we just see Heness Simster.
What are you seeing? Oh, man. Innocent.
**Bryce Buchanan** 03:12 Oh, good, okay.
**nacho** 03:14 Yep.
**Bryce Buchanan** 03:15 There, this one, here it is. I have a green box around it now.
**nacho** 03:19 You don't have password to revert on, and nothing personal there.
**Bryce Buchanan** 03:24 That's good.
So, last week, we spent all the meeting just talking about what to do with this repository,
division stuff, and we settled on the Swift core. And so now we've got, in both the, OpenTelemetry Swift.
has removed the API and the SDK and moved it into, OpenTelemetry Swift Core, and that all seems to be working. I just… I don't know if we want to do, like, a release that matches,
the version number of the existing OpenTelemetry Swift.
But I just… Defaulted it to 1.0 for now, just so that we can actually reference something.
Yeah, so… That's exciting.
And let me just… Go to the package here, and…
Yeah, here we have that in the dependencies now, so…
Yeah…
I don't know if anybody else wants to say anything about that, but there you go, there you have it.
**alexcohen** 04:50 That was a lot quicker than… than we thought it would be in the beginning.
**Bryce Buchanan** 04:54 Yeah, I mean, honestly, the hard part was, was making the repo over and over and over again.
**alexcohen** 05:00 I think… I think whoever came up with the idea of switching it around, creating a core, keeping the other one as is, was a great idea.
That, that streamlined everything a lot.
**Bryce Buchanan** 05:10 Yeah, it definitely made things easier, didn't it? And I guess, yeah, so the follow-ups there are, we do want to,
I can't remember what we wanted to do. We wanted to bring the, OpenTelemetry,
protobuf stuff into… into the, core, which aren't actually that large in terms of the dependency chain.
But we needed to remove the,
I can't remember exactly what… I think that there's a… Martin, you were looking at this, right?
**Martin Holman** 05:56 I put it down as the last one there, like, whether we can remove usages of the Neolibrary. That's right, yeah.
So… I basically, I, I,
pulled on, onto this, it's not running on Linux, because it, uses a bunch of, I think, macOS stuff, or Apple stuff,
But, I was like, presenting to everyone, like, is this… should we continue on this path? Like, it's… it's…
Basically written, its own test web server that doesn't use NEO,
the test will pass and everything but Linux, but we have to maintain this… well, maintain this HTTP test server that's, definitely a lot bigger than…
than just having the neode dependencies,
And it's 600 lines long.
**Bryce Buchanan** 06:57 Okay, that's… I mean, yeah, it's just for the test, so it's not too big of a deal.
But yeah, so the, the, the issue is, while NEO is not actually required by any of the OTLP,
products, it is required by the tests, and NEO is the real kicker in terms of the large dependencies, which is required by Prometheus, I believe, is why it's in our project at all. So…
**Martin Holman** 07:28 Okay, well, if I carry on then removing this, that will get rid of NEO dependency from the tests for the… for that stuff.
**Bryce Buchanan** 07:35 Yeah, so, yeah, and that will allow us to bring the…
OTLP, exporters into the core, which is… which is in line with the specific.
**nacho** 07:45 Isn't… isn't it needed for gRPC stuff?
**Bryce Buchanan** 07:50 Neo is not, I don't believe.
**nacho** 07:52 Oh, no?
**Martin Holman** 07:53 No, I think it's needed for gRPC, but maybe not the protobuf stuff.
**Bryce Buchanan** 07:56 Okay.
**Martin Holman** 07:57 for HD people.
**Bryce Buchanan** 07:58 It's going on.
**Martin Holman** 07:58 HTTP protobuf in, Core.
**nacho** 08:02 Okay, yeah.
**Martin Holman** 08:03 I believe.
**nacho** 08:04 So we, we would keep… Yeah, it's because I remember…
Yeah, I did it long ago, but I think it was,
it was needed by the gRPC staff, because it's the only way for…
**Bryce Buchanan** 08:22 No. Unless it's… unless gRPC depends on NEO… oh, it does, yeah, here. Oh, no, this is the tests.
Yeah, so I don't think gRPC actually needs the Neolibrary unless gRPC depends on it through another dependency.
Yeah, the only thing that… in our targets that actually depends on NEO is the Prometheus exporter.
**nacho** 08:58 Sweet.
**Martin Holman** 09:01 So yeah, I've removed it from… in that PR, I've removed it from the URL session tests and the exporter tests, so it should just be prepared after that.
**nacho** 09:11 Yeah, GRPC Swift depends on… on… Apple Swift Near.
**Bryce Buchanan** 09:16 Oh, okay, so maybe… alright, then.
**nacho** 09:18 In the gRPC package, it shows it, yeah.
**Martin Holman** 09:21 But that's okay, right? Because we don't… we don't want gRPC in… we don't need gRPC in core, we just want HTTP protobuf.
**nacho** 09:28 Yeah, yeah, yeah.
Totally agree, yeah.
**Bryce Buchanan** 09:31 Cool.
**nacho** 09:32 Yeah, the thing is, I would have never added…
Swift Neo, if it wasn't needed. I am sure of that.
But yeah, it was in, in, in…
**Martin Holman** 09:45 I mean, it certainly made the test easier to write, because it required 600 lines of code to replace it.
**Bryce Buchanan** 09:50 Yeah, yeah.
Alright, well, let's continue on with that.
Oh, what happened here? Yeah, okay, so,
I've removed NEO from tests, move, OTLP, HTTP, exporter…
**Vinod Vydier** 10:17 to…
**Bryce Buchanan** 10:19 core.
Alright, cool.
I think that's really all…
That we had from last week.
We didn't get to review the stuff from the week before, though, because our discussion regarding the… the breakout of the core stuff…
**nacho** 10:45 Yeah, I have one question about the
core thing. Have you tested in your own projects?
If it's… linking, or it's working properly with SPM?
that instructor.
**Bryce Buchanan** 11:01 Yeah.
**nacho** 11:01 Yeah, just that, yes.
to validate, right? It's, it's not that they adopted, but just to… To know it's working before.
Moving more along.
**Bryce Buchanan** 11:13 Yeah, I pulled it in in my project, and it seems to be working just fine.
**alexcohen** 11:17 We.
**nacho** 11:18 for it, so… and it works, it works fine as well.
**Bryce Buchanan** 11:21 Groovy.
**alexcohen** 11:23 also tried it out with all our, example, apps and stuff, and, one of them I had to pull in the, the, the whole, the whole one, the, the Swift one, or whatever we call it. But most of them are just core, and it worked fine. Mostly because you added the, you left the, standard,
out exporter, and… What's the example?
**nacho** 11:45 Okay.
**Bryce Buchanan** 11:48 Cool on.
Alright.
Let's, jump into the new topic. So, we've got a request to implement this, metrics filter.
I just wanted it to bring… or I wanted to bring this to our attention, just in case anybody wants to pick this up, because somebody does actually want it, so it might be worthwhile to implement. It's just, one minor feature that we decided to,
delay, or, rather, that we decided to push for the main release of the stable metrics stuff.
So… Please feel free to take a look at that if you're interested.
Alright, data compression follow-up, Ari?
**Ari Demarco** 12:46 Oh, so it was basically if we should create or not a PR with the…
with just copying the code from the data compression, as there's no movement from the author. I already made the PR, it was merged, because it was approved this week.
So, we just have to… eventually do a release with OpenTelemetry and InSPM, and also in CocoaPod, so that's…
Probably that will fix…
**Martin Holman** 13:14 Do we have any licensing issues with copying the code out of it?
**Ari Demarco** 13:17 Yeah, already included in the PR. I know this plan, we have introduced a test file. I know I also mentioned in the compression the Swift that I created, also in the heater, I mentioned to the author. The license is Apache 2.0, so…
It's really cheap that you have made extensions.
On… on what you're doing, and… Mentioned the offer.
**Martin Holman** 13:41 Perfect.
**Bryce Buchanan** 13:44 Cool, maybe we can do a hotfix release for that, and, see how it goes with the new, core dependency.
Do you want to head that up, Ari?
**Ari Demarco** 13:56 Yup, sure.
One, one question, when, when I do that release,
I have some questions regarding the versioning of OpenTelemetry Swift Core.
that… the version will… will mismatch, there's no problem with that? Or shall we make those two versions equal?
**Bryce Buchanan** 14:16 Yeah, that's… that's what I was wondering as well.
**Ari Demarco** 14:21 I don't care if they don't match, to be honest, because I think that at some point, we'll have more releases in one repo than the other, because of the contributions.
**Bryce Buchanan** 14:31 Yep.
**Ari Demarco** 14:32 I think that at some point, there will be differences, and also, I was looking at other repositories to see contribute versus their core.
There are differences, so… I don't have problems with it, just mentioning.
**Bryce Buchanan** 14:51 Yeah, it feels nice to set the core to 1.0. Like, it's a new thing. Of course, it spawned from, you know, like.
The main repo at 1.21, or whatever it's at.
But, I think that it's… that it's nice to have, like, a clean slate, fresh start kind of thing, and, ideally…
the API is not gonna change at all.
and the SDK may have additions to it, but it should stay at, like, 1.0, and I think that might be… I mean, pending any major… I think, yeah, honestly, all of our signals are… are…
pretty, pretty stable now, I think. Blogs, spans, and metrics. I don't foresee any major changes to them, so it should probably just stay at 1.0 going forward.
If that makes sense.
**Alolita Sharma** 15:48 Yeah, that makes sense, Bryce, because.
**Bryce Buchanan** 15:50 Sorry. Typically.
**Alolita Sharma** 15:53 It's… 1.0, even in the collector, you know, when… when, the maintainers were working on this were…
fundamentally set to, hey, you know, what our stability guarantees are, and as long as the, we state them, clearly.
stay at Rondo.
Unless there are new features rolling in where, you know, miners… Coming later.
**Bryce Buchanan** 16:22 Okay, cool.
**nacho** 16:23 Yeah, just what… Summer feedback,
I am a bit concerned about,
About the users of the library, if they use, for example, from the non-core dependency, and it links with the core one?
If we are not pinning the versions, Are we?
**Bryce Buchanan** 16:49 I…
**nacho** 16:50 ethics, or should we?
We, we…
**Bryce Buchanan** 16:56 I guess we're using Sprum.
**Alolita Sharma** 16:57 I mean, we should pin versions, right, Nacho? I mean…
**nacho** 17:01 That… because if not, if we are… it says… if it says from, it will update any…
Version which is not a… Yeah.
a version number, so the first number only. The rest will be updated if they update locally. The thing is.
I am a bit concerned.
If we keep them separated, that…
Someone who depends on the non-core.
And we update the core, they will be getting this, this update,
internally without much control step if they pin it. I don't know. It's something that it happens with Apple libraries, for example, with Swift Neo and those, because they have third-party dependencies, and you don't update NEO, but it changes something on the back.
And you end up with a version that you don't support, for example, with a Swift version or something like that, which is a bit tricky with SPM.
So, I don't know if we should try to keep the same version in both?
Or…
**Bryce Buchanan** 18:06 Yeah, I wonder… just some food for thought, right? Is that… Yeah.
**nacho** 18:10 Let's evaluate what.
**Bryce Buchanan** 18:13 Yeah, I think that in an ideal world, you know, if we are… if we're using this from 1.0 kind of… kind of, you know, thing,
if we're not making any breaking changes, it should be transparent, and it… and it should be, like, if we are releasing valuable additions to the Swift Core, they'll automatically be brought into…
the current version of the main repo without having to do a release, which would be great, right?
Like, ideally, that's how it… how it should work.
**nacho** 18:49 Yep.
**Bryce Buchanan** 18:50 However, if we introduce something that's breaking, then it's gonna cause problems.
And we don't catch it. So maybe what we should do is add
like a… like an actual build and test for the main repo in core to… to check on PRs. I know that's kind of… that… that is not, you know, that sounds kind of annoying to have a upstream, you know, like a downstream, upstream dependency on, like, a PR.
But that's just off the top of my head, that would be one way to kind of mitigate that. I don't know if there's other… other ways.
Does that make sense?
**nacho** 19:37 Yeah, it makes sense for me, yeah, just…
**Bryce Buchanan** 19:40 I don't know if we want to keep that or not, but maybe…
**nacho** 19:42 Yeah, I'm more thinking on… I mean, you're currently using it.
In production, in production code.
So, yeah, maybe we can change it later. I mean, we don't… we are not in a rush in order to update this, but yeah, for everyone to think about it, and what implications it can have for all your deployments.
And so we can update that. We can keep like this, but just think about those changes and what can mean for you in your products, in case it can…
Drink something. So, yeah, I guess…
**Bryce Buchanan** 20:20 Yeah, yeah. Yeah, I think it… go ahead.
**nacho** 20:22 And also thinking what kind of releases we must announce.
Should we announce core versions? Should we announce
Only non-core versions should we announce both?
**Alolita Sharma** 20:36 No, typically, not sure both are announced, and of course, the emphasis is on core, but, the contribib, you know, extended releases are also very useful, because they have integrations that, you know, different users are using.
So I think both… both are very valuable.
To announce.
**Vinod Vydier** 20:59 So, Bryce, you renamed the contract, right, to…
**Bryce Buchanan** 21:03 So there is no conflict, there's only Core and Swift.
**Alolita Sharma** 21:06 There's only core and Swift, yeah.
Yeah.
**Vinod Vydier** 21:09 So the Swift is actually kind of the…
Core plus additional stuff. So, like, the…
**Bryce Buchanan** 21:17 Yeah, yeah.
**Vinod Vydier** 21:18 It's a kind of inverse of the contrape, actually.
**Bryce Buchanan** 21:21 Yeah, yeah.
Yeah, in this way, it's more transparent to downstream users, but we still are able to
Kind of,
satisfy those who are dissatisfied with the size of the main… the main repo in terms of the dependencies. So going… going back to,
Swift Core releases, I think, yeah, for now, maybe we can just, when we are adding PRs, reviewing PRs in Swift Core, just think about how the downstream is going to be affected. And that actually,
unless there's any other conversation on this topic, leads me into this next thing regarding the SIMCOM thing.
updates.
**nacho** 22:07 Yeah. Yeah, and maybe we could have some kind of nightly builds of the non-core, something like that.
**Bryce Buchanan** 22:15 That's a good idea. That would… that would satisfy it, too. That's another solution.
**nacho** 22:20 And yes, just let it cry if it… .
**Ari Demarco** 22:25 It doesn't pass a test, or it doesn't build.
**nacho** 22:28 Yeah, our tests are a bit flaky. Maybe we should also… it will also help us fix those.
**Bryce Buchanan** 22:35 Cool, yeah. Yeah, and that would… that would, that would make it so that we don't have to actually add, like, a dependency into Swift Core on the Swift repo to run tests that way. I think that's a good, that's a good, medium… median, or in-the-middle solution.
**Ari Demarco** 22:52 you can trigger a workflow from the other repo, like, from Core to the official to the OpenTelementary Swift, and when that finishes, it could
make a comment on PRs or stuff like that, or just notify in the old Dell Swift channel that, okay, main is breaking, or OpenTelemetry Core is breaking.
Swift.
Something like that.
Whatever is preferred. All of those are feasible.
**Bryce Buchanan** 23:20 Cool, yeah.
**nacho** 23:21 Yeah, I have another comment about notifications in the channel.
I think there are so many notifications that maybe sometimes are hiding the real, talks that people, or questions that people could have.
I don't know if there is for other channels, maybe we could have another channel just for notifications?
For… Git notifications or things like that, so we can be there and be listening, but for…
Users of the library who might be interested in reading the channel.
It's a bit noisy, I think.
**Alolita Sharma** 24:01 Yeah, you can always have a separate channel for notifications, for sure, not sure. That's…
**nacho** 24:07 Okay.
**Alolita Sharma** 24:07 Pretty standard. And also, you know, as we do nightly builds and more releases, then, it would be…
It would get noisier, I think.
Actually, Bryce, to your… to the point that you were calling out in terms of releases and, you know, how we pin… pin releases, what are some of our assumptions, would it be useful to have some documentation on the site in terms of, you know, what…
some of our… assumptions are here now with, Core and Swift.
Swift Plus, if you will, with the new repo.
**Bryce Buchanan** 24:50 Yeah, I think so, I think that would be valuable.
**Alolita Sharma** 24:58 I mean, I can start a PR, and then, folks can add.
Add to it.
**Bryce Buchanan** 25:04 Yeah, I think that's a good idea.
Yeah, I can, if you send me that PR, I can add my thoughts to it.
**Alolita Sharma** 25:10 Yeah, yeah.
**Bryce Buchanan** 25:10 We can get some… Feedback from… from the other contributors, and…
**Alolita Sharma** 25:15 Yes.
**Bryce Buchanan** 25:15 and such.
**Alolita Sharma** 25:16 Yeah, sounds good, sounds good, because I think documentation is always useful, and as we kind of get into a more really, you know, regular cadence.
Maybe do a blog post on the… You know, project.
blog.
Because, that also helps get the word out. And especially as you're targeting to, you know, say that take core is one daughter with
with, stability guarantees, because I think that's a very big, great milestone.
**Ari Demarco** 25:51 I also find myself to do the… any sort of automation. I already raised ABR to make easier to rerun, like, CocoaPots issues, or…
Cool, cool.
the CI of Open Delemmetry Core.
I can't do the others, so…
**Alolita Sharma** 26:05 Right. Whatever needed.
**Bryce Buchanan** 26:07 Nice.
Alright.
Alright, I'm gonna… I'm gonna actually… Since…
this is relevant to our current conversation, I'm just gonna move this up here. So, I, I,
related to this… the sessions PR, actually, they were referencing semantic conventions in there as… and just hard-coding them, and so I was like, well, that's not okay.
We should have that… we should have that in there, and so that led me down the rabbit hole of updating our semantic convention generation script, which has been a bugbear for a long time.
But that's in… not in here, but in Swift Core.
**Vinod Vydier** 26:54 Generate script, right?
**Bryce Buchanan** 26:56 Yeah, the generate script, and so, it… they… they updated to this Weaver tool, which still uses, Jinja under the hood, but, it, it provides a bunch more, slash different,
methods to the Jinja script to make things
easier or harder, depending on how you look at it.
But, one of the… one of the big changes was, all of the…
Maybe we can… here, maybe I can look at it, on Xcode instead.
So, one of the big changes that was made,
Is they kind of want all of the, all of the different namespaces for the…
semantic conventions into their own files, because there's no more breakdown of signal-based semantic conventions, which is one of the things our old way of doing it was, is, like, you would say, like, I want the span semantic conventions, and that all went into one file, and then the resource semantic conventions went into another file. Now they're just all… they're broken down by their
you know, relevant topic, you know. So…
you know, there's the HTTP semantic conventions, and, you know, as you can see, just, there's a huge list of them. But, one of the things that…
I realized is,
we probably don't want to break the old way that we have, so I'm just going to leave our old documents in here with… so that anybody referencing them in core can still reference them, but, you know, going forward, I think that anything new is going to be in here, but we also kind of need to look at
which namespaces should we actually have in here? Because some of them aren't necessarily relevant to iOS.
Or not iOS, but even Swift, because, like, Linux might be relevant. Then there's some Linux-specific stuff.
Because we can build Swift on Linux, but
I think there's others that may or may not be relevant.
I…
**Vinod Vydier** 29:16 Swift on mainframe?
**Bryce Buchanan** 29:18 Yes, we've done mainframe. There you go.
I don't even know what this is.
It's only one… one thing, but…
So that's not a big deal, but…
So, I got my PR up, take a look at it. Let me know if you think that there's anything…
That should be, filtered out that we don't necessarily need.
Go is probably something we don't need. We don't need a Go memory type.
There's a… there's a Python one in here as well, I think.
So…
**Ari Demarco** 29:59 language and platform specifics that I don't…
I don't think we need, but…
**Bryce Buchanan** 30:03 Yeah.
**Ari Demarco** 30:04 I don't also see any… on having them, they are going to be automatically generated eventually.
So.
**Martin Holman** 30:12 Yeah, I was gonna say the same thing.
**Alolita Sharma** 30:14 Is there a way to actually, add a comment that this is not applicable, even if it is listed?
Because it's free, it can be generated, right? But then, maybe a comment.
**Bryce Buchanan** 30:27 Yeah, I mean, I could definitely, instead of filtering them out, I could just have that list, and it detects it when it's… when it's generating one of those.
**Alolita Sharma** 30:36 Yeah.
**Bryce Buchanan** 30:37 If that aren't applicable, and add a comment in there, that's an option as well.
**Alolita Sharma** 30:42 Because then it stays consistent with whatever, you know, the overall… formatters, and…
At the same time, it's very clear that these things don't apply.
**nacho** 30:55 Yeah, but it's just a name, right?
Yeah.
**Bryce Buchanan** 30:59 Yeah, it's.
**nacho** 30:59 It's just a… it's just a label.
**Alolita Sharma** 31:01 Yes, consistently.
**nacho** 31:02 Zoom.
to just… can simply not use… maybe thinking in another more…
Maybe switch on server functionality, maybe you can be…
It's having some…
non-IOS-related stuff, or non-Swift-related stuff there that's running, and maybe you are monitoring. I'm thinking about, for example, some…
Yeah, some task monitoring that can report what the task below is doing, and maybe it's written in other languages or something like that, so I would keep
All of them, also, as Ari said.
Even if we don't use them, they are small files and should… Compiled quite.
Fast, and probably will be…
hidden, if not used, right? No, they will be public, so they can set them.
In code, right? They could…
Yeah, they could… I think that that will be useful, if we have them, just in case someone needs them.
**Ari Demarco** 32:14 The only thing I would do… I saw your PR, the only thing I think maybe would be worth it is just mark the old ones as deprecated.
**Bryce Buchanan** 32:22 I think I did do that.
**Ari Demarco** 32:24 How about that?
**Bryce Buchanan** 32:25 Or maybe, maybe… oh, maybe I reverted them and I forgot to…
Because I… I was, like, churning on that file, so, yeah, I can add that in for sure. I thought I did, but maybe not. I've got this fly flying into my face over and over again. Get out of here.
Where did that go? I just…
I just,
kind of, here's a demonstration of the new way of doing it. So, like, we have this list of…
Semantic attributes, but now… so I've put it under semantic conventions.
And then we can do, like, exceptions, so the namespaces are broken out, rather than being in a single word. And then I can do message, and then raw value, so…
Basically, you just can put a dot instead of… having that.
Like that. Yeah, so… Although this one's messaged everyone, yeah. So… Or… type, there we go.
Oops.
Yeah, so that's… that's the new way of doing it, so that's cool. I don't know if we want to do semantic conventions, all one word, SIMCOM, or something… something else.
I would like to use attributes, but that's already taken.
**Alolita Sharma** 33:54 Huh.
What, what is, being used in general?
Did you check? I mean, on the other languages?
**Bryce Buchanan** 34:04 Oh, I don't know. Oh, in other languages, they're actually just global, so there's no…
**Alolita Sharma** 34:09 So there's no distinction.
**Bryce Buchanan** 34:11 Yeah.
**Alolita Sharma** 34:12 I see. Yep.
**Ari Demarco** 34:15 I think it's convention is right.
**Alolita Sharma** 34:17 Yeah.
**Martin Holman** 34:18 Yep.
I don't see anything wrong with it?
**Alolita Sharma** 34:19 I agreed.
**Bryce Buchanan** 34:22 Grooving. Alright, yeah, so, I'll make that update to that,
the PR to deprecate the old ones.
I just noticed also that we have some, helper functions that we should also… I can update to use a semantic convention instead.
Although this might not work anymore, because it's not under the…
the same attribute, so maybe I should, make a…
A parent object for them all.
Alright.
**nacho** 34:58 One question, yeah, I didn't look at your PR, but…
We also had resource attributes being generated by the same script.
**Bryce Buchanan** 35:08 Yeah, they're all… they are all under the same thing now.
**nacho** 35:12 Okay. Yeah, there's no more… there's no more, attributes broken down by signal type.
**Bryce Buchanan** 35:21 So,
Okay. Yeah, that was a confusing point for me as well, because I was like, oh, I've got to do the ones for the attributes, or the resources, and then also for the spans, and then, like, there's no… how do I do this with Weaver? There's no documentation on it. And I went and asked in the Slack channel, and they're just like, oh yeah, we don't do that anymore.
It's all just… One big blob.
**Alolita Sharma** 35:44 I see.
**Bryce Buchanan** 35:45 Yeah.
Yep. Okay, so…
**Alolita Sharma** 35:52 Cool.
**Bryce Buchanan** 35:52 Let me go back to the meeting notes.
Okay, yeah, so, that fascination was driven by this PR, which adds a session manager.
Which, looks good to me.
But, yeah, please, please take a look at this PR and make sure there's, there's no issues with it. Otherwise, we can probably merge it.
And then.
**Ari Demarco** 36:27 Worthy.
**Bryce Buchanan** 36:28 I guess we already talked about this one as well, Martin.
**Martin Holman** 36:30 Yeah.
**Bryce Buchanan** 36:31 Which is, yes, let us proceed.
**Martin Holman** 36:33 Sweet. Will do.
**Bryce Buchanan** 36:37 Alright, cool. Any other topics?
Alright.
**Ari Demarco** 36:47 So just, just to be clear, so I…
I should create a new version whenever we want, with new OpenTelemetry Core, and a version in OpenTelemetry Swift.
**Bryce Buchanan** 37:01 If there's no changes to core at the moment, then there's no reason to do, a version release of Core. Because right now, the package in the main repo is at core or 1.0.
And,
Yeah. If you do a release in the main repo, then it'll… it should pull down whatever's in core.
**Ari Demarco** 37:26 Okay.
Final question.
OpenTelemetry Core now has 1.0.
Mmm…
But if we try eventually… if we eventually move to 2.0, or something like that, we'll probably have some problems when trying to push CocoaPods versions, because we already have OpenTelemetry API.
So…
**Bryce Buchanan** 37:52 Right.
**Ari Demarco** 37:53 Continue from two point.
02 and upwards.
In the new OpenTemmetry core?
**Bryce Buchanan** 38:00 Yeah, that… that… That's a good point, yeah, that does throw a wrench in the idea of a 1.0, so maybe we do need to start using,
Using just the version from the main repo in core as well.
**Ari Demarco** 38:14 I can start with 2.1, and that's… Basically, if you guys want.
I don't know if you want to also include… if… now that it's going to be a minor version, maybe you want to include the semantic attributes PR?
I can't wait for that.
**Bryce Buchanan** 38:32 Yeah.
**Alolita Sharma** 38:33 That's a great idea.
**Bryce Buchanan** 38:36 Yeah, let's go with that. Yeah, so let's do a Swift Core release and bring the, version…
**Ari Demarco** 38:42 2.1.
**Bryce Buchanan** 38:43 Yeah, up to… yeah, here's the thing, is they're not… I don't want to lock them, right? So, we don't necessarily need to always do a core release when we do a main repo release.
**Alolita Sharma** 38:56 Yeah, that's right.
**Bryce Buchanan** 38:57 But just to satisfy the needs of CocoaPods, we should probably at least bring SwiftCore to the version
that it was at when it got, separated out, so that we don't have any weird issues with CocoaPods. Because CocoaPods is, you know, it's gonna have a 2.0 version, 2.x version of API and SDK, and if we start releasing under the 1.0 version, there's gonna be a really weird versioning confusion going on, so…
Alright, yeah, let's… let's…
**Ari Demarco** 39:29 Now that I'm talking about that, I find… I think I realized that I have to also change the way we bump specs in… in…
In OpenTelemetry Swift?
as probably OpenTelementary API and SDK will have different versions than the others.
So, I'll do that change too, on OpenTeometry Swift.
**Bryce Buchanan** 39:49 Oh, yeah, because, yeah, because you can specify from, like, a from in, in CocoaPods as well, yeah. Yeah, so we should probably do that as well.
Okay, cool.
**Ari Demarco** 40:05 I'll do that.
**Bryce Buchanan** 40:06 Thank you.
**Alolita Sharma** 40:06 Ari, as you, as you're kind of defining the release, you know, assumptions, it might be good to also note them in a README or something, because as you get, you know, maybe
If we are lucky enough to get men, you know, interns or others contributing, they can actually help with the release process in the future.
**Ari Demarco** 40:30 I think we can all include that in the… that, issue slash PR.
**Alolita Sharma** 40:34 Yeah, sure, sure, sure. Sounds good.
**Ari Demarco** 40:37 Have a single source of truth for all.
**Alolita Sharma** 40:39 Yes, agreed.
**Bryce Buchanan** 40:48 Awesome.
Okay.
If there's, no other topics, I think that we can call it here.
**Alolita Sharma** 40:59 Alright, coolness.
Thank you, everyone.
Y'all. Chat later. Thank you. Bye-bye.
**Vinod Vydier** 41:05 Good weekend. Bye.
