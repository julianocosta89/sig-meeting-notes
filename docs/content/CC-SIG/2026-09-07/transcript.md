SIG: C/C++ SIG
Date: 2026-09-07
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Marc Alff [MySQL]** 00:17 Hi, everyone.
**Douglas Barker** 00:24 Hey, everyone.
**Marc Alff [MySQL]** 00:27 Hey, hi, Duke.
**Douglas Barker** 00:30 Hey, Mark.
**Marc Alff [MySQL]** 00:49 I only prepared a few notes in the… In the Google Doc. Doug, do you want to share a screen, or shall I share mine?
**Douglas Barker** 01:00 If you can share yours this time, that would help.
**Marc Alff [MySQL]** 01:04 Okay.
And, hi Nikhilh, thanks for joining.
**Nikhil Bhatia** 01:43 Hi, Mark.
**Marc Alff [MySQL]** 01:47 I don't know if Tom and Ladit can join today, I've not heard from them.
So, Duke, a while ago, we discussed, so, today we have two meetings, one on this one, on Monday.
And another one on Wednesday, which is happening sooner.
So… is it okay for you if we move everything to Monday, then?
**Douglas Barker** 02:23 Yeah, that works for me.
**Marc Alff [MySQL]** 02:25 Okay, so… I wanted also… I think Tom and Lalit said okay on Slack, but I wanted to double-check with them before filing an issue on… in community to actually Change remitting times.
Okay.
So… I guess I will do that, so that we can… We need to file an issue to change the meeting times and have the calendars adjusted, and everything like this.
After that, we should be good to go.
**Douglas Barker** 02:56 Perfect.
**Marc Alff [MySQL]** 03:02 Nikhil, any specific topics you want to discuss since you're here? I don't know if you have… Some questions, or… It's not just passing by, or…
**Nikhil Bhatia** 03:17 No, Marc, I was just passing by. I… like, it's a long time contributing, so I thought I'd join today.
**Marc Alff [MySQL]** 03:24 Yes. So, things have changed quite a bit recently.
Especially, there's one thing I wanted to show you.
Yeah.
This… This is basically the number of PRRs that we just merged.
this year.
So, if you look at the entire history of, OpenTelemetry, in the best month, it was, like, 50 PRs in early development, and then, Something, like, in the 2030s, and since, since the spring, we have been systematically way, way other than that.
And the worst just happened with more than 100 PRs in a month.
So… We are seeing a flood of PRs, a flood of issues as well.
And, most… Important activity so far is trying to cope with that and to do reviews.
And, I have to say, it's a… it's a challenge because of the volume, and we need to figure out how to… how to scale that.
So… Compared to what you… you saw with OpenTelemetry earlier, this is the… Some recent changes.
And another recent change also is, I'm actually quite pleased we did a massive cleanup in the codebase. We've seen, ceiling tidy.
It's almost there, there's only one thing to… left to clean up, but it's, the codebase is actually cleaner and cleaner after all that effort.
And also, there's one contributor in particular who did A lot of testing, banging the curl code to death, and she found, actually, quite a few issues which have been addressed.
Either in the production code or in the unit tests, so… It's generating volume and work, but I think it's good for the codebase in general.
**Nikhil Bhatia** 05:55 Those are a very large number of commits.
like, for the month of August itself.
Yeah.
**Marc Alff [MySQL]** 06:02 It's 106.
**Nikhil Bhatia** 06:05 Oh, that's great.
I think AI is helping us a lot in this.
**Marc Alff [MySQL]** 06:11 It's a lot, and it's, it's especially taxing in terms of reviews, because it's, It takes time to review everything, and to… To provide comments and, have the comments addressed and things like that.
And for the first time, merging was actually a very… heavy job, because, because of a turnaround time in CI, like.
You need 2 hours, or 2, 2.5 hours to actually do a full build.
So, if you merge one issue, one PR, you need to wait, like, 3 hours to be able to merge the next one after that. So, just the time it takes to merge is also starting to become an issue as well.
Doug, is this… do you… is this your view also, or…
**Douglas Barker** 07:12 Yeah, I think so. The, there's so many things that we can do with the build times. The bottleneck at the moment is the Windows build. Takes a long time.
**Marc Alff [MySQL]** 07:22 Yes.
Maybe, well… The build time is one thing, but what is really slowing us is, Just being able to do the… to approve the code and do the review themselves.
**Douglas Barker** 07:37 Right.
**Nikhil Bhatia** 07:41 Yeah, I agree that, review takes a lot of time.
And, especially the larger ones are harder, even harder to review those.
**Marc Alff [MySQL]** 07:56 So… I just… so, for the meeting notes, I just copy and paste what you had last week, Jug.
The most important things for me, I think, are, to… To be able to release soon.
So, for this thing.
We're almost there. There are only, two issues, that have… part of that list that has… are not merged yet.
I tried to look at this one, but it's involving the metric aggregation code, so it's… I'm not too much familiar with it.
I was hoping that, maybe Lalit can provide some comments and approve it.
whole… Did you have the chance to look at it first?
I do.
**Douglas Barker** 09:03 I haven't gone through it, in depth.
But, it looked like Lillette was catching some things and had some good feedback, so I don't know.
**Marc Alff [MySQL]** 09:12 Yes.
**Douglas Barker** 09:12 Close to being, approved or not.
**Marc Alff [MySQL]** 09:19 I mean, I just looked, very quickly, so… It's… it kind of looks okay, but it's very hard to tell the… for the details, because I don't know the details for this code. Metrics in general, and aggregation in particular, it's, There are a lot of tricky things there.
Yeah.
**Douglas Barker** 09:39 And that Phase 2 aggregation is probably the most complex part of that code, too.
**Marc Alff [MySQL]** 09:43 Yes, that's right.
So, I don't know… What to do, whether we should wait to… To include this in the release, or if we should just postpone it for the next time.
Because, with all the… all the changes that we had recently, I think we should make a release soon, and not wait forever.
**Douglas Barker** 10:10 Yeah, I agree. Maybe we, ping a little light in Slack and see if he's, At the point where he wants to approve this, or if not, we can.
**Marc Alff [MySQL]** 10:19 Cool.
**Douglas Barker** 10:19 It makes… makes a.
**Marc Alff [MySQL]** 10:22 Yeah, I think we can do that.
And this one, I think it's, It's some cleanup that you did, I think. Where is it?
**Douglas Barker** 10:34 Yeah, so there's still an open PR to move all the tests. It's a lot of file changes, but it's… that PR's been open for about 3 weeks now. I think what I'll do is probably split it up and do, like, fewer changes.
We don't need to block their release on that.
**Marc Alff [MySQL]** 10:51 Okay.
**Douglas Barker** 10:54 Is that 4-4?
**Marc Alff [MySQL]** 10:55 Cause you… Is it this one, or…
**Douglas Barker** 10:58 That one I do want to get into the release, we can talk about that one later.
**Marc Alff [MySQL]** 11:02 Okay.
**Douglas Barker** 11:03 Right now, but that's needed. And then the 4441 is the…
**Marc Alff [MySQL]** 11:07 Okay.
**Douglas Barker** 11:08 Is the one that's the next step for the… the refactor of SDK Builder that's just moving all the tests and breaking them into their individual signal, test files.
**Marc Alff [MySQL]** 11:17 Okay.
Okay, so, I'll try to look at this one, yeah.
**Douglas Barker** 11:23 Yeah, it's a lot of changes.
**Marc Alff [MySQL]** 11:25 Because of it.
**Douglas Barker** 11:25 SDK Builder itself is 2,500 lines, and then the test file's about the same, so… I'll, I'll break this up into smaller ones, but we don't need to wait on the… Release for this one.
**Marc Alff [MySQL]** 11:38 Oh, yeah, but it's test-only, anyway.
**Douglas Barker** 11:41 It's only test, yeah.
**Marc Alff [MySQL]** 11:43 Okay.
Well, just don't break it. I will try to take a look. If it's test-only, we are not taking that… a great risk anyway.
The worst that can happen is a build break, which we will catch pretty much with CI anyway, and otherwise, I mean, if no production code is changed, I don't see what difference it can make.
Because the… Rakuten Propulsion code will, will behave the same way no matter what, so…
**Douglas Barker** 12:19 Okay, yeah, it's up to you.
**Marc Alff [MySQL]** 12:23 Yeah, don't… so, first thing, don't spend time splitting that in two pieces.
Because it's, It's a… it's a waste of effort, but… and I will try to look at it and see if we can add it then.
**Douglas Barker** 12:36 Okay.
**Marc Alff [MySQL]** 12:47 Yeah, so everything is, I wanted to check if we have… do you know if there are other things that we absolutely need to release?
Which would not be part of that list.
**Douglas Barker** 12:59 So the one that I found on the drop aggregation, there's also a bug fix in there for views, and it's… you know, Tom already took a look, so if that one's close to being approved, I would want to get that in, because it is… one, it's a big performance improvement if you're using drop degradation.
And then if you're using, like, multiple views, there's an easy bug to run into where you actually get duplicate counts. If you have, like, a wildcard view and a specific view, you can easily get into a situation where the storage… the aggregation storage object is duplicated per instrument, and that's not good.
**Marc Alff [MySQL]** 13:37 Okay.
Okay, well, if it's… if it's ready, we can take it, but I'll… I would like to avoid waiting forever, just because of the mass that we have.
**Douglas Barker** 13:49 Yeah.
not critical, so I'd also be okay if we just released what we have.
**Marc Alff [MySQL]** 13:54 Okay, good.
And yes, oh, speaking of triage, I also noticed someone else got interested in OpenTelement triage recently.
So, we have a new guy reporting a lot of things.
I took a quick look, so first of all is, His report is actually very detailed, so he's explaining, okay, what's going on, and the proposed fix, and things like that, so it seems like there is some work behind it.
I need to… to take a look to see, like, oh, is it a real issue, or is it something we can… Which is not an issue because of another reason, or things like that, to see… what is… Well, basically to clarify what is actually a really bug, and what is a misuse, or things like that.
But it's, yeah, it put a lot of effort into it. Oh, sorry.
So, yeah, things like that with the proposed fix. So… I think we can take a look and accept most of them, and possibly, since he knows the fix, ask him to do a PR to fix that.
And since Fusal.
Those reports look like simple issues, so the PR should be easy to review and approve and merge then.
**Douglas Barker** 15:43 Do you agree.
**Marc Alff [MySQL]** 15:49 And yeah, we have… Quite a few to sort out.
There is also all the bug reports from, from this contributor about the HTTP code in general.
So, I didn't have time to look at every single one of them, but in general, what she has been reporting is correct.
So, I think we should pay attention to those.
And the other thing is, she also has quite a few… open PRs.
Yeah, 12 open, and so… it takes time, but I think we can, I don't know how to do it, but at some point we need to dig into that and fix things.
There is this one in particular that I think we should pay attention to, because it's a test case which is flaky today, which is failing CRE once in a while.
And, if she has some improvement on it, That would be better.
**Douglas Barker** 17:02 Yeah, and I know if you go to the discussions tab, Owen has started a discussion about all of these curl bugs and fixes, and requested a design change.
I think that that issue has been filed, so maybe… We can ask Ellen to take a look at the design, and then… if there's a redesign, we'd probably close a lot of these issues, and PRs, I'm guessing.
**Marc Alff [MySQL]** 17:28 Yeah, okay.
on the need discussion, I don't think we have that many. I don't recall.
Don't you remember how to get the label.
Oh, jeez.
Anything in this list that you want to discuss today?
Some are very old.
**Douglas Barker** 18:26 No, I don't think so.
**Marc Alff [MySQL]** 18:28 Okay.
Okay, we should… Probably… Yeah, things, yeah, we know that.
For the old one, we should probably remove the discussed flag then, so that we don't, permit to that again.
And, yeah, reviews. So, one thing you notice also on… CPP will… well, contrib, first of all, yes, it is broken.
So not only we are flooded in CPP, but we are also flooded into… in CPP control.
like, 33 PRs are still outstanding.
The good news, so, You know that someone reported a security vulnerability.
on the web server module, whatever it is, and Lalit fixed it, and the PR has been reviewed and merged, so this thing is out of the way.
I don't know what the next step is, in particular, if we should do a release of CPP Country or not.
So it's… to clarify, so far, we don't have release of every single contributor.
So it's just like people pulling from a given, a given commit.
So, I guess we should check with Lalit also as… see his opinion, whether we should… we need to put a label, now that this reliability is fixed or not.
**Douglas Barker** 20:13 Yeah, I think it's a good question to answer for the security report on how to fully address it now that it's been closed. I think the bigger question for me is, since we don't have code owners for things like the web server, the HTTP.
**Marc Alff [MySQL]** 20:27 Oh, yeah, yeah, that's true.
**Douglas Barker** 20:29 how are we going to manage this going forward? Because I think there's certainly a path, and you see it in the collector and other repositories that have a lot of independent components, where if it doesn't have a code owner, there's a process for deprecation, and then potentially a process for removal, but once a component is deprecated, it's kind of in search of a code owner, and Removed from releases until it has a code owner.
**Marc Alff [MySQL]** 20:58 Yeah.
Yeah, it's definitely a big issue for CPVContribe, and… We've been avoiding that forever, I think.
Because we don't pay too much attention to contribib, Home.
Most of the time during the SIG meeting itself, it's only about CPP. We rarely discuss CPP contribute.
And in any case, yeah, we… Recently, we did some cleanup to actually remove a lot of people from the approvers and maintainers, or approvers mostly.
Lists, because they were just not active at all.
Some of them have been active, like, ages ago, but no activity recently.
But that doesn't solve the problem that, Maintainers for different parts, and we don't have one.
**Douglas Barker** 21:52 Yeah.
**Marc Alff [MySQL]** 21:52 I don't see it.
Yeah, go ahead.
**Douglas Barker** 21:55 Good.
**Marc Alff [MySQL]** 21:58 Yeah, on top of that, CI is breaking in a lot of places, so… Thompson Tomo, started to do some cleanup in CI itself.
Which is great, but just doing the review on that, it's also… takes time to see how CI was done there, and how it needs to be organized, and… And fixed, so it's a… Voice a lot of… A lot of things to… to fix, to get back to a working, Decent working state for contribute.
**Douglas Barker** 22:36 Yeah, and I'm also thinking about it as it's not a one-time fix, so even if it gets fixed now, then somebody needs to be maintaining it, you know, periodically, and then reviewing all these to depend a bot and renovate, update PRs, so… you know, I don't know if those contributors who are contributing to the CI now are actually using these components and may be interested in becoming code owners, but… that's what I would want to, I guess, ask and try to figure out, is do we have a path forward with a code owner, or are we just fixing the CI because we want to get Renovate working?
Beautiful.
**Marc Alff [MySQL]** 23:16 Well, basically, I'm… I'm mostly doing only the second, so every time Inovate says something, I just approve it.
**Douglas Barker** 23:23 Yeah.
**Marc Alff [MySQL]** 23:24 So, things like that, yeah, all those automated things.
I just approved it, I merged it, just to keep CI, floating.
But the… the more important things, like, oh.
adjust code when a dependency is changing an API. Well, that's a code change that needs to be Investigated, done, and things like that, and it's not that simple then.
**Douglas Barker** 23:55 I think it's something…
**Nikhil Bhatia** 23:56 Oh.
**Douglas Barker** 23:56 worth pushing on to find a code owner, especially the web server and the NGINX integration, because these are, if you look at them, they're rather large projects in and of themselves. They could easily be an entire repository by themselves, or entire project by themselves. And, you know, certainly it's outside of the knowledge base of the the main maintainers for OTELCPP, because we know about the extension points and can review the log appenders and the exporters and processors, but… Reviewing and maintaining these entire frameworks, it feels like it's completely outside the scope.
**Marc Alff [MySQL]** 24:33 Oh, yeah, it's a… it's a different story, yes, definitely.
**Douglas Barker** 24:38 Given that, should we.
**Nikhil Bhatia** 24:39 I can…
**Douglas Barker** 24:40 propose a path forward there with these, rather than going down the path of trying to fix and maintain all the CI with them.
**Marc Alff [MySQL]** 24:50 Yes, Nikhil? Yeah.
**Nikhil Bhatia** 24:51 Maybe I can try to, you know, go through it once, and I think contribute to the contrib repo as well.
**Marc Alff [MySQL]** 24:57 Okay.
**Nikhil Bhatia** 24:59 Yeah.
**Marc Alff [MySQL]** 25:00 Did you go through it once?
So, the country repo, there are many different things there. So, it's a collection, in fact, of different countries. So, You don't have to look at all of them, you just can pick one and see how it works.
**Nikhil Bhatia** 25:18 Yeah, sure.
**Marc Alff [MySQL]** 25:19 There are also… there are different things, but yes, that… that will help also, thanks.
**Nikhil Bhatia** 25:25 Yeah.
**Marc Alff [MySQL]** 25:26 And… and one thing that turned out… turned out in that discussion, which is to… Whoa.
Part of fixing CIV was to actually format the code there, and a result of that discussion was that we need an update on CPP build tools itself.
So… become that property.
Yeah, we had a couple of… dependable, changes also recently, I just, just measured that.
But I think the… the issue where, that was discussed is that In CPP, we use only, editor file, as .h, and CPP files as .cc, and nothing else.
But the code format, scenic format also needs to pick up CPP files and HPP headers and things like that, so… Just because of that, even if it's two lines of code to change in the scripts, We need to… First change it into the… the CPP will etoux, repo itself, but then we need to make a new release for that, so that the… the Docker image gets published, and then we can use it in other projects.
So, it's… It's not too complicated to do that, it's just that, I was not actually planning to, to look at that, so it's, One more thing in the grand list of things that we need to address.
On other things which are coming also, I just noticed Weaver did a new release.
from experience, every time Weaver does a new release, you can expect a release of semantic conventions right after that.
Because Weaver is the tooling used by semantic conventions.
So, I think that, typically.
Likely in the next week, we… we can expect a new release of semantic convention.
But we will need to adopt that in, in, OpenTelemetry CPP.
That part itself is not too bad, because the code is generated anyway.
Once in a while, we have to make adjustments to the scripts.
But in general, it's, there is no… not too much work for that, it's, voice.
Low surprises in that codebase.
So it's, it's not a big, big issue.
Alf Anything that I missed that you want to discuss as well?
**Douglas Barker** 29:07 For me, I think we covered everything.
**Marc Alff [MySQL]** 29:10 Okay.
Okay, so I'll try to do, as much as I can to get the next release ready.
Especially the… well, not only we have a lot of changes, but on top of that, there are some duplicated code that we said we will remove in October, I think.
Like, these things?
Yeah, so these things are announced that… so, a couple of flags and whatnot that, we said we will remove starting in October.
So… If we do that in October, I think we should have a release soon enough.
Otherwise, we will have… if we wait, like.
like, mid-September, it doesn't make sense to have a mid-September, and then another one 15 days after that, so… So yeah, just be aware that this is coming as well.
And I've not filed the, the issue for that yet, but I think all the work that Owens did in CMake.
Rename all the auctions we've, hotel CPP something?
The old namings are still supported for now, and I think we should… duplicate that as well, and I was hoping to remove it in the same time frame as everything else.
So if we do that, we should, We should announce it soon, then.
**Douglas Barker** 31:09 That one, we may have to wait up quite a bit longer, because once we remove Right now, it's, like, backwards compatible, so if people have the old options, they'll get a deprecated warning, and then it converts it to the ZoomMate cache for the new option.
If we… if we remove that, then the builds will break. So I think we… we may need to hold on to that… Deprecation, that conversion support, maybe until, like, the next major release or something, but it might be a while.
**Marc Alff [MySQL]** 31:38 Okay, yeah.
Well, that works too, I mean… what I did last time is to… There are so many things that we need to remove.
I picked up a date, like, very far in the future, to say, at this point, there will be removals, and then, plan removal of leaks of Y and Z, to try to group them for the same date. We can also do this, like, and say, for example, like, in 6 months from now, like, in the spring.
We have another release with many removals in them.
And start to… To pick what we announce, what will be removed, like, The road options, maybe, and then, overall… Over preview flags that, are stable and need to be… to go away, things like that.
So yeah, it's, we don't… we don't need to rush it for… for October and for the… For the old LCPP, renaming.
**Douglas Barker** 32:45 Yeah, that makes sense.
**Marc Alff [MySQL]** 32:46 Okay.
Basically, the thing I'm trying to avoid is, one… move all at every release. I prefer to group them together so that it's, it's easier to adapt.
Question for you, do you… What will be the next major cleanup?
But we should take.
Because, well… the configuration, YAML configuration is… is not totally complete yet, but I think it's getting close.
ceiling tidy is getting close, but the only thing remaining is all the code dealing with exceptions.
**Douglas Barker** 34:05 For me, in my projects, like, the biggest one top of mind is gonna be on… still on performance, and there's a big, Something we can do to optimize performance and also improve spec compliance around the logs and traces.
like the multiprocessors. So, we had a PR a while back that's gone stale, but it was to, if you don't have multiple processors, just to use a single processor. That multiprocessor adds quite a bit of overhead.
**Marc Alff [MySQL]** 34:37 Yep.
**Douglas Barker** 34:38 And then it also blocks a use case that came up recently with the span, or log events to span events.
**Marc Alff [MySQL]** 34:46 River Bridge, yes.
**Douglas Barker** 34:47 Yeah, so I think if we can… Allow replacement of those, multiprocessors with, kind of a pipeline-type processor.
We can… we can hopefully get closer to SPEC compliance and improve performance.
**Marc Alff [MySQL]** 35:02 Okay, yeah.
**Douglas Barker** 35:03 That's an area that I'd want to look at.
**Marc Alff [MySQL]** 35:09 Yeah, and everything related to performances will be beneficial for everyone in general.
Myself including, because I also have an app that depends on that.
**Douglas Barker** 35:23 Do you use multiple processors in your app?
**Marc Alff [MySQL]** 35:26 Not multiple processors, well, even though for matrix, I have some weird use case, because… In fact, I have multiple, meter providers.
This is just… the only reason for that is that I have different metrics that are exported with different frequencies.
And the periodic metric exporter just exports everything at once. There is no way to say Those metrics are frequent, and those over-expensive matrix are less frequent.
Things like that.
But no, I don't have multiprocessors for traces.
**Douglas Barker** 36:11 Yeah, so I think that… that could be a nice, nice cleanup. There's still, some work on compliance around the, enable states, like, for metrics, we need to.
**Marc Alff [MySQL]** 36:21 Glorious, yeah.
**Douglas Barker** 36:22 enable, flag, and then do the meter configurator update. So we got the PRs for that, which are pretty close, but I think we can get those into the next release, is what I hope.
**Marc Alff [MySQL]** 36:38 By the way, on… so on… compliant with specs.
Recently, I filed a PR on the configuration repo.
to report the state of the C++ implementation for the YAML config.
So, the… We made quite some progress there, because quite a few things were missing and have been implemented.
But of course, in the meantime, the configuration reports, we invented new properties on new YAML nodes.
So, there is a bit of catch-up to, There is a small catalog to do then.
Bhativouille.
We're getting close, really.
**Douglas Barker** 37:24 Yeah, it's really nice. I'm starting to convert my application over to it, so hopefully deleting a lot of configuration code and using the standard stuff.
**Marc Alff [MySQL]** 37:34 Well, yeah, not only that, but your… You don't need to change the… recompile the application to change the config, which is a massive change.
**Douglas Barker** 37:44 Yep.
**Marc Alff [MySQL]** 37:52 Okay, so, yeah, definitely some focus on spec compliance and performances, yeah.
Sounds like a good, good idea as well.
Okay, and I don't have anything else to discuss, so I will do the… I will file an issue in the community to change the meeting times.
And ping Tom and Lalit to just say there that they agree with it.
Because they will probably need to see all the maintainers there, to, To change the meeting time.
I will send you the PR details.
When Ivored.
Nikhil, any other things you want to discuss?
**Nikhil Bhatia** 38:58 No Marc.
Nothing.
**Marc Alff [MySQL]** 39:00 So, in any case, welcome back.
**Nikhil Bhatia** 39:03 No?
And also, I'll try to… yeah, sorry, go ahead.
**Marc Alff [MySQL]** 39:11 Yes, so if you want to do… Code reviews, and learn a few things, and take ownership of some code.
There is more than enough to do, so… Don't feel shy.
**Nikhil Bhatia** 39:23 Yeah, I'm open to that, Marc.
I'll go through the contribib report, and I'll see what I can take up.
And also, I think my PR was pending from a long time ago on Metrics SDK.
I'll even try to close that up. It's almost been a year since it's been open.
Or else, maybe I'll… I can do one thing that, I can try to close it and reopen it once again.
Because… It's been a long time since I had worked… I have worked on that, so…
**Marc Alff [MySQL]** 40:12 Well, we need to take a look at this.
Yeah, it's one of those, yeah.
The most important thing would be to fix the… The conflicts, because code have changed.
Since then.
And then we can take a look.
whether you fix the conflicts in the same PR, or you apply the change in the new PR, up to you, it doesn't matter, really.
**Nikhil Bhatia** 40:39 Yeah, most probably I'll take up a new PR.
**Marc Alff [MySQL]** 40:42 Okay.
Yep, thanks.
**Nikhil Bhatia** 40:54 Thanks, Mark.
**Marc Alff [MySQL]** 41:00 Alright, Rob, if you don't have anything else, it's, It's a bit late for me here, so… I think we can close the call then.
So… up until proven otherwise, we still have meetings on Mondays and Wednesdays, and once it is official that we move to every Monday.
The calendar will be updated, and then we'll update also the meeting notes.
Veh.
To reflect the new meeting times, so… In doubt, just look at the… Here and in the… in the calendar to see the… what is the meeting time, exactly.
So, Vivet, thanks everyone for joining.
**Douglas Barker** 41:53 Thanks, Mark.
**Marc Alff [MySQL]** 41:55 Thanks, my friend.
**Nikhil Bhatia** 41:56 kinds of deductions.
**Marc Alff [MySQL]** 41:56 Thanks, dude.
**Douglas Barker** 41:56 Nope.
**Marc Alff [MySQL]** 41:57 Thanks, thanks, Nikhil. Yes.
**Douglas Barker** 42:00 Good to see you back.
**Marc Alff [MySQL]** 42:02 Yes.
Okay.
**Nikhil Bhatia** 42:05 Yeah.
**Marc Alff [MySQL]** 42:07 Bye, bye now.
**Douglas Barker** 42:08 Alright guys.
**Nikhil Bhatia** 42:09 like…
