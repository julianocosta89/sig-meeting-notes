SIG: Android SIG
Date: 2025-06-17
Duration: 27 minutes
Zoom Recording URL: https://zoom.us/rec/share/tcpBoC04RkcvTgqD_CEOtpHBS7T7m1Ho5nl87HWaCNmlYL0jSt9JK66ltBB8qAX8.TnOBOuOiryM8YtC2
============================================================

## Zoom Recording Transcript

**Jason Plumb** 00:27 Hello!
Good morning!
**GZ Gregor Zeitlinger** 00:36 Oh!
**Jason Plumb** 01:07 Well, I will share my screen. But there is a very light agenda today.
By light I mean nonexistent.
**GZ Gregor Zeitlinger** 01:25 Then it's gonna be a quick meeting.
**Jason Plumb** 01:27 I think so. I need to circle back on this clever chuck. I think I gave you a review, but I haven't come back to it. So need to do that today probably looks like there's been some good discussion.
Hi, Hanson.
**Hanson Ho** 01:47 Hey!
**Jason Plumb** 01:52 We have a very light agenda. I did pull up clever Chuck's click instrumentation. That's had a lot of discussion, I think, is getting pretty close.
and there's nothing else on the agenda today. So.
**Hanson Ho** 02:09 I have to circle back. I looked at last week, but I haven't looked at it, but I saw you approved it, so I assume it's good to go.
**Jason Plumb** 02:17 Yeah.
**Cesar Munoz** 02:21 Hello!
**Jason Plumb** 02:28 What are these? These are? Probably, yeah.
Yeah. So Sonatype has a pretty serious outage for the last day, like literally 4 0, 4 for any of the snapshots.
and I clicked this. I clicked this feedback button and opened a ticket.
and they mailed me back and said, Yeah, we know about this. It's a major outage. They said it should be fixed in about 9 h, and that was yesterday afternoon, so it has not yet been fixed. So that's what these build failures are that we're seeing these. That's and that's happening across across a lot of repos now. And I don't know if this is fallout from them, preparing for all of the open store. Open source stuff moving over to Central, or I don't.
There's no root cause. But like they're Yeah, this leaves a little bit to be desired, like it's kind of. It's kind of not telling the full story here.
**Hanson Ho** 03:39 Yeah, we don't use the snapshot. So
**Jason Plumb** 03:43 Well, we publish to them is what this is right? So it's trying to do.
So that that's the regular build process. Failing as it's trying to push a snapshot.
**Hanson Ho** 03:53 Oh, okay, right? Right? Cause we're we're pointing to snapshots and not not the latest releases. Got it? Got it? Got it.
**Jason Plumb** 04:00 Yup!
**Hanson Ho** 04:04 That's not ideal.
**Jason Plumb** 04:05 No, I do think so. If I do think that the regular is this thing working?
No, just the regular repository does not look to be working, either.
It's a bummer, anyway. They know about it.
**Cesar Munoz** 04:27 So essentially, nobody is able to release anything that's awesome.
**Jason Plumb** 04:32 Like, I mean May. So the old stuff is still up that it's the the deadline for migrating was June 30, th so I'm assuming the the Ossh stuff is still up. Let's see, how do I get there? Maybe this thing?
Yeah, like, I'm assuming still working.
**Hanson Ho** 04:49 Yeah.
like, if you publish like for real, for real, it works. It's I think it's just a snapshot repo that's not working.
**Jason Plumb** 04:56 Well, we changed the publishing. Is the thing right? So this repo right here is hosted on the ossh. This thing.
I think that's what it's called.
Yeah, this thing. So there's a notice here that says this will be reaching end of life right. And then there's there's instructions on how to migrate. We did this migration like a week ago.
Across the Java related repositories.
But what that means is that we publish the 2 new 2 new Urls, and you should be, I think the Gradle Plugins also understand those new Urls.
So where to where to source stuff but snapshots. This is the new one that's the one that's not working, and then snapshots. This is the old one, this one.
So the old snapshots repository is also working, but we no longer publish to these like we were doing this work in preparation of the end of life. Right?
So whatever that's that's a problem. It's holding stuff up.
**Cesar Munoz** 06:08 Yeah.
**Jason Plumb** 06:10 It looks like not really any new issues.
Thank you for finding this one.
I think I marked that there was one that's very similar.
**Cesar Munoz** 06:19 Yeah, yeah.
**Jason Plumb** 06:20 But whatever that's, I've looked at it a couple of times, and it's it's challenging.
There's not a good way to do it yet. We we did talk about it in the log, Sig, but it's complicated. Yeah. Help wanted on that sampling logs.
Any new prs.
No, I think they were coming back around on this one.
**Cesar Munoz** 06:53 They say, they wear, yeah.
**Jason Plumb** 06:56 Yeah, okay, they're busy. Okay, well, does anybody have any topics they wanna get to in the rest of the time we have, which is a lot.
**CleverChuk** 07:15 Yeah, about that. Compose click stuff.
**Jason Plumb** 07:17 Yeah.
**CleverChuk** 07:20 So I tried to like change the version to the latest. And then I got the the error that the basically the compile options doesn't work anymore. It doesn't suppress the error because it's accessing internal Api. It only works up to one dot.
5 dot 4, our windows 6. It doesn't work anymore. However.
if you, if we convert that to like Java.
since Antana and Kotlin is just like public in Java. Anyways.
it will still work, but as I'll have to like get a little bit more research on that.
**Jason Plumb** 08:00 Okay? That I mean, that, of course, feels hacky, but that's.
**CleverChuk** 08:04 Hang on!
**Jason Plumb** 08:04 That's what we do in instrumentation is we build hacks right? So it feels a little dirty. But if if that's if you can build like a little Java shim around the the piece you need to get access to. I think that's fine.
I didn't see the details of what the version situation was, so catch me up on that.
**CleverChuk** 08:25 No, I didn't put it there. But so basically, if you if you go from one dot 6 0, whatever version is that now is one dot 5 dot 4 that's like the Max.
This current instrumentation will support.
**Jason Plumb** 08:40 Yep.
**CleverChuk** 08:41 If you go beyond that it wouldn't compile essentially.
**Jason Plumb** 08:47 Which class has the breakage like which class is using internal.
**CleverChuk** 08:52 Pretty much all of them, except for the instrumentation stuff. Anything. There's access in the compose stuff. So I'll say, the the tab target, the compile.
**Jason Plumb** 09:06 So one of these classes, or at least one of.
**CleverChuk** 09:08 Layout. Layout note is is internal, owner is internal.
**Jason Plumb** 09:13 Okay.
**Hanson Ho** 09:15 I would just keep the the older version then, because it's just a compile time dependency, you just need to compile it as long as it runtime. Everything works. Then we're okay. There's no reason to bump it higher, because you know, none of this is is running in real time. It's good to have be as high as possible. So you know you're not working against an Api that doesn't exist. But you.
**CleverChuk** 09:41 Yeah, I mean the the one dot 5 dot 4 is fine. Is it? Just like that's like the Mexico. It will support so happy holidays this by 2.
**Hanson Ho** 09:50 I would do that. But what I would also do is write an integration test so that you could take a look so so that every new version of compose that gets released especially Major. Well, I guess minor version, not patch versions. And it works because it'll compile. Time is fine because you're obviously pinned against an older version. But if the methods you rely on don't exist at Runtime, that's when things become a bit hairy. Well, that's when things don't work so as long as things work at runtime the compile, time is fine.
so to.
**CleverChuk** 10:28 Keeping.
**Hanson Ho** 10:29 Say, compile time totally fine. Just make sure that you know 1.9 at runtime works, and it will actually remove or change the package name, or do something that will that will.
**CleverChuk** 10:39 No, it would. It wouldn't work for 1.9, because it wouldn't compile at all.
**Jason Plumb** 10:45 Right, I think, Hansen saying a runtime. So an integration test that uses the 1.9 runtime with our instrumentation compiled against 1 5 4.
**Hanson Ho** 10:57 So.
**Jason Plumb** 10:58 Yeah, that's great.
It's very similar to the the muzzle stuff that we use in the instrumentation project for Java. Where the instrumentation declares what versions it is compatible with. And then there's an integration, tests that run that verify that the instrumentation can apply cleanly on all of those other versions.
It's different, of course, because that's byte code weaving. But certainly there's a way for this to be binary and compatible with the future version.
But we can probably still get lots of mileage out of this. I mean, I think, an integration test that Hanson is describing would be very helpful. I don't think it has to be in this pull request, but we do need to make some notes. I mean, the readme does call out the versions, which is great.
and so I think that's enough for now. But someone someone will come along and go. Hey? I'm using 1, 8, or whatever the latest is here it looks like 1. 8 is the latest.
Someone's gonna come along and be like, hey? Why is my thing not supported? And then we'll have to explain to them. Well, it probably is, you have to try it. And if we have an integration test that covers those newer versions at like through a runtime dependency or a runtime check that would be awesome so that could be a follow up issue.
**Hanson Ho** 12:10 Yeah. The compile version basically just guarantees that compile time. That version contains the Apis, that it is looking for at least a compile time at Runtime it will require similar. It will require the same Apis to exist. So you can actually, you know.
introspect and do all that stuff so whether you do it manually, test it, or whether you have an integration test. Just just verify it. And to do that would be to set the comp to set the example. App. The version that it includes to be 1.8 2 and then just see if this works.
**Cesar Munoz** 12:49 Something that I'm wondering is that this, this is actually a tricky issue.
And I'm wondering people who use compose today.
It seems to me that they are willing to keep up with the latest stuff always. I that's that's my view on on people using. Compose right now.
or may maybe not right now, but at least past couple of years, because it's kind of a new thing, even though it's already stable. I think so. I'm wondering if for them it will make more sense to always support the latest version, even though that will mean breaking support for older ones.
you know. And that way. Maybe it could maybe be easier for us to maintain it, just to ensure that the latest versions are supported.
**Hanson Ho** 14:01 So this may work. This probably works. So I would just test it at one time to see if it works. It's just like. Okay. Cp, you know, you compile against a particular version. But that's a compile time dependency. You know what is running when you actually have your app is slightly different.
So you know, sometimes there's Api compatibility issues that are more explicit and apparent. But sometimes there are subtle runtime dependence. The you know, issues, or the Api is fine, but it just runs differently. So things don't work.
So it's almost like, well, your compile time is one thing, but what you actually support at Runtime is quite another. And to verify that you have integration tests. But definitely, you don't need it as part of this like merge this, and it'll work for whatever versions it works. But then we should at least manually check what versions it actually at Runtime works.
**CleverChuk** 14:55 Okay.
**Cesar Munoz** 14:56 True is this, that it kind of sounds like more for a for a I don't know already. Stable, you know, tool from our side, and and at least also.
you know, kind of long term support, commitment. Things like that.
**Hanson Ho** 15:13 The problem is.
**Cesar Munoz** 15:14 I'm not sure we've gotten there.
**Hanson Ho** 15:16 The the problem is that we're depend, we're we're looking at internals in order to actually get information about behavior. If we were depending on a public Api, you know. Then yeah will be versioned. But this is the game.
**Cesar Munoz** 15:31 Yeah.
**Hanson Ho** 15:32 Yeah, this, I'm also play.
**Cesar Munoz** 15:34 I'm also wondering if you know.
because I see, compose is something that is in wildly changing like all the time.
So what are the chances that maybe in one of these newer versions is actually easier to to do this instrumentation, and maybe they will move towards making it. You know.
**Jason Plumb** 15:55 I'm assuming clever. Chuck looked at.
**Cesar Munoz** 15:58 Got it.
**Hanson Ho** 15:59 If anything, they're gonna go the other way, which is actually, you know, from from the class used to be public. And now it's internal they want to make this as a black box as possible, and they don't. Wanna basically have you look at the internals and then determine behavior. What what we're doing is explicitly not recommended but is the only way of getting things done.
So this is this is just what we have to to. You know, there may be what at 1 point where things change so dramatically that this doesn't work. But hopefully it's we're not at that point yet, and 1.8 2 still works, and hopefully 1.9 still works.
But you know we just have to to verify that at Runtime.
**CleverChuk** 16:38 Yeah, so it looks like it runs out. It works out, run time, because the the what do you call it? The sample I've used is one dot 8 dot 2.
**Jason Plumb** 16:49 Okay.
**Hanson Ho** 16:50 Then we're good.
**Jason Plumb** 16:53 But we should still have an integration test.
**Hanson Ho** 16:55 Yeah.
**Jason Plumb** 16:56 Yeah.
**CleverChuk** 16:59 What would that look like? Just a a sample app with? Well, a test with the one dot 8 there runtime around time, dependency.
**Hanson Ho** 17:15 Yeah, so you would you? You would.
**Cesar Munoz** 17:18 Wouldn't it be similar to the existing Andre tests that we have per instrumentation.
**Jason Plumb** 17:24 Maybe, but I don't know. How do you generate that click in a in a ui widget in an integration test?
**Hanson Ho** 17:29 You. You have to fake the events. So it would either be like a Ui test, like an espresso test or or something where you just have it.
you know. Run a live app you know. You could simulate things like lifecycle things with with roboelectric and and all those things. But I don't know if you can. You could simulate the compose life cycle in a in a in a way that that that would be yeah. You'd have to do some research.
**Cesar Munoz** 18:06 There should be a way right? I know that's espresso I haven't tried it with compose, but it got this kind of you know utilities such as you, you know.
**Jason Plumb** 18:19 On!
**Cesar Munoz** 18:19 By Id, or something like that.
**Jason Plumb** 18:21 Yeah.
**Cesar Munoz** 18:21 Sorry.
**Jason Plumb** 18:22 Why does this look so jacked.
**Hanson Ho** 18:25 What the hell.
**Cesar Munoz** 18:26 Yeah.
**Jason Plumb** 18:26 I'm like, okay, start here.
**Cesar Munoz** 18:28 Refreshing.
**Jason Plumb** 18:29 Go into instrumentation, never refresh. It's already looking screwball.
And then, yeah, just it's like this top part is doubled or something.
**Hanson Ho** 18:40 So so espresso is fine. Espressos runs a real app on an emulator. So if you have an espresso test, we have a special test. Here, then espresso totally works.
**CleverChuk** 18:50 So.
**Hanson Ho** 18:50 That is.
**CleverChuk** 18:51 The the question is, does that does that run in the Ci? Can it run in the Ci.
**Hanson Ho** 18:56 Yes.
**Cesar Munoz** 18:57 I think we haven't tried it, but it should.
**Hanson Ho** 19:00 But it's slow.
**Jason Plumb** 19:03 Yeah, we don't have any of that yet.
**Hanson Ho** 19:05 I I would I would manually test it, say it works, and then and then investigate how you would do that.
**CleverChuk** 19:14 I mean, it works.
**Hanson Ho** 19:16 There you go!
**CleverChuk** 19:17 Verified.
**Jason Plumb** 19:20 Can anyone? Would it? Would anyone be willing to open an issue to investigate this further, as far as how we can write an integration test to verify this.
**Hanson Ho** 19:31 Yeah. Go ahead. Oh, great, awesome.
**Jason Plumb** 19:34 Was that clever chuck.
**CleverChuk** 19:36 Yeah.
**Jason Plumb** 19:37 Thank you.
**Cesar Munoz** 19:46 Also cover shock. Thanks for taking on this.
**Jason Plumb** 19:50 Yeah. No kidding.
**Cesar Munoz** 19:50 Seems like a what are you waiting for?
Painful thing to deal with? Composing, you know. Instrumenting. Compose.
You're welcome, sounds good like.
**Jason Plumb** 20:02 Yeah, for sure.
I think I made that comment, too. I was like, I cannot believe how much work was involved. But it's great.
Yeah, cool.
So I think we're good to merge this. Then, right, does anybody have anything else? They wanna I think we've got the approvals on it. We should go ahead and merge it then, since this was this question was answered, I think I would. I would just make sure that.
**Cesar Munoz** 20:34 Good.
**Jason Plumb** 20:35 This after the approval. So there's a setting on Github Repos, where you can invalidate prior approvals. When commits are made, and we don't generally use that in the open telemetry project. So I like to go back and verify, you know, changes when they happen like, yeah.
**CleverChuk** 20:59 Yeah, this is mainly the version and then moving the package to click, because.
**Jason Plumb** 21:04 Right.
Yep.
**CleverChuk** 21:09 So no, not much could change like.
**Jason Plumb** 21:12 Click. Oh, yeah, yeah, that was, I think, I, yeah, okay, that's cool.
It's all just moves alright, going once, going twice.
**Hanson Ho** 21:31 We can always.
**Jason Plumb** 21:33 There was a discussion on the Java Channel in Cncf slack about Contrib, and the fact that we haven't had a release in a couple of months, and we're behind. Contrib is also. It contains the fix to disk buffering that we could could use.
Of course, sonotype is shitting the bed right now. But when that's resolved hopefully, we can get a release of contrib this week, and then we can look at releasing, because we are also 2 months behind.
**Cesar Munoz** 22:10 Now to be fair Jack merged a fix in core for that. This buffering issue? I think so. Maybe we don't need to wait for country. Probably I need to undo my country, changes.
**Jason Plumb** 22:27 You think, undo them.
**Cesar Munoz** 22:30 Yeah, because if they're no longer native, yeah.
**Jason Plumb** 22:34 It wasn't anything harmful, though it was just defensive, right.
**Cesar Munoz** 22:38 Yeah, I'll be. I can leave them there. But you know.
**Hanson Ho** 22:43 Just implementing the extended.
**Cesar Munoz** 22:46 Oh, yeah.
**Jason Plumb** 22:58 Oh, congrats on that one, too! By the way.
**Cesar Munoz** 23:01 Oh! Cheers!
**Jason Plumb** 23:06 Yeah, this one, right?
**Cesar Munoz** 23:10 Or whatever we don't.
**Jason Plumb** 23:11 We don't have to do.
**Cesar Munoz** 23:12 Oh!
**Jason Plumb** 23:13 I mean, is not this one.
**Cesar Munoz** 23:15 No, it's a it's a very much smaller one. Let me see if I can find.
**Jason Plumb** 23:22 This one.
**Cesar Munoz** 23:24 Yeah, that one.
**Jason Plumb** 23:33 Yes, this. Yep.
I mean this will. This will need to be refactored when this goes stable, anyway, right when extended log record data no longer exists when it's out of incubating.
**Cesar Munoz** 23:51 True.
**Jason Plumb** 23:52 That'll need that'll so this will just fall out. I wouldn't. I wouldn't revert this, I'd say. Just leave it, for now and then it'll fall.
**Cesar Munoz** 23:57 Let's leave it.
**Jason Plumb** 23:58 Happens.
**Cesar Munoz** 23:59 Out of curiosity. Have you heard anything in the Java sec about? When will that happen, or is it? It's unclear.
**Jason Plumb** 24:09 The contrib release.
**Cesar Munoz** 24:11 The no, I mean the
**Jason Plumb** 24:13 Stabilization.
**Cesar Munoz** 24:15 The stabilization. Yeah, of those extended attributes.
**Jason Plumb** 24:18 I haven't. Are you looking for it? To go stable.
**Cesar Munoz** 24:24 I guess if if in, if it's soon, then probably we can wait for for it to for them, for us to add proper support for that in in contribut.
Otherwise, then probably we can leave. You know it as is right now and then add proper support while still in incubating status, you know, because at the end of the day what I'm what I'm doing here is just returning the regular attributes.
So if there were some extended ones. Those are discarded.
**Jason Plumb** 24:55 Yeah.
yeah, I mean long term. We're gonna have to figure that out. We don't have any events yet that use extended attributes. But I think it'll happen.
**Cesar Munoz** 25:10 So probably it's it's worth adding support, anyway, while in incubating mode. Yeah.
**Hanson Ho** 25:19 Doesn't. Doesn't old Http. Implementation or instrumentation use? Use this.
**Jason Plumb** 25:27 The extended log record.
**Hanson Ho** 25:29 Yeah.
**Jason Plumb** 25:31 I don't think so.
**Cesar Munoz** 25:32 Now.
**Hanson Ho** 25:33 No. Okay. All right.
Okay.
**Jason Plumb** 25:37 No, and the the extended log record data exists purely to expose the set attributes right with the complex types.
**Hanson Ho** 25:45 Hmm.
**Jason Plumb** 25:46 I think that's the main or maybe event name is also still on there.
**Hanson Ho** 25:50 I think a vet name. I think.
**Cesar Munoz** 25:51 Evan.
**Hanson Ho** 25:52 Yeah, I think.
**Cesar Munoz** 25:53 That's right.
**Hanson Ho** 25:54 I remember something being pulled in that that including Okhtp people there were, you know, warnings of that being pulled in But.
**Cesar Munoz** 26:05 Event name. I think it was added actually recently by someone else into contract. So we should definitely wait for the next release.
**Jason Plumb** 26:22 Yeah.
and this thing. Okay.
**Hanson Ho** 26:30 Why is that still there.
**Cesar Munoz** 26:35 Well, if you have to. It's part of the it's part of the
**Jason Plumb** 26:39 Yeah, the log body. It's not the event body. It's a log body. Okay, that's why it's like.
**Hanson Ho** 26:45 Right.
**Jason Plumb** 26:45 Fluffy.
alright. Anything else that we wanna sneak into the agenda for today?
**Hanson Ho** 26:55 Well, I gotta take off, anyway. So perfect time.
**Jason Plumb** 27:00 Alright, we can end it here. Thanks again for your contributions. Appreciate everyone.
No.
**Cesar Munoz** 27:07 Thank you.
**Jason Plumb** 27:08 Sure see you later. Bye.
**CleverChuk** 27:10 Yeah.
