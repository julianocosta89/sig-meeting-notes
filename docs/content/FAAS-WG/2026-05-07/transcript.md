SIG: FAAS WG
Date: 2026-05-07
Duration: 23 minutes
Zoom Recording URL: https://zoom.us/rec/share/Pfj4NvZmXHjgRkZRFCfp08J9L8XqDc_kAKtHwRE0U9yVP4IzOYPZZKBoSjPBr-RB.cRGW64-L7HW4nkyJ
============================================================

## Zoom Recording Transcript

**Warre Pessers** 03:25 Hello.
Hello? Are you muted? Let me check if I can, kick this bot from the meeting.
Hmph.
Don't think I can… I know Tyler somehow… Was able to remove the bot last time, but… I'll have to ask him how to do this.
**Raphael Manke** 04:07 I will have to… some meeting ownership rights, so…
**Warre Pessers** 04:13 Yeah, I probably don't have those.
Yeah, doesn't matter, I guess.
Just going to wait for, Serkan, because he was going to join as well, and then we can get started.
**Raphael Manke** 04:39 Hello, Lucas.
**Warre Pessers** 04:47 Hmm.
Hello, Serkin.
**Serkan Özal** 05:36 Hello. Hello, everyone. Hello, Rory.
**Warre Pessers** 05:41 Do you know by any chance, how we can get this note-taking bot out of here? I remember that Tyler kicked him once, but I don't seem to be able to.
**Serkan Özal** 05:50 I see, but no idea, honestly.
**Warre Pessers** 05:55 Yeah, I guess it's fine for now, but I'll check with Tyler to get him out of here next time. Let's see, I'll share… the document… Alright, haven't really thought about what to put on the agenda for today. I can tell you I've been, starting to look into the integration tests, since I now have access to, to the AWS account.
And I've also been looking at doing our next release, but then a bunch of Dependabots PRs came in, so I'm going to… I have, I think, a couple to look at, and then I'll continue the process, and then probably tonight or tomorrow, I will do a quick release, and then for the next release, we should hopefully be, ready with the integration tests, so can go a bit quicker.
I also asked the question about, IAC tool preferences. I've done a little bit of… comparing, and I also think I'm leaning towards CDK now, because it seems like, having an actual test runner, like, Jest, for example.
will make the assertion part of the integration tests a little bit clearer and just more ergonomic. So I think it'll probably be CDK if everyone's on board with that.
**Raphael Manke** 07:38 Yeah, so we, in our Lambda extension that we released soon, we also built it based on CDK and made it very easy to iterate about different scenarios in different languages, because you can parameterize all the template generation. So, yeah.
**Warre Pessers** 07:57 Yeah, that makes sense.
I'm not a big kind of CDK expert or anything, but I'll obviously share the PR, so any feedback will be nice there.
**Raphael Manke** 08:14 I can help you.
**Warre Pessers** 08:16 Okay, thank you. So that was for the integration test, progress, then I see Lucas also added an agenda item.
**Lukas** 08:26 Yeah, this is more just, like, informational, but… I guess, since Serkan is here… I noticed that you opened an issue a while ago, like, in the Python, repo for, like, the cold start of the OTLP HTTP exporter, so I'm actually working on trying to get some… changes made so that we can actually, like, use our own HTTP client transport?
So, this should give us, like, a couple hundred milliseconds to the cold start time.
For Python, at least. So, yeah, just… just kind of… just informational, I guess. I don't know if anyone has any comments or suggestions on that, but yeah, this is just for Python as well.
**Warre Pessers** 09:16 Cool, I think that's nice. Always good to have some optimizations in that regard. I'll take a look at your PR just to understand a bit better what you're doing after the meeting, but I think it's nice that this is being worked on as well.
**Lukas** 09:30 Yeah, so once… assuming this eventually lands, we can switch to using, like, a URL lib client, so we will actually not even need to import anything, no requests or anything, which will… which should improve cold starts quite dramatically.
**Serkan Özal** 09:47 PR, PR is in the Pything country prepper, right? In the Corporation.
**Lukas** 09:52 in the, the main Python repo. So the idea is that it, like, we… this will actually generalize the HTTP exporter.
**Serkan Özal** 10:02 August.
**Lukas** 10:03 plug in whatever… Transport you want.
**Warre Pessers** 10:09 It makes sense.
now that I think about it, I also have another update. So, some of you may remember, but there's this, pull request that's been open for a long time on the JavaScript contribo to add SQS context propagation.
I've finally gotten… a bunch of reviews the last… two, three weeks from the people over there, and the code owner for the package was, happy with it and approved my PR, so we should be, finally getting that merged, hopefully sometime this week or next week. So that'll be… a gap, that we have finally filled, then, for the Lambda instrumentation.
So that would be cool, too, to get that, I might wait for the release for the JavaScript layer until that's merged, but I'll check in with the, maintainers, Regarding when they will release, but Just wanted to mention that this is finally getting wrapped up.
**Raphael Manke** 11:23 What is a big change in this new way?
**Warre Pessers** 11:27 So the JavaScript instrumentation it has support for propagating context over SQS when you use the AWS SDK, so you can add context to a message, and you can also parse it from a message, as long as you're using the SDK, but as you know, when we work with Lambda.
You don't use the SDK to pull messages from SQS, you just have an event source mapping. Your handler looks a bit different, and you get an incoming SQS event.
in your… in your Lambda function, so… We had to… basically just add parsing of the message attributes to the AWS Lambda instrumentation for whenever we're dealing with an SQS handler, of course, to also be able to propagate the context there.
**Raphael Manke** 12:25 And then you do spam linking, or, continue the trace?
**Warre Pessers** 12:29 Yeah, so we do span linking, but this is where a lot of the confusion came from, that it used to be one process span per message in your batch, with its own dedicated link back to the producing span.
And there have been some changes made to the messaging spec, which have already trickled down into the AWS SDK instrumentation, but haven't really propagated through all the specs themselves.
which means that now it's okay for us to do just a single process span that just has a bunch of span links to all the messages instead of all separate process spans, so that's how we did it here as well. Because the message was to just adhere to the messaging spec, and not really those very highly detailed, Lambda-specific specs and SQS specs that are floating around, but that are not always up-to-date.
**Serkan Özal** 13:33 As far as I remember, you were, patching the loops in the JavaScript, right, to create their own individual, consumer recipients for each SQS message, right?
**Warre Pessers** 13:49 Yeah, that's how I implemented it initially, back when we were doing a process span per message.
But that wasn't necessary anymore with the new approach, and it's also something that they explicitly… removed in the AWS SDK instrumentation, because it was a bit flaky, and I think maybe, there were some issues with test setup, but I don't remember exactly Why they, they preferred not to do that, but… So, probably, since you last, remember, the code has changed a lot, but I can… if you want, I can quickly, pull up the PR here again.
**Serkan Özal** 14:38 No, you can just send the link, I mean, I can check it out later.
**Warre Pessers** 14:42 Sure, I'll add it into the document, and then check it out. It currently still has a test failure, but it's due to a change in a different package, so I have to contact The maintainer and, hopefully, we can get that sorted out.
**Raphael Manke** 15:04 But this is then only the behavior for JavaScript, or also for the other languages?
**Warre Pessers** 15:09 So this is only for JavaScript. I know that, for Java, it is already… It's already implemented, so… kind of lost my train of thought, but for Java, it's already implemented properly. I spoke to Tyler about this a long time ago, and it seemed like it was all… fine. For Python, I'm not sure, and for Ruby as well, I'm not sure. I'd have to, I'd have to check. But we can start opening issues, maybe, to… to track some work, to do the same stuff there that we did here.
Just to get it everywhere, so… I'll add that to the action items, that's a good point.
**Lukas** 16:08 Yeah, I know last time I mentioned I can… I can definitely help out on the Python side, I think I I can't remember if I took a look at the Python implementation or not, but I think, yeah, there might be some changes required.
**Warre Pessers** 16:22 Yeah, I do remember that we spoke about this a while ago, but yeah, that would be nice to have some help there as well. I'll, keep you posted when I have opened the issues, and then we can… We can see from there.
Right… I personally don't have anything else to discuss for today, but… Do speak up… do speak up if you have any other topics to discuss.
Okay, then, I guess, have a rest… a nice rest of your day, and I'll see you in two weeks, and also in chat, of course, we'll, stay in touch.
**Raphael Manke** 17:09 Okay, thank you.
**Warre Pessers** 17:11 Bye, guys?
**Serkan Özal** 17:12 Take care, guys.
**Lukas** 17:13 Thanks.
