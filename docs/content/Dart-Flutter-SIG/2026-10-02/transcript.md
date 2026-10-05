SIG: Dart & Flutter SIG
Date: 2026-10-02
Duration: 30 minutes
============================================================

## Zoom Recording Transcript

**Michael Bushe (Mindful Software, LLC)** 02:37 Everybody, how's it going?
**Robert Magnusson** 02:50 Oops, sorry, I was muted. All good, thanks, how are you?
**Michael Bushe (Mindful Software, LLC)** 02:55 I'm doing terrific. Could be a good October, I think, even though the Red Sox lost.
**Robert Magnusson** 03:00 But didn't they win not so long ago?
Or I remember watching something saying, like, they didn't win forever, and then they had a good season not so long ago.
**Michael Bushe (Mindful Software, LLC)** 03:10 then they won 3 times. The way we measure ourselves is, if the New York Yankees win, and we didn't win, then we're losing. And it's at least the case that The Red Sox have won 3 times since the Yankees have won, so we're doing good. But it's getting a little aged now, not too bad, but the difficulty was, the last two years in a row, we played the New York Yankees in the playoffs, and lost badly both times. Well, last year wasn't so bad, this one got wiped out.
That's baseball.
**Robert Magnusson** 03:45 Yeah, that's fine.
**Michael Bushe (Mindful Software, LLC)** 03:50 We had a couple minutes. Victor Lu, I'm not familiar. Maybe you joined us and started adding.
**Victor Lu** 03:58 the.
**Michael Bushe (Mindful Software, LLC)** 03:59 speaker.
**Victor Lu** 04:00 Oh, no, actually… no, actually, usually I cannot attend this meeting. It's interesting, you're in Boston. I'm in Florida, but I'm happy to be in Abstain today. That's why the time is okay. So I don't know how you… you joined at 4am for you right now?
**Michael Bushe (Mindful Software, LLC)** 04:17 I'm actually in France. I'm from Boston.
**Victor Lu** 04:20 Okay.
**Michael Bushe (Mindful Software, LLC)** 04:20 In France.
**Victor Lu** 04:22 Oh, no wonder. Yeah, yeah, usually I I see this before, but yeah, no, I'm just visiting and see what this meeting's about.
**Michael Bushe (Mindful Software, LLC)** 04:30 And what's the that picture from?
with the…
**Victor Lu** 04:33 Actually, no, that's something I got from, internet. I live in Florida, so yeah, that's… Close.
**Michael Bushe (Mindful Software, LLC)** 04:44 I've spent a lot of time on, in various beaches around the world. I must have been… I've been a nomad for over 10 years, and I've been to easily 100 beaches, maybe over… maybe up to 200.
**Victor Lu** 04:58 Oh, nice. Yeah, that's my dream. I'm going to do that someday.
**Michael Bushe (Mindful Software, LLC)** 05:05 It's it's interesting. After doing it like full time for that long, I recommend not doing that. It's it's it's good to have an attachment to home. It's hard to go back home. It's it's that's what they say is though.
Is, is really true.
All right. We're 5 5 min in, so I guess we'll keep going. Harshita. Hope you're doing well, too. Thanks for joining us.
So I I just have a little bit of agenda. Feel free for you guys to for anyone to bring up any other topics.
I've been sort of MIA for about two weeks. I've had some other things to focus on, but I'm back, and I plan on going through the PRs today or this weekend.
merging or proving, moving them along wherever they need to be moved to. We have a stack of PRs, ready to be released for the API. I think I was waiting for the one more, and we got that critical one that was, that was a performance one, which I would really like to get out pretty quick.
Can I ask about that? Because I haven't dug into it yet. Did we add a performance test so we could see a little before or after? Before and after?
**Robert Magnusson** 06:22 No, I think that was not added. He had run tests and I had run tests, but.
It's a good question. I don't remember it being.
Performance test included in it. I mean, it was unit tested, but was there a performance test in there?
Hmm. I don't know off the top of my head.
**Michael Bushe (Mindful Software, LLC)** 06:38 I don't think we have performance tests in the API. We do have a performance test suite in the SDK.
So… but I don't think it's part of the regular run, and I don't think if things slowed down, it would fail. So, I will issue to make sure that, we track That if our performance degrades, We know about it before we release.
Yeah. And I'll add another issue to track, to add a performance test for this specific case.
Which is every case. Every case case, right?
Okay, so, Right, so I will be releasing the API. The SDK won't necessarily be updated right away, because there are some changes needed in the SDK that we need, so there… I think there already is a branch for this. If there's not, I will make one for the new API.
to… make that branch, update the API there.
clean up whatever dependent SDK issues are on that. That's what we should work on next, and maybe I'll actually chip in and do something rather than review everyone else's code to get the next release out. And then we'll merge that to main, and I'll try to get a release out.
from there.
Does anyone know where we are with the tracking issues? We were pretty close to done on the API.
**Robert Magnusson** 08:10 No, I didn't follow up on the tracking, but I was just trying to get through all the open PRs was in a merge.
And I think that's pretty good, like, I think everything that's open is sort of close to being mergeable, or is mergeable.
**Michael Bushe (Mindful Software, LLC)** 08:24 Oh, great, great. If we have that many open, I think the only thing we may have left for the API is Doc, which is great. So we can go make a release.
the next thing that might happen with the… I think that… I'll move on to the next topic. So, the next thing that might happen is, yeah, the semantic conventions are getting federated right now. For example, the Gen AI semantic conventions are in a federated repo.
I don't understand what we need to do with Weaver and how we manage the changes from all those teams.
Perhaps what we do is make an, I don't know whether we should make another… probably we should.
Maybe what we should do, is make another repo.
Well, heck, we have a… we… let's… you know what I'll do? I was gonna say, I can make another repo in Mindful Software, and then just publish something to claim the namespace, the official namespace, and then we could always.
change what repo we're publishing from, and I can retire that repo.
But let me see if we could do this more officially. Maybe what we should do is start a… I think we may already have a repo, if not, Severn's pretty quick about turning things around. We could get a repo, we could start the semantic conventions work in there, and just do as we talked about, which is… which is moving the semantic conventions out of the API into its own repo, and then we can start in there dealing with the with the federated case and and just keep the Api, the mindful software Api as it is.
Yeah.
**Robert Magnusson** 10:12 Sounds good. So, the repo, I mean… they can be in the same repo, right? Because we have the hotel… official OpenTelemetry Dart repo, which is more or less empty.
Currently.
So, could we put it directly in there and do this folder structure, which, It's the official… I'm not sure who was working on that.
**Michael Bushe (Mindful Software, LLC)** 10:31 It's the official OpenTelemetry repo.
**Robert Magnusson** 10:35 There's like one that has all the conventions.
How do you mean?
**Michael Bushe (Mindful Software, LLC)** 10:40 Maybe I should ask how do you mean?
**Robert Magnusson** 10:43 So I meant… I thought you meant that we want to… Let's… I guess there are two parts to this. So, I don't really know how the Semantic Convention Federation works. It's, like, one repo with all the languages that has all the… The specs per language in one place.
I guess that's maybe what I would…
**Michael Bushe (Mindful Software, LLC)** 11:04 That's the way it's been. Yeah, that's the way it's been until now.
**Robert Magnusson** 11:07 And their Dart is missing. I think I remember my agent saying to me something like that, like, I was trying to build up a local test for building up a Flutter auto app, and he said, like, no, I cannot verify this because it's not in the semantic convention.
Okay, now you've got Android.
**Michael Bushe (Mindful Software, LLC)** 11:22 You're getting a little ahead of me, but you're on the right track. So.
What the this is again, we talked about this last week, last meeting, and it's still the same thing where the client T the client SIG is is is we're gonna determine the client SIG how this works.
And it's still being determined, but probably… it's either going to be one of those two things, right? It's either going to be everything that's Flutter, Android, Swift. will be in the client repo. It's probably not going to work this way, but that's one option. Browser, too. Browser has its own already. Android has its own already. I think Swift does, too. So either those get merged all into client, or… Or we figure out a way to.
What I like better is that everybody keeps their own.
And those can rev independently, and then… you know, Dart is… we're not gonna just do the Dart ones, we gotta do all of them, because we have to expose in Dart everything. So I think instead of our weaver taking what's in the semantic conventions now, we… as they get federated, we will be including the federated ones and deprecating whatever is not consistent.
That's in just the common semantic conventions now.
Then, we will be responsible for… As each one that we pull in.
Revs, we will be responsible for regenerating with those with those revs.
That's the way I think it's gonna go. That's what I'm kind of pushing for. But I can't guarantee that that's the way it's gonna work.
Now, so what does that say? So that says either we're gonna have Flutter inside that client conventions repo, or, right, we're gonna have our own Flutter repo that has Fluttery stuff. And Dart stuff.
I don't know how it starts.
**Robert Magnusson** 13:27 And that's our own Fluttery Dart stuff.
That can all be in one repo, right? In the one we have now, the OpenTelemetry-Dart.
**Michael Bushe (Mindful Software, LLC)** 13:39 No. Wait, hope open no i think open telemetry hyphen Dart, isn't that, maybe I'm wrong, but isn't that the one that's somebody's kind of squatting on that name and that's not maintained. It's like two downloads. Yeah.
**Robert Magnusson** 13:52 Yeah, I mean, maybe, like, the public dev team. Sorry, I meant the repo, like, where we host all our future code.
So we have the…
**Michael Bushe (Mindful Software, LLC)** 14:01 Oh.
**Robert Magnusson** 14:01 The repo failed for us.
**Michael Bushe (Mindful Software, LLC)** 14:02 with you.
**Robert Magnusson** 14:03 And it's currently empty.
And I guess the one way we can now move forward is to start moving over, like, the… The Dart specific files for… yeah, sorry, go on.
**Michael Bushe (Mindful Software, LLC)** 14:14 I forgot, we have that repo already then, right? Is that right?
**Robert Magnusson** 14:17 Yeah, yeah, it's up and running, and it's, I mean, it's more or less empty. It has, I think, a license file and some, GitHub out-of-the-box automations that already get, like, renovate issues that I keep fixing.
But I think it's like in a shape where we can start moving over the things that we are sort of confident with.
**Michael Bushe (Mindful Software, LLC)** 14:35 Well, well, let's start doing it with the semantic conventions. But that's not I.
I gotta figure… we gotta figure this out, but, That's not where we define the conventions that we… that we are going to define for Flutter and Dart. That's where we produce… the repo is where we produce the library. Wait a minute, but that also means… right, so… There's two things going on, right? I think we would need… this repo is a monorepo, right? And so, we would need two projects in that repo. One, right, is where we say, here are our semantic conventions, like Gen AI did, we can sort of copy that as a model.
That might have a dozen or so. I don't know. Flutter app lifecycle would certainly be one that I could think of.
probably some other things. And when we do that, I'm sure I have some stuff with Dartastic.
that I defined, that I can… that I could push upstream. I've been waiting for this.
And And then, so, so, but that, that's gonna be like a dock, right? So that Weaver can take those things and… for example, Kotlin Multiplatform. I don't know who would do it. I don't know who would pull this in, right? Because we're kind of… as a multiplatform, we're at the relief… we are a leaf. Even Kotlin Multiplatform probably wouldn't depend on Flutter, but… anyone who wants to create a server, or, for example, you know, AI that knows about all the semantic conventions, they would use Weaver against our repo, and as well as all the other federated repos.
So there's the definition repo. I don't know what we'd call that. I'm open for names. There's probably some kind of naming consistency. We should do it the way everyone else is doing it.
And then there's the other repo, which looks like what we want to pull out of API, which takes those… which takes all the semantic conventions from that, and from Android, and Swift, and everybody else, Gen AI, and all the semantic common conventions.
And then, you know, generates it like we do today.
And that… we would publish that. That one gets published to PubDev.
**Robert Magnusson** 17:00 Yeah.
**Michael Bushe (Mindful Software, LLC)** 17:06 Feel free to dig in if you have any questions, let's look at chat about it on the.
**Robert Magnusson** 17:12 Yeah, I think I have to read up on how all those, federated part of how Clue works and how the other platforms are doing it.
**Michael Bushe (Mindful Software, LLC)** 17:20 Let me I'll I'll take I'll take a few yeah, feel free to do it yourself. I'm I'm also on I have a task to do that myself in the Gen AI and to see what they're doing to and to learn about it and also look at that what Swift and Android are doing.
But they're… but they are… I don't believe either one of those are federated yet.
**Robert Magnusson** 17:44 Yes, yeah, I also don't know that. I mean, I have two colleagues who's active in the Android SIG. I can check in with them if they… know if it's on the agenda for the SIG… for the Android SIG group.
**Michael Bushe (Mindful Software, LLC)** 17:56 Cool, cool.
I think that's all I have.
**Robert Magnusson** 18:06 Yeah.
But maybe I am misunderstanding now because yeah, sorry, go. Sorry.
**Victor Lu** 18:12 Maybe, maybe… I don't understand, what is it? The title of the meeting is interesting. Darton Futter? What does it mean? What is this for?
Dart and Flutter Stick? What is it about?
**Michael Bushe (Mindful Software, LLC)** 18:32 You know, this is a good… this is a good question. So, and this is an open question. So, Flutter apps are written in Dart, and we have a Dart SDK… a Dart API in SDK. That's the baseline. The question… one question we have outstanding is.
Pardon me. What do we do for Flutter?
Do we create another API? Do we create… is it its own SDK and API? I think, working on this for so long, I think it's not. I think Dart does almost everything you need to do for Flutter, but probably, like, it's probably a contrib… Library, there's… there's stuff that we may add on that That serves Flutter alone.
That way, if you're running… we have to… I mean… I'm not even sure if we want to do that, because if you think about it, what's the gain there? You might say… I don't know what the improvement is. You might say, well, if you're doing Dart on the server, you don't have to pull in this Flutter stuff.
Well, Dart is compiled. You're not pulling it in anyway. You've compiled it out. So I'm open to ideas on this.
**Robert Magnusson** 19:44 Yeah.
**Michael Bushe (Mindful Software, LLC)** 19:45 What the best… I mean, I…
**Robert Magnusson** 19:47 Quickly look at it, it feels like it should be separate, like, anything… there's a bit also how I think the Swift team, I've also been around in a few of the other clients' SIGs, and I think that's also how they think of it, or, like, how Apple wants to push the Swift SIG group, to say, like, Swift is a language.
don't tie platform stuff into that. I guess the same way, like, Dart is just a language, don't type… although Flutter is the biggest platform using Dart, but maybe try to avoid having that dependency in. Can still be in the same repo, I guess. I've also been playing with that last week, how to set up a Dart instrumentation using OTEL… sorry, a Flutter instrumentation using OTEL Dart.
And I think using this sort of composable add-on instrumentation that is Flutter platform-specific works. So, like, we can keep the… The Open Dart Pure.
And then whenever we need, like, I don't know, some specific, got the runtime specifics, then that could be an instrumentation That depends on Auto Dart, not the other way around. That Auto Dart stays, sort of.
Clean.
**Michael Bushe (Mindful Software, LLC)** 20:50 I fully agree. I'm wondering when that's gonna come, and I wonder if it's not… the other thing that, that all the other languages do is there's contribute libraries. So, like, what would you… what case would come up for this? And I think there are things like Navigator.
**Robert Magnusson** 21:09 Yeah.
**Michael Bushe (Mindful Software, LLC)** 21:10 right or but or but most people don't use navigator directly. They're using go router or auto route or right. And so for for each one of these, instead, what I think what we could do is have an Otel auto route. I may already have one that we can contribute back.
Sounds good. Right? Otel Go Router, I've got one of those, too, I can… we can contribute back. And by the way, the ones that I have are just, hey, AI, go do this for the first shot.
**Robert Magnusson** 21:42 real-time.
**Michael Bushe (Mindful Software, LLC)** 21:43 0… 010 Beta.
So.
**Robert Magnusson** 21:47 Yeah, I think that sounds good.
There's probably a few of them. Like, there's also, like, offline storage, maybe, or resource, or tap detection. A lot of this probably can be, like.
Instrumentations that you just add on as you want.
**Michael Bushe (Mindful Software, LLC)** 22:00 Well, now you're getting to something. No, that I think taps.
swipes, that kind of stuff, that makes sense to be part of Flutter, because it's Flutter, right? It's only in the Flutter SDK, it's not in Dart, and it's not dependent on a third-party library. So yeah, I'm for that.
I haven't… I haven't… right. Yeah, that would be the one. We should have one of those. And also a Flutter metrics, separate from the Dart metrics.
**Robert Magnusson** 22:34 Yeah.
So I think, yes, on that, we should think of how to build up, and also, like, find a sweet spot there, because Also, I've been playing with, like I said, the Android and Swift versions, and the Android, also Android, it's really, like.
mobile developer friendly. It's like the one-liner setup.
Whereas Auto Swift.
It's very pure OTEL. Like, there's a lot of bootstrapping you have to do to get stuff running.
And I think that also might scare off some Flutter developers. So I think… Even if it's separated like this, and, like, you shouldn't… only be able to depend on Otel Dart, and then have the other add-ons. We should probably offer some… maybe not a Flutter SDK, I'm not sure there, but, like, some bootstrapping, like.
Flutter Hotel Init something.
That maybe just calls functions on hotel Dart SDK, or something.
**Michael Bushe (Mindful Software, LLC)** 23:25 This is what Flutterific.
was the Flutter.
**Robert Magnusson** 23:28 Okay.
**Michael Bushe (Mindful Software, LLC)** 23:29 is… it's exactly that. Instead of OTEL dot, it's Flutter OTEL dot dot The only difference, I think… well, I mean, it does, like, page routing, but as I… as I dug in, I'm like, well, really, I'm doing GoRouter, and I want to split that out. I haven't, I haven't.
it's… we can use that as a learning source and do whatever we want. But for the most part, it was like that. One of the main differences was, resource collection. You know, when you collect the resources on START, now you're going to get an app ID.
Things like that.
what what the device is right? How how many pick, how many, how big the screen is that kind of thing.
**Robert Magnusson** 24:13 Yeah.
Sounds good.
**Michael Bushe (Mindful Software, LLC)** 24:16 Good, good fun project.
**Robert Magnusson** 24:19 Yeah, that's true.
**Victor Lu** 24:22 Yeah, so I didn't. And, by the way, I'm not a developer, so I'm sorry.
**Michael Bushe (Mindful Software, LLC)** 24:28 Victor, what do you do? May I ask?
**Victor Lu** 24:31 Well, long story. I was an unemployed physicist, and then, do a database. I'm kind of semi-retired, I'm a generalist. The reason I'm interested in hotel, actually, the one you mentioned, the Gen AI, cement convention.
There is a security matrix being proposed to add a security matrix for AI for OTEL and OCSF.
That's, that's why I was, involved there. So, yeah, so it sounds like Dart is just a… it's a language for mobile, devices, basically.
**Michael Bushe (Mindful Software, LLC)** 25:06 We're hoping not. So that's true, like, it's at least 90% of the usage of Dart is Flutter, which builds apps, not only for mobile, iOS and Android, but it also builds them for desktop, Windows, Linux, and Mac. And because it's doing… and it also builds for the web and WASM.
And when you say Linux, though I mean, now you're talking servers. And so I use a lot of Dart. Not many people do, but I use a lot of Dart on the server. I think it's a really great server language. It's type safe, null, safe, composite binary almost as fast as C.
But but and also there are Dart functions that in in cloud providers, at least in Gcp. You can write a lambda function, a serverless.
**Victor Lu** 25:58 If you create an elevator pitch for Dart and Flutter, what do you say?
**Michael Bushe (Mindful Software, LLC)** 26:04 If you created the what?
**Victor Lu** 26:06 I would pitch for White Dart and Flutter versus, like, Rust, which is also type-safe.
**Michael Bushe (Mindful Software, LLC)** 26:13 Dart is, the.
**Victor Lu** 26:16 Actually.
**Michael Bushe (Mindful Software, LLC)** 26:17 Dart. I do Rust as well. Dart is really simple. And it goes to Robert's point too, and we should always make sure this is our North Star.
Flutter is really simple. And anyone around the world can write a Flutter app really quickly and really easily.
And we need to keep it that way, and we don't want to, like Robert was saying, we don't want to have, you know, lots of setup for somebody just to do OTEL. It's got to be a one-liner, and that's why I kind of also went, even Dartastic.
even OpenTelemetry library we're working on, the, we have OTEL DOT, so that everything is sort of… you know there's one class, you go from here, and everything goes from there. You don't have to go fish around for the API. It kind of exposes itself.
I don't think other libraries have that, and I like it for that reason. It makes it more approachable, and we have to keep doing that. So Rust is not…
**Victor Lu** 27:18 Do you…
**Michael Bushe (Mindful Software, LLC)** 27:19 the.
**Victor Lu** 27:20 Sorry. How do you, like.
I guess, explain the relationship between Dark Flutter, Rust, and WebAssembly. How do they play together?
**Michael Bushe (Mindful Software, LLC)** 27:31 So, so Rust is… Rust is a low-level language, Rust doesn't do, UIs, or, I mean.
There are UI libraries, but I don't think they're used very widely. I've looked into that. And it's not made for purpose, for that purpose. And it's great if you're a systems programmer or somebody who writes C, C++, and Go, you know, it's on that level.
Dart is not made for that person who's usually very smart, experienced. I'm like, we're all smart, right? But they're usually very experienced developer dealing with those kind of issues like you see in the server. Dart is made to be really approachable. It looks like Java. It looks like Javascript.
You almost can't tell the difference between the languages anymore. The other thing that you should know about Dart that's very interesting is that when you start a Dart app, it's a lot like a node server. You have a single-threaded… and that's one big part of it, it's single-threaded, right? You can't start a new thread.
Not yet. And so it's like Node, which is also single-threaded, and that's why it's nice for the browser, right? There's only one message being handled at once, which has great facility for making programs easy to write. You don't have to worry about concurrency and comic operations, that kind of stuff.
Whereas Rust, you can do whatever the heck you want.
**Victor Lu** 29:11 Sounds like Dart and Flutter is kind of taking the best from both Rust for type safe as well as JavaScript for front-end implementation.
**Michael Bushe (Mindful Software, LLC)** 29:24 Right, I think of it this way, right, you're right, and it's very… it's a very nice language, it's my favorite language, it's not very popular, but it should be, I think. And the person who wrote the Java language specification, Gilead Braca, also wrote the Dart language specification. So, it's… a lot of the Java guys from Sun moved to Google.
A lot of the Java Swing guys moved to Google, and when Dart was developed, there was a lot of influence. The collections, for example, was worked on by the Java collections fella, I can't remember his name off the top of my head, and I always think of Dart as a better Java and Flutter as a much better swing. Both are right once run anywhere, but swing relied on the Jvm. Dart Java relies on the Jvm. And Dart just compiles to native. So it gives it a performance while keeping it cross platform.
**Victor Lu** 30:23 Final question, how does it play in the WebAssembly ecosystem?
**Michael Bushe (Mindful Software, LLC)** 30:29 Right? So you can. You can take any Dart or Flutter app and just compile it to Webassembly with a flag. Not any right. It's almost, you know, there are violations you can make that you may have to adjust to, but for the most part it compiles to Webassembly as well. And so I really like that feature. Google is really, and a lot of the people who are on the Flutter team at Google are really pushing Webassembly because they think that's future, and that allows us to compose Flutter inside other WebAssembly apps.
**Victor Lu** 31:02 Thanks.
**Michael Bushe (Mindful Software, LLC)** 31:04 Welcome.
**Robert Magnusson** 31:05 So I have to leave. I have a different meeting coming up.
**Michael Bushe (Mindful Software, LLC)** 31:08 Great, thank you guys, we can slack, what else?
Good morning.
**Robert Magnusson** 31:14 What are like the most important next steps wrapping up the open issues?
Open topics and the API, basically.
wrapping up the API level, and then releasing that, and then trying to see how we can get Some code into, maybe, the official repo now, starting with the semantic conventions.
**Michael Bushe (Mindful Software, LLC)** 31:34 Exactly. Alright, so, I'll… I will do… I'm gonna try to get those AP… I'll focus on getting the PRs closed, getting releases out. If you want to start taking a shot at the… at the official repo, and, we'll… starting with the semantic conventions, that would be awesome.
**Robert Magnusson** 31:52 Yeah, so there was an initial by Yusuf, I think, in a competitor in Slack.
Where he started drafting out how we could structure that.
Right. Maybe that's, like, a starting point.
But then… Keep it, like, maybe initially empty, and then see how we can move in initially the…
**Michael Bushe (Mindful Software, LLC)** 32:10 Oh, I I didn't see that. Oh, nice, nice. I totally missed this. Okay, great. Let me let me catch up there and I'll get back to you on Slack on that.
**Robert Magnusson** 32:19 Cool. Sounds good.
**Michael Bushe (Mindful Software, LLC)** 32:21 Alright, awesome.
**Robert Magnusson** 32:22 Cool. Nice to see everyone again. I have to run, but nice to see everyone. Have a nice weekend.
**Victor Lu** 32:27 Thank you.
**Michael Bushe (Mindful Software, LLC)** 32:29 Thank you.
