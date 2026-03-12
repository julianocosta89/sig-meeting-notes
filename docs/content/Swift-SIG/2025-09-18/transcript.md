SIG: Swift SIG
Date: 2025-09-18
Duration: 34 minutes
============================================================

## Zoom Recording Transcript

**nacho** 02:35 It'll be not good morning.
**Vinod Vydier** 02:37 Good afternoon, Nacho, how are you?
**nacho** 02:40 Pain, pain.
**Vinod Vydier** 03:07 No, bryce, I know… Ori, I think, right, is also…
**nacho** 03:14 Yeah, Ari might connect, he said.
**Vinod Vydier** 03:17 But, yeah. I think from his car, something like that. Yeah, yeah.
So, how are you doing?
**nacho** 03:28 Mine, yeah.
You're not in Vegas this week?
**Vinod Vydier** 03:33 What's that? Oh, yeah, it was…
**nacho** 03:34 You're not seeing mega this week, because… You are always there. I don't know if it's.
**Vinod Vydier** 03:41 Yeah, yeah, I'm always there, you know?
**nacho** 03:44 Notice that's a gaming problem or something?
**Vinod Vydier** 03:47 I go 3-4 times a year, at least. Every big conference is in Vegas. That's right. Yeah, yeah.
I think Vegas is the only place that can have large conferences now.
**nacho** 04:02 Yeah, that's a.
**Vinod Vydier** 04:02 Yep.
Yeah, I don't even touch the… I don't even… I don't think I've played, even a single quarter, right?
**nacho** 04:11 You don't have to tell that.
**Vinod Vydier** 04:12 Yes, yes.
**nacho** 04:13 You know. I know.
**Vinod Vydier** 04:17 Okay.
**nacho** 04:31 So, do we… One minute more, in case someone joins.
Yeah, I was trying to clean up a bit the document.
Okay, so let's start the meeting. We are not any people today.
But, yeah, we… can, talk about.
**Vinod Vydier** 05:26 Some of the topics.
**nacho** 05:28 you know, if you have any new topic, just add it. If it was handled last week, I have updated the document so we can talk about that also.
Sorry… Trying to surrend it.
Yeah, there's a very few.
Yeah, that's better.
Okay, so, yeah, from last week, I have copied the new topics from last week and the weeks that… the topics we already have there.
So… Yeah, timeline for this issue, I can look into this next week, be not…
**Vinod Vydier** 06:24 Yep.
**nacho** 06:25 You have your name there.
Have you…
**Vinod Vydier** 06:28 I think I should maybe just assign myself.
**nacho** 06:31 the metric filters.
**Vinod Vydier** 06:33 Go. No.
I haven't.
**nacho** 06:39 Okay, yeah. Yep.
I will not then… Okay, data compression follow-up… I think it has been already handled, right? It was already handled that week.
**Vinod Vydier** 07:01 Yeah, I think that was the one that Ari was working on.
**nacho** 07:05 Yeah, it was Price… Okay, and it was removed.
So, is merge… yes, so we can remove it from the… Topics, because it was already matched last week.
Yeah, core version and releasing discussion, we talked about this, currently hiring.
You just connected, I have just noticed. We were talking about diversioning.
That we will have for core.
And the standard library.
we decided to move everything to the… to a newer version, so, both CocoaPods And the users can… can… can have an updated number for everything.
So yeah, that… That was handled.
We also had a new Slack channel for Swift Notifications, that has been created, It's an open channel, so anyone who Really want to get those notifications.
And who's interested can register for it. The name is… The name is exactly… This one?
It's… it's public, so if anyone 1st, too.
Get those notifications of the… PRs that are open, or issues that are created.
you can, register that. As talked, the, the, the use for it is not, not to, Flute or flood the main channel, because it hides all the conversation and all the questions that would happen there.
So, yeah.
document release-based behavior for Swift Core.
And Swift.
I think that there has not been work on that area.
If anyone wants to add something, while I talk, just please, raise your hand, or… Say something.
While I continue.
Semantic convention update, we talked about that a bit. There were no… things to handle here, I think.
sessions… There was.
**Billy Zhou** 09:59 Yeah, this was resolved, and I think you guys shipped it already.
**nacho** 10:04 Okay, so that was merged already last week?
**Billy Zhou** 10:06 Yeah, yeah, thank you.
**nacho** 10:08 That was 2 weeks. Oh, yeah, sorry, then I, see?
I have no, Okay, it has no, note that it was finished. Is this path worth continuing with? This is a Martin, PR?
Neo-fantastic, yes, that's right.
Yeah, I think it's waiting for merging.
Like, that should simplify it.
I read something up, yeah.
Randomly.
lists… Oh, what they be? Sorry.
It's… What?
Okay, this is the… Corporation and main report for the initial code relays, satisfy CocoPot's assumptions, Ari.
That was done, that… That has been already released.
**Ari Demarco** 11:46 Yep. Yeah, yeah.
**nacho** 11:49 So then I will… Don't you?
And also, the corporate… this release was also done, right?
Yes, yes. 2.1.1?
**Ari Demarco** 12:06 Yeah, in both, in both car and Zwift.
**nacho** 12:08 Okay.
Perfect.
The pre-release process is set to release as pre-release, and then manually set as released. That's already handled, right?
**Ari Demarco** 12:25 Yeah, there's no… there's no actual process. The thing is, I think that the pre-release was mostly to change the release notes, like, in the past, seems that there was, like, some specific format.
And whenever the release is auto-generated, it basically just grabs the SquashShell commits.
difference between tags and tags. I don't know if we're gonna keep that, or just edit the release notes.
Whenever we have them.
**nacho** 12:58 Yeah, also it was done because, while it's in pre-release, You can update.
the project manually, I mean, if you put the exact number, SPM will download it.
But if it's released… directly… I mean, you can test with a pre-release if you put the number, but the users of the library won't get the latest update automatically.
**Ari Demarco** 13:27 Yeah, at least on SPM. I think in Cobalpots, that's not a thing, unless…
**nacho** 13:32 Oh, okay. Okay.
**Ari Demarco** 13:33 you use Zember, or something like that, like…
**nacho** 13:36 Okay.
**Ari Demarco** 13:37 2.1.1 RC4, or something like that, alpha, beta, whatever.
**nacho** 13:44 Okay. Yeah.
Yeah, that was the reason for pre-releases. It was for doing testing, For testing that the release was good enough, and that everything built with… with… as a user of the library and changing that. That was the reason it was like that, but… Yeah, if… If that's not useful anymore, we can't remove that.
Taint.
Okay, sessions sem… that was a PR?
**Billy Zhou** 14:21 I think I might have the wrong one. I have an open PR to, extend the semantic invention for session events.
**nacho** 14:29 Okay.
**Billy Zhou** 14:30 But it's still in progress, so I don't have an update on that. I can provide the correct link, though. One sec.
**nacho** 14:36 Oh, okay, okay, sorry.
Yeah, as you want. That's still in progress, right? In the semant…
**Billy Zhou** 14:43 Yeah, yeah, I have to address some feedback.
**nacho** 14:48 Okay, yeah.
And yeah, this was this… And also, we have this other, we talked about this other… semantic convention for a screenload upload app launched with Grace last week.
**Billy Zhou** 15:07 Yeah, they're moving forward with app.screen.name, just FYI.
**nacho** 15:13 Okay.
Yeah, great. So, yeah, I can… there are no tasks here.
To handle next meetings, because it was just topics we talked about.
I prefer just to keep the… Those that have tasks to continue handling.
Here. So yeah, for new topics, you have… 2… That was you, also, Billy?
**Billy Zhou** 15:41 Yeah, just a couple of small things regarding log records and, events.
Like, we noticed that, observe Timestamp is missing from log records, if you pull up the first one. I'm not really sure, like, how people were doing, like.
like, ingesting, log records without this time… without this field. So I, set the, default timestamp using the same one, same timestamp as timestamp. It looks like Ari already approved it, thank you. And then the second one is, regarding, Yeah, this is, I've noticed that, like, log records are totally immutable, which is a problem if you want to use, like.
processors to, you know, mutate your log records. So, I added a set attribute method, which should be helpful for us, Like, if you click on the, the first link, like, these ones?
Yeah, that one, Yeah, you can see that, like, you have to rebuild the entire log record currently, which is, obviously, like, a bad experience. So with this, we can just update the field. And then the second thing is that, I also noticed that, like, we don't support a log record as event, in Swift SDK, so, because there's no event name field and, like, the readable log record, struct. So, I added the event name, here as well, but, Because we split the, because we split the repo in two, I also have to do a follow-up PR in the other one to adjust the… the line, at the very bottom of the PR.
**nacho** 17:46 Yeah, this.
**Billy Zhou** 17:48 Yeah, so, yeah, the one we just… yeah, exactly, chair number 12.
**nacho** 17:55 If you click on the… Oh, this is the… this is the pregnant, the other one, yes.
**Billy Zhou** 17:59 Yeah, so I added event name to this, but it's not gonna do anything for us, If you go to the link in the bottom of the PR description.
**nacho** 18:13 Oh, sure.
**Billy Zhou** 18:19 Yeah, so, if you click on the bottom link… yeah, I also have to update the log record adapter for this to actually do anything for us, I think. So… I'll have to… I was actually gonna… wondering, like, do I have to wait for, a release of, of the Slift Core before I'm able to update, the log record adapter? Like, what is our, like, release strategy now?
You know what I mean?
**nacho** 18:48 Yeah, that's a weird question. Yeah, yeah, if… Definitely, these changes that you are doing on the lower quarter, or this quarter, yeah, definitely need that to be supported in… In the API, right?
**Billy Zhou** 19:09 Yeah, it'd be good if we could set event names, since it's.
**nacho** 19:13 Yeah, the idea is that, yeah, I think we can… We can update versions in the core easily.
I mean, there are no dependentials there, but… without breaking changes, that's true. Probably adding a new… Field here will mean that, yeah, we need to update that.
Andrew is also there.
the main, the, the default library. We have, yeah, we, we are just starting with this approach.
Yeah, I think it… really needs… yeah, this is one of the points that comes with.
repositories. We must… Yeah.
**Billy Zhou** 20:02 Okay, so I do have to wait for… Yeah.
Okay.
**nacho** 20:05 Yes, I, I mean… Because your change is…
**Billy Zhou** 20:10 It is.
**nacho** 20:11 It's changing the readable log record, or… So, if we are changing, log regular attribute here.
The, the, the structure of the class, we… Whoever reads it, needs to be updated also.
**Billy Zhou** 20:34 Yes, that's good.
**nacho** 20:36 Because… Yeah, I don't… Definitely, it can be changed.
But the uses of this labor need this updated also.
If they are gonna use any of the new fields.
Or even for some… Uses of the extracts, we could have Yeah, the thing is that this is tracked now.
**Ari Demarco** 21:02 One… one question around… One question around the attributes thing.
Are they able to be changed at that period of time, or they should be… Immutable.
**Billy Zhou** 21:17 Yeah, so I used the spin.
**Ari Demarco** 21:22 On the broom, right?
**Billy Zhou** 21:23 Like, and so, like, Yeah, I didn't really fully understand why the logs were immutable in the first place, because, like, how… what is the point of the processor if, you're unable to, mutate anything?
But I just used the spans as an example, so I saw a span had this, setAtribute method, and, just followed that.
**nacho** 21:50 Yeah, I can imagine that if you have something like a… Recorder that has a set of constant attributes.
If it does… it's selling… The recorder is adding attributes to the events.
That could have also their own errands, so both are added.
But yeah, we… how do you take this pig for that?
I, I, I don't know, I mean, the… The person who… Really knows about the log spec.
Is… is Bryce.
Hmm… He was who made most of the comments on the… Changes here.
And yeah, probably that should be, also, talked with him.
we can ping him. He's on PTO this week, but… We, we can… Ping him to know if that's… Why does… why that was not mutable, to begin with?
**Billy Zhou** 23:05 Okay, yeah, I can ping him when he's back.
**nacho** 23:09 Yeah, and, and, yeah, and review.
And review the spec, so maybe you can… Review this big on, And point to it in your… in your PR, if you find a reference for that?
**Billy Zhou** 23:25 When you say spec, what do you mean?
**nacho** 23:28 the, the, open the limited spec for logs?
**Billy Zhou** 23:32 Yeah, so we already have the, yeah, if you look at the bullet point number 2 in the link there, you can see the, Let's see, the logs, proto, spec, or whatever, it has this field, event name.
**nacho** 23:47 Oh, okay, yeah.
**Billy Zhou** 23:48 Yeah, so…
**nacho** 23:48 But, yeah, I think that Ari was asking about the…
**Billy Zhou** 23:51 attributes.
**nacho** 23:53 Right?
**Billy Zhou** 23:53 Oh, I see.
**Ari Demarco** 23:56 Yeah.
**nacho** 24:01 Yeah, this one, I mean… It definitely… it has been expanded to have a new, entry, that's event name, yeah, so they can be used for events, and the auto client needs these events to… to really be, I mean… For, for, for doing that. But it's about the attributes, being mutable, what, Yeah, I don't know why they were.
not mutable to begin with. I don't know if that's the spec, or it's the implementation that just oversight that.
**Billy Zhou** 24:36 Okay, yeah.
**nacho** 24:37 That was your question, right, Ari?
**Ari Demarco** 24:42 Yeah, exactly, exactly, because I don't really know, and just in case, if you go through the… if you find in the spec that there's no problem on making it mutable, I think we should protect that variable, because you'll be able to set and get from probably different threads.
**nacho** 25:02 Yep.
**Billy Zhou** 25:03 I see, yeah, okay, I can, Yeah, I'll take a look at that then.
Thank you.
**Ari Demarco** 25:13 if you don't find, or something like that, like, just drop a comment on the AutoSwift Slack channel, and maybe we can check it out.
**Billy Zhou** 25:21 Okay, thank you.
I think those are all the issues I wanted to address.
**nacho** 25:33 Okay.
Any other topic?
From anyone?
Do we follow up on the… with the… Open issues, if there are any.
And pull requests in the different repositories.
I will go with that, if anyone.
I think this was an old one… Yeah, it was… yeah, it's about… Yeah, it was about using, raw metrics directly.
Into the… so you can import a bunch of metrics directly into the… into OpenTelemetry instead of Having to create each metric independently, all the values.
That, yeah, that was really useful, but I think that's something… 200?
For the PRs, we have… Yeah, we have… these two… peers that are the ones that Billy, has commented now.
This is a new one, it's… STAD out, exporter, both spec.
Yeah, okay, yeah.
**Ari Demarco** 26:59 I basically…
**nacho** 27:00 Pretty rare.
**Ari Demarco** 27:00 I did this, yeah, yeah, yeah, I just did it, like, 2 hours ago or so.
**nacho** 27:07 Okay.
Yeah, I think, yeah, that that's an easy one to approve, I think, yes.
Adding it to the… Yeah.
Yeah, but the standard output exporter is mainly for debugging.
purposes, I hope.
I hope.
Okay.
Okay, yeah, I wouldn't think that…
**Ari Demarco** 27:33 Nobody complains.
**nacho** 27:35 Yeah.
Yeah, I will update, I will try to approve that.
Yeah, that's easy one.
And let's go with the main repository. Whoa, there are a lot of pull requests here, and several issues. Let's see if we have something new.
The… A low customizing persistent performance preset. Okay.
Okay, yeah, I think this is for the… Yeah, for the saving to this, that it… there were default performance for that.
The persistence exporter is a decorator that you can put on top of any exporter, and it uses diskatching for that.
Which is useful, and it had a pair of, presets that were, by default like that, and it looks like, yeah, it didn't have a way to create a custom one.
Yeah, this is an issue, which probably has another year.
Okay… It makes some sense for me, but I don't know why we would like this to be public.
Redouple from outside?
The rest makes sense. Yeah, it's basically making the constructor public, but why would you want… Would you like to know these values from outside if you create your own?
Does that make sense for anyone?
**Ari Demarco** 29:40 Maybe he hadn't tested, and he's trying to test them.
**nacho** 29:45 Yeah, but I don't think there are disquh.
**Ari Demarco** 29:50 then I don't think it's necessary, unless it's used afterwards for some logic, but I don't think we do.
**nacho** 30:03 Okay, yeah, I'm not logging in, so I cannot answer directly. Now, I will… do that later. I mean, it makes sense to have your own setup, definitely. I don't know why I didn't… why that didn't… why that was not added, to begin with, but yeah, it was some nice reports. Okay… So that was an issue, that was this one.
Any other issues, crossing the yards, or slow, that was… Asking for more information, but… No feedback.
An app process when linking up antenna to testify bits.
Yeah, I need to watch, yeah.
Yeah, Alice has part.
symbolicated graphs. Yeah, that's… That was useful.
Most of the time.
So yeah, waiting for those, so just pull request.
There are men… Oh, please.
Automatic updates… Remove references to batch processor, remove neural context, we have talked about that, and the proof of concepts and the rest of just automatic updates.
So, this is the present one. Remove references to batch processor, Okay… But this, this change.
Which is this… oh!
Okay, so this is for the tests, right?
Collector config planning.
**Vinod Vydier** 32:07 What is the… I'll be just listening.
This is just the export, the configuration for Dockers, right? For the Docker examples.
**nacho** 32:22 Yeah, okay, yeah, that…
**Vinod Vydier** 32:23 And once you remove the batch, is that what is…
**nacho** 32:28 Yeah, I don't know why they have to… I don't know anything about them.
**Vinod Vydier** 32:34 Let's go.
**nacho** 32:34 Oh, dick.
**Vinod Vydier** 32:35 Oh, the collective.
No, what is the… What is a PR about?
**nacho** 32:43 about removing references to batch processor. I… Yeah, this is… Pablo Ballenz, who… Yeah, who's in the collector, and also on the… Member of the, of the… of the committee.
I'm Castle.
Yeah, probably it's something that they are… Changing on the users of the… Yeah, even though… For me, it's good.
**Vinod Vydier** 33:12 Hmm.
**nacho** 33:13 look by this one in detail that I forgot in the issue that is… okay, so let's… For me, it's good.
Thank you.
I don't know anything about the collector. I think that Pablo directly works on the collector also, so if they are doing that in our examples, it's because probably it's out of… Out of, out of the… Outdated, basically.
Okay, so then, there are no more, issues or PRs to preview.
If there are no more topics here, maybe we can end up.
I'm continuing.
Next week?
**Vinod Vydier** 34:01 Okay, sounds good. Okay. Have a good weekend.
**nacho** 34:04 Have a nice weekend. Bye.
**Ari Demarco** 34:05 Bye, everybody. See ya.
**Vinod Vydier** 34:07 Bye.
**Ari Demarco** 34:07 Boom.
**Billy Zhou** 34:09 Thank you.
