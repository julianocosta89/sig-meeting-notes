SIG: Technical Committee
Date: 2025-07-02
Duration: 9 minutes
============================================================

## Zoom Recording Transcript

**Armin (Dynatrace)** 00:13 Behave.
**Tigran Najaryan** 00:17 Hey, Alvin, how are you?
**Armin (Dynatrace)** 00:22 It's good.
We don't have the Gctc. Meeting today. Right? That's every second Wednesday, right?
**Tigran Najaryan** 00:31 Yeah, I don't think we have it today. There's nothing on my calendar.
Hey, Jack, welcome.
**Jack Berg** 00:47 Hey? Tigreen.
**Bogdan Drutu** 00:50 Hmm.
**Jack Berg** 00:59 Right.
**Tigran Najaryan** 02:11 I think, Riley said. He can't join. I don't know if Joshua Lumilla will be here, though.
**Jack Berg** 02:23 Haven't heard anything from either of them.
**Tigran Najaryan** 02:41 Then we can start with your topic, Jack.
**Jack Berg** 02:45 Yeah, so this is this is an issue that was just open this morning
on the community repository. There's a donation proposal from elastic about some
sort of product that, you know automatically installs php instrumentation.
And so, you know, as part of that donation proposal.
I think there's going to be due diligence at some point. Maybe we can punt on it for the time being, because I think, if I remember the process correctly. The Gc. Has to kind of give it the thumbs up before we go ahead with the Tc technical diligence.
but just wanted to give a heads up that that's probably coming down the pipe.
**Tigran Najaryan** 03:36 Okay, I see Severin already, so that he's going to be the liaison. So I guess it's on the Gcs court at the moment.
so that there's nothing for us to do at this stage.
**Jack Berg** 03:53 Yeah, I don't. I don't think so. I'm just. I just wanted to call attention to it.
**Tigran Najaryan** 03:58 Okay.
okay, we'll figure out who does the due diligence after the Gc. And if they they accept it, I guess.
Okay, can we go to the next item.
**Jack Berg** 04:20 Yep.
**Tigran Najaryan** 04:23 Okay. So this one is, I guess, a carryover from the the last time we met. And with the we wanted to do the rotations, I think. Josh and Bogdan, you guys were not in that call everybody who was in the call. They agreed to do the rotations. You are the only people remaining there
who will need to, I guess, agree or or disagree any thoughts.
**Bogdan Drutu** 04:49 Both of us.
**Josh Suereth** 04:50 I'm totally on board. Yeah.
**Bogdan Drutu** 04:53 I think I did the same thing with the answer in the slack.
**Tigran Najaryan** 04:58 All right.
I think then we're good. We'll need to figure out. Where do we put it? In? What calendar we can do that offline. We don't have to
to it right now.
I think we have some details there that we need monthly. We need weekly schedules.
So we're just for now I guess we're going with Jack, I think we discussed, we'll just do the the Google Calendar right? We'll use it as a scheduling tool essentially
what I think last time we talked about it.
**Jack Berg** 05:29 Which Google Calendar
because I thought I remembered us talking about the the just adding it to the Tc. Meeting notes sort of like the the ga room.
**Tigran Najaryan** 05:43 Why don't we use the Google Calendar? Because it's
probably easier. And the kids are, I guess
I mean the the recurring. I guess the recurrence. You could put it in the calendar right? So that it also can remind you.
If it's a it's a calendar event, you can put the reminders and and stuff like that. I I mean, it's fine. If if Doc works, we can just do a doc as as well. It's okay with me.
**Josh Suereth** 06:11 I think we should optimize for 2 things. One is the least amount of work on us to keep it up to date, and 2 is the ability for us to go on vacation.
which is the whole point of having rotation. Right? So if you need to go on vacation, and you're scheduled for a certain date. And it's really annoying to swap with people which Calendar might actually make it that way in my experience. That would be problematic. So those those would be the 2 things that optimize for.
**Tigran Najaryan** 06:40 Okay, then then maybe let's start
very simple, and just put it in a doc, and we'll see if we need something more than that.
**Jack Berg** 06:49 So I can take an action item just to you know, seed the initial schedule, maybe something like 8 weeks in advance.
With, you know the dates, and I can use a random number generator to, you know. Figure out the order of things. And you know, that can be a starting point, and we can go from there.
**Tigran Najaryan** 07:10 Sounds good.
**Jack Berg** 07:22 Thanks. Bogdan.
**Josh Suereth** 07:25 If if we're gonna.
**Tigran Najaryan** 07:27 Toss, toss a coin. Bogdan.
**Josh Suereth** 07:28 Yeah.
**Tigran Najaryan** 07:29 A real physical random number generator.
**Josh Suereth** 07:33 If you want to be super crazy, we could hit. Ask AI to generate it for us.
Isn't that the thing? Now.
**Jack Berg** 07:42 Oh, yeah, maybe I'll give that a try, plug it in and see what it spits out, and then argue with it for an hour.
**Josh Suereth** 07:49 Yeah, yeah, it's a. It's cool.
We had a discussion just randomly on the side in the weaver channel where they were trying to teach AI how to do code reviews.
and it's when it doesn't get it right. It's like, you know, working with a toddler where you know that they will never learn
right, but when it gets it right it's magical. So.
**Jack Berg** 08:16 It's hard. I it's hard to know when you should stop arguing with it, and just give up versus like, you know, if I just
if I just say the right, you know order of words, the right words in the right order. Maybe it'll do the right thing, and so there's like some sunk cost fallacy going on.
**Josh Suereth** 08:40 Anyway. Sorry to derail it.
**Tigran Najaryan** 08:42 Okay? So should we, I guess for the private discussion, I guess we'll need to use a different zoom
link, right? This one gets recorded.
**Jack Berg** 08:54 Yeah. So I guess before we go over to that private zoom,
do we want to have that discussion? This is the this is the best attendance of the Tc. We've had in a while. We have 7 out of 8 of us here. That's pretty good. And you know, I think importantly, Josh is here, and Josh was leading some of these discussions a a bit back. And so is this the right time? I I think yes.
alright. I'll see you over there then.
**Tigran Najaryan** 09:24 Where? Where is? Where's the link over? Where can you post it? Somewhere in our slack channel?
**Jack Berg** 09:29 In the slack channel. There's a there's a section of called bookmarks, and Armin has set up all the bookmarks, for you know, common links, the private channel, and the.
**Tigran Najaryan** 09:38 Okay. Thank you. Yes. Okay. Got it.
**Jack Berg** 09:41 See ya.
**Armin (Dynatrace)** 09:42 You know.
