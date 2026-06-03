SIG: .NET SIG
Date: 2026-06-02
Duration: 19 minutes
============================================================

## Zoom Recording Transcript

**Martin Costello** 01:16 Hey, bud.
**Matthew Hensley / Grafana Labs** 01:21 Hello!
**Martin Costello** 01:22 physical.
**Matthew Hensley / Grafana Labs** 01:23 Yes.
Oh, I'm going okay.
So… Catching up on the news out of Build.
**Martin Costello** 01:36 Oh, I forgot that was today.
Anything good so far?
**Matthew Hensley / Grafana Labs** 01:43 Yeah, you know, the DGX Spark?
desktop NVIDIA released last year. They're, At least in a Surface version of it.
**Martin Costello** 01:58 Is it like that big, giant one, or is it like a laptop?
**Matthew Hensley / Grafana Labs** 02:03 They're doing both, actually. They're releasing, surface… Book Ultra.
That's roughly… has NVIDIA arms.
CPU in it, and it's roughly equivalent to a MacBook Pro, and then they're… but they're also releasing a desktop.
Has 128 gigs of unified RAM.
**Martin Costello** 02:26 The machine of the video card.
**Matthew Hensley / Grafana Labs** 02:28 Go the machine.
**Martin Costello** 02:29 Okay, just… I was… I was just wanting to check.
That's fine.
**Matthew Hensley / Grafana Labs** 02:33 It's both because it's unified, so it's, you know, GPU or CPU available.
That's fine.
Yeah, unfortunately, it'll probably be, like, 5 or 6 grand.
**Martin Costello** 02:51 Yeah, I'm not spending that on a computer.
**Matthew Hensley / Grafana Labs** 02:53 Yeah.
There's that, and then… Some, fun Windows updates coming.
So…
**Martin Costello** 03:02 I'll check that out after the meeting.
Hey, Zach Kujit? Hey, Julius.
**Zach Montoya** 03:11 Hello.
**Julius Koval** 03:12 You know, honey.
**Martin Costello** 03:19 Give it another 30 seconds to see if Alan comes. Raj has already said he can't make it today.
I think that's long enough to wait.
I don't know whether we'll be actually able to reach a conclusion on any of the, the items on the agendas. Oh, Alan is here. Hi, Alan.
**Alan West** 04:06 Ayy.
How are you?
**Martin Costello** 04:08 Not bad, thanks. I was in the middle of saying, I don't think we can do the agenda items with at least one other maintainer, and then…
**Alan West** 04:17 Sure.
Just taking a look.
**Martin Costello** 04:25 So, the first item is a PR that Steve opened.
A few weeks ago, about unvendoring… the environment variables, configuration stuff. I think we did talk about it previously.
But there's been no comments on the PR.
that Steve can say about it. Because I don't think Pierreta's against it. I'm not against it. It was just whether or not there was some hidden reason we shouldn't proceed with it or not.
**Alan West** 05:01 Alright, I remember I was talking about this. Yeah, the… the main concern, the reason why we didn't add it back in the day, just to kind of recap, I think, what we discussed before.
was… We were just trying to… not continue down the slippery slope of adding more and more dependencies to Microsoft extension packages.
And I guess, I suppose I could see the argument going like this, like, we add the environment variables one, so what would prevent us from adding, like, the JSON one, or XML one, or whatever other ones there are?
For this.
In the future.
All that to say, I don't… I don't think I have, like, a deep concern here.
So I'd be okay giving it a thumbs up, but I think I'd also want Raj's input as well.
So we should, we should definitely ping him on this PR.
I… I'm okay to approve this, I think.
**Martin Costello** 06:15 Okay, cool, yeah, if you could approve… I guess it doesn't build at the moment, because Steve's just waiting to get it moving. You just want to, like, do your virtual thumbs up on it, in whatever way, and then once we've got something from Raj, then Steve will know.
Definitively which way to go with it.
**Alan West** 06:37 Okay, yeah, that sounds good.
Yeah, especially if, if, like, bidder's okay with it. I know that… The instrumentation group was the… Was one of the consumers that was fighting all the… all the dependencies that we have, and so…
**Martin Costello** 06:57 Yeah, I think over the last year, there's been a bunch of changes that mean that it's… Less pro… less or not problematic for them anymore to put on yet another one.
**Zach Montoya** 07:11 I can confirm. Yeah, all I've changed have been to, minimize any issues from loading dependencies, so… I don't think we'll… there's really much pushback from that perspective.
**Alan West** 07:24 Okay, yeah, great.
**Martin Costello** 07:28 Cool. Thanks, Zach.
I'm gonna swap these two items around.
The next one, Raj brought this up, and I can't remember if we discussed it, Alan, and then you said, let's wait till Raj comes to the meeting or not, so if you did, I'm happy to just bump it again until next time Raj attends, which is about labels for prioritization.
**Alan West** 07:59 Yeah, yeah, I had suggested that we wait for Raj. He's the one that originally suggested the idea, and… Also, I guess this week sounds like it would be timely, since he said that he would be, devoting a fair amount of time to… to catching up on PR, so… Maybe it might be… maybe, maybe we could do it asynchronously, asynchronously over Slack or something like that.
**Martin Costello** 08:25 Yeah, we're cool.
**Alan West** 08:26 Wait until next week, one way or the other.
**Martin Costello** 08:28 I'll, I'll message about it in a bit, or tomorrow morning, rather.
About the labels, because yeah, it's like, they'd be… they'd be actually useful, but, we don't have them.
**Alan West** 08:42 Yeah, yeah.
**Martin Costello** 08:45 I mean…
**Alan West** 08:49 we could… I mean, just as a… just as an idea, I'm not… not necessarily, like, making… Like, a suggestion based off of, like, a strong opinion or something, but maybe you could just, Propose a couple labels, like… Low, medium, high kind of labels.
Priority labels, and then we could just… Rename them as we… discussed, I don't know, with Raj.
**Martin Costello** 09:20 Okay. Yeah, that seems reasonable. Yeah, I guess… what is a priority, and how are they relative to each other? It's probably something we could bike shed over for weeks.
**Alan West** 09:33 Yeah, totally.
Yeah, even if it was just one label, like a, like a… like… need eyes soon type of thing. If it was just… if it was just one… And then you kind of used it sparingly.
So that it just didn't get, you know, every PR got marked with it.
We could at least start there.
**Martin Costello** 09:56 Yeah, that makes sense.
Because, yeah, I think… The only thing I'd potentially push back on is having a low, because I feel it would just turn into a, don't look at it unless you've got nothing else to do in the whole world.
**Alan West** 10:11 Yeah, I think that makes sense. That's a good point, yeah. Yeah, maybe it is a good idea to just start with one label right now, so that we can kind of… As we catch up, you know, and some of the… some of the labeled ones begin to get merged, then new ones can get labeled, you know?
**Martin Costello** 10:30 Yep.
Another idea is… Maybe we could have a milestone… you could use a milestone?
Or maybe a project board, and then you could just, like, slap them on that instead.
that wouldn't necessarily give you high, medium, low. It would just give you a… don't look at the PR list, look at this list.
**Alan West** 10:56 Yeah, that would work well for, like, especially, like, the Prometheus work that you're… Doing to just kind of group, unless that's already in a milestone.
**Martin Costello** 11:04 It is in or… it is already in a milestone, but it's… it's, like, every… it's every possible sort of priority.
Rather than a… I'd like you to look at this one first, please.
**Alan West** 11:18 Yeah, yeah, yeah, I see, I see.
**Martin Costello** 11:20 Cool. I'll ever think about that, and I'll, I'll put a message in Slack tomorrow, and suggest something, so we can maybe try and get something sorted this week, rather than waiting until next week, at the earliest.
**Alan West** 11:32 Yeah, that makes sense. Cool, sounds good.
**Martin Costello** 11:36 And then the other thing I just… just a quick mention is, I've been chatting to CJO about, performance-related stuff, and there's an OTEP up at the moment about doing… benchmarking of the SDKs against fixed scenarios, so you can do something like, how long does it take to record a metric in any of the SDKs?
So that's one thing I'm looking at with him. That hasn't kicked off yet. And then the other thing, which is… related to, but not quite the same, that is something I want to start working on soon, is over the last month or so, particularly with the Prometheus stuff, and also with some of the security stuff we did, I've done a lot of running the benchmarks myself.
to check I'm not making things work.
And… it can get a bit time-consuming.
Because you can't really do anything else with your computer while it's running benchmarks, because you'll invalidate the results. So, something I'm interested in setting up is continuous benchmarking. So, like, once a day.
a set of benchmarks will run, and then the results will go somewhere that can be tracked over time. So then… Initial doing something is very performance sensitive.
And we know we're not doing a release the next day.
Then you've got something you can look at and sort of track over time and see if we're not regressing things or getting better.
And I've been pointed at some stuff that Jack did in the Java SDK, and some of the bits and pieces we've got for, like, some bare metal runners that we can use. So I've created an issue in the community repo to get the main repo allowed to use the bare metal runners, and then once that's done, that's something I'm gonna start experimenting with.
To see if that's something we can make part of our, like.
Don't want to say seedy, but, you know, sort of continuous improvement.
For the repo.
**Alan West** 13:48 Well, I didn't realize that the CNCF had access to Bare metal runners.
**Martin Costello** 13:54 I didn't either, because I asked a question, I think it was in the maintainer Slack channel, it was like, hey, do we have, like, an AWS account somewhere where we can spin stuff up?
And, someone was like, I don't think we do, but we do have these bare metal runners you could use.
So, that seems like a much lower friction starting point.
**Alan West** 14:15 Yeah, and I think that that's always the… historically, the things that I've read up on With respect to continuous benchmarking is that, like, cloud-based runners can often be They can, vary quite a bit from run to run, so it's… Often.
Not super useful, but bare metal.
Typically.
If it's a totally quiet machine, you know, and just running your thing, like, it can be more meaningful.
So, that's cool.
**Martin Costello** 14:50 Yeah, so, like, there's… we won't be able to run everything, because from experience trying to run lots of our benchmarks on my own laptop, it takes hours.
So I think once there's, like, a proof of concept set up, then separately we can come up with a, like, what are the, like, quote, quote-unquote golden metrics that we want to track, like a spread of… Different things that we're interested in, and then we can track those continuously, and, like, we have to share the machine with all the other projects, so that also constrains how often and the time, but we could do something like run a subset, like, every weekday.
Assuming it takes, like, up to an hour or something like that, and then we can just have numbers that we can track over time.
**Alan West** 15:38 And how would the sharing work? Is it, like, we… would we get a dedicated.
**Martin Costello** 15:43 So…
**Alan West** 15:44 building.
**Martin Costello** 15:45 So, I believe that how it would work is you would set a schedule on the workflow.
And then the GitHub Actions runner synchronizes itself, so it only gets one job at a time.
So it'd, like, say, kick off at 3am UTC, But if the runner was busy, it would just queue until it was free.
And then as soon as its slot comes up, then it would run. So it wouldn't be guaranteed to run at a certain time.
And if it was always queued, we could move the time around so it wasn't… But I think… There's low enough adoption of it at the moment, but if we picked a time that no one else is using, it would probably always run at the same time.
**Alan West** 16:32 Gotcha.
It almost makes sense, like, if we're doing this across, like, across SDKs, it almost makes sense that maybe it's a dedicated project that has its, like, a single workflow that runs, and it just runs all the SDKs.
Kind of serially.
**Martin Costello** 16:49 So I think that's kind of the thing CJ wants to do.
But that's more of a release to users, release-to-release tracking, rather than, like.
But the extreme end, like, commit-to-commit tracking.
**Alan West** 17:07 Yeah, I see, I see.
**Martin Costello** 17:09 So yeah, so the thing… I want to set up for… our repo, and then maybe later for Contrip as well, for some of, like, the higher value relative term. Higher value instrumentations?
like, say, SQL Client or ASP.NET Core.
So we can track… Performance for those as well.
F.
**Alan West** 17:36 Yeah, that sounds great. That would be cool. I think we've kind of talked about this in the past a little bit, that, you know, nobody's really ever… picked it up, but I definitely think it would be valuable, so…
**Martin Costello** 17:49 Yeah, it's just sort of… I've done something like this before for a different project, but it was just, like, the last month or so, where I've just, like, been sat with my laptop on my knees watching the TV for, like, 90 minutes while it does before and after.
And so I'm like, there must be a better way.
**Alan West** 18:10 Hey, I mean, you're getting paid, right?
**Martin Costello** 18:12 It's true.
But, could be more efficient use of my time.
**Alan West** 18:21 Cool.
**Martin Costello** 18:23 So, that was everything that was on the agenda. Is there anything anyone else wants to add on?
**Alan West** 18:37 Not for my end.
**Martin Costello** 18:45 I think that's a long enough awkward silence that the answer's probably no from everyone.
**Alan West** 18:51 Yep.
Alright, y'all.
**Martin Costello** 18:54 Right, thanks for coming, everyone. See you next time.
**Alan West** 18:57 Talk to you soon!
**Zach Montoya** 18:58 Thanks.
