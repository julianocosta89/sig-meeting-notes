SIG: Rust SIG
Date: 2026-06-10
Duration: 8 minutes
============================================================

## Zoom Recording Transcript

**Björn Antonsson** 00:59 Hey there. How are things?
**Scott Gerring** 01:02 Hey! Not bad, yourself?
**Björn Antonsson** 01:06 Keeping myself busy, we have a language platform work… Group summit thingy.
In Paris this week, so…
**Scott Gerring** 01:17 Oh, you're in Paris. I'm going to Paris for the first time in, 2 weeks to hang out with the profiling team, which will be cool.
**Björn Antonsson** 01:25 Yep.
**Scott Gerring** 01:27 I'm quite excited.
**Björn Antonsson** 01:29 Yeah.
Didn't really align up, but… Yep.
**Scott Gerring** 01:34 I will go and haunt, hall, at least.
**Björn Antonsson** 01:39 Yeah, absolutely. But, I mean, don't bother before 12 o'clock, so…
**Scott Gerring** 01:44 Don't bother what, sorry?
**Björn Antonsson** 01:45 Before 12 o'clock.
**Scott Gerring** 01:47 Is he a late… a late riser?
**Björn Antonsson** 01:49 Yeah, and a late worker, so it evens out, but…
**Scott Gerring** 01:53 Fair enough.
**Björn Antonsson** 01:55 Oh, is it lunch? Yeah, Paul is here. Let's go.
**Scott Gerring** 02:00 since… since the kids, I've realized that if I get up very early, I have Scott time, so I get up very early these days.
**Björn Antonsson** 02:06 Yes.
**Scott Gerring** 02:08 Yeah.
**Björn Antonsson** 02:09 I saw the photo of, The little one in the backpack, or the carrying thing.
**Scott Gerring** 02:15 Yeah, I… she's a lot bigger now. This is probably 5 years ago or something.
**Björn Antonsson** 02:20 Oh.
**Scott Gerring** 02:20 But I… I needed a… I looked too serious for, our corporate Slack standards, so I thought I would find something a bit… a bit more wholesome.
**Björn Antonsson** 02:28 Yep.
**Scott Gerring** 02:29 Yeah.
I'm gonna be hassling you folks soon.
hopefully about trying to get into a branch of Diddy Trace RS, this heap profiling machinery, so we can We've done things internally, which should be good fun.
**Björn Antonsson** 02:45 Yeah, that would be awesome.
Absolutely.
**Scott Gerring** 02:48 I think it should be very interesting.
I'm about to pull the trigger on the JetBrains license, because it turns out for this, I'm going to need every different IDE that exists, like Goland… Goland for the profiler itself.
Rust Rover, which I already have, and then there's a bunch of sea lying around everywhere as well.
**Björn Antonsson** 03:08 Yeah.
**Scott Gerring** 03:09 But, yeah.
I think it's probably just gonna be us.
**Björn Antonsson** 03:16 I didn't look in the Slack.
**Scott Gerring** 03:19 I will… actually be a good citizen of OpenTelemetry and post in the channel quickly?
**Björn Antonsson** 03:29 Yeah.
**Scott Gerring** 03:37 A… try and make… where do I… where's the invite button?
I'm terrible at zoning.
Which is sad when you spend so much time in something and you don't even know how to use it.
**Björn Antonsson** 03:52 It's got AI now, can't you just ask it?
**Scott Gerring** 03:59 Did you see all the breathless hype this morning about the new Anthropic Too Dangerous-to-ever-be-released, but now we've just released it model?
**Björn Antonsson** 04:06 But it's… tethered, but released. It's…
**Scott Gerring** 04:12 I went to play with it this morning, but I see that we've blocked it from our internal systems at the moment, which is maybe the best.
**Björn Antonsson** 04:21 Have we? Really?
**Scott Gerring** 04:23 Yeah, there's some business with… they've said that because they're scared of how terrifyingly dangerous it is.
**Björn Antonsson** 04:29 Oh, you…
**Scott Gerring** 04:30 During everything.
**Björn Antonsson** 04:31 You mean if you're using the official app?
**Scott Gerring** 04:34 Yeah, yeah, yeah, yeah.
**Björn Antonsson** 04:35 No.
I have MCPs to internal documents, and it's on Bedrock.
Anthropic.
So… Yeah, that's probably the AI gateway. I haven't tried it. I mean, I don't know what to tell it, so…
**Scott Gerring** 04:50 Yeah, I've got a few things… that I think are, like, inherently hard problems that I like to ask them to do to see if they get any better at them, and generally they haven't so far, but I'm willing to be surprised.
We will see.
Have you been doing any OpenTelemetry Rust recently?
**Björn Antonsson** 05:09 No, it's been way too many other things going on, both at work and, personally, so… But… After this week, I will probably get some focus time.
**Scott Gerring** 05:27 Cool. Yeah, I've been trying to kind of make a habit out of doing a little bit every day.
To push things along.
Where I can… Yeah, the thing is a bit, there's just a bunch of large PRs that need to be resolved at some point, like the runtime one I would really like to get in, but it requires focus for anyone to work on, and then focus for anyone to review, because it's just fraught, right?
But, yeah.
So it's the whole APM team in Paris this week, is it, or…
**Björn Antonsson** 06:02 No, no, no, it's way smaller. I mean, we've… I mean, you… there are new mandates about travel and other things, so… but it's, Much better. This is just language platform, which is the core Team for the different languages, and common components, of course.
So… We're roughly… are we? Like, 50 people-ish?
**Scott Gerring** 06:31 Hi, yep.
Cool. Yeah, I'm quite excited to come visit. I've heard lovely things about the office, and it's kind of sad that it's 5 hours train ride from me, like, it's not far.
**Björn Antonsson** 06:40 Yeah.
**Scott Gerring** 06:41 Need a good excuse.
**Björn Antonsson** 06:42 Yeah, absolutely.
**Scott Gerring** 06:45 What is your hot tip for the office to… for the… for the hotel to stay in?
**Björn Antonsson** 06:50 So, I generally stay at Marriott hotels.
So… but, I mean, it all depends. I don't know what the policy is now, but… I usually have been staying at the… what is it called? Marriott Opera Ambassador? I think it's really nice.
**Scott Gerring** 07:14 Yeah, one of the… I think Attila said that that was the place to stay. I've been collecting recommendations. I haven't looked anything yet, though.
**Björn Antonsson** 07:21 But this time, I was… wasn't… I wasn't booking in…
**Scott Gerring** 07:27 Navon?
**Björn Antonsson** 07:28 Yeah, in time, or in… and now it seems that it's, tourist season as well, so some of the hotels are… So expensive wheat.
I'm in a Citizen M, which is… was an interesting, experience.
**Scott Gerring** 07:45 They tend to be okay, I think, in this weird…
**Björn Antonsson** 07:48 like, hyper…
**Scott Gerring** 07:48 Modern fact.
**Björn Antonsson** 07:49 Nice, clean, whatever, but it's very compact, so…
**Scott Gerring** 07:53 Yeah.
**Björn Antonsson** 07:53 The breakfast was brilliant, so… yeah.
**Scott Gerring** 07:56 Yeah, no.
**Björn Antonsson** 07:57 complaints.
**Scott Gerring** 07:58 Yeah, the breakfasts are what I always do my health in for a work trip, so…
**Björn Antonsson** 08:02 Yeah.
**Scott Gerring** 08:05 Oh, anyway, I guess it's just us. Shall we wrap this up?
**Björn Antonsson** 08:09 I think so.
Nice chatting, and…
**Scott Gerring** 08:13 Yeah, we should… we should have a proper chat, sometime soon, outside of the automatic recording of the OpenTelemetry universe.
**Björn Antonsson** 08:20 Yep.
Cheers.
**Scott Gerring** 08:22 I'll see you soon.
Bye.
