SIG: Sampling SIG
Date: 2025-10-09
Duration: 13 minutes
============================================================

## Zoom Recording Transcript

**jmacdonald** 02:13 Alright.
**Peter Findeisen** 02:16 Morning.
**jmacdonald** 02:18 Here we are. I don't know how much there is to talk about today, but, This thing I… I have that I haven't spoken about with y'all in a week or two… two weeks, is this blog post.
Let me find it… Anyone seen it yet?
**Otmar Ertl (Dynatrace)** 02:46 I looked through it, yes.
**jmacdonald** 02:47 Okay, well, good, then.
Hopefully this is better than the last one. Someone wrote.
Okay, we've gotten more feedback that makes it look like I didn't completely miss the mark this time.
So… The governance committee or the docs reviewers will take a look at this whenever I tell them to.
I'm getting, minor feedback, it looks like.
Minor feedback… thank you. I tried to leave that one out, but I'm getting suggestions about putting in a couple uses so I can see that. We have consistent sampling decisions across traces. We also have legacy hash functions. Okay.
And then, spelling, and then spelling, and then spelling.
And then more on this example.
This is fantastic, at least for me. It looks like I didn't miss completely this time, so… taking this feedback, I can absolutely, work on it. Spelling is easy, for the explicit readiness values, the leaving you hanging, I could mention Peter's original concept, I think, was to do consistent across traces.
I've used it to make the hash functions consistent, so… Aside from that, any other… if there's any other feedback, I'd love to hear it here.
Otherwise, requesting permission to put all of you who contributed in a major way to this, and that's… Carlos, I would leave you out, but But the rest of us, and Yuan Yuan, I feel like this was a real group effort. Does that sound okay to everybody? Because it's pretty normal to put that many names on a blog post, and there's a way to do it, so I will, with your permission, do so.
I see Peter nodding.
That's okay.
**Peter Findeisen** 04:51 Yes.
**jmacdonald** 04:51 bar, Ken.
Cool.
Well… I think I've learned what I needed to, then, on this topic. I don't intend to go through it, since I, since I've seen that you've read it. So, I think we can call that one Check.
Oh, I was looking at it and not sharing right now, as I read through the… Yeah. Sorry.
**Kent Quirk (he/him)** 05:15 I was about to ask.
**jmacdonald** 05:17 You're like, come on, Josh. Okay, here it is.
Am I writing? My computer's being really weird today, I'm not sure… what's going on? This is the blog post.
which I'm referring to.
Feedback is minor, Josh.
will address… We'll use co-author list from the SIG. Cool.
And, I think that… Finishes that little item.
Hey, Carlos, how's our PR that… that I had open? I haven't checked on it. I should know, because I just looked at my list.
**Carlos Alberto Cortez** 05:59 I don't think people have been reviewing that, like, at the actual spec.
We need to poke them.
**jmacdonald** 06:06 Okay. I'm now referring to… My move of the experimental spec, I mean, like, I think it's fine to use OTEPs for future archival purposes, I'll change the string on that to say archived.
Carlos, that's, I'm sorry, I have two browser windows, I need to stop doing that.
This is… It's because my Edge browser is being stupid. Okay, that's… this is the one that is, moves the old spec away. If you look at the docs site, they both have the same title, it's really confusing.
And then… Was there… That was it. We… the other PR merged, so now the, deprecation plan for Trace ID ratio is fully merged. Okay, cool.
I was half expecting to see some visitors in the meeting today, I'll tell you why.
The… there was, open spec issue, this week, I looked at… Let me… Let me just click in somewhere and find what I'm talking about.
This week, This topic came up… Enhancing OpenTelemetry for large-scale metric management.
Spawned quite a large thread, actually.
And it is largely aimed at, publishing configurations to tame large producers of metrics.
But it didn't get long into this thread before someone talked about sampling.
Sampling configurations.
And a desire here that's like, maybe OPM could speak any type of configuration for any type of sampling.
And, like, I'm not… I actually did skim through this, I'm not skimming through it right now, but Josh is… Josh is leaning in the direction I like. Specific config formats, partial config… What I… well, all I had to say was, there's a lot of interest in sampling configuration. I referred to your draft PR, Peter, somewhere down here. This is a really long thread.
We're getting close to the bottom, though. I know I said something.
I just wanted to… this is where I tagged us. I said, Sampling SIG has been looking at this.
I totally agree that… and, you know, we have tail sampling configuration, we have OTEP 240-type configuration for the composable samplers, we also have Jaeger remote, we also have… Rate-limiting research, so… That's all I said.
Josh says yes.
So, it's just another opening. This is going to keep coming back until we get traction, and I think it's nice to remind people that we've done some work here.
without anyone to talk to, that's about all I have.
**Kent Quirk (he/him)** 09:23 For what it's worth, Refinery, it's still kind of experimental, but Refinery has added, opium support, so that's another way to push tail sampling configuration with Opium.
**jmacdonald** 09:35 Okay, yeah, so maybe the experience that you all gained using OpAmp would be… helpful, and I guess, I haven't thought through the problems that come up, but… .
**Kent Quirk (he/him)** 09:52 Yeah, it's basically just, give us a way to shove a configuration down from op-amp. It didn't…
**jmacdonald** 09:56 I'm assuming that you need, like, a type string. Like, this is the type of configuration I am sending you.
**Kent Quirk (he/him)** 10:04 Yeah, to be honest… .
**jmacdonald** 10:07 we… I didn't… I didn't implement this, so… Okay, maybe it's… maybe it's a whole.
**Kent Quirk (he/him)** 10:11 I should…
**jmacdonald** 10:12 configuration with new updated tail sampling.
**Kent Quirk (he/him)** 10:15 Well, as collector is one thing. We have… we have one… we've created a… a node we call Beekeeper in the cluster that Knows how to fetch configurations from a server, and… pushing… push them using op-amp protocol to both refinery and, Collector.
So…
**jmacdonald** 10:38 I feel like I've not… not paid enough attention to the op-amp spec in my… time, but maybe I should start to pick it up.
**Kent Quirk (he/him)** 10:49 Yeah, I don't think op-amp was ever intended to be specific to Collector.
**jmacdonald** 10:54 No, it wasn't. That was… that's been stated many times. We think that it would be good for the SDK, and I wrote that much, too. Like, we want to do sampling configuration changes for the SDKs.
Well, that's about all. I just wanted to mention that.
I have no further topics for this meeting.
I always love it when that happens.
I mean, not really. I like it when we have something to talk about, but I also like it when I have The rest of the hour back.
Without any… unless anyone objects, I think we could end it. I will finish my blog post draft. I'll take it out of the draft.
Put our names on it.
Fix the spelling, add a couple examples, and try again.
**Kent Quirk (he/him)** 11:39 Sounds great.
**jmacdonald** 11:40 Cool. Thank you all. Short meetings are great. See you next time.
**Peter Findeisen** 11:44 Thank you.
**jmacdonald** 11:45 Right.
