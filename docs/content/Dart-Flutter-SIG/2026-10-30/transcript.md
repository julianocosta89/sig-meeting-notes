SIG: Dart & Flutter SIG
Date: 2026-10-30
Duration: 30 minutes
============================================================

## Zoom Recording Transcript

**La Pyae Oo** 05:02 Only a Duke.
**Robert Magnusson** 05:05 Yeah, maybe there's a time difference issue, because in, In Europe, at least, we have the daylight saving.
So this is one hour earlier than it usually is.
Maybe I can give a ping in the channel.
One second… How are you doing? All good.
**La Pyae Oo** 05:44 Alright, yes, all good.
I think… I don't know.
Paste the program in.
And around… and I'm in itself.
Oh.
That is only happening for me, and then it's remarks.
our company need to meet Phoebe and to enter some, some website, so… I can't blow them, and I ran them songs.
**Robert Magnusson** 06:13 Sorry, Kizayan, I was just, pinging in the chat that we started the meeting. Sorry.
What were you saying?
**La Pyae Oo** 06:21 Thank you.
**Robert Magnusson** 06:36 Sorry, Lapai, did you say something before? I missed it, because I was typing in the chat, pinging people that the meeting is starting.
**La Pyae Oo** 06:45 Aw, okay. I know, I was, And got lower in… entering in… entering in websites.
One, and I intuitive, so, yeah.
I think there is only happening in between there.
When I enter to the phone, there is a loading.
loading.
I need to connect PPM, yes, you answered this, so, yeah.
I'll talk.
**Robert Magnusson** 07:16 I don't Harshit.
the cohesive.
More people drawing.
Hello?
Here's maybe a few more minutes, and see if Michael also joins. I didn't hear anything from him.
I'll share my screen… I guess.
Michael will not join.
So, what could be our meeting topic?
what's open? Are you blocked by something? I tried to catch up this week on PRs. I just had a really busy… weak, but… Yeah, I try to do at least… prioritize the Dart work and do it within, like, 2 days.
Is this something where you're blocked on, that you're waiting on feedback?
Good point.
However… Sorry, one second.
I have to turn my window there, okay… So, these are open PRs. That's yours, right, Harshit?
That's the pull request template, yes.
feedback, yes, but I think after this feedback, it should be good to go.
Some open questions, or it, it feels… I don't remember.
**Harshit Kushwaha (OpenTelemetry)** 11:01 Previously, we were having a discussion on the pull request template in SDK, Michael has said that AI is just a tool used by us, so we should have keep it as, like, I am a human authored this pull request, because AI is just like our tool, like a ID we use.
We have to keep it authored instead of verified.
So that's how I keep it author.
It's the same thing we are doing in the SDK right now.
**Robert Magnusson** 11:36 You mean running this, like,
**Harshit Kushwaha (OpenTelemetry)** 11:38 Yes.
**Robert Magnusson** 11:39 The, the wording here.
**Harshit Kushwaha (OpenTelemetry)** 11:44 when we were deciding the call request template for SDK, we decided the same thing there.
**Yusuf** 11:54 I think it's more… this one is more of me nitpicking on the step, on the wording.
Guess, well, to be honest, what's not?
My PR… I only do the verification, most of the… most of the right thing is, like, almost the other is actually on the AI.
Hello, Ryan.
**Robert Magnusson** 12:16 What's do… This is the… Following from the…
**Yusuf** 12:36 the previous one.
**Robert Magnusson** 12:38 Okay.
I don't know. I'm open to this.
I, I mean, I worked the same thing, that's mainly… AI is altering… It depends what author means, yeah. I guess it's, like, semantics.
But what do you say?
**Yusuf** 13:00 It's not a blocker, it's not… don't worry, it's not a blocker.
**Robert Magnusson** 13:04 Should we keep it also? Because what did you say, Harshita? We landed on authored in the… in the Dartastic report.
**Harshit Kushwaha (OpenTelemetry)** 13:09 previously.
**Robert Magnusson** 13:11 Okay.
Yeah, I mean, we can leave it also then, or what do you think, Yusuf?
**Yusuf** 13:19 Yeah, yeah, yeah.
**Robert Magnusson** 13:20 than it's interesting.
**Yusuf** 13:22 I… it's not a blocker.
I mean, it's not… I don't think it's… it matters anyway.
**Robert Magnusson** 13:29 Yeah.
Okay, cool. And other open… Questions on this, so then we are…
**Yusuf** 13:37 Hmm.
**Robert Magnusson** 13:37 Good to go.
Or do you have some other questions on the feedback, Harshit, or… Would that be… Good afternoon, so now we can leave this authored.
I don't remember my comments, what did I say? Something… I used the wording to use this pattern.
**Harshit Kushwaha (OpenTelemetry)** 14:01 Yes, I will update the comment.
Cool.
**Robert Magnusson** 14:10 Thank you.
And then the other, open PR… From Yusuf, thanks for driving this. I think this is, like, the bigger parts now, getting stuff in.
Into the… to the repo.
**Yusuf** 14:28 I mean, I'm trying, to be honest.
This one has been crazy for me.
Yes, I think it was, like, two times where I wasn't able to join the call.
So, yeah, I'm…
**Robert Magnusson** 14:43 No worries.
**Yusuf** 14:45 We're happy to see.
**Robert Magnusson** 14:46 That's all the time you can give us.
**Yusuf** 14:47 To find the time. But yeah, this is basically, to bootstrap.
the workspace. I also included CI for this.
So, it has, like, some verification.
If there are changes.
Yeah, this one is, I tried to follow what was, recommended by our… in our docs on project structure. That was, Michael's suggestion, so… So, do give this one… do I have… do… do review this change, this PR? Was it… is it still in draft? Oh, yeah, it's still in draft.
**Robert Magnusson** 15:29 It's still draft, but I think it could be a move to… To rewrite, because it feels more… more ready than drafty.
**Yusuf** 15:36 Yeah, yeah.
**Robert Magnusson** 15:39 Should I move it to ready for review?
**Yusuf** 15:42 Yeah, yeah, yeah, yeah. I'll… I think I can look into this over the weekend.
**Robert Magnusson** 15:48 Cool. I think I looked it over, and it looks great. I just had some thoughts on these awesome… placeholders. I guess they are created, like, out of the box when you create,
**Yusuf** 16:01 Those are all auto-generated by the…
**Robert Magnusson** 16:03 Yeah.
**Yusuf** 16:04 But Dart template, so there's not really much in…
**Robert Magnusson** 16:09 I think that was the only thing I found on this, that maybe we should just replace them with some sort of just empty… Empty files instead.
**Yusuf** 16:19 Oh, oh, show you one of the reasons why I do it this way? Because there is a CI that validates the run.
**Robert Magnusson** 16:27 I guess just, my toolbox used to not have this Place all the code that we will just remove directly afterwards, if we just replace.
**Yusuf** 16:35 Think about this.
**Robert Magnusson** 16:36 Sort of empty… empty files like this.
I mean, this is probably something we.
**Yusuf** 16:41 Okay, okay, alright, alright, got it.
**Robert Magnusson** 16:43 It would be sort of a… cleaner state, and just a tiny thing on maybe the changelog that it's, instead of just saying instant release, just, like, the initial, like, setting up the core package structure.
**Yusuf** 16:55 Yep, yep.
**Robert Magnusson** 16:56 But otherwise, I think it looked, it looked great.
**Yusuf** 16:59 Yep, yep, yep.
I'll, I'll limit…
**Robert Magnusson** 17:04 Super, thank you. I mean, also, if you're too underwater, I also had a really crazy last two weeks.
At work. But if you're too underwater, we can also split… split workload, because I saw you also took the other task to start actually moving in.
The semantics. So just let us know, then, if you want to… if you want to have some support on this.
**Yusuf** 17:24 I do appreciate some support, on top of the semantics. I mean, the drop is already there, the content is already there, if, like, yeah, so anyone can drop in, like, first-level review.
Even though it's still in draft. I think it's 4 off for the… addressing for semantics, Flutter, and just the default semantics, because currently, I just bought our fully semantics to… Good da-da-da.
semantics package. I don't actually create a semantics Flutter yet.
Since I'm also not sure what… how's the content gonna be for Flutter.
**Robert Magnusson** 18:06 Yep.
**Yusuf** 18:08 Okay.
**Robert Magnusson** 18:09 Yeah, also, I'm not 100% sure what we agreed on there with Michael. I think, like, Michael had this vision, what should go in there?
**Yusuf** 18:16 Yes.
**Robert Magnusson** 18:17 It just…
**Yusuf** 18:17 You did mention about there's a, like, the extra semantics for specifically for Flutter, but let's kind of open a question if I should move, like, Android iOS semantics to Flutter too, or… R.
Android and iOS shouldn't be there, and… It should not be in semantic Flutter. This is, like, gonna create a computer for me. So, reason why I put it in draft, because I plan to have a doc, like, how he came up with, for the project structure. Yeah, so there's the reason why it's in draft.
**Robert Magnusson** 18:54 Okay.
That sounds good. Maybe we can discuss… discuss that async, also with Michael, and see his vision on it.
But I think at least, like, this other one should be unblocked, so that should be able to be merged once it's, Approved. I think that's… that's clear.
The package structure.
**Yusuf** 19:13 Yep, yep.
**Robert Magnusson** 19:15 Like, I think that's it, because then that's the draft, and then this is just a renovate PR dependency updates that I can look into later.
And in Dartastic side of things.
What do we have there? Doesn't work. In a second, sorry.
Oh, sorry, I didn't really do any PRs at all, I've just been reviewing PRs, I've not been creating any code.
I will try to be more active also creating code.
Rs is one, two pairs open.
Is this the bigger one, async Valley Hardin… Yu Harshit… And actually, I started reviewing this.
You gave feedback. Yeah, so I found some small follow-up issues. I'm about… I was just starting to post them.
But I think it's… Close to done. Sorry for not finding all of this directly.
But I ran also a lot of AI over this now, and I think my last findings, Should be the last ones, at least.
I threw a lot of agents at it, and it looks in good shape. There's just, like, some edge cases that I found that I'm about to comment on.
Like, some enums that lose state.
So, I hope to have the comments out and all.
Okay, maybe 2 hours after this meeting.
And I'm sure, I guess Mike also wants to give, his input, because he… mentioned here, right? He wants to look into this, and… And focus on this. I'm not sure how much time he has. He said he would have a busy week this week, maybe he has more time next week.
But, yeah, I will try to focus on this and give you an update, Harshit that you have real estate.
And the other one… Formula Pay… I just threw a poore this morning.
So I guess we could merge this afterwards. Thanks for the…
**La Pyae Oo** 21:34 I think I need to update… I need to update this also, because from SDP, Harshit Also, I read it.
Beautiful.
Fantastic.
I think I need to update.
Down.
Who cares?
**Robert Magnusson** 21:53 Okay.
**La Pyae Oo** 21:54 Yeah.
**Robert Magnusson** 21:55 some changes, that's the case, I don't think, to me.
**La Pyae Oo** 21:57 Yes, that's an awesome idea.
Next.
**Robert Magnusson** 22:10 Message in here, template, or is it merged already, maybe?
Implement.
Okay. Yeah, then this update, I'm watching that PR, so I will just review it as soon as it's been. I'll try to get through all the PRs.
**La Pyae Oo** 22:26 today.
Perfect country.
**Robert Magnusson** 22:29 And then in the SDK side of things, something here urgent blocking you? I mean, I have an old one here I have to update. It was blocked by the API work way back ago.
I will try to lift this up again, and work on this.
Something here you're blocked by that you want urgent feedback on?
That's my gold.
Open… Maybe I look into Ben, that's the guy from, embrace. It would be nice if he also gets more active, so I… maybe I focus on this and give him some feedback.
Should we just go quickly over them?
What's this test?
Alright… Plugged on echo… And I reviewed it also… Hi, you did a change since then, okay, then I'm gonna re-review this.
But I guess it's then, blocked by Michael, so Michael needs to give his… thumbs… thumbs up. But I will review it, and I can… I'll give it a green light from my side, at least.
export risk.
**Yusuf** 23:54 Yeah, to be honest, I've already forgot what about the… what's this about?
**Robert Magnusson** 24:00 I mean, that's tough now in the beginning, we have so many PRs to work through.
**Yusuf** 24:05 Fucked.
**Robert Magnusson** 24:06 Once everything gets in, we have a bit more, like, incremental step-by-step work.
**Yusuf** 24:12 Yeah.
Well, I mean, mainly because I've.
**Robert Magnusson** 24:15 It is also quite old, yeah.
**Yusuf** 24:17 Ugh.
Oh, yeah, it was from August, oh.
**Robert Magnusson** 24:22 But no worries. Yeah, maybe we don't have to go with them, but I will… make sure today that I go over all the open PRs and give feedback on all of them.
And then they shall be in a better state.
I don't have to go over them one by one, but is there something you feel like you're blocked on that you want to have pushed out, that I should do first?
**Yusuf** 24:45 I… I'm not gonna say it's blocking anything.
Could be, just… I forgot, was it part of, like, the one that's blocking from merging and porting is to open telemetry?
Because I really need to look into the PR again.
**Robert Magnusson** 25:06 For which parallel, do you mean, sorry?
**Yusuf** 25:13 No, I'm talking about mine. I'm not sure if that one's blocking anything.
**Robert Magnusson** 25:20 Even the packet structure.
**Yusuf** 25:23 Oh, no, no, the one that you just opened. 292, yeah, I'm not sure.
**Robert Magnusson** 25:27 Perfect. No, I think it's not blocking. I think it's,
**Yusuf** 25:31 Yes.
**Robert Magnusson** 25:31 Standing on its own.
So, I think, no worries there. I would just, go over it. I'm not so familiar with the metric part of OpenTelemetry, so I guess I need a bit more time to get into that concept, but… Yeah, I will get to it and review it.
**Yusuf** 25:49 Alright, alright,
**Robert Magnusson** 25:50 And… Okay. Yeah, sorry.
Yeah, I think then the point was that Michael wanted to run another one of these audits and see where we still are missing, where we still have gaps.
And process-wide, I think then to get it officially into OTEL… with OTEL Dart repo, is what you started working on, Yusuf, with the semantics.
So I think we are on good track there, getting the package structure in, then getting your semantics in.
Verifying again, on the Dartastic side of things, that it's in sync.
Opening new issues, fixing them, and getting the API into… The old title.
Dark.
Oh.
Yeah, I think we're on scope. It's just everyone is busy, and things take more time than you think.
This analog serum,
**Michael Bushe (Mindful Software, LLC)** 27:00 Hello, gentlemen, sorry about that, my first European time zone change ever, so I got cut off, cut out a little.
**Robert Magnusson** 27:07 Hello.
Oh, no worries.
**Yusuf** 27:10 Hey, hey, hello.
**Robert Magnusson** 27:13 How are you, Michael?
**Michael Bushe (Mindful Software, LLC)** 27:14 I'm doing great. How are you guys doing?
**Robert Magnusson** 27:18 Good, good. We just went over the open… open issues, open PRs.
Yeah, and it's not so much, actually, in the… maybe you have good input there on the… I close it now.
So, in, Autel Dart… We have, this first package structure from Yusuf?
Open.
I guess that's the first thing we need to get in.
I think it looks good, with some minor comments on maybe those awesome out-of-the-box things.
But then I was not sure on the next part.
Because you supposed to open this, The art to stop moving in the semantics.
And I don't remember what we said there, what you… what your vision was to do that.
It's anyway blocked by the packet structure to get that in first, but after that…
**Michael Bushe (Mindful Software, LLC)** 28:17 Right? I briefly looked at the package structure, I saw your comment, I was good with that. I didn't actually look at it. I have almost no time this week, but I'll get to that this coming week, or even over the weekend. But then, yeah, the semantics, I didn't look at anything else. So the semantics is, What's, what's, what's the deal there?
This shouldn't be too hard.
**Robert Magnusson** 28:43 it's moving in the… or maybe you can explain it better, Yusuf, but it… is it this one? Sportsman's Conventional…
**Yusuf** 28:51 So, talking about semantics, right? What I did in this PR is actually just… I bought one-to-one from the… from the Datastic API.
The semantics, but based on the documentation, we have a plan to have a semantics Flutter, right?
So… Yeah, as of now, I do see there is, like, Android semantics, iOS semantics… Right? So, yeah, I was wondering if that should be in semantic Flutter, or it should be… should be in this ripple?
**Michael Bushe (Mindful Software, LLC)** 29:28 So, right… so, is this Weaver-generated?
**Yusuf** 29:31 Yes, yes, yes, it is.
Let's see here.
**Michael Bushe (Mindful Software, LLC)** 29:36 And where's Gen UI? Gen AI? Okay, I got it, I see it. I just wanted to make… that's the first federated one, I wanted to see that. Let's… where's… where's the, script?
That generates these.
**Yusuf** 29:49 Scripts, hmm.
Fuck, Let's look at that.
**Michael Bushe (Mindful Software, LLC)** 30:00 Should be in… Cool, that's where we… There, tools, simultane, okay, here we go.
**Yusuf** 30:07 Yeah, yeah, that's what it is.
Correct.
Sir, Awesome!
**Michael Bushe (Mindful Software, LLC)** 30:21 Alright, if it works, and then did you compare one-to-one to make sure it's consistent with what the API has now?
**Yusuf** 30:30 I'm sorry?
**Michael Bushe (Mindful Software, LLC)** 30:32 After you generated, did you take… did you compare the files Do a file compare, and each file.
And make sure that they are consistent with the Mindful Software API ones.
**Yusuf** 30:47 Oh… I didn't do that. Maybe I should, I should do that.
**Michael Bushe (Mindful Software, LLC)** 30:54 Just to make sure we didn't miss anything. It doesn't have… that doesn't have to be checked in, but just a… just a try.
**Yusuf** 31:00 Yeah, yeah, yeah. I'll do that, I'll do that. I'll just do some screenshot comparing all these, values at the same.
Excellent.
**Michael Bushe (Mindful Software, LLC)** 31:10 Yep. And then once we have it in… that's really great. I'll… I will take a look at that this weekend.
**Yusuf** 31:16 And…
**Michael Bushe (Mindful Software, LLC)** 31:17 After that, and we could just… let's just do one so it's the same.
And then we'll need a follow-up issue on Genuide, because that's the first federated one, so we'll have to change our script.
to bring in the new Gen UI, which I don't know if they're the same enums they've always had, but they at least moved their…
**Yusuf** 31:40 Excuse me?
**Michael Bushe (Mindful Software, LLC)** 31:41 So we'd have to pull in that… new, repo that Weaver can read.
But let's… but let's do this first.
**Robert Magnusson** 31:52 Yeah.
**Yusuf** 31:53 Alright, sure, sure.
**Robert Magnusson** 31:54 Maybe I'm a bit slow here, but… What is this doing? So, so this weaver, it reads, like, YAML, spec file and creates this, Dart… semantic files.
**Yusuf** 32:08 excuse me.
**Robert Magnusson** 32:09 ish.
**Michael Bushe (Mindful Software, LLC)** 32:10 That's right. Weaver is the tool… none of this is… none of those are handwritten. The, This is why I was… okay, so you… you copied the files over, right? Is that right?
**Yusuf** 32:22 Yep, yep.
**Michael Bushe (Mindful Software, LLC)** 32:23 Okay, okay.
You, I think… yeah, that's fair enough. That's fair enough. Why don't we do it this way first? That way we know it's all the same. You don't have to check, right? And then we can start here, and then… it would be… but none of those files were created by hand. Weaver is a tool that is used throughout OpenTelemetry. It's a really cool tool. It's not just used for this, but it is at least initially used for this.
Which is, it looks at the spec files, like the…
**Robert Magnusson** 33:01 those YAML files. Like, can I talk to Martin from the Client SIG group?
I talked to Martin Kuba from the Client SIG group.
**Michael Bushe (Mindful Software, LLC)** 33:12 Oh, good, good.
**Robert Magnusson** 33:13 He said they're creating, like, this… just a second, I will open the repo. Just give me, like, one second.
**Michael Bushe (Mindful Software, LLC)** 33:20 Yeah, he's… yeah, they're working on the client ones.
I didn't go to that meeting last week either, or 2 weeks ago, whatever it was.
**Robert Magnusson** 33:28 No, me neither. I said I would, but when I talked to him, I didn't have time. So, he said they're creating this here, and here they have, like, these, for browser, he started using that, and that's, like.
**Michael Bushe (Mindful Software, LLC)** 33:40 Right, exactly.
**Robert Magnusson** 33:40 Introducing.
**Michael Bushe (Mindful Software, LLC)** 33:41 Browsing ones, right.
**Robert Magnusson** 33:42 And here they have these YAML files, and these then are used by… I think by Weaver, I'm able to create, actually, the… her language.
files, but also, like, the docs gets created from these, I think, if I understand them correctly, like, these…
**Michael Bushe (Mindful Software, LLC)** 33:58 Correct. And Weaver generates the code for every language out of those, right?
Yeah. So… We're gonna ignore that just for now. Just for… let's get one… let's get an exact copy of what we have with whatever… spec version that we made them from last time, which I think was… 60. Might have been 59.
And then… and and then… right, and then let's have another issue where we pull in… there's two, right? So there's GenUI, they moved… that's not client, but we still have to deliver it for Dart users. That's a really… big one, that's an important one. It's a hot one. And they moved theirs out, and so, right, agreed, the browser… let's grab the browser one, too. We should do that as two separate issues.
**Robert Magnusson** 34:54 And where do we… so we also have something similar like this, then. We store, like, these, specification files.
**Michael Bushe (Mindful Software, LLC)** 35:03 We don't…
**Robert Magnusson** 35:03 We don't have any, so…
**Michael Bushe (Mindful Software, LLC)** 35:06 Today.
**Robert Magnusson** 35:06 So ours are hard-coded, like, manually written.
**Michael Bushe (Mindful Software, LLC)** 35:09 No, no.
**Robert Magnusson** 35:10 And then we merged them in with the old tail-created ones. Yeah, sorry for the stupid questions.
**Michael Bushe (Mindful Software, LLC)** 35:16 No, no, no, that's a smart question. There are no stupid questions, right? We just… there aren't any Flutter ones, so this is the other step. This is another step.
So there's… we only deliver ones for everybody else, and we don't have anything for Flutter ourselves. And so that… that's another issue. We… we identified that in the plan, and there should be a… there should be a directory for that? Maybe there isn't.
**Yusuf** 35:47 No, no, no, I'm not. I… because I'm… I'm not sure if I should… should I, like, should I create it right away here? Because I don't… it doesn't have a content yet.
That I can think of?
**Robert Magnusson** 36:03 But in this directory, that's where, like, the generated files would live, right? This is where the output for that we were generated would come.
**Michael Bushe (Mindful Software, LLC)** 36:11 Right, and so… right, and so then we would also need… maybe that's the same directory, maybe in the root directory is where we store the YAML file for Flutter.
Which would have Flutter life cycle, or hey, go to town, whatever you guys want to put in there.
Nothing there now, so it's a greenfield.
**Yusuf** 36:32 That's fair.
**Robert Magnusson** 36:32 Okay, so we would have a separate folder here that is, specced. Do we have something like that? No, we don't have anything like that currently in the.
**Michael Bushe (Mindful Software, LLC)** 36:39 Nothing at all. So, right, I guess, Flutter, just, or, or, Maybe it's a whole other directory, but I don't think so, I think it should fit under… No, wait a minute, wait a minute, wait a minute.
This… these directories are our packages, right? Yes, yes. And so we should keep our spec out of our package.
Because…
**Robert Magnusson** 37:04 And there'd be an open… yeah, sorry, go.
**Michael Bushe (Mindful Software, LLC)** 37:07 Yeah, so just another directory, Flutter semantics, or… I don't know, OpenTelemetry, Flutter semantics, or something like that.
**Yusuf** 37:15 I think it's gonna be semantic Flutter or something like that.
semantics and drive.
**Michael Bushe (Mindful Software, LLC)** 37:21 Awesome, awesome, okay.
That's what we agree.
**Yusuf** 37:24 No, that's absolute.
**Robert Magnusson** 37:29 Okay, but that… that can come later, I mean, we don't have to have that…
**Yusuf** 37:34 Correct.
**Robert Magnusson** 37:35 Best to get… the Dart semantics, like this, merge first.
**Michael Bushe (Mindful Software, LLC)** 37:40 Right, right.
**Robert Magnusson** 37:44 Okay.
And… So we have, like, this manually created files that are not generated yet?
Sorry, if I take, like, yeah, I don't know. Okay, aha, these are actually coming from that generated, like, these are… Generated out of… the hotel… Demonic spec file by Weaver.
**Michael Bushe (Mindful Software, LLC)** 38:08 I don't know if they were generated in… that are in our API and copied over, or they're generated here? It sounded like they're just copied over, which is okay.
**Robert Magnusson** 38:18 And… and how… like, Weaver does that automatically, like, Weaver has built-in knowledge where those files are hosted, or, like, it's part of this specific… the script here, where you say, like.
**Michael Bushe (Mindful Software, LLC)** 38:27 It's in the scripts of where?
**Robert Magnusson** 38:29 Pick them from these and these repos. Okay.
**Michael Bushe (Mindful Software, LLC)** 38:32 Right, it should… it should have a URL here somewhere.
Registries… nope, nope, nope, What source? Yeah.
**Robert Magnusson** 38:50 Okay.
**Michael Bushe (Mindful Software, LLC)** 38:50 I believe our source, maybe it copied it from somewhere, but still, it should…
**Robert Magnusson** 38:55 I mean, we don't have to teepag this together.
investigate this myself, but okay, so then… then Weaver goes to these sources, locations, Takes all those… YAML specs… And then outputs in an output folder, we say here, example, all these files.
**Michael Bushe (Mindful Software, LLC)** 39:15 Right.
**Robert Magnusson** 39:16 And then, parallel to those, we also have our hard-coded, like, manual-typed Dart spec files.
**Michael Bushe (Mindful Software, LLC)** 39:22 We do not have any. We should never have any.
Oh, what's… what's candidates?
**Robert Magnusson** 39:33 Are they available from the client space?
**Michael Bushe (Mindful Software, LLC)** 39:35 I guess I'm wrong, those… I don't… these are not in any spec, right?
**Robert Magnusson** 39:40 This one not…
**Michael Bushe (Mindful Software, LLC)** 39:41 Start tight.
**Robert Magnusson** 39:42 predicted.
**Michael Bushe (Mindful Software, LLC)** 39:43 Oh, I guess… I guess they did this once upon a time.
**Robert Magnusson** 39:47 I mean, wait, I can, I can check, I mean, and it will be in the… API… no, in the…
**Michael Bushe (Mindful Software, LLC)** 39:55 Yeah, it's an API, let me look at the history there.
**Robert Magnusson** 39:57 Sorry, I just opened the repo, I have it here… No, that's just, That's the eastern.
**Michael Bushe (Mindful Software, LLC)** 40:26 Yep, yep.
**Robert Magnusson** 40:28 And these are manually… so these are the ones that are living instead.
And there is some con…
**Michael Bushe (Mindful Software, LLC)** 40:35 These are not manual, right?
**Robert Magnusson** 40:36 These are the generated ones, okay.
If I go in, I would see this generation thing, yes.
Makes sense.
But… These are… manual greater than, I guess.
Okay, but what's our goal here, then? We just want to… Get the generated ones.
In,
**Michael Bushe (Mindful Software, LLC)** 41:09 Right. So, I think our first goal should be generated ones as they are in the current API. Just to… you should… this is kind of a practice of… of our, sort of rip and remove, right? So we're going to rip this out, remove it, and then depend on this. This will be our first dependency. So we kind of just want to put out one quick release that says, hey, look, we've done this first step, and, you know, get any feedback. It should work, but who knows, right?
People may… people may go, oh, you broke me somehow, or whatever. And then, and then from there, let's make it better. We can regenerate from our… from the latest specification.
We can pull in Gen AI, we can pull in the new client ones, browser and whatever else is coming.
And start to make our Flutter ones, which I guess… Comes from these, candidates, huh?
Where do we get the candlets from?
**Robert Magnusson** 42:05 I mean, are they maybe just manually create, sorry, not there, here… I guess they're just, like, manually built, like, playing where it's playing?
**Michael Bushe (Mindful Software, LLC)** 42:19 These are from somewhere else. These are from client.
Or… because, like, AppJ… That's not ours. Believe it or not.
We, we, we got, we got little…
**Robert Magnusson** 42:28 2…
**Michael Bushe (Mindful Software, LLC)** 42:29 there's two things. They have Jenk, which we use liberally, and a UI component is called a widget.
**Robert Magnusson** 42:41 I mean, this looks… I mean, we have been building out Android Hotel also, and this seems very Android Hotel, like, these are the semantics they are using, I think.
**Michael Bushe (Mindful Software, LLC)** 42:51 Yeah, okay. Yeah, well, they could be common for the client.
**Robert Magnusson** 42:54 Please.
**Michael Bushe (Mindful Software, LLC)** 42:54 Maybe it came from them. Oh yeah, right, app widgets right there.
**Robert Magnusson** 43:01 Okay. And then, sorry, one more question, back to the… Oh, did I remove that on there.
But that would only be, like… if we get semantics, that would only be the semantics, right? So these other would not be impacted by that.
Like, they should not have anything.
**Michael Bushe (Mindful Software, LLC)** 43:17 Not… not yet.
Right, so, right, later, so we're gonna… we have to make sure, you know, the existing users are happy, and We'll take that, and then when we do the API, it will look like our API, because it will be depending on… at that point, the API will be depending on OpenTelemetry semantics. So when we move that in, OpenTelemetry API will be looking like OpenTelemetry semantics.
**Robert Magnusson** 43:45 Okay.
Can I ask a question to you, Yusuf? Like, you spray this PR? You said you're busy a bit in the next… I would like, personally, to learn a bit more about Weaver.
Would you mind me supporting you and trying this out, or offloading you if you have a lot of work to do?
**Yusuf** 44:05 Yeah, sure, I don't… I think I don't really need some help on this one if you want to get it faster.
Yep.
**Robert Magnusson** 44:18 Cool, because I think it'll be interesting to… yeah, sorry, Michael, go.
**Michael Bushe (Mindful Software, LLC)** 44:21 Thanks for all this work, Yusuf, this is really great.
**Robert Magnusson** 44:25 Yes, yes, definitely, thanks.
But then maybe we postpone this draft PR, like, leave it as is. I will also try to get into the topic, and we can focus on getting the folder structure merged, this other PR.
**Michael Bushe (Mindful Software, LLC)** 44:42 Oh, I think I didn't look at these other ones, because they were in draft 2. What's… is this still in draft 2?
**Robert Magnusson** 44:47 It was draft, we just changed it to ready for review.
**Michael Bushe (Mindful Software, LLC)** 44:50 Okay, great, great.
Yeah, I was gonna get rid of the awesome white.
**Robert Magnusson** 44:59 Yes, so we talked about that tonight.
I think so. So then, maybe, if you have time, you can take in the feedback here, and then we can get this merged, and then I can have support with the…
**Michael Bushe (Mindful Software, LLC)** 45:10 Yep.
**Robert Magnusson** 45:11 For the semantics things.
And then I think we're good for now in the hotel Dart repo.
Yup. And then the, in the… Dartastic. I'm not sure, Michael, what's your core focus there? There's not so many open PRs? Like, only two there. Is that another round of reviews, coming up that we should run, or…
**Michael Bushe (Mindful Software, LLC)** 45:31 So we… so I think we should be focused on the SDK now, and try to get… The… those bugs fixed.
That's the plan. Meanwhile, what I'll do, I think, Robert, you've already reviewed the updates to the AnyValue one?
**Robert Magnusson** 45:49 Yeah, I have one more round of feedback coming in.
So one more small round of feedback is coming after this meeting.
**Michael Bushe (Mindful Software, LLC)** 45:58 Okay, so I'll follow up with my review of that. So this weekend, I hope to get an OpenTelemetry repo, the directory stuff merged.
We can get the new API merged, it even released, and then, that'd be a good one to have. Well, no, hold on, let's hold off on that released, but let's… this is all we have in the… we only have 7 open ones?
Oh, that's good. Actually, hold on, yeah, that's not the bad part. The bad part is…
**Robert Magnusson** 46:29 Is it this issue? Is it this, issue cover, you mean?
**Michael Bushe (Mindful Software, LLC)** 46:32 Yeah, I'll take a look at those 7 and make sure I'm up to date. I'll do all that this week, and so then we should be able to… Robert, you've gave all your review on this, on these?
**Robert Magnusson** 46:41 No, so I also had a really… I thought I was gonna have it more next week, but we had a lot of… a lot of firing stuff.
At the company. I'm looking over this today, it's on my top priority for today, to give feedback on all of them.
**Michael Bushe (Mindful Software, LLC)** 46:54 Cool.
Yeah, I've been busy because I took Rafana out of Dartastic.
Okay.
**Robert Magnusson** 46:59 Oh, no!
**Michael Bushe (Mindful Software, LLC)** 47:00 So, Good. Alright, so we'll… so our plan, too, is we'll… we will review these, make sure that those get closed, then maybe, maybe what we could do is, if we can get the SEMCOM in… we can release any value… we could… we probably should do this as two… no, we should… I don't know, we should do it as two releases or one releases, probably two releases, we can release these seven as another SD… wait a minute, did we just release the SDK?
I'll take… I'll take a look and see if this is a significant chunk. Let's go back to the tracker.
**Robert Magnusson** 47:44 Alright, yeah, where is the tracker? It's an issue in…
**Michael Bushe (Mindful Software, LLC)** 47:47 It's up the top of the tracking…
**Robert Magnusson** 47:49 Aha, cool, I didn't know that.
**Michael Bushe (Mindful Software, LLC)** 47:51 Yeah, I like how it does that. It's automatic.
And what do we got here?
We should… let's finish off our P0s.
**Robert Magnusson** 48:02 Yes.
I think I have one open in a draft since a long time.
**Michael Bushe (Mindful Software, LLC)** 48:09 Oh, maybe some of these can be closed, because they're closed in the API already.
**Robert Magnusson** 48:16 Okay. I mean, we're over time now for this meeting if people have to drop, but…
**Michael Bushe (Mindful Software, LLC)** 48:20 Yep.
**Robert Magnusson** 48:22 Yes, I can also try to go over this.
Async and see if something is… Ready to be closed.
Cool.
**Michael Bushe (Mindful Software, LLC)** 48:35 then we'll keep working on that. So let's… let's, you know, we can… we can… this all doesn't need to be done at once, right? And so I think the idea… what the team is working on is right, let's focus on what we can get done for the OpenTelemetry repo.
we'll… we'll clean up that API once all… I could do the… another AI review now, but I'd rather just take this, close them all, and then we'll do another AI review with better models, hopefully, which seem to come every week.
**Robert Magnusson** 49:05 Yeah, yeah, Google has caught up also.
**Michael Bushe (Mindful Software, LLC)** 49:08 Right? Yeah, it looks that way. I can't wait to try that one.
**Robert Magnusson** 49:10 Okay, but that's a good plan then, so getting semantics in soonish on all Consumer Dart, and closing P0s in the SDK level. That's sort of our next, main priorities.
**Michael Bushe (Mindful Software, LLC)** 49:24 Sounds good to me. What do you guys think?
All right, sorry for being late, everybody.
**Robert Magnusson** 49:33 Blame time, blame winter.
**Michael Bushe (Mindful Software, LLC)** 49:35 Right?
**Robert Magnusson** 49:37 I was also surprised. That's also mine.
**Michael Bushe (Mindful Software, LLC)** 49:41 So, in America, we… all the time zones change their clocks back, so I wasn't thinking G… I was thinking GMT changed, but of course it doesn't. That would be really bad.
**Robert Magnusson** 49:51 Bye.
**Michael Bushe (Mindful Software, LLC)** 49:52 Okay, fellas, thank you.
**Robert Magnusson** 49:54 Thanks for your time, have a nice weekend, everyone.
**Michael Bushe (Mindful Software, LLC)** 49:57 week.
**Robert Magnusson** 49:58 And here's what I bought it.
**La Pyae Oo** 49:59 Thanks.
**Yusuf** 50:02 Alright, thank you. Take care, guys. Bye.
