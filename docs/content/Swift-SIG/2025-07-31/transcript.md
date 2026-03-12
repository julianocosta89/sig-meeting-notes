SIG: Swift SIG
Date: 2025-07-31
Duration: 51 minutes
============================================================

## Zoom Recording Transcript

**Ariel Demarco** 00:39 Hey, Bryce.
**Bryce Buchanan** 00:42 Hey, Ari! How are you doing.
**Ariel Demarco** 00:44 Not too bad.
How about you?
How's work?
**Bryce Buchanan** 00:49 Doing good. It's not bad.
I'm I'm messing around with opamp and It's a very complicated.
It's a very complicated spec. I was like I was like, this is, gonna be easy. I just need to go and check and get some like updates for some config. Oh, God, what.
**Ariel Demarco** 01:11 But why? You're using open.
**Bryce Buchanan** 01:13 Oh, it's just we. We need to support it.
Oh, I see.
**Ariel Demarco** 01:19 Hey! Harry!
**Arri Blais** 01:20 Hello!
**Bryce Buchanan** 01:32 Don't you start.
Interesting.
You know I'm Okie Dokie Okey Dokey, why don't we go ahead and get started? So topics from last week? There's just the release. 2 point. Oh.
If I can spell things, but it's in pre-release.
I don't know if anybody's tried importing that at all, or used it a little bit.
Any any updates, any anybody test it out.
**Alex Cohen** 05:13 Yeah. Embrace has. Seems to be working perfectly fine as expected. Expect, except for that little issue that that, we reported.
**Bryce Buchanan** 05:23 Hmm, okay, very good.
Okay. Alright. Let's move on to a new topic. Sorry you've got a couple of them.
**Ariel Demarco** 05:31 Yeah. I'll start, I think, with the the simplest one is the data compression.
you mentioned that there was an issue on cocoa pots. Because of that library not supporting vision. OS, that is something we support.
I reached a Pr on their repository, but seems there's no kind of a lot of activity in that report. So it's it's mostly to see what what we should do.
that's basically because it it won't compile for cocoabots. I know why it's working fine with Sbm. To be honest, because it should break, because it has no support for region OS on on the data compression repository. But probably it's like it's it's trying to do an optimistic approach, xcode and try to build. And if it won't build because of, I don't know some specific Api not existing in vision. OS, it will fail, but if it works fine, it does.
But for some reason, in cocoa bots, you kind of need to to have it an explicit.
Yeah, explicitly. Say, you, you support that.
Yeah, that target. Finally, I think.
**Bryce Buchanan** 06:48 Okay, interesting hold on one second.
**Ariel Demarco** 06:51 Yeah, sure.
So for the for the rest of people.
We've been talking about this in the hotel. Swift, channel. I'll link you guys in the chat of this meeting the conversation. I'll also.
**Bryce Buchanan** 07:09 I mean.
**Ariel Demarco** 07:10 To the agenda.
**Bryce Buchanan** 07:11 This is exactly what I didn't want to happen with cocoa pods.
**Ariel Demarco** 07:15 Yeah.
**Bryce Buchanan** 07:18 So that was a good experiment. Time to rip it out. I'm tired of dealing with this, but well, no, I'm not. I'm not serious. But yeah, this is, I'm just really frustrated with this.
**Ariel Demarco** 07:29 Yeah, and that. And that's a bit of also the platform specific issues that our topic I was going to to talk about. But I know if you, if you want to 1st discuss the data compression and how to address it, or or.
**Bryce Buchanan** 07:40 Yeah, let's yeah, do we? Do you have any thoughts about what.
**Ariel Demarco** 07:44 No.
**Bryce Buchanan** 07:44 You to fix this.
**Ariel Demarco** 07:46 No, but to fix this. There's like kind of doing a rollback.
Again, copy the code in in our in the open Telemetry Repository, create a module that it's open telemetry data compression explicitly say, this is a copy from this repository. Blah blah.
**Bryce Buchanan** 08:06 Yeah.
**Ariel Demarco** 08:06 Yeah, so we are attributing the the owner.
That will probably fix it.
I haven't seen so much contributions contribution. Sorry in that repository, so I don't see my Pr. Being merged sooner to be honest.
**Bryce Buchanan** 08:27 Hmm, I see. Okay.
**Alex Cohen** 08:29 I I'm sort of not of the same opinion as Ari here.
we should not be copying code in from other modules and changing the name and bringing it in. That'll just lead to problems down the line. We should push in that that module, or or spm, or pod or whatever to get the new code merged. It'll not just be good for us. It'll be good for everyone else that uses it as well, because it's pretty widely used. I think the people that maintain it are probably just not paying attention. We just need to find them and push them a little bit, and I'm sure they'll get it merged right away.
I think. Yeah, I I think we can do do better than than copying the code in.
**Ariel Demarco** 09:13 Yeah, that's another option.
I don't see.
I don't see something bad on on doing it like the problem we had before is because we didn't change the actual class name and the module name was exactly the same. It was in that repository. So that was one. That was the problem, the original problem making collisions with others. If we have prepend an open telemetry or hotel, or whatever the problem won't exist, I agree that it will be great if we can contribute it.
My Pr. I won't. I won't close it. I will leave it like there until the the Maintainer tells me. Hey.
what we can do. But yeah, it's it's a matter of this deciding what what we want to do.
We had a leaf broken, the cocoa pot.
build or or fix it in a in any of those ways.
**Bryce Buchanan** 10:13 Yeah. I'm not super concerned about this particular cocoa pod being broken.
because the from what I understand, the people who are dependent on the cocoapods are not really using like the whole stack of the the packages that we offer. So like, really, they're just using like the the Api and SDK.
**Ariel Demarco** 10:41 Yeah, so.
**Bryce Buchanan** 10:43 If we I you know I'm I'm kind of more with Alex in that we should probably just get them to to fix the. You know their implementation rather than trying to fix it on our end. Just sort of hack it together. May Ari, do you have the pr, can you link that in the in the topics here, and maybe we can all all get on there and like like, add a plus one to it and I'll message some of the owners on through through Github, if I can.
**Alex Cohen** 11:17 We could temporary temporarily. Just use the fork as well, whatever whatever fork already created. I don't know if you created under embrace or under open telemetry.
**Ariel Demarco** 11:27 Oh, yeah, that's a good idea, too.
It's a personal one.
**Alex Cohen** 11:30 Yeah, we could just create it under open telemetry and and push the pr again under there and just point to that until the data compression team. You know, merges it that I don't see any reason why they wouldn't end up merging it at some point. So.
**Ariel Demarco** 11:48 It might be, I mean, I'm even offering just adding vision OS to the cocoa spec.
Because in my pr, if you see it. I changed the whole package.
and they talk about spec. And the original versions that this library was supporting are non-existent with the new package version. So I had to bump them.
So all of all of that is in the review of the all the pr description. So the owner can just ping me and say whatever he wants.
I'm open to do the change whenever it's necessary.
**Bryce Buchanan** 12:26 Okay.
yeah, I think I think that's a good way forward. Let's let's use the the fork until we can get this fixed or in the in the upstream repo and we could try to do another release and see if that like. You've confirmed that that cocoa pods will like Lent properly, using that, using your fix.
**Ariel Demarco** 12:51 Yeah, yeah, I did a link, and it's working fine. I wouldn't. I wouldn't use my fork, because we'll have problems with others using the original fork.
Oh, yeah, that's a good point, and will be breaking compatibility.
**Bryce Buchanan** 13:05 Yeah, I have.
**Ariel Demarco** 13:05 I think that your idea of for a while not supporting this library and not building it in cocoa, see something we can, I don't know. Add in the readme, or add something like that, and like, create a Pr. To disable for some for some time the building of those a coco bots. Facts. That depends on data completion.
That and add warning in the read me that for for the time being, until this Pr is gets merged.
**Alex Cohen** 13:36 Curiosity. And just I haven't looked at, or what I know. It compresses data, obviously. But like, what does it actually do? Is it? Is there something that's that's built into the frame, into the the OS frameworks that we could use instead? Does this just wrap up a couple of things. Do we use the whole thing like? Is it possible to just remove it and move to something else?
That's cool.
**Bryce Buchanan** 14:01 Yeah, I don't know what it does off the top of my head.
**Ariel Demarco** 14:04 Neither do I.
To be honest.
**Alex Cohen** 14:07 May. Maybe it's super simple. And we and it's just like a 1 liner today that used to.
**Bryce Buchanan** 14:12 Yeah.
**Ariel Demarco** 14:13 No, I I opened. I opened the code, and and, to be honest, I didn't understand anything. So I you gotta understand compression or or the things that it doesn't do the hood. It's not doing any sort of magic. Probably somebody burst on that area should understand the code and and.
**Bryce Buchanan** 14:30 Yeah, it's it's doing. It's I think it's used for, like Gzip and that sort of thing, ma'am.
So there might be other options, too. We might not need to use it. It could be It could be, you know, outdated. There might be something in the OS that actually does that. Now.
**Ariel Demarco** 14:49 Oh, not! That's also a possibility.
**Bryce Buchanan** 14:54 Okay.
Okay.
**Ariel Demarco** 15:18 Alright and do some research on that. If you want.
**Bryce Buchanan** 15:21 Oh, yeah, that'd be great. Thank you. Ari.
**Ariel Demarco** 15:26 And the other topic is, basically, I wanted to know your thoughts on on on this issue, because lately I noticed that many of the issues being raised, whether related to dependencies, build on distribution, we talk about, or spm.
or even the discussion the other day of bump into different versions stem from the fact that we try to support every single platform and all use cases. Aka mobile, slash, desktop, slash backend on one hand, from my perspective working at the brace. I I'm glad that we did a bump to Ios 15 or 16, because it will be a problem for us, but I also get that. What works well for our use case might create complication for other use cases.
On.
I don't know. I've seen that there are some other stuff that is changing in the spec, like, for example, there's an update to add a warning for people using mobile to not use the metric signal, because in the way it works it will load up, blow up the the collector because of the amount of different resources you are going to get.
**Bryce Buchanan** 16:33 Oh, yeah, that's a good point. Yeah, yeah, there really needs to be layer for that. But.
**Ariel Demarco** 16:38 Yeah. And and that's what I'm I'm I'm trying to understand. I also part of our company is also contributing in a new sig. That is the Browser Sig. That is a subset of the Jsig.
So I I don't know. I wanted to know your thoughts, because I know it's giving you guys problem in the whole open telemetry, swift repository to support the mobile aspect of this.
And maybe there's a better solution or something we can do or something we can contribute to. To make this easier for for all and and not create these kind of issues like everything we we are talking about data compression is because it's a problem on Ios, basically.
**Bryce Buchanan** 17:21 Yeah, you, you know, I mean, this has been a. This has been a problem. Yeah, the entire. The entire lifetime of this project is just like, you know, all of open telemetry is is server centric, and nobody gives a lot of thought to the mobile side of things. And I mean, maybe I'm kind of of the opinion is like, Okay, we wanna like people need metrics like, Are you kidding like, I don't care if it blows up the collector. That's that's the collector team's problem, you know, like.
they need to start thinking about mobile. And the only way they're gonna start thinking about mobile. If is, if their lives get difficult because of it.
**Ariel Demarco** 18:03 Yeah.
**Bryce Buchanan** 18:04 Because you know, no, no amount of complaining that I've done has gotten them to consider mobile. I mean, there's Sigs related to to Mobile like there's the there's the client side, Sig, but they have the same problem where they're like we need this. And then the entire spec, like stack is just like, no, we're not gonna do that. And so I I really don't have a lot of goodwill towards towards like the the greater organization, you know, regarding like these conflicts. So like, I'm just gonna I'm gonna provide metrics. And people are gonna expect metrics. And if there's problems upstream with metrics. Those problems need to get figured out upstream. And I'm willing to have like work with upstream people to get that sorted out. But we need to provide metrics like that's not. It's telling people not to use metrics is insane, like, yeah.
**Vinod Vydier** 18:55 And I.
**Ariel Demarco** 18:56 Yeah, I.
**Vinod Vydier** 18:56 Yeah. Even the collector problem that we talked about right on the server side is does not really exist on the on the browser side, or, you know, on the client side, right?
Because they are coming from a different place. So you will end up hitting an endpoint that is highly available, not like a collector, that you need to add additional memory if you have more servers in the cluster or something. So it's a very different use case. So I think there is a fundamental, I think, difference the way that people think about it. So server side and the and the client side in in open telemetry.
**Ariel Demarco** 19:32 Yeah, I think there's some sort of disconnection, but seems that it's getting track the client seek is is is adding more, more and more of these things to the specification. I think they are pushing now the the crashes and the sessions and the exceptions even on the website of things.
So I think that at some point the metrics should be a bit different for Mobile than from the back end, because of the way resources work. But in the end.
I think that not having metrics as a signal, it's going to not be the best solution. Long term.
Yeah.
I I know this is is like a broader topic. But I wanted to know what what would be the best way to address this. Considering. Now we have problems in in the repository.
trying to the multi-platform way of working.
**Bryce Buchanan** 20:33 I I think that, like the the our foremost target is mobile ios, you know, and and ipad, and those those sorts of mobile devices, the other stuff like the server side, swift, the vision OS stuff that's all extra and and if we have to like, I think we should pair it back. But I I think that like server side swift is okay, like there's not. We don't get a lot of issues with that. Maybe there are some some contentions, but it generally gets sorted out quickly, and also by the people who are actually passionate about that particular side of things.
but like, yeah, the vision OS was kind of like a like, I honestly like, it might be better just to like, not support vision. OS, anymore, you know, like, 1st of all, it's super niche, like how many, how many vision? OS, how many like of these ars are floating around, you know, like I don't know but it's almost like the Google Glass. It feels like I've never seen one in real life.
**Vinod Vydier** 21:42 No, in app apple itself is gonna move out of that space.
**Bryce Buchanan** 21:46 What's that?
**Vinod Vydier** 21:47 App apple itself is gonna stop making. You know, it's gonna move away from the vision hardware.
**Bryce Buchanan** 21:52 Oh, okay, yeah. So like, why are we even supporting it? Maybe we should just revert that. That's silly. It's causing too much problems.
**Ariel Demarco** 22:00 Yeah, I don't know. It's is this, this was mostly to to bring the discussion. I agree that if you do see you do something on Swift, like 95, 90% of the user base will be Ios.
yeah, by the west.
some of them will be Watch OS and Mac OS, and the rest will be like vapor, and all those other use cases. And, as you said, like, whenever we have, like Linux issues or stuff like that people tend to come and try to contribute and and test the issues, and and see if they can reproduce it. And like they are passionate about it.
So I know maybe the focus should be mostly mobile of the of the Sig, or stuff like that. But I know I know you work at elastic. I don't know natural where it works, and if you, your your main concern is not mobile.
Well, mine.
**Bryce Buchanan** 22:54 Timing altern is mobile, absolutely.
**Ariel Demarco** 22:56 Oh, I know naturals to be honest, because.
**Bryce Buchanan** 23:00 Yeah, nachos. A free agent, I think, in terms of of of hotel at least, and his main focus is mobile as well. So at least at least in the hotel sense. I think he works at a security company now.
But yeah, I I think yeah, it's it's the addition of the vision OS has only caused us problems like, you know, vis-a-vis, this data compression thing.
So.
**Ariel Demarco** 23:31 Okay.
**Bryce Buchanan** 23:32 Yeah, let's just get rid of it.
**Alex Cohen** 23:35 Oh, wait! Wait! What we.
**Bryce Buchanan** 23:38 What?
**Alex Cohen** 23:39 We can't get rid of just one of Apple's platforms. I don't know if you were serious or not.
**Bryce Buchanan** 23:45 No, yo, I am serious. Yeah, it was only just added in it was a cute idea. And it's it's not working for us. So.
**Alex Cohen** 23:53 I mean, it's not working for us. We have an issue with data compression which we can solve pretty pretty easily. What what else? What other issues do we have.
**Bryce Buchanan** 24:03 Well, I don't. I don't know but like it. It's I I don't know. I just don't see it as like a really an important yeah.
But I mean.
okay, alright, if you want, if you want to push back on it. That's fine. Like. It's only been in there for one release. It was like, you know, it's It immediately caused us problems with this data compression stuff. It's not. Why, like, I like, okay, let's resolve the data compression stuff. If there's other issues, then maybe maybe we can revisit this.
But like I, you know, I I'm not super like I. I don't really see vision OS, as like a really important platform to support for this, you know.
**Alex Cohen** 24:54 Well, I mean, I I can definitely understand that that point of view. But maybe maybe some people do, and maybe some people are going to go, some to some other open telemetry implementation because they need vision OS like, for example, embrace supports vision. OS right ari, we support vision OS.
**Ariel Demarco** 25:13 To be honest, I think we don't.
**Alex Cohen** 25:16 I think we don't.
**Ariel Demarco** 25:18 No, we were. We were planning. But it's it's it's a bit of of the same thing that supporting it depends on other sdks that are behind you to support it, and not all of them support them. So it. That's why it was complicated. Remember that at some point open telemetry didn't even have like cocopod support. So we added cocoapot support for the open telemetry. Api and SDK.
At that point.
**Alex Cohen** 25:48 That's different. That's a package manager versus a full on OS or.
**Ariel Demarco** 25:53 Yeah, yeah, yeah.
I'm yeah. Yeah. When I when I'm meaning supporting, it's being able to fully compile something in in that platform, regardless of. There's a preprocessor Macro, or stuff that it's a platform specific, like vision OS apis, or that are not in the vision OS plus being able to distribute it to all platforms. So we don't have support currently at the Maurice.
I'm glad that open telemetry tried to to provide support for it, but maybe something to us.
as Bryce said. Maybe if it's start to bring more and more problems, maybe something to revisit.
**Bryce Buchanan** 26:36 Yeah, alright. That's fine. Yeah, if if we can't resolve the data compression issue, if we resolve the data compression issue, and there's more issues with vision. OS cause I I you know I'm not sure how many other how many other dependencies we have that are not going to be compatible with this.
Oh, yeah, okay, so yeah, if if we can't solve this quickly, I don't want to spend a lot of time on it. We've got more important things to do.
**Alex Cohen** 27:20 I mean is someone gonna to resolve data compression? Or should I go because it's not.
**Bryce Buchanan** 27:26 Already said that he was gonna.
**Alex Cohen** 27:27 You're gonna take.
**Ariel Demarco** 27:28 Yeah.
**Alex Cohen** 27:28 Webinar.
**Ariel Demarco** 27:29 I I'm going to look at it. Probably I can bug you and bother you a bit, because help me out if I don't understand something.
**Alex Cohen** 27:36 Yeah, I'm just thinking it doesn't seem high on your priority list. If you don't care about the vision OS support. And this is for vision OS support. So like, I actually care a lot about it. Because even though, even though yeah, there are, there are, you know.
reports out there that apple's gonna drop it right? How do you actually know that they might drop that? But there's still going to be support for vision? OS, but maybe not the actual hardware that we're talking about now. That's expensive. But you know, whatever I just wanna, I just wanna make sure that the chances are that we keep it are good instead of it just lingering.
**Bryce Buchanan** 28:13 Sure.
All right.
So let's talk about the view. Ui view. Ui swift ui view versus open telemetry view.
**Ariel Demarco** 28:37 It's it's a simple issue, like, if you have both imports with ui and import open telemetry. SDK, there are 2 views like open telemetry SDK metrics view and the Swiftui View protocol that it's well known. So it's basically specified. Sweet ui dot view or open telemetry SDK view.
**Bryce Buchanan** 28:59 Yeah.
oh, sweet.
**Ariel Demarco** 29:05 I'm not fully into the metric spec.
If view the actual name could be renamed eventually to metric view, or something like that.
**Bryce Buchanan** 29:17 Yeah, we could do that. That's that's a that's an option. I mean, the spec just calls it a view. I'm kinda like this is, yeah, this is frustrating like, it could be namespace. But then people would have to namespace swift Ui view right?
**Ariel Demarco** 29:32 Yeah.
**Bryce Buchanan** 29:33 Which seems stupid, don't probably don't want people to do that.
**Ariel Demarco** 29:39 Practically speak. Objectively speaking, you should abstract whatever you have in your ui to something internal. So you have open telemetry in another object or class or file importing open telemetry. Ck, so you can use this with no problems. But yeah, I know that for somebody trying out open telemetry, it might be a problem.
**Bryce Buchanan** 30:03 Yeah.
**Ariel Demarco** 30:03 To figure out what is the actual problem.
Well, we understand that because we know that base.
**Alex Cohen** 30:09 One of our one of the embrace employees found this because the whole example program that they had written had this had this problem all of a sudden, after we upgraded to 2. So I think it would be, although your best practices sound really good. I don't think most people follow them, especially that our example code doesn't. So
**Ariel Demarco** 30:31 Yeah.
**Alex Cohen** 30:32 But maybe we could just move it inside of a structure, another structure or something to namespace it. Instead of being metric view, it could be metric, dot view, or whatever. Wherever we wanna put that that way, it's that way. There's no there won't be any problem at all.
**Bryce Buchanan** 30:51 Yeah. Yeah.
Hmm.
**Alex Cohen** 30:57 I would prefer that over over like a a full on name. Metric view, although views very, very, very general. So it doesn't really.
**Ariel Demarco** 31:08 Oh, we owe yeah, nothing.
**Bryce Buchanan** 31:19 Yeah, so you're like suggesting we wrap it in a in another class, or something like that.
**Alex Cohen** 31:25 Yeah, I don't know. I don't know exactly where it is within the SDK, but like, if you have like a struct or a class that's called metrics, that could basically just be there to hold other.
**Bryce Buchanan** 31:39 You know. Kind of name.
**Alex Cohen** 31:39 So basically act as a namespace.
**Bryce Buchanan** 31:42 Yeah, I I like that idea better than just renaming it to metric view itself.
**Alex Cohen** 31:50 We'd have to try it to make sure it actually works.
**Bryce Buchanan** 31:53 Yeah, that's that's that's my thinking is that that might not actually work. But
**Alex Cohen** 31:58 I think it should, because view should not be at the global namespace. In the in the global namespace at all. It should only be in the metrics metric namespace. So I think it should work. But I don't know if the compiler would be like oh, I see these 2 views, and you know I don't understand. I still don't understand. So.
**Bryce Buchanan** 32:15 Yeah, yeah.
**Alex Cohen** 32:17 Yeah, we can try.
**Bryce Buchanan** 32:18 Yeah, the the issue is, yeah. The issue is, you know it. It is namespace to the package. But the problem is is that you would have to. You have to namespace all the conflicts with it. I I don't know if there's a way to tell Swift to like. If you see it alone, then assume it's this one or not, but.
**Alex Cohen** 32:37 All, all packages are global namespace. So everything in a package goes to the global namespace. Even if you can use the package name to namespace it better to differentiate it. But anything namespaced within another structure class needs to be used within. Within there.
**Bryce Buchanan** 32:53 Yeah, yeah.
**Alex Cohen** 32:53 So it wouldn't be global or it should be.
But use the testing.
and it might be like it might, it might. We might be better off that way, because just using view within any code anywhere is a bit could be a little bit confusing as to what it means.
**Ariel Demarco** 33:18 Think that wrapping it will work.
**Bryce Buchanan** 33:37 Yeah, I don't know. Yeah.
I don't know if metric view is the right name for it, or hotel view, or yeah.
**Ariel Demarco** 33:46 In the past was stable view, and the other one what? Which was the like? The deprecated version of the view.
Yeah, yep.
**Bryce Buchanan** 33:56 What was that? A question?
**Ariel Demarco** 33:59 Yes, because there were 2 like the stable, that is, one bed that we after we we then rename it to just view.
Yep, yep.
was like an old version, or of the of the one that we deprecated. There was an instance of you there, or or that's a concept we created in the new version.
**Bryce Buchanan** 34:18 No, no, that. Yeah, that's a that's a new metric. The the stable metric spec is the view. And yeah, the original metrics did not have a view in it.
**Ariel Demarco** 34:30 I see, I see, I see.
**Alex Cohen** 34:34 What does it do, anyway.
**Bryce Buchanan** 34:36 This dictates.
How metrics are processed. I believe so. If you wanted. So you have, like a you have like a a a meter, or.
I guess, an instrument that produces like counts of things. Let's say you, you're counting like how many network requests you've made.
You could reorganize that data into a different aggregation, using a view so.
**Alex Cohen** 35:08 Like, if you're.
**Bryce Buchanan** 35:08 Yeah, like, you,
**Alex Cohen** 35:10 It's just like a database view or a sequel query, created view, or something like that. It's just the aggregation how to how to how to read the data, how to aggregate.
**Bryce Buchanan** 35:20 Yeah, yeah, you can specify a you can specify a regex even through view, and say, like, if my metric is named this way, if it uses this type of counter, re-aggregate it as like a Max value, or a gauge, or something rather than a than a than a counter or something. So yeah, it's it just provides, you know.
I don't know if it's like a like a SQL. View, because I don't really know.
**Vinod Vydier** 35:50 No, I think it. I think it's very similar to the database table to database view. Yeah.
**Ariel Demarco** 35:57 Yeah, it's it's to simplify gathering metrics and and aggregating them. Basically that.
**Alex Cohen** 36:04 So in. In that case, you might guys mind if I ask folks mind if I ask another question, why, why, Ari, earlier, were you saying that we could get a lot of metrics being pushed out and it would overload things or collect collectors. Aren't these? Aren't the metrics like locally aggregated things, using views and and whatnot.
Wouldn't that.
**Ariel Demarco** 36:24 That the thing is that if you, the the, as far as I understand the the way, then our aggregating is also using the resources.
So at at the ingestion level, you'll have like a lot a lot of different resources, because each device it's totally different from the others, and the versions and the all the stuff could change. So the the level of the the amount of of different type of resources it's going to make collectors.
It's going to make the life of the collectors a bit more complicated. This is in order to help, once the data is ingested, how to how to aggregate it, how to show it, how to use it, how to filter it all the stuff.
because it's it's it's different that opens, and metrics as a as a signal existed from a long time ago.
Open telemetry adds the possibility to link things each other using the resources concept.
So the problem with an open telemetry collector is that it's based on the, on the concept of the resource is the most problematic thing. Whenever we are talking about metrics there are a huge amount of of data plus the resources.
So the level of cardinality, it grows a lot.
**Alex Cohen** 37:50 Okay, I guess I'll have to dig into the. I guess the whole resources part that it sounds expensive, not the metrics, but the resources that sound expensive. So you there, you can't have a lot of them, for some reason or collectors blow up.
Yeah, I'm I'm curious. I'll go. I'll go see for myself.
**Ariel Demarco** 38:08 If if you're curious, the the Github issue, or Pr added to the notes of of this meeting, where they are discussing, to basically add the warning, have a bunch of links and relevant information on on why, it's complicated for for metrics to work well on on mobile. So.
**Bryce Buchanan** 38:31 This this one here, right.
**Ariel Demarco** 38:33 Yeah, yeah, exactly. You can take a look to it.
They've been discussing that on the, on the glance, I think. See? I think.
**Alex Cohen** 38:42 Cool. That link is in here somewhere in the
**Ariel Demarco** 38:47 Yeah, yeah, yeah, there.
**Bryce Buchanan** 38:49 Yeah, this one. This one here is.
**Alex Cohen** 38:51 Okay, it's linked in the issue.
**Ariel Demarco** 38:52 So.
**Bryce Buchanan** 38:52 Oh, no, that's not, that's our. That's.
**Ariel Demarco** 38:54 My my bad. I didn't add it to. I added to the chat of this meeting.
**Bryce Buchanan** 38:57 Oh, yeah, it's in the chat. That's where I got it.
**Ariel Demarco** 39:00 i i i can link it.
No.
**Bryce Buchanan** 39:07 Oh, I guess we didn't have a topic regarding that necessarily.
Yeah, yeah, go ahead.
**Ariel Demarco** 39:28 Oh!
**Alex Cohen** 39:29 It's ready.
**Bryce Buchanan** 39:31 Alright cool.
Alright, if there's no other topics. I just wanted to go through. Oh, this is the spec.
How do I get here.
there we go. I wanna go through just review our issues that we have okay, so we've talked about this one yeager, baggage, baggage, propagator field. Center.
Oh, interesting.
**Ariel Demarco** 40:19 They are. They are in the stack trace.
It's datadoc data, Doc.
**Bryce Buchanan** 40:24 Yeah.
**Ariel Demarco** 40:25 A different version of open telemetry.
**Bryce Buchanan** 40:29 Yeah, I don't think, think.
**Ariel Demarco** 40:31 This really matches.
**Bryce Buchanan** 40:33 Yeah, this might not be this, this, we might need to talk about this or talk with data dog about this, because we recently removed the data dog exporter. Just because we don't. It's not really a There was no maintainer for it.
**Ariel Demarco** 40:49 Yeah, but but basically they have their fork, and they are saying they are using open telemetry. Api. 1, 13, one. That is the one that they.
**Vinod Vydier** 40:57 For.
**Bryce Buchanan** 40:58 Yeah.
**Ariel Demarco** 40:58 They modify it, so there is no need to.
**Vinod Vydier** 41:02 Yeah, it's an older version, right? It's an older version that still had the exporter dated of the exporter. So.
**Bryce Buchanan** 41:07 Yeah, yeah, maybe.
**Vinod Vydier** 41:08 No.
**Ariel Demarco** 41:09 Yeah, let me give you the the actual repository where they have the the open telemetry org.
Maybe you can just mention, hey? I think you should submit this here.
**Bryce Buchanan** 41:30 Yeah, I'll I can update. I can reply to that issue there, yeah, it's not too.
**Ariel Demarco** 41:37 Putting it in the chat. This is the the fork.
**Bryce Buchanan** 41:42 Cool. Alright.
Okay. Let's see here, Header link, command failure. Interesting.
Oh.
**Ariel Demarco** 41:58 A linker, fresh.
**Bryce Buchanan** 42:07 Curious. This might need a little bit more. Details getting this error when adding, Tlp exporters.
Grpc, type Api.
I can follow up on this one as well. Just ask for a little bit more details about about what's going on, or maybe get their package. See how that's being set up.
This one's a simple one as well. I believe that they just need to go stable meter, provider.
builder.
But I can also verify that no issues there. Request. From who?
What in the demo report? A failure on 200 responses? The app can't decode the response.
This this sounds like this sounds like graphql, not graphql, wait, is that is that right?
**Ariel Demarco** 43:48 No, it could be. Also, whenever I think that the process of decoding is not tied entirely to the request process.
**Bryce Buchanan** 43:58 Yeah.
**Ariel Demarco** 43:58 You. You can just have the binary, move it everywhere, and after one second go and try to decode into something else. I don't think maybe they they should post the use case.
**Bryce Buchanan** 44:11 Yeah.
**Ariel Demarco** 44:12 Or Qrpc. Or something like that.
**Bryce Buchanan** 44:14 Yeah, they might be able to to pull down like the the active span as well.
although that might be. That might be Why,
**Ariel Demarco** 44:29 If you receive a 200, if if you receive a 200 already, the the span should be closed.
**Bryce Buchanan** 44:34 Yeah, yeah, that's yeah. That's what I was thinking. They might be able to snag it. After they create the request and then hold on to it so that they can update it after, although it might be immutable by that point.
**Ariel Demarco** 44:46 But span link.
**Bryce Buchanan** 44:47 Yeah. Probably the yeah. The best situation might be to to do a span link with an error like, create an error, and then link it, yeah.
does anybody wanna follow up on this one.
**Vinod Vydier** 45:02 Yeah, I can. I can do this.
**Bryce Buchanan** 45:04 Alright, cool!
Alright! Thank you, Vinad.
I'll sign it to you that favor.
**Vinod Vydier** 45:25 Gonna be in.
So how do I avoid that?
Figure it?
Yeah, it's okay.
**Bryce Buchanan** 45:35 Alright, URL session, instrumentation, configuration.
**Vinod Vydier** 45:40 Oh, okay, around that. But setting of the Rpac.
All gotta make sure that sort of thing.
**Bryce Buchanan** 45:57 I think the context of this is in the This isn't. This isn't the network instrumentation, is it?
**Vinod Vydier** 46:06 Think this.
**Bryce Buchanan** 46:07 This is
**Vinod Vydier** 46:09 Right now.
**Bryce Buchanan** 46:11 I think that this might have to do with.
**Vinod Vydier** 46:14 Don't! Banana.
**Bryce Buchanan** 46:14 The exporters.
**Vinod Vydier** 46:17 Get out. Has an annotation where, like, you can annotate a nation based pharmacy, then automatically gets access to that.
that is mainstream focus as an administrator of you.
**Bryce Buchanan** 46:31 Hmm!
Does anybody want to follow up on this one? Otherwise I can. I can take it.
**Ariel Demarco** 46:42 To me.
**Bryce Buchanan** 46:43 Okay. Thanks. Everyone.
**Ariel Demarco** 46:44 Take a look.
**Bryce Buchanan** 46:56 Add support for capturing ISP network type and device information in Ios. SDK, I'll just throw. I.
**Ariel Demarco** 47:04 I been investigating about this, some of these, that data was available in the past.
and Ios stopped providing them. I don't know if there's a low, level Api, we can use to get that information low, level, meaning something.
It's private or or something that might get an apple rejection or not about the the old Apis to get all of this information. Is not there. Some I think you can just get if it's Wi-fi, or Lte, or stuff like that.
No.
**Bryce Buchanan** 47:42 Yeah, right? I'm not. You know. How is the Android SDK doing that? I.
**Ariel Demarco** 47:48 No, Alex, if if you're a bit more knowledgeable on the low level area, if this is achievable.
**Alex Cohen** 47:57 Sp.
Probably not a good idea, just for you know anything regarding the telephony frameworks and stuff. I don't think we're even allowed anymore to use that to use that stuff, and we probably shouldn't drop it in to this. We should probably let 3rd parties put that information in, if they need to, maybe give them a module that can get it for them and apply it. But seems like a seems like a recipe for us to get into trouble.
**Ariel Demarco** 48:33 Yeah, I know that we have the the network status here.
**Bryce Buchanan** 48:36 But that just is more like the type.
**Alex Cohen** 48:40 You see cord telephony, telephony?
How are you? Pronounce it?
**Ariel Demarco** 48:45 Yeah, it really really changed the amount of data that core telephony now gives you. It gives like, just Wi-fi and all the stuff. And that's it. It doesn't really give you the actual caveat.
**Bryce Buchanan** 49:00 Oh, this this does isn't provided anymore.
Interesting?
Alright! Well.
**Alex Cohen** 49:07 What is, what is the what is the the request or the issues to get it automatically or.
Support.
**Bryce Buchanan** 49:15 Yeah, I think that I think they just want. You know, it's a feature request, essentially just to get like they want.
the ISP carrier, slash, carrier name, network type.
**Ariel Demarco** 49:30 Do you have xcode? Open.
**Bryce Buchanan** 49:33 Yeah.
**Ariel Demarco** 49:34 You can. You can see city carrier dot h the hitter.
It's been deprecated, like most of it, on on Ios 9.
**Bryce Buchanan** 49:42 Oh, wow!
**Ariel Demarco** 49:45 Now it gives you like a random value that is useless.
**Bryce Buchanan** 49:49 Oh, interesting!
**Ariel Demarco** 49:50 It's the same that happened with the the Mac address. At some point they started giving you like a hard coded string.
Same happens with the carrier. Now.
for privacy reasons which is obvious.
**Bryce Buchanan** 50:02 Okay? Deprecated with no replacement. Okay?
**Alex Cohen** 50:07 It might be interested. It might be interesting to check out like those those privacy P list flags. I don't know if any of that is in there, and we'd have to report it through the privacy file or not.
**Bryce Buchanan** 50:19 Oh, yeah.
**Alex Cohen** 50:20 So anything that's in there, we probably should just should leave out and let let people do it if they want to.
**Bryce Buchanan** 50:31 Yeah, I guess we used to provide this stuff. But through the through that, through that instrumentation. I was just looking at the network status stuff. But I guess if it's not available anymore.
then it's not available anymore.
I can. I can follow up on this one. It it seems pretty straightforward to to answer.
I guess. That's probably enough for today. We're kind of we've run out of time. So yeah, thanks everybody for showing up today. Good topics have a good weekend.
**Vinod Vydier** 51:13 Thanks.
**Ariel Demarco** 51:14 Y'all.
**Vinod Vydier** 51:15 See you have a good weekend.
**Ariel Demarco** 51:17 Next week.
