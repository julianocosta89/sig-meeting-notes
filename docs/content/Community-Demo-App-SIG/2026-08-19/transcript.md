SIG: Community Demo App SIG
Date: 2026-08-19
Duration: 30 minutes
============================================================

## Zoom Recording Transcript

**Juliano Costa | Datadog** 00:08 Hello, hello?
**Donal O'Sullivan** 00:16 Hey. Hey, Julian.
Juliano, how are ya?
**Juliano Costa | Datadog** 00:21 Good, how are ya?
**Donal O'Sullivan** 00:22 Good, yeah, good now, good, yeah. Busy.
**Juliano Costa | Datadog** 00:28 I'm gonna put audio.
**Donal O'Sullivan** 00:30 Huh.
**Juliano Costa | Datadog** 00:32 I'm just, like, yeah.
Yup.
Okay, yeah, it's good.
**Donal O'Sullivan** 00:44 Yeah, no, it's… yeah, yeah, are you seeing, like, an increase in, like, people opening issues, and then opening PRs against them, and kind of, like… I don't know, are they… they're kind of… it's like trivial things. Not that there's nothing wrong with that, but I noticed that a lot of it can be, like, trivial stuff, and you're like… Hmm, do I need to spend 30 minutes at this?
**Juliano Costa | Datadog** 01:09 Yeah, that's the story of my life, man. I'm just… I… I honestly don't know how to… how to tackle that, because I did see an increase on that. Hey, Jonathan.
**Donal O'Sullivan** 01:25 Hey, Johnson.
**Juliano Costa | Datadog** 01:26 And you get a… you get a PR, you have… you get an issue.
Then you get a PR with a full 100 lines of.
**Donal O'Sullivan** 01:37 Yeah.
**Juliano Costa | Datadog** 01:38 That is doing. And then you have the fix that changes 2 lines, but that's 10 lines of comments.
**Donal O'Sullivan** 01:46 Hmm.
**Juliano Costa | Datadog** 01:47 And then, like, let's say front-end. I don't… I don't know anything about, front-end, so what I do, I ask Claude to review the PR. And then Claude reviews, so I publish to… I reply on the thread.
**Donal O'Sullivan** 02:03 Yeah, yeah, yeah.
**Juliano Costa | Datadog** 02:04 the person that opened the PR, he opened through an agent as well. So it's basically his agent and my agent talking, and I'm just…
**Donal O'Sullivan** 02:12 Through the middle name.
**Juliano Costa | Datadog** 02:13 in the middle, like, do I need to do that? Like…
**Donal O'Sullivan** 02:19 Yeah.
**Juliano Costa | Datadog** 02:19 hybrid.
**Donal O'Sullivan** 02:21 Yeah, yeah, yeah.
**Jonathan Munz** 02:22 Has there been any, I know this is a problem in other repos as well, has there been any, like… hotel, or, linux Foundation-wide discussions on how to deal with the kind of flood of AI-generated…
**Donal O'Sullivan** 02:38 I know they're… they've now limit… I think GitHub brought in, like, a PR limit, so you can only open, like.
is it 3 PRs, maybe, max, per repo? So, like, it… restricting there, because I know there was some people just opening, like, a lot of pull requests, and… Yeah, I guess it's fine if you're in a proprietary Thing where it's closed source, and you have a team looking at it, but if it's… open source, and you have a few maintainers, it can probably… doesn't scale that well if you're… someone's opening lots of PRs, you know? So I… Juliano, you might know more, but from my own experience I've seen in other hotel repos, like, there is a limit, I think. You can open as many draft PRs as you want, but, like, actual ready-to-review PRs is 3, I think.
**Juliano Costa | Datadog** 03:23 I honestly don't know if that's enabled to all records. I think I… I need to require… Or change the… Terraform script on the… on the project.
Level, whatever.
But yeah, it's just… And they also have the agents.md file. That helps a bit, but still…
**Donal O'Sullivan** 03:52 Hmm.
**Juliano Costa | Datadog** 03:52 Some agents simply ignore that.
**Donal O'Sullivan** 03:55 Yeah, yeah.
Yeah.
Have you seen this with a… the kind of emergence of generative AI, I guess, Juliano? It's kind of gotten a bit worse, like, as a…
**Juliano Costa | Datadog** 04:08 Yeah, yeah.
**Donal O'Sullivan** 04:09 Yeah.
**Jonathan Munz** 04:10 some things that can… I mean, for the example that you just mentioned, Juliano, I… there is a lot of cognitive load with… Not even just the code changes, the… verbosity of the PR descriptions.
**Donal O'Sullivan** 04:24 Yeah.
**Jonathan Munz** 04:25 comments. Not that… I don't know the exact solution here, but I do think some guidelines around that can help, because Even if the change is completely generated, requiring the contributor to write the PR description themselves can help, because it proves they've… understood the change enough to be able to describe it succinctly without, you know, a page of explanation. And then maybe even some linters on the comments, because honestly, like, it's rare that a comment that's more than two lines is helpful, and so… and that is, you know, Claude seems to love… 5 or 6 line comment descriptions. So I think there's maybe some… just cutting down on the pros, can… can help, can go a bit with reducing some of that cognitive load as well.
**Juliano Costa | Datadog** 05:22 Yeah, I actually added a note on the Agent SMD, so… Where is it?
Code comments. Avoid angry comments all over the code.
I comment only when it is extremely necessary, and no documentation page already explains the behavior.
It could be changes.
Constantly, and every comment is one more thing that can go stale, and it's to be kept up to date.
And then I add two examples of valid comments, like, regex, please add a comment on a regex, nobody knows how to read that.
And workaround behaviors. So, like, whenever you need to change something, and then whenever there is a workaround, if there is an issue upstream.
Link… add the link to the… to the issue, so we can also keep track of it.
But, yeah, looks like simply Claude ignores the agent's MD file.
even in my sessions, like, I, yeah, sometimes I just go and remove the… Maybe comments on my own.
**Jonathan Munz** 06:45 Yeah, that seems to… there seems to be… I've had that same problem, there seems to be a block there, but, But yeah, I think that's a good start, and then… Rejecting con- or, you know, requiring the person to put it up to do that work, if those comments are just… you know, adding noise and not following the guidelines, right? Like, that's a quick thing that can help, like, hey.
this PR doesn't follow this guideline, you know, please, please update.
**Juliano Costa | Datadog** 07:11 Yep, totally.
**Shenoy Pratik** 07:14 Regex comment, my… reviewer Claude pick it up. So, whatever I do, whatever I review, I have a first run with Claude.
And for the reduction tier, regex was caught by the reviewer, saying that it is expected to be there, because it's there in the agents.md file, but it was not picked up by… I don't know if they're using coding agent or not, by the PR author.
So, yes, it… Does forget it well sometimes.
But I agree, you can add a more holistic agents.md.
Or comments and PRs, both.
**Donal O'Sullivan** 07:58 And as an aside.
maybe, like, a delay between opening an issue and filing a PR. Wait for feedback before… anyway, that's a separate thing, doesn't really…
**Juliano Costa | Datadog** 08:09 But I think we… I think we do have that already there, but yeah, that's not the case.
**Donal O'Sullivan** 08:16 Yeah, yeah.
**Juliano Costa | Datadog** 08:17 They simply will not wait.
They raised the PR… they've raised the issue already with the PR ready to go.
**Donal O'Sullivan** 08:26 Yeah, yeah, yeah.
**Juliano Costa | Datadog** 08:30 They're solving the issues, which is great, but, like, I just… It… it seems a waste of my time Going through a thing that the person not even… Invested his time.
**Donal O'Sullivan** 08:48 So… Yeah.
**Juliano Costa | Datadog** 08:49 maybe we should have an automation data, or an agent. We have Copilot, we could… I don't know.
have an agent to review the PRs that are opened by agents, and done, done. Like… I'm… We can scale.
**Donal O'Sullivan** 09:07 Yeah.
**Shenoy Pratik** 09:08 Getting that first pass from the agent is really important right now.
**Donal O'Sullivan** 09:12 Hmm…
**Shenoy Pratik** 09:13 I've seen that cognitive load in the PRs now. The problem is, even after I give some comments, there are these subtle things that are missed.
And for me as well, it's pretty difficult to look at the follow-ups that they have done and find the diff, and see if they have actually implemented everything or not. Like, that's… That's some trouble.
**Donal O'Sullivan** 09:36 I… I… I don't know, I have an assumption, maybe, that there… it's almost like some of the stuff I've seen is, is maybe AI being used to, like, look for, kind of, quick wins in the project, and then, like, an issue is opened? Look, I suppose it's maybe it's a good thing as well, but it's me just being a bit nitpicky.
But, Maybe there's an element to that.
Cool.
**Jonathan Munz** 10:02 Yeah, and I agree, it's like, those fixes are good.
to your point, I struggled of how you enforce this, but I do think it does need It shows a bit of a lack of respect for the person who's gonna be reviewing it, because if you're not… if you're not taking the time to at least look at the PR and be like, what could I do that reduces the cognitive load on the person who's eventually going to review this?
you know, you… again, it's… it's sort of a… it's a bit of a fuzzy thing. It's not like there's a linter rule for that, or, you know, it's like… you know, a human is gonna have to look at this, like, what can you do to make sure that's a bit easier? And if you're skipping that step, then… Then, yeah, it's tough.
And that's what I was curious about, because, yeah, I don't think it's unique to this repo. I was curious, like, I think a lot of open source projects are struggling with it, and how you kinda… How you kind of deal with that.
**Juliano Costa | Datadog** 11:05 Yeah, but I think if you get the, for instance, the most active repo in, in Ottawa is, the collector.
And if you take a look at their list of approvers and maintainers, they… they're… There are… there are plenty. Here, we don't… we do not have many folks.
**Jonathan Munz** 11:25 Yeah.
**Juliano Costa | Datadog** 11:25 And, and the problem is that we need… So, here, here is the, the, The maintainers, what is it called?
dilemma, the maintainer's dilemma. We need new folks.
To keep the project alive.
**Donal O'Sullivan** 11:44 Hmm.
**Juliano Costa | Datadog** 11:44 And we need to kind of foster people to get to know the project so they can become approvers and maintainers. But… with AI, people are contributing without actually knowing the project. They have their agents to go and look through and do the things, and they're okay, they're fixing stuff, but do they actually understand the project and everything that it would require them to know to become an approver and help maintain the project. And if we never get someone interested in joining the calls, discussing, being interested in the project, we will never get more approvers and more maintainers, and the project will eventually die.
**Jonathan Munz** 12:30 Yeah, that's a good point.
**Juliano Costa | Datadog** 12:33 So, yeah.
**Donal O'Sullivan** 12:34 I wonder, like, is there a way of categorizing the work? So, like, you have, like, your… non-AI work in one category, and you have all your AI work done in the other category, and you can obviously, as you said, you know, let Copilot just do the reviews of the AI stuff, and then it… it can be like a human in the loop at the end to be like, do we actually want this or not? But then the more serious focus is on, like, the… The human contribution, or, you know, obviously the maintainers… main approvers, we might be talking about a bigger feature that we want to work on and add to the demo, something more important than just kind of drive-by PRs, you know what I mean? But obviously, categorizing that will be difficult here. How do you differentiate, you know,
**Juliano Costa | Datadog** 13:19 I think, I think we could have tags.
And based on the tags, have GitHub Actions that would trigger the… the… the review? One sec.
I think that would be doable. Like, even if you consider the PRs that are that have the Claude as a contributor.
So, if we detect that, then we automatically tag, or PRs like, we do on the… on the… on the docs that we need to check, like, hey, I used AI here.
If this checkbox is enabled, then tag like that, and then have a first review from.
So, that, that is easy.
But… still, I don't know how much that would help with the whole thing.
**Donal O'Sullivan** 14:23 Yeah.
Yeah.
**Juliano Costa | Datadog** 14:28 Which, actually brings me to the point, Jonathan, I think you were involved in the project for some time. Would you like to… would you have time, and would you like to become an approver?
**Jonathan Munz** 14:41 I think that would be great, things are slightly in flux, at Embrace over the next couple weeks, but, so I won't be able to give an answer on time commitment, but, but yeah, I think that would be, That would definitely be, something I'd be interested in.
Starting the process. I don't know… What the next steps would be, or if you do have a rough idea of what sort of the time commitment you'd be looking for.
initially.
**Juliano Costa | Datadog** 15:24 Honestly, if we can get help on reviewing docs and the PRs that are open, that would be great.
It… it actually depends, like… I think now we are having more PRs than we usually have.
**Jonathan Munz** 15:43 Yeah, yeah.
**Juliano Costa | Datadog** 15:46 thanks to the… the testing framework that we have in place now, the PandaBots PR are super easy nowadays, so they're just, like, wait a test to run, all green, a proven merge.
That's, EasyWee. But, would be more, like, the PRs that we have open now, the ones that will come in, and, docs.
Yeah, Docs, I would really appreciate the help there, because, you know, we have… I think that the things that were released on 3.0 are still… a bunch of open PRs there.
**Jonathan Munz** 16:26 I mean, that might be a good start, like, I could just, I don't know if you have specific GitHub filters that would be the most useful, but I could just bookmark, like, a… A filter of… what would be the most useful to get another pair of eyes on, and just make a habit of checking that periodically over the next few weeks, and then if that goes well, we can… cause I- I can… I can hit approve.
and do everything without being an approver, it's just whether that means anything or not is based on my status, right? Okay, so yeah, I could start with that. I could… I could have, something bookmarked and just get in the habit of, Checking it periodically, and then we can… we can talk about next steps after that.
**Juliano Costa | Datadog** 17:11 Cool. Okay, yup.
**Jonathan Munz** 17:14 Is there anything beyond just clicking the open PRs for the repo? Is that enough, or would there be certain filters that would be… more use.
**Juliano Costa | Datadog** 17:23 No, for the demo itself, we don't have much. We have 13 PRs now, and I think one is trapped. Yeah, so we have, like, 12.
They only own the OpenTelemnistry.io, which are…
**Jonathan Munz** 17:42 Oh, right, the dark.
**Juliano Costa | Datadog** 17:42 Where we have… where we have the docs, then you can filter by… if you… if you search by demo, you'll see, like, all the PRs related to the demo.
**Jonathan Munz** 17:52 Okay, cool.
**Juliano Costa | Datadog** 17:53 I think those are the two, yeah.
**Jonathan Munz** 17:56 Great.
**Juliano Costa | Datadog** 17:57 Helm charts, we… we also take care of the helm charts, but, helm charts are just… Updated when we have a release, so not much, to do there.
As of now.
**Jonathan Munz** 18:10 Is it a label? Sorry, I'm just getting the filter for the opentelemetry.io.
**Juliano Costa | Datadog** 18:17 I think there is a label, but you do not need to. I think if you just search for Demo, you should find.
Okay, cool, yeah, I'm.
**Jonathan Munz** 18:27 that now.
Yeah. Okay, great.
**Juliano Costa | Datadog** 18:32 Cool. Embracing… embraces joining another company, right?
Yeah. Or got acquired.
**Jonathan Munz** 18:42 Okay, perfect.
**Juliano Costa | Datadog** 18:50 Cool.
Anything else you guys would like to discuss?
**Shenoy Pratik** 18:59 I added in the issue for Percy's addition to the demo.
Dadog in that.
**Juliano Costa | Datadog** 19:06 I think we all want that, right?
**Shenoy Pratik** 19:10 Yes.
**Juliano Costa | Datadog** 19:12 Any objections? Let's just thumbs up and, and go for it.
**Shenoy Pratik** 19:18 Question, do you want to replace Grafana, or have it as a separate alternative visualization tooling?
**Juliano Costa | Datadog** 19:27 Sorry, come again?
**Shenoy Pratik** 19:29 Do we want to replace existing Grafana dashboards and stuff?
Oh, okay. That makes sense then, yeah. Good hand.
**Juliano Costa | Datadog** 19:37 Yes. Yeah, I wouldn't ship, two things. I would ship only purses.
As Percy is a CNCF project, I think it's just another project to showcase.
And CDL mentioned that he can help with the alerting thing, but to me, on the Prometheus alerts, but to me, I don't know if that's something that we actually want to take care and have on the demo.
**Donal O'Sullivan** 20:14 Could… we could just get the… get Percy's in first, and then do, like, if… if we wanted to do the alerting afterwards, I guess, to kind of.
**Juliano Costa | Datadog** 20:23 Yup.
**Donal O'Sullivan** 20:23 Minimize the… it might be a fairly large chunk of work, maybe?
Initially.
**Juliano Costa | Datadog** 20:28 Yeah, yeah, it will be a large refactor, but I think… well, not sure if it would be a huge deletion.
Because… when we count both, because purses will also have the JSONs for the… For the dashboards, so I think… Because if we just think about replacing, removing Grafana, that would be a big… chunk of JSON being dropped.
**Donal O'Sullivan** 21:00 Yeah.
**Juliano Costa | Datadog** 21:01 We are also adding persistent, Which brings me to another thing. I opened an issue when we… we released the… the demo.
We don't know where it is… Yeah. Issue 3720.
Do you guys have any updates on your forks?
Because,
**Shenoy Pratik** 21:33 I'm planning to do it next week. I have something going on, but it's… yeah, we're also changing the repo paths and stuff, so I'll share it.
**Juliano Costa | Datadog** 21:43 what…
**Donal O'Sullivan** 21:44 What's… what's the issue, Juliano?
**Juliano Costa | Datadog** 21:46 I'll share here on the… on the chat.
I shouldn't have.
**Donal O'Sullivan** 21:52 Oh, yeah.
**Juliano Costa | Datadog** 21:55 I should have the… Then we'll see docs open.
**Donal O'Sullivan** 21:59 Oh yeah, yeah, so we've actually… we've… we've synced with… with Upstream, so we're… I think… Yeah, we've synced it upstream, and it's working. Well, it's working for me anyway. But we, yeah, we just have to do some stuff internally, but I think we're also gonna cut a release, like, we tend to do a release… like, when we update, we're kind of a… we do, like, a release of… Then soon after, so… but yeah, we're…
**Juliano Costa | Datadog** 22:29 Okay.
**Donal O'Sullivan** 22:29 We've synced with 3.
**Juliano Costa | Datadog** 22:32 Okay, yep, just,
**Donal O'Sullivan** 22:36 I'll update.
**Juliano Costa | Datadog** 22:36 Well, you have… you have permissions here, so you should be able to, checkbox your earning, because, not your name, but, Elastic.
Because the idea is to clean up the… the Demo Street training, the surrounding shop after.
Yeah, how many days?
60 days, so… July?
That would be September or something.
Yeah, and we just got one… person… from Coupai, or AI, whatever, at least, yeah.
reaching out to now, so I don't know if people did not read the thing, but yeah.
Anyways… whenever we remove, I think the vendors will come back and say, hey, why did you remove?
I'm asking, but I know that the Datadog one is still not updated. I'm still working on it. It's, complicated.
**Donal O'Sullivan** 23:47 Okay.
**Juliano Costa | Datadog** 23:50 And the demo added a bunch of stuff, so, like, yeah, it's a nightmare.
**Donal O'Sullivan** 23:56 Nice.
**Shenoy Pratik** 23:57 When do we… start tagging people and then DMing them on Slack for the removal.
**Juliano Costa | Datadog** 24:04 of… your call. Should I… Did we start now? Yeah, I don't know.
**Shenoy Pratik** 24:14 Let me see if I can do some… plot magic there. I don't want to just go into DMs of every… contributable.
Okay.
**Juliano Costa | Datadog** 24:25 I know that there are companies that do not exist anymore, I think… And companies that… they were added because someone was working there, and then this someone left, so… Like, we have Instana there, and Stana, I don't think… It exists anymore?
Causeley was added by Severin, because he was there, but now he's at Bronto, and then Bronto was added.
So, yeah, anyways.
Trace test is gone.
Cool. And we've reached, 7,000 forks.
So… Yeah, that's…
**Donal O'Sullivan** 25:42 Oh.
That's a lot.
**Juliano Costa | Datadog** 25:46 Yeah.
That… that's cool, though.
**Donal O'Sullivan** 25:49 Yeah, yeah.
**Shenoy Pratik** 25:52 AI contributions are helping in that number, I guess.
**Donal O'Sullivan** 25:59 Yeah.
Definitely.
**Juliano Costa | Datadog** 26:08 Cool.
Okay, then, I think we can… called… cold a day.
Yeah.
Then, see you all next week.
**Donal O'Sullivan** 26:28 See you guys. Bye-bye.
**Juliano Costa | Datadog** 26:29 Bye.
