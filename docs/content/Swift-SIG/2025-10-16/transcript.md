SIG: Swift SIG
Date: 2025-10-16
Duration: 22 minutes
Zoom Recording URL: https://zoom.us/rec/share/L2-uIA26HTn5YZN9gySJQLF1jJQ6Prta_UEBsjhaxYm5JdTY9IfE-oJDxWvJEoWL.8iLvr9WXJ2Qe4RD7
============================================================

## Zoom Recording Transcript

**nacho** 01:26 I'm putting on here.
**Bryce Buchanan** 01:30 Hey Nacho, good afternoon, how you doing?
Hey, Alex.
**alexcohen** 02:18 Hey, how's it going?
**Bryce Buchanan** 02:20 Good, how are you?
**alexcohen** 02:22 Pretty good.
**Bryce Buchanan** 02:23 Excellent.
Stop moving around so much, you're gonna make me puke with that camera.
**alexcohen** 02:34 Sorry.
**Bryce Buchanan** 02:35 It's like, yum, yum!
**alexcohen** 02:39 How do we even turn that thing off?
**Bryce Buchanan** 02:42 Yeah, it's weird, like, I guess it's a new feature that Zoom had added, but mine was turned off by default, so I don't know.
**alexcohen** 02:51 Still not know if there's an… there's an auto-frame in my video, that's probably not in… Video settings… Mirror… I'm sure it's super obvious, but I'm just not seeing it.
**Bryce Buchanan** 03:11 I'm not… yeah, I'm not sure.
**alexcohen** 03:16 it might actually just be… might not be Zoom, it might just be, like, the camera settings.
**Bryce Buchanan** 03:22 Oh, interesting.
**alexcohen** 03:23 I don't know if there are camera settings.
What is that called? It's like… there's a name for this… for this thing. It's… No follow-up, no follow-up.
**Bryce Buchanan** 03:37 What is it called? It's called.
**alexcohen** 03:41 Oh, fuck it.
**Bryce Buchanan** 03:45 auto-framing.
**alexcohen** 03:48 So my auto-framing is off in Zoom.
**Bryce Buchanan** 03:51 Mmm.
**alexcohen** 03:54 Obviously not.
But, like, it's coming from the… it's my, the display also probably has it in it, like, Apple has its own thing, which probably is what's going on, but I have no idea what it's called.
Don't even know where I could turn it off.
Maybe I just won't move. I bet that.
**Bryce Buchanan** 04:17 Yeah, it's okay, I'm just teasing you.
**alexcohen** 04:23 You know, I tend to move a lot, so it could be, could be annoying for other people, too.
**Bryce Buchanan** 04:30 Okie dokie, let me share. We'll solve that. I'll just share my screen, and then we won't have to look at the cameras anymore.
Okay, here we go. Alright, so let's, take a look at today's meeting notes.
So, topics from last week. Is Ari here? Ari's not here.
Maybe we started too early, but, he's been working on getting some tokens from CNFC for our build process, Looks like… He's added some documentation, or no, rather, this is the documentation for how to add it.
And here is his integration PR, which has been approved.
By me, even.
**nacho** 05:27 Yeah, he said that… In a… that he couldn't, last minute.
personal things arise, so… and that he has a… That solves the topic regarding the authorization in GitHub Actions using the Autelbot.
**Bryce Buchanan** 05:49 Say that again?
**nacho** 05:52 Yeah, he has said that he… solve the topic regarding the authorization in GitHub Actions.
Using the hotel bot.
**Bryce Buchanan** 06:02 Right, yeah, yeah. Yeah, so we won't know if it really, really works until we do a release, so we'll… we'll see that. Maybe we could just open a release build, and And… and test it out.
Let's see here, so, topics from last week… Nothing really new there.
Have you made any progress on the metric filters, Vinod?
**Vinod Vydier** 06:36 I just started looking at the Java one. Yeah, it seems like, yeah, it's set up in a different place, though. It's not in the metric producer there, so I need to do some more investigation.
**Bryce Buchanan** 06:47 Okay, yeah. I was, I was just looking through the other implementations, SDKs.
to see what they were doing, and it looks like Java was having some problem… some problems implementing it. They alluded to it being extremely complicated, so maybe… maybe it might be a little more difficult than I initially thought.
**Vinod Vydier** 07:12 So this would be something that is, done on the instrumentation side, right? Not on the collector side.
So, so it's… it's… it would be on the exporter.
When you are doing the exporting of the metrics.
You should be able to filter some by adding some, configuration to the institution.
**Bryce Buchanan** 07:41 Yeah, I think the idea is that you would use, like, a, like a, A… what do they call it in here?
**Vinod Vydier** 07:50 View?
**Bryce Buchanan** 07:51 Not necessarily a view, but like a, a, Let me see if I can find it… like an… like an instrument, definition.
Yeah, like… So you would be able to use these values to Capture… it's almost like a view, like, to capture the… the metric, but, You know, decide whether or not you want it to be transmitted.
Which I guess a view does too, so… Off the top of my head, I'm not really sure.
I would just follow the… I guess the… one of the key parts is this enumeration that gets returned.
Whether or not it's going to be, accepted or dropped, or accepted partially, which… is an interesting… I guess it would need to return more than just that enumeration.
But we can talk more about it offline.
**Vinod Vydier** 08:56 Okay.
**Bryce Buchanan** 09:01 So it doesn't look like there are really any other topics from last week, so I have a new topic, so Billy, let's all welcome Billy as our new addition to the SIG as a triager, so he's gonna be helping out with, you know, working on, pull request reviews, and helping us, work through our backlog of issues, and being a champion for that sort of stuff, so… Welcome, Billy.
**Billy Zhou** 09:29 Thanks, guys.
Yeah, I really, appreciate the, the community here. Yeah, looking forward to learning a lot with you guys.
**Bryce Buchanan** 09:41 Groovy, yeah.
**Billy Zhou** 09:42 I do have a quick question, For this, this crash issue, 91919, did anyone, Take a look at this, I… I think I might have seen something like this, Sun seems pretty bad.
**Bryce Buchanan** 10:05 Yeah, we took… we took a little bit of a look at it, but this… so this, particular issue, the… the… the 8 bad food error generally refers to, like, the OS killing the process because it was taking too long to initialize, which really the only thing that, in the… in the agent that could cause that is the URL instrumentation, which will scan classes. So the bigger your class, size is in your application, the longer that's gonna take. So I made some notes here about how they can, Hmm.
Kind of work around that, but we haven't heard anything back from them, so…
**alexcohen** 10:48 I would love it if they sent us a symbolicated stack trace. I mean, we… know what the problem is. It would be… I don't know if anyone knows the person that reported this and can reach out to them. They don't seem to be responding anymore to, To the, to the issue.
**Bryce Buchanan** 11:05 Yeah, yeah.
Yep.
But maybe what we could do is, add a little bit more detail to our URL session instrumentation documentation.
that just mentions this potential issue, so if you, like, like, warning, if you see this problem, like, you can override this by specifying which URL session delegates you want instrumented as a list when you implement this, Implement this, instrumentation.
Yeah. Then it bypasses that whole scan.
**alexcohen** 11:45 do we know that that actually takes a lot of time? Because, like, we do have a good, you know, between 5 and 10 seconds to stall on app launch before being terminated like that. So, to me, it feels like it's definitely a possibility.
But, like, things like this are usually more like a deadlock on startups, so they might be doing something that we totally didn't expect, and one of our locks is getting in the way of itself somehow.
**Bryce Buchanan** 12:12 So, I mean, it's…
**alexcohen** 12:14 obviously a good idea to add what you just said, but I sort of have a feeling that it might be more than just the instrumentation, because it doesn't feel like this would take that long, even if the list is big.
**nacho** 12:28 I never saw that, like, pressing because of timeout, but I have seen taking at 2-3 seconds.
just loading.
And, and, and… yeah, because it's a linear… search with all the classes that the system has registered with Objective-C.
Which… If you have many frameworks, it can be a really big, number of classes.
**Bryce Buchanan** 12:55 Yeah, I have run into this before with customers at New Relic, where, you know, we did a similar thing for instrumentation, or instrumentation of the URL session.
So, I know it's definitely possible.
But yeah, I mean, it could be another issue that we're just not aware of, but we really can't tell without, you know, more feedback, so…
**alexcohen** 13:21 I'll try and f- I'll try and, I'll try and find the person.
**Bryce Buchanan** 13:25 Sure, yeah, that'd be great.
**Billy Zhou** 13:28 Thanks.
**alexcohen** 13:28 part of everything, I'm just curious about it, too. I wanna… we're… we have open telemetry, and we all have… we all use the library in… in production products, so if there's something… if there's an issue, we'd like to know about it.
**Bryce Buchanan** 13:42 Yam, yam.
I'll make a follow-up ticket on that one. Where did it go?
Here it is.
To document that… That particular issue that we're talking about.
Okay.
Let's see… If there are no other topics that people want to discuss.
**nacho** 14:31 Just one thing that it was in the… Yeah, the nightly builds, I created a PR with… An idly build of all the targets in the open telemetry Street.
That was a task I had.
Two weeks ago, they're in the page you are showing.
Or, I know, sorry, in the… it was on two weeks ago, about just building a nightly OpenTelemetry Swift, so it downloads the… Maybe I should… yeah, change. It's just building, every night, but I think I could probably… It will be downloaded in the main branch.
Or the latest… yeah, probably I should configure something more.
**Bryce Buchanan** 15:24 Yeah, it sounds like you saw my… you saw my note on that PR.
**nacho** 15:30 I don't know.
**Bryce Buchanan** 15:30 Oh, no, okay. I was, I was just… I asked for clarification, if it was… it looks like it's just pulling the latest release of the core in the test, and running that against the main branch of… the Swift project. I was wondering if we should try to… pull in the head of the main branch on core and run that against…
**nacho** 16:00 Yeah, probably, yes, yeah. I just, I just realized later that, yeah, that's not gonna be… yeah, it will only take the released version now.
**Bryce Buchanan** 16:08 Yeah, I think that it might be valuable to do both, just to make sure that the stuff that is being added to OpenTelemetry Swift is still compatible with our main release… our release version of Core, but also to make sure that our… core version getting added there is also still compatible with what's… what's on the Swift.
**nacho** 16:34 Okay.
Yep. Okay, I will… I will work on that.
**Bryce Buchanan** 16:41 Cool, cool.
Let's just take a quick look at our issues, if there aren't any other topics.
Here we go. Nope, that's Silk Farm.
Thought that I had.
The main branch opens somewhere.
Just a new issue that I added for the discussion from, I think, last week, or maybe the week before, about whether or not AF Networking and AF resume are causing issues.
Haven't had a chance to actually grab that yet, so if anybody else wants to take a look at that, that'd be cool.
And… Oh, okay, I haven't had a chance to look at this either, so that's still on my plate as well.
It's just another… another crash regarding… our URL session instrumentation, it looks like.
And we're not getting a lot of feedback from them.
But, the error does look like they're trying to run network requests while the instrumentation is swizzling, so there could be just a conflict about when when they're actually enabling the URL session instrumentation, so… That's… that's a common issue that can occur.
And then we got this test flight build that we just discussed, and this one's related to the Alamo Fire.
issue.
Binat, have you been able to, this guy.
**Vinod Vydier** 18:52 Yeah, I need to.
**Bryce Buchanan** 18:54 Okay.
**Vinod Vydier** 18:54 Yep.
**Bryce Buchanan** 18:59 And… And then, Nacho, you also had this one as well, were you able to… get started on this. I guess you were working on the other build, the nightly build thing.
And that's kind of the top of our backlog there.
Let's… look at the good first issues here. I'm just wondering if there's anything that might be interesting to anybody.
I actually think that this might be resolved.
Allow headers to be updated in initialized export. Oh, maybe, maybe not, I'm not sure.
Yeah, maybe not.
So, it looks like a code sample on how to properly set up the metrics.
So that they're not, like, constantly sending.
Which basically, I think, is just, like, setting the, the aggregator to, use a delta rather than cumulative, or maybe the other way around, I can't remember off the top of my head, I'd have to look at the documentation. But this might be, if anybody is curious about how to use the metrics library, this might be a good, a good little, like, mini-project to write out documentation on how to do this, to learn it, so… Anybody interested, feel free to grab that.
This is also another good one, I think that some of our exporters, like, while they do pass a logger, they don't do a whole bunch with it, so it might be nice to add some logging in the exporters for when things go awry.
So that's another good one.
Yeah, so, yep, everybody can take a look at Good First Issues if you're interested.
It would be nice to get some of those taken care of.
Any other topics?
No? Alright.
Okie dokie. I guess we can call it here, have a little short meeting today. Not a lot going on.
**nacho** 22:14 Yep.
**Bryce Buchanan** 22:15 That's good. All right.
**Billy Zhou** 22:16 Thank you.
**nacho** 22:20 Have a nice weekend.
**Bryce Buchanan** 22:22 Yeah, you too.
**Billy Zhou** 22:23 bonus.
**Vinod Vydier** 22:23 Bye.
