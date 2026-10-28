SIG: OpenTelemetry Specification SIG + Maintainers Sync
Date: 2026-10-27
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Robert Pająk (Splunk Inc.)** 01:24 Hello.
**David Ashpole (Google LLC)** 01:28 Okay.
**Reiley Yang (Microsoft Corporation)** 01:51 Emma.
**Armin (Dynatrace)** 02:53 Oh, but will you be sharing your screen, or should I take care of it?
For your free topics that you have there?
**Robert Pająk (Splunk Inc.)** 03:00 Yes, I can share, I can start sharing, and then you can take over after me.
**Armin (Dynatrace)** 03:06 Alright, sounds good.
Let's maybe wait another minute, and then we can kick it off.
**Robert Pająk (Splunk Inc.)** 04:54 Let's start Armini?
**Armin (Dynatrace)** 04:57 Yeah, sounds good. 5 minutes passed. I think everyone has had the chance to join by now.
**Robert Pająk (Splunk Inc.)** 05:04 Okay, so, hello everyone. I have the first three topics.
I guess the first two will be kind of quick.
I'm guessing that third one would consume a lot of time.
Armin I would please ask you to just, when I will reach this topic, to make sure that we do not take more than 15 minutes, because I'm afraid that it is possible that we consume more, and I would prefer us to be, you know, timebox it, and just work on asynchronously, if needed, just to note, you know, bicycle during the meeting.
**Armin (Dynatrace)** 05:38 Good. I'll keep an eye on the time.
**Robert Pająk (Splunk Inc.)** 05:42 So, first one. First one, It's also for reminding, and also accredited PR. So we had the Environmental Variable Context Propagation Carrier Document, RC, since a few months. There have been, you see, like, 7 implementations of it.
Together with Alan Kukas, we have also presented it during, cloud, Observability Summit in Pro. Recently, I presented on Warsaw in Cloud Native Days. There have been blog posts.
So, there have been issues, LinkedIn posts, so we try to utilize as much, like, social media or whatever to announce it. Also, I decided to put this PR one week before, so that if anyone has any concerns, any problems, they still have, like, the last chance to call out any feedback if there's not anything breaking, they want us to change anything. The good thing is that a lot of these things are already working in practice, so a lot of tools are already using transparent environmental variables, like like, Jenkins plugins, like, I think Cloud, if I remember correctly, I'm not sure if Codex has not even recently using TraceParent, Docker build tool, Docker build… Docker… Build kit, so there are a lot of tools that are already using, kind of the things from this specification, and none reported any problems.
Okay, 2 minutes elapsed. Any questions?
Okay.
So, the idea is to merge this one after the next SIG meeting. I put a do not merge prefix here, just to make sure that it won't be, merged. I'm assigning it also to myself, just to keep an eye on it.
And… next one…
**Carlos Alberto Cortez (Dash0)** 07:37 By the way, before we move on, Probably not all Maintainers are coming to this call. Let's socialize that. So, in case you are here, and you're not a maintainer, but you attend a SIG, please socialize it there.
We will do it.
**Robert Pająk (Splunk Inc.)** 07:56 also create… I also, write it on Auto Maintainers Slack, just in case, later, as well.
Next one.
So, here I just, so this was, this was discussed, during last SIG meeting, I have addressed all of the comments. I think, mostly they were coming from Tigran, who's… I'm not sure if Tigran is here on the call.
He's not. But I think I addressed… so, I agree that his comments were valid, I addressed all of them, I applied the feedback, and yeah, and I just would like to merge it. I can still wait, like, a week.
Or so, I don't think it's critical, it's more like clarification, and I did my best here to address all the concerns, but I do not also want to bike sketch here to discuss if it's better to have short, or if it's better to have masks, except… I just… there are different opinions, and I think that the current wording is still, like, good enough, and… And valid.
Any questions, or can we move further?
Okay Okay, so let's go to the last one. So, armin… 20… when's 25 plus passed?
For our time zone. Then let's cut it out.
So, So, I'm happy that I see that people here come, probably, to discuss it, and I'm open to any feedback. So, first, I will tell where this PR is coming from, the background.
and a little bit rational. I try to put as much as possible in a kind of… transparent way in the PR description and in some comments.
And I really did… I really spent a lot of time creating this PR and finding the best possible description. Of course, AI helped me, but it was not like AI if I code it. I really took a lot of care on… on this one. So, the thing is that, Few things, One thing is that… there are these, entropy scanners, which I want to apply in, Go repositi, for instance, not a Go repository, but probably, I think, it should be adapted in more repositories.
And I found out that probably the, the way that I would like to… Like, integrated, is to have some base OAC, or whole auto telemetry, like, thread, common thread model, whole… for… for whole OpenTelemetry, how, how we understand, plugins, plugins, exporters, receivers, etc, so have some baseline.
And then, if there's, if there's anything specific to some repository, to some component.
then the repositories can have as component-specific thread model, which right now is used by many of these, scanning tools, but it was also pop… I know that this kind of document was popular, like, even, like, 5 years ago.
Even before these tools were, were here.
And, this PR does a few things.
I'll be asking afterwards that I'm considering splitting it into a few, but for the sake of this conversation, I decided to have it as one PR, even to gather this initial feedback. Maybe I'll decide to separate it later. So, one thing which I… which… I… I wanted to have is that each time when I was triaging existing autogo vulnerabilities.
I found that I… I had… some mental… I had this… I had some model in my head, which is probably common for a lot of maintainers, which was not described.
And this is one thing that I wanted to codify it, to make life easier.
For, for the Maintainers.
Second thing, the better it is described, I hope that the better quality of vulnerabilities will be reported, which will be, first of all, actual issues.
And second, also issues that are not filter out by, that are actual, issues.
So, and also, kind of update it.
So, what I changed? In… like, what I wanted to change.
One thing I wanted to change the CVSS.
S-E-V-S-S.
So… version 4. I find it a lot better and easier to triage than 3.1.
One of the reasons why it was created was because some things in the… in version 3.1 was kind of, it depends, it depends, it's hard if the version 4.0 is easier, especially for developers to go through.
Also, this is the current recommended thing, so this is something that could be probably done as a separate PR.
this is one part of… one big part of the PR.
The second big part, apart from a lot of description, is that personally, I… I strongly disagree that the things which are described here Are not considered as security vulnerabilities.
So, a denial of service attacks, which is a part of availability attacks.
I think we are filtering too much. Denial of service does not mean that we are brute forcing something. Denial of service means that if there's some… if there's some, I don't know, input or whatever, you do something.
it crashes your application. It doesn't need to be, you know, like, brute force. It means that, for instance, if there is a… if there's a memory leak, when you're putting, when you're making a request, and then it's long-term, it, it causes the application to crash, it is a version of denial-of-service attack.
Second thing, if, for instance, we are not handling empty log body field, and it causes the… and it causes the application to crash, it is also a denial service attack.
So this is one thing which I… I totally disagree, that this is a too broad statement.
And… Availability-related attack to endpoints properly by authenticated clients?
**Reiley Yang (Microsoft Corporation)** 15:04 over.
So, there's comments, and Pablo also raised a hand, because I think he made the original change.
Maybe, like, let's talk about the denial of service by authentic clients.
**Robert Pająk (Splunk Inc.)** 15:18 Sure.
I put a response here.
So, I think my response was here.
So maybe I'll just… do we need to… do you want me to comment, right? Do you suggest to comment on the existing ones? To the existing motivation here?
**Pablo Baeyens (Datadog)** 15:43 I think maybe, yeah, we could cover a bit the original motivation of this change, And then we can talk about the comments. So, I mean, I think… Jack made a very important point on the Zoom chat. This was meant to exclude things that were done by properly authenticated clients, and so… Well, this is something that I worked back to on May, because, the collector SIG, was getting a bunch of… security reports that were, related to availability, but assumed that, well, you were you were able to bypass authentication, or, like, you… you had not configured authentication in some way. And so, I… took a look at a few other projects, under security models, and I proposed this change so that you… So the operating model for OpenTelemetry in general would be that, you have set up authentication correctly, and so anything that, is only possible to be done by an authenticated client. For availability, it would not be considered a security vulnerability.
And that's… roughly, this stands from Postgres, from Prometheus.
to some extent from Envoy. Envoy's a bit more nuanced.
And I guess my last comment on this is also, I think everything can be discussed, and everything can be revisited, but this was a change that I believe had broad consensus, and so I feel like that.
**Robert Pająk (Splunk Inc.)** 17:37 Okay, so…
**Pablo Baeyens (Datadog)** 17:38 Specifically, we should probably have a similar level of consensus to change it again.
For other changes on the PR, I… I don't have a strong opinion.
**Robert Pająk (Splunk Inc.)** 17:52 So, I, I just want to comment that my guess, and this is my guess.
That's probably you were having attacks, like, somebody was flooding you with locks or traces.
Or is it… or is my assumption not correct? Because it's hard to, right now, you know, when you were proposing this.
what was the category of attacks? What is, like, really things that I personally assess as a security vulnerability? Like, you can get a panic, it crashes the… it crashes, even if it grows through the decay? Or was it, like, you know, we are flooded?
And we are not able to handle it, which is… which is that.
**Pablo Baeyens (Datadog)** 18:28 My intention was denial of service in general. For example, somebody has a carefully crafted payload that, you know, allocates a lot of memory. If that's something that you can only do, Either by… Not having set up authentication, or, like, by, assuming that the attacker has authentication privileges, then I don't think that should be considered a vulnerability, and that's… that was my intention with this PR.
**Robert Pająk (Splunk Inc.)** 18:58 Okay, so, in my opinion, and I added my reasoning here, I just… we have only 5 minutes, I tried to express fear and fear why I disagree with it. Here, I also try, because I think that, Brian, or no, I'm not sure, is Braydon, sorry, also, added some similar feedback to yours.
But I also want to assess that even if you have these security kind of standards, like MITRA, or when you have CVSS authentication.
It's not never dismissing the security vulnerability. It's decreasing the severity, and it's decreasing the severity a lot, but for instance, it's decreasing, you know, for instance, from critical to medium, depending on, you know, the calculator.
But… I'm more familiar with…
**Pablo Baeyens (Datadog)** 19:49 with CBS3, in that case, it is something that is, like, And reasonable configurations are, like, out of scope. Maybe that's not the case for CVSS4.
I did reply to your comments below on…
**Robert Pająk (Splunk Inc.)** 20:08 Okay, I was…
**Pablo Baeyens (Datadog)** 20:10 Yeah, I think it would be good to continue. I think the… the article I linked about regular expression denial of service vulnerabilities, although it is a different class of vulnerabilities, I think it is very interesting, and maybe it's a bit… opinionated, and a bit negative on the security researcher side, but I think it talks a bit about the dynamics at play here, and… why I… I feel like it's applicable here, I'm…
**Robert Pająk (Splunk Inc.)** 20:38 Okay.
**Pablo Baeyens (Datadog)** 20:38 It's an uninteresting.
**Robert Pająk (Splunk Inc.)** 20:40 I strongly disagree, mostly because, you know, our observability software can be used in a lot of environments.
And I think that if something causes crashing, something which is valid according to the OpenTelemetry Specification, or, you know, it's simply possible to put it via, you know, via OTLP or whatever, and it can cause things to crash.
I don't think we should ever treat it just as a bug.
you know, it can… it can crash, it can, you know, people can rely… the thing is, sometimes I'm even more concerned about memory leaks, even, than crashing, because it can also affect the neighboring processes… processes. So, for instance, you have some… yep.
**Pablo Baeyens (Datadog)** 21:27 This feels like a reliability concern more than a security concern, and I think we are aligned on reliability being important.
**Robert Pająk (Splunk Inc.)** 21:35 I just don't be secure.
**Pablo Baeyens (Datadog)** 21:36 communities.
**Robert Pająk (Splunk Inc.)** 21:36 So reliability is part of security.
**Pablo Baeyens (Datadog)** 21:44 I tend to disagree that that can be said as a broad statement, but yeah,
**Robert Pająk (Splunk Inc.)** 21:54 okay, especially availability. If, you know, if, because of that, something, something does not work, then… how you can say that's your… but whatever. I think we're, maybe less… I have also… I saw David is in the call. I have a question, because I know that for sure David iterated and reviewed this at least, I think, a few times. Do you have any suggestions how to proceed with this PR? Do you think that it would be good to split it into two or three, or something like this, when you're reading it? Have you get some impressions? Because for me, as an author, sometimes it's hard to judge.
I'm just, you know, swamped getting too much into… into the, you know, thing, and then I'm just getting lost.
**David Ashpole (Google LLC)** 22:39 Yeah, I didn't think it was unreadable, I just more… I think there's, like, a lot of trade-offs here, right? Like, obviously, We could have a very… Like… we could allow, like, anything to be reported as a vulnerability, and we'll get a lot more vulnerability reports, and maybe we'll get more out of, like, this Anthropic thing that you want to sign up for. I… I think… I think the collector in particular, I'm just concerned about because of the… enormous scope that it has, and I want to make sure that this, like.
I would view this, like, pragmatically as… or try and be pragmatic and not write down something that will just drown us in… Reports that are… super low scored.
**Robert Pająk (Splunk Inc.)** 23:30 So, my intention… just to have a feedback order, because I thought about it as well, so that's the reason when I thought that You know, just to not be overwhelmed with enormous issues, even if some, 6, decide that even if it's a long path, it's good, but, you know, it needs to be a journey to fix some things that will be reported, because I understand that if we change the model, then you put some scan, and we'll get, I don't know, 40 more vulnerabilities that you may not want to, you know, just handle At the same time, so that's why, we proposed This… Red model… Which con- which can contain exclusion, additional exclusions.
And I thought that maybe just the collector will just add those if they have strong opinions.
And it's a… if collector finds, or any other SIG, that this is very hard for them to have… to get rid of this, just to start and add this to their threat model with their reasoning, and then it can be adapted later.
Also, Nothing is written in stock, right?
There was some other feedback that, I think Trask wanted to say something.
**Trask Stalnaker (Microsoft Corporation)** 24:51 Yeah, yeah, I had, two… just wanted to call out two things. One, as Robert mentioned, the, whether a client is authenticated is already, baked into the CVSS scoring heavily, and so clearly.
They intend for authenticated clients to count for security vulnerabilities?
And so I think that makes sense as a baseline for all of OpenTelemetry.
But I was going to propose, and I totally agree what Robert just said, which is that an individual SIG, I think it's fine to make a different call, so I think the collector can scope that separately. But I think as the broad… All across, you know, the de- as our default.
I feel better about just leaning into the CVSS defaults.
**Robert Pająk (Splunk Inc.)** 25:57 We are out of time.
One minute or so.
If you have any, you know, if you have any feedback, feel free to comment. I will do my best to address them, or respond.
as much possible respect that I have.
And thanks a lot for your feedback. I really appreciate, even if you disagree, I really appreciate feedback, because we are also learning as a group when we are discussing these things, like all of us, and thank you.
And this is the end of my thing, and I think Trask is your… I just don't be willing to share.
**Trask Stalnaker (Microsoft Corporation)** 26:33 more security.
**Robert Pająk (Splunk Inc.)** 26:35 Yep.
**Trask Stalnaker (Microsoft Corporation)** 26:35 If people aren't, worn out on security yet.
Yeah, just bringing this, we've been, continuing to discuss this in the Security SIG, and thanks, a lot of you have been posting on the, providing feedback on the PR.
just wanted to kind of bring it more broadly to this audience for people who haven't maybe looked at the PR and give kind of a summary for folks.
What it is doing is defining these four levels that repos can choose from, for kind of their security requirements, what they will, and so, Standard and Elevated obviously come with higher requirements.
So kind of the… some of the key ones are, acknowledging and updating security reports, so this is, security advisories and security issues, Which we, these would be… public issues, sometimes, like, low priority, public security issues that people can raise. For example, something that's already publicly known about, dependency.
And so it defines some baseline, Days for… just for acknowledging, back, not… resolving. Yeah, let's… let's go for hands while… while we don't have to go to the end. Josh?
**Josh Suereth (Google LLC)** 28:23 Two things. One which is a joke, and one which is real. One is… What security level do I need to make all my passwords be 4? The number 4?
And then, the real question is actually around the security baseline model.
So… Weaver, as you know, is like a build tool, right? Versus, like, a server tool.
Is there… like, where do you see that fitting in terms of, like, baseline standard elevated, or is that, like, an orthogonal, like, I'm a development tool and we should have a security… consideration around… because again, security there is more like Salsa compliance and, you know, build… build a surety and that sort of thing. It's like a different… Beast a little bit.
So I wasn't sure if you've thought about that, or kind of where… where you think that fits with your level.
**Reiley Yang (Microsoft Corporation)** 29:13 Yeah, I can answer that. So the general wording should apply to all the OpenTelemetry projects. I even considered things like, hey, OpenTelemetry.io, we host a website, then the website might be attacked.
Like, there might be expired assert or something.
So, in general, like, it should apply to Weaver and any of the OpenTelemetry projects. If you think there are special cases that we haven't considered in the PR, please call that out.
**Josh Suereth (Google LLC)** 29:44 I haven't had a chance to review, I was just curious if that's, like, if we're supposed to be in the same model, so that sounds good. I'll take a look.
**Reiley Yang (Microsoft Corporation)** 29:50 Yeah, so the answer is yes, we should, and the PR is more focused on, like, very general practice, like your CICD, what artifacts you're shaping, and how do you plan to patch those artifacts.
**Trask Stalnaker (Microsoft Corporation)** 30:05 Robert.
**Robert Pająk (Splunk Inc.)** 30:07 What does updating means?
this one question.
And I just want to also tell to the judge that, kind of, these tools are also mentioned in my PR, in the security mode, yeah.
**Trask Stalnaker (Microsoft Corporation)** 30:27 So acknowledging, like, this is, my understanding is we got your report, and we're looking at it. It's just, like, so people know that it hasn't dropped into the ether?
**Robert Pająk (Splunk Inc.)** 30:42 Yeah, so what's updating? Is updating even necessary here?
**Trask Stalnaker (Microsoft Corporation)** 30:53 I think acknowledging is… the… Point of this first… Timeline.
**Robert Pająk (Splunk Inc.)** 31:04 I agree.
**Trask Stalnaker (Microsoft Corporation)** 31:05 I'm not sure, Reiley, Reiley do…
**Reiley Yang (Microsoft Corporation)** 31:09 Okay, so I'll answer it. I think a knowledge is when people first report that, and you provide a response. We just don't want the Maintainers to sit on it and do nothing, right? Otherwise, the people who report that might decide, okay, I'm screwed up, I'm going to make this public and destroy you.
Or maybe they just don't know what happened, they'll write a blog post saying, OpenTelemetry folks don't care about security, things like that.
Then, updating means there might be response, or they might be expecting something, so it's on you, and you as the maintainer, you have to keep the ball rolling. Instead of, I just acknowledge, and then I'll do nothing about it. Once you acknowledge, you might have to evaluate that, and you might have additional questions, you might reach out to this… the reporter saying, hey, like, I'm not able to reproduce this, and I tend to close that, do you agree? And they come back and say, I disagree, then you didn't do anything, you just ignored them for a month. This would be as bad as we're not acknowledging that at all.
So I think it's more like the two-way communication, keep the conversation active.
**Robert Pająk (Splunk Inc.)** 32:10 So really, I think to make it more readable and, you know, more clear, I would personally put it as a second bullet that, I don't know, responding to the reporter or something like that in 7 days. You know, I think because, yeah.
Replying, exactly.
**Reiley Yang (Microsoft Corporation)** 32:30 Yeah.
I'll make the update.
**Robert Pająk (Splunk Inc.)** 32:36 Thank you.
**Trask Stalnaker (Microsoft Corporation)** 32:38 Braydon, yeah.
**Braydon Kains (Google LLC)** 32:40 So I only joined the, like, maintainer group recently, which means I've only had access to… to advise… to, like, look at advisories and help with them over… for, like, a month or so. So I'm… in the collector, I'm… Seeing the pattern, and maybe, like, this is part of the motivation for introducing something like this, is that we had a few that took a really long time, or at least, like.
opening to remediation on paper was a really long time, but what tends to happen is we see the vulnerability… like, the… sorry, the advisory. We see the advisory usually relatively quick, and respond relatively quick, oftentimes saying… like, more times than not recently, saying, this isn't actually… A vulnerability. But then, as Maintainers, we lack the direct Permissions to, like, close it.
So we… a lot… there's a lot of them that were, like, open for a long time because the maintainer responded and said, we don't think this is valid, we're probably not going to address it, and then it just kind of sat there open.
And… the… that's the… the thing I'm noticing as a maintainer, is that, like, it's… it's actually kind of difficult To address them, because as Maintainers, we have the ability to, like.
Change the severity of the report is one thing we can do, and we have the ability to write a response, but then to do anything such as accept and open the private fork, or to close it.
we lack the direct responsibility… the direct permissions to do so, and either are relying on the TC, or making a PR to that, like, Terraform module to get temporary admin rights just to do something, and then… like, that feels… like, it's a lot of work for us to do something that we should maybe just be able to do. I don't know the right way to address this necessarily, but that's the, like, comment for, like, if we, the collector, were going to opt into standard, the big thing we would want was to make that sort of, like, triaging a little bit easier to do.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 34:39 That triaging bit where you lack the permissions to do things like request a private fork and close them, that's an unfortunate side effect of GitHub's permission model, and, you know, we don't like it, but it's what we're dealing with. I will say that the TC has made some changes in terms of its role in security advisories, and now there's always a TC member that's going to assign itself as the collaborator on every new advisory that's opened, and who… it's whoever was the TC member who was on call when the advisory was reported. That's, like, the person who's, like, sort of your touchpoint for the life cycle of that particular advisory. And so, like, if you don't want to go and get admin access, which I understand why, just, like, feel free to lean on whoever that TC person is to, like, request that they take these actions on the advisory on your behalf.
And, like, you know, it shouldn't be ambiguous, like, who on the TC you should be, like, reaching out to. It's a very specific person now, and that was the goal of this change.
**Reiley Yang (Microsoft Corporation)** 35:39 Yeah, and the on-call TC member should be able to also add the project maintainer, whoever wants to track that issue. As a collaborator, I think that would give you the access.
Anyways, so every security advisory that got, like, privately reported will have a TC member helping there, and I think the expectation is you as a product maintainer, if you need anything, you find you don't have the right permission or the right tool to do your job.
you should reach out to the TC member and ask them to help. If you don't reach out, you bet that most time, the TC member wouldn't even know you're stuck.
So we expect you to be accountable as a project maintainer, and if you cannot do your job, ask it to the TC.
And this is, less of a concern. I think the main concern of this, like, the main motivation for this PR is more on the publicly known security vulnerabilities. So there are two things. I think sometimes people might be… confused, and they might be mixing those two. So there are security advisories, which have a very specific meaning in GitHub. So those are privately reported things. These are just, like, security findings. It doesn't mean you have a real security issue.
You might agree with the advisory or disagree, or you might adjust the balance by saying, hey, I agree this is a security vulnerability, but the severity is not as high as you would expect. I'm going to lower that, so there's certain like, guidance how you can do that. And you can take the time, as long as the folks who reported that agree that they're going to keep it private.
But whenever they make it public, and it is a verified thing, it means, like, everyone in the world, as long as they have access to internet, they can see those problems.
And one typical example that people all know is there's a CVE database, right? If you… if you depend on a component XYZ, that component XYZ depends on some other components, and those bring in security vulnerabilities. There's already a published CVE and the security score. So, those are the things we want Maintainers to be very clear that, like, they are, like, everyone would expect you to fix that in a reasonable amount of time. Just don't sit on that.
And one typical argument I can see, some folks are saying, hey, although I depend on this component, and there's a known CVE, like, everyone can run a scanner on my released artifact and find this dependency. But I actually don't use that. It's on a dead cold path, like, there's no way I can trigger that.
So… so here, we're trying to be very clear, like, we don't care about that.
If people run scanner, they notice you have a supply chain issue, you should go and fix that. But you might change the release schedule by saying, hey, although this is a zero-day CVE in my downstream dependency, but I confirm that my code doesn't trigger this path, so I'm going to fix that anyways, but I'm not going to release a zero-day fix, because customers are not affected.
I'll just carry that in the normal monthly release. So… we see those patterns, and we see some SIGs got confused. This is more, like, to clear that and have the consistency for all the maintainers.
Yeah, so the short summary is.
everything that's publicly known, if you have a dependency on something, there's a CVE. The hackers contact you. You need to be fast.
If it's private, you can take the time, do the discussion as much as you want, as long as you agree with the people who report that, and as long as you respond to them instead of just sit on it and do nothing.
Rob?
**Robert Pająk (Splunk Inc.)** 39:32 I have one suggestion. It's in my mind since, I think, one or two months already.
Have you considered moving these documents to the auto-specification? The thing is that we have a lot of similar documents, like, about versioning, about stability, and things like that in the Specification, and I think once in the spec.
it's more visible to… especially to the… even to the Maintainers. I think that some… I have a feeling that the documents in SIG security, I kind of… I would say, not visible and transparent enough. Even though they are open to MTIO, I just think that a lot of people may not see them, not review them, etc. Have you any… do you have any thoughts on that, Reiley? And sorry for side-questing, but I think it can help long-term.
**Reiley Yang (Microsoft Corporation)** 40:20 Yeah, so I thought about that, and I tend to say no, and here's why. The first thing, I think the spec is more on the interface contract and behavior things, and security, of course, is a general, like, part of the behavior.
But I… I do believe there might be other OpenTelemetry implementations. Like, we have a spec because we want people to be able to implement something and call that a SPAC compliant thing. So, imagine if there's a different implementation, and they're saying, well, we run in a very controlled environment, and we… we don't need to release the patch, because nobody can access that physical environment. Our security bar is very different. I don't want OpenTelemetry to say, although you meet all this API and the behavior thing, but just because the security part is different, you're not a compliant OpenTelemetry implementation.
So, I do believe different entities, different communities might have different security bars. Number two is, I think the SPAC is very much, like, versioned, and… I wish the security model to be decoupled from versioning, so we can make the update as the climate change. I think it'll be really confusing if someone comes and say.
I meet the OpenTelemetry Specification Security requirement for version 1.2, and they were talking about something two years ago, and 1.2 just makes no sense for people who use OpenTelemetry these days.
**Trask Stalnaker (Microsoft Corporation)** 41:48 If it was gonna live in another repo, I think the community repo might be the better Yep. In place. Yep.
**Reiley Yang (Microsoft Corporation)** 41:58 Yeah, so something orthogonal to the spec, yeah, sure, adding a link to the… from the spec is a good thing, yeah.
Yeah, so I tend to say no, but happy to be convinced if there's a more, like, pros than the cons.
**Liudmila Molkova** 42:13 Can we have a link to it? And maybe even from every repo, if we have some special security Thing that's linked to every repo, then… At least your AI bots can discover where security things live.
**Reiley Yang (Microsoft Corporation)** 42:30 Yeah, we can put an action item on me. Thank you.
**Liudmila Molkova** 42:34 Awesome, thank you.
**Trask Stalnaker (Microsoft Corporation)** 42:37 And we're… I'd say we've hit time, but I wanted… one last thing, Braydon, for the… yeah, we've… I really, really hate the GitHub, maintainer permission model when it comes to security advisories.
It's definitely been a pain. Would you… but there might be… I mean, it's definitely worth us looking at what kind of automation kind of things we could do, like, we could potentially provide some automations that, you know, comment-driven automations on the security advisors, for example, that Maintainers could run. I don't know, But I was gonna ask if you wouldn't mind opening a community issue, just kind of… Since you've gone through this recently, of, like, pain points of maintainers.
Dealing with security advisories, and, It's something that I think the security SIG and the TC on-call folks could think about more.
**Braydon Kains (Google LLC)** 43:42 Yep, I can do that.
**Reiley Yang (Microsoft Corporation)** 43:43 Oh, related, if I can take maybe 30 seconds. So, Anthropics reached out, and they have a way how maintainers, like, if you own the repository, you can just submit a PR to the Anthropics repository, saying, I want you to run a daily scanner and create all the security findings, via… security advisory on GitHub. So previously, they were sending email, and Trask and I have been, like.
seeing all these emails, and now they're going to create advisory, so I encourage all the Maintainers to leverage that, and once you enable that, expect that you will see a lot of security advisories.
So if you haven't prepared for that, like, I think you should talk to your SIG and see if you have enough funding. And you're thinking, I'm the only one guy maintaining this repository. I definitely don't think this would work.
this is, the right time for you to think about, maybe, like, expand your Maintainer group, reach out to the TC and GC to see how we can potentially fund that. Leverage this, like.
Like, this recurring meeting, talk about yourself, give people the update to try to attract more maintainers.
Thank you.
**Armin (Dynatrace)** 45:07 All right, thank you. Next topic we have up is checks. Do you want to share yourself, or should I take care of it?
**Jack Berg (Raintank, Inc. – Grafana Labs)** 45:17 Just for convenience. And then I'll hand it back to you afterwards.
**Armin (Dynatrace)** 45:22 Sure.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 45:23 Okay.
So this is a… this is a PR that, Mikel opened.
And Mikel and I are both interested in this topic, but it's about specifying criteria for automatic injection in SDKs and instrumentation. And the reason Mikel and I are both interested is because we're both maintainers for the OpenTelemetry injector, which relies on this behavior. So, you know, the basic idea is, just to kind of regroup everyone, is that we want We want OpenTelemetry as a project. We want there to be tools that can install our automatic instrumentation across, broad polyglot environments, like, think an entire Kubernetes cluster, automatically and without you know, risking breaking applications. So this, this, you know, instrumentation needs to be safe and reliable.
And, So, you know, this PR was open, and there was some tension going back and forth in people, and I think I would characterize the underlying tension as, like, you know, we're trying to establish criteria that says that these, these auto instrumentations must be, like, safe to install, or should be safe to install in all circumstances. And, you know, people were bringing up a variety of different cases where it's just not practical or possible for a, one of these instrumentations To, to, to ver… to take these verification steps.
And so, yeah, I, I… Mikel and I, we regrouped, and we're coming at this from, like, a different angle now, and so, you know, the content has considerably changed in this, and, you know, what it does is we first established some terminology, there's a… the key terms are there's an injectable distribution, and that's the thing that you're injecting, that's the instrumentation you're attaching, like the hotel Java agent, for example. And then there's injector tools. And injector tools are responsible for installing these injectable distributions. And… What we do in this language now is, we establish that, you know, providing an injectable distribution is optional, but if you do, you must describe the mechanism and the prerequisites of installation in a contract.
So, this is the key bit. There's now a contract that you must declare all of your prerequisites and how the installation mechanism works, and that needs to be part of semantic versioning. So, you can't go making, like, breaking changes to this contract outside of a major version bump.
And, like, included in this contract are things like, you know, things like minimum supported runtimes and versions and dependency requirements, anything that is required for this to work successfully. And, you know, it's also supposed to identify which party verifies these prerequisites, these constraints. So, it could be the injectable distribution makes the verification.
or an injector tool is responsible for verifying it, so… That's, like, a key thing that you have to specify. But assuming that all the criteria in the contract is satisfied, The, the injectable distribution must not break the application. So, you know, it's basically backing off the original a bit and saying, like, instead of, like, the injectable distribution is responsible for everything, now there's a cooperative set of responsibilities. Some things are respon- like, the responsibility of the injector tool, some on the injectable distribution, and this is all declared in a contract, but assuming the prerequisites are satisfied, you must not break.
And so, you know, and so the next bit is that if… If an injector tool cannot establish that the prerequisites are satisfiable, like, if it just cannot detect the right information in an environment to know if it can satisfy the prerequisites, then it must not enable that distribution by default.
So, I think this creates, like, the right set of responsibilities and the right incentive structure. You know, basically, so write down your prerequisites, and the injector tool is going to do everything it can to try to satisfy those prerequisites, but if it can't, because there's technology limits on the injector tools themselves.
then we just can't enable this by default, so that's just the cost of, Of that, and it allows us to ensure that we can safely install these things across large environments.
And, you know, this isn't ideal, right? It's not ideal that one of these should not be enabled by default, but, you know, it encourages both the injectable distribution maintainers and the injector tool maintainers to work towards solutions to be able to either reduce the set of prerequisites that are required for safety, or to expand the detection capabilities, either within the distribution itself.
Or within the injector tool, that's… so, yeah, that's, that's the re-sort of framing of this, and, it, the PR currently has a couple of approvals from myself and Trask and Reiley, so if you're interested in this topic and you've been participating, please give it another review.
Diego?
**Diego Hurtado (Dash0)** 50:40 Yeah, is… is there already a… Specification for these contracts that you mentioned?
**Jack Berg (Raintank, Inc. – Grafana Labs)** 50:49 This is the specification, this is all net new.
So the contract, I'm imagining it's just pros. It's like a markdown file somewhere in the repository where this distribution lives. That's… there's no, like, formalization of it besides that.
**Diego Hurtado (Dash0)** 51:05 Right, but these contracts must be… must be translatable into code, right? Because they need to be evaluated into true and false conditions.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 51:15 Yeah, so just like the Specification is a contract written in prose that is versioned under SEMVR, the… I imagine that this contract that I'm talking about is also prose, and you know, some components are responsible for translating that prose into code.
**Diego Hurtado (Dash0)** 51:33 Alright, thank you, I'll take a look at this field.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 51:35 Yeah, sounds good, thanks.
Right. Well, there's no other, comments, we can move on.
**Armin (Dynatrace)** 51:54 Alright, next item is by Josh, but not really something to discuss. It's a link to the CNCF Slack with instructions on how to work around the Helios voting issues that some have been experiencing for the GC election. Also, not everyone's election is up for Technically, like, roughly one more day, so best about today, anyway.
And with that, I'll pass it on to Trask for our final item for today.
**Trask Stalnaker (Microsoft Corporation)** 52:24 Yeah, just, mainly just notify, FYI, RPC semantic conventions are finally getting marked stable. So if you want to look at any last thing or put your green stamp on that, Would love it.
And, call out to the, the GRPC team that, we were able to work with and align with them, So, I think, you know, that was one of the… the hiccups or last things that kind of drew it out for a while longer, but I think we all… we came out in a good place.
**Armin (Dynatrace)** 53:22 Thank you. Great news.
Any last-minute topic?
Alright, then let's wrap it up here. Thanks, everyone.
Have a nice rest of your day.
Bye-bye.
**Trask Stalnaker (Microsoft Corporation)** 53:43 I…
