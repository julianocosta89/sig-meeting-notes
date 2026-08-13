SIG: OpenTelemetry .Net Auto Instrumentation SIG
Date: 2026-08-12
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Zach Montoya** 05:02 Hey, Alexey!
**Alexey Pukhov** 05:04 Hey, Zach.
**Zach Montoya** 05:07 It's like we navigated the, new meeting link.
**Alexey Pukhov** 05:11 Yeah, I was like, oh, looks like you need to have an account. I'm like, okay, I'll just figure that out later, I'll join as a guest.
I think everyone is just struggling with this.
**Zach Montoya** 05:25 Yeah, I don't think we're in any rush.
You can just keep waiting for another, like, 5 minutes and see if anyone else, is able to join us.
**Alexey Pukhov** 05:34 Sure, yeah, definitely. Well, at least on our meetings, they were discussing Joining SIG, so I'm expected.
some Cisco guys.
Okay, quick update.
A couple of our folks said that they are on a meeting, but there is no one there.
**Zach Montoya** 07:42 Oh.
That's strange.
**Alexey Pukhov** 07:44 Like, there are two meetings, let me… Let me send them the link that I used to.
to get here.
**Zach Montoya** 07:52 Okay.
**Alexey Pukhov** 07:53 That's funny.
Okay, I send them the link.
Is he eager?
**Igor Kiselev** 08:59 Yes, I drew it.
**Alexey Pukhov** 09:02 So, Igor, did you navigate the lagoon?
**Igor Kiselev** 09:05 No, I just clicked, like, connect as a guest.
**Alexey Pukhov** 09:09 Connect as a yes, and then you just get the regular WebEx link.
**Igor Kiselev** 09:13 Yeah, but it's different length than it was in a calendar before, because first I was seated in a room, probably with Pukhar, where I connected through my calendar event.
**Alexey Pukhov** 09:25 Oh, I see, because, yeah, I usually go to… I usually click on a link to show the whole calendar, then I go to Wednesday.netseq and click there.
**Piotr Kiełkowicz (Splunk Inc.)** 09:41 Hey guys, sorry for being late.
**Zach Montoya** 09:45 No worries.
**Alexey Pukhov** 09:46 You're not the only one.
Piotr, did you have any issue getting into the meeting today?
**Piotr Kiełkowicz (Splunk Inc.)** 09:55 Not today, yeah. Just, I forgot, thus, I've missed the notification.
**Alexey Pukhov** 10:03 I see.
**Piotr Kiełkowicz (Splunk Inc.)** 10:12 So… Zach, do you want to drive the meeting, or no?
**Zach Montoya** 10:18 No, not really today.
**Piotr Kiełkowicz (Splunk Inc.)** 10:21 So, so I need to… One more minute to prepare.
**Zach Montoya** 10:26 Okay, thank you so much.
**Piotr Kiełkowicz (Splunk Inc.)** 10:30 Because I've lost the… Our docs ring.
OpenTele requests.
And, starting sharing the screen… Come on.
Can you see the screen? Yes?
**Zach Montoya** 11:32 Yep.
**Piotr Kiełkowicz (Splunk Inc.)** 11:34 Right, so, from the top, I've played a bit with, AI tool.
And I was able to speed up, kind of, native code sync, Zach, so it would be great if you can review it and explicitly accept.
With some… with some comments.
**Zach Montoya** 11:54 Yep. Yeah, I'll take a look.
**Piotr Kiełkowicz (Splunk Inc.)** 11:56 There is not so much commit just… just for the cleanup.
But it was kind of… the test one, not to… to bring too much in one batch for… for the… for the AI tool.
Fortunately, most of the code in this tags on the Datadoc site was related to the profiler, which is not part of… our distribution All to ours.
So, the next one is NPG SQL trace contact propagation. It is heavily AI-assisted, but… I review it, test it, and I think it is pretty solid.
The overhead is pretty big, because we have additional run trips to set and set the application name.
It was expected penalty, but, The customers may be not fully happy with the solution.
But as we consider it as a temporary solution, and the final one will be Implemented by NPG SQL team directly.
I do not see any better options, but… Please review.
When you have some time.
I know that 1,000 clients is… is big, but… But it is.
We should upgrade to Jaeger 2, our… Documentations.
And demo. I didn't have time yet to verify if it is really working or no.
But if you have time, it would be great to review its potential immersion. Unfortunately, Altar does not respond if he was testing.
Yev Gianni is not with us, but I think he's working with FDCAR.
So, maybe, eftika, you can share something?
**eftiquar shaikh** 14:19 Yes, so… Yeah, sorry, I was on mute.
This Pierre is more complex than it appears on the surface.
I have posted my comments in the conversation section. You already see I chose design for… yeah. So that's the key thing.
The problem is, especially in the multi-app domain scenario.
Initially, it was just a single service, and you start, and everything works fine, but now we are gonna… Start and stop and update the configuration, so the profiling service is not designed to handle this.
And given the complexity and surface area, first the profiler service itself needs to be cleaned up. It should support, idempotent start and stop, so that it reaches the complexity.
And bootstrap it once, and at runtime, apply the configurations, and make sure that there is a precedence order, because if OPAMP and App Domain, if they race against each other.
The OPAMP configuration should precedence… take precedence over the app domain or initial seed configuration. So all these details first need to be frozen in a contract, which I am working on right now.
And if need be, I might shoulder the responsibility of implementing on the native side. It depends on how UVA wants to proceed.
But the first contract needs to be in place, which is not there.
To give you an example of additional complexity.
If you stop the service mid-capture.
then the semantics need to be defined. Right now, the service only respects shutdown signal. If you pause the sampling service, it needs to pause at correct boundary, either finish the sampling of current thread.
or a bot export altogether. These nuances need to be handled, otherwise we'll mess up the way the CPU profiling, because it uses cumulative computation to show the CPU profiles. If you just send a truncated sample, it'll mess how the UI renders the CPU sampling.
So all these things need to be factored in. And… Opam signal can start and stop service dynamically, and if we… need to handle… if we handle that gracefully, we make sure that the thread joins and thread starts, so they don't lead to complications, because starting a thread and waiting for that thread to complete exist… finish is a complicated process, so we have to have a protocol. Ideally, the thread should be started only once, and stop… should pause the thread. It should not just kill the thread, because again, start signal can come anytime. So, keep it warm. So, all these semantic details need to be first frozen in the contract.
native side, it should not worry who is calling the config, it should just worry about precedence. So, there are a lot of nuances in this. I have… I'm in the middle of building the contract, I will share the contract in this PR. Yueni and me are scheduled to talk tomorrow in the morning, and we will update more details on that.
But…
**Piotr Kiełkowicz (Splunk Inc.)** 17:25 Great.
**eftiquar shaikh** 17:26 It's more complex than it appears.
**Piotr Kiełkowicz (Splunk Inc.)** 17:29 Okay, great, great to hear that.
**eftiquar shaikh** 17:32 Thank you.
**Piotr Kiełkowicz (Splunk Inc.)** 17:37 Oh… Messaging cluster, I think it was merged in the semantic conventions.
And I need to review this, but if you have time, also, feel free to pick it up. I'm not sure if I will be able to do this tomorrow.
NET 11 support… For now, it is passing… Preview 7.
So we are in the pretty good shape, but we still have, alexey has a lot of plans to verify The changes in the compilation.
the .NET 11.
There is a suspicion that we will need to… Adjust our… quotes.
Yep.
And we have also this MATS PR long opener.
We have just deprecated it.
No, not the precise.
I'm not sure if we can do anything more with this today.
So… I've lost… Notifications, sorry guys.
the… new issues.
We have two new issues.
This one is in progress, I will put it into the next milestone.
This guy is working on this.
Igor? Alex, did you have a chance to look into this, or… Not yet.
**Alexey Pukhov** 20:43 Yeah, no, unfortunately.
**Igor Kiselev** 20:46 we haven't looked and trade, but at the same time, we… Alexey… Alexey have plans to restore, for startup hook, a script that will create, the.
**Alexey Pukhov** 21:00 additional dependencies.
**Igor Kiselev** 21:02 folder, which will return to a status quo that we had before we merged our changes, and using that script, if will not work in .NET 11, and that's why we need to restore it back to to that state, which we discussed originally, and the same thing would, be… would make possible to use, in .NET 10, so… It's flat. Despite we have not looked in trade, the change that will solve that problem is already planned.
**Piotr Kiełkowicz (Splunk Inc.)** 21:39 So, it should go to .NET 11 release.
milestone.
**Igor Kiselev** 21:43 before .NET11 release, but it may be earlier.
**Piotr Kiełkowicz (Splunk Inc.)** 21:47 Sure, but putting it…
**Igor Kiselev** 21:49 milliliter, milliliter, yep.
**Piotr Kiełkowicz (Splunk Inc.)** 21:52 than that. Okay.
Oh, that's all.
And what else? Discussions… No dis… no discussions at all… The next milestone is 17, probably.
Or 16, whatever.
Nothing interesting there, and the project board updates.
I do not think that we need to update anything here.
Do you have any other topics for today?
Nope. Okay, so, stay here in September.
**Zach Montoya** 23:19 Alright, thanks, see you.
**Alexey Pukhov** 23:22 Bye!
