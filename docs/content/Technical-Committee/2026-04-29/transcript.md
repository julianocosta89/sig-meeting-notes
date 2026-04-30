SIG: Technical Committee
Date: 2026-04-29
Duration: 61 minutes
Zoom Recording URL: https://zoom.us/rec/share/BwQD3hz61j3sEWKpuxGHMSjs7ZmdTZuDIWWfZDZAnSNS8l74C8X_DkZ-A1HYhrPt.uti6Nb5nw2cLMHrW
============================================================

## Zoom Recording Transcript

**Reiley** 00:48 Hey, good morning, Jack, Tiger.
**Tigran Najaryan** 00:55 Oh.
**Reiley** 01:12 Army.
**Carlos Alberto Cortez** 01:32 Hello, everybody. Let's wait a couple of minutes. Actually, we have 6 people, so, maybe… 1 meters, and we start.
**Jack Berg** 02:01 FYI, I'm just getting started with assigning unassigned spec issues, because… That's sort of a time waster and can be done somewhat asynchronously without Discussion.
**Carlos Alberto Cortez** 02:13 Well, if it's something obvious, like, somebody's, like, the obvious person to, you know, to sign, sure. Otherwise, we can do something here.
**Jack Berg** 02:20 That's right. I'm gonna save anyone that might require discussion.
**Carlos Alberto Cortez** 02:31 We have Tigran here.
Oh yeah, we have. Okay, good.
**Tigran Najaryan** 02:36 I'm here, almost.
**Carlos Alberto Cortez** 02:40 Nice, yes, because you have the first topic. It's an important one.
**Tigran Najaryan** 02:43 I do. Do we want to start already, or first do the triaging?
**Carlos Alberto Cortez** 02:47 Jack, what do you think?
**Jack Berg** 02:50 Let's, let's do the triaging, We say we're gonna spend 15 minutes on that, each meeting, so…
**Carlos Alberto Cortez** 02:58 Let's do that. Okay, let me then, share my screen, second.
What's happening?
I think maybe it's my imagination, but GitHub is super slow for me today.
**Reiley** 03:24 I'm gonna share my screen.
**Armin (Dynatrace)** 03:27 And for me, it also won't show you, all of your issues and PRs.
**Carlos Alberto Cortez** 03:33 Oh, right.
**Armin (Dynatrace)** 03:34 Some issue there.
Like, the lists are non-exhaustive in the UI.
**Jack Berg** 03:42 Other outage?
**Reiley** 03:46 You want me to share?
**Carlos Alberto Cortez** 03:49 I was about to share, but I think it's, okay, so, Yeah, if you could share throat for now, because mine is still, like…
**Reiley** 03:58 Okay, let me do it.
**Carlos Alberto Cortez** 04:00 Yeah.
**Reiley** 04:04 So just look at the TC spec inbox, it's empty. I'm not sure if it's…
**Carlos Alberto Cortez** 04:08 Well, yeah, it could be.
**Reiley** 04:10 Yeah, not sure if it's empty or it's the GitHub issue yesterday, the same thing, but it seems to be empty for me.
So I tagged both links here.
And shall we look at the unassigned PRs, or… Or Jack, you're doing that offline?
**Jack Berg** 04:27 There's a couple that, weren't super obvious that could use a little discussion.
**Carlos Alberto Cortez** 04:33 Good.
**Jack Berg** 04:36 Audit logging signal. This is… I'm not sure this person is following our process. Robert chimed in and said, hey, look, you know, this is a big increase in scope. You need to make a, you know, a project proposal for this, and they pointed to a project proposal that's been open since 2024 and has zero approvals and is not merged.
**Reiley** 04:58 I see. So the… the one from… Sap, right?
**Jack Berg** 05:05 I'm not sure where this person's from.
**Reiley** 05:08 I mean, the previous one.
**Jack Berg** 05:09 Oh, yeah.
**Reiley** 05:10 CT is pretty interested in all this.
**Jack Berg** 05:13 Yep.
**Reiley** 05:15 Okay.
So… We'll just let them know that they should drive for more, like, community requirements before we take this, due to the bandwidth.
**Jack Berg** 05:30 I think so. And, like, who wants to take point on that, essentially, is to, you know, be the person that says, hey, like, you know, you need to drive consensus at the community project issue level.
**Reiley** 05:43 I think that's what GC agreed to do, right?
they… like, they established the process, but for this particular issue, I have the contacts, I'll just reply there.
**Jack Berg** 05:57 I'll sign you then.
**Reiley** 05:58 Yes, please.
But I think based on our discussion with GC earlier, it's like the GC will decide which product we have bandwidth to take, which one is higher priority, then the TC will do the work.
Okay, let's move to the next one.
**Carlos Alberto Cortez** 06:30 So that's not a tip, so I don't know if somebody wants to take on that.
It also has no reviews so far, sadly.
Oh, wait, actually, somebody commented on that. Trent.
**Josh Suereth** 06:43 So, I can jump on this one. This is the, how to deal with tenancy and tracing, is that right?
Yes.
This, this is actually super critical for us. I was… I was talking to the author, on Slack, and sent feedback on Slack. I didn't actually put in the PR, because I didn't know the PR was made yet. So yeah, you can assign that one to me.
**Reiley** 07:10 Do we want another name?
Do we need two approvals.
**Josh Suereth** 07:17 Yeah, I think anyone who manages a SaaS product and has to figure out what to do with traces should jump in on this.
**Carlos Alberto Cortez** 07:24 I am interested in this because of something I have seen before in some other thing I was playing with.
So I can do a review, yeah, yeah, let's do that.
**Reiley** 07:35 Okay, cool. Thank you.
Anything else, or we go to the next one?
**Jack Berg** 07:42 Go to the next one, this is just getting assignees.
So this was a spin-off from another PR that Robert had about coming up with a string representation for debugging purposes.
And it looks like he opened an alternative PR, it is one…
**Tigran Najaryan** 08:03 alternative, it's complementary, it's about attribute, this one is about values. So, I think whoever is doing the values, probably, they are quite related, so it should be the same person for efficiency.
**Reiley** 08:16 Yeah, this is already on David. I'll just do David.
**Tigran Najaryan** 08:20 Sure. I think that's the right thing to do. I commented on it, but one person should take care of both, I think.
**Reiley** 08:27 David, do you feel you need someone else to help here?
**Jack Berg** 08:31 I mean, I think we ultimately need more approvals to merge, and so I don't think that just the assignee is responsible for doing this. It's just, like, the assignee is just the shepherd, and, you know, other people should review and be on board with this.
**Reiley** 08:46 But I had problems where I was the only one who reviewed certain PR, and I have to rally a lot of folks, and in the end, there's lack of clarity who should do it, so I have to, like, bother a lot of folks.
And I wonder if that's a problem for you. Like, I mean, not a problem for me.
**David Ashpole** 09:04 No, I think… I think there's already been good dis… is this the one that's got a lot of discussion?
That has a lot of discussion, so I've just been letting it happen.
**Reiley** 09:13 Yeah, so the one that has a lot of discussion, you're already assigned, and I've seen your reply. Then, Robert just created another PR, which is related to the one that you reviewed, so we're assigning the new one to you, and that one is relatively smaller.
**David Ashpole** 09:29 Good.
That's, that's fine, I haven't reviewed it yet, so, usually I feel like… Once a PR gets one approval.
people are more willing to take a look and stamp, but if we're still talking about it next week, or in a while, then I can…
**Reiley** 09:45 Yeah.
**David Ashpole** 09:46 Ask for.
**Reiley** 09:46 Okay, yeah. Now let's move to the next one. I think this one is related to a previous OTAB which got merged, that's the process contacts, and both were driven by the same set of folks, and the goal is to have those contacts that can be used by For fighting sick, that's the immediate goal, but it's designed in a way that it can be used by anyone.
So should we take the previous, like, the process contacts one, and just assign the same set of folks?
**Tigran Najaryan** 10:21 We… we… I think we decided not to do assignments for OTEPs, but we want to do that.
**Reiley** 10:29 I don't.
But this one needs some attention, so just iFi.
**Jack Berg** 10:38 Yeah, I think that's probably the takeaway, is that, you know, this has not gotten any attention from TC, so… or maybe… has it? Maybe I misspoke there, but we should give it a renewed attention.
**Tigran Najaryan** 10:51 Yeah, what we should probably suggest to do is that whoever did the review of the process context, OTEP should also take a look at it, not at the new one, because they are.
**Reiley** 11:01 Yeah. Quite soon.
**Tigran Najaryan** 11:02 In some sense.
**Reiley** 11:04 Yeah, so a lot of us, hopped on the process context. The threat context, I guess… I'm just trying to be lazy there, because I want the profiling seg to debate among themselves, and once they agree, I'll review, because I… I think it's still, like, very early stage.
Ordin' this.
**Josh Suereth** 11:20 I think… I think they actually had all those debates, Riley. I mean, I haven't been to the Provine SIG in, like, a month or so since Tigran and I switched, but they, like, we talked… I… I remember talking to them about the thread contact sharing one in the.
**jmacdonald** 11:32 Good ones.
**Josh Suereth** 11:33 I think they've been hashing out that discussion. I… Yeah. We can go check the notes, but I don't think there was a lot of.
**Jack Berg** 11:44 So, Josh, if it's already hashed out, then they need to signal that they, as a group, agree with this through approvals.
**Josh Suereth** 11:51 Okay.
**Carlos Alberto Cortez** 11:53 Yeah, I think that's the correct way to go.
**Reiley** 11:55 I agree.
**Tigran Najaryan** 11:58 Let me just ping the profiling maintainers for a review.
**Josh Suereth** 12:03 That sounds good.
**Reiley** 12:08 Okay, so we've done the triage.
**Jack Berg** 12:14 Great, let's jump into the agenda.
**jmacdonald** 12:16 Mmm.
**Tigran Najaryan** 12:22 Okay.
So, I guess, system packaging.
I can speak, but I think, Carlos, you said you also had an opinion on this? Do you want to say anything, or you want me to… Talk about it.
**Carlos Alberto Cortez** 12:38 I also wanted to say that, I was reviewing that, I think that makes sense. I still feel that some, Jock… I think it was Florence Jack who said that, that some scope can be reduced for initial, you know.
taking on… I still think that the Phase 1 that they have It's kind of big.
And, I know that there are some concerns, one of them would be, like, reducing the scope even more, you know? I think that could help us To get an idea of… Of how this is working, you know?
And then see whether we need somebody from the FTC doing something more than simply escalating.
**Tigran Najaryan** 13:20 Yeah.
Okay, and I think Jack's concern… one other concern Jack had was about how exactly do we engage the delegates? What does that look like? We don't have a… We don't have a well-defined process for that. I think this… there's maybe… we can use this as an opportunity to do exactly that, right? To try a process of delegating, and what does that look like, and… I, I have a specific suggestion about how we can move forward with this one. We defined, limited scope for Phase 1 for this project, right? A reduced scope.
And what I would like to say is that We can set specific expectations from… the members of the SIG, and… if we decide to delegate to Antoine, from Antoine, on how we want to see the progress to happen, so that we are happy and And making sure that it is set up for success. So, we could probably start by saying, please present your plan in the spec sheet meeting at the beginning of the project. Let's say it's approved, right? You show to the maintainers specifically what you plan to do so that they are At the very least aware of what the work is being done, and… Are aware of the future plans that may impact the maintainers, if the changes are required.
For, for packaging purposes. Then, to ask the NUSIC to make sure they commit to coming to the spec slash maintainer meeting anytime they have.
Anything of… cross-seat concern that the maintainers need to be aware of, and to also ask them to do periodic status updates, quarterly, whatever, right? Something like that. So, establish some sort of a cadence of engagement with the specification and maintainers Meeting periodic engagement.
And, and then I can be the escalating… TC sponsor there, but also we all will have a chance to observe How this particular project that we're doing with delegation works, and if necessary, course-correct.
So that is the proposal I have there, right? So we do… try to… Come up with a good… good way of managing delegated projects, essentially, on… on this particular example.
And I'll take a bit of personal responsibility by being an escalating TC sponsor on this one.
**Jack Berg** 16:08 That sounds good to me. It's like, it's a little bit of a different model than other spec sub-sigs have taken in the past. Other spec sub-sigs have sort of spun up and gone off and worked in relative isolation, actually. And this is sort of a different model with the expectation set up front that they're going to have regular check-ins, regular status updates at the parent spec SIG meeting, so…
**Tigran Najaryan** 16:33 And that's intentional, Jack, because I want to address the concerns that you rightfully raised, that this is… A kind of a work which does require that sort of more… more, I guess, prostate concerns are part of the work that is happening, so we do want that… that extra Visibility of what they are doing, so they don't go away and just do their work. But also.
for maintainers to have a chance to course-correct whatever this SIG is doing. So, a bit of more… regular engagement.
is necessary for this particular project. I don't think we want this to be done in complete isolation, hence that particular way of engagement I'm suggesting.
**Jack Berg** 17:23 Yeah, and I do think that addresses my concerns. Thanks.
**Josh Suereth** 17:27 I'm gonna… I'm gonna ask the elephant in the room question. How is this not… asking Antoine to basically be a TC member.
and have TC responsibilities for this SIG.
requirements of coming to the spec meeting, for example, and just not giving them the title. Like.
That's… that's kind of what this feels like to me. This is… this is even more than what we normally do as spec sponsors.
**Tigran Najaryan** 17:53 I mean, I don't see anything wrong with that. It is… it can be seen as a way for us to prepare new TC members.
Right?
you try part of the job, why not? And just to be clear, this is not something that I'm… saying we should do exclusively with this project, or exclusively with Antoine.
If we find that it works well, it's successful, definitely let's do more of it, right? Let's prepare more potential TC members for the future.
**Josh Suereth** 18:26 Go ahead.
**Jack Berg** 18:27 So, Right now, we have this process where, the… the TC is acting as this gatekeeper of which Which projects we take on, what we do through sponsorship.
And so it's a gatekeeper in… in, like, I guess a good way, in the sense that, you know, we can channel our… our knowledge of all the things that are going on, and, And, you know, provide feedback if the timing is right, if the people are right, things like that. But it's gatekeeping in a bad way, in the sense that, you know, we've explicitly bounded ourselves to 10 people, and, you know, that means that we can do 10 people's worth of sponsorship of projects.
And we've stated in the past that, you know, we have these… these sets of people that, this set of people that are called spec sponsors today, that have been, you know, trustworthy collaborators with… in the spec and in cross-project initiatives a bunch of times over, and that, you know, at least in the context of complex spec issues, we would feel comfortable if they sponsor those and they run with those.
And I feel like that… that, you know, we need to refactor the project process to decouple the TC from being, like, a bottleneck in terms of our bandwidth.
And, like, the way that I see that that refactoring working, at least part of it, is adjusting the sponsorship requirement to be expanded to, like, TC plus spec sponsors.
**Josh Suereth** 20:07 I kinda hear what you're saying. I'm gonna… I'm gonna throw this out there as a possible alternative, like, I think we should seriously consider if we delegate this to Antoine, does a great job with a SIG, like, that's kind of like your founding proof that you're ready for TC, right?
I'm gonna throw that out there. You know, this is… this is what the job that a TC does. But we have this issue where we have leaders who could be on the TC, but we don't have room to add them. And we talked about this a bit last week, we need to sort out… I think OpenTelemetry's going through, and this happens all the time with open source projects, where some of the old guard needs to step down and new guard steps in, right? And so, I'm just gonna be blunt about it, like, I think we need to anticipate that in some fashion. That's coming, that's happening.
So… I… I like… so in terms of the plan, I'm not saying, like, don't do the plan.
What I'm saying is, like, I think we need to, like, what's our follow-through after this? You know, we elevate these sponsors, we bring them in, they're doing the job of the TC, effectively. They're doing what we would want folks to do. We can evaluate that, and I think we should have a path for them to kind of become, you know, leaders and things the way the TC is. And if some of us don't have time to take on responsibilities.
Great. Let's elevate those folks to do it instead.
If we think 10 is not enough TCs, let's expand the number.
If we think that that's the right thing to do, because effectively, that's what we're doing, we're just not being honest with ourselves about it, right? Effectively, that's kind of what's happening here. The coordination headwinds are still there, with delegating spec sponsors. So… I just… anyway, I know it's the elephant in the room. Lyudmilion of your hand up, so I'll stop my short rant. I just want us to kind of consider that.
I'm fine with us going forward with this proposal, I just want us to ask, what's next?
**Tigran Najaryan** 22:14 Yeah, just to quickly reply, I think, yes, you're right, and I think it's fine, right? I think it's a good thing, not a bad thing to happen. As for… let's say Antoine does this project and it's successful, does it make him a TC member? I don't necessarily think that's true. We are setting the bar for TC members a bit higher than that. It is not just a single successful project, but it's I guess… repeatedly doing cross OpenTelemetry projects successfully is more of a definition of a TC member, but it certainly puts the person much closer to being, to qualify for a TC membership. I think that's a good thing, really, in my opinion.
Okay, I'll stop here with Milo.
**Liudmila Molkova** 23:04 Yeah, I wanted to, add to this. So, okay, it's the… mental model I have, it's not close enough for us to act, but this is, I think, where we should go, is that we have it in our charter that TC is a set of active leaders in the project, and to a certain extent, it's dynamic function.
We have this documented in our TC charter that it's endless, but we are also active.
I think there's… there is a contradiction there.
And ideally, the TC could be a set of… this is another extreme… a set of leaders who are currently active on important projects, with some gatekeeping to the projects.
But not to the people who drive them.
So I think what I'm saying is essentially what Josh is saying. Can we make TC more… dynamic.
**Tigran Najaryan** 24:08 Yeah, I think it's a topic worth discussing.
It's not necessarily, I think, is a requirement for us to move forward with this.
So… Happy to, I guess, take that as a topic if we want to do it today or any time else, but I really want us to make a call on this one. We either support this, or say we can't, we're not doing it, right? So… I am very supportive of this proposal. For too long, yeah.
**Jack Berg** 24:39 So, Tiger, are you gonna, just to kind of close the loop on that, so are you gonna suggest these adjustments to the project proposal, and, like, basically say that something to the effect of, like, you know, pending these adjustments, like, the TCE supports this.
**Tigran Najaryan** 24:57 Yes, that's what I will do if we agree, or us to do. If we don't agree to do that, I would like to do the opposite and go and tell the GC we're not accepting this project and rejecting it.
It's in limbo, that's what I don't like, right? So let's make a call today.
**Jack Berg** 25:14 Does anyone disagree? Let's just, like, let's take a straw poll. Does anybody disagree with what Tigran has proposed here?
If nobody disagrees, then we agree.
**Carlos Alberto Cortez** 25:28 Yeah, I think we were fine.
**Tigran Najaryan** 25:32 Okay.
Sounds good to me.
And happy to continue discussing the TC membership and the other topic today or any time else, but I think we're good with the system packaging. I'll go and tell what we decided to do to the GC.
although this is, I guess, public, but anyway, to let them know what we decided, and then I will talk to… I can talk to one-to-one, and tell him what I expect to do, so that it is clear to him, and then we will all observe how well this is going in the spec meeting, which we all attend.
**Jack Berg** 26:08 So… So while we're on this topic of, you know, TC sponsorship, TC bottlenecks, TC membership, things like that, and potentially refactoring, you know, these processes, I just want to plant an idea in your head that I mentioned in the TC channel the other day, but, you know, it was in a thread, so it might be buried. And if we're going to do some adjustment to this process, I want to consider the role of maintainers as well. And I want to give them More privileges with respect to deciding where the project goes.
And the reason that I want to do this is twofold. Like, one, the maintainers carry an enormous amount of weight within the project.
They do the types of tasks that the casual contributor does not want to do. They don't want to triage issues. They don't want to review, you know, Dependabot PRs, they don't want to, you know, do security advisory work. They don't want to do the thankless work of reviewing, you know, somewhat AI-generated slot PRs, and just, like, curating the project on an ongoing basis. It's thankless work.
And so they need to be rewarded for that, and I think the way that we reward that for that and recognize that is by, like, formally, in some way, having them be able to vote and have input on the projects that we take on. So, like, if we're going to do some sort of road mapping task.
like, maintainers, what do you think? What are the things that you think we ought to do? And it's not just the GC, it's not just the TC that's influencing this, it's the maintainers in a formal capacity. And the thing that I think that benefits us in some way is it creates a carrot to attract more vendors to, you know, have… have their… to employ people that are, you know, have a goal of becoming a maintainer. And so, it ends up, you know, being sort of a virtuous cycle. And that's what I want to see.
**Carlos Alberto Cortez** 28:11 I think that's something you would… we would probably have to discuss with the GCE, because you may remember that Ted Young had some opinions on this matter, too.
But yeah.
**Jack Berg** 28:21 Definitely that, and I'm talking to Ted and whichever… whatever GC members I can. I'm starting to socialize this idea more, because I'm feeling some… that there might be some timing. The timing is right, where, you know, we're looking at these processes, and so, you know, if we're looking at them, let's… Let's try to incorporate other ideas as well.
**Josh Suereth** 28:45 I love it, man. I think it's a great time, I think it's a great idea.
**Jack Berg** 28:53 Alright, thanks for that.
Unless there's any additional comments, let's move on.
**Carlos Alberto Cortez** 29:00 Yeah, Jim McD, you want to present?
**jmacdonald** 29:03 Sure, yeah, I mean, why don't we just keep the screen, or click into 254, I don't know. I looked at the notes from yesterday's spec sig, I wasn't able to attend. I saw what had been discussed, and it wasn't very conclusive, so I haven't gone back to listen to the video.
do we have, I guess, a position, or are we delegating to Security SIG some sort of, like, policy? I know Riley has a PR open in Security SIG that's sort of related to this question, and I am, you know, still feeling responsible for, like, 18 security advisories in the collector-contrib rep repo right now, and I'm planning to do something about it, but… but I am stepping across, like, an unknown line of some sort if I do. Like, I want to take these 18 security issues.
I want to… after I have triaged them, I do not think they deserve CVEs. I think we just need to improve our documentation. Like, do not let unauthenticated traffic into this component, or you're at danger, like, essentially.
Otherwise, we're just flooding, like, ourselves with security advisories, and that's not gonna help anybody.
At the same time, we had… like, in the collector especially, we have this, like, multiple ownership problem, and so I kind of invented a policy there, which says that I can automatically assign the code owners.
But that leaked… that leaks because we don't have a document or a process to say, we're adding you to a security advisory please be careful not to leak this. You're trusted to keep this, you know, in confidence until it's been patched. We did end up leaking one of the triaged issues last time, and I think it's, like, not a big deal for a single issue, but, like, we need to figure out the right process.
if I did go ahead and run that downgrade security… downgrade advisory tool, I'm essentially taking a private bug report and making it public. I think it's safe for us to do that, as long as, like, the person pushing that button is aware that they need to look over it. If there's anything personally identifiable, or risky to publish, we shouldn't publish it. So there's a contract of, like, a responsibility there. And I just want to know how we're going to make those decisions, if anyone has any comments.
**Liudmila Molkova** 31:32 Remember, there was a discussion from Pablo around making… declassifying these things that you mentioned as non-CVEs right then.
It seems you are aware of it.
**Jack Berg** 31:48 One thing I've observed is that, you know, like, you've got… you've got something like this, like an advisory that's being proposed, and there's this question about, like, whether it's a bug or whether it's a security fix, and it's like, nobody is taking it's hard to reach a consensus. And so, like, when it's hard to reach a consensus because either, like, there's not strict agreement, or because, like, not a lot of participation, what do you do? And I think somebody's got to make the call, and we gotta be okay with maybe getting it wrong, and then adjusting our processes and learning from that.
And so, like, you know, I… I don't know who makes the call. Like, I'm inclined to delegate the authority of the call to the maintainers, because even if they get it wrong, they can grow from that.
And so… but, like, you're kind of wearing two hats, right? Like, so, you know, Yeah, if you make that call, like, in… because nobody in the collector wants to, or can make that call, like, great.
**jmacdonald** 32:51 Yeah, I'm sort of stepping in as maintainer, even though I just have the approver role. I actually think I should propose myself as maintainer at this point, so maybe I'll just do that.
But this goes.
**Jack Berg** 33:03 This actually is related to something else I was saying, which is that, like, I'm a maintainer of OpenTelemetry Java, and I don't have the owner role right now for the OpenTelemetry org, and so I physically cannot make the call on these, like, advisories within the repository for which I'm a maintainer. And that's a problem, because, like, it basically means that, like, the TC has to be the one making the call.
**Reiley** 33:25 Wait.
**Jack Berg** 33:25 fix that.
**Reiley** 33:26 I think you can. If you have an example where you cannot, I think this is something I'll work with folks to fix.
**Jack Berg** 33:34 I do have an example, so I can't share it right now, obviously, but, you know, if we were in a private room, I would share my screen.
**Reiley** 33:41 Please.
Yeah.
The goal here is, once the advisory is filed, we want the, like, we're going to give the control to the maintainers, and we want the maintainers to be able to drive it without the TC. TCA is making the delegation, so TCA is ultimately responsible, but we don't expect TC to do every… like, single work there, by themselves, because the amount of, like, the tribal knowledge is just, like, not something TC can handle.
And then, I think in Josh's PR, like, the one on the next tab, I didn't approve it, and I put my, thinking there, so I… I think, like, having tools is totally fine, but the tool has a… has a hint for the maintainers that they can just run the tools and assign the issue to an independent component owner, and I'm not sure if this is, like.
like, covered by the current process, so if we… we want to advocate for that, I think a process change is required. And I'll explain briefly on that. So… so you have the repo maintainers, and I believe, at least what we try to do, is when people have the advisory file on your repository, you're the maintainer.
they will automatically give you the power, so you will have access, and you can decide what to do there. And… and we hold you accountable. If you don't be… like, if you don't do the maintainer job after a while, we'll do something about it.
But the problem is, you as a maintainer, for some contributor, there are many components, and some components are contributed by a vendor. You just put their name there as the owner. They're also listed on the code owner's file, so they got tagged by the review, but they don't have the power.
They're not necessarily, like, being an owner of a particular folder or a component in a contribute repo doesn't necessarily mean they're an approver or the maintainer of the repo.
then they probably don't have the access. And also, we don't even know if you can just simply delegate that, because people might report an advisory saying there's something super sensitive, and they hint it might be related to XYZ. Then, if you just go and give that to someone that you don't fully trust.
they might just leak the issue, right? So, we want the maintainers to make their judgment That's my concern. So, so, like, the… The component-level owners, they don't have the proper access, and we don't have the delegation model right now.
**jmacdonald** 36:12 Here's the way I would ask the question, then. I realize that there's, like, a discretionary, like, moment where the maintainer is responsible for assigning the advisory to someone else.
am I expected to go to Slack and ask them first, or, like, use my judgment to make this call? Do I know them or not? Maybe whether they're responsible or not?
because at 18 of these, like, I'm not gonna do that. I'm not gonna make 18 Slack threads, and I'm not gonna go chat with 18 people.
**Reiley** 36:42 Yep. Or more.
**jmacdonald** 36:44 I need to use a judgment, and then maybe a tool can do it for me. That was helpful to run the tool, but, you know, it could leak a lot of information.
**Reiley** 36:53 Yeah, so previously, at least from my observation, I think Armini and I have done it a lot by just, like, rallying the maintainers. Sometimes we just, like, reach out to the maintainers on Slack, and… and I… I did this maybe, like.
like, 50 times, and I think it's a very bad thing. I will try to avoid that. I'll give you the reason.
Number one, when I look for people from Slack.
I saw the same name, but I found 3 entries. I have no idea which one is right, right? I might reach out to Anthony, I believe that's the maintainer, but then it might be another Anthony with the same name, so… so we don't require the maintainers to put the Slack information in their, like, profile or something. So… so this is just guys, and I'm super worried. So each time, like, I try to be very careful and only reach out to people that I know.
And I'll ask them, do you know the other maintainers? Put them in. And this is a very tedious process. And the second thing is, not all the maintainers have Slack. That's what I realized. I pinned someone, and they told me, I don't… so we don't even require the maintainers to have Slack.
**Liudmila Molkova** 37:57 fabric, we require everybody to have Slack.
It's part of your membership, hotel membership application.
**Reiley** 38:08 Maybe yes, but I've seen the cases where I couldn't find the folks, and either because they don't have Slack, they told me, and they created a Slack, or they just told me they use a very strange name. Like, you can call yourself, like.
**Liudmila Molkova** 38:21 Should we have a registry of maintainers with metadata about these, like, accounts to solve this? But I think it's also what I've seen, that people just don't know, how to do this? Maintainers, I don't know, in comms repo, it's rare for them, where in some repos where the security advisories are rare. Maybe we should have, I don't know, a SPAC call, or record a demo, write the blog on… for maintainers on what to do.
Like, more approachable than spec thing.
**Reiley** 38:52 Yeah, so one thing I was thinking, we have this, like, GC and TC reach out, so if you're a sponsor of a certain SIG, then you will be added to a private Slack group, where all the maintainers are there, and you as a TC member will be there.
So if they have any questions, they can discuss with you. I figure that's probably a formal thing, and you don't need to, like, spin up a different Like, so for… for the TC members, I would suggest maybe, like, have all the TC members joining that, like, SIG group, then you can just, for example, you have Profiling SIG, then you can go… go to the Profiling SIG maintainers group and say, hey.
like this one is not getting attention, I need your help. And… and you also give it, like, make it readable for the next TC member who's going to be on rotation.
Currently, it's just horrible, like, I… I can't ping, especially on the collector, I think that the contributory has a lot of maintainers, I have to add all of them, and then when I talk to them, I realize it's already Friday next week, someone else would be there, so I have to add people, and it's just, like, keep creating more and more Slack groups.
**jmacdonald** 39:57 We do have some Slack automation starting to happen. I know, some of the GitHub actions are posting to Slack these days. I had… I was surprised at how little information you can get through programmatic APIs for security advisories. It looks like they kind of restrict the surface area to keep you from accessing exactly the comments and such. So, I don't know what's possible exactly, but I could also imagine us trying to script, like, a maintainer engagement routine where you say, for this advisory, please look up the code owners, figure out their slacks.
Slack them in a temporary room automatically to discuss the issue.
I feel like that would get me involved much more as a maintainer, because Going to the advisory page itself is, like, quite a lot of work.
Okay, maybe that's the tool I should have written.
**Reiley** 40:59 So one thing, I can follow up, if that's something we agree, is to have the maintainer's name not just listed on the repo, but also have their Slack accounts listed there. I don't know if there's privacy concerns, I… I don't think so.
**Liudmila Molkova** 41:19 Slack is public.
**Reiley** 41:21 Yeah, so one thing I can do is I'll have all the TC members, like, listed, and then I'll bring that to the next maintainer's meeting, and ask them to do the same, and explain the reason, yeah.
I think it should be straightforward. I… I don't imagine we need to have a big discussion with all the GCNTC members.
**Liudmila Molkova** 41:44 There might be even some Terraform automation that can populate.
Banford repo, at least.
**jmacdonald** 41:51 this week's.
**Liudmila Molkova** 41:52 Of maintainers and approvers.
**Reiley** 41:55 Okay, so once we have.
**jmacdonald** 41:57 this registry of Slack handles, it seems reasonable to imagine the automation I just described. That doesn't sound like a tremendous amount of work.
**Reiley** 42:05 Okay. Then one interesting thing is, if you look at the admin repo, I think we've captured a lot of information about how the org works, except for maintainers.
like, for maintainers, we still use the GitHub, like, UI or some, like, CLI. We don't maintain that information as a JSON or YAML, like, structured data.
And I remember there was some, like.
it's by design. It's not like we don't want to do this.
**Armin (Dynatrace)** 42:41 Do you remember why it was done by design this way?
**Reiley** 42:45 I, I, I, I remember sometimes, like, it's like a… A security concern, we have some, like, private repositories that people don't even see. We keep those information in the admin repo. All the maintainers will be able to see that.
But I can double-check and see if it's the right time to do that.
**Armin (Dynatrace)** 43:09 Okay. I thought that you were talking about, like, membership of, individuals in the maintainer teams, because that would be independent of repos, right?
**Reiley** 43:21 Yeah, so we have an admin repo, and we maintain a lot of things there, but when it comes to… for each repo, who are the maintainers, that information is not in the admin repo. And I think we tried, we explored that, and we decided We're not going to do it.
**Jack Berg** 43:37 I'm actually trying to fix that right now with an effort with Pablo and the community repo. We're refactoring how we model and capture, you know, our system of record for SIGs, and included in that is going to be, like, a formalization of what the maintainer group is.
for each repository.
So, you know, for all the… all the SIGs will have associated repositories, and the SIGs will have associated maintainers, and so, you know, the relationship will be there.
Yeah.
**Reiley** 44:14 Okay, so long story short, Josh, for your PR, I think my only concern there, and this is why I won't approve, is I don't want the maintainers to just delegate things to random people there, because they have a name.
**jmacdonald** 44:28 Yeah. I will close the PR. I will… Sign myself up either to write a new issue saying, we need a better automation for, contribute repositories with sort of code ownership, but not maintainership.
It might involve Slack automation, but it does… We're sort of needing to raise the bar as far as accountability for code owners in these contribute repositories somehow, with the help of maintainers. Right. Yeah.
So I don't know exactly what I can do to help, but I wouldn't mind talking an agent into a Slack automation.
So, as I see you writing this, I think the idea is that we're gonna put a paragraph or two or three into the security SIG documentation on maintainer responsibilities, especially to address this code ownership question.
**Reiley** 45:33 Yeah.
**jmacdonald** 45:34 Okay, I can do that.
**Liudmila Molkova** 45:37 And we do a master class for maintainers and also community on how to… what we should expect, even if it's written down. I think it would be helpful if we had it recorded.
**jmacdonald** 45:52 You mean, like, a sort of, like, introduction to security advisories for maintainers?
**Liudmila Molkova** 45:57 Yeah, like, during the spec call, I don't know, 20 minutes, like, part of the security seek, very handy, something you can send people to rewatch if they have never done it as maintainers.
**jmacdonald** 46:11 I see.
That's a good idea.
Alright, well, I think we've, finished this issue.
**Carlos Alberto Cortez** 46:27 Okay, do we have anything else? We still have 14 minutes.
**Jack Berg** 46:36 Any OTEPs that we need to go back and spend time on?
That aren't getting the requisite attention.
**Carlos Alberto Cortez** 46:51 I can probably just mention my OTEP again. It has the feedback that people were asking for are just considered as… but yeah, mostly has what people were requesting.
**Liudmila Molkova** 47:04 Context sculpt attributes.
**Carlos Alberto Cortez** 47:07 Yeah, it'll win.
**Liudmila Molkova** 47:08 Oh, by the way, I've been meaning to come to it and share the feedback from Gen AI Isaik. I hope that some of them appeared in your comments, but if not.
It sounds like there is a very large interest for instrumentations to set context sculpt attributes, not just the end users.
**Carlos Alberto Cortez** 47:28 Yeah, that… we discussed that. Yeah, you were not in the call, probably, I think. Basically, we will be allowing this, but this will be an opt-in.
That users have to enable.
Explicitly.
Plus documenting that, you know, this attribute has this cardinality risk, etc, you know?
**Liudmila Molkova** 47:52 Cool, thank you.
**Jack Berg** 47:54 Anyone wonder about that, like, abuse of that type of capability? So, if instrumentation starts using, Contact scoped attributes, and, like.
you know, it's kind of a broad brush, right? The idea is you put these attributes in context, and everything underneath that gets, you know, these attributes get attached to it. And maybe we'll introduce config options that, you know, allow it to be slightly more granular, but, yeah, it's… it's a powerful tool, and I think it should be used judiciously by, by instrumentation, and my feeling is, like, hey, if it's all the same, just, like.
Propagate that context to your instrumentation, and have that instrumentation independently record the same data to your spans, to your metrics, in the places that, that, you know, the same sort of attributes need to be represented. Essentially, don't abuse context-scoped attributes as syntactic sugar to do this thing that's possible otherwise.
**Carlos Alberto Cortez** 48:59 Josh?
**Josh Suereth** 49:00 I agree with that, Jack. So, for context, pun intended, Census and Open Census, this was, like, the primary reason they existed.
Right? And they are, like, you have to be really judicious, so it's a good point. I also think that, with instrumentation, though, we need to allow instrumentation to do it. Like, the end… requiring the end user to do it means that it's basically not usable.
In practice, a lot of these context attributes that you have to add are decisions made at, like, the RPC layer, the HTTP layer. We need for a set of these things to be allowed.
And I think they should be, by default, even.
if they've gone through rigor and decision making. So, I honestly want to push on maybe… maybe we could do a thing, and Ludmila, tell me what you think about this, where, like, GenAI can judiciously pick, things that would be on by default, and we have sort of a… Centralized place to make decisions about what could be default and what can't?
that we can enforce. Like, I agree with you, you need a central thing. I'm just worried about if it's not on and kind of automatic.
it probably doesn't get used, and then why are we spending time on it? This was, like, my point earlier. So, you have to be very careful with them, but you also need them to kind of just work.
to be usable.
So, I think we need to find a way to balance this, and I would propose that, like, if GenAI says, hey, we're gonna have one context attribute, you know, agent name, agent ID, whatever the hell it is, that we feed through, I was looking through some of the instrumentation in And seeing the context stuff that they did in Python. So, I think there's a couple things that get thrown in there, but whatever we pick, we'd be judicious, you know, one, maybe two.
And things that we know aren't gonna explode cardinality, right? Right. Like, the SEMCOM SIG would make that decision. Are we then comfortable saying, okay, that could be on by default, because it's gone through that rigor?
**Jack Berg** 51:07 See, I think there's… and I want to get your feeling on this… I think we need to differentiate between attributes that are, like.
It's like, there's a difference between convenient and possible.
Right? So, like, if I'm talking about attributes that are well known within the Jet AI ecosystem, I can put those in context, in my own context keys, not the context-scoped attributes, just my own context.
Propagate that information down to the lower levels of instrumentation, extract that data out of context, and attach it to spans, logs, and metrics in the standard way.
That is distinct from a user trying to attach their tenant ID to all of the telemetry that's emitted underneath a particular scope. That's impossible for the user to add that tenant ID.
the instrumentation is… is… it's ignorant of that tenant ID. You can never have the instrumentation become aware. And so, like, that's the distinction in my mind. Is it possible to do… to attach this context, these, you know, Gen AI standard attributes, in a different way?
**Josh Suereth** 52:11 I see what you're saying, whereas I'm actually saying, you know, for the GenAI example, if we want to attach, like, the agent that is taking an action, and we want all the logs to have that ID, like, all the logs that are related to that in context, that's your second scenario, where it's, like, impossible to do that without, like, the instrumentation knowing, I take the ID and throw it in there. And most of the cases where the ID that gets thrown into context, I'm saying.
The instrumentation is the place where that has to happen, unless we're gonna, like, ask users to manually configure this instrumentation.
You know? Or we're gonna expose hooks where we have a new context extraction hook that all instrumentation has to support to expose the ability for you to do this, right?
**Jack Berg** 52:56 Exactly, so that's the type of thing that we… that I don't think is tenable, having some sort of, like, you know, context extraction configuration option for every single instrumentation. We should not entertain that.
**Josh Suereth** 53:07 Yep, yep.
**Liudmila Molkova** 53:08 This is essentially conventions, right? So, for metrics of lower level of instrumentation, we would define the attributes that you are expected to get out of the context called attributes. The rest, we probably ignore, because, like.
Why would we stamp unknown attributes on the metric? For logs, we have a good use case with MDC. It sucks, people run into all sorts of problems, but people know, like.
People use it, still, and this is the thing we can rely upon. Same with fans. I think there are more interesting questions.
how… what is the blast radius? Like, if I'm setting something on… GenESPAN, should it appear on HTTP span? Between instrumentations, between different families of the instrumentations?
I don't know.
Where there are things like user AD, tenant AD, session AD that are application-specific.
And then… Should we stamp them? They are a security concern, privacy concern. I don't know. We need the mechanism, but we will figure out how to use it.
**Jack Berg** 54:23 Yeah, and what I'm sure of is that we need this mechanism, and that we're gonna make some mistakes along the way, and so, like, let's not try to, you know, be too, sort of, like, prescient and, you know, see too far into the future. Let's get something out there, let's learn, and then, you know, iterate.
So, I think, I think Carlos' OTEP, you know, provides that basis already, and yeah.
**Carlos Alberto Cortez** 54:53 Yeah, there will be a lot of work trying to, you know, discuss, like, the actual prototypes, so that's gonna be the fun part.
**Liudmila Molkova** 55:00 We can probably find people interested in building prototypes in Gen AI.
**Carlos Alberto Cortez** 55:05 Yeah.
Yeah, actually, somebody presented something in Python, So we can just continue iterating on that. Also, CEO mentioned… CEO, mentioned that he could do something in Rust, like a prototype, if needed.
**Jack Berg** 55:20 We'll do a prototype in Java, too, because this has been, like, a long time, you know, you know, sticking point for users that just want to take this broad context data, like tenant ID, user ID, and stamp it on everything.
**Carlos Alberto Cortez** 55:33 I have a prototype in Java.
**Jack Berg** 55:35 Oh, great. Never mind then. Yeah, you got it.
**Carlos Alberto Cortez** 55:37 It's very simple, but it shows what's happening, yeah.
**Josh Suereth** 55:44 So… I know we only have 4 minutes left. I just want to briefly mention, we had a private discussion last week. I did follow up on the private discussion. If anyone's curious on what that is, I can talk about it, but we'll… privately. So, let me know if you want an update, I can give it to you.
**Carlos Alberto Cortez** 56:00 Yeah, I could say none of the… yeah, I had forgotten about that. That's a good one.
**Reiley** 56:06 Let's go to the private chat.
**Josh Suereth** 56:08 Okay, I'll give you an update in, like, 5 minutes. Sound good?
**Jack Berg** 56:13 See ya, everyone.
**Carlos Alberto Cortez** 56:14 Nope.
