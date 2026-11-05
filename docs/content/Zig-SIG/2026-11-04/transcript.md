SIG: Zig SIG
Date: 2026-11-04
Duration: 45 minutes
============================================================

## Zoom Recording Transcript

**Francesco Gualazzi (OpenTelemetry)** 00:39 Hey, Giovanni.
**Giovanni Panice (IBM)** 00:41 Hello?
**Francesco Gualazzi (OpenTelemetry)** 00:42 How you doing?
**Giovanni Panice (IBM)** 00:43 I'm fine. You?
**Francesco Gualazzi (OpenTelemetry)** 00:44 Not bad. I don't know what happened with the invite, again, I didn't even look at the invite.
So, yeah, some synchronization with the time zone issue? I don't know.
**Giovanni Panice (IBM)** 00:58 Honestly.
**Francesco Gualazzi (OpenTelemetry)** 00:59 Let's be quick. I think we can do it rather quick, so… I won't just wild hide… I'll… The increased contributions that we are having are putting A lot of interest in the project, because we have at least two new contributors.
At the same time, maybe the… the changes, the rate of changes that we are getting.
The conflicts that we have.
is drawing to me some attention, in the sense that, for example, what happened with my PR on the totals, and the exemplars.
as well as the exemplars and other two open PRs is, is a signal that, something Can be improved, right?
So…
**Giovanni Panice (IBM)** 01:48 Well, you know, we have a lot of contribution, sometimes it's normal to have this kind of conflicts. My only concern is about the stuff related to the… I don't remember, let me check… So… Something that pointed, Antoine. Yes, the baggage, the baggage…
**Francesco Gualazzi (OpenTelemetry)** 02:18 Yeah, yeah.
**Giovanni Panice (IBM)** 02:19 That, doesn't… it… it's not present in the, understand that this will,
**Francesco Gualazzi (OpenTelemetry)** 02:28 I think we fixed that, Antoine.
**Giovanni Panice (IBM)** 02:30 Yeah, yeah, you're snoring.
fix that, so maybe we should pay much more attention, you know, when we merge things. So, so this is only my only concern. So, conflicts, it's okay, but, we have to… I don't remember if I matched this kind of stuff, or… I don't know, but…
**Francesco Gualazzi (OpenTelemetry)** 02:49 merged one from me, dedicated one config in the exemplars PR, and and then the Exemplars PR, when I merged it.
**Giovanni Panice (IBM)** 02:58 E.
**Francesco Gualazzi (OpenTelemetry)** 02:59 I didn't check the CI. Well, there was a problem with the CI that was not returning, let's say, an error when we had memory leak, but I have a PR to fix that. It's open. And merging the exemplars PR also As I created conflicts in two or three other PRs.
Which are run by Yash, Yash990.
**Giovanni Panice (IBM)** 03:25 Yeah, that, actually, I have to be fair that I left, you know, in the queue.
**Francesco Gualazzi (OpenTelemetry)** 03:31 No worries, no worries. I mean, most of those are from the metrics, and so I can handle them, because, you know, that's what I know the most, because this was the first one that I wrote.
But I think, yeah, she's doing a good job there, and we are fixing actual bugs. So, what I'm talking about is the fact that for example, we don't have… a rule that I often use in other projects is that the… The base branch should always be up to date.
before merging the PR, right? You know what I mean?
**Giovanni Panice (IBM)** 04:09 Yeah, obviously.
**Francesco Gualazzi (OpenTelemetry)** 04:10 We don't have this rule now, so when…
**Giovanni Panice (IBM)** 04:13 Unfortunately, no, because, I mean, when I imagined something, I didn't notice some, this kind of…
**Francesco Gualazzi (OpenTelemetry)** 04:20 So I cannot… Apply these changes in the settings, apparently.
**Giovanni Panice (IBM)** 04:25 No, I don't reckon not to…
**Francesco Gualazzi (OpenTelemetry)** 04:27 I think those are organization-wide, right?
**Giovanni Panice (IBM)** 04:30 Probably, yes.
**Francesco Gualazzi (OpenTelemetry)** 04:33 Always suggest… no, no, here we go. Always suggest updating pool request branches. Here we go, I saved it.
Okay, let me write down.
**Giovanni Panice (IBM)** 04:41 Okay, another thing, well, I prefer that you use the rebase, honestly.
**Francesco Gualazzi (OpenTelemetry)** 04:46 Instead of merge commit.
**Giovanni Panice (IBM)** 04:48 Instead of the squash merging, yes.
**Francesco Gualazzi (OpenTelemetry)** 04:51 The point there, I think, and I cannot configure that, unfortunately, I think squash is forced by policy, and I think the point there is that sometimes the history can be…
**Giovanni Panice (IBM)** 05:04 Verbose.
**Francesco Gualazzi (OpenTelemetry)** 05:05 There goes, and someone does not develop.
**Giovanni Panice (IBM)** 05:07 Oh, but I think that we, let, we can, we can, we can do it. It's, on the third point, allow a basic merging, so…
**Francesco Gualazzi (OpenTelemetry)** 05:16 Oh, yeah? Wait?
**Giovanni Panice (IBM)** 05:17 Yes, in pull requests. It's something up to us. So I think I… honestly…
**Francesco Gualazzi (OpenTelemetry)** 05:22 discussed that in the past, but you like Or what do you think?
I love squash, I love Rabezo, oh, okay.
**Giovanni Panice (IBM)** 05:29 But, I mean, if we prefers squishing, okay, but, Okay, so…
**Francesco Gualazzi (OpenTelemetry)** 05:36 What do you say?
**Giovanni Panice (IBM)** 05:38 Well, mostly, I mean… I mean, my project that I work on, honestly, is the base. Let me check, for example, the OpenTelemetry Go, for example, so… To be aligned to open telemetry organization.
Yeah.
**Francesco Gualazzi (OpenTelemetry)** 06:11 So, I enabled this option… Always suggest updating pool requests.
Who have I… And second point you've mentioned that should we allow… Grebeis merged… Should we bring this to the slack?
**Giovanni Panice (IBM)** 06:40 Well, only one, not both, so only one, so… What do we mean?
So, only having, or rebates or merging, so not both.
**Francesco Gualazzi (OpenTelemetry)** 06:50 Yeah, so… You say, well, or rebase and squash is already there, or either add rebase, or either add merge commits, but I don't know.
**Giovanni Panice (IBM)** 07:03 So, taking a look to the OpenTelemetry Go, they seem to use the… The base, so let me… to be here.
It is also a conventional comet.
**Francesco Gualazzi (OpenTelemetry)** 07:21 Probably I can also link the project now, the Zig… wait, wait, wait, wait, I had not seen this before.
**Giovanni Panice (IBM)** 07:29 So… That is good.
**Francesco Gualazzi (OpenTelemetry)** 07:33 Oh yeah, Zinka Project, there you go, Zig!
Ugh.
Okay.
I've got the board, now, linked to the… the project.
This is in progress.
So, wait, should we… I pointed that as a question, okay? So, should we do that?
To the library-based merge, we can… we can enable it anytime, right?
**Giovanni Panice (IBM)** 08:08 Oh, yes.
**Francesco Gualazzi (OpenTelemetry)** 08:10 So… I linked the project to our… To the board, to our repo, which is good.
And what I want to avoid, honestly, which is something that is happening recently, is that we have, like, 10 open PRs at all times.
And, you know, with multiple rebases, multiple conflicting changes here and there.
That's probably not healthy, right?
**Giovanni Panice (IBM)** 08:37 Ugh.
you know.
**Francesco Gualazzi (OpenTelemetry)** 08:39 I mean, it depends.
**Giovanni Panice (IBM)** 08:40 In an open source project, I don't know, it's… I mean, normal, but I don't know what is your expectation?
**Francesco Gualazzi (OpenTelemetry)** 08:48 Well, we… because we have… we… the project is small, right?
**Giovanni Panice (IBM)** 08:52 Yeah.
**Francesco Gualazzi (OpenTelemetry)** 08:52 What's it this week?
**Giovanni Panice (IBM)** 08:53 We don't have many, many contributors.
**Francesco Gualazzi (OpenTelemetry)** 08:55 Exactly, so we should try to keep the… Say, the open… The open changes… I don't know, maybe 2 or 3 at a time.
**Giovanni Panice (IBM)** 09:07 Open or requests, so…
**Francesco Gualazzi (OpenTelemetry)** 09:09 If they're in draft…
**Giovanni Panice (IBM)** 09:10 How do you…
**Francesco Gualazzi (OpenTelemetry)** 09:12 I'll do block. No, it's not the block.
**Giovanni Panice (IBM)** 09:15 What do you… Sorry, I don't get what you want… how do you want to proceed? So, if someone wants to do a request, so… You cannot prevent to open a bully goes, no?
**Francesco Gualazzi (OpenTelemetry)** 09:32 No, no, no, I don't want to do that.
**Giovanni Panice (IBM)** 09:33 -Oh.
**Francesco Gualazzi (OpenTelemetry)** 09:34 What I'm… what I'm saying is that we should try to… or either review faster, or, let's say, set a guideline that the things that are in draft are not expected to have ever been even looked at. So, we only review the undrafted PRs.
And we only… and we try to have maximum, I don't know, 3, 4 open PRs for review at any given moment, you know?
Because otherwise, it gets, difficult.
**Giovanni Panice (IBM)** 10:08 Well, hmm.
from my experience, we… at this point, we should put some label, on, you know…
**Francesco Gualazzi (OpenTelemetry)** 10:19 Yeah, just…
**Giovanni Panice (IBM)** 10:20 Yeah, exactly, for, to… Because, if you make, any interaction into the pull request, it will be pop… pop up on top, even if it's, you know, old. So you have to check it with the hours of, when it's opened at the, I don't know,
**Francesco Gualazzi (OpenTelemetry)** 10:56 Yeah, I don't have a solution either.
**Giovanni Panice (IBM)** 10:58 So… I was just raising this point, because… Honestly, because, I mean, I'm checking the merger PRs, for example, the example leak, and it was approved by me and Antoine.
The bed kitchen…
**Francesco Gualazzi (OpenTelemetry)** 11:14 How easy to find out.
**Giovanni Panice (IBM)** 11:15 Was approved by you and merged by you, yes?
**Francesco Gualazzi (OpenTelemetry)** 11:19 So now it's already burst.
**Giovanni Panice (IBM)** 11:21 Yeah, yeah, yeah, no, I'm checking if something was merged without any review, any approval, or… no.
**Francesco Gualazzi (OpenTelemetry)** 11:27 No, no, that's not… that's not possible.
**Giovanni Panice (IBM)** 11:30 Yeah, indeed, I mean, it supports the idea.
No… Well, we have an accuracy 7 pull request, which… 4 in, draft.
So… Yeah.
**Francesco Gualazzi (OpenTelemetry)** 11:54 Yeah, exactly, but, well, again, if, if they are in draft, I don't… I don't think, I don't think…
**Giovanni Panice (IBM)** 12:04 So, for example, this one about test integration…
**Francesco Gualazzi (OpenTelemetry)** 12:08 Don't merge it, because again, I mean, this is approved by Jacob, but in reality, the… the co-pilot Review caught one interesting thing, so, well, it's a comment, but I need to fix that. I don't… I mean, I want to… I want to ensure… That everything is sound, you know, before I came in.
Oh, yeah, yeah.
This is all good, suggestions from Compiler.
So yeah. So how do we synchronize that?
Hi.
So once we have our approval, theoretically, any… any approver can… any maintainer can mail, right?
**Giovanni Panice (IBM)** 12:45 Yep.
**Francesco Gualazzi (OpenTelemetry)** 12:46 But how do we decide What needs to go first.
**Giovanni Panice (IBM)** 12:50 Okay, for this case, I'll request review for Jharanov, which It doesn't mean that he has to do, again, the review?
And, put the… yeah, the maintainer, the… Approvals. Approve… open tournament Zig approvals, okay.
as reviewer, for example, and remove… not remove Yarov, but request review.
**Francesco Gualazzi (OpenTelemetry)** 13:19 No, it… well, okay, now…
**Giovanni Panice (IBM)** 13:21 In this case, it will not…
**Francesco Gualazzi (OpenTelemetry)** 13:22 Do the changes. I have to do the changes.
**Giovanni Panice (IBM)** 13:24 Yeah, yeah, yeah, no, but in this case, yeah, you have to do the changes, yeah.
**Francesco Gualazzi (OpenTelemetry)** 13:28 That's not this.
**Giovanni Panice (IBM)** 13:28 should not pass now, I guess.
**Francesco Gualazzi (OpenTelemetry)** 13:31 You shall not pass! Is this what… is this what you're saying?
**Giovanni Panice (IBM)** 13:36 Yeah, something like that.
**Francesco Gualazzi (OpenTelemetry)** 13:39 Alright,
**Giovanni Panice (IBM)** 13:41 Oh, let's put a comment, wait for… Okay, so, like, okay, let me…
**Francesco Gualazzi (OpenTelemetry)** 13:49 But this…
**Giovanni Panice (IBM)** 13:50 wait for the, the, for, wait for the, compiler comments.
Let's go by the comments.
Anyway, from my side, what are the ones that I merged? I merged the one related to the testing failed CI.
I imagine the,
**Francesco Gualazzi (OpenTelemetry)** 15:04 But it's okay, I mean, as long as we… again, we have to find… I found a knob to update the branch. Okay, sort it out.
Then, what do we use when we are in doubt?
if a PR… can be merged immediately after approval. So imagine that I review a PR, right?
**Giovanni Panice (IBM)** 15:24 Oh, well, we should, we should put a comment or, like, a request for change. In this case, it would be blocked. So, like this one that I have done, I have done, now on the 162, so I put a comment, wait for other co-pilot comments, so… and in this case.
We can, I mean, oh… At least, Give time to… even if someone else has approved, so…
**Francesco Gualazzi (OpenTelemetry)** 15:57 Yeah.
Okay, I'm implementing the changes now. So, because I want to understand if the process works as expected, right?
So, there has been an approval, but the approval, let's say, is I wanna say… I don't wanna say misleading, but… Hey, it's like… more, faithful than needed. Then, how do we ensure that, A, we respect a potential merging order, because some changes need to be synced before?
the others, like the examples with other OpenPRs. And B, That we don't merge something… That was, you know, approved a bit lightly, you know what I mean?
It's not easy, huh?
**Giovanni Panice (IBM)** 16:57 Well, the idea is that we don't… we should not have, pull request that depends on each other. Otherwise, we should comment that they depends. In this case, there is this kind of, you know.
And, you know, they should not be… In order… a time… a time order, depends, but… Anyway, let's pay attention and, give more comments, about that, so… But,
**Francesco Gualazzi (OpenTelemetry)** 17:44 Now there is the update branch thing that I like, okay.
branch?
And this one is going to add a merge commit, but the merge commit obviously goes away when we squash.
Okay.
I mean, this is probably better.
Okay.
I think, I think this is… Okay, okay.
Because again, I hope we get more and more people. At the same time, I don't want that more PRs mean… more friction.
You know what I mean?
**Giovanni Panice (IBM)** 18:44 Yes, yes, but, In that case, we can try to address this kind of friction. So, you know, we can revert to the full request, or, you know, so… In any case, yeah.
**Francesco Gualazzi (OpenTelemetry)** 19:05 Because we are… we have… because we have not… say, yet released, but, I mean, this is a privilege, you know, that we are… The privileged situation that we're in.
It's, it's something that… might not last long. Because, again.
We should try to create the first alpha release by end of year, or starting next year, so…
**Giovanni Panice (IBM)** 19:29 Oh, yes, yes, yes, but, yes, I don't know, oh.
Mmm… Yeah, it's not easy, honestly.
Currently, in my project, I have 147 pull requests open, so, I check, now, so… so, you know, depends on the point of view, so…
**Francesco Gualazzi (OpenTelemetry)** 20:05 My rent is completely unjustified.
**Giovanni Panice (IBM)** 20:08 Yeah, so… No, I mean… It's complicated with an Aventus project, so… indeed, some stuff will go really slow, because sometimes you spend a lot of time doing this kind of, you know, reconciliation, so… to don't… because, Otherwise, you should be, pay attention to all the pull requests, and… but in any case, my expectation is that Wventh doesn't have too many… pull requests. I think that, like, if we reach 20 pull requests, it's.
**Francesco Gualazzi (OpenTelemetry)** 20:50 Depends on the project, you know.
**Giovanni Panice (IBM)** 20:52 It's, I don't know, we should be full of bugs. Indeed, if I had to take a look to the, I don't know, Go, for example.
Well… Well, 60, open pull requests, so I think that depending on, if they start using it, roughly and, like any other SDK, I think that we maybe will reach this kind of numbers, honestly.
**Francesco Gualazzi (OpenTelemetry)** 21:31 That would be good.
**Giovanni Panice (IBM)** 21:34 With the 100, 100-ish overnight, so… Let me take a look to Java.
Jai is in a better situ- in better, State. 24.
TypeScript?
Jonathan, maybe.
Anyway, we have some, some point, some, stuff to discuss, Apart from this kind of, things.
Yeah, it's a question. Do we have any points in the agenda? Okay, so maybe we can close here, so… Okay,
**Francesco Gualazzi (OpenTelemetry)** 22:35 Sorry, I need to do one thing. Come here.
Yeah, that's… I think that's all, right?
No, no more points in the agenda. Sorry, I had to pick up a notification on my phone.
There were no items prior to this, I think the… with the… with Antoine last time last week, we took a look at the milestone, and now that we closed the exemplars, which was one of the biggest items in the… In the milestone?
We're pretty close, huh?
Tried from some bugs here and there, but the core functionalities are all there.
**Giovanni Panice (IBM)** 23:27 about this point related to separated APIs and SDKs.
**Francesco Gualazzi (OpenTelemetry)** 23:32 Yeah, yeah, yeah.
**Giovanni Panice (IBM)** 23:33 Are you working on these kind of things?
**Francesco Gualazzi (OpenTelemetry)** 23:35 The other biggest thing, I think, is the Windows support.
**Giovanni Panice (IBM)** 23:40 the window support.
**Francesco Gualazzi (OpenTelemetry)** 23:42 Yeah, yeah, apparently we cannot compile at all on Windows because there is clock. So… there is one, there is one.
**Giovanni Panice (IBM)** 23:50 We use Linux and Mac.
**Francesco Gualazzi (OpenTelemetry)** 23:53 We… we use BOSIX API for the clock, so… while I don't expect anyone running Zig on Windows servers.
we should be able to let the people compile, even on Windows, in their native target, so… So… Yeah, I will find a way to… include Windows in CI, and I guess… evaluate if, really, clock is needed, no? Because, yeah, in fact, I already linked the… So… Issue 125 is… is on me, I can do that, but… the most pressing one. So we only have 3 items for the alpha release.
The empty trace state, which is probably tackled In a PR, if I'm not mistaken.
Rakuten through the hot.
Okay.
No? Not yet.
a handful of bugs that are, reported by Yash in their metrics aggregation.
although these two PRs, I do remember why we were doing it like so. So, the… Yeah, I need to speak with Yash about the decision that he's trying to push there. I may not fully agree, but We have tests to prove.
The effectiveness and the correctness of the final implementation, in case In case a change is done at the core of the matrix SDK, And then, the last one…
**Giovanni Panice (IBM)** 25:38 I think another thing that is important is the public AI documentation. I see an issue. Before the release, maybe we should have this…
**Francesco Gualazzi (OpenTelemetry)** 25:46 But I think we do have that. I mean, what we don't have is the published…
**Giovanni Panice (IBM)** 25:52 Yeah, on the Git… because I saw a comment on a comment. While working on the module, I found that we can use the existing GitHub pages workflow. Exactly.
**Francesco Gualazzi (OpenTelemetry)** 26:02 That one works.
**Giovanni Panice (IBM)** 26:04 We can decide if we want to keep this and incorporate GitHub overflow from point 3, or move to… out to the hotel docs page.
**Francesco Gualazzi (OpenTelemetry)** 26:12 I think we should do both.
Because the Zig docs, the auto docs from Zig, is just, like, a format that everyone in the Zig community is, You used to, so accustomed to?
So, they want to use that, right? And it works, it's deployed in the GitHub pages for the repo.
You know, that's fine.
All we have to do is to close that one, which you correctly pointed out.
should be part of the Bison Alpha.
**Giovanni Panice (IBM)** 26:43 Oh, absolutely, otherwise we have, so, so there is detect how to publish documentation in the official hotel channels.
**Francesco Gualazzi (OpenTelemetry)** 26:51 Exactly. This one, I didn't want to reach out on Slack on, Josh, with, to Josh and, Vita?
And… get some directions from them, because I think what we need to do is, like, a big PR… In the hotel docs report? Reportitory.
**Giovanni Panice (IBM)** 27:08 -
**Francesco Gualazzi (OpenTelemetry)** 27:10 And…
**Giovanni Panice (IBM)** 27:11 Include.
**Francesco Gualazzi (OpenTelemetry)** 27:11 Including Zig as a language, but maybe before that, we also want Zig in the demo?
I don't know. I mean, that's probably not strictly necessary, but desirable. So basically, we need to, say, hoist Zig into the OpenTelemetry support… official support language visibility that all other languages have. Right now, it's just, like, a bit hidden, if you want.
And then, and I can take care of that, honestly.
But not before we fix all the bugs. So when we have everything stable, the collection is working, the metrics aggregation is working, the view is working.
I don't even need to…
**Giovanni Panice (IBM)** 27:57 Maybe, maybe, maybe we need to have at least one release, because taking a look to the, I don't know.
the other language, they pointed also to the demo, which we have a pull request in place, but… We have to merge it, and we need to be, you know… I don't know if you get the chance to take a look, they do. Yeah, they asked us an opinion about that, that we should merge. So there is, for example, forego getting started, Instrumentation, libraries… Okay, sporters, resources… sampling API, which pointed the API on the, yeah, the one that will be… we can, you know, generate examples. The same Registry… Well, this is not something that we need, I guess. Okay. Yes.
Let me check, yeah, mostly everyone has a section on getting started. Libraries, instrumentation, the APIs… Okay.
Let me give a look… let me give a look… where are these dogs?
I suppose that, community Locks, let me check…
**Francesco Gualazzi (OpenTelemetry)** 29:50 If you have, something… if you know already some… how to publish the documentation, oh, can you link in the issue, please? I mean…
**Giovanni Panice (IBM)** 29:58 Yeah, I just found it.
**Francesco Gualazzi (OpenTelemetry)** 30:01 Okay, please link me…
**Giovanni Panice (IBM)** 30:03 Yes.
**Francesco Gualazzi (OpenTelemetry)** 30:04 link the information in the GitHub issue, and I will take it from there.
**Giovanni Panice (IBM)** 30:10 - yes.
We should open a pull request on the OpenTelemetry.io, so… Okay.
So… So maybe, for the first iteration, maybe we can, just, like, Zig, and, Intro.
to ventilated Zig, getting started.
And nothing else.
So, I don't know.
At least for the first iteration, but we can improve, I don't know.
**Francesco Gualazzi (OpenTelemetry)** 31:24 Okay.
**Giovanni Panice (IBM)** 31:39 Okay, anything else we want to discuss?
**Francesco Gualazzi (OpenTelemetry)** 31:42 Not right now. No, no, no. I go back to my… other Zig projects. Like, I'm… I'm trying to… be involved in the maintenance of Zig NAT client, because, you know, there's now an official.
**Giovanni Panice (IBM)** 31:58 Yeah, not, not, exporter. There is, I mean, if I recall correctly, Giuseppe works in the nuts.
Let's.
**Francesco Gualazzi (OpenTelemetry)** 32:12 Is that Pecha Renault?
**Giovanni Panice (IBM)** 32:13 Yes.
**Francesco Gualazzi (OpenTelemetry)** 32:15 Well, Cincinnati.
**Giovanni Panice (IBM)** 32:18 If I recall correctly, yes.
**Francesco Gualazzi (OpenTelemetry)** 32:20 message him. That would be nice.
**Giovanni Panice (IBM)** 32:23 Let me check, beta… Because I talked with him about that the other day. No, Francesco Hozzuto.
**Francesco Gualazzi (OpenTelemetry)** 32:36 Okay.
**Giovanni Panice (IBM)** 32:37 And she's.
**Francesco Gualazzi (OpenTelemetry)** 32:38 Nobody was…
**Giovanni Panice (IBM)** 32:38 It works in the scenario.
**Francesco Gualazzi (OpenTelemetry)** 32:39 I met him, I met him at Zig Day two Saturdays ago. We didn't talk about it, okay?
**Giovanni Panice (IBM)** 32:46 And, he works in Cincinnati, yes, I mean, I don't know how we, because he said, oh, no, I'm working on this project, Nats, and I said, yes, I have an integration with Nats, with the Bidium.
**Francesco Gualazzi (OpenTelemetry)** 32:58 Beautiful.
**Giovanni Panice (IBM)** 32:59 And, yes, we talked about that the other day, so…
**Francesco Gualazzi (OpenTelemetry)** 33:04 Very nice.
**Giovanni Panice (IBM)** 33:05 Yeah, Nazis is a really nice project.
**Francesco Gualazzi (OpenTelemetry)** 33:10 Okay, good to know. Thanks for letting me know.
**Giovanni Panice (IBM)** 33:16 Okay.
**Francesco Gualazzi (OpenTelemetry)** 33:17 Alright, Giovanni, thanks a lot, and I don't want to say. Enjoy your week, and see you next time.
**Giovanni Panice (IBM)** 33:23 too. Bye.
**Francesco Gualazzi (OpenTelemetry)** 33:25 Yes.
