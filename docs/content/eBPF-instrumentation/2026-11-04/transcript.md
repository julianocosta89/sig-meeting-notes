SIG: eBPF Instrumentation
Date: 2026-11-04
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Mike Dame (Odigos)** 00:20 Hello.
**Nikola Grcevski** 00:25 Bye.
**Tyler Yahn (Splunk)** 00:47 Hey.
**Mike Dame (Odigos)** 00:49 Meeting.
**Gregor Zeitlinger** 00:50 Owl!
**Tyler Yahn (Splunk)** 00:52 How's it going?
Yeah, he all set for KubeCon?
**Mike Dame (Odigos)** 01:01 I think so.
We've been running through our talks, me and Rafael. I think we've got them pretty down.
**Tyler Yahn (Splunk)** 01:08 What, what day is your talk?
**Mike Dame (Odigos)** 01:10 We're doing Observability Day, and then we have one on Tuesday at KubeCon, so get them done early in the week.
**Tyler Yahn (Splunk)** 01:17 Nice. Way to go.
What, what time on Tuesday?
**Mike Dame (Odigos)** 01:21 I think they're both, like, in the afternoon.
**Tyler Yahn (Splunk)** 01:25 Oh, okay.
**Mike Dame (Odigos)** 01:25 Good question.
I'll put the links to them in the,
**Tyler Yahn (Splunk)** 01:36 But yeah, that's a good idea, yeah.
Yeah, I don't know if I'll be able to make that talk, actually, if it's in the afternoon. I've got, like, booth duty, but if it's, like, later afternoon, then I might be able to make it.
**Mike Dame (Odigos)** 01:50 Yeah, we should… you have… you and Nikola have a talk, too, on observability Day, right?
**Tyler Yahn (Splunk)** 01:56 Yeah, yeah, I think it's, like, 11? 10.30 or something like that?
**Mike Dame (Odigos)** 02:02 Yeah, we should write all of these down that we've got.
**Tyler Yahn (Splunk)** 02:08 Yeah, and I saw, Antonio, as well, has, like, a lightning talk? Or maybe, I can't remember, something like that, but essentially it's like.
another OB talk as well, but yeah, we should try to get a list going.
**Nikola Grcevski** 02:19 Yeah, he's on the psyllium day. I think he got in.
**Tyler Yahn (Splunk)** 02:22 Compared…
**Nikola Grcevski** 02:24 Explaining how OB can run with psyllium together, and what they do, and how they complement, right?
It's very cool.
**Tyler Yahn (Splunk)** 02:30 Yeah, yeah.
Yeah, I wonder if I can walk over there.
**Nikola Grcevski** 02:36 Hmm.
Yeah.
Actually, surprisingly, I proposed a similar talk I don't know, when.
And it got waitlisted, but I didn't get in.
**Tyler Yahn (Splunk)** 02:47 Oh, really? Oh, okay.
Yeah, he's a… he's at the Thousand Eyes group, so I'm sure he has, like, inns with the Silian folk as well.
**Nikola Grcevski** 02:57 Yeah.
Double, yeah.
**Tyler Yahn (Splunk)** 02:59 I'm not saying something fishy's going on, but I'm guessing some back shoveling was happening.
Yeah, I don't know. I imagine it's a great talk.
**Nikola Grcevski** 03:09 Yeah, for sure, for sure.
**Tyler Yahn (Splunk)** 03:14 Well, cool. It looks like we're at Quorum, about 3 minutes past. I'm gonna… start… sharing my screen here. If you haven't yet, go ahead and add your name to the attendees list, and if you had agenda items you wanted to talk about, go ahead and add them there as well, and yeah, we can… Jump in here in just a second.
Cool.
So, to start us off, I wanted to ask about next week's meeting, this SIG meeting, do we want to cancel it?
It's, I think a question for the European folks, whether you wanted to meet next week or not.
Maria, I see you're talking about your muted.
**Mario Macias** 04:01 As you prefer, I mean, I can join, but I guess you… if you… most of you are in KubeCon, maybe you don't have time to… to… to join the meeting. Maybe you have other… better things to do, so… If most of you is going to be in CubeCode, we can cancel it.
**Tyler Yahn (Splunk)** 04:21 I think 4 of us are gonna be at KubeCon.
Anybody else?
**Nikola Grcevski** 04:28 Yeah, so you can still run it.
So we just need somebody to lead it.
**Mario Macias** 04:33 Okay. Hmm, yeah, then if all leaf, all is good.
**Nikola Grcevski** 04:37 Mario, you're volunteering.
**Mario Macias** 04:38 Yeah, yes, of course, of course, yeah, let's, let's keep it, and then, yeah.
**Nikola Grcevski** 04:44 Great.
**Tyler Yahn (Splunk)** 04:46 Okay, yeah, that sounds good.
Perfect.
Okay, then yeah, well, Please show up again, next week to everyone on the call.
Okay, moving on, next up I wanted to call out, some cleanup from the post-V1.
Merge, there's a docs PR here for updating the, documentation to the 1.0.
It still needs review, Dame, Mike, just approved it. Mike, I, did respond to this.
I didn't mean to be too harsh on this, I just realized that, like, all the changes I was making to the… I was like, this just is out of scope, so I was just gonna do another one. I forgot to leave a comment saying I was gonna do that.
**Mike Dame (Odigos)** 05:33 Totally, I just… I just wanted to make sure that I didn't come across this.
**Tyler Yahn (Splunk)** 05:36 Too much of that.
**Mike Dame (Odigos)** 05:36 Like, push it, yeah, so we're all good, yeah.
**Tyler Yahn (Splunk)** 05:38 No, okay.
**Mike Dame (Odigos)** 05:39 I'm happy to help out with this, too. I think I wrote the Auto SDK docs, so, like, you know, if I… since I'm the one complaining about it, I'm… definitely willing to… I think that there are definitely updates that should be made, like, it refers to the Go Auto project still as being, like, the main place to use it. So that's not right. So definitely stuff that we can do to that, and especially now with OBV1, we want to make sure that The right things are pointing people there, so… But otherwise, looks good. Yeah, happy to help, too.
**Tyler Yahn (Splunk)** 06:11 Okay, yeah, that sounds good. Yeah, happy to review the PR if you wanted to come up with it, otherwise it's probably gonna be a post, coupon thing for me, so… Yeah.
But yeah, otherwise, just need reviews from other, code owners.
On the doc update here.
**Nikola Grcevski** 06:27 There's a comment related to this on our channel, on the CNCF channel, somebody saying, it's good that you guys went 1-0, but the README still says Whatever. So, we need to upgrade the remake.
**Tyler Yahn (Splunk)** 06:42 Good, good lead in there, Nikola. So then there's also this PR.
**Nikola Grcevski** 06:46 Oh, okay.
**Tyler Yahn (Splunk)** 06:47 That updates the README.
**Nikola Grcevski** 06:48 Yeah, updates.
**Tyler Yahn (Splunk)** 06:49 Yes.
A few different things. Our versioning policy as well, needed to get updated. This updates, AI agent docs as well, saying that, like, you know, we're in a post-V1 phase, compatibility, guidelines need to be followed as well. So yeah, this is kind of like a docs cleanup for our site as well.
But yeah, please take a look at this, as well. This is, should be updating things.
Appropriately, if I miss things, please call them out, and I'm happy to update this again.
**Nikola Grcevski** 07:23 Nice.
**Tyler Yahn (Splunk)** 07:24 But yeah, thanks for calling that out.
Then, after that, I did an audit. So, one of the hard things is, like, once we get the 1.0 out, it kind of is, like, backwards, in, like, versioning history, because, like, it seemed like main was gonna be behind the 1.0, but you gotta remember, we tagged the 1.0 on the RC, so all of the things that happened after that tag, for the RC2, like, are considered still unreleased.
So, what I did is I did an audit of what things are going on here, and we need to do a cleanup.
We have a bunch of breaking changes that were actually merged, based on our compatibility guidelines, meaning that things like, the Go API, the exposed Go API, is changing in certain function signatures.
So, this, addresses all… all of the ones that I found here. And then on top of that, there are behavior changes being added to ConfigV1, so… Those are also getting reverted, and I wanted to bring these up as PRs. I see a bunch of questions, so yeah, maybe we'll pause here.
**Mario Macias** 08:35 Yeah. I… I'd say that some of… I haven't looked at all… all the PRs, but in some of them, I don't think they are… they are breaking changes. It's true that we say that we will not add more configuration to the… or more options to the V1.
And it's added, but, I wouldn't level them as breaking changes, because, for example, this root 53 resolution behavior.
is not breaking the behavior, it's just adding behavior on B1.
**Tyler Yahn (Splunk)** 09:17 Yeah, sorry, that was, misspoken on my part. So the V1 is… we have a development policy on the V1 where we've frozen the V1.
And that's what this is also addressing, is that development policy for the V1 no longer accepts,
**Mario Macias** 09:34 Okay.
**Tyler Yahn (Splunk)** 09:34 any sort of additional development, plus… and that includes, like, bug fixes, and yeah. I imagine…
**Mario Macias** 09:40 Okay, okay.
**Tyler Yahn (Splunk)** 09:41 I imagine, like, we don't have it documented here, but we probably should have it documented that we would accept, like, security vulnerability fixes, but, like, Yeah, I'd also be very surprised if we had a security vulnerability in our config. But anyways, like… Yeah, like, that was the… sorry, yeah, to clear that… clarify that, like, there are Go API changes that are breaking changes, but then there's… these are… these are just conformance with the development policy on the V1, and leaving it frozen.
**Nikola Grcevski** 10:06 Yeah, so we have to see if we can then… I mean, I… from our perspective, like, Rafana's side, I mean, we have… tons of customers now to migrate to V2.
fixes to behavior like, I don't know, something Route 53 is not working as it should be, I don't know, how do we achieve this, if… We have to keep V1 going a little bit longer, until everybody migrates.
No.
**Mario Macias** 10:38 Yeah, in the Rafana case, I mean, we can still maintain this, this compatibility layer at the Vela side, so it shouldn't be a big issue.
Yeah, mmm… Yes.
**Nikola Grcevski** 10:58 It's possible, always. If it's possible, kill cases, yeah.
Unless we have to figure something out.
**Tyler Yahn (Splunk)** 11:06 So… I'd love to hear a little bit more about, like, why… what's keeping you on V1, right? Like, the goal… the goal here for this configuration development is also to help motivate that migration, right? Like, it's…
**Mario Macias** 11:21 Hmm.
**Tyler Yahn (Splunk)** 11:22 It's unfortunately painful, but, it's also one of the things that says, like, you know, like, if you want the new features, we do want to be putting them on V1. I know that I have a list of, I think, like, 10… or so features or portions of the configuration that are not compatible right now, that are still actively trying to be fixed, are those the things that are blocking you recommending the full migration? Or… I think I… yeah, just, like, I'd love to better understand.
**Mario Macias** 11:47 Yeah, no, from my side, there's no reason saying I will not recommend, but it's some reluctancy of some users already having everything configured. I'm not talking only about Vela users. OB users already have the V1, so… migrating to V2, even if we provide Some, very good tooling.
Yeah, it requires some actions on their side that, you know, there's always something more critical to do before, but yeah, of course, at some point, they could get enough incentive to migrate to V2 if some features stop working.
**Nikola Grcevski** 12:34 Yeah, so the main challenge is that, yeah, we can't force them to upgrade.
We can try, but, they, they will complain that… Whatever, new features… new features are good, because then we say, no, that's only available, so you have to migrate your config to V2, and that works, but… like, small additions to existing stuff that existed now are like, oh, if you want to use that additional thing for Route 53, you can't. You have to move to V2, and for us, it's mostly just, Fixing functionality that was not there.
It creates a little bit of a… friction.
And we do have quite a bit of customers that need to migrate over. So, Yeah, we don't have a conversion path, or a compatibility conversion, or something that will help them get there. Also, then, the bad thing is that All the… they now just use agents to do this work, and Agents handle our V1 config really well.
I don't know how well they handle V2. Whether it's a training thing, maybe it just takes time to catch up.
**Tyler Yahn (Splunk)** 13:49 I mean, from my experience, I've definitely seen it.
I don't know how well it handles V1, to be honest. I've seen it handle V1, or V2.
**Nikola Grcevski** 13:59 Jason?
**Tyler Yahn (Splunk)** 13:59 Pretty successfully, but, again, like, your mileage may vary, like, what model are you using, what…
**Nikola Grcevski** 14:04 Yeah.
**Tyler Yahn (Splunk)** 14:05 what, you know, harness you're using. So, like, I don't know there. There is the migration tooling that I have, we have in the upstream project, here in OB. So, I would be definitely interested to understand if that's not satisfying, like, the needs of your customers.
in, like, their journey to migrate to the V2, like, it should be, like, obviously, like I said, like, there are caveats, there's, you know, I think something like 10… things that you just can't migrate, they're edge cases, they're not, like, you know, main configuration. But yeah, like, if, you know, you are finding that our customers are going, like, those are not edge cases, those are, like, you know, blockers for us, like, I would really want to understand that, I think, a little better.
I… so… I mean, I get it. Like, I also get, like, you know, migrating configuration is not, it's not a zero-hour, you know, thing, but it's also one of those things that, like, I think this is why we want to be doing these sort of, like, incremental fixes, incremental things, to try to help motivate these sort of, you know… if you really want this fixed, you need to do this, like, at this point, it's, you know, behind the times, like, you need to do this. Eventually.
I am going to say, like, eventually we are going to want to deprecate the V1. Like, I don't think that we're at that point yet, like, I think we're… it's, you know, months away, maybe. For a V2 of Obi, I think that we would probably want to have V1 removed at that point, but… So, it's more about just timing, and I think at this point, like.
you know, if customers are just hesitant because, like, they just don't have the time, literally, they don't have the time just, like, to deal with it, like, I get that. But if they're hesitant because, like.
they went through… they tried the migration, and, like, they had problems. I think that's… that's what I really want to hear about. Unfortunately, I, like, I don't… you know, that… don't think that should be the case, but, like, if it is, that's the… that's definitely problematic.
**Nikola Grcevski** 15:55 Yeah, as people start migrating, I think we'll find those problems.
We just, yeah, from our perspective.
Yeah, this just can't happen overnight.
**Tyler Yahn (Splunk)** 16:07 Yep.
**Nikola Grcevski** 16:07 So we need to… I mean, we made, internally a big push to make sure that OB, Bayla included, so work really well outside of Kubernetes, and that's been our mission, so customers that are waiting for the support.
And… So for that, that's critical to happen, and for now, we just have to support the V1 to make sure that still kind of works okay.
With, with this approach, because, we can migrate them and introduce them do new things. It says, oh, you want this to work well in non-Kubernetes? Well, you have to use v2 config, and… change everything you do internally to match it.
So we're in this sort of transition mode. I'm hoping that it won't be too long, but yeah.
I think it starts with us, we're gonna have to change our… Helm charts and everything else we have to start going with V2, and people slowly start to get, okay, well, the config is like this now, change the docs, and… Yeah.
Mostly. Yeah, I've definitely…
**Tyler Yahn (Splunk)** 17:21 tried to change the docs as well upstream, to use V2, I might have missed things, like, in our local docs, we have a big backlist of things in follow-up, so, like.
I don't think we're there today in saying that, like, you know, we can deprecate V1. Like, there's definitely a lot of tasks. I wouldn't want to do that until we can say, like.
There are no blockers, but… I also want to move forward in that progress.
**Nikola Grcevski** 17:46 So do we, so do we. Yeah. I mean, it's just, like I said, it's in between, it's traditional, we just have to somehow make it through.
Yup.
**Tyler Yahn (Splunk)** 17:59 Gregor and Nimrod?
**Nimrod Avni** 18:04 Wanna go ahead, Clare?
**Gregor Zeitlinger** 18:06 Yeah, sorry, I just needed to find the unmute button.
to make this easier in the future, maybe we can just add a test that flags incompatible things. In Java, this is working really well.
**Nimrod Avni** 18:24 like the GO contract, I guess? Or the…
**Gregor Zeitlinger** 18:28 that is supposed to be not done, just don't rely on human eyes catching it.
**Tyler Yahn (Splunk)** 18:35 Oh, I see what you're saying, sorry, for, like, yeah, these compatibility docs and that kind of thing, like, yeah, yeah. Oh, 100%, I agree. I think that's a great suggestion.
I… there's actually even tools for, like, the Go, like, Go Release, I think is a good tool that we use in, like, the downstream that checks this, but it's a manual process. Having an actual test… Would be very helpful, like you're saying.
I… if you wanted to open an issue to track that work, that'd be great. I probably should have opened this as well, because it was… I had that same thought, I just… yeah.
**Gregor Zeitlinger** 19:07 No, I did not want to volunteer, just wanted to.
**Tyler Yahn (Splunk)** 19:10 No, sorry.
I don't mean to do the work. If you want to open an issue just so that it doesn't get lost, I'm happy to add this as maybe, like, a next year's goals or something like that. I'm happy to… I'll work on it as well, like, this sounds really interesting.
**Gregor Zeitlinger** 19:23 Okay.
**Tyler Yahn (Splunk)** 19:24 Yeah, thanks, thanks for bringing that up, I totally forgot about that part, yeah.
Nimrod?
**Nimrod Avni** 19:32 Yeah, so we also, in CoreLogix, we're using V1 currently, and, like, we're telling our customers to use that, and we do want to migrate them to V2, but I agree, for example, with Nikola's point and Macias, I think we should… first do it, internally, let's say, in our, like, suites. Like, every integration test, I guess we should say, like, we use the V2, so, like, we can say that, we can say that we… we use it. And also, I think… I think you also, like, opened a lot of issues on the V1 to V2 migration, which, from what I saw, some of them are done, some are not, and… Maybe we should kind of wait until it's fully stable to say, like, until there's no gaps that we can find in the migration.
To stop adding… not even new features, but I don't know, if there is… some… I don't know, some critical setting that people need, like a knob that people need to turn on and off for, let's say, performance or, security, or something like that, maybe we should consider adding it, but new, like, completely new features, let's say, like Mark's, error tracking or something like that, that shouldn't go in V1. I think maybe that's a…
**Tyler Yahn (Splunk)** 20:51 Yeah, to be… to be blunt, I'm finding that kind of frustrating.
Because, I've been working on this for well over 6 months at this point, trying to track on this.
I've done a lot of work in this process. The issue that you're talking about in migrating our integration testing has been open for 3 months. I'm more than happy to have you pick it up in that time period and contribute to it. Like, I… I'm only a single person, I can only do so much.
there's a lot of, boogeyman, like, things being brought up here that, like, there are faults with Configv2.
I've identified the things that I have.
And I can tell you what those are, those are documented, those are really well documented. If you have other issues with it, like, I think that that's fine. But, like, if now you're telling me that, like, you're just now evaluating this.
And, you're not sure if we should stabilize it, like, that ship sailed last week. Like, it's stable, it's already out, we have compatibility docs, we have versioning docks.
That claim the stability, and it's… it's… it's done at that point.
Like, I don't know if that was not clear, it wasn't communicated properly, but like… We're, we're, we're past that.
**Mario Macias** 22:07 Yeah, no, I think you, you did it great. I understand your frustration.
In that case, it's just when we… we have been discussing this topic many, many times. It sounds great, but we have found some rough edges we didn't consider at the beginning that are delaying our, our, our, our adoption. I mean, in our plans, there are still the… the… the adoption, but… Yeah, I don't… I don't want you to feel that we are just saying, oh, this is not valid, and we don't… we don't want to… to do that. It's just… in our case.
We will need more time for the final rollout of V2.
**Tyler Yahn (Splunk)** 23:00 I… yeah, that… 100%. Like, I don't wanna… I don't wanna rush. I don't wanna say that, like, tomorrow, let's get rid of V1. I'm not trying to say that.
I am saying that, like, not to you, Mario, but to Nimrod, that, like, if you wanted to take your time as well, and that morale as well, like, go for it. Like, that, like, I totally get it, like, especially from a customer's perspective, you want to try to minimize that, like, drift.
But… like, Yeah, like, if there are things that you see and you want, like, I need help. Like, I can't just do this all on my own.
**Nimrod Avni** 23:37 I agree, and again, didn't mean anything by it, like, I'm… I'm saying, like, we also need some time to get it, I guess I also want to contribute to it, like, I tried looking around, like, doing the migration from the integration test from V1 to V2, then I saw, like, I ran into some of those issues that are open.
So I'm saying, I guess I could… I guess those are kind of blockers for doing, at least for our internal, migration. I can take some of those on.
And yeah, like, I'm super excited to get it, just, like, I think the… we need to probably… at least for helping our customers, and I guess some Grafanas and whatever, I guess we need to make sure the full tooling and stuff, like, especially for new customers, I agree that you should start with V2, and definitely no worries there. Maybe for just only the migration part, we just need to make sure it's tight, but I can also have a look at some of those issues as well.
**Tyler Yahn (Splunk)** 24:35 Yeah, I'd appreciate that.
Batia.
**matt** 24:39 Yeah, so that in the agenda we have some… something related to ContribFest.
Maybe we can use that to start migrating some tests?
start using some external help there. Since it's not a hard thing to do, but it's a long one. There are a bunch of tests, and Maybe you can use some help there.
**Tyler Yahn (Splunk)** 25:04 I think that's a fantastic idea, yeah.
Thanks for… thanks for bringing that up.
I'm happy we can jump into that. I think it's the next item.
Yeah, let me… let me jump in there. And I don't wanna… I did want to get, any other feedback on the V1.
Before we jump into this next one, but we can jump in.
Yeah, okay, cool. So, yeah, as, Macias pointed out, we are having a Kitchen Fest at this upcoming KubeCon.
This… suggestion is actually a really great suggestion, because, it's a lot of work, but it's also splittable into, like, really parsable things. We're looking for issues that are easy to understand and small enough that they contribute, and usually, you know, that means something that you could probably solve and… 10 minutes, maybe 15 minutes, with full, like, understanding of what you're actually trying to solve here, so I think that this is a great, great task. I am asking if, if you, as a maintainer, or as an approver, or anybody else, would like to contribute to help, build these issues.
Yeah, I think Mattia's suggestion was great. We need those issues. I'm actively looking to try to make some myself.
And… there are some things that need to be done.
They need to be tagged with the ContributeFest label. I don't know if it exists in the repo yet, I can make sure it is by the end of the meeting.
One of the other things that they can be doing as tasks is they can just do verification tasks, so if there's, like, bugs in the repo that you think are small enough and they just need verification, like, doing a reproduction is all that they need, we can also add a needs verification tag.
This is also very helpful to those users that, like, maybe don't have a setup, that they want to do coding tasks, they maybe just want to do something like this.
Their completion would be, like, an issue comment, something like that.
They need to be unassigned, so if they do exist, and they have, like, a stale assignee, unassign them. And then… The last thing is, is we don't want to get them, sniped by people outside. It's gonna happen, it's just what it is. But essentially, try to be vigilant in understanding that, like, if people are submitting work before the event, just to close the pull request with a comment saying that, like, we're holding these off for ContribFest.
But yeah, that's a great thing to bring up. I would love it if other folks would be happy to open up issues, that'd be great. For those that are attending KubeCon, like, I guess only the maintainers, please come to the event. Like, this is great to see people and have your face, like, recognized in the community, but also just to help those new, new people.
To solve some of these issues is kind of a big one.
**Nimrod Avni** 27:47 Yeah, I opened a bunch of issues in the past, like, week, and they get sniped really quickly, so I think we need to… there's some really… a couple new contributors, picking up tasks really quickly, so I guess we need to… For those, make sure that we mark them… to not work on them until the ContribFest.
**Tyler Yahn (Splunk)** 28:07 Yeah, that's a good point. We were trying to come up with a different plan, which is why this is kind of a late notice for this, but… The automation to try to get this out, like, the day of was not gonna happen, so… We're just gonna have to go with, public communication on this, yeah.
But yeah, that's a… it's a… Last time I ran this thing, it was a hard thing as well.
Yeah.
But cool.
Okay, moving on, Nimrod… or, I'm sorry, Nikola, you wanted to talk about local Linux host, Instrument Everything Mode.
**Nikola Grcevski** 28:40 Yeah, I wanted to bring this up to see… I mean, we prototyped it, or actually have it working in Bela. I wanted to see if this is a good suggestion for… to move upstream in the Obisig. I'll explain the feature a little bit.
Imagine you're dropping an OB, or maybe a full OTel Instrumentation image to somebody's VM. Like, we're not talking Kubernetes, we're talking just pure Linux host. People are baking it into their delivery of the VMs.
And… You want them to not have to configure which service.
Is to be instrumented.
Now… consider what we do with the Helm chart, which is, say, instrument everything at Kubernetes level, and it's smart enough, because you just go after every pod, it excludes, known services from kube system and whatever.
So how would we achieve the same experience on just bare-bones Linux host? When you think about it, like, OB will instrument SystemD, and… You don't want to instrument System D and create all this noise. So we thought about this, and we created this mode where, actually, we use Mike's dynamic pit instrumentation.
So, it's orthogonal to our selection criteria, and it sort of creates this mode, which it says, instrument everything, and if you use it with any selection criteria, it just says no.
sort of one or the other. Either you pick services you want, or you just let us instrument by the smart mode. And what the smart mode does is, essentially, any application that does any socket activity gets picked up, so not just listeners, but programs that will do client calls, like something pushing on Kafka Q, it just does outgoing sockets.
And it excludes, sockets that are done by services that are running as root.
Because there's a bunch of cylindic system services that do socket activity, but they run as root. Unless… you're trying to bind port less than 1024, because in the past, Linux permissions disallowed you to, bind ports less than 1024, unless you were root. So traditionally, if you wanted to install Apache on a Linux host and have it listen on 80, you would have to run it as root. So it has some sort of, like, a heuristic mode, which And my experience does pretty well. When I run it on my really busy Linux machine, where I have all sorts of things running.
Claude, and… VS Code and all sorts of things, it just picks up the right services, so… We have this mode, I'm just asking Do you guys want it?
bring it up. I mean, obviously, config V2. No, Config V1. But it's just an option, so it's effectively, it's like, yeah, instrument everything, host mode.
Sort of thing.
**Mike Dame (Odigos)** 31:47 Would it be nice if so, like, we'd be kind of dogfooding the dynamic selector, then would that be implemented basically the same way, and it'll be off the shelf, which is good for us to validate that contract.
**Nikola Grcevski** 32:00 Yeah, it uses a separate eBPF program. The eBPF program tracks sockets, started and created, and drives The dynamic bit selector.
Essentially, it sort of caches things as well. It's kind of complicated to explain. I can propose a PR, or a design doc, or whatever you like.
To bring it upstream, but… Because it's the kind of state that, like.
is anything that opened a socket at any point in time gets recorded, so you see the PID live, but you kind of ignore it until you see it speaking. Once you see it speaking, when it gets sockets going, then we're like, okay, well, you're interesting.
Are you on the route or non-root? So we check the user, and then we push it down the pipeline for dynamic bit selector to get picked up.
Yeah, so it sort of, like, watches all processes, but… Waits until they start… Talk into sockets.
**Tyler Yahn (Splunk)** 32:59 I mean, it sounds awesome. I'd… yeah, I'd be interested. Yeah, and like, if I… Yeah, that sounds great. I'd be interested in seeing this.
**Nikola Grcevski** 33:10 Okay, alright, so I'll bring it upstream. One less thing to worry about.
for breakage, but yeah, it was really… the dynamic play selector, I have to say, was perfect for this use, because it sort of, like, it's a completely separate way to kind of drive the pipeline by just selecting, yeah, this bit got interesting now.
let it go, or this bit died, and now it's no longer interesting, and so on. So, it was really good. And it worked out of the box, which I was really happy. I didn't have to fix anything in Obey, it just worked.
Yep.
And it's a perfect use case, like you said, Mike, for…
**Mike Dame (Odigos)** 33:47 That's awesome. It's an interesting use case, too, for, you know, that's an application of it that I honestly didn't think of, so… Glad to hear it worked.
**Tyler Yahn (Splunk)** 33:59 Cool, yeah. I'm guessing you got a PR incoming on that one, Nikola?
**Nikola Grcevski** 34:04 Yeah, I'll open it up, probably after KubeCon, or whatever. Lots of things to do before then, but the code is in Bela, I mean, everybody can look at it, it's not like we're hiding it, but I wanted to see how it works first.
And I think, yeah, I think it will go really well, to be honest, with the packaging sync.
Packages, of course, they packages with Obi. They're planning to just install OTel on a random Linux machine, right?
nobody will have a chance. Like, the injector works out of the box, instruments everything it can by setting environment variables, and I think it would be… mode like this would really go well with that.
install OTEL, and things just light up. You don't have to pick and choose or anything. It does the right thing out of the box.
Should we go?
**Tyler Yahn (Splunk)** 34:51 Yeah.
That's awesome.
Okay, cool. Mike, you wanted to next talk about embedded extension points?
**Mike Dame (Odigos)** 35:01 Yeah, this is, another proposal. It's long, but it's kind of… I think it's interesting.
Kind of builds on… dynamic selector we were just talking about as more of a way for embedders to, extend and customize OB, and less on the selection side and more on what it is actually, producing. So, deeper into the pipeline than the selection area, and it really kind of focuses around, custom protocol detection.
This is something that we've actually… so I had the SunRPC protocol that I, like, submitted upstream before, and even since then, we've had, like, another 4 or 5, like, very niche, protocols for, like, healthcare and finance, and even, like, custom protocols, so… Kind of propose a way to… Same idea through that Instrumenter.run, add options to define your own, user space protocol detection. At the kernel level is a little bit, I think, out of reach right now, but for simple, you know, based off of the, like, generic, tracer.
Protocol detection itself is not that… not that far out of reach. Kind of… Along with that comes, you know, being able to register custom swarm nodes to, you know, enrich data off of the custom protocols that you detected. And all of that sort of centers around adding a more generalizable set of attributes to the request.span object itself, so… I believe all of this, you know, it's kind of an… like, trying to keep it along the same lines as Dynamic Selector when I added it, it's just, you know, it's its own hop path and shouldn't… be conflicting or affecting the default use modes right now, but I do think that, you know, besides our own use cases, it'll probably give, you know, a lot more reach for OB2… address any sort of custom protocols that people have that might not fit upstream or not, so… take a look through it. I could start drafting some PRs, or give some more examples of stuff that… that we've done to… That would be good for it.
But otherwise, yeah, it hopefully shouldn't be too invasive on anything else.
Yep.
**Nimrod Avni** 37:31 Sounds… sounds really cool. Yeah, I wanted to… maybe, I don't know if you're thinking about also doing HTTP, like, other protocols based on HTTP that are kind of custom, like the way we do, say, Elastic and a lot of the Gen AI stuff.
I don't know if it'll be in the same kind of extension, a different… because you might wanna… already receive, sort of a kind of parsed HTTP packet instead of just raw binary, raw, like.
But that can be even, like, a follow-up. I don't know, just game time.
**Mike Dame (Odigos)** 38:09 Yeah, I… I mean, that's… that's a good suggestion. If you, you know, want to add that to the thread, I'm really… like, I'm trying to look at the simplest way to start dropping this in. I'm just really, like, I love the idea of OB Framework as, like, an extension platform for, you know, embedders, like, like what we're doing, and what it sounds like, Bela's doing with the dynamic selector, so… This seemed like a natural place to… like, I've… even with Dynamics, like, I was like, this kind of approach could be extended to more than just selection at some point, so I'm open to any suggestions of, things that can make it easier, but just to kind of kick off the discussion of possibilities, of areas that we can make it more pluggable.
And something that would benefit at least our use case, so we'd have one user from it. We don't have to carry these patches for… like, all the hard-coded detection that we have right now is… it just doesn't seem sustainable to grow and try to detect every protocol on Earth, especially, like, some of these ones that we've had users ask for, like.
I have never heard of them, and they're apparently, you know, very legacy things, Like, there's, like, custom healthcare protocols, like… They're, like, sending, you know, patient-admitted messages. But even then, you know, some company, some user could have their own custom protocol, so… Not to get too hypothetical, but… You kind of start to see the trend of, like, okay, some way for people to tie into this might be, a good way to… Spread it, make it usable.
But that's the idea, at least it, Yeah, it all kind of centers on… being able to customize that request.span object that OB's producing, and if we are able to do that without You know, breaking our contract, and… Should be.
Pretty easy to do.
Sounds good.
Yeah, take a look, leave some comments, let me know if, you know, thumbs up, down, I can start doing some PRs around them, but, I know we're also all pretty busy going into next week.
**Tyler Yahn (Splunk)** 40:22 Perfect. Awesome. Sounds good.
Yeah, we'll definitely need to take a look.
Thanks for bringing it up.
Okay, looks like we're at the end of the written agenda.
Any other topics folks had that they wanted to talk about?
Any other cool projects that you're working on?
**Gregor Zeitlinger** 40:44 Yeah, I have one, question. I thought we would be… Running out of time.
So, I have, two branches that are for bigger stuff. One is for the dynamic instrumentation, the other one is for Mies.
And on both of them, I wanted to update main, and the first time, it failed for some weird CLA stuff, and on the second one, it's now running in, into some issues because, some tests fail. I presume it's, flakes, and Trask had a suggestion on, on the Slack, that I didn't really understand, but, the discussion fizzled out, so I wanted to bring it up here again.
I don't know if you looked at it, at what, Trask said, Tyler,
**Tyler Yahn (Splunk)** 41:46 I didn't really understand it, to be honest.
**Gregor Zeitlinger** 41:49 Okay.
**Tyler Yahn (Splunk)** 41:50 Okay.
I thought it was just me, okay.
Yeah, let me see if I can try to find it again,
**Gregor Zeitlinger** 42:04 Maybe this is totally the wrong direction, and I should be doing something, else instead, I don't know.
**Tyler Yahn (Splunk)** 42:12 Maybe Edge Case… Oh, I see.
**Gregor Zeitlinger** 42:21 I should be running it in my fork, and we review it there. I'm just thinking out of the box.
**Tyler Yahn (Splunk)** 42:28 Yeah, I think that actually might be what he's saying to do here.
I kind of missed that, like, yeah, it's got, like, a four… yeah, I think that's what I'm getting from, like, him putting your first, or your repo name before the branch name.
Allow approver branch.
**Gregor Zeitlinger** 42:43 Oh, I thought this would be the branch name.
But maybe I didn't get it right.
**Tyler Yahn (Splunk)** 42:50 I might not be getting it right still, to be honest.
I don't… I'm not 100% sure. So… so the… the current CI failures are… Those are just flaky. The CLA thing was way more confusing for me. Like, is this second approach to merge in main, like, not having CLA failures?
**Gregor Zeitlinger** 43:13 And this is a different branch, it's the same approach, so I think I was just on… I just started off of a later main, and that, did not have the affected commit.
**Tyler Yahn (Splunk)** 43:27 So, one of the other things that, I mean, I'll just say it, like, is I think that, like, the maintainers here should have access to be able to push to those branches.
So, it may just be one of those things that we do outside of a PR, where we just merge main into the branch, and then just push to the branch itself.
I don't know… like, I don't know why the CLA… and essentially, like, what'll happen there is it'll just… it should move the base, you know, commit that it's forking, or, it's branching from, but, like.
**Gregor Zeitlinger** 44:00 cat ride.
**Tyler Yahn (Splunk)** 44:01 Yeah, like, I don't… Obviously it's not gonna be reviewable by the rest of the community, but, like, this is also kind of like a maintenance thing for a feature branch, so I'm like… Maybe just, proposing that?
I don't know what folks think of that. Other maintainers?
**Gregor Zeitlinger** 44:19 Yeah, that's definitely an easier possibility, if we agree that this is the way… how we should do it.
**Tyler Yahn (Splunk)** 44:29 Macias Nimrod… Rafael, Nikola, Mario, Mike?
Thoughts?
I got a thumbs up.
Can't see it.
**Gregor Zeitlinger** 44:40 I don't have the permission to do it, but I can ask one of the approvers to do it. Okay, cool, thanks.
**Tyler Yahn (Splunk)** 44:50 Yeah, that sounds like a good idea. Let's just go that way, because this is… I liked your approach, it's just, like, this complication is just kind of… I don't know what's going on there, to be honest.
**Gregor Zeitlinger** 45:00 Little bit artificial, yeah.
**Tyler Yahn (Splunk)** 45:02 Yeah.
Yeah, exactly.
Okay, yeah, let's, let's do that. Let's, yeah, let's just, have one of the maintainers, merge in main and push it to the feature branches, and let's, yeah, let's move there.
Okay, anything else folks wanted to talk about?
**Nimrod Avni** 45:21 Yeah, I wanted to say that I don't think Mark is here, but the work he's doing on the error capturing sounds really cool, and could… Like, like, I tried to think about, like, how we can actually do it… For me, like, errors is something that's very, like, user-oriented, like, he needs to specify what is an error, like, actually running a log, but if we can do it just from, assuming exceptions inside… on the inside, like, known frameworks and stuff, we can really bring… Like, it's not only, like, uncaught exceptions that are really rare, it's not actually, like… Application errors, that sounds really cool.
**Nikola Grcevski** 46:01 Very cool, yeah, I agree.
No.
**Tyler Yahn (Splunk)** 46:04 Yeah, I, I'm also really interested in this event pipeline, because I think it, like.
errors are cool, but I think it's actually going to be really useful for a lot of things. So, yeah, I agree.
**Nimrod Avni** 46:18 We can become log shippers now, Mattia. Prepare.
**Nikola Grcevski** 46:22 Yeah.
**Tyler Yahn (Splunk)** 46:24 Oh,
**Nikola Grcevski** 46:25 You'll see from me, you'll see sampling stuff.
I've been on a mission to fix their sampler.
Because, actually, my end goal is to do something cooler with sampling.
I don't know if this can be extended across OTEL, but I think the payload extraction you added, Nimrod, with… Ability to keep samples, even if they're partial, of errors or slow requests?
it gives a lot of power to debug problems in production. So you can have your sampling rate at 1%, but because internally in Bela, we have all the metrics, we know exactly how slow is a particular Route?
So we know the baseline. So if something is, like.
In the 95 percentile, you can configure it, say, give them everything that's 95% this low.
And we know that per each individual URL path.
So now we can say, no, this particular trace sample it, even though your sampling is not So, customers can configure And then… it's a partial choice, but… Where the payload's in there.
If we put it, then you can compare What does a good request look like? What does a bad request look like for an end user?
Or an error. You hit an error.
You can just override the sampling decision as they sample it.
and add the payload or something. So therefore, people can see why they're experiencing errors.
I remember when I was at Elastic, it was the hardest thing to do, is that somebody would say, oh, my cluster died, somebody sent their query.
And it just crashed the cluster and It's impossible to find.
what was the payload, and I had to imagine what the hell that was, and how to reproduce it, and see what we missed, and… And so on. So, Yeah, I think it'll be really cool. So, I'm on a mission there, so I've proposed a… but first, I'm starting with a PR to allow us people to change sampling strategies without having to restart, because I think that's really important.
Such that, you know, Imagine you needed to increase sampling because problems are happening in production, but then… Now you have to restart Obey.
to make that sampling decision, which means you have no telemetry for maybe a couple of minutes if you have a large cluster until it goes back and does all… finds all services, re-instruments them, and starts generating telemetry. It's just not a great state.
And it's a simple, just, toggle, right? For us, it doesn't matter.
**Tyler Yahn (Splunk)** 49:09 that we could support things like Jaeger's remote sampling?
**Nikola Grcevski** 49:11 Yeah, I don't see why now.
**Tyler Yahn (Splunk)** 49:13 Yeah.
**Nikola Grcevski** 49:14 Yeah.
**Tyler Yahn (Splunk)** 49:16 That's cool. Okay.
**Nikola Grcevski** 49:17 I mean, even, like, with OPAMP, you can just push sampling decisions, but I'm hoping that it won't have to be… I'll restart Anobi, just to change.
**Nimrod Avni** 49:29 Yeah, one…
**Nikola Grcevski** 49:30 2%, yeah.
**Nimrod Avni** 49:31 Yeah, I wanted to say I was interested, I was inspired by your PR to start thinking about it, like…
**Nikola Grcevski** 49:38 Basically.
**Nimrod Avni** 49:39 implementing OPAMP and, like, using your, like, hot reload.
**Nikola Grcevski** 49:43 joke, yeah.
It's all odd.
**Nimrod Avni** 49:45 I'll see if I can get something this week, at least some infrastructure stuff.
**Nikola Grcevski** 49:51 Cool, yeah, yeah, yeah, I think, some of these changes, we're restarting for no reason.
Adding a service or removing a service is such a… sort of like a normal situation in OB. So I think Sampler… I don't know if you guys think of anything else. Those are the two ones that I think are most important for me, like people running in production and just wanting to see more or less, or decided to instrument less or more.
But there might be other things.
Yeah.
**Tyler Yahn (Splunk)** 50:23 Yeah, this is a great place to start.
**Nikola Grcevski** 50:26 So I put up a PR for the sampler, toggling it on and off.
We're changing it without reload.
On top of the existing stuff.
But then I want to tackle, maybe, after KubeCon.
have a week after some off-site, but after that, I want to tackle this sort of more… like, targeted sampling, I don't know what you call it, but, that, together with the payload extraction, could be really, really cool.
maybe we start a spec or something to drive it up to SDKs as well, because I think, I don't know if all SDKs can capture payloads and stuff like that, but maybe they can.
I mean, even though it's partial trace, you didn't… maybe it was from a parent and came back as, don't sample this, and you sampled forward.
or anything after the fact, that when you've detected the problem. Still, I think with the payloads, it's really useful.
to debug why a slow request versus a good request.
**Tyler Yahn (Splunk)** 51:29 Yeah, I wonder… It probably… yeah, I don't know, maybe it's like a semantic invention?
Well, that's actually a big problem for OTEL, is there actually isn't specification on instrumentation.
So, like, our standard HTTP interpretation is governed by, like, semantic conventions, but, like.
**Nikola Grcevski** 51:47 Yeah.
**Tyler Yahn (Splunk)** 51:48 That kind of functionality you're describing may be separate, but…
**Nikola Grcevski** 51:51 Yeah, separate, yeah.
I mean, it doesn't fit in any of those sampler strategies.
**Tyler Yahn (Splunk)** 51:56 Yeah.
But I mean, that's the thing, it's like, it doesn't have to, like, be specified, right? It can just be a feature that.
**Nikola Grcevski** 52:02 You know, they…
**Tyler Yahn (Splunk)** 52:03 other… well.
**Nikola Grcevski** 52:04 and other SDKs, yeah.
**Tyler Yahn (Splunk)** 52:07 Yeah, like, we can find, like, like, the Go one stands out, that we could have that in our HTTP Instrumentation just added there.
**Nikola Grcevski** 52:13 Okay.
**Tyler Yahn (Splunk)** 52:14 So, yeah.
Cool. Yeah, that'd be cool.
Awesome.
Okay, well, I think if that's it, we could probably end the meeting here.
I will see you all in 2 weeks. For those of you at Coupon, I'll see y'all next week. But yeah, super excited.
Yeah, thanks everyone for all the help.
Talk to y'all later.
**Nikola Grcevski** 52:38 Oh, man.
**Rafael Roquetto** 52:38 See you guys!
**matt** 52:39 I'm blind.
