SIG: Go SIG
Date: 2026-08-06
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Puneet Singh** 00:22 globe.
**Tyler Yahn (Splunk)** 00:23 Hey, how's it going?
**Puneet Singh** 00:26 Not bad, weather is pretty good, so, yeah.
**Tyler Yahn (Splunk)** 00:29 Oh, yeah? You down from 40?
**Puneet Singh** 00:33 Yeah, it is, it is 26 off 27, so very decent, I would say.
**Tyler Yahn (Splunk)** 00:37 Yeah, that's great. Yeah, I could do that. I mean, it's still hot, but…
**Puneet Singh** 00:42 Yeah, happens, happens, like, 3 or 4 times in a month, so, so yeah.
**Tyler Yahn (Splunk)** 00:47 So yeah, now it's time to get outside and, go do all the outdoor things, right? Yeah.
**Puneet Singh** 00:53 Yep.
**David Ashpole (Google LLC)** 01:06 I hate…
**Tyler Yahn (Splunk)** 01:07 Hey, how's it going?
**David Ashpole (Google LLC)** 01:09 Don't know.
**Puneet Singh** 01:10 Boom.
**Tyler Yahn (Splunk)** 01:27 Cool.
Yes, I don't think Robert's… well, I know Robert's not shown up today. I don't know if Sam's gonna make it, but We could probably jump in here in just a little bit. If you haven't yet… No, yep, everyone's got their names on the attendees list.
Oh, no, David, missing you, I'll put you on there. And then, if you have agenda items you wanted to talk about, go ahead and add them there as well, and then we can… Jump in here.
-Oh. Did one happen.
**David Ashpole (Google LLC)** 02:07 Aska.
I feel like we should do, like, a little mini… I should probably unmute. I feel like we should do, like, a mini… Oh, not post-mortem, but, like, the fact that neither Sam nor I could actually do the release.
Because of the… I'm not sure what's up with being able to merge, like, the private branches, but I feel like we should get that figured out to make sure that we're not just, like, blocked on you being on vacation next time you go.
**Tyler Yahn (Splunk)** 02:40 No, you're not. It's not… I mean, I wasn't able to… I mean, technically, I am.
**David Ashpole (Google LLC)** 02:47 Okay, so you couldn't do it either, technically.
**Tyler Yahn (Splunk)** 02:49 Like, you actually have to go jump through some hoops, even as, like… like, you could have,
**David Ashpole (Google LLC)** 02:55 Oh, really?
**Tyler Yahn (Splunk)** 02:56 Yeah, like there was, like, there are steps you needed to do beforehand, where essentially you buy… you had, like, bypasses for all of our rules that would block, like, requirements, for you to actually do it, and then you just merge it with, like, bypasses. Yeah, so it's, like… Essentially, like, you take your admin permissions, and then you abuse it, and then you use that to actually merge it. So, it's a little sketchy, but… Yeah, that's the problem with, like, those private repos, is that, like, they are, great, because it, like, isolates everything, and puts it in an early, like, isolated spot, but, like, it also means that, like, CI can't run, by design. And so, our requirement for CI runs is, like, the main thing to get it into main, so, like, you can't… yeah, so you have to essentially, like… be an admin, go in, turn off, like, essentially, or allow yourself to… All the branch protection. Yeah, yeah, exactly, yeah.
So, yeah, I mean, yeah, it wasn't obvious, it still isn't obvious, exactly, but… Okay.
**David Ashpole (Google LLC)** 03:57 Well, now I know.
**Tyler Yahn (Splunk)** 03:59 Yeah, okay.
**David Ashpole (Google LLC)** 03:59 thought about that, I was like, you know, I wonder if I could do that, but that can't be the…
**Tyler Yahn (Splunk)** 04:03 Yeah, I know, like, the first time I did it, it was like, this is, like, super sketchy, like, I should not be doing this. And then, like, other TC members were like, no, that's how you do it. And I was like, oh, okay, like… Cool, alright, well, I guess I'll just keep doing that. But yeah, and I always seem to forget, because I'm always like, go there, and I'm like, how does this work again? So, yeah.
You're not allowed on that one.
**David Ashpole (Google LLC)** 04:25 So, when you're doing the release.
I won't… I wonder if we should… I mean, it's ugly, so maybe we shouldn't document it, but…
**Tyler Yahn (Splunk)** 04:35 Yeah.
**David Ashpole (Google LLC)** 04:35 You're doing the release.
you just, like, YOLO merge, the PR.
That's on the private branch.
**Tyler Yahn (Splunk)** 04:43 Yeah, because that's the other thing, it's like, the merge from, like, a security review, or a security advisory, like, private.
doesn't go through, like, it just goes straight to main, right? And, yeah, so the first step is, like, you have to actually be ready. Don't merge that until, like, you're ready to do the release, is kind of the key thing. But also that means that, like, you probably need to have, like, even if it's not your PR, like, go in there and try to, like.
run CI as best you can locally, you know, whatever that is. And then, then from there, like, you're gonna go into, like, the main repo. In the main repo settings, there are, like, not the branch protections, but the rules, like, which is, like, the new branch protections, In the rules, you'll find, like, a bunch of… like, I think there's two specifically that, like, reference, like, actions that you need to actually, like, talk to. One of them is the EZCLA, like, that's definitely one of them.
And you need to go in there, and you say, like, add a bypass rule, and, add, like, as a maintainer. Only allow, like, the maintainers to bypass this. And then… Yeah. Yeah, and then when you do that, like, it'll show, like, it'll still be, like, this big red thing that says, like.
**David Ashpole (Google LLC)** 05:53 Check it.
**Tyler Yahn (Splunk)** 05:54 Yeah, I've got this one.
**David Ashpole (Google LLC)** 05:55 on some other repos that I maintain, where it's like, I've seen that button before, but you basically go switch on the thing that lets maintainers bypass the rules.
**Tyler Yahn (Splunk)** 06:03 Yeah, exactly.
**David Ashpole (Google LLC)** 06:03 then you… Bypass them and merge without any precipice.
**Tyler Yahn (Splunk)** 06:09 Yep.
**David Ashpole (Google LLC)** 06:10 Do you kick off any CI jobs on main after merging?
**Tyler Yahn (Splunk)** 06:13 I mean, kinda, because, like, you… to get the… like, you have to merge whatever you merge in domain into your release PR, and your release PR has to pass CI, so…
**David Ashpole (Google LLC)** 06:22 Yep.
**Tyler Yahn (Splunk)** 06:22 Yeah, I mean, it'll automatically kick it off on main once you merge as well. Yeah, so yes, yeah. You take a look at the CI there. Hopefully, there's no breakage. That's happened once in, like, the eBPF space, I saw that, but usually do, like, merge conflicts as well, like, that's always problematic.
But yeah, then, then after that, just take out those bypass rules, and yeah. Or… let Terrafone do it for you, nightly or something like that, but… But yeah, so that's the whole process.
Yeah, it's kind of a circuitous thing, but it also is, like, I think, helpful to try to keep those things private, so, yeah.
Till the last minute.
**David Ashpole (Google LLC)** 07:05 Yeah, no.
**Tyler Yahn (Splunk)** 07:07 Yep.
**David Ashpole (Google LLC)** 07:09 Maybe someday they'll have, like, private runs or something.
**Tyler Yahn (Splunk)** 07:13 Yeah, I would like that. Like, I mean, I get it, because there's, like, secrets and stuff that you need to, like, set up, but, like, that seems like a solvable problem, like…
**David Ashpole (Google LLC)** 07:21 It does. It does.
It mostly is just, like.
for people who can just go look at the regular workflow runs. You don't just want it to be like, oh, look.
This is exactly…
**Tyler Yahn (Splunk)** 07:30 Yeah. Yeah, it's kind of annoying in that sense, but… But yeah, I mean, that should be all you need to get that done, but… Yeah, it was not a… Wasn't too easy of a release this time, so… Fair enough.
Cool.
Well, hopefully, Sam can watch the recording on this one.
But yeah, I don't know about documenting it either, because it's kind of a janky way to go around it, but… It's also, like, every… SIG has this problem, if they're using private repositories, so…
**David Ashpole (Google LLC)** 08:07 Right, I don't know if we… I guess the only thing we, like… reveal by documenting is, like.
Someone could sit around waiting for us to do a release.
**Tyler Yahn (Splunk)** 08:19 And then… Yeah, but even then, like, if you do the bypass rules right, you still need to be a maintainer to do the bypass.
**David Ashpole (Google LLC)** 08:25 Oh, yeah, yeah, right, we're not…
**Tyler Yahn (Splunk)** 08:26 Exactly, yeah We're not, like, opening up the floodgate, but yeah.
Yeah, I don't know. I don't know, like… I think the only… Actually, I don't know.
Yeah, I mean, I don't know, maybe they can… submit a bogus security advisory, put in some bogus changes into a private repo, I don't know.
Actually, I don't know what the attack vector is there, but… I'm gonna let you and the rest of the TC figure that one out. I'm happy to just know, and then keep it in mind.
**David Ashpole (Google LLC)** 08:57 No, it's okay. Now that I know it, at least we won't be blocked again.
**Tyler Yahn (Splunk)** 08:59 Yeah, yeah.
**David Ashpole (Google LLC)** 09:00 while I'm here.
**Tyler Yahn (Splunk)** 09:02 Yeah. Robert knows it as well, because he had to remind me on this one, so, yeah.
**David Ashpole (Google LLC)** 09:07 Nice.
**Tyler Yahn (Splunk)** 09:08 Yeah.
Although… I'm pretty sure he forgot as well, so it… I'll probably forget next time as well.
Okay, cool.
Jumping into the first item I had on here, I wanted to just, you know, we had the release go out 1.45, Which is pretty good, pretty great, actually, a lot of good stuff came out there. I wanted to take a second here and pause while we just get a plan together for what the next, release should be.
I've put together a few things in here, just… I think that the next big thing… is LogsGA. I'd really like to get that done before KubeCon. Seems like a long way away, but it also doesn't seem like a long way away.
Given especially European holidays, so I think it's something we should probably try to get prioritized.
and get planned out. So I put a date on this of August, or October 5th, which is, you know, 2 months away.
this has got all of the audit compliance stuff for the logs that's already on here. I think that we could… take a look at all of these things. I think there's a few other things that I've added here as well, but they're not, I think, blockers, but I wanted to make sure that, like, we just kind of go through these.
This, will allow key duplication, I think something we should probably decide on, at least, Get that in there.
There's the configure response body size limit. This is something also Robert has been looking at, so I wanted to keep this in here.
Definitely think there's some work to be done there.
But yeah, the big one is the 1.0 of the logs API.
I added your attempt to lazy compute filtered and dropped attributes. Don't think it's a blocker, but I, you know, we got some time. I feel like we should be able to get this in.
I'm…
**David Ashpole (Google LLC)** 10:59 I made one change and re-requested your review, by the way. Okay.
Because, a salmon cotton.
A pretty big regression in the attributes hashing functions.
**Tyler Yahn (Splunk)** 11:10 Hmm.
**David Ashpole (Google LLC)** 11:11 That I'd missed, because I think I… Like, ran it against a previous iteration.
We're.
**Tyler Yahn (Splunk)** 11:17 Something.
Okay.
**David Ashpole (Google LLC)** 11:19 So, I had… I made some… Yeah, I made some optimizations.
Yeah, I'd appreciate your…
**Tyler Yahn (Splunk)** 11:28 Take another look. Okay. Yeah, I can.
I also have the sync map for exponential histogram stuff in here.
Yeah.
This bug that came in yesterday, for attributes access concur… Concurrency issue, is in there as well. That's got a PR.
That one is gonna need another approver.
Which we're really low on these days. I don't know when Damien's coming back. Also, we probably need to get some more approvers.
But anyways, yeah, Sam, if you're watching the recording, you know, please take a look at this PR.
Fixed racing, concurrent spin, Asppot reads, that's this one, sorry. Audit compliance, this is all the stuff for the logs, release, so essentially this should be all set. There's probably some cleanup as well, but, like, we want to make sure that we're compliant first, so these are… all the issues that Robert's created for the audit compliance, those are all added here.
Yeah, the Do Not Change markers for our ins… Interfaces in the SDK, these are things we've always done.
the logger provider… Essentially, like, we're good to go, is with this release, it's kind of the idea for logs.
Same… Yeah, otherwise, and this is… this is already in here, so this batch processing stuff, I don't know… what's up with this? But… Yeah. Let's see, I think that's it.
Cool, alright, yeah. I think that should be… good from what I got on here. I put a little preliminary, like, overview?
it's not really that important how accurate it is, but it's more just, like, this October 5th is kind of like the due date. I'd really like to get us out by then, given early November is KubeCon, so, yeah, getting this out is kind of the goal.
Any other thoughts or anything that's missing?
this is the KubeCon release, essentially. I don't know if we're gonna get another one out before KubeCon, so just kind of thinking that through.
**David Ashpole (Google LLC)** 13:34 I wanted… I have a… I have a separate topic. It's… it's just related to the sync.map one for exponential histograms.
**Tyler Yahn (Splunk)** 13:42 This… okay, yeah.
**David Ashpole (Google LLC)** 13:46 I was wondering what people's… I thought that this would be a really good use case for the new stacked PRs thing.
But it requires them all to be from… to be from branches that are on the OpenTelemetry Go repo.
**Tyler Yahn (Splunk)** 14:04 Yeah.
**David Ashpole (Google LLC)** 14:05 Because this is actually… The only hesitation I have with this is that it's a small performance regression.
Until we actually… Do the lock list bit.
But given how long these take to review, I'm just concerned that, like, we'll have a regression for, like, 3 releases.
So… Yeah.
**Tyler Yahn (Splunk)** 14:28 I think if you put an issue in to the milestone, we can track that as a gate.
But we need to understand that it's a gate, you know?
I'm doing that a lot in the eBPF space, like, I'm doing this config migration.
And they did a lot of work in, like, 2 releases, and then this release, it's like, I need… I need 3 PRs to land, and I've just got an issue in the milestone that says, like.
effectively, these three PRs, like, we can't go until we get these three things done, kind of thing. I see. Yeah.
I don't know if that is helpful. I mean, I agree, like, I like the stack stuff, I've used it in, like, private repos, it's great, but… Yeah, synthetically, you can kind of recreate that, just with some sort of, like, tracking issue.
**David Ashpole (Google LLC)** 15:12 Like, right, I can also just wait till this gets approved, and then we can… we can… fake stack, and I can just open the next one and have a do not merge. That's also fine. I was just curious. I don't have any private repos, I guess, to play around with, so…
**Tyler Yahn (Splunk)** 15:27 Oh.
**David Ashpole (Google LLC)** 15:27 Yeah.
**Tyler Yahn (Splunk)** 15:29 Yeah, yeah, I, I, I mean… Yeah, I'd rather not, Push branches to this one outside of, like.
I don't know. What do we do? Like, the renovate stuff? I don't know. I think forking is a good idea, but… What do you mean you don't have private repos? You have… you have a fork at this.
It's right there.
**David Ashpole (Google LLC)** 15:56 True, true, I can have my own sex.
**Tyler Yahn (Splunk)** 15:58 Yeah.
**David Ashpole (Google LLC)** 15:59 Nobody wants to review those.
**Tyler Yahn (Splunk)** 16:00 No, he must review that, yeah.
But yeah, okay. But yeah, that sounds like a good plan, at least.
Going back also to the contribib, milestone for this, I've got essentially what's already been added here.
This one is not as, I think, as critical, it doesn't have too much to do with the logs, there's obviously, like, the logs, bridges here, which are gonna, you know, need an updated dependency, but we can look in, I think, after that release, stabilizing the logs bridges afterwards, or… waiting some time, I don't know how long we want to wait, but we could… we can look into that as well. But otherwise, like, this is just existing things that have already existed here. I don't know if I'm missing things as well here, so… We definitely don't want to block, like, the stable release, unless it's, like, critical.
But yeah, if folks have, like, things that we want to try to get in, we could try to mention them now.
To scope this work.
**David Ashpole (Google LLC)** 17:01 I don't think almost anything should block.
**Puneet Singh** 17:05 Yeah, I had one thing in mind, but I'm not sure if it needs to be part of this.
our next release, so this resource detector in the SDK core that detects the container ID, with container.
It depends on C Group 1, V1, I think, and I think most of the recent 2S have, like, started to ship C Group V2.
Which kind of also blocks whatever, so it kind of makes something private, which makes reading the container ID from the… From the file, you're supposed to read, kind of, like, there's nothing available, so kind of stops working, actually.
So, I mean, that thing is already in my mind. I have to create an issue and follow up for that.
I think the fixes will go into the core container detector, and also the Docker one, because it also depends on the, it for identifying the container ID, but just wanted to… I mean, yeah, business.
**Tyler Yahn (Splunk)** 18:13 Yeah.
**Puneet Singh** 18:13 Should I target for this release, or…
**Tyler Yahn (Splunk)** 18:15 I think that one doesn't have to be a blocker, but definitely if you wanted to work on it, I would say definitely look at the prior art, though, like, that, I think, has been attempted twice now.
The V2, API.
for the Docker setup, so, like, there's definitely been some work here, and, like.
Both times, like, there's been some, like, serious… Flaws with, like, access issues into the design and compatibility stuff, so… I think you're on the right path, I think it's a great thing to work on, but I would just say, like, be well-versed in, like, the prior art here on this one, okay?
**Puneet Singh** 18:49 I'm sorry, I didn't get the last part. Be well versed on the…
**Tyler Yahn (Splunk)** 18:53 the prior… so, like, the previous attempts, so the… the… there should be… I think there should be already an issue for this, so if you wanted to resurrect that, that sounds great. But there… I think, if my memory serves me correct, there's at least one. I thought there was two PRs that tried to resolve this, and they both, like… languished or, like, got outright rejected due to the fact that, like, they were just not correct. So…
**Puneet Singh** 19:16 But…
**Tyler Yahn (Splunk)** 19:16 I would just say, like, take a look at those, make sure that, like, all… any feedback that was provided to those is addressed in whatever you want to propose, but, like, yeah, I think that's a great thing. We do want to go this route, and we do want to add this, so, please, please do this if you have time, and I would not discourage you from working on it. We can definitely add it into this milestone, but just, like, I would say, like, start there, is all I would say.
**Puneet Singh** 19:40 Right. I've just looked at the two attempts in the other SDK. One is the JavaScript, and another is Java.
I think the… the overall follow-up was, like, more of a best-effort case that… The… whoever implemented the… the C group V2 support was not convinced that it is full error-proof approach, which is not going to break in future, because the standard is not quite… The approach is not quite as standardized at the, the cgroup level also, and its support across the container runtimes. So, so yeah, I think it's more of a follow-up, so I wouldn't insist too much on including this, but depends on how follow-up goes. We'll see about that.
**Tyler Yahn (Splunk)** 20:28 Yeah, okay, that sounds good.
I feel like Sam was the one who also, like, had worked on this. Unfortunately, Sam's not in the meeting, but yeah, maybe next time, if he's here, we could discuss it, but yeah.
Yeah, I agree, like, I'm guessing those other groups probably found the same problem, so, yeah.
**Puneet Singh** 20:47 ordered.
**Tyler Yahn (Splunk)** 20:48 Yeah.
Okay, well, cool, folks good for… release planning. I think we've got a set of work there. If there's more, I'd like, you know, in the next week, think about it. If you… if you come up with some things, go ahead and add them, or ping them, ping one of the maintainers to add it, and we can add it to the release. Otherwise, yeah, I think, I think we've got a good base to start from.
I believe the next one is probably used, Puneet for finalizing GRPC status message. I can start sharing my screen again.
This is you, right?
**Puneet Singh** 21:31 Yeah.
**Tyler Yahn (Splunk)** 21:31 Okay.
**Puneet Singh** 21:33 Oh, I didn't mention my name personally.
**Tyler Yahn (Splunk)** 21:35 No, I… yeah, I just figured. Continuity of last week, yeah.
**Puneet Singh** 21:40 Yeah. So, yeah, I think, just to recap a bit, this is about, providing option to user to override the mapping of, the gRPC status code to the hotel-specific, codes.
And this is because the spec allows for such override.
Previously we discussed, I think three approaches, and it was… the feedback was that we would like to see a combination of two and three.
Two being the method-specific mapping, and three is the global. So, just to, you know, I've kept those, but I've, like, suggested another one, which is a combination of two.
But, but yeah, rest is same, I've just typed in the definition of the, map-based mapping, that we are not going to support regex kind of stuff, it has to be absolute mesh, but otherwise.
It's a combination. In terms of precedence, the method-level mapping takes IS precedence at present, then follows the global mapping, and then follows the SDK default.
Both… APIs can be used, like, in any way, you can use method or global or both, and the precedence rule should follow.
So, yeah, I think that was the basis.
**Tyler Yahn (Splunk)** 23:04 Yeah, that sounds right. Yeah. Looks good to me.
**David Ashpole (Google LLC)** 23:08 Did we have.
**Puneet Singh** 23:09 So… yeah, David.
**David Ashpole (Google LLC)** 23:11 I remember last time, I was curious if there was, like, a way to… Like, if there's a… if there's a way to set this in middleware.
Like, with an interceptor or something?
**Tyler Yahn (Splunk)** 23:26 Yeah, we had talked about that, and the problem was, like, access to the span, though, right? Like, whether that middleware has access to the context or the span? Because, yeah, like, if you have access, you could just set the status at that point, but…
**David Ashpole (Google LLC)** 23:39 I mostly just want to explore If we've already ruled that out, then I think that's fine.
**Tyler Yahn (Splunk)** 23:45 I don't know if we rolled it out. I don't… I think it was, like… It was not clear how you would get access in the middle of a call, but I… I mean, I haven't looked… I haven't looked close enough, I couldn't say it's not possible.
**Puneet Singh** 24:02 I've got an interesting comment.
Sorry, David, go ahead.
**David Ashpole (Google LLC)** 24:08 No, you go. I was just talking out, or thinking out loud.
**Puneet Singh** 24:10 There was a comment from Ludmila, she mentioned something about that this… was supposed to be solved using a span processor-based hook?
Which is related to spam processor end, but it was… it is also part of spec, but it wasn't implemented, or it was, you know… I think some SIGs tried to implement it, including Go, but it was rejected because some technical limitation, I think.
**Tyler Yahn (Splunk)** 24:42 Hmm, that's actually a really good point, because… the span processor configuration is something that an operator is gonna set, and, like, this option that we're talking about here is something that instrumentation authors are gonna set.
Which is… so, that can be problematic. If you're, like, if you're importing something that already has, like, gRPC instrumentation, like, built into it.
like, you can't change this after the fact. Like, if they've already made the decision to do these overrides, like, that works great, but, like, If you as an operator are like, no, like, that actually is still an error, like, you can't go back outside of… Doing a spam processor to actually address this.
**David Ashpole (Google LLC)** 25:27 Yeah, it just… it reminds me so much of all the contextual stuff.
like, the contextual attributes, for example, where, like, yeah, user just wants to talk directly to the SDK, and the instrumentation is getting in the way. That's, like.
Yeah.
I want there to be some way to, like.
throw something in the context that says, hey, I'm… I'm not an error, so that users can, like.
you know, do what they want, basically. But I… I feel like if it works via on-ending, then I think that's definitely the route to go, otherwise I feel like we should… if there's some way for us to… I just don't like the, like, here, pass a function. It feels like that's what everything devolves into, if we don't have contextual. It's like, oh, here's a function on gRPC request that returns what… what the instrumentation should do with it. It's just, like, expensive.
End.
**Tyler Yahn (Splunk)** 26:27 Yeah, indeed.
Yeah, do we support the on-ending, though? I, like, I think that's still very experimental.
**Puneet Singh** 26:39 I think we've tried, but, I think the issue is mentioned, yeah.
But it was closed because… I think it needs, or no other… Locks to exist on a stand, something like that.
When calling on ending, but… But yeah, I'm not sure.
**Tyler Yahn (Splunk)** 27:00 Well, it's… it's experimental.
I think it'll…
**David Ashpole (Google LLC)** 27:03 It just needs, like, weird… X directories with… Duct typing, and the classic… Is it that sort of problem?
**Tyler Yahn (Splunk)** 27:14 I think so. I think this is, like… One of those things that we are also, like, this is… I think this is the proof of concept.
That we had, Looks like… Yeah.
Yeah, I don't know.
This looks like about what I would expect for the experimental. Maybe… why was this blocked?
Oh.
I think there's just implementation details here.
Yeah, I mean, I… so I don't… I think it… this is, like, it was close because it was stale, but this is probably about what I would expect for the on-ending stuff.
Sorry, we're going down the rabbit hole a little bit here, but, like, yeah, I mean, this X package thing, I think, was… had… merit?
The only thing that I would think about is, like, we've talked about it before, David, where it's, like, adding… Support for an interface.
from, like, our SDK packages is kind of a breaking change, if it changes in the future, but, Yeah, that's my only, like, slight hesitation, but it's also, like, I don't know how to, like.
I don't know how to get around that, and I think it's just something we can.
**David Ashpole (Google LLC)** 28:57 We have to, like… Do the whole define a new interface that includes the thing, and then…
**Tyler Yahn (Splunk)** 29:03 Yeah, but that… that's fine, right? Like, obviously, like, put that in, like, an X package, right? But then, like, you need to implement it.
**David Ashpole (Google LLC)** 29:09 I don't know, in the core package.
**Tyler Yahn (Splunk)** 29:12 Well, yeah, sure, we could do that. Yeah, that's definitely the stabilization method, like, we would have to do something like that. But, like, But the thing is, is, like, while we're prototyping, like, that on-ending.
like… How do you implement that in any of our processors, like, without it? Like, somebody finding it, taking a dependency on it, and then, you know, when we change it because it was experimental, it breaking them?
**David Ashpole (Google LLC)** 29:37 Is it in the processor?
Is that where this is?
**Tyler Yahn (Splunk)** 29:41 Yeah.
**David Ashpole (Google LLC)** 29:41 Oh my goodness.
Yeah. So we'd have, like, X… Experimental batch bed and processor, or whatever.
**Tyler Yahn (Splunk)** 29:52 No, no, no, it's just like, no, like, the SDK…
**David Ashpole (Google LLC)** 29:55 Right, you can't implement it on the SDK public types. Do we…
**Tyler Yahn (Splunk)** 29:58 Yeah.
**David Ashpole (Google LLC)** 29:59 I guess it depends what we return. We probably return a public struct, right? So we can't just… Alright.
**Tyler Yahn (Splunk)** 30:07 I think, I think it's, like, let me see… Yeah, it just… it… the on-ending accepts a trace span in this prototype that Damien… Proposed, which is, I think, what the… we'd have to double-check with the specification, but I'm guessing the specification is… Yeah, it's either a read… or a read-only or a, I don't know, a writable span.
is probably what I'm guessing is accepting, like, I don't know about the spec compliance on this, I haven't looked at this in a long time in the spec, but, like, yeah, like, we would have to accept something. There's nothing being returned from the method currently. But yeah, I mean, that's the thing, it's just like… If that signature changed at some point.
like, while it was in the prototype phase, then, like, yeah, it could get a little messy, because then, how do you change that on our… any of our processors that are already stable, and yet not break users who may have taken an appendix?
**David Ashpole (Google LLC)** 31:10 methods.
**Tyler Yahn (Splunk)** 31:11 Yeah, but you can't if they have the same name.
**David Ashpole (Google LLC)** 31:14 Yeah, right.
**Tyler Yahn (Splunk)** 31:15 So, like, unending becomes a registered thing at that point, and, like, yeah.
**David Ashpole (Google LLC)** 31:21 takes options.
**Tyler Yahn (Splunk)** 31:23 Yeah, on ending with additional param, or unend… yeah, so, like… And it's not like… like, we aren't publicly advertising that method, so, like, I'm kind of like, I don't know. It is technically a breaking change if we ever did change that method, but, like, I don't know if it's, like, something we wanted to add to, like, our versioning and saying that, like.
Yeah.
**David Ashpole (Google LLC)** 31:44 it's… I… I just don't want to end up where GRPC is, where we're just like, yeah, Go versioning stinks, so we just kind of, like.
**Tyler Yahn (Splunk)** 31:51 Hmm.
**David Ashpole (Google LLC)** 31:52 You know, we'll put a doc comment on it to tell you not to use it, but…
**Tyler Yahn (Splunk)** 31:56 Yeah, definitely don't want that. But I'm also, like, if that's also the case, then, like, unending needs to be stable before we accept it, is kind of the thing.
**David Ashpole (Google LLC)** 32:05 Which is a totally valid thing to do, so we…
**Tyler Yahn (Splunk)** 32:08 Yeah.
**David Ashpole (Google LLC)** 32:08 Like… I don't remember this user's… Use case, but… If there's any workaround we could provide.
Like… Wrapping a stats handler.
To get at the span, to do weird things.
So that we can push this off, even if it's ugly, like… I feel like that's the right thing to do for… like, long term.
Health and sanity and stuff.
Like, we just don't really have any other good options.
**Tyler Yahn (Splunk)** 32:40 Yeah, can you maybe just add a comment to the issue, so Puneet can kind of get this tracked?
David?
**Puneet Singh** 32:50 That would be helpful.
**Tyler Yahn (Splunk)** 32:54 We lost him.
I'm wondering if our sound cut out on his end.
**David Ashpole (Google LLC)** 33:06 For me?
**Tyler Yahn (Splunk)** 33:07 Yeah.
**David Ashpole (Google LLC)** 33:08 I can hear you, sorry. My dog unplugged my computer.
**Tyler Yahn (Splunk)** 33:12 I was just saying, could you add a comment to this effect on Puneet's issue, so then he could, investigate it, or if you can investigate it, put some findings or something, or… yeah.
Yeah, I think that would be helpful to make sure we're, like, comprehensive in following that, so… Okay, cool.
Alright, other than that, I don't see anything else on the agenda. Any other topics? Oh, actually, any talks accepted to North America KubeCon?
**David Ashpole (Google LLC)** 33:45 I even managed to get my maintainer talk.
Rejected.
**Tyler Yahn (Splunk)** 33:50 Wait, they announced some Xander stuff as well? Oh, I must have missed that.
**David Ashpole (Google LLC)** 33:53 No, they didn't, they didn't, There is a rule, so my co-speaker is not a maintainer of career.
**Tyler Yahn (Splunk)** 33:59 That's the expectation.
**David Ashpole (Google LLC)** 34:00 And she submitted the talk, and apparently there's just a blanket, like, if you're not the maintainer and you submit a talk, it's rejected.
Even though I was on the talk, and I am a maintainer.
Oh.
**Tyler Yahn (Splunk)** 34:13 Crossed.
**David Ashpole (Google LLC)** 34:13 So…
**Tyler Yahn (Splunk)** 34:15 Okay.
Yeah, I got two rejected from the main conf. I think they're still pending on, like, the, observability Day stuff.
But, I did get, onto the ContribFest, maintain… or presenters as well, whatever you want to call it. So, we are having an Hotel ContribFest this year again, which I'm super excited about.
Which I, again, hope we can get the GoSIG included in a lot of, you know, first PRs and first commits and first issues for folks, so… Yeah, more to come on that one.
definitely… it was great the last time I did it in London, so I was really excited about this, yeah.
Yeah, but otherwise, yeah, I'd love to… hopefully we got more talks. Like, I haven't heard of a lot of talks actually getting accepted.
I don't know.
**David Ashpole (Google LLC)** 35:10 Neither have I. I'll plan to go even if I don't get a talk accepted. We'll see.
**Tyler Yahn (Splunk)** 35:14 Yeah. Well, yeah, well, that's good.
Have you seen there.
Any other topics? Any other things people are working on? I saw a lot of Prometheus stabilization stuff going on in the spec, David. Anything that's being blocked here for that?
**David Ashpole (Google LLC)** 35:31 No, no.
The only discussions left are the very, like, obscure ones.
Yeah.
Yeah.
That nothing, I think, I feel like there's very little that's likely to change.
Yeah, for the SDK exporter.
**Tyler Yahn (Splunk)** 35:56 Yeah, okay.
Cool, alright, well, that's… that's good.
That's… yeah, that's actually a really positive news then.
Well, awesome. Yeah, if there's nothing else, folks… Had?
We can, end the meeting here.
Thanks all for joining. We'll see you all in a week's time, or asynchronously. Until then. Bye.
**Puneet Singh** 36:21 Great.
