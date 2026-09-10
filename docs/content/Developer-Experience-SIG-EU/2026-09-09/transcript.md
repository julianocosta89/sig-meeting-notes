SIG: Developer Experience SIG (EU)
Date: 2026-09-09
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Juliano Costa | Datadog** 01:05 Hello, hello.
I can't hear you. Now I can't. Okay.
**Johanna Öjeling** 01:12 It's… it's…
**Juliano Costa | Datadog** 01:15 Hi.
**Johanna Öjeling** 01:19 Richmond.
**Juliano Costa | Datadog** 01:21 Well, good, actually, yeah. Things are… getting close to the actual event, so, yeah. Like, what needs to be done, either is done, or… yeah, we can't do anything anymore.
**Johanna Öjeling** 01:37 They are. And, oh, you… you went to Linds during the weekend.
Oh, no, sorry, to grat.
**Juliano Costa | Datadog** 01:45 Yeah, yeah, yeah. Yeah, I presented that. Yeah, that was, Yeah, that was weird. The AV system didn't work with Mac, so… I wanted to run the demo to showcase, but yeah, I had to present from the… from the host.
Laptop, so… I just presented these slides, and then I switched back to my laptop and said, hey, whoever wants to see the demo running, come here and I'll share from my laptop.
**Johanna Öjeling** 02:17 Okay.
**Juliano Costa | Datadog** 02:18 Yeah, but it was a good event, yeah. Nice crowd, good questions, so, yeah.
**Johanna Öjeling** 02:25 It's good to hear. And now, the next event is the Datadog, yeah, event, right?
**Juliano Costa | Datadog** 02:32 Yeah, Datadog Summit, Sao Paulo, next week, on Tuesday.
So, I'm flying to Brazil this Saturday.
**Johanna Öjeling** 02:42 Oh… Will you have the opportunity to meet some, like, family or friends?
**Juliano Costa | Datadog** 02:50 Yeah, I'm spending a week there, because between the Datadog Summit Sao Paulo and the KCD Sao Paulo, it's like, 10 days.
**Johanna Öjeling** 03:00 funds.
**Juliano Costa | Datadog** 03:00 spending a week in my city, my hometown, and then I travel back to Sao Paulo to present at the KCD, and then I fly back.
**Johanna Öjeling** 03:08 Okay.
Nice.
**Juliano Costa | Datadog** 03:10 Hey, Brick.
**Johanna Öjeling** 03:12 Your purse.
**Perk (Marcin Stożek) | Elastic Ingest** 03:12 Hey guys, how are you?
**Juliano Costa | Datadog** 03:15 Good, good, good.
**Johanna Öjeling** 03:17 Congrats.
**Perk (Marcin Stożek) | Elastic Ingest** 03:18 Eddie?
With the presentation?
**Juliano Costa | Datadog** 03:22 I was actually booking my trip to… Perk (Marcin Stożek) | Elastic Ingest 03:25 Rock?
**Juliano Costa | Datadog** 03:26 to Copenhagen now, so, because, yeah, There is the cloud-native Copenhagen, and cloud-native Denmark, actually.
**Perk (Marcin Stożek) | Elastic Ingest** 03:38 Yep.
**Juliano Costa | Datadog** 03:38 And I got accepted at, KCD Porto, which is one day before, so, yeah, I was just trying to see if I can go to Porto, and then fly to Denmark, and then… Oh, nice. Yeah, I don't know if… if that will be possible, Yeah, there is only one direct flight from Vienna to Porto, that's from Ryanair, and they do not fly, on Wednesday. The event is Thursday, so it's, like, the exact date I meet, they don't have flights, and I'm like, oh, come on!
Please!
Yeah. Anyways, cool.
But the… the Observability Summit talk, slides, I think we are ready, right, Johanna?
**Johanna Öjeling** 04:26 Yeah, I think we just have, like, one slide to make some final touches.
But, yeah, I think, yeah, we've made good progress, so it's in a good shape.
**Juliano Costa | Datadog** 04:41 We need now to do a dry run, just to see if we are good on time, but yeah, hopefully… Yeah. Hopefully, things work.
**Perk (Marcin Stożek) | Elastic Ingest** 04:53 Very well. They will, for sure, come on. It's a friendly audience, isn't it?
Usually.
**Johanna Öjeling** 04:59 True.
**Juliano Costa | Datadog** 05:00 Yup.
**Johanna Öjeling** 05:01 How, how have you been, Perk?
I'm okay.
**Perk (Marcin Stożek) | Elastic Ingest** 05:05 I'm okay. I had some thoughts about the… about the… the article, about the Key Clock article.
I'm a little bit busy lately, so that's why I didn't join, like, a week ago and two weeks ago, but I'm good now. And, I had some thoughts about this, KeyCloud blog post, so, if you don't mind, like, I can tell you. So, I thought that… I thought that, maybe we should not go with the CNCF one.
Right now, maybe the better choice would be to go with the… with the open telemetry, and then maybe we have some others, you know, other… other projects as well, and then when we have a couple of those, like, let's say 3 or 4, we can do a synthesis.
This way, we will not be… because, you know.
We are saying things that are, that are going to be maybe seen as, like a criticism, you know? Like, for example, like this, like, Java agent is not in, like, the greatest shape. I mean, you have gotta, do… stuff for your own, to get proper SDKs, you know, properly… to get SDKs properly plugged into your code, you know, and it's just not ideal.
this feels okay for me, this feels okay for the OpenTelemetry blog post, where we are all, like, people who know the stuff, and we need this information. This is, you know, this is the most important content, while for the CNCF, it feels like, it's rather about, doing a positive Like.
you know, fuss around all of the projects and whatnot, so maybe it would be better to just get a couple of those and then synthesize. So, that's what I propose, that is one thing. So on that front, we would be good to go, but I have also one other idea, maybe, and… I can do it quite quickly. I would add, I would add two, two quotes, one from Alex, one from Martin, from what they said, actually, because we had this recorded, so they said something… I would just put it as a quote, you know, somewhere there, to make the flow maybe even better.
No? And then, when I have this, I think we are ready, but I probably need to create a ticket or something else. I mean, there is a ticket, I don't know what to do next.
**Juliano Costa | Datadog** 07:19 So, for the… for the… if we go with the hotel, everything is ready to go. You just open the PR, there is already an issue, you just.
**Perk (Marcin Stożek) | Elastic Ingest** 07:28 Interesting.
**Juliano Costa | Datadog** 07:28 fix this. Oh, okay.
**Perk (Marcin Stożek) | Elastic Ingest** 07:31 Okay.
**Juliano Costa | Datadog** 07:31 Just one note on the, on the choice here, and I think it's important, so we actually decide. Okay.
when I asked the Ambassador channel, like, hey, what is the process to publish stuff on the cncf.io blog? ovitz, I don't know if you know.
**Perk (Marcin Stożek) | Elastic Ingest** 07:51 Yes, sure. Oh, yeah, yeah, yeah, of course, yeah.
**Juliano Costa | Datadog** 07:53 So he said, hey, I… it's not easy to get a blog post in. I got rejected a couple of times.
And Aldra, the community manager from CNCF, she said, hey, this is the… well, Chad shared with me the link to open the issue and everything that I.
**Perk (Marcin Stożek) | Elastic Ingest** 08:12 Yeah, yeah, I sold that one, yeah.
**Juliano Costa | Datadog** 08:14 and Aldra came and said, hey, if the post is original, coming from, people involved on the SIG, this is, like.
Most likely to be approved, but if we go hotel, and then we try to, like.
do a highlight in the CCS later, I think the chances of being approved to get in will be lower.
**Perk (Marcin Stożek) | Elastic Ingest** 08:41 Yeah, that's fair, that's fair, but I'm… this is not what I'm suggesting, because I suggest… I suggest to do not the highlight.
But I suggest to write a new piece.
That will be a synthesis, but… so, because if I understood correctly, what I read there is that the CNCF does not like to hold a series. They don't hold series. While this blog post, this particular one.
feels like it could be part of the series. We could have similar discussions with more other open source projects that are, you know, around the CNCF, so… my proposal is to have a couple of those, like, 4 or 5, you know, and then do a new piece, which is a synthesis, and then go with this one to the CNCF folks. And I think this might fly even better than what we have right now. We would not need to be as politically correct, you know? I mean, during the synthesis.
You are, because it's a synthesis, and here we can be straight to the point, and, you know, like… Show things as they are.
**Juliano Costa | Datadog** 09:41 Yeah, I do like the idea of, like, let's say that we get 5 proj… 5 different projects that are using Oltao, and then we share, like.
In this instance, have how other projects are using.
**Perk (Marcin Stożek) | Elastic Ingest** 09:56 Yeah, exactly.
**Juliano Costa | Datadog** 09:56 observability. That's great. The problem is that the content Even though this blog post is new, the content will not be new, because we already have stories of, like.
the… the source of the… the things that we're gonna say are already published somewhere else. So this may be an issue for CNCF, this may not be an issue. I… I don't know. As I said, I never posted, something on CNCF, so I just wanted to… to share the… like, raise awareness of this… Thing that can be a problem solver.
**Perk (Marcin Stożek) | Elastic Ingest** 10:33 Yeah, yeah, yeah, this might be an issue. Yeah, yeah, I agree with you. Yeah, the way I think about it, though, is that while you're… you're correct that it may be seen as something that we repost.
If we do a synthesis, then it might be… it might be new content, because we can say.
that all of the projects found this problem, and some of the projects only found another problem. So… I think we could find our way around it, really.
**Juliano Costa | Datadog** 11:02 No?
**Perk (Marcin Stożek) | Elastic Ingest** 11:02 That's all I'm saying.
**Juliano Costa | Datadog** 11:04 Yeah!
**Perk (Marcin Stożek) | Elastic Ingest** 11:04 I would try to do it anyway, you know?
**Juliano Costa | Datadog** 11:07 Yeah, and yeah, and I think it would be… It would fit nicer, because then we would have, like, multiple projects.
**Perk (Marcin Stożek) | Elastic Ingest** 11:14 Yeah, exactly, more projects, yeah, so that'll be OpenTelemetry.
and how it's used here, here, here, here, here, and there, and yeah, I think that's a much stronger message for the CNCF crowd than the… Than the key clock only, you know?
**Juliano Costa | Datadog** 11:29 Yeah, totally.
**Perk (Marcin Stożek) | Elastic Ingest** 11:30 Yeah, I agree that, like, a single… like, a simple cross pause will not work. Yeah, I'm… yeah, I'm at peace with this now. I know.
So, yeah, that's my proposal. I'll add those two quotes, I'll ping you guys, then, you know, like, very quick review, if that works, and then we can… I'll do a PR.
On the block.
**Johanna Öjeling** 11:55 That's good.
**Perk (Marcin Stożek) | Elastic Ingest** 11:56 Yeah.
**Johanna Öjeling** 11:56 Okay.
**Perk (Marcin Stożek) | Elastic Ingest** 11:57 So, that's my update.
**Juliano Costa | Datadog** 12:05 I'm just adding to the, to the notes.
**Perk (Marcin Stożek) | Elastic Ingest** 12:07 Thank you, thank you, I was thinking, yeah, yeah, I see this, yeah.
No, sorry.
**Juliano Costa | Datadog** 12:51 Yeah, no worries. Okay, I don't have anything else to discuss.
One thing that I raised to Johanna last week, Perk, was that I think we, We need to think about the future of the… of this SIG.
Like, what we gonna do if… Because… Like, this interview thing may be cross… across work that we could maybe do together with the Blueprint folks?
and let's say that they have meetings in North America time zone, we could have our blueprint EU-friendly, meeting.
continue the interview process with, under the blueprints, SIG? Or we could try to really focus on what our SIG actually calls, which is Developer Experience.
I… I personally feel that OTel has a lot to evolve in developer experience.
I feel that… we have a lot of SIGs working on their own bubble, but they do not see, like, the pace of the user and how to actually start using OTEL, and how to add OTEL to the code, and, fix with, like, SDK configuration that is, like, 100 lines of code. So, like.
**Perk (Marcin Stożek) | Elastic Ingest** 14:37 Yay.
**Juliano Costa | Datadog** 14:38 This is also… this is all, like, the developer experience flow, I think this should still be… be approved.
I don't know if we have, Capacity, yeah, to actually invest in that and propose solutions, and I don't know. So, yeah. Okay, yeah. It's not something that we need to answer now, but, just to… to think.
**Perk (Marcin Stożek) | Elastic Ingest** 15:08 Yeah, I think that's a good call. Maybe, Maybe, having this written down.
might help us, to see if we are getting there or not. Like, if we… If we had this written, what is the charter, like?
we would like to make sure that the SDKs are better. We would like to make sure that people know how to do, like, you know, like, a couple of those sentences, that we can measure ourselves against. And then I agree with you, it feels like it's useful. The question is if we have time for this.
At the same time, the blueprints themselves, Yeah, it's like a part of this, but not the whole story, is it?
**Juliano Costa | Datadog** 15:56 Yes.
No, I also agree. I don't think Blueprints actually replace the developer experience.
But the main point is capacity and, yeah.
**Perk (Marcin Stożek) | Elastic Ingest** 16:11 Is there… oh, okay, okay, okay, because I assume we could continue what we are doing, maybe we could focus on something else, or… Or maybe… we could change our focus to be focused more on the DevEx, like we do have in the name. So, that's why I propose. So, Should we put that on the, GitHub repository?
on the page… I assume that's the web page of the SIG, isn't it? This charter.
**Juliano Costa | Datadog** 16:42 What… what do you mean?
**Perk (Marcin Stożek) | Elastic Ingest** 16:44 I mean, if we have this, something like that in writing, then we could add this to the GitHub page, like, what's the goal of SIG?
So I would start with that, you know?
So now… Sorry?
**Johanna Öjeling** 16:59 issue? Do you mean we had an issue for discussing it, or… Perk (Marcin Stożek) | Elastic Ingest 17:03 No, no, no, like, in the README, in the main README, just put an information, like, what's the goal of the SIG.
like, be… And be precise with this. And maybe then we will find out that, hey, this is too small, or this is too big, or this is actually going in the wrong direction, I don't want to do this, you know?
Let's see, GitHub…
**Johanna Öjeling** 17:33 Yeah, I think we'll need to kind of figure out what should be the, the purpose of the SIG.
**Perk (Marcin Stożek) | Elastic Ingest** 17:41 Yeah, because, you know, like, right now, we do have it, right? It's… Same.
Oh.
Not this one.
Here, what does the Developer experience seek? And the goal is to improve the experience of developers using OpenTelemet within their projects.
maybe we could… maybe we could get a little bit more specific, what we want to do. That's what I'm saying, you know?
And if we do, then we'll see if we have time for this. Because right now, the way it is written right now.
It can be anything, really.
Yep. A lot of stuff. So, that's my proposal. But I'm… I'm with you. It's hard to do… Right now, you know, I need 3 people.
I have 3 people, a lot of progress. At the same time, if we have, like, a good charter, I think we could do amazing stuff.
But, okay, That's a good foot for thought, sorry.
**Juliano Costa | Datadog** 18:41 Yeah, I feel that 3 people is not bad. I have 6 with less people. The thing is that we need to decide what we're gonna do, and then say, hey, yeah, we're gonna go that direction, and then, yeah, everyone's aligned, let's go, and then we… Yeah. Point and… and run towards But I feel that we are… Kind of in a limbo, currently, because… Perk (Marcin Stożek) | Elastic Ingest 19:07 a little bit.
**Juliano Costa | Datadog** 19:08 Yeah, the interviews ended, some stories are to be published, but, not yet there, and we are without, kind of, knowing what to do and what to do next with this SIG.
**Johanna Öjeling** 19:19 Yeah, and I agree, and in the summer, we discussed Some, like, potential initiatives, and started to write some, you know, proposals, but then… None of us.
has had, like, capacity to actually drive those, so… Yeah, I think it's… it's a good question to ask ourselves, like.
yeah, we, like, do we want to pursue one of those, or something else, or should we kind of merge with the Blueprint project? And checking the Blueprint or the hotel website. It looks like they still haven't received any… Other reference implementations than the ones we have created from the blog posts.
So…
**Juliano Costa | Datadog** 20:13 Hmm.
**Johanna Öjeling** 20:13 that's also, I think, an area where we could… If we, like, decide to, kind of, merge the things, or to… continue to support that. I'll be open to that, to help.
**Perk (Marcin Stożek) | Elastic Ingest** 20:30 With the blueprint.
**Johanna Öjeling** 20:31 More… create more, yeah, reference implementations.
Because I feel, right now, I don't have capacity to… to start.
And a completely, like, new… Initiative.
**Perk (Marcin Stożek) | Elastic Ingest** 20:47 Yeah, that's fair, that's fair.
I think, yeah, I think the important part is to, like, ask ourselves what everybody wants to do, but also, Yeah, having… having, one single goal, it's, it's helpful sometimes. Just, yeah, like, let's help out with the blueprints, okay, let's help out with the blueprints, and… Lovely.
**Johanna Öjeling** 21:10 Do you have anything in mind, Perk, that you would like to.
**Perk (Marcin Stożek) | Elastic Ingest** 21:14 Well, I don't have anything else, right now. The only thing, like, when I started, I had this thing with the Key Cloud blog post, so that was one thing.
I… I've enjoyed doing this, you know, along the way, so I may continue doing that, but then also Blueprint sounds like a good idea. Also, I wonder who takes care of the… I mean, you, Juliano, you do, you take care of the hotel demo.
Right? But should that be also a part of our discussions in here?
Or is there any other SIG, or is it, like, free flow right now?
So, I'm… I think I'm more towards, looking at the user experience overall and helping out where we can, but I do agree that having a… Specific goal helps.
Like, you know, like blueprints.
I don't have that much preference, though.
it's not like I wanna, like, do something concrete, like, I enjoy doing those, all those things, you know, so…
**Juliano Costa | Datadog** 22:26 Yup.
**Perk (Marcin Stożek) | Elastic Ingest** 22:26 It's a good sports also. Guys, we are all there in a month in Prague, maybe we have, like, you know, like.
Live SIG meeting.
**Johanna Öjeling** 22:36 And then we can work on…
**Juliano Costa | Datadog** 22:37 Totally.
**Perk (Marcin Stożek) | Elastic Ingest** 22:38 none of that.
**Juliano Costa | Datadog** 22:39 And also, maybe we have some feedbacks from the community, some folks interested, hopefully, I don't know, like, maybe the talk actually steers the… Perk (Marcin Stożek) | Elastic Ingest 22:51 Oh, definitely.
**Juliano Costa | Datadog** 22:51 To join and engage with us, and so, yeah.
**Johanna Öjeling** 22:55 - Perk (Marcin Stożek) | Elastic Ingest 22:56 Yeah, yeah, exactly, exactly, exactly. Maybe we should have a SIG after that. So maybe, you know, like, maybe… what time is your talk, by the way?
**Juliano Costa | Datadog** 23:05 I have no idea how to.
**Johanna Öjeling** 23:07 Is it around 2?
**Perk (Marcin Stożek) | Elastic Ingest** 23:09 2PM.
**Johanna Öjeling** 23:13 I can't remember.
**Perk (Marcin Stożek) | Elastic Ingest** 23:20 It would be better if it's in the morning, but if it's in the afternoon, that's not a problem. Maybe we can advertise a meeting, you know, like, we will have a SIG meeting, you know, like, at 3, or something.
**Juliano Costa | Datadog** 23:31 1…
**Johanna Öjeling** 23:32 50 feet.
**Juliano Costa | Datadog** 23:32 5…
**Johanna Öjeling** 23:33 Yeah.
**Perk (Marcin Stożek) | Elastic Ingest** 23:34 155, okay.
So that is after lunch.
**Johanna Öjeling** 23:39 Yes.
**Juliano Costa | Datadog** 23:40 Yes.
And I may be working on the booth… on the Datadog booth, so I need to check that.
**Perk (Marcin Stożek) | Elastic Ingest** 23:46 Oh, so you don't have that much time. Yeah, okay, okay, okay, okay.
Fair enough. Then we can advertise this virtual one, and we just meet, you know, when we have time in the corridor.
Yeah, okay, okay, that works.
That's what it is.
**Johanna Öjeling** 24:02 Yeah, there is a coffee break, 15.35, and then evening reception starting 17.30.
**Perk (Marcin Stożek) | Elastic Ingest** 24:10 7.30, okay. Do you… okay. Do you know how long is this evening reception? I didn't see the agenda at all, actually.
**Johanna Öjeling** 24:17 Let's see here… No, it doesn't have an… Yeah, it's on the schedule. I haven't seen it until now either, but it says, yeah, 17… 30 evening reception, doesn't happen anytime.
Oh, yeah, 8… until 1830.
**Perk (Marcin Stożek) | Elastic Ingest** 24:35 Oh, 1830, okay.
**Johanna Öjeling** 24:37 Journalists for drinks and appetizers with your fellow.
**Perk (Marcin Stożek) | Elastic Ingest** 24:40 Oh, nice, okay.
**Johanna Öjeling** 24:40 attendees. All attendees are welcome, yeah.
**Perk (Marcin Stożek) | Elastic Ingest** 24:44 We'll have time to speak, then.
**Juliano Costa | Datadog** 24:46 Oh.
**Perk (Marcin Stożek) | Elastic Ingest** 24:46 Very well.
Okay, cool. Thanks, yeah, I think it's important, I agree, I agree. Let's figure this out and try to be, try to drive things more, rigorously, maybe.
This way.
**Johanna Öjeling** 25:00 Yeah. Thanks by Juliano, do you know if there is a speaker's dinner?
**Juliano Costa | Datadog** 25:07 I have no idea.
**Johanna Öjeling** 25:09 Yeah, I haven't received any info about it, but…
**Juliano Costa | Datadog** 25:12 Yeah, there's… Perk (Marcin Stożek) | Elastic Ingest 25:14 There's no speakers dinner for KubeCon, or…
**Juliano Costa | Datadog** 25:17 Yeah, I know.
**Johanna Öjeling** 25:18 Okay, Okay, yeah, then probably not.
**Juliano Costa | Datadog** 25:23 Where is the… give me, give me just a sec. But that doesn't, avoid us from… from… Joining and having dinner, and maybe.
**Johanna Öjeling** 25:32 Yeah.
**Juliano Costa | Datadog** 25:34 So we have our SIG meeting in person.
**Perk (Marcin Stożek) | Elastic Ingest** 25:39 Actually, that doesn't sound that bad. I'll be there with my…
**Johanna Öjeling** 25:42 Maybe on Saturday.
**Perk (Marcin Stożek) | Elastic Ingest** 25:44 Yes, sir.
No, no, but the angel…
**Johanna Öjeling** 25:46 We can have an informal dinner.
**Perk (Marcin Stożek) | Elastic Ingest** 25:48 Yeah, yeah, yeah, yeah, exactly. I'll be there on Saturday and Sunday, but Sunday afternoon, it's like, yeah, sure.
If you're free.
**Juliano Costa | Datadog** 25:56 I arrive… Pretty late.
**Perk (Marcin Stożek) | Elastic Ingest** 26:00 Oh, okay.
**Juliano Costa | Datadog** 26:01 Whoa. Let me see my… Where is it? So… Why doesn't… Okay, so I arrive 7.39 PM in Prague.
**Johanna Öjeling** 26:15 Hmm.
**Perk (Marcin Stożek) | Elastic Ingest** 26:16 Okay.
**Juliano Costa | Datadog** 26:17 So, I arrive at dinner time, so… Perk (Marcin Stożek) | Elastic Ingest 26:20 Yes, straight from the.
**Johanna Öjeling** 26:21 Yeah.
**Perk (Marcin Stożek) | Elastic Ingest** 26:22 I don't know, airport or the train.
**Juliano Costa | Datadog** 26:24 I'm taking a train this time, yeah.
**Perk (Marcin Stożek) | Elastic Ingest** 26:27 Very well.
**Juliano Costa | Datadog** 26:28 Oh.
**Johanna Öjeling** 26:29 But yeah, maybe… maybe after that evening reception, if it's just drinks.
**Perk (Marcin Stożek) | Elastic Ingest** 26:34 So after, I cannot. Okay. But, anyway, no, yeah, because I'll be driving, I'll be driving for right after.
**Johanna Öjeling** 26:41 Well, we'll find some time.
**Perk (Marcin Stożek) | Elastic Ingest** 26:44 Yep. Yeah, yeah, okay, okay. We have some more time to plan this. Yes. Very well. Okay, okay, cool. Okay, I'll do the key clock, adjustments, and ping you guys.
You think? Anything else we have to discuss?
**Johanna Öjeling** 27:00 Mmm…
**Juliano Costa | Datadog** 27:00 Anything, Johanna, from your end?
**Johanna Öjeling** 27:04 No, there are no updates on the Atlassian blog post. I campaign video and check. But I… we're still waiting for James' approval.
**Juliano Costa | Datadog** 27:14 Yeah, we are waiting from James, and he replied to me, but then… He never replied back, so…
**Johanna Öjeling** 27:23 Okay, hmm.
Yeah, there has been no activity.
Since 19th of August.
**Juliano Costa | Datadog** 27:35 Just pinging him again.
**Johanna Öjeling** 27:38 Okay.
Thank you.
But yeah, other than that.
I'm… all good.
**Perk (Marcin Stożek) | Elastic Ingest** 27:50 Will?
Okie dokie. Good to see you guys.
**Johanna Öjeling** 27:53 Yeah, it's good to see you too.
**Perk (Marcin Stożek) | Elastic Ingest** 27:55 Stay around. Have a good day.
**Juliano Costa | Datadog** 27:56 Cheers. Bye.
