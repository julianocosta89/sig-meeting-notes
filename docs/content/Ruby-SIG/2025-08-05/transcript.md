SIG: Ruby SIG
Date: 2025-08-05
Duration: 28 minutes
Zoom Recording URL: https://zoom.us/rec/share/e1vVjB6M_QejdXQo940_Y0xYK7_goTWA4-JPfjNyv_trxV2aFCpW8Y2vJROzTthT.d_WSSFCp7S7Ur_AH
============================================================

## Zoom Recording Transcript

**Eric Mustin** 01:48 Can share the agenda.
**Hannah Ramadan** 02:16 Hey! There!
**Eric Mustin** 02:20 Hello! Hello!
Can let me know if you cannot see the screen.
**Hannah Ramadan** 02:35 No looks, good.
**Eric Mustin** 02:36 The today's August 5.th Okay, hello, Wendy, and I think we can wait a Scott.
I'm sorry, Rob, I think, said he would be back next week.
Okay?
And I saw Juan not. He said. He will not attend let me put.
**Hannah Ramadan** 03:05 Yeah. And Kayla is, is still out.
**Eric Mustin** 03:11 Well, good Let me just grab something from the slack. Okay, I I did not. In that case, I guess let's get started. I did not attend the spec sig.
I don't.
you know. I don't need to go over it, but I want to be respectful of everyone's you know. Use of this meeting, so I'm happy to review it, for I don't think we need to do 15 min. We could time box it to a 2 or 3 min review like last week.
and then move on to if there's any specific questions. I only had one question on or not question so much as opening, opening it up to the floor on someone, a question on Jaeger, remote sampling in the slack, and I didn't have a good answer for him, except saying, Go talk to this spec Sig folks who might.
I'm sorry a sampling sick folks who might who are kind of like working on that specification, and might be able to give you whatever updates on.
I guess situations where you're sampling. You know, at the time you're making a sampling decision. You're doing it on some attribute or span name. But then, downstream, later on after the sampling decision has been made.
Whether you could update the sampling decision? And I didn't think that was supported.
Like update it based on like, oh, the span name has changed, or something.
so it was blocking his attempt to implement the Jaeger remote sampler. Okay, I guess I went over mine first, st then. So whoops. But yeah, does anyone else have any questions? Or should we take a couple of minutes into the specs anyone Hannah, do you have any strong opinions here? Otherwise I'll just open it up.
**Hannah Ramadan** 05:14 Yeah, let's run through through that.
**Eric Mustin** 05:15 Okay.
the earlier today. And oh, my, gosh, okay.
how about we abandon this? Actually, because this is a big one and just get right to seeing if Wendy has any questions.
**Wendy Smoak** 05:39 I just kind of showed up to see how these work. And we've been using logs. And I started to play with metrics and metrics are very much not done. So I kind of just want to see. Is anyone working on it? How? What I found? I ran into a problem, and I found a Pr that's approved but not merged. So.
**Eric Mustin** 06:06 Okay, right? I recall you working on logs from slack a week or a few weeks ago. If I'm not mistaken. So yeah, it's
**Wendy Smoak** 06:16 I'll do primarily, I mean, I know they're still in development, but they they seem to be mostly under control. I mean, Kayla did all that work on them, and.
**Eric Mustin** 06:22 Yeah.
**Wendy Smoak** 06:24 They work metrics not so much.
**Eric Mustin** 06:26 Yeah, I mean the Hannah may no as well, I believe. Joan had. Who is not, as we mentioned earlier. Not this meeting has some open items he's working on for some of the metric.
I'm not sure which. Let me see, which mature usually. I cannot.
**Wendy Smoak** 06:51 I was trying the observable gauge. But it it is just not. I mean it has.
It's been checked.
It's not implemented.
**Eric Mustin** 06:57 Manager. Yeah, that's
**Wendy Smoak** 07:00 And yes, it is. Did you say it's.
**Eric Mustin** 07:03 Yeah, I'm not
**Wendy Smoak** 07:07 Okay.
**Eric Mustin** 07:08 Apologize.
**Wendy Smoak** 07:09 It's that top issue, and it links to his.
**Eric Mustin** 07:11 Yeah, that.
**Wendy Smoak** 07:11 Okay, so that that makes sense.
**Eric Mustin** 07:13 So he's not here. He had left a comment before, about 20 min ago, saying, he is working on it and the but I think he just dropped it in this slack channel. He had a specific comment around ariel is a also, not here, but is a maintainer of core of which neither for context, neither myself nor Hannah are around. I don't know some finer detail in it. But yeah, I would say, like off top of my head, it's not. I wouldn't depend on metrics in across the you know, if you're looking for like interoperability with Prometheus's, you know, or or stats these, you know. Collection of delta cumulative metrics. Yadda, yadda.
yeah, yeah, that's there's no production reliability or guarantees there, really on, I think any of it.
**Wendy Smoak** 08:09 Yeah, I mean, well, it's all of our developments.
**Eric Mustin** 08:11 Yeah, yeah.
**Wendy Smoak** 08:12 Take it, dude But the logs were marked development, and they were like after Kayla and Luna. They were pretty good, so I was hopeful, but.
**Eric Mustin** 08:18 I think the signals that have been implemented work, that there were some to some extent. There's been some some usage of some of, I think, like simple counters and stuff. But yeah, it's gone through a few like, you know. Trying to think of the good analogy of like in Indiana Jones when he's like getting to the Temple, and there's like the skeletons of people who have tried. There's there is some of that to be clear.
**Wendy Smoak** 08:46 So I mean the counter is fine. The the regular gauge, not the observable one. It doesn't respect the temporality preference that you can set as a yeah like. So someone made counter respect the temporality preference.
**Eric Mustin** 09:00 Okay.
Gauge.
**Wendy Smoak** 09:01 So I think I'm gonna open. And if if that.
**Eric Mustin** 09:03 Gotcha.
**Wendy Smoak** 09:04 It's not in the the other. Pr, I may just open that one because it's just a 1 line change to make that one work unless it's already in that pr.
so.
**Eric Mustin** 09:13 I don't have the context from last week, but I think it'll the context exists in the. I'm not sure the issues of the Prs. But yeah, I would say, Donna, I will send you down the rabbit hole like the wrong, you know. You'll probably get there faster.
**Wendy Smoak** 09:30 If I were to just look into it with you. Yeah, I don't see any.
The uppercase morality preference in the in that. Pr. So I'll maybe try to.
**Eric Mustin** 09:39 You're unable to make use the open telemetry collector pro processors, or rent to, you know, work around it, or something to that effect or just.
**Wendy Smoak** 09:50 Well, yeah, I mean, we can.
**Eric Mustin** 09:52 Thing the right way the 1st time.
**Wendy Smoak** 09:57 Well, yeah, I mean, we're not looking to use metrics right away. I was just kind of playing with it. See where we were.
**Eric Mustin** 10:01 Yeah, I think it's.
**Wendy Smoak** 10:02 And we've got the delta to cumulative processor in the in the pipeline for the moment to switch everything because Prometheus doesn't do Delta. So yeah, we're good. I just, I just wanted to kind of come and see if I try to fix something. Is someone already working on it and just go away, or like.
**Eric Mustin** 10:20 I think he's in terms of active work. I think it's just one. I don't think Kayla is contributing Hannah. Correct me if I'm wrong. So I and he's certainly happy to he's already doing, you know, in terms of like active development, some huge percentage of the active, you know, work. So I think he'd be happy to split up. Yeah, any metrics work. I just don't want to. Yeah, I don't tell you to go make a Pr. And then he's like, Hey, I have it accounted for it.
**Wendy Smoak** 10:46 That's fine, if and he may have it on a branch, and just not open to Pr yet, or whatever it's not that it's I mean I'll try that.
**Eric Mustin** 10:51 We.
**Wendy Smoak** 10:52 And then if he's back next week, I'll pop in and see what's going on.
**Eric Mustin** 10:56 I think he's around. I just he might answer asynchronously. He's gonna I think this meeting is also probably at a a not a good time for him. So I mean, that comment should have pinged the Pr. So if he's interested, I see you.
**Wendy Smoak** 11:11 Finish it.
**Eric Mustin** 11:11 Gotcha where's the Pr link.
**Wendy Smoak** 11:15 Ask the bottom.
**Eric Mustin** 11:16 Now over here.
**Wendy Smoak** 11:16 Gotcha? Yeah.
**Eric Mustin** 11:17 Okay.
**Wendy Smoak** 11:20 So maybe if that if that merges it'll get better.
**Eric Mustin** 11:22 I will.
If it's okay with you, I'll I'll try to set aside, you know, a little bit of time this week to make sure there's at least and a clear answer for the upcoming week, so that I don't look like an idiot 2 weeks in a row. But
**Wendy Smoak** 11:39 Fine.
**Eric Mustin** 11:40 Yeah, other than that, you know I got nothing else for the.
**Wendy Smoak** 11:44 It's fine.
**Eric Mustin** 11:44 I just.
**Wendy Smoak** 11:45 Kind of. I've been in the Channel for a while. I just kind of wanted to show up and see what happened.
**Eric Mustin** 11:48 Welcome every week. I swear I swear it's a much more as you can tell. I don't normally run this meeting, so I am.
**Wendy Smoak** 11:59 Summer.
**Eric Mustin** 12:00 Yeah, well.
**Wendy Smoak** 12:01 Bill.
**Eric Mustin** 12:02 Endless summer. Gotcha. Okay? Yeah. I don't want to pretend to know that. I'm up on the metrics. Stuff. Cool Hannah anything you wanted to cover? Or did you want to discuss any of your? I had one issue on? I think there are some comments on the rack er but
**Hannah Ramadan** 12:21 Yeah, that one. I think I need to spend a little more time with that. But I did see you comment. And so I haven't taken a look at those yet, but I plan to. I did have one thing, maybe, to discuss, looking for like opinions.
It's around. So I'm working on the database semantic conventions. It looks like the sequel based. Libraries are stable. Other ones seem like they're not. I can put the well in any case.
**Eric Mustin** 12:50 Oh, oh, sorry! Did you want to share? I unshared.
**Hannah Ramadan** 12:54 Yes, I can share.
Let's see, we're in all the okay. So adding some new attributes, so for the new semantic conventions, there are a few new ones that libraries don't have yet.
A couple months ago I had tried adding, I think it was the collection name to trilogy Mysql and Pg, that was blocked because we were to get those names required.
Parsing, SQL. And there were concerns about performance of having to do that every single time we see a query fair. They actually updated the collection name.
Sorry not wasn't really organized here. They updated it to make sure that we are actually not doing that. So that's fair. I think that's something that can be dropped, and if we're not doing it from that, and there's no way to get that from the libraries it seems like we probably shouldn't be collecting, that.
There are, however, some other attributes that would also require parsing, query, queries, and I, while. And one of the example would be, query summaries. So we can. We have like options for generating that.
But it doesn't. Okay. So this one. It says, Okay, cool. We're allowed to generate a query summary based on the SQL. Text.
When that was blocked for me before because of performance concerns, I am a little bit like wary of like moving forward and trying to go ahead and do some of these attributes that also require parsing SQL. Because of those concerns. So I was wondering if anyone had any opinions on this. And I can the old Pr. Where that was discussed, I believe.
Let's see, Ariel said it was okay. He thought maybe we could put it behind a config, so people could decide if they wanted to collect that. And that was for the collection name. It seems a little bit like.
All a little all over the place, which it is, you know, can be normal for hotels. We figure things out, but I wanted to see if anybody had any opinions on this.
**Eric Mustin** 15:45 let me if I could summarize what you're asking, because I actually I think I didn't. I didn't do a good job following some of the stable semantic inventions for database spans would require us to parse the You know the the SQL. Statement and we need to ensure that. And it's not just I I know we'd previously like. So at the today's state, I think we there's like the dB statement, field and we have an option to like, do obfuscation, or like some, you know, like, or or some formatting of it. So I know we parse it there. But you're saying they want to be able to like, take that and use it to inform some other attributes that we'd have to add.
**Hannah Ramadan** 16:37 Yeah, exactly. Let's see a few like query summaries, you know, something like that.
**Eric Mustin** 16:44 Yeah.
Oh, okay, gotcha. And so gotcha. And so then it's like.
under the hood, the implementation can be yeah, the extremely non performant if you're like our I think in most cases, when we people would turn on that obfuscation feature or sorry config option on the various dB instrumentation that you know whatever on some like monoliths it's like, Oh, there, you know, it's like there's like an observer effect that was like, you know, very whatever a few 100 ms. So they turn it off.
So yeah, there would have to be some sort of like overarching, you know ideally all of this logic is managed via some overarching flag that people could no OP out of that, because it seems like it would be extremely.
But you know there's there's going to be really bad performance cases for it.
**Hannah Ramadan** 17:50 Yeah, so yeah, it's so, perhaps.
**Eric Mustin** 17:53 So this is required for this is, it's not so. You're saying. It's not like Http where they I feel like the Http stands are largely just renaming of attribute keys right.
**Hannah Ramadan** 18:04 Yeah, I mean there, I don't have to add.
**Eric Mustin** 18:08 Yeah.
**Hannah Ramadan** 18:09 Attributes, I thought, why, while you know, we were updating to the new semantic conventions might as well add, the new attributes don't have to do that this round. But yeah.
**Eric Mustin** 18:24 At home.
**Hannah Ramadan** 18:25 Yeah.
**Eric Mustin** 18:25 I mean, okay, I yeah, I don't know.
I don't know.
I think it's I don't know. It's seems like a it seems like a huge hassle. But I can understand why it's valuable in theory. I just yeah would be yeah, it. It would force more of a rewrite of all the instrumentations. For you know, for this stuff, basically and we and I really don't have any best practice ideas off top of my head on the config.
**Hannah Ramadan** 19:00 Do you like your point about obfuscation being behind a config? And that.
you know, maybe there's an accepted performance hit, even if small like, for that.
**Eric Mustin** 19:10 This are some of the other languages. You know, that's always the 1st step I take is like, look at how they're kind of like are they doing some, you know. Is it just mountains or rejects? Do they have some sort of, you know?
Sql. Parsing they feel confident in, or how do they? You know I don't know. I just always is it? I assume it's implemented in a few languages, if it's in the recommended spec, so that'd be my next step, if you've you know I haven't gone down that this is the 1st I've paid attention to the database spans.
**Hannah Ramadan** 19:44 Yeah, I don't recall. I usually try to run off python, because I can.
Good.
Yeah.
**Eric Mustin** 19:53 Because they has python. Do they have this? You know, I think it's
**Hannah Ramadan** 19:59 Yeah, I haven't seen them do any migration like they had done for Http. How that looks! But I'll I'll take a look at that.
**Eric Mustin** 20:10 Especially, I would at least see like you know, especially I guess goes not. You know the some, whatever good go is probably not writing like, I think our obfuscation right now is just a bunch of rejects. So I assume they they have some more thoughtful implementations. Because, yeah, there's probably no you know, I don't even know if the Regex's we support are compatible and goes like you know, reject engine. So I assume they're doing it a little bit more intelligently might be interesting to see how they're, you know, handling this because and all I I also feel like most implementations land and go first.st but yeah, I'll should we?
So this works being tracked on an open issue? Or is it just on a branch when you were experimenting on how to do you know an internal branch, or where's Where can we sort of like?
where could I park a comment on this. If I look into whatever javascript, or python, or something.
**Hannah Ramadan** 21:11 Yeah, I don't. I? I've been tracking it kind of like separately. I don't know if there's an hotel open issue.
**Eric Mustin** 21:17 Okay.
**Hannah Ramadan** 21:17 I can create one.
**Eric Mustin** 21:19 Yeah, maybe that's a good next step I can try to. I think the next step here might be something Rob wants to do, too, is yeah, just see what the priority is.
Least.
that gives us a sense of what the expectations of users are going to be, for you know, how important some of these recommended attributes are. But yeah, I would just I mean you could split it up. Obviously, I think, is the is the if you're looking to just get unblocked on getting the Mandatory changes in are all are, are any of the obfuscate, you know, sort of like manipulation of these.
whatever large sequel statements. Are any of those in mandatory, or is just, are they just some recommended.
**Hannah Ramadan** 22:06 Yeah, they're all recommended. So it's not critical. And yeah, I guess I could move forward and just do the the naming switch.
**Eric Mustin** 22:15 Yeah, I've or I don't know. It's not be implementation dependent, too, right? Like, maybe in like whatever trilogy or something, this is a little easier. I don't know.
I don't want to lead you down the wrong path. But let's yeah. I'll maybe try to think of if we can find some examples and instrumentation that have. Added these new collection names that are at least like you, you know. Maybe this is also much easier in like, you know, Mongo, or whatever so you know, I think that's a good place to at least park a some some research on an open issue. And I I I'm sure someone will come along and and ask for it eventually it seems useful. So I don't. Wanna you know. Kick the can. But yeah, I don't have a great it's it seems problematic. So I'm a little anxious.
**Hannah Ramadan** 23:10 Yeah, we do. We do have an open Pr to add. I think it was batch size.
a row, count.
**Eric Mustin** 23:25 Yeah, I feel like I'm sure some of them are just available from the, you know. Rms, whatever out of the box.
**Hannah Ramadan** 23:34 Yeah methods. But I'll make an open. I'll make an issue. For this conversation separate from the semantic conventions migration, and maybe we just kind of like, separate. Yeah, those 2.
**Eric Mustin** 23:48 Yeah, that sounds I mean, unless I guess. Ariel left the comment originally. But he maybe just ping him on the open issue as well. And yeah.
I don't. Wanna I don't. I don't wanna leave you leaving the meeting feeling like you're stuck on not being able to move forward on some of the dB ones. So yeah, awesome work in general.
So.
**Hannah Ramadan** 24:11 And I mean, I guess there's nothing. I mean, we can always add these later.
Yeah. So.
**Eric Mustin** 24:18 Yeah, I mean, look you, I'm not. I think no one's asking you to be, an it's no one's asking you to be an expert on trilogy. So just be a good steward of. And so that's what this these Prs accomplish. So it's good. It's good work.
And you know.
we when I think if you have the the time or brain space later, or someone else who's been working on trilogy, you know, comes around as I go. This is, you know, I can test this. And I feel comfortable with how this implemented like.
yeah, it's it's in the spec to be added.
it's all good. Cool. I've just been rambling for 20 min. I think we're off. Yeah. Anything else. I think I'm doing more harm than good, so I don't want to let the meeting run any longer. If no one else has anything else.
**Hannah Ramadan** 25:11 I really appreciate your your conversation opinion there, it's all I feel like. All this stuff is.
**Eric Mustin** 25:16 And shit I'm I'm so deep in I'm like, Oh, my gosh! I can't believe I you know it's a the the the maintenance burden of the the spec is huge. It's it's not surprising that, you know. Wendy noticed that we're a little bit of a you know. I I hope I can't see if you've you know a little redhead stepchild. My my son and daughter are redhead, so I feel like I'm allowed to say that. But anyway, but yeah, Ruby, certainly, like there, there's as you can see, there's a pretty wide universe of like things that ought to get done on the repo and it's you know, best efforts on a lot of it.
**Wendy Smoak** 26:03 Oh, yeah, thanks, sir. I mean, I appreciate all the the work that's here, and I don't do it myself. But.
**Eric Mustin** 26:08 Yeah, my, as you can tell. I didn't. I didn't either.
you know. Maybe it's a little more active years ago.
**Wendy Smoak** 26:15 Yeah, we picked it up. We're just kind of getting, you know, like the we need logs. So we're gonna go ahead, even though it's it's like development. Because I've read all the code. And Kayla's there. And like, I trust, like, it's okay. But gosh! When other developers pick it up and try it, and and then like it just doesn't work in quotes.
I'm just get. I'm just getting kind of the.
**Eric Mustin** 26:39 Yeah, yeah, yeah.
**Wendy Smoak** 26:40 It's the marketing part of this, not the not the technical part of this.
Yeah, it's.
**Eric Mustin** 26:46 Wait joined elastic recently.
I felt your, you know. I felt similarly at my previous banking, you know roles, so I've tried to. But my day today isn't, you know, open source SDK, maintenance or anything? The way it was when I 1st got to, you know, be a Maintainer here or approver. I think I'm just prover but I have reached out and we have a we have a big group of the J. Ruby people at logs at, because at a elastic because of logs. Dash So I've tried to reach out to them and see if there's any interest in them.
I think they would like to contribute, because we actually don't have a lot of J. Ruby support like, in our own test suite. Like, I think, J. Ruby 10. We don't support J. Ruby. 10 But yeah, see if there's some folks there, some Rubius there who would like to contribute more, because, yeah, whatever they're good, open source people, I'm sure they are smart and have good.
**Wendy Smoak** 27:41 Yeah, I come. I come from Apache software Foundation, Java stuff way back. And
**Eric Mustin** 27:46 Cool. So you.
**Wendy Smoak** 27:47 Like working on the running edge of open source stuff in production. I'm fine because I've read all I mean, I've read all the code. It's the same stuff that's gonna get released right. But.
**Eric Mustin** 27:58 I mean speaking from my employers, you know, like if I were, if I to be devil's advocate, like I think they do have sla's and sla's, and all that stuff around the stuff they offer distributions for which ruby of which Ruby is not, you know. So. But you know.
anyway.
**Wendy Smoak** 28:17 Fun to play with, anyway. Make grass and grafana all good.
**Eric Mustin** 28:22 Yeah, I know. I know that feeling. I wish I wish I had Grafana back now. I gotta learn cabana as I was complaining last week.
Anyway. Cool. Yeah, yeah. All the best you guys. You know, I'll ping on slack if I have updates on those things. And yeah, we're, I think, try to.
We can, or, you know, respond as necessary until next week. True.
**Wendy Smoak** 28:43 See ya.
**Eric Mustin** 28:46 Bye.
**Hannah Ramadan** 28:48 Bye. Thank you.
