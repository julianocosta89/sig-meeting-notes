SIG: Java SIG
Date: 2026-07-16
Duration: 62 minutes
============================================================

## Zoom Recording Transcript

Trask Stalnaker 00:01:28 Good morning. Good afternoon.
jberg 00:01:32 We got a full house today. Everyone must be back from their summer vacations.
Gregor Zeitlinger 00:01:37 Hello! Or still waiting for them.
jberg 00:01:40 Oh, August isn't here yet? That's when Europe goes on vacation?
Trask Stalnaker 00:01:48 Sweet.
Gregor Zeitlinger 00:01:48 We have staggered vacations in Germany, so it depends on where you live.
jberg 00:01:56 To keep the country running? Or, like, is it intentional or accidental?
Gregor Zeitlinger 00:02:00 It is intentional, but it's not to keep the country running. It's related to cars.
To have the highway, not too congested.
jberg 00:02:11 Everyone proceed on your vacations in an orderly fashion. That's very German.
Gregor Zeitlinger 00:02:21 But the Bavarians, they always… keep their own spot. The other states have to rotate, but they have their own rule.
jberg 00:02:33 Bavarians.
John Watson 00:02:39 I mean, they're southerners, right? They kind of just do whatever they want to.
Gregor Zeitlinger 00:02:43 Yeah, that's, that's one way to put it.
John Watson 00:02:46 Okay.
jberg 00:02:51 We have a guest I see today, Marilia from the GC. Hello and welcome.
Marylia Gutierrez 00:02:56 Hello.
Trask Stalnaker 00:02:57 Hey, Maria.
Marylia Gutierrez 00:02:59 Nope.
Trask Stalnaker 00:03:00 Let me bump.
Your topic.
to the top. Wait, what did I copy paste too much here?
No.
Let's try that again.
Was better.
Yeah, yeah, let's start with yours.
Marylia Gutierrez 00:03:20 Sure.
Trask Stalnaker 00:03:20 So that you don't have to stay around for all this boring Java stuff.
Marylia Gutierrez 00:03:24 So yeah, for… well, in case someone here doesn't know, we do have, like, a workflow that every time a contributor… contributor is not a member of Merge APR, they get a message saying, like, hey, do you want to reply to the survey? This is what we're trying to, like.
make things, easier for new contributors, so we want to understand how the things are working for them. So can I gather… So I have a lot of comments from time to time and share. So has been six months since the last time I share. So I separated on the like core and the Java instrumentation, which are the two that we have for this egg. So for the Java one total of 9 answers, average score of 4.
4.8. So yeah, the majority of comments were very, like, positive, saying, like, responsive maintainers, fast turnaround, they were, like.
They really like the the feedback itself, the discussions just like spec alignment, things like that. So was a lot of positive or around a lot of people just putting like no comments on, because one of the questions like anything they feel like could be improved and things like that. So a lot of like nothing to add.
when it was the the people that they reply. So we're more questioning about like asking for more guidance on, like, some process itself. So, for example, like, oh, rerun, like, I didn't know how could I make, like, CIS rerun, or things like that.
this one was, like, what test coverage are expected? That one made me a little confused, because I assume, like, all tests and coverage are expected, but that was, like, the sentence. Also… Things about, like, protected branches, I think people are trying to create things on, and trying to run, and was having a hard time.
And one of them were just saying, like, trust more the people that are creating PRs, but yeah.
For the job instrumentation, yeah, 12 answers, average score.
Trask Stalnaker 00:05:26 Can we pause, can we pause there?
Marylia Gutierrez 00:05:28 Yeah, sure.
Trask Stalnaker 00:05:32 For the CI reruns, Jack and John, I want to share what we — I don't know if you all like this or not. But in the instrumentation repo, we basically have a — I… a job, a workflow that is triggered every time CI fails, so the GitHub actions have a CI failure trigger, or a CI completion trigger.
we see if that failed. We see out of, like, we run, like, 150 jobs. We see if Less than 4 of them failed.
We proactively think, oh, maybe that was flaky, and we auto-rerun the failed ones.
jberg 00:06:26 Yeah. I mean, it's sort of — I think we tried to do retries within our Gradle builds. But there's a whole class of failures, which are at the GitHub actions level.
Trask Stalnaker 00:06:39 Yeah, like, Maven Central…
jberg 00:06:42 Exactly.
Trask Stalnaker 00:06:43 Lo.
jberg 00:06:44 So I'm open to that.
You know, I think always the issue with retries is, like, it might bury the problem, but, you know, we're already in that territory, so…
John Watson 00:06:59 I I was going to my comment was I'm a maintainer and I'm unsure how CI reruns work so there you go.
jberg 00:07:07 Okay.
Trask Stalnaker 00:07:09 I have — in the instrumentation repo, I just added it maybe a couple — maybe three months ago. But it's been really nice, like, not to have to rerun flaky jobs, because, I mean, for all — like you said, we've done a ton of work. Lori has done a ton of work on The actual real flaky runs, Gradle, flaky stuff.
But yeah, there's that class of things that we just can't avoid.
And it's really nice not to have to rerun things.
John Watson 00:07:44 The trust autonomy, the trust autonomy one is a really interesting one that I'd like to have a chat about actually.
Trask Stalnaker 00:07:51 Yeah, let's go in order here, because I had thoughts on this one.
I… because I've had that question in the… because y'all have the code coverage… Piece, which is awesome, but it… it isn't… clear, like… That if I submit something, sometimes it's red, and sometimes that's OK. Or how much effort do I put into crazy mocking stuff to make it green?
jberg 00:08:26 Yeah, so I have, I have an opinion on this, and we could codify this in our knowledge base, and so the way I look at this is like, hey, if you don't want to draw attention to your tests, then exceed the coverage percent.
Right, so if… getting above 90% will just make it so it's, like, a non-issue. If it's below, then all of a sudden it's a conversation. It's like, is it impractical to test it? Is it not worth testing? Typically, the only kind of escape hatch is it's, like, not practical to test, but there are some cases where it's not worth testing, like.
For example, I'm thinking about the generated POJOs for declarative config.
Right? Like, those are generated model classes, and getting absolute coverage on every property, I don't think, is super important.
So yeah, that's how I think about it, and I, I won't necessarily, like, I won't not look at a PR because it's not meeting its test coverage requirement.
But yeah, you know, I can take an action item to codify that, and if anybody thinks, you know, I'm thinking about it wrong.
I can update my, my opinion as well.
Trask Stalnaker 00:09:35 I think this is the most important thing.
And… not sure how to, like… Ideally, like, and I've been kind of… with the — some of the workflows I've been trying to post with this new PR dashboard, I post — it posts a comment into the PR sort of to give people some Guidance on how to.
deal with their PR so that it works well.
In that… I don't know how many, comment… bot comments, like, at what… at some point, if we keep posting bot comments into the issue, into the PRs, the people will just stop reading them.
But yeah, this is, I think, probably the most important thing for people.
But if they're getting quick feedback, then it's probably not a big problem. It's more like if sometimes we don't get to a PR for A few days, and it's sitting there, and… Red, and people might think that's why.
jberg 00:10:45 Travis, I don't know if this is feasible, but the PR dashboard, it shows, like, the CEI status, and it's either green or red. And I'm wondering if there's, like… Some way to express that like.
The required parts of CI have passed, and the unrequired parts have failed.
You know? Because, like, think about the things that can fail in CI. There's link checking, and now one of the optional parts of CI, and it's not now, but one of the other optional parts of CI is the test coverage percentage. And if those fail, they're not deal breakers. We're allowed to merge without them.
And so that's where, like, judgment is involved. Like, did this PR introduce the breaking link? Did this PR, like, you know, introduce lower test coverage? And, you know, we should do something about it, or we should let it go.
Trask Stalnaker 00:11:34 Yeah, that's a good idea. I do think that.
Because A, we should be able — we should be able to check the required status checks pass, which is really all that matters. But users don't really understand that difference.
jberg 00:11:51 Right, that's for maintainer contacts, right?
Trask Stalnaker 00:11:54 And yeah, I do think with that PR dashboard, it's one of the things that the thing I'm working.
one of the… PRs I'm working on there is going to — for that static test text, the static text that it posts.
Into the PR, I'm gonna have it be a live status of who it's waiting on, basically. And so if that shows that it's waiting on reviewers as opposed to waiting on author, then that could address — would probably address this concern As well.
jberg 00:12:46 Yeah. And just just to complete the conversation here. So I don't. I'm not necessarily interested myself on having code coverage percentage and integrated into the PR dashboard.
I just, like… I use the PR dashboard sometimes, like the red-green flag of CI, to indicate whether it's, like, in a state for me to review.
And I think if all the required status checks are passing, then it is in a state to review, even if code coverage isn't high enough. But, like, if everything's red and CI is failing across the board, like, I want the author to, on their own accord, go and fix that up before I spend my attention on it.
John Watson 00:13:26 Gregor has a question.
Gregor Zeitlinger 00:13:31 And… I was wondering about this automatic rerun if only a couple of jobs fail. Maybe it would also be feasible to automatically let Copilot figure out if this is something that can be fixed right away.
We get better over time.
jberg 00:13:57 You mean like a transient failure? So somehow have Copilot investigate that transient failure and possibly do something about it?
Gregor Zeitlinger 00:14:06 Yeah, exactly. Because when I encountered that, I have a couple of times already asked the agent to investigate that and create a fix. And usually it's not that difficult because it is waiting for some condition or making some float comparison more lenient.
jberg 00:14:24 Right.
So those…
Trask Stalnaker 00:14:27 Those flaky tests we have, that's what we use the velocity for.
So if it's an actual flaky test in the test code, like Gradle is running, and our tests fail.
We auto-rerun them, but the Develocity has a really nice dashboard that you can see all your flaky tests, and that's what Lori has used to To… fix those kinds of things. So those are already tracked, Gregor.
Gregor Zeitlinger 00:15:00 Okay.
Trask Stalnaker 00:15:08 Cool, let's go to the next… How… Protected branch jobs behave.
Anybody have ideas what that means?
Marylia Gutierrez 00:15:23 So I, I was actually looking for the, the phrase, exact phrase in case that helped, but yeah, it was still a little generic. I was saying like, one possible, one possible improvement could be a bit more guidance for first time contributors around CI behavior and then parenthesis, for example, how and when to rerun failing jobs, especially on protected branches.
jberg 00:15:45 Nobody should be working on protected branches except for maintainers.
So that that that part is a little bit confusing. We everything is run off of forks.
Jack Shirazi 00:15:57 I wonder if they're talking about maintainers have right access, but the PR person doesn't, so can't do a rerun, which is what I find all the time.
jberg 00:16:10 Right.
I'm not sure what other folks think about that. Like, I want to communicate to a contributor that if your build failed because of something that seems flaky, we're not holding it against you. Like, our build is is a constant fight against, like, transient failures. It's a constant uphill battle, and we're working on it all the time. And, like, if you get a build failure, it's not necessarily because of you, and I'm not holding it against you.
Jack Shirazi 00:16:42 So that's what I.
Trask Stalnaker 00:16:43 I like about the auto rerun.
jberg 00:16:45 Okay.
Jack Shirazi 00:16:46 From the other side, from Pierre.
Okay, I got… person has generated a PR, my assumption is that if it's read, it's not going to be looked at.
So I have to get it green. So if it's a transient failure and I don't have the ability to rerun it, what I have to do is do a fake commit, you know, some minor change in order to get it to bump and redo it again, which I've done quite a lot of.
Jason Plumb 00:17:12 But keep in mind, this survey was for new contributors, and they might not be in that mindset yet, right? If they're just… if they're just coming to the project for the first time, first PR, they might assume that every PR is getting attention, right? Regardless of build status, regardless of… Whatever. Coverage.
Trask Stalnaker 00:17:30 But I think this comment, my read of this comment is that it is what Jack Shirazi is saying.
Jason Plumb 00:17:38 Yeah.
Trask Stalnaker 00:17:39 You know, people who aren't from, like.
In the know, or going to… like, it is a reasonable assumption that if it's read, that it may not get looked at.
jberg 00:17:51 Yeah, so…
Trask Stalnaker 00:17:52 responsibility to fix.
jberg 00:17:53 The solution seems twofold and kind of straightforward. One, automatic reruns like Trask is talking about. So that'll take this away a little bit. And then the other thing is communication.
So, you know, updating our contributing guide, and just like we're saying, like, hey, how to interpret falling below the test coverage requirement, you know, similarly, we can communicate, like, hey, if… if you have… if you have one you know, build stage that's red, and everything else is green, and you think it's a transient error, trust us, like, we're not holding that against you. So, something along those lines, just to communicate expectations.
Trask Stalnaker 00:18:32 And I think if — I think if I get this working well, this could go a long way.
towards, because it's very… will specifically say, if it's waiting on author, it'll say, for X, Y, and Z reason, like, you haven't resolved these discussion threads.
CI… maybe if we decide what to do about CI.
Marylia Gutierrez 00:18:57 Did you add the workflow here for the first time contributor? I don't remember if you added for.
Trask Stalnaker 00:19:02 No,
Marylia Gutierrez 00:19:04 Because one thing that I was thinking, like, yeah, for those who don't know, like, that we have, like, that share workflow repo, and I added a new one there, that is, when the first time that the person opened a PR, it shows a few messages of things that they can expect, for example, sign the CLA, or like, this is our AI policy, wait at least a few days before tagging somebody, and stuff like that, but there is also an option to add things specific for the repo, so you can Add.
the like that workflow to this repo.
Not… not this one. This is the survey on merge. It's the first time… For some, yeah.
Trask Stalnaker 00:19:41 Oh, okay.
Marylia Gutierrez 00:19:42 So this one, if you see, there's, like, a bunch of messages, and you can actually pass things that are specific for your, repo here as well. So here you could add things that are… Yeah, here's the example of the message. But yeah.
Trask Stalnaker 00:19:59 And how does it know first-time contributor?
Marylia Gutierrez 00:20:03 There is, like, you normally can see when a person opens the first time, there is, like, the flag, like, first time contributor, so it's kinda like they have first time, they're, like, non-computer, there's, like, a couple of things they need to check, so it's only gonna show for that case.
Trask Stalnaker 00:20:19 Nice, nice.
Alright, let's go to the last one…
John Watson 00:20:29 Yeah, the trust autonomy thing is something I think we should probably add to our contributor guide just to emphasize how Paranoid. We have to be.
Building something so foundational as the core repository that this thing is going to be the foundation of a lot of.
kind of… a lot of libraries. We list… that's what our goal is, for it to be foundational to a lot of libraries, and given the current, you know.
environment of supply chain attacks and other AI bombs and all sorts of things that can happen, we have to be super paranoid and really make sure very carefully and restrict people's autonomy because of that.
But I think we should just probably document it.
jberg 00:21:21 What would increased trust slash autonomy look like?
Trask Stalnaker 00:21:26 Yeah, I didn't really… I was surprised by that response.
John Watson 00:21:29 I'm guessing it's more like, hey, I want to make this change. I think it's more like, I want to make this change. And we're like, no, we have very strict guidelines about what goes in here. We're going to be very careful about the size of your changes. We're going to make sure that it's in line with the specification. Like there's all of those things that reduce contributors and our own autonomy.
And we do document some of that stuff, but I think it's important, probably important to maybe include it in that first-time PR stuff as well. Like, just kind of our… the way our stance has to be.
in this core repository.
and it's going to be hard. And also it's going to be hard for 1st time contributors, no matter what in this repository, because it is so complicated, and there's so much going on, and it's so foundational.
So anyway, those are my thoughts on that.
jberg 00:22:25 Mmhm.
Trask Stalnaker 00:22:27 Amelia, was there any, more context.
Marylia Gutierrez 00:22:31 No, this one was very like, please trust more the devs or something like that.
John Watson 00:22:39 Yeah, I think my point is we can't trust the devs.
Marylia Gutierrez 00:22:41 Yeah. I'm just kidding I don't even trust myself, okay.
jberg 00:22:45 I trust you know. Exactly.
John Watson 00:22:48 Exactly, exactly.
jberg 00:22:52 Cool. This is a polite no.
Marylia Gutierrez 00:22:54 Yeah, yeah.
John Watson 00:22:56 Well, I think it's more like, let's, let's document why we're really, we're so paranoid because I think it's important for people to realize why.
Marylia Gutierrez 00:23:05 By the way, I was just looking for an example. I just shared here one example of that first time that we added on the JavaScript, and that one, people keep forgetting the changelog all the time, so I actually added the difference of changelog, so you can see an example of, like.
When there is default messages and an extra just for your repo, they're all together there.
Trask Stalnaker 00:23:31 Oh, nice.
Alright, well, let's try to… Time box here, probably, a lot…
Marylia Gutierrez 00:23:42 It's very similar, yeah, it's very similar. The same thing, like, for the, like, total answers, 12 average score, like, 4.9. The similar comments, like, high satisfaction, like.
So, it's kind of funny, we see a lot of, like, so fast responses, and then the next thing is, like, so long, like, slow responses, like, okay, yeah. But yeah, I think, like, a lot of the confusion was a lot of, like, I got the approval, or, like, already got, like, part of the approval, but it was, like, not merged, so I think.
Trask Stalnaker 00:24:14 It was awesome.
Marylia Gutierrez 00:24:15 So, like… So okay, I already got the review like, should I tag people to merge? So it's a little like, what is the etiquette here like to deal with this.
Trask Stalnaker 00:24:25 That's a good one. Yeah, I've seen that actually a lot, where, like, one of… Yeah, look, we'll get a approval, but then… We don't merge right away to kind of give some time for other people to look at.
But, yeah, the authors get confused. They regularly ping us. Now what?
Marylia Gutierrez 00:24:49 Thank you.
Trask Stalnaker 00:24:49 Can this be merged? Yeah. I was like, we… yeah, yeah.
Yeah, let me think about… about… That, that's a good one.
Marylia Gutierrez 00:25:00 Yeah, sometimes when I don't mind that, like, I, when I feel like, no, it's ready to approve, like, approve something, and then, like, somebody can merge. If I, like, I'm approving, but I want someone else to still, like, take a look, I usually put a comment, say, like, I'm approving, but I would like someone else to still take a look before we get this merge. So at least, like, the author knows that.
We're waiting, but yeah.
But yeah, those are, like, the feedbacks. I think, like, in general, this is, like, this group was doing very well, a lot of good responses. You can see from the score as well that people give a lot of fives and stuff like that, so, awesome work for everybody here.
jberg 00:25:44 Marilia, what's the what's the OpenTelemetry org average?
I'm trying to understand, you know, how we're doing against our peers.
Trask Stalnaker 00:25:53 I'll give everything.
It was fire.
Marylia Gutierrez 00:25:55 No.
Trask Stalnaker 00:25:56 Norm.
Marylia Gutierrez 00:25:57 So the lowest that I saw was four, the highest was five.
because, like, for example, collector country, we had 76 replies.
So it's… a lot more comments there as well, but yeah, there are a few that have, like, 5 people that reply, and all of them give 5. But yeah, the lowest that I saw was 4.
Trask Stalnaker 00:26:22 Collector contrib is a rough repo.
Marylia Gutierrez 00:26:24 Mmhm.
Trask Stalnaker 00:26:25 Tough repo.
Marylia Gutierrez 00:26:26 Yes.
Jay DeLuca 00:26:28 One, one thought about the last one, the approval. I know a lot of times there'll be, Like if one of you guys, Traska or Lori, approve it and you have the intention of merging it, but you're giving it time, you'll add the milestone. Maybe if we just have automation, maybe we're getting into automation exhaustion territory, but that adds another comment that is like, hey, the intention is for this to be included in the next release.
No further actions needed, or something.
Trask Stalnaker 00:27:01 I like that.
Because that's usually the… Yeah.
how Laurie and I have worked.
Gregor Zeitlinger 00:27:11 But isn't that.
Trask Stalnaker 00:27:12 what…
Gregor Zeitlinger 00:27:13 Isn't that a bit redundant with the PR dashboard? Because it already says who's acting on it, and we are already posting a comment about it.
Marylia Gutierrez 00:27:24 Well, but the contributor doesn't know that.
They they don't know that you have a dashboard that you're looking.
I like the first time. We do.
Trask Stalnaker 00:27:32 They will with this.
So the goal of this here is to update that comment on the PR live.
With who it's waiting for, so it would then say, waiting on maintainers.
Gregor Zeitlinger 00:27:53 Yeah.
Trask Stalnaker 00:27:53 Might be worth… Let's see if that addresses… I'm sure we'll get, like, regularly we have that question, like.
once a month, so I'm sure if it doesn't work, we'll… somebody will tell us.
Marylia Gutierrez 00:28:08 Okay, you will see me again in 6 months, unless I get a lot of replies, I try to show up earlier, but yeah.
Gregor Zeitlinger 00:28:15 And now that we're talking about this dashboard, I wonder if this is only meant for hotel projects, or if this is… Can be used in any project.
Trask Stalnaker 00:28:25 It's only meant for hotel projects. I have no… No extra bandwidth to support other people.
jberg 00:28:34 I did see, what's his face? Yuri from Jaeger, posted a link to the, or link to the, the OTEL Java issue dashboard, or PR dashboard, and it was like, hey, should we do this in Jaeger, so… And.
Yeah, I would not say that you should try to support other things, but like.
If other people want to copy-paste, go for it, right?
Trask Stalnaker 00:29:00 Yeah, also, I'm running — like, there's actually two resource constraints that — Oh.
I guess you could make it — so the resource constraints are — currently, the way it works is it all runs in that shared workflows repository.
Meaning, all the workflows actually Run… they don't run in the individual repos… They run over here, the token needs… It uses… it uses… it runs into GitHub rate limits. It was. I did a lot of work to reduce… to, address that, but the more… at some point, we're gonna hit that again with just the number of Hotel Repo is probably… I gotta figure out what to do about that. The other is it uses my GitHub Copilot, token for the LLM, resolution, and it's just using a mini model, and it does really good caching, so it's… not.
Very expensive, but… yeah.
That's the other problem.
Marylia Gutierrez 00:30:20 The other option is just remove the collector contrib. That was the one causing all the hits.
Trask Stalnaker 00:30:26 Okay.
Marylia Gutierrez 00:30:27 As soon as I.
Trask Stalnaker 00:30:28 Yeah, I.
Marylia Gutierrez 00:30:28 Later on, it was like, yeah, I spent a day.
Trask Stalnaker 00:30:31 Died.
Marylia Gutierrez 00:30:32 Yeah, I died, and I spent a day fixing a bunch of stuff just because of Contrip.
No.
Trask Stalnaker 00:30:38 Yeah, it seems to be good, working well now.
For now. But it's going to hit that threshold again at some point. I can request from GitHub to increase the rate limit.
for a specific GitHub app. I'm not sure how to do that yet, or if that's regularly granted, but that's one of my next things.
Gregor Zeitlinger 00:31:05 I mean, even better.
jberg 00:31:06 I did.
Go ahead, Gregor.
Gregor Zeitlinger 00:31:09 Even better if they would implement this feature natively, it seems to be badly missing.
Trask Stalnaker 00:31:14 Okay.
They're doing some… yeah, yeah, yeah.
Yeah.
No, it's been cool to see that a lot of people have liked the… the dashboard's been helpful, kind of broadly, not just… Like, I did it for my needs, my desires, but it… Seems that it has one of those tools that Has worked well across repos.
jberg 00:31:44 Josh, you reminded me that I can delete my Copilot token from OpenTelemetry Java secrets because, since we switched to the shared workflow, we get to leverage yours now.
Trask Stalnaker 00:32:00 All right. Thank you, Mirelia. This was great.
and this is from… this is a project of the… Is the contributor…
Marylia Gutierrez 00:32:11 Consumer experience.
Trask Stalnaker 00:32:13 SIG.
Marylia Gutierrez 00:32:14 Yep.
Trask Stalnaker 00:32:15 Fantastic, so thank you to that whole group.
Alright, let's talk about… 3, 3.
I think… Gregor, I think I've got my head around… this… So I just need to review — continue reviewing those PRs. And yes, I think I — I think I just need to spend some more time, but I don't think I have any open questions there.
This one… I've just… Thought of while looking over this.
PR again.
In the Spring Boot Starter, we want to… migrate to declarative config. Our idea was to deprecate the old config properties, access… Right. Being… And… Lean into the config provider.
only M3O. Right.
But config provider is not stable.
Gregor Zeitlinger 00:33:45 Right? Yeah, that's that's an angle that I have not thought about right.
Trask Stalnaker 00:33:49 Me either, yeah.
So… I… I think, Jack, this is probably not They're… they're still… This is probably still, Couple months away, at least.
jberg 00:34:07 Config provider is… is… is… the API, that's the thing that's linked to the unstable part of the spec.
So we're blocked by other languages adopting that actually trust.
Trask Stalnaker 00:34:22 Oh, okay. Got it. So the only thing that's stable is the config file format.
jberg 00:34:31 The file format, the simple create and parse operations, and the data model, so that… which is, you know, comes from the format, or is, like, intertwined with that. So, that is what I am trying to stabilize at a programmatic level in the core.
Trask Stalnaker 00:34:52 So… Yeah, go ahead, G.
Gregor Zeitlinger 00:34:54 If I think this through, you're you may be implying that We have to… Keep supporting config properties because the starter is stable.
Trask Stalnaker 00:35:10 Right.
Gregor Zeitlinger 00:35:12 And that in return means, We cannot deprecate… The old bridge.
Is that right?
No, it's more nuanced. We have declared the spring starter stable, but we have not said that declarative configuration in the spring starter is stable.
Trask Stalnaker 00:35:40 Right.
Gregor Zeitlinger 00:35:41 So, all we have to do is undeprecate.
Config properties… In, the… what's in the properties mode, and then… then we're safe.
Yeah, that's a good Good one.
Trask Stalnaker 00:36:00 Cool, awesome.
All right, let's talk messaging semantic conventions. This just kind of came up recently.
And… For a brief moment I was. So the problem is that messaging semantic conventions are in a limbo state right now, where But… They're not stable.
They've diverged from the baseline, the de facto stable, whatever was declared.
Open up.
So… The idea was that messaging.
Like the other SimConf, we froze it at… a particular de facto stable version. And we said, you shouldn't.
Update the version of this.
that you emit, except under, you know, some kind of flag. At least don't change your default.
Until it's stabilized.
And unfortunately, it's been unstable for… Year has been in this process for years, and the messaging SIG has been, It is not… hasn't been active for… over a year, and it's not clear when it will be active again and pushing towards stabilizing things.
So, that leaves us kind of in a weird state, One of the ideas of this was that.
You would only want, like, we could use the 3.0 version, major version bump, we could make breaking changes, we could sync to the latest.
Messaging semantic conventions.
But that could get us out of sync with other… Languages… I don't know. I probably need to do some more thinking on this.
I had… kind of… I was thinking, okay, if we did… Update… if we did use 3.0… It's not as hard, it's not that… Like, there's nothing like database semantic convention update, it's… reasonably straightforward. I think it's something we could do.
But now I'm thinking maybe we shouldn't change the default, but… We could still do this work to update our things under the preview flag.
So, I don't know, that's me rambling and not having… Quite. But does anybody have… Thoughts or feelings about this?
Laurie, were you pretty neutral? I know you're on vacation here, so thank you for even joining in if you're just barely listening.
Lauri 00:39:49 I don't know what the other Sikhs are doing, but at least for us. I think it's We aren't currently following any of the semantic conventions.
But like the the original issue, I think, which started this discussion was that We wanted to add some additional metrics, and the question was, should we follow, like, the latest Semantic convention.
Or some older version of it.
Trask Stalnaker 00:40:28 Okay, yeah, let me — I'll do some more research. But I'm thinking — Against doing… changing the defaults?
Well, unless it's… I mean, we could introduce breaking changes, but still pinning to… like, I think the defaults, we should probably pin…
Lauri 00:41:00 Two, one.
Trask Stalnaker 00:41:01 Wanda.
Lauri 00:41:02 I think one of the problems with the messaging semantic conventions was that at this, like, usually to… I think it suggests to use one 24.
And.
But for messaging around that time they were experimenting with this Let's put all the things into separate traces and link them with span links.
And later.
They reverted that decision, and actually In later versions of the spec, what they recommended became closer to what we were already doing.
Trask Stalnaker 00:41:46 Oh, right, right.
Lauri 00:42:00 So yeah, you have to be a bit careful about what version do we actually choose.
And even with, like, the metrics that, like.
We have this receive metric and send metric, but we don't have a process metric. I think in 1.24, instead of process, they were using deliver, but in… In later versions, they started using process again.
So in that sense, like, I think using 124 didn't seem ideal.
If I remember correctly.
Trask Stalnaker 00:42:41 Would it be… Would you… would you like to see the default behaviors?
Change, or do you think… Just doing all of this work.
Under the messaging preview flag.
would…
Lauri 00:43:03 I think, changing defaults is probably too much effort.
Trask Stalnaker 00:43:12 Okay, so… Kind of… because that's… Kind of the path I was going down here, minus… I was thinking to change the default, but… pulling back on changing the default. All the other stuff is just… Implementing, basically, the latest under the preview flag.
Lauri 00:43:36 I think there are, like, multiple things there, like, one thing is using the latest version of attributes Which, I guess, sort of would be fine.
But they also introduced some changes to the trace structure.
They also have those, like, acknowledge or settle stuff that we haven't implemented at all.
Trask Stalnaker 00:44:01 Yeah, I was intentionally not… Thinking for now, at least, to implement the new, like the subtle and acknowledge pieces.
But the trace structure thing… I need to check, I'm not… sure if I got that right or not.
Lauri 00:44:28 They also have, like, the separate, like, receive traces enabled flag. I don't know how that will relate to the… latest state of the spec. What I was thinking was that, like, since we only have one messaging instrumentation that emits the messaging metrics, was that maybe it would be easier for us to immediately start using the Metric names from the current.
specification.
No.
Trask Stalnaker 00:45:01 From 1-24.
Lauri 00:45:03 Yeah, but I think in earlier versions, you have multiple different metrics. You have different metrics for receive and process, but in the latest version, you have a metric per client operation or something like that.
Of course, it would be weird, because, like, if we take the metric name from the latest specification, but stamp the old attributes on it.
Maybe it creates more confusion than, not necessary.
Trask Stalnaker 00:45:33 Yeah, that's where… My thought is to add all those metrics, but only under the preview flag.
So that, we're not out of line with semantic conventions and other Languages which are, at least in theory, supposed to be pinning to 124 for default behavior.
Lauri 00:46:02 Well, there definitely is some interest in, in getting the latest messaging, Same con we implemented. I think there have been, like, two attempts, but poof.
haven't led to anywhere.
Because of various reasons.
Trask Stalnaker 00:46:24 Yeah, so that's… I mean, basically what I was… Kind of tackling here, and… I bet.
I can… I can… Continue down this path.
I don't think as to… Too much work.
The key decision that I just I want to nail down is whether We, All of the new stuff is only behind the… preview flag versus… changing any default behavior, even in 3, even with the the 3.0 bump.
Lauri 00:47:16 I guess, like, the banner in the semantic conventions that says that That instrumentations shouldn't implement the latest version by default.
Kind of forces us not to use it by default.
Trask Stalnaker 00:47:36 Yeah, I mean, I could… I can… I could push on this.
you know, semantic convention, Sig.
In terms of, like, hey, we are taking a major version bump.
We're okay with breaking our users… And then breaking them again in another major version bump later.
And that's sort of where I was thinking, oh, that would be okay, but then I realized that that that would… put us… It could be weird for… Multi-language… Services… If… our defaults are different than the defaults of other language instrumentations. So in that case, I think there's a good argument for sticking to… what the SEMCONF says.
Lauri 00:48:30 Do you know, like, to the other languages.
Implement the messaging same column at all.
Or what, what are they doing?
Trask Stalnaker 00:48:42 I haven't looked. I'm sure that there is.
So… I could definitely… Check.
Lauri 00:48:54 I think, like, whatever they are doing, they're probably not aligned with us.
Trask Stalnaker 00:49:01 That is… Bear, I mean, well, your point about us not… we didn't… We have a… we have kind of a mishmash.
Lauri 00:49:13 Yeah, but I think it was necessary because the semantic conventions at that time were like… Didn't really make sense, I think.
Pushing for the separate traces, It was problematic because the backends didn't support span links.
And I think they still probably don't support it too well.
Trask Stalnaker 00:49:39 So does that meet your main question, sort of, of what other languages are doing as related to trace structure?
Lauri 00:49:49 I was just curious.
Trask Stalnaker 00:49:51 Yeah.
Lauri 00:49:55 Like, maybe, like, the only thing that… Possibly could be important is, like, If they are emitting messaging metrics, then, how… what are their metrics names, and what attributes do they stamp on them?
Because, like, like theory. I think it could be valuable if we manage to align with other instrumentations.
Trask Stalnaker 00:50:29 Yeah, no, is there, really good questions.
I will do some more research on it.
The impact on 3 0.
Basically, is… If we want to change the default behavior.
In 3.0 with a breaking change there, then I want to get it into… I think we would… Push the 3.0 release by one month.
So that we could… I would want the… I still want all the 3L behavior changes to be in the last 2X… Minor release under the V3 preview flag.
which, I mean, I'm okay with pushing… They're released by a month.
For a good cause.
it's…
Lauri 00:51:30 I think we probably shouldn't change the defaults.
But what we could do is implement the messaging metrics.
I know that the… Well, that's what this is.
Trask Stalnaker 00:51:47 is…
Lauri 00:51:48 It was implemented a long time ago.
at one point, I considered implementing, like, copying it for all the other, like, Messaging instrumentations, too.
But for some reason I gave up, but I don't remember why exactly, but I remember that.
It somehow got more complicated than it seems.
Trask Stalnaker 00:52:12 Bear, I will keep that in mind.
Okay, so I… I will… I probably need a… Couple… There's the… dig in further and also evaluate. I did — I have reviewed this, but I haven't reviewed Copilot's work on these follow-up PRs, draft PRs.
See where it's… Going.
but I will probably go ahead and proceed with the… I won't hold… I won't hold for 2.30 for any of the messaging stuff.
Okay.
Anything… else about… 3 0.
I don't think so.
CLAB, And then on the 2 dot 30.
PRs… Gregor.
Do… are these… I guess if we're not going to remove… That, so maybe that's not tied to 2.30 anymore.
Gregor Zeitlinger 00:53:49 It is. I'll just make the change as discussed.
Because for the DC mode, I still want to have that change in.
Trask Stalnaker 00:54:02 Yeah, it would still go into 3.0, I just mean whether we need it in 2.30.
You wanna…
Gregor Zeitlinger 00:54:12 Maybe, maybe not, but I'll double check.
Trask Stalnaker 00:54:15 Okay.
I think we probably can. I think… I think it was… I was pretty comfortable with this, so I think we can… Still target that. I probably won't make the release till tomorrow.
At the earliest.
Contribute this one. Is this needed for 2.30?
Because this one might…
Gregor Zeitlinger 00:54:44 That's a bit more difficult to answer. My rationale was that For CONTRIB, we want to do the switch as well, but CONTRIB is not, Using the same release schedule, so I'm not sure if this is tied or not tied, or if we want to have it done by then or not.
Trask Stalnaker 00:55:10 Okay.
I will… I'll spend some more time, I think… I have my head wrapped around this now, and I just need to look at the… the implementation.
Gregor Zeitlinger 00:55:25 Mmhm.
Trask Stalnaker 00:55:27 Remove JMX registration requirement. Okay, this is, yeah, just not… Oh, yes.
This one… Maybe Laurie probably left a reply to my question.
I'm… I 100%. I'm good deferring this to you, Laurie.
Lauri 00:56:11 Well, it is something that probably nobody is going to use, I think.
But it's just for completeness, it, or maybe… Maybe one area where it could help is It's with the terminology that we have.
Currently we have like this India or inline and non inline.
Maybe this strategy is then, like, the… To think that… Distinguishes those different modes of instrumentation.
Trask Stalnaker 00:56:48 Okay, yeah.
Makes sense. Let me, I will… I think I understand the angle you're going at. I will…
Lauri 00:56:57 Open.
as I said, like, could copy-paste it back to the experimental interface, too.
Trask Stalnaker 00:57:04 Do we have the experimental interface anymore?
Lauri 00:57:06 Yeah, sure.
Trask Stalnaker 00:57:08 Okay.
Lauri 00:57:08 There's other experimental stuff.
That we kind of need, but don't want to commit to.
Trask Stalnaker 00:57:17 Okay.
Cool, I'll just… Do one of those two things and merge it.
Okay, that and that not really. Okay.
Perfect.
all right. Sorry, you did use up all of our time.
Annie, in our last couple minutes. Anything.
that we… should prioritize.
jberg 00:57:53 I want to quickly advertise my Bound Instruments PR. I think it's ready to go. It's low risk because it doesn't affect the performance of the stable path at all. And it just introduces new incubating APIs.
That have quite good performance characteristics across the board at this point. If you've got some time to look at it, please do.
It's a nice feature.
Trask Stalnaker 00:58:21 Nice.
Puneet Singh 00:58:26 I think the spec thing will need more time, so I'll post the message in the Java channel. I brought it here because I thought that there will be the initial feedback that I need might have a… I might get a good response from this SIG, based on the work that is happening right now in dynamic control. So yeah, I'll post the message in the channel.
Trask Stalnaker 00:58:50 Sure, and, with… Should have more time, or we should have time to get to things. Like, I would still — Sylvain, let's plan on discussing this and these next week.
And yeah, we just had a couple of big topics today.
So yeah, feel free to… Throw it on next week's agenda.
jberg 00:59:14 Vineet, I'll follow up with you async as well, just so, like, in case you don't want to wait for a synchronous conversation next week. I did a lot of that work with meter configurator and the spec related to that, so, yeah, if you're interested for dynamic control, I'll follow up.
Puneet Singh 00:59:28 Sure. Sounds good. Thanks.
Trask Stalnaker 00:59:34 And This one, yes.
Yes.
Cool. Yeah, I will get this one merged. I think I didn't have anything else.
on it. And thank you.
to Jason for reviewing it.
I don't see what metrics proposal.
Okay, I'll read this.
Alright, folks!
Felix Wong 01:00:08 Yeah, so, yeah, sorry to… Oh, Felix. Yeah, so I would like to bring up the… Yeah, the backporting the CVE fixes to earlier versions of OpenTelemetry Java.
So the reason why is we have a micro profile telemetry project as part of the micro profile umbrella that we specify what version of the Java that we are using in a particular version of the spec.
And we have, I mean, with the oldest version of this spec that only using the trace of the OpenTelemetry Java. Back in, like, we were using, like, one dot.
19 version. And it is not practical to jump from 1.19 to 1.62. And then with all the excess like logs and metrics and a lot of new functions like So that's not easy, so I'm proposing to backporting the, fixes of the CVE45292 back to A few versions that we need, and we can… contribute the PR, but probably need you guys to help to make the branch and do the release.
Trask Stalnaker 01:01:31 Yeah, apologies, Felix, that we are out of time today. But would you be able to join? And I mean, I think the you got kind of a standard answer in the issue.
But I think it's worth some more discussion and color to understand, you know, how it affects micro profile and what we You know, if there's anything we can do to support you.
Felix Wong 01:01:58 Okay.
Trask Stalnaker 01:01:58 Would you be able to join next week? I'll put you on the top of the list.
Felix Wong 01:02:04 Yep, okay.
Trask Stalnaker 01:02:07 Alright, thanks all.
Felix Wong 01:02:09 Yeah, thank you.
jberg 01:02:10 But.
Felix Wong 01:02:10 Bye.
