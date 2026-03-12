SIG: Security Governance SIG
Date: 2025-07-21
Duration: 23 minutes
============================================================

## Zoom Recording Transcript

**Reiley Yang** 00:11 Hello, Jeremy!
**Jeremy Corley** 00:16 Hey! Hello!
**Reiley Yang** 00:41 Maybe give a minute for other folks to join.
I saw trust is still updating the agenda.
**Jeremy Corley** 00:50 Yeah.
**Reiley Yang** 01:43 Hey? Good morning, Trask.
**Trask Stalnaker** 01:46 Good morning!
**Reiley Yang** 01:51 Let's start. Can you see my screen.
**Trask Stalnaker** 01:55 Yes.
**Reiley Yang** 01:58 Okay, so we have 2 topics. Trust, we go first.st
**Trask Stalnaker** 02:02 Yeah. Just wanted to. Keep folks in the loop on kind of things that are in flight.
The minimum tokens token permissions.
Is moving along. The goal really is to eventually set the default permissions to read only for all the repos on I was going to. I had made a list of repos that had were ready for that and that I was going to apply this github setting but I'm going to postpone that for another couple of weeks, just because the minimum token permissions that were merged caused some workflow failures. And so I just wanna take a slightly conservative approach there, because once we set it to read, only then people won't be able to just simply roll back revert that change to get a local fix.
The second one. I just started working on I think it really ties into your topic, Riley. And here let me share my screen. I'll show you what I have and kind of what I'm envisioning there.
So I tested this on my test org.
So what I'm thinking, is having a private repo security advisors, advisories.
and basically it has a workflow that you know, runs once an hour, or whatever, and create thinks has a 1 to one mapping between open issues here and security advisories across the all the open Telemetry Repos.
so that you can. We can give the Tc. Or Security Maintainers on access to this repo.
and you can come in and see at a glance all the open, hot incidents.
And then we can.
Yeah, we can layer on. Then, I think, fairly easily. Escalations on these issues, like, if something has been open for X days. Then, you know, we can comment on it automatically. Comment on it. Escalate it, kind of drive it through github issues and then this would be as opposed to currently, we have the open telemetry private repo org because we couldn't have private repos before. But now we can. So we can get rid of this. And then this would basically take the place of the Grafana dashboard.
And what I like about this is that since so if if you watch this repo, then you, we can do escalations directly on the issues.
potentially, we could also do. Slack slack bot like, Hey, you have an escalated security issue kind of a thing. We do that with the stack. Overflow issues.
**Reiley Yang** 06:04 Yeah, this, sounds good.
**Jeremy Corley** 06:05 Is the is, is this able to pick up?
Oh, yeah, is this able to pick up the the advisories that have not been published.
**Trask Stalnaker** 06:18 Yes, yes, we have to give it a token that has rights to read them.
But it is a it will be a private lockdown repo. So I'm comfortable with that.
**Jeremy Corley** 06:31 Okay.
Okay, yeah. No. That sounds great. That sounds great.
**Reiley Yang** 06:37 I I always have a general question. What's in your mind about the the target audience of this Security advisory dashboard, or something?
I'll give you some context like, why I ask this question. So if you go to the Github Open telemetry organization and and you look at the the Security section.
**Trask Stalnaker** 07:07 Sorry. Tell me where.
**Reiley Yang** 07:09 Open climate trade org.
Yeah?
And you look at the org level security.
**Trask Stalnaker** 07:16 I'm worried that I don't know. If will that show any sensitive? I'm gonna stop sharing.
**Reiley Yang** 07:21 No.
So if you go to that security, you scroll down, you can see all the supply chain security issues.
For example, you might say, like open telemetry. Python. It has more than a hundred Cvs. And some of them have been there for a year, and even they're critical ones. So here's my understanding. If you have a repository and nobody is using that. Nobody is filing security advisory like issue, like they have to go to the tab to file security issue to you. But if nobody cares about it like nobody file issue, you still have critical dependency. That has Cve. Then this advisory dashboard we have today won't tell you anything.
**Trask Stalnaker** 08:03 Yeah, I I agree. This, this is the Advisory dashboard is very specifically for things that security advisories. But I agree that we need to tackle the other issue just as badly.
**Reiley Yang** 08:19 Yeah. And I always had a problem like, I've seen, issue has been there like critical issues, has been there for for a year. And then someone escalated. Then we see the advisory. So I I kind of feel this is probably the wrong approach.
Like I I I feel at least we should have a combined view with. If you have a repo ownership.
what are all the, all the supply chain security issues you have today, whether people report it or not.
plus the advisories that people reported, and for people like reported advisories there might be something that's considered sensitive, so we cannot share the detail before it got published. But for all the supply chain security issue, do you feel this is something we need to share and hold maintainers accountable.
**Trask Stalnaker** 09:13 I think we do need some kind of policy there.
I'm just trying to look at so like in the Java instrumentation repo. There, it says, there are.
20 open alerts.
12. I so let's see what those are.
So a bunch of them are. Code. Ql, like uncontrolled data used in path expression.
They're not dependencies.
Let me look at the dependent. Let me look at another repo. Maybe that has dependency alerts.
This one has dependabot alerts. Yeah, yeah, I think the Dependabot alerts are something that we should be watching and asking repo owners to work on.
**Reiley Yang** 10:38 Is that basically what the focus that you're thinking Riley, is specifically share. Let me share my desktop. So let me check. I don't have any sensitive information here.
Okay, so you submit that stuff.
**Trask Stalnaker** 10:55 Yeah.
**Reiley Yang** 10:57 Yeah. So, for example, like this one has critical security, vulnerability.
Well, there's no advisory. Maybe, like people just don't care about it.
Right? So I I feel we should combine this with advisory and have the single priority list, instead of having a dedicated dashboard for advisory.
and that that dashboard like the message. This is the single security dashboard that we think each product maintainer should prioritize. So we tell them explicitly from this sake, what are the things that are top on their list.
and we don't have to be perfect. Maybe we'll cover the the dependencies and the security advisories today. And later, we can add, maybe, Cicd, whatever, if there's a priority.
my, my worry is just like this one. Nobody cares about it right now, except for, like maybe the maintainers would care about that themselves, like Tc. Is not pushing people. Tc. Will just look at a dashboard which has partial information.
**Trask Stalnaker** 11:55 Yeah, I I think that's on this group to define kind of the expectation.
And create that view like, I don't think the Tc. I'm not even sure, like the Tc. Needs to be involved in the Security Advisory Review. Like, if we have a easy way, just mainly, my understanding is the Tc's involvement has been just to make sure things weren't getting ignored.
**Reiley Yang** 12:29 Yeah. Tc, are pinging the maintainers, but they only ping the containers for advisories. And if there's a security issue on the dependency, even if it's critical, even, it's for a year. Currently. Tc, is not doing that. And there's a huge gap.
**Trask Stalnaker** 12:44 Yeah.
So for the dependable for the critical alerts.
That you're showing those.
I'm not sure if those are public or not.
**Reiley Yang** 13:07 They are like, you can use any public analyzer. You just use whatever tool you can pop. You can capture this and publish in docker, and you just use a standard docker tool. It will give you the list of security, vulnerability.
**Trask Stalnaker** 13:19 Okay, Sue, I mean, that's the difference in terms of at least tracking between the 2, between advisories and dependency vulnerabilities.
**Reiley Yang** 13:34 Yep.
**Trask Stalnaker** 13:35 Is that the advisories we have to keep locked down, which is sort of why, I was thinking to have a you know, a place where only those are only there because it's gonna be super locked down.
**Reiley Yang** 13:53 Yeah, I I have a different idea. So maybe I would show the Maintainer. Here's a list of all the like. You remember, I I created an initial like dashboard in the security sake about the open Ss score. Right? So so like. I wonder if we want to have like a table, each repository. Then what are the security advisories? What are the critical, high, medium, low cves, and other columns, and in combination with how the Maintainer? If there's anything that you need to take action in 2 weeks. If there's anything that you have to take action in a month, then what are the thing that pass the due date. And this group can define the due date.
And and for for the the actual number, like people who don't have the permission with the click that they'll get nothing. We'll show them you don't have permission. But but I feel yeah place to show the Maintainer like, imagine you're a Maintainer every day. Maybe you care about. Is there anything I should worry about in the next 2 weeks, like, I probably need to publish a package. And another thing is, I notice, when the maintenance actually resolve whatever like advisory or the Cv. Is here, or the dependency problem.
it doesn't seem they have a clear guidance. What does the end mean? Like some? Some people would say, I already fixed the code. They ask like, Are you going to publish a new version the same.
We'll just like publish a new version every month. But this is critical. Are you going to publish an urgent fix or not? We don't know we need some guidance. So this is what I keep hearing.
**Trask Stalnaker** 15:30 Yeah, yeah.
**Reiley Yang** 15:30 Part is, once you publish a new version for the old version for people who are using that, how do they get notified?
So I won't have a like like the thing on, maybe on a single dashboard. So we we give this visibility to maintainers, and we tell them where they are currently it's scattered across the place, and for advisory Tc. Will ping them. But for for Cve dependency, nobody. Nobody is pushing that.
**Trask Stalnaker** 16:00 Yeah. So the question I have is, can that be public or not like, is it okay to have a public dashboard that lists that we have a critical advisory, an advisory open.
**Reiley Yang** 16:16 That part. I I don't know. Like we tell people there's an action item. We try to make it vague. We we don't tell how many security vulnerabilities you have? Would that be okay, or we should never share anything about it?
**Trask Stalnaker** 16:31 I don't know. I was.
**Jeremy Corley** 16:32 Or is there a way?
Oh, I was just thinking, is there a way where? If we had an automated tool that picked up these critical cde scans and then turned them into advisories right? So that so that the Maintainers are looking all in the same place because it in in the end.
you know, some of those could come through exactly like that right? Because if an external user goes, hey, there's a critical Cde in here. That's exactly what they're gonna do. They're gonna go in and and create an advisory for it.
So if we had a tool that could automatically go. Oh, you know, we scanned. We found 5 Cdes. We created advisories for them. Then you basically get the Maintainers looking in a single place for that And and if we did, at least for the criticals, right or or you know, and later, maybe we we tune it up to highs or something like that.
**Trask Stalnaker** 17:31 That would address the notification question that you were asking. Riley.
**Reiley Yang** 17:36 Yeah, that sounds sounds like a.
**Trask Stalnaker** 17:38 The user user notification.
**Reiley Yang** 17:41 Yep, then like.
**Jeremy Corley** 17:44 Now the-the-.
**Reiley Yang** 17:46 Then there's some kind of the one.
**Jeremy Corley** 17:49 Oh, sorry. I think there's a delay on my side.
yeah. And and and obviously the one wrinkle is figuring out, you know if if it's already been reported. But you know again they they have to deal with that anyhow, like users can multi report the same item, and they just have to go. Yeah, that's already covered and close it. But that's it.
**Reiley Yang** 18:14 Yeah, that sounds like a good idea to me. I have a small question for you, Jeremy. So, for example, if I have like 100 dependency issues.
I guess we probably need to file 100 independent advisories because we we want one issue, one like corresponding to one particular security item, right? You don't want to separate that and say, this issue, like 50% fixed.
Is that your understanding? Then.
**Jeremy Corley** 18:43 Yeah, generally. Yes.
cause cause you're particularly if those turn into you know where you're gonna actually publish your own Cve, you're gonna need separate Cbes for.
**Reiley Yang** 18:52 Yeah.
**Jeremy Corley** 18:53 Whichever issues, and all that.
**Reiley Yang** 18:55 Yeah, makes sense.
**Trask Stalnaker** 18:58 So would we only do critical.
**Reiley Yang** 19:05 I think the eventual.
**Jeremy Corley** 19:06 Place to start, yeah.
**Reiley Yang** 19:09 The eventual goal is to better. But starting from critical mix, critical and higher, I'll probably say.
**Trask Stalnaker** 19:18 Oh, yeah, those criticals.
Yeah, I'm looking at like, Evpf instrumentation. And the criticals are not dependency vulnerabilities. It's like other kinds of like analyze. Well, some of I guess cargo lock.
I don't really understand change.
**Reiley Yang** 19:58 The Javascript one seems a bit concerning I'm not a Javascript expert, but if you go to the open telemetry Gis, you can see some dependencies like.
**Trask Stalnaker** 20:09 And Github Github categorizes these things differently.
I feel like for maybe a re like like for a reason like.
And so I kind of.
I mean, I like the idea of having a dashboard, and and maybe we just need to lock that dashboard down.
To only maintainers access some.
**Reiley Yang** 20:43 A problem, because you probably don't want the Javascript Maintainers to see the critical issue from Donut. And this is why we have the Tc, doing this kind of like pinging people thing.
**Trask Stalnaker** 20:54 Yeah.
So I mean, if we have a say, we have a central private repo that only has, you know, secured like security maintainers access.
But we have the basically, we have an escalation where we know the slack usernames of the Maintainers. Or maybe even we open a public issue sane.
You have things to check.
**Jeremy Corley** 21:42 Well, if if the if we've auto filed them as advisories on the Repos, and the Maintainers will see the Advisories for their own repos.
And if people looking at that dashboard go, hey! This one's been sitting for a really long time.
And they are they by definition, would have the security manager role. They can actually go directly into the repo where that issue is, and they can comment on that advisory.
See, you know, see who's been commenting on it, and when it went, you know, when it went stale and say, Hey, what's going on with this advisory?
That there'd be should be ability to do that.
**Trask Stalnaker** 22:28 Oops. I just clicked on something that's going to create a Pr in the Evcf instrumentation to update one of them.
yeah, I guess what. The only reason I'm kind of hesitating on automatically creating security vulnerabilities is looking maybe we should go private, so we can share screens. So we.
**Reiley Yang** 23:01 Yeah, yeah.
**Trask Stalnaker** 23:02 Yeah, let's just jump. Since we're all on teams. Let's just jump over to teams or not recorded. Okay, see? It.
**Reiley Yang** 23:10 See you.
