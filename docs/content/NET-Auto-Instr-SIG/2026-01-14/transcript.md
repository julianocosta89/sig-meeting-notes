SIG: .NET Auto-Instr SIG
Date: 2026-01-14
Duration: 19 minutes
============================================================

## Zoom Recording Transcript

**Piotr Kiełkowicz** 04:09 Hey, guys.
**Zach Montoya** 04:29 Hello.
**Piotr Kiełkowicz** 04:30 He sucks.
Do you want to drive, or should I do this?
**Zach Montoya** 04:35 Do you want to take it today?
**Piotr Kiełkowicz** 04:36 No, but I will do that.
So… Some heads up from my side, spark needs to release,
new version of distribution shortly, kind of this month, and it is our plan. And we would like to include most of the changes from the upstream, so I would like to make a release of the instrumentation.
Next week?
I'm just after a short chat with Rash, and it will be great to include also a new version of the SDK.
Here, but it will be confirmed on the… next Tuesday.
So, that's a short plan.
**Rajkumar Rangaraj** 05:41 Yeah, I agree, Pierre. The only thing I asked to wait till Tuesday is… I know there is a SQL RC recently released, right? So I don't know how the versioning changes happens with that, so that's the conversation I need to have with there.
**Piotr Kiełkowicz** 05:58 Sure.
**Rajkumar Rangaraj** 05:59 Yeah, that's why, if not, we could have just gathered all the maintenance in a Slack, and if it needs to be done earlier than that, we can have a Slack discussion with all of the maintenance to see.
But I'm supporting.
**Piotr Kiełkowicz** 06:15 Let's say next Tuesday is perfectly fine, from my perspective.
**Rajkumar Rangaraj** 06:19 Okay.
**Piotr Kiełkowicz** 06:21 needs to… Need to log in.
Okay, let's back, so… Puerto Ricquist.
I'm not sure if you were able to…
We review all notifications, kind of.
If no, mapping kind of improved our…
security, compilation security for Windows libraries. There is ongoing stuff also for Delinooks.
And we were able to… let's say, enable core WCF instrumentation with, kind of, big changes.
And I think from the kind of feature perspective, we have only this one open right now.
It is related to the MongoDB 3.5 support. Zach, if you will be able to review it, it will be great.
I've looked into Datadoc code, and I know that you have it already, but…
**Zach Montoya** 08:09 Yeah, I can… I can take a look. I'll… I'll have a review before the next time I meet.
**Piotr Kiełkowicz** 08:14 Cool, thank you.
What else? There is a lot of,
Out of the… this one is related to flackiness of the core WCF test, unfortunately, but I'm not sure if it will go this way. I have other options on the plate.
That's all No, no, for now.
new issues… Discussions.
Non-discussions and issues.
As I mentioned, Martin also is working on
On this, it is kind of…
Security fixes for all the library and memory management.
I think we can include into the next release.
Based on what I see. If not, I will… Postpone to 1.15.
I think, Alexei, we are still looking for the prototype, yes?
**Alexey Pukhov** 09:47 Yep, yep. I know I promised to do something by today, but I'm almost done, so today I'll be posting the draft.
**Piotr Kiełkowicz** 09:55 Cool, thank you. So, I will put it to the release one… For the 115, hopefully.
**Alexey Pukhov** 10:07 Hopefully…
**Igor Kiselev** 10:12 Multiple.
SV…
earlier, it might be a good idea for that change to be released as a separate release, as a beta, to include all of the change and nothing else, as it would include a lot of change to
Layout of files, and… Multiences included.
**Piotr Kiełkowicz** 10:34 Sure. I agree that we can make the…
Release, let's say, next week, and merge your… these changes to the… to the main branch, and make the follow-up with the beta.
Especially if it is kind of crucial change, and it would be great to bottlene test that before February release.
Yevgeny, do you think that we… Needs to do anything here.
**Yevhenii Solomchenko** 11:10 I think not. We should wait for answer from customer.
**Piotr Kiełkowicz** 11:19 I will ping him a sign, and… Close next week.
Still waiting for the… Tips to reproduce.
I think we should do the same queue.
I will ping Steve in private channel also.
And what else? I hope it's asking that this… It's all new issues… discussions already.
Handbooks,
Everything's fine, and I'm not sure if we need to make any changes here. I think this one is in progress.
I cannot hear offline, sorry, Evgeny.
I think that… that's all what we have right now.
And it got news, topics, Or bad news.
**Chris Ventura** 14:23 I'm still in a very busy season, so…
My… if you need something directly from me, just reach out directly.
**Piotr Kiełkowicz** 14:33 Sure.
Thanks.
So, see you next week. Thank you.
**Zach Montoya** 14:43 Alright, thank you.
**Yevhenii Solomchenko** 14:45 Thank you, I'm Brian.
**Alexey Pukhov** 14:46 Thanks, everyone.
