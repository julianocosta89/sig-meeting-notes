SIG: OpenTelemetry .Net Auto Instrumentation SIG
Date: 2026-09-02
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Piotr Kiełkowicz (Splunk Inc.)** 08:47 Hey, guys.
**Alexey Pukhov** 08:53 Hi.
**Piotr Kiełkowicz (Splunk Inc.)** 09:11 I think we can start, so I'll try to find the… Pied with the notes.
I think we can start with the new PRs. There is a couple of them open up. First one… is related to Cisco internal codec scans, and… It basically fixes the predictive path.
In our share scripts, it will be using non-predictable.
It should be working on all supported systems based on my tests, so it should be saved. So, if you have time, please review.
We have couple more.
PR's first one is from the… External contributors related to IBM MessageQ.
over XMS.net, whatever it is, and it is bytecode Instrumentation for these systems. I do not have time yet to look into it.
It is not very popular, but Nugget package has, kind of, 4 millions of downloads, so it is not also kind of very edge case.
So, we need to decide how to proceed with this.
**Igor Kiselev** 11:02 question, if it adds any external dependency, should we already try to apply a model where each dependency in a separate NuGet package and enabled through all the targets?
or it should be the same way as everything else, and we target the split online feature. Right now, the only split dependency is Redis.
**Piotr Kiełkowicz (Splunk Inc.)** 11:28 I think it is fully bytecode instrumented.
**Igor Kiselev** 11:31 Okay.
**Piotr Kiełkowicz (Splunk Inc.)** 11:32 If I understand correctly, so the XMS dependency is going only to… our testing applications, and there is no changes on the CS Pro levels in the other products, so… so no new dependencies.
**Igor Kiselev** 11:49 Okay, good.
**Piotr Kiełkowicz (Splunk Inc.)** 11:50 The… the best what we… For sure, we should ask if he does not want to contribute directly to the IBM, if he's from IBM team, I'm not sure.
And ask to implement it natively in XMS.NET client.
And then… Using additional sources, it will be trivial to… To fetch all necessary data, because… Kind of, if you look into this, a lot of… Strange changes.
Raj, do you have any preference or experience with this message queue client?
**Rajkumar Rangaraj** 12:37 Nope.
**Piotr Kiełkowicz (Splunk Inc.)** 12:43 Okay, so for sure, I will ask tomorrow about the possibility to add native instrumentation for this For this project, and then we need to consider how to… how to proceed with this.
**Rajkumar Rangaraj** 12:58 That would be a good idea, right? Like, having an instrumentation and bringing that here.
**Piotr Kiełkowicz (Splunk Inc.)** 13:04 Yeah, it will be much cheaper for us to maintain it instead of, kind of, providing this legacy stuff.
**Rajkumar Rangaraj** 13:11 Yep.
**Piotr Kiełkowicz (Splunk Inc.)** 13:14 Yvgi and your RFTA, because we are probably working together on this.
Is it really ready to review, or you are working on this, and it is in draft stage?
ED car?
**Eftiquar** 13:38 Once…
**Piotr Kiełkowicz (Splunk Inc.)** 13:53 Okay, let's switch to another. The next one is Jagor V2. If you have some time, please review if it is working end-to-end. We should… Update our exams and deaf experience with the newer version.
But I didn't have time yet to verify if this is really working.
And… Last peer is related to the Kafka cluster ID, still waiting for… For the review, and this kind of… Almost 2… well, almost three months waiting, so it will be great if you… to look into it.
**Eftiquar** 14:40 Hey, Piotr, sorry, the unmute was not working, probably Zoom hung up on me. Maybe it's the codecs. So, the PR is not ready for you yet, that's why it's in draft. I will open it up for you by today evening.
**Piotr Kiełkowicz (Splunk Inc.)** 14:55 But this one, Evgeny.
**Eftiquar** 14:57 Yeah, so we can get… The dynamic config, or the name, yep.
**Piotr Kiełkowicz (Splunk Inc.)** 15:03 Sure, so I'm converting to draft, and when you will be ready, please reopen.
**Eftiquar** 15:08 Yes.
**Piotr Kiełkowicz (Splunk Inc.)** 15:11 I think that's all.
From the PR… new issues.
**Eftiquar** 15:21 Do you want to briefly touch on the sync up, or… Are we all in agreement that we will sync up the fixes that Datadog has done?
the fix on multi-byte to wide care, that I… the bug that I flagged.
And also, the wildcard filtering,
**Piotr Kiełkowicz (Splunk Inc.)** 15:45 Do you mean this, this PR? Yes, we should… we have kind of long-term agreement that we should… finally finds some workforces to go through all commits on the Datadoc side and bring all necessary changes. It is much easier now.
than it was historically possible, so I expect that we will be able to improve everything.
**Eftiquar** 16:14 Okay.
**Piotr Kiełkowicz (Splunk Inc.)** 16:25 And… what is this? Configuration binder.
for the no… For the readies, I've asked a couple days ago about the… Even yesterday, like, about the reproduce… steps to reproduce exact?
And minimum reproducible example, no… no issues, no response so far, so I'll keep it as it is.
And FTC cards, AGCRs.
Again.
**Eftiquar** 16:58 Yes.
**Piotr Kiełkowicz (Splunk Inc.)** 16:59 Do you want to discuss anything today, or…
**Eftiquar** 17:03 No, this is a…
**Piotr Kiełkowicz (Splunk Inc.)** 17:04 cities.
**Eftiquar** 17:05 Yeah, we can keep it as it is, because this has been already translated into PR, and I'll open up the PR, and hopefully there, the architectural details will reveal themselves. This was just a blueprint of what we are going to do.
**Piotr Kiełkowicz (Splunk Inc.)** 17:19 So, can I put it to VNEXT, or 117? VNEXT, okay.
**Eftiquar** 17:31 Thank you.
**Piotr Kiełkowicz (Splunk Inc.)** 17:38 It is not refreshing.
Yes, it's a server.
Discussions… Nothing new?
All issues correctly handled, and the project boards.
I think it is no longer true.
Yeah, nothing important. I will review it separately.
Any other topics you have for today?
**Igor Kiselev** 18:55 I have a… topic. So, we reintroduceport above dependency. Right now, our dependency policy, we discussed only about, Microsoft Extension, and, and system diagnostics. Protob is a new type of dependency. Right now, we try to upgrade it to a later structure, so the outcome of it would be with our target.
of customer assembly, we will upgrade for all Protob users to the latest version of Protobuff, I'm not… technically, we could still follow the oldest product above that's used by OpAMP, Or we could even ask a pump, probably, to downgrade Pukhov to an older version.
And once again, we have a… we may apply different options for NuGet package and for, zipper hype. But once again, we need to understand, would we like to… upgrade everybody to the latest version of Protobuff? Would we like to use oldest version, and do not upgrade for customers who are using it. Okay, once again, oldest, non-vulnerable.
All would like to do something else.
So, current state, we use latest version.
And automatically upgrade everybody, but above, it's not Microsoft Library, and it's pretty popular, so we may expect that for many customers, we will auto-upgrade it in the background.
**Piotr Kiełkowicz (Splunk Inc.)** 20:40 I do not think that it is a big issue.
If we consider… Our new auto-upgrade, possibility.
To be honest.
**Igor Kiselev** 21:13 Okay, so I'd say that for now, the decision, do nothing, and see if there will be any complaints.
It also works.
**Piotr Kiełkowicz (Splunk Inc.)** 21:22 I think so.
**Igor Kiselev** 21:29 I'm probably the most for complaining, because I have to upgrade Protabuff for our internal product, and probably some of our customers will have to upgrade. For many of them, it will be pretty easy.
Hold up.
Okay.
**Piotr Kiełkowicz (Splunk Inc.)** 22:18 So, thank you. See you next week.
