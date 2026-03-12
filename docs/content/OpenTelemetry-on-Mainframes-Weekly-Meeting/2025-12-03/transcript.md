SIG: OpenTelemetry on Mainframes Weekly Meeting
Date: 2025-12-03
Duration: 18 minutes
Zoom Recording URL: https://zoom.us/rec/share/vdTfuUwCVAcJtZLI4saUWumCGnDIQnqGeDydY2JWguxtD3JTgVsnuW6cl60xsNQI.FNuZVOrr7OIOM89y
============================================================

## Zoom Recording Transcript

**Kai Kirsch** 00:31 Hello, good evening.
**Angelika Heinrich** 00:37 Hello, we're the first ones.
**Jim Porell** 01:27 Hello, everyone.
**Angelika Heinrich** 01:31 Hello.
**Kai Kirsch** 01:32 So notice.
**Jim Porell** 01:33 I know that, rudiger's not gonna make it today.
**Angelika Heinrich** 01:38 Yep.
**Jim Porell** 01:40 And Anand as well.
Greg, I don't know if you saw the Slack, but I know Anand and Rudiger are not going to make it today.
**Greg Shriver** 02:33 I just saw that. Thank you, Jim.
So… Let's see… Okay.
Okay, I don't know if we're expecting… Morgan?
**Jim Porell** 03:01 Yeah, I don't know.
**Greg Shriver** 03:07 Okay.
**Angelika Heinrich** 03:19 I saw his comment last week, he was able… Ridico was able to find out a little bit more about the CNCF, Plans, for collector support.
For mainframe.
So… Hopefully we can get them to join a SIG and share some of their… Some of their plans there.
**Greg Shriver** 03:48 Yeah, I, let's see, today… I don't have… so, last week, I had… we had done a little show and tell, and I had shared what I was trying to do to add a doc PR.
And… and it turned out that I didn't do it correctly. And, last week, you guys provided, help for me to do it the right way. I… I did redo some of that, but I don't have a PR quite ready to share yet, so… So I did fork the repo.
And, and I did, create a branch there, and what I… but I'm not ready to actually issue the PR quite yet, because I think the net-net from last week's discussion was that rather than have us you know, have this group go over, you know, the content before doing the PR, it would be much more efficient if we just did the PR so that everyone could see, you know, and participate.
not only the people in this group, but anyone else who sees it, anyone could participate in the comments and review of that PR.
So, I don't have that ready yet, I'm hoping to have that next week.
So that's about the only update that I have to share.
Anything from anyone else today?
**Jim Porell** 05:28 Not here.
**Kai Kirsch** 05:33 Thanks, Craig. I would have a question for the SIC, basically.
I've been looking into messaging systems lately.
Specific on the broker or queue manager side, so Kafka, Revit MQ, and now for, right, for mainstream, of course, IBM MQ, and looking at, metrics.
And I know there are hotel semantic conventions, right, documented.
But they are mostly regarding the tracing aspects of spans, and also more on the producer and consumer side.
So, I was wondering, basically, if there is any… first of all, if anyone knows if there is a, messaging sick?
Right, that is working on that.
And the other question would be, basically, if there's any plans, right, regarding, semantic conventions for queue managers or brokers that provide a general approach to something, if anyone is aware, if there's some planning or documentation there.
**Jim Porell** 06:44 No, I don't know.
**Angelika Heinrich** 06:48 I think Morgan would have maybe been a good… contact for us to find out if there is a… an active messaging SIG.
I had a look, and the last… meeting with the messaging SIG seems to have been scheduled in around May, but there's no updates on their meeting notes since February.
So, I couldn't really glean from that.
Whether it's still active, or if… Maybe it's been merged into a different SIG.
Not sure. So… Maybe, we can message, Morgan in the Slack to see if he's got any advice on that piece.
I know for the pull requests so far, at least the resource attributes that we've spoken about, I don't believe… Which you guys can correct me if… If we discussed any messaging resources. I know TPS was one.
But I don't believe we've discussed… Any, Attributes or, you know, naming standards around messaging it.
**Jim Porell** 08:01 It's been basically the base operating system and hardware.
you know, we didn't do anything with respect to any of the subsystem managers, like KICS, IMS, and DB2. A lot of the… like with MQ in particular, a lot of it will be common with distributed queue.
things like unique display things I have to consider, you know. I'm a queue manager, so… But I don't think it's gonna be a huge difference.
**Angelika Heinrich** 08:36 Okay.
**Jim Porell** 08:44 Wait, Morgan, you look as cold as I feel on your, on your…
**Morgan McLean** 08:49 Yeah, it's an old photo.
I'm sorry for joining late, did you guys already get started, or are we just starting now?
**Greg Shriver** 08:59 Just getting started there, Morgan. And actually, we did have a question for you. The question was… What… what… and do we have a messaging SIG?
A SIG that covers, like, the… like, RabbitMQ.
**Morgan McLean** 09:18 Yes, I believe we do, actually.
**Greg Shriver** 09:21 Okay.
**Angelika Heinrich** 09:21 Do you know if they're still meeting?
**Morgan McLean** 09:24 It should have a meeting, it either has a… I'm just checking right now, it either would have its own meeting, or it would be part of the semantic invention sig.
**Angelika Heinrich** 09:32 Let me just take a look.
**Morgan McLean** 09:45 I think it's just part of, yeah, semantic conventions.
Yeah, there was a whole bunch of work done on it last year. I think it had a dedicated SIG, which they closed, but if we want to add things to it, we would just do that through the semantic conventions process.
I think last year they finished messaging and HTTP and possibly databases.
So, I can put us in touch with, like, Trask. Trask Delnacher's probably the right person to contact and get connected. What do we have planned? Like, obviously we're asking this because… I'm being asked this because we have some things we need to add, like, what are we looking to do?
**Kai Kirsch** 10:24 So, this is my basic question from my side. We're looking currently at messaging systems.
And I've looked at the semantic conventions that are there already, but it looks like they are more focused on the producer and consumer side, and not so much on the actual brokers or queue managers.
So, I was wondering whether SIG, if a SIG exists, already is working on that, and also whether they are already working on the… a generalization, approach, a general approach, right? Because I've seen there are changes there, to make the metrics more… more general, I would say. For example, right, we have, like, the reddish… reddish cash-hit ratio, and this is moving to cash-hit ratio, so I was wondering…
**Morgan McLean** 11:09 Let me message Trask and find out.
I'll do it on the mainframes channel, so that other people can see it and can reply.
**Kai Kirsch** 11:21 Perfect, thank you.
**Greg Shriver** 11:21 Thank you.
And I think from a, from a, from a, like, a planning and direction standpoint, I mean, I know… we had discussed on this SIG before about, you know, the desire to move forward with metrics, semantic conventions, including MQ. We just haven't had a whole lot of traction with that yet.
**Morgan McLean** 11:51 Yep, and I think for that one, like, Rudiger was working with Antoine and Trask to drive that forward. And when I chatted with Antoine, I mean, I work with him, so I chat with him a lot, but, like, we had a conversation about this two weeks ago at KubeCon. He mentioned something was coming up, but I haven't checked in with him on this specific topic.
But I think… I think something's in motion for that.
Let me… let me paint Trask here for the messaging one, and then… then we can sort of expand the conversation a bit.
**Greg Shriver** 12:24 Sounds good.
**Morgan McLean** 12:28 And Rudiger filed a PR for semantic conventions, right? Like, the issue is it's just not getting a whole lot of traction.
**Greg Shriver** 12:35 I think… so, no, we did have, I thought the one was merged.
**Morgan McLean** 12:40 Oh, great, okay, okay.
**Greg Shriver** 12:41 And there's.
**Morgan McLean** 12:41 The scores again.
**Angelika Heinrich** 12:42 This is still waiting.
**Greg Shriver** 12:44 TPS is still waiting, right? But…
**Angelika Heinrich** 12:47 But we haven't talked about any messaging or anything like that yet, or any metrics, right, up until now.
**Morgan McLean** 12:53 And for… for Trask, the question then is, like, who should you… like, we want… we have some… We have some early proposals for additions we want to make to messaging that we want to run past the people working on it to get their feedback.
Great.
**Greg Shriver** 13:05 Yeah.
And one of the other discussions, just for everybody who's new and hasn't been on all the meetings, to try and attack all of the metrics across all these different little subdomains all at once is just too big. It's almost an intractable problem, and… And what we discussed in prior meetings was that it would be probably better if we could split it up and have smaller PRs.
You know, so that a PR is very focused on, hey, we need to… we need to have… we have the need to… to have, you know, to have, certain metrics for MQ, for example, and these are the ones that we're proposing, what do you think?
Because that will spark, you know, that would spark whatever additional, you know, thoughts need to happen, hopefully. But anyway, I'm not articulating myself well, but, I mean, if we have a focused PR that's specifically for the 3, 4, 5, 6, MQ metrics we want to add, that's at least a stake in the ground.
And it would probably be easier to make progress on something that has a smaller number of proposed metric names.
**Morgan McLean** 14:27 Yep.
**Angelika Heinrich** 14:27 Correct.
**Greg Shriver** 14:27 Than something that's huge, which is how we started, and it's really difficult to make any progress with that.
**Morgan McLean** 14:33 Yep.
I'm just looking for the right thing to go.
2… BC… Alright, I will send this message to Trask.
Sent.
**Greg Shriver** 15:11 Very cool.
Thank you so much.
And one other thing, just another… I know, Angie, I know you and I have talked about this, but this call… is really late.
for everyone in EMEA.
Including Rutica.
**Morgan McLean** 15:32 Yes.
**Greg Shriver** 15:33 I, I… Should we consider… maybe either an alternate… not an alternate, maybe an alternate time, or a duplicate, I don't know, maybe we… I don't know if we have enough… enough… enough volume to have, you know, multiple calls and multiple geos, but… What are your thoughts there, Morgan, on.
**Morgan McLean** 15:56 I would suggest we stick to one, even if we move the time around. Okay. The project is small enough that I worry that fragmenting is just gonna kill all progress.
And Ruger in particular is such a… is doing so much heavy lifting that I think it's important for us to find a time to meet with them. If the time for this is challenging, I mean, we have full flexibility to move it to any time that people want, so… You know, obviously, schedules permitting, but if people want to move this earlier, that's not a problem.
**Greg Shriver** 16:26 I'm open to that. I'm sure… I expect that Rudigo would be open to that.
**Morgan McLean** 16:30 Yeah.
And Angelica, I imagine that would be…
**Angelika Heinrich** 16:34 Yeah, and there's… yeah, Kai as well. Okay. And there's a… there were a couple of other folks I'd spoken to on the side of the ocean who were interested in joining.
**Morgan McLean** 16:44 Yeah.
**Angelika Heinrich** 16:45 Made the comment that it was later.
**Morgan McLean** 16:47 Speaking for myself, I could join up to 2 hours earlier, though if it's gonna be… it'll be 8 AM Pacific, if I'm gonna do that, it can't be on Wednesdays. I could do 9am on Wednesdays, but 8 AM on Monday, Tuesday, or Thursday.
**Angelika Heinrich** 17:00 Yeah. Okay.
**Morgan McLean** 17:02 Greg, I don't know your restrictions.
**Angelika Heinrich** 17:04 Oh, go ahead, sorry. I was just gonna propose, like, a, I don't know, a Slack poll or something to see… That would be perfect. I would even be… I think even one hour earlier would be a big help, but yeah, let's see.
**Morgan McLean** 17:16 That would work great for me, too. Yeah.
**Angelika Heinrich** 17:19 Yeah.
**Morgan McLean** 17:20 Alright, Angelo, if you want to just…
**Angelika Heinrich** 17:22 Punch in a secpole, that'd be great. I can put… punch in a secpole, yeah. So you said up to 2 hours earlier, yeah?
**Morgan McLean** 17:27 Up to 2 hours on… for me, on Monday, Tuesday, or Thursday. 1 hour earlier is fine on Wednesdays.
**Angelika Heinrich** 17:33 Oh, on Wednesdays, okay.
**Greg Shriver** 17:34 Okay.
Monday, Tuesday, or Thursday, 2 hours earlier, Wednesday, up to 1 hour earlier.
**Morgan McLean** 17:41 Yes, I'm a horrible boss, and my team weekly meeting is at 8 AM Pacific on Fridays, so that one I also can't…
**Greg Shriver** 17:47 God.
Note to self, don't worry.
**Morgan McLean** 17:50 Half my org's in Europe, so it's the exact same constraints.
**Angelika Heinrich** 17:54 I see.
**Morgan McLean** 17:55 Like, I have pretty early mornings, yeah.
**Angelika Heinrich** 17:58 Okay.
Pop that in.
Okay.
**Greg Shriver** 18:13 Cool.
**Angelika Heinrich** 18:15 Yep.
**Morgan McLean** 18:16 Any other topics?
then we can probably wrap up. I just followed up with Rudiger, looks like we'll be reaching out to the CNCF about, getting GitHub runners, or GitHub Action Runners, for mainframes, which would be huge.
So, hopefully we hear more about that soon.
**Angelika Heinrich** 18:36 Awesome.
**Morgan McLean** 18:37 Great.
**Angelika Heinrich** 18:39 Thank you!
**Greg Shriver** 18:40 Yeah.
**Morgan McLean** 18:40 all later. Thank you all. Maybe an hour earlier.
**Jim Porell** 18:42 Yeah.
**Morgan McLean** 18:43 Alright.
**Jim Porell** 18:44 See ya.
