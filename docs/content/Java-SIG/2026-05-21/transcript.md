SIG: Java SIG
Date: 2026-05-21
Duration: 53 minutes
Zoom Recording URL: https://zoom.us/rec/share/jof_RXgG6ZXrzKf5kKZMN2u431lQd4N9tSNDwnm9Agvy0W5AavHZf2eJeYGM04S7.pmCALAQgtGdLHX9g
============================================================

## Zoom Recording Transcript

**Gregor Zeitlinger** 00:26 Hello?
**Jack Berg** 01:31 Hello.
**Gregor Zeitlinger** 01:40 Hi, Jack!
**Jason Plumb** 02:11 It's rare that we have such an empty agenda.
**Jack Berg** 02:19 Yes, please add your topics if you have them.
Somebody has messed with your font.
**Jason Plumb** 02:31 Yeah… I mean, I don't love the original one, I just love the consistency.
**Jack Berg** 02:45 That's not right.
Wait, so what did you do? Did you have the… The heading is a different font than the body.
**Jason Plumb** 02:56 I… I mean… I think it's been like that forever, yeah.
**Jack Berg** 03:09 Great news, everyone. OSGI support is one PR away from being finished. I know everybody cares deeply about this, so… It's been in the works for 5 years.
**Gregor Zeitlinger** 03:28 But it must be good.
**Jason Plumb** 03:30 Like, if I'm walking along and I see OSGI, I just sort of turn and go over here for a while.
**Jack Berg** 03:36 It's a pretty wild thing, having, like, gotten familiar with it. So, like, there's this… One of the things that it really breaks with is SPIs. If you have a module that needs to load SPIs, you need to explicitly add metadata in your manifest.mf file that says, like, hey, I need to load this SPI.
And if you provide implementations of an SPI, you have to add metadata in manifest.mf that says, like, hey.
I load, or I provide this SPI, but at least on, like, the provide side, like, that information is already available. Like, so…
**Jason Plumb** 04:15 Yeah, are they trying to prevent mistakes or something? Like, why do that?
**Jack Berg** 04:18 It's just, like, straight, redundant information, and, like, of what's in services, resources, or meta…
**Jason Plumb** 04:25 Yeah.
**Jack Berg** 04:25 and.
**Jason Plumb** 04:27 Maybe it's another level of control, like, you can just have the bucket of everything, and then here's, like, what you actually want? I don't know. Seems… seems messy.
**Jack Berg** 04:37 Yeah, and it's, it just makes it, like, really error-prone as well. And it's like the Gradle plugin that you use to generate this metadata. It's not like it's smart and looks at your meta-inf services and, like, automatically, you know, copies that information into your manifest. Like, you have to explicitly, like.
You know, state that a second time, so…
**Jason Plumb** 05:02 Yeah.
**Jack Berg** 05:05 I can't say I'm a fan.
**Lauri** 05:15 I think nowadays, not supporting OSGI is actually fine.
**Jack Berg** 05:23 And I would… I would have taken a stronger stance against it if it required anything on our part besides adding metadata in manifest.mf.
like… if it required us to take additional compile time dependencies and add new, you know, actual code that, you know, it introspected on, but it didn't. So, it's just some tests and some metadata, and I was like, okay.
I don't want OSGI… lack of OSGI support to be, like, a reason why somebody doesn't pick up the OpenTelemetry API or SDK, like… Okay, so we got one topic. I don't know whose topic that was, the Java Instrumentation V3 review?
And maybe that's a standing topic, just to make sure we go through that each week, and don't forget about it.
**Gregor Zeitlinger** 06:29 I just added, two things, where are you looking, or did I edit in the wrong place?
**Jason Plumb** 06:35 Yeah, there's a.
**Jack Berg** 06:37 Oh, oh, I'm sorry. I was looking at the wrong place. I was looking at template.
**Gregor Zeitlinger** 06:41 Oh, okay.
**Jack Berg** 06:49 Okay, so then I guess we'll just start with Gregor's topics. Pinned versions for muzzle distros.
**Gregor Zeitlinger** 06:55 Yeah, I already just discovered that I accidentally broke distros with a feature that I added a couple of weeks ago.
I'm just wondering what to do about it. So the feature, I, Still liked, because it makes repeatable builds, meaning that it does not depend on what is currently the latest version.
And muzzle checks, because it looks at the JSON file instead, but… Bistros don't work, I haven't really figured out why they don't work, but I'm still trying to… understand what we want to have for distros. My first idea was just use the file from upstream, but that doesn't work, because distros might have different Dependencies. That's… That's as far as I got. Laurie, maybe you already have more ideas on that.
than I do.
**Lauri** 07:54 I didn't look at it too thoroughly, but I think, Checking for the presence of the file.
This is… is never go… like, that file is never going to work with, Work with usages outside the instrumentation project.
**Gregor Zeitlinger** 08:14 Yeah, yeah, I'm not trying to argue that, this, is indeed working, I'm just trying to, who, Decide what a good way forward is.
**Lauri** 08:27 Well, there are basically two options, like, You can force everybody who's using that feature to generate the same file.
Or you can fall back to whatever it was doing previously, if the file isn't present.
**Gregor Zeitlinger** 08:43 Yeah, and I don't really like either one of those. The first one seems like it's too much work for distro authors.
And the second one… Well, maybe the second one works.
**Lauri** 08:56 The muscle checks aren't repeatable anyway, because they choose a random set of versions.
**Gregor Zeitlinger** 09:07 Sorry, I did get that. What are you suggesting?
**Lauri** 09:10 like, the muscle, like, The muscle check plugin, it isn't, like, completely repeatable anyway.
Even if you fix the latest version, because, it uses a random set of, Aversions to test.
And some of those versions might not pass for whatever reason.
**Gregor Zeitlinger** 09:36 You mean the feature is not working as, advertised?
**Lauri** 09:40 No, like, for example, Maven repositories contain broken artifacts that occasionally fail.
like.
**Gregor Zeitlinger** 09:51 Yeah, okay.
**Lauri** 09:52 If it chooses one set of artifacts, everything works, but if it stumbles upon one bad artifact, then it occasionally fails.
I guess your idea was to get repeatable builds, but I don't know if that's even possible with that thing.
**Gregor Zeitlinger** 10:07 Well, I wanted repeatable builds in the way that an upgrade or a new version does not break the build for everyone, and.
**Lauri** 10:17 Hmm, that…
**Gregor Zeitlinger** 10:17 is working. It does not fix all problems, right?
**Lauri** 10:25 Yeah, I just think that it might be easier for you to just somehow figure out How to make this plugin work without that file.
**Gregor Zeitlinger** 10:33 To basically as before.
**Lauri** 10:35 Yeah, well, inside agent, if the file is present, like, then it's fine, but if it's used anywhere else, like, I think, our extension example and distro sample might also use it, but apparently our builds probably Don't, don't actually test whether it works there.
**Gregor Zeitlinger** 11:02 It does not, otherwise we would have found the problem earlier.
Yeah, okay, I'll try that, thanks.
And I think I'll move my next one.
More to the bottom, since it's more open-ended one.
**Jack Berg** 11:27 Okay.
Okay, so my issue is next then, and so I have this PR open, to prepare for, this upcoming event sometime in the mid… middle of the year, when we're going to stop publishing the Zipkin exporter.
In align with spec guidance. And before we do that, I want to get rid of all shared internal code references from other modules.
So that it's guaranteed to continue… the last version we publish will be guaranteed to continue to function, you know, even if there's API changes in those shared internal code references, because they don't exist.
So, like, you would be able to use an older version of the Zipkin exporter with newer versions of the SDK.
That's the idea.
And so, as a part of that, one of the things that Zipkin does is it uses this instrumentation suppression, little API we have that prevents, the agent from instrumenting the exporters themselves.
And… let's see if I can find this… Here's the class.
It's called Instrumentation Utils, and all of our exporters, they wrap their export function in this suppressed instrumentation runnable, and the agent calls this should suppress instrumentation function, and, in a variety of places to make sure that it doesn't, you know, have these cycles of, of instrumentation. And so, yeah, I wanted to call this out for the instrumentation maintainers, that this package is going to change, so… That's happening.
Any comments?
Mr.
**Jason Plumb** 13:21 I think we use that in Android, or maybe we just write to the context in the same way, but I think we use it either in disk buffering or in Android, so thanks for the heads up.
**Jack Berg** 13:29 Well, it's an easy fix for everybody else, because, you know, it's just… you'll get compiled time, error.
But instrumentations probably has a subtler dependency.
Anyways, that's all.
Cool.
Jason.
**Jason Plumb** 13:49 Oh, I… you know, it was a light agenda, and I just… I saw this this morning, and I was like, why did this person think we want changelog Generator in this project? Because I don't want it.
So I did put a block on it, but, like, I'm… I mean, does anybody want this?
**Gregor Zeitlinger** 14:10 You mean this one, or any kind of changelog generator?
**Jason Plumb** 14:13 Well, this one… Is the task at hand.
It feels unnecessary to me, but…
**Gregor Zeitlinger** 14:23 Yeah, I'm asking because in other projects, I use change block generators, but they are used.
**Jason Plumb** 14:27 No.
**Gregor Zeitlinger** 14:28 smaller projects.
**Jason Plumb** 14:30 I mean, like, I think SemConf uses one, and other repos use them.
**Lauri** 14:36 Trask built his own changelot generator. I think we are going to use whatever he built.
**Jason Plumb** 14:44 Cool.
**Lauri** 14:45 And in the instrumentation repository, I think he did something that uses AI to somehow summarize the pull requests, and .
**Jason Plumb** 14:52 Yeah, totally, it's part of the release, but it… like, so this, though, this changelog generator requires people, when they submit PRs, to make an additional file, and it has to be in the right format, and it has to be in the right location, it's just like… Submitting PRs is so much work, so much worse.
**Gregor Zeitlinger** 15:09 Oh, this is the one from, Collector, I think.
**Jack Berg** 15:14 Yeah, I think Go uses it pretty widely across, like, a variety of Go projects, and I work over in the injector SIG, and it got… it got brought over there as well, so, like, it's something like this. If you go and open a PR against one of these repos.
Every single, not this one, this one's, like, a bad example, because it's just, like, Changing the workflow, but, like, Let's see… Let's see if we can get an actual feature.
**Jason Plumb** 15:47 There's also… Yeah, I think SemConf also has it, but there's also tricks to, like, instruct the tooling not to verify the changelog for small things, it's like… I don't know. It just feels…
**Jack Berg** 16:00 system that says this isn't needed.
**Jason Plumb** 16:02 Yeah.
**Jack Berg** 16:02 You don't have that label, your build fails without this changelog entry?
It's basically making the changelog very structured, right? So you say, like, what type of change it is, what the related issue is, things like, if you have a multi-module project, which modules where change is a part of it, and that's really good for the receiver, which has to, like… or for the collector, which needs to organize things by the specific components. It's arguably good for a place like Contrib that has lots of components as well, for places like instrument Which has lots of components, but… You know, I think… what Trask has done, with AI, and what I've been doing in CORE are similar things. We have to do a classification exercise, take all the PRs that were merged and classify them into categories, and It works reasonably well right now, such that, like, I personally, for core, wouldn't be interested in the additional overhead.
Just to get, you know, the additional structure.
Just adds extra friction.
**Gregor Zeitlinger** 17:02 Sweep.
**Jack Berg** 17:04 I don't know what you all think in, in contributing and instrumentation.
**Jason Plumb** 17:09 I'm not hearing from anybody that they love this, but if you do, now's the time to bring it up, I guess.
I think dressing is awesome.
**Trask** 17:17 I don't hate changelog, Jen. I mean, it's… But I also am not motivated to pull that in at this point.
I mean, the thing that's… Nice about it is it sort of brings a little bit more attention to… The changelog entries that we create when the PRs come in.
And with… certainly with, AI now, they're a lot easier to… I mean, you just pretty much have AI generated.
And we can review it, but… I don't know, I don't have any… Strong feelings at this point.
**Gregor Zeitlinger** 18:07 I really like the semantic PR titles, which you also see here, and it tells you here it's a feature, it's .NET, and for most of the projects, that's exactly the kind of structure that I want to have.
Yeah, okay, it's contradictory, but you get the point.
**Jack Berg** 18:29 I wasn't actually making that point. I was saying that, like, changelog gen, you know, does that classification as well.
But… You know, with additional, additional structure, like the component, I think, is a nice thing for complex projects.
But the question for me is, like, do we want to add the additional Friction for contributors and for ourselves.
**Jason Plumb** 18:57 That's my main gripe about it.
**Jack Berg** 19:00 I mean, it would just be a little skill for the agent to write. You would just, like, say, like, hey, write a changelog entry, it's a bug fix, it affects these components, and… It wouldn't be too much different than writing a commit, but being a little bit more structured.
**Trask** 19:17 Yeah, definitely, AI coding has changed my… Leaning on the changelog chin.
Because I did find it kind of a hassle, you know, like, a little bit more of a friction before.
But… that feels… Alleviated to me.
The one nice thing about the changelog, Jim, is as a… for making releases, like, you just… Click release at any point.
You don't need to go through, sort of, the changelog.
Generation and massaging.
Which takes some time, even with the tooling I have now, I still need to look over it.
**Jack Berg** 20:10 Yeah, it's probably, like, 15 minutes for me, each release, so not zero.
**Jason Plumb** 20:18 Yep, same.
**Trask** 20:23 instrumentation repo has a lot more PRs, generally.
**Jack Berg** 20:27 Yeah.
I believe it. I believe it could easily take 40 minutes.
I think in either case, though.
the way to approach this is not to just open a PR that's, you know, changes the process, it's to jump in… to open an issue, to, you know, raise a discussion and get consensus.
**Jason Plumb** 20:49 Yeah.
**Jack Berg** 20:50 code owners, and then… and then open the PR after you reach agreement, so…
**Jason Plumb** 20:55 Yeah, I mean, I think this person's just trying to help, but… Yeah.
**Lauri** 20:59 The problem is that in that repository, you can create the issue, but it's almost guaranteed that nobody will respond to that.
**Jack Berg** 21:10 I think it depends on who opens the issue.
And it… as bad as it sounds, like, I think more attention is given to issues and PRs from people that he recognized.
Can we move on?
**Jason Plumb** 21:40 Yep. Thanks, all.
**Jack Berg** 21:46 rigor.
I want to talk about security stuff.
**Gregor Zeitlinger** 21:54 Yep, yeah, since we're just working on, Hardening everything Grafana Labs, I wanted to ask if there's… Something that we have open, that needs a little bit more attention.
Since I've worked on linters, recently, I thought about having, security linters, such as SysMore, enabled on all the repositories.
But, I don't know if there's some thought about that already, how that should be handled, ideally.
**Trask** 22:34 Pyotr, Kilek just, brought that up. I asked him to open a issue in the SIG security repo, specific to Zismor.
just to have a discussion there, I'd like to kind of understand the overlap between CodeQL, Scorecard, and Zismor.
But I, you know, I think it's fine also if there's overlap. I'm curious. I haven't used this more, but I know that several OpenTelemetry repos are, and it Seems like it's a good… it's providing some good insights.
**Jason Plumb** 23:19 There's also this thing I have on my, kind of, backlog… To look into this Hardin Runner thing?
That I just linked to.
I don't… is anybody using that?
**Trask** 23:36 SIG Security Repo itself is using it.
**Jason Plumb** 23:40 Okay.
**Trask** 23:41 I think that's a feature… I think it's actually a feature coming in, GitHub Actions, in GitHub.
It's basically, like, firewalling.
**Jason Plumb** 23:56 Yeah, that makes a lot of sense.
Yeah, it was an exciting time at Grafana, I guess, recently.
Or so I heard.
**Gregor Zeitlinger** 24:09 Can count on that?
**Jack Berg** 24:13 See, Lori's eyebrows are raised. There's… there's blog posts about it.
Yeah, I was thinking about that too, like, is, is there anything we could do to… to impact our security posture, I think we're in a decent spot. I think about, like.
What are the… what are the risk profiles? Like, what are the attack factors is, of course.
You know, bugs in the code, advisories that are unfound, You could try to… Set up agent harnesses to find and fix those.
There's our whole, supply chain bit, which is, like, the keys we use to publish, the keys we use to sign artifacts.
We don't do any rotation of those. The keys are assigned to individuals. I don't think we can get away with that. That's kind of how, things like Maven are structured.
We have personal accounts, and our personal accounts give us permission to publish to namespaces.
**Trask** 25:32 Something I, did recently in the instrumentation repo, which I want to, advertise more widely.
is, the secrets.
I put all the secrets behind, environments.
The kind of confusing terminology from GitHub.
But you can have… so it created a protected environment, put all the, secrets behind that.
And only give access to… Main branch and release branches to that Environment?
Which… Cause that's always kind of… concern me that anybody with write permission to the repo, like, if you get… if you hack and get write permission to the repo.
You can… very easily.
Grab all the secrets.
You can just push a branch with, gitHub action that, you know, logs it.
**Jack Berg** 26:45 That's a good call. Right now, I have a protect… on the core, we have a protected environment that just does the, It just has one secret in it, which is the co-pilot token that's used to build the pull request dashboard.
And… I guess I need to learn what… how environments work.
Because I… Do you just have one protected environment, or is that the name of an environment, and it's… I named it… I named it.
**Trask** 27:15 I named it Protected.
**Jack Berg** 27:18 Okay, and…
**Trask** 27:19 You can optional.
**Jack Berg** 27:20 has restrictions on terms of which branches it can access it?
**Trask** 27:26 Yeah.
But I think generally, just, I didn't find the need for more than one environment in instrumentation repo, at least.
Because basically, I just want secrets available on main and release branches.
which are already protected, meaning you can't… no… nobody with right access can push directly to those branches anyways. Since they're protected, you have to go through PRs.
**Jack Berg** 27:56 So then, I'm looking at the configuration of the protected environment and core right now, and so I don't have it restricted to which branches or tags can access it, but you would, like… what I should do is say that only protected branches can access it, correct?
**Trask** 28:12 Yeah, I think you give it a list of branches, I forget what I did.
**Jack Berg** 28:18 You can either explicitly provide a list, or, all… Branches with protection rules on them, so…
**Jason Plumb** 28:26 Are you looking at Terraform?
**Jack Berg** 28:28 No, I'm looking at.
**Jason Plumb** 28:31 Just the settings page.
**Jack Berg** 28:32 There's nothing… there's nothing secret in here, so I can just show this.
I'm in GitHub Settings, Environments, and then this is the…
**Jason Plumb** 28:41 You're not sharing, Jack.
**Trask** 28:44 MC.
**Jason Plumb** 28:44 Oh, yeah, you are, you are. Sorry, I… this thing is tabbed now. What… how did I… how did that happen?
**Trask** 28:49 Perfect.
**Jason Plumb** 28:50 I know how to use computers.
**Jack Berg** 28:54 You're great at computers, Jason. Don't let anyone.
**Jason Plumb** 28:57 Great.
**Jack Berg** 28:57 otherwise.
Yeah, so this is the protected branch, and I guess, I could explicitly… Select the branches, or,
**Trask** 29:08 Yeah, that's what I did.
Because protected… its definition of protected branches is more broad.
There's, like, probably your benchmark branch.
Probably considered protected.
But, because there are some protections on it, like, you can't, force push override it.
But it doesn't prevent people from, pushing to it.
Directly.
**Jack Berg** 29:43 Yeah, so then the protected branches… I'll just do this right now, so we got, we have main… And then we have releases, wildcard, star.
Alright, and then… that makes sense. That's a… that's a… that's good advice, Trask.
**Jason Plumb** 30:08 So that's… that setting is not something that regular old maintainers can do. I think it requires extra permissions. Like, I don't see those… I don't see environments on other repositories.
**Jack Berg** 30:20 Yeah, so, that's… the guidance is actually shifting on that, Jason. I think for a while, we thought we could get away with all maintainers just having, like, the maintain role, and not Enroll on their repositories.
**Jason Plumb** 30:33 Yeah, yeah.
**Jack Berg** 30:34 It's problematic for security advisories, because if you just have maintain.
you don't have any ability to actually do maintenance tasks on advisories. You can't add collaborators, you can't open a private fork, you can't accept the advisory, you can't request a CVE, you can't do anything, except for add comments to it. And so, the guidance is sort of shifting, like, where, like, maintainers should have admin roles, because it's functionally required, based on GitHub's current permission To take, you know, control of your advisories.
And, yeah, the way you would… you get that right now is with a PR to the admin repo, the Terraform admin repo.
**Jason Plumb** 31:15 Okay, yeah, I figured it was something like that.
**Jack Berg** 31:26 Anything else we can do to improve our security posture?
**Gregor Zeitlinger** 31:31 Yeah, what about, using an agent to scan for vulnerabilities. Anybody tried to do that so far?
**Jack Berg** 31:39 I did that against score.
Spent, half a day or so creating a little harness, and I didn't find anything of note.
I mean, some minor things, but, you know, they were all sort of in this gray area of whether they're bugs or advisories or vulnerabilities.
**Gregor Zeitlinger** 32:00 Anything to share?
How to do it?
**Jack Berg** 32:05 It uses a decent amount of tokens.
Has anyone tried doing that against instrumentation?
**Trask** 32:16 So, this actually came up yesterday, Austin raised it.
And I actually applied yesterday to both the Claude, OSS security program and the, the… But, so Anthropic and, OpenAI Oss… security, program. Or it's OSS, it's, like, they'll give you… they give you tokens, but also give you access to their security harness.
So, I have no idea how… If that will… if we'll get approved, or when that will happen.
So, definitely, Gregor, I support, you know.
check out whatever Jack has, and if you run that against the instrumentation repo, that would be awesome.
**Jack Berg** 33:23 I mean, there's no secret sauce to it. It's about what you'd expect. Like, it's, you know, you work with the AI to come up with the list of types of things to look at.
And, you know, you create different categories and different types of patterns to search for. And then, you know, the thing that I guess made it work for me was being able to break it down and parallelize it into some, like, unit of work that can be applied on… Each module individually, and that works about how you'd expect.
You know, come up with a script that, you know, opens a different agent instance for each module and runs this skill against it, so… And then…
**Gregor Zeitlinger** 34:11 What exactly is, the attack vector that, We want to nail down, because that greatly influences what you get out of it.
I guess.
**Jack Berg** 34:24 In my end, what I was trying to find was…
**Trask** 34:26 It's like…
**Jack Berg** 34:27 I was trying to get ahead of advisories, so anything that might one day be open as an advisory against the repo, like, try to find those preemptively.
**Jason Plumb** 34:40 I did a separate exercise, I think I only did it on instrumentation, but I was looking for any… old… I think I used the word sketchy to the agent, GitHub Actions that might have been grandfathered in, that have been sitting around for a while, and some workflow. And by sketchy, I was really just intending to look at, you know, things that had not really been maintained.
Or that are just, like, owned by some person.
And it was not very exciting.
Fortunately.
**Trask** 35:14 Yeah, I've been…
**Jack Berg** 35:15 Something to be found in Contrib.
**Trask** 35:19 Yeah, definitely.
**Jason Plumb** 35:20 I'm curious about that in the other repos, too.
**Trask** 35:23 I've been very picky about the GitHub actions that we add, because that… vector, really.
**Jason Plumb** 35:30 Oh, yeah.
**Trask** 35:31 frightens me.
And it's so common, like, when you look at repos at all, like… super random GitHub actions that get pulled in, and I don't think people realize how… Vulnerable that is.
**Jack Berg** 35:48 Can you talk more about that? Like, what… what's the vector that you're referring to? I mean, I'm of course aware of, like, pull request target, and I can imagine that if you use different tools in your workflows, those tools could have, like, supply chain attacks. Did you have anything else in mind?
**Trask** 36:07 Well, you don't need… it doesn't have anything to do with pull request target, because if you are using a third-party action, and in your CI build that runs on main.
Right, it can grab your secrets there.
**Jack Berg** 36:24 Okay, so supply chain attack of the GitHub actions that you take a dependency on.
**Trask** 36:28 Yes, yes, yes.
**Jack Berg** 36:30 Yeah, I had that in mind as well.
**Trask** 36:33 And… because, like, with… Dependencies, right, were done, like.
Any dependency, really, can be a problem, problematic.
But I guess, for me, the, the GitHub actions feel, I like Jason's word, sketchy.
You know, the, like, some… repo that has… 7 stars, and just because, you know.
Copilot decided to pull it in, or it saves 3 lines of code of, people use it.
**Jason Plumb** 37:12 Or it's like, you know, I used it at my last job, it's fine, that kind of stuff. Like, and I wasn't really expecting to find anything, but, you know, it could have been something that's been in there for 5 years that we never think about. So just, like, doing that little audit. I'm assuming that the, the security SIG is doing audits like that periodically, but I don't.
**Jack Berg** 37:30 The security SIG is super understaffed.
**Trask** 37:33 Yeah.
**Jack Berg** 37:34 It's Riley and one other person, and yeah, they definitely do not do audits.
**Jason Plumb** 37:42 Okay.
**Jack Berg** 37:43 Maybe they could one day, if… If they staffed up significantly, but…
**Jason Plumb** 37:56 Well, he graduated, so clearly our security is perfect, and we don't have to think about it anymore.
**Jack Berg** 38:01 Yeah.
**Jason Plumb** 38:02 That's the way that works, right?
**Jack Berg** 38:10 There's… I had another idea in my head. I put this one down in the notes. Key rotation on some schedule, would that be, like, a useful thing to do?
Oh, here's the other one. I don't know if you all heard, about some of these recent supply chain attacks, but, they've mostly been in, like, the MPM ecosystem, and they've been pretty bad.
Where you can get, sort of, like, root access to your machine if you, like, have a developer dependency on some of these… these projects.
Because they use, like, this post-install script to, like, get a worm on your machine, and then they can just access whatever they want.
And, so some of the advice that I've heard about how you can mitigate against a certain class of issues is by not not immediately updating your dependencies. So, like, you know, the thought is, like, that most times, if there's an issue in some sort of supply chain attack.
And, you know, it's in the latest version, and so if you just wait a couple of days before updating to the latest version, somebody will find that, detect that, fix that, and, you know, you won't have a worm on your machine.
And so… I wonder if that applies to us in any way, if we should think about that.
**Trask** 39:37 There was a great, debate in the CNCF security tag about that.
Of, whether it was better to take updates right away or to make them delayed.
I do kinda, like…
**Jack Berg** 39:55 conclusion.
**Trask** 39:55 There was no conclusion. It was, it was mainly two opinionated people taking both sides.
**Jason Plumb** 40:03 Like, we could turn zero days into one days.
Great.
**Trask** 40:09 I am sympathetic to the idea, like, I kinda like the idea.
**Jason Plumb** 40:19 Yep, it's another… it's another approach. I mean, it certainly would help against Certain… certain types of attack.
**Jack Berg** 40:28 The first thing I thought about when I heard it was, like, what happens if everybody starts waiting one day, or, like, 5 days, or whatever the period is? Then it just takes you…
**Jason Plumb** 40:37 Yeah, huh.
**Jack Berg** 40:37 Learn about this right away, and…
**Jason Plumb** 40:38 That's my point about zero days becoming one days. Okay.
**Jack Berg** 40:41 Yeah.
**Trask** 40:45 But you also then… I mean, the other… Thing is, you don't get fixes right away, like, if there is a fix.
**Jack Berg** 40:57 Do you need to fix.
**Trask** 40:57 Although I guess…
**Jack Berg** 40:58 Problematic version?
**Trask** 41:00 Although, I guess, E… So the way I set up… Yeah, so we can get… I guess, if it's an actual fix, a CDE fix, it should break that out, it should break that delay.
Because I think Renovate has an option.
Delaying…
**Jack Berg** 41:28 It's to have options for everything, so…
**Jason Plumb** 41:32 I know, at least in some repos, we do the patches weekly, right? Which is kind of interesting, because the patches might be the ones that we should be applying quicker.
Right?
**Jack Berg** 41:44 I wonder if we need to, like, break these down by, like, type of dependency, not, like, major, minor, or patch, like… You know, do we actually need to get our GitHub actions updated right away? Like, those are the ones that could have a supply chain attack to exfiltrate secrets versus actual code dependencies? Does the, you know, what's… What's the risk of having a little delay on code dependencies?
**Trask** 42:13 So, we already have them on a schedule.
And I think it's weekly. On a couple of repos that I'm involved in, I've actually set it to monthly for the GitHub actions specifically.
Because I kind of… I'm getting irritated by all the Renovate PRs. And… the, it'll still… if there's a CVE fix, a real vulnerability-reported fix.
It won't wait for that whole month.
it'll send those right away, so I do think that's a good… Option.
Right? Before… So, that monthly… time window, I mean, and that's maybe where that delay thing additionally.
**Jack Berg** 43:07 Yeah, so, monthly, GitHub… Actions, updates, but, Early update if there's a CVE.
**Trask** 43:20 Yeah.
So I did check, and Renovate's supposed to break through, like, the… Schedule isn't supposed to apply to things that are actually security Advisories.
**Jason Plumb** 43:38 So I can tell that, that's cool.
**Trask** 43:41 Yeah, it uses… I mean, it just uses the GitHub security… database.
**Jason Plumb** 43:48 Yeah.
**Trask** 43:49 Now, One issue I ran into, though, with, Renovate is that that security The security breakthrough for Renovate only works on direct dependencies.
Not transitive dependence, so if there's a… CDE in a transitive dependency, Renovate won't pick that up.
But Dependabot will, so I actually, on the latest repo I set up, I, turned off security updates for… renovate and opted into those via Dependabot.
It's all.
It's a big, confusing… Ball.
**Jack Berg** 44:32 Full circle, we're back to Dependent Bot.
**Trask** 44:35 Heh, yeah, yeah.
**Jack Berg** 44:46 Alright, well, any other comments?
**Gregor Zeitlinger** 44:49 Is there some kind of, security registry that, like.
Checks all dependencies anywhere, and if it is scanned, then it is good to go, or is that too… Too naive.
**Jack Berg** 45:13 You mean, like, all dependencies transitive and direct?
**Gregor Zeitlinger** 45:17 Exactly, well… yeah, basically all dependencies, let's say, for Java, and then you just go to this, Registry, and check if this dependency has been scanned and is good, and then you can install it.
I don't know of any.
**Trask** 45:34 So there's different tools, yeah. For Java specifically, we're running that Sonotype. It used to be called OSS Index, I forgot, they just renamed it. I don't remember what they called it now.
And that… that does exactly that, what you're describing, Gregor.
**Jack Berg** 45:59 I just saw this the other day, actually, so check this out. So, like, for any… Specific version of any artifact, it gives, like, this trust score.
And, like, after we published a CVE recently for this older version, and it got patched in this latest, you know, presumably the trust scores of all those older versions now is lower than the latest. The latest is 87.
**Jason Plumb** 46:27 Record high.
**Jack Berg** 46:29 Yeah. Well, maybe the other ones were 87 previously, and, you know, they got adjusted, retroactive… retroactively.
So I think this is probably… what's included in this trust score is probably something like what you're talking about, Gregor, like some composite of, like, known CVEs about this specific artifact and all of its transitive dependencies.
**Gregor Zeitlinger** 46:55 And this only exist for Java, or is it… Do other ecosystems have similar things?
**Jason Plumb** 47:04 I think this one's only Java.
**Trask** 47:10 Yeah, so, Gregor, I think what you're asking about is really, I mean, Dependabot and GitHub have features to do that. One of the… I do remember, though, with Java… I don't think they look at transitive dependencies for Java.
The repo I was setting up recently was Python, and they did for Python, but for Java, when I tried that out.
A while back.
I had to opt in and do this thing where, during the build, we… publish, basically, the full transitive dependency, tree back to GitHub, so that then they can use that to scan You know, to cross-reference Dependabot against.
**Gregor Zeitlinger** 47:59 Hmm, okay.
**Trask** 48:00 So, I would start, if you're gonna investigate that, start with Dependabot and check out the features there.
Because it's, you know, GitHub ecosystem.
they have all the CVEs, and I think they have… where they don't support transitive dependencies, they have a ways… GitHub Actions that you can use during your build to publish your transitive dependencies.
**Gregor Zeitlinger** 48:30 Okay, thanks.
**Jason Plumb** 48:31 It's interesting that we're talking about this. I was looking at Android, where we use Fossa.
And I just looked at the output of one of those, and… It's completely failing. Like, the job is succeeding, but the scan is just falling over. That's awesome.
**Trask** 48:49 Yeah, that was a half-shaped rollout.
fossa.
**Jason Plumb** 48:54 So, should we leave it in there?
**Trask** 48:58 You can take it out, okay.
**Jason Plumb** 49:05 And so, is there guidance about what to replace it with?
**Trask** 49:10 Well, we never rolled it out fully, which was the problem. No, I don't think there's anything else. I think that is the right thing for license checking.
**Jason Plumb** 49:20 Yeah.
**Trask** 49:21 It just… Yuck.
**Jason Plumb** 49:25 Yeah, okay.
**Jack Berg** 49:33 What's failing about it?
**Jason Plumb** 49:36 Just click on one of the jobs and you can see.
**Jack Berg** 49:39 So it's, like, it's, like, silently failing?
**Jason Plumb** 49:42 Yeah, the third nuts.
The one above that one.
Yeah, Frank… Whoops.
**Jack Berg** 49:54 False positive.
**Jason Plumb** 49:59 Well, I will rip it out, is what it sounds like.
**Jack Berg** 50:03 I mean, if you can… If you can… Diagnosed this quickly, that seems like a good thing.
**Jason Plumb** 50:11 Yeah, if it was just for licenses, I mean, there's benefit in that, but we're not using it for security.
**Jack Berg** 50:16 Oh, okay, I missed that, sorry.
**Trask** 50:18 Oh, yeah, FOSTA's not about security, it's just about licensing.
license scanning.
**Jason Plumb** 50:26 Different form of security, but yes.
**Jack Berg** 50:30 Legal security.
**Jason Plumb** 50:32 Yeah.
**Jack Berg** 50:34 more important.
**Trask** 50:39 I thought David brought up, SNCC.
**Jason Plumb** 50:42 technique. Yeah.
**Trask** 50:44 do have access to that through the CNCF?
my experience was not great using it. It was very, like.
we were getting massive number, at least in a Go ecosystem, massive number of Things that it was flagging.
Probably just knowledge gap on… our side of… Digging in, again, to the tooling and figuring out how to set it up and use it.
Have you, sounds like you've used that, and… Have been successful.
**Jason Plumb** 51:31 David's often a lurker. He's more of a typer than a talker.
I can share my experience. We use Sneak on some things internally here, and we used it pretty extensively at New Relic, and I had good experience with it.
**Trask** 51:47 Nice.
**Jack Berg** 51:51 I think they're all about the same to me. Renovate, Dependabot, Sneak, none of them are perfect. They all do, you know, similar things.
Renovate, I've found the configuration to be the most expressive so far.
**Trask** 52:05 The thing that's attractive about something like Snyk is that it's just focused on security.
Like, it's not a dependency management… thing.
Renovate feels a little weak to me on the security Peace.
Of, like, scanning… and whatnot.
But I don't know. It all takes a long… a lot of… as you said, the SIG security is just… I mean, we really need… more. Gregor, maybe that's… maybe that's, if you've got time to burn, get involved in SIG security, reach out to Riley.
**Gregor Zeitlinger** 52:55 Yeah, I'm trying not to make it a long-term commitment.
**Trask** 53:01 Yeah.
**Jack Berg** 53:08 Alright, well, conversation's slowing down, I think we call it.
**Trask** 53:14 Yeah.
**Jack Berg** 53:15 Take care, everyone. Feel better, trust.
**Trask** 53:18 Thanks.
Bye off.
**Jay DeLuca** 53:20 Bill.
**Jason Plumb** 53:20 Alright, take care.
