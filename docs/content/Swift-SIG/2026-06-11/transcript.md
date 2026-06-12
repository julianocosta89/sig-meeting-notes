SIG: Swift SIG
Date: 2026-06-11
Duration: 57 minutes
============================================================

## Zoom Recording Transcript

**Vinod Vydier** 00:11 This floor?
**Ari** 00:16 We don't…
**Vinod Vydier** 00:20 Hey, Ari, how are you?
**Ari** 00:24 I'm… trying to… To, I'm chores.
**Vinod Vydier** 00:30 Yeah.
I mean, would you… Just enjoying my morning videos.
**Ari** 00:52 Oops.
I'm supporting that.
Let me see what I think.
That's… Got a sec.
Nice.
I assume I did not anticipate that.
political change.
Well, I think we can start, I don't think, oh, here it is. I don't think Bryce is going to join, based on what he mentioned last week, so… Hey, Nach.
**nacho** 02:32 Hello, good morning.
**Ari** 02:35 Good morning.
**nacho** 02:36 Damn.
I can attest that, Bryce, it's alike.
**Ari** 02:45 At least, at least he's alive.
**nacho** 02:47 Not an AI. Not only an AI.
**Ari** 02:52 Alrighty.
**Vinod Vydier** 03:01 So, is he… is he on his way back, or…
**nacho** 03:05 I think he…
**Vinod Vydier** 03:06 Thanks for joining.
**nacho** 03:08 I think he… today was his last day, but he has been very busy.
Yeah. Yeah, he was only with him on Sunday.
And I told him that he got some.
other, day that he wanted to have something.
That he could contact me, but yeah, I didn't receive any more.
Yeah, probably too many things to lose.
**Ari** 03:38 Right, I was going to share my screen, so maybe you can… Don't… Okay, so… Trum.
Do you see.
So… These are the notes for this week.
I copied the ones that were unsolved from last week. Seems that for the concurrency issue.
Bill is still working on this.
And I wasn't sure about which was this, issues with API types, finding extensions in SDK, so I know what it is, if there's something to do on our side, or what…
**nacho** 04:29 I think that's related.
to… The extensions of some classes not being public.
From the API in the SDK.
It was in…
**Ari** 04:43 It's an issue related to that.
**nacho** 04:45 I didn't… Don't remember, I think it was in some of the…
**Ari** 04:51 Let me check it out.
**Vinod Vydier** 04:53 There was a PR that someone sent, right?
And I think, Nacha, you did refute that.
**Ari** 05:04 I think?
Okay, I really don't know.
**nacho** 05:12 It's watching the car.
But it was in the cork, which is…
**Ari** 05:16 Yeah, this is Core, Dependency Dashboard.
**nacho** 05:20 Yeah, no, that's another…
**Ari** 05:22 That's per generated, and this is a concurrency one that… Will it's going to solve, I think.
**nacho** 05:31 Yes.
Yeah, Billy was on that. I think he has some updates on the code, but I…
**Ari** 05:37 Yeah, yeah, yeah, yeah. But I, I, I just… Yeah. Mentioned about still working on this, so… And these ones are the issues on OpenTelemetry Swift.
Recent update from Swift Love, OTLP profiling… Changes to the package to incorporate this spec.
This is the one I'm doing.
I don't really know which one it is.
To be honest.
**nacho** 06:08 I…
**Ari** 06:12 Oh, my goodness.
I really don't know.
Boom.
Megan.
Yep. Review. Yes.
Eric.
And that's it.
Are there any new topics you guys want to discuss?
**nacho** 06:35 No.
**Ari** 06:38 Okay, I have a quick thing. I shared with you guys, this doc.
The other day?
Related to… having, like, a deprecation notice or something like that for… for cocoa pots.
Mmm.
I don't know if we want to deprecate it, to be honest. This is, like, a kickoff, so we start discussing this, considering that by end of the year.
Cocopus is dying, so basically, as it was announced in this one and in this one.
This is the support plan. It was communicated, so…
**nacho** 07:18 ju…
**Ari** 07:19 this was.
**nacho** 07:19 That's true.
**Ari** 07:20 Most time.
**nacho** 07:21 You are not sharing it.
**Ari** 07:23 Oh, Josh. My bad.
**nacho** 07:25 Yeah, no worries.
**Ari** 07:29 Let me do it this way.
Tudor.
Here it is.
Bill.
this is the document. I basically mentioned, like, this is the original post from CocoaPost, and this is the one that is saying the timeline, and as you guys can see, on December by the end of this year.
It won't accept any new prospects. So… Considering that that's going to happen.
I created this document to kick off it.
So… I'm basically saying similar things to what other SDKs are saying.
Not saying anything new or anything really bad.
So… This is a bit of what we've been dealing last… months since we started with CocoBots, like.
This adds operational burden on us.
Cocoabots.
It's not really doing any sort of improvements.
So, you know, all the problems we've been having with the PBN and all that stuff, it's really been problematic. Like, we are having intermittent upload issues.
we had the problems with the vision OS stuff, on… on lately.
on some versions of the SDK.
So, there are not really a lot of efforts from the CocoaBots community to improve that, and it's not going to change.
And obviously, if we… just remote CocoBots, well, we'll have just SPM, We have less maintenance complexity.
it's going to be reliable always. It's going to be easier for contributors, because sometimes contributors don't… Don't add things to the pods, spec files, and all that stuff.
So, we got to spend time where… We won't.
I have no idea of… of how we want to announce it, or how we are going to do it.
**Vinod Vydier** 09:35 We did something for XC Framework, right? We had some requests, I think we can probably just follow that same…
**Ari** 09:43 We don't have nothing for XC Frameworks, but it would be really good if we support them instead of this. So, we just support XE frameworks, and We leave the… we can create… leave the pod spec in the repository.
I mentioned something like that here, like, we can't leave the Pacific, so anyone can go.
Fork the repository, or clone it, and just build the pod spec themselves, and that's basically it.
And the other one is we can generate an exit framework and leave the prospect, and everybody can go and just build the pipelines themselves.
And how about private spec? So… That's something people can do.
But… to be fair, I really don't know what we want to do. Like, we want to support Cocoa Pots after it finishes, or not? Like, that's kind of the first answer, or the first question we have to answer.
Then we can… follow… Start talking about, like, the details of what we want to support, what we want to… Another side.
**nacho** 10:50 To be honest, we have had But… Cocoa pot's broken.
several times.
Right?
**Ari** 10:58 Yeah.
Yeah, yeah, yeah.
**nacho** 10:59 Wait.
**Ari** 11:00 It's… It's been broken for, like, 2 or 3 releases.
**nacho** 11:05 And no one has traced any flaw.
In the public, so no one asked for that.
Right?
**Ari** 11:14 No, no. I think that unless they have specific issues in a specific version, I don't think that people is going to really, really worry about that.
**nacho** 11:24 Yeah, I mean, probably we can… Yeah, and we, we, we are gonna release now a Sweep 6 version.
Probably that can be the right one supporting this, if we want.
Or, or, yeah, I mean, it's like… Yeah, We'll… So, I don't think that… I mean, they are using a version that's… what it is, I don't… the only reason I can imagine for them to really update the frameworks that they are using is because they need some kind of sweepstakes. Maybe. We are… Already given that, so probably no one more will need something newer, except if they need some new spec or something new, and probably will need also to update. So, yeah, I don't think that that's a problem. About the About the frame… about the XC Framework thing?
Okay, can we really have… every liberty as an exit framework itself.
**Ari** 12:32 Not all of them.
**nacho** 12:36 Yeah, the thing is that… you probably want an XC framework if you have just one, right? We also talked in the past about allowing the people to create an XC framework with So, I think that the best option, and also performance-wise, is Being able to create your XC framework with all the libraries you really want.
is a much better solution than to have.
several XC frameworks, because you cannot really… link them properly.
later. So yeah, maybe that could be, the real good path.
Yep.
**Ari** 13:19 The only…
**Vinod Vydier** 13:20 So if you create an XC framework, will it be, like, multiple… Exec binaries at… A customer has to use, and so… Like, SPM will get all the dependencies, right? Automatically, whereas, excuse…
**nacho** 13:38 if you put an XC framework, you can just download that instead of downloading the source code and everything there, just clean.
**Vinod Vydier** 13:46 But how do they, how do they get the.
**nacho** 13:47 Jordan.
**Vinod Vydier** 13:48 How do they get the dependency? Do they have to, like, get the…
**nacho** 13:52 There's a way.
Yeah, you mark the dependencies and it will.
Take.
**Ari** 13:58 Let's… talking about SPM, considering we will just support SPM, What is going to happen is that you have to add a binary target, and that binary target, you have to add a specific direction for… for that… where that binary target is set.
And that's basically it.
So, it's… it's not really complex in that… In a way structurally do it.
what I think we may want to discuss is, do we want to host some of those Oxy frameworks ourselves?
Or not?
That's… that's something that maybe we can discuss.
And also, For which libraries? Because… I think that all the OpenTelemetry Swift libraries.
are not worth having them neither in CopaPass nor the XC frameworks.
like, the basic of OpenTelemetry to make it as compatible as possible, like, with everybody else and all that stuff, it's on the OpenTelemetry API and SDK.
But having all the others, I don't know if it's really worth it.
We are investing a lot of time and investing a lot of resources on having, like, another source of distribution.
In things that maybe people is not really using much.
**nacho** 15:24 Yeah, and also the thing is that when you are deploying a binary XC framework, you have to also create a SA that identifies exactly that binary, you have to do a lot of stuff that must be also Paired with your release.
So, it will probably have to be in a third… Repository where we will just land the binaries or something like that.
From a professional perspective, Everyone should keep their own.
fork of the library, and keep their own version, and build the exit frameworks that they really want, and expose that to the rest of the Right? That's… That's prelude it.
Best professional solution, because you… you have the… your version that you are tight, and you… that… that kind of things.
you are not depending on that… someone that raised you. Just update your… your fork with the new things that you need, and use that from now on. I think that's…
**Ari** 16:32 Yeah.
**nacho** 16:32 the way it should be used. Probably we will have users of many other methods.
**Ari** 16:39 There's only one problem to that, is that if two SDKs are using OpenTelemetry, let's say, API, And they build themselves with different Xcode versions.
An exit framework.
The binary… the resulting binary is going to be different.
And it's… it's going to… Hub linking issues, like, it's not going to compile.
That's… that's the only use case that's going to be… Not great.
But, to be honest, Vega still uses me.
it's not that they cannot use source code. It's like, you can still go use SPM, and let your customers use.
your SDK without.
DXC framework, and that's it.
it's not a problem on us, like, I think that eventually it's like, how do you want to distribute your SDK, and… If your SDK with XC Frameworks is generating issues, okay, use it without XC Framework.
I, I, I don't know. I think that… unless… unless we have, like, ourselves hosted the XD framework, it's going to be rough for people using SDK to… to use it. I would just advise towards not using it.
And that's it. Like, if they wanna use it for… development purposes, whenever they are developing their SDK, awesome, they can do it, so it's cached and all that stuff, but once they release the… to the public, they should… they shouldn't use the DXC framework. They should use, like.
The actual binary, the actual source code, and that's it.
**nacho** 18:25 Yeah, if it's… if it's a… if it's a framework or a library, yeah, definitely.
**Ari** 18:30 Shall we… Tell somebody about this?
shall we reach, people that we know they are using, like Datadog, Embrace.
I think that VLE in AWS is also using it.
**nacho** 18:51 All of them are using cocoa pots?
**Ari** 18:54 they support it, but again, I think that everybody will have to have a stance on what they are going to do in 6 months. Well, not 6 months, like.
Yeah, 6. In 6 months, this is… Everybody has to take a decision, like.
Firebase already announced this, and they are basically going to deprecate on November, because They will want to have at least a month, so they can test the last version.
So, but they say that the last version is going to be on release in November. Unless there's a huge bug on that version, they are going to… they are not going to do any other release.
**nacho** 19:34 Yeah, that's…
**Ari** 19:35 of WEMA.
**nacho** 19:37 Yeah, that makes sense. I would even put it a bit earlier, just in case.
**Ari** 19:42 Yeah, I think… I think we don't have that much manpower to say, okay, we will assess in a month.
**nacho** 19:49 Yeah, we can't fix everything in a moment.
**Ari** 19:51 Yeah, not only that, it's like, some SDKs or some applications has to go and adapt your SDK. We are not… I don't think the amount of persons that have Firebase is the same as the amount of persons that have OpenTelemetry, so I think we should go… into a similar path, maybe announce it, so in October, we are going to… Release the last version, and if there's no really big issues, that's going to be the last CocoaPods version. And that's it.
**nacho** 20:22 Yeah, I think that makes sense, yeah.
**Ari** 20:30 Then, the other thing is that we may want, or not.
To have the pod spec ourselves.
That's another thing that maybe we wanna… we wanna discuss.
**nacho** 20:49 they don't do much harm, right? I mean, them?
**Ari** 20:53 No, and we probably have to change every now and then, like.
the minimum deployment target support and all that stuff, but it's not really a big burden. And again, it will depend on people using that feature. If nobody's using that feature and we don't receive any sort of feedback in years, we can… or a year, we can just remove it and that's it.
**nacho** 21:15 Yeah, I think that makes sense.
**Ari** 21:18 I think that supporting XC Frame… creating a script to support XC Framework, it's… Way much more useful than…
**nacho** 21:28 Yep.
**Ari** 21:29 Highly in the bot spec, to be honest.
**nacho** 21:34 Yeah, definitely.
**Ari** 21:35 The other question… How's the… how… I don't know if you guys know, how we announced this, like, we use the Open Telemetry Swift repo in the README, we do… Have any sort of thing to mention in a blog, or something like that.
**Vinod Vydier** 21:55 I think there is a blog… site, so you can post it there. So that way it is, you know.
Goes out in the communication, right?
**Ari** 22:06 Yeah, yeah.
Okay.
I'll probably ping people from Embrace.
Maybe they wanna come to… to see what they… also tell us what they are going to do, because we don't know.
I don't know if, We want to go and reach Datadog people to see what they are going to do.
Or… We should open an issue with this.
**nacho** 22:34 For example, do they usually read OpenTelemetry Swift channel in Slack? Or what… What's the source of information they use?
Or…
**Ari** 22:47 Random race.
**nacho** 22:48 The README in the project.
**Ari** 22:50 from data.
**nacho** 22:50 And Rith said, yeah, I mean that.
**Ari** 22:52 Yeah.
**nacho** 22:53 I think from time to time, they share.
in the, in the, in the Slack channel, so maybe they just… they… I don't know, maybe they just take a look from time to time?
Or they just track it a bit more.
**Ari** 23:11 Datadog, or Embrace, or whom?
**nacho** 23:14 Yeah, I mean, I, I… yeah, I… embrace or undidal, yeah. Do you… Do you check it? Or do you know if they check the channel, or…
**Ari** 23:27 So, when I was at the race, I was constantly coming to these SIGs, so… I checked because I was… I was trying to contribute, like, actively.
Regardless of my company.
So, I really don't know the others, like, I don't know Datadog, I don't know if Embrace already has, like, somebody that comes to to the SAGs, or that wants to come to the SAGs, I really don't know.
But I can ping directly to people there.
And, and tell them…
**nacho** 23:58 I think… yeah, I think we can… maybe… we have an option, is… that I think can work for most of them.
If we write in this… in the AutoShift channel.
with, hereta, or something like that?
That would definitely at least show a notification to anyone, right?
**Ari** 24:22 Yeah.
**nacho** 24:23 that.
**Ari** 24:24 259 people are going to receive a notification, probably.
**nacho** 24:29 Okay, yeah, that's right. I mean, they are in the tunnel, right? And this is, More or less meaningful.
Change.
**Ari** 24:36 Yeah.
**nacho** 24:37 So I think we, we, we…
**Vinod Vydier** 24:39 We can do that.
**nacho** 24:40 Are we…
**Vinod Vydier** 24:41 I've never.
**nacho** 24:41 bundle.
**Vinod Vydier** 24:42 Or you can post it, because they have other deprecation notifications on the blog.
So… That's… I mean, this is a small announcement.
But I see a lot of these kind of small announcements also on, On the blog. It's like a communication outreach, kind of.
Please.
**Ari** 25:03 Okay.
**nacho** 25:03 Yeah, maybe we can use both, both ways.
Yeah, yeah.
**Ari** 25:08 I think that we should… like… communicated.
deprecating.
**nacho** 25:16 Yeah, I think that that's true.
I mean, channel if we are here, or something like that.
We'll probably reach Everyone.
Before October, right?
They have, like, 3… 3 months, or 3 months to read that.
**Ari** 25:39 Yeah. Yeah, I think that they have enough time. Obviously, I think that we need to… Come up with some decisions, or at least… which are the decisions that we are not going to change, and which are the ones that we are open to discuss. Like, I'm open to discuss on… I don't know, having or not the pod spec.
I'm not open to discuss having a private repository for CocoaPod trunks.
**nacho** 26:06 Yeah, yeah.
**Ari** 26:06 I don't think I don't think we should support this in a private repository, have a third repository with all that stuff.
Like, I don't think that's… that's the best one.
**nacho** 26:16 No, no, no, definitely not. I mean, if anyone needs that because they are there, each company should do that, I think, yeah.
**Ari** 26:25 or if there's a company that stands out and say, hey, we're going to maintain this, okay, you are now the official Cocoa Pods repository to maintain this. And that's it. It's not on us, like…
**nacho** 26:38 Yep.
**Ari** 26:39 It's going to be a painful, painful for them, yes, it's going to be painful, but… I don't know, like.
One, one simple example.
in order to support CocoaPots in Swift.
6, with the new access controls.
If you go and check the pod spec, it has a specific compiler flag in order to achieve that.
So… as time goes by, Swift is going to be releasing things that are more related to the way Swift works. I don't know if you guys… have checked it out, but in Swift 64.3 or 4, there's a, like, a C++, or the Rust.
Dot dot, like this, module, Doug dug method.
Thing?
**nacho** 27:30 Yep.
**Ari** 27:31 I don't know… if… we use that syntax if CocoaPots is going to work. I don't know.
Maybe not, and we'll have to go investigate how does No, no, dude.
how does the underlying system, whenever it's going to compile and link the different symbols, or the different object files, is going to use that feature? So… again, as time goes by, I don't think that cocoa pots is sustainable.
So, I think that the best solution is Start asking your people to… Remove CocoBox, and that's it.
**nacho** 28:08 Yep, he is.
Totally, totally agree. Yeah, I think, I think we, we… you said about that document, we can probably start putting some dates there?
And we review and approve the next meeting. What do you think about that?
**Ari** 28:27 Yeah, sure, sure. One me, I'm going to share again.
**nacho** 28:30 Yeah.
**Ari** 28:31 No, sorry.
**nacho** 28:32 to have something to work about. We can also share that… is that document shareable?
**Ari** 28:39 I'm sharing with… I share the link with you guys, like, anyone with the link is viewer.
**nacho** 28:45 Okay.
**Ari** 28:46 I can… if you have, like, an email, I can give you editor access.
**nacho** 28:51 No, no, no, no, I mean, in theory, we… Yeah, deprecation announcement, Probably can be…
**Ari** 29:03 When… on… by starting June, July, maybe?
When we post this. I don't know, it will not be nod, if there's a… If there's somebody we have to ask in order to write something for the blog.
**Vinod Vydier** 29:20 Yeah, we can always reach out to our, favorite governance committee person, right? Alurita.
**nacho** 29:27 Yeah, okay.
**Vinod Vydier** 29:28 Yup.
**Ari** 29:30 okay, we should bring Alolita about that, but obviously, I think that.
**Vinod Vydier** 29:35 Yeah.
**Ari** 29:36 July.
**Vinod Vydier** 29:36 Yeah, and your document, or, you know, maybe a summary of your document, we can add it as a… blog, and I think Alolita can… You know, find us the right… Yeah. To actually put that blog out.
**Ari** 29:53 Okay.
Do you guys think that… starting that in July would be worth… would be okay.
**nacho** 30:01 Yeah, it provides 3 pool moms.
I mean, probably holidays for many people, but 3 months is more than enough, for a… for a final Release in October.
I would say.
**Ari** 30:16 Okay.
I included this recommended migration period begins. That means that we are completely… Okay with the approach.
Because I think that from the deprecation announcement until we recommend something.
We should have discussions with people.
saying, okay, we would want to have the pod spec, we don't want to have the pod spec, we would need to have the XE framework to script, I would want you to have, like, an XE framework, like, there should be, like.
Some buffer between this and this.
What do you think? End of August?
Or something like that.
**nacho** 30:56 Yeah, yeah, probably. Yeah, it would… yeah, probably, yes.
**Ari** 31:00 It will be… it will be similar to recommended migration, and final release should be Not so far away from each other, because we will just have to create a release, And tested with… All the recommended thing.
**nacho** 31:16 Yep.
**Ari** 31:17 So maybe… End of August.
And this one will be… End of September.
**nacho** 31:29 Yeah, that, that… yeah, end of September is.
**Ari** 31:35 on Coco's importance.
I think it's… What's your reading?
**Vinod Vydier** 31:43 December 6th, right? That is the date.
**Ari** 31:47 Let me check.
Here.
Bless.
December.
I imagine if I was going to do that.
Okay, December 2nd, 26.
I think that with that, we have… I'll find outside.
**nacho** 32:22 Yeah, let's keep that date for now.
**Ari** 32:25 Yeah, we can then tweaked them.
**nacho** 32:27 Yeah, that's right. Yeah, we think about it for next meeting.
And we can approve and go with.
With that, yeah.
**Ari** 32:37 I will keep… I'll read this quick, so we can all agree or not on some stuff. Maybe I can add some comments right now.
Existing cold balance integration will continue to function, because Cocoa potty, it's going to still have those.
Once CocoaPod support is officially discontinued, previously published versions will remain available. No new SDK releases will be published. We'll leave the CocoaPodspot spec in the repositories until further notice. Maybe this is to be discussed.
New feature bug fixes and security updates will only be available through Swift Package Manager releases.
Maintainers won't invest that much. Maintainers, approvers, Priagers?
One invests, contributors.
Oh, contributors.
One invests too much resources into investigating or resolving issues that are specific to CocoaBots.
Is there anything else that we would want to clarify or say here?
**Vinod Vydier** 33:42 Looks good.
**Ari** 33:45 Right.
**nacho** 33:46 You know.
**Ari** 33:46 Recommend them, like, get something?
**nacho** 33:47 I think we can even remove the too much resources.
**Ari** 33:53 Wonderful.
**nacho** 33:54 We can say, won't invest resources. Okay, yeah, I mean.
**Vinod Vydier** 33:58 Some words, yes, always.
**nacho** 34:00 Maybe, I mean, if you really need that, then you ask for it, and someone has… Time for that, and experience maybe can try to help the… But yeah, we… we cannot say… You know, that will be a… You know, a nice… But, by the way, we cannot… And, you know.
**Ari** 34:22 If somebody wants to…
**nacho** 34:23 Yeah, that's… that's right, yeah.
**Ari** 34:26 Yeah, why this is not working in this latest version? I don't… I don't know. Go and figure it out yourself.
We are okay if you scroll…
**nacho** 34:35 Yeah.
**Ari** 34:36 Yeah, definitely.
**nacho** 34:36 Not too much, yeah.
**Ari** 34:39 Hungry.
Okay, recommended migration path. We recommend migrating to Swift Package Manager as soon as practical. Swift Package Manager is fully supported and will be the primary distribution mechanism moving forward.
migration from CocoPass to SPM is simple. There are guides and documentation out there in the community that can be used. I didn't want to, like, post links or have a tutorial on how to do migration, because that's… that's stupid. Like, if you use Twist.
you know how to do it. If you use Bazel, you know how to do it. If you use Xcode, just remove the workspace and use that package, and that's it. Like, it's not complicated.
**nacho** 35:16 Maybe we can also change primary for only?
If we want.
**Ari** 35:21 with me.
**nacho** 35:21 or… the earthly.
**Ari** 35:25 That's good.
Great.
And lastly is feedback. We understand that some organizations…
**Vinod Vydier** 35:38 That was giving us a clear writing tutorial today.
**Ari** 35:43 Yeah, yeah, yeah. No, and that's okay, like.
**Vinod Vydier** 35:46 No, that's…
**Ari** 35:47 We are going to…
**Vinod Vydier** 35:48 You could do it.
**Ari** 35:49 To share is… It's going to… be… Reading the blogs, so… so we don't… we don't want to… To compromise ourselves to things we are not going to do, and that's… that's okay.
**Vinod Vydier** 36:03 Yeah, and also don't confuse the user, too.
Keep it simple. Yeah, exactly.
**Ari** 36:10 So, we understand that some organizations still rely on CocoaPlots-based workflows. If so are finalized in the timeline, we would like to gather feedback before finalizing.
Duh.
Recommended.
Period time length, recommended migration period.
We would like to gather feedback from the community regarding mitigation challenges, tooling gaps, and operational concerns. Please share your feedback via if have issues, the CNCF Slack, or join us in our CSIG meetings.
That's… like, high level. Like, if you… if you have a complaint, reach out, and that's it. Like, but now we have at least a date, end of August.
But again, this is, like, the summary. This is, like, well-known. All of this is well known, so that's why I didn't… Review it. This is probably inky.
**nacho** 37:06 That sounds great to me, and sounds… yeah.
The only thing I will do will be… Just keeping that, for reviewing, thinking about it, just in case we… can find some hole here.
Before approving,
**Ari** 37:25 Yeah, yeah.
**nacho** 37:26 accepting that… In the next meeting.
I agree with what's here now, so if I have any issue, I will post In… in… in… in a chat, if I… if I do that before next meeting, so, yeah.
Let's not block.
**Ari** 37:44 Awesome.
**nacho** 37:45 On the people next meeting, but if anyone has any issue with this, information here.
yes, but let's use our, Our channels to update, and our… Yeah, and if any concern rises us, but yeah, I think it's good.
**Ari** 38:06 Awesome. Okay, let me go and change this. So, end of August is 31.
No, August.
31… 31st?
No, 31.
Like this? This?
or empty.
Asty.
I don't remember.
And September is… Wednesday.
September.
September.
That'll do.
236.
And July, we don't know when, because we'll… we'll probably need Alolida.
**nacho** 38:55 I… maybe we can put… not later than September 30th.
I don't know if we're gonna release that.
**Ari** 39:06 Then, November 3rd.
**nacho** 39:09 Yeah.
**Ari** 39:12 we can then do a… I can then write something like, what means deprecation announcement, what means recommend the migration period begins.
why… why there's a gap between the final release and the CocoaPod support, and all that stuff.
I can write that down after.
**nacho** 39:29 That's what… what we can assure. I mean, if we need to release something between 30th of September and December, because something is really broken, we will do, but we cannot compromise to that.
**Ari** 39:40 No, yeah, it's like, we consider this the final release, unless there's a patch to do.
Yeah. It's going to be the fa- it's going to be probably the last minor release.
That's… that's basically it.
Alrighty. Okay, that's it for the… my topic. It was, like, this one.
and review.
Cocoa butts.
Bam.
duplication.
I will notify, like, the people I know that probably are using this, if they want to join or something like that, but I don't expect anybody to have strong opinions on this, rather than, hey, do all the work, or… Yeah, no problem, we are going to deprecate it too.
So… We wanna review… the repositories?
**nacho** 40:39 Yeah, we can take a look to the SAML APIs if you want. I have not been able to take Oops.
Or review things, but…
**Ari** 40:52 Okay, no worries. So… This one is the only brand new in the OpenTelemetry Swift. Support OTLP profiling is now in alpha. I would like to see SDKs improvements supported, especially for things like OpenTelemetry EVF, EVPF Profiler.
condo profile.
or only… with very high overhead, such as heap profiling data. Bonus for sporting process context and thread context when they are ready.
Profiling working group would become welcome questions or input, and feel free to join the 490 call. All information about the call is at the top of our… okay, so probably this is somebody from the… from the…
**Vinod Vydier** 41:34 Yeah, there is no EVPF.
**nacho** 41:35 CLP profiling. I'm not sure this is not an only… a server-only.
**Vinod Vydier** 41:42 It's a Linux… it's a Linux-only thing, so if you're running Swift on Linux, then you can even look into it, because… eBPF is a… there is an effort on Windows eBPF, I don't think there is anything on Mac.
On iOS. Oh, yeah.
**Ari** 41:59 It's yours.
**Vinod Vydier** 42:00 Yeah, there is… it's a… it's a.
**nacho** 42:02 Yeah, yeah.
**Vinod Vydier** 42:02 the next kernel.
Technology.
**Ari** 42:04 Yeah, seems… seems that it's mostly…
**Vinod Vydier** 42:08 Yeah.
**nacho** 42:09 But yeah, it's a very small… group of users. I mean… So I don't know if that's what…
**Vinod Vydier** 42:20 It's very hot in OpenTelemetry, because there is always all this eBPF, auto discovery, auto-injection.
capabilities, but yeah, I don't think it's relevant for iOS or Mac.
platforms.
**Ari** 42:37 One of these ones?
**Vinod Vydier** 42:42 Actually, I can respond to this.
**Ari** 42:47 You wanna respond?
**Vinod Vydier** 42:47 Yep, yep.
**Ari** 42:49 Okay, I'll… I'll sign it to you, you know.
I'll be there. It's there.
Yeah.
like this.
Alrighty.
and then… There are some pull requests.
I checked the last one, this one, I requested changes.
So…
**nacho** 43:13 Yeah, but…
**Ari** 43:15 this guy found out that Ural Session Instrument Station is not injecting in some cases.
But it also changed the way… We detect that by using conformance.
That is… I… that is reasonable from… from… the Swift developer perspective, but in reality, there are a bunch of SDKs, frameworks, and even part of the Euro session SDK.
Foundation.
That doesn't rely on conformances. Like, it uses the response to selectors and forwards directly to that method.
I would keep that part in the same way as it was, and maybe just the class add method for the ones that they don't have it, that's okay.
But… I… I… I… that… that change on the using conformances is going to break.
other SDKs.
Okay. On apps.
Like, if you go and you create a URL session and an object that implements URL session delegate.
You can go and add the task delegate methods.
manually, like, funk, I don't know, didn't receive the task or something like that.
your session is going to work, it's going to forward them.
And even though you don't have, like, you are the session delegate, and the other conformant, you are the session task delegate, and you're a session… I don't know, download, delegate. You don't have to conform to them in order for your session to work.
And a bunch of SDKs have that problem. One of them, for example, as far as I remember, it was Firebase, like, Firebase.
Has conformances.
like… Response to those electors without having performances.
**nacho** 45:02 Okay.
**Ari** 45:04 There's a really well-known SSL pinning library, too.
that has this problem, right? So, I will just keep it the way it works today.
Oh.
So that's… that's the only new PR from… from this week.
Then there are, like, All of these ones.
The only problem, like, I see everyone has this cultural issue. I don't know if this is new or what.
**nacho** 45:43 Yeah, that… That was asked by the… By the day out.
by the committee.
to add code, QA, QL, yeah.
**Ari** 46:02 Right, so we have to investigate what the… the hell is wrong with this? I'm a big…
**nacho** 46:08 Yeah, it was added just because it was just too up the… We have to…
**Ari** 46:12 No, no, that's okay, it's a cold quality standard, that's no problem, but we should probably investigate why it's breaking.
In all of these PRs? And why it's not, for example, breaking in this one? Oh, it's not running because I haven't approved it.
That's.
**nacho** 46:28 Yeah, brilliant. I think it's brilliant, brilliant.
**Ari** 46:33 Okay, it's failing in the, in the Proto, protobast stuff.
I can check that out.
New topics, code VL.
Oh, this is… broken.
in.
Open. Oh.
telemetry.
Stop.
I am. What?
Okay.
So… That's it, and this is the only other BR?
But I'm not fully aware on how this works.
Oh, no, it's not this one. This one is old.
I don't know, 3 hours.
This is the one, though.
Little warning… Yeah, these are the new UPRs.
This one, I didn't really understand if this was done right.
I have doubts on how the metric storage registry works.
Because suddenly, all the logic that was outside the gauntlet It's… Inside of it.
And now it's returning something different. I'm not really… I don't… I don't really understand if this is intended or not.
So, I was waiting for Bryce to look at this, as he's the one that knows a lot of the metrics.
Thing.
But… Yep.
That's… that's one of them.
And the other one is… This one, update environment mapping getter to non-normalized environment variables.
That Eastern?
But this is not appropriate, isn't it?
**nacho** 48:47 Yeah, I think that it was added by… In all the repositories by… by… these… by them, I don't know why.
Thanks for that, mate.
of the class.
Probably some.
**Ari** 49:43 By the time.
Let me open this for a second.
**nacho** 49:51 I don't know why it changed the name of the cap, to be honest.
**Ari** 49:55 Yeah. I don't know either. That's why I'm trying to… the…
**nacho** 49:59 But probably it's just an AI, maybe close.
**Ari** 50:02 Yeah.
**nacho** 50:03 or Codex just being nice.
And doing things that they don't…
**Ari** 50:13 I don't really know.
Buck.
Oh, it's because it doesn't exist.
**nacho** 50:19 But it had the environment it didn't exist?
**Ari** 50:23 Unless it's in the other repository?
Let me get it? No, it's not… doesn't exist the environment variable getter.
That's why it's changing it. Let me see if capturing error works.
Yep.
Yeah, that… this changes. Okay.
So the idea is to… to ignore non-normalized environment variable names. So, this process was to normalize it.
Carrier, Muppet key.
**nacho** 51:16 Yeah, be, be, yeah.
**Ari** 51:22 If somebody else using this method, if not, he should just remove it, and that's it.
**nacho** 51:28 Yep.
**Ari** 51:39 This is only for the gets.
on GET.
Set.
Okay, so the problem is on the getter, it's not on the setter.
Okay, sounds fine to me.
Because,
**nacho** 52:05 Yeah, I don't know.
Seems tight. I think that probably the normalization method Shouldn't be used anymore, so it could be removed.
**Ari** 52:16 Yeah, it should be removed from this class, I think.
Enlightenment.
Mapping set, though.
**nacho** 52:25 Yeah, also, it shouldn't be the way to normalize that.
I mean, there are normalization methods in… in… Interest or in foundation.
**Ari** 52:42 See the ring.
We are not using the… Awesome.
this bus.
Anymore.
Can you remove it?
Okay.
That's it.
Because there's another class, this is the getter.
Then, oh, this is the measurement.
Wait a minute.
Oh, the setter uses it.
Context propagation, and the setter uses it.
Okay, no, not bad.
Shouldn't be removed.
delete.
I think this is right.
**nacho** 53:45 Okay.
**Ari** 53:47 Okay, I think that it's a rain.
There's a setter in this class that uses the same private method.
Yeah? I nourish it?
That's it.
And the other one is this one.
We should ask Bryce about this.
**nacho** 54:22 Yeah, but friends, he can't take…
**Ari** 54:25 Looks good, fine, but… it is weird that all of this logic was outside the gauntlet, and now it's inside of it. So, I'm not really…
**nacho** 54:38 But it was returning and doing the rest, because it was in the guard, right? Yeah.
**Ari** 54:43 Yeah.
**nacho** 54:44 outing.
**Ari** 54:45 If there was a registry before, it basically returns that registry. Now, if there's no registry.
It's… let's start again.
The ticket is, like, log a warning on a duplicate consumer registration, so… I think that the logic is wrong in that aspect, because if I already have it, And I wanna… Create it again.
You should just log in here, like, in the line 45. You should log in, that's it.
But… I don't know.
**nacho** 55:34 Yeah, it looks strange.
For logging a warning, right?
**Ari** 55:39 Yep.
**nacho** 55:40 Why are you iterating everything again?
For a warning.
**Ari** 55:47 Yeah, but at the same time.
If… if it's not on the registry, descriptor.
It's not here, it's not in the storage.
So… I, I, I don't know, like, this, this logic's… Looks weird to me. That's why I wanted, like, Bryce that knows better at this park, if you can take a look.
**nacho** 56:12 Yeah, it's also, I mean, he also changed the name of the variable, so it's more difficult to compare.
What really changed?
Yeah.
**Ari** 56:21 That's true.
**nacho** 56:22 Jesus.
**Ari** 56:24 To be reviewed.
This one.
**nacho** 56:30 Okay.
**Ari** 56:37 Okay, this link.
Buddy.
Yeah, and that's it, because… Or doesn't have new issues?
So… I think we're done.
**nacho** 56:51 Okay.
**Ari** 56:55 Just in time.
**Vinod Vydier** 56:56 Yep.
**nacho** 56:57 That's…
**Vinod Vydier** 56:59 Alright, that's good.
**nacho** 57:00 Yep.
**Ari** 57:00 Yeah, next week.
**nacho** 57:02 See you next week. Have a great weekend.
Bye. You're welcome.
**Vinod Vydier** 57:05 bye.
**Ari** 57:06 Bye bye.
