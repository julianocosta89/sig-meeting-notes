SIG: Python SIG
Date: 2025-07-31
Duration: 34 minutes
Zoom Recording URL: https://zoom.us/rec/share/M_VCiSaU1a_nauQvJG5ykLbQFSA-xcLwz7tiFh_YdZ8r_uDCqVg0SwXVqktAtedU.v2Gbq4KLsfj8oVO7
============================================================

## Zoom Recording Transcript

**Riccardo Magliocchetti** 04:01 Hello!
**Hector Hernandez** 04:05 Hello!
**Pablo Collins** 04:12 Hello!
**John Scancella** 04:17 Hello!
**Riccardo Magliocchetti** 04:32 So welcome to this weekly call. It looks like our agenda is empty, so if you have any topic.
feel free to add them, otherwise this would be a short one.
and we're waiting a few more minutes for more people to join or submit topics.
**Aaron Abbott** 08:47 Everyone.
**Riccardo Magliocchetti** 08:53 Thank you.
So.
**Aaron Abbott** 08:58 Still no topics for today.
**Riccardo Magliocchetti** 09:10 So, yeah.
**Aaron Abbott** 09:28 I have some, I can add.
we got a question in chat, too, from John about good 1st issue items.
so, John, we? We don't. We haven't been doing a great job, probably with the labeling, but there should definitely be some good 1st issue items.
Do you have any particular area that you're interested in working.
**John Scancella** 10:04 Nothing super particular. I did do python, as like my main development for like a couple of years, but I would say I'm much stronger in in Java to be honest. But just just looking to, you know I love open telemetry, and I wanted to get back. So, just looking to help, and I talked to Alita on the on the slack, and and she's like, Oh, the python people need help like. Go go talk to them.
So I did look briefly at the ones labeled, You know, good 1st issue. But I I also again. I I didn't want to step on anybody's toes if they were already working on on something and duplicate effort. So just was trying to get a sense of like, Hey, we need help with documentation or like, Hey, can you? Can you run through these these things? That sort of thing.
**Aaron Abbott** 10:54 Yeah, I got you. Yeah, like, I think, Ricardo, you're probably showing this. But we have a lot of instrumentation related. Good 1st issues.
You know, absolutely, docs. If we could. If you want to help with docs, that would be amazing.
**John Scancella** 11:09 Yeah, I have no problem with that.
**Aaron Abbott** 11:11 Yeah. So I'd say, one big effort we're doing lately is working on the logging Api and SDK, stability.
So we're we're making some changes to to the kind of interfaces before we mark things stable. But the documentation is also pretty scant. So that would be.
I don't know if we have a specific bugs for that, we could, we should definitely create some. If we don't, or you're welcome to create some.
Yeah. One other thing I would say is, we don't usually assign issues. We've taken a more just like people leave a comment. Hey, I'm working on this because when you assign things. People don't work on them, they tend to kind of just sit in the backlog. So if you're looking at an issue and you want to work on it. Please just drop a comment. Say, hey, I'm planning to work on this, and if there's no other recent similar comments, you can probably pretty safely assume nobody else is doing it.
**John Scancella** 12:05 Okay. Sounds good.
**Aaron Abbott** 12:08 Awesome, and thank you. Thank you for joining welcome.
**John Scancella** 12:12 Yeah, thanks. Glad to be here.
**Riccardo Magliocchetti** 12:18 Okay? So maybe we can start with the 1st topic from Kit, the Bb 8, instrumentation scalp.
**Keith Decker** 12:28 Yep. So we've been working same with the lang chain to get the initial proposal of what we're going to do for v. 8, bringing it from Traceloops Repository into open telemetries repository. So this is just skeleton and including namespace. The next Pr will include actual implementation of spans and just making sure we're good to go on this.
**Aaron Abbott** 12:58 Awesome. Thanks, Keith.
A quick question. Do you know the status of the link chain work at all?
**Keith Decker** 13:06 The Pr. For spans is an internal review over here at Splunk. Should be popping up for you guys here soon.
**Aaron Abbott** 13:17 Okay, cool. Yeah. I'll take a look at this one, the only other.
I don't remember if it was Cisco Spunk who was bringing the proposal for kind of like a util Jen AI utils library. I reviewed a doc about that.
**Keith Decker** 13:32 Yeah, that is also an internal review, too.
**Aaron Abbott** 13:34 Okay, cool. Were you planning to use that for the spans? Or was that gonna come as like a later refactor.
**Keith Decker** 13:40 Initially, I was going to write without it, because we didn't know how the timing on when that would come through. But with the fast follow of modifying it, to use that if if that comes pretty quick, so yes, to both.
**Aaron Abbott** 13:55 Oh, they sounds good. Awesome. I'll take a look and thank you also. Welcome. It's always good to see new people.
**Keith Decker** 14:04 Yeah. Good to be here.
**Aaron Abbott** 14:05 Yeah.
**Riccardo Magliocchetti** 14:08 By the way, speaking online chain installmentation, I think also, aws were working on something similar. And they opened up here some days ago and and have commented to Czech region, a people. And it's look like they did.
It was this one.
yeah.
So hopefully, okay.
**Keith Decker** 14:41 I will. I will. Ping Redeemer about that.
So that's 3, 6, 6, 2. Okay.
**Riccardo Magliocchetti** 14:51 Yes, yeah. But they also, like already, you started working on this. You was Cisco's plan.
Okay? So we have a deaf yeah.
**Pablo Collins** 15:00 I think there's gonna be a call this afternoon to to figure that out.
**Keith Decker** 15:04 Oh, looks like redeem already. Put it up into your guys. It's in draft status. Okay?
So I guess it's out of internal review.
**Riccardo Magliocchetti** 15:18 Okay?
And then Aaron.
**Aaron Abbott** 15:26 Yeah.
So I spent some time digging into this kind of hard to reproduce weird bug.
I think. Actually, Alex, from Pydantic left some really helpful comments. And the the logfire docs have some really helpful kind of recommendations for avoiding this problem.
So if people are out of the loop. It's basically there's a couple of things. But basically, any any kind of using the yield statement, whether it's a synchronous generator or an asynchronous generator within like an hotel with block.
It can kind of produce unexpected or possibly undefined behavior. There's, I would say, maybe, like 2 or 3 different bugs related to this. And so some of the fixes are helpful, for, like the finalization, so you can surround everything with a with a context loop dot closing, or a closing block.
But for synchronous generators there's this really kind of unexpected behavior where basically context slip is not aware of generators running in kind of separate context. So it's possible, for if you create a span within a generator, then that whatever span you set will be leaked out to the parent which is receiving the yield call So there's there's sort of 2 mitigations people can do in their code. But basically, I wanted to share, like, I don't think there's anything we can do from hotel side.
besides maybe giving more helpful error messages. So instead of kind of spitting out this thing about the the I think it's detached. Called in the wrong context. We could instead improve the logging and point to some docs. So I'd like to write some docs Update our logging to be a little more helpful. And yeah, I think that's pretty much all we can do. Unfortunately.
**Riccardo Magliocchetti** 17:33 Kind of the way.
**Aaron Abbott** 17:35 Yeah. Go ahead.
**Riccardo Magliocchetti** 17:36 Yeah, do you remember? Like, what kind of like? If is it any particular library that uses this pattern of yielding or.
**Aaron Abbott** 17:48 Yeah, we've seen it in a lot of AI libraries, because they use. They tend to use asynchronous generators. So you see it in Openai, and also in the the Google counterparts.
**Riccardo Magliocchetti** 18:00 Good. Thank you.
**Aaron Abbott** 18:01 Yeah, actually, so what happens with synchronous generators is there's no error that gets sent out because basically, when you call token, dot sorry when you call contextvar dot, detach, token, or reset. I think it doesn't throw an error because the context appears to be the same object, even if the the value you're trying to reset is actually not in context anymore.
So that one's just kind of a silent failure, which I think is why we're seeing it more. See more bug reports for Async generators. But it's a bit of a foot gun in hotel, and I think we should probably just document it, and maybe add, like a a warning when we see if we can detect it for synchronous generators, too.
**Jeremy** 18:47 Wait. So if it's for synchronous generators, then is the is this issue some sort of like it? Does the issue arise just with like with and yield.
**Aaron Abbott** 18:59 Yeah, pretty much.
**Jeremy** 18:59 Not. Actually, it doesn't have to actually have to do the Async element.
**Aaron Abbott** 19:04 Correct. Yeah, it's the the Async one has a couple slight different variations, but the bug, the bug is equally affecting both. I'd say.
**Riccardo Magliocchetti** 19:25 Okay, thank you, Adam.
Next topic is also from you.
**Aaron Abbott** 19:33 Yeah, so there's been some back and forth on this bug, and I'm still.
I think we've we've uncovered one concrete bug that I'll open up a separate issue for which is related to Uvicorn, and like when you, when you sign a unicorn process, it seems to kind of hang you can dig into that and figure it out. But the the point I wanted to raise is, I'm not.
I'm not sure if the actual issue here and I don't know if the media is here.
I don't think so. Oh, yeah, immediate here.
Yeah, it's not clear to me. If there's actually an infinite loop through exporter when using otlp exporter like I.
I'm not sure what the expected behavior is.
and I think it would be helpful to get kind of like a some ux feedback from all of you, if you have thoughts, so so so sort of 2 questions is one.
If you start the the SDK kind of with this code, and there's no otlp endpoint.
Do you expect to see error messages, or do you expect to not see any error messages, because it seems like It doesn't seem like we have real agreement on that.
**Emídio** 20:55 I think we are in the problem of telemetry generating telemetry again on the feedback loop and descriptor provided what I'm getting is like trying to export the the telemetry.
It provides a logging error message, right? So.
**Aaron Abbott** 21:22 Yep.
**Emídio** 21:23 We start the loop again because we still have a log message to export the Qe.
So the queue never gets empty.
**Aaron Abbott** 21:36 Yep, that's right. So that's that's the case for this specific code. But you could imagine lots of scenarios where the exporting fails transiently. And you don't really want to drop those error messages right?
**Emídio** 21:50 Right.
**Aaron Abbott** 21:55 I mean, at least that's my take. But If anybody thinks otherwise, please please share cause I may. Maybe I'm being pedantic here, and I don't. I don't want to be, but I don't. I don't see like log logging errors being logged as a bug. I think it's kind of expected behavior. But we can definitely improve the Ux.
**Emídio** 22:20 Yeah for me. It's working like, when I have a problem to the collector, I can get a feedback. It's just the cost of having, like more logs being emitted, but not like a very expensive.
**Aaron Abbott** 22:37 Yup.
Okay. So 1 1 thing is, Dylan, I think, sent a Pr that would try to rate limit the I don't know if it was specifically for that error message, or if it was just for that log site, and I haven't. I haven't looked at the Pr. Too carefully yet.
but I think that would be a good ux fix, because at least, if the if the rate limiting interval is longer than the shutdown the default shutdown timeout. It won't add new items to the queue while we're trying to shut down, which is kind of a helpful.
Yeah, that that 1st one, I think.
Oh, immediately you requested changes.
**Emídio** 23:28 Probably.
**Aaron Abbott** 23:34 Yeah, alright. Seems it seems like pretty much the same conversation.
**Emídio** 23:39 Yup, per!
Let me see this pure.
Hmm.
yeah, it seems my comment was so it.
**Aaron Abbott** 24:06 Yeah.
**Emídio** 24:07 Hmm, I remember that discussion. We are basically deciding if we're going to use like warnings or doing some filtering on the logs message.
For some reason we don't. We didn't agree about using one is because that is a potential issue underlying when you use capture rewinnings.
**Aaron Abbott** 24:32 Yep, yeah. I think I feel like it's a little different from the tracing situation, because.
you know, spends would be created whether or not, there's success, whereas we're only logging any errors.
So it's not. It doesn't seem exactly the same telemetry induced telemetry problem because there's a real error that we're trying to represent here.
So I I don't. I don't think I mean I can. I can be opinionated and share my opinion, but I think the only way to really make progress on this is to have kind of a consensus from a bunch of people. So If you all have any thoughts, please share them on the issue, or feel free to speak up. Now.
**Pablo Collins** 25:20 I thought that the attempt to address this, what it did was it deduplicated the most recent log.
So if you've got a log in the queue, and another identical log is attempted to be written. Then it gets discarded. And that's the that's kind of the solution that was proposed. That's that's my understanding.
**Aaron Abbott** 25:47 Okay, yeah. It just feels hard to read.
Read the user's mind, like, I don't know if we have a if that's all. Like, some people want to count the logs right?
but I think this is a pretty standard practice, like in in other languages. There's really good support for deduplicating logs, or for doing like rate limiting out of the box. So
**Pablo Collins** 26:12 I I played with this a little bit. I made a little toy application, and the conclusion that I came to was this, was that the solution to this problem is to have a separate queue for logs during the outage, let's say, during the network outage. So an exporter.
when it encounters a network error, it goes into an error mode, and and all subsequent logs logged by that exporter get shunted to a separate queue, a waiting queue.
and then, once connection is reestablished. If it is reestablished, then that waiting queue gets merged with the standard queue.
**Aaron Abbott** 27:03 Is the goal just to not not use up space in the queue that could be used for other logs.
**Pablo Collins** 27:10 The goal is to prevent the attempt to export logs that were just written during the outage because that will cause potentially a cascade of of additional logs.
because those logs, when they're attempted to be exported.
cause additional logs to be written, which in turn, you know.
**Aaron Abbott** 27:34 Yeah.
**Pablo Collins** 27:36 So I don't know. I I played with this, and and that's the kind of the solution I arrived at. But then I figure, like all the other hotel languages, should be also grappling with the same issue.
I wonder if one of them has fix it.
**Aaron Abbott** 27:54 Yeah.
So I mean.
well, one thing is, if we're if we're thinking specifically about Otlp. So you have like one Otlp exporter. Right?
We have a a back off loop, and then I think the default periodic export is like I don't remember if it's 30 seconds or shorter, but I guess my point is, we're talking like on the order of maybe I don't know.
Probably no more than like 10 logs per minute, right?
Maybe like 20 logs per minute, right?
**Pablo Collins** 28:31 Yeah.
**Aaron Abbott** 28:33 So
**Pablo Collins** 28:34 So you're saying, it's not a problem.
**Aaron Abbott** 28:36 I don't. I don't know. Like It's all it's also.
**Pablo Collins** 28:41 Right now.
**Aaron Abbott** 28:41 No like like. If we add additional logging, then it would be it could be really spammy, or the logs could have stack traces and be really big. So I don't know if that captures the whole problem. And and I think our our queuing logic goes off the number of queues. Sorry number of logs in the queue like there's no size based heuristic for for one to start applying back pressure or dropping items from the queue.
So.
I don't know. Pablo. Is there any chance you could leave like a a comment with the investigation? It sounds really helpful.
**Pablo Collins** 29:15 Yes, sure.
**Aaron Abbott** 29:16 Okay, yeah. And and I agree we should check we should check. What other languages do.
I think I think Javascript has this separate Api for error logging within the SDK, they call it like diag But then that's kind of kind of gives you this chicken and the egg problem where you have to turn that on.
and then it just prints to to the console. So like if you, if you had something like a resource exhausted. Issue.
or something like that. And the logs don't end up going to the same back end. You would just kind of never see those logs so.
**Pablo Collins** 29:55 Yeah, that sounds totally reasonable.
**Aaron Abbott** 29:58 Yeah.
So yeah, I think if we take a look around, see what other people are doing, it'd be helpful.
**Riccardo Magliocchetti** 30:29 Okay.
Thank you.
**Aaron Abbott** 30:33 Yeah, that's all I had. If you want to move on, Ricardo, your mic sounds kind of marbled.
**Riccardo Magliocchetti** 30:39 Oh, sorry! Oh, there you go!
**Aaron Abbott** 30:41 Sounds good.
**Riccardo Magliocchetti** 30:45 Okay. So another comment.
oh, yeah, this was the last topic for today.
Okay, okay, so thanks. Everyone.
**Pablo Collins** 31:12 Yeah.
Thanks. Everybody.
**Keith Decker** 31:15 Thanks guys.
**Emídio** 31:16 Thank you.
**Aaron Abbott** 31:16 Alright. See you later.
**Riccardo Magliocchetti** 31:17 We'll see you.
