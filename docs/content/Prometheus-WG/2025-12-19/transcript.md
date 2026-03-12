SIG: Prometheus WG
Date: 2025-12-19
Duration: 14 minutes
Zoom Recording URL: https://zoom.us/rec/share/_6arEfspNYOH5WyI6ZQLWNCvdKcmdwhnJvTCfck63rVBKjGNgqEod2uG0xfvS1d_.ASp5L_aPpZ_SQAh1
============================================================

## Zoom Recording Transcript

**Arthur Silva Sens** 00:55 Hello.
**Owen Williams (he/she)** 00:56 Hmm.
**Arthur Silva Sens** 01:04 How are you?
**Owen Williams (he/she)** 01:07 Pretty good.
**Arthur Silva Sens** 01:36 Hello, hello.
**Owen Williams (he/she)** 01:49 Oh, excuse me.
**Arthur Silva Sens** 02:08 Adam, do you know if David is coming?
I cannot hear you.
**Adam Bernot** 02:52 Tests?
**Arthur Silva Sens** 02:53 Oh, now I can hear you.
**Adam Bernot** 02:55 Alright, that was weird. He was showing the wrong, microphone. Yeah, David's out of office now.
Def?
**Arthur Silva Sens** 03:02 Okay, let's see.
I guess we can start then.
I… I was planning to… Review progress that we made towards a stabilization of Prometus Receiver.
But does anybody else has other topics? Because, like, we talk this about… we talk about this every week.
**Kyle Eckhart** 03:30 I mean, there was just a small thing on PR I did to try to fix the write-ahead log. I haven't gotten back to it, when I run the unit tests, like, one every, like, thousand times, they fail, so they're, like, slightly flaky, and I have not gotten back to look at, like.
Why? Why does it fail once every thousand runs? It… yeah, anyway.
**Arthur Silva Sens** 03:58 It failed consistently in the CI, though.
**Kyle Eckhart** 04:03 So those test failures were not… were complete… like, the CI ones, when I looked at them, they looked very unrelated.
Like, the K8 ones?
I guess I… maybe I didn't look super closely.
**Arthur Silva Sens** 04:18 Oh, I… okay, I think they… if somebody rerun, and yeah, they heard that I'm seeing today, it's very irregular.
Strange.
**Kyle Eckhart** 04:28 Yeah, that one just says water more metrics jobs failed.
Alright, here it is. No.
I can double check, but I swear the CI stuff was, like, it looked unrelated, at least the last I checked, but I can double check again. If it consistently fails and I have CI, then I have my answer.
But… I haven't been able to suss out why randomly it fails.
**Arthur Silva Sens** 04:54 Let me try… let me try every bunny.
**Kyle Eckhart** 04:57 Okay.
I could probably just ask Claude to tell me, see what it says.
**Arthur Silva Sens** 05:14 But when it's locally, what is the… Devor?
**Kyle Eckhart** 05:20 The second, so expected to receive two payloads, and the second payload never comes.
**Arthur Silva Sens** 05:34 Alright, let's see, if it fails again.
And I'm gonna try to help him.
**Kyle Eckhart** 05:40 I mean, like, at the moment, the wall's kind of just completely broken, though. So if we need to, I could probably… the test that is there… Doesn't really test anything.
Which was kind of how this was, this was, missed. Like, it doesn't wait for the data to come in.
But I can certainly, like, revert the test, and then come back to the test part, because like I said, without it, we're just continuously replaying all of the same data, which seems, like, not ideal behavior.
**Arthur Silva Sens** 06:17 Yep.
Okay.
Okay, Hmm.
Hey, we can review progress for the Prometes receiver.
But, from the people that I see here, I… Historically… historically, at least, you have not been… helping. This is not a, like, a blame situation, it's like, if you're not interested in this, we could just end the call.
Like, whichever you prefer. We can reveal, or we can end the call. And both works for me.
**Owen Williams (he/she)** 06:59 So is this progress on… is this moving it to core, or is this just work that's happening on it?
**Arthur Silva Sens** 07:06 Best work that is happening on the receiver, so we declare it stable, and once it's stable, we move it to core.
**Owen Williams (he/she)** 07:14 I mean, I'm at least interested in sort of an update of where things are at, just so that I'm… yeah, the status update seems fine to me. But yes, I'm not working on it. Yeah, it is of interest to me that it gets done.
**Arthur Silva Sens** 07:28 Got it.
So, oh my god, what is not going with that?
We have a few items in the workable state.
And it's mostly… Some really, really easy stuff, like… We just need to remove some fields from our struct, which is… Super easy.
I added the good first issue, but nobody took it.
Other…
**Kyle Eckhart** 08:03 Are there, like, could we post that one in, like, the mentoring channel? I'm trying to remember, I think there's a bunch of channels, that we could… we might be able to get somebody.
**Arthur Silva Sens** 08:12 Yeah.
That could be a good idea.
Other one that I also just… I… I pasted the code, somebody just needs to copy-paste it to the… and open the PR.
And yeah.
Also, I had some… somebody from my team at Grafana offering to do this, but… She went on holidays and didn't do it.
But, like, super easy.
Then we have the harder ones, like eliminating time dependency on tests.
I tried… I opened up PR using clock injection in Upstream, in Prometus Prometheus.
But I got rejected because somebody implemented sync test.
Have you… have you all heard about the SyncTest package that was introduced in Go 1.25, I think?
Now, I didn't have time to, to, to, to study, so I parked… I parked the work.
But yeah, what needs to be done here is, like, all the… not all, but most of the tests that we have in the provisions receiver performs real scrapes And for the scrapes, it needs, scrape intervals.
And then there are timing issues all the time, depending on how busy the VM that is running the test is.
The tests are flaky, scraping their walls are also, like, they take 15 seconds each test.
So yeah, I… the work here is a little bit more complex, but it's… it's gonna help a lot by making tasks more reliable and quicker.
There's another very hard issue that Cryo offered to help, but didn't have the time, and I think he's went on PTO as well.
That, the… Binary for the collector is huge.
And most of… most of the co… the reason why it's huge is because We have a lot of dependencies on Provitus service discovery.
And the service… the service discoveries are huge.
We are trying to find a way that… we keep service discovery in Prometheus, but when we build the collector We are able to remove most of the surface discoveries, so it decreases binary size.
Cryo suggested that we use build tags, build tags, upstream, which… enables service discovery by default, but we… We use those tags when building the collector to make it Without the service discoveries.
This is not in progress.
Super cool.
Yeah.
Cryo didn't have the time to do it.
we have… One issue about being able to… to observe the time.
We need to process, like, to… scrape a target, transform into OTLP, and then send this OTLP data to the next component in the collector?
this is being done upstream. We are introducing a metric in Prometheus Prometheus that measures the time we take to scrape, append, and commit a metric.
Let me try to find… This is being done by… I think as a student.
This was one of the… yeah, first PR he opened. It's taken a while to get… get it… get to the right place, but, like, it's… it's getting there.
What else?
Then after we finish this, there are some extra work to be done, like, we need to improve documentation, we need to… Ensure we have task coverage for the whole config block… block?
We need to work on the spec, declare the… the part of the spec that translates Prometheus to OTLP is stable.
And this is, a part of this pack that we didn't implement yet.
And that's it, then we're good to go.
Any questions?
**Owen Williams (he/she)** 13:12 Yeah, it sounds like more help is needed.
**Arthur Silva Sens** 13:15 Yes.
**Owen Williams (he/she)** 13:16 I… I might be able to… I mean, not this year, but I might be able to take some of the low-hanging fruit stuff.
And, yeah, I'll read up on SIG test, that's interesting. Definitely… Time-dependent tests is a bugbear of mine, so, yeah, that's…
**Arthur Silva Sens** 13:36 Yeah.
**Owen Williams (he/she)** 13:36 I have to, you know, I have to balance out other stuff I'm doing, but, like, I think I do have cycles to work on this.
**Arthur Silva Sens** 13:44 Sounds good.
But your priority is Delta, or is it something else?
**Owen Williams (he/she)** 13:49 It's Delta's.
**Arthur Silva Sens** 13:50 Okay, cool.
Alright, that's the update I had.
**Owen Williams (he/she)** 13:58 Yeah, that's super helpful.
**Arthur Silva Sens** 14:04 Then, 15 minutes back, to us.
**Owen Williams (he/she)** 14:09 Sounds good.
**Arthur Silva Sens** 14:11 Right?
**Owen Williams (he/she)** 14:12 Alright.
**Arthur Silva Sens** 14:13 Happy holidays!
**Owen Williams (he/she)** 14:14 Yeah.
**Arthur Silva Sens** 14:15 Right.
**Owen Williams (he/she)** 14:15 See you next year, probably. Yep, bye-bye.
