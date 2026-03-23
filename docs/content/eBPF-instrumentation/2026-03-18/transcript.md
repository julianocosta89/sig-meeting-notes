SIG: eBPF instrumentation
Date: 2026-03-18
Duration: 64 minutes
Zoom Recording URL: https://zoom.us/rec/share/q9XY5oeNU74OCTH5ub-KWW3bPEtAfrpfzVv22fKgv04uiDrg8ndxZOtIqhqurDdQ.rCR7yj8YKmPRR41j
============================================================

## Zoom Recording Transcript

**Giuseppe Ognibene | Coralogix** 01:07 Hi, everyone.
**Mattia Meleleo** 01:09 Blue.
**Tyler** 01:11 Yay!
Rafael, you've, changed your location again.
**Rafael Roquetto** 01:30 Yeah, I mean, tropical lands now with, 30 degrees, 25, life is good.
palm trees.
**Tyler** 01:38 Oh, nice. Are you back in Brazil?
**Rafael Roquetto** 01:40 I'm in Brazil, yes, yes.
**Tyler** 01:41 Yeah.
**Rafael Roquetto** 01:42 For this and next week, so… Tyler 01:43 Oh, nice.
Yeah, that's awesome.
**Rafael Roquetto** 01:45 Yes, it is. It is. I have no idea how happy it feels to just be out, to walk on t-shirts outside. Yeah, it's good.
**Tyler** 01:54 Yeah, that sounds great.
Cool. Well, we can probably get started here in just a second. If you haven't yet, go ahead and add your name to the attendees list. If you have agenda items you wanted to talk about, please go ahead and add them there as well. It's mostly, heavy on stuff I've added. So, yeah, if you have other things you wanted to talk about.
Yeah, we can… we can start in here in just a second.
Cool.
Yeah, let's, let's jump in here. Let me start sharing my screen here, and then, yeah, is, Rafael, do you know if Nicola, or Steven, do you know if Nicola or, Mario are joining?
**Rafael Roquetto** 03:21 Nikola is, on PTO.
Okay. This week? Yeah. Mario, I'm not… he should be around. Oh, there he is. Cool.
**Tyler** 03:30 Yeah.
Alright then. Well, if that's the case, we can jump in.
Okay, cool. So, to start us off, I wanted to talk, or do a little recap, about our, goals. It sounds like Robert's already jumping in here. So, just a kind of reminder, at the beginning of the year, we started, out on our roadmap, and we came up with a bunch of goals.
So, I was looking at some of these yesterday, I think that probably there's definitely some update needs to happen here, but yeah, I just wanted to jump in here. Maybe we could start off by, Robert, you're saying… This can be closed?
The cosigner image? Okay, this is complete at this point?
**Pellared** 04:16 Yeah, it should be, I have no permissions to close here, so yeah.
**Tyler** 04:20 Oh, okay. Yeah, sure.
Awesome. Yeah, that looks great. I was kind of wondering about that one as well. Okay.
3 out of 5, perfect. Okay, cool. So, maybe, maybe actually I'll just pause here. We can go through the whole list, but if somebody has, something assigned to them that's in the wrong status, or is done.
maybe you can speak up, and I can just address that right off the bat.
**Nimrod Avni** 04:51 I think the editor body extraction one is… Like, the header part is merged, the body one is in progress, so either we can move the whole thing to in progress, or… do some tasks.
**Tyler** 05:06 Yeah, I mean, I'm always about sub-issues, but I think you're right, like, having the in progress sounds great, here as well.
Let me… let me update this, then.
Okay, cool. Yeah, thanks, Rob.
Any others?
**Pellared** 05:48 Thank you for that?
**Mario Macias** 05:48 Oh… Pellared 05:50 I'm not sure how we can add things here to the goals.
**Tyler** 05:55 So the goal isn't really to add… To our 2026 goals.
**Pellared** 06:01 There was one more epic, which we added together.
**Tyler** 06:06 Okay.
**Pellared** 06:07 boost them.
Yeah, I added to the… I added to the… Yeah, it keeps the engine died.
**Tyler** 06:15 Okay.
**Pellared** 06:16 the clothes, it's… I'm speaking.
1199, yeah.
**Tyler** 06:26 Integration testing. Okay. Yeah, I don't know… Yeah, maybe I'll just, Mmm… It's the wrong thing.
Well, okay.
I'll look into this afterwards. Oh, this is like, yeah.
I can add this afterwards, Robert, I'll take that as an action item. But did you want to give an update on it?
**Pellared** 07:11 No, at least not from my side, at least Stephen had time to work on it.
**Tyler** 07:17 Oh, okay.
So, just still something that's a work in progress?
**Pellared** 07:26 President…
**Stephen Lang** 07:26 I haven't added anything to this.
**Tyler** 07:32 Okay, yeah, alright. Well then, cool. I will… I will leave this the way it is, and then we will try to add this after the call, so I don't have to flounder while we're on the call.
**Stephen Lang** 07:43 There was, Tyler, I don't know if you want to discuss it now or, offline, but the last thing with this was, I think Rafael put a comment, so there was a bit of a discussion I don't know if you've discussed this whilst I've been away, either.
But I don't know if this was… maybe something that we should, you know, discuss wider in the SIG around just the general approach of, you know, just how easy to use Docker Compose is versus the Docker test library. I know there's opinions on both sides, and it didn't feel to me last time that I looked at this that we had a, A consensus around this.
**Tyler** 08:21 Oh, yeah, I kinda remember talking about this.
I thought that we came to the consensus to try to switch to the Docker Compose, but I am maybe biased, so I'm happy to hear other folks' recollection of this.
**Pellared** 08:36 cooker test.
**Tyler** 08:37 Sorry, the Docker test, yeah.
**Rafael Roquetto** 08:43 Yeah, I should probably, go back and… And playing more with the Docker test. My only concern is really the developer experience of debugging, so… but to have an opinion, I have to understand this better, so I'll just… Go do my homework, and And come back, maybe next week, with… Something constructive.
**Mario Macias** 09:07 I was doing some tests with that, but maybe we can discuss in another moment. I played with the new… tests on, environment, and I've… I found many nice things, and many other things that we are losing, so maybe we can talk later.
about… About that, or even you can even first try and have a first idea.
We can get some… Feedback or some actions to… to do.
**Tyler** 09:42 Yeah, I think, Mario, if you wouldn't mind also maybe just commenting in that issue, some of your findings would be great.
**Mario Macias** 09:48 Okay.
**Tyler** 09:49 So we capture them. Yeah, I think that would be…
**Mario Macias** 09:51 Okay.
**Tyler** 09:52 So we'll probably lose it again if we don't, but yeah, I think that that's probably a good idea. And then Raphael is also gonna play with it, so yeah, we can probably try to move forward on that by doing something like this. That'd be great, if you could.
**Mario Macias** 10:03 Okay.
Yeah.
Cool.
**Tyler** 10:08 Yeah, cool. Alright.
Yeah, continuing on here, so maybe just kinda, going through these really quick.
**Mario Macias** 10:21 Yeah, the 10 is started.
**Tyler** 10:25 Number 10, it started, okay. Optimize switching to trace version.
Oh, cool, okay.
I will put that in the… in progress, then.
Anything else that's actively being worked on that's not in progress?
Maybe I'll look at Nikola's as well.
the EPF profiler, right? That's active, right, Mattia?
**Mattia Meleleo** 10:47 This should be in progress.
**Tyler** 10:49 Yeah, okay.
**Mario Macias** 10:52 Also the… Thank you.
**Nimrod Avni** 10:54 Correct me somewhat, also the trace log correlation. I think we made a lot of progress with it.
**Tyler** 11:00 Yeah. Yeah.
**Mattia Meleleo** 11:02 Oh, yes, true, yeah.
**Nimrod Avni** 11:04 And I don't know about the… hotel collector distribution. Tyler, I know you worked on it. I guess we… I don't know what's the status with it?
**Tyler** 11:14 That is somewhere in here.
Into the 11th century.
17. Okay, yeah, it's going really good. I'm actually waiting on a, a next release from us. There was a dependency issue thing, where if we tried to build it on systems that weren't guarded by our build tags.
it would try to import things that it shouldn't have imported. So, this next release is gonna have fix for the source code.
I was gonna try to get that out this week, except KubeCon's next week, so I don't really wanna, cause some major disruptions by releasing, from Obi this week. But, yeah, it's looking really good. I've got something upstream in the, collector releaser that is primed to get this out, so this is actually going along pretty good. I guess I could… I have myself as an attendee here as well, or a signee, But yeah, this is… this is actually really close, so thanks for calling that out, Nimrod, yeah.
**Nimrod Avni** 12:10 I wanted to ask, while we're on it, is the plan having the OB receiver inside the collector contrib, or having it As a different, a collector distribution, let's say, like, the profiler, has a separate distribution? Because I don't know, like, in my head, I thought it made sense maybe to have them both as a separate receiver that needs, like, elevated privileges, but maybe it's, like, just coupling without any reason, I don't know.
**Tyler** 12:41 No, I wanted to put them all into the same distribution, or sorry, not at all. I wanted to put the OB collector, or the OB receiver into the distribution for the collector contribib. It's not going to be in the collector contribib rep repo, because it would just be this, like, extremely thin wrapper, which… We might have needed to do, or we might still need to do if the build tags don't work, but… Yeah, the idea is that, like, it's, it's, It's a tangled, tangled web for the collector builds, but essentially, this is the repo that actually does all the building, and this distribution is where this will be, and so in this collect… hotel collector contribib.
**All it will do is it'll take a dependency on our, our repository, and in the process of taking dependency on our repository, it'll it… when it builds, it'll just be there. So it doesn't have to actually be in the repo, Nimrod Avni** 13:38 Yeah.
**Tyler** 13:39 But it will… yeah, so, like, right now, what this is doing is it's downloading our binaries… I'm sorry, our source files.
And since we have generated all the source files, this is great, and it's tying it in.
the problem, obviously, is that, like, when it ties it in, it tries to then build it in all of its environments, so things like Windows, things like not our architectures, it's building, which it should, but then it… currently is not completely guarded, for the V06 release, so it's crashing on the build. So, yeah, this is how it should look, and essentially what the… deliverable, or the action… or, like, the way that you're actually gonna use this, just using the collector-contrib, binary or the Docker container in our receiver should be there, is my goal on that one.
**Nimrod Avni** 14:29 Okay. Makes… yummy.
**Tyler** 14:32 Yeah, I… I, I… I like the idea of having it split out as well for, like, permission issues, but I also think that you could just run two, if that's gonna be the case.
Or, if we have a lot of users that would like that, we can always add it as an additional distribution, so we could have it here, we could also have it in its own distribution, so I think this.
**Nimrod Avni** 14:52 have, like, an eBPF, distribution with, like, OB and maybe the profile, yeah. Maybe if that makes sense.
**Tyler** 14:59 Yeah. I do think that, like, getting them in the same place, the profiler and, Obi is pretty critical, given we're gonna have that compatibility going forward, so whether that means that the profiler can then could also get included here.
Or vice versa, you know? Like, putting that in the profiler distribution one as well. Because it does sound like a lot of the restrictions… I think Florian's on the call, but a lot of the restrictions around, like, Sego, they don't exist anymore. So, yeah, like, there's… there's… just permission issues. Yeah, Florian, I don't know if you want to talk more about it.
**Florian Lehner** 15:30 Sorry, I think the eBPF profile is already in collector releases. There's a dedicated distribution for eBPF profiling.
**Tyler** 15:39 Yeah. It's more about, whether it would be included in the collector-contrib distribution as well.
**Florian Lehner** 15:47 Yeah, we don't have plans at the moment to do this step.
Because… of ownership and all these things, and adding the artifacts, or managing artifacts. You have it, stored in somewhere, downloaded from there. Profiling does have it in Git.
And so far, CollectorCon trip is… already quite loaded. Loading it even more with, EOBI and profiling is maybe not the best idea, but maybe you can just have a wrapper verbal collector receiver in Contrip that just imports, imports these repositories, then I think ownership would also be much easier to match, and this kind of stuff, I think.
Datadog already does something like this, where they just have a wrapper in the collector contract and just point to their repositories.
Yep, I don't know how this would turn out, but yeah.
A lot of stuff is moving.
**Tyler** 16:52 Yeah, definitely.
But yeah, so, to answer your question, Imrad, that's my plan right now, but I don't… I have to get this next release, I have to prototype it, and then we can probably… we have to get it through.
**Nimrod Avni** 17:04 Yeah, I guess as soon as we have it in a distribution, if we want to, like, after a change, like, add, I don't know, create a shared one with the profiler or whatever, it'd be way easier.
**Tyler** 17:17 I think so, too. So, yeah, that's my goal.
**Rafael Roquetto** 17:21 I don't know much about this, so just a question. How does it work in terms of dependency versions? Like, do they all have to match the dependency versions of anything that's being included?
**Tyler** 17:36 They have to match in the sense that, like, it has to resolve using the Go, highest value versioning.
Okay, that makes sense.
**Florian Lehner** 17:45 I think the easiest way is if you go, for example, into ePPER profile, and you see it, there's a manifest.
And the manifest defines all the dependencies, and we have a tag on the profiling repository, and this tag is just updated whenever we create a tag. We don't have fixed releases, as we don't have anything stable, that's why we have the tag, V0026 and then the week of the year.
So, 2610 it is, for the moment. But yeah, this manifest… is the base. So, if you just add, GoMod, I go OpenTelemetry I.O. slash OE with a tag, to the receivers, it will be just in there and go build… or the auto collector builder will just build it.
**Rafael Roquetto** 18:34 Okay. Okay.
Thanks.
**Florian Lehner** 18:37 And it's also fine that the dependency of OB and profiling are really separated, so if we decide on something, it does not impact OB and vice versa.
**Tyler** 18:57 Does that answer the question, Raphael?
**Rafael Roquetto** 18:59 Yes, yes, thanks for that.
**Tyler** 19:01 Yeah.
Okay, cool.
Looks like somebody got this in, this is great. Okay.
We're coming up on… maybe a time block here. If there's anything else that needs to get updated here, please go ahead and ping me if you're not able to update it directly, and then we can keep this… keep this accurate. So, yeah, that's kind of my goal.
Okay, yeah, so next up, I also wanted to talk about the next release milestone, so I did want to push this out till after KubeCon, so we're not in a huge rush, but I just wanted to call out, things that are existing in here.
And maybe just go through a little run-through here?
So, Rafael, you have this first one, it's document the new selective telemetry and Sampler. This is assigned to you. Is this something you're still working on? I can unassign you as well.
**Rafael Roquetto** 19:50 No, I haven't done any work on that.
**Okay. Couldn't find the time, so… Tyler** 19:57 That's… yeah, I… Welcome to the world of software development. I'm gonna unassign you here, so other people could jump in if they wanted to, but please feel free to keep working on it if you do find the time.
**Rafael Roquetto** 20:07 Okay.
**Tyler** 20:07 Yeah.
Same here for the document application span, hotel, I think… I'm gonna… Yeah, this has been a while. Okay, so… I'm gonna unassign, Nicola, just in case other people wanna work on it.
Okay, and then, Steven, you open this issue, find a way to use the latest run C in the VM workflows? Is… this is something… this looks interesting, This is an upgrade path issue, right? .
**Stephen Lang** 21:20 Yeah, so… Tyler 21:20 See it then.
**Stephen Lang** 21:21 I keep looking at this on and off, The… it seems to require potentially not using nested virtualization, so that would mean that we would need a, a GitHub Actions runner with KVM enabled.
And I believe the only way to do this is to have a self-hosted runner.
So, I played with the idea of using, some kind of AWS free tier or something like this, but I wondered, maybe, I believe OpenTelemetry has some self-hosted runners.
So I don't know if there's potentially one of those runners that we could use that already has KVM enabled, or if maybe there's a use case here.
For having some kind of OpenTelemetry, you know, shared self-hosted runner that any project could use, including our own.
Where we could have KVM enabled.
**Tyler** 22:16 Yeah, I think that that seems reasonable.
I think this is just worth a community issue on this one.
**Stephen Lang** 22:23 Okay.
**Tyler** 22:24 Yeah, there may be something that already exists, but I think it also has to do with, like, capacity planning as well, so I think that we'd probably want to know from, like, a project level how much this could get used. So, yeah, I think opening a community issue, just asking if there is something there, I think people on the TC would know this, answer. And then, if not, if we can get something, I think is something… That could be done in that issue as well.
**Stephen Lang** 22:47 Sure. Okay.
I'll ask.
**Tyler** 22:50 Yeah.
Okay.
Cool.
Should I assign this one to you? It seems like you're kind of working on this one.
**Stephen Lang** 23:16 Sure, yeah, yeah, on and off.
**Tyler** 23:18 Yeah, okay, cool.
Awesome. Alright.
Document the… for parent-child association limitations, I pinged Nicola on this one. It looks like it's, What did I say? Yeah, started the draft when I added the Java and Python async.
Yeah, so we're waiting on the Python async landing, before he was going to finish up this draft, so this may get bumped out of the milestone if that doesn't land before the, the release, so… Yeah, still actively working on it.
Blocked upgrades, this one for EVPF… actually, I don't know if there's a new status update on this. We're waiting on upstream changes, for this, If I remember correctly.
Looks like this is still open. So, yeah, this is not a blocker on this release, and this might just get bumped to the next milestone, so there's not really much we can do on this upgrade path.
The other one, though, is the upgrade of, oats. This is something that we could probably look at going through. I'm happy to take this on, I don't know if I'm the best person to take this on, but I think, Mark, I don't know if Mark's on the call, but Mark was looking at doing this in other places, how… challenging it would be. I'd love to get a… Yeah, I don't see Mark on the call. Okay.
So, okay, yeah, I can…
**Stephen Lang** 24:43 You too.
**Tyler** 24:45 Oh, he is.
Oh, sorry, yeah, there he is.
**Marc** 24:50 Yeah. Would you… you said I was looking at about… Tyler 24:54 I thought that you were… talked about this previously, talking about the Grafana Oats package upgrade, so we've tried doing this upgrade to the V061, and it breaks a bunch of, like, because the config file changed, and I thought I remember you saying that you had done a few of these before?
**Marc** 25:07 No, but, I can take a look. What's… Yeah.
**Tyler** 25:13 Oh, okay. Yeah, if you have time and you're able to take a look, yeah, just going through this upgrade, literally just upgrading the package, and then all of the, the modules that do these imports, we're gonna have to change the YAML file, configuration for it to match the new spec for the new one, but.
**Marc** 25:30 Trent, would you like to take a look?
**Tyler** 25:32 Cool.
There we go.
Cool, yeah, that'd be great. Thanks for the help.
Okay.
Moving on, this Cyclone, DXSBOM, so the Software Build of Materials Release Artifacts, this is up and ready, Is this the… yeah, this is the files change. So, this is, for independent verification of our build process for all of the releases. This is just using standard tools, this Swift, base, tooling.
the challenging part here was that the agent, the Java agent, dependencies and bill of materials wasn't actually getting included in our binaries, which is… probably needed, given it, is embedded in our binaries now. So, that was just a little bit of the, the complication, but it's not too, too much. But yeah, it's pretty straightforward from what we've done in the past. It's just updating the release thing to include a particular workflows, and then making sure that these generated, SBOM files are validated. And it's very low validation level, essentially saying that, like, does it exist, does it have the right format?
I didn't do too much here, obviously, because dependencies are gonna change, so I don't want to, like.
Build it too rigidly, but yeah, it should be ready for review at this point.
Cool, and then there is this other thing where I found the… I got nerd snipe. Somebody put a commented-out test for the TLS, support for Rails Puma, that looked like it was supposed to be supported, so I tried working with it, and I… it was not supported, and I've been playing with this for a while.
And I'm key covering bugs on this one. This isn't ready, this is a draft. I would like to get it in the release, but it's not active.
So maybe beyond that note, are there any other things that people are working on right now that they would like to be included in this release?
**Mike Dame** 27:35 I just opened a small bug fix a couple minutes ago to the dynamic PID selector that it would be nice to get into the release, since I added that PID selector through this, tag, but, I'm working with it off of Maine anyway, so it's, yeah, either way.
**Tyler** 27:52 No, yeah, that sounds great. I'll add it. Our goal is post-CubeCon, so I think that that seems, like, reasonable.
Cool.
Not a huge rush, I guess is what I'm saying.
Yeah, thanks, Mike. Any others?
**Nimrod Avni** 28:06 Yeah, I have, I think, Raf already approved the PR with the Seek User 1 stuff that I… kind of covering our bases, because I added previous one.
And now, this is just leftovers for… like, dynamically linked.
Node.js emulated.
**Tyler** 28:26 Ugh.
**Nimrod Avni** 28:27 The UV stuff.
**Tyler** 28:30 Yeah, this looks great. It looks like it actually has the approvals. Are we waiting on anything? Oh.
**Nimrod Avni** 28:36 I think just the… I think just the… this is, like, fixed. I don't know why it's… We… Tyler 28:43 This should be fixed.
**Nimrod Avni** 28:44 I can resolve it, because I fixed it.
**Tyler** 28:48 Okay, I will…
**Nimrod Avni** 28:50 I think it's ready to go.
**Tyler** 28:53 We can resolve it then, if you think it's fixed. Yeah, it looks like Rafael… Yeah, it does look ready to go. I don't know what's going on with the merge status here, looks like it needs to get updated. But, yeah, maybe we can get this merged, actually, today. So yeah, thanks, we'll add that to the milestone.
Any other ones?
Okay.
We are at the half hour mark, so maybe we can jump on. That's the whole milestone. Let's keep this moving. I did want to call out, from yesterday's spec meeting, Mattia was able to get a little bit of a guidance on moving forward with the profile context propagation stuff.
And so, the idea was that, like, we have the OTEP open to follow along of what was being done for the resource stuff.
But since it was such a specific profiler, and OB-related topic, it was… the recommendation from Maybe not the general, specification, but… Large, people in the specification that it's probably worth just working on this in our repos alone.
Finding a place for some sort of specification of our own to be defined and then, live in one of our repos.
I know Florian's on the call. We talked with, Evo as well yesterday during the SpecSIG meeting, and they were, you know.
excited.
**Mario Macias** 30:19 Sorry.
**Tyler** 30:19 Sorry. Oh, okay.
Yeah, maybe let's do it this way, so I can actually see who's talking. But yeah, so… the… the idea is to just have… have it live in one place. The next step is to find that place, is kind of the idea.
Mattia, I don't know if… Go ahead, yeah.
**Mattia Meleleo** 30:38 Yeah, I think since Obi is the producer, maybe the right place would be in the Obi repo.
If, if everyone agrees.
**Tyler** 30:50 I see a thumbs up from Florian.
**Florian Lehner** 30:52 Sorry, but… just before KubeCon, a lot of stuff is happening. Sorry, yeah, for me, it sounds good to have it, in the OB repository. We have to figure out, on the profiling side, prioritization, when information comes in from SDK versus OB versus other places.
I think this will be a blocker at some point, but other than this, yeah.
**Mattia Meleleo** 31:23 Sorry, I just, I just chatted with Christos for that, and, we agreed that Obi should be the least prioritized one, so I can put this, this in the… In the spec, or the…
**Florian Lehner** 31:36 contract.
**Mattia Meleleo** 31:36 or whatever, and we can unblock your PR.
**Florian Lehner** 31:40 This sounds nice. So, yeah, I'm just learning about this now. Cool, thanks.
**Tyler** 31:48 Awesome.
Yeah, alright, cool, so there you go. I think that sounds good, we'll work on it here. Thanks, Mattia, for pushing this forward, this is great. I'm super excited about it.
**Mattia Meleleo** 31:57 Thank you.
**Tyler** 31:58 Okay, next up, Rafael, you want to talk about upgrading the Go version?
**Rafael Roquetto** 32:04 Yeah, so… Tyler 32:05 It's included.
**Rafael Roquetto** 32:06 Steven… Steven pointed out to me this morning that, there's a CVE on, when the… Go 126.0, and 120… 5.7?
So… our, like, kub cache, Kubernetes cache image is on… imports the Go, like, the actual image is a Go 126 image.0, but our project is in 125.7 in the Go mod. So my understanding was that's because of Renovate, so this… this drift, and I would like to update this to cover the CVE, And I was wondering if you could just bump everything to 1.26.1, or if there is, like… Printed our rumors that could be a… some sort of issue with 126.1, but I don't know, like, when Nikola… Should be no one who knows, but he's away, so I just wanted to ask if you guys know anything.
**Tyler** 33:04 Yeah, so there's a few things here. So, the Go mod, I would not upgrade to 126. The Go mod is not necessarily the Go version that you use to run the application, it's the Go version that is supported by the application. So, leaving the GoMod actually where it is is probably fine. It's more about, like, how we distribute it, and, like, what we're using when we build it. So if you build it, you want to make sure you're building it with one that doesn't have a CDE. So this is going to be more in the CI system.
That we want to make sure that all of those are using, you know, patched versions. There, I think using the latest 126 is a great idea, so I think that that sounds good. I think updating our container images as well.
is a good idea. I would be surprised if Renvate hasn't done that one. I thought I saw, Oh, okay, so that's the second point. I think I did see them try to do that, and then Nikola pointed out that it actually caused, build fail… build failure, and there is a thing we need to look into, specifically around supporting this. I think there was, like, some… I'm guessing some details around… You know what, let's… maybe not… just come up with stuff, and we'll see if we can find it really quick.
For some reason, I thought it was in the milestone, but, I guess it isn't.
Support JSON RFC, no.
Man, hmm. I guess we can go about it another way and find it in the old…
**Stephen Lang** 34:39 So… Tyler 34:40 Maybe it is just a pull request, sorry.
**Stephen Lang** 34:42 Just in terms of, Renovate, I don't think it can handle the upgrade, because we use the OB generator image.
And that we need… that image needs to have… The same version or greater.
When it's… when it's building the repo. So the image needs to be updated first.
Which means that the image needs to be, built and pushed, which Renovate isn't able to do.
So, maybe this is why.
the, the Go version isn't, kind of, you know.
Living, and always on latest.
It's kind of like a manual step to, like, go… build the OB generator, tag it, and push it, and then use that version to build.
You know, update the go.mods then after that.
**Tyler** 35:31 Okay, I… Yeah, okay, so this is… oh, okay, here we go. This is the issue I was looking for.
Okay, not much more here.
Yeah, so this was… This is the failure for trying to do the upgrade with Renovate, This, yeah, no debug info.
So, I think, Steven, to your point, I think there is a… there's a dependency hierarchy here, but I think there is, like, a deeper thing as well that we need to take a look at, if I'm reading this correctly.
So Raphael, to answer your question, I think this is the… this is the place, that we have to start for that upgrade, if… if I understand it correctly.
**Rafael Roquetto** 36:37 Okay.
Okay, so… alright, so I'll do that, assuming, just so I understand, assuming everything… I get everything to work, then we do want to go to 126 for every… everything, or still leave the go.mod alone.
**Tyler** 36:52 Yeah, leafyGo. Just the images in CI, are.
**Rafael Roquetto** 36:57 Okay.
**Tyler** 36:57 But the CI, I'd be very surprised if we don't have… it already set up to pull in the latest, so, yeah. Go ahead, Steven.
**Stephen Lang** 37:06 So, then the problem is, CI is set to look at go.mod.
Because before, we had, like, loads of independent Go versions, and the CI workflows all had different versions of Go, so to centralize it all, I set all the CI workflows to read from Go.mod.
**Tyler** 37:23 Okay.
**Stephen Lang** 37:24 So it kind of requires that go.mod is.
**Tyler** 37:28 Well, so, it looks at go.mod, but does it pull in that exact version that's using go.mod?
**Stephen Lang** 37:33 Yeah, so when it does the… the go… so if you look at any, like, yeah.
There's a… there's a go… setup go action.
It uses the go.mod to pull that version of Go for… to run that in CR.
**Tyler** 37:47 Hmm… okay. Because I know that there's also ways to, like, specify during the setup, go, you know, use something above a particular value.
**Stephen Lang** 37:56 Okay. Because what we had… what we had before is we had, like, some files were, you know, specified at, like, a Senver minor version, and other files were specified at, like, a Senver major, and they were getting out of sync.
**Tyler** 38:07 Yeah.
**Stephen Lang** 38:08 So we had, like, certain actions running different versions, and it was kind of a bit of a mess.
So I thought it would be better just to have, like, a… a single source of truth for the… for the coversion.
**Tyler** 38:20 No, I think that works… That works well.
If we do need to update the Go mods, Rafael, like, I would also say that we don't want to go past the, the, old stale version, so… like you said, like, the latest 126 and the 125 have been updated. I would say we want to still support 125. There's not a guarantee that everyone has moved to 126 yet, is kind of my reluctance there.
But… Yeah, I'm also confused why this wouldn't pull in the latest, There is also a way you can just do latest and old stable here, but Yeah, okay, I can find that really quick.
But yeah, to Steven's point, I think if that's the case, then I'm happy to update the GoMods, but it would probably be something we still want to support 125 on some level, whatever patched version that is, if that makes sense.
**Rafael Roquetto** 39:18 Okay, it… alright, that would be one… one up from the current one, 125.8 from the top of my mind.
Alright.
**Tyler** 39:27 Yeah… Hmm.
And I don't know about the 126, like, there's also that issue, like.
if… if the 126 actually has, like… I mean, the thing is, is, like.
there's nothing stopping it from breaking the internals of Go, in, like, the latest 126, so there may be something additional to what you're talking about. So we can patch the CVE one by just upgrading the latest, like, patch, the 125 patch.
But the 126 upgrade and using that in our images is still something that… that issue that I linked from Nikola is probably something we need to look at.
**Rafael Roquetto** 40:01 Okay, because, the cube… cube cache… image does use 126, like, it pulls the Go 126 builder and whatnot.
So, do we want to… Just downgrade it to make everyone in 125.8.
**Or… Tyler** 40:19 I can't… I'd have to look deeper into that issue. The thing that Nikola pointed out was that, like, it's… it's breaking, on one… like, the latest 126. So, if it's building, I don't think… yeah, I think it… I think it'll still build, which is kind of the problem, right? Because it's going to silently fail, because its offsets are going to be incorrect.
**Rafael Roquetto** 40:36 Correct.
I will… let's do it like this, because I just, like, found all this morning, so I haven't really looked into it. I briefly did, so it's not something I gotta fix overnight. I will research it in a couple of days, and then if I have questions, I'll reach out to you guys.
Hopefully with better understanding, and we can take it from there.
**Tyler** 41:00 Alright, that sounds good.
**Rafael Roquetto** 41:02 Thanks, though, for all the, feedback.
**Tyler** 41:05 Yeah.
Okay, cool. Rafael, you also have to have the next item for the AI Contributions Guideline. I can start sharing my screen. Yeah, so…
**Rafael Roquetto** 41:12 last SIGA, you know, we talked on past days, we talked a little bit about it, and then, I thought I would put something up. It's an RFC.
So to take this as a starting point. Feel free to disagree, of course.
Tater, and remember, like, at least from where… what I believe is, this is not… set in stone, this is a starting point. And, you know, we can iterate this as we go.
But, yeah, please have a look, see what you think.
They're… There are a couple of, yeah, I updated the, contributing more for humans to, you know, like, make it explicit.
What I think we should do in terms of how to approach AI at Agents.md, which kind of describes the project. This all, like, I use the AI myself for this.
So… Kind of recursive problem, but yeah.
I made sure, like, to read everything, and I added some guidelines, mostly for General coding for eBPF, as well, for the seed code.
Yeah.
I don't know if this is good or not, so yeah, feel free to rip it apart and… And see if you agree.
We can iterate.
**Tyler** 42:38 That's great. I'm glad to… glad to see a start on this. This is awesome, yeah.
**Pellared** 42:43 Have you considered, adding to the pull request template something like, I understand this code, etc?
**Rafael Roquetto** 42:50 Yes, it's… Pellared 42:52 I see the person.
**Rafael Roquetto** 42:53 Yeah, it's there. It's there.
**Pellared** 42:54 I see it. Yeah, I must… Awesome.
**Rafael Roquetto** 43:03 I mean, please read it, see if you agree, you know, give feedback, and then I can, iterate it and amend it.
And… we can take it from there.
**Tyler** 43:14 Cool.
Yeah, thanks, that's, that's great, great to take a look at.
Okay, that's, close to the end. I've got one more thing, and that's just to look at the open pull requests, but before that, because that might close us out, I'll maybe just pause here, see if others have things they wanted to discuss.
One of the things that stands out to me is next week's, meeting, so next week is KubeCon Europe. I didn't know if, not everyone on the call is joining, but I didn't know if people wanted to cancel the meeting, or just continue the meeting in a smaller capacity, because I'm guessing folks that are going to KubeCon aren't gonna… join, I don't plan on being here, I guess is what I'm saying.
Any preference to… Continue having it, or drop the meeting?
**Nimrod Avni** 44:18 I don't know how many people will… like, how many people on this… I know Nikola is not gonna be you. I don't know who else, like, I think from Coral Arts, all three of us are, not gonna be in KubeCon, so we can be here, but… Maybe if we just see, like, if there's any agenda items?
We can decide. I don't know.
**Tyler** 44:41 Yeah, I mean, you could always, you know, if no one shows up, cancel within 5 minutes, too.
**Mario Macias** 44:46 clear.
**Tyler** 44:48 Nimrod, would you be willing to lead the meeting next week, then?
**Nimrod Avni** 44:52 Yeah, for sure.
**Tyler** 44:53 Okay, cool. Then, yeah, let's keep it on in the books, and then, yeah.
Yeah, we'll go that way.
Okay, cool.
Then let's jump back in here and… NPR.
**Rafael Roquetto** 45:10 Just, like, a side comment as well.
after these AI stuff that is submitted, one thing that's in the back of my mind, and I have been discussing this with Giuseppe, is, I want to add some, like, linkers to the C code. We have Clank Tidy and Clink Format.
But I think we can do better. I hope we can do better. But, tooling… the C tooling is a bit scarce, so I'm investigating something, I guess Giuseppe pointed out to me, something called sparse.
which I'll look into, and the other thing that I… that… you know, this is just, like, broad ideas.
It's, for, you know, lack of tooling and tailoring, like, compiler switches and whatnot, maybe use… using, like, some… AI agent to… to connect people, you know, ensure, like.
good practices and things like that. So, it's just something that… there's nothing concrete yet, but it's something that I've been Thinking about that might be something in the next coming weeks.
**Tyler** 46:14 Yeah, okay, cool. Yeah, that sounds great. I'd love to… Love to see more linting there, so that sounds great.
Okay.
Let's jump into some open pull requests. We've already gone through a lot of them, so I think maybe we can skip over some of these.
Maybe starting from the bottom. Config2's still something I'm thinking about? Probably won't get back to this.
**Rafael Roquetto** 46:37 We're seeing… we're seeing your, your top, or each top string.
**Tyler** 46:42 Oh, yeah, you didn't want to check that out? Thank you for.
**Nimrod Avni** 46:46 Well, mostly Zoom, consuming CPU.
**Tyler** 46:52 Okay. How about now? There we go, okay, that looks better.
Cool. So, yeah, Config 2.0, still a work in progress, still thinking about that one. I will get back to this probably after KubeCon, though, so no update on that one.
These Kafka image ones, these are still, I think, need investigation, so, if people are really into looking at Kafka, this is definitely something to, That would… we would appreciate some help on these, but these aren't actively being worked on right now.
I am interested in this one, so to support the MySQL, the MS SQL packets, this is something, Nimrad, you had talked about, Oren, I think, had opened this PR a few times.
Looks like it's got an approval from Mattia.
**Mattia Meleleo** 47:41 Yeah.
**Tyler** 47:42 I know the.
**Mattia Meleleo** 47:42 Something changed, I think. There, I think it should just be rebased to solve some conflicts.
**Tyler** 47:51 Oh, yeah.
**Nimrod Avni** 47:52 Yeah, and I told him, I don't know if he ended up, Adding integration tests.
I think, one of the major comments, I let him know, and… I'll try to ping him, see if he's working on that.
**Tyler** 48:08 Okay.
Yeah, that'd be great. Cool.
Okay, moving on then. The, Python Async I.O, Mark, this is also something you've been working on. Any update on this one? Looks like we've got a lot of comments.
**Marc** 48:26 Yeah, there's a… That violated a lot of comments, but, there's actually a comment of Mattia that, Since you're in the cold, maybe you can, Point me how to do it?
It's, regarding the… Which one?
The tail… the tail call? Yeah.
**Mattia Meleleo** 48:51 Yes.
**Marc** 48:53 Yeah.
**Mattia Meleleo** 48:53 Yeah, I can explain that. So, sometimes it happened to us that, even in production, we saw some, that, that error.
And it's because of some sys CTL config.
So I don't think we should increase it in CI just to make CI happy, because in production, it could happen that it's lower.
But I saw that we can, fix this by, splitting the… The socket filter program.
With, with another additional telco.
And, make it, Less big.
**Marc** 49:32 Okay. Do you have a… Like…
**Rafael Roquetto** 49:37 Yep, we can… I can help you with that if you want, Mark, too.
**Marc** 49:41 Okay, let's do a fair name.
**Rafael Roquetto** 49:43 Yeah, yeah, we can… we can do that.
**Mattia Meleleo** 49:45 So, last time I solved this, I just asked Claude to split it, and it worked.
**Marc** 49:51 Yeah, I mean, I also did, but I don't understand anything, so… that's why I want to have Rafael, or someone that knows, like, yeah, I did something, but I don't really understand how it works, so, yeah.
**Mattia Meleleo** 50:04 Okay.
**Marc** 50:05 Good.
**Tyler** 50:08 Cool, alright, yeah, so it sounds like Rafael can help out on that one. But yeah, we'll look for an update then on that.
Awesome. Anything else on that one, Mark?
**Marc** 50:21 No, no.
**Tyler** 50:22 Okay. Cool.
Next up, this Node.js detector. This is, again, one that we… looks ready to merge.
It's… What? I thought all the stuff was just resolved, what just happened?
**Nimrod Avni** 50:42 It's outdated, because I… I don't know, it got… maybe… That's weird. I think, Raffle, you passed it, you passed on it again, right? It should be good to go.
**Tyler** 50:58 Yeah, I… I mean, Raphael's…
**Rafael Roquetto** 51:01 Y-ye.
Sorry. Yeah, loose food to me, yeah.
**Tyler** 51:05 I don't know why these… we just looked at this, and these were all resolved, so I'm gonna… I'm just gonna resolve these. I see a green box on there. Sometimes GitHub also is a little funky, so… Yeah, this is still resolved as well. Okay, cool. This looks good. Let's merge it.
**Nimrod Avni** 51:25 Thank you.
**Tyler** 51:27 Cool.
Where are we at? The Add Cyclone, DXS bombs, we already talked about this one. This is, again, it's just updating for, Bill of materials.
I guess maybe the only thing is, after this, the next step is then packaging artifacts, so we're talking about, devs and RPMs and that kind of thing, so yeah, pretty excited to get this in so we can keep moving.
This is from Nicola, fix missing requests on pipe splice. I think I approved this, he's not on the call, but I think it was just the CI needs to get updated, No, I didn't approve this.
**Rafael Roquetto** 52:04 This one, it's a bit more, -Oh.
**Tyler** 52:07 Oh, yeah, this is definitely… Yeah. Okay.
Cool, alright. We'll wait on Nicole, he's out of office, so, yeah.
Also, Giuseppe, introduced the stats, Ollie, I saw this come out yesterday, I think.
**Giuseppe Ognibene | Coralogix** 52:21 Yo.
**Tyler** 52:21 some reviews, yep. I have… Giuseppe Ognibene | Coralogix 52:23 That's basically the whole op network tracer, which should solve the, extend the network matrix.
Rafael left me some comments, I think, that I… Did everything just, like, 10 minutes ago.
And Mario, the one question about the user configuration.
Yeah, I think it's the last one, yeah, this one.
**Tyler** 52:58 This one here? Yep.
**Giuseppe Ognibene | Coralogix** 53:00 I don't know if… what is in the rule? Yeah, I don't know if that was your question, but basically, I am planning to let the user configure… I mean, the granularity, it will be the metric.
Obviously, I just added one metric, so… It… It was not worth it.
**Mario Macias** 53:24 Yeah, yeah, okay, okay. Yeah, I was thinking in the future, If we introduce more… more overall… metrics that could go system-wide, I'm afraid that maybe we could realize it's some impact in the performance, or maybe all of the Enabling or disabling some of them.
**Giuseppe Ognibene | Coralogix** 53:46 Fortunately.
**Mario Macias** 53:46 For one metric, it's fine, but as long as we… Keep adding more and more metrics.
**Giuseppe Ognibene | Coralogix** 53:55 Yeah, yeah, yeah, I mean… after the merger, we'll start to work on the TCP field connection, so in that PR, I can just start also the… this… user configuration.
Okay.
**Tyler** 54:14 Yeah. Okay. That sounds good. So, I think with that, we're just waiting on more reviews on this. Like, Giuseppe said, I think there's been some updates, so yeah, please take another look.
Yeah, like I said, looking at the… Rails, Puma stuff here, don't need to look at it here, selectively replacing… Tracing programs, if the system supports them. This is something from Mario. Mario, did you want to talk about this one, or is this still something not worth taking a look at?
**Mario Macias** 54:47 This is currently, a proof of concept. I… Rafael previously submitted a poor, pull request, merge it to… to enable tracing… tracing programs as a replacement for K-propes for performance.
issue, reasons. I'm… I'm trying to, just to, get one K-Pro and replace it by a… tracing and see how it performs, but since K… since tracing programs are not available in all the systems, we need a way to… To specify both.
both programs, and let OB selecting with, between the K-Pro or, or the tracing program.
Depending on the availability of the… basically, the BPF trampolines.
It's currently just a draft work in progress, yeah.
**Tyler** 55:48 Yep, yeah.
Okay, well, cool, yeah.
**Mattia Meleleo** 55:51 By the way, just one comment here. I know it's still a draft, but there is one function that checks the availability of the programs in Celium eBPF.
It's the features package, and you can just.
**Mario Macias** 56:08 Okay, okay, okay, thank you. So this… we don't need this tracing enabler… okay, okay.
**Mattia Meleleo** 56:19 Yeah, maybe we can…
**Mario Macias** 56:20 Thank you.
**Mattia Meleleo** 56:21 that function in here. And it's also cached.
**Mario Macias** 56:24 Yeah.
**Mattia Meleleo** 56:24 to…
**Mario Macias** 56:25 Okay, great, great, thank you, I didn't, didn't know this.
**Mattia Meleleo** 56:29 No problem.
**Tyler** 56:34 Cool, alright.
This one is also ready to go, removing some unused functions, and global variables, this is from Mario as well.
It's got a bunch of approvals. Actually, I think this is probably ready to merge, unless people think otherwise. I think the… Main issue is that there's upstream dependencies on this one.
Which, I think the Bela folks are the ones… I see a thumbs up from Mattia as well, so…
**Mario Macias** 57:04 Yes, there is… please check this SQL… there is a function related to SQL. You recently added SQL, but I haven't found it… it is being used anywhere. I don't know if you plan to use it in the future, so I can just leave it.
**Mattia Meleleo** 57:25 No, it's actually hard, I tried to use it in the past when I added MySQL.
But it had some issue, I didn't use it. I wanted to delete it, because I saw that it's unused, but I left it there.
**Mario Macias** 57:37 Okay, so it's safe to… to delete. Okay, great.
**Tyler** 57:42 Yeah. Well, cool.
Let's, Okay, looks like the tests… .
**Mario Macias** 57:54 This might be the… huh?
**Tyler** 57:57 Yeah, that looks like… Sorry, this doesn't look like it's… Should be true.
**Mario Macias** 58:03 Okay, I will, I will double check.
**Tyler** 58:06 Okay.
Yeah, I'm guessing it's probably just a flake here, but yeah, we can double check that.
**Mario Macias** 58:12 Boom.
**Tyler** 58:13 And then this looks ready to get going in.
Okay, then last up, the RFC contributing, guidelines we talked about, and then the Enable Appali with, only Dynamics PID selector. This is something also Mike mentioned earlier. This is, to fix something, just came out. It looks like it just needs reviews.
Looks like it's pretty short as well.
Yeah. So yeah.
Mike, if you wanted to add…
**Mike Dame** 58:39 change.
Yeah. It's, basically just, you know, trying to test this out now and make sure that it works in code. I realized that the app OLLI instrumentation isn't actually, enabled unless you have, like, a broader selector that is passed to it, and that kind of defeats the point of the dynamic selector, of being able to say, I just want this PID. So, kind of explained it a little bit in there.
I am testing this, and I'll try to add some tests to this PR too, but, any eyes that people have right now would be great.
Not a huge rush.
**Tyler** 59:18 Perfect.
Okay, that's the end of the open pull requests, that we can go through. So, which is lining up really well, we got one minute left, yeah.
So anything, last comments before we jump off here?
Okay, well, it's good seeing you all. Thanks all for all the active work. I will not see you next week, but I will see you in two weeks, and to the folks coming in next week, we'll see you then.
**Rafael Roquetto** 59:46 CubeCon. Bye. Bye-bye.
