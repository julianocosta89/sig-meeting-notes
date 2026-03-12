SIG: .NET Auto-Instr SIG
Date: 2025-08-27
Duration: 25 minutes
============================================================

## Zoom Recording Transcript

**Zach Montoya** 00:47 True.
**Mateusz Łach** 00:52 So….
**Piotr Kiełkowicz** 00:59 Hello, guys.
Any volunteers to drive meeting today?
**Zach Montoya** 02:56 I can take it.
**Piotr Kiełkowicz** 02:58 Cool, thank you.
**Zach Montoya** 03:00 Let me just pull up a new screen, huh?
Alright… Alright… And it should be shared now.
Cool.
We can start with the agenda items that people have, added to the to the agenda, so there's two of them. The first one is we have a… this frequent sampling feature, that… we have, I think, at least one PR that was merged for ESL, Frequent sampling of Selected Threads.
So… Mattouche, it sounds like you want to cut a release soon so we can get this feature… Really? Yes.
**Mateusz Łach** 03:46 Yes, yes, if, if Sigu would be okay with that, we'd be interested in, Releasing the, like, beta version, so that our distribution can build on top of it.
I've been, doing some… so basically this was the one PR that is linked here, and also I've been doing some follow-up PRs, resolving some issues or addressing the feedback.
created another PR today, and I'm actually planning two more PRs, I think.
One is, with the, basically, incorporating some feedback that FTCAR shared some time ago.
And, the other one is, some simple change to the API, and, I think that's all that is planned related to this feature.
At the moment, so we should be able to… We should be, like… all of the code changes should be, … ready by the end of the week, or early next week, so we'd be interested in doing the better release if Sikh would be okay with that.
**Zach Montoya** 05:00 kind of….
**Chris Ventura** 05:01 I'm okay with that. I think, it would be nice to see what the remaining to-do list is. I don't know if you have a collection of sub-issues.
**Mateusz Łach** 05:11 Fuck.
**Chris Ventura** 05:12 Or anything like that?
**Mateusz Łach** 05:14 Okay, okay, I'll clean them up, sorry. Some of these issues, or basically some of the things that I was addressing in the recent PRs were things that were not planned, but basically I, like, noticed along the way, so I'll link all of them here, and at least the remaining stuff, so… I'll clean up… basically, I'll clean up this, the issue description and the list of, What's left, after the meeting?
**Zach Montoya** 05:47 Yep, that sounds good. Yeah, if you link everything from this issue, I think that will… That'll help. Yeah, also, sounds good, so… Do, like, a beta release.
For that future, once all the related, items emerge.
**Mateusz Łach** 06:06 Sounds good, thank you.
**Piotr Kiełkowicz** 06:08 Not better stuff, we have only one thing, it is support for RabbitMQ 5.2.
But still… It is… it should be… Enough to really try the beta, and then make a follow-up with the stable version.
**Zach Montoya** 06:27 Alright?
Okay, and then, next thing is, Raj, looks like… oh, it looks like we've, finished the publishing of these two.
**Rajkumar Rangaraj** 06:56 That's correct. Just want to give an update, like, last week, I prepared a PR for this one to the release date. Had an approval, and I had a discussion with Piotr, and he also recommended to speak with, Ellen before, on the naming part, especially for this package.
So, I had a discussion about that. So after that, once I have all the approval, I went ahead and published the package, and used the package with whatever the .NET monitor branch. I have it. It works perfectly.
In the next month, in one of the SIG, I'll give a notification earlier, SIG, and I'll try to demo the… the entire functionality, how things work with that package, so… everyone will have a, like, view on how it's going to look. Like, we always speak about out of process, how in reality, it may look like it. So, really, the .NET Monitor, whatever the demo I'm planning to do, will be from my branch, not the released one.
But it… I think it's very important for us to, … rsync to, know that how this package is used.
don't have it is in the releases. I did not… I recall, I did not add anything. … I, in the GitHub release, a section.
**Zach Montoya** 08:27 Yes, yes, yes. Anything there, so just wanted to bring a topic, should we be….
**Rajkumar Rangaraj** 08:32 Adding it here, or would this… Cause confusions to the customer.
**Zach Montoya** 08:40 So I think last time we spoke, just having the tag, we thought would be… Most efficient, … I'm… ambivalent, we could do either, including a release as well.
**Rajkumar Rangaraj** 08:54 For the… anyways, for the customer's consumption at this point in time. It's a very, very earlier thing.
And apart from .NET Monitor, we don't have anyone else who's in need of this package at this point. So that's why I have a question, how do we do it? I want to take the SIG's input on this. Should we have an entry here, or how do we go about it?
**Piotr Kiełkowicz** 09:18 I think with tech, we should be fine for now. Okay. It's when we'll be more major.
then I think we should clearly put also releases for this.
**Rajkumar Rangaraj** 09:31 Okay, cool, that makes sense. Yeah, I agree with that Okay, that's all I have. Like, I just want to notify that this is… this has happened.
**Zach Montoya** 09:45 Good.
Thanks for getting out there, hopefully we can start getting some usage and… Seeing how that works.
Alright, so, are there any other items that people would like to bring up before we go through our regular agenda?
Alright, hearing nothing, I'll just keep going on with the regular agenda, so let's close others… oops, those other tabs.
Alright, so we have a couple open pull requests.
There's a couple of drafts, which, I think we can ignore for now. There's one with N-Log instrumentation, I believe people are taking a look at this.
There's… oh, yes, would you?
**Piotr Kiełkowicz** 10:31 I think it is important to look into this.
I don't have… I'm out of time, to be honest, to focus on this, but… I see that they created new library.
… just for appender, if I'm correctly, and I think it is no-go option for us.
And they will need to make a step back, so if you have some time to review it, and put kind of good comments there, it will be great.
**Zach Montoya** 11:05 Okay, yeah, I… I noticed that, too. Yeah.
Okay.
Add that to my queue. … Yeah, that made sense.
… Raj, do you know if there's any movement at all, or any updates on, sort of, like, the .NET logs, like, bridge API?
It's on that side.
**Rajkumar Rangaraj** 11:30 From .NET side, currently we are working on the .NET 10 prep in that repo. Once that is done, I think we should try to make the LogsBridge API from the experimental to a stable release. That's the next big thing, I believe.
Even if .NET does not provide… there are many customers asking for it in both these repos. So, we cannot keep waiting on the .NET. If there is nothing after the .NET, then probably in the… month of November, the work in the OpenTelemetry SDK should start, to… stabilize the blocks bridge.
probably, like.
Piotr, and I think most of here are even an approver or someone joins as a contributor there, so we can continue the discussion there and prepare a plan during… once after this .NET 10-based OpenTelemeter release is done. There is a big challenge in one of the things, that using the 10 with… how do we do it? Once we tackle that, we will jump onto the Lux Bridge in that area.
**Zach Montoya** 12:40 Got it.
Okay.
Yeah, I imagine we might… we might change a little bit of our instrumentation once that arrives, but it sounds like that's a little bit of ways off.
**Rajkumar Rangaraj** 12:51 Yeah, once that's released, like, in the contrary, like, Pyotra already had few, upenders, proposed, so we could restrict and bring them back.
And then take a reference of that here and make things very simpler instead of complicating with the CLR provider and doing… The custom things for it.
**Zach Montoya** 13:17 Alright.
Alright, so let's move on to the next one. So vendor in YAML.net. Piacho, is there anything else you wanted to talk about on this one?
**Piotr Kiełkowicz** 13:27 I think Raj have a good comment, yesterday evening.
And I doubt that I'm able to avoid any touches in the original form of the file.
Hmm… Public contract needs to be modified, and in my opinion, also the namespaces. Other… And there is no other changes in Vendorat's code right now.
So, Rash, I minimize the changes as much as possible.
**Rajkumar Rangaraj** 14:02 Sure. No, it's based on my experience also. We also vendor in Azure SDK. Based on our experience, if we change it, it becomes very, very tricky, changing this license. Well, that's why I could cache it based on my experience. We have burnt our fingers on the similar thing.
Looks like Martin also has a proposal, so I don't know what does that mean. Even if that is going to reduce a lot more work, even we can explore that. Looks rendering is very easy, but maintaining a rendered core is very, very difficult when we need to take an update.
**Piotr Kiełkowicz** 14:37 I think that our upstream… Didi Company has kind of good experience with maintaining this stuff.
**Rajkumar Rangaraj** 14:47 Oh, okay, cool then.
**Zach Montoya** 14:48 Yeah, there's… and this is something we can do afterwards as well. Basically, in the Datadog repo, there's, like.
Just sort of like an automation… oh, that's not the… that's not the page.
we built a small utility to, like, do the vendors. It's somewhere in here, there's… update vendors. Yeah, just a program, and it's like, okay, well, download it, and then apply a bunch of things to it. That's not it. … Actually, okay, so, I don't remember exactly where all the code is, but essentially, just, like, a small piece of code to, like, pull them and then do automated updates. It helps a lot… it helps, because a lot of it can be automated, like, the namespace stuff.
So we do some transformations, … So that is something that we can adopt later as well.
And this repo.
**Rajkumar Rangaraj** 15:44 Yeah.
**Piotr Kiełkowicz** 15:45 Bigger.
**Rajkumar Rangaraj** 15:45 For me, Piotr, I'll go ahead and approve this. Like, there are several ways to do this. I was just… pointed out a few things to reduce the maintenance burden, but it's not a blocker, we can go… Sure. Yeah.
**Piotr Kiełkowicz** 15:57 The good part with this library is that there were no changes in the last half of the year.
**Rajkumar Rangaraj** 16:03 Okay.
The only concern I had was the licensing part. Apart from that, I'm good with everything else there.
**Piotr Kiełkowicz** 16:11 I fixed, I think, correctly, the license and the file also, so….
**Rajkumar Rangaraj** 16:16 Okay, cool, I'll just check and… Approve that.
**Chris Ventura** 16:19 Does vendoring this in, … Get that, library to work with.
Net 462.
**Piotr Kiełkowicz** 16:29 I think so. No compilation issues, and based on what I've seen on, … the whole PR, not the… not the vendor staff.
Yevgeny mentioned that it is working for him.
**Chris Ventura** 16:42 Okay.
Yeah, because my main concern was that the original NuGet package was just a Net Standard 2 package.
**Piotr Kiełkowicz** 16:56 There is kind of… the only tricky part is probably test on tuples, but it is compiling very well on even on 462 in our repository, so I do not see any.
Issues with this.
**Zach Montoya** 17:20 Rights… Any other comments?
And this one… Alright… let's see what else we have… And there's one more we have with Containers Profiler. Looks like this got approval, and I also reviewed this, … So if anybody else would like to provide feedback, handling shutdown, this looks… What's good, though?
So, yeah, I think we can move on.
Alright, … yeah, those are not dependable. New issues… Let's see, we have a couple from this week. Oh, this one looks like you were just tracking that, the profile shut down. Okay, nothing to do there.
Looks like we have one with… ASPNuts.
Span information. I have not looked at this at all. I'm not sure if anyone else has taken a look.
**Piotr Kiełkowicz** 18:25 it is probably… if you open the country repository, it's PNET Core Tests.
**Zach Montoya** 18:41 NetCore or Espinot?
**Piotr Kiełkowicz** 18:43 Peanut curve, yes.
**Zach Montoya** 18:45 Okay.
**Piotr Kiełkowicz** 18:47 And root tests… And….
**Zach Montoya** 18:53 Oh, not that one, sorry. Wrong one.
Brad and sauce.
**Piotr Kiełkowicz** 18:57 Read me… AndroidMe file, in fact.
**Zach Montoya** 19:00 Oh, okay, sure.
**Piotr Kiełkowicz** 19:03 X… for .NET 8, or… yeah, or 9, whatever.
Behavior is very similar, and if you check the conventional routing.
So, scroll down a bit, there will be, kind of, more information.
And if you… check ideal HTTP route, and what we really produce in activity HTTP route, it is kind of two different things, and… I suppose the customer… the issue is related to this stuff.
Because even if you are able to determine the Controller on our side.
And action, we're reporting the route, the very base conventional routing information.
And it is reported for all ISPNets corresponds through the conventional routing.
**Zach Montoya** 20:07 Let's see… So this one is… Roosevelt template, spaces for spin, pushes conventional writing, template might refer to… okay, ….
**Chris Ventura** 20:25 Either way, I feel like a change like this is not for this project.
It seems like it's more of a discussion for the, … for the ASP.NET Core instrumentation.
**Piotr Kiełkowicz** 20:42 We have also reported it internally, to be honest, and if I have time, it is… I plan to look into it more closely next week.
I think Alan… … Nope.
has the biggest knowledge about this, so… how to handle it, … I will need to check with him how to handle it correctly.
**Matthew Hensley** 21:07 I mean, currently, this is what the… You're supposed to do.
I mean, that's the correct span name.
**Piotr Kiełkowicz** 21:17 Yes and no. I start to, talking with Ludmua in private channel, And she mentioned that The controller and action… Should be replaced by the actual values, because it is still low cardinality.
And I agree that it is not obvious from the semantic convention perspective. Rasmus raised the issue two weeks ago, but then he has some holidays, so no progress, no big progress there.
Yeah, next week, probably. I will know more.
**Zach Montoya** 22:09 Okay.
Should we… Do you want me to sign to you to follow up?
**Piotr Kiełkowicz** 22:16 Yeah, you can… you can assign to me, and I will hand it to them next week.
**Zach Montoya** 22:21 Okay.
Alright.
Okay, so that's all for the new… … Let's see… oh, I guess we can… Close this, right, Raj?
**Rajkumar Rangaraj** 22:42 Sorry, I was on mute and speaking. Yeah, this could be closed.
**Zach Montoya** 22:46 Okay.
Yeah, I think that's… Let's… Alright, so nothing else there on issues, new discussions… no, any discussions?
Pretty quiet place over there.
Issues assigned to projects… … Okay, I don't see anything… And then project board… don't think particularly many updates.
Let's see… … Got a bunch in the backlog, I don't think there's any updates that you have on the backlog items.
Yeah, I don't really see any updates, … Yeah, no status changes on these.
Is there anything… any other item that should be added here?
Alright, … Alright, so with the pageant board review done, it looks like that's the end of our agenda.
Any other topics that you guys want to discuss, before we, before we leave?
Cool, well… Alright, that's it for this week.
Alright, see you guys later.
**Mateusz Łach** 24:34 Cheer. Bye.
