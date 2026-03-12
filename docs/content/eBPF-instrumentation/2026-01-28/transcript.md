SIG: eBPF instrumentation
Date: 2026-01-28
Duration: 64 minutes
Zoom Recording URL: https://zoom.us/rec/share/g6_1Eq3YbcAcevk0Ll_oQNoWEbWe3j-sA3M8X1sAVMp12QfK-Cz51OAeBRSNhbhh.25dB0j9KgY_YHgRQ
============================================================

## Zoom Recording Transcript

Tyler 00:00:44 Hey.
Stephen Lang 00:00:47 Great.
Rafael Roquetto 00:00:51 Hey, guys.
Tyler 00:00:53 Hey, how's it going?
Rafael Roquetto 00:00:55 Good, how are you guys doing?
Tyler 00:00:57 Good.
Rafael, what's the weather like up there?
Rafael Roquetto 00:01:11 Yeah… Could be better. It's like… It got warmer, because we had, like, minus 20, like, two days ago, and now it's… Yesterday was, like, 1 degree positive Celsius, and but yeah, there's notice melting, you know, it's that… that nice soup.
Oh, yeah. How about in your end.
Tyler 00:01:33 Real mess. Yeah, it's been pretty good. It's not been that cold, but it's been a little colder up here. But yeah, it's like the rain's starting to come back. We had a lot of grid break, like, sun, which is rare for the winter up here, so… Yeah, I can't complain. Heh.
Rafael Roquetto 00:01:50 Good, good, yeah. I'm starting to miss the green, the tree.
Pellared 00:01:53 Hello.
Rafael Roquetto 00:01:53 beliefs.
Tyler 00:01:55 Yeah, I don't think anybody would… Argue with missing Brazil, like, that sounds amazing, I… yeah.
Rafael Roquetto 00:02:02 Yeah.
Tyler 00:02:04 The only time I wouldn't want to be there is, like, when it's dead hot and super humid, but, man, during the winter, that sounds… sounds great.
Rafael Roquetto 00:02:11 Yep.
Tyler 00:02:13 Yeah.
Cool. Well, we can probably jump in here in just a second. If you haven't yet, please go ahead and add your name to the attendees list.
If you have agenda items you wanted to talk about, go ahead and add them there as well.
And, yeah, I'll start sharing my screen, we can start, start the meeting off.
Cool. Alright. So, yeah, welcome everybody. Let's jump in here. So, the first off, I wanted to talk about this binary distribution and, packaging plan.
This is something that we have on our 2026 goal, so I'm trying to work on this one. And, I've updated the description to have more of a breakdown of, like, a phased approach to Implementing this.
I just wanted to review this today. My, I guess, yeah, maybe I can start here. My goals for this one is to actually, like, get a review from you all and then start working on this. Robert has also, who's on the call, my colleague Robert, I think we met last time, is also wanting to work on this one, so I wanted to get some, like, feedback and make sure that, like, it's something we all want to pursue.
And then, yeah, I just go through and… build it out. So yeah, just to kind of break it down, like, these phases are essentially… Establishing… establishing some sort of way to, like, sign, our artifacts, so that includes the, multi-architecture binary distribution, but also our container images that we are currently, exporting. Double-checking on that one.
So… and after that, also including the binary distribution, so building that, in our release process.
The Phase 2 is then more about the auditability of our, supply chain and ensuring that, like.
all of the build processes are gonna be documented, as well as, like, what's included, the attestation of, like, our CI system, so any sort of, like, companies that require this sort of supply chain verification can, be provided it.
And then the last phase is a little bit more loose at this point, but it's more the idea of taking those binaries and then distributing them in some sort of APK, RPM, devs, that kind of thing.
There's a lot more details, we can go into here, a lot of high-level things around, like, what's included.
One of the things, maybe, that was called out before is this documentation. The goal is to always have, like, some sort of documentation on, even in, like, the Phase 1, how you would do these installs with the binary distribution. Currently, our standalone documentation just says to, like.
use the binary. It was pointed out yesterday that, like.
doesn't say anywhere how to get the binary, and so, yeah, I think that there's, like, some updates to the docs there. Obviously, like, once we have verification showing people how to verify things, and then, obviously.
Package manager stuff, like, yeah, include that in the, in the breakdown.
But if we kind of go down, you can see each one of these phases is broken up, with a lot of detail. The first phase has a lot more thought, just because I… plan on working on this next, so I think there's been more thought put into it.
And we can go through all of them, but I just wanted to maybe jump through this, this first, few sections here. So, essentially, what I'm planning to do is to update the releasing, Workflow, and make sure that, like, the binary that is, you know, being created, or create the binary using our standard, processes will actually get built. This is, a step for adding the cosign, keyless signing to make sure that, like, we're signing whatever we're actually gonna be, in… including… We're gonna, you know, name the binaries. I was thinking Obi, just because that's what we have in our docs.
But yeah, I'm open to, suggestions here.
then, all of these, like, checks and signing stuff needs to actually be, like, processed and uploaded before we actually do…
Pellared 00:06:15 Can we interrupt you, in case there's another one?
I'm looking today at it, I'm not sure if it should be compiled or artifacts, make artifact, make target, because it also has data agent, also, like, I think, licenses and notice files, and publishes it as, Starball.
Any thoughts on that?
Tyler 00:06:40 This compile target already exists.
Pellared 00:06:43 Yeah, yeah, I mean, but there's also Artifacts MakeTarget, which also builds the JVM agent.
The notices file, and licenses, which maybe should be published as well.
Tyler 00:06:57 Hmm.
Yeah, I think you're right.
So all that stuff needs to get included into some sort of, like, package that we're gonna distribute.
I don't know how you would include that in a binary, though.
Stephen Lang 00:07:16 Yeah, I think at least the Java agent needs to be shipped alongside.
Pellared 00:07:20 Was it?
Stephen Lang 00:07:21 As a separate jar.
Otherwise, if you try and run… OB, it might complain that the jar, doesn't exist in the same directory as the binary, at least when I've tried it, on a standalone machine.
Pellared 00:07:38 is, for instance, in .NET, we are basically in GitHub releases, we are publishing, like, parables or zip archives.
And the things inside can be simply signed.
Tyler 00:07:50 Hmm, okay.
Stephen Lang 00:07:54 Right, so it might not be a case of actually signing the binary, it might be a case of signing the compressed archive.
Pellared 00:08:00 Both, probably, needs to be signed.
I think it's Make Artifacts.
Tyler 00:08:13 Oh, sorry, thanks.
Okay, thanks. Yeah, that's… I see what you're saying now. Okay, that's helpful.
So I can update that afterwards?
Naming-wise, though, I think that that seems reasonable. I don't know if there's thoughts on that.
Okay, and then… yeah, so, binary distribution, this is included in the… Immutable release, that's something we want to make sure that is not changing.
Includes all of our artifacts. These would be the TAR zip files that we've just been talking about.
Kind of an ups… or an idea of how to actually do that in our workflow. This isn't final, this is pretty hand-wavy, but yeah, it's kind of the idea.
And then, last, if we have cosine set up for our binary images, then we could do the same thing for our, Docker containers as well.
Yeah, and then the last thing is just documentation, documentation of how to use this verification, documentation of how to, like, actually, you know, download this, binary from the releases and tell people how to do it.
Cool. So, that's a lot. I think that then next to the idea is to, jump in and, talk about the security stuff for Phase 2 or Phase 3, but I think maybe we can pause on that one.
If folks are interested, I would ask that maybe you go ahead and take a look at this. This is just more about, like, a high-level thing of potential things to include, for attestation of, like, this, supply chain.
Package, Phase 3, high level, again, just talking about how we would want to provide APK devs, and RPMs. This is pretty, ambitious in saying that we would want to get these into main distributions, but that's probably not going to be the case. But yeah. Go ahead, Steven.
Stephen Lang 00:10:20 Yeah, so do you have something with the, the pipeline where you're doing this, the checksum creation and, you know, the package creation?
you really want something at the very beginning, which is doing the testing and verification of everything as a prerequisite, because I think right now, the release is independent of all the CI checks that we have on every PR. You know, we have on main these CI checks that run.
But technically, you don't have to wait for those to pass. You could just push a git tag, and the release would happen anyway, even if we had a broken build.
So it might be that you want, as part of your process, either to re-run the entire test suite, or to have it such that the release Only occurs if there's some kind of dependency on the existing, you know, commit in main having passed all of its workflows in some way.
But either way, to create a, you know, a verified and validated release, you need to somehow assert that that commit hash has had the entire test suite run against it.
Tyler 00:11:21 Yeah, that makes sense. That's a good point. I'll keep that in the notes. That's definitely something to keep in mind.
Yeah, another thing that we could probably also.
Pellared 00:11:32 Also, one thing… Which I also remember was important, and… and basically slaped us a few times.
When we made, when we make a draft release, we already have the artifacts. They are not signed, but they are published, and before making it published, we could have some automated, basically, some automated tests, which basically checks if the correct artifacts were published.
It's like double-checking, but in case we publish the wrong stuff, there's no way to, you know, there's no way to basically remove the artifacts, which were already signed, etc.
Tyler 00:12:16 So I'm not following… so, like, the release workflow would upload the artifacts, but then it would immediately download the artifacts and verify them?
Pellared 00:12:22 Yep.
Or maybe just checking, or maybe it's not necessary, like, checking If we have at least the correct count of the artifacts, something like… something like this, just double checking.
But yeah, maybe we'll consider it later.
But for sure, publishing it should be manual, that the GitHub workflow should make it, you know, leave it as a draft.
And something… I think someone should manually, you know, publish it, you know, so that it's being signed some maintainer, in my opinion. I don't think the automation should, you know, publish and Publish it. You should just make a draft.
Not PR, draft, draft report.
Tyler 00:13:10 Yeah, sorry.
Pellared 00:13:13 And the maintainer will just, you know, interact it.
That will be good enough.
Tyler 00:13:21 Okay.
That makes sense. Puts in a little bit of a gate, that helps.
Yeah, okay, that makes sense.
one of the things… the thing with the… Steven, with your test passing, one of the other things is we could also require tests to pass for the PRs to be merged.
I thought we did…
Stephen Lang 00:13:46 We do, we do have those as a PR requirement, but that's correct.
Tyler 00:13:50 Okay.
Stephen Lang 00:13:51 Yeah. But that's not to say that you might… have two PRs, merged.
Within a very short period of time, where together in main, it can cause the tests to fail for.
Tyler 00:14:03 Oh.
Stephen Lang 00:14:04 You know, say one updates a dependency and another… is dependent on the previous version, and then the merge causes it to… this new feature to fail that wasn't tested on the other PR.
So that's why you need… you need the gate in Maine itself.
Tyler 00:14:18 We don't have linear history, is the problem.
Stephen Lang 00:14:21 Correct, yeah, I think it's maybe in the repo settings, you could, if you wanted to, you could explore, well, it's not the linear history, it's, forcing the PRs to be updated with main before they're merged.
Tyler 00:14:31 That's, yeah, that's the same, the linear history meaning that, like, the parent of anything that gets merged has to be main, so it has to be up-to-date before it actually merges. We have that in a lot of other repos. I noticed we didn't have that here just to get things moving, I think, but it might be worth exploring.
But… I don't… I mean… I've got this down as an issue. I'm gonna keep looking into what the solution is there. I think it may just be, like, what you're saying, just verify that what we are releasing, what is tagged, actually has the CI system Passed already, and then if not, then work on that, yeah, but… I'll… I'll take that under advisement, though, I think that's a great idea.
Okay.
Alright, I'm gonna… comment this and, pause there. So, yeah, planning to kick this off. I don't see any, like, major opposition to, the design or the idea. Obviously, like, the feedback I got has been great so far, so, like, let's keep going with that. If you have more, please go ahead and comment on this issue.
But otherwise, yeah, probably just start digging into this later in the week, and yeah.
Cool, so up next, Robert, you wanted to talk about, An epic to improve the integration test quality?
Pellared 00:15:52 So, I created… I had a conversation with you, Tyler, yesterday, and also today with Steven, like.
even, an hour ago. So basically, oh, geez, I… I have to not improved, okay. So, basically, when I looked at the repository, I saw a few things that could be improved in the integration test. So, basically, this epic is just about improving the things that In my opinion, hopefully, will be not just about, you know, just improving for the sake of improving, but to just increase, basically, the developer velocity by improving the test speed.
making it more stable, making it more maintainable, to give code reusability, so that we are not copy-pasting the Docker-compose files, also to reduce number, like, the dependencies that are used.
And yeah, basically, here's the example test, the goals. We also plan to… so together with Stephen, we plan to work in an interactive way, not… and in an interactive, also, not saying that, we'll refactor all the tests.
When we have an idea, but we'll just take a few tests, and we'll try to check If it actually helps, and then when we establish some patterns, then when we will be very sure, then we will just propagate it further, but probably first we will just try to find as much as possible good patterns, basically, based on a few tests, and from the integration tests, from the Kubernetes test, which is the kind, and also the old test. We will probably try to have some common solution, common patterns, instead of having, you know, like, different ways of of testing. That's our proposal.
And doing probably as much as in a Go way as possible, so that it's easy to debug and develop and code reuse, and as less external dependencies as possible.
Any comments on that? Stephen, do you want to add something to what I… Described.
Stephen Lang 00:17:54 No, I think you covered pretty much everything. Yeah, the main goal here is to, improve the developer experience of the integration test suite, which is massive. There's also a huge amount of code duplication. Anybody that's developing a new feature has probably experienced copying and pasting vast amounts of YAML files, etc.
what Robert's suggesting is to move some of that to be, instead of very much declarative with the massive amount of YAML files that we have right now, but to be more imperative and code-driven, with the main goal of being able to reuse this code amongst different packages.
Which I think is a good thing, because right now, with the amount of duplication that we have, it's very easy to introduce, you know, a change to one part of the test suite and not have it be consistent with the rest. It's very easy to miss that kind of change as well.
So yeah, having that code extracted out and reused as much as possible.
Can mean that, you know, we're sharing the learnings as we're reducing the flakiness of the test suite.
And it can help new features to be developed with a much lower overhead of scaffolding of integration tests. So I'm all for this.
The other part of it is it has potential to, reduce the length of the CI integration test times in the long run.
For now, as Robert said, it is a bit of an exploration in terms of experimenting with different approaches.
So, I think he's taken maybe 4 tests, and has, you know, ported them to DockerTest.
But maybe that isn't the final approach. You know, maybe he's going to experiment with some other different approaches, and effectively, whatever wins, we can then use that and apply and refactor to the entire test suite.
But yeah, there's certainly areas where we can highlight Where maybe entire test suites are duplicated at the moment. You know, look at the OATS test suite versus the integration test suite.
You know, when should you use which test suite? You know, what are the, as a developer, you know, where should we be adding tests, and where, and, you know, what's the overall coverage? So, yeah, I'm, Thank you, Robert, for bringing this, onto the agenda, and I think it's… I think it's a great step forward.
Marc 00:20:01 Yeah, so I saw that you're… you put here, like, refactor, right, the subset of oats test.
Doesn't mean that, rivania… Like, eventually move to use-only-outs test, or… Or…
Pellared 00:20:18 Or the other way around, maybe. Maybe not using codes, just using the approach we'll do here. We would explore these things.
Marc 00:20:27 Yeah.
Okay, I mean, it would be great to analyze the trade-offs, because, I think the oats is something that was internally developed in Grafana, so maybe there was a reason to… to… Yeah, that we start using that.
Mario nose, yeah.
Mario Macias 00:20:50 Yes, it was, theoretically to save time, but we… we started, but at the end, we… we always went faster with the other integration tests. Just one, point is that these oats… is, or is… is being discussed, is donation to OpenTelemetry. So maybe at some point, this… not this current notes, but some… a newer version becomes official from OpenTelemetry. That doesn't mean we are forced to use it, of course.
But… Yeah, maybe at some point the hotel community finds it useful, and it becomes more ubiquitous.
Pellared 00:21:38 Also.
if you have, we have this epic, so if there are any concerns, any proposals, any pain points that you have, then feel free to write it down and run here, or whatever you want. This can be, you know, just even a brainstorming place.
Mario Macias 00:21:54 Okay.
Pellared 00:21:55 Gathered… gather feedback was… was not working.
Mario Macias 00:21:59 Okay.
Thank you.
Tyler 00:22:03 Awesome. Robert, can I assign this to you and Steven?
Pellared 00:22:09 For sure.
Stephen Lang 00:22:10 Yep, fine.
Tyler 00:22:15 Awesome.
Cool, yeah, this is great. I'm… I'm really excited about that. I think that all the… yeah, the improvements that this can bring would be awesome. So, thanks for bringing this up, guys.
Pellared 00:22:25 You can also add to in progress.
the status in.
Tyler 00:22:29 Okay, thank you.
Okay.
Awesome. Next up, Rafael, you want to talk about, BPFFS?
Rafael Roquetto 00:22:40 Yes, hi. So this actually relates to, Matthias' proposal for, sharing PPF context. I don't know if you guys saw that.
Which is, pretty cool.
The… the way… I mean, for those who haven't seen it, and maybe Matia can correct me if I miss any details, but basically, it… uses a map to share the trace ID and span ID of a given thread at any point in time. So this allows, for instance, the EVPF profile to correlate, a given stack with a given, you know, tracing span ID. So that's pretty cool.
The thing with that is that… For this map to be shared, it needs to be pinned to a path, so… I mean, I guess everyone here is familiar with how eBPF maps and pinpaths work, but for those who aren't, basically, it just associates a file path to an eBPF map, which allows another process to open that same map, and then they can share, information. So… personally, I think this is the way to go, and… and really simple and clever in performing implementation, but it requires VPFFS, which is something we had removed in Bela back in the day.
Just because it, you know, it… it used to be a security burden, you know, configuration burden, they were… we got rid of that, but now I think… it makes sense to reintroduce it. So, in the discussion that we've been having, yes, me, Matia, and Florian, we are, talking about, the, the path. So, I just wanted to… I thought it would be easier to just discuss this here than back and forth in text. We can summarize this in text afterwards.
So, what's being proposed is that we would… pin the map to slash C slash FS slash BPF, map name. That is the canonical, path for BPFFS, where it's mounted.
But what I wanted to argue is that this is not enough, because… There are different distros that use different mount points for BPFFS.
Like, for instance, bought a rocket… now I was trying, like, I was digging and trying to remember why we did it like that. So, bought a rocket, I guess, will mount it to… somewhere else, like, slash var, BPF, and the reason for that is in the… as far as I know, and please correct me if I'm wrong, because I'm not the most, well-versed guy on this.
The, C's directory sometimes is, is, you know.
It needs to be constrained, like, security-wise, like… Sometimes you have App Armor policy that prevents it from being written, you know, you don't want people messing with that. So, it appears to me that it's fairly common for when you need BPF, FS in containers that, or even outside of containers, outside of Kubernetes environment, that you will lock down CSFS and mount BPFFS elsewhere, in VAR or anything else. So that… that is why I don't think we can actually hard code Or based on the assumption that BPFFS is always going to be, like, sys, FS, BPF, it should be, in my opinion, configurable. That could be the same default.
But we need to offer that, option to the user, which kind of sucks.
In a way, because I see the argument that, you know, you need… if the EVPF provider, for instance, or anyone interested.
on… on that map, we'll need to agree on the… on the… on the mount point for BPFFS, but I don't… I don't know if we can just default to… assuming it's always going to be on CIS, because that has, in the past, not always been the case.
I don't know if there's a better way of dealing with that.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:26:55 Yeah, I want to echo that. I mean, we started with, when we first implemented this in Bailout, it was on a CISFS VPF file system, and then… there were a number of issues. I think, I mean, originally, David Ashpel actually donated that code to Bela that made it configurable, this pin path, where it should be… because there's issues, like, I don't know, with GKE, like, if it insists, you need special permissions to mount these things, and… And so on, so it's easier to kind of have the path configurable. This unfortunately means that If it's going to be used by the profile, it also needs to know where this is, so… Which is a… Absolutely the second point, but… I think we should default to CISFSBPF, so it's the known location, and provide the option to… choose where to go, at least from OB's side, that's configurable.
Rafael Roquetto 00:27:48 I don't know.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:27:49 Oh, just…
Rafael Roquetto 00:27:51 I'll just add one thing based on what you said, Nicola, which is, this also allows us to, like, because the older builder documentation that I pointed in the discussion talks about unconfined containers and… or modes in Kubernetes. This allows us not to do that, because you can still have a confined, container.
or whatever, which will prevent accessing SysFS, but you can have a special rule for BPFFS mounted out.
somewhere else, so that… that kind of gives us regular permissions as well, more flexibility, so… Yeah.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:28:24 So, that's… that's a very good point. The, the thing with, this also… Dave Asheville did for… for that initial, The change he made was essentially, if… If this was in SysFS, then the default app armor policy does not allow you to access that.
The other thing, the default app armor policy does not allow you to mount any volumes, which prevents you, even if you had a custom path, but I think he had a workaround in our scripts with an init container that mounted it correctly.
it was passed down to OV, or Bela, right, at that time. So, allows you to play that trick. So, you can actually add an init container that specifically does the mount.
And then you can actually make that one run with higher permissions, with privilege, but that one dies right away, and then you don't have to have privilege on the… on the OB container, going forward.
So the only way around the app armor is if you have a privileged container.
Mattia Meleleo 00:29:30 I have one question.
Which is, if we make this configurable, we have to also make this configurable in the profiler, right?
And, they should, have the same config, basically.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:29:44 Yeah, so… But first step, we do it so that we can support this and default to SysFS, so then it's not actually… doesn't have to be changed on the profiler side.
To add this option, and then we work there to figure out what we can do.
Mattia Meleleo 00:30:01 Would that work if we make, like, a list of fallback paths, hard-coded fallback paths, instead of having it configurable?
Tyler 00:30:13 I would recommend.
Rafael Roquetto 00:30:14 It would work until someone points…
Tyler 00:30:17 I think it would be a good idea. Yeah, so I was thinking the same thing, Mattia, like… I think that having SysFS sounds great, and then having fallback paths that Raphael's already identified. You don't need many, maybe, like, 3, or maybe 2, I don't know. Like, having a standard, right, and put that in, like, the OTEP, and then if none of those are found, give up, but I think that you should also have the ability to have a user come in and say, like, hey, I also, like… I don't like any of your decisions, because, you know, maybe my situation is very unique that you didn't think about, and here's how I would resolve it there. But yeah, I think… I think the 80-20 principle is pretty important here, and I think that, like, SFS is probably gonna handle most of it.
And that, like, if you can just default to, like, you know.
you know, forward slash var or something like that, as, like, it's gonna… I'm gonna get another 80% of the last 20, right? Like, you're really… you're really getting most of it, and then the customizability's gonna cover everything, right? So it's just, like, graceful degradation when it doesn't actually met work is, I think, more the question of the… the issue here, but yeah, I think all the above sounds great.
Mattia Meleleo 00:31:22 Yeah, I was mostly worried about the, the bugability of this, if, for example, Profiler has a config which doesn't match the Obi-Wan and the… yeah.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:31:32 Yes, sir.
Mattia Meleleo 00:31:32 But I get your point, yeah.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:31:35 It's a really valid point, yeah.
Florian Lehner 00:31:37 I think it's fine to just use the default sysfp by default.
Make it this path configurable, so someone could override it if needed for whatever reason.
And then, have a common shared name for the map.
So, and the full path, then, for the… for the shared map, contains the SUSEF as part, or, respective configuration, configuration, and the map name. And, yeah, making the configuration for the… sysfpf is, I think, no, not a big issue also on the profiler side, it's just a configuration option that we have to add.
Mattia Meleleo 00:32:20 Okay, sounds good. I will, I will then update the audit.
Tyler 00:32:27 Awesome.
Cool. Rafael, was that, the extent of the BPFFS, conversation? Yes.
Rafael Roquetto 00:32:34 Yes, and feel free to redirect any builder code that you, That you'll see fit on that old PR.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:32:45 Absolutely.
Tyler 00:32:47 Okay, last up, we haven't done this in a little while, I wanted to jump through open PRs just to make sure that we don't have anything that's, waiting on folks, and so, yeah, I wanted to jump in here.
So, start us off, Mark, I… the Python AsyncIO PR is still open. Is this something that you need some help on, or, still a work in progress?
Marc 00:33:07 Yeah, I have a… an update here, because I created… one second… Yeah, so…
Rafael Roquetto 00:33:16 Life in Berlin, life in Berlin.
Marc 00:33:18 Exactly.
Yeah, so… yeah, so I was, trying to expand the support, because this was working, we managed to make it work for you, UVCORN, everything is called, and I was trying to make it work with UV loop, which is another implementation of a Sync I.O, and yeah, so I started to derail a bit, and… And everything that you've tried to… fix is a can of worms, so now I'm trying… I open, like, like, apparent, issue to track different implementations of the Sync IO framework.
And this is gonna be just for the… Simple scenario.
Which is a Cincaio, and then we want, at the follow-up request for UBCON, and… Potentially for UV loop as well.
Yeah, because it's… they have… they work different, and… And each task requires a bit of, yeah, investigation and… And I don't want to add everything in one sample request, because… It's gonna be hard to review and… implement.
Tyler 00:34:37 Yeah, I think that sounds like a great idea, to split it up the way that you've done it here. So, yeah, let's… let's do that.
So, if you're gonna scope this PR…
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:34:47 Yeah, I have a question. Do we wait for an update from you on this pull request we will review, or is it good to review?
Mark.
Marc 00:34:57 Can you repeat?
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:34:58 I was just asking if the scope of your current pull request, is it this first… to handle just the regular iSync.io? Should we start reviewing that, or you have some new commits that you want to push back, or revert some of the changes?
Marc 00:35:14 No, it's not yet ready to review, because I'm running the integration test, and…
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:35:20 Okay, yep, makes sense.
Marc 00:35:22 I'll let you know when it's ready.
Thanks.
Tyler 00:35:26 Okay, perfect, yeah, that'd be great.
Okay, next up, Rafael, there's an IPv4 option code, PR. This is, from December.
Rafael Roquetto 00:35:38 Yeah, I will need to… I completely forgot about that, to be really honest. I will, revisit it, make sure it still applies. I think Mario has a comment. I'll pick it up, and then I will rebase it, or close it. You guys will see. And then if I rebase it, you can review it. Again, if I close it, it's gone.
Tyler 00:36:00 Perfect. Awesome, yeah. I know the holidays, it gets all confusing, but… Yeah. Okay, add config JSON schema generation, Nimrod, I think this is you.
Nimrod Avni 00:36:11 Yeah, I just, rebased it today. There was a bit of discussion there, and it stopped.
I don't know if that's, like, the path. If someone opened an issue a while back that we don't have, like, any schema for our config, and they did something that kind of generates it automatically, and I think you opened another issue on that, of, like, describing the config in a more, like, declarative way.
If that's, like, the… like, the path… if you think this is a good path, I just saw there's some… small, like, CI issues, I can fix that.
basically just, you know, looks at, like, JSON schema annotations, added a bit of, like, custom annotations, and it generates a pretty good picture of, like, valid schemas, you can, like, take this, go to, like, some JSON schema generator website, and it'll create a mostly valid schema. We might need to fix, like, a couple of fields, but it mostly relies on, like, if we have, like, strong typing, it will work, but sometimes I've implemented, like, specific JSON schema for specific fields that are, like.
Kinda, very custom in the way they serialize, and they serialize, strings, and, like, the config.
Tyler 00:37:36 Yeah, this is awesome.
Yeah, this is great.
I think this is gonna resolve that issue that you're talking about. Yeah, I think it… God, there's so many cool things I think we could do with this, dock-wise, as well as, like.
providing validators for folks, so yeah, I think this is awesome.
Okay, this is, like, ready for review, if you'll…
Nimrod Avni 00:38:00 None.
Tyler 00:38:00 Okay, yeah, so looking for reviews on this one. Okay, then I'll try to add this to my list of things. And, you said the CI is a little flaky?
Nimrod Avni 00:38:08 Yeah, something with the notice, something with… deleted notices, maybe. I… I just, merged it, so… I need to check if it's my issue or, AI.
Tyler 00:38:22 I see. Oh, yeah, there's definitely some weirdness there. Okay. Well, cool, then I'll… I think… I think your content is still worth review, so this is looking for reviews, is what you're saying, so… Okay, let's… let's do that.
Okay, short update, go, dependencies, don't have to talk about this one. Oh, wait, this is not a renovate bot.
This is probably really outdated. The SEMCOM, up… grade, also, yeah, upgraded a lot of this stuff, just because we needed the latest version of the hotel package to make this work.
Mario Macias 00:39:02 Yeah, I think recent ver- we are in, currently in more recent versions.
Tyler 00:39:09 Yeah… I'm gonna… I think I'm gonna close this. I think this might actually be already done, but… Yeah, okay.
Okay.
Cool. Okay, inter-service, context propagation, documentation. Oh yeah, this is something I was talking with Robert about yesterday, actually, on this one.
I… I left some comments on this, and .
Nimrod Avni 00:40:25 I think I tagged Nicole on a couple that I… I'm not super familiar with, maybe… mainly the Java and V stuff.
If, like, some of my stuff are accurate. But I think, like, regardless, it's, Like, at least someplace good to know what, like, async frameworks we support.
Tyler 00:40:47 Yeah, I… I agree, like, I think that we, like, having something here is great, I do think the structure could be improved here, but I'm also kind of in the camp of, I think, maybe just getting this merged is more important than, like, we can go back and refactor it, But, yeah, maybe… I think, actually, since we've got a little bit of time, Here…
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:41:12 No.
Tyler 00:41:12 Why don't we…
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:41:13 Yeah. Yeah, get out of the way here.
Nimrod Avni 00:41:16 Live, live review. Yeah.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:41:26 Yeah, I think you're right about Java, yeah, that's… thread pools work, yeah.
Tyler 00:41:32 Version-wise, though, I think this is…
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:41:36 All versions.
Nimrod Avni 00:41:38 All versions?
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:41:39 Yeah, I mean, JDK8 is pretty much, but… You can say JDK8 and above, but… I mean, for general world, like, I don't think anybody… supports anything below JDK 8.
I mean, I have famous last words, but yeah, okay, fair enough. Yeah, I think, yeah.
Yeah.
Tyler 00:42:05 Okay, and then… gosh.
Is this… this is one that I didn't realize we had this limitation with 3 nested levels of go routines. Is this something that's… True?
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:42:18 Yeah, that's right. For… if a goroutine is launching another go routine, another go routine, we go look up the parent chain up to 3 levels.
Tyler 00:42:27 Up to 3 of those, okay.
Mario Macias 00:42:28 Is this configurable? I mean, I guess this is a loop with a number, a 3 somewhere, hard-coded, you can set…
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:42:35 That's right, it's hard, yeah, it's hard code. We can make it configurable. It just takes, you know, a couple of minutes now that we can put one of those volatile consts and configure it on the probe launch.
Yeah.
Tyler 00:42:51 Yeah, I also think that we could wait for a user to ask for it, too. I think this is probably… it's documented, I think, is the more important part, so from, yeah.
The Ruby stuff… Nikola, do you know if the… like, I've seen web breaks also work, in, like, a test that I did. Do we only test against the Puma server, is the idea, though?
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:43:14 Yeah, I only tested Rails, and it comes with Puma. I don't know if this thing… whatever you said, WebRec?
puma underneath the covers, I think it's the most… kind of used…
Tyler 00:43:26 I see.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:43:26 what do they call it? Reactor framework?
For building in Ruby, I think it's the only one that does that advanced sort of threading thing.
Tyler 00:43:38 Yeah, okay.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:43:39 It's… I mean, typically, this is what Rails… if you install Rails, it comes with Puma, and I call it Puma because that's where the actual instrumentation is.
Tyler 00:43:51 Okay.
So, it may be more, but I think this is a good place to start, is what you're saying.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:43:55 Yeah, so there might be more that use the same framework.
Tyler 00:44:01 I gotcha.
And then the other one that I had on here, I had put C++ in Rust. I think Rust is something we're still trying to tackle on the async.io, but, like, the C++ stuff, it seems like that… Works from my testing.
Nimrod Avni 00:44:18 I'm not familiar with, like, any, like, asynchronous-type framework for.
Tyler 00:44:24 Well, that, yeah, sorry, we've been That's why I think it works, because I don't think there is, like… I think it's, like, you can maybe do some weird threading stuff in there, but, like, yeah, so that's why, like, if we're talking about context propagation frameworks, like.
I just thought maybe we could just add C++. I don't get maybe it's not a framework. Oh, I see what you're saying, so… Yeah.
Nimrod Avni 00:44:42 Yeah, like, for Python, we can also add stuff, like, that are not async, and it works, like, I don't know, Flask or something will probably work We can document it, I thought, like, we should work the document… I think I've written above that by default, we use, like, the same thread, and if everything… like, if you're running, like, a single-threaded request, it will, by default, work, besides these special cases that we support.
Tyler 00:45:09 Okay.
So… I see, okay.
Rafael Roquetto 00:45:12 I would point out, I sent a link on the chat for BoostBeast. I think if you want to clean C++ support.
We should try that out, because that, that is the, popular C++ framework, and probably one of the canonical ones, just like, Puma.
Tyler 00:45:31 Okay.
Rafael Roquetto 00:45:33 Yeah, wonderful.
Tyler 00:45:34 That's helpful.
Rafael Roquetto 00:45:35 I think.
Tyler 00:45:37 To Nimrod's point, we could probably… add testing to that, but maybe for this PR, we can avoid it, but yeah, that's actually really helpful, Rafael, to know that that's probably the one we want to do verify, though.
So yeah, let's, let's do that.
Nimrod, I would also say that maybe we could… update the name of the section, just to be a little bit more descriptive that it's about, like, the async frameworks? I guess you have frameworks in the title. I don't know, I was confused by this, but maybe that's just me, so…
Nimrod Avni 00:46:04 Yeah, we can maybe do, like, a synchronous runtime support? I don't know if you have a better name.
Feel free.
Tyler 00:46:14 Yeah, I can, I can think about that, but, okay.
Okay, I will… I will take another look at this as well. I'd like to get something like this merged. I was looking for this documentation yesterday, and I totally forgot it hasn't been merged yet, so it's definitely… it's needed, so I appreciate you putting the time in for this.
But we can move on in the PRs, unless there's other folks who wanted to ask a question about this one.
If you haven't yet, you've already done most of the review on this, so, maybe also go and… Take a legitimate review, it would be helpful to move this one forward.
Okay… This is a RenovateBot one, let's skip that. Invoke to detach together with close. Mario, this is a draft, is this something we need to talk about, or is this still…
Mario Macias 00:47:02 It's… I found a bug, I reported a bug last week, when, for example, you have an ephemeral or a crashing.
process that is continuously being re-instrumented. There are some BPF links that are left there, and are never removed.
Until you… until you, kill OBI. I was suspecting that, it… I find in… in some VPF probes, we are calling detach, and in others, we are calling close, and I was suspecting that maybe not invoking detach, or not invoking Close.
will… will cause this issue, so I create… I… I just modified, a bit the interfaces to make sure we, we invoke two. But, after… after testing it, I didn't find… or, I mean, it didn't solve the issue.
So, yeah, I will give a second… I will, yeah, I will be… I will give a second… view, but probably I will close it.
Tyler 00:48:16 Okay.
Yeah, that's… it's, interesting, okay.
Okay, then I will, leave that one there.
Next up, Robert, you had DockerTest instead of, Docker Compose, OTil, or, yeah, and so… I don't know if Robert's still on the call.
Pellared 00:48:36 Yeah, I am here, yeah.
Tyler 00:48:38 Okay, cool. Looks like Steven has, check marks here… Yeah, this looks good. So this looks like it just needs, another review, right?
Pellared 00:48:50 Yeah, someone can take a look.
Tyler 00:48:53 Cool.
Yeah, I can, I'll put this on my list as well, for things to take a look at. So yeah, thanks, thanks for this one. This one's great. For those that aren't familiar with this, this is switching from all these Docker composes, to using the Docker API itself in Go, which has a lot of benefits, in comparisons, and Robert's done a lot of that.
Information is here, if you're interested.
worth questions, I guess.
Rafael Roquetto 00:49:15 Does that… does that still keep the Docker files?
I haven't seen the PR.
Pellared 00:49:20 This one removes one of the Docker files. So, basically, this refactors 4 tests which use one Dockerfile.
Rafael Roquetto 00:49:31 Not the Docker files. It removes the Docker Compose files.
Pellared 00:49:35 Yeah, yeah, you're right. You're right, sorry.
Stephen Lang 00:49:37 No, so it still builds the same images, but it's not using Docker Compose to orchestrate them. It uses the Docker API directly. So it's the same, like, runtime architecture, it's just that we're using code.
to start up the containers, rather than Docker Compose.
Rafael Roquetto 00:49:53 Okay, so the YAML file goes away, then. I should look at the PR.
Stephen Lang 00:49:56 Docker Compose YAML file that goes away, if we're building our own image with a Docker file in the repo, that remains the same.
Rafael Roquetto 00:50:04 I see, I see. The, one thing, I'll comment on that, and I'm not sure in the PR, don't get me wrong, it's… so, sometimes I find it useful to mainly launch those, Docker Compose files when I'm, you know, debugging tests.
So I don't know if that impacts the bugging, or if there is another way. So what I usually do, like, when, for instance, there are tests failing, and I want to reproduce them, and I don't want to just run the whole suite, or I want to set up the environment.
And play with it. I usually start from this Docker Compose file. I might… replace Obi with a… locally built version, you know, a different image, I tweak it a bit, but then I manually launched the Compose file, to… to debug it. I don't know if that… that would still be possible, maybe I can just… Run the test, and the test will leave the environment for me up, you know, like, instead of cleaning it up, something like that.
Otherwise, we lose that debugging ability. I don't know how important that is, maybe it's just me, but just food for thought, I guess.
Mattia Meleleo 00:51:12 I basically do the same, so I quote.
said, I comment out the teardown of the Docker Compose file, and I run the test, so I have the whole environment to debug.
I don't know if this is replicable with this approach.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:51:27 Yes, same here, same here, yeah.
Pellared 00:51:30 Okay, so…
Tyler 00:51:31 I think this is…
Pellared 00:51:33 Let me jump in here, because I had feedback, because basically, in .NET Automatic Instrumentation, where I'm also still a maintainer, but yeah, I'm not doing a lot more there, we were doing similar stuff.
So, basically, the workflow initially was someone wanted to add automatic instrumentation, they created Docker Copost for debugging development, and then they just copied almost the same Docker Compose file, and they used it, you know, for sake of integration tests.
And basically, the build time was even worse. Before Steven refactored, it was taking more than 4 hours.
Because we had so many to compos. So, so we started to work on it, and basically, we reached a similar setup like I'm proposing here.
And the thing is that, once peop- there are… so there are two things. First of all, if people basically had some idea about what they want to implement and instrument, basically.
They often even started by writing this quick integration test, and just, you know, and using it for even development and debugging. If they didn't have a need, because usually these tests were just being executed, like, in 20 seconds.
So… but if they needed more debugging, they needed to… and also, if you put a breakpoint, nothing is killed.
So, basically, they… so, even during development, they sometimes just, you know, put a… they just, you know, set up this integration test, they just made a breakpoint after the test is set up, and they started development, debugging, and thinking things.
So this is one approach. And the second one is that instead of having this a huge amount of Docker containers. I think I can share my screen. There's just one Docker Compose.
Or they used to be.
Which was meant for… which was meant for development.
Let me check if it's… you can see my screen, right?
Oh, Jesus, I'm drawing something.
It is… so there we have a death, and basically we had a special docker and Compose, which was basically just spinning up a collector contrib, and a Jaeger.
And also, even the collector even has, basically, metrics. So, basically, we want… so, basically, we're just configuring, you know, the auto… we're just doing everything on our host, you know, And when we wanted, for instance, just to, you know, work on instrumenting, I don't know, MySQL or whatever, we just separately created a MySQL container.
on the same network, for instance, and we were just using this one Docker Compose to make sure that, you know, our telemetry is getting there and playing manually, and that's basically everything we needed. We didn't need to have, you know.
a Docker Compose file for each… for each setup, because just adding, you know, one, one additional container to debug was good enough for us.
I don't know if it answers your questions or not.
Rafael Roquetto 00:54:42 I feel like I have to look at the PR and digest it, and understand.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:54:46 So, yeah, so we do something similar, I want to say, at least from my workflow, is when I… kind of try to build a new instrumentation, or try to figure out what we generate, and what kind of labels I need to test for, and things like that. It's really helpful to just bring something up, sort of not even run the test. And I messed with it myself.
turn on different options, environment variables, and… I'm just describing my workflow, sorry, not saying this is bad. And then… then… and I can… when I run it as standalone, I can just open up the port and open the Prometheus, see what is stored, and I'm like, oh, okay, this matches what I wanted, or this doesn't, it picked up this, why did it pick up that? So I use it for debugging, for… And if something that kind of runs and shuts down, it's kind of difficult, right? Because then it's going to fail, but then I have to keep on adding debug messages. So if there's a way to stop… run it and kind of leave it hanging, that would actually be similar to what we need.
But also, we do, in the OATS framework.
The way Gregor designed it is, like, you have these templated files.
And then… what it does, I don't know, I think it's different than DockerTest, I think I know it's… what he does is actually allows you to write a template, so you don't actually have to copy everything over. It's composable, you can kind of bring in your… your collector components and your other stuff, and then what the test framework actually does is combines them both, spits out one Docker file, and runs the test on it.
But then the Docker file that is spit out ends up in a temp kind of test directory locally, so then you can just run it manually. So you kind of, like, get the best of both worlds. Runs the test.
But then you can go back and see what it generated at Docker, boot it up, mess with it, check what it was, and so on.
I can show you. I was recently debugging something.
See if I can… This is serving… So… Let me see if I can zoom this a little bit. So, in the test output.
No results, it's fine.
You know… So if it will be in the build directory, it will produce the final YAML file.
that it generated, but the actual files have, like, a generic template, which brings up all the collector and Prometheus and whatever.
And then he sort of combines it. So you can write sort of subsets of just the stuff that you want to… Plug in with the different options here.
I don't know if this helps, but… Just saying.
Pellared 00:58:00 Thank you.
So, just one clarification, just quickly, I'll just… but really very quickly. So, one of the approaches that, for example, people were also using I think I can find it here, but I'm not sure if I'm… yes, I'm on the corroborate branch. So, for instance, one of the ways that you can just set up and play with it is, yes, you have this task.
Here?
So, if you just want to have, you know, the stuff that you want to… if you just want to have, you know, the kind of the back and forth telemetry.
and the stuff you want to instrument, but you do not want to have OB, because you want to play with obi yourself, you just, for instance.
Put the breakpoint here.
run, and then it will stop, you know, the container for Prometheus, Jaeger, Collector, and it will set up the stuff which you have to instrument, but you will skip the stuff here, which is about getting the stuff instrumented by OB.
and the assertions.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:59:01 Oh.
Pellared 00:59:02 So, just one of the ways how you can do it. And also, then you can, you know, you can close it, then if you just crash it, it will keep alive, depending how you close it.
it will just… if it just crashes, then it will not tear down anything, but if you just, for example, remove the code and, like, continue or something, then you will have it turned down.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:59:25 That sounds pretty good, if you ask me, then. Seems similar to what we need, which is… I mean, then… I personally would… would try this.
Like, if we can stop with the debugger right there and just be in a state that… It's similar to what we do today.
Tyler 00:59:42 Yeah, and I've found that I used to do a lot of the same workflow that a lot of people have, and this debugging option actually is a little bit pernicious because it, like.
makes you start using a debugger, and then I found it to be, like, unbelievably helpful. Because, like, yeah, it'll stop, you can go do things externally if you really want, but, like, really, like, what you're trying to do is test the OB, so it's like, oh, just start stepping through the instrumentation stuff, so, yeah, like… That being said, I think that maybe there's some, yeah, some work we can iterate on this. We are out of time, though, so yeah, definitely provide feedback to Robert in that PR, and otherwise, we will talk more next week.
Okay, everyone.
Talk to you later, bye.
Mario Macias 01:00:23 Bye-bye.
