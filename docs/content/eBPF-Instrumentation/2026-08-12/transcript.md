SIG: eBPF Instrumentation
Date: 2026-08-12
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Tyler Yahn (Splunk)** 02:54 Hey.
**Giuseppe Ognibene** 02:59 Hi, Tyler.
**Tyler Yahn (Splunk)** 03:00 How's it going?
**Giuseppe Ognibene** 03:01 Good, how are you?
**Tyler Yahn (Splunk)** 03:03 Good. Yeah, good. Just starting the day. How about yourself? Yeah, I'm guessing you're finishing up, right?
**Giuseppe Ognibene** 03:09 Yeah, I'm finishing almost Well, what's…
**Tyler Yahn (Splunk)** 03:14 Yeah, yeah, fair enough.
**Matt** 03:55 Hello.
**Tyler Yahn (Splunk)** 03:59 How's it going?
**Giuseppe Ognibene** 04:00 Boop.
**Matt** 04:01 Pretty good. How about you?
**Tyler Yahn (Splunk)** 04:05 Good. I could use another coffee. But, yeah, it's every morning.
Yeah.
Yeah, yeah.
**Nikola Grcevski** 04:14 I see an espresso machine that Mattia has there, but I don't know.
**Tyler Yahn (Splunk)** 04:18 I was gonna say, I'm talking to an Italian, I'm pretty sure, like… Oh, this one?
**Nikola Grcevski** 04:21 Oh, yeah?
**Matt** 04:23 It's a bad one. It's not, it's not that good.
**Nikola Grcevski** 04:26 Sound good?
**Matt** 04:27 Yeah.
I'm waiting to buy a good one when I find an apartment.
So I don't have to move stuff around.
**Nikola Grcevski** 04:37 Oh, okay.
**Giuseppe Ognibene** 04:39 It's the coffee you're using is not good, not the machine.
**Matt** 04:43 Even the machine. It's not a real Lespresso machine.
**Nikola Grcevski** 04:48 Obviously, compare, you know, Italians, I want to hear, the… the old, like, mocha press, the one that you have, like, they… is it… is that better than espresso, or no?
**Matt** 05:01 No.
**Nikola Grcevski** 05:02 Yeah, no.
**Matt** 05:02 It's good for emergencies, but it's not a good espresso. It's not a real espresso.
**Nikola Grcevski** 05:08 When you go camping, you mean? That's what it is.
**Matt** 05:11 Yeah.
**Nikola Grcevski** 05:15 That's good.
**Giuseppe Ognibene** 05:16 It's good for making tiramisu.
**Marc Tudurí** 05:18 Okay.
**Tyler Yahn (Splunk)** 05:27 Cool. So it looks like we're actually about 3 minutes in. We can jump in here and get started. If you haven't yet, please go ahead and add your name to the attendees list.
If you have agenda items that you want to talk about, please go ahead and have them there as well, and yeah, let's start this off.
First off, Nicola, I don't know if this is, like, just.
**Nikola Grcevski** 05:48 Copy.
**Tyler Yahn (Splunk)** 05:49 from last week, I can't quite remember if we talked about this, but maybe not. So I just wanted to put it up there, it was in the next week agenda thing, exposing the config v2 outside of the internal packages.
**Nikola Grcevski** 05:58 Yeah, I mean, just to ask primarily you, if you have any… anything against of, exposing the… the config V2 stuff.
To be not internal.
So, and I'll explain, this is the issue we have with Bela, and so… we have some extensions to the config to support, you know, Grafana auth and whatnot, and what we currently have is just we have the OB config, which is, like, everything, and we just tack on a couple of other things, but we can… Reuse the config.
Yeah, I mean, it is…
**Tyler Yahn (Splunk)** 06:32 There's no reason I would stop that. The only thing was, is just, like, during development, I didn't want it public, because it was going to change a lot, but I… yeah, we're going… we're going live with it, so, yeah.
**Nikola Grcevski** 06:44 Yeah, I know, yeah. So, because we… like, we build every Monday, right? So we take all the latest, and we try to run it through our tests and whatever, and it's like, okay, so now we support ConfigV2, I'd like to… actually be able to support it in Vela.
And I think we can work out of the box, whatever you have. I just wanted to see, can I add this additional stuff in the same sort of way?
Or maybe create a separate Grafana-specific config at the end, and then chap it on.
Okay, so if you're not against, then I think that answers my question, and… Yeah.
Yeah, absolutely. Yeah, I can make PRs to open up some parts.
That…
**Tyler Yahn (Splunk)** 07:28 Absolutely.
**Nikola Grcevski** 07:29 Yeah. Okay, cool. Thanks.
**Tyler Yahn (Splunk)** 07:31 Yeah, cool.
Yeah, I'm excited about that. Yeah, I mean, I think that's actually a great use for it, I just, yeah, yeah.
Okay, moving on. I wanted to jump into the next milestone, release. So, I had planned this for being released on the 18th. I wanted to jump through the last three issues that we have, Open in the milestone.
And just see where we're at on these. Nimrod, I think these are all assigned to you, so I wanted to check in with you specifically on these.
**Nimrod Avni** 08:01 Yeah, I'm making progress with them, none of them's probably gonna be completely done by the 11th, but I think I just opened… a PR, maybe not on, Yeah, I think it… I think it just updated if you go below, like, I think I just correlated some PR to this one.
Yeah.
And that's, like… I just wanna… I started working on it, it became a really big PR, so I'm trying to split it. So, like, this is one, only the schema, and then I'll have one of, like, a tool that Ashley… calculates how much of the schema we're covering, and after that, some more, like, tests on making sure that, like, the schema completely matches our code, and we don't forget anything, like, we don't forget anything to put in the schema, and, like, all the… All the attributes of all the metrics are there, so… it's a bit of work, probably not gonna be finished until, I don't know when we are planning to release it.
**Tyler Yahn (Splunk)** 09:06 Next Wednesday is, is the planned release date, but…
**Nimrod Avni** 09:10 I'm hoping it will be there, but I'm not sure if we can commit to that.
**Tyler Yahn (Splunk)** 09:19 Well, yeah, I mean, that's also kind of what I wanted to ask you, is if, I don't think these are super critical to get done in this cycle, I just wanted to get them done to make sure we were getting progress, so I had added them originally. I think…
**Nimrod Avni** 09:31 I think they're not… for me, they're not, like, super… any of them are super critical until the, like, for, like, 1.0, because I think we're still, like.
we're not committing to not breaking anything, probably, until 1.0, so I think it makes sense to put them, like, at most there, but… I hope to get them done before. The same with, like, the… the publishing the schema, and… And I think this one and the, like, last one are probably correlated to, like… Getting full coverage and defining the schema are kind of the… Yeah, I think that that's… I think even, like, most of the sub-issues here are dumb, but… They're kind of in the same thing.
**Tyler Yahn (Splunk)** 10:19 Yeah, I just think that there's probably some more… We need to split off, probably, I'm guessing, but… I haven't taken a look at it, to be honest, so, yeah.
But yeah, I guess that comes back to my question, though, is like, if that's the case, like… I mean, can we commit to getting these done in the next milestone, and we just move those to those? That milestone?
**Nimrod Avni** 10:41 That makes sense.
**Tyler Yahn (Splunk)** 10:42 Let's, let's do that, because this next milestone, I guess we can kind of jump into this. Like, this is the one, like, I was hoping to have be, you know, the last one that's not an RC, essentially. And then… ideally, you know, we're talking end of September, maybe early October, we're getting out our RC at that point, which is… in line with getting this V1 ready for KubeCon, so, like, that was kind of my idea. So, yeah, this is, like.
the V12 was kind of the hard deadline to actually get this stable by KubeCon sort of thing, so I think we can bump to there, and then we can go for that.
**Nimrod Avni** 11:18 Yeah, I think it… definitely, if it's, like, end of September, I think there's definitely time. I think I already have, like, a draft for, publishing the schema. It's probably gonna be on our, like, GitHub instead of the full, like, the auto website, but we can, worst case, migrate to that.
**Tyler Yahn (Splunk)** 11:39 I think that that sounds fine.
Yeah, like we talked about last time.
**Nimrod Avni** 11:43 Yeah.
**Tyler Yahn (Splunk)** 11:43 And, like, I'm not… Like, these don't… I'd like to have these in by the V1, because it's the sign of a mature project, plus it also fixes all of our telemetry. Like, this telemetry has to be, like… I don't want to be doing that afterwards, but, like, publishing this kind of stuff, like… Yeah, it's not like… super critical, but it's definitely, like, helpful, to get this out. So… Yeah, I think that that's, like… really good goals, and I think… I think, like you're saying, I think we can accomplish it, so let's… let's try to target that.
**Nimrod Avni** 12:14 Yeah, I'm on it.
**Tyler Yahn (Splunk)** 12:16 Okay.
Okay, with that said then, there's nothing left in the… V011, which means we could bump this up. I did want to ask Nikola about this, exposing the config V2 outside of the internal package stuff, like, did you want to try to get this in really quick before next Wednesday, or are you okay with us just doing a V011 and then,
**Nikola Grcevski** 12:41 No, no, it's okay. No, you can wait.
Yeah, I'm… I mean, with Baylor, we don't actually… we just pick off main, so… Okay.
**Tyler Yahn (Splunk)** 12:51 Alright, alright.
**Nikola Grcevski** 12:52 Yeah. I mean, we're going Yolo, we're trying to test as much as we can. I mean, not all releases make it, so if there's bugs and we find things, we fix them in OB, and then we skip that release, but… Yeah.
**Tyler Yahn (Splunk)** 13:07 Yeah, I gotcha. Okay.
Okay, cool. Alright, if that's the case, then, I guess I can ask really quick, like, are there other things that people wanted to get in, if they were hoping to get into this next release, or should we start the release process and maybe get this next release out in the next day or two?
And get it out early.
**Nikola Grcevski** 13:29 There might be that one of those… I think we can get it early. I… I was just hoping that… there's one bug this community user opened up related to DMS, I think maybe we want to fix that, but I don't know how many people use the DNS, so… might not be the end of the world.
He found out we were using the wrong helper.
Don't make sense now that I look at the code, but it is what it is.
So it… Yeah, so he opened a PR.
**Tyler Yahn (Splunk)** 13:57 PR, okay.
**Nikola Grcevski** 13:57 We are, yeah.
**Tyler Yahn (Splunk)** 13:59 Oh, I think I saw this, yeah.
**Nikola Grcevski** 14:02 Yeah, he opened a couple of PRs, but the… there's one about… no, that's a separate user, but there's DNS.
Yeah, fixed DNS capture so PR endpoints get named correctly.
But… Do you have me, maybe, what?
What?
Yeah, it's using the wrong helper, we're doing read user, and it never finds anything, but the thing is, it doesn't fail, and it's so bizarre.
Oh, but this is the CLA issue. Okay, well, not forget. Yeah.
Okay. Yeah.
**Tyler Yahn (Splunk)** 14:47 That's annoying.
**Nikola Grcevski** 14:51 I mean, he's from AWS, so maybe he needs approval.
**Tyler Yahn (Splunk)** 14:54 100%, that's… After working with other AWS employees, that's definitely happening right now, yeah.
**Nikola Grcevski** 15:00 Yeah.
Well, if it… if it doesn't come back or it can't sign CLA, I would just take this and replicate it.
**Tyler Yahn (Splunk)** 15:07 I was gonna say, yeah… That seems fine. It'd be helpful if they could just open an issue.
Yeah. Yeah.
Hmm.
**Nikola Grcevski** 15:18 Okay, well, let's just wait. Then, we can skip this release. It's been broken like this for a bit, so it's not the only problem.
**Tyler Yahn (Splunk)** 15:24 Okay, yeah, sure. Yeah, I was looking at this as well, so… okay, hmm.
Okay, yeah, let's, let's skip that one then.
Anything else from anybody else that needs to get, like, open, something open they wanted eyes on, get it in beforehand?
**Nikola Grcevski** 15:41 I would say this Marc thing with fixing the INO number for the goal.
**Tyler Yahn (Splunk)** 15:47 Yeah, that's actually a good point, I did see that.
**Nikola Grcevski** 15:50 But I just had a talk with Mark. I think it's a simpler change, if possible, rather than this.
So… I would probably go with that. Yeah, because I think that… I think the dev… And I know numbers we get at… with OV user space match what the kernel sees, so… We could just use the one I think you added, or Mattia, I don't know, because I wasn't here. The first fix was adding dev in the… Not tracking the binaries.
**Tyler Yahn (Splunk)** 16:23 Yep.
**Nikola Grcevski** 16:24 So I can just reuse that, and… from… And then we don't need to do anything else. Will we find… when we look at the goal offsets from eBPF side matches what we see. I mean, I just ran an experiment with Mark on the test case he's got, and we printed it, and they match 100%, so…
**Marc Tudurí** 16:46 Yeah.
I can't change it now, so…
**Tyler Yahn (Splunk)** 16:52 Oh, okay, alright.
**Marc Tudurí** 16:54 That's the case.
**Tyler Yahn (Splunk)** 16:55 Should I add this to the milestone?
**Marc Tudurí** 16:57 Sun Marc.
**Tyler Yahn (Splunk)** 16:57 Do you think?
**Marc Tudurí** 16:58 Yeah.
Okay. When is the… when do you plan to release this? I missed that.
**Tyler Yahn (Splunk)** 17:03 The 18th, so next Wednesday.
**Nikola Grcevski** 17:06 Yeah, there's no better way to begin, yeah.
**Tyler Yahn (Splunk)** 17:09 Yeah.
**Matt** 17:09 So I have one question about that.
**Tyler Yahn (Splunk)** 17:11 Four working days, by the way. But yeah, sorry, go ahead.
**Matt** 17:14 about the device and, you know, the stuff. Just to make sure the probes are attached once, right? Or even if the device is different.
**Nikola Grcevski** 17:26 Yes.
Well, actually… That's a good question, because… Because if…
**Matt** 17:34 If we have touched them multiple times, I think there will be issues.
That's what we noticed with the gRPC test. That's the only test that touches the same image multiple times, and we have different device, but the same inode, and the U-Pro is attached multiple times, so it fires multiple times for the same binary.
**Nikola Grcevski** 17:59 That's gonna be a problem.
**Matt** 18:08 But the test is not failing right now, so I'm not sure it's attached multiple times. I just wanted to make sure we double-checked that.
**Tyler Yahn (Splunk)** 18:18 Wait, how does the U-Probe attach multiple times to a… A binary?
**Matt** 18:25 I thought it's like space, we track it as a different binary, because there is the file identity, which is now device and inode.
If we use the same image on the same node.
That will, will result in, like, two binaries, because, it's, two different containers.
But the underlying inode is, is the same, because it's the same binary.
I think, yes.
**Tyler Yahn (Splunk)** 18:56 Two different containers, okay.
**Matt** 18:57 products.
**Tyler Yahn (Splunk)** 18:58 I see.
**Nikola Grcevski** 19:01 Hmm.
**Tyler Yahn (Splunk)** 19:02 Yeah, that makes sense.
**Nikola Grcevski** 19:04 Well, that's… So this is just fixing the go offsets, what Mark's working on, but I think you're right. I don't know what that happens then.
**Marc Tudurí** 19:16 Nati, are you talking about the gRPC case again, or…
**Matt** 19:19 Yeah, yeah, because, that's the only test that, that exercised that, and Last time that failed, it was because, the U-propes were attached,
**Nikola Grcevski** 19:32 fourth time.
**Matt** 19:33 times to the same binary, and there were maps which were, were being, thank you.
There were overlaps between these calls, and the maps were getting scrambled.
**Marc Tudurí** 19:46 Okay. I mean, I'm changing it now, and I can try to run a gRPC test and see… If it works?
**Matt** 19:54 Maybe we can just, check out the branch, start obby, and see how many links we have with BPS tool link.
**Nikola Grcevski** 20:03 Yeah. Yeah. Yeah, I should do that.
Also, I think along the same lines, there is a bug, I just don't know exactly yet.
Where… But there was an earlier fix, I think was made by Steven, maybe Raphael, Related to… The cache of executables?
I mean, we run this in production, right, at Grafana, and somebody noticed that Grafana executable would crash.
With legal instruction.
MOS every blue moon, or whatever. But they tracked it down to this… this being on.
And it started happening after that change went in. The change was totally cool, because it was actually… we weren't clearing some cache.
Based on the inode. So if, you actually had an executable, and… and you replaced it with another one, and it reused the same inode.
it was like a three kind of… you have one executable, you replace it, and then you put a third one you replace, and then you kind of got the offsets and everything from the first that was there, and it was completely wrong, and it was crashing. So it required… somebody had, like.
Bespoke, like, executable replacement.
Yeah, that's the one. So we fixed it around May 30th, and that's when we actually… they noticed it, but they just opened an issue now and said, hey, we've been having these issues, and it's crashing once in a while.
And with this bizarre legal instructions, and they dug into it, and it's like, oh, you have this VP of Instrumentation thing. When did you guys add this? And we sort of like… but this is our way of testing, making sure that this actually is safe, and runs on scale. So… So, they just noticed it, just a while back, but, But yeah, so I'm thinking maybe it's related to what Mattia is saying, maybe they are shared, and previously we would have just picked up the same binary and given the offsets, but now maybe we're double patching.
And if you double patch, I wonder what happens.
**Matt** 22:24 Well, the prop just fires multiple times, and if we… if there are… if there is data which is not, indexed correctly in a map that gets overwritten with bad data and happens a lot of bad things.
**Nikola Grcevski** 22:38 Yeah, a lot of bad things happened, so… And then I don't know how to tell…
**Marc Tudurí** 22:47 Yeah.
**Nikola Grcevski** 22:51 Okay, that's interesting. Okay, well, I think we need to dig into more.
I think the user that opened the issue said that we were attaching to only one of their executables, so they weren't able… right, Marc? They weren't able to instrument all they wanted.
It was instrumenting one, or it was instrumenting all of them? What was that?
**Matt** 23:09 it was Instrumenting 1, and it happened that they noticed the spans for only this one instance, but I think in that case, it could have happened that There were, for example, four containers on the same node with the same image, and once you detach one, once the one container is deleted.
All of those 4s go, because there is, there is no ref counting.
The link should remain. I think that's what happened in that case.
**Nikola Grcevski** 23:42 I see, so maybe then… we should just keep the inert.
**Matt** 23:47 Yeah.
**Nikola Grcevski** 23:48 And don't worry about the device, but then do reference counting rather than dropping them.
**Matt** 23:52 Yeah, Tyler… Tyler actually added the ref counting, I think, because, there was one PR, I remember. I remember doing some work on this, and it was already in May, so…
**Nikola Grcevski** 24:04 But then he said it didn't work for him, or something, like, with the previous patch, so that's why Mark is working on the subsequent fix.
Huh.
**Tyler Yahn (Splunk)** 24:13 Yeah, the one I added was specifically for, like, the Go, importation of the Auto SDK stuff.
So, yeah, I think… yeah, I think, Mattia, you're a good point, like, that's a good point. Like, I think we could add that more universal… that's kind of what I thought Marc was looking into. I thought that was what he was happening to do, but I didn't.
**Matt** 24:30 Well, I still have the branch. I can, I can see what… what's different than… If that didn't work.
**Nikola Grcevski** 24:39 Yeah, he said it didn't work, whatever that patch that was made, Marc suggested it, and then the latest stuff from Marc does work, but I'm now wondering why does it work? Maybe because we do attach it four times, and then we do remove it.
If things go away, then we do remove it, but then there's still 3 probes running.
So it's doing reference counting the hard way, sort of like, it attached 3, and it…
**Matt** 25:05 I don't think we are attaching it 3 times in the Marx PR, because else the gRPC tests would fail.
**Nikola Grcevski** 25:12 Okay.
**Matt** 25:13 That test would fail, like, 100% of the times.
I see. Excellent.
**Nikola Grcevski** 25:19 Okay.
**Marc Tudurí** 25:21 But maybe.
**Nikola Grcevski** 25:21 what I'm making Marc do now will force him to… Because I've asked, like, why did you add the process IDs, right? Because with the PIDs… so, actually, initially, when I wrote the… the go offset changes so that we can run multiprocess. I use the PID.
Now, that's… that's actually not much easier to add than this sort of, like, inode. But then I was like.
But that's inefficient, because then I'm gonna have to keep offsetsMap for every pit, but maybe I have… 1 binary and 10 PIDs from it, so the really… the offices are tied to the binary, not to the PIDs.
And that's when I switched to inode numbers.
So I can keep less stuff in… In memory, or whatever.
So… But adding the pits is super easy. We can… if we… maybe that's the best way to do… go about this. We just scrap this and forget about the inode numbers.
for the go offsets and go to PIDMAP.
In that case… I'm it.
It's simpler.
On addPid, you just register the offsets, on remove pid, you nuke them, and…
**Tyler Yahn (Splunk)** 26:37 Well, you have to ref count, though, right?
**Nikola Grcevski** 26:42 No, I don't think we need to, because the PID… when the PID dies, when a PID gets added, we add the offsets to the map.
So, we can find it, and when a pit goes away, we just remove it.
**Tyler Yahn (Splunk)** 26:53 Oh, I see you're saying… you're not saying, like, deduplicate the offsets, you're saying, like, just add the offsets Rapid. Yeah.
**Nikola Grcevski** 26:58 it, and be done with it.
**Tyler Yahn (Splunk)** 27:07 Do you know what sort of, like, memory footprint that would incur?
**Nikola Grcevski** 27:13 Yeah, I mean…
**Tyler Yahn (Splunk)** 27:15 I mean, like, in the worst case scenario, I'm guessing maybe, like, kilobytes? Like, I don't… I don't know.
**Nikola Grcevski** 27:20 Yeah, it's not that big. I was just primarily kind of thinking Kubernetes, right? So people run multiple instance pods for the same service, right? They… to scale it up to 10, and in that case, it's really wasteful, right? Because it's the same binary, but… You scale it up 10 times, you pay the cost of keeping it all in memory 10 times.
**Tyler Yahn (Splunk)** 27:40 Yeah, yeah.
I mean, we can take a look.
**Nikola Grcevski** 27:44 Yeah, we take a look. I think we need to go deeper, Marc, to understand that if what I'm making you do now, or suggesting you should do, maybe adds these multi-probes.
And… because there's not gonna be PID maps anymore.
But your latest change doesn't have any PID maps.
After your PR feedback, so… Maybe it's not an issue. Let's take a look.
Damn.
**Tyler Yahn (Splunk)** 28:10 So going back to the milestone, this next release, did we still want to keep this as, something to get done, or did we want to plan on just investigating it and then get it out when we get it out?
The only thing is if we get it out and it's a fix, I guess if it's a… Grafana user, you guys are pulling main, so it's not as critical, right?
**Nikola Grcevski** 28:30 critical now.
It doesn't have to be exactly this release.
**Marc Tudurí** 28:34 Okay.
**Tyler Yahn (Splunk)** 28:39 Well, okay, if that's the case, I think I'd rather move that out of milestone 11, get it into the next milestone, and then we try to get this milestone released early this week, ideally.
And then, yeah, we can… we can follow up on that. Also, I would say maybe we can create an issue to track this bug.
Do we have an issue? Okay, sorry.
**Nikola Grcevski** 29:00 I… yeah.
Or is that the.
**Tyler Yahn (Splunk)** 29:01 One, I might have just opened it to… oh yeah, okay, yeah. Okay.
Yeah, okay. Then, if that's the case, let's, let's do that, let's, Let's move in that direction. Sorry, I'm just gonna move it out of the milestone.
Okay, with that, let me start sharing my screen again.
Steven, I think that you're the next agenda item.
Yeah, you wanted to talk about the GenAI OTL Performance Dashboard?
**Stephen Lang (Raintank, Inc. – Grafana Labs)** 29:36 Yeah, so this is a new project from Trask, which was just shared to me, and I thought I'd pass it on, because It's possibly relevant to, to Obi?
And the idea is to kind of show, like, a conformance matrix.
for the, the kind of different Gen AI, tooling that's… that's available.
Right now, it's just kind of like a traffic light system, is to… you know, you run the Weaver, and you check what it looks like, very similar to what we're doing now, except there's a UI around it, and… There's… it's not just Obi.
So there were some talks about how OB could be added in future. I did try and ask for clarification to see, is this something that would be expected of, you know, OB to contribute to to the repo that I linked, or is this something that we would somehow publish a report on our repo?
And the guidance isn't clear there… yet. It's so new, it's just kind of a heads up, this exists, brand new project has been born.
It seems to align with, all the Weaver stuff that we have.
And Obi?
There was some talk around… Potentially, instead of just having this traffic light, like, check, uncheck box.
Maybe it'd be useful to have, like, a version matrix.
So the idea would be when users are looking at upgrading, you know, their version of their library or their instrumentation from one version to another.
You know, would that also mean that they're moving from one version of the semantic conventions to another, and would that be, like, a breaking change?
So it's… It's very new, but it seems relevant, so I thought I'd share it here. I don't think there's a particular action To take from this right now.
It's just kind of heads up, and… Anybody's free to check out the repo and, You know, contribute earlier if they wish.
But I did say that I would keep an eye on the project, and if there are any specific actions for us, I can, I can shove it.
**Tyler Yahn (Splunk)** 31:48 Yeah, I think this is great.
They shared it as well in the spec meeting yesterday, and I think it's, like.
Pretty helpful. I think Obi should definitely, Try to support this, given all the hard work that… Nimrod and others have been doing on trying to get, like, our semantic convention conformance, as well as, like.
you know, Weaver integrated into this. I don't think it's actually too much further outside of it.
Yeah, I mean, I think it's kind of funny you say, like.
how does this, how do we start using it? I just kind of assume you just point AI at it, and then it, like, does it, because it's… most of this is just generated by AI.
I'm guessing it's just, like, a copy of it, is what Trask has been using. So, yeah, I would go that direction. But yeah, I think this is great. I think we should probably look into this as well.
**Nikola Grcevski** 32:38 Cool.
**Tyler Yahn (Splunk)** 32:41 Yeah, awesome.
Well, cool. Yeah, if there's no other comments on that, please take a look at it. I think it's really cool. I think also, like, right now it's Gen AI, but, like.
My goal has never been… to have it just be Gen AI, right? Like, it's always, let's have all the semantic conventions there, would be really awesome.
But that's, I think, a little bit further away. We're getting there, yeah.
Next up, Nikola, you wanna talk about, ways to inject headers generically for Lib SSL and SSL, right? Oh boy, this is gonna be good.
**Nikola Grcevski** 33:18 Yeah, I mean, I… I thought about it, and I think I found a way how we could potentially do this.
And this is what I'm thinking is… Rust, Python, Node, everything, where we currently cannot pass in the header, because it's encrypted.
So… The main issue is that… I mean, we can hook them with, u-probe, right, or into Lib SSLSSL write, but we cannot modify the buffer, that got passed to LibSSLRite, because presumably they've allocated a certain size, and we cannot extend it, we cannot, expand it, and whatnot.
But I thought that maybe I can actually do this with… User space.
patching. So, what I'm thinking of doing is… And I have a little prototype here that's working in a simpler form.
I can, I can share it, I can demo.
If you'd like to see what I… what actually… Yeah, absolutely.
**Tyler Yahn (Splunk)** 34:30 That'd be great.
**Nikola Grcevski** 34:32 This is not how I'm thinking of actually doing at the end of the day.
But, it should… Should actually… I wrote a little LD preload.
I don't know if you can see my screen.
**Tyler Yahn (Splunk)** 34:51 Yep.
**Nikola Grcevski** 34:52 But imagine, so, with LD preload, I can… override what the library called SSLRID is.
Like, for example, we have this Rust service that calls libSSL to do the encryption, because it's, you know, doing SSL. So technically, I would find the original function here.
I would… I can do whatever I want with it.
So, technically, if you think about here, there's a buffer past from the service.
That's been instrumented at a specific LEN.
So… If I can intercept this call, I can allocate here a new buffer, and I can… Prepare and do something, whatever I'd like with it.
and then passing the new buffer and the LEND to the… outgoing call. So, SSL has no idea that I've kind of come in here and injected something.
So, we would have to add parsing here. Is it HTTP, is it HTTP2? Where exactly we want to put in the same stuff we do in eBPFI.
One major challenge that I… Always had with this approach was… how do I communicate from the eBPF side the trace ID that needs to be in here.
Because this now runs as its own process.
It's not actually in Obi.
So, there is no BPF here at all.
However, what dawned on me is that what I can do is… Actually, just like I did in Java, call IOCTL here, With some magic.
number, which is… will be recognized by the eBPF Pro we have on IOCTL, which is what we use for Java, and passing the buffer.
And then the size and whatever, len.
And maybe a little bit of extra… Trace ID above.
So, what this would do is two things. First of all, it would replace the U-Probe we put on SSLRite, so then… we… because… And I'll explain why I need that.
this trace buffer We'll usePFProbeWrite User to fill it in with the trace ID when it hits the probe.
So, this will hit the probe.
We will write in here the trace ID. When this guy comes back here.
It says, oh, did somebody give me trace ID? Is it all be running? If they did, then I'm gonna do the extension and pass it in down to the original.
Does it make sense?
**Tyler Yahn (Splunk)** 37:41 So does this get run kind of like a… like, the Java agent?
**Nikola Grcevski** 37:46 Yes.
So, essentially, what I'd want to do is add tiny agents into LibSSL. So… and so the question is, like, how do you do this? Well, here I did LD preload, and you can kind of see it here if I… I might as well not switch it, but… So here I can LD preload my SSL rewrite around our typical Rust example. So if I do curl, you can see it's actually printing, so…
**Tyler Yahn (Splunk)** 38:15 Oh, cool.
**Nikola Grcevski** 38:15 I'm intercepting all the calls.
So we have the SSL pointer here, we have everything that we currently have as… stuff we track in OB. Now, this will only work on start. Like, if we took this approach, This will not work, because… The application needs to be started with this LD preload.
And maybe this works on Kubernetes, we inject init containers and whatnot, and, you know, the usual stuff.
But it's not ideal.
Because, first it kind of will conflict with the injector.
Maybe, because that, they preload, they use the same approach, the OTL injector.
**Tyler Yahn (Splunk)** 38:55 Yeah.
**Nikola Grcevski** 38:56 But, there's a library called Frida, which people use to do binary patching. And… So… I was… that's much, I mean, more work for me to kind of get started on that, which is why I wrote this LD preload, just to kind of… play with it and see if I can intercept it. But technically.
This will be binary patched by Frida, Without… on a running executable.
And so, free days use in production by many services, and I know a couple of companies that actually make heavy use of it.
So I think it's stable enough for us to try.
So technically, we find an application I need to instrument, we figure out that I have Lib SSL support.
we go in, and instead of putting a U-probe on it.
we binary patch it to call our handler, which wraps the lead SSL with the logic just explained. So, it replaces the lib SSL call with a trampoline, just like the Upro would, to our function that then in turn goes back and calls the original one after it has modified the buffer and everything.
Then with IOCTL, call our probe, and that fills in the information that it needs to complete the SSL.
outgoing.
**Tyler Yahn (Splunk)** 40:28 That's cool, I like that.
**Nikola Grcevski** 40:35 I think it's gonna be doable, but I have to prove it. I mean, I don't know. With this LG preload, it's definitely gonna work, but Frida, I've never actually tried to use it. I know just it exists, I know people use it. I've never actually tried it.
That… Yeah. The only kind of potential downside is that we're gonna have to… I mean, I think Frida's written in C, if I'm not mistaken.
So I don't know how we call that from Go. Maybe SeaGo, but then that opens a can of worms. Do we enable Sego?
Or, Do we have a tiny binary that we just, unpack, just like we do with Java agent that does all this patching?
Hmm.
That's gonna be a little bit of a hassle, but…
**Tyler Yahn (Splunk)** 41:24 Yeah, that was kind of my question, was, like, what Frito was written in, but I was doing a quick search, I saw some, like, Python wrappers as well, but again, it's kind of like, you'd have to shell out for that kind of stuff, so…
**Nikola Grcevski** 41:35 Yeah.
So, essentially, it's the same idea as the Java agent. This could be also… Another way to implement log correlation?
without hijacking, Maybe the… and nullifying the… the output and doing it from all the user space?
Because if you can reset the call to right.
To a specific file descriptor that we're interested in.
Then, you can wrap it here, you can say, oh, it's doing the log.
then we give it a trace ID, we pull the trace ID by this IOCTL, magic.
And then we just pretend to the stream and let the original go.
Pretty much, we can hijack any call this way.
If it works.
Just like we do with U-brobes, except that we can mutate what's happening.
**Matt** 42:38 So, does Frida work at runtime? So, you start Obi, and it modifies the…
**Nikola Grcevski** 42:45 app?
It… it actually does the same trick as u-probes, and essentially, it patches in the binary with a trampoline, at the beginning of the function.
The same way, which is why we need this IOCTL to pass the buffer to OB instead of the U-Probe. So if we do this, we cannot use the Uprobe, because I think there might be a conflict. One will override each other.
But… so if we use this approach, then this… we had… we will not put U-Probe on SSL, right?
But the IOCTL will ship as the buffer, just like we do it in Java, and we, in turn, will give it back the trace ID so you can actually attach it to the outgoing.
**Tyler Yahn (Splunk)** 43:30 Yeah, that sounds really awesome.
I kind of wish I'd, you already have it done. I'd love to review it Sure.
**Nikola Grcevski** 43:40 I mean, yeah, I just, like I said, I have never actually attempted to use Freedom myself. I know a bunch of projects use it. I don't know if you guys know this company, MetalBear.
Yeah.
Yeah, so MetalBear does remote Kubernetes debugging, so you can kind of trace your… you can open a local debug session, but use resources in a remote Kubernetes cluster.
So imagine you're touching a file, but the file doesn't exist on your disk, but actually exists on some shared drive in a Kubernetes cluster.
So… Where there's software, you… They proxy every lip-sy call, or a multitude of them. They've written a wrapper for every lip-sy call.
So, when… when your program does file open locally to read the file, it… actually, they proxy it to a… to the Kubernetes cluster, where their agent runs, and they just ship you all the bytes back, so your local instance of the program is oblivious to That the file doesn't exist on your disk.
Every call is proxied to the remote machine, and then It pretends all the reason rights, everything, just… they've implemented the whole thing.
So you write to a local file, that actually gets proxied, it gets written to the cloud file.
And you get the responses back and everything, just like normal. And so… to pull that off for Go applications, for… like, let's say, a ZIG application, or anything that doesn't actually use libc, where these calls could be done with LD preload, these wrappers, that actually use Frida to binary patch in their handlers.
So I know it's doable.
They have, I mean…
**Tyler Yahn (Splunk)** 45:33 I feel like this opens up a lot of opportunity.
Bye.
**Nikola Grcevski** 45:36 I think so, too. I think so, too.
That means that… But I always, like, I knew this existed, I knew it could be done, but I never thought about, how do I give it back information from the eBPF side, which is where most of our stuff is?
But then… Then I thought of this last bit. Well, I can just call into something for which we have a probe, and that probe will recognize the magic, and then Use BPF Pro Bright user to write back data.
Maybe there's even a way to read the BPF maps directly, but I think for that we need root, right?
I don't think you can readBPF maps without… Super user privileges on the user space application.
**Matt** 46:20 Yeah, I think we do.
**Nikola Grcevski** 46:22 So, that relieves user, which is not great, I know. It's only a subset of people will be able to run it, but provided you have access to eBPF ProRate user, then… Now we can pull this off.
Yep.
Because otherwise, there's no way, like, the event needs to make it on the ring buffer to OB user space, somehow, to be stored.
The other alternative is what Go Auto did, maybe?
attach a memory segment, but you still needPF ProWrite user to write into that memory segment, so… Yeah.
Because technically, this guy just needs to read, what's the trace ID here? If we had a way to read from somewhere.
information about what is the trace ID, For this specific transaction that's currently running.
For this current thread.
That would be sufficient, but I don't know how to give it to it from eBPF.
he… the only way I thought of was that it called back, it calls, and we write the buffer, and… On the way back, this trace buff that we passed into IOCTL contains the value.
**Tyler Yahn (Splunk)** 47:42 Yeah, I mean, I think that makes sense. I think that's kind of what we do for the auto insertion as well, so… I think that that's… yeah.
**Nikola Grcevski** 47:48 Yeah.
Yeah, that's exactly it. Yeah.
**Tyler Yahn (Splunk)** 47:56 Yeah, I, I… Okay.
What's the… what's the timeline on this?
**Nikola Grcevski** 48:04 Well, I mean, I've been, I wanted to take… take on a task, so for me, this is important. Why? Because, I want to make sure that OB works really well outside of Kubernetes, so that's one of the things That I was kind of planning for myself to focus on, going… forward.
And so, one of the challenges that I always had was, like, how do I communicate, between the services, what their names are, which we kind of get for free now from Kubernetes, right? So, you produce, like, service graph metrics and all these things, and… It's, And it's not possible to do with SSL, right? So you can pass along messages between them on regular headers and whatnot, and say, I'm really this service, so when you get me, when you kinda… you know who's your caller, and so on.
And, but this opens up a way that we can do it for SSL.
and not rely on TCP packets. TCP… trace parents, because the TCP trace parents, as much as they're great, they die at proxies.
And so, we can do context propagation across, like, proxies or load balancers and things like that, right?
So this opens up a lot, so I think it's, high priority. So I'm gonna give it a shot.
**Tyler Yahn (Splunk)** 49:30 Cool.
**Nikola Grcevski** 49:32 I… I was thinking of first making a POC with the LD preload, because I already have this part working, so… and I'm more comfortable with that.
And see if I can actually get the whole loop done, such as… The IOCTL does give me the trace buffer, and I can populate it. Once I have that working.
I'm going to focus on the freedom part to see if I can actually do the binary patching instead, I'll be able to preload it.
**Tyler Yahn (Splunk)** 50:02 Did you see, Mattia mentioned that there's a Go API for it?
In the chat.
**Nikola Grcevski** 50:10 Yes, for Frida?
**Tyler Yahn (Splunk)** 50:12 Yeah.
**Nikola Grcevski** 50:13 Yeah, okay, great. I didn't know that. That's perfect. But I don't know if he uses Sego. If he uses SeaGo.
**Tyler Yahn (Splunk)** 50:20 Yeah, yeah, yeah. I just looked really quick, it didn't look like it did, based on its invocation of the compile, but it's tough to tell by the example whether that's actually the case or not.
**Nikola Grcevski** 50:31 Yeah, so Frida is, like, multiple projects into one, and so there's Frida Gum. Frida Gum is the one that actually does all the heavy lifting, and then there's, like, Frida Core, and I don't know what, but the main Frida product lets you script everything with JavaScript.
Which would probably be too heavy for us, because every time your handler runs, it invokes V8 to kind of run it.
Which was not great.
No. So what we want to do is, like, a binary… with Frida Gum, Which is, I think, what Meadow Bayer's using.
**Tyler Yahn (Splunk)** 51:05 Okay.
**Nikola Grcevski** 51:07 And just know that MetalBear actually does even the patching of Go, like, effectively what we do with U-Probes, they do it with Frida.
And they had to write the register remapping, because… I mean, technically, they… I think all of their code runs with Unix ABI, but code has its own registered conventions, so they have to… I think their contribution there was that they wrote the code to kind of shuffle the registers back and into a… Either the standard Linux API.
from the Go ABI.
So they do that registry mapping sort of thing. They spill the registers, remap them, then restore them back, so you have no idea from Go that something's done to you.
But… Yes.
We'll see. Alright.
I can't promise it will work, but I… I think it will.
**Tyler Yahn (Splunk)** 52:10 Yeah, this is super exciting. Pretty excited about this.
Okay, cool, we're coming up… 10 minutes left in the meeting. I did want to mention also, that, Steven, I think you shared that the KubeCon EU CFP is open, which is pretty exciting. If you didn't get your talk accepted to North America, maybe… submit it to EU, or come up with a new one. I think that the more OB talks we can get, the better. I'm super excited about that. I'm gonna try to start thinking about talks again.
Even though I still have other things to do in November. But anyways, yeah, welcome to the KubeCon life.
Also, I think on that note, the next Wednesday, if we're gonna try to get this next release out, I'd like to have us talk about the next milestone. I've already populated it with, like, bugs that I've identified, essentially, as blockers for the V1.
But I'd like to also have folks, if you, have things you want to get done before the V1, come to that meeting prepared, to have them added or talk about them in the milestone.
At that point. So, yeah, we'll do a little planning, I think, hopefully, next week.
But other than that, I think that those are kind of top of the, Double-check the comments, yeah. Anything else folks had they wanted to talk about?
Well, cool. Okay, if not, we can end the meeting here.
Yeah, I will see you all next week, or asynchronously. Until then.
Bye, everyone.
**Giuseppe Ognibene** 53:48 I would want…
**Nikola Grcevski** 53:48 Right.
