SIG: Swift SIG
Date: 2025-11-13
Duration: 20 minutes
============================================================

## Zoom Recording Transcript

**Bryce Buchanan** 01:10 Nope.
Hey, Nacho!
**nacho** 01:19 Hi, Bryce. How are you?
**Bryce Buchanan** 01:21 I'm good.
How about yourself?
**nacho** 01:26 Fine, yeah, that's important.
**Bryce Buchanan** 01:30 Nice.
**nacho** 01:31 Had some pressing leaks recently.
Yeah, some releases that we have soon.
And you know that dates, usually.
**Bryce Buchanan** 01:45 What's that?
**nacho** 01:46 Yeah, something's to release soon, so…
**Bryce Buchanan** 01:50 Oh, damn.
**nacho** 01:51 And that, yeah, that have taken several months.
So yeah, it gets… More pressure.
**Bryce Buchanan** 02:00 Yeah, no fun.
**nacho** 02:02 Nope.
I mean, fun, but different kind of fun.
**Bryce Buchanan** 02:06 Yeah, I suppose it's the Type 2 fun.
There you go.
**nacho** 02:10 throat.
**Bryce Buchanan** 02:12 It's not… it's not fun when you're doing it, but you look at it, and it was… that was fun.
Ari said he's not gonna be here today.
We'll just give it another minute or two.
Enough time for me to figure out where… My note window is.
What in the world?
Okie dokie.
Alright, so let's get started.
topics from last week. Dependabot was complaining about our… Core…
dependency, and, so I just added it to our… Ignore list, I'm not sure…
if this is actually gonna work, because it doesn't seem like there's a way to test it. I was trying to, like, find, like, a Dependabot linter or something, but…
Damn.
Or a job that we could run, but I couldn't see a job. It must be managed in some other repo. I don't know if anybody else knows.
How that is managed, would be useful.
Okay, alright.
Nightly builds.
Nacho, have you been able to make any progress on this with the, notes that we had last time?
**nacho** 05:23 No, I just confirmed that, yeah, I will use this new approach, even if the package must be modified for taking an environment into account, which is not very pretty.
But… Yeah, modifying that.
Yeah, he's… It's a nightmare.
And yeah, very error-prone, no way to do that. So, yeah, I will… I will move to this.
Ember, even the app package needs. Yeah, some.
some visibility on that, which I wanted to avoid, but yeah.
**Bryce Buchanan** 06:02 Okay, sounds good.
I guess that's all the topics from last week that needed discussion. Are there any new topics for this week?
No?
I see that we have a new, participant, Eric.
**ES Erick Sanchez** 06:28 Hey, folks.
**Bryce Buchanan** 06:31 Harding.
Welcome to the, SwiftSig. Was there anything you wanted to discuss, or have any questions about, about,
Our, librarian.
**ES Erick Sanchez** 06:42 Yeah, thank you. Wanted to surface, or I guess ask about… I guess I should have done maybe a little more research to see if it's already an existing problem.
So we're using, of course, the iOS SDK.
And we're noticing there… there's some crashes.
And I believe it's a… It's a data race, and And the metric…
In the metric, like, side of things, like, when we log some sort of metric, like an integer.
We're getting a data… what looks like a data raise. I think I could show it here.
**Bryce Buchanan** 07:23 Oh yeah, sure, that'd be… that'd be great.
**ES Erick Sanchez** 07:25 Any PII on this screen?
So, let me at least try that.
But…
Okay.
Fingers crossed.
So… This is the crash that we would get, and then looking at…
I guess where it lands, I guess we don't know.
We're not sure where it would land.
But this, this piece is inside the SDK.
And we were getting a handful of these, and…
I didn't, I didn't, mitigate the problem itself. It was another, another teammate.
And the… the change involved… Basically, anytime we… So we have our… It's, tracing…
like, a tracing layer that basically communicates to a handful of data sources of, like, hey, yeah, we started some work, and then we added some attributes, and then we finished the work. So, we just have, like, an abstraction layer that
That does that. And then, within each of these points, we communicate to our data sources, one of them being OTEL.
And then when it goes through that, I need to find a trace where it does that. This one isn't actually it, but all of them land around, I believe, this.
this component?
They have the same crash.
But basically, once we do those three things where we start, add some attributes, and then we finish the span, we get this crash.
And the solution was to just take that… take, I think the start and end, and just wrap it around some sort of, like, serial queue to where there is no data race.
So everything is happening, you know, serious, visiting non-concurrently, and that fixed, that fixed the problem.
**Bryce Buchanan** 09:33 Hmm, okay.
**nacho** 09:35 Okay.
Yeah, I have a couple of questions. First is, you are using the latest version of the library?
**ES Erick Sanchez** 09:43 That's a great question.
**nacho** 09:45 I mean, I remember I fixed several race conditions that we had in the… In the… in the…
In the metrics type?
Logado?
I cannot remember when exactly, but probably 3-4 months.
would be? Do you remember, Bryce?
I'm gonna run that.
**Bryce Buchanan** 10:08 Yeah, I vaguely recall.
**nacho** 10:11 And it could be related to that. Those were all the…
Threadroid condition that we could find in our tests?
So I basically ran the test with the thread sanitizer, and it pointed to some of those press conditions and were fixed.
So that brings the second question, is that… If you run… Any similar workflow
directly in Xcode in Europe with spread sanitizer, can you see that?
Race condition, being logged in Xcode.
**ES Erick Sanchez** 10:53 Mmm, I'm not quite following. What am I looking for?
**nacho** 10:57 Yeah, yeah, basically the first is knowing if it's the latest version of the SDK.
**ES Erick Sanchez** 11:01 Because if it's a bit older.
**nacho** 11:04 like, the 2.0 version or something around that. I think it still had those risk conditions.
They were fixed late, like, later, like, probably the release notes have that.
So that will be the first question, because it could be fixed.
Already in newer, versions.
**ES Erick Sanchez** 11:26 And if not, so…
**nacho** 11:28 And if it's updated the library, and it's in the…
In the, in the, in the newest version, then probably…
We… the thing will be to know exactly where, so maybe we don't have a test that has a similar
behavior, or… Something like that, so we cannot… detecting… Can you unmute?
**ES Erick Sanchez** 11:59 Got it, okay, I think that's… that's gonna be a start, because this is, this is what we have.
Oh, cool.
This is one of our fellows.
So, it looks like it's quite old, the version that we have. You mentioned it was a few months ago?
**nacho** 12:21 Oops.
Let me… I were… I was checking now…
Yeah, we have, in version 2.0.0,
I thought it was, after that, but no, we waited for that. there were several.
Threadrace condition in the new metrics API.
**ES Erick Sanchez** 12:46 Sweet. Okay, yeah, it looks like it's been…
**nacho** 12:51 I don't re… the… it was in… the… the Committed 7-1?
**ES Erick Sanchez** 12:59 I see your commit.
This one here.
**nacho** 13:03 Yes, that one, yeah, that one. So in that, there were… Many people?
So, if it's… Before that…
yeah, there were several risk conditions. If you are in 2.0 or later.
then… then we should fix those, yeah. So that will be the first thing to know about it.
Because probably, if it's on there, probably it's fixed.
Because there were several press-rise conditions. It was still not, like.
I mean, 2.00 was the first that we Publicly said that
metrics was, like, a great state, so we really replaced the old metrics and stuff, because that was basically for 2.0.
So if you are using Yeah, the metrics, probably…
Moving to 2.0, at least, will fix this, if you are not there.
**ES Erick Sanchez** 14:06 Gotcha. Okay, yeah, we are… looks like we're way back here, so…
We will definitely start with that. Okay.
Okay, Gran.
**nacho** 14:18 Oh, yeah.
**ES Erick Sanchez** 14:18 Yeah, please.
**nacho** 14:18 Probably fixed, then.
Maybe you can backport those.
a custom… I mean, probably you can… I don't know if you can update your library?
Maybe you can just…
cherry-pick that commit in a local branch if you need that. I don't know how you are building, but…
Yeah
If you're very old, it will be… it will be different… difficult to… to… to do, but, I mean, depends on how quick you want to fix that, or if you want the new things that come with 2.0.
**ES Erick Sanchez** 14:55 Yeah, yeah, basically we'll definitely have to do the…
Do a… a changelog between now and then, and see what we'll need to do to upgrade, or… yeah, well, we could probably cherry-pick and start from there.
Okay, Grant.
Muchas gracias. Yeah, this… this will… this will definitely be a good thing to… to try out, because, yeah, we'd hate to…
**nacho** 15:21 Yeah, I'm not saying it's fixed, right?
**ES Erick Sanchez** 15:24 I'm not saying it's fixed, but I really fixed many of them, so it's probably there.
**nacho** 15:29 Yeah.
**ES Erick Sanchez** 15:30 Grant, sweet. Okay, Grant, thank you. Yeah, we'll give it a try and see if we can get it in, and love to report back.
**Bryce Buchanan** 15:37 Yeah, if you are still seeing issues, you can join the CNFC Slack channel for, Swift, here.
Let me see what the exact name of it is, if I can remember. I think it's just,
I think it's just hotel-Swift.
So you can ask some questions in there, get some quicker feedback.
than waiting.
For Thursday's… the Thursday meeting. And then if it looks like it's an actual problem, we can open up an issue on the repo and start investigating it there collectively.
**ES Erick Sanchez** 16:14 Alright, sweet. Alright, will do.
**Bryce Buchanan** 16:16 Cool.
**ES Erick Sanchez** 16:20 Alright, thank you all.
**nacho** 16:20 Yep.
Also, I mean, if you really want to know if it's fixed, for example.
You can… if you run your app with Thread Sanitizer, and you do something like that exercise that code.
Thread sanitizer running in Xcode will show you.
Stress… the race conditions, even if they don't crash.
Because it… it… it just takes the…
memory areas, and if you touch a memory area which is shared with another thread, then it warns you. So it might point to the… to the place that's having the trace condition.
And you can check in the new version if that line is already covered, or if that value is…
Under a lock or not.
**ES Erick Sanchez** 17:14 Oh, grand, okay. Yeah, I'll give that a try. I think,
I can't recall if the fix itself was a shot in the dark, meaning, like, they didn't… they weren't able to repo it,
And… But after… after sending the change and sending it to production, it looks like the… the…
The number of crashes went down.
So, I'll, yeah, I'll try, since you mentioned it may not… it may not crash in Xcode, but at least it will point.
Could at least try that. Because, yeah, there is…
There's many places where we would use this, so… because it is just telemetry, so…
**nacho** 17:52 Yeah.
**ES Erick Sanchez** 17:54 as I will point out.
**nacho** 17:55 It's a really great tool, if you have not used it.
It's… yeah, it's a must run from time to time.
Yep.
**ES Erick Sanchez** 18:05 Oh, sweet.
**nacho** 18:05 Even with a test, for example, it's really, really useful.
**ES Erick Sanchez** 18:10 Sweet.
Appreciate it.
**Bryce Buchanan** 18:14 Cool.
Let's see, so… just some other notes that I wanted to… here, let me share my screen again. Actually, I'll belay that. Billy, do you have any, any issues that you want to talk about? Have you found anything interesting for prioritization?
**Billy Zhou** 18:38 Sorry, guys, lately I've been, kind of, hunkered down on, some work, but, yeah, I'm just, trying to, get some time to upstream all my, instrumentations that I did.
But, yeah, sorry, not in the last week.
**Bryce Buchanan** 18:59 Right on. No worries. I'm looking forward to seeing that instrumentation.
Let's see, so,
let's see, let's see. The, instrumentation for metric kit that was, recently,
In review, has been merged, so that's, thank you, Bea. Appreciate that one, that's a good one.
**Bee Klimt** 19:20 Thank you.
**Bryce Buchanan** 19:22 And for my plate, I need to investigate this,
this, AF networking issue, I believe, that's been on my plate for a little while.
So I'm gonna try to, take a look at that this week.
Specifically, this one.
Let's see, any other topics?
Well, if there's nothing else, I guess we can, call it here today.
Thanks for joining, everybody. Oh, hey, Vinod.
You're just in time for us to leave.
Alright. Have a good weekend, everybody.
**nacho** 20:33 Bye. Bye.
**Bryce Buchanan** 20:33 Bye.
