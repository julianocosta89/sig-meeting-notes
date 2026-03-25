SIG: .NET SIG
Date: 2026-03-24
Duration: 11 minutes
Zoom Recording URL: https://zoom.us/rec/share/ZTTNEWXZMssRMJ4PBU6psFiqqePoOCm_wPirAb7H601wU_9HDotTrQR6gMFWThvI.JDRwoL7uA2NXwkMq
============================================================

## Zoom Recording Transcript

**Julius Koval** 00:13 Hey.
**Matthew Hensley / Grafana Labs** 00:17 Hello!
**Rajkumar Rangaraj** 00:47 Hello, everyone.
**Julius Koval** 00:52 Bye.
**Rajkumar Rangaraj** 02:41 I just gotta know, I have a notification from Martin. Martin won't be joining. I think that's all. We may not have any more joining. We could start. I do see there are two topics added by Martin for a discussion.
Maybe I… one, I have the context, and the other one, I don't have enough information.
The first one on the TTRFS is TTLR, the database instrumentation, so I've not been closely following this, One. So, I would, try and park this.
For the later discussion, or if anyone has any, like, Sorry, there is a bar here which is… not allowing me to concentrate once again. Yeah, if anyone has any context about this, we can discuss. If not, we will move it for the next SIG.
**I see everyone is quiet, I'm just leaving it for… Matthew Hensley / Grafana Labs** 03:54 Yeah, I'm… I was reading through it, you… we can… move it to next time. I… Rajkumar Rangaraj 04:00 Yep.
**Matthew Hensley / Grafana Labs** 04:02 This looks like some semantic convention clarification.
**Stuff to be taken care of, so… Rajkumar Rangaraj** 04:08 Yeah. I think Alan is here. Alan has worked closely with, DBA, semantics and the SQL instrumentation. Alan, by any chance, you, you're aware of this one. If not, I think we can just move it for the next six discussion.
**Alan West** 04:27 Sorry, I just arrived. I came late.
So I don't know what this is.
**Rajkumar Rangaraj** 04:36 Okay, no, no worries. I think in that case, even I don't have the context of this completely, not been closely following what's going on in this.
what went on on this PR, so need to just go and check it before… just, commenting on this. Something related to the spec, I believe, that sparked it.
For the next week. And the… the second topic is on the patch release. We have been speaking about it for a pretty long time. So I… I think, we should, there are no other blockers, whatever the PRs we want… Waiting to merge all got merged. I think we should do the patch release, even customers started asking about it for the fixes we did.
So, anyone has any concerns or anything related to the patch release?
Cool. If there is nothing, I think, we should, start the release process. So, I see third… I'll move on to the next topic, if there is no question about the, release.
Julius, you want to speak about this?
**Julius Koval** 06:04 Yeah, so I created two PRs.
Related to the LuxBridge API, one most related to exception, and I guess we're still waiting for feedback there.
And, on this issue that I linked… Pyotr said that we should probably create… an issue or something which would track all the deviation of the LuxRich API from the spec.
**You know, I guess so we could keep track of it, so… Rajkumar Rangaraj** 06:34 Boom.
just create an issue on this and link it to this PR. Once that's done, we will get it merged. I don't think this PR is any way blocked.
on that.
**Julius Koval** 06:47 Okay.
Anyway, so I mentioned last week… I was working on… Adding support of KVList to the protobuf serializer, so I'll try to create a PR for that this week.
Sure, that's okay.
**Rajkumar Rangaraj** 07:03 Yep.
**Julius Koval** 07:06 Okay, good.
**Rajkumar Rangaraj** 07:07 And this is the, PR in discussion, like, where you are adding the spec-compliant API and trying to, deprecate the current API. The only reason, like, I have a concern is It's not a must declare… in the spec, it does not say it's must, it's optional. And creating a new API is going to cause a customer confusion, and even in this PR, we have not resolved what would happen if both the APIs get used.
So, in order to avoid all that challenge and keep it simple, this one also, I would say, we create an issue and then ignore this PR as it is. That's where I left my comments, like, wait for PRR to come back on it.
Alan, it would be helpful if you could just take a look at the conversations in this PR, not about the implementation.
**Alan West** 08:09 Okay, yep.
I'll take a look.
**Rajkumar Rangaraj** 08:17 So, this week, like, we got most of the PR smart, and I provided my approval on this Generate SMOM. I don't know why it's pending, I thought I'll ask Martin today.
I'll check with them… Why it's pending, if there is anything needed, or he's waiting on it.
On the last PR also, there is only one task pending. I just summarized and left, like, comment, there. So, waiting for the order to fix that. Once that's done, I think this also should be good to… Merge. So, overall, like, in the past two weeks, we made a good progress on all the PRs that had been pending over here.
So, switching back to the issues, this is the new issue.
I did not get a chance to look at it earlier. Let's see.
does not look like an… if it works locally and moving to somewhere else does not work, I don't know.
How well it's an issue with the configuration, so… Probably it could be an issue where they might have not moved Things. Like, we can just take a look at it offline.
I think, Martin has responded already, and this is also old. Nothing much from there.
So, that's all we have it. The only thing for this week that stands out is, not only thing, there are two things that stands out for this week, is one is the, the patch release, and, The next one is the, to unblock the logs bridge API work. There is a PR, it's sitting there. We need a concrete answer on it, so that we can move forward with those implementations.
just… I'll go back to the document and see if there are any other topics, left. Nothing else over here. So, does anyone have anything else, for discussion?
**Alan West** 10:57 Man.
**Matthew Hensley / Grafana Labs** 11:03 Nope, all good.
**Zach Montoya** 11:04 More than familiar.
**Rajkumar Rangaraj** 11:05 I think we could end it early. Thanks, everyone.
**Zach Montoya** 11:09 Thanks.
