SIG: SIG Security
Date: 2026-10-26
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Reiley Yang (Microsoft Corporation)** 01:38 Hey, Matthew.
**Matthew Spiekerman (New Relic, Inc.)** 01:44 Hey, Reiley, how's it going?
**Reiley Yang (Microsoft Corporation)** 01:46 Hey, good. How are you?
**Matthew Spiekerman (New Relic, Inc.)** 01:48 Pretty good.
**Reiley Yang (Microsoft Corporation)** 01:51 Let me share my screen.
You see my screen?
**Matthew Spiekerman (New Relic, Inc.)** 01:55 I can, yup.
**Reiley Yang (Microsoft Corporation)** 01:57 I normally don't see a lot of folks joining, so I'm glad that you… you joined.
I guess I haven't met you before.
**Matthew Spiekerman (New Relic, Inc.)** 02:06 Yeah, I'm brand new. I actually, just… Just found this over the weekend.
**Reiley Yang (Microsoft Corporation)** 02:15 Okay.
**Matthew Spiekerman (New Relic, Inc.)** 02:16 Yeah, I don't know if you want, like, a quick background on me, but yeah, I've, I've been working at New Relic for, about 8 months.
I'm new to observability as well.
But I dove in pretty… pretty fast to OpenTelemetry.
I did the OpenTelemetry Certified Associate certification through the Linux Foundation.
Just to get a better understanding of OpenTelemetry in general.
But before, before New Relic, I worked in cybersecurity for about a decade at Dow Chemical.
And so, my thought was, joining this group.
I could take a little bit of what I know in security and a little bit of, what I'm learning, or where I work now in observability, and kind of marry them together.
**Reiley Yang (Microsoft Corporation)** 03:07 Oh, this is awesome.
So, nice to meet you, and welcome. I've been in OpenTelemetry since day one, so serving the technical committee, and I kind of inherited the SIG security after the previous maintainers decided there's lack of traction, they wanted to step down.
So I'm… I'm still… holding the… the… how should I say the operational things here, making sure, like, we don't collapse, but I… I do wish that we can expand the… the SIG by having more people, and as you can see from from the SIG Security homepage. I think I'm the only maintainer, and Trask is the only approver, and both of us are from Microsoft.
**Matthew Spiekerman (New Relic, Inc.)** 03:57 I…
**Reiley Yang (Microsoft Corporation)** 03:57 I would wish to have more people here, but I… I also understand, like, this is more… more challenging than most of the SIGs. So, in this SIG, what we're trying to do is we try to define, like, procedures and processes, and helping OpenTelemetry to… Have better, like, help the maintainers to have better understanding about how to bring security to a good level.
And many of the challenges I'm facing here is because many maintainers, they're… they're not having this, like, fully paid job by their company to sponsor all the security work. They're like, hey, let's just make sure we contribute the features, and after that, who's going to patch the system? Who's going to look into the advisories? It's more like… more, like, community thing, so if you have time, you have interest, sure, go for that, but there's no… clear obligation. So, one thing I'm trying to do is to define the level of obligations inside an open source community, which you can imagine is a hard thing, so there has been a lot of back-and-forth thing, but I think I understand like, why this is hard. And… and I'm passionate about this space, because of two things. First is I… I think absorbability is very… common for all the software development, like, activities, so I couldn't even imagine if you have a software that you don't need observability. Then, if OpenTelemetry wants to become the, like, observability solution for most of the software, then I think it'll be ironic if we tell those, like, authors of the software, hey, by using OpenTelemetry, you will have better observability, but God knows whether you have security issues or not. We better tell them, hey, like, you can rely on us, we'll make sure we do a very reasonable job for security, and I think we should have a higher bar than most of the open source components, because the widespreading of the usage, things like that.
And… And another thing is, with the rise of AI, I think now it's, like, cheaper than ever for someone to, like, take a codebase or take an artifact and say, hey, can you just go and explore, give me a list of 100 security findings, and then maybe turn those into real attacks. So I feel if we don't do a… Good job, then we're falling behind, and then we'll be in a very bad situation where people don't have trust, because we cannot even do the basic security things.
So, this is where I'm coming from, and I… I think the SIG can give people a good opportunity if you have, like, security background, you want to help to drive this effort, because OpenTelemetry is big. Like, we have, like.
Reaches to so many different language ecosystems.
Or, for people who are running a security company, they can come and offer, like, free tools. We can negotiate and decide, hey, this is going to help OpenTelemetry. But ultimately, I think whatever finding, whatever things we reported, we need maintainers to take care of them, and… make sure, like, we patch them. This is why, like, in the past several months, we've been discussing about how to start.
the right bars, and… It is challenging.
Okay, so I'm hoping that you can help to influence New Relic to raise the… I guess New Relic also cares about security, and probably the level of interest might… like, increase due to all the… the… the climate that's ongoing. Hey.
**Matthew Spiekerman (New Relic, Inc.)** 07:39 Yeah, yeah, I think joining right now is an interesting time, right? If you think about last week, the PHP vulnerability, and just how… how, how front and center that combination of observability and security became. I know, So I have, a focus area in security within New Relic as well. So I meet with the product group, periodically, give them feedback on… we have a security capability called SecurityRx, but then again, more generically, just thinking about Security in the context of observability.
So… Yeah, I think there's a lot of shared interest between, you know, what's happening here and what, you know, the company I work for cares about as well.
**Reiley Yang (Microsoft Corporation)** 08:29 Cool Look forward for your contribution here.
And, so coming back to the topics, Trask all confess here, I've made some progress on that, on, on this PR.
I think I took most of the… The feedback, except for… I need to get back to you about this Java instrumentation, example, so I haven't done that yet.
**Trask Stalnaker (Microsoft Corporation)** 08:59 Oh, I think I marked it as… I thought you thumbs up it, and so I marked it as resolved.
**Reiley Yang (Microsoft Corporation)** 09:04 So I've done something, but I want to close that.
Yeah, and I also want to do the similar thing for OpenTelemetry Donna to be able to form a better understanding.
So, for this one, I've done another pass last week, and I think I cleared all the major comments, if you could take a look. And I saw one feedback from Robert that made me…
**Trask Stalnaker (Microsoft Corporation)** 09:29 I approved it. I'm, I'm… it's good to go from my perspective.
**Reiley Yang (Microsoft Corporation)** 09:34 Yeah, so… so Robert's feedback made me thinking, it… it seems like he… he was confused.
by the security… the virus and vulnerabilities. So, in this PR, I haven't put a lot of like, rigid bars on security advisories besides, like, we only want the maintainers to be proactively responding to those advisories. But how they fix that? We don't even know if the advisory is a real vulnerability or not, right? So, they can take the time negotiating with whoever reported that. They can take time, as long as the people who report that, they agree, they're not going to disclose that.
before a certain timeline. So that part, I think, is pretty flexible. But security vulnerabilities are either you have a dependency on something that has a known CVE registered, or you have this advisory, someone decided they're going to publish that. You already know the severity score. So, for those things, I think anyone can just, like, write a scanner on your software and know there's a vulnerability. So, it seems he… he has hesitation about the time where I think the confusion is he might… he might be treating vulnerability and advisories interchangeably, which, to me, they're two different concepts. So, I… I'm willing to add clarification, but not in this PR. I can send a follow-up PR to calls, these are different, but I want to check with you to see, like, if If that's clear to you, Or you also misunderstood my intention.
**Trask Stalnaker (Microsoft Corporation)** 11:14 Let's see… security advisories and issues will be acknowledged and updated, Sundays. All vulnerabilities are evaluated within 7 days of section.
So, by that, you are… so that line, like, I totally understand the security advisory line, the… all vulnerabilities… Do you mean… all, vulnerabilities in… Dependencies… can we say something a little bit more specific there by what, like, because vulnerabilities… Feels like a big umbrella term that includes advisories, issues…
**Reiley Yang (Microsoft Corporation)** 12:09 Yeah, so I'm… I'm thinking about publish the CVEs.
**Trask Stalnaker (Microsoft Corporation)** 12:14 published CVEs.
Including published CVEs in… dependencies.
**Reiley Yang (Microsoft Corporation)** 12:22 Yeah.
So those are public info, like, a vulnerability to me means the hiker can take your binary or source code and reproduce all the things and attack you.
**Trask Stalnaker (Microsoft Corporation)** 12:35 Yeah. Oh, I see you. Sorry, I'm just reading your comment here. A publicly known security issue, which has a… yes.
Yeah, I mean, it makes sense, I think, maybe just clarifying that somehow in that bullet.
that that's what… it means…
**Reiley Yang (Microsoft Corporation)** 13:02 Yeah, so I just want to check with you if this is, like, mostly aligned with what you've been thinking, because I think we use these two terms.
In this PR, and if everyone kind of misunderstood, then I'm going to add clarification and reset the approvals. But if people have just, you know, understanding this Robert, who came later, he… he was a little bit confused.
**Trask Stalnaker (Microsoft Corporation)** 13:25 I see.
**Reiley Yang (Microsoft Corporation)** 13:25 I'm not going to reset all the approvals.
**Trask Stalnaker (Microsoft Corporation)** 13:28 I don't… I wouldn't… I don't think resetting the approvals is needed. I mean, it's… I don't think it's… contentious… I don't think it's contentious, again, but, This is… we're not saying, again, mitigate it within 7 days, it's, again, it's, like, evaluated, acknowledged, sort of that first… first touch.
**Matthew Spiekerman (New Relic, Inc.)** 13:58 Maybe one thing that… that we could consider… I don't know how much this, like, timeline has changed, but years ago, when I was a vulnerability manager, there was a vulnerability exists, but it's not known to have an exploit.
And I think what you're trying to say is that if it's a vulnerability with a known exploit, that it should be reviewed within 7 days, just based on the… The verbiage down below, hackers have all the necessary information to form attacks, or are you saying all vulnerabilities released independent of whether there's a known exploit?
**Reiley Yang (Microsoft Corporation)** 14:29 Oh, so, so, if you look at the doc, I think our position is, if you have some dependency, and those dependencies have a known vulnerability, then you should fix it, instead of trying to distinguish, like, whether I'm using this package, but that particular vulnerability is on a bad path. I won't be able to even reach out to that, and we don't want you to even think about this. So you should fix that. However, how soon you want to fix that, I think we want to give you certain flexibility. Like, if you have a dependency on a critical CBE. Then you're saying, but I don't use that thing at all, so I'm going to patch it, but I'm not going to rush for a zero-day patch. Instead, I'm going to wait for my monthly routine release. I think that's totally fine, but what you have to do is you need to tell your user, communicate to your user on some, like.
Some, like, publish the thing.
saying, hey, we know this thing, but I, like, we checked, and we're not going to trigger this issue, so the fix will come from the next release. Set clear expectation. Otherwise, we expect you to always fix them, regardless of, like, how you're eating that.
Okay. And the reason… and the reason was mainly driven by many users that run scanners, and a lot of scanners are doing static things, they don't have this deep knowledge. If they see you have a dependency on something that has a CVE, they will raise alerts. And if you tell the user, don't worry, we don't use that code, like, path or something, or you will only hit that issue if you do this XYZ enable this environment variable, and you happen to run this on Linux, like, the user's mind will just explode. They're saying, I don't care, I sell this software to some other, like, company, or, like, anything, and they run the scanner against me, so if I don't fix that.
then I'm in trouble. So I think that situation, we're saying, we don't care if you really use that or not. If there's a CVE.
**Matthew Spiekerman (New Relic, Inc.)** 16:24 Sure.
**Reiley Yang (Microsoft Corporation)** 16:24 you should just go and patch it. But you might buy some time by saying, hey, this is on a… that code path, so I'm going to patch that later.
**Matthew Spiekerman (New Relic, Inc.)** 16:35 Yeah, that makes sense.
**Reiley Yang (Microsoft Corporation)** 16:38 Okay, so if you have time, please, like, take a look at the PR offline. Okay, so I'm just trying to check if I have additional agenda items.
If not, then… Are you…
**Trask Stalnaker (Microsoft Corporation)** 17:07 Reiley, are you going to be in the… at the spec meeting tomorrow?
If not, I could bring this… the PR up there.
**Reiley Yang (Microsoft Corporation)** 17:16 I will.
**Trask Stalnaker (Microsoft Corporation)** 17:17 Okay, awesome.
**Reiley Yang (Microsoft Corporation)** 17:19 But if you want to mention that, sure. I think I've already mentioned it a couple of times, so it would be good to have someone else. Okay.
**Trask Stalnaker (Microsoft Corporation)** 17:30 I will, I'll put it on the agenda under my name.
**Reiley Yang (Microsoft Corporation)** 17:33 of us.
**Trask Stalnaker (Microsoft Corporation)** 17:35 See ya.
**Reiley Yang (Microsoft Corporation)** 17:36 Okay, thanks, Laura, bye.
