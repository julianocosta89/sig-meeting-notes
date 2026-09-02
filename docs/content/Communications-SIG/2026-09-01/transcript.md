SIG: Communications SIG
Date: 2026-09-01
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Virginia-Diana Todea (VictoriaMetrics)** 02:50 Right, Severin?
**Severin Neumann (Bronto)** 02:53 How are you doing?
**Virginia-Diana Todea (VictoriaMetrics)** 02:55 Yeah, I'm good, fine. Sorry, I'm not gonna put myself in video, because I have a toddler here, and I'm officially on PTO, so it's a big…
**Severin Neumann (Bronto)** 03:03 Well, you should not do meetings during your PTO.
**Virginia-Diana Todea (VictoriaMetrics)** 03:07 Yeah, no, it's one of those things, yeah, you shouldn't do that, but I think we had some pending things to discuss, so even if we don't stay the entire hour, it's okay.
**Severin Neumann (Bronto)** 03:18 Yeah, yeah, no worries. Just, let's see if…
**Virginia-Diana Todea (VictoriaMetrics)** 03:22 Yup.
**Severin Neumann (Bronto)** 03:22 Is there any topic from, like, from the agenda you want to talk about in particular? Because then, like, we can put it at the front of the session.
**Virginia-Diana Todea (VictoriaMetrics)** 03:33 Yeah, I just added here a couple of things. So basically, obviously, we already talked about this async, about the release reports, if they're possible to run for non-maintainers. I don't know, to be honest.
**Severin Neumann (Bronto)** 03:50 I… I'm worried that not. Like, the one thing you could help us with is, like, what… what Vitor meant about, like, it is possible… possible to automate that. So what we could do is, like, have a… have a GitHub action added, like, every time at the first of the month.
Does a release on the website, right?
Okay. Because, I mean, I can quickly… we can email, like, I can… I think this is something where I can share my screen. Yeah, I should be able to do that.
Can you see my screen?
**Virginia-Diana Todea (VictoriaMetrics)** 04:25 Yep.
**Severin Neumann (Bronto)** 04:26 Yeah, let me just manage my, Zoom thingy here.
Because what you need to do is you need to be able to draft a release, right? So what we normally do is, like, you go into the releases, and I think you need maintainer permissions to do that.
**Virginia-Diana Todea (VictoriaMetrics)** 04:46 Alright.
**Severin Neumann (Bronto)** 04:46 I said, you can automate that, right? Because what we basically do is, like, I click on Draft a new release.
Sure. Then I… No, I think I need to do a tag first, right?
**Virginia-Diana Todea (VictoriaMetrics)** 05:02 Yeah, I think you need to create one for…
**Severin Neumann (Bronto)** 05:05 Yeah, I think I need to tack… But that's something I… Is it possible nowadays to do this via the… commits here… Can I do attack from here?
Maybe. Because this is the one we should tag, right? They last on… On the day of… of the year… But I don't think we have UI capabilities to tag something.
So what I technically need to do… I'm just checking. Is there UI capabilities for tags?
Not really. And the releases need a tag, right? So I cannot… I cannot… Oh, create new tag.
**Virginia-Diana Todea (VictoriaMetrics)** 05:56 Yeah.
**Severin Neumann (Bronto)** 05:56 Let's try then. What is it, Dan? 2000…
**Virginia-Diana Todea (VictoriaMetrics)** 06:00 2608, yeah. Let me just… one second, while you are doing this, if you can pause, I'm just trying to see if I can, first of all, look at the releases. So they're, like, in codes, but… Where exactly… one second, then… Giant shooting.
Okay, so tags… Right, okay, so there's, like… Releases… Draft a new release… Well, I can click on draft on New Release. I'm not sure… you mean probably afterwards, if I'm able to actually publish it? Publish it.
**Severin Neumann (Bronto)** 06:56 I mean, feel free to share your screen, and we can… Oh, okay.
**Virginia-Diana Todea (VictoriaMetrics)** 07:00 Yeah, yeah, sure.
**Severin Neumann (Bronto)** 07:01 If you can… I mean, totally fine with me.
**Virginia-Diana Todea (VictoriaMetrics)** 07:04 Yeah, I didn't even try it, so that's why I… okay, I think… I cannot share the screen while you're sharing.
**Severin Neumann (Bronto)** 07:14 Oh yeah, let me stop sharing…
**Virginia-Diana Todea (VictoriaMetrics)** 07:17 No one's true.
Perfect. Okay… Marrying… so I'm here… Right, so… Meet on your tags…
**Severin Neumann (Bronto)** 07:32 So, exactly, and then call it.
**Virginia-Diana Todea (VictoriaMetrics)** 07:34 Which one? Okay, so 2026… Rule 8, school… And right now, it's like… But, but…
**Severin Neumann (Bronto)** 07:43 But now you created the tag, but what did it target, like…
**Virginia-Diana Todea (VictoriaMetrics)** 07:47 Okay, I don't know, right now the target is Maine, but…
**Severin Neumann (Bronto)** 07:52 Yeah, excellent. This tag will be created. Okay, but… what… what… but commit… Okay, it will probably take the commit… like… At the top of it.
I mean… Yeah, let's try it. I mean, worst case, we have 5 commits from September 1st in that thing, so… I just don't care, so that's, that's not making a huge difference.
**Virginia-Diana Todea (VictoriaMetrics)** 08:25 Right.
**Severin Neumann (Bronto)** 08:26 Again, 202608, then say release notes, and then say previous tag. No, no, you don't have to write anything here.
**Virginia-Diana Todea (VictoriaMetrics)** 08:37 Oh, okay, sorry.
**Severin Neumann (Bronto)** 08:38 Click here on, previous tab.
**Virginia-Diana Todea (VictoriaMetrics)** 08:42 Good luck.
**Severin Neumann (Bronto)** 08:43 That one, yeah, exactly, and then click Generate Release Notes.
**Virginia-Diana Todea (VictoriaMetrics)** 08:48 Okay.
**Severin Neumann (Bronto)** 08:49 And then hopefully it takes a little bit, and then you see, like, that's… that's the thing that Fabricio is doing all the time, right? Because that gives you, like, the bottom of it. So if you go into the preview…
**Virginia-Diana Todea (VictoriaMetrics)** 09:00 No.
**Severin Neumann (Bronto)** 09:01 If you go into the preview.
Then you scroll down to the… to the bottom of it.
**Virginia-Diana Todea (VictoriaMetrics)** 09:08 Nope.
**Severin Neumann (Bronto)** 09:08 Which makes… you see, like, there's the.
**Virginia-Diana Todea (VictoriaMetrics)** 09:12 Oh, okay.
**Severin Neumann (Bronto)** 09:13 Yeah, yeah.
**Virginia-Diana Todea (VictoriaMetrics)** 09:14 Yeah, we see kind of, like, the new style, right?
We'll change log until…
**Severin Neumann (Bronto)** 09:21 Yeah, exactly.
**Virginia-Diana Todea (VictoriaMetrics)** 09:23 Okay.
**Severin Neumann (Bronto)** 09:24 And then you.
**Virginia-Diana Todea (VictoriaMetrics)** 09:25 -
**Severin Neumann (Bronto)** 09:25 Quick publish release, yeah.
**Virginia-Diana Todea (VictoriaMetrics)** 09:29 Yeah, so should I just do it?
**Severin Neumann (Bronto)** 09:31 Let's do it. I mean, as I said, I don't care about those 5 commits that are now… That are now in September already, technically, so… And now, if you scroll down… I think it should have something like… I feel like there's the number of contributors.
**Virginia-Diana Todea (VictoriaMetrics)** 09:50 Yeah, it's, up, up, like here, new contributors.
**Severin Neumann (Bronto)** 09:55 Yeah, exactly, so that's what it normally gives you, like.
**Virginia-Diana Todea (VictoriaMetrics)** 09:58 And you just have to count it and say, like, how many there are, like.
**Severin Neumann (Bronto)** 10:01 Yeah, exactly, that's… that's what I think what Fabrizio was doing in the past, that he said, like, oh.
We have, I don't know, How many are there?
**Virginia-Diana Todea (VictoriaMetrics)** 10:13 23. 23.
So there are 22.
**Severin Neumann (Bronto)** 10:22 I just can't.
**Virginia-Diana Todea (VictoriaMetrics)** 10:24 Counted 23.
**Severin Neumann (Bronto)** 10:26 So what we technically could do, if we would turn this into a workflow.
Then, of course, we could split it out and say, like, hey, we have first-time contributors, or we have people contributing to this and that area of the… But then the question is more like, why not turn this into a running thing, where we just have a board or something like that.
That just… Shows it all the time.
Fair enough.
**Virginia-Diana Todea (VictoriaMetrics)** 10:56 Okay Yeah, I mean, exactly. We can make other things from this part, that was the…
**Severin Neumann (Bronto)** 11:04 Yeah.
**Virginia-Diana Todea (VictoriaMetrics)** 11:05 Exactly.
**Severin Neumann (Bronto)** 11:05 Exactly, I mean, you could count at the top, like, how many are… Also, people are not consistent, I guess, with the… with the tags on, like, the localization or something like that.
But probably you could use an LLM and say, like, hey.
Do the comparison between that tag and the tag of last year, and give me the statistics.
**Virginia-Diana Todea (VictoriaMetrics)** 11:25 Interesting. Okay.
**Severin Neumann (Bronto)** 11:27 Something like that.
I mean, people would definitely appreciate that, like, if we would have something like that, so…
**Virginia-Diana Todea (VictoriaMetrics)** 11:33 Yeah, that's a… yeah, I mean, I'll think about it. It is… could be a cold project, that's not a problem.
Yeah. Yeah, of course.
Yeah, this is,
**Severin Neumann (Bronto)** 11:43 But then we know that, like, approvers can do releases, which is totally fine, but because for us, I mean, a release has no real meaning, right? The only thing why we do it is to have this kind of overview of, like, hey, what has happened.
Because the cool thing is now that you can now do release comparison also over longer periods.
So you can do a year-over-year thing fairly easily, the release a number, so you can do… compare this one with, 25.8.
**Virginia-Diana Todea (VictoriaMetrics)** 12:17 Yeah, yeah, yeah.
**Severin Neumann (Bronto)** 12:17 And I think then you get, like, hey, we had 1,000 commits, almost 3,000 file changes, 64 contributors, blah blah blah.
**Virginia-Diana Todea (VictoriaMetrics)** 12:27 Got it. Yeah, it's good for reporting, or, yeah, just…
**Severin Neumann (Bronto)** 12:35 What we do normally, like, if you go into the blog, we do this yearly thing, right, where we, at the end of the year.
**Virginia-Diana Todea (VictoriaMetrics)** 12:42 Okay.
**Severin Neumann (Bronto)** 12:42 Do a block, so there's, like, a… year in review, like, it's, if you go into the OpenTelemetry blog.
in the 2026, just saying, like, scroll down, and I think it's the first or the second that… the second that we… you see the one above, right?
**Virginia-Diana Todea (VictoriaMetrics)** 12:59 Yeah, yeah, yeah.
**Severin Neumann (Bronto)** 13:00 And a lot of that is…
**Virginia-Diana Todea (VictoriaMetrics)** 13:02 Other puppies.
**Severin Neumann (Bronto)** 13:03 Some of that is drawn from that information, right? Where we say, like.
**Virginia-Diana Todea (VictoriaMetrics)** 13:06 we have?
**Severin Neumann (Bronto)** 13:07 many commits… Yeah.
And something like that, so…
**Virginia-Diana Todea (VictoriaMetrics)** 13:13 No, exactly.
Yeah, it's good to have. Yeah, for me, it's a… it's a project I can definitely spend more time and see.
what I can take from it, you know, if I can help out with something that is not yet available. Yeah. And yeah, I could, I could put it out here, like, actually we have it in comms, or where do we have it? I'm not sure.
**Severin Neumann (Bronto)** 13:41 Yeah, normally you can, you can… so I think Fabrizio in the past, like, I mean, you could scroll up, and then he said, like, hey, new release, blah blah blah, and then… then he shares some, some, some, some…
**Virginia-Diana Todea (VictoriaMetrics)** 13:51 Yeah, I think he was putting it somewhere else…
**Severin Neumann (Bronto)** 13:58 I think if you scroll up, like, in the comms channel, if you scroll up to, like, August 3rd.
There, he did, like… The last one.
**Virginia-Diana Todea (VictoriaMetrics)** 14:08 Yeah, I'm trying to… Okay. Yeah. So, yeah.
Oops, nope.
Cool, yeah, yeah, yeah, so it's this one.
Yes.
So, okay, yeah, not a problem. It's just, like, to maintain more or less, like, a similar pattern.
**Severin Neumann (Bronto)** 14:29 Yeah.
**Virginia-Diana Todea (VictoriaMetrics)** 14:39 And then I can include this one that we have.
Yeah, yeah, okay, cool, that's… I mean, it's not, Biggie, in the sense that it's… But yeah, I wanted to see if it's done, and we'll kind of, like, made sure that it can be done, and from this one, I can build on something else.
Yeah, and the next thing I wanted to discuss was, just, I wanted to make sure I'm doing this properly. Obviously, I went ahead and… approved a bunch of things, I went with everything that was there. I, obviously, there are lots of, PRs there, there are lots of bosses.
**Severin Neumann (Bronto)** 15:36 Yeah.
**Virginia-Diana Todea (VictoriaMetrics)** 15:37 that give information. Sometimes I'm not approving it, because I'm not sure, especially the ones that, make a reference, probably I don't even have rights to accept, approve those ones, probably they go for the maintainers.
**Severin Neumann (Bronto)** 15:50 Basically, you should be able to approve everything, right? The moment you're an approver, you should be able to approve everything.
So, sometimes it's just like… but this is more the infrastructure stuff that especially Patrice and… and also Vitor are working on very often, that they sometimes verbally say something like, hey, I need a maintainer to approve it, but very often, like, if you take a look and approve it, it's… I mean, that's what we have here for as an approver, right?
**Virginia-Diana Todea (VictoriaMetrics)** 16:22 Yeah, yeah, no, for sure.
I mean, in the sense that I didn't want to prove it, because I need more time to understand, like, what's happening there, in the sense that sometimes it's not very clear for me, okay, is this registry I mean, is this request okay? Do I have to approve it? It's not. It's just, like, it's just pure formality, like, it really… it doesn't do any harm, or do I have to go through all the code and…
**Severin Neumann (Bronto)** 16:49 See what it is.
**Virginia-Diana Todea (VictoriaMetrics)** 16:49 does, or it's just a formality, and I just click on OK.
**Severin Neumann (Bronto)** 16:53 Yeah, so for the automated… you mean the automated PRs, right? Like the…
**Virginia-Diana Todea (VictoriaMetrics)** 16:57 Yup.
**Severin Neumann (Bronto)** 16:58 Yeah, so what I normally do is, like, I go over the code and I scan through it, like, I scroll over it if anything really jumps out, because normally you would see this really quickly, but then I approve them and merge them in, but I mean, you can approve them, that shortens it for us a little bit, but very often those are, like.
A proven merge in one shot for a maintainer.
**Virginia-Diana Todea (VictoriaMetrics)** 17:22 Okay.
**Severin Neumann (Bronto)** 17:23 Goodbye.
don't… I mean, I appreciate if you review them, but if you think, like, hey, they're just noise, then you also can do them, and spend more time on the other ones, like, there's definitely more value in doing them, right?
Just from my point of view, yeah.
**Virginia-Diana Todea (VictoriaMetrics)** 17:43 Sure, yeah, not a problem. I mean, right now, I've been, doing quite a bit of… activity there, so it's okay, and it's fine. I went back to this one, which was open on the July 12th.
**Severin Neumann (Bronto)** 17:58 Yeah.
**Virginia-Diana Todea (VictoriaMetrics)** 17:59 Because, yeah, Lisa is doing a bunch of, OpenTelemetry for Beginners videos. She did some in the past, like, before that in March, I think, and I also reviewed those, and they were okay.
This time we also had somebody else reviewing it via the CNCF Slack channel, so prior, like, in the same time. So she did, like, some corrections here that are not seen.
So I went to read, they're… they're useful, so definitely for beginners, I approved them. Sorry, not approved them, I put triage accepted.
**Severin Neumann (Bronto)** 18:34 Yeah.
**Virginia-Diana Todea (VictoriaMetrics)** 18:35 So it's just, about, going through the PR and… I think they're useful, especially for the… For the beginners, yeah, no.
**Severin Neumann (Bronto)** 18:46 I think that's the… that's the goal, what, what Lisa is doing there. So the thing is, it's a little bit of a… of a side project, right, that… that… that she's doing that.
Of course, I really hope that at some point we can integrate them a little bit better into the website.
**Virginia-Diana Todea (VictoriaMetrics)** 19:04 We've got…
**Severin Neumann (Bronto)** 19:04 pay attention to them, and if you give her feedback, because at the end, what she really needs is, like, a partner in crime like that.
Because one person creates the stuff, one person reviews it… I mean, technically, for me, it would also be okay if I… if you or anybody else would also create part of the content, and she's reviewing it, right? I mean…
**Virginia-Diana Todea (VictoriaMetrics)** 19:24 Yeah, yeah.
**Severin Neumann (Bronto)** 19:25 It's not like that she owns that, right? It's just more like she's doing that, and so far, nobody else… I asked a bunch of people already, like, hey, would you be interested to help Lisa with that? But so far, nobody showed up, but if you're curious about that, and I think, in general.
there's a lot of work that needs to be done around it, and I think you shared that same sentiment in the survey that I did.
we need much, much more… put attention back into the whole getting started experience, and the whole, docs and stuff around getting started, so I'm more than happy if you give her a hand on that, and make it possible that she can release some of those, so… Maybe we chase Lisa and ask her if she's, like, has everything to put out the next videos.
**Virginia-Diana Todea (VictoriaMetrics)** 20:17 It's interesting.
**Severin Neumann (Bronto)** 20:17 The first one is already now a year old.
**Virginia-Diana Todea (VictoriaMetrics)** 20:20 Yes, ma'am.
**Severin Neumann (Bronto)** 20:21 people in the comments asked for, like, the next one, so… Welcome to OTA!
**Virginia-Diana Todea (VictoriaMetrics)** 20:28 Yeah, no, I mean, yeah, no, I mean, she's been doing work because she asked me for some feedback back in March this year.
So, I already went through that and gave her a bunch of… For those ones, I think… So for that… but these are new. These two ones are new. I'm not sure if she… because I don't see them open, if she already.
**Severin Neumann (Bronto)** 20:50 Hmm.
**Virginia-Diana Todea (VictoriaMetrics)** 20:51 She already merged those that I did for… Yeah, looks like something happened, because they're not here, so probably she already merged something, but I don't… I don't think so, because they should be on the website.
**Severin Neumann (Bronto)** 21:05 Yeah, I can ping here and see, like, maybe something came… got… got in her way.
**Virginia-Diana Todea (VictoriaMetrics)** 21:16 Oh yeah, yeah, it's here. So, February… Anyway, yeah, I could ping her, because we definitely did that together, and.
**Severin Neumann (Bronto)** 21:26 Yeah.
**Virginia-Diana Todea (VictoriaMetrics)** 21:27 We already, we already did that.
**Severin Neumann (Bronto)** 21:32 Yeah, because last time I talked with Sarah, I think she always also has some other responsibilities she… she needs to…
**Virginia-Diana Todea (VictoriaMetrics)** 21:38 So, yeah. Woohoo!
Yeah, of course. Yeah, okay, I'll get back with her, but this is, like, it's good to, know that, we definitely are on the same, the same, Idea, yeah, the same… the same thoughts. I mean, from my side, it's okay. Like I said, I'm… I'm doing this, step-by-step is definitely a lot more that I understand now, that I see, like, all the PRs and all the workflows going on.
What I need… I need also from your side, like, not only from you, but, like, from the maintainer side, like, besides this, automated, bot, whatever, reminders to approve stock, what I can help with more, in a sense that you… if you tell me, hey, approvers, we need… these type of PRs that we definitely need to, you know, click on approve, or we need a set of eyes, like.
focus on this type, and then, for me, it's already good to, as an exercise, to take a look and see, okay, so this is… this type is different from the other stuff, and maybe like this, I could already train myself a bit more on, on those.
**Severin Neumann (Bronto)** 22:57 Yeah, so, I mean, what I think… so I think, as you know, like, there's a lot of moving pieces in our repository, and I mean, sure, you are a maintainer and approver for some of the localizations, that's definitely… that's definitely one part, but the thing I think that's… That's always the most important for us.
Is… is anything… It's anything related to real documentation.
**Virginia-Diana Todea (VictoriaMetrics)** 23:27 Okay.
**Severin Neumann (Bronto)** 23:29 So whenever there is a block… whenever there's an issue, or in PR, it says, like… like the one here that we have at Pop, like, feature flag names and service.
Coverage drift.
Also that, like, the demo maintainers reviewed it already, so, so that you take a look at it more from a… not necessarily anymore from a technical perspective, which is still fine if you spot anything, but more like, hey, does it look good on the website? Did they miss any good practices? Did they miss to link back, maybe, to specific things? Something like that, and then approve it, right? So… And then one thing you should never forget, right, I mean, you can approve all the PRs, but I'm also more than happy if you say, like, hey.
there's a particular section in the documentation that I want to improve.
any getting started guides, or any concept pages where you have to fill in… like, all of them need love and attention, right? All of them are, like.
Yeah.
So… If there's anything in that regards, then, then yeah, sure, take… take a look into doing… doing your own Your own thing on top of it, so…
**Virginia-Diana Todea (VictoriaMetrics)** 24:56 Okay, yeah, no, yeah, I mean, we, yeah, we discussed this, previously, that's totally fine.
Okay, yeah, I mean, of course, there's a lot, that I also want to do from my side and understand more, but yeah, I mean… It's just the beginning, so yeah, it's not a problem, there is… there is time to… really deep dive into everything. But yeah, I like the idea that you said the last time, for example, well, right now it's just the two of us, but, that you said the last time some, that in the comms meeting, it's good maybe to go through the dashboard.
And look together at some issues, or PRs, and just discuss them.
I think it's a good exercise in general.
**Severin Neumann (Bronto)** 25:42 Yeah, yeah. Yeah, no, we definitely can spend some time on that.
**Virginia-Diana Todea (VictoriaMetrics)** 25:47 Well.
**Severin Neumann (Bronto)** 25:48 But I suspect today you're happy if we… if we close early.
**Virginia-Diana Todea (VictoriaMetrics)** 25:52 Yeah, yeah, yeah, of course.
**Severin Neumann (Bronto)** 25:54 Yeah.
**Virginia-Diana Todea (VictoriaMetrics)** 25:54 I'll stop sharing, I also have a toddler who's.
**Severin Neumann (Bronto)** 25:57 Yeah, no worries. So since nobody else is here today, like, we can call it a day, and then circle back on all these things. Sure. So I really hope that now people come back to Burger. I mean, here in Germany, it's still… for some regions, at least, it's still summer break.
**Virginia-Diana Todea (VictoriaMetrics)** 26:16 Yeah, yeah.
**Severin Neumann (Bronto)** 26:17 I think over the next two weeks, everybody's coming back, so let's hope that… Did things… return to a little bit more normal by then. So yeah, then enjoy your time off, and I appreciate you to come here.
Today?
**Virginia-Diana Todea (VictoriaMetrics)** 26:31 No problem. Yeah. Yeah, thank you, Severin, and yeah, good luck with the talks at CNCF Meetups.
**Severin Neumann (Bronto)** 26:37 Yeah, thank you.
**Virginia-Diana Todea (VictoriaMetrics)** 26:38 This is cool, and by the way, congrats on the ambassadorship.
**Severin Neumann (Bronto)** 26:42 Yeah, thank you.
**Virginia-Diana Todea (VictoriaMetrics)** 26:43 deserve. Yeah, thank you. But yeah, we'll see each other in two weeks, in the next meeting. Thank you so much.
**Severin Neumann (Bronto)** 26:49 Exactly.
Thank you, bye-bye.
**Virginia-Diana Todea (VictoriaMetrics)** 26:51 Bye.
