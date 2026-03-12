SIG: Ruby SIG
Date: 2025-11-11
Duration: 17 minutes
Zoom Recording URL: https://zoom.us/rec/share/mWrVX-6ig-E93L5tm3LVEj4HauewcW9j1sqfHNOdIkHli02qB6D0n25wNp4Wp8v0.eZWbeoxKi7qfqL6d
============================================================

## Zoom Recording Transcript

**Hannah Ramadan** 01:55 Hey, Wendy, how's it going?
**Wendy Smoak** 02:01 Oh, pretty good. Wasn't sure how many… People we'd get if people have the holiday off.
**Hannah Ramadan** 02:07 Oh, yeah, I know, Ariella won't be here, Kayla also can't attend, so it could be… Could be just us, we could… Start looking at.
**Wendy Smoak** 02:21 I mean, it's recorded, so we can just look at the agenda and see if there's any PRs or anything.
**Hannah Ramadan** 02:26 Yeah.
So… I'm assuming neither of us went to the specs, say.
Keep meaning.
**Wendy Smoak** 02:35 Me too.
**Hannah Ramadan** 02:36 8 Pacific.
And it's canceled due to KubeCon, so…
**Wendy Smoak** 02:41 Yeah.
**Hannah Ramadan** 02:41 Nothing to see here.
Could be a quick one.
Pop in the core, see if there's any new issues.
Three days ago, there is… Let's see… This has to do with the logs and metrics SDK.
Nice, okay. Well, I think this… I'm… looks well documented.
And…
**Wendy Smoak** 03:33 I've also had… I've also had weirdnesses, like, I don't know, if it doesn't work, I just keep adding require statements, so it is entirely possible they're not.
Done in, like, the best… way, because I also… like, things don't work, so I asked… Claude to fix it, and it adds more require statements, and then it works, so… Probably someone should see if it could be done better.
**Hannah Ramadan** 03:59 Yeah, that does seem.
**Wendy Smoak** 04:00 I haven't stopped to try to see if there's anything… Like, wrong with it?
Seems… plausible.
**Hannah Ramadan** 04:09 Yeah, I think this is definitely one to take a look. I know we just… Carson. Yeah, and… Hopefully easy to fix, if we just need to add some requires in places.
**Wendy Smoak** 04:21 Either Caleb will explain why it is the way it is, or…
**Hannah Ramadan** 04:24 I have a feeling Kayla will want to take a look at that one.
**Wendy Smoak** 04:28 And that's me, I'm actually playing with that right now.
**Hannah Ramadan** 04:31 Nice, okay.
**Wendy Smoak** 04:33 basically by saying, hi Claude, go look at the python, because they did it, and see how you would do it here. Yep.
**Hannah Ramadan** 04:39 Love a good AI mask.
**Wendy Smoak** 04:45 Yes, we should have metrics coming out of the, like, how many log messages it processed, and what the size of the queues are, and such.
**Hannah Ramadan** 04:53 Wise.
**Wendy Smoak** 04:54 Maybe. We'll see.
First, I had to figure out Weaver and how it generates the things.
**Hannah Ramadan** 05:04 Yeah.
**Wendy Smoak** 05:05 that I've figured it out, but I got it to do it.
**Hannah Ramadan** 05:09 I mean, I haven't played with either.
Okay, some pull requests…
**Wendy Smoak** 05:17 Fun!
**Hannah Ramadan** 05:18 This, I guess this is the fix to the bug. Okay, that's nice, that's nice that they did that.
**Wendy Smoak** 05:23 Oh, this goes with the issue. Got it.
**Hannah Ramadan** 05:25 Yeah, so that's actually great that they…
**Wendy Smoak** 05:27 Yay!
**Hannah Ramadan** 05:31 Like, I'm assuming this is all Truffle Ruby failures… I may look into that later, maybe something we could do for this person.
**Wendy Smoak** 05:44 I mean, I merged main into my fork, and a bunch of stuff failed, so, like, I… that shouldn't happen.
Something must be wrong.
**Hannah Ramadan** 05:53 Yeah, I wonder if it… I wonder if we're seeing the same shuffle review issues, it's like a… Probably not on here, but… Nope, okay.
I was like, for the same thing, so it's like, oh, clearly it's like a truffle ruby or something.
**Wendy Smoak** 06:13 Unreal.
**Hannah Ramadan** 06:14 reasons. Maybe we could rerun it. I can't.
**Wendy Smoak** 06:19 Yeah, I don't have that button either.
**Hannah Ramadan** 06:20 Let's see if we can…
**Wendy Smoak** 06:32 And mine looks like… Yes, mine… I have the same failures when I merged Maine into my branch this morning.
Yet, Maine was passing when that commit made. So, something's going on.
**Hannah Ramadan** 06:52 You had the same truffle root beer failures?
**Wendy Smoak** 06:54 Yeah, on my fork.
**Hannah Ramadan** 06:56 Okay.
**Wendy Smoak** 06:57 I merged main into my… main on my fork just a little bit ago, and it emailed me with a bunch of failures, but it's also TOEFL Ruby, so something else is…
**Hannah Ramadan** 07:08 Okay.
**Wendy Smoak** 07:09 going on? Because it passed when… The commit was merged to main in the main repos.
**Hannah Ramadan** 07:15 Okay, hopefully just a rerun or something smooth.
**Wendy Smoak** 07:17 Yeah.
**Hannah Ramadan** 07:19 Ariel wanted to bump… Minimum 232. Looks like there's one… Failure…
**Wendy Smoak** 07:29 J, Ruby.
**Hannah Ramadan** 07:31 Yep.
**Wendy Smoak** 07:39 It's been so long since I worked on frameworks and had to care about all the different.
**Hannah Ramadan** 07:43 I know all the different K-Rubies.
terrifying to me. I just really have such trouble with that.
canceled after 360 minutes. We should probably have a, the maximum try.
That's funny. Okay, maybe that's just another rerun, I don't know. I think…
**Wendy Smoak** 08:06 Very, very simple.
**Hannah Ramadan** 08:08 Yeah, there's probably something there, I'm sure I'll take a look at it.
And another… PR, invalid, dependabot config, and I assume this is Truffle.
It is? Okay, so that just needs another rerun, too. I can have Kayla rerun all of these.
Perfect, this looks like… Small… Okay, so it looks like all the JRuby, and then we saw a Jaeger issue, I think in the 3-2 PR that Ariel just opened.
**Wendy Smoak** 09:09 And he's saying that we should just exclude compatibility for it, unless…
**Hannah Ramadan** 09:16 Great.
**Wendy Smoak** 09:17 Alright.
**Hannah Ramadan** 09:23 Nice.
**Wendy Smoak** 09:24 I might start a thread, because I don't… I haven't quite… I'll… I might start a thread in the Slack to say, alright.
There's a note on this PR and that PR, so what is… what is going to happen?
**Hannah Ramadan** 09:41 Yeah, wait, you said zero.
**Wendy Smoak** 09:43 Peter's having trouble with FixNum, and that's related to JRuby, but I didn't catch… he said something about Truffle Ruby at the top, so did he…
**Hannah Ramadan** 09:49 fix it?
Allows installation of all stuff over.
**Wendy Smoak** 09:54 Okay.
Alright, so maybe when that one merges, then it'll all go away.
**Hannah Ramadan** 09:58 Yes, actually, that's… Beautiful, so we actually need to merge this and rerun everything.
So we don't need to rerun these, what we really need to do… It's large.
then I guess we need to merge those into those branches, which…
**Wendy Smoak** 10:20 Yeah.
**Hannah Ramadan** 10:21 Yeah.
Cool.
**Wendy Smoak** 10:23 Good.
**Hannah Ramadan** 10:27 Alright, contrib. Any new issues? Yup, drop support, probably a…
**Wendy Smoak** 10:36 Oh, no.
**Hannah Ramadan** 10:36 Good.
Yep, no longer maintained. Great.
Arielle has been working on some semantic convention stuff for HTTP.
**Wendy Smoak** 10:50 Convention Rules? What does they say?
**Hannah Ramadan** 10:53 Yeah, so the… I think it had to do with the names. When we don't know what the method is, it should be other.
And then that also affects what the span name is as well, so he's working on, I think, a series of PRs To address something?
**Wendy Smoak** 11:14 So these are, like, directives in the… in the spec that tell us what to do that we need to follow.
**Hannah Ramadan** 11:20 Exactly, yeah.
**Wendy Smoak** 11:20 Got it.
**Hannah Ramadan** 11:24 And… this is his issue, and… Yep, started working on some PRs for that, so that's great to see.
Then nothing else… Nothing else, no.
I think this is ready to be merged by… Oh, wait, sorry, not this.
the pull request associated with that was ready, but I don't think it has been yet, yeah.
**Wendy Smoak** 12:01 Don't need to review it looks like.
**Hannah Ramadan** 12:10 Thought we were good with this, but maybe not quite.
Okay, well, once that's… Take a look at it. It's hard not to have many, like, working powers. Yeah, next week, probably, we can get that one merged, and… Still in draft, still in draft, and then this is one of those PRs from the issue that Ariel submitted.
**Wendy Smoak** 12:39 Changing…
**Hannah Ramadan** 12:41 Names, I believe, yep.
**Wendy Smoak** 12:54 No emergencies. I did not break anything this week.
**Hannah Ramadan** 12:57 Nope, this is always…
**Wendy Smoak** 13:00 Embarrassing myself on the internet since, like, 2005, and open source stuff. It's, like, fine. Like, done it!
Did it really have to be Martin showing up, telling me this?
**Hannah Ramadan** 13:08 Like, this is not doing…
**Wendy Smoak** 13:12 Oh, well.
**Hannah Ramadan** 13:17 Whoa.
**Wendy Smoak** 13:18 Anything else?
**Hannah Ramadan** 13:20 No, I think… I think that's all, contra, I'm just, like, new.
Like, the wish code for honors…
**Wendy Smoak** 13:40 There was a thread, I don't even remember it. I have to reproduce… so we put the logger bridge into a fairly complicated project with Puma?
And… it… you know how… I don't know if you looked at the code, it has a mutex to avoid getting itself into an endless loop.
like, logging… the SDK can't log… To itself, or it'll just keep going around and around, so there's a mutex to keep it from doing that?
But… In that situation, in that project, running it locally, it runs… it runs into that problem and crashes.
**Hannah Ramadan** 14:19 Oh, interesting.
**Wendy Smoak** 14:20 I have to figure out what the… it was… it's, like, not a project I work on. It's like, hey, this exists, let's stick it in, and then we'll have logs.
And the developers were like,
**Hannah Ramadan** 14:31 I don't know.
**Wendy Smoak** 14:32 So, yeah, we pulled it back out, and I need to go… I need to get that, you know, set up a simple example with Puma and whatever they're doing.
**Hannah Ramadan** 14:41 Yeah, that's.
**Wendy Smoak** 14:42 and see, because I did not expect that.
But the ones I work on are passengers, so it's, forking processes, and Puma's threads.
So… I think… not something I've done complicated work in yet with Puma and Rails, so I'm… I'll be interested to see.
What's going on, but, just stay… Miner mentioned that it's got Something.
Yeah. I don't know yet.
**Hannah Ramadan** 15:12 Yeah, I feel like that, Yeah, maybe that could be something interesting, like, issue to open. I feel like Kayla might be also intrigued by that one.
**Wendy Smoak** 15:21 Yeah, I want to see it happen. I've only got.
**Hannah Ramadan** 15:23 Yeah.
**Wendy Smoak** 15:23 I've got… they pasted the error, and it's like, yep, that's the SDK code. I remember looking at that code, where it sets a mutex and then checks the thread local variable and, you know, does the thing.
But… somehow, it got itself into a situation. I will see if I can… Strip that project down, or, like, basically start from nothing and build up enough of what they're doing to make it happen.
**Hannah Ramadan** 15:49 Nice.
**Wendy Smoak** 15:50 I hope it's reproducible!
**Hannah Ramadan** 15:52 We have to keep really hard to do it much if there's not everything.
**Wendy Smoak** 15:55 Yeah, I haven't… it's not… it's on my list to do, but it's not gonna be fun.
Fair enough.
**Hannah Ramadan** 16:02 That doesn't sound very fun, I agree. Maybe Claude can do something for you.
**Wendy Smoak** 16:07 Yeah, I will, I will ask it, like, set up a project with Puma and… I've had some luck with workspaces, like, multiple projects open at once.
So I can see all of the… like, I'll open the SDK and… my project, or… like, I opened the Python… OpenTelemetry Python and OpenTelemetry Ruby.
And told it, go look at what they did, and then tell me how you would do it in the Ruby project.
**Hannah Ramadan** 16:33 Wow, okay.
**Wendy Smoak** 16:34 Yeah, it could… it did, yeah, it's… it's… I've got a branch with…
**Hannah Ramadan** 16:39 the internal metrics.
**Wendy Smoak** 16:41 I like that one.
Because, I mean, I went and looked at the code, but… It would take me longer to think about what they did and how to convert it, so that's why we.
**Hannah Ramadan** 16:49 Yeah, Laura.
**Wendy Smoak** 16:50 That's where we have our little AI friends now, so…
**Hannah Ramadan** 16:53 Yeah, I did the same thing with, I… I think, like, some .NET code on the hotel side, and it… Khan told me what to do in Ruby, and I was like, okay, cool. Saved me a lot of hours trying to figure.
**Wendy Smoak** 17:06 Yeah.
**Hannah Ramadan** 17:06 Read other code?
**Wendy Smoak** 17:08 I was playing with Weaver over the weekend, and basically opened it up and tried the examples, and then it doesn't have support for logs, of course, because logs are always a third-class citizen around here.
So I told Claude to go make it work for logs, and it did. So now I have Rust code that works, that I… I have never written a line of Rust in my life. So it's like, I can't contribute.
I don't even know if it's right. I know it's working.
**Hannah Ramadan** 17:32 That is the hard part, I've definitely…
**Wendy Smoak** 17:34 I have to go now learn enough Rust to, like, be able to at least say intelligent things about this code.
And then see if they want it, but… Probably someone else will beat me to it. All right, I guess we will make it short.
**Hannah Ramadan** 17:47 Yeah, I think we're ready to go.
**Wendy Smoak** 17:49 Thank you!
**Hannah Ramadan** 17:50 See you next time!
**Wendy Smoak** 17:51 Alright, bye.
