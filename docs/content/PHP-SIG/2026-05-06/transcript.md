SIG: PHP SIG
Date: 2026-05-06
Duration: 29 minutes
============================================================

## Zoom Recording Transcript

**Sergey Kleyman** 03:17 Hello.
**Genivaldo Silva** 03:22 Hello.
**Sergey Kleyman** 03:24 Alright.
**Genivaldo Silva** 03:26 I…
**Sergey Kleyman** 03:28 You can hear me okay, right? I can hear you.
**Genivaldo Silva** 03:32 And could you repeat, please?
**Sergey Kleyman** 03:34 No, I just wanted to make sure, if you can hear me…
**Genivaldo Silva** 03:39 Oh, I…
**Sergey Kleyman** 03:39 But it seems like…
**Genivaldo Silva** 03:40 I hear, I hear.
**Sergey Kleyman** 03:41 Maybe not…
**Genivaldo Silva** 03:42 Yeah.
**Sergey Kleyman** 03:42 Not 100%, but… Okay, good, I can hear you as well.
**Genivaldo Silva** 03:46 I can hear, I can… I can see you.
**Sergey Kleyman** 03:53 Great, okay.
Do you know if Bob is going to join today?
Let me see… was there.
Oh, he has both?
**Bob Strecansky** 04:04 That's okay.
**Sergey Kleyman** 04:04 Bob, are you familiar with that movie? What about Bob? With the Bill Murray, and .
**Bob Strecansky** 04:11 Oh, I'm embarrassed.
**Sergey Kleyman** 04:11 That was quite a good move.
**Bob Strecansky** 04:13 I'm very familiar with that one, because I get that a lot, and I also get… there's a children's TV show called Bob the Builder. I get that a lot, too.
**Sergey Kleyman** 04:22 Mmm.
Yeah, but that's the problem. If you didn't… if you haven't grown up in the States, then as a grown up, it's… it's tricky to get exposed to that, but, yeah. That's right.
**Bob Strecansky** 04:33 That's right. Yep. And it's extra fun, because my dad's in construction, so… or was in construction, so… of course I'm Bob the Builder.
Hello, new person!
**Genivaldo Silva** 04:46 Hello?
**Sergey Kleyman** 04:48 Right?
**Genivaldo Silva** 04:49 Welcome. I'm Jane Volk.
I'm… I'm from Brazil.
**Bob Strecansky** 04:54 Oh, very nice.
**Genivaldo Silva** 04:56 Yeah, but I… I try better my English, and I… I… I'm sorry for my, salt duck.
**Bob Strecansky** 05:07 Your… your English is much better than my Portuguese.
**Genivaldo Silva** 05:14 I believe that.
**Sergey Kleyman** 05:15 What time is it? What time of the day is it for you? Well, I guess it should be similar to Yu-O's time, huh, right?
**Bob Strecansky** 05:20 Yeah.
**Sergey Kleyman** 05:21 Guys? Hmm.
This is the beginning of the day, right? I assume.
**Bob Strecansky** 05:27 I… That's true.
**Genivaldo Silva** 05:28 I start to use, open telemetry in my projects.
Yeah, in…
**Bob Strecansky** 05:35 Very cool.
**Genivaldo Silva** 05:36 in… This ear. Yeah, this ear. Yeah, I… I… I won't… contribute as well.
Very good. I hope, I hope.
**Sergey Kleyman** 05:53 Is that your personal initiative, or are you working for a company that uses OpenTelemetry?
**Genivaldo Silva** 06:00 And this moment, I use, in my company. I… But I try… use in future… in my pet projects. I have, one pet project, for, how can I say, In vehicles, yeah, and, and, analyze vehicles.
By plate.
**Bob Strecansky** 06:24 difficult.
**Genivaldo Silva** 06:25 Yes.
Very cool.
**Bob Strecansky** 06:28 Alright.
**Genivaldo Silva** 06:29 In future, this moment, I use… Is that, is that possible?
**Sergey Kleyman** 06:32 Is that something that you… is that application that you're trying to use OpenTelemetry on, is it public? Is it possible to see it, or is it internal?
**Genivaldo Silva** 06:44 This moment here, not totally public key. We have some services, And only internal.
company, but in… Next year may be… in… True.
to next month, and we have a public application use OpenTelemetry.
**Sergey Kleyman** 07:11 If you… if you will find the time, and you will be interested to show us, maybe sometime in the future, how you use the product, and how it can… how it helps you, and what can be improved to even help more, we'd be very glad to see that, like… Us as developers, we're not always getting, you know, feedback from real-world users, which, you are one of them, so it would be very interesting to us.
to hear feedback from somebody who uses OpenTelemetry for real-world applications.
So if you have a chance… if you have a desire and time to do that, it would be very interesting. Nothing formal, just to, you know.
And mostly, it would be interesting to, you know, any kind of, like, if you have some feedback, what can be improved, what can be done better, and additional features, that would be very interesting, yeah.
**Bob Strecansky** 08:02 Agreed.
Alright, well, I guess we'll get rockin'.
So… just to get, just to get you caught up to speed, the document that I shared with Zoom is the one that we have for our meeting agenda, so we usually go through that. If you have an agenda topic that you'd like to talk about, you can add in the agenda, and then we look at… we walk the, repositories and see if there's anything that we have going on.
With the project, so… I haven't like them.
**Sergey Kleyman** 08:31 But, you had to… sorry, sorry for interrupting.
**Bob Strecansky** 08:36 You're not… you're not interrupting. Yeah, I didn't have any specific agenda topics today, so if there's something you want to talk about, Surya, we definitely can.
**Sergey Kleyman** 08:43 Oh, okay, thank you. So, what I wanted to ask you, is there any document regarding how we generate, kind of PHP stubs, or I don't know how we formally call it, out of, essentially, same kind of package for PHP, out of the semantic convention themselves, because, one of the guys on our team from Java team, they mentioned that there are already… I think version of the current SEMCOM is, like, 141 or something like that, and I noticed that the latest package that we have on the packages is, like, 138.
So, and it was released, like, in January this year, so I was wondering if I maybe can, try to release the newest, if it's something that, you know.
That is, possible for…
**Bob Strecansky** 09:29 I think… I think, the answer to your question is, I don't think there's any documentation currently. I know Brett was, he was keeping track of those semantic conventions. I have not done a good job of that, so maybe that's something that we need to visit. The other thing, I know there is a package that gets used by the semantic convention group. I think it's called Weaver, and Weaver does a good job of generating the semantic stubs, and… I think that that's…
**Sergey Kleyman** 09:57 But I assume Brett already kind of, like, automated that, right? I assume he has some tools that do that.
**Bob Strecansky** 10:01 I don't know that he did. We can… we could definitely ask him, but my guess is… from what I've seen, he doesn't… he's not really much of a… an automator, per se.
At least not… at least I haven't seen it. Like, I think that that's… my guess is that would be ripe for a GitHub action, to, like, be able to generate semantic conventions with Weaver based on whatever version you pass in. It seems like something that we could do.
**Sergey Kleyman** 10:25 Right. So you think the best course of actions at the moment would be for me to reach out to Brett over Slack, right? Do you communicate with him over Slack?
**Bob Strecansky** 10:34 Yeah, he's a little bit delayed because he's on paternity leave, but he, yeah, maybe in that hotel, the PHP Maintainers channel would be a good place, just tag him, and, feel free to tag me if you want to, too.
**Sergey Kleyman** 10:46 There is a separate channel for, when you say… Yeah!
**Bob Strecansky** 10:50 I think, I think you got added, let me double check.
PH… Hotel PHP, yeah.
**Sergey Kleyman** 10:55 HP, and how is the channel that you refer to? How it's called?
**Bob Strecansky** 11:01 Oh, hold on one second… Yeah, you were not added, so I'm gonna put you and Powell in here.
**Sergey Kleyman** 11:08 Thank you. So, essentially, my goal would be then to sync up with Brett, and essentially maybe automate it to a degree that… and obviously document it. So, I will ask the Java team how they handle it, like.
I assume it's still manual in the sense that somebody needs to initiate it, like, somebody needs to follow and see if a new version of Simatic Convention is published, and kind of, like, change that to that version number, and But I will sync up with Java and find out how they do it, and maybe see if it's the same approach suitable for us, and take the same approach.
But I will try my best to also document it, so if, If somebody will be in the same position I am now, that you can exploit and say, okay, here's the document how to do it, right?
**Bob Strecansky** 11:58 Right. Yeah, that would be… that would be wonderful. Thank you for taking that on. I think. It's one of those things, it's just… I call… at work, I call those ankle biters. It's just… it's not something that's, like, super important, it's just, like, it will nip at you.
**Sergey Kleyman** 12:10 Yeah, sure.
**Bob Strecansky** 12:11 You…
**Sergey Kleyman** 12:11 Definitely.
But I think it's the right approach, right? As long as it's working, and it's not a priority, you leave it alone. Now it's time to make it more formal, so other people can pick it up if necessary, so we can make it more formal, yeah.
**Bob Strecansky** 12:28 Sounds good.
Cool.
**Sergey Kleyman** 12:33 So that's it from me.
**Bob Strecansky** 12:35 I did have an agenda topic, I… it's… in the maintainers meeting last week, and they were talking about using AI to, look for vulnerabilities in our repositories. And so, I did that this past week.
If anybody is interested in seeing the findings from that, I… put them in a private Google Doc and, like, sharing them very limited to people who might be interested, I didn't want to share that publicly for obvious reasons, but…
**Sergey Kleyman** 13:09 Is there something serious that we need to fix as soon as possible?
**Bob Strecansky** 13:13 No, I don't think so. There's just… there's, there were, like, a couple very, like, very small, minor things that realistically probably aren't… Like, earth-shattering, but… Yeah.
**Sergey Kleyman** 13:25 Is it easy to assess, like, how severe, indeed, any of those floated issues? Like, Like, is it possible that some of them, you know, marked as medium-high severity, but actually…
**Bob Strecansky** 13:39 No, it's a… I think, I think…
**Sergey Kleyman** 13:42 No, we don't have any of those anyway, so…
**Bob Strecansky** 13:44 No, I don't think so, and… I think… I don't think it, like… how do I say that the right way? It definitely just, like, groked the codebase and found some. I don't think it, like… I don't think it stacked against, like, a severity index. It was just… I think it just, like, sort of picked its own severity for some of the issues.
But, again, nothing earth-shattering, but… just thought it was kind of a fascinating exercise. And I think I mentioned this last week, but I'm gonna keep mentioning it. There's, gitHub is now doing security advisories for our repositories, and they're not enabled, so, I'm definitely gonna keep my eyes on those. They asked the maintainers to make sure that we did that, so…
**Sergey Kleyman** 14:25 The reason I asked about it is that I don't know if you read those articles, like, for example, Curel guys, they stopped, I don't think they even have Bounty, but I think they tried to kind of, like, encourage people to file security issues, but then they saw that a lot of people filed just what is called AI slop, right?
**Bob Strecansky** 14:43 Yeah, oh, yeah.
**Sergey Kleyman** 14:45 And they just closed that. They said too much time is wasted to even estimate, like, claims that this is the high severity issue, but then too many turned out to be just hallucinations, not even low severity issues, just nothing.
**Bob Strecansky** 14:59 Yeah, I think… I think, I mean… the fundamental crux there, right, is if you have a bug bounty, people are going to try anything they can to get that money. The, like.
Do it, like… investigating for the quote-unquote, for the love of the game is different than investigating for, you know, for money. And I'm sure that some of those bug bounty things… We're valid, but yeah, trying to sift through the noise is… super tough sometimes, and yeah, like you said, it's… a lot of it is slop, there are a lot of hallucinations, and discerning what is real and what is not real can sometimes be more difficult than just doing the work. At least that's what I've found in my experience, but I think… I think it doesn't… it shouldn't preclude us from Doing these things, it's just we have to have a discerning eye while we do them, which is something.
**Sergey Kleyman** 15:51 Right, right.
Okay, sounds good. Thank you.
**Bob Strecansky** 15:54 Yep.
All right. Genevaldo, is there anything specific you wanted to talk about today, or are you just observing today?
**Genivaldo Silva** 16:06 No, my… And my participation today, it's only… Here.
**Bob Strecansky** 16:17 You're just watching.
**Genivaldo Silva** 16:18 Yeah, here, and it's watching, and it's my first time in My first time participation in…
**Bob Strecansky** 16:28 In a SIG meeting.
**Genivaldo Silva** 16:30 Yeah, there's… it's a SIG meeting, yeah, and it's… for me, it's totally new, and I… I'm… Very nervous, because.
**Bob Strecansky** 16:42 Oh…
**Genivaldo Silva** 16:42 English here.
It's not my first language.
**Sergey Kleyman** 16:46 There's nothing nervous about it, it's completely informal. You can… you can ask anything.
Look at mine?
**Genivaldo Silva** 16:52 Yo.
I…
**Sergey Kleyman** 16:54 It's public, so you should never expose anything that you don't want to be published to everybody on the internet, but… Other than that, it's not completely informal, so if you have something that you're not sure about, go ahead and you can ask, and There is no penalty, that's all for.
**Bob Strecansky** 17:12 God.
That's right.
We have lots of people whose… we have lots of contributors where English is not their first language, so you are not alone, for sure.
**Genivaldo Silva** 17:21 Yeah, I… I enable caption for me, because I… I don't understand totally, totally meeting, yeah. But I… I work my English for… Understand, understand, totally.
**Bob Strecansky** 17:41 Very cool.
**Genivaldo Silva** 17:42 Future, I think, contrib… contribute more, yeah. But, but, I… I follow projects and new releases, and I update my projects with, new releases, especially in… Laravel, out instrumentation, yeah.
this moment here on Laravel, it's my… first framework.
**Sergey Kleyman** 18:16 IE applications that you monitor, they use Laravel?
**Genivaldo Silva** 18:19 Yeah, my application this moment, she used Largo.
And we have, and we have, one application that use netcore. But, but I don't… maintain this project, other person.
Maintain this project.
**Sergey Kleyman** 18:47 You yourself, are you a developer? Are you a developer? You write in code?
**Genivaldo Silva** 18:52 Yeah, at this moment, yeah, I'm a PHP developer.
**Sergey Kleyman** 18:58 You should be out.
**Bob Strecansky** 18:58 room.
**Sergey Kleyman** 18:59 So it's much easier for you to deal with BHP than .NET, I assume.
**Genivaldo Silva** 19:04 Yeah, I like to, like, be… I have, how can I say? I have love for PEP.
**Sergey Kleyman** 19:14 That's interesting.
**Bob Strecansky** 19:15 Yeah.
**Sergey Kleyman** 19:16 Which we popular in Brazil? Is that something that's popular?
**Genivaldo Silva** 19:19 Yeah, very popular in Brazil, PHP, and in this moment, she, I think, GoLink, it's… very popular as well, I think.
Yeah, I… I tried instead goaling in… future, I think.
**Sergey Kleyman** 19:44 No, I've been.
**Bob Strecansky** 19:44 Excellent.
**Genivaldo Silva** 19:45 That's my other love.
**Bob Strecansky** 19:46 That's on the matter of language, too.
**Genivaldo Silva** 19:48 Yeah, I… I… I'm so sorry, but I need to go now, because I have.
**Sergey Kleyman** 19:54 What is…
**Genivaldo Silva** 19:55 a company.
**Sergey Kleyman** 19:56 Feel free to join next time.
**Bob Strecansky** 19:57 Yeah, you're always welcome.
**Genivaldo Silva** 19:58 See you next week. Thank you. I think. I hope.
Bye-bye.
**Bob Strecansky** 20:03 I know.
**Sergey Kleyman** 20:03 Bye, nice meeting you.
**Bob Strecansky** 20:06 Alright, Sergey, so to look at, the rest of the board real quick, it looks like you had two draft PRs.
**Sergey Kleyman** 20:13 Yeah, yeah, I misunderstood. I thought… I copied what Java did, but then I saw that it's not, so I'm… I will redo them a bit, and then I will… I will remove the draft, and maybe I will pin you when it's ready for review.
**Bob Strecansky** 20:26 Yeah, that's… that's easiest. My GitHub… I get swallowed in a sea of GitHub notifications, so if you just ping me with it, I'm happy to review it when it's ready.
**Sergey Kleyman** 20:33 Yeah, yeah, sure, I will pin you… yeah, yeah, I will pin you when it's ready, and I will remove draft mark from it.
We are…
**Bob Strecansky** 20:40 We are… we're in a dangerous spot right now because Chris is on vacation, and Brett is on maternity leave, so I'm the only person who can approve and merge things right now, so… but I will be happy to help you when I can.
**Sergey Kleyman** 20:51 Yeah, and if you have anything that we can help with, like, if you have anything, kind of, like, that you feel swamped and you would like us to maybe try and get in, because we have some spare capacity, and we wanted to dedicate it to start, kind of, like, taking a bigger role, so if you feel that at the moment we can do something that is, kind of, like, necessary to do now, or we can discuss next time. I think we wanted to stabilize a couple of features, and we wanted to maybe take on some… I remember we discussed it multiple times in the past what would be the biggest contribution may be stabilizing the test, making sure tests are passed, and creating.
**Bob Strecansky** 21:28 Yeah.
**Sergey Kleyman** 21:29 Kind of, maybe the flow that keeps the tests green.
But if you feel there's something that is short-term urgent, then please let me or Pavel know, and both of us on the Slack, and we'll be glad to, you know, to try and help more.
Well…
**Bob Strecansky** 21:45 Yeah, I think that's, like, that should be our priority number one, probably, is getting the test screen on all three repos, but, yeah, I think that takes precedence over probably everything else. I did do a bunch of renovate cleanup this week. I had a couple of PRs open here, but, I may need to… revamped.
**Sergey Kleyman** 22:05 If you would like, we can try and review them, if you think that it might be helpful if somebody else takes a look at, Yeah, I'm… Yes.
**Bob Strecansky** 22:16 See, I have… honestly, what do I have open? I think I have a couple things open.
Oops, that's me… None.
**Sergey Kleyman** 22:24 Is that the issue that, kind of, like, security that was discussed in the past about the big response from the collector?
**Bob Strecansky** 22:31 Yeah, that's the one.
That's, that was… this one.
limit OTLP HTTP response body for me. This is a pretty relatively small change, and it looks like… you know, I didn't even notice… I didn't even notice there were some responses to this, so I'll probably have to pick that back up.
**Sergey Kleyman** 22:49 List of the farewell gift.
By the way, I don't know if, If it's something that, can be used or not. But, technically, we have a mock collector inside the distro tests.
Technically, we can even port them, but I don't know if it will be possible to anyway. So if you want to, I don't know if, do you have a way to simulate this and test the potential, kind of, like, the, the fix on… On a situation when the response is bigger than 4MB? Is that something that you can simulate in the testing framework that we use for SDK?
**Bob Strecansky** 23:27 I'm sure that we can. I haven't tried it yet, but I'm sure that that is something that is… On the horizon for me.
**Sergey Kleyman** 23:35 Right, so… so we can do it either… or we can alternatively add this as a test to distro, and test… I can test your fix in distro and see if it fixes the issue.
**Bob Strecansky** 23:47 That'd be great.
**Sergey Kleyman** 23:48 The only concern might be, let me think about it, like, the way we… the way Distro is constructed, it takes a release version of SDK as part of the dependency. Is it possible to kind of, like, fetch it based on the commit?
**Bob Strecansky** 24:07 We could always do… if we needed to, we could always do a draft.
release. That, like, we could… Make sure that this is tightened up, and then we could do a draft release, and you could use that as your…
**Sergey Kleyman** 24:18 Technically.
**Bob Strecansky** 24:19 It's probably…
**Sergey Kleyman** 24:19 idea to have, to have this ability, right? Because even the… some… some future, we would like to submit maybe some fix, but technically, I have a little bit hard time thinking about the real use case for this, because technically, if we are submitting some fix to SDK, there should be ability to test it as part of SDK, right? We should not kind of, like.
Try and pull it, based on commit into the distro, and then.
**Bob Strecansky** 24:46 Yeah.
**Sergey Kleyman** 24:47 Because if that stays in the distro, that means somebody can break it in SDK again and not know about until the distro runs with that version and discovers the bug, right? So that's.
**Bob Strecansky** 24:57 It's almost like you have to test it in both places individually, right? Like, you have to make sure that it works appropriately in the SDK, and then you have to make sure that it works appropriately in the distro.
**Sergey Kleyman** 25:07 We plan to just run the tests.com with SDK as part of the distro.
But for different reasons, essentially because of the shadow SDK's dependency, and we want to make sure we didn't, negatively affect the functionality of SDK by shifting its namespace into some kind of, like, namespace that will not clash with the application. But, I mean, technically, we always assume that, whatever dependence we pull.
we don't want to duplicate the test, like, according to your suggestion, maybe we will rerun the tests that already come with SDK, right? That makes sense. It doesn't make much sense to duplicate them, you know, like, to create almost the same test, unless it's not possible to test something as part of SDK, then, yeah, we will, we will do it as part of the distro.
But, yeah. So… so, if you have ability… by the way.
is it possible to really test something like that as part of the SDK? Because, essentially, you need something that will act as a mock collector, right?
**Bob Strecansky** 26:14 Yeah, this… I mean, this is… I think this is tough to test, right? Like, you have to… it's almost like you have to do an integration test to be able to test it effectively. There's not, like, a really good unit test that would probably capture all these things effectively.
**Sergey Kleyman** 26:27 In distro, we call those component tests, but…
**Bob Strecansky** 26:30 I'm…
**Sergey Kleyman** 26:30 Like, they are component in the sense that they're not integration in the sense that it doesn't test anything except for the distro.
But it mocks everything around it, and then it uses it kind of, like, on a real application, it kind of runs… I don't know if you can call it real, but it tries to run it, application itself in the distro, not in the context of HP Unit.
So it kind of, like, spawns external, and we plan to also run it in the context of HP FPM, and Apache, kind of, like, get closer to the real-world application. So, essentially.
try to apply the distro on kind of, like, real-world scenario, and then we have the small collector that will accumulate all the data in distro sends.
our SDK inside DistroSense, and and then we test it in PHP unit against the expected, received data.
So, in that sense, it allows, kind of like… because if you stay in PHP unit, if you're limited by that.
it, it limits you what kind of, like, scenarios you can run, right? Because, for example, it's almost impossible to test, like, wave frameworks like that, right? Because you essentially need wave framework to be its own framework. It's hard to run, kind of like Laravel inside each unit, although I understand that, kind of like, Laravel has this special mode.
to run modes of it stuck, to test it inside each period, right? When it, kind of, like, they try to use… to allow running it.
Even though it's inside PHP. But anyways, so, I will, I will take a look at the PR and, and see, and see if I can, maybe add this ability to run the distro on that, it might be also good, and, maybe even add the test, and I can, maybe.
in you and show you that we are with the test, and see if it fails or not.
But, yeah. Okay, I will take a look, no problem.
**Bob Strecansky** 28:23 Sounds like a pin. Alright.
**Sergey Kleyman** 28:25 By the way, what is the expected behavior when you receive something like that? Is it, like, truncating that, or…
**Bob Strecansky** 28:31 Yeah, there's, there's a little bit of documentation, I can find it for you.
**Sergey Kleyman** 28:35 Okay.
**Bob Strecansky** 28:36 Jim.
**Sergey Kleyman** 28:37 I assume there are links coming from that, right?
From the bargain, Yeah, I'm saying I expect that bug that you referenced here at the end, the fixes number.
**Bob Strecansky** 28:50 Yeah.
**Sergey Kleyman** 28:50 I assume it has a pointer to the documentation, like, what to do.
**Bob Strecansky** 28:54 Yes.
**Sergey Kleyman** 28:54 Expected behavior, right?
**Bob Strecansky** 28:56 That's right here.
**Sergey Kleyman** 28:59 Okay.
I will take a look, I will pin you.
When I have the results, but that might be interesting. I myself would be interested how… From how we can run based on committee.
**Bob Strecansky** 29:13 Sounds good. Sounds like a plan. Alright, I gotta run to another meeting. Thanks for meeting today, and we'll see you next week.
**Sergey Kleyman** 29:19 Thank you. Bye.
