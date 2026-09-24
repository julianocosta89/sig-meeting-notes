SIG: OpenTelemetry PHP SIG
Date: 2026-09-23
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Chris Lightfoot-Wild** 01:28 Hey, Bob.
**Bob Strecansky** 01:33 Chris, how are you?
**Chris Lightfoot-Wild** 01:35 Okay, Lencia, how are you?
**Bob Strecansky** 01:37 Oh, I'm living the dream, my man.
**Chris Lightfoot-Wild** 01:40 Working from the home office today?
**Bob Strecansky** 01:44 Ye for a little bit, and then I'm gonna go in.
**Chris Lightfoot-Wild** 01:48 Hectic traffic.
**Bob Strecansky** 01:52 Yeah, I normally take… I normally do that by getting to my office by 8am, but today I decided that I want to take my kids to go get donuts, so I did that, and now I'm gonna just do this, and then go in a little bit later than normal.
**Chris Lightfoot-Wild** 02:06 Nice.
**Bob Strecansky** 02:07 Yeah, buddy.
**Chris Lightfoot-Wild** 02:12 Read in the news this week that you were avoiding all hurricanes over there at the moment in this season.
**Bob Strecansky** 02:18 Yeah, hurricanes don't really come to Atlanta, it's too inland, but where my… Family is from… they have a lot of hurricanes.
My…
**Chris Lightfoot-Wild** 02:30 This year as well, or… Because I thought I'd seen that it was very quiet.
**Bob Strecansky** 02:34 So, I mean, like, even a quiet time is, like, still tumultuous.
So, where my… where I was… where I went to high school, and where my in-laws still live.
is, there's an island called Hilton Head, it's, like, the very bottom southern tip of South Carolina, and… The really scary part about living on that island is there is one bridge in, and one bridge out, so if you… if they have a hurricane and that bridge were destroyed, then, like, pretty much everybody would be stranded on the island with, you know, no end in sight, so… the scurry.
Pel, how are you?
**Chris Lightfoot-Wild** 03:12 Hippo.
**Pawel Filipczak (Elasticsearch B.V.)** 03:13 I'm okay, thank you.
Oh, you guys.
**Bob Strecansky** 03:17 Living the dream.
**Pawel Filipczak (Elasticsearch B.V.)** 03:19 Hmm.
**Chris Lightfoot-Wild** 03:19 Alright, we've got both sunshine here today, like, back in September. That's weird.
**Bob Strecansky** 03:26 That's weird for y'all, huh?
**Chris Lightfoot-Wild** 03:28 But yeah, yeah, it's getting quite… quite warm.
17 degrees Celsius, which is… Not for us.
**Bob Strecansky** 03:39 We have… we have an absolutely frigid day for late September here. It's going to be… 25, see?
**Chris Lightfoot-Wild** 03:46 25.
**Bob Strecansky** 03:50 Yeah.
I… I had a tennis lesson at 6… 6.30 in the morning yesterday, and it was already 25 at 6.30, and it was, like, 100% humidity. It was… I sweat through my shoes in one hour.
Monday innings.
But… Anyway… I think we had a lot on the agenda today, so let's get, as my son likes to say, let's rock and roll!
Oh, I almost… I sort of gave him a sneak peek of what I was doing. Shh, don't tell anybody.
**Chris Lightfoot-Wild** 04:31 life.
**Bob Strecansky** 04:32 So, Chris, you got the first agenda topics, my dude. Let's hear it.
**Chris Lightfoot-Wild** 04:36 Sorry, it looks like I just beat you to it, and… Uploaded a lot of stuff on that.
**Bob Strecansky** 04:41 But we're gonna cover them also. Matter.
**Chris Lightfoot-Wild** 04:44 So yeah, I guess it was the update, just to, obviously, Severin managed to get the account transferred for us. We've all got access to it now. Just the quirk that, like, where there's accounts where yourself and Brett already have, like, maintainers to data so on, so under certain packages, sorry.
that account, OpenTelemetry PHP doesn't, and it's obviously not necessarily a problem.
But I don't know if it was an exercise to go through and add That user to the mall as well.
Just for, like, the consistency. Obviously, it's a shared account that we can all, sort of, get into should we need, but,
**Bob Strecansky** 05:20 Yep.
**Chris Lightfoot-Wild** 05:20 Otherwise, it seems like… If, you know, there's a bus factor of 2 at the moment between you and Bob, but if that was zero…
**Bob Strecansky** 05:29 I… I am Bob. Brett.
**Chris Lightfoot-Wild** 05:32 You and Brett, sorry, sorry.
**Bob Strecansky** 05:33 Okay.
**Chris Lightfoot-Wild** 05:34 Yeah, sorry. You've got a bus factor of 1 with Bob.
Anyways, that was it, so…
**Bob Strecansky** 05:43 I feel very honored to even think that you put me and Brett in the same bucket, so…
**Chris Lightfoot-Wild** 05:48 Oh, of course, yeah. So that was just, like, the little sort of disclaimer to that, like, even their API doesn't support like, just adding an additional maintainer. And it looks like there's been tickets on their, sort of, repo in the past, where they were kind of like, well, we've not got any interest in doing this, so… it is what it is.
**Bob Strecansky** 06:10 Understood.
**Chris Lightfoot-Wild** 06:10 Yeah, hopefully that makes sense, but yeah, I think that's, That one's hopefully ticked off for now, if you're happy with that.
**Bob Strecansky** 06:17 Sounds good. Alright, looks like the next one's Long Running Lairville Instrumentation PR, finally ready. Let's go!
**Chris Lightfoot-Wild** 06:27 Yeah, I mean, I started this 2 years ago, so it's very…
**Bob Strecansky** 06:31 Whatever this.
I thought it was really funny that you put the little construction worker…
**Chris Lightfoot-Wild** 06:36 I needed probably more than one construction worker, I had to denote how long it was gonna take, So, the caveat to it is, like, there's some funky stuff in Psalm. I went through on 8.1, and it was all green.
But then on the other, sort of, build matrices, obviously, it pulls in different versions of things. On latest Laravel, this is a problem that just blows Psalm up.
But, like, the test pass… Across every single version that's covered.
And it's just some… some psalm quirkiness, so kind of… Almost, sick of fighting it.
Don't know what our thoughts are on, like, can we just… Make it go away for now, and then try and… like, patch them later or something, if… obviously, there's an upstream fix required first, so…
**Bob Strecansky** 07:29 I'm wondering if we're getting… I have not done any of the auditing for Mago lately, and I'm wondering how that's going. I know somebody took that ticket, but it seems like it went to DevNall somewhere, so I'm gonna add that as an action item.
**Chris Lightfoot-Wild** 07:42 Yeah, I wouldn't mind, obviously, if we were saying going that route, just swapping everything out for that, if it was…
**Bob Strecansky** 07:48 Zuh.
**Chris Lightfoot-Wild** 07:49 more reliable.
**Bob Strecansky** 07:51 Backlog…
**Chris Lightfoot-Wild** 07:53 Just, obviously, several iterations of, like, oh, go through all the fan stuff, make that happy, cool, that passes, go through Sam, make all that happy, PHP Sam, and then they just start competing with each other, and just getting upset, and… Then I go upset.
**Bob Strecansky** 08:08 Yeah, yeah. The amount of mental fatigue that we've had from some of these linting and checking and other tools, I wonder how, like.
I'm gonna say this very carefully. I wonder what the value is… the value proposition is for some of these compared to the amount of time and effort we've used to maintain them efficiently.
**Chris Lightfoot-Wild** 08:34 Yeah, I mean, I've been… with this PR in particular, I've had the test passing ages ago, like, way back when.
But the… the quality stuff just, like, put the brakes on a little bit, and then obviously, over time, it goes stale, so… Now I've gone through it all again, and it's still passing, and it's still fighting with the quality tools, I thought, yeah.
I've lost a lot of time to it, and there's… I found some… a couple of extra things as well, which were… the instrumentation was actually triggering the Laravel container to, like, load dependencies earlier than an application would have access to, intercept the behavior for.
So, like, the logger gets resolved during the bootstrap of the instrumentation, rather than the application.
So in Laravel, you can typically extend, that with, like, callbacks so that you can modify the logger yourself, but we kind of… being included in the mix. Break that behaviour, so… Yeah, found a… found a few instances of that which are fixed.
So, yeah, hopefully that will… Pave the way toward, Improvement… further improvements on the back of it as well.
**Bob Strecansky** 09:47 Glorious.
**Chris Lightfoot-Wild** 09:48 So I don't know if anyone wants to look at that, like, it's a bigger-looking one. Brett's looked at it in the past, but, like, that was maybe 2 years ago, so… Probably do with re-requesting review, I suppose.
**Bob Strecansky** 10:00 I will put it in my prioritized backlog.
Cool beans?
Now you have the Configuration Global API. That does look fun.
**Chris Lightfoot-Wild** 10:14 Yeah, sorry. So, this was what we spoke about a few weeks ago, and Pawel, I think you said you might have been speaking to some Java colleagues, potentially. Excuse me, I don't know if you've had time to do that, but I did.
**Pawel Filipczak (Elasticsearch B.V.)** 10:27 I tried to, but I was on vacation, so I.
**Chris Lightfoot-Wild** 10:30 Oh, okay. No, that's alright, no, thank you. I guess it was, again, on the back of the above PR.
When I was obviously getting through the merge conflicts and pulling everything in from men.
There's a recent cha… oh, not recent, but there's a change, Where it was using the configuration resolver.
To fetch config for some specific functionality.
So obviously this was, like, going down the route of using SPI and loading configuration that way, but then… there's this, like, global reach out to the SDK, or the API, sorry, which, is deprecated.
So, I was looking at the Java API, and… Obviously, the makeup of the language is different, so… it looks like they've got the equivalent, kind of, SPI functionality already natively provided by, like, class forename static or something, where you can load in an object based on, like, its class string, which is kind of what we've got with the service loader.
But the service loader isn't in the API, only exists in the SDK.
But that example sort of code snippet there just shows the Java API trying to… give the opportunity for the SDK to jump in and provide configuration.
Mmm.
I guess we would get around it by having our globals introducing, like, a configuration object that you can set in the SDK itself.
And otherwise, having, like, the… common, interface to that, so we'll go through the API, but… Like, pluggable, behaviour.
Yeah, sorry, so I don't know if it was, That might not have added much value to this, I just wanted to… highlight what Java was doing, I suspect, and beer.
just see… see where you're at with it, pal, so… so I guess just watch this space.
**Pawel Filipczak (Elasticsearch B.V.)** 12:33 I will reach out to them, so… I guess this or next week, beginning of next week.
Yeah, we'll see. Maybe they will share some ideas with me, how to…
**Chris Lightfoot-Wild** 12:49 Yeah, I think we can probably… obviously, we can come up with our own thing, but it'd be good to be consistent, I suppose.
**Bob Strecansky** 12:59 Thank you both.
**Chris Lightfoot-Wild** 13:00 Yeah, chisn's.
**Bob Strecansky** 13:04 Okay, cool, my turn. Let's see… the OSS scorecard workflows were merged, that was upstream, nothing really super important to talk about there, I just want to make sure that I document that in here.
There was a request for a distro release based on Levi Morrison's request.
**Pawel Filipczak (Elasticsearch B.V.)** 13:23 You' It's not about each draw, but it was about the extension, the… Sorry.
**Bob Strecansky** 13:30 There's an exception.
**Pawel Filipczak (Elasticsearch B.V.)** 13:32 Instrumentation.
**Bob Strecansky** 13:35 Thank you.
So, Pow, did you get a chance to look at that one?
**Pawel Filipczak (Elasticsearch B.V.)** 13:42 Yes, yes, I… I verified everything is okay, so the fix is… is good.
And, yeah. So, if they ask for a release, I guess we can do that.
**Bob Strecansky** 13:54 Yeah.
**Chris Lightfoot-Wild** 13:55 Brett beat you to the punch.
**Bob Strecansky** 13:57 Oh, did he? He already merged it, and…
**Chris Lightfoot-Wild** 13:59 Yeah, there's a tag of 1.42 yesterday, so…
**Bob Strecansky** 14:02 Gosh, that guy, too fast. I'm waiting to see him, you know, like… I want to believe that he's still real, you know? Maybe he's… maybe it's actually AI Brett.
**Chris Lightfoot-Wild** 14:14 Perfect.
**Bob Strecansky** 14:16 Okay, cool.
**Chris Lightfoot-Wild** 14:17 Well, this is whirring away in the background, so… Thanks, Brett, if you're ever watching.
**Bob Strecansky** 14:31 So, the next two things, I'm gonna follow up on this MACO backlog ticket.
And then the backlog grooming, I took, like, a very first pass at doing this, But, I don't know how y'all want to prioritize that, so I took some of the… issues that we had, and put them on this board, and added priority, priority levels to them, P0 being a production-impacting bug, P1 being something that we feel is important, and then P2 being everything else.
And then, started working through categorizing and doing whatever, so… I don't know… I don't… I don't know that it's worth spending, like, a very, very long time doing this as a group, unless y'all feel… if y'all feel it is, I'm very happy to sit here and backlog room with you, but… I don't know how y'all feel about that.
**Chris Lightfoot-Wild** 15:30 I guess it depends what… Time we have to put into actually working on the issues, other than this is roughly what we'd like to do if it was us doing it, but other contributors might just jump in with anything on the… On the issue bot?
**Bob Strecansky** 15:46 I'm sorry, Chris. Can you say that? Say that again?
**Chris Lightfoot-Wild** 15:51 But yeah, it was… it was more, I suppose, other contributors will probably not look at this, So it just depends, I guess, how much time we… As contributors ourselves, say, alright, we'll follow exactly this thing.
**Bob Strecansky** 16:05 Yeah, I think… I'm trying to decide the right way to, like, effectively evangelize that, right? It's like… If we have new contributors, or people that are looking to do open source for the first time, or people that are looking to contribute to this library.
How do we get them here, effectively?
**Chris Lightfoot-Wild** 16:24 Yep.
**Bob Strecansky** 16:26 And I don't know, is that, like, posting that in our Slack channel on, like, a given cadence? Is it… Like, whenever anybody asks about it, we do that. Is it doing something else?
So… I'm thinking about this as I'm talking, so… This is not.
**Pawel Filipczak (Elasticsearch B.V.)** 16:46 We can just, if they will contribute something, we will just invite them for the issue.
Or pull requests, and just let them know that there is a meeting, and we can just discuss things there.
I think there is no better way to do that.
**Bob Strecansky** 17:00 Yeah, unfortunately, I think you're correct. It's… I feel like this is one of those things that is always problematic, right? It's like, you have… Open source contributors that want to do what they want to do, but also we have these things that we need to get done, and how do we prioritize the right thing?
**Pawel Filipczak (Elasticsearch B.V.)** 17:17 So it…
**Bob Strecansky** 17:17 Come on.
**Pawel Filipczak (Elasticsearch B.V.)** 17:18 From the backlog, from time to time, and just, you know, to organize it and make priorities on the issues, and that's it.
**Bob Strecansky** 17:26 Yeah. I'm posting about it in our Slack channel now, and then I'm also gonna add it as a bookmark.
**Pawel Filipczak (Elasticsearch B.V.)** 17:37 So maybe we can just, you know.
Make one of our meetings last of the month, or the first of the month.
And just see… prioritize backlog on that meeting, and don't need that, or we can just, you know, start from the… with the backlog, and then go… go with the… our regular issues.
**Bob Strecansky** 18:03 Okay, so, yeah, I think… I think there's definitely value in walking through our… in walking through our issues, our current issues backlog, and then seeing, like, deciding whether or not we should close some or put them in here. So I… I would propose that we do that now. I think that that would be helpful, and we could do that on, like, a given cadence.
**Chris Lightfoot-Wild** 18:26 So we want to do that now, just to sort of see if there's any that aren't on the board, but it probably should be.
**Bob Strecansky** 18:31 Should be, yeah, I think that would be fine.
**Chris Lightfoot-Wild** 18:33 This… Just triaging stuff a bit better, generally.
**Bob Strecansky** 18:39 Bug, help wanted… I'm like, do I just open all of these and we'll slap through them? That might be the… it's a lot of tabs, but it might be worth it.
Let's try it on the first page, and then we'll… We'll, see what else we do.
This… if this goes well, we'll do it on the second page, how about that?
Click. Click. Click. Click. Click. Sounds like, I need a macro for that or something.
Alright, looks like eBay opened this one a week ago. We can put this in, prioritize backlog status to do, and then… Priority P1. Okay, so that's already in the backlog, I put that in there.
That's cool. I'd like to work on this as well. Looks.
**Chris Lightfoot-Wild** 19:39 I mean, there is actually a PR that's been approved, it just needs…
**Bob Strecansky** 19:43 It does… it does appear so. Thank you, Chris. Oh, I didn't realize…
**Chris Lightfoot-Wild** 19:48 agreement to it.
**Bob Strecansky** 19:49 haven't viewed this. So, I guess we… if you and Brett approve this, I'll merge it.
Huzzah! Look at that! We're already… we're already crushing it in the backlog triage.
Massive.
**Chris Lightfoot-Wild** 20:04 So will that automatically move itself across now in the board?
**Bob Strecansky** 20:08 I don't know, let's find out.
So, let's look for… Where did we just go?
Sorry.
There it is. Oops, close.
This is done. How about that? Where'd it go, GitHub? You did a great job with that.
Alright, add auto-instrumentation for Falcon PHP framework.
**Chris Lightfoot-Wild** 20:39 Yeah, we spoke about this briefly last week, didn't we? I had something to actually do on the back of that, which I've not.
**Bob Strecansky** 20:45 That's right, okay.
**Chris Lightfoot-Wild** 20:46 Yeah, we can put it in the backlog as a… That'd be cool to see.
**Bob Strecansky** 20:50 Great.
**Chris Lightfoot-Wild** 20:51 Next thing to pick up.
**Bob Strecansky** 20:53 PHP prioritize backlog… So I'll put that as a P… a to-do, and I'll put it as a P2. We'll just do everything as P2 by default.
**Chris Lightfoot-Wild** 21:04 One of the things I'll probably do as well with the PR I've got, is what we spoke about last week, adding, like, to the README, saying that I'm, like, one of the current maintainers of that package.
And then, can at least say, follow this example?
Lou, we want to go this route.
And then we'd be happy to do that. He or she, sorry, but…
**Bob Strecansky** 21:24 Hey.
Yeah, looks like y'all are doing a good job reviewing this already.
So I guess that should be… Not in our to-do, that should be in progress.
Alright, asynchronous instrument with no observation is exported as a major… as a… Metric with zero data points. We should probably label this one as a bug.
Put this in… Alright.
Should… But this is a to-do… This dude, yeah, they haven't… oh.
Yeah, still in… to do, and we'll put it as a PT.
Wonderbar… Context is not actually immutable, that's a bug.
**Chris Lightfoot-Wild** 22:23 Nevey, has currently done this already. I think Sam was okay, but it was… I guess it's whether or not… are we happy saying, okay.
We've already reviewed that now. Eva's, obviously.
Like, a bit of an expert in the subject, so let's close it off.
**Bob Strecansky** 22:40 Yep, I think, I wouldn't consider that.
Adding a comment noting that the objects are in contact must… yeah. So… I guess we gotta make a pull request, talking… saying that I'm gonna… I'll, I'll pin this so that I can do that later, because I could… that's just adding a comment, that's not a big deal.
Wrap PSR20 clock. This is cool, I didn't know this was available.
**Chris Lightfoot-Wild** 23:07 PSR20?
**Bob Strecansky** 23:09 No.
**Chris Lightfoot-Wild** 23:10 Yeah, I think we spoke about it before, it was, like, not as atomic, or it doesn't give the precision you'd want, or we'd want.
I think this person's got another PR as well, which I reviewed yesterday.
I think they already had a workaround to something,
**Bob Strecansky** 23:32 Love it.
So I guess we could put that in the project.
To-doo… D2… Cool.
Auto Laravel crashes when using MongoDB models query builders.
**Chris Lightfoot-Wild** 23:58 I believe that one has been cited. I'm not sure if that was the links.
Hmm.
**Bob Strecansky** 24:05 And it's closed.
**Chris Lightfoot-Wild** 24:09 If you scroll down a little bit, was there another reference one?
**Bob Strecansky** 24:14 That's just the issue.
**Chris Lightfoot-Wild** 24:16 Someone else had opened this recently, because I… Merged it in.
Oh, did you? Okay. Well, the solution was, we were kind of basically double capturing SQL.
**Bob Strecansky** 24:31 Oh, I see.
**Chris Lightfoot-Wild** 24:32 And on this one, it made sense to just remove it, because then Mongo doesn't blow up, but we're already capturing it at a lower level.
And then I sort of said, ultimately, at… I would like to remove… the query watcher that exists in Laravel framework instrumentation.
And just defer it to, like, the PDO instrumentation instead?
Because then, it's even less to reproduce, isn't it?
**Bob Strecansky** 25:00 Yeah.
**Chris Lightfoot-Wild** 25:02 Vola, yeah.
**Bob Strecansky** 25:03 After free, class names are just a stack method, which is at least without a reference being taken with span and hook.
Doesn't look like anybody has started working on this yet.
Priority… er, no, let's… Projects… To-do… P2… should I put this as a P1, you think?
Yeah, so…
**Chris Lightfoot-Wild** 25:34 Describing a very specific scenario that triggers it.
**Bob Strecansky** 25:38 And there's a bunch of thumbs up for it, so I think that this isn't the first person to deal with this problem.
Url full is recorded unredacted leaking signed URL signatures. Chris, it looks like you started talking on this one already.
**Chris Lightfoot-Wild** 25:54 Yeah, my thinking was basically that PR that you said you were going to look at, I want to get that in first, because it's been, like, a building block, and then there's a new functionality that exists that Niveve's done, that we can start pulling… No, sorry, the other one, the one with the little builder icon.
**Bob Strecansky** 26:09 Oh, okay.
**Chris Lightfoot-Wild** 26:09 I'd like to learn that first, and then… like, yeah, there's new functionality that didn't exist at the time, that now Neve has built, that can just start pulling in.
**Bob Strecansky** 26:20 Got it.
**Chris Lightfoot-Wild** 26:21 But yeah, if we do it beforehand, then I've got merge conflicts to fix again, and it's just never gonna get in there, so…
**Bob Strecansky** 26:27 Totally. Okay, sounds good. Looks like this one's assigned to you.
**Chris Lightfoot-Wild** 26:35 Yeah, we discussed that one, previously.
**Bob Strecansky** 26:38 Yeah, I kinda remember it.
**Chris Lightfoot-Wild** 26:40 The action's on me to, like, try and follow up with some… Maybe the maintainers in the Slack channel, we'll see.
**Bob Strecansky** 26:48 Great.
**Chris Lightfoot-Wild** 26:48 Do we drift significantly from their languages?
**Bob Strecansky** 27:01 Symphony. A throwing kernel view listener splits one request into two traces and loses a… you were just talking about this, right? That might be similar to what's happening in another… Contribute package?
Or is this something different? It's, like, might be something different.
**Chris Lightfoot-Wild** 27:22 I don't know if that's the internals of just Symphony on its own, is it saying just that, or…
**Bob Strecansky** 27:27 Cool. Put it on the project board?
**Chris Lightfoot-Wild** 27:29 Can we equally tag it as Help Wanted, I suppose?
**Bob Strecansky** 27:33 Yes, good idea.
**Chris Lightfoot-Wild** 27:36 Well, I've never really used Symphony much myself. I've used some of the components to it, obviously, via Laravel, but… Yeah, my knowledge is lacking.
**Bob Strecansky** 27:45 we have… it's very, other PHP developers always laugh when I tell them this. We have this, like, very old, cobbled-together PHP framework that's internal that's, like.
some Zend, some Symphony, some Laravel, some our own written stuff, some, like, other libraries, it's all just, like, in this… Frankenstein, and it's… Never fun to troubleshoot.
**Chris Lightfoot-Wild** 28:13 But I bet it's got a cool internal name, so there you go.
**Bob Strecansky** 28:17 So what's funny is it actually got open-sourced, and then they closed-sourced it again. So if you ever want to see it, I think they'll see it.
**Chris Lightfoot-Wild** 28:31 Vesta.
**Bob Strecansky** 28:41 Well, take it back, apparently it's not here.
Or maybe it is, let's see.
**Chris Lightfoot-Wild** 28:45 been eradicated.
**Bob Strecansky** 28:47 and eradicated.
It's around somewhere, I promise, but I have no idea where… that's how important it is.
Alright, auto PDO adds support for trace propagation through user variables. It looks like, you were talking about this.
**Chris Lightfoot-Wild** 29:09 Yeah.
I guess the person can't have been that interested in it himself.
**Bob Strecansky** 29:16 I guess not.
**Chris Lightfoot-Wild** 29:21 So I'll probably be, yeah, the lowest priority.
**Bob Strecansky** 29:25 SIG sub when using with Ion Cube and Octane with Roadrunner. Okay.
Looks like, looks like, Paw, you were already discussing this with them.
This has been raised previously, a few back from an iron cube. Okay, so we'll mark this as… Part of the project.
Then we'll mark it as… To do… P2, because we haven't had a lot of… Fast forward. Onto the next one.
Auto-guzzle, a post-hook invalid signature when client transfer throws asynchronously.
Looks already fixed in Maine… Blah blah blah. Closing.
support OTP profiling, oof, that's a… that's gonna be a big one.
**Chris Lightfoot-Wild** 30:23 That's just basically adopting the new signal, is it?
**Bob Strecansky** 30:26 Yeah.
Environment variables for OTLP retry configuration… Seems like a reasonable… oh, this one's got a lot of thumbs up.
That's cool. Prioritize that, and we'll put it as P1. I don't know why… I don't know why I'm choosing these priority levels, I just… it feels like it's a very vibes choice, but I'm okay with it.
Signed to myself.
**Chris Lightfoot-Wild** 31:05 It's nice, isn't it, when you think… there's, like, usually three of us here, and like, oh, there's nine other people that might be interested in something.
**Bob Strecansky** 31:10 to cover.
**Chris Lightfoot-Wild** 31:11 Our audience.
**Bob Strecansky** 31:12 People love this stuff.
Let's see, monologue bridge, just not defined all the dependencies. This one, the person already has defined for themselves, so we can put them in the prioritize backlog.
And we can say to do P2.
Come on.
You can do it.
Don't quit on me now.
**Chris Lightfoot-Wild** 31:41 Which dependence is it that it's lacking?
Is it just a…
**Bob Strecansky** 31:49 I intentionally do not require any other dependencies, and I pursue the following PHP script.
Some comp attributes.
**Chris Lightfoot-Wild** 32:01 Okay.
**Bob Strecansky** 32:03 And he's planning on helping. And Nivea said.
Okay, so this is already, Okay, this has already been implemented.
Good.
Compatibility check for PHP 5… 8.5. I guess I saw this to myself and I never did it, so… Do that, pin that for myself, response, body size limitation, I also assign that to myself.
do that.
Auto Doctrine… This one… Is it kind of the same issue? Okay, so this one has a… Closed.
**Chris Lightfoot-Wild** 32:43 That's because it's on the… on the fork, isn't it? I suppose. Split.
**Bob Strecansky** 32:48 No, he closed it. This repository, okay, reopened in the right place… Yeah, it looks like it might have been… oh, because they didn't sign the… Oh, he's unable to complete the EZCLA. I remember this.
We can… I guess we can just add this one as a, to-do, or something.
I'll make a note about this.
Additional enter was… Middlejuice on.
**Chris Lightfoot-Wild** 33:24 What does that actually leave us with?
If someone's already produced some work, but then they can't sign the… thing. Can you just take that work? Because… That's not covered by the thing they didn't sign.
**Bob Strecansky** 33:39 The way that I… the way that I interpret it… is… if somebody… opens a pull request, and they have signed the CLA, then it's fine.
**Chris Lightfoot-Wild** 33:50 But in this one, he hasn't signed the CLA.
**Bob Strecansky** 33:52 No, he hasn't, but, like, if I opened a pull request with the exact same information.
**Chris Lightfoot-Wild** 33:59 Hmm.
**Bob Strecansky** 33:59 That'd be okay.
At least that's how I interpret it. I can… I could be interpreting this incorrectly, but…
**Chris Lightfoot-Wild** 34:06 Sorry, I'm not trying to be difficult, I just wonder, like, I hope that doesn't leave us in, like, hot water or anything.
**Bob Strecansky** 34:12 Oh, this person also did the same thing here, and it looks like… This is in progress.
Yeah, I don't think… Sorry, go ahead, Chris.
**Chris Lightfoot-Wild** 34:25 I was gonna say, that one sounds similar to the thing where there's an issue about two… like, two traces disconnecting or something?
**Bob Strecansky** 34:34 Yeah, is this a bug? Yes, it's a bug.
Something isn't working.
Cool.
Dependency for Google Protobuff… Seems like this is required for 85. Okay, so this one, I think there's a bunch of… there's actually a bunch of requests for this, so I will… This says a Help Wanted… We'll put it as a project, and we'll put… give this one a P, oops.
No, but this… That's not good.
**Chris Lightfoot-Wild** 35:06 Suggestion there is it's just add in all 5 in the… Version constraints, so…
**Bob Strecansky** 35:13 Yeah.
**Chris Lightfoot-Wild** 35:14 Because it needs to do that and test it, but that's not a big one.
**Bob Strecansky** 35:16 Yeah, it's not big, but it's… oh, you know…
**Chris Lightfoot-Wild** 35:19 Oh, my luck.
**Bob Strecansky** 35:20 The bite size.
Calling exit before the… okay, so this one's a bug… Oh, it looks like Niveveh's already mentioned the… Solution, so I'll close it.
And periodic exporting metric reader not working… that's a bug.
Somebody typed as a bug.
Brett… own issue… Oh, Paol, you said you were gonna work on this, so… Alright. We are officially done with the first page of four. Maybe we'll just do one page a week. That seems reasonable to me.
Or do y'all want to just keep clacking? That's you.
**Chris Lightfoot-Wild** 36:22 Oh, that seems fun.
**Bob Strecansky** 36:24 Which, one page a week?
**Chris Lightfoot-Wild** 36:28 Yeah, I mean, I guess unless every week there's… we're probably working backwards, I suppose.
**Bob Strecansky** 36:33 There's only 3. There's only 3, let's just… It's short-term pain for long-term gain. We still have a little bit of time left in this meeting.
Alright, let's do it this way, that's not fun.
So what was the last one? Yeah.
Let's see… Because some of… I'm sure we'll see some of these. These are… we're getting to the point where they're, like, a year-ish old now.
**Chris Lightfoot-Wild** 36:59 Yeah, I guess maybe we can get to the point as well where other SIGs have probably got workflows that, you know, auto- Triaging labels or something, so that we can start filtering stuff and knowing how…
**Bob Strecansky** 37:12 Yeah.
**Chris Lightfoot-Wild** 37:12 Organize this a bit better.
**Bob Strecansky** 37:14 Yeah, maybe so.
**Chris Lightfoot-Wild** 37:15 So we can probably borrow those.
**Bob Strecansky** 37:18 Maybe so.
**Chris Lightfoot-Wild** 37:19 Mind having a look to see what's out there?
**Bob Strecansky** 37:24 I like short-term pain for long-term gain.
**Chris Lightfoot-Wild** 37:28 Some of these are going about 3 years, aren't they, so…
**Bob Strecansky** 37:30 Yeah, they are. I have a feeling a lot of these are gonna be.
**Chris Lightfoot-Wild** 37:33 Well, my recent PR, that might not mean it's gone away forever, so…
**Bob Strecansky** 37:38 Never say never, Chris.
**Chris Lightfoot-Wild** 37:40 Yeah.
**Bob Strecansky** 37:41 Symphony events, not recorded on spans when Symphony handles errors via sub request.
Looks like… oh, this is…
**Chris Lightfoot-Wild** 37:50 How old was this initial one? Because obviously… That particular name is one that, obviously, I've seen using AI before. We've never seen it at a meeting, I think.
Not that that's a problem, but I just, like, when they say something's closed, we might have to double check.
**Bob Strecansky** 38:06 Okay, so this one… Still has an open pull request.
And I'm waiting for… oh, and it has urge conflicts.
Still waiting on… It was beautiful like this.
Support PHP 8.5 and GitHub Actions, this seems like a good one. Oh, Brett is working on this, I'll send it to him.
This, This may… it's funny to say it, this actually makes me appreciate Jira, which is not something that I'd say very frequently, but… Route name is the routes and template. Okay, so this is a bug.
And there's a subscriber workaround.
Some open pull requests for it.
Bretton, you talked about it.
Sweet.
This request has conflicts.
Oops.
Triage… Alright.
Adding twigging, instrumentation… Wow, this is very old.
Well, it looks like Brett was working on this with them.
Oh, this isn't a different project.
Did not know that was a thing.
Next.
Support the new W3C random flag.
Looks like it's been fully implemented. Yeah, this has already been fully implemented.
Missing console default root span creation… So it does.
Looks like it is open. Oh, that has large conflicts.
Let's fix those, and then…
**Chris Lightfoot-Wild** 41:18 Did you put that as, like, a P2, then? Sorry.
**Bob Strecansky** 41:21 Oh, I didn't… because it… if they had merge conflicts, I wasn't putting them on the board, but I can't… I definitely can.
**Chris Lightfoot-Wild** 41:29 Just so, at least if we've had a first pass at every issue that's left, and they're all on the board somewhere, we can… Decide what to do with them the next time.
**Bob Strecansky** 41:39 Good idea.
**Chris Lightfoot-Wild** 41:42 Sorry, I'm trying to create more work.
**Bob Strecansky** 41:44 No, I like… I liked it.
Stack traces, blah blah blah… do some JavaStyle instead of regular PHP styling.
Why is this?
Most likely because… the original… Into mature.
But it's using the Java template as an example.
is… sheet.
**Chris Lightfoot-Wild** 42:19 Do the… Other languages presumably, just give their own.
Language, like, agnostic?
Oh, sorry, the native, sort of, stack trace, rather than an agnostic one?
**Bob Strecansky** 42:31 I don't know.
**Chris Lightfoot-Wild** 42:33 Because… I guess it simplifies it if we just say, alright, we'll just do the PHP one.
**Bob Strecansky** 42:37 Yeah, so I… I'm asking him, it's not necessarily for your use case. Maybe… maybe it's just… he just asked it as a question, and I was like…
**Chris Lightfoot-Wild** 42:46 But equally, that's… if that's in the SDK, that could be something that we could use SPI for, to give, like, Stack Trace Formatter interface, and…
**Bob Strecansky** 42:54 Sure, yeah.
We could.
**Chris Lightfoot-Wild** 42:56 do SPI for all the things.
**Bob Strecansky** 42:59 Dependency data… oh, this is… renovate. Shut up, renovate.
Laravel termination phase of request handling, not part of root span. Looks like you are talking through this with them, Chris.
**Chris Lightfoot-Wild** 43:16 I can't remember, but if you put it on the board, maybe assign me to it, then I can, I'll vote.
**Bob Strecansky** 43:25 I will do that.
Update all environments, base factories… Looks like… This is… draft.
So that's to-do.
We're doing a really great job of not trying to triage all these issues while we're going through the backlog way to go, Ruin.
SIG meeting details, yeah, this is all updated, and it's fine.
Update bad frosters to emit hotels sim comps, metrics.
That is… To do… P2?
Inconsistent console exporter, this is… I'm hoping to submit PR.
Okay, so help wanted… Right size… Forcing service resource detector prevents from using more stack service instance ID. Looks like Sean was triaging, and Brett was triaging, and it's fixed.
Close… Span drops and fast DGI and PHP FAM setup. Brett and Chris commented on this.
Okay.
Move API component providers to API packages, nive, nive… yeah, Phoenix, whatever his name is… It's a slow tune… So the pressure is back, like, P2.
DevCreate Adapter, HTTP discovery… I agree with this approach.
wanted, prioritize backlog to-do… P2… Cool.
Sport for Frank and PHP, alright!
There's already support built in for Frank and PHP.
**Chris Lightfoot-Wild** 46:09 Which bucket show are they talking about?
**Bob Strecansky** 46:11 Rick and PHP?
**Chris Lightfoot-Wild** 46:12 No, also a symphony, sorry.
**Bob Strecansky** 46:16 Whoa.
**Chris Lightfoot-Wild** 46:17 Good.
**Bob Strecansky** 46:18 Oh, here.
Yes.
Blah blah blah blah blah, there's a lot of comments on this one.
Okay, so that's… this is still a to-do.
Migrate Cloud's trace propagator to Contrib… So, we're so… This person's still working on it, so… We're so close to finishing.
PHP benchmarks, that's mine.
Okay.
Counter issue… blah blah blah… Looks like Pratt was working on this with them.
What's still to do… Expand suppression… Looks like this has been closed for… already… Doctrine Connection spans not appearing in New Relic… SIG faults with Xdebug, Bright is working on this…
**Chris Lightfoot-Wild** 48:20 Well, this is not tested yet, but it sounds like we're good from 3.45.
**Bob Strecansky** 48:23 Oh, yes, it does say that.
**Chris Lightfoot-Wild** 48:25 Is this just… done already now?
**Bob Strecansky** 48:28 Probably. Yeah, bug fix. Good enough for me.
Op cache optimization triggering SIG faults while using OpenTelemetry hooks.
It's for the bug report… Okay, this one looks like it's a bug, and it's still… I wanted… P0.
SDK should collect ITL metrics by default.
Any progress on this? Okay, so this is still to do. Maybe this should be P1, because people are asking about it.
**Chris Lightfoot-Wild** 49:03 Didn't you do some metric stuff recently in the SDK, Paul?
**Pawel Filipczak (Elasticsearch B.V.)** 49:08 Yes.
I added that, so I guess… It's… we can close that.
But… I'm not sure about messaging metrics, so… This is about the… it's not SDK itself, but it's about HTTP.
Database metrics and messaging, so…
**Chris Lightfoot-Wild** 49:29 Right, okay.
**Pawel Filipczak (Elasticsearch B.V.)** 49:31 Yeah, I think we can add it to SP1.
It's quite interesting.
**Chris Lightfoot-Wild** 49:39 Cool.
**Bob Strecansky** 49:39 Looks like it's been floating around for a little while.
They said it's… that was opened in 2024, so definitely people… definitely been floating.
This one is you, Chris!
Opening a review… P1… HubSub instrumentation for auto instrumentation… Yes, I will update the ticket… Network did the ticket… I'm gonna close this, cause I don't wanna deal with it.
Integrating Laravel with SQL Commenter… Please label it. Okay, so this is Help Wanted, projects, PHP projects back.
To do… P1… Or should I be too.
Troubleshooting guide, FAQ… this is still… Specification parity? This is a very old one for you, Chris.
**Chris Lightfoot-Wild** 50:54 Yeah, I guess you can probably close it, because probably the points are highlighted with.
Boom.
**Bob Strecansky** 51:00 Probability-based sampler… Sergey said he was going to take it, but… He ain't here no more.
SDK bundle roadmap questions…
**Chris Lightfoot-Wild** 51:27 This is a symphony thing, isn't it?
**Bob Strecansky** 51:32 It is.
I'm wondering if we should just close this.
**Chris Lightfoot-Wild** 51:43 You could always stick a… If anyone's interested in it, help wanted sort of thing on it, and…
**Bob Strecansky** 51:48 That's on you.
**Chris Lightfoot-Wild** 51:59 I mean, will the step… so, there's a stalebot PR that, Brett mentioned you've got… yes sir, right? If we.
**Bob Strecansky** 52:08 Yeah.
**Chris Lightfoot-Wild** 52:09 in soon.
Maybe a lot of these will just get closed off.
**Bob Strecansky** 52:13 I think you're right.
I'll reopen this.
So let's… That is old as fuck.
Holy cow.
All these are.
**Chris Lightfoot-Wild** 52:39 So we're working in the, Smithsonian today.
**Bob Strecansky** 52:41 I know, seriously.
So… Cardiff requirements more obvious, blah, blah, blah, blah… Initial fix… okay, so it's fixed.
Auto-instrumentation to OpenTelemetry Kubernetes operator… it's from Severin, wow.
**Chris Lightfoot-Wild** 53:13 That's what Joey's kind of been working toward, isn't it?
**Bob Strecansky** 53:17 Say it again?
**Chris Lightfoot-Wild** 53:18 Well, obviously, Sergey had started something, and then… Jerry's, kind of, Picked up.
It's kind of in process.
**Bob Strecansky** 53:30 the… In progress… Did you do… SDK bundle refactor. GMO!
He was such a nice man.
Let's secure,
**Chris Lightfoot-Wild** 53:55 You know, you never know, he might be back if you just tag him on the issue.
**Bob Strecansky** 53:58 I've emailed him twice. I think… unfortunately, I think he actually passed away. It's like, I haven't been able to get a… nobody was able to get any sort of hold on him, yeah.
He was relatively old, too, so… Last one And see… just in time for the meeting to be over.
Let's go. Good work, everyone.
**Chris Lightfoot-Wild** 54:43 I did have a quick question, sorry, at the end there, that I didn't mention before. The, so that… again, the PR I've got open, Bob. Are there any… Do you have any objections to potentially continue it on, like, the 1.0 sort of line?
Just imagine, you know… There's other bits that are obviously still sort of gonna be chopped and changed anyway, but… I'm dropping Laravel 6, 7, 8, and 9.
Which are all, you know, years out of support from Laravel themselves, anyway.
**Bob Strecansky** 55:17 Right.
**Chris Lightfoot-Wild** 55:18 So it's not necessarily breaking, but obviously those packages won't be able to update any… sorry, old applications can't update anymore.
**Bob Strecansky** 55:27 Yep.
**Chris Lightfoot-Wild** 55:28 Does this… this causes any concern? Like… And obviously, Pawel used in the stuff in the distro as well? Does that… Probably didn't.
**Pawel Filipczak (Elasticsearch B.V.)** 55:38 I… what about the supportability from the Laravel itself?
Did they drop it?
many years ago, I mean, the… You mean that you drop the 8, 6, 7, 8, and…
**Chris Lightfoot-Wild** 55:54 Yeah, 6 through 9 have dropped, but I don't think they've been developing those for years.
Actually, yeah, good point, I'll look in the Laravel docs, I think it mentions the supported versions.
Second…
**Bob Strecansky** 56:15 Bluebeats?
Alright, thanks y'all for sticking around for a little extra today, I think that was really…
**Chris Lightfoot-Wild** 56:23 I've got… I've got one thing in the,
**Bob Strecansky** 56:25 Oh.
**Chris Lightfoot-Wild** 56:26 Jutling, sorry.
Version 10, security fixes until February 2025.
Version 11 was until March this year.
So that 10 and 11 are kind of dead as well.
Not to say we have to stop supporting them yet, but… If we were talking about a year on from that point, then…
**Pawel Filipczak (Elasticsearch B.V.)** 56:50 So, if it's one year after this… If they stop supporting, then we can just drop it.
And that's it.
Yeah.
**Chris Lightfoot-Wild** 56:59 So you're happy with that in the distro as well? Like, you can obviously keep 10 in for now, but then on the next, you know, consider dropping that, because that's got no security fixes either.
The alternative is obviously, like, try and hack away at supporting everything all the time, but then it's just loads more work.
Yeah.
**Pawel Filipczak (Elasticsearch B.V.)** 57:16 If it's, you know.
time-consuming. If it's difficult to maintain that later, then it's not worth keeping the support for Just to keep it.
So…
**Chris Lightfoot-Wild** 57:28 Yep.
**Pawel Filipczak (Elasticsearch B.V.)** 57:29 Cool. Right.
**Chris Lightfoot-Wild** 57:31 Thank you very much.
**Bob Strecansky** 57:33 As I say, good enough for government work.
**Pawel Filipczak (Elasticsearch B.V.)** 57:36 Thank you.
Nice, and… see you next time!
**Chris Lightfoot-Wild** 57:42 moment.
**Pawel Filipczak (Elasticsearch B.V.)** 57:43 Nearby.
