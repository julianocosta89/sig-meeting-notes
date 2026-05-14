SIG: Packaging SIG
Date: 2026-05-13
Duration: 79 minutes
============================================================

## Zoom Recording Transcript

atoulme 00:06:26 Hey, dude.
Alright, so… I'm just gonna add this to the dock… one sec…
Michele Mancioppi 00:06:39 Oh, whoa!
atoulme 00:06:42 You know.
I'm just gonna put in normal text.
Okay.
We have a dock… a dead tripped for us, and I'm putting it in the notes. If you don't have it open, feel free.
Just gonna bring it up to the top packaging repo… Here, E, R, A, G… Zoom.
Sweet.
Well, here doesn't work.
Never mind.
Well, good to see you, Kelly. How about we?
So, the situation, I'm not sure if I did a good job of explaining this.
There is a request from the TC that I go present Yes, indeed. I put that on a… on, On the channel. Next week, Tuesday at 8 AM Pacific time.
I will present to maintainers the plan for the Sikh based on the PR merge in community.
Ahead of that time, we'll probably choose a project in the repository, if possible.
This will help us structure the work that we are doing.
I also present a reason for reporting, so there's been a request, it's not just us, they want to do this for every… everything. Then we start to have quarterly reports. They made that my job, and the condition for this, SIG to exist.
So, that's gonna happen. So, That's the context of this. So, I don't want to really go… fancy here. I just want to… use… All the work that you have done?
In prison citizen, as a matter of fact.
what's happening? Like, I'm not exactly sure why I'm having to tell you what's in that Markdown doc, but I'm happy to.
And… We go from there.
Right?
Okay, so…
Michele Mancioppi 00:08:50 By the way, Denis or Denise, I don't know which pronunciations you go by, I do not know your affiliations for the, meeting notes.
It's optional.
Denys Sedchenko 00:09:07 Basically, what company I'm working on.
Michele Mancioppi 00:09:09 Yes.
atoulme 00:09:10 Yes.
Denys Sedchenko 00:09:10 I will fail that.
atoulme 00:09:15 Oh, yeah.
Yushi, thank you for doing it.
I lost my dog.
Let's see.
Okay, looks like you can't win.
Okay.
And Dennis, you work with Ted, right?
Denys Sedchenko 00:09:42 Yeah.
atoulme 00:09:44 Cool, cool.
Welcome.
So…
Denys Sedchenko 00:09:48 Thank you.
atoulme 00:09:50 Alright, so I suspect that the best way is that we just take it, and then we go by line by line of that doc, and we just open issues every single time we see something there is to do.
Any questions?
Let's do it.
I'm gonna share my screen, we're gonna go through that.
And then, if I become… if it's becoming painfully slow, just, raise your hand and tell me it needs to stop, because I can't take it anymore.
Michele Mancioppi 00:10:15 Let's, so… There is a, it's worth to… To think a bit about it before we start creating the, the issues, because…
atoulme 00:10:30 Sure.
Michele Mancioppi 00:10:31 Otherwise, the issues, will be, very messy.
atoulme 00:10:36 Yep, that's fair.
Michele Mancioppi 00:10:37 Before we… there are two stones work. One is we can produce packages, and the second is we can host packages.
atoulme 00:10:46 That's the first… yes.
Michele Mancioppi 00:10:48 Which one do you want to do first?
atoulme 00:10:50 I think we should just get the packages up on… release. I mean, I would like us to build it before we make the deployment architecture and the infrastructure required to deploy those packages actually a meaningful amount of work.
Michele Mancioppi 00:11:06 We have had this discussion, do we want to put it on GitHub pages?
Follow me.
atoulme 00:11:12 That's…
Michele Mancioppi 00:11:13 Yeah.
atoulme 00:11:13 Absolutely wanted to do that, yes.
Michele Mancioppi 00:11:14 There is a… there is a caveat.
Gh pages, will not… there are limitations on the file sizes that I know they exist, but I couldn't find them. And, Deb… is going to, I'm not 100% sure this is gonna work.
I'll just say this straight out, I'm not sure.
what we might, and… yes, Denise?
Denys Sedchenko 00:11:46 Yeah, I have a question about the packaging. So, regarding Linos, if I recall correctly, we support basically Red Hat and Ubuntu.
Michele Mancioppi 00:11:55 APT and RPM.
The, so if you say.
most of the RPM ecosystem that is applicable in containers is RATAD. For, For APT, it's Debian derivative, which means mostly Debian and Ubuntu.
I have not seen anybody using mint in a container, yeah?
Denys Sedchenko 00:12:18 Yeah, yeah, I mean, like, Ubuntu, we have different versions, different versions of libc, dependencies, because in between Red Hot and.
Michele Mancioppi 00:12:26 Yes, but you don't care.
Denys Sedchenko 00:12:27 fedora.
Michele Mancioppi 00:12:28 We don't care, because the… we literally built the injector to be Libsy independent.
We support, we also could support Alpine if we wanted, we could do APK.
The.
atoulme 00:12:42 that the requirement to be included in packages? We could be, like, for the collector, it's statically compiled as well. There's no dependency on HCP.
Denys Sedchenko 00:12:51 Oh, later on.
Michele Mancioppi 00:12:52 Yes?
Denys Sedchenko 00:12:53 I have a question, so, before we're actually doing the infrastructure, if we will opt in into basically first building the packaging pipeline after the infrastructure, at least for Fedora, or for Red Hat, can we utilize Copper Repo to at least, like, initiate.
Michele Mancioppi 00:13:10 Go on.
it is, it is, having two different build processes. For example, that would be the same, like, with Sadaka, we use Launchpad from Canonico.
It's a nightmare. Let's not do that right now.
It's, it's, it's absolute nightmare.
atoulme 00:13:25 I want to be very incremental, just very agile, right? We need to get it to a point where we can have a bit of parallelization, so for example.
I want to build it so that we have something that's kind of getting us off the ground, and at first, if the APT package, the dev file is just a release in GitHub.
You know, that's fine. It's just a point in your release, and you can just point to it.
Michele Mancioppi 00:13:50 That is the bit where I'm not on board, because if it were a single monoritic package, I would say yes. In reality, there is a bunch of them, we met a packages, that ain't gonna fly.
It's not a nice experience to make it unload 5 packages and then DNF.
Each and every one of them. But, the…
Denys Sedchenko 00:14:08 We need to publish somewhere. We also need to host properly separately from the GitHub repo.
Michele Mancioppi 00:14:14 Yeah, yeah, that comes as something for the fish.
atoulme 00:14:16 Yes.
Michele Mancioppi 00:14:18 That's exactly the discussion we're having. By the way, I am wondering if you know that we effectively already have a first version of the packages?
Denys Sedchenko 00:14:28 Yeah, I saw we have, I saw we already have, basically, the building scripts infrastructure to build all the packages.
Michele Mancioppi 00:14:36 agent sold whatever it was at the moment, it's not deployed.
That's, it is not deployed. That's why I was asking, which one do we want to talk about first, because we need to document both.
And the biggest gap that we have right now is where do we put them so that you can add a repository to YAM or APT, and then do an APT or YAM install.
Yeah, okay.
atoulme 00:15:04 I see, so you're saying the value is actually much higher if we have a nice experience of doing Yum and APT.
Michele Mancioppi 00:15:11 Of course.
atoulme 00:15:12 we stop at making the Debian package available, if it's just going to sit on the GitHub release, it's not really fulfilling anything.
Michele Mancioppi 00:15:21 I mean.
atoulme 00:15:21 do.
Michele Mancioppi 00:15:22 And Eduardo, I… literally, in the first section of the summary, let me open the project, because I feel really strongly about this bit.
I'm happy.
atoulme 00:15:34 If you… yeah, absolutely.
Michele Mancioppi 00:15:36 Alright, let me share the screen.
atoulme 00:15:38 Yeah, of course, sorry. Go ahead.
Michele Mancioppi 00:15:44 This thing here… does not work without an EPTO or an RPM repository, yes?
atoulme 00:15:50 Yeah, that's.
Michele Mancioppi 00:15:51 We're teaching the first paragraph!
atoulme 00:15:53 Yeah, yeah, no, no, no. And you're right about that, but I'm just trying to give ourselves a little bit of breathing room, because…
Michele Mancioppi 00:16:00 No, but honestly, I mean, we did so much work up front, we already have a pretty good stretch of the packages, to an extent where if we had a place where to put these packages and the build process, I would probably just push the first ones out.
It's the repository that is missing right now, yeah?
atoulme 00:16:16 Yo, you're right. So… Okay, so let's go back to the discussion that we started with, which was, tactically, do we want to go to our GitHub pages knowing that we might run into some issues, or do we want to go straight for where the money is, which is we actually go for a real real repository.
Michele Mancioppi 00:16:35 Technically, the, so the real repositories for these things, I mean, you could… they were designed to work on FTP.
The moment you can put files somewhere, object storage, Gita pages, nobody cares, it's gonna work.
The reason why I'm, I'm, a little hesitant about GitHub pages is that, the files that you end up putting there can be very large.
So, for example, depending on how you build a repository, you may have a packaging.gz for Debian. They were just having 3, 4, 5 versions. That's very chunky, and I don't know if GitHub Pages is gonna like it. Besides, GitHub is not exactly the most reliable places nowadays.
atoulme 00:17:21 That's true.
Michele Mancioppi 00:17:22 Now, I do not expect that our download rate is gonna break the camel's back on that for the GitHub infrastructure.
Yes, Denise?
atoulme 00:17:32 Oh, but still, yeah, Denny's good.
Denys Sedchenko 00:17:33 The case, so… I can give you a real use case from a homebrew project, which you're probably familiar if you use macOS.
They basically had some problems, like, using free lasers.
Right now, they're basically abusing GitHub Container Registry.
Like, basically, your Dr. Invish is turbole at the end.
But I'm not sure if it's going to work for us as we're supporting Deb and our PM and etc.
Michele Mancioppi 00:18:01 Of course.
Denys Sedchenko 00:18:02 I have a follow-up question.
Some projects, usually, if they need infra, they got sponsored by some kind of, like, hosting provider, like, it can be a small one or a big one, like AWS.
atoulme 00:18:14 You ready?
Denys Sedchenko 00:18:15 What do you consider some kind of, like, search of some kind of sponsorship? Because we might need something like that.
Michele Mancioppi 00:18:21 Costco.
atoulme 00:18:22 Corrections.
Michele Mancioppi 00:18:22 the marker.
atoulme 00:18:24 Yes, go ahead.
Michele Mancioppi 00:18:26 Trask, Skarnac had already said that we have credits on Oracle that we could be using, Oracle Cloud.
atoulme 00:18:32 So, definitely, like, this is… So, I think when we started this discussion, one of the first things that, actually you asked me to look into, Michael, was to have a CNAME.
of some sort that would be under our control to manipulate and make sure we have a registry moving forward. And what I would like us to do is to work really hard on naming on that CD, just to make sure we're getting this right, and we don't… fuck up, like, we don't want to change our minds two weeks in, right? But then… and then, where that synonym goes is up to us.
Michele Mancioppi 00:19:05 I think so.
atoulme 00:19:05 First, if we get free credits for some Oracle Cloud stuff? Oh, absolutely, let's go ship.
Denys Sedchenko 00:19:10 Do you mean the DNS record, right?
Michele Mancioppi 00:19:12 Yes.
atoulme 00:19:13 Yeah, yeah, yeah, yeah.
Denys Sedchenko 00:19:14 Okay.
Michele Mancioppi 00:19:14 I mean, for me, for me, that is obviously packages.opentelemetry.io, so already the domain is already registered. The, the question that, that I'm having is, so right now, we want to, we want to support TBN and RPM, so Deb and RPM as formats.
Both of them.
allow to have a path separation, so you would have, the APT repository is under packages.opentra.io slash APT.
But I still think… so this is based on matter collections from several years ago, and I still think that we need to validate that all this is correct.
Yeah, I do not believe… so I do not really envision, a time in which, or at least not in the foreseeable future, when we are supporting non-Linux systems.
Because the injector is hard-coded for Linux and ELF.
As the, the metadata format to figure out what to inject.
Yes, sir.
atoulme 00:20:18 That's… Specifically, it's injector.
Michele Mancioppi 00:20:20 Yeah.
So, I would say that… Essentially.
atoulme 00:20:25 I would say that what could happen is that over time, we start to deploy and make available other fields.
The collector, to me, is high on that list.
As a package.
And that collector could be, you know, somewhat valuable for other OSs, but for that, there's a HomeBroot app that we can use later on this year.
Actually, we don't have to… I think that's the answer. It's like, we're only careful Linux right now for those two different subsystems of APT and Yum. And, anything else?
Michele Mancioppi 00:20:57 Let's also, let's also think about, let's also validate APK.
Because we do support muscle C in the injector.
atoulme 00:21:06 Yeah.
Michele Mancioppi 00:21:08 So, effectively, the moment you get APT, you get RPM, and you get APK, you have the entire civilized world of packages, because I'm not talking snaps, and I'm not talking flat file.
We're not talking that stuff. I refuse to talk about it. Apologies.
atoulme 00:21:25 user, right? Just those packages with, like, those.
Michele Mancioppi 00:21:29 With that, we do RPM, we can think later on to do APK, but for the, for example, whether we want to go with packages.opentra.io, which would be great.
slash APT slash blah. We need to validate that, we can use those subpaths.
In a way that works easily. And I have metacoluxions that are murky, and I don't know anything about APK.
So we need to check that for all those three systems, we can use a subpath instead of having to put, like, apt.packages.obotentry.io.
atoulme 00:22:06 Okay. It looks like…
Denys Sedchenko 00:22:07 by the way.
atoulme 00:22:09 Okay, perfect.
Denys Sedchenko 00:22:10 I'm not sure, did you hear about open source build service? And actually providing a separate, like, project open build service is, like.
it's not just open source focused, it's basically a service where you can build packages for different distros.
Michele Mancioppi 00:22:27 Never heard of it.
Denys Sedchenko 00:22:29 And do we… I know we… And also.
Although, basically, the packages are going to be statically linked, like, just to basically keep us safe, do we consider initially to basically have a, like, limitation, just for the beginning, when the project basically starts to, like… we definitely, like, support two LTS versions of Ubuntu, or something like that.
Michele Mancioppi 00:22:57 Oh, that is a discussion that we have had in the injector, which is a fertility. The atom, like, this sick is from a rib of the injector sig.
We want to, to support, so LTSs.
Yeah, but we need to go further. We need to go back. I have painful experiences as a product manager at Canonico, and I'm telling you that Ubuntu from 2014 is never going to die.
atoulme 00:23:26 Never.
Michele Mancioppi 00:23:28 So, we need to go… we need to go way back. Now, in containers, it's really simple, because if the injector works in containers, it will work on a virtual machine. The moving pieces are literally the same. So, testing that without having to have really questionable VMs running around, it's simple.
atoulme 00:23:49 We actually…
Michele Mancioppi 00:23:50 Absolutely.
atoulme 00:23:51 type of tests in the injector right now. Like, we have a container, we install the injector, we might not be installing it from… Yeah, I think we installed it from RPM.
And then we, we make it work, but it's on testing on Yubo 224, right? So, I think we should want to have, over time, a compatibility matrix where we say, here are all the versions of all the distribution that we are testing against.
And if you'd like to add your own, you're welcome to come and help, right? And we'll give them some way to, kind of, contribute to that.
But for now, I think it's a little out of scope. There's… in the collectors, they've done a good job of defining different tiers of support as well. When they say, barely compiles, we didn't try, we actually test on it every single commit, or we even benchmark on it, right? So we could do this type of tiered support.
But for now, like, for just to make sure we get started, we… We should probably start from the… from this. Yeah, go ahead.
Michele Mancioppi 00:24:47 This is, however, interesting.
But it's, it's also for hosting.
atoulme 00:24:57 I mean, it fits better than whatever we have to build our packages, we can use it.
Denys Sedchenko 00:25:02 But they actually have a separate… they actually have a separate, like, thing that they use under the hood, which is called OpenBuild Service. Just type OpenBuildService.org.
Michele Mancioppi 00:25:12 It's… it's this…
atoulme 00:25:13 It's.
Denys Sedchenko 00:25:14 docs. You can basically self-host this thing.
Michele Mancioppi 00:25:19 Yes, but does it do only the building, or also the hosting?
Denys Sedchenko 00:25:27 Hmm… So…
Michele Mancioppi 00:25:29 When I used… difficult part.
Denys Sedchenko 00:25:32 The dating back.
Michele Mancioppi 00:25:32 It's trivial, we could just do a… we already have a bunch of bash scripts with FPM that do it.
Denys Sedchenko 00:25:38 So, like, when I used… when I used, like, when I used some packages that they used OpenBuild service, like, they already provided a way to basically download from the OpenBuild service.
I didn't dig enough through to check if, whether it provides you, like, a PPA-like interface.
For, like.
Michele Mancioppi 00:25:56 Repositories. PPA. I mean, yeah, we need, yeah, PPA, but not in the very complicated launch pad idea, yeah.
Can you… can you look into that? I mean, this…
Denys Sedchenko 00:26:07 Yeah, sure, sure.
Michele Mancioppi 00:26:07 If you could do something like this instead of abusing GitHub pages, then… hell yeah.
atoulme 00:26:13 Alright.
Open.
Denys Sedchenko 00:26:15 With GitHub pages, we also, like, for the PPA, we also need to basically manage the signatures.
Michele Mancioppi 00:26:22 Yep.
Denys Sedchenko 00:26:22 Someone needs to be actually responsible for that.
Michele Mancioppi 00:26:25 Yeah, they ignore the PGP, that is always the thing.
The pain of animals?
Denys Sedchenko 00:26:32 Yeah, and also, like, to avoid someone stealing those.
Geese.
atoulme 00:26:36 Yeah… We would want to do this, So, I think that's actually going to be a big part of the packaging thing, is the responsibility of making those deployments, and We can put some securities in our GitHub repository, so for example, having a keys file that you have to run by when we make a release.
We could talk about this a little bit later. We… that's… that would be… Very important to do to go GA, like, to actually make it so that people can depend on it.
I'm really just worried about the hosting part right now. Just make sure we are able to get off the ground.
Michele Mancioppi 00:27:14 If we had a reputable hosting way, then it's 90% of the first, the alpha release is done.
atoulme 00:27:21 So… would it make sense, then, to just tell them, like, here's the pilot, the POC that we're going to build? The next 3 months are just going to be about securing some infrastructure, like an Oracle Cloud VM, or, you know, object storage, right, whatever, what have you.
go into this and do a little bit of identification of some of that infrastructure we can get a hold of, sorry. Discuss with Trask about having access to a CNAME setup.
Does it need to be, actually.
This is not a dependency. We can make it so that we use some random CNAME at first, like, just to test and validate, but…
Michele Mancioppi 00:27:59 Packages.opentermphread.io all the way.
atoulme 00:28:02 We want that, and I want this name, but I just want to also give them some peace, it's like, we're not just going to hook that up the first day we got an S3 bucket up, we're going to do that when we're good to go.
Michele Mancioppi 00:28:14 By the way.
atoulme 00:28:14 Stop.
Michele Mancioppi 00:28:15 Nobody said, so if… The intuition of Denise is correct, and OpenBuildServe is something we can use.
We don't need to go and screw around with buckets and Oracle Cloud and whatever.
atoulme 00:28:28 Yeah, that's even better.
Denys Sedchenko 00:28:29 We… we… so, like, it's, we might, like, we still might need an infrastructure to still host all of this thing. I have actually a follow-up question regarding my findings. What will be the best place to actually share my, like, search results. Just drop a message in HotelPackaging chat.
Michele Mancioppi 00:28:50 I don't know, we're going to start creating GitHub issues.
Okay. The goal of this meeting is that we create key tab issues. We're just discussing up front so that we don't create them weird-shaped, right?
atoulme 00:29:01 I think we're already seeing a little bit of an iteration. At first, we thought we were just going to forcefully go for infrastructure.
Frankly, I… I think we're getting to the right point. So, that means that we should investigate infrastructure possibilities. I think, Denise, if you'd like to go take the Open Build Service investigation, that would be great.
What I can do is, in parallel, just go inquire with Trask and others about exactly what does Oracle Free Credits looks like, because I… it's one thing to hear about this. I've heard this… I just want to be, like, I've had some past experience with this type of discussion, where they say, oh, yeah, we can get free credits.
Until you start to ask, how do I get those free credits? Who's giving me access? How is that access managed? Can I have a group of people have access to this? What's the RBAC like?
what type of… automation can we even build with Oracle Cloud? Can I push from GitHub to Oracle Cloud? And these type of things. So I think I have even… if open-build service is not the solution, I have a bit of… I can put on some legwork for myself to go work on exactly what that looks like to have infrastructure by CNCF.
I would even push, I would need to… I think, just more general research is, like, if… I'm sure the Linux Foundation and the CNCF have some pretty strong ideas about where RPM and IPC packages could be hosted.
Linux Foundation has Linux in the name.
Good hope.
But, yeah, so…
Denys Sedchenko 00:30:42 Oracle was the only… Oracle Cloud was the only contact.
Michele Mancioppi 00:30:46 That's what you just mentioned.
atoulme 00:30:48 So, to task off the stage.
Denys Sedchenko 00:30:49 As far as I know, AWS also have a free credits program, which they offer for a lot of.
Michele Mancioppi 00:30:55 If worse comes to worse, I just spin up an AWS account, and that still pays the bill. That's not a problem. It's just to avoid all the dance, the song and dance of the securing and the PGP key, if you can find something civilized, because Don't worry, if there is a cloud, be like and pay it. That's not… that's not it, right?
atoulme 00:31:16 I mean, that's very nice of you, Joffre. I… think that would… probably be a problem, but… and I, yeah, I know for a fact that we also have a DBS credit somewhere.
And the fact that Trask is just offering Oracle credits first is telling to me.
And that's okay, I need to just… figure it out, like, what even that means.
Like, how many Oracle credits are we talking about?
You know, is it 10 bucks?
Or is it… is it $5 million? What are we doing?
Denys Sedchenko 00:31:46 And how will we build? Because, like, is it also the traffic and etc?
atoulme 00:31:52 Yeah, how is it built? How is it, can it be abused? Because, even our doctor container image, right, these days.
Is downloaded millions of times a day.
Right.
It's very impressive how much traffic we are getting.
I'm not even talking about the vendor, but I think on hub.docker.com.
you can see the type of traffic to expect, right, on OpenTeometry.
So, I would say that overall, like, yeah, over a billion downloads, a billion pulls.
of the OpenTelemetry Collector Country, Docker image.
So I want to make sure that they have that love thoughts room.
This week has been pulled 7 million times.
Denys Sedchenko 00:32:50 By the way, guys, did you hear about an attack on Ubuntu intra?
that their PPAs were not, like, where they were not available for, like, one or two days.
atoulme 00:33:01 No, it's not.
And I think that's also talked to what Michael is saying, it's like, we should have a very simple PPA where you add the PPA yourself, you don't go through whatever… Ubuntu is making you do, right?
and we'll figure out later how to make it so it's part of whatever standard, I guess.
Denys Sedchenko 00:33:20 I mean, like, we might… we might consider in the future some DDoS protection.
atoulme 00:33:26 Okay, that's fair.
Michele Mancioppi 00:33:27 Yes, but… I also… I mean, that's a great problem to have.
atoulme 00:33:33 Oh, I want to have this problem so hard.
I won't be complaining to my wife about how I couldn't sleep last night, because, you know, we had a DDoS attack, oh my god.
Bye.
Yeah, you're right, right? Stones, no harm there.
Denys Sedchenko 00:33:48 Do we, like, in OpenTelemetry in general.
Do we already have, like, a dedicated person or, like, group of people who basically, like, manage SSL certificates. We shouldn't be managing all of that ourselves.
atoulme 00:34:03 So, yeah, I mean, your questions and your train of thought may be thinking about on-call, right? Operations, actual SRE type thing. We have nobody like that, and that's just been a problem, and it's actually what this packaging thing is trying to solve, to some extent.
Because people are very interested in building a draw file.
the moment it tells them, hey, how do you make that Java more available to people, their people just disappear, right? This has been… A constant for me.
Right? The Docker images, thank God, there's good Docker images for support with GitHub, because otherwise, I don't know that people would be able to make that available quickly.
in RPM and, Debian packages that There's just… yeah, no one's going to pop that up.
So, if open build service works, and someone else is going on call to make sure that they don't get delayed, and that they have the search up to date and all that, that's awesome, I want that. If we don't have that, then I think we need to start to put a little bit of thought into this, and we will need to, over a period of time, think about those type of challenges.
hosting content.
Michele Mancioppi 00:35:15 I'm sorry, why… so when you talk, when you say content, you mean the packages, right? Not additional stuff.
atoulme 00:35:21 Yeah, packages.
But the moment your horse bites, You're up.
So what, what are your… What type of, availability are we talking about? Do we care?
Wait, can we set some terms, just to make sure we don't get ourselves into a situation where… People get red in the face because it's been up, like, it was down over the weekend. Oh my god, how is that even possible?
Well, I'm sorry, this is upon telemetry, it's community-based, you're getting what you're getting, right?
If you, if you want.
Michele Mancioppi 00:35:51 At the end of the day, what I fully expect is that the moment we start doing this.
Also, vendors will set up their own repos, because the entire architecture of the packages is designed to allow vendors to swap language implementations with their own packages, so…
atoulme 00:36:11 Yeah, mirroring is fine, right? Yes. That's fine. Jeffrock does that for a living.
Oh, could we get a free jerfrog? Would that help, too?
Is that something you want to look at?
Denys Sedchenko 00:36:25 NFT Factory.
atoulme 00:36:26 Yeah.
Is that something that we could… is that even an option, or do you want just… no, Antoine, you're full of it?
Don't… don't even go there.
Denys Sedchenko 00:36:35 GFrock actually also solves this problem of, like, basically providing your own PPA, or, like.
atoulme 00:36:43 They run it for you.
I just don't know what that bill looks like, or if it's even possible for open source.
Denys Sedchenko 00:36:50 If I… if I recall correctly.
Do they still offer, like, a self-hosting option, or they don't?
Michele Mancioppi 00:36:58 Yeah, no, I'm not supposed in this, if I can avoid it. And if I'm supposed to get it, it's gonna be… the simplest imaginable thing is gonna be a nestry bucket.
I agree.
atoulme 00:37:10 that much.
Michele Mancioppi 00:37:11 So…
atoulme 00:37:11 Yeah.
If they run it for you, okay. If they don't, then it's free.
Because S3 scales, S3 never lets you.
Michele Mancioppi 00:37:19 These packages, they were designed for FTP.
Oh, bye.
Anything more complicated than FTP is overkill that we're going to pay for in blood and sleepless nights. No.
atoulme 00:37:32 Sorry.
Denys Sedchenko 00:37:33 If nothing works out, our fallback scenario is to basically have a repo as a, like, basically as a PPA, but it points to, like, whatever blob storage we use.
Michele Mancioppi 00:37:45 Oh, in reality, even the metadata of the repository, they sit very well in a string.
Denys Sedchenko 00:37:51 Nice.
Michele Mancioppi 00:37:53 You don't need to have an HTTP server with metadata.
Denys Sedchenko 00:37:58 Yeah, you're right. Basically, just a 3-bucket is a PPA.
Michele Mancioppi 00:38:01 Yes.
Perfectly, yes. With the right files inside, yes. The same way that a jar file is a zip with privileges, yeah?
atoulme 00:38:10 Yum.
Denys Sedchenko 00:38:11 I will try to search if there is, like.
If the… someone already also solved the problem of, like, basically having some automation around, like, S3 as a PPA.
Michele Mancioppi 00:38:20 Yeah, it's more… it's more the… the absolute pain in the backside is the signing and the keys. If it wasn't for the signing and the keys, we already would have an S3 bucket configured with everything else in front, because then it's 50 lines of CDK, yeah?
Denys Sedchenko 00:38:38 Yes, that's true. When I wanted to make my own repo, I also, like, dropped this idea because of signing.
Michele Mancioppi 00:38:44 So, I, can you please… I'm sharing the screen.
Can you double-check what I wrote down?
Denys Sedchenko 00:38:52 Yeah, just give me.
atoulme 00:38:53 No, that sounds good to me.
Denys Sedchenko 00:38:56 Yeah.
atoulme 00:38:59 That sounds great. Thank you.
Michele Mancioppi 00:39:01 Look, step one.
But we already read the tissue number 4? Damn it.
atoulme 00:39:07 Because he, he opened a few pull requests when he started, like, there were some open, like, renovate stuff. That's what…
Michele Mancioppi 00:39:14 Okay.
atoulme 00:39:16 Don't worry about it.
Michele Mancioppi 00:39:17 Do you want to take this one?
Denys Sedchenko 00:39:20 Yeah, yeah.
Michele Mancioppi 00:39:23 So…
atoulme 00:39:25 Denise is already a member of the team.
Michele Mancioppi 00:39:28 Wait a second, Denise or Denise?
Denys Sedchenko 00:39:31 Whatever you like. This is just how I'm, basically, what I have in my passport, but the international version is just Dennis, D-E-N-I-S.
Maybe I need to change my name to avoid people… to avoid confusion.
Michele Mancioppi 00:39:45 I know, I mean, my wife is from Ukraine, it makes a hell of a difference for her, so that's why I learned to ask, right?
atoulme 00:39:52 Indeed, okay. Okay.
Denys Sedchenko 00:39:54 I have a question regarding the third topic. Have a good way to manage SSL certificates and signing keys. Can we decouple SSL certificates from that? Because SSL certificates is something you'd basically do on your, like, separate.
Michele Mancioppi 00:40:09 Not entirely, not entirely.
Denys Sedchenko 00:40:11 No. If you have a CADI, like, if we can have a, basically, CADI reverse proxy, which manages ACMA provision, DNS, and, like, DNS affects…
Michele Mancioppi 00:40:20 Too complicated, too complicated. I don't want to run a reverse proxy.
That is, for example, bucket, congratulations, there is CloudFront in front of it. Now, the reason why I'm saying that we need to manage SSL certificates is because, we want to have, to mask it behind the C name, yes?
So, what you would do, you would add to APT repo, I don't remember what it's called, packages.opetern.io. If we move the repository somewhere else.
and keep the CNA, because that's the whole point of it, then the machines that have added the repository before are refusing to connect, because the certificate signature changes.
atoulme 00:41:04 That's right.
Denys Sedchenko 00:41:06 You mean, like, if I… if I'm doing a CNA… yeah, but… Yes. Yay.
Michele Mancioppi 00:41:14 Yes. So, for that is, can we host… can we get our Let's Encrypt certificate, for example, and use that?
atoulme 00:41:22 what I would go for.
Denys Sedchenko 00:41:23 I can consider that… as a, like, as an extra point, but I don't promise, because, like, if I'm talking about open build service, it's basically a product you deploy yourself. If you're talking about open source build service, which is, like, SaaS built on top of it, it's a separate question.
Michele Mancioppi 00:41:43 It is, but .
Denys Sedchenko 00:41:44 Maybe it's better to, like, to split, like, the SSL part, which is HTTPS, and, like, actually the, like, the machinery you will be using for building.
Michele Mancioppi 00:41:54 Yeah, I agree, that's why these are four different points.
Denys Sedchenko 00:41:59 Okay.
atoulme 00:42:02 So we're good.
Denys Sedchenko 00:42:03 Okay…
Michele Mancioppi 00:42:05 That's why there are four different points, and SSL and PGP are separate, because they're different concerns.
Denys Sedchenko 00:42:11 Okay.
atoulme 00:42:12 So, for PGP keys, what I've seen in most open source repos… open source discussions I've had is that we only trust that you will manage your own keys. You don't share those keys. They don't get uploaded to CI. There is no such thing.
You have to have… you have a human in the loop who is authenticated using a passphrase, their PGP key, to certify that the… to sign a request at some point.
Michele Mancioppi 00:42:40 The moment you slap it in an AWS secret.
Denys Sedchenko 00:42:44 Okay, so… One moment, like, there are two different approaches to the keys, like, there is, like, an approach that's actually used by Linux distributions, where, like, every key is basically managed. Every package is signed by the maintainer, and the keys of those maintainers are basically sitting in the keychain. Maybe it's, like, a K-chain of Arch Linux, for example.
How it's measuring.
atoulme 00:43:07 you have done an Apache.
Denys Sedchenko 00:43:08 You have to… you have to synchron… you have to synchronize the K-chain, or…
atoulme 00:43:13 you could always…
Denys Sedchenko 00:43:14 what a lot of… what a lot of, like, projects are doing that's shipping PPAs and having their own repositories, like Spotify Client, they actually have a common, like, CI, the key that CI actually using for signing.
Which is, like.
atoulme 00:43:29 So, if we do that, I'm okay with it, I just want to make sure we set that expectation.
Okay, so you would like CI to sign?
Michele Mancioppi 00:43:37 Yeah, CI builds and signs, yes.
atoulme 00:43:40 Do you want to have… when we get CIH assigned, you… I don't care anymore. Okay, fine.
Denys Sedchenko 00:43:48 It's a…
atoulme 00:43:49 Complex.
Denys Sedchenko 00:43:49 question.
Michele Mancioppi 00:43:51 Yeah, but in reality, look, look, let's be real about it.
The moment it's signed with an asymmetric key, It's good enough.
It has the additional passphrase, different keys for different maintainers.
Dude.
That's much better.
Denys Sedchenko 00:44:11 complicated way, like, for example, how the signature process works for Windows and Mac OS, for example, or they have a separate service that does all of that, or we can go… or what they proposed, let's go simple solution, where it's just like…
Michele Mancioppi 00:44:26 I feel like the simplest thing that works.
Denys Sedchenko 00:44:29 Okay.
atoulme 00:44:30 your dad.
Let's do that, and let's use a key that is going to be in the GitHub Secrets in that case, right?
Where are you gonna store your keys?
Denys Sedchenko 00:44:40 We actually have, like, just in recent months, there was a lot of, like, problems of, like, secrets leakage due to integrations with other, like, GitHub bots and apps, so this should be probably done separately in Vault.
atoulme 00:44:56 So, you wanna have a 1Password vault for Penteometry?
I think we have that.
Denys Sedchenko 00:45:02 I didn't…
atoulme 00:45:03 for a collector.
Denys Sedchenko 00:45:05 I didn't work with non-passport integration, but I used to fetch secrets from HashiCorp World.
Take whatever you like.
Michele Mancioppi 00:45:13 Yeah, we don't want self-managed infrastructure, we don't want a host vault. Securing that…
Denys Sedchenko 00:45:19 I mean, like…
Michele Mancioppi 00:45:19 hard drunk.
Denys Sedchenko 00:45:20 We can use 1Password vault, we just need to be able to just fetch this, fetch this secret in CI.
atoulme 00:45:27 If I find you, the way we do it for the collector, release it, which we sign.
Can we reuse that, and not do all…
Denys Sedchenko 00:45:35 Sure, sure, yeah, sure.
atoulme 00:45:37 Okay, that's… I can do some research to tell you exactly what we do there, because I think they've done some pretty good research into that, and if it works for them, then it's gonna have to work for us, kind of thing.
I think the way they've done it is that instead of making it a GitHub secret at the repository level, they have dedicated a specific, boot that has access to the secret.
And then the boat is being invited to come and sign, and that's the only thing it does, or something like that.
So, they separate a bit more the concerns.
Interesting.
Denys Sedchenko 00:46:11 Thanks.
Because, like, we just need to avoid storing those secret… these keys in GitHub secrets, that's all.
atoulme 00:46:19 Yeah, it's a switch thing, yeah.
Denys Sedchenko 00:46:21 And how does this actually… oh, okay, never mind, you will share your… research.
atoulme 00:46:27 I will.
But you're doing the… you're doing all the work on the open build service, you're… all that. For me to go look at what the collector does, probably, like…
Michele Mancioppi 00:46:37 I mean, theoretically… So, if you want to use the way of signing things of this, then hello, the build server is called GitHub Actions.
So that… what we… what you need is a hosting service.
atoulme 00:46:54 I understand.
Denys Sedchenko 00:46:57 Yeah, so we're just planning, look, just for the hosting service, not for the build service at all.
Michele Mancioppi 00:47:02 If, so we need a hosting service. If it comes in with a build process that checks all the boxes, great.
But the building is not the difficult part. It's the hosting the difficult part?
Denys Sedchenko 00:47:17 Okay, in case OBS, for example, does the building, but let's assume it doesn't do PPAs, or it does not provide you options, like.
I don't know, doesn't manage SSL for you.
What can be… can I also… I would probably need to put the option B. What will be the option B?
Michele Mancioppi 00:47:40 Look, look at a few options, find the pros and cons based on these four ones.
And then we go over it, right?
Denys Sedchenko 00:47:48 Okay, okay.
Michele Mancioppi 00:47:50 I have the feeling that we're trying to discuss upfront all the possible problems without knowing what the reality is.
Denys Sedchenko 00:47:57 Okay, and the outcome of this ticket, should it be, like, a proposal PR, or a comment?
Michele Mancioppi 00:48:05 just post in the comments, and then we chat about it on the next signal.
Denys Sedchenko 00:48:11 Nice, okay.
Sorry for naive questions, I'm just trying.
Michele Mancioppi 00:48:14 What was that?
Denys Sedchenko 00:48:14 What's the best approach.
Michele Mancioppi 00:48:16 We can keep it super simple, it's three of us with a big mission. That's the simplest thing that works.
atoulme 00:48:23 Yeah. So, we have a lot to figure out.
But the hosting service is going to define everything we do from there on.
Michele Mancioppi 00:48:31 Yep.
atoulme 00:48:31 So, whatever we can… Find out.
I'll shake the trees and see what we can get for free from the GC, like, you know, Amazon, Oracle, what else you got, right? What can we get?
Michele Mancioppi 00:48:44 I look for the kind, like, if it's just an Esther bucket that you end up using.
Let's not even go down the route of the, the credits or stuff, like, there still pays the bill. End of story. We make… the same way that to do auto bin, we make an AWS account.
And… We'll make it happen, it's not difficult.
Without having to go and talk with the partnership people of some other company, and… Then they revoke the credit, so we run out of it, so it's great.
atoulme 00:49:15 I don't think it's been that bad, but, I mean, it's a few extra steps, for sure, but, yeah.
Anyway, I'll take time with Strask, see what we can do.
Denys Sedchenko 00:49:29 Costa.
atoulme 00:49:29 But first, let's go open build service to find out what we can get for free.
Denys Sedchenko 00:49:33 And guys, I will be… PTO, like, I will be out of office today and Friday, so I will take a look at that at Monday.
atoulme 00:49:43 fellas.
Michele Mancioppi 00:49:45 the, this we effectively already have.
atoulme 00:49:52 Me too.
Michele Mancioppi 00:49:54 We have factory already have them. It needs to… it needs real-world validation.
atoulme 00:49:59 I, I mean… The injector, yes. The autoslotation, we currently don't have a separate RPM for those, right? So we would want to do what you.
Michele Mancioppi 00:50:08 If you want, go on.
atoulme 00:50:09 Break it off, right? What?
Michele Mancioppi 00:50:11 We do, we're doing my PR for the injector.
atoulme 00:50:13 Okay, in your PR for the injector, so, like you say, yeah, okay, that's what you mean by real-world validation, you said?
we will take that and actually shove it… push it into the packaging. Yeah. Because we… we did not implement that PR, and so we need to.
Michele Mancioppi 00:50:30 They did not merge that PR.
atoulme 00:50:33 We did not merge the PR.
Michele Mancioppi 00:50:37 It's not an SDPR, but it's… descends.
atoulme 00:50:40 Anyway.
Michele Mancioppi 00:50:41 It's different, it's… I wouldn't say if it's 100% ready, but it's close enough, right?
atoulme 00:50:46 Yeah, it works. So, what I want us to… yeah, so let's do that and test it in… so that next step, right? Hosting… And… and we start to, push the, the packaging code… with the… with the objects that we talked about, around injector implementation SDKs. Eventually, you'll be, or at some point.
Yeah.
And that's, that's the scope, is to make it easy for people to consume that. We should probably spend the time that you've been good about documenting this, is that We want this to be, for vendors in Avenue, for them to… Overlay or replace specific packages, so they can install, for example.
the injector from us, but then, oh, I'd like to get my own Java. Alright, so make it some sort of a documentation there.
Is that something you want to ship right away? I know we want to have this requirement well thought through.
So we don't back ourselves into a corner.
Is that… Even something we want to test for, in some sense.
Michele Mancioppi 00:51:57 I'm sorry, you lost me.
He lost me after the second set of brackets.
atoulme 00:52:03 Okay, take your time to write this story, it's okay, I can wait.
Michele Mancioppi 00:52:07 No, God, I… Now you have my full attention. What do you want?
atoulme 00:52:12 So, the requirement around having our own instrumentation SDKs packages is that we want vendors to be able to come in and say, I'd like to plug the Java Package, and replace it with my own.
Yeah. And… That's a very vital requirement to have vendors kind of be able to interface with the packaging scene, because otherwise we won't be able to play along with it.
And I… I think that's very clearly put into the… all the work that we have done, like, in the Markdown format, the file that you built, in the discussions we've had, it's been very consistent.
Do we want to make that… part of that implementation to the TC, and then, specifically.
Do we want to test?
That scenario. Somehow.
Michele Mancioppi 00:53:00 I already did. So I already prototyped it. I don't know if I pushed that to the PR, but ultimately, the way that you do that is to have two levels of metapackages. There is one that is the OpenTentry package, and then there is the OpenTentry Desk Java package.
And then, the… I think where I got stuck is the good name for that, for the open telemetry, like, kind of official or upstream or something.
That is where… that is where I did not have… no, no, wait a second, I think I settled for OpenTeetry Java Meta, for example.
And then, it would be just OpenTendra, Java is the one from us, and then, OpenTelemetry, there's Java, there's Xero, whatever, whatever the Xero wants to call it, for example. It doesn't matter, because in reality, what you say in the metadata for both RPM and dev, you say, this one replaces that, or this one satisfies that.
And then based on the order of, of the repositories that you put in the packages, okay, it's all this one.
atoulme 00:54:02 Okay, so as we're pushed back in, we will have those tests, we will have that in place. Okay, perfect, that's what I wanted to be.
Michele Mancioppi 00:54:07 And it's something that we need, actually, to settle on early on, because the, Well, no, purely technically. We can do it later, because then, The moment we want to introduce the second level of meta packages, then we just change the OpenTelemetry package to require OpenTelemetry Java Meta instead of OpenTelemetry Java. So that is also doable.
atoulme 00:54:33 Okay.
But at least we're going to say that we're thinking about it.
Michele Mancioppi 00:54:38 I think it's a necessary requirement for this to be successful.
atoulme 00:54:43 I agree. I… I… Just want to make sure I bring this up in a way that is very… very helpful… for people in the room to pick up and say, hey, I should go back to my boss and tell him We don't need to manage those packages.
we can really start, right away, think about how we get your interface with that SIG. That's a big interface. So I want to build a.
Michele Mancioppi 00:55:11 Because, for example, I do not expect anybody to want to make their own build-out injector.
But I do expect every single vendor to want to do their build of the Java agent.
atoulme 00:55:23 Yes.
Indeed, and this is worth bringing up as a population to the… to that TC discussion. So, packaging, users… Okay.
I'm just taking notes about, like, how I'm going to talk about it, that's all.
Go ahead.
Denys Sedchenko 00:55:42 Guys, I have a question.
Why the packaging alternatives basically been, like, discussed on our side?
Because as far as I understand.
Most of the package managers already, like, provides an option, basically, to specify that package provides something or conflicts.
Michele Mancioppi 00:55:58 Correct.
atoulme 00:55:59 Oh, I'm sorry, I'm really in the obvious territory here, right? I mean, ESU all thought about this. I just want to make sure that people who are less qualified to talk about packaging, I actually assume that there are a lot of people being touched by this. We don't know about those type of requirements, certification, like, the… There's a lot of details here that Michael is able to kind of very well articulate. Well, you should assume that we actually need to educate people about this a little bit here. And I think that actually was a bit of a problem when we started to talk about the packaging SIG.
We found that, we actually need to… bring them with us on that territory. Like, it's not going to be just… yeah.
So, you know, when you start to talk about, that it's about some of the stuff, like reviewing the PR, or reviewing the packaging thing, I could tell right away, it's like, oh, that guy knows, like, he's done an RPM build in his life.
Most people in OpenTemich have never done a single RPM build in their life. They don't know what's inside the Debian package. It's probably some mystery magic, right? They don't know the structure of the metadata of a repository, like, oh, what have you.
I'm sorry. I'm supposed to just…
Denys Sedchenko 00:57:11 documentation efforts.
Michele Mancioppi 00:57:13 No, it's also… there's also a bit of architecting, right? So.
atoulme 00:57:17 Bring them with us, making this a community effort is gonna take, No.
Michele Mancioppi 00:57:22 Now, Denise, think about it. Imagine that we skip the language level of Meta, and then the OpenTelemetry package which is a meta package, depends on OpenTelempry Java version, 4 or above.
I'm making numbers up.
The vendor package, It's gonna have a hard time to match versions.
But, if you put a meta package in between.
And we create a new version of the metapackage only when the material interface between the content of the language package changes. So, for example, the files are supposed to be in a different directory, or the format of the configuration that tells the injector where the JAR file is, is in a different place or has a different shape.
Then the vendor's saying, hey, this one, my-0-java.
is equivalent to that range of versions of the meta package. That is simpler.
So, I think it's worth to make an issue about that.
to validate… again, the thing, because I did all of this in my head, and I think I did some experiments, but… This is an important aspect.
Validate… Again.
Indeed.
laptop.
Alright, thanks.
atoulme 00:58:45 I think maybe just, I'm gonna use your PR and just build a nice little diagram, and that's going to be my… You already have a diagram, don't you?
Michele Mancioppi 00:58:56 If I know myself… oh, I should have had a diagram.
No, I do the diagram in words.
atoulme 00:59:05 Hey, always been.
I will do a little picture to present for that SIG, and it's going to be based off everything you've done. I will… Credit the work that you've done on this, and then let's use that for the number two discussion we'll have. So, number one discussion, hosting, number two discussion, great structure, look at this, vendors, you should play with us, we're gonna work with you.
Guys, I'm being pinged, I need to run to some emergency, I'm so sorry, I wish you the best of, of times. Have a good night. Mikuli. Good day, Denise. Talk to you soon.
Michele Mancioppi 00:59:39 Oh, I didn't.
Denys Sedchenko 00:59:39 Sure.
Michele Mancioppi 01:00:23 What makes sense, the description of the issue.
Denys Sedchenko 01:00:26 One moment… In general, yeah.
In my opinion, it makes sense to… explain what… what you… your proposal with all possible edge cases. Sorry, I'm not really familiar with Paris DKL packaging story.
Michele Mancioppi 01:00:50 There is no SDK packaging, auto SDK packaging store. At the moment, there is no such thing. The, the… let me give you a primer, since I have you here. So… The best, the best citizen, in terms of packages, is the, java agent.
This thing here is a JAR file.
Which we can effectively deploy wherever.
And it works.
No?
This is the golden standard.
It gets worse from here.
The, JS, Delta Instrumentation for JS, the out instrumentation for Python, so Delta Instrumentation for JS, and…
Denys Sedchenko 01:01:41 Node.js, right?
Michele Mancioppi 01:01:42 Yes, type JS. Yeah, Node.js. We're not doing the browser bits. So the instrumentation for Node.js is, it's okay, I mean, it's like a million small packages, but okay.
You can, it's very similar, we will end up doing something very similar to what, Debian does in main, because they have some… I don't know if in main or Universe, but they have some Node.js dependencies. Instead of packaging every single little package as a different system package, we just make Node.js instrumentation package, and that's a release strain.
Or at least that's, that's how I imagine the release train story to happen, and later on, we're going to make issues about the release train. Like, how often do we release Do we appropriate all the packages, or… I don't know. That we'll figure out. That's a… it's a big item of discussion in the entire stable-by-default work stream of OpenTelemetry.
So, Node.js and Ruby, fine. Okay, cool.
net and Python.
More difficult?
So.NET, for example, you need to package different binaries for different, libc. Same for Python.
So that's already not super fun.
Luckily, we're not going to care, because since we're building for DB and RPM, it's going to be libc. If you do APK, that is muscle, end of story.
The injector has a lot of, a lot of, machinery inside.
to actually figure out, by reading the ELF metadata.
Which libc is supposed to be linked to the process that has been injected?
So, the injector doesn't care about libc, can cope with either of them and multiple versions of them, no problem.
We are gonna have… but the injector was also built to just inject in containers, but since we can make assumptions about the distro, because we're not packages, then in system packages, we have a much easier life.
To the extent where we wouldn't need the entire ELF song and dance of the injector. We could just literally build different versions. There's only lip series, there's only… only, muscle, because… I don't think there is any reason to support the weird TBN patch sets that are using muscle C as the Libsy library, right? Just doesn't make sense.
So, there are, like, this kind of three different levels of complexity in packaging the OpenTentra SDKs, and it's not just the SDK, it's SDK plus auto-instrumentations.
In the Java case, SDK and data instrumentations live in the same jar file.
Right?
In every other, language, they are separate packages.
Denys Sedchenko 01:04:44 Mmm, and you can have mismatch potential.
Michele Mancioppi 01:04:47 Technically, yes, but then we will effectively decide that, hey, the release train for the SDK is going to take this, and then all the instrumentations together.
the, And then there is another category of languages, which are those that, the injector does not work with, so Rust, Go, C++.
Where… There we need to use OBI.
So, the OBI, Open Telemetry BPF Instrumentation.
There are graphanistas, like, Nicola, like, Mario, working on it.
They're also working on a system package, and effectively, that system package has to become part of our ecosystem of packages, where, you know, it's, it's part of our, like, the packaging is something… it's in the same repo, and it is referenced by our OpenTeentry meta package, and so on and so forth.
So that is too much of it. I did not talk about PHP, because it makes me sad.
But it's similar. The level of complexity is similar to something in between Node.js and Python.
Denys Sedchenko 01:06:05 I assume you omitted most of the pieces of complexity in Python, because you have dozens of versions of Python, you have UV, etc.
Michele Mancioppi 01:06:15 Yeah, it's, it's nonsense, but in reality, for Python, I found something very cool. So the, you are, you, with our system packages, you don't need to do peep or UV or whatever.
The way that the injector works is that, so, do you know how the injector works?
Denys Sedchenko 01:06:35 No, probably not.
Michele Mancioppi 01:06:36 Okay, so, it's an LD preload object.
So it's, it's a, it's a .SO that needs to be, to be, loaded, federally linked at runtime.
It assumes that the JVM, the CPython, the Node.js, they are dynamically linked.
And, when it's…
Denys Sedchenko 01:06:58 RoadKit, right?
Michele Mancioppi 01:07:01 Yeah, don't use that word. It's, Some rootkits use LD preload. LD preload was a mechanism that was actually devised for good, like, for example, switching out malloc.
Don't make that equation.
Denys Sedchenko 01:07:14 Okay, like mods in video games, let's say so.
Michele Mancioppi 01:07:16 Yes, thank you. Much better.
So, the, how familiar are you with LD Preload, ELF, and the like?
Yeah, no.
So, LD preload, it, it has an init array. The init array, has a job of, effectively launch the initialization. The initialization goes, looks at, the, AAWX, I don't remember the name, so the auxiliary startup parameters.
to find out the location in memory of the program header for ELF, And then it traverses the help data structures to find the dynamic symbols.
The first dynamic symbol it looks up are those with DT underscore needed, because those are the packages that the linker is supposed to link, and then identifies by name.
So, GLIBC is always lib, libc6.so or something like that, and muscle has either LD-Muscle or muscle, depending on how you build it, yeah?
So, it finds the, the type of lipc.
Then, what it does, it goes and looks at the memory maps.
To find out where it is actually linked.
It looks at the program headers of the lipc to find the offset of the DLSIM function.
The DLSIM function is something that allows.
Denys Sedchenko 01:08:54 wraps… it also wraps, Libel D, as well.
Michele Mancioppi 01:08:57 No, it doesn't wrap at all. It uses facilities of LibLD which is… in muscle, there is no libel D, muscle is one single thing. In the… in the… in the GNU… in the Lipsy world, yeah.
Denys Sedchenko 01:09:10 Same problem.
Michele Mancioppi 01:09:11 So it uses the DLSIM to find the location of the mviron pointer and of the getEmph function.
Denys Sedchenko 01:09:21 It's basically you're calling… it's like calling DLSIM with a null as a library name, so you can, like, query your… query your own process.
Michele Mancioppi 01:09:30 No, no, it's not a…
Denys Sedchenko 01:09:32 have.
Michele Mancioppi 01:09:32 Yes, yes, yes. Fundamentally, yes. And that… we did it like that, because, over the different versions of libc, there were additions like indirect symbols and other stuff that I didn't want to bother learning. So I said, okay, we find the LSIM, And when we found their sim, we let the logic of its own libc find out its own stuff we need.
And then when, when we have the pointer for environ, and the pointer for GetEmv, then we can add environment variables that will trigger, for example, the Java agent. You can… the JVM, if you pass the java dot underscore tools underscore options, and you put inside there manage java agent, colon, and then an absolute path with the location of the jar. At startup, the JVM, So, the DGVM has already started, but we're still in the init array phase. It will actually read that environment variable and append.
The content to the startup parameters, and then activate the instrumentation.
No question.
Denys Sedchenko 01:10:40 All of that stuff, is it happening before the CRT was initialized, or after?
Michele Mancioppi 01:10:46 The what?
Denys Sedchenko 01:10:47 CRT, C runtime. Basically, your pro… your function.
Michele Mancioppi 01:10:51 It is… it happens before the domain is called.
Denys Sedchenko 01:10:57 But after underscore start is called. Underscore start, initialize.
Michele Mancioppi 01:11:02 Underscore start? Yeah, because that is in the… that is in the libc. Underscore start is in the libc. It does the init array, it does a whole bunch of stuff. Then the main method is called, the main method is already in program… in program space. By then, we must have already set and modified the environ.
to… to put the right values. And, if you ask, okay, why don't you just look for the environs?
I have an entire explanation of all the things we tried. So, just ambulance is not enough, because you need to know, what is the original value for something.
So we need to also get amph. And, for example, something that we tried and it didn't work well was to have, the, SO of the injector have a weak symbol to AMPERON, That broke… for, programs that are dynamically linked without a libcim.
And there are a lot of good programs for that. For example, the AWS CNI plugin.
So, effectively, the fact that, you know, we load, and then inside, by doing all this ELF magic, we find out where the memory pointers are. By the way, all of this happens without memory allocations, because we're literally following pointers, yeah?
That is the safest way, to the extent where we have not broken anybody. Now… Now that you know how the injector works, let's talk Python.
So, in Python, we need to tell Python Where a, a site.
Denys Sedchenko 01:12:44 Site packages.
Michele Mancioppi 01:12:45 Yeah, the site repositories. And, we use, effectively, we append, we prepend, the location for the packages to the Python path.
So that our site gets searched first. And we have a site customized, file.py.
which needs to be compatible with both 2.7 and 3, because we never know which one it's gonna be.
Denys Sedchenko 01:13:10 Do you still support both?
Michele Mancioppi 01:13:12 You must.
support both… so, the SDK supports injecting the Python works in 3.6 and above.
But the injector does not know which version of Python it is. So, what happens, like, if you inject a Python 2.7, it still must be… the site customized script must be able to say, I'm not touching this, this is Python 2.7. The SDK is not gonna work.
So, the site customized script must be compatible with both 2.7 and 3.
But then in 2.7 or versions of 3 that are unsupported, it just throws its end in the air and says, no, I am not touching it.
Denys Sedchenko 01:13:51 Hmm.
Quite complicated machinery.
Michele Mancioppi 01:13:55 Yeah, it's very fun.
And the nice thing is, this is technology that at this theater we have Used in production for… for a long time, so it's such a good stable.
Twarks.
Denys Sedchenko 01:14:07 Hmm.
It's, like, it's a very impressive piece of machinery, even outside the observability itself.
Michele Mancioppi 01:14:14 It was, I mean, I built all this knowledge over years, I've been obsessed about putting SDKs where they did not belong.
Denys Sedchenko 01:14:23 usually such stuff of, like, basically manky patching and freaking around with binaries, usually all of that, like, if talking about, like, resources, all of that is being discussed on Windows.
But not really in Linux. I wanted to try something like that.
Michele Mancioppi 01:14:39 Wait a second, wait a second, wait a second.
The, the original, user of LD Preload.
is Dynatrace. They're the one agent, since 2016, has been doing only preload to activate the Dynatrace tracers.
I have learned a lot from them, because I was their customer at SAP.
So the fact that they would use all the preload, I learned there it existed. They never told me how it actually worked. So first, we did it at Instana, then I did it again at Lumigo, then we did at Decero, and there are actually generations of how I've been doing this, and I think this might be the final form.
Denys Sedchenko 01:15:19 Unfortunately, macOS, like, it also has dial-deep reload path, but, like, due to signature requirements, unfortunately, you cannot do such kind of things unless you turn off all the security measures.
Michele Mancioppi 01:15:31 But, I mean, who runs production software on macOS?
Denys Sedchenko 01:15:35 Cicd, basically, if you have macOS runners, or you have, services that, like.
Basically, there's, like, a service that allows you to wire up your right.
Michele Mancioppi 01:15:46 Never, in 5 years at Instana, 4 years at Terciro, never in my life I found sufficient amount of people running their software, production software on macOS, to justify doing dynamic injection.
Never.
Denys Sedchenko 01:16:07 I know at least one company, but they're basically providing you, like, a cloud VM with an iPhone, like, if you're a search engineer.
Michele Mancioppi 01:16:18 fine, but on the iPhone, you're not going to use the Java agent, you're going to use the iOS SDK, and that cannot be injected.
So the… also the Swift one cannot be injected. You need to build it in, In the Swift program, right? So it's not… Doesn't bother me.
Denys Sedchenko 01:16:34 actually depends, because, like, so, Objective-C is a very flexible runtime with dynamic dispatching.
And, for example, when you are debugging application on iOS, like on Xcode, an emulator, and not.
basically, behavior of some certain built-in iOS functions is actually different.
And Xcode itself, in emulator, they're basically having some kind of… they're also having ejector, mostly to trace whether you are doing something correctly or not. Like, for example, you're trying to call UI… update UI logic from a different thread, which is not going to work. They're going to show you a warning.
And basically, they needed to inject this behavior in nearly almost every Objective-C runtime function.
And, like, you… The problem is that you cannot… like, you can try to manky patch every possible function.
But you also need to know to know a return address, where you need to properly return from.
Michele Mancioppi 01:17:37 Excellent.
Denys Sedchenko 01:17:38 And, like, you can also extend classes, like, you mentioned human capacity method for a class.
But then you also need to properly manku patch it for the inherited class. Yeah. Because, like, inherited class is going to call the base class method.
Michele Mancioppi 01:17:53 Yeah.
Denys Sedchenko 01:17:54 But it will also return… but it will, like, it will return back into the… into over the base method of class A, instead of overridden method of class B, class B, so they basically ended up generating a very huge amount of trample lines.
And, like, crazy assembly machinery stuff, just to get, basically.
Michele Mancioppi 01:18:15 Yeah, so as far as we're concerned with system packages, if the SDK can be injected by having the files for the SDK somewhere where the process can see them.
And manipulate the environment, then great, we can support it.
If it's required, or it's supported by OBI, either of the two.
for example, purely technically, purely technically, it would be possible to support Go with a linking process.
Things by manipulating the dynamic symbols table to effectively put in between wrappers, yeah?
That's insanity, and Dynatrace has done it, and every time that the GoABI changes, which is every release, then they break everybody, so we're not doing that.
Denys Sedchenko 01:19:06 Alright.
Michele Mancioppi 01:19:07 I need to drop.
Sorry.
Denys Sedchenko 01:19:09 Thank you for, like, taking your time. Thank you for lecture.
Michele Mancioppi 01:19:13 So, we're… I'll see you next week.
Denys Sedchenko 01:19:16 Yeah, see ya. Bye.
