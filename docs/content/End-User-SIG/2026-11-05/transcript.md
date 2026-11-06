SIG: End-User SIG
Date: 2026-11-05
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Atil Sensalduz** 00:18 Hi, Vidhya.
**Vidhya Divakar** 00:21 Bye.
**Atil Sensalduz** 00:21 Who am I?
**Vidhya Divakar** 00:22 How are you?
**Atil Sensalduz** 00:23 Hi, I'm doing good here.
**Vidhya Divakar** 00:25 Yeah, good.
So, So, yeah, I think it was the first time, I'm meeting you. Yeah, so I…
**Atil Sensalduz** 00:37 is…
**Vidhya Divakar** 00:38 I recently started contributing, like, like, I think since 2025 with Open Elementary.
**Atil Sensalduz** 00:49 It's quite easy. We opened the PR for reference implementation, and then invited us for discussing it.
**Vidhya Divakar** 00:57 Oh, yeah.
**Atil Sensalduz** 00:58 Okay.
**Vidhya Divakar** 01:00 Hi, I'm… Adriana?
**Adriana Villela (Dynatrace LLC)** 01:07 we're gone.
**Atil Sensalduz** 01:12 Adriana?
**Vidhya Divakar** 01:13 And Gianna, okay.
**Adriana Villela (Dynatrace LLC)** 01:16 Adriana.
**Vidhya Divakar** 01:18 Adriana, okay, hi, Adriana.
**Adriana Villela (Dynatrace LLC)** 01:20 Hi, hi.
**Vidhya Divakar** 01:21 Nice to,
**Adriana Villela (Dynatrace LLC)** 01:22 Nice to friendly, meet in person. E-meet you.
**Vidhya Divakar** 01:27 Thanks for joining today.
**Adriana Villela (Dynatrace LLC)** 01:29 Yeah, is anyone else on the call?
**Vidhya Divakar** 01:32 Not yet, maybe, like, maybe a couple of minutes.
**Adriana Villela (Dynatrace LLC)** 01:35 Gonna… I'm gonna poke a few people. I know Reese just got back from a trip.
**Vidhya Divakar** 01:43 Sure.
Hi, Sophia.
**Sophia Solomon** 02:03 Hi! Hi, everybody!
**Adriana Villela (Dynatrace LLC)** 02:04 Yay! How's it going?
**Sophia Solomon** 02:07 Going good, it's going good. Apparently, one of the people we tapped for… Hi, Andre! One of the people we tapped for Humans of Votel is no longer attending, so…
**Adriana Villela (Dynatrace LLC)** 02:18 Bummer.
**Sophia Solomon** 02:19 Yeah, I need to find… A couple more people covering.
**Dan Gomez Blanco (New Relic, Inc.)** 02:23 Hey,
**Adriana Villela (Dynatrace LLC)** 02:26 Hey, Dan!
**Atil Sensalduz** 02:27 It does.
**Adriana Villela (Dynatrace LLC)** 02:27 you.
Andre?
Nice to see you.
**Andrej Kiripolsky** 02:38 Everyone, hello.
**Adriana Villela (Dynatrace LLC)** 02:40 Just poking, reese to see if she's joining. I know she just got back from a trip.
Very short trip across the continent.
Oh yeah, she texted me saying she's on her way.
**Dan Gomez Blanco (New Relic, Inc.)** 02:55 Cook.
Might not be able to stay for the whole meeting, but
**Adriana Villela (Dynatrace LLC)** 03:13 Does anyone have an agenda handy?
**Andrej Kiripolsky** 03:18 Yeah, I have it opened. We have really just one thing there at the moment, but I'm pretty sure there will be more topics.
**Adriana Villela (Dynatrace LLC)** 03:24 Yeah, yeah. Do you mind giving it a share if you haven't already?
Hey, Reese!
**Andrej Kiripolsky** 03:31 I'll drop here to the chat.
**Reese Lee (New Relic, Inc.)** 03:33 Hey, everybody!
I'm just finishing up a banana real quick, and then I'll come off camera. Come on camera.
**Sophia Solomon** 03:43 I get it.
**Dan Gomez Blanco (New Relic, Inc.)** 03:45 Oh, by the way…
**Adriana Villela (Dynatrace LLC)** 03:46 Sing lunch.
**Dan Gomez Blanco (New Relic, Inc.)** 03:47 I was gonna ask, Adriana and I met with, Abby Bankser at the KCD UK, and she mentioned that You had been in touch with her about Humans of Hotel, or something like that, Sophia?
**Sophia Solomon** 04:00 Who? Abby?
**Adriana Villela (Dynatrace LLC)** 04:02 Wait, did we… did we talk to Abby about Humans in Votel?
**Dan Gomez Blanco (New Relic, Inc.)** 04:05 I think she mentioned that, maybe she mentioned that to me. You were around.
Okay, okay. Oh. I know that you were…
**Adriana Villela (Dynatrace LLC)** 04:11 I was involved in OTEL, though.
**Dan Gomez Blanco (New Relic, Inc.)** 04:13 No, but that's what I mean, it's like, then I was thinking, well, it would be awesome if people from the… because I've been talking to them about the, you know, the platform engineering community.
And I think there is a lot of… You know, over the, sort of, like, the, the, the intersection between platform engineering and hotel, right?
So if we have any folks from… from that community to… say a few words about… if you are involved in a hotel, right? To say…
**Adriana Villela (Dynatrace LLC)** 04:40 idea.
**Dan Gomez Blanco (New Relic, Inc.)** 04:41 It's about a hotel, that would be awesome.
**Sophia Solomon** 04:44 Yeah, no, that would be nice. Yeah, I have been in touch with… I forgot what her name was. I was in touch with Jamie, Danielson, about all of this.
**Dan Gomez Blanco (New Relic, Inc.)** 04:53 Oh, cool.
**Sophia Solomon** 04:53 But,
**Adriana Villela (Dynatrace LLC)** 04:54 I thought we had Jamie before, no?
**Sophia Solomon** 04:56 We have, we have, we have, yeah, but we're just talking about potential people, but,
**Adriana Villela (Dynatrace LLC)** 05:01 Gotcha.
**Sophia Solomon** 05:02 Who is Abby? I know that, amy's not coming… And… Andy is good. I've tapped Tyler… Hellman… And… What's that other guy? What's his name?
Austin Parker.
So, I've tapped those guys.
But Philly, you're not coming.
**Adriana Villela (Dynatrace LLC)** 05:27 For one of our early ones, didn't we?
**Sophia Solomon** 05:30 Oh, no.
I'm trying to remember now.
**Adriana Villela (Dynatrace LLC)** 05:34 I'm trying to remember, I… it's very possible, I'm just… My memory might be faulty,
**Reese Lee (New Relic, Inc.)** 05:41 You know, I'm not…
**Adriana Villela (Dynatrace LLC)** 05:42 If not, if, if not, then it would be awesome, because I…
**Sophia Solomon** 05:45 Oh, nice.
**Adriana Villela (Dynatrace LLC)** 05:46 Seems like an obvious…
**Reese Lee (New Relic, Inc.)** 05:48 I don't know that we've ever had him as, a Humans of Atil. We might have, but I know for sure that they were doing a lot of livestreams for this.
**Sophia Solomon** 05:57 Oh, yeah, I see Liza.
**Adriana Villela (Dynatrace LLC)** 05:58 Yeah, yeah, yeah.
**Sophia Solomon** 05:59 But I didn't see individual interviews, but…
**Adriana Villela (Dynatrace LLC)** 06:02 Okay, okay.
**Dan Gomez Blanco (New Relic, Inc.)** 06:03 When we found out… this is when we find out that Austin is not human.
**Reese Lee (New Relic, Inc.)** 06:06 Absolutely.
**Dan Gomez Blanco (New Relic, Inc.)** 06:09 Not a human voter. He's everywhere, but he's not. He's just AI agents.
**Reese Lee (New Relic, Inc.)** 06:15 No.
**Adriana Villela (Dynatrace LLC)** 06:15 Yeah, that's true, that's true.
**Dan Gomez Blanco (New Relic, Inc.)** 06:22 But yeah, I mean, if he's not been, then of course.
**Adriana Villela (Dynatrace LLC)** 06:25 Yeah, I know, right?
**Dan Gomez Blanco (New Relic, Inc.)** 06:26 I think I've been in the… in one of… a couple of years ago, so…
**Adriana Villela (Dynatrace LLC)** 06:28 I feel like you were, yeah.
**Dan Gomez Blanco (New Relic, Inc.)** 06:30 Yeah.
**Adriana Villela (Dynatrace LLC)** 06:31 We need, like, a list, like, in one place, unless we already have one. I'm just going by, like, the old blog posts and stuff.
**Sophia Solomon** 06:41 Yeah, I just type in the person's name, and then Humans of Otel.
**Adriana Villela (Dynatrace LLC)** 06:45 Oh, yeah, yeah, yeah, that's…
**Sophia Solomon** 06:46 He's not smart.
**Adriana Villela (Dynatrace LLC)** 06:47 That's smart. Get Claude to compile a list based on, like, the humans of Votel blog posts. There you go. Good use of AI.
**Dan Gomez Blanco (New Relic, Inc.)** 06:55 Well, there is… there will be, I don't know if we get that… as a project, I'm pretty sure we don't.
I know that, you know, if you're a sponsor, you get a list of companies that are attending.
**Adriana Villela (Dynatrace LLC)** 07:06 Oh, man.
**Dan Gomez Blanco (New Relic, Inc.)** 07:07 So maybe that's, something for… maybe we can do it with the… with a list of speakers, and see who is… Because sometimes you don't know who's the attendant, right? So if we get the.
**Adriana Villela (Dynatrace LLC)** 07:17 Yeah, it's true.
**Dan Gomez Blanco (New Relic, Inc.)** 07:19 And then… Cross-check that with a list of contributors.
Toddale. Now we can say, okay, this person… That Tolkien also is an hotel contributor, and we can reach out.
**Sophia Solomon** 07:33 It would be good.
**Adriana Villela (Dynatrace LLC)** 07:35 And let's… let's try to make sure we get some girls.
It's always challenging.
**Sophia Solomon** 07:41 Yeah, no, that's what the hard part was. I was speaking with, I was speaking with Jamie Danielson, and she was like, All of the girls have already been interviewed.
**Adriana Villela (Dynatrace LLC)** 07:54 I know!
**Reese Lee (New Relic, Inc.)** 07:55 I feel like.
**Adriana Villela (Dynatrace LLC)** 07:55 We've tapped all the…
**Reese Lee (New Relic, Inc.)** 07:57 Oh, no.
**Adriana Villela (Dynatrace LLC)** 07:57 80s! Sophia.
**Reese Lee (New Relic, Inc.)** 07:59 Yeah, I… I… Hannah Ramadan?
Yeah, because I think we've done… we've interviewed Kayla before, but Hannah, this is gonna be her first time at KubeCon, so…
**Adriana Villela (Dynatrace LLC)** 08:13 Yay.
**Sophia Solomon** 08:15 Okay.
Hannah, Hannah…
**Reese Lee (New Relic, Inc.)** 08:18 Dang, can't believe I just didn't think of her sooner.
**Sophia Solomon** 08:21 Okay, I see. Hannah Robinson. Okay, let me tap her, too. Thank you.
**Reese Lee (New Relic, Inc.)** 08:24 She's on the Ruby SIG.
**Sophia Solomon** 08:26 Awesome.
The count has gone back up.
**Adriana Villela (Dynatrace LLC)** 08:40 Yeah, I was like…
**Dan Gomez Blanco (New Relic, Inc.)** 08:41 Thank you.
**Adriana Villela (Dynatrace LLC)** 08:41 Oh, it's too bad Amy can't come.
**Dan Gomez Blanco (New Relic, Inc.)** 08:43 about this, and I know that, you know, this is probably from the APAC meeting as well. Yoshi was asked… well, Yoshi's got the video ready for editing, right?
Do we know who's got any time and scales for editing video?
That could help to edit that.
**Reese Lee (New Relic, Inc.)** 09:01 feet.
**Dan Gomez Blanco (New Relic, Inc.)** 09:01 Already, do we have a.
**Andrej Kiripolsky** 09:03 And…
**Dan Gomez Blanco (New Relic, Inc.)** 09:04 It can kind of.
**Andrej Kiripolsky** 09:04 I think we have an update on this, so Sophia actually did the editing there.
Already, and thanks a lot for that, Sophia. And please, like.
feel free to give them yourself just… but there is one more thing, so I, we didn't have a proper meeting yesterday, but Yoshi mentioned already before that we'll need to just upload them to YouTube.
And he doesn't know how to do it, and I didn't… couldn't help either, so in case you folks can help with loading the videos to YouTube, that would be…
**Adriana Villela (Dynatrace LLC)** 09:34 Yeah, I have YouTube uploading powers.
**Sophia Solomon** 09:38 Okay. Are we gonna say…
**Adriana Villela (Dynatrace LLC)** 09:39 If you, if you just ping me with…
**Sophia Solomon** 09:41 you.
**Adriana Villela (Dynatrace LLC)** 09:41 info, yeah, yeah.
Yeah, make sure… because these are shorts, right?
**Andrej Kiripolsky** 09:47 Yep.
**Adriana Villela (Dynatrace LLC)** 09:48 Okay, perfect. Yeah, so let's… Song and dance.
**Sophia Solomon** 09:53 They should have the right dimensions for YouTube and everything, for the short.
Leo.
working with Japanese was just… Oh my gosh, yeah.
It's a beautiful language. It was just hard, as an American.
**Vidhya Divakar** 10:12 This CubeNob is, is this weekend, right?
**Adriana Villela (Dynatrace LLC)** 10:18 Connor's next week.
**Vidhya Divakar** 10:19 on. Next.
**Adriana Villela (Dynatrace LLC)** 10:20 Next week.
**Vidhya Divakar** 10:20 So you guys are, like, I mean, all going, or is it, like, virtual? You cannot join even virtually?
**Dan Gomez Blanco (New Relic, Inc.)** 10:28 I know they've had…
**Adriana Villela (Dynatrace LLC)** 10:30 virtually in the past, but I don't know, but in recent… Recent past.
**Sophia Solomon** 10:35 Yeah, I think they record the… the talks.
**Adriana Villela (Dynatrace LLC)** 10:38 Yeah, that's true, that's…
**Vidhya Divakar** 10:41 Okay. And there are CubeCons.
**Adriana Villela (Dynatrace LLC)** 10:43 throughout the world now, so there's KubeCon North America, there's KubeCon Europe in Barcelona, they… and then recently they've done a KubeCon India and KubeCon Japan, so…
**Vidhya Divakar** 10:55 Okay, so I think, last year we did Atlanta, right? I'm currently in Atlanta, so… Okay, okay.
**Adriana Villela (Dynatrace LLC)** 11:04 And, and so you just… you just missed it in your hometown.
**Vidhya Divakar** 11:07 By her!
Yeah, I don't understand.
Yeah, look out for these recordings if they're available.
**Adriana Villela (Dynatrace LLC)** 11:19 Yeah, and, and maybe, maybe, beg to go to KubeCon Barcelona.
**Andrej Kiripolsky** 11:29 Yeah, they're just selling the tickets now, and you can still…
**Adriana Villela (Dynatrace LLC)** 11:32 They are, actually.
**Andrej Kiripolsky** 11:33 That's, that's like…
**Adriana Villela (Dynatrace LLC)** 11:34 No!
**Andrej Kiripolsky** 11:36 There we go.
It's a really nice event, and So when I was on KubeCon for the first time, a couple of years ago.
I was very overwhelmed, like, a lot of strangers and, like, a lot of things happening, but… That was before my OpenTelemetry time, and now the most recent one in Amsterdam was actually very, very nice. Also a lot of people, but also, like, but the main impression for me was that there was a lot of familiar people, and it was great to just catch up, and I think I saw, like.
many of folks from the call now, and yeah, it was really, really nice. So, definitely, in case you want to contribute to this community and be part of it, I think KubeCons are one of those conferences that are worth Joining.
**Vidhya Divakar** 12:24 Yeah, sure.
**Adriana Villela (Dynatrace LLC)** 12:26 Definitely.
Yeah, as Andrej said, it's, like, overwhelming as hell.
**Vidhya Divakar** 12:39 And Andrej, you have shared a doc,
**Andrej Kiripolsky** 12:49 The agenda doc? Yeah, I shared it here in the chat, or do you need…
**Vidhya Divakar** 12:53 Damn.
**Andrej Kiripolsky** 12:54 Yeah.
**Vidhya Divakar** 12:56 And, yeah, and, Dan, actually, we were talking about the hotel, right? I and Adriana were, like, working with this, Duh.
Or tell me, discussion guide.
So, I just want to know, like, since we planned this for December, do we have to… when do we have to start the promotions and things like that?
**Adriana Villela (Dynatrace LLC)** 13:23 I mean, so when in December did you say it was?
**Vidhya Divakar** 13:28 We didn't plan a date yet.
**Adriana Villela (Dynatrace LLC)** 13:30 Oh, okay. Usually, like, 2 weeks before?
**Vidhya Divakar** 13:34 No.
**Adriana Villela (Dynatrace LLC)** 13:34 The three weeks before we promote.
**Vidhya Divakar** 13:36 Okay.
**Adriana Villela (Dynatrace LLC)** 13:37 I would say.
We've done it very last minute. It's not ideal to do it last minute, but… so two to three weeks is the sweet spot.
**Vidhya Divakar** 13:45 Okay.
Yeah, yeah, yeah, sure. I think, yeah, we… you… I mean, the next week you have… you have work, so I think it's too early to talk about this, right?
**Dan Gomez Blanco (New Relic, Inc.)** 13:57 Yes, yeah, so after KubeCon…
**Vidhya Divakar** 14:01 Yeah, yeah, I understand.
**Dan Gomez Blanco (New Relic, Inc.)** 14:03 Well, actually, after KubeCon, I'm gonna be on PTO for a couple of weeks.
Okay.
**Adriana Villela (Dynatrace LLC)** 14:09 Get over KubeCon. Yeah.
**Dan Gomez Blanco (New Relic, Inc.)** 14:12 I just wanted to call my… I normally get ill, so I just, like, this time, I got all the vaccinations, I'm ready.
But, but,
**Vidhya Divakar** 14:22 Obviously, it's holiday season too, right? Yeah.
**Dan Gomez Blanco (New Relic, Inc.)** 14:26 So, yeah, so I think, you know, let's see… I mean, I can… we can try to get the date… planned, maybe, like, mid-December, that would probably be… And that will give us some time to, like, plan it.
**Vidhya Divakar** 14:40 I know.
**Dan Gomez Blanco (New Relic, Inc.)** 14:40 with them. I don't know if… by the way, I don't know if that is the… maybe that's one of the things that we need to discuss.
Is the, the, the schedule. I'm not sure if there are any other sessions… We have the… by the way, I… I posted that… Roadmap… thing in the contributor's channel, that sort of project. Got your message, Vidya, that is, You see it as private, because at the moment, you can only see it If you're a member of the OpenTelemetry org.
**Vidhya Divakar** 15:16 Okay. Not ideal.
**Dan Gomez Blanco (New Relic, Inc.)** 15:18 Ideally, this should be public. The problem is that it's got a date, that is a… it's got a start date field that basically tells you, for every issue, you can assign, a start date, or a target date, or a target date field. And that's, for some reason, that became a restricted field. So any board in OpenTelemetry in the project that has a target date or a start date.
as a field, it will be only private to the repo. Even if it's marked public, it will be… not visible by others, and I've got that in my to-do list to erase it with, with the powers that be, I think at the moment is the infrastructure SIG that contains… that controls that, to change that, so that we can actually share that publicly. Ideally, we should have that as a public… As a public port.
**Vidhya Divakar** 16:06 Yeah, because it'll be nice to see all the… all the things in a single place.
**Dan Gomez Blanco (New Relic, Inc.)** 16:11 Yeah, because they're tentative dates, right? We can put their tentative dates, rather than… yeah, and then we can start to… to align them. They don't have to be final dates for us to be putting there, as opposed to, you know, we actually plan it, and it goes into OpenTelemetry Live, and, you know, then that is a firm date.
But, yeah, so I don't know if we've got anything else in the pipeline at the moment, Sophia… Victoria's not here, but, like.
She mentioned that we had something… For Hotel in Practice, I believe?
**Vidhya Divakar** 16:41 Yeah, I think there's, one in November 25th, they have Plan 1.
**Dan Gomez Blanco (New Relic, Inc.)** 16:46 Alright, so if someone can go to the… to the channel, the contributor's channel, there's a link there. You should be able to… Let me see if I can bring it up.
Let me just quickly share my screen.
Cool. Yeah, so I just put in there the ones that are… so if you add a new Autumn in practice, or… So they're tagged here, right? So we've got some… Hotel in practice, or tell me.
If you create a new one through the issues, it will have this label automatically.
And then, it will appear here.
If we have any dates for this that we can put in here, which is, like, add it there, I think for Adobe, I don't know, we might be looking at… Somewhere, like…
**Vidhya Divakar** 17:54 Wednesday.
**Dan Gomez Blanco (New Relic, Inc.)** 17:54 December the 16th, maybe that's a bit too far.
Maybe… December 9th.
On a Thursday. Do we normally do that on a Wednesday or a Thursday?
Can't remember.
**Sophia Solomon** 18:06 Just depends on the person.
**Dan Gomez Blanco (New Relic, Inc.)** 18:08 Depends on the person, right? Okay, so whenever we… if we've got any dates for any of these, then… Should probably…
**Sophia Solomon** 18:15 Not so far, but I'll go with Victoria, and we'll start… Planning them out for the rest of the year than going into next year.
**Adriana Villela (Dynatrace LLC)** 18:26 Yeah, I think realistically, as long as you do it on a Tuesday, Wednesday, Thursday, it doesn't really matter, and then make sure you book, ahead of, like, the day… a few days before, like, the tech check.
Yeah. With folks.
**Vidhya Divakar** 18:39 Okay, yep.
**Dan Gomez Blanco (New Relic, Inc.)** 18:43 Good.
Right.
Okay, so I'll stop sharing.
**Vidhya Divakar** 18:51 Yeah, sure, thanks.
**Dan Gomez Blanco (New Relic, Inc.)** 18:53 Yeah, so… so far, I guess we don't really have any… any… other dates, but yeah, let's think about somewhere, early December.
**Andrej Kiripolsky** 19:06 Hint.
And there are no more… agenda items so far, but I see that we have… we have some, new… faces here, and also, Atil, you just unmuted yourself, so please, go ahead.
**Atil Sensalduz** 19:18 Thank you so much. Actually, we included the PR, about the reference implementation, and Dan invites us for the Blueprints meeting, but we missed Dan.
So I joined this one, End-User, but it might be… wrong one for discussing TPRs.
I'm not sure, should I attend the blueprint meeting, or can we discuss it in… Is that this one, I-shaped, chat.
**Dan Gomez Blanco (New Relic, Inc.)** 19:49 tube.
**Atil Sensalduz** 19:49 Reference implementation.
from our company, Akbank, and…
**Adriana Villela (Dynatrace LLC)** 19:57 That feels more like a blueprint thing.
**Dan Gomez Blanco (New Relic, Inc.)** 20:00 Yeah, so we talked about it in the, in the Blueprints meeting, when, what was it? Like, last two… last Monday? The Monday before? Yeah, so it was the Monday before.
This is… yeah, so we have it… I think, you… yeah. Johanna has provided some feedback, yeah.
**Atil Sensalduz** 20:22 it…
**Dan Gomez Blanco (New Relic, Inc.)** 20:26 I guess, you know, it's… it's… this is basically what I was, I was mentioning, it's probably everyone's now very busy with KubeCon, which is the reality.
**Atil Sensalduz** 20:39 Dave.
**Dan Gomez Blanco (New Relic, Inc.)** 20:40 But it is in… you know, we discussed this in particular in the last Blueprints meeting. If you go to the… you can get the transcripts from the… from the meetings, if you want to see what we talked about. We didn't go into details of it, just that the fact that Johanna was, had already given some comments, and I see that you've responded.
Yeah, it's… we… thank you so much, first, for… for contributing that.
Ideally, we'll get to that after, you know, we'll probably get to that after KubeCon. We have, the meeting next Monday, we'll have to cancel it, because every one of the… of the approvers and blueprints will be at KubeCon, so we're gonna have to cancel that meeting, unfortunately. But,
**Atil Sensalduz** 21:26 Interesting.
**Dan Gomez Blanco (New Relic, Inc.)** 21:27 But we will… we will get to it, and then start to provide feedback when I…
**Atil Sensalduz** 21:33 Alright, thanks very much.
**Dan Gomez Blanco (New Relic, Inc.)** 21:34 No worries at all. Thanks for… thanks for sharing that.
As a matter of, like.
And one of the things I wanted to get as well, if you… maybe we can talk about this in the blueprints.
Meeting, later.
If you have any feedback on the contribution process, or… The, you know, if you find the template was too much, too little, the guidelines that come with the template as well.
You know, if it's… if you have any feedback on the contribution process, then, yeah, we'd love to hear it.
If you can give it to us in the Auto Blueprints.
Channel, if you're not there already.
**Atil Sensalduz** 22:16 Yeah, it should actually… my co-worker agreed that PR and through the process, so I will ask to him, and then I get feedback from him about the process, and then I will provide the info at the next Blueprint Meetings I will attend.
**Dan Gomez Blanco (New Relic, Inc.)** 22:33 Nice. We've got a couple in progress, for reference implementations, but just to give you an idea as well, we are going through the backlog of, the developer experience SIG, did some interviews with, 5 companies.
our Adobe… Mastodon, Skyscanner, Key Cloak, and Atlassian?
So, those 5 took, sort of, priority, and then KeyCloak was just published yesterday, or the date… no, last week.
**Atil Sensalduz** 23:03 Good.
Yeah, it's sweet.
**Dan Gomez Blanco (New Relic, Inc.)** 23:07 Yeah, so that's good.
**Atil Sensalduz** 23:08 Okay.
**Dan Gomez Blanco (New Relic, Inc.)** 23:09 OCM, we're just waiting for…
**Vidhya Divakar** 23:11 Yeah, I mean… Good evening.
**Dan Gomez Blanco (New Relic, Inc.)** 23:12 on their side.
**Vidhya Divakar** 23:12 the last review to be done, because folks are busy with KubeCon.
**Dan Gomez Blanco (New Relic, Inc.)** 23:18 Oh, you, of course, you were involved, you were…
**Vidhya Divakar** 23:20 Yeah, I wrote it.
**Dan Gomez Blanco (New Relic, Inc.)** 23:21 God.
**Vidhya Divakar** 23:21 So, just waiting for the last moment.
**Dan Gomez Blanco (New Relic, Inc.)** 23:25 I know that we probably spoke in a thread, I just didn't associate, like.
**Vidhya Divakar** 23:28 Yeah, I've been talking with Juliano regarding that, yeah.
**Dan Gomez Blanco (New Relic, Inc.)** 23:33 Yeah, yeah, cool, awesome. So I guess Platinum, which is waiting on them to approve, right?
**Vidhya Divakar** 23:39 Yeah.
**Dan Gomez Blanco (New Relic, Inc.)** 23:41 And and then basically what you're doing now, Atil, is that we will… You're basically joining the new contribution format, which is through the end-user SIG.
with a template, with, you know, a bit more self-serve. We can still help people if they don't have any technical writing skills.
But, but yeah, so if you're… It seems like, you know, you've already… done a good job with it. So, so yeah, so, I think the, it's just a matter of going through that review list.
**Atil Sensalduz** 24:20 Hey, thanks so much, Ben.
**Vidhya Divakar** 24:25 And, Dan, also, I want to ask you, like, if there's any, contribution that I can do for this KubeCon, anything is outstanding, or do you need help?
Anything like that?
**Dan Gomez Blanco (New Relic, Inc.)** 24:41 Don't sure… Apart from, like, I was gonna say, if, I asked this question as well in the channel, if anyone's going to be… At KubeCon, we can do an End-User SIG office hours, M… But I just wanted to get… an idea of who's, who's, who's around, and and you need to… that's on-site, right?
**Vidhya Divakar** 25:08 Yeah, that's right, yeah.
**Dan Gomez Blanco (New Relic, Inc.)** 25:10 Who's around, and who is going to be, what are the schedules looking like?
**Vidhya Divakar** 25:14 Okay. So, yeah. Yeah, I saw the list.
**Dan Gomez Blanco (New Relic, Inc.)** 25:23 But apart from that, I'm not sure if… I'm assuming that for KubeCon, from the end-user's sake, we do the… Just correct me if I'm wrong here, like any other maintainer.
But we do the Humans of Full Tail.
Stuff?
Do we do a… at life… like, OpenTelemetry Live from KubeCon thing.
**Adriana Villela (Dynatrace LLC)** 25:45 Yeah, Henrik was asking about booking that, actually.
And then, the other thing that we do is, is, coordinate with the maintainers to schedule SIG meetings.
On-site.
**Vidhya Divakar** 25:59 Don't think…
**Adriana Villela (Dynatrace LLC)** 26:00 Yeah.
Before we continue, since we've got a couple new faces, should we do intros?
**Dan Gomez Blanco (New Relic, Inc.)** 26:08 Yeah.
**Vidhya Divakar** 26:13 Yeah, I can go ahead.
So, basically, I have, like.
I am an engineer in electronics and communication.
So, I have, like, 8, 9 years of experience in, software documentation.
So, so currently in Atlanta. So I always, I would want to volunteer. I have done some proton types, there was another company which I was volunteering, and right now, this telemetry, I am interested in telemetry, so I thought… I'll give some time for that, and also, I do, agile delivery stuff. So, Since I have some time, I do freelancing, so since I have some time, so I thought I'll contribute up into elementary. So that's a little bit about me.
So right now, I'm in Atlanta, Georgia.
**Andrej Kiripolsky** 27:05 Cool. I can go next.
**Vidhya Divakar** 27:07 Nice meeting you guys.
**Andrej Kiripolsky** 27:10 Nice to meet you, and actually, like, we've been in touch with Vidya for a while.
**Vidhya Divakar** 27:14 I started in 2025, or maybe end of 2024.
**Andrej Kiripolsky** 27:19 Yeah, yeah, I know you, you're…
**Vidhya Divakar** 27:21 I've not attended meetings, but I've been there.
**Andrej Kiripolsky** 27:27 Yeah, yeah. So, my name is Andrej, I'm a user researcher at Grafana Labs, and I'm a maintainer at End-User SIG here, and I'm based in Czech Republic.
In… in Brno, and Yeah, here in the End-User SIG, I… do mostly… or, like, primarily focus on surveys, but I was terrible at it in the past, year, so I will… I will get better, but that's… I think that's… that's about it.
From me.
I wanna go next?
**Reese Lee (New Relic, Inc.)** 28:06 I'll go next, real quick. Hi everybody, I'm Reese. I've been involved with the EndUIG since the early, early days.
And now along with Adriana, I'm one of the OTL community managers. I also work on New Relic, along with Dan.
**Dan Gomez Blanco (New Relic, Inc.)** 28:24 Is that… that's it? Yeah, so I'm Dan. I've been, as well here since the beginning.
Of End-User SIG before it was a SIG, I guess, yeah? And, I… Yeah, I felt so… been a bit more work on the end-user SIG with hotel blueprints and reference, implementations.
And, since recently, I'm also part of a governance committee, which would probably mean that I… Have to dedicate less time to other things, but hopefully for a good reason.
I'll pass on to Sophia, that's on my next, next to me on the screen.
**Adriana Villela (Dynatrace LLC)** 29:02 Oh, and Dan, don't forget to mention you're our liaison, too, for the GC.
**Dan Gomez Blanco (New Relic, Inc.)** 29:06 Oh, yes, correct, yeah.
**Sophia Solomon** 29:07 Thank you.
**Dan Gomez Blanco (New Relic, Inc.)** 29:08 Yeah, so I'm the liaison for the GC liaison for the SIG, so if you find any issues in terms of, well, anything that you want to escalate, and that could be, nice things, or it could be bad things, like code of conduct and whatever, I'm here to… to help.
Hopefully it's all nice things.
**Sophia Solomon** 29:28 Okay, I'll take the… I'll take the popcorn. Hi everybody, I'm Sophia.
I am a developer advocate at Elastic, and yeah, I'm a maintainer and the End-User SIG. I like editing video, and I like doing creative stuff, so if you need anything creatively done, please Hit me up. And of course, there's a bunch of creative people in this SIG. It's the most creative SIG, IMHO. But yeah, welcome in. Glad to have you.
I'll pass it.
**Adriana Villela (Dynatrace LLC)** 29:59 I will vouch, I'll vouch for Sophia's amazing skills.
In creativity, Super Baller.
Between Sophia and Reese, I think, like, we've got… top-notch creativity, so…
**Autumn Capasso** 30:14 glasses, they're so cute.
**Sophia Solomon** 30:17 Thank you.
**Adriana Villela (Dynatrace LLC)** 30:18 Hey, I'm… I'm Adriana, with Reese Sweeping… SIG since the beginning of the SIG before… from before it was a SIG, and we were a working group, and no one took us seriously.
**Reese Lee (New Relic, Inc.)** 30:33 Everything was a struggle.
**Adriana Villela (Dynatrace LLC)** 30:35 It was a struggle, it was just, like, a few of us in the beginning, and then Dan joined, and we're like, yay, more people! And then all you joined, and we're like, yay!
**Reese Lee (New Relic, Inc.)** 30:45 People care, so…
**Adriana Villela (Dynatrace LLC)** 30:46 Yeah.
Yeah, I… like Reese said, I'm also a community manager, work at Dynatrace, and… Yeah, I won't be at KubeCon NA, but… Most likely at EU. Oh, also, hot off the press, Hotel Unplugged is happening in, after Fostom.
After…
**Reese Lee (New Relic, Inc.)** 31:10 February…
**Adriana Villela (Dynatrace LLC)** 31:11 February 1st. February 1st.
**Dan Gomez Blanco (New Relic, Inc.)** 31:13 Is that a Monday again? It's a Monday again, right?
**Reese Lee (New Relic, Inc.)** 31:15 I believe so.
**Adriana Villela (Dynatrace LLC)** 31:16 Great question, probably, yeah.
**Dan Gomez Blanco (New Relic, Inc.)** 31:19 I mean, I…
**Adriana Villela (Dynatrace LLC)** 31:19 So, it's probably.
**Dan Gomez Blanco (New Relic, Inc.)** 31:21 I mean… a lot of forced them, but the fact that the whole conference is in a weekend is, like, definitely a…
**Adriana Villela (Dynatrace LLC)** 31:26 I know, I know.
Yeah, I might not…
**Reese Lee (New Relic, Inc.)** 31:30 It's Monday.
**Adriana Villela (Dynatrace LLC)** 31:30 I'm gonna be in the general area, because I'm gonna be in London with Diana, actually, for KCD… I mean, for… oh my god, NDC London, so…
**Reese Lee (New Relic, Inc.)** 31:39 Nice.
**Adriana Villela (Dynatrace LLC)** 31:40 Maybe… I'm likely gonna pop over then for Atil Unplugged, since it's so close.
Who should I pass on to? I guess, Dana, since I mentioned you…
**Diana Todea** 31:54 Yeah, hi everyone, I'm Dana, I'm part of the hotel community, I'm currently involved in the SIG comms, or documentation, and I'm an approver in that SIG. I'm also a maintainer in the Romanian localization.
And yeah, I've been involved with Autel for more or less 3 years.
doing a lot of, talks as well, so most likely I've been bumping into many of you, in a lot of different, contexts, or you saw me at some PRs.
Yeah, so right now I have no escape. I have to be at the hotel unplugged on Monday.
February the 1st.
So… Yeah, that's… that's an obligation. Yeah, about me, sorry, yeah, I'm based in Valencia, Spain, but, I'm from Romania, Bucharest originally. Yeah, and if you're going, guys, to keep Council Lake City, I'll be there as well, so don't be shy.
Let's say hi.
grab a coffee. Well, I don't drink coffee, but you can buy me a decaf cappuccino.
Yeah, that's it.
**Reese Lee (New Relic, Inc.)** 33:14 I think we have two left.
**Atil Sensalduz** 33:18 I can go, maybe. I work as a SRE at Agpank. I'm from Turkey. I do in Smolti in Turkey, probably… you've never heard before, Snope.
And actually, I'm not in part of the community, but I am following the old events, or old YouTube videos you released, or old blog posts in the private area.
So I love the open telemetry, and… I remember the first video, Adriana released with the Iris, I guess.
Is this all? I'm not sure if I…
**Adriana Villela (Dynatrace LLC)** 33:58 Edith, you got it.
**Atil Sensalduz** 33:59 It is… And then, I, contacted Eliz, because… in that time, I was living in Portugal, and she was also in Portugal, and so I… I'm really glad to meet her after your video, actually.
if you don't release that kind of video, I am not aware of the person in the protocol and being the Automate community. And actually, we… talk afterwards. It's really great to follow these things to meet other people.
And I really liked why this meeting, actually. It's my first time I joined in this kind of committee meeting.
Yeah. Thanks so much.
**Reese Lee (New Relic, Inc.)** 34:50 Awesome, thank you.
**Adriana Villela (Dynatrace LLC)** 34:51 Thanks for joining me! I can't believe that you found us through the videos! That's so exciting!
**Reese Lee (New Relic, Inc.)** 34:56 That'd be cool.
**Adriana Villela (Dynatrace LLC)** 34:58 Aw, awesome hearing these stories.
Okay, Autumn, I think you're… you're last.
**Autumn Capasso** 35:04 Hi, I'm Autumn. I love open source and community, and I've worked in Linux and OpenJDK, but this is my first time with OTEL, so I'm really excited to get involved and to work with all of you, hopefully.
**Reese Lee (New Relic, Inc.)** 35:20 Yay!
**Autumn Capasso** 35:22 I miss you, Reese.
**Reese Lee (New Relic, Inc.)** 35:24 Yeah, I sent you a message on Slack, because I was like.
**Autumn Capasso** 35:28 Okay, good, because I miss you so much.
**Reese Lee (New Relic, Inc.)** 35:34 Yes. It's so awesome to have everyone here.
There was one thing I wanted to, we mentioned, like, at KubeCon.
Doing the livestream, Sophia?
Yeah, I just wanted to… I haven't had time to, like, really think about it, but Henry just pinged us again.
**Sophia Solomon** 35:59 Yeah, I've been asking, everyone that I've been talking to if they want to do the livestream.
So far, I have… Tyler would be available on Wednesday, as long as it's not during his talk.
**Reese Lee (New Relic, Inc.)** 36:15 Is that Jan or Helmuth?
**Sophia Solomon** 36:16 Helmuth.
**Reese Lee (New Relic, Inc.)** 36:17 Okay.
**Sophia Solomon** 36:18 And hopefully one of the girlies that, you guys just gave me Says that they would like to.
**Reese Lee (New Relic, Inc.)** 36:28 Awesome.
**Sophia Solomon** 36:31 Oh, okay.
Okay, yeah, but that's okay.
**Reese Lee (New Relic, Inc.)** 36:36 Okay, cool. So, yeah, we'll… we'll just tell Hendrik, yes, we are gonna snag it, and then we'll… We'll figure out… we'll figure it out from there.
**Sophia Solomon** 36:44 Yeah, yeah, yeah. This'll all be figured out before Wednesday, for sure.
**Reese Lee (New Relic, Inc.)** 36:48 100%.
**Autumn Capasso** 36:52 I'm not going to KubeCon, but if y'all need any help, or if there's any way I can contribute, let me know.
**Sophia Solomon** 36:58 If you know anyone going to KubeCon, please send me their name.
Please.
**Autumn Capasso** 37:05 hospitality.
**Adriana Villela (Dynatrace LLC)** 37:06 girl.
**Reese Lee (New Relic, Inc.)** 37:09 Diana, have we…
**Sophia Solomon** 37:12 We have…
**Reese Lee (New Relic, Inc.)** 37:13 Okay.
God, we need…
**Sophia Solomon** 37:17 Both the livestream and.
**Adriana Villela (Dynatrace LLC)** 37:18 I know, we…
**Sophia Solomon** 37:19 Asynch.
**Adriana Villela (Dynatrace LLC)** 37:20 We have, yeah, it's true, it's true.
It's true. Yeah, that's right, it was last year in Atlanta, right?
**Diana Todea** 37:26 Yes, that's it. Yeah, last year, yeah.
**Adriana Villela (Dynatrace LLC)** 37:30 Yeah.
Dang it.
**Reese Lee (New Relic, Inc.)** 37:33 I know, they're all blurring together.
**Adriana Villela (Dynatrace LLC)** 37:35 I know.
**Diana Todea** 37:36 So it's like, you get banned if you're, like…
**Sophia Solomon** 37:38 Oh my goodness.
**Diana Todea** 37:39 Or you're like, we don't want you, get out of here!
**Adriana Villela (Dynatrace LLC)** 37:42 How can I get out of here, man.
**Diana Todea** 37:44 But we want other people.
**Adriana Villela (Dynatrace LLC)** 37:47 Another thing that we can do, because we don't necessarily have to focus on, hotel, like, contributors and maintainers, even end users, to someone who uses OTEL, Tim… And also be… It's definitely most welcome, and we've done that in the past as well.
**Reese Lee (New Relic, Inc.)** 38:10 Yes, this is true.
**Adriana Villela (Dynatrace LLC)** 38:16 find them.
**Reese Lee (New Relic, Inc.)** 38:18 Yeah, so we have the humans at Botan, then we have the livestream.
**Adriana Villela (Dynatrace LLC)** 38:21 Yes. Yeah, the livestream has to be able to tell people.
Usually. Well, we used to do, like, one hotel person and then one end user, so… In the past, though, I guess we could still do that.
**Reese Lee (New Relic, Inc.)** 38:39 I feel like I remember Hazel being the only, like, non… Official hotel person that we.
**Adriana Villela (Dynatrace LLC)** 38:46 Yeah, maybe, now that you mention it.
**Autumn Capasso** 38:49 And it gets hard, because a lot of people aren't going to North America this year for, like, KubeCon.
And even people that were.
**Adriana Villela (Dynatrace LLC)** 38:55 me up.
**Autumn Capasso** 38:56 have, like.
canceled, so it's, like, rough trying to get people, like, I know people that are still trying to fit, like, fill fill days and, like.
You know, find people to replace him, so…
**Adriana Villela (Dynatrace LLC)** 39:07 Yeah…
**Sophia Solomon** 39:09 Oh, that's fun.
**Reese Lee (New Relic, Inc.)** 39:11 Yeah, I have a…
**Autumn Capasso** 39:12 Ours was way smaller than they were expecting, so I think it's just… Rough this year.
**Adriana Villela (Dynatrace LLC)** 39:17 Yeah, that's true.
**Reese Lee (New Relic, Inc.)** 39:19 Wait, what was way smaller than expected?
**Autumn Capasso** 39:21 Was it weird?
**Adriana Villela (Dynatrace LLC)** 39:21 numbers.
**Autumn Capasso** 39:22 I think.
**Adriana Villela (Dynatrace LLC)** 39:23 Oh, we are developers. Oh, the one in the… in California, right?
**Autumn Capasso** 39:27 Yeah, because it was the first year in the US, but I also just think that it's because people aren't traveling, and, like, not a lot of people are getting, like, funding to go to conferences, you know what I mean? So…
**Adriana Villela (Dynatrace LLC)** 39:37 Yeah, it's kind of a intersection of…
**Autumn Capasso** 39:42 Exactly. Like, it's a bunch of contributing factors all around.
**Adriana Villela (Dynatrace LLC)** 39:46 Yeah, it's true.
**Reese Lee (New Relic, Inc.)** 39:50 I'll look through my list of ContribFest people, like, maintainers are coming to ContribFest to help out.
And I'll see if there's anyone that we haven't talked to from that list yet.
**Adriana Villela (Dynatrace LLC)** 40:01 Great idea.
Worst case, we sneak in someone who's spoken before.
As long as it's been someone who's been, like, we haven't heard from in a while.
**Reese Lee (New Relic, Inc.)** 40:13 Yeah.
**Adriana Villela (Dynatrace LLC)** 40:14 That is also a possibility. Sometimes we have very ad hoc people… the conference itself, the day of, like, the last KubeCon EU, we literally sent people out, finest people to interview!
**Reese Lee (New Relic, Inc.)** 40:29 You did that.
**Adriana Villela (Dynatrace LLC)** 40:30 What?
That's also a thing.
**Reese Lee (New Relic, Inc.)** 40:39 I think that was… it. Okay, so we will…
**Adriana Villela (Dynatrace LLC)** 40:44 Dang.
**Reese Lee (New Relic, Inc.)** 40:45 Okay, I let Henrik know that we are gonna grab the 3.30 slot, and then we'll just see who can talk to us Wednesday at 3.30.
**Autumn Capasso** 40:53 How many people are you looking for that you don't have yet?
**Sophia Solomon** 40:56 As many as you want. As many as you can send.
**Adriana Villela (Dynatrace LLC)** 41:01 Dream 1 to 2, right?
**Reese Lee (New Relic, Inc.)** 41:04 Oh, yeah.
It also… yes, it also depends on, like, you know, their availability at the time, because it is a fixed time, and sometimes people talk or something. So yeah, whoever you can think of, and then we can see if the timing works out. But yeah, for the livestream, one to two people, and then… I'm not sure how many people Sophia's still looking for for humans of hotel.
**Sophia Solomon** 41:26 Honestly, just… One more person, but a big list.
**Adriana Villela (Dynatrace LLC)** 41:30 Oh, okay.
**Sophia Solomon** 41:30 I'll never say no to.
**Vidhya Divakar** 41:32 I think I missed the channel's name, Sophia. Where was the list posted? I saw it, like, a couple of days back.
The list of people.
**Sophia Solomon** 41:42 Oh, I mean, I can write it down in our notes so far, but
**Adriana Villela (Dynatrace LLC)** 41:47 Beautiful.
**Sophia Solomon** 41:47 But there's no, like, formal list anywhere.
**Vidhya Divakar** 41:49 I mean, oh, okay, I think I saw this somewhere, like, okay.
**Sophia Solomon** 41:55 Please.
**Adriana Villela (Dynatrace LLC)** 41:58 For the livestream, we can, we can probably get away with, like, a GC member, or TC member? Actually, it'd be nice to have a TC member.
In the livestream. Have we ever had a TV member in the livestream?
**Reese Lee (New Relic, Inc.)** 42:16 I have to look at the list, honestly.
**Adriana Villela (Dynatrace LLC)** 42:18 I think we've, like… it's usually been Austin and Ted.
And then we have…
**Reese Lee (New Relic, Inc.)** 42:23 on,
**Sophia Solomon** 42:26 Arna?
**Reese Lee (New Relic, Inc.)** 42:27 We had, yeah, actually, Sophia, the one that we did that.
**Adriana Villela (Dynatrace LLC)** 42:30 one year.
**Reese Lee (New Relic, Inc.)** 42:31 had Jacob…
**Sophia Solomon** 42:32 Hmm.
**Reese Lee (New Relic, Inc.)** 42:35 Oh yeah, that was the year we had Jacob, and Diana, I think.
**Sophia Solomon** 42:37 Yep.
**Adriana Villela (Dynatrace LLC)** 42:38 Yeah, Jacob's off.
But yeah, I think… We should probably try to get someone new.
**Reese Lee (New Relic, Inc.)** 42:46 But yeah, I'll, yeah, I'll try to get together a list of… Who we have talked to in the past.
And the contribute vest list.
**Autumn Capasso** 42:57 It sounds bad, but sometimes, like, the best way to do it is just to, like, find people at lunch that day that don't have anything quality.
**Adriana Villela (Dynatrace LLC)** 43:05 That is pretty much what we did last KubeCon.
**Autumn Capasso** 43:07 That has been very successful for me in the past.
**Reese Lee (New Relic, Inc.)** 43:11 Yeah, sometimes, yeah, sometimes it works out that way,
**Sophia Solomon** 43:14 my strategy.
**Autumn Capasso** 43:16 like, are you doing anything after this? Cool, guess what? You're on a panel.
**Adriana Villela (Dynatrace LLC)** 43:22 That's how First Humans of Votel came about. It just started randomly flagging people down.
**Autumn Capasso** 43:28 I feel like it works out, though, because there are people that are available, and they're, like, slightly more rested, because they went to lunch, because it's always, like, back-to-back, you have a talk, then you have to go to a panel, and you're tired. So, it works out sometimes.
**Adriana Villela (Dynatrace LLC)** 43:44 You know, that's not a terrible idea, because then, Like, we did pretty well.
with a booth last KubeCon.
We had lots of people come by.
I wonder if we just flagged them down.
**Autumn Capasso** 43:57 It worked well at scale, too.
**Adriana Villela (Dynatrace LLC)** 43:59 Yeah, why don't… why don't we… if we're really, really stuck.
**Reese Lee (New Relic, Inc.)** 44:04 Yeah, if we're really stuck, I'd rather book people ahead of time, because…
**Adriana Villela (Dynatrace LLC)** 44:08 Hmm.
**Reese Lee (New Relic, Inc.)** 44:08 borders for me, I have… Yeah, it's just gonna be… nuts,
**Autumn Capasso** 44:16 Are you going to keep Kantu?
**Reese Lee (New Relic, Inc.)** 44:19 Me? Yes.
**Autumn Capasso** 44:20 Awesome.
I'm sorry to not let you all.
**Reese Lee (New Relic, Inc.)** 44:24 Yeah, we'll try to book as many people as we can, and then if we're still looking for anyone else, then… Yeah, we'll do the KubeCon hallway track.
Method.
Mmm…
**Adriana Villela (Dynatrace LLC)** 44:38 Oh, livestream, that's a bit harder. You definitely need someone.
**Reese Lee (New Relic, Inc.)** 44:42 Yeah, since that one is…
**Adriana Villela (Dynatrace LLC)** 44:44 ahead of time.
**Reese Lee (New Relic, Inc.)** 44:47 Yeah.
Okay, well, that was all I have, I think.
**Adriana Villela (Dynatrace LLC)** 44:56 Should we talk about scheduling the SIG meetings on-site?
**Reese Lee (New Relic, Inc.)** 45:02 Oh, yes, actually… good call, I haven't.
**Adriana Villela (Dynatrace LLC)** 45:05 I know you had started that.
You said you started on the maintainer's channel, right?
**Reese Lee (New Relic, Inc.)** 45:10 I did… there were a couple… SIG got signed up, but I need to… Okay, let me see.
Okay, there's a couple more SIGs that have… Signed up.
And then kiosk shifts, but… I'll try to find other maintainers for that.
Yeah, I think getting the, SIG Meetings set up… Is probably the next… urgent list thing?
**Vidhya Divakar** 46:17 So I'm… I'm seeing a list, Dan shared, like, it shows all the… dates and times available. That's what you're talking about, right, Reese?
Dan, I shared in the Slack.
**Reese Lee (New Relic, Inc.)** 46:37 Mmm…
**Vidhya Divakar** 46:38 Yeah, hotels, SIG End-User contributors, yesterday at 1.22PM.
**Reese Lee (New Relic, Inc.)** 46:44 I'll also just dropped the link into the chat.
**Vidhya Divakar** 46:50 Okay, yep.
**Reese Lee (New Relic, Inc.)** 46:56 Yeah, ContribFest is happening, so I'm not sure how we're gonna fill these slots.
**Vidhya Divakar** 47:00 You know… What would be the starting place to look for people? Is it, like, from the Slack?
What is it?
**Adriana Villela (Dynatrace LLC)** 47:14 channels where we usually reach out, but, I mean, we can… If you really want, go into each individual SIG channel.
pump it up, like, big ones.
the language SIGs, Oppo Collector… Jenny on…
**Reese Lee (New Relic, Inc.)** 47:42 GenAI, we have… they have signed up.
CSED network policies…
**Adriana Villela (Dynatrace LLC)** 47:51 The op-amp people, I happened to be on their channel yesterday.
And they were talking about planning something for KubeCon, and then I'm like, we're looking at it.
**Reese Lee (New Relic, Inc.)** 48:02 Yeah…
**Adriana Villela (Dynatrace LLC)** 48:05 But I just point them to the… your message?
maintain it.
**Reese Lee (New Relic, Inc.)** 48:11 Or just, link to the sheet, and they can just pick a time from there.
**Adriana Villela (Dynatrace LLC)** 48:15 Okay.
**Vidhya Divakar** 48:16 Nope.
**Reese Lee (New Relic, Inc.)** 48:19 Okay.
**Adriana Villela (Dynatrace LLC)** 48:20 sheet. Sheets and maintainers, right?
**Reese Lee (New Relic, Inc.)** 48:22 It is. I also just posted it in the Zoom chat as well.
**Adriana Villela (Dynatrace LLC)** 48:26 Oh, sweet. That'll be easier. Okay.
I'm going to… perfect.
**Reese Lee (New Relic, Inc.)** 48:40 Okay… Yes, we still have several spots available, and…
**Diana Todea** 48:49 So, sorry, just a question, because I'm looking at the spreadsheets, Reese. So, if I wanna… take a slot, I just blur it out and put it immediately, or…
**Reese Lee (New Relic, Inc.)** 49:01 Oh, you can just put your SIG name down, and then… I can… I'll change it, because… yeah.
**Diana Todea** 49:06 Okay, I'll just put, because there is like, localization is within comms, so I just put COMS.
**Reese Lee (New Relic, Inc.)** 49:16 Okay, that works.
That's funny.
**Diana Todea** 49:19 So, I'll just put, like, comms slash localization.
**Reese Lee (New Relic, Inc.)** 49:23 Oh, awesome.
Okay.
Yeez!
**Diana Todea** 49:26 In case.
Is it close to the lunch place? I'm just kidding, no, I'm just… it's fine.
**Reese Lee (New Relic, Inc.)** 49:33 I…
**Diana Todea** 49:37 It's a joke, don't answer that. It's a trap.
**Reese Lee (New Relic, Inc.)** 49:41 Oh, I didn't do the full map.
Oh, you know what, actually, if you look… Go up a little bit, to the diagram.
And then you see where it says… where I circle project meeting tables? Next to it is, like, a fork and a knife, and so it might be… lunch pickup might be right there.
**Adriana Villela (Dynatrace LLC)** 50:01 Right on.
**Diana Todea** 50:02 Yes, it is.
I like it… sorry.
I like it how strategically it's positioned next to the lunch place, so people can just grab something and then chat about open telemetry, so that's cool.
**Adriana Villela (Dynatrace LLC)** 50:20 I mean, I did complain, or not complain, suggest that we really had a nice spot last time for KubeCon EU next to some tables for meetings, so it would be ideal to have a good spot again for our booth, so maybe that's why Maybe that's why we ended up with the switcheroo Reese.
Well, then they gave us extra slots.
For the booth.
**Reese Lee (New Relic, Inc.)** 50:45 Oh.
I don't know, but…
**Adriana Villela (Dynatrace LLC)** 50:48 Anyway, I did ask for an optimal… optimized location so we could hold our SIG meetings.
**Reese Lee (New Relic, Inc.)** 50:56 Nice.
Yeah, I don't know where the other flaw would have been. It's all very, like… Hush, hush.
Mmm…
**Adriana Villela (Dynatrace LLC)** 51:09 I, I basically, with, I think it was, I want to say Pablo, And I… pegged down Lindsay at Observability Summit and talk to her for, like, a good half hour.
And we're like, this, this. We gave her, like, of our, our, our stuff.
She was very good about it.
**Diana Todea** 51:38 Guys, sorry, I need to drop, I'm…
**Vidhya Divakar** 51:40 Yeah.
**Diana Todea** 51:40 We're having dinner now, and then I have, like, a Country Fest meeting with the people in, like, 5 minutes.
**Adriana Villela (Dynatrace LLC)** 51:49 Go for it.
**Diana Todea** 51:49 Good job in Salt Lake City. Take care.
**Adriana Villela (Dynatrace LLC)** 51:52 Alright, bye, thanks.
**Sophia Solomon** 51:53 scheduling in it.
**Autumn Capasso** 51:53 Bye.
**Sophia Solomon** 51:54 Have a nice dinner.
**Diana Todea** 51:55 Thank you, bye.
**Vidhya Divakar** 51:57 Yeah.
**Adriana Villela (Dynatrace LLC)** 51:58 I think we're pretty much done anyway, right?
**Vidhya Divakar** 52:01 I passed on.
**Adriana Villela (Dynatrace LLC)** 52:02 your message to the OpAmp people, so hopefully they sign up for a slot.
**Reese Lee (New Relic, Inc.)** 52:07 Awesome. Yay! Okay, cool. Yeah, I think we are… like, we're good!
**Autumn Capasso** 52:12 It would be the best place to, like, find stuff to start, like, being able to contribute or help out or anything.
**Reese Lee (New Relic, Inc.)** 52:22 With, like, this SIG specifically?
Excellent question.
**Autumn Capasso** 52:30 You don't have to answer it now. Just let me know if you think of anything, like, after a coupon, because it's a lot going on right now.
**Adriana Villela (Dynatrace LLC)** 52:37 You know what? You could always… we could always use help with coordination for the livestreams. Like, Sophia and Victoria run, run the livestreams themselves, but there's a lot of, like, prep work that goes on in the background.
So, even helping with coordination of guests, if you feel super, creative and want to create assets as well, like, we could always use help for that.
**Autumn Capasso** 53:00 Okay.
**Vidhya Divakar** 53:02 Yeah.
**Autumn Capasso** 53:03 let me know if there's anything in particular. If not, is there, like, a place for me to, like, find docs or issues or anything to, like…
**Sophia Solomon** 53:11 Yeah, and the end-user, SIG, GitHub.
Okay. For OpenTelemetry, and you can always message me and Victoria in, like, a group chat, and we can coordinate from there, too.
**Autumn Capasso** 53:23 Okay, thank you.
**Vidhya Divakar** 53:23 So much. Yeah, likewise, I also would like to reach out to you someday, like, whatever, like, Autumn says.
**Sophia Solomon** 53:29 For sure.
**Vidhya Divakar** 53:30 Yeah.
Anyway, it was nice meeting you guys, and I'd also like to drop, and…
**Adriana Villela (Dynatrace LLC)** 53:35 Here, I put a link to the… to the repo for both of you, Vidhya and Autumn, so, yeah.
**Sophia Solomon** 53:42 Thank you for joining.
**Vidhya Divakar** 53:43 Have a good time. Thanks, everybody.
**Adriana Villela (Dynatrace LLC)** 53:45 Thanks, we appreciate it. Alright!
**Vidhya Divakar** 53:48 Right?
**Adriana Villela (Dynatrace LLC)** 53:49 Bye!
**Vidhya Divakar** 53:50 Yay.
