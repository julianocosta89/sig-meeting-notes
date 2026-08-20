SIG: Developer Experience SIG (EU)
Date: 2026-08-19
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Juliano Costa | Datadog** 00:28 Hello, hello!
**Johanna Öjeling** 00:30 Hello!
**Juliano Costa | Datadog** 00:34 Good morning.
**Johanna Öjeling** 00:35 Hey! Morning! How are you doing?
**Juliano Costa | Datadog** 00:42 Yeah.
Beget, beget.
How about you?
**Johanna Öjeling** 00:52 How is it going with all of the torque preparation?
**Juliano Costa | Datadog** 00:57 The talks are the good part, yeah. It's just the… all the other stuff.
It's funny because, like, It's part of the job, but, like, you still have the job, so…
**Johanna Öjeling** 01:11 - Yeah.
**Juliano Costa | Datadog** 01:15 Oh.
**Johanna Öjeling** 01:17 Yeah, also quite busy since I'll be off tomorrow and on Friday, so trying to kind of wrap up things, yeah, before I go on vacation. And also we have some, like, team activities next week, and… Yeah, but… yeah, looking forward to having an extended weekend, and… Just switch off completely.
**Juliano Costa | Datadog** 01:44 Yeah, sounds good. Well, I aim you a bit.
Cool.
Let me just put together the agenda for today. I don't think we have anything to discuss if Perk doesn't join.
No.
Because we already discussed last week, and I think you, You opened… I saw that you opened the issue on the OpenTelem3.io.
**Johanna Öjeling** 02:15 Yes.
**Juliano Costa | Datadog** 02:16 And I reached out to James, and also added him to the docs.
to the… to the Atlassian, blog post, so he can… he could read me off.
So I think…
**Johanna Öjeling** 02:28 Thank you.
**Juliano Costa | Datadog** 02:28 Yep.
The things that we had painting from last week are done.
**Johanna Öjeling** 02:33 - Nice.
Hey, folks.
Oh, hello!
**Perk (Marcin Stożek) | Elastic Ingest** 02:40 Apologies.
**Johanna Öjeling** 02:41 Welcome back!
**Perk (Marcin Stożek) | Elastic Ingest** 02:43 Thank you.
**Johanna Öjeling** 02:43 What's your, time off?
**Perk (Marcin Stożek) | Elastic Ingest** 02:45 Oh, very well. And then I waited, like, 2 minutes on the other link that we've used before.
**Johanna Öjeling** 02:51 Oh… Perk (Marcin Stożek) | Elastic Ingest 02:53 Yeah, it was funny, but okay, okay, I'm here. Yeah, yeah, it was very good, but I have literally no idea what I was doing 3 weeks ago, so I need to catch up. It was good.
Thank you.
Was your talk? Ready?
for October?
**Johanna Öjeling** 03:12 I'm making good progress.
**Perk (Marcin Stożek) | Elastic Ingest** 03:15 Phew!
**Johanna Öjeling** 03:17 Yeah, did you… are you joining the Cloud Native Denmark?
Perk.
**Perk (Marcin Stożek) | Elastic Ingest** 03:23 No, unfortunately, my talk got declined, so I'll…
**Johanna Öjeling** 03:26 Okay.
**Perk (Marcin Stożek) | Elastic Ingest** 03:27 be there. No. No, no, no. Cannot be there. I'm going to be there on the OSMC instead.
That is quite close to that.
**Johanna Öjeling** 03:35 Okay.
**Perk (Marcin Stożek) | Elastic Ingest** 03:36 In Nuremberg.
**Johanna Öjeling** 03:39 Oh, okay.
**Perk (Marcin Stożek) | Elastic Ingest** 03:40 Like, a day before, I think.
**Johanna Öjeling** 03:42 Okay, nice. But yeah, it will be super nice to meet up in Prague.
**Perk (Marcin Stożek) | Elastic Ingest** 03:48 In Prague. Yeah, yeah, yeah.
**Johanna Öjeling** 03:49 Yeah.
**Perk (Marcin Stożek) | Elastic Ingest** 03:49 We're going to Denmark as well?
**Johanna Öjeling** 03:52 Yes, yes. It's very close, to me. It's, like a, 25-minute train ride from Malmber Island to Copenhagen.
**Perk (Marcin Stożek) | Elastic Ingest** 04:04 You're in Mammo! Okay, great. Okay, okay, okay, yeah. Oh, yeah, come on, yeah, it's super, super close.
**Johanna Öjeling** 04:10 Yeah.
**Perk (Marcin Stożek) | Elastic Ingest** 04:10 Very nice. Actually, you know, to see this bridge.
**Johanna Öjeling** 04:13 Yeah, - Perk (Marcin Stożek) | Elastic Ingest 04:14 So, it's amazing. Okay.
Okay, fingers crossed.
For that.
So guys, brief me, brief me in. I mean… And so we have a lot of… a lot of things in the agenda there, but is there any update for the blog post? Is there anything for me to do?
**Juliano Costa | Datadog** 04:36 No, just opened the PR.
**Perk (Marcin Stożek) | Elastic Ingest** 04:38 open up Okay.
**Juliano Costa | Datadog** 04:40 Yeah, okay, good.
**Johanna Öjeling** 04:41 I think it's been approved across the board.
**Perk (Marcin Stożek) | Elastic Ingest** 04:45 Very well. Yeah, okay.
**Johanna Öjeling** 04:46 So, yeah.
**Juliano Costa | Datadog** 04:47 I really like the trace that you added there.
**Perk (Marcin Stożek) | Elastic Ingest** 04:52 Oh, that was not me, I just…
**Juliano Costa | Datadog** 04:53 Yeah, yeah, yeah, but anyways, I think it's nice to see in, like, a concrete.
**Perk (Marcin Stożek) | Elastic Ingest** 05:01 Exactly, it is in action, right? Yeah, exactly.
**Juliano Costa | Datadog** 05:03 Yeah.
**Perk (Marcin Stożek) | Elastic Ingest** 05:03 used it, and it shows exactly what is happening. Yeah, yeah, yeah.
**Johanna Öjeling** 05:07 Yeah, I also think those were great additions, so yeah, looking forward to, Perk (Marcin Stożek) | Elastic Ingest 05:13 Very well.
**Johanna Öjeling** 05:13 Yeah, they.
**Perk (Marcin Stożek) | Elastic Ingest** 05:14 So you're saying, okay, I need to catch up on Slack, I need to create a PR for the dogs, probably, or some.
**Juliano Costa | Datadog** 05:21 Yeah, it's on the docs, I think there is a folder called logs.
**Perk (Marcin Stożek) | Elastic Ingest** 05:27 Okay, okay, okay, okay, I'll do it.
**Juliano Costa | Datadog** 05:29 Yeah, if you need any help there, just drop a message, I can go over it with you. But it's pretty straightforward, and it's Markdown file, so I think it's.
**Perk (Marcin Stożek) | Elastic Ingest** 05:41 Oh, okay.
**Juliano Costa | Datadog** 05:41 to… Change the titles so it, like… Perk (Marcin Stożek) | Elastic Ingest 05:46 Gets.
**Juliano Costa | Datadog** 05:47 The proper level of type, of, heading.
But although… the others are fine. Like, I think the main title you do not put, because it's the title of the page.
Okay. And then all the rest is plain text, and for the image, you may need to create a folder, so you add the image.
**Perk (Marcin Stożek) | Elastic Ingest** 06:08 Okay.
**Juliano Costa | Datadog** 06:09 But, like, if you take a look at previews, blog posts.
**Perk (Marcin Stożek) | Elastic Ingest** 06:12 Yeah, yeah, yeah, I'll do it. Exactly.
**Juliano Costa | Datadog** 06:15 And, I'm pretty sure that if you point your agent, Perk (Marcin Stożek) | Elastic Ingest 06:19 Oh, yes.
**Juliano Costa | Datadog** 06:20 We'll figure out.
**Perk (Marcin Stożek) | Elastic Ingest** 06:21 Yeah, then rewrite everything.
Yeah, yeah, I don't like that.
**Juliano Costa | Datadog** 06:25 That's not posted.
**Perk (Marcin Stożek) | Elastic Ingest** 06:26 I will rerun it.
You never know.
**Juliano Costa | Datadog** 06:29 Do ya?
**Perk (Marcin Stożek) | Elastic Ingest** 06:32 Okay, okay, okay, I'll do it.
**Juliano Costa | Datadog** 06:33 Yeah, this one is ready.
we have the other blog from Atlassian that Vidya wrote, and I want to briefly discuss that with… I think, Johanna, you went through. Did you take a look at the blog post, Perk? By any chance?
**Perk (Marcin Stożek) | Elastic Ingest** 06:52 No, I didn't. But I'll do it, I'll do it, okay.
**Juliano Costa | Datadog** 06:56 No worries. Yeah, I just want to briefly talk with Johanna.
I… while going through, I found that the blog is too long.
**Johanna Öjeling** 07:08 -
**Juliano Costa | Datadog** 07:10 I don't know if readers will go through, even though, like, the whole story is great. They have a really nice usage and configuration, and it's super well detailed.
But I feel that, maybe it's because, AI is used, to write. It has a lot of, what is the word? It's a lot, obnoxious, so it gets through.
**Johanna Öjeling** 07:41 repeating it.
**Juliano Costa | Datadog** 07:41 And not getting to the point, and then, like, he talks and talks, talks, and then talks again to… Get to a point.
So…
**Johanna Öjeling** 07:51 Yeah, -
**Juliano Costa | Datadog** 07:51 I think we could… Shorten a bit.
**Johanna Öjeling** 07:56 -
**Juliano Costa | Datadog** 07:57 I tried to… to give that feedback to Vidya on, I wrote on the… on the doc, but I also sent her a message.
**Johanna Öjeling** 08:06 -
**Juliano Costa | Datadog** 08:07 And then she reached out to me, and I told her that as I added James, let's wait to see what James says.
**Johanna Öjeling** 08:17 Mmm.
**Juliano Costa | Datadog** 08:17 And we can, move on with that.
**Johanna Öjeling** 08:21 Yeah, I think that's good feedback, because it's, yeah, like, readers may, you know, lose attention, when it's too long, so if we could maybe, like, skip some sections entirely, or make it more concise. And I even… I was struggling with that when I… with the Skyscanner post, because that was quite a long interview, like, one and a half hour, I think, in total, and they provided quite many, like, lessons and examples, so it's like, okay, how… how much should we actually… like, this will become longer than the others, but if there is too much, like, readers won't have the, kind of, energy to… to go through it all.
So I think… Yeah, I agree with your feedback there.
**Juliano Costa | Datadog** 09:18 Another thing I think the… the charts could get some, love.
So, if we approve the story and the writing, I may just open myself. I scholar and, like.
Yeah. I'm too picky for those things, like, I can't.
**Johanna Öjeling** 09:37 -
**Juliano Costa | Datadog** 09:39 I can't sleep at night if it's not aligned, or if the line is crossing the box, like, no, please!
Yeah, so I… but I, I think this… for that, I would just, Yeah, try to… to sketch something myself.
**Johanna Öjeling** 10:01 - yeah, I think, diagrams could be simplified.
**Juliano Costa | Datadog** 10:07 Ms.
Yep.
**Johanna Öjeling** 10:11 But then, yeah, also that's the… What content to actually… keep. So yeah, maybe some content will disappear then, the diagram.
Yeah. Yeah. But then, did James say… So he confirmed that he would… he would take a look at it, or… Yeah, okay, that's good.
**Juliano Costa | Datadog** 10:36 Yeah, so I, I pinged, I pinged him on, Slack.
And… after a couple of days, he replied.
And said, hey, I'm not using this Slack anymore, and then he pointed me to another user.
**Johanna Öjeling** 10:51 But he passed it.
**Juliano Costa | Datadog** 10:52 He pointed… he gave me his email, so I invited, him to… to… to the doc, and share the message with him. But I did that on Monday, so… yeah, I think this week.
**Johanna Öjeling** 11:05 It will. Okay.
**Juliano Costa | Datadog** 11:06 Corp.
**Johanna Öjeling** 11:11 Yeah.
Nice.
Yeah, thank you for reaching out to him.
**Juliano Costa | Datadog** 11:16 Yeah, no worries.
**Perk (Marcin Stożek) | Elastic Ingest** 11:20 I have a question for this KeyClock blog post. Where did we end up with the… where do we post it, actually? Whether that is, OpenTelemetry, or CNCF, or something else?
**Juliano Costa | Datadog** 11:35 Yeah, I… I had a to-do to me to check, and I never checked, so… That's on me.
**Johanna Öjeling** 11:44 Mmm, on the CSF club.
**Perk (Marcin Stożek) | Elastic Ingest** 11:48 I assume that's… that's still there, like, this could be pursued, this idea, right? Of posting this there on the CNCF. Okay, maybe I can do it as well. If you know who should we ask and where?
**Juliano Costa | Datadog** 12:04 Give me a second, I'll… I'll send a message on… on the CNCF Ambassadors that I have. It's a back channel here.
**Perk (Marcin Stożek) | Elastic Ingest** 12:15 Okay.
**Juliano Costa | Datadog** 12:15 And I… I… I'll let you know, whenever I hear back from them. But I'll send a message right away, otherwise I'll forget.
**Perk (Marcin Stożek) | Elastic Ingest** 12:30 Very well, thank you.
**Juliano Costa | Datadog** 14:13 Okay, posted. I'll… I'll let you all know.
**Perk (Marcin Stożek) | Elastic Ingest** 14:16 Awesome, thank you, thank you. Because if I remember correctly, the idea was that to me, you could maybe put it on CSCF, and then cross-post it from the OpenTelemetry, and maybe, Keyclog could do the same on their blog post, like, create some very short version, and then just said, hey.
session.
**Juliano Costa | Datadog** 14:33 Yep.
**Perk (Marcin Stożek) | Elastic Ingest** 14:34 Okay, okay, okay, okay. So, please ping me.
But,
**Juliano Costa | Datadog** 14:37 Yeah, as soon as I hear something, I'll let you know.
**Perk (Marcin Stożek) | Elastic Ingest** 14:43 Thank you.
**Juliano Costa | Datadog** 14:43 Awesome, thank you.
Okay, and the other thing that I had to do, that was also from the same day that we discussed, was about Richard Joan to talk about Envoy.
So, we'll do it right now again, because, yeah.
**Perk (Marcin Stożek) | Elastic Ingest** 15:07 Yeah, come on.
That'll work, that works.
**Juliano Costa | Datadog** 15:09 I'm struggling to keep track of the things.
**Perk (Marcin Stożek) | Elastic Ingest** 15:13 No, no, no, I think that's okay. You know, like, for me, actually, for me, this is like, you know, like, working from the same room. Doesn't mean that we have to, like, you know, like, talk about everything, but doing some stuff on the side.
on the topic, I think that's okay.
**Juliano Costa | Datadog** 16:20 Okay, massage sent. Yay!
**Perk (Marcin Stożek) | Elastic Ingest** 16:24 Great.
**Juliano Costa | Datadog** 16:25 I can check, check out those boxes in my head now.
**Perk (Marcin Stożek) | Elastic Ingest** 16:29 Oh, yeah.
Oh, yeah, yeah, that's important.
**Juliano Costa | Datadog** 16:34 Okay, Cool, yeah, I don't have any… anything else to… Perk (Marcin Stożek) | Elastic Ingest 16:44 Me neither. I'm good for now.
**Johanna Öjeling** 16:45 Yeah, no.
**Juliano Costa | Datadog** 16:46 to discuss Okay.
**Perk (Marcin Stożek) | Elastic Ingest** 16:50 Very well.
**Juliano Costa | Datadog** 16:50 then…
**Johanna Öjeling** 16:51 Good, so let's see when, yeah, what the reply will be, and… Yeah.
**Perk (Marcin Stożek) | Elastic Ingest** 16:56 Exactly.
**Johanna Öjeling** 16:56 Yep.
**Perk (Marcin Stożek) | Elastic Ingest** 16:58 Good to see ya.
**Johanna Öjeling** 17:00 Good to see you too. Enjoy the rest of your day. Bye.
