SIG: SIG Security
Date: 2026-10-12
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Reiley Yang (Microsoft Corporation)** 00:30 Hey, Trask. Morning.
**Trask Stalnaker (Microsoft Corporation)** 00:34 Good morning, Riley.
**Reiley Yang (Microsoft Corporation)** 00:36 Okay.
Yeah, I wonder if you have any topic. I don't. I know there's a dangling PR. I'm still, like, reaching out to a couple folks for their perspectives.
Basically, I'm waiting for… reply. And we did talk about, do I make the PR more complex by separating the advisory versus the known CVE?
I try not to do that before I see clear signal, because I… I think the longer the PR, the harder we'll get approvals.
**Trask Stalnaker (Microsoft Corporation)** 01:09 Oh, I see, a comment I made, let me remember what that was about.
issues… Oh, okay. My question there, kind of my follow-up question is, how… what is a security issue?
How do we… how do we identify? Like, I'm thinking from a… from our perspective, from a SIG perspective, at some point, we would like to have some workflow that, like, automatically escalates when dates aren't met.
**Reiley Yang (Microsoft Corporation)** 01:45 Yeah.
Yeah, so in my mind, there are two things. One is in the public domain, like, anyone should be able to reproduce. In your repository, you release some artifact.
whether it's a website that you host, like opentelemetry.io, or it is a demo project that you release, people can run on their local machine, or it's a reusable library, a component like Collector or an SDK, people can use. And they can basically use your artifacts.
to run any scanner there, the scanner will say, like, I know you have this dependency on this XYZ component, and that XYZ component has a known security vulnerability.
And the fix can be as simple as bump the version if everything works smoothly. Or maybe it can be very complex because when you bump the version, there are breaking changes. You have to look into it deeply.
And for websites, you can imagine a similar thing. People might realize, hey, your website is still using some, like, old CA rules, so I can use a fake certificate to attack you, or maybe, like, you… you didn't even require HTTPS, like, normal HTTP is sending authentication through, like, planet TCP is fine. So… so any artifact, I think, that people can reproduce in the public domain easily.
Then, I think the difference comparing to security advisory is when people only report to a private side of people, like… Yeah, sorry.
**Trask Stalnaker (Microsoft Corporation)** 03:06 I understand the distinction between those two things that you're making. What my… sorry, my question is.
We don't have something called a security issue, like, would we create a label?
**Reiley Yang (Microsoft Corporation)** 03:21 I want the SIG to create a label where people can report, and we can use automation to report, hey, you have this known thing, and all these issues should be in the public domain. And once it's known, we have a specific time, and that time is easier to define, because everyone can see that. There's also some, like, regulations.
Talking about that.
So here's an advisory. I don't think we want any… like, hard timeline regarding when are you going to resolve it. It's just, like, we want to make sure you look into it, so the response time is what we care about. We don't want you… like, people reach out to you for security advisory, and the researcher is saying, if you don't do anything, I'll disclose that in 6 months, and you forget about it.
And then after 6 months, it's becoming a public thing. It's very bad, so we just want to make sure you, as a maintainer, you will actively follow up on those, like, 5 days, 6, 7 days, whatever. So, I think those are the difference. And for security advisories, where they have the GitHub mechanism to track the security issues that are in the public domain, we don't have a standard tag. I want us to have a tag.
And I want us to have the issue templates, so when people, they try to reach out, they create an issue, the template will tell them.
if you have this, like, public issue, then you should just go ahead and create a GitHub issue. If it's a private thing, you don't think everyone should know, then you should go through the security advisory. So I want to do that, and I want to use the security SIG as an example, so first we can agree on that, then we'll… We'll set that as a basic requirement for all the repositories if they want to hit the low commitment level.
**Trask Stalnaker (Microsoft Corporation)** 05:05 Cool.
I am just leaving a comment on my comment from the SIG meeting, and I will resolve that.
**Reiley Yang (Microsoft Corporation)** 05:14 Okay, thank you.
And you like the idea, like, I want to use a security SIG to lead an example, so, like, how… it's not a real thing.
Security doesn't release any code.
We have a README file. We probably have CICD security concern, but we don't release an article. Or you want me to take a real…
**Trask Stalnaker (Microsoft Corporation)** 05:38 We can use… we can use the Java instrumentation repo is fine.
**Reiley Yang (Microsoft Corporation)** 05:43 Okay.
Then you're okay, like, because you're the maintainer, I can send a PR, you can review.
**Trask Stalnaker (Microsoft Corporation)** 05:49 Yeah.
Yeah, it's just Lori and me as the maintainers of that repo, so… We're pretty… Open to doing new stuff.
And do you want… let's see, approvals, is this… I guess I will check the… the only kind of contentious thing, like, the… the whole day's business days, but I think that's… Is there any concern now that you changed it to 7 days?
**Reiley Yang (Microsoft Corporation)** 06:51 I don't see any new concern. The previous one, I believe, already addressed. So basically, I was saying, if you're concerned about 3 business days, you're saying I might be on vacation. Now, I'm going to give you 7 days.
Same day should be enough, so I try to be very generous, but I don't want us to fight on business versus non-business days.
And I think nobody has objection.
**Trask Stalnaker (Microsoft Corporation)** 07:15 I'll give it one more read-through, but, try to leave an approval there.
**Reiley Yang (Microsoft Corporation)** 07:22 Okay, thank you.
I have a question. You set up this repo to do some, like, AI automation thing, and to help to detect the AI injection, and… and I… I mean, initially, I thought maybe you don't want me to merge the PR, I can't approve.
But I, I started to see some, like, very trivial things, like, I, I just, like, for example, like, bump a CI version or something. So I just approved and merged a couple PRs.
So how do you plan to run those? I mean, like, we haven't clarified who are the maintainers. I think TC and GC are both tagged there. I want to make sure I'm not stepping on your toes. Haha.
**Trask Stalnaker (Microsoft Corporation)** 08:07 No, no, I think you… I think the maintainers… R… Yeah, yeah, I should…
**Reiley Yang (Microsoft Corporation)** 08:15 The org maintainer.
**Trask Stalnaker (Microsoft Corporation)** 08:16 the…
**Reiley Yang (Microsoft Corporation)** 08:17 admin.
**Trask Stalnaker (Microsoft Corporation)** 08:18 Yeah, it's the GitHub admins. I see.
So, that's why you are… Yeah.
So, yes, you are. Okay. Authorized.
Yeah.
Yeah, I just aligned it with the, the admin repo.
I actually don't really have any strong feelings. We could make it all of GC and TC if we wanted to.
**Reiley Yang (Microsoft Corporation)** 08:47 Got it. Just let me know if I'm doing something that you want me to stop. I'm trying to do reasonable things there.
**Trask Stalnaker (Microsoft Corporation)** 08:54 Cool.
**Reiley Yang (Microsoft Corporation)** 08:59 I guess that's all. Anything else? Alright.
**Trask Stalnaker (Microsoft Corporation)** 09:02 Nope.
**Reiley Yang (Microsoft Corporation)** 09:02 Cool, thank you. Nice to see you again.
**Trask Stalnaker (Microsoft Corporation)** 09:05 Yeah.
