SIG: Swift SIG
Date: 2026-05-28
Duration: 28 minutes
============================================================

## Zoom Recording Transcript

**Bryce Buchanan** 00:50 Haven.
You're not true.
**nacho** 01:35 Good morning.
**Bryce Buchanan** 01:38 Hey, where do you live in Spain?
**Vinod Vydier** 01:41 He goes…
**Bryce Buchanan** 01:42 Madrid? Oh. I think, I think that we should, get a drink or something, because I'm gonna be in Madrid…
**nacho** 01:50 Oh, really?
**Bryce Buchanan** 01:51 And… actually, in 2 weeks.
**nacho** 01:56 Okay, sure.
**Bryce Buchanan** 01:57 For… for an elastic thing.
**nacho** 01:59 Okay, great.
**Bryce Buchanan** 02:03 Sometime during, or between the 8th and the 12th, I'll be there. Or not sometime, but for that period.
**nacho** 02:12 Okay, yeah, then we definitely must have a beer.
Listavia.
**Bryce Buchanan** 02:17 Yeah.
I think I have, like, a free night on Wednesday or something.
I'll have to look at my schedule, though, but I'll let you know.
**nacho** 02:28 Okay.
Yeah, I think… exactly day… the 10th, I, unavailable, totally unavailable, because I have to go to the day off, but… and I'm not sure if that's the day you are free. Oh, okay, well…
**Bryce Buchanan** 02:47 I think that I can… I can get away otherwise. It'll… it'll be okay.
**nacho** 02:53 Okay.
Yeah, yeah, I have a… just, I think, a family thing.
Sylvia.
**Bryce Buchanan** 03:02 Alright.
Oh my god.
I guess, shall we get started? I don't know if Ari's gonna be here or not. Did he say anything?
I guess he's kind of been lately, or he's been busy lately, or at least he has a conflict, I think.
Alright, let's just get started. Alright, so, not bringing forward the Swift release, gRPC 2.0, I can't remember, do we… we didn't really have any actions out of this, did we?
Just kind of thought about it.
**nacho** 04:17 No, yeah, we were just talking about…
**Bryce Buchanan** 04:20 Hmm.
**nacho** 04:20 Yeah, what were the limitations? Yeah, we didn't check that.
**Bryce Buchanan** 04:33 I suppose… yeah, I can probably look into this, this next week.
Maybe not.
**Vinod Vydier** 04:43 I'm also at an event today.
**Bryce Buchanan** 04:45 Oh yeah, CocoPods failed to publish. What's that? You're in an event? Nice.
**Vinod Vydier** 04:49 Yeah, so… you might hear some background.
**Bryce Buchanan** 04:55 I haven't been able to look into this either.
Maybe, maybe Ari, we can ask Ari to do it, because he seems to be the CocoaPods expert.
**Vinod Vydier** 05:10 He was maintaining it, and I think he was gonna… stop at some point, because PokerPod itself is gonna go away.
**Bryce Buchanan** 05:18 Yeah.
Yeah, I'm not sure what the timeline for that is, though.
I'll message, I'll message Ari about this and see what he thinks.
I'll do it in our group chat.
I'll just do it right now.
Random build failures due to… The architecture thing.
Did we… did we resolve this at all, or… Are they still occurring?
**Vinod Vydier** 06:49 You… the build failures, right?
**Bryce Buchanan** 07:22 Oh, here we go.
**nacho** 07:24 Oh.
**Bryce Buchanan** 07:26 Now I can rerun it.
Last time I couldn't do that.
Okay, cool.
Alright, do we have any new topics we want to discuss today?
**nacho** 08:08 I have seen that there was a PR about the session stuff.
**Bryce Buchanan** 08:14 Oh yeah, look at.
**nacho** 08:20 that… Yeah, it made sense what he said, but, I was almost not involved here.
Yeah, probably he has cleaned up here with him.
Doing much.
Talk with the team?
But…
**Bryce Buchanan** 08:47 Let's see, who is it? Robert?
I mean, I'm not opposed to this, I'm just curious… What the, the current, like, session spec Kind of says regarding these things.
So, I need to, let's see, compatibility, sort of behavior… The OpenTelemetry semantic conventions define session attributes and lifecycle events, but leaves lifecycle policy to instrumentation. Oh, okay, alright.
It says sessions may end due to inactivity or timeout, and allow… A new session start to include previous ID when continuing.
From a prior session.
Yeah, I think, I mean, if it's similar to what's going on in Android, I don't have a problem with that.
I think, yeah, we can take a look at this.
Cool.
I think that's a good contribution.
I'll take a little closer look at it.
Got some… Updates here… it looks like, I messaged Samuel on here, and it looks like he, oh, yeah.
**nacho** 10:35 No, he didn't.
**Bryce Buchanan** 10:35 Oh, oops, that's… yeah, that's not the one. There was a… oops, there was another one that… Maybe it was this one here.
Yeah, okay.
Just missing tests. I'm waiting on the… This was released, wasn't it?
Two weeks ago?
**nacho** 11:12 Yeah, it was March, yeah.
**Bryce Buchanan** 11:17 April 9th.
**nacho** 11:18 It was merged, but not in the release.
**Bryce Buchanan** 11:20 not released. Oh, okay, I see. Okay.
That's the problem. So maybe we could do a, a release for, core.
**nacho** 11:38 Yeah, that, that… yeah, he can also… directly developed versus Maine, but yeah, that's true, that… For a… For merging the PR he needs. But we are… We are nightly building with it, right?
**Bryce Buchanan** 11:56 I think so, we ought to be.
**nacho** 11:58 Total.
**Bryce Buchanan** 11:59 But I think that… I think the problem… well, yeah, the problem is…
**nacho** 12:02 Yeah, that test run with the not… don't run with main. They run with the last release. Yeah, that's true.
Totally true, yeah. We, we… yeah.
**Bryce Buchanan** 12:22 I don't think Will has, had any time on this one.
Man, it's still… oh, that's interesting.
Okay.
April 24th… okay, so nothing new here… And I'll go through and merge all these, Renovate after the meeting.
**nacho** 13:10 Yeah.
**Bryce Buchanan** 13:10 Dependency dashboard.
Right? It just doesn't like that things aren't getting updated anymore.
**nacho** 13:36 It would be better if it just… keep silence, right? Because we only use that for tests, do we do it for any… or did it have.
**Bryce Buchanan** 13:47 Yeah, let's.
**nacho** 13:47 utilized.
**Bryce Buchanan** 13:47 Yeah, let's take a look at this. So, yeah, the Docker stuff is, is just for demo… Checkout… what? How's checkout?
**nacho** 13:59 That's the checkout action for getting new code from the repository, yeah.
**Bryce Buchanan** 14:05 Yeah, okay, so, like, I guess, yeah, you don't… I mean, doesn't need to get updated, right?
App tokens… yeah, this is it… oh.
Okay…
**nacho** 14:20 Yeah, the thing is that.
**Bryce Buchanan** 14:21 Oh, I see.
**nacho** 14:21 things that run on the CI.
**Bryce Buchanan** 14:24 Oh, cool.
**nacho** 14:25 We don't need to update, right?
So, you shouldn't click anything there, please.
**Bryce Buchanan** 14:37 I guess it's just mad about this one that's an abandoned… .
**nacho** 14:42 Yep.
**Bryce Buchanan** 14:45 So we might, I mean, we might look at… I don't know if there's, like, another option for the SwiftLint, though.
And it seems to run fine.
But the following are waiting scheduling. So I guess it's just, like, being nicer to us, so it's not spamming us all the time, is that the idea?
**nacho** 15:06 I hope so.
Yeah, I don't know.
It looks like at least it has not created more.
Yeah. Or many more of those, because it was…
**Bryce Buchanan** 15:20 I'll… I'll merge what's open right now, and then look at that list again, and then see… see which other ones make sense. I mean, I don't have any problem with updating the… Various dependencies that we're using, as long as it doesn't break anything.
So hopefully it'll, it'll open a PR.
This one seems to have problems, though.
**Vinod Vydier** 15:46 So, is there another, SwiftLint from… that is official?
Is that what it's.
**Bryce Buchanan** 15:53 The official SwiftLint… well, there's two Swift Lints.
One is, like… I don't know, one is, like, the official one, but it's, like, jankier than the community one.
So… Yeah.
**nacho** 16:18 Yeah, in reality, there is one SwiftLint, and there are two Swift formats that do exactly the same.
**Bryce Buchanan** 16:25 Oh…
**nacho** 16:26 There is one Swift slash format and a Swift format without that slash one.
One is the, Apple one that… comes with Xcode, or with some… Tooling, but yeah.
I think no one used that.
At least not much.
**Bryce Buchanan** 16:55 Okay I'll do… I'll also start a release on this one.
And reviewed, PRs and issues, and both repos. All right. Anything else?
**nacho** 17:23 Yeah, there is another topic about, concurrency thing, I have been… Taking a look.
I was going to answer that not everything needs to be sendable.
But I think he has some points of… things that… could be better for… for concurrency, usage. So I… I think I will take a look, on the code in… in… It seems with code issues… anything in core, in the car.
**Bryce Buchanan** 17:58 Oh, it's in court, okay.
**nacho** 17:59 Yeah.
**Bryce Buchanan** 18:01 This one.
**nacho** 18:03 Yeah, that's right, yeah. He's making some points about the instance and the, And the concurrency thing there. So, I think… we can improve it a bit, for the use case. So yeah.
And he also mentions using the… The other provider… the other… Task-based one, that, yeah, that could work. But yeah, he also mentioned that the instance is used a lot.
Which, yeah, it makes it difficult for some users, and yeah, I have to review that properly, so I didn't answer directly. I will do some tests and probably Some code changes for improving that.
**Bryce Buchanan** 18:54 Cool.
I think we've discussed this… Before, as well, but, it's popped up again, and it's the, the, I'm… I… gosh, how do I describe it? The, builder pattern that we're using in metrics is kind of a pain in the butt, because a lot of… the, non-S, or non-API, OpenTelemetry API APIs.
Are not… They, they don't… I guess they're expanded in the SDK, but the way that it's defined, the… the… Types hide them, so it's not really possible to… you have to, like, do a weird cast, a weird, explicit cast, forced cast, to get access to, like, the set unit and stuff like that, which is a pain in the butt.
And so, oh, hey, Billy.
We were actually just wrapping up.
But, if I have some time, I might try to… try to look into that and fix it. I think that I've… Done some improvements to this sort of thing in the past, maybe with Spans, but I can't remember.
**nacho** 20:23 Yeah, that, that, that, yeah, that, that's how… And always… The, theme that we talk about the, yeah, how comfortable the APIs are.
Or the user, yeah.
It… it's not easy, yes, to use the, yeah, the APIs with… with Swift and, yeah, and the protocols, and how associated types work, and making that Really well usable, it's not easy.
**Bryce Buchanan** 20:52 Yep.
**nacho** 20:53 To be honest, yeah.
**Billy Zhou** 20:54 I see.
Hey guys, for the Swift Core, it seems like we need to actually start resolving some of the concurrency issues. Is that what the issue is about?
Like, we just, I think for Core, I just, like, made a build with Rosh.
the, a new, with the P6, if I didn't resolve anything like I did in, the main library.
Is that pretty much the gist of it?
**Bryce Buchanan** 21:25 Oh, no, I was talking about something different, but, we did just discuss this currency migration, issue, and not just planning on looking into it. He said that there's some, there's definitely value in, what this user's requesting, so… But were you running into specific issues as well?
**Billy Zhou** 21:48 No, I didn't see this, but, Like, like I said, I don't think I actually resolved any of the issues, the problems in the core library, I just, like, made a build, so I can, like, take another pass to actually, like, resolve them like I did for the main library.
**Bryce Buchanan** 22:12 Okay. Nacho, do you… are you okay with that? Or are there other specific things that you were planning on?
**Billy Zhou** 22:19 Oh, yeah, you can decide in the lace, you can go for it.
**nacho** 22:23 Yeah… I'm okay with that. Yeah, the thing was, thinking about the… about the… what he mentions about the instance.
and all the multiple states that we have there. So, yeah, I was thinking more about How he… what he mentions about having an instance, and the constructor, and that thing, and… and… and… Yeah, and maybe a bit about the usability that we could improve there.
Not specific about… Yeah, solving everything?
But more about the… Yeah, they, they… like, in a global context, you know what I mean?
**Billy Zhou** 23:14 -Oh, is that question from me?
**nacho** 23:16 Yeah, the thing is that, yeah, thinking about We… we are using an instance for everything, and that… yeah, that… It really makes it difficult for, some concurrency users' issues, or, sorry, concurrency uses, of the library, because, yeah, we, we are always ending on the, on the same point, and that could be a corner.
for this. But just, I mean, just say that I had to take a look and see, because it made sense what he says, right? And we could make it a bit better.
Not about using the OpenTelemetry concurrency module, but about making the the, the core, more, usable from a… from a… from a sendable perspective. We cannot make everything sendable, right? Because, you know, at the end, we… we are storing states.
We don't want to create actors or a synchronous code for everything, but yeah.
**Billy Zhou** 24:24 Okay, yeah, that makes sense.
Thank you, Nacho.
And sorry to interrupt, guys.
**Bryce Buchanan** 24:31 That's fine. So should I assign, Billy to this one, then, instead?
**nacho** 24:38 Yeah, yeah, you can, you can, you can assign him.
**Bryce Buchanan** 24:43 Are you alright with that, Billy?
**Billy Zhou** 24:49 Yeah, yeah, that's fine.
**Bryce Buchanan** 24:50 Very cool. Who knew?
For crying out loud.
There we go, alright. Did you have any topics that you wanted to discuss, Billy?
**Billy Zhou** 25:11 No.
**Bryce Buchanan** 25:13 Nope. Okay. Well, thanks for dropping in at the very end. I think we're done for.
**nacho** 25:17 Also, Billy, we have been talking about a PR that they have created about the Sessions instrumentation, that I think you worked on that in the past a lot.
Oh, yeah.
So maybe… I mean, it looks quite complete.
But yeah, I don't know if that's… what you expect from that part of the library also, so yeah, please, if you can… Review that, and… About the lifecycle rules, yeah.
**Bryce Buchanan** 25:49 Yeah. It's essentially just extending the configurability of the session stuff, so… It seems like it's in line with the spec, and he's… it looks like he's, adding… functionality that exists in the Android agent, so there's, like, pre-existing behavior, so there's, like…
**Billy Zhou** 26:14 Oxy problem.
**Bryce Buchanan** 26:15 Yeah. So, yeah, take a look. I was gonna take a look, too, but I think…
**nacho** 26:19 And also, if you like the approach, or the changes, if they are in the way you would add them in the spirit of the existing instrumentation, basically.
**Billy Zhou** 26:31 Okay, yeah, it looks, really good, and if it's already in Android, I'm sure a lot of people are used to it. They all look very familiar.
**nacho** 26:41 I mean, it's… this is because people is using it, right? So, they need a bit more.
**Billy Zhou** 26:47 Yeah.
That's cool.
**Bryce Buchanan** 26:52 Alright.
**Vinod Vydier** 26:53 Hey, any of you, any of you going to the KubeCon?
Cause we should, we should make a… Should I have a session on Nortel Swift?
**Bryce Buchanan** 27:09 What does that have to do with Kubernetes?
**Vinod Vydier** 27:11 No, it's actually part of the, what is that? CNCF, right? OTL is part of… CNC.
Everything open telemetry is part of, Yeah, I think for some reason they re… they named the conference as KubeCon, but it's actually… Got it, all CNCF, including hotels.
**Bryce Buchanan** 27:31 Well, that's just confusing.
**Vinod Vydier** 27:33 Yes, yes. Just like naming so many things is confusing.
**Bryce Buchanan** 27:40 I wasn't planning on it, but maybe, I don't know, it's all the way in November.
**Vinod Vydier** 27:44 No.
But they have, sessions, I think, by next week or something, if you want to put in a Swift session.
We have another week.
**Bryce Buchanan** 28:00 Oh.
**Vinod Vydier** 28:01 Yeah, you can even make it into a lightning talk or something, if you're going, because otherwise, I don't think you can do… Remote, yeah, you have to be there.
**Bryce Buchanan** 28:11 Yeah, I wasn't planning on going, so…
**Vinod Vydier** 28:13 Okay, okay.
**Bryce Buchanan** 28:15 Nacho's not planning on going.
**nacho** 28:21 It's a bit far.
**Bryce Buchanan** 28:26 Alright.
**Vinod Vydier** 28:27 Alright.
**Bryce Buchanan** 28:29 Have a good weekend. See you around soon.
**nacho** 28:30 Have a good weekend. See ya.
**Vinod Vydier** 28:32 Okay. Bye.
**Billy Zhou** 28:32 Thank you, guys.
**Bryce Buchanan** 28:34 See you, Billy.
**Vinod Vydier** 28:35 Bye.
