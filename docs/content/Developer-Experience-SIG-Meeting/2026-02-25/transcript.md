SIG: Developer Experience SIG Meeting
Date: 2026-02-25
Duration: 16 minutes
Zoom Recording URL: https://zoom.us/rec/share/h3vyP7pKgGtSSlXn4yP0mlUl52_Q44Cn6hYhZFo1iMc-qXXjivTmlapG9klEFFkd.JKfX8cViHyUly5IS
============================================================

## Zoom Recording Transcript

**Johanna Öjeling** 00:52 Good morning.
**Juliano Costa | Datadog** 00:54 Hello, hello. One sec.
Just kicking the… We've AI.
How are you?
**Johanna Öjeling** 01:07 Yeah, I'm doing well, thanks. How are you?
**Juliano Costa | Datadog** 01:10 Git, git?
Before we get into the things that are happening on the sink itself, I want to come back to you regarding one thing.
Yesterday we had the meetup here in these, and…
I asked the folks that were there that if they were… if they would be interested in having some folks from Grafana at a meetup, and everyone liked it, even though it would be in our holiday month.
**Johanna Öjeling** 01:42 -
**Juliano Costa | Datadog** 01:42 So we may…
may have that if you guys, of course, are willing to come to Linz. From Vienna to Linz is, like, one and a half, two hours train ride, depending on where you are.
**Johanna Öjeling** 02:00 -
**Juliano Costa | Datadog** 02:01 Yeah, but I think we can, like, arrange. I think…
topics would be nice to have things related to the open source space, and I think Grafana has a bunch of that.
So… but…
I didn't want to have only Old Town stuff. For me, it would be, like, an old OpenTelemetry meetup, but it's not, so maybe we could bring some Prometheus,
things, and maybe even K6, I don't know if the whole team will be there, or just the hotel folks, like…
Anyways, it is something to keep in mind. I will try to reach out to Marilia as well, because I already spoke with her about that.
So, yeah.
**Johanna Öjeling** 02:51 Yeah, that's…
**Juliano Costa | Datadog** 02:52 That may happen, yeah.
**Johanna Öjeling** 02:54 Yeah, that's great news, and we also got the dates now, so it will be end of August, beginning of September. So yeah, then we can check also internally what
Speakers may be interested, and yeah, if it's, possible to, you know, yeah, wait one day or afternoon or so, to shake the tree.
**Juliano Costa | Datadog** 03:18 Awesome. Yeah, we usually do…
after work, so it would be, like, starting at 6. We open the doors at 5.30, so we have some buffer to people leave their work and arrive. 6, we start with the first talk, and then we go up till, like.
8 or so, and then we have some snacks and stuff. We usually do two talks, but as it is, like,
I would say unique opportunity, or we may, like, have, like, smaller talks and have more talks about the things. I don't know, I think we can…
discuss and see what would be nice to have, and who would be interested from your side. So.
**Johanna Öjeling** 04:05 -
**Juliano Costa | Datadog** 04:07 And then we just need to set a date and look for a host that is willing to host us in that date.
**Johanna Öjeling** 04:14 Okay, -
**Juliano Costa | Datadog** 04:17 Because it's not, like,
It's a community-driven event, so we go around the city and ask for the… for the companies that are based here.
If they are… willing to sponsor, usually they…
Have they space, and they also provide some snacks and drinks.
**Johanna Öjeling** 04:38 Oh, okay, yeah, nice.
**Juliano Costa | Datadog** 04:41 So, yeah.
Nice, yeah, some folks got really excited, they came after the event to talk with me and said, hey, yeah, looking forward to that, I hope that works.
**Johanna Öjeling** 04:53 So,
Yeah, no, I think, yeah, that's a really good idea. I hope we can make something out of it.
**Juliano Costa | Datadog** 05:01 Awesome.
**Perk (Marcin Stożek) | Elastic Ingest** 05:02 Hey, guys.
**Johanna Öjeling** 05:03 Nice to see you.
**Juliano Costa | Datadog** 05:05 Hello, hello! You look like a hacker.
**Perk (Marcin Stożek) | Elastic Ingest** 05:10 Actually, Another hacker. The guy behind me is a hacker.
**Juliano Costa | Datadog** 05:14 The style of it.
**Perk (Marcin Stożek) | Elastic Ingest** 05:17 You know?
**Juliano Costa | Datadog** 05:20 Yeah, I… I have this thing on, when people… so, like, when you're talking with people and they leave the camera.
They're like, hi, I'm just fetching something, and then they leave the camera on, I take a screenshot of their background.
Which is usually their room, that I…
**Perk (Marcin Stożek) | Elastic Ingest** 05:39 Oh, wow.
**Juliano Costa | Datadog** 05:40 Yeah, and then it's creepy, but, funny at the same time. That is so funny.
**Perk (Marcin Stożek) | Elastic Ingest** 05:46 Okay. I love that.
**Juliano Costa | Datadog** 05:51 Let me, open the SIG meetings here.
Thanks.
So…
Just adding here, and adding… was here…
And I think for the agenda, we do not have any
missing thing? Like, or any planned thing, at least?
I know that I need to open the PR for the Macedon blog post. This is on my to-do list.
I think Adobe is also ready?
And…
**Johanna Öjeling** 06:55 Yep, it's approved, by Bogdan and yourself. I can ping Tristan also to see if he has any final, comments.
And then, Skyscanner, Neil came back with some more snippets to include, so…
**Juliano Costa | Datadog** 07:15 Cool.
**Johanna Öjeling** 07:15 Yeah, so I'll… I think he's still waiting for the PR communications department to approve it, but yeah, I can ping him as well and see.
If it's ready to go. Yeah, then we can also move this over to the OpenTelemetry I.O. repo.
**Juliano Costa | Datadog** 07:33 I'm seeing the… the snippets now. I just got the notifications, but I… This is really cool, actually.
Nice.
**Johanna Öjeling** 07:44 Yeah.
Yeah, it's nice that, we can, show, the readers
that much, like, real-life configurations. This is what, like, people have asked for.
So it's great that Skyscanner was willing to share so much.
**Juliano Costa | Datadog** 08:08 Indeed.
Cool. And then… Dusk, I haven't,
I haven't looked, through the blog, I just created the… the snippets, the… not the snippets, the illustrations.
Adjusted with the hotel logo and stuff.
**Johanna Öjeling** 08:36 -
**Juliano Costa | Datadog** 08:37 And, yeah, Tristan left a couple of comments on the… on the Mastodon one.
The ones that I can't address myself, I will do. The ones that he asked for more info from Macedon, I won't do, because that may take, like, an extra month.
**Johanna Öjeling** 08:57 Yeah.
**Juliano Costa | Datadog** 08:57 And we already got their final approval, I'll just move with, what we have. And Tristan is fine with that, so…
**Johanna Öjeling** 09:07 That sounds like a good idea.
**Juliano Costa | Datadog** 09:11 So I'll just add here, like, on the…
What is… what PR stands for, not on the… on the pull request space?
Like, it's publicly… public relations, right?
**Johanna Öjeling** 10:51 Yes. True, yeah.
**Juliano Costa | Datadog** 11:00 And… Which one is the other one? Adobe.
**Johanna Öjeling** 11:03 I do agree, yeah.
**Juliano Costa | Datadog** 11:04 Oh, baby.
Okay.
Maricin, is there anything that you would like to discuss?
**Perk (Marcin Stożek) | Elastic Ingest** 11:31 Yeah, I would, I talked, at the Auto Unplugged with a person from Key Clock.
And I have him here, let me show you, I have him here on the, this is funny, because I don't… I don't know his name.
But I know that it was him, you know, from Fosten, because he was at Fosten, and then he was at the Auto Unplugged as well. And I think he's, he's this person, Alexander Schwartz. And the reason I bring that up is that I talked with him about,
how they use KeyClock, so sorry, how they use OpenTelemetra at KeyClock.
And that they extensively…
I think instrumented KeyClock, and, you know, like, provide… have very, very good insights with them, and I wonder, maybe I should contact him, and maybe we should create a blog post. Maybe we should, you know, ask them to…
You know, contribute to our blog post with their user journey.
**Juliano Costa | Datadog** 12:37 I like that idea.
And Key Clock is, CNCF, projects, right?
**Perk (Marcin Stożek) | Elastic Ingest** 12:45 I think so, yes.
**Juliano Costa | Datadog** 12:46 I think so. Yeah, so I think it's nice to… to add… like, it's a nice touch to the story, like, how…
**Perk (Marcin Stożek) | Elastic Ingest** 12:53 It is.
**Juliano Costa | Datadog** 12:53 CNCF projects are using OPTEL to add observability to the… to their…
**Perk (Marcin Stożek) | Elastic Ingest** 12:59 Exactly, exactly. And the next one will be Kubernetes.
Will be.
**Juliano Costa | Datadog** 13:06 And in the end, the last one in the road will be the hotel collector.
**Perk (Marcin Stożek) | Elastic Ingest** 13:11 Oh, yes, the very last one, the very…
**Juliano Costa | Datadog** 13:13 Yeah, yeah. Everyone is using Auto except the telemetry Collector.
**Perk (Marcin Stożek) | Elastic Ingest** 13:20 Yes, yes, yes. And this didn't change for the past 4 years, it's unbelievable.
**Juliano Costa | Datadog** 13:25 Yeah. What, what's his last name?
**Perk (Marcin Stożek) | Elastic Ingest** 13:29 Let me sorry, I will put that. He said, farts.
**Juliano Costa | Datadog** 13:34 So, so I wanted to ask you if maybe you talked with him?
**Perk (Marcin Stożek) | Elastic Ingest** 13:39 Maybe because, you know, like, he was there for the full day,
But… so if you talk with him by any chance, then I wanted to bring that up. If you didn't, then I wanted to… I wanted to come here to know if you talk with him, and if I can… if there is any chance for me to find him, then I just looked it up on the website, and it's on Google, and I found him, so…
I just… I just…
**Juliano Costa | Datadog** 14:04 So, I… I never, I never spoke with him, just found out about him and Key Club now. So, I know the project by name, but,
I think it would be nice to… to bring him, and maybe schedule a call so we can…
do a recording. Usually the record… usually the recordings we do not do on this one, because this one is.
Recorded in… It is automatically made available to everyone.
But as it is a CNCF project, I don't know there are any…
secrets that needs to go through PR and stuff, so maybe we could even use the… the SIG meeting and… and do… because it's easier, so, like, if…
By his name, I think he's German or Austrian, so…
**Perk (Marcin Stożek) | Elastic Ingest** 15:03 I think so.
**Juliano Costa | Datadog** 15:03 most…
probably, if he's based in EU, I think this time, would be a cool time for him to join. So we can invite and see, hey, do you have any Wednesday at 10 a.m.
**Perk (Marcin Stożek) | Elastic Ingest** 15:16 Exactly.
**Juliano Costa | Datadog** 15:16 In the following weeks, so we can sync, and then we… we do it.
**Perk (Marcin Stożek) | Elastic Ingest** 15:21 Very good, okay. I'll contact him on LinkedIn, and let you guys know.
**Juliano Costa | Datadog** 15:29 Awesome. Awesome. Yeah, if you…
If you cannot… if you do not get any reply from him on LinkedIn, let me know. I may have other channels, CNCF Ambassador, and try to… to…
Sure. Somewhere.
**Perk (Marcin Stożek) | Elastic Ingest** 15:48 Yeah, maybe on Slack as well, or whatever.
Yeah, okay, so that was, that was my only topic. Also, by the name, by the way, my name is Martin, so you're correct, but I go by Perk everywhere, so…
**Juliano Costa | Datadog** 16:06 Oh.
Perkiness. Awesome.
Okay, cool. Anything… Anything else from your end, Johanna?
**Johanna Öjeling** 16:24 Nope, we don't think so.
Yep.
**Juliano Costa | Datadog** 16:34 Okay.
Then I think we are good to call it.
Yep, yeah. Thanks for joining.
**Perk (Marcin Stożek) | Elastic Ingest** 16:45 See ya.
**Johanna Öjeling** 16:47 Fantastic.
Okay, thanks.
Have a great day.
**Juliano Costa | Datadog** 16:50 Bye.
