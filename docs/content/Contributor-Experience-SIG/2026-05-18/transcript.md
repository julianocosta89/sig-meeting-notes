SIG: Contributor Experience SIG
Date: 2026-05-18
Duration: 20 minutes
============================================================

## Zoom Recording Transcript

**Amy Super** 01:03 Hi, hello.
Is it Dhruv? Is that how I say your name?
**Dhruv Ahuja** 01:08 Yeah, hi, Emmy.
**Amy Super** 01:10 Nice to meet you.
**Dhruv Ahuja** 01:12 Nice to meet you, too.
**Amy Super** 01:14 I'm just gonna hang out for a minute and see if anyone else joins, and if not, we can, Walk through a couple things.
**Dhruv Ahuja** 01:23 Okay, so, just so you know, it's, like, my first session, for this one. I just started hanging out at the Hotel Sikh just today, as a matter of fact.
**Amy Super** 01:33 Okay, cool. Yeah, well, happy to have you, and, can definitely give you an overview of what we do here, and, some of the things we have on flight.
It's a holiday in Canada, and the other maintainer who usually joins at this time is in Canada, so I think we'll just give it another moment, and then, we can jump in.
**Dhruv Ahuja** 01:56 Sure.
**Amy Super** 01:57 So it might just be the two of us, I guess is what I'm saying.
**Dhruv Ahuja** 02:01 Yeah, that's totally cool.
**Amy Super** 02:03 Cool. Alright.
**Dhruv Ahuja** 02:06 By the way, did I pronounce your name right? I think I got it wrong. It's Amy Wright.
**Amy Super** 02:11 Yes, it's Amy. You got it right.
And while we hang out, I'm not sure if you, have AXA or know where our notes are. I'm just gonna drop them into the chat for you.
And those are the, notes for these meetings.
**Dhruv Ahuja** 02:43 Okay, I bookmark that, yeah.
**Amy Super** 02:49 So just give it, like, 2 more minutes to see if anyone else joins in.
**Dhruv Ahuja** 02:54 Sure.
So, how many people are typically joining this call? Is it typically just the two of you?
**Amy Super** 03:02 It's usually pretty small, usually 2 to 3 of us, so I would say that… oh, hey, Bogdan.
I would say that generally, this is sort of a lighter attended, SIG meeting.
But certainly, we're interested in having, more people participate, so just because there aren't very many of us doesn't mean that there's not work to do, so… Yeah.
**Dhruv Ahuja** 03:33 Yeah.
**Amy Super** 03:36 So… let's just go ahead and jump in. Like I said, it's a holiday in Canada, and Marilla's there, so… And usually, she's the other person who joins here, so… So, Dhruv, do you want us to just give you, like, a little introduction of what we do here? And, you know, because it's just the two of us, so we can kind of go over that if you'd like.
**Dhruv Ahuja** 04:03 Yeah, please.
**Amy Super** 04:05 Sure, so this is the contributor experience SIG, and really what we're focused on is improving the ability of people to contribute to the community. So this is a little bit different from dev experience, which is very focused on, like, the developer experience, like, in terms of, like, what tests are being run, what checks are happening that are automated, right? Things like that. Whereas this is more like, how do you get started? How do you find out, what is on various backlogs? How do you know what the priorities are of the community. And so, the idea here is that we're looking at items like that. In the notes that I shared, we do have, our project board. It'll give you an idea of some of the things that we're working on.
And as I mentioned, this, this SIG, I would say probably about, 6 months ago or so, kind of wrapped up some work, and then started a new body of work, and so some people kind of dropped off of the SIG, and then some people have, started joining more frequently since then. So… One of the things that I've been working on is I did some user interviews to find out, so people had told us that they found it was difficult to get started contributing to OpenTelemetry, and so… but that could, like, mean anything.
So I did some user interviews to learn more about why… what was difficult about getting started, and the findings from that fed into some of the issues that are in our project board, which, I'm now starting to work through, but not very quickly, admittedly. So, so yeah, this is a little overview. Do you have any questions?
**Dhruv Ahuja** 05:52 No, yeah, it seems pretty clear to me. So, basically, just like how we have DevEx, basically, this is the contributor experience, where it… okay, so the intent is that anyone that wants to contribute, or even a seasoned contributor.
What are the workflows or improvements that they need to make the project better, essentially?
**Amy Super** 06:13 Exactly, yep, that's exactly it, so… So, usually what we do in this meeting is talk through some of our, kind of, like, to-do list, and… So the last thing that happened… so I wasn't here for our last meeting, I was traveling, and then I got sick, like I always do when I travel, and so I actually have, like, no movement on my action items from… Let's see, it would be April 20th, so I'm just gonna drop these… Here… And then nodes. So one of the things that we learned when we talked with people was that they felt that, they wanted some video content that was just, like, a very clear, where do I go to start.
And so Marillia and I talked about, some topics that we could take, and, And then I think neither of us have actually recorded the videos. So that is the top of my to-do list, and something that I plan to do, coming up soon.
So that's the only update that I have today. Bogdan, it looks like you were here last time, I don't know if you have anything to add as a follow-up. Go ahead.
**Bogdan Stancu** 07:28 Well, not really. I mean, that was a pretty good description of what, what had… I don't know what to add. What I would add is that, I… I just took, like, two issues last time, and I have a PR for one of them, and another one that's coming from another one.
And I wasn't really sure, like, how to just… that was the question that I had last time. Like, if I go through the backlog, what do I do? Do I just start Like, what would the process be? Because all the issues aren't really asks, they're, like, kind of… Issues, without an open-ended… task assigned to them.
So I… the answer was to just try to figure out a solution, and try to open a PR, or continue the conversation on the issue until something concrete happens. So I did open a PR, and I have a review that I didn't look over yet.
And I have another one coming for those two issues, and I'll get more after those are merged.
**Amy Super** 08:39 Nice. Yeah, I would say that, like, as far as how it works, we do need to update, and it's probably something else that needs to be done, we do need to update our repo, so in the past, when there were more maintainers and more contributors to this, SIG, It would be, like, if two people assigned themselves, it would become active, but we don't have enough people for that, so I would say that anything that looks achievable to you, that you would want to pick up. So I did create… let me just find the right… Tab here to share.
Okay, yeah. So, I did create this view that I called backlog prioritization, where I just sort of, like, dragged into kind of, like, my own sense of… but actually, it needs to be updated. This should be up here. So I'll fix that, but, I had just sort of dragged these as, what I thought would be the top things that we can work on, and I see that you grabbed the next one down, so I think that's great.
But yeah, I would say that, like, any of these, if you are unsure of how to work on them, or you have ideas, like, just kind of start, and then tag the rest of us, and we'll just give feedback, or check in on Slack if you want feedback and you're not hearing back from people.
So yeah, I think that's great. So… Dhruv, did you have a question? Go ahead.
**Dhruv Ahuja** 10:11 No, no. I think, yeah, it makes sense. I'll have to take a look.
**Amy Super** 10:17 Okay, cool. Yeah, what I tried to do was prioritize, and again, I have to fix it because it looks like our video stuff, I think by default, new things just fall to the bottom.
But what I tried to do was pick issues that I thought were, like, achievable by one person or two people, because some of these are a little bit trickier, like Asia Pacific Friendly SIGs. So, like, one of the pieces of feedback was that, there are, like, the meetings are not always at times that are friendly for APAC. And so… while, like, we could change that 4-hour meeting, we… it's hard to do for everybody else's, and so that's why it's a little bit lower on priority, just because I was thinking about, like, how to, you know, prioritize things that, like, we feel like we can, like, directly impact today.
So… so also feel free to have a look at this list, and if there's anything that, like, doesn't make sense to you, or that, you think should be higher priority, I'm very open to that. I really just tried to do this as a way of myself making sense of what was in flight.
And there's still more cleanup to do here as well.
**Dhruv Ahuja** 11:31 Got it.
Yeah, I think…
**Bogdan Stancu** 11:33 I agree.
**Dhruv Ahuja** 11:34 In part, I think the AI team… yeah, please.
**Bogdan Stancu** 11:37 No, sorry, study.
Okay.
**Dhruv Ahuja** 11:40 Yeah, so, I think the Gen AI instrumentation team has also just changed their APAC timing, to allow more people from the US and, Europe to join.
I think that just happened, like, an hour back.
So I think APAC is definitely an issue for some.
**Amy Super** 11:59 Yeah, yeah, for sure.
Yeah, and feel free, Droop, if you want to just comment on this issue, and just say that, like, this is a SIG that, you know, seems to be doing it well, or, like, has you know, just to add some more, details in here, that would be helpful, so feel free to go ahead and add that.
**Dhruv Ahuja** 12:24 Okay.
**Amy Super** 12:26 Bogdan, were you… were you gonna say something? Yeah.
**Bogdan Stancu** 12:32 Yeah, I just want to ask if the status changes automatically, or should I change it? Because I see that Progress, but the, the, the other one.
isn't, and well, the other one doesn't have any… There's another one, yeah, 22.
That one… the other one, the 22nd one, doesn't have any PR from me, so I'm thinking maybe it's automatic if I open a PR, or should we keep the status, like, in check?
**Amy Super** 13:01 It must be automatic if you open a PR, okay.
But I would say that if… if you are doing non-PR work.
Right? So, like, some of this stuff isn't necessarily PR-related. Feel free to flip the status to in progress.
So… So, like, for…
**Bogdan Stancu** 13:22 I don't know if I have.
**Amy Super** 13:23 Yeah, like, I have…
**Bogdan Stancu** 13:24 Candidate.
**Amy Super** 13:27 Sorry?
**Bogdan Stancu** 13:28 I don't know if I can do that.
**Amy Super** 13:30 Oh, okay. Well, here, let me… let me see if I can, because I think I might have rights to do that.
Open… Oh, that just added.
**Bogdan Stancu** 13:41 No.
**Amy Super** 13:41 Where is it in this view?
**Bogdan Stancu** 13:48 Which one? What?
**Amy Super** 13:49 Oh, how would I flip this to… oh, wait, can I just grab here? There we go, okay. So there, there you go, I got you.
So likewise, if there's anything that you can't do, feel free to tag and.
One of the maintainers can update stuff if you need help, so… Okay.
So just in terms of next steps, I'm just going to say, like, feel free to review the backlog.
Self-assign.
Yeah, there you go.
**Bogdan Stancu** 14:34 We cannot self-find them.
**Amy Super** 14:36 Oh, you can't? Okay.
**Bogdan Stancu** 14:38 No.
**Amy Super** 14:39 Okay, then you know what, I think we actually need an action item to… Review… GitHub permissions.
**Bogdan Stancu** 14:52 I wasn't even in the list to assign those issues to me until I commented on them.
**Amy Super** 14:59 That might be how…
**Dhruv Ahuja** 15:01 part of the org, right? Okay. Because I think it is set off on permissions itself, assigning or unassigning, adding labels and such.
I don't think that it is… it is, like, you can manage which exactly the things you want a user to do, as of my knowledge.
**Amy Super** 15:19 I see. Okay. So, I would say, in that case… If you see something you want to work on, just comment on it, and tag me, or tag Marillia, and we'll just do it.
Oak.
So…
**Dhruv Ahuja** 15:37 Yeah, I'll also check if what I'm saying is correct, or whether there is some way to have more granular permissions, but I'm pretty sure that… Okay.
**Amy Super** 15:59 Got it. Okay. Yeah, let's just do that for now, and then… Okay, cool.
Any other updates or questions or things we want to go over today?
**Bogdan Stancu** 16:19 I mean, I do have… about the stuff that I did, I do have questions, but I would post them on the issue, instead of talking here, because it has a lot more visibility there.
**Amy Super** 16:29 Okay, I mean, I was gonna say, we can go over it today, we have time, if you want to have a quick look, so… It's up to you.
**Bogdan Stancu** 16:36 Sure. If you want to review the… I can do the PR for the other one. This one?
**Amy Super** 16:43 Sure.
**Bogdan Stancu** 16:43 That one has a PR.
Okay. And I think it should be fine. And also, I did write a… a comment explaining what I did and why I didn't do some things.
**Amy Super** 16:55 Cool. Alright, yeah, we can have a look at that. Are you… is your PR just waiting for approval, then?
**Bogdan Stancu** 17:02 Yeah, it should be, linked somewhere, like, lower in the… In the issue.
That one. The community one.
**Amy Super** 17:10 Yes.
Cool.
Alright, sweet. Yeah, I'll check that out after this meeting and have a look. It looks like you got a review…
**Bogdan Stancu** 17:22 I don't know that you…
**Amy Super** 17:23 I think it's just from the community team, so I don't know that you need reviews from us, it looks like you just need reviews from the community team, so…
**Bogdan Stancu** 17:30 Probably, yeah.
**Amy Super** 17:32 Okay, cool.
**Bogdan Stancu** 17:33 And there's that other one, where I think it, like, a bunch of things happened since the issue has been opened.
And… This description doesn't… Describe what's… yeah. I mean, it does make sense, in a way, but the… that file that describes promotion and stuff like that is already pretty much here. I do have.
**Amy Super** 18:02 Okay.
**Bogdan Stancu** 18:02 the PR to kind of complete it. Okay.
just the promotion part.
But it is… It's not much.
**Amy Super** 18:12 That's okay, so I think that's totally fine, especially when you look at some of the ones that I put a little further down.
Some of them did just seem, like, out of date, and so I think that if you feel like the original issue was covered, and any work that you can do will, like, wrap it up, I think that's completely fine, and we can just then, you know, with your PR, then close it.
So, like, for example, like, this one, like, Maintainer's Handbook, like, I'm pretty sure we have a lot of content around this now, and so I don't know that we would actually pursue this further. So that's why some of these I do want to go through and kind of clean up and close, so… And like I said, I just need to move this to the top, but I, like, okay, let's see if it breaks everything.
So… I think that we're probably, like, here. There we go.
Okay, and so these are the videos that I was talking about earlier that Marilla and I said that we were going to work on, so… Cool.
And this one, I think we decided, Oh, that's right, I have a follow-up here. That if we're gonna do videos, we don't need to do a blog post, too, so… Cool.
Okay.
Anything else?
**Dhruv Ahuja** 19:38 Yeah, so, sorry, it just occurred to me that I think I can probably just get started off by looking at the issues, but are there any other resources that we have for this SIG itself that I can take a look at, or anything, any other issues that you feel that you resolved in the past that might help get more info?
**Amy Super** 19:57 So definitely take a look through our Slack channel and look back, the last couple months. It's not, like, really heavy traffic, so that's not, like, a huge ask, because a lot of stuff ends up getting posted there.
And I would say look through the, some of these notes. We'll have links to some of the things that we've been working on.
That will be helpful as well. But those would be the primary things that I would recommend that you have a look at.
**Dhruv Ahuja** 20:30 Gotcha.
**Amy Super** 20:31 Cool.
Well, we're happy to have you, thanks for joining. So, we could always use help, so…
**Dhruv Ahuja** 20:39 Yeah.
**Amy Super** 20:41 Okay, cool. Well then, let's call it, we don't need to stay for the hour, and I'm gonna have a look at this.
**Bogdan Stancu** 20:50 Thanks a lot.
**Amy Super** 20:51 Alright, cool.
Thank you, everyone. Thank you, bye-bye.
**Dhruv Ahuja** 20:54 Bye-bye.
