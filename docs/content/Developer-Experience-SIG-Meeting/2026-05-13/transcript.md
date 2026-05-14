SIG: Developer Experience SIG Meeting
Date: 2026-05-13
Duration: 27 minutes
============================================================

## Zoom Recording Transcript

**Juliano Costa | Datadog** 01:31 Hello, hello!
Sorry for being late.
**Johanna Öjeling** 01:36 Hello!
No worries. How are you, Jared?
**Juliano Costa | Datadog** 01:41 Oh, good, oh good. Yourself?
**Johanna Öjeling** 01:43 Yeah, doing well. I'm, wrapping up some things at work today before taking one and a half week off.
Or, yeah, tomorrow is a public holiday, then I'm taking Friday off, and next week, so, yeah.
**Juliano Costa | Datadog** 01:58 Like, yeah, likewise here, so…
**Johanna Öjeling** 02:01 Yeah, you're… oh, okay! Nice. So, what are you planning to do during your time off?
**Juliano Costa | Datadog** 02:08 So we are going to Hungary, to a, like, an all-inclusive place where I don't need to worry about anything, I just go and they take care of me.
**Johanna Öjeling** 02:19 That sounds amazing.
**Juliano Costa | Datadog** 02:22 Yes, and there are a lot of swimming pools and stuff, so the kid can play and get tired, so then we can all rest.
**Johanna Öjeling** 02:30 Perfect. How old is your kid?
**Juliano Costa | Datadog** 02:34 3?
**Johanna Öjeling** 02:35 Okay…
**Juliano Costa | Datadog** 02:37 Actually, he turns 3 on Friday, so we'll be there to celebrate his birthday.
**Johanna Öjeling** 02:43 Wow! Yeah, I'm sure he'll love it.
**Juliano Costa | Datadog** 02:48 What is… what are your plans for… for the…
**Johanna Öjeling** 02:53 I'm also traveling, but not as far, just traveling within Sweden to my parents.
**Juliano Costa | Datadog** 02:59 Huh. Cheers.
**Johanna Öjeling** 02:59 Yeah, and next week, on Monday is my birthday, so we'll have some, well, celebration. It's not a big birthday, but still, it's nice to get together, and yeah.
**Juliano Costa | Datadog** 03:12 Whoa.
**Johanna Öjeling** 03:13 Yeah.
**Juliano Costa | Datadog** 03:14 Nice, well done.
**Johanna Öjeling** 03:15 Looking forward to relaxing, and yeah.
hopefully we'll have good weather, so I can enjoy some sunshine.
**Juliano Costa | Datadog** 03:24 Yeah, it's getting nicer, at least in Austria. Yesterday was cold, but yeah, overall was good, so hopefully you also get, good weather there.
**Johanna Öjeling** 03:36 Yeah, - thank you.
**Juliano Costa | Datadog** 03:40 Before we… we jump in to… to the… some actual discussion. I want to ask you one thing. Are you aware of this report?
It's called GitDM.
**Johanna Öjeling** 03:57 Let's see… Is this for your… specify your company… yeah.
**Juliano Costa | Datadog** 04:06 Yeah, you're affiliate.
**Johanna Öjeling** 04:07 Yeah, yeah, -
**Juliano Costa | Datadog** 04:08 Okay.
Okay, okay.
Yeah, I'm… I'm doing some… some research here, and I… I found a bunch of… a bunch of folks that are not listed there.
And, like, even my contributions are not counting as, towards Datata.
So I, I was, wondering what, what is going on.
Let me… Let me show it to you what I mean?
Where is the share button? Here.
I… I opened an issue on Linux Foundation sites, because… I don't know if you know, but the Git DM and also the… the… Contributions that we do are rented here, and then you have, like, contributors Leaderboard, and organizations leaderboard.
So, when you are linked to the proper company, all your contributions add some to the company, so… I was… just… randomly checking the developer experience one, and I saw, okay, yeah, I have 78 contributions, but Datadog is not even listed here.
I guess I'm going… towards, like, CNCF. I don't know why.
So I… I opened Aisha.
2… to check with them that. The same for the… for the demo.
So I'll drop this one.
So, in that…
**Johanna Öjeling** 05:52 Clear.
**Juliano Costa | Datadog** 05:53 The third 3,000, but then, like, da-da-da is not even here.
**Johanna Öjeling** 05:59 Weird.
**Juliano Costa | Datadog** 06:01 So, yeah, I… I raised that, let's see what they say.
**Johanna Öjeling** 06:07 So, there is also another stats page that uses a Grafana dashboard.
**Juliano Costa | Datadog** 06:15 Yeah, yeah, the dev stats,
**Johanna Öjeling** 06:17 Yeah, exactly. Is it the same there, that… Sarah, or… or you?
**Juliano Costa | Datadog** 06:23 I don't know, actually, here, but I'm… I know that…
**Johanna Öjeling** 06:29 Yeah, the dev stuff has some issues, like, my contributions rarely show up there, so there is something weird going on there, too.
**Juliano Costa | Datadog** 06:37 So let… okay, so I'll use last year and go to the developer experience.
So I have 36, no idea what is that?
And company is Datadog, so let me go to the… Company, maybe?
needs table… Yeah, but this, this won't help. I want, like, companies per repo, or something like that.
This one, yep, and then I'll do developer experience.
But not, less decade? Less 2 years?
Yeah, just, contributions from Damien are… are… on web stats.
Which is interesting.
Maybe because…
**Johanna Öjeling** 07:48 They're not very accurate.
**Juliano Costa | Datadog** 07:50 He, So, it's tricky. I know that Linux Foundation uses one metric, and DevStats uses a different one.
And last year, Linux Foundation started pushing the LFX Insights as the official one, so then I started using it as official, so… I've been trying to report a bunch of stuff here.
I… I found a couple of other issues, like, if I go to the rest sig… I know from my team, Scott and Bjorn, they're not actually maintainers, they're approvers on the repo.
**Johanna Öjeling** 08:35 Okay.
**Juliano Costa | Datadog** 08:36 But it looks like they're just tagged, they just have the maintainer tag.
So, I will maybe take a look at the… the repo and, eventually send a PR or… or, like.
**Johanna Öjeling** 08:49 Okay.
**Juliano Costa | Datadog** 08:50 Let Claude do that for me.
**Johanna Öjeling** 08:53 Is this, statistic populated? Is the code also in the, repo, or do you know?
for the… next insights?
**Juliano Costa | Datadog** 09:05 That's a good question.
**Johanna Öjeling** 09:08 Or, like, how can we see where this stuff's come from?
**Juliano Costa | Datadog** 09:12 Yeah, that's a good question.
**Johanna Öjeling** 09:14 What's your attention?
**Juliano Costa | Datadog** 09:19 They have a documentation… duh… I… don't know.
Yeah.
But I think on the… On the documentation, where is it?
These sites… They do mention what the… What are the… Let me… let me share my screen again.
So, in this… Docs, they… they mention… where is it? Data sources?
**Johanna Öjeling** 10:20 Okay.
**Juliano Costa | Datadog** 10:22 and the… What is tracked?
**Johanna Öjeling** 10:28 Mmm.
**Juliano Costa | Datadog** 10:29 So, for instance, in GitHub, And Git, I think it's the one that we most mostly interact with.
It's like, when you reviewed a commit, when you approved, when you open a pull request or close a pull request.
So, I don't know… Like, if there are… different points.
Because… like, if I open a pull request changing a Helm chart that will update 1,000 lines, and open a PR, fixing a typo on the docs.
**Johanna Öjeling** 11:08 -
**Juliano Costa | Datadog** 11:08 would those two PRs be counted as a PR, or do I have, like… okay, so it's X times the number of lines you are changing.
Because Yeah, when we take a look at, for instance, let's go to all repos.
And so, for the last, 90 days.
I don't think, for instance, Tresca opened 6,000 PRs.
**Johanna Öjeling** 11:35 Yeah.
**Juliano Costa | Datadog** 11:36 I think there is some metric there, like, what you're actually doing and stuff, so… Yep.
Yeah, that's it.
**Johanna Öjeling** 11:47 So, it's interesting, like, Datadog doesn't show up at all in the leaderboard.
**Juliano Costa | Datadog** 11:55 Which one, do you mean?
**Johanna Öjeling** 11:58 Like, if you scroll down to the organization's leaderboard.
**Juliano Costa | Datadog** 12:02 I know, it…
**Johanna Öjeling** 12:03 Oh, there it is, okay.
**Juliano Costa | Datadog** 12:04 Yeah. When you…
**Johanna Öjeling** 12:06 It's.
**Juliano Costa | Datadog** 12:08 When you go to…
**Johanna Öjeling** 12:08 just for…
**Juliano Costa | Datadog** 12:09 To the overall repositories, yes.
**Johanna Öjeling** 12:11 Yeah, but, okay, yeah, but for, yeah, some people like yourself and the other two colleagues you mentioned.
Yeah, they're… they're pretty broken link to the affiliation.
**Juliano Costa | Datadog** 12:24 It is tricky because, like.
for me, checking the folks that I know from Datadog is easy, like, I know Young, I know Pablo.
Here, great, but… who else is from Datadog that is here, and… may not be… counting towards that, you know? So, like.
**Johanna Öjeling** 12:46 Yeah.
**Juliano Costa | Datadog** 12:47 And, like, all the other companies, because if it's happening with me, most probably there are other cases.
**Johanna Öjeling** 12:52 Yeah,
**Juliano Costa | Datadog** 12:54 So, yeah, it's tricky to… to…
**Johanna Öjeling** 12:59 Good thing you offend an issue about it.
**Juliano Costa | Datadog** 13:03 Yeah.
Maybe I should make the issue more generic.
Because at the moment, I'm just like, hey, this is, like, I'm saying, hey, this is wrong for my user when I check GitDM, I am… .
properly listed here as Datadog Inc.
But, when we access this link.
and I'm a top contributor, Datadog is not listed, so, yeah.
**Johanna Öjeling** 13:46 Yeah.
**Juliano Costa | Datadog** 13:47 Maybe we…
**Johanna Öjeling** 13:48 Yeah, that gives them a concrete… to investigate.
**Juliano Costa | Datadog** 13:55 Yeah.
Anyway, let's see how… how they… how this develops. Sorry, this is totally, Outside of the scope of developer experiences.
**Johanna Öjeling** 14:10 Yeah, no worries. We don't have much on the agenda today, so…
**Juliano Costa | Datadog** 14:16 I'm excited.
**Johanna Öjeling** 14:17 That also part of developer experience.
**Juliano Costa | Datadog** 14:21 No, there is actually another seat that is the contributor experience.
**Johanna Öjeling** 14:26 Oh yeah, that's right, yeah.
**Juliano Costa | Datadog** 14:27 That's… that's for them, not for us. True, yeah, of course.
**Johanna Öjeling** 14:31 Sister's sick.
**Juliano Costa | Datadog** 14:32 Yeah, so… As we spend already 15 minutes talking about that, I want to ask you, what… what would be the best approach to kind of raise awareness of folks about GitDM?
Because not everyone knows about this repo, and there are contribut… like, I… Again, randomly fo- randomly… saw a light step.
as top contributor in REPL, and I was like, okay, LightStep was sold, at least 2, 3 years ago. It shouldn't have any contribution assigned to LightStep.
**Johanna Öjeling** 15:16 Oh,
**Juliano Costa | Datadog** 15:18 So then I… I checked, and Jacob Arnhof, I think he's a Helm approver.
Or… or even a home maintainer, and he's assigned to LightStep on Git DM.
I'm pretty sure he knows about GitDM, maybe some… people just forget about it, but I… I know that there are other folks that do not know, and, like.
New folks are not, not there at all.
**Johanna Öjeling** 15:50 -
**Juliano Costa | Datadog** 15:51 Should that be, like, should we maybe… have a process, like, hey, sign the ECLI, ECLA, and also assign your company here on this ripple, or whatever. I don't know.
**Johanna Öjeling** 16:06 Yeah, that's a good, idea, and I only found out about it from Grafana, like, someone, posted, like, yeah, don't forget to do this, because we want it to be, like, accurate. So I think, yeah, people know about it from their employers, like, and that's only when the employer cares about the stats. So I think it would be good to have that reminder, both For… that will prompt new contributors to add their affiliation, but also remind existing contributors who may forget to update their affiliation if they change jobs or employers.
And, yeah, I think that's a good, I was thinking, hmm… like, is it something… like, how do you reach those people? Is it through some kind of social media, or, like, LinkedIn, or Slack, or whatever? But I think that's also a good, approach.
to have it, like, when someone opens a PR, or issue, or, like, somehow interact with GitHub, or with the data sources, where the contributions count towards.
**Juliano Costa | Datadog** 17:30 Yeah, I think they have… some… rules in GitDM that not everyone is in there. Like, if it's a one-off contribution, and the person won't be active, they not even add the person there.
But maybe… maybe… Maybe we should have a process of, like, Yeah, I don't know, I don't know.
And also, I don't understand the structure of the page, because… like, get the, let me open it here again. We have… 10 files, developers underscore affiliations. We have 1 to 10.
So, and they are not alphabetically ordered. So, what is the point of having 10? Like… What is this? Why?
You know? Like, why don't we have one without everything? Yeah, this fight would be too big, okay? Then… How we split.
**Johanna Öjeling** 18:38 Yeah.
**Juliano Costa | Datadog** 18:39 Yeah.
**Johanna Öjeling** 18:40 Yeah… Who is starting on this?
**Juliano Costa | Datadog** 18:49 new affiliations are important for… into DevStats about once per 4 weeks. This is what they say on their README. But on their README, they also… they also say, developer's affiliations list, Dev1, Dev2, Dev3, Dev4, Dev 5, but there is actually 6, 7, 8, 9, and 10, so 5 is missing.
**Johanna Öjeling** 19:13 Oh.
**Juliano Costa | Datadog** 19:18 Yeah, I don't know, how to… how to… How to approach that.
But maybe I'll just raise on the Hotel Maintainers channel and see what they say, and, yeah.
Yeah. And.
**Johanna Öjeling** 19:44 I think that that can be a good starting point, and yeah.
But yeah, I think you're raising a valid point.
**Juliano Costa | Datadog** 19:56 I…
**Johanna Öjeling** 19:57 And I know also Marilla, I looked into this.
probably recently, to see if she could find, like, a better way to represent, since there are, like, gaps, in… Yeah, that's… the stats are not accurate, and, like, not all CAR contributions count, so, Yeah, I know she was looking into it, and… But I'm not sure where she's at.
**Juliano Costa | Datadog** 20:28 There is a… an issue open with, report issue Grafana. I don't know who created it, let's see.
No. It's just, yeah, no, it's not.
Not related to Grafana at all.
I mean, I think it is, but not, like, any dashboard or whatever, or contributions per company.
It's just… Yeah.
Anyways… What I… okay, so what I actually want to discuss with you… Is… Did we hear back from… from the… the contributor that wanted to… to write, one of the…
**Johanna Öjeling** 21:30 Yes, the Atlassian one.
**Juliano Costa | Datadog** 21:32 Classiness.
**Johanna Öjeling** 21:34 And I gave her access to the… Collector blog posts?
Google Doc. So she… I've… She has started to write, in that document, like, an introduction, or maybe she just copied, but I saw that she has, yeah, started to interact with documents, yeah.
**Juliano Costa | Datadog** 22:03 Okay, cool. Okay, so let's lay out, let's see.
**Johanna Öjeling** 22:07 And then, actually, there was… In the Slack thread… where I tagged her.
Last week, Dan Gomez Blanco wrote also that since the blueprints and reference implementations now are underway, and they are published. It would be good if this blog post could Gonna follow that.
format, or, yeah, if she could read through the, kind of guidance, and then she, yeah, she said, I'll take a look at it then. There's a link to that message here.
And I saw the other day, maybe yesterday, there was a blog post going out about blueprints and reference implementations.
So that's nice, hopefully it will, nudge more organizations to take a look there and to contribute.
**Juliano Costa | Datadog** 23:22 Okay.
Oh…
**Johanna Öjeling** 23:30 But then, the growth… So… Yeah, finally… the person at Grok Kelly replied to the email, and then I responded with… Yeah, could she please take a look? But then, I didn't hear back from her, so…
**Juliano Costa | Datadog** 23:56 Okay.
Cool.
Park, not Cooper, yeah.
**Johanna Öjeling** 24:02 But yeah, I'll, I'll give her some more time otherwise. I'll send another email and follow up.
**Juliano Costa | Datadog** 24:15 Okay.
Yeah, and I… from the… from your meeting notes agenda… agenda here, I just realized that I need to go back to the telemetry level and detail it.
Yeah, sorry.
**Johanna Öjeling** 24:29 Oh yeah, no worries, no, I didn't, write the full, I just started, yeah, to summarize, you know.
Being dangerous.
And yeah, I created a tab here in this document. I don't know if we wanted to live elsewhere, but yeah.
Just to have a place to work in.
**Juliano Costa | Datadog** 24:51 Nice.
Nice, nice.
**Johanna Öjeling** 24:54 on that, too. But yeah, since I'll be out of office, maybe it will… Take another.
**Juliano Costa | Datadog** 25:00 Yeah, I will also post on the channel that, next week I… I won't be here, next week I'll be in Hamburg.
So I don't be able to join.
So, if you are out and not, maybe we should… should just skip, if Perk and Tristan are not charging that.
Just a realtor.
**Johanna Öjeling** 25:24 -
**Juliano Costa | Datadog** 25:26 I'll post here.
Okay.
**Johanna Öjeling** 25:28 Thank you.
**Juliano Costa | Datadog** 26:13 It's baconess.
Sweet.
Cool.
Ticket.
**Johanna Öjeling** 26:38 Thank you.
**Juliano Costa | Datadog** 26:38 Big Budd.
**Johanna Öjeling** 26:39 estate.
**Juliano Costa | Datadog** 26:39 I think we are good then.
**Johanna Öjeling** 26:41 Yep!
**Juliano Costa | Datadog** 26:42 Oh, boy.
**Johanna Öjeling** 26:45 the lawyer, and so on.
**Juliano Costa | Datadog** 26:47 bidding?
**Johanna Öjeling** 26:48 Yep, enjoy your holiday.
**Juliano Costa | Datadog** 26:51 And, your birthday?
**Johanna Öjeling** 26:53 Thank you.
**Juliano Costa | Datadog** 26:54 And see you in two weeks.
**Johanna Öjeling** 26:57 Yep.
G'day. Hi.
