SIG: PHP SIG
Date: 2026-05-13
Duration: 23 minutes
Zoom Recording URL: https://zoom.us/rec/share/6yewBpi24w_btr3fLtaANzFGWfOeV-SjWqvYSYVy7gaeXrXOuR9_ifXYyR-_OCP4.HxQLPAWXjw0V4Gr2
============================================================

## Zoom Recording Transcript

**Sergey Kleyman** 01:54 Hello.
**Bob Strecansky** 02:11 Hey, Sergio, how are ya?
**Sergey Kleyman** 02:13 Good, how are you?
**Bob Strecansky** 02:15 Hmm?
**Sergey Kleyman** 02:16 How's the weather? Getting warmer?
**Bob Strecansky** 02:20 Yeah, it's, like, 15, now it'll be… 22 later today, and it's gonna go up to, like, 30 this weekend.
**Sergey Kleyman** 02:28 Is that… Is that on Celsius?
**Bob Strecansky** 02:32 Yeah.
**Sergey Kleyman** 02:33 Oh, so you're pretty fluent in Celsius.
**Bob Strecansky** 02:36 Yeah, a couple years ago, I changed my car to Celsius in 24-hour time, because I was like, I know the American… I know the American units, so when I talk to people that don't use Freedom units, then I can give them valuable output.
**Sergey Kleyman** 02:51 What about the height? I think the hardest… because I think the formula for the temperature is not that complicated, especially if you're doing it constantly. But height, I find height is, I guess you can guess it by people mentioning it, like, 6 is supposed to be where people start to be tall, right? So it would be probably maybe 180 in centimeters? 6 feet?
**Bob Strecansky** 03:16 Yeah, oh yeah, I'm, 1.88 meters tall.
I know that much.
**Sergey Kleyman** 03:23 So you're 180. Okay, 180 centimeters. And how tall are you in feet?
**Bob Strecansky** 03:31 Yeah, it's not an easy…
**Sergey Kleyman** 03:33 Okay, so… So is it easy for her to map, like, if, if somebody's, like, how tall is, like, LeBron James? Like, 7, maybe even more?
**Bob Strecansky** 03:44 Yeah, he's 7 feet tall. Or no, he's like 6'8", maybe? 6'10".
**Sergey Kleyman** 03:49 So, how much is it in centimeters?
**Bob Strecansky** 03:52 Don't know, I have to use a calculator.
**Sergey Kleyman** 03:55 Oh, okay, so you're not completely switched, so…
**Bob Strecansky** 03:57 Oh, no, no.
**Sergey Kleyman** 03:58 Okay.
**Bob Strecansky** 03:59 I would definitely not, but…
**Pawel Filipczak** 04:03 Hey, guys.
**Sergey Kleyman** 04:04 Alright, Paul.
**Bob Strecansky** 04:05 Wow.
Here we go.
**Sergey Kleyman** 04:09 Will we have any surprise guests, today?
**Bob Strecansky** 04:13 I don't think so. I think it's just the three of us.
**Sergey Kleyman** 04:16 I'm scared that guy.
**Bob Strecansky** 04:19 Oh, yeah, he DM'd me a couple times asking me where to look at, like, how to start and what to look at, so we'll see.
**Sergey Kleyman** 04:26 That's good.
Kissing.
**Bob Strecansky** 04:35 Yeah, I guess we can get started. I don't expect anybody else today. Chris is still on vacation.
Let's see… Do y'all have any agenda? I don't have any, like, explicit agenda topics there. Do y'all have anything that you want to discuss?
**Sergey Kleyman** 04:49 No.
**Pawel Filipczak** 04:52 Alright.
**Sergey Kleyman** 04:53 I don't.
**Bob Strecansky** 04:53 Okay.
**Pawel Filipczak** 04:55 just, you know, updating the distro, adding some small features, but nothing spectacular. So, I think the most important is that we have the support for the PHP 8.5, right, Sergei? Is there anything, you know, bigger?
8.5?
Yeah.
**Sergey Kleyman** 05:12 Yeah, I think from user's point of view, the biggest one that we did recently.
**Pawel Filipczak** 05:17 Yeah.
**Bob Strecansky** 05:22 Cool.
Whoa.
**Pawel Filipczak** 05:27 And that's his…
**Bob Strecansky** 05:28 Oh, that's… that's easy enough.
Yeah, let me see… I will… Go back here… Oh, I do have one update. I forgot about it, We are gri- OpenTelemetry is graduating from the, Intubator project. It is going to be a full-fledged CNCF project now, with the release of 1.0.
So they're still talking about stable. I know you were talking about it earlier, Powell, it's stable by default, or is that you, Sergey?
**Sergey Kleyman** 06:09 Yeah, I think I mentioned that issue. Is that connected to the decision of making it, 1… 1-0?
**Bob Strecansky** 06:17 Somewhat. I think… I think that's, like, the CNCF wanted it to be, like, wanted us to have a stable release to, like, finish the intubation pro… project… process and become, like, a full-fledged CNCF project, but I think… I don't think it's, like, 100% necessary… it's not 100% contingent on that, but I think that's something that they wanted, so they're definitely putting some extra sauce on Stable by default, which is good.
I think, we also discussed in the maintainer, or, like, the, specifications SIG, the, it's not to be confused with the Alice Distro, but, like, they are starting a new SIG group that talks through, how to distribute OTel.php in, like, an installable binary for a bunch of languages. So, like, how do we get, OTel, how do we get OTel for specific languages, and the requirements on the host? Which, like, feels similar to y'all's distro, but I think slightly different, so there's a new SIG for that, so I thought y'all might want to know about that.
**Sergey Kleyman** 07:25 So you're saying it will be one package, but it will cover all the supported languages in one package?
**Bob Strecansky** 07:30 I think that it's… I think it's going to be language… language-specific. I don't know a lot of the details yet, I just know that that's, like, it's spinning up.
**Sergey Kleyman** 07:39 Hmm, that's interesting. I mean, I can see also some more Chanel having one package both languages, like, assuming that people don't even know what technology is used, Like, ideally, the best, like, DevOps would be to discover and monitor, right? That would probably be ideal for them, right? They just say, okay.
This is my machine, and monitor everything that runs on it, right?
**Bob Strecansky** 08:03 I think it's more along the lines of, I am a… Java developer, and I want to make sure that I have open telemetry, how do I… how do I use that as quickly as possible? Because, like, there's, you know… the collector, and there's, like, APIs and SDKs that are installable for a user, and a bunch of other things, but I think that overall there's no… It's… I'll be the first one to agree with this. It's like, it's hard to get OpenTelemetry installed sometimes, and, like, all the dependencies and all the things that go along with it, and so on and so forth, so… Thanks for…
**Sergey Kleyman** 08:36 And it does suit what we want to do with digital, right?
**Bob Strecansky** 08:40 Yeah, it seemed… that's what I was mentioning, it seems like… very, like, along the same path. So, I think that…
**Sergey Kleyman** 08:49 But you see some differences? You mentioned that maybe it's not 100% what they want to do. You see some difference in goals here?
**Bob Strecansky** 08:57 I'm not… I'm not 100% sure. They talked about it a little bit in the meeting, so I would… I'll see if I can find… hold on, let me see if I can find that, That discussion.
**Sergey Kleyman** 09:09 How'd you… Oh, wow.
Ginivaldo? Is… did I pronounce it correctly?
**Genivaldo Silva** 09:18 Yeah, that's correct. Yes, that's correct.
**Sergey Kleyman** 09:20 Lost that.
**Genivaldo Silva** 09:21 I woke up.
**Sergey Kleyman** 09:21 Quebec.
Excellent.
**Genivaldo Silva** 09:24 Thank you.
**Sergey Kleyman** 09:38 Yeah, so… we would definitely be, kind of, like, I think this was the… at least the… In my mind, I mean, I guess what you started with, like, when you said, I'm a Java developer, like, the way we thought… and again, maybe it just suits developers as well, but the way we saw Distro is more like targeting DevOps guys.
Like, so they definitely don't have access to application, they cannot change it for sure.
So, how do we essentially… Handle the use case, right?
Right. But, yeah, so… but if we can also make it usable for developers, sure, why…
**Pawel Filipczak** 10:20 It is. If you have it installed, then every IP on your system will be instrumented automatically, right?
**Sergey Kleyman** 10:26 Yeah, yeah, sure. Yeah, that's, I mean, I mean, I guess that we definitely would love developers to… That's probably also one of our near-term goals that we wanted to ask you guys, is what would be the best way to promote this kind of, like.
What you mentioned, how can we kind of, like, highlight the fact that people can skip all these, maybe manual steps and just install Distro and try it out?
That would be nice if we can somehow advertise that.
**Pawel Filipczak** 10:59 I have Docs PR ready, so I think I have to update it and push the docs into the OpenTel MetroIO docs page, so then it will be auto-promoted, at least in the docs, so…
**Sergey Kleyman** 11:13 Okay, so you're saying people will immediately see when they look at the docs. Okay, that's cool.
**Pawel Filipczak** 11:16 So I will do that today, tomorrow. Yeah, I've completely forgotten about that. I prepared the PR a few weeks ago, and… Yeah.
**Sergey Kleyman** 11:26 Yeah, the docs is fine, but I… for some reason, I think most of the developers, especially the ones that already know about the product, probably don't go to Docs, right? They already know…
**Pawel Filipczak** 11:35 That's true.
**Sergey Kleyman** 11:35 So the question is, how can we reach them? Maybe, maybe we should… we can publish some kind of blog, showing, did you already do that for… for OpenTelemetry? Maybe we can do it when we will have official 1.0 release for Distro?
**Pawel Filipczak** 11:52 So I wrote a blog about the donation, that it's complete, and we have the distro ready.
And it's published in the blog page of the OpenTelemetry AO. The docs tab, and also the blog tab there.
So it's already there.
Of course, if we'll switch to 1.0, then, yeah, it will be nice to have it, hmm?
I mean.
**Sergey Kleyman** 12:16 Okay, okay.
**Pawel Filipczak** 12:17 Yeah, non-depression.
**Sergey Kleyman** 12:19 Yeah, maybe we… maybe we can maybe paste that link on the… on the Slack channel. Maybe we'll do that, maybe.
**Bob Strecansky** 12:26 We could put it in the title bar if you want to get people's attention on it, if you want to.
**Sergey Kleyman** 12:32 Yeah, that would be great, like, if we can get feedback and start seeing, like, what people would want feature-wise.
That would be great, like, if, better understanding what are the difficulties, and how Distro can solve them, and obviously find bugs.
**Bob Strecansky** 12:49 Yeah, I think… I don't know, since I've started working on this project, what was that, 7 years ago? It seems like that's been one of the most difficult parts, is like, how do you evangelize using these technologies effectively, right? And because… the… VIN diagram of people that are interested in observability, interested in PHP, and instrument… interested in instrumenting this library art. That's a small… a small intersection, so we need to be able to capture and get attention to those people however we can.
**Sergey Kleyman** 13:21 Yeah.
Without maybe reaching out, I understand that Laravel is kind of, like, really becomes a really prominent, part of HP ecosystem.
So, we have one guy in Elastic, he's kind of like, What is the main guy in Laravel? Otwell? OTEL?
Don't remember his name.
So he's kind of, like, maybe in some… has some connection there, so maybe we'll try to… to find ways to… to see if OpenTelemetry can become a bigger part in Laravel.
**Bob Strecansky** 13:55 I think, yeah, I have a strong feeling that we've talked about that a lot, too. It's like, that… is how… that is almost certainly how we'll get a lot more adoption. Like, how do we get default instrumentation in WordPress? How do we get, Laravel and Symphony, like, first-class citizenship, those things. I think we just have to figure out how to do that effectively.
**Sergey Kleyman** 14:18 Yeah, WordPress can definitely… if we think that WordPress would be an interesting use case for us, we can kind of, like.
bring the most initial value with Distro, because Distro, we can automatically instrument WordPress. We don't need any manual changes to the application, right? So, it would be interesting, we just need to make sure that we generate enough value, maybe we'll need to improve the instrumentation itself.
But the whole manual thing that was required if you do… if you just use SDK in the instrumentation, it's not necessary with Distro. Distro can do all that automatically, right? So maybe it's a good point, maybe WordPress might be an interesting place to kind of, like, start.
**Pawel Filipczak** 14:59 distro. I'm testing distro with the WordPress, so it works great, and it shows all of the database calls, but I think that we can improve with metric collection from WordPress, so it might be an, PVV intake.
**Sergey Kleyman** 15:15 Yeah, let's… let's float it out, let's discuss, maybe we can prepare suggestions for the… one of the upcoming SIG meetings.
And, get feedback from you guys, if you're familiar with what people would want from… how can we improve what WordPress instrumentation generates?
And so, we kind of, like, can solve the manual stuff with the distro, but obviously, it will be better if we can also provide value with instrumentation itself, like what Paul mentioned. Maybe additional metrics, and whatever people want to see when they want to monitor WordPress.
**Pawel Filipczak** 15:48 Yesterday, I was reviewing the popularity of the packages, OpenTelemetry packages, on the Packages page.
And it looks like we should include some additional instrumentations into the… into the distro, like, resource detectors for the cloud environments, so that's what we are missing now, and I saw the PR with the Magento 2 instrumentation. I think it might be also quite interesting.
And of course, WordPress, but we have some auto-instrumentation for the WordPress. It requires a bit of manual tricks to install it.
But it's… it's just… it's… I think from… it's… it's not bringing anything… anything useful, so, I mean, from the… from the distro point of view, because in the distro, you are just instrumenting the database calls automatically, so, yeah.
So, maybe…
**Sergey Kleyman** 16:51 at the moment, it just instruments database calls from the WordPress side, and that's…
**Pawel Filipczak** 16:56 Yes, yes, yes, yes, yes.
**Sergey Kleyman** 16:58 Yeah, so that might be an interesting project, maybe, to improve it, because maybe this combination of the fact that distro, we can skip all the manual steps for WordPress, and if we will improve WordPress instrumentation by providing more value than just database calls.
**Pawel Filipczak** 17:12 Hmm?
**Sergey Kleyman** 17:12 can be done just with MySQLI instrumentation.
**Pawel Filipczak** 17:15 Okay.
**Sergey Kleyman** 17:16 Interesting, okay.
We'll follow up on that.
**Bob Strecansky** 17:27 Make sure to take a look at the board.
I was looking earlier how I could, Take a look at them, minus Renovate, so… that's… Kinda cool.
Wait, let's see… Let's see… Let's reduce the odds.
Magento stuff, I'm gonna take a look at this… Sergey, you were working on these, consistent projects.
**Sergey Kleyman** 18:10 Yes, I need to get back to that. I needed to finish something, quick, That was in the middle, but I will get back to it, yeah, this week.
**Bob Strecansky** 18:18 Okay. These two, I have to wait for Brett or Chris, because we can't… Merge them without that. Okay, that seems like pretty much everything good. Same thing with this one…
**Sergey Kleyman** 18:34 By the way, I saw that the OPR with the 4MB is failing. Is that an issue with the flaky tests, or…
**Bob Strecansky** 18:41 Yeah, I think… I think, I have to… I think that we definitely have some… we have some sort of failing CI stuff. We really need to pri… somebody needs to prioritize that, because, like, we've talked about this before, people aren't going to contribute if every time… I think that's something we… that somebody needs to prioritize pretty highly, but…
**Sergey Kleyman** 19:02 Yeah, we would like to take that to the moment we, We get, what we currently have in the short term to the distro. That's our highest priority, to stabilize the tests.
**Bob Strecansky** 19:13 Okay.
**Sergey Kleyman** 19:14 get you.
**Bob Strecansky** 19:15 That's…
**Sergey Kleyman** 19:16 If you guys have any ideas, well, I guess when we will get close to it, But if you have any ideas how to do it properly, like, I thought maybe we can somehow mark the ones that should be stable, and then if they fail, then it will kind of, like, fail the build, and then… There will be ones, like, you know, dirty room, clean room, so we'll start with the… and then we slowly will kind of, like, mark tests as, or we can do it the other way around, mark only those that are unstable, and then they will not fail the build, but the ones that are stable.
We should fail the build, and then we can slowly kind of, like, minimize the number of unstable tests.
**Bob Strecansky** 19:55 Right, makes sense to me.
**Sergey Kleyman** 19:57 Or maybe if you… that's just something that I thought maybe you guys, if you have any other ideas, how to… Make this kind of, like, incremental process, that would be also… Definitely would be interesting to consider.
**Bob Strecansky** 20:11 Let's see… That's too true.
Like, let's just look at one of the most recent ones.
I don't want you.
That's what I want.
Try this one… This looks like it's a Psalm error that… is just… I think it's little stuff like this, like, we have to fix these things. Like, this works for 8.5. I'm wondering if one of the renovate updates just, like, broke this for older versions or something, and we have to redefine something. This is probably worth… like I said, we need… somebody needs to investigate this.
We'll get back to it.
And then, instrumentation, same thing here.
World 2… What was these two old ones?
Alright, so let's look at the project board, too.
See if there's anything that's… processing… We're siding on this.
Yeah, these are all the important things.
Yeah, I'm wondering if, I'm wondering if we can try and fix some of these as soon as possible.
We'll get there.
Okay, anything else anybody wants to bring up today?
**Sergey Kleyman** 22:38 That's it for me.
**Bob Strecansky** 22:40 Alright, well, thanks, y'all.
**Pawel Filipczak** 22:43 Too good.
**Sergey Kleyman** 22:44 Guys.
**Bob Strecansky** 22:45 No, no.
