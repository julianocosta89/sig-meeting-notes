SIG: Security Governance SIG
Date: 2026-02-02
Duration: 38 minutes
============================================================

## Zoom Recording Transcript

**Reiley** 00:21 Hey, Jeremy.
Funny.
**Jeremy Corley (Microsoft)** 00:24 Hey, Brandy! Hello!
**Reiley** 00:56 Tuber.
Two minutes for Trust and others.
**Trask Stalnaker** 01:51 Can you hear me now?
**Reiley** 01:53 Yeah, I can. Hey, pause.
**Trask Stalnaker** 01:56 Ayy.
**Reiley** 02:28 Okay, I'm just checking the agenda. Seems like I have a small topic, then that's all.
Okay, so let me talk through, and I won't share my screen, because it's just one simple topic.
So, in the Open Telemetry Technical Committee, we have a weekly rotation.
the people take care of the security advisories. So, I'll just give you a brief, summary of the current process. So, the TC member, when they're the, on call for the week, and starting from Monday.
the previous, on-call will make them the OpenTelemetry org-level admin, so they can see all the security advisories. And then, they have, access to two things. One is they have a org-level security advisory audit log, so they can see all the Chronicle Alder, based, security advisory when people create that.
And every day, there's a reminder on the Slack, so they can, like, follow the link and check what's new. And also, they have access to a dashboard where they can see the summary of the status. So, for example, if an advisory was open, like, 2 weeks ago, but it got stuck, then they can see, like.
What's the progress?
And currently, the TC memory is, like, typically, like, kind of goes through the advisory and see if that makes sense or not. If it doesn't make sense, then we'll just, like, work with the maintainers. Normally, we can just go ahead and close them. Or if there's a maze wrote, like, it's sent to a wrong repository, then we can help to, close that and ask the… the folks who open that advisory to move to a different Drupal, but normally, like, once that's done, like, in the right place, then the TC is basically pinging the maintainers and letting the maintainers do their job.
And maintainers, I think there are two problems. Either the maintainers will take, like, some time to get back, so you have to ping them, and there's no… contract. The second one is even the maintainers, like, they took action.
sometimes there's a lack of, like, accountability or guidance. For example, they will say, like, this already fixed in my code, but then the question is, when are you going to release? You know, oh, we're waiting for the release, it'll happen, like, next month. But it is a, like, very important one.
Severity level is high, maybe we should do the release faster.
So this is why last year I created a PR, and I feel a little bit stuck, because there are people coming and saying, hey, let's just put one week.
The maintainers are saying, not possible because we have the, like, upstream dependency.
And some folks will say, like, no, like, if you look at some of the industry guidance or the standard, it seems like one month is a reasonable thing.
And then… We have feedback from others saying, one month is not enough, because OpenTelemetry is a fundamental component. We depend on OpenTelemetry indirectly. If OpenTelemetry fixed all the things on one month, then we wouldn't have any time. Like, we probably would fix our issue in two months, and that's far away from the expectation.
So, I recently got some connection, through Microsoft, internal, like, legal team, so I reached out to the NIST folks, I shared the… the concern with them, because they're the one who define some… like, they… they own the… the CVE, database. They're, like, there are probably, like, 3 owners, like, independently, they have CVE database, but this one is one of the widely used, and, like, open time should use that a lot.
And also, they defined some standard about, like, when… when are you expected to fix a security vulnerability? What's the CVS score and severity level? So I told them, hey, that doesn't seem to be… a rule, like, you have an expectation that things should be fixed in a month, but when we have a dependency chain, how to break that up, I… I recently worked with a couple folks in Microsoft, and… And we do have some proposal how to solve this problem, so the idea, I hope, is we will… we'll have some technical proposal, we'll work with NIST and see if there's anything, like, of course, we need to do the work. They're not the one who implement the system, but they can… they can take this into the consideration for the next version of the standard.
To give people the right guidance, so that's what we hope.
And also, I can imagine there might be a tracking system to evaluate whether a software component provider, whether it's open source or, like, enterprise provider, what's their history, like, the track record of them, like, meeting those standards. So just try to… like, make progress there before I come back, because I feel like, currently, I don't know how we can solve this problem. And… One thing I noticed is, for… binary-level dependency. Like, if you have a library, or you have an executable that depends on a chain of other libraries, that's one… situation. Another situation which is totally different is the container scenario, because for the binary dependency, you can imagine, normally the libraries won't have static link. Like, they will declare a dependency of the underlying libraries. The only one who might have static link is the final owner of the application, the executable. Like, if you own an executable, you depend on OpenTelemetry library. OpenTelemetry library depends on XYZ library. Then, normally, you have the freedom to bump the version of XYZ library, as long as it is within a major version. Like, you can see, now I want to bump the JSON series from 1.01 to 1.02. Normally, the library wouldn't say no to you, because they follow the semantic version.
The only, the only exception, I, I think, is, in some, like, C++, sorry, people might static link, so you might.
like, take dependency on a library from OpenTelemetry, and you realize, oh, they static link to another library, so in order for me to update that, I have to ping the OpenTelemetry maintainers, or if they don't respond, then the only choice I have is either don't use OpenTelemetry, or I fork my own OpenTelemetry.
So, that thing is very rare, based on my discussion with the C++ folks in OpenTelemetry.
The… but container is totally different, because, like, in OpenTelemetry, we also ship containers for the collector and the operator, and they have a base image, and they might have additional layers that are taking dependency on other images. And container, by design, is self-contained, so everything is included. It's essentially a reinvention of static link for goodness.
And then the problem is you won't be able to patch the container unless you Press the upstream.
So either you fork or you wait.
So that's a summary of my current understanding and the challenges I'm facing.
So I plan to, try some of the ideas, and then follow up with NIST, and once I know a practical guidance, because currently I feel, no matter what we put, we can put, like, one month, two weeks, or whatever, still, it wouldn't work.
It would work for someone.
And the problem for OpenTelemetry is if we don't put a timeline or expectation there, then the maintainers would normally assume They can do whatever they want.
And I feel like we're in a hard situation. Whatever guidance we put, we're essentially putting an arbitrary date.
And what have our reports will be wrong.
So, that comes to my last question. So, for the PR that I've been opening for almost, like, half a year.
should I abandon the PR for now, and put some context there? I can put a summary, and then come back.
Or… do you think we should just put something, like 2 weeks, just to maintain a balance and set us up? I mean, if we put 2 weeks, if maintainers come back and challenge us, I don't know how do I defend.
Like, if they come and see, like, why not 3 weeks?
I don't know. Or if customers come and say, 2 weeks won't work for us, we need 1 week.
Then it seems like an arbitrary thing we're trying to push.
Okay, so that finished my topic.
There's a question open for both of you, if you have any thoughts or feedback.
**Trask Stalnaker** 11:32 Yeah, I like the… I mean, I'm fine if we want to do something in the interim, but I like… Where you're going with trying to… lean on… a higher authority.
To produce recommendations.
I… I'm actually doing the exact same thing right now with, the CNCF security tag, started two weeks ago, a supply chain security, technical community group.
Which came out of, KubeCon discussions that I had with folks, last November.
And… My goal there is, to… have CNCF, official CNCF recommendations around a bunch of this stuff related to supply chain security and updating dependencies and all of that, along with, like, kind of little, like, recipes for concrete things that maintainers can follow.
We have… kinda scoped out, the whole CVE.
aspect, so I think that's… great for your focus, like, I don't think it overlaps with what you're doing.
I… that… could be something that we could try to drive at the CNCF… the broader CNCF security tag.
If you're… We might be able to… I don't know the process with working with NIST and trying to get recommendations there.
But we might be able to make some… that's another option, is the CNCF security tag.
just… but I like the idea of… yeah, because I'm… kind of hit a similar wall, where it's like, okay, I… I'm not really a security authority, I don't really, like, but we… I want to lean on… Like, we shouldn't be making this stuff up. There should be something broader that we can point to.
**Jeremy Corley (Microsoft)** 13:59 Yeah, 100% agree. Yeah, I feel like if we can… do it at a level above OpenTelemetry somehow, it would have both a lot more impact and have more leverage to it in a lot of ways.
Yeah, that's great.
**Trask Stalnaker** 14:18 takes us out of being… pointing fingers at us. It's like, oh, no! Came from higher authority. Go… go bother them, even if we're involved.
Up there, too.
**Jeremy Corley (Microsoft)** 14:31 Right.
**Reiley** 14:34 So, so trust for that PR that has been there for several months, I mean… do you… do you feel? Like, I… I can't imagine, like, two… options. The first one is to, just abandon it for now. I'll put some contacts there, and if people are interested, they can… they can see the history and can reach out.
The second option would be, we push something for, like, a very soft guidance, something like we generally expect this thing to be fixed in two weeks, as we're still figuring out what's the recommendation from a higher level authority. And then.
We, like, we… Also, provide some reporting.
tools, like a dashboard or something, just to show the maintainers where they are, because still, like, every week when I look at the overall number of supply chain security, like CVEs, advisories in the open telemetry organization, I see the number keep increasing.
And I feel there's something maybe we can do to at least change the trajectory.
So, Amazon is either option.
**Trask Stalnaker** 15:47 Even…
**Reiley** 15:48 I don't have a strong, like, preference, just want to know what… what… What 12 of you would think?
**Trask Stalnaker** 15:55 I mean, even putting something, you know, like, longer period of time, like, at least gives, then, some… Thing that we can start… a bar that we can start measuring ourselves against, and like you said, like, have a report that, calls out repos for being out of compliance with them.
**Reiley** 16:19 Like, I don't…
**Trask Stalnaker** 16:20 I… I don't… I like the idea of a report that just… Shows out of compliance for, repos.
Because then… It's… not really this group or the TC's, like, responsibility for bugging people. I mean, we can put that on the governance committee, we can, you know, just… or… Have notifications go out, something, but, like, it's sort of a… Could be a driving force to make people at least publicly accountable.
**Jeremy Corley (Microsoft)** 17:01 Are most of the, the repos, or at least the active ones, are they shipping monthly in general?
Is there generally a monthly cadence?
**Trask Stalnaker** 17:15 I'd say that's the most common, but there's a wide variety.
**Jeremy Corley (Microsoft)** 17:20 Okay, well, I think…
**Reiley** 17:22 Ask that, like, for repositories that have been… in OpenTelemetry for a long time, and it got a lot of attention, like, the collector, Java, and, like.NET.
JavaScript, they have a more predictable release schedule, but there are also projects that just started, or they… they suffer from lack of maintainers. Like, profiling. Profiling maintainers might think, we just started, we're not ready to release any… anything that people would use in production, but as long as you start to check in code, even if it's, like, a simple, like, Python script that you don't plan to ship, it's just part of a maintenance job, if your Python script has a security vulnerability, then It is a security vulnerability, so what do folks do? I think there's a vagal room. If you reach out to the maintainers, the maintainers say, we just started, I don't care, this thing, like, shouldn't affect anyone.
And… And then it's very hard for you to define a bar.
**Jeremy Corley (Microsoft)** 18:22 Right. I mean, I guess, you know, my thought is, is that if you put a bar of one month, even if that's kind of long, as far as, like, you know.
what we would eventually want to get to. You know, the problem of the, you know, the list being ever-growing, at least you could go to the… To the repos that are actually shipping every month, and you can say, look.
You know, we're not asking you to do, you know, releases out of band, you know, it's just part of your monthly ship cycle, but you should not be carrying CVEs from one release to the next release, to the next release to the next release, you know, and we're giving you… you know, guidance that says, hey, at least, you know, whatever was in your previous release, in the next one, at least clean up those before, you know, your next follow-on release. You know, at least get into that cycle. And I think that's not too tall of an ask.
you know, for most teams. Now, yeah, if there's teams that are like, oh yeah, we're barely going together, and we've shipped once 8 months ago, and we're, you know, we might ship again in another 6 months, you know, they might argue a little bit about it, but it's… but you can say, you know, again, it's like, okay, we're not… hopefully asking for too much, and, you know, if there's stragglers because of that, then, you know, that can be, you know, a one-off discussion, but… but I… You know, at least getting the main, you know.
You know, paths going on, and getting them to think, like, yeah, you just don't get to carry them you know, there should be quote-unquote, no excuse to carry them from release to release to release of leaving the CVEs in there.
In my opinion.
**Reiley** 20:10 Yeah.
Thank you. I'll put that in your meeting notes.
**Trask Stalnaker** 20:17 And, Riley, are you talking specifically about security advisories, reported against repos, or are you including also, like, the code scanning, Stuff that has been detected.
**Reiley** 20:35 Okay, so, so there are two things, but my main focus would be, if you have a dependency on something.
And the… The fix is as simple as you just bunk the version of the underlying dependency.
Then, this should be… Patched as soon as possible, instead of having the user waiting for months, and they complain.
And… And the next one is, if people risk any security concern, and you already have a fix in the code, and you admit that it is a CVE, so you have a… you have a CVE that you plan to publish, but you haven't released the change yet, then based on the severity.
The security sake should give some clear expectation, instead of people waiting and the user who reported the issue complaining about, hey.
I reported this, like, 3 months ago, and you already have a fix in the code, and everyone, like, if they're smart enough, they can actually look at the code and see what you're fixing, but why didn't you just go and release a new version? Then people are saying, but we're waiting for another major release, let's just give another week or two.
**Trask Stalnaker** 21:46 Okay, so you're specifically talking about security advisories reported by users…
**Reiley** 21:54 That's the second part, like, let me put that in the meeting notes. So, the…
**Trask Stalnaker** 21:59 Because where… what I'm getting at… what I'm trying to get at is, when we build this report, what's… what's… what data are we sourcing?
**Reiley** 22:10 Yeah, so there are two. One is you have a dependency on other components that are not owned by you, and they have known published CVEs, so you should just find the most and do the right.
**Trask Stalnaker** 22:20 Yeah, how do you… how do we query for that data?
How do we know…
**Reiley** 22:28 Yeah, so either… either it can be a… a dependent bot, enabled, or it can be a third-party like, scanner enabled. But the goal is, if you have a repository and you're the maintainer, you should enable some scanners that can detect your supply chain security.
and can notify you on the version change, like, any version you should bump, and we encourage you to use, like, RenovateBot or something else to automatically update that, but that's not done. You should also take care of the release.
If it's a critical one, you shouldn't just wait for a couple months until users come and complain, so…
**Trask Stalnaker** 23:06 Yeah, I feel like that's where, some more… Specifics for maintainers would be helpful.
Because, for example, I've… I tried doing this in Java.
Repos, and it's actually not… it's actually non-trivial to… Find out about, like… so… Dependabot Renovate.
Great with direct dependencies.
But transitive dependencies… not great.
and so, like, there's some other things that you have to set up in order to report all your transitive dependencies to Dependabot, and then you have to, like.
Filter out test dependency, like, this… It's not trivial.
I wish it was simpler, and maybe there's some tools… that… We could use, maybe that would help make that simpler.
Also, then, how do we report? You know, how do we… Report against… like, we want a dashboard that tells us if Our repos in compliance, and if we don't have a standard way To detect that, then we can't Really run… we don't… we can't generate that report.
**Reiley** 24:38 I see, so… so my thinking is the… the… The report will be… focusing on advisories and have a link to each, like, the repository based on the maintainer's specified place. Like, essentially, we'll ask the maintainers Do you have a way to detect the supply chain security issue? If not, then that report will show red for your repository. If you have one…
**Trask Stalnaker** 25:05 It's an app, at… attestation.
Like, basically, manual attestation that…
**Reiley** 25:12 Yeah, but if you have it, then you have to provide a way for us to collect the number of dependency issues you have. And if you don't have any of this, we'll try to do a catch-all.
situation, like, because on… on GitHub, you can already see the supply chain security for, like, for Python, they're… they're loud, and it's still climbing up. So we can… we can do a default thing, but we should call that the default option is not… the past.
**Trask Stalnaker** 25:52 Oh, yeah.
**Reiley** 25:54 Like, if you just go to OpenTelemetry org level, and you see the security…
**Trask Stalnaker** 25:58 I see the Dependabot alerts. Okay. Yeah, yeah.
I mean, that's at least… I like the Dependabot alerts as, even if it doesn't… Deal with transitives for some languages.
It's at least someplace to start.
**Jeremy Corley (Microsoft)** 26:21 It's a good first bite, yeah.
**Trask Stalnaker** 26:23 Yeah.
Because presumably those things would then bubble up to… To the dependencies until they hit your direct dependencies.
**Jeremy Corley (Microsoft)** 26:35 Cute.
**Trask Stalnaker** 26:40 Okay, I… I like that. I mean, I'm supportive of… you know, putting whichever approach you want, Riley. But yeah, like, if we want to move forward with it, I think… the PR… Just kind of softening the language… The requirement.
will… Make people… will help us to get it past community and start, then, iterating.
**Jeremy Corley (Microsoft)** 27:20 Are there… are there any, as far as when releases are made, are there common, like, OpenTelemetry-wide processes that are part of those releases, or is each repo kind of doing their own thing as far as How they, sort of do that release and generate that code. And where I'm going with that is, like, is there an opportunity for us to say.
if you are going to make a release, and you have a bunch of known CVEs that are, you know, publicly known CVEs already, like, you know, if we add some friction in, would it be easier for me to upgrade versus do I have to, like, write a report that says, okay, here's the… 27 CVEs that I've decided to let through on this release, and I need to describe, you know.
why, you know, if I have to go, oh, you know, I, you know, we haven't been able to get to this one yet, or this one requires a bug fix, and da-da-da-da, and go through on, you know, or this one hasn't been investigated kind of thing, and if there's a, you know, please list all the CVEs and the reason why they're, you know, they're being passed through kind of thing.
you know, do you add some friction and make it easier for them to just fix them before they make the release or not? You know, kind of thing. I don't know.
And that's probably… Me thinking with corporate brain on rather than open source brain on, but.
**Trask Stalnaker** 28:48 I think that aligns with, there's kind of a proposal to do, kind of train releases, release trains, which would be, like, I don't know, every… Quarter, every 6 months, something like that, where there would be an aligned… OpenTelemetry release across, you know.
Core set of repos.
And that that would be a good opportunity, I think, to… And kind of the purpose of that is to… create friction. Specifically, the discussion has been around stability.
And ensuring that things are stable by default, and, like, you opt in to this release train, you have to do a little extra work.
I dropped in chat a link to… This had come out of discussion with the CNCF, as part of the graduation discussions.
Because… they… the CNCF is a little more used to, like.
project-wide releases, like a Kubernetes style, and OpenTelemetry is… very decentralized, and so I think we, you know, we got the message, sort of, from the CNCF that While it's not a hard requirement, it is desirable to have more cohesive, releases, project releases.
**Reiley** 30:42 Yeah, just took a quick glance, seems really good.
And I assume the intention is to align the big release and still allow each repository to do their security hotfix, right?
**Trask Stalnaker** 30:59 Yeah, and even to allow individual repos to make, like, monthly minor releases if they want.
But then there would be a… train…
**Reiley** 31:11 release…
**Trask Stalnaker** 31:15 coordinated.
Cool.
**Reiley** 31:48 Should we call it?
**Trask Stalnaker** 31:49 Yeah.
**Reiley** 31:51 You have a topic, and it seems like you already covered that.
**Trask Stalnaker** 31:54 Oh, yeah. Yeah, yeah, yeah.
**Reiley** 31:58 Okay, then… That's important. Yeah.
**Trask Stalnaker** 32:01 I'll keep you all posted as we, But last week we picked… So I had brought, kind of, a bunch of examples from OpenTelemetry, and in last week, we picked, sort of, a first topic.
Which is, pendency update.
Which is… yeah. Anyway, a lot of… I'll keep… This group posted, as we have something To review, but still pretty early in that process.
We do meet, we're meeting weekly.
After this meeting, actually, on Mondays.
If there's ever a good topic or something, I'll… Send y'all, I'm sure the last thing you all want is another meeting, though.
**Reiley** 33:09 Yeah, so… Jeremy, you decide if you have, like, some bandwidth, maybe, like, starting from April, and see if there's something you can help.
I know I'm… for now, so I'll let you know if I have bandwidth, but for now, you should assume.
I won't.
**Jeremy Corley (Microsoft)** 33:29 Yep.
Yeah, I probably will, so yeah, that'd be great.
**Reiley** 33:35 Okay. Cool.
**Trask Stalnaker** 33:37 Send you more info. Alright.
**Jeremy Corley (Microsoft)** 33:39 See ya. Thanks, guys. Bye-bye.
