SIG: Swift SIG
Date: 2025-08-28
Duration: 50 minutes
============================================================

## Zoom Recording Transcript

**Bryce Buchanan** 01:01 Hey, Ari.
**Ariel Demarco** 01:04 Hey, Grace, how are you?
**Bryce Buchanan** 01:06 Good, how are you doing?
**Ariel Demarco** 01:08 Not too bad. … Was trying to fix… Well, to improve, I believe, the workflow for the release.
I'll probably be talking about that, like… I want to… make it easier to rerun all the CocoaPot stuff, that it's failing a lot.
**Bryce Buchanan** 01:27 Yeah.
I mean… Yep.
**Ariel Demarco** 01:40 Cocoa butts.
Bob….
**Bryce Buchanan** 01:43 I mean, this….
**Ariel Demarco** 01:43 You know, age.
**Bryce Buchanan** 01:44 This is exactly why I didn't want to support Cocoa Pods.
**Ariel Demarco** 01:49 Yeah, I know.
I know, I need some bummer. … I was going to ask you if you could add me afterwards to the trunk.
**Bryce Buchanan** 02:00 To the… Oh, yeah, for sure. … I… yeah… I'll have to look up how to do that, but I can… I can add that to you. Let me add a reminder for myself.
**Ariel Demarco** 02:13 Yeah.
… Oh, is he not shrunking? Who am I?
I'm using it.
Then I got a request for you, but… From… it's, like, internal, so I'll probably be given.
Brother.
**Bryce Buchanan** 02:38 Okay.
**Ariel Demarco** 02:42 I'm just so lucky.
Let's go.
**Bryce Buchanan** 03:01 Hey, Alex.
**alexcohen** 03:04 Hey.
**Bryce Buchanan** 03:07 How you been?
**alexcohen** 03:10 I have been pretty good. And you?
**Bryce Buchanan** 03:13 Doing well.
**alexcohen** 03:16 Sorry, this is my first meeting with this new laptop that I just got, so everything.
**Bryce Buchanan** 03:22 Gotta… where's all… gotta get it configured right.
**alexcohen** 03:26 Yup.
**Bryce Buchanan** 03:30 Am I sharing the right thing? What am I doing?
Stop.
There it is, okay.
There we are. Will this work? No? Yes? Okay.
Good deal.
**alexcohen** 03:59 Not a big attendance today.
**Bryce Buchanan** 04:01 Yeah, it's kind of quiet, isn't it? Oh, Ari, take that spot.
Okay….
**Vinod Vydier** 04:49 Good morning.
**Bryce Buchanan** 04:51 Maybe none.
**Ariel Demarco** 04:54 Maybe not.
**Vinod Vydier** 04:56 Yay.
**Ariel Demarco** 04:57 Awesome.
**Bryce Buchanan** 05:20 Okie dokie. Let's, let's get started here. So I'm just going through the topics from last week. It looks like you put the compression follow-up in the new topic, so we'll just skip that one. Repository division. So, we do have a new repository created. It's not complete just yet.
But, I wanted to hear about, … Alex, if the package if defs led anywhere valuable.
**alexcohen** 05:49 Yeah, so, yes and no, I mean… It works if you have, like, for if defs, no. So, macros or anything like that, like… didn't work. I explored the environment variable, now that works, but you have to explicitly pass it in, like you, like you mentioned. I was hoping that, like, I could call… I could call set environment in a parent package.
But they all have their own, sandbox, and that goes for the environment, as well as any files that are there, so they can't, like.
talk… they can't look in another file system or anything like that, they all have their own sandbox. So, there's basically… you basically can't get outside of your own little… little repo. So, that didn't work, unfortunately. It's too bad, because, like, it does work. It… but it just doesn't work in the way too. ….
**Bryce Buchanan** 06:47 Okay, that's too bad.
**alexcohen** 06:49 So I'm… I'm sort of the… the other thing I wanted to do, like, I asked around in the community to see if anyone, had any ideas. They were talking about, repository… what are they called? Like, groups of repositories that you can create on your own. I can't remember what they're called.
Give me a second.
Maybe I can find it really quickly… probably not. … But, oh yeah, Swift Package Registries is something that someone mentioned, but it seems, like, too complicated for what we want to do. We're better off just doing something else. They mentioned that AWS uses it and things like that, but, like, we really don't need to go that far, I think.
Let's see what else. So, I think… I think we're basically back to square one, where we… and it's… we're better off that way anyway. I think we need to split the… the repo up into pieces that make sense to go together. If it's… if we follow the spec, that's great, but it feels like because of SPM, it might be a little bit harder to follow the spec exactly like the spec says we should do it.
So, yeah, I even started, like, removing smaller pieces, well, bigger, smaller pieces, like gRPC, but that still doesn't remove enough, like, it doesn't… it doesn't… get us to a place where we have the API and SDK that really don't have any other dependencies or any other large dependencies. So we always end up with a bunch of Swift things anyways, whenever we keep any of the larger things, like Prometheus or gRPC or anything like that.
**Bryce Buchanan** 08:33 Right, anyway. Okay.
**alexcohen** 08:35 So, I still… my recommendation, I don't… I don't think it's the one that everyone agrees upon yet, but my recommendation is still to try and, do a 100% split from, like, a no-dependency API SDK, Repository, and then the rest, we can try and fit that into whatever repositories, we feel fit best.
**Bryce Buchanan** 08:59 Okay. Yeah. I'm… yeah, I'm… the… yeah, the way I feel about it is, like, I kinda… I kind of want to do it that way, too. There is… there are good reasons not to do it that way, you know, per the… Per the, the, spec.
But also additionally, like, if anybody needs, like, like, that solution, just splitting everything out from the API and SDK, that's still, that only really helps those who are just dependent on, like, the API or the SDK, and most people who are going to be using this need gRPC, or they need some OTLP exporter.
And so if we only just move that stuff into another repo, then we're just back at the same problem, where they have to pull in all the dependencies from that repo now.
So, yeah, I wonder… I wonder if we should really just audit… yeah, I guess that's the problem, though, is, like, we need to audit exactly which dependencies and packages are causing the bloat, and then move those ones explicitly out, and then everything else can probably stay in.
But….
**alexcohen** 10:15 Yeah, we could definitely do that as well. I mean, that wouldn't be too difficult. I started looking at that this morning, by, like, just moving GRPC out, but then there's still a lot of other things… mentioned the… I think, the Prometheus target, and a couple of other targets, but, like, if we want to just move those ones out, it's… I mean, we can… we can do that We can definitely do that as well. I don't… I don't see any issues with.
**Vinod Vydier** 10:41 So even if you don't have Prometheus and Jaeger, or, you know, the stuff that was there in the early spec.
the… I mean, which is, I think, now optional. We still need the… The OTLP exporter, right? The SDK?
**alexcohen** 10:58 Yeah, and what dependencies does that have?
**Vinod Vydier** 11:01 Yeah, it does have gRPC.
**Bryce Buchanan** 11:02 Yeah, I think… I think that if we broke out the gRPC exporter, that would be good, and we could leave the HTTP one, because I think that only really depends on, the Apple libraries, so I think that would be a good compromise. I think there's also, like, Swift Atomics might be a really big package as well.
I can't remember, I was looking at them yesterday, but, yeah, maybe I can, … Do an… do, like, do a check on the sizes of everything, and create a ticket that, kind of breaks out.
where all of the, where all of, like, the memory, or the, usage is in terms of, like, the sizes. And then we could discuss that in that issue, decide which ones we want to break out. So right now, the… I hate this, because the repository that we have made is OpenTelemetry Swift gRPC.
So, maybe… maybe for now, we can just put the gRPC stuff in there, and then… like, maybe we should just put the really big stuff into their own repos each, because… I don't know, I could go rename the repo again, and just, like, make it, you know, OpenTelemetry Swift dump or something, like, I don't… but, … Yeah, maybe we should just, think about adding, you know, an additional, you know, additional repos as well.
because it's the same amount of work as me going back and renaming the repo again anyway, because I have to go update a bunch of Terraform files and, you know, permissions and stuff, so….
**alexcohen** 12:43 So, if we were to go that direction, like, to me, I would… if we're… like, that… we could end up with a lot of repos, right? If we're gonna… one for gRPC, one for something else, another one for something else, and, like, it's… it… I… I don't know if that would be… that would be the best option in… in my opinion. It seems like it would be… It would be a bit complicated to maintain and to, you know, to get to a working state.
**Bryce Buchanan** 13:12 Yeah, I agree that that's a possibility. Why don't we… why don't we, look at who the… which packages are the major offenders, and if there's, like, a simple way we can break them out, like, not to… like, two additional repos instead of, you know, or… or if we want to just put everything in one, I think that really depends on how many there actually are, like, in terms of the big offenders. I think there's only really two big packages, like, at least 2 external dependencies that cause most of the bloat.
So….
**alexcohen** 13:47 So, what I'm… what I'm looking at is, like, let's say, and this is what I saw this morning, let's say we move gRPC out, right? Because it's one of the larger ones. Then there are a lot of other things that depend on gRPC that we need to move out as well. Do we move those out into… the gRPC repo, but we can't call it the gRPC repo, because those things are not gRPC, they just depend on it.
Right? And we don't want the main repo to depend on the gRPC one, because if that happens, then we've changed nothing.
**Bryce Buchanan** 14:18 Yeah, exactly. Yeah, I think that in terms of the naming, … Really, the only thing that GRP… isn't it just the OTLP exporter, gRPC exporter that depends on gRPC, or is there… is Prometheus also….
**alexcohen** 14:35 No, I think there were a couple of them, I can't remember exactly which ones, but there are a couple of them, but then there are also some executables that depend on them as well.
on….
**Bryce Buchanan** 14:47 Those are just examples, though.
**alexcohen** 14:50 Yeah, we still… but we still need to move them, right?
**Bryce Buchanan** 14:52 Yeah, yeah. Yeah, I think that any… I think that the idea is anything that's dependent on gRPC can go into the gRPC repo.
**alexcohen** 15:00 Yeah, but… okay, yeah. I mean, that… that sounds a little bit, weird to me, it's the… a naming, and, like, the naming is… we're talking about the naming because it makes… it sort of decides what we put into it.
Right? Based on the naming, and I saw someone say something like an examples repo, or… or whatever, something like that. Like, I feel like the naming is going to be important to understand what we can move there, what we can't move there. Because if it's called gRPC, like, there… we're going to end up creating other repos for other things that we need to move out as well.
**Bryce Buchanan** 15:36 Yeah, yeah, depend… yeah, … So one… one second here… Mmm.
**alexcohen** 15:45 So let me ask this, to go back to the original, the original proposal again, like, if we're making something better for a bunch of people, right, and for some people, nothing will change, or basically nothing will change, it's basically adding another repo.
Right? Which, for another package, which is not… which is not complicated. … isn't that… isn't it better to get something like that out there and working than to spend a lot more time figuring out exactly what the pieces should be, and how many repos we should have, and things like that? I'm just trying to see if… There's a way to, … To… to get the… to get this out there a little bit quicker.
**Bryce Buchanan** 16:33 … Oops.
Well, I guess the… well, this goes back to the naming thing, though, is, like, what precisely… Okay.
Okay, oh boy, now I've done it. I guess, like, what would we call… like, are you proposing that we just move everything into a separate repo, or…?
**alexcohen** 17:04 I'm saying, like.
**Bryce Buchanan** 17:06 Find the offenders and move those into a separate repo.
**alexcohen** 17:09 I'm saying we… we use the PR that I put up to… that basically has the core of… open telemetry, which is the API and the SDK. The others are, like.
They're sort of core, but not that much, because you don't absolutely need them. But you can't work without API and SDK, so that would be the repo that we have.
no, no changes, and the other repo, where we put the rest for now, it would be non-core or something like that, whatever, whatever we want to call it. I don't think extras works, it makes it feel, like, unimportant, but, like, non-core or something, something like that.
**Bryce Buchanan** 17:48 I mean, wouldn't it be more appropriate to move the API and SDK into something like Swift Core instead? I think that makes more sense than having, like, a non-core.
**alexcohen** 18:00 I agree, but I was just trying to keep that naming the same, just to not mess with most people.
Wait.
**Bryce Buchanan** 18:10 Well… I mean, if you are dependent on OpenTelemetry Swift.
That would be dependent on core, so… It would potentially be a transparent change, wouldn't it?
**alexcohen** 18:26 Sorry? What do you mean?
**Bryce Buchanan** 18:28 Also, so… We have OpenTelemetry Swift right now. If we pull out and make a core, OpenTelemetry Swift would depend on core, so anybody using OpenTelemetry Swift would automatically just be….
**alexcohen** 18:41 That works, that would work great as well.
**Bryce Buchanan** 18:43 That might, that might be it.
**alexcohen** 18:45 Great idea, yeah.
**Bryce Buchanan** 18:45 Yeah, that might be a better way to do it. I'm just looking at the packages here.
… yeah, I'll just share my whole screen.
**alexcohen** 18:58 So, if you look at my PR, that's basically the split that's there. Like, it's 100% updated to work like that.
**Martin Holman** 19:07 So, Alex, my only question about that is, like, if… if we split it out, like you say, API SDK and everything else.
Can you define, like, who the people are that it will actually help? Because it feels like, without any exporters.
If that's still the case, I haven't double-checked your PR again, but without even the HTTP exporter, 100% of the people will need to include Contrib anyway, and so it really… like, who are the people you have in mind that that would help by getting it out?
**Bryce Buchanan** 19:39 Yeah.
**Martin Holman** 19:39 That would help me to understand.
**alexcohen** 19:41 Okay, well, one of them would be the company I work for, obviously, and Ray.
**Martin Holman** 19:47 use any exporters? Like, how do you use the API and the SDK?
**alexcohen** 19:51 Maybe Ari can… I don't know exactly, but I know we don't use any of those. We have our own, and if anyone wants to put other exporters in there, they can… they can just plug them in, and we'll use those as well. But ours… inter… the internal ones we use are not, in the OpenTelemetry, repo.
Yeah, like, you only….
**Ariel Demarco** 20:21 No, no, the only other thing we use, we use exporters, but mostly on the React Native side of things. But again, it's an opt-in thing that you might want to use, or may not.
**alexcohen** 20:37 Yeah, so, basically, we… we have, we have our own, And there's another company that I shall not name the name, I guess, because it's caused issues in the past that doesn't seem like they would need them either.
Other than that, I don't know.
**Martin Holman** 20:57 So what… what do your exporters do, then? You don't accept OTLP as a….
**alexcohen** 21:04 So, we do if customers want to. So, basically, if they want to, they can just plug it in.
But at that point, that's their choice.
**Martin Holman** 21:20 Hmm.
I mean, I don't feel… I've… yeah, I feel a little conflicted about… optimizing for… one or two companies benefit when they're not supporting OTLP out of the box.
There's my only… I mentioned that.
**alexcohen** 21:36 Yeah, no, that's… that makes… that makes total sense. I'm just, you know, I'm just thinking that if, I'm a little bit new to this, and I know two companies already, and there are probably more out there as well, so, like, it's probably not just us two, and that's it.
**Martin Holman** 21:52 Shouldn't we be, like, the whole point of… of, you know, hotel is to encourage vendor independence, and if that… to that extent, like, encouraging vendors to accept OTLP as the standard protocol seems like the same goal.
And if we're going down the path of, like, encouraging every company to accept their own proprietary format and not the standard that exists. That seems a little against the goals of the hotel.
**alexcohen** 22:26 Yeah, can't argue that.
I mean, I feel like the… the product, the OTEL product, is not built in the way that, like, if we really wanted that, we would put it directly into API or SDK or something like that, and not allow it to be… to not be used.
I think, because otherwise we're just… we're just giving… given the option to not use it, which is basically not really what we want here, right?
We want people to use that.
**Martin Holman** 23:00 Yeah, which I think… was it a couple weeks ago? We were… was it… Anod maybe was saying that having the HTTP exporter is, like, part of the spec, is to have it, and… Cool.
**alexcohen** 23:12 So… yeah.
Well, I was… I didn't mean, actually, in the core, like, if it has no dependencies, then perfect.
It's the problem that I'm trying to solve, is to… to drop the dependencies from… that get automatically downloaded, through SPM.
So that's… that's why I want to do the split. My first… my first try at the split kept everything that didn't have dependencies, which did keep a lot of the exporters, in… in the core.
Which is the way… the way I sort of originally wanted it, and I think it fit better with, with what OTEL wants.
**Bryce Buchanan** 23:58 Okay.
**Martin Holman** 23:58 Yeah, I mean, I think… I would only… I would only strongly object if you couldn't take the… The… the primary package.
And not export.
HDB, OTLP, … stuff. If we can, then….
**alexcohen** 24:16 No, that's… that makes total sense. So… so, Bryce, can you just bring up that exporter, see what it depends on?
**Bryce Buchanan** 24:25 Which one?
**alexcohen** 24:26 … which one, Martin, you say? Which one? Who's? Who's? Yeah.
**Martin Holman** 24:31 I think… is it… Vinod probably knew better, but I think it… is it HTTP Protobuff? I forget, whichever one is, like, required as part of the spec, I think.
**Bryce Buchanan** 24:39 Oh, yeah, the, the OTAL P ones. So… we have the HTTP exporter here, and that just depends on data compression, which is negligible in size.
**alexcohen** 24:54 Okay.
**Bryce Buchanan** 24:54 like, less than a megabyte, I think.
**alexcohen** 24:57 We were talking about bringing that in, right?
**Bryce Buchanan** 25:01 ….
**Ariel Demarco** 25:01 Yeah, but it also depends on… on common. On common, that depends on gRPC.
**Bryce Buchanan** 25:08 Oh, common doesn't depend on gRPC, does it? It shouldn't. Yeah, see, it depends on protobuf.
**Ariel Demarco** 25:15 Pradova, sorry, Maba.
**Bryce Buchanan** 25:17 Yeah, so, I was actually just fiddling around, I don't know, can you… you can see my Finder window here.
So… So the real big offender is Swift Neo.
And that is 87… 87 megabytes there, and that is… that is, … … Prometheus.
Prometheus depends on Swift Neo. The other… the issue is, though, is that we have some tests that depend on NEO for some reason. I don't know why.
That seems… unnecessary.
Yeah.
**Ariel Demarco** 25:54 You're gone.
**Bryce Buchanan** 25:55 There's… maybe there's some useful stuff in there.
But maybe we can fix that.
The next largest issue, I think, is… is the protobuf. So, if… if… If we remove the Swift Neo stuff and the Protobuff stuff, then we'll be left with 20MB download.
**Martin Holman** 26:16 But we need the protobuf stuff, right?
**Bryce Buchanan** 26:17 Yeah, and the protobuf stuff adds… well, I mean, yeah, that's… so that's the thing, yeah. The gRPC depends on… or… and HTTP depends on protobufs.
the OTLP exporters, and so that.
**Martin Holman** 26:29 That biggest part of F just by itself, if we….
**Bryce Buchanan** 26:32 itself is… it looks roughly, 30 megabytes.
**Martin Holman** 26:36 Right.
**Bryce Buchanan** 26:41 And then, yeah, these other two are negligible. So it's really these Swift Neo and Swift Protobuff are causing the… the largest, … issues.
So… I mean, it might… it might be… if we can fix the dependencies in our tests and not use NEO there.
If we broke out the Prometheus exporter into its own repo, and then the OTLP into its own repo, then we'd have a pretty slim… main reason.
**Martin Holman** 27:12 The gRPC, you mean, not a GRP.
**Bryce Buchanan** 27:16 Oh, yeah, the GR… well, it's… well, the HTTP exporter depends on… oh, wait, no, does it? Hold on.
**Vinod Vydier** 27:28 So everything depends on the protobuf. You can keep it separate and, you know, you can compile it outside, you can have it as a separate repo.
But once it compiles and builds those, … Swift files, you need that, right?
**Bryce Buchanan** 27:42 So, the HTTP exporter depends on the core, the common OTLP, which depends on the protobufs. So if we were to break out protobufs, we would need to break out all of the OTLP exporter stuff.
**Martin Holman** 28:04 Yeah, that….
**Ariel Demarco** 28:05 No, no.
**Martin Holman** 28:06 Not ideal.
**Bryce Buchanan** 28:07 Yum.
Not ideal.
**Vinod Vydier** 28:10 Yep.
**Bryce Buchanan** 28:20 So, with Protobuff in there, still, you know, it cuts the dependency in half, like, the size in half, but… Still pretty big.
**Martin Holman** 28:30 But, like you were saying, Alex, half is better than… than… 100%.
**alexcohen** 28:37 What's that, sorry?
Who's that?
**Martin Holman** 28:40 Oh, sorry, you were just, advocating before for, like, let's get something that helps people, and half is better than 100%.
**alexcohen** 28:48 Yeah, yeah, no, I, like, forward progress is better than none, I would say. I… personally, I prefer us to move forward and get things out there than, Then just look into it for a month or two.
But, you know, that's just me. It's… if it's not to everyone, that's perfectly fine as well. I can… I can wait.
I do….
**Martin Holman** 29:13 Okay, well then, so is 50% good then? We should… sounds like you'd be forward for moving forward with that?
**alexcohen** 29:20 I… I am a board of anything that moves us forward. But just… just to go back, so yeah, I would… I would be. But just to go back a second, what… I like the idea of… keeping it as is and moving the core out and having Swift depend on the core. Is that… is that an option for… for anyone? I don't know if we totally dismissed that option or not, because it's sort of… Moves us forward where we can get a full package with no dependencies, like some of us may need, and then, and it gives… but other than that, we just stay status quo.
for everyone else. Which….
**Bryce Buchanan** 30:01 I was going to offer that, yeah. I think that that's a good first step right now.
And it at least provides some separation of the… of the packages, and provides some people a solution.
Of course.
**alexcohen** 30:18 It helps with the, it helps with the maintenance problems that Nacho was worried about as well. Well, we were all worried about them, that, like, … the… the main package will depend on the core, so the maintenance of that is… is sort of… is a little bit easier, I guess, maybe?
**Bryce Buchanan** 30:34 Yeah.
Yep.
Cool. Yeah, and maybe in the future we can look at separating out the Prometheus exporter into its separate repo, just due to the size of its dependencies, as well as the OTLP exporters.
I think that, that, … you know, no… nothing solid yet, but we can discuss that later if… if we think we need to do that. I think priority… priority in terms of after setting up Swift Core would be to separate out Prometheus, because that is… that's the major offender here.
**alexcohen** 31:09 Is that….
**Ariel Demarco** 31:10 So, the idea would be… Oh, sorry.
**alexcohen** 31:14 I was just gonna go back and ask Martin if that is something that he would be agreeable to.
**Martin Holman** 31:23 I heard your words, Bryce, I'm not sure that I, … so I maybe missed that proposal initially. I'm sorry, I joined a little late. So the… the idea would be to have another… Have another repository, but the… the OpenTelemetry Swift repo would depend on that instead of the other way around, is that…?
**Bryce Buchanan** 31:44 Yeah, the idea is, is we create an OpenTelemetry Swift core, which would contain the API and the SDK only.
And the reason why I like that idea is because, for the standard user who's using OpenTelemetry Swift, it should be a transparent change.
They might need to… import Swift Core instead?
Somewhere, but they won't have to muck around with, with the package, necessarily.
**Martin Holman** 32:18 Right.
Yeah, I… I… Yeah, that seems fine.
**alexcohen** 32:24 Well, actually, we'll be able to put, like, an export Swift Core somewhere, or a hotel core in… the later one, like, just put a file with that in it, and no one will have to do anything, it'll just work.
**Bryce Buchanan** 32:37 Yes.
Yeah, yeah, so that, yeah, that's a good point. So yeah, we could… we could make that change completely transparent to any users of the existing repo right now.
Which I think is, a great way to… Reduce the size for people who are dependent on only those two things?
… Who are the noisiest?
Complainers?
**Vinod Vydier** 33:03 I'm not….
**Bryce Buchanan** 33:05 I'm not… I'm not calling you out, Alex, no.
**alexcohen** 33:08 Sure, you won't do wrong.
**Vinod Vydier** 33:10 So, Bryce, just… so just to be clear, Bryce, in the hotel core, we'll only have the API and SDK and… the OTLP HTTP exporter.
**Bryce Buchanan** 33:23 Say again, Vinod, I missed the first part of what you were saying.
**Vinod Vydier** 33:26 So, I was saying that, so what you guys are proposing is, OTL core, which has the, you know, the basic dependencies, the PI SDK, and … It'll also have the OTLP HTTP exporter.
That's it.
**Bryce Buchanan** 33:44 No. It'll just have… it'll just have, the API and SDK.
All the… all the other, all the other libraries are gonna remain in OT… OpenTelemetry Swift.
And maybe in the future, if, … if… you know, I'm sure there's gonna be other… other people who don't… like, it's like, I'm not using Prometheus, right? I don't know of a lot of people who are using Prometheus.
….
**Vinod Vydier** 34:14 Yeah, so I think this is one of the things that, I don't… We did talk about this.
when Alulitha was also here, because that was one of the part of the spec, the early… days of the spec, that you had to have a… open source, … Exporter, that is… You know, beyond the… the basic OTLP exporter, right? So, Prometheus and Jaeger… Prometheus for metrics and Jaeger for Traces, which is there in pretty much all the other languages. But I think she mentioned it is optional now.
This is not required. So we can't… Yeah, we can remove the Prometheus and, … Jaeger, because it's optional, but I don't think we can remove, or we should remove the… OTLPHTTP exporter.
**Bryce Buchanan** 35:03 I mean, nothing is getting removed, it's just not living in the same repository.
**Vinod Vydier** 35:08 No.
**Bryce Buchanan** 35:10 … So, … I think, I think, well, and that's the thing, is anybody who's using those, like, GRP, or, you know, using OTLP, it's… they're still gonna be using OTLP, We've just extracted the core stuff into its own repo, and so they'll still be depending on the same repo that they've always been depending on.
**Vinod Vydier** 35:36 And if they want to use the OTLP HTTP exporter, they have to use this… Extra.
**Bryce Buchanan** 35:42 No, no, no, they'll just… we'll leave that all in, in OpenTelemetry Swift now.
I was just saying, in the future, if… if… Honestly, I think that we should still look at moving Prometheus into its own repo, because it… it is a big… like, these… these dependencies it uses is 90 megabytes, right? Like, that's a huge… That's a huge addition to the… to the… you know, everything else is, like.
**Vinod Vydier** 36:11 Yo.
**Bryce Buchanan** 36:12 It's… it's… Not nearly as big as that, so….
**alexcohen** 36:14 So, the change that we're talking about now is, Renad, is… so we're looking at it the other way around. Instead of creating a new repository with all the extra stuff.
we're creating a core repository, with only the basics. Only the basics. Like, the stuff that… the data models and whatever, all of that stuff. And….
**Vinod Vydier** 36:39 Heard of a field.
**alexcohen** 36:41 No, no, no.
No, no, no.
**Martin Holman** 36:44 Yeah, I think the miscommunication is the basics.
The… the basics that….
**alexcohen** 36:48 API and SPJ.
**Martin Holman** 36:49 I and Vinoda are talking about, include the protobuf, because that is a basic part of….
**Vinod Vydier** 36:54 Yeah, so the output of the protobuf would be the basics, right?
**Martin Holman** 36:58 But… I… I think I can… I can see that this is a compromise between… I feel like Vinod's on one side, I'm, like, probably closer to Vinod than… than Alex and Bryce, but, like.
This feels like a compromise that hopefully we can all agree on.
And I definitely see your point, Venod, like, I would prefer that we had a package that had the basics defined as the protobuf as well, but I think that's… Maybe a bridge too far for us all to agree on.
**alexcohen** 37:32 I mean… Not… It's… it's not really, like, if… If we all feel that having a dependency, having the Swift Protobuff dependency is core.
to OpenTelemetry, then, I mean, it should probably be in there. I… I guess I just, maybe… maybe I question, the spec. In that case, that's what I'm questioning. If we have, like, if the spec says it needs to be protobuf or something.
And if it's… if Protobuff isn't there, then you're not… fitting in with the spec, then I'm… the spec is what I'm disagreeing with, I guess.
Because there are people that seem to use it in a different way.
And don't use that part of the spec, but are stuck with it anyway.
**Martin Holman** 38:22 Yes.
I guess, yeah, maybe… I don't know what SIG controls that, but maybe… I feel like that's, not… not, not within our… within this discussion, so we have to change.
**Bryce Buchanan** 38:34 Oh, so, I guess I'm not necessarily against keeping the OTLP exporters in Swift Core, but here's the problem right now that I have that might cause, quite a bit of… churn, just in terms of making it happen. It's these… it's these neo-dependencies on the protocol exporter tests.
So, if we were to… if we were to bring the gRPC… if we were to bring these things into Core.
we would need to remove these dependencies, and I don't know What, how embedded those are.
You know what I mean?
**Martin Holman** 39:14 So, so maybe we need, we need, we need someone to, like, take on the investigation of that.
**Bryce Buchanan** 39:18 Got it.
**Martin Holman** 39:19 Stronger database.
**Bryce Buchanan** 39:20 ….
**Vinod Vydier** 39:21 Bryce, we should, … we should separate the gRPC and protobuf, because I think gRPC does have, … You know, a lot more… That's a much bigger package, right? So….
**Bryce Buchanan** 39:33 It's… it's… honestly, it's not that big.
**Vinod Vydier** 39:36 … compared to the….
**Bryce Buchanan** 39:38 the other ones.
**Vinod Vydier** 39:39 I wouldn't the book.
**Bryce Buchanan** 39:41 GRPC Swift.
Oops. Oh, no. I clicked it too fast.
… GRP Swift… gRPC Swift… is… 5 megabytes.
**Vinod Vydier** 40:00 Okay.
**Bryce Buchanan** 40:01 Yeah, for some reason, I thought it was much bigger. ….
**Vinod Vydier** 40:04 What about Protobuff?
**Bryce Buchanan** 40:06 Protobuff is a little larger.
But, that one's 33 megabytes, but the HTTP exporter depends on the protobuf, so….
**Vinod Vydier** 40:19 Yo.
**alexcohen** 40:22 And, just to clarify, my position, at least, on this, it's not… like, the size of the downloads is not exactly, the problem.
that I was seeing. It's the size plus the number of dependencies that we need to go get, because for every dependency, regardless of the size, there's a lot of work that package manager and the systems need to do to maintain it and cache it and all of that. So it's not just the size, so just saying 86 or 10 megabytes or whatever, and we can keep it or not is not… Like, doesn't totally fulfill what we're… what I'm looking at as… as the issue.
**Bryce Buchanan** 40:58 That's fair, yeah. The, the, the other… the other, party, that's concerned about this is… is specifically in CI, though, so they can't… they can't cache The, the dependencies.
And I think I've heard a couple of different, you know….
**Martin Holman** 41:20 vacation?
**Bryce Buchanan** 41:22 What's that?
**Martin Holman** 41:23 Why can't they cache the dependencies?
**alexcohen** 41:25 Bye.
**Bryce Buchanan** 41:26 I don't know, I don't know what their CI is.
**alexcohen** 41:29 I mean, we cache them for… at least for reuse on the run of CI, and we do a lot with the… in the same… in the same run, but….
**Bryce Buchanan** 41:38 Yeah, it's true. There probably are solutions to have your CI be more efficient.
… Yeah.
**Martin Holman** 41:46 So, like, that's, maybe a personal problem for a little bit.
Yeah, that's fair.
**Bryce Buchanan** 41:52 That's fair. But, so, alright.
I think that, … let's look to bringing the OTLP stuff into core. Let's… right now, let's just bring… let's create the core, bring the API and the SDK into it.
that'll be good. And then in the future, once somebody can figure out how big of a problem these neurodependencies and the tests are, then we can bring OTLP into the core as well.
**alexcohen** 42:24 So is Neil only in a test?
**Bryce Buchanan** 42:27 No, NEO is also, required by Prometheus.
**alexcohen** 42:30 Okay. Okay.
**Bryce Buchanan** 42:32 Yup.
**alexcohen** 42:32 It's a bit, yeah.
**Bryce Buchanan** 42:33 But I don't… yeah, so… but it's also in the tests for some reason, I don't know why.
**alexcohen** 42:38 There's probably… well, Prometheus is not… it… like, this test target doesn't depend on Prometheus. No. So, maybe… maybe they're doing something else.
**Bryce Buchanan** 42:48 There's some… yeah, there might be something of convenience in there.
**alexcohen** 42:51 Yeah, but regardless, like, if they're importing it, and… or if they need it, and Prometheus needs it, then as long as Prometheus needs it, like, it's not going anywhere.
**Bryce Buchanan** 42:58 Exactly, yep, yep.
Yeah, and… and that's… that's why, These should just stay in the… in the Swift repo, the OTLP non-core repo, or rather, the OpenTelemetry Swift non-core repo, because, this is probably going to require test rewrites.
And just in terms of, like, getting something out more quickly, as you were saying, Alex, I think that we should just focus on API and SDK right now, getting those into a core repo.
**alexcohen** 43:30 Yeah, I'm… I mean, I'm… I'm 100% behind that, it just doesn't sound like everyone is, so I don't want to… I don't want to go there in a river and not do it like everyone else.
**Bryce Buchanan** 43:40 I mean, we can… we can move… we can move things around as we need to, you know, nothing's set in stone, right? So… Yeah. I think that… I think that we should… I think I agree with Martin, is that we should put the OTLP stuff into core as well, but we just need to sort this out first, and so I think a good first step is API and SDK. Is everybody okay with that?
**Martin Holman** 44:01 I think I am, like, … Yeah, I think it's a… it's a compromise.
**Bryce Buchanan** 44:05 Ruby.
Alright.
**Martin Holman** 44:08 Maybe, Vinod, I saw you unmuted there. Do you… Yeah, yeah.
**Vinod Vydier** 44:13 I'm good.
**Bryce Buchanan** 44:14 Excellent. Alright. Alright. So, so it shall be. … I'll go and make the core repo now.
I bet the… whoever runs the OpenChill Emergency admin repo is like, what is this guy doing? I'm, like, in there, just like, I need more repos! Rename the….
**alexcohen** 44:35 Just rename them? Can't you rename repos?
**Bryce Buchanan** 44:38 I don't… no, it's… it's all… it's all, Terraform, so I need to go change the Terraform for them, I think. I don't know, maybe I could just rename them.
I'll try that. I mean, you can definitely rename it on GitHub. I don't know if….
**Martin Holman** 44:53 With a terraform, then override it, I guess, is the main thing.
**Bryce Buchanan** 44:55 Yeah, that's the thing, I don't know. Or would Terraform just create a new gRPC repo, and then there's this other one named… around with all the GRPC. Like, the problem is, is that, you know, we have the maintainers, triageers, approvers, those are all gonna be… those team names are gonna be… I need to rename the team names there, too, and the… yeah, there's a whole pile of… of things that need to happen.
**alexcohen** 45:20 Fun stuff.
But so are you going to take care of doing this? Because obviously I don't have, the permissions to do any, any of this, and… One thing that I noticed is that splitting a repo into two different repos and getting the pieces in the right places and not losing history, is not something that is easy to do, for someone like me versus someone who actually has access like you could just directly push.
into it, versus PRs and all of that.
**Bryce Buchanan** 45:52 That's… yeah, that's not a bad idea.
Yeah, so, … Yeah.
**alexcohen** 46:01 simpler for you to pull the stuff out and put it in another repo than to… or to pull the core out than to pull everything else out.
**Bryce Buchanan** 46:10 I think… I think what I will do is I will create the core, I'll clone everything that's in Odin Telemetry Swift into Core, that should preserve all the history of it.
and then remove the, the non-core items from, from the, from the project, and then update, OpenTelemetry Swift repo to point to that one and remove API and SDK from… from there.
**alexcohen** 46:40 Sounds like a good idea. That should work.
**Martin Holman** 46:42 Makes sense.
**Bryce Buchanan** 46:42 I think that… that should work. Okay, cool.
**Martin Holman** 46:45 There's gonna be some, gargantuan Piers.
**Bryce Buchanan** 46:48 Well, I'll just… I'll just do a push, yeah, from….
**Martin Holman** 46:52 No, no, I mean when you remove, when you remove everything.
**Bryce Buchanan** 46:54 I know, yeah.
**Martin Holman** 46:54 Price deleted 60,000 lines or something.
**Bryce Buchanan** 47:01 Okay, alright, well, I guess we didn't really get to anything else today.
… But, … alright, we have a… we have a plan. I'll go start working on that.
**alexcohen** 47:17 If you need any help, just reach out, I can help however you need, but, like, I don't know if I'll be able to because of, you know, the permissions and stuff, but… Still here if you need it.
**Martin Holman** 47:27 Definitely raise it in the slack or something, if there's anything… small bits that we can do.
**Bryce Buchanan** 47:32 Sounds good. Okay, cool.
Alright, have a good weekend, everybody.
**Billy Zhou** 47:38 Oh, I have one thing, ….
**Bryce Buchanan** 47:41 Oh, yeah.
**Billy Zhou** 47:42 Did I get our… hey, sorry, I showed up to the wrong Zoom link at first, … Yeah, I put out a PR for, sessions, implementation. I… I don't know if I followed, like, the exact, like, like, protocol, like, I don't know, typically maybe I have to cut a… get an issue first, and get aligned, and then… do the PR, but yeah, I put it out there, please let me know what you think.
open to, like, refactor it. There's basically just, do things, like, one is, like, having a session ID, span processor hooked up to a, session manager, And then the second thing is, implemented the, session events based on the semantic conventions for session start and end.
… Yeah, I think there's, like, a small, commit I have to put out, on top of this as well, but, yeah, this is, like, the overall approach, so yeah, let me know what you think.
**Bryce Buchanan** 48:42 Awesome, thank you, Billy. That… this looks really good.
I'll take a little closer look on it. I haven't had a chance to look at it yet this week.
But yeah, hopefully we can get some eyes on that.
**Billy Zhou** 48:57 Okay, great, thanks. Yeah, I'd like to push some other instrumentations in the future as well, like, I don't know what you guys have planned for, like, like, metric kit, or, like, crashes, or anything like that, I'd be open to putting those things out as well.
**Bryce Buchanan** 49:11 Yeah, that'd be awesome, for sure. I thought that we had something for Metric Kit already, but I'm not sure.
**Billy Zhou** 49:19 Oh.
Didn't interrupt, you didn't realize.
**Bryce Buchanan** 49:23 Yeah, I'm not… it sounds familiar, and that's… Yeah, interesting.
**Bee Klimt** 49:28 I don't think you do, last time I checked. There's something else with a very similar name that there is something, some instrumentation for, but not metric kit.
**Bryce Buchanan** 49:36 Oh yeah, it might be, like, signpost is what I might be thinking of.
**Ariel Demarco** 49:39 Yeah, yeah. There's no metricade implementation in Ariba.
**Billy Zhou** 49:45 Okay, I'll, write some issues, I guess, and, send them your way.
**Bryce Buchanan** 49:50 Proofing.
**Billy Zhou** 49:51 Alright, thanks guys.
**Bryce Buchanan** 49:52 How are you?
**Billy Zhou** 49:55 Have a good Labor Day for folks in the US.
**Bryce Buchanan** 49:58 Oh, yeah.
Sorry, Monday's off. Cool. Alright, well, yeah, have a good one, everybody.
**Martin Holman** 50:05 The yield.
**Ariel Demarco** 50:05 Have a good one.
