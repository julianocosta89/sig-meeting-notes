SIG: OpenTelemetry .Net Auto Instrumentation SIG
Date: 2026-10-21
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Eftiquar** 03:43 Are we gonna skip today's meeting, or waiting for someone?
**Mateusz** 03:51 Yeah, so probably, let's wait 2 more minutes, and if no maintainers join, we can skip.
**Eftiquar** 04:02 Sure.
905 can be better.
**Mateusz** 05:41 Yeah, so it's 5 past, I think, considering it's only… oh, Zach joined.
**Eftiquar** 05:49 Oh, look.
**Zachary Montoya (Datadog, Inc)** 05:56 Hello.
**Eftiquar** 05:57 Hello.
**Igor Kiselev** 06:01 Bye.
**Zachary Montoya (Datadog, Inc)** 07:00 Alright, I can, get us started.
**Eftiquar** 07:07 Sure.
**Zachary Montoya (Datadog, Inc)** 07:11 Or if it's… Alright.
Sue… Let's do this… Boom.
Yeah, let's go through.
Alright, in terms of open pull requests… It's like we have, sort of the same, the same set as before. We got some Kafka ones, some RabbitMQ, IBM MQ, I think this one I was supposed to take a look at, I haven't yet.
And then we also have the unsafe accessor type, so now this one is ready for review. How is… how's this one going?
**Alexey Pukhov** 07:57 This one has actually get approved, but I just received a few comments from Pyotr.
So I'll just address them, and push a new change into it, and, I mean, it's almost done.
**Zachary Montoya (Datadog, Inc)** 08:11 Okay.
Perfect.
Yeah, See, I don't think there's been any progress on the resource attributes. So, yeah, we have a couple. I haven't had time to take a look yet. I have been looking at some of the native updates that Piotr, added.
But… Got some bumps.
So, are there any, any PRs in particular that you guys, need help with or need reviews on at the moment?
**Mateusz** 08:44 Actually, Zach, I think this one related to resource attributes was updated, I think, even yesterday.
Oh. Yeah.
**Zachary Montoya (Datadog, Inc)** 08:51 Okay.
So I could scroll down… Oh, you're right, okay.
Okay, great, okay.
Sorry, sorry for the scrolling, Okay, yeah, update it to Maine, and I can manage it to local. Okay, cool. Glad to see some new changes.
Alright.
Cool, yeah, I'll take a look.
To see if it sort of satisfies the criteria that we… that we had.
So, we'll basically… Support… per app domain configuration. So basically, like, per web app.
As well, supporting app config, web config.
Let's see… So right now… not, per domain… not prep domain YAML… And… no interpolation… Resource attributes should not be merged.
And then we could do as many. Okay.
Cool, yeah, this'll be one to… See if we can, help get this one reviewed and pushed… pushed through.
Alright, yeah, if there's, no, like, active discussions you guys want to open up on these, we can keep going.
New issues… Yes, I think this one… Okay, so we have a couple of the… the Red MQ, some OpAmp.
a line process name, and then the duct typing one, I think this one was, done with… from one of the updates of… the native updates.
so I'll have to resolve that one.
Okay.
Yeah.
So, I guess nothing… nothing new at the moment.
But these are, you know, up for grabs if anyone had the inclination to do them.
Discussions… nothing.
Made sense.
Milestone… Let's see… 116?
Alright, so no… no issues at the moment.
About 118.
Yeah, okay.
Let's check 119 as well, okay.
Alright, so nothing there that is not sitting on the project board.
And then the project board, we have… again, some of the open PRs that… we have them in progress here. For .NET 11, we do have the runtime async support, and I… I think, if I recall, we were… Trying to get the native updates.
Sort of up to speed, and then applying the runtime async on top of that.
Is that sound… Correct, or are we… should we be looking to merge the runtime async Work, more immediately.
**Eftiquar** 12:30 I think the order is still… Gonna pull some upstream changes, as far as I know, this week.
And then I'm… then I think Igor and me, we will review together and take collectibles.
**Zachary Montoya (Datadog, Inc)** 12:46 Okay, cool. Yeah, that was my… my impression, just wanted to make sure.
**Eftiquar** 12:50 Yes, you're… you're correct.
**Zachary Montoya (Datadog, Inc)** 12:53 Okay.
Cool. Yeah, I think that's the biggest thing, tracking for .NET 11, that… and or any SDK updates.
And then the unsafe accessor, because this one will, be affected on .11, but this one is… In progress… is this… Is this one tracking the same PR?
Or is this a different PR?
Oh, okay, yeah, I believe that is St. Pierre.
Okay, I will move this to… In progress… So that's… Still checking this one really quick.
Double-check if we have any… There's any progress on this on our side?
**Igor Kiselev** 14:08 Let's see… should we already, try to close that issue?
**Alexey Pukhov** 14:14 No.
**Igor Kiselev** 14:14 Workaround provided, or…
**Alexey Pukhov** 14:17 Yep. Or we still need…
**Igor Kiselev** 14:18 to do something more, we… because we talked about that we probably need to add a detection to disable if it is a different profiler.
**Alexey Pukhov** 14:28 Yep, so, yeah, thank you, I was just distracted. So, yeah, I replied to that ticket, a quick, context. So, I reproduced the issue. The problem was… the regular reflection, in some cases, I mean, in this particular application, when we set up a contextual reflection to support the regular reflection, it just doesn't flow everywhere.
And this is unfortunately… I mean, nothing we can do about it. That's how .NET Runtime Orchestral, spawns those additional execution flows.
So, we can only Accept this limitation, and the suggestion was to use the additional dependencies workaround, which we brought back.
Or fix the dependencies manually.
If you're not using the framework-dependent application.
And, yes, there was this, additional… so, I mean.
From that perspective, yeah, this… we can just close this issue. I mean, there's nothing we're gonna be doing. But there is a separate, concern. We really do not check the profiler ID in startup hook isolation, so we just react to the fact that a profiler was configured.
So that is something unrelated to assembly conflict resolution, but we probably need to file… to do a follow-up here.
Somewhere, yeah, it's that section.
**Igor Kiselev** 16:00 Let's, let's do that. Let's try to open, a new ticket about, profile ID that we do not shoot ProfilerID, and, close that issue, since it, we, we already done everything, what we can do, so we restored additional dependencies.
And so there should be character expectations that no additional work will be done here.
**Alexey Pukhov** 16:25 Yep.
Okay. Perfectly for the conflict resolution. By the way, a quick comment. Now that I look at this, I mean, when I looked at this issue and realized, I mean, it's probably gonna happen for any MVC application, if not for other types of applications, that just makes startup hook-only isolation… Very, very… I mean, the use… the usability of this isolation is very limited. I mean, at this point, we can actually think about just retiring the startup hook-only isolation and relying solely on the additional dependencies for conflict resolution.
**Igor Kiselev** 17:03 We are… it's, again, only a… we are talking only about station where Profather is not involved.
**Alexey Pukhov** 17:08 Yep, yep. Only startup hook, only deployment.
I mean, this is really limited.
Yeah, it's just a thought. We don't have to decide on this right now, but this issue just shows how fragile a startup hook-only deployment is, and really not much we can do to support an automatic conflict resolution there.
**Igor Kiselev** 17:35 We knew it and been used by .NET 11.
**Alexey Pukhov** 17:39 Exactly, we…
**Igor Kiselev** 17:40 Still need to do something different.
So, that's why we… it's fully according to our plans and our discussion when we edited.
**Alexey Pukhov** 17:49 Yep, yep. Microsoft didn't provide much capabilities, they didn't want to do anything. They are the only users of the startup hook-only deployment. Most of the customers use Profiler.
So that's why, I mean… It's just a question, do we really want to keep that complicated isolation logic that is not that…
**Igor Kiselev** 18:14 the Lord be…
**Alexey Pukhov** 18:14 It's becoming less and less usable.
**Igor Kiselev** 18:17 Probably not needed, because in .NET 11, as soon as we release .NET 11 version, and we will migrate to a new version of System Diagnostic Assembly, startup hook only isolation would not be able to resolve it for .NET 10.
And that time, it would be great to remove that code.
Because it would.
You will…
**Alexey Pukhov** 18:46 Hold on, it will… it will, I mean, it may work, because it will always, push the diagnostic source to the default context.
That's why we did it.
That's why we did.
**Igor Kiselev** 18:59 No, we discussed that it would be not because .NET 10 comes with System Diagnostics . And we would need System Diagnostics 11.
That's why we originally said that by a .NET 11 release, we would need to.
**Alexey Pukhov** 19:15 Oh, right.
**Igor Kiselev** 19:16 So…
**Alexey Pukhov** 19:17 Right, right.
**Igor Kiselev** 19:18 be even more limited, but it's a separate discussion. We could file a ticket for it and discuss it in a separate ticket. So, how we should remove it, when we should remove it.
**Zachary Montoya (Datadog, Inc)** 19:33 Alright, so for… so for now, what we can do is we can close this, noting that the workarounds, like, highlight the workarounds that we do have, noting this is a limitation of the startup hook isolation.
And then just, create a separate, issue that, so that we don't, we additionally check the… the CLSID before…
**Igor Kiselev** 19:59 Yes.
**Zachary Montoya (Datadog, Inc)** 19:59 Determining that we are in Star Pukh only, okay.
**Igor Kiselev** 20:02 Yes, it would be… it would be the best.
**Zachary Montoya (Datadog, Inc)** 20:05 Okay.
Okay, cool. I can, I can just say that in a second.
Is there anything else?
So this will be… yeah, I'll respond on this one, and then that'll be close, and then the only other one we have committed is the ASP.NET Core hosting startup assemblies. Not sure if we're… You know?
**Igor Kiselev** 20:28 Nobody really interested in it too much, so it would not… it would only slightly improve package structure, but we need some time.
Do a thoughtful review of… and by analysis to check it, because…
**Zachary Montoya (Datadog, Inc)** 20:48 Yeah,
**Igor Kiselev** 20:49 Easily push it later.
**Zachary Montoya (Datadog, Inc)** 20:52 Yeah, I don't… I don't mind putting this back into the backlog, like, I don't see an immediate…
**Igor Kiselev** 20:57 Sure, let's move it into backlog, because, All our initial knowledge is done, and unless there would be some more people who are interested in validating it and checking it.
nothing happened, nobody is interested in that, because it will be only a nominal problem.
Yep.
**Zachary Montoya (Datadog, Inc)** 21:21 Cool.
Alright, so this looks… It's good.
Yeah, I mean, I… I'll update that other ticket, but otherwise, I don't have much here.
Is there anything else that we should discuss right now?
**Eftiquar** 21:45 All good.
**Zachary Montoya (Datadog, Inc)** 21:49 Cool.
Alright. Nope, thanks everyone for your time.
**Eftiquar** 21:53 Thank you.
