SIG: Arrow SIG
Date: 2025-07-10
Duration: 33 minutes
============================================================

## Zoom Recording Transcript

**jmacdonald** 04:14 I'm having trouble with my audio.
But maybe you heard me.
**Drew Relmas** 04:22 And I.
There we are.
**jmacdonald** 04:23 Oh, good! Always takes me like a minute.
Good morning, everybody. I know there are many people on vacation. I'm gonna present some notes that we have meeting notes, and we'll go from there.
There is an agenda item list. It's pretty empty right now.
Let me share alright. Well, here we are. Can you see? No, God.
I just don't like this software.
Aha! Now you can see my screen.
Okay, thanks for joining everybody we're recording. You can write your name if you feel like it.
I know that.
Well, a bunch of us are from the same company here, Tristan, you're the you're the you're the guest here. Maybe you'd like to speak first.st Welcome, Hi, Tristan. Anything to talk about on the agenda.
**tristan** 05:46 On the agenda. No, I'm just mostly here to listen and try to keep up to date. July fair, able to contribute.
**jmacdonald** 05:55 Love it all right. Well, So I can tell you what I know about the state of the project quickly. Before we go to the agenda.
so, Lawrence, on vacation. He'll be back next week. 2 we've got sort of 2 people working with Laurent closely and rust on his side neither of them are here but there. So there's 1 vacationer as well.
It's moving pretty well. I'm pretty pleased. So we are real close to standing up a collector. Let's put it that way. A rust, a rust pipeline, not a standalone collector and the the 1st item on the agenda is for me to share the planning. I've been doing to bring the 2 collector code bases together while the the collector code base with the new otop data data flow pipeline. I'm trying to avoid saying that we're building collector so with that, I will jump right in. I am so I've been working with some of my colleagues to try and make a plan here. It took a long time, and it's not quite, quite ready for me to share with the collector, Sig, but I'm gonna share it here.
this let that. We did a lot of investigation into the capabilities of the go runtime. Go plugins go shared, libraries go being called through. Ffi rust being called through Ffi rust being called through shared libraries, rust being called from go and go being called from rest, we did a lot of research.
This is the proposal that we came to after discovering many of the limitations in in both of those both runtime environments have a lot of limitations. Neither is very stable as far as like packaging binaries, and so on. But so I presented this document, and it has a a proposal in phases.
I want to get some feedback from people in the group.
and so I'll just walk through it.
Just in case people are reading this or listening to the recording as well.
So, as you may know, I'm pretty familiar with the code collector code base. That's that's an advantage here. So I've been given pretty specific description of how I will change the go go collector code base to meet the rest. Code base in 7 phases. This the the 1st step is to fix the builder so that you can create a cargo library and link it to your go. We're gonna then we're gonna do configuration. Then we're going to do which, you know, like Json Strings being passed back and forth over Ffi.
Next we do the life cycle starting and stopping a component. This is where we start to use this library that I've decided would be best for us, called rust to go. It's a byteance product. It's been. It's proven, and it looks pretty good to me. So that's my leading proposal right now.
Once we get the lifecycle being able to start and stop these components in rust or go. We will then link the pipeline up with consumers and consumer interfaces. That would be the. This is probably the biggest step. This is the step where the 2 pieces of code come together. So at this point we're starting to link the the Otap data, flow engine with the go collector leaving, of course, some details like timeouts and cancellations, and all the other things that we do with contacts passing metadata forward and passing errors backwards. All those things are gonna be are, in my design for phase 5.
This is where it gets interesting phase 6. The idea is that now we want to try and make these fall back to when you can't build plugins or can't build foreign function calls. So one of the big limitations of go plugins, for example, is windows, doesn't work and we can imagine some other environments where you just can't build this type of complex environment. Maybe you just need pure go, for one thing. So the idea here is in phase 6 to create a fallback. This is where we just partition. The Service graph, when I mean by that, is that we're going to take one collector configuration, turn it into 2 parts and use Otlp exporters and receivers to bridge between them, so that you can start a sub process collector and have it look like one collector, even though it's talking between itself with a a sub collector, a child collector.
and this is to work around all the reasons why someone might not be able to build such a complex environment with foreign function calls, and so on. And this is the last step. Now, the dream for many of us, and my employer included, is that we are then able to move away from a monolithic build.
from from static libraries into shared libraries. So the 1st 1st thing we did was make a fallback. Now we're going to try and make it so you can actually load plugins, which is only going to work on some platforms, is going to be a little bit trickier, but it's something that we have as requirement, and we're trying to get done. So I spelled out how I would do that. There's a lot of docker involved trying to make a reproducible build environment, because the hardest part here is making sure that you have exactly matching compilers exactly matching compiler flags, exactly matching dependencies, all those things. And so, anyway, this is the plan. It's gonna be it's a big one. And I wanted to lay it out. So now I have.
and I'll stop. I don't know. Many of you haven't seen this yet. Many of you are my coworkers, and we'll see it, and we can talk about it inside the company as well. But there it is. I will stop talking now about my plan.
**tristan** 11:43 Plugins, my.
**jmacdonald** 11:46 Yep.
**tristan** 11:46 Interpretation of that. The go documentation you showed before was that these were limitations they would be removing eventually.
**jmacdonald** 11:57 I don't know about that. They do.
**tristan** 12:00 Oh, really.
**jmacdonald** 12:01 Completely.
there! There seems to be like no love for the Plugin interface, even though the Go team created it. They immediately began, not wanting it to exist.
so there is like compatibility. Guarantee the 1 point X like they're gonna keep it. They just don't want to fix it. And what what this plan here is doing is saying, the go team has gone out of their way to tell you how many ways this can fail.
And we're going to look at every way. This can fail and try and make it work. That's what we're going to do.
**tristan** 12:36 Okay.
**jmacdonald** 12:41 Yeah. So this is the 1st time I've shared it. It really isn't much here for this team, this group to look at or pick apart. I think the collector Sig, is gonna savage. This document. We'll see what we'll see what happens.
but this is at least the the plan that we were able to come to after lots and lots of research. So at least it's out now. And I what am I asking for. I'm asking for any anyone with strong opinions or wants to preview it. Eager to see this definitely. Go, read it. I'm probably going to like, let it sit, for I'm going on a vacation myself. Next week.
When I come back I'll be ready to face the the collector, and also, anyway, I will publish this for the collector, Sig. In a week and a half or so.
**tristan** 13:27 I'm gonna go to that Sig meeting.
**jmacdonald** 13:29 Well, sure, sure you are. I'm also okay. Yeah. See you there.
**tristan** 13:36 Very eventful, I'm sure.
**jmacdonald** 13:39 I'll have to check which meeting happens the week after we can look at that right now.
I'm out next week.
Oh, yeah, it's a Wednesday, North America. It's 9 o'clock right there. It'd be exciting. Those are the biggest ones yeah. Count on that Wednesday, July 23.rd anyway, that's what I have and what I've been working on for a while. I've got other stuff in flight with the go collector just continuing to build trust there in that group and make sure that they like what we're doing. And they like us. So if anyone cares to talk about rate limiters and the go collector. I'm I'm an expert on that. But I don't think it's the topic for this group.
I think we should move on unless anyone really really wants to talk about plugins.
cause I know Drew has some stuff, and it'd be good to talk about those topics, Drew. We haven't had. You talk of the meeting for a while.
**Drew Relmas** 14:35 Yeah, oh, maybe I can. There it is. There's the video, hey? Yeah, I actually have 2 pretty small topics. If you wanna open up that issue on the 1st one? I was actually hoping another one of our coworkers Gokhan could be here today, but I think he had something that prevented him. So I was gonna talk about it a little bit.
this is kind of a repo maintenance housekeeping. Item we were thinking about, just making sure our Cis are working the best that they are. If any of you have done development in the repo, you know everything is pretty fast. We don't. We're not taking a whole lot of time to do all of our, you know. Go builds or cargo builds but one interesting pattern did come up. If you scroll down a little bit.
if you've looked at the actions the workflows that we run in the repo. One question that's come up is cargo bench, because this has started to be the longest running job we have. And when I say longest running, you know. Relatively, it's not. It's like 10 or 11 min. So it's not a big problem. But there was this issue open, seeing like, Hey, is there any improved like optimizations we should be making in terms of our rust. Build? And I'm happy. We have Ukarsh on the call, because I know you're, you know, involved in the hotel rust. SDK, I'm curious. Do we think that cargo bench is actually something that should run at Ci time?
The reason, I say that is, today it runs, but we're not validating the results. We're not comparing against anything. It's just spitting out into the void and not being saved anywhere. I could see a path where it's very helpful. If it's actually a gate that we're evaluating to make sure there's no performance regression.
But in its current state. We're not doing that. So should Bench simply be. I don't know. A nightly job that runs that we can consult if needed. Does it need to be on the Pr level? I'm curious. If the Hotel Rust group has any. I idea on this, I actually should go look at your workflow itself, and see if you're even running a cargo bench every time.
**Utkarsh Umesan Pillai** 16:51 We are not in the rust. SDK, we don't run the benchmarks as far as the but we have considered it. But I think, yeah, we never just like got to actually doing that. But yeah, as you said, it's right. I mean right right now, if you just run it. Firstly, also, we need to ensure the if at all we're doing this.
The runners are like dedicated for running. Ci. If it's it's shared, then, anyway, those numbers will be suffering from a lot of noise.
So I to India, as with the current state, we still have some manual checking to do. I mean, if I if somebody really wants to check regression, they have to.
They have to like, go and look at that Crm, and see how how the numbers look. But I am okay. I mean, I feel, yeah, George, go ahead.
**jmacdonald** 17:48 Hi, yeah, I I wish cj, were here. Because I've seen some work in parallel in the repository. In so. So I saw something that Cj. Was doing where there's a label on the pull request called performance, and you have to select the label to make it run those benchmarks? Because that because we know it's expensive. But I this is not just for the like cargo bench level stuff, but like the tests that they're running the performance testing apparatus that they're building. So I know that they're considering how to do that.
And we do, of course, really do want to have benchmarks output something that we can like. Monitor. I don't think it needs to be done on every Pr.
Given the number of Prs that are just like minor minor dependencies not related to performance, and so on. That, that would be okay with me.
**Drew Relmas** 18:40 Okay, I think that's the next step is Go Khan. And I can talk with C. Joe and confirm like, Hey, we think whatever cargo bench is doing right now in the Ci. It could easily be covered like with this on demand performance testing that you're working on. And if that's the case. We'll just take out the cargo bench.
job entirely.
Okay, that's a that's fair.
**jmacdonald** 19:04 I think it it may be like.
does cargo check tell you that the build is at least functional, because I've I remember times when you could in go in go code bases like the the build validates that there's viable viable code in those benchmarks. But as soon as you run it, you realize that the benchmarks are crashing like they haven't been run in months, that that's something I've seen, and so we don't want that case like they have to run.
**Drew Relmas** 19:32 We're still, we're still obviously enforcing like testing code coverage. So we get that at least.
I don't know if that is the same thing as what you're talking about.
**jmacdonald** 19:43 I guess I mean benchmarks won't do. Benchmarks influence code coverage without running. I mean, they can't. Right?
Yeah.
just a minor issue. I it's nice to make sure they aren't broken, is all I was trying to say.
**Drew Relmas** 19:58 Easy to throw a.
**tristan** 20:00 Pretty easy to throw a weekly thing in there on Github actions, so you could have them run every week, every month.
**jmacdonald** 20:09 I mean, I think Nightly would be okay, too.
Well, I hope that helps
**Drew Relmas** 20:17 Does?
**jmacdonald** 20:19 But I otherwise, I take it this, the build cache would mildly improve our build times. I suppose.
**Drew Relmas** 20:25 If most of our jobs are a handful of minutes at most, we're not.
**jmacdonald** 20:30 Just just wait till you put more data fusion in there. We real slow.
**Drew Relmas** 20:33 That's true. That's a lot of crates to import.
yeah, at that case, there is actually. So what Gocon did research is, there's a built in like there's a cache job that Github itself offers. That I haven't looked into too much, but could potentially be useful there. I think someone from F. 5 had also mentioned ccache was linked to at some point as another thing we could look into. But for now it's, I think, a little bit overkill, for where we are.
if there's no other comment on that we can move on to my second thing, which is also very small.
**jmacdonald** 21:15 Sir.
**Drew Relmas** 21:17 This is.
**jmacdonald** 21:18 Repository. Health is important, true.
**Drew Relmas** 21:20 Sorry.
**jmacdonald** 21:21 I say, repository health isn't.
**Drew Relmas** 21:23 Oh, yes, yes, so this is about renovate, which is something we've been playing with. 1st off we've I've been trying to do a couple of logical groupings of dependency upgrades.
For example.
Josh, you're well aware we have a collect, a go collector build in our repo that is like generated code. And automated go module dependency updates don't play well with that because you have to make the you have to build again. So, for example, that's 1 thing I've grouped all together because it still does require some manual work. I've also grouped together, like all Github action updates, because those are relatively safe and can probably just be merged together. This one is for docker digest updates in the last month alone. We've gotten. I mean, I linked a bunch of them right there so many Prs, because these docker digests aren't pinned by semantic version renovate ends up setting a pr. Every time the hash changes.
**jmacdonald** 22:28 Oh!
**Drew Relmas** 22:29 So I'm proposing. Let's just do this once a month and update to the latest once a month. You can look at the renovate thing that's changing here. But the WI want to bring this up just to get approval on this, or see if people agree, and then otherwise, I know we also have a bunch of other rust freight updates that are actually like, non, they're breaking, I guess you would say meaning they might require minor code changes to actually be integrated. There's 1 out there for Tokyo. Prost.
Yeah, right there. 6, 9, 6. I'm just wondering like.
**jmacdonald** 23:12 It's been vaguely skeptical of these auto updaters for all the reasons you're giving me right. Now go ahead.
**Drew Relmas** 23:19 So sometimes sometimes it works fine, sometimes the Ci just passes and it's all good. Sometimes someone needs to go in, make a minor code tweak or something like that. So I'm curious, like.
I know you know, depend about has been something well used over. Github I know renovate is relatively recently arrow, I think, in some other hotel air hotel repositories as well like what should be.
What's a good way for us to handle this like I, I think it still provides value. But what do we do when it breaks.
**jmacdonald** 23:57 Well, I I know that Dependabot was worse. That's that all that's all I know. I think.
**Drew Relmas** 24:03 That's From my experience, too. That's what I've seen.
**jmacdonald** 24:06 What's so? What's strange to me now? I haven't thought about this much, but we we've run into troubles where we can't add the co-pilot, like the the actually intelligent agent, could fix this.
**Drew Relmas** 24:16 Yes, but renovate easy, Cla.
**jmacdonald** 24:20 Good at sending me bad Prs, and I don't like it. Maybe if we could combine them. But I know that we're having trouble with Cla. How did renovate get through the Cla? But copilot not get through? The Cla is.
**Drew Relmas** 24:30 That's a good question.
**jmacdonald** 24:31 Usually a rhetorical question.
**Drew Relmas** 24:33 My maybe rhetorical answer is, I think, renovate uses a constant email as its committer and has been allow listed at some point. But I think the main problem with the co-pilot is it? They have different accounts that use that are hard to fully allow. There, there's like the easy Cla issue that they're looking into. But anyway, like, it's gonna be something small like this, like just changing a method, a function name or something.
**jmacdonald** 25:09 Yeah.
**Drew Relmas** 25:10 There's also. And this this would also be a question for Laurent. But I know, like there's another one out there for survey Yaml, which is in Boberg. Our reference implementation. And my question is, should we? Just I? I can exclude those. I can stop Updates going to that because we're not doing active development there.
**jmacdonald** 25:31 I have 2 answers to this especially good that Laurent is not here. Sort of yamo is toxic, and, as far as I can tell, and and has been unmaintained. And Laurent.
**Drew Relmas** 25:45 So the update is.
**jmacdonald** 25:46 Important or not.
**Drew Relmas** 25:48 Date is to 0 point 9 dot. Oh, and it's marked as this is the terminal update.
**jmacdonald** 25:52 Yeah, I think what Laurent has done in the past is PIN it to 0 point 8 so that it wouldn't get the deprecation notice. But that's not really a solution, and I'm ready to give up on Yaml. It's just trouble from so many different angles. But What's I? I would propose that we need to stop Bobor from building. It's nice that we put it in the open source. It's nice that it's a document and a record. It's history at this point, and almost everything I that I think is a value there has been copied into OO tap data flow.
**Drew Relmas** 26:23 Sure.
**jmacdonald** 26:24 Or could be recovered from history by. So at this point, either we remove it, or we tell it not to build and say, this is archival code which could be trouble for either of those could be trouble for different reasons.
I think it might be cleaner. We've left it in the Repository for 3 or 4 months.
We've all had a chance to look at it. I think we could just move. Remove it at this point, leave an empty directory with a like with the old Readme file. And like a update saying, this was historical code. We committed it. We used it, we read it.
It's done now.
Yeah, that's what I would propose without Laurent here. It's easy for me to propose that.
**Drew Relmas** 27:02 Yeah, yeah, gotcha. So we can, we can talk about this briefly, once he's back from vacation.
But I think, like another opportunity is just in case, I mean, I'm I'm happy to mark some of these.
As like good. 1st issue almost, is a label we could use like if someone is new to the repository, wants to contribute like coming in fixing up a dependency update like is a good way to get get interested or make a contribution. But really, this is just, I guess the tax that we pay.
**jmacdonald** 27:43 Yeah, I guess I've always wondered why these tools open Prs when they're not green like.
It's like, what am I supposed to do? Like volunteer to help the tool.
In which case, like, yeah.
**Drew Relmas** 27:55 Commit, commit directly to their branch to.
**jmacdonald** 27:58 Well, I also, I mean, it's like, when I watch this problem in the collector for for years like it, like stands 0 chance of getting these changes correct, because, as you've pointed out, like the go, the the make rule that has to run, and, like these, cross module dependencies are impossible.
But having a tool that consistently opens Prs that are broken is not helping anybody, and that's that's my feeling.
Once in a while they're green. I'm not sure. Anyway, it sounds like Drew, like you have an idea about how to fix it.
**Drew Relmas** 28:33 Yeah, somewhat. It's wonderful at Github action updates, or like docker digest, because that's just everything follows sember. And people are careful about breaking changes, Yada. Yada. But If we don't have to, there's not a lot more I want to talk about this. It's just if anyone has ideas on ways to improve, renovate, usage, feel free to let me know.
**jmacdonald** 29:01 I don't.
**Drew Relmas** 29:03 All good.
**jmacdonald** 29:07 Well, cool repository health stuff check So, as I was saying, we're close to standing up a collector. That's what Laurent told me. I have a feel for that just by reviewing all the code, but I know that there are still some details being sorted out. What would I say, is our status.
The the Albert is on Pto right now. He was working on this view mechanism to do efficient translation between bytes and otap frames.
It's all coming together. We've got otlp receivers, exporters, otap receiver exporter. We've got arrow data manipulation. We've got translation between otlp and otap and some sort of asynchronous engine that Laurent is masterminding it's close to being a thing, and that's where I that's what I wanted to say.
I don't actually have any more agenda items. As I mentioned, I've been so focused on the Go side that I have lots to say about go collector and not a ton to say about rust other than things we've just discussed.
Does anybody here? I know, Matthias, you joined us. After I was saying, Tristan, you're the only non Microsoft employee. But now we have 2. Is there anything you would like to add to the agenda? I don't have much else to say.
Well, then, here's what I do have to say. Thank you for for joining us. We've reached the end. It's nice to have a short meeting. There will be another one next week. I won't be there, but I believe Laurent and Albert will both be back.
And then, as I put in the notes, there'd be an exciting and spicy proposal by me on the 23rd at the go, Collector Sig, where I'm going to 1st reveal this plan to do. Go and rust interop, so maybe maybe join me then, and then I'll see you 2 weeks in this same location here.
On the 24.th Thank you. All.
**Drew Relmas** 31:01 Buh-bye! Everyone.
**jmacdonald** 31:02 Bye.
