SIG: Semantic Convention SIG
Date: 2025-09-15
Duration: 66 minutes
Zoom Recording URL: https://zoom.us/rec/share/csgLfBPiJK0hg7VfsnLUZoPFd3cpc25O71oHUdq-3GczG6Zw1WSid2Ky-lOACEs.Qw-3GWr8iVEXctdn
============================================================

## Zoom Recording Transcript

Josh Suereth 00:02:01 Hey, can folks hear me?
Trask Stalnaker 00:02:06 Yeah…
Daniel Dyla (Dynatrace) 00:02:07 Yes, I can hear you.
Josh Suereth 00:02:08 Okay, I'm having a problem where if I turn on my camera.
or use it in any way, my USB hub dies, and shuts off completely, and I lose my mouse and my keyboard, and then after it reboots, my camera comes back on. It's wonderful. So, I'm gonna go cameraless today, I hope you don't mind. I have to order a new one, I guess.
If anyone has ever had a malfunctioning camera that gets really hot and crashes your USB hub, I'd be curious to know if it's fixable.
Yeah, technology, it's wonderful. Alright, So yeah, apologies, I just discovered that this morning.
Yeah, if anyone else wants to run the meeting, feel free, I can just, like, present and take notes and things, that's fine. Just in case I drop.
Alright, with that…
Trask Stalnaker 00:02:58 I mean, I can… share, and… Drive of that.
It's not a problem.
Josh Suereth 00:03:04 Okay, I, I mean… I think I should be fine, but if I drop, do you want to take over? Does that sound good? Oh, of course.
Trask Stalnaker 00:03:10 Yeah, yeah.
Josh Suereth 00:03:11 Yeah.
Alright, feel free to add your name, feel free to add agenda.
And let's do a little bit of triage, shall we?
Trask Stalnaker 00:03:24 Yeah.
Josh Suereth 00:03:26 Okay.
Alright, so we have ready to be merged, take a quick look… oh, non-normative guidance for status metrics needs more approval.
This one, I think… Did I not do this one?
Trask Stalnaker 00:03:43 seeing the right. We're not seeing the triage board.
Yeah.
Josh Suereth 00:03:48 This one here?
Trask Stalnaker 00:03:50 Yep.
Josh Suereth 00:03:53 Yeah, so this is the current plan. I think I didn't… I think I can approve this. Is there anything open here? Braden, you were, is Braden on the call?
Trask Stalnaker 00:04:03 No.
Josh Suereth 00:04:04 No? Okay.
Anyone familiar with the status here? It'd be nice to get this one through. I think there's a couple things blocked on this one.
Just review feedback… Hugo Frontmatter… Yeah, I'm not seeing any open things. Alright, so… looks like we're pretty good. If we can get one more review, I'll take a look at this after the meeting. But yeah, it'd be good to get this one through, because there's a couple things blocked on this. I believe the basic gist is just, you can make, you can make a metric based on an entity attribute as a status column.
Joao G. (Dynatrace) 00:04:46 I think there was, I think there was discussions about, Like, if the… If it's a problematic that the metric name has the same name as the attribute name, but There was already discussions and, yeah, seems all, all solved now, or, all okay.
Josh Suereth 00:05:06 At least we agree on the way forward, yeah.
Joao G. (Dynatrace) 00:05:09 Exactly, huh? Yep.
Josh Suereth 00:05:11 Cool. Alright, needs more approval. App screen name. Does anyone know the status of this guy? Just to make sure this one gets through.
Looks like we have one approval from, front-end folks… We have an issue here… about an ID.
In the event… okay.
Trask Stalnaker 00:05:48 What are these… I'm seeing multiple approvals here, but they weren't showing up.
Let's see…
Josh Suereth 00:05:55 I think they made enough changes that they undid the approvals. That usually shows… yeah, this was reopened last week.
Trask Stalnaker 00:06:02 Okay.
Josh Suereth 00:06:03 Yeah.
So I'm guessing some of those got canceled and then, like, asked for new again.
Daniel Dyla (Dynatrace) 00:06:12 If you close and reopen a PR, does it dismiss all reviews? It probably does, huh?
Trask Stalnaker 00:06:18 No, I don't… it shouldn't. I think I was just… I was just watching the screen fly by, and I think I saw green, circles, but I only see one approval on there. Yeah.
Josh Suereth 00:06:31 Yeah, Lyudmila moved this into needs more approval, so it sounds like this made it past the first wave of, First wave of SIG, and now it's time for, kind of, general reviews. So, I think this one, just, please take a look at, folks, we'll move on. Doesn't look like it's blocked, just looks like it's in discussion.
Oh, update stale action to V10. That's just one we should take care of.
Extend GenAI content JSON schemas with multimodal blob and file data. This one… want to make sure this one doesn't have anything… Alright, yeah, this is approved, this one kind of just makes sense.
Cool. So we can review those too, and then I want to take a quick look at Blocked. We're at 7 minutes here.
Let's go to Oldest first. Is that at the bottom? No, it's at the top now.
Explicit ID for FAS entities… anyone know the status of this one?
James Thompson 00:07:28 There was commentary for the holiday.
Josh Suereth 00:07:32 There's what?
James Thompson 00:07:33 There was feedback the other day which needs to be looked at.
Josh Suereth 00:07:38 Okay.
I also think that the… I'm not sure the FAST SIG is meeting, so I think that one might be blocked kind of indefinitely, if there's anything related to FAST going on.
Their feedback?
Joao G. (Dynatrace) 00:07:52 I think so, because I also looked into it, and I added a blocking comment, because it is kind of breaking the change that is in the PR, so there was already a lot of back and forth in it, and We have this state that it is right now, but after this long discussion.
And this basically kind of more or less reverts to what was before the long discussion. I saw Tyler approve, but yeah, I don't think… I don't think we can't move on with this without a proper SIG stabilization, because a lot of folks depend on the thing that is there today, and if we just merge this, it will be just… Like, a breaking change without any, you know, like, migration path or anything.
it's not that it's not okay to have the braking change, but, just the braking change without upgrading or a stabilization path, I think we should probably avoid that, so that's why I blocked it.
Josh Suereth 00:08:51 Gotcha, yeah, especially if we're making braking changes that rely on existing instrumentation, we need to make sure that the folks who own that instrumentation are participating. That's one of the reasons we have the SIGs. So yeah, I think… I think this makes sense to block until we have folks who are going to, like, provide that transition period and own that code, invested.
Okay.
Cool.
Let's see, as in LMDB.
It's just… it's…
James Thompson 00:09:25 It's… it's the Ruby DBE system that's used.
by the OpenTelementary RubyDB system.
Josh Suereth 00:09:33 Okay.
Yeah.
What's this one blocked by?
Mill, Okay, so it looks like this just needs existing instrumentations and prototypes and naming guidance.
Trask Stalnaker 00:09:55 We're not seeing your screen, Josh.
Josh Suereth 00:09:57 Oh, shit.
Daniel Dyla (Dynatrace) 00:09:58 The triage board.
Trask Stalnaker 00:10:00 No.
Josh Suereth 00:10:00 Sorry, folks, I, I'm a little slow today. Alright, yeah.
Right, so I think there's… there's action items to unblock this, so let's move on.
We'll do one more in our time box here.
What else do we have? Going from oldest to… Right, LMDB, more app details.
James Thompson 00:10:24 Yeah, so recently we added in the build ID in the app namespace.
Right? And that's currently an identifying attribute.
However, if you have two apps with the same build ID, you'd end up with the same entity, so this adds in the name, etc. attributes as well, so that they can form part of the identifying part.
Because having just a build ID as identifying doesn't produce a unique enough Scenario.
Josh Suereth 00:10:56 For it. I see, you mean the entity is not unique?
James Thompson 00:11:00 Correct.
Josh Suereth 00:11:02 Now, are you going for universally unique or globally unique? Because entities only need to be globally unique.
James Thompson 00:11:10 Yeah, right, so if you had two apps producing the same build ID, but were totally different apps, you'd have the same entity.
Josh Suereth 00:11:20 I'll have to look at the details, but I also think, Jason's other concern is important here, where we're trying not to have app and… Service Compete.
We'll have to sort that out.
Where's your model?
So right now, there's an installation ID.
And this moves that to be an installation, right? So, I guess what I'm suggesting is you kind of don't need any of this.
You already have an entity that has the exact same ID as before, right? Wasn't it… it was before it was just installation ID?
James Thompson 00:11:56 No, it was installation and build ID.
Josh Suereth 00:11:58 and build ID. And build ID is…
James Thompson 00:12:01 the, identifying.
Josh Suereth 00:12:04 Right here. Gotcha.
James Thompson 00:12:06 Yep.
Josh Suereth 00:12:13 Yeah.
Alright, I do think that this probably needs to get sorted out, but I don't think adding in name, namespace, version, all that kind of stuff necessarily is right, given previous discussion, so I think this should be blocked on that discussion as well.
what Jason was saying?
So we should probably have a chat with a client SIG and figure out what we want to do here. What I don't want is, I don't want service and app to be… basically mean the exact same thing, but be at odds with each other.
So I think we should resolve that discussion first.
Right? If we're gonna… if we're gonna add in name, namespace, all that kind of thing, we should.
And build ID versus, say, version.
It's unclear to me What would be the difference there in terms of identifying attribute?
And how you track these things. Anyway… I think this one… this one has a bunch of other discussions we need to finish before we can move on.
Okay, cool.
We're out of time box here, so I'm gonna come back to the agenda.
And… let's start doing some of the general topics.
Sorry, I forgot to take notes. I'll take some notes while we do that. First off, RPC meetings are starting Wednesday at 5 PM Pacific.
Feel free to join.
Trask, you're attending those, right?
Trask Stalnaker 00:13:41 Yep, myself, Lanila, James, Steve from Alibaba, and… One other person from Alibaba.
from the Apache Doubo project.
Josh Suereth 00:14:01 Is there anything you want us to talk about there?
Trask Stalnaker 00:14:05 No, not yet, we're just… Doing the basics so far.
Going through the backlog.
I think we actually… we finished going through the backlog last week, and so we're starting.
Josh Suereth 00:14:22 PRs, you'll start to see PRs.
Hmm.
Okay.
Cool.
Happy to read and review those. Alright, there's another one from Lidmilla here. Please review best practice to record full conventions, not just a constant.
Let's talk through this real quick.
Add more guidance on how to define attributes in case… for example, how to approach the system.name enums.
We do not have to be exhaustive.
We can define a constant along with a convention.
is encouraged, and only stable instrumentation needs to document all constants that are used. I think this one is kind of critical. Yao, you had some comments here. Are any of these about the direction, or were they just naming things?
Joao G. (Dynatrace) 00:15:19 I know, it's just… it's just structuring the markdown. I think it's all good.
Josh Suereth 00:15:24 Okay.
Let me, let me just show this. I wanna… I do think talking through this kind of makes sense, So I'll do my best to impersonate Lyudmilla right now, and explain why. But basically, we need to find these enum attributes that could be, like, a bunch of different systems, like MongoDB, MySQL, that sort of thing. It's hard, like, we… don't want OpenTelemetry to be a giant database of everything that exists in the world. That's kind of an impossible mission.
And so what we want to do is document as many of them as make sense, as many of them as OpenTelemetry provides, but also allow people to use the convention, or say, like, hey, I have a database XYZ, OpenTelemetry might not be aware of it, but that's fine, because I can still match the semantic conventions.
and provide an enum for my component, right? Like a constant.
So where we have something like database.system.name, if I have a database that's not in the enum, all the enums in OpenTelemetry are open, meaning I can add a new one to it.
The reason we do that is because if we didn't require eNews to be open, we would never be able to make non-breaking changes to people, especially as anyone invents things on the internet. New databases show up all the time, relatively, and so… This is just encouraging you to kind of understand that. So if you define, like, MySQL-specific, you can treat those enums as, like, a constant for the purpose of your specific.
Yeah.
So, if you have an instrumentation that's doing something, you should document what values you're releasing before you release a stable artifact. You may support undocumented values that aren't in, that aren't in the SEMConv yet. So, if you are abiding by database semantic conventions, you're dealing with a database that's not in SEMConv yet, this opens the door to allow you to make a release abiding by SEMconf, but within a NUM that hasn't fully been documented.
That, I think, is the major thing we have to talk through in this issue, with the rationale behind it.
Hopefully.
Trask Stalnaker 00:17:40 question about… Yeah, go ahead.
Document, does this… I'm reading it as document in their documentation.
Josh Suereth 00:17:51 Yes.
Trask Stalnaker 00:17:52 Versus… Okay, versus… so you could release stable instrumentation using the values don't have to be in SEMCOMS.
They just have to be documented by the instrumentation in their documentation.
Josh Suereth 00:18:12 Yes.
Yeah, that's… that… and again, I'm channeling Ludmilla, so I'm not giving my own opinion yet. I'm trying to… to… to, advocate for what Ludmila's saying here. I think there's pros and cons to this. I think there's… in practice, there's a lot of good things this can do, particularly to open up Folks to just expand instrumentation rapidly.
But yeah, I think that the idea here is… We don't want to have some kind of turn into a giant registry of all the technology that exists in the world.
What we want it to be is, here's the shape of telemetry that lets people monitor databases effectively. If you provide this, there's a whole ecosystem of OpenTelemetry players that will make your life better.
If you need to do something custom, you can always still do something custom.
Right? That's the whole T-shaped API stuff.
But this, this kind of unblocks the community a little bit.
And on… specifically, though, this unblocks open telemetry instrumentation itself.
Trask Stalnaker 00:19:22 Yep.
Josh Suereth 00:19:26 For context, prior to this, we had… we had a line of, open telemetry instrumentation cannot define anything as stable that doesn't exist in semantic conventions.
So this is the big ship. This specific specification line is the most important thing to discuss on this PR.
Cool. Anyone have thoughts and things they want to talk about now?
Trask Stalnaker 00:19:52 Express my thought through an approval right now.
Josh Suereth 00:19:57 I need to think through some of the concerns myself first, because there's… there's a little bit… I have a slight hes… like.
I'm fine with this for the general case. I'm not sure if OpenTelemetry itself should have a higher standard for itself, just because of what we are, but Contrib is a crazy, wild place. And I know that you help manage Contrib things, Trask, so I feel like your opinion's more… More important than mine here, a little bit, but… Yeah.
Trask Stalnaker 00:20:29 Yeah, I mean, it does… yeah, I agree. We should probably even… it's probably even worth taking this to the spec, meeting tomorrow.
Josh Suereth 00:20:39 Yeah.
Trask Stalnaker 00:20:39 Because that was a previous… It does conflict with the previous…
Josh Suereth 00:20:46 guidance.
Trask Stalnaker 00:20:48 I'll add it to the…
Josh Suereth 00:20:50 Yeah, let's take it to the spec, I think I agree. I… I… Yeah, I mean, the main thing we want is… I want to make sure that Contrib is a healthy place in OpenTelemetry. I think that's our primary goal, right?
And there is a thing where if this was not a contribute repo.
they could do this all day long, and it would still abide by Semcov.
So… what's the difference between OpenTelemetry Contrib and the rest of the world? You know, where does the line need to be?
Anyway, cool. We'll talk about that more tomorrow.
Let's come back here. Yao, do you want to talk about the… do you want to take over presenting the triage process? Yao, for context, Yao's been working on making our triage process better. Yao does a lot of great work on our triage process, and I, I'm actually super excited for the changes, so, really… Really looking forward to this discussion. Yao, do you want to take over?
Joao G. (Dynatrace) 00:21:52 Yes, I can share.
So… Alright, So, I put this diagram together. There is, I'm working on some actual text, but this is… A representation of it, and… yeah, so the goal is… That we, yeah, define a triage process, and… we can have… we kind of need to have, or we'll have to have two categories of triage. One would be for, issues and PRs, created by the, let's say, general community.
And the same created by members of ActiveSig. For example, like, now the RPC SIG is starting, so the SIG will create PRs, they will create issues, and… For those, we want to have a more, a more, like, streamlined, triage process, because Yeah, the work is already agreed on, etc, so… This is what I… Translated to a diagram, and… The goal is really to… Ease the process for maintainers and triagers, and also make it transparent for contributors, what stage their, their, issue is, or their PI is, and what they can expect next, and what they can do to speed up things, or… Stuff like it, so… The goal is to, talk about the general case first, so the new issue comes, and we have already automations that Add the… at least the area label in this, triage, needs triage label.
So the goal is that, what we'll do… I don't know, once a week, twice a week, three times a week?
maintainers share the, let's say, burden of… allocated some time to look into this and start the process. So we initially look at things that have this triage needs triage label.
Yeah, and then we start the engagement with the author, to find out things, and I may… I may modify this a little bit, but… Just to cover the case where they auto-creates the issue and it never comes back, so we have a path to auto-close those as well. So that's the… with the left… left-hand side here.
Shulz?
But… Thinking about, okay, we… we talked a little bit, we clarified, so then the… The triage process reaches some conclusion, and the conclusion is, okay, we need more clarification on it, and then it starts with this triage and deciding.
Community Feedback, label.
So this, this… Kinda… Means that, for example, we need more real-world use case, we need design proposals, maybe even prototypes, or things like this, so we… Label the issue with this.
with this, while discussion is… is happening, and then after, for example, discussion… discussion happens, and And things like that.
Two things can happen, so either we say, okay, this is not for right now, it doesn't align with the roadmap, or we don't have enough people to work on it, or there's not much interest, so this is put into a new thing now, a backlog, so we'll add issues to… To this, this label will be at… to the issues where Marks into a bucket of issues that… are pre-accepted, more or less, they have all the information, they pass through all the initial checks, and… but just needs people to work on it. And this, of course, then, once interest picks up again, it goes back to the flow.
And then it can continue.
So what the other thing can happen is, if Isha goes through this and… Usually, in this case, it would be large in scope, or… Breaking change or not Trivial?
Trask Stalnaker 00:26:06 for a sec.
Joao G. (Dynatrace) 00:26:07 Sure.
Trask Stalnaker 00:26:08 So… Maybe could you zoom out? I didn't quite… from the community feedback…
Joao G. (Dynatrace) 00:26:16 Yep.
Trask Stalnaker 00:26:17 How do we get to… Oh, I see, that's an alternate, needs clarification, no backlog. Yeah.
Joao G. (Dynatrace) 00:26:27 Yeah, so maybe let's go to the, overview like this. So, if, for example, we… We see that the issue, for example, is small in scope, just typo formatting, or… or it's a bug, for example, it immediately can be received… can receive the triage accepted ready label, meaning that work can start immediately, or in the case it's created by a SIG, for example.
Also the same, so it receives this accepted ready with SIG label, and, for example, can be already added to the project board of the SIG.
So these are, let's say, the happy path, easy.
Trask Stalnaker 00:27:05 Yes.
Joao G. (Dynatrace) 00:27:06 So this is, like, the streamlined version for when there is already a SIG, or the SIG member creates the issue, or it's, yeah, small in scope of typo.
Yeah.
Trask Stalnaker 00:27:15 Okay.
And there's that…
Joao G. (Dynatrace) 00:27:21 Sorry, go ahead.
Trask Stalnaker 00:27:23 Oh, I thought… I think Dan had a question.
Daniel Dyla (Dynatrace) 00:27:25 I was about to say something, but Trask… I was deferring to Trask, it sounded like you were gonna talk. I was gonna ask why you go from accepted to community feedback, rather than one of the other accepted categories.
Because the only way to get into… community feedback.
Is if it needs clarification.
Or, if it doesn't need clarification, goes dormant, and is revived again.
Which seems like two weird paths to me.
Joao G. (Dynatrace) 00:28:00 No, so if it doesn't need clarification, it either goes directly to the accepted, label or the accepted with SIG, or it goes to the backlog as well, because there's.
Daniel Dyla (Dynatrace) 00:28:10 Right. So I get that, but why backlog accepted? If interest picks back up? Why does it go to community feedback rather than to one of the other accepted categories?
Joao G. (Dynatrace) 00:28:22 Yeah, I guess this can be debated, because my idea was that, like, it needs to be, like, discussed, I don't know, like, for example, the issue is one year in the backlog, and then, I don't know, needs to pick up discussion again, or it needs to present more use cases, or things changed, so just a way to say that it needs… to kick up… kickstart a discussion again. It can be maybe just directly to… to one of those, I'm open to.
to change.
Daniel Dyla (Dynatrace) 00:28:51 Yeah, I would say almost it should go back to, like, the beginning of the flow, rather than into community feedback.
Right? Should go back to… go back to, like, needs clarification, question mark, or something like that.
Joao G. (Dynatrace) 00:29:06 Yeah, that can be… I can change that, that makes sense, yes.
Trask Stalnaker 00:29:14 And so the reason it doesn't go straight to… Need SIG?
I guess that… my question is, why doesn't it go straight to, no, but not urgent or planned? Why doesn't that go straight to needs SIG? What's this backlog? What's the difference between backlog accepted and accepted need SIG?
Joao G. (Dynatrace) 00:29:46 So yeah, so I put this little text here. So the reason when this goes directly to the backlog, it's because basically, like, yeah, it makes sense, but, like, we discussed this category of issues that we think it's a good idea, for example, I don't know, some instrumentations for some What was the other thing that happened the other day? They suggested some, But it was the energy consumption or something. So there was some topic that came, and it's like, okay, this makes sense, it looks good, but, like, it's not priority right now.
So, it could either go… either go knit-seq, Or go to the backlog end. Yeah, I thought about introducing this new bucket of things that… Just, is there a park there? There are ideas, more or less?
And then there would be a step before into… before it needs a SIG or something.
Daniel Dyla (Dynatrace) 00:30:41 Or we could also do the same.
I had kind of the same question as Trask. The only way to get into Needs Sig as well is, like, kind of a convoluted path.
I would say from needs clarification, I would say your no, it doesn't need clarification are good, like, small in scope, or coming from an active SIG.
But then I would say… no, not urgent just means there is no SIG working on it, because if there's… if there's a SIG working on it, then it is theoretically urgent. And if there is not a SIG working on something, then, you know, it's not urgent. I… I would merge those two… categories together, probably. Accepted and needs SIG.
Trask Stalnaker 00:31:32 Yeah, there might be some subtle differences, Yao, but I…
Joao G. (Dynatrace) 00:31:36 I think, potentially, the simplification.
Trask Stalnaker 00:31:39 of just going straight to need SIG might be worth the, you know, the… Losing a couple nuances.
Joao G. (Dynatrace) 00:31:49 Right, right, yeah, Josh, go ahead.
Josh Suereth 00:31:54 Yeah, yeah, to… I think… I think this all makes sense. Yeah, I think the thing you were trying to do of having a backlog for things a SIG doesn't want to deal with yet, we can let the SIG figure that out, and if we need to create a label, like, on the right, like, after something gets to a SIG, for them to have a backlog.
Or take a bunch of issues and say, no, we're not gonna work on this. Like, that… just send it to the SIG, let the SIG make that decision, and, like, that… that process should kind of be on the right. So, like… Yeah, that… I like what you wanted to do there, but I agree with everyone else. It'll be a lot simpler for triage if we have simple yes-no answers, right?
Trask Stalnaker 00:32:29 Okay, so…
Daniel Dyla (Dynatrace) 00:32:30 And I think this…
Trask Stalnaker 00:32:31 codes.
Daniel Dyla (Dynatrace) 00:32:33 I think the SIG can also just, like, close these, too. Like, if something gets accepted and into the SIG, and then the SIG says, actually, we're not doing this, they can always just, you know, shortcut the closing process.
Joao G. (Dynatrace) 00:32:44 Yeah, when there is a SIG, that's fine, but it's just the point where there's, like, no group.
Trask Stalnaker 00:32:50 just because it says accepted needs SIG doesn't mean that the SIG, once it's formed, is going to accept that particular.
Joao G. (Dynatrace) 00:33:00 Right, right, no, no, that's…
Daniel Dyla (Dynatrace) 00:33:01 Yeah.
Joao G. (Dynatrace) 00:33:01 That's clear, yeah. Okay, so I can merge the… I can basically delete the backlog thing, it's simpler, I agree. And then… If it doesn't need clarification, go to record to need SEC.
Because we already have the other thing that comes directly from the sequels directly to the other, yeah, that's fine.
Daniel Dyla (Dynatrace) 00:33:19 And then from the backlog goes to needs clarification, and sort of loops back to… Kind of the start of that process.
Joao G. (Dynatrace) 00:33:27 Yeah, but the… won't I… won't we just discuss that I basically don't need the backlog?
Daniel Dyla (Dynatrace) 00:33:34 Oh, yeah, because Sigma…
Joao G. (Dynatrace) 00:33:36 Pick it up.
Daniel Dyla (Dynatrace) 00:33:37 and provide any needed clarification in their own SIG process.
Joao G. (Dynatrace) 00:33:41 Yeah.
Daniel Dyla (Dynatrace) 00:33:42 If something becomes very old, when the SIG picks it up, they can determine whether it needs…
Joao G. (Dynatrace) 00:33:47 what I… what I do need is here that I… I don't have it then now it's, like… like what we discussed, right? The SIG, once it… once it has this label, and then, I don't know, a SIG pharmacy, they say, oh, no, we don't want to work on this, then I have to have a path to rejecting it. It's not encoded here as well.
Okay.
Trask Stalnaker 00:34:04 Yeah.
Josh Suereth 00:34:04 One… one other thing, y'all, the, PR opened without issue, and then is closed with triage, rejected, declined. Make sure that Renovate and, Dependabot can still open PRs.
Joao G. (Dynatrace) 00:34:18 Yeah, sure. We had to find a way to exclude those users, yeah.
Josh Suereth 00:34:22 Yeah, so as long as we still get our version bumps, I think we're good.
Joao G. (Dynatrace) 00:34:26 Sure, yeah, no, I think… I think we can… we can work around that. Yeah, so the… Alright, so… Yeah, maybe I also have to think a little bit. I think that was… what happened was that I… I was… I was looking into the one that was… Spec'd out, or there's this issue in the spec that has this community.
Let's say, flow, and… I kinda… I kinda like that, but maybe it doesn't really fit you, so I'll rethink this a little bit.
Yeah, but the idea is this, right? So… something… people propose stuff, and then either it's large in scope, and then we would need a SIG, and this is their part until the SIG is formed, and… Then once the SIG is formed, it's picked it up, and labels change, and… goes to this, ready with SIG, and to the project board, the same as the one that's created by them directly.
Yeah, and then a PR is… at some point, PRs are issued towards the… the linked issue, and yeah, review, and then we have the normal flow. So either PR is merged, issue is closed.
or for some reason, the PR is… Unmerged and closed-end.
Either because the PR is going through a direction that's not accepted, or stale, or something else.
Yeah.
And the thing that we discussed in the document, or, like, in this Google document that I'm working, is about this on the right side.
PR opened without an issue, and Ludimila had a comment that, for SIG specifically, it would add to their, work that they, for example, always need to have an issue open before opening up PR.
I don't truly agree, because I would… try to… or I would prefer to avoid having distinctions in… in, like… because if we were gonna build automation for it.
this would be another fork of the decisions, like, is this coming from a SIG? Then I don't need this rule.
And I looked, for example, the Kubernetes SIG and the system sync, they are doing at least the ones that I found out, the PRs have linked issues to them.
and the issues are also added to… as a planning on the project board, for example.
So I don't think it's… it's too much. It's not adding too much to the… Workstream, especially because then… They… it will create the issue and immediately add the correct labels, because it's… it's cutting all this… complicated, flow here, so… yeah, I think… I don't think it's adding too much, and I'd prefer to keep the same process consistent.
Meaning that the PI always, always, always have a linked issue, that's the thing that I want to have.
Daniel Dyla (Dynatrace) 00:37:16 I think I don't necessarily agree with that, because there's a lot of, like, if you think about fixing typos and such, it adds a lot of overhead to, like, those small things.
I think there should be.
path to make quick PRs without an issue. Maybe it's just, like, if you put no issue in the title.
Trask Stalnaker 00:37:34 Sure.
Daniel Dyla (Dynatrace) 00:37:35 Yeah, chore, something like that.
Joao G. (Dynatrace) 00:37:39 Yeah, yeah, no, we have that already, but yeah, maybe for really small things, but definitely not for any… like, any adding attribute or anything like that, or change anything, I don't want to have value, but yeah, sure, maybe just, yeah, docs or whatever.
Daniel Dyla (Dynatrace) 00:37:53 Yeah, I agree.
Trask Stalnaker 00:37:54 automation… Workflow.
Joao G. (Dynatrace) 00:37:57 I'll try to add that. But, I think I don't need to encode that in the diagram, but of course, doing the automation, we can make that a little bit more flexible.
Yeah, so the idea is this, and also to… sorry, go ahead, Trask.
Trask Stalnaker 00:38:16 You could say non-chore PR opened.
Daniel Dyla (Dynatrace) 00:38:19 Yeah.
Joao G. (Dynatrace) 00:38:20 Exactly. Yeah, yeah, yeah, I'll add this.
Trask Stalnaker 00:38:22 On the diagram, just to be clear that we're not being… that.
Yeah.
Joao G. (Dynatrace) 00:38:28 Yeah, sure. I'll add that, yes.
Josh Suereth 00:38:32 Let's make sure the chore thing doesn't get abused, though, too. Like, we don't want people just saying, oh yeah, this is a chore, and yeah.
Joao G. (Dynatrace) 00:38:40 Yeah. And by people, I mean probably me.
Josh Suereth 00:38:43 But…
Daniel Dyla (Dynatrace) 00:38:43 Yeah.
The maintainers just closed the door. Sorry, this isn't a chore.
Trask Stalnaker 00:38:48 Yeah.
Yeah, let's just define chore for, like, not touching any YAML files, maybe?
Yeah, yeah.
Joao G. (Dynatrace) 00:39:00 But even that, like… like Dan said, I can… I can fix a typo in the YAML that will fix the markdown, so…
Daniel Dyla (Dynatrace) 00:39:05 Yeah, I think it's… I'm sure is a you-know-it-when-you-see-it type of thing, right? That this is some level of discretion given to the maintainers to just say, like, sorry, this does not qualify.
Joao G. (Dynatrace) 00:39:17 Yeah.
Yeah. No, I'm sure we can… we can, arrive at some good spot there, so I'll… I'll definitely think and… and put… put this here.
Daniel Dyla (Dynatrace) 00:39:27 There's also two spots in this diagram where… Something is closed, and then potentially goes into another state.
One thing I would point out is that, like, you have author object from closed with label triage rejected.
A lot of times, notifications on closed issues just go nowhere. Like, they're lost in the ether. Like, if you close an issue and somebody comments on it and says, hey, why did you close this? It doesn't even show up in the notifications for, like, a lot of people.
A lot of, you know, depending on your settings, that may not be effective. So… I think… Maybe a better way would be to just reopen a new issue, and then if you reopen the same thing a few times, tell somebody just, hey, this is obviously not going to happen, so stop doing that.
Joao G. (Dynatrace) 00:40:29 bomb.
Yeah.
But then a new issue can also be… hidden into your myriad of notifications, though? Isn't it the same notification?
Daniel Dyla (Dynatrace) 00:40:39 But at least it's in your notifications.
Joao G. (Dynatrace) 00:40:42 But if.
Daniel Dyla (Dynatrace) 00:40:43 If you…
Joao G. (Dynatrace) 00:40:43 on it, it should show up in your notifications as well.
Trask Stalnaker 00:40:48 I get comments on closed issues in my…
Joao G. (Dynatrace) 00:40:51 Notifications.
Daniel Dyla (Dynatrace) 00:40:53 Only if you are watching the issue, though, which I guess maintainers would be.
Joao G. (Dynatrace) 00:40:58 Yeah, yeah, we are all automatically watching everything as this… as we are part of this team user.
Yeah, I also get notifications from all the closed…
Daniel Dyla (Dynatrace) 00:41:11 Okay.
Joao G. (Dynatrace) 00:41:11 So… I guess it's fine, I just wanted to make sure. Yeah, it's just hard because I sometimes miss them, because there's so many. But, yeah.
Potentially, we…
Trask Stalnaker 00:41:24 I mean, yeah, Zhao, maybe the solution there is when we do triage.
If we can have a query that basically tells us, hey, somebody commented on.
Joao G. (Dynatrace) 00:41:38 Yeah, it's just a… it's just a normal, updated desk, filter.
Or a sorting in the… I think it's the default.
Like, if you open the issues page view, it already shows the… updated, like, the most recent updated one. If, like, say, the alter comments back after it's closed, it will be at the top of the…
Daniel Dyla (Dynatrace) 00:42:01 Yeah, but if you comment on a closed issue, it won't show up in the issues view unless you specifically…
Joao G. (Dynatrace) 00:42:08 Oh yeah, we have to remove the closed filter, yes, yes, for sure.
Exactly, yes.
Yeah, we just have to… that's a good idea. Maybe we should also put together with this a query for triaging.
Daniel Dyla (Dynatrace) 00:42:23 Yeah.
Joao G. (Dynatrace) 00:42:24 inquiries. Yeah, okay, that's a great idea.
Cool.
We have, have to watch… watch for, watch out for that, yeah.
Trask Stalnaker 00:42:35 Yeah, because I think part of the… the goal here for me, like, that would help me a lot is to not need to rely on. The notifications for SEMConv Repo are very voluminous, and I struggle to keep up with them, and so, actually.
like, to have this process where we can, instead of relying on push for getting these things, we can go and pull and be like, okay, I'm gonna spend, you know, half an hour doing triage, what's the list of things I should be doing?
Joao G. (Dynatrace) 00:43:09 Yeah, yeah, that's what Ludimila and I talked, that we should have this at some point at the beginning, we can have it Synchronous, like, together, and then once we have, like.
Figured out a good process, then we just do it, and then document it, and we do it.
Right, so I don't want to consume all the time, so the… the other thing also that will be, like, a side effect of this is the documentation of all the labels that we don't have today.
So there will be, like, a… envision, like, a page where we have the triage process encoded in text, and also this image, and then which label All the labels there, and what they mean, so the… so the contributors know what… what that status or what the label means for them.
Also along with the, like, the roles and the responsibility.
like… What triageers are supposed to do, and maybe also encode these queries there, so triageers know what to use for doing triage and so on.
Stuff like this, and… So, so the… the next steps are, I will… I will flush out the details here, and… Probably start… opening PRs to… to add the… at least add the documentation, add this there.
and then not enforcing it, yet, and then start building the automation, because, you know, we have to figure out… Ludimila wants, or had some ideas about Copilot.
I'm not entirely sure if everything there will work out, so maybe we'll start with manual scripts. I don't think it's too hard to automate via some scripts, so… And then maybe later we can use the Copilot to do some more, more, more work for us.
Trask Stalnaker 00:45:00 What I've seen, there's some, GitHub… Actions that will help you… that will, like, automatically label… they'll attempt to label issues.
Based on categories, so you can give it your list of categories, and it'll, you know, do inference on trying to figure out the best one.
Joao G. (Dynatrace) 00:45:23 Yeah, I have to look into those. Yeah, and then the… I'd say last step is, or some step in below this is I want to polish a little bit the boards that we have, like the triage board that we have today, because I think they're good, but I think there is some states that are missing. So after this is done, we agree on, you know, like, these labels and the process, and then I… I kinda… Kind of want to change the board a little bit, so each of these buckets are reflected in the board, and we can just… Also use the board for triaging.
Yes, I think that's… that's it, what I had to present today.
Josh Suereth 00:46:11 Awesome.
Trask Stalnaker 00:46:12 Yeah, that's great.
Josh Suereth 00:46:14 Yeah, I look forward to this being implemented.
So… Sweet. Let's, I think we have one item that got added to the agenda, so… Let me… Let's go back to sharing… And we'll pop this one up.
Okay.
Alright, increased consistency of general signal docs. Do you want to talk through this one, James?
James Thompson 00:46:45 Yep. So, when I've been looking at the documentation, there's been a couple of different patterns for documenting the General signal pages, right?
So, what I've done is tried to… Encapsulate that in a common approach.
Right? So that when you're looking at a profiles page, it is similar to if you're looking to an events page.
So, Luke LaMella's comment was before I went through and refactored it.
Josh Suereth 00:47:13 Okay.
James Thompson 00:47:14 Right? But effectively, you have a common structure where you go to whatever signal page you want, you have some general information about it.
You have a list of useful namespaces that you can add to it.
And then you have any compatibility that's defined for that signal.
Because currently, I think things are a little bit split up across the place.
Josh Suereth 00:47:42 Yeah, so one thing I'll say, based on our previous… this is not a chore.
Yeah, this is definitely, like, a feature restructuring, so this needs review. So, I think we're gonna have to be more careful about the use of chore.
Going into the new process.
But yeah, let's… so let's take a look.
What's the best… what's the best way to look at this? Should I look at a specific file and then go from there?
James Thompson 00:48:09 Yeah, so probably look at the trace file, for example.
Josh Suereth 00:48:12 I was… well, you…
James Thompson 00:48:13 Yes.
Josh Suereth 00:48:14 Okay, so General got changed, right? And then go into spans?
James Thompson 00:48:19 Yeah.
Josh Suereth 00:48:20 Okay.
James Thompson 00:48:24 Alright.
So… Yeah, I've left those lists of all of those namespaces up above, so if you look up… I don't know.
How well those lists are maintained?
So, but I've just… that's pre-existing.
Alright? But it's the useful additional attribute namespaces. So I've gone through identifying what namespaces are useful for providing additional context. So it's your It's your thread details, it's your code.
And then that takes you straight to the attributes definitions.
And I've brought in… the attributes.
Josh Suereth 00:49:04 This goes to the attribute registry, though, not to… gotcha.
James Thompson 00:49:08 Crap.
Josh Suereth 00:49:12 I think what Luna was talking about, and I think this is… this is the thing, these are… these are useful attributes, but it's… we don't necessarily want to drive you to the namespace, we want to drive you to some kind of a group that represents those attributes as a… as a structure. Like, we… we don't have a way of modeling this in SEMCOM. Like, code… feature flag, I think, is different, honestly. I don't think that's a… I think there should… there should, or there is, Daniel, you can correct me if I'm wrong, yeah, there's… there's literally feature flag docs here that you should go to, to talk about feature flags. Like, that should go to this README.
To talk about how to do feature flags overall. But code, peer, thread, those are ones that are… they're not spans.
They're not events, They're not entities, they're not logs, but they're something.
that can get attached to those things, and we don't have a name for these things yet. And what we don't want to do is make it appear like the attribute namespace is the end-all, be-all. We want to have Like, we're trying to move around signal-based structuring and signal-based understanding, and so the problem with going to the namespace is everything in code will show up, not necessarily, like, a cohesive whole or a description about how to fill it out.
So, I think I agree with Lyudmili here, is I don't think this has actually answered the fundamental question, that was raised. Basically, you know, this goes to code, this goes to the attribute namespace of code.
What's missing here, though, is, sure, this is a collection of attributes, but when do I fill out these attributes? Which ones do I fill out together? Which ones are needed for good observability, and which ones are optional?
And… and then how do they work cohesively, you know? I don't know if you've seen some of the error reporting stuff, where code stack trace and Error Stack Trace and Exception… no, it's Exception Stack Trace. Code stack trace and Exception Stack Trace, how do they interact together? Like, we need… we need a place to talk about that.
And that's why we actually have, fundamentally, a registry, and then the markdown, is because we started from the markdown, where we want to have more, kind of.
combined, you know, globbed discussions. And the registry, until we have a way of modeling and denoting that work.
The registry is an augmentation Of the rest of the markdown. Not the sole source of truth.
Trask Stalnaker 00:51:44 Lyudmila was sharing last week, separately, about Weaver and Schema V2 stuff.
Josh Suereth 00:51:55 Yeah, let me pull that up. Based on…
Trask Stalnaker 00:51:58 Yeah, and I think… some of Josh, you, and her had some… Ideas around that, specifically, that made a lot of sense to me, where… Like, we would… Yeah, exactly that concept, though, solving this issue. Oh, there, yeah.
Josh Suereth 00:52:20 Yeah, so I think the idea is, we have a notion of metrics, but what we're going to do in the future is instead of groups always being public.
Most groups would turn into private, but we might actually have a set of attribute groups that are public. And we're still fighting over what the term for that thing should be. Attribute group is a little generic, but it's basically, hey, here's a description of, like, the code… level attribute groups, or, you know, syntax-level attribute groups. Not sure what we want to call it.
And you could document that group and say, here is information about that whole group, here's how you fill it out as a group. When you expect one, you should expect multiple. You can have requirement levels and things on that group, but the idea would be that group would have visibility Public instead of internal.
And then it would show up in CodeGen.
it would show up in a registry, etc, etc, right? So I think that's the direction we'd like to move for some of those important groups, as opposed to, you know, pointing at the attribute registry.
James Thompson 00:53:30 But what I'm thinking of is what we currently have.
Alright.
In terms of… and… yes?
We… then the question becomes.
Do we even need a… if we go down the parcel of having those public attribute groups.
Right? Do we even need a linkage from the definition of the single to those public groups?
Right? How do we know which ones apply? Because… There could be different scenarios for profiles versus spans.
For example.
Josh Suereth 00:54:09 Yeah, that's… those are all good questions we need to sort out.
Like, that's… that's the thing, like, you're… we want to sort out those questions and answer them. This is a… this is a much larger project than a chore. This is not just a restructuring of docs, this is basically we're missing a concept in our data model, and we need to fix it. So that's the direction we're going here. What we don't want to do is just rip things apart and shift it around without knowing where we're going.
Right? So, like, the step one is this… this… this concept of these, like, code attributes, or, you know, thread attributes, right?
we need to find a way to model that effectively in SEMCOM, and understand what that model looks like. We want to understand how to do verification of it, like, how does this work with Weaver Live Check is a new thing we're asking all the time, because that's becoming very popular. How do we do code generation with it? It's not just about docs, right?
So how does it fit in the ecosystem? We want to model it, which means we need to ask and answer those questions. Until we have answers we agree on, moving the status quo might actually just make that… answering those questions harder. Let's start asking and answering those questions. What Lyudmil is showing here is a possible answer to those questions, and yeah, we need to sort out all those details, but that's the direction we're going. So we'd rather move this direction than take incremental steps that might have to get undone later.
James Thompson 00:55:40 Nope.
Josh Suereth 00:55:45 Now, I'm not trying to argue that, you know, perfect is the enemy of good. I think we want to make improvements, it's just, I think the PR as I saw it, I don't think is actually an improvement over a thing. It changes things today, but I don't think it's actually an improvement, and it might even start encouraging behavior we don't want people to take.
James Thompson 00:56:05 I think you need to look at what we currently have.
Alright.
Which…
Josh Suereth 00:56:12 with code and attributes? Oh, I'm… I'm familiar. I mean, we… I can bring it up.
James Thompson 00:56:16 Yeah, right. Currently, you have the one attributes page, Alright.
Right? Which lists exactly the same tables as in the registry.
Josh Suereth 00:56:34 So, which one are you specifically talking about?
James Thompson 00:56:37 No, it's under General and the Attributes page.
Josh Suereth 00:56:42 Under General Attributes, yes.
James Thompson 00:56:43 Yeah, so if you… so the whole network thing, that's good?
But when you get past that.
There, so this is exactly the same as what's coming out of the registry.
It's just rendering the registry tables as it is.
Josh Suereth 00:57:10 Yeah, yeah, that's… I mean, I don't see how what you were doing is better than this, right? Like, because again, this… this has context and semantics of what general attributes are in it. The registry does not.
Right?
These may be used in any span they apply to, particularly operations may refer to or require some of these attributes. This… this is the important bit of this section. It's not, like.
whether it's rendered the same as the table, or whether the table exists. We are rendering the same table as before, but the reason this exists is because the semantics around it are important. This is basically saying, hey, these are attributes that could apply to any spin.
Whatsoever. We're not actually limiting them to a particular span name the way we do the rest of SemConf.
And so, you know.
having that additional discussion is important, and if we need to make that more clear here, of these attributes, maybe you store information about a thread that started a span, or talk about, you know.
you know, the use of the word general, for example, is important here. If we just link to thread.
And the thread attributes, it's not clear where these are supposed to be attached.
This could be expanded to include logs, if that's, like, a concern. You know, we want general attributes for threads to be applicable to logs. That's fine.
But again, when we think of, like, the actual meaning of the semantics.
we are working towards the YAML being the definitive source, but there's still things like this.
where we don't have the YAML up to date, where it's not modeling this accurately yet.
Right? We actually don't have a way to represent a concept in the YAML that says, here are attributes that could apply to anything.
But they're grouped together in some way.
James Thompson 00:59:07 Nope.
Yeah. Just from a reading perspective, I just found it really difficult Right, the way things are split up.
Josh Suereth 00:59:19 I totally agree with you. What we want to make sure of is, as we… as we move forward, that we're moving forward together, and that we're moving forward in the same direction. So these… these attributes right now, if they were to show up on a span, right.
will Weaver Live Check flag them as, like, not belonging? It's possible it will today.
Right? If… if these attributes, if I want to generate them, right, can… does CodeGen generate them appropriately if I say, I want all the HTTP attributes?
or I'm looking at specific span-based signals and doing Cogen. I have to kind of guess and know that these attributes are somehow relevant to HTTP SEMConv, because they're under general.
But that general notion is not part of the YAML in any way.
They're just vanilla attributes. There's no, like, clarification that general attributes are different than signal-specific. So, there's a whole mess of our ecosystem that this has made that predates even the YAML.
That we need to clean up over time, and this is kind of the next thing we're working on. But what we want to do is actually work on the whole set of that problem.
and move that direction. What we don't want to do is, take steps that might, undermine the direction we're trying to go.
And the direction we want to go is, these general thread attributes, this is a group, or in new SEMCOM terms, we could call them general attributes. Maybe that's what we call a public attribute group, right?
So, that's where we want to go, is these are actually modeled directly in SEMCOV. You can get an index of these, like, we could actually create a registry of general attributes, where we say, this is a registry of attributes, and they're grouped together.
And we expect these to live on any signal. They can be added to any thread, or any span, or any event.
We have to be careful with metrics, because honestly, they can't just get added to metrics, or you literally break the identity of the metric, but that's… Anyway, So we could have the notion of a general attribute that gets added to spans and events just fine, and we have a way of advertising that. That's the way we want to go forward.
Same with source code attributes.
Which, again, here, yeah, the table doesn't show up, and it's just linked. This is something that we need to work on, agreed, but A, that PR is not a chore, it's actually a major refactoring, and it includes some directional shifts, and it's in counter to some of the directional shifts we're trying to take overall.
So, and then B, you know, I would follow along with what we're doing in SEMCOM v2 around trying to find names for these things.
And let's, let's, like, match how that's going to work, right?
We're over time, so I gotta drop, but, yeah.
If you have, if you have any, if you have any more thoughts, we can follow up on the PR, but I'll, I can make my comments on there as well. So.
James Thompson 01:02:38 Fair.
