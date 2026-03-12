SIG: Technical Committee
Date: 2025-06-18
Duration: 41 minutes
============================================================

## Zoom Recording Transcript

**Reiley Yang** 00:22 Well, tiger.
**Tigran Najaryan** 00:23 Hey, Rodney, how are you?
**Reiley Yang** 00:26 Hey? Good! Thanks! How are you?
**Tigran Najaryan** 00:29 Good, good.
**Jack Berg** 01:56 I do. Gruen. Hi, Riley.
**Reiley Yang** 02:00 Hey! Jack!
**Tigran Najaryan** 02:02 Hello!
This. This is going to be a quiet day, I guess.
Just the 3 of us.
**Jack Berg** 02:14 Could be. I know we had a a private topic that we were considering talking about last week.
But if we don't have quorum. And and Josh Sereth, who mentioned that he's not gonna be able to attend this week's meeting. Maybe we should punt on that till next week.
**Tigran Najaryan** 02:35 Okay, I just check the inboxes. They are empty. There's nothing to do there.
and I don't see anything in on the agenda at all.
**Jack Berg** 02:56 Thanks for that.
**Reiley Yang** 03:00 Have a quick update or question. So have you tried the co-pilot coding agent? The idea is, you assign the issue to the bot. The bot will just send Pr.
And if Ci. Field, the bot will try to fix it. So I try to enable it for couple repositories, and now I think the only blocking issue is easy. Cla, from the Linux Foundation is blocking the bot. Cla is saying this bot hadn't signed off the CIA part, so I already reached out to Linux Foundation, and normally they would get back in 2 days. So I think it'll be as simple as what they have been doing for the Github dependent bot and renovate bot. So they just add that, like the new coding agent to their allowed list. So I would expect that problem to be solved, and then it should start to work. And I want to have more folks give a try and see if there's any concern before I enable it for the entire org.
**Tigran Najaryan** 04:03 Yeah.
I think it's worth trying. Have you? Have you had experience actually using it on? Is it doing a reasonably good job.
**Reiley Yang** 04:14 Yeah, it's doing an awesome job. I I almost feel like from my experience, like 80% of the time.
It's a, it's like doing better job than average intern.
**Tigran Najaryan** 04:27 That's not not a very high bar, Riley.
**Reiley Yang** 04:31 But we have relatively high bar for interns and the interns like we we like, we.
We find smart people there.
**Tigran Najaryan** 04:40 Okay, no, that's cool. Okay, maybe. Yeah, definitely, definitely, we should try. Let's see how it does. I'm curious. I'm using some copilot stuff internally.
I mean most of the time. I'm not very impressed. Let's say it this way. Sometimes it does useful things, sometimes.
**Reiley Yang** 05:01 Yeah, it's not doing expert job so definitely not going to replace experts. And sometimes it will just give you some fake answer. And it seems to be very confident, but if you sound like tricks when you give the prompt like, like, you only do this. If you have high confidence, then it'll change the behavior.
**Tigran Najaryan** 05:21 Yeah.
**Reiley Yang** 05:21 Another thing is depending on which model you're using, the behavior could be very different.
**Tigran Najaryan** 05:27 Right, right.
**Reiley Yang** 05:28 Like. Some are like very conservative, like the open AI model seems to be conservative, and it gives you a lot of questions just to confirm things well, like Sonnet 4 is more aggressive. It will just go and do something and and wish that you could help to crack it or something. So it's more like aggressive developer versus like program manager versus conservative developers.
**Tigran Najaryan** 05:52 Yeah, yeah. Well, yeah, definitely, I'm I'm curious to try it a bit more to me. I guess the the minimum bar is there. Do I need to spend more time fixing the problems we've introduced?
Then I would spend time myself doing everything on my own right. If it saves me time. I I'm yes, I I of course I will use it. Why not?
**Reiley Yang** 06:14 It is saving, saving my time a lot.
**Tigran Najaryan** 06:17 Yeah.
**Reiley Yang** 06:17 The miller.
**Liudmila Molkova** 06:19 Yeah. So one of the things we are discussing in semantic conventions that they would like to experiment with is, it's actually as good as the prompt you give it, and you can give a reprovite prompts through copilot instructions. You can say, Okay, follow the styling guide and you can give it some additional encouragement to do stuff. But essentially you, you need to give it some guidance through the compiler instructions, and I would love this. But that. Well, actually, the reviewer to review naming, for example, it doesn't need a human being to review naming policy.
or improve wording. So the the reviewer is super useful. The agent it's getting there.
**Reiley Yang** 07:11 Do? Do you already have it enabled or not.
**Liudmila Molkova** 07:14 Not yet. I'm just thinking about it.
**Reiley Yang** 07:17 I can't have that enabled. So the the only blocking issue is, Ed is not allowing the commit from the bot because the bot is not in the Ed allowed list. I already reached out, so I expect them to like, get back in 2 days and fix that problem. But if you just want like review comments or something instead of merge. You're totally fine.
**Tigran Najaryan** 07:39 Yeah.
but the review should be already possible to do right. So I kind of enabled it on one of my internal repositories, not public github but splunk repositories. And you ask a review, it does it?
Okay? Not a great job. Not not very impressed, but maybe better than nothing, I guess.
**Reiley Yang** 07:59 Yeah, absolutely.
**Liudmila Molkova** 07:59 I think it's it's a good 1st I. The thing that we will miss everywhere is the copied instructions, and every repo owner would be, would need to define their own repo policy. And maybe we needed some pilot Repo to actually write this instructions and share with others.
**Tigran Najaryan** 08:21 Yeah, yeah.
**Reiley Yang** 08:22 Yeah. So I already talked to like 3 repo maintainers and have couple repos have that enabled. So talk with the on the Gctc. Channel. And if you think semantic convention has some additional thing that we didn't cover, you want to try. We can have that enabled oh, oh, cool like before, before pushing that to the entire org.
**Liudmila Molkova** 08:44 And if you want to enable and semantic conventions, I wouldn't mind. Armin is also here. I don't know. Maybe Armin has some other thoughts.
and I I can in parallel work on the instructions, so we can avoid the whole story together.
**Reiley Yang** 09:02 Yeah, also, like memory bank. And those things start to see. It's probably like a a good habit just to have a shared memory bank and then individual developers. They can add task, specific thing on their workspace.
**Tigran Najaryan** 09:20 If you, if you enable that on any of your repositories and and and see that it works well, maybe if you can capture some notes about how to do it. The best way would be great, right? So we can recommend the same way to some other other things to to use it.
**Reiley Yang** 09:38 Yeah, yeah. So my, my thing is like, we, we 1st try to enable it for a couple of repositories and make sure like things can work. I I think we're we're almost there. I just need to unblock the Ucla part. Then we'll see how people are using it and share the knowledge back to the community and see if there's any concern. If not, we'll have that enabled for the entire project.
**Tigran Najaryan** 10:03 Okay.
sounds good.
So what do we have for today, Jack? You said there was supposed to be a private topic. But since Josh is not here, we should postpone it.
**Jack Berg** 10:30 Yeah, I think so.
**Tigran Najaryan** 10:31 Is there anything else that we had for today.
**Jack Berg** 10:57 I don't think so. Sounds like sounds like no.
**Liudmila Molkova** 11:02 To Josh. Suggested. We talk about next steps on Tc. Charter rotation, so we can try to brainstorm without him.
We can call it a day.
**Jack Berg** 11:18 Has the Tc charter been updated? Did that?
do we? Do we need to update the charter and the community repository to formalize those rotations or
**Liudmila Molkova** 11:30 Let's see.
**Tigran Najaryan** 11:32 Alright does it have to be? This is this is between us. Right?
Do we need that to be like written down explicitly in the community repositories.
**Jack Berg** 11:44 No, that that's fine. I just I guess. What I I meant to say is.
there's been a lot of different topics that have spawned from this Tc Charter discussion and the The rotations are one of them, and you know, I guess.
are we all on the same page with what the rotation.
**Tigran Najaryan** 12:05 What did we agree to in the end? Right? What's the I guess the final all that. Do you guys have the link to the to the doc that Josh wrote that- that the everything about rotations is there right.
**Jack Berg** 12:19 I can pull it up.
Here we go. I'm gonna send it in the chat.
**Tigran Najaryan** 12:26 I guess. No, no harm. We could put it in the in Github as well like to make sure that it kind of is approved as goes through the approval process. Everybody's on board. Maybe we could do that.
Yeah, this is a large documentary.
You're right, Jack. It's it's a bit hard to tell the one exact. Which part did we already agree to, and which part we? We haven't yet.
**Jack Berg** 12:58 If I can share my screen, though. There's a section that's specifically about responsibilities or rotations that I think lead. Mela is referring to.
This is in the 1st draft tab, and it's somewhere down here.
So what do we got? We got the security rotation specification rotation request rotation.
**Tigran Najaryan** 13:27 So. Wh, what are the mechanics of this going to look like, are we just how do we keep track of the the rotations? Is it some sort of what? What do we do? Do we use Google Calendar for that?
Any tooling to help us to to stay on track here.
**Liudmila Molkova** 13:45 We can probably use Github. We can, I don't know, make a bot, create an issue, assign it to a specific person.
Weekly.
This would integrate with the existing stuff easily.
**Tigran Najaryan** 14:06 So we have stuff here that is weekly monthly.
It's either weekday or monthly. From what I understand right.
**Liudmila Molkova** 14:19 Or on demand.
**Tigran Najaryan** 14:20 Or on demand. Yeah. So for on demand, I mean, it's on demand, obviously. But for for stuff that is, that has some periodic cadence. I think some sort of yeah tooling to just just to remind right? So that we don't forget who is who is doing, who's on duty essentially.
**Liudmila Molkova** 14:40 So there are 2 weekly things, security and communications.
**Jack Berg** 14:52 So.
**Tigran Najaryan** 14:53 Are we? So what do we do about the communication? Since we're recording this? Now, that's no longer needed. Right? We're not taking meeting notes anymore, manually or not. No, not posting summaries, at least.
**Liudmila Molkova** 15:05 Alright!
**Jack Berg** 15:05 That's right. That's right. We we stopped doing that a couple of months ago. So I've I've crossed that out this. That's out of context. Now.
**Tigran Najaryan** 15:12 Right and note taking, do we still need that cause? We have this recordings that can be transcribed if necessary?
**Jack Berg** 15:20 Oh!
**Tigran Najaryan** 15:21 Let me know!
**Jack Berg** 15:22 It's it's dubious. But you know, I think, like all meetings, they're all recorded. And yet we try to do note taking to to some extent.
you know, we've talked about this before you. We we should try to rely less on synchronous meetings to get stuff done and try to record decisions and conversations on Github issues and Prs when possible. To the. So to the extent that we're discussing anything that has a public issue or Pr, we should record the notes directly on there. But maybe there's still some minimal note taking. We can do.
**Tigran Najaryan** 15:59 I'm in.
**Liudmila Molkova** 16:00 This is where I would shine. We don't need a human really to do this.
**Tigran Najaryan** 16:07 We don't need. What sorry can you say that again?
**Liudmila Molkova** 16:09 We don't really, really need a human being to record.
**Tigran Najaryan** 16:14 Right, right, exactly.
**Liudmila Molkova** 16:15 Meeting. We can have an AI doing it.
**Tigran Najaryan** 16:17 Yeah, that's that's what I was saying. Yes, yeah.
**Jack Berg** 16:20 Do. Do you all want to cross that bridge right now? Like is that do it like we? We've we've been operating for like 5 years, and most of the meetings still, you know, rely on somebody manually recording meeting notes, or you know, and there's varying degrees of success based on the Sig, you know.
I feel like.
**Tigran Najaryan** 16:41 All that, Jack. Is there a value in doing that? Like, if like, you said, if it's if it's something important, there's likely an issue. There's a Pr, there's some. There's some sort of a record somewhere else, definitely right?
**Armin (Dynatrace)** 16:56 Okay.
**Tigran Najaryan** 16:57 Go ahead!
**Armin (Dynatrace)** 16:57 I think that the very minimal note taking like, I don't know. It's 5 lines per Tc meeting, or something like that that we have been doing lately, I think, is a good compromise. There's a minimal note that gives the today, for example, 4 absent Tc. Members catching up afterwards some hint on where to look for, or what to to ask for, if they need details without taking up a lot of time to to jot it down.
So I think that that makes for a good minimal compromise, that there's some hints of what has been discussed, and one can ask about it or follow links, and only if they need the full picture, they can resort to watching the recording or asking an AI that will render a quick response of unknown quality.
**Tigran Najaryan** 17:51 So it's for us. Essentially, it's for our own use for us to maybe go back to. What did we talk about last weekend? Is there a continuing discussion necessary.
**Armin (Dynatrace)** 18:01 And for the absent and for the absent Tc. Members. For every who's interested. They they have the recording for the for the full picture and for full accountability. But the very short, concise hints, I think, are for Tc. Members, mainly.
**Tigran Najaryan** 18:19 Okay, makes sense. Yeah, thank you.
You know, unless we we start using the AI for that, right?
**Jack Berg** 18:30 I I mean, I think this is a perfect use case for AI so like don't take me the wrong way. But we've been discussing Tc. Responsibilities for months now, and to the extent that we can, I'd like to put a put a bow around these topics and move on like have conclusions about them, and then, you know, iterate from there. And so just I I feel like this could become a a bit of a rabbit hole where, you know, it's a it's a simple thing that we need to do. And we we.
we use this as a a way to kind of try to transform all of our note, taking about all of our meetings for the entire project.
which I'd rather not do.
But if somebody wants to do that like. Set up that automation and broach that that subject, you know. There's been some cold feet about AI and open telemetry. That's the sentiment that I've been picking up in in various meetings. People don't want bots in the meetings, transcribing everything and this seems kind of like an extension of that. So
**Liudmila Molkova** 19:36 And if we have a central note taking that, people would not need this thing.
and it will save us and every maintainer something. But they agree. We don't need to boil the ocean and decide here now how we'll do it, for the whole project.
**Jack Berg** 19:55 That'd be. That'd be amazing if that we had that centralized tooling.
**Liudmila Molkova** 20:01 There is a donation proposal on this. But yeah, let's probably move on. I think, yeah, it's not the key discussion here.
**Jack Berg** 20:12 So let's just quickly get on the same page about the other rotations. So the security rotation. This is essentially what Armin has been doing the specification rotation running the spec sig that's presumably being the person that shares their screen and organizes the the call. That's what Carlos has mostly been doing for a number of years. And you know, releasing the specification. Carlos has also been doing that releasing the protocol. We've been doing that ad hoc, and that's been driven by a variety of people mostly, whichever person is most interested in getting their changes released and then request rotation. So performing Tc. Approvals. What does this mean?
Oh, this is about one data due diligence. So whenever a language Sig is trying to cut a stable release and then donation reviews. This is an interesting one, so on demand and.
**Tigran Najaryan** 21:24 On demand. Right? Yeah, that's an on demand.
**Jack Berg** 21:28 It's it's on demand, and it doesn't rotate in the typical sense. I don't think because it's not necessarily appropriate to go just round Robin. You want the person that's most appropriate to do the job.
And also you don't want to overload one particular person. So it's some combination of like who has done recent reviews, and also who's the best person for the job.
**Tigran Najaryan** 21:52 Right.
**Liudmila Molkova** 21:53 Essentially, it's round Robin. With negotiation. You pick the next one, and if it's not the appropriate one you somebody needs to volunteer or.
**Tigran Najaryan** 22:03 Yeah, yeah.
**Liudmila Molkova** 22:04 To find a different one.
**Armin (Dynatrace)** 22:05 It's the next best subject matter expert that has time and for donations no conflict of interest.
**Tigran Najaryan** 22:17 Okay, anyway, I guess the the when. When I look at the whole list, I think it makes sense to me to have this rotations. So I guess the next step for us is to for all of us to agree to this, and if we agree, we will start rolling it out with some sort of tooling, or whatever we which uses tools.
So I I don't know how exactly we want to go about it, but maybe everybody goes and says I, I am on board. I agree. I approve of whatever on this section, and then we we're all done.
**Jack Berg** 22:53 What do we think about this like these members? You know the do. We want to give the ability for people to? I guess this is the only one that isn't the entire tc, the spec rotation. Should you have the ability to opt out? I think we probably have to.
**Tigran Najaryan** 23:14 Some scheduling problems. Let's like, if I'm on vacation.
then I'm open on vacation, right? But I think that's the opt out. Otherwise I don't see a reason why you would want them need to to opt out of out of any of this.
**Jack Berg** 23:30 So opt out is more of like a a rescheduling.
**Tigran Najaryan** 23:33 Responsibilities.
**Jack Berg** 23:34 Abilities rather than.
**Tigran Najaryan** 23:35 Yeah, it's rescheduling.
If I'm on vacation next month I can probably negotiate with somebody and swap places. I guess right.
**Jack Berg** 23:59 Let's just make that note there.
**Tigran Najaryan** 24:01 Do you wanna strike out the opt out? Because I think that's that's the wrong way of phrasing it.
Yeah.
**Jack Berg** 24:28 Alright. So we have. We have 6 of us here. There's only 2 people missing Josh and Bogdan. So I think that gives us quorum to like agree on this if we want to. And you know, then the next question is about tooling that Tigran was mentioning. I think there's a low tech version of this, where we don't need any tooling at all. And we, just as a 1st item in our in our weekly Tc meeting, you know, visit the current schedule for each of these rotations, and make sure that everyone's on the same page with who's responsible.
**Tigran Najaryan** 25:06 Would just put a for myself personally, even just put a calendar event on Google Calendar, repeating every whatever 8 weeks, or how many of us is now so weekly, and I would just know that that's my my week of responsibilities there, right? It's pretty easy to do.
**Liudmila Molkova** 25:27 So the week starts on Wednesday.
Yeah.
**Tigran Najaryan** 25:33 Could could be. Monday. Right, do-do. We need it to align with this call. For some reason.
**Liudmila Molkova** 25:40 It's just easier.
But it can start on Monday. Then we need to discuss to to whoever will be the next starting Monday. Well, that's fine. Yeah, we can discuss the just one.
every person for each of this.
Thanks.
**Tigran Najaryan** 26:02 Yeah, I'm fine, whatever we decide. I don't mind if it's on Wednesdays.
**Liudmila Molkova** 26:07 So this this table we have here.
It should be, poor thing! I can. I can draft the the table so it's each of those responsibilities, and the person responsible for the next week.
**Jack Berg** 26:24 And maybe we can go a couple of weeks out into the future, maybe 4 or 6 weeks, or something like that. Just so we can see ahead and give people the opportunity to reschedule.
**Liudmila Molkova** 26:33 Right.
**Tigran Najaryan** 26:38 Yep.
**Jack Berg** 26:40 So, okay, we have 6 people. Do we all want to agree to this in some sort of informal way.
**Reiley Yang** 26:51 Yeah.
we we already have the Tc meeting notes where we keep the agenda, and we used to have a rotation table there, right? So we can probably just use that.
**Tigran Najaryan** 27:03 Does anybody object to doing this? Rotations here on this call? Is everybody on board?
I'm on board.
**Liudmila Molkova** 27:15 I'm as well. One thing I wanna mention, some of these things has been historically run by specific people. I'm pointing to Armin and Armin. Would you mind documenting what you should do, and how you should react?
I don't know. 10 sentences or less.
**Armin (Dynatrace)** 27:37 Yeah, sure. Makes sense.
**Liudmila Molkova** 27:40 Thank you.
**Tigran Najaryan** 27:41 And for I guess, similarly, for the releases, Carlos, you're doing it. And I know we have a releasing document. Do you think there's anything that is missing there that you would like to capture.
**Carlos Alberto Cortez** 27:52 Oh, trust updated that recently. But I will double check in case there's something. Yeah. And, by the way, we don't use change log files like the collector or semicom. I just, you know, we do the change log, you know, stuff manually small. So anyway, we can talk about details later.
**Tigran Najaryan** 28:10 Yeah, yeah.
okay. And we should also obviously make sure that that Bogdan and Josh are also on board.
We'll need to ping them. Make sure that you agree to this as well.
**Jack Berg** 28:27 So what? What are the other things we wanna note?
Week starting on Wednesday.
**Liudmila Molkova** 28:36 I mean we can do Monday. I no, no strong opinion there.
**Jack Berg** 28:46 See, there is just there are 2 weekly rotations, one monthly so the the monthly one should start on the 1st of the month. Obviously, whatever day that lies on and the weekly ones.
I guess we can debate about it, whether it's Wednesday or Monday, but it makes no difference, because each one of these units is going to enclose. You know, exactly one spec meeting, exactly one Tc meeting.
and sometimes we skip Tc meetings and spec meetings, you know.
Do you get to skip your responsibilities for that week? Probably not. I think that your your responsibilities just probably get pushed to the next week.
**Liudmila Molkova** 29:37 It will be very hard to do.
But yeah, let's try.
**Jack Berg** 29:46 Let's just say weekly meetings weekly schedule start on on Monday. Just because I think it's probably most natural for how we I don't know about you all, but I'm always frustrated by the lack of alignment between like fiscal years and calendar years like that drives me crazy. Why do I? Don't. We all just like align with the calendar year? And so this seems like an extension of that.
**Liudmila Molkova** 30:08 Right. We can also reschedule this meeting can, but we would not change the schedule.
**Jack Berg** 30:22 Let's say, if back or Tc. Meeting is canceled.
you know, responsibilities carry over to the following week. So you don't just get to skip by, you know, getting lucky.
And we mentioned that we're going to just track using the You know, this rotation section of the the Tc. Meeting notes. And if anyone has ideas for automation around this, we can, we can definitely do that. But like, let's start low tech and and go from there.
**Tigran Najaryan** 31:09 Okay, I'm also pinging Josh and Bogdan to make sure that they read and agree to the rotations.
**Jack Berg** 31:27 Do we want to set up a quick little section to, to, you know, to formalize the rotations in this duty rotation section? Or does somebody want to do that offline? And once Josh and Bogdan give the thumbs up.
**Tigran Najaryan** 31:42 Yeah, let's wait for the thumbs up in case they have any comments, and then we'll do that.
**Jack Berg** 32:06 All right.
Anything else on this topic.
**Reiley Yang** 32:11 And then there's a public holiday.
What do we expect like I but I would expect we we we just carry as normal like, if you have a public holiday in your country or something been.
it's okay that he escaped that day, but coming back the next working day, he should still take care of things.
**Liudmila Molkova** 32:36 I would imagine, if.
**Reiley Yang** 32:37 Back meeting has that issue like, if you organize back meeting, but it's a public holiday for you. Then what do you do?
**Liudmila Molkova** 32:45 You probably don't want to be responsible for the the spec. Meeting is probably fine, but security, irritation. I would imagine you are there every day.
**Armin (Dynatrace)** 33:03 I think that the the person that's on shift if they happen to have a personal or public holiday that collides with it, they would be responsible for resolving it beforehand by just asking if someone else can can take over, jump in, or swap shifts, or or whatever up to them, but they would still be accountable for for ensuring that, because we don't know each other's vacations or or holiday schedule.
**Liudmila Molkova** 33:32 And that's why we should have a schedule set up for a few weeks in advance, so that we can plan.
**Reiley Yang** 33:42 It sounds like he won't, because if there's a like, the meeting has no agenda, it got skipped. Then the plan got screwed up.
**Jack Berg** 33:52 Yeah, right? So the if if we know in advance that the meeting is gonna be canceled, then we can obviously reflect that in our projection like, if we know Kubecon is on the schedule, we can skip that week in the schedule, but sometimes we we don't know until the week of that the meeting is canceled because we're bad at planning and foreseeing, you know, kind of big public holidays. So I guess we address those as needed.
**Liudmila Molkova** 34:18 Yeah. And we probably should admit there will be some mistakes and constellations and urgent rescheduling. But as long as it's not every week, it's fine.
**Reiley Yang** 34:34 Yeah, what's the problem if we just stick with like the calendar weeks and months, and if you're you're on duty. But the meeting got canceled, and you just don't drive that meeting. You still have other obligations like security. Other stuff, right?
Doesn't seem like a big change, and it makes planning easier.
**Jack Berg** 34:56 There's there's an argument to that. Yeah.
**Liudmila Molkova** 34:59 Just best effort, correct.
**Reiley Yang** 35:01 Yeah.
**Jack Berg** 35:04 So then that would just mean that we strike out this part. So we can still, you know, project it out several weeks in advance. So you know when your duties are coming.
And I guess you should still have the ability to swap with other Tc members, regardless of whether you know the meeting is canceled because of calendar issues. But this bullet is is essentially axed out and replaced with something like You know, you got lucky.
**Tigran Najaryan** 35:56 Jack, should we add this to the to the actual responsibilities, doc rather than meeting notes.
**Jack Berg** 36:03 Yeah, well, so that's that's that's kind of.
**Tigran Najaryan** 36:04 Maybe copy it later. That's that's fine as well.
**Jack Berg** 36:07 Maybe we actually extract out the formalization of the response, the rotations along with the calendar into a document that is just like linked to here, and so like everything about rotations, is in one place.
**Tigran Najaryan** 36:20 Yeah, yeah, maybe do that. Yeah.
**Jack Berg** 36:39 Alright!
Alright! And if if Armin is, you know.
you know Ludmilla mentioned that it'd be great if Armin could summarize in a few sentences what he's been doing on the security side of things, you know. We can just put that in an appendix in that document, too. So.
**Armin (Dynatrace)** 37:01 Yep. Sounds good.
**Jack Berg** 37:03 Dude.
Alright! Well, that was a productive use of time.
**Reiley Yang** 37:24 One very quick question. So if the meeting is canceled, then I I think there's still one small responsibility there. So if you're on duty. You should update the agenda just calling out, the meeting is canceled. I've noticed that couple of times I have to update the the meeting notes because people join up by mistake, and they they ask on slack.
So I would expect like. If you're on duty, then you should make sure you communicate that before the meeting.
**Jack Berg** 38:00 Yeah. And so update the meeting notes slack to indicate meeting is canceled and you know, I don't think we have calendar permissions. I think Trask has calendar permissions, and maybe some other folks on the Gc. But it'd be great if that person could also, you know, cancel the the calendar invite, as well.
**Liudmila Molkova** 38:18 I think everybody can get calendar permissions. I do have calendar permissions because I requested them.
**Jack Berg** 38:24 Oh, okay.
**Armin (Dynatrace)** 38:25 Yeah, every Maintainer can can request them. There's just some caveat depending on how secure your company has set up there mail, like trusted mail server domains and verification. The cancellation emails might not go through.
for example, from my work email. I can't cancel any any calendar things because they are coming from from Google, Google or Google Calendar mail servers, and and then recipients will reject them because they are not not allow listed as sending email on my behalf.
That's a bit annoying.
But for those that usually trust, but also others cancel on behalf of, I think, admin@opentelemetry.i/O, by logging in to that Google account they are reliably delivered.
But I don't know who has access to that. That Google account. Specifically.
**Jack Berg** 39:35 Would you know?
**Liudmila Molkova** 39:37 I would imagine that posting a quick message in the let's say spec chat, and adding the meeting canceled into the agenda.
Yes, good enough.
**Jack Berg** 39:53 Yeah. You know, the the whoever's on duty should somehow facilitate canceling the meeting, whatever that means. It's like, you know, if they can cancel the meeting themselves in the calendar, or they can ask somebody with calendar permissions to do it.
or you know, perhaps it's not even needed to to cancel the calendar, invite, and you can just post in slack, and then the meeting notes. But That's their job is to sufficiently communicate it.
**Liudmila Molkova** 40:29 Thank you all I need to drop off to do something.
But thank you.
**Jack Berg** 40:37 Yeah, if there's no other if there's no other comments on this, let's let's call this a day on this topic. Does anybody else have any other topics.
**Reiley Yang** 40:50 Nope.
**Carlos Alberto Cortez** 40:52 Yeah. Well, I wanted to mention. Oh, never mind. I, for some reason I thought was here. But no, because it was about the fast. See? You know that.
I will ping him directly.
Okay.
**Tigran Najaryan** 41:07 Alright. Thank you.
**Carlos Alberto Cortez** 41:09 Perfect.
**Reiley Yang** 41:10 Thanks! Take care! Bye.
