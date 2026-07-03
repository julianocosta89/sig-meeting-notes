SIG: Swift SIG
Date: 2026-07-02
Duration: 61 minutes
============================================================

## Zoom Recording Transcript

**Zoom user** 01:33 Hello!
**vinodv** 01:36 Dang.
**Zoom user** 01:57 In a nutshell.
Moving on.
**vinodv** 01:59 Hey, Bryce.
Can you hear me?
**Zoom user** 02:02 Am I… can you hear me? Am I…
**vinodv** 02:05 No, I can get you.
**nacho** 02:07 Yep.
**vinodv** 02:12 Can you hear me?
Amazing.
get home.
**Zoom user** 02:17 Hmm… Here's the problem.
Test, test, test.
**Robert Magnusson** 02:35 Hello!
**Zoom user** 02:36 Okay, there we go, now I can hear ya. Can you hear me?
Yes. Okay, there we go. Cool.
Zoom, obviously, you know, it should be putting sound through the microphone instead of listening with the microphone.
**Robert Magnusson** 02:55 Makes sense.
**Zoom user** 03:16 Come on.
Okay.
Alright, shall we get started, then?
**vinodv** 03:30 Nope.
**Zoom user** 03:31 And so, from last week, it looks like… some fellas from Grafana visited.
Garden Sputter Protone.
**vinodv** 03:44 Yes, I, I was actually… on my way back from my peak off, and ted… Ted was our… And, Ben was on.
So we… I think this was… they come from the client side, client SDK sign.
**Zoom user** 04:04 Huh.
**vinodv** 04:05 So, yeah, so we did… I mean, I think they were kind of trying to… Make sure that we are… Following the conventions that they are adding.
From the client… client-side SIG.
**Zoom user** 04:23 the icing.
**vinodv** 04:24 No. Well…
**Zoom user** 04:31 Oh, hey, Ari.
**Ari Demarco** 04:35 Hey, y'.
**Zoom user** 04:36 Robert, it seems like you're… you're from Grafana, too, are you?
Did.
**Robert Magnusson** 04:41 Yes.
**Zoom user** 04:41 Speak to this a little bit more, since…
**Robert Magnusson** 04:44 Yeah, so I missed… I wasn't there last week, this is actually my first time joining this big group.
I know some background to this one, though, I'm not sure why they pasted it in that meeting, though, but I'm part of that initiative, so it's driven by Michael Bush, I guess you pronounce it.
And it's trying to… bring… set up a lot of their door to… sick group, and, and donate, Michael's… initial work on… also for Dart.
And I'm actually involved as a maintainer on that.
I will be maintaining it once that gets approved.
**Zoom user** 05:17 Oh, cool, okay.
Yeah, so this is Flutter as in, like, the, hybrid framework for… for mobile device, or mobile, yeah, development.
**Robert Magnusson** 05:27 Yes.
**Zoom user** 05:28 Okay.
**Robert Magnusson** 05:28 Like, initially, I think it's a little bit Dart, the language, like, Swift, Bryos, so Dart for Flutter, so the language driving Flutter, but then long term, also Flutter, like, the Flutter specifics on top.
**Zoom user** 05:40 Very cool.
Okay, I guess we can take a look at this offline.
Is there anything specific, for us to look for, or… Just a general idea of… .
**Robert Magnusson** 05:57 I don't know why Ted and Ben shared this in the last meeting.
**Zoom user** 06:04 I mean, I suppose there's impact, right? If it's the hybrid framework support, there needs to be something probably on our end to… I'm guessing there's gonna be some sort of, like, cross-communication, like, maybe some sort of bridge for Swift into Flutter?
I don't… I'm not super familiar with how Flutter works, I mean, I've done work on React Native and stuff like that, but… Yes.
**Robert Magnusson** 06:33 So I think initially, not so much, but I think the first… sorry, my son is here, so my wife was out, I had to watch him for a second.
**Zoom user** 06:39 Oh yeah, no problem.
**Robert Magnusson** 06:40 So, initially, it's gonna be, like, dart focus, so that's the… Pure… Yeah.
So initially, it's pure Dart. That's not Flutter-specific.
And then maybe later on, Blutter will come, and that will have that native impact with Android and Swift.
But I think short-term, it will mainly be focused on DART.
**Zoom user** 07:03 Okay, cool. Yeah.
**Robert Magnusson** 07:06 I think Michael, who has been driving that, has been also involved in the client SIG group.
And… and getting knowledge from there, so… maybe that's also why they posted it there, to sort of highlight that… that the DART is trying to get… Actively involved in the whole client group.
**Zoom user** 07:23 Okay, cool. Yeah, thanks for bringing that to our attention.
Alright, let's pop back a week here, because it looks like there's some stuff that didn't get brought forward.
So, I'm guessing this is from Billy?
**nacho** 07:42 Yeah.
**Zoom user** 07:44 issues.
**nacho** 07:45 Yeah, I think that's the PR that… Just needed…
**Zoom user** 07:50 Yeah.
**nacho** 07:51 He created a PR with some small updates to the concurrency thing.
probably is… yeah, I think it's related to that.
Otherwise, I'll be the same mission.
**Zoom user** 08:04 Yeah, we'll talk about that in a minute. The, this is… yeah, I was looking at this one, Yeah, so… I think we should probably merge that and get a release out so that we can apply that to the main repo, and… yeah, because it seems like some build jobs are broken because of that.
Probably related to the Swift 6, runner that's… that is being used.
Alright, issues with APIs, type hiding, extensions, review this later, yeah.
That is something that I want to take a look at, for sure.
It would probably require some kind of refactor that… hopefully it won't be breaking anything, but… It might take a little bit of work.
- I like this.
Who brought… who brought this up?
**vinodv** 09:11 Ari has a detailed document.
**nacho** 09:14 Yep.
**Zoom user** 09:15 Oh, is there a document for this? Deprecation form?
**Ari Demarco** 09:18 Let me… get it.
For you guys.
Let's… the dedication.
Period.
Copy link.
sharing in the chat here. Okay.
So, also, Robert can take a look.
**Robert Magnusson** 09:45 Thanks.
**Ari Demarco** 09:48 Today, my Mac, it's not really.
In the best spot possible.
The, the meeting chat thing.
**Zoom user** 09:57 It's hard to find it.
**Ari Demarco** 09:58 Let me… let me re… let me reload.
**Zoom user** 10:01 Okay.
**Ari Demarco** 10:03 Oh.
Rum is frozen, okay.
I'll share it in Slack.
Did you guys?
Oh.
Everything is frozen. Okay.
**Zoom user** 10:13 Oh, no.
**Ari Demarco** 10:20 My god.
**nacho** 10:21 Your head still moves, so… Oh.
**Robert Magnusson** 10:28 Cameras prioritized.
**Zoom user** 10:30 Important, please.
**nacho** 10:35 Yeah, I think there was a link previously, right, in the… in the… in the notes?
**Zoom user** 10:41 I don't see it in here.
**nacho** 10:44 No?
Yeah, I remember we were talking about this.
**Zoom user** 10:56 There it is.
Let me just… Okay.
Maintenance mode, yep, yep, yep, yep.
I'm just going to read only in a few months.
Okay. Is this something that we've published, or… Is this just a working document at the moment?
**Ari Demarco** 11:59 Interesting.
**nacho** 12:00 a working document, I think, but we… Yeah, the thing… TTLDR, September last version, right? Yeah. And… I mean, that's the idea. If something we find broken, we still have some time to fix that. But the idea is… September is the last… 30th of September is the last day we are gonna publish something CocoaProots related.
And we expect that to be the last version that we will ever.
Ever. Release.
Okay.
Which… which makes sense, give us 3 months in case we release something that's broken, so we can… have something that works, but we are not promising anything after September 30th.
Yeah, that.
**Ari Demarco** 12:45 Also…
**nacho** 12:46 about the documentary.
**Ari Demarco** 12:48 Also, some… some things to maybe discuss if… if we wanna… provide some other… associated mechanism to distribute, like, providing XE framework scripts to generate OpenTelemetry API SDK, or host, in each release, the XE frameworks of OpenTelemetry API SDK. At the same time, if we want to keep the pod spec files or not.
If we want to generate, Another repository for specs, because if we want to maintain this, it should be a private spec.
I don't know, like, to… to be honest, what I would do is basically just remove everything, leave the pod spec in case somebody wants to fork the repo and have their own version of this.
we can even… I don't know if there's a company that wants to host them and be, like, the official one that we recommend, I think we can do it.
M.
But once we… we all agree on… on the things we want, and we may don't… we don't want to have.
We would create an issue or post something in the blog.
Let people come to contribute, and after a month.
There's no… there's nothing else to be done, like, we just go into the path of depregating this.
**Zoom user** 14:15 Yeah, okay. I think that's reasonable.
Yeah, leave it open to see what, what feedback we get regarding, like, what the next step forward is, but yeah, I feel like if we don't really hear anything, then probably just remove it all, or… And, and not worry about it.
**nacho** 14:36 So then we might… Yes, share this document.
In the channel already?
The percata announcement says July, so we are in July.
And I think it… if the… we just… I mean, we had talked about it once, it makes sense, we have… at least, for me, it makes sense.
Still, I don't know if you prefer to think a bit more about it, Bryce?
Before really, publishing this document, maybe we can also… Change something, if we get some feedback, that will… Done.
aspect.
But, yeah, I think sharing this document in the channel now Or later, I mean.
Now will be great, so people have also time to think about it and ask for things if they need.
**Zoom user** 15:33 Yeah, I'll give it a read-through, and if I have any notes, I'll just add a comment on there. But otherwise, maybe I'll try to get that published as a blog post? Does that sound good?
**vinodv** 15:47 Yeah, that's so…
**Zoom user** 15:47 Through TNFC?
I'm not really sure how to do, but I'm sure there's an easy way to do it.
**Ari Demarco** 15:55 I, I would also…
**vinodv** 15:57 Yeah, there are some community blog posts like this for deprecation.
**Zoom user** 15:59 None.
**vinodv** 16:00 Yeah.
**Zoom user** 16:01 Yeah, we can post it in the Slack channel, too, and…
**vinodv** 16:04 Yep.
**Zoom user** 16:06 Cool.
**Ari Demarco** 16:06 We… we can open an issue, too. So, because one of the first parts is basically gather community feedback or stuff like that, we can just open that issue.
In case somebody wants to give feedback or something like that.
And we can close it once the date of the document, I don't remember which one is. Recommended migration period begins, like, August 31. We just closed that issue as Sold, and that's it.
**Zoom user** 16:34 Okay, yeah. Oops. Yeah.
Ari, can you, can you do… create that issue?
**Ari Demarco** 16:51 Yeah, sure.
Thank you.
Shall we do it after the blog post, or we'll do it right now?
**Zoom user** 16:59 Let's do it right now. I think it's fine.
**Ari Demarco** 17:01 Okay, I'll do it, and I'll share the issue on the channel, the Slack channel.
**Zoom user** 17:06 Cool, sounds good.
**Ari Demarco** 17:08 shall I use a here for this, or… or not? Because, like, there are, like, 130 people, or something like that. No, 260 people in the channel.
**Zoom user** 17:19 I don't know, yeah, probably.
**nacho** 17:22 Oh, really?
Yeah, that's quite… yeah, Putin now, here, yes. At here. I see.
**Ari Demarco** 17:29 Okay, awesome.
**nacho** 17:30 That's important enough, right? If they are in the channel… That's true, yeah, that's get notified.
It's…
**Ari Demarco** 17:35 Okay, cool.
**nacho** 17:36 It's something you must… This is the kind of thing you really want to get notified.
**Zoom user** 17:41 Yeah. Just in case.
**nacho** 17:42 Right?
**Zoom user** 17:42 Hmm, yep, yep.
**vinodv** 17:44 Next meeting will… next meeting will have a lot more people showing up.
**nacho** 17:48 Yeah.
**Zoom user** 17:51 Rabble, rabble, rabble, rabble.
Oh yeah, CodeQL is breaking.
It's, I guess…
**Ari Demarco** 18:10 I wasn't able to look at it, to be honest.
VIN.
With a bunch of stuff.
Happening.
**Zoom user** 18:29 So Elastic let me keep my laptop, but I haven't set it up all the way yet, so all my, like, hotkeys are not… I'm not right.
I like to swap caps lock with, like, control, and so I can more easily… I just keep turning on caps lock now.
Okay, so let's take a look at one of these pull requests, and… oh.
Is it only in… That's weird.
Oh, I'm not signed in, that's fine.
Okay, hold on a second.
I have credit load.
Sorry.
Okay.
Alright, so… The issue is related to, Concurrency, yeah. So this is… this is the reason why I was thinking we need to get that other issue, that other PR merged.
That adds the syndables, onto various things.
**nacho** 20:17 Okay.
**Zoom user** 20:17 That's the cause of this, yeah.
**nacho** 20:20 So it's… it's… yeah, that's why you mentioned Swift-related, right?
Yeah, so in that, in that branch, it is… CodeQL is… is passing the test in the…
**Zoom user** 20:36 In this one? Oh, in, in that branch, yeah, here, let's take a look.
**nacho** 20:41 Yeah, that's… Yeah, because I typed in…
**Zoom user** 20:46 Yeah.
Yeah.
**nacho** 20:57 Okay, yeah, impressive there. Great. Yeah, I… great.
**Zoom user** 21:19 There's a… There is a, sister issue in… the main repo… oops.
But it, it's, it's pointing at, Let's having some issues, too. It's pointing at the, that, the, the, yeah, here.
It's pointing to his PR branch, so we can get that merged, and then do a release of Swift Core, and then we'll be able to correct this, and then it should be working again.
Okay.
Oh, here we are.
CodeQL to be reviewed… Okay, log warning, duplicate message…
**nacho** 22:18 Yeah, that, that was not solved.
Remote.
**Zoom user** 22:22 Right, yeah, so we went… I forgot about the feedback handler, so that's good that we're using that.
This is probably something that… We need to be more diligent about, because we have a lot of… spots in code where it's like, error message here. So we should probably, now that we have that feedback handler, go back, review it, and Get those implemented.
Yeah, so… That's good, so we'll get that in there. So, not here, up here, new topics… So, swift Core to do, Yeah, see, I'm trying to do CTRL-E all the time, it's not working.
let's create an issue for, adding a feedback handler.
to, stubbed error message.
locations.
We can do this, too, in, in the main repo.
But we don't need to use the feedback handler, we… the main repo has SwiftLog in it.
I don't remember why we decided not to add SwiftLog in the core. The main issue that we had when I recommended it, just the OS version, or the watchOS version target is too low for it.
So we don't… I don't think we need to touch… mess with that, since we have this feedback handler.
**Robert Magnusson** 24:16 What is that feedback, Andrew? Sorry for…
**Zoom user** 24:19 The feedback handler is… is just a stub, or it's just a wrapper for… for a, log message, and right now we're using OS log. However, OSLog's not available on Linux, so we added the feedback handler so that, you know, anybody using Linux who wants error messages can feed whatever logger they want into it.
I think Swift… SwiftLog does work on Linux, so.
**Ari Demarco** 24:48 Yep.
**Zoom user** 24:49 That, that's, another solution that requires less work for people on Linux… on using Linux Swift. But yeah.
**nacho** 24:57 Yeah, but adding dependencies to SwiftCore.
**Zoom user** 25:01 It's not great, yeah.
**nacho** 25:03 It's the reason we created SwiftCore, right?
**Zoom user** 25:06 Yeah, yeah, that's fair, that's fair.
Okay.
Shall we review some issues? Some PRs, maybe?
Let's start in the main repo. Well, actually, there's not really… there's not really a lot we can look at, because everything's kind of broken right now.
So, I think the first step is… Oh, I'm in… Let's… let's go to corner.
Yeah, and the same issue here, there's a lot of build failures, I'm guessing what happened was… Was it maybe, like, this, I think that that CodeQL thing uses this Docker, right? Is that the… Is that the problem? It got bumped to… oh, that's Swift.
1.
Hmm… I'm not precisely sure why this has all of a sudden started to be a problem.
Like, did we… did we bump to Swift 6? Is that what happened? Yeah, that's what happened, isn't it?
Oh, that's weird.
That was a while ago, though.
**nacho** 27:09 Yep.
**Zoom user** 27:13 I wonder why that just started… this just started to… to happen.
Curious.
But anyway… I think this, this is the…
**Ari Demarco** 27:29 Maybe… maybe CodeQL changed the version of CodeQL or something like that, and now it's using a different suite version.
**Zoom user** 27:37 Yeah, that could be it.
**Robert Magnusson** 27:41 Yeah, I opened up CFR.
I opened a pull request some time ago for the session manager config, and run into that issue also, and run some cloud code back and forth.
And I think what it reported on me is that it was a change with SwiftCore 250, where the log record… log record exporter became sendable.
And that costs… I mean.
**Zoom user** 28:07 That's not a good quality.
**Robert Magnusson** 28:08 do you think, but that's the… the… the, the threading thing, I guess.
**Zoom user** 28:33 3 weeks ago, 2 weeks ago, yeah, here it is. I'll do a little investigation after the fact, Yeah. I'm just a little curious as to why, why this started to happen. So I opened this PR, this was something I noticed in some of the builds as well. So, Ari, you added, added this, Resolve Simulator, script? Yeah.
But it's still, funny enough, if it's on architecture ARM64 or x8664, they have the same ID, so it's still running into this stupid problem.
**Ari Demarco** 29:15 Wow.
**Zoom user** 29:16 So, so, I just, I just…
**Ari Demarco** 29:23 That's a brigade watch for us. Yeah.
**Zoom user** 29:26 Yeah, yeah, so I… so… I just added this in there. Yeah, I think the only.
**Ari Demarco** 29:31 Yeah.
**Zoom user** 29:32 Well, yeah, the only place it's a problem, is in… Is it in SwiftCore? Yeah. We have a couple of tests that test time, like, the back-offs on certain, like, error responses, and if it doesn't fire quickly enough, then it fails it. But the problem is it'll be, like, 5 seconds longer than it should be. It'll be like, oh, it should have been 2 and a half seconds.
But if it's running the wrong simulator, then it's, like, really slow. So, yeah, that's the main problem why this keeps popping up.
But, so that's…
**Ari Demarco** 30:11 Simple.
**Zoom user** 30:12 little change of… oh, Nacho already approved it, so… I'll just… I'll just merge that.
So that should solve some problems with flaky tests.
Improve, renovate Docker handling.
Oh yeah, it just bumps this container that we use. Yeah.
Which is specifically for the Linux stuff.
Yeah, build tests for the gun, so… It just bumps out version, not a big deal. Oh, and it adds that matchup type.
Or match update type.
I think that, yeah, it's not worthwhile, I'm looking through this stuff right now, cause it's all broken.
But yeah, we just need to get this one merged, and basically all it does is it just adds some… You know, this sort of stuff, to make it a little bit.
**nacho** 31:21 vulnerability, yeah.
**Zoom user** 31:22 Yeah.
I was hoping Billy would be here, because I was kind of worried that this might kind of step on his Swift 6. Oh, I guess, did we merge that? I can't remember.
**nacho** 31:33 the… yeah… The original branch from Billy is merged.
**Zoom user** 31:37 Yeah, okay, yeah, so this is just some updated.
**nacho** 31:40 Yeah, yeah… It's also, I think it's also… I also approved it.
I think…
**Zoom user** 31:47 Oh, okay, good. Yeah. There were some issues, like, some of them needed to be unchecked. Specifically, like, the dispatch queue was,
**nacho** 31:56 Oh, yeah.
**Zoom user** 31:57 Support Linux, yeah. For some reason, it's okay on the Mac… with the Mac libraries, but it's not in the Linux libraries, so hopefully that isn't actually a problem on Linux. This will need to get refilled.
**nacho** 32:08 Yeah, probably… yeah, it… Probably it's not properly annotated on the Linux side.
**Zoom user** 32:15 Yeah, that's what I suspected as well, yeah.
Okay.
So, we can merge this, unless anybody else has any problems. Ari, are you okay with that?
**Ari Demarco** 32:27 Nope, I'm gonna go with that.
**Zoom user** 32:29 Okay, we'll get that… we'll get that merged.
Let's see, so… I'll get a release spun up here for this one.
And then we can get a.
**nacho** 32:43 Yeah, there is also another… another very small one, the third one I also reviewed.
**Zoom user** 32:49 This one here?
**nacho** 32:49 And, yeah.
It's just that a small spec change with the…
**Zoom user** 32:57 Oh, yeah. Okay.
**nacho** 33:00 It has asthma ticks. So, yeah.
**Zoom user** 33:04 Okay, cool. You wanna… you wanna merge that, too?
**nacho** 33:08 Yeah, I think, I think so. I mean, it's so simple, it… Yeah, if it fixes something.
**Zoom user** 33:15 Pretty good. Cool.
Cool, cool, cool.
**Ari Demarco** 33:21 I reviewed APR that is below there, like, it's the URL session, something like that. Url session instrumentation, so it's also always
**nacho** 33:32 But that, that…
**Ari Demarco** 33:34 Oh, that's.
**nacho** 33:35 non-coral, right?
**Ari Demarco** 33:36 Yeah, yeah, it's a suite. My bad, my bad.
**Zoom user** 33:39 Hi, host.
boat.
Let's take a look at that.
from here.
**Ari Demarco** 33:47 That one, yeah.
Because… I… I added… I rejected it two times.
And the last comment… I think he's wrong, but, maybe I'm wrong, because… what I'm saying, basically, in my comment is, hey, you are calling the completion handler after calling the original method.
Like, if you see their code, inside this result method, they basically call the original one, and then it adds a completion that allow.
Which means it's going to call the completion block twice.
And the second one we don't allow, which is a safe default, let's say.
But… I don't know what would happen on iOS if you called the same completion handler twice.
In the… in your session, which is… Black magic. So, I don't know.
Am I wrong on this one? Seems like… This is a dangerous thing to do.
**Zoom user** 34:53 Yeah, I don't… I don't… just basic… based on looking at this, that doesn't seem right to me either.
**Ari Demarco** 35:09 And his response is not really under… I didn't fully understand the response from him after my comment.
like… Broker is not…
**Zoom user** 35:19 It's not actually calling it. In the previous implementation, the original implementation that was being swapped, wrapped, would do the calling.
Well, we're… Well, we're calling the original implementation, aren't we?
**Ari Demarco** 35:36 Yeah, when you are calling south.urlsession session session.
**Zoom user** 35:39 Yeah.
**Ari Demarco** 35:40 State the task.
In… in there, we are calling it.
**Zoom user** 35:44 Yep. Yeah. Precise thing.
Yeah.
**Ari Demarco** 35:53 And I'm also worried because he mentioned he wasn't able to run tests.
So… I don't know, I don't think this is accurate, but…
**Robert Magnusson** 36:18 That's something that the URL session instrumentation is not calling it. Is there an update to that Swift, Arenal.
Is that what it means?
**Zoom user** 36:29 Oh, see that?
**Robert Magnusson** 36:29 URL session… does it mean that URL session has an updated implementation?
**Ari Demarco** 36:35 So…
**Zoom user** 36:37 Go ahead.
**Ari Demarco** 36:38 No, no, the PR at all, it covers a case where the reasoning is not working, which is completely fine, but what is happening here is that After swapping and after calling the original implementation, for some reason, it's calling a completion handler again, which is weird.
That's my whole comment on this, like, the PR itself and the logic of the PR was good, I made some good suggestions, something that would crash, or something like that. And after he made some changes, I saw this, and I was like, okay, this completion allowed, it's… Isn't necessary, for sure.
Unless we want to call that in our implementation, but… We don't want it.
**Zoom user** 37:20 response disposition.
**nacho** 37:22 Yeah, so the original implementation could be calling completion with a law, or deny, or whatever they want, right? That's the thing. We shouldn't allow PR just because we are reimplementing it.
Yeah.
**Ari Demarco** 37:36 Depending on how OAS compiles under the hood, the completion block, or the block itself called, now it's garbage. So that completion allow, I'm worried it's going to also crash.
**nacho** 37:50 Probably, probably it does nothing, I would say. Probably will be discarded, by, by, by the inner framework, but yeah, the Finley is not doing anything, because The handler should be… Called, right?
**Zoom user** 38:04 Is it possibly… is it possibly the case that, this is one of those, those callbacks that… if… if it's not detected on the… on the delegate, it will do something under the hood that, like, it'll… it'll do allow, basically, under the hood. Yeah. And then, because we're swizzling it, we're telling the delegate that this method exists on it, but then, if the actual implement… implemented delegate That we are swizzling doesn't have this method implemented on it.
then it… it's messing it up by… by… and calling something that's not actually calling the completion handler, basically, right? And so… Then he's saying that we need to call that allow, Because we're, we're, Interrupting the default behavior when there's no method detected.
I'm wondering if that might be what's going on.
But I think that what we probably need to do is get some… or at least verify the tests. Maybe… If he says that he couldn't.
couldn't run the tests. I haven't been actually able to run them.
Okay…
**Ari Demarco** 39:31 He's the one that built the changes for the concurrency thing, so maybe once that's merged and there's a release for that, I can… Go copy this branch into my… My local machine, merge the changes, run tests.
**Zoom user** 39:45 Yeah.
**Ari Demarco** 39:46 If this works, But… I wasn't sure if it would be good to approve it, considering.
**Zoom user** 39:54 Yeah, I mean, I definitely agree that that should not… the completion handler call should not be there. But there might be something else going on under the hood that… that makes it appear like it ought to be there.
Yeah. Yeah, and what we might need to do is do a check on the delegate we're swizzling, and verify that that method's on there before trying to swizzle it.
That might be the problem.
And we can, we can check that, in the tests, possibly.
M… But, yeah, we definitely shouldn't approve this just yet.
But I'll also follow up and take a closer look and see if that's the case. My theory is the case or not.
And get that, but yeah, it'll take that, PR getting merged first before we can… Check that out.
Okay.
Robert, was there anything that… any topics that you wanted to discuss at all, or are you just hanging out?
**Robert Magnusson** 41:02 I'm partly hanging out, trying to get into this group a bit, and seeing how you work, and… Sure. My goal is long-term contributing more here.
**Zoom user** 41:09 Oh, killer.
**Robert Magnusson** 41:10 I also…
**Zoom user** 41:11 Probably more of those.
**Robert Magnusson** 41:12 Yeah, okay, so… But I also have a PR, but it's also depending on this, on this broken test, test passing, so we can just postpone it until next week.
**Zoom user** 41:24 Sure, sure, yeah. Is that, oh, is it on the main repo, or the…
**Robert Magnusson** 41:29 Not in the core, in the… in the… which one is the main is main?
**Zoom user** 41:33 The main one is the not-core one. Okay.
**Robert Magnusson** 41:36 Then it's in the main one. It's the sys session manager config… wait, I can see if I have it here.
**Zoom user** 41:44 the config.
**Robert Magnusson** 41:45 It's a bill, PR number…
**Ari Demarco** 41:49 Yeah, configuration, like, cycle rules.
**Robert Magnusson** 41:52 Yes, 1107.
1107.
**Zoom user** 41:58 Oh, this one here, okay.
**Robert Magnusson** 42:00 Yes, sir.
**Zoom user** 42:02 Right.
**Robert Magnusson** 42:06 Yeah, I was just running into an issue, because we're trying to build this for Grafana, and in the Android and in our fatter world, we have, like, this control where we say, like, we want the session to be max this long, and every clean start of that, we're in the others expecting it to be a new session.
I'm not sure, like, what is the correct behavior according to the… to the hotel semantic spec, like, how it should behave, but I think it's an open-ended, not done decision, how session should behave in a case where you kill the app. So that's why I thought it might make sense to offer this configurability, at least. Yes.
**Zoom user** 42:40 Yeah, I think… I think we've taken a look at it, and I don't have any issues with it. I think that the problem is just the build. Yeah. Yeah.
**nacho** 42:47 Yeah, it's not actually really took a look.
Right, yeah. Yeah.
But yeah, the problem was that we couldn't… yeah, it was always saying we couldn't match, but it was. I don't know if that works, but it was…
**Zoom user** 43:12 Sorry, Nacho, you were breaking up quite a bit. I'm not sure…
**nacho** 43:15 implemented some of this in the past.
Can we, can we… Crystal, we didn't approve that much was, because it was an opinion.
There were some issues when you think that.
The test doesn't run, or we cannot make them run again.
In comments.
**Robert Magnusson** 44:00 Sorry, it was a bit tough to follow. It's chopping up for me, I don't fully hear.
**Zoom user** 44:04 I can't. Maybe try turning off your video, Nacho. For some reason, you're crystal clear, but the audio is not coming through at all.
**nacho** 44:11 Okay.
**Zoom user** 44:12 I wonder… or maybe you're… you're… the… Nope, still… still really garbled.
**nacho** 44:23 Okay.
**Zoom user** 44:25 But anyway, I don't see any reason why we can't approve this. I think we've just been holding off because of the build issues.
Yeah.
**Ari Demarco** 44:36 Yeah, I checked it out, and it seems like that.
Yeah. I have a quick topic to discuss, if there's nothing else to review.
Sure, Kim.
I think it was a month ago or something like that. We were discussing with Natural ambulance, if we can use trades.
for the SPM thing, to actually simplify the flows on having OpenTelemetry, Swift and Core, because it's kind of cumbersome.
I shared, kind of a post.
on the internal Slack channel, saying that it's not going to help.
But I was thinking, while I was finishing writing this doc from Cocoa Pots.
That one thing that we may wanna do.
Instead of having a specs repo.
we could have, like, the OpenTelemetry Swift Core repo, which will only… Hub tags and information related to… They, have a new package thrift that aims to a binary.
So, we could have an XD framework, That it's basically core.
And that's basically it. So, OpenTelemetry Swift Core will have, only a package Swift, will be the host of XC Frameworks.
So… we won't have any people that just want Swift, OpenTeometry, Swift Core API, and the other one, SDK, will just go download that, it will be super, super small, it will be super casual, which is also going to be a better approach.
If they have issues.
the only issues that could arise is that two or more SDKs, let's say Datadog, Embrace, and another one.
would want to use the same OpenTelemetry repo. They use different versions of the XT framework, and that will collide. That's the only potential problem that we could find, but in those cases, okay, go and use the official one, and that's it.
Just throwing that as a possibility, because maintenance… It's complicated, with just… the four of us, hopefully Robert could also help, but it's getting…
**Zoom user** 46:58 Two-door quick rubber.
**Ari Demarco** 47:00 it's getting cumbersome, and in particular, with all these swift changes between 6 and 5.x version, the different Xcode versions, the different macOS versions, like, it's… it's… it's not easy. Or we should really, really invest into improving the CI.
Or I think we should have a plan, too.
I don't know if unifying, again, everything, but at least having that separation in a different way, like, use Core as, okay, this is the exit frame workplace. Do you want the core SDKs? You can download it from there, and that's it.
**nacho** 47:38 Yes, I guess, how about, I mean… like, Get some volume that just point to a formula in the other.
Industries could triple.
And the fifth part is just, a super lever.
Oh, fantastic.
**Ari Demarco** 47:56 It's a module, you mean?
**Zoom user** 47:57 Yeah, submodule for SwiftCore.
**nacho** 48:00 So yes, something like this, just, other insight they have it for you.
I guess, comes to that from the Corps, and we have the insurance to do everything there. And you go to the core in Tony.
accept.
So, whenever we want to release an impression, we just change The person that you're talking about.
expansion, and… 19.
**Ari Demarco** 48:31 Yeah, that's…
**nacho** 48:31 Oh my gosh.
**Ari Demarco** 48:32 That's easier.
That's easier, but managing suit modules, it's also somewhat painful.
like, I used it in my previous company and in this one. It's good because you don't have to go and switch between all your branches, all your places, but… to switch from local to remote and all that stuff, it's not easy, too. So, I don't know, we may want to invest some time into defining what is the best approach.
But having…
**nacho** 49:06 I, I see the paperwork is, is, is 90 hours the most part.
**Ari Demarco** 49:15 I think your audio is chopping a lot. I don't know if it's the headphone.
**nacho** 49:21 Sorry.
Many, countries.
**Zoom user** 49:24 Yeah, because your video is fine, so yeah, maybe your headphones are doing something weird, maybe the Bluetooth connection is poor.
**Ari Demarco** 49:31 AirPods… AirPods are… are behaving bad today.
**Zoom user** 49:35 Yeah, yeah.
**Ari Demarco** 49:36 My Mac is not working, your AirPods are not working, so… Apple is… Apple is not happy about this.
**Zoom user** 49:43 Yeah.
But lucky for Apple, Windows is working.
**nacho** 49:48 What not?
**Zoom user** 49:51 Neither are good.
**nacho** 49:52 And you're criminal?
**Zoom user** 49:53 Yeah, there you are.
**Robert Magnusson** 49:54 Yeah.
**nacho** 49:55 Okay, yeah, I changed to the, to the laptop.
Yeah, I don't know, but yeah, we knew it was gonna be hard to have two, repositories. We have seen that it is even worse than we expected.
Doubly… more than doubling maintenance. We are also having problems with things that are not building on one side because we have not released the other, and we cannot be fluid at all.
So, yeah, I don't know, maybe Git modules is not a solution, because it cannot… I thought it… I don't know, we just need to point to a different commit version each time, a different point in another folder, which might be just a folder. I don't know if that would work.
But something like that will be perfect. Just for these companies, we told them to do exactly that.
to do, to have their own Zoom modules, just to… to re… to re… To check from there.
But they didn't want to, change to that, and we did it ourselves, but maybe we… we could go to that world, I don't know. But having different code.
with different versions and different things in two repos is… Extremely painful.
**Zoom user** 51:20 Yum.
It definitely causes a lot of problems.
Hey Ari, I don't quite understand your proposal. Do you think you could write up, like, an issue and kind of describe it that way, so…
**Ari Demarco** 51:36 Sure.
**Zoom user** 51:37 discussion there.
**Ari Demarco** 51:38 But basically, it's going back to the roots, everything on OpenTelemetry Swift, like the repo, everything.
And in OpenTelemetry Core, SwiftCore.
We would just have a package definition, a package.swift, with binary targets exposed.
those binary targets are going to consume XD frameworks that are generated inside there.
**Zoom user** 52:02 Oh, I see what you're saying. Okay, so we re-merge the API and SDK into the main repo, but then.
**Ari Demarco** 52:10 Sounded.
**Zoom user** 52:10 job that generates just the framework ex… or, like, the SDK and API frameworks in In the, in the, into XC frameworks. Okay, I see, okay. Yeah. Yeah.
**Ari Demarco** 52:24 One, one example, like, Ehh.
**nacho** 52:28 The problem is that you have to generate an XC framework for all the platforms, And all the simulators.
I mean, that means a lot of builds. You have to build for, probably, Intel, still Intel and ARM.
Oh, let me…
**Ari Demarco** 52:47 The thing is that…
**nacho** 52:47 also for Lina.
**Ari Demarco** 52:48 Absolutely.
**nacho** 52:49 And also, it's…
**Ari Demarco** 52:51 But this is a requirement just for people that are distributing SDKs.
And that is taking long for CI, because on the back end, you don't really care at all the… how heavy it is the CI, because you're probably downloading images and a lot of stuff that is way much heavier than a repository. So… I, I think field for TDOS, macOS, WatchOS, all of them, like, generating the exit framework is just slices. It's not that complicated, it's just one XE framework for each.
And that's it.
Bye.
**nacho** 53:31 And something like just copy All those folders into the other repository whenever we create a release in the main repository.
just copy… those folders.
**Ari Demarco** 53:43 Oh, like, I'm in a mirror.
**nacho** 53:45 Yes.
**Ari Demarco** 53:46 I mean, that mirror.
**nacho** 53:47 Yep.
Yeah, just with those folders.
**Ari Demarco** 53:52 I guess that could be also a possibility. Like… .
**nacho** 53:56 We don't.
**Ari Demarco** 53:56 Many companies.
**nacho** 53:57 Satan, we just copy The code that is in that folder, in that repository, and we maybe also create a release whenever we do that in the main repository.
**Ari Demarco** 54:08 That is a really cool idea. Like, at my previous company, we had, like, a public mirror and an internal mirror. We worked in the internal mirror, but the code was public, so every time we did a release, it was… Moved back into the… the… Officially, the public repository.
It was a bit inconvenient when people wanted to do contribution, that's why we made everything public.
But for us, that we have both repositories as public, it's… it's okay, like, we just… we can have a simple bot that every time there's a PR generated, or something like that, says, okay, go and submit this into the other repository, and that's it.
**nacho** 54:47 Or just when we release, because we don't need to keep… I mean, we don't want anyone to use the core repository.
Yeah. So we block that repository, we only allow Committee NAS, and whenever we create a release on the main repository, it creates a copy of the API.
**Ari Demarco** 55:06 Two folders.
**nacho** 55:07 folders, just copy to the other repository, and If possible, create a tag with the same number. That's all. And whoever wants to use that crate, whoever wants to create a PR there, they are blocked. They have to create a PR on the main repo.
**Ari Demarco** 55:24 I think that's an Islam idea.
**Zoom user** 55:25 Yeah, that's a cool idea, I like that.
**Ari Demarco** 55:29 Okay, I'll create an issue with that idea.
**nacho** 55:32 And we can continue working.
It will need to…
**Ari Demarco** 55:35 That's crazy.
**nacho** 55:35 MCI work, probably, on the release.
Face?
**Ari Demarco** 55:39 Yeah.
**nacho** 55:39 But, yeah, we, we, we closed that.
I mean, we make that read-only, right? Yeah, yeah. For everyone except the…
**Ari Demarco** 55:49 Yeah.
**nacho** 55:49 internal.
**Ari Demarco** 55:50 I think…
**nacho** 55:50 Copy.
**Ari Demarco** 55:52 I think Bryce has a good idea on how to do that, because he had to deal with all the Terraform files.
**Zoom user** 56:01 I don't… I don't. But I can try to make it happen, we'll see.
**Ari Demarco** 56:07 Yeah.
**Zoom user** 56:08 All right, cool. I think that's… that's good for today. We're running up on time. Any other… anything else anybody wants to mention before we go?
Nope.
**Ari Demarco** 56:21 I'll create the issue about that, related to that. Probably I'll mention Nacho's proposal. I think that one is way much better than the one I did.
**Zoom user** 56:31 Cool, yeah, right on. Sounds good. Alright, have a great rest of your week, everybody. Happy 4th for… oh, I guess there's… whoever's in the US, happy 4th of July. Happy qui… semi-quincentennial.
**nacho** 56:43 Thank you.
**Zoom user** 56:44 250th, 4th of July?
It's kind of cool.
**Ari Demarco** 56:47 Enjoy… enjoy your holidays, guys.
**nacho** 56:49 World Cup matches this weekend host.
**Ari Demarco** 56:51 Yes, tomorrow. Tomorrow is, is, is a big one.
**Zoom user** 56:55 Oh, no, darn.
**nacho** 56:56 today, also.
**Ari Demarco** 56:58 Oh, today.
**nacho** 56:59 Yes.
**Ari Demarco** 57:00 Relax Spain. Relax Spain.
**Zoom user** 57:02 Oh, yeah, okay.
**Robert Magnusson** 57:03 Yeah, good luck.
**Zoom user** 57:04 See ya!
**Ari Demarco** 57:05 Bye. See ya.
**Robert Magnusson** 57:06 Bye bye.
