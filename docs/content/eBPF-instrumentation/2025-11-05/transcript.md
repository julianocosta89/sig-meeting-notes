SIG: eBPF instrumentation
Date: 2025-11-05
Duration: 49 minutes
============================================================

## Zoom Recording Transcript

**Tyler Yahn** 01:03 Hey.
**Giuseppe Ognibene | Coralogix** 01:06 Hi, Doug.
**Tyler Yahn** 01:07 How's it going? How's it going?
Good.
How about yourself?
**Giuseppe Ognibene | Coralogix** 01:13 Fine, fine.
**Tyler Yahn** 01:14 Yeah, nice.
Giuseppe, did you say that you were gonna be at KubeCon, next week?
**Giuseppe Ognibene | Coralogix** 01:24 No. No, because I joined it too… too late. I will go to the fourth dim, actually, alone.
Oh, okay. Yeah, it's in, Bruxell.
**Tyler Yahn** 01:36 Yeah. Nice.
Hey, Mattia.
**Mattia Meleleo** 01:41 Hello, good evening, or good morning.
**Tyler Yahn** 01:44 Yeah, feels like the same.
**Mattia Meleleo** 01:47 Yeah.
**Tyler Yahn** 01:52 Hey, Steven.
**Stephen Lang** 01:55 Hi.
**kushal** 01:55 Guys, I have one question. I was looking into this OpenTelemetry eBPF profiler, so is there any community meeting for that?
**Tyler Yahn** 02:05 For the profiler? Yeah, there is.
Let me check the calendar really quick.
I think it's just called the Profiler SIG, sorry, there's a lot.
Actually, maybe there's a better way to do this, Sharing my screen. We can take a look.
Let's see… Hotel profiling, so every Thursday at 8… at 8… Guessing AM? Pacific time?
Is what that is?
I don't… See it on the calendar, though.
So… that might have changed.
Huh.
**Nimrod Avni** 03:33 Profighting sake?
**Tyler Yahn** 03:34 Yeah, the profiling, so yeah…
**Nimrod Avni** 03:36 I have, like… Oh my god, I remember it used to be, like, tomorrow, but…
**Tyler Yahn** 03:42 Yeah…
**Nimrod Avni** 03:43 Oh, just now, don't… maybe they can't, but next week it is, so maybe they can still cancel it just this week?
**Tyler Yahn** 03:52 Yeah, that might be it, actually.
Hmm.
Yeah, I mean, I guess with, like, KubeCon as well, maybe they're… That's, like, next week. I don't know. I don't see it, actually. But anyways, that's where it's supposed to be.
But… yeah… I… I think…
**Stephen Lang** 04:16 13th of November.
**Tyler Yahn** 04:18 Okay.
So yeah, on the 13th of November, there's the EVPF Profiling SIG, that's the profiling SIG, if I remember correctly.
**kushal** 04:26 Yeah. Don't think there's a difference.
**Tyler Yahn** 04:31 Yeah, no, I don't think there's a difference.
**kushal** 04:32 sleep.
**Tyler Yahn** 04:33 And so, I…
**kushal** 04:33 on the next… It's on the next, like, on the second Thursday, the upcoming second Thursday.
So… Maybe it's because of KubeCon, or… Yo.
**Tyler Yahn** 04:46 That's probably… it's probably delayed because of that. Another thing that you can do is you can check out the hotel profiles, Slack channel is a good way to just ask that question, and just… actually, if you wanted to ask other questions, that's a good place to also ask them.
**kushal** 05:02 Sure.
**Tyler Yahn** 05:03 Yeah.
But… But yeah, I think that's… that's probably where I would head for those. Hopefully that helps.
**kushal** 05:11 Yep.
Excellent.
**Tyler Yahn** 05:16 Cool. Alright, so, back to EDPF interpretation. If you haven't yet, please go ahead and add, your name to the attendees list. If you have agenda items you want to talk about, go ahead and add them there as well, and we can jump in here in just a second.
Let me see who's attending… Yeah, 5 minutes in.
I think the… Grafana folks might not be able to attend today, at some sort of off-site, if I remember correctly.
Yeah, and then… Yeah, huh.
**Stephen Lang** 05:47 I'm… I'm here, but Mario's out, Nicola's out.
Raphael's out. Yeah, just me.
**Tyler Yahn** 05:53 Yeah.
Cool, alright, well then, yeah, let's jump in here. So, I don't have too big of an agenda. I did want to point out that we did get a V02 release out yesterday, in case you haven't seen it. The V01 went out and, it was a great success. I think, like, that was pretty positive. We did have some issues with tagging of our images. There was, like, the V01… Technically doesn't have the tags for… I think it's AIM, it's ARM, images. So, if you tried to run out an ARM system.
Sorry, the V02, though, does, because we got our tagging system to actually work correctly, so this is all, it's all straight up, it's all, should be all good at that point.
I don't know about the Helm chart, if we want to go through and update that, or if they have, like, a way to update that, on their own. I'm not…
**Nimrod Avni** 06:43 I think they… we still didn't merge the… I had a fix, because the… I put the wrong, like, image name, because we moved from the GHCR to Docker, or, like, the opposite, so I still have a PR open, so I can change it now before it gets merged.
Oh.
**Tyler Yahn** 07:03 So we… I think, well, we published both, just a heads up on that one.
So, yeah, like, here we can take a look.
**Nimrod Avni** 07:16 You can look at the… there's the Helm chart PR, I think it's still… I think Steven also had a look at that.
I can still do the stuff you talked about with Dee.
App version was gonna short on time.
**Stephen Lang** 07:33 Yeah, no.
**Nimrod Avni** 07:34 But they opened some issues to track it later.
**Stephen Lang** 07:38 Yeah.
Yeah, no, I can help out on that as well, if you want, but .
**Nimrod Avni** 07:44 Is it… maybe Denver? Is there no, Is there nothing open on me? Maybe they already murdered, I don't know.
**Tyler Yahn** 07:51 Remind me your username, Rod?
**Nimrod Avni** 07:53 He brought, Avenue?
**Tyler Yahn** 07:55 Okay.
Yeah, it looks closed.
**Nimrod Avni** 08:01 I guess I got merged today, yeah, it's this one.
**Tyler Yahn** 08:04 Okay. But you can open a new one again.
**Nimrod Avni** 08:08 Because now I think it says still the… 01.
**Tyler Yahn** 08:12 Yeah, okay. That's… that's not too big of a deal. App version.
Oh, I see.
**Stephen Lang** 08:25 It probably helps to have one Helm chart release with the first tag, and then a second Helm chart release with this… with the second tag, just so that you… because you can target which Helm chart version, if anybody wants to test, you know, before and after.
**Tyler Yahn** 08:39 Hmm…
**Stephen Lang** 08:40 So, I think it's fine just to have, This spread across two commits, so there's basically one version per tag, which is fine.
**Tyler Yahn** 08:50 I see Yeah, this… so… I think using the GCR is fine. We could also… We push both, so I don't think there's too much big of an issue here.
I definitely think this is a fix for getting rid of main.
**Nimrod Avni** 09:06 Yeah, and I fixed the main in the Kubernetes cache, and also, like, in the first PR, I got recommended by Povilas to, like, use GHCR instead of… Docker, that's at least what they prefer.
**Tyler Yahn** 09:23 Okay.
Yeah, I mean, I… if that's what they prefer, we do both, right? So, it… yeah, that sounds great.
So… to follow up on this and to upgrade to a V02, Steven, are you suggesting that we… leave the Helm chart version at this, or are you saying we should also upgrade the Helm chart version?
**Stephen Lang** 09:46 But you need to bump the Helm chart version every time.
**Tyler Yahn** 09:49 Yeah, okay.
**Stephen Lang** 09:50 Otherwise, Helm doesn't detect an upgrade, so it won't, It'll be a no-op if somebody tries a helm upgrade. So you have to bump the, The chart version.
**Nimrod Avni** 10:02 Like, do I bump it to, like, if I change the image to 0 to 0, also change the chart to 0 to 0? Because the…
**Stephen Lang** 10:12 Yeah, I mean, maybe we'll never talk about…
**Nimrod Avni** 10:14 with that.
**Stephen Lang** 10:15 Yeah, maybe we want to talk about, like, how we want to handle that, because it doesn't actually matter. As long as Helm sees that the chart version has changed.
then that's enough for somebody doing a Helm upgrade to receive the updates.
But as to what that chart version is, it doesn't matter, really.
**Nimrod Avni** 10:36 I'm just wondering, I don't know how… How we usually, like… let's say we release, like, a minor patch, like, not even a minor, like, just a patch, so we do, like, 0, 2, 1.
And then we upgrade the Helm chart, and then you can… we can also do, like, a change that is only a patch in the Helm chart, but not in the image. Like, I don't… I don't think it really matters if, like, at least if we have… when we have, like, the consistent, like, app version and the home chart version, I don't think it really matters if they, like, stray away from each other.
**Stephen Lang** 11:11 Yeah, what I would say is, when they're different, when app version are different, to chart version.
It gets… there's an extra step you have to see as to, you know, which OB tag you're actually going to be targeting, if you're installing a certain version of the Helm chart.
Whereas when they're both the same.
you can do, you know, have a look at the Helm chart versions, and you know 2.5.0 is 2.5.0, 1.2.3 is 1.2.3, but when they're different, you kind of have to do an extra lookup to see which image tag am I actually going to get?
**Nimrod Avni** 11:45 Yeah.
**Stephen Lang** 11:46 then you can… if you do need to fix something on the Helm chart because the template was wrong, or you wanted to do, you know, like, use a dynamic app version in your templates, then you would need to independently bump the chart version.
So… I don't know, I mean, you could do something like… We could try and keep them in sync, so we could try… maybe the next one could be… You know, 0.2.0 for both app version and chart version.
And then, you could try and keep them in sync, but if we need to fix the Helm chart.
than that.
**Nimrod Avni** 12:21 We can do, like, patches there. Like, every change in the Helm chart that is only in the Helm chart will be, like, patches, but if we upgrade, like, miners, we could be also in the miner.
**Stephen Lang** 12:33 Yeah, or you could use some kind of, you know, hyphenated suffix.
I don't know, that would be, like, Helm chart-specific. I presume, like, Helm supports that.
**Nimrod Avni** 12:44 I can also… maybe I can look what they do in the collector, I don't know, like, or… like, if they try to keep it in line or not, I can… Have a look.
**Stephen Lang** 12:54 Yeah. Yeah.
**Nimrod Avni** 12:56 I'll try to…
**Stephen Lang** 12:56 open up.
**Nimrod Avni** 12:57 PR soon, and, like, to bump it to the new version.
**Stephen Lang** 13:00 Yeah, yeah. As long as the version is changing, it doesn't actually matter.
But it, yeah, it would be nice if the… App version is actually tracking our actual tag.
Because… If not for just reducing the amount of toil there is to actually bump the version.
Because, you know, you have, like, a load of line changes to change the tag, whereas if everything is inherited from the app version.
You just change it in chart.yaml, and then everything gets the update.
**Nimrod Avni** 13:35 Yeah, I think it's good to, like, kind of try to have the app version Aligned with the charge version, but if we need to change it, then… We can diverge.
**Stephen Lang** 13:49 Yeah.
Sounds good to me.
**Tyler Yahn** 13:53 Cool.
Alright, Syndamide, yeah, it sounds like you're gonna work on a PR there. Thanks a bunch for doing that, appreciate it. And then, we'll, keep going here.
Okay.
Okay, so the next thing that I had, related to the last release was also I noticed that, like, we don't have a changelog.
For the project, which is… going to become more problematic as we're trying to communicate, like, what, features and change sets are actually being released in the next, upcoming releases, so… open an issue to add, project changelog, plus, like, tooling and policy around it, There's… In the hotel space, two, kind of, main schools of thought, well, there's probably more than two, there's probably a lot of different schools of thought. On this one, the Go space, though, the hotel, group.
We use this Keep a changelog format. This is just something that I've used for a long time, and I was one of the people that decided on this long before the other changelog 4x existed, this existed, I'm guessing you've seen these before, essentially, like.
different subsections, that are very standardized, added, changed, deprecated, remove, fixed, and security. So, other than that, like, there's nothing there.
This is nice because it's more universal than just, like, our project, but it's also not the standard, I think, that the collector uses. The collector came up with their own, which is kind of like an OTEL thing, which I think came from more, like, the Java world.
Anyways, like, it's essentially these, actually, I don't know all of the suffixes, breaking enhancement bug fixes are pretty common.
The thing is, is that this format is, you can use the GoBuild tools to track this, which is really nice, because then you can use automation, or you can do some sort of, like, automation to, you know, work with these sort of workflows, so… Things like when we do, offset updates, we can then add changelog entries, if we do something without tooling, it, like, you have to kind of manually go in there and add, changelog entries for these automated PRs, which is not impossible. I mean, we do that in the auto-instretation package for Go, so it's, like, something we've already done, but, like, it's kind of annoying.
This is kind of nice, because you can just essentially say, like, create make tags to start up a new, entry. These all go into a directory, so each changelog entry is its own file.
And then, during the release process, what you do is you take all of those, changelog files, and it consolidates them into a single changelog entry, so it produces the changelog as the release happens. Which is kind of nice. It's able to see it. It's a little annoying, because it's, like.
when you're new to the project, or when we institute this, like, for the first few times, it'll be like, how does this work again? But, once you get a hang of it, it's not, like, the hardest thing. I've used them in both projects, so it's kind of, you know.
What it is. So I wanted to bring this up because I'd love to get some thoughts on this so we can put a policy in place if people have strong opinions one way or the other.
I think that we could, you know, go with whatever way you want, I just think that we need to have a way that we Keep it honest, because what happens is eventually, like, we're gonna have… Releases that are, you know, maybe tens, dozens, or maybe even hundreds of features, or changes, and the person doing the release, like, can't reliably construct a changelog entry at that point. And you need these to communicate in the release, you need these to communicate to users, like, what's going out there. So, they're pretty critical for the success and, like, health of the project.
So yeah, it's gonna be a responsibility of people who are submitting changes to, you know, ensure that that is included in the change set that they're actually submitting, when it's appropriate. Obviously, there's, like.
Stupid things like version bumps and that kind of thing that aren't required, but yeah.
**Stephen Lang** 18:08 So, this is in addition to the… Release notes generated by the commits.
And GitHub.
**Tyler Yahn** 18:16 Yeah, so what I normally like to do is kind of like what we did here, what's the wrong thing to click on? Is… So, yeah, kind of like this, so… the top section is what I would say is, like, the release notes, and these are essentially the user-specific communication, so it's at a high-level overview as to, like, if I'm a user, end user, I don't want to read through, commit messages and, like, PR titles. This one's not too bad, but, like, I think if you take a look at… No, that's in the right spot, actually. If you take a look at, like, the V01, like, you can kind of see, like, this becomes very… hard to figure out what is included, you know? Like, you have hundreds of different, entries, right? And, like.
**Stephen Lang** 19:10 Yeah.
**Tyler Yahn** 19:11 Yeah, I mean, I guess you could kind of search, and even searching sometimes is not really that helpful, because, like, you know, a lot of the times, like, there are different, like, features that are included in one PR, and, like, they aren't broken out in a PR title, they're, you know, encapsulated inside the PR.
So, you know, like, BPF fixed load error, like, there may have been other changes here as well, right? Like, and we want to make sure those are communicated that are relevant to the user, is kind of how that is. So yeah, I think the idea is that, like, we can still include this. I think this is great because it tells you… Like, in the release itself, like, what is included, so it helps communicate, like.
the full chain set, if you wanted to find a PR, like, if… If you're looking for a fix, right? You want to find out what release that fix is associated with.
We can try to use milestones, which I think is a great idea, but you can also just look at the release notes like this and say, like, hey, search this PR title, oh, it was here, so it's easier to find that way.
And I really like this for motivating new users to the project to show, like, we care about their contributions. So I would say we continue generating that, but I think that what we want is also just something at the top that users can read through really quickly to say, like.
Yeah, this is what's, what, like, is relevant to users at this point, yeah.
**Stephen Lang** 20:25 So this is something that you would do along with every PR, make sure that your PR has a changelog entry, if applicable.
**Tyler Yahn** 20:33 Yeah, correct. And if applicable, is pretty, Yeah, it's pretty lenient. So essentially, like, the way that we've classified it in, like, Go is… It's any sort of, like, user-facing change. And so that means, like, if it's gonna be an API change, if it's going to be a behavior change, if it's gonna be a severe or, like, dramatic performance change, like, these are things that users are going to care about.
If you're reshuffling code, if you're, you know, doing minor upgrades of, like, dependencies, if you're doing, like, you know, small documentation fixes or something like that, like, these are things we usually say, like, no, don't worry about it.
And it determines, and, like, the automation will check, and so if you don't have a PR, it'll fail the CI. It says, like, no, this is a changelog entry. But if you deem that it's worth it, One way we've done it is you can just put it in the title, you can call it a chore, and it will just skip that check. Another way is you can just tag it with a label, and it will just say, like, skip changelog, and then you don't have to have it run at CI.
But yeah, so essentially, like, there's a rule enforcement on each PR that you have to, like, if you're going to submit something, you need to either explicitly say, like, no, this isn't… Like, worth a changelog? Or… add a changelog, yeah.
**Stephen Lang** 21:44 Yeah, I like the idea of, Using the… the labels.
I'm… Also, I wanted to point this out with, maybe we can do a bit of both. So this is an example release.
That I just put in the Zoom chat.
And… there's a feature in GitHub releases which I didn't know about.
And it can split up the, the commit messages by headings based off of PR labels.
So I'm not saying that this is a replacement for the changelog, because what you've said about providing a, a TLDR, effectively, or, you know, highlighting important breaking changes, I think that makes a lot of sense.
But also with the huge change lock that we had in, 0.1.0.
Even just separating out, you know, the dependencies into a separate heading.
like, is something that we could do, as well as maybe, you know, looking at the changelog. But also, another option, maybe, an option three, is you could just use PR labels to separate things out into something that looks very much like the hotel example that you showed, which is, you know, what's a break and change, or what's a… an announcement, or whatever. This could be, like, a really lightweight, lightweight.
Way to do it, but there's nothing to stop you from I'm doing both, or having something super simple like this, which is just two sections, just to split out the, all the renovate PRs.
**Tyler Yahn** 23:13 Yeah, yeah. So wait, how is this, curated? Like, what… what generate… what moved this into a… oh, is it the dependencies? If it has, like, a dependency tag, then it moved it over here?
**Stephen Lang** 23:23 That's it, yeah.
**Tyler Yahn** 23:25 Yeah, oh, okay.
**Stephen Lang** 23:26 So GitHub has this, this whole doc, which I'll just drop into the chat.
a… I wanted to show you what the end result looks like, because the docs don't do a very good job.
**Tyler Yahn** 23:39 Yeah, yeah, I gotcha.
**Stephen Lang** 23:41 But you can… this is where you can choose, like, which labels go, or, you know, so you've got Changelog configuration options at the bottom there.
**Tyler Yahn** 23:52 Mmm, oh yeah, yeah, I see.
**Stephen Lang** 23:54 So it ties into the existing release action, which you're already using, and you just add a couple of config lines.
And it could, sort of split things out by PR labels, for example.
**Tyler Yahn** 24:05 Yeah, yeah.
Yeah, I mean, I really like this. This is great. I… Yeah, and even look at that, they've got, like, braking changes and everything.
**Stephen Lang** 24:16 So what I was thinking is, like, if, for example, you're coming to do the release.
**Tyler Yahn** 24:20 And you… well, I suppose you don't get…
**Stephen Lang** 24:23 you don't get this changelog until you've done the release. So did you… Did you go back and edit the release notes to add in the text at the top?
**Tyler Yahn** 24:34 At the top, no, so, normally, the workflow I have is, when you're drafting a new release like this, You essentially can put in whatever you want, and then, once you select a tag, right, like… It won't let me do it, because it's already done it, but, like, you can generate them here, and then you can just go back.
**Stephen Lang** 24:53 Okay.
**Tyler Yahn** 24:53 And you manually paste it in, essentially, up there.
Yeah, so that's how it's been done in the past, and I mean, I'm sure… Yeah, I see… I see it's… it's done through some sort of, like, work… workflow here,
**Stephen Lang** 25:07 So it's the same release notes generator that is the normal GitHub release notes generator. It's just you add in an additional config to that to say, split that big list up into multiple sections.
**Tyler Yahn** 25:20 Oh, okay, so if I click that button there, it'll use this to figure that out? Oh, okay.
**Stephen Lang** 25:24 Yeah, yeah, so it's not like a separate… it's GitHub native, if you like, it's not like a separate…
**Tyler Yahn** 25:29 Yeah. Okay.
**Stephen Lang** 25:30 It's just additional config to the release notes generator.
But you could, in theory, so if you were to do 0.3.0 with the config like this, you could generate the release notes, but at least then.
whoever's doing the release wouldn't be looking at the huge block of, you know, all changes. It might then be split, and then it would be a lot easier to say.
Oh, this is… you know, this group of three commits is actually a single feature that I have to highlight.
**Tyler Yahn** 26:00 Yeah, I really, I really like this. The only thing that I'm thinking it may be missing is when you have multiple features going into a single PR, and how to, like.
**Stephen Lang** 26:09 Yeah. Yeah, like, how…
**Tyler Yahn** 26:12 I mean, we could always just say, like, don't do that, but, like, sometimes, like, it's easier to, like, I don't know.
Yeah, I don't know, I like this because it gets out of the way a lot. Like, it really… it helps, like.
be more automated, and we can… we can do a lot of labels and tagging, I think that that's something you can do after the fact, like, even, yeah, before the release, but… Yeah, I guess that's the only other thing, but I, I think, Regardless, let's add this to the, the issue, and maybe we could talk a little bit more about here. I might be in favor of just starting with this, and if we find it to be too… Limited, then we could maybe look at, like, other options here as well.
**Stephen Lang** 26:57 Sure, yeah, and I don't think it's really a replacement for, you know, the curated version.
But even, I think, we could just benefit from splitting out the dependable or renovate PRs, you know.
**Tyler Yahn** 27:08 That is… yeah, that would be huge, yeah. At the very least.
Yeah, so maybe, yeah, maybe that's… maybe that's the answer, is maybe we do both. It's like, like you're saying, like a… I curated, plus, like, tried to get a little bit better in, like, this… this… parsing here. I think, yeah, like you're saying, just splitting up the dependencies would be a big change, so yeah.
**Stephen Lang** 27:27 Yeah, so you could potentially do both, though, because you were saying we could use PR labels, this is what got me thinking about it, to, you know, tag particular things as breaking changes, or… you know, new API or something that you want to highlight with categories that we define.
But you could actually reuse those labels for the auto-generated Release notes as well.
So they kind of… Kill two birds with one stone sort of thing.
**Tyler Yahn** 27:58 Yeah, I… I think you're right. I think that's… that'd be… that'd be cool.
Yeah, okay. I think that sounds good. I think that's… Great feedback.
I'll keep thinking about this. If you have more thoughts on this, and, like, a proposal, or anything like that, please comment on this, otherwise we can move ahead and, try to get this in place.
Sooner rather than later, so that we don't get a bunch of piled up work.
Yeah.
Okay, cool. Next up… I just wanted to do a review of the open PRs.
I, let's see… I think we've got a few in here that have been for a while, so this upgrades… Still need… to look at this, I imagine this isn't gonna happen until after KubeCon, so probably not till… Not next week and the week after. For these three, these definitely need some… some more insight into what's going on here. I think… I think there was a PR… by Mario to fix… yeah, this one right here, sorry. But it was also… still needs some work on it, so yeah. I think that those we can just skip over.
**Stephen Lang** 29:04 I think from… from Mario's… point of view, the… what he was saying is, at the moment, we have separate images for Tempo and Metheus.
And the difficulty is getting those to be, you know, compatible with each other, so that you're using releases in sync.
And so he was suggesting to remove the independent images and use the OTEL LGTM image.
Which is a single container image that has Multiple databases in it.
Oh. And then that is kind of more guaranteed that you'd have A set of databases which are compatible with each other at certain versions.
So I think that's what he was… Yeah, so he's mentioned there the single LTEL or GTM instance.
**Tyler Yahn** 29:49 I mean, I'm not…
**Stephen Lang** 29:50 I mean…
**Tyler Yahn** 29:51 Sounds great.
**Stephen Lang** 29:52 Yeah, so that would mean that you wouldn't have to track just an individual database upgrade, you'd effectively get a, A single container that contains them all.
Yeah, I…
**Tyler Yahn** 30:04 I think it's just we have to get this to work, though, is the only thing, right?
**Stephen Lang** 30:10 Yeah.
**Tyler Yahn** 30:11 Yeah, otherwise, I think, I think that's a great idea, yeah.
But yeah, so, we'll… we'll keep tuned on this one. I think this just needs more follow-up on… on making it work.
I think this is Giuseppe, right? Your PR here?
**Giuseppe Ognibene | Coralogix** 30:29 Yep.
Finally, all the tests.
I'll work.
**Tyler Yahn** 30:35 Yeah, it's got 2 reviews, looks like the tests are working.
I guess it's ready to go. Any… Reason people want to talk about it more?
**Giuseppe Ognibene | Coralogix** 30:45 I mean, the tests were failing, I don't know why, actually. With Mattia, we… we debugged it a bit, and basically the problem was that the last success server was not responding, even if we incremented the timeout, like, to 37s.
And then we… we didn't create the spawn, the last six-edge spawn, so the test was failing later.
I just changed it instead of a post, I'm using a GET, and everything is working.
**Tyler Yahn** 31:17 Yeah, I… That is weird, actually.
**Mattia Meleleo** 31:23 Yeah, I don't know if it's…
**Giuseppe Ognibene | Coralogix** 31:24 If it was because of the…
**Mattia Meleleo** 31:25 resource constraint?
Sorry, I don't know if it was because of a resource constraint, but on CI, the Elasticsearch Server, hangs sometimes on that endpoint, so… Yeah, that was the issue, basically.
**Tyler Yahn** 31:45 Well, okay, it looks like.
**Giuseppe Ognibene | Coralogix** 31:46 It's resolved.
Locally.
Yes.
**Tyler Yahn** 31:50 Is it a flaky test, or is it… Like, have you been able to update it so that it's reliably able to succeed now?
**Giuseppe Ognibene | Coralogix** 32:04 Sorry, I lost you, I don't know if I have a connection problem.
Yeah, so it's just that…
**Tyler Yahn** 32:10 Yeah, the… the change you made to switching to a Git instead of a POST, right? Like, that's… that's… should fix it reliably. It should not be a flaky test, right?
**Giuseppe Ognibene | Coralogix** 32:19 No, no, no, I also tried, two times, on DCI, and it's working.
Locally, I tried, like, 100 times, never failed. And, actually, the strange things was that that piece of code was already introduced in the Facebook request, not in this one.
So it was really… Break, yeah.
**Tyler Yahn** 32:44 Yeah, okay.
Well, cool, alright, yeah. Well, thanks for the contribution, yeah, this is great.
Excuse me.
Okay, moving on.
This is… Do not merge, yeah, this needs to get… cleaned up. For some reason, it's trying to do an upgrade on our 117, CI, which shouldn't happen based on a renovate config. So, this, again, is something I was looking into, as well as Mario, just haven't figured it out yet.
Mattia, I did want to ask you about this one, though. This upgrade. This… Yeah, I see… I see what you're saying at this point.
Oh, you responded as well. Yeah, so…
**Mattia Meleleo** 33:28 Yeah, I added a CI check to check that these two files are in sync now.
**Tyler Yahn** 33:34 Oh. Even better. Okay. Then, yeah, that sounds great. Let me, yeah.
I felt bad, I just saw this this morning, and I meant to respond yesterday, but, This looks great, I'll just update.
Yeah, okay, cool. Yeah, let's… let's merge this, then.
Cool. Where's the button?
Oh man, Zoom is always in the way.
Okay, cool, another one merged. Yeah, making a lot of great success.
Other than that, I think that's all the open PRs that we wanted to talk through. Yeah, once this is done, we'll have a lot more, these two should go away, and then this can get addressed as well.
Okay, cool, I think I saw, yeah, Nimrod, you wanted to ask about nightly builds in the main build.
**Nimrod Avni** 34:45 Yeah, many a question, like, I don't know what's our, like, versioning policy, or, like, what… when we plan on releasing stuff.
Now that we have, like, a stable version that we can, like, say, like, reliably works, and we have two, and we also have the main one, which basically gets pushed every time we have main, so we can… I guess we can just keep, like, both of those, and I don't know, do… have, like, patch versions when we feel like a bug that's, like, big enough or something?
is being fixed, or we can also, like, combine… I know other, like, parts of the hotel, community do, like, 90 builds? That's, like, doing one build a day, and what… and I don't know. But I think, like, our main one is, like, a super version of the… of the 90 build, because we do it on every PR.
Yeah, just, like, yeah, I want to know, like, what's our, like, when we want to release new… either minor versions or patch versions, and if we should just remain with our main build as, like, something that, for people who want to get, like, the newest, newest version, can still, just go through the main build.
**Tyler Yahn** 36:01 Yeah, I think the main build is really nice for, like, people who are developing this project, because then you can take that, and you can wrap it in something else, or you can use it in your own test server, or something like that, so I see, like.
I see that that's how its main use is going to be.
like, end users, I doubt, would want to use it, because there's probably going to be some things that are breaking, there. So, yeah, I think that seems fine to me. Like, I think… The only reason to go to, like, a nightly build compared to, like, a main build is if, like, the image cache or, like, the image server is getting overloaded with the number of images we're pushing to it.
Which may be a thing, eventually, but I think right now, I don't… no one's complained, so I might just say, like, keep it where it is. It has the benefit of, like.
you know, the nightly build kind of stinks, where if you don't make any changes in a day, it is still gonna build. The main build doesn't have that problem, like, if you don't make changes in a week, it'll only build what is being built, or what is new, right? So that's kind of a benefit of it.
But yeah, I think, I think that's… that's fair.
As for, like, when do we cut, like, versioned releases? That's another good question. I think that that's something, like, we definitely have some open issues on, like, our versioning and stability things, like, that's important to think about through as well. Like, we don't have a 1.0, just pointing that out as well, like, so… feature changes going into this binary, like, are… they can still be breaking, right? So, like, we wanna, I think… we want to nail down what we'd say, you know, happens when we do go to a 1.0 and, like, what we aren't going to break. I think it also helps us to say, like, what we are going to try to do in the interim as we get to the 1.0. You know, a lot of projects will try to do backwards compatible changes, you know, with some, like, opt-in and then opt-out sort of things.
Other projects are just, rolling release, where every, you know, if you're not in a 1.0, it's gonna be breaking each time, and you gotta pay attention to it, in the release notes, so… Yeah, I think those are things to decide.
I think the cadence that we want to try to, get things out.
it kind of depends on how fast we're developing things. Like, if we're putting out 100 features a week, which is great, I think that'd be awesome. Probably want to release every week, but… I imagine it'll take a little bit longer to get a substantial amount of features that people are going to want to see. You know, new, instrumentation, new features within existing instrumentation, that kind of thing, maybe optimizations as well. Like, all of those things, like… usually, I think, you know, we can decide on what we want to do. We could try to go for a week, we could try to go for every, 3 months. I think, you know, maybe we can just wait and just, you know, often what it is is, like.
I've seen in other projects is somebody releases something that's really cool, and they want to start using it at their project, or they want to have a customer use it, or something like that.
And that's usually when we start kicking off releases, If we can automate releases to make it even easier, then it's, like.
the faster, the better. There's really not a downside to doing something like that, like… Obviously there's a little bit of churn, I guess, on the end user's perspective, like, if they're always upgrading, but, like, if you're rolling out a bunch of new features, you're getting a lot of people, like, interested in the project, you're getting a lot of new things that are exciting, so I don't see a really big downside there.
So I guess to answer your question, it's up to us, when we want to do tagged releases, and so, yeah.
**Nimrod Avni** 39:28 Oh, sounds good. Yeah, just wanted to, like… I guess if we have… let's say, again, like you said, if we have, like, a customer or something, and we just added a feature, and we already… we want to push them to… to already use it instead of, like, going through the main build, we can just, like, I don't know, ping the OB channel and say, maybe we can do, like, a patch version, we added this and this and this.
And, we can release it.
**Tyler Yahn** 39:57 Yeah, I definitely think that's… that's reasonable. If we can get, like, There's other… there's been other attempts and other projects I've worked on.
to get a continuous delivery system going, so it's, like, essentially very easy to spin up those PRs. Like, right now, it takes a lot of… it doesn't take a lot. It takes some work from, like, a developer to actually, like.
run the make commands and curate that changelog and, you know, do all these things, but if we can build automation around that, where it takes 10 minutes to do a release.
There's, you know, if… if it's me stopping for 10 minutes to get that thing out is… is not a big deal. Stopping for, you know, an hour or two is also not a big deal, but, like, it's, you know, if I'm gonna be doing that every day, then that's… that's not really feasible, as well. So, yeah, I think… I think if we can do that, like.
the smaller the feature set per release becomes more realizable. Otherwise, we kind of wait to bundle it, I guess, yeah.
**Nimrod Avni** 40:55 No? Cool. Sounds good.
**Tyler Yahn** 40:59 Yeah, okay.
Well, cool. Yeah, I imagine, Yeah, we'll talk more as the next release comes up, as to when we want to do it, so, yeah.
**Stephen Lang** 41:08 I don't know, I just… I just realized.
Are you manually creating the Git tag?
And the release in GitHub at the moment. Okay. Because the thing that I linked… That's assuming that you already have a GitHub action that's triggered on Tagpush, based on a certain pattern.
So, like, when you do a git tag push of a, you know, V something something something.
and you trigger a GitHub action, and it generates the release notes for you, then you can use that config file.
**Tyler Yahn** 41:39 Yeah, okay, that's what I was thinking. Okay, okay.
**Stephen Lang** 41:42 Yeah, but it sounds like we're missing that.
**Tyler Yahn** 41:46 It does.
**Stephen Lang** 41:46 What you do lose, though, with automating that is you can't then, you know, Put in your, your manual TLDR at the top.
**Tyler Yahn** 41:57 Yeah, so I think, like, you… You can't, but you could if we did, like, the collector changelog.
**Stephen Lang** 42:04 I see.
**Tyler Yahn** 42:05 Right? Like, Or even if we did the other one, we could kinda… we could do some, like, horrible bash code to try to, like, generate it, but, like… Yeah, That's a good point. We should try to figure that out, though. That's why I'm also thinking, like, it may not be worth… doing that in the first phase, and maybe just using, like… I'm sorry, using the tagged thing with the GitHub automated, like, what's… what is happening, maybe just be a great first step in, like.
We can just start… we can just start doing that, and then doing the curated TLDR may be something we want to do in the future if we're… if we're not clear on these sort of things, so… Yeah, I, I… I kind of like that idea of just using these tags, but we could maybe just see how far we could take it as well.
But yeah, good point, thanks for pointing that out, yeah.
**Stephen Lang** 42:54 Yeah, yeah, I could add that, release action if you want, send you a PR with what it would look like just to auto-generate based on when you do it. So the only thing you have to do Is git tag, and then push the tag.
And then it'll… it'll trigger everything else and build everything else for you.
**Tyler Yahn** 43:12 Yeah, and you know, it just came to me, like, you can always edit releases afterwards, which we've done many times. So if we wanted to put a TLDR, like, we could always just do.
**Stephen Lang** 43:20 Yeah, they're backing it in.
**Tyler Yahn** 43:22 Yeah, yeah.
**Stephen Lang** 43:23 Yeah, you can't modify the commits or anything, but you can, yeah, change the description, presumably.
**Tyler Yahn** 43:28 Yeah, and we're also looking to lock down, like, the artifacts that are associated with the commit, so if we did want to do, like, artifact signing with our own, like, GPG keys.
Which, if we start distributing binaries, I think is something we would want to do, but we've talked about that in the past as well. There's other pipelines I think we can use, but like… That might be a little bit harder. Right now, just distributing Docker images is a lot easier to just, use the Docker tools to validate the images themselves. So… But yeah, but… yeah, otherwise, I think that should be… that should be a good first step, at least.
**Stephen Lang** 44:03 Okay, and because there's GitHub artifacts as well, I don't know if they, are signed.
In any way.
**Tyler Yahn** 44:10 No, they aren't. So that, yeah, that's the thing, is like, it'll build a tarball in a zip file for the repo, and it'll associate it with the release.
And they're not signed. There is a way to, like, use the GH tool to, like, ask GitHub to verify the download, essentially, but, like… if you can't trust GitHub.
hasn't mutated the tarball, why would you trust them to verify the mutated tarball? So, like, it was always, like, one of those things where, like, and it's not critical here, not a lot of people use this sort of feature, But, like, in our other projects, what we've done is, like, you know, each one of our maintainers has GPT keys because they sign their commits, and so all of those tarballs we would download, verify them, sign them, and then upload the signatures, after the fact. You can't do that if you don't… if you have, like, static releases, which is something that OTEL is considering turning on. So we actually would have to do that beforehand.
And I think that becomes more relevant here if, in those artifacts, we include binaries, because if we're trying to, like, just build, like, a compiled binary that somebody can run outside of a Docker image, That absolutely needs some sort of signature associated with it, and… I think there's more to talk about there, beyond just the releasing structure, but, like, I think that's maybe something we should, you know, cross that bridge when it comes, kind of thing, yeah.
**Stephen Lang** 45:37 Yep.
**Tyler Yahn** 45:38 So, yeah, I think… I think I love if we could get this automation working, just to, like, fix these releases, because I… the faster we can get releases out, I think the more, we can get momentum going in the project, so, yeah.
But yeah, please, if you wanted to send a PR or link an existing file in that issue, that'd be great, I'd love to see it.
**Stephen Lang** 45:59 Sure, I'll do that.
**Tyler Yahn** 46:02 So one of the last things that I forgot to add, but, I'll just add it here, is the next week is KubeCon, I… don't think a lot of us, or not everyone on the call is going to be there, but a lot of us are, is, do we want to cancel, next week's SIG meeting, in favor of… just waiting a week, or the people that are there, we can plan on meeting while we're at KubeCon.
**Giuseppe Ognibene | Coralogix** 46:34 By moment.
**Tyler Yahn** 46:36 Okay.
I will also post in a channel, but I'm seeing some thumbs up, so yeah, let's… let's plan on that, and then if there's any opposition, we can… Go from there.
Well, cool.
Alright, everyone, any other topics people wanted to talk about?
**Stephen Lang** 47:01 If we are meeting next week, I don't think we got a time on the calendar.
**Tyler Yahn** 47:07 Oh, at KubeCon?
**Stephen Lang** 47:09 Yeah.
**Tyler Yahn** 47:10 Okay, cool.
**Stephen Lang** 47:10 Or maybe, maybe post on the channel.
On Slack.
**Tyler Yahn** 47:15 I will, I'll try to find the doc with the schedule as well, and then I'll post that, so yeah.
**Nimrod Avni** 47:20 Steven, is that, what you sent and tagged Mario about? The observatory thing?
**Stephen Lang** 47:27 That's right, I think it's… I think it's that the… although this…
**Nimrod Avni** 47:30 Yeah, the schedule is.
**Stephen Lang** 47:33 read-only, but then there's the form, which I think you have to fill in.
If you want to get onto the schedule, but there's, looks like there's only… A handful of slots left, which are just… Either late on Tuesday, Or, around lunchtime.
**Tyler Yahn** 47:57 Yeah.
**Stephen Lang** 47:58 I'll just do something that's not on the official schedule.
**Tyler Yahn** 48:02 Yeah, I mean, we could always do that.
Yeah, that is… it's pretty loose, like, it… to be honest, like… this is more for the community. Like, if we all want to organize something and, like, just go find a space to go hang out and talk, like, there's nothing stopping us. It's more to, like, to market to the community and saying, like, hey, if you want to come talk about eBPF interpretation with all the maintainers, all the approvers.
All the approvers should be in one place, they're all gonna talk at that point, Yeah, like, in the past, like, it's not really well structured in the sense that, like, there's gonna be a formal agenda and everything's gonna be happening, it's more just, like, people come and they're interested, they want to talk about this subject, so, yeah.
But yeah, I'll, I can also just ping Antoine and see if it's possible just to get on the… because it looks like there's only some spots in the early morning, like you're saying, Steven, and then… Actually, I don't think there's anything… even, oh, I guess, like, 5 to 550.
Hmm.
Okay, I'll ask Antoine to see if there's still some time.
But otherwise, yeah, we can just do something, ad hoc as well. Like, there's nothing stopping us from just saying in the channel, like.
We're all gonna plan on being here at this time, so show up. Yeah.
Well, cool. Yeah, if that's the case… we can end it here. I'm excited to see most of you, next week, in person, but otherwise, I will see the rest of you, in two weeks' time.
Alright, I'll talk to y'all later.
**Giuseppe Ognibene | Coralogix** 49:42 Hello, everyone.
**Mattia Meleleo** 49:43 Bye.
