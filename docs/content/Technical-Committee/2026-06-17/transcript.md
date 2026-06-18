SIG: Technical Committee
Date: 2026-06-17
Duration: 19 minutes
============================================================

## Zoom Recording Transcript

**Reiley** 00:14 Morning, John.
**Jack Berg** 00:19 Good morning, Riley.
**tnajaryan** 01:00 Hey, guys.
**Reiley** 01:03 Hey, Tiger.
**Jack Berg** 01:06 Bye too, Grin.
**tnajaryan** 02:34 Should we do the triage, save the time now?
I'm trying to share my screen, but I can't for some reason. Can someone share their screen?
Something is wrong with my zoom.
**jmacdonald** 03:00 Looks like nothing in deciding.
Triage.
That was Spec Inbox, right?
Nothing in the.
**Jack Berg** 03:09 Second inbox, but there's items in the community inbox.
**jmacdonald** 03:14 Alright.
I guess we start at the top.
**tnajaryan** 03:27 That's a draft, I think, so…
**jmacdonald** 03:29 Yeah, looking at that.
**tnajaryan** 03:30 I should skip that.
**jmacdonald** 03:33 Okay.
**tnajaryan** 03:34 I don't know why the drafts lend into IS Inbox, we should probably remove that.
If it's a draft.
Let's look at the other one.
**jmacdonald** 03:46 Sure, I was trying to… It's funny, you can't see the draft state on this view.
**tnajaryan** 03:53 Yeah, that's weird.
Bootstrap, Dart, and Flutter. So this one is a new SIG, essentially, new language SIG.
**jmacdonald** 04:03 Okay. There was a donation proposal recently, I guess, And that must have been triaged already.
**tnajaryan** 04:20 Do we have a TC sponsor?
We don't, right?
That's.
**jmacdonald** 04:25 It's a lengthy thread, which I had not paid attention to, okay.
Severin seems very excited about this.
Okay, I don't, yes, we don't have a TexC sponsor.
**tnajaryan** 04:53 Yeah.
**jmacdonald** 04:53 what I'm seeing.
I wonder if we should ask Severin to find one.
I mean, sorry, did anybody find it interesting?
**tnajaryan** 05:05 because no one wants to be the CC sponsor, and I have reservations about how important this is, to be honest.
**jmacdonald** 05:13 Got it.
**tnajaryan** 05:14 We… I think we said… no to other, maybe more important things in the past, or were more reluctant about it, so I would want to… maybe have a good reasoning about why this is needed in OpenTelemetry.
Seems like Python-niche language to me.
I may be wrong. If anybody wants to be the sponsor, that's a different letter.
**Reiley** 05:37 I have a question. So, before the SIG bootstrap, I think the first step is to accept the donation, or these two are lockstep. Essentially, they're the same thing.
**jmacdonald** 05:48 Well, this says it's separated here.
For guidance. I'm not sure which guide… whose guidance that is.
**Reiley** 05:57 So, even if, like, regardless whether the donation is approved or not.
or, like, OpenTelemetry is going to accept it or not. It seems like here, the GC decided they want to accept the SID, right?
And this is the ask for the TC.
Is that your understanding?
**tnajaryan** 06:16 I think if we… if there is no SIG, if we don't create a SIG… then the donation doesn't make sense, right? Why do you donate it if there's nobody to take care of it?
**Reiley** 06:28 Yeah.
**tnajaryan** 06:29 So, accepting the donation, in my mind.
requires a SIG, so your SIG is a prerequisite here, in a sense.
**Reiley** 06:37 Yeah, and the SIG got created, the donation didn't happen, because people start to fight, they don't agree on things, then do we dismiss the SIG, or…
**tnajaryan** 06:44 Did the SIG not get created? Is it true? If there is no TC sponsor, how did the SIG get created?
**Reiley** 06:50 My question, like, I potentially can sponsor this, but before I sign up for some unknown job, I want to know what I'm signing up for. So, for example, if you see it got created, the donation failed, what do we do?
We're gonna dismiss as it, or… Like, do you think there's clarity?
If not, I can ask Severin. If you already know, like, I'm just being crazy here, then help me to understand.
**tnajaryan** 07:17 Sorry, your question is if… we create the SIP, but do not accept the donation.
**Reiley** 07:23 Like, Riley will say, yeah, I'm having to sponsor this as TC member, like, the SI got created. Then the donation part, I'll say, like, I'm not handling the donation, so not my problem. Then someone works on the donation, they come back and see the donation failed. What do I do? Do I ask the SIG to be dismissed?
**jmacdonald** 07:41 I think we would not accept the SIG without the donation.
**Reiley** 07:46 Okay, so two are lockstep, essentially. Either we take both of them, or not.
then… then they shouldn't say the seed creation is separated from the donation itself, like, it's not separated. This is not true, right?
**tnajaryan** 08:00 I mean, formally it could be, right? You could say I'm creating a SIG, I have the staffing for the sick. Donation is optional. If it's not… we don't accept the donation, we still have the staffing who will work on this. This is, I think, hypothetical. I don't know if we have the staffing, but it's at least theoretical possibility.
**Reiley** 08:20 Okay.
Okay, so I'll ask Sarah to clarify it.
I can follow up on that.
veneer…
**tnajaryan** 08:29 Okay, so you're saying, Ravi, you're interested, potentially.
**Reiley** 08:33 I mean, if they only need escalation.
I mean, escalation, to me, seems fine. I can, like, I help people to create 6. If they want to work on that, I… And they don't require a lot of help from the TC, I don't see why we want to say no to them.
**carlosalberto** 08:49 But previously, for new language6, like Kotlin, we have, considered doing, guiding, you know?
So, it's up to you, but yeah, I wanted.
**Reiley** 09:00 So, guys, no, I don't have bandwidth, but if they just need, like, if they just need someone to, like, do escalation part, certainly I can.
**carlosalberto** 09:10 Okay, bye.
**tnajaryan** 09:10 I think for Kotlin, it was guiding, because there was kind of the relation to Java, and somebody needed to take care of that. If this is more independent, then maybe just escalating is fine.
**Jack Berg** 09:22 I've been of the opinion that, you know, if… if there's a new SIG with new maintainers that are, you know, haven't participated in the OpenTelemetry ecosystem up to that point, then there's a lot to learn about how to develop and publish and maintain a language SDK, and they could, you know, just absorb it all through osmosis, just look around and do the right thing and follow the patterns of other languages. I don't have especially high confidence.
I think languages are, you know, better suited if they have… if they start out with, like, a maintainer, you know, from a different language. You know, I'm thinking about, CJO and some of the other maintainers that went over to Rust.
from .NET, and, like, while I think that's ideal, like, I don't know. I don't know that I feel strong enough that I want to, like, you know.
Require guiding sponsorship.
**tnajaryan** 10:24 Okay.
Let's move on.
**jmacdonald** 10:29 So, we have decided… This needs stronger… contributor rosters.
Jack, I see Grafana here. I'm wondering if you have an opinion about Grafana's stance.
**Jack Berg** 10:46 I have not heard anything about this from Grafana, or… and, you know, I guess I haven't looked at this. This is… this has been open for a long time, right?
**jmacdonald** 10:55 Well, this… the bootstrap request has been, but… and I… I can't believe this is from June, because I saw May.
So, May 6th, 2025.
It's… and now… yeah, this date is absolutely incorrect right here. I'm confused.
I guess maybe Severin made a comment on June 3rd. So we're going to remove triage TC inbox. Do you, I mean, what should we write?
**Liudmila Molkova** 11:31 I've heard some internal interest of… at Google in this. I didn't read it, and I don't promise anything, but I would like a few days to read and understand How interesting and important it is, and if there are any people interested in working on this.
**Jack Berg** 11:51 Can we scroll up real quick? Who added the TC inbox label?
the bot?
**jmacdonald** 11:59 GitHub Actions did.
when it was created, I suppose.
**tnajaryan** 12:08 We asked for this. We asked the GC that whenever a new project proposal is created, we are notified as soon as possible, so that we can begin the discussions.
Doesn't mean that we have to immediately reply like today, right? So we can take our time to discuss it, and then reply.
**Jack Berg** 12:28 So let's keep the TC inbox label on it, then, just so we don't lose track of it.
**jmacdonald** 12:35 Okay… This one is from CJO. It has a bunch of approvals, including from me, David, Trask, Austin.
Although… That seems pretty strong support to me.
**tnajaryan** 12:56 the stuffing is lined up as well, I think, from what I see.
**jmacdonald** 13:01 Is there a… let's see, a formal… yeah, so Martin… That seems pretty strong to me, as we're… that's two companies.
There.
I was encouraging Sigio to do this in the last couple months, so I definitely support it.
**Reiley** 13:23 And the SVAC PR has been merged already, right?
**jmacdonald** 13:26 Okay.
**Jack Berg** 13:27 Oh, really? Spec OTEP was merged?
**jmacdonald** 13:32 Good question.
I'm not sure why…
**Jack Berg** 13:35 It's linked up at the top, all the way at the top.
**jmacdonald** 13:42 Hmm… doesn't look like it's merged, but it has a million approvals.
**Reiley** 13:46 Okay, then I think, number one, we should just merge the PR right now, and then we get back to the SIG request and create a repo.
I can't create a repo.
**jmacdonald** 14:00 Okay.
Looks like we have a couple of changes to resolve here somewhere, but, We don't need to do that here and now. So… very soon, we will merge this OTEP.
I would say.
**Reiley** 14:18 Then let's tag Sigil here, and say, please drive the OTAB.
To be merged, and then get back here, and… who wants to help here to create a repo? I mean, I can't if nobody else wants.
**Jack Berg** 14:34 I think probably David, who's the TC sponsor for this.
**David Ashpole** 14:38 Sure. Is there… I haven't created a repo before, do I… I agree.
**Reiley** 14:45 Yeah, if you need some instructions, ping me, I can send you the links. They're in the community.
**David Ashpole** 14:52 Then I'm sure I'll find them, yeah.
**tnajaryan** 14:57 Yeah, I do think we could do the rest maybe offline, because we have the private topic to discuss, and…
**jmacdonald** 15:02 I just blessed us.
**tnajaryan** 15:03 We have enough time.
**jmacdonald** 15:05 Right, post-graduation roadmap is an ongoing one. I don't see why that's… In our inbox again.
Haven't we discussed this?
We just left it in the inbox.
**Reiley** 15:19 Yeah, I just gave this today, and switched to the channel, I think.
**jmacdonald** 15:24 Okay, see you all in a private channel very soon.
**Reiley** 15:28 See you.
