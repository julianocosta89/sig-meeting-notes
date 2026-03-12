SIG: Swift SIG
Date: 2026-02-05
Duration: 35 minutes
============================================================

## Zoom Recording Transcript

**Bryce Buchanan** 00:10 Hey, Billy.
**Billy Zhou** 00:13 Hey, Bryce.
Very done.
**Bryce Buchanan** 00:17 Not bad.
How about yourself?
**Billy Zhou** 00:23 It's, been a little crazy over here, but, yeah, it's good to… It's always good to be a part of this meeting.
**Bryce Buchanan** 00:30 That's good.
- Wow, where is everybody today?
Oh, Ari's not gonna be here.
**Billy Zhou** 02:01 So, I was… I've always been kind of curious, like, what do you work on in your day-to-day, over at, like, New Relic? .
**Bryce Buchanan** 02:09 I'm at Elastic.
**Billy Zhou** 02:10 Like, yeah.
**Bryce Buchanan** 02:11 I… these days, I've been working in Kibana, the… the.
**Billy Zhou** 02:17 Yeah.
**Bryce Buchanan** 02:18 web tool, yeah. So, I spend about, like.
maybe a day a week on hotel stuff, so yeah, it's pretty limited for me as well. It sounds like you're trying to balance other, other, projects and hotel?
**Billy Zhou** 02:36 Yeah, but it's settling now, it's just… honestly, the big thing is I've been dealing with, like, a medical issue, but…
**Bryce Buchanan** 02:42 Oh, I'm sorry, that sucks.
**Billy Zhou** 02:44 That's okay. Yeah, I might have to get surgery for something, and it's been a little stressful for that, and then…
**Bryce Buchanan** 02:49 That's so fun.
**Billy Zhou** 02:51 There's been some… Like, reorging going on, yeah.
**Bryce Buchanan** 02:56 well, hopefully it all turns out well.
**Billy Zhou** 03:00 Oops.
Let's say you mainly work on, the Kibana dashboard for Elasticsearch?
**Bryce Buchanan** 03:07 Yeah. Yup.
**Billy Zhou** 03:09 Okay, cool.
**Bryce Buchanan** 03:12 I'm still responsible for, like, the Elastic iOS agent, but I kind of spend about, like, 20% of my time on that stuff and OTEL.
**Billy Zhou** 03:24 Alright, very cool.
**Bryce Buchanan** 03:25 Yeah, and you know, like, when bigger projects come along, you know, I'll spend more time on it, but generally just kind of maintaining stuff.
Yep.
Alright, well… Hey, Vinat, I don't know if Nacho's gonna be here. Ari said that he's not gonna make it.
**Vinod Vydier** 03:42 Yeah.
**Bryce Buchanan** 03:45 But, oh, there's Nacho, cool.
Groovy.
Well then, let us… Get started. How you doing, Acho?
**nacho** 03:59 Sorry for being a bit late.
Meeting.
**Bryce Buchanan** 04:04 No problem.
**Vinod Vydier** 04:07 Alright.
**Bryce Buchanan** 04:08 Take a look, topics from previous weeks.
Crash reporter feedback… I think there, yeah, there are quite a few good notes on here.
I, added my feedback onto some of those as well, It sounds like, Billy, you haven't had a chance to really review this stuff yet, and…
**Billy Zhou** 04:31 Yeah, I finally got to it today. Sorry for the delay, guys. I have the changes staged, and I need to test it on a physical device, before, submitting it, so… Yeah, I'll ping you, today on it.
And then… Yeah, so that's it for the IKS Crash Fund.
I'll add a README and then address, the feedback.
**Bryce Buchanan** 04:55 Yep.
Yeah, I think, yeah, I think that, there's also, like, some potential additional configuration that we might want to provide.
**Billy Zhou** 05:05 Yeah, I was going to expose the KS Trash, configuration, I think, like… There is not a defined struct for it, so, maybe I'll have to just add our own.
yeah, exactly.
**Bryce Buchanan** 05:22 Yeah.
**Billy Zhou** 05:23 Yeah, it's kind of exposed that, that.
**Bryce Buchanan** 05:26 As an optional parameter, yeah.
**Billy Zhou** 05:28 Yeah, And then, yeah, there is, like, some ideas about, like, what to do about the exception message, Like, AWS, when I did this, I had to make the crash message, like, the unique identifier that, like, that's, like, groupable, as well as, like.
Coming up with, like, a decent, like, human-readable crash message, I think Alex was more of the opinion of, like, splitting them up, into, like, a hash and, like, a detailed message. I think for now.
just keep the message as is, and try to… if there's any weird performance issue, I can address that.
**Bryce Buchanan** 06:10 Yeah, I think, the ideal way to do it is… I think he mentions it somewhere in here, but… Figuring out the first, the first frame of the… app image in the crash stack, because generally, this is gonna be, like, in some system library, so you're gonna have, like, if you just take, like, the message or the top of the… top of the stack, it's just gonna, like, you know, over… Aggregate crashes together, and so you'll never really see, like, what's actually crashing from, like, a high-level view.
**Billy Zhou** 06:49 That's a good point, yeah. Yeah, so, like, par… so parsing…
**Bryce Buchanan** 06:52 down to, like, the crashing frame of the app itself. Like, just looking for the image of the app.
Whatever the first thing in there is, and then using that. That's usually a pretty good way to… to limit the over-aggregation of… of the crash, types.
And I think… I think he mentions that, but, like, yeah, first iteration, it's probably okay to just go… go with the solution you have.
Is there actually, like, a group… a grouping parameter that's defined in the semantic convention?
I don't… I haven't really looked at that.
It feels like something that is missing, though.
**Billy Zhou** 07:40 I don't think so, what do you guys typically call that field?
**Bryce Buchanan** 07:46 Oh… I think at Elastic, we, like, we call it a grouping key, which is, like, just a hash value of, like, various things, So, like, in some… like, for some platforms, it might be, like, a hash of the entire stack trace itself.
And in other ones, like iOS, it'll be, like, the… just the crashing line in the, application image.
The crashing frame.
**Billy Zhou** 08:22 Okay, I wrote out this, Stan, okay, I'll… Add those things to the backlog.
**Bryce Buchanan** 08:29 Cool, right on.
**Vinod Vydier** 08:30 So the crash file, with the… the DSIM file, you can actually go to the… From this, you can go to the exception, you can go to the line, right?
It is so…
**Bryce Buchanan** 08:41 Well, I mean, without the DSIM, you know, you just have the memory address, but that still works pretty well. The only issue is… I don't know, does Apple actually have any devices with, with different architectures anymore, because I remember back in the day, like, if you had a crash in an app, and you were only looking at the memory addresses, the, they would all be the same on the, on the same architecture, but if it was built for different architectures, then that, that, that, You know, normalized address would be different.
**nacho** 09:21 Yeah, basically, the address is also randomized for every execution, so you really have to… I mean, the address that it provides the crash is not… The real address in the binary.
So you really have to take to the binary, it… at the end of the Apple class, you have to… Different libraries and what addresses they take, so you have to really, get the… The address related to the address of your library.
**Bryce Buchanan** 09:53 Yep.
**nacho** 09:54 to get the real memory in the app. So, yeah.
So, this is something that, yeah, different companies handle differently. It's… it's… It will be great to have a default, usable thing for I would say small, companies, or small developers, or a small And allow many configuration, ways for more complex situations, I would say.
Let's… Try to help.
the, the, the simple, at least in my opinion. Let's try to help the simple solution for the… For those, you know, people that doesn't have such a lot of, you know, resources, to try to… Interesting.
**Vinod Vydier** 10:47 Provide some…
**nacho** 10:48 Anything useful for them?
Yeah, you need to map…
**Vinod Vydier** 10:51 You need to map the exact DSIM, right, to the version that the app has crashed.
So you gotta…
**nacho** 10:58 Yeah, you need… when you really want to simulate it, you need the, DSIM, files.
**Vinod Vydier** 11:04 Yeah. Which… Yeah, from the internet that is crashed, yeah.
**nacho** 11:08 Yeah, you need exactly the same.
the same file for the binary that was built, because everything is just, randomly… Stored. So, yeah, you can… there is… you can also, for… that's just for symbolication. You can do some symbolication, With Swiftish, I mean, difficult, because it's, not… I mean, it was not easy until last version of the compiler, which is exposing, At least the name of the function failing, but… Yeah, if you really want to symbolicate your crash, you need the DSIM files, and you need the address, and you need a lot of information around images and their addresses in memory when the crash happens, yeah.
**Billy Zhou** 11:59 Hello?
I just had a quick question, like, to get the application name, is… Do we need to put that into top-level configuration, or, is it… Auto… is it discoverable without…
**Bryce Buchanan** 12:12 I… I think it's discoverable via the application plist?
**Billy Zhou** 12:20 info.pa.
**Bryce Buchanan** 12:22 Yeah, the info, info.plist, yeah, I think… I think one of the values in there represents what's gonna show, like, the .app So you should be able to search for that in the list of images, and then get the address range from there.
Okay.
**nacho** 12:38 Sorry, I didn't get that question. Sorry, Billy.
**Billy Zhou** 12:42 I was referring to the, Yeah, I'll accept the feedback that, the exception message as is, is looking at the top of the stack trace, but, like, usually that's, like, a native module, so Bryce was suggesting, like, a skip past that and find the first line that matches, like, the application name to get, like.
The actual application line that… threw this… through the…
**nacho** 13:05 Yep.
**Billy Zhou** 13:06 We're the exception, and I was wondering how to get that application name, like, whether it needs to be in top-level configuration, or if you can just discover it, and he was saying you can get it from info.plist.
**nacho** 13:19 I think that this… all… also, passed by KS, KS crash. I mean, yeah.
**Bryce Buchanan** 13:26 Yeah, if you pull it out of the path…
**nacho** 13:29 Yep.
**Bryce Buchanan** 13:31 Because then down in the… if I can find it down here… oh.
**nacho** 13:35 In the case crass… structure, it has all those fields, like the apple, because you can create Apple-like
**Billy Zhou** 13:44 Oh, okay.
**nacho** 13:45 logs, you can say KSCrass, export this Apple-like log, and it will export that, with a very similar structure to this.
So Edith has… You… there is an instructor that you can, find what… all those, all those, all those things.
which is the name of the app, where is the app, address memory, because it also keeps the binaries. You can really get everything, from KSPress, because it parses everything.
**Billy Zhou** 14:21 Okay, yeah, I'll take… I'll double-check what Chaoscrash is doing and, add it to the, okay, yeah.
Yeah. Thank you. That's really useful.
**Bryce Buchanan** 14:29 Yeah, so, like, yeah, for a visual example, so, like… here is… you could… you could look… I think, yeah, you could look at the touch canvas, the process name, or the path here, because this you can look direct… you can map that directly to the image list, the binary image list, so that matches this touch canvas, and it gives you the… the address range.
**Billy Zhou** 14:53 Okay.
**Bryce Buchanan** 14:53 And then you can… then you can look at the crashing stack, and it's like, okay, so here's the first… touch canvas frame of the crash, and so you can grab that address, or if there's an actual, symbol. You can grab that symbol and then hash that, and that'll be a good way to identify a unique crash.
**nacho** 15:15 The thing is that… Here, you probably won't get.
**Bryce Buchanan** 15:20 Yeah, you won't get a frame, so you'll have to use…
**nacho** 15:21 You will probably just get an address.
**Bryce Buchanan** 15:26 This is the… Go ahead.
**nacho** 15:30 Yeah, I mean, yeah, that document explains it very well, but usually when you are in release mode, you are not getting any of your… if it's a Swift application, you don't get any of your class's name or methods. Yeah.
**Bryce Buchanan** 15:44 Yeah.
**nacho** 15:45 And there is… with newest Swift, there is a version, there is a… The mangler for the name of the method.
For older versions, you have to expose that. You can expose the name, because it's there in the runtime.
I can… I can link… Great.
**Billy Zhou** 16:07 In which runtime? To the Swift runtime, or.
**nacho** 16:09 Yeah, in short runtime, there is, yeah, I did that in the past, like, yeah, creating, You can even… even then, in a released version, you can demangle the name. It's a… Swift name that sometimes is a bit complex, especially with generics and things like that. It's not extremely demangled, but if you want to show that to the user, it can be useful.
**Billy Zhou** 16:34 Oh, for, oh, okay, yeah, yeah, it's… this is separate from, symbolication, right? It's the Swift, Swift main… okay, yeah, does KS Crash do that as well, or,
**nacho** 16:49 Yeah, KKS will give you all that information in lines.
**Billy Zhou** 16:52 does both.
**nacho** 16:52 It will not support, it will not give you the Mangle names per Swift, but yeah, the address will be there.
**Billy Zhou** 16:59 Okay, so only there's symbolication, okay.
**nacho** 17:02 Yeah, and usually the symbolication is done later, right? You get your crosses in your, in your backend, and you just go there with the addresses, and you can recreate the the stack with your DSIM files, because obviously you are not sharing your DSIM files.
**Billy Zhou** 17:22 Oh, that's okay.
**nacho** 17:22 code, yeah.
**Bryce Buchanan** 17:26 Yeah, so without the DSIM, this will be a memory address and offset value to the root address for the library, which is this one here.
But anyway…
**Vinod Vydier** 17:40 Yo.
**Bryce Buchanan** 17:43 Okay.
**Billy Zhou** 17:47 Yeah.
**Bryce Buchanan** 17:47 offered.
**Billy Zhou** 17:48 Yeah, for the next one, I was wondering, when we're doing, the Swift 6 release for main, Yeah, the engine staged, for this, but it needs a release.
**Bryce Buchanan** 18:05 Okay, I hear this one.
**Billy Zhou** 18:06 Yeah.
**Bryce Buchanan** 18:07 Oh yeah, and that's merged, so we can, Yeah, we should do a release then.
Cool. Do you think that this… is this gonna need a, A major version bump.
if this is not compatible with older versions, or, like, is this gonna be compatible with older versions of Swift Main?
**Billy Zhou** 18:34 How older?
**Bryce Buchanan** 18:38 Well, like, like, let's say we're… we try to use this one.
with the, existing Swift main release.
**Billy Zhou** 18:48 Yeah, I tested it, and it seemed okay. I can do it again as well, because it's been a couple weeks since I tested it.
**Bryce Buchanan** 18:54 Okay.
**Billy Zhou** 18:55 Thanks. Sorry, not for me to interrupt you.
**nacho** 18:58 Yeah, but basically to know if it's source code compatible or not. I expect it will.
Right, it should, but yeah.
**Bryce Buchanan** 19:06 Cool. Okay. Yeah, then we can just… we'll do a 2.4 for this.
Let's look at the pull request really quick.
Make these sendable… So we might… mmm…
**Billy Zhou** 19:25 Oh, that should be resolved by…
**Bryce Buchanan** 19:27 That looks like…
**nacho** 19:30 Yep.
I have reviewed that, It wanted to have, make… making those objects endable, probably because, if you, If you set your compiler to check concurrency, it will say that you cannot do some things with that.
**Bryce Buchanan** 19:51 Right.
**nacho** 19:52 Yeah, but I commented that, he wanted to make unsectionable one of the… one of the structs.
But the problem is that he's not… I mean, he's not really ascendable.
**Bryce Buchanan** 20:05 Right, yeah.
**nacho** 20:06 Truly.
**Bryce Buchanan** 20:06 Is overriding the warning.
**nacho** 20:08 Yeah, I mean, it's like, yeah, don't show the warning, but I don't think that's the… what we should do. I mean, if… so yeah, I asked for a different, Version. Yeah, but we don't need to be concurrency.
I mean, strict right now. We can go with 5-6, and that… that… that… that PR is not limiting our… possibility to release 56 now.
**Bryce Buchanan** 20:37 Alright, well, we've got a release PR up now, so we'll let that run, and then once that is looking good, we can merge that and get a release out for core.
**Billy Zhou** 20:52 Yeah, I'll, I'll also do a final check and, ping you and, I have, like, the screenshots and logs and everything.
**Bryce Buchanan** 20:59 Cool. Thank you.
Ari's not here for that update.
Let's see… was there… No.
Was there a PR?
Doesn't look like there's any PRs for that.
Alright, cool.
Alright.
So… So I have a topic, which is just a notification that I'm gonna be going on leave.
at the end of the month, for about a month, and then I'll be, be back after that, but, I've got a new baby on the way. It's coming on the 23rd, so…
**Vinod Vydier** 22:00 Congratulations.
**nacho** 22:01 Nice.
Congrats.
**Billy Zhou** 22:03 Congratulations, Braz.
**Bryce Buchanan** 22:04 Yeah, thank you.
**nacho** 22:06 That's the best reason, probably.
Cool.
**Bryce Buchanan** 22:09 What's that?
**nacho** 22:10 That's the best reason for taking a lease.
**Vinod Vydier** 22:13 Yeah.
**nacho** 22:14 Having a new baby. It's weird.
**Bryce Buchanan** 22:16 That's true, yeah.
**Vinod Vydier** 22:18 We can have a new release after you come back.
**Bryce Buchanan** 22:21 Sounds good.
So, I'll leave it… I'll leave it to, Nacho and Ari to run the meetings while I'm gone.
And Venoden.
**Vinod Vydier** 22:32 Yes.
Sounds good.
**Bryce Buchanan** 22:44 I can't type.
Cool. Are there any other topics that we'd like to discuss?
Nope. Nope? Okay. Well, let's take a quick look at our issues that we have open, if we got any new ones.
Feature request ensures the swift implementation of environment context propagation matches the specification. Okay, so this is just something that we need to do. It's a feature request and enhancement, the spec has changed.
And we need to follow that.
Ari's been working on this, but no updates so far.
Okay, so no real new issues here.
Collector, not a big deal, we can just merge this one.
Let me do that really quick.
Alright, there we go.
Synchronous processing… Has this been… We're just waiting for these conflicts to be resolved, maybe?
Maybe somebody else should review them.
Interesting.
**nacho** 24:26 Yeah, basically, it needs to… Just needs to… Special value as part… after the… yeah, that was the…
**Bryce Buchanan** 24:37 So I should just… do you think I should just remove these ones? Oops.
**nacho** 24:40 No, no, I think… I think you need to add the result value Equals .failer after the feedback handler.
**Bryce Buchanan** 24:49 Oh, I see, I see.
**nacho** 24:51 Yeah, I think that was added just in the other branch.
That will be the only…
**Bryce Buchanan** 25:06 Oh, that's interesting. Is that not used anywhere else? Is it…
**nacho** 25:11 No one is returning it.
No, yeah, it's being written on the end.
**Bryce Buchanan** 25:17 Why is that not showing up? That's bizarre.
Mmm, crookie?
**nacho** 25:35 Yeah, it looks good, yeah. It was a very simple one.
**Bryce Buchanan** 25:40 I just wanna double-check that.
In the actual change.
Okay… So that was added.
**nacho** 25:58 Yeah. Interchange…
**Bryce Buchanan** 25:59 I see, okay, alright.
**nacho** 26:01 Avoid the printing, yeah.
**Bryce Buchanan** 26:03 Okay.
Marked as resolved… Boom.
**Vinod Vydier** 26:12 Excuse me.
**Bryce Buchanan** 26:19 Will it work?
I might not be able to mute it. It didn't.
Nice.
**nacho** 26:25 Yeah, he didn't…
**Bryce Buchanan** 26:27 our repo, I can… I can update it if I want.
**nacho** 26:32 I didn't know we could…
**Bryce Buchanan** 26:34 That's funny.
**nacho** 26:37 That's cool.
**Bryce Buchanan** 26:41 I guess it depends on what permissions you.
**Vinod Vydier** 26:45 Yeah.
**Bryce Buchanan** 26:46 Here, I'll enable auto-merge there, because I think that we've got… yeah, Ari's approved it.
Okie dokie.
Pretty good.
And then we got the KS Crash… That's working, we got… this needs to get updated, and Will's gonna work on that, and… were you able to get this fixed, Fanad?
**Vinod Vydier** 27:07 I… so what do I need to do? Do I need to, you know.
**Bryce Buchanan** 27:10 I need to, need to… I think there's just some changes, some conflicts here. Docker Compose… Oh, it's just, like, an update version, it looks like.
But why is that removed? Should that be removed?
Mmm…
**nacho** 27:27 Probably it was updated to the university, and it's below, right?
**Vinod Vydier** 27:32 Yeah, right now it's at 143 or something is the latest version. But, you know, when I did it, it was 137 was the latest.
So, I don't know, what does this…
**nacho** 27:42 Yeah, I think the line down is the good one, because it's the newest version.
**Bryce Buchanan** 27:49 Yeah, but I'm just confused, like, do we need… does this platform be…
**nacho** 27:52 the platform thing.
**Vinod Vydier** 27:54 Platform thing is, I think, needed, because otherwise, It will not get the right… It won't get the right… Collector version.
**Bryce Buchanan** 28:06 Okay.
**Vinod Vydier** 28:07 Yeah. So, so that is actually…
**Bryce Buchanan** 28:09 You're adding… you are adding platform.
**Vinod Vydier** 28:11 Yeah, yeah, yeah, yeah, yeah.
**Bryce Buchanan** 28:13 And so that's why it's not showing up. So what we'll do is we'll remove that one, remove that one, remove that one, remove that one.
And… then we'll do that.
**Vinod Vydier** 28:25 Yeah, and I don't know if you need, you know, I think, latest should be… do we need that, SHA?
**Bryce Buchanan** 28:32 I think that the Dependabot adds that in there.
**Vinod Vydier** 28:35 Okay, okay, alright, okay.
**nacho** 28:38 Yeah, that… those are all the PRs, I'll just change that stuff.
**Bryce Buchanan** 28:44 So it automatically adds, okay, it automatically adds that, okay.
**Vinod Vydier** 28:48 This is.
**Bryce Buchanan** 28:51 Alright.
**Vinod Vydier** 28:52 Okay.
This is what we needed to do.
**Bryce Buchanan** 28:56 Okay.
And let's go and take a look at Swift Core, even though we just did that.
Alright, issues… async, await for APIs, yep, yep, yep. It's just an open issue, and we gotta release 4.
So, once that's merged, then we can update the, main branch, or the main repo, and… Yeah, that'll be good. Cool.
**nacho** 29:29 Billy, you are validating it.
bills, right? With the… with that version in the… In the non-core.
**Billy Zhou** 29:39 Yeah, so originally I did, test, main V5 against, core V6, and then I think after all the changes, I'll do another, I'll do another validation today, yeah.
**nacho** 29:53 Yeah, sure. In case something changed.
Maybe, yeah, maybe you can do that validation and approve, the… Because you need an approval, right, Bryce, for your release?
**Billy Zhou** 30:06 Well, I don't have right permission, but yeah, I'll bring it, yeah.
**nacho** 30:09 You don't… okay.
**Bryce Buchanan** 30:12 Yeah, I think that this just needs to get… yeah, this needs to get approved. Okay. Once it's…
**nacho** 30:18 And can you approve, Billy? You can, right?
**Billy Zhou** 30:21 I can still leave my review, yeah, but it won't, help him.
**nacho** 30:25 Your review one… is not valid.
**Billy Zhou** 30:29 Yeah.
**Bryce Buchanan** 30:29 Aren't you an approver? I thought you were.
**Billy Zhou** 30:32 Hi, Am I.
**nacho** 30:36 I didn't join the upperware, at least. I thought so. Yeah.
**Bryce Buchanan** 30:40 I don't even know.
**Vinod Vydier** 30:41 Yeah, maybe not, I think, you know. There is, one person that I think we can remove, because he's not joining.
**nacho** 30:48 Oh yeah, that's true.
**Vinod Vydier** 30:50 We can make, austin. Austin has not been here, right? So we can…
**nacho** 30:56 Yeah.
**Vinod Vydier** 30:56 Remove that and add Billy.
**Bryce Buchanan** 30:59 Yeah, sounds good.
**Vinod Vydier** 31:00 Yep.
One for one replacement.
**Billy Zhou** 31:03 Okay.
**Bryce Buchanan** 31:09 Yeah, I don't know how to check.
**nacho** 31:11 Yeah, okay, yeah.
**Bryce Buchanan** 31:12 I have to learn how to do it again, I don't remember.
**nacho** 31:14 Yeah, exactly.
**Bryce Buchanan** 31:15 Do you want me to?
**nacho** 31:15 Total rabbit hole.
**Bryce Buchanan** 31:16 Here we go.
**nacho** 31:17 Yeah, okay.
**Bryce Buchanan** 31:18 So maybe… Swift.
**nacho** 31:22 Swift, Swift… oh, there are two different approvers, but Swift approvers?
Shift approvers? Yeah, we can remove Austin.
Okay?
Oh, and you… oh, Billy, I thought you were in the approvals also, yeah.
**Bryce Buchanan** 31:47 Yeah, that's so true.
**nacho** 31:48 Yeah, great.
**Bryce Buchanan** 31:49 Link Billy and approver now.
**nacho** 31:51 Because you were a… you… You were an approver, at least on the, on the… On the papers, right?
Good.
**Bryce Buchanan** 31:59 Not so. Maybe we just forgot.
**nacho** 32:01 With core approvers, that also has a different approver team.
**Bryce Buchanan** 32:05 Yeah, we'll have to… yep, yeah, it does.
**nacho** 32:07 Apple.
**Billy Zhou** 32:08 I think you were missing from there as well, Nacho.
**nacho** 32:10 Yeah, I'm missing there, okay. Yeah, I think…
**Bryce Buchanan** 32:14 I think that you're a… you're a maintainer, so I think… I don't know…
**nacho** 32:17 Oh, good, good one. I don't know. No, you're on LinkedIn.
I don't know.
**Vinod Vydier** 32:23 Yeah, here also, I think you can do the same thing. Austin, out, and Billy in.
**Bryce Buchanan** 32:33 Are you kidding me?
**nacho** 32:35 Okay.
So maybe, maybe I cannot approve in Shift Core, I don't know.
**Bryce Buchanan** 32:44 There we go.
Billy has been added there… We'll add Billy over here, too.
Oh, it's… that's right, Will.
**nacho** 33:11 So it has a different group for its people.
I don't know.
**Bryce Buchanan** 33:21 Cool.
Yeah, hold on, yeah, hold on, let's look at this. So, 4 maintainers.
**Vinod Vydier** 33:28 While you're at it, you can also remove Austin, because he's not been…
**Bryce Buchanan** 33:34 I think he got…
**Vinod Vydier** 33:35 He's replaced by, ari.
**nacho** 33:41 In Embrace. I think he doesn't work for Embrace anymore.
**Bryce Buchanan** 33:44 Right, that's true.
**Vinod Vydier** 33:46 Yup.
**nacho** 33:48 Members with co-approvers.
**Bryce Buchanan** 33:50 Yeah, I think that I'm just on here because I set this all up, but you're in the, in the core maintainers.
**nacho** 33:58 Okay.
**Bryce Buchanan** 33:59 I don't know… yeah, I think, like, this is, like, an old… like a, like a, like the GitHub maintainer idea? Or is this as, like, the… yeah, I don't… I don't know. I don't know what…
**nacho** 34:12 Okay, yeah, no worries.
**Bryce Buchanan** 34:13 I don't know.
**nacho** 34:15 You, you, yeah, yeah, I can.
So you have a pull request here.
Let's see if I can… I'm… at least I am as… I appear there as a reviewer.
So, probably… And I think I have approved that in the past. I can submit a review, it says.
**Bryce Buchanan** 34:55 Interesting.
Okay.
**nacho** 35:00 I can approve it, and if Billy… Yeah, I have been able to approve it.
So if Billy validates it, we, we can, we can merge.
**Bryce Buchanan** 35:14 Cool. Sounds good.
Alrighty, well, I think, that covers just about everything. One last chance, any other topics we want to discuss?
**Vinod Vydier** 35:29 Nope.
**Bryce Buchanan** 35:30 Nope. Cool.
Okay. Well, let's call it a day, then.
Yep, see you all next week.
**Billy Zhou** 35:36 Bye-bye.
Right.
