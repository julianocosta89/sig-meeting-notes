SIG: .NET Auto-Instr SIG
Date: 2025-07-02
Duration: 25 minutes
Zoom Recording URL: https://zoom.us/rec/share/1H0f4GbSULUJwExxVRtPG3fvQUDyOZgIPR8_jzYdihfWa7z__JYr6c8ycKC4Pxbe.3tY0FMHbJAa6pjzn
============================================================

## Zoom Recording Transcript

**Paulo Janotti** 02:50 Hi, folks, almost 9 or 3.
Oh, start to share. And we get started.
Okay, 9 0, 3. Let's get started. So, Rasmus, you are bringing up a topic
related to one of the Prs.
**Rasmus Kuusmann** 03:40 Yeah, the Pr was itself closed already. So, and
seems the autobot doesn't have any rights to committer.
**Piotr Kiełkowicz** 03:54 I think the best. What you can do is to ping trust on slack channel
to double check this. I do not have longer admin access to the settings, and
based on. Because of this, it will be the the easiest way to proceed.
**Rasmus Kuusmann** 04:17 Okay.
**Paulo Janotti** 04:18 Yeah, teresca is the one that has been coordinating all of that. So yeah, the best thing. And I think he is in pacific time time zone. So now you'll be a great time to ping him.
All right. Let me.
Oh, let me skip the the fillerbox ones. We have quite a few of them.
So this is the one to fix the flushing on the log.
**Piotr Kiełkowicz** 05:18 We have discussed it. Yes, last week.
It will be great to have the
second opinion for me. It looks good, but is kind of crucial part, so double check.
**Paulo Janotti** 05:35 You. You had a you had a specific question to Chris. Chris. I'm not seeing Chris here. Oh, no.
**Chris Ventura** 05:43 Just joined. Sorry.
**Paulo Janotti** 05:45 Yeah.
**Chris Ventura** 05:47 So what's this question
**Piotr Kiełkowicz** 05:51 You were interested in fixing this bug before the release, so Pr. Is ready, and.
**Chris Ventura** 05:58 Okay.
**Piotr Kiełkowicz** 05:58 If you could take it would be great.
**Chris Ventura** 06:01 Yeah. I took a look at the draft pr
previously, and one of the things that stood out that I'm not quite understanding why we have to do it is so. We now had to add these try finally blocks a lot around a lot of the logging code.
And so in that. Finally block, we're trying to release some sort of resources I'm assuming to forcibly flush
the data.
And it's not clear to me why we have to introduce that behavior? Is it to make tests pass, or is it
because it it won't ever get flushed.
**Piotr Kiełkowicz** 06:45 For now we are writing directly to the disk, so if something fail, we hit, we still have, everything written to the file and stored
more or less. Everything last. The only last message can can be fake.
And now, we are changing to write disk to periodically, I think every 5 seconds.
If all internal buffers, or if
all internal buffers are not full before this time, so
if anything wrong happen before we dispose locks, we'll be losing this part
of the data, and it can be crucial data
especially on the start time. So the final finally.
so we have added finally blocks to prevent this
important scenario. When we are start we are starting the application, and something may wrong may happen to ensure that it will be locked.
**Chris Ventura** 07:56 Okay? So so that try finally, block is to handle some of the more critical startup scenarios.
**Piotr Kiełkowicz** 08:04 Yes.
**Chris Ventura** 08:05 Specifically, and we don't need it for
most of the other locations where we're
persisting logs. Okay, I think that's a reasonable trade-off.
**Piotr Kiełkowicz** 08:17 And, as I remember, because I 1st did kind of
2 days ago, as I remember, it is related only to startup hook and load their stuff.
**Chris Ventura** 08:32 Okay? And then I guess, another
alternative approach that we could consider
honestly can't tell you if it's better or not.
I believe Sarah log has a Async logger
that basically, you take your log messages. It pumps it to another thread, and then that thread is responsible for handling the disk rights
**Piotr Kiełkowicz** 09:05 Maybe I I was not checking this. I
I will pass this comment to to matteous.
**Chris Ventura** 09:14 Yeah. And honestly, if we just wanted to get something out the door. Now.
I I'm fine with this approach, but I just know that
I mean, Sarah Log has a lot of options. It's big.
So there's different things that can be considered.
**Paulo Janotti** 09:33 So it seems. And by what you just said, Chris.
let's try to take kind of the small gains right now
and file follow up issues. So then we can prioritize.
**Chris Ventura** 09:51 Yeah. And I think that's fair.
**Paulo Janotti** 09:55 All right.
**Chris Ventura** 09:56 I should have some time today to take a look at this.
To to do a final review pass.
But yeah, we talked about the main thing that I didn't quite understand, just from the Pr.
**Paulo Janotti** 10:18 All right.
So any updates for this one or we mentioned last week.
**Piotr Kiełkowicz** 10:40 Still in progress. The guinea is working on additional tests and additional handling additional environmental very ups by the file configuration.
**Paulo Janotti** 10:53 Okay.
what's holding up the deals? One.
**Piotr Kiełkowicz** 11:09 I have another chance to review this, and
it needs some adjustments. It is not.
Maybe my suggestion was not clear enough.
No.
yeah.
**Paulo Janotti** 11:29 So so basically, it's still a draft. And it's still need further review. For us to.
**Piotr Kiełkowicz** 11:37 Yeah, progress on that.
**Paulo Janotti** 11:40 And this is the one that materials have discussed it with us
a few times I talking about perhaps eventually kind of a demo of
what we are capturing here the stacks that are collected. I think you'll be helpful to provide more the context.
And yeah, the this this one had you. Do you wanna add anything about it? We already discussed it.
**Piotr Kiełkowicz** 12:24 It's still on my to do list. But
basically, yeah, the 1st point from the previous comment is, what is my goal at the beginning.
**Paulo Janotti** 12:41 Okay.
**Piotr Kiełkowicz** 12:45 Neural has similar functionality based on the comment from your users.
**Chris Ventura** 12:50 Yeah, similar functionality there.
We don't allow them to add dynamic information to to our instrumentation.
So there's some slight differences between the hotel instrumentation and the relic instrumentation.
But they're they're very similar. We have this concept of a transaction which is
more like a collection of spans within a a request, a single request, and we have separate
custom instrumentation that allows you to create transactions or to create spans. And we require you to create a transaction before you can create a span.
But we don't allow you to dynamically add data from the method being instrumented
into that span or transaction. We have some separate Api methods
that you can use if you've already created a transaction or span to to add those details.
but that that, of course, requires code access. And so we don't provide a codeless way for them to add that that data. So it still aligns with with what you're
proposing here.
It would be neat to be able to do some simple things like adding attributes to span like hard coded attributes to spans and and things like that.
I think that would be great. It's just any of that dynamic stuff that I think is going to be a lot harder to do from the no code perspective.
**Piotr Kiełkowicz** 14:45 I'm not sure if it will be required. I need to double check with with our Pm's. If this dynamic part is crucial or just static way will be cool enough.
**Chris Ventura** 14:58 And and I know that, at least for us, the static way has gotten us.
It's worked! Worked fairly well for us.
and then kind of the fallback is for for anyone that really needs more.
The having to make some code changes has been an okay trade-off so far.
**Piotr Kiełkowicz** 15:26 I'm in general. If if you, if you can modify the codes
and you still want to use auto instrumentation is pretty straightforward activity source and adds activity source to the environment. And you have it so.
**Chris Ventura** 15:44 Yeah.
**Paulo Janotti** 15:52 All right.
And this concludes the known detail about Prs.
**Piotr Kiełkowicz** 16:02 One more comment to Prs. They are failing.
all of them. There is some issue with installing package on the Ubuntu 16. I think
I don't have time to investigate it.
**Chris Ventura** 16:15 I know there was an issue reported by Ubuntu.
and I think the last time I checked it was recently resolved.
But on the Ubuntu website. There was an issue reported.
**Piotr Kiełkowicz** 16:31 Could you please share the link.
**Chris Ventura** 16:33 Let me let me find it again.
Okay, I found it.
**Piotr Kiełkowicz** 17:04 Interesting.
**Paulo Janotti** 17:08 Do do you wanna share? I can stop sharing.
**Piotr Kiełkowicz** 17:16 Hmm.
**Chris Ventura** 17:18 I don't. I don't really have anything to share from it. I was just aware that an issue was reported
because the team members said, Hey, our Prs are failing, and it looks like it's because of this ubuntu incident.
I honestly haven't had a chance to look. I've been in meetings all day.
**Paulo Janotti** 17:44 All right. There is something here asking me to reload.
Okay.
okay.
It seems fine from my perspective here, but
let me know if it disappear. Like.
okay, I think, Yvonian identified something here.
Oh, okay.
I output later.
So
let's keep waiting, I think. Mike has already worked with the files in the past. And
I I guess it's just a matter of time until he can get back with the info. So
what I was most did you have a chance to look at these or not? Yet?
**Rasmus Kuusmann** 19:52 Not yet possibly today.
**Paulo Janotti** 19:56 Okay. So I will leave as it is. And after your update we we track on next meeting.
**Rasmus Kuusmann** 20:03 Sure.
**Paulo Janotti** 20:07 We were waiting, I think. Mathils still didn't have time to follow up on that.
He is not today here. So let's keep there, and this is
**Chris Ventura** 20:24 Paulo for the flooding the logs thing, should we? Just schedule that for the the next release.
**Paulo Janotti** 20:32 Yes, definitely.
Yeah. I'm I'm I'm forgetting to to do that. Those steps.
**Chris Ventura** 20:44 Me, too!
**Paulo Janotti** 20:47 I think Rasmus was just back. I don't think you have anything to say about this or any updates in this regard, and to be fair, I think. When
rajes back, then perhaps he may also have some additional info there.
just in light of the same thing. I think we can put on Vmax.
and I'm not gonna add to the project for now, just
okay.
Nothing new here.
nothing new here.
I think the question is mostly to poetry.
How we are looking for a new release.
**Piotr Kiełkowicz** 22:08 No, I think when this fix for logic is merged we can cut off the release.
**Paulo Janotti** 22:16 Okay? So from the side of the SDK, everything is done we just need to to really publish all get the fixes that we want to then publish.
Okay, sounds good.
**Chris Ventura** 22:33 Yeah, if I can get to that Pr today, and things look good. Then you might be free to take care of things tomorrow.
**Paulo Janotti** 22:44 Sounds very good.
**Chris Ventura** 22:48 There was an issue that was worked on that.
I I think we are leveraging the hotel bot to handle some some of the updates in our repo
did all of the permissions issues get resolved for for that one? Or is that still an ongoing thing?
**Piotr Kiełkowicz** 23:09 Have discussed at the beginning, and Erasmus will Ping trust.
**Chris Ventura** 23:14 Okay.
**Piotr Kiełkowicz** 23:14 To help with this.
**Paulo Janotti** 23:16 Yeah, so it's not solved yet. But we are gonna track that.
**Rasmus Kuusmann** 23:20 Yeah.
**Paulo Janotti** 23:21 Sure.
**Rasmus Kuusmann** 23:21 Is in a vacation. So.
**Paulo Janotti** 23:24 Oh!
**Rasmus Kuusmann** 23:26 May.
**Paulo Janotti** 23:31 Yeah. And also use the slack, because this should be affecting other project, too. Right? So.
**Piotr Kiełkowicz** 23:41 Now it is our change.
**Paulo Janotti** 23:44 It's only our change. Okay, so yeah.
**Piotr Kiełkowicz** 23:47 But if it is not fixed, it is not a blocker, for anythingnet installation is working with a bit older scripts than previously.
Interesting.
**Paulo Janotti** 23:58 Yes, yes, that's true.
Okay, that covers the agenda.
anyone wants to bring something up for we closing perhaps very short. Today, I think we have a a couple of longer ones. So it's fine to have a shorter one today.
**Chris Ventura** 24:28 Yeah, I'm still behind on reviewing Prs, because, yeah, my workload increased.
So just like this logging one. If there's something you need me to take a look at, sooner feel free to reach out.
**Paulo Janotti** 24:48 All right, I hear silence. So then let's wrap up see everyone next week. Then.
