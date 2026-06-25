SIG: .NET Auto-Instr SIG
Date: 2026-06-24
Duration: 20 minutes
============================================================

## Zoom Recording Transcript

**Piotr Kiełkowicz** 01:41 Hi guys.
**Zach Montoya** 01:43 Hello.
**Alexey Pukhov** 01:47 Hi, everyone.
**Piotr Kiełkowicz** 02:00 Liz, can you drive a meeting today? I'm along with my children, Juan?
So… there is a chance that I need to drop.
**Zach Montoya** 02:15 Yeah, I can drive.
**Piotr Kiełkowicz** 02:16 Okay.
**Zach Montoya** 02:43 Let's give it one more minute… I guess we can get started?
Were there any… Doesn't seem like there's any topics you guys wanted to discuss.
Before we go through the agenda?
Alright.
Let's go through…
**Piotr Kiełkowicz** 03:25 So, sorry, Zach, one thing.
I'm checking the codec security.
Scan the results.
And there is a chance that we will need to include Kind of signing… Artifacts in our pipeline.
Mainly to be able to verify it on the… Customer sites.
For now, the open telemetry community is using mostly cosign.
**Zach Montoya** 03:59 Okay, yep.
**Piotr Kiełkowicz** 04:01 And we do not have access to any kind of official certificates, which would be Windows-friendly, so I think we… we need to follow this pattern.
**Zach Montoya** 04:15 Yeah, we use Cosine ourselves, Yeah, so that's something we'll need to do. Is there an open… Issue yet that we have for this?
**Piotr Kiełkowicz** 04:26 I think there is one.
But there is no details yet, because, kind of, it is… the security scans are, kind of.
internal to Cisco, unfortunately, and I am not able to share all details, but I can dump it later and send you in private if you want.
**Zach Montoya** 04:45 Okay, yeah, I mean, as long as we… I mean, I think this is something we need to do anyways, regardless of the… The… the code at scan.
Was there anything else that it brought up besides… Like… The code signing?
This is… Oh yes, okay.
**Piotr Kiełkowicz** 05:08 I've posted the issue to the chat… to the chat, if you want to kind of subscribe.
NET SDK already implemented this feature, and… Signatures are included into the no-get packages.
I think country is still missing, and we're for sure missing it for the, let's say.
Installation scripts, also for the artifacts, so… A lot of stuff to be fixed.
**Zach Montoya** 05:58 Okay.
Okay, that's good to know.
Alright, I guess… for now… Yeah, we can follow up on these threads.
But, glad we already have some tracking issues for that.
Is there anything else that the, the code scanning kind of brought to light?
**Piotr Kiełkowicz** 06:31 The one I sent you… Yes. Kind of a couple weeks ago, just related to some… artificially bets.
signatures and other things, I will dump everything, what I had, and I've shared with you.
**Zach Montoya** 06:48 Okay, yeah, I started… I started a code change to fix that, I just haven't completed it, or I just haven't… Sent to commit or anything.
**Piotr Kiełkowicz** 06:57 Sure.
But most of the… most of the problems are related to untrusted artifacts downloaded from the internet, which is kind of the highest severity. Other ones, I kind of… Law or informational one.
**Zach Montoya** 07:15 Okay.
**Piotr Kiełkowicz** 07:17 And I do not have capacity to focus on the low stuff and below, so we are taking the medium and the hires.
**Zach Montoya** 07:28 Yeah, that makes sense.
Okay.
So, on the subject… How should we… oh, I guess… I guess Robert actually posted an update here, we can solve this with us.
Okay.
**Piotr Kiełkowicz** 07:46 We were discussing it today, to be honest, because he's doing similar stuff for the… albeit.
**Zach Montoya** 08:03 I see, okay.
And I'm just opening up the link that… okay, yeah, perfect, this one.
Yeah, if we're okay to change subjects now.
the other main thing that was discussed last week, and I guess, is still open, is the StackWalk PR. So I guess, what else, yeah, what else, do we need here, or what's the next steps on this one?
**efshaikh** 08:29 So, Codex did point one issue. It's a subtle one, but I think it needs to be fixed. It was a nice point that it raised.
**Zach Montoya** 08:42 Six of mine.
**efshaikh** 08:43 So it's safe that you are calling… making calls to the methods that should be protected by exception handling, and it produced a patch. So I was evaluating. Thank you, Piter, for issuing that request. So it's a corner case, but nevertheless, it makes our code bulletproof. So I'll make those changes, and… Thus, update the PR.
But aside from that, the PR is solid now, and we would… we already have plus-one approval, but if there are more pair of eyes that would like to take a look at it, that'll be really helpful, because it's non-trivial PR, a lot of changes.
**Zach Montoya** 09:21 Okay, yeah, on this PR, I, you know, I delegate to… to Gregory to give a good look, you know, it's like he, also reviewed this, I think, a couple weeks back? Yes. And then Chris also did. Okay.
Okay.
I may not… yeah, I'm not sure if I'll be able to take a look, or at least provide very much insight on my end. So perhaps once, resolving, this particular issue, and then getting CI to pass, I don't see why we can move forward just with merging it.
**efshaikh** 10:01 Okay, yeah, I will resolve this issue upon it.
**Zach Montoya** 10:06 Cool.
Alright… So, let's see, going back to… There's a bunch of the Dependabots. I guess, actually, it's just 7 of the ones that I thought… Oh, they're renovated, so we gotta change our filter on that. Alright, we still have an issue open by Matt for the resource attributes.
I'm not sure… There's been any progress made since the last time.
Okay, we discussed this as a SIG, okay.
Okay, so for now, I think we've… Discuss what we wanted out of this.
So we can just let that be for now.
Stackwalk… the Public Plugins API, I took a look.
And I think… This looks good for the most part. One small change that I requested.
Just adding the APIs.
Rather than relying on reflection.
I don't think there's anything blocking, so… Ross will get back on that… And then the remaining open ones are for… We have a new Kafka one for, adding a span attributes.
So this will be a good one to review, and then also.
integration test for this hotel auto-traces additional legacy sources.
Okay, seems fair.
Be surprised that we haven't already… Have an end-to-end integration test for this?
potential improvements? Okay.
Great.
**Piotr Kiełkowicz** 12:05 So, fixes to be too much, like, kind of trivial, but it will be great if the contributor fix it. Otherwise, I will handle it probably next week.
**Zach Montoya** 12:15 Okay. Shall I approve it to run?
**Piotr Kiełkowicz** 12:19 Yes.
**Zach Montoya** 12:26 Alright, so they're started. Okay, cool, I can also take a look as well, but glad to see some… Improve testing.
This one, yeah, this one, we can take a look. Oh.
**Piotr Kiełkowicz** 12:45 In general, blocked by secure… the semantic convention.
**Zach Montoya** 12:49 Oh, and it's closed?
Oh, I wonder if there's, hmm So it should go to semantic conventions.
I know there was… I feel like there was a messaging-specific sig for that, but okay, yeah, I guess we'll just track this. But yeah, let's… we'll wait for… Any additions here before merging and searching?
Okay, besides that, the rest are Dependabots, so we can update those.
As long as they pass the CI.
Alrighty.
**Piotr Kiełkowicz** 13:37 I can share one more comment about the Oracle.
**Zach Montoya** 13:40 Sure.
**Piotr Kiełkowicz** 13:41 It is in draft right now.
I was in contact with PMs from the ORAC team, and there is set back on the ORAC side, and… Technically, this instrument… this implementation is working fine.
It is propagated, but the spans from the server site are… never go to the collector.
Or… it's… and it doesn't matter if it is our mocked collector or the real one. They have a bug on the server side, and we'll fix it in the July.
Probably, with the next release.
**Zach Montoya** 14:16 Okay, so there's an issue on the Oracle MDA package side, is that what you're saying?
**Piotr Kiełkowicz** 14:23 Oracle server site on the Docker image.
**Zach Montoya** 14:27 Oh, okay.
Okay.
**Piotr Kiełkowicz** 14:30 Because what Oract did, they… They have prepared native support for the propagation.
And context propagation, and what is more, the creating spans on the server side. So we have it both from the client side and the… Child spans, or we should have child spans from the server side also.
Like in the HTTP calls.
the same for the SQL queries, the Oracle stuff.
**Zach Montoya** 15:02 I think I'm still not quite understanding. I understand that we have client spans that we emit, you're saying there's also.
**Piotr Kiełkowicz** 15:09 We are emitting client spans, we are propagating context to the server side, and typically DBMON teams were kind of querying server-side to Correlates time execution, queries plans on the server side, and by some kind of dark magic correlations. And now the server span… server side is also covered by the spans, so you have all this info… should have all information from… natively.
From the modern servers.
**Zach Montoya** 15:44 Oh, okay, and those… are those emitted as spans, or…
**Piotr Kiełkowicz** 15:48 It should emit spans.
**Zach Montoya** 15:49 Oh, okay, I see.
Got it.
**Piotr Kiełkowicz** 15:53 But it is not working.
**Zach Montoya** 15:54 Okay, cool. Sounds good. You said end of July is when they start to produce?
FX.
**Piotr Kiełkowicz** 16:04 Yes.
**Zach Montoya** 16:05 Okay.
Sounds good.
Did you want to… I mean, did you want to block on… that for this PR, because I know this is… Primarily operating on the client spans.
**Piotr Kiełkowicz** 16:25 Yeah, I think we should wait with final merge, but I will check with my DBMON team if they are happy with current, let's say, current implementation, and if they will be able to just fetch information from the propagation.
I read it already. If so, if it will be useful for us, I think it will be useful also for others, because I think we are using the kind of common way to… to fetch this data from… for the open… for the open telemetry, so… Depends on the answers from the DMIMO team.
**Zach Montoya** 16:57 Okay.
Alright.
I think that's it, unless you guys had any other PRs you wanted to discuss.
Anything else?
Alright, issues… okay, so we have… Yeah, open up a issue to track this work. I'm not sure if you commented on here already. You can just follow along with the associated PR.
And then web configs.
We still don't have… we don't have a milestone for this. I'm not sure that we still want to do this, because we were talking about it over here.
Should we… I guess, should we close this, or… I don't want to keep, kind of, looking at this for now if we're not gonna act on it.
**Piotr Kiełkowicz** 18:03 I think it is related to the PR.
We have already… Review what?
**Zach Montoya** 18:12 Yeah, at least in here, we discussed.
Yeah, this was in the resource attributes… So, should we support it?
We decided yes.
Interpolation, that's a different question.
So for now, I mean, it sounds like we've… I mean, we could probably… I mean, I think we've exposed this for now and say, like, we're still going to support WebConfig, and then we can always come back and reopen, or if we change decision, we could… we could do that.
Sure.
**Piotr Kiełkowicz** 18:52 It makes sense.
**Zach Montoya** 18:54 Alright, let's just do… Let's… Okay, nothing to do here.
Alright?
So that's all the open issues.
No discussions… I don't think, We've changed anything for our next release.
I don't think there's anything… any progress over here.
I think we're done with that.
Alrighty, anything else?
**Piotr Kiełkowicz** 20:18 I don't think so.
**Zach Montoya** 20:22 Alright?
Cool. Well, thanks for your time, everyone.
**Piotr Kiełkowicz** 20:27 Thank you, I'll see you next week.
**Alexey Pukhov** 20:28 Thank you for driving it.
**malach** 20:30 Thank you. See you.
