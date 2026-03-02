SIG: Community Demo App SIG
Date: 2025-08-13
Duration: 12 minutes
============================================================

## Zoom Recording Transcript

**Alessio** 03:39 Hit.
Can you hear me?
Cool.
Let me just raise the volume, I think, because I hear you very low, I don't know.
**Roger Coll** 03:52 Yeah, it takes 20 seconds, now it should be good to….
**Alessio** 03:56 Okay, now it's good.
**Roger Coll** 03:58 I don't know what's going on with my mic, but it's always the same, it's….
**Alessio** 04:03 I don't know.
**Roger Coll** 04:03 I need to start talking, 20 seconds before, so….
**Alessio** 04:09 You need to prepare, ….
**Roger Coll** 04:11 Yeah, yeah, yeah.
**Alessio** 04:12 Low stars.
**Roger Coll** 04:13 Random words, and after….
**Alessio** 04:14 Yeah.
**Roger Coll** 04:15 20 seconds, the… I don't know if it's selling nutrition or what's about that.
**Alessio** 04:21 Hold on.
**Roger Coll** 04:23 Okay, let's see… yeah, probably….
**Alessio** 04:26 you know?
**Roger Coll** 04:26 Yeah, exactly.
**Alessio** 04:27 Everybody else joining.
**Roger Coll** 04:29 Yeah, probably… I don't think so, maybe…
During these days in summer, it's…
Yeah, it's probably that, yeah, most of the meetings get canceled, or at least.
happened to me last week with a couple more in the OpenTelemetry, so….
**Alessio** 04:47 Okay, because I noticed that Giuliano is in….
**Roger Coll** 04:53 Is it Juliano or Giuliano? I don't know. I don't know. Anyway, it's fine.
**Alessio** 05:00 I noticed that he's on vacation, and … yeah. I didn't have much, I basically had just the… like, I opened up very much draft PR for the… for the Elixir rewrite.
DUI.
Cool. But it's….
**Roger Coll** 05:19 Yeah, I just went through very quickly. I saw that it's, …
Yeah, it's a bit weird, but yeah, once you….
**Alessio** 05:27 Yeah, it's a lot.
**Roger Coll** 05:28 Yeah, I saw that, I don't know, maybe 45s or 25.
**Alessio** 05:33 Yeah, because it's basically the whole thing, like, the whole scaffolding of the service, plus all the… for example, the CSS and stuff like that, so it's…
I don't hope to get a review, like, soon.
With the green LG TM.
**Roger Coll** 05:50 And go online.
**Alessio** 05:52 Something like that.
**Roger Coll** 05:53 Okay, so you changed also, kind of, the UI thing as well, that's what I'm saying.
**Alessio** 05:58 Cool. No, I didn't… like, I… I struggle to… to… to actually…
I try to actually keep the same UI that we have, and….
**Roger Coll** 06:08 Okay.
**Alessio** 06:08 And just, like, shift the thing from JavaScript-based one to an Elixiri-based one.
I actually have to also auto-instrument that with OpenTelemetry, because that's the whole point.
Yeah. Yeah.
**Roger Coll** 06:25 Cool, yeah, I guess that once it's ready, not in a rush, let us know.
**Alessio** 06:30 Yeah, yeah, yeah.
**Roger Coll** 06:31 already, and I guess we can, I don't know, maybe divide the PR between myself, Giuliano.
Shinori also wants to take a look, and yeah, it will be very fast, I guess.
**Alessio** 06:45 Yeah, once we come back from the… from the vacation.
**Roger Coll** 06:49 Exactly. Are you going somewhere, or you already dead? Not yet, probably by the end of August, but….
**Alessio** 06:57 Yeah.
**Roger Coll** 06:57 Still planning, but yeah, all go… mid-August and mid-July, it's….
Those times up.
No one is here, so it's… it's good because it's calm, but…
Cool. So, well, thanks for working in that. It's really appreciated.
It will be great having Elixir in the demo, so… thanks.
Okay, … On my side, I don't have much things either, haven't worked that much on AutoDemo.
Just so that we've got, …
I know you also started, a Rast PR, right, about the… Smaller open search.
A lightweight.
I think you're on mute.
**Shenoy Pratik (AWS OpenSearch)** 07:49 Sorry. Yeah, I had one question on that. I have some settings that I want to update after OpenSearch spins up. So, now I have just created a Bash script as another Docker container, which can make API calls.
But I'm thinking what's, … Better plan when we also move this plan charts.
**Roger Coll** 08:11 Okay, so you want to modify some open search configuration once… It's running.
**Shenoy Pratik (AWS OpenSearch)** 08:20 Yeah, yeah.
**Roger Coll** 08:22 Hmm… Not sure, honestly, what's the best approach with the stocker.
….
**Shenoy Pratik (AWS OpenSearch)** 08:30 with… with Docker, I think this, … init.
Container makes sense.
But I'm more worried about selling charts later on.
How do we do that?
**Roger Coll** 08:44 as well.
Yeah, good point.
Hmm.
**Shenoy Pratik (AWS OpenSearch)** 08:49 We can do something similar, but at the end, maintenance is difficult with these kind of stuff.
**Roger Coll** 08:55 Okay.
And it's impossible to do that in the Docker file, right? It's not…
It only can be done after lunch.
**Shenoy Pratik (AWS OpenSearch)** 09:11 still, thinking around it and seeing if there are any gains or not in the first place with these settings. So it's not that we need them for sure.
But, … Once I have something concrete, maybe we can discuss further.
**Roger Coll** 09:26 Okay, what does it do? This, let's say, setting that you apply?
**Shenoy Pratik (AWS OpenSearch)** 09:32 Yeah, these are index replicas being turned off and everything, so that your indexing time goes low, and the memory usage during indexing doesn't take a lot of time.
**Roger Coll** 09:42 Okay. Yeah. But I guess that you can still benefit from a lower memory footprint with just a minimal image, right? Without….
**Shenoy Pratik (AWS OpenSearch)** 09:53 Yeah, yeah.
**Roger Coll** 09:54 I think….
**Shenoy Pratik (AWS OpenSearch)** 09:54 Just the basic plugins that I needed. It should be still good.
**Roger Coll** 09:58 So, I don't know, if you prefer, we can start just simple with the new image and see how it goes, and even go, yeah.
reduce the resources if… if we get still some complaints, or we want to… we see a huge difference between using the configuration or not.
But at least I think that minimal image, it's a nice…
Nice change, so I would just, … approve that.
**Shenoy Pratik (AWS OpenSearch)** 10:29 Amazing.
**Roger Coll** 10:32 But yeah, I don't know, with Hampshire, maybe with some bad jobs to run after installation or something like that, but also not very… not sure.
**Shenoy Pratik (AWS OpenSearch)** 10:49 Okay, I'll take another stab, maybe…
early next week, and then we can finalize on the first draft, maybe, just removing the unused plugins. That should be fine.
**Roger Coll** 11:00 Sounds good, yeah, I'll just start simple, and then just… just match the minimum language.
Thank you. Okay.
**Shenoy Pratik (AWS OpenSearch)** 11:07 I had one more, PR for updating the documentation.
With the open search to store logs in the architecture diagram.
-Oh.
We might need some… Approve us from our side to approve this.
**Roger Coll** 11:27 Sure, I will take a look.
**Shenoy Pratik (AWS OpenSearch)** 11:29 Thank you. Yep.
**Roger Coll** 11:44 Anything else?
Pierre, something you want to drink?
No.
Maybe, well, just to mention that we were planning a release, but I guess we can wait until Juliano is back. He had all the context for that one.
That's it.
You can call it a meeting.
Thank you.
**Alessio** 12:25 Oh, that was quick. Thanks.
**Roger Coll** 12:26 Yeah.
**Alessio** 12:27 Thank you.
**Roger Coll** 12:28 Take care, bye-bye.
**Alessio** 12:29 Thanks, everybody.
