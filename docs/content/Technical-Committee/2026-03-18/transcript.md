SIG: Technical Committee
Date: 2026-03-18
Duration: 37 minutes
============================================================

## Zoom Recording Transcript

**Reiley** 01:30 No, Jack.
**Jack Berg** 01:32 Hey, Riley.
**Reiley** 01:46 Hey, Tiger.
**Tigran Najaryan** 01:48 Hey, guys.
**Jack Berg** 01:55 Hey, Grin, it looks like you're in, suggestion mode on the document, so… Instead of edit mode.
**Tigran Najaryan** 02:05 Yeah, I don't know why is it doing that.
Is it just… Because, I'm not an editor for some reason, that's why.
**Jack Berg** 02:18 Maybe it's a different Google account.
**Tigran Najaryan** 02:22 I no longer have my, corporate Google account.
So, maybe that was… yeah, maybe it wasn't my personal Google account.
Do you want.
**Jack Berg** 02:33 Is your personal Google account in the, the bookmarks of the OTELTC channel? I can go and invite it right now to that document.
**Tigran Najaryan** 02:41 Let me see…
**Jack Berg** 02:45 I just see a Cisco one and a… and a personal one, but not a second Google one.
**Tigran Najaryan** 02:51 That's, you mean the… the… in the list of email addresses, or somewhere else?
**Jack Berg** 02:56 List of email addresses.
**Tigran Najaryan** 02:58 So the secondary email address is the… is my personal one. If you can add that, that would be great.
**Jack Berg** 03:06 Sure, I'll do that right now. And that's a… that's a G Suite account, so you can, you know.
**Tigran Najaryan** 03:11 Yeah, it's a personal Google account, essentially, yeah.
Sorry.
My Cisco email is no longer… has no access to Google Docs anymore, at all.
**Jack Berg** 03:28 I lied. Only the owner can manage access.
And the owner is… the… There's a shared Google account that owns things like the calendar and documents.
**Tigran Najaryan** 03:40 Okay, I requested the permission, so someone should receive it, I'm guessing, an email?
Are we all?
Probably our owners, I don't know how it works.
I don't think we are. Anyway, anyway, yeah. Anyway, we'll sort it out offline. Let's take a look, maybe, at the inbox.
Buffing there, community inbox… Nothing there, either, unassigned.
open spec PRs. We want to go over those, it's a long list. Let me share my screen.
**Jack Berg** 04:21 So the list gets pretty small when you filter out TC members, and you filter out OTEPs.
**Tigran Najaryan** 04:28 what do you mean? Filter by, like, choose names here?
**Jack Berg** 04:32 No, no, no, there's no, like, you know, you have to do this manually, I guess, because the link isn't set up to do this, and I'm not sure it could be. But yeah, like, so basically, we sort of casually decided that we should assign TC members to PRs, which are not OTEPs, and which are not authored by TC members.
**Tigran Najaryan** 04:57 Right.
Isn't this the entire list, then?
It is, but there'.
**Jack Berg** 05:03 There's a lot that are by… that are OTEPs and are by TC members. I see.
**Tigran Najaryan** 05:07 I see, yeah, okay, okay.
Do you guys want to spend time doing that now? What's the plan there? Did we… do we want to do that now?
**Reiley** 05:20 I think he has.
**Tigran Najaryan** 05:23 Okay, maybe let's do a few?
**Jack Berg** 05:26 Yep.
**Tigran Najaryan** 05:27 I don't think this needs an assignee.
It's a chore.
**Reiley** 05:31 Well, this one, I think we already got approval from the C++ seed, so we should just have another approval and merge it.
**Tigran Najaryan** 05:40 Okay, sure, but I don't think it needs an owner, right?
Does work in progress, draft, I'm skipping, this one.
That's from a TC member, and this one too, here too, so this one, okay.
**Reiley** 05:57 Okay, for this one, I noticed one thing. So, it seems like this PR is trying to add some feature. At least, like, I'm trying to be really lazy here. If you look at the changelog, it says add something, add something, but there's no issue tracking, there's no agreement, there's no triage, so this is why I block the PR, and I… I think we talk about this, we want to be a little bit more rigid here.
**Tigran Najaryan** 06:23 Okay.
Do you want to drive it? I said, well, yeah.
**Reiley** 06:26 Yeah.
**Tigran Najaryan** 06:27 Looking into it.
**Reiley** 06:28 Cool.
**Tigran Najaryan** 06:28 Can I put yours?
**Reiley** 06:29 Yeah, so David and I are already there.
**Tigran Najaryan** 06:46 What's this about?
**Jack Berg** 06:49 I just, assigned myself access to this. This is related to declarative config, a capability that's needed, for the collector's usage, so…
**Tigran Najaryan** 07:01 Thanks.
**Jack Berg** 07:11 It looks like this has a lot of consensus already. Maybe we can just assign, Josh or Riley, who have already approved it.
But, you know, it seems like this will go through, so hopefully not a lot of work.
**Tigran Najaryan** 07:24 Josh, can I assign it to you?
**Josh Suereth** 07:27 Yeah, that's fine.
**Tigran Najaryan** 07:34 This is from you, Jack.
Anyone wants to take care of this one? We already have some approvals.
I'm guessing should be good to go.
Mostly.
Can assign Jay McD, he's not here.
**Jack Berg** 07:59 He's here now. He's here now.
**Tigran Najaryan** 08:00 Oh, he's here.
**Jack Berg** 08:02 Enjoyed.
**Carlos Alberto Cortez** 08:04 Josh, you okay?
**Tigran Najaryan** 08:05 You approved it. Do you wanna… do you wanna drive this to completion? You okay?
**Jack Berg** 08:11 Well, you don't… just to be clear, you don't have to drive this to conclusion… well, maybe… maybe drive is the right word. You should just… we should be shepherding this towards, like, closing them, or… or resolving them one way or the other, so I guess that is driving.
**Tigran Najaryan** 08:24 Yeah, yeah.
**Carlos Alberto Cortez** 08:25 By the way, I thought… I thought… sorry, sorry, this is Carlos. Sorry, I thought that was a sign to me.
**Tigran Najaryan** 08:30 It's not. Do you want to take it?
**Carlos Alberto Cortez** 08:33 Yeah, I think that probably… that makes sense, because I also left the only comment that, I wanted the author to change, and he did change that, but I forgot to review that a pair of days ago.
But it's looking good. I just want it, yeah, to be aligned with what SikTin is doing the same way, yeah.
**Tigran Najaryan** 08:51 Okay, sounds good.
Let me take this one, okay.
I don't know what it is about, I'll take a look.
tab.
Let's check… It's a stale, I think.
And draft, okay.
**Jack Berg** 09:16 Yeah, everything else is drops and filter, so we're done.
**Tigran Najaryan** 09:19 We're done, we're done. Okay, good.
What is this one? What did you want to do? All that backlog with timebox? You want to take a look at the alt apps as well?
**Jack Berg** 09:32 That was the idea, just to get them, you know, unstuck, stop them from languishing.
**Tigran Najaryan** 09:39 And I guess…
**Jack Berg** 09:40 We were going in, reverse order, so, you know, oldest to newest? What was the last one we talked about last week?
**Josh Suereth** 09:48 Multiple.
**Jack Berg** 09:49 resources and an SDK?
**Josh Suereth** 09:51 Yeah, that one has enough approvals to merge. I have to fix a typo, but that one, that one's gonna get merged shortly. It has enough approvals, we talked about it, I think we're good to go to the next one.
**Tigran Najaryan** 10:10 This is also… this has some approvals, and… there was some progress made on this, I remember. I commented on it. I don't know if we just need probably more eyes and more approvals, but this is close, I think.
**Jack Berg** 10:29 approval on this. This is just an OTEP. It's not, like, the final work, and, you know, this person, Ivo, has… has, you know, done a lot of work to kind of, you know, show how this would work in different languages. And, yeah, like, you know, I think we all want this, and this… nothing's set in stone right now, so why not approve it?
**Tigran Najaryan** 10:48 Do we want to do the same thing and assign all types in the same way as we did for the… PRs, or we don't.
With the same idea of driving it, essentially, one way or another.
**Josh Suereth** 11:05 I, I think that makes sense. For this particular OTEP, I do want to check, who's the OB representative? I just want to make sure… I don't know who their GitHub names are, but I just want to make sure that they have… they're on here, too, because this is supposed to be eBPF and OB together. So… I just want to make sure that, like.
Both communities have approved this and are paying attention. I see all the profiling folks.
I don't…
**David Ashpole (dashpole)** 11:32 I don't see struggles from OB folks.
**Josh Suereth** 11:36 Okay.
**David Ashpole (dashpole)** 11:36 Unless it's in the… no, no, yeah, I don't see them.
**Tigran Najaryan** 11:41 Okay, you want to make that comment there, Josh? I remember the auto department find myself with the content.
**Josh Suereth** 11:49 Yeah, I approve the… I think this is gonna work for both. I just wanted to make sure that they had a chance to look at it and make comments. I don't really want to block the OTEP for it, but also, like, who's… who's our TC liaison to Obi?
**David Ashpole (dashpole)** 12:04 That's me.
**Josh Suereth** 12:05 That's you. So, David, is this something that you discussed at all with the SIG?
**David Ashpole (dashpole)** 12:10 No, so the SIG unfortunately conflicts with the TC meeting. So I haven't been able to attend the SIG at all.
**Tigran Najaryan** 12:18 Okay, let's, josh, make that comment about OB, let's move on to the next one.
I'm coming.
I was hoping…
**David Ashpole (dashpole)** 12:32 once we… I think we were gonna move the meeting once?
Or, like, every other, so I was hoping once that starts that I'll be able to… And then…
**Tigran Najaryan** 12:56 They do by default. We all know this one.
Josh, I remember when we discussed it the first time, we wanted to see it broken down a bit more into smaller ones. That didn't happen, but I see your approval.
**Josh Suereth** 13:25 It did happen, but…
**Tigran Najaryan** 13:27 Is it? Okay.
**Josh Suereth** 13:28 how you read it. Yeah, if you read the OTEP, the way it's phrased is, here's the work streams. Like, again, it's to the point where it almost doesn't need to… We don't have a place to put something like this, but if you read it the way I read it is, it's saying, here are the set of work streams, that we have a set of goals, we have a set of work streams, these work streams will have OTEPs and owners.
The only thing that I'm still not comfortable with is I think some of the owners are pretty nebulous.
and not necessarily set up for success. That said, this is an OTEP. This is, like, a direction. So I think that comes on us actually defining a project or set of projects for this work.
or having, like, those owners take things on. But if you look at it, it's basically saying, here's the set of work streams we need to kick off for this work. There's a set of open questions, future possibilities of how we're gonna do it. And actually for, like, the federated SEMP, I already have an OTEP for what I think we should do there, right?
Lunmilo is NoTep that's the foundation for the Federated SEMCOM one. So, like, there's already progress being made there. I think this is okay to merge. I do think, like.
again, if you look at it, look at the number of things that fall on, like, the security SIG, or the TC, or the GC, right? There's a lot of things where I feel like there's not a clear owner, or a clear person who will feel ownership, and that has me nervous that, like, some of these things just won't happen.
like the performance benchmarking workstream. Go take a look at that one. That one had a lot of contention. It now just describes what it wants to do, but the ownership is still I don't think set up where it'll actually happen. I think directionally everything's fine. Like, as a proposal, as design, this is fine. As a project proposal, which is this is not.
I'm… I have concerns. So, like, the OTEP, I approve.
project proposal, that's something we need to kind of talk about. How are we going to fit this work in? Who's going to do it? Who owns it? Who feels responsible? I don't see us being able to execute on this whole thing, for sure.
**Tigran Najaryan** 15:34 And that's a problem in my mind. I have no problem with having OTAPs which describe intent, and not some technical detail, but If you don't have a… if you don't have owners who you know will be driving that intent, Then… It's set up for failure, essentially, from day one.
I don't… I don't know what's the point then, right? Unless we make those assignments, and we have people who are clear about that they will be driving the particular work stream.
**Josh Suereth** 16:09 What do you want to do with this OTEP, then, in terms of, like, would you want to say, like, hey, let's cut all the work streams that have no clear ownership?
Or would we say, no, directionally we think these are the right work streams, we just… Need to find someone to staff those, like, to, like, drive that. Yes.
**Tigran Najaryan** 16:29 I think that needs to happen, yeah. I think we should say, yes, we agree with the direction, we think it's the right one.
But for this to be executable, we need owners, otherwise it's not going anywhere.
**Josh Suereth** 16:44 Right, so my view on that, though, is that's the responsibility of a project proposal, not an OTEP. An OTEP is a directional, here's what we should build, and a project proposal is, here's staffing, and people interested, and directly responsible people who will make it happen.
**Tigran Najaryan** 17:01 Okay, so then I guess the, we can say, okay, I abide that. I can say that this is not that we think is a vision.
Document, in a sense.
To execute that vision, there have to be projects created.
Possibly one per work stream, maybe a combined project, whatever it is, but it's not going to be possible to execute unless you do that work, so we need to be clear about that.
**Josh Suereth** 17:31 Yes.
**Tigran Najaryan** 17:31 I'm fine with that approach. I think that that's fine, that's okay. So, have it as a vision document, that's okay.
**Josh Suereth** 17:38 The other thing I'm a bit nervous about here, and I'll just call this out, I think this is in a state where it doesn't overstretch, it leaves room, it calls out problems that need to be addressed. And it took us a while to get there.
And that's why I approve it, because I think directionally this is fine. However.
if Trask and I are the only two that approve it, like, like, this is missing the community, right? This is missing the maintainers.
why are we missing the maintainers here? Is it that they don't have time to pay attention? Is it that they still disagree, but they're too… they don't want to voice anything more, because they feel like they already voiced it? Like, that's something… I don't know how to get that feedback, but that would be why me… me personally.
My technical judgment on this is it is now in a shape where, directionally, it's okay.
**Jack Berg** 18:26 Look, however.
I think it's the job of the author here, Austin, to go around to the maintainers and get support.
If you think that this is, like, you know, something that impacts the whole community, and I agree with that, then somebody has to go do that job of being a marketer, a promotion for this work.
And getting people to give their thumbs up on this.
**Tigran Najaryan** 18:54 Agree.
**Liudmila Molkova** 18:55 My impression that it's not actionable enough for maintainers to have a judgment. It's not clear what is it asking maintainers to do.
**Jack Berg** 19:05 It's asking maintainers to agree with, like, an idea. It's not… it's not specific actions yet, right?
Like, do you agree with this idea for the direction of the community? If so, vote with your approval.
**Tigran Najaryan** 19:23 Okay.
Can we provide that feedback to Austin?
That, in this case, it's… it's important to have, I guess, approvals from TC and GC, but it's equally important, maybe more important, to get approvals from maintainers on this, to get that buy-in. And essentially, we're expecting the author… To do the promoter of the idea and go get those approvals.
Or someone else, right? If anybody else is willing to do that work. But that needs to happen before… because it has an impact on all the… all the community, all the maintainers.
it's… not limited in scope, like many other OTEPs are, or most OTEPs are.
**Josh Suereth** 20:14 Yeah, I… I'll say two things. I think it's reasonable for us to ask for that. I'll ask two questions first.
The first one's the most important. Is this an OTEP that we think… requires the kind of technical judgment that is, like, specification technical judgment, where we think we really only need the TC and GC for this, because it's actually too vague for, like, a day-to-day maintainer.
Is that… is that something we feel is true for this OTEP?
Like, do we think maintainers can meaningfully say, yes, I'm behind this, because they understand the implications? Or do we want maintainers to actually participate more in the actual workstream proposals later? Question number one.
**Jack Berg** 20:57 I think maintainers can participate in this. I know it's not, you know, necessarily in their warehouse, but they still have opinions, they still have thoughts on where the community can go as a whole. You know, they're not limited to the technical details of their language implementations.
**Josh Suereth** 21:14 I absolutely agree, I just wanted to ask it, because it popped in my head.
Okay, then the second question would be, I think it's fair for us to tell Austin, like, look.
We don't see the community sponsoring this, and we think it's your responsibility to go meet with maintainers and find out, like, what the issue is, and in public meetings, they're not willing to tell you what they think.
Because he's been to the spec meeting to talk about this, and we're not getting feedback in the spec meeting on it, right? So, that means you need to start going to the other channels.
to make this… make this a thing. Like, actually start meeting with people directly. You know, I see other GC members who are maintainers, I see TC members who are maintainers, I don't see their approval here. So I think… I think that it's fair for us to ask him to go sort that out.
**Tigran Najaryan** 22:06 Yep.
**Jack Berg** 22:08 We gotta time box this, because I think, you know, we're… the second half of the meeting is dedicated to something else, so, just… can we get a quick volunteer to leave a comment to that effect?
**Tigran Najaryan** 22:23 It doesn't have to be a comment, can be a private message to Austin.
**Jack Berg** 22:29 Well, this is a public meeting, so, might as well be a public comment at this point.
**Tigran Najaryan** 22:34 I see, okay, yeah, fine.
**Jack Berg** 22:39 Jay McD will. Okay.
Thanks, Josh.
**Tigran Najaryan** 22:44 Okay, I think that's enough for today. Let's move on.
Josh.
You're talking about the last 30 minutes, okay, all right.
**Josh Suereth** 22:55 Yeah, and this is… it's optional, like, I think… but it'd probably be good for us to be there. I think it's an important discussion.
**Tigran Najaryan** 23:06 Chuck.
**Jack Berg** 23:07 Yeah, so, at the last GC meeting, GCTC meeting, we were talking about some of the things that went wrong with recent project proposals, and you know, I volunteered to take on one of the action items, which is to, you know, the way I understood it was to improve clarity around what we're working on right now, so we can know what it means to take on a new project, and how that will draw attention and resources away from things that we're already working on.
How I went and interpreted that was, like, hey, what we actually need is we need a data model for how our project works.
We need to come up with a vocabulary and, you know, a database, and in this case, a database is like a YAML file that, you know, conforms to a particular schema of the things we're doing.
And from that small little database, you can do simple reporting exercises. Here, there's, like, a simple script that comes and does a visualization of all the work that we have using a mermaid chart. This is, like, a simple thing you can do. There's things like, you know, shapes to indicate the type of work stream it is, whether it's a SIG or a working group. There's color coding to indicate, like, the sponsorship level.
From the TC, and things like that.
You know, further down at the bottom, this is, you know, like, what this essentially, like, does here is it, encodes this Google Sheet that Josh you know, created months ago and has… is now out of date, where we went through all of the SIGs and assigned a sponsorship level and a sponsor, and there was, like, a nice pivot table where we could, like, say, hey, like, what's everybody working on?
And at what sponsorship level. That's always been a private document. We can't share that with anybody else, or it hasn't been shared with anybody else. And so, like, when we say, hey, the TC is overloaded right now, like.
there's no data to back that up, and I think that's part of the issue. So, you know, actually encoding the things that we're working on and, and reporting on it, I think can drive some of the conversations. I noted a number of risks in the technical, in the TC notes about, like, this type of thing, like, you know, by, you know, reporting on this and structuring the data in a particular way, you create incentive structures, and you… and, you know, all of a sudden, it matters how you count. Like, what is considered a work stream? What, like, what isn't? And you kind of encourage working on things that contribute to the counts that the report acts on, rather than, you know, you disincentivize working on the popular spec issues that maybe aren't big enough to go into a work stream, so that's a problem.
I want to qualify all this with, like, you know, some sort of preamble that, like, states things like that. But, you know, I just wanted to give you a preview of some of the things I've been thinking about and collect some feedback. Riley.
**Reiley** 26:10 This is great, Jack. To add to your point, like, sometimes it's, like, unclear when TC members say they're overloaded, so I'm curious.
do you feel we have a general consensus? What's overloaded versus not? For example, you can… you can spend 3 hours per week on this project, and then you come and say, I'm overloaded, I only allocated 2 hours. So what's the expectation?
Okay, I would normally assume, as TC members, you would spend at least, like, 8 hours per week.
That's the min bar, and then normally I expect people to spend, like, maybe, like, 2 days on this.
**Jack Berg** 26:48 Yeah, yeah, I don't… I don't have an answer for that, and maybe that's part of the… what this surfaces?
is, like, if you can at least articulate what people are working on, then, you know, we can start to have conversations about, like, what overload it is and what it is not. You know, and I think the answer might emerge.
Gradually.
**Tigran Najaryan** 27:15 Yeah, and it's not necessarily just the number of hours, but also… I guess the type of the work you do, right? If you're leading the SIG, it requires a certain amount of mind share, right? So you… you have to have that capacity allocated in your mind to that particular SIG.
Whereas if it's… if it's a routine type of work, where I have to go and lead a spec-seq meeting, that's just that one hour, mostly, and maybe a bit, I guess.
Context awareness in addition to that, but it doesn't necessarily require much else beyond that.
So… It depends, right? So you probably can't take… let's say, I don't know, 5-6 to be a lead sponsor for those 6. That's just too much.
Whereas, I guess there's routine work that you can take, and it takes hours.
But it's… it's… it's… it's a different type of a load, so… I don't know if we should just specifically talk about hours only, or if hours are… Are the more important thing there.
**Jack Berg** 28:31 Yeah, I don't want to get too process-heavy on this. You know, I want to be able to say some things while, you know, keeping enough gray area for us to make judgment calls, because, you know, like, as I noted, these numbers aren't everything. They create incentives for how you count things, and you can quickly game the system. And so, you know, over-indexing on whatever the output of it is Is of this is not a good idea.
You know, one thing I noticed when I was… when I was doing some quick ad hoc analysis of, you know, the output of this is, if you scroll down to the bottom, Tigran, there's, like, this little pivot table that mimics what Josh had in your Google Sheet, and, you know, it shows that we have 23 combining leading and guiding sponsorships, and I was like, okay, where are we investing those coins? Like, where do those coins go?
And this doesn't show up anywhere on here, but 55% of those are in semantic conventions.
So, like… that's a lot, and that's what the numbers say, but it's… there's some things that go into that. Like, you know, several of the SEMCOM SIGs, or working groups, have multiple TC members on them, and there's also, like, this big umbrella of SEMCOM working groups. There's, like, one per domain. And so, like, the numbers say a particular thing, and, you know, maybe there's some signal in there, but maybe Maybe, I don't know, maybe we're recording things wrong.
**Tigran Najaryan** 30:01 I think that's an interesting signal.
Would you be able to maybe also show that as a sort of an aggregate data?
Because what you said was kind of sort of surprising to me, that 50-something percent of all TC capacity goes into SAMConf?
**Jack Berg** 30:20 at least in terms of the leading and guiding sponsorship right now, and, you know, there is some data sanity, some data cleanup that needs to be done here. There's also 13 of these work streams that are unassigned. You know, there's another 4 where we haven't assigned a sponsorship level. You know, people would need to actually, like, go in and update this data to say what level they're sponsoring at, so there's some quality issues like that, but Yeah, like, different views of this data tell different stories.
**Tigran Najaryan** 30:51 I think this is useful. This is definitely useful for us.
and for the GC to look at.
I want to question the usefulness of it as public information that the community needs to look at and make inclusions from.
it opens up… Maybe, Sort of a discussion that… I don't know what the utility of the discussion is in the community.
**Jack Berg** 31:23 Yeah, and I am sensitive about that, so, like, you know, I guess I'll… I'll keep working on this, I'll keep iterating on it, and I'll propose it to the GC and TC, you know, in private channels, even though this is publicly recorded, and you can go and look at my forks and see this right now. But, you know, I guess it's another step further to go and open a PR and have this, you know, merged to the community repo, which is what, you know, where the fork is, so… I'll hold off on that for the time being.
**Tigran Najaryan** 31:54 So, yeah, Jack, just to be clear, I'm not saying we should hide any of this, right? But I'm saying that If we try to somehow… emphasize that information in a specific way, then… then what, right? What point are we trying to make there? What is it that we're expecting will happen as a result of having this information front and center somewhere?
**Jack Berg** 32:20 Yeah, definitely not front and center, and even if it's anywhere public, I think it needs a thorough preamble describing what this is and what it isn't, and what signal you should take from this and ignore.
**Tigran Najaryan** 32:30 Yeah, yeah.
**Liudmila Molkova** 32:32 I think we should make it public in a sense that the, like, we show GC liaison.
sponsors in the project proposals. This is de facto public. We should have a column there in the YAML, in the community repo, with who is the CC sponsor, and what is the level of support is. And this becomes public, it's just not emphasized, the stats are not emphasized, but it's transparent. We should be transparent, I think.
**Tigran Najaryan** 33:00 Yeah, that's fine, I have no problem with that, yeah.
**Jack Berg** 33:04 Alright, should we jump over to the GC meeting?
**Tigran Najaryan** 33:09 Okay, yeah, let's go there.
