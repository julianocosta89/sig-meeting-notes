SIG: Go SIG
Date: 2026-05-21
Duration: 12 minutes
Zoom Recording URL: https://zoom.us/rec/share/VAfL2WUo4FPAa0qLpMQoBP3cklj412-xwnWS7aXK_rRfGNdgnYcg0iPtDelax01y.vPsQ8u7cG_4dDURO
============================================================

## Zoom Recording Transcript

**Pellared** 06:47 Hello?
**Puneet Singh** 06:49 Hello?
**Pellared** 06:55 How are you?
**Puneet Singh** 06:56 I'm good. Yeah, I'm Puneet, this is… I think I'm joining the call for first time, but I've been working on a few issues. I think, there was one PR which was… pending some feedback for quite long, so I thought, you know, I might join a meeting and… Collect some…
**Pellared** 07:14 Sure.
**Puneet Singh** 07:14 Feedback.
**Pellared** 07:16 We do not have the quorum today. I, I thought that, that if I want, I can take… we can take a look. Do you want to share your screen and show DPR?
**Puneet Singh** 07:27 Sure, just give me a sec… .
**Pellared** 07:33 Are you based… are you based in India, or not, or in the US?
**Puneet Singh** 07:36 I am, I'm… I'm an idiot, actually.
**Pellared** 07:38 Oh, so it's extremely late for you, right?
**Puneet Singh** 07:41 Yeah, kind of, kind of, but that's okay.
**Pellared** 07:47 I'm also in Europe, so for me it's like… 7PM, but for you it's, like, in the middle of the night.
**Puneet Singh** 07:53 Yeah, yeah. Can you see my screen?
**Pellared** 07:56 Yes, I can.
**Puneet Singh** 07:58 Okay, so, pull request… So… I think this was related to…
**Pellared** 08:11 You can, find… this is your pull request, or someone other's?
**Puneet Singh** 08:15 Yes, this is mine, this is mine, actually.
**Pellared** 08:17 you can, you can click alter, and if you click Alter, probably you have the suggestion, yeah. You're the first one.
**Puneet Singh** 08:23 I think this one… I think this was discussed also, previously.
**Pellared** 08:29 Okay?
**Puneet Singh** 08:31 And the issue was regarding, inter… introduction of interceptor for optional attributes.
**Pellared** 08:39 I was out last week, but I think it was discussed 2 weeks ago.
Or if you… yeah.
**Puneet Singh** 08:46 Right. But yeah, I think this is the first change which actually, adds the context variable, which will later be populated by interceptor. So, until that is… until the, you know, the interceptor is added and the interface is added, this is more like a change that will sit behind the scene, actually. So…
**Pellared** 09:11 Okay, we are planning to make a release.
Hopefully this week. We wanted to do the previously, but given this is just a first step.
I think our preference will be to merge it just after the release. It still won't be… because I don't think it matters for you, given it will be still not available with this PR, is it correct?
So…
**Puneet Singh** 09:38 Sorry, I didn't get your question.
**Pellared** 09:40 Do I understand correctly that this one just has a context variable, but from the user perspective, the telemetry still isn't, emitted, there is no additional things, or… No, no, there is…
**Puneet Singh** 09:55 Yeah, there is no additional things. I was planning to make this change after… after this PR, actually. So, can you give me a… just… I'll back in a few seconds.
Hello, sorry.
**Pellared** 10:26 Not a problem, I will just… I will add this pair to the agenda.
8, 9…
**Puneet Singh** 10:36 So, you were suggesting that, I should, like, try to include the rest of the work, like, on the APIs itself, so the…
**Pellared** 10:46 Endpoint.
**Puneet Singh** 10:46 You are an episode.
**Pellared** 10:47 because don't add anything more, because you already have one approval by David.
And if I take a look and approve it, then I can merge it.
And at least you have something already here. I just wanted to call out that probably this won't be… include the, even if you create a separate PR, you know, a follow-up.
There is a low probability that it will go to the nearest release until… unless it's very important for you, then I don't know, just let us know if it's critical.
**Puneet Singh** 11:21 Sure, I think that is totally fine. I don't think the overall change is that critical. It can take its time, and I think it should take its time, because it's also a change in the interface for the hotel gRPC instrumentation.
So, I believe, you know, it can take some extended… it can use some review from the Quorum itself, rather than, you know, trying to get it shipped quickly.
**Pellared** 11:46 Okay, let's… yes, I will take a look at this PR, just adding to the agenda. Yeah, recently, we just… More peers than usual.
And also, more stuff to do, okay, so…
**Puneet Singh** 12:02 Yeah, I think there were quite a task created for the detector migration, so… Yep.
There will be some PRs upcoming in that area also.
**Pellared** 12:12 Yes.
Is there anything else that you want to discuss?
**Puneet Singh** 12:16 No, I think that was more or less from my side.
**Pellared** 12:20 Okay.
Yeah, so… I think that's it. Thank you very much for joining.
I'm happy that you get the opportunity to, you know, to show it, and hopefully this will be merged soon.
**Puneet Singh** 12:33 Sure, sure. Thanks a lot.
**Pellared** 12:35 Thanks. Good night. Have a nice night. Bye.
**Puneet Singh** 12:37 Bye.
