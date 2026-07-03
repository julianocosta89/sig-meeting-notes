SIG: Python SIG
Date: 2026-07-02
Duration: 41 minutes
============================================================

## Zoom Recording Transcript

**Riccardo Magliocchetti** 00:08 Hello?
**Erdenesaikhan Tserendavga** 00:11 Hello, everyone.
**shuwpan** 00:14 Hello?
**Mike Goldsmith** 00:53 Hello, everyone.
**Riccardo Magliocchetti** 00:57 Hey, Mike.
I can get more people than expected.
**Mike Goldsmith** 01:01 Yeah.
**Diego Hurtado Pimentel** 01:04 Everybody…
**Mike Goldsmith** 01:06 Hey, Diego.
**Diego Hurtado Pimentel** 01:07 A…
**Riccardo Magliocchetti** 01:13 Welcome, everyone, to this week's Python 6 call. We are waiting a few more minutes for more people to join.
And in the meantime, please add yourself as an athlete.
And also, feel free to add any topic.
Or share what you're working on.
Thanks.
Okay, I think we can start with Riage.
Yeah, like, we have a bunch of… Dependable PRs.
But I think, the banterbot will close automatically.
When… But when I opened the PR on Core for bumping the versions in the OBLOG files.
So we should probably get closed.
Yeah.
Yeah, but there's a… Usually, stop here, so we need to take a look.
Yeah, anyone want to highlight?
Something?
Otherwise, I'll ask another approvers to please take a look at the review and approve APR columns.
Because I think some… some PRs are missing at the… Second approval, and then we can match.
Yeah, no.
That has been closed, but hasn't move to that.
Okay, so…
**Mike Goldsmith** 04:33 Yeah, I don't know why that's been left in no status, because it's been closed, I would have expected it to go to…
**Riccardo Magliocchetti** 04:38 Yeah.
**Mike Goldsmith** 04:39 dumb.
**Riccardo Magliocchetti** 04:43 This is strange, but yesterday at OpenAPR.
**Mike Goldsmith** 04:47 Yeah.
**Riccardo Magliocchetti** 04:48 I just closed, like…
**Mike Goldsmith** 04:51 It deleted their fork.
**Riccardo Magliocchetti** 04:54 It was a mistake.
CVSWAN, but, like, I don't understand the whole point of this, but… I think Lucas already took a look and combined that, yeah.
**Lukas** 05:15 Yeah, I don't know if we want to allow this, but, like… Yeah.
Technically, there's no way to disable SSL verification.
**Riccardo Magliocchetti** 05:32 Yeah.
Yeah, but I think that one of my colleagues open… I don't know if we open any shown or PR to discuss this.
on the specific Asian side, to add, like, an environment variable to… Like, disabled, SSL and SSL sub-verification.
But, yeah.
And, yeah, la que aussois.
Like, I was looking at… some… some cost stabilization… Issues, and found randomly this one.
were the Spanish name, and, and also, like.
the HTV route, value were wrong.
What?
or not correct regarding the HTTP semantic convention, but also, like, I have a strange issue here with the… only the PyPI.
like, PyPI… test behave differently than the CPython one.
And so, like, I need to take a look, but… Strange issues.
So, I think we'll move with the topics.
Diego, you're… okay, maybe we can take a look at… what we're working on this week. Mike, finishing up the initial declarative config work.
Yeah, like, I think you… I already approved the TrueDocs PR. I haven't looked at yet at the PR moving, declarative config code, in another package, but I'll take a look at that as well. And thanks.
**Mike Goldsmith** 07:35 Yeah, I think that's the last two things that we need to get, like, the initial set of config work. There's more things that we can add to it, and there's a few things I know Diego's been starting to look at, getting the instrumentations be managed by the creative config, so thank you for doing that. But I think moving the config to a new package and setting up the docs link to the upstream spec config compatibility matrix. I think that's a good place where we can say, like, people are able to start using it now.
Which is a really good thing. It's taken a while to get us here.
**Riccardo Magliocchetti** 08:13 Thank you.
I'm Fernivia Lucas, finishing up JSON supportive work.
immediate stability, some… some comp support formed by Mongo, which is the last Database 1. We have a… we don't have a PR yet.
We have a 1… open for Cassandra, one for… I'm Kash.
I guess. Yeah, I've already approved them. I think they're missing just an assertion in the test.
Looks good.
So, thanks again for your work.
And then, on the topics, Diego?
Cause these issues.
**Diego Hurtado Pimentel** 08:57 Right, so basically, I told Cloud to take a look at every issue that we have in a repo.
And tell me, which ones… Could be closed, cloud-produced… these recommendations, so I went and looked at each one of these issues, and reviewed them manually, and I produce a list, below, if you scroll down.
With all the issues that I suggest we close, which is about 30 or something.
I noticed that, Ricardo, you already closed several of them?
But yep, it's, I couldn't… clean up, at least 30… Of our 300 and something issues.
I plan on doing the same.
for, I don't know, maybe for the PRs, or maybe just to check that… we don't have duplicate PRs, or… or PRs that, are not assigned to any issues, or… I don't know, but anyways, if some maintainer could take a look at the list, below, can you scroll down, please, Ricardo?
area. If someone can take a look at that, each one of those issues has a comment of mine.
With a short description, saying what I think it should be closed.
Most of them are very non-controversial, and pretty easy to close, so… This can… can help us, clean up a little bit.
**Mike Goldsmith** 10:47 Yeah, it's great, thank you. For PRs, we introduced a still, like, bot, workflow recently, so that'll try and keep on top of things, so I think there's a 30-day, window for it to be marked still, and then another 30 days, and then it'll automatically be closed. We intentionally didn't look at doing it for issues, but I think… I don't see a reason why we wouldn't want to, because we can easily do something like what you've done here, determine something's not… that can be closed, and then have a stale bot do that as well, and then we can add, like, a not stale, or a, you know, a long-lived label if we want something to live beyond something that has been actively worked on. I think that'll help us keeping on top of this, too.
**Diego Hurtado Pimentel** 11:30 Yeah, it is, I understand, the… Why would we want to close stale issues?
in some very few special cases that I guess we can handle manually, right? There are some long-standing issues that are worth to keep open, because we really are missing something there. But yeah, I think in general.
That approach makes sense.
As long as we can have, like, a mechanism to just make a few exceptions here and there.
That'd be cool.
**Mike Goldsmith** 12:11 Yeah, so I think with PRs, we've got a… I think it's a not stale, or something that says to the workflow, don't try and mark this still, this is intentionally going to be long-lived, and you can do that for both PRs and then for issues, and then it'll just ignore it when it comes to it.
**Diego Hurtado Pimentel** 12:27 Alright, so there you go. Please someone that can closely just take a look. It's, Quite easy and quite satisfying work as well.
Those issues.
Thank you.
**Riccardo Magliocchetti** 12:43 Thanks. Like, my issue with the closing also the issue, is what… You know, Where maybe it's, like, really something really useful there.
Also, it'll probably take a lot of work to… I'll read that one here.
Like, double-check every stellif.
But, yeah, like… I won't block, anyway.
But, like, maybe we should, like, discuss when also… We have more people.
In the code. Anyway, thanks both for you, for your work.
And then we have Carlos.
Status of still PRs.
**carlosalberto** 13:30 Yeah, hello.
Yeah, basically it was going through some of the PRs that have been open for a little while, and I was inspecting some of them, and I wanted to just ask here, maybe have a discussion if that's needed. But yeah, I saw a lot of PRs that probably need to be closed.
or iterated on, and for example, I was trying to separate them, by, you know, category. So, for example, the first 3 PR… and that was from yesterday, so maybe things have changed today. But, for example, the first 3PRs, they… Received the feedback that my tenders asked for, and then after that, it's like, nothing is happening there.
So, probably, it's like… Some maintainers need to do something, or close that, or mention, you know, like, hey, we are not going to do this.
Then the second category is when you have, renovate, you know, the bot doing updates, and then nothing is happening.
And, for example, we have that… we still have that in the coding repo, where very often we don't want to actually apply what Renovate tells us to do, for many reasons.
We just go and close those, those PRs, for example. And finally, there's, like, the last ones, which are probably the hardest in general, and it's when There's something that is not clear, or it may be, like, subjective.
And then the maintainers have to, you know.
have to make a hard call, like, do we… this one is a perfect example of that. Like, there was some discussion, like, maybe this one belongs to country, maybe it doesn't belong to country at all, but basically somebody needs to pull the trigger and say yes or no, or what do we do, you know?
And yeah, basically, I just wanted to raise this here. Yeah, I would like to get some opinions on… in… on these kind of PRs.
**Riccardo Magliocchetti** 15:27 Yeah, like, I remember with Swan, because I think… I said on the issue, too, why not?
Yeah, going through a collector instead of implementing the very same thing in Python.
But, yeah, it was not an agreement, I guess.
**Lukas** 15:46 I think I commented, yeah, this… Shouldn't… I don't even think it belongs in Contrib, to be honest.
Like, we can just close it.
**Riccardo Magliocchetti** 15:57 Yeah.
Bye.
Yeah, like.
**Lukas** 16:01 There's also the third one, the third link on applied status, that one's being superseded by other work.
So we can immediately close that.
But, yeah, we can discuss… Offline.
**Emídio** 16:15 Yeah, I think we can close this one.
I don't remember if your PR was already measured, I don't think so.
**Lukas** 16:23 Sorry, what was that?
**Emídio** 16:24 your PR.
**Lukas** 16:26 Yeah, it's about to be merged, I just need to, Clean up some of the test naming.
**Emídio** 16:32 Okay, yeah. I think once your PR is measured, we can close this one.
**Lukas** 16:38 Okay.
**Mike Goldsmith** 16:39 What was interesting on that one that we just looked at, and it was actually in the done column for the board?
But it's still open, so I'll be interested to see how it got into that state.
**Emídio** 16:50 I reopened it, mainly.
**Mike Goldsmith** 16:52 Okay, and then it's just not moved it back.
**Emídio** 16:54 Yeah.
**Mike Goldsmith** 16:56 That's.
**Riccardo Magliocchetti** 17:03 Yeah.
And by the way, like, thanks, Carlos, for taking a look.
Yeah, like, the issue with the dependable trend of APRs is that usually very Don't work, like, they only update a subset of the stuff we need to update.
Or they just… You know, like, they update stuff we don't want to update, because we are testing all the versional stuff, so it's complicated, but yeah.
**carlosalberto** 17:34 Yeah, as I mentioned before, this also happens… has happened in the repo, and most likely in many SIGs, And, yeah, so in those cases, probably just makes sense to go and close the PRs with the comments. We are not debating this because of this or why reason.
So, you know, those PRs on Clodora. But yeah, totally fine to close, such stuff, if… They don't, they are not needed.
**Riccardo Magliocchetti** 18:01 Regarding the first, group, the year is probably, like… like, lately I is missing a lot of notification, because you have too many, and so sometimes… when I commented, I just missed stuff. So, sorry about that, but that happens as well.
Okay.
So, we come on to the next topic, Diego.
**Diego Hurtado Pimentel** 18:33 Right, so… A while ago, I opened this issue… To discuss how to use AI to help the review process of issues and PR, so… Thank you, everyone who commented there, and their ideas.
I was looking into… A few PRs, and I found a project that, Not this project, another project, I just don't remember which part it was, but… if I could understand correctly what they had done is that they had automated this process, the process that I described there, that I think It, would, be, okay.
a good solution for us as well. So what they do is that they… will automatically close any PR, If the author of that PR is not assigned to the issue.
That PR is trying to close.
And, after thinking about… a little bit… I think it makes sense, because I think it… Forces contributors to follow this approach, where they first need to File an issue.
And then they need to get… A maintainer to assign them to that issue.
And that, is, something that could… It's… requires them to do some human interaction, right? To put some human effort into finding the maintainer, And and also write a good issue that clearly describes what they are trying to do, right? So that… They will get assigned to that issue, and only after that, they can submit a PR.
So, I think that… Could help us, against, PRs that are… Pretty much, A little bit of, like, spam, right?
And, it also forces contributors to actually engage with the community.
to either attend the SIG meeting and ask for someone to assign them that PR. And some… and I think it also fixes a point that Ricardo mentioned a little bit above, if you can scroll up a little bit, please, Ricardo. I think it was your first reply to my comment. Right, the first point the fact that there is an issue doesn't mean that there is an agreement. I… I agree with that statement, that's true.
this process also forces people to defend an issue that is valid, right? So, for example, let's say that I… Anyone can open an issue.
But, we need first to get an agreement on that issue being valid before accepting… That issue to be assigned.
to someone, so that a PR can be opened, right? So… I can, let's say, open an issue, and then people can review it and say, okay, no, this is not a valid issue, so I will never get a chance to open a PR, which I think it's the right approach. So, I wanted to present this approach to you, and get your opinions.
What do you think about this?
**Mike Goldsmith** 22:19 Yeah, I can go first.
I… I definitely feel as though that this would be… I'd worry about that we're almost putting a gate in front of people being able to contribute to the project. I definitely feel as though that we need to improve the quality of submissions that we get. I think a lot of them are generated, and they don't always explain the issue, or… there's a higher… cost for somebody to review code than there is to review an issue, because they've got to take all of it in, think about the complications, think about how it's going to impact all of the rest of the projects, all… there's a lot… there's more complications to it. But I think requiring someone To have an issue that is fully agreed before, being able to open a PR, I think that'll… I think that would dissuade a lot of people from contributing to the project.
I think maybe having some guidelines around the size of it, or the complexity of it, and then try to figure out a way to sort of, like, gauge how much it… that… like, how much… how much pre-work you need to do before a PR is opened. I think that would be… I think that I'd feel more comfortable with that, but I think requiring an issue and it to be assigned before it will automatically close a PR, just… I don't think that'll be a good contributor experience.
**Diego Hurtado Pimentel** 23:38 Okay.
**Lukas** 23:41 Yeah, just to add… add to Mike's stuff, actually, I think I kind of like this idea, at least definitely for the main… Maybe not the contribib rep repo?
But the main repo?
The only part I don't… that I generally like is, like, that… people will need to hunt down maintainers, since I don't think maintainers want to be bombarded with all of this. So, I think that just having the discussion in the issue itself.
And just assigning it, just, like, maintainers can just go through the issues and assign it, and then at that point, they can open a PR. I think that would be… Preferable?
But yeah, actually, I kind of like this idea. At least, for sure, we should close PRs that don't have an issue linked. I think that's, like, a no-brainer, but I also think… that… requiring… Requiring people to be assigned to the issue is… is not a bad idea.
But, yeah, I do understand, like, Mike's point, that it might… Disuade people from contributing, but… It seems like we have… Like, too many, yours, so… I don't know.
**Riccardo Magliocchetti** 24:59 Carlos?
**carlosalberto** 25:00 Yeah, so, maybe I can provide some, additional context. In the specification, we do this, because we were also bombed, you know, we will… we were being bombed with so many changes and ideas.
So, on the… We are doing there something similar to what Diego is proposing, which means that you create an issue, you discuss that.
And then there's a triaging system, a traging team, that goes and reviews those things. If that makes sense, like, in a very obvious way, then we change the status to ready for any contributor to pick that up, including the person who opened the issue.
We advise against creating PRs.
Solely for the reason that very often people wrote a prototype.
And then, like, when they come to us, it's like, we are not going to implement that, period, sorry. And it feels kind of bad to them.
that, you know, they are writing a prototype and doing something else of PR, and then it's, like, probably they spend, like, a week or two weeks, and then nothing is happening. So, there's value in asking them to open an issue first.
And, on the other hand, for example, when people, they want to create a prototype either way, because they find value in that, they can open a draft PR, And then, like, they can iterate on the PR, get initial feedback, or something like that.
And that has worked well so far as well. So you're sharing this, I don't think you have to necessarily do that, and probably you will have to tune the process, and like, like Luca said, probably, like, have something between country and the main repo, and then play along and see what works the best.
Yeah, so you, you have your defined words, maintainers, but I think that, as I was saying before, there was some unexpected, value in this specification.
**Diego Hurtado Pimentel** 27:02 Well, if I may go next. Yes, I wanted to second that, Carlos just mentioned. The fact that, We require, first an issue before a PR, Will not be automatically closed.
doesn't mean that they cannot submit a PR, because many times, it is useful for whoever is submitting that issue to open a draft PR, as Carlos mentioned.
to make it easier to explain what they want to do, right? So, that is still something that we allow to happen.
We are not, what we are not allowing is, an open PR, right, that's, that is, Considered to be, ready for review.
Before all this process happens.
**Mike Goldsmith** 28:03 Yeah, I think that's fair. I think… having… not just playing outright not allowing PRs, I think that was something that I think would feel bad from a contributor point of view. If the guidance was… open a PR, get agreement, and you can create a draft PR, and as long as you don't move it into open PR status, so people have to actually act on it, I think that would be a better experience, because then, as you say, you can sure maybe something, how you'd like to see something happen, or how you expect it to work, but it's still working connection with the issue, rather than just having a PR that doesn't tell you what happens, or, putting the burden on somebody to review it before they've really agreed on the issue and haven't moved forward.
Yeah, I think that feels better.
Yeah, and I think I put a message in the Slack as well, approvers and maintainers can do that assignment of an issue to somebody. So yeah, I think as long as it's… something that we expect the approvers and maintainers to keep on top of as well is, like, making sure that they are reviewing issues, they are assigning them, they are, like, reviewing them for being able to act on.
I think… having everything to be discussed in, like, a SIG meeting would not feel good either, because then we wouldn't have enough time, and it'd be a very slow process for somebody to be able to get into a state to even be able to contribute.
**Diego Hurtado Pimentel** 29:25 Right, yeah, the… the idea is for things to be discussed and initiated asynchronously, mostly, right?
**Mike Goldsmith** 29:32 Yeah.
**Riccardo Magliocchetti** 29:39 for the discussion, I have to… opinions on this. The first one… Is that if we make the assignment mandatory, we also need an automatic way to remove stale assigners.
Because in the past, we have, like, in the past, also in the present and the future, we still have a lot of people coming to issue, saying, could you please assign this to me?
You assign the issue, and they disappear.
**Mike Goldsmith** 30:10 Yeah.
**Riccardo Magliocchetti** 30:10 And so… yeah. And the other thing… Is that… We probably need to understand if… You know, this… Vetting over sunny stuff.
And also, reviewing issue is more costly than reviewing PRs, or at least look at PRs, understand If it's just, like, crap, or slop or something useful.
**Diego Hurtado Pimentel** 30:45 Yeah.
**Riccardo Magliocchetti** 30:45 you know.
**Diego Hurtado Pimentel** 30:46 Oh, sorry.
**Riccardo Magliocchetti** 30:48 No, please go ahead, please.
**Diego Hurtado Pimentel** 30:51 Yeah, actually, I think that, Nowadays, with AI, I think it's gonna… Makes sense to put a little bit more effort into reviewing issues?
Because, code can now be generated Pretty easily, right?
And it's easy to open a PR and just tell Claude, implement this issue, right?
Discussing the issue, I think it's what's the most important, because I think the issue defines the what. The PR defines the how.
And, I'm not saying that reviewing PR is not important, right? I'm just saying that, I think, most of our… BBF or the… I guess it should, move.
Towards to reviewing issues, to make sure that we agree on What do we want to do?
And A little bit less on how we want to do it.
But yeah, that's… So, let's see…
**Mike Goldsmith** 32:04 Yeah, I agree with that. I think more conversation should happen, and issues is a better place to have a conversation than a PR.
**Riccardo Magliocchetti** 32:22 Yeah, they probably shouldn't.
Like, will take a while to find an approach that's, satisfy everyone.
And also, like, We need probably more approvers and maintainers in the discussion at the same time.
Or, like… If I'm looking at the recording and, and your comments here, Dave.
But yeah, like… we probably, like, we know we have a problem, at least. We agree that we have a problem.
Any other comment?
**Mike Goldsmith** 33:02 Just one more. Diego, are you okay, like, fleshing out some… I think you've got some bullet points there. Should we try and, like, build some guidance and just sort of, like, we'll start putting that together as, like, and then we can come back to this and then have that good discussion around what we think the, like, the criteria for each part is?
**Diego Hurtado Pimentel** 33:19 I… I want to expand my… my comment there to include these details that I did not include there, like, for example, draft PRs are always An option, and and the… and explain better… The intentions behind it, and And, the point that you raised, about, not making… the contribution experience, a bad experience for contributors, it's, of course, critical. I think it's… Extremely important, because we don't want to… push people away from contributing to this project, so… I think I need to be, Write again, a comment.
That explains this policy clearly, so that it shows, better How we're trying to implement this policy in a way that it'll it… it doesn't… push people away from contributing to this project. So, as an action item for me, I'll… I'll write another comment that explains this better and includes more details and input you have given in this conversation.
**Mike Goldsmith** 34:36 Thank you.
**Riccardo Magliocchetti** 34:40 Thank you.
But… Emilio?
**Emídio** 34:45 Hey, mine is more, like, please take a look on this PR.
It's, It's, open PR from May, but the user… the contributor already opened it, like, last year.
So, it's almost one year, trying to merge this. Essentially, semiconf… Species that, messaging instrumentations, they should produce, like, in case of salary, the tasks they… Should not be shared spans for every, consuming action.
Which is the case for our instrumentation.
The same company specifies that it should be links, spam links, and not shared spans. And SPR is implementing, is implementing a way to control that.
I left a comment saying that my opinion is more to have this as a default behavior hated than… Heads down, not, not having the… The way to control that, but this will break users, so… Yeah.
I think the change is fine. The referral behavior is still the same, like, having shared response.
I'll do this to some information specified it should be respond links.
And another thing, we don't have the… We don't have the semantic convention opt-in feature on this messaging.
Instrumentations, so we cannot put on the feature gate.
I mean, we don't have implemented it yet on our code.
**Riccardo Magliocchetti** 36:34 Yeah, but, like, probably, like, we can change the behavior, or… When we switch the instrumentation to… To this table, or…
**Emídio** 36:44 symbiot.
**Riccardo Magliocchetti** 36:45 Nice.
Well, it's still, like, it's not stable yet, the messaging is cool.
**Emídio** 36:54 Yeah, student development, yeah.
**Riccardo Magliocchetti** 36:56 Okay.
Like, strange, but where is the… They opt in, but we don't tell. Okay, maybe, like, some… something is there, or something, anyway.
Yeah.
**Emídio** 37:08 part of it. Yeah.
**Riccardo Magliocchetti** 37:11 I'll take a look at the PR, and sounds good to me, like, as a first step.
We can at least introduce the proper behavior in one way or another.
**Emídio** 37:23 Awesome.
**Riccardo Magliocchetti** 37:25 Thanks.
**Emídio** 37:27 Cute.
**Riccardo Magliocchetti** 37:32 Okay.
**Mike Goldsmith** 37:32 Go ahead, Carlos.
**carlosalberto** 37:34 Yeah, sorry, I didn't… I hadn't seen this PR, One question that I have, I don't know if you are aware, if not, I can follow up, but… the… there was messaging semantic conventions for this, and how spans should be modeled, and sadly, it was never made stable, it's still experimental.
I don't know whether, like, the person doing this, they just went and created this according to what they feel is the best, like, you know, their own design, or it's something after some of the conventions that exist, even if they are unstable.
If nobody knows, I can go and check myself.
Because, you know, even though, they were… they are not stable, probably it's useful to try to align with, you know, those ones.
Oh, you mean already commented.
**Emídio** 38:26 Yeah, my understanding is the recommended way for now, which I believe the group believes.
This should avoid the move forward.
So even, like, still not stable, but… The way we think is… We should use spun links.
**carlosalberto** 38:43 Okay, thank you. Makes sense.
**Riccardo Magliocchetti** 38:52 Thanks, Mike?
PR dashboard.
**Mike Goldsmith** 38:56 Yeah, so it's something that we're starting to use in Gen AI and a few other places. I think Java also uses it. So, there's a workflow that, just basically runs periodically, and then looks at all of the open PRs and tries to categorize them based on if it's waiting for maintainers, if it's waiting for reviewers, or if it's waiting contributors.
It's very… so it's a very similar feel to what we get out of our dashboard.
sorry, the PR, project, the GitHub project, but it doesn't rely on it being in the right state, so every time it'll look at the… what the last comment was, if there's been contributions to it, to try and categorize it instead of tell you what… who is responsible for doing the next action, rather than just hoping that it's in the right column, because sometimes we see things in the wrong column, or they don't get reassigned properly.
So I did… well, I've been using this with the Gen AI, and there's a few other places, and I quite like this, because then it's very… it's like a smaller section of things that it wants me to look at, rather than everything.
So I just wanted to see if anybody else was interested in seeing, like, seeing doing something like this. I think Trask has created it as, like, a generic workflow that can be ported across most different repos, so if… I would suggest people to have a look at it, see what it feels like, and then maybe we can adopt it for ourselves, too.
**Riccardo Magliocchetti** 40:18 Yeah, like, I think it'd be great to add.
Like, do you need any… like, do we need to ask admin to enable the workflow, or we can do ours ourselves?
**Mike Goldsmith** 40:29 That's right, yeah, so I think we… I'm… actually, I'm not sure. I think I can look into it if there's interest in doing something like this, we can look at how we would add it too. I don't know if it's a workflow that we need to import from somewhere else, or if we just copy it from another work… another repo that already has it. But yeah, this… it's quite a nice experience, so we can… if we're interested, we can… I can look at adding it.
And it can run alongside our project board as well, it's not going to compete with each other.
**Riccardo Magliocchetti** 40:58 Sounds, sounds great.
Thanks.
**Mike Goldsmith** 41:03 Yeah.
Yeah, I'll, I'll look to see what it looks like for us to add this, and then I'll come back the next SIG or something, and then sort of show.
What it would look like to add for us.
**Riccardo Magliocchetti** 41:17 Cool, thank you very much.
Any other topic? This was the last one?
Okay, so thanks, everyone.
You have nearly 20 minutes back.
Enjoy your rest of the day.
See you.
**Mike Goldsmith** 41:36 Thank you. Bye, everyone.
**carlosalberto** 41:38 Nope.
**Hector Hernandez** 41:38 Thank you.
**Lukas** 41:39 Thanks, everyone.
