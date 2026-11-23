SIG: FAAS WG
Date: 2026-11-19
Duration: 14 minutes
============================================================

## Zoom Recording Transcript

**Tyler Benson** 00:21 Good point. I didn't… I wasn't aware of that, that this worked.
**James Thompson** 00:26 Yeah.
I think it's the old link, though.
**Tyler Benson** 00:30 Yeah.
Most likely.
I don't know, I imagine there's some benefits with this new, Linux Foundation system, but it's also a little annoying.
**James Thompson** 00:49 Yeah, it doesn't surprise me.
**Tyler Benson** 00:53 So… Sounds like Serkin, sorry, Warre wasn't able to attend today, but… Yep.
Everything going well with you?
**James Thompson** 01:10 Cheer.
**Tyler Benson** 01:11 We can probably keep this pretty brief.
**James Thompson** 01:14 Yeah, like, from my side, the two main ones are, I put in the… Google Doc.
So, the resource detection processor, And then the Node… Node.js… Node SDK switch.
**Tyler Benson** 01:41 Okay.
**James Thompson** 01:42 Yeah.
one thing One thing that does come up is, are you involved in the benchmarking?
Sieg…
**Tyler Benson** 01:54 I have been involved in very little as of late.
**James Thompson** 01:58 Yep.
Alright, cheers.
One thing that came up with both those PRs.
Is… how do we monitor performance changes across versions?
**Tyler Benson** 02:18 Yeah, I think that… Warre was doing something with, benchmarking?
Yeah. I could be wrong.
**James Thompson** 02:27 So, what he had done was I added the integration tests.
Right, so that there's now the full end-to-end tests.
**Tyler Benson** 02:40 Yeah.
**James Thompson** 02:40 Currently, there's nowhere that information's stored.
**Tyler Benson** 02:47 Okay.
**James Thompson** 02:48 Yep.
Right? And, like, I found… what I found helpful for those two PRs, Was literally just to log What the platform report Generated, so then we can compare that, because that gives us memory usage, and then Right, and execution time, it gives us all those three key metrics.
Right? Directly from the lander.
**Tyler Benson** 03:18 Yeah.
**James Thompson** 03:19 Alright.
Right, so, and that's what I was using to compare performance.
**Tyler Benson** 03:26 What I wonder, and I'm afraid of, is how, consistent those, those times are between runs.
Yeah. One of the… The pivotal things for benchmarking is that ideally, you're running it on the same hardware, and that hardware isn't too busy, right?
And, obviously, we can't do that with Lambda.
**James Thompson** 03:55 Yeah.
**Tyler Benson** 03:58 So I wonder how… valid, those even are.
For purposes of benchmarking.
**James Thompson** 04:08 Yeah, like, I don't 100% trust them, especially, like you said, we don't control the environment.
But I think it gives some indication.
Right? That's a rough god.
**Tyler Benson** 04:22 Yeah.
**James Thompson** 04:24 Like, if we're running the function, and we're now seeing With this update, it's now taking 5 times as long Right? Across 5 runs. Then, hey, is this actually right?
**Tyler Benson** 04:38 So…
**James Thompson** 04:39 whereas… Yeah, I wouldn't trust them to be 100% accurate.
But… I see it as better than nothing.
**Tyler Benson** 04:49 Okay.
**James Thompson** 04:50 Yeah.
Right? And, like, what I found was the Venture tool, so we could actually send those Lambda reports directly into Venture, which would give us the statistic and analysis of how it traps.
**Tyler Benson** 05:08 Okay.
**James Thompson** 05:10 M.
**Tyler Benson** 05:11 So, what you need there is to figure out where to store the data.
**James Thompson** 05:16 Yes. I think that's the key thing, is… do we… go down the path of using Venture, just to… export the data to and store it there?
Right? Or what's the benchmarking SIG plan?
Because I know they have some reports, but the venture tool looks a lot more powerful than the reports they have.
would they look at switching to something like Bencher, for example, to store their benchmarks in? That way.
We're using the same tools as them.
We're not necessarily using it for… Professional-grade benchmarking, just as a guide benchmarking.
**Tyler Benson** 06:02 Alright. So, I'm not opposed to, exploring that. I've never heard of, Venture, and I'm not sure what that would entail, but on the, So, way back when, on the Java SIG, when I worked on benchmarking, what I set up there is to have the, The results published?
to a… a separate branch inside of the GitHub repository, and then it would get public, like, it would be visible as, like, a GitHub, Pages…
**James Thompson** 06:42 Yep.
**Tyler Benson** 06:43 document.
**James Thompson** 06:44 Yeah.
**Tyler Benson** 06:46 So, I don't know if, That would be worth exploring, but the problem there is that you also need something to periodically go back and clean things up.
**James Thompson** 06:58 Yeah.
Yeah, and then you also have to… generate the analysis of the run. This run is 5 times as long to run.
**Tyler Benson** 07:10 Well, this would only just, like, show the charts.
**James Thompson** 07:13 Yeah.
Whereas something like Venture gives us the charts, gives us the automatic cleanup, we literally… export a JSON file of info… as a report, everything else is handled for us.
Alright, so from an ease of convenience.
perspective, it looked quite easy to implement.
**Tyler Benson** 07:42 Okay. I mean, it sounds like a good idea. If you're wanting to explore that, I'm not opposed.
Alright, Phil, for you.
**James Thompson** 07:53 Yep.
**Tyler Benson** 07:53 But, anyway… I will go through some of these other issues, the pull requests that you've posted, and try to chime in there.
**James Thompson** 08:05 Yeah. Yeah, like, I think the big one is the resource detection one.
Right?
So, they're previously… There's two options, either… fork the… because what… the receiver's now doing… the process is now doing, is using the contrib libraries from the Go language.
For resource detection, and by default, it brings in every single library it needs.
**Tyler Benson** 08:35 Yeah, so it's a little excessive.
**James Thompson** 08:37 Yeah, right, and so there was complaints about that, right? And what they now have is bill tags.
Right, so you can specify which… which detectors do you want… want to include?
And so, for us, it made no difference to the… release size.
Once we use the build tags.
Yes.
Right? And that means all resource detection is handled via the Go SDK.
**Tyler Benson** 09:02 Awesome. Okay, yeah, I'll review that and, likely get merged.
**James Thompson** 09:08 Node.js to switch to the version 3 library, and trying to directly use the Node SDK.
Library, rather than trying to implement our own.
**Tyler Benson** 09:19 Had we done our own in the past?
**James Thompson** 09:22 Yeah, right, so it was directly building all the components and all that.
**Tyler Benson** 09:29 Oh, okay.
**James Thompson** 09:30 You know, so the change took out, like, 200 lines from our… the JavaScript wrapper.
**Tyler Benson** 09:37 Nice.
Yeah.
**James Thompson** 09:39 And then that further changes could occur once we… Have a deprecated release of a couple of the hooks, then we can remove even more code.
**Tyler Benson** 09:48 Okay.
Cool. Do… do you think that, we need to have… I guess maybe, mainly just a document, explaining the breaking change, perhaps, by moving to version 3?
**James Thompson** 10:08 Yeah. Alright, do we document it in the release notes? Right? I suppose, like, we should also update the README to document the additional hook.
Right?
**Tyler Benson** 10:20 Yeah.
**James Thompson** 10:21 Yeah, right, so yeah, I can have that rate, rate me.
**Tyler Benson** 10:27 I guess the only other question there is, do you think there's any, good reason to… Do another, Node.js release before we do this?
Or, should we just declare the last version as the one that…
**James Thompson** 10:50 So this release has no breaking changes?
Right? The… the hooks are marked as deprecated in the PR currently?
Okay? So we can… we could merge the PR that's open, right, without any breaking changes.
Okay, and then… I thought the…
**Tyler Benson** 11:12 But, moving to the SDK3 might have been the breaking change.
**James Thompson** 11:19 Right, yeah.
It's… but it's also tied into the Node.js switch as well.
Alright, so it needs a Node.js 22 switch.
Which… you opened the PR from, and I've already approved.
**Tyler Benson** 11:36 Okay.
**James Thompson** 11:37 Yeah, so it needs that, so we're already having a major version bump there.
Right, so we've technically got the breaking change for the Node.js rundown.
Right? But that's what the break and change is limited to currently in the PRs that are open.
**Tyler Benson** 11:54 Okay. So… Sounds like the best approach, then, is just to merge everything and do a release then, and anyone that still has issues can stick with the previous release?
**James Thompson** 12:08 Yep, and then… and then we… then once this release… once the next release is out, then we can go back and remove the deprecated methods.
**Tyler Benson** 12:18 Okay.
**James Thompson** 12:19 Yep.
**Tyler Benson** 12:20 Sounds good to me.
**James Thompson** 12:22 Nope.
**Tyler Benson** 12:24 Great. Do you want, any particular order I should merge these PRs in?
**James Thompson** 12:34 It's totally separate. One's changing the collector layer, and one's changing the Node.js layer to the totally separate.
**Tyler Benson** 12:40 Well, I'm talking about, like, for example, my release, my version that, adds Node 26 and removes… Node 20.
**James Thompson** 12:51 Yep, so merge that one first.
**Tyler Benson** 12:53 Merge that. Okay, I'll just click and merge that one now.
**James Thompson** 12:57 Yep.
**Tyler Benson** 12:58 Unless there's any objection.
**James Thompson** 13:01 No, I don't have any issues.
**Tyler Benson** 13:03 Okay.
**James Thompson** 13:04 Excellent.
**Tyler Benson** 13:04 When they're…
**James Thompson** 13:05 Because I still need to… I still need to go through and update the README, as we discussed.
**Tyler Benson** 13:12 Okay, so then hold off on, 2749. You wanted to update the README?
**James Thompson** 13:20 Yeah, that's an IJ switch, yeah, review that, right? And then if you're happy.
comment, and then I'll just update the… update the README.
**Tyler Benson** 13:30 Okay.
**James Thompson** 13:32 We could update the README after… after it's merged anyway, right? And just before release.
**Tyler Benson** 13:38 Cool.
So… Which one are you updating?
**James Thompson** 13:44 I can either update the Node.js switch here.
Right? Or I can open a separate PR to update the README.
**Tyler Benson** 13:53 Okay. You can just update that PR directly. Great.
So, I will focus then on the, the resource detector one first, and then I'll review the other one.
**James Thompson** 14:05 Yep.
**Tyler Benson** 14:06 Anything else?
**James Thompson** 14:07 No, that's it.
**Tyler Benson** 14:09 Great.
All thanks for your work, good job. Thanks.
I… I guess we'll see you in a couple weeks.
**James Thompson** 14:20 Yep, okay, see ya.
**Tyler Benson** 14:22 Oh, actually, I might be traveling on, during the next one, so, I might need… Everyone else to, cover the meeting.
**James Thompson** 14:35 Yep, that's fine.
**Tyler Benson** 14:37 But, anyway, cheers!
**James Thompson** 14:39 Fair.
**Tyler Benson** 14:40 Bye.
