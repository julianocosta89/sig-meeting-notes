SIG: eBPF instrumentation
Date: 2025-07-23
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Tyler Yahn** 03:06 Hello!
**Mike Dame** 03:12 Hey!
**Tyler Yahn** 03:15 How are y'all doing?
Yeah. So it looks like, we're 2 min in. We could probably wait just a little bit longer. See if other folks are able to join.
If you have agenda items you want to talk about, please go ahead and add them to the agenda, and if you haven't yet, please add your name to the attendees, and we'll get started here in just a second.
Raphael. Is Nicola able to make today's meeting.
**Rafael Roquetto** 03:57 I think so. He hasn't said anything.
**Tyler Yahn** 03:59 Okay. Alright.
Maybe we'll wait another 30 seconds.
There he is.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 04:11 Hey, folks? Sorry I'm late.
**Tyler Yahn** 04:14 Hey? How's it going.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 04:15 Okay.
**Tyler Yahn** 04:32 Okay. Well.
I guess we can start it off with just a review. I don't know if any people have any other topics that are top of mind that maybe we want to add after the fact. But maybe this will spark some interest. So I just wanted to just follow up and make sure we're keeping on task with addressing our milestone. So maybe we could just take a look at this really quick.
So it looks like we're assigned. And and there's movement on this. There's a lot that's been done. I've included everything that's already been accomplished. So closed issues and closed Prs are included in this milestone. So yeah, quite a considerable amount.
the things that are left. Obviously, we've got this Bayla Docs thing, I think, is kind of the big one I know.
Nicola. I think you spoke for Mario last time, but Mario sounds like you're working on this with Severn as well.
Did I see Mario on.
**MM Mario Macias** 05:31 Yes, yes, we separately did the first.st Pr.
yeah, we need to do many multiple changes to adapt this. But we, we will require shown from from from our grafana is is reworking. So Severn did a a copy of the of the Docs, but we are internally reworking them. So we will prefer 1st to get fixing the Bela docs and then copy them again to to hotel, to to start working from an improved version.
**Tyler Yahn** 06:09 Yeah, okay, that makes sense. Yeah.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 06:14 I pasted the link to the issue in the sorry, the Pr. In the notes.
**Tyler Yahn** 06:19 Oh, okay. Perfect.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 06:41 Yeah. So I mean this, this is a really critical issue. I think, in my opinion, for us to get started because we've already actually added new features in the code base. And we don't have docs.
I realized that some things have gone in and they're not documented because we simply don't have a repo now.
**Tyler Yahn** 07:00 Oh, wow, yeah. So let's yeah, let's make that happen.
Okay, I think that. Also, yeah, let's make sure we track anything that's gonna be missing in the docs as we're adding it, I guess, is probably a good idea, so we can add it at a future time. But yeah, that sounds like, let's get this step done. Is there anything sounds like severance doing great work on this? And obviously, it's it's waiting on internal stuff. Is there anything else that's blocking this that we can change? Or is it just just those 2 things.
**MM Mario Macias** 07:44 Yeah, I don't know.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 07:46 I think that's it.
**Tyler Yahn** 07:47 Okay, cool. Yeah. All right. Sounds good. Then.
okay, and then the last. Well, okay, this is this one. Ensure that there's documentation on how to exclude services. This is something that we need docs 1st to have. So waiting on that that's blocked audit. The Baylor name is another one that Mario. It looked like you had picked up. You've done a lot of great work on this one. So I are we moving forward, or are we close, or where we at on this one.
**MM Mario Macias** 08:16 Yeah. I think today, I just make sure that the Beta name is removed from any metric or configuration option.
There are still some internal, some internal functions or internal symbols that contain Bayla.
But yeah, we are. We are close.
at least at least someone using ob right now shouldn't see any Bela attribute nor Bella prefixent metrics.
Now, it's just for development. There are some symbols for calling. But yeah, it's not now. We can just rename them.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 09:02 I had a question. I don't know if you want to do this or just fix them, but it might be a good topic for good 1st issues to be posted if you have like, if it's just source code change, if somebody's just need to tidy up and rename a function, maybe we can just open issues.
rename this rename that, tag them as good 1st issue, and allow 1st time contributors to the project, too.
Jump in and do this, but it's also.
**MM Mario Macias** 09:27 I'm saying, Yeah.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 09:28 Yeah, you know, spark, more contributions.
**Tyler Yahn** 09:33 Yeah, that's a great idea, if you can. It takes a little bit of time to get it set up. But yeah, if you can do that. I think that's great. This good 1st issue is like tracked by external websites that are looking to try to help developers.
you know, get their 1st contribution to open source, let alone like find new projects. So yeah, I think that's a great idea. If you can. If you find something, yeah, create. Creating an issue is a great way. You don't necessarily have to do the work. Yeah. So that's great. Great idea.
Okay, well, I think if that's the case. I think we are looking pretty good. We're just waiting on docs at this point for this next release, I guess.
Probably need to get some releasing scripts in here.
So maybe that's on me. Actually, we need to probably add some sort of releasing steps. I don't know if there are any right now.
**MM Mario Macias** 10:28 We have the docker, the docker release.
Yeah, we have that for for the main branch. So we should replicate them for for actual releases.
We should also, if we want to release a binary.
we should retake those signet binary scripts, as someone mentioned at the at the very beginning.
Otherwise we can. We can polish demo signet. I don't know what you prefer.
The oh, sorry.
**Tyler Yahn** 11:04 Go ahead. No, I was just going to say, the binary may be a little bit more challenging than we want to do here. It may just be that we could. We could make a release with a tag, and then it can just be like a go release as well. It's kind of what we've done in the past to signify that although we have started verifying and signing our like, when you do a release, it'll create a tarball. Of all the code we have sort of verifying that in the hotel Repo. I feel like it's not much more to try to like. Get a binary built and then included in that release. But.
**MM Mario Macias** 11:41 Hmm.
**Tyler Yahn** 11:41 But maybe we keep that for a a v, 0, 2 release and and work.
Okay, just yeah.
**MM Mario Macias** 11:49 Okay.
**Tyler Yahn** 11:49 Unless unless you think it's crucial that we have a binary in this release.
**MM Mario Macias** 11:53 To be honest if if I have to take the Bella users as a as a reference.
most of them use kubernetes, so, having the container is is fine. We should maybe add some scripts to release the helm chart.
**Tyler Yahn** 12:11 Okay?
yeah. I agree like anything that we. So so it sounds like, what we need for this release is gonna be the helm track needs to get really. So does that just get uploaded into a centralized like vendor or cache.
**Nimrod Avni** 12:29 The helmshot. I opened an issue a while back and I opened a pr for open telemetry hand charts, and it got like kinda stuck. It's not like it's in the different level, but I think I know we might want to like push more on that if we want to get it merged.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 12:53 Have a link to the issue. And maybe there really is.
**Nimrod Avni** 12:56 I think the issue. The issue is still open. On, on.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 12:58 Oh no!
**Nimrod Avni** 12:59 Ob, I think, and it like kind of links to.
**Tyler Yahn** 13:09 Publish home chart. Maybe.
**Nimrod Avni** 13:11 Yeah, I think I think I typed something, though maybe no
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 13:17 Might be another one. I think I saw it from you. I just don't remember where.
**Nimrod Avni** 13:24 Open open, and then.
**Tyler Yahn** 13:31 Nimrod, what's your username.
**Nimrod Avni** 13:37 7 8. But the way I think I'll yeah, it's I'll send it in in the chat here.
**Tyler Yahn** 13:44 Okay.
**Nimrod Avni** 13:46 So this is the Pr.
And I think so. I just commented because I thought it got stuck So maybe I can start addressing those comments. I didn't see it.
**Tyler Yahn** 14:02 Oh, open. Oh, that's weird. Okay.
**Nimrod Avni** 14:04 Oh, it's the last Pr. I think I didn't send the the actual Pr. The the full request.
Yes, I got stuck for a while, and I think now I think I see tyler gave some comments, and I I'll
**Tyler Yahn** 14:29 Hmm, okay.
**Nimrod Avni** 14:30 I'll just fix whatever he said or yeah, I didn't see it.
**Tyler Yahn** 14:40 Okay, yeah. So this looks like it's going to get included. So do you know how this looks like when we publish like, is it just like this gets synced at that point? Or is it just? Is there really anything we need to do during that release?
**Nimrod Avni** 14:54 I think I think like the helm chart, like right now, the like. The helm chart points to the I think it's like the latest image of Ob.
And so it's like, every time someone will install it. It will just install the latest version unless we want to like like when we have like fixed releases of like 1 point oh, 2 point. Oh, we can like PIN it. And then, only like, make sure we update this on, on releases.
I think it is somewhere in the.
**MM Mario Macias** 15:27 Yeah, seems, weird.
**Nimrod Avni** 15:28 Think it's a value.
**MM Mario Macias** 15:38 Okay, yeah, it should be latest. But I will actually PIN it to given numbers just thinking on. Since we are still on early stages, we might add, breaking changes in the configuration.
so it might happen that if they just have the latest they might get their installations broken. If if we had some breaking change until we release a 1 to 0.
**Tyler Yahn** 16:08 That's a good point Mario. Cause like Maine is is literally Maine, like this is just bleeding edge head of the yeah. Okay.
**MM Mario Macias** 16:15 And.
**Nimrod Avni** 16:16 So I mean.
**Tyler Yahn** 16:17 Like nothing to to like that spend?
Yeah, I could. Yeah.
**Nimrod Avni** 16:20 Like commit hash, or something, just the latest.
**Tyler Yahn** 16:23 That makes sense. I think I think this this could probably get merged the way it is. But then, when we do the release, we definitely want to make sure there's an update to to PIN is what Mario is saying. Yeah, I think that makes a lot of sense.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 16:34 Yeah.
**MM Mario Macias** 16:35 For for now I sorry, Nicola. No, I was the I was about to say that, for now is the only tag we have. So it it must be in main if we wanted to work. Yeah.
sorry, Nicola.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 16:46 No, that's okay, like I said, it served as well to kind of have it pinned to a certain version and have the chart also update the version every time. So people when they hit an issue with a new release, something's not working. They can revert back with the help command to a different version of the Helm chart, which gives them a different version of ob technically.
**Tyler Yahn** 17:07 Because.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 17:08 They're controlling everything with the helm chart command, so they can just say helm chart upgrade. And then that would actually give them the latest, but then they run into something I don't know like could be anything really. And then it's easy for them to just go change the helm version that brings a different underlying version.
So we have these 2 values. We bump every time.
I think it's in the chart something.
If you go, there should be something. Yeah, chart. Yaml, that's 2 versions in there. So version one. Oh.
should be in here. But then this version you bump to say you have a new chart.
And then typically that points to a new release of the underlying products. So then you can control the charge version that gives you certain versions.
**Mattia Meleleo** 18:03 We. We also need to bump the images tag right? Because if we want to release to the same step.
and we can do that easily if it's in the same repo. But if it's in another repo, I think we have to open a pr via github actions, or something like that.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 18:20 Yeah, or just once we make a release, we make a Pr to update the helm chart. And you know the release. It's actually not a bad idea. Anyways, like you 1st release the release of Ob and people that are pulling it through. Docker. Maybe experience it 1st while you're working on health upgrade, having them kind of delayed by some amount of time, is not the end of the world, because then you get some blast radius of people pull pulling in latest.
and then they may open issues and sort of before you say, here's a new chart, then break more people.
If anything goes wrong.
**Tyler Yahn** 19:22 Okay, that sounds good. It sounds like we need some docs at this point.
Is, I think, kind of going to be important for this this release, because well, for one, we want to be all on the same page, if we, you know, because, like somebody's gonna have to actually do this. So like, unless we build automation, I guess. And even then, like, you need to click on some buttons. But we need, we need to kind of like, make sure this is documented. So maybe I'll I'll take an action item to open an issue to track like adding or releasing documentation, and then we'll we'll add all the like. It definitely sounds like we need some scripts here. The helm chart can be more of a manual process to start or an action.
for this 1st release, probably not building things to. To do it, I think, is probably the best and just doing it by hand, just because then we'll know, I think, a little bit more after the first.st What we what we need.
The Go tag stuff is pretty straightforward. I think there is a there's, there's multiple modules here. Actually. So we're probably going to want to use like the go tooling that we have for all the other repos using multimod. So I can definitely help setting that up.
The helm chart seems pretty straightforward. We're going to be blocked essentially on that Pr that we were just looking at. Actually.
yeah, until we can.
I think we need to get this merged right before we can do a release.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 20:51 Yeah, I mean, it's okay for the 1st one. Since we're not releasing anything to be pointing to Main. I don't think it's a big issue. I don't think we have to be concerned, but once we release a version with 0 point 1 0, I think it will be good to. Then, if this is merged, the chart, we put an update to kind of PIN it to that version officially, and then maybe more broadly, announce it.
**MM Mario Macias** 21:14 Hmm.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 21:15 But the majority of work here. I don't think it should be blocked on any release, I think.
Charts.
**Tyler Yahn** 21:21 Okay, I don't.
Actually, I don't even know if these these guys have like a Sig meeting.
**Nimrod Avni** 21:30 That's a good question.
I haven't. I have no idea.
**Tyler Yahn** 21:33 I mean, yeah, I definitely looks like the collector, I think, is one of the bigger.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 21:38 Hmm.
**Tyler Yahn** 21:42 Huh!
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 21:42 Does it say anything in the repo further down below.
**Tyler Yahn** 21:45 For their their meetings. No, I mean.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 21:48 They do have maintainers and approvers, so.
**Tyler Yahn** 21:51 Yeah, yeah, yeah, I can. I can ping Dimitri as well.
**Stephen Lang** 21:57 Collector. Sig itself is up next at the top of the hour.
**Tyler Yahn** 22:01 Yeah, that's what I'm wondering. I'm wondering if this is where, like, cause like, I know, there's like a lot of stuff that's rolled into the Go Sig as well. That isn't officially like like the Vanity URL. Stuff.
I wonder if this is this is a part of that where you could just talk to them about this, because, like, I would like to know, like the rollout process if we roll something out and then like, obviously like, we have to get a pr updated here. But then, like, what's the release cycle here?
because it probably needs to get coordinated.
Okay, I think more questions.
**Stephen Lang** 22:33 I can ask if you want, because I was going to go to that for another question, anyway.
**Tyler Yahn** 22:37 Oh, that'd be great. Yeah, Steven, if if you can. I mean, yeah. Or just find out the the people who maintain this are going to be there, so they'll tell you if there is another place to ask. But yeah, that'd be great if you could ask that.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 22:50 Yeah, there is an auto dash helm channel a channel on on the slack. Yeah, for the slack. Yeah.
**Nimrod Avni** 23:00 By the way, I just saw one of the comments he left me is saying that maybe the the name is too long of open territory. So maybe, do we want like? Have it as old or.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 23:15 Obi, yeah.
**Tyler Yahn** 23:16 Yeah, I think we already got a great alternative. There.
**Nimrod Avni** 23:19 Yeah, like, if it's if I'll invite him, unwrite him for that.
**Tyler Yahn** 23:25 Yeah, I'll make a.
**Nimrod Avni** 23:31 Nice, so I don't even need to change the prefix, because it's already prefixed with Obi.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 23:37 Yeah, right.
Very cool.
**Tyler Yahn** 23:42 Yeah. And no matter if you have any other issues that you need some sort of feedback on, I think maybe also just posting like those questions in slack, or or we can. We can look at it this as well, or CC Us. In this Pr, and we can. We can take a look.
**Nimrod Avni** 23:56 Yeah, sure.
**Tyler Yahn** 23:57 Obviously Mario already has, so he's he's on it. He's everywhere.
**Nimrod Avni** 24:03 Good.
**Tyler Yahn** 24:04 Okay? All right. So a little more to do. We're definitely waiting on docs, I think, is the last thing. And then just getting this releasing process kind of documented. So yeah.
cool. We're we're getting close.
Speaking of that. So what are we working on? So looking over the open pull request. Maybe we can just go through this. The ad process minimum age to filter out short lived processes. This one's been a while. I don't think there's any update, Nicola. Is there anything we want to say on this one.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 24:33 Got distracted for a second. Which 1? 0, yeah, I still on the sorry.
**Tyler Yahn** 24:38 Yeah, no, no worries.
Okay. Similarly, this update the Kubernetes package one. I think this again also just needs some eyes on it, because we're we're kind of.
we're breaking. We have to go back and look at what's changed in this process, because something is not working right now. So yeah, this is just waiting on some sort of feedback. Yeah.
or not. Feedback investigation, I think, is a better word. Yeah.
Yeah. Also similar. Here. One of the things that this is highlighting is that this is trying to bump our men go version to try to get a lot of other updates. And Nicole pointed out that maybe we need to update the dependabot security audit to ignore this one.
So I think it needs, we need to, I think, look into this one as well. So this just got some follow up actions on it.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 25:34 Yeah, I don't know like, so we I've done this before. I just don't remember how it was somewhere in Github that I messed with but maybe I don't have enough permissions in this repo to change this kind of rules.
**Tyler Yahn** 25:48 You probably don't. That's a good point.
I think. But if you, if you know like, if you can look in like another repo that you have done this. You can create an issue in the community Repo, to get this done, and they'll either use some sort of terraforming script, or they'll they'll give you permission to go. Do it, or they'll they'll do it themselves. But yeah, it's just a community issue.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 26:12 Okay.
**Tyler Yahn** 26:12 Repository. Maintenance. Yeah.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 26:14 Yeah, you can put me on the
**Tyler Yahn** 26:17 Assignee.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 26:18 Yeah, Signee, I will take care of this. Yeah, I did it for Bela. We had the same issue. Dependabot was finding all the security concerns.
Oh, yeah.
**Tyler Yahn** 26:32 Okay.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 26:34 There's similar things happen in, say, the the offsets, Jen Repos. So if you take, for example, the support we have, or I think, Kafka we support Sarama, which changed ownership from Ibm to shopify, or vice versa. I forget.
**Tyler Yahn** 26:54 Yeah.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 26:55 And then we wanted to support the old one. But then those old packages, whichever company was first, st they don't maintain it anymore. So it's full of security things.
So offsets is also one directory where we sort of don't wanna look into for the dependable.
It's not product. It's just there to give us ability to find offices for old versions of packages that people may still be using.
So we did exclusion on both the test folder and the offsets folder.
**Tyler Yahn** 27:29 That makes sense.
Let's yeah. Hmm, that's definitely kind of weird, actually.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 27:36 Because you can't find offsets for an old package if it keeps being updated right? So and so, this library is not even updated anymore.
**Tyler Yahn** 27:47 Hmm, right? Right?
That makes sense.
Okay, I think what we have right now, it's just the idea to make an exclusion. This makes sense. Given, this isn't.
This is updating something that is not consumable by our end users. We're not publishing this. So yeah, I think that's that's fair.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 28:09 So an alternative, I'm not sure I like this alternative because we're gonna lose the source. But technically we could remove this from a repo and build an image that we publish. That's just gonna be one that we it was not going to be in the scores.
I mean. And then the question is, if we ever need to update it, how do we do that?
**Tyler Yahn** 28:30 Yeah, yeah, that's yeah, right.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 28:34 Or maybe could be a community project that we just point to that is on this old version. And it's not in the repo anymore.
and then we build off the community repo that is not scanned. And it's just for testing purposes. Really.
**Tyler Yahn** 28:53 Yeah. So I'm maybe we can take a look a closer look at this. So integration component.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 29:01 Yeah, it's integration components.
And so technically, this is a clone of the test server. It's a go application. And it's pinned to a bunch of old packages, essentially.
**Tyler Yahn** 29:14 Yeah.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 29:15 And the reason it's here is because we want to make sure that we say, though you know we support 1 17 go.
We want to make sure with that still holds true.
As we go and make changes to the Go Ebpf code we may inadvertently break something, and we're not aware.
And then somebody using an old version which has happened before, which is why this was added. You know, this wasn't added just as a or a fun project.
We did break during development.
something related to a very old gold version. So then we added this and said, This is the oldest one we support. So this runs, you know, has Grpc in it, has all these things in it, gorilla mukes, whatever.
And then we wanted to make sure that you know all those old packages still working exactly as the new ones.
**Tyler Yahn** 30:12 Yeah, I mean, this seems reasonable.
I don't. Yeah.
I'm trying to think like, I mean, the only other option I could think of is like you kind of like, templatize this out. So instead of being a go MoD, it's like a text file. And then.
you know.
and some sort of like testing script. You take that and change it. So essentially, you're just skipping any sort of like renovate bot. You're skipping anything problem is is like, I can't go in here, and I can't run, go.
go, test, or something like that, like, I can't use the go tooling anymore. If that's the case.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 30:44 That's right. Yeah. So you have to build it with a docker file and.
**Tyler Yahn** 30:48 Yeah, yeah, and actually, these dependencies, then just get moved up to whatever the module contains is outside it. So yeah, there's there's a lot of problems with trying to do something like that.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 30:59 Yeah.
so it was. It was done for that reason. But we may have actually dependable, as may have updated some of these packages already. So.
**Tyler Yahn** 31:09 Yeah, that's I was. I was wondering about that as well.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 31:14 Look at the history of the file. I wonder if it's moved up the Grpcs.
**Tyler Yahn** 31:18 Yes.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 31:19 Somehow I remember it was on an older version. But
**Tyler Yahn** 31:23 Maybe not.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 31:24 Or maybe not. Okay.
**Tyler Yahn** 31:26 Yeah, I mean, if not, we should probably try to make sure we have a ignore on that in her renovate config.
Oh, actually, I think we could probably just look at the issue.
Wow, okay.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 31:53 Yeah.
**Tyler Yahn** 31:54 So see that shopify Sarama, I think shopify started this project.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 31:59 And then they they abandoned it. But then, somehow, Ibm took it over.
And then they continued, Yeah, now.
I mean, maybe it's not important to keep this shop professor on anymore and tell people you need to go on the new version.
However, I, when I grabbed in Github for references to shop. It does come up quite a bit, so.
**Tyler Yahn** 32:23 Yeah, I don't think it's not non 0 at this point. Yeah, exactly.
yeah. I think there's there's I think you can. You can deal with. This offsets a little bit differently like in in the auto insertation, like, what we do is we actually use like these templates to auto, generate a custom.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 32:40 Oh, okay.
**Tyler Yahn** 32:41 App during during whatever offset run is happening.
And so you don't have to actually have a full working example. It can just be auto generated as the code goes through. So.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 32:52 Okay.
**Tyler Yahn** 32:53 But that's that's not really that important. I think right now we can. We can look into that in the future. I think, what we have right now works. I did notice that this is not picking up that tools repo right now, or that tools directory. So that's interesting.
I wonder why, that's the case. I think this might just be. I think we've configured it to to do that.
Guess we can take a look.
Yeah, this doesn't I, yeah, I didn't see anything here. This doesn't look like it's doing anything, really. Yeah, I don't see another run of it. Okay? So I don't know why it's skipping this this test directory, but it seems like it's missing that module, so I don't, which is good. We wanted to do that, but I don't know why it's doing that. But okay, at least, it's not updating the things we don't want to update. So I think that's that's good. But yeah, we'll just try to get this excluded from Denapat to Benapot. Who is finding this. So yeah.
okay, thanks, Nicholas. Sorry about the tension. Everyone next up initialize host info metric on 1st span. This is a draft. I don't know if it's ready to actually get viewed.
I don't know if the author's on here as well.
Looks like there's already been some review on this. So yeah, oh, it's just yesterday. This is open. So yeah, so it looks like it's work in progress.
**MM Mario Macias** 34:15 Yes, it's I. I've reviewed it. It's it's fine. But I I've asked it for some extra testing for the behavior.
just to make sure we don't break it.
**Tyler Yahn** 34:26 Yeah, that's always great. Yeah, okay.
perfect. It looks like they're responsive, too. So yeah, we'll keep an eye on that.
Don't delete target info on expiry if the service is still instrumented. I think this is a Nicola. Yeah, this is the one where this 5 min timeout was causing things to get dropped. If I'm not mistaken, Nicola, I don't know if you want to say anything more about this.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 34:50 Yeah, it was just this was an issue. Open a while back at the Baylor repo that people were complaining about our expiry, which gives them gaps in their metrics. So essentially they will be watching a service that maybe kicks off a job every hour like some sort of like a I don't know, like a backdrop thing that checks something every hour, and then what they'll see is that we we would expire this service so they'll have like an empty slot. It's almost like the service is not there.
Because the metrics expire after 5 min. So we kick off this whole exporter, and for that particular service, and everything just disappears.
So what we wanted to show is that, yeah, there's no activity. But the service is still there. So at least there's there's some level of certainty that it's not that the service died, or I don't know So we changed a little while back to do the target info management lifecycle based on where the process is detected by Ob, and then when the process disappears or it dies or restarts, or whatever we clean up that information.
But then for the auto metrics exporter, I found this issue.
that we. So I remember why I wrote the code in there where it was removing the target info is because.
I had encountered this issue while 1st implementing this support was because we would see the process lifecycle management that the process is going away, and we would delete the target info. However, if you had buffered any metrics in your exporter, they will still make it on the other side like this. Certainly imagine the service was just regularly producing telemetry, and it certainly dies.
We would detect sometimes faster than the death of service. Then it, the exporter, will drain all the and serialize all the data. So technically you would delete the target info. But something recreates it right away.
So to fix that, I added the deletion, also under the punching of the of the reporter from the cache. So we have this lru cache, and as a porter as it as you know, this time's out, so the service is not seen for 5 min we would delete.
But then I realized by looking at this code recently reviewing the code, actually, that Jorge opened.
I found out. Oh, well, right now we delete this every time services will expire.
So let's say you have a service. It's live. It generated a bunch of telemetry, but then it went silent. Nobody's sending traffic to it.
In 5 min we will kick this off from the Reporter Pool.
and what this code will do is actually delete the target info.
It's not the end of the world, because as soon as the service starts generating data again, it will get back in, it will get recreated because targeting for is resource metric that gets created out of the regular metrics.
However, there will be a gap again.
So what I did is technically our delete hook, which is further down in the source file. I pointed at the Mario's comment, a link to the source.
Eventually this.
This code will delete the target info, and then it will remove the service from the internal tracking from this bit tracker that tracks how many processes ids have been associated with a service when the last process, Id goes away for a given service, so there's no more instances of the service. We completely remove it from the tracker.
So at that point we know that the service is no longer tracked by Ob.
So in that case, when this metric exporter gets expunged from the cache.
then we say, Oh, if you're not tracked already, then yes, go and delete the target info. But unless the service is.
it's not completely gone, then we do not want to delete the target info.
Does it make sense.
**MM Mario Macias** 38:58 Yeah, yeah, definitely
**Tyler Yahn** 39:02 Yeah, yeah.
**MM Mario Macias** 39:03 Actually didn't remember that part of the call. Yeah.
**Tyler Yahn** 39:12 Yeah. Looks good to me, too.
I think you got 2 reviews on this. If anyone else is looking to review it, I think, you're welcome to. I don't think anybody needs to. But yeah, it looks like it's ready to go.
I'm gonna resolve this as well.
I can merge it here. Actually, if.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 39:33 Sure.
**Tyler Yahn** 39:34 Once, twice. Anybody else want to review this, if not. Okay.
Awesome. Oh, okay.
And then last up SQL, support. Mysql, prepared statements, split and integration tests into Mysql and Postgres tests. Let's see.
**Mattia Meleleo** 39:56 Yeah, this is the last pr of the of the previous one that I split into multiple prs, this is just doing some refactoring of the user space and the adding some tests.
**Tyler Yahn** 40:11 Nice. Okay? Yeah. All right. Looks like Mario's already reviewed Raphael as well. So we're just waiting on some 13 min ago. So a little multitasking going on, which is great. Yeah.
**Rafael Roquetto** 40:26 Maybe morning man.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 40:28 Yeah.
**Tyler Yahn** 40:29 All right.
Well, cool, all right. So it looks like just a few more rounds of feedback. And then, yeah, thanks. Thanks for putting this up. 14. Yeah, we'll make it happen.
Okay, all right. That's the end of the agenda I put together. I can stop sharing here.
Oh, man.
Right. Any other topics. People want to talk about any things that got sparked while we were discussing things or new ideas.
**Nimrod Avni** 41:04 I can.
**Mattia Meleleo** 41:05 Just, I'm just go ahead, Nihmad. Yours is more important.
**Nimrod Avni** 41:10 I don't know if it's more important. But we.
by the way, I it's kind of related. I don't know me, and Mattel started working on. I think something could like, regardless of what specifically, specifically what we didn't call a lot. It's like trying to instrument, you know, the does the open till empty demo set of applications.
And we're trying to like basically instrument it like the whole thing with Obi. We also added, like a couple of variation to like. Add, like a couple more databases, because we wanted to some more stuff like the show, the full capabilities of of Obi and we also wanted to do it with like distributed tracers and on the cool stuff that we support. And we're like, well, kind of deploying it and kind of seeing exactly. Maybe we have some stuff that are misconfigured or stuff that are like not. We didn't configure correctly, like the the weirdest thing, the weirdest issue that I encounter encountered like 15 min before. This call is like that pods that are like being restarted like I can see telemetry on like pods. And then, when I restart them, and a new pod appears suddenly like no telemetry comes from that service, so I'm not sure if it's something that anyone in like I can share, like the I can probably do it on offline. We don't need to like
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 42:29 Yes, please. Logs, logs, please.
**Nimrod Avni** 42:32 Yeah, I can do logs and like config and and all that stuff. But and I just thought, if anyone like encounter the similar issue, but if not.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 42:39 As well like I've been doing the exact same thing as you are. I did encounter. I suspect that maybe it's this issue that recently fixed where we were kind of like depending on the sequence. Things start in.
Removed, the pod may not be detected. This was the reason why Kubernetes tests kept from failing the the case test, you know, in the Ci constantly failed. So this was resolved like yesterday. Maybe I merged, or the day before.
**MM Mario Macias** 43:08 Maybe try to.
**Nimrod Avni** 43:11 See if the image that I pull is the latest, and maybe that will solve. But interesting.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 43:16 Yeah. And yeah, so this is probably like, discovery did not catch the service. Usually, if you have debug logs that would really help, because it would go through the motions. And it'll say, Oh, I'm doing this, I'm doing that, and they will be it will not find a service. Maybe I noticed something like that myself, like product catalog. The service was running fine, and then all of a sudden disappeared. I looked at it, and it was restarted. We didn't catch it, and then I manually restarted. I nuked the pod, came back, and then it got it. So I think it's something random that might be related to that. But I didn't have the fixed merge in. So I'm going to test again with the fixed merged in. I'll put a new image.
**Nimrod Avni** 43:58 I think I also noticed that for some reason it like he said, the product catalog for me, it did work, but maybe it's because it's somehow related to like that. All the instrumentation stuff come from like go you probes instead of.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 44:14 Yeah.
**Nimrod Avni** 44:15 Like the the normal.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 44:18 Perhaps.
**Nimrod Avni** 44:18 This stuff, because when I started like others like Python ruby services, they stopped working. But they go on.
Okay.
But I don't know. Maybe I'll I'll try to.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 44:26 Yeah, I think it's totally random. Yeah. So debug logs, or even if you have like, this, info logs may help. But debug logs will definitely have everything related to you. Don't have to turn on the Ebpf logs. Just the debug log should be sufficient. I'm guessing we're not finding the services somehow.
**Nimrod Avni** 44:45 Yeah, I turned them on, and I saw some like messages from the Kubernetes cache like for the added for deleted.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 44:52 Yeah, yeah, yeah. So then, you have to look through like when we did it. So because there's this whole notion of you, we discover the process. Id right, that we want to instrument. But the process id has no metadata. There's no Kubernetes data for it. So it's kind of like naked, almost like empty. There's no data. We can identify it. Then the pod add information, and they have this container. Id.
So then we try to match the container id of the process with the container id from the pod, and once we match them, we say, Oh, now we generate new event. Tell the update the information so that the process discovery can catch it again.
And so I recently discovered a bug in there. If the things were in the wrong order.
we would register the process information, then delete it. Then the pod comes in, and then, when the pod information comes in the process, information is gone.
**Nimrod Avni** 45:50 So it usually happens in the container itself.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 45:54 Had a launcher of some kind, you know, like Npm start.
So then the Npm original process kicks off the node process. But then the Npm. Process dies, but they're both within the same container.
So then it depends in which order we see them. There was a bug just 2 days ago that would text was gone, merged.
Maybe it was yesterday. I think it was
**Tyler Yahn** 46:17 Yeah, I think it was yesterday. Yeah.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 46:19 Yeah, yesterday, though.
**Nimrod Avni** 46:20 We give it a try and make sure I'm on the latest version. And and if I'll still have some issues, I'll try to send, like the config and the bug logs, and all that.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 46:30 Yeah. So I also should say that for the distributed tracing to work correctly in a hotel demo, we still have to do the work to make it work with Grpc. Because a lot of the services use Grpc for traffic.
**Nimrod Avni** 46:42 Yeah, so that's also another like, yeah. Glpc, I know we still have some issues there. And with, like, I know that with Htp it it should work, but we also encountered. We encountered some weird issues that we had like kind of the the 2 traces. There was like a trace that it was like in the same. We have like 2 services, and one of them is in the same trace. But it's not like the correlated to the parent, which is like, maybe so we thought there was like a.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 47:12 Yes.
**Nimrod Avni** 47:12 In the middle of something that we didn't.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 47:15 Okay?
So so that will happen in an hotel demo in the hotel demo, because, the applications themselves also attempt to do context propagation.
so Obi is doing it for them, but they're internally also doing it.
So sometimes we don't see the internal because they're hotel applications right? So even if you cut off the the telemetry sending, they're still attempting to propagate the contacts themselves.
**Nimrod Avni** 47:44 So saying, maybe if we like, like, I, theoretically, if you like, remove all the other libraries from everywhere, might work better.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 47:51 Might work better. But I think our goal should be to make it work with them. Right?
Yeah.
maybe we can extract some of this traffic as it goes out, and update our internal representation of the spans. To say this was done by the application, don't do it yourself. Go pick that up. You know things like that. I think it's possible to improve it.
because maybe customers will be doing this. They will be using some hotel libraries to do internal propagation. Maybe we don't know right, or maybe they do that partially for some part of the code, but not for the other, and it would be nice if this all worked. It might be challenging, but I think it's it's doable.
I'll tell you so. There! There was one particular issue that we worked on before this was donated to Ob. It's in this ob was donated. So there it's in the source right now. But.
we encountered an issue with Istio, which is why we might have broken this so if you're on Istio service, mesh, what I saw them doing is that if you do not specifically tell them to use trace parent as a field, they track.
What they do is they take the incoming header, and they use it on the outgoing as well. So what ends up happening is that they take their trace context, which was now fabricated by Ob because it started propagating. Then they just append it over and over again. So it becomes this massive string.
So if we relied on what's in the headers from the application, we ended up pulling the wrong trace. Information for Istio and a lot of users use this deal. So I think we made some decisions to there to say no ignore it.
you know. Use the one from ob but we.
**Nimrod Avni** 49:41 Never like rely on the on the like. The header, like the experiment head. We don't rely on that. It's only it's only the ob level now.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 49:51 That's right. So I we used to rely on the. So we used to say, if you have a client call, and that actually has transparent in the headers used as the gospel. That is, yeah, there's yeah. That is your final truth. But it still broke that completely, and we had customers complaining a lot of using Istio, and then it was like and real close.
**Nimrod Avni** 50:12 Not configurable or something. It's just that we decided to.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 50:15 Yeah, configurable. But we could. We can make a configuration option to say No, no, prefer the client one, and then you can extract the information correctly.
**Nimrod Avni** 50:26 Yeah, I don't know, because the I'm guessing that maybe some of the docs were like, I don't know outdated because I didn't really know how the All network level propagation work. But that's really.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 50:38 We can.
**Nimrod Avni** 50:38 Come from the source like that, you know.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 50:40 Yeah, if you'd like, we can do next time or offline essentially on a session, we can kind of walk through the code and kind of explain how this works. We could definitely use help here to make this better. I I'll be really honest. It's yeah. I'm happy to to walk through the code and explain how this works and why certain decisions will make certain way.
But yeah, it still broke a lot of things.
Oh.
but maybe there's a way to detect it, you know. Maybe there's a way to detect that this is kind of done, and then only reject it in those cases but in the other cases use the the outgoing Http client context as the as the one that we use.
**Nimrod Avni** 51:23 Interesting. Okay.
**Tyler Yahn** 51:24 I think, Nicola, at your point of walking through the code sounds like a great idea. If if you're up for it, we could probably do that next week. And then, Nimrod, I would also say, like.
if you want to just do a demo of what you've gotten so far on being able to like, you know, to show all the all the warts and everything of of instrumenting the demo app. I think it'd be a great thing for just a part of this meeting as well if we wanted to do that next week. Yeah. So if if you guys feel up for it, can you add just a blurb that you plan to do that in the the next meeting notes at the top of the agenda. That'd be great, because I'd be interested in seeing both of those. If you're up for it.
**Nimrod Avni** 52:07 Cool. Yeah, like we, we still have, like a couple of minor tweaks to fix that hopefully will be done by next week.
**Tyler Yahn** 52:14 Yeah, I mean, I think getting eyes on it, even if it's like like, it sounds like you're getting data, right? So that's that's a very interesting thing to see. So I think that like, yeah, even even if you're just maybe misconfigured. Or there's smaller things. But it may also be like, like you found all these other issues that you know we're looking at. So I think, to share sharing. That'd be great. I'd love to see it.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 52:35 Yeah, I can share as well like I can show you my screen of what I'm doing right now, if it's similar, if it helps of.
**Tyler Yahn** 52:45 Yeah, I I. All of that stuff sounds like great topics and agendas. Obviously, we got like, 9 min left so maybe not today. But yeah, if you, whatever you guys are working on, it's like, I think that'd be great. If we could. If we get a little more of this kind of stuff. I think it'd be awesome.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 53:01 Yeah, the ultimate is a great test. I have to say, like, there's a lot. I'm really excited. Because somebody, actually, recently, I opened an issue, and they fixed it right away. They added sequel in the mix. Now it's supposed to be official. I don't know if there's a new release. But somebody, added Postgres, one of the services now talking to Postgres, I believe so. That was welcome to see, because I think it's very representative of people do on databases, customers, and it was like, we need more databases. What Nimrod said. You need more databases in the demo.
**Nimrod Avni** 53:32 Yeah, I think we we added, like it was like some posters, Mongo, this and some stuff.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 53:40 Cool.
**Nimrod Avni** 53:41 Like, especially if we, as we add more support for other types of instrumentations which are popular, it's gonna be okay.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 53:49 Yeah, great work.
**Tyler Yahn** 53:51 Yeah. Awesome. Really excited to see that cool. All right. Any other topics before we close it out here.
**Mattia Meleleo** 53:59 Mattia, you wanted to say something?
Yeah, just a short question. So last time did we reach an agreement to remove the vendor folder from for go.
We need some action item or something like that.
**Tyler Yahn** 54:14 Yeah, I brought it up.
so the only question is is, if we start vendoring in things back from open telemetry, the auto instrumentation project, for go, it sounds like we may need that vendor folder as well.
I don't think you can run in a partial mode where you have certain things we could do a sub module approach where we are like sub moduling the auto interpretation locally, I think that that could work.
That was the only reason I hesitated on on removing it. But we can, I mean, maybe it's just opening an issue. To track the discussion, at least, is probably a good idea to your point, Mattia.
**Mattia Meleleo** 54:54 Okay.
**Tyler Yahn** 54:57 Yeah, I think that that's that's a good move. But I also think that like, if we're immediately going to add it back in, because we have to like vendor and things for this probe. Then it's not really a good like, it's not going to work. So yeah.
but yeah, I'll I'll take an action item on that. Open an issue to at least document it.
Okay.
Then I think with that I can write that later. Any other questions, topics?
If not, we can end it here. Thanks everyone for joining, appreciate the contributions, all the work so definitely valued.
I will see you all in a week's time, or Asynchly bye.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 55:48 Bye.
