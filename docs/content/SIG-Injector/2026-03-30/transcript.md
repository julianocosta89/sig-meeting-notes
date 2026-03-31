SIG: SIG Injector
Date: 2026-03-30
Duration: 61 minutes
Zoom Recording URL: https://zoom.us/rec/share/9Cxato5RcYMDGzbQivuCgfHfAXf4koezZ3liiNtqxteJru7pe9S0fTU41tXqf-pr.KiLuGpSWezzeL0qS
============================================================

## Zoom Recording Transcript

atoulme 00:06:43 Okay.
Michele Mancioppi 00:07:03 Hello, girl.
atoulme 00:07:05 Yeah, long time.
Michele Mancioppi 00:07:07 On time.
atoulme 00:07:10 Alright, I'll just put up a new agenda for today. Do you have anything you want to talk about?
Michele Mancioppi 00:07:16 I'm recovering from KubeCon, so… Not for you.
atoulme 00:07:21 I know. Yeah.
I wanted to let you know about a little initiative I took, which was to open a new repository for the packaging in Injector.
So… I thought about… The way for us to move forward.
Without making the injector too much, responsible for packaging.
And to prepare for the packaging SIG, Rather than having everything inside the OpenTeometry injector repository, we could create a separate GitHub repository for, you know, injector packaging, for now.
And then when the packaging SIG shows up, we just move that repository from one sig to another.
Michele Mancioppi 00:08:17 I'm not against it.
atoulme 00:08:20 Oh, great. That's… that's a relief, because the GitHub repository is already created, so…
Michele Mancioppi 00:08:25 I want to lose.
Bastian Krol 00:08:26 I…
Michele Mancioppi 00:08:27 But my first reaction was… In the open calendar organization or somewhere else?
atoulme 00:08:34 Yeah, in OpenTeetry, yeah.
Michele Mancioppi 00:08:36 Okay.
It is gonna be all types of confusing, and we should say that this is just an experiment until the packaging's sick.
It's been created, and half people will still not read the first line of the README, because that's how people work.
atoulme 00:08:52 But we'll never find this place in the first place.
Michele Mancioppi 00:08:55 I would even think, like, we put it on some personal org, and then we transfer the repository over to OpenTelem to know when the stars align, right?
Jack Berg 00:09:02 We did something like that for config. Back when we were seeding the project, Tyler Jan, Alex Bowen, and I were just working in a public repository within Tyler Jan's GitHub handle, and we just collaborated on that for, like, 2 months before we submitted our initial OTEM.
Michele Mancioppi 00:09:22 I think that would make more sense, because the moment That there is… it's under the open desk telemetry org, then people will read way too much into it.
atoulme 00:09:33 Okay.
Alright, so… we can host it somewhere else, that's fine.
Michele Mancioppi 00:09:41 I'll, I'll put something in my personal org. Let me put my name on that sheet.
atoulme 00:09:46 Yeah, you got it. Yeah.
Alright, let's do that. In that case, can we apply your PR somehow to that personal org?
Does that… to that repo of yours? Is that where you want to go with that?
Michele Mancioppi 00:09:59 Yeah, let's do that. We close it in ejector, and then I… Okay. I had some fun with Claude to actually move that in my personal record.
atoulme 00:10:07 Alright, we'll, we'll work on that, and cool.
I think I heard from Pablo, for what it's worth, that given the feedback we gave him, he's going to work this week to get the packaging signal blocked.
Michele Mancioppi 00:10:27 Yeah, sounds cool.
atoulme 00:10:30 Yeah.
Alright, there's nothing in the agenda for today. We have… Usual suspects here. I'm just gonna add Bestie.
Michele Mancioppi 00:10:40 There is a PR from yours with a breaking change, and I'm like, does it really need to be breaking?
atoulme 00:10:47 Okay, so…
Michele Mancioppi 00:10:48 Thank you for breaking.
atoulme 00:10:50 That's an excellent discussion. So, this is just me taking your code, putting it back into the pull request, right? There is… there isn't anything that I actually consider.
Michele Mancioppi 00:10:57 I know.
atoulme 00:10:58 Put on those zinc, right?
Michele Mancioppi 00:10:59 I looked at it, and thank you for this, I looked at it, like.
What did a heavy mind do this?
atoulme 00:11:05 It's interesting, because if you slice it like this, you can actually see, like… like, it's making more clear some of the intents and some of the changes, and how they break, but also it's opening up a kind of warmth of discussion, so… I think I'm in support of this. This is really just the only way, as far as I understand, to really allow composition with Debian and RPM packages, is to allow having a conv.d type slide… slide… Style setup, right, where you can add additional files, right?
Michele Mancioppi 00:11:35 My remark was that we should not make it an either-or.
I would, keep the current behavior if the current fall is there, otherwise we do config.
atoulme 00:11:47 Yeah, but you changed the base folder, and because of that, it… the breaking change.
Michele Mancioppi 00:11:53 I don't remember my PR anymore.
But in general, having, like, you look at one place, if that is not there, then your behavior is… Usually correct.
atoulme 00:12:03 I don't mind if we break stuff, I mean, this is a good time to break stuff.
If we break stuff into amounts, I might have a different reaction, but right now it's a good time.
Michele Mancioppi 00:12:13 I wish we would have some idea of how many people are using the packages on InJet already.
I'm queasy about parking stuff.
atoulme 00:12:22 Well, I know CoreLogix, some guy from CoreLogix reached out 6 months ago and was like, really good job on the injector, we really appreciate it, thank you very much.
Bastian Krol 00:12:32 Okay, good to know.
Michele Mancioppi 00:12:35 Literally everybody except Dynatrace needs this technology.
Yeah. Manage, they have it and they don't share it.
atoulme 00:12:44 Yeah.
Yeah, but, I mean, that's… just a different culture, I guess. So… For what it's worth, yeah, it's used, but… I mean, we have made no promises that things were going to stay stable, and this… this is why people should get involved with us, like, if they want things to work. It's usually the force… the force towards stability and not goofing around as much is when people get really serious on calls and be like, hey.
You broke my stuff.
Bastian Krol 00:13:12 Yeah, but also, I think usually, in contrast to the collector or stuff like that, we probably don't have a lot of direct end users, right? We have other vendors, probably more, and they should really take a look at the changelog, maybe, if they… the version, so I'm also not so anxious about breaking stuff, as long as it's called out correctly in the changelog. You need to do this and that to update to this world.
Michele Mancioppi 00:13:41 Fair point. So, are you willing to assume that the people that use Injet are either vendors, or they're using the DBM packages that we published today?
atoulme 00:13:53 Well, I… huh, good question.
I think the way… the way… the feedback I got was that they were using all Debian packages, because that was easier… For them, in that capacity, but it was like a sales workshop.
So it was not meant for developers. For our own use case, for our distribution, we're in the process of integrating the injector back into our Splunk distro. We still haven't done it, because we… well… we need to take our time. We want the Python support that you folks added, that's really yummy, we would like that, but we are not in a rush yet. So…
Bastian Krol 00:14:32 Are you using the… Original injector codes that you contributed at the start, before we came in?
atoulme 00:14:40 Yeah, I have a… and you can even see it, like, this is all public stuff. We have our own distribution, which is itself open source, and you can see that I have a draft PR, where I show the amount of changes we have to apply, where we would remove the C code and start to use Zeek instead.
And I am struggling to remember how I assembled it, but I think I'll try as hard as possible not to use anything, but just the RPM, or just the binary, actually, the binary of your… of the injector, so that I don't do as much work.
Bastian Krol 00:15:16 Hmm.
atoulme 00:15:17 And… yeah, I don't… I think I just download the binary over… over the air, like, from GitHub releases or something like that.
Bastian Krol 00:15:24 Yeah, yeah, that's what we do in our operator as well.
So we…
atoulme 00:15:28 building the Debian and RPM, because we have done it our own way before, and we are kind of, fixed to that, but we would want to… I would much rather overlay on top of the existing. The other issue we have is that we have our own SDKs, so we would want to kind of manipulate some of the dependencies down the road.
And we are, you know, butting into the issue of packaging as a whole. But here, the changes there are fairly meaningful, but not that big. I can put them in the chat.
Yo.
just to be transparent, and things don't work the right way, because we had a lot of opinions about how things were done, so I had to peel off some of the changes already. Anyway, we… it's… It's not that bad, it's just a work in progress, it's great for us to try things out. There are a lot of things that we…
Bastian Krol 00:16:23 trusted.
atoulme 00:16:23 it go off because of the injector kind of already testing those things, in a sense. Like, we don't need our own C code anymore, we don't need those things, but we're not ready to go over quite yet. And I think we need to really be good about the story, about, like, how we embrace upstream. We would want to not just take the… the binary, but just even use the RPM and Debian package of the injector, and be able to lay… to overlay on top of it.
So… that's… at least that's the dream. We'll see.
So, I understand all that. So this PR, 291, let's go back to what we can do today, right? So… This is great because, in the sense, like, we all have had a hand into it.
And now we need to be good about what decisions we want to make. Could we simplify things a little bit here?
Oh, wow. What do they do?
So first off, I messed up the config YAML file, so that's no good.
Say… refer… We've heard those changes.
No, no, config ML files should not be changed.
Because I… I used a shorthand method to create the… The changelog entry, you know, you can do make changelog new, and it's using your branch name, and the branch name is named config, so it's overwriting the config file of changelog, and stupid.
Okay.
Okay, so… the injector subfolder thing, I think it's required because of kunf.d, more than anything else, right?
Michele Mancioppi 00:18:16 Yeah, the only way that I could, I could imagine We can integrate the declarative configuration format.
As a first-class citizen, the packages, is that If you're allowing the stretch of the packages.
for the language-specific declarative configurations to be brought in by additional packages. That is where having a folder for them made sense to me.
It gets really nasty the moment that multiple packages contribute to the same fo- to the same path in Linux, then it gets fucking.
atoulme 00:18:54 Yeah, I think… I mean, this is exactly what… yeah, I understand that.
Does it make sense, then, to make that breaking change, if you'd be okay with that?
Michele Mancioppi 00:19:04 I guess.
atoulme 00:19:05 Not too.
Michele Mancioppi 00:19:06 If we're saying, for example, like, we have that piece of feedback about YouTube.
the, the Dynatrace Deverell using it in containers, and he used the system packages.
So, I guess so.
atoulme 00:19:22 Okay, so I think throughout, like, this is the biggest breaking change. Like, you're having this injector subfolder, not just for the config file.
hotelinject.conf, but also for the, default, environment variables, so that's actually following another theme.
Maybe we could do a thing here, we could do, we could separate, having a base constant for the base folder, and then everything else, so that it's clear we're not… well, it doesn't matter, it's fine. Okay, The next step is… this is from Basty here, it says, making the default empty is also a breaking change for users that do not use system packages.
So, they build the container images, you just put the agents to these different locations. Let me share my screen so you can make sure we're looking at the same thing.
Bastian Krol 00:20:13 Yeah, I'm not sure how relevant it is, that the other thing is maybe more interesting. That is only breaking for users that really use the existing version, but, do not… set any custom paths to any of the SDKs, but actually just put the auto-instrumentation agents at the locations, user lib, open telemetry, etc. So, maybe nobody ever did that. Maybe somebody did.
So in our operator, we put that somewhere else, so it wouldn't affect us, so we could easily… Change that on our end. But, it's, it's more like, for having a complete change lock. If we go with a change at all, then we also need to call that out, and that's that. So, that's absolutely not meant to be, hey, we can't do that.
atoulme 00:21:14 We can make several, like, for what it's worth, we can have multiple brake… changelog per…
Bastian Krol 00:21:19 Okay.
atoulme 00:21:20 we could make, like, two breaking changes in one PR with two different changelogs. That's… that's… that's just that. But it… there was… yeah, I was trying to really run… wrap my head around some of the choices here. So, basically, you wrote this initially, when you make that change, I think you were trying to say, like, we should not have opinions about how things are installed, that's actually not our business.
Bastian Krol 00:21:40 Okay.
Staff?
atoulme 00:21:42 No, I mean, I'm asking Michaela here, because this…
Michele Mancioppi 00:21:46 That is, we should not have assumptions where this stuff is, because… I think we should make, vendor packages.
atoulme 00:21:59 So… yeah, okay, I see what you're doing.
Michele Mancioppi 00:22:02 15, 15, so it should be possible for somebody to drop the configuration file in the right folder.
And, for example, if there is the Splunk Java Distro and the Autel Java distro packages, so language-specific packages, at the level of the packaging system, they should conflict, so only one is installed, and they should put in the same place the file that says where the stuff is installed.
And we'll use different folders, because that's how vendors are.
He didn't put, opt slash their name, somebody dies.
Bastian Krol 00:22:37 Technically, we wouldn't need to make these defaults empty, because if the file doesn't exist, we ignore that gracefully and just say, hey, this is not there, we are not doing… anything for Node.js, for example, but it's certainly… it's always a warning that is printed, and that's… so having an empty default would Probably be much better, I guess.
atoulme 00:23:01 Okay, so this is still a breaking change, but also it's allowing us to have better vendor distribution discussion.
Michele Mancioppi 00:23:08 It depends. It depends on braking, right? If you used… the injector… Without the packages, yes, it's a freaking change, but only then, because we should make a matching fix.
In the current packages we publish.
atoulme 00:23:28 Have a dumb idea, it's coming to me. Should we have an integration test of the injectors, a test with, like, a dummy vendor?
Distribution.
Maybe we call it Acme Inc.
We make it create, like, a… You know, it doesn't have to be… very deep, but it would be great if we were able to test some of those assumptions here in a complete way, where we install all the RPMs, and then we install the vendor RPMs on top.
Michele Mancioppi 00:23:59 Yes.
atoulme 00:24:01 And this way, when we come in with our own RPMs and our overlay strategy, we can make sure that this is supported, and we can show that to other vendors and tell them how to overlay on top of the injector, rather than forking the code.
Michele Mancioppi 00:24:18 I would expect that to be actually not something we need to do in the injector, per se, but in the system packages.
But…
atoulme 00:24:25 Okay, sure.
Michele Mancioppi 00:24:26 I think it's a valid point. We could have it both places.
atoulme 00:24:30 I can put just an issue for capturing that, I'll put a note… Open… and, I mean, it's not… I think it's a lot of… on the injector to do. This is where, like, it gets messy, because you're… it's configuration, it's packaging, it's… There's been an issue for vendor to overlay.
On the injector.
Okay, so what else are we going about here?
So then this is deleted because it doesn't make sense anymore, it's been moved up, if I remember.
then there's something here about how… so this is very simple, no, I'm actually… I wouldn't know how to write this, but my understanding is, like, this is just, reading all the COF.D entries and doing some sort of a merge, right? Use some deterministic ordering based off that.
Cool. We read each file, and then for each file, we read the configuration file, and that kind of creates the final configuration from there.
And… That is mostly it. So, what might make sense, I'm not good at this, but I understand Zigg has some ability to have some tests in the same file? Yes. Should I… should I actually learn some Zeek today, and… Go and build a test?
Bastian Krol 00:25:50 I'm pretty sure.
Michele Mancioppi 00:25:51 What girls can learn for it?
I would just use Cloud Code if I were you, it's pretty good at this.
atoulme 00:25:59 Okay.
Alright, so I won't learn Zig.cod will learn ZIG for me.
bump.
Yeah, code already knows everything, right? Okay, so, adding a test… let me just put a thing just for myself here.
Note.
Adding a test for this code.
Bastian Krol 00:26:22 Yep.
atoulme 00:26:24 Okay. Just, before we… because I'm gonna revisit that in 3 days, we're, like, excited.
And forget everything I said, so, okay.
Bastian Krol 00:26:34 And the way we usually do that, but actually Claude will also figure that out, is that we have actual files in… I think there's a directory called test… unit test assets, or something like that, and then you would create, maybe, a directory structure with a couple of files there, and then Gives that to your unit test, and, Then you just do some assertions on the resulting configuration.
that's… said to do it.
And that pattern is already present in a lot of other… I guess even for source config, there's already stuff that does something like that.
atoulme 00:27:20 Awesome. Okay, alright. Okay, I think we're good.
So… Okay.
That's the only PR worth discussing today.
So this is, again, this is a slice of this one. This one is going to go live on the MKL's GitHub personal account, what we work towards the packaging SIG, that's cool.
Michele Mancioppi 00:27:50 I have the invites.
atoulme 00:27:52 In Syria.
Michele Mancioppi 00:27:54 You all have invites.
Thank you, sir.
atoulme 00:27:58 And then, there's a couple of zeros which are just updating things.
Looks like this one's passing the bill.
It's been approved twice by the same person.
Bastian Krol 00:28:10 Yeah, I thought I had already merged that, but maybe I… Click the merge button, we can just merge this one.
The other one is a long-standing, PR that… failed the builds, and I think you did… you tried something there with updating the Java?
atoulme 00:28:34 Oh yeah, we did that, right?
Bastian Krol 00:28:35 version, but I think it's still failing, and I'm not sure. Maybe we should take some time today to just take a look at what is up with that. You also said something about… the releases, we should not update, the Debian version or something like that. I'm… I don't even remember what PR tries to update, to be honest.
atoulme 00:29:02 PR is just updating everything and anything, and it's finding all the Docker images we use, that we are using in our testing, and for example, we use DBN12 to build a Java application, and then use the injector to check that it's been instrumented properly.
So the idea would be that as long as Debian 12, for example, is still, you know.
Yeah, just… I use this dumb website, for example, gives you an idea.
So, you would like to support 12, maybe 11, a little bit longer, but at least 12 for a couple more years.
They start to always be on the latest, that's great, but it turns out that sometimes some of the issues we have is that we start to have technologies that just not support in the old versions, and it bites, right?
Bastian Krol 00:29:51 Yeah, right.
atoulme 00:29:52 thinking Kubernetes stuff, right? So, but this is… this is no… That happens too. So, I don't think we should be updating constantly to major versions of our Docker images.
From… no, this is not it, this is fine, these are just…
Michele Mancioppi 00:30:12 But, we should actually make, distro-S images.
Where there is… No… no pays there.
Bastian Krol 00:30:24 Well, but these are our test applications, like a test.net or a testnode.js. I think that's fine if they are based on… that's something… not something that we really.
Michele Mancioppi 00:30:36 I had something else in mind. I had the implementation image, sorry.
atoulme 00:30:40 We should definitely update to minor versions updates, but I would like us to stay, so maybe, I don't know, maybe the wording is wrong, maybe, I don't know, but this might be… to me…
Bastian Krol 00:30:51 I got your point. But if we just close it, renovate it, probably just recreate it next?
Day, week, or something, right?
atoulme 00:31:03 Yeah, I'm worried about that. I think I'm still… So, we should… we should do better here. I was maybe waiting for someone to kind of save the day here. It's not… I'm not worried about this, we can move it to draft, for example.
Bastian Krol 00:31:18 Okay.
Yeah, that's awful.
atoulme 00:31:21 Yeah.
This way, no one can merge it without bringing it back to review, which is going to stop people. The Java 21 is even tendestious a little bit, but I think Java 21 is no longer supported, is that right?
Bastian Krol 00:31:36 I think you extracted that also in… into a separate…
atoulme 00:31:40 Still supported.
Bastian Krol 00:31:42 Yeah, okay.
atoulme 00:31:43 But 2025.
Bastian Krol 00:31:44 17, even…
Michele Mancioppi 00:31:47 Oh, so we wouldn't support anything from Java 8 above, because that's what Windows.
Bastian Krol 00:31:52 But to be fair, I don't think the onus of testing a lot of Java versions should be on us.
Michele Mancioppi 00:32:00 Nope.
Jack Berg 00:32:01 You don't have to worry about that. The Java repos already have extensive.
Bastian Krol 00:32:06 Yeah.
atoulme 00:32:07 Justin.
Jack Berg 00:32:07 for all different combinations of Java platforms.
atoulme 00:32:10 Yeah, so maybe for that one, it's like, okay, maybe we can just test the latest LTS, and we'll be…
Bastian Krol 00:32:15 It basically doesn't matter, as long as we test with one supported Java version.
atoulme 00:32:21 Yeah.
Bastian Krol 00:32:22 the… Doesn't matter, I think.
Jack Berg 00:32:24 Right, you all are trying to test the integration, so it's like a smoke test level thing, and, like, the detailed load-level testing needs to be, you know, offloaded to the specific JavaSig, or whatever language sig.
atoulme 00:32:36 Yeah, okay. I mean, I'm always going to be worried, like, as Nicholas said, like, if we want to support Java 8, we just need to be… you know… we need to know that this might be hanging over our head a little bit, and I don't know why that would break, but I can say, for example, like, Node.js, something I'm less familiar with.
Who knows, like, maybe they changed the way node options is spelled, right?
Bastian Krol 00:32:59 Yeah, yeah. And I mean, even for the other argument, we shouldn't update the, say, Fedora or Debian image in one of the test images. I cannot really imagine a scenario where that would make a difference for what we are doing, but of course.
It still could be, but it would really be… odd.
atoulme 00:33:24 I mean, I've always found that bugs show up when I lack imagination.
Bastian Krol 00:33:30 Fair point.
atoulme 00:33:33 Actually, I… look, I don't know, I'm also like, okay, we're… yeah, it's not even… If we could just remove that, that'd be… Anyway, it's, it's fine. Everything is okay. Yeah, okay. This is… the bigger problem is we need to start to update our dependencies at some point as well. We still haven't done that, and that's also something that maybe we do on purpose a little bit here, because we want to take our time to… You know, matures the whole thing, and not open the floodgates to everybody yet, right?
Right?
There are the versions of the things that we package with.
Yes. So, Java agent…
Bastian Krol 00:34:17 Yeah, that's all outdated.
atoulme 00:34:18 Yeah, this is… this is not working at all. I… I don't know, I'm messing up. So… I think we still have the open issue for that, right?
Bastian Krol 00:34:28 We have an open issue for that. I don't think… I don't think the argument, yeah, we are doing it on purpose, is a very valid one, because if we ship something that has that version, it should not be an outdated version.
This, that's reading.
atoulme 00:34:44 Yep.
Bastian Krol 00:34:45 But, it's also not super high priority.
atoulme 00:34:51 I would say we need to fix this soon, right?
Bastian Krol 00:34:56 Okay.
atoulme 00:34:57 Disgusting.
seeks research… This is still not fixed.
Why? I have not been able to understand why.
Okay.
Okay, there's more stuff.
Anything else in here that we should put towards the next release?
Michele Mancioppi 00:35:41 I am a bit distraught by the lack of plan in the… interplay with OBI.
atoulme 00:35:49 Damn.
Yeah, give me prep.
Yes, but Obi has… So, Obi, what I learned is, doesn't have any, has a way to not double instrument.
So, we would go first.
And then they would not… Instrument the application twice?
And that, for me, that was the binary.
And the next question is where to use which and why.
Michele Mancioppi 00:36:22 There is more to it than this.
atoulme 00:36:26 anymore.
Michele Mancioppi 00:36:28 the, Let me remember my general thoughts there.
atoulme 00:36:37 divorce.
Michele Mancioppi 00:36:37 Yes, it's the packaging of OPI, how it relates with OPI, with, The rest of the packages.
it is generally believed that OBI and injector will not collide with each other because of the At least will not inject instrumentation twice. I do not believe anybody tried.
And I do not know that they are not going to collide at the level of process environment manipulation.
And I am completely unfamiliar about what OPI does.
In terms of process environment manipulation.
But it seems that everybody is going, like, yeah, it's gonna work.
Jack Berg 00:37:19 Well, we have Nicola as a maintainer on this, and Nicola's one of the main maintainers on OBI.
Michele Mancioppi 00:37:24 Yeah, I know, it's just unfortunate that's here.
Jack Berg 00:37:28 He's, he's sort of the sanity check that, you know, I, you know, and he hasn't mentioned anything to me about, like, you know, fundamental flaws, and I know this is top of mind for him.
atoulme 00:37:40 would you actually like to test that behavior? We can do that in the packaging SIG in that repo you're building, because… Let's just build it, let's just ship something with a test, and install… you install everything you can think of, and you check that nothing blows up. How's that?
Michele Mancioppi 00:37:58 I think it's a good idea, yes.
atoulme 00:38:01 Alright.
Michele Mancioppi 00:38:02 Because at the latest, it blows in our faces in the packages, at the latest.
atoulme 00:38:07 Well, that's good to know.
So that's a regression, not a design flow, though, right?
Too funny.
Michele Mancioppi 00:38:14 I don't know.
If it is something profoundly foreseeable, I don't know if that's a good argument.
atoulme 00:38:22 The only thing I know is the next 5 lines of code, you know.
Testing with everything. Okay.
Packaging SIG idea…
Michele Mancioppi 00:38:33 Something that has keeping me busy in my head a bit is… there is a bunch of built-in behavior that we have, to deal with, special cases for Kubernetes, like… Automatically set case.pot.uid.
If there is the auto-injector, hits a positive, the environment forever set.
And I'm wondering… Shouldn't we rather?
Have something, more reliable.
So what I'm thinking about is the following.
We expect… the instrumentations in Kubernetes to run in an init container.
And we expect to be able to launch processes through the system package.
And an idea that we had in there still for a bit, and then it was abandoned on the wayside.
Was, to build… Somewhere, a companion process that would make resource detection as a one-off.
And then communicate to the injector what values to set.
atoulme 00:39:48 Oh.
Michele Mancioppi 00:39:49 What this technically could like is that, this particular thingy, effectively sets something in the language-specific, the quantity fires.
By setting the environment variables.
atoulme 00:40:06 you know… some of those SDKs have resource detection themselves, right? Like, Java has some stuff too, right? If I remember.
Michele Mancioppi 00:40:12 Yeah, but it's a pitiful little, and it requires, for example, to the best of my knowledge, Java does not have specific detectors built in, and it requires an act of God to set up those additional jar files and have them picked up.
We could do it in the injector, but then again, I've written a bunch of resource detectors, and it's a bunch of shitty applications, and I don't manage to get one merged in Python since the beginning of time.
atoulme 00:40:42 I see. The collector has also its own resource detector.
framework, right? Which is all of them. There's been a lot of contributions to it for different cloud providers and things like this. Would that be something that we could somehow That'd be good.
Michele Mancioppi 00:40:59 But technically, so something that I wanted to do in the packages, is to integrate also the collector package So that, then you could say, yeah, in that case, the resource detection is done centrally in the collector running on the VM.
atoulme 00:41:13 Yup.
Michele Mancioppi 00:41:13 But then we don't need to invent something specific for the injector itself, and then on Kubernetes, we already know what to do.
John, maybe that is the way?
atoulme 00:41:25 Okay, that's fair. And then, there is also, and this is what we do for what it's worth, I've seen some resource detectors in Java which were pretty advanced because you have to deal with WebSphere.
And the moment you do, then now you're reading XML files, and you're doing lots of ungodly things. I would take it the other way, it's like, it's not an act of God, it's the reverse. Because now you're having to parse where you went.
Michele Mancioppi 00:41:51 The talk of a DT doesn't mean it's a benign one, yes.
atoulme 00:41:54 And, And I don't know about anything else. That's the only example that comes to mind, is this type of stuff is still, like, super useful in Java environments, but because of the way Java is set up, it's just unwieldy. Like, you have so many apps under your app server, your app server is complex. Okay, yeah, if, I'm all for it, because I would like us not to duplicate some of the stuff that we're doing. And you think that right now it's a little brittle with the way we set up those environment variables for Injector, and you don't think it' enough.
Michele Mancioppi 00:42:30 I'm annoyed by the Kubernetes specificity of what we're doing for that.
atoulme 00:42:36 Yeah.
Michele Mancioppi 00:42:37 That doesn't, doesn't sound kosher to me.
It was really pragmatic, and it works wonderfully with the downward API of Kubernetes, but… it feels too Kubernetes-specific for me.
Bastian Krol 00:42:53 Yeah, but that's also, I mean, the Kubernetes specificity in there is for Kubernetes-specific resource attributes, like port name, port UID, and stuff. And for everything else, there's also this just with the resource attributes, key-value pairs that are not Kubernetes-specific.
I didn't really follow the idea, to be honest, from start to finish. Why would you do something with resource detection in a sidecar container? Did I get that right?
Michele Mancioppi 00:43:22 That I thought for a while, because the… The state of the art of the resource detections in multiple languages goes from Questionable to pitiful.
The amount of resource detectors that, for example, can tell you What is the Kubernetes pod UID?
From within the pod.
In upstream is this number.
Bastian Krol 00:43:47 Yeah, right, but it's also often very much not needed, because the case attributes processor can handle that pretty well without.
Michele Mancioppi 00:43:56 Except if you're running on a service mesh.
Bastian Krol 00:44:00 Always we see exceptions, yeah.
atoulme 00:44:04 Oh, you think about the IP being filtered through the service mesh, and therefore you lose it.
Michele Mancioppi 00:44:08 Yeah, literally, the connection source doesn't work for shit.
Yeah. Service meshes.
Bastian Krol 00:44:14 Yeah, that's…
Michele Mancioppi 00:44:15 There's ways of making a correlation in case pod UID, which know the tether sets, and KSPOD AP, which know the tether set, so…
atoulme 00:44:23 Good point. Is there a bug open for that on the previous processor to tell them that it's not getting it?
Because that put association right now is from… so you can have multiple sources, I'm just not remembering all the sources.
Michele Mancioppi 00:44:36 No, there is actually… it's very general. You can either have connection, which reads the IP address on the other side of the socket that talks to the receiver, or resource attributes.
So you can literally put anything there. For example, for the eBPF profiler agent, the only resource attribute that that thing is sending out is container.id, but if you set up the case attributes processor to correlate on container.id, it actually works.
atoulme 00:45:04 Hmm.
Michele Mancioppi 00:45:07 Much to my surprise, because I didn't think it would, but it does.
atoulme 00:45:11 So we have to at least do some discovery.
On the way out.
Okay.
Michele Mancioppi 00:45:17 I mean, that's the reason why the student injector had the Kubernetes pod UID from the get-go.
Because setting that environment variable through a downward API is trivial, and that single environment variable setting Kate's pod UID solves the problem of correlating gates up to processors everywhere.
atoulme 00:45:36 But tell me one thing, when you do… when you go through a service mesh, do you drop altogether the connection IP, or is that passed into a header?
Michele Mancioppi 00:45:43 No, the problem… the problem… it depends on the mode of the service mesh. I have not tested Istio in ambient mode.
But I do not expect it to really work differently. The, I never troubleshooted why it doesn't work, but I promise you it does not.
atoulme 00:46:01 Yeah, I mean, right now, like, the connection source thing is going to use the IP of the request, and I think that, now I'm… back when I was doing stuff like that, my understanding is that the Istio mesh, or the typical NGINX-type proxy, sets the original IP into a header just for kicks, no?
Michele Mancioppi 00:46:25 But it's not what it's been read. So it's not, what is it, the proxied from, or request from, header.
literally what the connection source does is look at the IP address until it's under the Unix socket.
atoulme 00:46:40 Yeah, but…
Michele Mancioppi 00:46:42 I give a shit about others.
atoulme 00:46:44 Yeah, but I could… we can change the code of the communities attributes processor to look for a header value, is what I'm saying.
Would that work?
Michele Mancioppi 00:46:52 We do that, or we make sure that the Kubernetes pod UID attribute is set like as intended, and then we don't care.
atoulme 00:46:59 Okay. Yeah.
Obviously, you want to go for that. That would make sense. I'm trying to look for an easy out.
Michele Mancioppi 00:47:09 We could check, we could check if.
atoulme 00:47:12 I don't.
Michele Mancioppi 00:47:13 I don't know if in the context you can access some HTTP headers, I promise you that the batch processor Breaks that like a brick, though.
atoulme 00:47:22 Yes, so the batch processor is a deep shit, right? That thing is the worst, right? It's in the middle of your pipeline, it goes async, and you lose all the context of what you had before. That's why the computer service processor has instructions to be placed before the batch processor, and I can count on my five hands how many support requests I've had about that, because people will get that wrong.
And it's just really hard.
Which is why we need to remove the batch processor from pipelines, or make it synchronous, whatever we're doing, we need to get this off.
At some point. But for this particular one, yeah, you're right, and I think, you can ask… you can add… you can have access to the headers from the context, only in some cases, if you actually set up the receivers to pass the headers into the context in the first place. So now you're asking people to just play with YAML a lot more.
So, yeah.
Michele Mancioppi 00:48:14 I'm not a fan of that.
atoulme 00:48:16 I don't think our customers will be happy with that either.
Yep.
Michele Mancioppi 00:48:20 No, our customers mostly don't care, because they use the, their state operator, and everything works like a charm, but… Right.
atoulme 00:48:28 Exactly, so they don't, they don't go down to the level.
Michele Mancioppi 00:48:30 What about using upstream? They're in for the fun of their life?
atoulme 00:48:33 Yeah, yeah, exactly. And then, you know, we end up with 5 different vendor distributions with their own quirks to make it work. Okay, alright, I hear you. So, setting the UID seems like the golden… the ground.
get it done. Okay.
Hmm, how do we do that? Should we set that up as an objective for all SDKs, or should that be an injector-level thing?
And… would you like to map that to the entities?
as well.
Michele Mancioppi 00:49:07 The entities, Kind of makes sense, but it's not like the injector generates its own data. It just sets the stuff up.
The moment that you set the Kubernetes ID, case.pod.uid.
That is the one attribute identifying attribute of the KSOT pod entity.
And, I don't know if the SDKs are going to do it on their own or what.
To attend the entity sync, but it was canceled.
atoulme 00:49:42 You probably need to have, a meaningful… push in terms of stabilization or something like that, so that everybody would implement it.
you could… Otherwise, I don't know.
Plus, I mean, so, no, what I was doing here is I was trying to generalize. From pod UID to whatever entity you think your stuff's going to be attached to, like your host, right? Should we make that some sort of a requirement, is that if you want to be considered stable, you should be able to map all incoming signals with some identifying attribute that maps you to an entity. Otherwise.
Don't really work with you, because your stuff is just decorated from everybody else.
Michele Mancioppi 00:50:24 Yeah.
atoulme 00:50:24 your metrics are no use to anybody, because we don't know which part it's attached to, but same thing for a host. Like, if you're just sending me a CPU utilization number, and I have no idea where it's attached to, then you know… Go home.
Stop sending me crap.
Michele Mancioppi 00:50:39 Well, speaking of which, Jack, in Grafana.
Well, I witnessed a certain aversion about setting UIDs.
how does that… I know that a bunch of third-zero customers migrated from Grafana were… had to set the Kubernetes pod DIDs, because Alloy wouldn't. It would just put the pod name, and the namespace name, and that kind of stuff.
How does that square with your supporting entities?
Jack Berg 00:51:07 I can't comment on that. I was aware with the Grafana's issue with UUIDs back from my time at New Relic before this. You know, and I believe it was just primarily from a cardinality standpoint. If those UIDs are… associated with every distinct instance, then, you know, all of the cardinality of that application is multiplied by the number of instances you have over the course of its lifetime, so it's… it's a lot. But…
Michele Mancioppi 00:51:39 I don't understand that, because if you make a case.bot.name.
Given the… given the suffixes, it's gonna have roughly the same cardinality as the UIDs.
Jack Berg 00:51:49 Exactly. And so, I don't know, yeah, I don't know the context about that, or, like, you know, what the current status is, but I don't hear, internally and externally that being, you know, reported as a problem as much these days as it was. So, presumably they got past it somehow.
Michele Mancioppi 00:52:10 Okay.
Jack Berg 00:52:15 Yeah, like you said, the difference between pod name and pod UID is just, it's, like, trivial.
Michele Mancioppi 00:52:20 Okay, so you're saving secularity when you manually create a pod in the same namespace with the same name, cool.
The time flies in the history of mankind.
Jack Berg 00:52:29 Exactly.
Michele Mancioppi 00:52:35 Alright, so then, I'm getting out of this discussion that I threw a wrench by sidetracking with something that actually doesn't really help, so putting resource detection as a part of the sort of system of packages, and instead, for now, we stick with what the language SDKs are doing, and maybe we prop them in the right direction.
By being less.
unwelcoming of, for example, cloud detectors.
And the funny thing is, if the Java agent doesn't want to add to the main jar file.
AWS detectors.
We can put those chart files and configure them in the system packages.
And it works.
It's different for things like Go, so… languages that… Where we cannot add functionality, then it's a baler to fix.
And I don't know if they ever want to do some resource detection in there, but…
atoulme 00:53:43 Ugh.
There was some discussion about Go plugins at KubeCon that was funny.
I don't think this is something that the Go SDK folks have looked at.
I don't have an answer for you. I'm sorry.
Michele Mancioppi 00:54:09 Okay.
Then we start working on the repo.
Thank you.
I'll, I'll push the PR in there.
Then, novility from there.
The, do we want to publish on GitHub pages for the foreseeable future?
atoulme 00:54:31 Yes, sir. That sounds perfect.
Michele Mancioppi 00:54:33 I mean, Trask spoke about Oracle Cloud, and I got sad.
Especially at this stage.
atoulme 00:54:41 I think we should say no to that.
Or we should say trust. Anytime. Go first.
find out more. I don't even know how to go to Oracle Cloud. Where is that even situated?
And how long do we get, like, a lease? Because once we set up… I think if we were to set this up, like, before, we should first do GitHub pages, and then we make it so that there is a really good DNS resolution for that.
And then we're going to need to be, like, there for, like, 10 years. So… I think we should really make the smallest possible jumps on this, and not try… if we… what I'm worried is, like, we go to Oracle Cloud, we go, okay, we need a domain name. Let's restart it with Oracle Cloud, because it's right here, it's easy. And now you're bought in into this. And two years from now, they just pull the rug from under us, tell us that, I don't know, they went all in on AI, and they have no cash left, and they're in a crunch, and they're going to turn off Oracle Cloud for 3 months while he figures this out.
And then we'll be deep in it. I don't.
Michele Mancioppi 00:55:45 We need to have an, like, packages.opentry.io, or something like that.
atoulme 00:55:51 Yeah.
Yeah, so… that's a good start. And from there, it needs to be, like.
you know, GitHub Pages does a good job for a while, and then we figure out when things start to get out of control.
Michele Mancioppi 00:56:04 I think it's fine until the SIG is underway to go and get the pages.
atoulme 00:56:09 Yeah.
Michele Mancioppi 00:56:10 And then one of the first things we do in the city is, you know.
We need not a DNS.
And true.
atoulme 00:56:17 agree.
Agree.
Thank you, yeah. Also, if later on we want to continue to use GitHub pages for development artifacts.
I would be okay with that.
Michele Mancioppi 00:56:27 is gonna work really shit at scale with, the, packages.gzed archives, or VPN, because that thing grows unwieldy.
atoulme 00:56:39 So… Okay.
Michele Mancioppi 00:56:40 That is gonna make everybody's more sad.
atoulme 00:56:43 Okay, okay, nevermind.
Michele Mancioppi 00:56:45 Oh, it's just a quick hack for now, but that stuff wants to be in auto storage.
atoulme 00:56:53 Yeah, I… Almost want to use Esri, more than anything else?
Lori Sridake?
Right? With some CDN on top?
Michele Mancioppi 00:57:03 That would effectively work, but the question is.
We don't have teams before that.
atoulme 00:57:10 Yeah, this is why I think having a member of the TC kind of blessing this is more about that type of decisions than the actual technology discussions.
Michele Mancioppi 00:57:21 I mean…
Jack Berg 00:57:23 What the TC really gets you is somebody to merge spec PRs.
They can't really make decisions any better than, you know, subject matter experts can, that have been researching the thing, but what they can do is use their approval and merge permissions in the spec.
So, like, and they also, like, unfortunately, we can't force other areas of the, the hotel community to make this, like, a priority and do this thing. We have to rely on, like, soft consensus gathering techniques.
Michele Mancioppi 00:57:53 Yeah, that is the funny bit, because I would have expected both the Governor's Committee and the technical committee to have enforcement.
On, on other areas.
Jack Berg 00:58:02 just not hierarchical like that, you know? Everybody's doing this on their own, you know, volunteer basis, and we can… like, the GC sets a roadmap, but, like, people have to come… people and groups have to come to their own, make their own decision to follow that roadmap.
Michele Mancioppi 00:58:19 So the Salta Roadmap is a wish list.
Jack Berg 00:58:22 It's like, it's a wish list, it's a guidelines, at least as it's structured today.
atoulme 00:58:27 I thought Ted… I mean, Ted Young, I think, gave us a bit of hope, because he said that he wanted the sinks to kind of have a meet-up point every year with the GC, where they had to renew Their goals, and… and realign.
Jack Berg 00:58:41 Yeah, that's a proposal right now.
Michele Mancioppi 00:58:43 Well, Jack said, cool, you can… I'll wait a second, the 6 need to renew, or… The TC.
atoulme 00:58:49 it doesn't.
Jack Berg 00:58:49 That's what Ted is suggesting doing. He's suggesting moving it from more of, like, a wish list to something where, like, the TC and the GC do have more of, like, enforcement, like you're proposing. But that doesn't exist today.
And the enforcement mechanism would be, like, some sort of annual or biannual meeting with the SIG maintainers and the GCTC to, like, review that SIG's priorities and make sure they're aligned with the, you know, the GC's priorities.
atoulme 00:59:18 Yep. Like a board meeting.
Michele Mancioppi 00:59:20 Yeah.
I mean, it would make a lot of sense to me.
Ultimately, OpenTelemetry, we need to align 50 different states that do the same bloody thing about languages, so…
Jack Berg 00:59:37 Yeah, it's very inefficient to do this sort of, Full federation, where everybody is, like, independently and independent actors, and we just hope that they, coordinate and are, like, marching in the same direction.
Michele Mancioppi 00:59:51 It's hard enough for people to march in certain direction when they are on payroll.
Jack Berg 00:59:55 Exactly.
Michele Mancioppi 00:59:56 It's over here.
atoulme 00:59:59 Yeah.
Okay, alright, okay, anything else? We got 5 minutes left.
Jack Berg 01:00:08 Well, we went from no agenda to 55 minutes, so…
Bastian Krol 01:00:12 Good enough.
atoulme 01:00:13 Uses. Every time. Every single time.
But it was good. We went over a bunch of stuff, right? So, We are unblocked on that PR, I can work on it. There's some more work on Injector Inobi, we need to test the whole thing, the packaging stuff, because he's going to build his own, We'll have some…
Michele Mancioppi 01:00:36 In the repo, usable by end of the week.
atoulme 01:00:39 Thank you, sir. And then, we'll… we'll start to be more, We'll try to answer every question with a test moving forward, especially, like, this Obi and OBI and Obi with… and Injector, are they playing well? Let's actually try it, and make that very public, and we can… work on some of those automated behavior for Kubernetes and PodUID later on, make sure we are also not creating too much flaky code inside the injector, so it has less opinions and it's more pluggable.
Did I get that right?
Alright.
Bastian Krol 01:01:15 That's good.
atoulme 01:01:16 Cool.
Michele Mancioppi 01:01:17 Okay.
Tish one?
atoulme 01:01:18 Me too.
Yeah.
Bastian Krol 01:01:20 Bye-bye.
atoulme 01:01:21 Bye, Take care.
