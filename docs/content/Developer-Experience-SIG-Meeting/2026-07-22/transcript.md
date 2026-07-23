SIG: Developer Experience SIG Meeting
Date: 2026-07-22
Duration: 26 minutes
============================================================

## Zoom Recording Transcript

**Johanna Öjeling** 00:14 Hey, Elena!
**Juliano Costa | Datadog** 00:20 Hello, hello.
Good morning!
**Johanna Öjeling** 00:23 Morning! How are you doing?
**Juliano Costa | Datadog** 00:26 Happy, you know?
**Johanna Öjeling** 00:29 Sorry!
Like, surprised, or pleasantly surprised when I woke up this morning.
**Juliano Costa | Datadog** 00:37 Yeah, I… I… I… I wasn't following that, actually, so… I woke up, and it was there, and I was like, okay, yeah, thank you.
And…
**Johanna Öjeling** 00:53 And then I was like, oh yeah, what was it that we, like, submitted? I had to go back and read the description.
**Juliano Costa | Datadog** 01:03 Yeah, I think… I think the talk can be, like, a nice, Like, we can share a little bit about what we have done, and maybe a little bit of… hello!
**Johanna Öjeling** 01:18 Hello.
**Juliano Costa | Datadog** 01:19 a little bit of our discussion on what is the future of the SIG and that stuff, so… yeah. Yeah.
**Johanna Öjeling** 01:26 I think that's a good idea.
**Juliano Costa | Datadog** 01:28 Yeah, we need to make it, interesting, some… in some way, like, add some storytelling, and,
**Johanna Öjeling** 01:35 Yeah.
**Juliano Costa | Datadog** 01:37 Because I think it would be… Mainly slides, right?
**Johanna Öjeling** 01:42 Mmm, exactly, it won't be, like, a live demo or anything, yeah.
So, Perk, for your context, Juliano and I got a talk accepted to the.
**Juliano Costa | Datadog** 01:54 I said.
**Johanna Öjeling** 01:54 Oh, yeah!
**Juliano Costa | Datadog** 01:56 I think he left.
No, I…
**Johanna Öjeling** 01:59 Oh, I left! Oh, okay, yeah, I didn't notice, yeah.
**Juliano Costa | Datadog** 02:03 I call and just left him.
**Johanna Öjeling** 02:06 Yeah, but anyway, I'm really excited to do the talk together, it will be so much fun.
**Juliano Costa | Datadog** 02:14 Likewise, yeah. Cool.
Cool, cool. When is that?
**Johanna Öjeling** 02:22 It's the 5th of October, I think.
**Juliano Costa | Datadog** 02:27 Okay, yeah, maybe we… we… we may need.
**Johanna Öjeling** 02:33 Yes, sorry.
**Juliano Costa | Datadog** 02:34 Working a little bit earlier.
Because, just so you know, in September, I'm in Brazil.
**Johanna Öjeling** 02:44 Hmm,
**Juliano Costa | Datadog** 02:45 So, I'll be… I mean, the time zones are not that different, so I… I mean, it is 4 or 5 hours. We can still get a… One-hour block, or whatever, during the day.
**Johanna Öjeling** 02:59 -
**Juliano Costa | Datadog** 03:00 But if we could… have… If we could have at least a draft or, like, an outline and stuff, we… That would make my life easier, because…
**Johanna Öjeling** 03:15 Yeah.
**Juliano Costa | Datadog** 03:16 In Brazil, I all have one Datadog event, and then the KCD Sao Paulo, so…
**Johanna Öjeling** 03:22 Okay.
**Juliano Costa | Datadog** 03:24 I'll be in events. Well, it is two days, but I'll be there for two and a half weeks.
**Johanna Öjeling** 03:32 Okay, yep.
Yeah, absolutely, we can, I mean, it's just nice to… Get it done early, or at least we can get started and then, kind of split it up, or yeah, and then work async.
**Juliano Costa | Datadog** 03:47 Okay.
**Johanna Öjeling** 03:48 together. And I think there is… Let's see… okay, the deadline for the presentation slides is the 30th of September, so yeah, just, like, a week before the actual event, but yeah, it's just nice if we… Dear darling.
Did you, get a new reply from the submission to the Cloud Native Denmark conference?
**Juliano Costa | Datadog** 04:19 No, not yet.
**Johanna Öjeling** 04:22 Yeah.
**Juliano Costa | Datadog** 04:22 No idea. Oh, actually paying Casper, let me give insight.
**Perk (Marcin Stożek) | Elastic Ingest** 05:17 Apologies, folks, I hit the little… Emergency at my home. Technical technician came.
And so I may be, like, on and off.
**Juliano Costa | Datadog** 05:29 Okay, hope it's all okay.
**Perk (Marcin Stożek) | Elastic Ingest** 05:31 No, no, no, it's okay.
**Juliano Costa | Datadog** 05:32 She's not good.
**Perk (Marcin Stożek) | Elastic Ingest** 05:33 facility that broke, so, he's just fixing it, but it just, like, you know, rang the door the moment we started, so…
**Juliano Costa | Datadog** 05:42 No worries.
Johanna and I were just talking. We got a talk accepted on Observability Summit.
**Perk (Marcin Stożek) | Elastic Ingest** 05:51 Oh, nice.
**Juliano Costa | Datadog** 05:52 Gonna present together I'll talk about this SIG, so, yeah.
**Perk (Marcin Stożek) | Elastic Ingest** 05:58 Nice! Okay, cool.
Observability Summit, in…
**Juliano Costa | Datadog** 06:04 Prague.
**Perk (Marcin Stożek) | Elastic Ingest** 06:05 In Prague. Oh, okay, cool, cool, okay, very well.
**Johanna Öjeling** 06:08 Yeah. I've never been to Prague either, so…
**Juliano Costa | Datadog** 06:12 Huh.
**Johanna Öjeling** 06:13 Also, looking forward to that.
**Juliano Costa | Datadog** 06:14 I've been to Prague a couple of times, it's a lovely city, yeah. You should take a couple of days to spend there.
**Perk (Marcin Stożek) | Elastic Ingest** 06:22 Yeah, that's okay.
**Johanna Öjeling** 06:23 What, day of the week is it? Oh, it's a Monday!
**Juliano Costa | Datadog** 06:29 Perfect.
**Johanna Öjeling** 06:32 Nice!
**Juliano Costa | Datadog** 06:50 Okay, regarding the things that, that we had to do and discussed last week, I… Honestly, didn't have time to take a look into that.
I still need to… by… hopefully by this Friday, I'm releasing… we are releasing the demo 3.0, so I'm still working on the… On the Helm chart update now?
testing and seeing if everything is working. We are… I think… almost a half year without releasing, or I would say close to a year. We have… a lot of changes that changed, a lot of things that changed, and the update is massive. So we are planning a blog post, like, the release itself, and then the help charts, so it's, like, My life is a mess at the moment.
I know the Montana.
**Perk (Marcin Stożek) | Elastic Ingest** 07:50 mentioned.
**Juliano Costa | Datadog** 07:51 All the maintainers are gone, so… Perk (Marcin Stożek) | Elastic Ingest 07:55 Oh, definitely, definitely.
Did you maybe have a chance at any point to maybe look at the blog post for, Key Clock?
**Juliano Costa | Datadog** 08:06 I did last week, a bit. Added a couple of suggestions, but then I saw that, Alex… Is it Alex, his name?
I think so.
**Perk (Marcin Stożek) | Elastic Ingest** 08:19 X, yeah, the, yeah, there was… Alex and Martin.
**Juliano Costa | Datadog** 08:23 Yeah, I think Alex, added a comment saying that he preferred the other way, so I would just, Perk (Marcin Stożek) | Elastic Ingest 08:31 Hmm.
**Juliano Costa | Datadog** 08:32 suggestion. Okay.
One thing that I felt while reading was that it was… Too direct.
So, this, this, this, and this.
I'm… I missed, but this is just a me feeling, maybe, from… from the… from the response. So, I suggested that, a change, and Alex said that he preferred the other way. So… what I suggested was just, like, kind of… a sentence or two connecting the two paragraphs? Because, for instance.
We mentioned that they use Quarkus, but we do not.
I mean, we mentioned ParkOS, but we do not mention that KeyClock is actually built using Parker.
**Perk (Marcin Stożek) | Elastic Ingest** 09:28 Oh, fair enough, yeah.
**Juliano Costa | Datadog** 09:29 And then, like, we do not give any, a bit of context there, but on the second… on the sex… on the sec… Jesus, on the second section, we do talk about, hey, Quarkus is that, so then they chose this approach because the agent added X overhead, but, like.
**okay, but, like, I… Perk (Marcin Stożek) | Elastic Ingest** 09:51 I missed it.
**Juliano Costa | Datadog** 09:51 a connection between the two paragraphs.
**Perk (Marcin Stożek) | Elastic Ingest** 09:54 Fair enough, fair enough, fair enough, yeah, okay, okay, okay. So, yeah, this is… this is exactly the feedback that I… that I need, because, you know, like, after some time.
You just don't see this.
**Juliano Costa | Datadog** 10:04 I'm frustrated, yeah.
**Perk (Marcin Stożek) | Elastic Ingest** 10:05 you read it multiple times, and you just don't see this. But that's perfect. I'll take a look. Thanks, thanks, yeah. Okay.
We'll get the points done.
**Johanna Öjeling** 10:15 Yeah, I also read it, I liked it, but I added some comment about maybe, To, like, break up the text and give more, like, illustrative examples, if we could have… Like, in the other blog post, we have some configuration snippets, or architecture diagrams, or quotes.
And… And this is, like, a special case for KeyCloak, since, like, it's not like the other organizations that use it for their… I can'.
Adobe, for instance, the Skyscanner, that's, like, in their internal software, but… Yeah.
Here, it's something that Keyclark also, like, enables for… Users, so they actually provide, like, official documentation that, like, if the interviewees won't… I mean, we can ask them to send some snippets, but we could also, if they don't want to, like, we could just take it from their official document.
**Perk (Marcin Stożek) | Elastic Ingest** 11:17 Yeah, fair enough, fair enough. So you're saying, like, snippets or visuals?
**Johanna Öjeling** 11:22 Yeah, I think that would be nice to, to provide.
**Perk (Marcin Stożek) | Elastic Ingest** 11:25 I struggle with this a little bit, because they're saying, like, how they adopted OpenTermet, like, what can you show with the adoption of, like, what is the image, right? So that is not easy.
**Johanna Öjeling** 11:38 No, yeah.
**Perk (Marcin Stożek) | Elastic Ingest** 11:39 But that's a valid feedback, yes.
**Juliano Costa | Datadog** 11:41 what we could try, I don't know how easy it is, I never used KeyClock, but we could maybe have a Hello World with Key Clock, something, and then share a screenshot of Jaeger.
It traces that, now.
**Perk (Marcin Stożek) | Elastic Ingest** 11:59 From a key clock, that's there.
**Juliano Costa | Datadog** 12:01 Exactly.
**Perk (Marcin Stożek) | Elastic Ingest** 12:03 Oh, that's a good idea.
**Johanna Öjeling** 12:04 Yeah, okay. Yeah, I like that.
**Perk (Marcin Stożek) | Elastic Ingest** 12:06 Maybe, maybe, maybe let's, hmm.
I'll ask Alex and Martin to provide that.
**Juliano Costa | Datadog** 12:14 Yeah, maybe they have it, yeah.
**Perk (Marcin Stożek) | Elastic Ingest** 12:15 Maybe they have it here.
**Juliano Costa | Datadog** 12:19 And if they don't have, but let's say that they have… I don't know. Maybe they have, like, the JSON of a trace. Then we can get this JSON, add to Jaeger, and Jaeger renders it.
**Perk (Marcin Stożek) | Elastic Ingest** 12:35 Yeah,
**Juliano Costa | Datadog** 12:36 So, we could… we could do that.
**Perk (Marcin Stożek) | Elastic Ingest** 12:41 Yeah.
Traces… Yeah, okay.
**Juliano Costa | Datadog** 12:51 But cool. Yeah, I… we discussed last week that, this block is easier to get.
merged because Alex and Martin are CNCF folks, and they, like, they're acting.
**Perk (Marcin Stożek) | Elastic Ingest** 13:05 Your response.
**Juliano Costa | Datadog** 13:05 Yeah, yeah, exactly.
**Perk (Marcin Stożek) | Elastic Ingest** 13:07 They fancy.
**Juliano Costa | Datadog** 13:07 So, the idea was to give you feedback as soon as possible, but yeah, Perk (Marcin Stożek) | Elastic Ingest 13:13 Very well, very well, yeah, yeah, yeah.
For… yeah, okay, okay, okay. It's, you know, like, every time is a hard time, so yeah, I'll.
**Juliano Costa | Datadog** 13:21 We'll take a look.
**Perk (Marcin Stożek) | Elastic Ingest** 13:21 I'll take a look. Actually, I have a… I have a PTO that is one week of staycation, which I actually, like, usually do. I very much, like, you know, stay at home and, like, finish stuff that I can hang around. This is one of those, so, I hope I'll find some time.
For this, you know, early, early August.
Thanks. Yeah, good feedback. Okay, okay, okay.
I'll come… yeah, I'll come next week with some updates.
**Juliano Costa | Datadog** 13:51 Oh, when is the PSRA staycation?
**Perk (Marcin Stożek) | Elastic Ingest** 13:54 Nor occur.
**Juliano Costa | Datadog** 13:55 friendly.
**Perk (Marcin Stożek) | Elastic Ingest** 13:55 August, first two weeks of August. Well, first.
**Juliano Costa | Datadog** 13:58 No.
**Perk (Marcin Stożek) | Elastic Ingest** 13:59 Let's get straight to it.
**Juliano Costa | Datadog** 14:00 Let's try to get this done by, like, latest next week, because then.
**Perk (Marcin Stożek) | Elastic Ingest** 14:05 Oh, you think? I assume. Okay, yeah, okay, fair enough.
**Juliano Costa | Datadog** 14:08 Because, I mean, Perk (Marcin Stożek) | Elastic Ingest 14:11 what we Do you cook.
**Juliano Costa | Datadog** 14:12 You could… you could, no, go ahead, sorry.
**Perk (Marcin Stożek) | Elastic Ingest** 14:16 No, I just wanted to say that previously we discussed that, hey, there's no rush, because, like, there's no…
**Juliano Costa | Datadog** 14:21 Oh, yeah, yeah, yeah.
**Perk (Marcin Stożek) | Elastic Ingest** 14:22 But if you say that this could go sooner rather than later, then that's okay with me. I just need to sit and do it then.
**Juliano Costa | Datadog** 14:31 I, I don't, I don't want to rush you. I just said, because I think, from what I felt, it's more on our end to review and, Perk (Marcin Stożek) | Elastic Ingest 14:44 Yeah, promotion.
**Juliano Costa | Datadog** 14:45 improve the flow, yeah, yeah, rather than on you to actually sit and write. But, I, I don't want to rush, so… Perk (Marcin Stożek) | Elastic Ingest 14:54 Oh, it's okay.
**Juliano Costa | Datadog** 14:54 to, to publish later, we published later, there's no… Sure.
One thing that I saw yesterday, so I opened up PR to raise a… I will do that right away, actually.
I opened up PR to create the… Auto demo blog post.
**Perk (Marcin Stożek) | Elastic Ingest** 15:17 Oh, great.
**Juliano Costa | Datadog** 15:18 And the folks from the docs asked me to create an issue.
So they have a new issue, blog post request. So I'm, I'm opening, I'm opening one with the, the description, and then I'll, I'll tag, I'll tag you, Perk, there.
**Perk (Marcin Stożek) | Elastic Ingest** 15:40 Very well, yeah, I'll create another one for Kiklok.
**Juliano Costa | Datadog** 15:43 Yeah, no, I mean, so, like.
**the PR… so… I don't know why they have done that, but, like, the PR now for the blog post needs to have an issue that they are tracking separately. So I think they… they schedule, and they, plan… I think that's… Perk (Marcin Stożek) | Elastic Ingest** 16:02 I think that's okay. It's, like, with cholesterol, you usually have the PR and the issue. I think that's fine.
**Juliano Costa | Datadog** 16:07 Yep.
So I'm… I'm gonna add there, and I need to add, like, sponsors.
**So I'll add Johanna and myself, and then, like, you… Perk (Marcin Stożek) | Elastic Ingest** 16:22 Reviewers, I'm happy to.
**Juliano Costa | Datadog** 16:24 Yeah, yeah.
**Perk (Marcin Stożek) | Elastic Ingest** 16:25 Very well, very well. Will do.
**Juliano Costa | Datadog** 16:27 Cool.
Cool, cool.
**Perk (Marcin Stożek) | Elastic Ingest** 16:33 Is Coco, like, the, the police squad? This… 99-something, like, cool, cool, cool, cool, cool, cool, cool, cool, cool.
**Juliano Costa | Datadog** 16:41 I, I, I… Perk (Marcin Stożek) | Elastic Ingest 16:43 You recall? Or you don't know? You don't know that one? Okay.
It's just that it sounded exactly like the, like the guy from the TV series.
When is the Observability Summit, by the way? Is it, like, December?
**Johanna Öjeling** 17:11 No, it's in October already, the 5th of… Perk (Marcin Stożek) | Elastic Ingest 17:14 Oh, sorry, October.
**Johanna Öjeling** 17:15 Sure.
**Perk (Marcin Stożek) | Elastic Ingest** 17:16 I'm a doctor, okay.
It's incredible.
**Johanna Öjeling** 17:19 Right.
**Perk (Marcin Stożek) | Elastic Ingest** 17:19 super close, close to me. Like, I've sent one, but, unfortunately didn't get in. But I think I may show up.
Huh?
**Johanna Öjeling** 17:27 Yay! Yeah!
Do you have any upcoming conferences?
**Perk (Marcin Stożek) | Elastic Ingest** 17:35 I'm going to OSMC, I know that already.
It's in Nuremberg, in, I think that's November.
Yeah, like, I've sent a couple of places. The KCD that you've mentioned, Juliano, the Copenhagen… So I just don't know yet, because they didn't respond just yet. I know that I didn't get into the observability Summit myself, because I've sent us some proposal, but it's fine, you just gotta send it out everywhere, and then some places just, you know, accept, and some have other agenda.
That's fine.
**Juliano Costa | Datadog** 18:08 So, I heard back from Casper, and the plan is to finalize the schedule by mid-August.
**Perk (Marcin Stożek) | Elastic Ingest** 18:17 For what? For which one?
**Juliano Costa | Datadog** 18:19 for the Denmark one.
**Perk (Marcin Stożek) | Elastic Ingest** 18:21 Oh, nice!
**Johanna Öjeling** 18:21 Okay,
**Juliano Costa | Datadog** 18:23 So, we have a month to hear from them.
**I got waitlisted in Poland, Perk (Marcin Stożek) | Elastic Ingest** 18:30 Oh, for Cloud Native, yeah, I didn't get that one as well, but I'm going to be there anyway.
**Juliano Costa | Datadog** 18:34 For sure. I won't be there if I don't get accepted. I'll have to go to the U.S. for a team event, so I'm really hoping to get accepted.
Please accept me.
**Perk (Marcin Stożek) | Elastic Ingest** 18:48 Fair enough.
Yes.
**Juliano Costa | Datadog** 18:51 I mean, I like my team and everything, but, like, yeah, it's New York.
**Perk (Marcin Stożek) | Elastic Ingest** 18:57 It's far away, isn't it?
**Juliano Costa | Datadog** 18:59 Yeah.
Cool. Okay, I'm gonna open the issue and let you both know. I'll tag you on GitHub.
**And… yeah, let's, Perk (Marcin Stożek) | Elastic Ingest** 19:14 And for me, I'll review your comments. Thank you for taking those, and be back with you next week. Also, I reached out to Alex.
And marketing for that.
That'll be good progress.
I think…
**Johanna Öjeling** 19:27 Oh, I also have… no, sorry.
**Juliano Costa | Datadog** 19:30 No, go ahead, go ahead.
**Johanna Öjeling** 19:31 Yeah, this is, like, different, but related. I have an update on the Grok blog post, or yeah, not really an update, but I reached out again, and Andreas, he also tried to, yeah, give advice from NVIDIA's, you know, legal department on how to proceed, since he's not in touch with anyone from Grok either, and They don't respond to my emails, so… let's see how it goes. So, yeah, not really an update.
**Juliano Costa | Datadog** 20:02 Cool.
But, was Grok… I think Drok was acquired by NVIDIA, right? Is that…
**Johanna Öjeling** 20:08 It's, like, not fully acquired, but it's kind of partly acquired, or some kind of, strategic partnership, or, yeah, kind of… Oh, okay, okay. Yeah, so,
**Juliano Costa | Datadog** 20:21 Tricky. Okay.
**Johanna Öjeling** 20:23 Yeah, so there are still, like, there is still a Grok entity, but yeah, Andreas moved over, so yeah.
**Perk (Marcin Stożek) | Elastic Ingest** 20:33 So the strategy is… it's complicated, they're saying.
**Johanna Öjeling** 20:35 Yeah, yeah, and he wants, since the blog post is about his work at Grok, then he wants also to get sign-off.
one at Croc before we publish it.
**Perk (Marcin Stożek) | Elastic Ingest** 20:45 Of course.
Of course.
Okie dokie.
**Juliano Costa | Datadog** 20:51 Cool.
Awesome.
**Perk (Marcin Stożek) | Elastic Ingest** 20:53 Very well.
**Juliano Costa | Datadog** 20:55 See you all!
**Perk (Marcin Stożek) | Elastic Ingest** 20:57 Next week.
**Juliano Costa | Datadog** 20:58 On the internet, yeah. Exactly.
**Perk (Marcin Stożek) | Elastic Ingest** 21:00 Cheers! Thank you, folks, have a great day.
**Juliano Costa | Datadog** 21:03 Sierra.
