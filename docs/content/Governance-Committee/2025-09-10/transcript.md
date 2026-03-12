SIG: Governance Committee
Date: 2025-09-10
Duration: 22 minutes
Zoom Recording URL: https://zoom.us/rec/share/F5JbyNgH4ckqtbR_iZ_5eECqAC0nJPTltO9uoyVsefwKMDjsICApiSxoVPjdwjST.JPp_adMxM3pvJSIh
============================================================

## Zoom Recording Transcript

**Juraci Paixão Kröhling** 00:40 Hello, hello?
**Austin Parker** 00:45 Ayy.
**Juraci Paixão Kröhling** 00:46 I see that you are a PM now, Austin.
**Austin Parker** 00:51 I'm a what?
**Juraci Paixão Kröhling** 00:52 PM.
I… I think I read that you are the MCP PM.
**Austin Parker** 00:59 Oh, yeah, probably.
PM, primary, engineer… Bmm… fall glider.
Video star… Hotel, shirt generator… I wear a lot of hats.
**Juraci Paixão Kröhling** 01:24 Yep, I can see that, yep.
Like, literally as well.
**Austin Parker** 01:29 Literally, yeah, no.
No, I mean, I said, it was sweet for…
**Reiley** 01:38 Yeah, right.
**Austin Parker** 01:43 Actually.
Now I feel shame of all of my West Coast colleagues. I ask them when we have meetings at 8am.
I know we're gonna be missing quite a few people from DC today.
Dan, Severin, and Morgan.
Can we possibly have this morning?
Do you have anything we need to handle?
I can't pay you fast.
**Ted Young** 03:58 Can't hear you, Trask.
**Trask Stalnaker** 04:04 How about now?
**Austin Parker** 04:05 Yay!
**Trask Stalnaker** 04:09 That's ridiculous.
So I gotta turn it off and turn it back on.
**Ted Young** 04:14 You forgot to cock your arms before, right? Like all good computers, you just turn it off and turn it back to normal.
**Trask Stalnaker** 04:23 I added, one thing because I had added it to the GC agenda, Forgetting that this was joint.
But it's probably worth… This… group, since, also Josh is involved.
I can share and kick that discussion off.
And maybe we'll end up with more on the agenda after.
Oh, sorry, I, getting machines mixed up here.
Alright, so this is a… new SIG proposal.
That we've been chatting about for a while, brought it to the GC maybe a month ago, and got some good feedback, from Austin and Ted and others.
And so I think it's in, a lot… I think it's in a lot better shape now, except possibly, as, said, the, the name of the SIG. This has gone through a lot of, revolutions already. It's been a struggle.
And I agree that this is still, like, to a general community member, kind of…
**Ted Young** 06:08 I always like, do… are we, like, Boolean or Bayesian logic? Like, what kind of logic are we modeling here?
**Alolita Sharma** 06:16 It is hard to understand, and I agree with that.
**Trask Stalnaker** 06:20 Yeah, and I think the name of a SIG is important.
**Ted Young** 06:24 I want people… people need to be aware of this SIG. I would probably not care if it was just some technical stuff off on itself.
**Austin Parker** 06:31 I also agree that the name is bad.
**Trask Stalnaker** 06:34 I agree.
**Alolita Sharma** 06:35 I think, I think, actually Josh had a few good recommendations, and I really liked the application and system, the service, you know, entities. Yeah. He had 3… 3 suggestions, and I think that was on point with what, you know, resources, and we are trying to address.
**Ted Young** 06:54 I didn't.
**Josh Suereth** 06:55 I listed them in my priority order, and Logical Enty was the last one, and that's the one that John V updated it to, yeah.
**Trask Stalnaker** 07:02 Hello, folks.
**Josh Suereth** 07:03 I might have, I might have not put them in the right order.
**Alolita Sharma** 07:05 I don't… and I don't know if it's in here, but I think it's really important that this is distinguished from entities, the hotel concept.
**Josh Suereth** 07:11 Yes, yes, exactly. I agree.
It's… it's actually not… the… the… It's supposed to be entity… so… Right now, we're stabilizing Kate's entities within the Kate SemComf SIG, right? And we kind of deferred logical entities, and so this is just tackling the most important logical entities from SemComf of service, deployment, things that are actually… resource attributes, if you will, that we need to, like, sort out. So that's where the logical entity, proposal came from.
**Austin Parker** 07:43 Yeah.
Do you, like, service resource them?
**Josh Suereth** 07:47 Yeah, I think you passed it, Trask, wherever I had.
**Alolita Sharma** 07:49 Yeah, Trask is listed in one of the comments. I'm trying to find it.
**Austin Parker** 07:55 Oh, did I already say that the name was wrong?
**Alolita Sharma** 07:58 Yeah, it's listed.
**Trask Stalnaker** 08:01 Everybody's… everybody has said the name is bad.
**Ted Young** 08:03 Sorry, yeah. Yeah, it's… Because it is.
**Austin Parker** 08:08 I see that this was, like, from July, and I honestly don't remember what.
**Ted Young** 08:12 What?
**Austin Parker** 08:12 I was doing in July, so…
**Ted Young** 08:14 I've wondered whether… is it… is it also maybe a scoping thing? Is it just quite clear enough? Like, if you guys… No, the scoping is quite clear.
**Alolita Sharma** 08:23 Seems pretty clear, that's so…
**Ted Young** 08:25 you know, could we just say it's, like, the service entity, or something like that? Yeah, let's totally okay with it, yeah.
**Trask Stalnaker** 08:30 That's what… yeah, so that's what I proposed to John V. after your comment, Ted, in Slack, was… I actually proposed, we, like, since it's already in phases… Where is the phase?
**Ted Young** 08:48 Yeah.
**Trask Stalnaker** 08:50 I'm not finding… .
**Alolita Sharma** 08:53 Yeah, just scroll down.
**Trask Stalnaker** 08:56 Deliverable… Phase… Phase? Yeah. Three phases. Oh, I see why I'm not finding it, because they're not, like, they're all in one paragraph.
So the first… to, like, we've got service entity, and, you know, I think somebody even said it earlier.
service entity stabilization, say, service, service entity… service and deployment, maybe, like, grouping these two together.
call it Service and Deployment Entity Stabilization, SIG.
**Ted Young** 09:31 Yeah.
**Trask Stalnaker** 09:32 and then actually rename the SIG for Phase 3 to be Data Sensitivity SIG.
**Ted Young** 09:40 Yeah, this is… I would love to see that, just like what we're doing with Browser. Like, there is, like, a pile of work, but yeah, you've got this Phase 3 that's, like, the stuff we'll do in the future once we get done with this.
And maybe just saying…
**Trask Stalnaker** 09:54 Actually rename, yeah, and actually just rename the SIG at that point, because, again.
**Ted Young** 09:58 just…
**Trask Stalnaker** 09:58 The SIG names are important.
**Ted Young** 10:00 We're gonna do service entity now, and then when we're done with this, this group of people will figure out What they want to tackle next, and they'll propose that next.
**Alolita Sharma** 10:09 Yeah, I think both of Josh's other suggestions were very on point, because the service and environment, is also very focused, you know, and application and service also. If we want to distinguish between application, you know, and platform services, if you will.
**Ted Young** 10:27 Yeah.
**Josh Suereth** 10:29 Yeah, I agree. Also, for clarity, John V, the one who is proposing this, is totally fine with making progress on the first two and having Phase 3 just be a, hey, we're gonna continue, but okay making that a separate project proposal, rename, all that kind of thing, yeah.
**Ted Young** 10:44 Yeah. That… that helps moving away from the Forever SIG.
**Alolita Sharma** 10:48 Yes, agreed, agreed, yeah. And also completing, you know, each phase.
And delivering.
**Josh Suereth** 10:56 Call it the Forever Sig. How's that for a name? The Forever Sig.
**Alolita Sharma** 10:59 No, no, that's, Ted's secret code word already.
**Ted Young** 11:02 That's… that's called the GC.
Yeah.
**Trask Stalnaker** 11:07 Josh, so, why don't you, in our chat with Javi, pick whatever you like best, because you're the closest to this.
And let's just do that.
**Ted Young** 11:21 Yeah.
**Trask Stalnaker** 11:22 Awesome. Yeah, these are good… I think all good options.
**Alolita Sharma** 11:26 Yeah.
**Trask Stalnaker** 11:28 Okay, cool, and then I will be coming back to… other than the name of the SIG, I think it is… good to review, but I understand if you want to wait to approve it until it actually has a signame that, Makes sense to the community.
**Alolita Sharma** 11:52 Yeah, both those, both of Josh's suggestions are very useful. They're much more on point.
**Trask Stalnaker** 12:00 And the plan right now is to, do alternating meetings, because we've got folks from India, Japan, U.S. West, U.S. East.
So at least currently, the plan… we gotta work through the meeting pool stuff, but would be to have alternating every other week, where John V would attend both, in basically time zones where she could attend both to have the continuity, but then pull in people.
**Alolita Sharma** 12:37 I mean, alternating is fine, but I think right now, I mean, I'm trying to work with her to get a little later time on the West Coast, because… You know… I…
**Trask Stalnaker** 12:48 provided that feedback also to her, that the meeting pool… right now, it only had… it didn't really have options, there was just…
**Alolita Sharma** 12:56 Right.
**Trask Stalnaker** 12:57 one… there was only one time for…
**Alolita Sharma** 12:59 I'm dying.
**Josh Suereth** 13:02 I talked to her about this, and she said, if you look at the instructions, she says, please propose meeting times that you would prefer. And I was like, John V, that's not how this works. Like, no one's gonna propose meeting time, just put all of them on there, and then people will pick one that works. They're not gonna, like, add So, that, I think, was just a miscommunication, yeah.
**Trask Stalnaker** 13:22 Cool.
**Ted Young** 13:23 Yeah.
**Trask Stalnaker** 13:29 Alright.
**Alolita Sharma** 13:30 Any other call-outs, Trask? Because then…
**Trask Stalnaker** 13:33 No, we can move on.
**Alolita Sharma** 13:34 Okay, I mean, Josh and I also talked, and we, again, I was trying to get some details and understanding, and I think we can also contribute from Apple, because we do have, you know, multiple We use all the clouds.
**Ted Young** 13:50 Consider making the meeting 30 minutes. That's my other.
**Alolita Sharma** 13:54 Yes, I agree, because I think they'll stay focused and, you know, really maintain a velocity.
**Ted Young** 14:01 Yep.
**Alolita Sharma** 14:03 Good suggestion, Ted.
Yeah, we'll work on Slack with Johnny Trask, so, you know, I think we should be in good order.
**Trask Stalnaker** 14:14 Do you have somebody, who we can add from Apple that we can add to the.
**Alolita Sharma** 14:20 Yeah, I'll pull folks in. I'll also… I'll also probably join in, because I do have platform, and then, I'd also like to see, you know, the… Inference training, you know, infrastructure, entities also kind of being considered here, because they do overlap with, the compute layer, if you will, so…
**Trask Stalnaker** 14:47 We'll definitely… Cool. Yeah, that would be great to get, more… more names on the, proposal.
**Alolita Sharma** 14:53 Yeah, yeah.
I should just comment on the issue, right, Trask? Yeah. Yeah, yeah.
Alright, sounds good.
**Trask Stalnaker** 15:11 Alright, we have no… No new topics appeared on our agenda.
So we're either done, or anybody have something that… They want to talk about. I know that the TC, y'all, did you want a private session?
**Josh Suereth** 15:27 I think maybe it's probably worth us… yeah, Tigrin, I don't think, was able to make it today, and he was driving that discussion, so if you want, we can, we can do a quick, quick chat. I don't… I don't want it to take very long, but if we end up chatty, that's fine by me. I just, if there's other things we need to talk about… Yeah, so I think just, just, like, one last follow-up on that would be good.
If there's any other topics, we should totally do them. We have 45 minutes.
**Alolita Sharma** 15:55 I think the only other topic I had… sorry, who was going…
**Austin Parker** 16:00 I was just gonna say, I… I can give you a quick graduation update, which is there's just no update.
There's the one.
**Alolita Sharma** 16:07 Yeah, even I also checked in with, emily, and she was…
**Austin Parker** 16:11 Yeah.
**Alolita Sharma** 16:12 Working through it.
**Austin Parker** 16:13 Fair.
They continue to work through adopter interviews.
**Alolita Sharma** 16:18 Yeah.
**Austin Parker** 16:19 So, no update.
**Alolita Sharma** 16:21 Austin, they told me that they would reach out once they had finished The, current folks in queue.
**Austin Parker** 16:31 Yeah.
**Alolita Sharma** 16:39 Who's Michigan Football20? Good.
**Juraci Paixão Kröhling** 16:41 Yeah, no, I'm just looking at the list of, invitees to this meeting here. There is one, like, Michigan Football20, I have no idea who that is. Could be… could be Jack.
I thought it could be Jack.
That's…
**Alolita Sharma** 16:55 That was my guess as well. He lives in the area, so…
**Juraci Paixão Kröhling** 16:58 That was my guess, but I would like a positive confirmation.
For my own sanity.
**Trask Stalnaker** 17:05 Yeah, he's in between employers, so maybe he switched.
**Austin Parker** 17:09 Oh my god.
**Juraci Paixão Kröhling** 17:11 The same… I mean, similar question, are the Splunk emails still active? Or, I see that, I think Morgan's is not active anymore, but I think Tigran is still there on his Splunk email.
On that invitation.
Anyone from Splunk here? No.
**Alolita Sharma** 17:28 I thought everything switched over to Cisco.
Jurassic.
**Trask Stalnaker** 17:32 scan the GCTC chat.
**Juraci Paixão Kröhling** 17:34 Yeah. Yeah, I'm gonna ask Lara.
**Alolita Sharma** 17:36 Yeah, good question.
**Juraci Paixão Kröhling** 17:39 I also removed a couple of people who left the JC. They were still there.
**Alolita Sharma** 17:45 Oh, okay, cool.
**Josh Suereth** 17:47 So, this is being recorded, so I don't want to share personal info, but that is not Jack's email address on the TC.
**Juraci Paixão Kröhling** 17:53 No? Okay.
**Austin Parker** 17:54 Do you want me to, start a new ball?
**Alolita Sharma** 17:59 True.
**Austin Parker** 18:00 Yeah, I'll start a call and put it in GC2P chat.
**Alolita Sharma** 18:03 Okay, I'll see you guys. Thank you. Bye.
