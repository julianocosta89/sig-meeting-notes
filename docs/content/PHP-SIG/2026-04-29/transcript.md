SIG: PHP SIG
Date: 2026-04-29
Duration: 38 minutes
Zoom Recording URL: https://zoom.us/rec/share/T83Yqp0kzTVE5Xtrb4mt5uAkTL-c7GKXYEEH6cI9ICQ30Iya-IPpD6JOFD92TZ5R.2P3ePhzFQPku2-cP
============================================================

## Zoom Recording Transcript

**Bob Strecansky** 00:42 Hey, Chris.
**Chris Lightfoot-Wild** 00:44 Hey, bro.
**Bob Strecansky** 00:45 How are you?
**Chris Lightfoot-Wild** 00:47 I'm okay, thanks, so are you?
**Bob Strecansky** 00:50 I'm doing alright.
**Chris Lightfoot-Wild** 00:52 Awesome.
**Bob Strecansky** 00:54 It's a kid at home, so… A little tired, but a little lush.
**Chris Lightfoot-Wild** 00:59 Caffeine to fuel you through the day.
**Bob Strecansky** 01:02 Cheers, buddy.
**Chris Lightfoot-Wild** 01:05 Got the old, cup of joe here, as they call it over there, don't you?
**Bob Strecansky** 01:10 So, I mean, that is a thing, but I don't know anybody that would call it that.
**Chris Lightfoot-Wild** 01:15 Well, I suppose I've only seen it on TV, so I don't know where that's come from, but…
**Bob Strecansky** 01:19 I think… I think that's, like, that's like a… like a 1950s thing. It's, like, very, very antiquated.
the kids these days, I'll just, I don't know, I think a lot of them don't drink coffee, I think a lot of them drink energy drinks all the time.
**Chris Lightfoot-Wild** 01:37 There you go. What kind of monster?
**Bob Strecansky** 01:41 Ugh, I love Monster.
I'm a non-apology energy drink connoisseur.
I do love it.
**Chris Lightfoot-Wild** 01:48 I've never tried one. I just worry it's addictive, so probably…
**Bob Strecansky** 01:53 Oh, yeah, yeah. I mean, I guess… They're the same… it's like the same kind of addiction as coffee, right? But… Probably not as good for you.
**Chris Lightfoot-Wild** 02:02 Yeah.
I'm also pretty excited, because I'm going on holiday, slash vacation, after tomorrow.
Hawaii.
**Bob Strecansky** 02:13 Oh, nice, have you been before?
**Chris Lightfoot-Wild** 02:15 Never, no.
**Bob Strecansky** 02:16 Oh, man. Which island? Which island are you going to?
**Chris Lightfoot-Wild** 02:19 Well, we're going to four, so I'm going to probably butcher the names. We're going to… so, well, first we're flying over to Vegas, and then connecting from there to… Honolulu?
And then we're there for a couple of days, I think? And then I'm going to… Oahu?
And then, I'm not entirely sure what the order, there's cow… Cowie? And then…
**Bob Strecansky** 02:43 It's called Kauai.
**Chris Lightfoot-Wild** 02:45 Cool, yeah, that one.
And then, so, bouncing around a little bit… Hey, Sylvia.
**Bob Strecansky** 02:54 I've been to Maui… I've been to Maui. I've been to Maui and Kauai. Make sure when you go there, you go on a coffee ta- like, a coffee tour. That's, like, one of the coolest things you'll ever see.
**Chris Lightfoot-Wild** 03:06 Yeah, we've watched, like, a YouTube video where someone was doing that, so I wouldn't mind trying it. My wife doesn't like coffee, but I do, so I could win over.
**Bob Strecansky** 03:16 Yeah, it does. Like, coffee aside, it's still really cool. What's so crazy about their, like, their climate is so strange that, like, the coffee… treat, like, the coffee plantations are, like, all on the top of a mountain, and, like, you'll drive up the mountain, it'll be a beautiful day, and then you'll be, like, halfway up the mountain, it starts thunderstorming, and then you drive up the other half of the mountain, and it starts… it's, like, perfectly sunny again, and this is, like.
normal behavior for the island. It's not, like, a weird thing. They're like, yeah, that's how, like, how it rains here all the time. Like, what? It doesn't make any sense at all!
Andre, you're here!
**Andrii Androshchuk** 03:52 I am. Sorry, I don't have camera, it's my stationary PC.
**Bob Strecansky** 03:56 That's… that's quite alright. We're just happy to have you present. It's so nice to finally meet you. I feel like I already know you on the internet.
This is…
**Chris Lightfoot-Wild** 04:07 Yeah, we're…
**Bob Strecansky** 04:08 So, because we have a new… hey, Sergey, how are you?
**Sergey** 04:12 Okay, yeah, we had some holidays, so I took a bit of vacation time back.
**Bob Strecansky** 04:18 Nice.
Did you do anything cool?
**Sergey** 04:21 Yes, I would like to… soon I hope I will finish that PR. I would like to finally… I remember I had the discussion about it in Brad. There is this new spec for the sampling, I think it's called the consistent probability sampling.
Essentially, the point there is to have metrics calculated correctly based on the… on the only sampled instances that are being sent, right? So, send enough information so you can extrapolate what was the actual count.
**Bob Strecansky** 04:50 elementary.
**Sergey** 04:51 So that's the main purpose of that change, so that's what I'm currently working on, and And it's quite interesting that this, It's just a new spec for sampling, but for some reason, in Java, they keep it in Contrib.
In my discussions, I couldn't understand why, so I'm going to open it on… just replace the current implementation, but maybe you know why they keep it in Contrib? Like, why it's not just replacing the default implementation?
**Bob Strecansky** 05:19 I don't… I don't necessarily know the technical reason, but I have a very strong guess that I know the social reason.
I have a strong… their job is, like.
one of… there… most of the people that started OpenTelemetry are involved somehow or someway in the Java SIG, and I think there's, like, there's definitely a lot of tumultuous, feeling in that SIG. It feels like… it's, like.
It's very difficult to get things in, and they're, like, move… move in different directions or whatever, so my guess is it probably went in to Contrib, because the barrier to entry for Contrib is a lot lower, and then… Maybe that's what happened, I'm not sure, you know, momentum building or whatever.
**Sergey** 05:59 I see. So you're saying that it's the similar explanation why United States is the only country that still keeps freedom units? It's more about people feeling independent than any logical reason.
**Bob Strecansky** 06:11 I can tell you from experience as an American, it is not logical to use the freedom units, that's for sure.
**Sergey** 06:18 Okay, I understand. So it just gives… it gives them ability to combine any components anybody wants, instead of having, kind of, like, opinionated default. Even though it doesn't sound, like, opinionated, it sounds like it was accepted as an official spec.
by OpenTelemetry, but… so, just to make sure we are on the same page, but we are okay to have it as a default, right? If it's official spec.
**Bob Strecansky** 06:43 Yeah, so I would follow up with the sampling SIG and see why… like, just double check to make sure why they did that, because it's… like, that should be a very low lift to ask them, because they're… I think they're pretty active right now, and I think, I think they'll be able to give you an answer quickly, and if not, then I have… I have no reservations with you implementing it in the base repositories, but I just want to make sure…
**Sergey** 07:06 All other languages did do it, just place the default, essentially, upgraded the default.
**Bob Strecansky** 07:12 Hmm.
Oh, if other languages besides Java just replace it with you, that's information I didn't have, then totally put it in ours.
**Sergey** 07:20 follow, like, the ones that we have in Elastic, so I know about Python, Node.js, and .NET.
**Bob Strecansky** 07:26 If those three have it in the main API and SDK, we can have it there, too.
**Sergey** 07:32 I see. Okay, I will find out. So that's the critical mass, okay.
**Bob Strecansky** 07:37 Yeah. Andre, just so that, you… I want to give you, like, a small… a short primer of how we normally handle this meeting. So, you can see my screen now, and we're walking through the agenda meeting notes. If you have particular, things, discussion points, or action items you want to talk about.
In today's meeting, you can go in here and add them at any time, and we'll talk about them.
So usually… so usually what we'll do is we'll walk through the agenda topics that people have, and then we'll look at the… we'll look at the repos quick and see what's, what's happening, and if we need… if anybody needs to add any concentrated attention on something. And then, with, the remaining time, if we have any left, we'll walk through the, the project boards.
**Andrii Androshchuk** 08:23 So…
**Bob Strecansky** 08:26 So, let's see… Sergey, you were asking about.
**Sergey** 08:35 Yeah, it's called the Consistent Probability Start Plan.
**Bob Strecansky** 08:39 Yes, consistent probability sampling. I just want to make sure that you're on here, too.
Existant… Aviability?
Goodbye.
Okay, and I wanted to add… Alright… Okay, so… I will get… we'll get started on some of these agenda topics. If you have more, please feel free to add them. Please feel free to add them at any point.
I have good news, I was able to get a release of 130.131 completed for Instrumentation 2 with Brett last night.
Minor… there's, like, a minor hiccup with 131. For some reason, it still has 130 contents, so my assumption is we'll probably just do a 132 in the near future, and get us back to true. I wonder if it was part of the implementation steps that we went through with doing two releases at once.
So, nothing… I don't think that there's anything to be nervous about there, it's just, know that that's what happened. 130 and 131 right now are essentially syntactically the same.
**Chris Lightfoot-Wild** 09:56 So have you got, Peckle access to do those in future as well, though?
**Bob Strecansky** 10:00 I have… I didn't… I still do not yet have PECL access. I was finally able to get ahold of Brett. He had… removed Slack from his desktop and had turned off notifications on his phone, and I think he just happened to catch it at some point. He is still on paternity leave. I'm not sure how much longer he's on paternity leave. I know they get a year in Australia, so probably a decent amount of time still.
**Chris Lightfoot-Wild** 10:22 I think it was October, wasn't it? He sort of went off, so… probably another few months, yeah.
**Bob Strecansky** 10:27 That's pretty impressive that you can remember that. I would not have remembered it.
Another thing that came up this week, we have… There is a new, thing that is being actively watched in GitHub. There are security advisories in GitHub for our repositories. We currently do not have any.
I checked for published security advisories. I don't know if that's just a manifestation of us being a smaller SIG, or if there… I very much doubt there's not any security vulnerabilities in our repo anywhere, but… I'm going to continue to try and monitor those as, as we, as we can, and, soon, see when they come in.
There was also discussion yesterday of doing some… Some testing against our repositories with, Large language models to see if they can find any find any by default. There's, like, you know, that whole discussion on the public internet with Mythos and being able to find zero… like, very old zero days, and eventually we'll probably want to do something like that for our repositories, so I… I feel like that's probably a good place to… make a ticket, or make an issue, I'll do that.
**Sergey** 11:50 Are you going to use some public tool, or do you think we'll have some special access to some, like, this myth thing that is kept, I don't know, called private, or whatever?
**Bob Strecansky** 12:01 So, I think the answer to that is, I don't have access to mythos, I have access to regular Cloud, and potentially I can do that, or maybe it will use something else. It is close to the end of the month, and token limits are Are closely approaching, so people will either have none, or they will be using a lot of them, so… I don't know that I'll be able to handle this before the end of the month, so it might be a next month thing.
**Sergey** 12:27 So you're gonna run it privately, you're not gonna… we're not gonna have it as a kind of, like, an action on GitHub, run, like, periodically, or on a QBR, or anything like that.
**Bob Strecansky** 12:38 You know, I would love to see that… I would love to see us being able to do that. I bet you pretty… I bet you a pretty solid amount of money that we won't be able to find a way to get tokens for OpenTelemetry to perform that. I think that would be neat, but… I think that… that is something that hasn't yet… at least… at least at the institution that I work at, the, like, public API with unlimited token canon is not a thing yet, so…
**Sergey** 13:10 I see, okay.
Although I wonder, like, if a GitHub account that we use, does it have maybe some allocation? Just, like, for, you know, for regular capacity that we use to run?
on Gitam.
**Bob Strecansky** 13:23 I don't… I don't know, and I don't know that it's… Yeah, I'm… I don't really have a good answer for you there. I did ask, like, we did ask for… Cloud Max subscriptions for our team, basically, because you, they give… Cloud Mac subscriptions for open source projects periodically, and I think that was, like, almost a month ago, and we're waiting back. I have a strong feeling we'll be waiting for a while, but eventually that could be something.
**Sergey** 13:52 Interesting.
**Bob Strecansky** 13:55 We talked about your consistent probability sampling. Sergey is going to open this in the… APIs, here we go… .
**Sergey** 14:10 Probably just SDK, no change in API.
**Bob Strecansky** 14:12 Oh, okay.
**Sergey** 14:13 There's some of those things, yeah.
**Bob Strecansky** 14:15 Got it. Excellent.
Chris, you wanna talk about Laravel contribute regression?
**Chris Lightfoot-Wild** 14:21 Well, yeah, I'll start opening by an apology again, and this was something that Andrea had flagged, So, actually, Andre, do you want to talk about this at all, or… I'm happy to… There you go for it.
**Andrii Androshchuk** 14:38 I'll prefer to listen for the first time.
**Chris Lightfoot-Wild** 14:40 Oh, yeah, sure, yeah. Yeah, no worries. So, apologies, so Andrea had contributed something in the past to improve the log API usage in the Laravel Contra package, but the… there was a… that was a newer PR from a pre-existing one that had kind of gone a bit stale.
Andreas had been in and merged and released, etc. And then this contributor had come back with, like, a sort of flurry of activity, rebased their PR, And, you know, sort of, it was pictured as, fixing a problem that I thought neither of the preps still existed, so apologies for that, that was my cock-up.
So yeah, we sort of worked through, merged that.
And then, obviously, it introduced some issues, so, yeah. There was… I've sort of gone back onto the, the original PR there, and sort of typed out sort of the plan where I'm suggesting we probably want to just revert their work.
You know, no hot feelings or anything, So, did want to sort of take it a step backwards.
Andrea, I don't know if you've got any, sort of.
opposing thoughts on that, but I don't think…
**Andrii Androshchuk** 15:57 Yeah, I'm pretty much aligned with that. I'm more interested to get the pipeline green so that I could contribute more, because right now it kind of just stops me or prevents me from.
**Chris Lightfoot-Wild** 16:12 Yeah, absolutely. So yeah, one of the things that had, been introduced was, like, using the deprecated configuration resolver from the API, so that failed on my SAM.
Check.
But I guess I neither then thought, well, okay, that's a deprecation that didn't previously exist, and it would have passed, you know, a few weeks ago if that wouldn't have been merged, but that was actually just masking other issues as well.
So, yeah, I'll revert that, apologies again, I'll tag a new release as you've got your next PR lined up, if that's okay. We can sort of align that. Sure.
But then, I guess… That leads me on to the next, oh yeah, sorry, I'm just trying to zoom in a bit. The next point I'd put on there, about the contribodors concept I'd seen.
Like, across Java and then, like, the collector repos?
**Bob Strecansky** 17:14 Yes.
**Chris Lightfoot-Wild** 17:16 I don't know if that was something that, like, maybe we could lean on the pattern that they seem to have.
Where they've kind of got their, monorepo in sort of split components.
I guess it's similar to how we've got contribib with.
You know, the various instrumentation packages all kind of under the same repo.
But then they've got some additional tooling to kind of delegate certain, I can't remember if they have, like, a contrib group, potentially, as well, but to delegate certain components toward those interested parties.
Obviously it was fortunate, or maybe unfortunate, depending on your perspective, that Andrea was around to highlight that, issue, and, obviously it's great he was here to pick it up, but… It would probably have been good if… there was a mechanism to tag interested parties in Laravel that, you know, there's a PR opened against it, and, you know, you might have a vested interest in it.
And I obviously don't currently have that.
So, yeah, I just wondered what the thoughts were around that kind of… Process, or is it something we'd adopt, or…
**Bob Strecansky** 18:27 I'm totally for code owners. We use it at my day job, and it really helps to… Delegate and, define ownership and allow people to, be notified, or at least, Be involved in the things that they want to be in.
no, you know, no hesitation for me for adding a codenard style in the contrib repo. I'm very happy to contribute to it, too.
**Chris Lightfoot-Wild** 18:51 We do already have one, don't we? We've got one already, but it was to, like, divvy up, like, certain paths to more specific people, rather than just, like, the main approvers or maintainers group.
**Bob Strecansky** 19:04 Understood. Okay, well… since we have one, I'm very happy for you to slice and dice it however you see fit. I think… I think it's a good idea. It's… there… how do I say that the right way? It's important that we make sure that people get the notifications for the things they want, and nothing more, right? Like, if we can make it so that Andre only gets stuff that he really cares about, and Sergey only really gets stuff that he cares about, that's going to be better than if you just get blanketed.
**Chris Lightfoot-Wild** 19:34 And I wasn't, sorry, necessarily saying, hey, Andre, you got to come and be part of this or anything, I just… as the concept, I thought if we had that, like, foundation there.
someone may be interested to sort of say, yeah, I'm happy to help out if I can.
You know, I think you've mentioned before, Powell, as well, with, like, the curl instrumentation you've worked on.
If someone makes a change to that, yours is currently not tagged or notified in any way, so… you know, I think that would probably help towards that.
So, yeah, I'll have a look at copying the existing, sort of, other SIGs way of doing that, if that's okay. It'll obviously be after I'm back from, vacation.
**Bob Strecansky** 20:18 Exactly.
**Sergey** 20:20 It probably would be more extendable if you use groups instead of directly people, right? Although I don't know if it's… much overhead is.
**Chris Lightfoot-Wild** 20:29 It looked like they did… so we've got, like, this contrib maintainers group now, and a contribib approvers group.
And it looked like… basing it on the Java one, they've got, the sort of top-level one is a Java triages.
And then the… approvers group.
Maintenance group is a subgroup of that. And then they've also got, somewhere in the mix, like, a contributors group.
So that the wider audience, if anyone wants to be a component owner, they have to be in that group.
**Bob Strecansky** 21:02 Yeah, I think…
**Sergey** 21:03 I'm just wondering, like, how do you envision it? Like, have Laravel instrumentation Group, or just directly encode the names of people into code owners?
**Chris Lightfoot-Wild** 21:13 If you look at the Java contrope package, instead of our PHP one, Bob.
That's got… there's, like, some additional scripts that's in the workflows, Where it sort of divvies out, based on, like, path mapping, who it thinks should be tagged for the PR.
**Bob Strecansky** 21:34 Where's there, there it is, like, keep it in the right place.
So, Java contributor… is that what you're talking about?
**Chris Lightfoot-Wild** 21:39 Well, they own the repository as a whole, but if you go to the… they've got a component owners.
YAML file in that GitHub directory as well.
**Bob Strecansky** 21:49 Oh, okay.
**Chris Lightfoot-Wild** 21:50 And this, this sort of says there, like, a list of.
**Bob Strecansky** 21:54 Oh.
**Chris Lightfoot-Wild** 21:56 So, when you open a PR against something that matches the path.
The component path, it'll tag those people.
Understood.
**Sergey** 22:04 something that is already handled by GitHub, or did they implement some workflow?
**Chris Lightfoot-Wild** 22:09 This looks like.
**Bob Strecansky** 22:10 It looks…
**Chris Lightfoot-Wild** 22:10 specific workflow that hotels come up with.
**Bob Strecansky** 22:13 Let's see, so if we go and look at the workflows assign our viewers…
**Chris Lightfoot-Wild** 22:19 So, obviously, I've got no insight into how well this has gone for them, but it seems it's in Java and Hotel Collector as well.
Yeah.
**Bob Strecansky** 22:29 I'm pretty sure this is one of the hotel people.
**Sergey** 22:35 It has, change vulnerability written all over it, right?
**Bob Strecansky** 22:42 It sure does.
I mean, I think… That's… I think that's alright.
**Sergey** 22:46 But you're saying, so there is no need to go, kind of, like, in this overhead of creating groups? It's kind of the intermediate solution that allows to map, kind of, like, create ad hoc group on the fly?
**Chris Lightfoot-Wild** 22:58 I don't think it needs, like, a per component group, does it? Sorry, Bob.
**Bob Strecansky** 23:02 Yeah, I don't think it's a group. I think it just… the way that I'm reading it is this assigns reviewer, so, like, if I open up a contrib request against AWS X-Ray, and then somebody is on the AWS X-Ray group.
Then they are able to… then they get tagged in the pull request.
**Sergey** 23:22 Is GitHub smart enough to understand that if just one member of that list approves, that's enough, or if all of them will be added as required to review, all of them need to approve?
**Chris Lightfoot-Wild** 23:34 You can have a minimum number of reviewers, can't you, on a PR?
**Bob Strecansky** 23:37 Yeah, I, I think, I think, if I remember correctly, you would just have to, like.
you have to have one approved reviewer to merge a PR. So, like, a really good example of this is, let's just say, let's just say Powell gets tagged in… the… the, the curl implementation that Chris was just talking about. He can approve it. I don't know that his approval would be good enough to merge it, but that would be a good virtue signal for me or Chris to approve it as well.
**Sergey** 24:09 Okay, so by tagged, do you mean, like, he will be listed as one of the required for review?
**Bob Strecansky** 24:17 It's just like, hey, can… hey, can you.
**Andrii Androshchuk** 24:22 Pretty good.
**Bob Strecansky** 24:23 It's not, hey, you need to…
**Sergey** 24:24 There you go, okay.
**Pawel Filipczak** 24:25 you know, notification. Sometimes I'm losing that someone changed something in the code, and, you know, I'm getting hundreds of emails.
So, yeah, it's… From time to time, I'm just missing the, the, the… the notifications, so it's hard to read everything, and maybe I should improve filters.
But anyway, yeah, I think it's… it can be still assigned, I mean, the review, to the group of the approvers, official approvers, but the review can do anyone, right?
**Chris Lightfoot-Wild** 25:01 Right.
**Sergey** 25:02 So we're not gonna have, like, we have an elastic where we have more strict, like, for example, if I'm touching documentation subdirectory, then I will need approval from documentation team. Here, we're still gonna be more relaxed about it, but… It's kind of like you saying you will read it as a signal of somebody reviewed. If some components were touched, and you see that all the people from those components, at least one of them reviewed, then it will be used as a signal.
that, all repo maintainers will have more confidence to merge that, right?
**Bob Strecansky** 25:32 Right. I think we don't have… we don't have enough.
We don't have enough people contributing for us to be that granular right now. That could change in the future.
Right? Like, the way that I see it right now, we have less than a dozen people that contribute to this repository on a given cadence, so I think optimizing for, like, having specific subdirectories have specific subgroups is probably not applicable quite yet, but fingers crossed, maybe someday.
**Sergey** 25:59 April.
**Chris Lightfoot-Wild** 26:00 Yeah, I think part of it was, obviously, I've got a vested interest in the live one, because, you know, day job uses that, but, like, I'd feel less confident just saying, yeah, this looks fine for the… you know, the Symphony one, or WordPress, or whatever, but if someone's come along, contributed before, and… can get, like, pulled out of the woodwork by being tagged in it. That'd be great. I think the bit you said then, Bob, about the review kind of not counting, I think… you can get the sort of green ticket from what I've read.
There is that sort of contrope group that those members are in.
**Bob Strecansky** 26:35 Right.
**Chris Lightfoot-Wild** 26:36 They can't merge it, but then the ticket is no longer grey, it's, like, green, and then we can see that and go, cool, yeah, this person that knows what they're talking about has accepted it, and happy to merge.
**Bob Strecansky** 26:45 Which is… which is kind of… I mean, I kind of understand that, but I… yeah, that's… I mean, that's fine for me. I think if somebody… if somebody that is a subject matter expert Is approving the pull request.
Then that probably means that it's okay to merge, in my perspective, but…
**Chris Lightfoot-Wild** 27:02 Yeah.
Yeah, so I'll have a look at how they've got their ecosystem set up and see if I can kind of mirror that, if there's no objections to that.
**Bob Strecansky** 27:12 See, this is me… this is me dancing for that, Chris. I'm very excited about that.
**Chris Lightfoot-Wild** 27:16 Cool. Thanks.
Again, apologies again, Andrea, for the confusion. I'll, I'll merge.
I'll do the revert, and then tug… tag your PR after that.
**Andrii Androshchuk** 27:28 Yeah, no worries. Thanks.
**Bob Strecansky** 27:30 By the way, Chris, this, this got merged, like, 30 minutes ago.
**Chris Lightfoot-Wild** 27:36 I had seen that, yeah, sorry, I'd, I know you said we were going to touch on this subject, and then Matt's completed, so I said, oh yeah, cheers for that.
**Bob Strecansky** 27:44 Yeah, I guess they do auto… they do auto-merge in this repo, so…
**Chris Lightfoot-Wild** 27:49 Because it looked like I couldn't see the repo anymore, and then he says, maybe I'm going to be able to see it again in future. If there's a final, If you go back to the community issue, there's a final one.
**Bob Strecansky** 28:02 MIDI issues… where did it go?
**Chris Lightfoot-Wild** 28:04 33, 60, knock as well.
**Bob Strecansky** 28:09 Oh yeah, I… that's… Let's look at that way.
**Chris Lightfoot-Wild** 28:15 So there's got, like, a… follow up here. So, have you already… is that the one you've already looked at, sorry, or…
**Bob Strecansky** 28:20 Yeah, that's… yeah, that's this one. That's the one I was talking about. It looks like it's adding you back into this.
Grouping.
**Chris Lightfoot-Wild** 28:27 So if you're okay with that, I guess you could.
**Bob Strecansky** 28:30 I will approve it.
**Chris Lightfoot-Wild** 28:31 Yeah, I wasn't sure, like, if I'd, you know, accidentally done something, or… I was, like, losing my mind.
**Bob Strecansky** 28:41 There we go.
**Chris Lightfoot-Wild** 28:43 So yeah, I was… I was trying to get through a bit of a backlog as well, with whatever was on the contrary board, so I've started merging it, I hope it's alright, I've started merging some of the renovate stuff.
Yeah, trying to lean that down a bit, because it was spreading two pages of PR, so… We'll try and get on top of that and take some more things before going on holiday, so…
**Bob Strecansky** 29:02 Sounds good to me.
**Chris Lightfoot-Wild** 29:04 Thank you.
**Bob Strecansky** 29:09 Alright, I think that's all of our agenda topics. Anybody else have anything they'd like to talk about?
Should we walk the boards?
**Sergey** 29:18 A small issue, I wonder… I don't have the issue with me, but maybe some of you follow, there's this issue on the General Committee, I don't know how it's called, the discussion to have a distro bin, including all the stable components? Are you familiar?
**Bob Strecansky** 29:33 Oh, yeah.
**Sergey** 29:34 initiative?
**Bob Strecansky** 29:35 Yeah, they've… The specifications SEG meeting has talked about this pretty much every week for, like, a couple months, about stable. Are you talking about stable by default?
**Sergey** 29:45 Yes, yes, yes.
**Bob Strecansky** 29:46 Yeah. Yeah, there's… if you go… if you go and look at the instrumentation, SIG meeting notes, there is copious, copious discussion about this, and it is a very, very hot topic.
**Sergey** 29:58 Is it… is there anything actionable already for us, or it's all still on…
**Bob Strecansky** 30:05 It's…
**Sergey** 30:05 Go either way.
**Bob Strecansky** 30:06 So I go to that meeting every week, and it ends up just being an endless cycle of, we should do this, we should not do this, we should do this, we should not do this, let's do this, let's not do this, this is the data, this is the other data. Like, it's one of those things that I feel like they'll come up with a resolution for it sooner or later, but I feel like it's, they're talking in circles quite a bit, but it's… I mean, that's… it's a difficult decision to make, right? Having stable by default is… It's something, so…
**Sergey** 30:34 By stable, they don't mean, like, not flaky in the sense that it scratches. By stable, they mean, like, the data that is being produced, it's stable, only uses, like, stable attributes and stuff like that?
**Bob Strecansky** 30:45 Yes.
**Sergey** 30:46 Okay, I see. And we have some kind of flag that allows to control that, right? Maybe, if I remember, was it only for HTTP?
There was some flag that you could have controlled and told it, do you want it to generate experimental or not, no? But it doesn't matter. So, you're saying there is nothing actionable yet, so…
**Bob Strecansky** 31:07 Not actionable yet, hopefully it will be actionable soon-ish.
**Sergey** 31:11 Oh, okay.
**Bob Strecansky** 31:12 Yeah.
**Sergey** 31:13 So, will it affect the distro? When they talk about, by default, they don't mean, like, SDK, right? So… or instrumentations. There still will be instrumentations that are not, like, stable in the sense.
**Bob Strecansky** 31:24 Yeah.
**Sergey** 31:24 each room that will also be stable by default? Is it each component individual, or is it some kind of collection that we will call distro?
**Bob Strecansky** 31:33 I don't know. I don't know, Sergey. I'd probably go and look at their… I know they've been actively discussing that in their SIG, and they have a bunch of issues about it. I've watched it at a surface level, but not any deeper than that.
**Sergey** 31:46 Okay, but you let us know if it's become sectional.
**Bob Strecansky** 31:49 Yeah, well, the second that… the second that somebody says that in that meeting, that it's… we have declared this the way that we're going, I'll make sure that we communicate that effectively here, too.
**Sergey** 31:59 Thank you.
**Bob Strecansky** 32:00 You're welcome.
I'll put a note about that, just in case anybody.
Okay, let's go take a look at our… Let me pause real quick… Alright, 36 mil… or 35 million.
Alright, let's go look at PHP and Tristan pull requests.
**Chris Lightfoot-Wild** 32:37 That top one, Bob, I've overviewed that, it's pretty small, but it could do with, Maybe you're merging it in?
Possorte.
**Bob Strecansky** 32:44 Okay.
**Chris Lightfoot-Wild** 32:45 If you're happy with it, if you'd add it to your list. There's a documentation one on the back of it as well.
**Bob Strecansky** 32:50 Okay, I will… mark that and review it in a little bit. And then… Rest of these are all renovate, and… Couple others, nothing crazy…
**Chris Lightfoot-Wild** 33:01 There's one from Neveh in there somewhere, which I see…
**Bob Strecansky** 33:06 Yeah, he's… wait, you're talking about this one?
**Chris Lightfoot-Wild** 33:09 Yeah, that was it.
**Bob Strecansky** 33:10 Okay, I will also…
**Chris Lightfoot-Wild** 33:12 Sorry.
**Bob Strecansky** 33:13 I do apologize for it. I will review that, too.
Alright… Also, this one got approved, and we haven't merged it yet.
**Chris Lightfoot-Wild** 33:28 Was that one… Did it actually bump it from… I can't remember if it just bumped it from 4 to 5?
**Bob Strecansky** 33:35 Core.
**Chris Lightfoot-Wild** 33:35 Additively, okay, cool, that's fine.
**Bob Strecansky** 33:37 Yeah, that's… that's the…
**Chris Lightfoot-Wild** 33:39 People would have bumped it, yeah.
**Bob Strecansky** 33:43 Right.
Close, control… Anything exciting in here? These are all just for renovate.
**Chris Lightfoot-Wild** 33:58 I'll try and work through a few more of those, if you're happy with me doing so.
**Bob Strecansky** 34:02 Yeah, that'd be great.
Thank you.
These are all renovated, too.
I will. I'm planning on going in and doing a renovate merge at some point this week, but… Andre, for reference, Renovate does automatic dependency updates for us, which is really nice, but you have to review them all, which is really not nice.
**Andrii Androshchuk** 34:21 I see.
**Sergey** 34:23 So when you say you're gonna do a renovate merge, you mean, like, you will enable automatic merge, or…
**Bob Strecansky** 34:29 No, I mean, I'll have to go in and approve and merge them all. We don't have the ability to do automatic merge right now. I would love to, but…
**Sergey** 34:38 You already… you're already feeling ripe to give it up and reviewing each PR individually?
**Bob Strecansky** 34:43 I don't know if it's… I feel alright about it, or it's just I'm tired of doing it?
**Sergey** 34:48 Yeah, right, no, it was obviously going to the direction, I was just wondering when you will give up, but you're saying there is no technical ability to enable that. Okay.
**Bob Strecansky** 34:57 I know that there is, I know that auto-merge is possible in our repos. I don't know yet how to enable it, and I don't know if they're letting specific SIGs do that, or if it's just… like, because we just saw that in the admin repo, right? So I know it is possible.
But I don't know if it is…
**Sergey** 35:14 But auto-merge means that when you approve, then it merged immediately. That means a lot.
**Bob Strecansky** 35:18 Right. But I don't… yeah, but I think that there's different levels of auto-merge, if I remember correctly. I could be wrong, but I think there's one that's, like, if it passes tests, then it can get merged, and then also, if it's approved, it can get merged. I think the latter is what what we're doing… it's still… that still means I have to go in and approve all of those, which is not any different than approve and merge, really, but…
**Sergey** 35:42 Right, right.
**Bob Strecansky** 35:43 So… Okay.
Anywho… Alright, that was the board, and then… Project board, check this out real quick.
Yep. Nothing… nothing really moving here.
And then, yeah, that's it.
Anybody have any last-minute stuff before we adjourn?
**Chris Lightfoot-Wild** 36:08 I guess only the, again, thanks, Sandra, for coming. You mentioned the other week about, like, a place to flesh out the ideas, perhaps a direction you wanted to, you know, add to the instrumentation.
Obviously, you see we've got, like, a project board, we don't use it, like, really religiously, but… If you've got ideas to throw into the mix, feel free to… open some issues, I'll keep, you know, opening PRs, etc, but…
**Bob Strecansky** 36:35 This is a good place to do it.
**Chris Lightfoot-Wild** 36:44 Yeah, because I've got my very, very long… it's going to come up to 2 years soon, that PR I've got for Laravel.
**Andrii Androshchuk** 36:50 Yeah, I was about to ask…
**Chris Lightfoot-Wild** 36:53 Yeah. What's that story going?
**Andrii Androshchuk** 36:56 Whether there are any real expectations when that thing will be done.
**Chris Lightfoot-Wild** 37:04 Yeah, probably another couple of months, I suppose, because I'm going away for most of the rest of May.
But it would be good if you've, like, got any time to potentially eyeball it and, you know, offer up your opinion, thoughts on it, because there's quite a lot of changes it's moving toward.
Using SBI, which is the newer, sort of, way of doing stuff.
Yeah, just to get someone else's input on it would be awesome.
So, yeah, feel free to poke around with it if you've got any capacity.
**Andrii Androshchuk** 37:34 Okay.
**Chris Lightfoot-Wild** 37:36 That'd be amazing, thank you.
**Bob Strecansky** 37:42 Alright.
Oh, so…
**Chris Lightfoot-Wild** 37:44 Yeah, I'm gonna be… I'm gonna be away until the end of May, so, yeah, apologies, I won't be able to make any meetings, but I'll be sunny myself in Hawaii, so…
**Bob Strecansky** 37:53 So you're back in June?
**Chris Lightfoot-Wild** 37:55 I'm back on the 26th, I think it's 27th, potentially, Wednesday, so I'll probably be at that one.
**Bob Strecansky** 38:02 Sounds good. Enjoy your time off.
**Chris Lightfoot-Wild** 38:04 Cheers, Central.
**Bob Strecansky** 38:06 Alright, cause y'all enter.
**Chris Lightfoot-Wild** 38:07 Visitor.
**Pawel** 38:08 You.
