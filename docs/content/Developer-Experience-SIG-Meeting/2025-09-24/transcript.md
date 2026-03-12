SIG: Developer Experience SIG Meeting
Date: 2025-09-24
Duration: 11 minutes
============================================================

## Zoom Recording Transcript

**Juliano Costa | Datadog** 01:56 Hello, hello!
**Damien Mathieu** 02:01 Hey, good morning.
**Juliano Costa | Datadog** 02:03 Morning.
Long time no see.
I'm with two laptops here.
**Tristan Sloughter** 02:16 Keyboard.
**Juliano Costa | Datadog** 02:17 God.
It's just a mess.
I'm testing the demo on my Linux machine.
This looks… yeah, it looks like it's… It has cons… memory consumption different, on Linux and Mac, for some reason. Well, the feature flag thing is the… is Elixir problem, Fristen.
I'm gonna get removed again.
Hopefully not, like, I was the Wishing for that, so, like, hopefully we get that stable.
**Tristan Sloughter** 02:59 Well, yeah, if you need me to look at anything, just ping me on Git… GitHub.
**Juliano Costa | Datadog** 03:04 Yes.
**Tristan Sloughter** 03:05 I don't want to keep it in there, but… Should be better at memory on Linux, because it doesn't have to run… a VM, but… That's sad.
Mmm… Yeah, so what do we have today? Because… Do we have anything to discuss besides the blog post?
**Juliano Costa | Datadog** 03:28 Not from my end.
**Damien Mathieu** 03:32 What's your feeling about yesterday's… Interview.
**Juliano Costa | Datadog** 03:39 I… I feel that it is pretty simple what they do.
But I… I think I mentioned to Tim that I like the way that It is simple, because they do have some traffic, and they do, have some traces flowing, so… It's nice to see that you do not need A lot of collectors deployed, just to kind of get started, or if you have a small company, like, one collector may be enough.
I like it. Again, it's pretty simple, but still, they are using operator to manage and that stuff, so… I was happy about it.
Okay, no, Damien's gone.
**Tristan Sloughter** 04:37 See if he pops back in.
Okay.
**Juliano Costa | Datadog** 04:40 There he is.
I have… So, I was saying that, in the end, I was happy with it.
Do you have any, any thoughts?
**Damien Mathieu** 04:57 Sorry.
**Juliano Costa | Datadog** 04:58 No worries.
So, why did you ask? Did you do something different?
**Damien Mathieu** 05:09 No, no, no, I think, I agree with you that it's nice, that it's simple, yet, at scale. I think it's… A good thing to show, that it can be at scale and remains simple as well.
Yeah, I think it's… it's a pretty good, thing to show. It should be a nice blog post.
**Juliano Costa | Datadog** 05:37 Cool. Yeah, I'll start working on that as soon as I get a new Helm release for the demo, that, yeah, it's just a mess at the moment. So, I'll try to get that out.
And I'll start working on the blog post. One thing that I want to check with you and Tristan is, should I… At an intro, telling readers what Mastodon is?
Or just point to their page and say, hey, wanna learn about Mastodome? Here it is.
**Damien Mathieu** 06:12 I would do both.
**Tristan Sloughter** 06:15 I think it's good to have, yeah, If you… because we're going to be describing How they use some technology, so good to have some understanding of what they're doing.
Perfect. Without just leaking somewhere else.
**Juliano Costa | Datadog** 06:30 Do you want to have…
**Tristan Sloughter** 06:32 The introduction to the series?
At, like, at the top tube.
Do that, and then go into it.
**Juliano Costa | Datadog** 06:43 Yep.
Should I add, like, 1 out of X, or just, like, part 1?
**Tristan Sloughter** 06:52 It's… yeah, probably just part one. So, I did get… so, a long time ago, the… user… user experience, SIG?
Who was looking in to people to interview for this, had reached out to, someone at Dunks… Commodities?
Is it German? And… They're a company of 500 to 1,000 employees, and have about 120 collectors running.
I… the idea was maybe they would be on the smaller side that we could interview. I'm not sure if we need to interview them anymore. They took a long time to get back, because the guy went on… went out of town, and then didn't reply, and then finally did. So I figured, yeah, we'd probably… Don't want to add another one on there, but figured I'd check with you guys to… Make sure.
Before I said anything to them.
**Juliano Costa | Datadog** 07:57 I… I wonder if we could maybe add them as medium size?
Because, at the moment, we have just… large companies, right?
**Tristan Sloughter** 08:13 That's true.
**Juliano Costa | Datadog** 08:13 Sebastian.
**Tristan Sloughter** 08:14 And…
**Juliano Costa | Datadog** 08:16 As high schooler, they are pretty big.
**Tristan Sloughter** 08:20 Yeah.
**Juliano Costa | Datadog** 08:20 I mean, the amount of collectors that they deploy?
**Tristan Sloughter** 08:23 Right.
**Juliano Costa | Datadog** 08:26 It's way more than 100.
**Tristan Sloughter** 08:29 Yeah, that's true. Skyscanery is way up there, isn't they?
I guess we do jump pretty… Pretty big, so that probably is a good fit in there in the middle. Okay.
Oh… reply, and… Let's see… Yeah, the number… let's see, one of the… closer to 200, so they have about 200… I'm assuming collector pod's probably running.
500 employees, yeah, that's a good… Good size, but then… I don't know what their engineering team actually is, but There's probably a lot of traders and stuff, but yeah, I'll reach back out, and maybe… hopefully we can get them in soon, and have that as a second blog post, and then… I don't know if we want to combine any, like, the larger ones, or… because we have… What is it? 3 other companies?
**Juliano Costa | Datadog** 09:33 I remember Skyscanner and Atlassian. Do we have another one?
**Tristan Sloughter** 09:38 Adobe.
**Juliano Costa | Datadog** 09:39 Adobe.
**Tristan Sloughter** 09:41 Those are all large, yeah.
**Damien Mathieu** 09:43 I mean, we also, mentioned Heroku, and Alex is… Or an interview.
**Tristan Sloughter** 09:50 Okay.
**Juliano Costa | Datadog** 09:51 So, we do have a bunch of super large companies.
**Tristan Sloughter** 09:56 Yeah.
Oh, we can look at… What they each bring, and decide, like, if they… Need their own posts, or if we can kind of combine them.
You can consider that, just detailing the most unique parts, but… Wouldn't be bad to do individual posts, especially if we get… Get sort of a feel for writing them with this first one, and just… We'll pump them out.
**Juliano Costa | Datadog** 10:30 Okay.
**Tristan Sloughter** 10:32 So, you know.
**Juliano Costa | Datadog** 10:33 Legion.
I'm the… I'm the blocker now, so, okay, pressure on me.
**Tristan Sloughter** 10:38 I'll get that out, Art.
**Juliano Costa | Datadog** 10:42 Drafted as soon as possible, and we can.
**Tristan Sloughter** 10:47 Review.
**Juliano Costa | Datadog** 10:48 We'll move on from there.
Cool.
**Tristan Sloughter** 11:00 Yeah. Did you guys have anything else you wanted?
To discuss…
**Juliano Costa | Datadog** 11:16 No, really, yeah. I think from my end, that's it.
**Tristan Sloughter** 11:20 Okay, then we can call it and get to work.
**Juliano Costa | Datadog** 11:23 Cool.
See you guys.
**Tristan Sloughter** 11:26 But…
**Juliano Costa | Datadog** 11:26 But…
