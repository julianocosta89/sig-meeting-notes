SIG: SIG Security
Date: 2026-09-14
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Reiley Yang (Microsoft Corporation)** 00:33 Hey, Marnie.
Can you hear me?
**Martin Costello (Raintank, Inc. – Grafana Labs)** 00:42 Sorry, I was on double mute.
**Reiley Yang (Microsoft Corporation)** 00:45 Hey, how are you?
**Martin Costello (Raintank, Inc. – Grafana Labs)** 00:47 Oh, good, thanks, how are you?
**Reiley Yang (Microsoft Corporation)** 00:56 Thanks for joining. I probably need to talk to you and see how we can help.
Yeah, let's give a minute for folks to try.
I'll share my screen. Let me know if you can see it.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 01:18 Yep.
**Reiley Yang (Microsoft Corporation)** 01:23 Okay, while we're waiting, I… I guess, like, Trask and Jonathon normally would join.
For one thing, I've been with him.
In the past couple weeks, is we… instead of, like, a corporate, where we can force certain repositories to do certain things, OpenTelemetry is a, like, open source product, so… at least from security's sake, we don't have any enforcement. I think the GC might have some at some moment, but we decided not to take that approach. So, what I did here… is I have a proposal. These are the different levels of expectations for security. So you see, like, they're, like, starting by default has no expectation. Then we ask each repository to declare what expectation do they set. So a repository maintainer can say, like.
We promise that we meet the medium expectation. Then we help the users to understand What they can get from this repository.
So this is the proposal, and my hope is I want to get the initial feedback. If there's any, like, big no, then I wouldn't go to the maintainers meeting tomorrow and share this. If people think this is generally a good direction, but there are details we need to polish, then I'll send this to a broader, like, audience for feedback.
So this is my main goal for this meeting.
**Trask Stalnaker (Microsoft Corporation)** 02:55 Cool, shall we take 5 or 10 minutes to read it?
**Reiley Yang (Microsoft Corporation)** 03:01 Sure.
I guess that's the only topic I have, unless anyone has additional topics.
Yeah, I, I can just, Go through that in the share screen, if that's easier.
**Trask Stalnaker (Microsoft Corporation)** 03:21 Sure.
**Reiley Yang (Microsoft Corporation)** 03:23 Okay, so, first I try to explain, like, OpenTelemetry is large, so we don't try to do it centrally. We define the standard, and we let each repository take care of themselves. And here, the maintainers should be accountable.
And this will be only applicable for all the public repositories. I know we have some private ones, so it… like, I think private one also needs security, but I… I don't think I'm going to cover it here, at least for now.
And, like, as a default, all the repositories start with no clear expectation. So this is, like, when they didn't do anything, or they clarify there's no expectation, then it's no expectation.
Then, low expectation, we start to have certain, like, concrete items. So I try to think about, like, do we trust the people there? Do we trust the communication there? Do we trust the CICD? Do we trust the code? Do we trust the dependency? Do we trust how artifacts are being published? And do we trust that when something happened.
we will be able to have the maintainers taking the lead and fix the problem. So with that, I think the first thing is about the communication. Like, previously we had the issue where people tried to reach out to maintainers on Slack, but they reach out to people who have the same name. So, when I did this for the TC and GC, you can see all the Slack member ID. I'm gonna do this for this… As well. So if we, like, in this group, if we think that, like, we agree on this, I'm going to start by setting low expectations for this repository. I'm going to create exactly what I described here, just to demonstrate how it works today.
And here, I want to make sure, like, we allow people to create security advisories and public issues.
I, I didn't try to ask, try to call out, like, for people who have been banned, because I know there are people who use spouse and do the, like.
prompt injection, or they try to, like, violate something, but I don't think that detail should be called out here. So, for security advisory, this is typically, like, people realize you have an issue, but they also understand that not many people would understand this.
So they probably, like, look at the code, or they probably discover some pattern of attack. They try to reach out to you secretly. This is self-advisory. Public issue, I think there are cases, I've seen a lot, people reach out saying, hey, like, Reiley, I'm using this OpenTelemetry Go SDK XYZ, and I have this dependency.
On something that hadn't been fixed for a long time, so… I've seen either people reach out to me, and I'll tell them, go and reach out to the maintainers, create a public issue. Or, you go and just fix that, send a PR. So, these are very public information. Anyone can just run a scanner and see that.
So, even if people file advisory, I think we'll just turn the advisory into an issue, and actually we have a Python script here. So, I want… I want us to be very clear about, like, any security thing that everyone can just easily run a scanner, be able to reproduce, should become a public issue, or should just be a PR without an issue.
then anything secret should be a security advisory. And… Also, I'm asking each repository to contain a top-level security.markdown file, and I'll create an example for people to get started before I present to the maintainers. And the top-level README file should have a security section which points to the security file, and the security file would explain.
what are we shaping from this repository? Like, it could be we shape those reusable libraries, we shape those binaries, or we actually host a service, or, like, OpenTelemetry.io website. I've seen the issue where people reach out saying, Opentelemetry.io website has a… expired cert or something, or, like, the search chain has been revoked, you gotta do something. So I… I think for all the artifact services and websites, whatever thing that we as OpenTelemetry maintains, we need to be accountable, and I want to use repository as the direct source.
Okay, I'll take a pause here. Any questions so far?
**Trask Stalnaker (Microsoft Corporation)** 07:23 I have a question about the top-level security MD file.
Today, we have the security md file in the .github repo.
In the org, which basically, then, everybody inherits that.
So is that what you mean here, or you mean that… Repositories should have their own copy, which talks about… maybe adds more details.
**Reiley Yang (Microsoft Corporation)** 07:55 I want them to have more details. Having a shared one is okay, but I think the shared one should point to some repository-specific thing. Like, the repository should declare what level they're trying to meet, right? A repository can see, like, don't expect me to do anything. I'm just, like, very new here, I'm exploring.
So, like, don't use anything from me in production.
if I… I can't imagine how having, like, a global security file would help that.
If there's a way.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 08:26 training mode.
**Reiley Yang (Microsoft Corporation)** 08:26 We can have the generic thing, and then say, this is the repository-specific thing you can check. That would be great.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 08:34 That's probably better, because I was going to say the same thing as Trask, because that on the .NET SDK right now, there is a security tab, because it's just inheriting the global one. So if we added a custom one that just said.
what that says. It would actually be less useful, because you have to… it would replace all the content, and then you'd have to click a link to go somewhere else to read everything, or you'd have to duplicate it all just to add one sentence to go, oh, by the way, we're a medium.
**Reiley Yang (Microsoft Corporation)** 09:07 Yeah, so for the repository-specific things, I think what we need is, for each repository, we need to give a laundry list of all the things they need to be accountable for.
Like, the… the artifacts. And I… I don't necessarily think.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 09:20 Could this…
**Reiley Yang (Microsoft Corporation)** 09:21 It has to be in the security file. It needs to be somewhere.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 09:24 Can it overlap with the… I forget where it is now in the repo, because it's moved. The CLO monitor stuff, because when I built the YAML file for that, I had to enumerate what the names of all the packages were.
**Reiley Yang (Microsoft Corporation)** 09:38 Yeah.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 09:38 So… You could potentially, sort of, have the global security file, have a section in it which tells you where to find repository-specific things, and then if they're there, they're there, and if they aren't, they aren't.
**Reiley Yang (Microsoft Corporation)** 09:53 Yeah, that'd be great. And also, like, listing all the artifacts don't have to be security, right? There can be many other purposes.
So, that'll be great.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 10:03 Oh, I found the file now. It's in… for the .NET repo, at least. It's in .githubsecurityinsights.yaml.
And there's a load of stuff in there.
**Reiley Yang (Microsoft Corporation)** 10:13 Okay, then I'll, I'll, I'll go, like, for the art.
**Trask Stalnaker (Microsoft Corporation)** 10:17 Yeah, and I think it would be helpful when maybe taking the proposal broader, like you were saying to do it in the SIG security repo itself.
But I think it would be… might be more helpful to have it done in a… in a real repo that publishes things and has real dependencies.
So that we can see how these things play out.
**Reiley Yang (Microsoft Corporation)** 10:43 Yeah.
Okay, I'll continue.
And I think this probably fits for the .GitHub security, like, how to distinguish a security issue versus a security advisory.
So, this is something I can work on.
**Trask Stalnaker (Microsoft Corporation)** 10:59 And I think we could, I mean, if we think that it's the best… like, user, experience. I mean, we can, have copies of SecurityMD, which, you know, have a specific section, and then we can have a, you know, a script workflow that synchronizes our global one to, like, a section at the bottom of that, or something like that.
**Reiley Yang (Microsoft Corporation)** 11:25 Yeah.
Yeah, then the last one is obvious, so we called, that's low expectation here, a link to this section.
And, for medium one, meet all the low expectations, or above.
And then I want all the gates.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 11:41 To have access to… Just a minor point, is that, how can you exceed A finite set of requirements.
**Reiley Yang (Microsoft Corporation)** 11:52 Sorry?
**Martin Costello (Raintank, Inc. – Grafana Labs)** 11:53 How could you be judged to be exceeding low?
**Reiley Yang (Microsoft Corporation)** 11:58 Oh, exceeding low, that means you meet everything, but here, for example, if we see something, like, you must fix this issue within 7 days, then you're saying, but I fix that in 5 days, then you exceed.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 12:10 Oh, I would treat that as meeting.
I would interpret that as meeting, because it was what I… I did what I had… the thing said I had to do.
**Jonathon Klobucar** 12:22 Yeah, I would say unless you're still getting really advanced, like, don't… just… it's either meat or doesn't meet. Don't try to have, like.
an XSEED thing, because, like, if you've got.
**Reiley Yang (Microsoft Corporation)** 12:32 I see.
**Jonathon Klobucar** 12:32 7 days, and someone does it in 5, like… Yeah, it means that we're meeting our commitments, and sort of just leave it at that.
**Reiley Yang (Microsoft Corporation)** 12:41 Yeah, this is probably me being contentic about English, so this one said he must say you meet low expectation. But here, we're saying you don't say you meet low expectation, you say you meet medium, so it's like you meet everything above.
**Jonathon Klobucar** 12:56 Fair enough.
**Reiley Yang (Microsoft Corporation)** 12:56 this one.
Hot…
**Martin Costello (Raintank, Inc. – Grafana Labs)** 12:59 Oh, yeah.
**Reiley Yang (Microsoft Corporation)** 13:00 Perfect.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 13:00 I get that, I just say, you meet all the criteria in the low section above.
**Reiley Yang (Microsoft Corporation)** 13:06 I see. Okay.
Yeah. Since I'm presenting, if you can just make a quick comment there, I'll just go and make the change after that discussion. Okay, so I'll continue. So, this one, we start to care about CICDs. We want all the GitHub actions to be pinged.
And any fix should be handled within 7 days. I think this is a pretty reasonable thing, because most of them, they're automated, and I haven't seen cases where you have a dependency.
**Jonathon Klobucar** 13:35 Can we… can we require, instead of using PIN and Insecure, that they… they pass the Zizemore audit?
that will… that will make things easier, because, like, Zizmoor will tell you what's not passing, and, like, we don't have to spell it out, it'll just be, like, must pass, like, Zizmoor.
**Reiley Yang (Microsoft Corporation)** 13:56 I… Like, here's… I'm on the fence. I want to give people best practice, but I don't want to dictate on which tool they use.
win.
**Jonathon Klobucar** 14:07 if you… if you… if you use Dismore and tell Claude to fix Zizmor findings, it'll fix it very quickly, and, like, everything's just… you're gonna… you're gonna just prevent a lot of security problems.
**Reiley Yang (Microsoft Corporation)** 14:17 Yeah, they're dependent about… there's, like, Renovate, there are many other tools, so do we want to…
**Jonathon Klobucar** 14:22 That doesn't matter, because this is more like, just audits the GitHub action flow itself, right? Like, it'll work.
**Reiley Yang (Microsoft Corporation)** 14:31 Okay.
**Trask Stalnaker (Microsoft Corporation)** 14:31 Reiley, Zizmoor is the one that I've been rolling out to all the repos.
**Reiley Yang (Microsoft Corporation)** 14:35 I remember, but do you want to dictate on this one? I mean, I'm…
**Jonathon Klobucar** 14:41 A number of security problems, because people haven't… audited their GitHub Actions, where a pull request target is, like, done stuff and other things that, like, I think… I think when you hit medium, that makes sense.
Otherwise, you, like, might have, you know.
to deal with security. I feel it's a low-hanging fruit, but I can differ off of that.
**Reiley Yang (Microsoft Corporation)** 15:01 Okay, I had a comment there, I'll address that.
**Jonathon Klobucar** 15:04 Yeah, yeah, no problem.
I'm not asking for pedantic mode with CISMOR, I'm just asking, like, it passes the normal CISMOR audit, which should be pretty good.
**Trask Stalnaker (Microsoft Corporation)** 15:13 I'm kind of in favor of, where we have… clear tooling.
That recommendation, like, that makes things easier for the maintainers.
It's like, maintainers are looking for the easy button, right? It's like, okay, I just… I need to make this tool pass. Check.
**Jonathon Klobucar** 15:33 Yeah.
**Reiley Yang (Microsoft Corporation)** 15:35 Yeah, sounds good.
**Jonathon Klobucar** 15:36 Yeah, yeah, I prom… yeah, and I promise from experience, it's, like, not a… it's not a… the heaviest lift. Like, I'm not asking for, like.
you know, it has to pass, like, in Python, it has to pass, like, tie-type checking and other stuff, I'm just… yeah.
**Reiley Yang (Microsoft Corporation)** 15:51 Yeah.
This is awesome. So you helped me to solve a problem.
**Jonathon Klobucar** 15:55 Yeah, I can write even the instructions on how to, like, run it against GitHub Actions as, like, a pull request for this, if you want, of, like, how to use it.
**Trask Stalnaker (Microsoft Corporation)** 16:05 So, Jonathon, I've been… I'll link you the… there's a SIG security issue, open. I've been rolling it out to all the repos.
Oh, cool. I think I'm at, like, let's see what I'm at. I'm at 51 out of 83 repos so far. Oh, nice.
**Jonathon Klobucar** 16:24 Yeah, I'm happy to help with some of that, now that I'm not, sick with pneumonia. So, if you want some help, let me know.
**Trask Stalnaker (Microsoft Corporation)** 16:31 Cool. I've got a bot that I've been babysitting, it's starting to get a little more annoying with some of… the easy ones were easy, and then the medium ones were… required a little more babysitting, and now the hard ones are requiring yet more babysitting.
**Jonathon Klobucar** 16:47 Oh, for sure.
**Trask Stalnaker (Microsoft Corporation)** 16:48 Yeah, I might ping you.
**Jonathon Klobucar** 16:50 Cool, sounds good, man. I would love to talk about this. Yeah, I've done a lot of these, just because usually when I go to a company, one of the first things I have to do is, like.
tighten up our CICD, and that's, like, kind of step zero to one.
**Reiley Yang (Microsoft Corporation)** 17:04 Okay, nice.
And this, this is the only thing I dictate in this PR. So, so Trask and I worked on this, like, a simple dashboard, so we collect each repository, and there…
**Jonathon Klobucar** 17:16 Oh, nice.
**Reiley Yang (Microsoft Corporation)** 17:17 SSF score. So when I look at that, I think the color coding is you have a deeper green if you ever reach, like, 8.0 or above. So here, for medium, I set as 8. When I look at that, I think it's pretty reasonable.
**Jonathon Klobucar** 17:36 So…
**Reiley Yang (Microsoft Corporation)** 17:39 Anyways, so if you… if you want to argue on the number, we can take it,
**Jonathon Klobucar** 17:43 I think, I think, I think mediums are 8s, and I think Zizmo and everything else will get you there pretty easily, so that's good.
That's great.
**Reiley Yang (Microsoft Corporation)** 17:51 And then… and then I want to avoid any individual maintainer just go and make any production change, like, release anything. So, like, we require at least one additional approval from the maintainer or approver.
I think this is suitable, but I… I guess it might need…
**Martin Costello (Raintank, Inc. – Grafana Labs)** 18:08 I feel this one's maybe getting into the realm of high.
**Trask Stalnaker (Microsoft Corporation)** 18:12 Yeah, good.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 18:13 for the release process we have for .NET at the moment, is we agree we're going to do it, and then you create an issue, and then PRs happen, and if… otherwise, it's going to be like some sort of thing with a movie with two keys.
to try and do a .NET release, it would take hours and hours and hours.
If we need two people to countermand everything.
**Jonathon Klobucar** 18:33 Is it possible on Medium, not to say that it requires another maintainer, but, like, it's, it's, the release process is through a GitHub action? Or is that getting it high? Like, I think that's, like.
**Trask Stalnaker (Microsoft Corporation)** 18:45 Yeah, it shouldn't be run locally.
**Jonathon Klobucar** 18:48 Yeah, I think, like, that's… like, build artifacts.
**Trask Stalnaker (Microsoft Corporation)** 18:50 Audible. Auditable.
**Jonathon Klobucar** 18:52 auditable and created, and then high can be the… the one… it requires at least one person to… to click approve besides someone else of that machine artifact.
**Reiley Yang (Microsoft Corporation)** 19:02 Yeah, sounds better. Can you make a comment?
**Jonathon Klobucar** 19:05 Yeah, I'll definitely do that.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 19:06 Shop.
**Jonathon Klobucar** 19:07 Yeah. Because, like, I do think that, like, medium, it's like, you should make machine artifacts, then high is like, okay, now… now I want two people to bless those machine artifacts.
Which I think, yeah, cool.
**Reiley Yang (Microsoft Corporation)** 19:18 I do have one thing that I've been fighting with myself, so I know that there are several projects where the maintainers have their personal, or whatever, their email account associated with some, like, artifact repository, like Maven Central or.
**Jonathon Klobucar** 19:34 Yes.
**Reiley Yang (Microsoft Corporation)** 19:34 for something. That means they can just, like, create whatever binary they have and call that OpenTelemetry.net as they can publish that. And I… I don't think they will have a perfect solution unless the… the repos… like, the… the new guide repo, or whatever, the tool.
Has a mechanism for that, so… so that would make them, like.
like, medium by default, so any.
**Jonathon Klobucar** 19:58 Yeah, I was gonna… we had talked about it, like, when I was sort of… when Charlie came on and was sort of… I was sort of starting, but, like, there may be something worth that if you… if you're becoming a maintainer.
We require you to get, like, an open telemetry email through, like, our Google Workspace, so that, like, your personality doesn't get popped or whatever. We can enforce 2FA on email and all sorts of stuff.
**Reiley Yang (Microsoft Corporation)** 20:21 You want this to be a high instead of medium, right?
**Jonathon Klobucar** 20:24 Yeah, yeah, yeah, I was gonna say on high, yeah, the two main target would be for high.
**Reiley Yang (Microsoft Corporation)** 20:28 Yeah.
**Jonathon Klobucar** 20:29 And then we can work out later if it's advantageous to try to go ask Google for a… Google Workspace from our email domain to give to maintainers that, like, if you're a maintainer, you must use this for, like.
You know?
GitHub SSO and everything.
**Trask Stalnaker (Microsoft Corporation)** 20:45 We do have a Google Domain… a Google Workspace, but each named user costs money, and so we have to…
**Jonathon Klobucar** 20:54 Yeah, I was trying to figure out if we could find a way to get them to donate, but Google's a little less… a little more frugal these days.
**Trask Stalnaker (Microsoft Corporation)** 21:01 Oh, they're also, yeah, enormous, so, like, it's hard to get, like, little exceptions.
**Jonathon Klobucar** 21:05 Yeah, for sure.
We'll figure something out eventually.
**Reiley Yang (Microsoft Corporation)** 21:10 For this one, I was a little bit vague, but what I'm really thinking is I want each repository to have a way for people to create… For people to create issues with a clear security tag.
That…
**Jonathon Klobucar** 21:25 Yeah, so… so there's two ways to create security advisors, right? Like, we should make sure that people, if they think it's… if they think it's a security issue, they should create a GHAS, right? Sorry, GHSA or whatever, security advisory. When in doubt, do that, and then, like, someone can always triage it over.
**Reiley Yang (Microsoft Corporation)** 21:45 Right.
And then for the more public one, like, I'm already saying you use an outdated package dependency, and I'm just trying to send a PR, but you require me to create an issue, so I'm just creating an issue. Yeah. And for that issue, I… I don't want those issues and PR to be ignored for many days.
**Jonathon Klobucar** 22:06 No.
We should figure out if there's a way to… To have, a way for something to take a first pass with, like, an AI to be like, what type… like, what to tag this issue as, right? Like, that would be helpful, but, like, we gotta… we gotta walk before we… we gotta crawl before we can walk on that one.
**Reiley Yang (Microsoft Corporation)** 22:24 Yeah, so… so Trask probably needs some of your help. Like, I… I don't want to dictate things in this talk, but I personally would prefer that we have a… like, an explicit issue template, let's say any security issue, and in the issue template, we should also say, if this is something sensitive, then you shouldn't go ahead and create the issue. You should go to security and advisory inside.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 22:49 You might already have that, let me check.
**Reiley Yang (Microsoft Corporation)** 22:53 We don't do it consistently, so I… like, I have my personal preference, but should we push.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 22:59 Because I'm not sure what makes it happen, but if I click on New Issue in the .NET SDK, and the template form pops up, the fourth item in the list is report a security vulnerability, and it links off.
To the security policy.
**Reiley Yang (Microsoft Corporation)** 23:12 If you look at the history, that's what I created, so I'm advocating for what I would prefer to do as a maintainer, but I don't know if maintainers would all agree with me.
**Jonathon Klobucar** 23:24 I would also say, based on some experience where I submitted a GitHub security issue that, We should… we should add some stuff in there on, like, what follow-up looks like, because, like, it got… it got fixed, but then, as the reporter, I had to go and figure out, like, did it get merged and released and stuff, and that was, like, not great.
And so we can add some stuff.
We can add some stuff to, like, medium and high on, like, your… like, what the lifecycle of a security issue looks like in full.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 23:55 I, also, I don't know what the top-level process is for, like, dealing with the security reports, but… within the UK, at 3 days, if someone reported something at, like, 5.01 on a Friday, and all of the American maintainers on… or on holiday vacation, then there's… and there was a bank holiday in the UK on Monday, then that would be 4 days until someone saw it.
**Jonathon Klobucar** 24:22 I would say that it's a minimum… maximum of 3 business days.
Not 3.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 24:28 That's a better way to phrase it.
**Reiley Yang (Microsoft Corporation)** 24:30 I fought with myself a lot when I wrote this, so 3 business days is hard to define, because as a user, you don't know Where the maintainers are working from.
Their business…
**Jonathon Klobucar** 24:42 Five.
that's totally fine, like, it's… it's, like, I… I always put, like, for my Corbett Bounty and security reporting, like, stuff, it's always business days, and, like, it gives you the flexibility to be, like, like, yes, in our case, we're kind of a little bit interestingly distributed, but, like.
it's pretty acknowledged, at least in most worldwide places, that either you have Friday, Saturday off, or Saturday, Sunday, like, it's… I think it's fine to say business. If you put a 72-hour clock on this, like, you're now asking people that they have to… they have to do stuff on weekends and outside of normal hours.
**Reiley Yang (Microsoft Corporation)** 25:18 No, I'm not saying that. I'm asking if you have people that are, like, all sitting in one time zone, then your repository is at danger. You should at least have someone who's working from a different time zone, and they have different.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 25:33 Oh, yeah, yeah.
But I…
**Jonathon Klobucar** 25:35 agree.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 25:36 Yeah, I'm saying, like, in .NET, all the maintainers are in two time zones, Pacific… no, three. Pacific, UK, and Europe. But also, they go on vacation, and, like, 50% of the maintainers have been off all summer.
So, once you add in time zones.
If it's the wrong time of year, because it's Christmas or whatever, then suddenly that gets a bit difficult.
If it's 3… if it's 72 hours, not 3 business days.
**Reiley Yang (Microsoft Corporation)** 26:06 Yeah, then I think you should feel comfortable saying, I cannot meet medium expectation, I'm looking for help, my expectation is low. Because during Christmas, there are commercial, like, websites being attacked, then they need some fix, and if OpenTelemetry is not doing that, we better be very clear.
**Jonathon Klobucar** 26:24 The difference is, is that all those people are, like… so I run these sorts of programs. For those, there's, like, an on-call schedule that's usually, you know.
a salary is attached. I think we have to, like, be somewhere in between. Like, I think at high, maybe you can be, like, it's 72 hours, but, like, medium, like, 3 business days is where, like, I think you can start, right? Like, if it is critical to open telemetry.
Someone is going to see it. It might even be the technical committee at that point for high expectation stuff, but, like.
**Reiley Yang (Microsoft Corporation)** 26:55 I see.
**Jonathon Klobucar** 26:56 I think for Medium, like, you have to… you have to relax it just a little bit, just because, like.
To his point, like, they're usually a smaller maintainer group, where there's… Now if it goes… now, if it goes more than 3 business days, then we can have some discussions, and I think that that's when you can be like, how do we get these maintainers more help? But it's largely volunteer-based.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 27:16 Also, as written right now, it's, like, all of them.
it's not, like, important ones. Like, I understand that you can't know what the severity is until it's been looked at.
But it's sort of bucketing everything in, like, this… what you would expect to pay for level of support, which is not what Hotel has.
Because you might be… the way you end up writing this is, like, no one can meet Medium.
Everyone's on low, because The structure isn't there to actually support medium and high.
It's good to have it as a goal, but then it might be a bit self-defeating to then point out that no one can meet it.
**Reiley Yang (Microsoft Corporation)** 27:58 You know, then I also feel it's probably fine for open telemetry to say we have low expectation, because we don't really have that side hug or the motivation.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 28:08 Slightly…
**Reiley Yang (Microsoft Corporation)** 28:09 Probably lower than most corporate expectations.
You see, average corporate expectation is medium, then open telemetry is low. I think that's very fair.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 28:20 Slight aside, I don't want to bikeshed on what term to use instead. I'm not a fan of saying expectation, because sort of culturally, to me, low expectations means I think someone's really bad at something.
I have low expectations of this person, because they never do anything. And I think it's making it sound like you're… you think they're all bad, rather than they just aren't reaching the heights of best practice.
**Reiley Yang (Microsoft Corporation)** 28:52 Yeah, and I do think so.
And this is why I choose those fours. I've been fighting a lot with myself on those.
**Jonathon Klobucar** 29:00 Yeah, we can, we can figure out how to, like… like, we can pay a preamble about, like, where we… we want, you know, I think… I think, like, looking at this, Reiley, I would say that, like.
We would really love most of our repositories to be medium, and our priority ones to be high, and low is, like, you're incubating, and kind of like… but we can reword it to be, like, the language to sort of describe What… what a low expectation, like… low expectation repo looks like versus medium, and then put some words around it, too, to be like, you know, medium is where we expect, like, 80% of our stuff to sit, and, like, we expect, like, 10% in low and 10% in high or something, right? Or maybe it's 50% and medium, but we can… we can set these goals, and then… you know, sort of try to evaluate the bell curve a bit on where we think people… like, I would love everyone to be high, but I know that, like.
if I have, like, a barely used hotel implementation, like.
Maintaining high is gonna be a lot of work.
But I'd love to move, you know, get up to that point.
**Reiley Yang (Microsoft Corporation)** 30:03 This is great.
**Jonathon Klobucar** 30:05 I want to say thank you for putting this together. I'm not trying to tear it all apart. I think that there's a lot of really good stuff in here.
**Reiley Yang (Microsoft Corporation)** 30:11 No, this is great feedback. This is exactly, like, I always fight with myself a lot, but I think your feedback is helping me to come with something neutral. By the way, I haven't mentioned, sorry for that, I have a hard stop now, so…
**Jonathon Klobucar** 30:26 Don't worry.
**Reiley Yang (Microsoft Corporation)** 30:27 But I think we went through all the major topics, and for the thing I haven't finished, all these are, like, day's numbers, so we can debate forever. I would encourage everyone to put your thoughts in the PR, and then I guess we probably need more time to hash out the right balance.
Like, I don't think… my goal is to have 80% of the existing repository meeting medium. If that's already there, then we should dismiss the SIG, because we're done.
**Jonathon Klobucar** 30:57 No, I don't think we're…
**Reiley Yang (Microsoft Corporation)** 30:57 Upstates are long.
**Jonathon Klobucar** 31:01 I don't think we want, like, a low… you know.
**Trask Stalnaker (Microsoft Corporation)** 31:04 No, I think we want it to be achievable for 80% of the SIGs.
**Reiley Yang (Microsoft Corporation)** 31:09 Yeah, exactly.
**Jonathon Klobucar** 31:10 Exactly, yeah.
**Reiley Yang (Microsoft Corporation)** 31:12 Okay, I have to go. Thank you.
**Trask Stalnaker (Microsoft Corporation)** 31:14 Alright, y'all.
**Jonathon Klobucar** 31:15 Have a good day.
