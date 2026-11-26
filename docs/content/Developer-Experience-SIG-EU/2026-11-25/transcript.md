SIG: Developer Experience SIG (EU)
Date: 2026-11-25
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Juliano Costa** 02:35 Hello, hell.
**Perk (Marcin Stożek) | Elastic Ingest** 02:36 Hello. Hey, Julian, how are you?
**Juliano Costa** 02:39 I'm good, how are you?
**Perk (Marcin Stożek) | Elastic Ingest** 02:41 You feeling good? Yeah, I'm good, I'm good. I saw you were… unable to go to some KCD portal and others.
**Juliano Costa** 02:50 Yeah. I, got pretty sick coming back from, KubeCon.
And, yeah. You good now?
Sorry, come again?
**Perk (Marcin Stożek) | Elastic Ingest** 03:02 You… you… you good now?
Yeah, thank you. Okay.
**Juliano Costa** 03:06 Thankfully, yeah. But I stayed, like, last week, the whole week,
**Perk (Marcin Stożek) | Elastic Ingest** 03:11 Oh, I see. Okay, okay.
**Juliano Costa** 03:13 embed.
How's QCon?
Pretty bad. Kubecon was pretty good.
8.
It was interesting, a bit… a bit different from KubeCon EU. It was my first time in North America.
Okay.
It felt quieter, like, less people, sessions were unpacked, and even, like, like, the… the… sponsors area.
We're like… Okay.
You could walk, walk around easily.
Get swags easily.
**Perk (Marcin Stożek) | Elastic Ingest** 03:58 I heard… because I was… I was a couple of times there at KubeCon in NA, and that was always the case, but I've heard that this one was particularly early.
Quiet.
**Juliano Costa** 04:13 Well, it was my first time there, so I honestly do not have, comparison.
**Perk (Marcin Stożek) | Elastic Ingest** 04:24 Okay, yeah, that's fair, that's fair. The thing that I can tell you about, the Elastic internal, conferences, is that… is this the same… is this the same case?
And it's not a matter of, preparation, it's a matter of the audience, like… the audience that we get in Amsterdam, it's just… a lot more, more and more people, you know, like, interested and reaching out and whatnot, and then it states, it is still there, but it just… less of it, you know? That's how I feel it.
Interestingly. Yeah.
I don't know, maybe, maybe there's, a lot more competition there, you know, because you have KubeCon, then you have the reinvent, you know, like, you have a lot of… lot of things happening.
**Juliano Costa** 05:11 Yeah, it was, I think, 2 weeks from the event, so maybe people didn't want to travel to the U.S. that close.
**Perk (Marcin Stożek) | Elastic Ingest** 05:21 Yeah.
**Juliano Costa** 05:23 Yeah, makes sense. Yeah. Okay.
I, I, I, I've never been to reInvent, I,
**Perk (Marcin Stożek) | Elastic Ingest** 05:29 Yeah, me neither.
**Juliano Costa** 05:31 is my, it's my, like, it's my area, where I meet the folks that I work with, and, I, I, I enjoy,
**Perk (Marcin Stożek) | Elastic Ingest** 05:41 Yeah.
I enjoy it.
**Juliano Costa** 05:42 spending time, with…
**Perk (Marcin Stożek) | Elastic Ingest** 05:45 I think this is… Extremely, extremely different thing, you know? AWS reinventing KubeCon, really, you know?
Yeah, the one being, like, super sales, and the other one trying to be a community thing.
You know? Yeah.
**Juliano Costa** 06:02 Yup.
**Perk (Marcin Stożek) | Elastic Ingest** 06:02 Okay, okay. I was at the, last week I was at the ISMC conference, you know, in Nuremberg.
he was very nice, you know? I was surprised, because those people, they are, like, entering auto… auto space, in a way, you know? But they are doing… on the other hand, they are doing the monitoring for 20 years already.
You know, just Node Auto, and they have a lot of… a lot of knowledge, you know? It looks… some tools that I've never heard of, you know, and whatnot. It was a very nice discovery for me.
So, I recommend it, no? If you're thinking. It was not the biggest one, but… but still, like, 200, 300 people, so…
**Juliano Costa** 06:47 Okay.
**Perk (Marcin Stożek) | Elastic Ingest** 06:47 No, that was, like, actually, actually, like, pretty nice conference, you know, and it was packed, like, two trucks.
And then people were, like, engaged, you know, asking questions and whatnot, so… I'd say good stuff.
Okay.
**Juliano Costa** 07:00 So is it.
**Perk (Marcin Stożek) | Elastic Ingest** 07:01 OSMC, Open Source Monitoring Conference.
**Juliano Costa** 07:05 Okay.
OSMC, okay.
**Perk (Marcin Stożek) | Elastic Ingest** 07:08 SMC, yeah.
**Juliano Costa** 07:11 Oh.
**Perk (Marcin Stożek) | Elastic Ingest** 07:12 And then… and then next year… next year, there's the… there's also Unplugged in Brussels at the beginning of February, just right after Fosden.
And then there is another conference, Open Source Observability Day in Ghant.
Like, 2 days after. I think the unplugged is in… on Monday, and this one is on Wednesday. So, just saying in case… Might be in.
**Juliano Costa** 07:38 Yeah.
Yeah, I saw the second one. I don't know if I'll be able to…
**Perk (Marcin Stożek) | Elastic Ingest** 07:45 Stay…
**Juliano Costa** 07:46 like, all of that… even for some, I'm not 100% sure in going. Last year, I was there, and well, this year I was there, and it was a mess. I couldn't join any session. I could only join the Rust dev room, but, like, yeah.
Mmm, how close them.
Yeah, not much observability. There was no observability room this year.
**Perk (Marcin Stożek) | Elastic Ingest** 08:12 Yeah.
**Juliano Costa** 08:12 And I went there because of the Auto Unplugged, so,
**Perk (Marcin Stożek) | Elastic Ingest** 08:18 I was…
**Juliano Costa** 08:18 But yeah, like, I didn't.
No.
**Perk (Marcin Stożek) | Elastic Ingest** 08:23 Yeah, same here, same here. I think I'll… I think I'll go in order to, like, fish for those other projects that we, you know, discussed lately.
**Juliano Costa** 08:32 Yeah, so, on that, we… I… I bumped into some envoy, maintainers that keep.
**Perk (Marcin Stożek) | Elastic Ingest** 08:44 Okay. Okay.
**Juliano Costa** 08:46 And asked him… asked them about stuff, and yeah, I… But the guy that I spoke, he sent me to another guy, and this other guy wasn't there when I passed by, so I need to follow up on that.
Hopefully, I can find, his name on the… Oh, God.
on… on Slack.
Because otherwise…
**Perk (Marcin Stożek) | Elastic Ingest** 09:19 Oh, okay, yeah, I can see they use OpenTelemetry there.
**Juliano Costa** 09:27 What is his name?
Yep, yuns… Obs… I've lost some of…
**Perk (Marcin Stożek) | Elastic Ingest** 09:38 Okay?
Okay, good. So we got a.
**Juliano Costa** 09:42 yeah, but I'll ping him, because he said that, Rohit… Rohit was… Road, I'm not sure how to pronounce his, his name, would be the person to talk with, so I'll ping him and ask for the contact from Roit.
**Perk (Marcin Stożek) | Elastic Ingest** 10:02 Okay, okay.
Mmm… That works, that works. And for me, I saw somebody ping me on, after the blog post, we need to do the blueprint, so I'll do it this week. I guess it's easy, because it's almost like a copy and paste, like we discussed with Johanna.
**Juliano Costa** 10:20 Basil.
**Perk (Marcin Stożek) | Elastic Ingest** 10:21 Oh.
**Juliano Costa** 10:22 Okay.
**Perk (Marcin Stożek) | Elastic Ingest** 10:22 So it is here, this week, and it's going to be, just closed.
I hope not this year. You know, yeah, copy and sync this year, in the next, like, 60 days.
Oh, oh my god.
Okay. How's life at Dash Zero?
**Juliano Costa** 10:43 Yeah, it's pretty good. Now I'm actually being onboarded, like, I enjoy.
**Perk (Marcin Stożek) | Elastic Ingest** 10:49 Okay.
**Juliano Costa** 10:50 I had all the talks to, to deliver, and I was, then sick.
**Perk (Marcin Stożek) | Elastic Ingest** 10:55 Yeah, yeah.
**Juliano Costa** 10:56 Traveling, so all of that, but now, yeah, now this is my first Official, non… preparing for a talk week.
**Perk (Marcin Stożek) | Elastic Ingest** 11:07 Okay. Oh, you'll see. Okay.
**Juliano Costa** 11:08 Oh, yeah.
**Perk (Marcin Stożek) | Elastic Ingest** 11:09 Okay, okay, okay, great.
Very well. So, we'll talk in, like, a couple of months.
**Juliano Costa** 11:16 Yep. Okay, so… I think from here, we do not have any… From the things that we were discussing, I do not have anything on my plate.
**Perk (Marcin Stożek) | Elastic Ingest** 11:31 Yeah, me neither, I don't have any updates. Let's chase those guys from Envoy.
And I'll just, I'll just ping my… AI friend.
to ask about other projects from CNCF and Linux Foundation, which ones are using the OpenTelemetry, and yeah, let's start doing that. I guess you're right that now is maybe the good time to do it, so… Yeah.
**Juliano Costa** 11:53 I still think Severin would be a nice contact to reach out to. He is doing a really nice series on his LinkedIn.
**Perk (Marcin Stożek) | Elastic Ingest** 12:03 I forgot.
**Juliano Costa** 12:03 Using a bunch of different, projects.
**Perk (Marcin Stożek) | Elastic Ingest** 12:08 Oh, man, and Severin was there, and I was talking with him, like, for an hour or two at the OCMC last week, and I forgot… I thought I forgot that he was the one.
Oh, man. Okay.
Yeah, yeah. Okay, but now I can do it more easily.
Yeah, yeah, yeah.
Yeah, good point. Okay, okay, okay. So, yeah, I'm free, I don't have any updates for today.
No chaos.
**Juliano Costa** 12:35 Cool, I think we can… we could call it a day, and… Rub it up. …next week, yeah.
**Perk (Marcin Stożek) | Elastic Ingest** 12:40 Sure. Good to see ya.
**Juliano Costa** 12:42 Cool. Likewise?
Cheers.
**Perk (Marcin Stożek) | Elastic Ingest** 12:44 Have a good week. Thanks, bye.
**Juliano Costa** 12:46 You too.
