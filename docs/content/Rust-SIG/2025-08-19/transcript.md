SIG: Rust SIG
Date: 2025-08-19
Duration: 23 minutes
============================================================

## Zoom Recording Transcript

**Utkarsh Umesan Pillai** 12:13 Hey, Christian.
… Kristen, are you saying something? I don't hear you.
**Christian Leghadjeu** 12:51 Well, so we always mention.
Can you get to me.
**Utkarsh Umesan Pillai** 12:55 Yeah, I can hear you now.
**Christian Leghadjeu** 12:56 Yo, hello.
**Utkarsh Umesan Pillai** 12:59 Hi, so, … Yeah, we'll probably wait for a couple more minutes, maybe give a few other maintainers
a chance to attend today's call.
Have you joined the SIG meeting before, or is this your first time attending this?
**Christian Leghadjeu** 13:16 No, it's my first time. I think this is the… the host… jurisdiction.
**Utkarsh Umesan Pillai** 13:25 Sorry, could you repeat that? This is the….
**Christian Leghadjeu** 13:28 I mean, is this the… the horse section?
**Utkarsh Umesan Pillai** 13:36 I'm… I didn't quite catch it. Is this, this, the, what, the… stick.
**Christian Leghadjeu** 13:42 the horse.
Whoa!
**Utkarsh Umesan Pillai** 13:45 Yeah, I mean, … The meeting usually is hosted
By, I mean, the Zoom meetings and anything that's hosted by the CNCF?
The channel itself, but the main drivers of the meeting are usually the maintainers of the repo.
And, … Yeah, there's a guy called CJ Thomas.
Then there's Lalet, and Yongyang, and then myself. There are a couple of maintainers for the repo, and…
we run the meeting. So, did you add things to the agenda items today for the doc, or…?
**Christian Leghadjeu** 14:23 No, no, it was just genuine to….
**Utkarsh Umesan Pillai** 14:26 We're just joining, okay, okay.
**Christian Leghadjeu** 14:27 You're interested.
**Utkarsh Umesan Pillai** 14:28 What do you do, like, and how… are you using OpenTelemetry Rust in your world?
**Christian Leghadjeu** 14:34 Yeah, in my, programs. So, just trying to see….
**Utkarsh Umesan Pillai** 14:40 could be a contributor. I see.
**Christian Leghadjeu** 14:43 I'm muting, but I've been using it.
**Utkarsh Umesan Pillai** 14:45 Okay, okay, okay, sounds good. …
Yeah, I… I'm not sure, somebody has put an agenda already on the… you know of the Google Docs, where we put the agenda for the…
Meeting and everything.
Yeah, yeah. So somebody has already put the agenda, but I don't know who it is, because…
There's no one other than the two of us, so… I will… riveted some more down, …
Also, feel free to write your name to the attendees list.
What's data.
**Christian Leghadjeu** 15:23 Oh.
**Utkarsh Umesan Pillai** 15:25 Yeah.
**Christian Leghadjeu** 15:25 In the agenda.
**Utkarsh Umesan Pillai** 15:27 Not in the agenda, I mean, yeah, under the attendees.
Section, title, head of….
**Christian Leghadjeu** 15:35 Oh, you mean in this meeting?
**Utkarsh Umesan Pillai** 15:38 Let me quickly show you what I'm talking about. So, are you aware of this… …
Let me know in my screen.
**Christian Leghadjeu** 15:54 Okay, I can see your screen.
**Utkarsh Umesan Pillai** 15:56 Yeah, so you, you know where… you know, do you have the link to this doc?
**Christian Leghadjeu** 16:01 No, no, I closed it. Please consensus chat.
**Utkarsh Umesan Pillai** 16:07 I see.
I can share the link here again, but … yeah, you can join the Slack channel, the Otil Rust Slack channel, if you're aware of it.
**Christian Leghadjeu** 16:17 Oh, okay, okay, that seems….
**Utkarsh Umesan Pillai** 16:19 If you don't have the link to the Slack channel, I can help you find that as well.
**Christian Leghadjeu** 16:24 No, thank you, that'll be good.
**Utkarsh Umesan Pillai** 16:30 Where to go to… the Rust SDK report.
and look at… contribute any.
So, yeah, this is the… this calendar will host… we'll have, like… we'll show you all the other…
SIGs, and when their meetups… when their SIG meetings happen.
This is the link to the Google Doc that I shared on the chat.
**Christian Leghadjeu** 16:56 No.
**Utkarsh Umesan Pillai** 16:58 And, just give me one sec, okay? Give me one sec.
Yeah, so, this is the contributing section, and, you can…
like, check the community calendar. You'll also have a link to the Google Doc, and this is the Slack channels link.
So I'd suggest you join it, and, like.
Yeah, just for more updates about the repo.
**Christian Leghadjeu** 17:56 Okay, okay, okay.
Might do that after the machine.
**Utkarsh Umesan Pillai** 18:00 Yeah, so I… I'm not sure at this point if any of the other maintainers are gonna join, but…
Yeah, feel free to write your name here, or I can just write it.
Yeah, up to you if you wanna put in your company, company name.
**Christian Leghadjeu** 18:27 No, not for now.
**Utkarsh Umesan Pillai** 18:29 Okay, for sure.
I am not sure who put the agenda, so… and, I mean, whoever put it hasn't joined, so…
I think we can, and …
Unless you have anything specific to ask.
**Christian Leghadjeu** 19:09 Mmm… not reading.
Thank you.
**Utkarsh Umesan Pillai** 19:13 And you can take a look at, …
Maybe, let me see if there are…
like, when you… if you go to the repo here and click on issues, …
Try to find, like, good first, good first issue.
on….
**Christian Leghadjeu** 19:38 Thank you.
**Utkarsh Umesan Pillai** 19:38 Wanted, and then… Yeah.
And then search for those, so we have a few, yeah, good first issue, maybe you can…
Take a look at these, and if you just want to get yours.
Hands dirty, and… Start trying things.
**Christian Leghadjeu** 19:56 Yeah. For the pull request, approvals, like, reviewers, are there specific people I need to… To others reviewers.
**Utkarsh Umesan Pillai** 20:04 No, not really. You just create a pull request, and, like, it's the approvers and maintainers…
responsibility to the UTIs and get them merged, so you don't have to add anyone specifically.
**Christian Leghadjeu** 20:17 Oh, okay, okay.
**Utkarsh Umesan Pillai** 20:18 Like, we get a notification anytime a new pull request is created.
If you get smushed.
Yup.
**Christian Leghadjeu** 20:28 Oh, good.
**Utkarsh Umesan Pillai** 20:29 Okay, yeah, I mean… I'm just gonna add in some other comments about, like…
Like, this was not discussed or something, but just update the meeting notes. But I think we can end the call, because I didn't see anyone else joining.
And, also, where do you work from? Like, which, like, where are you located?
**Christian Leghadjeu** 20:57 Come on.
**Utkarsh Umesan Pillai** 21:00 Well, where is that? Sorry.
**Christian Leghadjeu** 21:02 Come on, come on.
Okay. Africa.
**Utkarsh Umesan Pillai** 21:06 Oh, I see, okay. Nice.
….
**Christian Leghadjeu** 21:12 Sure.
**Utkarsh Umesan Pillai** 21:13 Alright then, sounds good. We'll end this meeting, but I think it's good to watch out, like, I would say in the Slack channel, and …
This last time to go.
….
**Christian Leghadjeu** 21:26 What you want to eat.
**Utkarsh Umesan Pillai** 21:27 updates, and then I think once we….
**Christian Leghadjeu** 21:32 Okay, okay.
**Utkarsh Umesan Pillai** 21:33 And I'm not sure what time
It is in Cameroon right now.
Somebody did put this in the agenda. Let me put in the, … wait, this is….
**Christian Leghadjeu** 21:47 No, it's, like, 5.14.
Right now.
**Utkarsh Umesan Pillai** 21:52 It's, … Okay, okay.
Yeah, so, I don't know, somebody put this agenda as well, so… Hmm…
It would have been great if they actually attended the meeting, and we could have discussed this, but… Yeah.
Oop.
I'm gonna end the meeting now.
**Christian Leghadjeu** 22:11 Okay, okay. Seeing for it, see you next.
**Utkarsh Umesan Pillai** 22:14 Before I see myself.
**Christian Leghadjeu** 22:19 Thank you, goodbye.
