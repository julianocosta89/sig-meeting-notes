SIG: Python SIG
Date: 2026-02-19
Duration: 53 minutes
Zoom Recording URL: https://zoom.us/rec/share/ExKvT13PywD3VAkvB555LPy3uw_RFHil2UdVXwqD_Rp51VaLAvkPhQbhmA9NuSCm.xgra_aeAPR3ulBIJ
============================================================

## Zoom Recording Transcript

**Aaron Abbott** 02:07 Hello.
**Mike Goldsmith** 02:11 Hello, good morning.
Good afternoon, wherever you are.
**Aaron Abbott** 02:36 We've got a little shorter agenda than last week.
Sure.
We'll wait another few minutes for people to join, but, Yeah, please add your names to the attendees list, or add your topics if you got a chance.
Alright, can everyone see my screen?
**Mike Goldsmith** 04:04 Yep.
**Aaron Abbott** 04:05 Cool.
Alright, let's get into it. Mike, are you around?
**Mike Goldsmith** 04:13 Yeah, I'm here.
So I had a conversation in the Slack channel just to, sort of raise that, we've got quite a lot of open PRs, both on the core project and the Contrib project, and a lot of them are old, like, really old. Some of them have not had interactions for, like, 12 plus months, and I think that adds quite a lot of burden to… the people looking at reviews, because there's so many to look at, it's quite overwhelming, and then also, I think, from a contributor point of view, it's not a good look, because it looks as though that there's a lot of stuff there that's just not getting looked at. So I suggested to introduce something like a stalebot or something like that. The Java SDK uses a GitHub action to do that. You can then configure it how long it'll wait before it'll mark it as stale, and then another set amount of time after that, if there's no more indirections, it will automatically close it for you. They use 7 and 7, that's quite aggressive.
we could set it as 14 and 14, or something like that, just to sort of, like, give people a little bit more time, but I think something like that would definitely help, because… I think just trying to make the project more approachable for the people that will want to contribute either directly or through reviews, it would help to know what is active, what's meaningful. Yeah.
**Aaron Abbott** 05:27 Yeah, yeah, I hear you.
I think we were chatting on Slack about this.
**Mike Goldsmith** 05:31 Yes.
**Aaron Abbott** 05:32 Alright, Leighton, do we have you? We have Leighton around today? I know Ricardo's not here.
**lechen** 05:36 Hello.
**Aaron Abbott** 05:37 Oh, hey, Leighton. I think I'm personally open to this. I agree, 7 and 7 is very aggressive. I think we could, Scale that back a little, but, Ricardo seemed a little on the fence on Slack. I'm on board with it.
Leighton, it sounded like you were on board, but maybe… you know, we could just follow up on Slack, and then… Mike, if you're open, you could send a PR with a workflow like this?
**Mike Goldsmith** 06:02 Yep.
**lechen** 06:04 Yeah, yeah, we'll get back to you. Thanks. Thanks, Mike.
**Mike Goldsmith** 06:06 Yeah, yeah, no problem.
**Aaron Abbott** 06:08 Yeah, I also saw some thumbs ups, or hearts, was it?
**Mike Goldsmith** 06:13 Yeah. Yeah, I think people are interested in it, just to try and reduce the, like, the mental bandwidth of the project right now. There's quite a lot of… there's… I think there's, like, nearly 100 on the court, and, like, over 200… nearly 250 on Contrib, so there's a lot there.
**Aaron Abbott** 06:26 Yep.
**Liudmila Molkova** 06:27 we use it on semantic conventions, and I was going to introduce, to propose it to the Python seal, because it's… it helps tremendously to have a low number of PRs, even though it's not WS that it does.
**Aaron Abbott** 06:49 Okay, so let's… we think we could take the rest to Slack or to the PR, but yeah, if you don't mind sending a pull request like this one, and maybe… I don't know what… we could discuss the days, obviously, on the PR, but I think something a little less aggressive.
**Mike Goldsmith** 07:06 Yeah, yeah, I think other than, like, the… the number of days to still enclosed, I think everyone's pretty much in favor of just gonna tune those back a little bit, because it's not to be not as aggressive.
**Aaron Abbott** 07:16 Yep.
Okay, yeah, anybody… yeah, thank you.
Does anybody, like, hate this?
Okay.
Cool.
Alright, Redima, you're on?
**Ridhima Satam** 07:36 Yes, so this is just a tiny peer, not many changes in this. We added logging… log and metric support in the GenAI util, so LandChain now, uses that in its telemetry handler, so if you go in just… yeah, I have two approvals already from.
Keith and Pablo, thanks to them, but if you see in the init.py.
I've added most of the tests for the lan chain.
Text Purpose… Other than that, it's just adding metrics and log provider, yeah.
**Aaron Abbott** 08:12 Okay, So one… one thing… I think I had left a comment on another PR, I don't think it was your PR, Riva, but, Are there new test cases added here?
**Ridhima Satam** 08:25 Yes.
**Aaron Abbott** 08:26 There are.
like, mmm…
**Ridhima Satam** 08:30 So for, say, log and metrics, what would be the expected.
**Aaron Abbott** 08:34 Yeah.
**Ridhima Satam** 08:34 telemetry for that, that's been checked in here, like, in perspective of Langchain.
**Aaron Abbott** 08:40 Okay.
Yeah, no, looks good, I can take a look.
Or just merge it, since we've got approvals already. Yeah, the only thing I would say is sometimes.
with these VCR tests we have.
If you just, you know, slap, like, the PyTest fixture, the perimeterized fixture on there.
You get a lot of really similar… VCR cassette files, and I'm guessing that, for the most part, these are, like, identical, or, like, it doesn't matter what the… what the value from the LLM was, they're just different variants based on the instrumentation. So, I can… I can leave a review, but it should be possible to kind of minimize that, and I just think it generates, like, a lot of noise on the PR, and in later PRs, so if we can minimize that, it'd be good. But otherwise, yeah, awesome, thank you.
**Ridhima Satam** 09:29 Okay, thanks.
**Aaron Abbott** 09:34 Cool.
Next one, Mike, again.
**Mike Goldsmith** 09:40 Yeah, just to, get some of it more, people interested, see if anyone else is interested in it. So we've got, the OpenTelemetry, declarative… that word's so hard for me. Declarative configuration.
And we've implemented it in Go, JavaScript, and Java so far, and I've started the process of doing it for Python. So I've been working with Alex, who does this original one, but I think this is in a place where we can actually get people to look at it, and maybe this is the first step. So this is taking the… JSON schema from the configuration, and then generating the models files that we can then use to configure the SDK with.
there was a little bit of back and forth around the use of the union operator, because it's not supported on 3.9, but I think we've got it in a good place now, so I just wanted to… raise it for people to have a look at it and see if they're interested in having a look at it as well. And then, once this is done, then there'll be more work on it to, you know, configure the different providers and the different propagators and resource attributes and all of that sort of stuff.
**Aaron Abbott** 10:43 Okay. Awesome, so you're pushing to… you and Alex are working together on this one, basically?
**Mike Goldsmith** 10:48 Yeah, that's right, yeah. So I've been helping out on the other ones, and I'm gonna try and drive this one on the Python side, too.
**Aaron Abbott** 10:54 Okay.
Awesome, and so this, this is generated, for example, this file here.
**Mike Goldsmith** 10:58 Yeah, so the main file is a generated one based on the scheme, and then outside of the generated file, there's not an awful lot of changes for this file, for this PR.
**Aaron Abbott** 11:07 How is… how is it generated? Sorry, I can… I can review as well.
Bye.
**Mike Goldsmith** 11:12 So we've introduced a tool called Data Model CodeGen, and then based off this, the JSON schema version, it then generates this file.
**Aaron Abbott** 11:20 Is the, generation, like, script checked into the repo?
**Mike Goldsmith** 11:24 It is, yes. Yeah, so it's in the PyProject TOML and the TOX file that shows you how it's configured, and what version of the file it's going to retrieve from the config repo, and then we've got a script that does a tiny bit of cleanup for, so it is compatible with 3.9 because of a type alias, import.
**Aaron Abbott** 11:44 Yeah, yeah.
Okay, yeah, this is awesome. So, I mean, I can dig into this, but, Is this tool specific? Like, because there's obviously generic JSON schema generators. Is this, like, a specific one with specific templates for OTEL?
**Mike Goldsmith** 12:01 No, so it's… this is a generic tool, but uses our custom… our specific JSON schema.
**Aaron Abbott** 12:07 Okay.
Awesome. I'm not, like, super… I know that in this space, there's usually, like, you know, 5 to 10 options per language, but I'm not super… up to speed on those, but I… it sounds like you did your due diligence. Was there any, like, trade-offs or anything you wanted to discuss?
**Mike Goldsmith** 12:24 No, I don't think so. I think the only one that really is worth mentioning is that this tool is… particularly wants to target 310+, because of the way that the union operator works. It doesn't… and that's why we had to make that custom, like, post-generation script that'll then do that type alias import for us.
Outside of that, it seems pretty good, and I haven't had any other issues with it.
**Aaron Abbott** 12:47 Alright, awesome, and then I guess once we drop 3-9, we could just remove that hack.
**Mike Goldsmith** 12:52 Correct, and then we could drop the post-processing script too, and introduce… the generation has a… as an option to use, to better use the union, and optional. So once we go to 310+, we can then turn that feature back on, and then the generation will be a bit better, too.
**Aaron Abbott** 13:10 Awesome.
Alright, well, thanks for working on this, and this is just the models, and then we'll have the config separate, so…
**Mike Goldsmith** 13:16 That's right, yeah, so this doesn't do anything other than model generation yet, and then the next one will be introducing, like, the base SDK configuration, and then setting up the SDK, and then start introducing the different providers and so on.
**Aaron Abbott** 13:29 Lucas?
**Lukas** 13:30 just submitting a PR to that… to the actual JSON code generator repo to fix the union… operator issue. Did we… Or, maybe I'm deceiving.
**Mike Goldsmith** 13:47 I'm sorry, I'm finding it difficult that you're a little bit distorted.
**Aaron Abbott** 13:50 Yeah, your mic's not great, Lucas.
**Lukas** 13:53 Is this better?
**Mike Goldsmith** 13:55 Yes.
**Lukas** 13:56 Yeah, I was just saying, I think I've looked at, I've reviewed this PR, and I think there was discussions of just submitting a PR to the that JSON schema code generator library to fix the union operator issue.
**Mike Goldsmith** 14:12 Okay.
**Lukas** 14:13 I don't know, like, to me, that seems like maybe a better approach than to writing the post-processing script, even though it will be temporary once we drop 3.9.
**Mike Goldsmith** 14:23 Yeah, we can look at doing that, I don't remember seeing a comment in the PR based around that, though, so is it… maybe, is it… are you using that tool in a different project?
**Lukas** 14:36 Sorry, maybe I was mistaken, but… Yeah, I think… yeah, that'd be my only comment, is that maybe it would be worth just, like, submitting a PR to the… to the library itself, rather than… writing our own post-processing script, but yeah, I mean, if we're gonna drop 3.9 in a few months anyways, maybe it's fine.
**Mike Goldsmith** 14:58 Yeah, yeah, I was gonna say the same, like, I think we've only got a few more months left with that we really want to keep 3.9, so maybe it's… Yeah, it's a temporary fix either way.
**Lukas** 15:10 Yeah, that was my only comment.
**Mike Goldsmith** 15:12 Okay, thank you.
**Aaron Abbott** 15:14 Yeah, great work, this is awesome.
I'm inclined to approve, but if anybody else, can take a look and review, I think we can… Merge, this looks pretty good, and we're in, like, a new… we're in a private namespace here, so… Yeah. You can always work on this iteratively.
**Mike Goldsmith** 15:31 Yes.
**Aaron Abbott** 15:33 Alright.
Thanks, Mike.
**Mike Goldsmith** 15:37 Yep.
**Aaron Abbott** 15:37 Anything else here?
**Mike Goldsmith** 15:39 No, that's it, that's great, thank you.
**Aaron Abbott** 15:40 Yep.
Alright, Emilio?
**Emídio** 15:43 Hey, just share that, Python 3.14PR for Contrib is ready to review.
I added all the truth classifiers, so PR is a bit big at this moment, but most of these changes are related to the… By project.tum files.
So, just need, like, one more review, and I think you are good to… to merge.
**Aaron Abbott** 16:09 Yeah, yeah, looks good. Maybe we'll get one more review I can… Annoy people… oops, yeah.
With that. Otherwise, anything else here?
**Emídio** 16:21 Nope.
**Aaron Abbott** 16:24 Cool. And then I think, yeah, I'll just… I think every time this one comes up, I say the same thing, but we talked about, adding tests for the free threading Python at some point. I know, like, that's not in scope for this one, but…
**Emídio** 16:38 Yeah, we should… we can add it later, like, we added for core.
**Aaron Abbott** 16:43 Yeah.
**Emídio** 16:43 But, yeah.
**Aaron Abbott** 16:44 We did, awesome.
**Emídio** 16:46 Yeah, it's running.
For free trade, yeah, I can create an issue for the contrib1.
**Aaron Abbott** 16:54 Yeah.
Okay, cool. Let's see if we can get one more review, and then we can, merge this in, maybe for the next release.
**Emídio** 17:03 Awesome, thank you.
**Aaron Abbott** 17:05 Thank you.
Alright, shuning, Shunning? Sorry if I'm butchering your name, you're around?
**Shuning Chen** 17:14 Yeah, yeah.
Thanks. I'm Shoonin, so I'm from, Splunk, so… I have, I actually have this, embedding type, and a spam creation PR, it's still work in progress, but, it should be ready within this week, just don't want to, push it until next week. So, this PR contains, this is my first PR, so it, needs some, detailed, modification based on the, later pipeline running, and, basically, I'm adding, embedding invocation type in the types file, and add a basic embedding type lifecycle.
Start embedding, stop embedding and fail, embedding supports and adding some, UTL methods in the UTLs.
file.
So, yeah, it will be, ready for review within this week.
**Aaron Abbott** 18:21 Okay.
Awesome. I think… so just a couple things, like, one would be if there's an issue, you could link here, it'd be useful just for context, and you can link to, like, the… Sorry, the semantic conventions.
that we're implementing here.
And also, you can always just leave, like, if you're not ready for a review, you can leave something in draft.
You can always put it back in draft if you want, but… Yeah.
**Shuning Chen** 18:50 Yeah, yeah, sure.
**Aaron Abbott** 18:51 Yeah, yeah, yeah, no problem. And one other thing was, the CLA, do you think you can sign the CLA, or is there any issue there?
**Shuning Chen** 19:00 Yeah, I will, sign it.
**Aaron Abbott** 19:05 Okay.
Awesome, yeah, thanks for… thanks for contributing, always good to have new contributors.
is, Is this embedding thing, is this already in the semantic conventions, or is it kind of a prototype of a work-in-progress convention?
**Shuning Chen** 19:21 it's… it's already in the semantic convention, so the current attributes I have added, It's already following the semantic conventions.
**Aaron Abbott** 19:31 Cool.
Well, awesome, looking forward to Yeah, looking forward, just let us know when it's ready for review. Actually, I might put it in draft for now, and then you can, there's a button You can do to convert it out if you didn't know, but yeah.
**Shuning Chen** 19:46 Oh, okay.
**Aaron Abbott** 19:48 Cool. Anything else on this one?
**Shuning Chen** 19:51 I'm good for now, yeah, thank you.
**Aaron Abbott** 19:57 Alright, awesome.
Josh, you're on?
**Josh Winerman** 20:03 Yeah, hey, Aaron. I just wanted to… I might have missed something, but I wanted to see if there was any traction on the conversation that we had last week, specifically, maybe regarding triageers or more reviewers. Is there any… Internal discussion or any clarification there?
**Aaron Abbott** 20:24 So… I don't think… I didn't take any steps to make this happen yet.
**Josh Winerman** 20:28 Okay.
**Aaron Abbott** 20:29 Can you just remind me, did we, like, agree? Like, I'm open to this, did we have an agreement on the SIG call last week?
**Josh Winerman** 20:35 No, I don't think we exactly had anything, I just wanted to bring it up again. Liam Miller, you're here too today, I can see. So if you wanted to express anything… I know Ricardo's not here, so it might be a little harder, too, though. But since you weren't a part of the conversation, last week, was there anything… Specifically, you had in mind regarding more reviews and the notes we took there?
**Liudmila Molkova** 20:57 Yeah, we… I think we need to figure out what to do here. We had some conversation on the… you've been there on the GenAI call on Tuesday, right?
But my thoughts… it doesn't mean that, it, it's… some… we don't need to take yours. I want to invest myself into the testing infrastructure, so we have, like, the unit test helpers, we have a life check. You're interested in triagers. Can… can you help me understand what What do we want to do here with three edgers?
**Josh Winerman** 21:32 I think, well, triagers in general, it's not just a GenAI issue, it seems like there were a lot of PRs that maybe could be redirected around, that's something that… I've been involved a little with another maintainer from another group, and he mentioned that triageers would be more helpful to streamline work to maintainers and reviewers, per se.
Which would just be the thought implicitly with triagers, if I'm being honest. But nothing's… either that or, like, Ricardo and Aaron, you might have mentioned, more reviewers as, approvers, per se, either or. I was just wondering if there was any, you know, thought.
**Liudmila Molkova** 22:15 Yeah, I… so what you're saying, We need someone to… to notice when there is a PR, And it needs… they need to… bring this PR… make sure this PR is triaged. Essentially, we need to establish some triage process for PRs, and the triageer would be the person who in this case, maybe creates this process, and also, makes… makes it happen. It does not guarantee any review, per se, or… but the treasure tries its best to organize the people around this.
**Josh Winerman** 22:55 Yeah, I'm not sure if we would think triagers had a green checkmark either or. I'm fine with either or, like you mentioned, but I think it would just help streamline work a little more. But Tammy, go ahead.
**Tammy Baylis** 23:09 Hi, yeah, I don't have a solution, but I just wanted to point out, this GitHub project board that I linked in the chat, and it's… it's kind of, at least from my point of view, become like a casual triage board.
And it's not just for GenAI, it's for all the Python SDK and CONTRIP PRs, and when PRs are created right now, they're not on this board, but whenever I see one.
come into my inbox, like, I might do a quick review and put it in ready for review, i.e, like, get other approvers and maintainers to have a look. Or if it's, like, an easy one, like a changelog or a typo fix, I'll put it in easy to review, and then… when they get to the last column on the right side, approved PRs, I think that's when the maintainers, decide to pull the trigger and merge the PRs. So… Yeah, I… I don't think this is perfect, but this is kind of… an informal triage process that we're doing right now, and it could definitely be improved upon to help with the Gen AI, PRs.
**Mike Goldsmith** 24:22 I think it'd be nice to add new issues or PRs directly to this board, so we don't have to go through that manual process of adding them.
**Emídio** 24:32 Yeah, I would say, like, in OpenStormetry.io SIG, like, the localization one, they have a lot of triggers approvers for every language, like.
Portuguese, Japan, etc, etc. And they are doing that by just assigning labels to the PRs, and they have, like, separated board for each one.
And the board gets, populated by the label.
So, I think it's a good example of having a lot of groups, and two Azure approvers and maintainers for each localization.
**Mike Goldsmith** 25:11 No.
**Aaron Abbott** 25:13 Yeah, so maybe if we were a little more diligent with, like, component owners and code owners for, like, even individual parts, so say, like, this person's a metrics expert, this person's, like, a logs expert, or whatever.
**Emídio** 25:25 Hmm.
**Aaron Abbott** 25:26 A bit easier to have accountability for… You know, who's gonna triage the issues, and… Talk about them.
**Emídio** 25:32 Yeah. The thing is, is that, like, the people want, like, the green tick, they need to get through the membership process.
Yes.
**Aaron Abbott** 25:41 Yeah, I was gonna share this, actually, so I… when you said triage art at first, I was thinking… I was thinking mostly about this, so there's, like, a formal… definition in hotel governance for, like, these roles. So, you know, triager… these are, I think, kind of in order. So, like, anybody can become a member after a couple of contributions and sponsorship, and then you could be made triager, and etc, etc. So, like, mechanically, this gives you access to You know, add labels, close issues, stuff like that.
Which… which we don't have, to be… to be completely clear. So, if people think this would be… helpful. I mean, I… I think it could, but I've seen usually this ends up being the same as the approver group.
But maybe if we… if we're more diligent about, Sub-owners in different… Categories, and at least we have somebody on the hook, and it's not strictly tied to these roles.
**Josh Winerman** 26:40 Tammy, could I ask… or, sorry, Lou Milla, could I ask for your… your feedback regarding, especially because this is something you're involved… you mentioned, you take it up on yourself to do this sort of right now. Do you think a triager would be helpful in this context, or would you rather just do it yourself?
**Tammy Baylis** 26:59 Yeah, Yeah, I… I'm happy to keep doing it, but I don't really have, like, a set schedule. It's just, for me, it's a whatever-I-can type basis.
I… the triager role would be great to fill, but yeah, I… through my years participating with the Python SIG, I find the biggest challenge is, like, people staying and people committing, because, there are quite a few people I've seen here, like, since I have started, but there's, you know, people who don't come back, or people who come in new, and which is awesome. So… I can commit to this, like, if I could be, like, the official triager, I think I'd be happy to help. I just have to check with, like, my company, Well, that could be a start, yeah.
What are others' thoughts?
**Aaron Abbott** 27:58 I mean, that sounds awesome. I think… I think that would be really cool. We could also, like, add a time slot at the beginning of the meeting if you want to do that, so, like, you know, it's not… it's not something that you have to spend as much time on. I think we did that for a while, and I think people hated it.
I was droning on about, like, going through the issue backlog. We had, like, a 10-minute time box at the end of each sig or something like that, or the beginning. But we do this in, like, Gen AI. I think if you do it every week, it usually takes less than 5 minutes, so I think… If you want to run that, Tammy, that would be awesome, and we could do this board, just go over it for 5 minutes at the beginning of each meeting.
**Tammy Baylis** 28:39 Okay, sure, I'll, I'll give that a try for next week.
**Aaron Abbott** 28:44 Yeah, no one likes… no one likes this stuff, so…
**Liudmila Molkova** 28:49 I'm curious, folks, so currently, because of this high number of PRs that are… most of them are out of date.
it's kind of overwhelming to understand, but how do you folks feel? Do we need a separate board for GenAI, or should we use this board and the same, should it be the same everything with the Python contract in general?
**Mike Goldsmith** 29:18 I think I would like to see what it would look like if we just tried to use one board, once we've got rid of all of the older stuff that we're not gonna want. If it still becomes… Challenging to look after, because the frequency, because it's so busy right now compared to other activities, then maybe we could create a separate board just for that.
**Liudmila Molkova** 29:39 Okay, so start here. Let's NC.
And then, essentially, what Aaron raised, that there are two possibilities. We can introduce a triage or role.
And then we could also… Just use the existing approver roll.
Yeah, Judge, go ahead.
**Josh Winerman** 30:09 Yeah, my last comment on this, I didn't want to throw Tammy under the bus and, put all that responsibility on her, but, either or, it was like, would you want that responsibility to… is it easy enough to just keep within the approvers, or, would you want… that time back, and just delegate it to another, like, an actual triager, per se. Or we can, like Lou and Millen mentioned, just keep it in the approvers, either or. I didn't mean to, to put that responsibility on you, but, thank you.
**Tammy Baylis** 30:42 Yeah, no problem, Josh. I'm happy to drive progress. In terms of groups, I… I don't know, I don't have an opinion. Aaron, do you want to formalize this with the groups now, or maybe wait and see?
**Aaron Abbott** 30:59 We can always wait and see. I mean… Maybe, like, also a quick show of hands, like, is there anybody here who's already… Pull that page back up.
Is there anybody here who's already, like, a member?
And wants to be a triager, but they're not an approver already?
Is that you, Josh?
**Josh Winerman** 31:29 Yeah, I mean, I wouldn't mind doing it myself, you know, or just looking to contribute.
**Aaron Abbott** 31:34 Okay.
**Mike Goldsmith** 31:35 I'm the same, I'd be happy to be a triager.
**Aaron Abbott** 31:39 Okay.
I mean, we'd also be super happy to, you know, make y'all approvers after you know, after a little time, like, obviously I can't make the decision on my own, but… That's what I usually see happen, is people who are diligent enough to triage, review stuff, send issues, you know, they usually can pretty quickly become approvers also, but… Yeah, that's… that's a fair point.
Somebody had their hand raised, I think. Maybe it went down.
**Lukas** 32:07 Well, I was just saying, I could be a triage… I'm already a prover in the contrib, but not the Python, so I could be a triager for Python.
**Aaron Abbott** 32:15 Okay.
**Lukas** 32:16 Nice to carry both.
**Aaron Abbott** 32:17 Yeah, fair points. Okay, let me, loop back with, Ricardo. I'll chat on Slack.
Leighton, do you… sorry to put you on the spot if you're still here, do you… what do you think?
**lechen** 32:32 Yeah, I'm okay with, everyone volunteering to be a triager. I think that'd be greatly appreciated. Thank you.
**Aaron Abbott** 32:41 Okay, cool.
Alright.
with Noah.
Here.
**Liudmila Molkova** 32:53 Yeah, I'm in this work position, we just talked about how many PRs and how hard it is to find ice.
on the PR, but here I am.
Asking for another round of reviews here. It's changing OpenAI V2 to the new version of semantic conventions, behind the feature flag.
And it uses hotels whenever possible.
There was some feedback. It's all incorporated, and it's ready for, I hope the final round.
Thanks, Josh, for your comments.
**Aaron Abbott** 33:34 Yeah, any of the reviewers around had anything to say about this one? I haven't taken a look yet, but… Oi.
Yeah, let's just get more eyes on it and merge. Thanks.
**Liudmila Molkova** 33:58 Thank you.
**Aaron Abbott** 34:03 Alright, thanks, Josh. Cool. So this last one's from Ricardo, who's not here. I have some context on this. I can talk about this one.
Alright.
Actually, Lucas, I don't know if you want to talk about this one. This is you, right?
**Lukas** 34:20 Yeah, I mean, this is pretty straightforward, it's just adding the… the random trace ID based on the trace context spec.
I'm not sure what he… what did Ricardo say he wanted to… Oh, this is with the ID generator, right?
**Aaron Abbott** 34:34 Yeah.
**Lukas** 34:35 Yeah, so I just added… I modified the IV generator ABC to have… this, you know, is trace ID random and just default to false for backwards compatibility, but any ID generators that do it, adhere to the random trace ID spec, they can just override this to return true, and then that flag will be populated.
**Aaron Abbott** 34:57 Okay.
**Lukas** 34:58 So, I don't see this as, like, really any risk, because even if you… you know, if you… if you don't override this method, this just will be false, and that's just the existing behavior anyways. But, for the… I have updated the SDK generator, and then there's also a… Aws… X-ray generator, that also adheres to the specs, so I've updated that in the contrib as well, so… I guess, like, if there's any other custom IT-generated implementations.
It might be a good idea to override this and make… and have the implementation return true, but…
**Aaron Abbott** 35:42 Yes, yes. Is anyone on the call who implement… who, has their own ID generator, like, either in Contrib or out of source?
Anyone from AWS around?
**Lukas** 35:58 We've tried to get in contact with AWS, and, like, it's just been silence for months.
Unfortunately.
**Aaron Abbott** 36:06 Yeah.
Yeah, I hear you. Are… is there a component owner of… the… sorry, the AWS ID generator in Contrib.
**Lukas** 36:22 There might be, but no one has… it's pretty much… if you go… you can look at the PR, and…
**Aaron Abbott** 36:30 Pull it up.
**Lukas** 36:31 I don't think… I think, I mean, I know, I know I've been pretty active on contributing to a lot of the AWS related stuff, particularly AWS Lambda, but, I'm not sure who else…
**Aaron Abbott** 36:51 This one, right?
**Lukas** 36:52 Yeah.
**Aaron Abbott** 36:54 Yeah.
**Lukas** 36:56 Yeah, you can see some close comments from Ricardo. We were trying to reach out to a few people.
Yeah.
**Aaron Abbott** 37:03 Yeah.
**Lukas** 37:04 But this, that was, like, almost 2 months ago.
**Aaron Abbott** 37:06 Okay, yeah, this has been kind of a problem before. Maybe we can, I think we have some folks, not necessarily from AWS, but from Like, not, not from, I guess CloudWatch or X-Ray, but from OpenSearch that joined the GenAI calls, so maybe they can… help us get in touch. I think it's Annie, I can put you guys in touch on Slack.
But yeah, I think… I think what you said is… is fine, like…
**Lukas** 37:35 I mean, yeah, to be fair, like, it's… in my opinion, it's such a minor change that… and it's a non-breaking change.
Well, actually, well, I did a… Yeah, I mean, yeah, it's definitely worth, like, an extra set of eyes on, but it is… it is a very straightforward change.
**Aaron Abbott** 37:55 Yep.
Okay, yeah, my only other comment on this was, like, yeah, for people who, This does change the default, in a sense, for the default implementation, which is this one, so…
**Lukas** 38:05 Yeah. But the default implementation does adhere to the spec.
**Aaron Abbott** 38:11 Yeah, I think we're gonna find out who's, not doing their fit masking correctly. So I actually shared this around internally to make sure that people…
**Lukas** 38:20 Yeah, I had to update all… if you go to the contribier, I had to update a bunch of tests, because…
**Aaron Abbott** 38:25 Oh my gosh.
**Lukas** 38:26 They were hard to put in the trace flags to just be, like, 0 or 1.
**Aaron Abbott** 38:29 That's pretty funny.
Yeah. Yeah, there's, like, this diatribe, I think, in the W3C spec about making sure you do it correctly.
**Lukas** 38:37 So it's kind of funny to see this come full circle. But yeah, maybe just a PSA to everybody here.
**Aaron Abbott** 38:45 Okay.
Cool, looks good to me, Any other comments on this one?
Intel Ricardo.
**Lukas** 38:55 No, yeah, nothing from my end.
**Aaron Abbott** 38:57 Yeah.
Okay, cool. This… this was the other one from Ricardo. Sorry, not this one.
This one.
I think this is mostly for me, I need to take a look at these, but these move the OTel Python, like, standard library logging handler out of the SDK.
Which… Yeah, it breaks auto instrumentation if you don't have the separate instrumentation installed.
And we can work around it, so… Yeah, I think Ricardo wanted to get these in for this release, so… Yeah, maybe we could just give some early feedback. I'll take a look at it offline.
And it's like, Obi?
Cool, Surya? Yup, you're on.
**Surya Teja** 39:59 Yeah, hi, sorry, I joined pretty late. So, these, these three need some eyes, and I want some approvals, but just seeing if anything more is needed, for merging them or not.
**Aaron Abbott** 40:17 Okay.
I think I… are these the three that I commented on?
**Surya Teja** 40:22 Yeah.
**Aaron Abbott** 40:24 Okay.
Was there anything outstanding on any of them? Like, this one I see.
**Surya Teja** 40:31 Yeah, I did not, resolve them because I was waiting for your feedback on them.
So.
**Aaron Abbott** 40:39 Yeah, so, I mean, let's chat about this name.
**Surya Teja** 40:42 Yeah.
**Aaron Abbott** 40:45 Look, I don't have any context on this at all, so I kind of defer to you. It's just something that's hard to change after the fact, so…
**Surya Teja** 40:54 Yeah, so I was thinking of, I… a little bit of time to reflect on it, and I felt that, having Cloud Agent SDK will, suit better for this one instead of Anthropic Agents, because, the library name in GitHub, and a lot of people use it as Claude Agent SDK.
So, if we use Anthropic agents, it's going to create a lot of confusion, so I thought Cloud Agents SDK did a better job, rather than using Anthropic agents. Initially, the reason was I saw OpenAI Agents V2, and I went with that, but since you'll… asked me that question, I started thinking more, and I felt that using the library name makes better.
**Aaron Abbott** 41:43 Yep, yeah, I agree, actually. I think that's good. I'm gonna resolve these comments, and… Yeah, I think this one was good then, I just need to make sure I reserve the name on PyPi.
Yeah. We can merge this one.
Yeah, thanks for the review, Mike. Awesome.
Cool.
So this… was this one of the other ones?
**Surya Teja** 42:04 Yeah.
it's around adding the, instrumentation around OpenAI's Responses API.
So… This is for the first method, which is going to, add instrumentation around responses.create.
**Aaron Abbott** 42:23 With streaming enabled and non-streaming one.
Cool?
Yeah, another look. I think that comment I left was… Probably the only thing.
**Surya Teja** 42:36 Yeah, I have… I found out a few specific things, like, say, the retrievals, the operation name retrieval is still not available in OTL semantic conventions, so there is a retrieve function inside, the responses API.
Initially, that was part of this PR, but Ridhima pointed out that whatever attributes that I was using for spans were not aligning with what we had, so I went ahead and did a little bit of digging, and I found out that semantic conventions was not having the retrieval operation name. Only chat, and a few others were there, so…
**Liudmila Molkova** 43:15 When you're saying this, do you mean the Python semantic conventions, or the semantic conventions?
**Surya Teja** 43:21 Python semantic conventions that we use for assigning the enum values and everything, right, for the operation, that was not available.
**Liudmila Molkova** 43:30 It's not available because we didn't release it yet, we are releasing semantic conventions. Today, it should become available, but I think it makes sense to add it as a next step anyway, because you… you already have the PR, and it's already pretty big enough, and it can be added later.
**Surya Teja** 43:47 Yeah, yeah, I was planning to add it in the next PRs when I was doing my… when I… when I'll be adding, but yeah.
**Liudmila Molkova** 43:56 Thank you. I will review this PR today. This one, I promise. I cannot promise Anthropic Whale or played, because I'm…
**Surya Teja** 44:04 Yeah.
**Liudmila Molkova** 44:04 more for Brighton folks, and I love the context.
**Surya Teja** 44:07 Yeah, the Anthropic, agents, boilerplate, I have a draft for the design. I want to pro… show that in the next week's SIG meeting. So it's not containing any code, it's just the boilerplate with jobs and everything.
**Aaron Abbott** 44:21 Yeah, I can… I can probably merge that one in today. It looked good.
Okay, and then, there was this last one.
**Surya Teja** 44:31 Yes, Aaron.
**Aaron Abbott** 44:33 That's.
**Surya Teja** 44:35 around, the same, it's… The previous one was the Responses API. This is for the Messages API for Anthropic.
So, it deals with the same thing, where I add instrumentation around the create method.
For both non-streaming and streaming one.
Mike already took a look at this, and he suggested a few good changes. I did the changes, and You had some comments, I, I replied back, I did not resolve them, just to get your, Opinion back.
**Aaron Abbott** 45:09 Hmm, okay.
I might have to absorb this comment, but I think… I think we should be able to avoid this.
Minky… But yeah, maybe, actually, if you don't mind just explaining.
**Surya Teja** 45:30 Yeah, one minute, let me pull up that.
So yeah, the way I wrote this test is, you were asking about why would the casets be missing, right?
So, the way I wrote this test was I was using, an API which supports both tool use and thinking tests, but sometimes if users are using an API which is not having the tool use and thinking tests, in those cases, the tests are going to fail.
So… I just added this card just to prevent some confusion over there.
Thinking that local testing can be opinionated in a little way to tell them.
**Aaron Abbott** 46:24 Okay, but if… Like, if you, you're saying if users use… But, like, the testing setup, is it required?
**Surya Teja** 46:32 No, no, not users, actually. The other developers, say someone pushes a change, or making a change to this, and it's not related, their change, they might be using an old SDK, and, say they run this test suit on their local, it might break, because the SDK will not support Tool changes or thinking tests.
So, just to avoid confusion when others are, using an old SDK, I wrote this one, but I can remove this if it is inappropriate.
**Aaron Abbott** 47:04 Okay, I got you. I think it would be better to, so what we usually do is we have a lock file for the oldest supported version and the newest supported version.
And, yeah, again, like, our tooling is kind of crap here, because… There's not great… like, tools… like, UV doesn't really support this well, so you have to kind of handhold it a little bit. I can point you to some examples, but… What happened is that every developer would get the same dependency versions, and we'd just have whatever's supported for the test.
**Surya Teja** 47:33 Yeah, yeah, yeah, makes sense. If you can give me some documentation or any old implementations, I can read through that and make the changes.
**Aaron Abbott** 47:46 Okay, yeah, I'll, I'll comment on that right after the call.
Alright, everybody else?
**Surya Teja** 47:53 Yeah, cool. Thanks.
**Aaron Abbott** 47:56 Cool.
**Liudmila Molkova** 47:59 I have a somewhat related question to folks.
So we… there is a lot of logic in the… for the streaming that's not in the OTIOs.
And it's kinda hard to… Have it unified.
Did anybody try? Did anybody look into making the stream wrappers?
generic?
Sounds like no.
**Surya Teja** 48:37 Are you asking me regarding the stream wrappers and the responses wrappers that I'm writing?
Ludmila.
**Liudmila Molkova** 48:45 It's not to you, it's to everyone, and it's not about your pull request, it's just for the future.
**Surya Teja** 48:50 Hmm.
**Liudmila Molkova** 48:51 if we… if there is any opportunity to unify those. It's probably hard, but is there?
**Aaron Abbott** 48:59 Bye.
**Surya Teja** 49:00 Yeah.
**Aaron Abbott** 49:01 Oh, sorry, go ahead, go ahead.
**Surya Teja** 49:02 I'm not well-versed with that, well-versed with the fundamentals of, to the nitty-gritties of Python, but in Java, we usually create, an abstraction, and we use that abstract class everywhere.
I was thinking of the same pattern in Python over here. Once we formalize all the implementations, I can do a refactor on top of this to unify them by using an abstract class kind of thing, and using it in all the places, but I have to dig more deeper to unify that, if that is what you're asking me, and… If whatever I'm speaking makes sense to you.
**Liudmila Molkova** 49:39 Yeah, it makes sense, it's just, it's not specific to Entropic. We have the same code in OpenAI, and I'm.
**Surya Teja** 49:45 Yeah, yeah.
**Liudmila Molkova** 49:45 other places.
**Surya Teja** 49:46 Yeah, I want to do it for all, because the responses as well as the messages have the same structure. They, if you read the code base also, they have the same, coding standards, because they're using some Steely or something to generate the code. So it's code generation. So we can… we can make it one… abstract class or something to formalize everything and use it everywhere.
**Liudmila Molkova** 50:11 Yeah, that would be an interesting exercise to see, like, how far we can go and how much benefit it brings, because if it's just the base class, then there's no implementation shared, then it's probably not worth it. I don't know.
**Aaron Abbott** 50:25 Yeah, I mean, my two cents is… We should probably be able to make this work.
Also, this is Python, so we can do… all sorts of crazy stuff, but, like, maybe we shouldn't. But yeah, I think in most cases, like, you know, we have abstract-based classes in Python for iterators, async iterators, etc, so…
**Surya Teja** 50:45 Yeah. It should be.
**Aaron Abbott** 50:46 Possible to satisfy whatever requirements, if it's, like, a wrapper.
And yeah, I think, based on, like, what I've seen in the Google instrumentations we have, I think It should be feasible, you know, there's, like, some weird cases where if… The… the thing that's returned is… has extra methods that aren't in the abstract base class, you have to do… we can use, like, wrapped.
Which we're already doing in a bunch of places, but that will basically automatically proxy calls to unknown methods through to, like, the implementation that's being wrapped.
Like the, huh?
**Liudmila Molkova** 51:26 That would be great, because it would help keep everything, at least provide some, some baseline. I was thinking more about the buffering, right? Buffering of the messages and reconstruction. This is probably specific.
But maybe there are some gains to be made there anyway.
**Aaron Abbott** 51:45 Yes, I can show… One thing that I did for Vertex, actually.
Let me see if I can find it quickly.
**Surya Teja** 51:57 Yeah, I don't know, on side note, can you send, those also in any of the PRs? I would love to formalize this and, create one base class or something, so that we can reuse that when I'm adding instrumentations for other methods.
**Aaron Abbott** 52:14 You mean, like, just the sample codes from other instrumentations?
**Surya Teja** 52:17 Yeah, yeah.
Or any places that you can point me to, that would be helpful.
**Aaron Abbott** 52:23 Yeah.
Yep.
So I think I'm trying to… you know, it's always hard when you look at code that you wrote a while ago, but I think basically what I do is we… we have this context manager, so you can wrap everything in this, and then… you can, It yields this function, which does the buffering for the streamed events.
this… this is the old code… sorry. I could just… I can just send it offline, but Bayside, I think it should be possible, At least to cover most of them, we might need some custom code for… Weird ones, or whatever, but yeah.
Cool.
Alright, I think that was the end of our agenda.
Yep.
Yeah, good job, everyone. Thanks for joining.
I'll follow up on the stuff I said right now.
See y'all next week.
**Liudmila Molkova** 53:30 Thank you.
**Emídio** 53:31 Thank you, bye-bye.
