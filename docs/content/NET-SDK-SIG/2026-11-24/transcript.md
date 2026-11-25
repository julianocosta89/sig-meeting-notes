SIG: .NET SDK SIG
Date: 2026-11-24
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Alan West** 00:19 Hey, Matt.
**Matthew Hensley (Raintank, Inc. – Grafana Labs)** 00:22 Hey, how's it going?
**Alan West** 00:24 Not too shabby.
Harry.
**Matthew Hensley (Raintank, Inc. – Grafana Labs)** 00:29 Doing alright.
Sorry to be a minute late, always having, Turns out it was my however-many-week LFX login adventure.
**Alan West** 00:40 Oh.
Funny, I always join as a guest. I… I don't… I don't try to go through the login.
Because I figure if I have an option.
To do it the easy way, I'm gonna choose that.
**Matthew Hensley (Raintank, Inc. – Grafana Labs)** 00:55 Don't blame you, probably smart. Let's see, we won't have Martin today, he's out this week.
**Alan West** 01:01 Yeah, I saw that, or he had… Shout a note about that.
Cool. Well, yeah, I kind of anticipated that this week would be quiet.
Do you have any topics that you want to discuss, just the two of us, or…
**Matthew Hensley (Raintank, Inc. – Grafana Labs)** 01:18 Ugh… One thing to consider is that there were some issues in Contrib.
And if you look at the open PRs… Let's see… someone's opened up… Or a couple of folks now have been opening up Hangfire, PRs, and… Doing so pretty quickly.
Against issues, against the repo, but… I was looking at them yesterday, and I don't think any of them are implementing semantic conventions. I think someone opened up some issues.
Hoping to get some stuff in SimComp?
**Alan West** 02:04 Yeah, Hangfire… I… never… Have been aware of any… Semantic conventions for frameworks like that, but, Sounds like maybe you heard of some movement on that?
**Matthew Hensley (Raintank, Inc. – Grafana Labs)** 02:23 No, well, there was, a while back, some effort alongside messaging to revive… messaging, and then for Hangfire and some other… I think Quartz was the other one. There's some Java thing, too. Like, for background batch processing jobs, trying to… Suggests there should be a thing for it, and… I believe, in the issues surrounding it.
I'm sorry, I don't have the actual… info here… But yeah, there's a… I think 5 or 6 PRs open against Contrib right now that… fix open issues that I'm not sure that are, I mean, it's… They're not following semantic conventions, because there are none for this topic.
**Alan West** 03:23 Right.
Yeah, I think I see them now.
Well, what, What caught your eye? Just… just the, volume of these… the volume of these PRs? Are they all from the… they look all from the same contributor.
**Matthew Hensley (Raintank, Inc. – Grafana Labs)** 03:46 There's actually… 3? 2 people? At least? Maybe 3?
**Alan West** 04:00 Yeah, I see that.
Oh, somebody actually does link over to… and open… semantic conventions.
**Matthew Hensley (Raintank, Inc. – Grafana Labs)** 04:18 Yeah, I was trying to find that one that actually linked back, because there were a few.
This did come up some… time ago, That there was a distinction?
But I don't think… Well, I know messaging hasn't moved forward at all.
So I'm not necessarily opposed, as part of trying to… Get that stuff moving.
In fact, a while back, I learned that the Java folks had shipped What they assumed were close enough messaging conventions?
And so, you'll see in Contrib that there's some work against Kafka.
And been working with, a new contributor, trying to Get some of that in, because might as well match Java, if no one's gonna work on it.
And someone's shipped them.
A while back.
we can match them, but I'm not sure there's anything that's hangfire equivalent, so… Not exactly sure how we want to handle this when…
**Alan West** 05:26 Yeah, that's what I'd want to, like… that's what I'd want to touch base with maybe the Semantic Conventions group on, or at least that's the suggestion I would make.
To these contributors, to… the… I just realized that the… Semantic Convention's proposal that is linked to from at least one of the PRs.
One, it's old. It's from over a year ago.
And two, it's just somebody's fork. It's a PR.
Against.
A fork of the Semantic Inventions repo.
I think… My impression is that it's, it was meant as just a draft proposal, but I don't… I have a good sense for whether this actually… Made it over to… The actual semantic conventions repository.
**Matthew Hensley (Raintank, Inc. – Grafana Labs)** 06:35 Oh, no.
**Alan West** 06:35 That's not hard.
**Matthew Hensley (Raintank, Inc. – Grafana Labs)** 06:36 of anything formal right now. There's not, like, a SIG for it, or even real proposals.
This… Here we go.
I found… Kind of what it grew out of, and… If you dig through enough of the issues, it links back to this SimConv.
one… From 2021.
**Alan West** 07:01 Yeah, I found something more recent. Here, I can just share my screen real quick.
this… was an actual PR, open… last year.
Thompson… Tomo, I… I don't really know him, but I recognize his name. He's around the community.
**Matthew Hensley (Raintank, Inc. – Grafana Labs)** 07:26 Yep.
**Alan West** 07:26 So… I've not looked at the details of this, but it was, link to from the… from the Hang Fire PR, or one of them.
And it looks like… I don't know how they… I don't know if it's, like, an actual human made this determination or not, but… Basically, it was just like, this is… there's no active, project within the semantic conventions to support this, so… It didn't get any traction.
And it was rejected because of that.
But, you know, a suggestion that… Starting one would be welcome.
And there's a process for that. So that's probably where I would start with these folks. I mean…
**Matthew Hensley (Raintank, Inc. – Grafana Labs)** 08:26 Well, I did consider that, but also I am guilty of something similar here, encouraging some work on messaging.
Someone tried to restart the messaging SIG, After 2 years, a few months ago.
And also did not get traction.
So, I think that… I don't know, it's a… it's a tough call, it's like… Yeah, there's no semantic conventions for it, but there's also no momentum behind it, and it's kind of a chicken and egg to me.
**Alan West** 09:00 Sure.
**Matthew Hensley (Raintank, Inc. – Grafana Labs)** 09:01 It's like someone's proposing We should just go ahead and implement this stuff as an unstable… Set of attributes, because other people have done it, and it's existed for a while.
And… Yeah, I mean, it's like, they're… There's a bunch of things like messaging that just hasn't moved forward in years, because.
**Alan West** 09:23 And the example… so I definitely understand messaging.
Have you found examples from other SIGs? You mentioned Java for the messaging, but, Has any other SIGs adopted this?
**Matthew Hensley (Raintank, Inc. – Grafana Labs)** 09:39 I believe this, if you… the link that I shared from… Goodness, let me go back and find this.
There's some Ruby things that were done.
And I've actually been available for a while. I mean, Ruby's not… that popular for a hotel, by any means, but…
**Alan West** 10:02 Yeah, Ruby is… Ruby's probably not the SIG that I would necessarily follow as a… As a precedent, just because it's… Historically been kind of behind, the spec.
**Matthew Hensley (Raintank, Inc. – Grafana Labs)** 10:23 What's this one?
Yeah, James Thompson, that one that you have… had… from 2025, did reference the Ruby stuff as precedence.
But there… it just… didn't get much traction, and now it seems… well, I think what happened is that there were issues opened against the .NET repo because they applied to Hangfire.
and… There was the suggestion that they should be aligned with this Ruby implementation, and some folks have taken that as actual work to do.
So, I am perfectly okay if we want to say, like, hey, you need to go talk to SimComp and get a… Something going here?
But… I also wish to be sensitive that people wish… want to help right now.
And getting things going in semantic conventions has been difficult.
**Alan West** 11:27 Yeah.
Yep, it's a hard… it's a hard issue. I… I… I… I'd still want to, like, do some, like, probably due diligence, right? Like, just get a sense for… again, because I've not… I've not paid attention to Hang Fire at all, so I'd want to… I'd want to get a sense for… Is it just the Ruby thing? Is there more than that?
Obviously, we found the previous attempts in the semantic conventions.
But… just… Purely for the… Means to just… kind of understand… Where the momentum… might come from if… We did start accepting this work. You know, would it just be… NET would be kind of standing on this island.
Forging forth with this… Instrumentation with… no other partnership.
from any other SIGs.
Or could we at least, you know, draw some, like, you know… Connections to at least some other Some other languages that might have made previous attempts, and so that we could rekindle this at least more productively. Like, it's hard, right, to, like, get things going in semantic conventions, but if… You build up, like, the… the… enough people's interest, then… Hard becomes a little bit easier, right?
**Matthew Hensley (Raintank, Inc. – Grafana Labs)** 13:16 Yeah, I don't mind replying to them and… asking them to gather some evidence. You know, we're certainly not opposed. Obviously, we want to see Improved instrumentation, just, is the community gonna head this way, and… People are interested, see if they are willing to put in the groundwork.
**Alan West** 13:35 Right.
Yeah, cause, I mean, you know, your point is… You know, the… It's a standard point, right? Like, we… have people who are excited about contributing, and we want to encourage that as much as possible. Yes, that's… That's good, but also, we don't want to accept their work, and then, you know, a year from now, be like, well, this went absolutely nowhere, we don't want to maintain it, let's delete it. You know?
That can be…
**Matthew Hensley (Raintank, Inc. – Grafana Labs)** 14:06 Well, actually, some of my, motivation here is actually because we… continue to have, at the SIMCOM level, Things like… Things move very slowly because there's not enough participation.
But also, there's these examples of people who have shipped, Solutions?
So, like, there's tons of Java instrumentation that doesn't follow semantic conventions.
Because it's just not covered by them.
And people have implemented things, and… for, like, the Kafka metrics that some folks want, I've just been encouraging them, like, okay, let's follow Java.
And… just go for it.
Because there's not been much… interest in SimConv and building a SIG. There's been… I mean, legitimately, there's been no movement since June of 2024.
And it's… Feels like a pretty fundamental thing.
I'd say with this batch processing stuff, it is much less urgent, in my opinion.
Like, it's important for some folks, but it's not fundamental.
And I have no problem asking, like, hey, do you want to go, like, lead this effort? We will support you. But… yeah, I… I'm… If it was something that was much more… critical. I probably… want to say we should just go ahead and push this through and try to make this a conversation within SimConf.
After the fact, in some ways, just because no one's done it.
But I don't feel like this is broad enough to do that with.
Does that make sense?
**Alan West** 15:58 No.
It's also difficult for me, I mean, like, you know, just saying, like, an I statement, it's hard for me to say to a person, you know, bring this to SEMCOMF, I will support you, because I, you know.
personally, I don't know how much bandwidth I'd actually have to, you know, make that I'm meaningful, and… Statement with substance behind it.
And, you know, I mean, that's… that's the general problem, kind of, I think, at CEMCOM level, too, right? There's not… there's not a whole lot of people there, and they have… they have bandwidth for… only so many things, so that's something that the community at large kind of struggles with. I think, I think Java, right, like I said.
previously, like, I don't know that I'd use Ruby as necessarily a precedent, because… I've not… Seeing that community And the members of that committee be the ones that ultimately do get things moved through SEMCOM, where I… my perception of Java is different in that regard, right? For better or for worse, that's kind of where the community is at, right? Like, because of the individuals that are behind the… Java projects.
They are also involved, you know, with the governance of the community, and… the sem… I'm heavily involved with previous semantic conventions, efforts, and so on.
And so… And also Java is probably just the… most mature, I would say? You know, arguably, maybe, but, like, most mature, of the languages.
**Matthew Hensley (Raintank, Inc. – Grafana Labs)** 17:42 Yeah, no, that's exactly kind of my… Concern here, it's, you know, if someone is cribbing from Java, It's probably… okay, just because, like you said, there's a lot of people involved, and… OTel on the Java side, And… If it shipped there… it's probably decently used, or at least was well considered, just because of the level of involvement, versus something like, hey, we're gonna reference Ruby. Yeah. I definitely get that one, I just… It's,
**Alan West** 18:17 And I'd have more confidence, right, if I were to tell somebody, hey, like, Yeah, yeah, go ahead.
and crib this Java work that, you know.
Maybe doesn't have a place yet in semantic conventions, but the fact that you… Cribbed it, and basically made a second… example of this, then I'd have more confidence saying to that person, That they might… Have more luck getting traction with the semantic conventions.
Group.
Because then they could go in not just saying, like, hey, we did this thing in .NET, but it's like, hey, you know.
we did this thing that's also been done in Java, so now there are two examples of it.
So there's more… more weight behind, trying to… Get a more serious conversation started.
**Matthew Hensley (Raintank, Inc. – Grafana Labs)** 19:14 Yeah, and that's what I've, been working with this new contributor on, Kafka-wise.
And including, our friends at Microsoft have… actually vendored the Kafka instrumentation to add some of this.
So there's already people, if you're familiar with .NET Aspire, Like, it's built-in observability… dev loop stuff, it already has some of it, so… There's, precedence in a few spots, but yeah, I agree that… Well, I'll go let them know that we're gonna need to go upstream on this one because there's not enough precedence. I'm happy to… Let them know that one.
**Alan West** 19:59 Yeah, if you want to convey that, that's good. But I mean, you know, like, I would say, just the conversation that you and I have, I don't think is, like, you know, means any final decision has been made. I think, Given it's the holidays and so on, and…
**Matthew Hensley (Raintank, Inc. – Grafana Labs)** 20:15 Hell yeah.
**Alan West** 20:16 Martin's not here, Raj isn't here, I don't know if Peter's, chimed in on any of this yet, but… you know, I'd value their input as well, because… You know.
If anything were to land.
In… This instrumentation, then… You know.
If they say, yes, this is something we're totally cool with maintaining, you know, that… that… that would mean a lot.
I think, so… I guess I'd… Add that caveat, too, about… about this.
**Matthew Hensley (Raintank, Inc. – Grafana Labs)** 20:57 Oh yeah, of course. I mean, we can always decide if it's something we want to pursue.
That's worthwhile, but… Definitely makes it, harder ask.
Thoughts and precedents.
**Alan West** 21:20 Cool, yeah, that's, That's a good observation.
I've not generally been the one that has driven this, but where is this? It's this thing.
I see, yeah, you're saying you're…
**Matthew Hensley (Raintank, Inc. – Grafana Labs)** 21:51 That's actually unrelated.
To what I was… Helping out some folks with…
**Alan West** 22:00 Oh, this is actually one of my coworkers, I hadn't.
Realize that maybe he's reopened this.
Oh, Martin's already kind of approved some stuff, so… That's… good to see. I hadn't, Yeah, this Ashish guy that I work with, he'd expressed some interest in improving some of the AWS instrumentation.
A while back, so… Cool.
And then a slew of hang fire stuff that you,
**Matthew Hensley (Raintank, Inc. – Grafana Labs)** 22:45 Yeah, got the step function thing also from your… colleague, and then this one down here, I'm waiting on authors.
is… Our new contributor.
Trying to catch up with Java on some stuff.
**Alan West** 23:05 Okay.
**Matthew Hensley (Raintank, Inc. – Grafana Labs)** 23:10 If you want to look at the… let's see, the actual main SDK repo, I don't think there's too much.
There's some… Anthropic.
finds… That needs some looking at.
Computer opened today, a couple of them down there in the waiting for reviewers, those last two.
That I'm gonna look at this afternoon.
**Alan West** 23:52 Cool, okay.
Looks…
**Matthew Hensley (Raintank, Inc. – Grafana Labs)** 23:57 I don't know how much you've been looking at these anthropic security scan things.
Have you been out for a bit.
**Alan West** 24:06 Oh, this just updated.
What, is this an example of one of them?
**Matthew Hensley (Raintank, Inc. – Grafana Labs)** 24:17 Yes.
**Alan West** 24:25 Yeah, the… the word I've gotten is that They've been flagged, but… At least the ones that I've heard about.
They're not… really… like, urgent.
Security kind of things.
**Matthew Hensley (Raintank, Inc. – Grafana Labs)** 24:44 No, no, so far, it looks like… I don't know… Maybe 10% of them are… Like, very actionable.
Not to say, like, there's not problems.
To be solved, but… The situation you have to get into to actually exploit some of these is… Yeah.
It… there are some contrived problems. I mean, they're legitimate, you could get into that state, but… It's… Not easy in many cases. So, good things to fix, and there's been some interesting optimizations to pick out of them.
But I don't think there's anything… Very urgent.
**Alan West** 25:31 Yeah.
Oh, cool.
Alright.
Well, I don't have anything in particular.
Beyond that… Sean, I see you just joined.
Do you have anything?
To discuss before we, call it?
**Sean Li** 25:58 I don't have anything.
**Alan West** 26:00 Okay.
Alright, y'all. Well, I don't know. Do you have anything else, Matt?
**Matthew Hensley (Raintank, Inc. – Grafana Labs)** 26:11 I don't think so this week.
**Alan West** 26:13 Okay.
Cool.
**Matthew Hensley (Raintank, Inc. – Grafana Labs)** 26:15 Oh, actually, that's not true. Hotel Unplugged.
Yeah. …is happening again.
**Alan West** 26:21 It's coming up in February again, right?
**Matthew Hensley (Raintank, Inc. – Grafana Labs)** 26:23 Yeah, it's February 1st.
In Brussels.
Bro, drum.
**Alan West** 26:31 Yeah, I thought the word last year was that it was gonna alternate between Europe and the States, but… I guess.
the connection to Fosden was appealing, I assume, or something?
**Matthew Hensley (Raintank, Inc. – Grafana Labs)** 26:44 I think it was just, like, timing with organizing things.
**Alan West** 26:49 Gotcha.
Gotcha. Yeah, I don't know if I'll make it this year. But, are you going?
**Matthew Hensley (Raintank, Inc. – Grafana Labs)** 26:58 Yeah, I'm, I shall be there for this one.
also managed to make KubeCon last minute.
**Alan West** 27:07 No, in Salt Lake? Yeah. Yeah.
Good deal.
Cool, yeah, well, I don't know. We'll see how things turn out. I… I have not… gotten excited about traveling to Belgium again.
**Matthew Hensley (Raintank, Inc. – Grafana Labs)** 27:25 Yeah, I understand that. Hey, I will say one thing, talking to lots of end users at KubeCon, because it had actually been booked by then, I think we're gonna have lots of non-vendor people there.
Or at least, hoping to.
**Alan West** 27:49 in the KubeCon people suggested that they would show up to, Hotel Unplugged?
**Matthew Hensley (Raintank, Inc. – Grafana Labs)** 27:58 Yeah, yeah, hotel end users.
**Alan West** 28:01 Yeah.
**Matthew Hensley (Raintank, Inc. – Grafana Labs)** 28:02 We're pretty interested.
**Alan West** 28:05 Yeah, I think that was the dream of the, of the Unplugged conference, right? That it would be focused on end users.
**Matthew Hensley (Raintank, Inc. – Grafana Labs)** 28:12 It's song.
Yeah, we definitely had some. I was surprised at the level of interest, so… we printed up a bunch of paint-outs and… People enthusiastically took them, and… I got commitments from a few folks that already got approved to go, so… Hoping we're gonna have a pretty good turnout.
**Alan West** 28:34 That's cool, that's cool.
Well… I guess I'll, I'll let you know. I'll let you know if I'm gonna show up. I don't know.
Still got a few more months.
**Matthew Hensley (Raintank, Inc. – Grafana Labs)** 28:53 Sounds good. I'm sure we will, bring it up a few more times, make sure everyone's aware.
**Alan West** 28:58 Yeah.
Cool. Alright, y'all. Well… Enjoy the, long weekend, and… See you next week!
**Matthew Hensley (Raintank, Inc. – Grafana Labs)** 29:11 See ya?
