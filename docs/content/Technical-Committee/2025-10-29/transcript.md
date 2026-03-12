SIG: Technical Committee
Date: 2025-10-29
Duration: 27 minutes
============================================================

## Zoom Recording Transcript

**Tigran Najaryan** 00:41 Hey, guys.
**Reiley Yang** 00:43 Hey, Steven. Take care.
**David Ashpole (dashpole)** 00:45 Hey.
**Tigran Najaryan** 03:18 I just checked the inboxes. There is, there's the issue that we replied to two weeks ago, but it still shows up in our inbox.
I'm in this one.
Maybe I can share my screen.
This one.
So we did reply and said that… It's the job of the maintainers to figure out what they want to do, so not sure… What do we do with this thing now? Should we just remove it from the inbox, because we replied to it?
**David Ashpole (dashpole)** 04:02 Was there something about setting up… I can bring this to the GoSig if we want to discuss it. Was there something about setting up, like.
auto-issue filing or something like that.
**Tigran Najaryan** 04:17 Either way, it's, It's on the… so we are… we're not doing anything outside GoSeq at the moment, so maybe we just move the issue to GoSeq?
Or close this one and create a new one at the… the repository, I don't know how you want to go about it.
**David Ashpole (dashpole)** 04:38 Either way is fine. I'll make sure it gets discussed on Thursday.
**Tigran Najaryan** 04:44 in those acumen.
**David Ashpole (dashpole)** 04:47 Yes.
**Tigran Najaryan** 04:49 Okay.
Oh, we forgot to… I forgot to remove it from the TCN box, right? Yes, that's what I was… yes, should we just remove the label? Because now, I guess, the next step is in GoSeq, right?
The question is, should we keep this open, or we consider this, like.
Since we replied, and the next action is not in the community anymore.
Should we cause the issue?
**Armin (Dynatrace)** 05:14 If we have a designated person that's following up with the GoSig and collect the SIG, we could just assign them and then remove it from the inbox.
**Tigran Najaryan** 05:23 David just volunteered, I believe, to work on this in GoSeq, right?
So we could close it. Do you want to do that, David? Maybe you can comment and say you're going to do a follow-up in GoSig and close the issue so that it's clear you're owning it.
**David Ashpole (dashpole)** 05:40 Yep.
**Tigran Najaryan** 05:42 Okay, thanks.
**Liudmila Molkova** 05:46 The fun thing about that one, that nobody has access to the actual reports of this tool.
Except the person who set it up. And we need to file a PR to some repo to list.
Google accounts of the owners.
**David Ashpole (dashpole)** 06:04 I look…
**Armin (Dynatrace)** 06:04 the report last time, and I could see something, but I was wondering if it was because it… it was past the, like.
how's it called? Like, first they get a heads up, and then after a matter of weeks, it's… it's open to the public. Maybe… maybe I only saw the ones that were already past that deadline and were thus, published. Not sure about that. But I could see some…
**David Ashpole (dashpole)** 06:32 Some content as well.
**Liudmila Molkova** 06:36 Okay, s-some…
**Armin (Dynatrace)** 06:39 Yeah, I think I just followed the link that was posted by… Someone in the… Issue that we just had there.
But yeah, maybe it was really just because it was past the deadline.
**Tigran Najaryan** 07:18 Okay You wanna stop with your topic, Josh?
**Josh Suereth** 07:24 Sure. I shared this out a little while ago. This is just a discussion about, creating a spec maintainer and a protocol maintainer position. So the idea here is, from the TC, you know, restructuring that we did with the our charter. This kind of gives folks to be a technical authority in the specification without the, like, heavy commitment of sponsorships.
Which I think is going to be important going forward.
So, allowing, basically, you can be active on the specification, do deep technical reviews and kind of maintainership that you would expect without having to do the rest of, like, you know, shepherding around OpenTelemetry.
Should I present?
**Liudmila Molkova** 08:22 Yep.
**Tigran Najaryan** 08:22 Yeah, please do.
**Josh Suereth** 08:23 Okay, so basically what this is, by the way, I love that people commented on this, I copy-pasted the existing maintainer rules.
and made a few changes. And most of the comments I got were not on the changes I made.
Which I love.
**Liudmila Molkova** 08:38 Sorry.
**Josh Suereth** 08:38 So, if we don't like… the existing maintainer rules of community, we should go update them. Here's the TLDR. These are the changes to existing rules on maintainership.
The big change is actually what does it… what do you need to be a spec maintainer? For general maintainership, we require, basically, deep knowledge.
of whatever you're maintaining. So if you're on Go, you should understand Go. If you're on the collector, you should understand the Collector. For the specification The proposal here was that, and I think, Tigran, you also commented on this, you need broad knowledge of everything in hotels, so that you can understand how it fits together, and then deep in specific areas that are deep enough to be, like, one of the co-maintainers. And that's… That's a change from the regular maintainership thing, and I think it's important. I was gonna pause here for thoughts or comments.
**Tigran Najaryan** 09:40 I think it makes sense to me, right? Anyway, broad knowledge, I mean, it's very subjective, right, obviously. There may be pockets of of OpenTelemetry that you don't know much about. I mean, that's okay as long as that broad knowledge is there, right?
So that's fine.
**Josh Suereth** 09:58 Yeah, I think the demonstration of this is basically, you know when to… you know when and who to escalate to when you don't know what you're talking about. Yeah.
That's the… that's the most important skill.
Okay, the other thing is for contribution, the contribution phrasing in the current one is very, very specific to, like, sending PRs, doing issue triage, that kind of stuff. I just updated it to be what we do, right? So, you contribute through OTEPs, proposals, prototyping, or review of spec PRs.
And then, instead of requiring meetings, like a specific meeting for the spec, we already have one. So there's a thing about how maintainers have to hold a SIG meeting for people interested in their area. This is just saying, okay, cool, the spec maintainer SIG is where you go.
Alright. Responsibilities, there's a testing requirement, so basically, I just changed the testing requirement phrasing to say we need valid checks on submission, spell check, link check, etc, and that the specification compliance matrix stays up to date. That would be a responsibility of the maintainers to Check this every now and then, go ask people, that sort of thing.
I think that might have recently happened with Go and exponential histograms, I think someone was just asking about those.
That's something that would be a responsibility of maintainership.
And lastly, coordinate milestones and release implementations with SIGs. There's a notion of coordinating releases.
and milestones, and roadmap. And I think that, roadmap is hard for the spec.
Because it's kind of OpenTelemetry's roadmap, so instead, I changed the responsibilities to just be coordinating those milestones, and making sure spec releases are happening, and that, pieces of spec can transition for release.
Okay.
Then the initial list of who would be involved would be all TC members.
And we can expand that as we see fit, with, like, folks who have walked through spec. The idea would be spec sponsors become spec approvers, and that we can elevate them to maintainers the same way that we do in any other OpenTelem tree.
Project.
Okay, protocol maintainer. I don't know if folks looked at this one as much, but I want to call this out. Technical experience?
Basically, deep technical knowledge of protocol buffers, because we use those gRPC and general networking protocols, JSON, that sort of thing.
directly contributed to the subproject through proposals or review.
So proposals could have been OTEPs, or could be directly on the Proto repo, and then SIG meetings for this also happen in the spec maintainer's SIG. This would not have its own, like, meeting.
responsibilities.
Basically, beyond releasing, just communicating releases to other SIGs, so letting people know that a protocol release has occurred, and what changes are in it. I don't think this has a roadmap component.
So I don't… again, that goes back to the other one before. And then, the testing requirement, we just need to provide, prototyping performance measurement… measurements on change. This is something we've started doing, and I think it's working well for the profile intake.
And then ensuring the repository validation remains up to date. So this is actually something I think we do need to spend some more time on. The build tools always falls out of date, and I think right now, some of the code gen… is serving its purpose, but is dubious if people depend on it, so I think we need… anyway, there's work there to be done, but that would be the responsibility of a maintainer.
And the initial list of this, I think, probably can be a subset of TC members. I think this one doesn't see as much activity, I think it's a little bit sensitive, and I think we don't need all of us on it, I think we just need some of us.
But that could be contentious, I just… I'm calling that out. I didn't list who, because I wanted to run it by everyone.
Okay, so that's protocol maintainer. Finally, title committee, we just changed our responsibility, so we removed that we're responsible for approving changes to specification, because the maintainers are now responsible for that.
And we removed that we set release dates, because we actually haven't been doing that, for, like, OTEL. Now, that said, I wrote this before some of the recent discussions.
And I think that needs to be revisited, but… First, I wanted to walk through the TLDR of this proposal, and see How do folks feel? Should we execute on it?
Are we comfortable with these changes to the, the, the, maintainer position.
**Tigran Najaryan** 15:07 I think it makes sense to me.
I don't see anything controversial here, to be honest.
It's… Oh, Yeah, we'll need to… figure out, I guess, the initial list that we start with the existing TC members. That's clear. We should also look into who from the existing TC sorry, spec sponsors are, are… Are the candidates to be added as maintainers to the spec? And what does the process look like?
Is it the same process as we… I think we have something written about how to become a maintainer? Is it exactly the same way?
For the spec, or there's going to be any differences there?
Yeah, we have some requirements.
**Josh Suereth** 16:03 I don't know if they directly apply or no.
This is where I was changing the, like, this deep understanding of technical rules and direction, deep understanding of technical domain. That's why we have that, that caveat. There's responsibilities and privileges, and then how to become. So the how to become… Is, unless otherwise stated, which we could do, just existing maintainers vote.
And the vote is started when you have a pull request to add the member, and it ends when you get enough people who have, approved it from the existing maintainers.
And you have to keep it open for 5 days.
**Tigran Najaryan** 16:40 Yep.
Which means that the… because we are starting with the TC, then the TC will be essentially voting for adding more maintainers.
**Josh Suereth** 16:48 Exactly, exactly.
**Tigran Najaryan** 16:51 Okay.
**Josh Suereth** 16:54 Also, it does say self-nomination is encouraged. Now, I… I went back and forth on whether we should encourage self-nomination or not, I still think we should probably encourage it, so… I think we just have to be judicious, like, you know, make sure the requirement bar is understood.
**Liudmila Molkova** 17:18 So we had some situations in the past where people were, Disappointed by it not being nominated?
And I think it's useful to have self-limination here.
Plus, not every maintainer group, actively Promotes people they see contributing positively, and we need an escape hatch for people who think they deserve it, even though that they might not meet the bar.
**Josh Suereth** 17:47 I… agreed. Agreed. I… I think… I… I would love if we had a consistent every 3 months, maybe as part of GC check-in, hey, who are your approvers that could become maintainers?
just, like, a process that we all run, and we all think about, because I think it's all too easy to forget people. My problem with self-nomination is actually… sometimes this is discriminatory.
there are people who will never self-nominate themselves. And so what… if we rely only on self-nomination, that's a problem. So you need to augment it with, like, group nomination.
And I really want to focus on that, because I think group denomination ends up with an overall healthier ecosystem.
But, I agree with you, like, if we forget, we should allow self-nomination.
**Liudmila Molkova** 18:35 I think we have a point somewhere that maintainers are responsible for mentoring people. We can expand it and say that they're also responsible for promoting People, they see… That means the bar.
**Josh Suereth** 18:52 Yeah, yeah, I… maybe… maybe we should mention this to the GC, or I can take an AI to open a community issue about the Becoming a Maintainer section having a thing about maintainers periodically reviewing and nominating folks, right? Or periodically reviewing who they could nominate.
Yeah.
Okay.
Cool. There's also, this also gives us an Emiratus.
Thing for, you know, maintainer, approver, triager?
So… you could… you could go to be Emeratus as well if you don't have time. I… Okay, cool. Alright, let's go back to… this… One thing I do want to say, I was gonna… this, originally, I was planning to remove release dates. I think we need to talk about… the current blog post from the GC, release dates, this notion of, like, an open telemetry-wide release. I think that's a different discussion, so I'm gonna cut this. It does say the TC Charter has release dates on it, but, and I don't think… I think that the way the TC chart is worded is it really states for all of OpenTelemetry, not just the spec, so I think we can just ignore that section for now.
Okay.
Cool.
Yeah… your comment, Tiffin, here. Any, any concerns with executing on this? If not.
would folks be okay if I started opening NPRs in the community repo and describing this stuff?
Okay, last question.
These differences here.
Should this be in the community repo, or should this be in the specification repo describing How the bar is different for maintainership on the spec versus the community.
**Tigran Najaryan** 20:58 Yeah, I think we should put it in the spec recall, right? It belongs there.
**Josh Suereth** 21:02 Yeah.
**Tigran Najaryan** 21:02 It's about spec maintainers, so let's put it in the spec people.
That was my… By the way, Josh, this… yeah, this whole thing, I think it would be good to present this to the GC as well.
**Josh Suereth** 21:13 Okay.
**Tigran Najaryan** 21:14 To see what they think about it.
**Josh Suereth** 21:18 Yep, and then, then, then start out in GoNet.
Yeah, and then we should all… if folks… I'm gonna do this as well, Tigran. Anyone who wants to maintain the protorepo, or feels like they can.
please add your name. We'll just self-nominate. I just said that I think that is a little bit, people might not self-nominate, so if we don't see enough names, I might reach out to people and ask them. But please self-nominate if you're interested in maintaining the ProtoRepo.
Okay, cool. Thanks, everybody. That was it for that topic.
**Carlos Alberto Cortez** 22:01 So, in that case, I have a private topic, it's not, like.
just, like, super important discussion-wise, more, like, for your information, the status of some… Previous discussion, so he… I would like to present in the private channel, if that's okay.
**Tigran Najaryan** 22:21 Okay, let's go ahead.
**Carlos Alberto Cortez** 22:22 You're there.
**Armin (Dynatrace)** 22:23 You do?
**David Ashpole (dashpole)** 22:24 Wait, how do I get there?
**Carlos Alberto Cortez** 22:27 Oh.
**Josh Suereth** 22:27 Slack. There's a list of bookmarks on the CNCF Slack channel.
With all the private and public things, yeah.
**David Ashpole (dashpole)** 22:35 Yep, yep, yep, thanks.
**Carlos Alberto Cortez** 22:36 We also have a, yeah, a reference to the private meeting notes there, for stuff we can do, because in public yet.
**Liudmila Molkova** 23:17 Hello again.
I… If you're talking, Josh, I cannot hear you. Is it just me, or…
**Joshua MacDonald** 24:00 I don't know where I'm supposed to be right now. I realize that there's two channels.
I'm trying to find… I just found all the notes, so I'm doing… doing better.
**Liudmila Molkova** 24:14 I think I joined the private one?
**Joshua MacDonald** 24:18 I didn't go anywhere, so you're in the wrong place, and so am I.
**Liudmila Molkova** 24:20 Oh, okay, thanks.
**Joshua MacDonald** 24:22 But I don't know how to find this link. Where is this link?
**Liudmila Molkova** 24:26 If you go to Slack.
**Joshua MacDonald** 24:29 Okay, it's in Slack.
**Liudmila Molkova** 24:30 bookmarks, and then there is a private TC Zoom room.
**Joshua MacDonald** 24:35 Private Zoom room. There it is!
Oh, wow. Those are useful links, I didn't know. Goodbye.
**Liudmila Molkova** 24:41 Yeah.
