SIG: OpenTelemetry PHP SIG
Date: 2026-09-30
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Pawel Filipczak (Elasticsearch B.V.)** 01:04 Hey, Grace.
**Chris Lightfoot-Wild** 01:09 Hey, pal. How you doing?
**Pawel Filipczak (Elasticsearch B.V.)** 01:12 Okay, how are you?
**Chris Lightfoot-Wild** 01:14 Yeah, I'm okay, thanks, yeah.
Seeing them… Bob said he couldn't make today, so…
**Pawel Filipczak (Elasticsearch B.V.)** 01:19 the.
**Chris Lightfoot-Wild** 01:20 It's just gonna be the two of us, or… Maybe Brett was, the pop around, did look like he'd have a lot of activity recently.
**Pawel Filipczak (Elasticsearch B.V.)** 01:29 you know.
So he's…
**Chris Lightfoot-Wild** 01:32 Okay.
**Pawel Filipczak (Elasticsearch B.V.)** 01:33 We come back to the SDK V2, right? I saw one on Slack.
**Chris Lightfoot-Wild** 01:37 Yeah. Yeah, he's got… he said he was gonna write a proposal, so I guess we'll… Watch this space.
And.
How's it going over there in Destroy Land?
**Pawel Filipczak (Elasticsearch B.V.)** 01:50 Not much progress.
Hi, I… what I… what I did?
Mmm.
Nothing spectacular, just focus on some other things, and… yeah.
**Chris Lightfoot-Wild** 02:08 Is it just yourself on the PHP side, I guess, at the moment, then? Obviously, without Sergey, you know?
**Pawel Filipczak (Elasticsearch B.V.)** 02:14 Yeah, so now I'm alone, but I have also different topics, so sometimes I have to, you know, sometimes my PHP work and focus on something else, then switch back. So A lot of context switchings.
**Chris Lightfoot-Wild** 02:28 I've got,
**Pawel Filipczak (Elasticsearch B.V.)** 02:29 you know, But I'm thinking about, about implementing this probability head-based sampling, so Sergey started.
two months ago, and I will continue that in upcoming weeks, so, yeah. But I have to do a research how to do that.
First, and then I will… I guess next week I will start implementation.
Oh, yeah.
**Chris Lightfoot-Wild** 03:02 Sounds good.
Should I share my screen? And I'm saying that… I need to just open the right browser tab, sorry, because my laptop restarted and I've lost them all. Bear with me.
And… Core, because you're relying on machines.
Started to turn the browser back on, it started resuming a YouTube video.
I bet what these things are.
Is there already anything on… I've not opened the agenda yet, is there anything on there that's particular today, or we're just going to go through?
**Pawel Filipczak (Elasticsearch B.V.)** 04:01 No, I don't have anything to share.
**Chris Lightfoot-Wild** 04:07 Cool.
**Pawel Filipczak (Elasticsearch B.V.)** 04:17 If you don't have anything, we can just skip.
Today.
**Chris Lightfoot-Wild** 04:21 Yeah, I suppose, I guess the other bit I was gonna do… I was gonna mention was I'd seen some span suppression stuff.
in a different, PR.
And that was something that people have raised an issue with as well, with, like, Laravel.
Before, so I'd started looking at that.
I've seen something that Jerry had done in one of his instrumentation packages, with a suggestion from Nivea of… During the, sort of, instrumentation setup, just grabbing the initial context, where everything's, like, no op.
And then activating and deactivating that when you don't you know, when you wanna discard all the spans that have been generated.
So I'm kind of just looking into that.
But yeah, I'd take the, the new Laravel package version as a beta as well.
But I don't know… I couldn't see anything on packages. Are you aware of any means of actually checking?
Is it even being used?
Do we get… If not, I've got no indication of… People are using it at all.
Which is quite difficult, I suppose, isn't it?
No, no one's come in with a bug report, but Equal have not advertised that it's out.
**Pawel Filipczak (Elasticsearch B.V.)** 05:43 I'm not sure if you… It was released, I mean, you mean 110 beta, that one?
**Chris Lightfoot-Wild** 05:50 Yeah, like, I tagged the release, but, like, I don't know if anyone's… But he looked at it, or whatever, I would even check.
**Pawel Filipczak (Elasticsearch B.V.)** 05:58 If we can change… split the install by the version.
But yes, you can split the install count by the version, so it's…
**Chris Lightfoot-Wild** 06:07 Oh, is that doable?
**Pawel Filipczak (Elasticsearch B.V.)** 06:08 That's one a day.
**Chris Lightfoot-Wild** 06:10 Oh, right.
**Pawel Filipczak (Elasticsearch B.V.)** 06:11 far, so…
**Chris Lightfoot-Wild** 06:12 laughs Quite low impact.
**Pawel Filipczak (Elasticsearch B.V.)** 06:16 So…
**Chris Lightfoot-Wild** 06:18 Okay.
**Pawel Filipczak (Elasticsearch B.V.)** 06:20 But I'm… I don't know why it only shows, you know, the… from the past week.
So 1.9, I will show you the link on the chat.
I.
**Chris Lightfoot-Wild** 06:32 Did we get to that? Was that under…
**Pawel Filipczak (Elasticsearch B.V.)** 06:36 I put it on the on the meetings chat. So you have to click the installs on the top.
And then you can go into and speed by the version.
**Chris Lightfoot-Wild** 06:45 Right, okay.
**Pawel Filipczak (Elasticsearch B.V.)** 06:46 Yeah.
**Chris Lightfoot-Wild** 06:48 Oh, and that's on 191. Does it list the 110?
Yeah, it does, yeah, yeah, sorry, yeah. Okay, cool.
**Pawel Filipczak (Elasticsearch B.V.)** 06:55 That's 2.5K per day, so not bad. I mean, this 1.9.
dot one.
**Chris Lightfoot-Wild** 07:07 Yeah. Okay, well, maybe I'll take a further poke at that, but I… I guess it would be a similar sort of story with the distro, like, what's your strategy there for… Tagging the betas are the release candidates you have.
How do you get people using them?
**Pawel Filipczak (Elasticsearch B.V.)** 07:23 So… I… I noticed that when I… when I merged the documentation.
Then people started using that. Before that, it was just a few installs, so now it's it's way better. But to get metrics, I have to use the page from GitHub.
Let me… let me check… it's the… Is that one? So… it shows how many total installs each release has. So, the latest one has 200, but the previous one was 1,700 SOAP.
Not much, but… it's growing. But before the documentation, it was, you know, less than 100 per version, so it was just few… Few of users was using that.
**Chris Lightfoot-Wild** 08:20 Okay.
Well, maybe I can try and have a look and see if I can get any… Stats anywhere out of this as well.
But, yeah, thank you. I guess if we're happy to just sort of skip the majority of this one, then, did you have any PRs that you needed anyone to look at?
**Pawel Filipczak (Elasticsearch B.V.)** 08:36 No.
**Chris Lightfoot-Wild** 08:36 Oh, no.
**Pawel Filipczak (Elasticsearch B.V.)** 08:37 income.
**Chris Lightfoot-Wild** 08:39 Cool. Well, I guess we might as well, get back the rest of our day and…
**Pawel Filipczak (Elasticsearch B.V.)** 08:43 Yeah.
**Chris Lightfoot-Wild** 08:44 Yeah, I'll see you next week. Have a good one.
**Pawel Filipczak (Elasticsearch B.V.)** 08:46 See you next week. Have a nice weekend. Bye.
**Chris Lightfoot-Wild** 08:48 You too, bye-bye.
