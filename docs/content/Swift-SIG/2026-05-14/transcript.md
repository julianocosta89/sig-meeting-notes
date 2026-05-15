SIG: Swift SIG
Date: 2026-05-14
Duration: 42 minutes
Zoom Recording URL: https://zoom.us/rec/share/FuTZWtpMtZoGFZzfGdmZ_zkyBo0hA59R3OWexcoAMrYMC3mcDMUtudH-6bj9zV4X.QBIkV_t8RW3P1Rx9
============================================================

## Zoom Recording Transcript

**nacho** 05:08 Lowe?
**Billy Zhou** 05:19 Not true.
**nacho** 05:21 How are you?
**Billy Zhou** 05:24 Good.
**nacho** 05:31 Yeah, I don't know how many people is joining today.
Bryce said he couldn't.
Also… Be not said he's joining late.
It's joining at all?
And I don't know about… Ali… Notice seaweed.
damaged that, if not.
I also don't have much time today.
So… Alright.
Okay, so… yeah.
Let's start. If anyone joins, we can always recap from there.
So let me, sir.
the notes… Yeah, these are old… I just copied now, so… renew wheels… things from here.
I don't… To write the job.
your, training call.
Sorry, if not. Okay, so… Let's track what we did last week.
So, release two for one, you raise your hand, Billy?
**Billy Zhou** 07:05 I didn't misclick. I kinda see what this Fireflies AI note-taker thing is, and just, yeah.
**nacho** 07:11 Yeah, okay, I don't know what this note ticker does.
but, okay.
So, last week, released 2 for 1, I think it has been already released, right?
I think so?
I think, price released on Monday.
Say I'm a branch… No, it's not been released.
Oh, maybe it's… Please release. Okay.
Yeah, I think it needs some cleanup with all the updates to the core dependencies.
Oh, this is crazy.
Yeah, I think it thinks it needs some cleanup, removing all this.
and make it… Available for everyone.
Oof, this is crazy. Maybe we can… Thrugged it.
Later, if we have some time.
But yeah, I don't know. Okay, prevaced Swift… Version 6, PR.
This is your PR.
Anything here?
**Billy Zhou** 08:45 I think it just needs Bryce's review.
**nacho** 08:48 I reviewed, I think, right? I'm starting, I think.
Oh, yeah, this one.
okay, you are… you address it? No.
No, no.
**Billy Zhou** 09:04 Oh, they're an AI.
**nacho** 09:05 Yeah, the thing is, yeah, we have this… Values there, and it's like… Much safer, using those attributes directly instead of the… of the… Of the row of strings that… can always, you know, be, it adds, type, security everywhere, so we don't miss any, any update in the future. So, yeah, just that. For the rest, I think it's… it was very, very nice.
I… I think Bryce was gonna review everything also, so yeah, that… that would be… Then, so that script work.
Ali has not said anything, about, this PR, he has not contacted also in the channels.
So… He'd probably continue with this.
Yeah, Bryce will start a release yet. He created a PR with the release, I approved that, and he created the pre-release version, I don't know if that should be… also… Two, done.
Yeah, I don't know if it has been tested, At all?
10 seconds.
Okay.
Yeah, I think that… that's… What do we have?
From the last week… Okay.
**Billy Zhou** 11:09 I also.
**nacho** 11:13 Hey, Eddie!
**Billy Zhou** 11:14 Yeah.
**Ari** 11:17 Hey guys, how are you?
Bye now.
**nacho** 11:20 How are you?
**Ari** 11:23 Fine, receive…
**nacho** 11:27 Precinct, really?
**Ari** 11:29 Yeah, yeah, yeah.
Here, it's, you can check.
**nacho** 11:33 Yeah, I… Yeah, I, I think… In May, you are in the wrong side of the, of the world.
**Ari** 11:40 Yeah.
It's… oh, it's… it's not that bad.
Cold. It's 13.
Degree Celsius?
**nacho** 11:48 Okay, yeah.
**Ari** 11:50 It's bad, that, not that bad.
**nacho** 11:55 Yeah, it's coming across here, at least in Spain, we… Yeah.
Yes, big… Some 20-something this weekend.
**Ari** 12:05 Yeah, that's… that's really illegal.
**nacho** 12:09 Okay, yeah, we were reviewing, last week.
Things, We… the Swift 6 PR from Billy has been, reviewed, some… some more. There is just some more feedback there.
Probably Bryce will also review, and, yeah, you are also open to review it if you… won't… it's a very big PR.
Yeah.
**Ari** 12:38 Yeah, yeah.
**nacho** 12:38 But yeah, it's… I did review it, and, and it's quite, quite good.
Just a nitpick from my side. I don't know if any… Bryce said he will review, probably, so maybe he has some more. This is an important PR to have.
**Ari** 12:57 Yep.
**nacho** 12:58 So, yeah.
So the next…
**Ari** 13:02 Jeff.
**nacho** 13:03 Topic was… yeah, we had talked about… you said that you started changes to the package to incorporate Yeah.
This change that was there.
**Ari** 13:18 Deprecation.
off their…
**nacho** 13:21 It's kind of.
**Ari** 13:22 Yeah, yeah. I basically started reading and generating I'm creating, like, a sample app to have myself, like, now that I left the… So, I'm creating sample apps to test all those changes, started the overall design.
I'll raise a draft with the overall idea and interfaces and changes.
If we are all right with that, I'm going to finish it eventually, with all of that.
I will probably merge this after Billy's… 56 PR, probably. I don't want to mess with that.
I'd rather go and change my implementation, rather than… Forcing him to change his… V6PR is kind of big already. Yeah.
**nacho** 14:12 Yeah, probably we'll have some conflicts with your…
**Ari** 14:16 Yeah, but it doesn't really matter, because… It's going to be big, but not… as complex as… the B6.
**nacho** 14:27 Okay.
**Ari** 14:28 To be honest.
**nacho** 14:29 Great.
Yeah, apart from that, Bryce created a pre-release.
Of, of the, of the version.
Two for one, it's currently pre-release. I think it needs to update the… the… what's changed.
To, yeah, to be allowed to vote.
And I don't know if he has been able to test it, if it was working in any other project, before, going with a proper release.
But, yeah, I think we can… Yay.
whenever anyone can test that it works as expected, because it's just created, I don't know if it did, we can just release it.
If it works in… your scenarios, or… Or Billy?
I don't know if you can just run with that person some of your… current… projects that use OpenTelemetry and CP.
Just builds and doesn't fail.
That that should be enough.
Hello, Beanut.
**Vinod Vydier** 15:41 Me or two. Okay.
**nacho** 15:43 Yeah, and apart from that, I think we can start with reviewing, if you want.
some of the issues and PRs that are still open.
Let's, twist!
with Core, I think.
Yeah.
I think some issues… The potential has worked.
Okay.
Oh.
They are moving to not being so… so noisy, maybe? I don't know.
With the dependency changes.
I… Okay.
Yeah, so that… that's about… Addressing the dependencies in a different way.
It's good, for pull requests. I, I reviewed them.
this week, so I don't… I think I addressed attribute all that were open, And all these are… Yeah, documentation… This one… was for… Bryce, I think, because we were talking last week, he said that This was not the solution to be done.
but he had to… that was his code, so he still has to review.
Yeah, but he asked me about it… two weeks ago, maybe I can answer and say… This is what we told last week, but no one answered him.
with this big… aspects.
Yeah, very, very sounding.
yeah.
The other is entity POC, as I do not merge. He was working on it.
These are update versions.
This also… are dependency versions of… dependencies, so that, that, so, tracked.
Regarding the main library… Let's review.
Yeah, poor requests, I think I also reviewed. Many of them… Okay, there is… Something new there.
So, we are… this is the PR from Willy, version 6, in the review.
The distributed tracing bridge, now it's, unblocked, because I… I merged the PR that was… adding the possibility to add links to expans once they are open.
That had been also for review long period, so it will probably… Continue here… I don't know if there is some progress, probably not, right? I'm not sure.
Yeah, that last answer was… the PILL team.
Made to the core.
What was this about? This was a draft. This was a work in progress.
Yep.
Okay, yeah, so… bracelet feedback that we talked last week.
The Tristar updates, yeah, we have these other PR.
There are sessions to maintain more than one spam per request on what's always?
your assessment on whatsoever does public API calls instead of internal ones, so current instrumentation comes multiple times for the same request, and creates or find… Anyways… Okay.
Recession being sent in here.
Okay, that… It's interesting.
Yeah, I think it needs to be.
**Ari** 21:22 Yeah.
Also…
**nacho** 21:24 ass.
**Ari** 21:25 this… Tesla failing.
Maybe because of this.
**nacho** 21:34 Yep.
BCNOS.
**Ari** 21:38 edition.
**nacho** 21:44 Yeah, I think it must serve you.
Okay, because the rest… I've been married.
**Ari** 21:55 I'll check that one.
**nacho** 21:59 Yeah, the release was March, but it's in pre-release.
Just need validating and updating the… the… what's name?
Yeah, and also what's the… the network status crash that was reported twice by two developers with two different PRs, we definitely The rest of the… Why not?
And I think that's all. Oh, sorry, misuse.
Super Base from Supergolf.
This is the crash that was fixed already, so that was messed… Good fix.
Okay, yeah, I think this is the report regarding this.
Drop here.
Yeah, that's just waiting.
Brace at rest, yeah.
Okay, yeah, so that's about… Eat… all the topics are open. The only missing thing will be… Validating these feelings.
And change it to an official release. Yeah, most of the things are just… That appendage.
I don't know, the idea's value that it works as expected.
Yeah, if anyone wants to take a look and update what's changed, and change that to release.
Once validated, that will be great.
And I think there's nothing more.
Any other topic you have?
**Ari** 24:11 No, not really.
There's one thing that maybe we should discuss eventually, that is, what are our plants with cocoa pots?
You know, we have an issue to make that better for releases and other stuff.
I think it was… everything went well in this release, but maybe having, like, a… I don't know.
A long-term idea, if we wanna support that, or if we don't wanna… If we should let people know about that, etc.
**nacho** 24:49 Yeah, that's a good topic also, because cocoa pots is… .
**Ari** 24:55 Yeah, they support this.
**nacho** 24:56 Right?
**Ari** 24:58 Yeah, as time goes by, the support is… going to be dropped from some…
**nacho** 25:07 Yeah, I agree.
**Ari** 25:08 Like, I found out that some… Important that DK started.
saying, okay, this is our last release with Copos and stuff like that, so maybe it's also something we can start discussing.
If we want to keep doing that, or not.
**nacho** 25:26 Yeah.
**Vinod Vydier** 25:27 We had the same problem that we had with the XC framework, right? There were a lot of interest for XC framework.
**Ari** 25:33 Yeah, I think that both of them are… Are problematic stuff, like… from one side, like, I'd rather provide XC framework support or a way to create your own XC framework.
Rather than keeping… keep maintaining CocoBots, because it seems like CocoBots is, like, dying.
Eventually, I think that this year, or next one, is that they… they are going to archive the main Cocoa.ex.
**nacho** 26:05 Nope.
in next December, something like that, I remember.
**Ari** 26:11 Yeah, so at that point in time, we either have a private repo with the specs ourselves.
to keep maintaining OpenTelemetry releases.
Or we just say, It's all folks. No more cocoa butts.
Or something like that.
**nacho** 26:32 Yeah, I think… I think that's the… the final solution, right? We can provide, best effort.
For now.
I would say, if possible, and just switch it off also.
I think we… Tough enough maintenance.
In the project, that we almost not… cannot get to everything, because Most of us, Yeah, I'm not finding enough time.
For… for handling all the tasks needed, so probably reducing it a bit.
Of the support is the best idea, for the best of the project.
I would say.
**Ari** 27:21 And also, I think that, on the long term, again, I'd rather have XC Frameworks aboard rather than CocoaBots.
Because… there are more benefits in exit frameworks.
on… I don't know, CocoPots is dying, and the only good thing of having CocoaPots is, you know, probably Datadog or Embrace and other companies are still using it, but I think they also should have their own idea of when they are going to stop supporting CocoaPots 2. Like…
**nacho** 27:54 Yep.
**Ari** 27:55 Everybody should be prepared themselves to sunset.
coconuts.
Eventually.
**nacho** 28:01 Yeah, yeah, that's right. I mean, it will be frozen, so for old versions, it will work. That also allows us to clean up some of the old versions, support that we have, right?
**Ari** 28:14 Exactly.
Yeah, and we just… we will just say, hey, this is going to… die at this moment. We expose the plan and let people know, like, When that's.
**nacho** 28:28 Again, I'm almost regretting on separating into two repositories.
To be honest, because the maintenance has grown a lot, and… So, yeah, I don't know, even thinking about Using trades, or something like that, in order to only have a package, or waiting, Yeah, I don't know if there have been changing something in SPM to remove that.
dependent.
**Ari** 28:55 I, I…
**nacho** 28:56 Hell.
**Ari** 28:57 I haven't tested the trace things, but maybe with trades, that's something that could be achieved in a single repo, and maybe that's something we can try again, eventually.
**nacho** 29:08 Yep.
I, I… This is getting me crazy with… you know, you have to handle maintenance of to re…
**Ari** 29:17 issues.
**nacho** 29:18 Two weeks ago.
**Ari** 29:19 yards.
**nacho** 29:20 Two things that gets updates automatically with the core dependencies, that it's getting crazy.
Yeah.
It's as well as we expect a traditional coin.
But yeah, I can understand also that for some users, it's much better, but if we can get the same with just one repo, that would be great.
**Ari** 29:41 Yeah, I'm going to investigate the trades and see if that's feasible.
Because, yeah.
**nacho** 29:47 Okay.
**Ari** 29:47 it's becoming a burden, to be honest. It's not really easy to keep up. I sometimes forgot to go and check the issues, like, for example, this issue on this PR on watchOS, I haven't seen it, to be honest. I went to the OpenCelement record.
So yeah, it's something that maybe it's good to revisit.
**nacho** 30:08 And also, we need to release in two times, like, first the core, later the API, Or later, the, the main repo?
Just to be sure that anything is… nothing is broken. You update things on the core, and then you discover that it's not breaking, or showing warnings, or things not… Being correctly handled, just because we need a… A nightly build to run that.
Yeah, it… It's very cumbersome.
**Ari** 30:40 Yeah, or…
**Vinod Vydier** 30:41 Less than a year, right? Less than a year since we separated.
Maybe 6 months.
**nacho** 30:45 I… I don't remember.
**Vinod Vydier** 30:47 Yeah, yeah.
**nacho** 30:48 But, yeah…
**Ari** 30:49 We… we either invest… We then invest on… on… or more automation to… make everything easier, like… I don't know, having a test app that has the full integration and all that stuff.
something like the job, I think Billy did to check If changes in OpenTelemetry Core will break, OpenTelemetry shift.
Or we find a way to unify again, and do kind of a rollback.
But yeah.
Okay, I'll see if I can investigate a little on the trades, because… That'll be the only way to fix this.
Obviously, you will… Bump the dependency, so people will have to depend on a higher Package version, if they want to use that feature, but… All in all.
Again, it's something we can communicate with sometime.
I'm… Anybody have objections or wants to come to the project and help us maintain it?
**nacho** 31:58 Yeah.
**Ari** 31:59 They mean it. That's… that's a different thing.
**nacho** 32:06 Ted's being.
**Ari** 32:07 I don't…
**nacho** 32:07 There are.
**Ari** 32:08 I don't wanna…
**nacho** 32:10 Name.
**Ari** 32:13 Yeah, but, like, you know, the original issue was opened by a company, they even… After we did all the changes, they submitted, like, 3 issues to make it better for themselves, and they never came back here, so… I know.
**nacho** 32:31 Yeah, they have… as I said, they have never added anything to this project.
And they… have not done it either later. Only that, yeah.
the watchOS issue, that's the only developer from that company that's doing that.
That's… Oh. He's, he's from that.
companions.
**Ari** 32:57 Oh, I see.
**nacho** 32:58 But yeah, but he's in a different team than the one that came asking for that.
So…
**Ari** 33:04 Yeah.
**nacho** 33:04 We're so loud, yeah.
Okay, I think we can finish here. I need to… drop.
**Ari** 33:14 Yeah, no worries. I think we'll handle.
How's up?
**nacho** 33:18 Right.
How funny?
**Ari** 33:20 Okay, folks.
**Vinod Vydier** 33:20 Beyond.
**Ari** 33:22 Bye. Bye-bye.
