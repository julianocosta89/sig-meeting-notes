SIG: Zig SIG
Date: 2026-10-14
Duration: 45 minutes
============================================================

## Zoom Recording Transcript

**Giovanni Panice** 02:36 Hold on.
**Francesco Gualazzi (OpenTelemetry)** 02:38 Good afternoon, Javan, how are you doing?
**Giovanni Panice** 02:41 Do you hear me, Fran?
**Francesco Gualazzi (OpenTelemetry)** 02:43 I can hear you, ok, do you hear me?
**Giovanni Panice** 02:45 Yes.
**Francesco Gualazzi (OpenTelemetry)** 02:46 Okay, nice.
Hello, what's up?
**Giovanni Panice** 02:51 All good, all good.
And you? What about you?
**Francesco Gualazzi (OpenTelemetry)** 02:56 Nothing special, I guess.
Everything is okay. I was working on a couple of interesting things, for my job?
And I discovered the bug in the The metrics aggregation.
Although I.
**Giovanni Panice** 03:15 the.
**Francesco Gualazzi (OpenTelemetry)** 03:15 Yeah, okay.
**Giovanni Panice** 03:16 This famous big bug.
**Francesco Gualazzi (OpenTelemetry)** 03:19 It's not that big, but the problem is that it could, to say, no, it does… Create an imbalance, let's say, in the, in the exported metrics, so yeah, I'm working on a fix.
Other than that, I'm happy that we landed the WGV-IIIC support, that's great.
And, we were able also to Fix a couple of things, if I'm not mistaken… In the, yeah, there is a bug that also fixed in the exporting that was reported by Caught this, so I think that that's Francesco Consulto, no? Yes?
**Giovanni Panice** 04:06 Yes.
**Francesco Gualazzi (OpenTelemetry)** 04:07 Your fellow Neapolitan Francesco Consulto.
**Giovanni Panice** 04:12 He's a super nice guy.
**Francesco Gualazzi (OpenTelemetry)** 04:15 Yeah, yeah, yeah. So… yeah, nothing, nothing more than that.
**Giovanni Panice** 04:21 I have only one point. You know, there is… I don't remember the name, let me check… Buck Garage, no? Yeah, yeah, Buck, yes. An example, okay? Some… from OpenTelemetry asked us some question, okay? The one related to the… The maturity of the project, okay?
**Francesco Gualazzi (OpenTelemetry)** 04:48 Yeah, yeah, yeah.
**Giovanni Panice** 04:49 So.
Well, in my opinion, I mean, we should say that we are, as we said, we should wait for the OpenTelemetry, so for the Protobuf, okay?
**Francesco Gualazzi (OpenTelemetry)** 05:03 Yeah, yeah, yeah, no, I replied in the same thread that we want to…
**Giovanni Panice** 05:07 You replied on the… No, but no, no, no, there is also a full request. Oh.
**Francesco Gualazzi (OpenTelemetry)** 05:12 Is that okay?
**Giovanni Panice** 05:14 Yes, let me show you, so…
**Francesco Gualazzi (OpenTelemetry)** 05:16 Please share your screen. I didn't see the pull request.
**Giovanni Panice** 05:18 Okay.
So… Do you see?
Sorry.
Hmm?
together.
**Francesco Gualazzi (OpenTelemetry)** 05:28 No, not anymore.
**Giovanni Panice** 05:31 Let me… Okay, maybe now, yes, so…
**Francesco Gualazzi (OpenTelemetry)** 05:37 Okay.
**Giovanni Panice** 05:43 Okay, do you see him?
**Francesco Gualazzi (OpenTelemetry)** 05:45 This is for the demo.
**Giovanni Panice** 05:47 Yeah.
**Francesco Gualazzi (OpenTelemetry)** 05:48 yeah.
**Giovanni Panice** 05:48 Okay, and I mean, apart from little stuff that me and Antoine answered, okay, the main question is, which is reasonable, okay? He said, okay, what is your perspective on this? Do you think that implementation is stable enough to bring it to the demo project?
**Francesco Gualazzi (OpenTelemetry)** 06:06 Yeah, I not yet. My answer would be not yet.
**Giovanni Panice** 06:11 Yeah, yeah, Well, you know, hmm… okay, because I mean, I don't…
**Francesco Gualazzi (OpenTelemetry)** 06:17 I don't know, let me know what you think, but my gift…
**Giovanni Panice** 06:20 The problem is that, I mean, I don't want to lose the enthusiasm of Bach, because, I mean, he opened it, he created the, you know, the demo, which is, I mean…
**Francesco Gualazzi (OpenTelemetry)** 06:30 I know, yes.
**Giovanni Panice** 06:31 So, I don't want to say, hey, we should wait a bit.
Maybe, I mean, I know that we merged the stuff from Antoine yesterday or two days ago, I think, if I remember well.
**Francesco Gualazzi (OpenTelemetry)** 06:49 Mmm… two days ago… yes?
**Giovanni Panice** 06:53 I mean, what is missing from your opinion from two mergers to the stuff related to Protobuf?
**Francesco Gualazzi (OpenTelemetry)** 07:01 Oh, no, well, yes, there is 1, there is 1, 1, open item with, There is one open item with, with the Protobuf support, and, And I don't remember where we are with that, I think it's ready to be, ready to be merged, I guess, I don't remember, but I have to check, so Antoine created 1 PR.
**Giovanni Panice** 07:30 Yeah, I remember. Yes.
**Francesco Gualazzi (OpenTelemetry)** 07:31 Yes. Okay.
**Giovanni Panice** 07:34 In a pull request for the 0.17.
**Francesco Gualazzi (OpenTelemetry)** 07:42 Okay.
No, that's… but there's another one already that is, Hope in draft and it has the gRPC lib support.
**Giovanni Panice** 07:57 Okay.
**Francesco Gualazzi (OpenTelemetry)** 07:58 Okay, so that one…
**Giovanni Panice** 08:00 Absolutely.
**Francesco Gualazzi (OpenTelemetry)** 08:03 That one is also ready, I think, but I didn't see I didn't I didn't review yet. That's that's the problem.
**Giovanni Panice** 08:11 What I'm trying to say is that if we are like Wix.
From releasing a first alpha.
Maybe we can say, hey, we are more or less ready, we can wait a bit, you know, so leaving there the question and say, hey, we are ready. Or we can say, we need some more time.
**Francesco Gualazzi (OpenTelemetry)** 08:34 I… I don't think, honestly, that we can… that we can call it.
**Giovanni Panice** 08:38 Yeah, we can answer that we are still, we are still, Working on, and we should wait a bit more, okay?
**Francesco Gualazzi (OpenTelemetry)** 08:48 Yes.
Okay.
Just so that…
**Giovanni Panice** 08:58 Okay, so I'll answer.
**Francesco Gualazzi (OpenTelemetry)** 09:00 Okay.
**Giovanni Panice** 09:00 like.
**Francesco Gualazzi (OpenTelemetry)** 09:01 So also because again, when we want to do alpha release.
We also have to synchronize the documentation. So there's a bunch of things that needs to happen.
On top of, on top of just having a stable SDK. Right.
**Giovanni Panice** 09:18 Okay, so currently we are still working on some major stuff.
In order to have a kind of stable release, alpha release.
I don't know, I want to say stable, alpha is not so stable, kind of alpha release.
We can say Alfa Renisa.
for the OpenTelemetry Zig.
SDK.
**Francesco Gualazzi (OpenTelemetry)** 09:51 SDKs…
**Giovanni Panice** 09:52 So it might be, so.
We… so we can wait, to… Wait, the, the first release… To complete them.
Something like that.
**Francesco Gualazzi (OpenTelemetry)** 10:17 I think that's reasonable, yes.
Hello? You still there?
**Giovanni Panice** 10:44 Yes. No, I'm fixing it… Into my… Yeah.
Exactly, so I think it's okay, no, as answer.
**Francesco Gualazzi (OpenTelemetry)** 11:03 Yes, yes.
**Giovanni Panice** 11:04 Okay.
Okay, so this is… All from my side, I don't know if you have any other things, comment.
**Francesco Gualazzi (OpenTelemetry)** 11:14 No, honestly, no.
**Giovanni Panice** 11:16 Okay,
**Francesco Gualazzi (OpenTelemetry)** 11:18 Antoine will be joining in a couple of minutes. He said he was a bit late.
**Giovanni Panice** 11:21 He will join, we can wait him, so if,
**Francesco Gualazzi (OpenTelemetry)** 11:24 I don't have any other topics. Actually, I need to update the document still.
**Giovanni Panice** 11:31 If you don't mind, I'll send you a link, I'll send you a Google Meet.
Because I want to talk to you about a thing.
**Francesco Gualazzi (OpenTelemetry)** 11:40 Right now? Like…
**Giovanni Panice** 11:42 After the meeting.
**Francesco Gualazzi (OpenTelemetry)** 11:44 I have a hard stop at half past five because I have to go to my daughter's.
**Giovanni Panice** 11:50 One minute, one minute thing, as usual.
**Francesco Gualazzi (OpenTelemetry)** 11:52 Okay, well, we know what we can do. Call me on Telegram after…
**Giovanni Panice** 11:58 could.
**Francesco Gualazzi (OpenTelemetry)** 11:59 Nice. After we leave this meeting. So… I'm generally happy about the status of the project, honestly, I think…
**Giovanni Panice** 12:07 Cool!
**Francesco Gualazzi (OpenTelemetry)** 12:07 the.
**Giovanni Panice** 12:08 We have, we have already some contributors, we, there is a lot of interest, Antoine is doing a great job, you are driving a lot, very well the, all the discussion and all the things, so… Actually, we are… It's, In a good status, in a healthy status, from my point of view, honestly. So…
**Francesco Gualazzi (OpenTelemetry)** 12:37 You are the, you are the pro, you are the expert of open source, not me.
**Giovanni Panice** 12:48 Well, the next year, what we can do, if you want, we can participate to some mentorship program.
And, you know, we can have some, you know, contributors from Linux Foundation or Google Summer of Code and get them to contribute some part of the library. So if we have some idea for some project.
Looks good.
We can propose it, so…
**Francesco Gualazzi (OpenTelemetry)** 13:20 Fine.
So, let me think, what are we trying to achieve?
I think not much other than what we just discussed last time, no, so.
**Giovanni Panice** 13:36 Let's wait for Antoine, if Antoine cannot join.
**Francesco Gualazzi (OpenTelemetry)** 13:40 No, I can, I mean, but this is gonna just, just gonna be late.
No, no one has… Have you been able to see the recent code changes in the code base or you've been too busy with something else?
**Giovanni Panice** 13:55 I've been very busy, and so I want to, to… take some window on some cycle for the project, because I'm too… I have to take a bit, you know, some… I'm losing a bit of the, you know, the, the status, so I want to follow a bit more, ok so, I'll, I think, Not the next week, but the other one, maybe I can give some… take some things to… .
on the… Take some issues, or take a look to the overall status, or…
**Francesco Gualazzi (OpenTelemetry)** 14:38 Okay.
**Giovanni Panice** 14:40 But, yes, I see the messages, I see things around, and they're honestly really good, so…
**Francesco Gualazzi (OpenTelemetry)** 14:50 Well… And what about your, adderhood. Adderhood, yes, that's the word.
**Giovanni Panice** 15:01 Well, she drains me a lot of energy, but I'm very happy about that. So, all the energy that I'm happy to share with my family, so…
**Francesco Gualazzi (OpenTelemetry)** 15:13 This is awesome.
**Giovanni Panice** 15:20 The other day I saw the son, the son, the Mario's son.
To do a vacation, to see him, obviously, you know, by photo and videos, no?
**Francesco Gualazzi (OpenTelemetry)** 15:38 The new one,
**Giovanni Panice** 15:39 Yeah.
**Francesco Gualazzi (OpenTelemetry)** 15:40 Don't remember his name.
Are you ready for the discussion?
**Giovanni Panice** 15:44 you.
**Francesco Gualazzi (OpenTelemetry)** 15:45 I know it ends with Pio.
**Giovanni Panice** 15:47 In any case, in any case, he looks like his father.
**Francesco Gualazzi (OpenTelemetry)** 15:54 Oh yeah, for sure.
We're all gotten very old, huh?
**Giovanni Panice** 16:06 I wanted to… I wanted to talk with you, but I don't have a cycle to… to… To give some energy again.
I know that Christoph is a bit… Who's Christoph?
Christopher… Christopher… The.
From the Zig Foundation.
Dolores.
**Francesco Gualazzi (OpenTelemetry)** 16:32 Loris, yeah, yeah, yeah, yeah, okay.
**Giovanni Panice** 16:34 Loris is a bit, doesn't like the FOSDEM conference.
**Francesco Gualazzi (OpenTelemetry)** 16:44 Okay.
**Giovanni Panice** 16:44 Well, maybe the next year. I wanted to, I mean, I wanted to talk about you, about that, but we can try to do a call for the room.
Call for the room, I call for the room for Zig room.
**Francesco Gualazzi (OpenTelemetry)** 17:01 That looks good, yeah I mean, oh, Antoine, that, that is, that would be an interesting thing I don't remember who already asked me that there was someone who asked me that.
Oh yeah, now I do remember Pietro Peter Longo.
He messaged me on Telegram.
**Giovanni Panice** 17:18 And.
**Francesco Gualazzi (OpenTelemetry)** 17:19 The exact same thing this youth just said to me.
And, and I, and I had to reply, look, I, it's difficult for me to go to Fosden because, that's the period where my My family mostly is gathered together because of Birthdays, and, you know…
**Giovanni Panice** 17:36 Yeah.
**Francesco Gualazzi (OpenTelemetry)** 17:37 But, if I find someone who is interested, I will let you know, so I will let him know that you would like to do the same, but you, you do, you do go regularly or to fast?
**Giovanni Panice** 17:48 I go every year to do FOSDEM and this year I have a call for the dev room for data streaming dev room.
**Francesco Gualazzi (OpenTelemetry)** 17:56 Hey.
**Giovanni Panice** 17:57 So maybe the next year we can, if we can have, you know, we can create a committee and we can launch a Zigroom.
**Francesco Gualazzi (OpenTelemetry)** 18:09 And that's why you said that you started with Lovis doesn't like the format because you.
**Giovanni Panice** 18:13 Yeah, because he doesn't like the format. He doesn't like the format, he doesn't like the FOSDEM as a place.
He has a very strong opinion about that, but usually the Fortem is really open for… to give rooms for languages, especially the one… Like, you know, in early stage, like Zig.
And, you know, there is a, we say, Gurum, for example.
So…
**Francesco Gualazzi (OpenTelemetry)** 18:44 Okay.
**Giovanni Panice** 18:47 Antoine.
**Francesco Gualazzi (OpenTelemetry)** 18:49 We can discuss that later, when we…
**Antoine Gagniere** 18:53 Hello?
**Francesco Gualazzi (OpenTelemetry)** 18:54 Bye, Lee.
**Giovanni Panice** 18:56 We are talking about one project for the 2028, if you are interested.
**Antoine Gagniere** 19:02 What?
**Giovanni Panice** 19:03 No, we were… I was saying that maybe in the 2028, we can, do the call for the room for the FOSDEM in Bruxelles. Okay.
**Antoine Gagniere** 19:14 Yeah, I see.
**Francesco Gualazzi (OpenTelemetry)** 19:15 That would be nice.
So other than that, again, I don't think we have, main topics to discuss with regards to the special interest group. It's just, an understanding of.
Where we are with the… with the various status of things, and therefore, Yeah, nothing, nothing special more than that. So we, we just landed W3C trace propagation from Bach.
And that allows us basically to Run the hotel demo project. But, but, we also… need a release, you know, an alpha release, and to do the release, I would like to first have some proper, handling of some bugs that we still have. For example, I discovered one earlier, and yeah, we need to fix it.
Mmm… That said, yeah, it could be. It could be. I'm not saying that it will be, but I will be positive and say that it could be that we have a release in, I don't know, a couple of months. So before the new year.
You know? Because, because, yeah, I'm just… I'm just… Thinking that we will fix the bugs, we will be able to explore maybe a couple of more features that needs to be there once the gRPC support is completed.
And then, yeah, and then I think it's, it's all, roses and, and champagne, as we say.
It's gonna be, it's gonna be easier than we think, I suppose.
Yeah. So, that was basically what we just said.
You didn't lost much of the conversation.
**Antoine Gagniere** 21:20 Yeah, so I worked on GRPC this weekend, and now I'm on the… I'm… My packages are assuming 0.17 now.
Okay. And so, I made the 0.17 pull request in Hotel SDK.
**Francesco Gualazzi (OpenTelemetry)** 21:41 Beautiful.
**Antoine Gagniere** 21:42 And it's only blocked because of the… The flaky test. That's what you know. There's a race condition pull request.
It's…
**Francesco Gualazzi (OpenTelemetry)** 21:51 Oh, the one, yes. That one might be fixed by my PR, actually.
**Antoine Gagniere** 21:55 Possibly, yes. Yeah. So, and so the 017 pull request is not, is ready for review, actually. It's just I have one failing test because of this.
Flaky test, so… Would.
**Francesco Gualazzi (OpenTelemetry)** 22:11 Would you… would you try to rebase on top of my PR, or do you think we should merge mine first?
**Antoine Gagniere** 22:18 Well, we can merge,
**Francesco Gualazzi (OpenTelemetry)** 22:21 So.
**Antoine Gagniere** 22:22 I mean… but… So.
Let me see…
**Francesco Gualazzi (OpenTelemetry)** 22:28 Mine is 116 and yours is 115.
And in my PR, what I do basically is I fix the Batching processors.
By applying, a synchrony pattern from the standard library, plus a mutex. So, you can see that the shutdown now does lock uncancellable on the I.O.
And then waits to be waked.
If there is an ongoing export task.
So… Yeah.
**Antoine Gagniere** 23:07 Cool.
What does he wait for?
Big.
**Francesco Gualazzi (OpenTelemetry)** 23:14 So the problem here was that, we don't, we don't wait for the export to complete.
Before shutting down, right?
With this one, we do wait because we set this mutex, and the mutex is just waken only when the export is completed.
**Antoine Gagniere** 23:46 But so I why don't you see?
modify the… export.
Cool. Function, then.
**Francesco Gualazzi (OpenTelemetry)** 23:55 There is no need, huh?
**Antoine Gagniere** 24:02 Okay, so, okay, because, so in my other PI, the spec shows So, yeah, when you shut down, actually, you want to force flush before, no?
**Francesco Gualazzi (OpenTelemetry)** 24:18 Mmm… yes.
**Antoine Gagniere** 24:20 Yes, there's force flush, and there's shutdown. Shouldn't… Like, yeah, what's the difference between them? Why do the two exist?
**Francesco Gualazzi (OpenTelemetry)** 24:32 I have to check.
Give me a sec.
**Antoine Gagniere** 24:36 Because, yeah, I appear to have the same issue, but about force flush happening at the same time as another export. So there was two exports happening at the same time.
And it's not permitted by the spec.
And so we.
Good.
I made it sequential.
**Francesco Gualazzi (OpenTelemetry)** 25:00 Okay, let me see how you do this.
**Antoine Gagniere** 25:02 And so we.
My PR makes it so that the force flush waits for all other exports.
To finish before returning.
But so I'm wondering if your shutdown comes after a force flush, then it also solves the same issue, but very differently. So That's where I'm… Surprised.
**Francesco Gualazzi (OpenTelemetry)** 25:32 Hmm.
**Antoine Gagniere** 25:48 But okay, anyway, I just want… meant that the O17 pull request is ready to review.
The test is just… so we're both trying to fix this flaky test anyway, so… Yeah.
**Francesco Gualazzi (OpenTelemetry)** 26:07 Okay.
By the way, and I have to go in five to ten minutes because I have Your daughter's daughter's school thing. Honor.
So yeah, I… I am super happy where we are, I was saying. And if we can get these bugs fixed, and the gRPC support, then we are… Let's say days or weeks away from the first working release.
I suppose.
That said, That's sad. What do I want to say? Oh yeah. Why is your gRPC PR still in draft? Do you need to make adjustments or
**Antoine Gagniere** 27:04 Yeah, I did a lot of improvements on the packages below, and so…
**Francesco Gualazzi (OpenTelemetry)** 27:10 Okay.
**Antoine Gagniere** 27:10 I will want to rebase on O17.
**Francesco Gualazzi (OpenTelemetry)** 27:14 Okay. Okay, so you want to migrate to 17 before, okay.
**Antoine Gagniere** 27:17 Yes, before merging GRPC, yes.
**Francesco Gualazzi (OpenTelemetry)** 27:20 Okay.
Looks good.
Yeah.
**Antoine Gagniere** 27:24 It's going to build statically by default. It's what you wanted, I think.
**Francesco Gualazzi (OpenTelemetry)** 27:30 Yes, yeah, that's, that was one of my worries when we import… when we started importing, when we said that we would have started importing some, Some libraries, so… I think it's sorted out by now.
**Antoine Gagniere** 27:44 And it will be configurable.
Snoops.
**Francesco Gualazzi (OpenTelemetry)** 27:48 Good.
Awesome. Yeah, then, I think that's all. I don't know if you have any more things. Let's go ahead with the… with building the PRs and fixing the bugs, and then we just roll with it.
**Antoine Gagniere** 28:01 Yep.
**Francesco Gualazzi (OpenTelemetry)** 28:02 Beautiful.
See you next time then.
Enjoy your day.
**Giovanni Panice** 28:07 I.
**Francesco Gualazzi (OpenTelemetry)** 28:07 Cheers. Bye.
