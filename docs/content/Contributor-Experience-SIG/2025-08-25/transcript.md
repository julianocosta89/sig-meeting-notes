SIG: Contributor Experience SIG
Date: 2025-08-25
Duration: 47 minutes
Zoom Recording URL: https://zoom.us/rec/share/VMLdxQqXBEO1h3yjtVVS02Ngc60R6XWF43L30h5mhqWO6vYGL1pZlroYS3rYuhIT.jJtILLkqTEuFffOn
============================================================

## Zoom Recording Transcript

**Amy Super** 01:42 Hey, hello.
**Antoine Toulme** 01:49 Hello.
**Amy Super** 01:51 I don't think we've met before. I'm Amy. Nice to meet you.
**Antoine Toulme** 01:54 Hey, nice to meet you. Antoine.
**Amy Super** 01:57 Nice.
… Are you, normally involved with this SIG, or are you just dipping your toe in the water and seeing what it's all about?
**Antoine Toulme** 02:09 Yeah, the latter. Okay. Know what I'm up to.
**Amy Super** 02:13 Nice.
I am also just getting started with this SIG, so, maybe we can find our way together.
**Antoine Toulme** 02:20 For sure.
**Amy Super** 02:22 Nice.
**Antoine Toulme** 02:23 What's….
**Amy Super** 02:25 Sorry, go ahead.
Oh, you know what, I just realized I'm on the wrong Wi-Fi network. Hang on, let me switch. I'll be right there.
**Antoine Toulme** 02:31 Okay.
**Amy Super** 02:39 Okay, I think it's switched. I have, … I don't know. One outside, one inside, it was a whole thing, and sometimes the computer picks up the wrong ones, you know, so….
**Antoine Toulme** 02:50 I had that for the longest time. It was a pain. And I think a big quality of life was I eventually upgraded to, … a mesh Wi-Fi that is the same across my whole house, and it does the handover for me, and it… it changed… measurably my quality of life, because I can take my laptop and go Yeah, it didn't come back.
**Amy Super** 03:10 I should do that. That's… that's on those… that's one of those, like, maybe one day I'll get to this kind of things, you know? So….
**Antoine Toulme** 03:18 Yeah, no, definitely, I get it. You know, we have… we have busy lives, only so much time.
**Amy Super** 03:23 Yeah, yeah.
**Antoine Toulme** 03:24 I found that, my level of frustration about things to… on a daily basis, there are things I can't do much about, right? Life is difficult, work is what it is. You get, you know, the world is what it is, but I can control this. I can make this much better.
**Amy Super** 03:41 That's awesome.
**Antoine Toulme** 03:42 Yeah, so, this has been….
**Amy Super** 03:44 Nice.
**Antoine Toulme** 03:45 been really helpful for me. ….
**Amy Super** 03:47 There you go.
**Antoine Toulme** 03:47 Okay, so, let me see, is there a doc?
Yeah, it's interesting.
**Amy Super** 03:51 There's a doc.
**Antoine Toulme** 03:52 And then there's hope.
**Amy Super** 03:54 Yeah, which actually I need to pop open here, too, so… ….
**Antoine Toulme** 04:00 Oh, interesting. So we don't have anything for today, right?
**Amy Super** 04:04 Hang on, I'm still catching up on getting the dock open, so, ….
**Antoine Toulme** 04:09 Hey, go ahead.
**Amy Super** 04:19 Great, there we go.
No, we don't have anything. So I am happy to, since I have not met you, and… Bogdan, I don't think we've talked before, so maybe we should just start with a round of introductions, and we can talk about, kind of, what's going on, and then go from there? Does that sound okay?
**Antoine Toulme** 04:42 Great.
**Amy Super** 04:44 … So, hello, I'm Amy. I'll just keep talking. I was already talking. So, my day job is that I'm a principal product designer at Grafana Labs, and, … I've gotten really interested in this SIG because, to me, a lot of it being kind of experience-based is in my sweet spot of what I like to do, which is figure out what pain points are and learn more about them in order to decide what to do about them.
So I first got involved with the OpenTelemetry community as a whole by mentoring through Linux Foundation CNCF mentorship program, which I'm still doing, but then I kind of also looked at this SIG, and I'm just starting to get involved in it, and so I think that generally what I have observed is that … there was, like, a big body of work where the SIG did this, survey to do some outreach and learn where there were pain points, and then that was, like, a natural dropping-off point, where some people were like, okay, we sort of, like, shipped something, so now we're done. And it's kind of up to, the rest of us to pick it up and decide what we do next. And so that's what I'm trying to work on doing.
That's me.
**Antoine Toulme** 06:07 Logan, go.
**Bogdan Nicolae Stancu** 06:09 Okay, okay. I'm not good at this, but I'll try. I'm Bogdan, based in Romania, working for Adobe, and a developer in the observability team.
And, well… I don't know, I'm just… getting into OpenTelemetry, I did some… random PRs, I guess? … Trying to learn how open source works.
I've been told that this… I mean, it all started kind of when… One of my colleagues left the team, that I really liked, and he told me, like, one of the best things that he told me that I… is that I should focus on ISS, because the community, is… Well… let's just say community-driven things are better than just internal tools. Let's say that. And, yeah, I'm here to… learn more, and yeah, well, I'll try to, … just, join as many as, as many as, as many meetings as I can, just to understand what's going on. And I, I mean, I do have something that I would like to talk about.
But after the introduction.
Yeah, well….
**Amy Super** 07:34 Sounds good. Thank you.
**Antoine Toulme** 07:39 I can go next, I guess. So my name is Antoine, I'm a… I'm a contributor to OpenTeometry since 2020. I… I'm now a maintainer on contribib, collector contribib, I'm an approver on core. I say to dip my toes into Java, I got a contribution, I'm a code owner of some of the code there.
So, I… I do a lot of PR triage, a lot of issue triage, a lot of work with first-time contributors, and I'm very sensible to make sure that we have the best experience for this type of first-time contributors in particular, because we want them to kind of take them on a funnel, right? So it's a… if I was to think about… my mental model for this is that I find it's like a sales funnel. You start with a population of leads who are interested in your project. I think Ogden kind of illustrated that very well. It's like, there's interest for personal reasons, company reasons, all sorts of different reasons why you might be interested.
Very personal. They come in.
They're looking at the project, they want to consume it, they start to want to make contributions, and we need to find a way to kind of give them an approach of how they're going to be able to get more and more out of the project by being also more and more recognized and rewarded for their behaviors.
So, in my collector contribository, for example, we have a fair amount of people who are first-time contributors.
And we're trying to kind of get them a bit more help, or a bit more advice, because they're their first time that they're coming here.
And we… we need to kind of get them more into the… the rhythm of the project. So… a lot of, a lot of things happening, on that. It's just a constant, like, there's just a lot going on. And, … I think I've been sponsoring people non-stop since I joined the project, and that's one of the best ways to get them, is to really proactively, early on, try to sponsor them, try to get them to show up for triage roles, and then start to get them on the ladder where they can get more and more of that type of recognition.
… So, I want to share some tips and tricks that I've learned from the project.
And, lastly, I think we don't have a uniform approach to how we handle contributions between different SIGs.
And that creates a bit of a disparity of approach, which may actually create some aversion for people to help across different SIGs, which… Sometimes you think it's Go or Java that is becoming the problem, but actually, that's not true. Most of the time, it's, I don't know the people there, I might make a fool of myself, how do I get past this insecurity factor? And even though I might be a Java expert, and I've been in JavaSig, actually, I don't feel like I can go help with the collector.
And I'd like to have more people cross-breed between different projects.
**Amy Super** 10:44 Thank you for that. Relia, we're just doing, quick introductions, since some of us have not met before, so would you like to as well?
**MG Marylia Gutierrez** 10:54 Yeah, sure So yeah, I'm really… I am one of the maintainers for this group. So… yeah, this group, we kind of gave, like, even a feedback on how we started. It was because we were discussing on some other six that we were, like, getting the feedback of people having, like, those challenges of just starting. We're like, okay, so we were, like, even discussing this should be, like, an end user group, a developer group, because we already had those two six, but, like, it's not quite those things, we need some, like, focus on helping.
people that don't know even, like, how to start and want to be, like, actual contributors. So this is why we started this group, and we… I don't know if you ever… if you saw, we have a project board that I can also share here.
So we do have, like, a pro report, a few things that we already did. So for example, one thing that we would notice that was happening a lot, but people having a hard time just to, like, set up their own local environment to start. Because a lot of times, like, how do I even, like, start? And… when I checked all the repos, a lot of them didn't have anything about how to contribute. Some of them were, like, very basic. So, at the beginning of the year, we worked with the was the outreachy, don't know if you, know this, but it's like a program to help and have an intern.
And then, so I was the mentor for that program, and with that one, we were able to create a contributing doc for every single repo. So we created the template, and we put it like the basics, so… but at the same time, we depended on the maintainers to look at all of them.
Because we don't know a lot of them, how it works. So at least all of them should have a basic on why you need to, like, what are dependencies and stuff like that on how to contribute.
We also then did a survey of… how people are doing. So we have, like, two types of surveys, so one we actually ran with a lot of people, and the other is whenever a new contributor opens us and merger PR for the first time, they get a message saying, like, hey, tell us how was your experience?
So, currently, we only have that one on the Opentelemetry.io and the JavaScript one, just as a test, and they work quite well, so we're gonna add two more repos. It's a way to always keep getting feedback from people.
And from those results, is that we were currently, like, analyzing, seeing, like, what are the challenges for people, and the things that we should be focusing on next.
**Antoine Toulme** 13:38 That's cool. Feel free to, let us know for corrective concept, but I think it would be useful.
**MG Marylia Gutierrez** 13:45 So, probably all of them should have, like, ….
**Antoine Toulme** 13:54 Yeah.
We started to do a thing for first-time contributors, it's not working quite yet for the collector contributor repository.
So, it's more a wrinkle for me as a maintainer.
But I'm having a hard time… with, first-time PRs, because you need to run the CI for them.
You need to go into the PR and click a button that says to run the bill, which is… Ridiculous, but… Of course, you're doing that 20 times now, because, you know, first time around, they come back, the same shoes, and they push to main, then they….
Emerge, they rebase, they do this, and then sometimes they even just repeatedly, over a period of a day, keep pushing the button to update the latest main in hope that being on top of the latest change is going to help them get faster to the queue.
But really, what happens is that they actually get less and less of the ability to be selected for merge, because you have to rerun the test.
And then they cut off the… even the CI by merging again. So what we have now is we have a little bit of a text that shows up, a comment that says, welcome, here's a contributing guide, go learn more about us.
And, we put a label that says first-time contributor, so I'm gonna have a way for all the maintainers and approvers to be able to look for a list of these PRs and proactively go and review them much earlier in the process.
**MG Marylia Gutierrez** 15:16 ….
**Antoine Toulme** 15:17 But it's, it's a tough one. We… We had a meeting last week where the GitHub experience team joined the Project Infra SIG on Thursday.
**MG Marylia Gutierrez** 15:29 Huh.
**Antoine Toulme** 15:29 And we discussed with them some of the issues we're having with triaging in that repository. We have 140 PRs open at any time at this point, and we're trying to make it so that we can get the pressure down a bit.
But it's difficult to get people to kind of understand where they are in the process of being merged, and they offered that we should use a project in GitHub to take care of showing this, this, sliding between states, but… We need to kind of use workflows with actions to use some, you know, association of action to move to a different stage in the project, something like that.
**MG Marylia Gutierrez** 16:06 Yeah, because doing this manually, yeah, would be hell.
**Antoine Toulme** 16:10 But the problem we're having is we've done our own process.
Because we have the need to have You need to be in draft if you don't want us to look at it. If you want us to look at it, we're going to take a look. If it doesn't pass CI, or if there's obviously a conflict or something like that, we put it back in draft. If it's good to go, then we're going to mark it as waiting for code owners, meaning that someone who's an expert in that part of the codebase needs to take a look.
**MG Marylia Gutierrez** 16:35 Which becomes more of a….
**Antoine Toulme** 16:37 like, a difficult exercise to kind of get the people, the right people, to pay attention to that and all that. Once that is done, then we can mark it ready to merge, and it gets ready to merge.
… yeah, this is an informal process that I built for myself, just to survive the onslaught of PRs we have.
**MG Marylia Gutierrez** 16:57 Bye.
**Antoine Toulme** 16:58 I think the contributors are not clear on this, but also, it's very different if you use, let's say, Java contrib. There's no process. It's just a bunch of guys, and they complain to me that they're not getting enough people to pay attention to their repositories, but I think I know why. It's because their process is even less clear to me.
And much more based on attending the SIG meetings, for example, to get your attention on your PRs.
So… I think….
**MG Marylia Gutierrez** 17:23 I think it can vary a lot, like, for example, for the JavaScript that I… I basically joined the JavaScript one, and so we had, like, people always looking like the up one, and then I noticed, like, we have a lot of PRs that are, like, very old.
That nobody's looking like at all. So we made part of our sick, the end. We ordered by, like, the oldest, and we kept looking. So when we started… we started about, like, 3 months ago doing this.
And we had things from, like, 2020. Now, the oldest that we have is from, like, 2024.
And we, so we kept this practice of always adding, reviewing, making, seeing if they're still valid, like, closing, or like, oh, they should actually get merged, and merge is a way to force the maintainers to look again at those things, but yeah, don't take as a common process.
**Antoine Toulme** 18:18 No, yeah, we don't have… We tried two SPRs in meetings, and it was a disaster. We were able to do three.
And it's just a lot of opinions, too.
**MG Marylia Gutierrez** 18:28 So….
**Antoine Toulme** 18:31 Here. Anyway.
That's… that was my… what I'm here for is to understand better how we can make this more of an effort across OpenTemmetry, because if we diverge too much, we're gonna have a hard time making this work.
Matt, what did you… Bogdan said he had something, so….
**Bogdan Nicolae Stancu** 18:52 Yeah.
What I… what I wanted to, well, point out, I guess, is that, well, the first thing that I did when I was interested in, contributing is looking at the issues.
finding something to do, because I… I didn't come here with, some own problem, like.
We didn't have something that I wanted to fix. I was just looking around.
And the first thing that I did was, look for the… Good first tissue label.
**Antoine Toulme** 19:23 Hmm. Which….
**Bogdan Nicolae Stancu** 19:25 I think… I don't know if there's a, like, an actual guideline for when that should be applied.
But, in my experience, it's either very old… I mean, I think in the main collector one, the issues are really old.
And in the contribib, what I did find, and what I did do initially, was just… Random, very easy tasks that weren't per se, good first issues. Like, they weren't teaching me anything. I shouldn't… if I want to start learning OpenTelemetry, I shouldn't start with those.
Because, like, it was just, like, change one line. This error is not clear enough. I don't know, something like that.
And, yeah, I would have loved… I do have, … well, I did find stuff to do, which have been kind of way better first issues, even though they weren't as easy. They… I think they should be… They shouldn't require an in-depth Knowledge of the subject, but it doesn't matter how hard it is, as long as you can just come and do it.
And yeah, I mean… to what I'm studying.
**MG Marylia Gutierrez** 20:37 Yeah, I was gonna say that I think by default, people don't try to pick hard things for the good first issue, because they're usually tied to things about… Are you able to, like, have this running locally and test it out? So if it is, like, an error message that was not clear.
If you have, like, already trouble, like, just in setting up your environment, that is a good first issue for you to try and make sure that everything is running. So a lot of times, could be very simple things like that.
… but then you can grab… I see some people sometimes doing, like, an up for grabs. That is something that is not… easy for, like, if you don't know, like… like, yeah, it's my first time, but if you want to learn, you can pick it up. So I have seen some up-for-grabs labels as well, that is kind of, like, a little more advanced from the good first issue.
**Bogdan Nicolae Stancu** 21:32 Yeah, that sounds good. I think that there should be a differentiation between the beginner in the project and the beginner in general.
That's what I think I didn't… didn't find.
**Antoine Toulme** 21:45 Yeah.
**MG Marylia Gutierrez** 21:47 Yeah, there is also, like, the challenge of… okay, you were coming, just you want to learn hotel, but there is also what are, like, the priorities for that SIG? Usually, the SIG have, like… right now, we are focusing on this particular issue, like, might have two or three, and usually… or they're gonna put this somewhere, or they have, like, an issue, they're making that clear, or somewhere, so… If you want to learn, you would look at those focus areas for the tick, and you might get, like, more help from people, like, hey, I want to help out, because I see this is an area that more people are already looking, so you're probably going to have more people to review your things, so usually those are the good ones to start as well.
We did have an idea of also creating, like, a Slack channel specific for, like, it would be, like, open telemetry, like, start here.
type of thing, and then it would be, like… because we… we noticed a lot, a lot, like, the maintainers get the message, like, I want to help, what should I do? Like, and they don't even know, like, which language they want to use, or which project they want to use, and it's very, like, I just… want to help type of thing, so we wanted to have one Slack that would be, like, generic for everybody, and it would list, like, good force issues for this repo, click here, click there. But the concern was that we didn't have enough volunteers to look at the channel.
Yeah. So… and to have a channel like this that nobody's looking doesn't make a lot of sense, so….
**Antoine Toulme** 23:22 It could be a very expensive proposition, because sometimes we… we find that, you know, you're in a minority bug, and most of the people.
**Bogdan Nicolae Stancu** 23:31 Probably.
**Antoine Toulme** 23:32 know how to set up Go, and they ask us questions about things which are… Sometimes a bit scary.
We also have, like, we have people who will commit to making some small changes so they can get in and get their first commit in, because, again, that's actually the biggest barrier, is to get their first commit in. But I've seen people who are just like, you're like, yeah, I've seen good first issues, I'm like, I just need that one-line change, just like you mentioned, and they changed the whole file.
And I started to think, this is some ChatGPT thing going on here, like… So….
**MG Marylia Gutierrez** 24:07 Yeah, there's a lot of ChatGPT things you have to keep looking.
**Antoine Toulme** 24:12 Yeah, yeah.
So… We have a country fest that we've done in the past, I don't think we have one for KubeConne, right?
**MG Marylia Gutierrez** 24:23 Perfect.
Not sure if they set that up. They usually try to set that up.
Even, like, the last one, it was, like, last minute that we did.
**Antoine Toulme** 24:33 Oh, wow. Okay.
**MG Marylia Gutierrez** 24:34 Though, like, the year of one, it happened, but I don't think it was, like, it was a last minute, like, yeah, we got a room, here, go!
**Antoine Toulme** 24:43 I think the one that was in Salt Lake, which was a year ago, it made it at 5pm on the last day.
Which is really not fun. And something like 30 people showed up still, which was a testament of how this is important to people.
So, but… I… I would love to do sessions where I can show people, like.
We could even have a… I'd be happy to go through the code and just randomly point out problems, right, if that helps anyone. And then you could go on your own and be like, well, Antoine didn't like that to-do, so I'm sure we can go solve that, and, you know… fix that.
That could be a fun exercise, because I find those issues sometimes a little stale, and it's difficult to keep up with them.
So, maybe that's another way to look at those.
**Bogdan Nicolae Stancu** 25:42 Yeah.
**Antoine Toulme** 25:43 I would say on the country, also a really good source of recognition and easy path to kind of get into the project, is to look at the flaky tests. We have a lot of those.
And they're usually turned into a computer science puzzle, because most of the time, they're, like, some asynchronous behavior from some… something that's taking longer than it should on that run, but not others. How does that come up? Where… is there lock that is required? Are we missing something in the test setup, or is it actually an issue in the component itself? Like, there's a lot of fun things that can be done there. I find, … I find those to be more interesting. I… I take him up sometimes, because I'm usually bored, I'm looking to, kind of.
I need a brain teaser for some reason, and they never disappoint. There's always something to learn from those.
… And then make your life better, right? A CIA for contribute, is massive.
So….
**Bogdan Nicolae Stancu** 26:44 Noted.
**Amy Super** 26:47 So I do actually… sorry. I just have to drop in 5 minutes, so I just wanted to give a little update on what I've been up to, if that's okay? Sorry, I didn't know if we had paused because we were done with this topic or not. So, … if you look at the, notes from last session, I've been working on, as I mentioned, a plan for running some interviews with newer contributors to hear from them.
So we did, the SIG did a survey that had some really good general findings, but some of the findings were a little bit, you know.
hard to parse in terms of, like, what action items would actually make a difference. So it was like, newer contributors don't confidently know how to get started. Well, like, well, like, what do we mean by getting started, right? And what do they mean… what did they try to do? … And so, there is a research plan linked in, as I mentioned, the notes from August 11th, so please feel free to have a look. I feel pretty ready. I've also put together a Google Form to get people to, confirm that, like, they're okay with me recording the interview for note-taking purposes, and whether or not they're comfortable with, sharing, you know, quotes from them, or video from them.
So, just kind of looking for a second set of eyes on that, if anyone has the chance, and if it looks good, then I'll probably start doing some outreach to start scheduling interviews.
… So yeah, that's what I've been up to. But you can feel free to follow the links, and I won't spend the time sharing it here, because you can all read, so….
**MG Marylia Gutierrez** 28:37 Yeah, the thing that I was gonna say is that if you have, like, any ideas that you think, like, hey, this should be something that we should, like, organize, like, across six, open, like, the issue that project that I share. If you don't have permission to edit the project, feel free to tag me, and I can do it. It's just because that is the way that we can, like, discuss ideas, and then assign people to actually work on them.
**Amy Super** 29:02 So, I… I do have an issue that I'm assigned to that's on the project board.
So it's listed as in progress, so I think that's good. … But let me know if there's something I need to do, or some tag I need to put on it that doesn't… isn't working appropriately. Okay.
**MG Marylia Gutierrez** 29:20 No, no, it's all good then.
**Amy Super** 29:21 Okay, cool.
Just making sure.
**MG Marylia Gutierrez** 29:24 It's funny that one of the in-progress is the explain why we need to manually approve CI on PRs.
That you were just selling. That is the one that… I think… Tevin or Pablo, they're looking to that one.
**Amy Super** 29:51 Okay, well, I'm gonna drop for my next thing, but, it was nice to meet those of you I haven't met before, and, thanks for your time today. See you later.
**Antoine Toulme** 30:05 Bogdan, you had a feedback on good first issues, just looking at the project board, there's an issue here?
Related to good first issue, if you want to contribute your viewpoint, I think.
I think that would be very valuable. Oh, it's in the Zoom chat, it's, issue 24.
**Bogdan Nicolae Stancu** 30:28 Oh, yeah, the greatest, yeah, okay.
Yeah, I mean, and this is what I was about to propose, like, something… There should be some… I think should be some guide for all, labels, not just the good first one.
**Antoine Toulme** 30:41 Yep.
Good point.
No.
**Bogdan Nicolae Stancu** 30:46 Maybe it was just me, going instantly to the issues and searching by that label, maybe it's not something normal, I don't know.
**Antoine Toulme** 30:56 No, I think you're right. You know… … Why do I have a fix for this?
I'm too deep inside the… I find… I find that it's actually very fun to do this type of code reviews with people, because they… This is when things start to kind of pop up.
… So maybe it's just something that we need to do as a group, and then just file issues for everything that feels out of whack. But it's also… why are we doing this is more important. So, I'll tell you, from the concrete perspective, right, what we're trying to do is to mature everything.
if you look at my research activity on the project, I opened, like, 15 issues recently to ask components that have been in alpha stage to move to Beta. After being in alpha for over a year, what is going on? What are you guys doing? What is… what is in your way? How can we help you? And… I think the community, and anyone using those components, should feel free to comment on those issues, say, I think it's more than warranted that you move to Beta, because I'm using you in prod, and I need this stuff to work, and I really depend on it, and I would want to kind of get this community engagement of people who are also voting On this type of issue, saying.
you know, I don't… you're not alone, people care, and it's happening, and, you know, we really need you to move around to a later stage so we can trust you a bit more.
And if you look at that issue, it actually has a checklist, which has been kind of a discussion that was mandated from discussions with the collector core, the maintainers, and all that.
And it goes over a number of things which are pivotal to make it move to better, right? So, having a stable API, make sure there's no open issues, which are glaringly showing that there is instability, or problems that have not been addressed yet. Making sure we have enough people to review issues, that there's a commitment, that they're going to be around for help.
I find this to be probably the most useful ones from a product perspective around this type of projects, and if you find this type of issues, interesting, to help, again, to help mature things, that's… that's a good way to do it.
Another thing I do… so, on one hand, I mature things as much as possible so that we can get better adoption.
On the other, I look for things to cut, because we have way too much scope. What can we do? What can we stop doing, right? So, we had these open census receiver and exporters.
I started to jot around, like, do we need those? Are they helpful? This deck has been deprecated for 3 years. Why are we still maintaining that?
Right? So upon initially, I said, I'm gonna give you 6 months of discussion. Whoever wants to take that up and become more of a… engaged in that component, I need you to pay attention to it and kind of take over.
No one showed up, so we're removing those now. As we remove those, people are coming out of the wilderness, saying, hey, I depend on this, like, my life depends on it. I'm like, okay, great. Did you want to step up as a co-owner?
Silence.
no, I guess we're still removing it, right? So, there's… this type of community engagements are, like, worthwhile, and probably better of my time to kind of engage with people this way.
… Yeah, what else? We have a number of components who have no code owners.
Per the collector, agreement. If there's no codoners for a period of time, then we can actually remove it.
And unfortunately, we have, like, something like 20 or so, and they're all very important and needed by people.
But we're all lazy in trying to get away with stuff, right? So, … What happens is that the… People will wait until the last moment.
And I opened the PR to remove massively all that code to tell me that, actually, no, we cannot possibly do that.
But….
**MG Marylia Gutierrez** 34:52 And what we did on the JavaScript is the things that we did not have owner, we kept it there, but we don't accept any new PRs on it.
If somebody wants to add some change, then we say, okay, you need to, or find a co-owner, or find, like, a sponsor. If it's something like, oh, it's actual bug, and one of the maintainers is… can sponsor this PR, then you can merge. Otherwise, we don't merge anything unless you have a co-owner.
**Antoine Toulme** 35:19 That's a great idea. I will… I will use that.
I've also had people send us a PR that's over 500 lines, and my first response is.
You… we get that in, you're a code owner now.
Like, we're tying… we're tying you up to that matter.
You're not getting away from this.
And that's a condition to approve and merge a PR, right? And sometimes people take me up on it, which has been a great way to also get more engagement.
**MG Marylia Gutierrez** 35:47 Logo.
**Antoine Toulme** 35:48 It's been meaningfully running with it.
….
**MG Marylia Gutierrez** 35:52 But they keep the engagement, because I see sometimes people, like, as soon as they create it, a few months after, they might disappear.
**Antoine Toulme** 35:58 But donors are the worst. They are just… so that's a bigger issue. It's like, if you're an approver or a maintainer on a project, you put it on LinkedIn. You're proud of this. It's a big deal. This is going to help you land your next job. It's important. It also helps you from a point of view of running the project or participating in things. Great.
But code owners, like… you don't really get that much value from this. Like, here, you're now responsible, you know, you can't get all the chores, you have to do all the sort of work, you know, things are… people are angry at you, do you get yelled at? It's not fun at all. Like, why would you want to be a co-owner, right?
So, usually I use the code owner thing, and then I see the stick around, then, okay, we need to get them as 3 Azures, right? Or we start to kind of… need to start to get them creep up a bit more into the project, because that's a stepping stone, mostly.
**MG Marylia Gutierrez** 36:52 Hmm.
**Antoine Toulme** 36:53 But yeah, code owners are bad. They are my… in collector contrib, the weakest link is the… I think we have a problem where we don't ping them enough.
Or we ping them too much, or we don't do a good job of keeping them interested and around.
I don't know what to… how to do about that.
**MG Marylia Gutierrez** 37:12 Now, the way we did on… that JavaScript is. On the main repo, we have a set of, like, maintenance and approvers, but we do have a separate set of approvers on contrib, which include code owners.
So this way, they're able to, like, approve.
their actual PRs with, like, the green check, and we count there as, like, an actual approval, because otherwise it doesn't really count in the gray one. So at least it's a way for them to also have some ownership, and I feel like….
**Antoine Toulme** 37:45 That'd be… that'd be great. I don't think we have been able to do that.
And… because their approval doesn't count, then if you look at the list of PRs, they all look like they still need a review.
So I have to go and open each PR one by one to see if actually someone did the work of reviewing it.
Ehh.
**MG Marylia Gutierrez** 38:07 What we are currently doing is also creating a flow that, if a code owner approves, we want to add a label automatically, so this way we can see the label that is, like, already approved, and then we can just go in and merge the things.
**Antoine Toulme** 38:20 So we're all… we're all going about this in different ways.
**MG Marylia Gutierrez** 38:24 Yeah.
**Antoine Toulme** 38:24 Exact same challenge, looks like, so… We really need to just merge our approaches so we have less esoterical problems like this.
Because for a contributor, like, if they were to do something in JavaScript versus the collectors, then they get vastly different experiences.
**MG Marylia Gutierrez** 38:39 Yeah.
**Antoine Toulme** 38:43 So I was hoping that because we're starting to have decentralization of all the GitHub repositories' definitions and teams and all the branch protections rules and all that in the admin repository, where Terraform is running everything.
I was trying to ask Trask if we would be able to do these type of things also, like, having a common set of labels, having a common set of workflows. He's not saying no, but it's almost a photo to what you can do with Starform. You don't… have those things in Daphone.
So, I don't know.
**MG Marylia Gutierrez** 39:17 I think part of the issues that sometimes we were discussing, like, for example, if we now decided, like, okay, let's create, like, a workflow that every time that is approved by a code owner, it gets… get this label. So that is going to apply to every single repo. Who owns that script?
So if something goes wrong with that script, we, like, need to have somebody to own this and keep checking on repos. So that was also a….
**Antoine Toulme** 39:42 Yeah.
**MG Marylia Gutierrez** 39:42 a discussion.
**Antoine Toulme** 39:45 No, that's fine.
-Oh.
**MG Marylia Gutierrez** 39:52 Yeah, those are all great, like, feedbacks, and it's funny to see, like, same thing happening over and over, just in different segs.
**Antoine Toulme** 40:02 Yeah, we're a bit more terminal on our face, because what I… you know what's really happening with the collector control repository is that I'm the latest new maintainer.
So I still got some life in me?
But the others are just crusty, and they're like, yeah, I'll get to it when I get to it, and they don't, and it's… We're starting to see an exhaustion of the maintainers themselves.
And the moment they go and are no longer able to kind of keep up with stuff, it impacts the project quite a bit, because the… So, in a sense, all those open PRs are, like, un… it's like wasting money, right? It's like a bunch of value that's just sitting in some transit, right?
And… 140 PR, to me, is a staggering amount of, like, lost value.
… why are we not able to lend them at all? What's going on? What are we… what are we doing? You know, so… Yeah, we… we were talking about PRs this morning with some of the stability folks from the collector, right? We're trying to go stable on a bunch of modules, and one thing that's coming up over and over is that every time a PR is over a certain size, we cannot review it, because we lose our ability to review things after, like.
the brain just switches off. It's over 500 lines.
It's over.
So, I don't know how we fix that, but it might make sense also to start people to just break it down a lot more.
… But sometimes you get the reverse action there, because, like, okay, you're adding this thing, but why? I'm like, well, if you wait 5 PRs.
I'll show you why.
**MG Marylia Gutierrez** 41:46 Yeah, so it really, like, depends. So I'm trying to, like, for example, this one, set by example on… because I'm doing the declarative configuration on JavaScript, and currently I'm the only one working on it, so it's like, I could… I was like, I could create a PR that is going to be Huge. So, what I'm doing is actually, I created an issue for every step that I need to make.
And then I put it in a place to say, like, see, these are all the ones that I need to do in this order, this is the first one. And sometimes it is a PR, like, very, like.
it looks, like, so idiotic, like, you're only checking the file as a YAML, that's all. Like, yes, that's all this PR is doing. The next one is, like, parsing, the next one is whatever. So, at least they have… they can see, like, this is my end goal, and this is how I'm getting there, so at least this is what I'm doing.
But, yeah.
**Antoine Toulme** 42:38 That's a valid approach.
Yeah, so… well, communication, for sure.
Yeah, I've… I've had this issue with the operator where I was trinking together PRs, and I was like, I know the end result might not be the I can't bring them to this yet, because they won't agree to that.
But if I manage to bring up a bunch of incremental changes, then the change, the final reversal of that change, I think it will land just fine. People will be happy with it.
And… it was… it was a bit disconcerting for them. Like, what are you doing? Like, you… okay, this is… okay, fine. And they keep going with me, and they keep going with me, and at some point, BAM!
Here is a big change, and you go, Oh, no.
Oh.
Well… huh.
So, anyway.
**MG Marylia Gutierrez** 43:34 Yeah, so I think, like, for, like, this group is, like, how we can provide, like, guidance for the Sikhs in general, like, how we should all… we were able to discuss, should we have, like.
proper, like, message to say, like, oh, this is how you should reply if people send, like, a really big PR. How… so we have at least a common thing that we can always tell the, like, contributors, doesn't matter what, so we can have, like, the list of… This is why, like, why our issue is getting closed, or why this PR is not getting approved, list of reasons, and we can have, like, this template that can be used anywhere.
**Antoine Toulme** 44:12 prefer.
Okay, yeah, so I see you have an issue in to-do state for, maintainer handbook.
But it would be best read by both populations, maintainers and contributors, is what I think, what you're saying, right? In a sense.
**MG Marylia Gutierrez** 44:29 Yeah, it's always kind of, like, agree with the maintainer, like, this is what you should be doing, and then the maintainers can, like.
Pass this information on whenever a decision is made.
**Antoine Toulme** 44:41 Understood.
**MG Marylia Gutierrez** 44:45 But yeah, for that, we need, at the moment, like, on the issue, like, feedback. What are the type of issues that you are facing? You can put it there, so we know that when we create the handbook, we, like, we talk about all those scenarios. So the more information you can add there, like.
Things that happen, that would be helpful.
**Antoine Toulme** 45:09 Okay.
Can't take that too hard. I'll put that into the issue.
**MG Marylia Gutierrez** 45:14 ….
**Antoine Toulme** 45:15 By the way, I dislike the approach that GitHub is taking, which is, oh, you can do everything as a project. It felt like, actually, a huge amount of work when I looked at how much you need to do in actions to transition between states.
**MG Marylia Gutierrez** 45:28 So….
**Antoine Toulme** 45:29 I don't want to do that just for collector control, for that reason, because if I was to just do that.
See, you would… if we had this, standardization of labels, and you get that project for free.
like, kind of created for your six as part of the setup, or something like that, and all of a sudden, you have the same trash process for everybody, because we agreed on that. Okay, now I can actually sleep at night thinking, okay, this is actually worth it. But if I have to do it, and I'm the only person benefiting from doing this work.
Because the only… yeah, the other maintainers also don't really pay attention to what I'm doing. I'm telling them, like, hey, I'm moving people back into draft mode.
And I get no response from the maintainers.
No.
But I'm like, this is a big change. You need to understand, I'm gonna piece off people because of moving their stuff, which doesn't work, back into bad ref mode. Are you okay with that?
They don't care.
**MG Marylia Gutierrez** 46:23 I see.
**Antoine Toulme** 46:27 But otherwise, I don't know what to focus on, and I realized I had to kind of find a shortlist approach of things, and so….
**MG Marylia Gutierrez** 46:36 Yeah, it's a lot of things that, like, if you start, like, creating the list of things that you want to look at it, it becomes quite big.
**Antoine Toulme** 46:44 That is true.
Yeah.
**MG Marylia Gutierrez** 46:54 So I guess, yeah, whatever… Any… like, if you see any of the issues open, then you want to add some input, because then we… we know how to prioritize and look at those ones first, as well. Or if any of the things that we mentioned, we don't have an issue for it, feel free to open and ping me on any of them, and then we can, like, start assigning people to… Just talk with the maintainers and so on, to get those things done.
Any other topics?
**Bogdan Nicolae Stancu** 47:29 Sit.
**Antoine Toulme** 47:34 Nice to meet all of you.
**MG Marylia Gutierrez** 47:36 Nice to meet you.
**Bogdan Nicolae Stancu** 47:37 Thanks a lot for this.
**MG Marylia Gutierrez** 47:38 And thanks for joining!
Bye.
