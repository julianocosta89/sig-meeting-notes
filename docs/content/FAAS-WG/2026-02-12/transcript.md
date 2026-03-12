SIG: FAAS WG
Date: 2026-02-12
Duration: 14 minutes
Zoom Recording URL: https://zoom.us/rec/share/2GY9tiMYKiI1B9T6Ha0UQe0KmtP6LhduxUMOV4PmrorO_ML2eefHSs6j0dzcWccI.o_63lDmviOvlo13t
============================================================

## Zoom Recording Transcript

**Warre Pessers** 00:52 Hello.
**Tyler Benson** 00:57 Hello, hello!
**Warre Pessers** 01:01 How you doing?
**Tyler Benson** 01:03 Doing pretty good.
So I've not been able to make it the past couple times.
**Warre Pessers** 01:14 Yeah. For me, it wasn't, easy as well. Had to skip some here and there, but, I think I'm getting some more time to, to work a little more on this stuff now.
**Raphael Manke** 01:33 Hello.
**Warre Pessers** 01:37 I'll turn on my cam as well.
Hello, Rafael.
**Raphael Manke** 01:46 Just wanted to say hi and listen in a little bit, because I have… This time I have some time in my calendar, so I thought I'd stop by.
**Warre Pessers** 01:55 That is nice, I think we can also use some help, because it's been difficult to get things really pushed through, and the start of the year for me personally has been very busy, so nice to see that some of you guys are, a bit more active as well.
I don't know if anyone else is joining, I saw… I thought that Lucas was definitely joining, but maybe he has… Time zone issue again, let me check.
And then, did you hear anything from Cirque and Tyler, or not?
**Tyler Benson** 02:44 He thumbed-upped your message, but I didn't see any response beyond that.
**Warre Pessers** 02:49 Because I did see he was, like, reviewing a couple of PRs just a minute ago.
And otherwise, I think we can start.
Let's see… Share the documents… Okay, so, not sure if any of you has any specific, things to discuss today?
Also, There's working. Raphael, I don't know if you have access to the doc. It's in the meeting invite, but I'll add your name here. Yes.
I think that's "-0, right? Yes.
Just like that.
Okay, hi Serkan, how are you doing?
**Serkan Özal** 03:59 Hello guys, I'm doing good. And you guys?
**Warre Pessers** 04:04 Yeah.
I'm doing good as well.
Little bit busy.
**Serkan Özal** 04:08 Yeah, same here.
**Tyler Benson** 04:12 Are you still dealing with, acquisition stuff, or what's the latest with you?
**Serkan Özal** 04:18 Actually, I'm no longer working with the… with the catch point and the logic monitor. I mean, since for some time, I had some… some ideas, and then I just started working on On one of the ideas, and… hopefully… actually, as of now, working on a prototype, and then we'll start talking with the VCs for funding.
But, yeah, I am… and the idea is about the, of course, the observability and the AI.
Yeah, we will see whether, I mean, there will be some interest from the VCs.
As of now, we have… I mean, I have 3… we have 3 people, from my… Old collects, and… yeah.
Busy days, and we have been working on almost 2 weeks on the prototype.
of… And planning to… to make a demo.
Starting from the next week to the VCs for funding.
**Tyler Benson** 05:26 Cool, congrats!
**Serkan Özal** 05:28 Yeah, thank you.
**Tyler Benson** 05:29 I'd love to… to hear more after this.
**Serkan Özal** 05:32 Yeah, sure.
**Warre Pessers** 05:35 Yeah, and good luck to your endeavors.
If no one has anything to kick this off, I can tell you what I'm working on currently. There was this PR from Lucas, he introduced the receiver for the metrics, A while ago, and now he added a… export interval, but I'm not really sure yet. I have to think about some stuff regarding, like, the AWS Lambda, lifecycle.
To see if this is a good fit, I'm struggling a bit, but I was getting to it just before this meeting, so probably will finish up this evening. And other than that… Right before the new year, I opened a PR on the SemConf repo that didn't get any traction yet. It's still for supporting the propagation of trace context in SQS. I am looking forward to joining one of their meetings to talk to them, because I did chat to them a bit in the past, but, I think to get this unblocked, I'll have to, sit in on one of their meetings and, yeah, like, talk to them like that.
And then hope that sometime soon we can, finally gets something… Working for that.
in the JavaScript instrumentation as well.
**Raphael Manke** 07:18 Do you have a document for this work, or…
**Warre Pessers** 07:21 Like, not really, like, a running document of findings, or I don't know what exactly you mean, but I, I did open just issues, on their, on the semantic conventions repo, and I also have an open PR, on the JS Country repo.
But so, like, the actual changing of the documents, if the SEMCOMF people agree, still needs to happen after we discuss the issue. I didn't open a PR yet, just the issues.
**Tyler Benson** 07:57 Would you mind pasting a couple of links for context into the agenda?
**Warre Pessers** 08:02 Yeah, is it okay if I do it after, then I can…
**Tyler Benson** 08:05 Yeah, that's fine.
**Warre Pessers** 08:06 separate links, so I'll do that.
I'll just… Put a placeholder here, so I don't forget.
Don't know if anyone else has something to discuss today?
**Raphael Manke** 08:24 So, I'm working on the account ID, Cloud Account ID PRs, which is spread across a lot of all the instrumentations and, resource detectors. So, I think I opened up the… auto collector one for the extension as ready already, because once that is merged, I think it's easier for the other instrumentations to point to that to see that the capability is finalized.
And, yeah, then I will catch up with the other PRs on the other instrumentations.
**Warre Pessers** 09:00 Okay, cool, yeah, I did see you open a bunch of those PRs. I don't know if anyone else has taken a look yet, but I can take a look after, Otherwise, for the collector one.
**Serkan Özal** 09:11 Yeah, well, so I have… Yeah, also, I have a few, I mean, PRs, I mean, approached, I mean, approved and approached, and I will share the links of those PRs, so… I think, I mean, some of you guys already approached those PRs, so if you're okay with that, I think we are, we are okay to merge them.
Just after the meeting, I will share the list.
**Warre Pessers** 09:39 Yeah, that sounds great.
Okay, anything else for the agenda to discuss right now, or… All good.
Because I do have one action item, I just wanted to ask, maybe it's time for a release soon?
So, if everyone thinks that's a good idea, I will get started on, well, first, let's wait until all Dependabot stuff, is merged, I can look at that as well. And then I will have to do some testing, because, of course, we still don't have, real integration test suite, so it'll be manual for now, and then if everything's good, I will, go ahead with releasing that if you all think that's a good idea.
**Raphael Manke** 10:34 We also added.
**Tyler Benson** 10:35 Actually.
**Raphael Manke** 10:35 I had a customer complaint that the auto collector layer right now has, like, 5 CVEs open, based on the Go version. I hope that some of them are gone with the upgrade.
**Warre Pessers** 10:48 Yeah, I guess, I guess they will, we'll, look at what's open for Dependables, and then, I can take a deeper look into the CVEs if you want, and then, we can make sure that the latest…
**Raphael Manke** 11:01 Yeah, the list, yeah.
**Tyler Benson** 11:03 I don't think that the Dependabot upgrades the, the Go version, inherently.
**Warre Pessers** 11:09 No, I do remember someone opened the PR for this, like, a week ago, and we merged it, so… I think it is fixed, but, it is a manual process indeed.
**Tyler Benson** 11:20 Yeah, it's unfortunate that it doesn't update that.
I don't know if that's intentional, if there's… I'm not super familiar with Go, so maybe it's not good to automatically update the Go version? I don't know.
**Warre Pessers** 11:38 I have no clue myself, not really a Go expert, but I can take a look into that as well when I'm doing this anyway, so… I'll just, Noted down as well.
**Tyler Benson** 11:53 If you run into any hiccups during the, the release process, let me know, and I can try to help out.
**Warre Pessers** 12:00 Okay, great. Like, yeah, I remember, like, last time, I pushed the tags the first time, and then it didn't trigger the pipelines, but when I deleted and pushed them again, magically worked, so… Hopefully it goes as smooth.
**Tyler Benson** 12:25 Sounds good, though.
**Warre Pessers** 12:26 Okay, then, I have nothing else for today. Again, I do think that Lucas has some stuff he wants to talk about, and he already showed some interest in, like.
driving the effort for adding integration testing, because for now, I only have just an issue on our repo open for that, but, he seemed very eager to, to get that going, that effort, so I'm looking forward to when he can introduce himself here. But I'll check in with him after the meeting, if… maybe it's the time, I don't know.
I'll ask, if it's difficult for him to attend.
And then that's it for me for today, nothing else.
**Tyler Benson** 13:18 Ew.
Serkin, good news for you.
Daylight savings time will be over in a month.
**Serkan Özal** 13:25 Yeah, yeah, I think, I mean, in… starting from the next month's, I mean, next month.
It'll not be an issue, but, yeah.
I think no need to… no need to change the… change the time to… I mean, one hour before, because starting from the March, I think… It will not be… 7pm in my local, but to 6PM, and that will be okay-ish for me.
**Tyler Benson** 13:57 Sounds good.
**Warre Pessers** 13:59 Okay, yeah, I'll, I'll check in with Lucas then, and we'll see, what he says. But anyway, thanks for attending today, and for all your input, and also nice to meet you, Rafael, because I don't think I've seen you here in person before.
**Raphael Manke** 14:16 I was here only once.
**Warre Pessers** 14:18 Okay.
**Raphael Manke** 14:19 But I'll be at KubeCon in Amsterdam, so if anyone is on-site, I'm happy to have a coffee or something.
**Warre Pessers** 14:26 I wanted to come, but couldn't make it this time. Some other people from my company are attending, but probably less with observability focus in mind, so… But I'll tell them to check out the dash zero, stand.
Okay, cool. Thank you all, and see you next time, I guess?
**Tyler Benson** 14:51 Thanks, Rory.
**Serkan Özal** 14:54 Bye. Take care.
