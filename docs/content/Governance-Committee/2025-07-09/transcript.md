SIG: Governance Committee
Date: 2025-07-09
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

Alolita Sharma 00:02:06 Hey? Everyone! Good morning!
Josh Suereth 00:02:10 Morning.
Alolita Sharma 00:02:12 Hi, Joe, sure. Good morning. Good morning.
I think. Thank you again. Everyone for accepting the invite on the talk. And, Morgan, I did write to the Cncf. Kubecon folks, and they said that they would resend the invite after the reviews are done. Okay.
Morgan McLean 00:02:34 Cool.
Alolita Sharma 00:02:36 Okay.
Morgan McLean 00:02:36 Perfect.
I will be off camera for a few minutes. They're doing some electrical work on my street, and my power is about to go out, so I'm rigging up my generator right now.
Alolita Sharma 00:02:46 Oh, my, gosh, okay.
Morgan McLean 00:02:48 There's 2 construction sites to the 2 houses next to us are getting rebuilt. I think they're just getting their final hookups today, so the power will be up for a few hours.
Alolita Sharma 00:02:57 Wow.
So Trask, I opened up the service desk ticket and I CC, you on it also. So you should be also getting updates. But the main question they had which they ping me back on was that the lists that we wanted to get removed were the have a very high subscription.
So if we have a alternative that they can ask folks to move to, then let me know, because we can maybe craft a couple of lines and share that they can send it out as a broadcast. And, Trask, I can't hear you if you're saying something so.
Trask Stalnaker 00:03:49 How about now?
Alolita Sharma 00:03:50 I can hear you now.
Trask Stalnaker 00:03:52 Fantastic. It's magic. I added that to the agenda today to discuss.
Alolita Sharma 00:03:58 Awesome, alright, cool.
Trask Stalnaker 00:04:05 Looks like we've got quorum.
Let's see, Severin is not here. But let's see.
Php. Elastic donation next step. I think the next step is, I think, the Gc. Needs to vote first, st to pass it on to the Tc.
Morgan McLean 00:04:37 Yeah, that's it. Yeah, okay.
Trask Stalnaker 00:04:41 Next up.
Austin Parker 00:04:44 I just saw it on it.
Trask Stalnaker 00:04:48 Do we have.
Alolita Sharma 00:04:50 Did you just raise our hand.
Trask Stalnaker 00:04:51 2, 3, 4, 5.
Morgan McLean 00:04:54 I'm not on video.
Trask Stalnaker 00:04:54 Yes.
Morgan McLean 00:04:55 Consider mine rice.
Alolita Sharma 00:04:56 Yeah.
Trask Stalnaker 00:04:57 Alright plus plus one.
Austin Parker 00:05:01 I.
Alolita Sharma 00:05:02 Hand raised.
Trask Stalnaker 00:05:08 Austin, you have thoughts.
Austin Parker 00:05:11 I said I.
Alolita Sharma 00:05:13 I didn't know.
Austin Parker 00:05:13 We were raising our hand to ask questions or raising no, the vote.
Trask Stalnaker 00:05:17 I heard I, and I didn't know if it was a YE, or I.
Austin Parker 00:05:21 Oh, yeah.
Trask Stalnaker 00:05:22 The beginning of it.
Austin Parker 00:05:23 I, I, I.
Trask Stalnaker 00:05:31 Okay, gc, votes to move it to move it forward.
Okay, so it's just in the Tc. Should we probably comment on that issue is Severn.
I'll I'll post in the Gc. Channel. We'll figure that out.
I've got a bunch of kind of maybe small hopefully, small. kind of triaging things.
this is about enabling copilot.
There was one contributor, one Maintainer had concerns about.
Ip.
Tooling workflows.
So I agree with like it should not have been gone out without notice like, and so I will work on drafting a process kind of guidelines for the Github admins to follow, to just make sure that we create community issues for anything that's gonna.
Austin Parker 00:07:07 I have a question on this likewise actually got turned on.
Trask Stalnaker 00:07:13 Cause I thought cup out was already enabled for the org.
Alolita Sharma 00:07:16 I think it gets renewed every X number of days.
They send a notification when they renew licenses every month I get. Yeah, every month. I get an email.
Yeah.
Austin Parker 00:07:28 From Github, but that I think that's separate than this. I thought.
Trask Stalnaker 00:07:32 That's different.
Austin Parker 00:07:33 We had turned off.
Spill it.
Trask Stalnaker 00:07:36 This is the coding agent, and so we've only enabled it now for 4 repos.
Austin Parker 00:07:45 Oh, okay, so this is a different thing.
Trask Stalnaker 00:07:49 This is what allows you and.
Austin Parker 00:07:52 This is so, you can add co-pilot and.
Trask Stalnaker 00:07:56 You can assign issues.
Austin Parker 00:07:57 Delegate.
Trask Stalnaker 00:07:57 Co-pilot.
Yeah. So if I look in the assignees here, I have copilot listed.
Austin Parker 00:08:07 And that is, is this also the co-pilot? Pr review? Is it all the same thing.
Trask Stalnaker 00:08:14 No, we could do copilot. Yeah.
So if you look at say the Java repo where it's not enabled.
I I can't define it to copilot, but I can.
Austin Parker 00:08:32 To go.
Trask Stalnaker 00:08:32 No.
Austin Parker 00:08:33 Pr. You can request a review from copilot.
Trask Stalnaker 00:08:36 Yeah.
Austin Parker 00:08:38 Just bang up marketing job.
Okay? Well, that explains why I was confused, because it's the same name for different things.
Trask Stalnaker 00:08:55 Get used to copilot, meaning everything.
Alolita Sharma 00:08:58 Everything exactly.
Trask Stalnaker 00:09:01 It's not a feature, and that and nothing. Yes.
Austin Parker 00:09:05 Yeah, and.
Pablo Baeyens 00:09:11 Hmm! I think, like typical way it should work for making changes on something like this is, somebody makes a request on the community repo for a particular report.
Then the Maintainers of the Repository approve it, and then we go ahead.
Trask Stalnaker 00:09:28 I don't think there's any can contention about the process we should be following there. I'll draft that up.
Alolita Sharma 00:09:38 This needs to be published process, Pablo. So it's.
Trask Stalnaker 00:09:41 My.
Austin Parker 00:09:42 Yeah.
Trask Stalnaker 00:09:43 Question. My question for this group is, do we agree that it is.
Austin Parker 00:09:51 Yes, that's.
Trask Stalnaker 00:09:52 Call usage.
Okay, that was the that was the only thing I wanted to come back. I wanted to double check.
Pablo Baeyens 00:10:00 If we accept it locally, we should accept this as well.
Austin Parker 00:10:03 Yeah, yeah, like, I mean, I think it's fine to say, maintainers can opt in but yeah, under the Lf policy and our policy, it's fine.
Trask Stalnaker 00:10:16 Okay, great.
I think we can.
Oh, this I mean, I.
This is.
Austin Parker 00:10:26 That was the question I had like, oh, sorry, Riley, and when they'll have their hands up, so we get in queue.
Reiley Yang 00:10:31 Yeah. So so my specific question is, what does maintainer of him mean? Like, if there are 3 maintainers, 2 of them strongly believe it should be enabled. One Maintainer got pissed off. Think it should be disabled? Then what's the arbitration process?
Pablo Baeyens 00:10:46 Don't we have the same problem for any other decision that retainers need to make.
Trask Stalnaker 00:10:49 The Tc, yeah, that that's where the Tc vote.
Reiley Yang 00:10:54 Because if it's a technical thing, the Tsa would vote. Whether have this enabled or not, I feel this is not a technical thing. It's more about a process thing or like policy.
right? If they debate on whether we should implement this Api or not, the Tca. Would chime in. But this one. I don't feel Tca is in the right place.
Alolita Sharma 00:11:14 Yeah, it's a policy, for sure.
Trask Stalnaker 00:11:16 Then it would be gc, I mean, the each Maintainer group can decide if they want to do majority vote or unanimous vote.
but if they want to, if they choose to, only to do unanimous vote, and they can't get unanimity.
then. Yeah, that I guess I was assuming tc, because that's generally where things flow up to. But yeah, for this one, it could definitely be gc.
Pablo Baeyens 00:11:47 My comment was that I don't think this is different from any other disagreement with the Maintainers like it needs to be escalated to somebody.
Alolita Sharma 00:11:59 Right. But I think Pablo sorry. Go ahead.
Liudmila Molkova 00:12:03 No, go ahead if you can chime.
Alolita Sharma 00:12:04 No, no, I was just saying that rask is right, but that it'll just get escalated to the Gc. But it should be called out right, that's all.
Please go ahead, Utmilla.
Liudmila Molkova 00:12:18 Yeah, a slightly different different question.
Who would have a permissions to request copilot to do things?
Is it just maintainers, or anybody with right access to the repo. Do we care.
Trask Stalnaker 00:12:39 I don't know.
Austin Parker 00:12:39 I have a related question which is the not all maintainers have co-pilot licenses. Isn't the license in this case assigned to the org and not the individual.
Trask Stalnaker 00:12:55 I don't think so, but let's we can find out.
So I switch over.
So now, if I'm in issues.
Oh, well, I don't have even right?
You don't have right? Yeah.
Austin Parker 00:13:22 I would imagine anyone that has right would have it would flow down from that right or correct.
Liudmila Molkova 00:13:32 That's good.
Trask Stalnaker 00:13:32 I.
Austin Parker 00:13:35 And.
Trask Stalnaker 00:13:37 Don't know.
Jack Berg 00:13:41 Hey? I'm over in the semantic conventions, Java repo, which is one of the ones that this co-pilot feature is enabled for. And if I go to an issue and try to assign someone. I'm not prompted with copilot.
Trask Stalnaker 00:13:55 Yeah, that's what I.
Austin Parker 00:13:57 Expected making available and over.
Trask Stalnaker 00:14:10 And that's why I want to bug. Keep bugging the Cncf. Here.
I pinged them last week, but.
Austin Parker 00:14:20 Oh, wait!
Trask Stalnaker 00:14:22 Hi.
Austin Parker 00:14:22 No, it does follow the.
Trask Stalnaker 00:14:30 Jack, you're just to confirm you're in the regular simcom repo.
Jack Berg 00:14:34 Stemcom, Java. I guess I'll go to regular stemcom.
Trask Stalnaker 00:14:38 Semcomp. Java doesn't have copilot enabled.
Jack Berg 00:14:42 Alright, let me try and regular some conf. I'm not. I don't have right access to regular sum comp but I do. I'm not prompted for co-pilot. There.
Austin Parker 00:14:49 So looking. I'm reading the Doc all right.
Jack Berg 00:14:52 I can assign other people.
Trask Stalnaker 00:14:53 Okay.
Jack Berg 00:14:54 Yep.
Trask Stalnaker 00:14:54 You do have right access because you're in shape. Java SIM, conf.
Jack Berg 00:15:00 Okay.
Austin Parker 00:15:00 So I'm I'm reading the docs on coding agent. I'll put them in the Zoom chat. And my interpretation of this is that it does actually follow you the user.
Because if you look under section.
Alolita Sharma 00:15:17 Oh, interesting!
Austin Parker 00:15:18 If you look if you look at user, if you look at overview and then you look at opting repositories out.
So if you go down. Yeah, by default users with copilot coding agent and able to use it in all repositories.
All org owners can opt out repositories and prevent co-pilot coding issues being used in those repositories.
So it does.
So all we're toggling is, can someone that has co-pilot.
Alolita Sharma 00:15:48 For their account, use it on this repo.
Trask Stalnaker 00:15:52 And triage, access.
Austin Parker 00:15:55 Right, which does, I guess I I haven't heard anything back. Let me look at service desk, so I have a ticket open about this.
Trask Stalnaker 00:16:05 I tagged them again last week on it. But I think we should.
Austin Parker 00:16:09 Okay.
Trask Stalnaker 00:16:10 Yeah, I think we should escalate it just because that is.
it feels weird to me to allow some maintainers, but not all maintainers to use it.
Austin Parker 00:16:33 I'm logged in with the wrong account.
This is 2671, yeah.
I will. DM, someone about this.
Trask Stalnaker 00:16:55 Awesome. Thank you.
Cool. So it sounds like we're fine. If Maintainers request access. I will mention that we are trying to address. We're trying to address this issue with all Maintainers having access to it.
But it's okay. In the meantime.
thanks.
Somebody. Just a Maintainer posted this in slack this morning. They were asking how they get the this cool little Maintainer badge by their name. I figure does anybody happen to know Austin? Us.
Austin Parker 00:17:43 No idea.
Trask Stalnaker 00:17:44 Year.
Okay?
Austin Parker 00:17:46 I think I have it.
Alolita Sharma 00:17:47 I I think it might be Trask related to the list of maintainers that the Cncf. Maintains.
Austin Parker 00:17:59 So.
Alolita Sharma 00:18:00 But I don't.
How it would get tagged here.
Austin Parker 00:18:04 There. There's also I I perhaps had someone I had someone else ping me about this, and completely, independently asking why the numbers were wrong on
Trask Stalnaker 00:18:15 Oh, there's no honeycomb, there's no honeycomb here.
Yes.
Austin Parker 00:18:19 Yeah. Well, also the if you check if you compare this to.
I assume we were paying by the same person for us.
Alolita Sharma 00:18:28 So.
Austin Parker 00:18:29 If you compare the numbers on there. The accounts on there with dev stats, they don't line up so.
Alolita Sharma 00:18:37 Yeah, exactly.
Austin Parker 00:18:38 Something in the Insights. Beta Channel.
Oh.
Trask Stalnaker 00:18:42 Oh, okay.
Pablo Baeyens 00:18:43 I mean, if you click on the all activities thing you can see, they also track like stack overflow on other stuff like that. So yeah.
Austin Parker 00:18:51 Well, I get that. But it's like the problem is, it's under counting like I could understand over count like that.
I would. I would my suspicion? My question is like, Well, if you're adding in more stuff. So I could see these being bigger than they would be. But the problem or not the problem, but the issue is that they're under what they should be in some cases by like a lot awesome.
I think so clear.
Alolita Sharma 00:19:21 Yeah, yeah. I think, though, that they have a formula, Austin, from the insights team that I have we have spoken with, and you might want to just chat with Daniel Crook. And yeah.
Austin Parker 00:19:34 I, yeah, I already posted about it.
Alolita Sharma 00:19:36 Okay. Okay.
Austin Parker 00:19:37 Daniel saw it. So yeah, I'm sure I will get an answer.
Alolita Sharma 00:19:41 It's but you're correct that they are not synchronized, and they are looking at a different formula and insights compared to what Grafana or Grafana dashboards did earlier.
Austin Parker 00:19:55 Austin, can you?
Trask Stalnaker 00:19:58 Post, the the slack.
Austin Parker 00:20:00 The link to the message.
Trask Stalnaker 00:20:03 Cool. I'll I'll ask about the Maintainer tag over there.
Austin Parker 00:20:08 Do. You may put it in zoom, chat.
Trask Stalnaker 00:20:11 Sure anywhere is good.
Austin Parker 00:20:14 Yeah, there's the message, Daniel, already.
replied to it, and Tag Kieran, I think.
Alolita Sharma 00:20:24 Yeah. Karen is.
Trask Stalnaker 00:20:26 Were you asking about the Maintainer Tag?
Austin Parker 00:20:29 I was asking about the numbers. But you can go ahead and ask about the Maintainer Tag, too.
that I would assume comes from something with groups. I don't know. I think you can look at yourself like I think if you look at yourself in Lfx. My assumption is that this is the my assumption is The people don't have their profiles set up right.
or it's not like their github isn't linked to Lfx or something.
Trask Stalnaker 00:21:06 I see there's a login here. How do I even log in.
Austin Parker 00:21:11 If you go to open profile, dot dev you can.
Trask Stalnaker 00:21:16 Open profile.
Oh, open profile! Dot dev gotcha like! What does that mean?
Austin Parker 00:21:28 Oh, yeah, it's a website.
Trask Stalnaker 00:21:30 Excuse me.
Austin Parker 00:21:31 Bye, although that doesn't show.
Oh, does that show? Don't show it on the antenna.
Trask Stalnaker 00:21:43 Alright, I'll I'll ask in the slack channel. Not Let's good.
Austin Parker 00:21:49 Damn data and privacy can't send anybody's.
Trask Stalnaker 00:21:55 This one, just, I realized, needs a follow up. I don't know if anybody particularly wants to shepherd this from the Gc, if not, I can, if people want to. I I don't want to shepherd it through the donation process, but I can just reply that We, you know, to go ahead and make a donation proposal.
If they, you know, do what we had suggested before of the staffing issue, getting the staffing issue addressed.
Austin Parker 00:22:40 Yeah, that's fine.
Trask Stalnaker 00:22:41 Only looking at you from the client Sig perspective, but doesn't have to be.
Ted Young 00:22:49 Yeah, I mean, I think the main thing was just the staffing, right?
You know.
Trask Stalnaker 00:22:55 Cool. I'll I'll just reply that yeah, this all seems fine. We just need to see the staffing issue addressed first.st And this was what alita was mentioning earlier. So we're thinking to any 1st of all, any last call for these lists before we delete them. And then second question is.
do we had considered having an announce list?
If we want to have an announced list maybe it makes sense to create that first, st and then post one last time on these.
Austin Parker 00:23:47 Yeah, I think we should do the announce list.
Alolita Sharma 00:23:49 Yeah, we should totally do that. I think it's a great, great suggestion.
Trask Stalnaker 00:23:54 Do we want in.
Pablo Baeyens 00:23:55 Yeah. No.
Trask Stalnaker 00:23:55 List!
Oh.
Alolita Sharma 00:23:58 Okay.
Pablo Baeyens 00:23:58 Can we manage the announce list with buffer like? Can we do the same process as we do for everything else?
Austin Parker 00:24:06 I'm not sure if Buffer has a way to send to a mailing list I can check, though.
Dan Gomez Blanco 00:24:16 So do.
Trask Stalnaker 00:24:17 You want that.
Dan Gomez Blanco 00:24:18 So this would be specific to maintainers right well, not maintainers to contributors rather than to end users. Would that be.
Alolita Sharma 00:24:25 Everybody, members, members, all members. So anybody signs off.
Dan Gomez Blanco 00:24:31 I'm just thinking, like, we've got the Cncf community group that can send emails as well.
Alolita Sharma 00:24:36 Yes.
Dan Gomez Blanco 00:24:38 Yeah, at the moment that Cncf community group is mostly focused on on end user events.
But yeah.
Alolita Sharma 00:24:46 That's fine. They could. Then they could still use it right, because again.
Austin Parker 00:24:50 So I think the announcements thing would be more like.
Alolita Sharma 00:24:55 Releases.
Austin Parker 00:24:56 Software, yeah, like, release and change log things. And then the community.
Trask Stalnaker 00:25:00 Security.
Austin Parker 00:25:02 Yeah, security Cvs, whatever, like basically announced should be, hey, this is actually important stuff.
not not saying the community stuff isn't important. But like.
Dan Gomez Blanco 00:25:12 Yeah, yeah.
Austin Parker 00:25:13 Announce would be reserved for like releases security information, you know.
And then community stuff would be everything else.
Pablo Baeyens 00:25:25 Can we? Should we carry over the subscribers to these lists into the new announced list?
Yeah, so that's the discussion, right, Pablo, because that's on the ticket. Again.
I don't know.
Alolita Sharma 00:25:40 That's the discussion that, hey, you know, should we send out a broadcast and redirect them to sign? Signing up on the announced list.
Pablo Baeyens 00:25:48 Oh, I was talking not about like telling them to sign up, but just like moving them automatically, or even just like leaving one of these 3 mailing list, and using that one as the.
Alolita Sharma 00:25:57 I think the Cncf. Suggested that. You know they send it. Send out a request to move over to announce that the new list is being because it has to be.
I guess the Requester is signing up and not automatically moving to a new list.
Pablo Baeyens 00:26:15 Right. I don't know if we one of these, then yeah.
Trask Stalnaker 00:26:19 Rename it. Yeah.
Alolita Sharma 00:26:21 Yeah. Totally.
Trask Stalnaker 00:26:21 I'm last question I had was, do we want to use the Cncf list? Or do we want to use a Google group announce at opentelemetryio.
Alolita Sharma 00:26:41 Probably a Cncf list right?
Austin Parker 00:26:43 List. Yeah, it integrates into all their stuff.
Alolita Sharma 00:26:47 Yeah.
And and they can also, you know, if there are any related updates, they can also post into it. Not that Google groups is, they can't.
It's probably more integrated, though.
Austin Parker 00:27:01 I think, from a continuity perspective, it would make more sense to have it be a Cmcf list. It's good to have like a second, I think it is arguably good to have a second channel like or to have a.
I can think of cases where it's like, okay, we need to have, you know, having some like important stuff list over here that is not connected to our other infrastructure. So that.
like, if something I don't know, something happened to the hotel domain. We get domain hijacked, or whatever. Then.
having a separate list list, serve infra to announce like, Hey, if it's fucked, would be good.
Alolita Sharma 00:27:46 Yeah.
Trask Stalnaker 00:27:48 Cool. Sounds good Alita. Do you want to follow up on the service desk ticket?
Alolita Sharma 00:27:57 Sure. Sure I can do that. Yeah.
Trask Stalnaker 00:27:59 Okay.
Alolita Sharma 00:28:00 I mean, you're in CC, so you know, feel free to chime in. But I'll I'll just ask them that, hey? You know did did you want to let me know? Once the announce list is set up, or should we ask them to create one.
Trask Stalnaker 00:28:13 Let's just ask them on the on that same.
Alolita Sharma 00:28:16 Same ticket. Right? We ask them to create the new announced list and then move everybody over. Or let's ask if they can move everybody over.
Trask Stalnaker 00:28:27 Yeah.
Alolita Sharma 00:28:27 And yeah. And then they don't have to send out a broadcast or something. Okay, I'll I'll ask right away.
Trask Stalnaker 00:28:34 Thanks.
Alolita Sharma 00:28:35 Sure.
Trask Stalnaker 00:28:39 All right, Ted.
Ted Young 00:28:43 Yeah, just kind of like circling back to our 1st con com.
Item around the Php donation. It just reminded me like we. We have like a bit of process around donations. But I have noticed that, you know they do require a fair amount of work from us. If they're big donations to process, and and they can get just kind of like, like stuck or sort of like air gapped. I I noticed this with the Baylet donation. You know where they were like it. It kind of made its way. But there are repeated parts where the Maintainers were pinging me, being like, we're not sure what's going on like. What's the next step like? What? What should we do?
So it seems like a place where we want to make sure we're very actively leading these donation discussions. And.
you know, staying on top of them. I'm just wondering if we need like a bit of process around it because it it is like quite involved to actually like, get one of these things into open telemetry. And it's easy for for us to to drop the ball on it.
So I'm just wondering if people have thoughts on on that subject.
Jack Berg 00:30:08 Donation reviews and proposals are pretty expensive for us to get involved with. You know I I don't. I think, like there's a risk of us over prioritizing donations at the expense of the other projects and things that need our attention. You know I'd really love it if there could be like an orderly queue of some kind, and we could, you know, have some sort of obligation of like how many entries in the queue. We can process per quarter or per month, or something like that. Just so, you know, the people making the donations aren't surprised when we don't get around to it for a while, and we are not overloaded by a flood of donations that you know just anecdotally, I do see quite a lot of donation proposals.
Austin Parker 00:30:58 So my my question is, we do have the guide on donation already.
I'm curious like.
are we looking to? Do you think that what I asked. My question is, what do you feel like? This is missing.
Ted Young 00:31:22 So I think it's missing. 2 2 things. 1, 1 is just like some structure for us, paying attention to it essentially like triage to make sure. Like, like we aren't like. It's not just making sure these things don't get into some state where it's paused because people are waiting for stuff from us. But we're not like moving on it or telling them whatever and then the second thing I'll note is like, basically yeah, like the Tc. Part of it is almost like a sponsorship.
and we're trying to use the sponsorships as like a limiting factor for not overloading Tc members.
So I almost feel like it needs to kind of these things. Almost need to like go in like the project list in some way, right? Because it seems to be like they're shorter lived the reviews, but they do seem to take up just as much time for a Tc. Member.
you know, for the duration that they have to be involved in the review.
Austin Parker 00:32:39 yeah, that makes sense.
I think they could be actually Tras, do you want to go to the project?
a new project board working Progress.
I don't remember if it's linked up here.
I don't think it is. I mean, it's off of the.
Dan Gomez Blanco 00:33:18 Is in the.
Austin Parker 00:33:19 It's under a roadmap, I think.
Yeah, this one like this is not done done yet.
But we could make project. We could make issues in here, for, like we could create a I mean, we could just treat a re donation proposal as a project right.
Dan Gomez Blanco 00:33:49 Yep.
Ted Young 00:33:49 Yeah.
I I think if we just treat it as a project, we finish our our kind of Project Board work for keeping track of this stuff.
Austin Parker 00:33:58 Yeah.
Ted Young 00:33:59 They're listed there as projects where, when we're using our formula for figuring out how booked we are.
you know, they count as a sponsorship.
And then, when we have our weekly triage, you know, we're we're just looking at the state of those things.
Dan Gomez Blanco 00:34:21 So does that mean that? I guess it would be like the we still have the same issue, template like, create a donation proposal. And then during that triage, we can say, Well, this requires a project, or this donation is so straightforward that you know it does.
Austin Parker 00:34:37 Yeah, I think what I think, what I would do probably is I can update this to pull to, also to to basically create project issues from.
Whenever, like a donation issue is created, we would pull that in and create a new issue over here that maps to the project issue stuff so show up on like the calendar view, and which it would get the right fields.
If you do, people want me to walk them through this? I know. I know I posted about it, but I can do you also. I wanna say that everything in this is, you know, not like we can change any of this.
He's.
Ted Young 00:35:18 But I'd love to get the default sort order to sort by estimated end date.
just so that all the finished projects drop to the drop to the bottom.
Austin Parker 00:35:36 Let me pull it back up. Not sure what exactly you mean on here.
Ted Young 00:35:46 Yeah, right, like this.
Austin Parker 00:35:49 Oh, I think we would filter this to only show open ones.
Ted Young 00:35:54 Yeah.
Austin Parker 00:35:57 Like we could change to only in progress.
A lot of these, I I will say, like a lot of these dates are not necessarily correct.
Because not everything had a super parsable date, like some of this stuff like I got I I created the start like the start date should be right, because these were based off of when did the project get merged into the thing?
But some of this also, like whoops like these milestone flags were sort of generated by like, were there milestones present in the dock? And did I get parsed it out correctly?
So I think it'll be just a task for the Gc to go through and figure out like.
And basically, I think we're gonna have to go through and like, go through each of these, one by one, and kind of figure it out.
But if we look at, I think browser instrumentation is probably the best one to look up.
So these all have labels, and then we have the project fields. So thanks.
The other thing that we can do is I can have it. I can set up a field to pull in like the Project board status, because everything should have a project board. So some, if.
Ted Young 00:37:41 Yeah, so if people are using.
Dan Gomez Blanco 00:37:43 Put this Project board together still. But if you you go down there in that so like status.
and see that where it says like, if you had an update.
Austin Parker 00:37:53 Yeah.
Dan Gomez Blanco 00:37:55 And you can set the end date or edit that update. For example, right where it says on track and that target date, I think that is the target date for the project. So like it would be. I think it would be neat if we were to say to like project leads. Well, you can update this.
Austin Parker 00:38:12 So update this.
Dan Gomez Blanco 00:38:14 Yeah, also.
Austin Parker 00:38:17 Yeah, if that, if that actually does update the target date of the does this have a target date.
Dan Gomez Blanco 00:38:24 And not yet, but.
Ted Young 00:38:28 I wasn't. No, I wasn't aware. That was like something projects had, was it?
Dan Gomez Blanco 00:38:33 Yeah. So it's pretty neat like you can set the so like status. And like, you know, target date.
Austin Parker 00:38:38 I'm just gonna do this burden. I'm just gonna push this in here.
And just see what it does.
Dan Gomez Blanco 00:38:49 So now, if you go to, I think if you go to projects you will see it in. Oh, that's weird. I think I definitely, have a view where that shows the the target date.
Yeah. So if you go to the community report, maybe that's that's a better way.
And you go to projects there at the top.
Austin Parker 00:39:26 Oh!
Dan Gomez Blanco 00:39:29 That's weird.
Austin Parker 00:39:31 Sort by new associates. And update. Yeah, no.
Dan Gomez Blanco 00:39:37 Because there isn't.
Yeah.
I've seen another view where, like, you know, in that view, there, I show you the the the target date as well. But
Austin Parker 00:39:47 I mean, is it on the roadmap view.
Dan Gomez Blanco 00:39:57 Now wait, wait. I think you you didn't set. Let's just set the target date. I think.
Austin Parker 00:40:03 Oh, I said.
Dan Gomez Blanco 00:40:03 I'm not sure if you clicked on on, save basically, I just did it now.
Austin Parker 00:40:07 I did.
Dan Gomez Blanco 00:40:08 No, I just. I just saved it. Now. I just said that.
Austin Parker 00:40:10 Oh!
Dan Gomez Blanco 00:40:11 So if you go back to the view, you'll be able to see it now to the project. View the.
Austin Parker 00:40:18 Oh, okay.
Dan Gomez Blanco 00:40:20 So that is a feature.
Austin Parker 00:40:21 That's the.
Dan Gomez Blanco 00:40:22 Yeah.
Austin Parker 00:40:22 That's that's the date for the project itself. So yeah, we could. So what I could probably do is we could probably take that if if that's set, then we could. I could have something that would like override this estimate target date.
Right?
Yeah, this whole the whole the whole way. This works is a little like.
not bass backwards, but it's challenging because github projects project items are not inherently issues. They are like a weird.
extended issue, and you can attach things to project items that do not appear on issues. But there are certain things that only appear in the issues.
So you basically either wind up with like one like we could do this where there was like.
I cause I'm pretty sure a project can be on multiple boards, or an issue can be on multiple project boards, right?
Dan Gomez Blanco 00:41:40 Yeah.
Austin Parker 00:41:40 So if we wanted to, we could have something that like uses the issue, the canonical issue, and pulls it in and sets all those fields.
but I don't know if that's the better way to do it versus the current thing which is basically cop creating issues in the project repo and.
Ted Young 00:42:17 What?
Austin Parker 00:42:17 Doing stuff.
Ted Young 00:42:19 What would be great is if it was somehow scraped from either the project board for each project or the project file for each.
Austin Parker 00:42:32 Okay, well, that's so. That's what that's so, that's what it is doing today. Right now, right? Like all of the stuff.
Ted Young 00:42:38 Scraping.
Austin Parker 00:42:38 Just saw there was scraped. Yeah.
Ted Young 00:42:41 Okay. So you didn't.
Austin Parker 00:42:42 Adjust the spring.
Ted Young 00:42:43 That out.
Austin Parker 00:42:44 Oh, God! No good Jesus!
Ted Young 00:42:46 That's awesome.
Dan Gomez Blanco 00:42:47 Thinking like
Austin Parker 00:42:49 I have. I have fucking chat, Gpt pro and Claude backs. I do very little work on my own, like my AI wrote my robots do it
Dan Gomez Blanco 00:42:58 Oh, yeah.
Austin Parker 00:42:59 Like.
Dan Gomez Blanco 00:43:01 If we were to take it from the the advantage, I guess, of taking it from the Project board, as in from the Github project stuff is that it doesn't require, then A. Pr to change the target date.
Well, maybe we maybe we do want to.
Austin Parker 00:43:17 No, no, we we well, no. So I'm said, Yeah, no, I think like, yes, we should. We can. I can adjust the scraper to pull that field right like.
So another issue with all of this is it may surprise you to learn that doing anything involving a project there is not a nice, happy Api path for this. There is a rather convoluted graphql mutation that has to happen.
Because, github so anything is possible.
It just takes work.
I'm I am still of the opinion that, like the easiest, or maybe not the easiest. The the thing that is most legible to me is the scraper runs. It looks at certain things.
And then because, like, here's the problem with the issue, like here, here's a very specific thing, right? Like project files are issues or not. Sorry project files are files that go into the community repo. Now, if projects were issues.
then we could just say, you create an issue. You add this label to it, it gets pulled into this board, and then something happens to populate those fields.
But that's not how it works right. Their projects are files that live in the repo.
Ted Young 00:44:44 Right.
Austin Parker 00:44:44 Because we want to go through Pr processes and da da da. So I think we can. We can be flexible. But I think the ultimately having the until something changes on Github side, where they add more features of this being able to say, like, Okay, we're gonna have a scraper that runs. And it's going to create an issue based off of the project file, or whatever or it's gonna create an issue based off of another issue. So if someone opens a donation proposal issue, then we will scrape that and create an issue over in the project Repo.
a tracking issue and canonically the source of truth is, wherever all this stuff comes from, right, it's not that project issue, but practically we.
You know, we just have automation. That's kind of like keeping these things in sync.
Ted Young 00:45:47 Yeah, I I would be totally fine with everything that happens in that project.
Github Repo and that project board, if like.
if our approach was like that is all automated as humans. We never touch anything in there. We only look at it.
Austin Parker 00:46:03 M.
Ted Young 00:46:04 I definitely don't wanna kind of mixed mode.
Austin Parker 00:46:07 Right? Yeah, I think that project those project issues, we can automate. So.
Ted Young 00:46:11 Yeah, and I would prefer having a single source of truth, which right now is the project files. So like, I would kind of suggest target dates and things like that go in there just so that we don't have like 2 2 places to look, you know, like it. All of that information could instead move into the Project board for a project right? Because you could, instead of having a project file, have all of that in there and like the project description and stuff.
I think the issue is more for me. It's just more like, what's easier for people to update right? Like the problem we had with projects being issues originally is like, you want to keep updating like this canonical description of what the project's doing. But, like you can't do that as like an issue, right? Because only the person who made the issue can edit edit it.
Or Admins. So it's just kind of worked better to have them be files.
Dan Gomez Blanco 00:47:20 And then with files, you, yeah, I guess there's a certain level of like having. The file does mean that it needs approval. Right? So like.
Ted Young 00:47:27 That's the only thanks.
Dan Gomez Blanco 00:47:28 It has a bit of friction, but maybe we do want that like to be more of a I don't know. Just creating. The Pr adds that extra step before reviewing someone changes the target dates. I don't know if you want that.
Ted Young 00:47:44 Yeah.
Dan Gomez Blanco 00:47:45 Or if we just let you know, 6 leads basically be able to to change the dates whenever they see fit. And then we make it easier. And then, basically, if you if you put everything into the project board itself, then you're making everything a lot more a lot easier for people to change things right. I guess.
Ted Young 00:48:06 It's easier to change. It's a little bit harder to like. See what's going on right like the other. Nice thing is all the project files being in a folder and and when you're making the proposal, having a be a Pr on.
you know the community Repo is helpful.
So.
Dan Gomez Blanco 00:48:27 I think.
Ted Young 00:48:28 I don't know.
Dan Gomez Blanco 00:48:28 Would agree that having a single source of truth is definitely, you know, less confusing.
Yeah.
Ted Young 00:48:37 Yeah, but I think the single source of truth for like donations could be could be an issue instead.
I don't know if we want donations to move into like like a file that has to live in there. I don't know if they're long lived enough of a project.
but just circling back to that like, yeah, it would be great if, like, our donation process gets formalized enough that that we can keep track of it the same way we're keeping track of projects on that big board, and my hope with all of this, is like to be able to use that as part of like starting to schedule things right like, especially things like donations where we're saying like, we can't deal with this right now. But we're interested. I think people would be willing to hear like come back later, if it like. Had a a time associated with it, like.
you know. Come, come back in September, and we'll be able to to process this. But we can't process it right now.
That's kind of like one of my goals with this next step of project management is being able to like reliably punt things out and have people accept that as an answer and have us actually, then do it.
Dan Gomez Blanco 00:49:59 Makes sense.
There was another topic. I think we've got 10 min. There's 1 that I added to the agenda, which is related to this as well is the.
There's a draft Pr. That I raised at the moment. I think it's trying to align with the with the new sponsorship requirements that the Tc has been put together, and that basically the sponsorship requirements from the Tc. Are for Sigs. Right? 6. Get sponsorship. And then how do we align that with projects or project proposals, and especially when we've got like project that may come out of an existing Sig right? That Sig has already got sponsorship.
And can we make it easier and more streamlined for let's say, you know.
Java say, wants to kick off at something a project that is, I guess.
communicating to the communities. As you know, this is a big piece of work.
and then I think we shouldn't really go through the. You know, we need a new sponsor. We need a Gc liaison and all that, because it already exists. Right? It's part of the Sig already.
So yeah, that was my intention with that document is clarifying that if you're a seg already, and you want to create a project.
things should be a lot more streamlined right and is but still a good practice that we want to encourage.
John.
Josh Suereth 00:51:28 Yeah, I just, I think we need to be careful. I I agree with streamlining. The care we need to have is like, let's say someone signs up to be the sponsor, for like the go sake, and then go proses. 5 projects. Now, all of a sudden, that Tc members completely overloaded, and we've kind of hidden that. So that that would be my only caveat here of like, I think we should basically consider that the current sponsor de facto sponsor right? But we also need to to limit load. And so the danger here is that I think there are some Sigs that are inordinately busy.
And so we we just have to be careful. Semcom is the one that I really think about like if you were to de facto say, Oh, semcom sponsorship. Right? Any new simcom pulls in a Tc member from the current set pool of Simcom. We're we're already dead at that point.
Yeah. So yeah.
Dan Gomez Blanco 00:52:22 I guess in that case that would require normally, that requires a new yeah. I guess I knew.
Ted Young 00:52:27 Right.
Dan Gomez Blanco 00:52:28 Set of approvers, and, like, you know, let's we spin up a new.
Ted Young 00:52:31 But.
Dan Gomez Blanco 00:52:31 Anything, right?
Ted Young 00:52:33 I think, anything that requires Tc level involvement. We just want to use our current process for doing it. But I think to your point, Dan. It's more that like.
if if we're getting projects stood up and and we're liking them. And we are starting to see some of the Sigs that are involved with them, wanting to just organize their own backlog a little more like this. And I think it would be great.
especially if we're like scraping these things like the simplest thing I could think of is like, well, if other repos right like, if other Sigs want to have like a projects folder where they're putting in project files. And these aren't things that, like the Tc needs to be involved with. These are more like, say, implementation Sigs implementing part of the spec right? And they want to organize that as a project or in Javascript. They're like overhauling the they did like an SDK overhaul project recently where they just had a bunch of backlog on the SDK, they just wanted to work on.
and if they organize those things into projects and put them in a project folder. If that could get scraped and then go up on a project board, then that would kind of plug a gap there where we're actually being able to see more of these major initiatives that are happening in the implementation Sigs.
And I see a bunch of hands.
Dan.
Dan Gomez Blanco 00:54:01 I thought Trask was.
Ted Young 00:54:03 I did, but Ted said everything I wanted to say so so.
Dan Gomez Blanco 00:54:08 Yeah, no, that's it. I think that's another example of this, that. And I think this is what it's worth doing is the client side or the client instrumentation sake, which is now basically being well. We we thought, okay, still good to keep it, because we've got like the things that that say we'll try to tackle is things that are cross cutting from mobile browser, and so on, right?
But now that we're thinking about like a new project. An idea started to like, you know, we need a project that covers like stabilization of like session and session managers, and also optimizing like otop, and, like, you know, the scope started to grow already. So I guess my intention there is to say, Well, can we scope it to like something smaller.
and then, if there is already a Gc. Liaison there, and there's already a I don't think there's currently a Tc. Sponsor in there, but if we find one for anything related to that Sig, then continuous. You know, we focus on something. Now we move on to something else rather than like having a huge scope of a project right? That would be there almost like a Sig charter rather than a I think there's like the definition between a Sig charter and a project right? I guess that's the that's what I'm trying to get to.
Ted Young 00:55:28 Yeah, I think that's kind of like a special case. Just to explain to people like, there's some work that we discovered. That's kind of like cross sig around like the entities stuff where we're trying to like. Figure out what entity providers should look like. And the people driving that work are the people on the different who care about like session managers right like want to do the prototypes to make sure it works for them. But then those session managers are getting irrelevant to a couple of different Sigs. Right? The browser Sig and the Android Sig like, for example.
So it is like like a bit of work that's like related to a bunch of different sigs.
and you could say, like, whatever we're just gonna organize all of this as the entities, Sig. And like Browser Android people, just be part of the entity, Sig, if you're interested in, you know, prototyping the entity provider.
But it was like a good point that it was just like. On the one hand, it was kind of like cross Sig work. But, on the other hand, this wasn't something that really needed, like a Tc sponsor for it. Right? It's already worked. It's being done under several different sigs. It's just more like a couple of different sigs, trying to coordinate with each other.
Dan Gomez Blanco 00:56:51 Yeah.
Ted Young 00:56:52 And it's like across like a cross sake. They're right. It's a pro. It's a project that people are doing across.
Dan Gomez Blanco 00:56:57 So, yeah, you know, across 6. But like all of those already have sponsors and.
Ted Young 00:57:03 Yes.
we we were feel we wanted to make a project. It was complicated enough for like, we want to make a project file just to keep track of like, who said they would do what on this?
But it could be a project in the entity sick. That's actually how I would maybe just simplify this
Austin Parker 00:57:25 The only thing I wanted to add.
yeah, the only thing I wanted to add is at least from a you know, what is the stuff that needs to be that needs to exist on on those issues in the Project board or in the roadmap board, like a lot of those are things that are just like board specific. Right? So if we go to a say, if there's a Sig that's like we're already tracking projects in issues, and they want to keep using that. Then we could say, Okay, fine. We just need to make you to make sure that.
like you're still using project boards, or whatever right like, they don't necessarily have to adopt the entire, you know, create a project folder, and create project files thing that would probably make our lives easier. But it's not a hard requirement.
Ted Young 00:58:27 You. You mean we could have a couple of different scraping targets for that project board.
Austin Parker 00:58:32 Right or just like someone could add like we could, what we could do is we could just have something like what what will probably what would probably be is like if someone adds a issue from another repo into that project roadmap board, then that would basically trigger the scraper to go and keep it up to keep the fields up to date based off of whatever criteria we said again, we can do a lot.
Dan Gomez Blanco 00:59:03 Yeah.
Or if someone were to like.
you know, add a project board and then say, Okay, well, now you can go and scrape it from here? Right? Yeah.
Ted Young 00:59:12 Right. I mean, things can also use their own project boards and just do whatever the hell they want. But I just I kind of like the idea one. I'm just noticing that some things it's like as we're getting more organized. Some things are looking at that organization and being like that would be useful.
And one thing that's interesting is like, if we're scraping. I like the scraping approach to keeping track of some of this information because it allows us to put it in a couple of places right? It means like that's it can have their own project board and do whatever the heck they want to keep track of their stuff, but also know that, like, there's like this global view of hotel.
Yeah, that their stuff is getting funneled into.
Dan Gomez Blanco 00:59:55 And I think this would really help end users and just kind of like everyone get a sense of like if you had this big, searchable.
Ted Young 01:00:04 You know roadmap
Dan Gomez Blanco 01:00:09 And if you want more.
and then if you want detail, you can just, you know, click through and then go into whatever like the project or something? Yeah.
Ted Young 01:00:19 Anyways, we're we're we're out of time. But I'm liking. I'm really liking the direction that this stuff is going.
But in the case, the of the particular session manager stuff we just talked about. I'm gonna tell everyone. Let's let's do that work out of the entities. Sig instead of the client, Sig.
because that's.
Austin Parker 01:00:39 So.
Alolita Sharma 01:00:39 Yeah, that's a that's a good idea.
Ted Young 01:00:42 Yep.
Alolita Sharma 01:00:42 Tent.
Ted Young 01:00:47 Alright, cool.
Trask Stalnaker 01:00:48 Let's end on time.
Alolita Sharma 01:00:49 Okay, thanks. Everyone. Take care. Bye.
Trask Stalnaker 01:00:53 I.
Austin Parker 01:00:54 Hello!
