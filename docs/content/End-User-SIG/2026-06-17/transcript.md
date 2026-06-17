SIG: End-User SIG
Date: 2026-06-17
Duration: 61 minutes
============================================================

## Zoom Recording Transcript

Andrej 00:03:30 Okay.
We have… So, there's two of us again, and… a Ultra AI note ticker.
This happens to all, so, so frequently.
Yoshi Yamaguchi 00:03:47 That's us.
Yeah.
Andrej 00:04:21 But yeah, Adam is on his way.
Yoshi Yamaguchi 00:04:23 Oh.
Andrej 00:04:49 Yeah, and by the way, you… when writing the… In the attendees list, you included affiliation, Yeah. Like, the company name?
Yoshi Yamaguchi 00:05:00 Ugh.
Andrej 00:05:01 I don't think it's, like, a bad idea, but we never did it before.
Yoshi Yamaguchi 00:05:06 Really, because in other SIGs, like, semantic convention 6 and in others, We… we put affiliations alongside.
Andrej 00:05:18 Okay, okay. In that case…
Yoshi Yamaguchi 00:05:23 But it seems like the Indonesia City is not following that convention, so it's fine.
Andrej 00:05:29 But I can now open it with… with folks tomorrow.
Adam Gardner 00:05:31 Hello, hello, hello.
Andrej 00:05:34 Never know.
Yoshi Yamaguchi 00:05:35 But.
Adam Gardner 00:05:36 Select a speaker, let's pick that one, and hopefully I'm better at my, technology today.
Andrej 00:05:44 Yeah, yeah.
Adam Gardner 00:05:45 No, clearly not.
This is gonna be a regular thing, isn't it? Every single time. Adam's useless.
Sound.
There we go. Good.
Andrej 00:06:00 Hello, Adam, can you hear us now?
Adam Gardner 00:06:02 I can, how are you, gents?
Andrej 00:06:05 All good? Good. Yeah, yeah.
I was just telling Yoshi that I was… pushing this to-do to actually share resources and create a meeting for quite some time. And then, when I eventually got to it, I almost didn't manage on time, because Yeah, because it just takes time, you know? Like, you have to get, like, people involved, and… and, for, like, so they can get help with that, but eventually, Marilla created the event and the link, so yeah.
Here we are at the official, official meeting with OfficialLink.
Yoshi Yamaguchi 00:06:44 Nice.
Andrej 00:06:45 what we were talking about with Yoshi is that, this is… there is an event in OpenTelemetry Calendar, And, Yeah, so if you want to, like, see it and see all the other events, I'm not sure if you subscribe, Adam, already or not, but yeah, I added a calendar link there, so… Yeah, going forward, we'll be… I will not be creating, like, my own, meetings, but, we can… we can join this one right away.
Adam Gardner 00:07:19 Perfect, I'll, yeah, I'll subscribe to that so I know what's going on. That's a good idea.
Andrej 00:07:24 Sounds good, sounds good. Adam, what's the time where you are located?
Adam Gardner 00:07:29 It's just gone 5pm.
Andrej 00:07:32 And is it dark outside, or… because I think it was, like, a bit less dark. Interesting. So in Australia, it gets dark already at 5pm.
Yeah, because…
Adam Gardner 00:07:42 data.
Andrej 00:07:43 But you have winter? Yes, yeah, yeah, okay.
Okay, okay. Now it all makes sense. Now it all makes sense.
Alrighty.
Shall we jump right in?
Yeah.
Yeah, we're also discussing, conventions for writing people's names into attendees list.
Adam Gardner 00:08:10 And…
Andrej 00:08:11 Now I realize that we also don't use the tags that I used wrongly, so I rewrote it as just normal, normal names. Anyway… Folks, awesome that we are here again, and we are meeting.
Today, I'd like to go through the resources that I shared with you.
couple of days ago.
And perhaps discuss what… what you could… what kind of work you could potentially pick up, or not yet. There is no… no rush with this. As you folks mentioned, that you might want to also just, like, observe for some time, or join other people on… on some things. It's totally… totally fine as well.
And, tomorrow, we have… a usual end-user SIG meeting, so… If we have any… questions to discuss with folks, I'll be happy to bring it there as well.
So… So that's… that's it so far.
Anything you'd like to discuss?
Yoshi Yamaguchi 00:09:21 So, I have one question regarding the blueprints. So I am translating the documentation into Japanese, and then a blog as well.
And then I… I saw a couple of examples from Skyscanners.
And other… I forgot the other… Which one? New Relic, I guess?
Yeah, anyway, so that was… to… to… to… So, those blog posts were about… explaining… how they applied OpenTremetry into their system, and how they… improved… their operations based on those symmetries. So… Is it… is it… how do they, like, ask… the end users to write the draft, or, like, the broke entries.
to the OpenDemetery blog, and then how… I'd like to know the process. So if… if it's okay for me to, like, reach out to the end users in Japan, and then ask them to, like.
make a request to the OpenTemmetry.io repository directory, then, you know.
I… I can start out that part as soon as possible.
Andrej 00:10:46 That sounds great, that sounds great. So the question is, how can you start with…
Yoshi Yamaguchi 00:10:52 Yeah, so is there any, yeah, is there any criteria?
for… for… to… to post their, like, use case onto OpenDemetery blog.
Andrej 00:11:05 So, I think there are criteria.
I actually am not aware of that Skyscanner and New Relic blog post that you mentioned, but… There is an issue template.
for… posting blueprints. This is something that Dan was working on with… with other folks, with Lucas and Tiffany, other folks in the last couple of months, and they are trying to come up with a A standardized way how to… how to share and come up with blueprints.
and reference architecture. So there are two things, blueprints and reference architectures.
Let me quickly find like that.
Or reference implementations, yeah. Dan wrote a blog post about this some time ago.
And my understanding is that anyone can use the issue template to come up with a proposal.
And, then it's just for, like… your… thing to move it forward. People will be giving feedback, and and it's… I think that's kinda… it's kinda… it. I don't know where does the creation of Of blog posts fit into this process?
But I'm sure that Blueprints folks would be able to tell you more about this.
If blueprints are interesting for you, I think it might make sense to try to get Dan join this meeting next time, if it would be possible for him, and he would be able to share more details.
How does that sound?
Yoshi Yamaguchi 00:13:09 Yeah, sounds good, and then I just found that the blueprint is… different from the Q&A one.
So.
Andrej 00:13:17 Yes.
Yoshi Yamaguchi 00:13:18 I was… I misunderstood, and I was confused about the difference between the Q&A and Blueprint. So Blueprint is more for differential architecture.
thing, whereas Kyundai is more… Use a use case-based… Kyundai.
Andrej 00:13:38 Yeah. Yeah, yeah, yeah. Okay, so… So, there are two different things. So, there are those live streams that we do. They are called, Hotel Q&A.
Q&A.
Or, I think this is how it was… how it was used… how it was used to… Jesus, that's terrible grammar. How… It used to be called… yeah, that's probably the right way how to put it. Now, it used to be called before, now we call it hotel… Me?
Yoshi Yamaguchi 00:14:10 Oh, okay.
Andrej 00:14:11 Something like that. Then we have… Hotel in practice.
Yoshi Yamaguchi 00:14:16 Yeah.
Andrej 00:14:18 So, OTELME is with end users.
Hotel in practice is with contributors who want to talk about some, some, like, cool new concepts, whether… with hotelme, it's more just, like, talking about people's normal setup. It doesn't have to be something, like, eye-opening and super special.
Hotline practices, on the other hand, like, something new and special. Then we have… A couple more, so let me… let me open this.
Yeah, what's up in Hotel? This is a rather new one.
That's about… Updates from SIGS.
Yoshi Yamaguchi 00:15:03 Oh, and I see.
Andrej 00:15:06 Hotel… they don't have… People of Hotel, or… Oh, that's cool.
Huh.
No, I don't remember how it's called. Humans are hotel, no, not people are hotel. Humans are hotel.
And that's the last one, I guess. That's about… intros of individual contributors who contribute to Hotel, just to get to know the community.
So this, these are usually happening at conferences, where people just do, like, quick profiles, like, short interviews, sharing stuff about the contributors.
This is one part, this is the YouTube… stuff, and then the blueprints part is a separate one that's not as video-focused, it's more, text-focused and block-focused, and it's quite a bit more structured. At the same time.
it doesn't mean that we cannot combine these together. Like, we can have, like, a blueprint And then… do a hotelme session with end users who follow that blueprint. I think it would be actually pretty awesome if these, like, multiple things could, like, nicely fit.
Fit together, and if you could… if you could connect them all.
So… but I love that you mentioned that you are thinking about getting some Japanese, people Talk about their setups.
Yeah. Do you want to.
Yoshi Yamaguchi 00:16:58 Go ahead. Yeah, so, can you, can you open the blog, blog post link? I just shared on Zoom?
Andrej 00:17:05 Okay.
Yoshi Yamaguchi 00:17:06 Zoom chat.
Andrej 00:17:08 Oh yeah, I see now.
Yoshi Yamaguchi 00:17:11 So this one is kind of a little bit old, 3 years ago, and then…
Andrej 00:17:15 Just one.
Yoshi Yamaguchi 00:17:16 Is this the use case from the, light step?
Yeah.
Andrej 00:17:21 And then…
Yoshi Yamaguchi 00:17:22 This one is… this one seems to be a Q&A, but it's all written and it's not YouTube, so I must… I was wondering what type of… Content is this?
Andrej 00:17:37 Yeah, yeah. I think back then, what we've done was also that we were posting, transcripts from the YouTube.
as blog posts. So I think that might be… that might be… that might be it. We stopped doing it, but just because we didn't have time, I guess.
Yoshi Yamaguchi 00:17:55 Yeah, you need to kind of burden, yeah.
Andrej 00:17:58 Yeah, yeah, but I think it's, it's just a great way to… To spread the information, across… different places, so if you would like to run HotelMe and then do a blog post, I think it would be… It's, like, totally okay to use the same resources for both.
On both channels.
Adam Gardner 00:18:21 I think that's a great idea, getting the subtitles and then running it through AI, and having a… and then just, like, saying, this is a snippet, you know, if you want to watch the full video, go over here.
Andrej 00:18:36 Yeah, yeah.
Let me… let me write it to the… to the agenda, just again, so we have… Sorry. Go ahead, Ellen.
Adam Gardner 00:18:47 I'll let you write that up, and then I'm just formulating my thought on that, actually. Let me know when you finish typing.
Andrej 00:19:14 Oh, yep.
Adam Gardner 00:19:16 I forgot what I was gonna say.
where… so if I… if I was experimenting with something like this, taking… taking the subtitles, or… and… and doing a short, like a… a vertical format, maybe, or a… like a teaser blog post to then point people to the video, where would I then share the output of that?
So that other people in the SIG could say, yeah, that's great, or no, it's rubbish, get rid of it, doesn't work.
Andrej 00:19:50 That's also a very good question. We do not have any, or at least I'm not aware of any.
Like, cloud… Like a commonplace.
Adam Gardner 00:20:02 Yeah.
Andrej 00:20:03 Yeah, yeah. So what we do is that we mostly share it From our personal cloud storage.
Adam Gardner 00:20:09 Okay.
Andrej 00:20:10 So, it could be your own Google Drive, it could be… people, like, have their own Google Docs to use. Mostly we use Google stuff, but… There is no, like, it's, it's, it's just, like, a best… somehow happened that we did it this way, but feel free to use whatever you want, and yeah, I don't think we have anything shared. The only thing that is shared is the repository.
But it's not a good place to share, videos of, like, this type of content, so…
Adam Gardner 00:20:41 But then, if I find a place to host stuff, where would I put the links? Where is everybody congregating so that I could say, hey, check this out?
Andrej 00:20:51 Yeah, once it's done, and once it is, approved by everyone, it gets posted to YouTube.
So, people, people did it this way.
Adam Gardner 00:21:01 Oh, it's the middle bit, so where… if I've done something, where would I put it so that people could say yay or nay?
Andrej 00:21:08 I would put it on my personal Google Drive.
shared with the rest of the SIG, and if they say it's okay, then it would get uploaded to YouTube.
Adam Gardner 00:21:18 Just on… on Slack, okay, okay.
Andrej 00:21:21 Oh, oh, now I… okay, sorry, I didn't get Yes, and then on Slack, yeah, Slack would be the best, I guess.
Adam Gardner 00:21:28 Okay.
Andrej 00:21:28 or during these meetings, but I think Slack is better because it gets more visibility.
So, it's a combo. On Slack, you get more visibility. Also, there's risk that actually nobody will respond. During these meetings.
It's… you kind of force people to… to respond, because… They join, and they go through the agenda, so they will respond. But it's not as many people as on Slack, so, you know, pros and cons. But what I would recommend to do is to… posted to either the agenda for… so, Slack, plus the agenda for our meeting, or the agenda for… For the regular one.
Yeah.
Adam Gardner 00:22:10 Okay.
Andrej 00:22:24 Okay, so I'll try to write this down as well.
So you mentioned you would like to start with short format, basically just creating clips from existing videos that could point people to those existing videos, is that correct?
Adam Gardner 00:22:42 Yep, yep.
Andrej 00:22:50 That's amazing, that's amazing. Yeah, there were these kind of ideas before.
But I don't think anyone actually… Actually, like, started, really. Lisa, who is now more focused on the… on the… on the communications stuff, she was working on this.
Adam Gardner 00:23:17 So I don't want to step on toes if there's a communication… what does the communication SIG do, and…
Andrej 00:23:25 That's a very good question. I have absolutely no idea of what is the, like, boundary. We have communication sick that Kinda does the blog post, and does… Yeah, some of the communications… interestingly, CommunicationSeq is mostly, like, my understanding is it's mostly about the website.
about… They have the keys from the blog post.
And they do… What else is there?
They do love, like, ottoman stuff.
So, for example, like, creating this meeting was, for some reason, part of the ComSig, like, it was in the ComSig repository. At the same time, I don't think there are, like.
They do some… some part of, like… to some extent, they are involved with social media, but it's mostly the end user, my understanding is. Also.
I guess they can post to YouTube, but again, I think mostly CN user posts to YouTube. So it's… it's, like, very blurry, it's not, like, very clearly deliminated.
Adam Gardner 00:24:36 Okay.
Andrej 00:24:36 who is responsible for what. I think it's okay to… For you, and for the short format videos, to just… do it within the secant user.
Adam Gardner 00:24:49 Okay. Do me a favor, then, and drop, I didn't catch the name, but if you drop the name either in Slack now or in the Google Doc for the meeting notes, I'll have a play around with stuff, and then I'll run it… I'll make sure to tag That person in.
Just, you know, just in case it kind of goes out, and then someone goes, hang on a minute, I didn't… See that?
Andrej 00:25:15 Got it, got it. I don't think, like, I think it's a good idea to do it, absolutely.
At the same time, let me find it, I will share a link, too.
Wow.
Okay.
I don't know where communication sig lives, actually, so now I'm lost. Yeah.
So I'll pause here… I think that's Lisa's name, but let me double check.
Holy smoked.
Yeah, so I think it's totally fine to tag Lisa there. I think we should be able to even find it somewhere… Somewhere in our… project board. As I told you before, the project board is still a little bit of a mess.
And, yeah, I didn't have a chance to clean it up. But I found a… I found a discussion.
So you can basically just say that you are… You're continuing the work.
Okay.
Literally just started.
And it seems that she already, like, prepared some stuff, so we might actually find something, useful there.
Adam Gardner 00:27:24 Cool.
You don't have access to this thing. Okay, I'll get…
Andrej 00:27:31 to GitHub, OpenTelemetry, or we should.
Adam Gardner 00:27:33 No, I've gone through the Google group for the end user SIG.
Just to try and get the calendar… to get subscribed to the calendar. But I think I've just requested access, so that'll go to someone, and then…
Andrej 00:27:48 Okay, okay.
Adam Gardner 00:27:49 I think, I think I'm in now, yep.
Andrej 00:27:52 Okay.
Adam Gardner 00:27:53 Conversations. There we go. Perfect.
Andrej 00:27:56 Super cool.
Nice, so you folks both now have… have… Something? Or, like, So, Adam, I think for your part, I think this is pretty straightforward, and no… Because, like, there is… there is… there are videos, you should just create shorts and get… get them… get feedback on them from… from, from folks. Who I would recommend you to get feedback from is… Israelis.
Adam Gardner 00:28:30 Okay.
Andrej 00:28:31 And Adriana.
Because I think they do most of the video stuff.
These days.
Yoshi Yamaguchi 00:28:42 Adriana is in your same… is in the same company as you, right, Adam?
Adam Gardner 00:28:47 Yeah, yeah, yeah.
Yoshi Yamaguchi 00:28:48 Okay.
Adam Gardner 00:28:48 there.
Both autonometrace, yep.
Yoshi Yamaguchi 00:28:51 Nice.
Adam Gardner 00:28:53 Which makes it nice, because she can then join the Europe-friendly meetings, and then we'll sort of have a chat, and it's good, it works out well.
Yoshi Yamaguchi 00:29:00 Nice.
Andrej 00:29:03 Very, very good.
Alrighty, alrighty. So, for Adam, we have it… this is kind of sorted.
I'll post it here just for… so we have it.
shorts… and Yoshi, you mentioned that you would like to start with, with… And I… this one, I just want to clarify. So you want to start with proposing a blueprint? Because, like, a blueprint is… Hey.
Yoshi Yamaguchi 00:29:38 Blueprint is more, more, more, like, general architecture, difference architecture explanation, and then whereas the Q&A is all, like, other use case spaces is, is a different one.
And then…
Andrej 00:29:52 Yes, yeah, so the Q&As are really more focused about, like, the person who is talking. They can talk about whatever they want, and it's less of a, like, process involved. Blueprints are more process-focused, and use cases are just as an illustration.
And it's more of, like, the text stuff. You can combine them both, absolutely.
But you can also pick just one.
Yoshi Yamaguchi 00:30:18 So, yeah, yeah.
Andrej 00:30:19 Which of them… what would work the best for you?
Yoshi Yamaguchi 00:30:23 Yeah, I was wondering, for, use case-based blog entries, like, like the ones… covered by the YouTube interviews, but because, yeah, because Japanese developers are not, like, comfortable with showing themselves in front of the large audience.
Always there, with his… with their, you know, face.
So… They prefer written format.
Got it. In the case of these kind of activities.
So…
Andrej 00:31:00 Okay, wonderful, that sounds great, sounds great. So… It would be basically the same thing that we do in OTelMe videos, but it would be just written, so we make it more approachable.
Yoshi Yamaguchi 00:31:11 Yeah.
Andrej 00:31:24 Wonderful.
There is a template for HotelMe, Let me share with you real quick.
And there is… I think there is, like, a list of questions. Yes, there is an interview template, there. So, when you will be creating something like that, you have… you have, like, a starting point. Feel free to turn it around whatever way works for you.
Yoshi Yamaguchi 00:32:00 Because I'm in a localization SIG as well, my idea is to… put the Japanese version first.
and then reverse translate it. Reverse translate those Japanese blog posts into English.
So that's more, like… so that's to… so that the, like, broader audience can read.
the contents.
Andrej 00:32:23 Yeah.
Yoshi Yamaguchi 00:32:24 So that's…
Andrej 00:32:25 It's a great idea.
Yoshi Yamaguchi 00:32:26 Yeah.
Andrej 00:32:38 Awesome, awesome. So we actually have, very clear next steps for you folks, that's amazing.
Hmm.
Regarding the… the… other things. As I mentioned, one thing what could be pretty cool is to get a better overview of how Blueprints work. Would this be interesting for you? Because I would be happy to ask Dan to join us and talk about it.
a little bit. Do you think you, you… But, again, just if this is… If this is something you folks might be interested in.
Yoshi Yamaguchi 00:33:20 Yeah, yeah, I'm interested. Yeah, I have a couple of… I have a couple of the… The contacts… That, from the large companies who are using OpenTeametry in it.
And then they… they have… they have solved a couple of challenges, technical challenges, from OpenTimetry's performance issues, so they should have something to show.
For the blueprint, I guess.
Andrej 00:33:52 Awesome, awesome. Yeah. Yeah.
By the way, one thing, worth mentioning is that, as I said, we don't do a great job of tracking our work with issues, but we are trying. So… it would be great if, for those two things that you… that you want to work on, if you would create issues for them. For Adam, I think you can… you can just continue working on that on that issue that I shared with you already.
If that… if that… covers.
What do you want to do, of course?
Sure.
Adam Gardner 00:34:31 I'm trying to find it now. Where did you share that with me?
The issue?
Andrej 00:34:34 template.
Nope, I shared it with…
Adam Gardner 00:34:41 It says here, yeah.
Andrej 00:34:42 Yeah, yeah.
Adam Gardner 00:34:44 Found it.
Andrej 00:34:45 Yeah, sorry, sorry, sorry. So, this is one… this is the issue. I'll be happy… if you want to work on it, I'll be happy to assign you to it.
but… you would have to first comment on the issue, saying something like, hey, I would like to work on this, maybe to assign it. But think about it, like, read through it, just make sure that it actually is what you want to do. If you think about it a bit differently.
you can always create your own separate issue, or, like, propose your own separate issue, and… and start working on that there. Again, just for the visibility, so… So… other people know what you folks are up to. Yoshi, for you, what I would recommend to do is to take that blueprints.
Not blueprints, oh my god. Oh, tell me, issue template?
Create an issue, and just clean it up to remove any… Like… live streaming, part. Like, remove the livestream, make sure it's clear that it's gonna be just a blog post.
Yoshi Yamaguchi 00:35:51 Yeah, so we removed anything that are related to the video shooting.
Andrej 00:35:55 Yes, yes.
Yoshi Yamaguchi 00:35:56 From the site, yeah, okay, makes sense.
Andrej 00:35:59 Cool, cool, wonderful. So, regarding blueprints, we talked… When you think about surveys.
So, Marilia, who is our SIG liaison, so not sure if you are familiar with this, I wasn't for a long time.
So, the governance in OpenTelemetry works in a way that there is a governance committee and technical committee, and then there are SIGs.
That work on different things.
And to make sure that these SIGs have support from the governance folks, each SIG has their own liaison, I hope I'm pronouncing it correctly. Basically, like, a contact person in the GC, governance committee, who is in touch with everyone and discusses the admin stuff, and not only admin stuff. So for us, it's Mariglia.
Really, That is… I hope this is the… no, this is totally not the correct pronunciation.
I'll, I'll share here.
And why I'm mentioning her?
Mariglia, talked to a lot of maintainers all around hotel, and came up with a survey that she would like to Oh, boy.
that you'd like to run. I will work with her on the survey, but if you folks would be… but you mentioned that you might be interested in, like, being around when some projects are done, just so you see how it works. Feel like you can always join.
Join and contribute to this stuff as well.
But it's totally up to you. Also, I would not… necessarily recommend working on, like, too many things at the same time, just so you have your focus. So, yeah, just FYI, and think about it.
Yoshi Yamaguchi 00:38:14 So is the… is this survey… is this survey, like… similar to the one we had for Japanese community, or is this a completely new survey for a broader audience?
Andrej 00:38:27 It's a new survey?
I think Marilla talked to quite a few different maintainers of different SIGs, and because of that, there are a lot of different topics covered there.
There are some broader topics, there are some… like, in general about OTEL, there are some topics relevant to only JavaScript, there are some topics relevant to only Collector, there is some stuff relevant to only communications. So, one of my goals here is to work with Marillia to make sure that… Yeah.
The survey makes as much… It's, like, as efficient as possible, in the sense that In my experience.
Like, more focused surveys that are shorter work better.
Because people just tend to, like, actually finish them. Like, the longer the survey is, the more likely it is that people will drop out. So I will try to work with her on, like, figuring out if we can make them shorter, if we can make them a bit more focused. But let's see how this goes.
Yoshi Yamaguchi 00:39:31 Nice.
Andrej 00:39:33 Yeah, don't.
Yoshi Yamaguchi 00:39:34 The reason why I ask this is because I can, I can, you know, I can contribute to the Japanese survey if you want to, like, if we want to keep the, that survey For… for coming years.
Andrej 00:39:46 Yes. Yeah, yeah. Yes, yes, yes. I would love to. I would love to keep that survey. I think I created a… An issue for it.
In our issue board.
And actually… So let me, let me take you there.
No, I cannot take you. So I will… I will share the link to that survey with you. Again, please feel free to just comment there or subscribe, so you know what is… What is going on?
we ran the Japanese survey We ran the Japanese survey in the winter last year.
And, I think it's good to maintain, like, the same periodicity, just so we don't have it, done, like, too often. So I would recommend to run it again in the winter. This doesn't mean that you cannot start, like, preparing already now. Also, we have one contributor Dhruv, who is joining the… The stand… the usual meeting.
I think showed interest. He's based in India, I think, so it's… Yep.
so you might want to collaborate with him, because he's very, very active, and he's got a lot of ideas. So… So, I can mention it to him.
You don't have access, so let me… let me share… or let me try to share, let's see if it can work.
Yoshi Yamaguchi 00:41:45 Hmm.
Andrej 00:41:46 Okay… Yoshi, can I use your, your work… your Grafana email, or do you prefer some…
Yoshi Yamaguchi 00:41:52 Either is fine, either is fine.
Andrej 00:41:57 Okay… Okay, so I sent you an invite, you should be able to access it now.
Yoshi Yamaguchi 00:42:25 Thank you.
Andrej 00:42:27 That's funny. So the… the Open Telemetry Community Custom Interview Guide is in… New Relics Google Drive.
Yoshi Yamaguchi 00:42:37 So…
Andrej 00:42:38 It feels so strange that I am giving you access to New Relic's Google Drive stuff.
Yoshi Yamaguchi 00:42:44 And I know, I know that…
Andrej 00:42:46 I mean, this is.
Yoshi Yamaguchi 00:42:46 the all-video series, like, live streaming series, like, such as AutoMe and Author in Practice, live streams through the, the Dynatrace… Dinotrace's account of… Some, like, live streaming platform.
Andrej 00:43:06 Yes, that's…
Yoshi Yamaguchi 00:43:07 Yeah, Henrik's, like, Henrik's… no, no, not Dynatre's one. Henrik's… Personal accounts.
Andrej 00:43:14 Yeah, yeah, yeah.
Yoshi Yamaguchi 00:43:15 Yeah.
Andrej 00:43:20 Alrighty, so we covered a lot of stuff. Folks, did you have a chance to take a look at the resources that I sent you, and do you have any questions about those?
Adam Gardner 00:43:32 Didn't have a chance, if I'm quite honest. Yet.
Yoshi Yamaguchi 00:43:37 I, I… to be honest, I… I realized this link.
For the first time, though I have translated all documentation out into, you know, under docs and in blogs. So, I need to go through it.
Andrej 00:43:54 Okay, okay, fine. I was just… the only reason I'm asking is just if… if you have any questions, if… if… yeah, anything. If not, totally fine.
Feel free to get back to it whenever you want. As I mentioned.
Just real quick, the end user resources… I think… Is our, like, main… page when end-user SIG is contributing to the website.
We are trying to make it, like, end-user focused, so people know how to… how to get involved, and… If they don't want to just contribute, yeah, sorry, give me a moment, I have to go open the door.
Yoshi Yamaguchi 00:45:06 Adam, do you have any chance to visit Kubukun Japan?
Adam Gardner 00:45:12 Oh, I'd love to. No, I don't think so.
Yoshi Yamaguchi 00:45:15 Oh, oh no.
Adam Gardner 00:45:17 Not this year, unfortunately.
I'd love to get back to Japan, so, let's try and find a, a talk or a session that we could do, and then I'll be there.
Yoshi Yamaguchi 00:45:29 Straight away. Yeah, definitely. Yeah.
Sounds good.
Andrej 00:45:38 Okay, I'm back.
So, yeah, I was talking about that end user… And these resources, page.
Yoshi Yamaguchi 00:45:47 Yes.
Andrej 00:45:48 Then YouTube, there are all the playlists, the things that I mentioned earlier today, so… yeah, just take a look. I think it's a good idea to, like, watch one.
Of each, just to… to… understand how it looks. Then the blog post, there's a lot of stuff there, so… so you'll see. Repo, we use the repository to… to document stuff, mostly… the surveys.
I think this is the most active.
Peace, currently.
But… Folks used to use it also for interviews.
I think it's been a while since they updated it, but… In general, like, it should be, like, one place where we… where we have all our stuff referenced in some way, and if we have some… like, for example, about survey data, we are publishing survey data here. We have… we had discussion about this with Yoshi a while ago.
So… That's… that's how we use the repository, and then we have the projects. So Blueprints have their own project, and NGC has their own project. As I said, it's a little bit messy, but again, it might be a good idea to take a look, just so you folks see the type of work that people are doing.
How… how they are organizing it, and yeah.
how they're thinking about it. So, yeah, just take a look when you have time, but as I said, it's not…
Yoshi Yamaguchi 00:47:29 Yeah, I'll be good.
Adam Gardner 00:47:30 One thing I've just noticed on the main website, the end user, there's a section, hotel in practice, and I'm wondering if that's slightly out of date and we need the other one. So, is that… section, that page, supposed to be per YouTube playlist? And if it is, then we need one for Oh Tell Me, for example.
Andrej 00:47:55 Oh, so on the end user resources page, I can see, actually.
Where is it? Yeah, there's… Let me share my screen.
Just so I understand, what exactly are you referring to?
So, here we have… Join a podcast?
And there is hotel me and hotel in practice.
Adam Gardner 00:48:20 Oh, okay, just in the left-hand menu, hotelme is missing from the left-hand, like, the end user.
Andrej 00:48:28 I see, I see, I see, I see.
There's this, too. So this even has, like, its own subpage.
Yeah, I mean, I was rewriting this page, like, a half year ago, or a year ago.
If you folks… like, this is a great catch, if you will be reading through it, like, feel… please, please document all… all… all your…
Adam Gardner 00:48:52 Okay. -Oh.
Andrej 00:48:54 observations, and we can update that, yes, absolutely, there should be… there should be hotel in practice.
Or, or, or… Yeah.
Adam Gardner 00:49:03 Don't tell me.
Andrej 00:49:04 The hotel, me mentioned there. Perhaps we can mention also the, the other, the other, formats that, that I mentioned to you as well.
Of course.
Adam Gardner 00:49:14 Yep.
Andrej 00:49:15 Yeah, that's a good one.
And, I guess that's gonna be it for today. We are already at time. I have one thing that I would just, like, briefly like to discuss with Yoshi.
But… Because that's related to the Japanese survey that we did a while ago.
But, yeah, up to Dan, up to you, Adam, if you wanna… if you wanna stay here, or if you want to… if you want to drop.
Adam Gardner 00:49:47 Oh, it's okay, I'll hang around. I'm not in a mad rush unless it's, business proprietary stuff. I'm happy to hang around.
Andrej 00:49:54 No, no, no, it's actually… it's actually very non-business proprietary.
So… back when we were doing… when we did the first Japanese survey, in winter this year, is that in… relates to what I mentioned about the repository, that we try to post data from our survey.
Yoshi Yamaguchi 00:50:18 Oh yeah, oh yeah, so the, the, the… I think I remember that I left a comment about the content.
data column.
Andrej 00:50:27 Yes, exactly.
Yoshi Yamaguchi 00:50:28 Yeah, yeah.
Andrej 00:50:28 This was a very, very good comment, and I appreciate that you shared it.
Oh, just… I have to fir- like, I'll try to share my screen.
Once I find the right one… Yeah, here it is.
So, we had the discussion in a pull request. It's been a total mess.
For two reasons.
Or for one reason, actually. I opened it… like, way too long to… yeah, 4 months ago, or February, yeah, so a long time ago. It was… I was… I tried to just merge the data there, and Yoshi had Had a comment about whether we get a constant there, because without consent, we should not be sharing the data.
And, as I said, I think it's a good one. We did not have, like, any super special content before.
But… there is nuance there that you have to have a constant if the data is not anonymous. If you are sharing data anonymously, and the person cannot be identified, it is okay. So.
What I was proposing here is to… Is if we can come up… so, first of all, we definitely should have a consent.
And, I created an issue, and, I came up with a constant, so in the new survey that we are running now, we already use this, this content there, so this should be covered. But for the data about Japanese survey… yeah, so I didn't show this one… Okay, I don't know how to show it in Zoom. So anyway… Jeez, did I just close the issue? Can you see my screen? No, you cannot.
Yoshi Yamaguchi 00:52:23 I think you can.
Andrej 00:52:27 You can see my screen.
Yoshi Yamaguchi 00:52:30 No, no, you can share your screen.
Andrej 00:52:33 Yeah… Yeah, so here is an issue link to that consent. Yeah. But my proposal was Do you think we can… somehow… Do any, like, magic with the data.
to… lower the risk that it… that somebody could be identified. For example.
In past, we did a survey about contributory experience.
Where it's pretty, like, you know, it's just contributors to retail, so it's basically a couple of hundreds of people.
based on where do they contribute, it can be very easy to identify who is the person actually responding. So what folks did is that they separated the… the data about where do people contribute to with the feedback they provided. And this way, we could not… we could not… like, nobody could… could connect these two things together.
this… Yeah, so basically these two are, like, two separate CSVs. Both are in randomized order.
So… again, there's no way how you connect it. Would it be possible to do it for the Japanese survey, Yoshi? That we would, for example, have demographic questions separate, open-ended questions separate, and the rest of the questions separate? So, We would know where, for example, where people are based.
But we would not be able to connect it with the preference around, their… Like, yeah, what kind of events do they prefer, and also the open-ended questions.
Yeah, would it be okay for you?
Yoshi Yamaguchi 00:54:10 Yeah, that sounds… that sounds great.
So, because… so you… you mean that you… Break down all… Answers from the each… Each responders, and then anonymize them.
To… to the… to… to… to… Anonymize them by splitting the… the record.
Andrej 00:54:36 So…
Yoshi Yamaguchi 00:54:38 No.
Andrej 00:54:38 I'm not sure about the first part that you mentioned, but basically, I was thinking that we have this big table, a big CSV with everything, and I would take the first, like, the demographic questions, like, where are you based.
Yoshi Yamaguchi 00:54:50 Yeah.
Andrej 00:54:50 how big is the company where you work on, and this kind of stuff. We would separate it into.
Yoshi Yamaguchi 00:54:56 Yeah, yeah, yeah.
Andrej 00:54:57 So you can split the question.
Yoshi Yamaguchi 00:54:59 Yeah.
Andrej 00:55:00 Yeah, yeah. So there will be 3 CSVs, there will be all the… all the records will be Or, like, So the number of records will be the same.
But they will be basically just split into three.
Yoshi Yamaguchi 00:55:14 And also, you can change the order.
Andrej 00:55:15 It will be randomized. Exactly. It will be randomized, so it's not possible to connect together.
Yoshi Yamaguchi 00:55:20 Yeah, that should be… yeah, that should work, I think.
Andrej 00:55:24 Okay, okay. Yeah, so to me, this way, it's no longer… identifiable, and therefore the… The constant part would not… apply.
But I wanted to… Go ahead.
Adam Gardner 00:55:39 do you not lose something if you do that? Because you can't then say.
You can't group by, for example, company size and say, big companies need this, small companies… are you talking about… splitting one response so that, for example, if I filled it out, bits of my survey would be jumbled up with everyone else, or could you… it's just so that you can't put my whole response back together and sort of infer that I'm Adam from… Dynatrace, and, and, and then… Is that… is that the idea?
Andrej 00:56:19 Yes, the second one, that I would just split it into 3 pieces, and they would all live in a separate one, but this is a very good comment about the size of the company.
that we… do not… then, well, like, we lose some, some, some information, for sure. And,
Adam Gardner 00:56:39 For example.
Andrej 00:56:39 to us.
Adam Gardner 00:56:40 Yeah.
Andrej 00:56:40 Yeah, yeah.
Adam Gardner 00:56:42 No, just, I mean, the size of the company was just one, but, like, what industry… they work in versus their needs for hotel, because I imagine someone working in, you know.
manufacturing would be maybe using hotel in OT, not IT.
And so their needs might go towards more privacy, or network, type… You know, physical monitoring.
do… do we lose… I'm just thinking about the output of the report. Do we… do we… are we making it too difficult to actually draw conclusions from the survey in aggregate if we split it too much?
Andrej 00:57:23 I think there is a fine line, absolutely, about… Like, that at some point we start losing the important context.
For example, and we can figure out how to do it correctly, or how to do it best, that we, on one hand, make the data not identifiable, on the other hand, we… We, maintain as much contacts as possible.
And that's… more for… for… for a discussion, I think. So, regarding the size of the company, we… what we cannot do… like, the first thing that came to my mind is that, yeah, maybe we could include size of the company with both the demographic question part.
And also with the, like, actual substance questions, where we ask about how, like, the setup and stuff.
But that probably would not be a good idea, because we can end up in a situation when there are just two people from a certain size of the company.
and then it would be quite easy to connect them, and then it would be identifiable. So we would have to Take the company size and move it to the… to the second… Group?
But that's doable, that's doable, that's doable. But that's perhaps for… So, to me, it seems that if we say that people are from 10,000 plus size company.
it not… it should not be identifiable, like… like, saying that somebody in a 10,000 plus size company in Japan has this kind of setup, I don't think we should… we could be able to identify, but this is maybe something I would… I would ask Yoshi for his input, because I don't know how… how… yeah, how it works in Japan, like, how easy it is. Like, I know that… the industry is, like, very specific there, that there are, like, a couple of giant companies, and maybe not that many small ones. I really don't know. Do you… like.
I know we actually don't have to… don't have to solve it now. Let me come up with a proposal of how to split it. I would tag you both, folks.
there, and I would, like to get… get your input, and just… Wanna make sure that we do it in, like, the… The best way we can. So, very, very curious to hear what you think.
Is it okay?
Adam Gardner 00:59:52 Yep.
Andrej 00:59:53 Wonderful. And I will have to create a new PR, because I forgot that there's a quite specific way how we create PRs in OpenTelemetry.
I… you might be familiar with it, but just to mention briefly, you have to fork your… you have to fork the repository.
Make changes to your fork, and then propagate the changes to… to the original repository. You cannot be… Making changes directly to the repo, even though… even if you would be just creating a new branch.
You cannot do it for the, for the main repo. You have to go through your own fork.
So, and I didn't do it correctly back then, so I'll have to create a new fork… not a new fork, a new PR, so we'll not continue discussion there in the original PR.
Suggested FYI.
Okay, okay, so that was the only thing. So, Yoshi, you mentioned you would be okay with this one. Adam, you mentioned this great point about, like, the context.
I will do my best to come up with some, like, a proposal that is a compromise. And, yeah, thank you both very much for joining.
And in order to suppress…
Adam Gardner 01:01:11 Glad to be here.
Andrej 01:01:12 Okay?
I'll see you in two weeks, then.
Yoshi Yamaguchi 01:01:15 Excuse me.
Adam Gardner 01:01:16 See you then.
Andrej 01:01:17 See ya, bye-bye.
Yoshi Yamaguchi 01:01:18 Yeah, bye.
