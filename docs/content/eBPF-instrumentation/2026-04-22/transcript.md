SIG: eBPF instrumentation
Date: 2026-04-22
Duration: 50 minutes
Zoom Recording URL: https://zoom.us/rec/share/F5aB6rhHLwXfTGj-svLfVr-rP2XPnZ4Qb055p83TElvOLCp6kBgm4MX3z-aAqI81.PiSXO3MR5p7-o08B
============================================================

## Zoom Recording Transcript

**Tyler** 01:15 Hey, how y'all doing?
**Stephen Lang** 01:19 Bye.
**Giuseppe Ognibene | Coralogix** 01:20 My daughter.
**Tyler** 01:22 Dude.
Giuseppe, you're making me jealous at that coffee.
**Giuseppe Ognibene | Coralogix** 01:27 It's an espresso, it's not only popfast.
**Tyler** 01:29 Ugh… I could use one right now.
**Giuseppe Ognibene | Coralogix** 01:33 Yeah.
**Tyler** 01:35 What time is it there? Isn't it, like, 4PM for you, or 5PM?
**Giuseppe Ognibene | Coralogix** 01:39 5PM.
**Tyler** 01:40 Yeah.
Just a little… just a little evening cap, huh?
**Giuseppe Ognibene | Coralogix** 01:45 a coffee. Yeah, before gym, you need a coffee.
**Tyler** 01:48 Oh, dude, yeah, I'm with you on that. That's where it's at.
Cool. So, it looks like we may have Quorum, maybe wait a little bit longer. Rafael, I think, might also make it. I know that, some Grafana folks are probably out. Right, Steven? They're still out today, right?
**Stephen Lang** 02:10 Yeah, Mario, I'll mix it all around.
**Tyler** 02:14 Yeah, okay.
**Stephen Lang** 02:15 Mark and Raphael.
**Tyler** 02:27 Well, cool. We could probably jump in here then and get started.
start sharing my screen. If you haven't yet, go ahead and add your name to the attendees list.
And if you have agenda items you wanted to talk about, please go ahead and add them. And, yeah, we'll jump in here.
Cool. Alright, I see Raphael has, joined.
Awesome. Well, cool. I didn't have too much myself, outside of just reviewing pull requests here, so, we can jump into this if there's no other takers.
It's kind of action items for the day, anyways.
We made it to two pages. I don't know if Nimrod's on the call, but he was getting worried about… how many things we had. Two pages is nothing. Go look at the collector contribib. Yeah, so… Anyways, to jump in here, I don't know if most of the folks are on the call, but we can just go through these. So, fix the OB agent for build on macOS… I think this is still a work in pro- well, it's still definitely a work in progress draft. I don't see…
**Stephen Lang** 03:48 So I took this one on and sort of asked Copilot to have a look, and I tried it out myself as well, and then I left some comments for the author.
**Tyler** 03:59 I gotcha. Is this something… because, Steven, you had mentioned that you're working on a Mac, right?
**Stephen Lang** 04:06 Yeah. Yeah, so I did… I did reproduce it. It is broken.
And then I did try the PR, and the PR does fix it, but it also completely breaks our CI and release process.
So, I left a few comments on… on there.
**Tyler** 04:23 Okay.
Is this something you would like to see fixed? Like… Do you want to take up this PR and just, like, build another one? Or is this something you don't mind just waiting on?
**Stephen Lang** 04:33 Well, I mean, to be honest, like, there's a lot of things that don't work on the Mac anyway, like around the UDPF side. So, I mean, there's some things that are nice to have, like the linting. Like, I made that job a while ago to lint on the Mac, because at least You know, if you're just writing the Go user space stuff, that is fine on a Mac.
But for most of the things, I had to sort of jump over to Linux anyway.
Yeah. So for that reason, it's not, like, a massive priority for me. I'm happy to look into it, but I think it's… doesn't seem to be a priority generally.
**Tyler** 05:04 No, that's fine. I just didn't know if you were waiting on it, feel free to go ahead and supersede. Seeing something that's, you know, more than 2 weeks old is all I was just getting at. But, yeah, if it's not a priority, I don't… there's only so much time you have in the day, right? So, yeah.
**Stephen Lang** 05:21 Yo.
**Tyler** 05:23 Cool, alright. Well, thanks for looking at that, we'll see if the response probably closes out if it reached the stale marker, which is also being added.
Next up is Configv2. This is something we've been talking about for a while. This is in a state of review, like, needs more reviews at this point.
I'm happy to go through it again, gone through it a bunch of times. I was hoping Nimrod would be on, because I kind of wanted to ask him about this.
Nope, still not on. But okay, maybe I'll just reply in thread. But yeah, if you haven't yet, please go ahead and take a look, needs… needs more eyes. This is blocking the collector distribution, just a heads up. I don't know if I made that clear multiple times now, but, like, yeah, that's… this is something that… The collector's asked for is a split in how this is actually, parsing out things for what is going to be allowed in Obi and what isn't going to be allowed in Obi. We definitely don't want to, like, trim down Obi so that it's nothing, but we don't want the collector config to be, like.
A bunch of no-ops that don't actually do anything, or cause errors, or something like that, so yeah.
Okay, this one might be the one I might want to talk about. I've taken a look at this.
Yes, this is the one I'm taking a look at. The… there's a lot of CI failures on this one, starts out, it was just not upgrading the Zookeeper configuration while it was upgrading the rest of this Kafka stuff.
That was done, there's still a bunch of failures, and I'm still waiting through them, and it's slow going, but it's still continuous. So yeah, taking a look at this one.
**Mattia Meleleo** 06:58 I have a question about this one. So, initially we had some tests with, which run on Kafka 3.x.
Then, later, we added the four.txt, because something was changing in regards of the topic. I think they use UUAD now, or something like that. Would be… would it be okay to have tests for both? I mean, should we… Are we forced to upgrade this, or… I think we have tests for both versions, so I think it's fine to have one 3.9 and one… 4.x.
**Tyler** 07:39 Yeah. I mean, I don't know the full test coverage of Kafka offhand.
I agree with you, it'd be a good idea to have testing for both. I'd actually want that, right? Like, you want to have, like.
probably testing for every version, if I could live in a perfect world, but, Yeah, so I'm not opposed to that. I don't know, I'd have to look a little bit closer at, like, the rest of, like, the testing.
Because I… yeah, I'm with you, like, it'd be nice if we could do a 3.9, but also do a 4.0. Are you saying that it's done somewhere else, that we are doing a 4.0 testing?
**Mattia Meleleo** 08:15 Yeah, if you search in the codebase, there is a docker file underscore 400, and that's testing the version 4.0.
**Tyler** 08:26 Like, 400 like that, 400?
**Mattia Meleleo** 08:29 Yep.
**Tyler** 08:30 Okay, there's probably better ways.
**Mattia Meleleo** 08:32 It's the… it's docket file underscore 400.
**Tyler** 08:35 Okay.
Java Kafka…
**Mattia Meleleo** 08:52 And, there is also Docker Compose, which uses this Docker file, which, which is the ZooKeeperless version.
**Tyler** 09:01 Okay.
Yeah, and then this one is specifically… Yeah, the oats test, though.
So that would mean that we'd have integration tests for… this… older version, but the OATS test as well? Yeah, okay.
Okay, I can take a look. Yeah.
**Mattia Meleleo** 09:31 Ox tests, I'm not sure if we should duplicate them as well, because we already have integration tests, so… Not sure.
**Tyler** 09:41 Yeah, I think that's, like, kind of, like, the big problem here is, like, it sounds like we have a lot of tests, and it may be that we're, like, duplicating coverage, and we need to, like, be a little bit more… I don't know.
Explicit with what we want, and, like, Yeah, okay.
But that's… that's a good point. Don't wanna lose this.
Yeah, okay, good follow-up. I will… I will take another look, and maybe just… we'll throw away this change.
But we probably need more holistically to look at it and say, like, what is our coverage of the Kafka testing, so… okay.
Yeah, thanks, thanks to follow up on that one. We don't have to solve it here, but yeah.
Okay, Yeah, because also up is the CPCAF, Docker tag. I haven't looked at this one. I don't… I think Nickel looked at this one and think it was very similar with the Zookeeper stuff is missing, if I'm not mistaken.
Oh, maybe it's a different thing? So this also needs more eyes on it. I don't know what the… the testing on this one is, but yeah, just another upgrade.
Okay, continuing on, the features support, MS SQL… Packets, I think this is… It's gotten approval. It's… Out of draft form.
**Mattia Meleleo** 11:18 Yeah, I had the last reviewer to this one, and it looks good to me, but there are a lot of other reviewers, so I left a little bit of time for other people if they want to give another look.
**Tyler** 11:33 Yeah, absolutely. I see, Giuseppe and, Rafael You are all… Also, taking a look at this one, is this something you can come back and take a look at, or is this something… Cool, alright, yeah, if you guys want to take a look at this, it'd be great to get this merged in, so yeah, we'll wait on that.
Okay… Mario is selectively replacing tracing programs with the system with this… support them. This is definitely a work in progress, Mario's not here. I think we're gonna skip this one today.
Update the Docker, again, also needs more eyes on it.
This probably can get closed, but it again needs more eyes. This is doing a bunch of major version upgrades.
Mark is on, add support for the NATS protocol.
Let's talk about this one.
**Marc** 12:22 Yeah.
There was some feedback from Raphael, and… I already addressed it, so… I need another round.
**Rafael Roquetto** 12:31 Did I get to it today as well.
**Marc** 12:33 Thanks.
**Tyler** 12:35 Okay.
Awesome.
Okay, mr. Alias, who's this guy?
Yeah, this is an interesting one. I guess I could ask, maybe, if there's appetite for this. This was kind of a POC, like, when I was at KubeCon, I was talking with Nicola and some of the other guys, and this was an interesting idea, is that, like, if you have asynchronous, like, Go programs right now, you can't… like, asynchronous in the sense that they pass context via a channel, like, that context gets lost, but… If you were gonna manually instrument it, you would just link spans from one context to the other context using span links, and there's really nothing, like, stopping us from doing that.
So this is a POC that I, like, put up, and I… Obviously forgot about it, And essentially, it does that, like, it looks for channel reads and channel writes, and if there are contacts active in any one of those Go routines, it'll link the Go routines by adding, like, a span link. It doesn't work with, select, if I remember correctly, yet. It could, but I guess that's just a question to the people on the call, like.
Is this something we should pursue? Like, is this interesting? Or is this not really, like, worth… Adding.
I can't see… I see a thumbs up from Mattia, I don't know if.
**Mattia Meleleo** 14:02 Yeah, I think it's interesting, I'm… I haven't had a look at the code, but I wonder how do we keep in check all the… all the maps? Because we have a lot of maps in Go, which hold the context by Go routine. Do we keep all of them in check, or… How do we do that?
**Tyler** 14:23 I don't think it was too hard, it was, like, there's not… so essentially, you're asking in the Go routine, like, you just ask if there's an active context in the Go routine, for the Go routine.
And if there is, there's just a linking that goes on there. It wasn't… If I remember… sorry, it's been a few weeks since I looked at this, but yeah, it was pretty straightforward, like, there's a few different, like.
channel structures that we added, but, like, the map… map lookup was actually pretty simple. It's just, like, if there's an active Go routine being run, it should be in, like, your common map, and then… Yeah, the only hard part was really just, like, finding the insertion points, and then, like, for the channel reads and writes, yeah, that was… that was about it. I mean.
Again, like, the select case is way harder, because the select case has, like, the code for that in Go is, like, very complex, I still don't think it's impossible, but this one was.
**Mattia Meleleo** 15:20 Just like…
**Tyler** 15:20 Essentially, like, it's just… yeah.
**Mattia Meleleo** 15:22 Okay, I think I saw the code that I meant to ask.
There's the Mongo map, the SQL, yeah, yeah, it's this one. Okay.
**Tyler** 15:31 Yeah, definitely.
**Mattia Meleleo** 15:33 DFC.
**Tyler** 15:34 Okay, I see what you're saying.
**Mattia Meleleo** 15:35 Yeah, yeah.
**Tyler** 15:38 Yeah. Yeah. I mean, I can try cleaning this up and move this out of, POC. If… if you're interested in taking a look, I will do that. Yeah, take that as an action item.
**Mattia Meleleo** 15:50 Yeah, I will.
**Tyler** 15:52 Yeah, I… you're welcome to take a look beforehand, but I don't want to waste your time either, so, let me… let me pull this out of POC, and then we can… I'll ask for review.
Awesome.
Okay, next up, generate config docs. This is, again, also from Nibrod. This is, Probably waiting on me, if I remember correctly.
Yeah… Moved… okay, cool.
So it looks like this has just moved to the dev docs, which… actually, I think this is ready to merge.
Yeah, looks great to me.
Okay. Are there any other people, waiting to review this one?
Speak now, or forever hold your peace.
Cool. Let's get this merged then.
Awesome.
Okay.
Next up, Go! Yeah, this one. This one just needs the regular cleanup, I haven't got around to it. It still is trying to upgrade, eBPF, which they haven't put out a patch yet, so… that's gotta get pulled back. Essentially, like, everything we've done for a lot of the other ones, because we bundle everything together, I gotta pull out the ones that we can't… I maybe look at it a little closer, try to see if I could, like, add renovate config to tell it to not upgrade to this V021, explicitly, but yeah, otherwise… I haven't gone through all the others, but they usually are pretty straightforward. So this just needs some eyes on it, and then manipulation.
**Mike Dame** 17:42 Tyler, is this still what we need to do the, Go Auto, release for?
Or was that for another reason?
**Tyler** 17:50 No, for the Go Auto release, that was because, most of the upgrades over there require Go 125 as a minimum.
we still support 124 over there, and that hasn't been, like, supported by Go for a few months. And so it's more, we need our release to tell everyone that we're no longer supporting 124 over there.
And then we can go through the upgrade paths.
**Mike Dame** 18:13 Right. Yeah, as soon as I volunteered, it was like, had time to do it, and then, of course, as soon as you volunteer to do something, a bunch of other stuff comes up, but I do still want to work on that, or at least help out with it.
**Tyler** 18:26 Yeah, yeah, I know the feeling. okay, cool. Yeah, if you want more info on that, please just ping me in Slack, I can fill you in.
**Mike Dame** 18:36 talk after.
**Tyler** 18:37 Okay.
Okay, cool. Cia daily test reporting.
I hope this isn't blocked on me.
**Stephen Lang** 18:48 So this…
**Tyler** 18:48 Steven, how we doing on this one?
**Stephen Lang** 18:49 This is done, and there's a couple of approvals, but just because you did one pass on it before, I wasn't sure if you wanted another look at it.
But it's, it's been tested as much as I… Cannes, and there was, like, an example in, in the PR, which I updated based off of your comments.
Okay.
And this is fairly, like, low risk, because it just kind of runs on its own, and the report itself just sits within GitHub Actions. It doesn't touch.
**Tyler** 19:19 Yeah, I agree. I'm tempted to merge it here, given Mario and Mattia have already approved it, so, unless there's opposition to that… Got a thumbs up.
Perfect.
Maybe. Okay.
**Stephen Lang** 19:37 Nice.
**Tyler** 19:39 Cool.
Okay… Next up, Docker test, this just needs some more eyes on it. Looks like the, Sea ice healing.
This is interesting, this is, gRPC HTTP, support.
**Mattia Meleleo** 19:57 Yeah, I had a look at the… the new review from, from Rafael. I addressed all my… all the comments in the… in my local branch.
There are a couple of them which, which breaks everything again, so… I might have an explanation for that.
But yeah, I will, answer everything, I think, today.
**Rafael Roquetto** 20:20 Yeah, I just wanted to say sorry if I'm not reviewing the whole thing at once, it's just like a big PR, so I'm just trying to…
**Mattia Meleleo** 20:28 It's completely fine, it's…
**Rafael Roquetto** 20:30 I hope that's a.
**Mattia Meleleo** 20:31 Big PR, so… Yeah, yeah, completely fine.
**Rafael Roquetto** 20:34 Okay, cool.
**Tyler** 20:39 Okay, cool. Needs more iteration. Sounds good.
Okay, moving on then?
Where are we at? Do not review, I'll leave that one out.
Alright, add issue templates, stale workflows, and, component auto-labor… auto-labeler.
Oh, I thought this was Mattia, unfortunately. Nebrad is not here.
Yeah, this looks good. There was just some details I wanted to get addressed. I don't see Mattia… or, sorry, I keep thinking that you're PR, Mattia.
Yeah, I think the only blocker for me on this one was that there was, like, this blank issue. I think we should still be able to create that, but I don't think that that's too controversial.
And then Mark has also reviewed.
Yeah, I think that these all are great feedback. So, this just needs, Nebrad, take another look at this.
Next up is Add MCP supports. This is also something that came in, I think.
Oh, 5 days ago, I thought it was, like, yesterday.
See, I thought I saw Raphael, you took a look at this, but it looks like maybe it's just Nimrod…
**Rafael Roquetto** 22:17 Yeah, I, I think I requested, Copilot.
Again, so… the way, yeah, the way I usually… I've been usually reviewing code is, like.
I just request a co-pilot, I wait for it, so, you know, it's just so many reviews.
So I kind of try to prioritize, wait for Copilot, see if they address it, then once they're done, then I'll go and jump in, do a manual review. That's how I'd be mostly doing things. So, you know, I'll have a look again on this one as well, today.
**Tyler** 22:46 Yeah, I'm not… I… first off, I do… I do that to myself as well, so, like, I'm… I'm all about the Copilot reviews, But… I'm kind of confused, I thought they were gonna split this into… minimize the MCP support code… oh, okay, alright.
Oh, okay, so it has been minimized. Okay, I see.
**Rafael Roquetto** 23:07 Yeah.
**Tyler** 23:08 So yeah, okay, I guess this is just ready for review at this point. I'm kind of confused about this one, so like… Rafael, have you taken more of a look than just, like, a cursory Glance, or is this something that is just very opaque to you right now?
**Rafael Roquetto** 23:22 It's still a bit opaque. I mean, my understanding is that they're just adding support for MCP, and they use some existing infrastructure that we have in the code, so it's kind of a, you know, higher level, so they're not dealing with eBPF buffers, or even, like, the code path on TCP detect transform. It's a bit one level up. So now I need to go and look and understand the protocol and make sure It's, it's, sane, basically.
**Tyler** 23:49 Yeah, yeah, okay.
Yeah, I mean, I think it's a cool idea, I just, yeah, I haven't gotten it either, so, okay.
This just needs review, then.
**Rafael Roquetto** 23:58 Yeah.
**Tyler** 23:58 Not just, Raphael's review. Other people on the call, if you're able to, please also take another look. Looks like there's merge conflicts as well, but that, I think, doesn't block the review.
I think similar to that, there's another… Oh, it's way up here. Okay, so, Next up, also from Nimrod is this, share, PID, NS disambiguity?
I don't know… I see Mattia's reviewed it, I see Rafael's reviewed it. Thank you both for reviewing everything. I keep saying your names, by the way.
**Rafael Roquetto** 24:38 I had one question for, for Nirod, which is, The bug is correct, so he's right onto that, and I think his fix is correct.
But… basically… so the problem is that we can have more, more than one… PID in different namespaces, so the PID can repeat and then it can, collide.
And then we are using the host PID, to disinvigorate that, but then my question was, okay, if you're… if you're factoring the host speed into the equation. Why not just use that? Maybe… maybe it's a bigger refactor doing that, and then we don't want to do it. We want to do one just done it here, because, you know, then don't explore the scope of the PR.
But I… you know, yeah. Basically, I was just waiting on that answer.
**Tyler** 25:35 Yeah, it looks like… We're also waiting on… Maybe Nicola or Mario to weigh in on this one as well, but yeah.
No, it's a fair question.
**Florian Lehner** 25:44 Maybe a dumb question, doesn't this open the question on how everything is deployed? Because at the moment, everything is expected to be deployed as a daemon set.
And we know it works, but with this change, maybe it enables use cases where, where, OB is deployed as a sidecar, so if someone is not interested for whatever reason.
Using it as a, daemon set.
That's just the only argument I can think of at the moment around this topic.
**Rafael Roquetto** 26:20 I think they might already work. I mean, don't quote me on that. I know Bela worked as a sidecar. I don't know what the current state with OB is, I would expect it to be the same.
But that's… this is a good question, because if the… PID.
is coming… you know, the players, the sidecar and the PAG is coming… from somewhere else.
We don't have access to the host page, I don't know what would happen. Like, I actually have to go and reread the code to try to understand this better.
**Florian Lehner** 26:51 Yeah, this is just something that pops into my mind, but I never tried OBI as a sidecar deployment, always Demon said.
But people are creative out there.
**Rafael Roquetto** 27:01 Yep.
**Tyler** 27:05 Mattia, do you know if this popped up because Nimrod was looking at Sidecar?
**Mattia Meleleo** 27:09 Yeah, I think this specific bug came out from my deployment in which it was used as a sidecar, if I'm not wrong.
I think. I'm… but I'm not sure. We have to wait anymore for that.
**Tyler** 27:23 Okay.
So yeah, this may come back to that, yeah.
Okay, alright, moving on then.
Also… Man, I'm getting all confused. I'll have to send Nikola PR.
Another open one from Nimrod is to skip these Lambda classes during dynamic agent attachment to prevent this no class death found.
Looks like this has the reviews… Yeah, I don't think anything's blocking this. Any opposition to merging this one?
**Rafael Roquetto** 28:27 I think we can merge it.
**Tyler** 28:29 Yeah, okay, cool.
Yeah, this is on my list of things to review, so, I will trust in the two approvers who have already done this one.
Perfect.
**Rafael Roquetto** 28:39 Big mistake.
**Tyler** 28:43 Okay, next up, add debug events to NetHolly and Statshall user space. This is from Giuseppe.
I thought I saw Giuseppe on the call, if I'm not mistaken.
**Giuseppe Ognibene | Coralogix** 28:57 Yep.
**Tyler** 28:59 Yeah, anything you wanted to say about this one?
**Giuseppe Ognibene | Coralogix** 29:02 Yeah. For me, you can match it. There was some copilot, comments. I did it.
**Tyler** 29:10 Okay, so it's been… yeah, so this just needs approvals, is what it looks like then, right?
**Giuseppe Ognibene | Coralogix** 29:15 Yep.
**Tyler** 29:17 Okay, so yeah, this is, again, needs reviews, I'm coming back and I'm seeing Rafael and Matia, reviewing, so yeah, I'm trying my best to get some reviews, but yeah, more people, if you please, could get some more reviews, that'd be great. Yeah, and we'll try to get this moving.
Okay, next up, I think this is the same… MCP guy… Talking about embedding?
This one, I was a little bit more confused on, I think there was also, like, 3PRs, so… I was even more confused on this one.
But, yeah, it looks like there's a lot of, like, meta-operations that this is trying to encapsulate in, like, the MCP servers… I'm sorry, not MCP ser… the, the agents and, like, their communications.
I'm not as familiar with this one, but… yeah, okay.
Looks like they've changed it. There was, like, a specific vendor that was in here before, and I was a little… Confused why that was the case, but… Okay, yeah, this is… looks like it just needs reviews at this point, hasn't had any.
We can keep moving, though, if no folks have taken a look at this one.
Okay, next up is the Document the Cates cache. Again, this is, I think, a Nimrod PR, yes.
Taking a look at this one, I was a little confused on this, because I don't think some of these things are that accurate, but I don't see any response from Nimrod yet, so… I don't know if this actually needs any more discussion. It just needs… I think, Nimrod would take a look at it.
Also, up, notices, run notices updates in a container. This is for… per architecture. This is from Mattia.
**Mattia Meleleo** 31:12 Yeah, I think I addressed the last comment. I think it's ready to go.
**Tyler** 31:18 Cool. So yeah, the only thing I had was the… The… how did you end up… Getting the release thing to work?
**Mattia Meleleo** 31:32 It's in the last commit. I tried locally by… by doing the make release.
And it seems to work, there is no… no licenses for AMD64, which are being put into an ARM64 package.
**Tyler** 31:53 I see.
This is taking forever.
**Mattia Meleleo** 31:58 I think it's better if you're in the comments tab.
This is unreviewable.
**Tyler** 32:03 Yeah, So, it's in the makefile, is where you addressed this specifically?
**Mattia Meleleo** 32:15 Yeah.
**Tyler** 32:17 Oh, okay, alright, yeah, I'll have to take a look at this.
Okay, cool, yeah, yeah, this needs more.
**Mattia Meleleo** 32:23 It's just the CP minus R notices go arch into the staging deer notices.
**Tyler** 32:31 Yeah, yeah. Oh, yeah, okay.
Yeah, this is all I was looking for as well, so… Okay, Yeah, let me… let me take another look at this.
Outside of the context of the meeting, but otherwise, this looks good.
Thanks for doing this as well. I know folks that are running on different architectures Would like to use the CI system. So, yeah, this is great.
Okay.
Next up, yeah, coin support, I didn't even notice this one.
Okay, oh, 9 hours ago, okay, that's why. Another… AI, support. Yeah, this is great. There's a lot of, lot of, a lot of AI support coming in.
**Stephen Lang** 33:17 This one, I think I took… I took a look at it. There's… there's a lot of fixed test commits with all failing tests, so I think it's still kind of… In progress.
**Tyler** 33:26 Okay.
Yeah, it does look like it's still got failing tests, but it looks like maybe the tests are… Getting closer, but yeah, still, still a work in progress.
Awesome.
Mark, I know you've also taken a look at this. Have you gotten deeper into the codebase?
**Stephen Lang** 33:50 Oh, he looks AFK at the moment.
**Tyler** 33:53 Oh, okay, alright. Thanks for a heads up.
Okay, then, yeah, we'll wait on this one. Looks like tests, and then, if you have time, take a look at that one as well.
Mario, has fixed, Java agent injection.
I don't know if I've seen this one. Yeah, okay.
Copy of the agent jar into the cache.
Yeah… I… am worried about this one.
I think that the caching was pretty useful, given… that otherwise we're gonna have to be copying the agent around all over the place. So I'll have to take a look at this one. I'm not exactly sure we'd want to just write the Java agent every single time.
Yeah, it just looks like it's just taken out the caching entirely. Okay, I probably need to review this one, unless folks have already taken a look at it.
Okay, Steven, you have, error attaching, TCX.
**Stephen Lang** 35:19 Yeah, we can talk on this one. This is a draft for discussion. So, the error that I've been seeing is in the description there, the attaching TCX.
So, Raphael, I don't know if this is your domain, but the context is we deploy on many different clusters, and there's only one cluster in particular which is really super high churn, so if you imagine a lot of nodes being created and destroyed very frequently.
And in that case, when running as a daemon set, I'm seeing this error pretty much as soon as the node is available.
And it seems to be some kind of race condition where the interface like, ready event has fired, but then the interface is, like, not fully available yet. It's, like, not attachable.
So the, the event, the kernel event is there.
But then the attachment actually fails, and it's almost like it needs… Some kind of… Short sleep timeout, or, you know, some kind of exponential back-off retry, or something.
But it's happening in two scenarios. One is when a node has just come online, and another is when a node has had, many, many tens of workloads suddenly deployed to it.
And, you know, maybe there's some kind of interface which is not quite available yet. So, if you look at this PR, it's a reproduction test.
Which is kind of messy, but what it does is that it hammers creating a new interface.
And then at the very end, it just kind of asserts if it's actually come across this error or not.
And then if you look at the failed test on this commit, then you can… you can see it happening in action. So all that I've done now is just to reproduce the error.
And then, like, how we go about actually fixing this, I thought it might be best to, you know, to discuss.
**Rafael Roquetto** 37:14 Yeah, I would expect… I think you're right. This makes sense to me, this error.
I would expect, though, that the error is that the interface is gone. Not that it has come online, but it's not ready. It could be that, I don't… I'm not saying it isn't. Maybe that is a thing, because the way, from the top of my mind, it's been a while since I last touch this code.
the way this works is, like, the interface gets created. We got an event, hey, there's an interface, and we try to attach to this interface, and then no such device, I mean, kind of indicates that interface is already gone.
I… it could be that it's not ready to be attached, but I don't know if this is really a thing. So, if I were to put my money on it, it would be… it created, we got the event, but in between we getting the event and processing it, the interface is already being deleted and replaced with something else. Could that be the case in your test?
**Stephen Lang** 38:11 Yeah, yeah, I mean, that could be the case. I mean, so in that case, if it is that the interface has gone, which is fine, then I think this should be demoted from an error to a devo, or something.
Otherwise, like, so it's either a big issue or it isn't, because if the interface is gone, then it's fine, we don't care.
**Rafael Roquetto** 38:30 Yeah.
**Stephen Lang** 38:30 But if it's that we weren't able to attach to an interface, then it leaves that completely uninstrumented for the lifecycle of that interface.
**Rafael Roquetto** 38:38 So, I, I, I… I'm almost positive that, without, you know, could be wrong here, that the interface is just already gone. And… I think the fix would be then, I agree with you.
We can check the… try to check the error. If it's a no-such-device error, we demote it to a debug. If it's something else, you might want it to be a warn or an error. Keep it. I don't know how hard it would be, because the error is wrapped.
The very end of the predicate, but if we could do something like this, I think that would be… The most comprehensive fix, otherwise just demoting everything to to a debug, I think it works as well.
Okay. I mean, we only use TCX now for the… Not only flows fetcher, And… nothing else, As far as I remember, because the TC Tracer is gone. I don't think it's a big deal.
Mattia has a comment here.
Let's see…
**Mattia Meleleo** 39:41 Yeah, I did a quick Google search, I found this piece of code, so it might return node dev when the FD is wrong as well, of the PPF program, I think.
So, might need more investigation, I'm not sure.
**Rafael Roquetto** 39:57 Okay.
Okay.
**Stephen Lang** 40:02 Okay, I'll see if I can look a bit deeper into the reproduction side of it.
And, maybe catch up with you later, Raphael.
**Rafael Roquetto** 40:12 Sounds good.
**Tyler** 40:14 Perfect.
Okay.
Go back to sharing my screen here, and we can finish up.
Okay, last one is from Giuseppe, update error handling and let all a packet stats package.
**Giuseppe Ognibene | Coralogix** 40:35 Yay's.
**Tyler** 40:36 Chef.
**Giuseppe Ognibene | Coralogix** 40:36 follow-up of a previous VR that got matched.
Just to… to answer code.
**Tyler** 40:43 Oh, I gotcha. Yeah, just returning an error instead. Yeah.
Yeah, this looks great.
Let's… Let's get this merged.
Okay, I think with that then, that's all the pull requests. Dare I hit refresh?
Yeah, okay, cool. Then, jumping back into the agenda, see if there's any other topics we want to talk about there. Nope, nothing added. So I can stop sharing my screen, pause here. Anything else people wanted to talk about?
maybe some cool projects people are working on, cool use cases of OB, People have been thinking about talk ideas for KubeCon North America?
**Stephen Lang** 41:42 I don't know if… Robert, are you on the call?
**Pellared** 41:46 Yes, I am.
**Stephen Lang** 41:47 So I started just trying to throw some ideas around the integration test suite and this kind of fake Prometheus Jaeger Hotel collector setup.
You said you'd done this before. Is there any kind of, reusable projects.
From, from, from this.
**Pellared** 42:07 Yeah, so we are doing it our show in Go country, but I think, yeah, we can sing, just afterwards if you want, so to know to… yeah, we can jump on a Zoom call just after this one if you want.
**Stephen Lang** 42:20 Yeah, I have another call, but, I can get you on Slack message.
**Pellared** 42:23 Okay, okay. By the way, right now, I'm stabilizing this related stuff in GoCountry, just as we are speaking.
Yes.
**Stephen Lang** 42:33 Okay.
**Pellared** 42:34 length…
**Tyler** 42:36 Yeah, that's a great idea, we can… If we're finding all these use cases for it, let's build that test suite out in the public, yeah.
**Stephen Lang** 42:43 Yeah, so the context is the integration test suite, although it runs in less than half an hour, actually uses over three and a half hours of CI time.
On, you know, on every room.
So, that's huge.
**Tyler** 42:56 Somehow I know, I ran it on my personal account where I don't have infinite CI.
**Stephen Lang** 42:59 Oh, no.
**Tyler** 43:01 Oh, dear. I blew that out really quick, yeah.
**Stephen Lang** 43:04 Yeah.
**Tyler** 43:05 Yeah.
But yeah, no, it's, it's pretty, pretty funny.
Well, cool, yeah, awesome.
Well, anything else people wanted to talk about? For those who can end the meeting early here?
Hmm.
**Mike Dame** 43:22 I guess maybe worth mentioning here quick is the Go Auto stuff that we've been talking about, trying to figure out a path forward for that. It's kind of becoming pretty clear that there's a lot of confusion between that project and this project, and I think that will probably I don't know, just talking address, he needs to talk to Tyler and the rest of the Ghostig, too, and come up with a plan, but… it seems like archiving Go Auto, making sure that OB is, has feature parity, at least with whatever the, like, gaps between GoAuto and OB now are.
It's probably the best path forward for everyone, the community, maintainers, the users. So that's kind of what's on our minds right now, at least mine. And hopefully that can… Give us a place to focus our efforts, and, kind of… tie up the story in Go Auto and move forward with OB as the, you know, canonical eBPF instrumentation source in OTEL, so… I think the GoSig's gonna do a lot of… Go AutoSig's gonna do a lot of work on that. Anyone here, happy to, join in, but, I think, you know, the people that are involved know.
No, you know, an idea of what to do. So, yeah, we'll keep everyone updated on that, and, hopefully make some progress there.
**Tyler** 44:42 Awesome. Yeah, that sounds good to me. Thanks for the update on that. Thanks for leading the push on that, Mike. Yeah, I really appreciate it.
**Mike Dame** 44:50 Yeah, I feel like I should be. I've been kind of, the one that was digging my heels in on it for a long time, so if anyone's gonna be, you know, leading the push, I think I have a bit of a responsibility to… Accept my mistake there.
**Tyler** 45:05 That's just called responsibility, I guess, right, eventually. Accepting all your mistakes. Yeah. Yeah, ask me how… ask me how I know.
Okay, but cool. Jokes aside, yeah, thanks, thanks for that, I appreciate it. So, yeah.
M.
Okay, I think with that then, maybe we can end the meeting early. Thanks everyone for joining. Good seeing you all. We will talk in a week's time, or see you asynchronously. Till then, bye.
