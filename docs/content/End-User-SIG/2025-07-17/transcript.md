SIG: End-User SIG
Date: 2025-07-17
Duration: 59 minutes
============================================================

## Zoom Recording Transcript

**Andrej** 00:37 Hello, Sophia!
**Sophia Solomon** 00:41 Hello, Andre, how you doing.
**Andrej** 00:44 Pretty good, pretty good. How are you.
**Sophia Solomon** 00:46 I'm good. I'm good.
**Andrej** 00:49 Great to see you in the in the Seek End user meeting. I haven't haven't seen you before.
**Sophia Solomon** 00:55 Yeah, yeah. I'll give you some background. I'm like a new developer advocate with elastic. And so they want me to get more involved in. Like the Cncf community.
**Andrej** 01:06 This limit.
**Sophia Solomon** 01:06 Tree, so.
**Andrej** 01:08 That's amazing. That's amazing. I think you are in the right place then, because I know that a bunch of folks who are joining regularly, are also dev advocates.
So, yeah.
**Sophia Solomon** 01:18 Awesome, awesome.
**Andrej** 01:23 Hi lisa hi lutao.
**Lutao Xie (Datadog)** 01:27 Hey? Long time.
**Andrej** 01:30 Oh, yeah.
Oh.
**Adriana Villela** 01:42 Hey? How's it going.
**Lisa Jung** 01:44 Adrian, how are you?
**Lutao Xie (Datadog)** 01:45 Hello!
**Adriana Villela** 01:47 Sorry I'm multitasking. I'm gonna be making lunch while we chat.
**Andrej** 01:56 No worries.
**Adriana Villela** 01:59 Nice to see some familiar faces whom we haven't seen for a while, and I see we have a new joiner.
**Sophia Solomon** 02:05 Hello!
**Adriana Villela** 02:07 Hi! Welcome! Is this your 1st time attending? Because I think I missed the last meeting so.
**Sophia Solomon** 02:12 Yeah, totally. Hi, I'm Sophia. I'm a developer advocate from elastic. I'm pretty new. I started like a month ago. So just.
**Adriana Villela** 02:20 Amazing, amazing welcome. I'm so excited to have so many people. Who have joined the end user. Sig in the last little while.
yeah. For for some background it is. It used to be basically 3 of us. Running this thing for the last little while. So it's it's so nice to have some like new faces join and all sorts of fun enthusiasm.
So yeah, is this your 1st advocacy role?
**Sophia Solomon** 02:51 Yeah, yeah, I was a software engineer at General Motors for.
**Adriana Villela** 02:56 Oh, it's 40.
**Sophia Solomon** 02:57 Years, and then I got this awesome rolling, elastic, and I don't know it's been fun. I like it a lot.
**Adriana Villela** 03:03 So cool. Where? Where are you based out of.
**Sophia Solomon** 03:05 Austin. I'm in Austin, so if anyone else is, please, nobody.
**Adriana Villela** 03:11 I'm in Canada. I'm in Toronto.
**Sophia Solomon** 03:14 Oh, nice! I always wanted to go to Canada like that sounds weird, being an American. But like, really, I've always wanted to go to Canada.
**Adriana Villela** 03:24 That's so cool.
**Reese Lee** 03:26 Oh, that's not weird at all. And Hello! Hi! Everybody.
**Adriana Villela** 03:29 Hey, Reese? Nice to see you.
**Reese Lee** 03:31 You, too. I know I I've been so, mia! I'm.
**Adriana Villela** 03:36 Oh, my God!
Me too! Me, too! I I think the last meeting I was I was in Japan for Cubecon. So
**Reese Lee** 03:44 Nice.
**Adriana Villela** 03:45 Where I was like it. I think it was a 13 h time difference from from Toronto, so like when I got back, I like the jet lag going. There was okay. But coming back, I was wrecked for 2 weeks.
like, Oh, yeah.
**Reese Lee** 04:00 That's yeah.
**Adriana Villela** 04:01 Oh, my God!
**Reese Lee** 04:02 Right, they say, like an hour.
It takes your body like a week to adjust per hour. I mean, I don't know if that's.
**Adriana Villela** 04:08 Yeah.
**Reese Lee** 04:10 Or or sorry a day, not a week.
**Adriana Villela** 04:12 Yeah, it's a, it's a day per hour, right? Something like that. Yeah. So it was like, yeah, it was about 2 weeks. So yeah, I I've never experienced anything like it, but it was fun.
So nice nice to see everyone.
**Reese Lee** 04:25 I know. Hey, Lisa, seen you in a while, either.
**Adriana Villela** 04:28 Yeah.
**Lisa Jung** 04:29 When you say you put them away. I'm like me, too.
**Adriana Villela** 04:33 I'm back. Yeah, hey, you you you had your hands full with Grafanicon. Right.
**Lisa Jung** 04:39 Yeah, Grafanacon. And then I found out I was speaking at Hotel Community Day. So like.
**Adriana Villela** 04:45 Oh!
**Lisa Jung** 04:45 I got back it was just like Bam, bam.
**Adriana Villela** 04:47 Oh, yeah.
**Lisa Jung** 04:48 Yeah. Sorry.
**Adriana Villela** 04:49 And then it's the rush to like, Get get the talk. It's like, Yeah, you got accepted. Oh, shit. I got accepted.
**Lisa Jung** 04:55 Exactly.
**Adriana Villela** 04:57 Yeah sets in.
**Lutao Xie (Datadog)** 05:00 I ran into Lisa in person at in Denver.
**Adriana Villela** 05:05 Oh, yay! Amazing! How was it?
**Lisa Jung** 05:08 It was fun. It was fun. I got to meet a lot of people I met Austin there, and it's kind of like surreal to see people you see on like zoom in like in person. So that was like wild. But yeah.
yeah.
**Adriana Villela** 05:21 It is, and then then you find out how tall or short they are like when people meet me, they're like, Oh, you're a lot shorter than I expected. I'm like, really. I come off as tall.
**Lisa Jung** 05:33 Yourself tall.
**Adriana Villela** 05:35 Thank you. Yeah, I'm I'm 5, 3. So I'm definitely not tall.
So I guess I guess we should get down to business. Actually, maybe we should introduce ourselves, since Sophia is a new joiner.
It! It would probably be helpful so that she knows who's who in the sink.
**Sophia Solomon** 05:56 Yeah, that'd be so cool. Please.
**Adriana Villela** 05:58 Cool cool. I'm gonna show my face briefly. To introduce myself before I return to making my lunch. Hello, I'm Adriana. I'm based out of Toronto. As I said. I am a developer advocate at Dynatrace, and I guess I've been involved in the hotel community for the last, I guess, since 20, I wanna say, since 2022 And that's around the time I met Reese and and we we are like hotel talk, buddy speakers.
slash conference world travelers.
**Reese Lee** 06:37 As long as long as you really keeps them, letting me come.
**Adriana Villela** 06:44 I know right.
**Reese Lee** 06:46 I'm developer relations engineer at new relic. I've been involved in delta committee since late 2021, and yeah, it's been really exciting to see the projects.
Broad words it is. And you know, continue.
And yeah, I'm excited to see more new faces and see the new old faces, old new faces so, and.
**Adriana Villela** 07:17 And Reese was one of the Og maintainers of the end user Sig when it was still a working group, and then I joined a little bit after yeah.
**Reese Lee** 07:29 Yeah for a long. Just us 2, and like one or 2 other people chugging along.
**Adriana Villela** 07:37 Yeah.
**Reese Lee** 07:38 So we're very excited to have.
**Adriana Villela** 07:40 No, we're like, yeah, people who care.
Thank you for caring.
**Reese Lee** 07:47 Yeah.
Lisa.
**Lisa Jung** 07:51 Sure I can go next. Hi, Sophia! We've already met. I'm Lisa. I'm a dev advocate at Grafana. What else? I've been joined the Sig for almost over a year now, I think.
and have been having a lot of fun. Yeah. Glad to have you join us so.
Andre, do you want to go next.
**Andrej** 08:13 Of course. So Hello, my name is Andre. I'm a user researcher at Grafana labs.
And I'm based in the Czech Republic in Europe. And yeah.
I randomly bumped into sick end user roughly 4 months ago or 5 months ago, and I'm very happy about it ever since then, and they are trying to contribute some.
**Reese Lee** 08:38 Oh, so have we. We've also been very happy.
**Andrej** 08:42 Yeah, so this is like.
**Adriana Villela** 08:43 Indeed.
**Andrej** 08:45 Ulta luta. When you continue.
**Lutao Xie (Datadog)** 08:48 I'm lu Tao from Datadog as a product manager. I found myself the only product manager.
not heavily, but, you know, starting to go into the Sig meetings. Yeah. So I've been at datadog for 3 plus years, mostly on the collector experience side.
Yeah.
I have been in and out for a little bit. But still looking for areas that I can contribute to the group.
**Adriana Villela** 09:26 Oh, awesome!
**Lutao Xie (Datadog)** 09:27 No thanks for everyone speaking.
**Sophia Solomon** 09:29 Thank you. Everybody.
**Adriana Villela** 09:29 Yeah, I think we've got everyone.
**Sophia Solomon** 09:31 Nice to meet everyone.
**Adriana Villela** 09:33 Yeah. Nice to meet you, and thanks again for joining is there? Is there anything that you had in mind that you wanted to get out of contributing to the Sig, or you just kind of like.
**Reese Lee** 09:48 Checking things, out.
**Adriana Villela** 09:49 Waiting to see.
**Sophia Solomon** 09:51 Yeah, I mean, I want to contribute, like, actively to like the hotel like Cncf community. But for the time being I'm just kind of getting a sense of like everything, and how everything is working together. You know.
**Reese Lee** 10:06 Oh, yeah.
**Adriana Villela** 10:08 Sounds good.
Shall we?
Can someone put up? Pull up? I guess the the meeting notes if there's anything on the agenda. Did anyone add anything to the agenda?
**Reese Lee** 10:26 There's a few items on here.
**Adriana Villela** 10:28 Oh, amazing! Yay!
**Reese Lee** 10:30 Then also pull up first.st
**Adriana Villela** 10:37 Can we put an item just to do like a recap on the Apac hotel and practice in case anyone attended.
**Reese Lee** 10:56 I'm so used to, you know, these events being in our time zone that I completely spaced that this was happening.
**Adriana Villela** 11:05 Oh, yeah, yeah, at least at least for you. Being in the West Coast, you can still catch it right? Cause there's it ends up being better overlap for you than for me.
**Reese Lee** 11:14 I think it was like at one am my time, or something.
**Adriana Villela** 11:17 Oh, was it? Oh, never mind that!
Let's see, I know I have a I have a coworker who's in Brisbane, in Australia, and I think, like his time difference is ridiculous compared to mine, like my 5 Pm. Is his. 7 Am. The next day. So, like we, we have like a.
sometimes we we get to connect over zoom. But yeah, the time difference is just crazy.
Okay, well, I guess. Yeah, let's let's get on.
**Andrej** 11:49 Okay.
**Adriana Villela** 11:50 We'll start with Andre's stuff.
**Andrej** 11:52 Yep, yeah, sure. Can you hear me? Because I was trying to talk? But I was muted. But so just want to make sure.
**Adriana Villela** 11:58 Can you hear you.
**Andrej** 11:59 Wonderful. So yeah, last quarter, I participated in a Linux Foundation mentorship.
And it went pretty well. And that's basically where Victoria.
where I met Victoria, when where she started contributing to to Prometheus in a hotel as well, and I would like to do something similar again. There will be a new round of mentorships.
starting soon, I think, in August, not 100% sure, maybe in September. But the Cfps, or like call for topics, or whatever is quite soon.
I think it's in 2 weeks when the topics have to be have to be proposed, and I want to ask if you folks who have any ideas about what topics we could. We could do so previously I did something that was driven by Prometheus folks, but overlap with hotel, and now I think it like doing something like hotel, only would be also totally totally cool and interesting. So yeah, wanted to bring it up during this meeting and ask if if we have any, we have any ideas, we can go through the backlog or just brainstorm. And before we jump to the into that. I want to mention that the mentorship lasts for 3 months.
and roughly, it takes the Mentee 30 to 40 h.
working on the on the mentorship. So I think it's quite, quite a lot of effort that can go into it.
And and yeah, the the mentees are usually folks who are starting their career, or who are, I mean, like after university, or who are transitioning into into tech from from other careers. So we have folks who don't necessarily have a hold of experience, but it might be also an interesting background to work with.
So yeah, that's that's where I will stop. And I'll ask you if you folks have any ideas about what what they could work on.
Or if if you think this is, this could be interesting for for our for our group.
**Adriana Villela** 14:21 I think it could be very interesting.
And Hello, Victoria! I saw you joined, or did she?
He was.
**Reese Lee** 14:32 Yes, she's here.
**Adriana Villela** 14:33 Yeah. Okay?
Oh, yeah, yeah, that's right. Hi.
yeah, in terms. I wonder if there's something that we can do. Take advantage of of continuing the work around, streamlining the surveys, perhaps.
**Andrej** 14:56 And.
**Adriana Villela** 14:56 Funny.
**Andrej** 14:58 And and especially around like
**Adriana Villela** 15:01 Specifically around data collection and actioning.
The data that we that we collect. Because I think that that's I think that's always been one of the struggles of or I would say, one of the challenges of the sig to be able to bring the back that that feedback to the community and make sure that it's actioned effectively. And I think we've gotten better simply from even just doing the surveys. So I think this could be an opportunity for us to tweak that process a little bit more and and get a little bit deeper into into like the action.
like actioning what we've learned, basically making sure that it gets actioned on having like a follow up process. Maybe with the Sigs. Now that we have more people, I would say this was harder when there were fewer of us. But I wonder now, having more of us, and having someone like dedicated to that, maybe that could be something that could work thoughts. And and please tell me if I'm full of crap.
**Reese Lee** 16:15 I think it makes sense, and that's exactly up on Jay's Alley.
**Adriana Villela** 16:23 Right. You've created a monster.
It's a cuddler monster.
**Andrej** 16:34 Yeah, that sounds great. That sounds great.
**Adriana Villela** 16:37 Awesome.
**Andrej** 16:38 Alright. Any other ideas.
**Reese Lee** 16:41 Are there any guidelines for the topic?
I'm not very familiar with them.
**Andrej** 16:52 I? That's a good question. I don't think so. I so when I participated last time, the topic was like kind of came from the Maintainers of the Prometheus of Prometheus, and I didn't actually try to figure out like if there were any any specific requirements. But yeah, I haven't heard about this, but I can double check.
**Reese Lee** 17:21 Okay, Gotcha. So the idea for the topic is just for the mentee to have, like, a project to work on.
**Andrej** 17:31 I think so.
So with Victoria, for example.
The topic was basically just run like, do user research around the topic of promotion of resource attributes from hotel to Prometheus. And I think it was really like this. It was really this broad. And then Victoria Kinda crystallized it, or like figured out how to how she wants to approach it. Victoria, please correct me if I'm if I'm wrong.
**Victoria Nduka** 18:09 Oh, I think I don't know if I'm putting.
**Reese Lee** 18:13 Oh, she she did! A thumbs up.
**Victoria Nduka** 18:18 Oh.
my next one is over!
**Reese Lee** 18:29 Something is off with her audio or something. But she did do a thumbs up.
**Andrej** 18:34 Cool.
Yeah. So to if I would try to answer your question, then I think there are no super special guidelines. It can be quite, quite general. And, for example, the the topic that Adriana suggested sounds sounds good to me.
and I mean, like the the topic will go through the review. I believe.
**Reese Lee** 18:59 Gotcha.
**Andrej** 19:00 Whoever is in the is is reviewing. I believe they will be reviewed by somebody in the in the mentorship area.
And yeah, so I think we can be quite creative here.
**Adriana Villela** 19:18 Like, so are you? So you'll put together. Then the the proposal and.
**Andrej** 19:23 I can, I can put together a proposal. Yeah,
**Adriana Villela** 19:25 Okay? And and so if you want any of us to review, just pop a link in the in the Sig channel and and tag us.
**Andrej** 19:33 Sounds, like.
**Adriana Villela** 19:33 Be happy to do that.
**Andrej** 19:49 alrighty. So yeah, that's that's kind of it for me. If anything else comes to your mind, please let me know. And if anyone else would like to mentor. Also, I can recommend. I think it's a it's a really.
it's a lot of fun. And it's it's a nice opportunity for both mentees and mentors. So yeah, I can. I can recommend, by the way, maybe for Sophia.
this was like I in parallel, I started contributing and doing working on the mentorship. So I actually didn't have any hotel background before drink. And it was really good.
Yeah, it was a good start. It was a good start. So if you would be thinking about how to get in touch with the community better, I think this this might be a good thing to do as well.
**Sophia Solomon** 20:41 Thanks for the recommendation. Yeah, I just might.
**Andrej** 20:46 Alrighty. So yeah, that's it for me. Thanks, folks, for for your input.
**Reese Lee** 20:51 Thank you so earlier last week, or is it this week?
**Andrej** 21:08 I think it was this week.
**Reese Lee** 21:11 Dan Gomez did an Oh, tell me session with Alibaba for the Apac in the Apac time zone, and something kind of cool which I'm trying to find. So I can show you guys, is it helped increase the number of users?
**Andrej** 21:32 Okay.
**Reese Lee** 21:32 See? And I'm actually not sure where he got this graphic. But I'm gonna post it in here. Hang on one second.
Who's see?
Yeah, okay, so increase the number of members in the community group is what he said. So.
**Adriana Villela** 21:59 Well, maybe he got the stats from you know our our Cncf communities slash open telemetry.
**Reese Lee** 22:08 That page.
**Adriana Villela** 22:09 Age, the one that we use for for like promoting the Cncf events.
Yeah, that's pretty cool.
Yeah. And I think it goes to show that like we should definitely yeah, target more apac friendly stuff. And I think folks located in like Emia can probably can probably help to facilitate those, because it's less of a jarring time difference.
And actually, that reminds me, remember how you conversation with Dan.
**Reese Lee** 23:15 Yeah, I know there's a lot of contributors and people who are interested in.
you know, in Emea and Apac, and.
**Adriana Villela** 23:22 Yeah.
**Reese Lee** 23:25 Yeah. For while we did have those discussion groups in Apac, we had a couple people who were able to host I haven't seen them around in a while, but I'm sure they're still involved.
**Adriana Villela** 23:41 Yeah.
**Reese Lee** 23:42 Yeah. And I remember the apac sessions of all the ones when we did those. I think they were the most well attended. Right.
They were pretty well attended, I think. I don't recall exact numbers anymore, but.
**Adriana Villela** 23:54 Yeah.
**Andrej** 23:57 Like. What came to my mind is also that it's Alibaba, that it might be well known company that people want to learn more about. At the same time, if you folks have experience that apex sessions are in general attended more, then it might not be just about the the company itself.
**Adriana Villela** 24:14 Okay, it would definitely be worth exploring that theory to see if we can get some more Apac people.
So if anyone knows anyone any other companies.
I'll reach out to my coworker in Australia to see if he knows of anyone.
**Reese Lee** 24:44 Yeah. I'm sure we have users that are based there that we could reach out to you as well. I would just have to.
**Adriana Villela** 24:56 Yeah.
**Reese Lee** 24:56 Find out who that who those people are.
**Adriana Villela** 24:59 Yeah, yeah, I know.
Yeah, it. It was interesting when I was at Cubecon, Japan. Like they had stats that they put up on, like all the different, like so many people from Japan, like our contributors to like open source projects.
So really like it.
I I think, like between seeing that stat and then seeing how well things went for the Alibaba session. I think this could be like a you know the the incentive that we need to become more inclusive to those folks.
**Reese Lee** 25:34 Yeah. And I think that's well also keeping in mind. You know our, our, the time that we have this meeting at But I think.
**Adriana Villela** 25:45 Yeah.
**Reese Lee** 25:45 Some figs that have I'm not exactly the deal, but I know they have like an Apac. Give me a friendly time. I don't know if they like, just alternate or.
**Adriana Villela** 25:58 Have 2 instances.
This.
**Reese Lee** 25:59 Or like a different group of people meet.
**Adriana Villela** 26:01 Yeah.
**Reese Lee** 26:02 For that one, and then they like catch up Async. I'm not sure.
**Sophia Solomon** 26:05 Yeah, I think which one, this is end user developer experience does that. But the America one isn't very active.
But the email one is.
**Reese Lee** 26:22 Okay. Okay.
**Sophia Solomon** 26:23 Hmm.
**Reese Lee** 26:24 Yeah. And I think the collector Sig does as well.
yeah. I mean, I think it makes sense to see if there's anyone in the Apac region who is interested in hosting these, for you know other Apac people. And yeah, I don't know. I maybe I'll ask Dan about what the standard is for this kind of stuff. I'm sure he'll.
**Adriana Villela** 26:54 Oh, yeah, I feel like he's got the inside scoop.
**Reese Lee** 26:58 Yeah.
**Adriana Villela** 27:00 And then I guess once we get that more information, then we can. We could even put in a call on our channel and ask if anyone would be interested in hosting.
**Reese Lee** 27:13 Yeah, we could also start by reaching out to those the former hosts of the Apac discussion groups. I'll have to go back.
**Adriana Villela** 27:21 Yes, yeah. Cause it was prne right from signos.
**Reese Lee** 27:25 Yes, Prene, and I forget who the I think it was a coworker of his, but I don't remember the name.
**Adriana Villela** 27:34 Yeah, I I think I know who you're talking about. I know the name escapes me right now.
**Reese Lee** 27:40 Yeah.
**Lisa Jung** 27:43 And if I remember correctly, I think the hotel documentation is being translated into Japanese. So perhaps we can reach out to people who are doing that to see if they know anybody within the.
**Adriana Villela** 27:55 That's a good idea.
**Lisa Jung** 27:56 I'll I'll do that. Yeah.
**Adriana Villela** 27:57 Okay, that's great. That's great. I think they have sub sigs for the for the language. Translation stuff.
So try. See if you can find like the.
**Lisa Jung** 28:10 A slack Channel.
**Adriana Villela** 28:11 Japan, yeah.
**Lisa Jung** 28:12 Okay.
**Adriana Villela** 28:13 Yeah. And and if you can't, then I guess you can always default to the Com. Sig. For as a starting point.
**Lisa Jung** 28:19 So it's yeah.
**Adriana Villela** 28:20 Yes.
**Lisa Jung** 28:21 See you.
**Adriana Villela** 28:22 Since you already work with them, anyway, right.
**Lisa Jung** 28:24 Yeah.
**Adriana Villela** 28:25 Yeah.
**Lisa Jung** 28:26 Sorry. Can you guys see my dog barking?
Oh, sorry!
**Adriana Villela** 28:30 No, can't.
There! There's 1 thing that I I wanted to see. Does anyone have any other suggestions for hotel in practice or hotel. Me?
I know also, like this is a weird time of year where everyone's going on vacation.
I know in Europe a lot of people peace out in August.
North America's like here and there. July, August.
**Reese Lee** 29:16 Yeah, a lot of people, Chen.
getting ready for going back to school and stuff.
**Adriana Villela** 29:21 Oh, yeah. Oh, yeah, that's right in the States. Y'all have the weird thing of going back to school in August. So bizarre.
**Lisa Jung** 29:27 But when does.
**Adriana Villela** 29:28 Breaks, my brain.
**Lisa Jung** 29:29 Yeah.
**Adriana Villela** 29:30 We start after labor day.
**Lisa Jung** 29:32 Oh!
**Adriana Villela** 29:34 So we're off July, August, and then we start in September. So cause I think, in the States you finish Memorial Day, right? So you're like off June, July, I guess.
**Lisa Jung** 29:42 In May, like beginning of May mid, yeah.
**Adriana Villela** 29:45 Yeah, yeah, we we start, basically, we start vacations around the weekend like, coincides with Canada day, which is July first.st So.
But yeah, so but I did have a thought like.
I was thinking, like, if there are any ideas that people had that of things we can do to keep just our Sig front of mind for people so like in the past, we've done like a webinar on just doing like writing cfps. I was thinking it would be really great to do one on like how to contribute to open telemetry.
and someone suggested, I can't remember who, but it was a great suggestion to have.
like someone from the python like get some representation from various sigs. To talk about, like how to contribute to that Sig. So we can do like a panel.
and I think that's probably a little easier to coordinate than getting someone for hotel, me and and hotel and practice but if anyone has any other suggestions on.
**Andrej** 31:05 On things that we can
**Adriana Villela** 31:08 We can host.
**Reese Lee** 31:12 I think, having the commute the demo Sig demo app sig. Come on and comments street.
**Adriana Villela** 31:25 Oh!
**Reese Lee** 31:26 Think that might be pretty cool.
**Adriana Villela** 31:29 Yes, absolutely.
**Andrej** 31:36 Excellent.
**Adriana Villela** 31:44 And that's even something that we can probably between that and the how to contribute to open telemetry. That's probably something that we can run like once a quarter as a regular thing. Because, yeah, or like, yeah.
people. Oh, sorry. Go ahead. Sorry.
**Lutao Xie (Datadog)** 32:03 I. This really resonate with me because I actually like, for for someone who's like super new to like, how to contribute in, you know community projects and stuff like that.
I think a series like this, or even just how how to be part of the you know hotel community in general talk about their sigs for different topics, and how do you become a member? And all those, I think, would also be very helpful.
**Adriana Villela** 32:32 Yes.
**Lutao Xie (Datadog)** 32:33 People just who don't have, you know, dev advocacy, experience, and and like me.
**Adriana Villela** 32:40 Yeah, yeah, yeah, for sure. And we can even like, if we if we've run like the how to contribute quarter like on a quarterly basis. We can even have people from different Sigs each time talking about like we can talk about generally how to contribute. But then we can talk about. What is it like to contribute to this Sig and that Sig.
**Reese Lee** 33:03 This is what the contributor experience, Sig.
Now that we could probably collab with, I'm not.
**Adriana Villela** 33:10 Oh, yeah, perfect.
**Reese Lee** 33:12 I'm not 100% sure what their scope is.
**Lutao Xie (Datadog)** 33:19 Yeah, I'm not.
I agree with the Sophia. Because when I was like, okay, I'm gonna join a sick meeting, I'm gonna start joining a sick meeting, and then looked through the whole list.
And then I was like, Oh, my God, there are! So with you!
And then I see the end user sake. I was like, Okay, this seems a little bit more closer to the product and my function. And I'm gonna start with this one.
It was.
**Adriana Villela** 33:43 Yeah.
**Sophia Solomon** 33:44 Yeah, I totally agree. This is.
**Adriana Villela** 33:48 Yeah, yeah, we're we're a low barrier to entry, and we we roll with it.
I love it.
you know. Another thing that I was thinking of. Is we could have like a what's new with open telemetry every so often.
**Reese Lee** 34:07 That would be really fun. Austin used to do the
**Adriana Villela** 34:12 Oh, tell Tuesdays right.
**Reese Lee** 34:13 Yes, I forget it was. There was like a snazzy name, I think. But yeah. Then that ended a while ago.
**Adriana Villela** 34:23 Yeah.
**Reese Lee** 34:23 I think I'll even like once a month.
**Adriana Villela** 34:28 Yeah, exactly.
**Reese Lee** 34:30 Because I don't even.
**Adriana Villela** 34:31 I don't I?
Yeah, I I I I want to be more apprised of what's going on, and I need somebody to just shove it down my throat.
Yeah, it'd be great if.
**Reese Lee** 34:43 If we I mean, I guess this is like, you know, kind of help me, and push us to actually find out what is.
**Adriana Villela** 34:55 Totally self serving, but I I honestly think that the community would would seriously benefit from that.
I can reach out to Austin and be about coordinating that because there would be. It's almost like a community call right in some ways.
**Reese Lee** 35:15 Yeah, it could be like how you're just saying, Adriana, about how we can. What are some ways we can keep at the top of mind.
It'd be doing this like once a month.
**Adriana Villela** 35:28 Yeah.
**Reese Lee** 35:30 An idea. Andre.
**Andrej** 35:33 Yeah, I just want to mention something that we discussed during the last call or the previous one, when and I think it was something connected to what Lisa is doing about the communication stuff. That if this is something that a end user sick is is the remit of end user sick, or if it's perhaps more of a something that communication would be taking care of. And it's not because I mean about stepping on each other's toes. But I just I just remember that we had this discussion before that.
**Reese Lee** 36:07 Oh!
**Andrej** 36:08 Do you remember? I think it was about the video?
Yep, yep, created.
Yeah, yeah. Yeah.
If it should belong in one or the other. So I'm just wondering which.
**Adriana Villela** 36:18 I think, because this is about connecting end users with each other and with the with like. What's new with a project.
You can go either way.
**Lisa Jung** 36:29 I think it's most. I agree. I think it's more end user, Sig related, because this isn't strictly about how to.
**Adriana Villela** 36:37 Yeah, exactly.
**Lisa Jung** 36:38 Because how to is Comsig. And if it's more like, Hey, this is what's new. The community should know about it. I think end user. Sig is like better suited for that.
**Reese Lee** 36:48 Because more like announcements.
**Lisa Jung** 36:50 Yeah.
**Reese Lee** 36:51 M.
**Lutao Xie (Datadog)** 36:51 I I was curious like, for what's new? What are we thinking about like? Is it about, for example, the big things on the release notes or any specific milestones.
Oh, yes.
**Adriana Villela** 37:06 All of the above, I think anything, anything that.
**Lutao Xie (Datadog)** 37:09 Or tell me upcoming, or tell me, or I don't know sessions.
**Reese Lee** 37:13 I think we could also do like cause there's more and more projects that are that I've been started. That are hotel native, and I don't know is know about those either, and I think those would be interesting as well to mention, even if they're not directly like part of the open telemet project, but they you know, there was started to work natively with hotel in some capacity.
I'm trying to think of an example, but I'm spacing on the name and.
**Adriana Villela** 37:58 Sorry. Say that. Say that again. I think I caught part of that.
**Reese Lee** 38:03 Just talking about like lesser known projects that work with hotel, but that are not.
**Adriana Villela** 38:11 So.
**Reese Lee** 38:11 Directly, like, you know.
**Adriana Villela** 38:15 Like hotel adjacent.
**Reese Lee** 38:17 Yeah, so like the oh, God, what was it?
There was like a like a collector ui thing that someone just made and.
**Adriana Villela** 38:32 Oh, I see that sort of thing. Yeah, yeah.
**Reese Lee** 38:35 Yeah.
**Adriana Villela** 38:36 Yeah, like tools tools in the community. That kind of can help elevate the hotel experience.
**Reese Lee** 38:45 Oh, my God! What is it called?
It was just.
**Adriana Villela** 38:49 Like. There's so many of these things out there.
Are you thinking? Bind plane.
**Reese Lee** 38:55 No, it's something to validate your collector. Config.
**Adriana Villela** 38:59 Oh, Ollie Garden, the Ollie Garden people, right or no.
Think of something else.
**Reese Lee** 39:04 That was before. This is.
**Adriana Villela** 39:06 Oh, I think I know a little bit what you're talking.
**Reese Lee** 39:08 I think it.
**Adriana Villela** 39:09 Oh, yeah. Yeah. Yeah. Yeah. Yeah.
**Lutao Xie (Datadog)** 39:11 Or oh, oh, tell Ben!
Yes, it was hotel bin for that.
Yeah.
**Reese Lee** 39:17 Yeah, so something like this. So this is an example.
because, yeah, this is actually pretty cool.
So yeah, just an example, dash 0 actually don't really know what dash 0 it is, but they have this.
**Lutao Xie (Datadog)** 39:45 Yeah, it's it's an it's an open source tool.
**Reese Lee** 39:49 Yeah, open. Slow. Machine. Native yeah.
**Lutao Xie (Datadog)** 39:54 The Dasho itself. Oh, sorry. The hotel bin itself is a open source tool. I just don't know how open telemetry in general community guidelines in terms of promoting. Or we're using open source tool.
**Reese Lee** 40:10 Yeah, I mean, I think we just talk about the tool that's cool.
**Lutao Xie (Datadog)** 40:14 Yeah.
**Reese Lee** 40:15 Like, I don't.
Yeah, it wouldn't necessarily be promoting like, Oh, this vendor does this.
We're like, Oh, yeah.
**Adriana Villela** 40:25 And I think that's what we need to just be careful of that. We don't get into like the territory of like promoting a vendor.
**Reese Lee** 40:33 Yeah.
**Adriana Villela** 40:34 Yes.
**Reese Lee** 40:35 And I think you know, obviously, we'll put together like script or notes, so that we can all review it before we actually like do it to make sure that we stay within the standards.
But that was an example of, you know.
not just open telemetry news, but also like, Oh, did you know that there's like this open source tool.
**Adriana Villela** 41:04 Right? Yeah, yeah, that's true. I mean, cool, cool stuff the community builds around hotel.
**Reese Lee** 41:13 Yeah, and okay.
**Victoria Nduka** 41:53 Is. Is this my queue to? Are we? Are we done?
Hi! Anya.
**Reese Lee** 41:59 Oh, I think so. Did anyone else have anything to add this kind of this discussion kind of.
**Lutao Xie (Datadog)** 42:08 I'm.
**Victoria Nduka** 42:09 Okay.
**Lutao Xie (Datadog)** 42:09 I was just gonna say, I'm actually very interested in to see like what we I can contribute to what's new with hotel. I'm curious like what would be the next step, because because I could help also, like outsource, a list of things to be selected for what's new with hotel like, for example, I'm close to, let's say the new bug fixes or feature release and and all those which I'm pretty state I'm pretty like up to date with, especially on the collector side, just naturally.
**Adriana Villela** 42:44 Cool.
Yeah.
**Lutao Xie (Datadog)** 42:46 Yeah.
**Adriana Villela** 42:47 Yeah. So I mean, we can. We can look at at this potentially from a couple of angles. Cause I I reached out also to members of the Gc. To see about having, like members of the Gc. Also on to talk about what's new. But I like. But then that means having a dependence on members of the Gc.
I like this idea of actually going out and sourcing that information. So I guess we could have basically 2 types of roles around this, we have the sourcing out the information and also making sure that we have, like 2 people hosting.
Well, I guess it depends. If it's like if it's I guess we could have like one person hosting and then like, and then the other, and then having, like someone who talks about what the what's new? So having like a a host and an interviewee kind of thing, so then someone, someone from the end user Sig could could do the interview. And then we can either source someone from another sig to talk about what's new. And we can even talk about. We can do this on a Sig to Sig basis, maybe find find someone to talk about that, or, or, as you say, you can source the information you you collect collect the data, and then you can share that as well. That's another.
That's another thing. So yes, yeah, I think I think it would be fun to do it in.
**Reese Lee** 44:24 Like a different in different formats, like we could put like a fun slide deck together, and also show like little Demos and then, of course, some of the stuff will, you know, be more like announcement style, like, you know?
Maybe bug fixes or.
**Adriana Villela** 44:51 Yeah.
**Reese Lee** 44:52 New releases and then.
**Adriana Villela** 44:55 Yeah, yeah.
**Reese Lee** 44:56 I think, couple interviews or something.
And yeah, we could even do like a pre-recorded little interview if someone can't make it for some reason, or if you know zone.
**Adriana Villela** 45:13 Yeah. Great idea.
**Reese Lee** 45:16 Oh!
**Adriana Villela** 45:16 Get it.
Yeah, and then create activity.
**Reese Lee** 45:20 We can connect with Dan, who is our Governance Committee liaison, just to confirm that this is.
I don't know. Just like, Hey, this is cool right? And make sure no one else is also planning to do this because we I think we don't want to.
you know.
**Adriana Villela** 45:42 Step on toes.
**Reese Lee** 45:45 Yeah, and like, duplicate something. If someone's already doing this, or maybe we can like collaborate or something. So actually, maybe I'll just do this as like the 1st to do.
**Adriana Villela** 45:55 Yeah, I I I reached out because we have our our channel with the with the Gc and end user Sig.
that we have like for the end user Sig maintainers with the Gc liaise panel. You remember that one.
**Reese Lee** 46:11 Oh, Yes, Luta, I just.
**Adriana Villela** 46:15 So I.
**Reese Lee** 46:16 Oh, sorry!
**Adriana Villela** 46:17 Just so I just posted a thing on there to ask what people thought about it.
**Reese Lee** 46:23 Okay, perfect. And then, Luta, I just had a question in terms of formats. Would there be an option for email subscription?
**Lutao Xie (Datadog)** 46:31 It's mostly because I subscribe to Tldrma Era times, and, like found it useful.
**Reese Lee** 46:40 And Sophia.
Oh, my God, if you did a fun comic! That would be freaking. Amazing!
I'm there is also Ollie News House, and blahs puts out let's see.
**Lutao Xie (Datadog)** 47:02 We can maybe collaborate with him a little more close.
Nice. I know him Michael from aws right.
**Adriana Villela** 47:10 Yeah, that's right. That's right.
**Reese Lee** 47:13 Yeah. And he does a lot of like other project and articles.
That's cool. Yeah. So there's a lot of cool info in here, too.
And his is more, I think, like.
yeah, sharing assets from around the community.
**Adriana Villela** 47:46 Yeah, it's not necessarily. It can be articles from like the hotel blog, but it doesn't necessarily have to be.
**Reese Lee** 47:53 Yeah, I honestly haven't caught up with this in a while. There's probably lots of stuff I've list.
**Adriana Villela** 48:02 I skim it every month. I'm subscribed to it.
**Reese Lee** 48:04 Yes, and.
**Adriana Villela** 48:05 Every month, every week, and I'll I'll skim for like. Is there anything that tickles my fancy.
**Reese Lee** 48:21 But to your question, Luta, I think that would be something we want to discuss with the Gc. Cause. I know they have.
they have thoughts around email communication. Maybe if it's something like people sign up for that might be okay.
Yeah. And I think it would just depend like how much you know. Work you want to put into this and I'd be happy to help, of course.
but I think if we didn't ask something like some people can sign up for versus like, Oh, we're just gonna send this out.
That would probably be more okay than if we were like, oh, can we send this out kind of thing to the email list?
**Adriana Villela** 49:10 The. The only thing I would caution on this is, I feel like this could be overlap with the config.
So we just need to make sure we're not stepping on their toes as well.
**Reese Lee** 49:22 Yeah, so.
**Adriana Villela** 49:24 I do like the idea.
**Lutao Xie (Datadog)** 49:30 I feel like we do need to also think through like what area like, what content goes to what's new, so is there's no overlap like I can. Let me paste the example here. Content, wise like example it could be, you know, barely like Oh, my goodness!
Like it could be fairly like technical with the top news like releases.
And then specification updates like collector updates.
**Adriana Villela** 50:05 Yeah, honestly, that's the type of thing that I I was thinking for this.
**Lutao Xie (Datadog)** 50:10 Yeah, like, is this.
**Adriana Villela** 50:11 I like that.
**Lutao Xie (Datadog)** 50:12 Before or components.
**Adriana Villela** 50:15 Yeah, basically.
**Lutao Xie (Datadog)** 50:16 They like the.
**Adriana Villela** 50:17 Tldr of.
**Lutao Xie (Datadog)** 50:18 Yeah.
**Adriana Villela** 50:19 That's.
**Lutao Xie (Datadog)** 50:19 Going.
**Adriana Villela** 50:19 Going on. Yeah, yeah, exactly.
**Lutao Xie (Datadog)** 50:22 Pizza.
**Adriana Villela** 50:23 But then, as we said, we can play around with also, like elaborating on certain areas.
**Reese Lee** 50:30 Yeah. So like, because we don't. I think if we're, gonna you know, spend the time and effort to do a video, we don't want to. Just we have stuff that people can see. And you know the change log.
Yeah.
**Adriana Villela** 50:52 Yeah. But also also remember that different people consume information differently, right? Because then they're the they're going to be the docs. Readers. They're going to be the people who dig into the code. They're going to be the video people. And then they're going to be the people who are asking for the tldr of it.
**Lutao Xie (Datadog)** 51:08 Chat, gpt style, so.
**Adriana Villela** 51:11 I think catering to those different ways of consuming information, could work.
**Reese Lee** 51:17 Yeah. And I think, no, I mean, I think there's lots of different cool ways. We could make this really engaging.
So yeah, like little demos and interviews fun graphics, which of course, I am more than happy to help with.
**Adriana Villela** 51:43 Starring your cast.
Please make them include your cats.
**Reese Lee** 51:48 I can definitely include like hats.
Yeah, I think there's a lot of potential to do some really fun stuff with this.
Okay, so, Adrian, it sounds like you already posted.
Oh, why is the snow not working? Oh, okay. Here we go.
Oh, why can I do that?
**Adriana Villela** 52:35 When someone can, we have someone create an issue just to capture that as well, so that this doesn't get lost.
**Reese Lee** 52:41 My God, ducks!
Oh, great! Are you not? Gonna there we go.
Just do the community updates community updates.
This will be new issue.
**Andrej** 53:43 We have more minutes left, and I know that Victoria have a topic as well that she wanted to discuss.
**Reese Lee** 53:50 Oh, yes, yes, let's do that. I can do that after.
Thank you. Andre, yeah.
**Victoria Nduka** 53:57 Hey, please, please confirm. You can't hear me, because I don't know.
**Reese Lee** 54:03 Oh!
**Andrej** 54:04 We can hear you.
**Victoria Nduka** 54:05 Oh!
**Reese Lee** 54:13 Okay, so I can't access the link.
**Victoria Nduka** 54:21 Okay, yeah. I'll have to give you access edit access.
But I think Andre can.
But so far I think the questions are done.
And I've added the docs question the additional questions that 54 one said added, section them. So that's users who who do not have have let me see.
it's actually in a way that if a user selects an option and they don't need to answer the subsequent questions that follow.
they can just keep.
So the end of the Soviet summits.
So I think the next thing now is to send it over to the collector folks for them to review, and then we can go.
Let me see that it's critical.
I will drop a message in the slack channel.
**Reese Lee** 55:22 Okay.
**Victoria Nduka** 55:23 To let them know what your thought is, and on the subject of getting to seek top of mind for people, I just wanted to share that we're holding an event here in Nigeria. Oscar Fest is an open source event.
Think the biggest in Nigeria and and Kcd. Nigeria will also be holding alongside.
I think that's a great I'll I'll be. At events, I think it's a great opportunity for me to meet, or people contributing to the community. People have contributed to the open telemetry projects as actually intense Olympics, Olympics, Mentees.
and and get them to continue contributing to hotel if they have stopped.
or at least talk about the project. Get more books, get more people to learn about it.
So yeah, I'm going to be doing some advocacy work this week, no national tokens
**Andrej** 56:39 Sounds, great.
**Reese Lee** 56:46 Thanks for helping with that Victoria.
Alright, I guess we I guess we're good.
I will. I'll finish flushing out this issue and then share it in the channel, so people can like y'all can add comments and stuff to it.
**Adriana Villela** 57:17 I'm spoiled.
**Reese Lee** 57:21 And cool beans. Good meeting, you guys.
**Adriana Villela** 57:26 Yeah. Super productive. Meeting.
**Reese Lee** 57:29 I know I'm so excited that y'all are here.
I feel like this is one of the biggest goose you've had on a call, and it was. I know.
**Adriana Villela** 57:40 Oh.
yeah, and and actually like people interacting because we we have had, like, you know, which was which is super fair people, just like listening in.
**Reese Lee** 57:49 Yeah, the name like, drop in, and then we wouldn't see them again.
**Adriana Villela** 57:55 So we appreciate y'all.
**Reese Lee** 57:57 Yes, thank you.
**Sophia Solomon** 57:58 Be here!
**Adriana Villela** 58:00 A.
**Lutao Xie (Datadog)** 58:01 I have been struggling a little bit to see how I can contribute. So if anything. Yeah.
I'm here also learning.
**Adriana Villela** 58:10 I think this like community, like what's new thing, could be a really great opportunity to.
**Lutao Xie (Datadog)** 58:16 Like, yeah.
**Adriana Villela** 58:16 Yeah, yeah, yeah.
**Sophia Solomon** 58:18 Yeah. And I'd love to help just Fyi, just.
**Adriana Villela** 58:21 Same.
Yeah. And and you know, like, whenever we do these things like just having like rotating amongst people like hosting, hosting these.
as I think a great opportunity, like Andre and and Victoria have been awesome co-hosts. For like oh, tell me, in the recent for a couple of our recent events. And now, now that you've got your feet wet, you can like probably host, your own so like, I think there's plenty of opportunities for various people to like run like run with a planning host. The events, like definitely tons of ways to contribute. When we, when we organize these.
**Reese Lee** 59:02 Yeah. And if you think of, you know an idea that you're interested, definitely mention it. And, Sophia, if you're not already in the end users like slack channel. You can join I'll just pop this link to our.
**Sophia Solomon** 59:20 I think I.
**Reese Lee** 59:22 Bucks.
**Sophia Solomon** 59:22 Am in it also. Sick. Yeah.
**Adriana Villela** 59:25 Yay!
**Sophia Solomon** 59:27 Dance that I can't make this.
He's a call today. Okay, yeah.
**Adriana Villela** 59:31 Awesome.
**Reese Lee** 59:32 Well have a wonderful day. Y'all.
**Adriana Villela** 59:35 Yeah. See? You see, you next time I probably won't see you the next meeting, because I'll be on vacation in 2 weeks. So.
**Reese Lee** 59:43 Chilly.
Okay. Awesome.
**Sophia Solomon** 59:47 Nice meeting!
**Adriana Villela** 59:50 Bye.
**Victoria Nduka** 59:52 Bye.
