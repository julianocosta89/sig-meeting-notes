SIG: Swift SIG
Date: 2025-10-02
Duration: 25 minutes
============================================================

## Zoom Recording Transcript

**Bryce Buchanan** 01:15 Hmm… In a nutshell.
**nacho** 01:55 Hello?
**Bryce Buchanan** 01:57 How's it going?
**nacho** 02:00 Fine. Yeah, fine.
**Bryce Buchanan** 02:08 I'm gonna delete this semantic convention thing. It doesn't… Doesn't go anywhere.
**nacho** 02:33 Remove the links also in the top.
**Bryce Buchanan** 02:37 There was just the one.
And it was broken.
**nacho** 02:41 Already?
**Bryce Buchanan** 02:45 I just… I looked through the, the document history, and… It's just been that one link for… For quite a while.
I mean, maybe it only went back to July. Let me go a little bit further back.
**nacho** 03:04 I… I am… I am seeing a different thing than you, I think.
**Bryce Buchanan** 03:09 Yeah.
**nacho** 03:11 I am seeing… I am seeing the GitHub repository there, the Slack channel also.
**Bryce Buchanan** 03:18 Oh, interesting, I wonder why they went away.
**nacho** 03:22 And I'm seeing here, and I'm… Grundy.
**Bryce Buchanan** 03:26 When did they get removed?
**nacho** 03:28 That's not why I missed it seeing them.
**Bryce Buchanan** 03:31 That's weird.
**nacho** 03:34 Maybe you have that in some kind of editing version without the headers, maybe it's in the headers.
**Bryce Buchanan** 03:40 Oh, maybe that's it, yeah.
Boop-a-doo.
Hmm.
That's weird.
**nacho** 03:55 Yeah, who knows how it's… Who will not work?
**Bryce Buchanan** 04:15 I don't know.
That's weird. Okay.
**nacho** 04:36 Yeah, definitely is a header, yeah, checked in my… about in May.
laptop, I don't know why you are not showing them, but yeah.
**Bryce Buchanan** 04:44 Yeah, I don't know.
I don't know Okie dokie. Why don't we get started?
So, topics from last week.
timeline for this issue here, which I think is a metrics filter.
Vinod, have you made any progress on this one?
**Vinod Vydier** 06:11 Yeah, I did look at it. Actually, I wanted to… ask if, should I follow a pattern? Is there a right place that I can… look at.
**Bryce Buchanan** 06:25 Yeah, I think that the Java instrumentation looks very similar to ours, so I would take a look at that for inspiration.
**Vinod Vydier** 06:36 Okay.
**Bryce Buchanan** 06:37 Yeah.
**Vinod Vydier** 06:39 And…
**Bryce Buchanan** 06:41 Cool, okay.
Groovy.
Let's see here, so the next one is document the release behavior. I've made some notes on it, it's actually pretty straightforward. I'm wondering where I should put it. Should I put it into the README, or in Contributing, or… a separate… location altogether.
Maybe, like, a, a dev folder, dev documentation?
Any, any thoughts, suggestions?
**nacho** 07:18 Yeah, I think maybe… It should be in the readme of each of them, so…
**Bryce Buchanan** 07:26 Okay.
**nacho** 07:28 So, yeah, if you get to one or the other.
You get the reference to the…
**Bryce Buchanan** 07:34 Yum, yum.
**Vinod Vydier** 07:36 Yeah, I think the docks are preferably behind, it still has, like, single repo, kind of…
**Bryce Buchanan** 07:41 stuff in there, right? We need…
**Vinod Vydier** 07:43 We need to make those modifications, yeah.
**Bryce Buchanan** 07:46 Yeah, so from my, just running the release and stuff, it does seem that, you know, I can… if I have my Swift core in my project set to, like, a from.
it'll pull the latest version of SwiftCore, and it'll pull the latest of Swift, and it doesn't really matter what SwiftCore is in the main repo, it'll pull the latest of SwiftCore in my project, so that's nice.
So it's not, like… I don't think that we need to be, like, really on top of… making sure that the version in the main Swift is matching the version of Core, other than just for testing purposes, and making sure that that is, working properly. So we still need to do nightly builds.
For… for this, though, I think.
Does anybody want to look into that?
**nacho** 08:59 I can take a look, yeah.
**Bryce Buchanan** 09:00 No, thanks, Nacho.
Cool, okay, so I still will add that to the README.
This still needs to get reviewed.
Looks like we got a couple of… I just haven't had a chance to look at it. I've been busy this past week. If you're just waiting for me to approve this.
If everybody else thinks it looks good, then, we can just go ahead and merge in.
I trust y'all.
**nacho** 09:42 Yeah, the only thing was that there was a comment that said that Oh, that… The tests were leaking the… Indirect… the last comment? Someone…
**Martin Holman** 09:55 Yeah, we talked about that last time.
And it was about the transit disease.
**Bryce Buchanan** 10:05 Oh, okay.
**Martin Holman** 10:08 Yeah, and I think… so we talked about it, like, there is still some usages of NEO in… The taste package?
But rather than just try and stamp them all out, like, this gets us further to where we are.
Chip away at us tomorrow.
**Bryce Buchanan** 10:23 Okay.
Yeah, I mean, there might be nothing to do at this point if, you know, the… yeah, the transitive dependencies are bringing it in. I think that… I think that, this was kind of like two parallel conversations we were having, because it's like, oh, you know, the gRPC stuff pulls in NEO no matter what.
And so there's really… since this is the… the, main repo, there's not a lot we can do about that.
Okay.
**nacho** 10:58 Yeah, I think we can… also mess this and continue the work on removing. I mean, this… this PR works, it doesn't cover all everything, but it's an advance, so I think we could… We could just, yeah.
**Bryce Buchanan** 11:14 Yeah, I'll.
**nacho** 11:14 Land and, and, and continue.
**Bryce Buchanan** 11:23 Okay, so… Yeah, so just… this is kind of the same thing as my release, Investigation, but yeah, it seems like… the… the Resolve, It, doesn't seem to matter, except for… What… if you're working on the project locally, And so, I don't know, like… it's kind of like, one or the other. It's just an extra dependency. I don't know if we should bother removing it or not.
Like, what do y'all think? I think that… I think that we should probably remove it.
**nacho** 12:10 Yeah, I think the final user can fix that, right? But… I don't know if that could end up with… Incompatible versions if they don't select properly.
**Bryce Buchanan** 12:22 Well… I think that, the ones that we have pinned to an exact version are always going to be pinned to those exact… I think it just comes down to if we are diligent in which dependencies we are allowing to update.
And so, when they get new updates, and we build, and something's broken, That'll be a problem.
But, I think that… let's see… I think that there's really only… there's only these Swift… Like, the Apple dependencies.
Yeah, that are using FROM.
And our core dependency that we're using from And again, this is only going to affect, development locally. So if you have… if you're using this as, if you're using this as a dependency, it's not going to respect the package resolve that this repo sets. It's going to be respecting the package resolve that your project sets.
So, it'll still be pulling these froms in that.
**nacho** 13:43 Okay.
**Bryce Buchanan** 13:44 main repo. So, I think that… that this… Kind of… yeah, we think that it provides some sort of security, but it doesn't really in terms of when people are actually using this project.
Any other… if anybody else disagrees, then just, yeah, let me know, and we can not do that.
Alright. So be it.
**nacho** 14:15 Yep.
**Bryce Buchanan** 14:20 Alright, cool. Any new topics?
Okay.
Should we take a look at some… some open issues, see where we're at?
This looks like a new one that just got opened today.
So, crash on iOS using URL instrumentation cannot set task delegate after resumption.
That's interesting.
presumption.
I believe this looks like it may be related to, trying to It looks like there's a race condition between a network request and the instrumentation occurring.
So I wonder if they have some… If there's, like, You know, some network request that's getting sent off while it's being instrumented.
I can reply to that. I don't want to do that with everybody here.
**Martin Holman** 15:56 Are they configuring it?
During the request? Because the code sample is configuring the URL session instrumentation.
**Bryce Buchanan** 16:04 Yeah, yeah, it's not… it's not a lot… there's not enough context here. I just am… I'm seeing this message here, so that… That speaks to me that there's some request Some object, you know, like task object, task delegate object, that is resumed, like, they call resume on it.
And so it's making a request, but then we're also trying to, like, swizzle it at the same time.
**nacho** 16:31 I think the clue is there when it says, SwiftUI app using .task on a view.
**Bryce Buchanan** 16:41 Oh, interesting.
**nacho** 16:43 Yeah, that… It means that whenever the… View is shown.
It starts what's in the task, and probably that's what is in the… Desk.
Sorry, what's in the view. So… .
**Martin Holman** 16:59 Oh, configuring…
**nacho** 17:00 Excuse me.
**Martin Holman** 17:00 is in the task, or sending the request is in the task.
**nacho** 17:03 I think the request is in the task of debut, where he… probably, he wants to… Start something to load something from the network to load in a view?
With that task, and maybe it's crossing.
**Bryce Buchanan** 17:20 Yeah, everyone.
**nacho** 17:21 Would it be great if they provided a sample.
**Bryce Buchanan** 17:24 Yeah. The more simple app.
**nacho** 17:26 Our more simple, yeah, something that we can reproduce locally, so we can really inspect.
depth.
Yeah, maybe it's running in a fancy way.
inside the view task, and it's doing, I mean, like.
Yeah, it says, cannot set task delegate after resume? Maybe the system is compiling that as a session that's resumed later, or something like that?
Yeah, who knows the magic of Sweep UI?
**Bryce Buchanan** 17:53 Yeah, yeah. Yeah, that's an interesting… yeah, I can, follow up on that.
**nacho** 17:59 Maybe, yeah, maybe we should… yeah, I don't know if we… For other similar situations, we are not allowing Instrumentation on them, but yeah, for this situation, probably… I could expect that some views just load things from the web when they load, and maybe some lazy loading, something like that, is what they are trying to do, and that should be a more or less usual scenario. So yeah, we should try to fix that, if we have something that can reproduce, yeah.
**Bryce Buchanan** 18:29 Totally.
Allow custom persistent performance presets. So, Yeah, this is just, something that should be done.
I think, yeah, those presets are just hard-coded, and we didn't make them, like, editable, so… Yeah, I think that this is a good… a good improvement.
Let's add a label to this.
enhancement. So, I think that this would be a pretty easy one, if anybody wants to, you know, add a little, add a little to the repo. It's just essentially just, like.
make the initializer non-internal, and that should… should do it. Allow people to… to, add more of those?
App crash in test flight.
They got a crash here?
Watchdog times out.
Dare I open a random zip from the internet?
If I disconnect on the wine.
**nacho** 20:09 Yeah, the only reason for a watchdog there, maybe it's.
**Bryce Buchanan** 20:12 Yes.
**nacho** 20:13 Trying to Swizzle network classes, if it's a really big application, the… and URL session instrumentation tries to dynamic… dynamically Find networks… sorry, network classes, and so it itreats all the classes, maybe, that if it's a really big Code, that could happen.
But yeah, I don't know.
**Bryce Buchanan** 20:44 Yeah. I mean, it's just a… it's taking too long to start up. Yeah, I wonder if it's a swizzling thing, like, there's… they're too… There's too many classes to swizzle, is that what you're saying, Nacho? I know you can't see it, but it's a useless crash because it's all obfuscated, it's all just…
**nacho** 21:15 Yeah, but that was just 3 weeks ago, I don't know.
**Bryce Buchanan** 21:17 Yum.
Let's see if… There is… we do have a, Like, it's probably the URL instrumentation, right?
**nacho** 21:37 It's the only thing I can think that Can take a long time.
When loading?
I think we also have a… way… To only set the classes you want to instrument, something like that?
**Bryce Buchanan** 21:59 Yeah, yeah, exactly, that's what I was thinking.
**nacho** 22:02 So that could… help here.
**Bryce Buchanan** 22:25 And I think that… Is…
**nacho** 22:32 Yeah, I have asked in that thread about that sample today.
Class Switzerland, we see.
**Bryce Buchanan** 22:42 Should instrument… Or is it… is it in the configuration?
**nacho** 22:49 Yeah, maybe it's too new enforced.
**Bryce Buchanan** 22:56 Delegate classes to instrument.
**nacho** 22:58 Yeah, that's… yeah, it's not in the…
**Bryce Buchanan** 23:17 Let's see, okay. Crashing OS log, is this the, yeah, that's this one.
Did this not get merged?
Interesting. So, date again.
**nacho** 23:38 No, yeah, I… Yeah, I updated the branch.
**Bryce Buchanan** 23:44 I've never worked before, that's fine, too.
There we go, okay.
Alright, well… I think that… Supporting new attribute types… Oh yeah, I haven't had a chance to take a look at this.
We're getting started… I don't even remember making this issue.
Yeah, it looks like there's a couple of, you know, just tasks that need to get done in here. If anybody's interested in contributing, just take a look.
I'll try to grab one myself when I have some time, it's just been busy over here with… non… Hotel stuff, so… I haven't had a chance.
If there's, is there anything else that, anybody would like to discuss?
Huh?
Alright, I guess we can have another short meeting this week.
Alright, have a great rest of your week, and have a nice weekend.
**Martin Holman** 25:32 Thanks, Jolene.
**nacho** 25:33 Nice weekend.
