SIG: Security Governance SIG
Date: 2025-11-10
Duration: 11 minutes
Zoom Recording URL: https://zoom.us/rec/share/zbGPjkEn6ppnnRyj5vaxpDLdIfUVQsZjPaEU4uiZlIituqT51SMEG1M11AIqlZfR.y7buAwFqeLYc5KgQ
============================================================

## Zoom Recording Transcript

**Reiley** 00:38 Morning, Jeremy.
**Jeremy Corley (Microsoft)** 00:40 Morning.
**Reiley** 01:23 Do you have agenda items?
**Jeremy Corley (Microsoft)** 01:27 I don't have any for today, no.
Other than I was just gonna ask Trask where he was… there was a… Update on the dashboard.
Yeah, he had a PR in there.
**Reiley** 01:50 It looks like we have a… New member joining. Hey, Kusha.
**kushal** 01:57 Hello, hello, Kemi?
**Reiley** 02:02 Yeah, we can.
I guess it's probably very lightweight, because Jeremy and I don't have any agenda item today.
We'll give a minute and see if Trask has any topic that he would want to join.
Is this the first time you joined this meeting?
**kushal** 02:30 Yeah, this is my first time, like, I've joined… sector meeting, and
specifications, SIG specification meeting, so, yeah.
Security is my first.
Damn, I'm joining.
**Reiley** 02:44 I see. So we're a bit under stuff here. Jeremy and I are leading the security effort, and most folks, I think, currently on the security side are coming from Microsoft.
Actively looking for Like, people who… one tool…
**kushal** 03:00 How often have been interested in the security space?
**Reiley** 03:03 Ideally, like, we want more Have more folks, coming from other companies.
**kushal** 03:09 Sounds good. May I know which language you're working on? Like, it's a Golang, or…
**Reiley** 03:13 Oh, we are working across the board, so to give you some idea,
We're driving the security standard across the OpenTelemetry product. I'll give you some examples. When people report a security vulnerability in private, then what, like, what maintainers of each language should do? What's the expectation?
And as users of OpenTelemetry, what should they expect?
So we try to define those processes, and as part of that, we come up with tools and procedures to help people.
**kushal** 03:51 Sounds interesting, yeah.
Actually, I'm contributing to… recently, I just solved an issue in collector content, and I'm just looking around, like, which repositories
suits to me. So, one I found is collector contract, and… Yeah, I just… Looking around.
**Reiley** 04:11 Yeah, so some examples, like, we… we do have some, like, language-specific contribute repository, and people contribute a certain thing, and then later, it… it…
it didn't get enough traction, then, like, you see a stepping back. The question is that component is still there in the repository, and it will have maintenance issues. There's downstream dependency with security issues, then what should we do? Like, one option, of course, is go and remove the code, right?
The second option is you want to find someone who can own it. Sometimes, like, maintainers, they try to be nice, not too aggressive, but that leaves open telemetry in a dangerous zone, because the scanners will detect vulnerability, and in general, make OpenTelemetry look very bad from a security perspective.
**kushal** 04:57 Sounds… sounds interesting, yeah.
**Reiley** 05:01 Okay, I guess we're 5 minutes past, we don't see Trust here.
So, I… I think unless any of you have specific topics, then we probably will skip today.
**Jeremy Corley (Microsoft)** 05:17 Yeah, I didn't… I didn't have anything else. I'll ping Trask later, maybe, when I see him, and
Asko at his update to the dashboard.
If he's picking up on that.
It's beautiful.
**Reiley** 05:31 Yeah, so Kusha, I have a question for you. So, since you're exploring, and maybe you can do a quick intro, and Jeremy and I can see how we can help, like, if you want to get more plugged in.
**kushal** 05:42 Try to help, I think.
**Reiley** 05:43 Like, what are you trying to do here, and how can we help?
**kushal** 05:47 Sure. So, basically, I started my contribution in, like.
2024, I started looking into this Cloudnative Computing Foundation.
And there, I was contributing to Kubernetes, and I've contributed to Prometheus.
And after that, I got selected in Linux Foundation Mentorship Program.
Where I was contributing to Prombench as an LFX mentee, and…
After that, contributing into Prometheus, I just get to know about this OpenTelemetry.
And, yeah, I'm just looking around, like, what else I can do better in this organization. Because I saw that, OpenTelemetry is used by many companies, and
there is one company who is asking me for, like, do you know OpenTelemetry? And at that time, I don't know. So, that's the thing which kicks me to go and explore this,
new open source project. So, yeah.
Okay, so… And it's been, yeah.
**Reiley** 06:49 I've been with OpenTelemetry since the beginning of the project, and…
We started, around, like, 2018-19.
And the product has grown to…
one of the most active products under CNCF.
I… I… I… I think, like, last year, when I looked at the statistics.
And Kubernetes is the number one most active project under CNCF. OpenTelemetry is the second.
looking at the trajectory, I guess if I take a scan today, maybe it's the most active one.
So, telemetry is a very broad space, and before OpenTelemetry, there's barely any, like, industry standard, so, like, every developer would care about how do you observe your software, right? How do you instrument your code? Like, how do you add a log?
How do you track metrics from your code for performance for troubleshooting?
And OpenTelemetry really, like, fills the… gap, and… And I think that's why…
We're getting a lot of trajectory, and…
And I have no doubt that.
**Jeremy Corley (Microsoft)** 07:56 all the time cool.
**Reiley** 07:57 play an even more important role. So, glad that he discovered us.
**kushal** 08:02 Oh, yeah.
Thanks.
**Reiley** 08:04 Yeah, and as part of that, like, when open telemetry being used in almost all the software supply chain, you can imagine, like, any security issue.
**kushal** 08:11 Mmm.
**Reiley** 08:12 It's becoming a broad security issue for the entire software industry.
So we're seeing more and more of those cases.
**kushal** 08:22 Yo.
And also,
it's related to eBPF. I was, I have con… like, I have a basic understanding of eBPF.
So, that's also quite interesting, looks interesting to me, like, how this thing works.
Behind the scene, and yeah.
**Reiley** 08:45 Yeah, so EBPF is more covered by the providing state.
one of the telemeters, you know, that really goes to the low-level details for performance. Okay, so.
Thanks for the introduction. Feel free to reach out to me and Jeremy on Slack, we can follow up. And this meeting, like, we typically have, like, bi-weekly meetings, but due to the lack of, like, folks, especially, like, it's more, like, Microsoft
dominant hit. We're… we're looking at the expansion, so we definitely, like.
Be willing to take additional help from you and from others.
**kushal** 09:25 Yeah, I'm happy to help you guys, like…
If… is any help, like, if you need any help, I will… I'm there.
**Reiley** 09:33 Yeah, so if you look at the Sikh security repository under OpenTelemetry.
And this is our home repository, so we have the issue tracking there, and you can see some of the proposals and PRs. I have a PR, which I plan to
Make an update.
I… I can send a link in the chat.
Yeah, just put that in the chat. So take a look at the PR, and we have another PR open. Some of them…
like, haven't been updated because I came back from vacation, then got randomized by something else, but I do plan to…
Come back before the end of the month.
So I hope that will give you some idea, and see if that aligns with your interest.
**kushal** 10:41 Sounds good, yeah.
**Reiley** 10:42 Okay, I think that's all. Pretty lightweight for giving the time to Ira. Thank you.
**kushal** 10:50 Yeah, goodbye.
**Jeremy Corley (Microsoft)** 10:50 Thank you, Governor.
