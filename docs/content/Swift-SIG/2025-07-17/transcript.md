SIG: Swift SIG
Date: 2025-07-17
Duration: 39 minutes
============================================================

## Zoom Recording Transcript

**Bryce Buchanan** 00:58 Harry.
**Arri Blais** 01:01 Hello! How you doing, Bryce?
**Bryce Buchanan** 01:04 Doing good.
Little a little sleepy didn't get very great sleep last night. The kiddo was having some problems.
**Arri Blais** 01:19 I I also didn't get a ton of sleep last night, but that's my own damn fault.
**Bryce Buchanan** 01:27 I mean, you know. It's my fault, too, I suppose.
**Arri Blais** 01:32 I mean we could. You could play that game all day.
**Bryce Buchanan** 01:35 It, raise it back.
Yeah.
**Arri Blais** 01:39 I. I have a few friends with kids and it. It definitely sounds like sleep. Deprivation is a core part of the experience.
**Bryce Buchanan** 01:47 Yeah, yeah. And it they the the hard part is is when they they start getting good sleep. And they're like, Oh, alright! And then they'll like, have a regression. And then you're like, Oh, man.
**Arri Blais** 01:57 Oh, my goodness!
**Bryce Buchanan** 01:59 But usually the regressions don't last that long. So you know.
we're kind of thinking she might be in a sleep regression, though, but she just has been having a hard time this past couple of days.
**Arri Blais** 02:11 Oh, that's too bad!
**Bryce Buchanan** 02:13 Yeah, I don't know if it's the heat. Maybe she's not. Maybe it's just too hot.
Hello.
**Charlie Le** 02:31 My 1st time here. But yeah, I've been trying to contribute to the project.
I just wanted to see how the how the meetings go.
**Bryce Buchanan** 02:46 Cool. Yeah, welcome. Thank you for contributing even on, hey, Martin? We'll we'll get the meeting started in a couple more minutes. Here. I'm not sure if Nacho is, gonna make it or not.
**Vinod Vydier** 03:17 It's okay.
**Bryce Buchanan** 03:50 So, Charlie, the way that this meeting usually works is, we have the notes which is linked in the the meeting. the calendar event.
And you know, oh, you're already there. Good. Yeah. So just add any new topics that you wanna discuss, and we'll we'll go over them when the time comes.
**Charlie Le** 04:11 Sounds good.
**nacho** 04:19 Sorry. I'm a bit late.
**Vinod Vydier** 04:27 Guess that.
What's up.
**Bryce Buchanan** 04:56 I'm not sure.
Okey Dokey, let's get started. So version 2 point. Oh, I think that's ready to release It's I'm I'm just getting I I was on vacation last week, so I'm still just getting reoriented to what.
**Vinod Vydier** 05:21 Don't you agree that he's mad.
**Bryce Buchanan** 05:27 Have a nod you're transmitting. There we go.
I was like, well, Bernard's not not speaking.
Yeah. So we were. Gonna release this before I went on vacation. But I'm I'm I think, that I took care of this. The type aliases I'll have to take make a double check, but
**nacho** 05:51 Yeah. You missed that.
**Bryce Buchanan** 05:53 Oh, it already got merged. That's right. Yeah. So we're ready to release the 2 point. Oh, unless we want to oops unless we want to wait a minute for this race condition.
Get that fixed, and I think there's a couple of other Prs
**nacho** 06:10 Yeah, the the threat race condition Pr is is ready. It has several changes.
Because it was not easy. There were several trace conditions to be okay. Oh, yeah, here it is here. Excellent. Okay?
So yeah. It also changed a bit of the things that you define for the new metrics, like some parameters that were in out that were not needed. And things like that. So okay, very good. It's good.
Take a look and also updated the SDK logs in the code to use another approach more similar to the new text that it apple uses from Ios. 18. That can also be used when we transition to sweep 6, because you can define the types as constant with let. And the and the type includes the lock itself. So it's very similar to the new text that Apple has, but only supports on ios. 18 and up. So that should please review that because it's most in your code, Bryce.
**Bryce Buchanan** 07:16 Yeah, I'll take a look after this meeting, cool or yeah. There's also a couple of other prs, that I think would be valuable to to get in before the 2.0 release.
such as this like a crash preventing swizzling filter for the URL sessions so that it doesn't accidentally initialize classes by just looking at them.
Let's see, was there another one? I think we can take a look at that one in a minute.
But yeah, we'll take a look at that in more detail in a minute. Okay, cool. Alright. So we'll fix that. That's the race condition thing version 2, ios, 15 minimum. So I looked at this recently, actually, let me see if I can.
What did I come up with? Yeah. So I actually I think bumping it up from to 16 might actually be valuable because I was looking at a usage chart.
**Martin Holman** 08:30 Does. Ios. 16 imply.
Other version is imply specific versions of like TV, OS and watch OS and stuff.
**Bryce Buchanan** 08:37 No, it doesn't.
That's not the one I market share. Maybe here we go. Yeah. So here's kind of a a breakdown of the actual market share of of the versions here. And so, like Ios 15, it looks like it's at like 1.9%.
**nacho** 09:04 Yeah, I mean the the the limit I I've put there was more based on in order to upload apps to the to the app store in Ios.
You need a minimum xcode version.
And I think the minimum X code version that now is needed to build your apps for the app store the minimum Ios supported target support is Ios 15.
**Bryce Buchanan** 09:35 Oh, interesting! So you still have to build it, for Ios 15 to go to the app store.
**nacho** 09:42 No, no, no, no! That the xcode version doesn't support building for earlier than that with 16 if needed. In. Indeed, I think that.
No it was no sorry I I missed that. Yeah. The also the 16 version itself. I think that the devices that support 17 are exactly the same, except one model of an ipad, only that supported Ios. 16, but not 17.
But yeah, ios 15 and 16. Yes, they they. They have more devices that could not be supported. But also in the in the document there is an a comment from someone from embrace that says that they are supporting. Ios. 13.
**Bryce Buchanan** 10:31 Go on!
**Ari Demarco** 10:32 Yep.
**nacho** 10:33 The then I, so maybe that yeah, if they are still using that, maybe we should keep that.
But yeah, I don't know how your customers are building apps with that for ios 30 and upload to the app store.
I don't know
**Ari Demarco** 10:57 Yeah, I I still don't know. I I promised I was going to bring some data around that. And if you want guys I can share. I can share that
**Bryce Buchanan** 11:08 So, yeah, if you have it.
**Ari Demarco** 11:10 So basically, what I did. It's see all our customers, all the applications that are out there find the latest up version that was published.
and see from all the sessions of those customers. And that version, if that version actually supports, is 1314, or less so, and and see if those apps read, if we get rid of those apps.
what would be the impact in terms of actual sessions? So let's say, want on the map?
A Google. Let's say they support Ios 1314, and we got rid of it.
How much percentage of the sessions they they provide us would would drop. Because I'm doing this also internally. So people would understand the impact if we bump to is 15.
So what I found out is basically that 12% of the sessions would be impacted by this.
**nacho** 12:18 12%.
**Bryce Buchanan** 12:20 Oh, wow!
**Ari Demarco** 12:21 Yes, because some of the big applications we have actually support. Ios 13, ios. 14.
And those might be the ones that we want support. Because, okay.
**nacho** 12:36 And they, and you know, if they were running in Ios 13 or 14.
**Ari Demarco** 12:42 Yes, I can. I can split that if if needed. If we want.
**nacho** 12:46 I mean, yeah, yeah, that that the.
**Ari Demarco** 12:51 Yeah, yeah.
**nacho** 12:52 The thing is that, yeah, if the SDK supports, that doesn't mean that they are anyone I mean.
can can you put an app in the app store that targets ios. 13.
**Ari Demarco** 13:09 Yes, until now. Yes, you can.
At least that's what what what I can see, because what I'm basically validating is not that we support is 13. Is that the app version in production actually has sessions or usage.
**nacho** 13:25 We? We hire 13.
**Ari Demarco** 13:27 Exactly. So. What I found out is that that said in terms of usage, like actual ios, 13 and 14 sessions, it's less than 1% less. Okay, I'd say, like 0 point 0, something like that. So the amount of usage is almost no. But the impact in those applications will be high unless you go and like, tell them, hey, bump, do newer version. I think Excall is going to force them to do that eventually, because I think.
**nacho** 14:00 Yeah.
**Ari Demarco** 14:02 In 16, I think, or or something like that the next year or this year, I don't remember. They are going to be forced to use Ios 15.
**nacho** 14:12 Yeah, that that's what I worth thinking about. Yeah, that I think they are forcing people to use Xcode 16 already for the app store, I would say so if you upload a new app to the app store you need, it needs to be in xcode 16 and only supports. Ios. 15.
**Ari Demarco** 14:34 Let me!
**nacho** 14:35 That was my believing.
**Bryce Buchanan** 14:46 I'm not able to find what the minimum supported version is, but I do see that the it must be built with ios. 18 SDK.
**Ari Demarco** 14:59 Yes.
**Bryce Buchanan** 15:00 But I don't know what the minimum for that is requirements.
**Ari Demarco** 15:10 I was 16, or later.
**Bryce Buchanan** 15:14 Or xcode 16 or later.
Hmm, well, maybe we can spend some time after this meeting to try to figure that out. Yeah.
**nacho** 15:31 At least at least, for with xcode 16 the the you can only download the Ios 15 simulator.
so you cannot test on something other.
Say with latest xcode, and I don't know if they the SDK you can build against it supports something lower than that.
**Bryce Buchanan** 15:55 Oh, yeah.
to recently, I was looking earlier. But recently, Ios 15 is only is less than 1% of the of the market share. It looks like, according to this metric or telemetry.
there are some nice like generic features that are available on Ios. 16 that might be useful to to have. But we can. We can leave it at 15 if we want to bump it up to 15. Or I see. Yeah, let's figure out what the what the minimum upload version is for for Ios.
**nacho** 16:40 Yeah. And also, if we plan to move to sweep 6, yeah, we it won't be available in all their versions of X code. Right?
**Bryce Buchanan** 16:51 Yeah.
all right, let's move on to new topics. So Charlie Prometheus Exporter book.
**Charlie Le** 17:04 Yeah. So I was just playing around with the a Prometheus sample just following the example.
And I noticed that the exporter that you? That you see, when you run the program, it has duplicate metrics in the the scrape like output. And so I was sort of confused like, why, that was happening, and it didn't seem like a normal thing. But I was just wondering if that was like the expected sort of the expected like behavior of the program, to like continually print the same like value and and metric like every time it exports the results.
**Bryce Buchanan** 17:55 Yeah, that's actually, that's a setting that you can. You can adjust for the I think it's the maybe the periodic what is it called the periodic can't remember off the top of my head what it's called. Let me let me try to find it here under sender exporters.
The periodic metric. Reader, so is it. The metric reader might be the exporter to, or maybe one of the views.
so you can set the the temporality of the metric, whether it's cumulative or delta, and I think that if you only wanted to send like the metric once, if it's not changed.
then it would you would want to set it to Delta.
Let me see if I can find out where that is.
Maybe it's in the aggregator.
**Charlie Le** 19:15 Cause. Cause. What's interesting is like after you like.
you make a request to the metrics, endpoint the entire scrape result is cleared.
and so that makes me wonder if, like 2 people are scraping the same endpoint at the same time, they may get different responses because one of them will basically clear the the.
**Bryce Buchanan** 19:42 The metrics endpoint, and then the other. One sorry.
**Charlie Le** 19:52 Yeah.
**Bryce Buchanan** 19:52 Could you say that again.
**Charlie Le** 19:54 Yeah. So like, if you run the program and then you hit the metrics endpoint that it ex exposes on from the program.
It should start like putting metrics onto the the slash metrics endpoint right? And if you hit that request you'll start to see stuff. But then, if you hit it again, you may see nothing, because it basically clears out what it was exporting before.
So pr, as well. That tries to fix this. But basically, what it does is instead of appending to the list of metrics, it just sets it instead, just like, because I think it has to do with how maybe the the Grpc exporter works in Otlp, where, after you send something, you want to send it again, so it like clears it out. But then, on the Prometheus exporter side, you're expected to keep that.
Whatever metrics are still active, to be scraped.
**Bryce Buchanan** 21:00 Oh, okay.
**Charlie Le** 21:01 Yeah.
**Bryce Buchanan** 21:03 Okay. Maybe that's just a misunderstanding of how the Prometheus exporter is supposed to work.
**Charlie Le** 21:07 Yeah.
**Bryce Buchanan** 21:08 Cool. Okay, do you have can you, on this Pr share the relevant spec for the Prometheus Prometheus exporter that that could that that shows that just cross reference. It.
**Charlie Le** 21:27 From, like the from the Prometheus Repo, or something like that.
**Bryce Buchanan** 21:30 Yeah, yeah, I'm not. I'm not very familiar with the Prometheus spec. So I'm not sure where that would would actually come from.
**Charlie Le** 21:38 Okay, yeah, I'll link it sure.
**Bryce Buchanan** 21:40 Alright. Thank you.
Cool.
**Vinod Vydier** 21:43 So so the the issue is, once it exports it, it resets it to 0.
**Charlie Le** 21:50 Once it ex once you hit that endpoint, the metrics endpoint that it exposes, it actually clears out everything because there's that function. Get and clear metrics. You see online?
I think it was 45. Here on the 1st file, Prometheus exporter.
It actually just overrides it to an empty list, right? And so that's that's what happens. And so basically, it's it's it's kind of like if 2 people are scraping that endpoint right there. One of them is going to see something else, basically depending on, they scrape it. And so that's not expected. I don't think that's expected.
**Vinod Vydier** 22:34 So the solution is to not call it right, but to clear the metrics.
**Charlie Le** 22:39 Yeah, you don't want to clear. It's been scraped that that doesn't make any sense to me.
**Vinod Vydier** 22:45 Yeah, so does this not clear in the metrics? Does it have any impact in terms of.
does it like keep adding to the memory.
**Charlie Le** 22:57 Yeah. So if you if basically, if you, the way that it is right now is if it keeps running, it's going to keep appending the current list of metrics to itself indefinitely until it runs out of memory.
That takes right.
So that doesn't seem like the right behavior.
**Vinod Vydier** 23:21 Oh, so this. So this is just a stopgap. We gotta take care long term.
**Charlie Le** 23:26 No, this is. This seems like the actual behavior that you that you would want where you would copy the metrics that are being instrumented by the like, all of the metric, the meters that you have.
and then put that as something that you would want to export.
**Vinod Vydier** 23:47 Mean.
okay.
Thanks.
**Charlie Le** 23:54 Yeah, sure.
**Bryce Buchanan** 24:01 Alright cool.
We'll take a closer look at that.
Okay.
so let's look at some of these other Prs that we have. Yeah. So we have this race condition one. I'll take a look at that after the meeting.
this seems like a pretty good change. I I looked it over. I don't know if anybody else wants to take a look at it before we merge it, but essentially, what it's doing is it's just providing a new configuration to the URL session instrumentation which allows a ignore class prefix array of of class names and stuff.
And it'll check against that when it's looping through the the list of.
**nacho** 24:57 Yeah. The truth.
**Bryce Buchanan** 24:58 Wants to
**nacho** 24:58 Yeah, one tries to switch all the methods right?
**Bryce Buchanan** 25:02 And it'll skip over anything in the class. And yeah, it makes sense to me.
**nacho** 25:07 Yeah. Totally.
**Bryce Buchanan** 25:07 The the submitter was saying that they're they have some like classes that get messed up if they get initialized at the wrong time, and by looking at it use doing the swizzler stuff to it like that call, you know, initializes a class. So yeah, I think that that this is a This is a good change. I had some just minor nitpicky feedback. But yeah.
otherwise, if yeah, if nobody wants to take a look at it. I'll get this merged once my feedback is
**nacho** 25:44 Took a look. Yeah, it looks good. Yeah.
I didn't add my my commentary because you had your comments. But yeah, for me, it looks good. I didn't approve because you had comments simply, but yeah.
It makes sense.
**Bryce Buchanan** 25:59 Cool.
See fixed links to help wanted in good 1st issue label.
**Charlie Le** 26:14 Oh, yeah, this was me I just noticed, like in the readme on the the main repo, the the link is like broken. And so I just made it like pretty with Ghana. It shows you the number.
a factor open issues as well.
**Bryce Buchanan** 26:28 Oh, yeah, look at that. That's cool.
**nacho** 26:34 Yeah, that's quick.
**Bryce Buchanan** 26:36 I've not heard of this. This image shield.
**Charlie Le** 26:40 Yeah, it's it's used in a lot of the open telemetry collector contrib exporters and receivers. And so they have like this image on all the the Readmes.
**Bryce Buchanan** 26:53 Nice.
**Charlie Le** 26:54 To give, like an idea of how many issues are currently like related to that exporter or that receiver.
**Bryce Buchanan** 27:07 Yeah, I think that looks great.
**nacho** 27:12 Yeah, also, we can. Now, now it there is a at least we can merge. Automatically.
They added some kind of train of approval. Yeah, that that's right.
**Bryce Buchanan** 27:27 Oh, for like
**nacho** 27:30 Yeah. Auto merging when everything passes.
**Bryce Buchanan** 27:34 Right? Yeah.
Okay. So fixed links, we'll take take a look at that in a little more detail. Later.
Chores, chores, chores.
Alright cool. Yeah, I think that's everything. So we'll get these last couple of big issues merged.
this needs to get. It's got some. There's some name changes that need to get resolved on this one.
If you could take care of that, Charlie.
**nacho** 28:14 What's that? Yes.
**Bryce Buchanan** 28:17 Conflicts that need to get resolved before this can can be approved and merged.
**Charlie Le** 28:22 Okay. Yeah. Okay. Sounds, good.
**nacho** 28:24 Yeah, basically, the a stable from the metric name has has been changed. That that's probably that.
**Charlie Le** 28:32 Yeah, sounds good.
**Bryce Buchanan** 28:37 Cool all right.
Great is there any other topics anybody wants to cover?
**nacho** 28:46 Yeah, basically, version 2, we wait for the minimum version for Ios decision.
**Bryce Buchanan** 28:56 Yeah, let's yeah, let's sort that out.
**nacho** 28:59 And yeah, let.
**Martin Holman** 29:03 We do, we need to discuss the other ones as well. The watch OS TV, OS, etc.
**Bryce Buchanan** 29:11 I think that we should.
**nacho** 29:11 I.
**Bryce Buchanan** 29:12 Yeah. Go ahead.
**nacho** 29:14 Yeah, I was saying that what the the version that matches with Ios 15 whatever it is for Mac OS Macos, and I don't remember which one it is. But yeah, probably I will keep diversion data.
the features that comes from one person to in order to match all the others.
So.
**Martin Holman** 29:37 Makes sense.
**nacho** 29:38 Yeah, whenever it comes to 26, like New Ios, 26, everything will have the same number.
**Martin Holman** 29:45 Oh, yeah. True.
**nacho** 29:46 Basically whatever the year that that was released, the one that was for each other.
that that was the idea. When I said the target of expression. It was to say, just one of them.
I'm another, related one.
**Martin Holman** 30:02 Tape.
**nacho** 30:02 My main concern here was if there was some market developer with, because you don't need to use xcode or a given version of xcode to release your apps, because you don't depend on the app store. But for xcode 16 I thought that it was already mandatory to use X code 16, and that it didn't support billing for something earlier. But maybe it does.
So. Yeah, we should clarify that.
I don't mind if we still support ios. 13. But yeah, I don't know.
There are some things that came with Ios 15, like some timers, for example, that behave way better.
And probably if we want to move to Swift 6, we will need X Code 16 also, and many of the features that I don't know if they will roll back very well with earlier X code versions that won't support.
Yeah, that that was my main concern with with this.
and that we cannot test on other persons either.
If there are any issue, any back, we maybe there are no ways to test that or even run on Github.
Okay.
**Bryce Buchanan** 31:48 Alright. Well, we can continue this in the in the slack channel in the switch.
I'll try to find what the actual minimum supported upload version for the latest version X code is. And then, we'll go from there honestly, like.
I think that if we can find some more data on like market share and usage.
That might be helpful to look at as well.
**nacho** 32:25 Yeah, it's it's true that with us those numbers, even your Ios 15 looks like totally out of the market. Now.
**Bryce Buchanan** 32:35 Yeah, yeah.
**nacho** 32:36 But yeah, but as most of the users of the library are Middleware, and they have our.
**Bryce Buchanan** 32:45 Well, yeah, yeah, that's the yeah. That's the the thing is like going. Yeah, because, like, you may have users on old versions of of, you know, using old versions of your application. But it's like, you know, the they might not even be able to update to later. Ver, yeah, I don't know. It's weird.
Okay, yeah.
**nacho** 33:10 We can talk about this more offline.
Yep.
**Bryce Buchanan** 33:15 Alright. Well, I don't have anything else.
**Billy (he/him)** 33:17 I had a question, hey, guys?
I was thinking about submitting implementation for sessions.
hey? Can you guys hear me? Kind of.
**Bryce Buchanan** 33:29 Yeah, we can hear you.
**Billy (he/him)** 33:30 Okay.
my screen blocked out. Yeah, I had a question about what we're doing with session. Id. I remember from a while back. Where, there's a question about how to get session Id into the resource object which is immutable, and from what it looked like it seemed pretty tricky to update this object without like tearing down the whole agent and rebuilding it, and everything or like sorry tearing down the you know all the other the pieces of the system. Is there like a recommendation on that or
**Bryce Buchanan** 34:10 Yeah.
**Billy (he/him)** 34:10 It's just like on the regular attribute is.
**Bryce Buchanan** 34:13 Yeah, yeah, the it. It's not feasible to add it to the resource attribute directly. I think the only way that we can solve this problem is by creating, like a a new type of processor that fits in between, that that adds attributes to signals like it with a with like an attribute, or with like a attribute manager, or something along those lines.
**Billy (he/him)** 34:42 Okay? So that that's fine. There, right? Session ideas.
**Bryce Buchanan** 34:47 Yeah.
**Billy (he/him)** 34:49 Okay, yeah. Would you guys be open to like reviewing something like that? Then.
**Bryce Buchanan** 34:55 Absolutely. Yeah. Bring it on.
**Billy (he/him)** 34:57 Okay, cool. Yeah. I'll I'll put something together. Thank you.
**Bryce Buchanan** 34:59 Great. Thank you.
Alright. Well, I guess we'll see you all next week.
**Vinod Vydier** 35:15 But yeah.
**Martin Holman** 35:15 You know.
**Vinod Vydier** 35:16 Good weekend, bye.
**nacho** 35:18 Bye.
