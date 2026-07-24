SIG: Swift SIG
Date: 2026-07-23
Duration: 13 minutes
============================================================

## Zoom Recording Transcript

**Bryce** 00:31 Hello, sorry I'm late.
Maybe not.
I was able to get in here.
**vvydier** 00:48 On your image, okay.
**Bryce** 00:50 Just now. Let me… I'm getting the, notes set up.
Let's share… Meeting notes, there we go.
Date… Don't mind.
Alright, if you have a topic you wish to discuss, please put it into the new topics, We'll bring these… Word… Alright, let's get started. So, topics from last week, Cocopods, deprecation plan, the pop blog was finally published after many long hours of… Back and forth with the build system.
**vvydier** 03:05 Oh, it is published on the, okay, official.
**Bryce** 03:08 On the official blog, so that's good, so we can proceed with that.
And, I don't think there's much else to say about that. The next… Migration period begins August 31st. Final publish date for our repo, or for our, the Swift, OpenTelemetry SDKs will be December 30th, and then CocoaPod support ends in The start of December.
So I think everything's on path there.
Let's see here… And so, we have an issue open for merging Swift Core back into Swift Main, sort of a discussion.
Not sure what the timeline for that is gonna be just yet. I was hoping that some more maintainers would be on today to discuss that, but Otherwise, no movement there so far.
**vvydier** 04:29 And Ari, I think, has not joined, right? Last couple of weeks, he's been…
**Bryce** 04:33 Yeah, I think he's been on vacation.
Hmm.
Yep, yep, yep, yep.
That kind of covers all of the last week's topics.
Let's see, I don't really have any new topics for this week. Matt, Vishwan?
Do you have anything you'd like to discuss? Just dropping in to see what's going on?
**Vishwan aranha** 05:03 I'm just… I work with Robert Magnusson on Labs, and I'm just dropping in to learn more about… I'm planning to be a regular on this call starting now, but yeah, I just wanted to meet you guys and say hi.
**Bryce** 05:17 Yeah, nice to meet you.
Very good.
Alright, if there's no topics that anybody wants to discuss, maybe we can just kinda look over… where the PRs are at these days. We got a new… PR Open, looks like, 3 days ago.
And then the usual bot updates.
I'll update the Ager imagery main. So we've got a couple of things that we can take a look at. I don't think there's been any update on this… Issue… Two weeks ago. I'll leave this open for a little bit longer, because I don't… I would like to get at least a little note into the OpenTelemetry instrumentation to kind of explain.
What was discussed in there.
Let's just take a look at this top one here, so… Bound flush semi-4 weight and metrics and logs exporter. So, this is a follow-up to this issue.
Asynchronous processing. Okay, follow up there.
Still block on Barrassing before we wait, so… A request that never completes, hangs, and calls, or oh, yeah, that's no good.
So give it a timeout…
**vvydier** 06:43 So, what's the issue here? That, you had to wait for some time for it to… Release and lock.
**Bryce** 06:52 Yeah, it seems like the… the weight… semi-4… The semi-4 here is hanging if it never completes, so I think, yeah, so… That might be the problem there. Okay, I'll take a little closer look at this after the meeting.
That's… that's good, that's good.
Just a little README update… Ager tracing images have been switched.
as existing images, REL, okay.
Oh, I see, okay. So this is just a simple order example.
**vvydier** 07:32 So they changed it to the… The latest one, yeah.
**Bryce** 07:36 Yeah, yeah, there was some changes under the… in the… in the Ager tracing on how that's deployed, looks like. Okay, cool.
Was there another one?
Renovate pot.
**vvydier** 07:52 The chore is actually opened, automatically by bot.
**Bryce** 07:57 Yeah, these tours are by the… by the Renovate Bond.
**vvydier** 08:02 But it's also Thompson Tomo, right? So that's why I was, like.
**Bryce** 08:05 Yeah, that's the one we just looked at.
**vvydier** 08:06 Yeah, so Thompson Tomo is a person, is a member, or…
**Bryce** 08:10 Oh, yeah, he's a… yeah, and they're… they're… they're inactive. I mean, it could be a bot, I don't know. They have a bot image on there.
**vvydier** 08:20 So, because… Envoy.
**Vishwan aranha** 08:22 I saw their PR.
**Bryce** 08:24 I saw the PR.
**Vishwan aranha** 08:25 They're in Android repo as well, OpenTelemetry, so…
**Bryce** 08:29 Yeah.
Not, not, encouraging with that, with that, avatar there.
Okay, no new issues here… Let's go and look at Swift Core now.
Yeah, just some renovate updates.
Williams Draft… Okay.
And no new issues there.
Alright, well, I guess that really covers it for today, not a lot going on.
Vishwan, did you have any questions or curiosities about the project that you wanted? You know, since we have a lot of time, we haven't really… I'm done.
**Vishwan aranha** 09:19 No specific questions yet, but, if we had to, like, help, contribute to the project, like, can I pick up from any specific issues? Do you guys have a priority order that…
**Bryce** 09:31 Not, not particularly. This, yeah, it's probably something… we could use, like, ChatGPT to do is, is kind of curate our issues. They're kind of a jumbled mess. But, yeah, basically anything, anything in here, there's some good, Let me think here, yeah, we've got other lists of good first issues. If nobody's assigned to it already, then, yeah, feel free to, pick it up. If somebody is assigned to it, but there's not been, like, any action on it, at least no apparent action, just message that person if you're interested in that issue and want to take it over.
Awesome.
Yeah.
**Vishwan aranha** 10:12 So, sounds good. So I'll pick up, like, smaller tasks and, like, something… as I get used to the project, I'll take something that is, like, low risk, and help out where I can.
**Bryce** 10:22 Yeah, that'd be cool.
Awesome.
Thanks, Vishwan. I'm saying your name correctly, right?
**Vishwan aranha** 10:26 Yes, yes, it's perfect.
**Bryce** 10:28 Excellent. Good deal.
Alright, well, I guess,
**vvydier** 10:32 There's also another… Matt, do you have anything to…
**matt** 10:37 Yeah, hi, I'm Matt, I work on Firebase. I just wanted to get a sense of, like.
is this the right group for iOS? And I also want to know… what the… I don't know what it's called, like ROM or EDM or whatever you call it now, Lifecycle Vision is for iOS. Would this be the right… to discuss that.
**Bryce** 11:03 Yeah, to a degree, I think that, The more, like, instrumentation or, like, forward, forward-thinking, SIG for, like, rum and that sort of thing is the, gosh, what do they call it these days?
**vvydier** 11:23 I'm saying.
**Bryce** 11:24 E…
**vvydier** 11:24 Inside SDK, yeah.
**Bryce** 11:27 What's that?
**vvydier** 11:27 client SDK. Yeah, the client.
**Bryce** 11:29 Yeah, the client side, the client-side SIG. They do more discussions on, like, how to monitor RUM, and we're more focused on… The… Swift SDK itself, And so, I think, you know, deciding the, deciding, like, the semantic conventions and stuff like that. It more goes on in that department, in that area, and then we're kind of downstream, and we'll, we'll implement the things that they are designing in that SIG.
If that makes sense.
**matt** 12:06 Yeah, okay, so, whatever they do, you're just gonna implement?
**Bryce** 12:12 Yeah, I mean, like, we'll kind of, you know, after they kind of hash it out, we'll take a look at it, and, you know, there'll be some feedback But, like, generally, you know, they have… You know, I used to be more involved with that one before I got a little bit more busy with, with my, day job. But, They… they seem to have a good idea of… of the… Requirements of mobile despite them being more focused on the JavaScript rungs kind of side of things, and so I've not really had too much contention with… the, you know, like, they're, they designed, like, the, session implementation that we want to use, our semantic conventions around that, and, so… yeah, I guess that's…
**matt** 13:11 Alright, cool, thanks.
**Bryce** 13:12 Yep. Thanks for dropping in, Matt.
**vvydier** 13:15 Yeah, the client side is… client-side is across iOS, Android, and… JavaScript, right? So this is…
**Bryce** 13:20 Yeah, yeah.
**vvydier** 13:24 Okay.
**Bryce** 13:26 Alright, have a great rest of your week, everybody.
**Vishwan aranha** 13:29 Thanks, you too much.
**vvydier** 13:30 Okay, bye.
