SIG: PHP SIG
Date: 2026-06-24
Duration: 40 minutes
============================================================

## Zoom Recording Transcript

**Sergey Kleyman** 00:36 Alright.
**Pawel Filipczak** 00:37 Hey, boss. Hey, Sergei.
**Bob Strecansky** 00:39 Gentlemen, how are we?
**Pawel Filipczak** 00:42 Mute?
**Sergey Kleyman** 00:43 Good, good. How are you?
**Bob Strecansky** 00:46 to play?
**Sergey Kleyman** 00:51 How's the bedroom?
**Bob Strecansky** 00:54 It's… today it's kind of… today it's kind of alright, but it's been anywhere between, like, 22 and 38 over the last couple weeks.
**Pawel Filipczak** 01:03 Whoa.
**Bob Strecansky** 01:05 Big Delta.
**Chris Lightfoot-Wild** 01:06 Hello. And it's…
**Bob Strecansky** 01:07 It's, like, unbelievably humid here too often, so… that's another thing.
**Pawel Filipczak** 01:16 Same here.
Now it's 20, so it's… it's… it's nice, so it's… it's… actually, it's a huge difference if it's 20, but… Previously, it was winter, so it's still cold, so I cannot go outside in t-shirt, but now it's hot. It was hot. 35, 38.
And now it's 20, so it's still hot, but it's 20s. It's… it's comfortable.
**Bob Strecansky** 01:42 Alright.
**Pawel Filipczak** 01:43 It's killing me. Here, it's crazy.
**Bob Strecansky** 01:46 It has been fascinating to watch a lot of international people in Atlanta with the World Cup here.
**Sergey Kleyman** 01:55 You're one of the cities that, hosts, World Cup? Oh, okay.
**Bob Strecansky** 01:59 Yep, there's a game in it, but they end up, like, I don't know, a couple miles from my office today, so… I will not be going, because I would have to take out a small mortgage to pay for one of the tickets, but…
**Sergey Kleyman** 02:12 But do Americans interested? Like, does it affect traffic, seriously? Like, other than local… you probably… I mean, I find it… find it hard to believe that Americans are that interested in soccer.
**Bob Strecansky** 02:23 Are they? Well, there's a couple things. One, traffic in Atlanta is always bad, so… but, you know, I'm interested to see how it affects traffic. This is the first day I'm intentionally coming to my office with traff… on a match day.
No, American… I mean, soccer is definitely picking up popularity in America, but I think we definitely have a lot of international visitors in Atlanta for this month to see World Cup games.
So… Yeah, overall, pretty good.
Alright, cool. Chris, looks like you put some stuff on the agenda. Let's… let's rip.
**Chris Lightfoot-Wild** 03:03 Yeah.
The… just fill out the attendees, or is that not really.
**Bob Strecansky** 03:09 Oh, yeah.
**Chris Lightfoot-Wild** 03:10 Oop.
Well, how to?
**Bob Strecansky** 03:15 I'd like to find one that has all of us.
There we go.
Alright, proposals to split CI and Contrib.
**Chris Lightfoot-Wild** 03:36 Yeah.
I guess this was following on from some of the conversation about fan stuff last week, and I started just looking at like, the workflow, and then, I guess, went off slightly off-piece, deciding that, oh, maybe we could just split the workflows.
So, each component can have, like, its own separate build matrix, Yeah, so… and then I've made, utilized the reusable workflows so that… When we do a subtree split, it will remotely be able to be triggered from That individual, split repo.
So then we could, down the line, obviously, if we wanted to schedule that as, like, a weekly… ruin or something, we could do that.
So, yeah, it felt quite a bit more flexible, but… Yeah, I just… I'd picked out 3 examples to do.
Which were, Laravel, MySQL, and Kafka.
So, I've linked to the workflows as well, if you want to, ping back over to the…
**Bob Strecansky** 04:44 Oh, yeah.
**Chris Lightfoot-Wild** 04:45 the meeting notes, and then look at the MySQL split as an example one.
**Bob Strecansky** 04:50 bet.
**Chris Lightfoot-Wild** 04:51 So there's one that's just in Contrib, where it matches on… the workflow runs on that MySQL.
They're within the same repo.
**Bob Strecansky** 05:01 Oh, nope.
**Chris Lightfoot-Wild** 05:03 So it's got, like, the 8.2, 3, and 4 builds.
And then if you look at the subtree split.
Although, it's an artificial one, I just pushed up to my own repo, my own fork, sorry.
**Bob Strecansky** 05:16 Which one.
**Chris Lightfoot-Wild** 05:18 That's it, yeah.
**Bob Strecansky** 05:23 Does the same thing.
**Chris Lightfoot-Wild** 05:25 Yeah, so that shows it, obviously, brilliant.
Running there as a remote workflow.
**Bob Strecansky** 05:32 That's cool, that's cool.
**Chris Lightfoot-Wild** 05:35 So I don't know if… I guess what the initial thoughts were on it, and then if maybe we could… If we're accepting of it, just try it out with those maybe three, and see, you know, what that looks like, but… Happy to take feedback on this approach.
**Sergey Kleyman** 05:52 If you duplicate, so how much duplication, will there be? Like, for example, if you're adding 8.5… How many files you will have to update with that?
**Chris Lightfoot-Wild** 06:01 At fair point, every instrumentation one, that's its own split.
which, yeah, is, I guess, more worth…
**Sergey Kleyman** 06:08 Something that will be purely automatic, like mechanical, just adding a 5, or… Even if there are many files, the question is, is it something that can be easily done? Like, obviously, duplication has these two sides, right?
**Chris Lightfoot-Wild** 06:21 You have nothing.
**Sergey Kleyman** 06:21 versus not to forget to do all this stuff. Like, if it can be done just mechanically over all the files, maybe it's okay.
**Pawel Filipczak** 06:30 So in this row, we introduced the properties file, and we have the supported PHP versions in the property file, so then it's easier just to add the additional version to the matrix, so then it's been loaded into the matrix.
**Sergey Kleyman** 06:43 It sounds to me that this cantripCI is kind of, like, serves this purpose of our property file, right? It's some kind of customization per project, right? Per component.
**Chris Lightfoot-Wild** 06:52 Yeah, but if you've got a better way, then, by all means, I guess if we could… kind of, mangle the two together, if you've… if you've got a thought on it, Paul.
**Sergey Kleyman** 07:03 You're taking the opposite approach, you kind of, like, have basic blocks in the shared, and then this contribute CI YAML kind of, like, picks them up and builds a flow that you want out of them?
**Chris Lightfoot-Wild** 07:14 Yeah, so each component would have its own workflow file, so that it can match on the path that it should run against.
So obviously now, when you open the PR, it will run all of the components?
Whereas, obviously, I think this would allow us to, you know, if I made a change to Laravel, only the Laravel workflows would run.
So… you know, I thought that was…
**Sergey Kleyman** 07:38 You want to see if PR only touches one component, and only workflow for that component will run? Is that the purpose?
**Chris Lightfoot-Wild** 07:47 Yeah, that was what I was proposing.
And I think that's why maybe in the subtree split ones, we could have, it run there on a schedule to say it's gonna pick up things that, you know, on a weekly cadence or whatever, but…
**Sergey Kleyman** 08:04 So the purpose, like, the motivating goal here is to essentially minimize the amount of stuff that runs in HPR, or to have flexibility for each component, or both.
**Pawel Filipczak** 08:16 I think…
**Chris Lightfoot-Wild** 08:16 Kind of both, because…
**Pawel Filipczak** 08:18 Sorry, go on.
**Chris Lightfoot-Wild** 08:19 Cool.
**Pawel Filipczak** 08:19 I think that, from my point of view, the biggest problem is that other… other components are failing, and they're affecting the build, right? So you don't… you can't be sure that the process because other instrumentation is failing. So, yeah, it shows the… the green light, right? To match it.
**Chris Lightfoot-Wild** 08:37 Yeah, like, on the back of this PR, I can see that the MySQL stuff all is green, so that one's good. And then the next PR that goes in, you can tackle one more and, you know, get them green over time.
**Bob Strecansky** 08:50 I was gonna say, you've probably addressed my two biggest concerns. One is upgradeability, like Sergey said, adding a new version or changing all of these is… It's annoying, but not annoying enough to where we shouldn't do it. It's just something we have to be conscientious of. And the other one is, what happens if you have a change that is cross-cutting against multiple dependencies, but it seems like those will run those specific CI checks individually, right? Like, if I change something that changes both Laravel and MySQLI, then it will… the… both CIs will run.
And I don't know how… I don't know if we have any places where you have interoperability like that. Like, if I'm making an update to the MySQL package, what sort of transitive dependency do we have on another package in the repo? But I don't… I don't… I'm not smart enough to know, like, how much interdependency these contribib packages have on one another. I don't think a lot, but it's just something to consider.
**Chris Lightfoot-Wild** 09:48 I think typically when you do that, you can then reference the same by a local, path as well. So that's probably, like, a bridge that we could still cross, but haven't hit that problem yet.
Okay. The biggest difficulty in this was, well, I was trying to get a shared… Custom action to work across like, from a remote workflow call, but I just… I was hitting a brick wall, so… Yeah, that didn't… I changed course with that. But the services that run, provide, like, a service mapping string, sort of, like, if you look at the example there, Kafka 1, line 36, Triggers only that one service to spin up, so each.
Instrumentation can defy, decide which services But they're all defined just in the PHP contrib, workflow.
**Bob Strecansky** 10:43 Okay.
**Sergey Kleyman** 10:45 What is the purpose of this contribiyaml in each component? Is that what defines?
**Chris Lightfoot-Wild** 10:52 Yeah, so when you do a subtree split, that ends up in the other repo, and then…
**Sergey Kleyman** 10:57 I see.
**Chris Lightfoot-Wild** 10:58 Yeah, so…
**Sergey Kleyman** 10:59 That other repo doesn't run CI, right? That repo is just for the exposition, like.
**Chris Lightfoot-Wild** 11:03 We don't currently run CI, but it's not because it's disabled, it's just because there's no workflows.
So if this… if we add this in.
**Sergey Kleyman** 11:12 Okay, so you do want to, in those read-only repos, you want to run CI there?
**Chris Lightfoot-Wild** 11:19 I mean, personally, I think so. I don't…
**Sergey Kleyman** 11:22 I see.
**Chris Lightfoot-Wild** 11:22 We don't have to, I mean… It's just, if someone discovers that and it's got a green tick on it, it looks better than… I don't know what the hell this is. There's no… there's no tests that I've run.
**Sergey Kleyman** 11:33 Right, right. But that will not happen in a PR, right? So if I, like, let's say I'm creating a PR and only making changes to my SQLI instrumentation, then I will see green mark be… I will still see green market at PR, Because there is a separate repo there, it's gonna kind of, like, split the…
**Chris Lightfoot-Wild** 11:51 No, the split is… Yeah, those ones don't make a difference, those Contrape CI ones.
That would only take effect after we'd done a split, and then it would run in a separate repository as its own thing.
But if you…
**Sergey Kleyman** 12:07 They are, I will steal… Cheers, go ahead.
**Chris Lightfoot-Wild** 12:12 So if you open a PR against Contrib, you'll just get these workflows to run. If you look… if you scroll up a bit, Bob, and go looking at the… the actions that ran against this one. You'll see a list of… I'll just go back to, like, the conversation bit.
Or I guess checks. Czechs equally would, hold it.
If you scroll down in that list.
Yeah, there's all the CI larval ones.
Kafka, and then the MySQL ones.
**Sergey Kleyman** 12:44 So you're saying, technically, I will be able to see that if my intent was only to make changes to Kafka, I will only pay attention to Kafka that I agree, and then I can… I can be, kind of, like, confident in the… okay.
**Chris Lightfoot-Wild** 12:58 Yeah, the other workflows wouldn't run, so the idea, I guess, would be that the existing PHP CI would just start Migrating across to a specific workflow for each component.
And then you get to a point where only that… you know, the Laravel one, it runs its build matrix, and it's got, you know, X number of versions against… Laravel versions against X number of PHP versions, and you get a build matrix of, like, 15 or something.
Versus… 70, or 100, or whatever it is, currently.
**Sergey Kleyman** 13:30 this… this is… when this will happen, with additional changes, or even in despair? So this minimization of only the Iranian… so… this is something that you want to get to, or it's already implemented here that you will only run the Laravel combinations and not run the rest of it?
**Chris Lightfoot-Wild** 13:47 Well, all the rest of them, until they've got, like, targeted instrumentation, they'll just exist in the current workflow.
Like, so that's why I guess I'm proposing doing this, and if we're not against it, then I'd drop it out of the PHP CI for Laravel, MySQL and Kafka.
And then just have those 3 as an example, and then try and port the other ones across as well.
And then they've got… The capability to individually target each instrumentation to fix them.
But…
**Sergey Kleyman** 14:20 You said target doer.
**Chris Lightfoot-Wild** 14:22 So…
**Sergey Kleyman** 14:24 So, when you say target, is that something… when you run the… so when you create a PR, will it automatically detect that it only made changes to Kafka, and it will only run… a workflow related to Kafka?
**Chris Lightfoot-Wild** 14:36 Yeah, if you look back in the files change, Bob, So at the top there, that Kafka example, there's the on push, or on pull request, and then specifying the paths.
So it only runs against those… any files changed within those paths, and that's just a built-in, you know, GitHub action feature, so… It's just that, obviously, on this exist… on this PR, the other workflow still triggers that does everything anyway, so…
**Sergey Kleyman** 15:03 But do you want to take the rest of it, and also convert it to this format, so it will only be triggered by a specific path? And then, after those changes.
**Chris Lightfoot-Wild** 15:10 Yeah, if we're happy with this approach, like, if we're not, then obviously it's just…
**Sergey Kleyman** 15:15 But we don't have any shared code, you're saying we are… should be safe with this approach, because technically we keep them in one repo, but that's only for convenience sake. There is no shared code between them, maybe some testing infrastructure.
But, like, in production code, there is no shared… so we don't need to detect any changes to shared code and trigger all of them, because there is no shared code. Is that correct, my assumption?
**Chris Lightfoot-Wild** 15:37 That's correct.
That's correct, yeah.
**Sergey Kleyman** 15:39 So, keeping them in one repo, we can imagine that those subdirectories are actually separate repos, and there is no actual reason not to treat them as separate repos, and then we're okay with running workflows only when the changes in each subdirectory only run workflow for that subdirectory.
Right? That's essentially how we see that, right?
**Chris Lightfoot-Wild** 15:58 I think so.
**Bob Strecansky** 15:59 And then I'm… and then I'm assuming Chris's intent here is to, lessen the barrier for individual contrib… contributors to get their code to production, right? Like… If we only have to… if we only have to worry about CI for RD Kafka, somebody contributing to RD Kafka, it's like, okay, I don't have to worry about the MySQL, or the Azure, or whatever, other CSS is failing. Like, I understand why we're doing this.
**Chris Lightfoot-Wild** 16:25 Yeah. Yeah, it obviously seems a bit more work in maintaining separate workflows, like, they've got separate build matrices, etc, but you don't have to then expand the… like, if we do, currently, we say we'll add 8.5 or 8.6 in future.
And then if there's a bunch of exclusions to make in that matrix, we've got to go through and check all those anyway.
So, I guess personally, it doesn't seem like it's that much more effort to just go into each file and say, oh, I want to explicitly run this version, and I want to drop 8.1 from this now, and, you know, managing that can be done as part of the… updating of that instrumentation, I think.
**Bob Strecansky** 17:05 Yeah, I wonder if the success criteria for using this, Chris, would be something along the lines of.
if we need to, how can we easily update all of these, and how can we ensure that we don't have, like, gigantic drift between each of them? I don't know what that level of effort for that would be, but it's like, okay, so… you know, the, MySQL people decide they want to test against 8.6, and then… the Azure people haven't made an update in 10 years, and they're testing against 8.1.
And, like, is that okay? Probably not, like, we probably need to keep our P… like, and I'm using PHP version here, it's just, like, off the top of the, you know, off the cuff, like, perhaps we need to ensure that we have some sort of… what's the right word? Baseline configuration for these things, and that all of the… all of the different GitHub workflows.
Adhere to that baseline so that we don't have too much drift.
**Sergey Kleyman** 18:04 I mean…
**Chris Lightfoot-Wild** 18:05 A little bit.
**Sergey Kleyman** 18:05 Again, I don't… yeah, please go ahead, Chris, yeah, please go ahead.
**Chris Lightfoot-Wild** 18:08 Well, so maybe I'm misunderstanding, but, like, the baseline is the PHP contrib workflow, that all of these other ones then have very, you know, the option to configure via.
**Bob Strecansky** 18:20 Right?
**Chris Lightfoot-Wild** 18:21 oats.
**Sergey Kleyman** 18:23 them? Can you say, I'm building on the base, and I now want to add additional dimension of Laravel versions? Can you take the base YAML that only shows you which PHP versions you want to test, and then you can add the second dimension of Laravel versions. Can you do that with this YAML?
**Chris Lightfoot-Wild** 18:39 Yeah, if you… well, that's just by the, build matrix. If you scroll down a bit in that Laravel example, the second file there.
That's got two… .
**Sergey Kleyman** 18:50 Yeah, but you duplicated them. What I think Bob referenced is that, okay, let's have base YAML. Like you said, we'll have some kind of base YAML contrib, right? And we will add 8.5 there, and it will automatically also be used by all the sub-packages.
Instead of going in each one. Now, the question becomes, how do we allow somebody to opt in the additional version, or opt out?
I will just give an example how we did it in distro. We essentially use a script. It's possible to use a script to generate on-the-fly… whatever you want, dimensions of any matrix. So technically, when we invoke that script, we can allow additional parameters that can tell it if you want to exclude certain versions, or if you want to include the additional one that is, not the default, like, base case, right? And then we can just easily search the repo and find how the script is invoked, and if there are invocations with these additional parameters that are changing the default. So this, for example, can be done, but I don't know if that's the simplest approach.
I don't know what, Bob, what you mentioned, I'm not sure what can we do. Like, if we have some Azure, and we don't have anybody that wants to continue supporting it, if they didn't update it since 8.1, That will probably state like that, right? Like, it's not like we… I mean, it sounds to me that finding that this is the case will be the easiest part, right? We can easily run a simple search, even if the rows will be separate YAMLs, that can report and say, okay, these components are not in line with what we define the base case, supporting both versions we declare as being supported by, let's say, SDK.
But the question is what this report can be easily generated, what can be done with it, right?
**Bob Strecansky** 20:44 Yeah, maybe I'm… maybe I'm being too picky here, I'm not certain, but I just wanted to make sure.
**Sergey Kleyman** 20:49 Like I said, there are technical solutions. We can do the script, the same as we did in distro. It's just in distro, we did it because we have About, like, 4 dimensions, so it was just easier to express it in a script.
Because it's not a perfect cube, it's, because we want to minimize, so we don't want complete, kind of, like, combinatorial explosion.
Because there will be too much resources to spend. So, but here, I think, if we think that the, you know, the case that we have here is two dimensions.
version of PHP plus version of technology. I think YAML will work, and we can just easily write some report-generating thing that will just show, okay, these components are not in line with what is declared that SDK supports.
And we can easily see that report, but what I'm saying is that That will be probably 1% of the effort to get in line, right? Generating the report.
**Pawel Filipczak** 21:43 Matrix generator can be implemented in YAML as a workflow and raised through all workflow.
And we can just put some bash scripting inside the work profile, and just put it in line. We don't have to commit any scripts. If it's just two dimensions, then… it, it should be easy, but he… previously, I was using the, the… just… just the workflow to generate metrics, and we are… I guess in distro, too, we are… we have the… We have the metrics generator as a resultable in our workflow.
Then it can be easily included.
**Chris Lightfoot-Wild** 22:21 So, it sounds like, with your experience, then it, what you've… what we've got here looks like it would be possible to adapt in future if we needed to.
**Pawel Filipczak** 22:29 True.
Yeah.
**Chris Lightfoot-Wild** 22:32 I mean, I guess, is there any hesitation against going this route? Like… Could I trial it with these three, or…
**Sergey Kleyman** 22:38 And from what you described, like, if we want to keep those subdirectories completely independent, which probably is, It's quite a good assumption, I think, your approach. I don't see any problems with it.
**Bob Strecansky** 22:48 Yeah, I don't… I have… I have no trepidation here, Chris. Like, we were talking through the potholes because we want to make sure the road is smooth for you, but I think that this will definitely… like, splitting these out will definitely help the contribut repo be a little less… Hectic? Is that the word I'm looking for? Yeah, hectic.
**Sergey Kleyman** 23:07 Yeah, I think that the biggest, what I understand is the biggest might be a threshold that if somebody makes changes and sees tests failing, and it's not a written component that you touched, that's a big, problem, right? So, not having that will be a big achievement, yeah.
**Bob Strecansky** 23:20 not problem as much as frustration, right? Like, damn it, like, why is… why is… why are these Azure people not making their updates?
Okay, cool.
**Chris Lightfoot-Wild** 23:30 So if we're okay with that, then, would I be able to try and sort of clean this up a little bit? Because at the moment, I've got to reference my own fork of these, but if I… So, realign that. Is that something that we could, sort of, trial with these three instrumentations, potentially?
**Bob Strecansky** 23:46 Works for me. We can always revert it if we decide that it doesn't work.
**Chris Lightfoot-Wild** 23:50 Yeah, so for the time being, then I'll just comment out in the existing workflow, those three instrumentations.
And then, once we merged that into master, I can do a separate, like, smaller PR against, like, something in Laravel, and just check what the workflow looks like, you know, what the build matrix spits out.
On that PR.
**Bob Strecansky** 24:12 Works for me.
**Chris Lightfoot-Wild** 24:14 Cool, alright, yeah, thanks very much, and cheers for everyone's, discussion around that. It's interesting.
**Bob Strecansky** 24:22 Oh, new distro release.
**Pawel Filipczak** 24:25 Yes, yes, today we released, yesterday, today we make it two releases. Today contains the fix, or with the new Gaza package, it contains some security issues.
It wasn't used by default, because we are… we have the… native exporter.
in the distro, but yeah, if you have dependencies on Gaza HTTP in your projects, it's worth to update.
So…
**Sergey Kleyman** 24:54 Those are log files that we check them in, because we want to ensure that they are pinned.
**Pawel Filipczak** 24:59 Yeah, yeah.
**Sergey Kleyman** 25:00 So we want to make sure that the build is reproducible.
**Bob Strecansky** 25:04 Is this something we need to do for the…
**Sergey Kleyman** 25:07 For this…
**Bob Strecansky** 25:07 We'll repost you.
**Pawel Filipczak** 25:09 No, no.
**Sergey Kleyman** 25:10 The case kind of, like, serves as a dependency that you take in… like, I assume we won't probably to allow developers to decide. They themselves can check in their log file if they want to, but they have flexibility about it.
We… we cannot… we cannot rely on that here, because we are being distributed as a self-contained package, right? So, we have to pin those dependencies to ensure that it's reproducible.
Right, if we will allow it to run install each time, then it might download different versions.
**Bob Strecansky** 25:43 Right. Okay.
**Pawel Filipczak** 25:45 But if you are some summers didn't have application deployed with the Gazelle HTTP, It's forced to update it.
I mean deployment, you know, companies.
So, yeah.
**Bob Strecansky** 25:59 Good to know.
**Sergey Kleyman** 26:00 For users, it most likely will not be an issue, because if they pick latest, it will just automatically work. So SDK itself.
**Pawel Filipczak** 26:05 Yes, but still.
**Sergey Kleyman** 26:06 Yeah, coffee.
**Pawel Filipczak** 26:08 You have to call… you have to call composerUpdate, right? It will not do that automatically.
**Sergey Kleyman** 26:14 or update to install, like, depends how you build your application, right? Like, if you… if you don't check in log file, then you don't need update, you just need to install, and… yes, I agree with you, you need to repackage your application if you have to install, or update if you… if you check in your log file, then you'll have… yeah, you need to update it and check in.
But, let's say the simplest flow, just install, and, But, yeah, there is this.
**Pawel Filipczak** 26:41 That's it.
**Sergey Kleyman** 26:41 Interestingly, the big sequence of almost all the versions, except for the few latest ones, got, Got marked as having the security issue, so…
**Pawel Filipczak** 26:51 Hmm.
**Bob Strecansky** 26:52 Is there a specific security issue that y'all are looking at? I'm looking at the guzzle releases now.
**Pawel Filipczak** 26:59 I will… I will put it into the… into the… this PR, okay? And I will…
**Sergey Kleyman** 27:04 If you look at the packages on GazelHTTP, you will see that almost all the versions marked as having security vulnerability, except for the few latest ones.
**Bob Strecansky** 27:13 Okay, I will take a look. Oh, yes, I see.
Alright, that's good context, thank you for letting us know.
**Sergey Kleyman** 27:22 Right, but again, it's not a problem for SDK itself, because it doesn't end the version in any way, so… It's up to the end users to decide if they… If they want to pin it in any way.
**Chris Lightfoot-Wild** 27:34 This is just because of your… your distro, where you're doing the shadowing thing, aren't you?
**Sergey Kleyman** 27:39 No, no, that was even before each other, because we pinned the versions.
First of all, even if we didn't pin the versions, like, let's say we already released distro with certain versions, like, two months ago, when the latest was still having this vulnerability, we would still need to rebuild the distro and take the latest one.
And re-release it, right? Just because the… the problem is the distro already contains the Godzilla HTTP inside of it, right? We don't allow users to… decide to install, Gazelle HTTP by themselves. They might have a separate copy. If you refer to the fact that we can allow coexistence of their latest copy of GazelleHTP and ones that we packaged, yes, it now works because we also shadow them, yes. But before we did…
**Chris Lightfoot-Wild** 28:21 Yeah, that's what I meant, sorry, yeah. So, you're controlling that. You've patched it by the lock file, and it's shadowed, but the application…
**Sergey Kleyman** 28:29 Well, yeah, before it was even worse. It's not like the problem was brought by Shadoin. Before Shadowing, we probably would have not allowed even the application to use the latest, right? We would have loaded the bad one with vulnerability first, and then application, even if it comes with the latest one, it would not help it, because it was still the Use the version that we loaded, because we load first.
**Pawel Filipczak** 28:53 minimum.
You can read the details, I provided the link in the description of the issue, so you can read the details.
**Sergey Kleyman** 29:00 Now, yes, you are correct. Because of the shadowing, even with the vulnerability, it will… it would have only affected us, the distro, not the application.
**Chris Lightfoot-Wild** 29:09 Awesome.
Did you get… have you got DependBot, configured against this, or are you using Renovate, or something?
Because it's under the Open Telemetry organization.
**Sergey Kleyman** 29:21 Are you asking?
**Chris Lightfoot-Wild** 29:21 Plug it for you.
**Sergey Kleyman** 29:22 Have we discovered this? Excuse me?
**Chris Lightfoot-Wild** 29:24 Well, did… did anything, like, flag this automatically for you, or did you just…
**Pawel Filipczak** 29:30 sneakers.
**Sergey Kleyman** 29:30 Have a night.
**Pawel Filipczak** 29:31 Nick, we have the stick stand in the Elastic, so if you're building The elastic distribution, then we are scanning the dependencies automatically.
**Sergey Kleyman** 29:40 Yeah, yeah, the regular stuff, like renovate, will not work here, because we don't have this version mentioned in, In, Composer chase.
We bring this… we bring this Gazelle HTTP because of the… because SDK brings it in, it's transitive dependency. But we pin it in a log file, that's the problem.
We brought all the transitory dependencies, like, all the three down from SDK. We pinned it all because we want it to be reproducible next build, right? If we want to rebuild the same thing, we want to have all the same dependencies, and that means that we pinned the version with vulnerability.
So, even though… so the tools like Renovate would… cannot discover this because we have this elaborate workflow with opinion and generating log files.
as a separate step, not something we mentioned explicitly in JSON, in Composer JSON.
**Chris Lightfoot-Wild** 30:33 Okay, so does Snyk runs as part of the workflow as well, does it, when you're building this?
Yes, correctly.
**Sergey Kleyman** 30:39 me if I'm wrong, Pavel, we feed the log files to Snyk, not the composer JSON.
**Pawel Filipczak** 30:43 Yes, locals. We are checking exact packages, not trying to guess during the composer install, so we are just providing versions which are Which are delivered by the package.
**Chris Lightfoot-Wild** 30:58 And this is happening automatically, sorry, is it as part of the workflow, then? You don't…
**Pawel Filipczak** 31:02 Yes.
**Chris Lightfoot-Wild** 31:03 Yeah, nice. Okay, cool, sorry.
Sorry for the questions.
**Sergey Kleyman** 31:08 Well, but it happened because we have EDOT, so you are right about flagging it, right? It doesn't happen, so maybe it will be an action item on us if we can ask Elastic maybe to sponsor running Snyk on Upstream repo on the OpenTelemetry distro.
Because technically, if we didn't have Elastic downstream distro derived from upstream, from OpenTelemetry distro, we would not have discovered, because Snyk only runs on Elastic Distro.
It's only, it's only, it's now a very thin layer around what we contributed upstream.
But still, Snyk only runs there, it doesn't run on upstream, on OpenTees.
So that might be an issue. We need to see what we can do about it, if Elastic have maybe running it also on the open… open to the distro.
Maybe that will be a plus.
**Bob Strecansky** 31:58 I'm wondering if there is, Looks like there might be a snake.
There's a… There is a dedicated CNCF snake tendency.
**Pawel Filipczak** 32:13 Oh, great, so maybe we can just include it into the build?
**Bob Strecansky** 32:17 Yeah.
**Sergey Kleyman** 32:17 Probably a little bit.
**Bob Strecansky** 32:18 I'll follow up in the maintainer's channel to see if there's a pattern for that.
**Sergey Kleyman** 32:23 Because technically, it doesn't even happen at the same time, right? Because we first contribute stuff into upstream, so technically, we can introduce… we can introduce security vulnerability, and until we go and sync EDOT, Elastic Distro with it, with upstream, we will not discover that vulnerability. So running… Directly on upstream is also… will be good for that, so it might be a good idea to do that as well.
**Pawel Filipczak** 32:47 We are trying to validate it just after the distro, I mean, the elastic distribution, but still, it can take.
**Sergey Kleyman** 32:54 Yeah, but sometimes it can take weeks, right? Sometimes we not necessarily do it immediately, so yeah. So it's best to do it upstream.
to be upstream, to be completely independent, we want… we don't want it to be dependent on Elastic downstream in any way.
**Pawel Filipczak** 33:11 By the way, do we have any plans to release the SDK soon?
**Bob Strecansky** 33:16 We can.
**Pawel Filipczak** 33:18 So, maybe it will be good to do that. I will then try to include the metrics I implemented to the distro.
**Bob Strecansky** 33:28 Okay. Yeah, I can try, I'll try and do that this week.
**Pawel Filipczak** 33:32 Cool, thank you.
**Bob Strecansky** 33:34 You're welcome.
**Sergey Kleyman** 33:37 By the way, guys, I remember asking in the past, do you guys use metrics in any way in your usage of OpenTelemetry?
Or it's mostly traces?
**Chris Lightfoot-Wild** 33:48 I'm personally not using metrics yet, but with the problems I had in the past, that was probably the main reason why.
**Sergey Kleyman** 33:58 of this.
**Chris Lightfoot-Wild** 33:58 I still want to try the distro, which probably solves all those problems.
**Sergey Kleyman** 34:02 But I'm not sure, you probably refer to the problems we discussed in the past about this inability to accumulate, right? The fact that it gets reset on each request?
I don't think we solved those problems, maybe… maybe we should.
If you're saying that it's going to be an additional motivating factor for you to use it.
That, maybe that will be enough for us to be a motivating factor to fix it. We'll see, we'll look into it.
But technically, it should be possible, like, we do have, A central process that can accumulate stuff from workers, but you still might have similar issues if you run multiple machines, right?
They will still have its own, kind of, counters on each one.
But, yeah, maybe we should look into it. For now, we're just talking about metrics, like, completely independent.
Not accumulating, like… Like, skew memory… How many spans were sent?
Yes, some of them should be accumulated, we'll see how it will work.
Hmm.
**Chris Lightfoot-Wild** 35:07 Were they…
**Sergey Kleyman** 35:08 Nope.
**Chris Lightfoot-Wild** 35:08 as well, then, sorry. What got added to the SDK? Sorry, do you have to turn them on? Is this some sort of environment variable switch or something, or… To enable SDK metrics functionality, or is it just… Hop them by default.
**Sergey Kleyman** 35:29 open.
**Pawel Filipczak** 35:30 Sorry, I didn't hear you.
Bye.
**Chris Lightfoot-Wild** 35:32 So, the new functionality for SDK metrics, is it opt-in, or is it just enabled?
By default.
**Pawel Filipczak** 35:40 So you have to… you have to enable the internal metrics. There is a hotel PHP internal metrics plug, somehow, I… Yeah, yeah, you have to enable it manually.
Aye.
**Sergey Kleyman** 35:55 By default, it's disabled?
**Pawel Filipczak** 35:56 Yes, yes, I mislead you last week, so… because I had it in my scripts, just… and I forgot about that.
I will… I will put it on chat, the option name, let me, let me… So, it's auto… the metrics you name?
One second, copy…
**Sergey Kleyman** 36:17 Is it something that we introduced in this change, or was it… did it exist before?
**Pawel Filipczak** 36:22 It existed before, so yeah, I didn't bring any additional option.
But to get SDK metrics, you have to enable that one I put on the chart.
**Chris Lightfoot-Wild** 36:36 Awesome. Thank you.
**Sergey Kleyman** 36:37 And also, you need to make sure that you use endpoint that either one that's shared for all the signals.
**Pawel Filipczak** 36:44 You have to specify the global endpoint, or the specific one for the metrics.
Yes.
**Sergey Kleyman** 36:52 Right.
And do you know what was the motivation of making it behind the flag? Is it an experimental feature? Like, we were wondering if it might introduce additional latency.
Like, if people will enable this, the fact that we will send on each request metrics in additional response.
We had some concerns, can it potentially introduce latency or not?
**Pawel Filipczak** 37:16 Of course it will. It's opening additional endpoint connection, and it also serializes the data, so if you are not using the native serializer, then it's adding the overhead.
Oh, and if you are not using distro, then you have the overhead on the sending, so it's blocking.
**Sergey Kleyman** 37:37 So, for SDK, it will be disabled by default, as it was before, right? And for distro, we'll probably enable it by default.
**Pawel Filipczak** 37:45 No, in this store, you have to specify this option, too.
**Sergey Kleyman** 37:48 No, but we can do it automatically, is what I mean, like.
**Pawel Filipczak** 37:51 Yes.
**Sergey Kleyman** 37:51 That we can discuss separately. In fact, the distro will not suffer from latency, right? It will automatically send them in background. There is no reason not to enable, because we don't have this performance heat, right?
**Pawel Filipczak** 38:02 Yes, exactly.
**Sergey Kleyman** 38:11 Okay.
**Bob Strecansky** 38:16 Cool.
Anybody else have other agenda items today?
No. Okay.
Walk the boards, or walk the repos real quick and call it a day.
**Sergey Kleyman** 38:34 By the way, just for me, I guess, probably there's a little bit of a rhetorical question. So the fact that you want to split it, Chris, all this testing between the subdirectories and contrib… What is the purpose still having Contrib as one repo? Is that just convenience sake? Instead of having, like, separate read-only repos to be actual repos?
I'm just wondering, like, is there an additional advantage, or is it pure convenience of just having it? And this is how other agents would also do it, just keep all the stuff in one country, and that's it.
**Chris Lightfoot-Wild** 39:05 But I think from what Bob had said in the past, it was that the other languages had, like, a single contrib report, so we were kind of sticking with that pattern, rather than just introducing 80 additional repos into the open source elementary organization.
**Sergey Kleyman** 39:22 Those repos exist, but they are read-only.
**Chris Lightfoot-Wild** 39:25 They exist in the system.
**Sergey Kleyman** 39:26 with the org, right?
**Chris Lightfoot-Wild** 39:28 Yeah, separate org.
**Sergey Kleyman** 39:31 Because unlike SDK, where it's monorepo, there it's also justified from the code layout point of view, right? It's just easier the way it's built. But here, we actually want, on purpose, not to be not in any way dependent on, and not having any shared code.
But we're just keeping them together because it's easier in one rip.
Okay.
**Bob Strecansky** 39:57 Nothing pressing in the repos.
Alright, thanks for your time today, y'all. I'm gonna have to… I'll probably have to miss next week. My brother is getting married next week, so I'll probably be preoccupied, and we'll see you the weekend.
**Chris Lightfoot-Wild** 40:12 Very good excuse, I suppose.
**Bob Strecansky** 40:14 Yeah, I guess so.
**Sergey Kleyman** 40:16 Are you a businessman?
**Bob Strecansky** 40:18 Yeah, into the smooth.
It'd be fun.
**Sergey Kleyman** 40:21 Okay.
Have fun. Thank you.
**Bob Strecansky** 40:23 Look at you on.
**Chris Lightfoot-Wild** 40:24 It is too good.
