SIG: Swift SIG
Date: 2026-11-12
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Marius Ciocanel** 01:49 Hey, Ben.
How's it going? Hey, this one.
**Vishwan aranha** 01:53 Hey guys.
**Ben Joseph** 01:54 Good, how are you?
**Marius Ciocanel** 01:56 Yeah, yeah, alright, I guess.
Just have a lot of stuff, like, we've, we're gonna be moving house, so, like.
Between putting the house on the market and making a move, it's…
**Ben Joseph** 02:09 That's… that.
**Marius Ciocanel** 02:10 Yeah.
**Ben Joseph** 02:11 I hate moldings.
**Marius Ciocanel** 02:14 Yeah, I mean, last time we did this was 6 years ago, so… You know, hopefully we don't do it very often, because, yeah, it's… It's a pain, it's just a lot of time, a lot of money spent just to move from place to place.
**Nacho Bonafonte** 02:32 I'm a burning.
**Ben Joseph** 02:33 Hi, Nacho.
**Marius Ciocanel** 02:34 Ain't Nacho.
Hey, Vladimir.
**Nacho Bonafonte** 02:44 Yeah, where?
Probably all of us today, Billy told me he's not joining.
But, yeah, so… the usual suspects are all here, so I think we can… Maybe a start already?
Yeah, there are some.
Interesting.
Wow.
advances in Campier, so… I don't know if you have already added the… Topics, if you want or not.
And so, yeah, topics from last week… We… we talked about the, launch instrumentation, project from Bini.
With, with, with this PR, I don't know if you have been able to take a look on this. Anyone?
But, yeah, it's… it's looking good, I think he still needs to do more testing, just co-pilot.
ransom.
some… some reviews there that I think he already addressed.
I don't know, they have changed the way.
the PSR zone on GitHub.
which… Yeah, it's…
**Marius Ciocanel** 04:17 Yeah, I think they reversed the order, so the latest thing is at the top.
**Nacho Bonafonte** 04:22 Yeah, so it's a bit difficult to just readapt. I have been trying during this week, but probably I'm missing something.
Yeah, because it keeps the summary here and the comments so opposite. So, Billy added some things here, I don't know if he addressed Many things, but yeah, there is still some.
some, that's failing.
So yeah, he's still working on that.
Yeah, if you can take a look, it's… It's quite… quite interesting.
And yeah, probably you can also add… value there.
While it's in development.
Also, the RR web thing that… Yeah.
Billy mentioned last week, I don't know if…
**Marius Ciocanel** 05:11 a session replay, Ben? I know you mentioned something about it.
**Nacho Bonafonte** 05:16 Yes, it was about that, yes.
about, yeah, an external project I was interested in knowing.
About this.
From some use cases, but yeah, I think it was… Hundled, later privately.
And also, we have the iOS-specific docs, which this is the… Yes, okay, yeah.
**Marius Ciocanel** 05:44 I was hoping I would get to this, but it's just not a hard time this week.
**Nacho Bonafonte** 05:47 Okay. Okay. Yeah.
**Marius Ciocanel** 05:49 Yeah, I'll… yeah, if I get to it, yeah, I'll tag everyone.
But yeah, not hot enough for this.
**Nacho Bonafonte** 05:57 Okay, yeah, I… Don't think we are in a rush for this, to be honest, because there is other documentation, but yeah, it will be great to have as soon as possible, so yeah.
A… So, new, new topics. Then, we have this merge… Jeez…
**Marius Ciocanel** 06:21 So, this is the Weaver update, that we kind of had it open last week as well, made some changes based on what we've discussed.
Yep. Where we can hold a generate script, or, I guess, major releases when we can afford to… Have breaking changes, but also… We can call them on minor versions as well.
I think, yeah, there was some feedback, that I've addressed, and… I think this could go in, as it is, and then I'll… Follow it up with, another PR that actually brings us to the latest version of the semantic,
**Nacho Bonafonte** 07:08 Yeah, yeah, perfect.
Yeah, it looks good.
Yeah, I think it has been approved by… by… yeah.
Three of us now, so, I think it's… Good to go.
Yeah, brilliant. Yeah, so that…
**Marius Ciocanel** 07:31 whip.
**Nacho Bonafonte** 07:32 About why not adding the new version, but that's another PRG. I think there.
**Marius Ciocanel** 07:36 That will probably add tens of file changes that.
**Nacho Bonafonte** 07:41 Yeah, yeah, that's right, yeah.
**Marius Ciocanel** 07:42 I just hide it,
**Nacho Bonafonte** 07:45 Yeah, totally. It allows, yeah, it allows Kukushin much better.
So yeah, I think it's already, MMO… Yeah, probably I'm removing all the description.
**Marius Ciocanel** 08:26 Yeah, I think it's all in the title. Mainly in the title, anyway.
**Nacho Bonafonte** 08:36 Okay, great, so we now have support for the newer…
**Marius Ciocanel** 08:40 Yeah, all of… I can pick up the… I guess the next PR, where we bring, library to the latest version.
I think it's one…
**Nacho Bonafonte** 08:51 that.
**Marius Ciocanel** 08:51 0.45.
**Nacho Bonafonte** 08:53 Okay, we can break.
**Marius Ciocanel** 08:54 I'll do the next one, yeah.
**Nacho Bonafonte** 08:55 Oh, names, yeah, that's right.
Great.
Okay.
Then… Yeah, let's go… these are the new topics that are here. So I think we can go to the rest of the topics.
That there are… that… During the project.
I think some new issues were created by, Vladimir.
I don't know if you want… To talk about them, or…
**Vladimir Kukushkin (Apple)** 09:28 I can, but yeah, so the idea, just to continue. I have some time allocated to go through the open turn to Swift to point out any anything that's worse.
changing or fixing related to the accessibility API bridges, and yeah, this is one of them.
So the idea is we want to be able to correlate between the… Tracing, whatever.
logs, for example. Logs is the most important thing, so we need to be able to get the span ID.
out of there.
out of the tracer, and there's a pattern for that. We call it the metadata provider that checks the task local.
**Nacho Bonafonte** 10:14 Okay.
**Vladimir Kukushkin (Apple)** 10:15 Service context, aka instrumentation context now.
And it's just not available.
So you can't… send logs with the… if you happen to have logs going to a different place, not handled by the OpenTelemetry SDK, not handled by something else, you can't correlate them with the same ID that is used by OpenTelemetry. That's not… not very important, but this is one of the expectations observability AI users have. You should be able to do that.
So, I would expect To pick it up, from the community.
**Nacho Bonafonte** 10:52 Okay.
Yeah, yeah, what you're asking here is just reading the values, or writing them?
**Vladimir Kukushkin (Apple)** 11:02 Breezing.
**Nacho Bonafonte** 11:03 Reading. Yeah, I think… yeah, okay, I think that… reading, reading.
I'm not sure the spec is… wants it, but yeah, definitely being readded, I don't think it harms anything.
Writing will be a different topic, probably.
**Vladimir Kukushkin (Apple)** 11:24 Right, yeah, yeah, writing, absolutely.
**Nacho Bonafonte** 11:27 So, yeah, I think that's… that's… that… Yeah, I think I've been reading, to these values, If it's useful, yeah, that should be made. At least the… Setting a private set, probably, on the values.
Or something like that, so they can be read. Or just a getter.
**Vladimir Kukushkin (Apple)** 11:49 Just together, yeah.
Let's good that.
**Nacho Bonafonte** 12:04 Okay.
**Vladimir Kukushkin (Apple)** 12:08 Thank you.
**Nacho Bonafonte** 12:13 Yes, as a note portal.
Someone who wants.
**Vladimir Kukushkin (Apple)** 12:16 That's a great comment. Thank you.
**Nacho Bonafonte** 12:19 Okay, great. And yeah, I see you…
**Vladimir Kukushkin (Apple)** 12:22 So create a second one… yeah, these, I think this is… This looks like just the bug.
So… Yes, for those who haven't seen the distributed tracing APIs, this is how you can… Scope something with a span, and then there is a span, and you can modify the span attributes.
Adding attributes, setting attributes works. Removing attributes is not propagated to the OpenTelemetry exporter.
Again, not a very, not a very popular case.
But nevertheless…
**Nacho Bonafonte** 13:03 Yeah, yeah, that's… I don't think there is many people removing antibodies, but yeah, that's true.
**Vladimir Kukushkin (Apple)** 13:08 Yeah, yeah.
**Nacho Bonafonte** 13:09 be, supported. Yeah, that, that's,
**Vladimir Kukushkin (Apple)** 13:12 Yeah.
**Nacho Bonafonte** 13:12 A nice, and probably can be also a good first issue.
**Vladimir Kukushkin (Apple)** 13:19 If you say so.
**Nacho Bonafonte** 13:21 Probably… Yeah, that's something just to… locate where that's not being done. I think it's… Earlier.
And you see… It should be easy, unless, you know, you never know, right? Yeah, yeah. You start to dig, but yeah, it should be, yeah, great.
Great, thanks, thanks for… for that.
**Vladimir Kukushkin (Apple)** 13:42 Yeah, and as I'm speaking, the CLA signing for me is still not being approved. It's not like… it's not approved, because reasons it's not approved because.
**Nacho Bonafonte** 13:54 Okay.
**Vladimir Kukushkin (Apple)** 13:55 process is slow. Okay. So I apologize for that. I wish it as much as it is.
**Nacho Bonafonte** 13:59 Okay, no worries.
**Vladimir Kukushkin (Apple)** 14:01 It's… yeah.
It's been working a couple of PRs in…
**Nacho Bonafonte** 14:06 Yeah, okay, I can… that's totally understandable. You know, companies have their rules, have their, you know.
So… Yeah, the only thing will be, just… going back to those, PRs and trying to revert.
Adopting your, your comments, and that should be enough.
Yeah.
Also, if you create some… Yeah, you've… Yeah, for the filter, I mean, You know that you cannot create content, right?
**Vladimir Kukushkin (Apple)** 14:41 Yeah, yeah, yeah, yeah. Yeah, this also blocks me. I want to update the READMEs for the bridges, all three of them, because they have a very, very small place. The log bridge has, but metrics and tracing, they don't really have.
**Nacho Bonafonte** 14:55 Okay.
**Vladimir Kukushkin (Apple)** 14:56 rooms. I won't update those, but I can't.
**Nacho Bonafonte** 15:00 I've…
**Vladimir Kukushkin (Apple)** 15:01 Anyway…
**Nacho Bonafonte** 15:02 Yeah, I don't know how we could do that.
**Marius Ciocanel** 15:05 And you can create the issue and say, this region should really say, da-da-da, and someone can just take it and paste it like this?
**Vladimir Kukushkin (Apple)** 15:13 I'm considering this. If the promo thing doesn't happen until, I don't know, Thanksgiving, something like that, then this would be my option.
**Nacho Bonafonte** 15:23 Okay, okay, yeah, I mean, yeah.
No, no worries. You can do that. Clearly, yeah, we can, we can follow, how it's needed, yeah.
Thanks. Thanks, brother.
Okay.
So for the rest, we have pull requests.
Also, yeah, it looks… we still have many of the, tomarimi, PRs, but he has updated one of them, that it was about documentation, and It has been approved.
by this one, so I melts it.
So… He's still updating things, which is nice, but probably all of these are still… I don't… I have not checked if he has done More.
lately today, because I usually check the project Very early in my morning.
Which is, like, yeah, 10 hours ago. So I don't know if more changes have happened, but yeah, it still has some… Conflicts and issues in the rest of the Yes, but he shows that he's still alive, so… Probably that will… Not… Will… will happen in… Not… not very long period.
So, for the RECS… For the rear rest, we have… Yeah, this one is the… the… Vladimir approval.
We have something for MetricKit. I added some feedback there. We have, meetings PR… And we have the packet straight. So that's another one that we will… Track later. Because, yeah, I want to have clarity on how to handle that. So this is about the metric kit.
I asked some documentation, he also asked why… He's… fixing it to Compiler 6.4, which I think it's a bit too high, but I don't know if there is something. So that's why I asked if there is something that needs that version specifically.
because… I don't know, but I will be a bit surprised that it's not about the iOS version, but the Swift version is a bit surprising for that, but yeah, maybe there is something. But his still on Draft.
I don't know if you have reviewed it.
Yeah, it's… it looks… In general, good.
You can take a look, that would be great. But yeah, he has not moved much lately on this player.
Here we have… The package trades, yes, T1.
So he created the PR and changed lots of files.
I suspected, right? That that's… That's part of this. So, yeah, I tried this.
just downloading this package and trying here, and the thing is that when you open the project in Xcode, you just run the basic So the… the… not all trades, right? Just the no trades at all. And that was a bit my, My comment here?
Is that for the OpenTelemetry Swift developers?
if you open the package in Xcode, how do you enable all the trades? So when you change code, you are running all the tests and not breaking things on other libraries? That was my main concern, yeah.
vladimir said that this is the correct pattern, which I agree, but maybe there is… something we should do, maybe some file, some Xcode file, or something that Justice that is thread when you are doing for development?
So people don't forget about that, and run everything on locally, instead of just on the CI.
Any idea here?
**Marius Ciocanel** 19:56 Yeah, I've now looked at this one.
No.
No feedback.
**Nacho Bonafonte** 20:01 Yeah, the thing is that, yeah.
I don't know if I am, the thing is, you add the project, like, add in the trades when you import the project in the package, right? So you import the package and add here the trades, right? It will be… the URL, it will be open history from 3.
OTLP gRP6, so basically it will import the base… Classes?
Plus the… plus this product from the… from the package.
But when you open the package, by default.
It just opens without those traits.
Which means that How do you open that in… you know, for development, and adapt all those traits, right? You are not importing, you are just opening the project.
Can that be… change somehow, or create some Xcode file there that… like, like an XC config file or something like that, that can put that value when you open in Xcode.
Because if not, how do you… you know, I mean, you are probably using Linux, so… probably not using… I don't know if you use Xcode or not, but… You know, if you are developing here, and you are doing some changes, you need everything, and the project is, you know, we are not updating Xcode project.
Anyone has any idea how… Could that be done?
**Vladimir Kukushkin (Apple)** 21:41 For an individual developer environment, you open your project in an Axe code, and you can configure the environment variables in the targets.
But that's gonna be for your local… Perfect How can it be done so this configuration is also shipped with the… Yes, with the package.
**Nacho Bonafonte** 22:05 Because if I don't load that to another branch… I would like to, you know, don't have to change that, or anyone who develops.
Okay.
**Vladimir Kukushkin (Apple)** 22:16 Yeah, so, the alternative would be that… The whole set of traits is the default.
And then the, the, the feature… Yep. Switches is opt-in to remove unnecessary stuff.
**Nacho Bonafonte** 22:33 Yes, that's what I… more or less what I said in my comment. Yeah.
**Vladimir Kukushkin (Apple)** 22:37 Yep.
**Nacho Bonafonte** 22:38 Yeah, that's… Yeah, I don't know. But it's, it's… Yeah, maybe I'm thinking very, you know, very laterally here. It's not the usage, because it's for importing, but for the day-to-day development, I think it If we can't find a solution, it would be great.
okay, maybe we need to do some research here.
**Marius Ciocanel** 23:04 I mean, we can always, once we figure out how we can do this, we can always document it for people to know what to do, because I think the research part of figuring out how we're going to do this It's tricky, yeah.
I'm not sure what the answer is.
**Nacho Bonafonte** 23:25 Yeah, probably something like an execonf file there in the project.
If that can be configured to be…
**Vladimir Kukushkin (Apple)** 23:34 Yeah, I'll take an action point at the last round, Next code.
and SwissPM people, what would they recommend? Because it seems like, again, not a very popular use case, but a legit use case. You have a package of trades, and you want to help with the development. How do you do it in Xcode?
Yeah, I was cramped.
**Nacho Bonafonte** 23:59 Yeah, great, great, thanks.
Yeah, just, just for, for helping, when, yeah, opening the project. Not, not important, but that's sort of, that's clear, but yeah.
Maybe if someone wants to help and just, you know, change something or address appears, and your failure happens on the CI, Or having to download a project from a third, you know, use… I download a branch from another developer to review it.
And… and I have to change again every time the… the… you know, if we can fix that, it will be great. If not, okay, we will live with it.
But yeah, I… would like to have that a bit improved, because that's the only usage I do for the project, right?
I don't use it externally.
No. Okay. Great. Thanks, thanks for that, Vladimir.
Okay, and the latest… Appear here.
It's another… Version?
changes, that it was already approved, so I can imagine that And merge this.
Okay, so that… those are all the PRs that… Are still in the works.
And on the issues.
So… Yeah, anyone has any other… Topic, problem, issue, comment to have?
If not, we can just drop it here.
**Vishwan aranha** 25:43 I just have one question, like, when are we planning to do the next release?
**Nacho Bonafonte** 25:51 Yeah, whenever we want, right?
**Vishwan aranha** 25:58 I know there's holidays coming, so just wanted to…
**Nacho Bonafonte** 26:01 Yeah, it will be great having it be for Santa, right?
Oh,
**Marius Ciocanel** 26:08 I can push this PR with the semantic, conventions, and after that, I guess, whenever you want.
**Nacho Bonafonte** 26:16 That's… that's a good one.
If we could have this, I think if we could have, this… sorry, I… I missed the name. The one that we talk now, sorry. The…
**Marius Ciocanel** 26:36 traits.
**Nacho Bonafonte** 26:37 Yeah, trades, sorry, yeah.
If we can have the trades resolved for 3… 0.0, that will be… Perfect. Maybe we can also merge like this, right? Because it's just a development program that we can fix in the next time. We just… We, we can… Maybe fix that with a small commit.
I hope.
But yeah, I would like to have a… I would like to have the trades problem solved.
So every… anyone can use version 3 with the minimum.
features or problems, or, or dependencies downloaded. Because as we are dropping, the switch telemetry code.
of internal restrictive car, we… we… we can't have the same Kind of usage for the users.
Of that packaging, that would be great.
So, yeah, I think those, those two things are… are… should be, mandatory before a 3.0 release?
But, I mean, if you don't agree, we can. I mean, it's not a decision to be made only for… by me, so if you have any other… Opinion, or you want any other thing to come in before that version?
Yeah, raise your hand, say hello.
**Marius Ciocanel** 27:59 Do we want to timebox this as well, to say, you know, like, aim for… to have these things, see if we can get them merged in the next, like, 2 weeks or so, or, like, before December, and then, say, the first week of December, we can do a release.
Or we can decide the week before?
If we have everything we need.
**Nacho Bonafonte** 28:27 Yeah, I think… Yeah, I think a two-week, so having that Before December will be great.
It will give time to people.
Before going Christmas to… To maybe test it, or think about.
you know.
**Marius Ciocanel** 28:47 Report… report any issues, yeah, before it gets too busy.
**Nacho Bonafonte** 28:51 Yeah, that would be… that will be a great time, and I think that Yeah, I said we could do that now if we wanted, right? But probably we prefer it being a… Big release, or a… yeah, a major release, so… then… then… Probably having those two things properly set, it will be great.
Okay.
**Marius Ciocanel** 29:19 Sounds good.
**Nacho Bonafonte** 29:21 So, if there are no… More topics… I will add here the release.
And yeah, we can just…
**Marius Ciocanel** 29:42 So, that would be the 26th.
of November is the last meeting before December.
**Nacho Bonafonte** 29:53 Yeah, we can make… we can take a decision on the 26th, if you… yeah.
If you want to use that, as a… date for checking, everything is ready, we can… we can take that, yeah. I mean, releasing is very easy, just tagging and… written release notes. Probably we will need… A week of a draft release, so… Not final, not latest.
But you can ping to that with the version number, and just check that everything works on your different scenarios, or different… Yeah, projects that you can have.
So, just to be certain, nothing is broken, and release after that.
So, yeah, maybe 2060s I would date for that, or maybe… We could do it… Yeah, 26th is 2 weeks from now, yeah. Apparently, that's a good period.
And maybe after that, releasing publicly on the 2nd of December, which… or something. That is the next meeting.
**Marius Ciocanel** 30:53 Yeah.
**Nacho Bonafonte** 30:54 That would be the perfect timing, I think, but… Awesome.
You also have voice fear and decisions, not…
**Marius Ciocanel** 31:04 Sounds good to me. Vishwan, you asked about this, what do you think?
**Vishwan aranha** 31:07 Yeah, that sounds good to me, yeah. Giving people enough time to report any issues, and yeah. If we need to do any patch or hotfix, we can do it, like, the second or third week of December, as needed.
**Nacho Bonafonte** 31:34 Okay.
I think more or less says what we… what we decided. Great.
Okay, so, yeah, this is all for today.
Thanks for joining, see you next week, and have a nice weekend.
**Marius Ciocanel** 31:52 Have a nice weekend. Take care, everyone.
Right. Bye.
