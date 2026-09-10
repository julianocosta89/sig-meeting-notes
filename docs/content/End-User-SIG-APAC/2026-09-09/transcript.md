SIG: End-User SIG (APAC)
Date: 2026-09-09
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

Andrej Kiripolsky 00:04:21 Here you are.
Yoshi Yamaguchi (Raintank, Inc. – Grafana Labs) 00:04:24 Andre?
Andrej Kiripolsky 00:04:25 Oh, hello! Good morning.
Or, I mean, and good evening to you.
Yoshi Yamaguchi (Raintank, Inc. – Grafana Labs) 00:04:30 Good morning.
Andrej Kiripolsky 00:04:32 Yeah, yeah, yeah.
How are you? How was the trip?
Yoshi Yamaguchi (Raintank, Inc. – Grafana Labs) 00:04:35 I'm good. It was great to meet you in person.
Andrej Kiripolsky 00:04:39 Yeah, that's a good point as well.
Yoshi Yamaguchi (Raintank, Inc. – Grafana Labs) 00:04:42 Yeah. Finally, I, I… I came back from the jet lag.
Andrej Kiripolsky 00:04:49 Oh, okay. Yikes.
It's, like, really, like, a healthy…
Yoshi Yamaguchi (Raintank, Inc. – Grafana Labs) 00:04:53 Yeah, first… first couple of days after the trip.
I couldn't sleep at the midnight.
So that was… that was tough.
Andrej Kiripolsky 00:05:03 Oh, man. Yeah, yeah.
I sometimes complain that all these cool events are in Europe. So, like, I don't get to see all the world.
At the same time, when I hear people from the U.S. and you folks.
Having jet lag and, like, actually, like, adjusting for, like, a couple of weeks to… to the time zone change.
Yeah. It has its benefits as well.
Yoshi Yamaguchi (Raintank, Inc. – Grafana Labs) 00:05:32 Yeah, I think so. So I… Before… before 2022?
So we had a… we had a… the conference called SRE Cone.
Okay. In APAC. So, ZRA Con is a series of the conference held in, U.S. and EMEA.
And, Africa, an APAC. But… the APAC one was… Canceled.
Because… because the most of the attendees are from other regions.
So… and then for… the organizer is the usernics, and then they said.
It doesn't make sense to, like, have… The people from all over the world.
And, to, to… all the way to the APAC.
So… so they canceled the APAC series.
those still they have the US one and the EMEA one, they canceled the APAC one. So, for me, I don't have… attractive SRE-related conference, large conference.
Andrej Kiripolsky 00:06:48 Interesting.
Yoshi Yamaguchi (Raintank, Inc. – Grafana Labs) 00:06:49 is not in APAC, in the same time zone. So for me, in order to join such a, like, fancy or, like, attracting event, I need to take long-haul flights to Europe or US, and then have jet lag, always.
So that's a challenge.
Andrej Kiripolsky 00:07:11 Yeah, yeah. And is it worse for you when you travel… when you travel to Europe, or when you traveled back? Because I know that it's a little different for the US folks, that when you travel to Europe, like, you have a hard time going… or, like, you get tired early, but not, like…
Yoshi Yamaguchi (Raintank, Inc. – Grafana Labs) 00:07:29 So, for… for me, traveling… going west is easier, and going west… going east is harder. So, for me, the last trip in your… our trip, I mean, our… our off-site.
Indiana was easier, because it's the way to the west.
So we flew… So, on the way to Vienna, We flew, so departure time here was… 11… No, 10… almost 11 p.m.
And then landed in Vienna.
6 AM.
So, technically, what I did was just to sleep, During the flight.
And that's it.
That was easier.
Yeah. But on the way back… that the day… was shortened.
Andrej Kiripolsky 00:08:30 Yeah.
Yoshi Yamaguchi (Raintank, Inc. – Grafana Labs) 00:08:31 So, it's… it's hard to adjust. In the case of going to West.
the day gets longer, so I need to just keep awake.
That's it. So… Yeah.
Andrej Kiripolsky 00:08:45 Yeah, yeah.
Yoshi Yamaguchi (Raintank, Inc. – Grafana Labs) 00:08:46 So, go ahead, so… Yeah, so I think, I think, so for you, going to U.S. is… is easier.
than coming back from U.S, right?
Andrej Kiripolsky 00:08:56 Like, I was there just once, but… and I was so stressed that I didn't notice any difference.
Because my flight… I had… I had a stopover, and my next flight got canceled, so I had to, like, figure it out, so I was just so stressed that I… I don't remember any… any, like, jet lag issues. But, yeah, probably… probably there was some… Something, you know.
Yeah, and how did you like the… how did you like the… Vienna offsite. Did you have a chance to spend a lot of time with the rest of the team, and anything, like, particularly interesting?
Yoshi Yamaguchi (Raintank, Inc. – Grafana Labs) 00:09:37 Yeah, so, like, because my team… is… is scattered.
In order of whatever, so they were the advocacy team, so… I finally could meet Most of the people in person.
Yeah. At the team, I mean, and also… I finally could meet many folks from OpenTemmetry community as well.
Andrej Kiripolsky 00:10:04 Yeah.
Yoshi Yamaguchi (Raintank, Inc. – Grafana Labs) 00:10:05 Yeah, like, Maria, you… And Tyler… And many folks.
So, that was… that was great, because… I saw many Grafana stars on OpenTeametry repositories as, as an icon.
But now, I meet everyone in person, and then now I could tell who's who.
Who's, who's, who's which icon, and so on. So, that was great.
Andrej Kiripolsky 00:10:38 Yeah, I enjoy this as well, a lot. Like, on one hand, like, spending time with my team is always nice, but I love that, like, right now I have basically, like, the second team with the OpenTelemetry folks, so I think I hang out, like, 50-50 with each of them, and yeah, it was really nice. It was really nice.
Yoshi Yamaguchi (Raintank, Inc. – Grafana Labs) 00:10:55 Yeah, yeah, yeah.
Andrej Kiripolsky 00:10:57 Yeah, I have just a couple of things that I wanted to discuss today, just, like, a brief… update about the survey that I have a PR opened.
If you want to take a look, feel free, but I will… I will ask, like, a lot of other people for review, so it's, yeah, totally up to you. I wanted to ask you about the Humans of Hotel Japan, if there is any blocker, or if there is anything…
Yoshi Yamaguchi (Raintank, Inc. – Grafana Labs) 00:11:24 Yes.
So the only block is the video editing part, which is handled by, Let me see…
Andrej Kiripolsky 00:11:33 I think Sofia volunteered?
Yoshi Yamaguchi (Raintank, Inc. – Grafana Labs) 00:11:34 Yeah, Sophia. Yeah, Sophia.
Andrej Kiripolsky 00:11:37 Okay, because Dan asked about it in the issue.
So I will just reply there that Sophia volunteered.
True.
That is a journalist.
8, so far.
Yeah.
Shit.
Yeah.
So, I'm writing. Then, the last update is Sofia volunteered to do the video editing, Yoshi has a blog post ready to be published once the video is done.
I think that should be… that should be it.
Okay… Yeah, that was last week. And, Yeah, so basically you are done with that. Like, on your side, I think that's… that's it, right?
Yoshi Yamaguchi (Raintank, Inc. – Grafana Labs) 00:13:14 Yeah, yeah. So, once the video is available on YouTube, then I embed it into the draft.
And then… the… the PR.
Ready to review.
And, get the final approval from the DOX approvers and, Open Territory Compass SIG. I mean, that's it.
Andrej Kiripolsky 00:13:35 Yeah, that makes sense. So I edit Sophia as an assignee to the issue, And, I guess that's… that's about… As much as we can do about this.
Yeah.
So I'm almost done with this… with the survey, so I will just move to something else. I will probably work on the survey that Marilia proposed.
To help her, like, unblock her a little bit.
Because I feel like she did not have time recently.
It's this one, to work on it, because basically we gave her a lot of feedback.
When she asked, and I think she didn't have a chance to incorporate it, so I think I will just help with that.
But… Is there anything, like, specifically APEC-related that you think I could work on? Or maybe, actually, maybe we could just start working, like, very slowly, we could start working on the Japanese survey, or, like, APEC survey that we want in December, because, like, honestly, things are not… Running super quickly.
Like, it takes a couple of months, or a month or two to get everything, prepared, so maybe that would be a good thing to get started with. But before we talk about this, I wanted to ask you about, like, a quick retro of these meetings, because, like, right now there are just two of us.
We had a… we had people joining, I think that was nice.
But… Yeah, just… just to hear your thoughts about, like, how it is going. If it is worth… Running these or not? And, yeah, what are your thoughts?
Yoshi Yamaguchi (Raintank, Inc. – Grafana Labs) 00:15:23 Yeah, so, for me, this meeting is really great, because… because I can talk to you.
Okay. So that is the biggest, biggest, value to me, because I… you are connected to both Emian U.S.
community as well. So… I can… Catch up with the latest updates from those.
So that's great. But, at the same time, I feel sorry for you to wake up early and enjoy this meeting.
And they also… I would love to have… Other… The contribution from… contributions from, like, others in APAC as well, so, I'm not sure. So this is… I'm not sure how long it takes, but, like, this isn't… I think this is not the things that we ask to… For… ask… ask them to do.
But… So far, I don't see much… You know, appetite from other folks joining this… Meetings, so that's the only concern I have. But otherwise, I'm pretty much pretty happy to join this meeting, because this is a really rare meeting.
That is held in APAC time… time… time… APAC time… APAC friendly, truly APAC-friendly.
time.
So, yeah.
Andrej Kiripolsky 00:16:58 Yeah. Okay, that's actually a super… I'm super glad to hear that, like.
it's 9am for me, so it's not really bad. Like, I wake up at 6, 7 in the morning, I have to get my kids out of the door, so they go to school, so it's not, like, inconvenient for me at all. I just wanted to make sure that We are not doing it just out of inertia, that just, like, because we started, we keep doing it without.
Yoshi Yamaguchi (Raintank, Inc. – Grafana Labs) 00:17:25 Oops.
Andrej Kiripolsky 00:17:26 Like, any value there, but… like, if you find it valuable, I think it's wonderful, I… I am happy to continue. Like, I think it's… I like the idea that we would have… we would have this meeting. If it is just two of us.
Like, moving some stuff forward.
And there is an opportunity for other people to join if they want. I think that's already… that is already, worth it.
And, I think, like, with contributions, we have to think about how to actually get people engaged and get them to contribute. Like, I tried with the issue board, I tried to, like, give people… Tasks, but as you could see, Like, some of them.
Yoshi Yamaguchi (Raintank, Inc. – Grafana Labs) 00:18:11 Yeah.
Andrej Kiripolsky 00:18:11 The start date?
But they are also joining the other meeting, so maybe that's why you don't see them.
And the APAC folks, I think there was just one, I think Nikita?
volunteered, but she actually didn't get to it. But, like, in general, I don't think it was, like.
not useful. Like, we had a bunch of people who joined just because it was APEC. There was this guy from… from Australia, yeah, yeah. There were a bunch of folks from India joining, so I think it's… and I'm pretty sure that they would not join if it was in the other time, so…
Yoshi Yamaguchi (Raintank, Inc. – Grafana Labs) 00:18:47 Yeah, so I was just not sure if they just… they're just not… Not joining this week's meetings, or… They… just… Lost the interest.
of the group, because I don't see much… messages on the Slack, for example.
Andrej Kiripolsky 00:19:12 That's…
Yoshi Yamaguchi (Raintank, Inc. – Grafana Labs) 00:19:13 Yeah, so I don't see… I can… I cannot track their activities and what they're doing.
From my point of view.
Andrej Kiripolsky 00:19:20 Yeah, yeah, that's so true.
This is something I can… I can give you, some, some context about. So, folks from Africa.
And I mean specifically Victoria and Ernest, they joined both meetings. They joined both EMEA and Apex.
Yoshi Yamaguchi (Raintank, Inc. – Grafana Labs) 00:19:38 I see.
Andrej Kiripolsky 00:19:39 So, that's why you sometimes don't get… Don't get the updates here, but they share stuff there.
Victoria is taking care of videos, and the hotelme sessions and these kind of things, so that's why So that's what she, she works on mostly, and she's pretty, pretty active right now. Ernest… has his less active periods, but he still hangs out with us, so I think that's the most important.
And, regarding folks, and Dhruv. Dhruv is joining, both meetings.
And, he, he helped with the Prometheus survey.
But… that was blocked by me, because I was super slow getting it through, and yeah, I hope he didn't just lose interest. But let's see. And but I know that he also works with contributor experience sake, so I think he's just, like, doing his own stuff as well.
And, the other folks who were joining, they are really just, like, people who, like, tried to look around what is happening, and many of them, I don't think they even, like, intended to start to contribute, so I think they just wanted to… to see how… how things, like, are doing, so that's… and that's also fine.
And, Yeah, I want to say… oh, regarding Slack. You mentioned Slack. I think… this is something I brought up last time.
At the previous… Oh, oh my god, where is it?
At the previous SIG meeting, And, that maybe we could create a separate Slack channel, because I, for example, speaking for my, like, of my own experience.
I don't really like posting to a Slack channel where there are, like.
Let me check how many people are there.
Yeah, so Victoria just wrote that she couldn't…
Yoshi Yamaguchi (Raintank, Inc. – Grafana Labs) 00:21:54 Is this, End-User SIG repository?
Andrej Kiripolsky 00:21:57 Yes, it's… this is in the End-User SIG repository in the project. Basically, the proposal is that we would create a separate channel just for contributors, because in the hotel SIG End-User channel, there are 1,000 people.
And I think that some folks might… Find it uncomfortable to post updates and share just, like, regular work stuff.
In such a big channel.
But that's just my assumption. So… Yeah.
So I think that might be a reason why you are not seeing a whole lot of activity in Slack.
Yoshi Yamaguchi (Raintank, Inc. – Grafana Labs) 00:22:31 Yeah, that's fair enough. I didn't realize how many people are joining that channel until now.
So, yeah, that makes sense, yeah.
Andrej Kiripolsky 00:22:39 Yeah, because it was a bit mixed that, on one hand, it was supposed to be, like, SIG channel, at the same time, folks… promoted it as, like, if you are new to OpenTelemetry, join this channel and introduce yourself. So that's why they are Like, a load of people there, and Yeah, I don't think this helps with just this, like, day-to-day collaboration.
Yoshi Yamaguchi (Raintank, Inc. – Grafana Labs) 00:23:02 Yeah, now I understand that the reason why, and then I get it.
Yeah, this is… this channel is truly for long-tail, you know, for long-tail people as well. So, your suggestion on the issue is… is that issue makes sense, so, so that we… we can use that, the current channel.
As the, like, announce… for the announcement, or any call to action for, say.
humans of Autel, or, like, auto, Autel Me series, and so on. Or, like, a survey.
Versus we can use the contributor's specific channel for more, like, Active, you know, frequent conversation.
For, yeah, updates and so on, so that makes sense.
Andrej Kiripolsky 00:23:53 Yeah. Yeah. Hi, Dhruv.
Dhruv Ahuja 00:23:57 Hello.
Yoshi Yamaguchi (Raintank, Inc. – Grafana Labs) 00:23:58 Oh, yeah, finally, he Dhruv!
Andrej Kiripolsky 00:24:02 We were just talking about you and everyone else, it's like, hmm, it's just two of us with Yoshi today.
So yeah, good to have you here as well.
We were just talking about the meeting, just doing some small retro about it, like, if every… like, how is everything going? Like, I think we've been doing this for… for, like, a half… not half year, probably, but… but maybe, maybe almost half year now. So just… I wanted to chat about, like, if… If we find value in this or not, but so far.
What we discussed with Yoshi is that, like.
There is a value, it is helpful.
to connect, like, because for Yoshi, it was… it was difficult to join other meetings, so at least just, like, this is one way how to… how to get connected with… with the rest of the community, so… yeah, but Yoshi, maybe… I mean, like, no need to… to summarize, just… just… just a quick, Overview of what we discussed.
Yoshi Yamaguchi (Raintank, Inc. – Grafana Labs) 00:25:02 Yeah, in short, I wanted to talk to you.
Andrej Kiripolsky 00:25:05 Yeah, yeah.
Yoshi Yamaguchi (Raintank, Inc. – Grafana Labs) 00:25:07 So Andre and I, you know, both belong to the same company, so sometimes I can talk to Andre over the internal Slack channel, or, like, our internal Zoom, but… I cannot talk to you, Dhruv, you know, especially, so there was another topic about the Slack channel.
So, the current End-User SIG Slack channel has… More than 1,000 people.
in the… in the room. So, maybe… Some people feel uncomfortable to throw messages.
In the, in the flag, like.
Dhruv Ahuja 00:25:47 You know.
Yoshi Yamaguchi (Raintank, Inc. – Grafana Labs) 00:25:48 In a casual way.
Andrej Kiripolsky 00:25:49 Yes, you do, I do.
Yoshi Yamaguchi (Raintank, Inc. – Grafana Labs) 00:25:50 Okay, okay. So, so the, so, so the, the Andre just, shared the, the issue raised in, End-User SIG repo, that is about creating the new Slack channel for the contributors only.
Dhruv Ahuja 00:26:06 Yeah.
Yoshi Yamaguchi (Raintank, Inc. – Grafana Labs) 00:26:06 The reason why we had it is because I wanted to catch up with you in the format of the Slack, or, like, Zoom, or, like, Preferably in person, but the last one is really hard, so I wanted to, you know.
hang out with you on a… on a… on a Slack and Zoom in. So we… we had such kind of a conversation until you joined.
Yeah.
Dhruv Ahuja 00:26:30 Okay.
Yoshi Yamaguchi (Raintank, Inc. – Grafana Labs) 00:26:32 Yeah.
Dhruv Ahuja 00:26:32 Yeah, I think it makes sense to have a different channel, just… just to keep things lean, because I think if you look at it now, Victoria's message, does make sense to be present there.
for example, this hotel in practice session, and then whatever internal updates that are needed. And then we can be more verbose as well. We don't need to worry about polluting the main channel. That, okay, hey, what about this, what about this, and we could have more Frequent discussions there without worrying that, okay, we need to maybe wait 2 days to get into the call, and we can then discuss it there.
For example, I joined late today. I actually was thinking that maybe I should just skip it today. Some stuff… I've been stuck with some stuff, but I thought, okay, let's bop in for 20 minutes, right? So, I think having a different channel can also then reduce the dependency on these Meetings, just… or maybe the obligation that a person needs to be present in the meeting to always stay up to date with what is actually going on, if we can be more active in a contributor-focused channel.
Andrej Kiripolsky 00:27:39 Yes, yes, 100%. I like what you said about, like, being more verbose, because, like, yeah, I definitely, when I post there, I'm, like, always checking, like, is it necessary to post this? Like, is this the way how to post it? And, you know, like, if you keep overthinking these kind of things, like, then you actually don't get as productive as you potentially could.
So let me write down… And, yeah, Dhruv, how are you doing while I'm posting? How is everything?
Dhruv Ahuja 00:28:18 Yeah, so I had a family emergency, so I was actually planning to go on holiday, so I had to go there instead.
But I'm still taking some time off of work just to unwind. And I needed a break from work, so it's been a bit hectic.
Since I joined, so, and… yeah, new job, so…
Andrej Kiripolsky 00:28:39 So you… you changed jobs?
Dhruv Ahuja 00:28:41 No, no, no. Back when I joined the current company.
Andrej Kiripolsky 00:28:45 Oh, okay.
Dhruv Ahuja 00:28:46 had to do a lot of… because I was coming from engineering to marketing.
with Azure Developer Relations Content.
person, so… Had to do a lot of, like, mental adjustment and just catching up with things and experimenting.
So, I was pending a holiday, basically.
So I'm still taking some time off, relaxing, so that is why I was a bit half-minded whether I should join, but then I thought it's always good to join, because It's always fun.
Andrej Kiripolsky 00:29:17 Nice to hear that. Yeah, I'm, like, I'm definitely, like, we are, we're… I think we are both very glad you joined, so it's, it feels less than, just one-on-one for… for two of us, and, like, as a proper SIG meeting now.
Alrighty, so I wrote this down, the stuff about, the channel.
I'm… I will do my… like, it's on one of… one of the things that is on my list to create that channel, but if anyone would like to pick it up, totally up to you. I don't think that… Yeah, it doesn't have anyone assigned, so if anyone would like to create a channel, Just feel free to.
Oh, is it in APEC? No, I won't.
We'll add a pick label.
Just so we can see it on the board.
Yeah, here it is. And for whatever reason, I put it to in progress, but let me put it back.
Yeah, with Yoshi, we also discussed that his, KubeCon Japan thing is right now… Waiting for another, person for Sophia to do the video editing, so Yoshi is basically free now.
I'm also kind of free, cause I… I just created a PR.
Wait, I forgot too.
Oh, here it is.
So here is an issue that I created in the blog.
Or in the… in the… on the website, repo, and here is PR. Dhruv, I tagged you there, so if you have time.
please take a look and give me feedback. It's not a… Like, it's probably the same thing as there was… or, like, it's almost the same thing as it was in the… in the Google Doc that you already saw, but… yeah, just having thumbs up here would… would be… would be valuable, and I'm pretty sure that you would catch up… catch some… some other things that… that we didn't.
Oh wait, I'm not, I'm not sharing.
Yeah, so this is the… this is the PR.
So, in this PR, if you… I tagged you here, so yeah, feel free to… or, like, please give me… give me, a review if… if you have time. And fortunately, we will finally get it through the finish line.
We are getting there, we are getting there, it's so slow, oh my god. Or, like, I am so slow, oh my god, sorry for that.
And, yeah, just getting back to… Our project board?
There are some things that… open to pick for anyone, so if you folks would like to pick something else to work on.
That would be amazing.
If not, no problem at all, so totally, totally up to you. I mentioned to Yoshi that I would probably try to help Marilia with her survey, but when I joined Sig End-User, I was mostly focusing on surveys, or that was the Yeah, my… My goal, that is, I would work on surveys, and honestly, I'm not doing a good job there. I think that we are doing actually less surveys this year than last year, so that's not great, that's actually pretty terrible. So, yeah, I would like to get some more surveys out.
Also, we discussed with Yoshi that maybe we could start, like, slowly preparing for the APEC survey, like, the follow-up on Japanese survey that we did last year.
Dhruv Ahuja 00:32:58 Yes, I'd also like to participate in the contributor experience survey, that you're gonna run, because I'll be there in that other, SIG as well.
Andrej Kiripolsky 00:33:08 So, you folks want to run a survey in contributor experience?
Dhruv Ahuja 00:33:11 No, no, I meant, the one with Marillia, if it's related to.
Andrej Kiripolsky 00:33:16 Oh, goodness.
Dhruv Ahuja 00:33:16 Otherwise, as well.
Andrej Kiripolsky 00:33:19 Got it, got it, got it. That's actually a good question. So, Marillia's survey is pretty… It was pretty big.
So she had, like, 30 questions there.
Yeah.
Yoshi Yamaguchi (Raintank, Inc. – Grafana Labs) 00:33:33 Oh.
Andrej Kiripolsky 00:33:34 So… That's all.
That was part of the feedback, is, like, that it's very long, and I'm pretty sure that people must not respond. Like, we wouldn't get enough responses, and then it kind of loses the whole point. So, what we need to do with Marillia's survey is to break it down into two or three smaller surveys, and then run each of them separately.
So that is the goal. I actually don't think there are, like, a whole lot of contributor experience-related things. But Dhruv, if you folks in contributor experience SIG would like to run a survey, just let me know, because there was a survey two years ago.
That folks ran.
And, I think it might make sense to just rerun the same thing and see how things are going.
Dhruv Ahuja 00:34:18 Right.
Andrej Kiripolsky 00:34:18 Yeah, so just, yeah, feel free to bring it up with the other SIG and, and see what they will tell you.
And…
Dhruv Ahuja 00:34:27 Yeah, I think, yeah, it would make sense, because, I just, on that little tangent, I raised a PR just now for improving the contributing docs, which I believe was raised in our End-User SIG Thread, and then was ported over, because there were 3 blogs being written about how people have contributed. So, Diana wrote about it, Marilia wrote about it, and then Diana wrote about it, and then the conversation happened. So, I think it definitely makes sense. I think once Amy's back, we can try poking at it.
Andrej Kiripolsky 00:35:03 Yeah, that's a good idea, that's a good idea. I know that there were some interviews being done earlier during the year, so that's why Amy didn't want to run the survey, but maybe now is the time.
Dhruv Ahuja 00:35:12 broken.
Andrej Kiripolsky 00:35:14 By the way, regarding the board, I think we can move stuff that people are actually not working on to do, just in case anyone else would like to pick it up. So, Nikita.
Volunteer to take this one.
later was in July, it was 2 months ago, and since then, she did not… join the meeting, so I will just move it back here to to-do. Also, Yoshi, I think we talked about this one, have we?
Do you remember that?
Yoshi Yamaguchi (Raintank, Inc. – Grafana Labs) 00:35:45 Oh…
Andrej Kiripolsky 00:35:47 It was a while ago, Lisa opened this, but I don't think there was any update since, like, last October, so for a year.
And I think we decided to keep this issue, But, it might.
Yoshi Yamaguchi (Raintank, Inc. – Grafana Labs) 00:36:01 Yeah, so… yeah, so now… so we… we… This conversation was stalled for a while, but… These days, we had a conversation amongst the localization team about expanding the localization team in Japan, and we concluded that we need to run some events for the, like, Japanese developers to ramp up the process for localization process.
So… Again, we'd like to run it.
Yeah. That's good. Can you, can you, can you mention… Okay, I opened up this issue, and it mentions some folks.
In a localization team.
Andrej Kiripolsky 00:36:51 Yeah, do you need to make any edits to the description, just to make sure that it still reflects what the issue is about? Or, like, so two questions. Do you want to continue with this issue, or do you want to start a new one?
Yoshi Yamaguchi (Raintank, Inc. – Grafana Labs) 00:37:04 Okay, I think the… the plan is slightly different from the original intention, so I'll open up the new… Okay. …new issue. Referring… referring to this… this, issue. So, I'd open up the new issue, and then you can close this issue anytime.
Andrej Kiripolsky 00:37:25 Can I ask, or, like, I actually don't know if, if, Can I ask you to close it once… so we will close it with the link to the new issue, just to make sure there is a connection.
Yoshi Yamaguchi (Raintank, Inc. – Grafana Labs) 00:37:36 Okay, okay, make it clear.
Andrej Kiripolsky 00:37:38 I don't think, actually, anyone would… would lose any context. It's been a while, and it was really just you participating with a bunch of other folks, but I think it would be just… it would be nicer if, if… we link these two, so I'll make a note in the…
Yoshi Yamaguchi (Raintank, Inc. – Grafana Labs) 00:37:56 in June.
Andrej Kiripolsky 00:37:58 In our doc.
So, Yoshi will go…
Yoshi Yamaguchi (Raintank, Inc. – Grafana Labs) 00:38:10 Oh yeah, so this is the event, for, virtual event.
Right?
Andrej Kiripolsky 00:38:18 Yeah, I think it was supposed to be… like, it was very, very early when we started talking about, about.
Yoshi Yamaguchi (Raintank, Inc. – Grafana Labs) 00:38:24 Right, right.
Andrej Kiripolsky 00:38:25 So, I know we talked about, like, a lot of different things.
Yoshi Yamaguchi (Raintank, Inc. – Grafana Labs) 00:38:29 Yeah, this is… this is to… this is… The… this top… this is the topic to run autoimm practice and autonomy in APAC region.
Andrej Kiripolsky 00:38:38 But we have another issue for that as well, so… oh yeah, that's the OZLM blog post that was… But it's a book post, it's separate.
Yeah. I mean, we don't… we probably don't need, like, a general issue to, like, run events.
in APEC, like, if you want to run an event, you… I think it would be better to create a specific issue for that particular… That particular event.
So, let me move…
Yoshi Yamaguchi (Raintank, Inc. – Grafana Labs) 00:39:05 Yeah, I have… I have… if time allows, I'd like to run the auto-me or ordering practice in… region as well.
But that one is different from the conclusion that they… that we made in a localization team. So, these two are different topics, so… I don't know. Okay, I'll leave some comments on this issue about the virtual event issue.
Andrej Kiripolsky 00:39:39 Sounds good.
Yoshi Yamaguchi (Raintank, Inc. – Grafana Labs) 00:39:39 As well, and then also, I will create a new issue for, like, ramp up.
upstream contribution event in Japan as well.
Andrej Kiripolsky 00:39:50 Sounds good, sounds good. Okay, by the way, and I will, I will add a link to the board, both to the… To the notes, and to… And here, I send it here as well in the meeting.
Is any one of you using Discord?
Yoshi Yamaguchi (Raintank, Inc. – Grafana Labs) 00:40:12 I am.
I, I, I noticed that my…
Andrej Kiripolsky 00:40:16 My discomfort.
Yoshi Yamaguchi (Raintank, Inc. – Grafana Labs) 00:40:17 Somebody's sending, you know, noisy, point.
Andrej Kiripolsky 00:40:20 Good.
Yoshi Yamaguchi (Raintank, Inc. – Grafana Labs) 00:40:21 Sound.
Andrej Kiripolsky 00:40:22 I'm also a Discord user, so when I… and I use it just for, like, playing computer games, so when I hit Discord, like… like, there's a very specific.
Yoshi Yamaguchi (Raintank, Inc. – Grafana Labs) 00:40:30 I'm trying… I'm trying to, like, the… I'm trying to mute the sound of the Discord, but I…
Andrej Kiripolsky 00:40:37 I'm sorry.
Yoshi Yamaguchi (Raintank, Inc. – Grafana Labs) 00:40:37 How to do it.
Andrej Kiripolsky 00:40:38 No, me neither, me neither. No, it's fine, just, just, yeah, as I said, like, whenever I hear it, there's, like, there's, like, Pavlov reflects off…
Yoshi Yamaguchi (Raintank, Inc. – Grafana Labs) 00:40:47 Oh, yeah, yeah, yeah.
Dhruv Ahuja 00:40:48 Give me a…
Andrej Kiripolsky 00:40:48 Nothing's happening, nothing's happening.
Anyway… Cool, so this is good. By the way, regarding hotel in practice.
think about it. If you would like to run it, I'm more than happy to help.
I can co-host if you want, or Victoria can co-host. I know, look, she's… she was co-hosting some of the… some of the sessions recently. Dhruv, also, if you would like to join and help running these, we are more than welcome. So, I think that would be… that would be wonderful.
Yoshi Yamaguchi (Raintank, Inc. – Grafana Labs) 00:41:21 Yeah, so the one question is that, many Japanese developers, I mean, all the practitioners are interested in joining this video series, but the problem is they are not comfortable with with, you know, getting interviewed in English.
So… so that, that, that kind of things are discussed in the, in the original issue on the GitHub.
Yeah, and So, my question is, if it's okay to run it in Japanese, or, otherwise, we need to find someone in the Epac region.
who… who use OpenTeametry.
In… in practice. So, this is the question.
Andrej Kiripolsky 00:42:08 I mean, whatever works for you better. The suggestion that we can help is more about just, like, if you need help, and if we can help with something, we are happy to. If… with Japanese… with running the Japanese, I don't think I would be able to help, or anyone else on the team.
Yoshi Yamaguchi (Raintank, Inc. – Grafana Labs) 00:42:26 Yeah, yeah, yeah.
At least, at least in the case, at least, in the case, I can run the, the, the, that… event in Japanese, then I'm happy to run it. I can… I'm happy to host the event.
Andrej Kiripolsky 00:42:39 Sure, sure, sure.
Yoshi Yamaguchi (Raintank, Inc. – Grafana Labs) 00:42:41 And my only concern I have is the same as the ordering human, so the same as the ordering human.
I can… I can shoot and record a video, like, I just record a Zoom video.
And then… send the recorded video to Sophie, Sophia, or someone who can do the video edit. The problem is, this time.
The length of the video should be longer than 10 minutes, at least, right?
Andrej Kiripolsky 00:43:09 So…
Yoshi Yamaguchi (Raintank, Inc. – Grafana Labs) 00:43:10 Yeah, the video captioning is the problem.
That's the only quota I have.
Andrej Kiripolsky 00:43:18 So… For hotel and practice, we had… There was a guy from Dynatrace, Henrik, if I'm not sure.
Yoshi Yamaguchi (Raintank, Inc. – Grafana Labs) 00:43:31 Yeah, Henrik, yeah, yeah, yeah, yeah, yeah.
Andrej Kiripolsky 00:43:32 So he was helping with the technical side of things, so he has… a program for running live streams and stuff, and I know that this is something that's really important for Adriana and Rhys, that the I mean… For humans in hotel, like.
It's something that we run during the event, so it… We can do it in just, like, perhaps less prepared way.
But for… I think for Auton, in practice, they really wanted to keep the quality bar high, just so it.
Yoshi Yamaguchi (Raintank, Inc. – Grafana Labs) 00:44:09 Right, right, right. Yeah, yeah, yeah.
Andrej Kiripolsky 00:44:11 Let me open this with them in the APEC meeting afterwards, just to double-check that if it would be okay to run it just as a recorded Zoom meeting, and then post it to YouTube.
Or if, it would be better to get Henrik involved, and do, like, a proper, hoteling practice with, like, all the setup, and not sure if you saw it, but, like, Henry is doing the transitions, and, like, it has some…
Yoshi Yamaguchi (Raintank, Inc. – Grafana Labs) 00:44:41 Yeah, yeah.
Andrej Kiripolsky 00:44:42 waiting room, and, like, it looks much more professional, and I think that's something that folks found very, very important. So, just want to double check with them.
Yoshi Yamaguchi (Raintank, Inc. – Grafana Labs) 00:44:52 Yeah, now I remember that Hendrik is using StreamYard for the recording, and then they do… he does… Like, video switching and so on, by himself, so… Yes.
Yeah, yeah, I remember that.
Andrej Kiripolsky 00:45:07 Okay, okay. But, I mean, we will figure out how to do it. Do you have any, like, ideas about who could be… who could participate already?
Yoshi Yamaguchi (Raintank, Inc. – Grafana Labs) 00:45:20 Yeah, so, the people, I say, in, alternating human videos are happy to join.
Andrej Kiripolsky 00:45:28 funny.
Yoshi Yamaguchi (Raintank, Inc. – Grafana Labs) 00:45:28 If it's okay.
Andrej Kiripolsky 00:45:31 Beautiful.
Yoshi Yamaguchi (Raintank, Inc. – Grafana Labs) 00:45:31 Also, we have, more people, who, who use OpenTemmetry in practices, in production, I mean. Yes. So, yeah, we have many candidates.
Andrej Kiripolsky 00:45:44 Okay, yeah, and just to clarify, hotel in practice is for… and this is just, like, this is just a naming thing. Hotel in practice is for hotel contributors who want to share some stuff.
Yoshi Yamaguchi (Raintank, Inc. – Grafana Labs) 00:45:57 Oh yeah, oh yeah.
Andrej Kiripolsky 00:45:57 like, deep dive technical things, that's my understanding, and then there is.
Yoshi Yamaguchi (Raintank, Inc. – Grafana Labs) 00:46:01 Let me see.
Andrej Kiripolsky 00:46:03 where people describe how they use hotel in their session, and basically it's… it's a very… it's simpler, it's much more simple, because with hotel in practice.
You would act as a host, that you would introduce the people?
And then they are basically giving a presentation, and then there is a Q&A at the end.
with HotelMe, it's… It's a conversation between you and the person, and you are asking some, like, a predefined set of questions.
Yoshi Yamaguchi (Raintank, Inc. – Grafana Labs) 00:46:35 So I was… I was imagining the alter me, mostly.
Andrej Kiripolsky 00:46:39 Okay, hotel me.
Yoshi Yamaguchi (Raintank, Inc. – Grafana Labs) 00:46:40 So, yeah, so I have many candidates… we have many candidates for AutoMe in Japan, at least. And also, we have a couple of candidates for autoimm practice as well.
So, the Japanese… not Japanese, but the… one… Vid, text messaging service called Lying.
Is using OpenTemmetry for… for… for, instrumentation, of their software side application.
And then that is… the workload of… of the… of the chemistry is really large.
So it's like… it's like WhatsApp.
Andrej Kiripolsky 00:47:23 Oh, nice.
Yoshi Yamaguchi (Raintank, Inc. – Grafana Labs) 00:47:23 Yeah, so, and also, they, they run all of their workload on their own hardwares. Oh, nice. They're not using cloud. So, this is the things that… Usually, we don't have.
So, we can ask them… we can ask the person in charge of the, like, observability area in the team, so… That should be a really good candidate for authoring practice, I guess.
Andrej Kiripolsky 00:47:56 I think this would be for hotelme.
Or.
Yoshi Yamaguchi (Raintank, Inc. – Grafana Labs) 00:47:59 No, no, no, no, no, so for order me, oh, so you need the contributors?
Active contributors.
Andrej Kiripolsky 00:48:06 For hotel in practice, it would be contributors talking about…
Yoshi Yamaguchi (Raintank, Inc. – Grafana Labs) 00:48:10 Okay, okay.
Andrej Kiripolsky 00:48:11 But let me double-check that as well, I can… or we have a… we have a… And… user resources… Let me share this. And, Yeah.
So, OTelMe is a discussion between our host and end user about their OpenTelemetry adoption and implementation, and OTEL in Practice is interactive enablement session on different aspects of OpenTelemetry by contributors and End users.
Yoshi Yamaguchi (Raintank, Inc. – Grafana Labs) 00:48:41 I see.
Andrej Kiripolsky 00:48:42 So it's really more about enablement than their own, like, than explaining their setup.
But again, this is just… this is just, like, a naming, like, we definitely have a format for whoever you will…
Yoshi Yamaguchi (Raintank, Inc. – Grafana Labs) 00:48:54 Yeah.
Andrej Kiripolsky 00:48:54 Want to interview.
Yoshi Yamaguchi (Raintank, Inc. – Grafana Labs) 00:48:56 So, in Japan, we don't have many contributors to OpenTeametry, and especially, they are not the… though we have a couple of contributors, they are not the, like, continuous contributor to the project. Got it. They just… yeah, they just… contribute… they have just contributed to the OpenTeametry.
By chance, you know, while they're using OpenTemmetry, they found a couple of issues, and then they fixed it, and that's it. So, they are not regular contributor to the community. So, in the case of Japanese community, most of the folks And almost 100% of the folks are candidates for OTLME.
Andrej Kiripolsky 00:49:37 Sounds good, sounds good. Yeah, so… once you feel ready, feel free to just create an issue. I think we have an issue template for that, for HotelMe. Like, it's the same template as you use for humans, Hotel, but this one should be actually a little bit… this time, it should be more useful, because for humans of Hotel… it is actually a template for hotelme, so for Humans of Hotel, you had to, like, tweak it quite a lot. Now you should be able to, like, reuse it.
the content that is… that is there. Wonderful. So this sounds good. I will talk to… Adriana and Rhys about the technical stuff, but I think you can… Just go ahead and, and, and…
Yoshi Yamaguchi (Raintank, Inc. – Grafana Labs) 00:50:22 Fantastic.
Makes sense.
Andrej Kiripolsky 00:50:25 Start preparing, and let… just let us know if you need any… any help.
Again, except for hosting.
Yeah. Dhruv, how are your Japanese skills?
Dhruv Ahuja 00:50:39 I mean, Shiva, Shiva Dhruv. I think that…
Yoshi Yamaguchi (Raintank, Inc. – Grafana Labs) 00:50:42 Oh, perfect!
Andrej Kiripolsky 00:50:43 Nice, nice, nice, nice.
Dhruv Ahuja 00:50:45 This is all I know, and I remembered the word Vatashiva as soon as you asked me how about your Japanese skills, so it was spur of the moment.
Andrej Kiripolsky 00:50:54 Nice, nice, nice.
Dhruv Ahuja 00:50:56 That is basically all I know.
Andrej Kiripolsky 00:50:59 That's… that's… I mean, like, that's a good start, like, maybe next, so next one will be, Dhruv will be hosting the next one in Japanese. Yeah.
Yoshi Yamaguchi (Raintank, Inc. – Grafana Labs) 00:51:08 Excellent.
Andrej Kiripolsky 00:51:09 I don't know, I don't know anything, like, not a single word, and that's… That's pity, that's pity. I should, I should, learn something.
Dhruv Ahuja 00:51:17 I'm proud… I spoke clearly, so I'm proud of that, at least.
Only if it was 3 words.
Andrej Kiripolsky 00:51:24 Yeah, nice, nice, nice, nice. Alrighty, so, Yoshi, for you, we have… Bunch of, next steps… as I said, for me, it will be really a survey that's super important to enable her on that, or, like, help her move forward with that. Dhruv, for you, totally up to you, as I said. I know that you are involved also with ContributorSeek, so yeah, just wanted to mention that, like, in case you would like to pick up anything, you are always super Super welcome.
And, yeah, by the way, talking about Japanese, community.
I talked to Ted Young from TC, last week.
And he also mentioned this, this thing that… because I mentioned that we are running the APEC meetings, and that actually we have a lot of folks joining from… or, like, we have folks… we had folks joining from Australia, from India, from Philippines, and different countries, but actually nobody from Japan. And this is what he also mentioned, that people from Japan might… prefer to join if it's, like, actually, like, in Japanese, so they might… they might not… feel comfortable joining a meeting that is in English, so… Oh… Yeah.
We'll have to.
But I don't think…
Yoshi Yamaguchi (Raintank, Inc. – Grafana Labs) 00:52:49 Yeah, they're just not… Used to… not… used to speaking in… you know, making a conversation in English, that's it. So, they are, like, still there, okay to… to joining the meetings.
Just listen to it.
But they have some trouble when it comes to… You know, raising the topics by… by themselves, and also making the conversation, so because… because they're… they're not… they're just not get… they're… they do… just not… do not get used to… No, listening to understand what the… no, no, no.
Speaking English sentences.
So…
Andrej Kiripolsky 00:53:33 Yeah, I'm… I understand, I totally, totally understand.
But… what… and what I'm bringing it up, because Ted suggested that we could run meetings specifically in Japanese, I think it's a good idea, but perhaps a little later. Like, I think that as a… like, first step, I think this meeting is okay, and but I don't think we have a capacity right now to… Or, like, for you to run a separate meeting. And also, since you don't have any backup.
I don't think it would make sense to spin a separate, like, specifically Japanese meetings.
Do you agree?
Yoshi Yamaguchi (Raintank, Inc. – Grafana Labs) 00:54:10 Hell yeah.
Yeah, yeah.
Andrej Kiripolsky 00:54:12 Okay.
Yoshi Yamaguchi (Raintank, Inc. – Grafana Labs) 00:54:13 Yeah, for me, for me, I always welcome any support for Japanese community, but only concern I have is extra burden or extra effort for all of them, like, and especially, therefore, the amount of effort is larger, if you're a large one, than… You know, that is… the result will be… You know, really hard, like… that kind of effort cannot be usually, sustainable, so that's the only question I have. But if… as long as you don't feel, like, you don't feel it as a burden, then that'll be great.
Andrej Kiripolsky 00:54:51 Hmm… Yes, but the… so… but you mean, just to understand it correctly, you mean that it would be great to run it, but at the moment, it would be a problem because you don't have anyone to help with that effort.
Yoshi Yamaguchi (Raintank, Inc. – Grafana Labs) 00:55:07 Yeah, for example, for example, if I… so I'm happy to run… I'm happy to host that kind of, you know, Japanese-specific Meetings and so on, but someone needs to communicate with us, right?
Andrej Kiripolsky 00:55:25 You mean that there should be… there should be people joining, or you mean that there should be someone with the rest of the community?
Yoshi Yamaguchi (Raintank, Inc. – Grafana Labs) 00:55:33 So, the community of, say, for example, if I were the lead of the, like, the meeting, Then… I need to summarize everything into English.
Andrej Kiripolsky 00:55:45 Oh, yeah, no, I understand, I understand.
Yoshi Yamaguchi (Raintank, Inc. – Grafana Labs) 00:55:48 Yeah, yeah, so that is the straightforward.
Andrej Kiripolsky 00:55:51 That makes sense.
Yoshi Yamaguchi (Raintank, Inc. – Grafana Labs) 00:55:52 Yeah, so… Yeah.
And also, even if someone can help us, that person, needs to… to… Needs to keep looking after The meeting, like, or community.
Andrej Kiripolsky 00:56:10 Right. Yeah.
Yoshi Yamaguchi (Raintank, Inc. – Grafana Labs) 00:56:10 So that is kind of… that… this kind of thing doesn't happen if the Japanese developers can join the common meetings.
Yes.
Andrej Kiripolsky 00:56:22 Yeah, yeah.
Yoshi Yamaguchi (Raintank, Inc. – Grafana Labs) 00:56:23 where all conversations are in English directly. So, yeah, so that's the only concern I have.
If it's… Got it.
From the sustainable point of view.
Andrej Kiripolsky 00:56:37 Got it. Yeah, so for now, I would suggest to keep it as it is, and maybe later we can… we can open the…
Yoshi Yamaguchi (Raintank, Inc. – Grafana Labs) 00:56:44 Yeah, yeah.
Andrej Kiripolsky 00:56:44 Yen.
Yoshi Yamaguchi (Raintank, Inc. – Grafana Labs) 00:56:45 Hell yeah.
Andrej Kiripolsky 00:56:47 Okay, we have 2 minutes to go. Anything else before we wrap up?
Dhruv Ahuja 00:56:51 Yeah, Andre, I wanted to ask, so you mentioned that I could potentially help out in the live streams, so what does that typically entail?
Andrej Kiripolsky 00:57:00 So, usually… or, like, the way how I started with livestreams was really just… I was there to lead the Q&A, just… because it's… it's easy. So… I think that's… that's the best way how to… how to first try it.
What would be the steps to do it is… You would… reach out to Victoria or Sophia, who are leading livestreams right now.
Because they have a bunch of live streams lined up, and just tell them that you'd be happy to help, and I'm pretty sure they would be able to find… U… A… Yeah.
Figure out how to get you involved.
I, I think I would definitely recommend this, like, just, just leading the Q&A. That's… like, the last 10 minutes of the livestream, you are there to ask some follow-up questions from the community, and that's kind of it. So if this would be interesting for you, I would recommend to… I know that you are joining also the other meeting, or you joined it a bunch of times, so… Are you right, if I remember correctly?
Dhruv Ahuja 00:58:17 Yeah, yeah, yeah, I'm joining.
Andrej Kiripolsky 00:58:18 Yeah, so I think it would be the best to mention it there, that you are happy to help. I'm pretty sure that they would be happy to get… Because, like, it's a lot of effort, and again, like, I think it's pretty easy to start hosting the events. I think that folks will be more than happy to to have you as a host over time, but I think the first step is always just this, like.
just leading the Q&A, and And, doing something small, just also for you to get used to it.
Would you have an ambition to lead these kind of things?
Dhruv Ahuja 00:59:01 I'll give it a shot and see, because typically the calls happen late at night for me, so… That's kind of… Even in the last, even in the last call, I was half asleep, that's why I didn't turn off my… turn on my camera.
Andrej Kiripolsky 00:59:17 Got it.
Yeah, yeah, I understand, I understand. Yeah, that's, that's tricky, that's tricky. But… I think that for… Yeah, mention it there, and we'll try to figure it out somehow.
Dhruv Ahuja 00:59:33 Yeah, yeah.
Andrej Kiripolsky 00:59:34 I can imagine that, for example, if, if, In case we find someone English-speaking in APEC, we can… we can run it together, and then… then it should be, like, normal… normal time for you. And… and, Oh, yeah.
Or if… if it's somebody in, like, European or, like, EMEA, that should be… that should be still pretty… pretty fine. But yeah, you said that it's… that it's, that it's already too late. Yeah, we'll figure it out. Let's… let's… let's discuss it at the… at the main meeting.
Dhruv Ahuja 01:00:06 Yep.
Yoshi Yamaguchi (Raintank, Inc. – Grafana Labs) 01:00:07 Sorry, folks, I gotta go, but, thank you for making time, and I'm looking forward to the next meeting, and also updates on these topics.
Andrej Kiripolsky 01:00:15 Yeah, me too, me too, yeah. Bye-bye.
Yoshi Yamaguchi (Raintank, Inc. – Grafana Labs) 01:00:18 That's interrupt.
Dhruv Ahuja 01:00:19 Okay.
