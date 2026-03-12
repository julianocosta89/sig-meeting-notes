SIG: Ruby SIG
Date: 2025-07-29
Duration: 28 minutes
Zoom Recording URL: https://zoom.us/rec/share/PysPV00EJKFJf7z2p8r1jWGCNlRdF3cEei2Y2Tzp4PPFSN2qVQN33h0jV7LwmUs.VgTYmZUtF_kA-75P
============================================================

## Zoom Recording Transcript

**Eric Mustin** 01:59 Hey, everyone.
**Hannah Ramadan** 02:07 Hey Eric, hey! Sean.
**Eric Mustin** 02:16 How is your Tuesday going? I'm just loading up the calendar. Sorry the Google, Doc.
Okay, I think Kayla can't attend today. I can.
I happy to it back.
Which is full. Actually.
yes.
**Hannah Ramadan** 03:15 Here I can.
**Eric Mustin** 03:16 And you're like off all the attendance.
Let me share you can probably say like 10,000 chapters. But okay, let me know if you cannot share. See my screen.
these are. These have been things Kayla dropped in here. Is that right? There's these aren't dupes from last week. Right
**Hannah Ramadan** 03:49 Alright!
**Eric Mustin** 03:50 Okay.
Did anyone attend the spec Sig by any chance.
**Hannah Ramadan** 04:00 No.
**Eric Mustin** 04:01 Yeah, I did.
Have you ever done those?
**Hannah Ramadan** 04:08 I never have.
**Eric Mustin** 04:10 I think I maybe went once in the and then left halfway through. But I certainly didn't attend this one. Okay, well.
I can. We can look at it for 2 seconds. If no one objects or I'll time box it to, you know.
3 min, maybe and see if there's anything that came up that we should urgently be concerned about, and something about something on the client with user agent and something about okay. Gosh.
I don't know what that is. Entity, which is is that even I didn't even know that was merged into the specs. That shows where I'm at I guess there's a something around entity and environment variables. But I don't think, are we implementing entity anywhere in our SDK, I don't think so okay.
well, in that case, I don't have any questions. So I think that, concludes the spec, I? Okay, that was a minute.
Okey dokey we're getting so onto our stuff.
There's some run from the security scanning tool about importing or running the security savings tool. Okay.
does anyone know anything about this?
The skill engine reschedule.
**Hannah Ramadan** 06:06 Looks like what I can't tell. This is maybe the 1st failure. This one was 16 h ago.
I don't know, because it's like anything before this, or brand new.
**Eric Mustin** 06:18 See?
Okay, I'm not concerned.
Something failed. Is that the one from? No? Oh, it's yeah. Failing.
**Hannah Ramadan** 06:28 Yeah.
**Eric Mustin** 06:28 It retried. No? Oh, it's a different a different scan.
Hmm!
Maybe it was an intermittent failure.
**Hannah Ramadan** 06:43 Potential.
**Eric Mustin** 06:48 Maybe I'll just search for this error message real quick in our open issues.
if you don't mind. I certainly don't know anything about it.
where we come up upon this. Maybe I guess it didn't come up as an issue it just she Kayla, just noticed a fail I don't think let's see if this specific action was in this following job. And then I'll maybe time box the investigation because I have no experience here. Unless someone else has a I'll get back there. Concern.
So apologies for it.
What's around?
So there this action was.
**Hannah Ramadan** 07:55 Yeah.
**Eric Mustin** 07:56 This action. Let's compare that to the following act the one that was passed.
See if there is some.
It looks like the same.
**Hannah Ramadan** 08:09 Oh, action!
**Eric Mustin** 08:11 No, there's an error again.
Something about the gem file.
Gosh, But it passed eventually, and.
**Hannah Ramadan** 08:27 Well.
**Eric Mustin** 08:28 Confused again. Sorry I am down a weird rabbit hole.
and let's see where it passed somehow, or did we just time out in some way occurred pretty failed.
Gosh.
**Hannah Ramadan** 08:44 Yeah, it looked like it was just upset from a missing a Gen. File lock. I can't.
**Eric Mustin** 08:49 And then recovered or reinstall dependencies in some way. Let me see if I scroll past it.
**Hannah Ramadan** 08:59 What if this happens every time.
The other one seems kind of intermittent. The I think I saw it was like an error fetching faucet.
**Eric Mustin** 09:09 Yeah, it was a oh, I see there's a few.
Seems to be the same.
**Hannah Ramadan** 09:18 Since there.
**Eric Mustin** 09:20 I guess they're running this.
In this next case they were actually running the tool and the tools output was a failure. Something along those lines. I'm I'm not quite sure.
I'm trying to time box it, but I don't have a maybe we need to open an issue at least case here. Where?
See? Why? Let's let's see if this consistently fails. Like to your point you just mentioned. I guess. And then, you know, because I got nothing see what else on the agenda? I guess.
looking at the time we we still have a few minutes. If you wanna computer.
**Hannah Ramadan** 10:02 The bundle, one seems, or the jump out the lock error I saw on a couple other ones, probably just something that takes a couple of Retries don't love it, but.
**Eric Mustin** 10:11 Okay.
**Hannah Ramadan** 10:12 It? Possibly.
**Eric Mustin** 10:16 Okay, I we'll go ahead and say that I'd think we should leave this as maybe open an issue. And because if I see here, I don't think we have an issue for this, and maybe try to close in the future.
Does that sound like a good plan here?
Yeah, hmm.
**Hannah Ramadan** 10:48 Yeah, yeah, I think you can.
**Eric Mustin** 10:49 Or is it? I guess it was intermittent, so there's no real concern.
I'll just leave a note on that comment here.
**Hannah Ramadan** 10:56 Yeah, I'm trying to see if Fossa had updates recently.
**Eric Mustin** 10:59 No.
**Hannah Ramadan** 11:00 Would have caused that by not seeing anything.
I feel like we can see what happens tomorrow.
**Eric Mustin** 11:05 Seems transient.
Just won't forget how to spell. And okay, great So Kayla points out our in the contribute issues.
We have a something about. Let's see, here we close the other tabs apologies here as I putz around.
Okay, this right. This one is pointing out that one of the configuration options on sidekick is, I think, configurable as I can an enum or something along like an array. Or let's see, she let's say we have web request with the user is uploading a document.
And for certain jobs there will be different, you know, once for file conversion ones for analytic processing.
And then so there'd be some ability to disconnect the trace when it's for certain types of jobs rather than can contain it on a you know a single parent child trace that way. It would be a new.
you know. There'd be a spam link, I guess. But no, but you know new trace ids, which is I think pretty common because it affects it affects query query performance. You you know you don't some. Sometimes you don't want to load like huge traces. So and then I think I'm opening invoice functionality. Basically, the ask is, can we just have a propagation style setting be configurable via sort of like a ad hoc! You know, lambda, or proc, or whatever my thoughts are, that's fine. It seems like Ariel was saying, that see?
This should belong in the specification. Okay, okay. And then, should it be involved in specification? Yada Yada.
I don't know. I think it's fine to implement make a pick a Pr, and then, like whatever at least, there'd be a reference implementation or something.
but I think it should be. Probably I I'm fine with I I think I'm I've been generally overruled here in the past, but I think it's fine to expose you know custom, you know the ability to write custom proxy stuff on config although it opens up a possibility of sort of like a large foot foot. Sorry large foot guns.
so I don't know. I let's the ask here.
What do you thought so? Yeah, I mean, I I don't know. I don't have strong opinions.
I don't know. Let's see, when we last this has been open since March. So it's been okay. So we probably ought to provide some sort of but okay, I understand the context here. And then, Kayla, a few, you know, weeks ago, commented that you know we should address this because it's a valid question, or actually, that was a month ago. I'm sorry it was March.
So it was. It was due to be deleted, and it was, you know, kept alive, which I think makes sense to do, because it's an unanswered question.
And then there appears to be a reference apologies for rambling here, guys, reference and specification which great this person opened, and it is.
oh, okay, so it looks like at this point we're waiting on some sort of comment from the Mila, who's at azure. But I think we should be open to you know I'm I'm certainly happy to be open to it as a you know.
reference, implementation, language, or something to that extent.
but yeah, it looks like the oh, current comment is that there needs to be, you know. So whatever there so yeah, I mean me personally, like I'm happy to, you know. So whatever review prs there but I I you know, if there's future folks watching, I certainly understand there's some prior context for meetings. So if people you know don't think that belongs in the SDK or or whatever that's I'm not, you know, strongly against or anything. But I'm certainly happy if if what's this person? If sorry, Hazel wants to make a Pr. I think you know, happy to review it and merge it, and, you know, maintain it.
Okay, that's all. Well, I don't know anyone else Juan or Hannah. You just kind of talking into the wind. Sorry.
**Hannah Ramadan** 17:01 No, I think everything you said sounds good. I wish I knew more about that as a topic, to have a strong opinion, but I want, and I feel like if if Hazel is willing to contribute something, and she's open to spec to have more conversation on it, I think you know, supporting her, and what she's trying to accomplish sounds like.
**Eric Mustin** 17:22 Yeah, I mean, I think it's at the end of the day. It's just allowing people to choose an email like it's still only allowing. It's not like we're allowing people to write into like I would understand some more concern, or I think this concern has come up previously. When it's like, Hey, do you want to do this for allowing like per http client, you know.
connection or so, you know, request and so, or like it, to allow a proc for like spit, you know, arbitrary naming of fields like oh, let me take the request, body and like mutate it, and then, you know.
like you can have these explosions in cardinality and so I I don't think this is one of those cases. It feels like it's just letting people choose a you know, a type of propagation style, and we have it in other It seems like we have it in other languages, too, because or this would be something that sorry other. Some of the other libraries. We offer support for, which have, like these sort of Kafka type patterns. I think we'll wanna.
This will be a a common technique used to shorten trace, you know, size or so. Okay, that's all I got and I think I whatever I'll just put we're open to it.
Okay, I don't have any spam next one was Kayla asking about yeah, Hannah your I think this was an open question on your Mrs. Or sorry Getlab. Speak for Prs.
Where?
There's like just weird naming, you know, like formatting and but camel casing, and no one knows why.
**Hannah Ramadan** 19:25 Yeah. Yeah, this was I. I didn't touch anything. Related to actual instrumentation. I just really was looking at attributes. But Kayla came across this. It looks intentional to me. I don't know why, and I wasn't able to find anything, but it does the same.
**Eric Mustin** 19:44 Code block exists, I think, in another library, too. So it yeah.
**Hannah Ramadan** 19:49 Seems like maybe it was meaningful, but.
**Eric Mustin** 19:53 I is it possible on the original implementer?
I would guess it's because when we ported it from whatever library got ported into from this was just, there is my guess.
I don't think there's, you know. I would assume I wouldn't assume it intention to a lot of
**Hannah Ramadan** 20:13 Yes.
**Eric Mustin** 20:14 Stuff in this. Let's maybe check whatever we're at a I don't have any.
not off top of my head. Let's see how much time. Do we have? Okay, we have a few.
So let me just quickly do a test and see if it's in there.
Oh, sorry!
Oh, sorry whoops.
Let's try to search for connect, maybe is that if they're asking why, it just randomly uppercase.
I know that at some point in data, dogs like ingestion. I think we were just in the to save on like storage where you're just upper casing everything or something like that, or down Kit, I forget so that would be my guess.
but let me I'm not very good at searching. Apparently this yeah, there's no incentive.
**Hannah Ramadan** 21:25 Doesn't exist.
**Eric Mustin** 21:26 Yeah. So maybe it's not some intent, something. I wonder I don't know how to search for. How do I search for all uppercase?
okay, I have. No, I have no context here. I wouldn't assume I'm just trying to think of whether this is some sort of breaking change. Sorry. Let me.
I lost my spot.
New idea.
yeah, I would. I wouldn't assume any if if we feel like that's an improvement or standardization that we should make, or it's like adheres to the spec. I think.
it's worth making the change, you know, to like make it whatever there's a preference on what we think it should be. But I don't. You know.
I don't think there was any intention. Is my guess, anyway.
So I left a comment. So auto instrumentation twan did you want to speak on?
Let me?
Yeah, Hannah, I mean, what can I? Is there any, I guess, before we move on? Is there anything we're still open on on Prs. I saw that, for those is rack still open from? I think I owe you a review on rack. Still, is that right?
**Hannah Ramadan** 23:09 Yeah, rack is still open. There were a few more changes that I I spoke with Kayla about for Sinatra and something else where we wanted to make sure the span names that were getting created were in line with.
**Eric Mustin** 23:27 Okay.
**Hannah Ramadan** 23:28 But the new ones where we're dropping think it's just the Http.
I'm from the verb. So yeah, a couple more changes. With that I probably should move it to draft. But the other one should be ready.
**Eric Mustin** 23:41 Okay. Sorry, I know, I said. Last week I've been doing the dumb onboarding stuff. I'm sorry. So.
**Hannah Ramadan** 23:48 Totally good.
**Eric Mustin** 23:49 Prioritize that.
**Hannah Ramadan** 23:50 It's okay. We have a.
**Eric Mustin** 23:52 So today.
**Hannah Ramadan** 23:52 We're gonna do it for the database. So plenty of opportunity.
**Eric Mustin** 23:57 Yeah, that makes sense.
Oh, it's good that I'm glad you're getting time to work on it. I I wish hopefully I'll settle down and be able to more.
speaking okay, so, but cool. So moving on on some small.
I guess. Ariel left some comments as well.
I see you're on your phone. So I'm not gonna attempt to ask you to you know work through them. But and I'm not sure when I'll be returning from.
I think he's on some some vacation or something. So
**Xuan’s iPhone** 24:48 I can. I can. I can work on this.
**Eric Mustin** 24:52 Cool.
**Xuan’s iPhone** 24:52 Yeah.
**Eric Mustin** 24:56 Cool. Yeah, he is. I'm glad I'm glad this is so. Be great to you know, I think.
do you have a concern about last week's issue on who would maintain the some of these gems like is that where, you know? Do you feel like. There's folks in the operator who you need to get a response from, or something like that.
**Xuan’s iPhone** 25:35 No, they they're pretty open to have the it's better, for we have a gem to include everything else.
Something that too separate for them.
So yeah.
**Eric Mustin** 26:00 Okay, yeah. I I'm certainly not up to date, obviously. But except that I saw that you know, people are definitely asking for it of of auto instrumentation. It's nice to see that there are still people out there in Rubyland who so it's cool. I think it's great, I will one day maybe I'll be able to catch up and give you good feedback instead of just cheering, you know our applause. But yeah, this is great. Huh?
Okay, do I need to approve this?
There's an attempt to get what was the question here?
this needs some sort of approval.
Oh, sorry. One second.
sorry about that. I was approving it.
Okay, yeah.
Looks like that's good to go.
I'll let someone else merge it and cool, and so concludes, got 30 min back.
**Hannah Ramadan** 28:08 Nice thanks for driving Eric.
**Eric Mustin** 28:11 I just add nothing to this. I just get to. You know, it's great to see all this open source work. Continue. So yeah, good luck. Everyone.
Okay, stay here.
**Xuan’s iPhone** 28:23 Sure.
**Hannah Ramadan** 28:24 Profile.
**Eric Mustin** 28:25 Great to see you. I'll stop sharing cheers.
