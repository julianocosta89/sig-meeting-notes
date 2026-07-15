SIG: Specification SIG
Date: 2026-07-14
Duration: 64 minutes
============================================================

## Zoom Recording Transcript

**Armin (Dynatrace)** 02:18 That will you be presenting stable by default?
**Ted Young** 02:24 I don't have a big update, on that. What I would like to do next is start going to each individual, each, individual, group or SIG that… that owns some part of it and breaking it down into, like, actual roadmap pieces for that, but I've been pretty snowed under with… with other things, the past two weeks. So… Until I do that, I'm happy to, like, answer questions or, like, discuss things with people.
But to me, that's kind of the next step. It seems like, discussion has mostly died down, people in agreement that this looks like a good roadmap.
**Armin (Dynatrace)** 03:14 Okay, all right, but there's no, like, formal, update that you're… You're presenting today.
**Ted Young** 03:20 No, I think maybe my goal for this week on that will be to actually literally get that doc approved. Right now it's still sitting as like an open PR. So I'll try to get that merged this week and see if that flushes out.
Let's just add anything. So let me add that actually to the agenda.
**Armin (Dynatrace)** 03:40 It's a good point.
**Ted Young** 03:41 Please do a review of this from the perspective of it getting merged, and if… You are… Happy… Give it a check mark.
That would actually be a request, even if because it's a high-level roadmap, I would love to see appro… whether you have a green checkmark or not, you know, I would love to see approvals on this, just as a form of community buy-in. It'd be helpful to see maintainers and other people agree that this is great, or if you still think it needs work at this level, leave a comment on what you'd like to see.
**jberg** 04:28 Todd, I just sent a link in the chat and I just wanted to call your attention to this because Tigran left a comment.
three weeks ago on behalf of the TC on this that was sort of trying to sort through what the meaning is of approval and merging this because it's not the same as other sort of project proposals. It's a different type of thing. And you know, basically what we were looking for as a TC was like, hey, do you, Ted, are you aligned with like our interpretation of what the meaning is of approving and merging this. And, like, you know, go ahead and read that comment. If you can, like, you know, confirm on the issue that this matches your understanding, I think a lot of us would feel more comfortable approving.
**Ted Young** 05:14 Yeah, yes, I'll respond directly to him, but it does match Tigran's expectation, which is like the purpose, and this is… it feels like a gap in our structure that this is kind of getting… coming in as, like, a project doc, because it's higher level, and, like, this is where we'd like to figure out, you know, where we could add some more structure.
But, yeah, the idea is simply that we would like to then, as the next step, go make projects for each of the things in here, with the appropriate owner.
for that project. That, that's all it means. So if you see anything on this roadmap where you're like, that should be super deprioritized, that, that would be helpful. If you see something on here that's like, not in the weeds, but at a high level, I'm not sure what the scope is for this thing, or I'm concerned that the scope is too large.
for a section, let us know. But I think it's… I don't want to go into, like, detailed planning of each part of this roadmap in one document, because it's different owners for different parts, and I think they should have They should have the agency to figure that part out. And also, it'll be a novel.
**jberg** 06:37 Right, yeah. So like, you know, whereas on other project proposals, sometimes we get caught up in the weeds on things like staffing and project lead and stuff like that. That is not what approval means in the context of this PR. So like, I think a comment sort of confirming your understanding with Tigran would help in like pointing to the other reviewers, like I see Robert on there, I see Cijo on there, I see others on there, would help like everybody be the same page of what to review for and what not to review for.
**Ted Young** 07:06 Great, I'll leave a follow-up comment today.
clarifying all of that and asking for approvals on the PR itself.
**jberg** 07:15 Sounds good. Thanks.
**Armin (Dynatrace)** 07:22 Thank you.
Any other questions on that topic.
All right, then have a look at the PR, please. Link is in there.
agenda on the very top now. And next up is Evo with FRED context sharing.
Do you want to kick us off?
**Ivo Anjo** 07:48 Yes, so I, the regular… this is my, being annoying, regularly… regular message kind of thing, is like, I think we have a bunch of approvals, we've done another round of… like, replying to all feedback, so I think we're almost good to mark, like, I see a lot of the… we have the… a bunch of green checks, so… yes, let us… let me, us, whatever, the people working on this know if, there's more feedback that we can address, or if we can move on.
Maybe.
**carlosalberto** 08:23 Yeah, I think that Robert had some feedback, but he didn't confirm it's done.
And what I could recommend, based on the number of approvals, is that we wait a couple days.
And that's it, otherwise we merge, you know?
**Ivo Anjo** 08:38 Sounds good.
**jberg** 08:39 So, before we move on from this topic, so, like, you know, a good way to make sure that we don't just have this as a recurring topic on next week's spec meeting is to set some sort of conditions. So, there's approvals from three people that have merge rights.
Does any one of them want to take, take, you know, responsibility for merging if there's no additional feedback within a couple of days' time?
**carlosalberto** 09:03 Actually, I can do it myself. I wanted to. I wanted to do a last review. I did review this initially, and I did review the previous Pr. So we can do that.
**Reiley Yang** 09:15 Yeah, I'll follow up. I'll add a comment there, let people know that by default, I'll merge it by end of the week. If they see any blocking issue, they should block the PR and make comments.
**jberg** 09:25 Thank you, Riley.
**Armin (Dynatrace)** 09:29 So just to clarify, do we have any outstanding questions, any threats still? Because I looked at it briefly and I couldn't find any.
**Reiley Yang** 09:39 No, we don't.
**Ted Young** 09:41 Just a point of process, are there, are there prototypes in a couple different languages for this? I'm just curious whether enough maintainers have looked at it, and whether the spec works for their language.
**jberg** 09:56 So, yeah, just continuing the point of process, and I'm not sure we have clarity on this, at least it's not clear in my head. So, you know, we have a prototype requirement for, for spec PRs, like if you add a new in-development feature, OTEPs, you know, presumably we have a prototype requirement. There are prototypes, in a couple of languages that I've heard Ivo talk about in the past. Like, do we have a firm number on it? Like, in my head, my intuition says, like.
one prototype is enough for an OTAP, because it's even earlier stages than, you know, an in-development spec feature, right? So, like, as long as people agree with the concepts, if there's even, like, one prototype that's in place, that's enough.
And then, you know, obviously, you need more prototypes as you as you go up the maturity ladder towards ultimate stability.
**Ted Young** 10:51 That's kind of like, in the past, the way we've done it is to try to work everything out in the OTEP, and have then the… if the OTEP is pre… If the OTEP is approved, then the act of, like, actually putting it into the spec should be almost mechanical.
And not a place where we've, we're, we're rehashing the details, and we've asked for, like, like, three prototypes, usually, in a NOTEP. You know, usually it was something like Java Go, because Go usually is a bit different from the other languages. And then like JavaScript or Python or another dynamic language.
That's sort of how we treated OTEPs in the past. So that you don't approve a high-level concept without having figured out the details, and then you're halfway through merging spec PRs to get the details in, but still… trying to put together what exactly it is we're building. That was sort of where OTEPs came from originally, was to get around that issue.
**jberg** 12:02 I can think of a few instances where an OTAP was merged that had multiple years worth of work before anything happened.
Yeah, like, does anyone else want to chime in on this? I, like, you know, because they're, like, if we say something like, the OTEP is where the details are hashed out, and then promoting that from an OTEP to an in-development feature, and in-development to a stable feature is, like, sort of a formality.
you know, I have never seen that… I haven't seen that happen before, where people have, like, rubber-stamped the PR, taking it from, like, an OTEP to, you know, a spec something. I've always seen a ton of additional scrutiny, even. So, Yeah, like, at least on Carlos's recent context-scoped attributes, we had, you know, conversation that was to the tune of, like, hey, you know, this is directionally aligned, we still have some things we need to learn, let's merge this, and then, you know, clarify some of the finer points later.
Oh.
that was a recent example. I can't, like, you know, I'm not an encyclopedia of all the OTAPs ever.
**Ted Young** 13:10 We, you know, we could totally re… this could be something that we revisit, like, what… these days doing spec work, like, how… how do we want to improve our process around spec work? But I can't say, like, the whole reason we added OTEPs in the beginning, when you roll it back.
all the way, you know, to when we were working on tracing, was just this issue of, we would get high-level buy-in about doing something important, that was tricky to design. And… but then, in the process of, like, trying to actually implement it at the spec level.
having, like, a bunch of independent PRs, and, like, do they actually fit together? And, like, is this still making sense? Like, that became stressful, and we started to be like, it would be great to have the whole design in one place, in one dock.
Before we spread it out to the different parts of the spec where it would end up living, with some prototypes and everything. So the TC and everyone else can actually understand what it is they're saying yes to that. That was the motivation originally. Whether or not we still actually work that way, I agree, is up for debate.
Umm.
But, I can imagine there's certainly… some things we're trying to design that touch enough parts that we want to do it that way. And then there's maybe other things that are small enough in scope where it's actually… you know, doing an OTEP and then doing a spec PR just means having the same conversations, like, multiple times over, and it's just slowing us down.
**carlosalberto** 14:52 But you know, you know, there's a small problem that I saw. Well, it's not a problem. It's a situation that even if the tape has a design and you have different prototypes. Once this part reaches specification.
and languages start getting the beta, you know, or some preview for users, users may be pushing back, and then you have to change some of the stuff. So, it's not as mechanical, just putting it into the spec as we would like to.
**Ted Young** 15:17 Our whole thing in OpenTelemetry is, like, we have to figure out something that's coherent across a lot of languages and a lot of implementations, and the push and pull is that if you want to have a good design, you need to have a concentrated group of people thinking about it, right? Like a small group. And then, but then the wider community needs to then have their shot at giving it feedback. And they're not in that small group. And it's like, how do you run that process where it's like actually helpful versus just like rehashing the entire debate?
Three times over again, and it being like a dentistry.
Trying to get something, actually into the spec.
I don't think there's, like, any one perfect answer to that, but I feel like, in terms of open telemetry design process, like, dealing with that reality of, like, how do you… how do you get… End users, maintainers, everyone else, their chance to give feedback so that we build it right, but also have, like.
a concentrated group of people get all of the design information loaded up in their head so they can make decisions? Like, how do we do that?
I don't think there's, like, a perfect answer, but that's usually where… where we're struggling with our process.
Either we rushed it through and people didn't get a chance, or, like, we're having the same conversation 3 or 4 times over again.
Josh.
**Josh Suereth** 16:54 Yeah, so this is one thing I was looking into and I think it's funny. We don't follow our process. So if you read our process, it's lazy consensus, but we're entirely too nice to each other.
So, lazy consensus is supposed to be, if you don't comment with a blocking issue.
or respond to something that's resolved within, like, N amount of time.
the community makes a decision and moves on, right? So you have time to do that, and you have clear decision makers. But lazy consensuses of the maintainers, unless someone actively blocks it, the default is yes.
We treat the default as no.
And we, instead of lazy consensus, I feel like we have eager veto.
is more how I'd phrase it.
So, the only way I've seen lazy consensus work is if everyone knows that you're riding a train that's moving at 10,000 miles an hour, and so you don't get really upset that, like, people didn't wait for your opinion when you're busy and overloaded. And there's a risk that, like, you know, things can kind of rip apart if somebody pushes something through.
like, when people are on vacation, so you have to be careful, but, like, this is a cultural shift that we could try to enact if we wanted to actually use lazy consensus, where we actually tell people ahead of time, we mean it, you know? It's not like… we want everyone's opinion, we want people to be able to contribute, but we're gonna start putting a hard cap on our lazy consensus, and that hard cap means after N amount of time, if you haven't commented yet, we're going to approve it and move forward, because we need to do that.
But… As opposed to, you know, right now, I think we're very… And I think this is a good thing, OpenTelemetry is very accommod And I think that's good, and I don't want to lose that if we were to move quicker. But, I just want to call out that's an option. Like, we have a process, and we don't abide by it, and that's part of the issue.
**jberg** 18:49 So, I do that type of thing all the time, and sometimes in the spec, and especially in other repos, you know, where the stakes are lower, like, you know, I'm going to merge it on this date if somebody doesn't say anything.
And so… but, like, before you even get to that point, we still have merge requirements, which requires green checkboxes, so that sort of gets in the way of your lazy consensus, because, like.
you need at least 2 or 3 green checkboxes in the case of the specs. So somebody has to go out of their way, not to disagree, but to agree.
**Josh Suereth** 19:23 That's true, but look at, like, Evo's PR today.
that's… it's an OTEP, it's been approved, it's the design doc we're talking about. According to our process, unless there's a blocking comment on that, that should be merged today.
**jberg** 19:38 Right, and we're all fine with that. Like, you know… Yeah, good, yeah. Right, so no one's gonna take an issue with that. Like, you know, we're just saying one final call for comments. So, you know, it's just like, it took us a long time to get to this point with Evo's Right? Because we struggled to get those, those, you know, the, not just the, the lack of blocking comments, but the positive approvals.
**Josh Suereth** 20:00 That's fair, yeah, and I think that's also working as intended. If you can't attract enough attention for people to give you a green checkmark.
maybe you're not building something the community wants or needs to do right now, right? That's a sign of interest, if you will.
Okay.
**Ted Young** 20:14 There's also an attention economy, and this is a thing we've noticed over the years of, like, Overlapping, right, and socializing things properly helps a lot, like, it used to be, a group would go off in a corner, do a huge amount of, like, design work, get all the way to the end, and then come back and try to, like, get buy-in, and then you could really risk having, like, a lot of work thrown away. And I think we've gotten better about using forums like this one.
To sort of socialize things earlier, but I think we could always be in.
improving that.
So if we want things to not… to either get, feedback faster or get approvals faster.
You know, there's just so much stuff going on in the spec backlog. How do we focus our attention better as a community? You know, I would love ideas from people on how we could do that.
**jberg** 21:21 My idea is find small coalitions of like-minded people, get offline agreement with them, or, like, you know, online on issues, and, you know, get these group of people that all have approval rights, and say, hey, we're gonna do this this week, or this month.
get on board. And then, you know, you can move really fast when you have, like, you know, a couple of people with all approval rights working together. So form coalitions with each other.
**Ted Young** 21:46 But I so, for example, to take to take that to the next step, you know.
One group are spec maintainers.
you know, aka, you know, the TC, but, there's, like, lots of stuff in there that needs maintainer TC approval, and if there was a way to signal, like, if, let's say there's 15 design Proposals that need to be looked at, you know.
if the TC ordered… if there was some… a bit of, like, we're gonna look at these 5, then these 5, then these 5, is there a way to concentrate everybody's attention a bit more, and thus increase you know, decrease latency and increase throughput, because we're trying to work on 5 at a time instead of 15 all at once. I'm just spitballing here, but, like, is there a way to do that that would focus attention and let us move faster?
**jberg** 22:46 I don't know how long to take this conversation. I, of course, have thoughts. I have thoughts on everything, but This goes back, I think, to Josh Surratt's like, we're too nice to each other. So like, you know, PRs get opened and, you know, there's they may be open before there's consensus that we want to work on this topic. They get open anyways. And like what we might do if we had more rigid rules is just close them outright and just say, hey, look, we're this isn't a priority right now. We'll come back to this later. Maybe.
But we don't do that type of thing. Instead, we try to just leave them open, and they… They may just, you know, collect dust and atrophy and die a slow death.
**Ted Young** 23:24 Yes.
Diego?
**Diego** 23:29 Yeah, right, so… actually, we're ex… Oh.
Sorry.
Yeah, we are, thinking about doing the same thing, the exact same thing in Python. Put this, We're discussing about… or actually, I'm pushing for… This process that… Automatically closes any PR.
that is just opened. And the process is first, st you need to submit an issue.
And even if you submit a PR and there is an issue, if you are not the one assigned to that PR, you also get it closed.
Because, yeah, probably the same reasons you have.
So yeah, I don't think that's a bad idea.
Oh.
And it helps with… Keeping the process more in order and also avoiding people working on PRs.
that are gonna be rejected anyways.
**Ted Young** 24:37 Yeah.
I think this is an interesting conversation. Maybe we should get through the rest of the agenda, and then if there's time and people want to chew the fat on this, we could use the rest of the meeting time for that.
**Armin (Dynatrace)** 24:56 For now, we only have one more item, and that's Robert's. So should we do a quick detour into your topic, Robert?
**Pellared** 25:06 Please share. Do you want to share your screen or should I?
**Armin (Dynatrace)** 25:10 If you have it open, go ahead.
**Pellared** 25:13 I don't disclaimer.
**Armin (Dynatrace)** 25:15 Then let me open it up.
**Pellared** 25:17 Thanks.
Yeah, I saw I was absent last week.
And I saw the recording, and I saw some questions, Maybe you'll find… oh, yes, there, I'm sure So, it was about adding this new attribute for the depth limit.
So, I remember it was discussed without me, and there was basically a consensus for it.
I, one additional comment for it is that some serializers, like for JSON, I have not checked for Potaba.
would even fail if the depth would be too big, because I also remember that Tigran was worried about the size of the whole payload, but even if the payload will not be big, some languages will simply drop and fail if the depth limit is too large.
For .NET, it was the smallest that I have found, it was 64.
It's also adding, you know, additional, so it's not only the size, having something nested usually consumes more resources than just, you know, the memory size, because of the, like, recursive nature of, of, of processing.
And, I think I want to add one thing to this PR, which is for sure no blocking. I want to add to the compliance matrix, for the locks, for the locks, for locks and spans, because these are the only places we usually miss right now.
And here, I'm still waiting… Yeah, I'm still waiting for reviews, maybe approvals or not, just to make sure that nobody blocks it. I'm not inclined here. Instagram?
**Tigran Najaryan** 27:02 So I'm just looking at the prototype you created, Robert.
I was a bit surprised to see it's over 7,000 lines of code.
I wasn't expecting that, to be honest. I'm just wondering, can you provide a bit of color on why this turned out to be so large? My intuition was that it should be fairly simple.
**Pellared** 27:22 I think I was doing more things there. I think I was also making some performance improvements to remove keep allocations. That's one reason to make it efficient to not decrease the performance on the hot path. I was experimenting there a lot. That's one reason.
Second reason is that I was not cleaning up a lot of the code, I was just more concerned about, you know, having the performance on the whole tab, just making sure that it won't cause any issues. Third reason, it was very much code-assisted, you know, AI-assisted.
So, but I was reviewing the code to make sure each time to make sure that there's no, no, any bugs there. So there are probably a lot of junk in the tests and things like that. So that's probably also the reason why, why DPR is so big. And this prototype is not something that is going to be merged, not although for sure.
It will need… I remember that I was working on it. It will require a few PRs to go to this stage, because we already have some problems with implementation.
that, just adding this will just increase, quadratically, like, in a square meter, it will increase the HIPAA efficiency map correctly, so we need to just make some, we have some homework to do before that.
Which is, you know, something that we ignored previously.
**Tigran Najaryan** 28:46 Okay, so generally speaking, I was supportive of the feature. I would want maybe a bit more feedback from other maintainers of other SIGs.
To see whether it's going to be similarly.
complicated for them to do it in a performant way like you did.
**Pellared** 29:05 Okay.
**Tigran Najaryan** 29:05 Just trying to be cautious here.
I don't think it blocks it anyway, but…
**Pellared** 29:10 Okay.
**Tigran Najaryan** 29:11 Like I said, I was kind of a bit surprised to see that it's.
It's a lot more complicated than I was expecting it to be.
**Pellared** 29:19 I can say, I can share the same concern as you. I was also discussing this.
**Tigran Najaryan** 29:25 Yeah, yeah. Okay, maybe if you can tidy up the PR, like you said, if you can clean it up, remove the unnecessary bits, it will make it.
easier to.
To accept it. Anyway, no, no.
Not trying to block it in any way, but…
**Pellared** 29:41 Yeah, I'm still… I'm.
So I'm still waiting at this thing and also I have some other stuff to do concurrently. So probably I will get back to this like in two weeks or one week or something like that.
**Tigran Najaryan** 29:55 Yeah. Okay Maybe also do another language. Prototype would be would be helpful to see.
Maybe some other languages have it simpler.
**Tyler Yahn** 30:06 Yeah, I would just jump in there, Tigran. I think maybe Robert didn't quite mention that, like, they go… PR that he has is, like, touching Probably a lot more than what other languages probably have to touch.
I mean, this is jumping deep into the SDK and doing deduplications. We do a lot of repeated code as well.
A lot of it, what he's actually touching on is templates, which are then copied all over the place, so… There's a lot of, I think this is coming specifically from the Go code. If you go take a look at it in actual, like, earnest, like, there's not actually as much as being presented there.
**Tigran Najaryan** 30:47 So from what I see, some of it is actually generated code from templates.
**Tyler Yahn** 30:52 Yeah, that's what I'm…
**Tigran Najaryan** 30:53 Yeah, yeah.
Okay, sounds good.
**Pellared** 31:01 Carlos?
**carlosalberto** 31:02 Yeah, by the way, I just wanted to mention for everybody that this is not experimental, so I really would love maintainers to take a look. This is not like a typical thing that we want to try out.
So please take a look.
**jberg** 31:19 Oh, we're not marking this as experimental first. This is going straight to stable.
**Pellared** 31:24 Yes, I put some reasoning there that I think that can be considered as a bug.
In my opinion.
**jberg** 31:32 Oh, the fact that this doesn't exist today, it can be considered a bug.
**Pellared** 31:36 Yeah, that's my opinion, but you can disagree. I just thought that maybe, maybe there's a good motivation for it. I hope that I, I hope that I describe it for sure. I was thinking a lot about it.
Yeah, it's just.
**jberg** 31:50 I'm just gonna leave a comment on this PR, making sure that we give it, like, additional scrutiny given that we're gonna skip the the the experimental status. I do plan on reviewing this. I'm interested in this topic right now for, like, other reasons in Java. So, like, it's not gonna be, like, indefinite, but, yeah, maybe maybe another week or so. That that would be, like, plenty of time for me to, like, properly explore this and, you know, maybe even prototype it in Java.
Okay.
**Pellared** 32:16 That will be awesome. I see that it was the last bullet point in the notes that I might, that I'm adding you to this table.
**jberg** 32:24 All right, thank you.
**Pellared** 32:26 Thanks.
I think, Armin, we can go further. Thanks.
**Armin (Dynatrace)** 32:42 thanks all right that would be the last item so we can jump back to the otter process discussion.
**Ted Young** 32:50 Yeah.
So just out of curiosity, thinking about attention.
Just having a look at the spec backlog, In terms of PRs, there's 33 open pull requests, which is actually a pretty reasonable number, given the size of the project. And out of those, they're fairly fresh.
There's 5 that are… have been open for more than 6 months. I'm not saying there's… there's, like, good or bad, but in terms of, like, it feels like a relatively fresh backlog for something that's, like, spec work that might move kind of slow.
Then when we look at our issues, There's 625 open issues.
Just a quick count, 14 of them are seven years old.
But.
So, I find that… that's kind of interesting. Like… like, our pull request, backlog is… is, like, very tidy. Our issue backlog… Maybe has a pile of stuff in it.
That could be… could be laid to rest.
I know we've done a house cleaning on that in the past, but certainly, When it comes to focusing people's attention.
The cleaner the backlog is, the easier it is to understand what to be looking at.
I'm curious what other people think about that.
**jberg** 34:31 Look, when I look at the backlog, when I look at the issues in the spec you know, I see a variety of problems, but one of which is that it's, again, it comes back to this niceness thing. So we have, like, we have a large people of… a group of people that are, like, collective maintainers for the spec. There's the TC, plus some additional people. And, like, if I'm reading this, like, a spec issue, and I think, hey, like.
I get what you're saying, but I don't think we should do this. The best I can do is comment on this, and it, like.
I don't know, socially, it doesn't seem quite right for me to kind of go out of my way and close the issue as, like, won't do or something without getting more consensus from other maintainers that they agree with me, that, like, you know, we shouldn't work on this.
But getting that consensus on all of these issues is a high burden.
like getting consensus to close. So it's like, you know, that it's so it's an issue to, you know, for a large group of people to say like, Hey, we we think we shouldn't work on this. And it's an issue to, you know, just the, you know, the social issue of like closing something. You may basically rejecting the person is saying like, we won't do this. So I think those kind of turn into this inevitability of having, you know, 600 open issues.
Many of which are probably duplicates, many of which we'll never get to, many of which are, like, hopelessly outdated, but, you know, who's gonna do the work of, you know, scrubbing those and making sense of it?
**Ted Young** 36:10 Yes.
**Diego** 36:11 I'll do it.
I'll do the work.
**jberg** 36:16 Is that you, Diego?
**Ted Young** 36:20 I mean, one thing that's interesting, and again, I'm just, like, pawing through this, is, like, the first eight pages of issues haven't had anything touch… any update to them in… 5 years.
Or more?
So that's… that's, like, 8 pages of things I feel like we could just be, like… No one cares about this, we can just close it. Come back later if you care about this issue.
**carlosalberto** 36:55 Yeah, that's what I wanted to say. There are a lot of things that people would love to see, but nobody's investing in that and nobody has invested. So even if there are things that people really need, it's like it's not important enough. So, yeah.
**Ted Young** 37:12 Diego, you've got your hand up. I don't know if that's a new hand up or the same hand.
**carlosalberto** 37:18 But he forgot.
**Ted Young** 37:23 But I wonder if that's, like, some… maybe just, like… we should add more, you know, if we need more process, that's great. If we need more tooling, that's great. But, just one straightforward thing that comes out of this is, like, maybe just cleaning up the GitHub issues, on the spec repo would be a handy thing to do at this juncture.
One thing that's changed is we now have AI, and I know in the past we wanted to leave things open if we felt like it contained information we didn't want to lose, like context we didn't want to lose. And I feel like it's easier now to go back in time and find that context if you're trying to build up context around something.
Than it used to be.
Maybe we can be more aggressive about.
Closing things that no one has touched in, say, the last 3 or 4 years.
Just to… just to get the attention focused a little bit more.
**carlosalberto** 38:29 Diego, I think you are having some… Problem, so…
**Diego** 38:33 If I choose, yeah.
**Ted Young** 38:34 Just raising both hands now.
**Diego** 38:37 Yeah, my… my Wi-Fi just started dying, so I just had to switch to my cell phone and talk, so… I have missed everything you have said in the few minutes. So sorry if I'm going to mention something you already discussed.
the last thing I heard was Jack asking who's gonna do this, and I tried to offer. Okay, the reason why I'm… I was offering to do it is because I already did the same for Python.
So, not long ago, a few days ago, I pretty much told Claude, okay, take a look at every issue that's open in Python, and tell me what can be closed.
And it did a pretty good job.
And, we… I think we managed to… The club suggested about 30 or something issues. I reviewed each one of them by hand. It's much easier to review To do that, When there's an AI agent who has already done the first round of investigation for you.
So it's not that hard to waste it.
Claude does it, so I… I can do the same for… for the spec.
And yeah, I just posted a comment saying, close this issue. And I agree with Jack. The first time I did it, it didn't feel that nice as well, right?
Yeah, I'm sorry, am I just gonna tell this person?
We don't think… We should do this, or we don't think this is an issue, or we're not gonna do that, but At the end of the day, We're not being bad people, I think. We're just trying to move things forward.
**jberg** 40:25 Diego, I think one of the problems is, like, I close issues all the time in OpenTelemetry Java, because, like, I feel like I have a firm grasp over that entire domain. The spec Is is just so much scope, so many different domains that I think it's hard for any one person to claim, that like, hey, they have like expertise over enough of these to, to be able to definitively comment on an issue and like, close it as like, won't do.
There's ways to get around that, you know, to adopt, like, a sense of… like, hey, closing isn't a permanent thing, right? We're gonna close, and we're gonna aggressively close. If you think we got it wrong, we encourage you to reopen. I think that can help with this, but.
**Diego** 41:09 Yep.
Totally. The thing is that, I think when people take a look at the the.
600 or so issues.
it's, it already stops people from even trying, right? Because it just seems like too big a problem, so… What I did with Python was, just leaving comments there for maintainers. Okay, I think this issue can be closed, and then I brought that to the… to the SIG meeting. And many issues have been closed now that a maintainer took another look at it. And it's much easier when there's a human being, I think, already saying, hey, I have already taken a look at this.
And this can be closed, right? So I can… I offer… I can do that. I can give it a try. I can prepare a list for you with issues from cloud that I have also reviewed and I think can be closed.
And then it's easier. I can do that if you are agreeing.
All right.
**Trask Stalnaker** 42:27 Just wanted to share feedback from what has been working well, I think, in the Java instrumentation repo.
where we have a good number of issues, and it has been challenging to keep them under control over time, and just like a lot. There's just like so many. I mean, I feel like it's a little bit like the spec where there's just so many different things people could want, right? And so people open stuff, and then they… they sit… those issues sit there and clutter up over time.
And… I forget when, but maybe a year and a half ago, maybe 2 years ago, we started Trying to go back in this history here. We started just staling them. And I agreed — sorry, I just switched over from my phone, so I lost the Slack.
chat history, but I think Jack was saying close it directly rather than a staleness marker, which is what we're doing in the instrumentation repo.
Because it's not like, oh, we're going to mark it stale, and then somebody comes back and says, oh, this isn't stale. No, we just close it with a nice message that explains that this is not a permanent decision. It's just for keeping the backlog.
manageable.
**Daniel Dyla (Dynatrace)** 43:59 Something that Jack said, made me think that.
I think we don't have… clarity around the definition of what it means for an issue to be open or for an issue to be closed.
So, if an issue is open and 10 months old, Does that mean that We are planning on working on it? Does it mean nobody has looked at it? Or does it mean that It is in, like, the… it has suffered a silent death, where nobody is going to look at it, but nobody was comfortable closing it.
A couple of people have mentioned that closing issues is not permanent.
Unfortunately, in JS, we've found that, closing issues is permanent. Not because we are saying this is a permanent decision, but because it's so difficult to surface closed issues. And when people come to the repo and they look for issues, they typically don't look through closed ones, and it's not always clear why things were closed.
And, like, it's just… it does… Tend to be a fairly permanent decision, but so is letting it.
Sit in the, in the open issues.
triage list forever.
I think what we really need is, is… Some clarity and definition around what that actually means. And a difference between an open issue that we're never going to work on and one that we think is a good idea, but we don't have time for right now.
I guess what I'm… what I'm suggesting is maybe we have, like.
some single issue of, like, a tracking issue for, we're gonna close this for now, but it's not because we're rejecting it. We're gonna add it to some backlog list where it doesn't clutter up the entire issue pool of, we might get to this later.
But I would move towards a, I… a model where you have to… Jack mentioned earlier some… some small pool of people that have approval access that say, we're gonna work on this. I think it was Jack.
Maybe we move towards a model where that's kind of the default. If you go a week and you don't have some core group of people that say, this is a good idea and we're willing to work on it.
Something it goes into some backlog where it doesn't clutter up the issue list, but also isn't just closed.
And then that would free us to, one, close issues and move them over there, but then also to close issues and say, we're not doing this right now. I think we just need definitions for both of those states.
**Tigran Najaryan** 46:53 So I just took a quick sample of very old issues that I created, like six-year-old ones.
And they are very, very different.
Some are completely irrelevant.
and should be definitely closed. They are like, we record child counts.
On the… on the span, or something like that.
Some are… Not like that, they are still relevant.
There was no discussion on those, but they are still relevant, and we are… we have plans to work on those, because there were some recent discussions about those. Although, if you look at the issue, you're not going to see that, because the latest comments are still quite old, many years old.
And the third bucket is issues created six years ago, which had an active discussion almost every year. And there's even a recent discussion even this year. So we're planning to work on those. I don't think blindly closing all the issues is going to work.
There's very different types of fault issues. We need to be careful about what do we do about those.
**Trask Stalnaker** 48:05 Tigran, do you think, though, that, like, I mean, the issues that haven't then… Updated in a year, or let's say in the spec repo, we say even 2 years, like, say we say it's 2 years.
What… what's the harm in closing the… just auto-closing them? I mean, if somebody care… if somebody… If it's something that we're gonna work on.
Then people are going to make that happen when they have time and motivation to make it happen.
Like, it's… not the… The issues… like, the community doesn't work in this way of people submit issues, and then some other group works on them. It's sort of like somebody really needs to care about this issue. It needs to affect them personally. They need to be invested in that and put the time into that.
**Tigran Najaryan** 49:02 Yeah, no, I guess that's fine. We can do that as long as there is a clarity that it's okay to reopen.
if it still is relevant. So we shouldn't automatically assume that if it's old and nobody commented on it, it's not relevant anymore. It's okay, we… I don't mind if we close it, but we should make sure we don't discourage people From working on something just because it's an old issue.
I looked at the… there's one issue that was created in 2020 about remote SDK management.
And there was no comments on it since then. And it's something that we recently started working on, like this year or last year. Some of the languages began adding support for that. So… We shouldn't signal that this is… not relevant, and we don't want to work on it just by closing an issue. As long as we're clear about that, I think it's fine. We can close, we can then reopen if necessary, we can create a new one that is more properly described.
If needed, that's okay, I don't mind that. My comment was more about, let's make sure we don't say this is not relevant anymore, because it's old and nobody commented on it.
**Trask Stalnaker** 50:15 Yeah, I put into chat the specific comment we use in Java instrumentation.
To try to make that… I mean, I agree, it took some time to craft this message, because I had the same concern, right? Like, I want it to still be a friendly close, not like, no, this idea is terrible.
Which people will think if we say nothing or say it incorrectly.
**Tigran Najaryan** 50:40 Yeah, sounds good to me.
**Ted Young** 50:43 Yeah, and I think that I'm seeing this also in the chat, but like when closing.
if one of the reasons we wanted to keep an issue open is because it had relevant information in it. Like, often what issues have is, like, they have a statement of, like, a problem or an issue, right? Not just a solution. And usually we don't… we're reluctant… one reason we're reluctant to close things is because we don't want to lose that information, right? We don't want to say the problem you're experiencing, you know, isn't valid. It's more that, like.
we're probably not going to work on this anytime soon, in terms of proposing a solution. If there was just a tag to sort of help with, you know, AI-generated search To say that, you know, this contains, project feedback or a case study or something like that when we close it. That would be maybe another nice way of making it clear to the person who opened it that we aren't, you know, disrespecting their concern.
And it would also maybe… Help us, when it comes to new issues being opened, having some kind of tool that searches The closed backlog to see if there's relevant information hiding from years past.
That… something like that, right, to allow us to be more aggressive about closing these things, without feeling like we're losing useful information that we want to hold on to.
**jberg** 52:24 I just want to respond to that really quickly, because I heard you mention a comment like that before, and like.
This is… everyone knows this, but closing an issue does not erase the information.
We're all nodding along, okay. It might make it a little bit less intuitive to find, because when you're searching in the issues, you have to, like, search closed issues as well as open issues, but, like.
You know, I think people are gonna have to figure that out.
Because we're dealing with like the lesser of two evils here. Like, yeah, what's worse for us, like prematurely closing an issue that still might have merit that still might be worked on someday, or having an issue backlog of open issue backlog of 600, such that nobody reviews and responds to new issues, such that nobody dedupes issues such that like nobody, people don't even feel comfortable opening issues because they're just dropping their needle in the haystack.
So, like, you know, to me, there… it's not perfect, closing issues and trying to get a grapple on our backlog, but it's better than not doing it.
**Ted Young** 53:27 100%. And I really think of like all of the ways AI has actually been helpful, like research and information gathering.
is, like, at the top of that list. I think it's much easier today to go paw through that closed backlog to see if there's relevant information to any new topic somebody cares about. So, that should allow us to be more aggressive about feeling confident that we can close these things, and we're not we're not, binning it, you know, in the rubbish bin where it's gonna… we have to paw through 2,000 closed issues to see if there's something relevant, right? Like, that… that used to be more intimidating, I think, to us, and it doesn't feel intimidating at all anymore.
**jberg** 54:17 It still feels intimidating to have… a really big set of open issues for a maintainer, because, like, you know, I feel some sense of obligation to engage in them when new ones are opened, and I feel like I'm supposed to be doing something about the ones that exist, and there's so many, I can't do anything about it.
So like, what do we have to protect? The the the what do we want to protect more like the random contributor that is opening their first issue or like or the maintainers that are underwater. And I think both like nobody's unimportant. But, I, I think I've mentioned this before. I want to prioritize maintainers.
**Ted Young** 54:55 And just to be clear, I see you have your Haskell trends, but I was agreeing with that. I was saying, like, I think the closer we can get to the open issue being the project backlog, like, the fewer other tools we need, and I think we could be a lot more aggressive about it these days than we could in the past.
Sorry, Trask.
**Trask Stalnaker** 55:17 Yeah, I see issues as sort of like… I mean, people open issues, right? And they kind of, like… I don't feel, as a maintainer, I don't necessarily feel bad about not addressing, like, getting, doing something with them. I see them as a place people open issues, see if it gains traction among community or somebody who is motivated to work on it.
And then, you know, at some point, you know, that window sort of stales out. I'm like, okay, like, nobody really… it didn't catch on, that issue. And so it kind of goes out of the window.
But I really see… I don't see the maintainer's jobs necessarily, like… I mean, for bugs, and that's why, you know, let's say with, like, the Java instrumentation, staling out only applies to enhancements, because I do feel like bugs are, you know, something that maintainers should be at least, really looking at. But for enhancements, I'm like, there's, like, a bazillion enhancements that people could want, and… So, that, I do not feel is, like, something that maintainers are really responsible for. It's kind of just, okay, throw out all these ideas. If they Gain traction, somebody wants to work on it, that's awesome. If not, after some point in time, they stale out.
And if somebody is… if it's a good idea, and somebody wants to work on it, it's gonna come back.
**jberg** 56:53 So we got three minutes left.
I hope that this conversation, which, you know, people had different ideas, but I think there was a lot of nodding along to some common core of, you know, what people agreed with. And so, I would love it if we could turn that into something.
Maybe we don't solve the problem all at once, but maybe we can chip away at it with some things, like, some of the common parts that I didn't hear anybody disagree with were, you know, coming up With, like, you know, common conventions of what it means for an issue to be opened and closed.
a staleness policy for spec PRs with automation that closes things and with a comment that informs the users not familiar with our process with what it actually means for an issue to be closed.
You know, and is friendly about it and, and just, you know, it makes our, our process.
familiar to them. does anyone want to volunteer to to take a crack at some of these things.
**Diego** 58:00 Yeah, I want to.
**jberg** 58:02 Diego wants to… Thank you, Diego.
**Diego** 58:07 Oh.
**jberg** 58:07 So… Yeah, great. Does anybody disagree that we should do this? Because if not, like, I love it that, Diego, I love that you're volunteering. I don't think we have a formal issue about this and the spec. Maybe we should do it just for tracking purposes, but, you know, I certainly agree with it, so… them.
In the, in the, you know, in the spirit of lazy consensus, Joshua, unless you disagree, let's assume that we're going to do some of this stuff.
**Ted Young** 58:42 That's awesome. Yeah.
We can definitely use more process, but a spring cleaning on the issues would, I think, be a fantastic first step.
So, thanks for…
**Diego** 58:54 By the.
**Ted Young** 58:54 Keep it on, Die.
**Diego** 58:56 Oh yeah, by the way, I'm already running the, I already asked Claude, take a look at all these spec issues and tell me.
Welcome to Cloud. So, I'll report soon with whatever Cloud said, and… And then I'll manually take a look at The recommendations of cloud so that you know that a machine and a human being.
Took a look at it.
**jberg** 59:17 I appreciate your generous offering of tokens.
**Ted Young** 59:21 Yeah.
**jberg** 59:22 Can't imagine how many that's gonna consume to go through 600 issues in process, but, good luck. Let's wrap it up today. We're at the top of the hour, so, thanks all for the conversation. We'll see you next week.
**Armin (Dynatrace)** 59:36 Thanks, everyone. Bye.
