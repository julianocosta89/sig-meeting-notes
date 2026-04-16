SIG: PHP SIG
Date: 2026-04-15
Duration: 30 minutes
Zoom Recording URL: https://zoom.us/rec/share/lhpyPymRIBTTBrGNuc_raYWl_Nyix27yjHTSNufOOARXavmdZaynMIxpm0UMCxfT.WrTzgJrVz_4Y6Yiz
============================================================

## Zoom Recording Transcript

**Bob Strecansky** 02:10 Hello, Mr. Life Football.
**Chris Lightfoot-Wild** 02:12 Hey, how you doing?
**Bob Strecansky** 02:15 Doing pretty good, how are you?
**Chris Lightfoot-Wild** 02:17 Alright, thanks, yeah. I thought you were outside for me there, is it? A background?
**Bob Strecansky** 02:21 So, I am at… beautiful Rev Coffee in Smyrna, Georgia. It's a coffee shop that I really like that's, like, kind of on the way to work, and I had to spring my doubles partner, so I delivered it to him. Very nice coffee shop.
**Chris Lightfoot-Wild** 02:41 Awesome.
Amazing blue skies, you're making me miss being over in America.
**Bob Strecansky** 02:48 Well, and this, like, what I'm just finished drinking is also pretty American, too. I drink black coffee, like, 99.9% of the time.
And this place and another place near me are the only places where I get, like.
other coffee drinks that aren't black coffee, and this one, they have a coffee drink here called the Mr. Peanut.
And the Mr. Peanut is a latte that has peanut butter in the latte, which sounds disgusting, but one of my friends was like, no, no, no, you have to try it, you have to try it. I was like, fine, and it is one of my favorite coffee drinks on the planet.
**Chris Lightfoot-Wild** 03:24 It sounds great. I mean, I love, like, Reese's peanut butter cups and stuff, so if it's anything like that.
**Bob Strecansky** 03:29 It's… well, it's not very chocolatey, it's just very.
**Chris Lightfoot-Wild** 03:33 The peanut yourself, just…
**Bob Strecansky** 03:34 Yeah, yeah, it's kind of similar.
**Chris Lightfoot-Wild** 03:37 Excuse me.
**Bob Strecansky** 03:38 Alright, we'll wait a couple more minutes for… is the background noise all right here?
**Chris Lightfoot-Wild** 03:43 Yeah, it's canceled.
**Bob Strecansky** 03:44 My noise-canceling headphones doing their job.
**Chris Lightfoot-Wild** 03:48 Absolutely. Money well spent.
**Bob Strecansky** 03:50 Did I tell you, did I tell you I got a new job at Intuit about a week ago?
**Chris Lightfoot-Wild** 03:56 Yeah, he said you changed teams. Is that going okay?
**Bob Strecansky** 03:59 Yeah. Yeah, everything's good, but I am no longer working in PHP or telemetry or any of it, so…
**Chris Lightfoot-Wild** 04:05 Oh, no.
**Bob Strecansky** 04:06 I'm now working on a Kotlin app, and the React frontend, and a Postgres database, which is much different than MailChimp's.
React and PHP and MySQL, so… Very different.
**Chris Lightfoot-Wild** 04:21 Are you planning on sticking around, then? Like, with the.
**Bob Strecansky** 04:23 Yeah, I definitely am planning on sticking around, because I'm… it doesn't… just because I had to change jobs doesn't change the fact that I'm interested in this.
Arena, and like.
It's… it's not like… I don't feel like I must, but, like, if I left, there'd be really nobody that would be interested in doing any of this work. I wouldn't abandon you like that.
**Chris Lightfoot-Wild** 04:45 Yeah, no.
**Bob Strecansky** 04:48 I really like… I like the PHP SIG, it's like, it's important to me. I think it's good, like, a good career builder thing. It's good to be connected to open source. I've learned a lot, so…
**Chris Lightfoot-Wild** 05:02 So, is… maybe I'm a bit off the market, but is Kotlin, like, a Java derivative? It's like TypeScript to JavaScript kind of thing.
**Bob Strecansky** 05:10 Yeah, it's, I'm… like I said, I'm still learning it a little bit, but it's, Yeah, I think that is a good comparison. Kotlin's often used, as, like, a quote-unquote better version of Java, like, an abstraction layer on top, and then there's, there are frame… like, we're using Spring Boot, which is a framework, sort of like… that would be like Laravel for PHP.
But…
**Chris Lightfoot-Wild** 05:31 I just wondered if there's much crossover, if you end up, you know, learning bits from the JavaSig that, you know, is now more, perhaps.
**Bob Strecansky** 05:37 Cool.
**Chris Lightfoot-Wild** 05:37 your role, then…
**Bob Strecansky** 05:39 There is… there is now a Kotlin sig, too.
**Chris Lightfoot-Wild** 05:43 Oh, okay.
**Bob Strecansky** 05:44 Relatively easy.
Maybe it's just gonna be you and me today, that's very surprising and unusual.
**Chris Lightfoot-Wild** 05:50 Yeah, I think… well, sometimes Paul turns up a few minutes.
**Bob Strecansky** 05:54 Right.
**Chris Lightfoot-Wild** 05:55 kicked off, doesn't he? Just… busy fella, so…
**Bob Strecansky** 05:57 Yeah. But we were… so… I do… we have a couple agenda items to get through today, so let's just get Rick… get rockin' on them.
**Chris Lightfoot-Wild** 06:06 Nice.
**Bob Strecansky** 06:07 Let me share my screen.
Can you see my… you can see my window all right?
**Chris Lightfoot-Wild** 06:17 Yeah, there's…
**Bob Strecansky** 06:18 Okay, so, couple things. That release is almost complete. I went to do the last step of the release, which is publish it to Peckle, and I do not have access to Peckle, and they have replaced Peckle with Pi, so I cannot get access to Peckle. I had to, like, email somebody and hope that it goes through.
And so I've asked… I've asked Brett for help, but I've not yet heard back, so, we will be waiting on that. That is a big gap that I was unaware of, and now we're trying to remediate it, but that's pretty much all I can do at this point.
**Chris Lightfoot-Wild** 06:53 True.
**Bob Strecansky** 06:55 The other one, I opened some PRs this week, and you asked about one being AI-assisted, and so the answer to that is yes, it was AI-assisted, and all of them were… have… all of my PRs lately have been AI-assisted. Intuit is asking us to do this for all of the things that we do, and it's sort of carried over into my open source.
**Chris Lightfoot-Wild** 07:15 No, no worries, I just… it looked like there was some odd… Yeah. Non-humanic stuff going on.
**Bob Strecansky** 07:22 Yeah, so, I think that that is… yes, it is important to call, like, to call that out. Thank you for doing so, and it's important to… I'm glad that you raised that, because I was having an issue, because… whenever you use Claude to create a PR, it usually co-authors the GitHub pull request with you, and then it's very clear and apparent that it is an AI-assisted pull request. However.
for a while, OpenCLA did not allow this, and that's why, I had, like, I had to prompt Claude to say, don't… co-author this, because it would… wouldn't pass the CA. I believe they have fixed this problem now, but that was why, and I should have probably been a little bit more transparent with Adams, and my apologies, but I was like… I was just trying to, use up some tokens before the end of the month.
**Chris Lightfoot-Wild** 08:21 I think… I'd seen on the OpenTelemetry Community repo, there's, like, a Gen AI policy, which we should probably maybe reference in our repos as well.
Just on the back of that, just obviously in case anyone else comes along, tries to open something, and… I think it was the… like, the sentiment behind what I'd seen was, you know, we appreciate that people have these tools available, but sometimes they're in the hands of people that are maybe interested, but not really experts at what they're doing, and they just provide Extra noise for maintainers to, like, have to troll through.
**Bob Strecansky** 09:00 That's true. I've been… I've been… maybe you can help me with this, too, because I've been trying to figure out how to eloquently say this for, like, 2 weeks now.
I think AI-assisted development is okay, and I think it can really help get over some hurdles and break through some stopgaps or whatever, but when you have AI planning, AI coding.
AI pull request reviews, AI merge queue help, AI-assisted Test Writing.
**Chris Lightfoot-Wild** 09:28 Yeah.
**Bob Strecansky** 09:29 That's… it was, like, very… our CEO called it this in a meeting recently, and I had never heard this before. There was no HI, human interaction. That's when I think you get into a spot where you're ripe for failure.
And, like, it compounds on itself, too, because you have individual contributors that write code, and then do not understand how the code works. Like, that is a tale as old as time in computer science, but now they really don't know, because they didn't even really attempt to write it. It's just, like.
don't want to use the word slop, because that's sort of a derogatory term, but it is.
Way too AI-assisted.
**Chris Lightfoot-Wild** 10:14 Yeah, absolutely. I agree. I don't know how to summarize that any better than what you've done there with the.
**Bob Strecansky** 10:20 Hey, Joy.
**Chris Lightfoot-Wild** 10:20 thing, I've not heard of that term, so that's… that's… Points.
**Bob Strecansky** 10:23 Yeah, and so there, there also is a discussion now about, different levels of AI reliance. There's, like, a scale… I'll have to find it. There's, like, a scale from 1 to 10, where 1 is developer thinks about using AI and goes, I don't want to. And then 10 is completely developed by AI. And I think this is being used in industry a little bit here and there to, like, really eloquently state how much AI interaction there is. I probably need to learn a little bit more.
But that's something to consider.
**Chris Lightfoot-Wild** 10:58 It would probably be nice, wouldn't it, to put it on our repos to say about what the policy is as the OpenTelemetry community as a whole, because… I guess we do want contributors, but we don't want… contributors that only use AI don't understand it, and then it's like a drive-by contribution, they just want to get the name in there, and then…
**Bob Strecansky** 11:16 Yeah, I bet.
I have a strong feeling, Chris, that we will see that more and more. And I don't… I don't know the right answer to that right now, but I think… and I think we'll have to visit that as it comes, because, like.
if you open a pull… it's also, like, it feels like it's insanely subjective, too, right? Like, if you opened a pull request that you completely wrote with AI and didn't even read and just submitted, because I have a good rapport with you, I'd be like, oh, Chris had really good intentions here. But if… Somebody from a different country, or a different location, or a different… something else.
a different internet presence. Open the same pull request, I might be a little bit more skeptical of said pull request.
And it doesn't knock them or you, it's just, like, that's kind of how it works.
And I don't… I don't have a good solution for it, but… I did also notice that we do have available to us, co-pilot reviews.
In GitHub, I have used those, and I will continue to use those, because I think that, as we see pull requests come in, there is no negative to doing that, except for the cognitive overhead of clicking the button and reading the review.
I think it sometimes can give valuable insight. So I am planning, as a reviewer, to continue to do so, but, Yeah, I just… I think that's important to talk about, too.
Speaking of, did you ever get… hear back about your approver status?
**Chris Lightfoot-Wild** 12:48 Someone commented on the thread linking to a PR in, like, an admin repo, but I can't see that repo, so obviously maybe the ball's rolling, or maybe there's a discussion there that I'm just unaware of, or something.
**Bob Strecansky** 13:01 Let's see, let's see, let's see.
**Chris Lightfoot-Wild** 13:07 That was the one… the fourth one down?
**Bob Strecansky** 13:10 this one.
I don't know if you guys today.
**Chris Lightfoot-Wild** 13:14 Oh, sorry, no.
Sorry, sorry, that's not me. Those ones you've made. It was in the community.
**Bob Strecansky** 13:20 Yeah, I'll just go to the refill.
Sorry, the Zoom overlays.
**Chris Lightfoot-Wild** 13:25 I thought that ended up looking very, very similar to the wording I'd used, but…
**Bob Strecansky** 13:34 Let's see, I go to issues…
**Chris Lightfoot-Wild** 13:43 Oh, that is, about 1 to 6, 6 or 7 down.
Repository, one only, that's it.
**Bob Strecansky** 13:49 Oh, goodness.
**Chris Lightfoot-Wild** 13:50 You're at 3, 3, 6, 0. Don, one more.
**Bob Strecansky** 13:57 I agree.
**Chris Lightfoot-Wild** 13:58 But yeah, I can't see that repo, so I wasn't sure what was…
**Bob Strecansky** 14:01 I ca- I can.
**Chris Lightfoot-Wild** 14:04 Nice.
**Bob Strecansky** 14:05 Congratulations! You've been approved.
**Chris Lightfoot-Wild** 14:10 Well, one thing I didn't realize, I didn't want to complicate it further, but, like, I guess, looking at the Java, and they also look to potentially have contribut provers as well.
But they're a bigger SIG than us, aren't they, from what I understand? So, like… Maybe we could evolve in future if there's more of us.
**Bob Strecansky** 14:29 Okay, so, again, I'll… I'll say this.
I think you have… I mean, you've proven yourself over and over again. You could absolutely be a maintainer, too, if you wanted to be. I don't know if you want that responsibility, but you have proven yourself with pull requests and unique contributions and attendance and all the things that make for Being a maintainer, but if you don't want that responsibility, then you can…
**Chris Lightfoot-Wild** 14:52 Maybe one day down the line, I feel, you know, working up to it.
**Bob Strecansky** 14:56 Yeah, totally.
**Chris Lightfoot-Wild** 14:57 Yeah, thank you.
They've also had some interesting things in there, just poking around. They've got, like, in some of the SIGs where they do a subtree split, and they've got, you know, in contrary, several components.
They've got a workflow where it, sort of, based on the path that's been changed in the PR, tries to identify what contributors it should maybe ping as, kind of.
Kodo.
**Bob Strecansky** 15:21 Yeah, yeah, do you, do y'all use that at work? We use that extremely heavily. There is, you can apply a code owner's file in the .github, like, in the .
**Chris Lightfoot-Wild** 15:34 Yeah, the route already, yeah, it looked like there was some additional stuff going on, though, in that other workflow as well.
**Bob Strecansky** 15:40 Well, if you're doing a git split, or, like, git subtree kind of situation, you probably can do separate code owners for those specific splits, but we definitely don't need that right now. I think that… I do think… I do see the inherent value of potentially having code owners for different, parts of Contrib, just because, like, dealing with con… Sorry, I shouldn't say dealer.
negotiating with all of the contrib members can be difficult, right? Like, I work at IBM, I create the Insana PHP instrumentation, and then, like you said, sort of like with AI, I think it was, like, uses, like, I'm not interested in attending the SIG meetings, I'm not interested in what AWS is doing for their part, I'm not interested in the API, I'm not interested in instrumentation, I just care about the instrumentation for my particular flavor of telemetry. And that's… that's fine, like, that is the success criteria, right? Like, if companies and ICs are interested in Instrumenting their own part of… So, like, in their own part and contribute, that's great, but what we have to remember is, like, it is best effort for us, and, like, all of the GC and the TC have accentuated that very, very frequently, right? Like, as maintainers, we care mostly about the API and the SDK.
Because that's what our main focus is. Like, if we need to help with contrived stuff for whatever reason, fine, but we have to make our best moral judgment about how to best steer the sick, and that's often not Dealing with contribib baloney.
**Chris Lightfoot-Wild** 17:21 Yeah, no, that makes sense.
**Bob Strecansky** 17:25 Okay, all right, was there any other… oh, so let's, let's go walk the board real quick, and then we can spend a little bit of time doing our, creating our board, because I know we talked about doing that today.
**Chris Lightfoot-Wild** 17:38 Yeah, I mean, happy to defer that to another time if you want, like, given it's just the two of us, unless.
**Bob Strecansky** 17:44 Yeah, maybe it makes sense to do that. I mean, I feel like that's one of those things we're just gonna defer over and over again until we actually do it, but I agree, two people is not enough.
**Chris Lightfoot-Wild** 17:52 I just… I just obviously wondered if, like, the Arctic guys, given they're, like, building out the distro, they… they would have some kind of roadmap or not as well for that?
**Bob Strecansky** 18:01 Yeah.
**Chris Lightfoot-Wild** 18:01 And that warrants a project board or not.
**Bob Strecansky** 18:04 Agreed.
**Chris Lightfoot-Wild** 18:05 Oh, it's a different sort of setup, though, isn't it? Because they're doing it, like, sponsored, essentially, under company time.
And we're just here as, like, you know, independent contributors, so…
**Bob Strecansky** 18:13 It's almost like they need their own… I don't want to be… I don't want to be that, that segmented, or that, like, Locked, but it's almost like they should have a separate board for the distro work.
**Chris Lightfoot-Wild** 18:26 Yeah. I mean, they probably do. They probably already have it in their… mapped out in their mind.
**Bob Strecansky** 18:30 Yeah, it's on, elastic.jira.com or something like that.
**Chris Lightfoot-Wild** 18:35 Okay.
**Bob Strecansky** 18:37 These are all… Okay, so these are mostly… I have to go through and do all the, renovate… I have to merge all these renovate things again, but, I think I have 3 open in here.
for BotMD, PHPT, and… And what are you here?
Yeah, just those two.
Why do you keep opening? Stop it.
Ugh, sorry.
So, yeah, this one is just a CloudMD… oh, there's, conflicts for that one, and then this one is just adding… this was using… Applied to add a bunch of PHPT tests to improve our test coverage for instrumentation.
So.
**Chris Lightfoot-Wild** 19:29 Trying to look through some of these.
**Bob Strecansky** 19:31 Yeah, no, zero hurry. I'm just trying to, And see what I have. Same thing with this one, I added a quad in the unit test coverage here, and then in OpenTelemetry PHP. This is that one that we were talking about with, response body to 4 megs.
And… increased test coverage and a lot of these, so… I think… I think you reviewed this one already, and then I… accepted your view, and then I need you to click.
**Chris Lightfoot-Wild** 20:03 Oh, sorry, I need to re-review, sorry.
**Bob Strecansky** 20:05 I'll, I'll put this in, chat so you can approve it real quick and, like, merge it so we don't have to… I don't have to think about other people.
**Chris Lightfoot-Wild** 20:13 Yep, and what was I heard about?
Nope.
**Bob Strecansky** 20:41 Thank you much.
Yeah.
Oh, I didn't realize that you had your own domain.
**Chris Lightfoot-Wild** 20:49 Huh?
**Bob Strecansky** 20:50 Wild.meeted.
I didn't know me.uk was a TLD.
**Chris Lightfoot-Wild** 20:56 Yeah.
**Bob Strecansky** 20:57 to the floor.
Yes, I guess, why would I know that?
**Chris Lightfoot-Wild** 21:03 I was just wild before I married, and my… I got… me and my wife.
Lights slash wild, combined.
**Bob Strecansky** 21:12 Yeah, did you… have you, speaking of internet TLDs, have you, read Tim Berners-Lee's book yet?
**Chris Lightfoot-Wild** 21:21 No?
**Bob Strecansky** 21:24 He put out this book, The Story… The Unfished Story of the World Wide Web. I've been listening to it on audiobook. It has been a very good book if you're… if you need a new good thing to listen to.
Like, the history… the history of how the internet started.
**Chris Lightfoot-Wild** 21:40 Is it, worthy listen slash read?
**Bob Strecansky** 21:43 I've… yeah, so I've been listening to it on audiobook, and I don't think it would translate well to… I think it would be, like, a very boring reading book, but it's… it's been a very good, like, in-the-car, driving audiobook, so…
**Chris Lightfoot-Wild** 21:57 I'll try and have a check out, thank you.
**Bob Strecansky** 22:00 Okay, and then… I don't think… I don't think we've had any other really big contributions or issues this, let me…
**Chris Lightfoot-Wild** 22:10 I did get tagged on, the Laravel, PR from the other week that we did merge, and I said, oh, it'll be released soon. Is that… Oh, yeah. Are you doing that on the back, or trying to get the instrumentation out first?
**Bob Strecansky** 22:22 Yeah, I was planning on… I don't want to get into a state where we have, like, split releases, so I will… hopefully Brett will respond today, when it's… when he's alive.
Because he's probably asleep now.
**Chris Lightfoot-Wild** 22:34 It's like a different… so you're thinking when you do a release, you'll do, like… everything at once, almost, like API, SDK, instrumentation, That's all true.
**Bob Strecansky** 22:44 That's what… that's my hope for now. I think, at least for me, that seems like a good… a good split, but I'm… I'm very open to releasing them separately if we decide that we want to, but I… whatever, I don't really have a strong opinion.
**Chris Lightfoot-Wild** 22:58 My only thought process, I guess, is, like, should we have some sort of, workflows first? You know, should… do other things… Are they more automated in a fashion?
**Bob Strecansky** 23:09 Oh, yeah, for sure.
I was in.
**Chris Lightfoot-Wild** 23:12 Just a case of, you know, having to put effort in to build out the flows and things like that.
**Bob Strecansky** 23:17 Yeah, I mean, this is our… this is the release management for OpenTelemetry PHP, and it is very, very, it's very manual. It's a very manual process, and I would love to make it a more automated process, but… What's that? XJCB?
**Chris Lightfoot-Wild** 23:32 I'm not… sorry, it was not complete, it was totally, you know…
**Bob Strecansky** 23:36 No, I think… I think it… have you seen this before? Is it worth the time? Like, this is… this is 100% what.
**Chris Lightfoot-Wild** 23:43 What that…
**Bob Strecansky** 23:44 We release once every month or less, so… Is it worth it? Probably. Should we make a ticket about it? More than likely. Is it gonna happen?
At some point, at some point.
**Chris Lightfoot-Wild** 23:58 No, we've done so far without it, so we're fine, right?
**Bob Strecansky** 24:01 Yeah, I think that that's it.
Okay… Stats… 35 million… 34 million installs.
**Chris Lightfoot-Wild** 24:11 I mean, you are our bus factor of 1 at the moment, so hopefully, obviously, Brett's, you know, planning to come back to us.
**Bob Strecansky** 24:18 Yeah, he… I mean, his… their paternity leave is insane. It's like a year. So… She's just, like.
as I understand it, he's just, like, sabbatical-ing, more or less. Not… obviously not sabbatical-ing, because kids take a lot of time and energy, but, like, he's disconnected.
**Chris Lightfoot-Wild** 24:36 Yeah, the most time.
**Bob Strecansky** 24:37 Yeah. I'm so jealous, because we get… I mean, we get a ton at 12 weeks. Like, that is best in class for Intuit, and that still didn't feel, like, nearly long enough.
Anywho. Alright, what else? Anything else on your mind?
**Chris Lightfoot-Wild** 24:57 No, I don't think so, just the usual, usual stuff, I was trying to test something that, Nevey had quoted on PR, but just not found the time yet, so… which, Yeah, it's hopefully the library stuff. Just, I'm obviously conscious that the longer I leave it as well, and it's been ages already.
**Bob Strecansky** 25:16 Yeah.
**Chris Lightfoot-Wild** 25:17 The more work kind of comes in, and people are… coming up with ideas and just contributing them in and going, I've done this thing, and then, like, can we merge it? I want to use it. And it's, it's difficult when that's, like, out of the blue.
I don't know if maybe… I don't know how we try and convince people to… like, obviously, some people, if they've got an idea, they can just PR it, and it's fine.
But it's nice to sometimes know what the idea might be up front as well.
So it's like…
**Bob Strecansky** 25:43 I do… I do feel like that, like, that is part of a meta-discussion that I would like to have with more people in the SIG at some point in the future, is like.
We need to come up with a better way to reduce… we need to come up with some ways to reduce friction for contribution in this repo. I feel like the friction is… I'm gonna take a couple quick notes here about where I think we have… friction.
How do we… How do we reduce hotel PHP?
attribution friction.
So it's, get CI green… Look… Let's see… Figure, figure… Way to triage issues more quickly.
lease process… more automated… Work through project boards.
So people can understand.
Where we are… I guess it would also be, like, Continuous… contingencies labels…
**Chris Lightfoot-Wild** 27:05 I improved label usage.
**Bob Strecansky** 27:09 Yeah, I don't want it.
Alright, good. If you… more involved.
PHP is, and .php plus 4… What else?
**Chris Lightfoot-Wild** 27:35 Well, even some of the stuff, like, for the Laravel, thing for contributing, like, version 13, Someone had opened the issue on the subtree split repo, and I guess that kind of went unchecked.
But I think you could… we could probably put workflows in that, you know, the automatic closing of PRs and things like that, and refers to the main place. I know it's in the… It's kind of an RTFM thing, but, you know.
**Bob Strecansky** 28:04 Yeah.
**Chris Lightfoot-Wild** 28:05 still do it. So, and I don't have permission to just even close those issues. I don't know if you have permission, or who owns that.
**Bob Strecansky** 28:13 Do you… do you not now?
**Chris Lightfoot-Wild** 28:15 No, because it's a Oak, so it's.
**Bob Strecansky** 28:18 Oh, yes, okay.
**Chris Lightfoot-Wild** 28:19 Yeah, I think maybe you and Brett, potentially, on that one?
**Bob Strecansky** 28:23 Yeah, I can… I know I can close this.
Oh, I have… I think I have pretty close to full admin, or at least I can get it with the just-in-time thing, if we need to do stuff.
I know it used to be they would just give… full admin permissions to all the maintainers, and I know they are… they were working on doing, like, more fine-grained commissions, which I'm okay with, it's just…
**Chris Lightfoot-Wild** 28:48 Yeah, absolutely.
**Bob Strecansky** 28:48 IAM is one of the most… I always joke that I'm going to quit tech either from IAM or AI.
And… so, yeah. Okay. Yeah, I think this is a… this is a good starting point of the things where I feel like we could reduce friction.
But… I'll put… I'll, I'll post this in… Our channel, too.
**Chris Lightfoot-Wild** 29:14 Yeah, that's good, yeah.
Yes, ultimately, there's people lurking as well, isn't there? It'd be nice to get more of them out of the woodwork, and…
**Bob Strecansky** 29:22 Yeah.
**Chris Lightfoot-Wild** 29:22 Interested in helping in some way.
**Bob Strecansky** 29:29 PHP SIG meeting today. How do we reduce total PHP contribution friction?
Here were a couple of ideas we had.
Would love info.
the greater… Did she luminous.
What else are you?
Cool.
Alright.
**Chris Lightfoot-Wild** 30:10 More ideas in from the wider community.
**Bob Strecansky** 30:14 Whoa.
That's all from me.
**Chris Lightfoot-Wild** 30:19 Yeah, me too. Well, enjoy the rest of your coffee trip visit, and have a good day.
**Bob Strecansky** 30:25 I will, we'll catch you later.
**Chris Lightfoot-Wild** 30:27 Cheers, hello, bye-bye.
