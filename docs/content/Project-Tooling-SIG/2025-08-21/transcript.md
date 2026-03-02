SIG: Project Tooling SIG
Date: 2025-08-21
Duration: 33 minutes
Zoom Recording URL: https://zoom.us/rec/share/vGRde9EyDgxafp5M0fT-vkcowNlwggjVWhZhPU03ChVkNdZSrCFmjZzBKL4Td5tm.Tw9DwfBg22SZA4bX
============================================================

## Zoom Recording Transcript

**Ashley Wolf (GitHub)** 01:06 Hi there!
**Adriel Perkins** 01:10 Hey, how's it going?
**Ashley Wolf (GitHub)** 01:11 Good, we got an invite to join here, from… I don't want to mispronounce his name. We're from GitHub, but we were invited to join this call in lieu of a one-on-one with us here, so hopefully that still works.
**Adriel Perkins** 01:27 Very cool. … Yes, … let me message him, because he…
he said he… he posted in the, Project Infra channel in Slack and said that he's got a call.
**Ashley Wolf (GitHub)** 01:43 Oh, maybe he wants… he's on our Zoom.
**Adriel Perkins** 01:46 I think he might be on your Zoom, yeah.
**Ashley Wolf (GitHub)** 01:48 Okay, let me check. I just emailed him. Let's see what he prefers.
Let's see if he's over there…
we're just hopping Zooms, and… he's not on the other Zoom.
**Adriel Perkins** 02:02 Okay.
**Ashley Wolf (GitHub)** 02:04 I'll keep that one open just in case. But he said this time conflicted with this call, and that I should join this call instead, so Zach… oh, he joined the other one. I will go pop over there.
**Adriel Perkins** 02:15 Alright, cool. Yeah, have a good one.
**Ashley Wolf (GitHub)** 02:35 Alright, we're hanging out here, Zach.
**Zack Koppert** 02:39 Okay, sounds good.
**Antoine Toulme** 02:40 There you go.
**Ashley Wolf (GitHub)** 02:44 Zoom, huh.
**Adriel Perkins** 02:45 shopping.
**Ashley Wolf (GitHub)** 02:46 Yes.
Better than Microsoft Teams hopping, some might say.
**Adriel Perkins** 02:51 Heard.
**Antoine Toulme** 02:54 So…
Sorry about that. I was 2 minutes late, and I assumed that Ashley would be on the Zoom. So, thanks, Ashley, for taking the time with us. I think I sent a little message to the team so they know that….
**Ashley Wolf (GitHub)** 03:07 Awesome.
**Antoine Toulme** 03:08 You were coming, so it's not a good surprise.
I mean, we all have needs for more stuff from GitHub, and Trask has been managing a lot of the minutiae of making all those projects work, and all those repositories kind of work on time.
…
I think I… out of all the repositories in OpenTemmetry, the OpenTeometry Collector Conflip repository is probably the biggest in terms of CI minutes and, waste.
But, yeah, so… I wanted to understand better, like, if there's anything in the works from GitHub in terms of
Collaboration features, or if we're going to kind of continue to do more with labels, or if there's anything that we should know. Where to spend our calories in terms of development.
**Ashley Wolf (GitHub)** 03:59 Well, I… yeah… Just a head….
**Trask Stalnaker** 04:01 Just a heads up, in case Antoine didn't mention, this is a publicly recorded call.
**Ashley Wolf (GitHub)** 04:06 Awesome. Oh, good, thank you for that. Yeah. Well, first, thank you so much for participating in the Maintainer Advisory Network. That's how we came into contact and requesting time with GitHub. We…
I can share or make connections with the product teams, depending on which area it is, or share what's on the public roadmap, as far as I know. …
And if it's an opportunity to share product feedback, we'll help get that to the right folks and share what the use case here is. So, if you can narrow in a little bit around what
hiccups.
**Antoine Toulme** 04:45 True.
**Ashley Wolf (GitHub)** 04:45 hitting, or where there's limitations, or the challenges, so that we might be able to help on our end a bit more. But, like, PRs, notifications, labels, issues, mapping all that to the right people, but just helpful to hear what exactly those pain points are, and then we could share more on our end. And Zach's joining me here from GitHub as well for his first call between GitHub and.
**Antoine Toulme** 05:10 and maintainers, so… Nice to meet you. We'll do what we can on this call.
Okay, sorry to, … let me try to go for something specific to my use case, which is why I wanted to have the call with you, which is that there is no set way of running a workflow to triage and get a PR all the way in.
in, you know, repositories. Actually, most of our repositories have different processes. I can see that between, let's say, Java, or Go, or .NET, or the collector contribib. For collector contrib, we have, at all times, about 140 PRs open.
At any time.
Which is massive. It's very difficult for us to kind of keep up on top of them. Lots of them still out, and we've had the feedback, at least in the last year, year and a half, that people were starting to get really frustrated because we didn't get to the PRs.
And, the CI is complex, runs about…
40 minutes or so, has about 200 different jobs running at any time. It tests for Windows, tests for different versions of Linux, tests for different versions of Go, tests for linting, integration, testing, whatever you want.
There's many, many ways to get yourself cut in that process. And, the… to add insult to injury, we also have, flaky tests that tend to fail on the regular.
So, when you're well accomplished as a repository, you can have… you can circumvent some of that, because you can rerun tests.
Right, so you don't have to rerun the whole shebang for no reason. …
There's some level of, minutiae and bureaucracy that went into this, such as we… we now have the…
the requirement that you must add a lower YAML file for every one of your PRs that says you need a changelog, or you need to put something in the title that says it's a chore, or you put skip changelog as a label. Once your PR is finally up.
then, it stands there until someone actually wants to take a look at it. So we have a little bit of an issue about how to make sure people get pinged on that. We, I think, have a problem with our code owner's ping, so the problem is
We have official GitHub, … things which are, like, triage or approver maintainer, right?
But we also have cod owners who are responsible for just a code path inside the repository. We have 220 components or so.
So, you have code owners who are going to be experts in, let's say, SQL Server, they only care about SQL Server, you want them to be reviewing everything coming for that… for that path.
Well, they don't get pinged. It's difficult.
So, we also don't know when it's a good time to start to ping them. So, I had to do a process recently where I said, I think I'm going to come up with something by myself.
Where every time the CI doesn't pass, or there's a conflict, which is also hard to find, you have to go click on the PR to find out if there's a conflict.
I would mark it back in draft.
Which is thankful.
…
And then, you know, tell them, hey, make it… market ready to review when it's good to go again.
If it's in good shape, then it starts to be ready for a code owner to review, so you have a label for that.
And then waits until such time that it's been reviewed by them.
and somehow, magically, I'm gonna do another pass and find out it's been reviewed and approved by them, because I don't get notified of that, and I'm gonna know to merge that.
This is extremely expensive. Every time I see someone approving a PR, I have to go do the mappings, like, are you a code owner again? I need to check…
the tooltips and all the help you get from the UI in GitHub is not helping that much. And so I spent about an hour or two a day reviewing PRs on this thing. I merge about 5 PRs a day.
It's… it's a battle to stay on top of things.
…
And then, yeah, we have long-running PRs that never get merged, like, we have one with 111 comments on it, just never gonna get there.
…
But for the most part, we also want to make it so that people have a better time. We just added, as of this week, a first-time contributor workflow. I wanted to show that to the infrastructure group here, which is going to post a comment saying, hey, welcome, and here is the contributing guidelines, here is how to work with us.
**Ashley Wolf (GitHub)** 09:23 Nice.
**Antoine Toulme** 09:24 but also put the first-time contributor label on the PR, because then we know to go run the CI for them. Yeah. Because that's another thing, is that they wait for us constantly to run the CI.
So, that's the feedback. Lost Ashley for a second.
Said too much.
**Zack Koppert** 09:42 Yeah, she's like, alright, and that's our time. Yeah, I'm sure she'll be back in a second.
**Antoine Toulme** 09:48 I'm sure I got, like, 4 minutes left with you.
**Trask Stalnaker** 09:51 Zoom crashed.
**Antoine Toulme** 09:53 So… She'll be right back.
Microsoft Teams not so bad now, huh?
**Zack Koppert** 09:58 Oh, yeah.
We'll report that, yeah.
**Ashley Wolf** 10:04 My Zoom was overloaded, sorry.
**Antoine Toulme** 10:07 Sucking too much. … Okay, so….
**Trask Stalnaker** 10:13 give, sort of what's slightly… what's potentially different about the OpenTelemetry repos than maybe your common setup.
So one is that, our approvers can't merge. We don't give them rights to merge PRs, which is different than typical. So it has to go to a maintainer to click merge.
… And we use, the branch protection rule setting to do that.
Which, by the way, is not available in rule sets.
Which is a different alternate,
different issue altogether. But anyway, the other difference about our repos is, like, the contrib repo, like Antoine mentioned, since we have these, you know, lots of different components owned by lots of different people.
We weren't.
We don't actually give them… we don't actually make them real approvers and put them in code owners.
We make… we have a different file that associates that mapping, and so we'd only give those people, basically, like, triage access,
And because we work
Again, just concerned about over-broad… we're giving right access to the repos to all those different people who maintain just a very small little component in this large repo.
**Zack Koppert** 11:53 Okay.
**Trask Stalnaker** 11:53 Because otherwise, if you're doing the common, like, approvers can merge stuff, and approvers are trusted, with right access, then…
Some of these flows work better, of course.
**Zack Koppert** 12:06 That makes sense. So it sounds… it sounds like the main problem is managing PR throughput and review
Along with status of those PRs through the process. Would you say that that's, like, the 30,000-foot view?
**Antoine Toulme** 12:29 Yeah.
**Zack Koppert** 12:30 Yeah? Okay. … So, and then in, in using actions, How…
You talked about not getting notified for things, I'm curious, what's your main window into, like, okay, I'm ready to sit down and spend an hour on, like, working on PRs? Are you on the PR page, or are you in the notifications page, or…
Somewhere else.
**Antoine Toulme** 12:52 I've cleared my notifications a week ago. I currently have 590 notifications for Contrib.
**Zack Koppert** 12:58 Whoa.
**Antoine Toulme** 12:59 The only way I get anything done is I go to the PRs, and I have my, … I search by labels, and negating labels, so for example.
If I want to see what's ready to merge, I'm gonna say draft false, and not waiting for code owners, and I… hopefully I'm gonna have about 30 PRs to work with, and that is a much better file set to, kind of.
look at.
But my goal is to make sure that we move them to the right workflow. Either we put them back in draft, we make them wait for code owners, or we get them merged, right?
There's also a recency bias, for sure. Like, whatever's just on the first page of the PRs gets more attention, at least. And as long as I'm able to do that every day, I'm gonna try to capture up to that first page and make sure we don't leave anything behind.
But once it's been a week or two, and it's sitting there, and it starts to rot pretty quick, so….
**Zack Koppert** 13:51 Yeah.
**Antoine Toulme** 13:52 The problem I'm having is we have not discussed enforcing that as a project. I'm just doing this because I need that, otherwise I'm gonna just lose it. We're doing a weekly report as well of anything that can be used. You can see it's in the issues. We have a report label that, it's associated with the report itself.
We have a stell boat that, after 60 days, is going to close the PRs which are not used.
**Zack Koppert** 14:18 Okay.
**Antoine Toulme** 14:18 we are reaching the scalability of humans here, frankly. So….
**Zack Koppert** 14:24 Yeah, so it sounds like a couple of things are in my mind about, like, …
auto-triaging things. I think the labels are a great programmatic way to do it, but having to go through different label search criteria based on what you're looking for would probably be easier managed in a GitHub project.
Have you used GitHub projects at all?
**Antoine Toulme** 14:48 Yeah, we've done that too.
**Zack Koppert** 14:50 Okay. But we don't….
**Antoine Toulme** 14:51 We don't control…
what people come up with. Like, someone's going to come and say, hey, I decided to go work on the SystemD receiver.
Okay,
**Zack Koppert** 15:00 Sure.
**Antoine Toulme** 15:00 Cool. That's not part of any project.
**Zack Koppert** 15:03 Yeah, so the project wouldn't be, like, a view of a certain project that we're trying to get to completion, but it would be, like, almost your,
your triage part. Right? And so, imagine the columns being things like, okay, under review, needs attention from a maintainer, and then it's tagged with maybe the database expert label. So the subject matter expert knows, oh, okay, this is my column that I pay attention to.
Where they have a view of the project that has that label added. But essentially, what it's doing is it's taking all of your views that you look at for the different PR issues that you filter, right? And then putting that into columns on a board, or specific views of a board.
**Antoine Toulme** 15:47 That's him.
**Zack Koppert** 15:47 Where everyone can use those.
**Antoine Toulme** 15:49 Okay. Or you can switch between them quickly.
**Zack Koppert** 15:52 Yeah, and then, Ashley, I don't know if you have any more information on, like, the auto-triage, or auto-adding labels based on PR state, or an analysis of the PR.
**Ashley Wolf** 16:03 Yeah, there's a… there's a neat initiative that a team at GitHub announced a few weeks back around continuous AI, and the idea that you can
use actions for these workflows continuously off of triggers, whether that's in a use case for triaging, autoresponse, and they can be AI-powered, so it can analyze the
text in the issue, it can look at your issue templates or your contribution guide, and make an assessment of what labels should be added. It doesn't need to take full action, like, end-to-end for you. A human should still be involved and put eyes on it and triage, of course.
But what it can do is help assist with the recommendation around labels and put it in the right places based off of
the instructions that you supply it with. There's a lot of utility tools that have been put out recently in the past few weeks that I would recommend checking out. I can give you a list of those.
pretty… pretty cool to experiment with creating those workflows yourself. I've been doing that on my side a lot for one-off things, but I know your PO… like, the load time for all of your workflows is pretty hefty already, but it might be something that's valuable to consider.
Sounds good. And there are a lot of triage workflows right now. Like, there's, like, I've been trying to open up the repo with the list of examples. There's a good set of them, whether it's continuous or not, or you want to do it ad hoc and just run the workflow one time for yourselves, it's…
to start with, I think is a good place to begin with, but, I think those are immensely valuable for maintainers, especially when you're stretched on time.
**Antoine Toulme** 17:52 Understood, yeah, interesting.
**Ashley Wolf** 17:54 Is that what you were thinking along those lines, Zach, too? Yep. Yeah. Okay, let me grab those.
**Zack Koppert** 17:59 And then, the other thing I wanted to mention was, do you folks have access to Copilot through your,
**Antoine Toulme** 18:07 Possibly.
**Zack Koppert** 18:08 Okay.
**Trask Stalnaker** 18:10 I mean… Right.
**Ashley Wolf** 18:11 You are under CNCF, right?
**Trask Stalnaker** 18:14 Yeah….
**Ashley Wolf** 18:14 Okay, we are….
**Trask Stalnaker** 18:16 I have a….
**Ashley Wolf** 18:16 My T… oh, go ahead.
**Trask Stalnaker** 18:17 Thank you. I have a ticket open with CNCF, too. I've been bugging them every month.
**Antoine Toulme** 18:22 Oh, nice.
**Ashley Wolf** 18:23 So, we're working on, helping to accelerate use of Copilot, making that easier. You all should actually be able to get access to Copilot Enterprise, which is the most robust grade of Copilot we offer, mostly for companies, but we understand for open source, it's needed. So my team has been working with the IT folks at the LF and within CNCF,
to roll that out. So you're all, like, first up in that, queue. So, … Awesome.
**Trask Stalnaker** 18:52 So, that's great.
**Ashley Wolf** 18:53 Let them know, if not, I can ping in our channel that we have shared with some folks there as well. But there's a opportunity to consider, and Zach, you could probably share, like, how to use some of agent mode tools to be able to assist there and do reviews for you, but go ahead.
**Zack Koppert** 19:10 Yeah, so the two things that it sounds like you guys should focus on once you get Copilot access is the, Copilot code review instructions. You can give Copilot an instruction set of.
hey, here's what I need you to look for in reviews, it should have X, Y, and Z. Sort of feeding it your contributor guidelines, as well as any extra criteria that you find that you add on top of that when you evaluate them. You can also ask Copilot, point it to the last 10,000 PRs and say.
based on the feedback that I normally give, and the number of times I repeat myself in a PR, add this to this instructions file.
Then, when you check in that instructions file into the repository, then Copilot will do its automated reviews once a draft goes into, ready for review mode. It'll look for that, and I think that's going to be extremely helpful.
in terms of triaging and getting PRs ready for you guys to actually review versus, to help them get ready to review. And then the other… the other piece is that
I've actually had recent experience with this on my team, where we've looked at CI and said, oh my gosh, this is taking so long, and we're diving into, like, what could be more parallelized, or…
what things are taking the longest amount of time, kind of doing a performance analysis of the CI would have taken somebody a week or two. Copilot had it turned around for us in an hour and a half, and we're like, oh, wow, this is really useful information, and we know exactly what to go do.
And then some of those tasks were even easy enough, or low enough hanging fruit, that we could assign Copilot to go do it and to fix it. And then we reviewed the code and committed it. And that's actually been… we've noticed that Copilot is particularly good at doing… solving problems like that.
the large analysis, and then, coming up with discrete things that can be done to improve, even… or even experiments. Let's try this, and, you know.
Fork the replay, right here, so….
**Antoine Toulme** 21:03 Yeah, we do a lot of experiments, for sure. We've been playing with better caching and stuff like that. That's definitely been paying off. But we're struggling a little bit. We have, …
So, one thing, specifically about caching, we've been using, for the collector control repo, about a… two weeks ago, we were using 561 gigabytes out of the 10 gigabytes allowed.
The reason for that is, I was explaining that to the team, is what's happening is, you have caches which are competing for existence, and if you have one in your default branch, then it will pick it, but if it's not there for any reason, then all the PRs will create one.
So you end up…
Yeah, because you evict, you evict every… every 24 hours, you evict everything that's older than 24 hours. The ones that are used by main actually may be evicted at any point in time. The moment they get evicted, all the PRs will recreate the exact same cache, and we don't have time to do that.
**Zack Koppert** 22:00 40 open PRs, yeah.
**Antoine Toulme** 22:02 So we want to make sure that the PRs only read the cache, don't write it. But I haven't found a way to do that, and I have opened a couple, …
couple issues and a PR against, Action Cash to say, hey, I think this should be a best practice, but I haven't heard back at all. I don't know, probably a completely different team, but FYI, that's, ….
**Zack Koppert** 22:22 It is, yeah, that's good to know, though. I can, raise awareness for that issue. Do you have a link to that at all?
**Antoine Toulme** 22:29 I'll find it, I'll find it.
And, we're going over your time, folks, I'm sorry.
**Zack Koppert** 22:36 Well, thanks for sharing about, kind of the pickle that you guys are in, and scaling, and trying to keep CI and actions going, while also servicing folks' PRs. That's a lot, so, yeah. Yeah. See the link there.
**Antoine Toulme** 22:49 We do a lot, for sure.
**Zack Koppert** 22:52 Yeah.
**Trask Stalnaker** 22:53 Yeah, thanks for the, the, triage, the AI triage, links. I, I'm… I'm very…
Excited about the possibilities there of, like, even just, like, it should be such an easy task for it to categorize and label stuff.
Just some basic things that could be really helpful for us.
**Ashley Wolf** 23:16 And those are continuous, but I suspect we could find dozens of actions you could run one time as a single workflow to be able to do that, rather than… or I guess you could run this one time as well, but if you don't need it to continuously monitor and label, and you want to experiment, there's other types of actions as well in this same family.
**Trask Stalnaker** 23:38 And so, are we able to do those, without having a co-pilot license? How does that… Work.
**Ashley Wolf** 23:49 Yes, so these are actions plus GitHub models, and they're using tokens, so there are thresholds there in capacity, but it's not relying on
GitHub Copilot to be able to process. So, for free, there's a pretty decent threshold available, so you can check that out and then figure out ways if you need to break it up so that it can run if there's
too much being processed, but it's not going through Copilot per se. It could be going through OpenAI or other systems.
**Trask Stalnaker** 24:24 I see. Okay.
**Ashley Wolf** 24:25 And run it through GitHub, different models, OpenAI, I think primarily those are the two paths right now, or Zach, I don't know if you know if others are supported, but I think….
**Zack Koppert** 24:35 Not that I know of, yeah.
**Trask Stalnaker** 24:36 Okay.
**Ashley Wolf** 24:39 Lots of sample code available in that repo I listed out as well.
**Trask Stalnaker** 24:57 Cool, anything else, Antoine? Should we let these lovely folks from GitHub go?
**Antoine Toulme** 25:04 Yeah, absolutely. Thank you.
**Ashley Wolf** 25:05 I mean, we're very glad to chat with you. We speak often with folks from LF and CNCF. We have a good shared channel and healthy cadence for communication there, so we're happy for you to ping us through those channels, or join these calls, or separate calls.
I'm sure this won't be the only instance of pain points around managing a project at scale and developing at scale, but we can try to, like, recap here, but I think the project board suggestion for triage sounds really useful. Definitely check out some of these.
workflow tools that might be able to help, or at least experiment with them. I'm eager to hear how they work for you. I've been trying to spin up a few on my own and finding teams that we might be able to see if it's valuable there and get feedback, so the ones that we are creating could be improved. So, let us know if there's feedback. The GitHub Next team has been creating a ton of them. They have a Discord channel, they're very open to
feedback and improvements, so if anything there is working or not working well, let us know.
And then, on Copilot Enterprise, let us know if there's any issues with onboarding or seats, but I know we're actively in the process there of helping you out.
**Trask Stalnaker** 26:24 I'm going to update our CNCF ticket and said… tell them that Ashley said to… that… such and such….
**Ashley Wolf** 26:34 Excellent.
**Trask Stalnaker** 26:35 Cool.
**Ashley Wolf** 26:35 I'm glad, Zach, that you were here. It's awesome. Zach's all about actions and workflows there. So, is there anything else that we can help with in the near term?
big or small, we're happy to, do what we can to provide some quick help or connect you with the right folks at GitHub.
**Trask Stalnaker** 26:58 I'm just gonna share… we don't need to talk about it, but I will share our… I did start…
a, GitHub feature wish list.
**Ashley Wolf** 27:08 Lovely.
**Trask Stalnaker** 27:09 We'll take it.
**Ashley Wolf** 27:13 Awesome. Very helpful. We'll definitely keep an eye out on this one. And if you are opening any support issues, feel free. I don't know if you go through the IT team or not, but you could send them our way to take a look at as well.
**Antoine Toulme** 27:28 Oh, perfect.
**Ashley Wolf** 27:29 Yep.
Awesome. Well, we'll let you all….
**Trask Stalnaker** 27:31 Thank you very much.
**Ashley Wolf** 27:32 continue on. Thanks for recommending that we join this call. Nice to meet all of you, and hope to speak with you soon. Feel free to come by anytime. Thank you.
**Zack Koppert** 27:42 Just hijacked the conversation, yeah.
**Ashley Wolf** 27:44 Awesome.
**Antoine Toulme** 27:45 No.
**Ashley Wolf** 27:46 So, thanks for all you're doing.
**Trask Stalnaker** 27:48 Bye.
**Antoine Toulme** 27:51 Yeah, sorry to hijack your cold risk.
That's awesome.
**Trask Stalnaker** 27:56 Yeah, yeah.
**Antoine Toulme** 27:57 It's just, they re… they rescheduled the call on top of this one. I'm like, well…
That sounds actually a very good idea. If I can get more people involved, that's… that's more… that's more valuable than just me talking to them.
**Trask Stalnaker** 28:10 Yeah, there's what you promised, man.
Do we have any normal business for today?
**Antoine Toulme** 28:21 …
Yeah, I wanted to mention this first-time contributor workflow. I thought it would be maybe useful for other projects, so I just wanted to bring that up, but I don't know that it needs to be applied to everybody across.
It finally worked. I had issues testing it, because you have to test it with a branch inside the project. If you test from a fork, your GitHub token does not have the right permissions. So, I want to try to find a good one.
I'm gonna… I'm gonna look for that label, first time… First time contributor…
So we had just one so far.
Yeah, I finally work here, so I'm just putting it here in the chat. So you can see it for yourself, what it does, that it adds a GitHub Actions command that says, welcome, contributor!
Thank you for your contribution to the pandemic collector contrib. Here are some reminders. Here's what to do. A maintainer will review a pull request soon. Thank you for helping, making…
Like, for helping make OpenTemperature better. So this was actually contributed by someone. I just opened the issue, and some guy from the internet decided to help.
…
The only thing that's cool about it is, the fact that we're able to detect that these are people who have non-status. So, if I go to GitHub workflows….
**Trask Stalnaker** 29:44 Are you sure?
**Antoine Toulme** 29:45 Yes, I can show my screen.
… Is this the right one?
Let me just write… let's share this. So, if you were to see here, this is the whole workflow. The only thing that is really tricky is to look for this.
So the offer association, if it's none, it's a specific
It's a specific state where they've never contributed before.
And that's how you know to show this.
Okay?
**Trask Stalnaker** 30:20 Okay.
**Antoine Toulme** 30:20 And that's good to know, I guess. And then, voila! It finally works, I'm happy about it. Really gave me a headache.
So feel free to… feel free to steal it, please.
**Trask Stalnaker** 30:34 Alright.
**Antoine Toulme** 30:37 That's it.
**Trask Stalnaker** 30:38 Yeah, we have many of, … a lot of the issues you were describing for the collector, contrib, repo.
We have, in semantic conventions, as well. … like, how… There's just…
there's not the same number of PRs, but it's, like, stuff that…
there's enough that GitHub notifications isn't very helpful, like, I don't want to click on every single one, I want to…
I need a pull model, not a push model.
….
**Antoine Toulme** 31:12 Oh yeah, right, exactly.
I like the idea of the project as a rendering of the different states of the workflow, so I'm gonna give it a shot, and I'll report back what I find.
But the other thing that I'm having trouble with is, we're in many different time zones. I haven't had a good chance to discuss with the other maintainers, so I think it's not going to happen before KubeCon that I can sit down with more people from the project, and we can talk a little bit about how we want to maintain this, what's our view of that.
I do a lot of promotion, too. I've been… you're the guy who signs off on the membership request. I, every single week, I make sure we have one more member. The Collector ContraPo is a big funnel to bring people into the platform. Yeah, yeah.
**Trask Stalnaker** 31:59 Right, right.
**Antoine Toulme** 32:00 So we try to have a very low bar, because we realize that if they don't become members, they don't get notified, they don't get notified, they don't… they lose interest, they don't get the ability to become cod owners as well. Like, we need to…
Really to make it easy for people to be on a journey where they can become quickly, important in a project, and they can feel the importance that they have.
So…
Yeah, I don't… I don't have a fix for this, it's just… it's actually human people, like, it's a people problem, it's not a technical problem.
**Trask Stalnaker** 32:35 We can make the technical, … can use technical things to make the human problem easier, though.
**Antoine Toulme** 32:43 That's right, but it's very subtle, right? So it's like…
Default recommendation, your issue template, go a long way.
people…
people, if they see that you need to provide tests, they will… they will think twice before they push the pull request, right? Stuff like that.
Yeah, we know the tricks, but it takes a village.
Anyway….
**Trask Stalnaker** 33:04 Cool.
**Antoine Toulme** 33:05 Okay, I gotta run.
**Trask Stalnaker** 33:07 Alright.
See ya!
**Antoine Toulme** 33:10 By Adria.
**Adriel Perkins** 33:14 Take care. Yep.
