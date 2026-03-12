SIG: Semantic Convention SIG
Date: 2025-12-01
Duration: 18 minutes
============================================================

## Zoom Recording Transcript

**Trask Stalnaker** 00:31 Hello!
**Christophe Kamphaus** 00:33 Hello?
**Liudmila Molkova** 00:50 I think it's my turn to run the call, and give me a sec.
**Trask Stalnaker** 00:59 Alright, thank you.
**Liudmila Molkova** 01:06 It's quiet here today.
**Armin (Dynatrace)** 01:11 Thanksgiving aftermath.
**Trask Stalnaker** 01:13 Aftermath.
I like that.
**Liudmila Molkova** 01:16 It didn't even have Thanksgiving, Carmen, did you?
**Armin (Dynatrace)** 01:21 We do have something with the same name, but I don't know when… It's celebrated, it's more of a… Countryside thing by, like, farmers who harvest actual crop.
No idea when that happens. I think… Also, someone in 4.
**Liudmila Molkova** 01:57 Okay, yeah, so let's take a look at the triage board.
We have some… Nothing blocked, nothing ready to be merged.
There are a couple of RPC pull requests that would benefit from general review. Trask approved.
So maybe… In case, oops, somebody is going to read notes.
I'll put them here.
This one… I believe is not… ready for the general review, there are… it's a GenAIPR, and there are some Unresolved comments that should be addressed first.
There are a lot of things that are awaiting co-donor approval.
Not sure if anything… Should be called out.
**Trask Stalnaker** 03:36 I think the service criticality… just got approved by Josh, so I can move that to… He's a code owner for the service.
SIG.
**Liudmila Molkova** 03:56 Okay, cool, I moved it to need some more approvals.
Oh, and this one should be ready to go?
**Trask Stalnaker** 04:13 Let's… I think so, but let's let, oh, did I not resolve… Yeah, yeah, you can resolve my conversation. I had intended to.
Oh, the conflict.
**Liudmila Molkova** 04:31 Resolution.
**Trask Stalnaker** 04:32 I see.
**Liudmila Molkova** 04:37 So I'll move it to ready to be merged, then.
**Trask Stalnaker** 04:42 Cool.
**Liudmila Molkova** 04:54 Let's take a look at a few more.
Okay, still awaiting, still awaiting… Still awaiting.
It's too early.
Should we take a look at the issue trash board? I'm a bit scared to look there.
**Trask Stalnaker** 05:19 Right.
**Liudmila Molkova** 05:23 No status. How come something doesn't have a status?
Should do when the request fails.
Sounds like… It should be accepted.
And… This one… It's decor.
So, I trashed it, I don't know if you folks want to take a look.
I think the original Problem is that there are some Oh, I don't even understand the original problem, to be fair.
**Trask Stalnaker** 06:24 index for… I think I missed… I didn't see this one.
**Liudmila Molkova** 06:37 So this is a hidden… Read me.
that placed all the LESs for… this folder.
**Trask Stalnaker** 06:54 What's the PR number? Oh, I see, you closed it, got it, got it. That's what I wasn't finding, Oh.
I see that as… it looks like… James closed that last week.
**Liudmila Molkova** 07:10 Okay.
So, I then would like to close this shit as well.
Should we close the class?
Jewish.
**Trask Stalnaker** 07:33 That's a good question.
Yeah, probably.
I mean, if… If… if it's… Not clear… software, at least?
I don't know.
Our men… Do we have a… Why not have Yao?
I don't recall what we have decided. We've been just focused on the PR triaging.
Workflow.
**Armin (Dynatrace)** 08:29 I don't recall either.
**Trask Stalnaker** 08:33 I think I'd like to get some… Clarity on… or consensus from… the other SEMCOM maintainers… .
**Liudmila Molkova** 08:47 Maybe I'll bring it up in the, maintainer's chat, and we can, discuss it next time.
If there is anything to discuss.
**Armin (Dynatrace)** 08:57 Yeah, sounds good.
**Trask Stalnaker** 08:59 Thanks.
**Armin (Dynatrace)** 08:59 I don't know if we've… if we've discussed it at our issue.
Yeah, let's figure it out there.
**Liudmila Molkova** 09:10 Okay. But then… Okay, there is no…
**Trask Stalnaker** 09:18 Could do needs triage. I mean, we're kind of still in that… Oh, initial triage, I see.
**Liudmila Molkova** 09:30 It's okay.
**Trask Stalnaker** 09:31 Okay.
**Liudmila Molkova** 09:44 Okay, closed to have a child that has status now.
Should we move on to the main agenda?
Pretty light.
Mikael, next steps with service, pure namespace.
You have a PR for this, right?
**Michele Mancioppi** 10:03 Yeah, and I received a very nice message from Trask with a bunch of questions.
That I hope I answer to satisfaction.
**Trask Stalnaker** 10:11 I will review, I saw that. I will review it, and I reopened the PR, it got auto-closed for… because of our amazing, workflow. So I reopened it, and I will review your response today. Thank you for going through all of that.
**Michele Mancioppi** 10:28 Ben, my job is done.
**Liudmila Molkova** 10:37 Anything that needs a discussion?
**Trask Stalnaker** 10:42 I don't think so. I mean, unless, well, I haven't read, Michelle's response here.
But I… generally, we're… the SIG is on board with this change. We just want to map out what the, sort of.
Breaking implications, migration process.
Should be for, usage.
**Liudmila Molkova** 11:14 Oh, and…
**Trask Stalnaker** 11:15 Yeah.
Go ahead.
**Liudmila Molkova** 11:17 You mentioned the SIG, it's the, the service in deployment seek that.
**Trask Stalnaker** 11:23 that counts it. Yeah, yeah.
**Liudmila Molkova** 11:24 Yeah. I see. Nice.
**Trask Stalnaker** 11:26 Yeah, and it got auto-closed because it, deprecated the peer.namespace, and we don't have a peer… a SIG-owning peer.
**Liudmila Molkova** 11:38 I see.
That's great, actually, removing something, deprecating something that's not owned.
**Trask Stalnaker** 11:45 Yeah, yeah.
**Liudmila Molkova** 11:46 Yay.
Cool, so then, from the triage perspective, I think it should be… A waiting co-owner's approval?
**Trask Stalnaker** 12:02 Yep.
**Liudmila Molkova** 12:04 Awesome.
Okay.
And I… let me just quickly introduce our PCPRs here.
We are making progress on our PC side.
And there are a couple of PRs I want to call out. The first one… as… Deprecating a bunch of… Technology-specific.
Attributes related to status code.
into… Single one.
So we had gRPC status code, RPC ConnectRPC error code, and JSON RPC error code. They're all now… RPC response status quoad.
There are a bunch of changes which are super minor. We used to say that there is a gRPC status code. It's a small correction that we now see, just general GRPC status code.
other than that… this PR… clarifies… When they should be, when… corresponding status code.
results in the error. So, for example, we had a table in gRPC That talked about which status cuts, constitute an error.
Now it's part of the… attribute… Of the description.
So… for… Client spans, all status codes except a case should be considered errors, and there is a similar section for server spans.
And so on, that, that's it, that's the change.
Somebody would like to take a look?
**Trask Stalnaker** 14:21 Armin? I'm volunteering, Armin.
**Armin (Dynatrace)** 14:26 Sure, I can take a look.
**Trask Stalnaker** 14:28 Thank you.
**Liudmila Molkova** 14:29 Thanks.
And another one is, about… duration, so we… used to have, RPC client server duration, and now we are calling it RPC client… Server call duration, it's also changed to seconds from milliseconds.
It does a lot of, Pattern matching quiz, database conventions, saying that the metric… is, Matching the span, if span is recorded, and it also clarifies streaming cases.
So, we had this wording while streaming.
RPC may record this metric, it's hard to interpret in practice. Instead, we're saying this metric matches the RPC call from start to end. In case of streaming, it includes the full stream duration until say, the final response is received, in case of gRPC, until the gRPC status code is received. This matches gRPC metrics native instrumentation.
And this matches our idea that we would measure the whole call duration. It might be somewhat not interesting in case of streaming. Oh, I'm sorry, my setup just broke.
It would match… In case of streaming, it might not be super useful. We could also introduce, for streaming cases, a metric like time to first response, or time to, first request, or something like this. It's not the… the… Our goal to cover streaming fully.
But this just aligns… this pull request just aligns this metric with, what we have with our best practices, across other conventions.
So I also would appreciate your review.
**Trask Stalnaker** 16:51 I've… I've approved this, right?
**Liudmila Molkova** 16:53 You did, yeah.
**Trask Stalnaker** 16:55 Okay, great.
**Liudmila Molkova** 17:00 And… If you are super excited about RPC, come join our meetings, and come join our secret.
**Trask Stalnaker** 17:09 Midnight.
**Liudmila Molkova** 17:10 rapid.
**Trask Stalnaker** 17:10 at midnight for Armin.
**Liudmila Molkova** 17:17 Sorry, Armin.
**Trask Stalnaker** 17:18 APAC.
Friendly.
**Armin (Dynatrace)** 17:20 It's… it's fine.
The chokes, not the meeting time.
Do you have sufficient staffing for the RPC group, or are you still looking for more people there?
**Liudmila Molkova** 17:40 We are looking for more approvers, for more people who would like to contribute, Either by reviewing, creating PRs, writing PRs, did research.
**Armin (Dynatrace)** 17:53 then maybe if you… if you call it out in the general spec channel, not specs and conf channel, maybe someone else might be interested? I'm… I'm sure you're not the only vendor who's using RPC on this planet.
**Liudmila Molkova** 18:26 Cool! We are at the end of the agenda.
**Trask Stalnaker** 18:31 Alright.
**Liudmila Molkova** 18:33 Okay, quick one. Thank you all for joining.
**Trask Stalnaker** 18:37 Thank you.
Bye.
**Armin (Dynatrace)** 18:40 Thanks, bye-bye.
**Christophe Kamphaus** 18:41 See you.
