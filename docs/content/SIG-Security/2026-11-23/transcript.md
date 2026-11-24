SIG: SIG Security
Date: 2026-11-23
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Trask Stalnaker (Microsoft Corporation)** 01:26 Hey, Reiley.
**Reiley Yang (Microsoft Corporation)** 01:28 Any cost… Are they?
**Trask Stalnaker (Microsoft Corporation)** 01:33 Good, just grabbing a… Re… re… regenerating my coffee between meetings.
You might not have seen, I posted in the maintainer channel, GitHub released a feature on Friday.
That we're long waited for, that allows us to give maintainers access to security advisories.
Awesome. So, testing it out right now on the, Java Instrumentation repo. I just… I, I created the custom role.
and I, added it into the Terraform, So, once… once I… make sure that all works, then, my plan is to roll it out. Oh, I have a community issue.
Tracking that.
**Reiley Yang (Microsoft Corporation)** 02:52 Hey, Jonathon.
**Jonathon Klobucar** 02:54 Hello.
**Trask Stalnaker (Microsoft Corporation)** 02:56 Ayy.
Yeah, so it still doesn't cover… Merging fixes from temporary private forks.
Although, I guess that kinda relates to… the discussion that you and Robert were having.
In one of the PR, SIG security PRs, about… the process for… Patching and releasing.
Honestly, like, the way that I've been doing it in repos, in the Java repo, has been… Because it's such a pain to… the private fort… Like, we'll use the private fork to… draft the PR and review it amongst the maintainers.
But then… I don't actually merge it from there, typically. I will just… wait until right before a release, and I'll send a sort of nondescript PR, non-dis… Not security vulnerability sounding PR.
And then… Make the release right after that.
**Reiley Yang (Microsoft Corporation)** 04:35 Yeah, I understand. I've seen similar cases.
So I… I… I feel like for the direction, I don't feel comfortable of recommending people to just go public. I understand there are some mechanical… blockers or obstacles that make it difficult, but I… I feel like we… we should still push for the direction that fix, like, if the vulnerability has been reported in private, and people haven't got reasonable evidence saying this is already a public domain knowledge, then they should do as much as possible to not disclose any details to the hikers before people have the binary shakes. So, I…
**Trask Stalnaker (Microsoft Corporation)** 05:23 Yeah. I agree in theory, I'm just not sure how to put that into practice.
Because you can't run GitHub Actions in private forks, like, they're so… Useless.
**Jonathon Klobucar** 05:37 Yeah, the only thing they're useful for is, like, does this code do the thing? And then, like, you can do the attestation that the POC no longer works locally, right? And you're like, great, I think it's fixed, but then, yeah, like, I feel…
**Trask Stalnaker (Microsoft Corporation)** 05:51 We use it to review… yeah, we purely use it as a place for maintainers to review the code.
**Jonathon Klobucar** 05:58 Yeah. And stage how you want to, like, well, that's also… that can also be in the GitHub service advisory of how you actually, well, security advisory, how you actually, like, plan to… to, like, roll it out and announce, and… I think right now, I mean, if it goes into the repo, like.
You've already got people that are scanning commit trees for silent fixes, right? That's just the thing.
Especially with AI, so… I think as soon as it lands…
**Trask Stalnaker (Microsoft Corporation)** 06:29 Yeah, and not that I feel comfortable even… yeah, I forgot, that's, I think the main… one of the reasons I don't… merge directly from the private fork, because I can't run the GitHub action anyway, like, I want to run… Yeah, like, if you go through the.
**Jonathon Klobucar** 06:43 But then it has to be, like, a nondescript thing, but as soon as, like, as soon as you… I would say putting up the PR is not as big of a deal. I guess it depends on the severity. If they're, like.
like, not critical, like, I think it's probably fine to some degree, right? Like, it's not great, but it's like… fine, and then you, like, as soon as it merges, you release the CV and cut a version, right? Like, ta-da!
I don't think… I don't think there's a way around that right now, like… Particularly, like, if… even with a nondescript PR, if it, like, lands as a nascent commit, people are just scanning with AI to be like, oh, like, what… what changes landed? Oh, look, this looks like security-related.
**Reiley Yang (Microsoft Corporation)** 07:26 Nope.
**Jonathon Klobucar** 07:27 And then you get, like, In bad spots.
**Reiley Yang (Microsoft Corporation)** 07:31 Yeah, I want to give one example. I know this is different from how OpenTelemetry is today, but imagine this, like, I used to put a lot of engineers from Microsoft on OpenTelemetry.net, not anymore.
But at that time, like, most of the maintainers are for Microsoft, and they're internal build pipelines. We know how to publish things, and we have reasonable I wouldn't say it's reasonable. They have… they have a lot of access to some of the engineering mechanisms, so if we notice there's a critical CVE that we want to fix, and we don't want to disclose that, because there's so many important things that are depending on it. What we'll do is we'll just have those Microsoft engineers doing a fix in a private branch, and they'll… they'll comment how to run and build a pipeline, and leverage the Microsoft internal system to get everything validated, and then they'll use their admin or, like, maintainer power to just push the binary, like, NuGet package.
And then we'll… we'll communicate the… the fix in… in a murky way, so let people know there's a critical CVE, this is when they should consider the fix, but we don't disclose any details. And because these are binary, I think for people who want to reverse engineer and try to compare the dish, they still can, but it's much more difficult.
then waiting for several days, for the major system to take the patch, then we'll merge the PR in the public repository and disclose that, like, all the details.
So, let's fine.
**Trask Stalnaker (Microsoft Corporation)** 09:07 Yeah, let's talk about how, I mean… I don't think there's disagreement there. It's just how… let's talk about how we could… what it would require to implement something like that in OpenTelemetry.
For example, we can make… We can make private… Repos in the org.
Which… you know, would have access to GitHub Actions and release workflows and that kind of thing.
**Jonathon Klobucar** 09:42 Yeah, I just think that, like, on some of our repos, like… like, some of them, you don't just release a binary of, like, Node will always… Node and Python and, you know, mostly… I mean, Java, I guess you can release a jar, but… Unless you're obfuscating it, it just is all the files in it, right? So…
**Reiley Yang (Microsoft Corporation)** 10:00 No.
**Jonathon Klobucar** 10:00 So, I think we've got some headwinds with, like, oh, we released this binary, like… don't… just Arizona's critical, we haven't released it yet, but, like, I do think that there's a way that… if we do the… I think to Trask point, if we do the internal testing, like, if we can figure out a way to, like, make, like.
a temporary repo, which I think… I mean, GitHub has a little checkbox for this repo as temporary, and we can do, like, a hard fork. We could run, like… some set of… some subset of machinery for, like, PR floor or whatever, right? Like, let's check, tests, let's do all stuff, and then you could… pull the patch over. I still think it's a big pain in the butt, and I would only reserve it for issues that are, like.
critical RCEs for the rest of them, I'd be like, okay, like, we can put the patch in, we can put the PR in, keep it kind of undescript, and then, like… those tests run for, like, an hour or whatever, and then we release, and you say there's a CV and a new version. I think that that's… Fine.
Because most of the lower issues are gonna be, like, a DDoS, or something that's not great, but it's not gonna be… I just… Pwned you through OpenTelemetry.
**Reiley Yang (Microsoft Corporation)** 11:13 Right.
**Jonathon Klobucar** 11:14 Does that… does that make sense?
**Trask Stalnaker (Microsoft Corporation)** 11:17 Yeah, so maybe, like, a CVS, CVSS score threshold?
**Jonathon Klobucar** 11:23 Yeah.
Is how we, sort of.
Like, if it's a bunch of lows and mediums, like, I don't think it needs to be super secret, but yeah, as I said, if there's, like, wow, this is… This, this, like, definitely dumps a lot of memory.
**Reiley Yang (Microsoft Corporation)** 11:39 Or, like, remote code execution, right?
**Jonathon Klobucar** 11:41 Yeah.
**Reiley Yang (Microsoft Corporation)** 11:42 most one, like, if you have remote code execution, and you're not releasing a source-level package, then I think there are a lot of things we should do. And when I have something like a GitHub, like, OpenTelemetry private organization, I'm even thinking, like, if a certain, like.
SIG, for example, OpenTelemetry.net, they're saying, we have a lot of users, and… And those are running back-end services, so if you have remote code execution, it's terrible. We would be willing to have something like OpenTelemetry.NET, private.
like, a repository under an OpenTelemetry private organization with all the CICD pipeline, and only maintainers have access there. I think there are ways to do it, so I'm, like, basically, I'm not ready to give up and just make everything public.
**Trask Stalnaker (Microsoft Corporation)** 12:34 So, if we did a private repo, definitely we could do the… I mean, it's easy to do the PR validation over there, running GitHub Actions.
Doing the release over there, is certainly possible.
But… Would have to be, like, getting that release sort of back into the public repo, Like, everybody would sort of need to redo that whole, like, release workflow. That would be a pain… that would be painful, but… but possible.
**Reiley Yang (Microsoft Corporation)** 13:12 Yeah.
So what I've seen, at least people are doing that in Microsoft, if they have this private fix, and they release a binary patch, and they gave a certain number of days, like, let people explicitly know that these are the number of days you can apply the patch, and after that, everything will just be public domain. And by that.
time, they will… they will take this private fix and send a public PR and merge that, and quickly do the release. If they have, like, in parallel, they have a release, they're stepping on others' toes, they have to do some, like, 3-bit merge or something.
**Trask Stalnaker (Microsoft Corporation)** 13:48 Oh, I see, so you make the… you make the release out of the private repo, and then… You would still then, a few days later, make the release out of the public repo?
**Reiley Yang (Microsoft Corporation)** 14:02 Yeah.
Yeah, so the private release will tell you this is an urgent hotfix, it's a stable version, we've tested everything, and you should just shut up and go and apply it, and we'll give you 7 days for you to apply the patch. After that, everything will be public.
And then after 7 days, if there's a… like, during that time, maybe the public repository will just go and do its own, like, next version release, whatever. So that will not have a private fix, but by the date.
We'll have the private fix merged back to the public, and if… if it needs another release, whether it's a major release, minor, like, patch release, whatever, you just do it.
**Jonathon Klobucar** 14:39 But none of our… like, there's so many languages that our releases aren't binary format, so then you're just releasing the code as a private fix, right? So…
**Reiley Yang (Microsoft Corporation)** 14:47 No, no, so I have very different thinking there. I think if you're a source packages, then just give up.
**Jonathon Klobucar** 14:55 Yeah.
**Reiley Yang (Microsoft Corporation)** 14:55 The first time you receive the security advisory, I still think we should discuss that in private, because by that time, you don't even have a fix. People don't know, right? So, you should discuss and take as much time as you need, and once you figure out, Jesus, this is how I'm going to fix my code.
You should quickly fix the code in the public domain and release it.
There's nothing you can hide.
**Jonathon Klobucar** 15:17 So which… which ecosystems do we give binary releases of OpenTelemetry for?
**Trask Stalnaker (Microsoft Corporation)** 15:23 I was gonna ask, where do you consider Java, for example?
I mean, it's technically binary, but it's effectively Source code, given.
**Jonathon Klobucar** 15:35 Here's the class file path, right?
**Trask Stalnaker (Microsoft Corporation)** 15:37 Generate.
**Reiley Yang (Microsoft Corporation)** 15:38 the… Yeah.
**Trask Stalnaker (Microsoft Corporation)** 15:39 Yeah, reverse engineer the bike code.
There have been Java decompilers for decades.
It's not even an AI thing.
**Reiley Yang (Microsoft Corporation)** 15:51 Yeah, so I… like, my position is I… I guess it's probably a reasonable choice for the maintainers to make.
they know the language better, but I just don't want us to simply close the door and just try to say, everyone has this low bar, just do everything in public.
**Jonathon Klobucar** 16:07 Oh, I mean, I don't think anyone's arguing that we do everything public. I'm saying there's… I think for the fixes, I think we have to find a way that's, like.
supporting private until we disc… until disclosure, right? Like… That's, that's, that's, I think, the, I think should be the goal.
**Reiley Yang (Microsoft Corporation)** 16:26 Yeah.
**Jonathon Klobucar** 16:29 And there's policies, yeah, but like, yeah, and like, also, part of it is there's pressure to be like, I found this fix, you aren't fixing it, and, like, well, yeah, there's, like, a billion other fixes that are going on, you know, so… That's… It's just… it's just prioritizing it and setting that expectation.
How… I guess, like, a meta question is, how… I don't see many of the reports, like, access-wise, like, how is the volume? Has it dramatically gone up from, like, a bunch of AI reporting, or is it… Okay, or okay.
**Reiley Yang (Microsoft Corporation)** 17:09 Yeah, it has increased, and the quality is not bad at all. And recently, I think even the Anthropics model, they try to help, so there's an OSS scanner, you can explicitly add that.
in your repository security setting, and by adding that, you're basically saying, I don't worry about DDoS attack. The Anthropics model can file as many security advisories.
**Jonathon Klobucar** 17:34 Yeah, yeah. I've used… I've used their scanners pretty extensively for stuff, that makes sense. It was more like… that, and it's just like, yeah, like, you know, I'm, you know, I, for instance, where I'm at, I'm getting, a lot of random people submitting, like, just a ton of AI slop comp, and I was curious if, like, the volume had gone up for OpenTelemetry, and if the quality had… Gone down as well.
**Reiley Yang (Microsoft Corporation)** 18:00 So the volume did increase, I would say, between 10 times to 20 times.
**Jonathon Klobucar** 18:05 The common…
**Reiley Yang (Microsoft Corporation)** 18:07 I… I personally feel the quality's pretty good, like…
**Trask Stalnaker (Microsoft Corporation)** 18:11 It's good now. There was definitely a phase where we were getting a lot of bad slop.
**Jonathon Klobucar** 18:18 Okay.
**Trask Stalnaker (Microsoft Corporation)** 18:19 The models have gotten better, though. Yeah.
**Jonathon Klobucar** 18:22 So yeah, even people copy-pasting whatever the model says is at least better than what it used to be.
Even if the scoring is probably still subject to be like, it'll be like, I found critical, and you're like, no.
**Reiley Yang (Microsoft Corporation)** 18:39 Right, and there are things that people start to, like, require some explicit proof of the repro. They're saying, you just gave this, like, theory, we're not going to take it, because they're just too.
**Jonathon Klobucar** 18:51 Yeah.
I think… I think if our repos don't have a security threat model that tells you what's in scope and what's not in scope, we probably should make that a recommendation for everybody.
It'll help a lot, because then the agent will automatically be like, oh, let me go read in the security MD, oh, these things are not in scope, so I won't report them.
**Trask Stalnaker (Microsoft Corporation)** 19:24 Alright, yeah, I can… Reiley, I can get behind that with a threshold of only doing that for… You know, some level of criticality.
Because I don't think we're… we actually get that many… That are… that.
critical.
**Reiley Yang (Microsoft Corporation)** 19:50 Think about this as, like, we want to leave like, some space for the maintainers if you want to shoot for a higher bar, but I don't want this to be a requirement. Like, think about this, if you're a maintainer of some language SIG, and you release a binary packet.
And, package, and you don't even have the private symbol there, so people, like, it's hard for people to reverse engineer. Then, it's your choice whether you want to meet a higher bar. You're saying, I don't have enough bandwidth, even if I got a critical CVE, I would just go and do it publicly, because doing it privately requires a lot of extra work, and I just don't have bandwidth, so either I just don't fix it, or I'll do it publicly. I think in that…
**Jonathon Klobucar** 20:34 I think we need to also, like, I agree with you, that also, I think, implies, like, we just need guidance on how to do private fixes with tooling better, because I don't think… I think that might be a gap, like, I think all of us have experienced how to do it, but I'm not sure… every maintainer has, like, good guidance on, like, how to do private fixes, so that might help a bunch of this.
Because if you can give those instructions to, like, your agent, it'll probably try to do the right thing privately.
And then, yeah, guidance instead of enforcement, and then I would say also, like, you know, we should also… I feel… I don't know how to describe this, but I feel that we should explain to maintainers that they're getting a lot of volume of reports, work on the most important ones… Try not to burn out, like, all sorts of stuff, because… I feel that that… that… that would be good, like, to… To be like, you know, you're a small team, try to figure out which ones are the most harmful, and, like, don't… Like… Be pretty ruthless in prioritizing security, like, reports if you have to.
Because I do think that burnout… security, like, triage burnout is pretty real.
**Reiley Yang (Microsoft Corporation)** 21:54 Yeah, that's a good point.
**Jonathon Klobucar** 21:55 Yeah.
**Reiley Yang (Microsoft Corporation)** 22:02 Okay, I guess that's the only topic, so I'll get back to the PR and add a comment there, still maintain the position, but give more actionable suggestions, instead of just blocking.
**Trask Stalnaker (Microsoft Corporation)** 22:17 Sounds good.
**Reiley Yang (Microsoft Corporation)** 22:19 Okay, cool.
So, Jonathon, can I call you right after this meeting? Maybe take, like, 3 minutes?
**Jonathon Klobucar** 22:26 Yeah, yeah, yeah, give me a call, I've got a few minutes.
**Reiley Yang (Microsoft Corporation)** 22:28 Okay, thank you.
**Jonathon Klobucar** 22:29 Perfect, yeah, thank you.
**Reiley Yang (Microsoft Corporation)** 22:30 That's awesome.
