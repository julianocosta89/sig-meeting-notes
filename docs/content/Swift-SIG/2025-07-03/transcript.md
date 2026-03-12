SIG: Swift SIG
Date: 2025-07-03
Duration: 43 minutes
Zoom Recording URL: https://zoom.us/rec/share/JFIAKb_0CL6y860E3GPEeISrOfYGwrT-D_Gx0Xqs6FqrISYnNd0fDFkpNSp1vQ-T.ETP0HIDOJJbSyQUR
============================================================

## Zoom Recording Transcript

**Alex Cohen** 01:47 Hey! There!
**Bryce Buchanan** 01:50 Hey!
**Alex Cohen** 01:51 How's it going.
**Bryce Buchanan** 01:52 Good! How are you doing.
**Alex Cohen** 01:54 Good. I don't think we've met I'm Alex. I've been messing around with the With hotel a bit, and I've been doing some consulting for embrace. So it's been going crazy.
**Bryce Buchanan** 02:06 Nice to meet you.
**Alex Cohen** 02:08 We do it.
What do you do outside of hotel.
**Bryce Buchanan** 02:12 Oh, I I'm at elastic right now.
**Alex Cohen** 02:17 Oh, cool!
**Bryce Buchanan** 02:19 Yeah. Yep.
Working on their mobile agent as well, and and a bunch of other stuff, Kibana, and that sort of thing.
**Alex Cohen** 02:28 You guys use open telemetry internally.
**Bryce Buchanan** 02:32 Oh, yeah, very heavily. Yeah.
In a nutshell.
**nacho** 02:43 Hey!
Good morning!
**Bryce Buchanan** 02:46 Good morning.
We'll give a couple more minutes to see who all filters in here.
If you have any topics. Alex. Feel free to add them to the to the meeting notes here.
**Alex Cohen** 03:11 Absolutely.
**Bryce Buchanan** 04:51 Alright. Let's get started. Okay. So topics from last week, the data compression discussion, not show. Is that a Pr regarding that?
**Alex Cohen** 05:04 Well, I actually put that one up, and that was my main reason for for being actually I know that we already have a Pr for this, or at least a branch somewhere. But it's been causing, at least for embrace. It's been causing issues like currently where where we could be losing customers because of this. And I imagine that some some other people are just not gonna report the problem right? They're just gonna see a problem and move on either away from open telemetry, because it just didn't work out of the box or embrace, or any other company that might be using open telemetry or the open telemetry library. So that's sort of why I I feel like it's it's more pressing than waiting for the next version. I know. I know I read in the issue that we might want to wait for the next version, but I feel like we might wanna think about it a little bit more, and possibly just put out a a dot release for it. I understand that it's breaking in the name of the of the library. I sort of feel like it's more breaking for, for, like the whole ecosystem of people trying to use all of the the other sdks that depend on this, or even open telemetry, so it might be worth making a a small concession on this one, and having a breaking change without a major version.
That's my pitch.
**nacho** 06:29 Yeah.
yeah, yeah, there is a, as you said, there is a branch with very similar things that that this pr on that, and and that that's the only difference. And it's very similar to this one.
and I was thinking that the yeah, the issue comes from
**Alex Cohen** 06:54 Yes.
**nacho** 06:54 That's from spm.
And I'm not sure if the issue comes from the target name or it comes from the library name.
because maybe we could.
**Alex Cohen** 07:08 Sorry go ahead.
**nacho** 07:08 That change the library name, but not the class name, or some or something like that, that wouldn't be so painful currently.
instead of changing everything. That's something that just came to my mind if we could. Just I don't know if it's there is something there. I think it's the library. Name the one that's different the one that makes Swift Pm. Fail.
**Alex Cohen** 07:39 What's interesting here is I didn't even think about just changing one of them or the other, because I think this code is taken from another library and brought into open telemetry. As is, and then name not change, and just left there. We might have made changes to this, so regardless of that, there's a conflict of of like, okay, the code that we're reusing is conflicting with the original code that other people are using in their library, so regardless of like the naming we should at least make it very very clear that this whole thing is taken from there, and it's renamed, and it should really be only internal. It should probably not even be exported. I noticed that it's used in one place or 2 in the exporters, I think maybe but we can figure something else out for that. But I can't answer your question as to is it just the target, or or the the library, but I not.
I'm not sure about that.
But I think where I'm trying to go with this is, I'm looking. I'm looking for. If it's possible to get something out there quickly. Cause it has been a while since it's it the issue has existed, and we don't like. We don't have control over anything. I tried a couple of things. I tried module, alias aliases, to like rename things like from the from this, from the the application side or from the SDK side. Those didn't didn't work so like I've tried a lot of things, and this is really what I've come up with, which is probably the best solution for right now.
so like this is this is this is the proposal that maybe we can get in fast and like, do we actually know that it's breaking changes for anyone?
Like, I know, it's hard to know who's using open telemetry, and if it's a breaking change or not but maybe we could put it out as a as a release candidate of a minor version or a bug, fix, or something like that, and see if there are any complaints, or ask the community somehow. Cause even internally, we only use it in 2 places right or open. Telemetry only uses in 2 exporters, and I think it's the Hotel Http. Exporters. I can't remember the exact names, so there's not. There's not actually much use to it.
So I I would really I it would be much appreciated on our side, and I think a lot very appreciated from a lot of other people that might run into the problem.
**Bryce Buchanan** 10:13 Just
**Alex Cohen** 10:14 Do something fair.
**Bryce Buchanan** 10:16 So I think that that might maybe we can do a a a beta release or something like that for 2 dot. Oh, the problem is, one of the big changes that was going into the 2 auto release has been merged. And so now we're basically looking at the the you know the major major revision versioning in in the next release. So whether or not this is a breaking change is kind of a moot point now, because you know, we're gonna be doing our our big 2 dot. O release. Now.
**Alex Cohen** 10:53 We could. We like I I totally understand that. But we could base make it a just a bug release or something or point release and just base it off of the released the what's released. And I'm I'm not sure what the current version is. 1.1 4 1.14. I can't. I can't remember exactly, but just a quick release off of that, so that we can get people going, because I think 2 point O has a lot of other stuff like the stability metrics in it, and things like that which are which are going to be great and large, but they might take longer to get to 2 point O to to an actual release, whereas this is at at least we feel it's it's pretty important to try and get this fixed up quickly. For like it, it basically blocks us from from moving forward a lot unless unless we actually use our own fork, which we desperately don't want to do. We'd love to the official version.
moving other other libraries that we're using, such as chaos, crash and things like that. We've moved to the official repo releases instead of having our own forks. So you know, this is all. This is all. With that in mind.
**Bryce Buchanan** 12:04 Okay? I mean, we could. We could consider branching a 1 dot x off of the last release version.
And merge that in. Merge this into there for for you, or we could just release 2 dot. Oh, I'm not sure what all is blocking us on that. It. It does look like Nacho. You have a thread race condition in the metrics that you've discovered.
**nacho** 12:29 Yep, yep, probably want to fix that basically running, running the tests. So they were not like big issues. But I have not. I mean, I was trying to fix them.
Like there are like 4 or 5 places where they sold just running the test.
But yeah, apart from that. I. I also had a pr, that also is a breaking change for the name of the span. SDK, basically.
**Bryce Buchanan** 12:56 Yup, I saw that.
**nacho** 12:57 And and I think with that, yeah, we we are. We are ready to release at 2 dot. O.
**Bryce Buchanan** 13:04 Hmm! Maybe maybe what we can do is I So I'm not sure I can't remember how accommodating spm is with with pre-release. Candidates like you can make a you can make a set as pre release here.
I'm not sure if if if spm will let you release something with a pre-release in it or not.
**Alex Cohen** 13:39 I think, whatever like, we can point it to a branch or or anything like that. We want to. We're just hoping to point it to releases as like as much as possible right? Right?
Especially if anyone outside is like outside is using Opentel in there, like outside.
**Bryce Buchanan** 13:55 I I know that I know that apple won't let you build for release. If you are referencing, non releases in your in your swift package. So like. If you want to release an app with a branch in it. It won't let you do that. I'm not sure if it will let you do that with a pre-release or not.
But maybe what we can do is just do like a
**nacho** 14:19 Yeah, if if you want a branch, there is already a branch that has these changes compatible.
**Bryce Buchanan** 14:25 Yeah, yeah.
**nacho** 14:26 So you you could also point that to that branch if you can build and release with our brand.
The branch name I don't remember is something like.
**Alex Cohen** 14:37 Yeah.
**nacho** 14:37 That's nice.
**Alex Cohen** 14:38 Oh, that branch!
**nacho** 14:39 Yeah. And did you try with that brand.
**Alex Cohen** 14:42 No, I didn't, actually, because, like I trusted that. It said that branch worked, and it was it. It fixed the problem. But that branch had like I can't remember exactly, but it seemed to have a lot of changes in it versus.
**nacho** 14:56 It's just it. Just the change that you have rebased on top of Main.
**Alex Cohen** 15:02 Hmm.
**nacho** 15:04 With the last public release. So if we release 1 17.1, that branch is 1 17.1. With this change of the name just revised.
**Alex Cohen** 15:16 Okay.
**nacho** 15:18 So I mean it. It will solve lots of changes because it's already based, since it was created from from all the different versions that we have revised. But but that branch is there so that can be used.
If you can use branches that that's done there.
If you cannot, then you need a number. If you.
**Alex Cohen** 15:36 We can definitely.
yeah, we can definitely reference the branch. But now I'd have to check and see if we could release with it. But do we actually want to release with the with the branch is something else like we're releasing an SDK that would depend on a branch of the of open telemetry. Which, and like the our our SDK itself like is people use it and pay a lot of money to be able to use it. So releasing it on a branch is not. I like, I understand that it would be okay. But getting that passed through everyone and and it working in the company, we'd prefer a release like an actual, real release.
Obviously.
**nacho** 16:17 Okay. Yeah.
**Alex Cohen** 16:18 Excellent.
**nacho** 16:19 I mean, yeah, yeah, that that makes sense. I I can understand that. That's why I say, we we we are gonna really release a 2.0 brand now.
And if you can use that that branch, I mean, yeah, I know you prefer that. But you will probably change to dot 0. After that, I mean.
**Alex Cohen** 16:39 Well, I mean.
**nacho** 16:40 You can. You can compare, I mean, if you take that Grant and you and you do something like a Pr against Maine.
Github would show you the the real differences there. And you you will see that. Only that that change.
But we yeah, if we release that Beta price. Sorry. We should put also that this change within. Yeah.
**Bryce Buchanan** 17:04 Yeah, yeah, yeah, I was just testing to see how angry spm is. Gonna get if I have like, beta dash beta one in the version.
Okay.
yeah. So like for the for the 100, like, there are a couple of breaking things that we want to get into to the 2 dot O, and so I'm hoping maybe we can like kind of like, release them incrementally, as like betas, or whatever just so that we have one big version change with the 2 dot o rather than having several breaking releases like 2 dot O, 3 dot o that sort of thing.
Because we wanna we wanna get Swift 6 support in here as well, I believe.
But I think that if we can probably come up with something. If if spm isn't cooperative, maybe like a 2 dot o dot o dot one or something I don't know
**Alex Cohen** 18:04 If you put, if you get this into 2.0 and a beta release, I will. I will try with the Beta release, at least internally, and make sure everything's fine and stuff, and we'll see if we're agreeable to release with it, and maybe we won't be making a release before 2 point. Oh, is released.
By by this group. Do we? Do we have any inclination as to when 2 point oh, might be released. Because if 2 is gonna be released like within a week or 2 or 3 or something like that, then like it's, there's absolutely no problem, because, like it's it's gonna take a little bit of time to do a release, even if we merged into 1 point something. So right.
anyway. So we're not. I'm not pushing like I need this tomorrow. Give it to me tomorrow. But so like, if 2.0 is out within a few weeks, like.
I don't have a problem with that, and it's great.
**Bryce Buchanan** 18:53 I think the the one other big. So we got the metrics able metrics merged in. We just need to do the rename, which is not a big deal. It's like a find and replace and then we are. I want to talk about a little bit about Swift 6 today and see what the big hurdles are. I was playing around with it yesterday and ran into some but we can. Maybe we can.
You know, table that until that, then. But I think that that's really like Swift 6 is like the big blocker at this point. And so I don't know if we want to. We'll have to discuss that and figure out what we want to do. But I I don't foresee if if Swift 6 is gonna take more than a month to sort out. Then I think that we should do a 2 release before.
**Alex Cohen** 19:40 Got it.
**Bryce Buchanan** 19:41 Yeah, without it? Exactly. Yeah. So I think I think that we're all on the same page here regarding regarding a release with this breaking change.
And and there it sounds like there's a several other little changes that we want to make. So I think that's fully reasonable. Within the next week or 2. I'm off next week, so I won't be able to do anything there. But I'll be back the week after, and then, and you're not sure if you want to move forward with a 2 dot O release while I'm while I'm out. That's fine.
But just.
**Alex Cohen** 20:14 Just so, I'm clear just to reiterate. Just so, I'm clear. When how many weeks is it within a month, or is it within 2 weeks. I'm not. I'm not sure.
**Bryce Buchanan** 20:22 I would, I would say, within a month. Certainly.
**Alex Cohen** 20:25 Okay, cool that that works that works for me. That's
**nacho** 20:29 Would probably be 2 weeks.
Yeah, 1 1 month, for sure. Yeah.
**Alex Cohen** 20:37 Yeah, that's.
**nacho** 20:37 But there are some things that could be missing. And also the 3 6 changes probably are. Yeah, I think they are. Gonna be too much.
To make them this work here.
**Bryce Buchanan** 20:51 It seems it seems like it's allowing it. I'm I'm not sure until you try to do a release. Build on an app.
**nacho** 20:58 Yeah, that.
**Bryce Buchanan** 20:59 We might, it might not like it, but
**nacho** 21:03 Yeah. The the problem is, when you try to use that branch in your project and you want to build for release.
**Bryce Buchanan** 21:12 Yeah, it's probably when it'll complain.
**nacho** 21:14 It's not how you generate it, but how, when you use that in a release.
**Alex Cohen** 21:21 So we have some like, obviously embraces an SDK, but we have some internal apps that we send over to test flight and stuff. So that's basically production. So I'll be able to try that out and report back if it if it works like as soon as we have this branch. I would I would, or this Beta release, I would be able to to check it out.
**Bryce Buchanan** 21:44 Cool.
I don't even see where you're. Oh, here it is.
So all right are. Is this acceptable open telemetry, data, compression.
**Alex Cohen** 21:58 It doesn't need to be this one, I think the other one. We already had a branch up for that, that if you wanted to just merge that branch into main, or it might be already as long as as long as it works. It's fine with me. I just use that name because it.
**nacho** 22:11 Yeah, I think it. Yes, the name is hotel data compression. I think that one you can. I mean, you can check that ranch quickly, if you in the project.
Yeah, yeah, that's right.
**Bryce Buchanan** 22:34 Oh, okay.
**nacho** 22:36 Yeah, that was the. But yeah, basically, it's the same.
**Bryce Buchanan** 22:40 I I yeah, I don't know. I I'm not the I don't care either way. We do have hotel swift logs, but open, you know are the SDK. Is open telemetry? SDK, so it could go either way.
**Alex Cohen** 22:51 I didn't know which one to choose.
**nacho** 22:54 Yeah, I choose O hotel, only just because the other is like the.
**Bryce Buchanan** 22:59 That's like, yeah, they've.
**nacho** 23:01 Yeah, the official name so it was like related, but not official or not.
**Alex Cohen** 23:06 Okay. Cool.
**nacho** 23:06 The the core of the library itself. But yeah.
**Alex Cohen** 23:11 Can I ask? Why? Why did we choose to force it to be static as much as possible within the library? It's
**nacho** 23:19 Yes, yeah, it it. It was mainly for historical reasons. It was because people were not able to link it properly. Never.
**Alex Cohen** 23:28 And are we? Are we against adding a dependency on the original library for Summary, where we pulled the code from, instead of actually importing it like like that. I think the Data Compression library is from somewhere else. Right? It like it's it could.
**nacho** 23:46 Yeah, it's an Apache Apache, 2.0 code. And and we have that copied there in in inside the project. We couldn't there. There was no library then to use, or something like that. There was no spm project, or something like that when it was created.
**Alex Cohen** 24:03 There is now.
**nacho** 24:06 Could be. Yeah, that could be.
**Bryce Buchanan** 24:08 Yeah, maybe maybe the correct thing to do is to remove this, the code we have in there, and just use this one instead.
**Alex Cohen** 24:16 This is this is, it has a package.
**Bryce Buchanan** 24:19 Yeah.
**nacho** 24:19 That the yeah, that could be a a good reason.
**Alex Cohen** 24:25 No dependencies, it supports, supports everything we need. I think I.
**Bryce Buchanan** 24:31 I think that all your problem right.
**nacho** 24:33 Yeah, definitely that that's that's way. Better. Yeah.
**Bryce Buchanan** 24:40 Alex, do you mind reconfiguring your Pr. To do that?
**Alex Cohen** 24:43 Yeah, definitely, I can take care of that.
**Bryce Buchanan** 24:45 Great. Thank you very much.
**nacho** 24:47 Yeah, and and yeah, and we and we can go with these 3 definitely.
**Bryce Buchanan** 24:51 Excellent.
**Alex Cohen** 25:00 Could you? Just paste the the the URL in there for a data compression library. Thank you.
**Bryce Buchanan** 25:09 Certainly. Yeah.
This. This is the one. Right? Yeah.
**nacho** 25:14 Yeah, I think that's 1. That's the one yeah.
**Bryce Buchanan** 25:21 Oh, oops! That's your cursor there, not mine.
Here we go.
Alright cool, alright any let's see any other topics from last week. Oh, yeah. So cocoa pods. I fixed this. I was able to sort that out. It was It was due to the core telephony. trying to be linked in versions of the OS or OS versions that don't support it.
For, like the network status stuff for the the you know, like sell information which doesn't exist on Mac, and and like watchos.
So that has been corrected.
span attributes, extensions that was all merge metrics. Pr. Is merge. Just need to do the rename, and then that'll be that'll be ready to go all right. So alright, swift 6. Let's talk about this. So I was playing around with Swift 6 a little bit yesterday.
I haven't worked through all the issues, but the one real sticky issue that I ran into was the semantic attribute generation. And I'm wondering it seems like we have a script in the semantic attribute, or that generates the semantic attributes.
it hasn't been running a long time. It uses this template.
and I'm wondering this also looks like it was generated. And so I was wondering, does anybody not sure? Do you know where this was generated from? Or.
**nacho** 27:26 No, yeah, I think it.
Yeah. I think it.
It was probably done by. I don't remember his name now. Sorry he was from from Uk right.
**Bryce Buchanan** 27:50 Right, the the original maintainer.
**nacho** 27:55 Of this of this part. I think that, yeah.
**Bryce Buchanan** 28:00 Yeah, unless.
**nacho** 28:01 Ha, ha, yeah, I I yeah. He. He was early in the project helping. Yeah. Sherlock. Yeah, that's.
**Bryce Buchanan** 28:09 Oh, okay.
**nacho** 28:10 Yeah, he! He was the one who added it. Yeah.
**Bryce Buchanan** 28:12 Oh, okay. Okay.
Interesting. All right?
**nacho** 28:18 Yeah, and what's the problem with that?
**Bryce Buchanan** 28:20 Well, so the let me see, do I have? I don't know if I have.
**nacho** 28:26 Yeah. But yeah, I also had a.
**Bryce Buchanan** 28:28 But the the main issue that I'm running into is the static static variables that are that are in it. And
**nacho** 28:43 Okay.
**Bryce Buchanan** 28:43 Swift 6 is not happy with those. So you know, it's not a big issue, because I can just add, like a an override for the warnings or for the errors that it that it generates. The issue that I have is that it was all. It's all generated code. So I was hoping that we could regenerate it, using Swift 6 so that it just doesn't. Oh, where is it? It's under traces.
Here we go.
Yeah, so oh, that's what the hell!
Oh, that's in. Okay, specifically, these public static. Let's it just isn't happy about this, because it's like. I don't know if that's mutable or not.
And so.
**nacho** 29:33 Okay.
**Bryce Buchanan** 29:33 Yeah, I can probably just update the template to add, like an unsafe unsafe warning. Let's see, what is it?
Non isolated unsafe. So.
**nacho** 29:48 Yeah.
**Bryce Buchanan** 29:48 Yeah.
**nacho** 29:49 The the thing about the swift is change. That is, that it seems a lot with xcode 26, and with 3, 6.
**Bryce Buchanan** 30:03 Point 2.
**nacho** 30:06 In a way, better so it it gets really better, I would say.
**Bryce Buchanan** 30:12 Oh, okay.
**nacho** 30:12 In the way it works, but that will only come in October.
**Bryce Buchanan** 30:17 Oh, the limitations!
Gotta wait a little bit.
**nacho** 30:20 And with the limitation.
**Alex Cohen** 30:23 I don't know if it's actually mutable or not. But can you just make dB system value sendable and it should quiet. Yes.
**Bryce Buchanan** 30:32 Yeah, we could do that as well.
**nacho** 30:34 That could be. Those are all static, so you can probably say that it's sendable yourself.
**Alex Cohen** 30:40 Well, just like.
**nacho** 30:41 Or I'm 16 00, one.
**Bryce Buchanan** 30:42 Doesn't sendable mean that it's only accessible on the main dispatch queue.
**Alex Cohen** 30:48 No, I mean, it means that it can be moved across threads without problem, basically because it's.
**Bryce Buchanan** 30:53 Oh, okay, okay, okay, alright. Yeah. I'll I'll look at that. Then I was just trying to get it working as is. So I figured just flagging them as non isolated, unsafe for now would would be okay. But yeah, I can make that sendable, too.
**Alex Cohen** 31:09 Yeah, so.
**nacho** 31:09 Yeah, I think the.
**Alex Cohen** 31:11 Sorry.
**nacho** 31:11 Yeah, those looks are all like, yeah, static things. It will say, Dv system values. If you say that that's sendable or unchecked, sendable in the definition.
**Bryce Buchanan** 31:23 It will probably silence all of them. Just after this customer string convertible, you put a comma and say.
Send the ball.
**nacho** 31:33 Send double or uncheck sendable. If send out.
**Alex Cohen** 31:36 Probably doesn't even need unchecked since it. What is? What is the how does it hold the strings? It just like a let.
Oh, let let string.
Yeah, I don't know the variable as long as it's not var, you should be okay to make it sendable, otherwise you'll need to make it unchecked.
**nacho** 31:55 Yeah, but it has the description. Probably that's the.
**Alex Cohen** 31:58 Oh, yeah, that's.
**nacho** 31:59 The one that we'll say.
**Bryce Buchanan** 32:06 Yeah, it's unclear. Why, this isn't just an enum.
**nacho** 32:11 Because the way it's auto generated yeah.
**Bryce Buchanan** 32:15 Well, what's weird is that these ones up here are enums, and they're auto generated as well, aren't they?
**Alex Cohen** 32:23 Probably had bigger plans for this.
**nacho** 32:27 Yeah, because it has also has some value in itself.
So it has that value that is initialized.
**Bryce Buchanan** 32:35 It's like a it's all it's like a tuple or something.
**nacho** 32:39 Yeah.
**Alex Cohen** 32:39 So no, that's all the same thing. It's like that. dB, system values all the lets run run through the the init custom value, and they're assigned to.
**Bryce Buchanan** 32:49 Oh, yeah, and it just, yeah, yeah.
**Alex Cohen** 32:52 Yeah.
**Bryce Buchanan** 32:54 Curious.
It feels like it could just be an enum.
Okay?
Well, anyway.
I'll tinker around that a little bit more. So it sounds like there's a there's a path forward on that. I might not even need to necessarily. rewrite the template. Maybe just a little bit
**nacho** 33:21 Yeah, that that's what I also the thing is that with approachable concurrency that comes with xcode 26, I think I think things make more sense.
and things are more naturally worked out.
I don't know your opinion on that. If you have some experience with that.
we can make that with 56, with.
**Alex Cohen** 33:45 I think the Olympics.
**nacho** 33:46 But we will have to probably change that for Swift 6, 2.
**Alex Cohen** 33:51 I think the biggest change is that everything is I think it's by default main actor based with a I can't remember what they call it, but I don't think that'll have much much effect on this right here.
**nacho** 34:04 Yeah, for for a framework it should be non-insulated by default. But now non-insulated methods followed that of the the they use the same actor the same that from when, where they are called.
and and that that feels way way more natural for all the things. And you don't have to put many actor in so many places. You don't have to add so much extra code that once once we move to 3, 6, 2, we will have to remove I might move my my, the the product I I am doing to shift 6 point 0. And now, what for? Swift 6.2. I had to change several things So that's a risk that I think we should try not to address now, and because it will be much easier later. That's my opinion.
**Bryce Buchanan** 35:07 Okay. Yeah.
**nacho** 35:08 Yeah, so.
**Bryce Buchanan** 35:09 Yeah, yeah, if that's the case, then maybe we should just leave it until October, October and do a do like a 3 dot o release or something for that. I don't know.
**nacho** 35:17 Yeah, or even a 2 dot one, or whatever. I don't think that that's not a breaking change.
**Bryce Buchanan** 35:23 Oh, okay.
**nacho** 35:24 I would say, you can still link with a framework that has different 3 versions, so.
**Alex Cohen** 35:33 If it's only the semantic attributes gives. Give a sendable a try. Yes.
**nacho** 35:39 There are many things there are.
**Bryce Buchanan** 35:42 Yeah, there's we've got lots of Singletons and stuff like that. So yeah.
**nacho** 35:47 There are a lot. Really. I also created a branch with trying that long ago. And and yeah, it. There are many changes that I tried one.
**Bryce Buchanan** 35:58 SDK, and gave up after 15 min on my 1st try. So try again at some other point, but not today.
Yeah. Okay, so I I think that that is reasonable. We can. We can table swift 6 until our until swift, swift 6 dot, 2.
**nacho** 36:15 Yeah, we we could create a swift 6 branch. If you want Bryce to work on that.
**Bryce Buchanan** 36:21 Yeah.
**nacho** 36:21 With, but I will use only the the latest xcode beta, the 26 one, and we can work on that I. And that could be in October, but can be a dot one version if we want.
I think that that's a good option.
**Bryce Buchanan** 36:43 Okay, I might. I'll. I'll probably look into that the week after next.
**nacho** 36:51 Yeah. Try with text code 26.
Yep, yep, the it will be more straightforward.
**Bryce Buchanan** 36:59 Alright sounds good alright, so that well, we won't block version 2 dot o for that. Then cool alright nacho version 2 dot O.
**nacho** 37:13 Yes, yeah, basically was about the same we have been talking. I put that before we started talking about these other things. I. I also created 1, 1, 1, 1 rename on on the span for the SDK. The record events a readable Spanish, I mean. It was a such a long name. I don't know why it was chosen like that. And I think that is a good moment to change that to a span. SDK, so it follows the span. Api name.
I also, added I, there is a a Pr. Open. It also keeps the type, alias for for the old name.
So it shouldn't be an issue for code that I mean, it shouldn't even break existing code. But it has added a a warning for the renaming. So, oh, yeah.
anything, even if they use that, and also but will show a warning with the deprecation and the rename.
**Bryce Buchanan** 38:15 Cool.
**nacho** 38:16 Which should be quite did it without issues, I hope. And and apart from that, yeah, there was about our plan for 2 dot 0. I maybe that renaming is something that we could add also add for the metrics for the old, and they all names that when they keep their stable in the name so we could maybe update that, I would say, and keep.
**Bryce Buchanan** 38:50 I was planning on on putting it or putting or doing that today, getting a pr, yeah, yeah, great.
And so.
**nacho** 38:55 If you put a type, alias for the old name, so they can also update their old names to the new one. That will be great. And apart from that, I think we can go.
Yeah, we can go with it. There is this just running the test with threat sanitizer. It's showed some thread race condition in the metrics.
They're worth 4 places where there were threat race condition I had to start the Pr with fixes for them.
But I still have not finished. But yeah, that will be great if we can release with that.
**Alex Cohen** 39:32 That one running was that one running tests with the thread sanitizer? Or was it running something else under the thread sanitizer?
**nacho** 39:41 No, no, just just the test. Yeah, just running the test. It showed. Yeah.
**Bryce Buchanan** 39:47 So we've had a warning on the stable metrics for quite a long time.
Oh, I see what you're saying. Yeah, you're right. Okay. Yep.
Yup, yup, yup, Yup, alright. Yeah, I'll do that. I'll I'll do the type. Alias for them.
Shouldn't be a problem.
**nacho** 40:08 Yeah, I will just re remove the stable from the name.
**Bryce Buchanan** 40:13 Yep.
**nacho** 40:13 And and use table. Yes, stable equals the the new name without the stable. So it it's naturally named for for everyone.
so we can remove the warning and the pile, alias in the future if we want and that. So yeah, we we finish all day transition.
**Bryce Buchanan** 40:36 Cool. Alright?
Okay, yeah. And then the thread risk conditions.
Working on a Pr for that neat, not Joan.
**nacho** 40:52 I have started working. But if any other one wants to do that and address it yeah, that can be faster, if I I don't i mean.
**Bryce Buchanan** 41:04 Look at it cool.
**nacho** 41:06 Putting some logs or some queues that handle that in the best possible way.
But yeah, no, not not a special not any special.
Reason to do it myself. If anyone wants to take it.
**Bryce Buchanan** 41:30 I'm not gonna be able to to look at it until at least the 14.th
**nacho** 41:34 Okay. Then then I then I can take that. Yeah.
**Bryce Buchanan** 41:42 Okay, during all right.
Any other topics?
**Alex Cohen** 41:49 Sorry just to go back to Version 2. Is there any way that I I might be asking too much here? But could you put it in there as a bullet point that we we wanna try and target within the next month to release.
**Bryce Buchanan** 42:00 Oh, sure. Yeah.
**Alex Cohen** 42:01 Just so. Just so. When I go tell the the the team at embrace. I have something to point to.
**Bryce Buchanan** 42:08 Sure.
**nacho** 42:08 Okay.
**Alex Cohen** 42:09 I think I'm making it.
**Bryce Buchanan** 42:10 Let's see here, maybe a release. By the 7th of August.
**Alex Cohen** 42:19 Sounds good to me.
Thank you.
**Bryce Buchanan** 42:23 Cool.
Alright, if there's no other topics let's call it here.
I'll get that that pr in today for the stable. Rename and yeah, if if you're able to fix this thread race condition or decide, it's not an issue, feel free to release while I'm out next week, or wait until I get back and.
**nacho** 42:51 Yeah, I mean, I think we we can wait for your you back and just confirm everything is is nice for us 2.0 right?
**Bryce Buchanan** 43:03 Cool.
**nacho** 43:04 Yep, correct.
**Bryce Buchanan** 43:08 All right.
See you in 2 weeks.
**nacho** 43:12 Yep.
**Alex Cohen** 43:12 Here we go!
**nacho** 43:15 But.
