SIG: eBPF instrumentation
Date: 2026-06-24
Duration: 52 minutes
============================================================

## Zoom Recording Transcript

**Tyler** 00:23 Hey, how y'all doing?
**Rafael Roquetto** 00:26 Dude, how's it going?
**Tyler** 00:27 Good. Good.
**Nikola Grcevski @ Grafana / OpenTelemetry** 00:29 Bye, hey.
**Mike Dame** 00:35 They…
**Tyler** 00:47 Where are we at? Okay.
So I added some, agenda items from last week onto the agenda, as well as some new ones as well. But yeah, for folks joining, go ahead and make sure you add your name to the attendees list, and if you have some topics you wanted to discuss, go ahead and add them there as well, and yeah, we can jump in here in just a second.
Awesome. Okay, yeah, let's jump in here. Let's get started. Almost 3 minutes in.
Cool. Y'all can hear me, right?
**nimrodavni** 02:07 Yep.
**Nikola Grcevski @ Grafana / OpenTelemetry** 02:08 Yeah.
That's good.
**Tyler** 02:10 Yeah, can never tell when the microphone resets, so, yeah. Cool, awesome. So moving on to the first issue, this one's pretty simple, I… No, this isn't the simple one, the other one is a simple one. But this is, the next in the phase of the V2, for the config.
This is the import side of the V2, so this is essentially a translation back from… the V2 config to our standard, like, internal model of our configuration, meaning that this is the way we're gonna proxy any sort of, like, configuration that we get from the V2 to what we already have. This is essentially a shim. My goal here is that, like, as we've talked about before, like, when people pass a V1 config, we should be able to then continue supporting that for a little while. I don't know what that time period is, maybe indefinitely, maybe short, period, I don't know. But the other side is the V2.
So instead of re-plumbing the rest of Obi to just actually, like, use the native, like, representation of, like, the QP2 config, this is just doing that translation, given there is a parity, that we've already guaranteed here. So, yeah, the idea is, this is just continuing in that foundation. There's actually already been one PR.
This is just expanding it. This is dealing with the capture rules, so these are the things that are talking about, like, what we actually want to, instrument, so… Yeah, there's a few others coming, network rules, the actual support for the tracer provider, the meter provider, they're all ready, they're all staged off of this PR here, so, yeah, this is, this is… ready to go, should be ready for review, I'm just asking for review on it.
Okay, next up.
**Nikola Grcevski @ Grafana / OpenTelemetry** 03:54 I'll review today. Sorry. I didn't notice it. When did you make it? Yesterday, or…
**Tyler** 04:00 Yeah, I think it was yesterday, maybe, or the day before, I don't… two days ago. But yeah, it also, like… Nikola Grcevski @ Grafana / OpenTelemetry 04:08 I missed this.
**Tyler** 04:09 It starts in draft mode, so… Nikola Grcevski @ Grafana / OpenTelemetry 04:11 Yeah, okay.
**Tyler** 04:11 Oh, wow.
**Nikola Grcevski @ Grafana / OpenTelemetry** 04:12 Maybe that's why.
**Tyler** 04:13 Two days ago. Yeah, okay, so, yeah, it, as someone who gets probably over 100 notifications a day, I can, I can commiserate, so, yeah.
Cool. Yeah, that's why we have the meetings, just bring them up here. Awesome. Next up is this, this is the easier one, the guards, the renovate Major Op- major renovate updates, so… right now, major renovate updates are being done for Docker images, and as we talked about last week for the Go ones, like.
it's just sitting there languishing, it's not really helping us. So this is doing, kind of a similar thing. It's breaking off the major, updates to be their own independent, upgrades.
But it's notably not allowing most of them, because we don't really want, or haven't ever wanted most of them. Some of them are just breaking, hence why the upgrades are breaking. Others are for compatibility.
So essentially anything in this list is something that's not going to be upgraded. A lot of these are for, you know, specific integration tests that we're looking at particular versions.
please go ahead and take a look at it. If, like, you think this is the wrong list, or these should still go through major version upgrades, I'm happy to adjust. This was just my, take of looking at what was already being done in the existing PR that's opened.
So yeah, this hopefully should stop that PR from existing, and the ones that are upgradable, we should then be able to upgrade. And then, if we find more, we can just update… upgrade this list.
Cool.
Okay, next up, Nimrod, you wanted to ask about stale issues.
**nimrodavni** 05:55 Yeah, I wanted to maybe go over… not necessarily stale issues, but just the easiest ones to kind of start cleaning up. I think Mario also suggested it, cleaning up some of our… Old issues, stuff that have already been solved, stuff that, like… if these are, like, feature requests that people think are still viable, we can just put some label to not stale them. And if there's stuff that's already solved or are not relevant, we can just close them and start cleaning up issues. I think Mario suggested maybe doing, like, 5-10 minutes every… SIG meeting, and I wanted to maybe get it started. So we can… I don't know.
tell me what you think, like, the correct format is. We go over it, like, synchronously now, and try to… you know, mark these issues as, like, either we can close them or not, we want to do it, like, asynchronously. I put down, like, the… I removed the goal label and just put the stale, but we can even do something like filtering the oldest issues that are not goals, and… Doing by that.
So, you know, we can… I did a couple of them myself, but, Maybe some of them, like, people already know if they're relevant or not.
**Tyler** 07:16 Hmm.
Yeah, I mean, I'm happy to… Do whatever the group wants to do here.
I… I don't know… If… like, if it helps to do it asynchronously, I think that's fine.
I don't know if it needs the whole SIG to do this, this is more of a maintainer task, is kind of my problem, that I'm kind of stumbling over here. So, like, I didn't know if maybe we wanted to have, like, a separate triaging meeting. We've definitely done that in other hotel meetings, instead of… having everyone on the call, go through this. If we… everyone on the call wants to just go through it, we can go do that.
Yeah, I'm, I'm… whatever you think is best.
**nimrodavni** 08:06 Yeah, like, I'm fine with doing it, even as a… Separate meeting, maybe more like the maintainers or something, but.
**Nikola Grcevski @ Grafana / OpenTelemetry** 08:17 Yeah, let's do that. Yeah. Let's try to get a crack at this, maybe async, and then let's organize on this, on this.
CNCF Slack to figure out when is a good time for everyone to kind of go over the stuff that We just don't know where the person that went through that. I saw on the list a couple of things that I think I can close off.
Banks that are fixed are questions, yeah.
**Stephen Lang** 08:42 This might actually be relevant to what Raphael… Raphael and I put on the list as well.
Because, yeah.
**Tyler** 08:50 Yeah, I saw that as well.
**Stephen Lang** 08:51 A separate triaging meeting kind of comes into it, so… It's kind of linked.
**Tyler** 09:00 Yes, maybe we can… maybe we can talk about that as well. Steven and Raphael, I saw that you also added… this PR review bandwidth and assignees and triage.
So maybe, yeah, we can kind of group that in, like.
Do you wanna go ahead and… Takeover?
**Stephen Lang** 09:18 Yeah, so it's not to dismiss you know, the triaging idea at all. In fact, it's to talk more about that. So I've kind of noticed, personally, when I'm reviewing PRs, I think I sort of hinted at this last week, but maybe you didn't articulate it very well when we were talking about a PR load.
But I found oftentimes I might be reviewing a PR in depth, and then it kind of gets approved and merged.
Whilst I'm looking at it.
And I think I'm not the only one that's kind of seen this, And I think sometimes, you know, I don't always have the time to be able to drop into a PR, like, the same day as the SIG, with the SIG being kind of my end of day, in the UK.
So, what I'd like to be able to do is somehow to… use something like maybe the assignee field on a PR, just to say, hey, wait, I would like to take a look at this PR before it gets shipped.
And you know, if there's something in particular that I'd really like to take a look at.
I'm not sure we have, like, that kind of communication Right now in the project, which is to say, maybe with a request you know, somebody to look at this thing, and Raphael can maybe put a different perspective on this as well.
**Rafael Roquetto** 10:31 Yeah, so, apart from… what Stephen just said, which I fully agree, it's, so there are a couple of issues, I mean, this for me, is… I also suffer from, you know, start reviewing a PR, and then it gets approved, and sometimes it gets merged.
And then it's, usually, using a strong word is a waste of time, because, you know, ship has sailed.
And also we're getting, like, it's rainy PRs, left and right. Some… some are more… I guess I would say more… important is not the right word, every PR is important, I guess, but, you know, more urgent than others, or tackle different things. Some forces, which I guess is part of the… you know, being an open source project, that's normal, but some PRs are really revolutionary, and it's not really part of our roadmap, and it kind of forces us to pivot to them, and, you know, new discussions. So, I guess… you know, you could spend the whole day, 5 days a week, just reviewing PRs, which is obviously not what we can do in practice. So, I like the idea that Steven is proposing of, well, a couple mechanisms to kind of balance these. First one is If you, you know, assigned to a PR, you don't ship a PR until everyone who's been assigned.
has, you know, approved the PR. I think that's a very easy… way to kind of, you know, you're signed, you wait for the others to give their opinion. If they don't, you can ping them, or you… Yeah, that would be one… one way… one thing that I would support doing, and the other thing… And I, I think… People might have different opinions then is, like, the triage, having a triage meeting so that we can kind of see, okay, we're gonna be… reviewing this set of PRs between, these two SIG meetings. Obviously, this doesn't have to be, you know, a hard rule. If you feel like reviewing some other PR during your week.
that show… that showed up, or if there's something important that needs to be fast-tracked, you know, I think we… we remain flexible. It's more like a north. But doing this in between weeks allow… Us to kind of… have an overview of what's going on. Sometimes even, you know, it gives you time to assign yourself to a PR to begin with, because what I'm saying, okay, you assign yourself.
But, like Steven said, if it happens at the end of your day, you know, it can happen that PR gets raised, people assign themselves, it gets shipped, you didn't even have the chance to see it. Maybe that's fine, we don't have to see.
all of the PRs, you know, like, it's not like the Eye of Sorum or anything like that. It's just a… just a thought, I don't know what you guys think.
**Giuseppe Ognibene | Coralogix** 13:42 Hi, Yogiri.
Sorry, I was finding the microphone.
**Rafael Roquetto** 13:46 Yeah, all good.
**Tyler** 13:52 Yeah, I mean, I, I… it's hard for me to not be jaded at this point, I guess, is maybe what I'm trying to say politely. Working in hotel for 5 years? 6 years?
Man, I don't want to do that math, actually. So, like… it doesn't bother me anymore, because I think it just is a natural part of, being a maintainer and being a part of these projects, is that, like, you are going to get a lot of conversation and a lot of… Noise, I guess, is maybe a way to say this. So… that's not to say that, like, we shouldn't try to address it. I just want to point out that, like, your feelings are valid here on this one, is what I'm trying to, like, roundabout say, right? And so, like, it happens, and, like, it just becomes overwhelming.
Definitely heard a few other, like, talks on this line, right? So this is not, like, unique to us. I think your approach for the approval stuff, like, that could be very helpful. I definitely know it's frustrating, when you see a PR merge, like, it, you know, it feels like the ship has left.
I think I saw Robert on the call as well, who works in a lot, or used to work a lot in the, Hmm… the .NET SIG, where they were really active about, post-merge reviews as well. Like, if you reviewed a PR, but it had already merged, you know, obviously within, like, a few days or something like that, like… any sort of that feedback was still addressed, and it was considered, like, valid feedback, right? And I think that that's always the case, it's just that, like, it's not a cultural thing in a lot of repositories. A lot of people, like, see the merge, and they're like, well, I'm not… I'm not hitting that review button now, like, that's just pointless, waste of my time, right?
So, like, I don't know if we wanted to try to do that. I like the, assignee thing. I know that in… in the specification, I think, or there's other repos they auto-assign, so, you know, you take a list of all of the approvers that are part of the project, and each new PR gets an assignee, and then… That assignee's really just there to triage it. When they find that they should review it, they're responsible for their review. If they think somebody else should review it, they put their… that other person on there. I do think that, like, if you're an approver, you should have the ability to assign yourself to the PR. That's another good question for people who are approvers here. I know that, like, there's maintainers and approvers.
like, if you're an approver, like, can you assign yourself to the PR? Because I think that if we just go with that ethos that you just described, Raphael, I'm all about it. Like, if you just want to say, like, hey, I'm taking a look at this, you know, I've laid claim, don't merge this without my approval, that seems valid.
You can have multiple assignees, you don't have to have just one, that's another thing.
So yeah, I mean, all this sounds good.
The only thing is, is that I would codify this into some sort of policy, or somewhere, just write it down, because putting it out into the ether here is not gonna really, like… Yeah. Yeah. It's the only thing.
**Rafael Roquetto** 16:54 I just wanted to add one thing, like, yeah, it's expected to… and I'm not disagreeing with you.
But I think there is an important thing that happened in the past 6 months, again, AI, which kind of… when I say it's rainy PRs, it's… a lot of PRs that we get are maybe… shouldn't… it wouldn't be there, shouldn't be PR. The amount of cognitive load that you have to put in a PR nowadays is much higher than, you know, a year ago. Because a year ago, you had a natural filter. Now it's like, you're basically reviewing whatever people come up with, and a lot of contributions I've seen don't… still like a little bit of understanding of the context of the code, so that kind of does… it added up, at least for me.
Where, you know, usually, I don't know, you take half an hour to review a PR, now it's, like, 2 hours. So that doesn't help either, so maybe it's a little bit of this coming, at least speaking only for myself, as a reaction to that, like, how do I… how do we keep, like, the project going?
With, you know, keep… keeping the quality of the code growing good without, like, rotting, and still, we also don't want to block new contributions and things like this. I think, Mattia wanted to say something?
**Mattia Meleleo** 18:15 Yeah, a couple of things. So, I don't know if we have any policy for, like, the minimum number of approvers or reviewers. I don't think we have.
Maybe, maybe it would be good to set it to 2, for example, because sometimes I, prove a PR, and I don't know if it's… if it's… if… just one review is good enough for merging it, because that depends on the type of the PR, like, if it's just a dependency upgrade, then it's fine.
But if it's something more complex, then maybe 2 or 3 reviewers would be better.
And one other thing is, there is also the option, in the code owner's file, I think.
To set a directory and automatically assign some reviewers to that code path.
Maybe we should, we should use that.
**Rafael Roquetto** 19:14 I think two reviewers are good.
The idea, regardless.
Just… that's just me, yeah.
**nimrodavni** 19:24 Nonethe.
**Tyler** 19:24 Yeah, I like the two reviewers, we have that in other repositories. Two reviewers specifically from other companies is also a qualifier we normally put on that.
That comes from… drama that I hope never bleeds into this fig. But, like, the… the idea there is also, like.
it can be hard to get those two reviews, so I might also… I might put a qualifier on that, saying that, like, 2 reviews within 24 hours, and then, maybe based on, like, the size of the PR, if it's, you know, relatively small, after 24 hours, or after a full working day, one review, because, you know, people are out of town or something like that might be good, but I'm also okay if everyone just wants the two, yeah.
**Rafael Roquetto** 20:11 Nikola?
**Nikola Grcevski @ Grafana / OpenTelemetry** 20:12 Yeah, that actually sounds good. I like that approach. I was gonna say, do you want to just maybe slow down in terms of, you know, require at least a day for a PR to be merged, or things like that? But I think what Tyler said makes more sense.
If we could… You know, it's a small PR, something obvious, okay, fine, like, after 24 hours, you don't need two reviewers, you just merge it. But if it's something sizable, maybe that lasts a bit longer, requires the two reviewers for a bit of… more period of time.
**Rafael Roquetto** 20:41 what we could do, I don't know if this is a good idea, but just thinking out loud is… in this particular case. So, the premise is, like, PRs get reviewed by whoever is assigned, whoever's assigned gets to approve it. And then… you can… nothing prevents me from adding any of you as an assignee. If I think, you know, you know, it's a BPF, I want Mattia and maybe Giuseppe to have a look, for instance, that also… I think as someone's gonna have to… at least one person's gonna have to approve a PR, so as an approver or as a maintainer, maybe… I don't know, maybe it should be enough that use your judgment to think, okay, this requires… this can be approved by myself, or no, I would like someone else to have a look, and then you… you… you pick someone, and… and this… I don't know, just a thought to kind of not end up with a lot of, rules that are difficult to digest, not saying this is the case, it's just another thought, but I am fine either way.
**Nikola Grcevski @ Grafana / OpenTelemetry** 21:40 Yeah, that works to it for me as well, if you think this particular piece of code that's being proposed.
somebody who's an expert on that, or should really be looked at somebody who worked on this before, and maybe request some other maintainer or approver on the team to kind of do the review. And if they're not around, then… That's fine, you know, like… People go on vacations, people have work requirements that prevent them from contributing as much that week, or whatever, then… That's… that's fine.
Yeah, we can try that.
**Tyler** 22:18 Going back to the triaging stuff as well, like… I am hesitant to have, like, another reoccurring meeting in my calendar, but I am okay if we wanted to do it for, like, a limited time period. And maybe during that limited time period, we could also be addressing, like.
still PRs, but also just, like, this assignee, process. Go through, essentially, a few times and say, like.
hey, this PR needs someone to take a look at it, and then we'll assign somebody and go through that there.
So, yeah, I mean, I'm definitely okay if we wanted to try to add in a triage meeting, trying to loop this back to Nimrod's original point as well for, like, stale issue stuff.
And maybe we can just coordinate that over the next, a little bit in Slack afterwards? Does that… does that seem reasonable?
**Rafael Roquetto** 23:14 That sounds reasonable, yeah. And can we agree then, just to, like, get everyone here on the same page, that at least a PR needs to be merged when all the assignees approved it. I think that's also a really easy one, and if you can always ping the assignee, or on the PR itself, if the person is missing action or something.
Wow.
**Nikola Grcevski @ Grafana / OpenTelemetry** 23:38 But that will block PRs that people go on vacation. Let's say you were reviewing something, you started a conversation, and it took 2 weeks because you were out for 2 weeks.
Maybe it's PR, yeah.
**Tyler** 23:50 Yeah, I… I think… I think I… yeah, to Nicola's point, like, I… I can see the being assigned… having an assignee as a lock, or like, like, you know, from the coding parlance, right?
If you're holding that lock for multiple hours, that means that you're actively reviewing it for those multiple hours, is kind of how I see it. If you're holding that lock for multiple days, I think you just forgot, or you moved away.
**Nikola Grcevski @ Grafana / OpenTelemetry** 24:11 Yeah.
**Tyler** 24:12 Obviously, like, if you put a comment in that PR saying something to the effect of, like, I've been thinking about it for a little while, like, you know, let's hold off on this, like… I think that's… that's more… that's more effective than just having an assignee there, but I think if you have an assignee, I'm expecting you'd be, like, you know, actively reviewing that PR, is kind of my goal here. So, like.
waiting… waiting days to… to wait on that, I don't think is reasonable.
**Rafael Roquetto** 24:37 Yeah.
**Nikola Grcevski @ Grafana / OpenTelemetry** 24:39 For the triage, I mean… we don't have to have a sync meeting, maybe we can just go with a… use the channel a little bit more on Slack, and say, hey, for this week, we have those PRs.
maybe we should review these, like, whoever is available, just bring it up there to people's attention, or this… these, issues need to be kind of looked at, let's take it chunk by chunk, and I'm sure we'll blow through them, be more active on that front, and kind of prioritize that this PR should be looked at and merged. And I know stuff comes through the week all the time, but we just… When you see something that you think is important, just post it.
And make sure we get through them.
**Tyler** 25:21 Yeah, I mean, I do wonder if I can, like… If we can set up some sort of automation, and somebody can just… Manage that, where they go, like, you know.
Monday morning at 8 AM, they post in channel, like, here are the open stale issues, like, please comment in thread, like, you know, something like that. Here are the PRs that haven't had any reviews, please comment in thread, or something like that if you plan on taking it.
**Nikola Grcevski @ Grafana / OpenTelemetry** 25:42 Yeah, that would be great, yeah.
**Tyler** 25:43 Yeah.
Does anyone want to take on that action item, for automation, or is that something that I've unfortunately designed myself?
**Nikola Grcevski @ Grafana / OpenTelemetry** 25:53 I don't know how to do it. I don't know how to do it, so…
**Tyler** 25:56 Okay.
**nimrodavni** 25:56 I can try… I don't know if… like, we already have some GitHub actions for it, I just don't know… we probably need some Slack authentication. I can try to check.
**Tyler** 26:05 Yeah, I imagine… there's probably a little bit of manual pro… anyways, like, something, right? Like, even if it's manual for the first few days, or first few, weeks, or something like that, but yeah.
**nimrodavni** 26:15 Maybe something like Steven's, like, CI report or something.
**Tyler** 26:18 Yeah, yeah. And you just copy-paste it or something like that, that seems reasonable, but yeah.
**nimrodavni** 26:23 I'll try to explore if we can even integrate with Slack.
Yeah.
**Roy Reshef** 26:27 One thing you may want to consider here is to use Git commits. Sorry, Git commit messages.
for part of this automation. I mean, we've done it internally for a totally different purpose, but… For example, we use AI review.
I'm not gonna propose it here, but you can trigger it by putting a commit into a PR, saying, hey, I want AI review on this, or whatever.
So, let's say you are, some, you know, you're committing something into a PR, and either you want a specific person to review it, or you say, even though this PR looks small, because it only has 20 lines of code, it's… it's very sensitive, so I want multiple reviewers.
You can add it with commit messages, and then, You know, make your actions use commit messages to do whatever.
Just a suggestion.
**Tyler** 27:29 Yeah, thanks. I think we've… Yeah, we've definitely been dabbling with the AI review, so that's also helpful.
One of the… the last things I want to touch on here, Rafael, is we had an action item to capture, all this, like, two approvals and the, assignee stuff in a policy. Is that something you can take on?
**Rafael Roquetto** 27:54 Yes, I can do it.
**Tyler** 27:56 Okay, cool.
And so, along those lines also, One of the other things I noticed, I… sorry, like, just wanna… Put a, come back to this, like, you also were talking about, like, large, seismic, even, changes of… happening in PRs.
I do think that, like, that is a… Important thing to also have in our policy docs.
It's… I think that those PRs should be closed, to be honest. You just need a policy to point to, though, is the problem, though. I think that, like.
a lot of other… almost… I don't know any other SIG here that doesn't have some sort of policy around, like, if you're… if you're trying to propose some completely new feature, completely new issue, completely new, like.
you know, a workstream, like, you need to do that in… in an issue, you need to do that in some sort of, like, scoped project even, right? And, like.
Then we can prioritize that, especially if that person is expecting to dump the PR and have all of the maintainers maintain that, right? Like, that's not… that's not really appropriate, if it's just gonna derail all of the active work that we've already planned for the rest of the year, right? So… I think, Rafael, as you're updating the policy docs, like, maybe it's also worth, like, considering in a separate PR or something like that, you know, putting your thoughts on this as well, like, if you wanted to put some restrictions on what sort of processes we want to put in place and that kind of thing, and you can make a proposal around that, yeah.
**Rafael Roquetto** 29:34 Yeah, okay, I will… I'll take care of it.
**Tyler** 29:38 Yeah, okay.
**Rafael Roquetto** 29:38 In a separate year.
**Tyler** 29:41 Yeah, that's a part of the policy now.
Okay, we've been on this for a little while, but I want to make sure, any other things people wanted to bring up here, there's a lot, we can continue talking about this for sure, in future meetings as well.
But if not, we can head on back to the agenda. So the next thing up, Nikola, he would ask about the next, minor release. I think we're pretty close. There's still a few issues, we have in the milestone.
That need attention.
Yeah.
**Nikola Grcevski @ Grafana / OpenTelemetry** 30:16 The reason I asked is because there was a customer in the public channel that said they wanted a release.
For an issue. And also saw somebody else comment on that.
pull request, it was done by a new contributor, Milos, or something like that?
I forget.
He fixed the gRPC bug on high load.
**Tyler** 30:41 Oh, it's already merged?
**Nikola Grcevski @ Grafana / OpenTelemetry** 30:43 It's already merged gRPC, maybe you can search by gRPC… Oh, great.
Right.
**Tyler** 30:57 What was this? Last month? Okay, maybe just look at the history, actually.
**Nikola Grcevski @ Grafana / OpenTelemetry** 31:00 Yeah.
Maybe it doesn't mention GRPC.
It's recent, it's not too long ago. I think I can find the issue ID. Just one second.
Hmm.
Yeah, issues 2300.
**Tyler** 31:37 Okay.
**Nikola Grcevski @ Grafana / OpenTelemetry** 31:39 So… On heavy load, I think it's… it was causing some protocol issue.
I don't know.
The originator of the issue fixed it eventually.
And we merged it.
**Tyler** 31:54 Yeah. Yeah.
**Nikola Grcevski @ Grafana / OpenTelemetry** 31:56 So… So, they were asking us, I guess.
Channel to see if we can get a release.
**Tyler** 32:11 Yeah, I'd love to… I'd love to get a release out, honestly.
**Nikola Grcevski @ Grafana / OpenTelemetry** 32:16 So should we.
**Tyler** 32:17 There's a ton.
**Nikola Grcevski @ Grafana / OpenTelemetry** 32:18 movie.
**Tyler** 32:18 There's a ton of things that we've got done, there's a bunch of bugs, not just the gRPC, like, there's… Nikola Grcevski @ Grafana / OpenTelemetry 32:23 Yeah.
**Tyler** 32:24 23 bugs I know of that got resolved, right? Yeah, some, yeah.
there's still… there's still two things, I think, that are blocking this, though.
**Nikola Grcevski @ Grafana / OpenTelemetry** 32:33 Huh.
**Tyler** 32:34 possibly 3 now, with what Nimrod just posted, but, this cloud node metadata, exported Prometheus and OTLP without sensitivity filters, This is the last bug that I've opened that I wanted to get addressed in this release.
I was looking for feedback on this.
I guess I can just go ahead and start implementing this plan I posted, but… Yeah.
Essentially the idea is that, like.
Yeah, these cloud fields are really high cardinality, and so having some sort of way to manage that cardinality is pretty critical to not overload backends.
Yeah. Yeah, and so this was just the… it was pointed out, I think.
**Nikola Grcevski @ Grafana / OpenTelemetry** 33:26 For the reason?
**Tyler** 33:27 Yeah, this is, I think, pervasive in a lot of things, but so.
Yeah, so one of the things that I wanted to do was just not look at necessarily just, like, the selector, but just actually look at these, these opt-in behaviors, essentially, and try to, like, wrangle this.
If… folks are okay with this, I'm happy to start tackling this so we can get this resolved. This is, I think, the last major, like, bug that I wanted to get Finished up.
**Nikola Grcevski @ Grafana / OpenTelemetry** 33:52 Okay.
I don't see a problem with that, so let's… I mean, I can help with some of this stuff as well.
Okay. Let's try to… Smash these and get this… Really sad.
**Tyler** 34:04 Okay, cool. Cool, let's… let's… I'll prioritize this.
The other thing is, this. I'd really like to get this in.
We have support for non-buffer channels right now. This is adding support for the buffer channels.
I… I know that Nicola's already taken a look at this one already, and reviewed it. It's had great feedback, thanks for the feedback as well, it's been updated. Okay. I think this is ready for another round of reviews.
Yeah, the only thing left after this is just documentation on it, Because otherwise, like, I'm not trying to tackle the selector stuff in this, this release.
So Yeah.
And then, Imrat, I saw this as well. This is a good call-out. I think this is worth including, I figured…
**nimrodavni** 35:01 Already, like, maybe we can even merge it.
**Tyler** 35:04 Yeah, I think it's actually ready to merge. Oh, that was, I just wanted to ask Nikola… You had this question here. I didn't know if, like, you've taken a look since, Hmm… since updates?
**Stephen Lang** 35:20 I love this historical.
He got a call.
**Tyler** 35:24 Okay, cool. Alright. I… I'm just gonna resolve this, and… I think Giuseppe's on the call, right? I'm pretty sure, Giuseppe, you've already responded to the… or you've gone through this, right?
**Giuseppe Ognibene | Coralogix** 35:36 Yep.
**Tyler** 35:39 Okay. Yeah, I'm gonna resolve it. If that's a mistake, then that's a mistake.
**Giuseppe Ognibene | Coralogix** 35:45 Italer, I don't know if you saw it, but I changed the way I mean, like you… you said, more or less.
Now we can, we can have a list of default PD param, and then the user can, Include or exclude?
I mean, there is no semantic convention, there is no… okay.
**Tyler** 36:08 Yeah, yeah, she said. Oh, yeah, I definitely saw that. Yeah, all about it.
Did you adjust the… the Go stuff is still remaining as a follow-up, right? Yeah. Okay.
**Giuseppe Ognibene | Coralogix** 36:19 Yeah, I open Anisha, we'll work on that.
**Tyler** 36:22 Yeah, yeah, no worries, yeah, okay.
Yeah, let's… this looks ready to go, yep.
Okay, cool.
Awesome.
I don't think there's any other… PR as a standout. I was just looking through all of them yesterday. But yeah, okay. So, last step is just this. So, yeah, I'm working on this. There's this documentation for parent-child association limitations.
It'd be nice to get in, but I don't think this is a blocker. We talked about this last time. I've got this import config v2 capture rules more just to track it. It's not blocking anything, this isn't actually exposing anything yet, so… Technically not in this milestone, actually, I don't know why I have it in here. I think it's more just to show that it was gonna get done.
So, yeah, please take a look at this. Pr, definitely help progress this, and then let's start on this.
Okay, Next up, I wanted to call out again, like a broken record, that we would appreciate it if you can take a look at this, issue.
and the associated PR with it, and, just comment on here. A simple comment to the effect of, this is great, I support it, I'd like to see this move forward.
all would be really helpful. Thumbs-upping it, also really helpful. So, yeah, please… Please take a look.
I'm enjoying to see these emojis.
Okay.
Awesome.
That's the end of the agenda. Any topics people had that aren't on the agenda?
**nimrodavni** 38:05 If we're on the topic of sending, PRs and other refos. Maybe if you can also comment and thumbs up the… I send it in Slack.
About, sharing the register instrumentation with external readers.
I think, Florian, you're on the call, I think we talked about… some stuff there, and I think, of me and Evo kind of discussed options, and maybe if you can comment there, there'll be… great as well, but if anyone else, like, wants to go through that, I think it will help us with, Kinda, moving from, like, an all-or-nothing instrumentation to being more, like, a complementary instrumentation of, like… we can instrument, for example, only DNS and TCP stuff, but we'll leave the auto-instrumentation for the… Library, so we can do some really cool stuff, but we just need the support on the resource process, protocol.
And if anyone has any comments on that, I will… Next to get some… some more traction there.
**Florian Lehner** 39:24 Yeah, cool.
**Tyler** 39:25 Cool.
Go ahead, Florian, sorry.
**Florian Lehner** 39:28 Sorry, yeah. Yeah, I think that the problem here at the moment, there are too many things happening at the process context.
Over a resource process context, at all. The… the initial batch of this work is just merged in Proto, but there's no release yet that is… that contains it, so you cannot actually use it unless you're using the proprietary version that is, that you could distribute with eBPath Profiler.
I think I'm trying to ask for a release of, OTL Proto.
Maybe this could then help bringing us these steps closer, but, with also the work happening on… threat context, there will be some overlap, so… and my feeling is at the moment that, specification sick and maintainer sick is, at the moment a bit overloaded with all these changes.
So, yeah, I think that that's the reason for a slow progress.
**nimrodavni** 40:38 Okay. Like, the… the thread level, context is but something kind of different, right? Like, it's not… it's kind of the same… it gives, like, similar benefits to, like, OBM.
**Florian Lehner** 40:51 Yeah, I'm.
**nimrodavni** 40:52 It's also really exciting.
**Florian Lehner** 40:54 Yeah.
**nimrodavni** 40:55 You're saying, like, the resource context is kinda… there's no official, like, base release for it, so we can't extend it yet?
**Florian Lehner** 41:04 Yes, and if you look into OTA Proto, it was just merged, but since the merge of this, of this product, there was no release on that.
And, once this is merged, we can bring it into the SDKs, for example, Go.
We can bring it into Java, we can move it out of eBPF Profiler. I want to then work also on the, the draft PR, I've opened with eBPF, so with OBI. So, there are pending steps.
Yeah, let's see how it goes.
**nimrodavni** 41:37 Yeah, makes sense, but I think still, Like, maybe more common for that will maybe, make the… hoping will make, like, the specification and maintainers, Try to look at it more, but…
**Florian Lehner** 41:52 I think getting attention from the specification sick is only joining Tuesday, I think they have a call, and ask them on the agenda. Otherwise, they will hardly look at it, is my experience.
**nimrodavni** 42:06 Okay, I can try to… Come… come… I think I already, like, came to get them to open it from an issue to a PR, and then we got some comments.
But yeah, I'll continue looking. And if you can have a look at the comment where, like, I described, like, all the… you said, like, instead of doing it as a separate field, doing it as attributes.
So I try to describe all the options of doing it as attributes. I'm not sure I'm super… like, I don't think any one of them is really… Great, because it's, like, an array of structs, but… Yeah, I'll send you the deck link.
**Florian Lehner** 42:46 Yeah, thanks for bringing it up. I will look at it again. It just was pushed down with notifications over the last week.
**nimrodavni** 42:53 Nope.
Thank you very much.
**Tyler** 42:56 Robert, are you a proto-approval?
**Pellared** 42:59 Use the M.
Anything that…
**Tyler** 43:01 Do you know… oh, even better, what's the release schedule for the Proto?
**Pellared** 43:07 I have no bloody idea.
**Florian Lehner** 43:09 Oh, it was above.
**Pellared** 43:10 in… Yeah, I think it's on demand. On demand, it's not… Not every month, right?
**Florian Lehner** 43:17 There's no schedule, it's on demand.
**Tyler** 43:21 So, robert, can we get a proto-release?
**Pellared** 43:26 So I think it's better… the best thing is just to create an issue to track if their others are, you know, have no concerns, especially that there's no segmenting dedicated for Proto.
**Tyler** 43:38 Right.
**Pellared** 43:38 So, I think it'll be the easiest way to make sure that all the things are addressed before the release.
**Tyler** 43:47 Yeah, that'd be great. Florian, could you create that issue?
**Florian Lehner** 43:50 Yeah, I can also support this, this release then.
Yeah, we have tomorrow… tomorrow, a SICK meeting with profiling, and we want to get some stuff in.
And, yeah, then I can bring this up.
**Tyler** 44:05 That'd be great, yeah, let's, let's keep that… keep that going.
Awesome.
Cool, any other topics? Projects? Things we're working on? Interesting side things? Oh, side things.
One of the side things, is that, that demo, the store demo that we merged recently, I've been playing around with it on the sides, And trying to build in features that, are in the OTEL observatory as well, essentially adding in functionality, things like, Kafka Q, LLMs, and LLM, like, message payloads, what's another one? Oh, yeah, like, an image proxy is also included in the, the Astroshop. So, I've got those, like, kind of, like, working in, like, the side, fork of this example, but my goal is, like, to merge this back in upstream.
Yeah, it's pretty awesome. It's a really full-featured, like, OB demo, like, when you start to see, like, everything that it can touch. I mean, it's just end-to-end.
And, yeah, so, like, yeah, more to come on that one, but yeah, it's a pretty cool, like, setup. Even, like, the base one right now, I think, is good, but, like, yeah, just… Just, just working on getting something together, and then we'll try to fork that and move that upstream, yeah.
**Nikola Grcevski @ Grafana / OpenTelemetry** 45:23 Yeah, that's fantastic. I mean, I think even the operator project can benefit from that demo, because it's dealing with auto-instrumentation, so showing completely uninstrumented application and instrumenting it.
Yeah, I wanted to mention, from our side, I think, it's a hackathon week here at Grafana, so Steven and I have been hacking around.
As well, I'm mostly looking at the hotel demo, but I also found some cool use cases. Thought about using… It will be for, like, tracking data flow rather than service connectivity, so kind of seeing which services touch which databases.
We also found a really cool use case for the payload extraction.
That… And we… I'm gonna propose a change, actually, a new config option, to have different redaction string per rule.
We found this kind of cool, because you kind of… can redact PAI information with something, and you can redact healthcare information or something else, and then you can then build dashboards to know which services are touching health information, which services are touching PI information, or which services are touching credit card information.
So you can kind of create special identifiers, with a config, and then display that kind of stuff to say, oh, there's this very sensitive service because it handles healthcare data.
Yeah, it's pretty cool.
**Tyler** 46:52 That's cool, because then you could also see, like, change in behavior, right? Like… Nikola Grcevski @ Grafana / OpenTelemetry 46:56 Yeah, yeah.
**Tyler** 46:57 Why is my greeting service asking me, trying to touch healthcare things?
**Nikola Grcevski @ Grafana / OpenTelemetry** 47:00 Healthcare data, yeah.
**Tyler** 47:02 Yeah.
**Nikola Grcevski @ Grafana / OpenTelemetry** 47:02 We're still experimenting with a lot of things, but yeah, we decided to go deep on… Yeah.
So we found some bugs as well. So, yeah, you'll see PRs coming, hopefully, when this week is over.
Yeah.
**Tyler** 47:21 Cool. Awesome. Yeah, I'm super excited. That's… that's great.
**Roy Reshef** 47:27 About this, Tyler, about the examples.
Sorry, go ahead.
**nimrodavni** 47:32 No, I want to say about the Obi store that's really cool. We had… like, we… in order to test some of the features, we developed In Obi, we kind of made, like, a… we forked the, Basically the, demo.
continued adding… I don't know exactly… I didn't fully look at the store and all the capabilities, but I think we added some stuff, like… Couchbase and Mongo and, like, an AI agent to test all the, the, the… Stuff that, was worked on, so maybe we can try pushing some of it to Obi.
**Nikola Grcevski @ Grafana / OpenTelemetry** 48:12 Yeah.
**nimrodavni** 48:12 I don't know exactly what's the difference between what we have and what the OB SOR has, but we can try to push some of it.
**Tyler** 48:21 Yeah, that'd be… maybe I'll open an issue tracking the features that I've already added, and, like, if you can… I'll point you towards it so you can also, like… because I definitely didn't add Couchbase or any of these other databases, so that's, like, great.
So yeah, I would love to… especially things we, like, already support, so all the databases you said, like, the Kafka, anything, essentially, that, like, OB has, like, I'd love to be a part of the demo, so yeah, that'd be great. The LLM stuff, I think, is really great, because we're working a lot on that as well, so… Yeah, I'll open an issue. Let's work on getting some features upstream.
**Nikola Grcevski @ Grafana / OpenTelemetry** 48:53 Actually, I wanted to say, sorry, sorry, Ray, about the LLM, because we're mentioning it here. I know that the hotel demo, apparently we just found out that they've added LLM, because we've been playing with it, but I don't think we catch any of that, because it's… I think it's an internal service that just kind of mimics OpenAI with chat completions, and we lack the headers, so it doesn't actually look like an OpenAI to us, and we don't get excited about it.
**nimrodavni** 49:20 I did some, like, LLM proxy, which looks like it exposes OpenI request… open anthropic requests, but, like, behind the scenes just goes to a local… Nikola Grcevski @ Grafana / OpenTelemetry 49:32 Yeah.
**Tyler** 49:33 Yeah, I, Your point is correct, Nicola, and I copied, essentially, what they did upstream, and it didn't work.
**Nikola Grcevski @ Grafana / OpenTelemetry** 49:41 Okay.
**Tyler** 49:42 And I had to go and fix it to be having the right headers and things, so… Nikola Grcevski @ Grafana / OpenTelemetry 49:45 Yeah, yeah, if you don't see the headers, we're just like, oh, that could be any V1 chat completions, that doesn't actually mean it's an OpenAI, like, how would we possibly know? It could be somebody, customer service just chose that name for another reason, right?
**Tyler** 49:58 Yeah, yeah, exactly. Yeah, so, like, it also required us changing the demo a little bit, but… Nikola Grcevski @ Grafana / OpenTelemetry 50:03 Yeah.
**Tyler** 50:04 Once it did, it was really great, because all that kind of stuff just starts kicking in, yeah.
**Nikola Grcevski @ Grafana / OpenTelemetry** 50:08 Nice. Sorry, Ryan, go ahead.
**Roy Reshef** 50:10 Actually, what I wanted to say was just about this. I was playing with, locally, with Cube.ai. I don't know if you're familiar, it's a very popular AI inference server. I did it for mainly metrics collection, I didn't try to instrument anything over there, but… It's pretty easy to set up, and you have models that can run on CPU only, so you don't even need the hardware. I mean, I have a kind cluster with a toy GPU inside.
So I could actually deploy the minimal Llama model on it and run it. It might be a good candidate to check out.
**Tyler** 50:52 Yeah, that's great.
**Nikola Grcevski @ Grafana / OpenTelemetry** 50:53 Cube AI, you said?
**Roy Reshef** 50:54 Cube AI, yeah. I can send the links on the Slack channel.
**Tyler** 50:59 Yeah, on Slack, it'd be great. Yeah, like, right now, I did the same thing as in broad, where essentially it's like canned responses, so if it sees a particular request, it's like, oh yeah, I'll act like I'm an AI, but it's not really, it's just… But yeah, that'd be cool if you could actually have something a little bit more, like, demo-y.
Because then it could also probably have different responses that we could capture, so it's not just, like, you always see the same payload. So, yeah, that'd be cool.
**Nikola Grcevski @ Grafana / OpenTelemetry** 51:29 Yeah, well, there's a bunch of LLMs that are so tiny, like the nanomodels and our OSS, we can even run an actual LLM that responds back. The only challenge is that probably the answers will vary. I mean, some of these, even with temperature zero.
They still give you different answers, each time you call, so…
**Tyler** 51:52 Yeah. Which… maybe a feature. Yeah. Maybe it's also, like, you don't want… you want something consistent, I don't know. Yeah. Yeah.
But… Well, cool, yeah.
Awesome. Alright. Any other topics? Otherwise, we can probably end the meeting here.
Cool. Oh, it was good seeing you all. Thanks for the discussion. We will see you all in a week's time, or asynchronously. Till then.
**Nikola Grcevski @ Grafana / OpenTelemetry** 52:22 Bye now. Bye.
