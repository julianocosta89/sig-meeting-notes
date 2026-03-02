SIG: OpenTelemetry on Mainframes Weekly Meeting
Date: 2026-01-14
Duration: 9 minutes
Zoom Recording URL: https://zoom.us/rec/share/0oCLWQwLvqJ0GCSxguwghmCdlQ9rHhBxJ4qgL2K-_5yzEdTJkXkjuWc5CtGc8vaF.lLNyNtfbo1-stB0w
============================================================

## Zoom Recording Transcript

**Morgan McLean** 02:49 Hey everyone, looks like we have quite a few people out sick today, so I don't know if we're actually gonna meet.
**Kai Kirsch** 03:00 Hi, Morgan, Andre, yep. That's okay for me.
I think Greg also might not join, he's out of office today.
**Morgan McLean** 03:08 Yeah, Greg said he's away, Rudiger's traveling, and Angelica is sick.
Everyone okay if we skip?
**Andrej Chmelo** 03:21 Hi, I'm okay if we skip, but if you have time for one question, it would be… Sure.
**Morgan McLean** 03:28 Yeah. What's your question?
**Andrej Chmelo** 03:30 So, in general, I was asking, it was at the end of the last year, like, how other people test their own, like, enhancement or implementation of OpenTelemetry in their applications, and…
I was suggested to use the golden image, or golden files, to test them.
But they have some… or we found some limitations there, so I just wanted to ask, like… If…
This is really how everyone is being, or is testing this, or if you would have some other suggestions how we can
We can test them.
**Morgan McLean** 04:12 This is specifically for mainframe use, or is this just Please.
**Andrej Chmelo** 04:16 I think it's general, because, like, we are testing, our…
Our… like, we are developing Gateway, so we are testing it in the GitHub Actions.
So, we also want to run this golden collector there.
**Morgan McLean** 04:33 Yeah.
I…
I don't have a whole lot of hands-on experience of how end users are doing their testing. I know it's Splunk, I think that's roughly what we do.
But, yeah, like, so, so, like, your goal here is to take the collector image and then test that?
Using GitHub Actions, is that accurate?
**Andrej Chmelo** 04:55 Yeah, something like that. Like, we… we are adding some, attributes.
And we just want to see, like, if we add something
Then the metrics that's being produced, that we can, like, match them with something that we have.
**Morgan McLean** 05:18 Yeah, I mean, that seems straightforward. Like, what met…
Can you walk me through, like, your specific test cases?
**Andrej Chmelo** 05:30 Ugh… Sure, like, it's very… so far, it's very simple, so,
Let me take a look where it is.
I'm not sure if it will be better if I share my screen, or… Sure.
**Morgan McLean** 06:24 Yeah.
**Andrej Chmelo** 06:26 Okay…
So, basically, this is what we were able to achieve.
We just start the application.
Start the collector, start the golden collector, And…
We are just waiting for some metrics to be produced, and then…
we defined this… this expected YAML.
**Morgan McLean** 07:01 And…
**Andrej Chmelo** 07:03 We all just wanted to… to see that…
These attributes are there, and then potentially, get something out of the… Of these metrics.
It was just a BOC.
**Morgan McLean** 07:19 Yeah, this seems… I mean, this seems fine.
**Andrej Chmelo** 07:23 Well, but the only… the only issue is that…
The collector is running for some time, so the…
The result of this test really depends on how long it runs, because the amount of metrics can change.
And, basically.
**Morgan McLean** 07:43 Yeah, because the underlying… are you running it on, like, a GitHub Actions provided host? Yeah, okay. I mean, that's… that's more due to the latency, or…
Or, Sort of non-constiteness of GitHub actions, okay.
You might wanna… so, and that's the issue, is like, you just don't know how long to wait before declaring that the test has failed or passed?
**Andrej Chmelo** 08:05 Yeah, so basically, if this is the right approach, how to do it, that's maybe the first question, if…
**Morgan McLean** 08:12 reasonable. You may want to actually join the collector SIG and ask them. They may have some better ideas. Like, this is the mainframe SIG, and so we don't really deal with this a whole lot. I'm just going off my own knowledge.
So I'd recommend asking the collector SIG. That being said, this seems… this is what I would probably do.
**Andrej Chmelo** 08:28 Okay. Yep.
Okay, then, then fair enough.
**Morgan McLean** 08:31 So CollectorSig will have people who have done this for years, and they may have… they have much more specialized knowledge than I do, and they may have better ideas.
**Andrej Chmelo** 08:40 Sure, sure.
**Morgan McLean** 08:40 Yeah, but this seems pretty reasonable to me.
**Andrej Chmelo** 08:43 Yeah, like, and it all, like, looks pretty good, the only issue…
Like, maybe it's not an issue, it's just the documentation around this is very limited, and…
We are paying, like, a hard time to find, like, what are the customization options, how we can, you know, skip some metrics and so on. Yeah.
So, okay, about that, I'm… I will ask there. Thanks for your tip.
**Morgan McLean** 09:11 Of course. Alright.
Think we can wrap it up?
See you all then.
**Andrej Chmelo** 09:18 Okay, see you. Have a nice day.
**Kai Kirsch** 09:19 next week.
Bye-bye.
